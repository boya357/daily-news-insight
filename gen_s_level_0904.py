#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
20260904 盘后 S级催化扫描
三重催化：七部门双化协同方案 + 华虹55亿扩产 + 美光HBM4产能翻倍
"""
import sys, os
sys.path.insert(0, '/root/daily-news-insight/v3')
os.chdir('/root/daily-news-insight')

from v3.generators.s_level_catalyst import SLevelCatalystGenerator
from components.data import StockTags
from components.layout import Section

gen = SLevelCatalystGenerator(
    date_str="20260904",
    catalyst_title="七部门双化协同方案+华虹55亿扩产+美光HBM4翻倍",
    subtitle="2026.09.04 · 盘后S级催化"
)

# Step 1
gen.add_catalyst_overview(
    overview="""
    <strong>【盘后三重催化共振】</strong>9月4日盘后，AI算力与半导体产业迎来"政策+产业+海外"三重利好叠加：<br><br>
    1️⃣ <strong>七部门联合印发《双化协同实施方案》</strong>：明确存算一体、高性能存储、液冷散热、800V高压直流供电、超百千瓦单机柜为重点研发方向，直接利好液冷、存储、算力基础设施全产业链。<br>
    2️⃣ <strong>华虹宏力55.56亿加码无锡三期</strong>：总投资69.5亿美元，月产能5.5万片12英寸特色工艺产线，2027年底投产，国产晶圆代工扩产持续加速。<br>
    3️⃣ <strong>美光宣布HBM4产能翻倍计划</strong>：盘前涨1.89%，年底月产能从5万片扩至6万片12层HBM4，AI存储需求持续爆发。<br><br>
    <strong>评级：S级</strong>｜政策顶层设计+国内龙头扩产+海外龙头验证，AI算力基础设施长逻辑持续强化
    """,
    importance="S级"
)

# Step 2
gen.add_catalyst_details(
    background="""
    <strong>【宏观背景】AI算力扩张与绿色低碳的双重命题</strong><br><br>
    • AI大模型训练算力需求每3-4个月翻番，单GPU功耗从H100的700W攀升至Rubin的2300W，散热与能效成为卡脖子问题<br>
    • 国家"双碳"目标下，数据中心PUE需降至1.25以内，传统风冷已无法满足高端算力散热需求<br>
    • 国内半导体设备/材料/制造环节正处于国产替代加速期，政策扶持+资本开支持续加码<br>
    • 海外AI算力建设持续超预期，美光/英伟达/台积电等龙头不断上修资本开支指引
    """,
    trigger="""
    <strong>【三大触发因素】</strong><br><br>
    📌 <strong>政策端</strong>：中央网信办等七部门9月4日联合印发《促进数字化绿色化协同转型发展实施方案(2026-2030年)》，明确存算一体、高性能存储、液冷散热、800V高压直流供电为重点技术方向<br><br>
    📌 <strong>产业端</strong>：华虹宏力9月4日晚间公告，拟将超募资金及结余募资合计55.56亿元投向无锡三期项目，建月产能5.5万片12英寸特色工艺产线<br><br>
    📌 <strong>海外端</strong>：美光宣布年底前将12层HBM4月产能从5万片翻倍至6万片，美股盘前涨1.89%；纳指期货涨0.5%，英伟达盘前涨1.22%
    """
)

# Step 3
gen.add_industry_chain_analysis(
    upstream=[
        {"name": "半导体设备", "desc": "晶圆厂扩产+国产替代双轮驱动，设备需求30年未见", "stocks": [
            {"code": "002371", "name": "北方华创", "impact": "平台型龙头"},
            {"code": "688012", "name": "中微公司", "impact": "刻蚀龙头"}
        ]},
        {"name": "半导体材料", "desc": "大硅片/光刻胶/前驱体/特种气体全面受益", "stocks": [
            {"code": "002409", "name": "雅克科技", "impact": "前驱体+光刻胶"},
            {"code": "688535", "name": "华海诚科", "impact": "先进封装材料"}
        ]},
        {"name": "存储芯片", "desc": "HBM需求爆发+国产替代，存储景气周期上行", "stocks": [
            {"code": "603986", "name": "兆易创新", "impact": "NOR Flash龙头"},
            {"code": "688008", "name": "澜起科技", "impact": "CXL/PCIe"}
        ]}
    ],
    midstream=[
        {"name": "晶圆代工", "desc": "台积电全球20座厂+华虹扩产，代工涨价周期开启", "stocks": [
            {"code": "688347", "name": "华虹宏力", "impact": "特色工艺龙头"},
            {"code": "688981", "name": "中芯国际", "impact": "先进制程龙头"}
        ]},
        {"name": "先进封装", "desc": "HPC/AI芯片需求驱动，先进封装成国产替代突破口", "stocks": [
            {"code": "600584", "name": "长电科技", "impact": "封测龙头"},
            {"code": "002156", "name": "通富微电", "impact": "AMD核心合作伙伴"}
        ]},
        {"name": "液冷散热", "desc": "高功耗芯片标配，政策+需求双轮驱动", "stocks": [
            {"code": "002837", "name": "英维克", "impact": "液冷龙头"},
            {"code": "300990", "name": "同飞股份", "impact": "高盈利质量"}
        ]}
    ],
    downstream=[
        {"name": "AI算力服务器", "desc": "AI大模型驱动算力需求持续爆发", "stocks": [
            {"code": "000977", "name": "浪潮信息", "impact": "服务器龙头"},
            {"code": "603019", "name": "中科曙光", "impact": "算力国家队"}
        ]},
        {"name": "云厂商/IDC", "desc": "数据中心建设加速，PUE要求驱动液冷渗透", "stocks": [
            {"code": "600845", "name": "宝信软件", "impact": "IDC龙头"},
            {"code": "300383", "name": "光环新网", "impact": "数据中心运营商"}
        ]},
        {"name": "PCB/铜箔", "desc": "AI服务器PCB需求高增，高端铜箔供不应求", "stocks": [
            {"code": "002463", "name": "沪电股份", "impact": "PCB龙头"},
            {"code": "301217", "name": "铜冠铜箔", "impact": "电子铜箔龙头"}
        ]}
    ]
)

# Step 4
gen.add_investment_opportunities(
    opportunities=[
        {
            "title": "液冷散热",
            "level": "S级",
            "logic": "七部门明确支持液冷散热技术创新推广，探索800V高压直流供电架构，推动超百千瓦单机柜部署。政策顶层设计确认液冷为算力基础设施标配，行业渗透率从2025年33%提升至2026年53%，未来三年CAGR 35%+。",
            "stocks": [
                {"code": "002837", "name": "英维克", "impact": "液冷龙头+全链条布局+深度绑定英伟达/英特尔"},
                {"code": "301018", "name": "申菱环境", "impact": "数据中心液冷订单同比增2.3倍"},
                {"code": "300990", "name": "同飞股份", "impact": "液冷毛利率高+现金流优异"}
            ]
        },
        {
            "title": "存储芯片/HBM",
            "level": "S级",
            "logic": "美光HBM4产能翻倍验证AI存储需求爆发；七部门明确高性能存储、存算一体为关键支撑技术；长江存储IPO已问询。HBM单价是DRAM的8-10倍，AI服务器单机HBM价值量持续攀升。",
            "stocks": [
                {"code": "688347", "name": "华虹宏力", "impact": "55亿扩产12英寸特色工艺+存储业务高增长"},
                {"code": "603986", "name": "兆易创新", "impact": "存储芯片设计龙头+NOR Flash全球前三"},
                {"code": "688008", "name": "澜起科技", "impact": "CXL3.2导入三星/SK海力士+PCIe Switch年内流片"}
            ]
        },
        {
            "title": "晶圆代工/先进封装",
            "level": "A级",
            "logic": "台积电全球近20座晶圆厂同步建设，设备采购需求30年未见；华虹宏力无锡三期扩产69.5亿美元；长电科技65亿定增扩产先进封装。晶圆代工涨价周期开启，8英寸已涨5-15%，12英寸成熟制程Q2-Q3跟进。",
            "stocks": [
                {"code": "600584", "name": "长电科技", "impact": "65亿定增+HPC/存储封测扩产"},
                {"code": "002156", "name": "通富微电", "impact": "AMD核心封测合作伙伴"},
                {"code": "002185", "name": "华天科技", "impact": "存储封测+先进封装布局"}
            ]
        },
        {
            "title": "半导体设备/材料",
            "level": "A级",
            "logic": "全球晶圆厂建设潮+国产替代加速，设备需求30年未见峰值；台积电设备采购从基准1倍上调至1.9倍；国内扩产+国产化率提升双轮驱动，设备材料企业订单饱满。",
            "stocks": [
                {"code": "688012", "name": "中微公司", "impact": "刻蚀设备龙头+CCP/ICP双平台"},
                {"code": "002371", "name": "北方华创", "impact": "平台型设备龙头+全产品线覆盖"},
                {"code": "688535", "name": "华海诚科", "impact": "先进封装材料+HBM Underfill"}
            ]
        }
    ],
    view_mode="card"
)

# Step 5
gen.add_catalyst_deep_analysis(
    events=[
        {
            "title": "七部门双化协同方案",
            "type": "policy",
            "description": "中央网信办等七部门联合印发《促进数字化绿色化协同转型发展实施方案（2026-2030年）》，明确存算一体、高性能存储、液冷散热、800V高压直流供电等为重点技术方向",
            "category": "政策催化",
            "three_d_heat": {"market_heat": 85, "policy_support": 95, "industry_fundamentals": 80},
            "swot": {
                "strengths": ["政策层级高（七部门联合）", "覆盖产业链全环节", "明确量化目标和时间表"],
                "weaknesses": ["政策落地需要时间", "部分技术仍处早期", "企业盈利兑现存在滞后"],
                "opportunities": ["液冷渗透率加速提升", "存储国产化替代加速", "算力基础设施投资加码"],
                "threats": ["AI需求不及预期", "行业竞争加剧毛利率下滑", "地缘政治风险"]
            },
            "scenarios": [
                {"name": "乐观情景", "probability": "30%", "description": "AI需求持续超预期+政策落地超预期，液冷/存储板块估值继续扩张，板块整体涨幅30%+", "impact": "强烈看多"},
                {"name": "中性情景", "probability": "50%", "description": "政策按预期推进+业绩逐步兑现，板块震荡上行，龙头企业收益显著", "impact": "看多"},
                {"name": "悲观情景", "probability": "20%", "description": "AI资本开支放缓+宏观经济承压，板块回调20%以上", "impact": "谨慎"}
            ]
        },
        {
            "title": "华虹宏力55亿扩产",
            "type": "industry",
            "description": "华虹宏力拟将超募资金及结余募资合计55.56亿元投向无锡三期项目，总投资69.5亿美元，建月产能5.5万片12英寸特色工艺产线",
            "category": "产业催化",
            "three_d_heat": {"market_heat": 75, "policy_support": 85, "industry_fundamentals": 90},
            "swot": {
                "strengths": ["产能持续满载（利用率102.8%）", "特色工艺领域龙头", "国产替代受益者"],
                "weaknesses": ["先进制程差距较大", "折旧压力大", "毛利率低于行业龙头"],
                "opportunities": ["8英寸转单效应", "AI Power需求爆发", "存储业务高速增长"],
                "threats": ["行业周期下行风险", "美国出口管制", "扩产进度不及预期"]
            },
            "scenarios": [
                {"name": "乐观情景", "probability": "35%", "description": "晶圆代工涨价超预期+产能快速爬坡，2027年盈利大幅增长", "impact": "强烈看多"},
                {"name": "中性情景", "probability": "45%", "description": "扩产按计划推进+价格温和上涨，业绩稳步增长", "impact": "看多"},
                {"name": "悲观情景", "probability": "20%", "description": "行业景气度下行+价格回落，短期业绩承压", "impact": "谨慎"}
            ]
        },
        {
            "title": "美光HBM4产能翻倍",
            "type": "overseas",
            "description": "美光宣布年底前将12层HBM4月产能从5万片扩至6万片，AI存储需求持续超预期，美股盘前涨1.89%",
            "category": "海外催化",
            "three_d_heat": {"market_heat": 90, "policy_support": 70, "industry_fundamentals": 95},
            "swot": {
                "strengths": ["AI需求持续爆发", "HBM技术壁垒高", "量价齐升格局"],
                "weaknesses": ["扩产需要时间", "技术迭代风险", "客户集中度高"],
                "opportunities": ["HBM价值量持续提升", "国产替代空间大", "产业链整体受益"],
                "threats": ["AI需求阶段性见顶", "行业竞争加剧", "地缘政治影响供应链"]
            },
            "scenarios": [
                {"name": "乐观情景", "probability": "40%", "description": "AI算力需求持续超预期，HBM价格继续上涨，存储板块全面爆发", "impact": "强烈看多"},
                {"name": "中性情景", "probability": "45%", "description": "需求稳步增长+产能逐步释放，板块震荡上行", "impact": "看多"},
                {"name": "悲观情景", "probability": "15%", "description": "AI需求放缓+产能过剩，价格战开启", "impact": "谨慎"}
            ]
        }
    ]
)

# Step 6: 持仓影响
stocks_data = [
    {"code": "002837", "name": "英维克", "impact": "利空（板块情绪+估值压力）"},
    {"code": "301217", "name": "铜冠铜箔", "impact": "中性偏多（PCB需求链受益）"},
    {"code": "002409", "name": "雅克科技", "impact": "偏多（半导体材料+国产替代）"},
    {"code": "002789", "name": "*ST建艺", "impact": "无直接关联（重组主题）"}
]

portfolio_analysis = f"""
<div style="background: linear-gradient(135deg, rgba(59,130,246,0.10) 0%, rgba(139,92,246,0.08) 100%); 
            border-radius: 14px; padding: 20px; border: 1px solid rgba(96,165,250,0.25);">
    <div style="display: flex; align-items: center; margin-bottom: 16px;">
        <div style="width: 36px; height: 36px; background: linear-gradient(135deg, #8b5cf6 0%, #3b82f6 100%); 
                    border-radius: 10px; display: flex; align-items: center; justify-content: center; margin-right: 12px;">
            💼
        </div>
        <span style="font-size: 16px; font-weight: 700; color: #a5b4fc;">持仓影响评估</span>
    </div>
    
    <div style="margin-bottom: 12px;">
        <div style="font-size: 12px; color: #94a3b8; margin-bottom: 8px;">核心持仓标的</div>
        {StockTags(stocks_data).render()}
    </div>
    
    <div style="font-size: 13px; color: #cbd5e1; line-height: 1.9; margin-top: 16px;">
        <strong style="color: #f87171;">🔴 英维克（-6.69%）：</strong>液冷板块调整延续，中报增收不增利引发市场对盈利兑现的担忧。七部门政策利好液冷长期逻辑，但短期估值压力仍存（PE 166倍）。<strong>建议：</strong>持仓观望，55-60元区间可考虑分批低吸，止损位50元。
        <br><br>
        <strong style="color: #fbbf24;">🟡 铜冠铜箔（-3.79%）：</strong>随电子板块回调，PCB铜箔需求逻辑未变，AI服务器PCB高端铜箔仍是高景气赛道。<strong>建议：</strong>持有观察，95-100元支撑位附近可考虑加仓。
        <br><br>
        <strong style="color: #34d399;">🟢 雅克科技（-3.78%）：</strong>半导体材料龙头直接受益于国产替代加速和晶圆厂扩产，HBM前驱体、光刻胶等核心产品需求持续增长。PE 53.7倍在半导体材料板块中处于合理区间。<strong>建议：</strong>持有，115-120元可加仓。
        <br><br>
        <strong style="color: #a78bfa;">🟣 *ST建艺（+8.75%）：</strong>与本次催化无直接关联，尾盘拉升主要受重组预期驱动。ST板块整体活跃（159涨/29跌），该股作为建筑装饰重整标的有独立行情。<strong>建议：</strong>持有，关注重整进展。
    </div>
