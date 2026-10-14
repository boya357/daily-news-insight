#!/usr/bin/env python3
"""2026-10-14 每日新闻洞察 - V3 Pro生成器"""
import sys, os
sys.path.insert(0, 'v3')
os.chdir('/root/daily-news-insight')
from generators.daily_pro import DailyReportProGenerator

gen = DailyReportProGenerator(
    date_str="2026-10-14",
    weekday="周三",
    subtitle="韩股崩盘SK海力士暴跌10%三星-7.39% | 存储芯片超级周期见顶担忧发酵 | 博通CEO警告AI投资如赌博 | 美国9月CPI今晚公布",
    data_dir='/root/daily-news-insight/data'
)

# TL;DR
gen.set_tldr([
    ("韩股崩盘SK海力士暴跌10%", "韩国KOSPI暴跌5.46%创7月新低，SK海力士-10.09%三星-7.39%，存储芯片周期见顶担忧+长鑫4F²架构突破+博通CEO警告AI投资如赌博三重利空", "red"),
    ("美股三大指数集体收跌", "道指-0.35%标普-0.02%纳指-0.15%，费城半导体-0.23%（盘中一度跌超3%），应用材料-6.69%美光-3.62%AMD+1.9%英伟达+0.97%", "red"),
    ("存储超级周期见顶担忧发酵", "长鑫存储官宣4F² DRAM架构突破年底推DDR5 RDIMM，市场担忧DRAM竞争加剧韩厂定价权承压；外资持续抛售韩股累计净卖近200万亿韩元", "red"),
    ("博通CEO警告AI投资像赌博", "博通CEO陈福阳在新加坡表示，很多AI投资者根本不知道自己在投什么，设定了极其激进的预期，就像在赌场下注", "orange"),
    ("美国9月CPI今晚公布", "北京时间20:30美国公布9月CPI数据，美联储柯林斯预计年底前进一步加息，沃勒称长端收益率上升已在抑制需求", "orange"),
    ("油价续涨布油站稳106美元", "布油+0.78%报106.51美元，WTI+0.77%报94.87美元；特朗普指责胡塞武装中期选举前蓄意推高油价", "green"),
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
                "title": "📉 韩股崩盘KOSPI跌5.46% SK海力士暴跌10%三星-7.39%",
                "content": """10月13日韩国股市遭遇血洗，半导体板块领跌触发程序化卖盘熔断：
<br><strong>收盘数据：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>韩国KOSPI <strong style="color:#ef4444;">-5.46%</strong> 报6035.35点，创7月30日以来新低</li>
<li>SK海力士 <strong style="color:#ef4444;">-10.09%</strong> 报144.3万韩元，单日市值蒸发近5800亿元</li>
<li>三星电子 <strong style="color:#ef4444;">-7.39%</strong> 报23.2万韩元，外资持股比例降至46.37%（2009年以来最低）</li>
<li>韩国交易所启动SIDECAR机制，暂停KOSPI程序化卖盘</li>
</ul>
<strong>暴跌三大原因：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li><strong>技术冲击：</strong>长鑫存储官宣4F² DRAM架构突破，年底推新一代DDR5 RDIMM，市场担忧DRAM竞争加剧</li>
<li><strong>情绪冲击：</strong>博通CEO陈福阳警告AI投资"具有赌博性质"，质疑AI投资回报可持续性</li>
<li><strong>资金冲击：</strong>外资今年KOSPI累计净卖出近200万亿韩元，存储板块前期涨幅巨大获利回吐</li>
</ul>
<strong>日股同步大跌：</strong>铠侠控股-13.28%、软银-8.5%、东京电子-7.15%、爱德万测试-2.91%。
<br><br>
<em style="opacity:0.6">来源：21世纪经济报道、中国证券报、财联社</em>""",
            },
            {
                "title": "🇺🇸 美股三大指数集体收跌 存储/设备股重挫应用材料-6.7%",
                "content": """美国时间10月13日，美股三大指数全线收跌，连续第二日下跌：
<br><strong>收盘数据：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>道琼斯 <strong style="color:#ef4444;">-0.35%</strong> 报51670.10点</li>
<li>标普500 <strong style="color:#ef4444;">-0.02%</strong> 报7805.45点</li>
<li>纳斯达克 <strong style="color:#ef4444;">-0.15%</strong> 报27204.38点</li>
<li>费城半导体 <strong style="color:#ef4444;">-0.23%</strong> 报12208.79点（盘中一度跌超3%）</li>
</ul>
<strong>科技股分化：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>Meta +2.63%（Muse代理应用订阅计划）、AMD +1.90%、英伟达 +0.97%</li>
<li>微软 +0.43%（创一年新高）、苹果 +0.09%、谷歌 +0.30%</li>
<li>亚马逊 -0.37%、特斯拉 -0.74%、SpaceX -4.21%</li>
</ul>
<strong>存储/设备股重挫：</strong>应用材料-6.69%、美光-3.62%、SK海力士-3.19%、西部数据-1.61%、科磊-3%+、科休半导体-3%+。
<br><strong>市场情绪：</strong>美联储官员释放偏鹰信号，叠加美国9月CPI今晚公布，市场情绪谨慎。
<br><br>
<em style="opacity:0.6">来源：每日经济新闻、证券时报、新浪财经</em>""",
            },
            {
                "title": "⚠️ 博通CEO陈福阳：很多AI投资者像在赌场下注",
                "content": """博通CEO陈福阳（Hock Tan）在新加坡DBS Asia Future Forward大会上发表重磅警告：
<br><strong>核心观点：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>"很多投资者根本不知道自己在投资什么"</li>
<li>"设定了极其激进的预期，结果却发现自己几乎就像是在赌场里下注"</li>
<li>AI投资交易"具有赌博性质"</li>
</ul>
<strong>市场影响：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>博通CEO的表态加剧了外界对AI领域过热的担忧</li>
<li>投资者开始质疑企业如何兑现AI盈利预期</li>
<li>存储芯片/AI基础设施板块承压明显</li>
</ul>
<strong>背景：</strong>此前英特尔CEO也警告称，资金获取能力可能成为制约AI投资热潮的一大因素。两大芯片巨头CEO连续警告AI投资风险，市场对AI支出可持续性的担忧升温。
<br><br>
<em style="opacity:0.6">来源：新浪财经、环球市场播报</em>""",
            },
            {
                "title": "💾 长鑫存储4F² DRAM架构突破 年底推DDR5 RDIMM",
                "content": """长鑫存储（CXMT）宣布重大技术突破，成为韩股存储暴跌的导火索之一：
<br><strong>技术进展：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>长鑫存储总裁曹堪宇在第四届集成芯片和芯粒大会上官宣</li>
<li>4F² DRAM架构研发取得关键进展（更小物理空间实现更大存储容量）</li>
<li>混合键合技术同步推进</li>
<li><strong>预计2026年底推出新一代DDR5 RDIMM产品</strong></li>
</ul>
<strong>市场影响：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>三星、SK海力士、美光三家合计占全球DRAM市场约90%份额</li>
<li>长鑫技术突破可能加剧行业竞争，韩厂高端存储定价权承压</li>
<li>但专家指出：技术进展能否转化为稳定供货和价格竞争仍需观察</li>
</ul>
<strong>对A股影响：</strong>国产存储产业链迎来催化，长存供应链（雅克科技/华海诚科等材料端）长期受益于国产替代逻辑。
<br><br>
<em style="opacity:0.6">来源：21世纪经济报道、中国证券报</em>""",
            },
            {
                "title": "🛢️ 油价续涨布油站稳106美元 特朗普指责胡塞推高油价",
                "content": """国际油价周二继续上涨，能源股同步走强：
<br><strong>收盘数据：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>WTI原油 <strong style="color:#22c55e;">+0.77%</strong> 报94.87美元/桶</li>
<li>布伦特原油 <strong style="color:#22c55e;">+0.78%</strong> 报106.51美元/桶</li>
<li>康菲石油 +2.42%、埃克森美孚 +1.16%、雪佛龙 +1.31%</li>
</ul>
<strong>最新动态：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>特朗普指责胡塞武装在美国中期选举前蓄意推高油价</li>
<li>美以领导人被曝商讨重启对伊朗军事行动</li>
<li>中东地缘风险持续升温支撑油价</li>
</ul>
<strong>贵金属：</strong>COMEX黄金+0.21%报4186.08美元，COMEX白银-0.27%报59.37美元。
<br><br>
<em style="opacity:0.6">来源：每日经济新闻、东方财富</em>""",
            },
            {
                "title": "📊 美国9月CPI今晚公布 美联储官员释放偏鹰信号",
                "content": """北京时间10月14日20:30，美国劳工部将公布9月CPI数据：
<br><strong>美联储最新表态：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li><strong>柯林斯：</strong>预计美联储将在年底前"进一步"上调利率，新一年政策路径取决于数据</li>
<li><strong>沃勒：</strong>长端美债收益率上升正在抑制利率敏感领域需求，AI短期推升通胀但预期仍锚定良好</li>
<li>克利夫兰联储主席哈马克：宁可小幅度高频调整，也不要犹豫后冒更大纠偏风险</li>
</ul>
<strong>市场关注：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>10年期美债收益率维持高位压制科技股估值</li>
<li>CPI数据将直接影响11月/12月加息预期</li>
<li>数据中心建设正在对通胀数据施加压力</li>
</ul>
<strong>A股影响：</strong>CPI若超预期可能引发美债收益率进一步上行，外资流出压力加大，科技成长股承压。
<br><br>
<em style="opacity:0.6">来源：大河财立方、证券时报</em>""",
            },
        ], cols=1)
    },
    {
        "label": "国内要闻",
        "content": gen.create_card_group([
            {
                "title": "📈 中国前三季度进出口数据公布 贸易韧性延续",
                "content": """10月14日国新办举行新闻发布会，海关总署介绍2026年前三季度进出口情况。
<br>（数据详见发布会正式披露，盘前以官方发布为准）
<br><br>
<em style="opacity:0.6">来源：央广网</em>""",
            },
            {
                "title": "💻 微导纳米拟定增募资49.44亿元扩产半导体设备",
                "content": """微导纳米(688147)公告拟定增募资不超过49.44亿元：
<ul style="margin:8px 0;padding-left:20px;">
<li>无锡先进半导体设备产业化升级迭代项目</li>
<li>华中先进半导体设备产业化项目</li>
<li>尖端薄膜沉积技术研发中心项目</li>
<li>补充流动资金</li>
</ul>
半导体设备国产替代持续推进，设备厂商加速扩产。
<br><br>
<em style="opacity:0.6">来源：央广网、公司公告</em>""",
            },
            {
                "title": "📊 三季报业绩预告密集披露 最高预增超1500%",
                "content": """A股三季报业绩预告进入密集披露期，多公司业绩亮眼：
<ul style="margin:8px 0;padding-left:20px;">
<li><strong>富春染织：</strong>前三季度归母净利润同比预增1347.69%—1519.01%</li>
<li><strong>恩捷股份：</strong>前三季度归母净利润15.4—20.5亿元，同比扭亏为盈（锂电池隔膜龙头）</li>
<li>德业股份10派16元、丽珠集团10派10.2元今日实施分红</li>
</ul>
<br>
<em style="opacity:0.6">来源：中国证券报</em>""",
            },
            {
                "title": "🎤 歌尔股份终止分拆歌尔微至港交所上市",
                "content": """歌尔股份(002241)公告终止分拆歌尔微至香港联交所主板上市。
<br>具体原因以公司公告为准，关注对歌尔股份及声学产业链情绪影响。
<br><br>
<em style="opacity:0.6">来源：公司公告</em>""",
            },
            {
                "title": "⚠️ 茶百道港股IPO被暂停 香港证监会指可能被操纵",
                "content": """香港证监会10月13日公告，指示联交所暂停茶百道(02555)股份交易：
<ul style="margin:8px 0;padding-left:20px;">
<li>茶百道首次公开招股可能曾被人为操纵</li>
<li>调查期间暂停股份交易</li>
<li>新消费/茶饮板块情绪或受影响</li>
</ul>
<br>
<em style="opacity:0.6">来源：香港证监会、央广网</em>""",
            },
        ], cols=1)
    },
]

