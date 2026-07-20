#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S级催化扫描 - 20260721 盘前
核心催化：美股芯片暴力反弹 + 国内政策组合拳内外共振
"""
import sys, os
sys.path.insert(0, '/root/daily-news-insight/v3')
os.chdir('/root/daily-news-insight')

from v3.generators.s_level_catalyst import SLevelCatalystGenerator
from v3.components.layout import Section

gen = SLevelCatalystGenerator(
    date_str="20260721",
    catalyst_title="芯片股暴力反弹+政策组合拳 内外共振",
    subtitle="2026.07.21 · 盘前S级催化"
)

# ===== 1. 催化概述 =====
gen.add_catalyst_overview(
    overview="隔夜美股芯片股集体暴力反弹，费城半导体指数开盘涨2%、盘中涨超3%，存储芯片板块领涨（闪迪+6%、美光+5%、AMD/英特尔+5%），"
             "结束连续数日的技术性熊市调整。与此同时，国内政策面打出组合拳：国务院部署'六张网'万亿基建投资、两大央企（国新+诚通）合计600亿真金白银增持、"
             "证监会召开投资者座谈会全力维稳、央行维持流动性宽松。内外双重利好共振，A股科技成长赛道有望迎来超跌反弹窗口。"
)

# ===== 2. 隔夜外盘扫描模块 =====
overnight_html = """
<div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 12px; margin-bottom: 16px;">
    <div style="background: linear-gradient(135deg, rgba(34,197,94,0.15) 0%, rgba(22,163,74,0.08) 100%); 
                border-radius: 12px; padding: 16px; border: 1px solid rgba(34,197,94,0.25); text-align: center;">
        <div style="font-size: 12px; color: #86efac; margin-bottom: 4px;">费城半导体 (SOX)</div>
        <div style="font-size: 20px; font-weight: 700; color: #4ade80;">+3.2%</div>
        <div style="font-size: 11px; color: #6b7280; margin-top: 2px;">11,959点 · 反弹</div>
    </div>
    <div style="background: linear-gradient(135deg, rgba(34,197,94,0.15) 0%, rgba(22,163,74,0.08) 100%); 
                border-radius: 12px; padding: 16px; border: 1px solid rgba(34,197,94,0.25); text-align: center;">
        <div style="font-size: 12px; color: #86efac; margin-bottom: 4px;">英伟达 NVDA</div>
        <div style="font-size: 20px; font-weight: 700; color: #4ade80;">+2.1%</div>
        <div style="font-size: 11px; color: #6b7280; margin-top: 2px;">$205 · 温和反弹</div>
    </div>
    <div style="background: linear-gradient(135deg, rgba(34,197,94,0.15) 0%, rgba(22,163,74,0.08) 100%); 
                border-radius: 12px; padding: 16px; border: 1px solid rgba(34,197,94,0.25); text-align: center;">
        <div style="font-size: 12px; color: #86efac; margin-bottom: 4px;">美光科技 MU</div>
        <div style="font-size: 20px; font-weight: 700; color: #4ade80;">+5.2%</div>
        <div style="font-size: 11px; color: #6b7280; margin-top: 2px;">$880 · 存储领涨</div>
    </div>
    <div style="background: linear-gradient(135deg, rgba(34,197,94,0.15) 0%, rgba(22,163,74,0.08) 100%); 
                border-radius: 12px; padding: 16px; border: 1px solid rgba(34,197,94,0.25); text-align: center;">
        <div style="font-size: 12px; color: #86efac; margin-bottom: 4px;">台积电 TSM</div>
        <div style="font-size: 20px; font-weight: 700; color: #4ade80;">+2.6%</div>
        <div style="font-size: 11px; color: #6b7280; margin-top: 2px;">$403 · Q2业绩超预期</div>
    </div>
</div>

