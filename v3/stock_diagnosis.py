"""
股票深度诊断模块 - V5.0 L1-4
提供多维度持仓诊断能力：
1. 估值锚：PE/PB分位数（vs 历史/行业），标注高估/合理/低估
2. 资金流向：近5日主力净流入/流出趋势
3. 关联标的联动：板块/产业链联动分析
4. 条件预案：价格触发下的减仓/补仓/清仓操作预案
5. 走势研判：支撑位/压力位/均线位置

基于本地数据+静态规则，不依赖实时API（盘后分析/周末开发用）；
实盘使用时由 daily_update.py 灌入实时数据后增强准确度。
"""
import json
import os
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple, Any
from dataclasses import dataclass, field, asdict
from pathlib import Path


# ============================================================================
# 持仓股关联图谱（人工维护的产业链关系）
# ============================================================================
# 每个key对应一个持仓股代码，value含：产业链、关联标的、驱动逻辑
PORTFOLIO_LINKAGE = {
    "002409": {  # 雅克科技
        "name": "雅克科技",
        "main_chain": "HBM/半导体材料",
        "core_logic": "HBM前驱体+光刻胶+电子特气，深度绑定SK海力士/三星/长鑫",
        "upstream": ["前驱体原材料", "光刻胶树脂"],
        "downstream": ["HBM3E/HBM4", "先进封装", "DDR5"],
        "linked_stocks": [
            {"code": "002049", "name": "紫光国微", "relation": "HBM/存储芯片同业", "corr": 0.65},
            {"code": "300666", "name": "江丰电子", "relation": "半导体材料-靶材", "corr": 0.55},
            {"code": "300236", "name": "上海新阳", "relation": "半导体材料-光刻胶", "corr": 0.60},
            {"code": "002371", "name": "北方华创", "relation": "半导体设备-Beta锚", "corr": 0.50},
            {"code": "688981", "name": "中芯国际", "relation": "晶圆代工景气度", "corr": 0.55},
            {"code": "301217", "name": "铜冠铜箔", "relation": "存储链PCB/HVLP铜箔", "corr": 0.40},
        ],
        "overseas_anchors": ["SK海力士", "三星电子", "美光", "费城半导体指数(SOX)"],
        "key_catalysts": ["HBM出货指引", "三星/海力士资本开支", "国产光刻胶验证进展"],
        "key_risks": ["HBM扩产低于预期", "光刻胶国产替代进度", "半导体板块系统性杀跌"],
    },
    "002837": {  # 英维克
        "name": "英维克",
        "main_chain": "液冷散热/AI算力基础设施",
        "core_logic": "数据中心液冷+储能温控+机柜温控，绑定阿里/字节/曙光/浪潮",
        "upstream": ["压缩机", "冷板", "铜管/连接件"],
        "downstream": ["AI数据中心", "算力服务器", "储能电站"],
        "linked_stocks": [
            {"code": "300861", "name": "高澜股份", "relation": "液冷同业-冷板式", "corr": 0.70},
            {"code": "300499", "name": "高澜股份B", "relation": "液冷板块联动", "corr": 0.60},
            {"code": "603138", "name": "海量数据", "relation": "数据中心/算力", "corr": 0.50},
            {"code": "688256", "name": "寒武纪", "relation": "AI算力芯片-需求端", "corr": 0.40},
            {"code": "000977", "name": "浪潮信息", "relation": "AI服务器-下游客户", "corr": 0.55},
        ],
        "overseas_anchors": ["英伟达(NVDA)", "博通(AVGO)", "Vertiv(VRT)", "奇宏(AVC)"],
        "key_catalysts": ["英伟达B系列/GB300放量", "国内AI服务器招标", "液冷渗透加速"],
        "key_risks": ["AI Capex低于预期", "液冷价格战", "客户集中度风险"],
    },
    "301217": {  # 铜冠铜箔
        "name": "铜冠铜箔",
        "main_chain": "HVLP铜箔/PCB/存储封装",
        "core_logic": "HVLP极低轮廓铜箔+锂电铜箔，受益AI服务器PCB/HBM载板升级",
        "upstream": ["电解铜", "铜材", "硫酸"],
        "downstream": ["AI服务器PCB", "HBM载板", "高级封装基板", "锂电负极"],
        "linked_stocks": [
            {"code": "603920", "name": "世运电路", "relation": "AI服务器PCB-下游", "corr": 0.55},
            {"code": "002463", "name": "沪电股份", "relation": "PCB/载板-同业", "corr": 0.50},
            {"code": "002409", "name": "雅克科技", "relation": "存储链材料-上游", "corr": 0.40},
            {"code": "300476", "name": "胜宏科技", "relation": "PCB-HDI", "corr": 0.45},
            {"code": "600362", "name": "江西铜业", "relation": "铜价-上游成本", "corr": -0.30},
        ],
        "overseas_anchors": ["LME铜价", "台光电", "欣兴电子", "南亚电路板"],
        "key_catalysts": ["铜箔加工费上调", "HVLP铜箔客户验证", "AI服务器PCB订单"],
        "key_risks": ["电解铜价大涨挤压毛利", "HVLP良率低于预期", "锂电铜箔过剩"],
    },
    "002789": {  # *ST建艺
        "name": "*ST建艺",
        "main_chain": "建筑装饰/ST风险股",
        "core_logic": "⚠️ST股，7/6起扩幅至10%，流动性差，退市风险",
        "upstream": ["建材/施工"],
        "downstream": ["基建/装饰"],
        "linked_stocks": [
            {"code": "002060", "name": "粤水电", "relation": "建筑施工同业", "corr": 0.20},
        ],
        "overseas_anchors": [],
        "key_catalysts": ["重组/摘帽预期（低概率）"],
        "key_risks": ["退市风险", "扩幅10%流动性风险", "业绩持续亏损"],
    },
}


