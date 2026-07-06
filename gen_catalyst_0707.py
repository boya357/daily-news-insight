#!/usr/bin/env python3
"""明日催化剂生成脚本 - 2026年7月7日（周二）"""
import sys, os
sys.path.insert(0, 'v3')
os.chdir('/root/daily-news-insight')

from v3.generators.tomorrow_catalyst import TomorrowCatalystGenerator
from components.layout import Section

gen = TomorrowCatalystGenerator(
    date_str="20260707",
    subtitle="2026.07.07 · 明日催化剂"
)

# ========== 核心催化剂 ==========
gen.add_key_catalyst("""
<div style="line-height:1.9;">
<p><strong style="color:#ef4444;">&#128293; S级：三星Q2初步财报+存储涨价双验证</strong> — 三星电子将于7月7日发布Q2初步财报，市场预期营业利润约86万亿韩元（同比暴增约18倍），有望超越英伟达Q1创下全球科技企业单季营业利润历史最高纪录。叠加DRAM三季度涨价20%预期，将直接映射A股存储/半导体板块。<br>
<span style="color:#6b7280;font-size:12px;">来源：新浪港股、华尔街见闻（2026-07-06）</span></p>

<p><strong style="color:#ef4444;">&#128293; S级：OpenAI发布GPT-5.6，AI算力需求再催化</strong> — OpenAI计划7月7日发布GPT-5.6三大子模型（Sol/Terra/Luna），引入"速度拨盘"功能，精准卡位Claude Fable 5限额失效真空期。Sol Ultra编程测试达91.9%，性能对标Fable 5但价格更低，AI大模型军备竞赛升级，利好算力/液冷/光模块链。<br>
<span style="color:#6b7280;font-size:12px;">来源：36氪、华尔街见闻（2026-07-06）</span></p>

<p><strong style="color:#f59e0b;">&#9889; A级：SpaceX纳入纳斯达克100指数</strong> — SpaceX将于7月7日美股开盘前正式纳入纳指100，上市仅15天创最快纳入纪录。预计带来43-270亿美元被动资金强制买入，商业航天/卫星互联网板块有望获外围情绪映射。<br>
<span style="color:#6b7280;font-size:12px;">来源：界面新闻、新浪财经（2026-07-06）</span></p>

<p><strong style="color:#f59e0b;">&#9889; A级：欧洲首届物理AI/具身智能峰会MACHINA Summit</strong> — 7月7日在巴黎召开，为7月全球人形机器人海外最高规格场，特斯拉、优必选、智元等量产节奏有望披露，催化国内人形机器人板块情绪。<br>
<span style="color:#6b7280;font-size:12px;">来源：财联社（2026-07-05）</span></p>
</div>
""")

# ========== 明日事件日历 ==========
events = [
    {
        'type': 'data',
        'title': '中国6月外汇储备数据公布',
        'description': '国家外汇管理局7月7日公布6月外汇储备数据。中国央行已连续19个月增持黄金，关注外储规模变化及黄金储备动向。',
        'category': '宏观数据'
    },
    {
        'type': 'policy',
        'title': 'USTR举行对60国加征关税公开听证会',
        'description': '美国贸易代表办公室（USTR）7月7日举行公开听证会，审议以"未禁止进口强迫劳动产品"为由对全球60个经济体征收额外关税方案。贸易摩擦新变量，关注全球风险偏好扰动。',
        'category': '贸易政策'
    },
    {
        'type': 'meeting',
        'title': '北约峰会（安卡拉，7月7-8日）',
        'description': '北约峰会在土耳其安卡拉举行，俄乌冲突、防务支出、亚太安全议题为核心关注。地缘风险或阶段性升温，利好军工/黄金避险板块。',
        'category': '国际会议'
    },
    {
        'type': 'meeting',
        'title': '太阳谷峰会开幕（7月7-10日）',
        'description': '艾伦公司太阳谷峰会开幕，苹果库克、亚马逊贝索斯、Meta扎克伯格、OpenAI奥特曼等科技巨头出席，马斯克、黄仁勋缺席。关注AI产业方向信号。',
        'category': '产业会议'
    },
    {
        'type': 'meeting',
        'title': 'MACHINA Summit欧洲物理AI/具身智能峰会',
        'description': '欧洲首届专属物理AI/具身智能峰会在巴黎举办，7月全球机器人/人形机器人海外最高规格场，特斯拉、优必选、智元等有望披露量产节奏与零部件招标进展。',
        'category': '产业会议'
    },
    {
        'type': 'meeting',
        'title': '上海市政府发布会：WAIC 2026筹备进展',
        'description': '上海市政府举行发布会，介绍2026世界人工智能大会（7月17-20日）筹备进展。WAIC聚焦"智能伙伴，共创未来"，具身智能、世界模型、AI for Science为核心议题。',
        'category': '国内会议'
    },
    {
        'type': 'general',
        'title': '卓然股份复牌被实施退市风险警示（*ST卓然）',
        'description': '卓然股份(688121)因无法在法定期限内完成2025年年报披露，7月7日复牌并被实施退市风险警示，简称变更为"*ST卓然"，涨跌幅限制仍为20%。',
        'category': '个股风险'
    },
]
gen.add_events_calendar(events)

