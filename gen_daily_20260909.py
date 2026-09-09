#!/usr/bin/env python3
"""2026-09-09 每日新闻洞察 - V3 Pro生成器"""
import sys, os
sys.path.insert(0, 'v3')
os.chdir('/root/daily-news-insight')
from generators.daily_pro import DailyReportProGenerator

gen = DailyReportProGenerator(
    date_str="2026-09-09",
    weekday="周三",
    subtitle="AI硬件逆势起飞 | 高通亚马逊600亿芯片大单 | 布伦特逼近百元关口",
    data_dir='/root/daily-news-insight/data'
)

# TL;DR
gen.set_tldr([
    ("AI硬件逆势分化爆发", "道指大跌1.18%但费半涨1.3%，英特尔+9%CPU再涨价，高通拿下亚马逊600亿AI芯片订单，光通信板块集体大涨", "green"),
    ("布伦特原油逼近百元", "中东局势持续升级，伊朗警告霍尔木兹海峡油轮，布伦特99.52美元WTI 94.63美元，通胀预期回升", "red"),
    ("9月8日A股跷跷板行情", "沪指涨0.2%创业板跌1.15%，成交1.98万亿，石油石化+3.68%领涨，电子-1.12%领跌，高低切换明显", "orange"),
    ("存储超级周期延续", "三星4nm产线超50%用于HBM4基础裸片，SK海力士1c nm工艺2027年初成第一大DRAM工艺", "green"),
    ("今日CPI/PPI数据公布", "8月CPI预期回升至0.9%，PPI前值3.5%，通胀数据决定货币政策空间，进出口数据同日公布", "orange"),
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
                "title": "🤖 高通拿下亚马逊600亿美元AI芯片大单 定制ASIC赛道再扩容",
                "content": """高通宣布与亚马逊达成数据中心芯片长期合作协议，横跨多代产品，共同开发AWS AI基础设施定制芯片：
<br>
<ul style="margin:8px 0;padding-left:20px;">
<li>未来十年订单金额最高可达<strong>600亿美元</strong></li>
<li>亚马逊获认股权证，可每股161.26美元购买最多2500万股高通股票（价值约40亿美元）</li>
<li>继博通(谷歌)、Marvell(Meta)之后，定制ASIC赛道又一重量级绑定</li>
<li>高通股价涨3.18%，AI算力第二增长曲线从GPU独大转向GPU+ASIC双轨</li>
</ul>
<strong>产业链含义：</strong>云厂商自研定制芯片进入新阶段，AI算力硬件多元化趋势明确
<br><br>
<em style="opacity:0.6">来源：高通公告、财联社、澎湃新闻</em>""",
            },
            {
                "title": "💻 英特尔CPU再涨价10% 股价暴涨超9%创年内最大涨幅",
                "content": """英特尔计划10月5日再次上调PC处理器价格约10%，为今年第三轮涨价，策略重心从抢份额转向保利润：
<br>
<ul style="margin:8px 0;padding-left:20px;">
<li>英特尔收涨<strong style="color:#22c55e;">9.05%</strong>报104.47美元，盘中最高106.09美元</li>
<li>今年以来已多次涨价，从消费者级到服务器级全面提价</li>
<li>同时计划裁减5%-10%员工，聚焦数据中心与AI等高利润业务</li>
<li>北陆资本上调评级至"跑赢大盘"，目标价120美元</li>
<li>存储涨价之后逻辑芯片也开始按利润定价，供给端确实紧</li>
</ul>
<strong>对A股映射：</strong>半导体设备/材料板块受益，国产替代逻辑强化
<br><br>
<em style="opacity:0.6">来源：DIGITIMES、澎湃新闻、CityTimes</em>""",
            },
            {
                "title": "🔆 光通信板块集体爆发 康宁拿下Verizon八年光纤大单",
                "content": """AI数据中心互联需求爆发，光通信成为隔夜美股最强板块：
<br>
<ul style="margin:8px 0;padding-left:20px;">
<li>Lumentum <strong style="color:#22c55e;">+11.04%</strong>，Coherent <strong style="color:#22c55e;">+7.10%</strong></li>
<li>康宁 <strong style="color:#22c55e;">+9%+</strong>，签下Verizon 2027-2032年超8000万英里高密度光纤协议</li>
<li>迈威尔科技+0.83%，Ciena涨超2%</li>
<li>这批光纤将成为AI数据中心网络骨干，连接美国主要长途通信走廊</li>
</ul>
<strong>对A股映射：</strong>光模块、光纤光缆、CPO方向映射强度较高
<br><br>
<em style="opacity:0.6">来源：第一财经、九百日记、澎湃新闻</em>""",
            },
            {
                "title": "🛡️ 中东局势急剧升级 伊朗警告霍尔木兹海峡油轮",
                "content": """美伊冲突持续升级，霍尔木兹海峡航运风险加剧：
<br>
<ul style="margin:8px 0;padding-left:20px;">
<li>伊朗革命卫队警告停泊在科威特和巴林港口的油轮船员立即离开</li>
<li>美军9月8日打击伊朗哈尔克岛和贾斯克附近目标</li>
<li>伊朗称在霍尔木兹海峡捕获一艘美军最先进智能无人潜艇</li>
<li>美国财政部宣布对伊朗新一轮制裁，涉及36个对象</li>
<li>WTI原油<strong style="color:#ef4444;">94.63美元</strong>(+1.72%)，布伦特<strong style="color:#ef4444;">99.52美元</strong>(+1.63%)逼近百元</li>
</ul>
<strong>市场影响：</strong>高油价推升通胀预期，制约美联储政策空间，A股油气板块受益
<br><br>
<em style="opacity:0.6">来源：央视新闻、澎湃新闻、汇通网</em>""",
            },
        ], cols=1)
    },
    {
        "label": "国内政策",
        "content": gen.create_card_group([
            {
                "title": "📊 今日重磅数据：8月CPI/PPI+进出口",
                "content": """9月9日将公布多项关键经济数据，市场高度关注：
<br>
<ul style="margin:8px 0;padding-left:20px;">
<li><strong>8月CPI同比：</strong>预期回升至0.9%左右，前值0.5%</li>
<li><strong>8月PPI同比：</strong>前值3.5%，油价上涨或推升工业品价格</li>
<li><strong>8月进出口数据：</strong>验证外需景气度，北向资金动向受关注</li>
<li>锂电池出口增长34.4%、汽车+47.1%、船舶+29.8%（按近期趋势）</li>
<li>高附加值产品继续扛起出口大梁</li>
</ul>
<strong>市场影响：</strong>CPI回升确认消费复苏，PPI维持高位验证工业品景气，数据超预期将提振市场情绪
<br><br>
<em style="opacity:0.6">来源：海关总署、国家统计局、第一财经</em>""",
            },
            {
                "title": "🏛️ 央行维稳信号明确 流动性合理充裕",
                "content": """央行高层会议释放明确维稳信号，打消市场对流动性收紧的担忧：
<br>
<ul style="margin:8px 0;padding-left:20px;">
<li>持续实施稳健灵活的货币政策，保持流动性合理充裕</li>
<li>精准降低社会综合融资成本，畅通货币政策传导机制</li>
<li>坚决维护金融市场平稳运行，防范大幅波动风险</li>
<li>财政部续发50年期超长期特别国债，竞争性招标350亿元</li>
<li>人民币跨境支付系统与11家外资机构签约</li>
</ul>
<strong>市场影响：</strong>"金融托底+产业赋能"双重利好格局，为A股提供资金与政策支撑
<br><br>
<em style="opacity:0.6">来源：央行、财联社、东方财富</em>""",
            },
            {
                "title": "🏥 七部门推进灵活就业人员医保提质 三年专项行动启动",
                "content": """国家医保局等七部门发布通知，开展灵活就业人员参加基本医保提质专项行动：
<br>
<ul style="margin:8px 0;padding-left:20px;">
<li>用3年左右时间提高灵活就业人员等参加基本医保人数</li>
<li>特别是参加职工医保人数，探索新就业形态参保缴费模式</li>
<li>国家卫健委印发眼健康服务工作方案(2026-2030年)</li>
<li>到2030年全国百万人口白内障手术率超4000，95%以上县域可独立开展常见眼病诊疗</li>
<li>"人工智能+数字三品"专项行动启动，打开创新药行业成长空间</li>
</ul>
<em style="opacity:0.6">来源：国家医保局、卫健委、第一财经</em>""",
            },
            {
                "title": "🎪 服贸会+外滩大会今日开幕 数字经济与AI成焦点",
                "content": """两大重量级展会今日同步开幕，数字经济与AI科技成为核心议题：
<br>
<ul style="margin:8px 0;padding-left:20px;">
<li><strong>2026中国国际服务贸易交易会</strong>（北京，9/9-9/13）</li>
<li><strong>2026 Inclusion·外滩大会</strong>（上海，9/9-9/12）</li>
<li>聚焦数字贸易、AI应用、绿色金融等前沿领域</li>
<li>DeepSeek V4.1 Flash开启中间版本内测</li>
<li>小鹏人形机器人首台下线，2026年底规模量产、2027年交付</li>
</ul>
<em style="opacity:0.6">来源：第一财经、东方财富</em>""",
            },
        ], cols=1)
    },
    {
        "label": "存储芯片",
        "content": gen.create_card_group([
            {
                "title": "💾 三星4nm产线超50%用于HBM4基础裸片 产能全速运转",
                "content": """受AI算力驱动HBM需求持续远超供给影响，三星大规模倾斜产能：
<br>
<ul style="margin:8px 0;padding-left:20px;">
<li>三星4nm制程<strong>超过50%-60%产能</strong>分配给HBM4基础裸片生产</li>
<li>对应月产能约1.5万片晶圆，集中在平泽S5、S6产线</li>
<li>HBM4量产四个月收入已突破10亿美元</li>
<li>HBM4良品率从不到60%提升至接近80%，提前达成年末目标</li>
<li>三星正评估2nm工艺用于HBM基础裸片，定向供应英伟达新一代芯片</li>
</ul>
<strong>技术趋势：</strong>HBM基础裸片从DRAM工艺转向逻辑工艺，三星凭自有代工形成差异化竞争力
<br><br>
<em style="opacity:0.6">来源：Wccftech、ZDNet Korea、超能网、环球网</em>""",
            },
            {
                "title": "📈 SK海力士1c nm工艺2027年初成第一大DRAM制程",
                "content": """韩媒ChosunBiz报道，SK海力士第6代DRAM工艺加速扩产：
<br>
<ul style="margin:8px 0;padding-left:20px;">
<li>1c nm产能占比从2026Q1的10%逐季提升至2027Q1的35%</li>
<li>2027年初1c nm(35%)将超越1b nm(33%)成为第一大制程</li>
<li>HBM4E将升级到1c nm DRAM Die，为HBM升级做平滑过渡</li>
<li>三星与美光第6代DRAM产能占比约16%和19%（2026Q2末）</li>
<li>三星SK海力士库存已降至不足10天，KB证券预警历史性短缺</li>
</ul>
<em style="opacity:0.6">来源：ChosunBiz、IT之家、新浪科技、券商中国</em>""",
            },
            {
                "title": "🏭 存储超级周期确认 2027年存储占AI基建57%",
                "content": """KB Securities最新报告验证存储超级周期逻辑：
<br>
<ul style="margin:8px 0;padding-left:20px;">
<li>2027年全球超大规模数据中心AI基建投资达<strong>1.3万亿美元</strong>，同比+60%</li>
<li>存储在AI基建中占比从2025年14%升至2027年<strong>57%</strong>，两年翻四倍</li>
<li>TrendForce预计占比可能高达68%</li>
<li>HBM4晶圆产能约为通用DRAM的三倍，挤占传统DRAM产能</li>
<li>2027年DRAM+NAND比特需求将超供给逾10个百分点</li>
</ul>
<strong>对A股影响：</strong>存储产业链（HBM材料、存储封测、铜箔/PCB）持续受益
<br><br>
<em style="opacity:0.6">来源：KB Securities、券商中国、证券时报</em>""",
            },
        ], cols=1)
    },
    {
        "label": "地缘大宗",
        "content": gen.create_card_group([
            {
                "title": "🛢️ 布伦特逼近100美元关口 通胀预期回升",
                "content": """中东局势升级+OPEC+减产推动油价持续走高：
<br>
<ul style="margin:8px 0;padding-left:20px;">
<li>布伦特原油<strong style="color:#ef4444;">99.52美元/桶</strong>（+1.63%），逼近100美元关口</li>
<li>WTI原油<strong style="color:#ef4444;">94.63美元/桶</strong>（+1.72%）</li>
<li>伊朗警告霍尔木兹海峡航运风险，地缘溢价持续上升</li>
<li>美国8月PPI预期从4.7%加速至5.4%，CPI预期3.3%</li>
<li>高油价推升全球通胀预期，可能强化美联储加息逻辑</li>
</ul>
<strong>对A股影响：</strong>油气开采/油服板块受益，但输入性通胀制约货币政策空间
<br><br>
<em style="opacity:0.6">来源：澎湃新闻、汇通网、Wind</em>""",
            },
            {
                "title": "🥇 黄金跌破4400美元 加息预期压制无息资产",
                "content": """加息预期升温叠加美元走强，黄金短期承压：
<br>
<ul style="margin:8px 0;padding-left:20px;">
<li>COMEX黄金<strong>4387.72美元</strong>（-1.16%），盘中跌破4400关口</li>
<li>现货黄金收报4355美元/盎司，跌1.15%</li>
<li>CME FedWatch 9月加息概率约60%，市场等待周五CPI数据</li>
<li>中国央行连续22个月增持黄金的长期逻辑不变</li>
<li>地缘风险提供底部支撑，但短期受利率因素主导</li>
</ul>
<em style="opacity:0.6">来源：Wind、澎湃新闻、国家外汇管理局</em>""",
            },
            {
                "title": "🇯🇵 日本央行9月加息概率上升 日元创7个月新高",
                "content": """日本7月名义工资创近30年最大升幅，强化加息预期：
<br>
<ul style="margin:8px 0;padding-left:20px;">
<li>日本7月名义工资同比+4.7%，创1997年以来最大升幅</li>
<li>市场已完全计价日本央行9月17-18日加息25bp</li>
<li>日元一度涨至1美元兑153.80日元，刷新近7个月新高</li>
<li>日经225指数跌0.90%，韩国KOSPI因半导体支撑表现相对坚挺</li>
<li>日本货币政策正常化或对全球资本流动产生溢出效应</li>
</ul>
<em style="opacity:0.6">来源：券商中国、彭博、凤凰网</em>""",
            },
        ], cols=1)
    },
]

