import sys, os
sys.path.insert(0, os.path.join(os.getcwd(), "v3"))
os.chdir('/root/daily-news-insight')

from v3.generators.tomorrow_catalyst import TomorrowCatalystGenerator

gen = TomorrowCatalystGenerator(
    date_str="20261006",
    subtitle="2026.10.06 · 假期催化周报 | 节后前瞻版"
)

# ===== 1. 明日核心催化 =====
key_catalyst_text = """
<strong>节后首交易日前瞻</strong>A股将于10月8日（周四）迎来国庆后首个交易日。假期期间海外市场整体偏暖：
<span style="color:#4ade80;">美股纳指创历史新高，美光财报超预期提振半导体板块；</span>
<span style="color:#4ade80;">日本股市大涨2.5%，日本1400亿美元数据中心投资计划引爆AI算力主题；</span>
<span style="color:#4ade80;">美联储9月非农爆冷（仅增2.9万 vs 预期9万），10月加息概率骤降至22%；</span>
<span style="color:#fbbf24;">中东局势反复，油价波动加剧，需警惕能源链扰动；</span>
<span style="color:#f97316;">节后三季报密集披露窗口开启，业绩验证成为核心主线。</span>
<br><br>
<strong>10月6日焦点事件：</strong>美联储官员密集发声 + 港股正常交易 + 节前政策红利（购房贴息/PSL降息/科技创新再贷款）持续发酵。
节后操作建议：科技成长为主线（AI算力/半导体/液冷），红利资产做底仓，关注三季报业绩超预期方向。
"""
gen.add_key_catalyst(key_catalyst_text)

# ===== 2. 本周事件日历 =====
events = [
    {"type": "data", "title": "美国8月JOLTS职位空缺数", "description": "北京时间10月6日22:00公布，非农爆冷后就业数据持续受关注，若继续走弱将强化美联储暂停加息预期", "category": "海外经济"},
    {"type": "data", "title": "美国9月ISM非制造业PMI", "description": "10月6日22:00公布，服务业PMI是美国经济韧性的核心指标，前值52.8，预期52.5", "category": "海外经济"},
    {"type": "meeting", "title": "微软与英伟达RTX Spark发布会", "description": "10月7日凌晨（北京时间）微软与黄仁勋联合发布RTX Spark平台及6款创作向Windows新品，Grace CPU+Blackwell GPU统一内存架构，利好AI PC产业链", "category": "科技新品"},
    {"type": "data", "title": "美联储9月会议纪要", "description": "北京时间10月8日凌晨2点公布，9月美联储全票通过加息25bp至3.75%-4.00%，市场关注后续加息路径及中性利率讨论", "category": "海外政策"},
    {"type": "general", "title": "A股国庆后首个交易日", "description": "10月8日周四A股开市，港股通同步恢复。历史数据显示国庆后上涨胜率超60%，节后资金回流+政策预期驱动", "category": "市场日历"},
    {"type": "data", "title": "欧洲央行9月会议纪要", "description": "10月8日周四公布，9月欧央行加息应对能源推动的通胀上行，关注10月加息可能性指引", "category": "海外政策"},
    {"type": "general", "title": "新股申购：通则康威(301718)", "description": "10月9日申购，宽带连接终端设备龙头，发行3645万股，申购上限1万股，中信建投保荐", "category": "新股日历"},
    {"type": "earnings", "title": "三季报披露大幕开启", "description": "10月15日起三季报正式披露，节后前10个交易日134家公司率先披露，集中于电子/化工/医药/有色行业", "category": "业绩季"},
    {"type": "meeting", "title": "2026金融街论坛年会预热", "description": "10月19-22日在北京举办，主题为开放合作包容共筑全球金融发展新生态，40多国400位嘉宾出席，金融政策预期催化", "category": "重要会议"},
    {"type": "meeting", "title": "美国SEMICON West半导体展", "description": "10月13-15日旧金山举办，全球半导体设备和材料年度盛会，AI芯片需求与先进封装技术为核心看点", "category": "行业大会"},
    {"type": "general", "title": "10月限售股解禁洪峰", "description": "10月全月解禁市值超3100亿元，138家公司解禁，西安奕材（764亿）、中船特气（733亿）居前两位，合计占比48%", "category": "解禁日历"},
    {"type": "meeting", "title": "OCP Global Summit 2026", "description": "10月12-15日圣何塞举办，三星/英伟达/Lumentum等展示AI基础设施方案，光模块和CPO主题催化", "category": "行业大会"},
]
gen.add_events_calendar(events)

