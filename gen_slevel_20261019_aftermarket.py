#!/usr/bin/env python3
"""
S级催化扫描 - 2026年10月19日 盘后
核心催化：英伟达GTC柏林大会前夕+NVHBM统一标准+人形机器人政策双重催化+美股半导体超跌反弹
V3.0 SLevelCatalystGenerator
"""
import sys, os
os.chdir('/root/daily-news-insight')
sys.path.insert(0, '/root/daily-news-insight')
sys.path.insert(0, '/root/daily-news-insight/v3')

from v3.generators.s_level_catalyst import SLevelCatalystGenerator
from v3.components.layout import Section, SubCard, SplitLayout, CardGrid, Card
from v3.components.data import StockTags, KeyPoints, DataGrid, DataCard, ProgressBar, Badge, CompareTable, Tabs, StatCard
from v3.components.special import RiskAlert, QuoteBlock

gen = SLevelCatalystGenerator(
    date_str="20261019",
    catalyst_title="英伟达GTC大会前夕+NVHBM统一标准+人形机器人政策双S级催化",
    subtitle="2026.10.19 · 盘后S级催化"
)

# === 1. 催化事件概述 ===
gen.add_catalyst_overview(
    overview="""
    <p><strong>10月19日盘后双S级催化共振：AI算力+人形机器人两大主线同时迎来重磅利好：</strong></p>
    <ol>
        <li><strong>催化一：英伟达GTC柏林大会前夕，NVHBM统一标准重磅落地</strong>。三星电子将采用台积电3纳米工艺生产英伟达下一代定制HBM（NVHBM）基础裸片，英伟达要求三星、SK海力士、美光三大供应商均采用台积电3nm工艺+1c DRAM工艺统一标准。这是HBM历史上首次跨厂商统一制造标准，意义堪比"安卓统一生态"。</li>
        <li><strong>催化二：人形机器人政策双响炮，需求侧空间打开</strong>。商务部等9部门发布《科技兴商意见》，首次从消费端推动机器人落地（家庭服务+商贸物流）；市场监管总局发布首批6项人形机器人国家标准（2027年4月实施）。宇树科技大涨16.15%，市值重回2000亿。</li>
        <li><strong>催化三：美股半导体超跌反弹，纳指期货涨1.3%</strong>。费城半导体8连跌后迎来修复，英特尔涨4%（摩根大通上调评级）、美光涨2.4%、英伟达涨1.3%、台积电ADR涨1.8%。黄仁勋GTC演讲+科技巨头财报周开启。</li>
        <li><strong>催化四：长鑫科技前三季净利超1300亿，存储业绩兑现</strong>。Q3收入环比+15-20%，虽增速放缓但绝对值惊人，回购10-20亿元。立昂微前三季扭亏为盈，验证半导体硅片复苏。</li>
        <li><strong>持仓股今日表现</strong>：英维克44.46元(-0.54%)、铜冠铜箔84.77元(-0.76%)、雅克科技96.11元(-1.94%)、*ST建艺13.25元(-9.31%，ST建艺跌停需警惕)。</li>
    </ol>
    <p><strong>核心判断：</strong>今日双S级催化——AI算力（NVHBM统一标准+GTC前夕）和人形机器人（政策+国标）——均为中期级别利好，非短期情绪炒作。NVHBM统一标准标志着HBM从"各家自造"进入"产业标准化"阶段，加速放量；人形机器人首次从消费端打开需求空间，政策级别升级。明日半导体+机器人板块有望共振反弹。但*ST建艺跌停属基本面利空，需严格止损。</p>
    """,
    importance="S级"
)

