#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S级催化扫描 - 2026年8月5日 盘前
隔夜全球科技多重共振利好
"""
import sys, os
sys.path.insert(0, '/root/daily-news-insight/v3')
os.chdir('/root/daily-news-insight')

from v3.generators.s_level_catalyst import SLevelCatalystGenerator

gen = SLevelCatalystGenerator(
    date_str="20260805",
    catalyst_title="隔夜全球科技多重共振：费半暴涨6.55%+台积电上调资本开支+央行放水2000亿",
    subtitle="2026.08.05 · 盘前S级催化"
)

# ========== 1. 催化概述 ==========
gen.add_catalyst_overview(
    overview="隔夜全球资本市场迎来多重重磅利好共振：费城半导体指数暴涨6.55%创四连涨累计反弹超15%，台积电将2026年资本开支上限上调至640亿美元（+80亿），SK海力士联合闪迪发布HBF下一代存储技术标准，央行开展5000亿买断式逆回购净投放2000亿中长期流动性。AI算力产业链基本面持续验证，科技成长主线有望迎来修复反弹。",
    importance="极高"
)

# ========== 2. 催化详情 ==========
gen.add_catalyst_details(
    background=(
        "7月全球科技股经历剧烈调整，A股半导体/AI算力板块从高点回撤30%-50%，"
        "市场对AI资本开支可持续性产生担忧。进入8月，随着美股财报季密集披露，"
        "AI产业链业绩持续超预期，叠加地缘局势缓和（霍尔木兹海峡重开谈判、油价暴跌6%），"
        "全球风险偏好快速回升。"
    ),
    trigger=(
        "① 美股半导体板块集体爆发，费城半导体指数涨6.55%，ARM+17%、闪迪+10%、"
        "英特尔+10%、美光+7.6%、AMD+7%、英伟达+2%；<br>"
        "② 台积电上调2026年资本开支至600-640亿美元（原520-560亿），追加80亿投向AI芯片/先进封装/HBM；<br>"
        "③ SK海力士+闪迪发布HBF（高带宽闪存）首个标准规范，谷歌、Tenstorrent加入联盟；<br>"
        "④ 央行开展5000亿3个月买断式逆回购，净投放2000亿中长期流动性；<br>"
        "⑤ 美伊谈判取得进展，布油暴跌6%破79美元，通胀预期降温利好成长股估值。"
    )
)

# ========== 3. 隔夜外盘扫描模块 ==========
overnight_html = """
<div class="grid grid-cols-2 md:grid-cols-4 gap-3 mb-4">
    <div style="background: linear-gradient(135deg, rgba(34,197,94,0.15) 0%, rgba(22,163,74,0.08) 100%); 
                border-radius: 12px; padding: 16px; border: 1px solid rgba(34,197,94,0.3);">
        <div style="font-size: 12px; color: #86efac; margin-bottom: 6px;">费城半导体SOX</div>
        <div style="font-size: 22px; font-weight: 800; color: #4ade80;">+6.55%</div>
        <div style="font-size: 11px; color: #6ee7b7; margin-top: 4px;">四连涨累涨15%+</div>
    </div>
    <div style="background: linear-gradient(135deg, rgba(34,197,94,0.15) 0%, rgba(22,163,74,0.08) 100%); 
                border-radius: 12px; padding: 16px; border: 1px solid rgba(34,197,94,0.3);">
        <div style="font-size: 12px; color: #86efac; margin-bottom: 6px;">纳斯达克</div>
        <div style="font-size: 22px; font-weight: 800; color: #4ade80;">+2.59%</div>
        <div style="font-size: 11px; color: #6ee7b7; margin-top: 4px;">报26584.99点</div>
    </div>
    <div style="background: linear-gradient(135deg, rgba(34,197,94,0.15) 0%, rgba(22,163,74,0.08) 100%); 
                border-radius: 12px; padding: 16px; border: 1px solid rgba(34,197,94,0.3);">
        <div style="font-size: 12px; color: #86efac; margin-bottom: 6px;">道琼斯</div>
        <div style="font-size: 22px; font-weight: 800; color: #4ade80;">+1.71%</div>
        <div style="font-size: 11px; color: #6ee7b7; margin-top: 4px;">首破54000点创历史新高</div>
    </div>
    <div style="background: linear-gradient(135deg, rgba(239,68,68,0.15) 0%, rgba(220,38,38,0.08) 100%); 
                border-radius: 12px; padding: 16px; border: 1px solid rgba(239,68,68,0.3);">
        <div style="font-size: 12px; color: #fca5a5; margin-bottom: 6px;">布伦特原油</div>
        <div style="font-size: 22px; font-weight: 800; color: #f87171;">-6.0%</div>
        <div style="font-size: 11px; color: #fca5a5; margin-top: 4px;">报78.68美元/桶</div>
    </div>
