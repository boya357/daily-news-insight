#!/usr/bin/env python3
"""2026年8月17日 每日新闻洞察生成 - 周一·AMD+6.5%发债扩AI产能·存储芯片融资一周砸20亿·四部门发布集成电路税收优惠·7月社融22.25万亿·本周超级事件周"""
import sys, os, shutil, json
WORK_DIR = '/root/daily-news-insight'
sys.path.insert(0, os.path.join(WORK_DIR, 'v3'))
from generators.daily_pro import DailyReportProGenerator

gen = DailyReportProGenerator(
    date_str='2026年8月17日', weekday='星期一',
    subtitle='2026年8月17日 周一 · 美股微跌费半-0.31%·AMD+6.5%发债扩AI·存储融资一周20亿·集成电路税收优惠·本周四大事件定方向',
    data_dir=os.path.join(WORK_DIR, 'data')
)

def render_cards(items):
    out = ''
    for i in items:
        c = 'text-red-400' if i['up'] else 'text-green-400'
        bg = 'from-red-500/20 to-orange-500/10 border-red-500/20' if i['up'] else 'from-green-500/20 to-emerald-500/10 border-green-500/20'
        out += '<div class="bg-gradient-to-br %s border rounded-lg p-3 text-center transition-all duration-300 hover:scale-105"><div class="text-xs text-white/60 mb-1">%s</div><div class="text-sm font-bold %s">%s</div></div>' % (bg, i['name'], c, i['change'])
    return out

def render_list(items):
    out = ''
    for i in items:
        c = 'text-red-400' if i['up'] else 'text-green-400'
        out += '<div class="flex items-center justify-between py-2 border-b border-white/5 last:border-0"><span class="text-sm text-white/70">%s</span><span class="text-sm font-semibold %s">%s</span></div>' % (i['name'], c, i['change'])
    return out


gen.set_tldr(
    key_points=[
        '美股高位震荡微跌：道指-0.20%、标普-0.17%、纳指-0.28%；费城半导体-0.31%高位整固；AMD+6.5%创历史新高（47.5亿美元发债扩AI产能+BofA上调服务器CPU市场至2100亿），博通-5.94%、应用材料-5.12%拖累指数',
        '存储超级周期继续：美光+2.30%续创新高，韩股三星+2.43%、SK海力士+3.26%；融资资金一周狂砸20亿加仓存储芯片（江波龙+12亿、兆易创新+8.77亿）；摩根大通上调2028年存储市场至1.82万亿美元',
        '周末政策利好密集：①四部门发布集成电路/工业母机税收优惠（非货币性资产交换所得分5年缴纳）；②跨国公司跨境资金池业务全国推广；③7月社融新增22.25万亿，企业债券+政府债双发力；④国家电网战略投资国盛量子',
        '上周五A股反弹修复：沪指+0.01%收3927点，深成指+0.45%，创业板+1.12%，科创50持平；持仓全线反弹（铜冠+3.20%、英维克+2.96%、雅克+1.15%），市场情绪从恐慌转向中性',
        '本周超级事件周：7月经济数据、LPR报价、世界机器人大会、美联储会议纪要四大事件密集落地，将决定8月中下旬行情方向'
    ],
    operation_advice='周一开盘：周末政策利好+美股科技分化，A股预计震荡偏强。存储芯片（融资加仓）、液冷（台系业绩验证）、集成电路（税收优惠）三个方向关注。但上方3960压力仍在，仓位控制在4成，利用反弹继续减仓高位股，等待中报落地后的布局机会',
    risk_level='中等',
    suggested_position='4成'
)

gen.set_quick_anchors([
    {'id': 'section-隔夜全球市场深度解读', 'title': '全球市场', 'icon': '🌍'},
    {'id': 'section-A股昨日复盘与今日展望', 'title': 'A股复盘', 'icon': '📊'},
    {'id': 'section-核心题材与今日催化', 'title': '核心题材', 'icon': '🔥'},
    {'id': 'section-持仓诊断与操作建议', 'title': '持仓诊断', 'icon': '💼'},
    {'id': 'section-空方视角与多空博弈', 'title': '空方视角', 'icon': '⚖️'},
    {'id': 'section-预判验证闭环', 'title': '预判验证', 'icon': '🔮'},
    {'id': 'section-教训库引用', 'title': '教训库', 'icon': '📚'},
])

gen.set_holdings([
    {'name': '英维克', 'code': '002837'},
    {'name': '铜冠铜箔', 'code': '301217'},
    {'name': '雅克科技', 'code': '002409'},
    {'name': '*ST建艺', 'code': '002789'},
])

gen.set_og(
    description='每日新闻洞察 2026年8月17日：AMD+6.5%发债扩AI产能、存储融资一周20亿、集成电路税收优惠、7月社融22.25万亿、本周四大事件定方向',
)

gen.add_global_market()

global_cards1 = render_cards([
    {"name":"道琼斯","change":"-0.20%","up":False},
    {"name":"标普500","change":"-0.17%","up":False},
    {"name":"纳斯达克","change":"-0.28%","up":False},
    {"name":"费城半导体","change":"-0.31%","up":False},
    {"name":"日经225","change":"-0.90%","up":False},
    {"name":"恒生指数","change":"-1.10%","up":False},
])
global_list1 = render_list([
    {"name":"WTI原油","change":"-0.24%/$81.28","up":False},
    {"name":"布伦特原油","change":"-0.07%/$88.46","up":False},
    {"name":"COMEX黄金","change":"+0.09%/$4441","up":True},
    {"name":"COMEX白银","change":"+0.38%/$65.35","up":True},
])
global_list2 = render_list([
    {"name":"三星电子","change":"+2.43%","up":True},
    {"name":"SK海力士","change":"+3.26%","up":True},
    {"name":"美光科技","change":"+2.30%","up":True},
    {"name":"台积电ADR","change":"-0.96%","up":False},
])
global_list3 = render_list([
    {"name":"英伟达","change":"-0.06%/$225.16","up":False},
    {"name":"AMD","change":"+6.50%/$514.39","up":True},
    {"name":"微软","change":"-0.30%/$495.40","up":False},
    {"name":"苹果","change":"+0.22%/$305.93","up":True},
    {"name":"博通","change":"-5.94%/$392.99","up":False},
    {"name":"英特尔","change":"-1.97%/$102.50","up":False},
    {"name":"应用材料","change":"-5.12%/$507.18","up":False},
    {"name":"阿斯麦","change":"-0.21%/$1844.08","up":False},
])