gen.add_catalyst_details(
    background="""
    <p><strong>背景一：费城半导体8连跌后技术超卖</strong>。受AI估值担忧、CoreWeave债务风险、对冲基金连续5日净卖出AI股等因素影响，费城半导体指数连跌8日（追平2006年以来最长连跌纪录）。技术面严重超卖，反弹一触即发。</p>
    <p><strong>背景二：GTC大会是英伟达下半年最重要的技术与生态大会</strong>。本届大会重心从"卖GPU"进一步推向"卖AI工厂"，聚焦智能体AI(Agentic AI)、物理AI(Physical AI)、机器人、AI基础设施。黄仁勋将于10月21日发表主题演讲，德国总理默茨将与黄仁勋会面。</p>
    <p><strong>背景三：人形机器人产业加速从"才艺展示"迈向"真实作业"</strong>。特斯拉Optimus量产在即，国内头部企业产品从科研向工业/商业场景转移。此前政策多集中在产业侧，此次9部门意见首次从促消费、商贸流通角度为机器人打开需求侧空间。</p>
    <p><strong>背景四：半导体业绩分化，真金不怕火炼</strong>。长鑫科技前三季净利1310-1325亿（去年同期亏损52.8亿），源杰科技Q3净利同比+579%~660%，立昂微扭亏为盈。AI算力产业链的业绩兑现正在验证。</p>
    """,
    trigger="""
    <p><strong>触发因素一：NVHBM统一标准——HBM产业的"安卓时刻"</strong>。英伟达要求三星、SK海力士、美光三大HBM供应商的NVHBM产品，基础裸片统一采用台积电3nm工艺，核心裸片统一采用1c DRAM工艺。这是HBM历史上首次跨厂商统一制造标准，将大幅提升良率、降低验证成本、加速HBM4E放量。</p>
    <p><strong>触发因素二：9部门联合发布《科技兴商意见》</strong>。商务部等9部门10月19日发布，提出推动具身智能技术在商贸领域落地，拓展家庭服务、商贸物流等应用场景，培育机器人陪伴等智能服务新业态。首次从需求侧政策支持机器人。</p>
    <p><strong>触发因素三：首批6项人形机器人国家标准发布</strong>。市场监管总局10月15日批准发布，包括5项技术要求系列标准+《人形机器人仿真测试平台技术规范》，2027年4月1日实施。行业标准统一，加速产业化。</p>
    <p><strong>触发因素四：美股半导体超跌反弹</strong>。纳指100期货涨1.3%，英特尔涨4%（摩根大通从减持上调至中性）、美光涨2.4%、SK海力士涨3.9%、博通涨2.2%。8连跌后技术修复+GTC预期+财报季催化。</p>
    <p><strong>触发因素五：长鑫科技前三季净利1310亿+回购20亿</strong>。验证存储超级周期业绩兑现，董事长提议回购10-20亿元，显示对未来信心。</p>
    """
)

