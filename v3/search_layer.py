"""
统一搜索工具层 (L3-1)
======================================
V5.0 升级 - 2026-07-04

功能：
1. 统一HTTP请求封装（自动重试/指数退避/超时控制）
2. 搜索结果去重（URL规范化 + 标题相似度）
3. 自动来源域名标注 + 来源类型分类
4. 搜索结果置信度自动评估（官方源=高🔴/权威媒体=中🟡/自媒体=低⚪）
5. 关键数据双源验证接口
6. 搜索会话记录（可追踪/可复现）
7. 供所有CodeAct脚本和Pro生成器统一调用

设计说明：
- HTTP请求层：封装urllib/requests的重试与错误处理
- 来源评估层：根据域名/关键词自动分类来源等级
- 验证层：双源比对、置信度标注
- 结果层：统一SearchResult数据结构
"""

import os
import sys
import re
import json
import time
import hashlib
import logging
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any, Tuple, Union
from dataclasses import dataclass, field, asdict
from urllib.parse import urlparse, urljoin, quote_plus
from difflib import SequenceMatcher

# ---------------------------------------------------------------------------
# 日志
# ---------------------------------------------------------------------------
logger = logging.getLogger("search_layer")
if not logger.handlers:
    _h = logging.StreamHandler()
    _h.setFormatter(logging.Formatter("[%(levelname)s] %(name)s: %(message)s"))
    logger.addHandler(_h)
logger.setLevel(logging.INFO)


# ---------------------------------------------------------------------------
# 数据结构
# ---------------------------------------------------------------------------

@dataclass
class SearchResult:
    """单条搜索结果"""
    url: str = ""
    title: str = ""
    snippet: str = ""
    domain: str = ""           # 自动提取
    source_type: str = ""      # official/authority/financial/social/unknown
    source_label: str = ""     # 来源中文名：财联社/上交所等
    confidence: str = "medium" # high/medium/low
    confidence_icon: str = "🟡"
    publish_time: str = ""
    verified: bool = False     # 是否已双源验证
    fetched_at: str = ""
    extra: Dict[str, Any] = field(default_factory=dict)
    
    def __post_init__(self):
        if not self.domain and self.url:
            self.domain = _extract_domain(self.url)
        if not self.source_type:
            self.source_type = classify_source(self.url, self.title)
        if not self.source_label:
            self.source_label = _domain_label(self.domain)
        if not self.confidence_icon:
            self.confidence_icon = CONF_ICON.get(self.confidence, "🟡")
        if not self.fetched_at:
            self.fetched_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)
    
    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> "SearchResult":
        return cls(**{k: v for k, v in d.items() if k in cls.__dataclass_fields__})


# ---------------------------------------------------------------------------
# 置信度常量（与 pro_base.py 保持一致）
# ---------------------------------------------------------------------------
CONF_HIGH = "high"
CONF_MEDIUM = "medium"
CONF_LOW = "low"

CONF_ICON = {CONF_HIGH: "🔴", CONF_MEDIUM: "🟡", CONF_LOW: "⚪"}
CONF_LABEL = {CONF_HIGH: "高", CONF_MEDIUM: "中", CONF_LOW: "低"}


# ---------------------------------------------------------------------------
# 来源域名分类表
# ---------------------------------------------------------------------------

# 官方源（置信度=高）
OFFICIAL_DOMAINS = {
    # 监管机构
    "csrc.gov.cn": "中国证监会",
    "sse.com.cn": "上交所",
    "szse.cn": "深交所",
    "bse.cn": "北交所",
    "cffex.com.cn": "中金所",
    "shfe.com.cn": "上期所",
    "czce.com.cn": "郑商所",
    "dce.com.cn": "大商所",
    "gf.com.cn": "发改委",
    "pbc.gov.cn": "中国人民银行",
    "mof.gov.cn": "财政部",
    "stats.gov.cn": "国家统计局",
    "gov.cn": "中国政府网",
    "miit.gov.cn": "工信部",
    "mofcom.gov.cn": "商务部",
    # 公司公告/披露
    "cninfo.com.cn": "巨潮资讯",
    "static.cninfo.com.cn": "巨潮资讯",
    "hkexnews.hk": "港交所披露易",
    "sec.gov": "美国SEC",
    # 交易所官方
    "sse.com.cn": "上交所",
    "szse.cn": "深交所",
}

