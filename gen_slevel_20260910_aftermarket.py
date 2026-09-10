import sys, os
sys.path.insert(0, '/root/daily-news-insight')
sys.path.insert(0, '/root/daily-news-insight/v3')
os.chdir('/root/daily-news-insight')

from v3.generators.s_level_catalyst import SLevelCatalystGenerator
from components.layout import Section

gen = SLevelCatalystGenerator(
    date_str="20260910",
    catalyst_title="油价破百通胀冲击+台积电超预期",
    subtitle="2026.09.10 · 盘后S级催化"
)

# 1. Catalyst overview
gen.add_catalyst_overview(
    "盘后双重S级催化落地：<strong>①油价破百重燃全球通胀恐慌</strong>——布伦特原油突破105美元/桶，WTI逼近100美元，"
    "美伊战事升级致霍尔木兹海峡航运骤降八成，全球央行加息预期飙升，美债收益率上行压制成长股估值；"
    "<strong>②台积电8月营收同比暴增53.3%</strong>——单月营收5148亿新台币（约163亿美元），环比再增10.1%，"
    "AI需求持续超预期验证半导体产业景气度。此外，英维克盘后推出2500万份股票期权激励计划，三年业绩增长目标95%，"
    "彰显管理层信心。隔夜费半逆势涨0.37%，美光+2.75%、AMD+3.04%，半导体产业逻辑与宏观风险激烈博弈。"
)

# 2. Catalyst details
gen.add_catalyst_details(
    background=(
        "2026年9月，美伊战事再度升级，霍尔木兹海峡局势急剧恶化。作为全球约20%石油供应通道，该海峡自8月12日"
        "伊朗宣布关闭以来，海上交通量已骤降八成。布伦特原油从8月初的80美元附近快速拉升至105美元上方，累计涨幅超30%。"
        "与此同时，AI算力需求保持强劲增长——台积电8月营收再创历史新高，同比增长53.3%，环比增长10.1%，远超市场预期。"
        "存储芯片方面，三星+SK海力士DRAM库存不足10天的历史性短缺格局未变，但铠侠CEO最新表态称价格已涨够，"
        "警告进一步大幅涨价可能损害AI投资需求，引发市场对存储涨价持续性的担忧。"
    ),
    trigger=(
        "【宏观端】油价破百冲击：布油+3.75%报105美元，WTI+3.84%报99.73美元。法国智库TAC测算，若高油价持续数个季度，"
        "美国累计通胀将多升1.4个百分点，美联储收紧流动性压力明显加码。若油价冲上160美元则演变为全面滞胀。\\n"
        "【产业端】台积电8月营收5148亿新台币，同比+53.3%、环比+10.1%，AI HPC主芯片先进制程持续供不应求，"
        "PMIC/功率分立器件等AI周边芯片需求同步增长，消费电子供应链提前备货效应延续（TrendForce数据）。\\n"
        "【公司端】英维克推出2500万份股票期权激励，行权价46.73元/股，768人覆盖，三年净利润增长目标25%/56%/95%，"
        "彰显管理层对液冷长期赛道的信心；苹果发布首款折叠屏iPhone Duo，A20 Pro芯片采用2nm制程。\\n"
        "【政策端】工信部电子信息司召开电子元器件产业发展座谈会，部署十五五时期产业发展路径，"
        "证监会副主席李超表态优化发行上市制度、支持新兴产业优质企业发展壮大。\\n"
        "【资金端】今日龙虎榜机构合计净卖出3.16亿元，30只个股现机构身影，其中11只净买入、19只净卖出，"
        "金安国纪获机构净买入2.03亿元居首，敦煌种业遭净卖出2.13亿元。"
    )
)

