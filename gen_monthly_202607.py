#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
2026年7月月度报告生成器
使用V3.0 MonthlyReportGenerator生成
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from v3.generators.monthly import MonthlyReportGenerator
from v3.components.data import DataCard
from v3.components.layout import Section

# 生成器初始化
gen = MonthlyReportGenerator(
    date_str="2026年7月",
    month="2026年7月",
    subtitle="A股结构性深度调整 · 科技重挫 · 防御占优"
)

# ========== 1. 月度核心总结 ==========
month_summary = """
7月A股经历了一轮<strong>剧烈的结构性调整</strong>，呈现出典型的"大强小弱、价值占优、成长重挫"格局。
上证指数月跌6.4%回吐年内全部涨幅，科创50暴跌25.9%创历史最大单月跌幅，创业板指跌23%创逾十年最大单月跌幅。
<strong>科技成长板块遭遇系统性抛售</strong>：半导体跌36%、CPO跌30%、存储芯片跌32%、液冷板块回撤超50%；
<strong>防御板块逆势走强</strong>：煤炭涨14%、石油石化涨13%、银行涨12%、食品饮料涨11%。
驱动因素：海外地缘冲突（美以伊冲突推升油价）、全球科技股共振回调（费城半导体跌20%、韩股跌22%）、
融资盘强平（单月流出超4100亿）、长鑫科技上市虹吸效应。
政策托底信号明确：7月政治局会议提出"提升资本市场韧性和信心"，两大国资合计增持超600亿元。
展望8月：科技板块短期仍有调整压力，但估值已大幅回落，政治局会议政策利好逐步释放，
建议关注AI算力产业链中报业绩验证、存储芯片周期反转、机器人量产催化等结构性机会。
"""
gen.add_month_summary(month_summary.strip())

# ========== 2. 指数表现（用DataCard+Section直接构建，绕过StatCard bug） ==========
indices = [
    {"name": "上证指数", "value": "3832.26", "trend": "-6.40%", "trend_up": False, "icon": "trending_down"},
    {"name": "深证成指", "value": "13578.93", "trend": "-16.21%", "trend_up": False, "icon": "trending_down"},
    {"name": "创业板指", "value": "3343.96", "trend": "-23.00%", "trend_up": False, "icon": "trending_down"},
    {"name": "科创50", "value": "1635.96", "trend": "-25.90%", "trend_up": False, "icon": "trending_down"},
]

cards_html = '<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 12px;">'
for idx in indices:
    trend_color = "#10b981" if idx["trend_up"] else "#ef4444"
    trend_icon = "↑" if idx["trend_up"] else "↓"
    cards_html += f'''
    <div style="background: rgba(255,255,255,0.05); backdrop-filter: blur(10px); 
                border: 1px solid rgba(255,255,255,0.08); border-radius: 14px; padding: 16px;">
        <div style="font-size: 13px; color: #94a3b8; margin-bottom: 6px;">{idx["name"]}</div>
        <div style="font-size: 22px; font-weight: 700; color: #f1f5f9;">{idx["value"]}</div>
        <div style="display: flex; align-items: center; color: {trend_color}; 
                    font-size: 13px; font-weight: 600; margin-top: 6px;">
            <span style="margin-right: 4px;">{trend_icon}</span>
            <span>{idx["trend"]}</span>
        </div>
    </div>'''
cards_html += '</div>'

index_section = Section(title="📊 指数表现", content=cards_html, icon="chart")
gen._components.append(index_section)

# ========== 3. 行业板块回顾 ==========
sectors_top = [
    {"name": "煤炭", "change": "+14.29%", "up": True, "comment": "地缘冲突推升能源价格，高股息防御属性凸显，中煤能源、中国神华领涨"},
    {"name": "石油石化", "change": "+12.63%", "up": True, "comment": "美伊冲突加剧霍尔木兹海峡风险，国际油价单月涨24%突破90美元"},
    {"name": "银行", "change": "+11.57%", "up": True, "comment": "资金避险涌入大金融，高股息+低估值双重支撑，国有大行领涨"},
    {"name": "食品饮料", "change": "+11%+", "up": True, "comment": "白酒板块反弹，消费复苏预期+防御属性获资金青睐"},
    {"name": "贵金属", "change": "+25.84%", "up": True, "comment": "地缘冲突+降息预期双重催化，黄金价格逼近4000美元/盎司"},
]
sectors_bottom = [
    {"name": "电子", "change": "-34.72%", "up": False, "comment": "AI硬件估值体系重估，全球半导体板块共振回调，融资盘集中爆仓"},
    {"name": "通信", "change": "-31.90%", "up": False, "comment": "CPO概念退潮，光模块龙头高位回撤超50%，英伟达交易模式遭质疑"},
    {"name": "半导体", "change": "-36.45%", "up": False, "comment": "产品与设备双双暴跌，长鑫上市虹吸效应+海外科技股回调双重打击"},
    {"name": "存储芯片", "change": "-31.89%", "up": False, "comment": "HBM概念降温，费城半导体跌20%传导，国产存储龙头高位腰斩"},
    {"name": "建筑材料", "change": "-27.9%", "up": False, "comment": "地产链持续低迷，需求不振预期拖累建材板块"},
]

