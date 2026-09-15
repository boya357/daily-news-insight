import sys, os
sys.path.insert(0, '/root/daily-news-insight')
sys.path.insert(0, '/root/daily-news-insight/v3')
os.chdir('/root/daily-news-insight')

from v3.generators.s_level_catalyst import SLevelCatalystGenerator
from components.layout import Section

gen = SLevelCatalystGenerator(
    date_str="20260915",
    catalyst_title="AI减速恐慌费半暴跌6%+光刻胶涨价",
    subtitle="2026.09.15 · 盘后S级催化"
)

# 1. Catalyst overview
gen.add_catalyst_overview(
    "盘后双重S级催化落地：<strong>①费城半导体暴跌5.86%创7月以来最大单日跌幅</strong>——"
    "30只成份股全线收跌，AI巨头集体呼吁\"减速前沿AI\"引爆市场对AI资本开支放缓的担忧，"
    "英伟达-3.36%/台积电ADR-3%+/SK海力士-7.6%/美光-5.25%，芯片产业链市值蒸发超5000亿美元；"
    "<strong>②日本三大光刻胶厂10月起全面涨价</strong>——JSR/东京应化/信越化学宣布10月1日起光刻胶新定价整体上调15%，"
    "高端ArF长协涨16%-22%、HBM专用浸没式ArF最高涨24%、现货散单涨32%-38%，国内光刻胶国产替代逻辑再强化。"
    "值得注意的是，A股半导体今日逆市获得逾70亿主力净流入，国产替代逻辑与外盘情绪激烈博弈。"
)

# 2. Catalyst details
gen.add_catalyst_details(
    background=(
        "2026年9月14日（美东时间），Anthropic CEO阿莫代伊发表《我们必须放慢前沿AI的推进脚步》署名文章，"
        "OpenAI CEO奥尔特曼、xAI创始人马斯克相继表态支持，三大AI巨头罕见形成\"减速共识\"。"
        "市场迅速将此解读为AI资本开支可能收缩的信号，芯片股遭遇恐慌性抛售。与此同时，10年期美债收益率盘中突破5%创2007年以来新高，"
        "美联储9月加息25bp概率升至近90%，高利率环境进一步压制成长股估值。"
        "另一面，日本光刻胶三巨头（JSR/东京应化/信越化学）宣布10月起全球客户新定价上调15%，"
        "HBM专用浸没式ArF最高涨24%，光刻胶作为半导体材料\"咽喉\"的战略地位再度凸显，国产替代紧迫度升温。"
        "9月15日A股半导体板块逆势走强，获得逾70亿主力净流入，西陇科学等电子化学品股涨停。"
    ),
    trigger=(
        "【外盘端】费城半导体重挫5.86%（-692.72点），30只成份股全线收跌，创7月1日以来最大单日跌幅。"
        "泰瑞达-13.3%、Coherent-12.73%、Astera Labs-11.74%、ARM-9.74%、英特格/拉姆研究跌超8%、"
        "阿斯麦/应用材料跌超7%、博通/AMD跌超4%、英伟达-3.36%、台积电ADR-3%+、美光-5.25%、SK海力士-7.6%。"
        "芯片产业链市值蒸发超5000亿美元。\n"
        "【产业端】日本JSR/东京应化/信越化学三大光刻胶厂商宣布，自2026年10月1日起全球客户新定价整体上调15%，"
        "高端ArF系列长协报价涨16%-22%，HBM专用浸没式ArF最高涨24%，现货散单涨32%-38%，"
        "KrF常规牌号涨9%-14%、3D NAND厚膜专用KrF涨18%-20%。日本企业控制全球光刻胶70%以上、高端EUV约95%份额。\n"
        "【政策端】特朗普公开驳斥\"AI毁灭人类\"说法，称AI与数据中心将成为史上最强劲经济发展引擎，"
        "黄仁勋也反对AI减速——不到36小时出现两次表态反转，\"减速论\"仍停留在口头阶段，未出现任何资本开支削减或订单下调的实质性变化。\n"
        "【资金端】今日A股半导体板块获逾70亿主力净流入，电子化学品板块全天强势（西陇科学涨停），"
        "电子行业整体获逾133亿净流入居全行业首位；但全市场超4400只个股下跌，成交缩至1.63万亿创5个月新低，分化极端。\n"
        "【公司端】雅克科技9月15日发布2026年中期权益分派实施公告（10派3.5元，9月21日股权登记日）；"
        "铜冠铜箔召开2026年第三次临时股东会；英维克中标宝信软件889万元采购项目；江波龙当日回购15.17万股耗资4995万元（近一月累计回购6.53亿）。"
    )
)

