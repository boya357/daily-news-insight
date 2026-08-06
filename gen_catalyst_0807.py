import sys, os
sys.path.insert(0, 'v3')
os.chdir('/root/daily-news-insight')

from generators.tomorrow_catalyst import TomorrowCatalystGenerator

gen = TomorrowCatalystGenerator(date_str="20260807", subtitle="2026.08.07 · 明日催化剂")

# ====== 1. 明日核心催化 ======
key_catalyst = """
<strong>8月7日（周五）四大核心催化事件</strong>
<ul>
<li>🔥 <strong>美国7月非农就业报告</strong>（北京时间20:30）：美联储7月议息会议后首份完整就业数据，3票加息分歧背景下，直接决定9月利率路径预期，全球资产定价锚点</li>
<li>🤖 <strong>马斯克Grok 4.6大模型发布</strong>：参数规模1.5万亿，重点优化监督微调与强化学习，SpaceX工程数据首次注入训练，AI算力与应用链迎情绪催化</li>
<li>🔬 <strong>第27届电子封装技术国际会议（ICEPT 2026）闭幕日</strong>：Chiplet先进封装、2.5D/3D封装、HBM等前沿技术最新进展，先进封装成A股新主线</li>
<li>📈 <strong>科创板新股频准激光申购</strong>（688826）：发行价186.88元/股为年内最贵，量子科技+半导体精准激光光源，战略配售获中微半导体、佰维存储、先导智能等产业资本加持</li>
</ul>
"""
gen.add_key_catalyst(key_catalyst)

# ====== 2. 事件日历 ======
events = [
    # 数据发布
    {'type': 'data', 'title': '美国7月非农就业报告（NFP）', 'description': '北京时间8月7日20:30公布，市场预期新增约8万人，失业率4.3%，将直接影响美联储9月利率决议预期', 'category': '宏观数据'},
    {'type': 'data', 'title': '中国7月外汇储备', 'description': '8月7日公布，6月为3.416万亿美元，关注黄金储备增持节奏（已连续20个月增持）', 'category': '宏观数据'},
    {'type': 'data', 'title': '中国7月贸易帐（进出口数据）', 'description': '海关总署公布7月外贸数据，关注高技术制造、"新三样"出口增速及对东盟、一带一路国家贸易份额', 'category': '宏观数据'},
    {'type': 'data', 'title': '美国7月失业率与平均时薪', 'description': '与非农同步公布，平均时薪增速反映工资通胀压力，直接关联美联储政策走向', 'category': '宏观数据'},
    # 重要会议
    {'type': 'meeting', 'title': '第27届电子封装技术国际会议（ICEPT 2026）', 'description': '8月5-7日在西安举行，聚焦Chiplet、2.5D/3D封装、HBM、CPO、混合键合等前沿技术，预计2000名专业观众', 'category': '半导体会议'},
    {'type': 'meeting', 'title': '2026中国品牌节', 'description': '8月7-10日在北京举办，主题"出海与生态"，2万人次参会，200+演讲嘉宾，发布世界品牌500强等榜单', 'category': '品牌盛会'},
    {'type': 'meeting', 'title': '镇江科创大会暨第四届金山英才周启幕', 'description': '8月7日启动，8月8日主活动，发布创新转型"九项工程"和人才"镇兴"行动2.0版，2000人规模', 'category': '科创人才'},
    # 业绩公告
    {'type': 'earnings', 'title': '存储巨头财报落地后的市场反应', 'description': '闪迪、西部数据8月6日盘后发布Q2财报，存储板块全球暴跌背景下关注8月7日A股映射，NAND闪存价格趋势成焦点', 'category': '海外财报'},
    {'type': 'earnings', 'title': 'A股中报披露持续进行', 'description': '寒武纪、药明康德、百济神州、中国稀土、立昂微等半导体重磅标的本周陆续披露中报', 'category': 'A股财报'},
    # 综合事件
    {'type': 'general', 'title': 'Grok 4.6大模型发布', 'description': '马斯克xAI预计8月7日发布Grok 4.6，1.5万亿参数，SFT与RL显著提升，后续Grok 4.7（2.1万亿参数）数周后推出', 'category': 'AI大模型'},
    {'type': 'general', 'title': '科创板新股频准激光网上申购', 'description': '申购代码787826，发行价186.88元/股，发行市值74.75亿元，量子科技+半导体精准激光赛道', 'category': '新股申购'},
    {'type': 'general', 'title': 'SpaceX解禁后市场表现', 'description': '8月6日SpaceX约9.1亿股内部股解禁，规模远超6.4亿股公众流通盘，关注对美股科技股情绪传导', 'category': '海外市场'},
]
gen.add_events_calendar(events)

# ====== 3. 限售股解禁详情 ======
earnings_stocks = [
    {'name': '通行宝', 'code': '301339', 'type': '股权激励解禁', 'growth': '343.77万股（0.59%）'},
    {'name': '海星股份', 'code': '603399', 'type': '限售股解禁', 'growth': '周五解禁'},
    {'name': '奥精医疗', 'code': '301091', 'type': '限售股解禁', 'growth': '周五解禁'},
    {'name': '狄耐克', 'code': '300884', 'type': '限售股解禁', 'growth': '周五解禁'},
    {'name': '中农立华', 'code': '603070', 'type': '限售股解禁', 'growth': '周五解禁'},
]
gen.add_earnings_announcements(earnings_stocks)

