#!/usr/bin/env python3
"""
topic_tracking guide v2.

This is a clean event-level flow kept next to the legacy guide.py. It avoids the
old article-level draft_list -> validation split and asks the agent to submit
only events that are good enough to enter the briefing.
"""

import argparse
import hashlib
import html
import json
import os
import re
import shutil
import subprocess
import sys
import urllib.request
import urllib.parse
import uuid
from datetime import date, datetime, timedelta


SCRIPT_PATH = os.path.abspath(__file__)
SCRIPT_DIR = os.path.dirname(SCRIPT_PATH)
SKILL_DIR = os.path.dirname(SCRIPT_DIR)
SESSIONS_DIR = os.path.join(SKILL_DIR, "sessions_v2")
STATE_DIR = os.path.join(SESSIONS_DIR, "_states")
SCRIPT_CMD = f"python {SCRIPT_PATH}"

DEFAULT_TRACKING_ROOT = "/app/data/所有对话/主对话/热点资讯追踪"
TOOLS_PATH = "/app/data/所有对话/主对话/基础设定TOOLS.md"
EVENT_FRESHNESS_HOURS = 48
EVENT_FRESHNESS_DAYS = max(1, (EVENT_FRESHNESS_HOURS + 23) // 24)
URL_PATTERN = re.compile(r"^https?://\S+")
URL_CHECK_TIMEOUT = 10
URL_CACHE_TTL_HOURS = 24
MIN_PAGE_TEXT_LENGTH = 200
URL_CHECK_USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
)
SOFT_404_KEYWORDS = ["404", "not found", "页面找不到", "页面不存在", "页面已删除", "内容已下线"]
JS_CHALLENGE_KEYWORDS = ["byted_acrawler", "__ac_signature", "_$jsvmprt"]
JS_CHALLENGE_REACHABLE_HOSTS = []
BLOCKED_SUPPORT_URL_DOMAINS = [
    # 技术搬运/SEO
    "csdn.net", "iteye.com", "oschina.net",
    # 个人博客/笔记
    "jianshu.com", "bokeyuan.com", "cnblogs.com",
    # 文库/文档站
    "wenku.baidu.com", "doc88.com", "docin.com", "360doc.com", "ishare.iask.sina.com",
    # 百度系低质
    "baijiahao.baidu.com", "zhidao.baidu.com", "jingyan.baidu.com", "tieba.baidu.com",
    # 问答/论坛
    "zhihu.com", "segmentfault.com", "v2ex.com",
    # 短视频/社交/低质聚合
    "douyin.com", "kuaishou.com", "weibo.com", "xiaohongshu.com", "toutiao.com",
    # 电商/营销
    "jd.com", "taobao.com", "tmall.com", "pinduoduo.com",
    # 其他低质
    "myzaker.com", "xueqiu.com",
]
SOURCE_TYPES = ["cross_valid", "official", "coze"]
SOURCE_TYPE_ALIASES = {
    "cross_valid": "cross_valid",
    "cross_verified": "cross_valid",
    "official": "official",
    "coze": "coze",
}
CROSS_VALID_MIN_URLS = 3
AUTHORITY_REQUIREMENTS = ["high", "low"]
TARGET_EVENT_GROUPS = 5
RELEVANCE_LEVELS = ["不相关", "弱相关", "强相关"]

SETUP_STEPS = ["S1", "S2"]
BRIEFING_STEPS = ["B1", "B2", "B3", "B4"]
STEP_TITLES = {
    "S1": "理解话题并写入追踪设定",
    "S2": "试运行与日程设置",
    "B1": "恢复上下文",
    "B2": "阅读资讯并聚合事件",
    "B3": "生成本期日报",
    "B4": "收尾摘要",
}

TOOLS_RULE_BLOCK = """<!-- topic_tracking_delivery_rule:start -->
## 扣子话题追踪日报交付规则

日程追踪系列的日报必须以日程/子会话严格筛选、验证、去重和时效性检查后的产物为最终结论。
主会话收到日程/子会话最终重复的信息后，必须直接按其中的 computer:// 日报文件交付给用户。
主会话严禁再次搜索、补充来源、重写事实、重新筛选、合并其他信息，或为了凑数量补充未验证内容。
如果日报新闻数量较少，说明这是严格筛选后的高质量结果；不得放宽标准。
如果日程/子会话结论是暂无最新动态，主会话必须只向用户说明“该话题暂时没有监测到最新动态”，不得自行补搜、不得建议放宽时效性或筛选标准、不得添油加醋解释。
主会话可以根据用户偏好微调交付时的表达形式，但不得改变日报事实、结论、来源、排序和取舍。
对用户只呈现本期结果和日报，不暴露 token、run_label、阶段名、JSON 文件名或内部目录。
<!-- topic_tracking_delivery_rule:end -->
"""


def _new_token(prefix):
    return f"{prefix}_{uuid.uuid4().hex[:8]}"


def _safe_name(value):
    value = (value or "").strip()
    value = re.sub(r"[\\/:*?\"<>|]+", "_", value)
    value = re.sub(r"\s+", " ", value)
    return value[:120] or "未命名话题"


def _default_tracking_dir(topic):
    return os.path.abspath(os.path.join(DEFAULT_TRACKING_ROOT, _safe_name(topic)))


def _state_path(token):
    return os.path.join(STATE_DIR, f"{token}.json")


def _session_dir(st):
    if st.get("session_dir"):
        return st["session_dir"]
    token = st["token"]
    if st.get("flow") == "briefing" and st.get("setup_token"):
        return os.path.join(SESSIONS_DIR, st["setup_token"], token)
    return os.path.join(SESSIONS_DIR, token)


def _contract_path(tracking_dir):
    return os.path.join(tracking_dir, "tracking_contract_v2.json")


def _briefing_md_path(tracking_dir, topic, run_label):
    return os.path.join(tracking_dir, f"{_safe_name(topic)}_{run_label}.md")


def _low_volume_confirmation_path(tracking_dir, run_label):
    return os.path.join(tracking_dir, f"{run_label}_event_list_confirmation.json")


def _event_url_blacklist_path(tracking_dir, run_label):
    return os.path.join(tracking_dir, f"{run_label}_event_url_blacklist.json")


def _briefing_artifact_exists(tracking_dir, label):
    if not tracking_dir:
        return False
    patterns = [
        f"{label}_event_list.json",
        f"{label}_summary.json",
        f"*_{label}.md",
    ]
    for pattern in patterns:
        if any(os.path.exists(os.path.join(tracking_dir, p)) for p in _glob_names(tracking_dir, pattern)):
            return True
    return False


def _glob_names(directory, pattern):
    import glob

    return [os.path.basename(p) for p in glob.glob(os.path.join(directory, pattern))]


def _next_run_label(tracking_dir, day):
    for index in range(1, 100):
        label = day if index == 1 else f"{day}_v{index}"
        if not _briefing_artifact_exists(tracking_dir, label):
            return label
    return f"{day}_v{uuid.uuid4().hex[:4]}"


def _read_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def _read_json_if_exists(path):
    if not path or not os.path.exists(path):
        return None
    try:
        return _read_json(path)
    except (json.JSONDecodeError, UnicodeDecodeError, OSError):
        return None