</div>
"""

section = Section(title="💼 持仓影响评估", content=portfolio_analysis, icon="briefcase", variant="highlight")
gen._components.append(section)

# Step 7: 隔夜外盘
overseas_content = """
<div style="background: linear-gradient(135deg, rgba(16,185,129,0.10) 0%, rgba(59,130,246,0.08) 100%); 
            border-radius: 14px; padding: 20px; border: 1px solid rgba(16,185,129,0.25);">
    <div style="display: flex; align-items: center; margin-bottom: 16px;">
        <div style="width: 36px; height: 36px; background: linear-gradient(135deg, #10b981 0%, #3b82f6 100%); 
                    border-radius: 10px; display: flex; align-items: center; justify-content: center; margin-right: 12px;">
            🌍
        </div>
        <span style="font-size: 16px; font-weight: 700; color: #6ee7b7;">隔夜外盘动态（截至北京时间20:00）</span>
    </div>
    
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px;">
        <div style="background: rgba(255,255,255,0.05); border-radius: 10px; padding: 14px;">
            <div style="font-size: 12px; color: #94a3b8; margin-bottom: 8px;">📈 美股指数</div>
            <div style="font-size: 13px; color: #e2e8f0; line-height: 1.8;">
                • 纳指100期货：<span style="color: #4ade80;">+0.50%</span><br>
                • 标普500期货：<span style="color: #4ade80;">+0.06%</span><br>
                • 道指期货：<span style="color: #f87171;">-0.09%</span><br>
                • 10年美债收益率：4.77%
            </div>
        </div>
        
        <div style="background: rgba(255,255,255,0.05); border-radius: 10px; padding: 14px;">
            <div style="font-size: 12px; color: #94a3b8; margin-bottom: 8px;">💾 半导体核心标的</div>
            <div style="font-size: 13px; color: #e2e8f0; line-height: 1.8;">
                • 英伟达 NVDA：<span style="color: #4ade80;">+1.22%</span> $231.23<br>
                • 美光 MU：<span style="color: #4ade80;">+1.89%</span> $976.30<br>
                • SOXL半导体ETF：<span style="color: #4ade80;">+5.40%</span><br>
                • 台积电 ADR：前日<span style="color: #4ade80;">+0.36%</span>
            </div>
        </div>
    </div>
    
    <div style="margin-top: 12px; background: rgba(255,255,255,0.05); border-radius: 10px; padding: 14px;">
        <div style="font-size: 12px; color: #94a3b8; margin-bottom: 8px;">📰 重要海外消息</div>
        <div style="font-size: 13px; color: #cbd5e1; line-height: 1.9;">
            1️⃣ <strong>美光宣布HBM4扩产</strong>：年底前将12层HBM4月产能从约5万片提升至6万片，AI存储需求持续爆发 <span style="color: #4ade80;">[利好]</span><br>
            2️⃣ <strong>Anthropic冲刺IPO</strong>：拟将信贷额度扩至150亿美元，IPO估值或达2万亿美元，超SpaceX <span style="color: #4ade80;">[利好AI]</span><br>
            3️⃣ <strong>特朗普拟加征半导体关税</strong>：新关税框架可能扩大至芯片下游产品，豁免与美本土投资挂钩 <span style="color: #f87171;">[中性偏空]</span><br>
            4️⃣ <strong>韩美半导体关税磋商</strong>：韩方称美方未提时间表，韩国不会在竞争中处于不利地位 <span style="color: #fbbf24;">[中性]</span><br>
            5️⃣ <strong>意大利推半导体激励</strong>：批准税收优惠和快速审批程序，吸引半导体厂商投资 <span style="color: #4ade80;">[利好]</span>
        </div>
    </div>