# ============================================================================
# 估值锚分析（PE/PB分位数模型）
# ============================================================================

# 行业PE/PB中枢（静态参考，可由data_loader定期更新）
# 格式：{industry: {pe_median, pb_median, pe_25, pe_75, pb_25, pb_75, historical_pe_low, historical_pe_high}}
INDUSTRY_VALUATION = {
    "液冷散热/AI算力": {
        "pe_ttm_median": 45, "pb_median": 4.5,
        "pe_25": 30, "pe_75": 70,
        "pb_25": 3.0, "pb_75": 7.0,
        "hist_pe_low": 20, "hist_pe_high": 95,
    },
    "电子/铜箔/PCB": {
        "pe_ttm_median": 35, "pb_median": 3.5,
        "pe_25": 25, "pe_75": 55,
        "pb_25": 2.5, "pb_75": 5.5,
        "hist_pe_low": 15, "hist_pe_high": 80,
    },
    "半导体材料/HBM": {
        "pe_ttm_median": 60, "pb_median": 5.5,
        "pe_25": 40, "pe_75": 90,
        "pb_25": 4.0, "pb_75": 9.0,
        "hist_pe_low": 30, "hist_pe_high": 130,
    },
    "建筑装饰/ST": {
        "pe_ttm_median": -1, "pb_median": 2.0,  # 亏损股
        "pe_25": -1, "pe_75": -1,
        "pb_25": 1.0, "pb_75": 3.0,
        "hist_pe_low": -1, "hist_pe_high": -1,
    },
}

# 个股当前估值快照（周末开发用，非实盘数据；实盘由daily_update写入data/stock_valuation/*.json）
STOCK_VALUATION_SNAPSHOT = {
    "002837": {
        "name": "英维克",
        "industry": "液冷散热/AI算力",
        "pe_ttm": None,  # 2025年可能亏损/PE失真，用PB
        "pb": 5.8,
        "market_cap": 240,  # 亿
        "pe_hist_percentile": None,
        "pb_hist_percentile": 35,  # PB分位35%（从高到低）
        "pe_industry_percentile": None,
        "pb_industry_percentile": 65,  # 高于行业65%
        "note": "业绩承压，PE失真，PB参考意义更大；深度破位后估值已回落至中位以下",
    },
    "301217": {
        "name": "铜冠铜箔",
        "industry": "电子/铜箔/PCB",
        "pe_ttm": 65,
        "pb": 9.2,
        "market_cap": 290,
        "pe_hist_percentile": 75,  # 历史估值75分位（偏贵）
        "pb_hist_percentile": 85,
        "pe_industry_percentile": 78,
        "pb_industry_percentile": 88,
        "note": "因AI铜箔预期PE/PB处历史高位，纯题材驱动，业绩尚未兑现",
    },
    "002409": {
        "name": "雅克科技",
        "industry": "半导体材料/HBM",
        "pe_ttm": 72,
        "pb": 6.8,
        "market_cap": 980,
        "pe_hist_percentile": 55,
        "pb_hist_percentile": 60,
        "pe_industry_percentile": 58,
        "pb_industry_percentile": 55,
        "note": "HBM高景气给予估值溢价，但两日累跌-15.5%后估值已从高位回落至合理偏上区间",
    },
    "002789": {
        "name": "*ST建艺",
        "industry": "建筑装饰/ST",
        "pe_ttm": None,
        "pb": 4.5,
        "market_cap": 25,
        "pe_hist_percentile": None,
        "pb_hist_percentile": 90,
        "pe_industry_percentile": None,
        "pb_industry_percentile": 95,
        "note": "⚠️ST股，PB高位+业绩亏损，纯炒作逻辑，绝不能留仓",
    },
}


def classify_valuation(pe_percentile: Optional[float],
                       pb_percentile: Optional[float]) -> Dict[str, Any]:
    """根据分位数判断估值状态
    
    Returns:
        {level, label, color, desc}
        level: undervalued(低估) / reasonable(合理) / overvalued(高估) / extreme(极度高估)
    """
    # 取可用的分位数
    ps = [x for x in [pe_percentile, pb_percentile] if x is not None]
    if not ps:
        return {"level": "unknown", "label": "估值数据不足", "color": "#9ca3af",
                "desc": "PE/PB缺失，无法判断估值水平"}
    
    avg_p = sum(ps) / len(ps)
    
    if avg_p >= 85:
        return {
            "level": "extreme",
            "label": "极度高估 🔴",
            "color": "#ef4444",
            "badge_bg": "rgba(239,68,68,0.15)",
            "badge_border": "rgba(239,68,68,0.3)",
            "desc": "估值处历史高位，杀估值风险大，严格止盈不追高",
        }
    elif avg_p >= 65:
        return {
            "level": "overvalued",
            "label": "偏高估 🟡",
            "color": "#f59e0b",
            "badge_bg": "rgba(245,158,11,0.15)",
            "badge_border": "rgba(245,158,11,0.3)",
            "desc": "估值高于行业/历史中枢，已有一定泡沫，逢高分批锁利",
        }
    elif avg_p >= 35:
        return {
            "level": "reasonable",
            "label": "估值合理 ⚪",
            "color": "#3b82f6",
            "badge_bg": "rgba(59,130,246,0.15)",
            "badge_border": "rgba(59,130,246,0.3)",
            "desc": "估值处于合理区间，持有或逢低布局",
        }
    else:
        return {
            "level": "undervalued",
            "label": "低估 🟢",
            "color": "#10b981",
            "badge_bg": "rgba(16,185,129,0.15)",
            "badge_border": "rgba(16,185,129,0.3)",
            "desc": "估值处历史/行业低位，具备安全边际，可逢低加仓",
        }


