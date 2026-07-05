"""
2026年7月5日 周末速递生成脚本
使用 WeekendExpressGenerator V3.0
"""
import sys, os
sys.path.insert(0, 'v3')
os.chdir('/app/data/所有对话/主对话')

from v3.generators.weekend_express import WeekendExpressGenerator

gen = WeekendExpressGenerator(
    date_str="20260705",
    subtitle="2026.07.05 · 周末速递 | 十五五政策密集落地+A股交易新规周一实施+中报预告潮来袭"
)

# ============ 1. 周末要闻速览 ============
highlights = [
    {
        'icon': '🏛️',
        'title': '国常会重磅部署！审议通过"十五五"碳达峰行动方案+深入实施"人工智能+"行动',
        'content': '6月29日国常会双料重磅：①审议通过《"十五五"碳达峰行动方案》，政策逻辑从"减碳是代价"转向"绿色是红利"，强调战略牵引、能源结构调整和碳排放考核硬约束；②听取人工智能发展汇报，要求"加力推进AI创新突破，加快关键技术攻关和超大规模智算集群建设，深入实施人工智能+行动"。算力基建获顶层定调。',
        'tag': '顶层政策',
        'importance': 'high',
        'source': '新华社/中国政府网',
        'time': '6月29日'
    },
    {
        'icon': '📋',
        'title': '发改委印发《循环经济发展"十五五"规划》：2030年产业产值达8万亿',
        'content': '7月4日发改委印发规划，明确2030年主要资源产出率较2025年提升约16%，大宗固废年综合利用量45亿吨、再生资源年循环利用量5.1亿吨，产业产值突破8万亿元（复合增速约10%）。亮点是精准补齐"新三样"（新能源车、光伏、锂电池）固废循环利用短板，利好回收龙头。',
        'tag': '部委政策',
        'importance': 'high',
        'source': '国家发改委',
        'time': '7月4日'
    },
    {
        'icon': '💰',
        'title': '央行重磅！7月6日开展1万亿3个月期买断式逆回购，时隔3月重启净投放',
        'content': '央行公告7月6日开展10000亿元3个月期买断式逆回购（当日到期8000亿元），净投放2000亿元，正式结束连续3个月缩量回笼节奏。叠加6月25日MLF加量2000亿，6月29-30日隔夜逆回购9000亿呵护跨月，释放明确宽货币信号。中信证券明明团队：这是今年3月以来首次净投放，宽松取向明确。',
        'tag': '货币政策',
        'importance': 'high',
        'source': '央行官网',
        'time': '7月3日'
    },
    {
        'icon': '🏭',
        'title': '工信部等八部门发布工业互联网意见：2030年建成5万张工业5G专网',
        'content': '工信部等八部门联合发布《关于推动工业互联网高质量发展的实施意见》，提出到2030年建设5万张工业5G专网，核心产业增加值突破2.5万亿元。配套八部门+国资委人形机器人实景实训专项行动推进，工业智能化改造订单加速释放。',
        'tag': '产业政策',
        'importance': 'high',
        'source': '工信部',
        'time': '本周'
    },
    {
        'icon': '🚗',
        'title': '财政部三部门：2027年起取消新能源汽车/节能汽车车船税优惠',
        'content': '财政部等三部门公告，自2027年1月1日起，取消对节能汽车减半征收车船税政策，取消纯电动商用车、插混商用车、燃料电池商用车免征车船税政策。新能源车购置优惠逐步退出预期增强。',
        'tag': '财税政策',
        'importance': 'normal',
        'source': '财政部',
        'time': '本周'
    },
    {
        'icon': '⛽',
        'title': '国内成品油年内最大降幅！汽柴油每吨分别下调950/915元',
        'content': '7月3日24时调价窗口开启，汽柴油零售限价每吨分别下调950元、915元，创2026年年内最大降幅。油价下跌利好航空、物流、化工下游。',
        'tag': '大宗商品',
        'importance': 'normal',
        'source': '发改委',
        'time': '7月3日'
    },
    {
        'icon': '📊',
        'title': '6月制造业PMI重返扩张区间：50.3%，环比+0.3pct',
        'content': '国家统计局数据，6月制造业PMI为50.3%，比上月上升0.3个百分点，时隔2月重返扩张区间，经济边际改善信号显现。',
        'tag': '宏观数据',
        'importance': 'normal',
        'source': '国家统计局',
        'time': '6月30日'
    },
    {
        'icon': '🤖',
        'title': '宇树科技科创板IPO注册获批！A股人形机器人第一股诞生在即',
        'content': '7月2日证监会同意宇树科技科创板IPO注册，从3月20日获受理到注册生效仅104天，创科创板预先审阅机制以来最快纪录，发行市值预计约400亿元，2026上半年营收同比增长近40%。将成为A股"人形机器人/具身智能第一股"，催化板块情绪。',
        'tag': '资本事件',
        'importance': 'high',
        'source': '证监会/上交所',
        'time': '7月2日'
    },
    {
        'icon': '💾',
        'title': '存储业绩炸裂！江波龙中报预增622倍-744倍，三星Q3再传涨价20%',
        'content': '①江波龙7月3日晚发布中报预告：上半年净利润92-110亿元，同比增长62204%-74394%（一季度单季净利38.6亿，Q2预计53-71亿环比+38%-84%）；②三星传Q3通用DRAM售价环比再提20%（LPDDR超20%），若落地则今年累计涨幅达340%，高盛称供需不平衡达近15年高峰。⚠️但本周存储板块剧烈波动，周四周五龙头单日跌超10%，分歧巨大。',
        'tag': '产业/业绩',
        'importance': 'high',
        'source': '公司公告/第一财经',
        'time': '7月3日'
    },
    {
        'icon': '🌏',
        'title': '商务部：原则同意将美农产品纳入对等降税；中欧贸易投资磋商机制正式成立',
        'content': '①商务部发言人何亚东7月2日表示，经近期经贸磋商，中美设定扩大农产品双向贸易指导性目标，原则同意将相关农产品纳入对等降税框架安排；②6月29日中欧贸易投资磋商机制首次会议在布鲁塞尔召开，确认正式成立机制，下设四大板块。中美、中欧经贸关系边际缓和信号。',
        'tag': '对外经贸',
        'importance': 'normal',
        'source': '商务部',
        'time': '7月2日'
    },
    {
        'icon': '📉',
        'title': '外盘警示：美股7月3日芯片股暴跌！费半跌5.44%、闪迪-14%、美光-5.5%',
        'content': '7月3日（周四，周五因独立日休市）美股芯片板块连续第二日大跌：费城半导体指数-5.44%，VanEck半导体ETF SMH-4.54%，闪迪-14%、科磊-11.5%、西部数据-10%、应用材料-7%、格芯-9.5%、ARM-6.6%、英特尔/美光-5%+、AMD-4%、英伟达-1.39%（抗跌）。道指受苹果+4.84%/防御股拉动创历史新高52900点，纳指-0.8%。美国6月非农仅增5.7万远低预期，但市场重新定价AI估值，半导体遭遇资金高低切。A股半导体/存储周一开盘需警惕情绪冲击。',
        'tag': '外盘警示',
        'importance': 'high',
        'source': '财联社/新浪财经',
        'time': '7月3日'
    },
    {
        'icon': '⚠️',
        'title': '持仓警示：国轩高科减持铜冠铜箔套现8.29亿元，仍持股1053万股',
        'content': '7月3日晚国轩高科公告，上半年全资子公司合肥国轩通过集中竞价出售铜冠铜箔（301217）839.95万股，成交金额8.29亿元（暴赚近20倍），截至公告日仍持有1053.16万股（持股约1%）。铜冠铜箔本周连续3日下跌累计跌幅6.28%，股东减持+板块回调双重承压。',
        'tag': '持仓相关',
        'importance': 'high',
        'source': '公司公告',
        'time': '7月3日'
    },
]
gen.add_weekend_highlights(highlights)

