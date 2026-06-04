#!/usr/bin/env python3
"""
Batch URL liveness verification for Deep Research evidence and report files.

Usage:
    # File mode — auto-extracts URLs from evidence or report markdown files
    python verify_urls.py evidence.md
    python verify_urls.py report.md

    # URL mode — pass URLs directly as arguments
    python verify_urls.py "https://example.com/a" "https://example.com/b"

    # Stdin mode — pipe URLs line by line
    echo "https://example.com" | python verify_urls.py --stdin
"""

import asyncio
import os
import re
import sys
from collections import defaultdict
from urllib.parse import urlparse

import httpx

# --- Configuration ---
GLOBAL_CONCURRENCY = 40  # Max total concurrent connections
PER_HOST_CONCURRENCY = 5  # Max concurrent connections per domain
TIMEOUT = httpx.Timeout(connect=5.0, read=5.0, write=5.0, pool=5.0)
USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/125.0.0.0 Safari/537.36"
)
HEADERS = {
    "User-Agent": USER_AGENT,
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
}

# Status codes that indicate HEAD is not supported → retry with GET
HEAD_UNSUPPORTED_CODES = (405, 501)
# Status codes that might be anti-bot on HEAD → retry with GET
HEAD_BLOCKED_CODES = (403, 406, 429)
# Status codes where HEAD is unreliable (some sites return 404 for HEAD but 200 for GET)
HEAD_UNRELIABLE_CODES = (404,)

# Anti-bot detection signals in response body (lowercase)
ANTIBOT_SIGNALS = [
    "captcha", "challenge", "cloudflare", "cf-browser",
    "access denied", "forbidden", "please verify",
    "robot", "bot detect", "human verification",
    "login", "sign in", "subscribe", "paywall",
    "enable javascript", "enable cookies",
    "unusual traffic", "rate limit",
]