# 3. Overnight market
overnight_html = """
<div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 12px; margin-bottom: 16px;">
    <div style="background: linear-gradient(135deg, rgba(239,68,68,0.15) 0%, rgba(185,28,28,0.08) 100%); border-radius: 12px; padding: 16px; border: 1px solid rgba(239,68,68,0.25); text-align: center;">
        <div style="font-size: 12px; color: #fca5a5; margin-bottom: 6px;">布伦特原油</div>
        <div style="font-size: 22px; font-weight: 800; color: #f87171;">+3.75%</div>
        <div style="font-size: 11px; color: #fca5a5; margin-top: 4px;">105.0美元</div>
    </div>
    <div style="background: linear-gradient(135deg, rgba(16,185,129,0.12) 0%, rgba(5,150,105,0.06) 100%); border-radius: 12px; padding: 16px; border: 1px solid rgba(16,185,129,0.25); text-align: center;">
        <div style="font-size: 12px; color: #6ee7b7; margin-bottom: 6px;">费城半导体</div>
        <div style="font-size: 22px; font-weight: 800; color: #34d399;">+0.37%</div>
        <div style="font-size: 11px; color: #6ee7b7; margin-top: 4px;">逆势走强</div>
    </div>
    <div style="background: linear-gradient(135deg, rgba(239,68,68,0.12) 0%, rgba(185,28,28,0.06) 100%); border-radius: 12px; padding: 16px; border: 1px solid rgba(239,68,68,0.25); text-align: center;">
        <div style="font-size: 12px; color: #fca5a5; margin-bottom: 6px;">纳斯达克</div>
        <div style="font-size: 22px; font-weight: 800; color: #f87171;">-0.64%</div>
        <div style="font-size: 11px; color: #fca5a5; margin-top: 4px;">承压调整</div>
    </div>
    <div style="background: linear-gradient(135deg, rgba(245,158,11,0.15) 0%, rgba(217,119,6,0.08) 100%); border-radius: 12px; padding: 16px; border: 1px solid rgba(245,158,11,0.25); text-align: center;">
        <div style="font-size: 12px; color: #fcd34d; margin-bottom: 6px;">美光科技</div>
        <div style="font-size: 22px; font-weight: 800; color: #fbbf24;">+2.75%</div>
        <div style="font-size: 11px; color: #fcd34d; margin-top: 4px;">存储景气</div>
    </div>
</div>
<div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 14px;">
    <div style="background: rgba(255,255,255,0.04); border-radius: 12px; padding: 16px; border: 1px solid rgba(255,255,255,0.08);">
        <div style="font-size: 14px; font-weight: 700; color: #f1f5f9; margin-bottom: 10px;">全球科技股表现</div>
        <div style="display: flex; flex-direction: column; gap: 8px;">
            <div style="display: flex; justify-content: space-between;"><span style="font-size: 13px; color: #94a3b8;">AMD</span><span style="font-size: 13px; font-weight: 600; color: #34d399;">+3.04%</span></div>
            <div style="display: flex; justify-content: space-between;"><span style="font-size: 13px; color: #94a3b8;">美光科技</span><span style="font-size: 13px; font-weight: 600; color: #34d399;">+2.75%</span></div>
            <div style="display: flex; justify-content: space-between;"><span style="font-size: 13px; color: #94a3b8;">英特尔</span><span style="font-size: 13px; font-weight: 600; color: #34d399;">+1.69%</span></div>
            <div style="display: flex; justify-content: space-between;"><span style="font-size: 13px; color: #94a3b8;">台积电ADR</span><span style="font-size: 13px; font-weight: 600; color: #f87171;">-0.83%</span></div>
            <div style="display: flex; justify-content: space-between;"><span style="font-size: 13px; color: #94a3b8;">英伟达</span><span style="font-size: 13px; font-weight: 600; color: #f87171;">-0.91%</span></div>
            <div style="display: flex; justify-content: space-between;"><span style="font-size: 13px; color: #94a3b8;">博通</span><span style="font-size: 13px; font-weight: 600; color: #f87171;">-1.13%</span></div>
            <div style="display: flex; justify-content: space-between;"><span style="font-size: 13px; color: #94a3b8;">应用材料</span><span style="font-size: 13px; font-weight: 600; color: #f87171;">-0.83%</span></div>
            <div style="display: flex; justify-content: space-between;"><span style="font-size: 13px; color: #94a3b8;">阿斯麦</span><span style="font-size: 13px; font-weight: 600; color: #f87171;">-2.00%</span></div>
        </div>
    </div>
    <div style="background: rgba(255,255,255,0.04); border-radius: 12px; padding: 16px; border: 1px solid rgba(255,255,255,0.08);">
        <div style="font-size: 14px; font-weight: 700; color: #f1f5f9; margin-bottom: 10px;">宏观与商品关键数据</div>
        <div style="display: flex; flex-direction: column; gap: 8px;">
            <div style="display: flex; justify-content: space-between;"><span style="font-size: 13px; color: #94a3b8;">道琼斯</span><span style="font-size: 13px; font-weight: 600; color: #f87171;">-0.77%</span></div>
            <div style="display: flex; justify-content: space-between;"><span style="font-size: 13px; color: #94a3b8;">标普500</span><span style="font-size: 13px; font-weight: 600; color: #f87171;">-0.48%</span></div>
            <div style="display: flex; justify-content: space-between;"><span style="font-size: 13px; color: #94a3b8;">WTI原油</span><span style="font-size: 13px; font-weight: 600; color: #f87171;">+3.84% / 99.73美元</span></div>
            <div style="display: flex; justify-content: space-between;"><span style="font-size: 13px; color: #94a3b8;">COMEX黄金</span><span style="font-size: 13px; font-weight: 600; color: #f87171;">-1.27% / 4404美元</span></div>
            <div style="display: flex; justify-content: space-between;"><span style="font-size: 13px; color: #94a3b8;">COMEX白银</span><span style="font-size: 13px; font-weight: 600; color: #f87171;">-4.50%</span></div>
            <div style="display: flex; justify-content: space-between;"><span style="font-size: 13px; color: #94a3b8;">恒生指数</span><span style="font-size: 13px; font-weight: 600; color: #f87171;">-1.27%</span></div>
            <div style="display: flex; justify-content: space-between;"><span style="font-size: 13px; color: #94a3b8;">日经225</span><span style="font-size: 13px; font-weight: 600; color: #f87171;">-0.90%</span></div>
            <div style="display: flex; justify-content: space-between;"><span style="font-size: 13px; color: #94a3b8;">富时100</span><span style="font-size: 13px; font-weight: 600; color: #34d399;">+0.77%</span></div>
        </div>
    </div>
</div>
"""

