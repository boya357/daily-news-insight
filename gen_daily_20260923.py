#!/usr/bin/env python3
"""2026-09-23 每日新闻洞察 - V3 Pro生成器"""
import sys, os
sys.path.insert(0, 'v3')
os.chdir('/root/daily-news-insight')
from generators.daily_pro import DailyReportProGenerator

gen = DailyReportProGenerator(
    date_str="2026-09-23",
    weekday="周三",
    subtitle="存储芯片四巨头集体暴涨 | 美光单季净利剑指350亿超微软 | 纳指再创历史新高",
    data_dir='/root/daily-news-insight/data'
)

# TL;DR
gen.set_tldr([
    ("存储芯片四巨头集体暴涨", "闪迪+6.82%美光+5%西数+3.67%SK海力士+3.45%，费城半导体+2.06%，美光9月30日财报前持续拉升，分析师预测2027财年利润或超微软", "green"),
    ("纳指再创历史新高", "纳指收涨0.45%报27244点创收盘新高，半导体全线拉升，ARM+3.19%高通+2.08%阿斯麦+2.14%，道指微跌标普平收", "green"),
    ("美光单季净利剑指350亿美元", "美光FY26Q4指引净利润约350亿美元，毛利率逼近87%，16项SCA协议锁定约千亿美元营收，HBM售罄至2027年", "green"),
    ("9月22日A股窄幅震荡", "沪指涨0.06%报3952点深成指微跌，成交2.14万亿，铜冠铜箔+2.70%领涨持仓，英维克-1.14%雅克科技-1.15%", "orange"),
    ("日本收紧先进封装材料出口", "日本METI将IC封装特种聚合物纳入A-2类出口管制，对华单批超500kg需提前30天申报，利好国产替代", "orange"),
])

# === 1. 隔夜全球市场 ===
gen.add_global_market()

# === 2. 市场总览 ===
gen.add_market_overview()