global_html = '''
<div class="grid md:grid-cols-3 gap-4">
  <div class="md:col-span-2">
    <div class="text-white font-semibold mb-3 flex items-center gap-2"><span>🌍</span><span>隔夜全球市场 · 美股高位整固·AMD+6.5%独涨·存储继续走强</span></div>
    <div class="grid grid-cols-3 md:grid-cols-6 gap-2">{0}</div>
    <p class="text-xs text-white/50 mt-3 leading-relaxed">
      ⚡ <b class="text-yellow-400">核心要点：美股三大指数小幅收跌，纳指-0.28%；费城半导体-0.31%高位整固；AMD+6.5%创历史新高（47.5亿发债+ BofA上调服务器CPU市场），博通-5.94%、应用材料-5.12%大幅拖累；存储板块继续强势，美光+2.30%、SK海力士+3.26%、三星+2.43%</b>——<br>
      ①<b>AMD创历史新高+6.5%</b>：完成史上最大规模债券发行（47.5亿美元，是2025年3月发行的3倍多），全部用于AI数据中心扩产；BofA上调2030年服务器CPU市场至2100亿美元（原1700亿），AMD为首选标的。Helios AI机架Q4开始出货，客户包括Meta、OpenAI、Anthropic（Anthropic承诺2GW MI450订单）。数据中心Q2营收+107%至67.2亿美元。<br>
      ②<b>存储板块持续走强</b>：美光+2.30%续创新高，New Street Research将美光目标价大幅上调，预计2030年市值可达2-3万亿美元。韩股三星+2.43%、SK海力士+3.26%、三星SDI+5.95%。摩根大通上调2026-2028年存储市场规模4-8%，2028年达1.82万亿美元，供需短缺未来两年持续。<br>
      ③<b>半导体设备股回调</b>：应用材料-5.12%、博通-5.94%领跌费半。博通下跌或与AI芯片竞争加剧有关，AMD在AI加速卡和机架层面直接对标英伟达/博通。设备股回调反映市场对资本开支周期的担忧。<br>
      ④<b>英伟达微跌0.06%</b>：盘整于225美元附近，等待8月26日Q2财报。分析师一致预期Q2营收约920亿美元、EPS 2.06美元，Q3指引超1030亿美元。市场关注Blackwell产能和中国业务清零后的增长可持续性。<br>
      ⑤<b>大宗商品微幅波动</b>：WTI原油-0.24%收81.28美元，布伦特-0.07%收88.46美元。美伊谅解备忘录8月17日到期，目前无达成协议迹象，地缘风险仍存但市场已逐步消化。COMEX黄金+0.09%收4441美元。<br>
      ⑥<b>亚太市场普跌</b>：日经225-0.90%、恒生指数-1.10%。港股科技股承压，恒生科技指数编制方法修订（扩容至50只）预计带来360亿港元被动资金增量。
    </p>
  </div>
  <div class="space-y-4">
    <div>
    <div class="text-white font-semibold mb-3 flex items-center gap-2"><span>🛢️</span><span>大宗商品</span></div>
      <div class="bg-white/5 rounded-lg p-3">{1}</div></div>
    <div>
    <div class="text-white font-semibold mb-3 flex items-center gap-2"><span>🇰🇷</span><span>韩股存储双雄</span></div>
      <div class="bg-white/5 rounded-lg p-3">{2}</div></div>
    <div>
    <div class="text-white font-semibold mb-3 flex items-center gap-2"><span>💻</span><span>美股科技龙头</span></div>
      <div class="bg-white/5 rounded-lg p-3">{3}</div></div>
  </div>
</div>'''.format(global_cards1, global_list1, global_list2, global_list3)
gen.add_section("隔夜全球市场深度解读", global_html, "🌍")

# A股昨日复盘
ashare_html = '''
<div class="space-y-4">
<div class="grid md:grid-cols-4 gap-3">
  <div class="bg-gradient-to-br from-red-500/20 to-orange-500/10 border border-red-500/30 rounded-xl p-3 text-center">
    <div class="text-xs text-white/60 mb-1">上证指数</div>
    <div class="text-xl font-bold text-red-400">3927.18</div>
    <div class="text-xs text-red-400">+0.01%</div>
  </div>
  <div class="bg-gradient-to-br from-red-500/20 to-orange-500/10 border border-red-500/30 rounded-xl p-3 text-center">
    <div class="text-xs text-white/60 mb-1">深证成指</div>
    <div class="text-xl font-bold text-red-400">14354.31</div>
    <div class="text-xs text-red-400">+0.45%</div>
  </div>
  <div class="bg-gradient-to-br from-red-500/20 to-orange-500/10 border border-red-500/30 rounded-xl p-3 text-center">
    <div class="text-xs text-white/60 mb-1">创业板指</div>
    <div class="text-xl font-bold text-red-400">3626.30</div>
    <div class="text-xs text-red-400">+1.12%</div>
  </div>
  <div class="bg-gradient-to-br from-green-500/20 to-emerald-500/10 border border-green-500/30 rounded-xl p-3 text-center">
    <div class="text-xs text-white/60 mb-1">科创50</div>
    <div class="text-xl font-bold text-green-400">1717.68</div>
    <div class="text-xs text-green-400">-0.00%</div>
  </div>
</div>

<div class="grid md:grid-cols-2 gap-4">
  <div class="bg-white/5 rounded-xl p-4">
    <h4 class="text-white font-semibold mb-3 flex items-center gap-2"><span>📈</span> 领涨/反弹板块</h4>
    <div class="space-y-1 text-xs">
      <div class="flex justify-between"><span class="text-white/70">创业板/成长股</span><span class="text-red-400">+1%~+2%</span></div>
      <div class="flex justify-between"><span class="text-white/70">存储芯片/材料</span><span class="text-red-400">+1%~+3%</span></div>
      <div class="flex justify-between"><span class="text-white/70">液冷/算力硬件</span><span class="text-red-400">+2%~+3%</span></div>
      <div class="flex justify-between"><span class="text-white/70">PCB/铜箔</span><span class="text-red-400">+2%~+4%</span></div>
      <div class="flex justify-between"><span class="text-white/70">医药/CRO超跌反弹</span><span class="text-red-400">+0.5%~+1%</span></div>
    </div>
  </div>
  <div class="bg-white/5 rounded-xl p-4">
    <h4 class="text-white font-semibold mb-3 flex items-center gap-2"><span>📉</span> 领跌/弱势板块</h4>
    <div class="space-y-1 text-xs">
      <div class="flex justify-between"><span class="text-white/70">科创50/硬科技</span><span class="text-green-400">持平~-1%</span></div>
      <div class="flex justify-between"><span class="text-white/70">ST板块</span><span class="text-green-400">弱势震荡</span></div>
      <div class="flex justify-between"><span class="text-white/70">房地产/金融</span><span class="text-green-400">分化调整</span></div>
      <div class="flex justify-between"><span class="text-white/70">新能源/锂电</span><span class="text-yellow-400">低位震荡</span></div>
      <div class="flex justify-between"><span class="text-white/70">军工/航天</span><span class="text-green-400">继续回调</span></div>
    </div>
  </div>
</div>

<div class="bg-white/5 rounded-xl p-4">
  <h4 class="text-white font-semibold mb-3 flex items-center gap-2"><span>🔍</span> 上周五核心逻辑深度拆解</h4>
  <div class="text-xs text-white/70 space-y-3 leading-relaxed">
    <div class="bg-white/5 rounded-lg p-3">
      <p class="text-yellow-400 font-semibold mb-1">① 超跌反弹+情绪修复，从恐慌回到中性</p>
      <p>经历了周四放量大跌（2.55万亿+4300股跌）后，周五市场迎来技术性反弹。创业板+1.12%领涨，深成指+0.45%，沪指基本平收。涨跌比约1.17，赚钱效应小幅回暖。市场情绪从周四的恐慌（恐惧贪婪约35）修复至中性（50），但成交量明显萎缩，说明反弹力度有限，更多是缩量企稳而非增量入场。</p>
    </div>
    <div class="bg-white/5 rounded-lg p-3">
      <p class="text-yellow-400 font-semibold mb-1">② 科技成长股反弹，存储/液冷/铜箔领涨</p>
      <p>隔夜美股存储板块暴涨（闪迪+13.67%）的传导效应在周五显现，A股存储板块全线反弹：雅克科技+1.15%、铜冠铜箔+3.20%（停牌前）、华海诚科+3.51%。液冷方向英维克+2.96%，台系液冷厂商Q2业绩暴增（奇鋐+139%、双鸿+513%）验证行业高景气。铜冠铜箔因董秘无法履职消息，午后临停，但收盘仍涨3.2%。</p>
    </div>
    <div class="bg-white/5 rounded-lg p-3">
      <p class="text-yellow-400 font-semibold mb-1">③ 缩量反弹=观望情绪浓，增量资金未入场</p>
      <p>周五两市成交约2.25万亿（较周四2.55万亿缩量约3000亿），缩量反弹说明：一是前期出逃资金没有回来，二是场外资金仍在观望等待中报落地。7月金融数据已经公布（社融22.25万亿），但市场反应平淡，说明流动性宽松≠股市上涨，关键还看盈利预期。</p>
    </div>
    <div class="bg-white/5 rounded-lg p-3">
      <p class="text-yellow-400 font-semibold mb-1">④ 周末政策密集释放，为周一提供情绪支撑</p>
      <p>周末公布多项利好：①四部门发布集成电路/工业母机税收优惠；②跨国公司跨境资金池全国推广；③7月社融数据超预期（前7月22.25万亿）；④国家电网战投国盛量子。这些政策将为周一开盘提供正面支撑，但能否形成持续上涨还需观察成交量配合。</p>
    </div>
  </div>
</div>

<div class="bg-yellow-500/10 border border-yellow-500/30 rounded-xl p-4">
  <h4 class="text-yellow-300 font-semibold mb-2 flex items-center gap-2"><span>🎯</span> 今日展望（8月17日周一）</h4>
  <p class="text-xs text-white/70 leading-relaxed">
    周末政策利好密集释放+美股科技分化（AMD涨、设备股跌），今日A股预计震荡偏强，沪指有望冲击3950-3960压力位。但上方套牢盘沉重，一次性突破难度大，大概率冲高回落或震荡整固。<br>
    <b class="text-yellow-400">操作策略：</b>仓位4成防御为主，不追高反弹。周末利好的三个方向（存储芯片、集成电路设备材料、液冷算力）可关注开盘力度，但高开就是减仓机会，不要追涨。本周四大事件（经济数据、LPR、机器人大会、美联储纪要）密集落地，建议控制仓位观望，等待信号明确后再加仓。
  </p>
</div>
</div>
'''
gen.add_section("A股昨日复盘与今日展望", ashare_html, "📊")

