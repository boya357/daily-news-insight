#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
20260730 盘后 S级催化扫描
核心催化：政治局会议定调下半年经济 + 增量政策预期 + 科技股错杀甄别
"""
import sys, os
sys.path.insert(0, 'v3')
os.chdir('/root/daily-news-insight')

from v3.generators.s_level_catalyst import SLevelCatalystGenerator

gen = SLevelCatalystGenerator(
    date_str="20260730",
    catalyst_title="政治局会议定调增量政策",
    subtitle="2026.07.30 · 盘后S级催化"
)

# ============ 1. 催化事件概述 ============
gen.add_catalyst_overview(
    "中共中央政治局7月30日召开会议，部署下半年经济工作，明确提出\"实施好更加积极的财政政策和适度宽松的货币政策，及时谋划出台务实管用的增量政策，加大逆周期调节力度\"。"
    "同时强调\"深化资本市场投融资综合改革，提升资本市场韧性和信心\"。"
    "在科技股连续暴跌、市场情绪极度悲观的背景下，本次政治局会议释放的政策加码信号，构成S级宏观催化。"
    "叠加长江存储深夜辟谣专利无效传闻、美股盘后微软大涨7.8%（资本支出指引超预期）等多重利好，科技股有望迎来超跌修复窗口。",
    importance="S级"
)

# ============ 2. 事件背景与触发因素 ============
gen.add_catalyst_details(
    background=
    "【宏观背景】2026年上半年经济呈现动能向新、结构向优态势，但面临外部冲击与内部困难挑战。"
    "7月以来A股科技板块持续调整，科创50从高点回撤超30%，半导体、光模块、AI算力等前期主线集体重挫，市场情绪跌入冰点。"
    "美联储连续第五次按兵不动，联邦基金利率维持3.5%-3.75%，但内部鹰派声音增强（3票反对加息），全球科技股承压。"
    "市场普遍担忧：AI资本开支能否兑现、科技股估值是否过高、外部地缘风险是否升级。",

    trigger=
    "【核心触发】7月30日政治局会议六大重磅信号：\n"
    "1️⃣ 政策加码：更加积极的财政政策+适度宽松的货币政策，增量政策在路上\n"
    "2️⃣ 逆周期调节：加大逆周期调节力度，加快财政支出和债券资金使用\n"
    "3️⃣ 资本市场：深化投融资综合改革，提升韧性和信心（首次将资本市场纳入安全屏障体系）\n"
    "4️⃣ 产业方向：深入实施\"人工智能+\"行动，打造新兴支柱产业，推进\"六张网\"建设\n"
    "5️⃣ 扩内需：挖掘服务消费潜力，适应不同群体消费需求扩大优质供给\n"
    "6️⃣ 防风险：稳定房地产市场，实施一揽子化债方案，推进地方中小金融机构改革\n\n"
    "【盘后催化共振】长江存储深夜辟谣专利无效传闻（27项专利在美起诉美光）、微软盘后大涨7.8%（FY2027 CapEx指引1750亿美元），多重利好叠加。"
)

# ============ 3. 产业链分析 ============
gen.add_industry_chain_analysis(
    upstream=[
        {"name": "半导体设备/材料", "desc": "国产替代核心，大基金三期持续投入，AI+行动长期受益", "tag": "重点"},
        {"name": "电子特气/光刻胶", "desc": "长江存储专利反击印证技术实力，半导体材料国产替代加速", "tag": "催化"},
        {"name": "存储芯片", "desc": "长江存储IPO推进中，Xtacking架构全球领先，3D NAND价格周期向上", "tag": "关注"},
    ],
    midstream=[
        {"name": "AI算力基础设施", "desc": "微软CapEx 1750亿美元指引超预期，算力需求确定性强，液冷/PCB/光模块回调后性价比凸显", "tag": "重点"},
        {"name": "先进封装/HBM", "desc": "AI芯片核心封装技术，国产替代空间大，雅克科技/华海诚科等材料龙头", "tag": "重点"},
        {"name": "人形机器人", "desc": "美方限制先进机器人进口，反而倒逼国产替代加速，核心零部件自主可控", "tag": "催化"},
    ],
    downstream=[
        {"name": "大消费/白酒/食品饮料", "desc": "扩内需政策直接受益，防御属性强，机构调仓首选", "tag": "受益"},
        {"name": "AI应用/教育/软件", "desc": "人工智能+行动落地，应用层需求释放，传智教育等领涨", "tag": "活跃"},
        {"name": "银行/高股息", "desc": "资本市场改革受益，估值修复+高股息防御，北向资金回补", "tag": "防御"},
    ]
)

# ============ 4. 影响个股 - 持仓评估 ============
gen.add_catalyst_deep_analysis([
    {
        "title": "持仓股影响评估",
        "level": "high",
        "impact": "中性偏多，政策底确认",
        "stocks": [
            {"code": "002837", "name": "英维克", "impact": "利空出尽？连续4日暴跌累计-30%，液冷逻辑未变但情绪极致悲观，政策底后或迎技术反弹，但中期趋势仍弱"},
            {"code": "301217", "name": "铜冠铜箔", "impact": "中性偏多，存储铜箔刚需+AI算力PCB铜箔双逻辑，80元附近有支撑，政策催化下超跌反弹概率大"},
            {"code": "002409", "name": "雅克科技", "impact": "中性偏多，HBM前驱体龙头+半导体材料国产替代核心标的，跌停属板块系统性杀跌，政策底+产业逻辑硬，反弹弹性大"},
            {"code": "002789", "name": "*ST建艺", "impact": "利空，退市风险未消除，政策利好不覆盖ST股，继续坚持清仓纪律"},
        ],
        "analysis": "今日持仓4只3只跌停（英维克/雅克科技/*ST建艺），铜冠铜箔跌8.57%创调整新低。"
                   "核心原因是板块系统性杀跌+恐慌情绪蔓延，并非个股基本面恶化。"
                   "政治局会议释放增量政策信号，叠加微软CapEx指引超预期验证AI算力需求，科技股政策底已现，但市场底需时间确认。"
                   "操作上：雅克科技/铜冠铜箔等有硬逻辑的标的，可在急跌后分批布局底仓；英维克/*ST建艺坚持纪律离场。"
    },
    {
        "title": "龙虎榜资金信号",
        "level": "medium",
        "impact": "机构逆势回补龙头",
        "stocks": [
            {"code": "000938", "name": "紫光股份", "impact": "跌停+机构净买5.06亿，机构在跌停板上真金白银回补，IT服务龙头错杀信号明确"},
            {"code": "600584", "name": "长电科技", "impact": "跌停+龙虎榜净买入3.17亿，先进封装龙头，机构逆势接盘"},
            {"code": "002156", "name": "通富微电", "impact": "跌停+机构净卖4.46亿+北向净卖13.5亿，先进封装方向资金分歧大，短期承压"},
            {"code": "001309", "name": "德明利", "impact": "涨停+机构净卖4.57亿+北向净卖3.5亿，典型派发局，机构和北向双双撤退"},
        ],
        "analysis": "龙虎榜数据揭示资金真实意图：紫光股份、长电科技等龙头在跌停板上获机构大额净买入，显示长线资金认为\"跌过头了\"；"
                   "而德明利等小票涨停却是机构在派发，说明资金正在从纯题材小票向有业绩支撑的龙头集中。"
                   "政治局会议后，市场风格将进一步从题材炒作转向业绩+政策双驱动的核心资产。"
    }
])

# ============ 5. 隔夜外盘（独立模块，确保数据可见） ============
overnight_html = '''
<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-bottom: 16px;">
    <!-- 美股指数 -->
    <div style="background: linear-gradient(135deg, rgba(239,68,68,0.12) 0%, rgba(185,28,28,0.08) 100%); 
                border-radius: 14px; padding: 18px; border: 1px solid rgba(248,113,113,0.25);">
        <div style="display: flex; align-items: center; margin-bottom: 14px;">
            <div style="width: 34px; height: 34px; background: linear-gradient(135deg, #ef4444, #b91c1c); 
                       border-radius: 9px; display: flex; align-items: center; justify-content: center; margin-right: 10px;">📉</div>
            <span style="font-size: 15px; font-weight: 700; color: #fca5a5;">美股主要指数</span>
        </div>
        <div style="display: flex; flex-direction: column; gap: 10px;">
            <div style="display: flex; justify-content: space-between; align-items: center; padding: 8px 12px; 
                       background: rgba(255,255,255,0.04); border-radius: 8px;">
                <span style="color: #e2e8f0; font-size: 13px;">纳斯达克综合</span>
                <span style="color: #f87171; font-weight: 700; font-size: 14px;">-1.74%</span>
            </div>
            <div style="display: flex; justify-content: space-between; align-items: center; padding: 8px 12px; 
                       background: rgba(255,255,255,0.04); border-radius: 8px;">
                <span style="color: #e2e8f0; font-size: 13px;">标普500</span>
                <span style="color: #f87171; font-weight: 700; font-size: 14px;">-1.52%</span>
            </div>
            <div style="display: flex; justify-content: space-between; align-items: center; padding: 8px 12px; 
                       background: rgba(255,255,255,0.04); border-radius: 8px;">
                <span style="color: #e2e8f0; font-size: 13px;">道琼斯工业</span>
                <span style="color: #f87171; font-weight: 700; font-size: 14px;">-2.19%</span>
            </div>
            <div style="display: flex; justify-content: space-between; align-items: center; padding: 8px 12px; 
                       background: rgba(255,255,255,0.04); border-radius: 8px;">
                <span style="color: #e2e8f0; font-size: 13px;">费城半导体指数</span>
                <span style="color: #f87171; font-weight: 700; font-size: 14px;">-5.0%+ (4日累跌11%+)</span>
            </div>
        </div>
    </div>
    <!-- 核心科技股 -->
    <div style="background: linear-gradient(135deg, rgba(59,130,246,0.12) 0%, rgba(37,99,235,0.08) 100%); 
                border-radius: 14px; padding: 18px; border: 1px solid rgba(96,165,250,0.25);">
        <div style="display: flex; align-items: center; margin-bottom: 14px;">
            <div style="width: 34px; height: 34px; background: linear-gradient(135deg, #3b82f6, #1d4ed8); 
                       border-radius: 9px; display: flex; align-items: center; justify-content: center; margin-right: 10px;">💻</div>
            <span style="font-size: 15px; font-weight: 700; color: #60a5fa;">核心科技股表现</span>
        </div>
        <div style="display: flex; flex-direction: column; gap: 10px;">
            <div style="display: flex; justify-content: space-between; align-items: center; padding: 8px 12px; 
                       background: rgba(255,255,255,0.04); border-radius: 8px;">
                <span style="color: #e2e8f0; font-size: 13px;">英伟达 NVDA</span>
                <span style="color: #f87171; font-weight: 700; font-size: 14px;">-3.5%+</span>
            </div>
            <div style="display: flex; justify-content: space-between; align-items: center; padding: 8px 12px; 
                       background: rgba(255,255,255,0.04); border-radius: 8px;">
                <span style="color: #e2e8f0; font-size: 13px;">微软 MSFT <span style="color: #fbbf24; font-size: 11px;">盘后</span></span>
                <span style="color: #4ade80; font-weight: 700; font-size: 14px;">+7.8% 🔥</span>
            </div>
            <div style="display: flex; justify-content: space-between; align-items: center; padding: 8px 12px; 
                       background: rgba(255,255,255,0.04); border-radius: 8px;">
                <span style="color: #e2e8f0; font-size: 13px;">Meta <span style="color: #fbbf24; font-size: 11px;">盘后</span></span>
                <span style="color: #f87171; font-weight: 700; font-size: 14px;">-7.0%+</span>
            </div>
            <div style="display: flex; justify-content: space-between; align-items: center; padding: 8px 12px; 
                       background: rgba(255,255,255,0.04); border-radius: 8px;">
                <span style="color: #e2e8f0; font-size: 13px;">美光科技 / AMD</span>
                <span style="color: #f87171; font-weight: 700; font-size: 14px;">-9%+ / -5%+</span>
            </div>
        </div>
    </div>
</div>

<!-- 美联储 + 关键事件 -->
<div style="background: linear-gradient(135deg, rgba(168,85,247,0.12) 0%, rgba(139,92,246,0.08) 100%); 
            border-radius: 14px; padding: 18px; border: 1px solid rgba(192,132,252,0.25); margin-bottom: 16px;">
    <div style="display: flex; align-items: center; margin-bottom: 12px;">
        <div style="width: 34px; height: 34px; background: linear-gradient(135deg, #a855f7, #7c3aed); 
                   border-radius: 9px; display: flex; align-items: center; justify-content: center; margin-right: 10px;">🏛️</div>
        <span style="font-size: 15px; font-weight: 700; color: #c084fc;">美联储议息会议 + 关键事件</span>
    </div>
    <div style="color: #cbd5e1; font-size: 13px; line-height: 2; padding: 4px 8px;">
        <b style="color: #fbbf24;">【美联储】</b> 连续第5次按兵不动，利率维持3.5%-3.75%，但<b style="color: #f87171;">3票反对加息</b>（2016年以来首次鹰派分歧），沃什强调"无隐性通胀目标"<br>
        <b style="color: #fbbf24;">【微软财报】</b> FY2027资本支出指引<b style="color: #4ade80;">1750亿美元</b>，Azure AI增长强劲，盘后暴涨7.8%，验证AI算力需求韧性<br>
        <b style="color: #fbbf24;">【Meta财报】</b> 上调全年CapEx下限至<b style="color: #f87171;">1300亿美元</b>，投入加大引发"回报比"担忧，盘后大跌7%+<br>
        <b style="color: #fbbf24;">【长江存储】</b> 深夜声明辟谣"19项专利无效"传闻，27项专利在美起诉美光仍在审理中，Xtacking架构全球领先<br>
        <b style="color: #fbbf24;">【美方限制】</b> FCC将外国电力逆变器和先进机器人列入覆盖清单，商务部回应将坚决反制
    </div>
</div>

<!-- 亚太市场 -->
<div style="background: linear-gradient(135deg, rgba(245,158,11,0.12) 0%, rgba(217,119,6,0.08) 100%); 
            border-radius: 14px; padding: 18px; border: 1px solid rgba(251,191,36,0.25);">
    <div style="display: flex; align-items: center; margin-bottom: 12px;">
        <div style="width: 34px; height: 34px; background: linear-gradient(135deg, #f59e0b, #d97706); 
                   border-radius: 9px; display: flex; align-items: center; justify-content: center; margin-right: 10px;">🌏</div>
        <span style="font-size: 15px; font-weight: 700; color: #fbbf24;">亚太市场动态</span>
    </div>
    <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 10px; margin-top: 8px;">
        <div style="text-align: center; padding: 12px 8px; background: rgba(255,255,255,0.04); border-radius: 10px;">
            <div style="color: #94a3b8; font-size: 12px; margin-bottom: 6px;">韩国KOSPI</div>
            <div style="color: #f87171; font-weight: 800; font-size: 16px;">-12%+</div>
            <div style="color: #64748b; font-size: 11px; margin-top: 4px;">连续熔断</div>
        </div>
        <div style="text-align: center; padding: 12px 8px; background: rgba(255,255,255,0.04); border-radius: 10px;">
            <div style="color: #94a3b8; font-size: 12px; margin-bottom: 6px;">东京电子</div>
            <div style="color: #f87171; font-weight: 800; font-size: 16px;">-10.59%</div>
            <div style="color: #64748b; font-size: 11px; margin-top: 4px;">半导体设备</div>
        </div>
        <div style="text-align: center; padding: 12px 8px; background: rgba(255,255,255,0.04); border-radius: 10px;">
            <div style="color: #94a3b8; font-size: 12px; margin-bottom: 6px;">台积电ADR</div>
            <div style="color: #f87171; font-weight: 800; font-size: 16px;">-3.51%</div>
            <div style="color: #64748b; font-size: 11px; margin-top: 4px;">晶圆代工龙头</div>
        </div>
        <div style="text-align: center; padding: 12px 8px; background: rgba(255,255,255,0.04); border-radius: 10px;">
            <div style="color: #94a3b8; font-size: 12px; margin-bottom: 6px;">中概金龙</div>
            <div style="color: #4ade80; font-weight: 800; font-size: 16px;">+1.7%</div>
            <div style="color: #64748b; font-size: 11px; margin-top: 4px;">逆势飘红</div>
        </div>
    </div>
</div>
'''

from v3.components.layout import Section
overnight_section = Section(title="🌙 隔夜外盘跟踪", content=overnight_html, icon="moon", variant="highlight")
gen._components.insert(4, overnight_section)

# ============ 6. 投资机会 ============
gen.add_investment_opportunities([
    {
        "title": "方向一：AI算力基础设施（错杀修复）",
        "confidence": "高",
        "time_window": "1-2周",
        "return_expectation": "15%-25%",
        "logic": "微软FY2027资本支出1750亿美元指引，验证全球AI算力需求韧性。"
                 "国内算力链经过连续暴跌，估值已大幅消化。政治局会议明确\"人工智能+\"行动，政策+产业双驱动。",
        "targets": [
            {"name": "紫光股份", "code": "000938", "reason": "跌停+机构净买5.06亿，IT服务/算力龙头错杀最明显"},
            {"name": "铜冠铜箔", "code": "301217", "reason": "AI服务器PCB铜箔核心供应商，80元附近支撑强，弹性大"},
            {"name": "雅克科技", "code": "002409", "reason": "HBM前驱体龙头，半导体材料国产替代核心，跌停属错杀"},
        ]
    },
    {
        "title": "方向二：半导体设备/材料（政策+国产替代）",
        "confidence": "高",
        "time_window": "1-3个月",
        "return_expectation": "20%-30%",
        "logic": "政治局会议强调基础研究长期稳定支持+新兴支柱产业打造，半导体设备是战略必争领域。"
                 "长江存储专利反击印证国产技术实力，大基金三期持续投入。",
        "targets": [
            {"name": "长电科技", "code": "600584", "reason": "先进封装龙头，龙虎榜机构逆势净买，估值合理"},
            {"name": "华海诚科", "code": "688535", "reason": "环氧塑封料国产替代龙头，HBM核心材料供应商"},
            {"name": "中船特气", "code": "688146", "reason": "电子特气龙头，六氟化钨全球紧平衡，国产替代加速"},
        ]
    },
    {
        "title": "方向三：大消费/扩内需（政策直接受益）",
        "confidence": "中高",
        "time_window": "1-2周",
        "return_expectation": "10%-15%",
        "logic": "政治局会议明确\"挖掘服务消费潜力\"\"扩大优质供给\"，扩内需政策有望加速落地。"
                 "白酒/食品饮料/教育等消费板块已连续逆势走强，机构调仓方向明确。",
        "targets": [
            {"name": "舍得酒业", "code": "600702", "reason": "白酒板块领涨，业绩弹性大，机构回补"},
            {"name": "传智教育", "code": "003032", "reason": "AI教育龙头，4连板情绪标杆，政策受益"},
            {"name": "一鸣食品", "code": "605179", "reason": "食品消费3连板，消费复苏预期"},
        ]
    }
])

# ============ 7. 风险提示 ============
gen.add_risk_warning([
    "市场底尚未确认：政治局会议是政策底，但市场底通常滞后，仍有二次探底风险，不宜满仓抄底",
    "美联储鹰派风险：3票反对加息显示内部鹰派增强，若通胀反弹可能重启加息，压制全球科技估值",
    "AI投入回报风险：META资本开支上调引发市场对\"投入回报比\"的担忧，纯题材标的估值继续承压",
    "地缘风险：中东局势紧张、美方科技限制升级，可能随时冲击市场情绪",
    "业绩验证风险：中报季进入尾声，高位科技股若业绩不及预期，可能引发新一轮杀跌",
    "个股风险：英维克/*ST建艺等深度破位标的，纪律性减仓/清仓，严禁补仓抄底",
])

# ============ 8. 投资策略 ============
gen.add_investment_strategy(
    "<b>【总仓位建议】3-4成底仓，分批建仓，保留现金应对二次探底</b><br><br>"

    "<b>🔴 必须清仓（纪律执行）：</b><br>"
    "• 英维克（002837）：连续4日暴跌累计-30%+，深度破止损-54.8%，任何反弹都是离场机会，严禁抄底<br>"
    "• *ST建艺（002789）：退市风险未消除，政策利好不覆盖ST，立即清仓关闭敞口<br><br>"

    "<b>🟡 持仓应对（防守反击）：</b><br>"
    "• <b>铜冠铜箔（301217）</b>：收79.51元创调整新低，已破85元支撑位。<b>策略：75-80元区间可分批建底仓（总仓位≤15%）</b>，"
    "AI算力+存储双逻辑，政策催化下超跌反弹弹性大，止损位下移至72元<br>"
    "• <b>雅克科技（002409）</b>：放量跌停收136.96元，150元支撑被有效击穿，短期进入下跌通道。<b>策略：底仓持有不动，120-130元区间可加仓至20%仓位</b>，"
    "HBM前驱体龙头+半导体材料国产替代核心，产业逻辑未变，政策底确认后反弹弹性大，止损位115元<br><br>"

    "<b>🟢 新增关注（政策+错杀双驱动）：</b><br>"
    "• 紫光股份（000938）：跌停+机构净买5.06亿，最明确的错杀信号，32元以下可分批建仓<br>"
    "• 长电科技（600584）：先进封装龙头，机构逆势接盘，60元附近安全边际高<br>"
    "• 华海诚科（688535）：环氧塑封料国产龙头，HBM核心材料，80-85元击球区<br><br>"

    "<b>⏰ 明日重点观察：</b><br>"
    "1. 科技股能否放量反弹（科创50涨幅>3%且成交额放大视为有效反弹）<br>"
    "2. 北向资金流向（连续净流出后是否回补）<br>"
    "3. 龙头标的表现（中际旭创/新易盛/兆易创新是否止跌企稳）<br>"
    "4. 量价配合（反弹必须放量，缩量反抽即是减仓机会）"
)

# ============ 发布 ============
result = gen.publish(
    title="政治局会议定调增量政策",
    filename="20260730_盘后_S级催化扫描_政治局会议定调增量政策.html",
    excerpt="政治局会议定调下半年经济，增量政策在路上，科技股错杀甄别"
)

print("✅ 发布结果：", result)
