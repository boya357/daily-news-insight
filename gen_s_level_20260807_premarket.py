#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S级催化扫描 - 2026年8月7日 盘前
存储板块全球重挫+英伟达缩减Rubin Ultra显存+HBM短缺加剧
"""
import sys, os
sys.path.insert(0, '/root/daily-news-insight/v3')
os.chdir('/root/daily-news-insight')

from v3.generators.s_level_catalyst import SLevelCatalystGenerator

gen = SLevelCatalystGenerator(
    date_str="20260807",
    catalyst_title="存储板块全球重挫+英伟达缩减Rubin显存+HBM短缺加剧 科技板块结构性分化",
    subtitle="2026.08.07 · 盘前S级催化"
)

# ========== 1. 催化概述 ==========
gen.add_catalyst_overview(
    overview=(
        "隔夜全球科技板块呈现剧烈结构性分化：美股存储链重挫（西部数据-13%、闪迪-6.8%、"
        "SK海力士-5%、美光-1.3%），费城半导体指数从跌3%深V反转收涨约1.4%；英伟达考虑"
        "缩减Rubin Ultra显存应对HBM短缺，马斯克定性\"内存是AI最大瓶颈\"；韩国股市前一交易日"
        "暴跌4.6%后今日盘前反弹约1%。核心逻辑：AI算力供给侧瓶颈从GPU转向HBM存储，"
        "存储行业内部分化加剧（NAND过剩vs HBM紧缺），A股半导体材料/先进封装主线有望"
        "延续结构性机会。今晚美国非农数据将决定全球风险偏好走向。"
    ),
    importance="高"
)

# ========== 2. 催化详情 ==========
gen.add_catalyst_details(
    background=(
        "8月以来全球科技股经历剧烈波动，存储板块成为多空博弈的核心战场。"
        "7月费城半导体指数暴跌21%创2008年以来最差单月，8月初迎来超跌反弹。"
        "闪迪年内涨幅达469%后估值已充分反映乐观预期，一旦业绩指引不及\"whisper number\""
        "便引发剧烈回调。AI算力产业链正从GPU瓶颈转向HBM存储瓶颈，英伟达被迫考虑"
        "缩减下一代GPU显存规格，供给侧约束成为新的定价逻辑。"
    ),
    trigger=(
        "① 闪迪/西部数据Q4财报超预期但Q1指引不及乐观预期，存储链集体重挫，西部数据-13%、闪迪-6.8%；<br>"
        "② 英伟达考虑缩减Rubin Ultra显存规模，HBM高端芯片供不应求成AI算力核心瓶颈；<br>"
        "③ 马斯克：\"AI热潮最大瓶颈是内存，存储供给年增约20%，但需求增速高达200%+\"；<br>"
        "④ 台积电因DRAM短缺堆积10亿美元苹果A20处理器无法完成封装；<br>"
        "⑤ 韩国KOSPI前一交易日暴跌4.6%，SK海力士-10.37%、三星-6.3%，今日盘前反弹1%+；<br>"
        "⑥ 费城半导体深V反转：开盘跌1.5%后转涨，收涨约1.4%，多空博弈激烈；<br>"
        "⑦ 葛卫东夫妇增持兆易创新合计4.66亿元，知名投资人逆势加仓存储芯片。"
    )
)

# ========== 3. 隔夜外盘扫描模块 ==========
overnight_html = """
<div class="grid grid-cols-2 md:grid-cols-4 gap-3 mb-4">
    <div style="background: linear-gradient(135deg, rgba(34,197,94,0.15) 0%, rgba(22,163,74,0.08) 100%); 
                border-radius: 12px; padding: 16px; border: 1px solid rgba(34,197,94,0.3);">
        <div style="font-size: 12px; color: #86efac; margin-bottom: 6px;">费城半导体SOX</div>
        <div style="font-size: 22px; font-weight: 800; color: #4ade80;">+1.35%</div>
        <div style="font-size: 11px; color: #6ee7b7; margin-top: 4px;">深V反转 收12171点</div>
    </div>
    <div style="background: linear-gradient(135deg, rgba(239,68,68,0.15) 0%, rgba(220,38,38,0.08) 100%); 
                border-radius: 12px; padding: 16px; border: 1px solid rgba(239,68,68,0.3);">
        <div style="font-size: 12px; color: #fca5a5; margin-bottom: 6px;">纳斯达克</div>
        <div style="font-size: 22px; font-weight: 800; color: #f87171;">-0.06%</div>
        <div style="font-size: 11px; color: #fca5a5; margin-top: 4px;">报26348点 几近平收</div>
    </div>
    <div style="background: linear-gradient(135deg, rgba(239,68,68,0.15) 0%, rgba(220,38,38,0.08) 100%); 
                border-radius: 12px; padding: 16px; border: 1px solid rgba(239,68,68,0.3);">
        <div style="font-size: 12px; color: #fca5a5; margin-bottom: 6px;">道琼斯</div>
        <div style="font-size: 22px; font-weight: 800; color: #f87171;">-0.85%</div>
        <div style="font-size: 11px; color: #fca5a5; margin-top: 4px;">终结五连涨 跌400点</div>
    </div>
    <div style="background: linear-gradient(135deg, rgba(245,158,11,0.15) 0%, rgba(217,119,6,0.08) 100%); 
                border-radius: 12px; padding: 16px; border: 1px solid rgba(245,158,11,0.3);">
        <div style="font-size: 12px; color: #fcd34d; margin-bottom: 6px;">布伦特原油</div>
        <div style="font-size: 22px; font-weight: 800; color: #fbbf24;">+4.13%</div>
        <div style="font-size: 11px; color: #fcd34d; margin-top: 4px;">报82.73美元/桶</div>
    </div>