# === 3. 隔夜外盘跟踪（V4.0强制覆盖） ===
gen._components.append(Section(
    title="🌍 隔夜外盘跟踪（V4.0强制覆盖）",
    icon="globe",
    content=DataGrid(cards=[
        DataCard(title="道指期货", value="微跌", subtitle="道指上周五-0.34%", trend="-0.16%", trend_up=False, variant="warning"),
        DataCard(title="纳指100期货", value="涨1.3%", subtitle="超跌反弹", trend="+1.3%", trend_up=True, variant="success"),
        DataCard(title="标普500期货", value="涨0.5%", subtitle="温和反弹", trend="+0.5%", trend_up=True, variant="success"),
        DataCard(title="费城半导体", value="8连跌", subtitle="追平2006年纪录", trend="-3.83%(上周五)", trend_up=False, variant="danger"),
        DataCard(title="英伟达", value="涨1.33%", subtitle="GTC前夕+NVHBM", trend="+1.33%", trend_up=True, variant="success"),
        DataCard(title="美光科技", value="涨2.41%", subtitle="存储修复", trend="+2.41%", trend_up=True, variant="success"),
    ]).render() + """
    <div style="margin-top: 16px;">
        <div style="background: rgba(59,130,246,0.08); border: 1px solid rgba(59,130,246,0.25); border-radius: 14px; padding: 16px;">
            <div style="font-size: 14px; font-weight: 700; color: #60a5fa; margin-bottom: 10px;">📰 外盘核心要点（截至10月19日20:00）</div>
            <div style="font-size: 13px; color: #bfdbfe; line-height: 1.8;">
                <p><strong>1. 8连跌后半导体股超跌反弹</strong>：费城半导体上周五跌3.83%（8连跌，追平2006年以来纪录），今日盘前全面反弹。英特尔涨4%（摩根大通上调评级至中性），美光涨2.4%，SK海力士涨3.9%，博通涨2.2%，ASML涨约2%。</p>
                <p><strong>2. NVHBM统一标准催化台积电+英伟达</strong>：三星将采用台积电3nm生产NVHBM基础裸片，英伟达要求三大供应商统一标准。台积电ADR涨1.8%，英伟达涨1.33%。HBM产业链迎来"标准化+加速放量"双重利好。</p>
                <p><strong>3. GTC大会前夕，黄仁勋10月21日演讲</strong>：大会聚焦Agentic AI、Physical AI、机器人、欧洲主权AI。英伟达欧洲投资总额将达近100亿美元（已有80亿+本周新增约20亿）。德国总理默茨将与黄仁勋会面讨论工业AI合作。</p>
                <p><strong>4. 科技巨头财报周开启</strong>：本周特斯拉(周三)、Meta(周三)、谷歌(周四)、微软(周四)等财报密集发布，将检验AI投资回报。市场将密切关注资本开支指引。</p>
                <p><strong>5. 10年期美债收益率5.06%</strong>：上周五美债收益率单周下行约17bp，本周一继续跌1bp。Warsh表态令市场下调本月加息预期。</p>
                <p><strong>6. 光通信/存储板块盘前领涨</strong>：Lumentum涨4%、康宁涨2.6%、应用光电涨4.6%、闪迪涨3.1%、希捷涨2.3%。AI算力基础设施链全面反弹。</p>
            </div>
        </div>
    </div>
    """
))

