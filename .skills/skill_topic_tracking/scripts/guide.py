#!/usr/bin/env python3
"""
topic_tracking guide.

Current event-level flow for setup and briefing. The legacy article-level flow
is archived under archive/legacy_article_flow/.
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
from contextlib import contextmanager
from datetime import date, datetime, timedelta


SCRIPT_PATH = os.path.abspath(__file__)
SCRIPT_DIR = os.path.dirname(SCRIPT_PATH)
SKILL_DIR = os.path.dirname(SCRIPT_DIR)
SESSIONS_DIR = os.path.join(SKILL_DIR, "sessions_v2")
STATE_DIR = os.path.join(SESSIONS_DIR, "_states")
EVENT_TIME_INDEX_PATH = os.path.join(SESSIONS_DIR, "_event_time_index.json")
EVENT_TIME_INDEX_RETENTION_DAYS = 90
EVENT_TIME_INDEX_MAX_ITEMS_PER_TIME = 100
CURRENT_TOPIC_TIMELINE_FILENAME = "tracked_event_timeline.md"
OTHER_TOPICS_TIMELINE_FILENAME = "tracked_other_topics_event_timeline.md"
SCRIPT_CMD = f"python {SCRIPT_PATH}"

DEFAULT_TRACKING_ROOT = "/app/data/所有对话/主对话/热点资讯追踪"
TOOLS_PATH = "/app/data/所有对话/主对话/基础设定/TOOLS.md"
EVENT_FRESHNESS_HOURS = 48
EVENT_FRESHNESS_DAYS = max(1, (EVENT_FRESHNESS_HOURS + 23) // 24)
VERIFY_RUN_MAX_AGE_MINUTES = 10
URL_PATTERN = re.compile(r"^https?://\S+")
URL_CHECK_TIMEOUT = 10
URL_CACHE_TTL_HOURS = 24
MIN_PAGE_TEXT_LENGTH = 200
URL_CHECK_USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
)
SOFT_404_KEYWORDS = ["not found", "page not found", "页面找不到", "页面不存在", "页面已删除", "内容已下线"]
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
GENERIC_SUPPORT_URL_INDEX_NAMES = {
    "index.html", "index.htm", "index.shtml", "index.php",
    "default.html", "default.htm", "home.html", "home.htm",
}
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
    "S2": "确认设定并试运行",
    "B1": "恢复上下文",
    "B2": "阅读资讯并聚合事件",
    "B3": "生成本期日报",
    "B4": "收尾摘要",
}

TOOLS_RULE_BLOCK = """<!-- topic_tracking_delivery_rule:start -->
## 扣子话题追踪日报交付规则

日程追踪系列的日报必须以日程/子会话严格筛选、验证、去重和时效性检查后的产物为最终结论。
主会话验收本次子会话/日程产物时，必须使用日程描述里的 setup_token 运行：verify-run --setup-token "setup_xxxxxxxx"。
验收标准以 verify-run 输出为准：校验通过且明确可交付时才能交付；任一不满足，必须重新运行 briefing，不得直接向用户交付。
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


def _event_time_index_path():
    return EVENT_TIME_INDEX_PATH


def _event_time_index_lock_path(path):
    return f"{path}.lock" if path else ""


@contextmanager
def _locked_event_time_index(path):
    if not path:
        yield
        return
    lock_path = _event_time_index_lock_path(path)
    os.makedirs(os.path.dirname(lock_path), exist_ok=True)
    with open(lock_path, "a+", encoding="utf-8") as lock_file:
        try:
            import fcntl

            fcntl.flock(lock_file.fileno(), fcntl.LOCK_EX)
            yield
        finally:
            try:
                import fcntl

                fcntl.flock(lock_file.fileno(), fcntl.LOCK_UN)
            except Exception:
                pass


