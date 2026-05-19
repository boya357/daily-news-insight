#!/usr/bin/env python3
"""
话题追踪 validation.json 校验脚本。

校验目标：把 briefing 的候选文章约束成可审计的工单数据，避免相关性、时效性、
来源权威性、去重说明等关键字段被 agent 漏填或随意填。
"""

import json
import hashlib
import os
import re
import sys
import urllib.request
import unicodedata
from datetime import datetime, timedelta
from guide import FRESHNESS_DAYS

REQUIRED_DIMENSIONS = [
    "relevance",
    "freshness",
    "source_analysis",
    "quality",
    "ctr_pred",
    "dedup",
    "authority",
]

DECISION_DIMENSIONS = ["quality", "ctr_pred", "dedup"]
DECISION_VALUES = ["keep", "filter"]

RELEVANCE_LEVELS = ["不相关", "弱相关", "强相关"]
RELEVANCE_PASS = ["强相关"]

AUTHORITY_LEVELS = ["自媒体", "专业账号", "官方账号", "其他"]
AUTHORITY_PASS = ["专业账号", "官方账号"]

VERIFICATION_CONCLUSIONS = ["pass", "reject"]

FRESHNESS_MAX_HOURS = FRESHNESS_DAYS * 24
MIN_REASON_LENGTH = 5
REQUIRED_ARTICLE_FIELDS = ["title", "link", "summary", "validation"]

URL_PATTERN = re.compile(r"^https?://\S+")
PLACEHOLDER_HOSTS = ["example.com", "example.org", "example.net", "xxx", "placeholder"]

# coze.cn 资讯文章默认视为时效性合格，跳过 freshness 过滤
FRESHNESS_WHITELIST_HOSTS = ["coze.cn"]

# 低质量域名黑名单，命中直接过滤
BLOCKED_HOSTS = [
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
    # 短视频/社交
    "douyin.com", "kuaishou.com", "weibo.com", "xiaohongshu.com",
    # 电商/营销
    "jd.com", "taobao.com", "tmall.com", "pinduoduo.com",
    # 其他低质
    "myzaker.com", "xueqiu.com",
]

URL_CHECK_TIMEOUT = 10
MIN_PAGE_TEXT_LENGTH = 500  # 去标签后纯文本低于此值视为无有效内容（JS壳/软404等）
URL_CHECK_USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
)
_PAGE_TEXT_CACHE = {}
URL_CACHE_TTL_HOURS = 24


def _parse_time(value):
    return datetime.strptime(value.strip(), "%Y-%m-%d %H:%M")


_SOFT_404_KEYWORDS = ["404", "not found", "页面找不到", "页面不存在", "页面已删除", "内容已下线"]


def _extract_html_time_metadata(html):
    """保留 meta/JSON-LD 中的发布时间，避免去标签时丢失。"""
    if not html:
        return ""

    snippets = []
    patterns = [
        r'<meta[^>]+(?:property|name)=["\'](?:article:published_time|datePublished|publishDate|pubdate|publishTime)["\'][^>]+content=["\']([^"\']+)["\']',
        r'<meta[^>]+content=["\']([^"\']+)["\'][^>]+(?:property|name)=["\'](?:article:published_time|datePublished|publishDate|pubdate|publishTime)["\']',
        r'"(?:datePublished|publishDate|pubdate|publishTime)"\s*:\s*"([^"]+)"',
    ]
    for pattern in patterns:
        for match in re.finditer(pattern, html, flags=re.IGNORECASE):
            value = match.group(1).strip()
            if value and value not in snippets:
                snippets.append(value)
    return " ".join(snippets)


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
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        fetched_at = datetime.fromisoformat(data.get("fetched_at", ""))
        if datetime.now() - fetched_at > timedelta(hours=URL_CACHE_TTL_HOURS):
            return None
        if data.get("url") != url:
            return None
        return bool(data.get("reachable")), data.get("page_text")
    except (json.JSONDecodeError, UnicodeDecodeError, OSError, ValueError, TypeError):
        return None


