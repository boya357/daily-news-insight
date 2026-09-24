import sys, os
os.chdir('/root/daily-news-insight')
sys.path.insert(0, '/root/daily-news-insight/v3')

from v3.generators.tomorrow_catalyst import TomorrowCatalystGenerator
from components.layout import Section, CardGrid
from components.data import StatCard

gen = TomorrowCatalystGenerator(
    date_str="20260925",
    subtitle="2026.09.25-09.27 · 中秋假期催化剂与节后展望"
)

# ========== 核心催化 ==========
core_text = """
<div style="line-height: 1.8; color: #f1f5f9; font-size: 14px;">
<p style="margin: 0 0 12px 0;"><strong style="color: #fbbf24;">⚠️ 重要提示：</strong>9月25日（周五）至9月27日（周日）为中秋国庆假期，A股休市三天，9月28日（周一）正常开市。本期报告聚焦假期三天重大事件及节后首个交易日催化剂。</p>
<p style="margin: 0 0 12px 0;"><strong style="color: #f87171;">🔥 顶级催化：习近平访美收官 + 中美AI对话落地</strong>——习近平主席9月23-25日对美国进行国事访问，期间中美元首会晤及AI首次对话成果是节后市场最大变量。中美经贸磋商已达成多项共识，若访美期间签署贸易理事会、投资理事会及AI治理框架协议，将对科技股、外贸板块形成重大利好。</p>
<p style="margin: 0 0 12px 0;"><strong style="color: #60a5fa;">💊 重磅催化：医药工业"十五五"规划发酵</strong>——工信部等十部门联合印发《医药工业发展"十五五"规划》，提出创新药产业规模年均增速20%+、FIC全球占比25%+等硬指标，首次系统部署AI制药、脑机接口、核素诊疗等前沿方向。假期消息面持续发酵，节后CXO、创新药、AI制药板块有望延续强势。</p>
<p style="margin: 0 0 12px 0;"><strong style="color: #34d399;">📈 数据催化：美联储9月加息靴子落地后首周</strong>——美联储9月加息25个基点已落地，假期期间将有多位美联储官员讲话，可能释放后续货币政策信号。若释放鸽派信号，将进一步缓解全球流动性压力，利好成长股估值修复。</p>
<p style="margin: 0;"><strong style="color: #a78bfa;">🎯 节后焦点：三季报业绩验证窗口开启</strong>——上交所三季报预约披露时间出炉，有研新材将于10月13日率先披露。节后市场将正式进入三季报业绩验证期，有业绩支撑的科技权重股有望迎来补涨行情。</p>
</div>
"""
gen.add_key_catalyst(core_text)

# ========== 事件日历 ==========
events = [
    {
        'type': 'meeting',
        'title': '习近平主席对美国进行国事访问（9月23-25日）',
        'description': '应美国总统特朗普邀请，国家主席习近平于当地时间9月23日至25日对美国进行国事访问。期间中美元首会晤、中美经贸磋商第八轮后续落实、AI治理首次对话等议题备受关注。访问收官成果将直接影响节后A股市场情绪。',
        'category': '顶级外交事件'
    },
    {
        'type': 'policy',
        'title': '工信部等十部门印发《医药工业发展"十五五"规划》',
        'description': '到2030年生物医药研发应用稳居世界前列，创新药产业规模年均增速20%+，FIC全球占比25%+，医药工业上市企业平均研发投入强度年均不低于10%。首次系统部署AI制药、脑机接口、核素诊疗、太空制药等前沿方向。',
        'category': '产业政策'
    },
    {
        'type': 'policy',
        'title': '央行第三季度货币政策例会：继续实施适度宽松货币政策',
        'description': '央行货币政策委员会2026年第三季度例会于9月19日召开，明确要继续实施适度宽松的货币政策，加大逆周期调节力度，更好发挥货币政策工具的总量和结构双重功能，加强货币财政政策协同配合。',
        'category': '货币政策'
    },
    {
        'type': 'data',
        'title': '美联储官员密集讲话（假期期间）',
        'description': '9月加息25个基点靴子落地后，假期期间多位美联储官员将发表讲话，包括美联储古尔斯比等，市场将密切关注其对后续货币政策路径的指引，判断是否为"最后一次加息"。',
        'category': '海外货币政策'
    },
    {
        'type': 'earnings',
        'title': '亨通光电拟定增募资66.36亿元投向光通信与CPO',
        'description': '亨通光电发布定增预案，拟募资不超66.36亿元，投向新一代光纤研发生产、CPO先进封装研发、AI先进光互联等项目，进一步加码光通信与AI算力基础设施赛道。节后复牌有望带动光通信板块情绪。',
        'category': '定增预案'
    },
    {
        'type': 'meeting',
        'title': '第五届全球数字贸易博览会（9月23-27日，杭州）',
        'description': '李强总理出席启动仪式并致辞，马来西亚总理安瓦尔、吉尔吉斯斯坦总理卡瑟马利耶夫出席。博览会聚焦数字贸易、跨境电商、数字经济合作等议题，相关数字贸易、跨境电商概念股有望受益。',
        'category': '国家级展会'
    },
    {
        'type': 'data',
        'title': '粤芯半导体IPO完成申购（9月24日）',
        'description': '粤芯半导体发行价12.01元/股，9月24日完成网上网下申购，中签号将于9月29日公布。作为国内模拟芯片龙头企业，其IPO进程对半导体板块情绪有一定带动作用。',
        'category': '新股申购'
    },
    {
        'type': 'general',
        'title': '第48届世界技能大赛（9月22-27日，上海）',
        'description': '被誉为"技能奥林匹克"的世界技能大赛在上海举办，马来西亚总理安瓦尔出席开幕式。涉及职业教育、技能培训、高端制造相关概念股。',
        'category': '国际赛事'
    },
]
gen.add_events_calendar(events)

