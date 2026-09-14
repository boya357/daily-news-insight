#!/usr/bin/env python3
"""2026-09-14 每日新闻洞察 - V3 Pro生成器"""
import sys, os
sys.path.insert(0, 'v3')
os.chdir('/root/daily-news-insight')
from generators.daily_pro import DailyReportProGenerator

gen = DailyReportProGenerator(
    date_str="2026-09-14",
    weekday="周一",
    subtitle="沙特管道被炸原油跳涨3% | 算力网顶层定调国常会加码 | 十五五金融强国规划落地",
    data_dir='/root/daily-news-insight/data'
)

# TL;DR
gen.set_tldr([
    ("原油跳涨3% 中东局势再升级", "沙特东西管道遭袭停运（占全球供应4%），布伦特原油跳涨至108美元，霍尔木兹海峡会议突然延期，特朗普称中期选举后结束战事", "red"),
    ("十五五金融强国规划落地", "央行证监会四部门联合发布，打造A股为境内优质企业上市首选地，社保/年金/保险今年净买入A股超6000亿元，3000亿特别国债补充金融资本", "green"),
    ("算力网顶层定调 国常会加码", "国务院常务会议专题研究算力网建设，构建多层次网络化算力体系，推动算电协同与绿电直连，雄安算力中心启动2.7万P", "green"),
    ("存储超级周期延续 HBM缺口扩大", "三星/SK海力士成品库存不足10天，HBM现货价为长协价4-5倍，国产AI芯片因HBM缺货涨价20-50%，华为昇腾950DT报价超25万", "green"),
    ("A股上周五普跌4800+只", "沪指跌1.18%失守3900点，成交1.97万亿，MLCC/光通信/CPO逆势领涨，本周关注8月金融数据、经济数据、LPR报价及美联储加息", "orange"),
])

# === 1. 隔夜全球市场 ===
gen.add_global_market()

# === 2. 市场总览 ===
gen.add_market_overview()

