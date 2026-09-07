#!/usr/bin/env python3
"""2026-09-07 每日新闻洞察 - V3 Pro生成器"""
import sys, os
sys.path.insert(0, 'v3')
os.chdir('/root/daily-news-insight')
from generators.daily_pro import DailyReportProGenerator

gen = DailyReportProGenerator(
    date_str="2026-09-07",
    weekday="周一",
    subtitle="周末利好利空交织 | 金融注资3000亿vs非农爆表加息预期 | 液冷政策催化",
    data_dir='/root/daily-news-insight/data'
)

# TL;DR
gen.set_tldr([
    ("财政部3000亿注资金融央企", "工行1000亿+农行1600亿等8家金融央企获特别国债注资，银行资本充足率提升，金融权重托底市场", "green"),
    ("非农爆表加息预期重燃", "美国8月非农16.2万远超预期5.5万，CME加息概率飙至58-60%，10年期美债收益率跳升", "red"),
    ("七部门液冷政策利好", "数字化绿色化方案出台，支持液冷散热/800V高压直流，英维克等液冷龙头直接受益", "green"),
    ("半导体卖硬买软切换", "9月4日半导体板块净流出153亿，硬件获利了结，AI应用/软件获资金流入", "orange"),
    ("持仓普跌 ST建艺逆势涨", "英维克-6.69%、铜冠铜箔-3.79%、雅克-3.78%、*ST建艺+8.75%，板块整体回调", "red"),
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
                "title": "🏦️ 财政部3000亿特别国债注资8家金融央企",
                "content": """财政部向8家金融央企注入3000亿元特别国债资金，大幅补充核心一级资本：
<br><strong>注资明细：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>工商银行 <strong>1000亿元</strong></li>
<li>农业银行 <strong>1600亿元</strong></li>
<li>其余6家机构合计400亿元（含中行、建行、国开行等）</li>
</ul>
<strong>市场影响：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>银行核心一级资本充足率提升约0.3-0.5个百分点，信贷投放能力增强</li>
<li>金融权重股估值修复，对大盘形成托底支撑</li>
<li>财政政策发力稳增长信号明确，提振市场风险偏好</li>
</ul>
<em style="opacity:0.6">来源：财政部、证券时报、财联社</em>""",
            },
            {
                "title": "❄️ 七部门出台数字化绿色化方案 液冷散热获政策支持",
                "content": """七部门联合印发《数字化绿色化协同发展实施方案》，明确支持数据中心液冷技术路线：
<br>
<ul style="margin:8px 0;padding-left:20px;">
<li>推动液冷散热技术规模化应用，鼓励800V高压直流供电</li>
<li>新建大型、超大型数据中心全面推广液冷技术</li>
<li>支持液冷服务器、冷却液、冷板等核心零部件国产化</li>
<li>目标2027年新建数据中心PUE降至1.15以下</li>
</ul>
<strong>受益方向：</strong>液冷散热（英维克、申菱环境）、数据中心电源、储能温控
<br><br>
<em style="opacity:0.6">来源：工信部、七部门联合发文</em>""",
            },
            {
                "title": "💰 央行5000亿逆回购护盘 流动性维持宽松",
                "content": """央行开展5000亿元7天期逆回购操作，对冲到期后净投放3000亿元，维护季末流动性平稳。
<br>
<ul style="margin:8px 0;padding-left:20px;">
<li>银行间市场利率稳定，DR007维持在政策利率附近</li>
<li>季末资金面总体宽松，降准预期仍存</li>
<li>人民币汇率保持稳定，在6.85附近震荡</li>
</ul>
<em style="opacity:0.6">来源：央行公开市场业务交易公告</em>""",
            },
        ], cols=1)
    },
    {
        "label": "海外市场",
        "content": gen.create_card_group([
            {
                "title": "🇺🇸 非农数据大爆冷 加息预期急剧升温",
                "content": """美国8月非农就业人数增加16.2万人，远超市场预期的5.5万人，劳动力市场韧性超预期：
<br><strong>核心数据：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>非农就业 <strong style="color:#ef4444;">+16.2万</strong>（预期+5.5万，前值+1.7万修正为+3.2万）</li>
<li>失业率 <strong>4.1%</strong>（预期4.3%，前值4.2%）</li>
<li>平均时薪同比 <strong>3.7%</strong>（预期3.6%）</li>
<li>劳动参与率 <strong>62.6%</strong>（预期62.5%）</li>
</ul>
<strong>市场影响：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>CME FedWatch显示9月加息概率从20%飙升至<strong>58-60%</strong></li>
<li>10年期美债收益率跳升至4.95%，创近月新高</li>
<li>美元指数走强，黄金跌破4400美元</li>
<li>三大股指承压，道指-0.51%、纳指-0.29%</li>
</ul>
<em style="opacity:0.6">来源：美国劳工部、CME、汇通网</em>""",
            },
            {
                "title": "💾 存储芯片暴涨 美光+6.1% 费城半导体+3.37%",
                "content": """尽管大盘承压，半导体板块逆势大涨，存储芯片成为最强主线：
<br><strong>核心标的涨幅：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>费城半导体指数 <strong style="color:#4ade80;">+3.37%</strong>（收11735点）</li>
<li>美光科技 <strong style="color:#4ade80;">+6.10%</strong>（收$1016.59，创历史新高）</li>
<li>AMD <strong style="color:#4ade80;">+4.69%</strong>（收$477.57）</li>
<li>英伟达 +0.84%（收$230.36）</li>
<li>台积电ADR +1.56%</li>
</ul>
<strong>催化因素：</strong>
<ol style="margin:8px 0;padding-left:20px;">
<li><strong>HBM需求爆发</strong>：AI大模型训练推动HBM3E/HBM4需求持续超预期</li>
<li><strong>存储涨价周期</strong>：DRAM/NAND合约价持续上涨，三季度业绩确定性强</li>
<li><strong>韩股联动</strong>：三星、SK海力士逆势走强，存储景气度验证</li>
</ol>
<em style="opacity:0.6">来源：东方财富、证券时报</em>""",
            },
        ], cols=1)
    },
    {
        "label": "地缘大宗",
        "content": gen.create_card_group([
            {
                "title": "🛡️ 中东局势升级+OPEC+暂停增产 油价破92美元",
                "content": """地缘政治风险叠加供应收紧预期，国际油价大幅上涨：
<br>
<ul style="margin:8px 0;padding-left:20px;">
<li>WTI原油 <strong style="color:#ef4444;">92.35美元</strong>（+3.2%）</li>
<li>布伦特原油 <strong style="color:#ef4444;">96.80美元</strong>（+2.9%）</li>
<li>OPEC+宣布暂停增产计划，延长减产至年底</li>
<li>中东局势再度紧张，原油运输风险溢价上升</li>
</ul>
<strong>对A股影响：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>油气开采、油服板块直接受益</li>
<li>高油价推升通胀预期，制约货币政策空间</li>
<li>交运、化工等下游行业成本压力加大</li>
</ul>
<em style="opacity:0.6">来源：汇通网、OPEC公告</em>""",
            },
            {
                "title": "🥇 黄金回落 避险情绪分化",
                "content": """受加息预期升温压制，黄金从高位回落：
<br>
<ul style="margin:8px 0;padding-left:20px;">
<li>COMEX黄金 <strong style="color:#ef4444;">4382美元</strong>（-1.2%）</li>
<li>美元指数走强至104.8，压制金价</li>
<li>地缘风险仍提供底部支撑，跌幅受限</li>
</ul>
<em style="opacity:0.6">来源：全球市场数据</em>""",
            },
        ], cols=1)
    },
    {
        "label": "产业动态",
        "content": gen.create_card_group([
            {
                "title": "💻 半导体“卖硬买软” 硬件净流出153亿",
                "content": """9月4日A股半导体板块出现明显资金切换：
<br>
<ul style="margin:8px 0;padding-left:20px;">
<li>半导体板块主力净流出 <strong style="color:#ef4444;">153.11亿元</strong></li>
<li>设备、材料、存储等硬件方向获利了结明显</li>
<li>AI应用、大模型、软件方向获资金流入</li>
<li>市场风格从"硬科技"向"软应用"切换迹象</li>
</ul>
<strong>切换逻辑：</strong>硬件涨幅较大估值偏高，叠加中报业绩兑现期资金获利了结；AI应用端商业化加速，估值弹性更大。
<br><br>
<em style="opacity:0.6">来源：东方财富资金流向</em>""",
            },
            {
                "title": "🤖 人形机器人：宇树催化持续 产业链加速落地",
                "content": """人形机器人产业动态更新：
<br>
<ul style="margin:8px 0;padding-left:20px;">
<li>宇树科技上市后持续催化国产人形机器人估值体系</li>
<li>T链人形机器人9月周产预计1000+台，量产进度超预期</li>
<li>特斯拉Optimus Gen-3预计Q3亮相，效果有望超预期</li>
<li>减速器、丝杠、传感器等核心零部件国产替代加速</li>
</ul>
<em style="opacity:0.6">来源：财联社、各公司公告</em>""",
            },
        ], cols=1)
    },
]