# === 4. A股今日表现与持仓分析（双重验证） ===
gen._components.append(Section(
    title="📊 A股今日表现与持仓分析（双重验证）",
    icon="bar_chart",
    content=DataGrid(cards=[
        DataCard(title="英维克(002837)", value="44.46元", subtitle="液冷散热龙头", trend="-0.54%", trend_up=False, variant="warning"),
        DataCard(title="铜冠铜箔(301217)", value="84.77元", subtitle="PCB铜箔龙头", trend="-0.76%", trend_up=False, variant="warning"),
        DataCard(title="雅克科技(002409)", value="96.11元", subtitle="半导体材料", trend="-1.94%", trend_up=False, variant="danger"),
        DataCard(title="*ST建艺(002789)", value="13.25元", subtitle="⚠️跌停！博弈持仓", trend="-9.31%", trend_up=False, variant="danger"),
    ]).render() + StockTags([
        {"code":"002837","name":"英维克","impact":"液冷龙头·跌0.54%·接近前低43元支撑"},
        {"code":"301217","name":"铜冠铜箔","impact":"高端铜箔·跌0.76%·中期分红10派0.6元"},
        {"code":"002409","name":"雅克科技","impact":"前驱体+光刻胶·跌1.94%·17.89亿增资利好仍在"},
        {"code":"002789","name":"*ST建艺","impact":"ST板块·跌9.31%·⚠️基本面恶化需止损"},
    ]).render() + """
    <div style="margin-top: 16px;">
        <div style="background: rgba(239,68,68,0.08); border: 1px solid rgba(239,68,68,0.25); border-radius: 14px; padding: 16px;">
            <div style="font-size: 14px; font-weight: 700; color: #f87171; margin-bottom: 10px;">⚠️ *ST建艺跌停双重验证结论</div>
            <div style="font-size: 13px; color: #fecaca; line-height: 1.8;">
                <p><strong>验证信源1（行情数据）</strong>：*ST建艺今日开盘14.60元，最低13.15元（触及跌停），收盘13.25元，跌幅9.31%。成交额5764万元，换手率2.76%。主力资金净流出498万元（证券之星+新浪财经双源一致）。</p>
                <p><strong>验证信源2（利空原因）</strong>：据新浪财经AI分析，跌停原因包括：①主业大幅收缩（最低单季营收仅1.06亿），二季度新签订单仅80余万；②资产负债率超95%，担保余额占净资产近10倍；③46亿+应收账款中七成以上账龄超3年，累计减值超25亿；④庭外重组进展不及预期，前期博弈重组资金集中离场。</p>
                <p><strong>性质判断：<span style="color: #f87171;">实质性利空</span></strong>，非监管模板性风险提示。基本面持续恶化，重组预期落空，属于博弈性持仓的典型风险兑现。</p>
                <p><strong>操作建议：<span style="color: #fbbf24;">严格执行止损纪律</span></strong>。*ST建艺作为博弈仓位（总仓位占比低），今日大跌9.31%已严重超预期，建议明日开盘后视情况止损出局，避免基本面进一步恶化导致更大损失。</p>
            </div>
        </div>
    </div>
    <div style="margin-top: 12px;">
        <div style="background: rgba(245,158,11,0.08); border: 1px solid rgba(245,158,11,0.25); border-radius: 14px; padding: 16px;">
            <div style="font-size: 14px; font-weight: 700; color: #fbbf24; margin-bottom: 10px;">🔍 雅克科技17.89亿增资跟踪（双重验证）</div>
            <div style="font-size: 13px; color: #fef3c7; line-height: 1.8;">
                <p><strong>增资事项持续验证中</strong>：雅克科技10月14日公告对江苏雅睿增资不超过17.89亿元（雅克4.39亿+外部投资者13.5亿）。10月15日补充公告披露有董事投弃权票（大基金管理机构任职董事认为定价低于估值）。</p>
                <p><strong>今日下跌-1.94%</strong>：雅克科技今日收96.11元，继续受半导体板块整体调整拖累。17.89亿增资利好尚未完全兑现，需关注后续股东大会进展和子公司业务进展。</p>
                <p><strong>估值锚：</strong>动态PE约40-44倍（不同口径），PB约5.72倍。半导体材料赛道国产替代背景下估值合理偏低。</p>
            </div>
        </div>
    </div>
    """
))

# === 5. 产业链分析 ===
gen.add_industry_chain_analysis(
    upstream=[
        {"name": "HBM材料/前驱体", "desc": "NVHBM统一标准加速HBM4E放量，前驱体/光刻胶需求确定性提升",
         "stocks": [
             {"code":"002409","name":"雅克科技","impact":"前驱体+光刻胶（持仓）·HBM核心材料"},
             {"code":"688535","name":"华海诚科","impact":"先进封装材料·HBM底部填充"},
         ]},
        {"name": "半导体设备", "desc": "GTC大会+NVHBM催化AI算力需求，设备是卖铲人最确定环节",
         "stocks": [
             {"code":"688012","name":"中微公司","impact":"刻蚀+ALD设备龙头"},
             {"code":"002371","name":"北方华创","impact":"平台型设备龙头"},
             {"code":"688120","name":"华海清科","impact":"CMP设备·董事长提议回购"},
         ]},
    ],
    midstream=[
        {"name": "HBM/存储芯片", "desc": "NVHBM统一标准是HBM产业里程碑事件，加速HBM4E放量",
         "stocks": [
             {"code":"688825","name":"长鑫科技","impact":"DRAM龙头·前三季净利1310亿"},
             {"code":"301308","name":"江波龙","impact":"存储模组·HBM布局"},
             {"code":"603986","name":"兆易创新","impact":"NOR+DRAM"},
         ]},
        {"name": "先进封装", "desc": "HBM+CoWoS产能瓶颈持续，先进封装是AI芯片交付核心",
         "stocks": [
             {"code":"600584","name":"长电科技","impact":"封测龙头"},
             {"code":"002156","name":"通富微电","impact":"AMD核心供应商"},
             {"code":"688535","name":"华海诚科","impact":"先进封装材料"},
         ]},
        {"name": "AI算力基础设施", "desc": "GTC大会+AI工厂叙事，液冷/铜箔/光模块需求确定性高",
         "stocks": [
             {"code":"002837","name":"英维克","impact":"液冷龙头（持仓）·43元前低支撑"},
             {"code":"301217","name":"铜冠铜箔","impact":"AI服务器铜箔（持仓）"},
         ]},
    ],
    downstream=[
        {"name": "人形机器人整机", "desc": "9部门政策+6项国标+宇树生态大会三重催化，需求侧空间打开",
         "stocks": [
             {"code":"688836","name":"宇树科技","impact":"人形机器人龙头·涨16.15%"},
             {"code":"300024","name":"机器人","impact":"工业机器人龙头"},
         ]},
        {"name": "机器人核心零部件", "desc": "减速器/丝杠/电机/传感器是机器人核心壁垒，国产替代空间大",
         "stocks": [
             {"code":"002472","name":"双环传动","impact":"RV减速器龙头"},
             {"code":"688017","name":"绿的谐波","impact":"谐波减速器龙头"},
             {"code":"601100","name":"恒立液压","impact":"液压+丝杠"},
         ]},
        {"name": "具身智能/AI Agent", "desc": "GTC核心议题，从聊天机器人向Agentic AI进化，算力需求倍增",
         "stocks": [
             {"code":"688787","name":"海天瑞声","impact":"AI数据服务"},
             {"code":"300229","name":"拓尔思","impact":"NLP+语义搜索"},
         ]},
    ]
)

