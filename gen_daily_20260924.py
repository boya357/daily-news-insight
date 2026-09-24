#!/usr/bin/env python3
"""2026-09-24 每日新闻洞察 - V3 Pro生成器"""
import sys, os
sys.path.insert(0, 'v3')
os.chdir('/root/daily-news-insight')
from generators.daily_pro import DailyReportProGenerator

gen = DailyReportProGenerator(
    date_str="2026-09-24",
    weekday="周四",
    subtitle="美联储鹰派升温纳指跌1.13% | 花旗上调美光目标价至1300美元 | HBM供需缺口扩大三星扩产40%",
    data_dir='/root/daily-news-insight/data'
)

# TL;DR
gen.set_tldr([
    ("美联储鹰派升温 美股集体收跌", "纳指跌1.13%报26936点，费城半导体跌1.23%，10年期美债收益率创2007年新高5.135%，10月加息概率升至69.7%，芯片股普跌博通-2.62%美光-2.22%", "red"),
    ("花旗上调美光目标价至1300美元", "花旗预计DRAM价格表现超预期，上调美光Q4营收至510亿EPS 31.45美元，SEMICON West前仍有上行空间；但大空头伯里再度加码做空美光", "orange"),
    ("HBM供需缺口持续拉大 三星扩产40%", "三星2027年HBM产能从18万片增至25万片/月，HBM4占比从40%升至80%，伯恩斯坦预计三星Q3 HBM营收环比+72%至114亿美元，HBM现货价已涨至长约价4-5倍", "green"),
    ("工信部印发AI+软件专项行动方案", "到2028年培育一批智能编程工具，推广覆盖2万家规模以上软件企业，打造100个智能体软件标杆应用，智能体软件新业态加速涌现", "green"),
    ("持仓：铜冠铜箔涨4.09%领涨", "铜冠铜箔+4.09%报119.23元，雅克科技+1.31%报137.28元，英维克-0.44%报61.25元，*ST建艺-0.23%报13.17元", "orange"),
])

# === 1. 隔夜全球市场 ===
gen.add_global_market()

# === 2. 市场总览 ===
gen.add_market_overview()

