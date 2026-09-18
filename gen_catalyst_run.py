import sys, os
sys.path.insert(0, '/root/daily-news-insight/v3')
os.chdir('/root/daily-news-insight')

from v3.generators.tomorrow_catalyst import TomorrowCatalystGenerator

gen = TomorrowCatalystGenerator(
    date_str="20260919",
    subtitle="2026.09.19 · 明日催化剂"
)

# 1. 核心催化
gen.add_key_catalyst("""
<b>明日三大核心催化聚焦</b>：① 富时中国A50指数季度调整18日收盘后生效（中微公司、生益科技纳入，牧原、万华化学剔除），周五盘后成分股调仓对权重股资金面影响持续发酵；② 金帝股份（603270）3300万股限售股9月18日解禁上市，占总股本15.06%，占现流通盘46.67%，对次新板块情绪构成压力测试；③ 国新办9月20日"十五五"市场监管高质量发展发布会周末落地，药监局参会，医药/创新药板块或提前博弈政策预期。
""")

# 2. 事件日历
events = [
    {
        'type': 'policy',
        'title': '国新办"十五五"市场监管高质量发展发布会',
        'description': '9月20日（周日）上午10时，市场监管总局副局长束为、国家药监局副局长杨胜介绍"十五五"时期推动市场监管高质量发展有关情况。关注创新药审评审批、反垄断、消费者权益等方向。',
        'category': '政策发布'
    },
    {
        'type': 'meeting',
        'title': '第140届广交会预热发布会',
        'description': '商务部持续推进第140届中国进出口商品交易会筹备工作，本届广交会将于10月15日开幕，出口贸易企业、跨境电商板块受益预期升温。',
        'category': '重要会议'
    },
    {
        'type': 'data',
        'title': '中国8月经济数据密集公布周（已披露）',
        'description': '8月规模以上工业增加值增长5.2%、社零总额增长1.1%、固定资产投资基本平稳、70城房价数据出炉。电子行业对工业生产贡献率居首，装备制造较快增长。',
        'category': '经济数据'
    },
    {
        'type': 'earnings',
        'title': '多家公司披露回购/减持/重组进展',
        'description': '视源股份股东拟合计减持不超0.85%；中国巨石股东减持2832万股；*ST英飞签署28.41亿元重整投资协议；恺英网络拟2.98亿美元参股海外游戏资产。',
        'category': '公司公告'
    },
    {
        'type': 'policy',
        'title': '《金融产品网络营销管理办法》9月30日实施倒计时',
        'description': '央行等八部门制定的《金融产品网络营销管理办法》9月30日起实施，上海证监局进一步细化基金网络营销合作要求，利好持牌金融机构及合规金融IT公司。',
        'category': '监管政策'
    },
    {
        'type': 'meeting',
        'title': '联合国大会下周开幕 特朗普将出席',
        'description': '第81届联合国大会下周在纽约开幕，特朗普总统预计下周二与海湾国家领导人会晤，商讨伊朗战事后续安排；以色列总理也可能在纽约与特朗普会面。',
        'category': '海外会议'
    },
    {
        'type': 'general',
        'title': '华为全新计算架构发布 百万处理器互联突破',
        'description': '华为发布全新计算架构，让百万处理器成为一台计算机，突破大规模计算互联瓶颈，算力基础设施与自主可控方向再迎技术里程碑。关注华为算力链、液冷、先进封装。',
        'category': '产业科技'
    },
    {
        'type': 'general',
        'title': '国庆中秋双节旅游热度持续走高',
        'description': '国庆假期首日（10月1日）火车票已于9月17日开售，双节旅游热度持续升温，中秋休市9月25-27日、国庆休市10月1-7日。旅游酒店、餐饮、免税、航空板块迎催化。',
        'category': '消费节日'
    }
]
gen.add_events_calendar(events)

# 3. 限售股解禁详情
from components.layout import Section, SubCard
from components.data import DataGrid, DataCard

