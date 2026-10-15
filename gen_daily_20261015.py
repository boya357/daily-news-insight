#!/usr/bin/env python3
"""2026-10-15 每日新闻洞察 - V3 Pro生成器"""
import sys, os
sys.path.insert(0, 'v3')
os.chdir('/root/daily-news-insight')
from generators.daily_pro import DailyReportProGenerator

gen = DailyReportProGenerator(
    date_str="2026-10-15",
    weekday="周四",
    subtitle="美国9月CPI超预期3.7%纳指大跌1.88%芯片股六连跌 | 费半重挫4.3%创2025年5月来最长跌势 | 央行7000亿逆回购护盘 | 嘉元科技前三季净利预增12倍",
    data_dir='/root/daily-news-insight/data'
)

# TL;DR
gen.set_tldr([
    ("美国9月CPI超预期 纳指重挫1.88%", "CPI同比3.7%环比0.6%均超预期，10月加息概率飙升至48.5%，纳指跌1.88%创7月来最大单日跌幅，道指-0.09%标普-1.11%", "red"),
    ("费城半导体暴跌4.3%六连跌", "费城半导体指数重挫4.3%连续6日下跌，创2025年5月以来最长下跌纪录，较6月高点累计跌超20%进入技术性熊市，ARM-6.8%SK海力士-6%AMD-5.7%", "red"),
    ("央行7000亿买断式逆回购护盘", "央行今日开展7000亿元6个月期买断式逆回购操作，保持银行体系流动性充裕，M2同比7.2%社融存量同比7.1%", "green"),
    ("中国9月CPI同比0.9%PPI环比+1.2%", "9月CPI环比0.2%同比0.9%，核心CPI同比1.0%；PPI环比1.2%工业品价格延续回升态势，经济复苏动能增强", "green"),
    ("嘉元科技前三季净利预增12倍", "嘉元科技预计前三季度归母净利润5.3-5.8亿元同比增1197%-1319%，铜箔需求景气度持续验证，铜冠铜箔产业链受益", "green"),
    ("都铎琼斯警告2027年做空美股", "华尔街传奇投资人保罗·都铎·琼斯表示2027年全年做空美股，称AI IPO潮+财政赤字将导致股票供应大增，市场像1999年互联网泡沫前夕", "red"),
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
                "title": "📉 美国9月CPI超预期 纳指重挫1.88%创7月来最大跌幅",
                "content": """美国劳工部10月14日公布9月CPI数据，全面超出市场预期：
<br><strong>CPI数据：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>同比 <strong style="color:#ef4444;">+3.7%</strong>（预期3.6%，前值3.4%），五个月来最大涨幅</li>
<li>环比 <strong style="color:#ef4444;">+0.6%</strong>（预期0.6%，前值0.4%），4月以来新高</li>
<li>核心CPI同比 <strong style="color:#ef4444;">+2.6%</strong>（预期2.5%，前值2.4%），四个月来最快涨幅</li>
<li>核心CPI环比 <strong>+0.3%</strong>（预期0.3%，前值0.3%）</li>
</ul>
<strong>通胀推手：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>汽油价格环比 <strong style="color:#ef4444;">+9.1%</strong>，对CPI涨幅贡献超过一半</li>
<li>能源指数环比+5.2%，住房成本环比+0.4%</li>
<li>娱乐、二手车、教育、机票、医疗、服装价格全线上涨</li>
</ul>
<strong>市场反应：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>交易员预计10月加息概率飙升至<strong style="color:#ef4444;">48.5%</strong>（周二仅22%）</li>
<li>预计到2027年底前美联储还将累计加息三次</li>
<li>10年期美债收益率和美元指数显著上涨</li>
</ul>
<em style="opacity:0.6">来源：新华网、金十数据、财联社</em>""",
            },
            {
                "title": "🔻 费城半导体暴跌4.3%六连跌 进入技术性熊市",
                "content": """费城半导体指数连续第六日下跌，创2025年5月以来最长下跌纪录：
<br><strong>收盘数据：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>费城半导体指数 <strong style="color:#ef4444;">-4.30%</strong> 报11684.38点</li>
<li>较6月历史高点累计跌幅已超<strong style="color:#ef4444;">20%</strong>，进入技术性熊市</li>
<li>ARM <strong style="color:#ef4444;">-6.81%</strong>、SK海力士 -6.06%、AMD -5.73%</li>
<li>英特尔 -4.56%、美光 -4.08%、应用材料 -3.79%</li>
<li>英伟达 -3.16%、博通 -3.10%、台积电ADR -3.40%、阿斯麦 -3.94%</li>
</ul>
<strong>下跌原因：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li><strong>通胀超预期：</strong>CPI数据打击降息预期，高利率压制科技股估值</li>
<li><strong>周期见顶担忧：</strong>存储芯片超级周期见顶讨论升温，韩股连续暴跌</li>
<li><strong>AI投资质疑：</strong>博通CEO+英特尔CEO连续警告AI投资风险</li>
<li><strong>获利回吐：</strong>年内涨幅巨大，资金从高位板块撤离</li>
</ul>
<strong>都铎琼斯警告：</strong>传奇投资人保罗·都铎·琼斯称2027年全年做空美股，市场像1999年互联网泡沫前夕。
<br><br>
<em style="opacity:0.6">来源：证券时报、凤凰网、财联社</em>""",
            },
            {
                "title": "💼 阿斯麦Q3财报：净利49.6亿欧元超预期 全年指引再上调",
                "content": """光刻机巨头阿斯麦(ASML)发布2026年第三季度财报：
<br><strong>核心数据：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>净销售额 <strong>116.6亿欧元</strong>，略低于市场预期</li>
<li>净利润 <strong style="color:#22c55e;">49.6亿欧元</strong>，超市场预期</li>
<li>毛利率 <strong style="color:#22c55e;">57.5%</strong>，双双超出市场预期</li>
</ul>
<strong>业绩指引：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li><strong>连续第三个季度提升全年业绩展望</strong></li>
<li>由于产能无法满足需求，订单排产已至2030年</li>
<li>正在评估进一步扩大2028年产能提升计划</li>
</ul>
<strong>市场意义：</strong>阿斯麦财报验证半导体设备需求仍强，但股价当日仍跌3.94%，反映市场整体情绪偏弱，以及对AI支出可持续性的担忧。
<br><strong>对A股影响：</strong>先进封装/半导体设备板块短期受外围情绪压制，但国产替代长期逻辑不变。
<br><br>
<em style="opacity:0.6">来源：凤凰网、公司财报</em>""",
            },
            {
                "title": "⚡ 都铎·琼斯：2027年全年做空美股 像1999年泡沫前夕",
                "content": """华尔街传奇投资人、都铎投资创始人保罗·都铎·琼斯重磅警告：
<br><strong>核心观点：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>"我2027年全年都会做空股市，原因就是它没什么价值"</li>
<li>当前市场像<strong>1999年互联网泡沫破裂前一年</strong></li>
<li>美股资金流和供需局面可能是2002年以来最糟糕的</li>
</ul>
<strong>做空两大理由：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li><strong>股票供应大增：</strong>Anthropic、OpenAI要上市，SpaceX刚完成大发行，更多公司增发筹钱搞AI建设</li>
<li><strong>财政赤字清算：</strong>不断膨胀的财政赤字可能迎来"算总账"时刻，没有政客会主动加税或削减开支</li>
</ul>
<strong>对石油的判断：</strong>琼斯表示做多石油，中期选举后油价可能再涨20-25美元，如果真这样股市会"非常讨厌"。
<br><br>
<em style="opacity:0.6">来源：证券时报、CNBC</em>""",
            },
            {
                "title": "🏆 苹果市值首次突破5万亿美元 成第二家5万亿公司",
                "content": """苹果逆市上涨，成为继英伟达之后第二家市值达5万亿美元的公司：
<br><strong>收盘数据：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>苹果股价 <strong style="color:#22c55e;">+0.50%</strong> 报342.96美元</li>
<li>总市值达到<strong style="color:#22c55e;">5.01万亿美元</strong></li>
<li>在科技股普跌行情中逆势走强，成为避险标的</li>
</ul>
<strong>背景：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>今年6月，英伟达市值首次突破5万亿美元</li>
<li>苹果凭借稳定现金流和消费电子龙头地位，在市场回调时展现防御属性</li>
<li>AI硬件/软件业务逐步推进，Vision Pro+Apple Intelligence双轮驱动</li>
</ul>
<strong>其他巨头表现：</strong>英伟达-3.16%、微软-1.80%、Meta-3%+、特斯拉-2%+、谷歌-1%+、亚马逊-1%+。
<br><br>
<em style="opacity:0.6">来源：财联社、东方财富</em>""",
            },
            {
                "title": "🛢️ 油价小幅回调 黄金涨1.26%避险需求升温",
                "content": """大宗商品市场震荡分化，地缘风险与加息预期博弈：
<br><strong>能源：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>WTI原油 <strong style="color:#ef4444;">-0.50%</strong> 报94.61美元/桶</li>
<li>布伦特原油 <strong style="color:#ef4444;">-0.59%</strong> 报105.43美元/桶</li>
<li>美军在阿曼湾摧毁与伊朗有关联帆船，中东地缘风险仍在</li>
<li>胡塞武装称击中一架沙特"台风"战斗机</li>
</ul>
<strong>贵金属：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>COMEX黄金 <strong style="color:#22c55e;">+1.26%</strong> 报4159.79美元</li>
<li>COMEX白银 <strong style="color:#22c55e;">+0.54%</strong> 报56.18美元</li>
<li>通胀超预期+地缘风险支撑贵金属避险需求</li>
</ul>
<strong>今日关注：</strong>国内成品油24时开启新一轮调价窗口。
<br><br>
<em style="opacity:0.6">来源：财联社、新华网</em>""",
            },
        ], cols=1)
    },
    {
        "label": "国内要闻",
        "content": gen.create_card_group([
            {
                "title": "🏦 央行7000亿买断式逆回购护盘 流动性充裕",
                "content": """中国人民银行10月15日开展大额流动性操作：
<ul style="margin:8px 0;padding-left:20px;">
<li>开展<strong style="color:#22c55e;">7000亿元</strong>买断式逆回购操作</li>
<li>期限：6个月（182天），到期日2027年4月15日</li>
<li>方式：固定数量、利率招标、多重价位中标</li>
<li>目的：保持银行体系流动性充裕</li>
</ul>
<strong>9月金融数据：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>M2余额<strong>359.63万亿元</strong>，同比增长7.2%</li>
<li>社会融资规模存量<strong>468.17万亿元</strong>，同比增长7.1%</li>
<li>前三季度社融增量累计27.46万亿元，同比少2.63万亿元</li>
<li>对实体经济发放人民币贷款增加11.5万亿元，同比少增3.04万亿元</li>
</ul>
<strong>解读：</strong>央行大额逆回购释放护盘信号，有助于稳定市场预期，缓解外围市场波动带来的流动性压力。
<br><br>
<em style="opacity:0.6">来源：中国人民银行、中国证券报</em>""",
            },
            {
                "title": "📊 中国9月CPI同比0.9% PPI环比+1.2% 经济复苏动能增强",
                "content": """国家统计局10月14日发布9月物价数据：
<br><strong>CPI数据：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>环比 <strong>+0.2%</strong>，涨幅比上月回落0.2个百分点</li>
<li>同比 <strong style="color:#22c55e;">+0.9%</strong>，涨幅比上月扩大0.1个百分点</li>
<li>核心CPI同比 <strong>+1.0%</strong>，涨幅与上月相同</li>
</ul>
<strong>PPI数据：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>环比 <strong style="color:#22c55e;">+1.2%</strong>，工业品价格延续回升</li>
<li>工业生产活跃度提升，需求端持续改善</li>
</ul>
<strong>进出口数据：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>前三季度进出口总值<strong>39.94万亿元</strong>，同比增长18.8%</li>
<li>贸易韧性延续，外需表现超预期</li>
</ul>
<strong>解读：</strong>CPI温和回升+PPI转正+进出口高增，显示经济复苏动能增强，但仍需关注内需恢复力度。
<br><br>
<em style="opacity:0.6">来源：国家统计局、海关总署</em>""",
            },
            {
                "title": "💰 嘉元科技前三季净利预增12倍 铜箔需求景气验证",
                "content": """嘉元科技(688388)发布2026年前三季度业绩预告：
<br><strong>核心数据：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>预计归母净利润 <strong style="color:#22c55e;">5.3-5.8亿元</strong></li>
<li>同比增长 <strong style="color:#22c55e;">1196.6% - 1318.9%</strong>（约12倍）</li>
<li>业绩变动主因：下游行业景气度上升，铜箔需求稳步增长</li>
<li>产能建设与技术改造推动产能利用率上升，单位成本降低</li>
</ul>
<strong>对持仓的意义：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>铜冠铜箔（持仓标的）同属铜箔赛道，行业高景气度得到验证</li>
<li>铜箔量价齐升逻辑持续兑现，关注铜冠铜箔三季报表现</li>
<li>锂电铜箔+电子电路铜箔双轮驱动，需求结构性向好</li>
</ul>
<strong>其他业绩亮点：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>远大控股：前三季净利预增890%-1018%</li>
<li>佛塑科技：前三季净利预增1330%-1568%（重组后368%-446%）</li>
<li>荣盛石化：前三季净利预增778%-823%</li>
</ul>
<em style="opacity:0.6">来源：公司公告、中国证券报</em>""",
            },
            {
                "title": "📈 北向资金三季度调仓 银行医药增配 AI出海链减配",
                "content": """沪深股通2026年三季度末持股数据出炉：
<br><strong>整体规模：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>北向资金共持有3531只个股，持仓总规模<strong>2.577万亿元</strong></li>
<li>较二季度末3.127万亿元回落超5500亿元</li>
<li>与一季度末2.572万亿元基本持平</li>
</ul>
<strong>加仓方向：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li><strong>银行板块：</strong>持股市值增673亿元，环比+47%，增幅居31个申万行业榜首</li>
<li><strong>医药生物：</strong>持仓市值增幅显著</li>
<li><strong>非银金融、交通运输、家电、食品饮料：</strong>大金融大消费板块获增配</li>
</ul>
<strong>减仓方向：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>AI产业链、出海链方向获减配</li>
<li>第一大重仓行业仍为电子，第一大重仓股为宁德时代</li>
</ul>
<strong>解读：</strong>北向资金从高位成长股转向低估值红利板块，防御性配置思路明显。
<br><br>
<em style="opacity:0.6">来源：上海证券报</em>""",
            },
            {
                "title": "🎮 游戏板块连续反弹 版号常态化+储备新品驱动",
                "content": """A股游戏板块近期出现连续反弹行情：
<ul style="margin:8px 0;padding-left:20px;">
<li>10月14日短剧游戏、网络游戏等概念板块涨幅居前</li>
<li>传媒板块近几个交易日成为主力资金净流入主要方向</li>
<li>年初至今游戏版号审批节奏逐步趋于平稳</li>
<li>行业供给端预期持续巩固，储备新品进入测试上线周期</li>
</ul>
<strong>催化因素：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>AI赋能游戏降本增效持续推进</li>
<li>版号常态化发放消除政策不确定性</li>
<li>多款重磅新品进入上线窗口期</li>
</ul>
<br>
<em style="opacity:0.6">来源：财联社</em>""",
            },
            {
                "title": "🏛️ 王毅会见拉夫罗夫 讨论APEC及国际协作",
                "content": """当地时间10月14日，王毅在巴库会见俄罗斯外长拉夫罗夫：
<ul style="margin:8px 0;padding-left:20px;">
<li>祝贺俄方成功举行国家杜马选举</li>
<li>下月APEC领导人非正式会议将在深圳举行</li>
<li>俄方全力支持中方办好APEC会议</li>
<li>两国就高层交往及国际热点问题协调立场</li>
</ul>
<strong>其他地缘动态：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>朝鲜试射两种潜射战略巡航导弹</li>
<li>美军在阿曼湾摧毁与伊朗有关联帆船</li>
<li>胡塞武装称过去24小时遭沙特联军42次空袭</li>
</ul>
<br>
<em style="opacity:0.6">来源：新华社</em>""",
            },
        ], cols=1)
    },
]