</div>

<div class="grid grid-cols-2 md:grid-cols-4 gap-3 mb-4">
    <div style="background: rgba(239,68,68,0.08); border-radius: 10px; padding: 12px; border: 1px solid rgba(239,68,68,0.2);">
        <div style="font-size: 12px; color: #fca5a5;">西部数据 WDC</div>
        <div style="font-size: 18px; font-weight: 700; color: #f87171;">-13.03%</div>
    </div>
    <div style="background: rgba(239,68,68,0.08); border-radius: 10px; padding: 12px; border: 1px solid rgba(239,68,68,0.2);">
        <div style="font-size: 12px; color: #fca5a5;">闪迪 SNDK</div>
        <div style="font-size: 18px; font-weight: 700; color: #f87171;">-6.81%</div>
        <div style="font-size: 10px; color: #fca5a5;">指引不及高预期</div>
    </div>
    <div style="background: rgba(239,68,68,0.08); border-radius: 10px; padding: 12px; border: 1px solid rgba(239,68,68,0.2);">
        <div style="font-size: 12px; color: #fca5a5;">SK海力士 ADR</div>
        <div style="font-size: 18px; font-weight: 700; color: #f87171;">-4.97%</div>
    </div>
    <div style="background: rgba(239,68,68,0.08); border-radius: 10px; padding: 12px; border: 1px solid rgba(239,68,68,0.2);">
        <div style="font-size: 12px; color: #fca5a5;">美光科技 MU</div>
        <div style="font-size: 18px; font-weight: 700; color: #f87171;">-1.31%</div>
        <div style="font-size: 10px; color: #86efac;">盘中一度翻红涨2%</div>
    </div>
</div>