# 领涨板块
top_sectors_html = '<div style="margin-bottom: 16px;"><div style="font-size: 14px; font-weight: 600; color: #10b981; margin-bottom: 8px;">📈 领涨板块 TOP5</div>'
for s in sectors_top:
    top_sectors_html += f'''
    <div style="background: rgba(16,185,129,0.08); border: 1px solid rgba(16,185,129,0.2);
               border-radius: 10px; padding: 10px 14px; margin-bottom: 6px;">
        <div style="display: flex; align-items: center;">
            <span style="font-size: 13px; font-weight: 600; color: #f1f5f9; flex: 1;">{s["name"]}</span>
            <span style="font-size: 13px; font-weight: 600; color: #10b981;">{s["change"]}</span>
        </div>
        <div style="font-size: 11px; color: #94a3b8; line-height: 1.4; margin-top: 4px;">{s["comment"]}</div>
    </div>'''
top_sectors_html += '</div>'

# 领跌板块
bottom_sectors_html = '<div><div style="font-size: 14px; font-weight: 600; color: #ef4444; margin-bottom: 8px;">📉 领跌板块 TOP5</div>'
for s in sectors_bottom:
    bottom_sectors_html += f'''
    <div style="background: rgba(239,68,68,0.08); border: 1px solid rgba(239,68,68,0.2);
               border-radius: 10px; padding: 10px 14px; margin-bottom: 6px;">
        <div style="display: flex; align-items: center;">
            <span style="font-size: 13px; font-weight: 600; color: #f1f5f9; flex: 1;">{s["name"]}</span>
            <span style="font-size: 13px; font-weight: 600; color: #ef4444;">{s["change"]}</span>
        </div>
        <div style="font-size: 11px; color: #94a3b8; line-height: 1.4; margin-top: 4px;">{s["comment"]}</div>
    </div>'''
bottom_sectors_html += '</div>'

sector_section = Section(
    title="🏢 行业板块回顾",
    content=top_sectors_html + bottom_sectors_html,
    icon="building"
)
gen._components.append(sector_section)

# ========== 4. 大类资产表现 ==========
assets = [
    {"name": "国际原油(WTI)", "change": "+23.95%", "up": True, "note": "美伊冲突+OPEC+减产"},
    {"name": "伦敦黄金", "change": "+0.94%", "up": True, "note": "避险需求支撑，逼近4000美元"},
    {"name": "伦敦铜", "change": "+3.16%", "up": True, "note": "美元走弱+需求预期"},
    {"name": "恒生指数", "change": "+13.13%", "up": True, "note": "政策利好+估值修复"},
    {"name": "纳斯达克", "change": "-3.20%", "up": False, "note": "AI交易模式遭质疑"},
    {"name": "费城半导体", "change": "-20.61%", "up": False, "note": "全球半导体估值重估"},
    {"name": "韩国综合指数", "change": "-22.19%", "up": False, "note": "半导体权重股暴跌"},
    {"name": "日经225", "change": "-8.14%", "up": False, "note": "科技股回调拖累"},
]
gen.add_asset_allocation(assets)

