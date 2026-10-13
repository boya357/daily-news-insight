#!/usr/bin/env python3
"""2026-10-13 每日新闻洞察 - V3 Pro生成器"""
import sys, os
sys.path.insert(0, 'v3')
os.chdir('/root/daily-news-insight')
from generators.daily_pro import DailyReportProGenerator

gen = DailyReportProGenerator(
    date_str="2026-10-13",
    weekday="周二",
    subtitle="美股半导体普跌费城指数-2.67% | 微软Maia 300登场市值重回4万亿 | 中金换股合并东兴/信达两券商",
    data_dir='/root/daily-news-insight/data'
)

# TL;DR
gen.set_tldr([
    ("美股分化 半导体重挫2.67%", "道指+0.38%标普-0.06%纳指-0.44%，费城半导体指数跌2.67%，美光-3.88%英伟达-1.29%AMD-2.28%，存储/光通信板块全线走低", "red"),
    ("微软Maia 300 AI芯片登场", "微软发布新一代自研AI芯片Maia 300，2027年起数吉瓦规模部署，每兆瓦Token产出提升40%，市值重回4万亿美元上方", "green"),
    ("中金合并东兴/信达证券落地", "中金公司拟换股吸收合并东兴证券、信达证券，两券商10月19日终止上市，证券业航母级整合再进一步", "orange"),
    ("原油大涨1.4% 金价收跌", "布油+1.34%报106.12美元，WTI+1.43%报93.16美元，沙特输油管道扩至1000万桶/日；COMEX黄金-0.48%", "orange"),
    ("日经225跌超2% 亚太承压", "日经225指数13日早盘跌幅扩大至超2%，韩股三星-4.39%SK海力士-4.52%，亚太市场跟随美股科技股回调", "red"),
])

# === 1. 隔夜全球市场 ===
gen.add_global_market()

# === 2. 市场总览 ===
gen.add_market_overview()

