#!/usr/bin/env python3
"""2026-10-12 每日新闻洞察 - V3 Pro生成器"""
import sys, os
sys.path.insert(0, 'v3')
os.chdir('/root/daily-news-insight')
from generators.daily_pro import DailyReportProGenerator

gen = DailyReportProGenerator(
    date_str="2026-10-12",
    weekday="周一",
    subtitle="美光FY26净利850亿美元创新高 | 长鑫4F²架构突破年底推DDR5 RDIMM | 新质生产力意见重磅发布",
    data_dir='/root/daily-news-insight/data'
)

# TL;DR
gen.set_tldr([
    ("美光FY26净利润850亿美元创新高", "2026财年营收1332亿同比+256%，Q4单季净利377亿同比+1078%，回购计划扩至350亿美元，1γ DRAM节点量产强劲，2027财年更强劲", "green"),
    ("长鑫4F²架构重大突破", "长鑫科技官宣DRAM下一代4F²架构取得突破，预计年底推出新一代DDR5 RDIMM，存储密度提升30-50%，VSG垂直包围栅晶体管自研", "green"),
    ("新质生产力意见重磅发布", "中共中央国务院印发《关于发展新质生产力的意见》，部署19项重点举措，大力推进科技创新、产业创新深度融合", "green"),
    ("美股四连阳 软件安全股领涨", "道指+0.83%标普+0.59%纳指+0.64%，纳指周线四连阳创5月以来最长连涨，软件/网络安全股走强，半导体分化", "orange"),
    ("英伟达洽谈收购Reflection AI", "估值250亿美元，谈判早期阶段，英伟达此前已投资8亿，进一步布局开放权重模型与AI生态", "orange"),
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
                "title": "💰 美光FY26净利850亿美元创历史新高 Q4单季377亿同比+1078%",
                "content": """美光科技公布2026财年全年业绩，净利润849.69亿美元创半导体行业历史纪录：
<br><strong>核心财务：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>全年营收<strong>1331.88亿美元</strong>，同比+256%</li>
<li>全年净利润<strong>849.69亿美元</strong>，去年同期85.39亿</li>
<li>毛利率81%，去年同期40%，前年22%</li>
<li>每股收益74.33美元，去年同期7.59美元</li>
<li>Q4单季营收542亿同比+380%，净利377亿同比+1078%</li>
</ul>
<strong>分产品：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>DRAM营收1006.8亿美元，占比76%</li>
<li>NAND营收317.9亿美元，占比24%</li>
<li>云/HBM业务430.85亿，数据中心375.92亿</li>
</ul>
<strong>关键进展：</strong>1γ DRAM节点为业界首个EUV DRAM节点，Q4已成为出货量最大节点；HBM需求持续供不应求。
<br><br>
<em style="opacity:0.6">来源：美光科技10-K年报、证券之星、21世纪经济报道</em>""",
            },
            {
                "title": "🔒 美光回购计划扩至350亿美元 年内股价涨260%",
                "content": """美光董事会批准扩大股票回购计划，回购上限从100亿美元上调至351.6亿美元：
<br>
<ul style="margin:8px 0;padding-left:20px;">
<li>回购计划将于2026年12月9日起生效</li>
<li>此前100亿回购约22亿尚未使用</li>
<li>美光股价周五下跌0.66%，今年累计上涨约260%</li>
<li>FY27 Q1营收指引615亿美元，EPS 37.84美元</li>
</ul>
<strong>展望2027财年：</strong>美光董事长Sanjay Mehrotra表示，FY26创纪录业绩，<strong>预计2027财年表现更强劲</strong>。四大业务单元（云存储、数据中心、移动客户端、汽车嵌入式）均实现强劲增长。
<br><strong>现金流：</strong>经营现金流896.75亿美元，资本支出307.12亿美元，现金及等价物383.64亿美元，财务状况极为健康。
<br><br>
<em style="opacity:0.6">来源：财联社、36氪</em>""",
            },
            {
                "title": "🚀 长鑫4F²架构重大突破 年底推新一代DDR5 RDIMM",
                "content": """第四届集成芯片和芯粒大会上，长鑫科技总裁曹堪宇宣布DRAM下一代核心架构4F²取得重大突破：
<br><strong>技术突破：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>从主流6F²架构升级到4F²，单位面积存储密度提升<strong>30%-50%</strong></li>
<li>自研<strong>VSG垂直包围栅晶体管</strong>，解决漏电与短沟道效应</li>
<li>同步完成字线金属化、位线成型、结激活等核心工艺</li>
<li>预计2026年底推出融合4F²架构+混合键合的新一代DDR5 RDIMM</li>
</ul>
<strong>战略意义：</strong>首款落地产品选服务器内存DDR5 RDIMM，直面最高难度市场。目前全球服务器DRAM被三星/SK海力士/美光三家垄断，长鑫用下一代架构弯道超车意图明显。
<br><strong>挑战：</strong>4F²架构无法沿用原有产线，改造投入巨大；服务器内存认证周期长（2-3年）。
<br><br>
<em style="opacity:0.6">来源：证券日报、企业上市公众号</em>""",
            },
            {
                "title": "📈 华强北内存条一年涨超300% AI需求虹吸产能",
                "content": """深圳华强北内存价格持续暴涨，AI算力需求对上游产能虹吸效应明显：
<br>
<ul style="margin:8px 0;padding-left:20px;">
<li>DDR4 16G：去年最低100多元 → 现在最低600多元，涨幅超300%</li>
<li>DDR5 16G：最便宜200多元 → 现在最低1400元以上</li>
<li>金士顿DDR3：去年9月218元 → 目前499元，涨幅129%</li>
<li>金百达DDR5：5月底价2399元 → 最新3499元，涨幅45.9%</li>
</ul>
<strong>根本原因：</strong>AI服务器内存需求量是普通服务器的8-10倍，全球约70%先进存储产能被AI吞噬，三巨头持续将产能转向利润更高的HBM，消费级DRAM供给被严重挤压。
<br><strong>趋势判断：</strong>供应链消息称成熟制程DRAM四季度仍将"稳步涨价"，HBM4价格2027年预计涨近3倍。
<br><br>
<em style="opacity:0.6">来源：36氪、深圳广电、界面新闻</em>""",
            },
        ], cols=1)
    },
    {
        "label": "海外市场",
        "content": gen.create_card_group([
            {
                "title": "📈 美股周线四连阳 软件安全股领涨 半导体分化",
                "content": """美股周五集体收涨，纳指录得连续第四周上涨，创5月以来最长连涨纪录：
<br><strong>收盘数据：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>道琼斯 <strong style="color:#22c55e;">+0.83%</strong> 报51654.95点（+423点）</li>
<li>标普500 <strong style="color:#22c55e;">+0.59%</strong> 报7811.54点</li>
<li>纳斯达克 <strong style="color:#22c55e;">+0.64%</strong> 报27366.17点</li>
<li>纳斯达克100 <strong style="color:#22c55e;">+0.51%</strong> 报30883.15点</li>
<li>费城半导体 <strong style="color:#ef4444;">-0.41%</strong> 报12572.42点</li>
</ul>
<strong>板块分化：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>领涨：软件、网络安全股（Snowflake、Datadog、Palantir、Palo Alto Networks）</li>
<li>下跌：半导体股（ARM、英特尔-2.22%、AMD-2.03%、超微电脑）</li>
<li>大型科技：微软+2.38%、博通+0.39%、阿斯麦+0.60%、英伟达-0.52%</li>
</ul>
<strong>本周涨幅：</strong>道指+0.93%，标普+1.15%，纳指+0.64%。道指创8月7日以来最大单周涨幅。
<br><br>
<em style="opacity:0.6">来源：Great Day Trading、TipRanks</em>""",
            },
            {
                "title": "🤖 英伟达洽谈收购Reflection AI 估值250亿美元",
                "content": """据媒体10月10日报道，英伟达正与AI初创公司Reflection AI洽谈收购或深化投资事宜：
<br>
<ul style="margin:8px 0;padding-left:20px;">
<li>谈判处于早期阶段，尚未确定具体条款</li>
<li>Reflection AI今年3月融资后估值达<strong>250亿美元</strong></li>
<li>英伟达此前已向其投资约8亿美元</li>
<li>可能交易结构：人才收购、技术授权、股权投资或提供更多算力</li>
<li>Reflection AI专注于开放权重模型研发</li>
</ul>
<strong>战略意义：</strong>英伟达正从芯片供应向模型、算力及开发生态延伸。硬件垄断的护城河正被开源软件生态侵蚀，通过投资/收购模型公司既能拓展GPU应用场景，也能增强在AI产业链影响力。
<br><strong>其他AI动态：</strong>微软推出Microsoft-Decision-1决策AI模型，速度较GPT-6 Sol快35倍；马斯克将SpaceXAI更名为SpaceX Super Intelligence。
<br><br>
<em style="opacity:0.6">来源：每日经济新闻、新浪财经</em>""",
            },
            {
                "title": "🇰🇷 ASML上调韩国客户零部件价格10% 三星SK海力士接受",
                "content": """ASML已通知三星电子和SK海力士，将光刻机零部件价格统一上调10%：
<br>
<ul style="margin:8px 0;padding-left:20px;">
<li>涉及EUV和DUV光刻机零部件</li>
<li>包括消耗性部件及光学系统、光源等核心组件</li>
<li>涨价预计2027年1月生效</li>
<li>三星和SK海力士均已接受涨价</li>
</ul>
<strong>韩股半导体表现：</strong>周五三星电子-2.42%、SK海力士-2.44%，韩国半导体板块整体回调。
<br><strong>三星Q3业绩：</strong>三星电子初步财报显示单季营业利润突破100万亿韩元，创韩国企业历史纪录，主要受益于存储芯片价格大涨。
<br><strong>越南扩产：</strong>三星投资40.8亿美元在越南扩建存储测试基地，分散韩国本土产能风险。
<br><br>
<em style="opacity:0.6">来源：每日经济新闻、DIGITIMES</em>""",
            },
            {
                "title": "🛢️ 金价再创历史新高 油价回落美债收益率5.24%",
                "content": """大宗商品市场走势分化，黄金再创新高，原油承压：
<br>
<ul style="margin:8px 0;padding-left:20px;">
<li>COMEX黄金 <strong style="color:#22c55e;">+0.42%</strong> 报4233.85美元/盎司，创历史新高</li>
<li>COMEX白银 <strong style="color:#22c55e;">+0.95%</strong> 报61.63美元</li>
<li>WTI原油 <strong style="color:#ef4444;">-1.21%</strong> 报90.74美元</li>
<li>布伦特原油 <strong style="color:#ef4444;">-1.10%</strong> 报103.57美元</li>
<li>10年期美债收益率约5.24%</li>
<li>VIX恐慌指数 -1.56% 报14.84</li>
</ul>
<strong>驱动因素：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>黄金：地缘政治风险+央行持续购金+降息预期支撑</li>
<li>原油：中东局势缓和+需求担忧压制油价</li>
<li>美债：AI基建投资热潮推升融资需求，收益率维持高位</li>
</ul>
<br><br>
<em style="opacity:0.6">来源：TipRanks、全球市场数据</em>""",
            },
        ], cols=1)
    },
    {
        "label": "国内政策",
        "content": gen.create_card_group([
            {
                "title": "📋 中共中央国务院重磅发布《关于发展新质生产力的意见》",
                "content": """中共中央、国务院印发《关于发展新质生产力的意见》，部署19项重点举措：
<br><strong>五大方面：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>大力推进科技创新</li>
<li>推动科技创新和产业创新深度融合</li>
<li>着力推进发展方式创新</li>
<li>扎实推进体制机制创新</li>
<li>深化人才工作机制创新</li>
</ul>
<strong>核心原则：</strong>坚持创新主导、改革为要、因地制宜、先立后破，坚持高技术、高效能、高质量。以科技创新为引领，以全要素生产率大幅提升为核心标志，推动技术革命性突破、生产要素创新性配置、产业深度转型升级。
<br><strong>投资启示：</strong>新质生产力相关赛道（AI、半导体、高端制造、新能源、生物医药等）有望持续获得政策支持，科技成长主线逻辑进一步强化。
<br><br>
<em style="opacity:0.6">来源：证券时报、新华社</em>""",
            },
            {
                "title": "🏦 吴清主持座谈会 多路增量资金四季度入市可期",
                "content": """证监会主席吴清10月10日主持座谈会，就资本市场和金融形势听取意见：
<br><strong>政策建议：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>持续加强稳市机制建设，拓宽中长期资金来源</li>
<li>发展壮大耐心资本</li>
<li>推动上市公司加大分红回购力度</li>
<li>优化发行上市制度，支持多元化优质企业</li>
<li>强化交易监管，加强跨境风险监测</li>
<li>研究储备更多增量政策工具</li>
</ul>
<strong>增量资金测算：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>保险资金：二季度末股基配置6.39万亿，五大险企上半年净流入A股3523亿</li>
<li>若落实30%保费入市目标，三四季度增量或超2000亿</li>
<li>社保、年金四季度有望持续加码高股息红利资产</li>
<li>公募基金运作管理办法修订，加快增量资金入市步伐</li>
</ul>
<br><br>
<em style="opacity:0.6">来源：证券日报、中国证券报</em>""",
            },
            {
                "title": "🏭 中国工博会今日开幕 人形机器人/智能制造成焦点",
                "content": """第二十六届中国国际工业博览会10月12日至16日在上海举办：
<br>
<ul style="margin:8px 0;padding-left:20px;">
<li>聚焦智能制造、工业互联网、机器人等前沿领域</li>
<li>人形机器人企业集中亮相，展示最新量产进展</li>
<li>优必选与建发股份共建合资公司，目标2030年销1万台人形机器人</li>
<li>国产工业机器人、数控机床、智能装备等将集中展示</li>
</ul>
<strong>人形机器人动态：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>优必选+建发股份：合资公司落地福建，1万台销售目标</li>
<li>特斯拉Optimus、小米CyberOne、Figure等产品持续迭代</li>
<li>产业链关注：减速器、伺服电机、控制器、传感器</li>
</ul>
<strong>催化预期：</strong>工博会期间人形机器人/智能制造板块或有主题性催化，关注技术突破与量产进展。
<br><br>
<em style="opacity:0.6">来源：上海证券报、每日经济新闻</em>""",
            },
            {
                "title": "⚖️ 工业富联/立讯精密遭美国337调查",
                "content": """美国ITC对多家中国科技企业启动337调查，需警惕地缘政治风险：
<br><strong>工业富联：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>Vicor指控"垂直供电系统"专利侵权</li>
<li>公司回应：涉及产品处于内部验证阶段，对生产经营无实质影响</li>
<li>337调查周期长、应诉成本高，需持续跟踪</li>
</ul>
<strong>立讯精密：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>ITC正式启动调查，编号337-TA-1526</li>
<li>涉及产品处于客户验证阶段，尚未量产</li>
<li>调查尚处立案初期，未作实质认定</li>
</ul>
<strong>风险启示：</strong>美国对华科技遏制持续，电子制造/半导体设备等板块需警惕出口管制与专利诉讼风险，优先选择国产替代确定性高的标的。
<br><br>
<em style="opacity:0.6">来源：每日经济新闻、中国证券报</em>""",
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
        "content": "⭐ S级主线 | 美光FY26净利850亿创纪录，Q4单季377亿同比+10倍，回购扩至350亿；长鑫4F²架构突破年底推DDR5 RDIMM；内存现货价一年涨300%+，超级周期延续",
        "icon": "🟢",
    },
    {
        "title": "💻 AI算力/液冷",
        "content": "⭐ S级主线 | 英伟达洽谈收购Reflection AI布局开放权重模型；ASML零部件涨价10%；微软推出决策AI模型快35倍；新质生产力意见支持科技创新",
        "icon": "🟡",
    },
    {
        "title": "🤖 人形机器人",
        "content": "⭐ A级主线 | 工博会今日开幕，人形机器人成焦点；优必选+建发股份1万台销售目标；具身智能产业加速落地，关注减速器/伺服电机产业链",
        "icon": "🟡",
    },
    {
        "title": "🔧 先进封装/半导体材料",
        "content": "⭐ A级主线 | 长鑫4F²突破利好国产设备材料；ASML零部件涨价10%传导效应；雅克科技/华海诚科等半导体材料国产替代加速",
        "icon": "🟡",
    },
], cols=2)

gen.add_section("行业追踪", industry_content, "🏭")

# === 5. 今日催化 ===
catalyst_content = gen.create_card_group([
    {
        "title": "⚡ 存储板块业绩催化",
        "content": "美光FY26创纪录业绩+回购扩至350亿+FY27指引更强劲，长鑫4F²突破利好国产存储，A股存储板块情绪有望提振",
        "icon": "🟢",
    },
    {
        "title": "📋 新质生产力政策催化",
        "content": "中共中央国务院发布新质生产力意见，19项举措支持科技创新，科技成长主线获政策加持",
        "icon": "🟢",
    },
    {
        "title": "🤖 工博会主题催化",
        "content": "中国工博会今日开幕，人形机器人/智能制造/工业互联网成焦点，相关板块或有主题性机会",
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
        "title": "存储板块高位回调风险",
        "content": "美光年内涨幅260%，费城半导体指数连续调整，存储板块前期积累巨大涨幅。虽然业绩确定性强，但高估值下任何低于预期的指引都可能引发大幅回调。A股存储板块跟随美股波动，追高需谨慎。",
        "tag": "估值风险",
        "tag_color": "red",
    },
    {
        "title": "美债收益率5.24%压制成长股估值",
        "content": "10年期美债收益率维持在5.24%高位，AI基建投资热潮推升融资需求。高利率环境下，科技成长股估值面临压力，外资流入节奏可能受扰动。",
        "tag": "利率风险",
        "tag_color": "orange",
    },
    {
        "title": "337调查升温 地缘政治风险",
        "content": "美国ITC近期频繁对中国科技企业启动337调查（工业富联、立讯精密等），中美科技博弈持续。半导体设备、电子制造等板块需警惕出口管制和供应链风险。",
        "tag": "地缘风险",
        "tag_color": "orange",
    },
    {
        "title": "上周五A股科技股集体回调",
        "content": "10月9日A股科技板块调整明显，英维克-3.74%、雅克科技-4.64%、*ST建艺-4.68%、华海诚科-6.18%，持仓4只核心标的3只下跌超4%。调整是否结束需观察量能支撑，不宜盲目抄底。",
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
    description="美光FY26净利850亿美元创历史新高，Q4单季377亿同比+10倍；长鑫4F²架构突破年底推DDR5 RDIMM；新质生产力意见重磅发布；美股四连阳纳指周线四连涨",
    image="https://boya357.github.io/daily-news-insight/assets/og-daily.png"
)

# === 发布 ===
output_file = "docs/daily/20261012_每日新闻洞察.html"
result = gen.publish(output_file)
print(f"OK 报告已生成: {result}")
if result.get("success"):
    import shutil
    shutil.copy(output_file, "docs/daily/latest.html")
    print(f"LATEST 已更新 latest.html")
    print(f"SIZE 文件大小: {result.get('file_size')} 字节")
else:
    print(f"ERROR 验证失败: {result.get('errors')}")