# ========== 业绩公告 ==========
gen.add_earnings_announcements([
    {'name': '容百科技', 'code': '688005', 'type': '半年报预告', 'growth': '扭亏为盈 净利1.0-1.2亿'},
    {'name': '华源控股', 'code': '002787', 'type': '半年报预告', 'growth': '+50.5%~+85.6%'},
    {'name': '国风新材', 'code': '000859', 'type': '半年报预告', 'growth': '亏损2800-3800万（减亏）'},
    {'name': '江波龙', 'code': '301308', 'type': '半年报预告', 'growth': '+62204%~+74394%（已发）'},
    {'name': '永鼎股份', 'code': '600105', 'type': '半年报预告', 'growth': '+57%~+120%（已发）'},
    {'name': '招商轮船', 'code': '601872', 'type': '半年报预告', 'growth': '+214%~+248%（已发）'},
])

# ========== 数据发布 ==========
gen.add_data_release([
    {'name': '中国6月外汇储备', 'prev': '32863亿美元（5月）', 'expect': '基本稳定', 'actual': '待公布'},
    {'name': '美国5月贸易帐', 'prev': '-1222亿美元', 'expect': '待公布', 'actual': '美东时间周二'},
    {'name': '韩国6月外汇储备', 'prev': '—', 'expect': '—', 'actual': '同日公布'},
])