# ============ 2. 政策解读 ============
policies = [
    {
        'title': '🔥"十五五"碳达峰行动方案：从约束性目标升级为战略牵引',
        'content': '国常会6月29日审议通过，三大变化：①定位升级——从"紧箍咒"变"指挥棒"，双碳嵌入新质生产力培育；②能源结构——非化石能源发电量占比目标50%、消费占比25%，推动煤炭石油消费达峰；③考核硬约束——4月《碳达峰碳中和综合评价考核办法》已将双碳纳入省级党政考核，与干部任用挂钩。',
        'impact': '绿色电力、碳交易、环保、节能改造是长期主线，但短期更直接的是与AI算力相关的绿电+液冷温控——英维克作为液冷温控龙头直接受益于智算集群建设+绿色数据中心政策双轮驱动。',
        'sector': '绿色电力,液冷温控,环保,碳交易',
        'level': '国家级'
    },
    {
        'title': '🔥"人工智能+"行动升级：加力推进超大规模智算集群建设',
        'content': '国常会明确要求：①加力推进AI创新突破；②加快关键技术攻关；③加快超大规模智算集群建设；④深入实施"人工智能+"行动。配合之前八部门工业互联网意见（5万张工业5G专网）和大基金三期加码，算力基建获最强政策背书。',
        'impact': '算力基建（IDC、液冷、光模块、HBM存储）是核心受益方向。但注意美股芯片周四大跌+中报高位兑现风险，算力链短期高位震荡加大。雅克科技（半导体材料/前驱体/光刻胶）受益于晶圆厂扩产+大基金三期。',
        'sector': 'AI算力,液冷温控,半导体设备,光模块,HBM',
        'level': '国家级'
    },
    {
        'title': '循环经济"十五五"规划：2030年8万亿产值，"新三样"回收补短板',
        'content': '发改委7月4日印发，核心目标：主要资源产出率+16%、大宗固废45亿吨、再生资源5.1亿吨、产值8万亿（CAGR≈10%）。重点方向：①"新三样"（新能源汽车/动力电池/光伏）固废规范化回收；②大宗固废综合利用；③再生资源循环利用体系。规范化管理加速低效产能出清。',
        'impact': '动力电池回收龙头、再生资源企业、工业固废危废处理细分龙头受益。铜冠铜箔作为锂电铜箔龙头虽主营不是回收，但产业链循环规范化有助于龙头集中度提升。',
        'sector': '动力电池回收,固废处理,再生资源,铜箔',
        'level': '部委级'
    },
    {
        'title': '央行1万亿买断式逆回购：结束3月缩量周期，宽货币明确',
        'content': '7月6日（周一）央行操作1万亿3个月买断式逆回购（到期8000亿，净投放2000亿），今年3月以来首次净投放。背景：①DR001/DR007均升至1.4%政策利率附近；②7月共有1.7万亿买断式逆回购+4000亿MLF到期；③政府债券净融资约1.7万亿。叠加6月25日MLF加量2000亿，宽货币窗口正式打开。',
        'impact': '流动性宽松支撑权益市场估值，利率敏感型板块（成长科技、券商、地产）受益，高股息红利承压。为A股中报行情+7月解禁潮提供流动性缓冲。',
        'sector': '成长股,券商,高股息承压',
        'level': '货币政策'
    },
    {
        'title': '八部门工业互联网+人形机器人专项行动：万台级落地硬指标',
        'content': '①工信部等八部门：2030年建成5万张工业5G专网，核心产业增加值2.5万亿；②工信部+国资委《人形机器人与具身智能实景实训专项行动》：2026年底万台级规模化落地，央企/园区必须完成部署任务；③宇树科技科创板IPO注册获批（104天最快纪录）；④中国人形机器人百人会倡议防范伦理风险（"赛博伴侣"争议）。',
        'impact': '人形机器人板块全年主线地位确认。短期催化：宇树科技IPO+特斯拉Optimus V3 7-8月量产+减速器/伺服中报预增。但需注意：伦理倡议提示监管风险，板块前期已大涨需注意高低切。',
        'sector': '人形机器人,减速器,伺服电机,工业互联网',
        'level': '部委级'
    },
    {
        'title': '📅 周一落地！A股交易新规正式实施（5大变化）',
        'content': '7月6日起沪深北交易所新版交易规则正式实施：①盘后固定价格交易扩容至全部A股+沪深ETF（15:05-15:30）；②基金收盘改为集合竞价；③主板ST/*ST涨跌幅由5%放宽至10%（⚠️直接影响*ST建艺持仓）；④创业板引入做市商制度；⑤大宗交易机制优化（创业板盘中实时确认）。',
        'impact': '*ST建艺涨跌幅从5%扩至10%，波动幅度翻倍，需严格执行止损纪律。ST板块整体活跃度提升但波动加剧，注意规避纯炒作ST股。',
        'sector': 'ST板块,券商,市场生态',
        'level': '交易所'
    },
]
gen.add_policy_interpretation(policies, view_mode="tab")