# 手动构造解禁表格HTML
unlock_html = '''
<div style="overflow-x: auto;">
<table style="width: 100%; border-collapse: collapse; font-size: 13px; color: #cbd5e1;">
<thead>
<tr style="background: rgba(59, 130, 246, 0.15);">
<th style="padding: 10px 12px; text-align: left; border-bottom: 1px solid rgba(255,255,255,0.1); color: #e2e8f0;">代码</th>
<th style="padding: 10px 12px; text-align: left; border-bottom: 1px solid rgba(255,255,255,0.1); color: #e2e8f0;">名称</th>
<th style="padding: 10px 12px; text-align: right; border-bottom: 1px solid rgba(255,255,255,0.1); color: #e2e8f0;">解禁数量(万股)</th>
<th style="padding: 10px 12px; text-align: right; border-bottom: 1px solid rgba(255,255,255,0.1); color: #e2e8f0;">占总股本</th>
<th style="padding: 10px 12px; text-align: right; border-bottom: 1px solid rgba(255,255,255,0.1); color: #e2e8f0;">占流通盘</th>
<th style="padding: 10px 12px; text-align: left; border-bottom: 1px solid rgba(255,255,255,0.1); color: #e2e8f0;">类型</th>
</tr>
</thead>
<tbody>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.05);">
<td style="padding: 10px 12px;">603270</td>
<td style="padding: 10px 12px; color: #f1f5f9; font-weight: 600;">金帝股份</td>
<td style="padding: 10px 12px; text-align: right; color: #fbbf24;">3300.00</td>
<td style="padding: 10px 12px; text-align: right; color: #fbbf24;">15.06%</td>
<td style="padding: 10px 12px; text-align: right; color: #fbbf24;">46.67%</td>
<td style="padding: 10px 12px;">首发原股东限售</td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.05);">
<td style="padding: 10px 12px;">000010</td>
<td style="padding: 10px 12px; color: #f1f5f9;">*ST美丽</td>
<td style="padding: 10px 12px; text-align: right;">3382.14</td>
<td style="padding: 10px 12px; text-align: right;">2.94%</td>
<td style="padding: 10px 12px; text-align: right;">3.69%</td>
<td style="padding: 10px 12px;">定向增发机构配售</td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.05);">
<td style="padding: 10px 12px;">688368</td>
<td style="padding: 10px 12px; color: #f1f5f9;">晶丰明源</td>
<td style="padding: 10px 12px; text-align: right;">324.54</td>
<td style="padding: 10px 12px; text-align: right;">1.59%</td>
<td style="padding: 10px 12px; text-align: right;">2.62%</td>
<td style="padding: 10px 12px;">首发原股东限售</td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.05);">
<td style="padding: 10px 12px;">002911</td>
<td style="padding: 10px 12px; color: #f1f5f9;">佛燃能源</td>
<td style="padding: 10px 12px; text-align: right;">949.59</td>
<td style="padding: 10px 12px; text-align: right;">0.73%</td>
<td style="padding: 10px 12px; text-align: right;">0.75%</td>
<td style="padding: 10px 12px;">股权激励限售</td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.05);">
<td style="padding: 10px 12px;">002796</td>
<td style="padding: 10px 12px; color: #f1f5f9;">世嘉科技</td>
<td style="padding: 10px 12px; text-align: right;">42.50</td>
<td style="padding: 10px 12px; text-align: right;">0.17%</td>
<td style="padding: 10px 12px; text-align: right;">0.19%</td>
<td style="padding: 10px 12px;">股权激励限售</td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.05);">
<td style="padding: 10px 12px;">603192</td>
<td style="padding: 10px 12px; color: #f1f5f9;">汇得科技</td>
<td style="padding: 10px 12px; text-align: right;">25.31</td>
<td style="padding: 10px 12px; text-align: right;">0.15%</td>
<td style="padding: 10px 12px; text-align: right;">0.15%</td>
<td style="padding: 10px 12px;">股权激励限售</td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.05);">
<td style="padding: 10px 12px;">688261</td>
<td style="padding: 10px 12px; color: #f1f5f9;">东微半导</td>
<td style="padding: 10px 12px; text-align: right;">18.25</td>
<td style="padding: 10px 12px; text-align: right;">0.15%</td>
<td style="padding: 10px 12px; text-align: right;">0.15%</td>
<td style="padding: 10px 12px;">股权激励限售</td>
</tr>
<tr>
<td style="padding: 10px 12px;">300743</td>
<td style="padding: 10px 12px; color: #f1f5f9;">天地数码</td>
<td style="padding: 10px 12px; text-align: right;">14.02</td>
<td style="padding: 10px 12px; text-align: right;">0.09%</td>
<td style="padding: 10px 12px; text-align: right;">0.11%</td>
<td style="padding: 10px 12px;">股权激励限售</td>
</tr>
</tbody>
</table>
</div>
<div style="margin-top: 14px; padding: 12px 14px; background: rgba(251, 191, 36, 0.08); border: 1px solid rgba(251, 191, 36, 0.2); border-radius: 10px; color: #fcd34d; font-size: 13px; line-height: 1.7;">
<b>影响分析：</b>明日解禁规模整体可控，合计约0.8亿股，但<b>金帝股份（603270）</b>解禁压力最大——占现流通盘比例高达46.67%，首发原股东低成本筹码集中释放，可能对股价形成显著抛压，并波及次新股板块情绪。参考近期摩尔线程、沐曦股份解禁后20-30%的跌幅，次新投资者应保持谨慎，避免追高。下周铜陵有色（132亿元）、聚仁新材（占总股本23.94%）等解禁规模较大，需提前规避。
</div>
'''
gen._components.append(Section(title="🔒 限售股解禁详情", content=unlock_html, icon="lock"))