gen._components.append(Section(title="隔夜外盘跟踪", content=overnight_html, icon="globe"))

# 4. Industry chain
gen.add_industry_chain_analysis(
    upstream=[
        {
            "name": "半导体设备/材料",
            "desc": "台积电营收超预期验证AI芯片扩产需求，设备材料订单确定性增强。但油价上涨推升制造成本，需关注通胀对资本开支的潜在压制。",
            "stocks": [
                {"code": "002409", "name": "雅克科技", "impact": "强"},
                {"code": "688082", "name": "盛美上海", "impact": "中"},
            ]
        },
        {
            "name": "原油/油气产业链",
            "desc": "油价破百直接受益。布油105美元、WTI逼近100美元，霍尔木兹海峡局势恶化推动油价持续上行。关注油气开采、油服设备等方向。",
            "stocks": [
                {"code": "601857", "name": "中国石油", "impact": "强"},
                {"code": "600028", "name": "中国石化", "impact": "中"},
            ]
        },
        {
            "name": "液冷温控/算力基础设施",
            "desc": "英维克股权激励彰显管理层信心，三年95%净利润增长目标印证液冷赛道长期景气。AI算力扩张驱动温控需求持续增长。",
            "stocks": [
                {"code": "002837", "name": "英维克", "impact": "强"},
            ]
        },
    ],
    midstream=[
        {
            "name": "晶圆代工/先进制程",
            "desc": "台积电8月营收5148亿新台币同比+53.3%，AI HPC主芯片持续供不应求，2nm/3nm产能满载。先进制程景气度为全产业链最强环节。",
            "stocks": [
                {"code": "688981", "name": "中芯国际", "impact": "中"},
            ]
        },
        {
            "name": "存储芯片",
            "desc": "存储短缺逻辑仍在但出现分歧。三星+SK海力士库存不足10天，美光涨2.75%，但铠侠CEO警告价格已涨够，NAND涨价斜率可能放缓。",
            "stocks": [
                {"code": "603986", "name": "兆易创新", "impact": "中"},
                {"code": "688525", "name": "佰维存储", "impact": "中"},
            ]
        },
        {
            "name": "铜箔/PCB（AI算力配套）",
            "desc": "AI服务器算力扩张传导至PCB/铜箔环节，高端高频高速材料需求增长。但油价上涨推升原材料成本，关注盈利承压风险。",
            "stocks": [
                {"code": "301217", "name": "铜冠铜箔", "impact": "中"},
                {"code": "002636", "name": "金安国纪", "impact": "强（龙虎榜）"},
            ]
        },
    ],
    downstream=[
        {
            "name": "AI服务器/智算中心",
            "desc": "台积电营收超预期验证AI算力需求强劲。英伟达Blackwell/Rubin产能持续扩张，AI服务器出货量保持高增长。",
            "stocks": [
                {"code": "000977", "name": "浪潮信息", "impact": "强"},
                {"code": "603019", "name": "中科曙光", "impact": "强"},
            ]
        },
        {
            "name": "消费电子/苹果产业链",
            "desc": "苹果秋季发布会发布首款折叠屏iPhone Duo（2nm A20 Pro芯片），顶配26499元。初期日产量仅数百部，年底前供货紧张。",
            "stocks": [
                {"code": "002475", "name": "立讯精密", "impact": "中"},
                {"code": "300136", "name": "信维通信", "impact": "中"},
            ]
        },
        {
            "name": "光通信/光模块",
            "desc": "AI算力扩张持续拉动光模块需求，800G/1.6T光模块量价齐升。但短期大盘承压可能压制板块表现。",
            "stocks": [
                {"code": "300308", "name": "中际旭创", "impact": "强"},
                {"code": "300394", "name": "天孚通信", "impact": "强"},
            ]
        },
    ]
)

