#!/usr/bin/env python3
"""2026-09-08 每日新闻洞察 - V3 Pro生成器"""
import sys, os
sys.path.insert(0, 'v3')
os.chdir('/root/daily-news-insight')
from generators.daily_pro import DailyReportProGenerator

gen = DailyReportProGenerator(
    date_str="2026-09-08",
    weekday="周二",
    subtitle="存储芯片超级周期确认 | GPT-6引爆算力预期 | 瑞银预警年内两次加息",
    data_dir='/root/daily-news-insight/data'
)

# TL;DR
gen.set_tldr([
    ("存储超级周期再获验证", "三星SK海力士库存不足10天，KB证券预测2027存储占AI基建57%两年翻四倍，日韩存储股集体大涨", "green"),
    ("GPT-6 Astra引爆算力预期", "OpenAI发布最强模型，增强多步骤推理与Agent能力，AI算力与HBM需求再上修", "green"),
    ("瑞银预警年内两次加息", "美国8月非农大超预期三倍，CME加息概率60.4%，瑞银预测9月+12月各加25bp", "red"),
    ("9月7日A股V型反转", "沪指微涨0.07%深成指+1.91%创业板+3.41%，成交1.95万亿缩量，AI算力/CPO/PCB领涨", "orange"),
    ("信息通信十五五规划出台", "2030年智能算力达9800 EFLOPS，加强6G研发适时启动商用，利好算力全产业链", "green"),
])

# === 1. 隔夜全球市场 ===
gen.add_global_market()

# === 2. 市场总览 ===
gen.add_market_overview()