# 权威财经媒体（置信度=中-高）
AUTHORITY_DOMAINS = {
    "cls.cn": "财联社",
    "caixin.com": "财新网",
    "21jingji.com": "21世纪经济报道",
    "stcn.com": "证券时报",
    "cs.com.cn": "中国证券报",
    "cnstock.com": "上海证券报",
    "xinhuanet.com": "新华网",
    "people.com.cn": "人民网",
    "yicai.com": "第一财经",
    "eeo.com.cn": "经济观察网",
    "thepaper.cn": "澎湃新闻",
    "jiuyangongshe.com": "韭研公社",
    "china.com.cn": "中国网",
    "reuters.com": "路透社",
    "bloomberg.com": "彭博",
    "wsj.com": "华尔街日报",
    "ft.com": "金融时报",
    "nikkei.com": "日经",
    "thelec.net": "TheElec",
    "thelec.kr": "TheElec",
    "trendforce.com": "TrendForce集邦咨询",
    "digitimes.com": "DigiTimes",
    "icvtank.com": "投研会",
}

# 金融数据平台（置信度=中）
FINANCIAL_DATA_DOMAINS = {
    "eastmoney.com": "东方财富",
    "10jqka.com.cn": "同花顺",
    "wind.com.cn": "Wind",
    "finance.sina.com.cn": "新浪财经",
    "finance.qq.com": "腾讯财经",
    "xueqiu.com": "雪球",
    "guosen.com.cn": "国信证券",
    "htsc.com.cn": "华泰证券",
    "citics.com": "中信证券",
    "cn.investing.com": "Investing",
    "marketwatch.com": "MarketWatch",
    "cnbc.com": "CNBC",
    "yuncaijing.com": "云财经",
}

# 自媒体/社区（置信度=低）
SOCIAL_DOMAINS = {
    "weibo.com": "微博",
    "weibo.cn": "微博",
    "zhihu.com": "知乎",
    "toutiao.com": "今日头条",
    "bilibili.com": "B站",
    "douyin.com": "抖音",
    "baidu.com": "百度",
    "163.com": "网易",
    "sohu.com": "搜狐",
    "mp.weixin.qq.com": "微信公众号",
    "guba.eastmoney.com": "东方财富股吧",
    "tieba.baidu.com": "百度贴吧",
    "taoguba.com.cn": "淘股吧",
}


def _extract_domain(url: str) -> str:
    """从URL提取主域名"""
    if not url:
        return ""
    try:
        url = url.strip()
        if not url.startswith("http"):
            url = "https://" + url
        parsed = urlparse(url)
        host = parsed.netloc.lower()
        # 移除www.前缀
        if host.startswith("www."):
            host = host[4:]
        # 移除端口
        host = host.split(":")[0]
        return host
    except Exception:
        return ""


def _domain_label(domain: str) -> str:
    """根据域名返回中文来源名"""
    if not domain:
        return "未知来源"
    for table in [OFFICIAL_DOMAINS, AUTHORITY_DOMAINS, FINANCIAL_DATA_DOMAINS, SOCIAL_DOMAINS]:
        for d, name in table.items():
            if domain == d or domain.endswith("." + d):
                return name
    # 通用：取主域名前两段
    parts = domain.split(".")
    if len(parts) >= 2:
        return parts[-2].capitalize()
    return domain