# ========== 5. 持仓月度表现 ==========
holdings = [
    {
        "name": "英维克 (002837)",
        "start": "79.56元",
        "end": "47.45元",
        "change": "-40.36%",
        "up": False,
        "comment": "液冷总龙头深度回调，从6月高点93.52元回撤近50%。7月20日跌停开启加速下跌，主力资金连续20日净流出累计约24亿。液冷板块随AI硬件系统性崩盘，一季度业绩不及预期（净利降82%），高估值泡沫被刺破。严格执行止损纪律，任何反弹都是离场机会。"
    },
    {
        "name": "铜冠铜箔 (301217)",
        "start": "165.07元",
        "end": "82.62元",
        "change": "-49.95%",
        "up": False,
        "comment": "铜箔板块重灾区，从202元高点腰斩。存储PCB产业链整体回调，虽然一季度业绩暴增2138%，但高增长预期已充分定价。7月30日跌8.57%探底77.28元，7月最后一日反弹3.91%。85元为关键支撑位，跌破则趋势完全破位。"
    },
    {
        "name": "雅克科技 (002409)",
        "start": "224.50元",
        "end": "133.80元",
        "change": "-40.40%",
        "up": False,
        "comment": "HBM前驱体龙头剧烈震荡，月初最高236元→中旬最低143元→下旬反包至169元→月末再跌回134元。7月29-31日连续三日跌幅偏离值超20%触发异常波动公告。HBM长期逻辑未变但短期估值偏高，中报业绩验证是关键催化剂。跌破150元需大幅减仓。"
    },
    {
        "name": "*ST建艺 (002789)",
        "start": "11.55元",
        "end": "9.57元",
        "change": "-17.14%",
        "up": False,
        "comment": "ST退市风险股持续阴跌，新增诉讼仲裁累计超4400万占净资产21%。一季度巨亏5300万，负债率94%，债务问题严峻。7月最后一日涨8.5%至9.57元，但退市风险未消除。最高优先级清仓止损，绝不恋战。"
    },
]

holdings_html = '<div style="display: flex; flex-direction: column; gap: 12px;">'
for h in holdings:
    change_color = "#10b981" if h["up"] else "#ef4444"
    holdings_html += f'''
    <div style="background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.08);
               border-radius: 12px; padding: 16px;">
        <div style="display: flex; align-items: center; margin-bottom: 8px;">
            <span style="font-size: 15px; font-weight: 700; color: #f1f5f9; flex: 1;">{h["name"]}</span>
            <span style="font-size: 16px; font-weight: 700; color: {change_color};">{h["change"]}</span>
        </div>
        <div style="display: flex; gap: 16px; margin-bottom: 8px; font-size: 12px; color: #94a3b8;">
            <span>月初: {h["start"]}</span>
            <span>月末: {h["end"]}</span>
        </div>
        <div style="font-size: 12px; color: #cbd5e1; line-height: 1.6;">{h["comment"]}</div>
    </div>'''
holdings_html += '</div>'

holdings_section = Section(
    title="💼 持仓月度复盘",
    content=holdings_html,
    icon="briefcase",
    variant="highlight"
)
gen._components.append(holdings_section)

# ========== 6. 月度重大事件 ==========
events_html = '''
<div style="display: flex; flex-direction: column; gap: 10px;">
    <div style="background: rgba(99,102,241,0.1); border-left: 3px solid #6366f1; padding: 12px 16px; border-radius: 0 8px 8px 0;">
        <div style="font-size: 13px; font-weight: 600; color: #a5b4fc; margin-bottom: 4px;">7月30日 · 中央政治局会议</div>
        <div style="font-size: 12px; color: #cbd5e1; line-height: 1.6;">提出"提升资本市场韧性和信心""稳定房地产市场"，明确"实施好更加积极的财政政策和适度宽松的货币政策"。新增"深化资本市场投融资综合改革"表述，释放稳预期强信号。</div>
    </div>
    <div style="background: rgba(99,102,241,0.1); border-left: 3px solid #6366f1; padding: 12px 16px; border-radius: 0 8px 8px 0;">
        <div style="font-size: 13px; font-weight: 600; color: #a5b4fc; margin-bottom: 4px;">7月19日 · 国资密集增持</div>
        <div style="font-size: 12px; color: #cbd5e1; line-height: 1.6;">中国国新、中国诚通两大国有资本运营公司合计投入超600亿元增持A股，明确表态坚定看好中国资本市场发展前景，政策底信号明确。</div>
    </div>
    <div style="background: rgba(239,68,68,0.1); border-left: 3px solid #ef4444; padding: 12px 16px; border-radius: 0 8px 8px 0;">
        <div style="font-size: 13px; font-weight: 600; color: #fca5a5; margin-bottom: 4px;">7月中下旬 · 全球科技股暴跌</div>
        <div style="font-size: 12px; color: #cbd5e1; line-height: 1.6;">费城半导体指数月跌20.6%，韩国综合指数跌22.2%，日经225跌8.1%。导火索是英伟达7500亿美元AI交易引发"循环融资"模式质疑，全球AI硬件估值体系重估。</div>
    </div>
    <div style="background: rgba(245,158,11,0.1); border-left: 3px solid #f59e0b; padding: 12px 16px; border-radius: 0 8px 8px 0;">
        <div style="font-size: 13px; font-weight: 600; color: #fcd34d; margin-bottom: 4px;">7月 · 美以伊冲突升级</div>
        <div style="font-size: 12px; color: #cbd5e1; line-height: 1.6;">霍尔木兹海峡运输风险升温，国际油价单月大涨24%突破90美元，推升美国通胀预期，美联储维持鹰派立场，十年期美债收益率冲击年内次高。</div>
    </div>
    <div style="background: rgba(16,185,129,0.1); border-left: 3px solid #10b981; padding: 12px 16px; border-radius: 0 8px 8px 0;">
        <div style="font-size: 13px; font-weight: 600; color: #6ee7b7; margin-bottom: 4px;">7月 · 长鑫科技上市</div>
        <div style="font-size: 12px; color: #cbd5e1; line-height: 1.6;">国产存储龙头长鑫科技登陆科创板，首日涨465%收49元，市值3.28万亿登顶A股。MSCI快速纳入（8/10生效），对存量科技股形成资金虹吸效应。</div>
    </div>
    <div style="background: rgba(99,102,241,0.1); border-left: 3px solid #6366f1; padding: 12px 16px; border-radius: 0 8px 8px 0;">
        <div style="font-size: 13px; font-weight: 600; color: #a5b4fc; margin-bottom: 4px;">7月31日 · 7月PMI数据</div>
        <div style="font-size: 12px; color: #cbd5e1; line-height: 1.6;">制造业PMI降至49.2%（前值50.3%），非制造业PMI 49.0%，双双跌破荣枯线。高技术制造业PMI 53.3%仍保持扩张，新旧动能转换持续。</div>
    </div>
    <div style="background: rgba(139,92,246,0.1); border-left: 3px solid #8b5cf6; padding: 12px 16px; border-radius: 0 8px 8px 0;">
        <div style="font-size: 13px; font-weight: 600; color: #c4b5fd; margin-bottom: 4px;">7月中旬 · 世界人工智能大会</div>
        <div style="font-size: 12px; color: #cbd5e1; line-height: 1.6;">习近平提出"人工智能是世界经济增长的新引擎和新旧动能转换的加速器"。上半年集成电路产量2798亿块增23.1%，工业机器人增28%，AI产业持续高景气。</div>
    </div>
</div>
'''