# 核心题材与今日催化
catalyst_html = '''
<div class="space-y-4">
  <div class="bg-gradient-to-br from-red-500/20 to-orange-500/10 border border-red-500/30 rounded-xl p-4">
    <h4 class="text-white font-semibold mb-3 flex items-center gap-2"><span>🔥</span> 催化一：存储超级周期深化·融资资金一周砸20亿·摩根大通上调市场至1.82万亿【S级】</h4>
    <div class="text-xs text-white/70 space-y-2 leading-relaxed">
      <p><b class="text-yellow-400">事件：</b>①近一周（8/10-8/16）存储芯片赛道获融资资金大幅加仓，江波龙+12亿、兆易创新+8.77亿、普冉股份+5.23亿，三只票合计融资净买入超26亿元；②摩根大通上调2026-2028年全球存储市场规模4-8%，2026年约9690亿→2027年1.44万亿→2028年1.82万亿美元；③美光+2.30%续创新高，New Street预测2030年美光市值可达2-3万亿美元；④SK海力士上半年从英伟达获得销售额超17万亿韩元（占总销售额13%），设备投资同比增70%。</p>
      <p><b class="text-yellow-400">核心逻辑：</b>AI驱动存储需求结构性爆发，HBM/企业级SSD供需缺口持续扩大。不同于传统存储周期的"繁荣-萧条"模式，AI存储需求具备更强的抗周期性（LTA长期协议锁定）。存储涨价已从DRAM/NAND蔓延到HBM，未来2年供应短缺格局难以改变。</p>
      <p><b class="text-yellow-400">A股映射：</b>融资资金（杠杆资金）持续加仓存储芯片说明机构资金对中期行情有信心。但短期A股存储股经过反弹后（雅克从127→151=+19%），上方套牢盘仍重，持续性取决于成交量。建议关注业绩确定性强的材料/设备龙头，规避纯题材炒作标的。</p>
      <p><b class="text-yellow-400">受益标的：</b>雅克科技（前驱体）、华海诚科（塑封料）、北方华创（设备）、中微公司（刻蚀）、江波龙（存储模组）、兆易创新（NOR Flash）</p>
    </div>
  </div>

  <div class="bg-gradient-to-br from-orange-500/20 to-yellow-500/10 border border-orange-500/30 rounded-xl p-4">
    <h4 class="text-white font-semibold mb-3 flex items-center gap-2"><span>💰</span> 催化二：四部门发布集成电路/工业母机税收优惠·跨境资金池全国推广【A级】</h4>
    <div class="text-xs text-white/70 space-y-2 leading-relaxed">
      <p><b class="text-yellow-400">事件：</b>①财政部等四部门发布税费支持政策，2026-2028年集成电路、工业母机企业非货币性资产交换所得可分5年分期缴纳税款，有效缓解高端制造企业资产重组、产能整合税务压力；②央行、外汇局通知，跨国公司本外币跨境资金集中运营业务全国推广，门槛降低（国际收支规模≥7亿→自贸区内3.5亿），大幅简化跨境资金调配流程。</p>
      <p><b class="text-yellow-400">政策意图：</b>双政策组合拳支持硬科技产业发展。税收优惠直接利好半导体企业并购重组和产能扩张（比如存储芯片扩产、先进封装产线建设）；跨境资金池全国推广则利好有海外布局的科技企业，提升资金使用效率。体现了"科技自立自强"的国家战略导向。</p>
      <p><b class="text-yellow-400">市场影响：</b>对半导体设备、材料、工业母机等方向构成政策利好。但注意：这不是"大水漫灌"式的刺激，而是精准滴灌的产业政策，对相关公司业绩有实质利好但短期股价催化有限，更多是中长期支撑。</p>
    </div>
  </div>

  <div class="bg-gradient-to-br from-blue-500/20 to-cyan-500/10 border border-blue-500/30 rounded-xl p-4">
    <h4 class="text-white font-semibold mb-3 flex items-center gap-2"><span>📊</span> 催化三：AMD+6.5%创历史新高·AI算力竞争进入系统级对决【A级】</h4>
    <div class="text-xs text-white/70 space-y-2 leading-relaxed">
      <p><b class="text-yellow-400">事件：</b>AMD股价大涨6.50%收514.39美元创历史新高，市值突破3200亿美元。催化剂：①完成史上最大规模47.5亿美元债券发行（3倍于2025年3月），全部用于AI数据中心产能扩张；②BofA上调2030年服务器CPU市场至2100亿美元（原1700亿），AMD为首选标的；③Helios AI机架Q4量产出货，客户包括Meta、OpenAI、Anthropic（后者承诺2GW MI450订单）。</p>
      <p><b class="text-yellow-400">核心逻辑：</b>AI算力竞争从"卖芯片"升级到"卖整柜"。英伟达Vera Rubin NVL72（72颗GPU/柜）vs AMD Helios（72颗GPU/柜），系统级对决正式开打。AMD的优势在于开放架构+更低的单Token成本+CPU+GPU协同（EPYC+Instinct组合），英伟达优势在于CUDA生态+先发优势。两家竞争的结果是：AI算力供给加速，对液冷、PCB、光模块等上游供应链是利好。</p>
      <p><b class="text-yellow-400">A股映射：</b>AI算力基础设施需求持续超预期，液冷（英维克等）、PCB铜箔（铜冠铜箔等）、光模块、服务器产业链持续受益。AMD崛起意味着供应链多元化，对有海外客户的国内供应链公司是额外增量。</p>
    </div>
  </div>

  <div class="bg-gradient-to-br from-purple-500/20 to-pink-500/10 border border-purple-500/30 rounded-xl p-4">
    <h4 class="text-white font-semibold mb-3 flex items-center gap-2"><span>📅</span> 催化四：本周超级事件周·四大事件定方向【A级】</h4>
    <div class="text-xs text-white/70 space-y-2 leading-relaxed">
      <p><b class="text-yellow-400">事件：</b>本周（8/17-8/21）是8月行情关键周，四大重磅事件密集落地：</p>
      <p>①<b>7月经济数据</b>：GDP、工业增加值、社零、固投等（8月18日左右），判断经济复苏强度的核心指标；<br>
      ②<b>LPR报价</b>：8月20日，关注是否下调1年期/5年期LPR，配合政府债发行的货币政策动向；<br>
      ③<b>世界机器人大会</b>：8月21日开幕，人形机器人产业链催化，宇树科技上市后首秀；<br>
      ④<b>美联储会议纪要</b>：8月21日凌晨，9月加息路径的关键信号，当前加息概率约38%。</p>
      <p><b class="text-yellow-400">影响：</b>四大事件将从宏观经济、货币政策、产业催化、海外流动性四个维度影响A股。建议在事件落地前控制仓位，观望为主。如果经济数据超预期+LPR下调=利好周期和科技；如果美联储偏鹰=利空成长股。</p>
    </div>
  </div>

  <div class="bg-gradient-to-br from-pink-500/20 to-purple-500/10 border border-pink-500/30 rounded-xl p-4">
    <h4 class="text-white font-semibold mb-3 flex items-center gap-2"><span>⚔️</span> 催化五：国家电网战投国盛量子·央企加速布局前沿科技【B级】</h4>
    <div class="text-xs text-white/70 space-y-2 leading-relaxed">
      <p><b class="text-yellow-400">事件：</b>国盛量子完成数千万元战略融资，投资方为国家电网旗下创投基金，资金用于金刚石NV色心量子测量技术迭代、产能建设及工业场景落地。此外中石油、国家电投等能源央企也在加快布局可控核聚变、氢能等前沿未来产业。</p>
      <p><b class="text-yellow-400">影响：</b>能源央企加大对量子科技、核聚变、氢能等前沿技术的产业投入，体现顶层战略布局决心。量子传感在电力工业场景的商业化落地加速，A股量子科技板块有望迎来情绪催化。但行业尚处于产业化早期，技术和商业化不确定性大，更多是主题性机会。</p>
    </div>
  </div>

  <div class="bg-white/5 rounded-xl p-4">
    <h4 class="text-white font-semibold mb-3">📅 本周重要事件日历</h4>
    <div class="text-xs text-white/70 space-y-1">
      <p>• <b>8月17日（周一）</b> 美伊谅解备忘录到期；央行连续三日隔夜逆回购</p>
      <p>• <b>8月18日（周二）</b> 中国7月经济数据（工业增加值/社零/固投）；年内最贵新股频准激光上市</p>
      <p>• <b>8月19日（周三）</b> 70城房价数据；中国平安/中际旭创/紫金矿业中报</p>
      <p>• <b>8月20日（周四）</b> LPR报价；阿里巴巴/小米集团财报；世界机器人大会开幕前夕</p>
      <p>• <b>8月21日（周三）</b> 世界机器人大会开幕；美联储会议纪要（凌晨）</p>
      <p>• <b>本周</b> 476家公司已披露中报（近九成盈利），中报密集披露期</p>
    </div>
  </div>
</div>
'''
gen.add_section("核心题材与今日催化", catalyst_html, "🔥")