# 5. Investment opportunities
gen.add_investment_opportunities([
    {
        "name": "半导体/AI算力（核心主线）",
        "priority": "高",
        "logic": "台积电8月营收同比+53.3%、环比+10.1%，AI需求强劲程度超市场预期。费半逆势上涨、美光+2.75%、AMD+3.04%，产业逻辑独立行情持续验证。虽然油价破百带来宏观压力，但AI算力作为最强产业趋势，回调即是布局机会。重点关注：半导体材料/设备、先进封装、光模块三个方向。",
        "stocks": [
            {"code": "002409", "name": "雅克科技", "impact": "持仓强"},
            {"code": "300308", "name": "中际旭创", "impact": "强"},
        ]
    },
    {
        "name": "油气/能源（防御+进攻双属性）",
        "priority": "高",
        "logic": "布油突破105美元，WTI逼近100美元，霍尔木兹海峡局势持续恶化。高盛警告油价可能冲向120美元。油价上涨直接利好油气开采、油服企业，同时通胀受益标的具备防御属性。法国智库TAC测算若高油价持续数季度，美国通胀将多升1.4个百分点。",
        "stocks": [
            {"code": "601857", "name": "中国石油", "impact": "强"},
            {"code": "600028", "name": "中国石化", "impact": "中"},
        ]
    },
    {
        "name": "液冷温控（英维克股权激励催化）",
        "priority": "中",
        "logic": "英维克盘后推出2500万份股票期权激励计划，行权价46.73元/股，三年净利润增长目标25%/56%/95%（2025年为基数），覆盖768名核心员工。股权激励彰显管理层对液冷赛道长期信心，行权价提供估值锚。但当前股价61元仍显著高于行权价，需关注短期情绪面压力。",
        "stocks": [
            {"code": "002837", "name": "英维克", "impact": "持仓强"},
        ]
    },
    {
        "name": "存储芯片（涨价周期存分歧）",
        "priority": "中",
        "logic": "存储历史性短缺格局未变（三星+SK海力士库存不足10天），美光涨2.75%验证景气。但铠侠CEO最新表态警告价格已涨够、进一步大幅涨价可能损害需求，NAND涨价斜率存在放缓预期。DRAM供需格局仍紧，涨价确定性高于NAND。关注存储芯片设计、封测环节。",
        "stocks": [
            {"code": "603986", "name": "兆易创新", "impact": "中"},
            {"code": "688525", "name": "佰维存储", "impact": "中"},
        ]
    },
    {
        "name": "苹果产业链（折叠屏催化）",
        "priority": "低",
        "logic": "苹果发布首款折叠屏iPhone Duo，2nm A20 Pro芯片，顶配26499元。初期日产量仅数百部，年底前供货紧张。折叠屏作为iPhone外观最大变化，有望带动新一轮换机需求。但消费电子整体需求仍偏弱，苹果发布会利好兑现后可能出现利好出尽行情。",
        "stocks": [
            {"code": "002475", "name": "立讯精密", "impact": "中"},
        ]
    },
], view_mode="tab")