# === 3. 重大新闻 - tab切换 ===
news_tabs = [
    {
        "label": "国内政策",
        "content": gen.create_card_group([
            {
                "title": "📡 信息通信\"十五五\"规划出台 2030年智能算力9800 EFLOPS",
                "content": """工信部等部门发布信息通信行业发展规划，明确中长期发展目标：
<br><strong>核心目标（2030年）：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>行业收入规模达 <strong>4.1万亿元</strong></li>
<li>智能算力规模达 <strong>9800 EFLOPS</strong></li>
<li>加强6G、空芯光纤研发，适时启动6G商用</li>
<li>算力网络、工业互联网、卫星互联网全面部署</li>
</ul>
<strong>受益方向：</strong>算力基础设施（服务器/液冷/光模块）、6G通信、卫星互联网、CPO高速互联
<br><br>
<em style="opacity:0.6">来源：工信部、财联社</em>""",
            },
            {
                "title": "🏦 3600亿金融央企增资落地 大金融基本面获支撑",
                "content": """8家中央金融企业合计3600亿增资完成落地，大幅补充银行保险核心资本：
<br>
<ul style="margin:8px 0;padding-left:20px;">
<li>工商银行1000亿、农业银行1600亿，其余6家合计1000亿</li>
<li>增强服务实体经济与风险处置能力</li>
<li>大金融板块基本面预期得到支撑，估值修复空间打开</li>
</ul>
<strong>市场影响：</strong>金融权重估值修复，对大盘形成托底支撑
<br><br>
<em style="opacity:0.6">来源：财政部、证券时报</em>""",
            },
            {
                "title": "💰 央行5000亿买断式逆回购 流动性平稳应对季末",
                "content": """央行9月7日开展5000亿元3个月期买断式逆回购等量续作，精准对冲季末资金压力：
<br>
<ul style="margin:8px 0;padding-left:20px;">
<li>到期对冲后小幅净回笼45亿元，操作以精准对冲为主</li>
<li>8月末外储34383亿美元，环比增195亿，央行黄金储备连续22个月增持</li>
<li>人民币汇率稳定，离岸人民币在6.71附近窄幅波动</li>
</ul>
<em style="opacity:0.6">来源：央行公开市场业务交易公告</em>""",
            },
            {
                "title": "📱 华为发布麒麟9050 Pro 时隔六年旗舰芯片回归",
                "content": """华为发布Mate XT 2三折叠手机，搭载最新麒麟9050 Pro芯片：
<br>
<ul style="margin:8px 0;padding-left:20px;">
<li>全球首款落地"韬定律"、采用逻辑折叠技术的旗舰芯片</li>
<li>整机性能较上代提升42%，芯片性能跨越式提升</li>
<li>小米同步发布18 Fold折叠屏，造芯累计投入210亿元</li>
<li>国产半导体链情绪提振，折叠屏/铰链/UTG硬件链热度维持</li>
</ul>
<em style="opacity:0.6">来源：华为发布会、财联社</em>""",
            },
        ], cols=1)
    },
    {
        "label": "海外市场",
        "content": gen.create_card_group([
            {
                "title": "🇺🇸 非农大超预期三倍 瑞银预警年内两次加息",
                "content": """美国8月非农就业增加16.2万人，远超预期5.5万人，劳动力市场韧性超预期：
<br><strong>核心数据：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>非农就业 <strong style="color:#ef4444;">+16.2万</strong>（预期+5.5万，约三倍超预期）</li>
<li>失业率 <strong>4.1%</strong>（预期4.3%）</li>
<li>平均时薪同比 <strong>3.7%</strong>（预期3.6%）</li>
</ul>
<strong>市场影响：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>CME FedWatch显示9月加息概率 <strong style="color:#ef4444;">60.4%</strong></li>
<li>瑞银修正预测：9月+12月各加息25bp，全年累计加息50bp</li>
<li>花旗/麦格理也上调利率预期，华尔街分歧加剧</li>
<li>10年期美债收益率维持高位，成长股估值承压</li>
</ul>
<strong>关键节点：</strong>本周五（9/11）美国8月CPI数据将决定最终路径
<br><br>
<em style="opacity:0.6">来源：美国劳工部、CME、瑞银、财联社</em>""",
            },
            {
                "title": "🤖 GPT-6 Astra发布 OpenAI最强模型引爆算力预期",
                "content": """OpenAI 9月3日发布GPT-6 Astra，为迄今能力最强的AI模型：
<br>
<ul style="margin:8px 0;padding-left:20px;">
<li>增强编程、研究、计算机操作及复杂多步骤任务处理能力</li>
<li>可按用户模板制作文档、表格、演示文稿</li>
<li>Agentic AI能力提升，推动AI基础设施投资加速</li>
<li>市场对AI算力及存储需求预期再度升温</li>
</ul>
<strong>市场反应：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>日韩存储芯片股集体爆发：三星电子+5.68%、SK海力士+8.26%、铠侠+7%</li>
<li>美股存储板块上周五大涨：闪迪+11.9%、美光+6.1%、西部数据+5.86%</li>
<li>费城半导体指数+3.37%，逆势走强</li>
</ul>
<em style="opacity:0.6">来源：OpenAI公告、新浪财经、21世纪经济报道</em>""",
            },
            {
                "title": "💾 存储超级周期再确认 三星SK海力士库存不足10天",
                "content": """KB Securities最新报告验证存储超级周期逻辑：
<br><strong>核心判断：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>三星电子、SK海力士内存库存 <strong>已不足10天</strong></li>
<li>2027年全球超大规模数据中心AI基建投资达1.3万亿美元，同比+60%</li>
<li>存储在AI基建中占比从2025年14%升至2027年57%，<strong>两年翻四倍</strong></li>
<li>DRAM供不应求格局至少延续至2028年</li>
</ul>
<strong>高盛上调光模块预测：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>2026-2028年全球光模块市场677亿/1314亿/1485亿美元</li>
<li>较此前预测上调33%/81%/115%</li>
<li>AI服务器架构向高速网络迁移，单GPU光模块用量增加</li>
</ul>
<em style="opacity:0.6">来源：KB Securities、高盛、集邦咨询</em>""",
            },
        ], cols=1)
    },
    {
        "label": "地缘大宗",
        "content": gen.create_card_group([
            {
                "title": "🛡️ 中东局势持续 霍尔木兹海峡航运骤减",
                "content": """美伊冲突背景下，霍尔木兹海峡航运风险持续被市场定价：
<br>
<ul style="margin:8px 0;padding-left:20px;">
<li>霍尔木兹海峡日均通行商船仅10艘，为5月以来最低</li>
<li>WTI原油 <strong style="color:#ef4444;">92.60美元</strong>（+1.22%），布伦特 <strong>97.15美元</strong></li>
<li>布伦特逼近100美元关口，通胀预期回升</li>
<li>有消息称伊朗接近与阿曼达成临时安全航道协议，或成缓和变量</li>
</ul>
<strong>对A股影响：</strong>油气开采/油服板块受益，但高油价推升通胀，制约货币政策空间
<br><br>
<em style="opacity:0.6">来源：汇通网、财联社</em>""",
            },
            {
                "title": "🥇 黄金4400关口多空激战 央行增持支撑长期逻辑",
                "content": """加息预期与地缘风险交织，黄金在4400美元关口展开多空拉锯：
<br>
<ul style="margin:8px 0;padding-left:20px;">
<li>COMEX黄金 <strong>4470美元</strong>附近震荡，加息预期短期压制</li>
<li>中国央行连续22个月增持黄金，8月增65万盎司至7673万盎司</li>
<li>8月末外储34383亿美元，环比增195亿美元</li>
<li>本周CPI/PPI数据将决定黄金短期方向</li>
</ul>
<em style="opacity:0.6">来源：国家外汇管理局、汇通网</em>""",
            },
            {
                "title": "🔶 LME铜价创历史新高 制造业成本压力加大",
                "content": """铜价持续走高，LME铜一度触及14533美元/吨创历史新高：
<br>
<ul style="margin:8px 0;padding-left:20px;">
<li>供需紧平衡+AI算力/新能源需求拉动铜价上行</li>
<li>刚果金禁运铜钴精矿，供给端扰动加剧</li>
<li>PCB、家电、基建等中下游制造业成本压力加大</li>
<li>铜冠铜箔等铜加工企业：原料涨价传导+需求弹性双重影响</li>
</ul>
<em style="opacity:0.6">来源：上海有色网、财联社</em>""",
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
        "title": "💾 存储超级周期确认",
        "content": "三星SK海力士库存不足10天，KB证券预测2027存储占AI基建57%，存储板块情绪催化",
        "icon": "🟢",
    },
    {
        "title": "🤖 GPT-6引爆算力预期",
        "content": "OpenAI发布最强模型，Agent能力提升推动AI基建投资，算力链/HBM需求再上修",
        "icon": "🟢",
    },
    {
        "title": "📡 十五五算力规划",
        "content": "2030年智能算力9800 EFLOPS，6G适时商用，算力基础设施全产业链政策催化",
        "icon": "🟢",
    },
    {
        "title": "🇺🇸 加息预期升温",
        "content": "非农大超预期，CME加息概率60.4%，瑞银预警年内两次加息，外资节奏或受扰动",
        "icon": "🔴",
    },
    {
        "title": "❄️ 液冷政策发酵",
        "content": "七部门数字化绿色化方案持续催化，液冷/绿色数据中心方向明确，英维克受益",
        "icon": "🟢",
    },
    {
        "title": "📊 今日进出口数据",
        "content": "上午公布8月进出口贸易数据，出口进口验证外需景气度，北向资金动向受关注",
        "icon": "🟠",
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
        "title": "非农爆表 加息预期升温",
        "content": "美国8月非农超预期三倍，CME加息概率升至60.4%，瑞银预计9月+12月各加25bp，美债收益率维持高位，外资流入节奏可能受扰动，成长股估值承压。",
        "tag": "海外风险",
        "tag_color": "red",
    },
    {
        "title": "油价飙升 通胀预期回升",
        "content": "布伦特逼近100美元，中东局势+OPEC+减产，高油价推升全球通胀预期，可能强化美联储加息逻辑，制约国内货币政策宽松空间。",
        "tag": "通胀风险",
        "tag_color": "red",
    },
    {
        "title": "存储板块获利了结压力",
        "content": "隔夜存储股大涨但A股存储板块前期涨幅较大，高位获利了结压力不容忽视，板块波动率可能放大，追高需谨慎。",
        "tag": "资金风险",
        "tag_color": "red",
    },
    {
        "title": "成交缩量反弹 持续性存疑",
        "content": "9月7日成交1.95万亿较上日缩量846亿，缩量反弹意味着资金参与度下降，AI算力主线持续性需观察，量能能否恢复是关键。",
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
    description="存储超级周期再确认！三星SK海力士库存不足10天，GPT-6引爆算力预期；非农大超预期瑞银预警年内两次加息；9月7日A股V型反转创业板+3.41%",
    image="https://boya357.github.io/daily-news-insight/assets/og-daily.png"
)

# === 发布 ===
output_file = "docs/daily/20260908_每日新闻洞察.html"
result = gen.publish(output_file)
print(f"OK 报告已生成: {result}")
if result.get("success"):
    import shutil
    shutil.copy(output_file, "docs/daily/latest.html")
    print(f"LATEST 已更新 latest.html")
    print(f"SIZE 文件大小: {result.get('file_size')} 字节")
else:
    print(f"ERROR 验证失败: {result.get('errors')}")