# ===== 3. 重要数据发布 =====
data_list = [
    {"name": "美国9月非农就业", "prev": "16.2万(8月)", "expect": "9万", "actual": "2.9万(爆冷)"},
    {"name": "美联储9月会议纪要", "prev": "加息25bp", "expect": "年内或再加息1次", "actual": "10/8凌晨公布"},
    {"name": "美国ISM非制造业PMI", "prev": "52.8(8月)", "expect": "52.5", "actual": "10/6 22:00"},
    {"name": "中国9月CPI/PPI", "prev": "CPI+0.8%/PPI+3.8%", "expect": "CPI约+0.9%", "actual": "10/14公布"},
    {"name": "中国9月社融/M2", "prev": "8月新增1.9万亿", "expect": "约2.3万亿", "actual": "10月中旬公布"},
    {"name": "中国三季度GDP", "prev": "上半年+5.3%", "expect": "约+5.2%", "actual": "10/19公布"},
]
gen.add_data_release(data_list)

# ===== 4. 业绩预告 =====
earnings_stocks = [
    {"name": "芯联集成-U", "code": "688469", "type": "三季报预增", "eps": "0.52元", "growth": "+扭亏(+6.81亿)"},
    {"name": "力勤资源", "code": "001246", "type": "三季报预增", "eps": "-", "growth": "+近60%"},
    {"name": "贝特利", "code": "839580", "type": "三季报预增", "eps": "-", "growth": "+超50%"},
    {"name": "富祥股份", "code": "300497", "type": "三季报扭亏", "eps": "-", "growth": "+扭亏(3.5-4.3亿)"},
    {"name": "世纪数码", "code": "301153", "type": "三季报预增", "eps": "-", "growth": "+近48%"},
    {"name": "安达科技", "code": "830809", "type": "三季报扭亏", "eps": "-", "growth": "+扭亏(1.7-2.2亿)"},
]
gen.add_earnings_announcements(earnings_stocks)

# ===== 5. 限售股解禁重点 =====
from components.layout import Section, CardGrid
from components.data import StatCard

jiejin_cards = [
    StatCard(title="中国神华(601088)", value="218.76亿", subtitle="10/8解禁 定增机构配售 占比2.1%", icon="trending-down", variant="danger"),
    StatCard(title="中国能建(601868)", value="254.90亿", subtitle="10/8解禁 定增机构配售 占比5.8%", icon="trending-down", variant="danger"),
    StatCard(title="哈尔斯(002615)", value="9.35亿", subtitle="10/8解禁 定增机构配售 占比16.7%", icon="trending-down", variant="warning"),
    StatCard(title="西安奕材(688290)", value="763.68亿", subtitle="10/28解禁 首发原股东 占比70.3%", icon="alert-triangle", variant="danger"),
    StatCard(title="中船特气(688146)", value="732.98亿", subtitle="10月解禁 首发原股东 占比72.6%", icon="alert-triangle", variant="danger"),
    StatCard(title="陕西能源(001286)", value="226.08亿", subtitle="10月解禁 首发原股东 占比57%", icon="alert-triangle", variant="warning"),
]
jiejin_grid = CardGrid(jiejin_cards, cols=3)
jiejin_section = Section(title="限售股解禁重点标的", content=jiejin_grid.render(), icon="unlock", variant="dark")
gen._components.append(jiejin_section)

# 解禁影响分析
jiejin_impact = """
<div style="line-height: 1.8; color: #e2e8f0; font-size: 14px;">
<strong>解禁结构分析：</strong>
<ul style="margin: 8px 0; padding-left: 20px;">
<li><strong>节后首日（10/8）解禁压力集中：</strong>中国能建（255亿）、中国神华（219亿）两大央企定增解禁合计超470亿，是节后首个交易日最大供给冲击。但需注意：定增机构有持仓成本，且央企股东减持意愿通常较低，实际抛压可能小于账面规模。</li>
<li><strong>10月下旬是真正洪峰：</strong>10月23-29日多个交易日集中释放大额首发原股东限售股，西安奕材（764亿）+中船特气（733亿）两只科创板巨无霸合计近1500亿，占10月全月解禁规模的48%。这两家均为半导体产业链核心标的（碳化硅衬底/电子特气），解禁前需警惕筹码供给增加对估值的压制。</li>
<li><strong>高比例解禁标的风险清单：</strong>泰凯英(73.6%)、天元智能(73.5%)、长江能科(73.3%)、中船特气(72.6%)、西安奕材(70.3%)——解禁比例超过70%的5家公司流通盘将大幅扩容，短期供需失衡风险需警惕。</li>
<li><strong>操作策略：</strong>对解禁比例超30%且估值偏高的次新股，解禁前1-2周宜降低仓位观望；对解禁股东以央企/产业资本为主、基本面优质的标的，反而可能存在利空出尽后的布局机会。</li>
</ul>
</div>
"""
jiejin_analysis_section = Section(title="解禁影响深度分析", content=jiejin_impact, icon="file-text")
gen._components.append(jiejin_analysis_section)