# ====== 4. 重要数据发布 ======
data_list = [
    {'name': '美国7月非农就业（万人）', 'prev': '14.7（下修至1.4）', 'expect': '约8.0', 'actual': '待公布'},
    {'name': '美国7月失业率', 'prev': '4.1%', 'expect': '4.2-4.3%', 'actual': '待公布'},
    {'name': '美国7月平均时薪（YoY）', 'prev': '3.8%', 'expect': '3.8-3.9%', 'actual': '待公布'},
    {'name': '中国7月外汇储备（亿美元）', 'prev': '34160', 'expect': '约34000', 'actual': '待公布'},
    {'name': '中国7月出口同比', 'prev': '前值高位', 'expect': '关注增速变化', 'actual': '待公布'},
    {'name': '中国7月进口同比', 'prev': '前值', 'expect': '关注内需修复', 'actual': '待公布'},
]
gen.add_data_release(data_list)

# ====== 5. 市场影响深度分析 ======
impact_analysis = """
<h3 style="color:#f1f5f9; margin-bottom:12px;">一、美国非农：全球风险资产定价的"总闸门"</h3>
<p style="margin-bottom:12px;">7月美联储议息会议以9:3票维持利率3.50%-3.75%不变，出现三张加息异议票，为2016年以来最分裂的一次决议。在此背景下，8月7日公布的7月非农就业数据成为市场判断美联储9月政策路径的最关键依据。</p>
<p style="margin-bottom:12px;">市场预期新增非农约8万人，失业率升至4.3%。若实际数据<strong>低于预期（如低于5万）</strong>，则将强化经济降温叙事，9月降息预期升温，美元走弱、美债收益率下行、成长股估值修复，A股科技成长板块（AI算力、半导体）将迎来喘息窗口；若<strong>超预期强劲</strong>，则三票加息异议的合理性被印证，市场可能重新定价加息路径，全球风险资产承压。</p>
<p style="margin-bottom:16px;">特别关注平均时薪增速——若工资通胀粘性超预期，即便就业数据走弱，美联储"higher for longer"立场仍将维持。对持仓影响：<strong>英维克（液冷）、雅克科技（半导体材料）</strong>均属AI算力链，对海外利率高度敏感，需警惕非农超预期带来的估值压制。</p>

<h3 style="color:#f1f5f9; margin-bottom:12px;">二、Grok 4.6发布：AI大模型竞赛"军备竞赛"再升级</h3>
<p style="margin-bottom:12px;">马斯克xAI预计8月7日发布Grok 4.6，参数规模1.5万亿，重点优化监督微调（SFT）和强化学习（RL）。更重要的是，SpaceX全量工程数据将首次注入Grok训练语料，涵盖制造工艺、材料科学、Starlink硬件设计等领域，目标是打造"世界最强工程师型AI"。</p>
<p style="margin-bottom:12px;">对A股的影响路径有三：<strong>（1）算力需求验证</strong>——大模型参数持续膨胀印证AI算力长期景气，液冷（英维克）、PCB、光模块等算力基建产业链需求有支撑；<strong>（2）国产大模型映射</strong>——海外头部模型迭代加速，倒逼国产大模型厂商加大投入，AI芯片（寒武纪、海光信息）、AI应用等板块情绪受益；<strong>（3）工程AI新方向</strong>——SpaceX数据注入开创"工业工程数据训练大模型"先河，工业软件、智能制造、机器人等板块或迎新叙事。</p>
<p style="margin-bottom:16px;">操作建议：Grok 4.6若性能超预期，短期AI算力链（英维克、雅克科技）有望迎来情绪修复；若不及预期，需警惕AI板块整体回调风险。本周存储板块暴跌已造成科技股情绪承压，需关注Grok发布能否成为新的情绪催化剂。</p>

<h3 style="color:#f1f5f9; margin-bottom:12px;">三、先进封装主线：ICEPT会议叠加Chiplet产业趋势</h3>
<p style="margin-bottom:12px;">第27届电子封装技术国际会议（ICEPT 2026）8月5-7日在西安举行，这是亚洲规模最大的封装技术国际盛会，预计2000名专业观众参会。会议聚焦Chiplet异构集成、2.5D/3D封装、HBM、CPO、混合键合等前沿方向，正值A股先进封装/半导体材料成为新主线的关键窗口。</p>
<p style="margin-bottom:12px;">在存储板块全球暴跌（闪迪/西数盘后大跌、韩股暴跌）的背景下，资金正在从纯存储概念向<strong>先进封装、半导体材料、半导体设备</strong>等细分方向切换。ICEPT会议上的技术突破和产业动向有望成为新的催化点。</p>
<p style="margin-bottom:16px;">持仓相关：<strong>雅克科技（002409）</strong>是半导体材料龙头，覆盖前驱体、光刻胶、电子特气等品类，深度受益先进封装产业链扩张；<strong>铜冠铜箔（301217）</strong>的铜箔产品在封装基板等领域有应用，先进封装渗透率提升将带动高端铜箔需求增长。建议重点关注会议期间Chiplet相关技术进展的报道。</p>

<h3 style="color:#f1f5f9; margin-bottom:12px;">四、存储板块暴跌后的传导与应对</h3>
<p style="margin-bottom:12px;">8月6日存储板块全球暴跌——闪迪、西部数据盘后大跌，韩国存储股重挫，市场对存储周期见顶的担忧急剧升温。导火索是TrendForce集邦咨询报告显示DRAM现货价格上涨势头自7月下旬以来有所减弱，叠加FMS 2026闪存峰会后市场对HBM需求节奏的重新评估。</p>
<p style="margin-bottom:12px;">但需要注意的是：<strong>存储周期并未结束</strong>，三大内存原厂已基本完成2027年产能分配谈判，供应紧张态势预计持续至2027年。本轮下跌更多是前期涨幅过大后的回调，以及对短期现货价格波动的过度反应。</p>
<p style="margin-bottom:16px;">对持仓的影响：雅克科技作为上游材料供应商，受存储价格波动的直接影响相对较小，反而在行业扩产周期中持续受益；铜冠铜箔需关注存储板块情绪传导带来的短期波动。操作上不宜盲目杀跌，可利用回调机会逢低布局基本面扎实的半导体材料标的。</p>

<h3 style="color:#f1f5f9; margin-bottom:12px;">五、频准激光申购：量子科技+半导体国产化的硬科技标的</h3>
<p style="margin-bottom:12px;">8月7日科创板新股频准激光（688826）开启网上申购，发行价186.88元/股为2026年以来最贵新股，发行市盈率49.42倍（低于行业均值68.04倍），发行市值74.75亿元。公司主营精准激光器，应用于量子计算、量子精密测量及晶圆制造/量检测/隐切等半导体领域。</p>
<p style="margin-bottom:12px;">亮点：（1）战略配售获产业资本集体加持——中微半导体、佰维存储、先导智能、德龙激光、京东方创新投资等均参与战略配售，彰显产业认可度；（2）毛利率高达69.33%，远超普通工业激光器企业，体现精准激光的高技术壁垒；（3）2023-2025年营收复合增速68%，半导体领域收入复合增速103.8%，成长动能强劲。</p>
<p style="margin-bottom:16px;">申购建议：作为年内最贵新股，单签金额较高（500股约9.34万元），但考虑到其科创属性强、发行市盈率低于行业、新股首日赚钱效应持续，<strong>建议积极申购</strong>。对半导体设备/材料板块有情绪催化作用。</p>

<h3 style="color:#f1f5f9; margin-bottom:12px;">六、限售股解禁：整体压力较小，关注股权激励性质</h3>
<p style="margin-bottom:12px;">8月7日（周五）限售股解禁规模较小，主要标的包括：通行宝（301339）343.77万股股权激励解禁（占总股本0.59%）、海星股份（603399）、奥精医疗（301091）、狄耐克（300884）、中农立华（603070）等。整体解禁市值远低于周一周二的高峰日（浙江荣泰95亿元、麦格米特32亿元）。</p>
<p style="margin-bottom:16px;">8月全月解禁市值约1113.75亿元，为全年最低水平，市场整体解禁压力较轻。持仓股中<strong>*ST建艺（002789）</strong>本周无解禁安排，无需担忧。</p>
"""
gen.add_impact_analysis(impact_analysis)