# ============================================================================
# 资金流向分析（近5日主力净流入）
# ============================================================================

# 近5日资金流快照（周末开发用；实盘由daily_update写入data/stock_fundflow/*.json）
# 格式：{"D-4":净流入(亿), "D-3":.., "D-2":.., "D-1":.., "D-0":..}
STOCK_FUNDFLOW_SNAPSHOT = {
    "002837": {
        "name": "英维克",
        "days": {
            "D-4": -3.82, "D-3": -5.15, "D-2": -2.93, "D-1": -2.96, "D-0": -0.41,
        },
        "note": "近5日主力累计净流出约-15.27亿，连续出货迹象明显，卖压沉重",
    },
    "301217": {
        "name": "铜冠铜箔",
        "days": {
            "D-4": +4.28, "D-3": -2.15, "D-2": -3.42, "D-1": -2.73, "D-0": -1.85,
        },
        "note": "近5日主力净流入-5.87亿，由前期净流入转为连续净卖出，高位派发",
    },
    "002409": {
        "name": "雅克科技",
        "days": {
            "D-4": +2.15, "D-3": +1.08, "D-2": -3.52, "D-1": -3.87, "D-0": -1.91,
        },
        "note": "近5日主力净流出-6.07亿，近两日机构大额兑现，光刻胶流出榜第3",
    },
    "002789": {
        "name": "*ST建艺",
        "days": {
            "D-4": -0.08, "D-3": -0.05, "D-2": -0.12, "D-1": -0.03, "D-0": -0.02,
        },
        "note": "近5日资金持续小幅流出，流动性枯竭，无主力介入",
    },
}


def analyze_fundflow(code: str) -> Dict[str, Any]:
    """分析近5日主力资金流向趋势"""
    data = STOCK_FUNDFLOW_SNAPSHOT.get(code, {})
    days = data.get("days", {})
    if not days:
        return {"trend": "unknown", "total": 0, "bars": [], "desc": "无资金流数据"}
    
    # 按日期排序
    order = ["D-4", "D-3", "D-2", "D-1", "D-0"]
    values = [days.get(k, 0) for k in order]
    total = sum(values)
    
    # 判断趋势
    inflow_days = sum(1 for v in values if v > 0)
    outflow_days = 5 - inflow_days
    recent_3d = sum(values[-3:])
    recent_1d = values[-1]
    
    if total < -10:
        trend = "massive_outflow"
        trend_label = "大幅出逃 🔴"
        trend_color = "#ef4444"
    elif total < -3:
        trend = "outflow"
        trend_label = "持续流出 🟡"
        trend_color = "#f59e0b"
    elif total < 0:
        trend = "slight_outflow"
        trend_label = "小幅流出 ⚪"
        trend_color = "#9ca3af"
    elif total < 3:
        trend = "slight_inflow"
        trend_label = "小幅流入 🟢"
        trend_color = "#10b981"
    else:
        trend = "inflow"
        trend_label = "主力抢筹 🔴↑"
        trend_color = "#10b981"
    
    # 加速度判断（近3日对比前2日）
    first_2d = sum(values[:2])
    accel = "neutral"
    if first_2d > 0 and recent_3d < -first_2d * 0.5:
        accel = "deteriorating"
    elif first_2d < 0 and recent_3d > abs(first_2d) * 0.5:
        accel = "improving"
    
    # 生成柱状图数据（用于HTML内联SVG）
    max_abs = max(abs(v) for v in values) if values else 1
    bars = []
    for i, (k, v) in enumerate(zip(order, values)):
        is_in = v > 0
        h_pct = abs(v) / max_abs * 100 if max_abs > 0 else 0
        bars.append({
            "day": k.replace("D-", "前").replace("前0", "今"),
            "value": v,
            "height_pct": h_pct,
            "color": "#10b981" if is_in else "#ef4444",
            "is_inflow": is_in,
        })
    
    return {
        "trend": trend,
        "trend_label": trend_label,
        "trend_color": trend_color,
        "accel": accel,
        "total": total,
        "recent_3d": recent_3d,
        "recent_1d": recent_1d,
        "inflow_days": inflow_days,
        "outflow_days": outflow_days,
        "bars": bars,
        "note": data.get("note", ""),
    }


# ============================================================================
# 支撑/压力位 + 均线位置研判
# ============================================================================