news_tab_html = gen.create_tab_pane(news_tabs, tab_id="important-news", style="default")
gen.add_section("重大新闻", news_tab_html, "📰")

# === 4. 行业追踪 ===
industry_content = gen.create_card_group([
    {"title": "🔋 存储芯片/HBM", "content": "⚠️ S级主线 | 费半暴跌4.3%六连跌进入技术性熊市，SK海力士-6%美光-4%，存储超级周期见顶担忧升温。外围恐慌情绪传导，A股存储板块承压明显，但国产替代逻辑不变，关注开盘后承接力度", "icon": "🔴"},
    {"title": "💻 AI算力/液冷", "content": "⚠️ S级主线 | 英伟达-3.16%AMD-5.73%微软-1.8%，科技股普跌+CPI超预期加息概率飙升，AI板块估值承压。但英伟达中国开发者日今明两天在苏州举行，关注催化信号", "icon": "🔴"},
    {"title": "🔧 半导体设备/材料", "content": "⭐ A级主线 | 阿斯麦Q3净利超预期+全年指引上调，但股价仍跌3.94%。设备板块短期外围情绪拖累，中期国产替代逻辑强化，关注雅克科技、华海诚科等材料端机会", "icon": "🟡"},
    {"title": "🤖 人形机器人/智能制造", "content": "⭐ A级主线 | 工博会后政策持续催化，新质生产力方向不变。但外围科技股大跌拖累情绪，板块分化明显，关注有业绩支撑的核心标的", "icon": "🟠"},
    {"title": "🏦 银行/红利", "content": "⭐ A级主线 | 北向资金三季度增配银行板块环比+47%，中国太保首次中期分红10派4.2元。在市场波动期，高股息红利资产防御属性凸显", "icon": "🟢"},
    {"title": "🛢️ 油气/能源", "content": "B级主线 | 油价维持高位布油105美元，中东地缘风险持续，CPI中能源项贡献最大。油气/煤炭/新能源等能源板块或有结构性机会", "icon": "🟡"},
], cols=2)
gen.add_section("行业追踪", industry_content, "🏭")