<div class="grid grid-cols-2 md:grid-cols-4 gap-3 mb-4">
    <div style="background: rgba(34,197,94,0.08); border-radius: 10px; padding: 12px; border: 1px solid rgba(34,197,94,0.2);">
        <div style="font-size: 12px; color: #86efac;">英伟达 NVDA</div>
        <div style="font-size: 18px; font-weight: 700; color: #4ade80;">-0.10%</div>
        <div style="font-size: 10px; color: #fbbf24;">盘中创2个月新高</div>
    </div>
    <div style="background: rgba(34,197,94,0.08); border-radius: 10px; padding: 12px; border: 1px solid rgba(34,197,94,0.2);">
        <div style="font-size: 12px; color: #86efac;">AMD</div>
        <div style="font-size: 18px; font-weight: 700; color: #4ade80;">+1.50%</div>
        <div style="font-size: 10px; color: #fca5a5;">前日大跌7%后修复</div>
    </div>
    <div style="background: rgba(34,197,94,0.08); border-radius: 10px; padding: 12px; border: 1px solid rgba(34,197,94,0.2);">
        <div style="font-size: 12px; color: #86efac;">阿斯麦 ASML</div>
        <div style="font-size: 18px; font-weight: 700; color: #4ade80;">+1.56%</div>
    </div>
    <div style="background: rgba(34,197,94,0.08); border-radius: 10px; padding: 12px; border: 1px solid rgba(34,197,94,0.2);">
        <div style="font-size: 12px; color: #86efac;">台积电 TSM</div>
        <div style="font-size: 18px; font-weight: 700; color: #4ade80;">+0.98%</div>
    </div>
</div>

<div class="grid grid-cols-2 md:grid-cols-4 gap-3 mb-4">
    <div style="background: rgba(34,197,94,0.08); border-radius: 10px; padding: 12px; border: 1px solid rgba(34,197,94,0.2);">
        <div style="font-size: 12px; color: #86efac;">微软 MSFT</div>
        <div style="font-size: 18px; font-weight: 700; color: #4ade80;">+2.54%</div>
        <div style="font-size: 10px; color: #86efac;">创去年11月新高</div>
    </div>
    <div style="background: rgba(34,197,94,0.08); border-radius: 10px; padding: 12px; border: 1px solid rgba(34,197,94,0.2);">
        <div style="font-size: 12px; color: #86efac;">ARM</div>
        <div style="font-size: 18px; font-weight: 700; color: #4ade80;">+4.41%</div>
    </div>
    <div style="background: rgba(239,68,68,0.08); border-radius: 10px; padding: 12px; border: 1px solid rgba(239,68,68,0.2);">
        <div style="font-size: 12px; color: #fca5a5;">韩国KOSPI</div>
        <div style="font-size: 18px; font-weight: 700; color: #f87171;">-4.60%</div>
        <div style="font-size: 10px; color: #fca5a5;">8月6日暴跌 今日盘前反弹</div>
    </div>
    <div style="background: rgba(34,197,94,0.08); border-radius: 10px; padding: 12px; border: 1px solid rgba(34,197,94,0.2);">
        <div style="font-size: 12px; color: #86efac;">SpaceX</div>
        <div style="font-size: 18px; font-weight: 700; color: #4ade80;">+6.14%</div>
        <div style="font-size: 10px; color: #86efac;">解禁后反弹</div>
    </div>
</div>

<div style="background: rgba(59,130,246,0.08); border-radius: 10px; padding: 14px; border-left: 3px solid #3b82f6;">
    <div style="font-size: 13px; color: #93c5fd; font-weight: 600; margin-bottom: 6px;">📰 隔夜重要产业消息</div>
    <ul style="font-size: 12px; color: #cbd5e1; line-height: 1.9; margin: 0; padding-left: 18px;">
        <li><b>英伟达考虑缩减Rubin Ultra显存</b>：测试至少三个版本，部分显存低于原规格，HBM高端芯片供不应求成AI算力核心瓶颈（来源：财联社/华尔街见闻）</li>
        <li><b>马斯克定性内存瓶颈</b>："AI热潮最大瓶颈是内存，存储供给年增约20%，需求增速高达200%+"，台积电10亿美元A20芯片因DRAM短缺无法封装（来源：财联社）</li>
        <li><b>闪迪/西部数据财报指引不及高预期</b>：闪迪Q4营收89.7亿美元（+372%）超预期，但Q1指引中值105.5亿低于华尔街预期108亿；西部数据Q4营收37.5亿（+44%）（来源：澎湃新闻/中新经纬）</li>
        <li><b>存储行业内部分化加剧</b>：NAND Flash指引疲软引发抛售，但HBM供需缺口扩大，摩根士丹利认为存储短缺可能持续2-3年（来源：Morgan Stanley/36氪）</li>
        <li><b>葛卫东夫妇增持兆易创新</b>：二季度合计增持4.66亿元，知名投资人逆势加仓DRAM赛道（来源：东方财富/先机财经）</li>
        <li><b>韩国半导体暴跌后盘前反弹</b>：SK海力士韩股盘前涨1.4%、三星涨1.3%，前一交易日分别暴跌10.37%和6.3%（来源：Newsis/韩联社）</li>
        <li><b>高盛/摩根大通大幅增持中际旭创</b>：高盛多头持仓升至12.19%、摩根大通升至13.72%，外资加码光模块龙头（来源：港交所/钛媒体）</li>
        <li><b>网信办对派拓网络启动网络安全审查</b>：国产替代逻辑强化，网络安全板块迎催化（来源：网信办/钛媒体）</li>
    </ul>