</div>
"""

section2 = Section(title="🌍 隔夜外盘跟踪", content=overseas_content, icon="globe", variant="highlight")
gen._components.append(section2)

# Step 8
gen.add_risk_warning([
    "AI算力需求阶段性不及预期，导致半导体/液冷板块回调风险",
    "美联储9月加息不确定性，关注本周五非农数据",
    "美国对华半导体出口管制可能进一步升级",
    "持仓股英维克估值偏高（PE 166倍），盈利兑现低于预期可能引发估值回归",
    "液冷行业竞争加剧，价格战导致毛利率下滑风险",
    "华虹宏力扩产进度、产能爬坡存在不确定性"
])

# Step 9
gen.add_investment_strategy(
    strategy="""
    <strong>【总体策略】三重催化共振，AI算力基础设施长逻辑强化，回调即是布局机会</strong><br><br>
    
    <strong>仓位建议：</strong>科技成长仓位维持6-7成，利用回调分批加仓核心主线标的<br><br>
    
    <strong>操作策略：</strong><br>
    1. <strong>液冷板块</strong>：短期情绪承压但长期逻辑不变，英维克在55-60元区间可考虑分批低吸，止损位50元；关注同飞股份等高盈利质量标的<br>
    2. <strong>存储/HBM</strong>：美光产能翻倍验证需求爆发，国产存储链持续受益，建议配置雅克科技（材料）+ 兆易创新（设计）+ 澜起科技（CXL）组合<br>
    3. <strong>先进封装</strong>：长电科技65亿定增扩产，先进封装是国产替代重要突破口，回调可加仓<br>
    4. <strong>半导体设备/材料</strong>：全球晶圆厂建设潮+国产替代双轮驱动，逢低布局北方华创、中微公司、华海诚科<br><br>
    
    <strong>重点关注：</strong><br>
    • 本周五美国8月非农数据（决定美联储9月加息路径）<br>
    • 长江存储IPO进展（国产存储核心催化）<br>
    • 三季报预告窗口期（业绩验证期，关注盈利兑现标的）<br><br>
    
    <strong>风险控制：</strong>单一个股仓位不超过20%，严格执行止损纪律，高位股反弹分批减仓
    """
)

# Step 10: Publish
result = gen.publish(
    title="S级催化：七部门双化协同+华虹55亿扩产+美光HBM4翻倍",
    filename="20260904_盘后_S级催化扫描_七部门双化协同+华虹55亿扩产+美光HBM4翻倍.html",
    excerpt="9月4日盘后三重催化共振：七部门印发双化协同方案明确液冷/存储方向、华虹宏力55.56亿加码无锡三期12英寸产线、美光HBM4产能翻倍。"
)

print("发布结果:", result)