# 6. Deep analysis
gen.add_catalyst_deep_analysis([
    {
        "title": "油价破百的通胀冲击",
        "type": "macro",
        "description": "布油突破105美元，全球央行加息预期飙升，成长股估值承压",
        "category": "macro"
    },
    {
        "title": "台积电超预期营收",
        "type": "industry",
        "description": "8月营收5148亿新台币同比+53.3%，AI需求持续超预期验证产业景气",
        "category": "semiconductor"
    },
    {
        "title": "英维克股权激励",
        "type": "company",
        "description": "2500万份期权，三年增长95%目标，彰显液冷赛道长期信心",
        "category": "company"
    },
])

# 7. Portfolio impact
portfolio_html = """
<div style="display: flex; flex-direction: column; gap: 12px;">
    <div style="background: linear-gradient(135deg, rgba(16,185,129,0.10) 0%, rgba(5,150,105,0.05) 100%); border-radius: 12px; padding: 16px; border: 1px solid rgba(16,185,129,0.25);">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
            <div style="display: flex; align-items: center; gap: 8px;">
                <span style="font-size: 18px;">🧪</span>
                <span style="font-size: 15px; font-weight: 700; color: #f1f5f9;">雅克科技（002409）</span>
                <span style="padding: 3px 8px; border-radius: 12px; font-size: 11px; font-weight: 600; background: rgba(16,185,129,0.2); color: #6ee7b7;">利好</span>
            </div>
            <span style="font-size: 13px; font-weight: 700; color: #fbbf24;">★★★★★ 强受益</span>
        </div>
        <div style="font-size: 13px; color: #cbd5e1; line-height: 1.7;">
            <strong>催化逻辑：</strong>台积电营收超预期验证AI芯片扩产需求，存储短缺格局未变，半导体材料景气度持续。雅克科技作为HBM前驱体龙头深度受益于存储扩产。<br>
            <strong>新增催化：</strong>9月9日雅克科技接待泰康资产等3家机构调研，明确中韩双基地扩产明年年底前建成，钼前驱体在300层以上NAND应用前景广阔。9月10日召开第二次临时股东大会。<br>
            <strong>风险点：</strong>油价破百推升通胀预期，美债收益率上行可能压制成长股估值，半导体板块短期面临宏观压力。<br>
            <strong>双重验证：</strong>①公司公告确认机构调研内容及扩产计划（深交所公告）；②台积电8月营收5148亿新台币同比+53.3%（台积电官网）；③TrendForce/KB证券多方验证存储短缺逻辑。
        </div>
    </div>
    <div style="background: linear-gradient(135deg, rgba(59,130,246,0.10) 0%, rgba(37,99,235,0.05) 100%); border-radius: 12px; padding: 16px; border: 1px solid rgba(59,130,246,0.25);">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
            <div style="display: flex; align-items: center; gap: 8px;">
                <span style="font-size: 18px;">❄️</span>
                <span style="font-size: 15px; font-weight: 700; color: #f1f5f9;">英维克（002837）</span>
                <span style="padding: 3px 8px; border-radius: 12px; font-size: 11px; font-weight: 600; background: rgba(59,130,246,0.2); color: #93c5fd;">偏利好</span>
            </div>
            <span style="font-size: 13px; font-weight: 700; color: #fbbf24;">★★★★ 中度受益</span>
        </div>
        <div style="font-size: 13px; color: #cbd5e1; line-height: 1.7;">
            <strong>催化逻辑：</strong>盘后推出2500万份股票期权激励计划（占股本1.95%），行权价46.73元/股，覆盖768名核心员工。业绩考核目标：以2025年净利润为基数，2026-2028年增长率分别不低于25%、56%、95%。股权激励彰显管理层对液冷赛道长期信心，行权价提供估值锚参考。<br>
            <strong>今日表现：</strong>收61.08元（-2.16%），成交18.11亿元，近3日主力资金净流出5.74亿，短期情绪面仍偏弱。当前股价较行权价溢价约30.6%。<br>
            <strong>双重验证：</strong>①公司官方公告《2026年股票期权激励计划（草案）》（深交所公告）；②2026年半年报营收30.17亿+净利润1.85亿（公司财报）；③液冷行业需求增长逻辑获多家机构验证（中信建投/国盛证券）。
        </div>
    </div>
    <div style="background: linear-gradient(135deg, rgba(245,158,11,0.10) 0%, rgba(217,119,6,0.05) 100%); border-radius: 12px; padding: 16px; border: 1px solid rgba(245,158,11,0.25);">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
            <div style="display: flex; align-items: center; gap: 8px;">
                <span style="font-size: 18px;">🔩</span>
                <span style="font-size: 15px; font-weight: 700; color: #f1f5f9;">铜冠铜箔（301217）</span>
                <span style="padding: 3px 8px; border-radius: 12px; font-size: 11px; font-weight: 600; background: rgba(245,158,11,0.2); color: #fcd34d;">中性</span>
            </div>
            <span style="font-size: 13px; font-weight: 700; color: #9ca3af;">★★★ 间接影响</span>
        </div>
        <div style="font-size: 13px; color: #cbd5e1; line-height: 1.7;">
            <strong>催化评估：</strong>油价破百推升铜等大宗商品价格，对铜箔企业原材料成本构成压力。但AI算力扩张拉动高端电子铜箔需求增长，供需两端均有变化。整体影响偏中性，需关注成本传导能力。<br>
            <strong>关注重点：</strong>电子铜箔产能释放进度与高端产品认证进展；锂电铜箔价格走势；油价上涨对铜价的传导效应。<br>
            <strong>今日无重大公告，继续持有观察。</strong>
        </div>
    </div>
    <div style="background: linear-gradient(135deg, rgba(107,114,128,0.10) 0%, rgba(75,85,99,0.05) 100%); border-radius: 12px; padding: 16px; border: 1px solid rgba(107,114,128,0.25);">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
            <div style="display: flex; align-items: center; gap: 8px;">
                <span style="font-size: 18px;">🏗️</span>
                <span style="font-size: 15px; font-weight: 700; color: #f1f5f9;">*ST建艺（002789）</span>
                <span style="padding: 3px 8px; border-radius: 12px; font-size: 11px; font-weight: 600; background: rgba(107,114,128,0.2); color: #9ca3af;">中性</span>
            </div>
            <span style="font-size: 13px; font-weight: 700; color: #9ca3af;">★ 影响有限</span>
        </div>
        <div style="font-size: 13px; color: #cbd5e1; line-height: 1.7;">
            <strong>催化评估：</strong>油价破百和半导体催化均与建筑装饰行业无直接关联。公司核心逻辑仍在于摘帽预期和主业恢复。今日无重大公告。继续作为组合防御端配置观察。
        </div>
    </div>
</div>
"""