</div>
"""

gen._components.append(
    type('obj', (object,), {
        'render': lambda self: f'<div class="report-section"><div class="section-header"><span class="section-icon">🌍</span><span class="section-title">隔夜全球市场扫描</span></div><div class="section-content">{overnight_html}</div></div>'
    })()
)

# ========== 4. 产业链分析 ==========
gen.add_industry_chain_analysis(
    upstream=[
        {"name": "半导体材料/HBM材料", "impact": "⭐⭐⭐⭐⭐", "desc": "HBM短缺加剧+国产替代加速，前驱体、光刻胶、电子特气等上游材料量价齐升逻辑强化"},
        {"name": "半导体设备/零部件", "impact": "⭐⭐⭐⭐", "desc": "日本出口管制升级+国产替代政策加码，设备零部件国产化率提升加速"},
    ],
    midstream=[
        {"name": "先进封装/HBM封装", "impact": "⭐⭐⭐⭐⭐", "desc": "HBM短缺凸显封装环节价值，CoWoS、2.5D/3D封装需求持续扩张，国内封测链弹性释放"},
        {"name": "存储芯片（结构性分化）", "impact": "⭐⭐⭐", "desc": "NAND指引疲软短期承压，但HBM/DRAM紧缺逻辑不变，行业内部分化加剧，优选有HBM/DRAM敞口标的"},
        {"name": "AI芯片设计", "impact": "⭐⭐⭐⭐", "desc": "英伟达Rubin缩显存不改AI算力长期趋势，国产AI芯片替代逻辑持续强化"},
    ],
    downstream=[
        {"name": "光模块/CPO", "impact": "⭐⭐⭐⭐", "desc": "中际旭创获高盛/摩根大通大幅增持，AI算力扩张持续带动高速光模块需求"},
        {"name": "AI算力基建/液冷", "impact": "⭐⭐⭐", "desc": "DeepSeek上调API定价验证算力需求景气，但液冷板块前期调整深，需等待企稳信号"},
    ]
)

# ========== 5. 投资机会（StockTags组件） ==========
gen.add_investment_opportunities(
    opportunities=[
        {
            "title": "HBM材料/先进封装（供给侧缺口主线）",
            "level": "S级",
            "logic": "英伟达缩减Rubin显存+HBM短缺成AI最大瓶颈，供给侧缺口是确定性最强的主线，材料/封装环节受益最直接",
            "stocks": [
                {"code": "002409", "name": "雅克科技", "impact": "HBM前驱体龙头+光刻胶"},
                {"code": "688525", "name": "佰维存储", "impact": "存储模组+HBM封测"},
                {"code": "600584", "name": "长电科技", "impact": "先进封装龙头"},
                {"code": "002156", "name": "通富微电", "impact": "AMD核心封测+HBM封装"},
            ]
        },
        {
            "title": "半导体设备/国产替代",
            "level": "S级",
            "logic": "日本出口管制升级+商务部反制+大基金三期持续投入，设备国产化是贯穿下半年的主线",
            "stocks": [
                {"code": "688012", "name": "中微公司", "impact": "刻蚀设备龙头"},
                {"code": "300604", "name": "长川科技", "impact": "测试设备"},
                {"code": "688082", "name": "盛美上海", "impact": "清洗/电镀设备"},
                {"code": "603690", "name": "至纯科技", "impact": "湿法设备"},
            ]
        },
        {
            "title": "光通信/光模块（外资加仓验证）",
            "level": "A级",
            "logic": "高盛/摩根大通大幅增持中际旭创，AI算力扩张持续带动高速光模块需求，业绩确定性强",
            "stocks": [
                {"code": "300308", "name": "中际旭创", "impact": "光模块龙头 外资加仓"},
                {"code": "300502", "name": "新易盛", "impact": "高速光模块"},
                {"code": "002281", "name": "光迅科技", "impact": "光芯片/光模块"},
            ]
        },
        {
            "title": "高端铜箔/PCB材料",
            "level": "A级",
            "logic": "AI服务器铜箔用量是传统机型5-10倍，HVLP高端铜箔全球缺口1500吨，铜冠铜箔等国产厂商量价齐升",
            "stocks": [
                {"code": "301217", "name": "铜冠铜箔", "impact": "HBM/HBF铜箔核心供应商"},
                {"code": "600183", "name": "生益科技", "impact": "覆铜板龙头 英伟达认证"},
                {"code": "002463", "name": "沪电股份", "impact": "AI算力PCB龙头"},
            ]
        },
    ],
    view_mode="card"
)

# ========== 6. 催化深度分析 ==========
gen.add_catalyst_deep_analysis(
    events=[
        {
            "title": "存储链全球重挫：预期差修正而非周期见顶",
            "type": "市场情绪",
            "description": "闪迪/西部数据财报超预期但指引不及高预期，引发存储板块集体回调。本质是高估值背景下的预期差修正，而非行业景气拐点。闪迪FY2027约50%产能已通过NBM锁定，FY2028升至2/3，供需紧张格局仍将持续",
            "category": "存储芯片"
        },
        {
            "title": "HBM短缺：AI算力供给侧瓶颈转移",
            "type": "产业催化",
            "description": "英伟达考虑缩减Rubin Ultra显存+台积电10亿美元A20芯片等DRAM+马斯克定性内存是AI最大瓶颈，标志AI算力瓶颈从GPU转向HBM存储。HBM产业链紧缺逻辑进一步强化，上游材料/封装环节价值重估",
            "category": "HBM/先进封装"
        },
        {
            "title": "AI行情分化：从普涨到龙头集中",
            "type": "市场结构",
            "description": "微软创历史新高+英伟达近2个月新高+存储链重挫，反映AI行情从普涨转向业绩确定性龙头。资金集中流向竞争优势明确、盈利兑现能力强的核心龙头，二线标的面临估值压力",
            "category": "宏观/市场"
        },
    ]
)

# ========== 7. 风险提示 ==========
gen.add_risk_warning(
    risks=[
        "存储板块全球暴跌情绪可能向A股传导，需警惕开盘后存储概念股低开压力",
        "今晚20:30美国7月非农就业数据，若超预期强劲可能引发美联储加息预期升温，全球风险资产承压",
        "霍尔木兹海峡局势反复，油价大涨可能推升通胀预期，压制成长股估值",
        "英伟达缩减Rubin显存可能被解读为AI需求不及预期，影响AI板块整体情绪",
        "A股缩量上涨（2.53万亿缩量1300亿），主力资金净流出311亿，追高力量不足，警惕冲高回落",
        "先进封装/半导体材料短期涨幅较大，存在获利回吐风险，不建议追高",
        "持仓个股英维克、铜冠铜箔技术面仍偏弱，需严格执行止损纪律"
    ]
)

# ========== 8. 投资策略（含持仓建议） ==========
strategy_text = """
<b>【整体策略】科技板块结构性分化加剧，聚焦HBM供给侧缺口主线，控制仓位谨慎操作</b><br><br>