# === 3. 重大新闻 - tab切换 ===
news_tabs = [
    {
        "label": "存储芯片",
        "content": gen.create_card_group([
            {
                "title": "🚀 存储芯片四巨头集体暴涨 美光涨5%闪迪涨6.82%",
                "content": """隔夜美股存储芯片板块全线爆发，四大龙头集体大涨：
<br>
<ul style="margin:8px 0;padding-left:20px;">
<li><strong>闪迪 +6.82%</strong>、<strong>美光科技 +5.00%</strong></li>
<li><strong>西部数据 +3.67%</strong>、<strong>SK海力士 +3.45%</strong></li>
<li>希捷科技 +4.85%、费城半导体指数 +2.06%</li>
</ul>
<strong>催化因素：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>META个人AI智能体工具Muse上线两周登顶iOS免费榜，智能体应用爆火推升CPU/存储需求预期</li>
<li>美联储加息靴子落地，利空出尽推动科技板块上涨</li>
<li>美光9月30日发布Q4财报，市场预期单季EPS达31美元，创历史新高</li>
</ul>
<strong>机构观点：</strong>中泰证券认为费城半导体指数补涨意味着新一轮全球科技板块轮动行情启动，国产算力链后市有较大补涨空间。
<br><br>
<em style="opacity:0.6">来源：中新经纬、中国证券报、东方财富网</em>""",
            },
            {
                "title": "💰 美光单季净利剑指350亿美元 分析师称2027年利润或超微软",
                "content": """美光科技FY26Q4指引净利润约350亿美元，单季利润超上年全年四倍，分析师大胆预测2027财年利润有望超越微软：
<br><strong>核心数据：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>FY26Q3净利润282亿美元，Q4指引再增约25%</li>
<li>DRAM平均售价环比上涨60%+，出货量仅增长低个位数</li>
<li>毛利率从37.7%飙升至84.6%，Q4指引86%</li>
<li>FY27 EPS预期156美元/股，对应P/E仅6.8倍</li>
</ul>
<strong>16项SCA协议锁定收入：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>覆盖约20% DRAM产量和1/3 NAND产量</li>
<li>累计最低承诺收入近1000亿美元，含220亿现金定金</li>
<li>多数为5年照付不议合同，设定价格上下限</li>
</ul>
<strong>关键判断：</strong>美光CEO称"存储行业已被AI结构性变革"，供需紧张持续至2027年后，HBM产能是主要瓶颈。
<br><br>
<em style="opacity:0.6">来源：智通财经、S&P Global、24/7 Wall St.</em>""",
            },
            {
                "title": "🔒 HBM售罄至2027年 供需格局深度紧张",
                "content": """美光最新披露HBM产品已售罄至2027年，客户需求远超供给能力：
<br>
<ul style="margin:8px 0;padding-left:20px;">
<li>美光只能满足最大AI客户50-67%的需求</li>
<li>HBM3E与DDR产能消耗比约3:1，HBM4E或升至4:1</li>
<li>DRAM已成为AI基础设施首要瓶颈，超过电力和算力</li>
<li>部分客户因DRAM供应不足被迫降低单服务器内存密度</li>
</ul>
<strong>三巨头产能竞赛：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>三星：2027年HBM总产能从18万片/月增至25万片/月，HBM4占比从40%升至80%</li>
<li>SK海力士：清州M15X厂产能从1万片跃升至8万片/月，龙仁新厂2027年投产</li>
<li>美光：年底HBM产能增至10万片/月，目标缩小与双雄差距</li>
</ul>
<strong>投资启示：</strong>存储超级周期延续性超预期，国产存储替代赛道（长鑫存储产业链、HBM材料）长期受益。
<br><br>
<em style="opacity:0.6">来源：S&P Global、半导体行业观察</em>""",
            },
        ], cols=1)
    },
    {
        "label": "海外市场",
        "content": gen.create_card_group([
            {
                "title": "📈 纳指创历史新高 半导体全线拉升",
                "content": """美股三大股指周二收盘涨跌不一，纳指再创新高：
<br><strong>核心指数：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>道琼斯 <strong style="color:#ef4444;">-0.36%</strong> 报51863点</li>
<li>标普500 基本平收报7764点</li>
<li>纳斯达克 <strong style="color:#22c55e;">+0.45%</strong> 报27244点，创收盘历史新高</li>
<li>费城半导体 <strong style="color:#22c55e;">+2.06%</strong> 报12689点</li>
</ul>
<strong>大型科技股分化：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>特斯拉+0.96%、英伟达+0.66%、苹果+0.23%</li>
<li>Meta-0.63%、微软-0.72%、谷歌-0.99%、亚马逊-1.34%</li>
</ul>
<strong>中概股：</strong>纳斯达克中国金龙指数+0.32%，BOSS直聘+2.63%、理想汽车+1.22%、拼多多+1.33%。
<br><br>
<em style="opacity:0.6">来源：中新经纬、东方财富网</em>""",
            },
            {
                "title": "🛢️ 油价回落 金价反弹逼近4400美元",
                "content": """大宗商品市场分化，油价下跌金价走强：
<br>
<ul style="margin:8px 0;padding-left:20px;">
<li>WTI原油 -0.75% 报89.85美元，失守90美元关口</li>
<li>布伦特原油 -0.56% 报94.88美元</li>
<li>COMEX黄金 <strong style="color:#22c55e;">+0.58%</strong> 报4401.77美元，再度逼近4400关口</li>
<li>COMEX白银 <strong style="color:#22c55e;">+2.16%</strong> 报67.97美元</li>
<li>美元指数 +0.17% 报100.60</li>
</ul>
<strong>驱动因素：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>中东地缘冲突缓和 + 美联储加息靴子落地，推动油价回落金价企稳</li>
<li>申万期货认为黄金价格中枢中长期仍具备向上基础</li>
</ul>
<br><br>
<em style="opacity:0.6">来源：中新经纬</em>""",
            },
            {
                "title": "🇯🇵 日本收紧先进封装材料出口管制",
                "content": """日本经济产业省(METI)修订先进材料出口管制指南，将高密度IC封装用特种聚合物纳入严格管控：
<br>
<ul style="margin:8px 0;padding-left:20px;">
<li>苯并环丁烯(BCB)、聚酰亚胺衍生物等纳入A-2类出口许可管理</li>
<li>涉及ABF载板材料、2.5D/3D Chiplet封装应用</li>
<li>对华单批出口超500kg需提前30天申报</li>
</ul>
<strong>影响评估：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>短期：中日封装材料合作项目进度可能放缓，国内封测厂高端基材供应稳定性受关注</li>
<li>中长期：加速国产替代进程，利好国内先进封装材料企业（雅克科技等前驱体/光刻胶企业）</li>
<li>欧盟同步推进：2.1亿欧元资助英飞凌/NXP/IMEC的3D IC封装研发，目标2028年实现本地化测试能力</li>
</ul>
<br><br>
<em style="opacity:0.6">来源：七帅化工、EU Chips Act</em>""",
            },
        ], cols=1)
    },
    {
        "label": "国内产业",
        "content": gen.create_card_group([
            {
                "title": "🏭 台积电加码3DIC封装投资 本土供应链受益",
                "content": """台积电积极扩建3nm及更先进工艺晶圆厂，同步扩大后段封测投资：
<br>
<ul style="margin:8px 0;padding-left:20px;">
<li>3DFabric南科封测厂/竹南AP厂下半年进入量产</li>
<li>支持TSMC-SoIC 3D堆叠+InFO/CoWoS 2.5D先进封装</li>
<li>年底将有5座3DFabric专用晶圆及封测厂投产</li>
<li>加速供应链本土化，万润、辛耘、弘塑、钛升等设备厂入围</li>
</ul>
<strong>产业趋势：</strong>HPC芯片采用InFO/CoWoS先进封装已成主流，3DIC封装延续摩尔定律，苹果/英伟达/AMD/高通等大客户全面导入。
<br><br>
<em style="opacity:0.6">来源：芯片采购网</em>""",
            },
            {
                "title": "🧊 液冷赛道加速升温 行业三季度迎订单业绩兑现期",
                "content": """液冷概念板块持续活跃，产业链从技术验证走向规模化量产：
<br>
<ul style="margin:8px 0;padding-left:20px;">
<li>TrendForce：液冷在AI芯片中渗透率持续提升，英伟达下一代Vera Rubin平台全面导入无风扇全液冷架构</li>
<li>中金预测：2026年成为液冷放量元年，全球智算中心液冷市场规模超千亿元</li>
<li>机构预计2026年液冷行业渗透率达53%，2028年市场规模攀升至3000亿元</li>
<li>一次侧扩容+二次侧升级双击驱动，三季度起订单向业绩加速兑现</li>
</ul>
<strong>持仓相关：</strong>英维克上半年营收30.17亿元同比+17.24%，Q2归母净利润环比大增1934%，机构一周净买入1.37亿元。
<br><br>
<em style="opacity:0.6">来源：证券时报·e公司</em>""",
            },
            {
                "title": "📊 A股半年报收官 铜冠铜箔净利增514%",
                "content": """铜冠铜箔2026半年报业绩亮眼，铜箔行业景气度持续回升：
<br><strong>核心财务：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>营收40.21亿元，同比+34.16%</li>
<li>归母净利润2.15亿元，同比<strong style="color:#22c55e;">+514.75%</strong></li>
<li>扣非净利润2.07亿元，同比+754.21%</li>
<li>Q2单季净利润1.09亿元，同比+259%，环比+2%</li>
</ul>
<strong>增长驱动：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>锂电铜箔板块整体回暖</li>
<li>高端PCB铜箔呈现供不应求态势</li>
<li>覆铜板行业处于高景气周期，量价齐升</li>
</ul>
<br><br>
<em style="opacity:0.6">来源：证券时报</em>""",
            },
        ], cols=1)
    },
]

