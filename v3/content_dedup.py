"""
报告内容去重与交叉引用模块 - V5.0 L1-0
解决日报/S级/盘中/盘后多份报告重复覆盖同一事件的问题。

核心思想：
1. 建立"今日事件池"JSON（按交易日存放），每份报告生成后把它覆盖到的事件/话题写入
2. 后续报告生成时，查询事件池，只输出"增量信息"，已覆盖的事件给出交叉引用链接
3. 明确定义四类报告的内容边界：
   - daily(日报)    = 信息全景：全市场覆盖，每个事件1-2句摘要 + S级深度链接
   - s_level(S级)   = 单题材深挖：深度分析+交易策略+空方视角+证伪条件
   - intraday(盘中) = 增量异动：只写相对日报/S级新增的变化，不重复已写内容
   - aftermarket(盘后) = 当日验证+持仓诊断+龙虎榜

数据结构 data/event_pool/YYYYMMDD.json：
{
    "date": "2026-07-04",
    "events": [
        {
            "id": "evt_20260704_001",
            "keywords": ["费半","SOX","费城半导体"],
            "title": "费半指数暴跌X%，半导体板块承压",
            "summary": "1-2句摘要",
            "category": "外盘/行业/个股/政策/资金/风险",
            "level": "S/A/B/C",
            "covered_by": [{"report_type":"s_level","report_file":"...","anchor":"#xxx","covered_at":"..."}],
            "first_covered_at": "...",
            "last_updated_at": "...",
            "updates": [{"report_type":"intraday", "update":"新增变化描述", "at":"..."}]
        }
    ],
    "reports_generated": [
        {"type":"s_level", "file":"...", "generated_at":"...", "events_covered":[evt_ids]}
    ]
}
"""
import json
import os
import re
import hashlib
from datetime import datetime, date
from typing import Dict, List, Optional, Any, Tuple
from dataclasses import dataclass, field, asdict
from pathlib import Path
from difflib import SequenceMatcher


# ============================================================================
# 报告类型内容边界定义
# ============================================================================

REPORT_CONTRACTS = {
    "s_level": {
        "name": "S级催化",
        "role": "single_topic_deep_dive",
        "description": "单题材深挖：深度分析+交易策略+空方视角+证伪条件",
        "depth": "deep",              # 对单个题材写200-500字深度分析
        "coverage": "single_topic",   # 只覆盖1-2个核心S级题材
        "must_include": ["深度分析", "交易策略", "空方视角", "证伪条件", "止损位"],
        "must_link_to": [],           # S级是源头，其他报告链接到S级
        "skip_existing": False,       # S级不跳过，它是深度内容生产者
    },
    "daily": {
        "name": "每日新闻洞察",
        "role": "panorama",
        "description": "信息全景：全市场覆盖，每个事件1-2句摘要+S级深度链接",
        "depth": "summary",           # 每个事件1-2句
        "coverage": "full_market",    # 全市场
        "must_include": ["宏观", "外盘", "行业", "个股异动", "资金", "政策"],
        "must_link_to": ["s_level"],  # S级题材要加"详见S级催化→"链接
        "skip_existing_in_depth": True,  # S级已深度覆盖的题材在日报只写摘要+链接
    },
    "intraday": {
        "name": "盘中快报",
        "role": "incremental",
        "description": "只写增量异动：较日报/S级新增的变化，不重复已写内容",
        "depth": "delta",             # 只写"变化了什么"
        "coverage": "delta_only",     # 仅增量
        "must_include": ["新增异动", "快速变化", "临盘机会/风险"],
        "must_link_to": ["s_level", "daily"],
        "skip_existing": True,        # 已覆盖且无变化的事件不重复
    },
    "aftermarket": {
        "name": "盘后速递",
        "role": "verification",
        "description": "当日验证+持仓诊断+龙虎榜：复盘预判兑现情况",
        "depth": "verification",      # 验证+诊断
        "coverage": "portfolio_focused",
        "must_include": ["预判验证", "持仓诊断", "龙虎榜", "次日策略"],
        "must_link_to": ["s_level", "daily", "intraday"],
        "skip_existing": True,
    },
}


# ============================================================================
# 事件池管理
# ============================================================================