print("DEBUG: tabs start")
# === 3. 重大新闻 - tab切换 ===
news_tabs = [
    {
        "label": "海外市场",
        "content": gen.create_card_group([
            {
                "title": "📉 美股三大指数分化 半导体重挫费城指数跌2.67%",
                "content": """美国时间10月12日，美股三大指数收盘涨跌不一，科技股内部明显分化：
<br><strong>收盘数据：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>道琼斯 <strong style="color:#22c55e;">+0.38%</strong> 报51850.55点（+195点）</li>
<li>标普500 <strong style="color:#ef4444;">-0.06%</strong> 报7807.24点</li>
<li>纳斯达克 <strong style="color:#ef4444;">-0.44%</strong> 报27245.90点</li>
<li>费城半导体 <strong style="color:#ef4444;">-2.67%</strong> 报12236.79点</li>
</ul>
<strong>大型科技股：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>Meta +3.38%、苹果 +1.29%、微软 +1.14%</li>
<li>谷歌-A +0.30%、亚马逊 -1.11%、特斯拉 -1.22%</li>
<li>英伟达 -1.29%、博通 -1.88%、AMD -2.28%</li>
</ul>
<strong>半导体板块重挫：</strong>美光-3.88%、闪迪-5.97%、SK海力士-4.02%、西部数据-2.60%、希捷-3.80%、超微电脑-4.48%、英特尔-3.20%。
<br><strong>市场情绪：</strong>Q3财报季本周开启，银行股先行披露。中东地缘风险叠加CPI数据临近，市场情绪谨慎。
<br><br>
<em style="opacity:0.6">来源：东方财富、证券时报、MarketBeat</em>""",
            },
            {
                "title": "🤖 微软发布Maia 300 AI芯片 市值重返4万亿美元",
                "content": """微软正式公布新一代自研AI芯片Maia 300及后续部署计划，股价收涨1.14%，市值重回4万亿美元上方：
<br><strong>核心参数：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>面向<strong>长上下文推理、低延迟对话、多步骤智能体</strong>任务设计</li>
<li>每兆瓦功率对应的Token产出较领先GPU系统<strong>提高40%</strong></li>
<li>2027年起Azure Maia系列扩展至<strong>数吉瓦规模</strong>部署</li>
<li>将成为微软产品和服务的主要AI推理系统</li>
</ul>
<strong>部署进度：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>Maia 200已用于Microsoft Copilot生产工作负载</li>
<li>GitHub Copilot及Microsoft Foundry预计2026年底前跟进</li>
<li>Maia 300将大幅降低AI服务运行成本</li>
</ul>
<strong>战略意义：</strong>微软自研芯片持续加码，对英伟达GPU依赖度降低，AI算力格局面临重塑。国内液冷/服务器产业链需关注微软自研芯片对供应链的影响。
<br><br>
<em style="opacity:0.6">来源：中国证券报、微软博客</em>""",
            },
            {
                "title": "🛢️ 国际油价涨超1% 沙特输油管道扩至1000万桶/日",
                "content": """国际油价周一大涨，能源股同步走强：
<br><strong>收盘数据：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>WTI原油 <strong style="color:#22c55e;">+1.43%</strong> 报93.16美元/桶</li>
<li>布伦特原油 <strong style="color:#22c55e;">+1.34%</strong> 报106.12美元/桶</li>
<li>标普500能源指数 <strong style="color:#22c55e;">+1.48%</strong></li>
<li>康菲石油 +2.58%、埃克森美孚 +1.89%、雪佛龙 +1.43%</li>
</ul>
<strong>沙特最新表态：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>沙特能源部长：输油管道扩建计划有望将输油能力提升至<strong>1000万桶/日</strong></li>
<li>沙特天然气管道切换可能在7至8周内完成</li>
<li>产能扩张信号明确，原油供应端格局生变</li>
</ul>
<strong>贵金属：</strong>伦敦金现-0.54%，COMEX黄金-0.48%；伦敦银现-0.84%，COMEX白银-0.78%。
<br><br>
<em style="opacity:0.6">来源：东方财富、新浪财经</em>""",
            },
            {
                "title": "🇯🇵 日经225跌超2% 韩股半导体大跌",
                "content": """亚太市场13日早盘承压，跟随美股科技股回调：
<br><strong>日本市场：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>日经225指数跌幅扩大至<strong>超2%</strong></li>
<li>科技股领跌，半导体板块跟随美股回调</li>
</ul>
<strong>韩国市场：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>三星电子 <strong style="color:#ef4444;">-4.39%</strong> 报250500韩元</li>
<li>SK海力士 <strong style="color:#ef4444;">-4.52%</strong> 报1605000韩元</li>
<li>三星SDI -1.41%、LG新能源 -0.75%</li>
<li>SK Innovation -5.03%</li>
</ul>
<strong>A股影响：</strong>亚太科技股集体回调，A股半导体、存储板块开盘或承压。关注北向资金流向及板块承接力度，短期不宜追高。
<br><br>
<em style="opacity:0.6">来源：财联社、全球市场数据</em>""",
            },
        ], cols=1)
    },
]

print("DEBUG: tab 1 done")
print("DEBUG: tabs creation done, adding section...")
news_tab_html = gen.create_tab_pane(news_tabs, tab_id="important-news", style="default")
gen.add_section("重大新闻", news_tab_html, "📰")
print("DEBUG: section added")

# === 4. 行业追踪 ===
industry_content = gen.create_card_group([
    {"title": "🔋 存储芯片", "content": "⭐ S级主线 | 美光创纪录业绩后隔夜回调3.88%，闪迪-5.97%SK海力士-4.52%，短期获利回吐但超级周期基本面未变，Q4涨价逻辑延续，回调是布局机会", "icon": "🟡"},
    {"title": "💻 AI算力/液冷", "content": "⭐ S级主线 | 微软Maia 300 AI芯片发布2027年数吉瓦部署，液冷需求同步增长；英伟达洽谈收购Reflection AI；ASML零部件涨价10%传导", "icon": "🟡"},
    {"title": "🔧 半导体设备/材料", "content": "⭐ A级主线 | ASML涨价10%倒逼国产替代，设备零部件本土化加速；雅克科技/华海诚科等半导体材料受益；费城半导体隔夜-2.67%短期承压", "icon": "🟡"},
    {"title": "🤖 人形机器人/智能制造", "content": "⭐ A级主线 | 工博会持续举办中，人形机器人成焦点；新质生产力意见支持智能制造；短期科技股整体回调，主题性机会分化", "icon": "🟠"},
    {"title": "⚡ 储能/逆变器", "content": "B级主线 | 中欧贸易磋商积极进展，储能/逆变器板块逆势领涨，首航新能、金冠电气20cm涨停；新能源汽车出口退税率下调需关注", "icon": "🟡"},
    {"title": "🌾 农业/水利", "content": "B级主线 | 超强厄尔尼诺事件正式形成或为史上最强；上周五农业板块冲高回落巨量分歧，追高谨慎，关注回调后布局机会", "icon": "🟠"},
], cols=2)
gen.add_section("行业追踪", industry_content, "🏭")