# 3. Overnight market
overnight_html = """
<div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 12px; margin-bottom: 16px;">
    <div style="background: linear-gradient(135deg, rgba(239,68,68,0.18) 0%, rgba(185,28,28,0.08) 100%); border-radius: 12px; padding: 16px; border: 1px solid rgba(239,68,68,0.3); text-align: center;">
        <div style="font-size: 12px; color: #fca5a5; margin-bottom: 6px;">费城半导体</div>
        <div style="font-size: 22px; font-weight: 800; color: #f87171;">-5.86%</div>
        <div style="font-size: 11px; color: #fca5a5; margin-top: 4px;">30股全跌</div>
    </div>
    <div style="background: linear-gradient(135deg, rgba(239,68,68,0.12) 0%, rgba(185,28,28,0.06) 100%); border-radius: 12px; padding: 16px; border: 1px solid rgba(239,68,68,0.25); text-align: center;">
        <div style="font-size: 12px; color: #fca5a5; margin-bottom: 6px;">纳斯达克</div>
        <div style="font-size: 22px; font-weight: 800; color: #f87171;">-0.56%</div>
        <div style="font-size: 11px; color: #fca5a5; margin-top: 4px;">大盘窄幅调整</div>
    </div>
    <div style="background: linear-gradient(135deg, rgba(16,185,129,0.12) 0%, rgba(5,150,105,0.06) 100%); border-radius: 12px; padding: 16px; border: 1px solid rgba(16,185,129,0.25); text-align: center;">
        <div style="font-size: 12px; color: #6ee7b7; margin-bottom: 6px;">10Y美债收益率</div>
        <div style="font-size: 22px; font-weight: 800; color: #34d399;">5.01%</div>
        <div style="font-size: 11px; color: #6ee7b7; margin-top: 4px;">2007年以来新高</div>
    </div>
    <div style="background: linear-gradient(135deg, rgba(245,158,11,0.15) 0%, rgba(217,119,6,0.08) 100%); border-radius: 12px; padding: 16px; border: 1px solid rgba(245,158,11,0.25); text-align: center;">
        <div style="font-size: 12px; color: #fcd34d; margin-bottom: 6px;">布伦特原油</div>
        <div style="font-size: 22px; font-weight: 800; color: #fbbf24;">+1.02%</div>
        <div style="font-size: 11px; color: #fcd34d; margin-top: 4px;">105.68美元</div>
    </div>
</div>
<div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 14px;">
    <div style="background: rgba(255,255,255,0.04); border-radius: 12px; padding: 16px; border: 1px solid rgba(255,255,255,0.08);">
        <div style="font-size: 14px; font-weight: 700; color: #f1f5f9; margin-bottom: 10px;">核心半导体标的表现</div>
        <div style="display: flex; flex-direction: column; gap: 8px;">
            <div style="display: flex; justify-content: space-between;"><span style="font-size: 13px; color: #94a3b8;">泰瑞达</span><span style="font-size: 13px; font-weight: 600; color: #f87171;">-13.30%</span></div>
            <div style="display: flex; justify-content: space-between;"><span style="font-size: 13px; color: #94a3b8;">ARM</span><span style="font-size: 13px; font-weight: 600; color: #f87171;">-9.74%</span></div>
            <div style="display: flex; justify-content: space-between;"><span style="font-size: 13px; color: #94a3b8;">阿斯麦 ASML</span><span style="font-size: 13px; font-weight: 600; color: #f87171;">-7.25%</span></div>
            <div style="display: flex; justify-content: space-between;"><span style="font-size: 13px; color: #94a3b8;">SK海力士</span><span style="font-size: 13px; font-weight: 600; color: #f87171;">-7.60%</span></div>
            <div style="display: flex; justify-content: space-between;"><span style="font-size: 13px; color: #94a3b8;">美光科技</span><span style="font-size: 13px; font-weight: 600; color: #f87171;">-5.25%</span></div>
            <div style="display: flex; justify-content: space-between;"><span style="font-size: 13px; color: #94a3b8;">英特尔</span><span style="font-size: 13px; font-weight: 600; color: #f87171;">-5.00%+</span></div>
            <div style="display: flex; justify-content: space-between;"><span style="font-size: 13px; color: #94a3b8;">博通 AVGO</span><span style="font-size: 13px; font-weight: 600; color: #f87171;">-4.77%</span></div>
            <div style="display: flex; justify-content: space-between;"><span style="font-size: 13px; color: #94a3b8;">AMD</span><span style="font-size: 13px; font-weight: 600; color: #f87171;">-4.40%</span></div>
            <div style="display: flex; justify-content: space-between;"><span style="font-size: 13px; color: #94a3b8;">英伟达 NVDA</span><span style="font-size: 13px; font-weight: 600; color: #f87171;">-3.36%</span></div>
            <div style="display: flex; justify-content: space-between;"><span style="font-size: 13px; color: #94a3b8;">台积电ADR</span><span style="font-size: 13px; font-weight: 600; color: #f87171;">-3.0%+</span></div>
        </div>
    </div>
    <div style="background: rgba(255,255,255,0.04); border-radius: 12px; padding: 16px; border: 1px solid rgba(255,255,255,0.08);">
        <div style="font-size: 14px; font-weight: 700; color: #f1f5f9; margin-bottom: 10px;">全球指数与商品</div>
        <div style="display: flex; flex-direction: column; gap: 8px;">
            <div style="display: flex; justify-content: space-between;"><span style="font-size: 13px; color: #94a3b8;">道琼斯</span><span style="font-size: 13px; font-weight: 600; color: #f87171;">-0.29% / 52421</span></div>
            <div style="display: flex; justify-content: space-between;"><span style="font-size: 13px; color: #94a3b8;">标普500</span><span style="font-size: 13px; font-weight: 600; color: #f87171;">-0.48% / 7620</span></div>
            <div style="display: flex; justify-content: space-between;"><span style="font-size: 13px; color: #94a3b8;">恒生指数</span><span style="font-size: 13px; font-weight: 600; color: #f87171;">-1.00% / 24667</span></div>
            <div style="display: flex; justify-content: space-between;"><span style="font-size: 13px; color: #94a3b8;">日经225</span><span style="font-size: 13px; font-weight: 600; color: #f87171;">-0.90%</span></div>
            <div style="display: flex; justify-content: space-between;"><span style="font-size: 13px; color: #94a3b8;">富时100</span><span style="font-size: 13px; font-weight: 600; color: #34d399;">+0.77%</span></div>
            <div style="display: flex; justify-content: space-between;"><span style="font-size: 13px; color: #94a3b8;">WTI原油</span><span style="font-size: 13px; font-weight: 600; color: #fbbf24;">+1.37% / 102.78</span></div>
            <div style="display: flex; justify-content: space-between;"><span style="font-size: 13px; color: #94a3b8;">COMEX黄金</span><span style="font-size: 13px; font-weight: 600; color: #f87171;">-0.88% / 4313</span></div>
            <div style="display: flex; justify-content: space-between;"><span style="font-size: 13px; color: #94a3b8;">恐慌指数VIX</span><span style="font-size: 13px; font-weight: 600; color: #f87171;">+8% / 17.10</span></div>
            <div style="display: flex; justify-content: space-between;"><span style="font-size: 13px; color: #94a3b8;">美联储9月加息概率</span><span style="font-size: 13px; font-weight: 600; color: #f87171;">~90%</span></div>
        </div>
    </div>
</div>
"""