# 持仓诊断
portfolio_html = '''
<div class="space-y-4">
  <div class="grid md:grid-cols-2 gap-4">
    <!-- 英维克 -->
    <div class="bg-white/5 rounded-xl p-4 border border-blue-500/20">
      <div class="flex items-center justify-between mb-2">
        <h4 class="text-white font-semibold flex items-center gap-2"><span>❄️</span> 英维克 (002837)</h4>
        <div class="text-right">
          <div class="text-xl font-bold text-red-400">57.09</div>
          <div class="text-xs text-red-400">+2.96%</div>
        </div>
      </div>
      <div class="text-xs text-white/60 mb-2">总市值 728亿 | 换手率 3.5%+ | 成交额 约25亿</div>
      <div class="bg-green-500/10 border border-green-500/30 rounded-lg p-2 mb-2">
        <p class="text-green-300 text-xs font-semibold">⚡ 状态：超跌反弹·液冷景气验证·反弹力度尚可</p>
      </div>
      <div class="text-xs text-white/70 leading-relaxed space-y-1">
        <p><b>周五走势：</b>受台系液冷厂商Q2业绩暴增催化，英维克反弹2.96%收57.09元。奇鋐科技Q2净利+139%、双鸿+513%，7月营收双双创历史新高，验证液冷行业高景气。</p>
        <p><b>利好：</b>①台系液冷厂商业绩持续验证（奇鋐+139%、双鸿+513%），下半年英伟达Rubin+谷歌TPU出货有望提升液冷渗透率；②东方证券研报指出液冷产业链下半年需求增长趋势延续；③液冷从可选方案升级为AI服务器刚性标配。</p>
        <p><b>风险：</b>①股价从52元反弹至57元（+10%），但成交量未显著放大，反弹基础不牢；②上方60-63元套牢盘密集，反弹空间有限；③A股科技股整体仍在调整期，液冷难以独善其身。</p>
        <p><b class="text-yellow-400">操作建议：</b>反弹减仓策略不变。58-60元区间继续减仓，跌破52元清仓止损。周末存储/算力利好可能带来高开，但高开就是减仓机会，不要追涨。本周四大事件密集，控制仓位是第一要务。</p>
      </div>
    </div>

    <!-- 铜冠铜箔 -->
    <div class="bg-white/5 rounded-xl p-4 border border-orange-500/20">
      <div class="flex items-center justify-between mb-2">
        <h4 class="text-white font-semibold flex items-center gap-2"><span>🟠</span> 铜冠铜箔 (301217)</h4>
        <div class="text-right">
          <div class="text-xl font-bold text-red-400">123.05</div>
          <div class="text-xs text-red-400">+3.20%</div>
        </div>
      </div>
      <div class="text-xs text-white/60 mb-2">总市值 1020亿 | 换手率 5.25% | 成交额 52.69亿 | 午间临停</div>
      <div class="bg-yellow-500/10 border border-yellow-500/30 rounded-lg p-2 mb-2">
        <p class="text-yellow-300 text-xs font-semibold">⚠️ 注意：董秘兼财务负责人无法履职·周五午间临停·需关注消息面</p>
      </div>
      <div class="text-xs text-white/70 leading-relaxed space-y-1">
        <p><b>周五走势：</b>开盘119.47→最高124.09→午间临停前收123.05元，涨3.20%。公司公告董秘兼财务负责人王俊林因身体原因无法履职，选举慎志辉为职工代表董事。午后临停至收盘。</p>
        <p><b>利好：</b>①AI服务器带动高端铜箔需求，PCB铜箔供需紧张逻辑不变；②台系PCB厂商Q2业绩亮眼（欣兴Q2毛利率首破30%）；③市值破千亿后机构关注度提升。</p>
        <p><b>风险：</b>①董秘无法履职的具体原因不明，存在管理风险；②市盈率TTM高达621倍，估值严重透支；③股价处于高位震荡区间，125-126元是强阻力位；④连续多日冲高回落，高位见顶信号需警惕。</p>
        <p><b class="text-yellow-400">操作建议：</b>高位股+管理层变动=不确定性加大，坚决执行减仓纪律。120元以上继续减仓至1/3底仓。如果周一高开，利用反弹继续减；如果低开，看115元支撑，破位继续减。教训库第4条：连续冲高回落=顶部信号，不要抱有幻想。</p>
      </div>
    </div>

    <!-- 雅克科技 -->
    <div class="bg-white/5 rounded-xl p-4 border border-purple-500/20">
      <div class="flex items-center justify-between mb-2">
        <h4 class="text-white font-semibold flex items-center gap-2"><span>🔬</span> 雅克科技 (002409)</h4>
        <div class="text-right">
          <div class="text-xl font-bold text-red-400">151.22</div>
          <div class="text-xs text-red-400">+1.15%</div>
        </div>
      </div>
      <div class="text-xs text-white/60 mb-2">总市值 720亿 | 换手率 ~7% | 成交额 ~50亿</div>
      <div class="bg-yellow-500/10 border border-yellow-500/30 rounded-lg p-2 mb-2">
        <p class="text-yellow-300 text-xs font-semibold">⚡ 状态：大跌后超跌反弹·存储利好支撑·上方压力仍大</p>
      </div>
      <div class="text-xs text-white/70 leading-relaxed space-y-1">
        <p><b>周五走势：</b>雅克科技反弹1.15%收151.22元，受隔夜闪迪+13.67%和存储超级周期催化，但反弹幅度弱于预期（存储板块整体涨2-3%），说明上方抛压仍重。前一日放量大跌3.67%（换手率10.19%）后，周五缩量反弹，资金承接力度一般。</p>
        <p><b>利好：</b>①存储超级周期深化，摩根大通上调2028年市场至1.82万亿美元；②融资资金一周20亿加仓存储芯片（江波龙+12亿、兆易+8.77亿），杠杆资金持续布局；③SK海力士上半年设备投资+70%，前驱体材料需求确定性强；④四部门集成电路税收优惠政策利好。</p>
        <p><b>风险：</b>①周四大跌换手率10%+，筹码大规模交换后短期难快速走强；②从127元反弹至151元（+19%），反弹幅度已不小；③中报临近，业绩能否支撑70倍PE存疑；④上方155-160元套牢盘密集。</p>
        <p><b class="text-yellow-400">操作建议：</b>周末存储利好+集成电路税收优惠，今日可能高开。但<b class="text-red-400">高开就是减仓机会</b>，150-155元区间坚决减仓。教训库第6条：存储超级周期是真的，但A股股价已经提前反映了。等中报落地后再评估是否加仓。</p>
      </div>
    </div>

    <!-- *ST建艺 -->
    <div class="bg-white/5 rounded-xl p-4 border border-red-500/30">
      <div class="flex items-center justify-between mb-2">
        <h4 class="text-white font-semibold flex items-center gap-2"><span>⚠️</span> *ST建艺 (002789)</h4>
        <div class="text-right">
          <div class="text-xl font-bold text-green-400">10.15</div>
          <div class="text-xs text-green-400">-0.39%</div>
        </div>
      </div>
      <div class="bg-red-500/10 border border-red-500/30 rounded-lg p-3 mb-3">
        <p class="text-red-300 text-xs font-semibold">⚠️ 最高优先级：立即清仓止损，退市风险敞口必须关闭</p>
      </div>
      <div class="text-xs text-white/70 leading-relaxed">
        <p><b class="text-yellow-400">📰 最新动态</b>：退市风险股，周五微跌0.39%收10.15元。公司重组和摘帽申请进展不明，存在重大不确定性。</p>
        <p class="mt-2"><b class="text-yellow-400">⚡ 操作策略</b>：退市风险股，任何价格立即清仓。退市风险+债务问题未消除，不要抱有任何幻想。ST股的基本面不会因为股价反弹而改善，早一天减仓少一分风险。本周内必须完成清仓。</p>
      </div>
    </div>
  </div>

  <div class="bg-white/5 rounded-xl p-4">
    <h4 class="text-white font-semibold mb-3 flex items-center gap-2"><span>📋</span> 组合总览与今日策略</h4>
    <div class="text-xs text-white/70 space-y-2 leading-relaxed">
      <p><b class="text-yellow-400">周五表现</b>：持仓全线反弹，铜冠铜箔+3.20%领涨（临停前），英维克+2.96%，雅克科技+1.15%，*ST建艺-0.39%。组合整体跑赢大盘（沪指+0.01%），但缩量反弹说明上涨基础不牢。</p>
      <p><b class="text-yellow-400">今日策略（8月17日周一）：</b><br>
      ① 周末政策利好密集（集成电路税收优惠、跨境资金池、社融超预期）+美股科技分化，今日A股或有高开。但<b class="text-red-400">高开=减仓机会</b>，不是加仓理由。本周四大事件密集落地，不确定性大，控制仓位优先；<br>
      ② <b>雅克科技</b>：存储+集成电路双利好，预计高开，150-155元区间坚决减仓，逢高分批减，不要追涨；<br>
      ③ <b>铜冠铜箔</b>：董秘无法履职增加不确定性，高位股+管理风险=减仓理由，120元以上继续减仓至1/3底仓，周一关注复牌走势；<br>
      ④ <b>英维克</b>：液冷景气验证但个股反弹力度有限，58-60元区间减仓，跌破52元清仓；<br>
      ⑤ <b>*ST建艺</b>：立即清仓（最高优先级）；<br>
      ⑥ 整体仓位4成，防御为主。本周四大事件（经济数据、LPR、机器人大会、美联储纪要）落地前不加仓，等待信号明确。
      </p>
    </div>
  </div>
</div>
'''
gen.add_section("持仓诊断与操作建议", portfolio_html, "💼")