# === 3. 重大新闻 - tab切换 ===
news_tabs = [
    {
        "label": "美联储&宏观",
        "content": gen.create_card_group([
            {
                "title": "📉 美联储鹰派信号升温 纳指跌1.13%美债收益率创19年新高",
                "content": """周三美股三大指数集体收跌，美债收益率飙升压制风险资产：
<br>
<ul style="margin:8px 0;padding-left:20px;">
<li>道琼斯 <strong style="color:#ef4444;">-0.68%</strong> 报51511点</li>
<li>标普500 <strong style="color:#ef4444;">-0.75%</strong> 报7706点</li>
<li>纳斯达克 <strong style="color:#ef4444;">-1.13%</strong> 报26936点</li>
<li>费城半导体 <strong style="color:#ef4444;">-1.23%</strong> 报12534点</li>
<li>10年期美债收益率触及<strong>5.135%</strong>，创2007年7月以来新高</li>
</ul>
<strong>加息预期升温：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>CME美联储观察：10月加息25bp概率升至<strong>69.7%</strong></li>
<li>12月累计加息50bp概率升至<strong>54.8%</strong></li>
<li>多位美联储官员释放偏鹰信号，油价+关税推升通胀</li>
<li>高盛：核心通胀被关税和内存价格统计偏差虚增，剔除后内生通胀反降</li>
</ul>
<strong>市场影响：</strong>黄金股集体大跌（盎格鲁黄金-5.6%），中概股多数收跌（阿里-4.75%百度-2.87%），金融板块普跌。
<br><br>
<em style="opacity:0.6">来源：新华财经、证券时报、CME</em>""",
            },
            {
                "title": "⚠️ 纳斯达克创新高背后科技股极端分化 2000年泡沫警示信号",
                "content": """尽管纳指接连创新高，但内部极端分化与2000年互联网泡沫前特征高度相似：
<br>
<ul style="margin:8px 0;padding-left:20px;">
<li>费城半导体指数较6月高点仍跌14%，30只成分股中10只较52周高点回撤超30%</li>
<li>半导体成分股平均回撤幅度达<strong>26%</strong></li>
<li>标普500近一月涨1.2%，但11个行业板块中有9个收跌</li>
<li>市场广度极度收窄，少数科技巨头拉动指数</li>
</ul>
<strong>历史对比：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>与2000年互联网泡沫破裂前特征高度相似</li>
<li>分析师警示中期维度需保持谨慎</li>
<li>当前科技股估值分化程度已达历史极值</li>
</ul>
<strong>对A股启示：</strong>科技板块结构性行情下需精选真成长标的，警惕纯概念炒作退潮风险。
<br><br>
<em style="opacity:0.6">来源：新浪财经、券商研报</em>""",
            },
            {
                "title": "🏦 央行9月MLF加量续作2000亿元 维护流动性充裕",
                "content": """中国人民银行9月24日开展8000亿元MLF操作，本月加量续作2000亿元：
<br>
<ul style="margin:8px 0;padding-left:20px;">
<li>操作规模：8000亿元1年期MLF</li>
<li>到期规模：6000亿元</li>
<li>净投放：<strong>2000亿元</strong></li>
<li>操作方式：固定数量、利率招标、多重价位中标</li>
</ul>
<strong>政策意图：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>保持银行体系流动性充裕</li>
<li>对冲节前资金需求，维护市场平稳</li>
<li>释放稳增长政策信号</li>
</ul>
<br><br>
<em style="opacity:0.6">来源：央行公告、澎湃新闻</em>""",
            },
        ], cols=1)
    },
    {
        "label": "半导体/存储",
        "content": gen.create_card_group([
            {
                "title": "🎯 花旗上调美光目标价至1300美元 SEMICON West前仍有上行空间",
                "content": """花旗发布报告上调美光科技目标价，看好存储行业供需紧张格局：
<br>
<ul style="margin:8px 0;padding-left:20px;">
<li>目标价从1150美元上调至<strong>1300美元</strong></li>
<li>预计Q4营收达<strong>510亿美元</strong>，EPS达<strong>31.45美元</strong></li>
<li>综合DRAM售价高于此前预期，未来几季业绩/指引仍有上行空间</li>
<li>SEMICON West大会将是下一重要催化剂</li>
</ul>
<strong>供给约束逻辑：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>设备/PCB/光学元件等供应链瓶颈限制产能扩张</li>
<li>DRAM和NAND供给增长被压制在20%出头水平</li>
<li>DRAM价格预计持续上涨至2027年Q2见顶</li>
<li>当前季度DRAM均价预计环比涨20%，下季度再涨13%</li>
</ul>
<strong>空方观点：</strong>大空头迈克尔·伯里再度加码做空美光，对半导体和AI热潮持久性存疑。
<br><br>
<em style="opacity:0.6">来源：花旗研报、新浪财经</em>""",
            },
            {
                "title": "🔋 HBM供需缺口持续拉大 三星产能提升40%抢英伟达订单",
                "content": """HBM行业景气度持续升温，供需缺口短期难以逆转：
<br>
<ul style="margin:8px 0;padding-left:20px;">
<li>三星2027年HBM总产能从18万片/月增至<strong>25万片/月</strong>（+40%）</li>
<li>HBM4系列占比从今年40%大幅提升至明年<strong>80%</strong></li>
<li>伯恩斯坦预计三星Q3 HBM营收环比<strong>+72%</strong>至约114亿美元</li>
<li>HBM现货价已涨至长约价的<strong>4-5倍</strong>，现货市场极度紧缺</li>
</ul>
<strong>三巨头产能竞赛：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>三星：HBM4月产能10-12万片，玻璃载板采购量提升至2.5倍</li>
<li>SK海力士：HBM4已量产出货，12层稳定量产，16层认证中</li>
<li>美光：已交付超10亿美元HBM4产品，年底产能达10万片/月</li>
</ul>
<strong>产业链利好：</strong>2026年全球HBM市场规模预计增长58%至546亿美元，产能缺口维持50-60%，国产存储/先进封装产业链持续受益。
<br><br>
<em style="opacity:0.6">来源：DigiTimes、伯恩斯坦、国金证券</em>""",
            },
            {
                "title": "💡 HBM价格高企 英伟达Rubin削减HBM用量 Feynman才配512GB",
                "content": """HBM内存价格持续上涨，连英伟达也开始调整产品策略控制成本：
<br>
<ul style="margin:8px 0;padding-left:20px;">
<li>英伟达Rubin Ultra将HBM从12层<strong>砍至8层</strong></li>
<li>下一代Feynman才会配置512GB HBM内存</li>
<li>存储成本上涨背景下，更重视单位带宽成本与整机经济性</li>
<li>宏碁CEO警告：大陆存储产能增加2027年底或缓解供应压力</li>
</ul>
<strong>英特尔表态：</strong>CXL不是HBM的替代品，只能作为二级存储补充，两者形成互补关系。
<br><br>
<strong>对市场影响：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>短期：HBM供需紧张仍持续，价格支撑逻辑未变</li>
<li>中期：需关注英伟达减配对HBM需求增速的边际影响</li>
<li>长期：CXL等技术或逐步成为补充方案</li>
</ul>
<br>
<em style="opacity:0.6">来源：快科技、SemiAnalysis</em>""",
            },
        ], cols=1)
    },
    {
        "label": "国内政策&产业",
        "content": gen.create_card_group([
            {
                "title": "🤖 工信部印发「人工智能+软件」专项行动实施方案",
                "content": """工信部发布AI+软件专项行动方案，智能体软件成为核心方向：
<br>
<strong>2028年目标：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>培育一批高水平智能编程工具和智能开发平台</li>
<li>推广覆盖<strong>2万家</strong>规模以上软件企业</li>
<li>组织实施100项软件企业智能化技改项目</li>
<li>打造<strong>100个</strong>智能体软件标杆应用</li>
<li>孵化5个以上优质开源项目</li>
</ul>
<strong>三大重点方向：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>推进软件生产变革：智能编程工具链、软件企业智能化技改</li>
<li>加快软件产品智能化升级：基础软件/工业软件智能化转型</li>
<li>培育智能体软件新业态：智能体软件技术基础、产品、应用市场</li>
</ul>
<strong>2030年远景：</strong>关键软件全面智能化升级，智能编程/智能体软件/智能服务成为产业新增长极。
<br><br>
<em style="opacity:0.6">来源：工信部、证券时报e公司</em>""",
            },
            {
                "title": "📡 工信部：系统推进新一代通信网建设 推动算力设施扩容提质",
                "content": """工信部副部长在2026中国国际信息通信展览会开幕式上表态：
<br>
<ul style="margin:8px 0;padding-left:20px;">
<li>坚持应用牵引、<strong>适度超前</strong>、系统推进新一代通信网建设</li>
<li>推进低轨卫星互联网系统建设</li>
<li>统筹优化国际海陆网络布局</li>
<li>推动算力设施扩容提质，强化算网协同和算力互联</li>
<li>加快信息通信网络和行业智能化升级</li>
</ul>
<strong>AI与通信融合：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>超前研判人工智能对信息通信网络体系的变革性影响</li>
<li>积极推进AI与信息通信融合创新</li>
</ul>
<strong>相关受益方向：</strong>算力基础设施、液冷散热、光模块、卫星互联网、算网一体化。
<br><br>
<em style="opacity:0.6">来源：新华社、通信世界</em>""",
            },
            {
                "title": "📱 小米全球首发高通第六代双旗舰骁龙8平台",
                "content": """2026骁龙峰会上，小米宣布全球首发高通最新旗舰处理器：
<br>
<ul style="margin:8px 0;padding-left:20px;">
<li>骁龙8超级至尊版 + 骁龙8至尊版两款2纳米制程芯片</li>
<li>首发机型：小米18 Pro系列，9月23日国内发布</li>
<li>主打终端侧AI性能提升</li>
<li>小米、vivo、荣耀等头部品牌均将率先搭载</li>
</ul>
<strong>产业意义：</strong>2nm制程芯片量产标志着半导体工艺持续推进，终端侧AI算力大幅提升，智能体应用硬件基础进一步夯实。
<br><br>
<em style="opacity:0.6">来源：新浪财经</em>""",
            },
        ], cols=1)
    },
]