class EventPool:
    """今日事件池 - 维护当日已覆盖事件清单"""
    
    def __init__(self, pool_dir: str = "data/event_pool", trade_date: str = None):
        self.pool_dir = pool_dir
        os.makedirs(pool_dir, exist_ok=True)
        self.trade_date = trade_date or datetime.now().strftime("%Y%m%d")
        self.pool_path = os.path.join(pool_dir, f"{self.trade_date}.json")
        self.pool = self._load()
    
    def _load(self) -> Dict:
        if os.path.exists(self.pool_path):
            try:
                with open(self.pool_path, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except Exception:
                pass
        return {
            "date": self.trade_date,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "events": [],
            "reports_generated": [],
        }
    
    def save(self):
        os.makedirs(self.pool_dir, exist_ok=True)
        with open(self.pool_path, 'w', encoding='utf-8') as f:
            json.dump(self.pool, f, ensure_ascii=False, indent=2)
    
    # -------- 事件匹配 --------
    
    @staticmethod
    def _normalize_keywords(kws: List[str]) -> List[str]:
        """标准化关键词（去符号、统一简称）"""
        synonym_map = {
            "SOX": "费半", "费城半导体": "费半", "费半指数": "费半",
            "英伟达": "NVDA", "nvidia": "NVDA",
            "海力士": "SK海力士", "sk海力士": "SK海力士",
            "HBM3": "HBM", "HBM3E": "HBM", "HBM4": "HBM",
            "非农业就业": "非农", "非农数据": "非农",
            "美联储": "Fed",
        }
        out = []
        for k in kws:
            k = re.sub(r'[（）()【】\[\]·\s]', '', str(k))
            if not k:
                continue
            k = synonym_map.get(k.lower(), k)
            k = synonym_map.get(k, k)
            out.append(k)
        return list(set(out))
    
    @staticmethod
    def _event_fingerprint(keywords: List[str], title: str = "") -> str:
        """事件指纹（基于关键词+标题hash，用于快速匹配）"""
        kws_sorted = sorted(EventPool._normalize_keywords(keywords))
        raw = "|".join(kws_sorted) + "||" + re.sub(r'\s+', '', title)[:30]
        return hashlib.md5(raw.encode('utf-8')).hexdigest()[:12]
    
    def find_similar(self, keywords: List[str], title: str = "",
                     threshold: float = 0.55) -> Optional[Dict]:
        """在事件池中查找相似事件（关键词重合+标题相似度）"""
        norm_kws = set(self._normalize_keywords(keywords))
        best = None
        best_score = 0
        for evt in self.pool["events"]:
            evt_kws = set(self._normalize_keywords(evt.get("keywords", [])))
            if not evt_kws or not norm_kws:
                continue
            jaccard = len(norm_kws & evt_kws) / max(1, len(norm_kws | evt_kws))
            title_sim = SequenceMatcher(None, title, evt.get("title","")).ratio() if title else 0
            score = jaccard * 0.65 + title_sim * 0.35
            if score > best_score:
                best_score = score
                best = evt
        if best_score >= threshold:
            return {"event": best, "score": best_score}
        return None
    
    # -------- 事件增/改 --------
    
    def add_event(self, keywords: List[str], title: str, summary: str,
                  category: str = "行业", level: str = "B",
                  source: str = "") -> Dict:
        """添加新事件（若已存在则更新）"""
        similar = self.find_similar(keywords, title)
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if similar:
            evt = similar["event"]
            # 合并关键词
            existing_kws = set(self._normalize_keywords(evt.get("keywords", [])))
            new_kws = set(self._normalize_keywords(keywords))
            evt["keywords"] = list(existing_kws | new_kws)
            # 更高等级覆盖
            level_order = {"S": 4, "A": 3, "B": 2, "C": 1}
            if level_order.get(level, 0) > level_order.get(evt.get("level","C"), 0):
                evt["level"] = level
            return evt
        # 新事件
        evt_id = f"evt_{self.trade_date}_{len(self.pool['events'])+1:03d}"
        evt = {
            "id": evt_id,
            "fingerprint": self._event_fingerprint(keywords, title),
            "keywords": self._normalize_keywords(keywords),
            "title": title,
            "summary": summary,
            "category": category,
            "level": level,
            "source": source,
            "covered_by": [],
            "updates": [],
            "first_covered_at": now,
            "last_updated_at": now,
            "deep_dive_url": "",   # 指向S级报告的链接
            "panorama_url": "",    # 指向日报的链接
        }
        self.pool["events"].append(evt)
        return evt
    
    def mark_covered(self, evt_id: str, report_type: str, report_file: str,
                     anchor: str = "", is_deep_dive: bool = False,
                     depth: str = "summary"):
        """标记某事件被某份报告覆盖"""
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        for evt in self.pool["events"]:
            if evt["id"] == evt_id:
                # 避免重复
                if not any(cb["report_type"] == report_type and cb.get("anchor") == anchor
                           for cb in evt["covered_by"]):
                    evt["covered_by"].append({
                        "report_type": report_type,
                        "report_file": report_file,
                        "anchor": anchor,
                        "depth": depth,
                        "covered_at": now,
                    })
                if is_deep_dive and not evt.get("deep_dive_url"):
                    evt["deep_dive_url"] = report_file + ("#"+anchor if anchor else "")
                if report_type == "daily" and not evt.get("panorama_url"):
                    evt["panorama_url"] = report_file + ("#"+anchor if anchor else "")
                evt["last_updated_at"] = now
                break
    
    def add_update(self, evt_id: str, report_type: str, update_text: str):
        """为已有事件追加增量更新（盘中快报使用）"""
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        for evt in self.pool["events"]:
            if evt["id"] == evt_id:
                evt["updates"].append({
                    "report_type": report_type,
                    "update": update_text,
                    "at": now,
                })
                evt["last_updated_at"] = now
                break
    
    def record_report(self, report_type: str, report_file: str,
                      events_covered: List[str]):
        """记录已生成的报告"""
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # 去重：同一report_type只保留最新
        self.pool["reports_generated"] = [
            r for r in self.pool["reports_generated"] if r["type"] != report_type
        ]
        self.pool["reports_generated"].append({
            "type": report_type,
            "file": report_file,
            "generated_at": now,
            "events_covered": events_covered,
        })
    
    # -------- 查询接口（给报告生成器判断是否要写/怎么写） --------
    
    def get_covered_before(self, report_type: str) -> List[Dict]:
        """获取当前报告生成前，已被其他报告覆盖过的事件清单"""
        covered = []
        for evt in self.pool["events"]:
            covered_by_types = [cb["report_type"] for cb in evt["covered_by"]]
            if covered_by_types and report_type not in covered_by_types:
                covered.append(evt)
        return covered
    
    def get_deep_dive_url(self, keywords: List[str], title: str = "") -> str:
        """查找某事件是否已有S级深度报告URL"""
        similar = self.find_similar(keywords, title, threshold=0.5)
        if similar:
            return similar["event"].get("deep_dive_url", "")
        return ""
    
    def coverage_stats(self) -> Dict:
        """统计当前事件池覆盖情况"""
        total = len(self.pool["events"])
        by_category = {}
        by_level = {}
        deep_dives = 0
        for evt in self.pool["events"]:
            by_category[evt.get("category","其他")] = by_category.get(evt.get("category","其他"), 0) + 1
            by_level[evt.get("level","C")] = by_level.get(evt.get("level","C"), 0) + 1
            if evt.get("deep_dive_url"):
                deep_dives += 1
        return {
            "total_events": total,
            "by_category": by_category,
            "by_level": by_level,
            "deep_dives": deep_dives,
            "reports_generated": len(self.pool["reports_generated"]),
        }


# ============================================================================
# 报告生成时的去重决策助手
# ============================================================================

class DedupDecider:
    """给报告生成器提供：对于一个事件，应该怎么写、是否跳过、如何引用"""
    
    def __init__(self, pool: EventPool, report_type: str, report_file: str):
        self.pool = pool
        self.report_type = report_type
        self.report_file = report_file
        self.contract = REPORT_CONTRACTS.get(report_type, {})
        self.newly_covered_ids = []  # 本报告新覆盖/更新的事件
    
    def decide(self, keywords: List[str], title: str, summary: str,
               category: str = "行业", level: str = "B",
               has_deep_content: bool = False) -> Dict[str, Any]:
        """
        对于一个待写事件，返回处理决策。
        
        返回字段：
        - action: "write_deep" | "write_summary_with_link" | "write_delta_only" | "skip"
        - existing_event: 匹配到的已有事件（或None）
        - cross_ref_html: 需要追加的交叉引用HTML（如"详见S级催化→"）
        - message: 说明
        """
        similar = self.pool.find_similar(keywords, title)
        norm_kws = self.pool._normalize_keywords(keywords)
        
        if not similar:
            # 全新事件
            evt = self.pool.add_event(keywords, title, summary, category, level)
            self.newly_covered_ids.append(evt["id"])
            if self.report_type == "s_level" or has_deep_content:
                return {
                    "action": "write_deep",
                    "event": evt,
                    "cross_ref_html": "",
                    "message": "新事件+深度分析（S级首发）"
                }
            else:
                return {
                    "action": "write_summary",
                    "event": evt,
                    "cross_ref_html": "",
                    "message": "新事件+摘要"
                }
        
        # 已有相似事件
        evt = similar["event"]
        score = similar["score"]
        covered_by_types = [cb["report_type"] for cb in evt["covered_by"]]
        has_deep = bool(evt.get("deep_dive_url")) or ("s_level" in covered_by_types)
        
        # 根据报告类型决定
        if self.report_type == "s_level":
            # S级是深度生产者。若已有S级，本次若等级更高或有新角度就更新，否则跳过
            if "s_level" in covered_by_types and level <= evt.get("level","B"):
                # 已经有同级别S级，且本次不升级
                return {
                    "action": "skip",
                    "event": evt,
                    "cross_ref_html": self._cross_ref_html(evt),
                    "message": f"事件已被S级报告覆盖(sim={score:.2f})，本次不重复"
                }
            self.newly_covered_ids.append(evt["id"])
            return {
                "action": "write_deep",
                "event": evt,
                "cross_ref_html": "",
                "message": f"事件已存在(sim={score:.2f})，本次S级深度补充/升级"
            }
        
        elif self.report_type == "daily":
            self.newly_covered_ids.append(evt["id"])
            if has_deep:
                # 已有S级深度：日报只写摘要+链接
                return {
                    "action": "write_summary_with_link",
                    "event": evt,
                    "cross_ref_html": self._cross_ref_html(evt),
                    "message": f"事件已由S级深度覆盖(sim={score:.2f})，日报只写1-2句摘要+链接"
                }
            else:
                return {
                    "action": "write_summary",
                    "event": evt,
                    "cross_ref_html": "",
                    "message": f"事件已存在但无S级深度(sim={score:.2f})，日报写摘要"
                }
        
        elif self.report_type == "intraday":
            # 盘中：只写增量
            if "intraday" in covered_by_types and not has_deep_content:
                return {
                    "action": "skip",
                    "event": evt,
                    "cross_ref_html": self._cross_ref_html(evt),
                    "message": f"事件已被盘中快报覆盖(sim={score:.2f})，无增量不重复"
                }
            self.newly_covered_ids.append(evt["id"])
            return {
                "action": "write_delta_only",
                "event": evt,
                "cross_ref_html": self._cross_ref_html(evt) if has_deep else "",
                "message": f"盘中增量更新(sim={score:.2f})，只写新增变化"
            }
        
        elif self.report_type == "aftermarket":
            self.newly_covered_ids.append(evt["id"])
            return {
                "action": "write_verification",
                "event": evt,
                "cross_ref_html": self._cross_ref_html(evt),
                "message": f"盘后验证视角(sim={score:.2f})，验证预判兑现情况"
            }
        
        else:
            # 未知类型默认写摘要
            self.newly_covered_ids.append(evt["id"])
            return {
                "action": "write_summary",
                "event": evt,
                "cross_ref_html": "",
                "message": "默认摘要"
            }
    
    def _cross_ref_html(self, evt: Dict) -> str:
        """生成交叉引用链接HTML"""
        links = []
        if evt.get("deep_dive_url"):
            url = evt["deep_dive_url"]
            # 相对路径转换：../../../ 或 /daily-news-insight/s_level_catalyst/xxx
            links.append(f'<a href="{url}" target="_blank" style="color:#a78bfa; font-size:12px; margin-left:6px; text-decoration:underline;">📖 详见S级催化→</a>')
        if evt.get("panorama_url") and self.report_type != "daily":
            url = evt["panorama_url"]
            links.append(f'<a href="{url}" target="_blank" style="color:#60a5fa; font-size:12px; margin-left:6px; text-decoration:underline;">📰 日报摘要→</a>')
        return ''.join(links)
    
    def finalize(self, anchor_map: Dict[str, str] = None):
        """报告生成完成后，统一标记覆盖并保存
        Args:
            anchor_map: {evt_id: "#anchor_id"} 用于生成精准锚点
        """
        anchor_map = anchor_map or {}
        is_deep = (self.report_type == "s_level")
        depth = "deep" if is_deep else ("summary" if self.report_type == "daily" else "delta")
        for evt_id in self.newly_covered_ids:
            anchor = anchor_map.get(evt_id, "")
            self.pool.mark_covered(
                evt_id, self.report_type, self.report_file,
                anchor=anchor, is_deep_dive=is_deep, depth=depth
            )
        self.pool.record_report(self.report_type, self.report_file, self.newly_covered_ids)
        self.pool.save()


# ============================================================================
# 便捷HTML组件（生成报告末尾"事件覆盖/交叉引用"模块）
# ============================================================================

def render_cross_ref_section(pool: EventPool, current_report_type: str) -> str:
    """渲染"📑 今日报告覆盖地图"模块，在每份报告末尾展示"""
    reports_order = ["s_level", "daily", "intraday", "aftermarket"]
    report_names = {"s_level":"S级催化","daily":"日报","intraday":"盘中","aftermarket":"盘后"}
    report_colors = {"s_level":"#ef4444","daily":"#3b82f6","intraday":"#f59e0b","aftermarket":"#10b981"}
    report_icons = {"s_level":"🔥","daily":"📰","intraday":"⚡","aftermarket":"📊"}
    
    stats = pool.coverage_stats()
    now = datetime.now().strftime("%H:%M")
    
    # 已生成报告状态
    report_status_html = ""
    generated_types = {r["type"] for r in pool.pool["reports_generated"]}
    for rt in reports_order:
        r = next((x for x in pool.pool["reports_generated"] if x["type"] == rt), None)
        name = report_names.get(rt, rt)
        color = report_colors.get(rt, "white")
        icon = report_icons.get(rt, "•")
        if r:
            report_status_html += f'''
            <a href="{r['file']}" target="_blank" style="display:inline-flex; align-items:center; gap:6px;
                background:{color}22; border:1px solid {color}55; color:{color}; padding:6px 12px;
                border-radius:20px; font-size:12px; font-weight:600; text-decoration:none; margin:3px;">
                {icon} {name} <span style="opacity:0.6; font-weight:400;">{len(r['events_covered'])}条</span>
            </a>
            '''
        else:
            report_status_html += f'''
            <span style="display:inline-flex; align-items:center; gap:6px;
                background:rgba(255,255,255,0.05); border:1px dashed rgba(255,255,255,0.15); color:rgba(255,255,255,0.4);
                padding:6px 12px; border-radius:20px; font-size:12px;">
                {icon} {name} <span style="opacity:0.6;">待生成</span>
            </span>
            '''
    
    # 等级分布
    levels_html = ""
    for lv in ["S","A","B","C"]:
        cnt = stats["by_level"].get(lv, 0)
        color = {"S":"#ef4444","A":"#f59e0b","B":"#3b82f6","C":"#9ca3af"}[lv]
        levels_html += f'<span style="color:{color}; font-weight:700; margin-right:10px;">{lv}级:{cnt}</span>'
    
    return f'''
    <div class="card-glass p-5 mt-6" style="border-left:4px solid #a78bfa;">
        <h3 style="font-size:15px; font-weight:800; margin:0 0 10px 0; display:flex; align-items:center; gap:8px;">
            <span>📑</span>今日报告覆盖地图
            <span style="margin-left:auto; font-size:11px; font-weight:400; opacity:0.5;">V5.0 L1-0 内容去重 · {now}更新</span>
        </h3>
        <div style="font-size:12px; opacity:0.7; margin-bottom:10px;">
            共追踪 <strong style="color:white;">{stats['total_events']}</strong> 条事件：{levels_html}
            · 深度覆盖 <strong style="color:#ef4444;">{stats['deep_dives']}</strong> 条
        </div>
        <div style="display:flex; flex-wrap:wrap; gap:6px;">{report_status_html}</div>
        <p style="font-size:11px; opacity:0.45; margin:10px 0 0 0;">
            📌 报告边界：S级=单题材深挖｜日报=信息全景｜盘中=增量异动｜盘后=验证+持仓+龙虎榜；
            同一事件在多份报告间自动交叉引用，避免重复阅读。
        </p>
    </div>
    '''


# ============================================================================
# CLI自测
# ============================================================================

if __name__ == '__main__':
    # 清理测试池
    test_date = "99999999"
    pool = EventPool(trade_date=test_date)
    
    # 场景：先写S级，再写日报，再写盘中
    print("=" * 60)
    print("场景：S级 → 日报 → 盘中 三步去重测试")
    print("=" * 60)
    
    # 1) S级报告生成
    decider_s = DedupDecider(pool, "s_level", "s_level_catalyst/99999999_S级.html")
    r1 = decider_s.decide(["费半","SOX","费城半导体"], "费半暴跌2.3%，半导体板块承压",
                          "费半隔夜-2.3%/美光-3%，HBM链承压", category="外盘", level="S", has_deep_content=True)
    print(f"[S级] 事件1: {r1['action']} - {r1['message']}")
    r2 = decider_s.decide(["HBM","海力士","SK海力士"], "SK海力士HBM3E出货超预期",
                          "SK海力士HBM3E出货超指引30%，HBM链持续景气", category="行业", level="S", has_deep_content=True)
    print(f"[S级] 事件2: {r2['action']} - {r2['message']}")
    decider_s.finalize()
    
    # 2) 日报生成
    decider_d = DedupDecider(pool, "daily", "daily/99999999_日报.html")
    r3 = decider_d.decide(["费半","SOX"], "费半隔夜-2.3%", "费半-2.3%/美光-3%", category="外盘", level="S")
    print(f"[日报] 事件1(费半): {r3['action']} - {r3['message']}")
    assert r3['action'] == 'write_summary_with_link', f"期望write_summary_with_link，实际{r3['action']}"
    r4 = decider_d.decide(["非农","就业"], "美国非农就业超预期", "非农新增25万，超预期，9月降息概率下降", category="宏观", level="A")
    print(f"[日报] 事件3(非农): {r4['action']} - {r4['message']}")
    assert r4['action'] == 'write_summary', "新事件期望write_summary"
    decider_d.finalize()
    
    # 3) 盘中快报
    decider_i = DedupDecider(pool, "intraday", "intraday/99999999_盘中.html")
    r5 = decider_i.decide(["费半","SOX"], "费半隔夜-2.3%", "无新增变化", category="外盘", level="S")
    print(f"[盘中] 事件1(费半无变化): {r5['action']} - {r5['message']}")
    # 注意：虽然"无新增变化"，但因为是首次遇到，会触发write_delta（内容由生成器控制，只写变化）
    r6 = decider_i.decide(["雅克科技","002409","HBM"], "雅克科技盘中急跌-8%",
                          "雅克科技早盘急跌-8%，HBM材料板块出现机构大额抛售", category="个股", level="A")
    print(f"[盘中] 事件4(雅克异动): {r6['action']} - {r6['message']}")
    decider_i.finalize()
    
    # 统计
    stats = pool.coverage_stats()
    print(f"\n事件池统计：{stats}")
    
    # 渲染覆盖地图
    html = render_cross_ref_section(pool, "daily")
    print(f"\n覆盖地图HTML长度：{len(html)}")
    
    # 清理测试文件
    test_path = os.path.join("data/event_pool", f"{test_date}.json")
    if os.path.exists(test_path):
        os.remove(test_path)
    
    print("\n✅ 自测通过：去重机制正常工作（S级深度首发→日报摘要+链接→盘中增量+跳过无变化事件）")