def classify_source(url: str = "", title: str = "") -> str:
    """根据URL自动分类来源类型
    
    Returns:
        'official' | 'authority' | 'financial' | 'social' | 'unknown'
    """
    domain = _extract_domain(url)
    
    for d in OFFICIAL_DOMAINS:
        if domain == d or domain.endswith("." + d):
            return "official"
    
    for d in AUTHORITY_DOMAINS:
        if domain == d or domain.endswith("." + d):
            return "authority"
    
    for d in FINANCIAL_DATA_DOMAINS:
        if domain == d or domain.endswith("." + d):
            return "financial"
    
    for d in SOCIAL_DOMAINS:
        if domain == d or domain.endswith("." + d):
            return "social"
    
    # 根据标题关键词判断自媒体
    if title:
        social_keywords = ["网传", "网友", "爆料", "大V", "公众号", "朋友圈", "内幕", "据传", "听说"]
        for kw in social_keywords:
            if kw in title:
                return "social"
    
    return "unknown"


def assess_confidence(url: str = "", title: str = "", source_type: str = "") -> Tuple[str, str]:
    """自动评估搜索结果置信度
    
    Returns:
        (confidence_level, confidence_icon)
    """
    if not source_type:
        source_type = classify_source(url, title)
    
    if source_type == "official":
        return CONF_HIGH, CONF_ICON[CONF_HIGH]
    elif source_type == "authority":
        # 权威媒体默认中等，有"独家""证实"关键词升高
        if title and any(kw in title for kw in ["证实", "公告", "官方", "披露", "发布"]):
            return CONF_HIGH, CONF_ICON[CONF_HIGH]
        return CONF_MEDIUM, CONF_ICON[CONF_MEDIUM]
    elif source_type == "financial":
        # 金融数据平台默认中等
        return CONF_MEDIUM, CONF_ICON[CONF_MEDIUM]
    elif source_type == "social":
        # 社交媒体默认低
        if title and any(kw in title for kw in ["重磅", "突发", "惊人", "震惊", "疯狂", "必看"]):
            return CONF_LOW, CONF_ICON[CONF_LOW]
        return CONF_LOW, CONF_ICON[CONF_LOW]
    else:
        return CONF_MEDIUM, CONF_ICON[CONF_MEDIUM]


# ---------------------------------------------------------------------------
# 工具函数
# ---------------------------------------------------------------------------

def _normalize_url(url: str) -> str:
    """URL规范化（去锚点/排序参数/统一协议）用于去重"""
    if not url:
        return ""
    try:
        if not url.startswith("http"):
            url = "https://" + url
        parsed = urlparse(url)
        scheme = "https"
        netloc = parsed.netloc.lower()
        if netloc.startswith("www."):
            netloc = netloc[4:]
        path = parsed.path.rstrip("/") or "/"
        # 忽略常见跟踪参数
        query = parsed.query
        # 简单去重：只保留核心path
        return f"{scheme}://{netloc}{path}"
    except Exception:
        return url


def _title_similarity(a: str, b: str) -> float:
    """标题相似度（0-1）"""
    if not a or not b:
        return 0.0
    return SequenceMatcher(None, a.strip(), b.strip()).ratio()


def deduplicate_results(results: List[SearchResult], 
                        url_threshold: float = 0.95,
                        title_threshold: float = 0.85) -> List[SearchResult]:
    """搜索结果去重
    
    规则：
    1. 完全相同URL → 保留先到的
    2. URL规范化后相同 → 保留置信度更高的
    3. 标题相似度>阈值 → 保留置信度更高、内容更全的
    """
    if not results:
        return []
    
    seen_urls = {}  # normalized_url -> index
    seen_titles = []  # [(title, index)]
    keep = []
    
    for r in results:
        norm_url = _normalize_url(r.url)
        is_dup = False
        
        # URL去重
        if norm_url and norm_url in seen_urls:
            existing_idx = seen_urls[norm_url]
            existing = keep[existing_idx]
            # 保留置信度更高的
            if _conf_rank(r.confidence) > _conf_rank(existing.confidence):
                keep[existing_idx] = r
            is_dup = True
            continue
        
        # 标题相似度去重
        for seen_title, seen_idx in seen_titles:
            sim = _title_similarity(r.title, seen_title)
            if sim >= title_threshold:
                existing = keep[seen_idx]
                if _conf_rank(r.confidence) > _conf_rank(existing.confidence):
                    keep[seen_idx] = r
                is_dup = True
                break
        
        if not is_dup:
            idx = len(keep)
            keep.append(r)
            if norm_url:
                seen_urls[norm_url] = idx
            if r.title:
                seen_titles.append((r.title, idx))
    
    return keep