news_tab_html = gen.create_tab_pane(news_tabs, tab_id="important-news", style="default")
gen.add_section("重大新闻", news_tab_html, "📰")

# === 4. 行业追踪 ===
industry_content = gen.create_card_group([
    {
        "title": "🔋 存储芯片",
        "content": "⭐ S级主线 | 美光暴涨5%HBM售罄至2027年，存储超级周期延续性超预期，三巨头产能竞赛中，国产替代加速",
        "icon": "🟢",
    },
    {
        "title": "💻 AI算力/液冷",
        "content": "⭐ S级主线 | 纳指创新高AI算力链强势，液冷渗透率加速提升，Muse智能体爆火推升存储/算力需求预期",
        "icon": "🟢",
    },
    {
        "title": "🔧 先进封装",
        "content": "⭐ A级主线 | 日本收紧封装材料出口管制加速国产替代，台积电加码3DIC投资，雅克科技/华海诚科等受益",
        "icon": "🟡",
    },
    {
        "title": "🥈 铜箔/PCB",
        "content": "⭐ A级主线 | 铜冠铜箔半年报净利增514%，高端PCB铜箔供不应求，覆铜板高景气周期延续",
        "icon": "🟢",
    },
], cols=2)

gen.add_section("行业追踪", industry_content, "🏭")