# ============ 3. 下周题材预判 ============
topics = [
    {
        'name': 'S级：人形机器人（宇树IPO+特斯拉量产+政策落地三重催化）',
        'probability': '高确定性',
        'logic': '①宇树科技科创板IPO注册获批（104天最快），A股"具身智能第一股"催化估值锚重塑；②特斯拉Optimus V3 7-8月量产，网传7月订单已下供应商排产到8月；③工信部+国资委专项行动万台级硬指标+国网68亿集采；④优必选U1预售超13000台9月交付；⑤中报减速器/伺服企业预增50%-150%基本面验证。⚠️风险：伦理协会倡议提示监管边际、前期累计涨幅大需高低切。',
        'stocks': ['减速器', '绿的谐波', '双环传动', '中大力德', '伺服电机', '汇川技术', '鸣志电器', '传感器', '柯力传感', '弹性小票', '丰光精密', '贝斯特'],
        'category': '核心主线',
        'rating': '强烈推荐'
    },
    {
        'name': 'S级：存储芯片（业绩炸裂但波动剧烈，分歧中找机会）',
        'probability': '高确定性',
        'logic': '①江波龙中报预增622-744倍验证景气度，Q2环比继续增长38%-84%；②三星传Q3 DRAM再涨20%（年内累计涨幅或达340%），高盛称供需不平衡达15年高峰；③美光广岛HBM工厂7月4日动工（93亿美元），SK海力士514亿美元NAND新厂+HBM扩产；④大基金三期持续加码存储设备/材料。⚠️核心风险：美股芯片周四大跌（费半-5.44%、美光-5.5%、闪迪-14%），A股存储板块周四周五已剧烈分歧，龙头单日跌超10%，周一开盘承压。策略：不追高、等分歧低吸，聚焦上游设备/材料（雅克科技、安集科技）及HBM配套（香农芯创、澜起科技）。',
        'stocks': ['设备材料', '中微公司', '雅克科技', '安集科技', 'HBM配套', '澜起科技', '香农芯创', '模组龙头', '江波龙', '佰维存储'],
        'category': '核心主线',
        'rating': '推荐（分歧低吸）'
    },
    {
        'name': 'A级：AI算力/液冷温控（政策+业绩双驱动，但需规避高位）',
        'probability': '高确定性',
        'logic': '①国常会明确"超大规模智算集群建设"；②央行1万亿净投放呵护流动性；③中报业绩验证期，英维克等液冷龙头订单饱满。⚠️风险：美股科技股分化（英伟达仅-1.39%相对抗跌，但Meta-4.9%/特斯拉-7.5%），A股算力租赁高位股兑现压力大，需聚焦上游设备/液冷硬科技。英维克作为持仓直接受益。',
        'stocks': ['液冷', '英维克', '高澜股份', '申菱环境', '光模块', '中际旭创', '新易盛', 'IDC', '润泽科技', '科华数据'],
        'category': '核心主线',
        'rating': '推荐'
    },
    {
        'name': 'A级：半导体设备/材料（大基金三期+中报+海外扩产订单）',
        'probability': '高确定性',
        'logic': '①大基金三期持续增资设备/材料企业；②美光/SK海力士千亿级扩产拉动上游设备材料需求；③国产替代加速；④雅克科技（前驱体/光刻胶/SOD）直接受益于HBM扩产+先进封装。持仓雅克科技受益方向明确。',
        'stocks': ['雅克科技', '中微公司', '北方华创', '拓荆科技', '安集科技', '华海清科'],
        'category': '核心主线',
        'rating': '推荐'
    },
    {
        'name': 'B级：ST板块（涨跌幅放宽至10%，*ST建艺双刃剑）',
        'probability': '中确定性',
        'logic': '7月6日起主板ST/*ST涨跌幅限制由5%调整为10%。对*ST建艺持仓影响：①弹性翻倍（上涨空间打开）；②风险翻倍（止损纪律必须更严）；③ST板块整体活跃度提升，但纯炒作ST股波动加剧。*ST建艺需密切关注摘帽进展与基本面变化，严格执行止损。',
        'stocks': ['*ST建艺'],
        'category': '持仓相关',
        'rating': '关注'
    },
    {
        'name': 'B级：高股息/红利（宽货币下相对承压）',
        'probability': '中确定性',
        'logic': '央行重启净投放+资金利率下行，高股息红利策略相对吸引力下降，但防御属性仍在。铜冠铜箔虽属新能源材料不是纯红利，但机构持仓+融资余额创新高，需警惕国轩高科减持后的承接力。',
        'stocks': ['铜冠铜箔', '银行', '电力', '煤炭'],
        'category': '持仓相关',
        'rating': '谨慎'
    },
    {
        'name': '事件驱动：美联储6月FOMC会议纪要（7月9日周四凌晨）',
        'probability': '中确定性',
        'logic': '新主席沃什首次主持的会议纪要，6月点阵图半数委员预计年内加息。但6月非农仅增5.7万远低预期（创4月新低），市场加息预期降温（CME显示7月不加息概率68.5%）。若纪要偏鸽将利好全球风险资产，偏鹰则冲击港股/科技股。',
        'stocks': ['黄金', '成长股', '港股互联网'],
        'category': '事件驱动',
        'rating': '关注'
    },
    {
        'name': '事件驱动：6月CPI/PPI（7月9日周三9:30）',
        'probability': '高确定性',
        'logic': '浙商证券预计6月CPI同比+1.1%（环比-0.3%，食品价格季节性回落），PPI同比+4.1%（环比+0.1%，资源品传导+中游补涨）。K型分化延续：上游资源品价格上行vs下游需求偏弱。PPI回升利好周期/资源股，但挤压中下游利润。',
        'stocks': ['有色', '化工', '煤炭', '消费'],
        'category': '事件驱动',
        'rating': '关注'
    },
]
gen.add_next_week_topics(topics, view_mode="tab")