def _conf_rank(conf: str) -> int:
    """置信度排序值（越高越好）"""
    return {CONF_HIGH: 3, CONF_MEDIUM: 2, CONF_LOW: 1}.get(conf, 0)


# ---------------------------------------------------------------------------
# HTTP请求层（统一重试/退避/超时）
# ---------------------------------------------------------------------------

def retry_with_backoff(func, max_retries: int = 3, base_delay: float = 1.0,
                       backoff_factor: float = 2.0, exceptions: tuple = (Exception,),
                       retry_on_status: Tuple[int, ...] = (429, 500, 502, 503, 504)):
    """指数退避重试装饰器/包装器
    
    Args:
        func: 要执行的函数
        max_retries: 最大重试次数
        base_delay: 初始延迟秒数
        backoff_factor: 退避倍数
        exceptions: 需要重试的异常类型
        retry_on_status: 需要重试的HTTP状态码
    """
    def wrapper(*args, **kwargs):
        last_exc = None
        for attempt in range(max_retries + 1):
            try:
                result = func(*args, **kwargs)
                # 如果返回(response, status_code)形式，检查状态码
                if isinstance(result, tuple) and len(result) >= 2:
                    status = result[1] if isinstance(result[1], int) else None
                    if status and status in retry_on_status:
                        raise RetryableHTTPError(f"HTTP {status}", status_code=status)
                return result
            except exceptions as e:
                last_exc = e
                if attempt < max_retries:
                    delay = base_delay * (backoff_factor ** attempt)
                    logger.warning(f"[Retry] 第{attempt+1}次失败: {e}, {delay:.1f}s后重试...")
                    time.sleep(delay)
                else:
                    logger.error(f"[Retry] 已达最大重试次数{max_retries}，放弃: {e}")
        raise last_exc
    return wrapper


class RetryableHTTPError(Exception):
    """可重试的HTTP错误"""
    def __init__(self, message: str, status_code: int = 0):
        super().__init__(message)
        self.status_code = status_code


def http_get(url: str, headers: Dict[str, str] = None, timeout: int = 15,
             max_retries: int = 3, **kwargs) -> Tuple[Optional[bytes], int, str]:
    """统一HTTP GET请求（含重试）
    
    Returns:
        (content_bytes, status_code, final_url)
    """
    import urllib.request
    import urllib.error
    import ssl
    
    default_headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                      "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    }
    if headers:
        default_headers.update(headers)
    
    ssl_ctx = ssl.create_default_context()
    ssl_ctx.check_hostname = False
    ssl_ctx.verify_mode = ssl.CERT_NONE
    
    last_error = None
    for attempt in range(max_retries + 1):
        try:
            req = urllib.request.Request(url, headers=default_headers, **kwargs)
            with urllib.request.urlopen(req, timeout=timeout, context=ssl_ctx) as resp:
                content = resp.read()
                return content, resp.status, resp.geturl()
        except urllib.error.HTTPError as e:
            last_error = e
            if e.code in (429, 500, 502, 503, 504) and attempt < max_retries:
                delay = 1.0 * (2 ** attempt)
                logger.warning(f"[HTTP] GET {url} => {e.code}, 第{attempt+1}次重试, {delay:.1f}s后...")
                time.sleep(delay)
                continue
            return None, e.code, url
        except Exception as e:
            last_error = e
            if attempt < max_retries:
                delay = 1.0 * (2 ** attempt)
                logger.warning(f"[HTTP] GET {url} 异常: {e}, 第{attempt+1}次重试...")
                time.sleep(delay)
                continue
    
    logger.error(f"[HTTP] GET {url} 最终失败: {last_error}")
    return None, 0, url