</div>

<div class="grid grid-cols-2 md:grid-cols-4 gap-3 mb-4">
    <div style="background: rgba(34,197,94,0.08); border-radius: 10px; padding: 12px; border: 1px solid rgba(34,197,94,0.2);">
        <div style="font-size: 12px; color: #86efac;">美光科技 MU</div>
        <div style="font-size: 18px; font-weight: 700; color: #4ade80;">+7.62%</div>
    </div>
    <div style="background: rgba(34,197,94,0.08); border-radius: 10px; padding: 12px; border: 1px solid rgba(34,197,94,0.2);">
        <div style="font-size: 12px; color: #86efac;">AMD</div>
        <div style="font-size: 18px; font-weight: 700; color: #4ade80;">+7.0%</div>
        <div style="font-size: 10px; color: #fca5a5;">盘后-9%（指引不及高预期）</div>
    </div>
    <div style="background: rgba(34,197,94,0.08); border-radius: 10px; padding: 12px; border: 1px solid rgba(34,197,94,0.2);">
        <div style="font-size: 12px; color: #86efac;">英伟达 NVDA</div>
        <div style="font-size: 18px; font-weight: 700; color: #4ade80;">+2.17%</div>
    </div>
    <div style="background: rgba(34,197,94,0.08); border-radius: 10px; padding: 12px; border: 1px solid rgba(34,197,94,0.2);">
        <div style="font-size: 12px; color: #86efac;">阿斯麦 ASML</div>
        <div style="font-size: 18px; font-weight: 700; color: #4ade80;">+4%</div>
    </div>
</div>

<div class="grid grid-cols-2 md:grid-cols-4 gap-3 mb-4">
    <div style="background: rgba(34,197,94,0.08); border-radius: 10px; padding: 12px; border: 1px solid rgba(34,197,94,0.2);">
        <div style="font-size: 12px; color: #86efac;">闪迪 SNDK</div>
        <div style="font-size: 18px; font-weight: 700; color: #4ade80;">+10%+</div>
    </div>
    <div style="background: rgba(34,197,94,0.08); border-radius: 10px; padding: 12px; border: 1px solid rgba(34,197,94,0.2);">
        <div style="font-size: 12px; color: #86efac;">应用材料 AMAT</div>
        <div style="font-size: 18px; font-weight: 700; color: #4ade80;">+5%</div>
    </div>
    <div style="background: rgba(34,197,94,0.08); border-radius: 10px; padding: 12px; border: 1px solid rgba(34,197,94,0.2);">
        <div style="font-size: 12px; color: #86efac;">台积电 TSM</div>
        <div style="font-size: 18px; font-weight: 700; color: #4ade80;">+2%+</div>
        <div style="font-size: 10px; color: #86efac;">1.4nm厂进度超前</div>
    </div>
    <div style="background: rgba(34,197,94,0.08); border-radius: 10px; padding: 12px; border: 1px solid rgba(34,197,94,0.2);">
        <div style="font-size: 12px; color: #86efac;">ARM</div>
        <div style="font-size: 18px; font-weight: 700; color: #4ade80;">+17%</div>
    </div>
</div>