# === 5. 今日催化 ===
catalyst_content = gen.create_card_group([
    {
        "title": "⚡ 存储板块情绪催化",
        "content": "隔夜存储四巨头集体暴涨5-7%，费城半导体+2%，A股存储/HBM/半导体材料板块情绪有望提振",
        "icon": "🟢",
    },
    {
        "title": "📰 今日LPR报价",
        "content": "9月LPR报价今日公布，关注1年期和5年期利率变动，市场预期维持不变",
        "icon": "🟠",
    },
    {
        "title": "🌏 亚太市场联动",
        "content": "日经-0.9%恒指+0.18%，关注日韩半导体板块动向及外资流向",
        "icon": "🟡",
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
        "title": "存储板块高位追高风险",
        "content": "美光科技年内涨幅已超500%，FY27 EPS预期156美元对应的P/E虽仅6.8倍，但存储行业历来具有强周期性，若AI需求增速放缓或产能释放超预期，价格拐点可能导致业绩大幅回撤。A股存储板块前期涨幅较大，追高需谨慎。",
        "tag": "周期风险",
        "tag_color": "red",
    },
    {
        "title": "美元指数走强 外资流入或受扰动",
        "content": "美元指数涨0.17%报100.60，美联储加息预期下美元维持强势，人民币汇率承压，北向资金流入节奏可能受扰动，成长股估值面临一定压力。",
        "tag": "资金风险",
        "tag_color": "orange",
    },
    {
        "title": "日本出口管制短期冲击",
        "content": "日本收紧先进封装特种聚合物出口管制，虽然中长期利好国产替代，但短期可能影响国内高端封测企业的材料供应稳定性和项目进度，相关标的需警惕短期情绪波动。",
        "tag": "政策风险",
        "tag_color": "orange",
    },
    {
        "title": "成交缩量 持续性待验证",
        "content": "9月22日A股成交2.14万亿较此前缩量，沪指窄幅震荡0.06%，量能能否恢复是行情延续关键。存储板块虽有隔夜美股催化，但A股能否跟涨需观察量能配合。",
        "tag": "技术面风险",
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
    description="存储芯片超级周期再确认！美光涨5%闪迪涨6.82%，HBM售罄至2027年单季净利剑指350亿美元；纳指创历史新高；日本收紧封装材料出口管制利好国产替代",
    image="https://boya357.github.io/daily-news-insight/assets/og-daily.png"
)

# === 发布 ===
output_file = "docs/daily/20260923_每日新闻洞察.html"
result = gen.publish(output_file)
print(f"OK 报告已生成: {result}")
if result.get("success"):
    import shutil
    shutil.copy(output_file, "docs/daily/latest.html")
    print(f"LATEST 已更新 latest.html")
    print(f"SIZE 文件大小: {result.get('file_size')} 字节")
else:
    print(f"ERROR 验证失败: {result.get('errors')}")