gen._components.append(Section(title="隔夜外盘跟踪", content=overnight_html, icon="globe"))

# 4. Industry chain
gen.add_industry_chain_analysis(
    upstream=[
        {
            "name": "半导体材料（光刻胶）",
            "desc": "日本三巨头10月起光刻胶全面涨价15%，HBM专用浸没式ArF最高涨24%。日本企业垄断全球70%+光刻胶份额、EUV约95%，涨价直接利好国内光刻胶国产替代。雅克科技（前驱体+光刻胶双布局）、南大光电（ArF光刻胶）直接受益。",
            "stocks": [
                {"code": "002409", "name": "雅克科技", "impact": "强（持仓）"},
                {"code": "300346", "name": "南大光电", "impact": "强"},
            ]
        },
        {
            "name": "半导体设备",
            "desc": "费城半导体暴跌下设备股重挫（阿斯麦-7.25%、应用材料-7%+、拉姆研究-8%+），但国产替代逻辑进一步强化。国内大基金三期持续加码，设备材料自主可控紧迫性提升。",
            "stocks": [
                {"code": "688082", "name": "盛美上海", "impact": "中"},
                {"code": "603690", "name": "至纯科技", "impact": "中"},
            ]
        },
        {
            "name": "电子布/覆铜板",
            "desc": "7628电子布出厂价11.5-12.1元/米，环比涨10%-20%，年内涨幅最高达162%。AI算力扩张带动高端CCL/电子布需求，涨价传导中。",
            "stocks": [
                {"code": "600176", "name": "中国巨石", "impact": "中"},
            ]
        },
    ],
    midstream=[
        {
            "name": "晶圆代工/先进制程",
            "desc": "AI减速担忧压制晶圆代工估值，但AI算力需求的长期逻辑未变——当前\"减速论\"仅限口头表态，无任何资本开支削减或订单下调的实质性变化。国产代工逻辑独立。",
            "stocks": [
                {"code": "688981", "name": "中芯国际", "impact": "中"},
            ]
        },
        {
            "name": "存储芯片",
            "desc": "SK海力士-7.6%、美光-5.25%、闪迪-4.98%，存储板块跟随大盘重挫。但存储行业供需基本面（三星+SK海力士库存不足10天）未变，股价下跌提供错杀布局机会。盘后存储芯片概念股小幅反弹（美光盘后+0.86%、SK海力士+0.96%）。",
            "stocks": [
                {"code": "301308", "name": "江波龙", "impact": "中（回购）"},
                {"code": "688525", "name": "佰维存储", "impact": "中"},
            ]
        },
        {
            "name": "铜箔/PCB（AI算力配套）",
            "desc": "AI算力扩张拉动高端铜箔/PCB需求，但外盘情绪压制板块表现。铜冠铜箔作为高端电子铜箔标的，受AI算力需求+国产替代双逻辑支撑。",
            "stocks": [
                {"code": "301217", "name": "铜冠铜箔", "impact": "中（持仓）"},
            ]
        },
    ],
    downstream=[
        {
            "name": "AI服务器/智算中心",
            "desc": "AI减速论短期冲击情绪，但产业逻辑未变——无任何厂商宣布削减资本开支。特朗普公开反对降速，黄仁勋也反对，政策面有支撑。国产算力链独立逻辑更强。",
            "stocks": [
                {"code": "000977", "name": "浪潮信息", "impact": "中"},
            ]
        },
        {
            "name": "光通信/光模块",
            "desc": "光通信跌幅最惨烈：康宁-13.7%、Coherent-12.73%、Lumentum-9.92%。光模块对AI资本开支敏感度最高，情绪冲击最大。但国产光模块全球竞争力强，需关注Q3订单数据验证。",
            "stocks": [
                {"code": "300308", "name": "中际旭创", "impact": "强"},
            ]
        },
        {
            "name": "液冷温控",
            "desc": "AI算力扩张驱动液冷需求长期增长逻辑未变。英维克短期情绪面偏弱但股权激励提供估值锚。外盘大跌下液冷板块波动加大，但长期需求确定性高。",
            "stocks": [
                {"code": "002837", "name": "英维克", "impact": "中（持仓）"},
            ]
        },
    ]
)