# ========== 限售股解禁 ==========
unlock_html = """
<div style="overflow-x:auto;">
<table style="width:100%;border-collapse:collapse;font-size:13px;">
<thead>
<tr style="background:rgba(239,68,68,0.1);color:#fca5a5;">
<th style="padding:8px;text-align:left;border-bottom:1px solid rgba(255,255,255,0.1);">代码</th>
<th style="padding:8px;text-align:left;border-bottom:1px solid rgba(255,255,255,0.1);">简称</th>
<th style="padding:8px;text-align:right;border-bottom:1px solid rgba(255,255,255,0.1);">解禁数量(万股)</th>
<th style="padding:8px;text-align:right;border-bottom:1px solid rgba(255,255,255,0.1);">占总股本%</th>
<th style="padding:8px;text-align:left;border-bottom:1px solid rgba(255,255,255,0.1);">类型</th>
</tr>
</thead>
<tbody>
<tr style="border-bottom:1px solid rgba(255,255,255,0.05);">
<td style="padding:8px;color:#fbbf24;">300013</td>
<td style="padding:8px;color:#fbbf24;font-weight:600;">新宁物流</td>
<td style="padding:8px;text-align:right;color:#fbbf24;">11167</td>
<td style="padding:8px;text-align:right;color:#fbbf24;">20.00%</td>
<td style="padding:8px;">大额解禁（大河控股定增）</td>
</tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.05);">
<td style="padding:8px;">002688</td>
<td style="padding:8px;">金河生物</td>
<td style="padding:8px;text-align:right;">432.6</td>
<td style="padding:8px;text-align:right;">0.56%</td>
<td style="padding:8px;">定增</td>
</tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.05);">
<td style="padding:8px;">605298</td>
<td style="padding:8px;">必得科技</td>
<td style="padding:8px;text-align:right;">146.3</td>
<td style="padding:8px;text-align:right;">0.78%</td>
<td style="padding:8px;">首发</td>
</tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.05);">
<td style="padding:8px;">000534</td>
<td style="padding:8px;">万泽股份</td>
<td style="padding:8px;text-align:right;">162.5</td>
<td style="padding:8px;text-align:right;">0.32%</td>
<td style="padding:8px;">定增</td>
</tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.05);">
<td style="padding:8px;">600662</td>
<td style="padding:8px;">外服控股</td>
<td style="padding:8px;text-align:right;">29.1</td>
<td style="padding:8px;text-align:right;">0.01%</td>
<td style="padding:8px;">定增</td>
</tr>
</tbody>
</table>
</div>
<p style="margin-top:10px;font-size:12px;color:#9ca3af;">重点关注：<strong style="color:#fbbf24;">新宁物流</strong>解禁1.12亿股占总股本20%，大河控股定增股份解禁，盈利质量待提升，需警惕抛压；其余个股解禁比例较小。</p>
<p style="font-size:12px;color:#9ca3af;">来源：中财网、财联社、东方财富（2026-07-06）</p>
"""
unlock_section = Section(title="&#128275; 7月7日限售股解禁", content=unlock_html, icon="unlock")
gen._components.append(unlock_section)

# ========== 持仓关联诊断 ==========
portfolio_html = """
<div style="line-height:1.9;">
<p style="color:#ef4444;font-weight:700;font-size:15px;">&#128680; 持仓紧急操作指引（7月7日周二）</p>

<p><strong style="color:#fbbf24;">铜冠铜箔（301217）</strong>：今日高开159.98后暴跌至143元，振幅15.95%，典型高位出货形态，移动止盈150已破。<br>
<strong style="color:#ef4444;">明日策略</strong>：若不能快速收复150，继续减至1/3以下。三星Q2业绩暴增若带动存储/半导体情绪修复，反弹至150-155区间为减仓窗口。</p>

<p><strong style="color:#fbbf24;">雅克科技（002409）</strong>：连续三日累跌-17.5%，200元整数关失守，12.88%天量换手机构加速兑现。<br>
<strong style="color:#ef4444;">明日策略</strong>：底仓保留1/2，180为关键支撑，破则继续减仓。半导体前驱体赛道高位兑现压力大，三星财报若证伪HBM景气度将加速下跌。</p>

<p><strong style="color:#f87171;">英维克（002837）</strong>：今日+3.68%相对抗跌，反弹至76.99后回落，换手率5.77%，仍属超跌反弹性质。<br>
<strong style="color:#f59e0b;">明日策略</strong>：75-77区间继续减仓，OpenAI GPT-5.6发布若带动算力情绪，反弹高度或达77-80区间，珍惜减仓窗口。</p>

<p><strong style="color:#ef4444;">*ST建艺（002789）</strong>：ST涨跌幅扩至10%首日继续下跌-3.49%至11.33元，摘帽预期基本落空。<br>
<strong style="color:#ef4444;">明日策略：任何反弹都是逃命机会，开盘务必清仓离场！</strong>新规后ST波动翻倍，持有风险极大。</p>

<hr style="border-color:rgba(255,255,255,0.1);margin:12px 0;">
<p style="font-size:13px;color:#d1d5db;"><strong style="color:#60a5fa;">明日核心逻辑</strong>：<br>
1. 今日市场极致分化——沪指微跌0.06%，创业板跌1.77%，高位科技集体杀跌（PCB/玻纤/光模块/存储领跌），资金流向煤炭/养殖/医药等低位防御板块，存量博弈高低切换正式开启<br>
2. 三星Q2业绩+GPT-5.6+SpaceX纳入纳指三重催化能否扭转科技股颓势是明日看点，但若催化兑现不涨需警惕"利好出尽"<br>
3. 两市成交3.09万亿缩量914亿，北向净卖出980亿，外资大幅兑现高位筹码，控制仓位为第一要务</p>
</div>
"""
portfolio_section = Section(title="&#128188; 持仓股明日操作指引", content=portfolio_html, icon="briefcase", variant="highlight")
gen._components.append(portfolio_section)