news_tab_html = gen.create_tab_pane(news_tabs, tab_id="important-news", style="default")
gen.add_section("重大事件", news_tab_html, "📰")

# === 4. 板块观察 ===
gen.add_sector_analysis()

# === 5. 今日催化 ===
catalyst_content = gen.create_card_group([
    {
        "title": "📡 光通信爆发映射",
        "content": "隔夜美股光通信大涨，Lumentum+11%/康宁+9%，Verizon八年光纤大单验证AI数据中心互联需求",
        "icon": "🟢",
    },
    {
        "title": "💾 存储超级周期",
        "content": "三星4nm产线50%+用于HBM4，SK海力士1c nm加速扩产，库存不足10天，供需缺口扩大",
        "icon": "🟢",
    },
    {
        "title": "🛢️ 油价逼近百元",
        "content": "中东局势升级+OPEC+减产，布伦特逼近100美元，油气开采/油服板块催化",
        "icon": "🟢",
    },
    {
        "title": "📊 CPI/PPI数据",
        "content": "今日公布8月CPI/PPI+进出口数据，通胀与外需景气度验证，影响货币政策预期",
        "icon": "🟠",
    },
    {
        "title": "❄️ 液冷产业验证",
        "content": "液冷订单排到年底、产线两班倒，CDU最紧张，英维克谷歌CDU订单，液冷从可选变必选",
        "icon": "🟢",
    },
    {
        "title": "🤖 人形机器人",
        "content": "小鹏首台人形机器人自主下线，2026年底规模量产，机器人产业链催化",
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
        "title": "油价破百 通胀压力回升",
        "content": "布伦特逼近100美元，中东局势持续升级，高油价推升全球通胀预期，PPI可能加速至5.4%，美联储加息概率升至60%，国内货币政策空间受限。",
        "tag": "通胀风险",
        "tag_color": "red",
    },
    {
        "title": "科技股高低切换 获利了结压力",
        "content": "9月8日A股呈现明显跷跷板效应，电子板块主力净流出76亿元，科技股高位获利了结压力大，存量资金从成长转向周期防御，短期调整可能延续。",
        "tag": "资金风险",
        "tag_color": "red",
    },
    {
        "title": "英伟达回调 GPU链情绪受扰",
        "content": "英伟达隔夜跌2.01%，美光跌1.61%，定制ASIC崛起（高通亚马逊600亿大单）可能分流GPU需求，市场担忧AI算力格局生变。",
        "tag": "产业风险",
        "tag_color": "orange",
    },
    {
        "title": "成交仍在2万亿下方 增量资金不足",
        "content": "9月8日成交1.98万亿虽微放量但仍未破2万亿，市场处于存量博弈状态，缺乏增量资金进场，难以支撑全面上涨，结构性轮动将加剧。",
        "tag": "流动性风险",
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
    description="AI硬件逆势爆发！高通亚马逊600亿AI芯片大单，英特尔CPU再涨价涨超9%，光通信板块集体大涨；布伦特原油逼近百元，中东局势升级；9月8日A股跷跷板行情，石油石化领涨电子领跌",
    image="https://boya357.github.io/daily-news-insight/assets/og-daily.png"
)

# === 发布 ===
output_file = "docs/daily/20260909_每日新闻洞察.html"
result = gen.publish(output_file)
print(f"OK 报告已生成: {result}")
if result.get("success"):
    import shutil
    shutil.copy(output_file, "docs/daily/latest.html")
    print(f"LATEST 已更新 latest.html")
    print(f"SIZE 文件大小: {result.get('file_size')} 字节")
else:
    print(f"ERROR 验证失败: {result.get('errors')}")