# 5. Investment opportunities
gen.add_investment_opportunities([
    {
        "name": "光刻胶国产替代（核心催化）",
        "priority": "S级",
        "logic": "日本JSR/东京应化/信越化学三大厂商10月1日起光刻胶全面涨价15%，HBM专用浸没式ArF最高涨24%，现货散单涨32%-38%。日本企业垄断全球70%以上光刻胶、EUV约95%份额，涨价既是成本传导更是供应链安全警示。国内光刻胶国产替代紧迫度大幅提升，雅克科技（光刻胶+前驱体双布局）、南大光电（ArF光刻胶）等直接受益。电子化学品板块今日已获资金追捧（西陇科学涨停）。",
        "stocks": [
            {"code": "002409", "name": "雅克科技", "impact": "强（持仓）"},
            {"code": "300346", "name": "南大光电", "impact": "强"},
            {"code": "002584", "name": "西陇科学", "impact": "强"},
        ]
    },
    {
        "name": "半导体国产替代（独立行情）",
        "priority": "A级",
        "logic": "外盘费半暴跌5.86%，但A股半导体今日逆势获得逾70亿主力净流入，电子行业整体133亿净流入居首，国产替代独立行情特征明显。\"AI减速论\"目前仅限于口头表态，无任何实质性资本开支削减，且特朗普和黄仁勋均公开反对减速。国产半导体设备/材料/设计受益于自主可控+大基金三期双重逻辑，在外围冲击下反而可能加速国产替代进程。",
        "stocks": [
            {"code": "688981", "name": "中芯国际", "impact": "强"},
            {"code": "688082", "name": "盛美上海", "impact": "中"},
        ]
    },
    {
        "name": "存储芯片（错杀机会）",
        "priority": "A级",
        "logic": "存储板块跟随大盘暴跌（SK海力士-7.6%、美光-5.25%），但存储行业供需基本面（三星+SK海力士DRAM库存不足10天、2027年或出现历史性短缺）未变。盘后存储芯片已现反弹（美光盘后+0.86%、SK海力士+0.96%）。若A股存储标的跟随外盘情绪回调，将是较好的错抄布局窗口。江波龙持续大额回购（近一月6.53亿）彰显信心。",
        "stocks": [
            {"code": "301308", "name": "江波龙", "impact": "中（回购托底）"},
            {"code": "688525", "name": "佰维存储", "impact": "中"},
        ]
    },
    {
        "name": "电子布/CCL涨价链",
        "priority": "B级",
        "logic": "7628电子布出厂价环比涨10%-20%，年内涨幅最高达162%。AI算力扩张拉动高端覆铜板需求，电子布作为上游材料持续涨价。玻璃玻纤板块指数连续7日上涨，宏和科技连涨7日，中国巨石/国际复材/中材科技连续5日上涨。",
        "stocks": [
            {"code": "600176", "name": "中国巨石", "impact": "中"},
            {"code": "603256", "name": "宏和科技", "impact": "强"},
        ]
    },
    {
        "name": "AI光模块（高弹性高波动）",
        "priority": "B级",
        "logic": "光通信板块跌幅最惨烈（康宁-13.7%、Coherent-12.73%），对AI资本开支敏感度最高。但国产光模块全球竞争力最强，若AI减速证实为\"口头表态\"而非实质性削减，光模块将迎来最强反弹。需等待Q3订单数据验证，左侧慎入。",
        "stocks": [
            {"code": "300308", "name": "中际旭创", "impact": "强"},
        ]
    },
], view_mode="tab")