<div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 12px; margin-bottom: 16px;">
    <div style="background: linear-gradient(135deg, rgba(34,197,94,0.12) 0%, rgba(22,163,74,0.06) 100%); 
                border-radius: 10px; padding: 12px; border: 1px solid rgba(34,197,94,0.2);">
        <div style="font-size: 12px; color: #6b7280; margin-bottom: 4px;">应用材料 AMAT</div>
        <div style="font-size: 18px; font-weight: 700; color: #4ade80;">+1.4%</div>
    </div>
    <div style="background: linear-gradient(135deg, rgba(239,68,68,0.12) 0%, rgba(220,38,38,0.06) 100%); 
                border-radius: 10px; padding: 12px; border: 1px solid rgba(239,68,68,0.2);">
        <div style="font-size: 12px; color: #6b7280; margin-bottom: 4px;">科磊 KLAC</div>
        <div style="font-size: 18px; font-weight: 700; color: #f87171;">-0.4%</div>
    </div>
    <div style="background: linear-gradient(135deg, rgba(239,68,68,0.12) 0%, rgba(220,38,38,0.06) 100%); 
                border-radius: 10px; padding: 12px; border: 1px solid rgba(239,68,68,0.2);">
        <div style="font-size: 12px; color: #6b7280; margin-bottom: 4px;">泛林 LRCX</div>
        <div style="font-size: 18px; font-weight: 700; color: #f87171;">-0.4%</div>
    </div>
    <div style="background: linear-gradient(135deg, rgba(34,197,94,0.12) 0%, rgba(22,163,74,0.06) 100%); 
                border-radius: 10px; padding: 12px; border: 1px solid rgba(34,197,94,0.2);">
        <div style="font-size: 12px; color: #6b7280; margin-bottom: 4px;">阿斯麦 ASML</div>
        <div style="font-size: 18px; font-weight: 700; color: #4ade80;">+2.5%</div>
    </div>
</div>

<div style="background: rgba(15,23,42,0.6); border-radius: 10px; padding: 14px; border: 1px solid rgba(71,85,105,0.3);">
    <div style="font-size: 13px; color: #94a3b8; line-height: 1.9;">
        <strong style="color: #e2e8f0;">📊 隔夜外盘核心要点：</strong><br>
        • <strong style="color: #4ade80;">存储芯片领涨</strong>：闪迪(SNDK)+6%、美光(MU)+5%、AMD+5%、英特尔(INTC)+5%，是本轮反弹最强方向<br>
        • <strong style="color: #fbbf24;">设备股分化</strong>：应用材料(AMAT)+1.4%，科磊(KLAC)/泛林(LRCX)微跌-0.4%，设备端反弹力度弱于设计/存储<br>
        • <strong style="color: #60a5fa;">整体情绪修复</strong>：阿斯麦(ASML)+2.5%，台积电(TSM)+2.6%，博通(AVGO)+2.1%<br>
        • <strong style="color: #a78bfa;">催化剂</strong>：谷歌正在研发AI新芯片的消息提振市场信心，云计算服务商概念股全线反弹（Hut 8、IREN +10%）<br>
        • <strong style="color: #f97316;">大宗商品</strong>：WTI原油回落至81美元（-0.9%），地缘紧张有缓和迹象；黄金4010美元震荡<br>
        • <strong style="color: #22d3ee;">韩国/亚洲</strong>：SK海力士美股涨超4%，三星电子随板块反弹
    </div>