<div style="background: rgba(59,130,246,0.08); border-radius: 10px; padding: 14px; border-left: 3px solid #3b82f6;">
    <div style="font-size: 13px; color: #93c5fd; font-weight: 600; margin-bottom: 6px;">📰 隔夜重要产业消息</div>
    <ul style="font-size: 12px; color: #cbd5e1; line-height: 1.9; margin: 0; padding-left: 18px;">
        <li><b>台积电资本开支上调</b>：2026全年CapEx上调至600-640亿美元（原520-560亿），追加80亿投向AI芯片/先进封装/HBM配套产能（来源：财联社/中信建投）</li>
        <li><b>SK海力士+闪迪发布HBF标准</b>：高带宽闪存首个标准规范发布，8层/16层堆叠最高512GB，带宽0.4-3TB/s，谷歌已加入联盟（来源：SK海力士官方/中国证券报）</li>
        <li><b>AMD Q2财报超预期但盘后跌</b>：营收115亿美元（+50%），数据中心收入67亿（+107%），Q3指引130亿超一致预期但不及部分乐观预期，盘后跌9%（来源：AMD官方/第一财经）</li>
        <li><b>存储涨价周期延续</b>：集邦咨询预测Q3 DRAM合约价涨13%-18%，NAND涨10%-15%，三大原厂2027年HBM产能已提前售罄（来源：券商中国/集邦咨询）</li>
        <li><b>国务院修订集成电路布图设计保护条例</b>：10月15日施行，引入惩罚性赔偿，扩展保护范围至光子/量子集成电路（来源：新华社/人民网）</li>
        <li><b>日本第三轮半导体出口管制8月1日生效</b>：20大类先进封装设备纳入管制，高端固晶机/减薄机/3D键合设备等需逐案审批（来源：搜狐/行业媒体）</li>
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
        {"name": "半导体设备", "impact": "⭐⭐⭐⭐⭐", "desc": "台积电上调CapEx+设备交期延长涨价，上游设备零部件充分受益"},
        {"name": "半导体材料", "impact": "⭐⭐⭐⭐", "desc": "HBM/先进封装扩产带动前驱体、光刻胶、CMP材料需求增长"},
    ],
    midstream=[
        {"name": "晶圆代工/先进封装", "impact": "⭐⭐⭐⭐⭐", "desc": "台积电CoWoS产能持续紧张，CoW环节外包日月光等封测厂，国内封测链受益"},
        {"name": "存储芯片", "impact": "⭐⭐⭐⭐⭐", "desc": "HBF标准发布+存储涨价周期延续+HBM产能售罄，量价齐升逻辑强化"},
        {"name": "AI芯片设计", "impact": "⭐⭐⭐⭐", "desc": "AI算力需求持续超预期，国产替代加速，AMD业绩验证行业高景气"},
    ],
    downstream=[
        {"name": "AI服务器/算力基础设施", "impact": "⭐⭐⭐⭐", "desc": "Anthropic与Volta Infra签100亿美元算力协议，AI资本开支持续验证"},
        {"name": "光通信/CPO", "impact": "⭐⭐⭐⭐", "desc": "应用光电+19%、Coherent+12%，AI算力扩张带动光模块需求"},
    ]
)

# ========== 5. 投资机会（StockTags组件） ==========
gen.add_investment_opportunities(
    opportunities=[
        {
            "title": "存储芯片/HBM产业链",
            "level": "S级",
            "logic": "HBF标准发布打开存储新赛道，Q3涨价延续+2027年产能售罄，量价齐升逻辑再强化",
            "stocks": [
                {"code": "002409", "name": "雅克科技", "impact": "HBM前驱体龙头"},
                {"code": "301217", "name": "铜冠铜箔", "impact": "HBM/HBF铜箔核心供应商"},
                {"code": "688525", "name": "佰维存储", "impact": "存储模组+HBM封测"},
                {"code": "688099", "name": "晶晨股份", "impact": "存储控制芯片"},
            ]
        },
        {
            "title": "半导体设备/零部件（国产替代）",
            "level": "S级",
            "logic": "台积电上调80亿美元CapEx+日本先进封装设备管制，国产设备替代加速",
            "stocks": [
                {"code": "688012", "name": "中微公司", "impact": "刻蚀设备龙头"},
                {"code": "603501", "name": "韦尔股份", "impact": "半导体设计+设备"},
                {"code": "300604", "name": "长川科技", "impact": "测试设备"},
                {"code": "688082", "name": "盛美上海", "impact": "清洗/电镀设备"},
            ]
        },
        {
            "title": "先进封装/CoWoS产业链",
            "level": "A级",
            "logic": "台积电CoWoS供需缺口20%，CoW环节外包封测厂，国内封测链弹性释放",
            "stocks": [
                {"code": "600584", "name": "长电科技", "impact": "先进封装龙头"},
                {"code": "002156", "name": "通富微电", "impact": "AMD核心封测合作方"},
                {"code": "002185", "name": "华天科技", "impact": "存储封测"},
            ]
        },
        {
            "title": "光通信/CPO",
            "level": "A级",
            "logic": "隔夜美股光通信板块暴涨（应用光电+19%），AI算力扩张持续带动光模块需求",
            "stocks": [
                {"code": "300308", "name": "中际旭创", "impact": "光模块龙头"},
                {"code": "300502", "name": "新易盛", "impact": "高速光模块"},
                {"code": "002281", "name": "光迅科技", "impact": "光芯片/光模块"},
            ]
        },
    ],
    view_mode="card"
)