# 4. 新股申购
ipo_html = '''
<div style="overflow-x: auto;">
<table style="width: 100%; border-collapse: collapse; font-size: 13px; color: #cbd5e1;">
<thead>
<tr style="background: rgba(16, 185, 129, 0.15);">
<th style="padding: 10px 12px; text-align: left; border-bottom: 1px solid rgba(255,255,255,0.1); color: #e2e8f0;">名称</th>
<th style="padding: 10px 12px; text-align: left; border-bottom: 1px solid rgba(255,255,255,0.1); color: #e2e8f0;">代码</th>
<th style="padding: 10px 12px; text-align: right; border-bottom: 1px solid rgba(255,255,255,0.1); color: #e2e8f0;">发行价(元)</th>
<th style="padding: 10px 12px; text-align: right; border-bottom: 1px solid rgba(255,255,255,0.1); color: #e2e8f0;">市盈率</th>
<th style="padding: 10px 12px; text-align: right; border-bottom: 1px solid rgba(255,255,255,0.1); color: #e2e8f0;">申购上限(股)</th>
<th style="padding: 10px 12px; text-align: left; border-bottom: 1px solid rgba(255,255,255,0.1); color: #e2e8f0;">板块</th>
<th style="padding: 10px 12px; text-align: left; border-bottom: 1px solid rgba(255,255,255,0.1); color: #e2e8f0;">日期</th>
</tr>
</thead>
<tbody>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.05);">
<td style="padding: 10px 12px; color: #f1f5f9; font-weight: 600;">力勤资源</td>
<td style="padding: 10px 12px;">001246</td>
<td style="padding: 10px 12px; text-align: right;">21.23</td>
<td style="padding: 10px 12px; text-align: right;">12.98倍</td>
<td style="padding: 10px 12px; text-align: right;">51500</td>
<td style="padding: 10px 12px;">主板</td>
<td style="padding: 10px 12px; color: #10b981;">9月18日申购</td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.05);">
<td style="padding: 10px 12px; color: #f1f5f9;">宇特光电</td>
<td style="padding: 10px 12px;">920157</td>
<td style="padding: 10px 12px; text-align: right;">13.75</td>
<td style="padding: 10px 12px; text-align: right;">14.99倍</td>
<td style="padding: 10px 12px; text-align: right;">618300</td>
<td style="padding: 10px 12px;">北交所</td>
<td style="padding: 10px 12px;">9月21日申购</td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.05);">
<td style="padding: 10px 12px; color: #f1f5f9;">世纪数码</td>
<td style="padding: 10px 12px;">920229</td>
<td style="padding: 10px 12px; text-align: right;">15.67</td>
<td style="padding: 10px 12px; text-align: right;">13.49倍</td>
<td style="padding: 10px 12px; text-align: right;">467500</td>
<td style="padding: 10px 12px;">北交所</td>
<td style="padding: 10px 12px; color: #3b82f6;">9月22日上市</td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.05);">
<td style="padding: 10px 12px; color: #f1f5f9;">粤芯半导体</td>
<td style="padding: 10px 12px;">301660</td>
<td style="padding: 10px 12px; text-align: right;">待定</td>
<td style="padding: 10px 12px; text-align: right;">--</td>
<td style="padding: 10px 12px; text-align: right;">--</td>
<td style="padding: 10px 12px;">创业板</td>
<td style="padding: 10px 12px;">9月24日申购</td>
</tr>
<tr>
<td style="padding: 10px 12px; color: #f1f5f9;">联亚药业</td>
<td style="padding: 10px 12px;">301569</td>
<td style="padding: 10px 12px; text-align: right;">待定</td>
<td style="padding: 10px 12px; text-align: right;">--</td>
<td style="padding: 10px 12px; text-align: right;">--</td>
<td style="padding: 10px 12px;">创业板</td>
<td style="padding: 10px 12px;">9月28日申购</td>
</tr>
</tbody>
</table>
</div>
<div style="margin-top: 14px; padding: 12px 14px; background: rgba(16, 185, 129, 0.08); border: 1px solid rgba(16, 185, 129, 0.2); border-radius: 10px; color: #6ee7b7; font-size: 13px; line-height: 1.7;">
<b>申购建议：</b>明日（9月19日周五）<b>无新股申购</b>。力勤资源已于9月18日完成申购，中签缴款日为9月22日。下周一（9月21日）北交所宇特光电开启申购，发行价13.75元，发行后市盈率14.99倍，属于光通信/光纤连接器赛道，行业景气度较高，建议积极申购。粤芯半导体（模拟芯片IDM）9月24日申购，为近期最受关注的半导体新股，需提前准备市值。
</div>
'''
gen._components.append(Section(title="📈 新股申购与上市", content=ipo_html, icon="trending-up"))