news_tab_html = gen.create_tab_pane(news_tabs, tab_id="important-news", style="default")
gen.add_section("重大新闻", news_tab_html, "📰")

# === 4. 行业追踪 ===
industry_content = gen.create_card_group([
    {
        "title": "🔋 存储芯片/HBM",
        "content": "⭐ S级主线 | 花旗上调美光目标价至1300美元，HBM供需缺口持续扩大三星扩产40%，伯恩斯坦料三星Q3 HBM营收环比+72%，存储超级周期延续",
        "icon": "🟢",
    },
    {
        "title": "💻 AI算力/液冷",
        "content": "⭐ S级主线 | 工信部推算力设施扩容提质+算网互联，英伟达Rubin减配HBM关注成本压力，美联储加息压制科技股估值",
        "icon": "🟡",
    },
    {
        "title": "🔧 先进封装",
        "content": "⭐ A级主线 | HBM扩产拉动先进封装需求，三星玻璃载板采购量提升2.5倍，国产封装材料/设备持续受益国产替代",
        "icon": "🟢",
    },
    {
        "title": "🤖 智能体软件",
        "content": "⭐ 新催化 | 工信部印发AI+软件专项行动方案，2028年打造100个智能体标杆应用，智能体软件新业态政策催化落地",
        "icon": "🟢",
    },
], cols=2)