news_tab_html = gen.create_tab_pane(news_tabs, tab_id="important-news", style="default")
gen.add_section("重大新闻", news_tab_html, "📰")

# === 4. 行业追踪 ===
industry_content = gen.create_card_group([
    {"title": "🔋 存储芯片/HBM", "content": "⚠️ S级主线 | SK海力士暴跌10%三星-7.39%美光-3.62%，存储超级周期见顶担忧+长鑫4F²突破+博通CEO警告三重利空。但长鑫突破利好国产替代，材料端（雅克/华海诚科）长期逻辑不变，短期情绪承压", "icon": "🔴"},
    {"title": "💻 AI算力/液冷", "content": "⭐ S级主线 | 英伟达+0.97%AMD+1.9%微软创一年新高，AI算力龙头相对抗跌；但博通CEO警告AI投资如赌博，市场对AI支出可持续性存疑，短期情绪压制", "icon": "🟡"},
    {"title": "🔧 半导体设备/材料", "content": "⭐ A级主线 | 应用材料-6.69%设备股领跌，长鑫技术突破国产替代加速，微导纳米定增49亿扩产。短期外围压力大，中期国产替代逻辑强化", "icon": "🟡"},
    {"title": "🤖 人形机器人/智能制造", "content": "⭐ A级主线 | 工博会余热，新质生产力政策支持；外围科技股大跌拖累情绪，板块分化，关注有业绩支撑的标的", "icon": "🟠"},
    {"title": "🛢️ 油气/能源", "content": "B级主线 | 布油站稳106美元续涨，中东地缘风险升温，特朗普指责胡塞推高油价，能源股逆势走强，关注油气开采、油服板块", "icon": "🟢"},
    {"title": "🏦 券商/金融", "content": "B级主线 | 中金合并东兴/信达落地，金融街论坛19日召开吴清演讲，金融板块有催化但需关注大盘整体情绪", "icon": "🟡"},
], cols=2)
gen.add_section("行业追踪", industry_content, "🏭")