def _briefing_artifact_exists(tracking_dir, label):
    if not tracking_dir:
        return False
    patterns = [
        f"{label}_event_list.json",
        f"{label}_summary.json",
        f"{label}_run_status.json",
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


def _json_type_name(value):
    if isinstance(value, dict):
        return "对象"
    if isinstance(value, list):
        return "数组"
    if isinstance(value, str):
        return "字符串"
    if isinstance(value, bool):
        return "布尔值"
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        return "数字"
    if value is None:
        return "null"
    return type(value).__name__


def _read_json_with_error(path):
    if not path:
        return None, "路径为空"
    if not os.path.exists(path):
        return None, f"文件不存在：{path}"
    if not os.path.isfile(path):
        return None, f"路径不是普通文件：{path}"
    try:
        return _read_json(path), None
    except json.JSONDecodeError as exc:
        return None, f"JSON 解析失败：{path}:{exc.lineno}:{exc.colno} {exc.msg}"
    except UnicodeDecodeError as exc:
        return None, f"文件编码错误（需要 UTF-8）：{path}（{exc}）"
    except OSError as exc:
        return None, f"读取文件失败：{path}（{exc}）"


def _read_json_checked(path, *, label, expected_type=None, expected_desc=""):
    data, error = _read_json_with_error(path)
    if error:
        return None, f"{label} {error}"
    if expected_type is not None and not isinstance(data, expected_type):
        desc = expected_desc or getattr(expected_type, "__name__", str(expected_type))
        return None, f"{label} 类型错误：期望 {desc}，实际是 {_json_type_name(data)}：{path}"
    return data, None


def _json_fix_action(path):
    if not path or not os.path.exists(path):
        return f"请写入：{path}"
    return f"请修正：{path}"


def _write_json(path, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def _write_text(path, text):
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


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


def _url_source_domain(url):
    host = _url_host(url).strip(".")
    if not host:
        return ""
    labels = [part for part in host.split(".") if part]
    while labels and labels[0] in {"www", "m", "wap", "mobile"}:
        labels = labels[1:]
    if len(labels) <= 2:
        return ".".join(labels)
    multi_part_suffixes = {
        "com.cn", "net.cn", "org.cn", "gov.cn", "edu.cn", "ac.cn",
        "co.uk", "com.hk", "com.tw", "com.au", "co.jp",
    }
    suffix = ".".join(labels[-2:])
    if suffix in multi_part_suffixes and len(labels) >= 3:
        return ".".join(labels[-3:])
    return ".".join(labels[-2:])


def _is_coze_url(url):
    host = _url_host(url)
    return host == "coze.cn" or host.endswith(".coze.cn")


def _blocked_support_url_reason(url):
    host = _url_host(url)
    for domain in BLOCKED_SUPPORT_URL_DOMAINS:
        if host == domain or host.endswith("." + domain):
            return f"{domain} 属于低质量或可追溯性不足的来源域名，不可作为 support_url"
    return ""


def _generic_support_url_reason(url):
    try:
        parsed = urllib.parse.urlparse(url)
    except Exception:
        return ""

    host = (parsed.netloc or "").strip()
    path = urllib.parse.unquote(parsed.path or "").strip()
    query = (parsed.query or "").strip()
    if not host:
        return ""
    if not path or path == "/":
        return "这是站点首页，不是具体资讯、公告、发布页或原始材料，不能作为 support_url"

    trimmed = path.strip("/")
    if not trimmed:
        return "这是站点首页，不是具体资讯、公告、发布页或原始材料，不能作为 support_url"

    segments = [part for part in trimmed.split("/") if part]
    last_segment = segments[-1].lower() if segments else ""
    if last_segment in GENERIC_SUPPORT_URL_INDEX_NAMES:
        return "这是首页或频道索引页，不是具体事件页面，不能作为 support_url"

    if not query and len(segments) == 1 and not re.search(r"\d", segments[0]):
        return "这是一级频道/栏目页，不是具体事件页面，不能作为 support_url"

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


def _run_status_path(tracking_dir, run_label):
    return os.path.join(tracking_dir, f"{run_label}_run_status.json")


def _briefing_artifact_paths(st):
    tdir = st.get("tracking_dir") or ""
    topic = st.get("topic") or ""
    run_label = st.get("run_label") or date.today().isoformat()
    return {
        "event_list_path": os.path.join(tdir, f"{run_label}_event_list.json") if tdir else "",
        "briefing_md_path": _briefing_md_path(tdir, topic, run_label) if tdir and topic else "",
        "summary_path": os.path.join(tdir, f"{run_label}_summary.json") if tdir else "",
        "run_status_path": _run_status_path(tdir, run_label) if tdir and run_label else "",
    }


def _run_status_payload(st, *, status=None, result=None, message="", errors=None):
    paths = _briefing_artifact_paths(st)
    event_count = _event_count_from_file(paths["event_list_path"]) if paths["event_list_path"] else None
    md_exists = bool(paths["briefing_md_path"] and os.path.isfile(paths["briefing_md_path"]))
    summary = _read_json_if_exists(paths["summary_path"]) if paths["summary_path"] else None
    inferred_result = result
    if not inferred_result:
        if st.get("empty_result"):
            inferred_result = "empty"
        elif md_exists and isinstance(summary, dict):
            inferred_result = "briefing"
        elif status == "BLOCKED":
            inferred_result = "blocked"
        else:
            inferred_result = "running"
    return {
        "schema": "topic_tracking.run_status.v1",
        "status": status or ("DONE" if st.get("current_step") == "DONE" else "RUNNING"),
        "result": inferred_result,
        "legal_for_delivery": bool(status == "DONE" and inferred_result in ("briefing", "empty")),
        "topic": st.get("topic") or "",
        "run_label": st.get("run_label") or "",
        "brief_token": st.get("token") or "",
        "setup_token": st.get("setup_token") or "",
        "current_step": st.get("current_step") or "",
        "completed_steps": st.get("completed_steps", []),
        "skipped_steps": st.get("skipped_steps", []),
        "empty_result": bool(st.get("empty_result")),
        "event_count": event_count,
        "artifacts": {
            "event_list": paths["event_list_path"],
            "briefing_md": paths["briefing_md_path"],
            "summary": paths["summary_path"],
        },
        "artifact_exists": {
            "event_list": bool(paths["event_list_path"] and os.path.isfile(paths["event_list_path"])),
            "briefing_md": md_exists,
            "summary": bool(isinstance(summary, dict)),
        },
        "tracking_dir": st.get("tracking_dir") or "",
        "session_dir": st.get("session_dir") or "",
        "message": message or "",
        "errors": errors or [],
        "created_at": st.get("created_at") or "",
        "updated_at": datetime.now().isoformat(),
    }


def _write_run_status(st, *, status=None, result=None, message="", errors=None):
    if st.get("flow") != "briefing":
        return ""
    paths = _briefing_artifact_paths(st)
    path = paths.get("run_status_path")
    if not path:
        return ""
    payload = _run_status_payload(st, status=status, result=result, message=message, errors=errors)
    _write_json(path, payload)
    st["run_status_path"] = path
    return path


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


def _event_time_index_empty():
    return {
        "schema": "topic_tracking.event_time_index.v1",
        "updated_at": datetime.now().isoformat(),
        "items_by_time": {},
    }


def _event_record_id(record):
    raw = "|".join([
        record.get("event_time", ""),
        record.get("topic", ""),
        record.get("run_label", ""),
        record.get("event", ""),
        record.get("event_list_path", ""),
    ])
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()[:16]


def _run_label_from_event_list_path(path):
    name = os.path.basename(path or "")
    suffix = "_event_list.json"
    if name.endswith(suffix):
        return name[:-len(suffix)]
    return ""


def _event_time_record_from_event(event_obj, group, *, context, event_list_path, run_label, topic):
    event_time = event_obj.get("event_time")
    if not isinstance(event_time, str) or not event_time.strip():
        return None
    try:
        event_time_key = _parse_event_time(event_time).strftime("%Y-%m-%d %H:%M")
    except ValueError:
        return None

    support_urls = group.get("support_urls", []) if isinstance(group, dict) else []
    if not isinstance(support_urls, list):
        support_urls = []
    record = {
        "event_time": event_time_key,
        "event": event_obj.get("event", ""),
        "topic": topic or "",
        "run_label": run_label or "",
        "setup_token": (context or {}).get("setup_token", ""),
        "brief_token": (context or {}).get("brief_token", ""),
        "tracking_dir": (context or {}).get("tracking_dir", ""),
        "event_list_path": os.path.abspath(event_list_path) if event_list_path else "",
        "source_type": group.get("source_type", "") if isinstance(group, dict) else "",
        "relevance_with_topic": group.get("relevance_with_topic", "") if isinstance(group, dict) else "",
        "support_urls": _ordered_unique_urls(support_urls),
        "created_at": datetime.now().isoformat(),
    }
    record["record_id"] = _event_record_id(record)
    return record


def _event_time_records_from_event_list(event_groups, *, context=None, event_list_path="", run_label="", topic=""):
    if not isinstance(event_groups, list):
        return []
    records = []
    for group in event_groups:
        if not isinstance(group, dict):
            continue
        group_events = group.get("events")
        if not isinstance(group_events, list):
            continue
        for event_obj in group_events:
            if not isinstance(event_obj, dict):
                continue
            record = _event_time_record_from_event(
                event_obj,
                group,
                context=context or {},
                event_list_path=event_list_path,
                run_label=run_label,
                topic=topic,
            )
            if record:
                records.append(record)
    return records


def _tracking_dirs_from_states():
    dirs = []
    seen = set()
    for st, _ in _state_items():
        tracking_dir = st.get("tracking_dir")
        if not isinstance(tracking_dir, str) or not tracking_dir.strip():
            continue
        path = os.path.abspath(os.path.expanduser(tracking_dir))
        if path not in seen:
            seen.add(path)
            dirs.append(path)
    return dirs


def _topic_from_tracking_dir(tracking_dir):
    contract = _read_json_if_exists(_contract_path(tracking_dir))
    if isinstance(contract, dict) and isinstance(contract.get("topic"), str):
        return contract["topic"]
    return os.path.basename(os.path.abspath(tracking_dir or "")) or ""


def _backfill_event_time_index():
    import glob

    index = _event_time_index_empty()
    tracking_dirs = _tracking_dirs_from_states()
    root = os.path.abspath(DEFAULT_TRACKING_ROOT)
    if os.path.isdir(root):
        tracking_dirs.append(root)

    seen_dirs = set()
    for tracking_dir in tracking_dirs:
        tracking_dir = os.path.abspath(os.path.expanduser(tracking_dir))
        if tracking_dir in seen_dirs or not os.path.isdir(tracking_dir):
            continue
        seen_dirs.add(tracking_dir)
        pattern = os.path.join(tracking_dir, "**", "*_event_list.json")
        for event_list_path in glob.glob(pattern, recursive=True):
            data = _read_json_if_exists(event_list_path)
            if not isinstance(data, list):
                continue
            item_dir = os.path.dirname(event_list_path)
            topic = _topic_from_tracking_dir(item_dir)
            run_label = _run_label_from_event_list_path(event_list_path)
            has_completed_artifact = (
                bool(run_label)
                and (
                    os.path.exists(os.path.join(item_dir, f"{run_label}_summary.json"))
                    or bool(glob.glob(os.path.join(item_dir, f"*_{run_label}.md")))
                )
            )
            if not has_completed_artifact:
                continue
            context = {
                "topic": topic,
                "run_label": run_label,
                "tracking_dir": item_dir,
                "event_list_path": os.path.abspath(event_list_path),
            }
            _merge_event_time_records(
                index,
                _event_time_records_from_event_list(
                    data,
                    context=context,
                    event_list_path=event_list_path,
                    run_label=run_label,
                    topic=topic,
                ),
            )
    return index


def _read_event_time_index_unlocked(path, *, backfill=True):
    data = _read_json_if_exists(path)
    if isinstance(data, dict) and isinstance(data.get("items_by_time"), dict):
        _prune_event_time_index(data)
        return data
    if backfill:
        data = _backfill_event_time_index()
        _prune_event_time_index(data)
        return data
    return _event_time_index_empty()


def _read_event_time_index(path, *, backfill=True):
    with _locked_event_time_index(path):
        return _read_event_time_index_unlocked(path, backfill=backfill)


def _merge_event_time_records(index, records):
    if not isinstance(index, dict):
        index = _event_time_index_empty()
    by_time = index.setdefault("items_by_time", {})
    existing_ids = set()
    for items in by_time.values():
        if not isinstance(items, list):
            continue
        for item in items:
            if isinstance(item, dict) and item.get("record_id"):
                existing_ids.add(item["record_id"])

    added = 0
    for record in records:
        if not isinstance(record, dict):
            continue
        event_time = record.get("event_time")
        record_id = record.get("record_id") or _event_record_id(record)
        if not event_time or record_id in existing_ids:
            continue
        record["record_id"] = record_id
        by_time.setdefault(event_time, []).append(record)
        existing_ids.add(record_id)
        added += 1

    for event_time, items in list(by_time.items()):
        if not isinstance(items, list):
            by_time[event_time] = []
            continue
        by_time[event_time] = sorted(
            items,
            key=lambda item: (item.get("created_at", ""), item.get("topic", ""), item.get("run_label", "")),
            reverse=True,
        )
    index["updated_at"] = datetime.now().isoformat()
    _prune_event_time_index(index)
    return added


def _prune_event_time_index(index):
    if not isinstance(index, dict):
        return 0
    by_time = index.get("items_by_time")
    if not isinstance(by_time, dict):
        index["items_by_time"] = {}
        return 0

    cutoff = datetime.now() - timedelta(days=EVENT_TIME_INDEX_RETENTION_DAYS)
    removed = 0
    for event_time, items in list(by_time.items()):
        try:
            parsed = _parse_event_time(event_time)
        except (TypeError, ValueError):
            del by_time[event_time]
            removed += 1
            continue
        if parsed < cutoff:
            del by_time[event_time]
            removed += 1
            continue
        if not isinstance(items, list):
            by_time[event_time] = []
            continue
        if len(items) > EVENT_TIME_INDEX_MAX_ITEMS_PER_TIME:
            by_time[event_time] = items[:EVENT_TIME_INDEX_MAX_ITEMS_PER_TIME]
            removed += len(items) - EVENT_TIME_INDEX_MAX_ITEMS_PER_TIME
    return removed


def _write_event_time_index(path, index):
    _prune_event_time_index(index)
    _write_json(path, index)


def _update_event_time_index_unlocked(path, event_groups, *, context):
    if not path or not isinstance(event_groups, list) or not event_groups:
        return 0
    event_list_path = context.get("event_list_path", "")
    run_label = context.get("run_label", "")
    topic = context.get("topic", "")
    records = _event_time_records_from_event_list(
        event_groups,
        context=context,
        event_list_path=event_list_path,
        run_label=run_label,
        topic=topic,
    )
    if not records:
        return 0
    index = _read_event_time_index_unlocked(path)
    added = _merge_event_time_records(index, records)
    if added:
        _write_event_time_index(path, index)
    return added


def _update_event_time_index(path, event_groups, *, context):
    with _locked_event_time_index(path):
        return _update_event_time_index_unlocked(path, event_groups, context=context)


def _is_current_event_time_record(record, context):
    if not isinstance(record, dict) or not isinstance(context, dict):
        return False
    current_event_list = os.path.abspath(context.get("event_list_path", "")) if context.get("event_list_path") else ""
    record_event_list = os.path.abspath(record.get("event_list_path", "")) if record.get("event_list_path") else ""
    if current_event_list and record_event_list and current_event_list == record_event_list:
        return True
    if context.get("brief_token") and record.get("brief_token") == context.get("brief_token"):
        return True
    return (
        bool(context.get("topic"))
        and bool(context.get("run_label"))
        and record.get("topic") == context.get("topic")
        and record.get("run_label") == context.get("run_label")
    )


def _format_event_time_history(items, limit=5):
    visible = [item for item in items if isinstance(item, dict)]
    lines = []
    for item in visible[:limit]:
        urls = item.get("support_urls") if isinstance(item.get("support_urls"), list) else []
        url_text = "，".join(urls[:3]) if urls else "无"
        lines.append(
            f"{item.get('topic', '未知话题')} / {item.get('run_label', '未知run')} / "
            f"{item.get('event', '未知事件')} / 来源: {url_text} / 文件: {item.get('event_list_path', '')}"
        )
    if len(visible) > limit:
        lines.append(f"... 另有 {len(visible) - limit} 条同时间历史记录")
    return "；".join(lines)


def _sort_event_time_history_for_context(items, context):
    topic = (context or {}).get("topic") if isinstance(context, dict) else ""
    return sorted(
        [item for item in items if isinstance(item, dict)],
        key=lambda item: (
            item.get("topic") == topic,
            item.get("created_at", ""),
            item.get("run_label", ""),
        ),
        reverse=True,
    )


def _event_time_validation_context(st, event_list_path):
    return {
        "topic": st.get("topic") or "",
        "run_label": st.get("run_label") or "",
        "setup_token": st.get("setup_token") or "",
        "brief_token": st.get("token") or "",
        "tracking_dir": st.get("tracking_dir") or "",
        "event_list_path": os.path.abspath(event_list_path) if event_list_path else "",
    }


def _completed_event_list_paths(search_dir):
    import glob

    if not search_dir or not os.path.isdir(search_dir):
        return []
    paths = []
    for event_list_path in glob.glob(os.path.join(search_dir, "**", "*_event_list.json"), recursive=True):
        item_dir = os.path.dirname(event_list_path)
        run_label = _run_label_from_event_list_path(event_list_path)
        if not run_label:
            continue
        has_completed_artifact = (
            os.path.exists(os.path.join(item_dir, f"{run_label}_summary.json"))
            or bool(glob.glob(os.path.join(item_dir, f"*_{run_label}.md")))
        )
        if has_completed_artifact:
            paths.append(event_list_path)
    return sorted(paths)


def _timeline_search_dirs(current_tracking_dir):
    dirs = [DEFAULT_TRACKING_ROOT]
    dirs.extend(_tracking_dirs_from_states())
    if current_tracking_dir:
        dirs.append(current_tracking_dir)

    seen = set()
    result = []
    for path in dirs:
        if not isinstance(path, str) or not path.strip():
            continue
        abs_path = os.path.abspath(os.path.expanduser(path))
        if abs_path in seen or not os.path.isdir(abs_path):
            continue
        seen.add(abs_path)
        result.append(abs_path)
    return result


def _record_tracking_dir(record):
    if not isinstance(record, dict):
        return ""
    tracking_dir = record.get("tracking_dir")
    if isinstance(tracking_dir, str) and tracking_dir.strip():
        return os.path.abspath(os.path.expanduser(tracking_dir))
    event_list_path = record.get("event_list_path")
    if isinstance(event_list_path, str) and event_list_path.strip():
        return os.path.abspath(os.path.dirname(event_list_path))
    return ""


def _timeline_records_from_event_list(event_list_path):
    data = _read_json_if_exists(event_list_path)
    if not isinstance(data, list):
        return []
    item_dir = os.path.abspath(os.path.dirname(event_list_path))
    run_label = _run_label_from_event_list_path(event_list_path)
    topic = _topic_from_tracking_dir(item_dir)
    context = {
        "topic": topic,
        "run_label": run_label,
        "tracking_dir": item_dir,
        "event_list_path": os.path.abspath(event_list_path),
    }
    return _event_time_records_from_event_list(
        data,
        context=context,
        event_list_path=event_list_path,
        run_label=run_label,
        topic=topic,
    )


def _all_completed_timeline_records(current_tracking_dir):
    records_by_id = {}
    for search_dir in _timeline_search_dirs(current_tracking_dir):
        for event_list_path in _completed_event_list_paths(search_dir):
            for record in _timeline_records_from_event_list(event_list_path):
                record_id = record.get("record_id") or _event_record_id(record)
                if not record_id:
                    continue
                records_by_id.setdefault(record_id, record)
    return list(records_by_id.values())


def _timeline_run_sort_key(run_label):
    value = str(run_label or "")
    match = re.match(r"^(\d{4}-\d{2}-\d{2})(?:_v(\d+))?$", value)
    if not match:
        return (value, 0)
    return (match.group(1), int(match.group(2) or "1"))


def _timeline_one_line(value):
    return re.sub(r"\s+", " ", str(value or "")).strip()


def _format_tracked_event_timeline(records, *, title, include_topic):
    grouped = {}
    for record in records:
        if not isinstance(record, dict):
            continue
        run_label = _timeline_one_line(record.get("run_label"))
        event_time = _timeline_one_line(record.get("event_time"))
        event = _timeline_one_line(record.get("event"))
        if not run_label or not event_time or not event:
            continue
        grouped.setdefault(run_label, []).append(record)

    if include_topic:
        usage_note = "!!! 【跨话题防重】用途：发现跨话题重复或相邻事件；发现相似事件时必须谨慎确认，严禁把其他话题已覆盖的同一事实进展换个话题名重复收录。"
        warning_note = "!!! 【禁止重复】如果候选事件与本文件中的事件只是同一事实、同一时间线、同一进展的换标题/换角度表达，不得写入本期 event_list；只有确有新的事实增量时才可收录。"
        line_format = "每行格式：事件真实发生时间｜话题｜事件。"
    else:
        usage_note = "!!! 【当前话题强约束】用途：当前话题严格去重；本文件中的事件表示已经交付过。"
        warning_note = "!!! 【严禁重复】同一事件、同一时间线、同一事实进展、同一来源链条已经覆盖过，就绝对不得再次写入本期 event_list 或日报；不要换标题、换表述、换来源重复收录。"
        line_format = "每行格式：事件真实发生时间｜事件。"

    lines = [
        f"# {title}",
        "",
        "> 该文件由 B1 动态读取已有完成简报生成，放在当前话题目录下；只读即可，不要手工维护。",
        "> `## 2026-05-07 简报` 表示哪一期简报已经交付过；每行开头的 `2026-05-07 09:30` 才是事件真实发生时间。",
        "> 按简报时间倒序排列，最新简报在最前；同一期内按事件真实发生时间倒序排列，最新事件在最前。默认优先读取前 100 条事件即可。",
        f"> {line_format}",
        f"> {usage_note}",
        f"> {warning_note}",
        "",
    ]
    if not grouped:
        lines.append("- 暂无已追踪事件")
        lines.append("")
        return "\n".join(lines)

    for run_label in sorted(grouped.keys(), key=_timeline_run_sort_key, reverse=True):
        lines.append(f"## {run_label} 简报")
        lines.append("")
        for record in sorted(
            grouped[run_label],
            key=lambda item: (_timeline_one_line(item.get("event_time")), _timeline_one_line(item.get("event"))),
            reverse=True,
        ):
            event_time = _timeline_one_line(record.get("event_time"))
            event = _timeline_one_line(record.get("event"))
            if include_topic:
                topic = _timeline_one_line(record.get("topic")) or "未知话题"
                lines.append(f"- {event_time}｜{topic}｜{event}")
            else:
                lines.append(f"- {event_time}｜{event}")
        lines.append("")
    return "\n".join(lines)


def _refresh_tracked_event_timelines(tracking_dir):
    if not tracking_dir:
        return "", "", False, False
    current_dir = os.path.abspath(os.path.expanduser(tracking_dir or ""))
    all_records = _all_completed_timeline_records(current_dir)
    current_records = []
    other_records = []
    for record in all_records:
        if _record_tracking_dir(record) == current_dir:
            current_records.append(record)
        else:
            other_records.append(record)

    current_path = os.path.join(current_dir, CURRENT_TOPIC_TIMELINE_FILENAME)
    other_path = os.path.join(current_dir, OTHER_TOPICS_TIMELINE_FILENAME)
    _write_text(
        current_path,
        _format_tracked_event_timeline(
            current_records,
            title="当前话题已追踪事件时间线",
            include_topic=False,
        ),
    )
    _write_text(
        other_path,
        _format_tracked_event_timeline(
            other_records,
            title="其他话题已追踪事件时间线",
            include_topic=True,
        ),
    )
    return current_path, other_path, bool(current_records), bool(other_records)


def _b1_timeline_lines(current_path, other_path, current_has_events, other_has_events):
    lines = []
    if current_has_events:
        lines.append(f"- 当前话题已追踪事件时间线（!!! 强约束，严禁重复，必须重点读取）：{current_path}")
    if other_has_events:
        lines.append(f"- 其他话题已追踪事件时间线（!!! 跨话题防重，也要读取，严禁换话题重复收录）：{other_path}")
    return "\n".join(lines)


def _b1_timeline_notes(current_has_events, other_has_events):
    lines = []
    if current_has_events:
        lines.append("- !!! 严禁重复：重点理解当前话题已经覆盖过哪些事件、时间线和事实进展；后续不得把已覆盖事件换标题、换来源、换表述重复写入 event_list。")
    if other_has_events:
        lines.append("- !!! 跨话题防重：如果其他话题时间线里有相似事件，必须确认是否同一事实进展；严禁把其他话题已覆盖事件换个话题名重复收录。")
    return "\n".join(lines)


def _b2_timeline_confirm_line(current_has_events, other_has_events):
    parts = ["追踪定义", "用户偏好", "历史 summary"]
    if current_has_events:
        parts.append("当前话题时间线")
    if other_has_events:
        parts.append("其他话题时间线")
    return f"- 沿用 B1 已恢复的{'、'.join(parts)}；不要重新做上下文恢复。"


def _b2_timeline_dedup_lines(current_has_events, other_has_events):
    lines = []
    if current_has_events:
        lines.append("- !!! 判断是否重复时，必须以 B1 已读取的当前话题时间线原文为准。")
        lines.append("- !!! 严禁重复：当前话题时间线中已覆盖的事件、时间线、来源或明确不应重复的内容，不得再次写入 event_list。")
    if other_has_events:
        lines.append("- !!! 跨话题防重：其他话题时间线作为辅助提醒；发现跨话题相似事件时必须谨慎确认，严禁换话题重复收录，但不要机械过滤真正不同的新事件。")
    lines.append("- 如果新资讯只是对历史事件的转载、复述、延伸评论或换标题重发，不算本期新事件；只有出现新的事实变化、新时间点、新官方动作或新的可验证进展，才可以作为新事件组提交。")
    return "\n".join(lines)


def _b2_timeline_core_line(current_has_events, other_has_events):
    if current_has_events and other_has_events:
        return "5. 必须沿用 B1 已恢复的用户偏好和话题边界；!!! 历史去重必须以当前话题时间线原文为准，其他话题时间线用于跨话题防重。历史已覆盖或明确不应重复的事件，严禁再次整理。"
    if current_has_events:
        return "5. 必须沿用 B1 已恢复的用户偏好和话题边界；!!! 历史去重必须以当前话题时间线原文为准。历史已覆盖或明确不应重复的事件，严禁再次整理。"
    if other_has_events:
        return "5. 必须沿用 B1 已恢复的用户偏好和话题边界；!!! 其他话题时间线用于跨话题防重，发现相似事件必须谨慎确认，严禁换话题重复收录，但不要机械过滤真正不同的新事件。"
    return "5. 必须沿用 B1 已恢复的用户偏好和话题边界；如果发现资讯只是对已知历史事件的转载、复述、延伸评论或换标题重发，不要再次整理。"


def _validate_event_list(
    event_groups,
    *,
    cache_dir=None,
    low_volume_confirmation=None,
    url_blacklist_path=None,
    authority_requirement="high",
    event_time_index_path=None,
    event_time_index=None,
    current_context=None,
):
    now = datetime.now()
    window_start = now - timedelta(hours=EVENT_FRESHNESS_HOURS)
    errors = []
    new_blacklist_entries = []
    url_blacklist = _load_url_blacklist(url_blacklist_path)
    if not isinstance(event_time_index, dict):
        event_time_index = _read_event_time_index(event_time_index_path) if event_time_index_path else _event_time_index_empty()
    event_time_history = event_time_index.get("items_by_time", {}) if isinstance(event_time_index, dict) else {}
    current_context = current_context or {}
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
                generic_reason = _generic_support_url_reason(url)
                if generic_reason:
                    errors.append(f"[{label}] support_url 过于泛化，不采用：{url}；{generic_reason}。请更换为能直接支撑事件事实和时间的具体页面。")

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
            source_domains = [_url_source_domain(url) for url in unique_urls if isinstance(url, str) and URL_PATTERN.match(url)]
            unique_source_domains = sorted({domain for domain in source_domains if domain})
            if len(unique_urls) < min_support_urls:
                errors.append(
                    f"[{label}] 当前话题要求 support_urls 至少需要 {min_support_urls} 个不同且可达的 URL，且来自不同来源域名；"
                    "如果找不到足够可靠支撑，请更换事件组，不要降低来源要求。"
                )
            if min_support_urls > 1 and len(unique_source_domains) < min_support_urls:
                errors.append(
                    f"[{label}] 当前话题要求 support_urls 至少来自 {min_support_urls} 个不同来源域名；"
                    f"当前只有 {len(unique_source_domains)} 个：{', '.join(unique_source_domains) or '无'}。"
                    "同一域名下多个链接不能凑多源，请更换为不同机构/站点的来源。"
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
                if _blocked_support_url_reason(url) or _generic_support_url_reason(url):
                    continue
                reachable, page_text = _fetch_page_text(url, cache_dir=cache_dir)
                if not reachable:
                    errors.append(f"[{label}] support_url 不可达或疑似软404: {url}")
                    continue
                timestamps = _extract_precise_page_timestamps(page_text)
                if not timestamps:
                    errors.append(
                        f"[{label}] support_url 未解析到明确分钟级发布时间，不能作为本期来源：{url}。"
                        "请更换为页面内容或元信息中包含明确发布时间、且能直接支撑事件事实和时间的具体页面。"
                    )
                    continue
                _, page_time, raw_time = timestamps[0]
                if page_time < window_start:
                    errors.append(
                        f"[{label}] support_url 发布时间不在最近 {EVENT_FRESHNESS_HOURS} 小时内：{url}；"
                        f"解析到 {raw_time}。请删除该来源并更换为符合时效的新来源，"
                        "不要把旧来源用于本期事件。"
                    )
                    new_blacklist_entries.extend(_blacklist_entries_for_urls(
                        [url],
                        reason="freshness",
                        label=label,
                        detail=f"support_url 发布时间 {raw_time} 早于最早允许时间 {window_start.strftime('%Y-%m-%d %H:%M')}",
                    ))
                if page_time - now > timedelta(minutes=10):
                    errors.append(
                        f"[{label}] support_url 发布时间是未来时间：{url}；解析到 {raw_time}。"
                        "请核实来源，不要使用时间异常的页面。"
                    )
                    new_blacklist_entries.extend(_blacklist_entries_for_urls(
                        [url],
                        reason="freshness",
                        label=label,
                        detail=f"support_url 发布时间 {raw_time} 是未来时间",
                    ))

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
                historical_items = [
                    record for record in event_time_history.get(event_time_key, [])
                    if not _is_current_event_time_record(record, current_context)
                ]
                historical_items = _sort_event_time_history_for_context(historical_items, current_context)
                duplicate_confirmed = (
                    event_obj.get("time_duplicate_confirmed") is True
                    and isinstance(event_obj.get("time_duplicate_note"), str)
                    and len(event_obj.get("time_duplicate_note", "").strip()) >= 5
                )
                if historical_items and not duplicate_confirmed:
                    errors.append(
                        f"[历史 event_time 重复: {event_time_key}] 当前事件 {event_label}《{event_obj.get('event', '')}》"
                        f"命中全局 event_time 索引中 {len(historical_items)} 条历史记录，可能是跨话题或跨 run 的重复事件。"
                        f"历史上下文：{_format_event_time_history(historical_items)}。"
                        "请确认是否重复；如确认不是重复，请在该 events[] 对象加入 "
                        '"time_duplicate_confirmed": true 和 "time_duplicate_note": "说明与历史记录的差异"，否则请合并或删除该事件。'
                    )
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
    events, error = _read_json_checked(
        event_list_path,
        label="event_list",
        expected_type=list,
        expected_desc="数组",
    )
    if error:
        return {"pass": False, "error": error}

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
    event_time_index_path=None,
    current_context=None,
):
    events, error = _read_json_checked(
        event_list_path,
        label="event_list",
        expected_type=list,
        expected_desc="数组",
    )
    if error:
        return {"pass": False, "errors": [error]}, None
    confirmation = _read_json_if_exists(low_volume_confirmation_path) if low_volume_confirmation_path else None
    return _validate_event_list(
        events,
        cache_dir=cache_dir,
        low_volume_confirmation=confirmation,
        url_blacklist_path=url_blacklist_path,
        authority_requirement=authority_requirement,
        event_time_index_path=event_time_index_path,
        current_context=current_context,
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
            "default": f"authority_requirement={authority_requirement} 时，每个事件组至少需要 {support_url_min} 个不同来源域名的可达支撑 URL；不确定来源或时间时不要提交事件。",
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


def _parse_after_time(value):
    if not value:
        return None, None
    raw = value.strip()
    try:
        return datetime.fromisoformat(raw), None
    except ValueError:
        pass
    try:
        return datetime.strptime(raw, "%Y-%m-%d %H:%M:%S"), None
    except ValueError:
        pass
    try:
        return datetime.strptime(raw, "%Y-%m-%d %H:%M"), None
    except ValueError:
        return None, "after 时间格式不正确，请使用 YYYY-MM-DDTHH:MM:SS 或 YYYY-MM-DD HH:MM:SS"


def _state_time(st, key):
    value = st.get(key)
    if not isinstance(value, str) or not value.strip():
        return None
    try:
        return datetime.fromisoformat(value.strip())
    except ValueError:
        return None


def _now_like(value):
    if value and value.tzinfo is not None and value.utcoffset() is not None:
        return datetime.now(value.tzinfo)
    return datetime.now()


def _select_briefing_for_verify(args):
    after_time, after_error = _parse_after_time(getattr(args, "after", None))
    if after_error:
        return None, after_error

    run_status = getattr(args, "run_status", None)
    if run_status:
        status_path = os.path.abspath(os.path.expanduser(run_status))
        status_data, error = _read_json_checked(
            status_path,
            label="run_status",
            expected_type=dict,
            expected_desc="对象",
        )
        if error:
            return None, error
        token = status_data.get("brief_token")
        if not isinstance(token, str) or not token.strip():
            return None, f"run_status 缺少 brief_token，无法定位本次运行：{status_path}"
        st = load_state(token.strip())
        expected_path = os.path.abspath(_briefing_artifact_paths(st).get("run_status_path") or "")
        if expected_path != status_path:
            return None, f"run_status 文件不属于该 briefing 运行：{status_path}"
        return st, None

    if getattr(args, "token", None):
        st = load_state(args.token)
        if after_time:
            created_at = _state_time(st, "created_at")
            if not created_at or created_at < after_time:
                return None, f"briefing token 创建时间早于本次运行开始时间：{st.get('created_at') or '未知'}"
        return st, None

    setup_token = getattr(args, "setup_token", None)
    if not setup_token:
        return None, "必须提供 --setup-token；内部排障时也可提供 token 或 --run-status"

    candidates = []
    for st, _ in _briefing_items_for_setup(setup_token):
        if getattr(args, "run_label", None) and st.get("run_label") != args.run_label:
            continue
        if after_time:
            created_at = _state_time(st, "created_at")
            if not created_at or created_at < after_time:
                continue
        candidates.append(st)

    if not candidates:
        hint = f"未找到 setup_token={setup_token} 对应的 briefing 运行"
        if after_time:
            hint += f"（after={args.after} 之后）"
        if getattr(args, "run_label", None):
            hint += f"（run_label={args.run_label}）"
        return None, hint

    candidates.sort(key=lambda item: item.get("created_at") or item.get("updated_at") or "", reverse=True)
    return candidates[0], None


def _verify_briefing_state(st):
    errors = []
    if st.get("flow") != "briefing":
        errors.append("token 不是 briefing 流程")
    if st.get("current_step") != "DONE":
        errors.append(f"流程未完成，当前步骤是 {st.get('current_step') or '未知'}")

    topic = st.get("topic") or ""
    run_label = st.get("run_label") or ""
    setup_token = st.get("setup_token") or ""
    if not topic:
        errors.append("缺少 topic")
    if not run_label:
        errors.append("缺少 run_label")
    if not setup_token:
        errors.append("缺少 setup_token")

    paths = _briefing_artifact_paths(st)
    event_list_path = paths["event_list_path"]
    md_path = paths["briefing_md_path"]
    summary_path = paths["summary_path"]
    events, event_list_error = _read_json_checked(
        event_list_path,
        label="event_list",
        expected_type=list,
        expected_desc="数组",
    )
    if event_list_error:
        errors.append(event_list_error)
        event_count = None
    else:
        event_count = _event_count_from_data(events)

    empty_result = bool(st.get("empty_result")) or event_count == 0
    result = "empty" if empty_result else "briefing"

    if empty_result:
        if event_count == 0 and not st.get("empty_result"):
            errors.append("event_list 为空，但流程状态没有标记 empty_result")
        if isinstance(events, list) and len(events) != 0:
            errors.append("状态标记为空结果，但 event_list 不是空数组")
    else:
        if not isinstance(event_count, int) or event_count <= 0:
            errors.append("非空日报必须包含至少 1 个事件")
        if not os.path.isfile(md_path):
            errors.append(f"日报文件不存在：{md_path}")
        _, summary_error = _read_json_checked(
            summary_path,
            label="summary.json",
            expected_type=dict,
            expected_desc="对象",
        )
        if summary_error:
            errors.append(summary_error)

    return {
        "pass": not errors,
        "errors": errors,
        "topic": topic,
        "run_label": run_label,
        "brief_token": st.get("token") or "",
        "setup_token": setup_token,
        "completed_at": st.get("updated_at") or st.get("created_at") or "",
        "result": result,
        "event_count": event_count,
        "event_list_path": event_list_path,
        "briefing_md_path": md_path,
        "summary_path": summary_path,
        "run_status_path": paths["run_status_path"],
        "rerun_command": f'{SCRIPT_CMD} init --flow briefing --setup-token "{setup_token}"' if setup_token else "",
    }


def _setup_topic_for_token(setup_token):
    if not setup_token:
        return ""
    matches = _find_setup_matches(setup_token=setup_token)
    if not matches:
        return ""
    return matches[0][0].get("topic") or ""


def _print_rerun_briefing_action(setup_token, topic=None):
    if not setup_token:
        return
    topic_label = topic or _setup_topic_for_token(setup_token) or "该话题"
    briefing_cmd = f'{SCRIPT_CMD} init --flow briefing --setup-token "{setup_token}"'
    print("主会话动作：")
    print("不得向用户交付当前结果。")
    print("请使用 session_spawn 创建一个新的子会话任务重新运行 briefing，任务描述使用以下内容：")
    print()
    print("```markdown")
    print(f"请为「{topic_label}」生成本期结果。已有追踪已配置好，不要重新创建追踪。")
    print("1. 先加载并阅读 topic_tracking 技能。")
    print(f"2. 执行命令：`{briefing_cmd}`。")
    print("3. 按脚本指引完成完整 briefing 流程，直到状态为 DONE；如果中途校验未通过，按提示修正后继续，不要只运行 init 就结束。")
    print("4. 若没有符合标准的新内容，按脚本的暂无动态流程完成，不要降低筛选标准。")
    print("5. 完成后只回传最终状态和脚本要求输出的信息，不要直接发给用户。")
    print("```")
    print()
    print("新子会话完成后，主会话必须重新运行 verify-run 验收，通过后再按验收输出交付。")


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

先认真理解用户到底要追什么，不要只拆关键词。S1 负责先根据用户原始需求、当前对话上下文和必要的搜索/浏览，拟定一版可确认的追踪设定；除非缺少无法合理推断的关键信息，否则不要在 S1 反复打断用户。S2 会统一向用户确认设定。

请写入：

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
   - `high`：信息真实性要求高，适用于政策、监管、财经、医疗、安全、企业重大事项、资讯/事实类捕捉、突发事件等；后续每个事件组至少需要 3 个不同来源域名的可达 support_urls。
   - `low`：信息真实性要求较低或天然难以多源验证，适用于攻略、教程、经验、玩法、如何用 AI 赚钱、路线建议等；后续每个事件组至少需要 1 个可达 support_url。
4. `topic_analysis.authority_policy` 要解释为什么选择 high 或 low，以及哪些来源可接受。
5. `focus_directions` 是后续搜索的方向，不是最终栏目标题，可以动态服务于搜索。
6. 如果用户没有明确偏好，`user_preference` 写空字符串即可，不要编。
7. S1 只是拟定追踪设定，不要创建子会话、不要创建日程、不要开始 briefing 试运行。

完成后运行：

```bash
{SCRIPT_CMD} next {token}
```"""

    if flow == "setup" and step == "S2":
        setup_token = st["token"]
        briefing_cmd = f'{SCRIPT_CMD} init --flow briefing --setup-token "{setup_token}"'
        quick_mode = bool(st.get("quick"))
        if quick_mode:
            confirm_instructions = """快速模式：跳过确认，直接试运行。

本 setup 是通过 `--quick` 启动的，通常用于旧版配置升级、用户明确要求快速跑一版，或用户已经授权 agent 自行决定。不要再向用户确认追踪设定，也不要直接创建日程；先进入首次 briefing 试运行。"""
            next_action_prefix = "quick 模式已跳过确认，现在"
        else:
            confirm_instructions = """先确认，再试运行。

默认必须先把 S1 拟定的追踪设定用自然语言发给用户确认，不要直接创建子会话、不要直接创建日程。只有当用户已经明确表达“快速跑一下”“先跑一版”“你定就行”“不用确认”“赶紧跑”等跳过确认意图时，才可以跳过确认并直接进入首次试运行。

向用户确认时，只说用户能理解的内容，不要暴露 token、内部目录、JSON 文件名或阶段名。建议包含：
- 这个追踪到底追什么，以及不追什么；
- 主要关注方向；
- 来源严谨度：高严谨度会要求多源支撑，低严谨度适合攻略/经验/玩法类话题；
- 用户偏好、排除项和建议频率；
- 说明确认后会先试跑一版，试运行成功后才会创建日程。

确认话术示例：

```text
我先按下面这版来建追踪，你确认一下：

追踪定义：……
会收录：……
不收录：……
重点方向：……
来源要求：……
频率建议：……

确认后我会先试跑一版；试运行成功后再创建后续定时追踪。
```"""
            next_action_prefix = "用户确认后，或用户此前已经明确要求快速试跑，再"
        return f"""「{topic}」追踪设定已保存。

{confirm_instructions}

{next_action_prefix}按需要做两件事。给子会话或日程的描述要保持简洁，但必须说清楚：先加载技能、再执行命令、并按脚本指引完整跑到 DONE。

1. 首次试运行：新开一个子会话，任务描述可直接使用下面内容。

```markdown
请为「{topic}」生成本期结果。已有追踪已配置好，不要重新创建追踪。
1. 先加载并阅读 topic_tracking 技能。
2. 执行命令：`{briefing_cmd}`。
3. 按脚本指引完成完整 briefing 流程，直到状态为 DONE；如果中途校验未通过，按提示修正后继续，不要只运行 init 就结束。
4. 若没有符合标准的新内容，按脚本的暂无动态流程完成，不要降低筛选标准。
5. 完成后只回传最终状态和脚本要求重复的信息，不要直接发给用户。
```

2. 创建日程时，标题和描述保持简洁：

标题：

```text
扣子话题追踪 - 「{topic}」
```

描述：

```text
扣子话题追踪 - 「{topic}」
版本：V2

1. 先加载并阅读 topic_tracking 技能。
2. 执行命令：{briefing_cmd}
3. 按脚本指引完成完整 briefing 流程，直到状态为 DONE；如果中途校验未通过，按提示修正后继续，不要只运行 init 就结束。
4. 完成后只重复脚本要求的信息。
```

日程触发后只运行 briefing，不要重新 setup。必须先等首次试运行成功返回最终结果，再创建日程；试运行未成功前不要创建日程。完成试运行或日程设置后运行：

```bash
{SCRIPT_CMD} next {token}
```"""

    if flow == "briefing" and step == "B1":
        contract_path = _contract_path(tdir)
        b1_path = os.path.join(sdir, "B1_context.json")
        summaries = _recent_summary_paths(tdir, limit=1)
        current_timeline_path, other_timeline_path, current_has_events, other_has_events = _refresh_tracked_event_timelines(tdir)
        timeline_lines = _b1_timeline_lines(current_timeline_path, other_timeline_path, current_has_events, other_has_events)
        timeline_notes = _b1_timeline_notes(current_has_events, other_has_events)
        return f"""B1：恢复「{topic}」的追踪上下文，并写入 B1_context.json。

本步骤只做上下文恢复：不搜索外网、不产出事件、不写日报。你需要先读设定和历史，再把后续 B2 必须遵守的追踪定义、用户偏好和去重线索整理进上下文文件。

按顺序完成：

1. 读取追踪设定，确认本次要追踪什么
- 文件：{contract_path}
- 重点理解：话题定义、权威性要求、关注方向和用户偏好。

2. 读取历史，确认哪些内容不要重复
- 最近一期 summary（用于理解上期主线）：
{_format_path_list(summaries)}
{timeline_lines}
{timeline_notes}

3. 做一次自我回忆，补充用户偏好和避坑点
- 先回忆当前对话、历史反馈和你自己记得的用户偏好、边界、避坑点。
- 如果当前环境提供 `memory_search`，用话题名、近义表达、用户偏好关键词各检索一次；如无结果，在 `context_summary` 里简要说明即可。
- `memory_search` 只用于找自己的记忆和历史反馈，不是外网搜索。

4. 写入上下文文件

{b1_path}

JSON 格式：

```json
{{
  "context_summary": "读完追踪设定、最近一期 summary、两条事件时间线，并完成自我回忆后的上下文总结。说明本话题要追什么、用户偏好和边界是什么、历史大致覆盖过哪些方向、本期搜索和去重时最需要注意什么。"
}}
```

要求：
1. 只写 B1_context.json，不搜索外网，不写 event_list，不写日报。
2. B1_context.json 只允许包含 `context_summary` 一个字段。
3. 当前话题时间线是强约束，其他话题时间线是辅助提醒；不要把已覆盖事件重复写入本期 event_list。
4. `context_summary` 是内部上下文总结，不要暴露给用户。
5. 如果今天同一话题已经跑过，本次仍是新版本；历史只用于去重，不要让主会话合并多个版本。
{_same_day_version_hint(st.get("run_label"))}
完成后运行：

```bash
{SCRIPT_CMD} next {token}
```"""

    if flow == "briefing" and step == "B2":
        run_label = st.get("run_label") or date.today().isoformat()
        event_list_path = os.path.join(tdir, f"{run_label}_event_list.json")
        now = datetime.now()
        window_start = now - timedelta(hours=EVENT_FRESHNESS_HOURS)
        freshness_days = EVENT_FRESHNESS_DAYS
        authority_requirement = _contract_authority_requirement(tdir)
        support_url_min = _support_url_min_count(authority_requirement)
        _, _, current_has_events, other_has_events = _refresh_tracked_event_timelines(tdir)
        return f"""阅读大量资讯并聚合「{topic}」本期相关事件。

开始前确认：
{_b2_timeline_confirm_line(current_has_events, other_has_events)}
- 如对话题边界或来源要求不确定，再回看追踪设定：{_contract_path(tdir)}

历史去重要求：
{_b2_timeline_dedup_lines(current_has_events, other_has_events)}

本话题来源要求：
- 每个事件组的 `support_urls` 至少需要 {support_url_min} 个不同来源域名的可达 URL。
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
6. 每一个 `support_url` 都必须能从页面内容或元信息中解析出明确到分钟的发布时间，且发布时间必须在最近 {EVENT_FRESHNESS_HOURS} 小时内；解析不到、发布时间过旧或时间异常都会被脚本报错。
7. `support_urls` 必须共同指向同一个事件组，并共同支撑组内所有事件的事实和时间；不要把多篇转载同一段文字当作独立验证。如果本话题只要求 1 条来源，该 URL 仍必须可达、质量可接受，并能支撑事件事实和时间。
8. 如果仍无法确认事件是否真实、真实发生时间是否在最近 {EVENT_FRESHNESS_HOURS} 小时内，或支撑 URL 是否可靠，不要提交该事件；应换其他事件，或写入空数组。

核心思想：
1. “事件组”是一组 `support_urls` 可以共同支撑的一组事实变化；一个发布会、一个官方公告或一组报道可能同时包含多个事件。
2. “事件”是最近 {EVENT_FRESHNESS_HOURS} 小时内发生、符合「{topic}」定义和用户偏好的具体事实变化；主体是事件，不是资讯。
3. 多个 URL 提到同一组事实变化时，不要拆成多条资讯；应合并成同一个事件组，并把这些 URL 放入同一个 `support_urls`。
4. 你要从大量资讯中识别真正围绕「{topic}」的新事件，再为事件组寻找支撑来源。
{_b2_timeline_core_line(current_has_events, other_has_events)}
6. 如果事件来自转载、社评、专业账号整理或聚合资讯，必须进一步寻找事件源头，确认真实发生时间和事实是否成立；不能把转载发布时间当作事件发生时间。
7. 事件时间以主体事件真实发生时间为准；网页发布时间只作为辅助证据。
8. 本期只允许最近 {EVENT_FRESHNESS_HOURS} 小时内发生的事件。当前时间：{now.strftime('%Y-%m-%d %H:%M')}；最早允许事件时间：{window_start.strftime('%Y-%m-%d %H:%M')}。
9. 目标是收集 {TARGET_EVENT_GROUPS} 个左右的高质量事件组；如果近期事件丰富，可以多给，不需要压缩到 5 个。
10. 如果某个事件真实发生时间不在最近 {EVENT_FRESHNESS_HOURS} 小时内，该事件不合格。不要为了通过校验修改事件时间，应删除该事件并寻找其他符合时效的新事件。
11. 脚本会用全局 event_time 索引检查跨话题、跨 run 的同时间事件；如果命中历史同一时间，会把历史事件、话题、run 和来源上下文报出来。你必须确认是否重复；确认不是重复后，在对应 event 对象里写 `time_duplicate_confirmed: true` 和 `time_duplicate_note` 说明与历史记录的差异。
12. 如果当前 event_list 内两个事件必须使用完全相同的 `event_time`，也要先确认它们不是同一事件被拆分；确认后在对应 event 对象里写 `time_duplicate_confirmed: true` 和 `time_duplicate_note` 说明差异。
13. 只有与「{topic}」强相关的事件组才能提交；弱相关、不相关、只是背景提及或相邻话题都不要放入 event_list。
14. 已经因为时效性或相关性被脚本打回过的 URL 会进入本次黑名单；不要复用黑名单 URL，也不要通过改写 event_time 或 relevance_level 让它重新通过。
15. `support_urls` 不允许使用低质量域名黑名单：{_format_blocked_support_domains()}。命中时说明来源质量低，不采用，请更换为官方、权威媒体或更可追溯的来源。
16. `support_urls` 不允许使用站点首页、频道首页、索引页或过于泛化的主页域名；必须是能直接支撑事件事实和时间的具体资讯页、公告页、发布页或原始材料页。
17. `support_urls` 中每一个 URL 都必须能解析出明确到分钟的页面发布时间，并且该发布时间在最近 {EVENT_FRESHNESS_HOURS} 小时内；不要用旧闻、旧转载或无法提取发布时间的页面凑数。
18. 本话题每个事件组 support_urls 至少需要 {support_url_min} 个不同来源域名的可达 URL；同一来源域名下多个链接不能凑多源。

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
2. `events`：该组来源共同支撑的事件数组；每个事件必须写 `event`、`event_time`、`relevance_level`，如遇同一时间点命中本次或历史记录且确认不重复，可额外写 `time_duplicate_confirmed` 和 `time_duplicate_note`。
3. `event`：事件本身，不是文章标题，也不是某篇资讯的摘要。
4. `event_time`：事件真实发生时间，格式必须是 `YYYY-MM-DD HH:MM`，且必须在最近 {EVENT_FRESHNESS_HOURS} 小时内；不能为了保留旧事件而改写时间。
5. `time_duplicate_confirmed` / `time_duplicate_note`：只有脚本提示同一 `event_time` 可能重复、且你确认不是重复事件时才填写；note 必须说明与历史事件或同时间事件的差异，不能只写“已确认”。
6. `support_urls`：同一组内的 URL 必须共同支撑组内所有事件；同一个 URL 全局只能出现在一个事件组，不能重复使用；多源要求按来源域名计算，同一来源域名下多个链接只能算 1 个来源。
7. `support_urls` 中每一个 URL 都必须可达，并能解析出最近 {EVENT_FRESHNESS_HOURS} 小时内的明确页面发布时间；解析不到或发布时间过旧会报错。
8. `support_urls` 不允许来自低质量域名黑名单；例如 toutiao.com 质量和可追溯性不足，不可采用。
9. `support_urls` 不允许写站点首页、频道首页或索引页；例如 `http://www.gmw.cn/` 只是主页，不是具体事件来源，不可采用。
10. `events[].relevance_level`：事件级审计字段，只能填 `强相关` / `弱相关` / `不相关`；只有 `强相关` 允许通过。如果你判断是弱相关或不相关，不要提交该事件，应该更换事件。
11. `relevance_with_topic`：事件组级字符串，说明这组事件为什么严格符合「{topic}」的定义、边界和用户偏好；不要只写“相关”。
12. `source_type`：必须填写 `cross_valid` / `official` / `coze`。
13. `source_type=cross_valid`：普通媒体、专业账号、自媒体、转载、社评或来源链不清楚时都使用 `cross_valid`。
14. `source_type=official`：表示支撑 URL 中包含官方媒体、官网或官方账号发布页，并直接发布/确认事件事实；普通媒体报道“官方称/官方宣布”不等于官方来源。
15. `source_type=coze`：表示支撑 URL 中包含 coze.cn 发布内容；仍需满足本话题至少 {support_url_min} 个 support_urls 的要求。
16. `support_urls` 数量由本话题来源要求决定：当前至少需要 {support_url_min} 个不同来源域名的可达 URL。

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
        current_timeline_path, _, current_has_events, _ = _refresh_tracked_event_timelines(tdir)
        timeline_read_line = f"\n- 当前话题已追踪事件时间线：{current_timeline_path}\n" if current_has_events else ""
        timeline_requirement = (
            f"B2 已经读取过当前话题时间线；写作前必须再次读取 `{current_timeline_path}` 做最终复核，确认 event_list 中没有已覆盖事件；"
            "如果此时发现重复，立即从当前 event_list 删除重复事件或事件组，并只基于剩余事件写日报；如果删空，把 event_list 写成空数组 []，不要写日报正文，然后直接运行 next 按暂无最新动态结束。"
            if current_has_events
            else "B2 已经做过历史去重；写作前如发现当前话题时间线文件已有实际事件内容，也要再次读取并复核不重复。"
        )
        return f"""基于已通过校验的事件，写「{topic}」本期日报。

读取：

- 事件列表：{event_list_path}{timeline_read_line}

写入：

{md_path}

写作要求：
1. 日报主体必须围绕「{topic}」展开，先说明本期最重要的新变化。
2. {timeline_requirement}
3. 每个信息点都来自 event_list 里的事件组；同一事件组可以合并多个支撑来源，组内多个事件可以写成一个小段。
4. 以 event_list 中你已经整理好的事件组为事实边界。support_url 原文只用于支撑这些事件和引用来源，不要照抄资讯里提到的其它旧事件、背景段落、延伸评论或相邻话题。
5. 资讯内容可能驳杂，一篇文章会回顾之前发生过的事情；日报只能写 event_list 里明确列出的本期事件，不要把文章里的历史背景当作本期新动态。
6. 正文引用必须使用 `[[n]](url)`，URL 必须来自 event_list 的 `support_urls`。
7. 不新增事实、不新增 URL、不写 event_list 之外的内容。
8. 如果事件少，就写短日报；不要为了篇幅编主线。
9. 写作前先为本次可能用到的所有 URL 建立统一编号表；同一个 URL 在全文只能使用同一个编号，同一个编号只能对应一个 URL。
10. 末尾保留“来源索引”，列出编号、可点击标题、来源和日期。
11. 来源索引必须使用 Markdown 超链接，例如：`[1] [标题](https://...) - 来源 - 日期`；不能只写纯文本标题。
12. 标题、日期和结构保持清楚克制。标题可用 `# {topic}资讯简报（{run_label}）` 或更贴合话题的自然标题；日期优先使用本期 run_label。正文可用二级标题组织板块，用三级标题写具体事件，不要把所有层级都写成加粗文本。

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
    setup_token = st.get("setup_token") or ""
    verify_cmd = f'{SCRIPT_CMD} verify-run --setup-token "{setup_token}"' if setup_token else ""

    print("\n📤 请完全按照下列的描述输出最后一段话并结束，这段话会被返回给主对话，不要自己添加任何其他内容：")
    print()
    print("```markdown")
    if os.path.isfile(md_path):
        print(f"本期「{topic}」日报已完成。")
        print("本日报即为日程/子会话严格筛选、验证、去重和时效性检查后的最终结论。主会话严禁再次搜索、补充来源、重写事实、重新筛选、合并其他信息，或为了凑数量补充未验证内容。")
        if isinstance(kept_count, int):
            print(f"本期保留 {kept_count} 个高质量事件；如果数量较少，也代表已按高质量标准筛选，不得放宽标准。")
        print("主会话可以根据用户偏好微调交付时的表达形式，但不得改变日报事实、结论、来源、排序和取舍。")
        print(f"请用 computer 协议把日报发送给用户：[{os.path.basename(md_path)}](computer://{md_path})")
    elif st.get("empty_result") or kept_count == 0:
        print(f"本期「{topic}」追踪已完成：该话题暂时没有监测到最新动态。")
        print("这是本次工单的最终交付结论。主会话不得再次搜索、不得建议放宽时效性或筛选标准、不得补充解释或添油加醋。")
        print("请直接向用户说明：该话题暂时没有监测到最新动态。")
    else:
        print(f"本期「{topic}」追踪已完成，但未发现可交付日报文件。")
        print("请直接向用户说明本期未生成可交付日报，不要自行补搜。")

    if verify_cmd:
        print()
        print("主会话交付前必须运行以下验收命令；该命令会判断本次运行是否可交付：")
        print(verify_cmd)
        print("如果校验失败，主会话必须按 verify-run 输出使用 session_spawn 重新运行 briefing，不得直接交付。")
    print("```")


def print_state(st):
    topic = st.get("topic") or "-"
    token = st.get("token")
    flow = st.get("flow")
    step = st.get("current_step")
    run_label = st.get("run_label")
    completed = len(st.get("completed_steps", []))
    total = len(SETUP_STEPS if flow == "setup" else BRIEFING_STEPS)

    print("\n=== 话题追踪 ===")
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
            "quick": bool(getattr(args, "quick", False)),
            "completed_steps": [],
            "created_at": datetime.now().isoformat(),
        }
        os.makedirs(st["session_dir"], exist_ok=True)
        save_state(st)
        print_state(st)
        return 0

    if flow == "briefing":
        if getattr(args, "quick", False):
            print("错误：--quick 只用于 setup 流程；briefing 不需要确认阶段")
            return 1
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
        _write_run_status(st, status="RUNNING", result="started", message="briefing 已初始化，等待执行 B1。")
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
        data, error = _read_json_checked(
            contract_input,
            label="setup_contract.json",
            expected_type=dict,
            expected_desc="对象",
        )
        if error:
            print(f"❌ {error}，停留在 S1。")
            print(_json_fix_action(contract_input))
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
        data, error = _read_json_checked(
            b1_path,
            label="B1_context.json",
            expected_type=dict,
            expected_desc="对象",
        )
        if error:
            print(f"❌ {error}，停留在 B1。")
            print(_json_fix_action(b1_path))
            return 1
        if set(data.keys()) != {"context_summary"}:
            print("❌ B1_context.json 只允许包含 context_summary 一个字段，停留在 B1。")
            return 1
        if not isinstance(data.get("context_summary"), str) or len(data.get("context_summary", "").strip()) < 20:
            print("❌ B1_context.json 的 context_summary 至少需要 20 个字符，停留在 B1。")
            return 1
        print("✅ B1 上下文已恢复。")

    if st.get("flow") == "briefing" and cur == "B2":
        run_label = st.get("run_label") or date.today().isoformat()
        tdir = st["tracking_dir"]
        event_list_path = os.path.join(tdir, f"{run_label}_event_list.json")
        confirmation_path = _low_volume_confirmation_path(tdir, run_label)
        url_blacklist_path = _event_url_blacklist_path(tdir, run_label)
        event_time_index_path = _event_time_index_path()
        validation_context = _event_time_validation_context(st, event_list_path)
        authority_requirement = _contract_authority_requirement(tdir)
        events, error = _read_json_checked(
            event_list_path,
            label="event_list",
            expected_type=list,
            expected_desc="数组",
        )
        if error:
            _write_run_status(
                st,
                status="BLOCKED",
                result="missing_event_list",
                message=error,
                errors=[error],
            )
            print(f"❌ {error}，停留在 B2。")
            print(_json_fix_action(event_list_path))
            return 1

        cache_dir = os.path.join(_session_dir(st), "url_cache")
        confirmation = _read_json_if_exists(confirmation_path)
        indexed = 0
        with _locked_event_time_index(event_time_index_path):
            event_time_index = _read_event_time_index_unlocked(event_time_index_path)
            result = _validate_event_list(
                events,
                cache_dir=cache_dir,
                low_volume_confirmation=confirmation,
                url_blacklist_path=url_blacklist_path,
                authority_requirement=authority_requirement,
                event_time_index=event_time_index,
                current_context=validation_context,
            )
            if result.get("pass") and len(events) > 0:
                indexed = _update_event_time_index_unlocked(event_time_index_path, events, context=validation_context)
        if not result.get("pass"):
            added = _append_url_blacklist(url_blacklist_path, result.get("new_blacklist_entries", []))
            _write_run_status(
                st,
                status="BLOCKED",
                result="validation_failed",
                message="event_list 校验未通过，停留在 B2。",
                errors=result.get("errors", []),
            )
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
            _write_run_status(st, status="DONE", result="empty", message="该话题暂时没有监测到最新动态。")
            save_state(st)
            print_state(st)
            return 0
        print(f"🧭 已更新全局 event_time 索引：{event_time_index_path}（新增 {indexed} 条）")

    if st.get("flow") == "briefing" and cur == "B3":
        run_label = st.get("run_label") or date.today().isoformat()
        tdir = st["tracking_dir"]
        topic = st.get("topic") or ""
        event_list_path = os.path.join(tdir, f"{run_label}_event_list.json")
        md_path = _briefing_md_path(tdir, topic, run_label)
        cache_dir = os.path.join(_session_dir(st), "url_cache")
        confirmation_path = _low_volume_confirmation_path(tdir, run_label)
        url_blacklist_path = _event_url_blacklist_path(tdir, run_label)
        event_time_index_path = _event_time_index_path()
        validation_context = _event_time_validation_context(st, event_list_path)
        authority_requirement = _contract_authority_requirement(tdir)
        raw_events = _read_json_if_exists(event_list_path)
        if isinstance(raw_events, list) and len(raw_events) == 0:
            print("ℹ️ event_list 已清空：该话题暂时没有监测到未重复的新动态，流程直接结束。")
            st.setdefault("completed_steps", []).append("B3")
            st["current_step"] = "DONE"
            st["empty_result"] = True
            st["event_list_path"] = event_list_path
            st["skipped_steps"] = ["B4"]
            st["updated_at"] = datetime.now().isoformat()
            _write_run_status(st, status="DONE", result="empty", message="该话题暂时没有监测到未重复的新动态。")
            save_state(st)
            print_state(st)
            return 0
        event_result, events = _validate_event_list_file(
            event_list_path,
            cache_dir,
            confirmation_path,
            url_blacklist_path,
            authority_requirement,
            event_time_index_path,
            validation_context,
        )
        if not event_result.get("pass"):
            added = _append_url_blacklist(url_blacklist_path, event_result.get("new_blacklist_entries", []))
            _write_run_status(
                st,
                status="BLOCKED",
                result="validation_failed",
                message="event_list 重新校验未通过，停留在 B3。",
                errors=event_result.get("errors", []),
            )
            print("❌ event_list 重新校验未通过，停留在 B3。")
            print(json.dumps(event_result, ensure_ascii=False, indent=2))
            if added:
                print(f"\n⚠️ 已将 {added} 个因时效性或相关性失败的 URL 写入黑名单：{url_blacklist_path}")
            print("请删除不符合时效/来源要求的事件，并寻找其他符合时效的新事件；不要通过改写事件时间来通过校验。")
            print(f"\n请修正后重新运行：{SCRIPT_CMD} next {args.token}")
            return 1
        _update_event_time_index(event_time_index_path, events, context=validation_context)

        url_result = _check_briefing_urls_against_events(md_path, event_list_path)
        if not url_result.get("pass"):
            _write_run_status(
                st,
                status="BLOCKED",
                result="validation_failed",
                message="日报 URL 校验未通过，停留在 B3。",
                errors=url_result.get("errors", []),
            )
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
        event_time_index_path = _event_time_index_path()
        validation_context = _event_time_validation_context(st, event_list_path)
        authority_requirement = _contract_authority_requirement(tdir)
        event_result, events = _validate_event_list_file(
            event_list_path,
            cache_dir,
            confirmation_path,
            url_blacklist_path,
            authority_requirement,
            event_time_index_path,
            validation_context,
        )
        summary, summary_error = _read_json_checked(
            summary_path,
            label="summary.json",
            expected_type=dict,
            expected_desc="对象",
        )

        if not event_result.get("pass"):
            added = _append_url_blacklist(url_blacklist_path, event_result.get("new_blacklist_entries", []))
            _write_run_status(
                st,
                status="BLOCKED",
                result="validation_failed",
                message="event_list 重新校验未通过，停留在 B4。",
                errors=event_result.get("errors", []),
            )
            print("❌ event_list 重新校验未通过，停留在 B4。")
            print(json.dumps(event_result, ensure_ascii=False, indent=2))
            if added:
                print(f"\n⚠️ 已将 {added} 个因时效性或相关性失败的 URL 写入黑名单：{url_blacklist_path}")
            print("请删除不符合时效/来源要求的事件，并寻找其他符合时效的新事件；不要通过改写事件时间来通过校验。")
            print(f"\n请修正后重新运行：{SCRIPT_CMD} next {args.token}")
            return 1
        _update_event_time_index(event_time_index_path, events, context=validation_context)
        if events is not None and len(events) == 0:
            _write_run_status(st, status="BLOCKED", result="invalid_state", message="event_list 为空时不应进入 B4。")
            print("❌ event_list 为空时不应进入 B4；请重新查看状态。")
            return 1
        if summary_error:
            _write_run_status(st, status="BLOCKED", result="missing_summary", message=summary_error, errors=[summary_error])
            print(f"❌ {summary_error}，停留在 B4。")
            print(_json_fix_action(summary_path))
            return 1
        if not os.path.isfile(md_path):
            _write_run_status(st, status="BLOCKED", result="missing_briefing_md", message="日报文件不存在。")
            print("❌ 日报文件不存在，停留在 B4。")
            print(f"请写入：{md_path}")
            return 1
        print("✅ 收尾摘要已确认。")

    st = _advance_step(st)
    if st.get("flow") == "briefing":
        status = "DONE" if st.get("current_step") == "DONE" else "RUNNING"
        result = "briefing" if status == "DONE" else "running"
        message = "本次话题追踪已完成。" if status == "DONE" else f"已推进到 {st.get('current_step')}。"
        _write_run_status(st, status=status, result=result, message=message)
    save_state(st)
    print_state(st)
    return 0


def cmd_status(args):
    st = load_state(args.token)
    print_state(st)
    return 0


def cmd_verify_run(args):
    st, error = _select_briefing_for_verify(args)
    if error:
        print("❌ 验收失败：本次话题追踪运行不合法，不可交付。")
        print(f"- {error}")
        if getattr(args, "setup_token", None):
            print()
            _print_rerun_briefing_action(args.setup_token)
        return 1

    result = _verify_briefing_state(st)
    require_recent = bool(
        getattr(args, "setup_token", None)
        and not getattr(args, "token", None)
        and not getattr(args, "run_status", None)
        and not getattr(args, "run_label", None)
        and not getattr(args, "after", None)
    )
    completed_at = _state_time(st, "updated_at") or _state_time(st, "created_at")
    if require_recent:
        if not completed_at:
            result.setdefault("errors", []).append("无法确认最后一次运行完成时间")
        else:
            now = _now_like(completed_at)
            age = now - completed_at
            if age < -timedelta(minutes=1):
                result.setdefault("errors", []).append(
                    f"最后一次运行完成时间晚于当前时间：{completed_at.isoformat(timespec='seconds')}，当前时间：{now.isoformat(timespec='seconds')}"
                )
            elif age > timedelta(minutes=VERIFY_RUN_MAX_AGE_MINUTES):
                result.setdefault("errors", []).append(
                    f"最后一次运行完成时间距离当前超过 {VERIFY_RUN_MAX_AGE_MINUTES} 分钟：{completed_at.isoformat(timespec='seconds')}，当前时间：{now.isoformat(timespec='seconds')}"
                )
        result["pass"] = not result.get("errors")
    status = "DONE" if result.get("pass") else "BLOCKED"
    _write_run_status(
        st,
        status=status,
        result=result.get("result") if result.get("pass") else "verify_failed",
        message="verify-run 校验通过。" if result.get("pass") else "verify-run 校验失败。",
        errors=result.get("errors", []),
    )

    if not result.get("pass"):
        print("❌ 验收失败：本次话题追踪运行不合法，不可交付。")
        if completed_at:
            print(f"最后运行完成时间: {completed_at.isoformat(timespec='seconds')}")
        print("原因:")
        for err in result.get("errors", []):
            print(f"- {err}")
        print()
        _print_rerun_briefing_action(result.get("setup_token") or getattr(args, "setup_token", None), result.get("topic"))
        return 1

    if result.get("result") == "empty":
        print("✅ 验收通过：本次话题追踪运行合法，且确认为空结果。")
    else:
        print("✅ 验收通过：本次话题追踪运行合法，可交付。")
    print(f"话题: {result.get('topic')}")
    if completed_at:
        print(f"最后运行完成时间: {completed_at.isoformat(timespec='seconds')}")
    if result.get("result") == "empty":
        print("结果: 暂无最新动态")
        print()
        print("主会话动作：")
        print("请直接向用户回复：该话题暂时没有监测到最新动态。")
        print("不要补搜，不要解释技术原因，不要展示候选事件，不要建议放宽时效性或筛选标准。")
    else:
        print(f"结果: 已生成日报，事件数 {result.get('event_count')}")
        print(f"日报文件: {result.get('briefing_md_path')}")
        print()
        print("主会话动作：")
        md_path = result.get("briefing_md_path") or ""
        if md_path:
            print(f"请直接发送日报文件给用户：[{os.path.basename(md_path)}](computer://{md_path})")
        else:
            print("请直接发送日报文件给用户。")
        print("不得再次搜索、补充来源、改写事实、合并其他信息。")
    print()
    print("验收优先级：")
    print("主会话只以本 verify-run 结果和已生成产物为准；如果子会话自然语言里出现“实际监测到的内容”“URL 校验没过但内容靠谱”“供参考候选”等冲突信息，一律忽略。")
    print(f"状态文件: {result.get('run_status_path')}")
    return 0


def cmd_list(args):
    items = _state_items()
    setups = [st for st, _ in items if st.get("flow") == "setup"]
    unfinished = [st for st, _ in items if st.get("current_step") != "DONE" and st.get("token")]

    if not setups:
        print("暂无话题追踪。")
    else:
        setups.sort(key=lambda item: item.get("created_at") or "")
        print("当前话题追踪：")
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
        errors.append(f"setup/session 目录不在当前 sessions 目录下，拒绝删除：{session_dir}")
    if delete_session and _is_protected_delete_path(session_dir):
        errors.append(f"setup/session 路径受保护，拒绝删除：{session_dir}")
    if delete_tracking and _is_protected_delete_path(tracking_dir):
        errors.append(f"tracking_dir 路径受保护，拒绝删除：{tracking_dir}")
    if delete_tracking and not args.force and not _tracking_dir_has_topic_marker(tracking_dir, setup_token, topic):
        errors.append("tracking_dir 缺少当前追踪标记，拒绝删除。确认无误后可追加 --force。")

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
    parser = argparse.ArgumentParser(description="topic_tracking guide")
    sub = parser.add_subparsers(dest="command")

    p = sub.add_parser("init", help="创建 setup 或 briefing 流程")
    p.add_argument("--flow", choices=["setup", "briefing"], required=True)
    p.add_argument("--topic")
    p.add_argument("--setup-token")
    p.add_argument("--tracking-dir")
    p.add_argument("--quick", action="store_true", help="setup 快速模式：S2 跳过用户确认，直接要求首次 briefing 试运行")

    p = sub.add_parser("next", help="推进当前 token 到下一步")
    p.add_argument("token")

    p = sub.add_parser("status", help="查看 token 状态")
    p.add_argument("token")

    p = sub.add_parser("verify-run", help="校验本次 briefing 运行是否合法可交付")
    p.add_argument("token", nargs="?", help="内部排障用 token；主会话通常不用")
    p.add_argument("--run-status", help="内部排障用：指定本次运行状态文件")
    p.add_argument("--setup-token", help="主会话使用：用 setup_xxx 校验今天最新 briefing")
    p.add_argument("--run-label", help="可选：限定 run_label")
    p.add_argument("--after", help="可选：限定本时间之后创建的 briefing，用于确认是本次运行")

    sub.add_parser("list", help="列出话题追踪")

    p = sub.add_parser("delete", aliases=["rm"], help="删除已追踪话题（默认只预览，加 --yes 才删除）")
    target = p.add_mutually_exclusive_group(required=True)
    target.add_argument("--topic", help="按话题名精确匹配删除")
    target.add_argument("--setup-token", help="按 setup_xxx token 删除")
    p.add_argument("--yes", action="store_true", help="确认执行删除；不加时只输出预览")
    p.add_argument("--keep-files", action="store_true", help="只删除状态和 session 记录，保留话题产物目录")
    p.add_argument("--force", action="store_true", help="tracking_dir 缺少当前追踪标记时仍允许删除（仍会保护关键目录）")
    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()
    if args.command:
        _stamp_tools_rule()
    if args.command == "init":
        return cmd_init(args)
    if args.command == "next":
        return cmd_next(args)
    if args.command == "status":
        return cmd_status(args)
    if args.command == "verify-run":
        return cmd_verify_run(args)
    if args.command == "list":
        return cmd_list(args)
    if args.command in ("delete", "rm"):
        return cmd_delete(args)
    parser.print_help()
    return 1


if __name__ == "__main__":
    sys.exit(main())