# 空方视角
bear_html = '''
<div class="space-y-4">
  <div class="bg-red-500/10 border border-red-500/30 rounded-xl p-4">
    <h4 class="text-red-300 font-semibold mb-3 flex items-center gap-2"><span>🐻</span> 空方观点：缩量反弹=熊市中继·本周四件大事=四大雷区·中报暴雷潮临近</h4>
    <div class="text-xs text-white/70 space-y-3 leading-relaxed">
      <div class="bg-white/5 rounded-lg p-3">
        <p class="text-red-300 font-semibold mb-1">风险1：缩量反弹=没有增量资金，熊市中继不是底部</p>
        <p>周四大跌2.55万亿放量、周五反弹2.25万亿缩量——这是典型的"放量跌、缩量涨"熊市特征。放量下跌说明主力出逃，缩量反弹说明场外资金不买账、没人接盘。没有增量资金的反弹都是耍流氓，反弹完了还要继续跌。沪指3900点不是底，下方3800、3700都有可能。</p>
      </div>
      <div class="bg-white/5 rounded-lg p-3">
        <p class="text-red-300 font-semibold mb-1">风险2：本周四大事件=四大雷区，哪个都能引爆下跌</p>
        <p>本周四大事件密集：7月经济数据（可能不及预期）、LPR（可能不降或降幅不及预期）、机器人大会（利好出尽）、美联储纪要（可能偏鹰）。四个事件任何一个不及预期都可能引发调整。更可怕的是，如果两个以上同时不及预期，就是双击。在不确定性如此大的一周里，仓位应该越轻越好。</p>
      </div>
      <div class="bg-white/5 rounded-lg p-3">
        <p class="text-red-300 font-semibold mb-1">风险3：中报密集披露期，业绩暴雷才刚开始</p>
        <p>截至8月16日，才476家公司披露半年报，只占全部A股的不到10%。接下来两周是中报披露最高峰，很多高位科技股业绩根本跟不上股价。铜冠铜箔621倍PE、雅克科技70倍PE、英维克146倍PE——这些估值都是建立在"AI永远增长"的假设上，一旦中报低于预期就是戴维斯双杀。工业富联"利好出尽"的教训还在眼前。</p>
      </div>
      <div class="bg-white/5 rounded-lg p-3">
        <p class="text-red-300 font-semibold mb-1">风险4：消费级存储价格倒挂，存储超级周期存隐忧</p>
        <p>财联社报道，eMMC现货渠道价格已跌破原厂合约价出现倒挂，主要出现在低容量消费级存储上。虽然主流DRAM/NAND合约价仍在上扬，但消费级与高端存储的走势分化说明需求并不是全面爆发。如果AI需求增速放缓，存储行业的"超级周期"可能比想象中短。A股存储概念股估值已经price in了最乐观的情景。</p>
      </div>
      <div class="bg-white/5 rounded-lg p-3">
        <p class="text-red-300 font-semibold mb-1">风险5：美伊谅解备忘录到期，地缘黑天鹅风险升温</p>
        <p>美伊谅解备忘录8月17日（今天）到期，目前几乎没有达成最终协议的迹象。如果谈判破裂、霍尔木兹海峡局势升级，油价飙升→通胀回升→美联储推迟降息→全球科技股杀估值，这条传导链非常清晰。当前市场对地缘风险定价严重不足，一旦出事就是黑天鹅。</p>
      </div>
    </div>
  </div>

  <div class="bg-green-500/10 border border-green-500/30 rounded-xl p-4">
    <h4 class="text-green-300 font-semibold mb-3 flex items-center gap-2"><span>🐂</span> 多方反驳：政策底+业绩底+估值底三底共振·调整后空间更大</h4>
    <div class="text-xs text-white/70 space-y-2 leading-relaxed">
      <p>① <b>政策底明确，流动性充裕</b>：央行8月合计净投放2000亿买断式逆回购+每日6000亿隔夜逆回购，流动性非常充裕。二季度货币政策执行报告明确"加大逆周期调节力度"。7月社融22.25万亿超预期，企业债券+政府债双发力，直接融资占比提升。政策底信号非常清晰。</p>
      <p>② <b>存储超级周期才走了一半</b>：摩根大通上调2028年存储市场至1.82万亿美元，供需短缺未来两年持续。融资资金一周20亿加仓存储芯片，说明机构资金在持续布局，不是散户在炒。A股存储材料公司的业绩爆发期还在后面（Q3-Q4才是旺季），当前估值不算贵。</p>
      <p>③ <b>AI算力需求持续超预期</b>：AMD+6.5%创历史新高，47.5亿发债扩产AI数据中心，Helios机架Q4出货。英伟达8月26日财报预计Q2营收920亿、Q3超1030亿。AI资本开支不是泡沫，是真实的业绩增长。A股算力产业链（液冷、PCB、光模块）有基本面支撑。</p>
      <p>④ <b>科技股调整已充分，估值逐步合理</b>：经过7月下旬以来的调整，科技股普遍回调15-25%，估值泡沫得到一定程度消化。雅克科技从246元跌到127元（-48%），铜冠铜箔从高点回调20%+。调整后优质标的布局性价比提升。</p>
      <p>⑤ <b>政策利好持续释放</b>：集成电路税收优惠、跨境资金池全国推广、机器人大会、世界机器人大会……产业政策密集出台，硬科技是国家战略方向，政策支持只会加强不会减弱。</p>
    </div>
  </div>

  <div class="bg-yellow-500/10 border border-yellow-500/30 rounded-xl p-4">
    <h4 class="text-yellow-300 font-semibold mb-2 flex items-center gap-2"><span>⚖️</span> 综合判断</h4>
    <p class="text-xs text-white/70 leading-relaxed">
      短期（本周）：A股处于"放量下跌后的缩量修复期"，周末政策利好提供支撑，但本周四大事件（经济数据、LPR、机器人大会、美联储纪要）密集落地，不确定性大。建议控制仓位4成，观望为主，等待事件落地后再加仓。<br>
      中期（1-3个月）：存储超级周期+AI算力需求爆发+国产替代加速+政策支持，四大逻辑支撑科技成长股中期向好。但当前估值仍偏高，需要中报业绩验证，调整后优质标的将迎来更好的布局机会。<br>
      <b class="text-yellow-400">核心结论：短期谨慎，本周控制仓位4成防御为主。
      利用反弹继续减仓高位科技股，等待中报披露和四大事件落地后的布局机会。
      关注三个方向：存储芯片材料/设备（中期逻辑最硬）、液冷（业绩最确定）、工业母机/高端制造（政策催化）。</b>
    </p>
  </div>
</div>
'''
gen.add_section("空方视角与多空博弈", bear_html, "⚖️")