</div>
"""

overnight_section = Section(title="🌍 隔夜全球市场扫描", content=overnight_html, icon="globe")
gen._components.insert(1, overnight_section)

# ===== 3. 催化详解 =====
gen.add_catalyst_details(
    background=(
        "7月以来A股科技成长赛道经历剧烈调整，半导体、光模块、PCB等AI硬件板块普遍回调20%-30%，"
        "费城半导体指数从6月高点累计下跌超20%进入技术性熊市。核心原因包括："
        "① 台积电Q2业绩虽超预期但市场担忧AI资本开支见顶；"
        "② 月之暗面Kimi K3发布引发AI算力需求担忧；"
        "③ A股中报季资金从高位成长股转向防御板块避险；"
        "④ 融资盘去杠杆导致踩踏式下跌。"
        "截至7月20日，A股单日超200只个股跌停，市场情绪极度悲观。"
    ),
    trigger=(
        "隔夜多重信号形成底部共振：\n"
        "【外盘】美股芯片股集体反弹，SOX指数涨超3%，存储芯片领涨——闪迪+6%、美光科技+5%、AMD+5%、英特尔+5%、"
        "英伟达+2%、台积电+2.6%、阿斯麦+2.5%。市场对AI需求的担忧阶段性缓和。\n"
        "【政策】国务院常务会议部署'六张网'万亿基建，涵盖算力网、新型电力网、新一代通信网等，直接利好算力硬件产业链。\n"
        "【资金】中国国新已动用超500亿+诚通近百亿，两大央企合计600亿增持央企与科技标的，并承诺继续增持。\n"
        "【监管】证监会召开投资者座谈会，吴清强调全力维护市场平稳运行，拟优化两融规则、限制减持、引导中长期资金入市。\n"
        "【产业】台积电Q2业绩超预期，净利润暴增77%，上调全年资本支出至600-640亿美元，AI需求结构性增长逻辑未破。"
    )
)

# ===== 4. 产业链分析 =====
gen.add_industry_chain_analysis(
    upstream=[
        {
            "name": "半导体材料",
            "desc": "光刻胶/前驱体/电子特气，国产替代加速",
            "stocks": [
                {"code": "002409", "name": "雅克科技", "impact": "半导体材料平台龙头"},
                {"code": "688535", "name": "华海诚科", "impact": "存储封装材料"},
                {"code": "300054", "name": "鼎龙股份", "impact": "CMP抛光垫+光刻胶"},
            ]
        },
        {
            "name": "铜箔/CCL",
            "desc": "AI服务器高频高速材料，短期超跌严重",
            "stocks": [
                {"code": "301217", "name": "铜冠铜箔", "impact": "高频高速铜箔龙头"},
                {"code": "688519", "name": "南亚新材", "impact": "高端CCL"},
            ]
        },
        {
            "name": "石英材料",
            "desc": "半导体+光伏双需求驱动",
            "stocks": [
                {"code": "300395", "name": "菲利华", "impact": "石英材料龙头"},
                {"code": "603688", "name": "石英股份", "impact": "高纯石英砂"},
            ]
        },
    ],
    midstream=[
        {
            "name": "晶圆代工",
            "desc": "成熟制程受益于国内AI芯片需求",
            "stocks": [
                {"code": "688981", "name": "中芯国际", "impact": "大陆晶圆代工龙头"},
                {"code": "688347", "name": "华虹公司", "impact": "特色工艺代工"},
            ]
        },
        {
            "name": "封装测试",
            "desc": "先进封装是AI芯片产能瓶颈",
            "stocks": [
                {"code": "600584", "name": "长电科技", "impact": "封测龙头"},
                {"code": "002156", "name": "通富微电", "impact": "AMD核心封测伙伴"},
            ]
        },
        {
            "name": "半导体设备",
            "desc": "国产替代+扩产周期双驱动",
            "stocks": [
                {"code": "002371", "name": "北方华创", "impact": "设备平台龙头"},
                {"code": "688012", "name": "中微公司", "impact": "刻蚀设备龙头"},
            ]
        },
    ],
    downstream=[
        {
            "name": "AI算力芯片",
            "desc": "AI芯片需求持续高增长",
            "stocks": [
                {"code": "688256", "name": "寒武纪", "impact": "国产AI芯片龙头"},
                {"code": "NVDA", "name": "英伟达", "impact": "全球AI芯片霸主"},
            ]
        },
        {
            "name": "液冷散热",
            "desc": "算力密度提升核心受益",
            "stocks": [
                {"code": "002837", "name": "英维克", "impact": "液冷散热龙头"},
                {"code": "301018", "name": "申菱环境", "impact": "数据中心温控"},
            ]
        },
        {
            "name": "光模块/CPO",
            "desc": "800G/1.6T升级周期",
            "stocks": [
                {"code": "300308", "name": "中际旭创", "impact": "光模块全球龙头"},
                {"code": "300502", "name": "新易盛", "impact": "中报预增77%-103%"},
            ]
        },
    ]
)

# ===== 5. 投资机会 =====
gen.add_investment_opportunities([
    {
        "name": "存储芯片超跌反弹",
        "priority": "高",
        "stocks": [
            {"code": "301217", "name": "铜冠铜箔", "impact": "中报预增486%-544%，20CM跌停后情绪修复弹性大"},
            {"code": "688535", "name": "华海诚科", "impact": "存储封装材料龙头，回调50%后估值性价比凸显"},
            {"code": "002409", "name": "雅克科技", "impact": "半导体材料平台型公司，融资盘去杠杆接近尾声"},
        ],
        "logic": "隔夜美股存储芯片领涨（闪迪+6%、美光+5%），国内存储板块前期跌幅巨大，技术面超跌+基本面验证（中报预增）+外盘情绪修复，三重共振下反弹弹性最大。"
    },
    {
        "name": "算力基建（六张网政策催化）",
        "priority": "高",
        "stocks": [
            {"code": "002837", "name": "英维克", "impact": "液冷散热龙头，算力网建设直接受益"},
            {"code": "300308", "name": "中际旭创", "impact": "光模块龙头，新易盛中报预增验证行业景气"},
            {"code": "000977", "name": "浪潮信息", "impact": "服务器龙头，算力基建核心标的"},
        ],
        "logic": "国务院'六张网'规划将算力网列为首要建设方向，叠加工信部推动算力市场化定价标准，算力基础设施建设有望加速。"
    },
    {
        "name": "半导体设备/材料（国产替代）",
        "priority": "中",
        "stocks": [
            {"code": "002371", "name": "北方华创", "impact": "设备龙头，国产替代核心标的"},
            {"code": "688012", "name": "中微公司", "impact": "刻蚀设备龙头，受益于扩产周期"},
            {"code": "300655", "name": "晶瑞电材", "impact": "光刻胶国产替代加速"},
        ],
        "logic": "台积电上调资本支出验证全球半导体扩产周期延续，国内设备国产化率持续提升，政策+产业双轮驱动。"
    },
])

# ===== 6. 催化深度分析（Skill增强） =====
gen.add_catalyst_deep_analysis([
    {
        "title": "美股芯片反弹持续性评估",
        "type": "外盘反弹",
        "description": "费城半导体指数单日反弹3%，存储领涨，但SOX已从高点跌20%+，此次反弹是技术反抽还是趋势反转？",
        "category": "国际市场"
    },
    {
        "title": "国内政策组合拳力度研判",
        "type": "政策催化",
        "description": "国务院六张网+央企600亿增持+证监会维稳+央行流动性，政策底是否已经出现？",
        "category": "国内政策"
    },
    {
        "title": "AI硬件赛道中期趋势判断",
        "type": "产业趋势",
        "description": "经历本轮深度调整后，AI算力产业链是否还能成为下半年最强主线？",
        "category": "产业趋势"
    },
])

# ===== 7. 风险提示 =====
gen.add_risk_warning([
    "本次反弹性质仍需观察：美股芯片股反弹可能仅为技术反抽，SOX指数已进入技术性熊市，中期趋势是否反转需连续验证",
    "国内政策底不等于市场底：历史上政策底后往往还有市场底，不宜盲目抄底满仓",
    "铜冠铜箔中报预增但环比走弱（Q2净利润环比下滑），需警惕业绩增速不及预期的风险",
    "融资盘去杠杆尚未结束：雅克科技等个股融资余额仍处高位（27.57亿，占流通市值4%，90%分位），不排除后续被动平仓压力",
    "美联储9月加息概率超80%，全球流动性收紧预期仍存，外资可能继续流出",
    "*ST建艺基本面恶化（一季度亏损5300万，负债率94%），ST股风险极高，不建议参与"
])

# ===== 8. 投资策略 =====
gen.add_investment_strategy(
    strategy="""