# ========== 限售股解禁 ==========
unlock_cards = []
unlock_data = [
    {
        'name': '科瑞思（301660）',
        'value': '3437.53万股',
        'subtitle': '占总股本62.22% · 9月28日解禁 · 首发原股东',
        'icon': 'alert-triangle',
        'variant': 'danger'
    },
    {
        'name': '建发致新（301584）',
        'value': '18487.69万股',
        'subtitle': '占总股本43.68% · 9月28日解禁 · 首发前股份',
        'icon': 'alert-triangle',
        'variant': 'danger'
    },
    {
        'name': '东方钽业（000962）',
        'value': '1148.17万股',
        'subtitle': '占总股本2.18% · 9月28日解禁 · 定增股份',
        'icon': 'lock',
        'variant': 'warning'
    },
    {
        'name': '广哈通信（300711）',
        'value': '3126.30万股',
        'subtitle': '占总股本11.15% · 9月30日解禁 · 定增股份',
        'icon': 'lock',
        'variant': 'warning'
    },
    {
        'name': '劲旅环境（001230）',
        'value': '91万股',
        'subtitle': '占比约0.9% · 9月28日解禁 · 股权激励',
        'icon': 'lock',
        'variant': 'info'
    },
    {
        'name': '傲农生物（603363）',
        'value': '9.49万股',
        'subtitle': '占比0.0035% · 9月30日解禁 · 重整转增股',
        'icon': 'lock',
        'variant': 'info'
    },
]
for item in unlock_data:
    unlock_cards.append(StatCard(
        title=item['name'],
        value=item['value'],
        subtitle=item['subtitle'],
        icon=item['icon'],
        variant=item['variant']
    ))

grid = CardGrid(unlock_cards, cols=3)
section = Section(title="🔒 限售股解禁详情", content=grid.render(), icon="lock")
gen._components.append(section)

# ========== 新股申购 ==========
ipo_cards = []
ipo_data = [
    {
        'name': '南方乳业（920196）',
        'value': '14.21元/股',
        'subtitle': '北交所 · 9月28日申购 · 发行3518.52万股',
        'icon': 'trending-up',
        'variant': 'success'
    },
    {
        'name': '联亚药业（301569）',
        'value': '7.00元/股',
        'subtitle': '创业板 · 9月28日申购 · 发行13373.96万股',
        'icon': 'trending-up',
        'variant': 'success'
    },
    {
        'name': '粤芯半导体（301660）',
        'value': '12.01元/股',
        'subtitle': '创业板 · 9月24日已申购 · 中签号9月29日公布',
        'icon': 'clock',
        'variant': 'info'
    },
]
for item in ipo_data:
    ipo_cards.append(StatCard(
        title=item['name'],
        value=item['value'],
        subtitle=item['subtitle'],
        icon=item['icon'],
        variant=item['variant']
    ))

grid2 = CardGrid(ipo_cards, cols=3)
section2 = Section(title="📈 新股申购日历", content=grid2.render(), icon="trending-up")
gen._components.append(section2)