# ========== 市场影响分析 ==========
gen.add_impact_analysis("""
<div style="line-height:1.9;">
<p><strong style="color:#60a5fa;">【正面催化】</strong><br>
1. <strong>三星Q2业绩约86万亿韩元（同比+18倍）</strong>：若超预期将直接引爆全球半导体/存储链情绪，A股江波龙（已发744倍预增）、佰维存储、香农芯创、长电科技、通富微电等存力封测标的有望获资金回流。但需注意今日存储板块已遭机构净流出，业绩兑现后或有"利好出尽"风险。<br>
2. <strong>GPT-5.6发布</strong>：AI大模型军备竞赛升级，算力需求逻辑再强化，但光模块/CPO今日已领跌（量化集中抛售），短期修复需等待筹码充分交换。关注液冷（英维克为持仓）、AI服务器PCB等细分弹性。<br>
3. <strong>SpaceX纳入纳指100</strong>：43-270亿美元被动资金买入，外围商业航天情绪映射A股，但今日商业航天板块已下跌，谨防"利好兑现"。<br>
4. <strong>MACHINA具身智能峰会</strong>：特斯拉/优必选/智元量产节奏有望催化人形机器人板块，减速器/丝杠/传感器等核心零部件或迎事件驱动。<br>
5. <strong>央行万亿买断式逆回购后续效应</strong>：净投放中长期资金2000亿，流动性宽松托底大盘无系统性风险。</p>

<p><strong style="color:#ef4444;">【负面/风险因素】</strong><br>
1. <strong>USTR 60国关税听证</strong>：贸易摩擦新变量，若释放强硬信号可能压制全球风险偏好，出口链/光模块/消费电子等外销型科技股承压。<br>
2. <strong>北约峰会地缘风险</strong>：俄乌冲突升级风险扰动，军工/黄金有避险逻辑，但同时增加全球市场不确定性。<br>
3. <strong>高位科技杀跌趋势未止</strong>：今日PCB、玻纤、光模块、存储集体暴跌，机构集中兑现上半年浮盈，短期高低切换趋势明确，避免追高已反弹的高位标的。<br>
4. <strong>北向资金大幅净卖出980亿</strong>：外资兑现高位成长筹码，短期增量资金不足，结构性行情下选股难度加大。</p>

<p><strong style="color:#10b981;">【策略建议】</strong><br>
当前市场处于"万亿流动性托底+高位科技获利了结+中报业绩分化"三重博弈阶段，建议仓位控制在3-4成，方向上：<br>
- <strong>进攻方向</strong>：存储芯片（业绩确定性最高，三星财报+江波龙744倍预增验证）、人形机器人（MACHINA峰会催化）<br>
- <strong>防御方向</strong>：创新药（政策催化+机构加仓）、煤炭/养殖（顺周期低位+资金避险）<br>
- <strong>持仓处理</strong>：严格执行止损止盈纪律，铜冠铜箔/雅克科技/英维克反弹减仓，*ST建艺开盘清仓</p>
</div>
""")