# === 5. 今日催化 ===
catalyst_content = gen.create_card_group([
    {"title": "📉 韩股存储崩盘 A股半导体承压", "content": "SK海力士-10%三星-7.39%美光-3.62%，存储超级周期见顶担忧发酵，A股半导体/存储板块开盘或大幅低开，注意风险控制", "icon": "🔴"},
    {"title": "🇨🇳 长鑫存储技术突破 国产替代催化", "content": "长鑫官宣4F² DRAM架构突破年底推DDR5 RDIMM，国产存储产业链长期受益，材料/设备端国产替代逻辑强化，关注长存供应链", "icon": "🟢"},
    {"title": "🛢️ 油价续涨 能源板块逆势催化", "content": "布油+0.78%站稳106美元，中东地缘风险升温，能源/油服/油气开采板块或逆势走强", "icon": "🟢"},
    {"title": "📊 美国CPI今晚公布 全球聚焦", "content": "北京时间20:30美国9月CPI，美联储官员释放偏鹰信号，CPI超预期可能引发全球市场波动", "icon": "🟠"},
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
    {"title": "存储芯片周期见顶风险", "content": "SK海力士暴跌10%三星-7.39%美光-3.62%，韩股连续五日下跌，外资持续抛售。市场担忧存储超级周期见顶，Q4涨价逻辑可能生变。A股存储板块前期涨幅巨大，回调风险需高度警惕。", "tag": "周期见顶", "tag_color": "red"},
    {"title": "AI投资泡沫化担忧", "content": "博通CEO陈福阳警告AI投资如赌博，英特尔CEO也警告资金约束。两大芯片巨头连续发声，AI投资回报可持续性遭质疑。AI算力/光模块/存储等前期高位板块估值承压。", "tag": "估值风险", "tag_color": "red"},
    {"title": "美国CPI+加息预期双重压制", "content": "今晚美国9月CPI公布，美联储柯林斯预计年底前进一步加息。10年期美债收益率高位运行，外资流出压力下科技成长股估值承压。", "tag": "利率风险", "tag_color": "orange"},
    {"title": "持仓4只标的连续回调", "content": "英维克/铜冠铜箔/雅克科技连续多日回调，外围半导体暴跌雪上加霜。需严格执行止损纪律，关注开盘后承接力度，避免被动深套。", "tag": "持仓风险", "tag_color": "red"},
    {"title": "长鑫技术突破冲击韩厂定价权", "content": "长鑫4F² DRAM架构突破年底推DDR5 RDIMM，国产存储崛起可能压缩韩厂溢价空间。短期对全球存储价格预期形成压制，但长期利好国产替代。", "tag": "竞争风险", "tag_color": "orange"},
    {"title": "中东地缘风险升级", "content": "美以商讨对伊朗军事行动，特朗普指责胡塞推高油价，中东地缘风险持续升温。油价上涨推升通胀预期，进一步压制科技股估值。", "tag": "地缘风险", "tag_color": "orange"},
], cols=2)
gen.add_section("空方视角", bear_content, "⚠️")

# === 13. 教训库 ===
lessons_html = gen.build_lessons_section()
gen.add_section("历史教训", lessons_html, "📚")

# === 14. 每日总结 ===
gen.add_daily_summary()

# OG
gen.set_og(
    description="韩股崩盘SK海力士暴跌10%三星-7.39%，存储超级周期见顶担忧+长鑫4F²突破+博通CEO警告三重利空；美股三大指数收跌应用材料-6.7%；美国9月CPI今晚公布；油价续涨布油站稳106美元",
    image="https://boya357.github.io/daily-news-insight/assets/og-daily.png"
)

# === 发布 ===
output_file = "docs/daily/20261014_每日新闻洞察.html"
result = gen.publish(output_file)
print(f"OK 报告已生成: {result}")
if result.get("success"):
    import shutil
    shutil.copy(output_file, "docs/daily/latest.html")
    print(f"LATEST 已更新 latest.html")
    print(f"SIZE 文件大小: {result.get('file_size')} 字节")
else:
    print(f"ERROR 验证失败: {result.get('errors')}")