# === 5. 今日催化 ===
catalyst_content = gen.create_card_group([
    {"title": "📉 美股半导体回调压制开盘情绪", "content": "费城半导体指数-2.67%，美光-3.88%英伟达-1.29%，日经225早盘跌超2%，A股科技板块开盘或承压，关注承接力度", "icon": "🔴"},
    {"title": "💎 券商合并催化金融板块", "content": "中金换股合并东兴/信达证券落地，航母级券商整合加速，金融街论坛19日召开吴清将演讲，券商/金融板块或有催化", "icon": "🟢"},
    {"title": "🛢️ 油价上涨利好能源板块", "content": "布油+1.34%报106.12美元创近期新高，沙特输油管道扩至1000万桶/日，油气/能源板块或逆势走强", "icon": "🟢"},
], cols=3)
gen.add_section("今日催化", catalyst_content, "⚡")

print("DEBUG: basics done, adding dynamic sections...")

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
    {"title": "半导体板块技术性回调风险", "content": "费城半导体指数跌2.67%，美光闪迪SK海力士集体大跌，存储板块前期涨幅巨大。A股半导体/存储板块开盘或承压，短期获利回吐压力下不宜盲目抄底，需等待企稳信号。", "tag": "回调风险", "tag_color": "red"},
    {"title": "日经跌超2% 亚太风险传导", "content": "日经225指数早盘跌幅扩大至超2%，韩股三星-4.39%SK海力士-4.52%，亚太市场集体回调。北向资金若大幅流出将加剧A股科技股调整压力。", "tag": "外围风险", "tag_color": "red"},
    {"title": "美债5.24%高利率压制估值", "content": "10年期美债收益率维持5.24%高位，密歇根大学通胀预期上升推高收益率。高利率环境下科技成长股估值承压，外资流入节奏可能放缓。", "tag": "利率风险", "tag_color": "orange"},
    {"title": "持仓4只标的3只大跌", "content": "10月12日英维克-4.01%、铜冠铜箔-4.60%、雅克科技-3.36%，仅*ST建艺微涨+1.3%。连续两日大面积回调，需警惕短期趋势走坏，严格执行止损纪律。", "tag": "持仓风险", "tag_color": "red"},
    {"title": "新能源汽车出口退税率下调", "content": "2027年4月起新能源汽车出口退税率从13%降至9%，影响出口利润。铜箔等上游产业链需求端或受波及，新能源链短期情绪承压。", "tag": "政策风险", "tag_color": "orange"},
    {"title": "Q3财报季不确定性", "content": "美股Q3财报季本周开启，银行股先行。在高估值背景下，任何低于预期的财报都可能引发大幅波动。A股科技股受美股财报情绪传导。", "tag": "财报风险", "tag_color": "orange"},
], cols=2)
gen.add_section("空方视角", bear_content, "⚠️")

# === 13. 教训库 ===
lessons_html = gen.build_lessons_section()
gen.add_section("历史教训", lessons_html, "📚")

# === 14. 每日总结 ===
gen.add_daily_summary()

# OG
gen.set_og(
    description="美股半导体重挫费城指数跌2.67%，美光-3.88%闪迪-5.97%；微软发布Maia 300 AI芯片市值重回4万亿；中金合并东兴/信达证券落地；日经225跌超2%亚太承压",
    image="https://boya357.github.io/daily-news-insight/assets/og-daily.png"
)

print("DEBUG: publishing...")
# === 发布 ===
output_file = "docs/daily/20261013_每日新闻洞察.html"
result = gen.publish(output_file)
print(f"OK 报告已生成: {result}")
if result.get("success"):
    import shutil
    shutil.copy(output_file, "docs/daily/latest.html")
    print(f"LATEST 已更新 latest.html")
    print(f"SIZE 文件大小: {result.get('file_size')} 字节")
else:
    print(f"ERROR 验证失败: {result.get('errors')}")