# 个股技术面快照（含均线/支撑/压力）
STOCK_TECHNICAL_SNAPSHOT = {
    "002837": {
        "name": "英维克",
        "current": 71.43,
        "ma5": 72.30, "ma10": 74.85, "ma20": 78.60, "ma60": 89.50,
        "supports": [
            {"price": 70.50, "type": "前低/心理关口", "strength": "strong"},
            {"price": 68.00, "type": "前期平台/缺口支撑", "strength": "medium"},
            {"price": 65.00, "type": "2024年低点参考", "strength": "weak"},
        ],
        "resistances": [
            {"price": 74.41, "type": "近期高点(7/3)", "strength": "strong"},
            {"price": 78.60, "type": "MA20", "strength": "medium"},
            {"price": 85.00, "type": "前期密集成交区", "strength": "medium"},
        ],
        "ma_position": "price_below_all",  # 价格低于所有均线
        "trend": "down",
        "volume_trend": "shrinking",  # 缩量
        "pattern": "缩量十字星，下跌中继或企稳信号待确认",
    },
    "301217": {
        "name": "铜冠铜箔",
        "current": 154.63,
        "ma5": 160.20, "ma10": 162.50, "ma20": 158.80, "ma60": 148.20,
        "supports": [
            {"price": 150.00, "type": "移动止盈线/7/3最低", "strength": "critical"},
            {"price": 148.20, "type": "MA60", "strength": "strong"},
            {"price": 140.00, "type": "前期平台", "strength": "medium"},
        ],
        "resistances": [
            {"price": 160.20, "type": "MA5", "strength": "medium"},
            {"price": 164.56, "type": "7/3最高(减仓窗口)", "strength": "strong"},
            {"price": 175.00, "type": "前高/心理关口", "strength": "strong"},
        ],
        "ma_position": "price_below_ma5_10_20_above_ma60",
        "trend": "pullback",
        "volume_trend": "heavy",  # 放量
        "pattern": "高位放量回调，跌破MA5/MA20，150元关键支撑",
    },
    "002409": {
        "name": "雅克科技",
        "current": 199.50,
        "ma5": 208.40, "ma10": 215.60, "ma20": 212.30, "ma60": 185.50,
        "supports": [
            {"price": 199.00, "type": "200元心理关口(险守)", "strength": "critical"},
            {"price": 195.00, "type": "减仓线/前期支撑", "strength": "strong"},
            {"price": 185.50, "type": "MA60", "strength": "strong"},
        ],
        "resistances": [
            {"price": 205.00, "type": "短期反弹位", "strength": "medium"},
            {"price": 210.00, "type": "减仓窗口下沿", "strength": "strong"},
            {"price": 220.00, "type": "MA10/前期高点", "strength": "strong"},
        ],
        "ma_position": "price_below_ma5_10_20_above_ma60",
        "trend": "sharp_correction",
        "volume_trend": "heavy",
        "pattern": "两日累跌-15.5%，跌破5日线，200元关口险守，待企稳信号",
    },
    "002789": {
        "name": "*ST建艺",
        "current": 11.74,
        "ma5": 11.82, "ma10": 12.05, "ma20": 12.30, "ma60": 12.80,
        "supports": [
            {"price": 11.50, "type": "前期低点", "strength": "medium"},
            {"price": 11.00, "type": "退市整理参考位", "strength": "weak"},
        ],
        "resistances": [
            {"price": 12.05, "type": "MA10", "strength": "medium"},
            {"price": 12.50, "type": "止损位", "strength": "strong"},
        ],
        "ma_position": "price_below_all",
        "trend": "down",
        "volume_trend": "shrinking",
        "pattern": "最后交易日缩量，7/6起扩幅10%，流动性风险极高",
    },
}


def analyze_technical(code: str) -> Dict[str, Any]:
    """技术面研判：均线/支撑/压力/形态"""
    t = STOCK_TECHNICAL_SNAPSHOT.get(code, {})
    if not t:
        return {"status": "no_data", "desc": "无技术面数据"}
    
    cur = t["current"]
    
    # 均线状态
    ma_status = []
    for ma_name, ma_key in [("MA5", "ma5"), ("MA10", "ma10"), ("MA20", "ma20"), ("MA60", "ma60")]:
        ma_v = t[ma_key]
        diff_pct = (cur - ma_v) / ma_v * 100
        above = cur > ma_v
        ma_status.append({
            "name": ma_name,
            "value": ma_v,
            "diff_pct": diff_pct,
            "above": above,
            "color": "#10b981" if above else "#ef4444",
            "label": f"{'站上' if above else '跌破'}{ma_name}",
        })
    
    # 均线排列判断
    above_count = sum(1 for m in ma_status if m["above"])
    if above_count == 4:
        ma_arrange = "多头排列 🟢"
        ma_arrange_color = "#10b981"
    elif above_count >= 2:
        ma_arrange = "多空交织 🟡"
        ma_arrange_color = "#f59e0b"
    else:
        ma_arrange = "空头排列 🔴"
        ma_arrange_color = "#ef4444"
    
    # 找最近的支撑和压力
    supports = sorted(t["supports"], key=lambda x: -x["price"])
    resistances = sorted(t["resistances"], key=lambda x: x["price"])
    nearest_support = None
    nearest_resistance = None
    for s in supports:
        if s["price"] <= cur:
            nearest_support = s
            break
    for r in resistances:
        if r["price"] >= cur:
            nearest_resistance = r
            break
    
    return {
        "current": cur,
        "ma_status": ma_status,
        "ma_arrange": ma_arrange,
        "ma_arrange_color": ma_arrange_color,
        "ma_position": t.get("ma_position", ""),
        "supports": supports,
        "resistances": resistances,
        "nearest_support": nearest_support,
        "nearest_resistance": nearest_resistance,
        "trend": t.get("trend", ""),
        "volume_trend": t.get("volume_trend", ""),
        "pattern": t.get("pattern", ""),
        "next_support_distance": (cur - nearest_support["price"]) / cur * 100 if nearest_support else None,
        "next_resistance_distance": (nearest_resistance["price"] - cur) / cur * 100 if nearest_resistance else None,
    }


# ============================================================================
# 条件预案生成器
# ============================================================================

def _fmt_price(p: float) -> str:
    return f"{p:.2f}"