# 5. 经济数据公布
gen.add_data_release([
    {
        'name': '美国8月工业产出',
        'prev': '上月环比+0.6%',
        'expect': '预期+0.4%',
        'actual': '9月18日已公布'
    },
    {
        'name': '美国9月密歇根大学消费者信心指数初值',
        'prev': '前值78.5',
        'expect': '预期76.0',
        'actual': '周五公布'
    },
    {
        'name': '中国8月70城房价指数',
        'prev': '7月环比-0.2%',
        'expect': '关注环比变化',
        'actual': '9月18日已公布'
    },
    {
        'name': '日本8月核心CPI',
        'prev': '7月+1.8%',
        'expect': '预期+1.8%',
        'actual': '实际+1.7%'
    },
    {
        'name': '英国8月CPI',
        'prev': '7月+2.9%',
        'expect': '预期+3.0%',
        'actual': '实际+3.1%'
    },
    {
        'name': '美国费城联储制造业指数(9月)',
        'prev': '前值47.4',
        'expect': '预期30.5',
        'actual': '实际37.8'
    }
])

# 6. 海外大事提醒
overseas_html = '''
<div style="display: flex; flex-direction: column; gap: 12px;">
<div style="background: rgba(139, 92, 246, 0.08); border: 1px solid rgba(139, 92, 246, 0.2); border-radius: 12px; padding: 14px 16px;">
<div style="color: #c4b5fd; font-weight: 600; font-size: 14px; margin-bottom: 6px;">🏛️ 联合国大会下周开幕（9月22日起）</div>
<div style="color: #cbd5e1; font-size: 13px; line-height: 1.7;">第81届联合国大会一般性辩论将于下周在纽约举行。特朗普总统预计下周二在纽约联合国大会期间，与海湾国家领导人举行会晤，商讨伊朗战事后续安排。市场关注美国提出的"战后战略构想"对中东局势及原油价格的影响。当前布伦特原油仍在100美元上方波动，地缘风险溢价显著。</div>
</div>
<div style="background: rgba(239, 68, 68, 0.08); border: 1px solid rgba(239, 68, 68, 0.2); border-radius: 12px; padding: 14px 16px;">
<div style="color: #fca5a5; font-weight: 600; font-size: 14px; margin-bottom: 6px;">💵 美联储三年多首次加息25个基点 释放鹰派信号</div>
<div style="color: #cbd5e1; font-size: 13px; line-height: 1.7;">美联储9月16日宣布加息25BP至3.75%-4%，为2023年7月以来首次加息，并暗示年内还可能再加息一次。鲍威尔（沃什）强调通胀压力顽固，全球能源价格走高。香港金管局及沙特、阿联酋等多国央行跟随加息。美股科技股反弹，纳指涨1.69%，AI硬件股、芯片股大涨（英特尔+7%、美光+5%）。对A股影响：短期外资流动或有扰动，但"科技+红利"杠铃策略仍是机构主线。</div>
</div>
<div style="background: rgba(251, 191, 36, 0.08); border: 1px solid rgba(251, 191, 36, 0.2); border-radius: 12px; padding: 14px 16px;">
<div style="color: #fcd34d; font-weight: 600; font-size: 14px; margin-bottom: 6px;">🇬🇧 英国央行维持利率3.75%不变 但上调通胀预期</div>
<div style="color: #cbd5e1; font-size: 13px; line-height: 1.7;">英国央行以6:3投票维持基准利率3.75%不变，为连续第六次按兵不动。但央行上调通胀预期，预计2027年一季度通胀率将略高于4%，警告能源价格波动可能需要加息。英国30年期国债收益率跌至5.76%（创5月最大单日跌幅）。全球主要央行政策分化加剧。</div>
</div>
<div style="background: rgba(59, 130, 246, 0.08); border: 1px solid rgba(59, 130, 246, 0.2); border-radius: 12px; padding: 14px 16px;">
<div style="color: #93c5fd; font-weight: 600; font-size: 14px; margin-bottom: 6px;">🇯🇵 日本8月核心CPI 1.7% 央行加息预期升温</div>
<div style="color: #cbd5e1; font-size: 13px; line-height: 1.7;">日本8月核心CPI同比上涨1.7%，虽较7月1.8%小幅回落，但剔除生鲜食品和能源的核心CPI维持1.9%涨幅。日生基础研究所预计核心CPI将于10月加速破2%，2027财年达3%。市场预期日本央行9月可能加息至1.25%。日元汇率及日股波动需关注。</div>
</div>
</div>
'''
gen._components.append(Section(title="🌍 海外大事提醒", content=overseas_html, icon="globe"))