隔夜美股存储链重挫但半导体指数深V反转，反映市场对AI产业链的定价逻辑正在发生结构性变化——从普涨转向供给侧缺口龙头集中。操作策略：<br>
① 回避纯存储/NAND概念股，聚焦HBM材料、先进封装、半导体设备等有真实业绩支撑的供给侧主线；<br>
② 整体仓位控制在3-4成，等待今晚非农数据落地后再做方向性决策；<br>
③ 不追高，利用回调分批布局基本面扎实的细分龙头。<br><br>

<b>【持仓个股操作建议】</b><br><br>

<b>🔴 英维克（002837）：下降趋势未改，反弹继续减仓</b><br>
液冷板块虽受益于AI算力长期逻辑，但个股下降趋势完全失控，从高点回撤超65%。昨日微涨1.15%但成交缩量，缺乏主动买盘。<br>
<b>操作：</b>反弹至55-58元区间分批减仓，跌破50元无条件止损清仓，严禁补仓抄底。<br>
<b>估值锚：</b>当前PE（TTM）约140倍，2026年业绩增速约30%，PEG≈4.7倍严重偏高。合理估值区间35-45元（对应25-30x 2027E PE）。<br><br>

<b>🟡 铜冠铜箔（301217）：HBM铜箔逻辑受益，但存储情绪扰动需警惕</b><br>
高端铜箔量价齐升逻辑不变，上半年净利同比+540%以上，HVLP全谱系量产。但存储板块全球暴跌可能对铜箔板块情绪造成短期扰动。<br>
<b>操作：</b>持仓成本附近持有观察，反弹至90-95元减仓锁定利润，跌破80元（前低）止损。不建议加仓。<br>
<b>估值锚：</b>当前PE（2026E）约20-25x，高端铜箔涨价周期下业绩弹性大，PEG≈0.5-0.8低估。但需警惕存储周期见顶风险，持续跟踪HBM铜箔放量进度。<br><br>

