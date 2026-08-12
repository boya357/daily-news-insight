#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
明日催化剂 - 2026年8月13日版
"""
import sys, os
sys.path.insert(0, '/root/daily-news-insight/v3')
os.chdir('/root/daily-news-insight')

from v3.generators.tomorrow_catalyst import TomorrowCatalystGenerator

gen = TomorrowCatalystGenerator(
    date_str="20260813",
    subtitle="2026.08.13 · 明日催化剂"
)

# 1. 核心催化总结
gen.add_key_catalyst(
    "8月13日四大核心催化：闪迪投资者日定调NAND周期与HBF高带宽闪存路线图，存储板块迎产业级指引；中芯国际盘后披露中报，检验晶圆代工景气度与先进封装产能爬坡；SMM电池技术产业大会长沙开幕，固态电池与钠电路线成焦点；谷歌Pixel 11系列发布会，消费电子AI化标杆落地。此外，美国7月PPI与初请失业金数据、英国Q2 GDP初值为全球宏观再添定价锚。"
)

# 2. 事件日历
events = [
    {
        'type': 'meeting',
        'title': '闪迪2026投资者日',
        'description': '美东时间9:00（北京时间21:00），CEO David Goeckeler出席，聚焦NAND存储周期与HBF高带宽闪存路线图，与FMS闪存峰会行情呼应。A股映射：江波龙、佰维存储、德明利、朗科科技。',
        'category': '存储芯片'
    },
    {
        'type': 'earnings',
        'title': '中芯国际2026年中报披露',
        'description': '盘后发布二季报，检验晶圆代工景气度与先进封装产能爬坡进度。市场关注14nm/7nm产能利用率、AI相关芯片代工收入占比、资本开支指引。',
        'category': '半导体'
    },
    {
        'type': 'meeting',
        'title': '2026 SMM电池技术产业大会',
        'description': '8月13-14日在湖南长沙召开，王先友院士作《固态电池及其发展思考》主旨报告，重点研讨固态电池材料、装备进展与钠电标准化。A股映射：赣锋锂业、上海洗霸、金龙羽、当升科技、璞泰来。',
        'category': '电池/储能'
    },
    {
        'type': 'meeting',
        'title': '谷歌Made by Google发布会',
        'description': '北京时间8月13日06:00，推出Pixel 11系列四款新机（标准版/Pro/Pro XL/Pro Fold），全系搭载台积电2nm工艺Tensor G6处理器、256GB起步，深度整合Gemini生态。',
        'category': '消费电子'
    },
    {
        'type': 'earnings',
        'title': '京东集团二季报发布',
        'description': '京东物流、京东健康、京东工业同步披露业绩，关注电商消费复苏力度与下沉市场表现，京东工业AI供应链进展。',
        'category': '电商/消费'
    },
    {
        'type': 'data',
        'title': '美国7月PPI数据',
        'description': '20:30公布7月PPI及核心PPI，承接12日CPI数据，进一步验证美联储9月政策路径。若PPI超预期反弹，或强化市场加息担忧。',
        'category': '宏观数据'
    },
    {
        'type': 'data',
        'title': '英国Q2 GDP初值',
        'description': '英国第二季度GDP初值、工业产出、商品贸易帐等数据公布。市场预期GDP环比0.0%（前值0.1%），经济疲弱状态延续。',
        'category': '海外宏观'
    },
    {
        'type': 'meeting',
        'title': '第四届中国具身智能机器人产业大会（第二天）',
        'description': '上海新国际博览中心，8月12-14日举办。13日进入专业观众日与技术论坛高峰，关注人形机器人关节、灵巧手、具身大模型等新品发布与技术路线进展。',
        'category': '机器人'
    },
    {
        'type': 'policy',
        'title': '国新办"美丽中国建设"新闻发布会',
        'description': '8月13日上午10点，生态环境部部长黄润秋介绍全面推进美丽中国建设进展并答记者问。关注"十五五"生态环保目标、碳达峰路径、绿色产业扶持政策表述。',
        'category': '环保政策'
    },
    {
        'type': 'general',
        'title': '逸飞激光摘帽复牌',
        'description': 'ST逸飞撤销其他风险警示，证券简称变更为"逸飞激光"（688646），8月13日起复牌交易。激光设备+储能+半导体概念，关注摘帽后资金博弈。',
        'category': '个股事件'
    },
    {
        'type': 'earnings',
        'title': '中国移动/华虹公司中报',
        'description': '港股中国移动披露中报，关注算力网络与AI云服务进展；华虹公司（688347）同步披露业绩，与中芯国际互为参照，验证晶圆代工周期复苏斜率。',
        'category': '科技蓝筹'
    },
    {
        'type': 'data',
        'title': '美国初请失业金人数',
        'description': '20:30公布至8月8日当周初请失业金人数，为非农数据后首份周度就业指标，判断劳动力市场降温节奏。',
        'category': '就业数据'
    },
]

gen.add_events_calendar(events)

# 3. 业绩公告
gen.add_earnings_announcements([
    {'name': '中芯国际', 'code': '688981.SH', 'type': '中报披露', 'growth': '待公布'},
    {'name': '京东集团', 'code': '09618.HK', 'type': '二季报', 'growth': '待公布'},
    {'name': '中国移动', 'code': '00941.HK', 'type': '中报披露', 'growth': '待公布'},
    {'name': '华虹公司', 'code': '688347.SH', 'type': '中报披露', 'growth': '待公布'},
    {'name': '联想集团', 'code': '00992.HK', 'type': '首季业绩', 'growth': '待公布'},
    {'name': '华虹宏力', 'code': '01347.HK', 'type': '中报披露', 'growth': '待公布'},
])

# 4. 经济数据发布
gen.add_data_release([
    {'name': '美国7月PPI环比', 'prev': '待确认', 'expect': '+0.2%'},
    {'name': '美国7月核心PPI同比', 'prev': '待确认', 'expect': '+2.5%'},
    {'name': '美国初请失业金人数', 'prev': '待确认', 'expect': '23.5万'},
    {'name': '英国Q2 GDP环比初值', 'prev': '+0.1%', 'expect': '0.0%'},
    {'name': '英国6月工业产出环比', 'prev': '-0.5%', 'expect': '+0.1%'},
    {'name': '欧元区6月工业产出环比', 'prev': '-0.2%', 'expect': '-0.1%'},
])

# 5. 市场影响深度分析
impact_html = '''
<div style="line-height: 2; color: #e2e8f0; font-size: 15px;">

<h3 style="color: #fbbf24; margin-top: 20px; margin-bottom: 12px;">📌 核心事件一：闪迪投资者日 — HBF高带宽闪存能否成为存储板块新叙事？</h3>
<p style="margin-bottom: 12px;"><strong>事件性质：产业级指引，偏利好（结构性）</strong></p>
<p style="margin-bottom: 12px;">闪迪8月13日投资者日的核心看点已不再是传统NAND价格周期，而是<strong>HBF（High Bandwidth Flash）高带宽闪存</strong>这一全新技术路线。8月4日，闪迪与SK海力士已通过OCP发布首版HBF技术规范，定位为AI推理场景下HBM的成本补充方案——即用NAND闪存承接HBM覆盖不了的大模型KV缓存、推理加速等场景，从"存储墙"角度切入AI基础设施。</p>
<p style="margin-bottom: 12px;"><strong>影响逻辑：</strong>如果闪迪在投资者日上给出明确的HBF商业化路线图与客户进展，将直接引爆A股存储板块的<strong>"第二增长曲线"</strong>预期。当前存储板块的核心叙事——NAND涨价周期——已经交易了近两个季度，边际增量递减。HBF若能打开"NAND+AI"的新估值空间，相当于给存储股重新定价。A股受益梯队：①<strong>江波龙</strong>（301308，存储模组龙头，Q2净利润同比增71528%，已预告中报大增）；②<strong>佰维存储</strong>（688525，AI存储深度布局，信创+消费电子双轮）；③<strong>德明利</strong>（001309，移动存储+企业级SSD转型）；④<strong>朗科科技</strong>（300042，存储控制器+国产替代）。</p>
<p style="margin-bottom: 12px;"><strong>操作建议：</strong>存储板块当前处于涨价周期兑现+HBF预期升温的双驱动窗口。短期受美国CPI/PPI扰动可能有波动，但产业趋势向上明确。<strong>已有持仓可继续持有，不追高</strong>，回调5-8%是加仓机会。核心标的优先选择业绩已兑现（江波龙）+AI业务弹性大（佰维存储）的组合。</p>

<h3 style="color: #fbbf24; margin-top: 24px; margin-bottom: 12px;">📌 核心事件二：中芯国际中报 — 晶圆代工景气度的试金石</h3>
<p style="margin-bottom: 12px;"><strong>事件性质：业绩验证，中性偏谨慎（预期已高）</strong></p>
<p style="margin-bottom: 12px;">中芯国际盘后披露中报是周四最重磅的A股公司事件。当前市场对晶圆代工复苏预期较高，但分化明显：<strong>成熟制程（28nm及以上）</strong>受AI边缘计算、汽车电子、工业控制拉动，产能利用率回升较快；<strong>先进制程（14nm/7nm）</strong>受出口管制与客户验证周期影响，爬坡速度仍需观察。</p>
<p style="margin-bottom: 12px;"><strong>市场关注点：</strong>①产能利用率回升幅度（Q1约80%，市场预期Q2提升至85-88%）；②晶圆ASP（平均售价）是否止跌回升；③先进封装（CoWoS类）业务收入占比及增速；④下半年资本开支指引是否上调；⑤AI相关芯片代工收入具体规模。</p>
<p style="margin-bottom: 12px;"><strong>影响标的：</strong>中芯国际（688981）本身、华虹公司（688347）、北方华创（002371）、中微公司（688012）、拓荆科技（688072）、雅克科技（002409，前驱体材料）、华海诚科（688535，封装材料）。</p>
<p style="margin-bottom: 12px;"><strong>操作建议：</strong>半导体设备与材料板块近期累积涨幅较大，中芯业绩若<strong>符合预期可能出现"利好兑现"</strong>走势，需警惕短期回调。但若超预期（如产能利用率超90%或先进封装收入大增），则可能带动半导体板块新一轮上攻。建议<strong>持仓者设好止盈，空仓者等回调后再介入</strong>。</p>

<h3 style="color: #fbbf24; margin-top: 24px; margin-bottom: 12px;">📌 核心事件三：SMM电池技术大会 — 固态电池与钠电的路线之争</h3>
<p style="margin-bottom: 12px;"><strong>事件性质：产业催化，利好（主题性）</strong></p>
<p style="margin-bottom: 12px;">2026 SMM电池技术产业大会8月13-14日在长沙召开，是继芝加哥全球固态电池峰会后又一行业盛会。王先友院士的《固态电池及其发展思考》主旨报告将定调国内技术路线方向，硫化物、氧化物、卤化物三条路线谁更接近量产是最大看点。</p>
<p style="margin-bottom: 12px;"><strong>三大看点：</strong>①固态电解质技术路线收敛趋势（近期卤化物电解质关注度上升，导电率突破10mS/cm）；②钠电标准化进展（工信部赵丽香司长出席，钠电池国标落地节奏）；③干法电极、锂金属负极等降本技术的产业化进度。</p>
<p style="margin-bottom: 12px;"><strong>影响标的：</strong>固态电池方向——<strong>上海洗霸</strong>（603200，氧化物路线）、<strong>金龙羽</strong>（002882，硫化物）、<strong>赣锋锂业</strong>（002460，全固态+半固态布局）、<strong>当升科技</strong>（300073，正极材料）、<strong>璞泰来</strong>（603659，负极+涂覆）；钠电方向——<strong>传艺科技</strong>、<strong>维科精密</strong>、<strong>元力股份</strong>。</p>
<p style="margin-bottom: 12px;"><strong>操作建议：</strong>固态电池属于<strong>主题性投资</strong>，商业化落地仍需2-3年，短期炒作成分较大。大会前后可能有脉冲行情，但持续性存疑。建议<strong>快进快出，不恋战</strong>，优先选择有真实技术布局+业绩支撑的标的（赣锋锂业、当升科技），回避纯概念股。</p>

<h3 style="color: #fbbf24; margin-top: 24px; margin-bottom: 12px;">📌 核心事件四：美国PPI与初请数据 — 美联储政策路径的二次确认</h3>
<p style="margin-bottom: 12px;"><strong>事件性质：宏观级影响，高不确定性</strong></p>
<p style="margin-bottom: 12px;">8月12日CPI数据是本周的"主菜"，13日PPI则是"甜点"但同样重要。当前市场对美联储9月政策预期处于微妙平衡：7月非农就业减少2.3万、失业率升至4.1%，支持降息；但通胀粘性担忧仍存，沃什主席已表态若通胀反弹则准备加息。</p>
<p style="margin-bottom: 12px;"><strong>情景推演：</strong>①<strong>良性情景</strong>（概率约55%）：PPI温和回升，核心PPI同比2.4-2.6%，初请22-24万——市场延续降息预期，科技股继续上行；②<strong>利空情景</strong>（概率约30%）：PPI超预期反弹，核心PPI>2.8%——加息预期升温，纳斯达克回调2-3%，A股科技股承压；③<strong>利多情景</strong>（概率约15%）：PPI大幅回落+初请飙升——强化降息预期，市场加速上涨。</p>
<p style="margin-bottom: 12px;"><strong>操作建议：</strong>CPI已在12日晚落地，PPI的边际影响相对减弱。但若CPI与PPI同向超预期（同高或同低），则会放大市场波动。<strong>周四开盘前建议降低杠杆，控制仓位在5-6成</strong>，等待数据落地后再根据方向加仓。重点关注北向资金流向——如果PPI超预期导致美元走强，北向可能短期流出。</p>

<h3 style="color: #60a5fa; margin-top: 24px; margin-bottom: 12px;">💡 其他重点事件点评</h3>
<p style="margin-bottom: 10px;"><strong>谷歌Pixel 11发布会：</strong>Tensor G6（台积电2nm）+Gemini深度整合是核心看点。对A股消费电子产业链影响有限，主要利好<strong>台积电供应链</strong>（但A股间接受益），重点关注<strong>立讯精密</strong>（消费电子代工龙头）、<strong>蓝思科技</strong>（盖板+结构件）、<strong>东山精密</strong>（FPC+散热）的情绪映射。</p>
<p style="margin-bottom: 10px;"><strong>具身智能机器人大会第二天：</strong>宇树科技申购资金释放后，机器人板块进入"会后验证期"。关注大会上是否有<strong>超预期的技术突破或量产消息</strong>，若只是常规产品展示，板块可能进入短期调整。核心标的：绿的谐波、鸣志电器、长盛轴承、三花智控。</p>
<p style="margin-bottom: 10px;"><strong>美丽中国建设发布会：</strong>政策层面的吹风会，短期催化有限，但长期看环保、新能源、绿色制造板块有政策托底。关注<strong>节能装备、固废处理、碳交易</strong>等细分方向的政策表述变化。</p>
<p style="margin-bottom: 10px;"><strong>江淮汽车解禁后续：</strong>12日解禁后，葛卫东10亿定增浮亏超50%是市场焦点。牛散选择"割肉"还是"扛周期"，将成为定增投资情绪的风向标。若葛卫东减持动作明确，可能拖累整个智能电动车板块情绪。</p>
<p style="margin-bottom: 10px;"><strong>本周前瞻提示：</strong>8月14日（周五）贵州茅台、海光信息、生益科技等重磅财报密集发布；同日成品油调价窗口开启（预计下调）；美国SEC 13F季度持仓截止披露。8月15日（周六）126家公司集中披露中报，为中报季最拥挤日之一，需提前避雷。</p>

</div>
'''

from v3.components.layout import Section
section_impact = Section(title="🔍 市场影响深度分析与操作建议", content=impact_html, icon="search", variant="highlight")
gen._components.append(section_impact)

# 6. 风险提示
gen.add_risk_warning([
    "美国PPI数据若超预期反弹，可能引发美联储加息预期升温，全球科技股估值承压",
    "中芯国际等半导体财报若仅符合预期，存在利好兑现回调风险",
    "固态电池、机器人等主题板块短期炒作成分大，需警惕大会后情绪退潮",
    "江淮汽车等大额解禁个股抛压可能扩散，回避解禁比例高+股价处于高位的品种",
    "8月14日1万亿买断式逆回购到期，资金面波动需关注央行续作态度",
    "本文所有分析基于公开信息整理，不构成投资建议，股市有风险，入市需谨慎"
])

# 发布
result = gen.publish(
    title="明日催化剂",
    report_type="tomorrow_catalyst",
    filename="20260813_明日催化剂.html",
    excerpt="闪迪投资者日定调HBF+中芯国际中报+SMM电池大会+谷歌Pixel 11发布+美国PPI数据，四大方向深度解读"
)

print("发布结果:", result)
print("报告生成完成!")