# ============ 4. 下周重大事件日历 ============
calendar_html = '''
<div style="display: grid; gap: 12px;">
'''
events = [
    ('7月6日 周一', '🚨重磅', [
        ('央行1万亿3M买断式逆回购', '宽货币落地'),
        ('A股交易新规正式实施', 'ST涨跌幅扩至10%/盘后固定价格扩容/创业板做市商'),
        ('SK海力士ADR簿记建档启动', '募资约290亿美元，7月10日上市'),
        ('SpaceX纳指100纳入生效', '7月6日收盘后被动基金买入'),
        ('央行10000亿买断式逆回购操作', '3个月期，净投放2000亿'),
        ('北交所新股：龙鑫智能申购', ''),
    ]),
    ('7月7日 周二', '📊数据', [
        ('6月外汇储备数据', '国家外汇管理局'),
        ('SpaceX正式纳入纳斯达克100', '预计43亿美元被动资金流入'),
        ('美对60国加征关税听证', '贸易摩擦新变量'),
    ]),
    ('7月8日 周三', '📈解禁', [
        ('屹唐股份解禁653亿', '占下周解禁65%，半导体设备龙头'),
        ('智谱/MiniMax港股解禁', '合计850亿港元，AI独角兽流动性考验'),
        ('亨通光电股权激励解禁', '519名激励对象收益近11倍'),
    ]),
    ('7月9日 周四', '🔥关键日', [
        ('中国6月CPI/PPI发布', '9:30，CPI预计+1.1%/PPI预计+4.1%'),
        ('美联储6月FOMC会议纪要', '凌晨2:00，沃什首秀，鹰鸽关键'),
        ('SK海力士ADR确定发行价', ''),
        ('美股二季报开启', '达美航空盘前'),
        ('A股中报预告密集披露', '7月15日前强制披露截止'),
    ]),
    ('7月10日 周五', '💼事件', [
        ('SK海力士ADR纳斯达克上市', '创纪录规模'),
        ('天承科技解禁126亿', '解禁比例61.98%'),
        ('美伊新一轮会谈', '巴基斯坦举行，影响原油/黄金'),
        ('科创板新股：泰诺麦博申购', ''),
        ('百事公司财报', '美股二季报'),
    ]),
]