gen._components.append(Section(title="持仓股影响评估", content=portfolio_html, icon="pie-chart", variant="highlight"))

# 8. Risk warnings
gen.add_risk_warning([
    "宏观风险（最高等级）：油价破百重燃全球通胀恐慌，布油105美元/WTI 100美元，美联储加息预期飙升，美债收益率上行系统性压制成长股估值，大盘回调风险加剧",
    "地缘政治风险：美伊战事升级，霍尔木兹海峡航运骤降八成，局势若进一步恶化（如能源基础设施遭摧毁），油价可能冲向120-160美元，引发全面滞胀",
    "存储涨价放缓风险：铠侠CEO公开表态价格已涨够，指示销售团队不再大幅涨价，NAND涨价斜率可能放缓，存储板块短期情绪面承压",
    "技术面风险：A股今日缩量调整（年内第二低量），市场观望情绪浓厚，半导体板块处于三角形震荡下沿，若跌破关键支撑可能触发技术性抛压",
    "持仓股风险：英维克近3日主力净流出5.74亿，短期情绪面仍弱；雅克科技需验证存储扩产对业绩的实际拉动；铜冠铜箔需关注油价上涨对成本的传导压力"
])

# 9. Investment strategy
gen.add_investment_strategy(
    "<strong>整体策略：</strong>今日盘后S级催化呈现产业利好+宏观利空的复杂格局——台积电超预期营收验证AI算力产业景气度（正面），"
    "但油价破百引发的通胀和加息预期对成长股估值构成系统性压力（负面）。建议采取<strong>防御为主、精选个股</strong>的策略，"
    "整体仓位控制在5成以下，重点配置油气等通胀受益板块作为防御，同时逢低布局半导体/AI算力核心标的。"
    "<br><br><strong>核心方向排序：</strong>油气/能源（防御） ＞ 半导体材料/设备 ＞ 液冷温控 ＞ 光模块 ＞ 存储芯片"
    "<br><br><strong>持仓操作建议：</strong>"
    "<br>• <strong>雅克科技</strong>：台积电超预期+存储短缺逻辑持续验证，半导体材料景气度未变。建议持有底仓策略，"
    "若因大盘回调至75-80元区间可考虑加仓，PE历史分位约35%，估值尚合理。技术支撑位参考60日均线"
    "<br>• <strong>英维克</strong>：股权激励计划出台（行权价46.73元，三年增长95%目标），彰显管理层信心，属正面催化。"
    "但当前股价61元仍高出行权价30%，且短期资金持续流出，建议耐心等待企稳信号（放量阳线+站稳60元）再考虑加仓。"
    "<strong>技术支撑位58-60元，止损位55元。估值锚：以2025年净利润为基数，2026年25%增长目标对应PE约35-40倍</strong>"
    "<br>• <strong>铜冠铜箔</strong>：油价上涨推升原材料成本压力，但AI算力需求拉动电子铜箔增长，整体中性。"
    "继续持有观察，关注电子铜箔业务进展，支撑位参考前期低点"
    "<br>• <strong>*ST建艺</strong>：与催化关联度低，继续作为防御端持有，关注摘帽进展"
    "<br><br><strong>明日关注：</strong>"
    "<br>① 油价走势及中东局势变化（重点关注是否有新一轮冲突升级消息）"
    "<br>② 半导体板块能否在外盘费半上涨带动下企稳反弹，重点看成交额能否有效放大"
    "<br>③ 沪指关键支撑位有效性，若跌破需进一步降低仓位"
    "<br>④ 英维克股权激励市场反应（能否止跌企稳是关键观察点）"
    "<br><br><strong>数据来源：</strong>台积电官网、TrendForce、EIA、法国智库TAC、工信部、证监会、东方财富Choice、财联社、证券时报、新浪财经"
)

# Publish
result = gen.publish(
    title="油价破百通胀冲击+台积电超预期",
    report_type="s_level_catalyst",
    filename="20260910_盘后_S级催化扫描_油价破百+台积电超预期.html",
    excerpt="盘后双重S级催化：油价破百重燃全球通胀恐慌，布油105美元/WTI逼近100美元，央行加息预期飙升；台积电8月营收同比暴增53.3%，AI需求持续超预期。英维克推出2500万份股权激励，三年增长95%目标。隔夜费半逆势涨0.37%。"
)

print(f"发布结果: {result}")