def _write_url_cache(cache_dir, url, result):
    path = _url_cache_path(cache_dir, url)
    if not path:
        return
    reachable, page_text = result
    try:
        os.makedirs(cache_dir, exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            json.dump({
                "url": url,
                "reachable": bool(reachable),
                "page_text": page_text,
                "text_length": len(page_text or ""),
                "fetched_at": datetime.now().isoformat(),
            }, f, ensure_ascii=False, indent=2)
    except OSError:
        pass


def _fetch_page_text(url, cache_dir=None):
    """尝试用 urllib 获取页面文本内容。

    返回 (reachable, page_text):
      - reachable: bool, HTTP 请求是否成功且非软404
      - page_text: str|None, 去标签后的纯文本；若内容太短（JS壳等）则为 None
    """
    cache_key = (cache_dir or "", url)
    if cache_key in _PAGE_TEXT_CACHE:
        return _PAGE_TEXT_CACHE[cache_key]
    cached = _read_url_cache(cache_dir, url)
    if cached is not None:
        _PAGE_TEXT_CACHE[cache_key] = cached
        return cached
    try:
        req = urllib.request.Request(url, headers={"User-Agent": URL_CHECK_USER_AGENT})
        resp = urllib.request.urlopen(req, timeout=URL_CHECK_TIMEOUT)
        raw = resp.read()
        text = raw.decode("utf-8", errors="replace")
        metadata_text = _extract_html_time_metadata(text)
        # 先去掉 script/style 块（含内容），避免 JS壳/CSS 撑大字符数
        text = re.sub(r"<script[^>]*>[\s\S]*?</script>", " ", text, flags=re.IGNORECASE)
        text = re.sub(r"<style[^>]*>[\s\S]*?</style>", " ", text, flags=re.IGNORECASE)
        # 再去 HTML 标签，保留纯文本
        clean = re.sub(r"<[^>]+>", " ", text)
        clean = re.sub(r"\s+", " ", clean).strip()
        if metadata_text:
            clean = f"{metadata_text} {clean}".strip()
        if len(clean) < MIN_PAGE_TEXT_LENGTH:
            # 内容太短：检查是否软404
            lower = clean.lower()
            if any(kw in lower for kw in _SOFT_404_KEYWORDS):
                result = (False, None)  # 软404，视为不可达
            else:
                result = (True, None)  # 可达但内容无效（JS渲染壳等），跳过原文校验
            _PAGE_TEXT_CACHE[cache_key] = result
            _write_url_cache(cache_dir, url, result)
            return result
        result = (True, clean)
        _PAGE_TEXT_CACHE[cache_key] = result
        _write_url_cache(cache_dir, url, result)
        return result
    except Exception:
        result = (False, None)
        _PAGE_TEXT_CACHE[cache_key] = result
        _write_url_cache(cache_dir, url, result)
        return result


def _normalize_evidence_text(text):
    """用于 raw_sentence 命中的格式归一化。

    只处理符号/排版层面的等价差异，仍要求 raw_sentence 是正文里的连续片段：
    - 去掉 Markdown 强调符号
    - 统一中英文/全半角常见标点和引号
    - 去掉空白差异
    """
    if not isinstance(text, str):
        return ""
    value = unicodedata.normalize("NFKC", text)
    value = re.sub(r"[*_`~]+", "", value)
    translate_table = str.maketrans({
        "“": '"',
        "”": '"',
        "„": '"',
        "‟": '"',
        "‘": "'",
        "’": "'",
        "‚": "'",
        "‛": "'",
        "，": ",",
        "。": ".",
        "；": ";",
        "：": ":",
        "！": "!",
        "？": "?",
        "、": ",",
        "（": "(",
        "）": ")",
        "【": "[",
        "】": "]",
        "《": "<",
        "》": ">",
        "—": "-",
        "–": "-",
        "－": "-",
        "…": "...",
    })
    value = value.translate(translate_table)
    value = re.sub(r"\s+", "", value)
    return value


def _raw_sentence_in_page(raw_sentence, page_text):
    """校验 raw_sentence 是否可视为正文连续片段。

    先做严格原文匹配；失败后仅放宽符号和空白格式差异。
    不做语义相似、不允许改写。
    """
    raw = raw_sentence.strip()
    if raw in page_text:
        return True
    normalized_raw = _normalize_evidence_text(raw)
    if not normalized_raw:
        return False
    return normalized_raw in _normalize_evidence_text(page_text)


def _canonical_url_for_compare(url):
    if not isinstance(url, str):
        return ""
    value = url.strip().split("#", 1)[0]
    return value.rstrip("/")


def _external_evidence_urls(evidence_urls, article_link):
    link_key = _canonical_url_for_compare(article_link)
    if not isinstance(evidence_urls, list):
        return []
    result = []
    for url in evidence_urls:
        if isinstance(url, str) and URL_PATTERN.match(url) and _canonical_url_for_compare(url) != link_key:
            result.append(url)
    return result


def validate(filepath: str, valid_branches: list = None, cache_dir: str = None) -> dict:
    if not os.path.exists(filepath):
        return {"pass": False, "error": f"文件不存在: {filepath}"}

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        return {"pass": False, "error": f"JSON 解析失败: {e}"}

    if not isinstance(data, list):
        return {"pass": False, "error": "顶层结构必须是数组（每个元素是一篇文章）"}

    if len(data) == 0:
        return {
            "pass": True,
            "total_articles": 0,
            "message": "校验通过：validation.json 为空数组，表示本次无符合标准的新资讯",
        }

    errors = []
    warnings = []

    for i, article in enumerate(data):
        if not isinstance(article, dict):
            errors.append(f"[第{i + 1}项] 必须是对象")
            continue

        title = article.get("title", f"第{i + 1}篇（缺少title）")

        for field in REQUIRED_ARTICLE_FIELDS:
            if field not in article or not article[field]:
                errors.append(f"[{title}] 缺少必要字段: {field}")

        link = article.get("link", "")
        page_text = None  # 缓存页面文本，供 freshness raw_sentence 校验用
        if not link or not URL_PATTERN.match(link):
            errors.append(f"[{title}] link 无效或为空: '{link}'，必须是完整的 http/https URL")
        elif any(ph in link.lower() for ph in PLACEHOLDER_HOSTS):
            errors.append(f"[{title}] link 疑似占位链接: '{link}'，请替换为真实 URL")
        else:
            # URL 可达性验证 + 获取页面文本
            reachable, page_text = _fetch_page_text(link, cache_dir=cache_dir)
            # link 请求失败不在 validate 阶段报错；filter 阶段会直接移除不可达文章。
            # validate 只拦截 agent 可以修正的结构/格式/字段问题。

        validation = article.get("validation", {})
        if not isinstance(validation, dict):
            errors.append(f"[{title}] validation 字段必须是对象")
            continue

        for dim in REQUIRED_DIMENSIONS:
            if dim not in validation:
                errors.append(f"[{title}] 缺少维度: {dim}")

        for dim in DECISION_DIMENSIONS:
            val = validation.get(dim)
            if val is None:
                continue
            if not isinstance(val, dict):
                errors.append(f"[{title}] 维度 {dim} 必须是对象，包含 decision/reason")
                continue
            decision = val.get("decision")
            reason = val.get("reason")
            if decision not in DECISION_VALUES:
                errors.append(f"[{title}] {dim}.decision 必须是 {DECISION_VALUES} 之一")
            if not isinstance(reason, str) or len(reason.strip()) < MIN_REASON_LENGTH:
                errors.append(f"[{title}] {dim}.reason 需要至少{MIN_REASON_LENGTH}字符")

        relevance = validation.get("relevance")
        if relevance is not None:
            if not isinstance(relevance, dict):
                errors.append(f"[{title}] relevance 必须是对象，只包含 level/reason_with_topic")
            else:
                level = relevance.get("level", "")
                reason_with_topic = relevance.get("reason_with_topic", "")
                extra = set(relevance.keys()) - {"level", "reason_with_topic"}
                if extra:
                    errors.append(
                        f"[{title}] relevance 存在多余字段: {', '.join(sorted(extra))}。"
                        "只允许 level/reason_with_topic"
                    )
                if level not in RELEVANCE_LEVELS:
                    errors.append(f"[{title}] relevance.level 必须是 {RELEVANCE_LEVELS} 之一")
                if not isinstance(reason_with_topic, str) or len(reason_with_topic.strip()) < MIN_REASON_LENGTH:
                    errors.append(f"[{title}] relevance.reason_with_topic 需要至少{MIN_REASON_LENGTH}字符")

        freshness = validation.get("freshness")
        if freshness is not None:
            if not isinstance(freshness, dict):
                errors.append(
                    f"[{title}] freshness 必须是对象，包含 content_event_time/time_evidence_raw_sentence/time_evidence_reason"
                )
            else:
                cet = freshness.get("content_event_time", "")
                raw_sentence = freshness.get("time_evidence_raw_sentence", "")
                reason = freshness.get("time_evidence_reason", "")
                # content_event_time 校验：非空时必须符合格式，允许为空（filter 阶段会移除）
                if not isinstance(cet, str):
                    errors.append(f"[{title}] freshness.content_event_time 必须是字符串")
                elif cet.strip():
                    try:
                        _parse_time(cet)
                    except ValueError:
                        errors.append(f"[{title}] freshness.content_event_time 格式必须是 YYYY-MM-DD HH:MM")
                # time_evidence_raw_sentence 校验：允许为空（filter 阶段移除），非空时校验是否出现在原文中
                if not isinstance(raw_sentence, str):
                    errors.append(f"[{title}] freshness.time_evidence_raw_sentence 必须是字符串")
                elif raw_sentence.strip():
                    # 如果能获取到页面文本，校验 raw_sentence 是否真的出现在原文中
                    if page_text is not None:
                        if not _raw_sentence_in_page(raw_sentence, page_text):
                            errors.append(
                                f"[{title}] freshness.time_evidence_raw_sentence 未在原文中找到: "
                                f"'{raw_sentence.strip()}'。raw_sentence 必须是从正文中复制的原句，不能自行编造。"
                                "校验已自动忽略 Markdown 强调、引号/常见标点全半角和空白差异；"
                                "若仍失败，请重新复制正文中的连续片段，或在正文无事件时间时留空。"
                            )
                # time_evidence_reason 校验
                if not isinstance(reason, str) or len(reason.strip()) < MIN_REASON_LENGTH:
                    errors.append(f"[{title}] freshness.time_evidence_reason 需要至少{MIN_REASON_LENGTH}字符")

        source_analysis = validation.get("source_analysis")
        if source_analysis is not None:
            if not isinstance(source_analysis, dict):
                errors.append(
                    f"[{title}] source_analysis 必须是对象，包含 requires_verification/verification_conclusion/source_trace/evidence_urls/verification_explanation"
                )
            else:
                requires_verification = source_analysis.get("requires_verification")
                conclusion = source_analysis.get("verification_conclusion", "")
                source_trace = source_analysis.get("source_trace", "")
                evidence_urls = source_analysis.get("evidence_urls", [])
                explanation = source_analysis.get("verification_explanation", "")

                if not isinstance(requires_verification, bool):
                    errors.append(f"[{title}] source_analysis.requires_verification 必须是布尔值")
                if conclusion not in VERIFICATION_CONCLUSIONS:
                    errors.append(f"[{title}] source_analysis.verification_conclusion 必须是 {VERIFICATION_CONCLUSIONS} 之一")
                if not isinstance(source_trace, str) or len(source_trace.strip()) < MIN_REASON_LENGTH:
                    errors.append(f"[{title}] source_analysis.source_trace 需要至少{MIN_REASON_LENGTH}字符，用于说明核心事实可追溯到哪里")
                if not isinstance(evidence_urls, list):
                    errors.append(f"[{title}] source_analysis.evidence_urls 必须是 URL 字符串数组")
                else:
                    external_evidence_urls = _external_evidence_urls(evidence_urls, link)
                    for url in evidence_urls:
                        if not isinstance(url, str) or not URL_PATTERN.match(url):
                            errors.append(f"[{title}] source_analysis.evidence_urls 包含无效 URL: {url}")
                        elif _canonical_url_for_compare(url) == _canonical_url_for_compare(link):
                            errors.append(f"[{title}] source_analysis.evidence_urls 不能与文章 link 相同: {url}")
                    if requires_verification is True and conclusion == "pass":
                        if not evidence_urls:
                            errors.append(
                                f"[{title}] source_analysis.requires_verification=true 且 verification_conclusion=pass 时，"
                                "必须补充至少 1 个真实可达的 evidence_urls；如果找不到来源证据，应改为 reject"
                            )
                        elif not external_evidence_urls:
                            errors.append(
                                f"[{title}] source_analysis.requires_verification=true 且 verification_conclusion=pass 时，"
                                "必须补充至少 1 个不同于文章 link 的真实可达 evidence_url；如果找不到来源证据，应改为 reject"
                            )
                if not isinstance(explanation, str) or len(explanation.strip()) < MIN_REASON_LENGTH:
                    errors.append(f"[{title}] source_analysis.verification_explanation 需要至少{MIN_REASON_LENGTH}字符")

        authority = validation.get("authority")
        if authority is not None:
            if not isinstance(authority, dict):
                errors.append(f"[{title}] authority 必须是对象，包含 level/reason")
            else:
                level = authority.get("level", "")
                reason = authority.get("reason", "")
                if level not in AUTHORITY_LEVELS:
                    errors.append(f"[{title}] authority.level 必须是 {AUTHORITY_LEVELS} 之一")
                # 不在 validate 中拦截 level 值，由 filter 阶段处理
                if not isinstance(reason, str) or len(reason.strip()) < MIN_REASON_LENGTH:
                    errors.append(f"[{title}] authority.reason 需要至少{MIN_REASON_LENGTH}字符")

    if errors:
        result = {
            "pass": False,
            "total_articles": len(data),
            "error_count": len(errors),
            "errors": errors,
        }
        if warnings:
            result["warnings"] = warnings
        return result

    result = {
        "pass": True,
        "total_articles": len(data),
        "dimensions_checked": REQUIRED_DIMENSIONS,
        "message": f"校验通过：{len(data)} 篇文章，全部包含结构化校验字段",
    }
    if warnings:
        result["warnings"] = warnings
        result["message"] += f"（有 {len(warnings)} 条警告）"
    return result


def validate_draft_list(filepath: str, cache_dir: str = None) -> dict:
    """校验 draft_list.json 格式和候选链接可用性。

    draft_list 是候选准入门：占位链接、编造链接、不可达链接不应进入 B3。
    """
    if not os.path.exists(filepath):
        return {"pass": False, "error": f"文件不存在: {filepath}"}
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        return {"pass": False, "error": f"JSON 解析失败: {e}"}
    if not isinstance(data, list):
        return {"pass": False, "error": "顶层结构必须是数组"}
    if len(data) == 0:
        return {"pass": True, "total_articles": 0, "message": "draft_list 为空，本次无候选"}
    errors = []
    for i, item in enumerate(data):
        if not isinstance(item, dict):
            errors.append(f"[第{i + 1}项] 必须是对象")
            continue
        title = item.get("title", f"第{i + 1}项")
        for field in ["title", "link", "summary"]:
            val = item.get(field)
            if not isinstance(val, str) or not val.strip():
                errors.append(f"[{title}] 缺少或为空: {field}")
        link = item.get("link", "")
        if not link or not URL_PATTERN.match(link):
            errors.append(f"[{title}] link 格式无效或为空: '{link}'，必须是 search_web/fetch_web 返回的完整 http/https URL")
        elif any(ph in link.lower() for ph in PLACEHOLDER_HOSTS):
            errors.append(f"[{title}] link 疑似占位/编造链接: '{link}'")
        elif any(host in link for host in BLOCKED_HOSTS):
            errors.append(f"[{title}] link 命中低质域名黑名单: '{link}'")
        else:
            reachable, _ = _fetch_page_text(link, cache_dir=cache_dir)
            if not reachable:
                errors.append(f"[{title}] link 请求失败或疑似软404: '{link}'。不要手写/猜测 URL，只能复制工具返回的真实 URL")
    if errors:
        return {"pass": False, "error_count": len(errors), "errors": errors}
    return {"pass": True, "total_articles": len(data), "message": f"校验通过：{len(data)} 篇候选"}


HOLLOW_PHRASES = [
    "未提及", "未知", "不确定", "不清楚", "没有提到", "无法确定",
    "未说明", "无明确", "无具体", "时间不详", "没有时间",
]

SOURCE_TRACE_UNCLEAR_PHRASES = [
    "无法追溯", "来源不清", "来源不明", "未找到来源", "没有明确来源",
    "未说明来源",
]

SOURCE_TRACE_VAGUE_ONLY_PHRASES = ["网传", "有消息称", "外媒称", "媒体报道"]
SOURCE_TRACE_CLEAR_MARKERS = [
    "来源为", "来自", "可追溯到", "官方", "公告", "原始", "访谈",
    "会议", "播客", "财报", "法院", "权威", "央视", "新华社",
]


def _source_trace_unclear_reason(source_trace: str) -> str:
    stripped = source_trace.strip()
    for phrase in SOURCE_TRACE_UNCLEAR_PHRASES:
        if phrase in stripped:
            return phrase

    compact = re.sub(r"[\s，,。；;：:、“”\"'（）()]+", "", stripped)
    has_clear_marker = any(marker in stripped for marker in SOURCE_TRACE_CLEAR_MARKERS)
    for phrase in SOURCE_TRACE_VAGUE_ONLY_PHRASES:
        phrase_compact = re.sub(r"[\s，,。；;：:、“”\"'（）()]+", "", phrase)
        if compact == phrase_compact or (not has_clear_marker and len(stripped) <= 16 and phrase in stripped):
            return phrase
    return ""


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
    """按页面出现顺序提取带年份且精确到分钟的时间戳。"""
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


def filter_validated(validation_path: str, output_path: str, cache_dir: str = None) -> dict:
    """从 validation.json 按业务规则过滤，写入 draft_filtered.json。"""
    with open(validation_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    now = datetime.now()
    kept = []
    removed = []

    for article in data:
        v = article.get("validation", {})
        reasons = []

        # 域名黑名单
        link = article.get("link", "")
        page_text = None
        if any(host in link for host in BLOCKED_HOSTS):
            reasons.append(f"域名在黑名单中: {link}")
        elif link and URL_PATTERN.match(link):
            reachable, page_text = _fetch_page_text(link, cache_dir=cache_dir)
            if not reachable:
                reasons.append(f"link 请求失败: {link}")

        # relevance
        rel = v.get("relevance", {})
        if rel.get("level") not in RELEVANCE_PASS:
            reasons.append(f"relevance.level={rel.get('level')}")

        # source_analysis：高影响事实必须被确认，并给出证据 URL
        source_analysis = v.get("source_analysis", {})
        verification_conclusion = source_analysis.get("verification_conclusion")
        requires_verification = source_analysis.get("requires_verification")
        source_trace = source_analysis.get("source_trace", "")
        evidence_urls = source_analysis.get("evidence_urls", [])
        external_evidence_urls = _external_evidence_urls(evidence_urls, link)
        if verification_conclusion == "reject":
            reasons.append("source_analysis.verification_conclusion=reject")
        if verification_conclusion == "pass":
            if not isinstance(source_trace, str) or len(source_trace.strip()) < MIN_REASON_LENGTH:
                reasons.append("source_analysis.source_trace 为空或过短")
            else:
                unclear_reason = _source_trace_unclear_reason(source_trace)
                if unclear_reason:
                    reasons.append(f"source_analysis.source_trace 来源链不清楚({unclear_reason}): {source_trace}")
        if requires_verification is True:
            if verification_conclusion != "pass":
                reasons.append(f"source_analysis.requires_verification=true 但 verification_conclusion={verification_conclusion}")
            if not isinstance(evidence_urls, list) or not external_evidence_urls:
                reasons.append("source_analysis.requires_verification=true 且有效 evidence_urls 为空")

        # authority：官方/专业账号直接通过；自媒体必须有可追溯证据支撑
        auth = v.get("authority", {})
        auth_level = auth.get("level")
        self_media_with_evidence = (
            auth_level == "自媒体"
            and verification_conclusion == "pass"
            and bool(external_evidence_urls)
        )
        if auth_level not in AUTHORITY_PASS and not self_media_with_evidence:
            if auth_level == "自媒体":
                reasons.append("authority.level=自媒体 且有效 source_analysis.evidence_urls 为空")
            else:
                reasons.append(f"authority.level={auth_level}")

        # 解释性维度的显式决策：agent 在 B3 判定质量/关注度/去重应过滤时，门控必须执行。
        for dim in DECISION_DIMENSIONS:
            decision_block = v.get(dim, {})
            if isinstance(decision_block, dict) and decision_block.get("decision") == "filter":
                reason = decision_block.get("reason", "")
                if reason:
                    reasons.append(f"{dim}.decision=filter: {reason}")
                else:
                    reasons.append(f"{dim}.decision=filter")

        # freshness（白名单域名跳过时效性检查）
        skip_freshness = any(host in link for host in FRESHNESS_WHITELIST_HOSTS)

        if not skip_freshness:
            fresh = v.get("freshness", {})
            cet = fresh.get("content_event_time", "")
            raw = fresh.get("time_evidence_raw_sentence", "")

            page_timestamps = _extract_precise_page_timestamps(page_text)
            if page_timestamps:
                _, page_time, page_time_raw = page_timestamps[0]
                page_delta = (now - page_time).total_seconds() / 3600
                if page_delta > FRESHNESS_MAX_HOURS:
                    reasons.append(
                        f"网页首个明确分钟级时间戳 {page_time_raw} 距今 {page_delta:.1f}h，"
                        f"超过 {FRESHNESS_MAX_HOURS}h"
                    )

            if not cet or not cet.strip():
                reasons.append("content_event_time 为空")
            else:
                try:
                    parsed = _parse_time(cet)
                    delta = abs((now - parsed).total_seconds()) / 3600
                    if delta > FRESHNESS_MAX_HOURS:
                        reasons.append(f"content_event_time 距今 {delta:.1f}h，超过 {FRESHNESS_MAX_HOURS}h")
                except ValueError:
                    reasons.append(f"content_event_time 格式错误: {cet}")

            if not raw or not raw.strip():
                reasons.append("time_evidence_raw_sentence 为空")
            elif any(hp in raw for hp in HOLLOW_PHRASES):
                reasons.append(f"time_evidence_raw_sentence 含空洞短语: {raw}")

        if reasons:
            removed.append({"title": article.get("title", ""), "reasons": reasons})
        else:
            kept.append(article)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(kept, f, ensure_ascii=False, indent=2)

    return {
        "kept_count": len(kept),
        "removed_count": len(removed),
        "removed": removed,
    }


def check_briefing_urls(md_path: str, filtered_path: str) -> dict:
    """检查简报 .md 中的 URL 是否来自 draft_filtered.json 的 link/evidence_urls，且使用 [[n]](url) 编号引用。"""
    if not os.path.exists(md_path):
        return {"pass": False, "error": f"简报文件不存在: {md_path}"}
    if not os.path.exists(filtered_path):
        return {"pass": False, "error": f"draft_filtered.json 不存在: {filtered_path}"}

    with open(md_path, "r", encoding="utf-8") as f:
        md_content = f.read()
    with open(filtered_path, "r", encoding="utf-8") as f:
        filtered = json.load(f)

    source_index_match = re.search(r'(?m)^#{2,}\s*来源索引\s*$', md_content)
    body_content = md_content[:source_index_match.start()] if source_index_match else md_content
    source_index_content = md_content[source_index_match.start():] if source_index_match else ""

    allowed_urls = set()
    for article in filtered:
        if not isinstance(article, dict):
            continue
        link = article.get("link")
        if isinstance(link, str) and URL_PATTERN.match(link):
            allowed_urls.add(link)
        validation = article.get("validation", {})
        source_analysis = validation.get("source_analysis", {}) if isinstance(validation, dict) else {}
        evidence_urls = source_analysis.get("evidence_urls", []) if isinstance(source_analysis, dict) else []
        if isinstance(evidence_urls, list):
            for url in evidence_urls:
                if isinstance(url, str) and URL_PATTERN.match(url):
                    allowed_urls.add(url)

    numbered_ref_re = re.compile(r'\[\[(\d+)\]\]\((https?://[^\s\)>\]\"\'\u0060]+)\)')
    numbered_refs = numbered_ref_re.findall(body_content)
    numbered_urls = {url for _, url in numbered_refs}
    source_index_link_re = re.compile(r'(?<!\!)\[[^\]\n]+\]\((https?://[^\s\)>\]\"\'\u0060]+)\)')
    source_index_urls = set(source_index_link_re.findall(source_index_content))

    url_re = re.compile(r'https?://[^\s\)>\]\"\'\u0060]+')
    found_urls = set(url_re.findall(md_content))
    body_urls = set(url_re.findall(body_content))

    if allowed_urls and not numbered_refs:
        return {
            "pass": False,
            "error": "简报中缺少 [[n]](url) 编号引用；正文引用必须使用 [[1]](https://...) 这种格式",
        }

    unnumbered_urls = body_urls - numbered_urls
    if unnumbered_urls:
        return {
            "pass": False,
            "error": f"简报正文中有 {len(unnumbered_urls)} 个 URL 未使用 [[n]](url) 编号引用格式；来源索引中的 [标题](url) 会被允许",
            "unnumbered_urls": sorted(unnumbered_urls),
        }

    invalid = found_urls - allowed_urls
    if invalid:
        return {
            "pass": False,
            "error": f"简报中包含 {len(invalid)} 个不在 draft_filtered.json 的 link/evidence_urls 中的 URL",
            "invalid_urls": sorted(invalid),
        }
    return {
        "pass": True,
        "url_count": len(found_urls),
        "numbered_reference_count": len(numbered_refs),
        "source_index_link_count": len(source_index_urls),
        "message": f"简报中 {len(found_urls)} 个 URL 全部来自 draft_filtered.json 的 link/evidence_urls；正文引用均使用 [[n]](url)，来源索引允许 [标题](url)",
    }


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(json.dumps(
            {"pass": False, "error": "用法: python validate_tracking.py <validation.json 绝对路径>"},
            ensure_ascii=False,
        ))
        sys.exit(1)

    result = validate(sys.argv[1])
    print(json.dumps(result, ensure_ascii=False, indent=2))
    sys.exit(0 if result["pass"] else 1)