for date, level, items in events:
    color = {'🚨重磅':'linear-gradient(135deg,#ef4444,#dc2626)', '📊数据':'linear-gradient(135deg,#3b82f6,#2563eb)',
             '📈解禁':'linear-gradient(135deg,#f59e0b,#d97706)', '🔥关键日':'linear-gradient(135deg,#8b5cf6,#7c3aed)',
             '💼事件':'linear-gradient(135deg,#10b981,#059669)'}[level]
    calendar_html += f'''
    <div style="background: rgba(255,255,255,0.05); border-radius: 14px; padding: 16px; border: 1px solid rgba(255,255,255,0.1);">
        <div style="display:flex;align-items:center;gap:10px;margin-bottom:12px;">
            <span style="background:{color};color:white;padding:4px 10px;border-radius:8px;font-size:12px;font-weight:700;">{date}</span>
            <span style="color:rgba(255,255,255,0.7);font-size:13px;">{level}</span>
        </div>
        <div style="display:flex;flex-direction:column;gap:8px;">
    '''
    for name, note in items:
        note_html = f' <span style="color:rgba(255,255,255,0.5);font-size:11px;">· {note}</span>' if note else ''
        calendar_html += f'''
            <div style="display:flex;align-items:baseline;gap:8px;">
                <span style="width:6px;height:6px;background:rgba(255,255,255,0.4);border-radius:50%;flex-shrink:0;margin-top:7px;"></span>
                <span style="color:rgba(255,255,255,0.9);font-size:13px;line-height:1.6;">{name}{note_html}</span>
            </div>
        '''
    calendar_html += '</div></div>'