def generate_contingency_plan(stock: Dict[str, Any], linkage: Dict,
                              valuation: Dict, tech: Dict) -> Dict[str, Any]:
    """根据持仓状态+估值+技术面，生成条件化操作预案
    
    返回包含减仓/补仓/清仓/持有四套条件预案
    """
    name = stock.get("name", "")
    code = stock.get("code", "")
    cost = stock.get("cost_price", 0)
    cur = stock.get("current_price", 0)
    stop = stock.get("stop_loss_price", 0)
    profit_pct = (cur - cost) / cost * 100 if cost else 0
    
    plan = {
        "reduce_1_3": [],   # 减1/3条件
        "reduce_1_2": [],   # 减1/2条件
        "clear_all": [],    # 清仓条件
        "add_position": [], # 补仓条件（极少使用）
        "hold_conditions": [],  # 继续持有条件
    }
    
    # 特殊处理ST股
    if "ST" in name or "建艺" in name:
        plan["clear_all"].append({"condition": "任何价格", "action": "集合竞价清仓", "priority": "P0",
                                   "reason": "7/6起扩幅10%，退市/流动性风险极大，不计成本离场"})
        return plan
    
    # 深度破止损（英维克场景）
    if cur < stop and profit_pct < -15:
        plan["reduce_1_2"].append({
            "condition": f"反弹至73-75元区间（近高{tech.get('nearest_resistance',{}).get('price','')}）",
            "action": "反弹减仓1/2", "priority": "P0",
            "reason": f"深度破止损{profit_pct:.1f}%，反弹给逃命窗口，减仓1/2降低风险敞口"
        })
        plan["clear_all"].append({
            "condition": "跌破70元前低",
            "action": "无条件清仓", "priority": "P0",
            "reason": "70元为心理关口+前低，跌破将打开下跌空间至65元"
        })
        plan["clear_all"].append({
            "condition": "大盘或AI算力板块单日暴跌>3%",
            "action": "当日不计成本清仓", "priority": "P0",
            "reason": "弱势股遇系统性杀跌无承接，流动性踩踏风险"
        })
        plan["hold_conditions"].append({
            "condition": "71-73震荡且成交量缩至25亿以下，且板块企稳",
            "action": "暂持等待反弹", "priority": "P2",
            "reason": "深套不宜割在地板，但反弹必须减仓"
        })
        # 补仓：极度谨慎，仅小仓位试错
        plan["add_position"].append({
            "condition": "放量站稳MA20(78元)且连续3日不破，板块β转强",
            "action": "仅用≤10%仓位试错", "priority": "P3-严控",
            "reason": "趋势反转信号确认后才可少量参与，严禁摊低成本"
        })
        return plan
    
    # 浮盈股（铜冠铜箔/雅克科技场景）
    if profit_pct > 30:
        # 已大赚，保护利润优先
        
        # 第一减仓点
        res1 = tech.get("resistances", [{}])[0] if tech.get("resistances") else {}
        res2 = tech.get("resistances", [{}, {}])[1] if len(tech.get("resistances", [])) > 1 else {}
        sup1 = tech.get("nearest_support", {})
        
        # 结合止盈线
        if code == "301217":
            trailing_stop = 150.0
            take_profit_zone = "160-165"
        elif code == "002409":
            trailing_stop = 195.0
            take_profit_zone = "210-215"
        else:
            trailing_stop = stop
            take_profit_zone = f"{stop:.0f}-{cur*1.05:.0f}"
        
        plan["reduce_1_3"].append({
            "condition": f"反弹至{take_profit_zone}区间放量滞涨",
            "action": "减仓1/3锁利", "priority": "P1",
            "reason": "高位放量滞涨是经典出货信号，先兑现1/3利润"
        })
        plan["reduce_1_3"].append({
            "condition": "板块高潮日（板块涨停>5家/指数涨>3%）",
            "action": "减仓1/3", "priority": "P1",
            "reason": "板块高潮次日易分化，锁利为上"
        })
        plan["reduce_1_2"].append({
            "condition": f"跌破MA20({tech.get('ma_status',[{},{}])[2].get('value','')})且次日不能收回",
            "action": "减仓至1/2以下", "priority": "P0",
            "reason": "跌破MA20意味着中期趋势走弱"
        })
        plan["reduce_1_2"].append({
            "condition": f"跌破移动止盈线{trailing_stop}元",
            "action": "减仓1/2", "priority": "P0",
            "reason": "移动止盈线是利润保护底线，跌破必须减仓"
        })
        plan["clear_all"].append({
            "condition": f"跌破MA60({tech.get('ma_status',[{},{},{},{}])[3].get('value','')})",
            "action": "清仓离场", "priority": "P0",
            "reason": "跌破MA60=中期趋势破坏，走为上"
        })
        plan["clear_all"].append({
            "condition": "核心催化被证伪（如HBM扩产不及预期/客户验证失败）",
            "action": "不计成本清仓", "priority": "P0",
            "reason": "逻辑破坏时估值支撑失效"
        })
        plan["hold_conditions"].append({
            "condition": f"在MA5~MA20之间健康调整且成交量缩量",
            "action": "底仓持有", "priority": "P2",
            "reason": "强势股调整正常，缩量调整后仍有新高可能"
        })
        plan["add_position"] = []  # 浮盈大票原则上不补仓
    
    elif profit_pct > 0:
        # 小幅浮盈
        plan["reduce_1_3"].append({
            "condition": "触及压力位放量回落",
            "action": "减仓1/3", "priority": "P1",
            "reason": "压力位附近先锁部分利润"
        })
        plan["clear_all"].append({
            "condition": f"跌破成本价{cost:.2f}且不能当日收回",
            "action": "清仓", "priority": "P0",
            "reason": "保本出局"
        })
    else:
        # 小幅浮亏但未破止损
        plan["clear_all"].append({
            "condition": f"跌破止损价{stop:.2f}",
            "action": "无条件止损", "priority": "P0",
            "reason": "止损是铁律"
        })
        plan["add_position"].append({
            "condition": "回踩MA20企稳+板块β转强+放量",
            "action": "小仓位补(<10%)", "priority": "P3",
            "reason": "正常回踩可加仓，破位则不加"
        })
    
    return plan


# ============================================================================
# 关联标的联动报告生成
# ============================================================================