# === 6. 投资机会分析 ===
gen.add_investment_opportunities(
    opportunities=[
        {
            "title": "💎 HBM统一标准：NVHBM的安卓时刻，加速产业标准化与放量",
            "level": "S级",
            "description": "英伟达要求三星、SK海力士、美光三大HBM供应商的NVHBM产品统一采用台积电3nm工艺制造基础裸片+1c DRAM工艺制造核心裸片。这是HBM历史上首次跨厂商统一制造标准，意义重大：①统一标准后产品性能一致性大幅提升，英伟达可减少逐家验证负担；②台积电3nm包揽基础裸片订单，台积电先进制程地位进一步巩固；③HBM4E放量节奏有望超预期。",
            "opportunity": "NVHBM统一标准是AI算力产业链的S级催化——HBM从各家自造进入标准化量产阶段，放量速度和良率都将大幅提升。明日HBM产业链（存储芯片、先进封装、半导体材料、半导体设备）有望迎来GTC前夕的反弹行情。重点关注：长鑫科技（存储龙头+业绩兑现）、雅克科技（前驱体+光刻胶+持仓）、华海诚科（先进封装材料）。",
            "risk": "GTC大会可能买预期卖事实；半导体板块整体情绪仍偏弱；美联储加息不确定性",
            "target_stocks": [
                {"code":"688825","name":"长鑫科技","impact":"DRAM龙头·业绩兑现·回购"},
                {"code":"002409","name":"雅克科技","impact":"前驱体+光刻胶（持仓）"},
                {"code":"688535","name":"华海诚科","impact":"HBM底部填充材料"},
            ]
        },
        {
            "title": "🤖 人形机器人：9部门政策+6项国标+宇树生态大会三重催化",
            "level": "S级",
            "description": "人形机器人迎来三重催化：①商务部等9部门发布《科技兴商意见》，首次从消费端推动机器人落地（家庭服务+商贸物流），需求侧空间打开；②市场监管总局发布首批6项人形机器人国家标准（2027年4月实施），行业标准统一加速产业化；③宇树科技10月22日举办世界物理AI大会暨合作伙伴生态大会。宇树科技今日大涨16.15%，市值重回2000亿。",
            "opportunity": "人形机器人政策级别从产业端升级到产业+消费双端驱动，9部门联合发文规格高、影响大。叠加首批国标的发布和宇树生态大会催化，板块情绪有望持续升温。但注意：多数机器人公司业绩尚未兑现，以主题炒作为主，需精选有真实技术壁垒和客户验证的标的。",
            "risk": "机器人板块业绩普遍尚未兑现，估值偏高，主题炒作持续性存疑；龙头宇树科技单日大涨后可能回调",
            "target_stocks": [
                {"code":"688836","name":"宇树科技","impact":"人形机器人龙头·标杆标的"},
                {"code":"002472","name":"双环传动","impact":"RV减速器·有业绩支撑"},
                {"code":"688017","name":"绿的谐波","impact":"谐波减速器龙头"},
            ]
        },
        {
            "title": "🎮 英伟达GTC柏林大会：AI工厂+Agentic AI+机器人",
            "level": "A级",
            "description": "英伟达GTC大会10月20-22日在柏林举行，黄仁勋21日发表主题演讲。核心看点：①Vera Rubin平台（面向智能体AI的全栈计算平台）的实际部署进展；②欧洲主权AI投资（英伟达欧洲投资总额将达近100亿美元）；③Agentic AI和Physical AI的技术突破；④机器人和工业AI的新进展。德国总理默茨将与黄仁勋会面。",
            "opportunity": "GTC大会是英伟达下半年最重要的技术与生态大会，通常会有重磅发布。AI工厂叙事+Agentic AI进化+欧洲投资预期，有望提振AI算力板块情绪。重点关注AI算力基础设施（液冷、光模块、PCB铜箔）和AI Agent相关标的。",
            "risk": "市场预期过高可能导致买预期卖事实；若黄仁勋演讲无超预期内容，可能引发短线回调",
            "target_stocks": [
                {"code":"002837","name":"英维克","impact":"液冷龙头（持仓）·AI算力基础设施"},
                {"code":"301217","name":"铜冠铜箔","impact":"AI服务器铜箔（持仓）"},
            ]
        },
        {
            "title": "⚠️ 持仓风险警示：*ST建艺跌停，严格执行止损",
            "level": "D级（风险）",
            "description": "*ST建艺今日大跌9.31%，接近跌停。利空原因包括：主业大幅收缩（单季营收仅1亿出头）、资产负债率超95%、应收账款46亿+且7成以上账龄超3年、庭外重组进展不及预期。前期博弈重组资金集中离场。",
            "opportunity": "不建议抄底。作为博弈性持仓，基本面恶化超出预期时必须严格止损。建议明日开盘后视情况减仓或清仓，避免更大损失。总仓位中ST类博弈仓位占比应控制在5%以内。",
            "risk": "面值退市风险（虽当前13元尚远，但基本面持续恶化）；庭外重组失败风险；持续经营不确定性",
            "target_stocks": [
                {"code":"002789","name":"*ST建艺","impact":"⚠️跌停·建议止损"},
            ]
        },
    ]
)