calendar_html += '</div>'

from components.layout import Section
calendar_section = Section(title="📅 下周重大事件日历", content=calendar_html, icon="calendar")
gen._components.append(calendar_section)

# ============ 5. 持仓诊断 ============
portfolio_html = '''
<div style="background: linear-gradient(135deg, rgba(251,191,36,0.15) 0%, rgba(245,158,11,0.1) 100%); 
            border: 1px solid rgba(251,191,36,0.3); border-radius: 16px; padding: 18px; margin-bottom: 14px;">
    <div style="color: #fbbf24; font-weight: 700; font-size: 15px; margin-bottom: 12px;">
        ⚠️ 持仓核心关注：ST涨跌幅放宽+国轩减持铜箔+美股芯片暴跌传导
    </div>
    <div style="color: rgba(255,255,255,0.85); font-size: 13px; line-height: 1.8;">
        下周一<kbd style="background:rgba(251,191,36,0.2);padding:2px 6px;border-radius:4px;font-size:12px;color:#fbbf24;">交易新规</kbd>
        正式实施，<b style="color:#fbbf24;">*ST建艺涨跌幅从5%→10%</b>，波动翻倍，务必严格止损纪律。
        铜冠铜箔遭<b>国轩高科减持8.29亿元</b>（仍持1053万股），叠加美股芯片暴跌传导，周一开盘承压。
    </div>
</div>

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 14px;">
'''

portfolio_stocks = [
    {
        'name': '英维克 (002837)',
        'tag': '液冷温控',
        'tag_color': 'linear-gradient(135deg,#3b82f6,#2563eb)',
        'rating': '🔥 核心持有',
        'rating_color': '#10b981',
        'catalysts': ['国常会"超大规模智算集群建设"直接利好', '液冷+绿色数据中心双轮驱动', '中报订单饱满预期'],
        'risks': ['算力高位股分歧可能波及', '短期累计涨幅较大注意节奏'],
        'action': '中线持有，回调加仓，止损参考20日均线'
    },
    {
        'name': '雅克科技 (002409)',
        'tag': '半导体材料',
        'tag_color': 'linear-gradient(135deg,#8b5cf6,#7c3aed)',
        'rating': '🔥 核心持有',
        'rating_color': '#10b981',
        'catalysts': ['大基金三期持续加码设备材料', '美光/SK海力士HBM扩产拉动前驱体需求', '先进封装+光刻胶国产替代'],
        'risks': ['美股半导体周四暴跌传导', '板块高位震荡加剧'],
        'action': '持有，若低开至支撑位可分批加仓'
    },
    {
        'name': '铜冠铜箔 (301217)',
        'tag': '锂电铜箔',
        'tag_color': 'linear-gradient(135deg,#f59e0b,#d97706)',
        'rating': '⚠️ 减持承压',
        'rating_color': '#f59e0b',
        'catalysts': ['循环经济规划利好产业链集中度提升', '易方达祁禾两只基金新进'],
        'risks': ['国轩高科减持8.29亿+仍持1053万股待减', '本周已连跌3日累计-6.28%', '融资余额处于90%分位高位', '新能源板块整体偏弱'],
        'action': '⚠️ 周一若低开破位严格止损，反弹减仓为主，不宜加仓'
    },
    {
        'name': '*ST建艺',
        'tag': 'ST摘帽预期',
        'tag_color': 'linear-gradient(135deg,#ef4444,#dc2626)',
        'rating': '🚨 波动翻倍',
        'rating_color': '#ef4444',
        'catalysts': ['周一ST涨跌幅扩至10%，弹性翻倍', 'ST板块整体活跃度提升', '摘帽预期仍在'],
        'risks': ['涨跌幅从5%变10%，风险同时翻倍', 'ST新规后博弈更激烈', '基本面无实质变化则纯炒作'],
        'action': '严格设置止损线（-8%止损），不追高，若摘帽消息落地逢高兑现'
    },
]

