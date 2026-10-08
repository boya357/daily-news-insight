#!/usr/bin/env python3
"""
S级催化扫描 - 2026年10月8日 盘后
核心催化：光芯片板块20cm跌停潮+FCC禁令预期+AI硬件全面回调+存储板块相对韧性
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
    date_str="20261008",
    catalyst_title="光芯片崩盘+AI硬件重挫+存储韧性分化",
    subtitle="2026.10.08 · 盘后S级催化"
)

# === 1. 催化事件概述 ===
gen.add_catalyst_overview(
    overview="""
    <p><strong>国庆后首个交易日，AI硬件链遭遇史诗级分化调整，光芯片/CPO板块20cm跌停潮，存储板块相对抗跌展现韧性：</strong></p>
    <ol>
        <li><strong>光芯片/CPO板块集体崩盘</strong>：长光华芯、源杰科技双双20cm跌停，东山精密封死10%跌停板，仕佳光子跌超15%，德科立跌超10%，天孚通信跌超7%。机构净卖出源杰科技达14.36亿元，长光华芯净卖3.77亿。三重利空叠加：①大摩国庆期间发布FCC"受控清单"可能限制中国产光模块研报；②长光华芯董事长称光芯片长期存在降价可能；③源杰科技控股股东拟减持约4.9亿元。</li>
        <li><strong>科技成长全面重挫</strong>：科创50暴跌4.82%，创业板指重挫3.15%，半导体板块跌超4%。长鑫科技放量大跌7.79%，创8月11日以来新低，市值回落至3.43万亿。AI硬件板块（光通信+存储+半导体设备）全面承压。</li>
        <li><strong>隔夜外盘分化：费半跌1.15%，美光逆势涨4.06%</strong>：费城半导体指数跌1.15%，台积电ADR跌超2%，但美光科技逆市涨4.06%（D.A. Davidson上调目标价至3000美元，为华尔街最高）。纳指跌0.22%，道指跌0.66%。</li>
        <li><strong>存储板块展现相对韧性</strong>：三星Q3营业利润107.4万亿韩元，同比暴增782.5%，虽略低于预期但利润增速惊人。TrendForce预计Q4 DRAM/NAND合约价延续双位数上涨。长鑫科技G5平台量产，上半年营收同比增8.7倍。存储基本面逻辑最硬，但受AI硬件整体情绪拖累。</li>
        <li><strong>油价飙升至103美元，油气煤炭逆势走强</strong>：布伦特原油涨超4%突破103美元/桶，也门胡塞武装袭击沙特机场，中东局势升温。油气开采、煤炭等防御板块逆势上涨。</li>
    </ol>
    <p><strong>核心判断：</strong>今日AI硬件板块的集体重挫是三重利空叠加下的情绪宣泄，并非基本面逆转。光芯片的FCC禁令实质影响有限（最早3.2T代际落地，且有"美国含量豁免"），但市场选择第一时间定价供应链风险。存储板块基本面最硬（涨价逻辑未变），调整后或率先修复。持仓方面，铜冠铜箔今日逆势微涨展现铜箔赛道韧性，英维克/雅克科技跟随科技板块调整，*ST建艺跌5.08%（新增诉讼2999万，已双重验证为监管模板性公告，非实质性利空）。策略上，科技板块进入中期调整窗口，建议控制仓位至60%以下，优先加仓基本面最硬的存储与PCB铜箔赛道。</p>
    """,
    importance="极高"
)

# === 2. 催化事件详解 ===
gen.add_catalyst_details(
    background="""
    <p><strong>背景一：AI硬件板块前期涨幅巨大，拥挤度极高</strong>。光模块、光芯片、存储芯片作为AI算力核心赛道，今年以来涨幅均超过100%，部分龙头股涨幅超300%。筹码结构脆弱，任何利空都可能引发剧烈调整。</p>
    <p><strong>背景二：美债收益率创24年新高，压制科技成长估值</strong>。10年期美债收益率突破5.36%，30年期突破5.73%，均创2002年以来新高。期限溢价升至2011年以来最高。高利率环境对高估值科技股形成持续压制。</p>
    <p><strong>背景三：存储超级周期基本面依然坚实</strong>。TrendForce预计Q4企业级SSD合约价环比涨23-28%、整体NAND涨15-20%。美光Q4财报炸裂，DA Davidson上调目标价至3000美元。三星Q3营业利润同比增782.5%。AI驱动的存储需求是结构性的。</p>
    <p><strong>背景四：美联储9月加息25bp，年内或再加息一次</strong>。联邦基金利率升至3.75-4.00%，为2023年7月以来首次重启加息。多数官员认为年底前再加息一次可能合适。10月会议按兵不动概率约83%。</p>
    """,
    trigger="""
    <p><strong>触发因素一：大摩FCC"受控清单"研报引发光模块供应链恐慌</strong>。摩根士丹利国庆期间发布研报称，美国FCC可能通过"受控清单"机制限制中国产数据中心光模块进口，核心是"65%美国含量"规则，最早可能在3.2T代际分阶段落地。长光华芯、仕佳光子等公司均表示未收到降价相关消息，FCC禁令实质财务影响预计延至2027年后。</p>
    <p><strong>触发因素二：长光华芯董事长言论引发光芯片降价预期</strong>。长光华芯董事长在业绩交流会上表示，随着良率提升、产能扩充及新参与者进入，光芯片长期存在价格下降的可能。市场解读为行业价格战信号。</p>
    <p><strong>触发因素三：源杰科技控股股东拟减持约4.9亿元</strong>。源杰科技控股股东及一致行动人9月底披露上市以来首份减持计划，合计拟减持不超过28.85万股，潜在套现约4.9亿元。机构今日净卖出14.36亿元，为龙虎榜机构净卖出榜首。</p>
    <p><strong>触发因素四：三星Q3利润虽增782%但略低于预期</strong>。三星Q3营业利润107.4万亿韩元，同比增782.5%，但低于市场预期的108.7万亿韩元。市场对存储涨价斜率的定价已非常苛刻，"不及预期"即引发抛售。</p>
    <p><strong>触发因素五：中东局势升温，油价飙升推升通胀担忧</strong>。也门胡塞武装袭击沙特机场，布伦特原油涨超4%突破103美元。油价上涨加剧通胀担忧，强化美联储加息预期，进一步压制科技成长股。</p>
    """
)

# === 3. 隔夜外盘表现数据卡片 ===
gen._components.append(Section(
    title="🌍 隔夜外盘核心数据（盘后更新）",
    icon="globe",
    content=DataGrid(cards=[
        DataCard(title="纳斯达克", value="27538.69", subtitle="科技股普跌", trend="-0.22%", trend_up=False, variant="primary"),
        DataCard(title="费城半导体", value="13066.15", subtitle="芯片股普跌", trend="-1.15%", trend_up=False, variant="danger"),
        DataCard(title="美光科技", value="逆势上涨", subtitle="目标价上调至$3000", trend="+4.06%", trend_up=True, variant="success"),
        DataCard(title="台积电ADR", value="跌超2%", subtitle="9月营收同比+54.6%", trend="-2.09%", trend_up=False, variant="danger"),
        DataCard(title="三星电子", value="-2.42%", subtitle="Q3利润增782%", trend="韩股下跌", trend_up=False, variant="danger"),
        DataCard(title="SK海力士", value="-2.44%", subtitle="HBM龙头跟跌", trend="韩股调整", trend_up=False, variant="danger"),
    ]).render()
))

# === 4. A股今日龙虎榜异动 ===
gen._components.append(Section(
    title="📊 龙虎榜机构动向（10月8日）",
    icon="bar_chart",
    content="""
    <div style="background: rgba(239,68,68,0.08); border: 1px solid rgba(239,68,68,0.25); border-radius: 14px; padding: 20px; margin-bottom: 16px;">
        <div style="font-size: 15px; font-weight: 700; color: #f87171; margin-bottom: 12px;">⚠️ 机构净卖出前三（光芯片集体出逃）</div>
        <div style="font-size: 13px; color: #fecaca; line-height: 2;">
            <p>1. <strong>源杰科技</strong>：机构净卖出<strong>14.36亿元</strong>（20cm跌停，控股股东减持+FCC禁令双重利空）</p>
            <p>2. <strong>长光华芯</strong>：机构净卖出<strong>3.77亿元</strong>（20cm跌停，董事长降价言论冲击）</p>
            <p>3. <strong>仕佳光子</strong>：机构净卖出<strong>3.34亿元</strong>（跌超15%，光芯片板块联动调整）</p>
        </div>
        <div style="margin-top: 10px; font-size: 12px; color: #fca5a5;">
            注：光芯片板块机构净卖出超21亿元，为今日资金流出最集中方向。源杰科技单股14.36亿机构出逃，说明机构对光芯片板块估值体系产生分歧。
        </div>
    </div>
    <div style="background: rgba(34,197,94,0.08); border: 1px solid rgba(34,197,94,0.25); border-radius: 14px; padding: 20px;">
        <div style="font-size: 15px; font-weight: 700; color: #4ade80; margin-bottom: 12px;">✅ 机构净买入前三</div>
        <div style="font-size: 13px; color: #bbf7d0; line-height: 2;">
            <p>1. <strong>中石科技</strong>：机构净买入<strong>3.32亿元</strong>（导热材料，AI散热概念）</p>
            <p>2. <strong>新华传媒</strong>：机构净买入<strong>1.14亿元</strong>（传媒板块）</p>
            <p>3. <strong>奥佳华</strong>：机构净买入<strong>9850万元</strong>（按摩椅，消费复苏）</p>
        </div>
        <div style="margin-top: 10px; font-size: 12px; color: #86efac;">
            观察：机构净买入方向从AI硬件转向消费/传媒等防御性板块，AI散热赛道（中石科技）仍获机构认可。
        </div>
    </div>
    """
))

# === 5. 产业链分析 ===
gen.add_industry_chain_analysis(
    upstream=[
        {"name": "光芯片/光模块", "desc": "FCC禁令预期+降价担忧+减持三重利空，机构大规模出逃，短期回避", "icon": "📡",
         "stocks": [{"code":"688498","name":"源杰科技","impact":"机构净卖14.36亿·利空出尽前回避"},{"code":"688048","name":"长光华芯","impact":"20cm跌停·降价言论冲击"},{"code":"688313","name":"仕佳光子","impact":"机构净卖3.34亿·板块联动"},{"code":"300620","name":"光库科技","impact":"光器件"}]},
        {"name": "半导体材料", "desc": "科技板块调整中相对抗跌，存储扩产逻辑未变，中期仍看好", "icon": "🧪",
         "stocks": [{"code":"002409","name":"雅克科技","impact":"前驱体龙头（持仓）"},{"code":"688535","name":"华海诚科","impact":"GMC塑封料"},{"code":"300054","name":"鼎龙股份","impact":"CMP抛光垫"}]},
        {"name": "半导体设备", "desc": "盛美上海在手订单170.73亿，同比增88.2%，行业景气度验证", "icon": "🔧",
         "stocks": [{"code":"688082","name":"盛美上海","impact":"在手订单170亿+"},{"code":"002371","name":"北方华创","impact":"设备龙头"},{"code":"688012","name":"中微公司","impact":"刻蚀设备"}]},
    ],
    midstream=[
        {"name": "存储芯片（DRAM/NAND）", "desc": "基本面最硬赛道，三星利润增782%+美光目标价3000美元，调整后或率先修复", "icon": "💎",
         "stocks": [{"code":"688825","name":"长鑫科技","impact":"DRAM龙头·G5平台量产"},{"code":"603986","name":"兆易创新","impact":"回购10-20亿+NOR龙头"},{"code":"301308","name":"江波龙","impact":"回购4-8亿+存储模组"},{"code":"688110","name":"东芯股份","impact":"全栈存储设计"}]},
        {"name": "PCB/铜箔", "desc": "今日AI硬件链中最抗跌赛道，铜冠铜箔逆势微涨，高端PCB需求确定", "icon": "🌐",
         "stocks": [{"code":"301217","name":"铜冠铜箔","impact":"高端铜箔（持仓）"},{"code":"002463","name":"沪电股份","impact":"AI服务器PCB"},{"code":"300476","name":"胜宏科技","impact":"高端PCB"},{"code":"688722","name":"中一科技","impact":"锂电铜箔+PCB铜箔"}]},
        {"name": "先进封装", "desc": "HBM封装+Chiplet，存储与AI算力核心受益环节，回调中布局机会", "icon": "📦",
         "stocks": [{"code":"600584","name":"长电科技","impact":"HBM封装龙头"},{"code":"002156","name":"通富微电","impact":"AMD核心封测伙伴"},{"code":"688362","name":"甬矽电子","impact":"回购1-1.5亿"}]},
    ],
    downstream=[
        {"name": "AI算力基础设施", "desc": "短期受情绪压制，中期资本开支确定性仍高，关注Q3财报验证", "icon": "🖥️",
         "stocks": [{"code":"000977","name":"浪潮信息","impact":"AI服务器龙头"},{"code":"603019","name":"中科曙光","impact":"算力基础设施"}]},
        {"name": "液冷散热", "desc": "AI算力密度持续提升，液冷渗透率加速，英维克跟随板块调整", "icon": "❄️",
         "stocks": [{"code":"002837","name":"英维克","impact":"液冷龙头（持仓）"},{"code":"300137","name":"先河环保","impact":"液冷CDU"}]},
        {"name": "油气/煤炭（防御）", "desc": "油价破103美元，中东局势升温，防御性板块逆势走强", "icon": "🛢️",
         "stocks": [{"code":"601857","name":"中国石油","impact":"油气龙头"},{"code":"601088","name":"中国神华","impact":"煤炭龙头"},{"code":"600028","name":"中国石化","impact":"炼化一体化"}]},
    ]
)

# === 6. 持仓股影响分析（双重验证） ===
gen._components.append(Section(
    title="💼 持仓股影响分析（双重验证）",
    icon="briefcase",
    variant="highlight",
    content=StockTags([
        {"code":"002837","name":"英维克","impact":"液冷龙头·随科技板块调整·基本面未变"},
        {"code":"301217","name":"铜冠铜箔","impact":"高端铜箔·今日逆势微涨·PCB铜箔韧性强"},
        {"code":"002409","name":"雅克科技","impact":"前驱体龙头·随半导体调整·存储扩产逻辑未变"},
        {"code":"002789","name":"*ST建艺","impact":"新增诉讼2999万·模板性公告·非实质性利空"},
    ]).render() + """
    <div style="margin-top: 20px;">
        <div style="background: rgba(59,130,246,0.08); border: 1px solid rgba(59,130,246,0.25); border-radius: 14px; padding: 16px;">
            <div style="font-size: 14px; font-weight: 700; color: #60a5fa; margin-bottom: 10px;">📝 *ST建艺诉讼公告双重验证结论</div>
            <div style="font-size: 13px; color: #cbd5e1; line-height: 1.8;">
                <p><strong>验证信源1（公告原文）</strong>：*ST建艺2026-10-08公告《关于新增累计诉讼、仲裁情况的公告》（公告编号2026-100），新增累计诉讼金额约2999.84万元，占最近一期经审计净资产绝对值的14.58%。涉案金额800万以上仅1起（1734万元，建设工程纠纷，一审待开庭）。</p>
                <p><strong>验证信源2（历史规律）</strong>：*ST建艺今年已多次发布同类公告（7月28日、7月29日、7月31日、9月22日），均为装饰工程行业正常诉讼累计披露，属于<strong>监管模板性风险提示</strong>，非新增实质性利空。</p>
                <p><strong>结论</strong>：<span style="color: #fbbf24;">中性事件</span>。今日下跌5.08%主要受大盘拖累+ST板块情绪影响，诉讼公告为常规披露，不构成减仓理由。庭外重组仍在推进中，继续持有观察重组进展。</p>
            </div>
        </div>
    </div>
    """
))

# === 7. 投资机会分析 ===
gen.add_investment_opportunities(
    opportunities=[
        {
            "title": "💎 存储芯片——基本面最硬，调整后优先修复",
            "level": "S级",
            "description": "光芯片崩盘引发AI硬件整体调整，但存储板块基本面最坚实：①三星Q3利润增782.5%；②美光目标价上调至3000美元（DA Davidson）；③TrendForce预计Q4 DRAM/NAND延续双位数涨价；④长鑫科技G5平台量产，上半年营收增8.7倍。存储涨价逻辑未被任何事件证伪。",
            "opportunity": "今日调整为情绪错杀，存储板块或率先迎来修复。重点关注：国产DRAM龙头（长鑫科技）、存储模组（江波龙，回购4-8亿）、NOR龙头（兆易创新，回购10-20亿）",
            "risk": "短期AI硬件整体情绪压制，可能继续震荡",
            "target_stocks": [{"code":"688825","name":"长鑫科技","impact":"DRAM龙头·G5平台"},{"code":"301308","name":"江波龙","impact":"模组龙头·回购4-8亿"},{"code":"603986","name":"兆易创新","impact":"NOR龙头·回购10-20亿"}]
        },
        {
            "title": "🌐 PCB/铜箔——AI硬件链最抗跌赛道",
            "level": "A级",
            "description": "铜冠铜箔今日逆势微涨0.14%，在AI硬件全线大跌中展现极强韧性。高端PCB/铜箔需求受益于AI服务器+800G/1.6T光模块双轮驱动，景气度确定性高。",
            "opportunity": "AI硬件调整中资金流向基本面更确定的PCB/铜箔赛道，铜冠铜箔作为持仓标的表现亮眼",
            "risk": "铜价波动风险",
            "target_stocks": [{"code":"301217","name":"铜冠铜箔","impact":"高端铜箔（持仓）"},{"code":"002463","name":"沪电股份","impact":"AI服务器PCB"},{"code":"300476","name":"胜宏科技","impact":"高端PCB"}]
        },
        {
            "title": "📡 光芯片/CPO——短期回避，等待利空出尽",
            "level": "C级（回避）",
            "description": "三重利空（FCC禁令预期+降价担忧+减持）叠加下，光芯片板块机构大规模出逃（单日净卖出超21亿元）。虽然FCC禁令实质影响有限（最早3.2T代际落地），但短期筹码结构恶化，需要时间消化。",
            "opportunity": "等待机构卖盘释放完毕+板块企稳后再考虑布局。光模块行业高景气度未变，2027年光通信行业高景气度确定性较高（高盛上调出货量预测31%）",
            "risk": "短期继续下跌风险，机构持仓调整未完成",
            "target_stocks": [{"code":"300308","name":"中际旭创","impact":"光模块龙头·等待企稳"},{"code":"300502","name":"新易盛","impact":"光模块核心·观望"}]
        },
    ]
)

# === 8. 催化深度分析 ===
gen._components.append(Section(
    title="🧠 存储板块深度研判：情绪错杀还是基本面拐点？",
    icon="brain",
    variant="highlight",
    content=DataGrid(cards=[
        DataCard(title="涨价确定性", value="95", subtitle="Q4延续双位数涨", trend="极高", trend_up=True, variant="success"),
        DataCard(title="需求持续性", value="90", subtitle="AI+消费电子双轮", trend="强", trend_up=True, variant="success"),
        DataCard(title="供给纪律性", value="85", subtitle="原厂扩产克制", trend="较强", trend_up=True, variant="primary"),
        DataCard(title="估值合理性", value="55", subtitle="长鑫分歧大", trend="中等", trend_up=False, variant="default"),
        DataCard(title="短期情绪面", value="30", subtitle="AI硬件普跌拖累", trend="弱", trend_up=False, variant="danger"),
        DataCard(title="综合评分", value="71", subtitle="基本面>情绪面", trend="偏多", trend_up=True, variant="primary"),
    ]).render() + '''
    <div style="margin-top: 16px;">
        <div style="background: rgba(168,85,247,0.08); border: 1px solid rgba(168,85,247,0.25); border-radius: 14px; padding: 16px;">
            <div style="font-size: 14px; font-weight: 700; color: #c084fc; margin-bottom: 10px;">💡 核心结论与情景推演</div>
            <div style="font-size: 13px; color: #e9d5ff; line-height: 1.8;">
                <p><strong>判断：今日存储板块调整为情绪错杀，非基本面拐点。</strong></p>
                <p><strong>支撑理由：</strong>①美光逆势涨4.06%，DA Davidson上调目标价至3000美元；②TrendForce确认Q4存储合约价延续双位数上涨；③三星Q3利润增782.5%，虽略低于预期但增速惊人；④长鑫科技G5平台量产，国产替代加速。</p>
                <p><strong>风险点：</strong>①美债收益率创新高压制估值；②长鑫科技融资余额持续下降（杠杆资金撤离）；③东芝扩产HDD被解读为供给纪律松动。</p>
                <p style="color: #fbbf24;"><strong>情景推演：</strong>乐观（+3~5%）美光创新高传导+资金回流基本面最硬赛道（30%）/ 中性（-1~+2%）震荡整理（50%） / 悲观（-3~-5%）AI硬件情绪传导继续下探（20%）。</p>
            </div>
        </div>
    </div>
    '''
))


# === 9. 投资策略建议 ===
gen.add_investment_strategy(
    strategy="""
    <p><strong>【整体仓位】</strong>科技板块进入中期调整窗口，建议<strong>总仓位控制在60%以下</strong>，预留弹药应对进一步调整。当前市场处于"估值重估+情绪宣泄"阶段，不宜急于抄底。</p>
    <p><strong>【持仓操作建议】</strong></p>
    <ol>
        <li><strong>铜冠铜箔（301217）</strong>：今日逆势微涨展现韧性，AI服务器PCB+高端铜箔需求确定性高，<strong>继续持有</strong>，回调可加仓。估值锚：动态PE约25倍，处于历史中位偏低位置。技术位支撑：20日线。</li>
        <li><strong>英维克（002837）</strong>：液冷龙头，随科技板块调整，基本面未变（AI算力液冷渗透率持续提升），<strong>持有为主</strong>，跌破60日线考虑减仓10-20%。估值锚：2026年PE约35倍，处于历史较高分位。支撑位：60日线。</li>
        <li><strong>雅克科技（002409）</strong>：前驱体龙头，存储扩产逻辑未变，<strong>底仓持有</strong>，反弹至压力位减仓机动仓。估值锚：PE约40倍，高于历史中位。支撑位：120日线。</li>
        <li><strong>*ST建艺（002789）</strong>：新增诉讼为模板性公告，非实质性利空（双重验证通过）。庭外重组推进中，<strong>继续持有观察</strong>，严格执行止损纪律（跌破前低清仓）。</li>
    </ol>
    <p><strong>【明日关注方向】</strong></p>
    <ul>
        <li>优先观察存储板块修复力度（长鑫科技、江波龙、兆易创新）</li>
        <li>光芯片板块是否企稳（源杰科技、长光华芯是否继续跌停）</li>
        <li>隔夜美股半导体表现（费半指数、美光科技走势）</li>
        <li>三季报业绩线（业绩预增股的持续性）</li>
    </ul>
    <p><strong>【核心原则】</strong>调整中不恐慌，聚焦基本面。存储涨价逻辑未被证伪，AI算力长期趋势不变。光芯片板块的FCC禁令实质影响有限，等待利空出尽后仍是优质赛道。控制仓位，分批布局，保留现金等待更好的击球点。</p>
    """
)

# === 10. 风险提示 ===
gen.add_risk_warning(
    risks=[
        "光芯片板块机构出逃未完成，短期可能继续拖累AI硬件整体情绪",
        "美债收益率持续上行，科技成长股估值承压",
        "中东局势升级，油价飙升加剧通胀担忧，强化美联储加息预期",
        "三星Q3利润略低于预期，存储涨价斜率可能低于市场最乐观预期",
        "FCC禁令后续若进一步升级，对光模块出口影响需重新评估",
        "科创50破位下行可能引发融资盘平仓，加剧市场波动"
    ]
)

# === 发布 ===
if __name__ == "__main__":
    result = gen.publish(
        title="光芯片崩盘+AI硬件重挫+存储韧性分化",
        filename="20261008_盘后_S级催化扫描_光芯片崩盘+AI硬件重挫.html"
    )
    print(f"发布结果: {result}")