def analyze_linkage(code: str, tech: Dict, valuation: Dict) -> Dict[str, Any]:
    """分析产业链/关联标的联动状态"""
    link = PORTFOLIO_LINKAGE.get(code, {})
    if not link:
        return {"status": "no_data"}
    
    # 基于当前状态判断联动方向
    trend = tech.get("trend", "")
    cur = tech.get("current", 0)
    
    linkage_signals = []
    
    # 海外锚点判断（基于近期已知信息的简单提示）
    if code == "002409":
        linkage_signals.append({
            "anchor": "费城半导体(SOX)/美光/海力士",
            "status": "⚠️ 隔夜费半-2.3%/美光-3%，外盘半导体承压",
            "impact": "negative",
            "desc": "HBM链对外盘敏感，外盘弱势下周一A股半导体承压",
        })
    elif code == "002837":
        linkage_signals.append({
            "anchor": "英伟达(NVDA)/Vertiv(VRT)",
            "status": "⚠️ 英伟达高位震荡，Vertiv近1周-8%",
            "impact": "negative",
            "desc": "海外液冷龙头回调，A股液冷映射承压",
        })
    elif code == "301217":
        linkage_signals.append({
            "anchor": "LME铜价/台光电/欣兴",
            "status": "🟡 铜价高位震荡，台股PCB本周-3%",
            "impact": "neutral_negative",
            "desc": "铜价高位压制铜箔毛利，台股PCB走弱提示行业景气度承压",
        })
    
    return {
        "main_chain": link.get("main_chain", ""),
        "core_logic": link.get("core_logic", ""),
        "upstream": link.get("upstream", []),
        "downstream": link.get("downstream", []),
        "linked_stocks": link.get("linked_stocks", []),
        "overseas_anchors": link.get("overseas_anchors", []),
        "key_catalysts": link.get("key_catalysts", []),
        "key_risks": link.get("key_risks", []),
        "linkage_signals": linkage_signals,
    }


# ============================================================================
# 综合诊断入口
# ============================================================================