gen.add_section("行业追踪", industry_content, "🏭")

# === 5. 今日催化 ===
catalyst_content = gen.create_card_group([
    {
        "title": "🏦 MLF加量续作",
        "content": "央行今日开展8000亿MLF操作，净投放2000亿，释放稳增长信号，关注今日LPR报价及市场流动性反应",
        "icon": "🟢",
    },
    {
        "title": "📰 文旅部十五五发布会",
        "content": "今日上午10时国新办举行文旅部十五五高质量发展发布会，关注文旅消费政策方向",
        "icon": "🟡",
    },
    {
        "title": "⚠️ 美联储加息压制",
        "content": "10年期美债收益率创19年新高5.135%，10月加息概率升至70%，外资流入节奏或受扰动",
        "icon": "🔴",
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
        "title": "美联储加息预期升温 全球风险资产承压",
        "content": "10年期美债收益率创2007年以来新高5.135%，10月加息概率升至69.7%，美元走强压制新兴市场。高利率环境下成长股估值面临压力，外资流入A股节奏可能受扰动。需密切关注美联储官员讲话和通胀数据走向。",
        "tag": "外部风险",
        "tag_color": "red",
    },
    {
        "title": "科技股极端分化 2000年泡沫警示",
        "content": "纳指创新高但费城半导体较6月高点跌14%，30只成分股10只回撤超30%，标普500近一月仅2个板块上涨，与2000年互联网泡沫破裂前特征相似。A股科技板块同样存在内部分化，纯概念标的需警惕退潮风险。",
        "tag": "估值风险",
        "tag_color": "red",
    },
    {
        "title": "英伟达削减HBM用量 需求边际变化需警惕",
        "content": "英伟达Rubin Ultra将HBM从12层砍至8层，宏碁CEO警告大陆存储产能2027年底或缓解供应压力，大空头伯里加码做空美光。虽然当前HBM供需缺口仍大，但需关注需求端边际变化对存储板块情绪的影响。",
        "tag": "产业风险",
        "tag_color": "orange",
    },
    {
        "title": "假日效应 节前市场波动可能加大",
        "content": "中秋（9月25日）国庆假期临近，市场交投情绪可能趋于谨慎，成交缩量背景下个股波动可能放大。建议控制仓位，避免追高，持币过节还是持股过节需根据个人风险偏好决定。",
        "tag": "节假日风险",
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
    description="美联储鹰派升温纳指跌1.13%，10年期美债收益率创19年新高；花旗上调美光目标价至1300美元，HBM供需缺口持续扩大三星扩产40%；工信部印发AI+软件专项行动方案；持仓铜冠铜箔涨4.09%领涨",
    image="https://boya357.github.io/daily-news-insight/assets/og-daily.png"
)

# === 发布 ===
output_file = "docs/daily/20260924_每日新闻洞察.html"
result = gen.publish(output_file)
print(f"OK 报告已生成: {result}")
if result.get("success"):
    import shutil
    shutil.copy(output_file, "docs/daily/latest.html")
    print(f"LATEST 已更新 latest.html")
    print(f"SIZE 文件大小: {result.get('file_size')} 字节")
else:
    print(f"ERROR 验证失败: {result.get('errors')}")