# ====== 6. 催化深度分析（Skill增强） ======
deep_events = [
    {'title': '美国7月非农就业报告', 'type': 'data', 'description': '全球风险资产定价锚点，决定美联储9月政策路径', 'category': '宏观数据'},
    {'title': 'Grok 4.6大模型发布', 'type': 'general', 'description': 'AI大模型军备竞赛升级，SpaceX工程数据首次注入训练', 'category': 'AI大模型'},
    {'title': '先进封装ICEPT会议', 'type': 'meeting', 'description': 'Chiplet先进封装技术风向标，A股半导体新主线催化剂', 'category': '半导体会议'},
]
gen.add_catalyst_deep_analysis(deep_events)

# ====== 7. 风险提示 ======
risks = [
    "美国非农数据超预期强劲，引发美联储加息预期升温，全球风险资产承压",
    "存储板块暴跌情绪持续扩散，半导体板块整体回调风险",
    "Grok 4.6发布不及预期，AI板块情绪降温",
    "SpaceX解禁后抛压加剧，美股科技股波动向A股传导",
    "国内7月贸易数据不及预期，出口链承压",
    "先进封装概念短期涨幅过大，存在获利回吐风险",
    "持仓股*ST建艺（002789）存在退市风险警示标的的不确定性",
    "本报告仅供参考，不构成投资建议，入市有风险，投资需谨慎",
]
gen.add_risk_warning(risks)

# ====== 生成并发布 ======
result = gen.publish(title="明日催化剂 2026.08.07", filename="20260807_明日催化剂.html")
print("发布结果：", result)