# ========== 催化深度分析 ==========
top_events = [
    {
        'type': 'earnings',
        'title': '三星电子Q2初步财报（营业利润预计同比+18倍）',
        'description': '三星电子7月7日发布Q2初步财报，分析师预期营业利润约86万亿韩元，同比暴增17-18倍，有望超越英伟达Q1创全球科技企业单季历史最高。核心驱动力为HBM/DRAM涨价+AI服务器存储需求爆发。叠加SK海力士7月10日ADR美股上市，全球存储产业链景气度验证关键窗口。',
        'category': '半导体/存储'
    },
    {
        'type': 'policy',
        'title': 'OpenAI发布GPT-5.6三模型组合',
        'description': 'GPT-5.6包含Sol（旗舰推理）、Terra（全能性价比）、Luna（轻量高频）三大子模型，Sol Ultra在Terminal-Bench 2.1达91.9%超越Claude Fable 5。引入速度拨盘+提示缓存机制，定价大幅低于竞品。AI大模型"价格战"正式打响，算力需求刚性再强化，利好算力基础设施链。',
        'category': 'AI/算力'
    },
    {
        'type': 'general',
        'title': 'SpaceX纳入纳斯达克100指数',
        'description': 'SpaceX上市仅15天即纳入纳指100，创历史最快纪录。预计带来43-270亿美元被动资金强制买入。SpaceX估值持续攀升映射全球商业航天/卫星互联网赛道高景气，A股航天产业链存在情绪联动机会，但需警惕事件兑现后的获利回吐。',
        'category': '商业航天'
    },
]
gen.add_catalyst_deep_analysis(top_events)

# ========== 未来一周前瞻 ==========
week_ahead_html = """
<div style="line-height:1.9;">
<p><strong style="color:#a78bfa;">本周剩余重磅事件（7月8日-10日）</strong></p>
<ul style="padding-left:20px;margin:8px 0;">
<li><strong>7月8日（周三）</strong>：第25届中国互联网大会开幕（北京）；智谱港股首批限售股解禁（约850亿港元解禁压力）；*ST卓然复牌后首个完整交易日</li>
<li><strong>7月9日（周四）</strong>：<strong style="color:#ef4444;">中国6月CPI/PPI数据公布</strong>（市场预期CPI+1.1%，PPI+4.1%）；<strong style="color:#ef4444;">美联储6月FOMC会议纪要</strong>（新主席沃什首秀，半数委员预期年内加息）；立讯精密港股上市；三环集团港股上市；美联储威廉姆斯、洛根讲话；朱雀三号遥二酒泉发射验证垂直回收</li>
<li><strong>7月10日（周五）</strong>：SK海力士纳斯达克ADR上市（募资约294亿美元，阿里后最大亚太IPO）；科创板新股泰诺麦博申购；南京具身智能机器人产业展开幕（特斯拉/优必选/智元量产披露）；美伊新一轮会谈（巴基斯坦）</li>
</ul>
<p style="font-size:13px;color:#9ca3af;">本周是7月首个超级周：CPI/美联储纪要/SK海力士上市/智谱解禁四重重磅集中在周四周五，波动率将显著放大。</p>
</div>
"""
week_section = Section(title="未来一周事件前瞻", content=week_ahead_html, icon="calendar-days")
gen._components.append(week_section)

# ========== 风险提示 ==========
gen.add_risk_warning([
    "三星Q2业绩若低于预期（<80万亿韩元），存储板块可能补跌，高位半导体/PCB/光模块杀跌风险持续",
    "USTR关税听证若释放超预期强硬信号，可能引发全球风险资产回调，出口链科技股首当其冲",
    "新宁物流7月7日解禁1.12亿股（占总股本20%），ST板块涨跌幅翻倍后波动风险极大，*ST建艺务必清仓",
    "高位科技股（PCB/玻纤/光模块）机构集中兑现趋势未止，抄底需等待放量企稳信号",
    "北向资金单日净卖出近千亿，外资风险偏好明显下降，短期A股或延续结构性分化格局",
    "本报告基于公开信息整理，不构成投资建议，数据来源包括财联社、新浪财经、36氪、华尔街见闻、东方财富、中财网等"
])

# ========== 发布 ==========
result = gen.publish()
print("=" * 60)
print("PUBLISH RESULT:", result)
print("=" * 60)