# === 5. 今日催化 ===
catalyst_content = gen.create_card_group([
    {"title": "🔻 美股暴跌+CPI超预期 A股开盘承压", "content": "纳指-1.88%费半-4.3%芯片股六连跌，美国9月CPI超预期加息概率飙升至48.5%，A股半导体/科技板块开盘压力大，注意控制仓位", "icon": "🔴"},
    {"title": "🏦 央行7000亿逆回购护盘", "content": "央行今日开展7000亿元6个月期买断式逆回购，释放稳定流动性信号，有助于对冲外围市场波动影响", "icon": "🟢"},
    {"title": "💡 英伟达中国开发者日 苏州举行", "content": "英伟达GTC China 10月15-16日在苏州举行，关注AI算力、液冷、先进封装等方向的最新技术发布和合作动态", "icon": "🟠"},
    {"title": "📈 嘉元科技净利预增12倍 铜箔催化", "content": "嘉元科技前三季净利预增1197%-1319%，验证铜箔行业高景气度，铜冠铜箔同赛道受益，关注铜箔板块表现", "icon": "🟢"},
], cols=2)
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
    {"title": "CPI超预期+加息概率飙升 全球流动性收紧", "content": "美国9月CPI同比3.7%超预期，10月加息概率从22%飙升至48.5%，预计到2027年底还将加息三次。美债收益率上行，外资流出压力加大，科技成长股估值承压。", "tag": "利率风险", "tag_color": "red"},
    {"title": "费城半导体进入技术性熊市 芯片周期见顶担忧", "content": "费半六连跌较6月高点跌超20%，ARM-6.8%SK海力士-6%AMD-5.7%。存储超级周期见顶+AI投资回报质疑+获利回吐三重利空，A股半导体板块面临情绪传导压力。", "tag": "板块风险", "tag_color": "red"},
    {"title": "都铎·琼斯警告美股泡沫 传奇投资人做空信号", "content": "华尔街传奇投资人都铎·琼斯称2027年全年做空美股，市场像1999年互联网泡沫前夕。AI IPO潮+财政赤字导致股票供应大增，若全球风险偏好下降，A股难以独善其身。", "tag": "系统性风险", "tag_color": "red"},
    {"title": "持仓4只标的外围承压 注意开盘风险", "content": "英维克/雅克科技属AI算力+半导体材料赛道，外围科技股暴跌+芯片股六连跌，开盘或大幅低开。铜冠铜箔虽有嘉元科技业绩催化，但整体情绪偏空。需严格执行止损纪律。", "tag": "持仓风险", "tag_color": "red"},
    {"title": "北向资金三季度减配AI 外资持续流出", "content": "北向资金三季度减配AI、出海链方向，增配银行医药等红利板块。在外围加息预期下，外资流出压力持续，高位科技股面临资金撤离风险。", "tag": "资金风险", "tag_color": "orange"},
    {"title": "中东地缘风险升温 油价推升通胀", "content": "美军在阿曼湾打击伊朗关联目标，胡塞武装与沙特冲突升级。地缘风险支撑油价，而油价推升通胀预期，形成油价→通胀→加息→科技股下跌的传导链。", "tag": "地缘风险", "tag_color": "orange"},
], cols=2)
gen.add_section("空方视角", bear_content, "⚠️")

# === 13. 教训库 ===
lessons_html = gen.build_lessons_section()
gen.add_section("历史教训", lessons_html, "📚")

# === 14. 每日总结 ===
gen.add_daily_summary()

# OG
gen.set_og(
    description="美国9月CPI超预期3.7%纳指重挫1.88%，费城半导体暴跌4.3%六连跌进入技术性熊市；央行7000亿逆回购护盘，嘉元科技前三季净利预增12倍铜箔景气验证；都铎·琼斯警告2027年做空美股像1999年泡沫前夕",
    image="https://boya357.github.io/daily-news-insight/assets/og-daily.png"
)

# === 发布 ===
output_file = "docs/daily/20261015_每日新闻洞察.html"
result = gen.publish(output_file)
print(f"OK 报告已生成: {result}")
if result.get("success"):
    import shutil
    shutil.copy(output_file, "docs/daily/latest.html")
    print(f"LATEST 已更新 latest.html")
    print(f"SIZE 文件大小: {result.get('file_size')} 字节")
else:
    print(f"ERROR 验证失败: {result.get('errors')}")