# 7. 重点事件影响深度分析与操作建议
deep_html = '''
<div style="line-height: 1.9; color: #cbd5e1; font-size: 14px;">
<h3 style="color: #f1f5f9; border-left: 3px solid #fbbf24; padding-left: 10px; margin-top: 0;">一、富时A50调仓生效：权重股资金面短期扰动</h3>
<p>富时中国A50指数季度调整已于9月18日收盘后正式生效，<b>纳入中微公司（688012）、生益科技（600183），剔除牧原股份（002714）、万华化学（600309）</b>。这一调整反映了外资对中国科技制造资产的配置偏好上升，传统消费和化工龙头权重下降。</p>
<p><b>影响判断（中性偏多）：</b>中微公司作为半导体设备龙头被纳入，将带来被动指数基金的增量买盘，预计资金规模约10-20亿元级别，对股价形成短期支撑。生益科技作为PCB/CCL龙头，受益于AI服务器和先进封装需求爆发，纳入A50是基本面的认可。被剔除的牧原股份和万华化学短期面临被动资金流出压力，但考虑到调整已提前公告，预期基本消化。</p>
<p><b>操作建议：</b>中微公司作为持仓雅克科技的半导体设备上游标的，纳入A50对整个半导体设备链情绪有正向带动。持有雅克科技的投资者可适度提高对半导体设备板块的信心，但雅克本身不在调仓范围内，不建议追高加仓，维持底仓+机动仓策略。</p>

<h3 style="color: #f1f5f9; border-left: 3px solid #ef4444; padding-left: 10px; margin-top: 20px;">二、金帝股份巨量解禁：次新板块情绪压力测试</h3>
<p><b>金帝股份（603270）3300万股限售股</b>已于9月18日上市流通，占总股本15.06%，占现有流通盘高达46.67%。这意味着流通筹码一夜之间扩容近一半，供需关系严重倾斜。</p>
<p><b>影响判断（利空）：</b>参考近期摩尔线程（9月7日解禁后跌停，累计跌超30%）和沐曦股份（解禁前连跌9天，较高点腰斩）的表现，次新股首发解禁的抛售压力不容小觑。金帝股份作为2024年上市的轴承精密制造企业，发行后股价涨幅较大，原始股东获利丰厚，减持意愿较强。</p>
<p><b>操作建议：</b>持仓中<span style="color: #fbbf24; font-weight: 600;">无金帝股份</span>，无需直接操作。但需关注次新板块情绪传导效应，若金帝股份大幅低开或跌停，可能带动近期上市的次新股集体调整。次新股仓位较重的投资者应考虑降低仓位，规避解禁高峰期风险。下周铜陵有色（132亿元解禁）、聚仁新材（23.94%大比例解禁）同样需要警惕。</p>

<h3 style="color: #f1f5f9; border-left: 3px solid #10b981; padding-left: 10px; margin-top: 20px;">三、华为全新计算架构：国产算力自主可控再突破</h3>
<p>华为发布全新计算架构，实现<b>"百万处理器成为一台计算机"</b>的技术突破，解决了大规模计算互联瓶颈问题。这是继昇腾AI芯片之后，华为在算力基础设施层面的又一里程碑。</p>
<p><b>影响判断（利好）：</b>华为算力体系的持续突破对整个国产算力产业链形成强催化。受益链条包括：①华为昇腾算力供应链（PCB/CCL的生益科技、沪电股份、深南电路）；②液冷散热（英维克、申菱环境、高澜股份）；③先进封装/Chiplet（华海诚科、雅克科技、长电科技）；④光模块/光互联（中际旭创、新易盛、天孚通信）。</p>
<p><b>操作建议：</b>持仓中<b>英维克（液冷）、雅克科技（前驱体/先进封装材料）</b>均直接受益于华为算力链扩张。华为新架构将推动算力集群规模升级，单机液冷需求量和热管理复杂度同步提升，英维克作为液冷龙头有望深度受益。雅克科技的前驱体和光刻胶业务与华为半导体生态协同紧密。建议维持英维克、雅克科技底仓持有，逢回调加仓机动仓。</p>

<h3 style="color: #f1f5f9; border-left: 3px solid #8b5cf6; padding-left: 10px; margin-top: 20px;">四、"十五五"市场监管发布会周末落地：医药板块博弈窗口</h3>
<p>国新办9月20日（周日）上午10时将举行<b>"十五五"时期推动市场监管高质量发展</b>主题发布会，市场监管总局副局长束为、国家药监局副局长杨胜出席。市场关注创新药审评审批提速、医疗器械监管优化、反垄断执法等方向。</p>
<p><b>影响判断（中性偏多）：</b>"十五五"期间市场监管方向的定调对医药创新、消费、互联网平台等行业具有中长期影响。若药监局释放创新药审评审批加速、鼓励创新的信号，将利好CXO、创新药企业；若反垄断政策趋严，则可能对互联网平台股形成压制。</p>
<p><b>操作建议：</b>当前持仓中无纯医药标的，但雅克科技的电子材料业务与医药板块无直接关联。可关注创新药板块的短线交易性机会，如恒瑞医药、药明康德等，但周末事件驱动存在不确定性，不建议重仓博弈，小仓位试错即可。</p>

<h3 style="color: #f1f5f9; border-left: 3px solid #06b6d4; padding-left: 10px; margin-top: 20px;">五、双节旅游消费预热：国庆中秋假期临近</h3>
<p>中秋国庆双节临近，国庆假期首日（10月1日）火车票已于9月17日开售，双节旅游热度持续走高。中秋休市：9月25日（周五）至9月27日（周日）；国庆休市：10月1日（周四）至10月7日（周三）。</p>
<p><b>影响判断（中性偏多）：</b>双节8天长假（可拼假）预计出行人次和旅游消费再创新高。受益板块：旅游酒店（锦江酒店、首旅酒店、中国中免）、航空（中国国航、南方航空）、餐饮（广州酒家、绝味食品）、免税（中国中免）。但需注意"节日效应"往往提前兑现，假期正式开始后可能出现"利好兑现"回调。</p>
<p><b>操作建议：</b>当前持仓中无消费股，以科技成长为主。若看好双节消费行情，可考虑小仓位配置消费ETF或龙头股作为对冲，但不建议放弃科技主线仓位。重点还是回归AI算力、先进封装、存储等核心成长赛道。</p>
</div>
'''
gen._components.append(Section(title="💡 重点事件深度分析与操作建议", content=deep_html, icon="zap", variant="highlight"))

# 催化深度分析模块（Skill增强）
gen.add_catalyst_deep_analysis([
    {'type': 'policy', 'title': '华为全新计算架构发布', 'description': '百万处理器互联突破，算力自主可控里程碑，利好华为算力链、液冷散热、先进封装材料', 'category': '产业科技'},
    {'type': 'general', 'title': '美联储加息25个基点', 'description': '时隔三年首次加息，鹰派信号，年内或再加息一次，影响外资流动和全球风险偏好', 'category': '海外政策'},
    {'type': 'meeting', 'title': '国新办"十五五"市场监管发布会', 'description': '周末发布市场监管高质量发展规划，药监局参会，关注创新药政策方向', 'category': '政策发布'}
])

# 8. 风险提示
gen.add_risk_warning([
    "美联储加息超预期，全球流动性收紧，外资流出A股压力加大",
    "次新股解禁潮持续，金帝股份、铜陵有色等大额解禁可能冲击市场情绪",
    "中东地缘局势恶化，原油价格飙升推升通胀预期，压制成长股估值",
    "双节前资金避险情绪升温，高估值科技板块可能面临获利回吐",
    "国内经济复苏力度不及预期，消费和地产数据偏弱"
])

# 发布
result = gen.publish()
print("发布结果:", result)