for s in portfolio_stocks:
    cat_html = ''.join([f'<div style="padding:3px 8px;background:rgba(16,185,129,0.15);border-radius:6px;font-size:11px;color:#10b981;margin:2px;">✓ {c}</div>' for c in s['catalysts']])
    risk_html = ''.join([f'<div style="padding:3px 8px;background:rgba(239,68,68,0.15);border-radius:6px;font-size:11px;color:#f87171;margin:2px;">✗ {r}</div>' for r in s['risks']])
    portfolio_html += f'''
    <div style="background: rgba(255,255,255,0.06); border-radius: 14px; padding: 16px; border: 1px solid rgba(255,255,255,0.12);">
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:10px;">
            <div style="font-weight:700;color:white;font-size:15px;">{s['name']}</div>
            <span style="background:{s['tag_color']};color:white;padding:2px 8px;border-radius:6px;font-size:11px;font-weight:600;">{s['tag']}</span>
        </div>
        <div style="margin-bottom:10px;">
            <span style="color:{s['rating_color']};font-weight:700;font-size:13px;">{s['rating']}</span>
        </div>
        <div style="margin-bottom:8px;">
            <div style="color:rgba(255,255,255,0.6);font-size:11px;margin-bottom:4px;">催化因素</div>
            <div style="display:flex;flex-wrap:wrap;gap:4px;">{cat_html}</div>
        </div>
        <div style="margin-bottom:10px;">
            <div style="color:rgba(255,255,255,0.6);font-size:11px;margin-bottom:4px;">风险提示</div>
            <div style="display:flex;flex-wrap:wrap;gap:4px;">{risk_html}</div>
        </div>
        <div style="padding:8px 10px;background:rgba(255,255,255,0.08);border-radius:8px;border-left:3px solid {s['rating_color']};">
            <span style="color:rgba(255,255,255,0.9);font-size:12px;font-weight:500;">📌 操作：{s['action']}</span>
        </div>
    </div>
    '''

portfolio_html += '</div>'
portfolio_section = Section(title="💼 持仓诊断（4只）", content=portfolio_html, icon="briefcase")
gen._components.append(portfolio_section)