def http_get_text(url: str, encoding: str = "utf-8", **kwargs) -> Tuple[Optional[str], int, str]:
    """统一HTTP GET请求（返回文本）"""
    content, status, final_url = http_get(url, **kwargs)
    if content is None:
        return None, status, final_url
    try:
        text = content.decode(encoding, errors="replace")
        return text, status, final_url
    except Exception as e:
        logger.error(f"[HTTP] 解码失败 {url}: {e}")
        return None, status, final_url


# ---------------------------------------------------------------------------
# 双源验证接口
# ---------------------------------------------------------------------------

def dual_source_verify(value_a: Any, source_a: str,
                       value_b: Any, source_b: str,
                       tolerance: float = 0.02,
                       label: str = "") -> Dict[str, Any]:
    """关键数据双源验证
    
    Args:
        value_a: 主源数值/文本
        source_a: 主源名称
        value_b: 副源数值/文本
        source_b: 副源名称
        tolerance: 数值允许的相对误差（默认2%）
        label: 数据项名称（用于日志）
    
    Returns:
        {
            'passed': bool,
            'value': 采用值,
            'conflict': bool,
            'diff_pct': float,
            'message': str,
            'source_a': str, 'source_b': str,
        }
    """
    result = {
        "passed": False,
        "value": value_a,
        "conflict": False,
        "diff_pct": 0.0,
        "message": "",
        "source_a": source_a,
        "source_b": source_b,
        "label": label,
    }
    
    # 数值比较
    try:
        a = float(value_a)
        b = float(value_b)
        diff = abs(a - b)
        base = max(abs(a), abs(b), 1e-6)
        rel = diff / base
        result["diff_pct"] = rel
        
        if rel <= tolerance:
            result["passed"] = True
            result["message"] = f"✅ 双源一致（偏差{rel:.2%}）"
        else:
            result["conflict"] = True
            result["message"] = f"⚠️ 双源分歧: {source_a}={value_a} vs {source_b}={value_b}，偏差{rel:.2%}，采用主源{source_a}"
        return result
    except (TypeError, ValueError):
        pass
    
    # 文本比较
    if isinstance(value_a, str) and isinstance(value_b, str):
        sim = _title_similarity(value_a, value_b)
        if sim >= 0.9:
            result["passed"] = True
            result["message"] = f"✅ 双源文本一致（相似度{sim:.0%}）"
        elif sim >= 0.6:
            result["passed"] = True
            result["message"] = f"🟡 双源文本基本一致（相似度{sim:.0%}），采用主源表述"
        else:
            result["conflict"] = True
            result["message"] = f"⚠️ 双源文本分歧: [{source_a}]「{value_a[:30]}」vs [{source_b}]「{value_b[:30]}」"
        return result
    
    # 类型不同
    result["conflict"] = True
    result["message"] = f"⚠️ 双源类型不一致，无法直接比较"
    return result


# ---------------------------------------------------------------------------
# 搜索会话记录
# ---------------------------------------------------------------------------