# 预判验证
prediction_html = '''
<div class="space-y-4">
  <div class="bg-white/5 rounded-xl p-4">
    <h4 class="text-white font-semibold mb-3 flex items-center gap-2"><span>🔮</span> 预判记录（T+N验证）</h4>
    <div class="space-y-3 text-xs">
      <div class="bg-yellow-500/10 border border-yellow-500/30 rounded-lg p-3">
        <div class="flex justify-between mb-2">
          <span class="text-yellow-300 font-semibold">预判#20260814-01：闪迪投资者日催化存储板块二次反弹</span>
          <span class="text-xs bg-yellow-500/30 text-yellow-200 px-2 py-0.5 rounded">验证中·T+1</span>
        </div>
        <p class="text-white/70">预判内容：闪迪投资者日公布NAND 5000亿市场+80%毛利率超级指引，股价+13.67%，将催化A股存储板块情绪修复。存储材料/设备方向有望迎来3-5%的高开反弹，但持续性取决于成交量和内资承接力度。</p>
        <p class="text-white/50 mt-1">当前进度：T+1验证（上周五首日），雅克科技+1.15%、铜冠铜箔+3.20%（临停前）、华海诚科+3.51%。整体反弹幅度1-3.5%，基本符合"高开反弹"预期，但反弹力度分化且缩量，持续性待观察。T+2（本周一）是验证持续性的关键。</p>
      </div>
      <div class="bg-yellow-500/10 border border-yellow-500/30 rounded-lg p-3">
        <div class="flex justify-between mb-2">
          <span class="text-yellow-300 font-semibold">预判#20260814-02：A股短期调整延续至下周三</span>
          <span class="text-xs bg-yellow-500/30 text-yellow-200 px-2 py-0.5 rounded">验证中·T+1</span>
        </div>
        <p class="text-white/70">预判内容：A股放量下跌后短期调整需要3-5个交易日消化，沪指在3850-3950区间震荡，科技高位股继续回调，防御板块相对抗跌。下周三前后可能出现新一轮布局机会。</p>
        <p class="text-white/50 mt-1">当前进度：T+1验证（上周五首日），沪指+0.01%收3927点，处于3850-3950区间内。创业板+1.12%超跌反弹，但缩量上涨持续性存疑。整体调整格局未变，继续观察T+3（本周三）前后是否出现布局机会。</p>
      </div>
      <div class="bg-red-500/10 border border-red-500/30 rounded-lg p-3">
        <div class="flex justify-between mb-2">
          <span class="text-red-300 font-semibold">预判#20260812-01：算力期货催化算力产业链</span>
          <span class="text-xs bg-red-500/30 text-red-200 px-2 py-0.5 rounded">验证失败·T+3</span>
        </div>
        <p class="text-white/70">预判内容：CME推出算力期货（H100/B200）是里程碑事件，将催化算力产业链情绪修复，GPU/服务器/液冷/光模块方向有望迎来2-3%的反弹，持续1-2个交易日。</p>
        <p class="text-white/50 mt-1">验证结果：失败。T+3验证，算力期货题材未能形成持续反弹，A股科技股冲高回落后大面积下跌。"新物种"题材发酵需要时间，短期催化效应有限，且被市场整体调整对冲。</p>
      </div>
      <div class="bg-red-500/10 border border-red-500/30 rounded-lg p-3">
        <div class="flex justify-between mb-2">
          <span class="text-red-300 font-semibold">预判#20260812-02：SK海力士扩产催化存储材料</span>
          <span class="text-xs bg-red-500/30 text-red-200 px-2 py-0.5 rounded">验证失败·T+3</span>
        </div>
        <p class="text-white/70">预判内容：SK海力士大连NAND扩产50%，将催化半导体材料板块情绪，雅克科技、华海诚科等存储材料标的有望持续走强，中期（1-2周）涨幅5-10%。</p>
        <p class="text-white/50 mt-1">验证结果：失败。T+3验证，雅克科技冲高回落后大跌3.67%（周四大跌），周五小幅反弹1.15%。短期催化效应不及预期，反而因为"利好出尽"+市场整体调整导致资金出逃。中期（1-2周）仍有待观察，但短期预判失败。</p>
      </div>
      <div class="bg-green-500/10 border border-green-500/30 rounded-lg p-3">
        <div class="flex justify-between mb-2">
          <span class="text-green-300 font-semibold">预判#20260803-01：雅克科技跌停后3日内反弹</span>
          <span class="text-xs bg-green-500/30 text-green-200 px-2 py-0.5 rounded">已验证·正确</span>
        </div>
        <p class="text-white/70">预判内容：雅克科技跌停板机构抄底近5亿，预计3个交易日内出现5-10%反弹。</p>
        <p class="text-white/50 mt-1">实际走势：从8月4日跌停价127元反弹至最高158.6元（+25%），远超预期。验证正确，但反弹后回落速度也快，高点已过。</p>
      </div>
      <div class="bg-green-500/10 border border-green-500/30 rounded-lg p-3">
        <div class="flex justify-between mb-2">
          <span class="text-green-300 font-semibold">预判#20260730-02：存储板块调整期2-3周</span>
          <span class="text-xs bg-green-500/30 text-green-200 px-2 py-0.5 rounded">已验证·正确</span>
        </div>
        <p class="text-white/70">预判内容：7月30日科技股大跌后，存储板块进入2-3周调整期，调整幅度约15-25%。</p>
        <p class="text-white/50 mt-1">当前进度：第12个交易日，板块从高点回调约20%后出现超跌反弹但持续性不足。时间和幅度均验证正确，目前仍在调整周期内。第3周（本周）是观察调整是否结束的关键窗口。</p>
      </div>
      <div class="bg-red-500/10 border border-red-500/30 rounded-lg p-3">
        <div class="flex justify-between mb-2">
          <span class="text-red-300 font-semibold">新增预判#20260817-01：本周四大事件落地后科技股迎来布局窗口</span>
          <span class="text-xs bg-red-500/30 text-red-200 px-2 py-0.5 rounded">待验证·T+5</span>
        </div>
        <p class="text-white/70">预判内容：本周（8/17-8/21）四大事件（经济数据、LPR、机器人大会、美联储纪要）密集落地后，市场不确定性消除，叠加中报披露进入后半段，科技股有望迎来新一轮布局窗口。存储芯片材料/设备、液冷算力、先进封装三个方向有望率先反弹，涨幅5-10%。</p>
        <p class="text-white/50 mt-1">验证时间：8月22日（T+5，下周六）验证反弹是否出现及幅度</p>
      </div>
      <div class="bg-red-500/10 border border-red-500/30 rounded-lg p-3">
        <div class="flex justify-between mb-2">
          <span class="text-red-300 font-semibold">新增预判#20260817-02：铜冠铜箔短期见顶，调整幅度15-20%</span>
          <span class="text-xs bg-red-500/30 text-red-200 px-2 py-0.5 rounded">待验证·T+5</span>
        </div>
        <p class="text-white/70">预判内容：铜冠铜箔621倍PE严重透支，董秘无法履职增加管理风险，连续多日冲高回落+高位放量滞涨是明确见顶信号。短期内股价将调整15-20%，目标价位100-105元。</p>
        <p class="text-white/50 mt-1">验证时间：8月22日（T+5，下周六）验证调整幅度</p>
      </div>
    </div>
  </div>

  <div class="bg-white/5 rounded-xl p-4">
    <h4 class="text-white font-semibold mb-2 flex items-center gap-2"><span>📊</span> 准确率统计</h4>
    <div class="grid grid-cols-3 gap-3 text-center text-xs">
      <div class="bg-white/5 rounded-lg p-2">
        <div class="text-lg font-bold text-yellow-400">64%</div>
        <div class="text-white/60">总体准确率</div>
      </div>
      <div class="bg-white/5 rounded-lg p-2">
        <div class="text-lg font-bold text-green-400">14/22</div>
        <div class="text-white/60">已验证正确/总数</div>
      </div>
      <div class="bg-white/5 rounded-lg p-2">
        <div class="text-lg font-bold text-blue-400">5</div>
        <div class="text-white/60">待验证</div>
      </div>
    </div>
  </div>
</div>
'''
gen.add_section("预判验证闭环", prediction_html, "🔮")