# ========== 经济数据公布 ==========
data_list = [
    {'name': '美国9月PCE物价指数', 'prev': '+2.5%', 'expect': '待公布', 'time': '假期期间'},
    {'name': '美国8月个人支出', 'prev': '+0.4%', 'expect': '待公布', 'time': '假期期间'},
    {'name': '中国8月规模以上工业企业利润', 'prev': '待公布', 'expect': '有望延续修复', 'time': '9月底'},
    {'name': '欧元区9月经济景气指数', 'prev': '90.2', 'expect': '待公布', 'time': '9月29日'},
]
gen.add_data_release(data_list)

# ========== 海外大事提醒 ==========
overseas_content = """
<div style="display: flex; flex-direction: column; gap: 12px;">
    <div style="background: rgba(30,30,50,0.5); border: 1px solid rgba(255,255,255,0.08); border-radius: 12px; padding: 14px 16px;">
        <div style="font-size: 14px; font-weight: 600; color: #f1f5f9; margin-bottom: 6px;">🇺🇸 习近平访美收官（9月25日）</div>
        <div style="font-size: 12px; color: #94a3b8; line-height: 1.6;">国家主席习近平9月23-25日对美国进行国事访问，中美元首会晤成果、AI对话框架、经贸协议签署等是全球市场最大关注点。若达成实质性共识，将大幅提振全球风险资产信心。</div>
    </div>
    <div style="background: rgba(30,30,50,0.5); border: 1px solid rgba(255,255,255,0.08); border-radius: 12px; padding: 14px 16px;">
        <div style="font-size: 14px; font-weight: 600; color: #f1f5f9; margin-bottom: 6px;">🏛️ 第81届联合国大会一般性辩论（持续中）</div>
        <div style="font-size: 12px; color: #94a3b8; line-height: 1.6;">多国领导人聚焦中东局势，美伊代表在纽约会谈3小时（自7月停火破裂后首次接触）。国家副主席韩正9月24-26日赴纽约出席联大一般性辩论并出席全球发展倡议5周年高级别对话会。</div>
    </div>
    <div style="background: rgba(30,30,50,0.5); border: 1px solid rgba(255,255,255,0.08); border-radius: 12px; padding: 14px 16px;">
        <div style="font-size: 14px; font-weight: 600; color: #f1f5f9; margin-bottom: 6px;">💵 美联储官员密集发声</div>
        <div style="font-size: 12px; color: #94a3b8; line-height: 1.6;">9月加息靴子落地后，假期期间多位美联储官员将发表讲话。市场重点关注是否释放"最后一次加息"的鸽派信号，以及对通胀和经济前景的最新判断。</div>
    </div>
    <div style="background: rgba(30,30,50,0.5); border: 1px solid rgba(255,255,255,0.08); border-radius: 12px; padding: 14px 16px;">
        <div style="font-size: 14px; font-weight: 600; color: #f1f5f9; margin-bottom: 6px;">⚡ 美伊霍尔木兹海峡局势</div>
        <div style="font-size: 12px; color: #94a3b8; line-height: 1.6;">伊朗要求各战线全面止战、美国停止"侵略行径"作为重开霍尔木兹海峡的条件。美国财长贝森特警告伊朗航空公司将被全球停飞。假期期间地缘局势变化将显著影响原油价格及全球风险偏好。</div>
    </div>
    <div style="background: rgba(30,30,50,0.5); border: 1px solid rgba(255,255,255,0.08); border-radius: 12px; padding: 14px 16px;">
        <div style="font-size: 14px; font-weight: 600; color: #f1f5f9; margin-bottom: 6px;">🇮🇹 意大利通过法案重启核能发电</div>
        <div style="font-size: 12px; color: #94a3b8; line-height: 1.6;">意大利议会通过法案将重启核能发电，欧洲能源结构转型再进一步，对全球核电产业链有中长期利好影响。中国核电出海概念值得关注。</div>
    </div>
</div>
"""
section_overseas = Section(title="🌍 海外大事提醒", content=overseas_content, icon="globe")
gen._components.append(section_overseas)