# 6. Deep analysis
gen.add_catalyst_deep_analysis([
    {
        "title": "AI减速论本质辨析",
        "type": "macro",
        "description": "三巨头\"减速共识\"仅限口头表态，无任何资本开支削减/订单下调，且特朗普+黄仁勋公开反对，36小时两度反转",
        "category": "macro"
    },
    {
        "title": "光刻胶涨价的国产替代机遇",
        "type": "industry",
        "description": "日本三巨头10月起涨价15%-24%，全球70%份额被垄断，国内光刻胶国产替代紧迫度大幅升级",
        "category": "semiconductor"
    },
    {
        "title": "A股半导体独立行情验证",
        "type": "market",
        "description": "费半暴跌5.86%但A股半导体获70亿净流入，国产替代逻辑与外盘情绪脱钩，独立行情特征明确",
        "category": "semiconductor"
    },
])

# 7. Portfolio impact
portfolio_html = """
<div style="display: flex; flex-direction: column; gap: 12px;">
    <div style="background: linear-gradient(135deg, rgba(16,185,129,0.12) 0%, rgba(5,150,105,0.06) 100%); border-radius: 12px; padding: 16px; border: 1px solid rgba(16,185,129,0.25);">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
            <div style="display: flex; align-items: center; gap: 8px;">
                <span style="font-size: 18px;">🧪</span>
                <span style="font-size: 15px; font-weight: 700; color: #f1f5f9;">雅克科技（002409）</span>
                <span style="padding: 3px 8px; border-radius: 12px; font-size: 11px; font-weight: 600; background: rgba(16,185,129,0.2); color: #6ee7b7;">利好</span>
            </div>
            <span style="font-size: 13px; font-weight: 700; color: #fbbf24;">★★★★★ 强受益</span>
        </div>
        <div style="font-size: 13px; color: #cbd5e1; line-height: 1.7;">
            <strong>催化逻辑：</strong>日本三大光刻胶厂（JSR/东京应化/信越）10月1日起全面涨价15%，HBM专用浸没式ArF最高涨24%。雅克科技作为半导体材料龙头，光刻胶+前驱体双布局直接受益于国产替代加速。今日收涨3.69%，逆势走强验证催化有效性。<br>
            <strong>今日公告：</strong>2026年中期权益分派实施公告（10派3.5元，股权登记日9月21日，除权除息日9月22日），属中性偏正面。<br>
            <strong>风险点：</strong>外盘半导体暴跌可能引发情绪传导；A股整体缩量（1.63万亿创5个月新低），市场承接力不足。<br>
            <strong>双重验证：</strong>①日本JSR/东京应化/信越化学官宣涨价（多家媒体报道）；②今日电子化学品板块大涨、西陇科学涨停（盘面验证）；③雅克科技2026中期权益分派公告（深交所公告原文核实）。
        </div>
    </div>
    <div style="background: linear-gradient(135deg, rgba(59,130,246,0.10) 0%, rgba(37,99,235,0.05) 100%); border-radius: 12px; padding: 16px; border: 1px solid rgba(59,130,246,0.25);">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
            <div style="display: flex; align-items: center; gap: 8px;">
                <span style="font-size: 18px;">❄️</span>
                <span style="font-size: 15px; font-weight: 700; color: #f1f5f9;">英维克（002837）</span>
                <span style="padding: 3px 8px; border-radius: 12px; font-size: 11px; font-weight: 600; background: rgba(59,130,246,0.2); color: #93c5fd;">中性偏空</span>
            </div>
            <span style="font-size: 13px; font-weight: 700; color: #9ca3af;">★★★ 间接承压</span>
        </div>
        <div style="font-size: 13px; color: #cbd5e1; line-height: 1.7;">
            <strong>催化评估：</strong>AI减速论引发市场对AI算力投资放缓担忧，液冷作为算力配套环节间接承压。但当前"减速论"仅为口头表态，无实质资本开支削减，液冷长期需求逻辑未变。<br>
            <strong>今日表现：</strong>收59.84元（-0.28%），成交17.29亿元，远强于外盘半导体跌幅，显示A股液冷龙头韧性。近期股权激励（行权价46.73元）提供估值锚。<br>
            <strong>双重验证：</strong>①费城半导体暴跌5.86%（彭博/东方财富多源验证）；②英维克中标宝信软件889万元采购项目（公司公告）；③股权激励计划（9月10日公告）。<br>
            <strong>估值锚：</strong>PE(TTM)约155.8倍，PB约21.3倍。以2025年净利润为基数，2026年25%增长目标对应PE约35-40倍。技术支撑位58-60元，止损位55元。
        </div>
    </div>
    <div style="background: linear-gradient(135deg, rgba(245,158,11,0.10) 0%, rgba(217,119,6,0.08) 100%); border-radius: 12px; padding: 16px; border: 1px solid rgba(245,158,11,0.25);">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
            <div style="display: flex; align-items: center; gap: 8px;">
                <span style="font-size: 18px;">🔩</span>
                <span style="font-size: 15px; font-weight: 700; color: #f1f5f9;">铜冠铜箔（301217）</span>
                <span style="padding: 3px 8px; border-radius: 12px; font-size: 11px; font-weight: 600; background: rgba(245,158,11,0.2); color: #fcd34d;">中性</span>
            </div>
            <span style="font-size: 13px; font-weight: 700; color: #9ca3af;">★★★ 结构性影响</span>
        </div>
        <div style="font-size: 13px; color: #cbd5e1; line-height: 1.7;">
            <strong>催化评估：</strong>AI减速论对铜箔需求预期有间接压制，但电子布/CCL涨价潮（7628电子布年内涨幅最高162%）+AI算力高端铜箔需求增长形成对冲。整体中性，结构上高端电子铜箔优于锂电铜箔。<br>
            <strong>今日公告：</strong>2026年第三次临时股东会决议公告，程序性事项，无重大影响。<br>
            <strong>双重验证：</strong>①股东会决议公告（深交所原文核实，无否决案，属常规决议）；②电子布涨价数据（卓创资讯）；③上半年归母净利2.15亿同比+514.75%（中报）。
        </div>
    </div>
    <div style="background: linear-gradient(135deg, rgba(107,114,128,0.10) 0%, rgba(75,85,99,0.05) 100%); border-radius: 12px; padding: 16px; border: 1px solid rgba(107,114,128,0.25);">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
            <div style="display: flex; align-items: center; gap: 8px;">
                <span style="font-size: 18px;">🏗️</span>
                <span style="font-size: 15px; font-weight: 700; color: #f1f5f9;">*ST建艺（002789）</span>
                <span style="padding: 3px 8px; border-radius: 12px; font-size: 11px; font-weight: 600; background: rgba(107,114,128,0.2); color: #9ca3af;">中性</span>
            </div>
            <span style="font-size: 13px; font-weight: 700; color: #9ca3af;">★ 无直接关联</span>
        </div>
        <div style="font-size: 13px; color: #cbd5e1; line-height: 1.7;">
            <strong>催化评估：</strong>与AI减速/光刻胶涨价两大催化均无直接关联。今日跌4.18%收12.84元，成交5020万元，波动加大。公司核心逻辑仍在于庭外重组推进与摘帽预期。<br>
            <strong>今日无重大公告</strong>，继续作为组合防御端配置观察。
        </div>
    </div>
</div>
"""