# === 3. 重大新闻 - tab切换 ===
news_tabs = [
    {
        "label": "海外市场",
        "content": gen.create_card_group([
            {
                "title": "🛢️ 沙特东西管道遭袭停运 原油跳涨3% 布伦特破108美元",
                "content": """中东局势周末急剧升级，沙特阿拉伯东西向输油管道遭无人机袭击停运，全球石油供应面临4%缺口风险：
<br>
<ul style="margin:8px 0;padding-left:20px;">
<li>布伦特原油跳涨<strong style="color:#ef4444;">3.47%</strong>至108.24美元，WTI涨<strong style="color:#ef4444;">3.26%</strong>至103.32美元</li>
<li>沙特东西管道日输油约400-500万桶，占全球供应约4%，是绕开霍尔木兹海峡的关键替代通道</li>
<li>沙特红海延布港库存仅能维持5-7天出口，若管道不尽快重启库存将很快耗尽</li>
<li>霍尔木兹海峡会议突然延期，伊朗与海湾国家对话进程再遭挫折</li>
<li>国际能源署(IEA)：沙特8月石油供应降至30多年来低点</li>
</ul>
<strong>对A股映射：</strong>油气开采、油服、煤炭等能源板块有望获得催化，同时加剧通胀预期
<br><br>
<em style="opacity:0.6">来源：路透社、央视新闻、IEA</em>""",
            },
            {
                "title": "🇺🇸 特朗普称美伊战事中期选举后结束 油价将快速下跌",
                "content": """美国总统特朗普9月13日在爱尔兰访问期间重申，美伊战事预计将在11月美国国会中期选举后立即结束：
<br>
<ul style="margin:8px 0;padding-left:20px;">
<li>特朗普："伊朗非常想达成协议"，强调必须谈成"合适的协议"</li>
<li>称战事一旦结束，"汽油价格将会快速下跌"</li>
<li>这是特朗普近期第二次将战事结束时间明确指向中期选举</li>
<li>伊朗方面：重开霍尔木兹海峡的前提是美国重新履行"伊斯兰堡谅解备忘录"承诺</li>
<li>阿曼宣布原定于9月14日的地区会议推迟，具体日期未公布</li>
</ul>
<strong>市场含义：</strong>特朗普的表态给市场提供了一个时间锚点——中期选举（11月）前油价可能维持高位，之后存在快速回落的政治驱动预期
<br><br>
<em style="opacity:0.6">来源：路透社、美联社、中新网</em>""",
            },
            {
                "title": "💾 美光9月30日财测成关键 分析师目标价1500美元",
                "content": """美光科技将于9月30日发布2026财年第四季度财报（截至8月31日），HBM超级周期下业绩或再创新高：
<br>
<ul style="margin:8px 0;padding-left:20px;">
<li>管理层指引：Q4营收同比+341%至约500亿美元，EPS同比+985%至30.73美元</li>
<li>华尔街预期：2027财年Q1销售额566亿美元，全年EPS 155美元</li>
<li>当前股价975.26美元，较6月历史高点折价约19%</li>
<li>38位分析师平均目标价1295.63美元，最高看至2000美元</li>
<li>动态PE仅22.1倍，低于标普500和纳指100，价值洼地凸显</li>
<li>风险点：60%企业转向更便宜AI模型降本，AI资本开支可持续性存疑</li>
</ul>
<strong>对A股映射：</strong>存储产业链（HBM、DDR、封测）受益于超级周期延续
<br><br>
<em style="opacity:0.6">来源：MarketBeat、Nasdaq、The Motley Fool</em>""",
            },
            {
                "title": "💻 戴尔暴涨近12%创历史新高 市值一夜增2500亿",
                "content": """戴尔科技股价飙涨11.9%报567.14美元，创历史新高，市值一夜暴增约385亿美元（约2582亿人民币）：
<br>
<ul style="margin:8px 0;padding-left:20px;">
<li>AI服务器需求持续爆发，戴尔作为GPU服务器龙头直接受益</li>
<li>英伟达Vera Rubin新一代GPU系统出货在即，戴尔为核心组装合作伙伴</li>
<li>AI基础设施资本开支浪潮下，服务器厂商订单能见度高</li>
<li>英特尔+2.61%、高通+2.88%、AMD+2.49%，芯片板块普涨</li>
<li>费城半导体指数涨1.81%，报11824点</li>
</ul>
<strong>产业链含义：</strong>AI算力硬件从芯片向整机/服务器环节扩散，服务器ODM、液冷、PCB等配套环节受益
<br><br>
<em style="opacity:0.6">来源：36氪、彭博社</em>""",
            },
        ]),
    },
    {
        "label": "国内政策",
        "content": gen.create_card_group([
            {
                "title": "🏛️ 十五五金融强国规划落地 打造A股为上市首选地",
                "content": """9月10日国新办发布会，央行、证监会等四部门联合发布《金融强国建设"十五五"规划》完整施工图：
<br>
<ul style="margin:8px 0;padding-left:20px;">
<li>首次提出将<strong>A股打造为境内优质企业上市首选地</strong>，配套9份专项行动方案</li>
<li>健全"长钱长投"机制，今年社保/年金/保险等中长期资金合计净买入A股超6000亿元</li>
<li>持有流通市值较2025年底增长12.5%，中长期资金"压舱石"作用增强</li>
<li>IPO平均审核周期缩短至6个月左右，优质公司再融资审核不到一个月</li>
<li>科创板上半年营收增速近40%、净利润增长4.4倍，硬科技上市通道实质性跑通</li>
<li>财政部拟发行3000亿元特别国债，支持8家中央金融企业补充核心一级资本</li>
</ul>
<strong>市场含义：</strong>以改革的确定性对冲外部环境的不确定性，制度红利加速释放，利好券商与优质科技成长资产
<br><br>
<em style="opacity:0.6">来源：证监会、国新办发布会、华夏时报</em>""",
            },
            {
                "title": "⚡ 国常会专题部署算力网建设 算电协同+绿电直连",
                "content": """9月11日国务院常务会议专题研究"算力网"建设，明确算力网是人工智能发展的基础支撑：
<br>
<ul style="margin:8px 0;padding-left:20px;">
<li>构建<strong>多层次网络化算力体系</strong>，推动算电协同、算网融合</li>
<li>加强骨干光纤网络建设，加快绿电直连、源网荷储项目落地</li>
<li>雄安国际算力一体化调度中心启动，总算力超2.7万P</li>
<li>中国算力大会发布15项重大突破成果，长飞空芯光纤创0.04dB/km世界纪录</li>
<li>Token数据大爆发，机构预测2026年国内Token年消耗量达10亿亿级别，CAGR近12倍</li>
<li>高盛将2026-2028年全球光模块出货量预测整体上调20%以上</li>
</ul>
<strong>对A股映射：</strong>算力基础设施（光通信/光纤/液冷/PCB）、AI算力芯片、绿电等方向获政策+产业双催化
<br><br>
<em style="opacity:0.6">来源：国务院、央视财经、科创板日报</em>""",
            },
            {
                "title": "💰 央行提前化解季末钱紧 连续4天逆回购最高2.4万亿",
                "content": """央行精准操作化解季末流动性紧张预期，为市场提供稳定资金面保障：
<br>
<ul style="margin:8px 0;padding-left:20px;">
<li>9月14日至17日连续4天开展隔夜逆回购，每日操作量不超过6000亿元</li>
<li>最高提供<strong>2.4万亿元</strong>短端流动性兜底，基本消除季末资金面不确定性</li>
<li>8月末外汇储备34383亿美元，环比+195亿</li>
<li>央行连续第22个月增持黄金，达7673万盎司</li>
<li>8月CPI同比+0.8%（环比+0.4%），PPI同比+3.8%，双双回升</li>
<li>发改委对成品油实施临时调控，应上调435元/吨，调控后实际上调260元/吨</li>
</ul>
<strong>本周关注：</strong>8月金融数据（14日）、8月经济数据（15日）、9月LPR报价（15日）
<br><br>
<em style="opacity:0.6">来源：央行、国家统计局、发改委</em>""",
            },
            {
                "title": "🚗 工信部九部门印发智能网联新能源汽车十五五规划",
                "content": """新能源汽车产业规划落地，叠加AI+软件专项行动，汽车智能化加速推进：
<br>
<ul style="margin:8px 0;padding-left:20px;">
<li>2030年新能源乘用车/商用车新车销量占比分别达<strong>70%、40%</strong></li>
<li>高速公路等场景实现高度自动驾驶</li>
<li>配套《"人工智能+软件"专项行动实施方案》</li>
<li>到2028年覆盖2万家规上软件企业、打造100个智能体软件标杆应用</li>
<li>宁德时代完成200-400亿注销式回购首笔操作，首次回购60.43万股约2亿元</li>
</ul>
<strong>产业含义：</strong>新能源汽车渗透率持续提升，智能化、智驾产业链进入加速期
<br><br>
<em style="opacity:0.6">来源：工信部、央视新闻</em>""",
            },
        ]),
    },
    {
        "label": "产业动态",
        "content": gen.create_card_group([
            {
                "title": "🧠 HBM缺货潮传导 国产AI芯片涨价20%-50%",
                "content": """HBM供应紧张从存储原厂传导至AI芯片端，国产算力芯片厂商大幅上调报价：
<br>
<ul style="margin:8px 0;padding-left:20px;">
<li>华为昇腾950DT加速卡意向报价升至<strong>25万元</strong>以上，较两个月前涨20%-50%</li>
<li>昇腾950PR从年初约6万升至8万以上，910C从约9万升至11万以上</li>
<li>寒武纪下一代"690"芯片报价上调约20%-30%，沐曦、天数智芯同步调价</li>
<li>三星/SK海力士成品库存低于<strong>10天</strong>，为存储行业从未达到的紧张水平</li>
<li>HBM3E现货价约2100美元，是长协价的4-5倍；HBM4现货价高达3500美元</li>
<li>SemiAnalysis预测：2026年DRAM供需缺口7%，HBM缺口6%；2027年缺口扩大至9%</li>
</ul>
<strong>完整传导链：</strong>HBM缺货涨价→AI芯片成本上升（HBM占BOM 30-50%）→国产芯片提价→云厂商算力涨价→Token调用价格上行
<br><br>
<em style="opacity:0.6">来源：路透社、彭博社、36氪、KB证券</em>""",
            },
            {
                "title": "📈 长鑫存储利润率反超三星SK海力士 达82%居全球第一",
                "content": """全球存储芯片行业格局生变，中国厂商盈利水平首次登顶：
<br>
<ul style="margin:8px 0;padding-left:20px;">
<li>2026年Q2长鑫存储息税前利润率达<strong>82%</strong>，一举超过SK海力士（76%）和三星半导体（70%）</li>
<li>成为当期全球盈利水平最高的存储芯片厂商</li>
<li>三大内存厂年度合并营业利润：2025年785亿美元→2026年795万亿韩元→2027年1284万亿韩元</li>
<li>三星已将70%存储产能通过LTA锁定到2031年，客户包括英伟达、微软、谷歌</li>
<li>分析师警告：三大原厂过度依赖长期合同，若AI资本开支放缓存在重新谈判风险</li>
<li>DeepSeek将KV-Cache HBM需求降低75%，SSD需求降低87.5%，算法优化可能影响长期需求</li>
</ul>
<strong>对A股映射：</strong>国产存储产业链（长鑫产业链、设备、材料）有望获得价值重估
<br><br>
<em style="opacity:0.6">来源：QUICK FactSet、36氪、智通财经</em>""",
            },
            {
                "title": "☀️ 阳光电源宣布涨价 光储产品上调5%-15%",
                "content": """AI算力+新能源双重景气，光伏逆变器和储能迎来量价齐升：
<br>
<ul style="margin:8px 0;padding-left:20px;">
<li>阳光电源9月11日发调价函，9月20日起光储产品价格上调<strong>5%-15%</strong></li>
<li>包括光伏逆变器、储能变流器及储能系统全系列</li>
<li>三安光电同步上调LED、射频、光芯片全系列价格</li>
<li>算力需求爆发驱动数据中心电力基础设施投资，储能+绿电需求共振</li>
<li>国常会强调算电协同、绿电直连，政策层面持续加码</li>
</ul>
<strong>产业含义：</strong>从存储到光储，硬件涨价潮从半导体向新能源领域扩散，有定价权的龙头企业受益
<br><br>
<em style="opacity:0.6">来源：财联社、阳光电源公告</em>""",
            },
            {
                "title": "🔧 MLCC/元件涨价链持续活跃 本周领涨概念",
                "content": """AI服务器上游电子元件进入涨价周期，MLCC成为上周最强概念板块：
<br>
<ul style="margin:8px 0;padding-left:20px;">
<li>上周MLCC概念涨幅居首，铜缆高速连接、CPO、PCB、光通信全线领涨</li>
<li>AI服务器MLCC用量是消费电子的5-10倍，高端MLCC供不应求</li>
<li>村田、三星电机等日系韩系厂商持续上调报价，国产替代加速</li>
<li>元件涨价链（MLCC、覆铜板、PCB）具备涨价能力+扩量逻辑双轮驱动</li>
<li>有研硅收购山东有研艾斯71.89%股权，9月14日复牌，半导体材料整合加速</li>
</ul>
<strong>操作建议：</strong>元件涨价链是AI硬件上游最确定的细分方向之一，回调即是布局机会
<br><br>
<em style="opacity:0.6">来源：财联社、科创板日报</em>""",
            },
        ]),
    },
    {
        "label": "持仓相关",
        "content": gen.create_card_group([
            {
                "title": "🔄 英维克：液冷长期逻辑未变 短期估值修复中",
                "content": """英维克当前价60.55元，深度调整后估值逐步回归合理区间：
<br>
<ul style="margin:8px 0;padding-left:20px;">
<li>最新收盘价<strong>60.55元</strong>，较年内高点回撤约40%+</li>
<li>国常会算力网建设部署，算电协同+绿电直连，液冷作为算力基础设施核心环节长期受益</li>
<li>液冷从"可选"变"必选"趋势明确，AI芯片功率密度持续提升驱动液冷渗透率提升</li>
<li>短期需关注：50元整数关口支撑力度，以及量能能否有效放大确认企稳</li>
<li>产业面：谷歌CDU订单持续交付，海外AI数据中心液冷需求爆发</li>
</ul>
<strong>操作建议：</strong>已深度破位，反弹至关键压力位减仓为主，等待右侧企稳信号再加仓
<br><br>
<em style="opacity:0.6">来源：公司公告、财联社、新浪财经</em>""",
            },
            {
                "title": "📈 铜冠铜箔：PCB+铜箔涨价链双受益",
                "content": """铜冠铜箔受益于AI服务器PCB需求爆发和铜箔涨价双重催化：
<br>
<ul style="margin:8px 0;padding-left:20px;">
<li>AI服务器用PCB需求量是普通服务器的3-5倍，高端铜箔供不应求</li>
<li>上周PCB概念、复合铜箔概念均进入涨幅前十，产业链景气度持续验证</li>
<li>铜箔加工费进入上升周期，下游需求旺盛+供给相对刚性</li>
<li>存储封测产能扩张也带动高端铜箔需求增长</li>
<li>关注半年报业绩兑现情况，验证盈利改善的持续性</li>
</ul>
<strong>操作建议：</strong>AI硬件上游确定性方向，回调可分批低吸，关注量能配合
<br><br>
<em style="opacity:0.6">来源：财联社、公司公告</em>""",
            },
            {
                "title": "🧪 雅克科技：HBM材料+存储产业链核心标的",
                "content": """雅克科技作为HBM材料核心供应商，受益于存储超级周期：
<br>
<ul style="margin:8px 0;padding-left:20px;">
<li>HBM缺货潮持续，三大原厂加速扩产，前驱体等关键材料需求增长确定</li>
<li>存储超级周期下，三星、SK海力士、美光资本开支持续加码</li>
<li>HBM3E→HBM4升级换代，对材料性能要求提升，单价同步提高</li>
<li>国产替代逻辑：半导体材料国产化率持续提升空间大</li>
<li>短期关注前期低点支撑，以及存储板块情绪修复节奏</li>
</ul>
<strong>操作建议：</strong>存储材料赛道长逻辑稳固，等待企稳信号，分批布局核心标的
<br><br>
<em style="opacity:0.6">来源：公司公告、行业研报</em>""",
            },
            {
                "title": "🏗️ *ST建艺：防御性配置 油价上涨催化基建链",
                "content": """*ST建艺作为组合防御端，油价上涨背景下基建链条有望获得关注：
<br>
<ul style="margin:8px 0;padding-left:20px;">
<li>原油价格维持高位，石油石化板块景气度高，带动基建/工程建设需求</li>
<li>ST板块整体情绪修复，摘帽预期仍在</li>
<li>组合对冲作用：科技股调整时防御性标的表现相对稳定</li>
<li>关注后续重整/摘帽进展公告</li>
</ul>
<strong>操作建议：</strong>维持底仓配置，作为组合缓冲器，关注事件性催化
<br><br>
<em style="opacity:0.6">来源：公司公告、Wind</em>""",
            },
        ]),
    },
]

