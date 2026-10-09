#!/usr/bin/env python3
"""
S级催化扫描 - 2026年10月9日 盘后
核心催化：OpenAI营收不及预期引发AI硬件链深度调整+MLCC/PCB/光模块集体重挫+探底回升分化
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
    date_str="20261009",
    catalyst_title="OpenAI营收下修引发AI硬件链深度调整+探底回升分化",
    subtitle="2026.10.09 · 盘后S级催化"
)

# === 1. 催化事件概述 ===
gen.add_catalyst_overview(
    overview="""
    <p><strong>10月9日A股探底回升，AI硬件链遭遇第二波深度调整，OpenAI营收不及预期是核心导火索：</strong></p>
    <ol>
        <li><strong>OpenAI年化营收500亿美元 vs 市场预期700亿，差200亿美元</strong>：英国FT爆料OpenAI向投资者披露截至9月底年化营收"接近500亿美元"，而市场普遍预期为700亿。市场立即重新定价AI资本开支逻辑：连最赚钱的AI应用入口都只有这个数，云厂商千亿级算力资本开支能否兑现？隔夜美股纳指跌1.25%，费城半导体重挫3.39%，美光跌4.8%，英伟达跌2.9%。</li>
        <li><strong>MLCC板块崩盘，风华高科跌停，一日蒸发58亿</strong>：MLCC概念龙头风华高科封死跌停，国瓷材料跌超13%，昀冢科技跌超12%，宏达电子/火炬电子/三环集团全部跌超9%，MLCC指数单日下挫8个百分点以上。PCB/光通信同步跳水：中际旭创跌超5%失守年线，金安国纪封板跌停。</li>
        <li><strong>A股探底回升，三大指数集体收涨，风格极端切换</strong>：上证指数涨0.05%，深证成指涨0.17%，创业板指涨0.22%（跌破3000点后V型回升，70个交易日累计跌超31%）。两市成交额1.92万亿，近3300只个股上涨。文化传媒午后爆发（芒果超媒20cm），贵金属/农业/软件/券商领涨；通信设备/半导体探底回升，能源设备/军工/银行下跌。</li>
        <li><strong>美股盘前强力反弹，光通信+存储率先修复</strong>：Lumentum CEO称直至2029年初的光器件产能已全部售罄，盘前涨超4%；存储芯片普涨（美光+2%、SK海力士+2.2%）；英伟达涨2%。市场开始意识到OpenAI营收口径偏差（去年底200亿到今年9月500亿，实际增速依然惊人），恐慌情绪正在修复。</li>
        <li><strong>持仓股表现分化：铜冠铜箔跌5.11%，雅克科技探底回升，英维克跌2%</strong>。铜冠铜箔受MLCC/PCB板块联动拖累，但AI服务器铜箔需求逻辑未变；雅克科技探底回升幅度大，存储扩产逻辑坚实。</li>
    </ol>
    <p><strong>核心判断：</strong>本次AI硬件调整是预期层面的"二次校准"，而非基本面逆转。OpenAI从去年底200亿年化到今年9月500亿，增速依然惊人（9个月增150%），市场过度解读了"低于预期"。MLCC/PCB/光模块的暴跌是情绪传导+高位筹码松动，真正的基本面（AI服务器需求、存储涨价、光通信产能紧缺）均未改变。美股盘前强力反弹已验证修复逻辑。策略上：利用恐慌分批加仓基本面最硬的存储/PCB铜箔/光通信龙头，回避纯题材小票。</p>
    """,
    importance="高"
)

# === 2. 催化事件详解 ===
gen.add_catalyst_details(
    background="""
    <p><strong>背景一：AI硬件板块前期涨幅巨大，筹码结构脆弱</strong>。光模块、存储芯片、PCB铜箔等AI算力核心赛道今年涨幅惊人，部分龙头股涨幅超200-300%。融资盘扎堆，任何利空都可能触发剧烈调整。风华高科是融资客最集中的票之一，跌停板上几十万手封单，多杀多效应明显。</p>
    <p><strong>背景二：创业板指70个交易日跌超31%</strong>。2026年6月25日至今，创业板指从4400点上方一路下跌到3000点附近，跌幅超31%，创2025年11月27日以来新低。科技成长板块持续承压，AI硬件是少数维持高景气度的方向，因此"补跌"压力巨大。</p>
    <p><strong>背景三：Lumentum产能售罄至2029年，光通信基本面比想象中更紧</strong>。Lumentum CEO周五表示，由于科技公司争相建设更快的AI数据中心，该公司直至2029年初的光器件产能已全部售罄。部分产品明年仍有约70%需求无法满足，2028年还有30%缺口。这直接反驳了"AI资本开支见顶"的恐慌叙事。</p>
    <p><strong>背景四：景旺电子Q3业绩预增205%-265%，验证PCB高景气</strong>。10月9日盘后景旺电子披露2026Q3业绩预告，净利润9.12-10.89亿元，同比增205%-265%，核心驱动是高速通信、AI数据基建赛道的高性能PCB产品量产交付加速。AI硬件业绩实锤持续落地。</p>
    """,
    trigger="""
    <p><strong>触发因素一：FT爆料OpenAI年化营收500亿，低于市场预期700亿</strong>。英国《金融时报》报道，OpenAI向投资者提供的文件显示截至9月底年化营收"接近500亿美元"，而上个月市场广泛流传的口径还是700亿。200亿美元的差距直接动摇了"AI资本开支指数级增长"的叙事，全球AI硬件链集体下挫。</p>
    <p><strong>触发因素二：美股隔夜暴跌，情绪传导至A股</strong>。费城半导体指数跌3.39%，美光跌4.8%，博通跌4.3%，英伟达跌2.9%。光通信方向领跌：应用光电重挫逾13%，Coherent跌超9%，康宁/Lumentum跌超5%。A股开盘后AI硬件链直接跟跌。</p>
    <p><strong>触发因素三：MLCC龙头风华高科跌停引发板块连锁反应</strong>。风华高科封死跌停，一日蒸发58亿市值。作为AI服务器MLCC涨价逻辑的核心标的，其跌停带动整个电子元器件板块（PCB、光通信、半导体材料）联动下挫。融资盘集中的票出现多杀多。</p>
    <p><strong>触发因素四：三星手机Q4减产最高30%，消费电子需求担忧</strong>。三星电子MX事业部正式敲定Q4手机产量最高下调30%，供应链端已同步接到20-30%缩减通知。这加剧了市场对消费电子需求的担忧，但AI服务器需求与手机需求是两条完全不同的产业链。</p>
    <p><strong>触发因素五：A股自身探底回升，资金从硬科技流向防御+传媒</strong>。文化传媒午后爆发（芒果超媒20cm），贵金属/农业/软件/券商上涨。资金在科技板块调整时寻找避风港，但本质是轮动而非系统性撤离。</p>
    """
)

# === 3. 隔夜外盘+盘前表现 ===
gen._components.append(Section(
    title="🌍 隔夜外盘与盘前修复（双重验证）",
    icon="globe",
    content=DataGrid(cards=[
        DataCard(title="纳斯达克隔夜", value="27193", subtitle="OpenAI营收担忧", trend="-1.25%", trend_up=False, variant="danger"),
        DataCard(title="费城半导体隔夜", value="重挫", subtitle="AI硬件普跌", trend="-3.39%", trend_up=False, variant="danger"),
        DataCard(title="美光科技隔夜", value="跌4.8%", subtitle="存储龙头领跌", trend="-4.80%", trend_up=False, variant="danger"),
        DataCard(title="英伟达隔夜", value="跌2.9%", subtitle="市值蒸发1.13万亿", trend="-2.90%", trend_up=False, variant="danger"),
        DataCard(title="美股盘前修复", value="强力反弹", subtitle="Lumentum产能售罄催化", trend="芯片股普涨", trend_up=True, variant="success"),
        DataCard(title="Lumentum盘前", value="涨4%+", subtitle="产能售罄至2029年", trend="+4.23%", trend_up=True, variant="success"),
    ]).render() + """
    <div style="margin-top: 16px;">
        <div style="background: rgba(34,197,94,0.08); border: 1px solid rgba(34,197,94,0.25); border-radius: 14px; padding: 16px;">
            <div style="font-size: 14px; font-weight: 700; color: #4ade80; margin-bottom: 10px;">✅ 盘前修复信号（双重验证）</div>
            <div style="font-size: 13px; color: #bbf7d0; line-height: 1.8;">
                <p><strong>验证一：Lumentum CEO表态</strong>：截至2029年初光器件产能全部售罄，部分产品明年缺口70%。直接验证AI光通信需求持续紧张，反驳"资本开支见顶"叙事。</p>
                <p><strong>验证二：美股盘前集体反弹</strong>：截至18:00，Lumentum涨4.23%、应用光电涨超5%、Coherent涨3.36%、美光涨1.94%、SK海力士涨2.26%、英伟达涨2%。恐慌情绪快速消化。</p>
                <p><strong>验证三：OpenAI实际增速依然惊人</strong>：2025年底年化营收约200亿美元，2026年9月达500亿，9个月增长150%，年化增速约200%。所谓"不及预期"只是相对于700亿的乐观预期，而非基本面恶化。</p>
            </div>
        </div>
    </div>
    """
))

# === 4. A股今日龙虎榜异动 ===
gen._components.append(Section(
    title="📊 龙虎榜机构动向（10月9日）",
    icon="bar_chart",
    content="""
    <div style="background: rgba(239,68,68,0.08); border: 1px solid rgba(239,68,68,0.25); border-radius: 14px; padding: 20px; margin-bottom: 16px;">
        <div style="font-size: 15px; font-weight: 700; color: #f87171; margin-bottom: 12px;">⚠️ 机构净卖出前三</div>
        <div style="font-size: 13px; color: #fecaca; line-height: 2;">
            <p>1. <strong>陆家嘴</strong>：机构净卖出<strong>1.83亿元</strong>（跌8.72%，地产股持续承压）</p>
            <p>2. <strong>芒果超媒</strong>：机构净卖出<strong>1.05亿元</strong>（20cm涨停，机构借上涨减仓传媒）</p>
            <p>3. <strong>众生药业</strong>：机构净卖出<strong>5870万元</strong>（涨停，医药板块分歧）</p>
        </div>
        <div style="margin-top: 10px; font-size: 12px; color: #fca5a5;">
            注：今日机构净卖出方向集中在地产和涨停板兑现，AI硬件方向无大规模机构出逃（MLCC/PCB跌停股未上龙虎榜机构大额净卖）。
        </div>
    </div>
    <div style="background: rgba(34,197,94,0.08); border: 1px solid rgba(34,197,94,0.25); border-radius: 14px; padding: 20px;">
        <div style="font-size: 15px; font-weight: 700; color: #4ade80; margin-bottom: 12px;">✅ 机构净买入前三</div>
        <div style="font-size: 13px; color: #bbf7d0; line-height: 2;">
            <p>1. <strong>新华传媒</strong>：机构净买入<strong>1.12亿元</strong>（10cm涨停，传媒板块）</p>
            <p>2. <strong>吉林化纤</strong>：机构净买入<strong>8453万元</strong>（10%涨停，碳纤维/新材料）</p>
            <p>3. <strong>东岳硅材</strong>：机构净买入<strong>8427万元</strong>（20cm涨停，有机硅+半导体材料）</p>
        </div>
        <div style="margin-top: 10px; font-size: 12px; color: #86efac;">
            观察：机构净买入方向从AI硬件转向传媒/消费/新材料防御，东岳硅材（半导体材料方向）获机构认可，说明半导体材料逻辑仍受资金青睐。
        </div>
    </div>
    """
))

# === 5. 产业链分析 ===
gen.add_industry_chain_analysis(
    upstream=[
        {"name": "MLCC/被动元件", "desc": "OpenAI营收担忧+高位筹码松动，单日暴跌8%+，短期回避", "icon": "🧱",
         "stocks": [{"code":"000636","name":"风华高科","impact":"跌停·MLCC龙头·机构出逃"},{"code":"300285","name":"国瓷材料","impact":"跌13%·MLCC陶瓷粉"},{"code":"688260","name":"昀冢科技","impact":"跌12%·MLCC结构件"},{"code":"300726","name":"宏达电子","impact":"跌超9%·军工MLCC"}]},
        {"name": "半导体材料", "desc": "随板块调整但相对抗跌，存储扩产逻辑未变，中期仍看好", "icon": "🧪",
         "stocks": [{"code":"002409","name":"雅克科技","impact":"前驱体龙头（持仓）·探底回升"},{"code":"300821","name":"东岳硅材","impact":"有机硅·机构净买8427万"},{"code":"300054","name":"鼎龙股份","impact":"CMP抛光垫"}]},
        {"name": "半导体设备", "desc": "AI算力资本开支长期确定性高，短期情绪压制", "icon": "🔧",
         "stocks": [{"code":"688082","name":"盛美上海","impact":"清洗设备龙头"},{"code":"002371","name":"北方华创","impact":"设备龙头"},{"code":"688012","name":"中微公司","impact":"刻蚀设备"}]},
    ],
    midstream=[
        {"name": "存储芯片（DRAM/NAND）", "desc": "基本面最硬赛道，美光/SK海力士盘前涨2%+，调整后或率先修复", "icon": "💎",
         "stocks": [{"code":"688825","name":"长鑫科技","impact":"DRAM龙头"},{"code":"603986","name":"兆易创新","impact":"NOR龙头+回购"},{"code":"301308","name":"江波龙","impact":"存储模组+回购"},{"code":"688110","name":"东芯股份","impact":"全栈存储设计"}]},
        {"name": "PCB/铜箔", "desc": "MLCC带崩PCB，但景旺电子Q3增205%-265%验证景气，铜冠铜箔被错杀", "icon": "🌐",
         "stocks": [{"code":"301217","name":"铜冠铜箔","impact":"高端铜箔（持仓）·被情绪错杀"},{"code":"603228","name":"景旺电子","impact":"Q3增205-265%·业绩实锤"},{"code":"002463","name":"沪电股份","impact":"AI服务器PCB"},{"code":"300476","name":"胜宏科技","impact":"高端PCB"}]},
        {"name": "光通信/光模块", "desc": "Lumentum产能售罄至2029年，盘前涨4%+，A股今日错杀或迎修复", "icon": "📡",
         "stocks": [{"code":"300308","name":"中际旭创","impact":"光模块龙头·跌5%失守年线"},{"code":"300502","name":"新易盛","impact":"光模块核心"},{"code":"688498","name":"源杰科技","impact":"光芯片·前期大跌"}]},
    ],
    downstream=[
        {"name": "AI算力基础设施", "desc": "短期受情绪压制，中期资本开支确定性仍高，关注Q3财报季验证", "icon": "🖥️",
         "stocks": [{"code":"000977","name":"浪潮信息","impact":"AI服务器龙头"},{"code":"603019","name":"中科曙光","impact":"算力基础设施"}]},
        {"name": "液冷散热", "desc": "AI算力密度提升+液冷渗透率加速，英维克随板块调整", "icon": "❄️",
         "stocks": [{"code":"002837","name":"英维克","impact":"液冷龙头（持仓）·随板块调整"},{"code":"300137","name":"先河环保","impact":"液冷CDU"}]},
        {"name": "文化传媒/贵金属（防御）", "desc": "资金避风港，午后爆发，持续性存疑，不建议追高", "icon": "🎬",
         "stocks": [{"code":"300413","name":"芒果超媒","impact":"20cm涨停·机构净卖1.05亿"},{"code":"600825","name":"新华传媒","impact":"10cm涨停·机构净买1.12亿"},{"code":"601069","name":"西部黄金","impact":"贵金属防御"}]},
    ]
)

# === 6. 持仓股影响分析（双重验证） ===
gen._components.append(Section(
    title="💼 持仓股影响分析（双重验证）",
    icon="briefcase",
    variant="highlight",
    content=StockTags([
        {"code":"002837","name":"英维克","impact":"液冷龙头·跌2%·基本面未变·AI液冷渗透率持续提升"},
        {"code":"301217","name":"铜冠铜箔","impact":"高端铜箔·跌5.11%·MLCC/PCB情绪错杀·业绩逻辑未变"},
        {"code":"002409","name":"雅克科技","impact":"前驱体龙头·探底回升·存储扩产逻辑坚实"},
        {"code":"002789","name":"*ST建艺","impact":"ST板块·需跟踪庭外重组进展"},
    ]).render() + """
    <div style="margin-top: 20px;">
        <div style="background: rgba(59,130,246,0.08); border: 1px solid rgba(59,130,246,0.25); border-radius: 14px; padding: 16px;">
            <div style="font-size: 14px; font-weight: 700; color: #60a5fa; margin-bottom: 10px;">📝 铜冠铜箔下跌双重验证结论</div>
            <div style="font-size: 13px; color: #cbd5e1; line-height: 1.8;">
                <p><strong>验证信源1（下跌原因）</strong>：今日MLCC板块崩盘（风华高科跌停、MLCC指数跌8%），带动整个电子元器件/PCB/铜箔板块联动下跌。铜冠铜箔今日跌5.11%，盘中最低89.99元，收盘94.61元，明显探底回升。属于板块情绪传导，而非个股利空。</p>
                <p><strong>验证信源2（基本面实锤）</strong>：10月9日盘后景旺电子（603228）披露Q3业绩预告，净利润同比增205.46%-264.74%，核心驱动是AI数据基建高性能PCB量产交付加快。同赛道业绩实锤验证PCB铜箔高景气度未变。</p>
                <p><strong>结论</strong>：<span style="color: #4ade80;">情绪错杀</span>。铜冠铜箔下跌是MLCC崩盘带动的板块联动效应，AI服务器铜箔需求逻辑未变（景旺电子Q3业绩验证）。探底回升显示下方有承接，建议持有为主，回调可考虑加仓。</p>
            </div>
        </div>
    </div>
    <div style="margin-top: 12px;">
        <div style="background: rgba(168,85,247,0.08); border: 1px solid rgba(168,85,247,0.25); border-radius: 14px; padding: 16px;">
            <div style="font-size: 14px; font-weight: 700; color: #c084fc; margin-bottom: 10px;">📝 雅克科技下跌双重验证结论</div>
            <div style="font-size: 13px; color: #e9d5ff; line-height: 1.8;">
                <p><strong>验证信源1（下跌原因）</strong>：雅克科技今日早盘最低105.86元（跌8.26%），收盘回升至约112元（跌约3%），探底回升形态明确。下跌原因是半导体板块整体调整（AI硬件链普跌），无个股利空公告。</p>
                <p><strong>验证信源2（基本面）</strong>：雅克科技中报净利润稳健增长，电子材料业务持续放量，与韩国主要存储客户保持长期稳定合作关系。存储扩产周期下前驱体需求确定性高。美股盘前美光、SK海力士均涨2%+，存储情绪修复将传导至雅克。</p>
                <p><strong>结论</strong>：<span style="color: #4ade80;">情绪错杀+探底回升</span>。存储扩产逻辑未变，前驱体业务受益于晶圆厂产能扩张。探底回升显示资金认可当前价位，底仓持有，反弹至压力位可减仓机动仓。</p>
            </div>
        </div>
    </div>
    """
))

# === 7. 投资机会分析 ===
gen.add_investment_opportunities(
    opportunities=[
        {
            "title": "💎 存储芯片——基本面最硬，美股盘前已修复，A股或率先反弹",
            "level": "S级",
            "description": "OpenAI营收担忧引发的AI硬件调整是情绪面冲击，而非基本面逆转。存储芯片有三大实锤支撑：①美光、SK海力士美股盘前涨2%+，先行修复；②TrendForce预计Q4 DRAM/NAND延续双位数涨价；③Lumentum产能售罄至2029年反证AI资本开支仍在加速。存储涨价逻辑未被任何事件证伪。",
            "opportunity": "今日A股存储板块随大盘调整，但美股盘前已率先反弹，明日A股存储板块或迎来修复行情。重点关注：国产DRAM龙头（长鑫科技）、存储模组（江波龙，回购4-8亿）、NOR龙头（兆易创新，回购10-20亿）",
            "risk": "短期AI硬件整体情绪压制，可能继续震荡反复",
            "target_stocks": [{"code":"688825","name":"长鑫科技","impact":"DRAM龙头·率先修复"},{"code":"301308","name":"江波龙","impact":"模组龙头·回购4-8亿"},{"code":"603986","name":"兆易创新","impact":"NOR龙头·回购10-20亿"}]
        },
        {
            "title": "🌐 PCB/铜箔——景旺电子Q3业绩验证景气，铜冠被错杀",
            "level": "A级",
            "description": "今日MLCC崩盘带动PCB/铜箔板块联动下跌，但景旺电子盘后披露Q3净利增205%-265%，核心驱动是AI数据基建高性能PCB。PCB/铜箔与MLCC逻辑不同：MLCC既有消费电子又有AI服务器，而高端PCB/铜箔几乎纯受益于AI服务器需求。铜冠铜箔今日跌5.11%属情绪错杀。",
            "opportunity": "景旺电子Q3业绩将在明日发酵，PCB/铜箔板块或迎来业绩驱动的修复行情。铜冠铜箔作为持仓标的，AI服务器铜箔需求确定性高，回调即加仓机会。",
            "risk": "MLCC板块继续下跌可能继续拖累PCB情绪",
            "target_stocks": [{"code":"301217","name":"铜冠铜箔","impact":"高端铜箔（持仓）·错杀修复"},{"code":"603228","name":"景旺电子","impact":"Q3增205-265%·业绩实锤"},{"code":"002463","name":"沪电股份","impact":"AI服务器PCB龙头"}]
        },
        {
            "title": "📡 光通信——Lumentum产能售罄至2029年，A股今日错杀或迎强修复",
            "level": "A级",
            "description": "Lumentum CEO周五明确表态：截至2029年初的光器件产能已全部售罄，部分产品明年缺口70%。这直接反驳了\"AI资本开支见顶\"的恐慌叙事。美股盘前Lumentum涨4.23%、应用光电涨超5%、Coherent涨3.36%。A股光模块今日跟随下跌纯属情绪错杀。",
            "opportunity": "明日光模块板块有望迎来修复行情，中际旭创、新易盛等龙头或低开高走。但需注意前期光芯片板块（源杰科技、长光华芯）调整较深，修复力度可能分化。",
            "risk": "FCC禁令后续若进一步升级，对光模块出口影响需重新评估",
            "target_stocks": [{"code":"300308","name":"中际旭创","impact":"光模块龙头·错杀修复"},{"code":"300502","name":"新易盛","impact":"光模块核心·弹性大"},{"code":"688048","name":"长光华芯","impact":"光芯片·前期超跌"}]
        },
        {
            "title": "🧱 MLCC/被动元件——短期回避，等待情绪出清",
            "level": "C级（回避）",
            "description": "风华高科跌停带动MLCC板块单日跌8%+，融资盘集中的票出现多杀多。虽然AI服务器MLCC涨价逻辑未变，但短期筹码结构恶化，需要时间消化。OpenAI营收担忧可能反复发酵。",
            "opportunity": "等待跌停板打开+量能萎缩+机构资金回流后再考虑布局。MLCC行业高景气度未变，村田/三星电机/太阳诱电均发涨价函。",
            "risk": "融资盘平仓风险+消费电子需求担忧+AI资本开支预期下修",
            "target_stocks": [{"code":"000636","name":"风华高科","impact":"MLCC龙头·等待企稳"},{"code":"300285","name":"国瓷材料","impact":"MLCC陶瓷粉·观望"}]
        },
    ]
)

# === 8. 催化深度分析 ===
gen._components.append(Section(
    title="🧠 OpenAI营收真相：500亿到底是利空还是利好？",
    icon="brain",
    variant="highlight",
    content=DataGrid(cards=[
        DataCard(title="营收绝对增速", value="150%", subtitle="9个月200亿→500亿", trend="极快", trend_up=True, variant="success"),
        DataCard(title="相对预期差", value="-200亿", subtitle="vs 市场预期700亿", trend="低于预期", trend_up=False, variant="danger"),
        DataCard(title="AI资本开支周期", value="早期阶段", subtitle="仅0.5-1%IT支出", trend="刚起步", trend_up=True, variant="success"),
        DataCard(title="光通信需求验证", value="售罄至2029", subtitle="Lumentum官方", trend="极度紧缺", trend_up=True, variant="success"),
        DataCard(title="存储涨价确定性", value="Q4双位数", subtitle="TrendForce", trend="持续上涨", trend_up=True, variant="success"),
        DataCard(title="综合评级", value="80", subtitle="情绪冲击>实质影响", trend="逢低布局", trend_up=True, variant="primary"),
    ]).render() + '''
    <div style="margin-top: 16px;">
        <div style="background: rgba(251,191,36,0.08); border: 1px solid rgba(251,191,36,0.25); border-radius: 14px; padding: 16px;">
            <div style="font-size: 14px; font-weight: 700; color: #fbbf24; margin-bottom: 10px;">💡 核心逻辑拆解：为什么500亿不算利空？</div>
            <div style="font-size: 13px; color: #fef3c7; line-height: 1.8;">
                <p><strong>第一，绝对增速依然惊人。</strong>2025年底OpenAI年化营收约200亿美元，2026年9月达500亿，9个月增长150%，年化增速约200%。这样的增速放在任何行业都是顶级水平。市场之所以解读为利空，是因为之前预期太乐观（700亿），而非基本面恶化。</p>
                <p><strong>第二，AI资本开支与AI应用营收是两回事。</strong>OpenAI赚多少钱≠云厂商资本开支多少。谷歌、微软、亚马逊、Meta四大云厂商的资本开支计划是基于自身竞争战略的长期投入，不会因为OpenAI营收低200亿就砍掉几百亿的GPU订单。Lumentum产能售罄至2029年，就是最好的佐证。</p>
                <p><strong>第三，市场反应过度，修复速度会很快。</strong>美股盘前已经验证了这一点：芯片股普涨，光通信领涨。A股今日的恐慌性抛售（特别是MLCC/PCB方向）是情绪过头了，明日大概率修复。</p>
                <p style="color: #4ade80;"><strong>情景推演：</strong>乐观（+3~5%）美股芯片股今晚大涨+A股情绪修复（40%）/ 中性（-1~+2%）震荡磨底（40%） / 悲观（-3~-5%）恐慌延续（20%）。</p>
            </div>
        </div>
    </div>
    '''
))


# === 9. 投资策略建议 ===
gen.add_investment_strategy(
    strategy="""
    <p><strong>【整体仓位】</strong>科技板块第二次深度调整（第一次是10月8日光芯片崩盘），但基本面未发生实质逆转。建议<strong>总仓位保持60-70%</strong>，利用恐慌分批加仓基本面最硬的方向，保留30-40%现金应对极端情况。</p>
    <p><strong>【持仓操作建议】</strong></p>
    <ol>
        <li><strong>铜冠铜箔（301217）</strong>：今日跌5.11%，属于MLCC崩盘带动的情绪错杀。景旺电子Q3增205-265%验证PCB高景气。<strong>继续持有，回调至90元附近可加仓5-10%</strong>。估值锚：动态PE较高但业绩增速快（中报增514%），PEG合理。技术位支撑：前低89.99元/20日线。</li>
        <li><strong>英维克（002837）</strong>：今日跌2%，随科技板块调整，基本面未变。AI算力液冷渗透率持续提升是长期逻辑。<strong>持有为主</strong>，跌破50元整数关考虑减仓10%。估值锚：2026年PE约35倍。支撑位：50元整数关/前期低点。</li>
        <li><strong>雅克科技（002409）</strong>：今日探底回升（最低跌8.26%，收盘跌约3%），存储扩产逻辑未变，前驱体业务受益。<strong>底仓持有</strong>，反弹至120元附近可减仓机动仓。估值锚：PE约50倍（TTM），高于历史中位，但存储扩产周期下业绩有上修空间。支撑位：105-110元区间。</li>
        <li><strong>*ST建艺（002789）</strong>：庭外重组推进中，<strong>继续持有观察</strong>，严格执行止损纪律（跌破前低清仓）。</li>
    </ol>
    <p><strong>【明日关注方向】</strong></p>
    <ul>
        <li>光模块板块修复力度（Lumentum产能售罄消息能否带动A股光通信反弹）</li>
        <li>景旺电子Q3业绩发酵对PCB/铜箔板块的带动效应</li>
        <li>美股今晚芯片股走势（费半指数能否收复失地）</li>
        <li>存储板块是否率先修复（长鑫科技、江波龙）</li>
        <li>三季报业绩线（业绩预增股的持续性）</li>
    </ul>
    <p><strong>【核心原则】</strong>恐慌中不盲目杀跌，反弹中不盲目追高。OpenAI营收500亿不是利空，是预期校准。AI硬件的长期逻辑（算力需求指数级增长、存储涨价、光通信产能紧缺）没有任何改变。利用这次调整，优化持仓结构：加仓基本面最硬、业绩有实锤的标的（存储、PCB铜箔），减仓纯题材、估值过高的小票。控制仓位，分批布局，保留现金等待更好的击球点。</p>
    """
)

# === 10. 风险提示 ===
gen.add_risk_warning(
    risks=[
        "MLCC/PCB板块融资盘平仓风险，可能继续拖累AI硬件整体情绪",
        "美债收益率持续上行（30年期破5.7%），科技成长股估值承压",
        "中东局势升级，油价飙升加剧通胀担忧，强化美联储加息预期",
        "OpenAI营收担忧若进一步发酵（如更多机构下调AI资本开支预期），可能引发第二波调整",
        "FCC禁令后续若进一步升级，对光模块出口影响需重新评估",
        "创业板指破位下行（跌破3000点）可能引发系统性风险",
        "三星手机减产可能蔓延至消费电子供应链，影响部分半导体需求预期"
    ]
)

# === 发布 ===
if __name__ == "__main__":
    result = gen.publish(
        title="OpenAI营收下修引发AI硬件链深度调整+探底回升分化",
        filename="20261009_盘后_S级催化扫描_OpenAI营收预期+AI硬件调整.html"
    )
    print(f"发布结果: {result}")