def _write_json(path, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def _json_list_count(path):
    data = _read_json_if_exists(path)
    if isinstance(data, list):
        return len(data)
    return None


def _url_cache_path(cache_dir, url):
    if not cache_dir:
        return None
    digest = hashlib.sha256(url.encode("utf-8")).hexdigest()
    return os.path.join(cache_dir, f"{digest}.json")


def _read_url_cache(cache_dir, url):
    path = _url_cache_path(cache_dir, url)
    if not path or not os.path.exists(path):
        return None
    try:
        data = _read_json(path)
        fetched_at = datetime.fromisoformat(data.get("fetched_at", ""))
        if datetime.now() - fetched_at > timedelta(hours=URL_CACHE_TTL_HOURS):
            return None
        if data.get("url") != url:
            return None
        return bool(data.get("reachable")), data.get("page_text", "")
    except (json.JSONDecodeError, UnicodeDecodeError, OSError, ValueError, TypeError):
        return None


def _write_url_cache(cache_dir, url, result):
    path = _url_cache_path(cache_dir, url)
    if not path:
        return
    reachable, page_text = result
    try:
        _write_json(path, {
            "url": url,
            "reachable": bool(reachable),
            "page_text": page_text or "",
            "fetched_at": datetime.now().isoformat(),
        })
    except OSError:
        pass


def _html_to_text(raw_html):
    raw_html = re.sub(r"(?is)<script[^>]*>.*?</script>", " ", raw_html or "")
    raw_html = re.sub(r"(?is)<style[^>]*>.*?</style>", " ", raw_html)
    raw_html = re.sub(r"(?is)<[^>]+>", " ", raw_html)
    text = html.unescape(raw_html)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def _is_known_js_challenge(raw_html, url):
    if not raw_html:
        return False
    host = _url_host(url)
    if not any(host == item or host.endswith("." + item) for item in JS_CHALLENGE_REACHABLE_HOSTS):
        return False
    return any(keyword in raw_html for keyword in JS_CHALLENGE_KEYWORDS)


def _is_known_dynamic_article_url(url):
    host = _url_host(url)
    if not any(host == item or host.endswith("." + item) for item in JS_CHALLENGE_REACHABLE_HOSTS):
        return False
    try:
        path = urllib.parse.urlparse(url).path
    except Exception:
        return False
    return re.match(r"^/(group|article)/\d+/?$", path or "") is not None


def _js_challenge_marker(url):
    host = _url_host(url) or "unknown-host"
    return (
        f"reachable js challenge page from {host}; "
        "urllib cannot extract article body, but the HTTP page responded with a known anti-bot challenge. "
        * 4
    ).strip()


def _dynamic_article_marker(url):
    host = _url_host(url) or "unknown-host"
    return (
        f"reachable dynamic article url from {host}; "
        "local Python networking could not fetch the body, but this known article URL pattern should not be treated as a soft 404. "
        * 4
    ).strip()


def _page_text_result_from_raw(url, raw):
    if _is_known_js_challenge(raw, url):
        return True, _js_challenge_marker(url)
    page_text = _html_to_text(raw)
    metadata_text = _extract_html_time_metadata(raw)
    if metadata_text:
        page_text = f"{metadata_text} {page_text}".strip()
    low = page_text[:3000].lower()
    soft_404 = any(keyword in low for keyword in SOFT_404_KEYWORDS)
    return len(page_text) >= MIN_PAGE_TEXT_LENGTH and not soft_404, page_text


def _fetch_page_text_with_curl(url):
    try:
        proc = subprocess.run(
            [
                "curl",
                "-L",
                "--max-time",
                str(URL_CHECK_TIMEOUT),
                "-A",
                URL_CHECK_USER_AGENT,
                url,
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            timeout=URL_CHECK_TIMEOUT + 3,
            check=False,
        )
        if proc.returncode != 0:
            return False, ""
        raw = proc.stdout.decode("utf-8", errors="ignore")
        return _page_text_result_from_raw(url, raw)
    except Exception:
        return False, ""


def _extract_html_time_metadata(raw_html):
    if not raw_html:
        return ""

    snippets = []
    patterns = [
        r'<meta[^>]+(?:property|name)=["\'](?:article:published_time|datePublished|publishDate|pubdate|publishTime)["\'][^>]+content=["\']([^"\']+)["\']',
        r'<meta[^>]+content=["\']([^"\']+)["\'][^>]+(?:property|name)=["\'](?:article:published_time|datePublished|publishDate|pubdate|publishTime)["\']',
        r'"(?:datePublished|publishDate|pubdate|publishTime)"\s*:\s*"([^"]+)"',
    ]
    for pattern in patterns:
        for match in re.finditer(pattern, raw_html, flags=re.IGNORECASE):
            value = match.group(1).strip()
            if value and value not in snippets:
                snippets.append(value)
    return " ".join(snippets)


def _fetch_page_text(url, cache_dir=None):
    cached = _read_url_cache(cache_dir, url)
    if cached is not None:
        return cached

    try:
        req = urllib.request.Request(url, headers={"User-Agent": URL_CHECK_USER_AGENT})
        with urllib.request.urlopen(req, timeout=URL_CHECK_TIMEOUT) as resp:
            content_type = resp.headers.get("Content-Type", "")
            if content_type and not any(t in content_type.lower() for t in ["text", "html", "json", "xml"]):
                result = (False, "")
            else:
                charset = resp.headers.get_content_charset() or "utf-8"
                raw = resp.read(2_000_000).decode(charset, errors="ignore")
                final_url = resp.geturl() or url
                result = _page_text_result_from_raw(final_url, raw)
    except Exception:
        result = _fetch_page_text_with_curl(url)
        if not result[0] and _is_known_dynamic_article_url(url):
            result = (True, _dynamic_article_marker(url))

    _write_url_cache(cache_dir, url, result)
    return result


def _canonical_url(url):
    if not isinstance(url, str):
        return ""
    return url.strip().split("#", 1)[0].rstrip("/")


def _ordered_unique_urls(urls):
    seen = set()
    result = []
    for url in urls:
        key = _canonical_url(url)
        if key and key not in seen:
            seen.add(key)
            result.append(url.strip())
    return result


def _url_host(url):
    try:
        return urllib.parse.urlparse(url).netloc.lower().split("@")[-1].split(":")[0]
    except Exception:
        return ""


def _is_coze_url(url):
    host = _url_host(url)
    return host == "coze.cn" or host.endswith(".coze.cn")


def _blocked_support_url_reason(url):
    host = _url_host(url)
    for domain in BLOCKED_SUPPORT_URL_DOMAINS:
        if host == domain or host.endswith("." + domain):
            return f"{domain} 属于低质量或可追溯性不足的来源域名，不可作为 support_url"
    return ""


def _format_blocked_support_domains():
    return "、".join(sorted(BLOCKED_SUPPORT_URL_DOMAINS))


PRECISE_TIMESTAMP_PATTERNS = [
    re.compile(
        r"(?P<year>20\d{2})\s*年\s*(?P<month>\d{1,2})\s*月\s*"
        r"(?P<day>\d{1,2})\s*日?\s*(?P<hour>\d{1,2})[:：](?P<minute>\d{2})"
    ),
    re.compile(
        r"(?P<year>20\d{2})[-/.](?P<month>\d{1,2})[-/.](?P<day>\d{1,2})"
        r"(?:\s+|T|　)+(?P<hour>\d{1,2})[:：](?P<minute>\d{2})"
    ),
]


def _extract_precise_page_timestamps(page_text):
    if not page_text:
        return []

    results = []
    seen = set()
    for pattern in PRECISE_TIMESTAMP_PATTERNS:
        for match in pattern.finditer(page_text):
            raw = match.group(0).strip()
            if raw in seen:
                continue
            seen.add(raw)
            try:
                parsed = datetime(
                    int(match.group("year")),
                    int(match.group("month")),
                    int(match.group("day")),
                    int(match.group("hour")),
                    int(match.group("minute")),
                )
            except ValueError:
                continue
            results.append((match.start(), parsed, raw))
    return sorted(results, key=lambda item: item[0])


def _parse_event_time(value):
    return datetime.strptime(value.strip(), "%Y-%m-%d %H:%M")


def _normalize_source_type(value):
    if not isinstance(value, str) or not value.strip():
        return "cross_valid"
    return SOURCE_TYPE_ALIASES.get(value.strip(), "")


def _normalize_authority_requirement(value):
    if isinstance(value, str) and value.strip().lower() in AUTHORITY_REQUIREMENTS:
        return value.strip().lower()
    return "high"


def _support_url_min_count(authority_requirement):
    return 1 if _normalize_authority_requirement(authority_requirement) == "low" else CROSS_VALID_MIN_URLS


def _contract_authority_requirement(tracking_dir):
    contract = _read_json_if_exists(_contract_path(tracking_dir)) if tracking_dir else None
    if isinstance(contract, dict):
        return _normalize_authority_requirement(contract.get("authority_requirement"))
    return "high"


def _event_group_label(index, item):
    if isinstance(item, dict):
        group_events = item.get("events")
        if isinstance(group_events, list) and group_events:
            first = group_events[0]
            if isinstance(first, dict):
                event = first.get("event")
                if isinstance(event, str) and event.strip():
                    return f"第{index}组/{event.strip()}"
    return f"第{index}组"


def _event_entry_label(group_index, event_index, event_obj):
    if isinstance(event_obj, dict):
        event = event_obj.get("event")
        if isinstance(event, str) and event.strip():
            return f"第{group_index}组第{event_index}个事件/{event.strip()}"
    return f"第{group_index}组第{event_index}个事件"


def _event_count_from_data(event_list):
    if not isinstance(event_list, list):
        return None
    count = 0
    for group in event_list:
        if not isinstance(group, dict):
            continue
        group_events = group.get("events")
        if isinstance(group_events, list):
            count += len([item for item in group_events if isinstance(item, dict)])
    return count


def _event_count_from_file(path):
    return _event_count_from_data(_read_json_if_exists(path))


def _validate_low_volume_confirmation(data, group_count):
    if group_count >= TARGET_EVENT_GROUPS:
        return None
    if not isinstance(data, dict):
        return (
            f"事件组数量为 {group_count}，少于目标 {TARGET_EVENT_GROUPS} 组。"
            "请继续补搜；如确认近期确实不足，请按下方提示写入 event_list_confirmation.json。"
        )
    if data.get("confirmed") is not True:
        return (
            f"事件组数量为 {group_count}，少于目标 {TARGET_EVENT_GROUPS} 组。"
            "event_list_confirmation.json 必须包含 confirmed=true。"
        )
    reason = data.get("reason")
    if not isinstance(reason, str) or len(reason.strip()) < 10:
        return f"event_list_confirmation.json 的 reason 至少需要 10 个字符，说明为什么少于 {TARGET_EVENT_GROUPS} 个事件组仍可进入下一步。"
    search_summary = data.get("search_summary")
    if not isinstance(search_summary, list) or not any(isinstance(item, str) and item.strip() for item in search_summary):
        return "event_list_confirmation.json 需要提供 search_summary 数组，说明已经补搜过哪些方向或来源。"
    return None


def _low_volume_confirmation_guide(path):
    return f"""少于 {TARGET_EVENT_GROUPS} 个事件组时，请先继续补搜不同关键词、不同来源和更接近源头的 URL。
如果确认近期确实不足，写入确认文件：

{path}

JSON 格式：

{{
  "confirmed": true,
  "reason": "为什么本期少于 {TARGET_EVENT_GROUPS} 个事件组仍然是合理结果",
  "search_summary": ["已经补搜过的关键词、方向或来源"]
}}"""


def _load_url_blacklist(path):
    data = _read_json_if_exists(path)
    if not isinstance(data, list):
        return {}
    result = {}
    for item in data:
        if not isinstance(item, dict):
            continue
        key = item.get("canonical_url")
        if isinstance(key, str) and key:
            result[key] = item
    return result


def _blacklist_entries_for_urls(urls, *, reason, label, detail):
    entries = []
    for url in urls:
        if not isinstance(url, str) or not URL_PATTERN.match(url):
            continue
        key = _canonical_url(url)
        if not key:
            continue
        entries.append({
            "url": url.strip(),
            "canonical_url": key,
            "reason": reason,
            "label": label,
            "detail": detail,
            "created_at": datetime.now().isoformat(),
        })
    return entries


def _append_url_blacklist(path, entries):
    if not path or not entries:
        return 0
    existing = _read_json_if_exists(path)
    if not isinstance(existing, list):
        existing = []
    by_key = {}
    for item in existing:
        if isinstance(item, dict) and isinstance(item.get("canonical_url"), str):
            by_key[item["canonical_url"]] = item
    added = 0
    for item in entries:
        key = item.get("canonical_url")
        if not key or key in by_key:
            continue
        by_key[key] = item
        added += 1
    if added:
        _write_json(path, list(by_key.values()))
    return added


def _validate_event_list(
    event_groups,
    *,
    cache_dir=None,
    low_volume_confirmation=None,
    url_blacklist_path=None,
    authority_requirement="high",
):
    now = datetime.now()
    window_start = now - timedelta(hours=EVENT_FRESHNESS_HOURS)
    errors = []
    new_blacklist_entries = []
    url_blacklist = _load_url_blacklist(url_blacklist_path)
    authority_requirement = _normalize_authority_requirement(authority_requirement)
    min_support_urls = _support_url_min_count(authority_requirement)

    if not isinstance(event_groups, list):
        return {
            "pass": False,
            "error_count": 1,
            "errors": ["event_list 顶层必须是数组"],
        }

    seen_urls = {}
    events_by_time = {}
    low_volume_error = _validate_low_volume_confirmation(low_volume_confirmation, len(event_groups))
    if low_volume_error:
        errors.append(low_volume_error)

    for index, item in enumerate(event_groups, start=1):
        label = _event_group_label(index, item)
        if not isinstance(item, dict):
            errors.append(f"[第{index}组] 必须是对象")
            continue

        for field in ["events", "support_urls", "source_type", "relevance_with_topic"]:
            if field not in item:
                errors.append(f"[{label}] 缺少必要字段: {field}")

        group_events = item.get("events")
        if not isinstance(group_events, list) or not group_events:
            errors.append(f"[{label}] events 必须是非空数组；找不到合格事件时请让 event_list 顶层写空数组 []")
            group_events = []

        raw_source_type = item.get("source_type", "cross_valid")
        source_type = _normalize_source_type(raw_source_type)
        if not source_type:
            errors.append(f"[{label}] source_type 只能是 {SOURCE_TYPES} 之一")
            source_type = "cross_valid"

        support_urls = item.get("support_urls")
        unique_urls = []
        support_page_times = []
        if not isinstance(support_urls, list):
            errors.append(f"[{label}] support_urls 必须是 URL 字符串数组")
        else:
            unique_urls = _ordered_unique_urls(support_urls)
            valid_url_items = [url for url in support_urls if isinstance(url, str) and URL_PATTERN.match(url)]
            if len(unique_urls) != len(valid_url_items):
                errors.append(f"[{label}] support_urls 组内有重复 URL；请先去重")
            for url in unique_urls:
                key = _canonical_url(url)
                if key in seen_urls:
                    errors.append(f"[{label}] support_url 与 {seen_urls[key]} 重复: {url}；同一个 URL 全局只能出现在一个事件组")
                else:
                    seen_urls[key] = label

            for url in unique_urls:
                blocked_reason = _blocked_support_url_reason(url)
                if blocked_reason:
                    errors.append(f"[{label}] support_url 来源域名质量低，不采用：{url}；{blocked_reason}。请更换为官方、权威媒体或更可追溯的来源。")

            for url in unique_urls:
                key = _canonical_url(url)
                if key in url_blacklist:
                    entry = url_blacklist[key]
                    errors.append(
                        f"[{label}] support_url 命中本次黑名单，严禁通过改时效性或相关性重新使用：{url}。"
                        f"首次拉黑原因：{entry.get('reason', 'unknown')}；"
                        f"上下文：{entry.get('label', '')}；详情：{entry.get('detail', '')}。"
                        "请更换事件组和来源 URL。"
                    )

            single_coze_url = len(unique_urls) == 1 and _is_coze_url(unique_urls[0])
            if len(unique_urls) < min_support_urls:
                errors.append(
                    f"[{label}] 当前话题要求 support_urls 至少需要 {min_support_urls} 个不同且可达的 URL；"
                    "如果找不到足够可靠支撑，请更换事件组，不要降低来源要求。"
                )
            if source_type == "coze":
                has_coze_url = any(_is_coze_url(url) for url in unique_urls)
                if min_support_urls == 1 and not single_coze_url:
                    errors.append(f"[{label}] source_type=coze 且当前话题只要求 1 条来源时，support_urls 必须且只能包含 1 个 coze.cn URL")
                elif min_support_urls > 1 and not has_coze_url:
                    errors.append(f"[{label}] source_type=coze 时，support_urls 至少需要包含 1 个 coze.cn URL")
            for url in support_urls:
                if not isinstance(url, str) or not URL_PATTERN.match(url):
                    errors.append(f"[{label}] support_urls 包含无效 URL: {url}")
            for url in unique_urls:
                if _blocked_support_url_reason(url):
                    continue
                reachable, page_text = _fetch_page_text(url, cache_dir=cache_dir)
                if not reachable:
                    errors.append(f"[{label}] support_url 不可达或疑似软404: {url}")
                    continue
                timestamps = _extract_precise_page_timestamps(page_text)
                if timestamps:
                    _, page_time, raw_time = timestamps[0]
                    support_page_times.append((url, page_time, raw_time))

        relevance_with_topic = item.get("relevance_with_topic")
        if not isinstance(relevance_with_topic, str) or len(relevance_with_topic.strip()) < 10:
            errors.append(f"[{label}] relevance_with_topic 必须是至少 10 个字符的字符串，说明该事件组为什么强相关于当前话题")

        for event_index, event_obj in enumerate(group_events, start=1):
            event_label = _event_entry_label(index, event_index, event_obj)
            if not isinstance(event_obj, dict):
                errors.append(f"[第{index}组第{event_index}个事件] 必须是对象")
                continue
            for field in ["event", "event_time", "relevance_level"]:
                if field not in event_obj:
                    errors.append(f"[{event_label}] 缺少必要字段: {field}")
            if not isinstance(event_obj.get("event"), str) or len(event_obj.get("event", "").strip()) < 5:
                errors.append(f"[{event_label}] event 需要至少 5 个字符")

            relevance_level = event_obj.get("relevance_level")
            if not isinstance(relevance_level, str) or not relevance_level.strip():
                errors.append(f"[{event_label}] relevance_level 必填，且只能是 {RELEVANCE_LEVELS} 之一")
            elif relevance_level not in RELEVANCE_LEVELS:
                errors.append(f"[{event_label}] relevance_level='{relevance_level}' 无效，只能是 {RELEVANCE_LEVELS}；请更换事件，不要把弱相关改成强相关硬过")
                new_blacklist_entries.extend(_blacklist_entries_for_urls(
                    unique_urls,
                    reason="relevance",
                    label=event_label,
                    detail=f"relevance_level 无效: {relevance_level}",
                ))
            elif relevance_level != "强相关":
                errors.append(f"[{event_label}] relevance_level={relevance_level}，只有强相关事件允许通过；请更换事件，不要把弱相关/不相关强行改成强相关")
                new_blacklist_entries.extend(_blacklist_entries_for_urls(
                    unique_urls,
                    reason="relevance",
                    label=event_label,
                    detail=f"relevance_level={relevance_level}",
                ))

            event_time = event_obj.get("event_time")
            if not isinstance(event_time, str) or not event_time.strip():
                errors.append(f"[{event_label}] event_time 不能为空；不确定时不要提交该事件")
                continue
            try:
                parsed = _parse_event_time(event_time)
                event_time_key = parsed.strftime("%Y-%m-%d %H:%M")
                events_by_time.setdefault(event_time_key, []).append({
                    "label": event_label,
                    "event": event_obj.get("event", ""),
                    "confirmed": event_obj.get("time_duplicate_confirmed") is True,
                    "note": event_obj.get("time_duplicate_note", ""),
                })
                if parsed < window_start:
                    errors.append(
                        f"[{event_label}] event_time 超出最近 {EVENT_FRESHNESS_HOURS} 小时范围，"
                        f"该事件不符合本期要求；最早允许 {window_start.strftime('%Y-%m-%d %H:%M')}。"
                        "请删除此事件并寻找其他符合时效的新事件，严禁把旧事件时间改新来通过校验。"
                    )
                    new_blacklist_entries.extend(_blacklist_entries_for_urls(
                        unique_urls,
                        reason="freshness",
                        label=event_label,
                        detail=f"event_time={event_time} 早于最早允许时间 {window_start.strftime('%Y-%m-%d %H:%M')}",
                    ))
                if parsed - now > timedelta(minutes=10):
                    errors.append(f"[{event_label}] event_time 不能是未来时间；请核实来源，不要编造或调整事件时间。")
                    new_blacklist_entries.extend(_blacklist_entries_for_urls(
                        unique_urls,
                        reason="freshness",
                        label=event_label,
                        detail=f"event_time={event_time} 是未来时间",
                    ))
                fresh_page_times = [
                    (url, page_time, raw_time)
                    for url, page_time, raw_time in support_page_times
                    if window_start <= page_time <= now + timedelta(minutes=10)
                ]
                stale_page_times = [
                    (url, page_time, raw_time)
                    for url, page_time, raw_time in support_page_times
                    if page_time < window_start
                ]
                if parsed >= window_start and stale_page_times and not fresh_page_times:
                    url, page_time, raw_time = stale_page_times[0]
                    errors.append(
                        f"[{event_label}] support_urls 中可解析到的明确发布时间均不在最近 {EVENT_FRESHNESS_HOURS} 小时内，"
                        f"示例：{raw_time}（{url}）。该事件不符合本期要求，请删除并换另一个新事件，"
                        "不要把旧事件时间改新来通过校验。"
                    )
                    new_blacklist_entries.extend(_blacklist_entries_for_urls(
                        unique_urls,
                        reason="freshness",
                        label=event_label,
                        detail=f"support_urls 明确发布时间过旧，示例 {raw_time} ({url})",
                    ))
            except ValueError:
                errors.append(f"[{event_label}] event_time 格式必须是 YYYY-MM-DD HH:MM")

    for event_time, items in events_by_time.items():
        if len(items) <= 1:
            continue
        unconfirmed = [
            item for item in items
            if not item["confirmed"] or not isinstance(item.get("note"), str) or len(item["note"].strip()) < 5
        ]
        if unconfirmed:
            context = "；".join(f"{item['label']}《{item['event']}》" for item in items)
            errors.append(
                f"[重复 event_time: {event_time}] 发现 {len(items)} 个事件使用同一时间点，可能是同一事件被拆分：{context}。"
                "请确认是否重复；如确认不是重复，请在每个相关 events[] 对象加入 "
                '"time_duplicate_confirmed": true 和 "time_duplicate_note": "说明差异"，否则请合并或删除重复事件。'
            )

    if errors:
        return {
            "pass": False,
            "total_groups": len(event_groups),
            "total_events": _event_count_from_data(event_groups),
            "error_count": len(errors),
            "errors": errors,
            "new_blacklist_entries": new_blacklist_entries,
        }

    return {
        "pass": True,
        "total_groups": len(event_groups),
        "total_events": _event_count_from_data(event_groups),
        "message": f"event_list 校验通过：{len(event_groups)} 个事件组，{_event_count_from_data(event_groups)} 个事件",
    }


def _allowed_event_urls(event_list):
    allowed = set()
    for group in event_list:
        if not isinstance(group, dict):
            continue
        support_urls = group.get("support_urls", [])
        if not isinstance(support_urls, list):
            continue
        for url in support_urls:
            if isinstance(url, str) and URL_PATTERN.match(url):
                allowed.add(url)
    return allowed


def _check_briefing_urls_against_events(md_path, event_list_path):
    if not os.path.exists(md_path):
        return {"pass": False, "error": f"日报文件不存在: {md_path}"}
    events = _read_json_if_exists(event_list_path)
    if not isinstance(events, list):
        return {"pass": False, "error": f"event_list 不存在或不是数组: {event_list_path}"}

    with open(md_path, "r", encoding="utf-8") as f:
        md_content = f.read()

    source_index_match = re.search(r'(?m)^#{2,}\s*来源索引\s*$', md_content)
    body_content = md_content[:source_index_match.start()] if source_index_match else md_content
    source_index_content = md_content[source_index_match.start():] if source_index_match else ""

    allowed_urls = _allowed_event_urls(events)
    numbered_ref_re = re.compile(r'\[\[(\d+)\]\]\((https?://[^\s\)>\]\"\'\u0060]+)\)')
    numbered_refs = numbered_ref_re.findall(body_content)
    numbered_urls = {url for _, url in numbered_refs}
    source_index_numbered_link_re = re.compile(r'\[(\d+)\]\s+\[[^\]\n]+\]\((https?://[^\s\)>\]\"\'\u0060]+)\)')
    source_index_numbered_links = source_index_numbered_link_re.findall(source_index_content)
    source_index_link_re = re.compile(r'(?<!\!)\[[^\]\n]+\]\((https?://[^\s\)>\]\"\'\u0060]+)\)')
    source_index_link_urls = set(source_index_link_re.findall(source_index_content))
    url_re = re.compile(r'https?://[^\s\)>\]\"\'\u0060]+')
    found_urls = set(url_re.findall(md_content))
    body_urls = set(url_re.findall(body_content))
    source_index_urls = set(url_re.findall(source_index_content))

    if allowed_urls and not numbered_refs:
        return {
            "pass": False,
            "error": "日报正文缺少 [[n]](url) 编号引用",
        }

    body_num_to_url = {}
    body_url_to_num = {}
    for num, url in numbered_refs:
        if num in body_num_to_url and body_num_to_url[num] != url:
            return {
                "pass": False,
                "error": f"正文引用编号不统一：[[{num}]] 指向了多个 URL",
                "urls": sorted({body_num_to_url[num], url}),
            }
        if url in body_url_to_num and body_url_to_num[url] != num:
            return {
                "pass": False,
                "error": "正文引用编号不统一：同一个 URL 使用了多个编号",
                "url": url,
                "numbers": sorted({body_url_to_num[url], num}),
            }
        body_num_to_url[num] = url
        body_url_to_num[url] = num

    unnumbered_urls = body_urls - numbered_urls
    if unnumbered_urls:
        return {
            "pass": False,
            "error": f"日报正文有 {len(unnumbered_urls)} 个 URL 未使用 [[n]](url)",
            "unnumbered_urls": sorted(unnumbered_urls),
        }
    if numbered_urls and not source_index_match:
        return {
            "pass": False,
            "error": "日报缺少“来源索引”二级标题；来源索引必须列出正文引用来源",
        }
    if numbered_urls and not source_index_link_urls:
        return {
            "pass": False,
            "error": "来源索引必须使用 Markdown 超链接，例如 [标题](url)，不能只写纯文本标题、来源和日期",
        }
    if numbered_urls and not source_index_numbered_links:
        return {
            "pass": False,
            "error": "来源索引必须使用统一编号和 Markdown 超链接，例如 [1] [标题](url) - 来源 - 日期",
        }

    index_num_to_url = {}
    index_url_to_num = {}
    for num, url in source_index_numbered_links:
        if num in index_num_to_url and index_num_to_url[num] != url:
            return {
                "pass": False,
                "error": f"来源索引编号不统一：[{num}] 指向了多个 URL",
                "urls": sorted({index_num_to_url[num], url}),
            }
        if url in index_url_to_num and index_url_to_num[url] != num:
            return {
                "pass": False,
                "error": "来源索引编号不统一：同一个 URL 使用了多个编号",
                "url": url,
                "numbers": sorted({index_url_to_num[url], num}),
            }
        index_num_to_url[num] = url
        index_url_to_num[url] = num

    missing_index_urls = numbered_urls - source_index_link_urls
    if missing_index_urls:
        return {
            "pass": False,
            "error": f"来源索引缺少 {len(missing_index_urls)} 个正文引用 URL 的 Markdown 超链接",
            "missing_urls": sorted(missing_index_urls),
        }
    mismatched_index = []
    for url, num in body_url_to_num.items():
        index_num = index_url_to_num.get(url)
        if index_num and index_num != num:
            mismatched_index.append({"url": url, "body_number": num, "source_index_number": index_num})
    if mismatched_index:
        return {
            "pass": False,
            "error": "来源索引编号必须与正文引用编号一致",
            "mismatched": mismatched_index,
        }
    invalid = found_urls - allowed_urls
    if invalid:
        return {
            "pass": False,
            "error": f"日报中包含 {len(invalid)} 个不在 event_list.support_urls 中的 URL",
            "invalid_urls": sorted(invalid),
        }
    return {
        "pass": True,
        "url_count": len(found_urls),
        "numbered_reference_count": len(numbered_refs),
        "source_index_url_count": len(source_index_urls),
        "message": f"日报中 {len(found_urls)} 个 URL 全部来自 event_list.support_urls",
    }


def _validate_event_list_file(
    event_list_path,
    cache_dir,
    low_volume_confirmation_path=None,
    url_blacklist_path=None,
    authority_requirement="high",
):
    events = _read_json_if_exists(event_list_path)
    if events is None:
        return {"pass": False, "errors": [f"event_list 不存在或无法解析: {event_list_path}"]}, None
    if not isinstance(events, list):
        return {"pass": False, "errors": [f"event_list 不是数组: {event_list_path}"]}, None
    confirmation = _read_json_if_exists(low_volume_confirmation_path) if low_volume_confirmation_path else None
    return _validate_event_list(
        events,
        cache_dir=cache_dir,
        low_volume_confirmation=confirmation,
        url_blacklist_path=url_blacklist_path,
        authority_requirement=authority_requirement,
    ), events


def save_state(st):
    os.makedirs(STATE_DIR, exist_ok=True)
    _write_json(_state_path(st["token"]), st)


def load_state(token):
    path = _state_path(token)
    if not os.path.exists(path):
        print(f"错误：找不到状态 token: {token}")
        sys.exit(1)
    return _read_json(path)


def _load_setup_context(setup_token):
    setup = load_state(setup_token)
    if setup.get("flow") != "setup":
        print(f"错误：{setup_token} 不是 setup token")
        sys.exit(1)
    tracking_dir = setup.get("tracking_dir")
    contract = _read_json_if_exists(_contract_path(tracking_dir)) if tracking_dir else None
    if isinstance(contract, dict):
        setup["topic"] = contract.get("topic") or setup.get("topic")
        setup["tracking_dir"] = contract.get("tracking_dir") or tracking_dir
        setup["contract"] = contract
    return setup


def _stamp_tools_rule():
    try:
        current = ""
        if os.path.exists(TOOLS_PATH):
            with open(TOOLS_PATH, "r", encoding="utf-8") as f:
                current = f.read()
        start = "<!-- topic_tracking_delivery_rule:start -->"
        end = "<!-- topic_tracking_delivery_rule:end -->"
        if start in current and end in current:
            updated = re.sub(
                rf"{re.escape(start)}.*?{re.escape(end)}",
                TOOLS_RULE_BLOCK.strip(),
                current,
                flags=re.S,
            )
            if updated == current:
                print("✅ TOOLS.md 已经打上扣子话题追踪日报交付规则。")
                return
            with open(TOOLS_PATH, "w", encoding="utf-8") as f:
                f.write(updated)
            print("✅ 已更新 TOOLS.md 中的扣子话题追踪日报交付规则。")
            return
        os.makedirs(os.path.dirname(TOOLS_PATH), exist_ok=True)
        with open(TOOLS_PATH, "a", encoding="utf-8") as f:
            if current and not current.endswith("\n"):
                f.write("\n")
            f.write("\n" + TOOLS_RULE_BLOCK + "\n")
        print("✅ 检测到第一次运行，已为 TOOLS.md 打上扣子话题追踪日报交付规则。")
    except OSError as e:
        print(f"⚠️ TOOLS.md 规则写入失败：{e}")


def _validate_contract(data, *, topic, tracking_dir):
    errors = []
    if not isinstance(data, dict):
        return ["setup_contract.json 顶层必须是对象"]
    if not isinstance(data.get("topic"), str) or not data.get("topic", "").strip():
        errors.append("缺少 topic")
    if data.get("topic") and data["topic"].strip() != topic:
        errors.append(f"topic 必须保持为当前话题：{topic}")
    if not isinstance(data.get("topic_analysis"), dict):
        errors.append("缺少 topic_analysis 对象")
    else:
        for field in ["definition", "in_scope", "out_of_scope"]:
            if not data["topic_analysis"].get(field):
                errors.append(f"topic_analysis.{field} 不能为空")
    authority_requirement = data.get("authority_requirement")
    if not isinstance(authority_requirement, str) or authority_requirement.strip().lower() not in AUTHORITY_REQUIREMENTS:
        errors.append(f"authority_requirement 必须是 {AUTHORITY_REQUIREMENTS} 之一")
    focus = data.get("focus_directions")
    if not isinstance(focus, list) or not any(isinstance(x, str) and x.strip() for x in focus):
        errors.append("focus_directions 至少需要 1 条")
    if "tracking_dir" in data and data["tracking_dir"]:
        if os.path.abspath(os.path.expanduser(data["tracking_dir"])) != tracking_dir:
            errors.append(f"tracking_dir 必须是当前目录：{tracking_dir}")
    return errors


def _normalize_contract(data, st):
    topic = st["topic"]
    tracking_dir = st["tracking_dir"]
    focus = [x.strip() for x in data.get("focus_directions", []) if isinstance(x, str) and x.strip()]
    authority_requirement = _normalize_authority_requirement(data.get("authority_requirement"))
    support_url_min = _support_url_min_count(authority_requirement)
    contract = {
        "schema": "topic_tracking.contract.v2",
        "setup_token": st["token"],
        "topic": topic,
        "tracking_dir": tracking_dir,
        "created_at": st.get("created_at"),
        "updated_at": datetime.now().isoformat(),
        "topic_analysis": data.get("topic_analysis", {}),
        "authority_requirement": authority_requirement,
        "support_url_min_count": support_url_min,
        "focus_directions": focus,
        "user_preference": data.get("user_preference", ""),
        "frequency": data.get("frequency", ""),
        "source_policy": data.get("source_policy", {
            "default": f"authority_requirement={authority_requirement} 时，每个事件组至少需要 {support_url_min} 个不同且可达的支撑 URL；不确定来源或时间时不要提交事件。",
        }),
    }
    return contract


def _recent_summary_paths(tracking_dir, limit=5):
    import glob

    paths = sorted(glob.glob(os.path.join(tracking_dir, "*_summary.json")))
    return paths[-limit:]


def _format_path_list(paths):
    if not paths:
        return "- 暂无"
    return "\n".join(f"- {p}" for p in paths)


def _iter_state_files():
    if not os.path.isdir(STATE_DIR):
        return []
    paths = []
    for name in sorted(os.listdir(STATE_DIR)):
        if name.endswith(".json"):
            paths.append(os.path.join(STATE_DIR, name))
    return paths


def _state_items():
    items = []
    for path in _iter_state_files():
        st = _read_json_if_exists(path)
        if isinstance(st, dict):
            items.append((st, path))
    return items


def _find_setup_matches(topic=None, setup_token=None):
    matches = []
    for st, path in _state_items():
        if st.get("flow") != "setup":
            continue
        token = st.get("setup_token") or st.get("token")
        if setup_token and token != setup_token:
            continue
        if topic and st.get("topic") != topic:
            continue
        matches.append((st, path))
    return matches


def _briefing_items_for_setup(setup_token):
    return [
        (st, path)
        for st, path in _state_items()
        if st.get("flow") == "briefing" and st.get("setup_token") == setup_token
    ]


def _latest_output_time(tracking_dir):
    import glob

    if not tracking_dir or not os.path.isdir(tracking_dir):
        return ""
    candidates = []
    for pattern in ["*_summary.json", "*_event_list.json", "*.md"]:
        candidates.extend(glob.glob(os.path.join(tracking_dir, pattern)))
    if not candidates:
        return ""
    latest = max(candidates, key=lambda p: os.path.getmtime(p))
    try:
        return datetime.fromtimestamp(os.path.getmtime(latest)).isoformat(timespec="seconds")
    except OSError:
        return ""


def _path_within(child, parent):
    if not child or not parent:
        return False
    try:
        child_abs = os.path.abspath(os.path.expanduser(child))
        parent_abs = os.path.abspath(os.path.expanduser(parent))
        return os.path.commonpath([child_abs, parent_abs]) == parent_abs
    except (ValueError, OSError):
        return False


def _protected_delete_paths():
    return {
        os.path.abspath(os.sep),
        os.path.abspath(os.path.expanduser("~")),
        os.path.abspath(os.getcwd()),
        os.path.abspath(SCRIPT_DIR),
        os.path.abspath(SKILL_DIR),
        os.path.abspath(SESSIONS_DIR),
        os.path.abspath(STATE_DIR),
        os.path.abspath(os.path.dirname(SESSIONS_DIR)),
        os.path.abspath(DEFAULT_TRACKING_ROOT),
    }


def _is_protected_delete_path(path):
    if not path:
        return True
    try:
        path_abs = os.path.abspath(os.path.expanduser(path))
    except OSError:
        return True
    if path_abs in _protected_delete_paths():
        return True
    parts = [p for p in path_abs.split(os.sep) if p]
    return len(parts) < 4


def _tracking_dir_has_topic_marker(tracking_dir, setup_token, topic):
    import glob

    if not tracking_dir or not os.path.isdir(tracking_dir):
        return True

    contract = _read_json_if_exists(_contract_path(tracking_dir))
    if isinstance(contract, dict):
        if contract.get("setup_token") == setup_token:
            return True
        if topic and contract.get("topic") == topic:
            return True

    if topic and os.path.basename(os.path.abspath(tracking_dir)) == _safe_name(topic):
        artifact_patterns = ["*_summary.json", "*_event_list.json", "*.md", "tracking_contract_v2.json"]
        return any(glob.glob(os.path.join(tracking_dir, pattern)) for pattern in artifact_patterns)

    return False


def _same_day_version_hint(run_label):
    if not re.search(r"_v\d+$", run_label or ""):
        return ""
    base_day = re.sub(r"_v\d+$", "", run_label)
    return (
        f"\n同日多版本提醒：本次是 {base_day} 今天再次运行产生的新版本。"
        "之前同一天的产物只作为历史参考；最终交付时直接发送本次日报，不要合并多个同日版本。\n"
    )


def save_guide_file(st, text):
    step = st["current_step"]
    sdir = _session_dir(st)
    path = os.path.join(sdir, f"{step}_guide.md")
    os.makedirs(sdir, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    return path


def guide_text(st):
    flow = st["flow"]
    step = st["current_step"]
    token = st["token"]
    topic = st.get("topic") or ""
    tdir = st.get("tracking_dir") or ""
    sdir = _session_dir(st)

    if flow == "setup" and step == "S1":
        contract_path = os.path.join(sdir, "setup_contract.json")
        return f"""创建「{topic}」的话题追踪设定。

先认真理解用户到底要追什么，不要只拆关键词。请与用户补齐必要边界，并写入：

{contract_path}

JSON 格式：

```json
{{
  "topic": "{topic}",
  "topic_analysis": {{
    "definition": "一句话定义这个追踪到底追什么",
    "in_scope": ["明确应该收录的事件类型"],
    "out_of_scope": ["容易误收、但不应该收录的内容"],
    "authority_policy": "这个话题对来源严谨度的要求，例如爆料型/严肃新闻/监管金融医疗安全等"
  }},
  "authority_requirement": "high",
  "focus_directions": ["方向1", "方向2"],
  "user_preference": "用户偏好、排除项、写作口味和关注重点",
  "frequency": "建议频率，例如 每天 09:00",
  "tracking_dir": "{tdir}"
}}
```

要求：
1. `topic_analysis.definition` 要讲清楚概念边界，例如“黑天鹅”这类词必须先解释判断标准。
2. `in_scope` / `out_of_scope` 要能帮助后续 briefing 判断相关性，不要写空泛词。
3. `authority_requirement` 只能填 `high` 或 `low`：
   - `high`：信息真实性要求高，适用于政策、监管、财经、医疗、安全、企业重大事项、资讯/事实类捕捉、突发事件等；后续每个事件组至少需要 3 个不同且可达的 support_urls。
   - `low`：信息真实性要求较低或天然难以多源验证，适用于攻略、教程、经验、玩法、如何用 AI 赚钱、路线建议等；后续每个事件组至少需要 1 个可达 support_url。
4. `topic_analysis.authority_policy` 要解释为什么选择 high 或 low，以及哪些来源可接受。
5. `focus_directions` 是后续搜索的方向，不是最终栏目标题，可以动态服务于搜索。
6. 如果用户没有明确偏好，`user_preference` 写空字符串即可，不要编。

完成后运行：

```bash
{SCRIPT_CMD} next {token}
```"""

    if flow == "setup" and step == "S2":
        setup_token = st["token"]
        briefing_cmd = f'{SCRIPT_CMD} init --flow briefing --setup-token "{setup_token}"'
        return f"""「{topic}」追踪设定已保存。

接下来按需要做两件事。给子会话或日程的描述要保持简洁，但必须说清楚：先加载技能、再执行命令、并按脚本指引完整跑到 DONE。

1. 首次试运行：新开一个子会话，任务描述可直接使用下面内容。

```markdown
请为「{topic}」生成本期结果。已有追踪已配置好，不要重新创建追踪。
1. 先加载并阅读 topic_tracking 技能。
2. 执行命令：`{briefing_cmd}`。
3. 按脚本指引完成完整 briefing 流程，直到状态为 DONE；如果中途校验未通过，按提示修正后继续，不要只运行 init 就结束。
4. 若没有符合标准的新内容，按脚本的暂无动态流程完成，不要降低筛选标准。
完成后只回传最终状态和脚本要求重复的信息，不要直接发给用户。
```

2. 创建日程时，标题和描述保持简洁：

标题：

```text
扣子话题追踪 - 「{topic}」
```

描述：

```text
扣子话题追踪 - 「{topic}」

1. 先加载并阅读 topic_tracking 技能。
2. 执行命令：{briefing_cmd}
3. 按脚本指引完成完整 briefing 流程，直到状态为 DONE；如果中途校验未通过，按提示修正后继续，不要只运行 init 就结束。
```

日程触发后只运行 briefing，不要重新 setup。完成试运行或日程设置后运行：

```bash
{SCRIPT_CMD} next {token}
```"""

    if flow == "briefing" and step == "B1":
        contract_path = _contract_path(tdir)
        b1_path = os.path.join(sdir, "B1_context.json")
        summaries = _recent_summary_paths(tdir)
        return f"""恢复「{topic}」的追踪上下文。

必须读取：
- 追踪设定：{contract_path}
- 历史 summary（最近几期）：
{_format_path_list(summaries)}

写入上下文文件：

{b1_path}

JSON 格式：

```json
{{
  "topic": "{topic}",
  "topic_definition": "从 tracking_contract_v2.json 提炼出的追踪定义",
  "authority_requirement": "从 tracking_contract_v2.json 原样继承 high 或 low",
  "focus_directions": ["本次搜索会用到的方向"],
  "user_preference": "用户偏好，原样继承即可",
  "history_hint": ["历史已覆盖的事件、时间线、来源或明确不应重复的内容"]
}}
```

要求：
1. 只做上下文恢复，不搜索。
2. `history_hint` 用来避免重复，不要暴露给用户。
3. 如果今天同一话题已经跑过，本次仍是新版本；历史只用于去重，不要让主会话合并多个版本。
{_same_day_version_hint(st.get("run_label"))}
完成后运行：

```bash
{SCRIPT_CMD} next {token}
```"""

    if flow == "briefing" and step == "B2":
        run_label = st.get("run_label") or date.today().isoformat()
        b1_path = os.path.join(sdir, "B1_context.json")
        event_list_path = os.path.join(tdir, f"{run_label}_event_list.json")
        now = datetime.now()
        window_start = now - timedelta(hours=EVENT_FRESHNESS_HOURS)
        freshness_days = EVENT_FRESHNESS_DAYS
        authority_requirement = _contract_authority_requirement(tdir)
        support_url_min = _support_url_min_count(authority_requirement)
        return f"""阅读大量资讯并聚合「{topic}」本期相关事件。

先读取：
- {b1_path}
- {_contract_path(tdir)}

历史去重要求：
- 开始搜索和整理前，必须先读取 B1_context.json 的 `history_hint`。
- `history_hint` 中已覆盖的事件、时间线、来源或明确不应重复的内容，不得再次写入 event_list。
- 如果新资讯只是对历史事件的转载、复述、延伸评论或换标题重发，不算本期新事件；只有出现新的事实变化、新时间点、新官方动作或新的可验证进展，才可以作为新事件组提交。

本话题来源要求：
- 每个事件组的 `support_urls` 至少需要 {support_url_min} 个不同且可达的 URL。
- 如果你认为当前事件无法满足本话题的来源要求，请更换事件；不要降低要求或凑低质量来源。

工具用法（按需要组合，不固定流程）：
- 搜索近两天候选信息时使用：`search_web(query_list=[...], freshness={freshness_days}, response="short")`。
- 需要更多上下文、交叉验证、寻找同一事件更多来源或更接近源头的报道时，可使用：`search_web(query_list=[...], freshness={freshness_days}, response="medium")`，必要时提高到 `response="long"`。
- 读取网页正文时使用：`fetch_web(url=..., response="medium")` 或 `fetch_url(url=..., response="medium")`。
- 如果正文片段不足以确认事件时间、事实、来源出处或关键证据句，把 fetch 的 `response` 提高到 `"long"`。
- 具体先搜什么、何时 fetch、何时扩展关键词，由你根据 topic、focus_directions、用户偏好和已读内容自己判断；目标是确认同一个事件的事实、发生时间和来源支撑。

事件溯源和验证方法：
1. 先浏览近两天相关资讯，快速识别可能符合「{topic}」的新事件；此时重点是发现候选事件，不要一开始逐篇深挖。
2. 对每个候选事件，先判断三件事是否清楚：事实变化是什么、真实发生时间是什么、来源链条是否清楚。
3. 如果真实性、时效性或来源出处有任何模糊，继续搜索和浏览网页进行溯源和交叉验证：用事件主体、关键动作、专名、时间词组合搜索，优先寻找官方公告、发布会/访谈原始内容、权威媒体或多家独立报道。
4. `event_time` 必须是列出的具体事件的准确发生时间，不是搜索结果时间，也不是转载文章发布时间；只有当网页发布时间就是官方发布/活动发生/产品上线等事件本身的时间时，才可以采用。
5. 如果相关资讯原文只写“近日”“最近”“今日早些时候”等模糊时间，或完全没有说明事件时间，必须继续搜索更优 URL 来支撑事件时间；如果实在找不到能确认准确时间的来源，放弃该事件组。
6. `support_urls` 必须共同指向同一个事件组，并共同支撑组内所有事件的事实和时间；不要把多篇转载同一段文字当作独立验证。如果本话题只要求 1 条来源，该 URL 仍必须可达、质量可接受，并能支撑事件事实和时间。
7. 如果仍无法确认事件是否真实、真实发生时间是否在最近 {EVENT_FRESHNESS_HOURS} 小时内，或支撑 URL 是否可靠，不要提交该事件；应换其他事件，或写入空数组。

核心思想：
1. “事件组”是一组 `support_urls` 可以共同支撑的一组事实变化；一个发布会、一个官方公告或一组报道可能同时包含多个事件。
2. “事件”是最近 {EVENT_FRESHNESS_HOURS} 小时内发生、符合「{topic}」定义和用户偏好的具体事实变化；主体是事件，不是资讯。
3. 多个 URL 提到同一组事实变化时，不要拆成多条资讯；应合并成同一个事件组，并把这些 URL 放入同一个 `support_urls`。
4. 你要从大量资讯中识别真正围绕「{topic}」的新事件，再为事件组寻找支撑来源。
5. 必须用 B1_context.json 的 `history_hint` 做历史去重；历史已覆盖或明确不应重复的事件，不要再次整理。
6. 如果事件来自转载、社评、专业账号整理或聚合资讯，必须进一步寻找事件源头，确认真实发生时间和事实是否成立；不能把转载发布时间当作事件发生时间。
7. 事件时间以主体事件真实发生时间为准；网页发布时间只作为辅助证据。
8. 本期只允许最近 {EVENT_FRESHNESS_HOURS} 小时内发生的事件。当前时间：{now.strftime('%Y-%m-%d %H:%M')}；最早允许事件时间：{window_start.strftime('%Y-%m-%d %H:%M')}。
9. 目标是收集 {TARGET_EVENT_GROUPS} 个左右的高质量事件组；如果近期事件丰富，可以多给，不需要压缩到 5 个。
10. 如果某个事件真实发生时间不在最近 {EVENT_FRESHNESS_HOURS} 小时内，该事件不合格。不要为了通过校验修改事件时间，应删除该事件并寻找其他符合时效的新事件。
11. 如果两个事件必须使用完全相同的 `event_time`，先确认它们不是同一事件被拆分；确认后在对应 event 对象里写 `time_duplicate_confirmed: true` 和 `time_duplicate_note` 说明差异。
12. 只有与「{topic}」强相关的事件组才能提交；弱相关、不相关、只是背景提及或相邻话题都不要放入 event_list。
13. 已经因为时效性或相关性被脚本打回过的 URL 会进入本次黑名单；不要复用黑名单 URL，也不要通过改写 event_time 或 relevance_level 让它重新通过。
14. `support_urls` 不允许使用低质量域名黑名单：{_format_blocked_support_domains()}。命中时说明来源质量低，不采用，请更换为官方、权威媒体或更可追溯的来源。
15. 本话题每个事件组 support_urls 至少需要 {support_url_min} 个不同且可达的 URL。

写入事件列表：

{event_list_path}

JSON 格式：

```json
[
  {{
    "events": [
      {{
        "event": "事件一句话，直接写事实变化",
        "event_time": "YYYY-MM-DD HH:MM",
        "relevance_level": "强相关"
      }}
    ],
    "relevance_with_topic": "为什么这一组事件严格符合「{topic}」定义、边界和用户偏好",
    "source_type": "cross_valid",
    "support_urls": ["https://...", "https://...", "https://..."]
  }}
]
```

字段要求：
1. 顶层数组的每一项是一个事件组，不是一篇资讯。
2. `events`：该组来源共同支撑的事件数组；每个事件必须写 `event`、`event_time`、`relevance_level`，如遇同一时间点确认不重复，可额外写 `time_duplicate_confirmed` 和 `time_duplicate_note`。
3. `event`：事件本身，不是文章标题，也不是某篇资讯的摘要。
4. `event_time`：事件真实发生时间，格式必须是 `YYYY-MM-DD HH:MM`，且必须在最近 {EVENT_FRESHNESS_HOURS} 小时内；不能为了保留旧事件而改写时间。
5. `support_urls`：同一组内的 URL 必须共同支撑组内所有事件；同一个 URL 全局只能出现在一个事件组，不能重复使用。
6. `support_urls` 不允许来自低质量域名黑名单；例如 toutiao.com 质量和可追溯性不足，不可采用。
7. `events[].relevance_level`：事件级审计字段，只能填 `强相关` / `弱相关` / `不相关`；只有 `强相关` 允许通过。如果你判断是弱相关或不相关，不要提交该事件，应该更换事件。
8. `relevance_with_topic`：事件组级字符串，说明这组事件为什么严格符合「{topic}」的定义、边界和用户偏好；不要只写“相关”。
9. `source_type`：必须填写 `cross_valid` / `official` / `coze`。
10. `source_type=cross_valid`：普通媒体、专业账号、自媒体、转载、社评或来源链不清楚时都使用 `cross_valid`。
11. `source_type=official`：表示支撑 URL 中包含官方媒体、官网或官方账号发布页，并直接发布/确认事件事实；普通媒体报道“官方称/官方宣布”不等于官方来源。
12. `source_type=coze`：表示支撑 URL 中包含 coze.cn 发布内容；仍需满足本话题至少 {support_url_min} 个 support_urls 的要求。
13. `support_urls` 数量由本话题来源要求决定：当前至少需要 {support_url_min} 个不同且可达的 URL。

fewshot：

```json
[
  {{
    "events": [
      {{
        "event": "某公司正式发布新一代 AI 编程工具",
        "event_time": "{now.strftime('%Y-%m-%d')} 09:30",
        "relevance_level": "强相关",
        "time_duplicate_confirmed": true,
        "time_duplicate_note": "同一发布会内的两个不同产品动作：一个是工具发布，一个是企业版开放"
      }},
      {{
        "event": "该公司同步开放 AI 编程工具企业版",
        "event_time": "{now.strftime('%Y-%m-%d')} 09:30",
        "relevance_level": "强相关",
        "time_duplicate_confirmed": true,
        "time_duplicate_note": "同一发布会内的两个不同产品动作：一个是工具发布，一个是企业版开放"
      }}
    ],
    "relevance_with_topic": "该事件组是围绕「{topic}」的产品级新发布和企业版开放，符合用户对产品进展和企业采用路径的关注偏好。",
    "source_type": "cross_valid",
    "support_urls": [
      "https://official.example.com/news/product-launch",
      "https://media.example.com/report/product-launch",
      "https://another-media.example.com/product-launch-analysis"
    ]
  }},
  {{
    "events": [
      {{
        "event": "某公司在官网发布新产品更新",
        "event_time": "{now.strftime('%Y-%m-%d')} 10:00",
        "relevance_level": "强相关"
      }}
    ],
    "relevance_with_topic": "该事件由官网/官方账号原文直接发布，属于「{topic}」边界内的官方产品进展。",
    "source_type": "official",
    "support_urls": [
      "https://official.example.com/news/product-update",
      "https://media.example.com/report/product-update",
      "https://another-media.example.com/product-update"
    ]
  }}
]
```

如果补搜后仍找不到最近 {EVENT_FRESHNESS_HOURS} 小时内、事实和准确时间都能被支撑的相关事件，写入空数组：

```json
[]
```

完成后运行：

```bash
{SCRIPT_CMD} next {token}
```"""

    if flow == "briefing" and step == "B3":
        run_label = st.get("run_label") or date.today().isoformat()
        event_list_path = os.path.join(tdir, f"{run_label}_event_list.json")
        md_path = _briefing_md_path(tdir, topic, run_label)
        return f"""基于已通过校验的事件，写「{topic}」本期日报。

读取：

{event_list_path}

写入：

{md_path}

写作要求：
1. 日报主体必须围绕「{topic}」展开，先说明本期最重要的新变化。
2. 每个信息点都来自 event_list 里的事件组；同一事件组可以合并多个支撑来源，组内多个事件可以写成一个小段。
3. 正文引用必须使用 `[[n]](url)`，URL 必须来自 event_list 的 `support_urls`。
4. 不新增事实、不新增 URL、不写 event_list 之外的内容。
5. 如果事件少，就写短日报；不要为了篇幅编主线。
6. 写作前先为本次可能用到的所有 URL 建立统一编号表；同一个 URL 在全文只能使用同一个编号，同一个编号只能对应一个 URL。
7. 末尾保留“来源索引”，列出编号、可点击标题、来源和日期。
8. 来源索引必须使用 Markdown 超链接，例如：`[1] [标题](https://...) - 来源 - 日期`；不能只写纯文本标题。
9. 标题、日期和结构保持清楚克制。标题可用 `# {topic}资讯简报（{run_label}）` 或更贴合话题的自然标题；日期优先使用本期 run_label。正文可用二级标题组织板块，用三级标题写具体事件，不要把所有层级都写成加粗文本。

结构 fewshot：

```markdown
# {topic}资讯简报（{run_label}）

## 本期主线

本期最重要的变化是某公司发布了新一代 AI 编程工具，并同步开放企业版。官方发布页给出了产品功能和发布时间[[1]](https://official.example.com/news/product-launch)，两家媒体也确认了同一发布会信息[[2]](https://media.example.com/report/product-launch)[[3]](https://another-media.example.com/product-launch-analysis)。

## 产品更新

### 新一代 AI 编程工具发布

该工具新增多智能体协作、自动测试和企业权限管理，意味着产品从个人开发者工具进一步进入团队协作场景[[1]](https://official.example.com/news/product-launch)。

### 企业版同步开放

企业版重点补齐审计、权限和私有环境接入能力。后文如果再次引用官方发布页，仍然使用同一个编号[[1]](https://official.example.com/news/product-launch)。

## 后续关注

- 企业版开放后的首批客户和定价细节。
- 多智能体能力是否进入稳定可用阶段。

## 来源索引

[1] [某公司发布新一代 AI 编程工具](https://official.example.com/news/product-launch) - 官方发布 - 2026-05-08
[2] [某公司 AI 编程工具发布会报道](https://media.example.com/report/product-launch) - 媒体报道 - 2026-05-08
[3] [新一代 AI 编程工具发布分析](https://another-media.example.com/product-launch-analysis) - 媒体报道 - 2026-05-08
```

短日报 fewshot：

```markdown
# {topic}简报（{run_label}）

本期只监测到一个符合标准的新事件：某公司在官网发布产品更新，补齐企业权限和审计能力[[1]](https://official.example.com/news/product-update)。

## 来源索引

[1] [某公司产品更新公告](https://official.example.com/news/product-update) - 官方发布 - 2026-05-08
```

完成后运行：

```bash
{SCRIPT_CMD} next {token}
```"""

    if flow == "briefing" and step == "B4":
        run_label = st.get("run_label") or date.today().isoformat()
        event_list_path = os.path.join(tdir, f"{run_label}_event_list.json")
        summary_path = os.path.join(tdir, f"{run_label}_summary.json")
        md_path = _briefing_md_path(tdir, topic, run_label)
        return f"""收尾本期「{topic}」追踪。

确认产物：
- 事件列表：{event_list_path}
- 日报文件：{md_path}

写入 summary：

{summary_path}

有内容时：

```json
{{
  "topic": "{topic}",
  "run_label": "{run_label}",
  "event_count": 3,
  "key_events": ["本期关键事件"],
  "sources": ["本期使用的重要来源"],
  "next_watch": ["下期继续观察什么"]
}}
```

完成后运行：

```bash
{SCRIPT_CMD} next {token}
```"""

    return "未知步骤。"


def _advance_step(st):
    cur = st["current_step"]
    steps = SETUP_STEPS if st["flow"] == "setup" else BRIEFING_STEPS
    if cur not in steps:
        st["current_step"] = "DONE"
        return st
    st.setdefault("completed_steps", []).append(cur)
    idx = steps.index(cur)
    st["current_step"] = steps[idx + 1] if idx + 1 < len(steps) else "DONE"
    st["updated_at"] = datetime.now().isoformat()
    return st


def _print_done(st):
    flow = st.get("flow")
    topic = st.get("topic") or ""
    print("✅ 所有步骤已完成。")

    if flow != "briefing":
        print()
        print(f"「{topic}」追踪设定已完成。")
        print("后续日程或手动更新只运行 briefing 命令，不要重新 setup。")
        return

    tdir = st.get("tracking_dir")
    run_label = st.get("run_label") or date.today().isoformat()
    md_path = _briefing_md_path(tdir, topic, run_label)
    event_list_path = os.path.join(tdir, f"{run_label}_event_list.json")
    kept_count = _event_count_from_file(event_list_path)

    print("\n📤 请重复下列信息并结束。工单结束后，你最后重复的信息将被发送给主会话。")
    if os.path.isfile(md_path):
        print()
        print(f"本期「{topic}」日报已完成。")
        print("本日报即为日程/子会话严格筛选、验证、去重和时效性检查后的最终结论。主会话严禁再次搜索、补充来源、重写事实、重新筛选、合并其他信息，或为了凑数量补充未验证内容。")
        if isinstance(kept_count, int):
            print(f"本期保留 {kept_count} 个高质量事件；如果数量较少，也代表已按高质量标准筛选，不得放宽标准。")
        print("主会话可以根据用户偏好微调交付时的表达形式，但不得改变日报事实、结论、来源、排序和取舍。")
        print(f"请用 computer 协议把日报发送给用户：[{os.path.basename(md_path)}](computer://{md_path})")
    elif st.get("empty_result") or kept_count == 0:
        print()
        print(f"本期「{topic}」追踪已完成：该话题暂时没有监测到最新动态。")
        print("这是本次工单的最终交付结论。主会话不得再次搜索、不得建议放宽时效性或筛选标准、不得补充解释或添油加醋。")
        print("请直接向用户说明：该话题暂时没有监测到最新动态。")
    else:
        print()
        print(f"本期「{topic}」追踪已完成，但未发现可交付日报文件。")
        print("请直接向用户说明本期未生成可交付日报，不要自行补搜。")


def print_state(st):
    topic = st.get("topic") or "-"
    token = st.get("token")
    flow = st.get("flow")
    step = st.get("current_step")
    run_label = st.get("run_label")
    completed = len(st.get("completed_steps", []))
    total = len(SETUP_STEPS if flow == "setup" else BRIEFING_STEPS)

    print("\n=== 话题追踪 v2 ===")
    if run_label:
        print(f"Token: {token}  话题: {topic}  流程: {flow}  本次: {run_label}")
    else:
        print(f"Token: {token}  话题: {topic}  流程: {flow}")
    print(f"当前: {step} {STEP_TITLES.get(step, '')}  已完成: {completed}/{total}")
    if st.get("skipped_steps"):
        print(f"跳过: {', '.join(st['skipped_steps'])}")
    if st.get("tracking_dir"):
        print(f"目录: {st['tracking_dir']}")
    print()

    if step == "DONE":
        _print_done(st)
        print()
        return

    text = guide_text(st)
    guide_path = save_guide_file(st, text)
    print(f"--- {step}：{STEP_TITLES.get(step, '')} ---\n")
    print(text)
    print(f"\n📎 本步骤完整指引已保存至：{guide_path}\n")


def cmd_init(args):
    flow = args.flow

    if flow == "setup":
        if not args.topic:
            print("错误：setup 必须传入 --topic")
            return 1
        token = _new_token("setup")
        tracking_dir = os.path.abspath(os.path.expanduser(args.tracking_dir)) if args.tracking_dir else _default_tracking_dir(args.topic)
        st = {
            "schema": "topic_tracking.state.v2",
            "token": token,
            "setup_token": token,
            "flow": "setup",
            "current_step": "S1",
            "topic": args.topic,
            "tracking_dir": tracking_dir,
            "session_dir": os.path.join(SESSIONS_DIR, token),
            "completed_steps": [],
            "created_at": datetime.now().isoformat(),
        }
        os.makedirs(st["session_dir"], exist_ok=True)
        _stamp_tools_rule()
        save_state(st)
        print_state(st)
        return 0

    if flow == "briefing":
        if args.topic:
            print("错误：briefing 不需要 --topic；请传 --setup-token")
            return 1
        if not args.setup_token:
            print("错误：briefing 必须传入 --setup-token")
            return 1
        setup = _load_setup_context(args.setup_token)
        topic = setup.get("topic")
        tracking_dir = setup.get("tracking_dir")
        if not topic or not tracking_dir:
            print("错误：无法从 setup 恢复 topic 或 tracking_dir，请确认 S1 已完成。")
            return 1
        token = _new_token("brief")
        st = {
            "schema": "topic_tracking.state.v2",
            "token": token,
            "setup_token": args.setup_token,
            "flow": "briefing",
            "current_step": "B1",
            "topic": topic,
            "tracking_dir": tracking_dir,
            "run_label": _next_run_label(tracking_dir, date.today().isoformat()),
            "session_dir": os.path.join(SESSIONS_DIR, args.setup_token, token),
            "completed_steps": [],
            "created_at": datetime.now().isoformat(),
        }
        os.makedirs(st["session_dir"], exist_ok=True)
        save_state(st)
        print_state(st)
        return 0

    print(f"错误：未知 flow: {flow}")
    return 1


def cmd_next(args):
    st = load_state(args.token)
    cur = st.get("current_step")

    if cur == "DONE":
        print_state(st)
        return 0

    if st.get("flow") == "setup" and cur == "S1":
        sdir = _session_dir(st)
        contract_input = os.path.join(sdir, "setup_contract.json")
        data = _read_json_if_exists(contract_input)
        if data is None:
            print("❌ setup_contract.json 不存在或无法解析，停留在 S1。")
            print(f"请写入：{contract_input}")
            return 1
        tracking_dir = os.path.abspath(os.path.expanduser(st["tracking_dir"]))
        errors = _validate_contract(data, topic=st["topic"], tracking_dir=tracking_dir)
        if errors:
            print("❌ setup_contract.json 校验未通过，停留在 S1。")
            for err in errors:
                print(f"  - {err}")
            return 1
        os.makedirs(tracking_dir, exist_ok=True)
        contract = _normalize_contract(data, st)
        _write_json(_contract_path(tracking_dir), contract)
        st["tracking_dir"] = tracking_dir
        st["contract_path"] = _contract_path(tracking_dir)
        print(f"✅ 已写入追踪设定：{st['contract_path']}")

    if st.get("flow") == "briefing" and cur == "B1":
        b1_path = os.path.join(_session_dir(st), "B1_context.json")
        data = _read_json_if_exists(b1_path)
        if not isinstance(data, dict):
            print("❌ B1_context.json 不存在、无法解析或不是对象，停留在 B1。")
            print(f"请写入：{b1_path}")
            return 1
        if not data.get("topic_definition"):
            print("❌ B1_context.json 缺少 topic_definition，停留在 B1。")
            return 1
        print("✅ B1 上下文已恢复。")

    if st.get("flow") == "briefing" and cur == "B2":
        run_label = st.get("run_label") or date.today().isoformat()
        tdir = st["tracking_dir"]
        event_list_path = os.path.join(tdir, f"{run_label}_event_list.json")
        confirmation_path = _low_volume_confirmation_path(tdir, run_label)
        url_blacklist_path = _event_url_blacklist_path(tdir, run_label)
        authority_requirement = _contract_authority_requirement(tdir)
        events = _read_json_if_exists(event_list_path)
        if events is None:
            print("❌ event_list 不存在或无法解析，停留在 B2。")
            print(f"请写入：{event_list_path}")
            return 1

        cache_dir = os.path.join(_session_dir(st), "url_cache")
        confirmation = _read_json_if_exists(confirmation_path)
        result = _validate_event_list(
            events,
            cache_dir=cache_dir,
            low_volume_confirmation=confirmation,
            url_blacklist_path=url_blacklist_path,
            authority_requirement=authority_requirement,
        )
        if not result.get("pass"):
            added = _append_url_blacklist(url_blacklist_path, result.get("new_blacklist_entries", []))
            print("❌ event_list 校验未通过，停留在 B2。")
            print(json.dumps(result, ensure_ascii=False, indent=2))
            if added:
                print(f"\n⚠️ 已将 {added} 个因时效性或相关性失败的 URL 写入黑名单：{url_blacklist_path}")
            if isinstance(events, list) and len(events) < TARGET_EVENT_GROUPS:
                print()
                print(_low_volume_confirmation_guide(confirmation_path))
            print(f"\n请修正后重新运行：{SCRIPT_CMD} next {args.token}")
            return 1

        print(f"✅ {result.get('message')}")
        if len(events) == 0:
            print("ℹ️ event_list 为空：该话题暂时没有监测到最新动态，流程直接结束。")
            st.setdefault("completed_steps", []).append("B2")
            st["current_step"] = "DONE"
            st["empty_result"] = True
            st["event_list_path"] = event_list_path
            st["skipped_steps"] = ["B3", "B4"]
            st["updated_at"] = datetime.now().isoformat()
            save_state(st)
            print_state(st)
            return 0

    if st.get("flow") == "briefing" and cur == "B3":
        run_label = st.get("run_label") or date.today().isoformat()
        tdir = st["tracking_dir"]
        topic = st.get("topic") or ""
        event_list_path = os.path.join(tdir, f"{run_label}_event_list.json")
        md_path = _briefing_md_path(tdir, topic, run_label)
        cache_dir = os.path.join(_session_dir(st), "url_cache")
        confirmation_path = _low_volume_confirmation_path(tdir, run_label)
        url_blacklist_path = _event_url_blacklist_path(tdir, run_label)
        authority_requirement = _contract_authority_requirement(tdir)
        event_result, events = _validate_event_list_file(
            event_list_path,
            cache_dir,
            confirmation_path,
            url_blacklist_path,
            authority_requirement,
        )
        if not event_result.get("pass"):
            added = _append_url_blacklist(url_blacklist_path, event_result.get("new_blacklist_entries", []))
            print("❌ event_list 重新校验未通过，停留在 B3。")
            print(json.dumps(event_result, ensure_ascii=False, indent=2))
            if added:
                print(f"\n⚠️ 已将 {added} 个因时效性或相关性失败的 URL 写入黑名单：{url_blacklist_path}")
            print("请删除不符合时效/来源要求的事件，并寻找其他符合时效的新事件；不要通过改写事件时间来通过校验。")
            print(f"\n请修正后重新运行：{SCRIPT_CMD} next {args.token}")
            return 1

        url_result = _check_briefing_urls_against_events(md_path, event_list_path)
        if not url_result.get("pass"):
            print("❌ 日报 URL 校验未通过，停留在 B3。")
            print(json.dumps(url_result, ensure_ascii=False, indent=2))
            print(f"\n请修正日报后重新运行：{SCRIPT_CMD} next {args.token}")
            return 1
        print(f"✅ {url_result.get('message')}")

    if st.get("flow") == "briefing" and cur == "B4":
        run_label = st.get("run_label") or date.today().isoformat()
        tdir = st["tracking_dir"]
        topic = st.get("topic") or ""
        event_list_path = os.path.join(tdir, f"{run_label}_event_list.json")
        md_path = _briefing_md_path(tdir, topic, run_label)
        summary_path = os.path.join(tdir, f"{run_label}_summary.json")
        cache_dir = os.path.join(_session_dir(st), "url_cache")
        confirmation_path = _low_volume_confirmation_path(tdir, run_label)
        url_blacklist_path = _event_url_blacklist_path(tdir, run_label)
        authority_requirement = _contract_authority_requirement(tdir)
        event_result, events = _validate_event_list_file(
            event_list_path,
            cache_dir,
            confirmation_path,
            url_blacklist_path,
            authority_requirement,
        )
        summary = _read_json_if_exists(summary_path)

        if not event_result.get("pass"):
            added = _append_url_blacklist(url_blacklist_path, event_result.get("new_blacklist_entries", []))
            print("❌ event_list 重新校验未通过，停留在 B4。")
            print(json.dumps(event_result, ensure_ascii=False, indent=2))
            if added:
                print(f"\n⚠️ 已将 {added} 个因时效性或相关性失败的 URL 写入黑名单：{url_blacklist_path}")
            print("请删除不符合时效/来源要求的事件，并寻找其他符合时效的新事件；不要通过改写事件时间来通过校验。")
            print(f"\n请修正后重新运行：{SCRIPT_CMD} next {args.token}")
            return 1
        if events is not None and len(events) == 0:
            print("❌ event_list 为空时不应进入 B4；请重新查看状态。")
            return 1
        if not isinstance(summary, dict):
            print("❌ summary.json 不存在、无法解析或不是对象，停留在 B4。")
            print(f"请写入：{summary_path}")
            return 1
        if not os.path.isfile(md_path):
            print("❌ 日报文件不存在，停留在 B4。")
            print(f"请写入：{md_path}")
            return 1
        print("✅ 收尾摘要已确认。")

    st = _advance_step(st)
    save_state(st)
    print_state(st)
    return 0


def cmd_status(args):
    st = load_state(args.token)
    print_state(st)
    return 0


def cmd_list(args):
    items = _state_items()
    setups = [st for st, _ in items if st.get("flow") == "setup"]
    unfinished = [st for st, _ in items if st.get("current_step") != "DONE" and st.get("token")]

    if not setups:
        print("暂无 v2 追踪。")
    else:
        setups.sort(key=lambda item: item.get("created_at") or "")
        print("当前 v2 追踪：")
        for index, st in enumerate(setups, 1):
            token = st.get("setup_token") or st.get("token")
            topic = st.get("topic") or "未命名话题"
            tdir = st.get("tracking_dir") or ""
            status = st.get("current_step")
            latest = _latest_output_time(tdir)
            briefing_count = len(_briefing_items_for_setup(token))
            print(f"{index}. {topic}")
            print(f"   setup_token: {token}")
            print(f"   状态: {status}")
            print(f"   目录: {tdir or '未保存'}")
            print(f"   briefing_count: {briefing_count}")
            print(f"   last_output_at: {latest or '暂无'}")
            print(f"   手动更新: {SCRIPT_CMD} init --flow briefing --setup-token \"{token}\"")
            print(f"   删除预览: {SCRIPT_CMD} delete --setup-token \"{token}\"")
            print()

    print("未完成流程：")
    if not unfinished:
        print("- 暂无")
    else:
        for st in unfinished:
            token = st.get("token")
            print(f"- {token} | {st.get('flow')} | {st.get('topic') or ''} | 当前步骤: {st.get('current_step')}")
            print(f"  继续查看: {SCRIPT_CMD} status {token}")
    return 0


def cmd_delete(args):
    matches = _find_setup_matches(topic=args.topic, setup_token=args.setup_token)
    label = args.topic or args.setup_token

    if not matches:
        print(f"❌ 未找到要删除的话题追踪：{label}")
        print(f"可先运行：{SCRIPT_CMD} list")
        return 1

    if len(matches) > 1:
        print(f"❌ 找到多个同名话题「{label}」，为避免误删，请改用 setup_token 删除：")
        for st, _ in matches:
            token = st.get("setup_token") or st.get("token")
            print(f"  - {st.get('topic') or '未命名话题'} | {token} | {st.get('tracking_dir') or '未保存目录'}")
        return 1

    st, setup_state_path = matches[0]
    setup_token = st.get("setup_token") or st.get("token")
    topic = st.get("topic") or ""
    tracking_dir = os.path.abspath(os.path.expanduser(st.get("tracking_dir") or "")) if st.get("tracking_dir") else ""
    session_dir = os.path.abspath(os.path.expanduser(st.get("session_dir") or os.path.join(SESSIONS_DIR, setup_token)))
    briefing_items = _briefing_items_for_setup(setup_token)
    state_paths = [setup_state_path] + [path for _, path in briefing_items]
    latest = _latest_output_time(tracking_dir)

    delete_session = os.path.isdir(session_dir)
    delete_tracking = bool(tracking_dir and os.path.isdir(tracking_dir) and not args.keep_files)

    errors = []
    if delete_session and not _path_within(session_dir, SESSIONS_DIR):
        errors.append(f"setup/session 目录不在 sessions_v2 下，拒绝删除：{session_dir}")
    if delete_session and _is_protected_delete_path(session_dir):
        errors.append(f"setup/session 路径受保护，拒绝删除：{session_dir}")
    if delete_tracking and _is_protected_delete_path(tracking_dir):
        errors.append(f"tracking_dir 路径受保护，拒绝删除：{tracking_dir}")
    if delete_tracking and not args.force and not _tracking_dir_has_topic_marker(tracking_dir, setup_token, topic):
        errors.append("tracking_dir 缺少 v2 追踪标记，拒绝删除。确认无误后可追加 --force。")

    print("=== 删除话题追踪预览 ===")
    print(f"话题: {topic or '未命名话题'}")
    print(f"setup_token: {setup_token}")
    print(f"briefing_count: {len(briefing_items)}")
    print(f"last_output_at: {latest or '暂无'}")
    print(f"state_files: {len(state_paths)} 个")
    print(f"setup_session: {session_dir if delete_session else '未找到'}")
    print(f"tracking_dir: {tracking_dir or '未保存'}")
    print(f"保留产物目录: {'是' if args.keep_files else '否'}")
    print()
    print("将删除：")
    for path in state_paths:
        print(f"  - 状态文件：{path}")
    if delete_session:
        print(f"  - setup/session 目录：{session_dir}")
    else:
        print("  - setup/session 目录：无")
    if delete_tracking:
        print(f"  - 话题产物目录：{tracking_dir}")
    elif tracking_dir and args.keep_files:
        print(f"  - 话题产物目录：保留 {tracking_dir}")
    else:
        print("  - 话题产物目录：无")

    if errors:
        print()
        print("❌ 安全检查未通过：")
        for err in errors:
            print(f"  - {err}")
        return 1

    if not args.yes:
        print()
        print("当前为预览模式，未执行删除。确认无误后运行：")
        target_arg = f"--setup-token \"{setup_token}\"" if setup_token else f"--topic \"{topic}\""
        keep_arg = " --keep-files" if args.keep_files else ""
        force_arg = " --force" if args.force else ""
        print(f"  {SCRIPT_CMD} delete {target_arg}{keep_arg}{force_arg} --yes")
        return 0

    for path in state_paths:
        try:
            os.remove(path)
            print(f"✅ 已删除状态文件：{path}")
        except FileNotFoundError:
            pass
    if delete_session:
        shutil.rmtree(session_dir)
        print(f"✅ 已删除 setup/session 目录：{session_dir}")
    if delete_tracking:
        shutil.rmtree(tracking_dir)
        print(f"✅ 已删除话题产物目录：{tracking_dir}")
    if tracking_dir and args.keep_files:
        print(f"📁 已按要求保留话题产物目录：{tracking_dir}")
    print("✅ 话题追踪删除完成。")
    return 0


def build_parser():
    parser = argparse.ArgumentParser(description="topic_tracking v2 clean guide")
    sub = parser.add_subparsers(dest="command")

    p = sub.add_parser("init", help="创建 setup 或 briefing 流程")
    p.add_argument("--flow", choices=["setup", "briefing"], required=True)
    p.add_argument("--topic")
    p.add_argument("--setup-token")
    p.add_argument("--tracking-dir")

    p = sub.add_parser("next", help="推进当前 token 到下一步")
    p.add_argument("token")

    p = sub.add_parser("status", help="查看 token 状态")
    p.add_argument("token")

    sub.add_parser("list", help="列出 v2 追踪")

    p = sub.add_parser("delete", aliases=["rm"], help="删除已追踪话题（默认只预览，加 --yes 才删除）")
    target = p.add_mutually_exclusive_group(required=True)
    target.add_argument("--topic", help="按话题名精确匹配删除")
    target.add_argument("--setup-token", help="按 setup_xxx token 删除")
    p.add_argument("--yes", action="store_true", help="确认执行删除；不加时只输出预览")
    p.add_argument("--keep-files", action="store_true", help="只删除状态和 session 记录，保留话题产物目录")
    p.add_argument("--force", action="store_true", help="tracking_dir 缺少 v2 追踪标记时仍允许删除（仍会保护关键目录）")
    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()
    if args.command == "init":
        return cmd_init(args)
    if args.command == "next":
        return cmd_next(args)
    if args.command == "status":
        return cmd_status(args)
    if args.command == "list":
        return cmd_list(args)
    if args.command in ("delete", "rm"):
        return cmd_delete(args)
    parser.print_help()
    return 1


if __name__ == "__main__":
    sys.exit(main())