class SearchSession:
    """搜索会话记录器 - 记录本次报告生成过程中的所有搜索行为"""
    
    def __init__(self, session_name: str = "", data_dir: str = "data"):
        self.session_name = session_name or datetime.now().strftime("search_%Y%m%d_%H%M%S")
        self.data_dir = data_dir
        self.queries: List[Dict[str, Any]] = []
        self.results_cache: Dict[str, List[SearchResult]] = {}
        self.started_at = datetime.now().isoformat()
    
    def log_query(self, query: str, engine: str = "general", 
                  results: List[SearchResult] = None, metadata: Dict = None):
        """记录一次搜索"""
        entry = {
            "query": query,
            "engine": engine,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "result_count": len(results) if results else 0,
            "metadata": metadata or {},
        }
        self.queries.append(entry)
        if results:
            self.results_cache[query] = results
        logger.info(f"[SearchSession] 查询: {query} => {entry['result_count']}条结果")
    
    def get_results(self, query: str) -> List[SearchResult]:
        return self.results_cache.get(query, [])
    
    def save(self, filepath: str = None) -> str:
        """保存会话记录到JSON"""
        if not filepath:
            os.makedirs(self.data_dir, exist_ok=True)
            filepath = os.path.join(self.data_dir, f"search_session_{self.session_name}.json")
        
        record = {
            "session_name": self.session_name,
            "started_at": self.started_at,
            "ended_at": datetime.now().isoformat(),
            "queries": self.queries,
            "total_queries": len(self.queries),
            "total_results": sum(q["result_count"] for q in self.queries),
            "source_distribution": self._source_distribution(),
        }
        
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(record, f, ensure_ascii=False, indent=2)
        logger.info(f"[SearchSession] 搜索记录已保存: {filepath}")
        return filepath
    
    def _source_distribution(self) -> Dict[str, int]:
        """来源分布统计"""
        dist = {}
        for q_results in self.results_cache.values():
            for r in q_results:
                label = r.source_label or r.domain or "未知"
                dist[label] = dist.get(label, 0) + 1
        return dist
    
    def summary(self) -> str:
        """生成人类可读的搜索摘要（可附在报告末尾）"""
        if not self.queries:
            return ""
        dist = self._source_distribution()
        source_tags = " ".join([
            f'<span class="bg-white/5 text-white/70 text-xs px-2 py-1 rounded border border-white/10">{s} <span class="text-white/40">×{c}</span></span>'
            for s, c in sorted(dist.items(), key=lambda x: -x[1])
        ])
        return f'''
        <div class="mt-3 p-3 bg-white/[0.03] rounded-lg border border-white/5">
            <div class="text-xs text-white/40 mb-2">🔍 本次报告搜索记录（{len(self.queries)}次查询 / {sum(q['result_count'] for q in self.queries)}条结果）</div>
            <div class="flex flex-wrap gap-1.5">{source_tags}</div>
        </div>
        '''


# ---------------------------------------------------------------------------
# 快速构造SearchResult
# ---------------------------------------------------------------------------

def make_result(url: str = "", title: str = "", snippet: str = "",
                publish_time: str = "", **extra) -> SearchResult:
    """便捷构造SearchResult，自动评估置信度和来源"""
    confidence, icon = assess_confidence(url, title)
    return SearchResult(
        url=url,
        title=title,
        snippet=snippet,
        confidence=confidence,
        confidence_icon=icon,
        publish_time=publish_time,
        extra=extra,
    )


def results_from_search_response(raw_results: List[Dict[str, Any]]) -> List[SearchResult]:
    """从搜索API原始响应批量构造SearchResult列表（自动去重+置信度评估）
    
    原始响应格式兼容：[{"url":..., "title":..., "snippet":..., "date":...}, ...]
    """
    results = []
    for item in raw_results:
        r = make_result(
            url=item.get("url", ""),
            title=item.get("title", ""),
            snippet=item.get("snippet", item.get("content", "")),
            publish_time=item.get("date", item.get("publish_time", "")),
        )
        results.append(r)
    return deduplicate_results(results)


# ---------------------------------------------------------------------------
# SourceTag HTML组件（与pro_base.py的source_tag保持一致，方便非生成器环境直接调用）
# ---------------------------------------------------------------------------

def source_tag_html(source: str = "综合", confidence: str = CONF_MEDIUM,
                    verified: bool = False, rumor: bool = False) -> str:
    """生成数据来源标注HTML"""
    icon = CONF_ICON.get(confidence, "🟡")
    label = CONF_LABEL.get(confidence, "中")
    verify_html = ' | <span class="text-green-400">双源验证✅</span>' if verified else ''
    rumor_html = ' <span class="text-yellow-400 font-semibold">⚠️未经证实，仅供参考</span>' if rumor or confidence == CONF_LOW else ''
    return (
        f'<span class="inline-flex items-center gap-1 text-[11px] text-white/50 '
        f'bg-white/5 border border-white/10 rounded px-1.5 py-0.5 ml-1 align-middle">'
        f'来源: <span class="text-white/70">{source}</span> | '
        f'置信度: <span class="text-white/70">{label}</span>{icon}{verify_html}'
        f'</span>{rumor_html}'
    )