# 教训库
lesson_html = '''
<div class="space-y-3">
  <div class="bg-red-500/10 border border-red-500/30 rounded-lg p-3">
    <p class="text-red-300 font-semibold mb-1">教训#1：放量大跌=真出逃，不是"洗盘"，立即减仓</p>
    <p class="text-white/60 text-xs">
      8月13日A股放量下跌（2.55万亿成交+452亿主力净流出+4300股下跌），这不是"洗盘"，是真金白银的出逃。
      很多人喜欢给自己找借口——"这是洗盘、是下蹲是为了跳更高"，结果越套越深。
      <b>正确做法</b>：放量下跌当天就应该减仓，不要等"明天反弹"。放量下跌=市场用脚投票，
      说明大资金在撤离，散户不要逆势接盘。减仓后等缩量企稳再接回来，比死扛更主动。
      记住：缩量下跌还有救，放量下跌必须跑。
    </p>
  </div>

  <div class="bg-orange-500/10 border border-orange-500/30 rounded-lg p-3">
    <p class="text-orange-300 font-semibold mb-1">教训#2：隔夜美股涨≠A股涨，A股有自己的节奏</p>
    <p class="text-white/60 text-xs">
      隔夜美股涨了、存储股暴涨，很多人就兴奋了，以为A股今天一定大涨。
      但最近多次出现"美股涨、A股高开低走"的情况。
      8月12日工业富联中报+96%，股价反而跌4.58%；8月13日雅克科技高开低走跌3.67%。
      <b>正确做法</b>：隔夜美股上涨只能作为情绪参考，不能作为加仓依据。
      美股的逻辑是"业绩验证→继续涨"，A股的逻辑是"利好出尽→赶紧跑"，两个市场的投资文化完全不同。
      看到美股涨了，第一反应不应该是"今天要加仓"，而是"今天高开能不能减仓"。
    </p>
  </div>

  <div class="bg-yellow-500/10 border border-yellow-500/30 rounded-lg p-3">
    <p class="text-yellow-300 font-semibold mb-1">教训#3：换手率10%+的高位股=筹码大交换，立即警惕</p>
    <p class="text-white/60 text-xs">
      雅克科技周四换手率10.19%、成交额50亿、放量大跌，这三个数据加在一起就是明确的见顶信号。
      换手率超过10%意味着一天之内有十分之一的流通股被倒手了一遍，
      说明筹码在高位大规模交换——老资金在出货，新资金在接盘。
      <b>正确做法</b>：高位股换手率突然放大到10%以上，不管是涨是跌，都要减仓。
      放量上涨也要警惕（可能是对倒出货），放量下跌更要跑（直接就是出逃）。
      换手率从低到高的过程，就是风险从低到高的过程。
    </p>
  </div>

  <div class="bg-green-500/10 border border-green-500/30 rounded-lg p-3">
    <p class="text-green-300 font-semibold mb-1">教训#4：连续冲高回落=顶部信号，不要抱有幻想</p>
    <p class="text-white/60 text-xs">
      铜冠铜箔连续多日冲高回落，雅克科技也是高开低走放量大跌。
      连续冲高回落不是巧合，是主力在"边拉边出"。
      <b>正确做法</b>：连续两天以上冲高回落，第三天开盘就应该减仓，
      不要等到"再涨一点就卖"——往往等不到再涨，就直接下去了。
      冲高回落的本质是：上方有大量抛压，每一次上涨都有人在卖。
      连续出现说明卖方力量远大于买方，短期见顶概率极大。
    </p>
  </div>

  <div class="bg-blue-500/10 border border-blue-500/30 rounded-lg p-3">
    <p class="text-blue-300 font-semibold mb-1">教训#5：事件密集周=风险周，控制仓位优先</p>
    <p class="text-white/60 text-xs">
      本周有四大重磅事件（经济数据、LPR、机器人大会、美联储纪要），
      很多人以为事件多=机会多，其实事件多=不确定性多=风险多。
      四个事件里只要有一个不及预期，就会引发调整；如果两个以上同时不及预期，就是双击。
      <b>正确做法</b>：重大事件密集落地前，应该降低仓位、观望为主，
      而不是赌某个事件会超预期。等事件落地、不确定性消除后再加仓，
      虽然少赚了"预期差"的钱，但避免了"踩雷"的风险。
      在股市里，活着比赚快钱更重要。
    </p>
  </div>

  <div class="bg-purple-500/10 border border-purple-500/30 rounded-lg p-3">
    <p class="text-purple-300 font-semibold mb-1">教训#6：存储超级周期是真的，但A股股价已经提前反映了</p>
    <p class="text-white/60 text-xs">
      闪迪投资者日公布的数据很炸裂——NAND市场2027年5000亿、毛利率80%、FCF利润率50%。
      存储超级周期的逻辑完全成立。但问题是：A股的存储概念股已经涨了多少了？
      雅克科技从低点55元涨到最高246元（+347%），铜冠铜箔从30元涨到130元（+333%）。
      这些涨幅是不是已经把"超级周期"提前price in了？
      <b>正确做法</b>：行业逻辑再好，也要看股价位置。
      股价在低位+行业逻辑好=买入机会；股价在高位+行业逻辑好=利好出尽。
      不要因为"行业空间大"就追高，A股永远是炒预期，等逻辑所有人都看懂了，就是出货的时候。
    </p>
  </div>

  <div class="bg-pink-500/10 border border-pink-500/30 rounded-lg p-3">
    <p class="text-pink-300 font-semibold mb-1">教训#7：管理层异动=危险信号，不管什么原因都要减仓</p>
    <p class="text-white/60 text-xs">
      铜冠铜箔董秘兼财务负责人因身体原因无法履职，这种消息不管原因是什么，都是负面信号。
      财务负责人是公司最核心的岗位之一，突然"无法履职"往往意味着有更深层的问题。
      是真的身体原因？还是被调查？还是业绩有假？散户永远是最后知道的。
      <b>正确做法</b>：高位股出现管理层异动（尤其是财务负责人、董秘），
      第一反应就是减仓，不要等"真相大白"。等真相大白的时候，股价已经跌完了。
      宁可错杀，不可放过——因为错杀的损失可以追回，踩雷的损失可能是毁灭性的。
    </p>
  </div>
</div>
'''
gen.add_section("教训库引用", lesson_html, "📚")

# 生成+发布
output_path = os.path.join(WORK_DIR, 'docs/daily/20260817_每日新闻洞察.html')
result = gen.publish(output_path=output_path)
print("发布结果:", result)
print("成功:", result.get('success', False))
print("报告路径:", output_path)
file_size = os.path.getsize(output_path)
print("文件大小:", file_size, "字节 (%.1f KB)" % (file_size / 1024))

# 更新 latest.html
latest_path = os.path.join(WORK_DIR, 'docs/daily/latest.html')
shutil.copy2(output_path, latest_path)
print("latest.html 已更新")