# === 7. NVHBM统一标准深度解读 ===
gen._components.append(Section(
    title="🧠 NVHBM统一标准深度解读：HBM产业的安卓时刻",
    icon="brain",
    variant="highlight",
    content=DataGrid(cards=[
        DataCard(title="基础裸片工艺", value="台积电3nm", subtitle="三大供应商统一", trend="标准化", trend_up=True, variant="success"),
        DataCard(title="核心裸片工艺", value="1c DRAM", subtitle="第六代DRAM工艺", trend="统一标准", trend_up=True, variant="success"),
        DataCard(title="HBM架构", value="HBM4E", subtitle="第七代HBM", trend="下一代", trend_up=True, variant="success"),
        DataCard(title="供应商数量", value="3家", subtitle="三星+SK海力士+美光", trend="跨厂统一", trend_up=True, variant="success"),
        DataCard(title="英伟达角色", value="标准制定者", subtitle="从GPU到HBM生态", trend="生态扩张", trend_up=True, variant="warning"),
        DataCard(title="台积电新增量", value="HBM基础裸片", subtitle="3nm订单再增", trend="超预期", trend_up=True, variant="success"),
    ]).render() + """
    <div style="margin-top: 16px;">
        <div style="background: rgba(34,197,94,0.08); border: 1px solid rgba(34,197,94,0.25); border-radius: 14px; padding: 16px;">
            <div style="font-size: 14px; font-weight: 700; color: #4ade80; margin-bottom: 10px;">✅ 为什么说NVHBM统一标准是里程碑事件？</div>
            <div style="font-size: 13px; color: #bbf7d0; line-height: 1.8;">
                <p><strong>1. 性能一致性大幅提升</strong>：此前三家HBM供应商各有各的制造工艺和设计方案，同样的HBM产品性能差异大、兼容性差。统一标准后，英伟达可确保NVHBM性能一致性，降低验证成本和时间。</p>
                <p><strong>2. 加速HBM4E放量节奏</strong>：标准化生产意味着良率提升、成本下降、产能扩张加快。HBM4E的量产时间和放量速度可能超市场预期。</p>
                <p><strong>3. 英伟达生态控制力进一步增强</strong>：从GPU标准制定者，进一步向HBM标准制定者延伸。英伟达通过统一技术标准，将整个AI算力产业链纳入自己的生态体系，英伟达等于AI工业标准的地位更加稳固。</p>
                <p><strong>4. 台积电是最大赢家之一</strong>：HBM基础裸片全部采用台积电3nm工艺，台积电3nm订单再增新来源。此前HBM基础裸片多由三星自家代工，现在转单台积电，台积电先进制程市占率进一步提升。</p>
                <p><strong>5. 三星被迫让步的信号意义</strong>：三星放弃自家一站式方案转而使用台积电3nm，说明在HBM竞争中，英伟达的话语权远大于三星。三星的战略收缩也意味着全球半导体产业格局正在向英伟达生态集中。</p>
            </div>
        </div>
    </div>
    <div style="margin-top: 12px;">
        <div style="background: rgba(239,68,68,0.08); border: 1px solid rgba(239,68,68,0.25); border-radius: 14px; padding: 16px;">
            <div style="font-size: 14px; font-weight: 700; color: #f87171; margin-bottom: 10px;">⚠️ 空方视角：需要警惕什么？</div>
            <div style="font-size: 13px; color: #fecaca; line-height: 1.8;">
                <p><strong>1. 买预期卖事实风险</strong>：GTC大会前夕市场情绪高涨，但如果黄仁勋演讲无超预期内容，可能引发短线回调。8连跌后的反弹持续性有待观察。</p>
                <p><strong>2. HBM涨价放缓</strong>：长鑫科技Q3净利润环比增速仅1-3.9%，较Q2的113%大幅放缓。DRAM涨价幅度收窄可能影响存储板块整体盈利弹性。</p>
                <p><strong>3. 对冲基金持续减仓AI股</strong>：高盛数据显示，对冲基金连续5个交易日净卖出全球AI股票，自2025年初以来的累计净买入在一周内被悉数抹去。机构资金撤退信号值得警惕。</p>
                <p><strong>4. 美联储政策不确定性</strong>：10年期美债收益率仍在5%以上，若通胀数据超预期，加息压力可能重新抬头，压制科技股估值。</p>
            </div>
        </div>
    </div>
    """
))