# ========== 重点事件深度影响分析 ==========
deep_analysis = """
<div style="line-height: 1.9; color: #e2e8f0; font-size: 14px;">
<h3 style="color: #fbbf24; margin: 16px 0 10px 0; font-size: 16px;">一、习近平访美收官：节后市场最大变量，AI+经贸双主线</h3>
<p style="margin: 0 0 10px 0; text-indent: 2em;">本次习近平主席对美国事访问是当前全球资本市场最高级别事件。第八轮中美经贸磋商已在纽约举行，双方围绕落实已有共识、对等降税安排、建立贸易理事会和投资理事会、AI对话等议题进行了坦诚深入交流，达成多项共识。何立峰副总理与贝森特财长还举行了人工智能首次对话。</p>
<p style="margin: 0 0 10px 0; text-indent: 2em;">假期期间访美收官成果将直接决定节后A股开盘方向。若达成贸易理事会框架协议并明确降税时间表，外贸板块（纺织、家电、消费电子出口链）将迎来估值修复；若AI治理对话取得突破、双方同意建立AI合作框架，AI算力、半导体、光模块等科技赛道情绪将进一步提振。</p>
<p style="margin: 0 0 16px 0; text-indent: 2em;"><strong>影响标的：</strong>AI算力主线（英维克、中际旭创、新易盛）、半导体（雅克科技、华海诚科、粤芯半导体）、外贸出口（捷昌驱动、乐歌股份）、光通信（亨通光电、中天科技）。<strong>操作建议：</strong>假期前已持仓者可保留核心仓位过节，等待访美成果落地；空仓者建议关注9月28日开盘后消息面明朗再决定是否加仓，避免追高。</p>

<h3 style="color: #fbbf24; margin: 16px 0 10px 0; font-size: 16px;">二、医药"十五五"规划：政策底确认，机构补仓空间巨大</h3>
<p style="margin: 0 0 10px 0; text-indent: 2em;">工信部等十部门联合印发的《医药工业发展"十五五"规划》是近期医药板块爆发的核心催化剂。这份规划的含金量远超以往产业政策：一是给出了可量化的硬指标（创新药年均增速20%+、FIC全球占比25%+、上市企业研发强度≥10%），二是首次系统部署AI制药、脑机接口、核素诊疗、太空制药等前沿方向，三是明确支持CRO/CDMO面向全球市场服务能力。</p>
<p style="margin: 0 0 10px 0; text-indent: 2em;">从筹码结构看，截至二季度末剔除医药主题基金后，普通主动基金对医药持仓占比仅2.0%-2.9%，处于近三年极低水平。这意味着机构补仓空间巨大，本轮行情绝非单纯游资炒作，而是机构从低配向标配回补的中期过程。</p>
<p style="margin: 0 0 16px 0; text-indent: 2em;"><strong>影响标的：</strong>创新药CXO（药明生物、泰格医药、美迪西）、AI制药（英矽智能、成都先导、泓博医药）、生物试剂（百普赛斯、义翘神州、诺唯赞）、高端医疗器械。<strong>操作建议：</strong>短期涨幅较大不建议追高，可等待回调至5日均线附近分批建仓，优先选择有出海逻辑+业绩兑现的龙头标的。</p>

<h3 style="color: #fbbf24; margin: 16px 0 10px 0; font-size: 16px;">三、三季报业绩验证窗口：节后市场核心驱动切换</h3>
<p style="margin: 0 0 10px 0; text-indent: 2em;">上交所三季报预约披露时间已出炉，有研新材将于10月13日率先披露，标志着三季报业绩验证窗口正式开启。中信证券、华泰证券等主流券商均指出，三季报业绩披露可能是更大级别行情的催化剂，科技主线业绩逐步兑现是市场上行的核心支撑。</p>
<p style="margin: 0 0 10px 0; text-indent: 2em;">从产业趋势看，AI算力产业链三季报确定性最强：行云科技披露截至9月在手5年期算力长期框架订单规模达160亿元，V客户/VB客户/VC客户首批交付已于8月完成起租并确认收入，将在三季报中体现。光模块、液冷散热、存储芯片等环节也有望延续高景气。</p>
<p style="margin: 0 0 16px 0; text-indent: 2em;"><strong>影响标的：</strong>液冷散热（英维克、申菱环境）、光模块（中际旭创、新易盛）、存储芯片（铜冠铜箔、雅克科技）、算力租赁（行云科技、润泽智算）。<strong>操作建议：</strong>节后重点布局三季报确定性高的细分赛道龙头，回避纯概念炒作、无业绩支撑的高位股。</p>

<h3 style="color: #fbbf24; margin: 16px 0 10px 0; font-size: 16px;">四、节后首日解禁压力：科瑞思、建发致新需警惕</h3>
<p style="margin: 0 0 10px 0; text-indent: 2em;">节后首个交易日（9月28日）限售股解禁规模较大，需要重点关注两只高比例解禁标的：科瑞思（301660）首发原股东限售股份解禁3437.53万股，占总股本62.22%，而当前流通股仅1825.74万股，解禁后流通盘将扩大63.8%；建发致新（301584）解禁18487.69万股，占总股本43.68%，流通盘将从5371.43万股增至23859.12万股，增幅达344%。</p>
<p style="margin: 0 0 10px 0; text-indent: 2em;">科瑞思基本面堪忧：上半年净利润同比下降42.07%，扣非净利润更是转亏为-31.19万元，市盈率高达165倍，显著高于行业均值65倍。高比例解禁+业绩下滑+高估值，三重压力下短期股价承压风险较大。建发致新虽基本面较好，但流通盘骤增3倍以上，短期供需失衡也可能带来股价波动。</p>
<p style="margin: 0 0 16px 0; text-indent: 2em;"><strong>风险标的：</strong>科瑞思（301660）、建发致新（301584）。<strong>操作建议：</strong>持仓者建议在解禁前择机减仓规避短期冲击；空仓者不要在解禁初期抄底，等待解禁消化1-2周后再评估介入机会。</p>

<h3 style="color: #fbbf24; margin: 16px 0 10px 0; font-size: 16px;">五、亨通光电66亿定增加码CPO+AI光互联：光通信板块催化剂</h3>
<p style="margin: 0 0 10px 0; text-indent: 2em;">亨通光电抛出66.36亿元定增方案，投向新一代光纤研发生产、CPO先进封装研发、AI先进光互联等多个高景气项目，这是近期光通信行业最大规模的再融资案例，反映出行业龙头对AI光互联赛道长期景气度的高度看好。</p>
<p style="margin: 0 0 10px 0; text-indent: 2em;">定增项目中CPO先进封装研发、AI先进光互联项目合计投资超12亿元，直接对应算力网络升级的核心需求。随着AI大模型训练对光互联带宽要求持续提升，800G/1.6T光模块和CPO封装技术正加速渗透。亨通光电作为光通信全产业链龙头，定增加码将进一步巩固其在AI光互联领域的竞争力。</p>
<p style="margin: 0 0 10px 0; text-indent: 2em;"><strong>影响标的：</strong>光通信龙头（亨通光电、中天科技、长飞光纤）、CPO概念（中际旭创、新易盛、天孚通信）、光芯片（源杰科技、光迅科技）。<strong>操作建议：</strong>关注节后光通信板块联动效应，但定增对短期股价影响偏中性（存在稀释效应），不宜盲目追涨，可关注中际旭创等光模块龙头的回调机会。</p>

<h3 style="color: #fbbf24; margin: 16px 0 10px 0; font-size: 16px;">六、中美经贸磋商第八轮成果落地：对等降税+双理事会框架</h3>
<p style="margin: 0 0 10px 0; text-indent: 2em;">中美两国经贸团队在纽约举行的第八轮经贸磋商达成多项共识，包括落实已有经贸磋商共识、对等降税安排、建立贸易理事会和投资理事会、吉隆坡经贸磋商联合安排延期等。这是中美经贸关系持续改善的重要信号，也是自特朗普政府上台以来双方在经贸领域取得的最实质性进展。</p>
<p style="margin: 0 0 10px 0; text-indent: 2em;">对等降税安排将直接降低中美两国贸易成本，利好出口占比高的企业；贸易理事会和投资理事会的建立将为中美经贸关系提供常态化沟通机制，降低政策不确定性；AI对话机制的建立则意味着双方在高科技领域从对抗走向竞合。</p>
<p style="margin: 0 0 10px 0; text-indent: 2em;"><strong>影响标的：</strong>出口链（捷昌驱动、乐歌股份、海象新材）、跨境电商（吉宏股份、安克创新）、科技股（中际旭创、英伟达供应链）。<strong>操作建议：</strong>若假期访美成果超预期，节后可适当配置出口链弹性标的，但需注意利好兑现后的回调风险。</p>
</div>
"""
gen.add_impact_analysis(deep_analysis)

# ========== 催化深度分析（Skill增强） ==========
gen.add_catalyst_deep_analysis(events[:3])

# ========== 风险提示 ==========
risks = [
    "习近平访美成果不及预期，中美关系再生变数",
    "假期期间地缘冲突升级（中东/俄乌局势），引发全球避险情绪",
    "美联储官员释放超预期鹰派信号，全球流动性再度收紧",
    "节后首日大规模限售股解禁冲击市场情绪",
    "医药板块短期涨幅过大存在获利回吐风险",
    "三季报业绩验证期部分科技股业绩不及预期"
]
gen.add_risk_warning(risks)

# ========== 发布 ==========
result = gen.publish(
    title="中秋假期催化剂与节后展望",
    report_type="tomorrow_catalyst",
    excerpt="习近平访美收官+医药十五五规划发酵+三季报窗口开启+节后解禁压力全景分析"
)
print("发布结果:", result)