<b>🟢 雅克科技（002409）：HBM前驱体龙头，供给侧缺口核心受益</b><br>
HBM短缺加剧是昨夜最核心的产业催化，雅克作为HBM前驱体全球核心供应商，中长期逻辑进一步强化。昨日主力净流出5811万（8月5日净流入4.86亿后正常回调），技术面150元支撑位有效。<br>
<b>操作：</b>150元以上持有底仓，若回调至145-150元可适度加仓机动仓，反弹至160-165元减仓机动仓做T。站稳165元看高一线。<br>
<b>估值锚：</b>当前PE（2026E）约35-40x，HBM前驱体全球份额领先，业绩增速40%+，PEG≈1合理。HBM紧缺加剧背景下，目标价180-200元（2027年25-30x PE）。<br>
<b>双重验证：</b>产业逻辑（HBM短缺加剧+英伟达缩显存）+业绩验证（前驱体订单增长+Q2业绩预期），两个独立信号源交叉确认，持有逻辑稳固。<br><br>

<b>🚨 *ST建艺（002789）：立即清仓，退市风险敞口必须关闭</b><br>
退市风险+债务问题未消除，地量成交流动性极差，与科技反弹无关。<b>最高优先级：无条件清仓止损</b>，绝不恋战。<br><br>

<b>【仓位建议】</b>整体仓位3-4成，核心配置HBM材料/先进封装（雅克科技）+半导体设备+光模块，回避纯存储概念股和高位题材股。今晚非农数据落地前保持谨慎，数据出炉后视情况调整仓位。
"""

gen.add_investment_strategy(strategy_text)

# ========== 9. 发布 ==========
result = gen.publish(
    title="S级催化盘前 - 存储链重挫+HBM短缺加剧",
    excerpt="闪迪/西部数据指引不及预期引发存储链全球重挫，英伟达缩减Rubin显存暴露HBM短缺，AI算力瓶颈从GPU转向存储，供给侧缺口主线成确定性方向",
    filename="20260807_盘前_S级催化扫描_存储链重挫+HBM短缺加剧.html"
)

print(f"发布结果: {result}")