# ============ 6. 下周操作计划 ============
plan = '''
<div style="background: linear-gradient(135deg, rgba(99,102,241,0.15) 0%, rgba(139,92,246,0.1) 100%); 
            border: 1px solid rgba(99,102,241,0.3); border-radius: 16px; padding: 20px; line-height: 1.9;">
    
    <div style="margin-bottom: 16px;">
        <div style="color:#a5b4fc;font-weight:700;font-size:15px;margin-bottom:8px;">📊 当前市场定调</div>
        <div style="color:rgba(255,255,255,0.85);font-size:13px;">
            风险指数 <b style="color:#f59e0b;">60 橙色中高风险</b> | 建议仓位 <b style="color:#fbbf24;">3-4成</b> |
            主线：人形机器人S+ / AI算力液冷S / 存储A级（分歧加剧）/ 半导体设备材料S级
        </div>
    </div>

    <div style="margin-bottom: 16px;">
        <div style="color:#86efac;font-weight:700;font-size:15px;margin-bottom:8px;">🎯 周一开盘策略（7月6日）</div>
        <div style="color:rgba(255,255,255,0.85);font-size:13px;">
            <b style="color:#10b981;">核心原则：不追高，等分歧，控仓位</b><br>
            ① <b>开盘警惕</b>：美股芯片周四大跌（费半-5.44%、美光-5.5%），A股存储/半导体低开压力大，<b>不要恐慌割肉也不要盲目抄底</b>，观察前30分钟量能再决策；<br>
            ② <b>流动性利好</b>：央行1万亿净投放落地+ST新规，券商/成长/机器人可能有结构性机会；<br>
            ③ <b>持仓动作</b>：英维克/雅克科技中线持有，观察盘中承接；铜冠铜箔重点警惕减持压力，破位即止损；*ST建艺盯紧新涨跌幅下的波动，严格止损。
        </div>
    </div>

    <div style="margin-bottom: 16px;">
        <div style="color:#fbbf24;font-weight:700;font-size:15px;margin-bottom:8px;">⚡ 本周重点节奏</div>
        <div style="color:rgba(255,255,255,0.85);font-size:13px;">
            ① <b>周一</b>：消化外盘跌幅+央行净投放落地+新规实施，波动加大，观察机器人/液冷强度；<br>
            ② <b>周二-周三</b>：中报预告密集期，存储/机器人高弹性个股业绩兑现或证伪；屹唐股份653亿解禁注意半导体设备板块情绪；<br>
            ③ <b>周四</b>：<b style="color:#ef4444;">关键日</b>——CPI/PPI+美联储FOMC纪要双事件，决定大盘方向，纪要公布前控制仓位；<br>
            ④ <b>周五</b>：SK海力士美股上市定价+HBM映射+美伊会谈，警惕周末前避险。
        </div>
    </div>

    <div style="margin-bottom: 16px;">
        <div style="color:#fca5a5;font-weight:700;font-size:15px;margin-bottom:8px;">🛡️ 风控铁律（严格执行）</div>
        <div style="color:rgba(255,255,255,0.85);font-size:13px;">
            ① 单票止损<b style="color:#ef4444;">-8%</b>无条件执行，*ST建艺新规则下波动翻倍，更要严守；<br>
            ② 总仓位控制在<b style="color:#fbbf24;">3-4成</b>，美联储纪要前不加仓；<br>
            ③ 存储板块高位分歧严重，<b style="color:#ef4444;">年内翻倍标的高开超4%绝不追高</b>；<br>
            ④ 主线（机器人/算力/半导体）聚焦核心龙头，远离边缘蹭概念小票。
        </div>
    </div>

    <div>
        <div style="color:#93c5fd;font-weight:700;font-size:15px;margin-bottom:8px;">💡 关键机会排序</div>
        <div style="color:rgba(255,255,255,0.85);font-size:13px;">
            <b>S级</b>：人形机器人（宇树IPO催化+特斯拉量产+政策）<br>
            <b>A级</b>：AI算力液冷（英维克持仓受益）/ 半导体设备材料（雅克科技持仓受益）<br>
            <b>B级</b>：存储芯片（业绩验证但波动巨大，分歧低吸不追高）<br>
            <b>回避</b>：高位算力租赁/纯炒作ST/涨幅翻倍的边缘存储概念股
        </div>
    </div>
</div>
'''
gen.add_trading_plan(plan)

# ============ 7. 风险提示 ============
gen.add_risk_warning([
    "美股芯片股周四暴跌（费半-5.44%）可能引发A股半导体/存储周一低开传导",
    "美联储6月FOMC纪要（7月9日）可能释放鹰派信号，全球风险资产承压",
    "下周解禁市值超1000亿（屹唐股份653亿）+智谱/MiniMax港股850亿解禁冲击流动性",
    "*ST建艺涨跌幅扩至10%，波动翻倍，必须严格止损纪律",
    "铜冠铜箔遭国轩高科减持8.29亿+仍有1053万股待减，抛压持续",
    "存储板块高位剧烈分歧，单日跌超10%的龙头股不排除继续回调",
    "中报预告7月15日强制截止期，业绩不及预期个股可能暴雷",
    "地缘风险：美伊会谈7月11日、北约峰会7月7-9日，原油/黄金异动风险",
])

# ============ 发布 ============
print("开始生成并发布...")
result = gen.publish(
    filename="20260705_周末速递.html",
    excerpt="十五五碳达峰+AI+双国常会重磅部署｜央行1万亿重启净投放｜宇树IPO催化机器人主线｜美股芯片暴跌预警｜周一ST涨跌幅扩至10%｜江波龙中报预增622倍"
)
print("\n发布结果:", result)