news_tab_html = gen.create_tab_pane(news_tabs, tab_id="important-news", style="default")
gen.add_section("重大事件", news_tab_html, "📰")

# === 4. 板块观察 ===
gen.add_sector_analysis()

# === 5. 今日催化 ===
catalyst_content = gen.create_card_group([
    {
        "title": "🛢️ 原油跳涨能源链催化",
        "content": "沙特管道遭袭布伦特破108美元，全球供应损失4%，油气开采/油服/煤炭全线受益",
        "icon": "🟢",
    },
    {
        "title": "⚡ 算力网政策加码",
        "content": "国常会顶层定调算力网建设，算电协同+绿电直连+骨干光纤，光通信/液冷/PCB全链受益",
        "icon": "🟢",
    },
    {
        "title": "💾 HBM缺货国产芯片涨价",
        "content": "HBM库存不足10天，现货价为长协价4-5倍，华为昇腾950DT报价超25万，国产替代加速",
        "icon": "🟢",
    },
    {
        "title": "🏦 十五五金融强国规划",
        "content": "打造A股上市首选地，长钱入市6000亿+，3000亿特别国债补充金融资本，券商/银行受益",
        "icon": "🟢",
    },
    {
        "title": "📊 8月金融数据今日公布",
        "content": "9月14日央行公布8月新增人民币贷款/社融/M2数据，观察宽信用进展与经济复苏力度",
        "icon": "🟠",
    },
    {
        "title": "📈 MLCC/元件涨价链",
        "content": "AI服务器MLCC用量5-10倍于消费电子，高端MLCC供不应求，日系厂商持续提价",
        "icon": "🟢",
    },
], cols=3)