def extract_urls_from_file(filepath: str) -> list[str]:
    """Extract URLs from a markdown file (supports evidence and report formats)."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    urls = set()

    # Universal pattern: any https:// or http:// URL in the file
    for match in re.finditer(r"https?://[^\s)\]>\"']+", content):
        url = match.group(0).rstrip(".,;:!?")  # strip trailing punctuation
        urls.add(url)

    return sorted(urls)


async def check_url(
    client: httpx.AsyncClient,
    url: str,
    host_semaphores: dict,
    global_sem: asyncio.Semaphore,
) -> tuple[str, int | str, bool]:
    """
    Verify a single URL.
    Returns (url, status_code_or_error, has_antibot_signal).
    """
    host = urlparse(url).netloc
    if host not in host_semaphores:
        host_semaphores[host] = asyncio.Semaphore(PER_HOST_CONCURRENCY)
    host_sem = host_semaphores[host]

    async with global_sem:
        async with host_sem:
            try:
                # First attempt: HEAD
                resp = await client.head(url, follow_redirects=True)
                head_code = resp.status_code

                # HEAD not supported, blocked, or unreliable → fallback to GET (can inspect body)
                if head_code in HEAD_UNSUPPORTED_CODES or head_code in HEAD_BLOCKED_CODES or head_code in HEAD_UNRELIABLE_CODES:
                    resp = await client.get(url, follow_redirects=True)
                    get_code = resp.status_code
                    # Check response body for anti-bot signals
                    has_signal = _detect_antibot(resp)
                    return url, get_code, has_signal

                return url, head_code, False

            except httpx.TimeoutException:
                return url, "TIMEOUT", False
            except httpx.ConnectError:
                return url, "CONNECT_ERROR", False
            except httpx.TooManyRedirects:
                return url, "TOO_MANY_REDIRECTS", False
            except Exception as e:
                return url, f"ERROR:{type(e).__name__}", False


def _detect_antibot(resp: httpx.Response) -> bool:
    """Detect anti-bot signals from response headers and body."""
    # Check common anti-bot headers
    headers_lower = {k.lower(): v.lower() for k, v in resp.headers.items()}

    # Cloudflare
    if "cf-ray" in headers_lower or "cf-cache-status" in headers_lower:
        if resp.status_code in (403, 429, 503):
            return True

    # Generic WAF / challenge headers
    if "x-robots-tag" in headers_lower:
        return True

    # Check body content (read first 2KB to avoid memory issues)
    try:
        body_preview = resp.text[:2048].lower()
    except Exception:
        return False

    signal_count = sum(1 for sig in ANTIBOT_SIGNALS if sig in body_preview)
    # 2+ signals → high confidence it's anti-bot, not a real 403/404
    return signal_count >= 2


def classify_result(url: str, status: int | str, has_antibot: bool, host_results: dict) -> str:
    """
    Classify into PASS / FAIL / UNCERTAIN using behavioral signals.

    Strategies:
    1. Status-based: 2xx/3xx=PASS, 404/410=definite FAIL
    2. Anti-bot body detection: response contains challenge/captcha signals → UNCERTAIN
    3. Host-level aggregation: if ALL URLs from same host got 403 → likely anti-bot → UNCERTAIN
    """
    # Non-numeric errors
    if isinstance(status, str):
        # TIMEOUT means server exists but is slow → treat as accessible
        if status == "TIMEOUT":
            return "UNCERTAIN"
        return "FAIL"

    # 2xx, 3xx → PASS
    if 200 <= status < 400:
        return "PASS"

    # 404, 410 → definite dead link, no ambiguity
    if status in (404, 410):
        return "FAIL"

    # For 401, 403, 429, 503 — check anti-bot signals
    if status in (401, 403, 429, 503):
        # Signal 1: Response body contains anti-bot markers
        if has_antibot:
            return "UNCERTAIN"

        # Signal 2: Host-level pattern — all URLs from this host got blocked
        host = urlparse(url).netloc
        host_statuses = host_results.get(host, [])
        if host_statuses:
            all_blocked = all(
                isinstance(s, int) and s in (401, 403, 429, 503)
                for s in host_statuses
            )
            if all_blocked and len(host_statuses) >= 1:
                return "UNCERTAIN"

        # Signal 3: 403 specifically — server is alive, just refusing us
        if status == 403:
            return "UNCERTAIN"

    # Non-standard status codes (not in HTTP spec) → site is alive with custom logic
    if status >= 400 and status not in (404, 410, 400, 405, 500, 502, 503, 504):
        return "UNCERTAIN"

    # Other standard 4xx/5xx → FAIL
    return "FAIL"


def format_result(url: str, status: int | str, classification: str) -> str:
    """Format a single result line for LLM-friendly output."""
    icons = {"PASS": "✅", "FAIL": "❌", "UNCERTAIN": "⚠️"}
    icon = icons[classification]

    if classification == "UNCERTAIN":
        if status == "TIMEOUT":
            return f"{icon} {status} {url} (server slow but likely accessible)"
        return f"{icon} {status} {url} (likely anti-bot, URL probably valid)"
    return f"{icon} {status} {url}"


async def main(urls: list[str]) -> int:
    """Run batch verification. Returns exit code (0=all pass, 1=some failed)."""
    if not urls:
        print("No URLs provided.")
        return 0

    # Deduplicate while preserving order
    seen = set()
    unique_urls = []
    for u in urls:
        u = u.strip()
        if u and u not in seen:
            seen.add(u)
            unique_urls.append(u)

    print(f"Verifying {len(unique_urls)} unique URLs...\n")

    global_sem = asyncio.Semaphore(GLOBAL_CONCURRENCY)
    host_semaphores: dict[str, asyncio.Semaphore] = defaultdict(
        lambda: asyncio.Semaphore(PER_HOST_CONCURRENCY)
    )

    async with httpx.AsyncClient(
        timeout=TIMEOUT,
        headers=HEADERS,
    ) as client:
        tasks = [
            check_url(client, url, host_semaphores, global_sem)
            for url in unique_urls
        ]
        results = await asyncio.gather(*tasks)

    # Build host-level result map for aggregation-based detection
    host_results: dict[str, list] = defaultdict(list)
    for url, status, _ in results:
        host = urlparse(url).netloc
        host_results[host].append(status)

    # Classify and output
    pass_count = 0
    fail_count = 0
    uncertain_count = 0

    for url, status, has_antibot in results:
        classification = classify_result(url, status, has_antibot, host_results)
        print(format_result(url, status, classification))
        if classification == "PASS":
            pass_count += 1
        elif classification == "UNCERTAIN":
            uncertain_count += 1
        else:
            fail_count += 1

    print("---")
    print(
        f"TOTAL: {pass_count + fail_count + uncertain_count} | "
        f"PASS: {pass_count} | FAIL: {fail_count} | UNCERTAIN: {uncertain_count}"
    )

    return 0 if fail_count == 0 else 1


if __name__ == "__main__":
    args = [arg for arg in sys.argv[1:] if not arg.startswith("--")]
    stdin_mode = "--stdin" in sys.argv

    if stdin_mode:
        urls = [line.strip() for line in sys.stdin if line.strip()]
    elif len(args) == 1 and os.path.isfile(args[0]):
        # File mode: extract URLs from the file
        urls = extract_urls_from_file(args[0])
    else:
        # URL mode: arguments are URLs
        urls = args

    exit_code = asyncio.run(main(urls))
    sys.exit(exit_code)