# === 8. 投资策略建议 ===
gen.add_investment_strategy(
    strategy="""
    <p><strong>【整体仓位】</strong>今日双S级催化（NVHBM统一标准+人形机器人政策）叠加美股半导体超跌反弹，明日AI算力+机器人板块有望共振修复。建议<strong>总仓位保持65-75%</strong>，利用反弹优化持仓结构：减仓基本面恶化的博弈性标的（*ST建艺），加仓有业绩支撑+逻辑清晰的AI算力核心标的（铜冠铜箔、雅克科技）。</p>
    <p><strong>【持仓操作建议（双重验证+估值锚）】</strong></p>
    <ol>
        <li><strong>铜冠铜箔（301217）</strong>：今日收84.77元(-0.76%)，近5日跌6.08%，近20日跌20.96%，调整较为充分。AI服务器铜箔需求确定性高，PCB铜箔景气度持续。<strong>持有+逢低加仓机动仓</strong>。支撑位：80元（整数关口+前期平台），压力位：95元（20日线）。估值锚：PE(TTM)约163倍偏高，但H1净利同比增514%验证高增长，PEG约0.3-0.5处于合理区间。</li>
        <li><strong>雅克科技（002409）</strong>：今日收96.11元(-1.94%)，17.89亿增资利好仍在消化中。NVHBM统一标准利好HBM前驱体/光刻胶需求。<strong>持有观望</strong>，等待GTC催化+增资落地双重信号。支撑位：92.7元（今日低点），压力位：105元（10日线）。估值锚：PE(TTM)约44倍，PB约5.7倍，半导体材料赛道国产替代背景下估值合理。</li>
        <li><strong>英维克（002837）</strong>：今日收44.46元(-0.54%)，液冷板块持续调整，接近前低43元支撑位。液冷长期逻辑不变，短期受板块情绪拖累。<strong>持有观望</strong>，等待放量企稳信号再加仓。支撑位：43元（前低），压力位：50元（20日线）。估值锚：PE(TTM)约115-154倍（不同口径差异大），PB约15.9倍，估值偏高，需业绩验证消化估值。</li>
        <li><strong>*ST建艺（002789）</strong>：今日大跌9.31%，收13.25元，接近跌停。基本面恶化（主业收缩、负债率95%+、重组不及预期）。<strong>建议明日止损出局</strong>，博弈性持仓遇到基本面利空必须严格执行纪律，不可恋战。止损位：今日已跌破预期，明日开盘后视流动性情况减仓或清仓。</li>
    </ol>
    <p><strong>【明日关注方向】</strong></p>
    <ul>
        <li>美股半导体反弹持续性（纳指期货、费城半导体指数表现）</li>
        <li>NVHBM统一标准对A股HBM/存储/先进封装板块的催化效果</li>
        <li>人形机器人板块延续性（宇树科技能否继续走强、板块扩散广度）</li>
        <li>GTC大会前夕消息面变化，黄仁勋演讲是否有超预期内容</li>
        <li>长鑫科技开盘表现（业绩+回购双重利好）</li>
    </ul>
    <p><strong>【核心原则】</strong>双S级催化共振是好信号，但也要警惕利好出尽风险。操作上：①*ST建艺必须严格止损，基本面恶化的博弈持仓不可心存侥幸；②加仓方向聚焦有真实业绩支撑的标的（铜冠铜箔、长鑫科技），回避纯题材炒作；③GTC大会前可适度乐观，但演讲后要警惕获利回吐；④控制仓位，保留现金应对可能的市场波动。</p>
    """
)

# === 9. 风险提示 ===
gen.add_risk_warning(
    risks=[
        "GTC大会买预期卖事实风险，若黄仁勋演讲无超预期内容可能引发短线回调",
        "费城半导体8连跌后反弹持续性存疑，对冲基金连续5日净卖出AI股",
        "DRAM涨价幅度放缓，长鑫科技Q3净利润环比增速仅1-4%",
        "美联储政策不确定性，10年期美债收益率仍在5%以上",
        "人形机器人板块业绩普遍尚未兑现，估值偏高，主题炒作持续性存疑",
        "*ST建艺基本面持续恶化，庭外重组进展不及预期，止损执行风险",
        "中美半导体管制进一步升级的可能性",
        "科技巨头财报周风险：Meta、特斯拉等财报若不及预期可能引发板块下挫"
    ]
)

if __name__ == "__main__":
    result = gen.publish(
        title="英伟达GTC前夕+NVHBM统一标准+人形机器人政策双S级催化",
        filename="20261019_盘后_S级催化扫描_NVHBM统一标准+人形机器人政策.html"
    )
    print(f"发布结果: {result}")