# ===== 6. 市场影响分析 =====
impact_text = """
<h3 style="color:#fbbf24; margin-bottom: 12px;">节后市场五大核心变量</h3>

<strong style="color:#4ade80;">海外风险偏好修复</strong><br>
国庆假期前4天海外市场整体利好：美股纳指创历史新高、日经225大涨超2.5%、黄金白银全线走高。核心驱动力是9月非农数据爆冷（仅增2.9万 vs 预期9万），市场对美联储10月加息概率从约50%骤降至22%。美债收益率从高位回落，全球流动性压力边际缓解。这为A股节后开门红提供了有利的外部环境。
<br><br>

<strong style="color:#4ade80;">节前政策组合拳持续发酵</strong><br>
9月底政策密集出台：(a)财政部/央行/金融监管总局联合推出居民购房贷款贴息政策（最高100万额度、年化贴息1%、最长5年），10月1日起实施；(b)央行下调PSL利率0.25个百分点、扩大支持领域；(c)增加科技创新和技术改造再贷款2000亿元、支持比例从60%提至100%；(d)增加支农支小再贷款5000亿元。政策从稳地产、稳投资、稳科技、稳小微四个维度发力，政策底信号明确。节后地产链、科技成长有望率先反应。
<br><br>

<strong style="color:#fbbf24;">三季报验证期开启</strong><br>
节后市场将从估值博弈转向业绩真实兑现。截至目前已有近40家公司披露三季报预告，预喜率约68%。亮点集中在：半导体（芯联集成扭亏、高凯技术+37%）、新能源材料（富祥股份电解液添加剂扭亏、安达科技磷酸铁锂扭亏）、出海链（力勤资源镍产业链+近60%）。但需注意，科技板块前期涨幅较大，业绩能否消化高估值是关键考验，三季不及预期的标的可能面临戴维斯双杀。
<br><br>

<strong style="color:#f97316;">中东局势与油价波动</strong><br>
假期期间中东局势反复：胡塞武装袭击沙特阿美设施、沙特东西输油管道遭袭传闻引发油价剧烈波动。布油在100美元/桶上方震荡，WTI在90美元附近。能源价格持续高位将推升全球通胀预期，制约央行降息空间，并对化工、交运等下游行业盈利形成挤压。需持续关注中东事态发展。
<br><br>

<strong style="color:#8b5cf6;">AI算力产业催化密集</strong><br>
节后AI算力方向催化剂密集：(a)10月7日微软与英伟达RTX Spark发布会（黄仁勋出席）；(b)10月12-15日OCP Global Summit（光模块/CPO方向）；(c)10月13-15日美国SEMICON West半导体展；(d)日本1400亿美元数据中心投资计划。叠加美光财报超预期验证存储周期复苏，AI算力产业链有望成为节后最强主线。
"""
gen.add_impact_analysis(impact_text)

# ===== 7. 催化深度分析 =====
deep_analysis_events = [
    {"title": "美联储9月会议纪要", "type": "data", "description": "10月8日凌晨公布，非农爆冷后会议纪要的鹰鸽倾向将决定10月加息预期走向", "category": "海外政策/加息"},
    {"title": "微软与英伟达RTX Spark发布会", "type": "meeting", "description": "10月7日黄仁勋与微软联合发布RTX Spark平台及6款新品，Grace+Blackwell统一内存架构，AI PC新标杆", "category": "科技新品/AI算力"},
    {"title": "A股节后首个交易日+三季报窗口", "type": "general", "description": "10月8日A股开市，叠加三季报披露窗口开启，业绩验证+节后资金回流将决定十月行情方向", "category": "市场日历/业绩季"},
]
gen.add_catalyst_deep_analysis(deep_analysis_events)

# ===== 8. 风险提示 =====
risks = [
    "中东局势升级导致油价飙升，推升全球通胀并制约央行政策空间",
    "美联储会议纪要偏鹰派，10月加息预期重新升温",
    "三季报业绩不及预期，高估值科技板块面临回调压力",
    "10月下旬限售股解禁洪峰（近1500亿科创板解禁）冲击市场流动性",
    "美债收益率再度上行，压制全球风险资产估值",
    "国内房地产销售数据不及预期，政策效果存疑",
]
gen.add_risk_warning(risks)

# ===== 发布 =====
result = gen.publish(
    title="明日催化剂",
    filename="20261006_明日催化剂.html",
    excerpt="国庆假期特辑·节后前瞻：美联储会议纪要/英伟达RTX发布会/三季报窗口开启/AI算力催化密集"
)
print("发布结果:", result)