gen.add_section("今日催化", catalyst_content, "⚡")

# === 6. 话题动态 ===
gen.add_topic_dynamics()

# === 7. 深度话题 ===
gen.add_topic_deep_dive()

# === 8. 韭研公社热点 ===
gen.add_jiuyan_hot_topics()

# === 9. 持仓跟踪 ===
gen.add_holdings_tracking()

# === 10. 明日预判 ===
gen.add_tomorrow_prediction()

# === 11. 风险预警 ===
gen.add_risk_warning()

# === 12. 空方视角 ===
bear_content = gen.create_card_group([
    {
        "title": "原油破108美元 通胀压力急剧升温",
        "content": "沙特管道停运+霍尔木兹海峡局势紧张，布伦特原油突破108美元，全球通胀预期急剧升温。美国8月核心CPI环比+0.3%超预期，美联储9月加息概率升至90%，国内PPI可能加速至4%以上，货币政策空间进一步受限。",
        "tag": "通胀风险",
        "tag_color": "red",
    },
    {
        "title": "上周五普跌4800+只 情绪极度低迷",
        "content": "9月11日A股4870只个股下跌，仅643只上涨，跌停21家，炸板率38%，市场情绪极度低迷。成交1.97万亿虽维持高位但以恐慌性抛盘为主，短期市场信心恢复需要时间和量能配合。",
        "tag": "情绪风险",
        "tag_color": "red",
    },
    {
        "title": "本周解禁压力大 铜陵有色超139亿",
        "content": "9月14日为解禁高峰日：铜陵有色解禁21.4亿股（占总股本15.96%、市值超139亿）、中瓷电子解禁1.1亿股（占24.59%、市值超133亿），叠加盛科通信、杰理科技等，短期抛压需消化。",
        "tag": "供给风险",
        "tag_color": "orange",
    },
    {
        "title": "AI资本开支可持续性存疑",
        "content": "60%企业转向更便宜AI模型降本，Uber等巨头AI预算提前耗尽，DeepSeek将KV-Cache HBM需求降低75%。若AI推理成本持续上升导致需求放缓，存储和GPU超级周期可能提前见顶。",
        "tag": "产业风险",
        "tag_color": "orange",
    },
], cols=2)

gen.add_section("空方视角", bear_content, "⚠️")

# === 13. 教训库 ===
lessons_html = gen.build_lessons_section()
gen.add_section("历史教训", lessons_html, "📚")

# === 14. 每日总结 ===
gen.add_daily_summary()

# OG
gen.set_og(
    description="沙特管道遭袭原油跳涨3%，布伦特破108美元；十五五金融强国规划落地，打造A股上市首选地；国常会算力网顶层定调，光通信/液冷全链受益；HBM缺货潮传导国产AI芯片涨价20-50%",
    image="https://boya357.github.io/daily-news-insight/assets/og-daily.png"
)

# === 发布 ===
output_file = "docs/daily/20260914_每日新闻洞察.html"
result = gen.publish(output_file)
print(f"OK 报告已生成: {result}")
if result.get("success"):
    import shutil
    shutil.copy(output_file, "docs/daily/latest.html")
    print(f"LATEST 已更新 latest.html")
    print(f"SIZE 文件大小: {result.get('file_size')} 字节")
else:
    print(f"ERROR 验证失败: {result.get('errors')}")