<strong style="color: #fbbf24;">【总体判断】</strong>内外双重利好共振下，A股科技成长板块有望迎来超跌反弹窗口。
但需明确：当前仍定义为<strong style="color: #f87171;">熊市中的反弹</strong>而非反转，操作上应以<strong style="color: #4ade80;">反弹减仓、控制仓位</strong>为主基调。

<br><br>

<strong style="color: #60a5fa;">【持仓操作指引】</strong><br>
• <strong>英维克(002837)</strong>：液冷龙头，算力网政策直接受益。若今日反弹至5日线附近，可考虑减持1/3仓位锁定利润；
  若低开则持有观望，不建议加仓。估值锚：2026年PE约35-40倍，处于合理区间。<br>
• <strong>铜冠铜箔(301217)</strong>：中报预增486%但昨日20CM跌停，今日大概率随板块反弹。
  注意：Q2净利润环比Q1下滑（Q1 1.06亿 vs Q2 0.99-1.19亿），属于<strong style="color: #f87171;">利好兑现+环比走弱</strong>的典型杀估值。
  反弹建议减仓至底仓，不抄底。估值锚：200倍PE仍处历史极高位，估值透支严重。<br>
• <strong>雅克科技(002409)</strong>：半导体材料平台型公司，融资余额仍处高位（27.57亿，占流通市值4%，90%分位），
  去杠杆压力仍存。反弹至10日线减仓，不破前低可持有观察。估值锚：2026年PE约30倍，材料股合理。<br>
• <strong>*ST建艺(002789)</strong>：昨日跌停，基本面恶化严重（负债率94%，持续亏损），
  属于<strong style="color: #f87171;">高风险标的</strong>，建议趁反弹尽快清仓，不抱侥幸。

<br><br>

<strong style="color: #a78bfa;">【交易策略】</strong><br>
1. <strong>仓位控制</strong>：整体仓位维持5成以下，反弹不加仓，逢高减仓<br>
2. <strong>方向选择</strong>：优先关注存储芯片（外盘领涨+超跌最严重）和算力基建（政策直接催化）<br>
3. <strong>止盈止损</strong>：反弹至5日线减1/3，至10日线再减1/3，跌破前低止损<br>
4. <strong>抄底时机</strong>：等待成交量萎缩至地量+融资余额明显下降后再考虑左侧布局
"""
)

# ===== 验证 =====
errors = gen.validate()
print("验证结果:", errors if errors else "✅ 无错误")

# ===== 发布 =====
result = gen.publish(
    title="S级催化·芯片反弹+政策共振",
    filename="20260721_盘前_S级催化扫描_芯片反弹政策组合拳共振",
    excerpt="隔夜美股芯片股暴力反弹+国内政策组合拳（万亿基建+600亿增持+证监会维稳），内外共振下超跌反弹窗口开启。含隔夜外盘全扫描、产业链机会、持仓操作指引。"
)
print("发布结果:", result)