news_tab_html = gen.create_tab_pane(news_tabs, tab_id="important-news", style="default")
gen.add_section("重大事件", news_tab_html, "📰")

# === 4. 板块分析 ===
gen.add_sector_analysis()

# === 5. 今日催化剂 ===
catalyst_content = gen.create_card_group([
    {
        "title": "🏦️ 3000亿注资金融央企",
        "content": "财政部3000亿特别国债注资8家金融央企，银行资本充足率提升，金融权重托底大盘",
        "icon": "🟢",
    },
    {
        "title": "❄️ 七部门液冷政策利好",
        "content": "数字化绿色化方案支持液冷散热/800V高压直流，液冷龙头直接受益，英维克催化",
        "icon": "🟢",
    },
    {
        "title": "💾 存储芯片隔夜暴涨",
        "content": "美光+6.1%创历史新高，费半+3.37%，HBM需求爆发+涨价周期共振",
        "icon": "🟢",
    },
    {
        "title": "🇺🇸 非农爆表加息预期",
        "content": "8月非农16.2万远超预期，CME加息概率飙至60%，美债收益率跳升",
        "icon": "🔴",
    },
    {
        "title": "🛡️ 中东升级油价破92",
        "content": "OPEC+暂停增产+地缘风险，WTI破92美元，通胀预期回升",
        "icon": "🔴",
    },
    {
        "title": "💻 半导体资金切换",
        "content": "硬件净流出153亿，卖硬买软风格切换，AI应用获流入",
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
        "title": "非农爆表 加息预期重燃",
        "content": "美国8月非农大超预期，9月加息概率升至60%，美债收益率跳升，外资回流节奏可能受扰动，成长股估值承压。",
        "tag": "海外风险",
        "tag_color": "red",
    },
    {
        "title": "油价飙升 通胀预期回升",
        "content": "WTI破92美元，中东升级+OPEC+减产，高油价推升全球通胀预期，可能制约国内货币政策宽松空间。",
        "tag": "通胀风险",
        "tag_color": "red",
    },
    {
        "title": "半导体资金大幅流出",
        "content": "9月4日半导体净流出153亿，硬件板块获利了结压力大，高位股资金兑现意愿强，短期调整可能延续。",
        "tag": "资金风险",
        "tag_color": "red",
    },
    {
        "title": "成交放量下跌 多空分歧加剧",
        "content": "9月4日成交2.05万亿放量2700亿但指数收跌，放量下跌意味着多空分歧加大，短期震荡可能加剧。",
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
    description="财政部3000亿注资金融央企 vs 非农爆表加息预期升温，七部门液冷政策利好；9月4日A股放量下跌成交2.05万亿，半导体净流出153亿",
    image="https://boya357.github.io/daily-news-insight/assets/og-daily.png"
)

# === 发布 ===
output_file = "docs/daily/20260907_每日新闻洞察.html"
result = gen.publish(output_file)
print(f"OK 报告已生成: {result}")
if result.get("success"):
    import shutil
    shutil.copy(output_file, "docs/daily/latest.html")
    print(f"LATEST 已更新 latest.html")
    print(f"SIZE 文件大小: {result.get('file_size')} 字节")
else:
    print(f"ERROR 验证失败: {result.get('errors')}")