# ========== 6. 催化深度分析（Skill增强） ==========
gen.add_catalyst_deep_analysis(
    events=[
        {
            "title": "台积电上调资本开支",
            "type": "产业催化",
            "description": "台积电将2026年CapEx从520-560亿美元上调至600-640亿美元，追加80亿投向AI芯片、先进封装、HBM配套产能",
            "category": "半导体设备"
        },
        {
            "title": "HBF存储技术标准发布",
            "type": "技术突破",
            "description": "SK海力士+闪迪联合发布高带宽闪存HBF首个标准规范，定位介于HBM与SSD之间的新型存储层级",
            "category": "存储芯片"
        },
        {
            "title": "美股半导体暴涨+央行放水",
            "type": "市场情绪",
            "description": "费城半导体涨6.55%四连涨，央行净投放2000亿中长期流动性，科技成长情绪修复",
            "category": "宏观/市场"
        },
    ]
)

# ========== 7. 风险提示 ==========
gen.add_risk_warning(
    risks=[
        "AMD盘后大跌9%可能拖累A股AI芯片情绪，需关注开盘反应",
        "高开过多可能引发短线获利盘兑现，警惕冲高回落风险（创业板昨日已涨5.64%）",
        "日本半导体出口管制升级（8月1日生效），先进封装设备供应链存在不确定性",
        "存储涨价周期高位，渠道库存与终端需求需持续跟踪，警惕周期拐点风险",
        "地缘局势反复（霍尔木兹海峡），油价波动可能传导至通胀与流动性预期"
    ]
)

# ========== 8. 投资策略（含持仓建议） ==========
strategy_text = """
<b>【整体策略】三重利好共振下的科技成长反弹窗口，控制仓位灵活操作</b><br><br>

隔夜外围科技股暴涨+台积电上调资本开支+央行流动性投放三重利好共振，A股科技成长板块有望延续反弹。但需要注意：
① AMD盘后跌9%可能对AI芯片板块情绪造成扰动；② 创业板昨日已大涨5.64%，高开过多警惕获利回吐；③ 反弹性质仍是修复而非反转，仓位控制在3-5成。<br><br>

<b>【持仓个股操作建议】</b><br><br>

<b>🔴 英维克（002837）：深度破止损，反弹坚决减仓/清仓</b><br>
液冷板块虽有望随AI算力情绪反弹，但个股下降趋势已完全失控（从高点回撤超65%），基本面没有新增逻辑。
<b>操作：</b>任何反弹都是减仓/离场机会，反弹至55-58元区间分批减仓，严禁补仓抄底。
<b>估值锚：</b>当前PE（TTM）约60x，2026年业绩增速约30%，PEG≈2倍仍偏高，合理估值区间40-45元（对应25-30x PE）。<br><br>

<b>🟡 铜冠铜箔（301217）：存储+HBF双催化，85元为生命线</b><br>
隔夜存储板块大涨+HBF标准发布，铜箔作为HBM/HBF核心材料直接受益。但个股从高点回撤超57%，技术面仍偏弱。
<b>操作：</b>85元以上持有观察，反弹至90-95元减仓锁定成本，跌破85元无条件止损。
<b>估值锚：</b>当前PE（2026E）约25-28x，存储铜箔涨价周期下业绩弹性大，但需验证HBM铜箔放量进度。<br><br>

<b>🟢 雅克科技（002409）：HBM前驱体龙头，HBF催化+存储涨价双驱动</b><br>
隔夜SK海力士+闪迪发布HBF标准，存储产业链情绪直接提振。雅克作为HBM前驱体核心供应商，中长期逻辑不变。150元关键支撑位经昨日大跌考验。
<b>操作：</b>150元以上持有底仓，反弹至160-165元可减仓机动仓，站稳165元可适度加仓。
<b>估值锚：</b>当前PE（2026E）约35-40x，HBM前驱体全球份额领先，业绩增速40%+，PEG≈1合理。目标价180-200元（2027年25-30x PE）。<br><br>

<b>🚨 *ST建艺（002789）：立即清仓，退市风险敞口必须关闭</b><br>
退市风险+债务问题未消除，地量成交流动性极差，与科技反弹无关。<b>最高优先级：无条件清仓止损</b>，绝不恋战。<br><br>

<b>【仓位建议】</b>整体仓位3-5成，核心配置存储/HBM（雅克科技、铜冠铜箔）+半导体设备，回避纯题材股和高位股。现金为王，等待市场确认企稳信号（缩量止跌+量价配合反弹）后再逐步加仓。
"""

gen.add_investment_strategy(strategy_text)

# ========== 9. 发布 ==========
result = gen.publish(
    title="S级催化盘前 - 隔夜科技多重共振",
    excerpt="费半暴涨6.55%+台积电上调资本开支+央行放水2000亿+存储HBF标准发布，A股科技成长迎修复窗口",
    filename="20260805_盘前_S级催化扫描_隔夜科技多重共振.html"
)

print(f"发布结果: {result}")