gen._components.append(Section(title="持仓股影响评估", content=portfolio_html, icon="pie-chart", variant="highlight"))

# 8. Risk warnings
gen.add_risk_warning([
    "AI资本开支放缓风险（最高关注）：若\"AI减速论\"从口头表态演变为实质性削减资本开支，将对全球半导体产业链造成重大冲击。需密切关注云厂商/AI实验室的下一轮资本开支指引",
    "美联储加息风险：9月加息25bp概率已近90%，10年期美债收益率突破5%创2007年以来新高，高利率环境系统性压制成长股估值",
    "外盘情绪传导风险：费半暴跌5.86%创7月以来最大跌幅，A股半导体虽今日逆势，但需警惕次日情绪传导和补跌风险",
    "光刻胶涨价利好兑现风险：今日电子化学品板块已大涨（西陇科学涨停），部分资金可能借利好出货，短期需警惕冲高回落",
    "市场流动性风险：全市场成交缩至1.63万亿创5个月新低，超4400只个股下跌，存量博弈下板块轮动加速，持续性存疑",
    "持仓股风险：英维克浮亏较深需严守止损纪律；雅克科技利好兑现后短期可能回调；*ST建艺跌4.18%波动加大需关注"
])

# 9. Investment strategy
gen.add_investment_strategy(
    "<strong>整体策略：</strong>今日盘后S级催化呈现\"外空内多\"的复杂格局——费半暴跌5.86%+AI减速论（外盘利空），"
    "光刻胶涨价+A股半导体逆势70亿净流入（国内利好）。核心判断：<strong>AI减速论仅限口头表态，无实质资本开支削减，"
    "且特朗普+黄仁勋公开反对，短期情绪冲击大于实质影响</strong>。建议采取\"国产替代为主、精选错杀标的\"策略，"
    "仓位控制在5-6成，重点配置国产替代确定性强的半导体材料/设备，回避对海外AI资本开支敏感度高的光模块等环节。"
    "<br><br><strong>核心方向排序：</strong>光刻胶/半导体材料 ＞ 半导体设备/国产替代 ＞ 存储芯片（错抄） ＞ 液冷温控 ＞ 光模块"
    "<br><br><strong>持仓操作建议：</strong>"
    "<br>• <strong>雅克科技</strong>：今日逆势涨3.69%，光刻胶涨价+国产替代双催化直接受益，是本次S级催化最强受益标的。"
    "建议持有底仓，若因外盘情绪传导回调至120-125元区间可考虑加仓。<strong>估值锚：PE(TTM)约61倍，PB约7.9倍，"
    "处于历史合理区间。技术支撑位参考125-128元（20日均线附近），止损位115元</strong>"
    "<br>• <strong>英维克</strong>：今日仅跌0.28%表现强于板块，股权激励（行权价46.73元）提供估值锚。"
    "AI减速论间接压制情绪但液冷长期逻辑未变。建议继续持有观察，<strong>技术支撑位58-60元，若跌破55元坚决止损。"
    "估值锚：以2025年净利润为基数，2026年25%增长目标对应PE约35-40倍</strong>"
    "<br>• <strong>铜冠铜箔</strong>：电子布涨价+AI算力高端铜箔需求形成支撑，整体中性。"
    "继续持有观察，关注电子铜箔产能释放与高端认证进展"
    "<br>• <strong>*ST建艺</strong>：与催化关联度低，今日跌4.18%需警惕。继续作为防御端持有，但需关注重组进展与流动性"
    "<br><br><strong>明日关注：</strong>"
    "<br>① A股半导体板块能否延续独立行情，重点看成交额能否放大及雅克科技/西陇科学等龙头表现"
    "<br>② 美股盘前/盘中半导体是否企稳（关注存储芯片反弹持续性）"
    "<br>③ 美联储议息会议最新动向（9月15-16日召开，17日凌晨公布决议）"
    "<br>④ 光刻胶涨价催化的扩散程度（是否有更多国内厂商发布涨价或国产替代进展公告）"
    "<br>⑤ 龙虎榜机构动向（半导体板块是否有机构大额净买入/净卖出）"
    "<br><br><strong>数据来源：</strong>东方财富Choice、财联社、证券时报、第一财经、新浪财经、21世纪经济报道、彭博、TrendForce、CME FedWatch、深交所公告原文"
)

# Publish
result = gen.publish(
    title="AI减速恐慌费半暴跌6%+光刻胶涨价",
    report_type="s_level_catalyst",
    filename="20260915_盘后_S级催化扫描_AI减速+光刻胶涨价.html",
    excerpt="盘后双重S级催化：费城半导体暴跌5.86%创7月最大跌幅，AI三巨头呼吁减速引发资本开支放缓担忧；日本三巨头光刻胶10月起全面涨价15%，HBM专用最高涨24%，国产替代紧迫度升级。A股半导体逆势70亿净流入，独立行情验证。"
)

print("Report published:", result)