events_section = Section(
    title="📰 月度重大事件",
    content=events_html,
    icon="newspaper"
)
gen._components.append(events_section)

# ========== 7. 资金面分析 ==========
fund_html = '''
<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px;">
    <div style="background: rgba(255,255,255,0.05); border-radius: 12px; padding: 14px;">
        <div style="font-size: 13px; color: #94a3b8; margin-bottom: 4px;">月日均成交额</div>
        <div style="font-size: 20px; font-weight: 700; color: #f1f5f9;">2.70万亿</div>
        <div style="font-size: 11px; color: #9ca3af; margin-top: 2px;">较6月3.13万亿明显萎缩</div>
    </div>
    <div style="background: rgba(255,255,255,0.05); border-radius: 12px; padding: 14px;">
        <div style="font-size: 13px; color: #94a3b8; margin-bottom: 4px;">融资余额变化</div>
        <div style="font-size: 20px; font-weight: 700; color: #ef4444;">-4126亿</div>
        <div style="font-size: 11px; color: #9ca3af; margin-top: 2px;">单月锐减近14%，杠杆资金强平</div>
    </div>
    <div style="background: rgba(255,255,255,0.05); border-radius: 12px; padding: 14px;">
        <div style="font-size: 13px; color: #94a3b8; margin-bottom: 4px;">股票ETF净流入</div>
        <div style="font-size: 20px; font-weight: 700; color: #10b981;">+5023亿</div>
        <div style="font-size: 11px; color: #9ca3af; margin-top: 2px;">年内首次月度净申购，创历史新高</div>
    </div>
    <div style="background: rgba(255,255,255,0.05); border-radius: 12px; padding: 14px;">
        <div style="font-size: 13px; color: #94a3b8; margin-bottom: 4px;">主力资金流出</div>
        <div style="font-size: 20px; font-weight: 700; color: #ef4444;">-11001亿</div>
        <div style="font-size: 11px; color: #9ca3af; margin-top: 2px;">全市场主力资金大幅出逃</div>
    </div>
</div>
<div style="margin-top: 12px; font-size: 12px; color: #94a3b8; line-height: 1.6;">
    <strong style="color: #cbd5e1;">资金面特征：</strong>7月呈现典型的"杠杆资金出逃+ETF逆势抄底"背离格局。融资盘单月暴减4100亿是市场急跌的重要推手，
    而宽基ETF获得5000亿净流入创历史新高，显示中长期机构资金在下跌中逆势布局。银行板块获主力资金+632亿净流入居首，
    电子行业融资净卖出1493亿元居首，但半导体板块主力资金口径获+340亿净流入——主力与杠杆资金在科技板块操作方向完全相反。
</div>
'''