# ---------------------------------------------------------------------------
# 便捷导出
# ---------------------------------------------------------------------------

__all__ = [
    # 数据结构
    "SearchResult",
    # 常量
    "CONF_HIGH", "CONF_MEDIUM", "CONF_LOW", "CONF_ICON", "CONF_LABEL",
    # 分类与评估
    "classify_source", "assess_confidence", "_extract_domain",
    # 去重
    "deduplicate_results",
    # HTTP
    "http_get", "http_get_text", "retry_with_backoff", "RetryableHTTPError",
    # 双源验证
    "dual_source_verify",
    # 会话记录
    "SearchSession",
    # 便捷构造
    "make_result", "results_from_search_response",
    # HTML组件
    "source_tag_html",
]


# ---------------------------------------------------------------------------
# 自测
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    print("=" * 60)
    print("🧪 统一搜索工具层自测")
    print("=" * 60)
    
    # 测试1: 来源分类
    print("\n【1】来源分类与置信度评估")
    test_urls = [
        ("http://www.sse.com.cn/disclosure/listedinfo/announcement/", "上交所公告"),
        ("https://www.cls.cn/detail/1234567", "财联社电报"),
        ("https://xueqiu.com/123456/posts", "雪球用户帖"),
        ("https://weibo.com/123456", "微博"),
        ("https://www.cninfo.com.cn/new/disclosure/detail?stockCode=002409", "巨潮资讯-雅克科技公告"),
        ("https://www.thelec.net/news/articleView.html?idxno=123", "TheElec"),
    ]
    for url, title in test_urls:
        st = classify_source(url, title)
        conf, icon = assess_confidence(url, title, st)
        label = _domain_label(_extract_domain(url))
        print(f"  {icon} [{st:10s}] {label:12s} | {title[:30]}")
    
    # 测试2: 去重
    print("\n【2】结果去重")
    test_results = [
        make_result("https://www.cls.cn/detail/1", "半导体板块大涨5%", "半导体..."),
        make_result("https://www.cls.cn/detail/1", "半导体板块大涨5%", "重复URL"),
        make_result("https://www.cls.cn/detail/2", "半导体板块大涨5.2%", "相似标题"),
        make_result("https://www.eastmoney.com/a/123.html", "半导体板块今日强势上涨", "不同来源不同标题"),
    ]
    deduped = deduplicate_results(test_results)
    print(f"  原始{len(test_results)}条 => 去重后{len(deduped)}条")
    for r in deduped:
        print(f"  - {r.title[:40]} [{r.source_label}]")
    
    # 测试3: 双源验证
    print("\n【3】双源验证")
    v1 = dual_source_verify(7389.23, "东方财富", 7389.50, "同花顺", label="雅克科技价格")
    print(f"  数值一致验证: {v1['message']}")
    v2 = dual_source_verify(7389.23, "东方财富", 7500.00, "同花顺", label="某股价")
    print(f"  数值分歧验证: {v2['message']}")
    v3 = dual_source_verify("涨停", "财联社", "涨停", "证券时报")
    print(f"  文本一致验证: {v3['message']}")
    
    # 测试4: 搜索会话
    print("\n【4】搜索会话")
    session = SearchSession(session_name="test")
    session.log_query("雅克科技 HBM", "general", deduped)
    session.log_query("半导体设备 国产替代", "general", [])
    print(f"  总查询数: {len(session.queries)}")
    print(f"  来源分布: {session._source_distribution()}")
    
    print("\n✅ 自测完成")