def diagnose_stock(stock: Dict[str, Any]) -> Dict[str, Any]:
    """对单只持仓股执行完整五维诊断"""
    code = stock.get("code", "")
    name = stock.get("name", "")
    
    # 1. 估值
    val_snap = STOCK_VALUATION_SNAPSHOT.get(code, {})
    val_status = classify_valuation(
        val_snap.get("pe_hist_percentile"),
        val_snap.get("pb_hist_percentile"),
    )
    
    # 2. 资金流
    fund = analyze_fundflow(code)
    
    # 3. 技术面
    tech = analyze_technical(code)
    
    # 4. 产业链联动
    linkage = analyze_linkage(code, tech, val_status)
    
    # 5. 条件预案
    plan = generate_contingency_plan(stock, linkage, val_status, tech)
    
    return {
        "code": code,
        "name": name,
        "valuation": {
            "snapshot": val_snap,
            "status": val_status,
        },
        "fundflow": fund,
        "technical": tech,
        "linkage": linkage,
        "contingency_plan": plan,
        "diagnosed_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }


def diagnose_portfolio(portfolio_data: Dict[str, Any]) -> Dict[str, Any]:
    """对整个组合执行深度诊断"""
    stocks = portfolio_data.get("stocks", [])
    diag_results = []
    for s in stocks:
        diag_results.append(diagnose_stock(s))
    
    # 组合层面诊断
    total_risk_score = 0
    risk_flags = []
    for d in diag_results:
        code = d["code"]
        if d["valuation"]["status"]["level"] in ("extreme", "overvalued"):
            risk_flags.append(f"🔴 {d['name']}估值{d['valuation']['status']['label']}，建议逢高减仓")
        if d["fundflow"]["trend"] in ("massive_outflow", "outflow"):
            risk_flags.append(f"🔴 {d['name']}资金{d['fundflow']['trend_label']}，{d['fundflow']['total']:.1f}亿")
        if d["technical"].get("ma_arrange", "").startswith("空头"):
            risk_flags.append(f"🟡 {d['name']}均线{d['technical']['ma_arrange']}")
    
    return {
        "stocks_diagnosis": diag_results,
        "portfolio_flags": risk_flags,
        "diagnosed_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }


# ============================================================================
# 诊断结果HTML渲染组件（供portfolio_dashboard_pro调用）
# ============================================================================

def render_fundflow_chart(fund: Dict) -> str:
    """渲染5日资金流迷你柱状图（内联SVG）"""
    bars = fund.get("bars", [])
    if not bars:
        return ""
    
    w, h = 220, 80
    bar_w = 32
    gap = 10
    total_w = len(bars) * (bar_w + gap)
    baseline = h / 2
    
    bars_svg = []
    for i, b in enumerate(bars):
        x = i * (bar_w + gap) + 8
        bh = max(4, b["height_pct"] / 100 * (h / 2 - 8))
        if b["is_inflow"]:
            y = baseline - bh
            color = "#10b981"
        else:
            y = baseline
            color = "#ef4444"
        val_label = f"{b['value']:+.1f}"
        bars_svg.append(f'''
        <rect x="{x}" y="{y}" width="{bar_w}" height="{bh}" rx="3" fill="{color}" opacity="0.85"/>
        <text x="{x+bar_w/2}" y="{y-3 if b['is_inflow'] else y+bh+11}" text-anchor="middle" 
              fill="white" font-size="9" opacity="0.8">{val_label}</text>
        <text x="{x+bar_w/2}" y="{baseline+ (bh/2 if not b['is_inflow'] else -bh/2) }" 
              text-anchor="middle" fill="rgba(255,255,255,0.4)" font-size="9">{b['day']}</text>
        ''')
    
    return f'''
    <svg viewBox="0 0 {total_w} {h}" style="width:100%;max-width:{total_w}px;height:{h}px;">
        <line x1="0" y1="{baseline}" x2="{total_w}" y2="{baseline}" stroke="rgba(255,255,255,0.2)" stroke-width="1"/>
        {''.join(bars_svg)}
    </svg>
    '''


def render_diagnosis_html(diag: Dict) -> str:
    """渲染单只股票深度诊断模块HTML"""
    name = diag["name"]
    code = diag["code"]
    val = diag["valuation"]["status"]
    val_snap = diag["valuation"]["snapshot"]
    fund = diag["fundflow"]
    tech = diag["technical"]
    link = diag["linkage"]
    plan = diag["contingency_plan"]
    
    # 估值模块
    pe_pct = val_snap.get("pe_hist_percentile")
    pb_pct = val_snap.get("pb_hist_percentile")
    pe_str = f"PE-TTM {val_snap.get('pe_ttm','-')}（历史分位{pe_pct}%）" if pe_pct else "PE失真"
    pb_str = f"PB {val_snap.get('pb','-')}（历史分位{pb_pct}%）" if pb_pct else "PB-"
    
    # 均线HTML
    ma_html = ""
    for m in tech.get("ma_status", []):
        sign = "+" if m["above"] else ""
        ma_html += f'''
        <div style="background:rgba(255,255,255,0.08); border-radius:8px; padding:8px 10px; text-align:center; min-width:60px;">
            <div style="font-size:10px; opacity:0.6;">{m['name']}</div>
            <div style="font-size:13px; font-weight:700; color:{m['color']};">¥{m['value']:.2f}</div>
            <div style="font-size:10px; color:{m['color']};">{sign}{m['diff_pct']:+.1f}%</div>
        </div>
        '''
    
    # 支撑/压力位
    sup_html = ""
    for s in tech.get("supports", [])[:3]:
        dist = (tech["current"] - s["price"]) / tech["current"] * 100
        color = "#10b981"
        if s.get("strength") == "critical":
            color = "#ef4444"
        sup_html += f'''
        <div style="display:flex; justify-content:space-between; padding:6px 0; border-bottom:1px solid rgba(255,255,255,0.08); font-size:12px;">
            <span>¥{s['price']:.2f} <span style="opacity:0.6; margin-left:4px;">{s['type']}</span></span>
            <span style="color:{color};">-{dist:.1f}%</span>
        </div>
        '''
    
    res_html = ""
    for r in tech.get("resistances", [])[:3]:
        dist = (r["price"] - tech["current"]) / tech["current"] * 100
        res_html += f'''
        <div style="display:flex; justify-content:space-between; padding:6px 0; border-bottom:1px solid rgba(255,255,255,0.08); font-size:12px;">
            <span>¥{r['price']:.2f} <span style="opacity:0.6; margin-left:4px;">{r['type']}</span></span>
            <span style="color:#f59e0b;">+{dist:.1f}%</span>
        </div>
        '''
    
    # 关联标的
    linked_html = ""
    for ls in link.get("linked_stocks", [])[:5]:
        linked_html += f'''
        <span style="display:inline-block; background:rgba(255,255,255,0.08); border-radius:14px; 
                     padding:3px 10px; font-size:11px; margin:2px;">
            {ls['name']} <span style="opacity:0.5;">{ls['relation'][:6]}</span>
        </span>
        '''
    
    # 海外锚点信号
    anchor_html = ""
    for sig in link.get("linkage_signals", []):
        anchor_color = "#ef4444" if "negative" in sig.get("impact", "") else "#10b981"
        anchor_html += f'''
        <div style="background:rgba(255,255,255,0.05); border-radius:8px; padding:8px 10px; margin-top:6px; font-size:12px;">
            <div style="color:{anchor_color}; font-weight:600; margin-bottom:2px;">{sig['anchor']}</div>
            <div style="opacity:0.8;">{sig['status']}</div>
            <div style="opacity:0.6; font-size:11px; margin-top:2px;">{sig['desc']}</div>
        </div>
        '''
    
    # 条件预案
    def render_plan_section(items, color, label, icon):
        if not items:
            return ""
        rows = ""
        for it in items:
            pri_color = "#ef4444" if it.get("priority") == "P0" else "#f59e0b" if it.get("priority") == "P1" else "#3b82f6"
            rows += f'''
            <div style="background:rgba(255,255,255,0.04); border-radius:8px; padding:8px 10px; margin-top:6px; border-left:3px solid {pri_color};">
                <div style="display:flex; justify-content:space-between; align-items:center; font-size:12px;">
                    <span style="font-weight:600; color:{color if False else 'white'};">{it['action']}</span>
                    <span style="background:{pri_color}26; color:{pri_color}; padding:1px 6px; border-radius:4px; font-size:10px; font-weight:700;">{it.get('priority','-')}</span>
                </div>
                <div style="font-size:11px; opacity:0.75; margin-top:3px;">📌 触发条件：{it['condition']}</div>
                <div style="font-size:11px; opacity:0.55; margin-top:2px;">💡 {it['reason']}</div>
            </div>
            '''
        return f'''
        <div style="margin-top:10px;">
            <div style="font-size:12px; font-weight:700; color:{color}; margin-bottom:4px;">{icon} {label}</div>
            {rows}
        </div>
        '''
    
    plan_html = ""
    plan_html += render_plan_section(plan.get("clear_all", []), "#ef4444", "清仓/止损", "⛔")
    plan_html += render_plan_section(plan.get("reduce_1_2", []), "#f59e0b", "减仓1/2", "🔻")
    plan_html += render_plan_section(plan.get("reduce_1_3", []), "#f59e0b", "减仓1/3", "🔸")
    plan_html += render_plan_section(plan.get("hold_conditions", []), "#3b82f6", "继续持有", "💎")
    plan_html += render_plan_section(plan.get("add_position", []), "#10b981", "补仓条件（严控）", "🟢")
    
    return f'''
    <div class="card-glass p-5 mb-6 stock-diagnosis-panel" data-stock="{code}">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:16px;">
            <div style="display:flex; align-items:center; gap:10px;">
                <span style="font-size:22px;">🔬</span>
                <h3 style="font-size:18px; font-weight:800; margin:0;">{name} <span style="font-size:13px; opacity:0.6;">{code}</span> · 五维深度诊断</h3>
            </div>
            <span style="background:{val['badge_bg']}; border:1px solid {val['badge_border']}; color:{val['color']}; 
                         padding:4px 12px; border-radius:20px; font-size:12px; font-weight:700;">{val['label']}</span>
        </div>
        
        <!-- 估值锚 -->
        <div style="background:{val['badge_bg']}; border:1px solid {val['badge_border']}; border-radius:12px; padding:12px; margin-bottom:12px;">
            <div style="font-size:13px; font-weight:700; color:{val['color']}; margin-bottom:6px;">💰 估值锚</div>
            <div style="display:flex; flex-wrap:wrap; gap:8px; font-size:12px; margin-bottom:6px;">
                <span style="background:rgba(255,255,255,0.08); padding:4px 10px; border-radius:8px;">{pe_str}</span>
                <span style="background:rgba(255,255,255,0.08); padding:4px 10px; border-radius:8px;">{pb_str}</span>
                <span style="background:rgba(255,255,255,0.08); padding:4px 10px; border-radius:8px;">市值 {val_snap.get('market_cap','-')}亿</span>
            </div>
            <div style="font-size:11px; opacity:0.7;">{val['desc']} · {val_snap.get('note','')}</div>
        </div>
        
        <!-- 资金流向 -->
        <div style="background:rgba(255,255,255,0.04); border:1px solid rgba(255,255,255,0.08); border-radius:12px; padding:12px; margin-bottom:12px;">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
                <div style="font-size:13px; font-weight:700;">💸 近5日主力资金流向</div>
                <span style="color:{fund['trend_color']}; font-weight:700; font-size:12px;">{fund['trend_label']} 累计{fund['total']:+.2f}亿</span>
            </div>
            {render_fundflow_chart(fund)}
            <div style="font-size:11px; opacity:0.65; margin-top:6px;">{fund.get('note','')}</div>
        </div>
        
        <!-- 技术面/均线/支撑压力 -->
        <div style="background:rgba(255,255,255,0.04); border:1px solid rgba(255,255,255,0.08); border-radius:12px; padding:12px; margin-bottom:12px;">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
                <div style="font-size:13px; font-weight:700;">📈 技术面研判</div>
                <span style="color:{tech.get('ma_arrange_color','white')}; font-weight:700; font-size:12px;">{tech.get('ma_arrange','-')}</span>
            </div>
            <div style="display:flex; gap:6px; flex-wrap:wrap; margin-bottom:10px;">{ma_html}</div>
            <div style="font-size:11px; opacity:0.7; margin-bottom:10px;">📊 {tech.get('pattern','')}</div>
            <div style="display:grid; grid-template-columns:1fr 1fr; gap:12px;">
                <div>
                    <div style="font-size:11px; color:#10b981; font-weight:700; margin-bottom:4px;">▼ 支撑位</div>
                    {sup_html}
                </div>
                <div>
                    <div style="font-size:11px; color:#f59e0b; font-weight:700; margin-bottom:4px;">▲ 压力位</div>
                    {res_html}
                </div>
            </div>
        </div>
        
        <!-- 产业链联动 -->
        <div style="background:rgba(255,255,255,0.04); border:1px solid rgba(255,255,255,0.08); border-radius:12px; padding:12px; margin-bottom:12px;">
            <div style="font-size:13px; font-weight:700; margin-bottom:8px;">🔗 {link.get('main_chain','')} · 产业链联动</div>
            <div style="font-size:11px; opacity:0.75; margin-bottom:8px;">{link.get('core_logic','')}</div>
            <div style="margin-bottom:8px;">{linked_html}</div>
            {anchor_html}
            <div style="margin-top:8px; font-size:11px; opacity:0.7;">
                <span style="color:#10b981;">●催化：</span>{' / '.join(link.get('key_catalysts',[])[:3])}
            </div>
            <div style="font-size:11px; opacity:0.7;">
                <span style="color:#ef4444;">●风险：</span>{' / '.join(link.get('key_risks',[])[:3])}
            </div>
        </div>
        
        <!-- 条件预案 -->
        <div style="background:rgba(255,255,255,0.04); border:1px solid rgba(255,255,255,0.08); border-radius:12px; padding:12px;">
            <div style="font-size:13px; font-weight:700; margin-bottom:4px;">🎯 条件化操作预案（按优先级排序）</div>
            <div style="font-size:10px; opacity:0.5; margin-bottom:6px;">P0=立刻执行/P1=当日/P2=观察/P3=严控仓位</div>
            {plan_html}
        </div>
    </div>
    '''


if __name__ == '__main__':
    # 自测
    import sys
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    data_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data', 'portfolio.json')
    with open(data_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    result = diagnose_portfolio(data)
    out_path = '/tmp/stock_diagnosis_test.json'
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2, default=str)
    print(f"诊断完成，共{len(result['stocks_diagnosis'])}只股票，风险标记{len(result['portfolio_flags'])}条")
    print(f"结果已保存至 {out_path}")
    for d in result['stocks_diagnosis']:
        print(f"  - {d['name']}: 估值={d['valuation']['status']['label']}, 资金={d['fundflow']['trend_label']}, {d['technical'].get('ma_arrange','-')}")