fund_section = Section(
    title="💰 资金面全景",
    content=fund_html,
    icon="dollar-sign"
)
gen._components.append(fund_section)

# ========== 8. 月度投资策略 ==========
strategy_text = """
<strong>7月策略回顾与反思：</strong><br>
7月科技板块遭遇系统性估值重估，持仓4只标的全线深度回调，组合回撤幅度远超预期。
核心教训：<strong>①</strong>高位科技股风险敞口过大，缺乏防御板块对冲；
<strong>②</strong>止损纪律执行不坚决，英维克破止损后未及时清仓导致亏损扩大；
<strong>③</strong>对全球科技股共振回调风险预判不足，对地缘冲突传导效应估计偏低；
<strong>④</strong>ST股风险敞口未及时关闭，*ST建艺浮亏持续扩大。
<br><br>
<strong>8月操作策略：</strong><br>
1. <strong>仓位控制：</strong>整体仓位控制在3成以内，现金为王，等待市场明确企稳信号（缩量+止跌+量价配合反弹）<br>
2. <strong>持仓处理：</strong>英维克/铜冠铜箔趁反弹坚决减仓，雅克科技跌破150元减至底仓，*ST建艺立即清仓<br>
3. <strong>防御配置：</strong>适度增加高股息红利板块（银行/煤炭/公用事业）作为组合压舱石，对冲科技波动风险<br>
4. <strong>重点跟踪：</strong>中报业绩验证（尤其是AI算力产业链）、美联储9月降息预期、政治局会议政策落地进展<br>
5. <strong>关注机会：</strong>存储芯片周期反转（HBM+DDR5）、人形机器人量产催化、国产半导体设备国产化加速
"""
gen.add_investment_strategy(strategy_text.strip())

# ========== 9. 下月展望 ==========
outlook_text = """
<strong>8月市场展望：震荡筑底，结构分化</strong><br><br>
<strong>📈 乐观情景（概率30%）：</strong>政治局会议政策加速落地，8月LPR降息+财政增量政策出台，市场情绪快速修复，
科创50引领反弹，AI算力+存储+HBM主线回归，指数有望收复7月失地的50%。<br><br>
<strong>📊 基准情景（概率50%）：</strong>政策利好逐步消化但增量有限，市场震荡筑底，
科技板块在当前位置反复磨底，防御板块继续占优，指数在当前区间震荡整理。
中报业绩成为个股分化核心变量，业绩验证的标的率先企稳反弹。<br><br>
<strong>📉 悲观情景（概率20%）：</strong>地缘冲突进一步升级，油价破百推升全球通胀，
美联储降息预期推迟，全球科技股继续下行，A股科技板块再下一个台阶，
沪指考验3600点支撑。需警惕融资盘二次爆仓风险。<br><br>
<strong>🔑 8月关键变量：</strong>
① 中报业绩披露（8月中下旬密集期）；
② 美联储9月降息预期变化；
③ 政治局会议配套政策落地节奏；
④ 中美关系与地缘冲突演变；
⑤ 长鑫科技纳入MSCI后的资金流向。
"""
gen.add_next_month_outlook(outlook_text.strip())

# ========== 10. 风险提示 ==========
risks = [
    "地缘冲突升级风险：美以伊冲突可能进一步扩大，推升油价和全球通胀预期",
    "美联储政策转向风险：若通胀反弹，降息预期推迟将压制科技股估值",
    "中报业绩不及预期风险：AI算力产业链高增长能否兑现存在不确定性",
    "融资盘强平风险：若市场继续下跌，杠杆资金平仓可能引发踩踏",
    "退市风险：*ST建艺退市风险未消除，持仓需立即处理",
    "外部冲击风险：全球科技股估值重估向A股传导的溢出效应",
]
gen.add_risk_warning(risks)

# ========== 生成并保存 ==========
output_dir = "docs/monthly"
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, "202607_月度报告.html")

html = gen.generate()
with open(output_path, "w", encoding="utf-8") as f:
    f.write(html)

print(f"✅ 月度报告生成完成: {output_path}")
print(f"   文件大小: {os.path.getsize(output_path)/1024:.1f} KB")

# 验证报告
issues = gen.validate()
if issues:
    print(f"   验证问题: {issues}")
else:
    print(f"   验证通过 ✓")
