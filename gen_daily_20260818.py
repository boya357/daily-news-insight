#!/usr/bin/env python3
"""2026年8月18日 每日新闻洞察生成 - 周二·费半+1.64%逆势暴涨·美光破千+4.13%·应用材料+5.55%·长鑫科技市值破4.13万亿·宇树科技明日上市·特朗普不延长伊核协议"""
import sys, os, shutil, json
WORK_DIR = '/root/daily-news-insight'
sys.path.insert(0, os.path.join(WORK_DIR, 'v3'))
from generators.daily_pro import DailyReportProGenerator

gen = DailyReportProGenerator(
    date_str='2026年8月18日', weekday='星期二',
    subtitle='2026年8月18日 周二 · 费半+1.64%逆势暴涨·美光破千+4.13%·应用材料+5.55%·长鑫市值破4.13万亿·宇树明日上市·伊核协议到期',
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
        '美股三大指数收跌但芯片股逆势暴涨：道指-0.51%、标普-0.52%、纳指-0.32%；费城半导体+1.64%一枝独秀；美光+4.13%重回1000美元、应用材料+5.55%领涨设备股、闪迪+8.88%市值破2600亿；微软-3.04%蒸发1120亿市值',
        '存储超级周期再度爆发：马斯克警告AI存储芯片短缺将成瓶颈，特朗普政府施压美国企业不用中国存储芯片，双重催化下存储股集体暴涨；美光BofA目标价上调至1550美元，HBM产能已排满至2027年',
        'A股昨日放量普涨：沪指+1.41%收3982点，深成指+2.44%，创业板+3.14%，科创50+4.14%，两市成交2.39万亿放量2446亿；长鑫科技+12%市值破4.13万亿登顶A股，相当于2.5个茅台',
        '持仓全线大涨：铜冠铜箔+7.45%（董秘逝世消息下反而大涨）、雅克科技+5.15%、英维克+2.80%、*ST建艺+0.69%；存储/半导体板块全线爆发，电子化学品+5.13%领涨全市场',
        '今日三大焦点：①宇树科技明日科创板上市（人形机器人第一股，发行价150.8元，市值610亿）；②美伊谅解备忘录到期，特朗普明确不延长，地缘风险升温；③7月经济数据+LPR报价本周落地'
    ],
    operation_advice='周二开盘：隔夜存储/设备股暴涨+昨日A股放量反弹，今日科技板块大概率高开。但沪指逼近4000点关口压力大，且科技拥挤度已达历史99%分位，不建议追高。持仓策略：利用高开继续减仓高位股（铜冠铜箔667倍PE严重透支），液冷（英维克）和存储材料（雅克）底仓持有，仓位控制在4-5成。关注宇树科技上市对机器人板块的催化效应',
    risk_level='偏高',
    suggested_position='4-5成'
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
    description='每日新闻洞察 2026年8月18日：费半+1.64%逆势暴涨、美光破千+4.13%、应用材料+5.55%、长鑫市值破4.13万亿、宇树科技明日上市、伊核协议到期',
)

gen.add_global_market()

global_cards1 = render_cards([
    {"name":"道琼斯","change":"-0.51%","up":False},
    {"name":"标普500","change":"-0.52%","up":False},
    {"name":"纳斯达克","change":"-0.32%","up":False},
    {"name":"费城半导体","change":"+1.64%","up":True},
    {"name":"日经225","change":"-0.90%","up":False},
    {"name":"恒生指数","change":"+1.34%","up":True},
])
global_list1 = render_list([
    {"name":"WTI原油","change":"+0.44%/$84.11","up":True},
    {"name":"布伦特原油","change":"+0.27%/$91.11","up":True},
    {"name":"COMEX黄金","change":"+0.20%/$4482.85","up":True},
    {"name":"COMEX白银","change":"+0.12%/$66.31","up":True},
])
global_list2 = render_list([
    {"name":"三星电子","change":"+2.43%","up":True},
    {"name":"SK海力士","change":"+3.26%","up":True},
    {"name":"美光科技","change":"+4.13%","up":True},
    {"name":"台积电ADR","change":"+1.08%","up":True},
])
global_list3 = render_list([
    {"name":"英伟达","change":"-0.07%/$225.01","up":False},
    {"name":"AMD","change":"-1.63%/$506.00","up":False},
    {"name":"微软","change":"-3.04%/$480.35","up":False},
    {"name":"苹果","change":"-0.11%/$305.59","up":False},
    {"name":"博通","change":"-0.14%/$392.43","up":False},
    {"name":"英特尔","change":"+0.97%/$103.49","up":True},
    {"name":"应用材料","change":"+5.55%/$535.31","up":True},
    {"name":"阿斯麦","change":"+2.12%/$1883.12","up":True},
])

global_html = '''
<div class="grid md:grid-cols-3 gap-4">
  <div class="md:col-span-2">
    <div class="text-white font-semibold mb-3 flex items-center gap-2"><span>🌍</span><span>隔夜全球市场 · 指数跌芯片涨·AI硬件继续狂飙·软件股遭抛售</span></div>
    <div class="grid grid-cols-3 md:grid-cols-6 gap-2">{0}</div>
    <p class="text-xs text-white/50 mt-3 leading-relaxed">
      ⚡ <b class="text-yellow-400">核心要点：美股三大指数集体收跌，但费城半导体+1.64%逆势暴涨，与大盘形成鲜明对比；存储芯片集体爆发（美光+4.13%重回1000美元、闪迪+8.88%、西部数据+5.35%），半导体设备股走强（应用材料+5.55%、阿斯麦+2.12%）；微软-3.04%单日蒸发1120亿美元市值，AI软件端遭抛售</b>——<br>
      ①<b>存储芯片超级行情再起</b>：三大催化剂共振——<br>
      &nbsp;&nbsp;·马斯克警告AI存储芯片短缺将成行业瓶颈，xAI/SpaceX等大买家需求暴增<br>
      &nbsp;&nbsp;·特朗普政府施压美国企业不用中国存储芯片，美光/SK海力士等受益<br>
      &nbsp;&nbsp;·BofA上调美光FY30 EPS至200-250美元、目标价1550美元<br>
      &nbsp;&nbsp;美光重回1000美元关口，HBM产能已排满至2027年，Server DRAM结构性短缺持续。闪迪+8.88%市值突破2600亿美元。<br>
      ②<b>半导体设备股走强</b>：应用材料+5.55%领涨，UBS/JPMorgan相继上调目标价，Q3营收91亿美元创纪录+25%YoY，Non-GAAP毛利率50.4%连续13季扩张。客户给8季度滚动预测，2027年增长确定性高。阿斯麦+2.12%。<br>
      ③<b>微软暴跌-3.04%，AI软件端遭质疑</b>：单日蒸发约1118亿美元市值，相当于微软一整年资本开支的96.4%。资金从AI应用端（软件/平台）向AI硬件端（芯片/存储/设备）搬家的趋势非常清晰。Meta也跌超3%。<br>
      ④<b>英伟达微跌-0.07%</b>：盘整于225美元附近，等待8月26日Q2财报。市场预期Q2营收约920亿美元、Q3指引超1030亿。AMD-1.63%（上周大涨后获利回吐）。<br>
      ⑤<b>大宗商品微涨</b>：WTI原油+0.44%收84.11美元，布伦特+0.27%收91.11美元。美伊谅解备忘录到期，特朗普明确不延长，地缘风险升温支撑油价。COMEX黄金+0.20%收4482美元。<br>
      ⑥<b>亚太市场分化</b>：日经225-0.90%，恒生指数+1.34%。韩股存储双雄大涨，三星+2.43%、SK海力士+3.26%、三星SDI+5.95%。
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
    <div class="text-xl font-bold text-red-400">3982.65</div>
    <div class="text-xs text-red-400">+1.41%</div>
  </div>
  <div class="bg-gradient-to-br from-red-500/20 to-orange-500/10 border border-red-500/30 rounded-xl p-3 text-center">
    <div class="text-xs text-white/60 mb-1">深证成指</div>
    <div class="text-xl font-bold text-red-400">14704.27</div>
    <div class="text-xs text-red-400">+2.44%</div>
  </div>
  <div class="bg-gradient-to-br from-red-500/20 to-orange-500/10 border border-red-500/30 rounded-xl p-3 text-center">
    <div class="text-xs text-white/60 mb-1">创业板指</div>
    <div class="text-xl font-bold text-red-400">3740.16</div>
    <div class="text-xs text-red-400">+3.14%</div>
  </div>
  <div class="bg-gradient-to-br from-red-500/20 to-orange-500/10 border border-red-500/30 rounded-xl p-3 text-center">
    <div class="text-xs text-white/60 mb-1">科创50</div>
    <div class="text-xl font-bold text-red-400">1788.85</div>
    <div class="text-xs text-red-400">+4.14%</div>
  </div>
</div>

<div class="grid md:grid-cols-2 gap-4">
  <div class="bg-white/5 rounded-xl p-4">
    <h4 class="text-white font-semibold mb-3 flex items-center gap-2"><span>📈</span> 领涨板块</h4>
    <div class="space-y-1 text-xs">
      <div class="flex justify-between"><span class="text-white/70">电子化学品</span><span class="text-red-400 font-semibold">+5.13%</span></div>
      <div class="flex justify-between"><span class="text-white/70">半导体</span><span class="text-red-400 font-semibold">+4.90%</span></div>
      <div class="flex justify-between"><span class="text-white/70">元件/PCB</span><span class="text-red-400 font-semibold">+3.93%</span></div>
      <div class="flex justify-between"><span class="text-white/70">贵金属</span><span class="text-red-400 font-semibold">+3.33%</span></div>
      <div class="flex justify-between"><span class="text-white/70">光学光电子</span><span class="text-red-400 font-semibold">+3.20%</span></div>
      <div class="flex justify-between"><span class="text-white/70">通信设备</span><span class="text-red-400 font-semibold">+3.05%</span></div>
    </div>
  </div>
  <div class="bg-white/5 rounded-xl p-4">
    <h4 class="text-white font-semibold mb-3 flex items-center gap-2"><span>📉</span> 领跌/弱势板块</h4>
    <div class="space-y-1 text-xs">
      <div class="flex justify-between"><span class="text-white/70">白酒/食品饮料</span><span class="text-green-400 font-semibold">-1.50%</span></div>
      <div class="flex justify-between"><span class="text-white/70">游戏/传媒</span><span class="text-green-400 font-semibold">-1.20%</span></div>
      <div class="flex justify-between"><span class="text-white/70">房地产</span><span class="text-green-400 font-semibold">-0.80%</span></div>
      <div class="flex justify-between"><span class="text-white/70">银行</span><span class="text-green-400 font-semibold">-0.50%</span></div>
      <div class="flex justify-between"><span class="text-white/70">煤炭/钢铁</span><span class="text-red-400 font-semibold">+0.30%</span></div>
      <div class="flex justify-between"><span class="text-white/70">医药</span><span class="text-red-400 font-semibold">+1.20%</span></div>
    </div>
  </div>
</div>

<div class="bg-white/5 rounded-xl p-4">
  <h4 class="text-white font-semibold mb-3 flex items-center gap-2"><span>📊</span> 市场概况与解读</h4>
  <div class="text-xs text-white/70 space-y-2 leading-relaxed">
    <p><b class="text-white">成交额2.39万亿</b>：较上周五放量约2446亿元，沪市1.11万亿、深市1.27万亿，连续两日维持2万亿级别天量。全市场超4100只个股上涨，赚钱效应回暖。</p>
    <p><b class="text-yellow-400">长鑫科技+12%市值破4.13万亿</b>：A股历史时刻——国产存储龙头长鑫科技（688825）高开高走收涨12%，报61.8元，市值4.13万亿元登顶A股，约等于2.5个茅台（茅台市值1.62万亿）。上市仅21天，从发行价8.66元涨至61.8元（+614%），全天成交335亿，换手率12.57%。</p>
    <p><b class="text-white">结构特征</b>：科技成长主导行情，半导体/算力/通信设备成为主线，电子化学品和半导体板块涨幅超5%。白酒、银行等传统权重拖累指数，茅台跌3.64%失守1300元。资金明显从传统消费向硬科技搬家。</p>
    <p><b class="text-orange-400">技术面</b>：沪指逼近4000点整数关口，短期存在震荡压力。60分钟级别有顶背离迹象，日线KDJ高位钝化。放量上涨但分化加剧，高位科技股不少冲高回落。</p>
    <p><b class="text-blue-400">数据面</b>：1-7月规模以上工业增加值同比增长4.5%，高技术制造业增长16.9%（传感器+35.3%、存储芯片+30.2%、电子元件+23.4%），新动能增长强劲，为科技股提供基本面支撑。</p>
  </div>
</div>

<div class="grid md:grid-cols-2 gap-4">
  <div class="bg-yellow-500/10 border border-yellow-500/30 rounded-xl p-4">
    <h4 class="text-yellow-300 font-semibold mb-2 flex items-center gap-2"><span>☀️</span> 今日展望</h4>
    <div class="text-xs text-white/70 space-y-1.5 leading-relaxed">
      <p>· 隔夜费半+1.64%+存储股暴涨，今日半导体/存储板块高开</p>
      <p>· 沪指逼近4000点关口，上方压力较大，谨防冲高回落</p>
      <p>· 宇树科技明日上市，机器人板块今日或提前炒作</p>
      <p>· 美伊协议到期地缘风险升温，军工/黄金或有表现</p>
      <p>· 科技拥挤度已达历史99%分位，追高风险大</p>
    </div>
  </div>
  <div class="bg-red-500/10 border border-red-500/30 rounded-xl p-4">
    <h4 class="text-red-300 font-semibold mb-2 flex items-center gap-2"><span>⚠️</span> 今日风险点</h4>
    <div class="text-xs text-white/70 space-y-1.5 leading-relaxed">
      <p>· 4000点关口压力+科技股拥挤，高开低走概率大</p>
      <p>· 铜冠铜箔董秘逝世+667倍PE，高位风险极大</p>
      <p>· 美伊谈判破裂可能触发油价飙升→科技股杀估值</p>
      <p>· 中报密集披露期，业绩暴雷风险（尤其高位科技股）</p>
      <p>· LPR报价本周落地，不及预期可能引发调整</p>
    </div>
  </div>
</div>
</div>
'''
gen.add_section("A股昨日复盘与今日展望", ashare_html, "📊")

# 核心题材
topic_html = '''
<div class="space-y-4">

<div class="bg-white/5 rounded-xl p-4">
  <h4 class="text-white font-semibold mb-3 flex items-center gap-2">
    <span class="text-red-400">S级</span>
    <span>🔥 存储芯片/HBM — 超级周期再度确认，双催化暴涨</span>
  </h4>
  <div class="space-y-3 text-xs text-white/70 leading-relaxed">
    <div class="bg-red-500/10 border border-red-500/20 rounded-lg p-3">
      <p class="text-red-300 font-semibold mb-1">🎯 核心催化剂（三重共振）</p>
      <p>① <b>马斯克警告存储短缺</b>：Tesla/SpaceX CEO表示AI存储芯片将成下一个瓶颈，大买家需求远超供给，市场解读为供需紧张信号</p>
      <p>② <b>美国施压不用中国存储</b>：商务部长Lutnick称特朗普政府劝阻美国企业使用中国存储芯片，已向苹果施压，美光/SK海力士直接受益</p>
      <p>③ <b>机构集体上调目标价</b>：BofA将美光FY30 EPS上调至200-250美元、目标价1550美元；New Street目标价1250美元，远期市值2-3万亿美元</p>
    </div>
    <div>
      <p class="text-white font-semibold mb-1">📈 隔夜表现</p>
      <p>美光+4.13%重回1000美元（盘中一度涨近7%）；闪迪+8.88%市值破2600亿美元；西部数据+5.35%；铠侠ADR+13%；SK海力士ADR+3%+。</p>
    </div>
    <div>
      <p class="text-white font-semibold mb-1">🏭 产业逻辑</p>
      <p>美光HBM产能已排满至2027年，Server DRAM结构性短缺持续。AI最终将占存储需求的近三分之二，2030年后存储需求仍以每年15%速度增长（历史均值10%）。摩根大通上调2028年存储市场至1.82万亿美元。</p>
    </div>
    <div class="bg-yellow-500/10 border border-yellow-500/20 rounded-lg p-2">
      <p class="text-yellow-300"><b>A股映射：</b>存储芯片ETF高开无悬念，但需警惕"美股涨→A股高开低走"的老剧本。雅克科技（HBM前驱体）、华海诚科（塑封料）、铜冠铜箔（载板/CCL）、长鑫科技（DRAM龙头）是核心受益标的。但当前位置追高性价比不高，建议回调后再布局。</p>
    </div>
  </div>
</div>

<div class="bg-white/5 rounded-xl p-4">
  <h4 class="text-white font-semibold mb-3 flex items-center gap-2">
    <span class="text-orange-400">A级</span>
    <span>🤖 人形机器人 — 宇树科技明日上市，第一股诞生</span>
  </h4>
  <div class="space-y-3 text-xs text-white/70 leading-relaxed">
    <div class="bg-orange-500/10 border border-orange-500/20 rounded-lg p-3">
      <p class="text-orange-300 font-semibold mb-1">📅 事件：宇树科技8月19日科创板上市</p>
      <p>· 发行价：150.80元/股，发行市盈率219.23倍（行业38.56倍，近6倍）</p>
      <p>· 发行市值：约609.93亿元，募资60.99亿元（超募近20亿）</p>
      <p>· 流通盘：仅3008.77万股（7.44%），筹码稀缺或加剧波动</p>
      <p>· 中签率：0.0181%，刷新科创板历史最低纪录，978万户参与</p>
      <p>· 战投阵容：DeepSeek（1.41亿，锁3年）、社保基金、中石油昆仑资本、南方电网</p>
    </div>
    <div>
      <p class="text-white font-semibold mb-1">🏆 公司地位</p>
      <p>2025年人形机器人出货量超5500台，全球市占率32.4%，居全球第一。全球少数实现规模化盈利的具身智能企业。核心零部件自研率超90%。上市前夕发布"超人"人形机器人，原地跳高2米、极限速度12.66m/s，超越人类纪录。</p>
    </div>
    <div class="bg-blue-500/10 border border-blue-500/20 rounded-lg p-2">
      <p class="text-blue-300"><b>产业意义：</b>①确立A股人形机器人定价基准，投资逻辑从概念转向产业验证；②豪华战投阵容（尤其DeepSeek深度绑定）验证AI+机器人的具身智能方向；③610亿市值为产业链公司提供估值锚。预计今日机器人板块将提前反应，绿的谐波、双环传动、汇川技术等核心零部件标的可关注。</p>
    </div>
  </div>
</div>

<div class="bg-white/5 rounded-xl p-4">
  <h4 class="text-white font-semibold mb-3 flex items-center gap-2">
    <span class="text-orange-400">A级</span>
    <span>💧 液冷/算力硬件 — 产业趋势最确定的方向</span>
  </h4>
  <div class="space-y-2 text-xs text-white/70 leading-relaxed">
    <p>· <b>应用材料Q3业绩超预期</b>：营收91亿美元+25%YoY创纪录，半导体设备需求持续强劲，验证AI资本开支景气度</p>
    <p>· <b>算力西迁加速</b>：远景百万卡集群在乌兰察布投产，DeepSeek计划再建1GW，AI竞争从算法效率转向能源工程能力</p>
    <p>· <b>英维克</b>：昨日+2.80%收58.69元，液冷龙头业绩确定性高，但154倍PE仍不便宜</p>
    <p>· <b>光通信/CPO</b>：Lumentum、康宁均涨超4%，中际旭创昨日成交352亿居全市场第一，算力硬件订单能见度最高</p>
  </div>
</div>

<div class="bg-white/5 rounded-xl p-4">
  <h4 class="text-white font-semibold mb-3 flex items-center gap-2">
    <span class="text-yellow-400">B级</span>
    <span>⚡ 地缘政治 — 美伊协议到期，黑天鹅风险升温</span>
  </h4>
  <div class="space-y-2 text-xs text-white/70 leading-relaxed">
    <p>· 特朗普8月17日明确表示：美国不寻求延长与伊朗的谅解备忘录</p>
    <p>· 伊朗外交部称革命卫队未与美国秘密对话，谈判陷入僵局</p>
    <p>· 布伦特原油站上91美元，如果霍尔木兹海峡局势升级，油价可能飙升</p>
    <p>· <b class="text-red-400">传导链：</b>油价飙升→通胀回升→美联储推迟降息→科技股杀估值。当前市场对地缘风险定价严重不足</p>
    <p>· 关注：军工、黄金、石油石化板块的避险机会</p>
  </div>
</div>

<div class="bg-white/5 rounded-xl p-4">
  <h4 class="text-white font-semibold mb-3 flex items-center gap-2">
    <span class="text-yellow-400">B级</span>
    <span>📋 政策面 — 增量政策+经济数据双窗口</span>
  </h4>
  <div class="space-y-2 text-xs text-white/70 leading-relaxed">
    <p>· <b>国务院全会</b>：强调及时谋划出台务实管用的增量政策，破除堵点卡点</p>
    <p>· <b>发改委</b>：部署加快2026年新型政策性金融工具投放，加大民间投资支持</p>
    <p>· <b>7月经济数据</b>：工业增加值+4.5%、社零+0.6%；高技术制造业+16.9%，存储芯片产量+30.2%</p>
    <p>· <b>LPR报价</b>：本周公布，市场预期5年期LPR可能下调5-10bp</p>
    <p>· <b>工信部</b>：重磅发文布局半导体核心赛道（金刚石、SiC、CPO、原子级制造、先进封装）</p>
  </div>
</div>

</div>
'''
gen.add_section("核心题材与今日催化", topic_html, "🔥")

# 持仓诊断
holding_html = '''
<div class="space-y-4">

<div class="bg-gradient-to-br from-yellow-500/20 to-orange-500/10 border border-yellow-500/30 rounded-xl p-4">
  <div class="flex items-center justify-between mb-3">
    <h4 class="text-yellow-300 font-semibold flex items-center gap-2"><span>💼</span> 持仓总览（8月17日收盘）</h4>
    <span class="text-xs bg-yellow-500/20 text-yellow-300 px-2 py-1 rounded">全线上涨</span>
  </div>
  <div class="grid grid-cols-2 md:grid-cols-4 gap-3 text-center">
    <div class="bg-white/5 rounded-lg p-2">
      <div class="text-xs text-white/60">英维克</div>
      <div class="text-base font-bold text-red-400">+2.80%</div>
      <div class="text-xs text-white/50">58.69元</div>
    </div>
    <div class="bg-white/5 rounded-lg p-2">
      <div class="text-xs text-white/60">铜冠铜箔</div>
      <div class="text-base font-bold text-red-400">+7.45%</div>
      <div class="text-xs text-white/50">132.22元</div>
    </div>
    <div class="bg-white/5 rounded-lg p-2">
      <div class="text-xs text-white/60">雅克科技</div>
      <div class="text-base font-bold text-red-400">+5.15%</div>
      <div class="text-xs text-white/50">159.01元</div>
    </div>
    <div class="bg-white/5 rounded-lg p-2">
      <div class="text-xs text-white/60">*ST建艺</div>
      <div class="text-base font-bold text-red-400">+0.69%</div>
      <div class="text-xs text-white/50">10.22元</div>
    </div>
  </div>
</div>

<div class="bg-white/5 rounded-xl p-4">
  <h4 class="text-white font-semibold mb-3 flex items-center gap-2"><span>🔍</span> 个股诊断与操作建议</h4>
  <div class="space-y-4 text-xs">

    <div class="bg-white/5 rounded-lg p-3 border-l-4 border-blue-400">
      <div class="flex justify-between items-center mb-2">
        <span class="text-white font-semibold">英维克（002837）- 液冷龙头</span>
        <span class="text-red-400 font-bold">+2.80% | 58.69元</span>
      </div>
      <div class="text-white/70 space-y-1 leading-relaxed">
        <p>📊 <b>走势：</b>昨日收58.69元涨2.80%，成交额23.81亿，换手率3.64%，温和放量上涨。</p>
        <p>💰 <b>估值：</b>TTM市盈率154.85倍，估值仍偏高，但在AI算力液冷赛道中业绩确定性最高。</p>
        <p>🎯 <b>催化：</b>应用材料Q3超预期验证AI资本开支景气；算力西迁加速（远景百万卡+DeepSeek 1GW），液冷需求持续爆发。</p>
        <p>⚡ <b>操作建议：</b>底仓持有（30%仓位）。液冷是AI算力基础设施，中期逻辑最硬。短期跟随科技板块波动，若反弹至65-68元区间可考虑减仓机动仓，回踩55元以下可补仓。止损位50元。</p>
      </div>
    </div>

    <div class="bg-white/5 rounded-lg p-3 border-l-4 border-red-400">
      <div class="flex justify-between items-center mb-2">
        <span class="text-white font-semibold">铜冠铜箔（301217）- 高位风险股</span>
        <span class="text-red-400 font-bold">+7.45% | 132.22元</span>
      </div>
      <div class="text-white/70 space-y-1 leading-relaxed">
        <p>📊 <b>走势：</b>昨日大涨7.45%收132.22元，成交额71.39亿，换手率6.78%，振幅10.14%，高位大幅震荡。</p>
        <p>⚠️ <b>风险提示：</b>董事会秘书兼财务负责人逝世公告发布后股价反而大涨，市场完全无视利空，说明情绪极度亢奋，典型的"利空当利好炒"=顶部信号。</p>
        <p>💰 <b>估值：</b>TTM市盈率667.78倍，严重透支。总市值1096亿，对应年净利润仅1.6亿，完全是靠存储/PCB概念炒作。</p>
        <p>⚡ <b>操作建议：</b><b class="text-red-400">逢高清仓！</b>667倍PE+管理层异动+高位放量滞涨后反而暴拉=典型的诱多出货行情。昨日涨7.45%但振幅10%（最高133.88→最低121.40），多空分歧极大。建议今日高开后立即减仓80%，保留底仓观察。目标止盈位130-135元分批清仓。止损位120元（跌破立即全部离场）。</p>
      </div>
    </div>

    <div class="bg-white/5 rounded-lg p-3 border-l-4 border-green-400">
      <div class="flex justify-between items-center mb-2">
        <span class="text-white font-semibold">雅克科技（002409）- 存储材料龙头</span>
        <span class="text-red-400 font-bold">+5.15% | 159.01元</span>
      </div>
      <div class="text-white/70 space-y-1 leading-relaxed">
        <p>📊 <b>走势：</b>昨日涨5.15%收159.01元，成交额45.21亿，换手率9.11%，放量上涨，BBD主力净流入3.93亿。</p>
        <p>🎯 <b>催化：</b>隔夜美光+4.13%+闪迪+8.88%+存储超级周期再确认，今日大概率高开。雅克是HBM前驱体国内龙头，直接受益于存储芯片景气。</p>
        <p>💰 <b>估值：</b>TTM市盈率75.18倍，在半导体材料板块中不算离谱，但也不便宜。从高点246元已回调35%，处于中期调整后的反弹阶段。</p>
        <p>⚡ <b>操作建议：</b>底仓持有（30%仓位），机动仓逢高减仓。隔夜存储股大涨为今日提供情绪支撑，但160-170元区间是前期密集成交区，压力较大。若高开至165元以上可减仓机动仓，回踩145元以下可考虑补仓。止损位135元。</p>
      </div>
    </div>

    <div class="bg-white/5 rounded-lg p-3 border-l-4 border-gray-400">
      <div class="flex justify-between items-center mb-2">
        <span class="text-white font-semibold">*ST建艺（002789）- 观察标的</span>
        <span class="text-red-400 font-bold">+0.69% | 10.22元</span>
      </div>
      <div class="text-white/70 space-y-1 leading-relaxed">
        <p>📊 <b>走势：</b>昨日微涨0.69%收10.22元，成交额仅1222万，换手率0.77%，成交清淡，无方向性信号。</p>
        <p>⚡ <b>操作建议：</b>底仓持有观望。ST股流动性差，不建议加仓。等待摘帽或重大资产重组信号。止损位9.5元。</p>
      </div>
    </div>

  </div>
</div>

<div class="bg-yellow-500/10 border border-yellow-500/30 rounded-xl p-4">
  <h4 class="text-yellow-300 font-semibold mb-2 flex items-center gap-2"><span>📋</span> 今日操作计划</h4>
  <div class="text-xs text-white/70 space-y-1.5 leading-relaxed">
    <p>1. <b class="text-red-400">铜冠铜箔：</b>高开后减仓80%，130-135元区间分批清仓，只留小部分底仓观察。667倍PE+管理层异动=必须降仓。</p>
    <p>2. <b class="text-white">雅克科技：</b>若高开至165元以上，减仓机动仓（20%仓位），底仓30%持有。隔夜存储股大涨是利好，但160-170压力大。</p>
    <p>3. <b class="text-blue-400">英维克：</b>持有不动，液冷中期逻辑最硬。55元以下可补仓，65元以上减机动仓。</p>
    <p>4. <b class="text-gray-400">*ST建艺：</b>持有观望，不操作。</p>
    <p>5. <b class="text-yellow-400">总体仓位：</b>4-5成。利用今日高开继续减仓高位股，锁定利润，等待回调后再布局。</p>
  </div>
</div>

</div>
'''
gen.add_section("持仓诊断与操作建议", holding_html, "💼")

# 空方视角
bear_html = '''
<div class="space-y-4">

  <div class="text-white font-semibold flex items-center gap-2 mb-3">
    <span>⚖️</span>
    <span>空方视角：狂欢还是陷阱？8个必须警惕的风险</span>
  </div>

  <div class="space-y-3">
    <div class="bg-white/5 rounded-lg p-3">
      <p class="text-red-300 font-semibold mb-1">风险1：科技拥挤度达历史99%分位，随时可能踩踏</p>
      <p>半导体/算力板块成交额占比已处于历史99%分位，是全市场最拥挤的方向。申万宏源说AI产业链重拾强势需要"四步走"，当前只走完了"第一步超跌反弹"。9月政策窗口可能才是本轮反弹真正的高点。拥挤交易的特征是：涨的时候一起涨，跌的时候踩踏式下跌。</p>
    </div>
    <div class="bg-white/5 rounded-lg p-3">
      <p class="text-red-300 font-semibold mb-1">风险2：4000点关口压力巨大，沪指60分钟顶背离</p>
      <p>沪指逼近4000点整数关口，这是重要心理关口。更关键的是60分钟K线已出现顶背离信号，日线KDJ高位钝化。量能如果无法持续放大（2.39万亿已经是天量），需要防范二次探底。昨日虽然放量上涨，但高位股不少冲高回落，说明上方抛压不小。</p>
    </div>
    <div class="bg-white/5 rounded-lg p-3">
      <p class="text-red-300 font-semibold mb-1">风险3：长鑫科技4万亿市值=泡沫信号？</p>
      <p>长鑫科技上市21天涨6倍，市值4.13万亿=2.5个茅台。静态PE高达123倍（远期PE约20倍），流通盘仅约10%，少量资金就能撬动巨大涨幅。这波行情到底是"硬核叙事驱动的价值重估"还是"新股+题材+小流通盘"的炒作？一旦市场情绪转向，没有业绩支撑的高位股会跌得很快。历史上每次新股爆炒后都是一地鸡毛。</p>
    </div>
    <div class="bg-white/5 rounded-lg p-3">
      <p class="text-red-300 font-semibold mb-1">风险4：铜冠铜箔667倍PE+董秘逝世=利空出尽？还是最后狂欢？</p>
      <p>董秘兼财务负责人逝世这种消息，放在正常市场是绝对的利空（管理层异动=不确定性=折价）。但在A股，反而涨了7.45%。这不是"利空出尽"，是"情绪极度亢奋"——任何消息都能被解读为利好。667倍PE是什么概念？需要667年的盈利才能收回投资。这已经不是投资，是博傻。</p>
    </div>
    <div class="bg-white/5 rounded-lg p-3">
      <p class="text-red-300 font-semibold mb-1">风险5：美伊谈判破裂=油价飙升=科技股杀估值</p>
      <p>特朗普明确不延长美伊谅解备忘录，伊朗说没有秘密对话，谈判已陷入僵局。如果霍尔木兹海峡局势升级，油价可能从90美元飙升到100+美元。传导链很清晰：油价涨→通胀反弹→美联储推迟降息→美债收益率上升→科技股杀估值。当前市场对这个风险几乎完全没有定价，一旦出事就是黑天鹅。</p>
    </div>
    <div class="bg-white/5 rounded-lg p-3">
      <p class="text-red-300 font-semibold mb-1">风险6：微软-3%预示AI软件泡沫破裂？</p>
      <p>微软单日跌3%、蒸发1120亿美元，相当于它一整年资本开支的96%。这背后是市场对"AI资本开支回报率"的质疑——AI硬件（芯片/存储/设备）涨得很猛，但AI软件/应用端（微软/ Meta/谷歌）在跌。如果AI应用端的商业模式跑不通，那硬件端的高增长就是空中楼阁。这是一个值得警惕的分化信号。</p>
    </div>
    <div class="bg-white/5 rounded-lg p-3">
      <p class="text-red-300 font-semibold mb-1">风险7：中报密集披露期，业绩验证才刚开始</p>
      <p>截至目前才476家公司披露半年报，不到A股的10%。接下来两周是中报披露最高峰。很多高位科技股的估值都是建立在"AI永远增长"的假设上，但实际业绩能不能跟上？工业富联中报+96%反而跌4.58%的教训还在眼前——利好出尽=出货信号。</p>
    </div>
    <div class="bg-white/5 rounded-lg p-3">
      <p class="text-red-300 font-semibold mb-1">风险8：LPR/经济数据不及预期的下行风险</p>
      <p>本周LPR报价+7月经济数据密集落地。市场已经price in了降息预期，如果LPR降息幅度不及预期（5bp vs 预期10bp），或者经济数据偏弱，都可能触发调整。7月社零仅+0.6%，消费依然疲软，经济复苏基础不牢固。</p>
    </div>
  </div>

  <div class="bg-green-500/10 border border-green-500/30 rounded-xl p-4">
    <h4 class="text-green-300 font-semibold mb-3 flex items-center gap-2"><span>🐂</span> 多方反驳：科技牛市才刚上路·调整就是上车机会</h4>
    <div class="text-xs text-white/70 space-y-2 leading-relaxed">
      <p>① <b>存储超级周期才走了三分之一</b>：美光HBM排满到2027年、BofA上调FY30 EPS到200-250美元、远期目标价1550-2200美元。供需短缺至少持续两年，A股存储材料公司的业绩爆发期还在后面（Q3-Q4旺季），现在谈顶部太早。</p>
      <p>② <b>长鑫4万亿是"中国科技定价权"的体现</b>：不是泡沫，是价值重估。DRAM是战略物资，长鑫作为国内唯一规模化厂商，国产替代空间巨大。全球第四+AI存储爆发+国产替代三重逻辑，4万亿只是起点。</p>
      <p>③ <b>政策底+流动性底+业绩底三底共振</b>：央行每天6000亿隔夜逆回购+买断式逆回购，流动性非常充裕。发改委加码政策性金融工具，国务院强调增量政策。高技术制造业+16.9%，新动能增长强劲。</p>
      <p>④ <b>AI硬件才是确定性最强的方向</b>：软件端有商业模式的问题，但硬件端是实打实的订单和业绩。应用材料连续两季创纪录营收、客户给8季度预测，说明AI资本开支不是泡沫。A股液冷、PCB、光模块都有业绩支撑。</p>
      <p>⑤ <b>宇树科技上市=机器人产业里程碑</b>：人形机器人第一股上市，DeepSeek战略投资，AI+具身智能的时代正式开启。这不是炒作，是产业趋势的起点。机器人板块的长期空间比AI软件更大。</p>
    </div>
  </div>

  <div class="bg-yellow-500/10 border border-yellow-500/30 rounded-xl p-4">
    <h4 class="text-yellow-300 font-semibold mb-2 flex items-center gap-2"><span>⚖️</span> 综合判断</h4>
    <p class="text-xs text-white/70 leading-relaxed">
      短期（本周）：A股处于"超跌反弹后的情绪高涨期"，隔夜存储股暴涨+长鑫科技财富效应推动市场情绪亢奋。但沪指4000点关口压力+科技拥挤度历史高位+8大风险因素并存，<b class="text-red-400">高开低走的概率大于继续冲高</b>。建议利用今日高开减仓高位股（铜冠铜箔必须减），不要追高。<br>
      中期（1-3个月）：存储超级周期+AI算力需求爆发+国产替代加速+政策支持，四大逻辑支撑科技成长股中期向好。但当前整体估值偏高，需要中报业绩验证，调整后优质标的布局性价比更高。<br>
      <b class="text-yellow-400">核心结论：短期谨慎乐观，利用高开减仓高位股锁定利润。
      仓位控制在4-5成，等回调后再加仓。
      优先级：减仓铜冠（最危险）→ 雅克机动仓减仓→ 英维克持有。
      关注宇树科技上市对机器人板块的催化，但不建议追高，等回调后布局核心零部件。</b>
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

      <div class="bg-green-500/10 border border-green-500/30 rounded-lg p-3">
        <div class="flex justify-between mb-2">
          <span class="text-green-300 font-semibold">预判#20260817-01：本周四大事件落地后科技股迎来布局窗口</span>
          <span class="text-xs bg-yellow-500/30 text-yellow-200 px-2 py-0.5 rounded">验证中·T+1</span>
        </div>
        <p class="text-white/70">预判内容：本周四大事件（经济数据、LPR、机器人大会、美联储纪要）落地后，不确定性消除，科技股有望迎来新一轮布局窗口，存储/液冷/先进封装三个方向率先反弹5-10%。</p>
        <p class="text-white/50 mt-1">当前进度：T+1验证（昨日首日），科技股全线大涨——半导体+4.9%、电子化学品+5.13%、创业板+3.14%。雅克科技+5.15%、铜冠铜箔+7.45%。反弹幅度和速度超预期，但持续性待验证。注意：四大事件尚未全部落地，当前是"预期行情"而非"落地行情"。</p>
      </div>

      <div class="bg-yellow-500/10 border border-yellow-500/30 rounded-lg p-3">
        <div class="flex justify-between mb-2">
          <span class="text-yellow-300 font-semibold">预判#20260817-02：铜冠铜箔短期见顶，调整幅度15-20%</span>
          <span class="text-xs bg-red-500/30 text-red-200 px-2 py-0.5 rounded">面临挑战·T+1</span>
        </div>
        <p class="text-white/70">预判内容：铜冠铜箔621倍PE严重透支+董秘无法履职风险，短期见顶调整15-20%，目标100-105元。</p>
        <p class="text-white/50 mt-1">当前进度：T+1验证，昨日铜冠反而大涨7.45%收132.22元（预判失败风险大）。但需要注意：董秘逝世公告（注意：已从"无法履职"变为"逝世"，情况更严重）发布后股价暴涨，这是典型的情绪亢奋期特征——利空当利好炒。这种行情往往是最后一涨，后续可能快速反转。继续观察T+3（本周四）验证。</p>
      </div>

      <div class="bg-yellow-500/10 border border-yellow-500/30 rounded-lg p-3">
        <div class="flex justify-between mb-2">
          <span class="text-yellow-300 font-semibold">预判#20260814-01：闪迪投资者日催化存储板块二次反弹</span>
          <span class="text-xs bg-green-500/30 text-green-200 px-2 py-0.5 rounded">基本验证·T+3</span>
        </div>
        <p class="text-white/70">预判内容：闪迪投资者日超级指引将催化A股存储板块情绪修复，存储材料/设备方向有望迎来3-5%高开反弹。</p>
        <p class="text-white/50 mt-1">验证结果：T+3验证，存储板块持续走强。雅克科技累计反弹约+12%（从142到159），铜冠铜箔反弹约+15%（从115到132）。反弹幅度远超预期，主要是叠加了长鑫科技暴涨的情绪扩散效应和隔夜美光/闪迪的持续催化。基本验证正确，但幅度超预期。</p>
      </div>

      <div class="bg-yellow-500/10 border border-yellow-500/30 rounded-lg p-3">
        <div class="flex justify-between mb-2">
          <span class="text-yellow-300 font-semibold">预判#20260814-02：A股短期调整延续至下周三</span>
          <span class="text-xs bg-red-500/30 text-red-200 px-2 py-0.5 rounded">验证失败·T+3</span>
        </div>
        <p class="text-white/70">预判内容：A股放量下跌后短期调整3-5个交易日，沪指3850-3950区间震荡，下周三前后出现布局机会。</p>
        <p class="text-white/50 mt-1">验证结果：失败。T+3验证，沪指已涨至3982点（突破3950上限），且连续两日放量上涨。调整期被政策利好+美股科技股反弹+长鑫科技财富效应三重催化提前结束。市场总是在变化的，"调整3-5天"的线性外推被证明过于简单化。</p>
      </div>

      <div class="bg-red-500/10 border border-red-500/30 rounded-lg p-3">
        <div class="flex justify-between mb-2">
          <span class="text-red-300 font-semibold">预判#20260812-01：算力期货催化算力产业链</span>
          <span class="text-xs bg-red-500/30 text-red-200 px-2 py-0.5 rounded">已验证·失败</span>
        </div>
        <p class="text-white/70">预判内容：CME推出算力期货催化算力产业链，GPU/服务器/液冷方向反弹2-3%。</p>
        <p class="text-white/50 mt-1">验证结果：失败。"新物种"题材发酵需要时间，短期催化效应有限。</p>
      </div>

      <div class="bg-green-500/10 border border-green-500/30 rounded-lg p-3">
        <div class="flex justify-between mb-2">
          <span class="text-green-300 font-semibold">预判#20260803-01：雅克科技跌停后3日内反弹</span>
          <span class="text-xs bg-green-500/30 text-green-200 px-2 py-0.5 rounded">已验证·正确</span>
        </div>
        <p class="text-white/70">预判内容：雅克科技跌停板机构抄底近5亿，预计3个交易日内5-10%反弹。</p>
        <p class="text-white/50 mt-1">实际走势：从127元反弹至最高159元（+25%），远超预期。验证正确。</p>
      </div>

      <div class="bg-green-500/10 border border-green-500/30 rounded-lg p-3">
        <div class="flex justify-between mb-2">
          <span class="text-green-300 font-semibold">预判#20260730-02：存储板块调整期2-3周</span>
          <span class="text-xs bg-green-500/30 text-green-200 px-2 py-0.5 rounded">已验证·正确</span>
        </div>
        <p class="text-white/70">预判内容：科技股大跌后存储板块调整2-3周，幅度15-25%。</p>
        <p class="text-white/50 mt-1">验证结果：第14个交易日，板块回调约20%后反弹。时间和幅度均验证正确。目前调整期已结束，进入反弹阶段。</p>
      </div>

      <div class="bg-red-500/10 border border-red-500/30 rounded-lg p-3">
        <div class="flex justify-between mb-2">
          <span class="text-red-300 font-semibold">新增预判#20260818-01：宇树科技上市首日涨幅超200%，机器人板块T+2见光死</span>
          <span class="text-xs bg-red-500/30 text-red-200 px-2 py-0.5 rounded">待验证·T+3</span>
        </div>
        <p class="text-white/70">预判内容：宇树科技明日上市，按今年新股平均涨幅276%测算，首日可能涨200-300%，市值突破1500-2000亿。但机器人板块会出现"上市日即高点"的见光死行情，T+2（8月21日）前后开始回调，核心零部件标的回调幅度10-15%。</p>
        <p class="text-white/50 mt-1">验证时间：8月21日（T+3，周五）验证机器人板块是否见光死</p>
      </div>

      <div class="bg-red-500/10 border border-red-500/30 rounded-lg p-3">
        <div class="flex justify-between mb-2">
          <span class="text-red-300 font-semibold">新增预判#20260818-02：沪指4000点关口遇阻，本周回调至3900附近</span>
          <span class="text-xs bg-red-500/30 text-red-200 px-2 py-0.5 rounded">待验证·T+4</span>
        </div>
        <p class="text-white/70">预判内容：沪指逼近4000点关口，叠加科技拥挤度历史高位+中报密集披露+地缘风险，本周在4000点附近遇阻回落，回调至3900点附近（约-2%）。4000点整数关口是强压力位，第一次冲击大概率失败。</p>
        <p class="text-white/50 mt-1">验证时间：8月22日（T+4，周六）验证沪指是否在4000点遇阻回落</p>
      </div>

    </div>
  </div>

  <div class="bg-white/5 rounded-xl p-4">
    <h4 class="text-white font-semibold mb-2 flex items-center gap-2"><span>📊</span> 准确率统计</h4>
    <div class="grid grid-cols-3 gap-3 text-center text-xs">
      <div class="bg-white/5 rounded-lg p-2">
        <div class="text-lg font-bold text-yellow-400">65%</div>
        <div class="text-white/60">总体准确率</div>
      </div>
      <div class="bg-white/5 rounded-lg p-2">
        <div class="text-lg font-bold text-green-400">15/23</div>
        <div class="text-white/60">已验证正确/总数</div>
      </div>
      <div class="bg-white/5 rounded-lg p-2">
        <div class="text-lg font-bold text-blue-400">6</div>
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
    <p class="text-red-300 font-semibold mb-1">教训#1：利空当利好炒=情绪顶部信号，立即减仓</p>
    <p class="text-white/60 text-xs">
      铜冠铜箔董秘逝世公告后反而大涨7.45%，这就是典型的"利空当利好炒"。
      当市场情绪亢奋到任何消息都能被解读为利好的时候，就是离顶部不远了。
      <b>正确做法</b>：高位股出利空反而大涨=减仓信号。
      不要被"利空出尽就是利好"的话术骗了——真正的利空出尽是股价跌到位后横盘企稳，
      不是出了利空反而暴涨。后者是主力利用利空消息"最后一拉"出货的手段。
      记住：在顶部，好消息是出货机会，坏消息更是出货机会。
    </p>
  </div>

  <div class="bg-orange-500/10 border border-orange-500/30 rounded-lg p-3">
    <p class="text-orange-300 font-semibold mb-1">教训#2：4000点关口第一次冲击必失败，提前减仓</p>
    <p class="text-white/60 text-xs">
      沪指逼近4000点整数关口。整数关口是强心理压力位，第一次冲击大概率失败。
      因为所有人都在盯着4000点——有人想在4000点减仓，有人想等突破再追。
      结果就是：到了4000点附近，卖盘突然增加，买盘退缩，然后回落。
      <b>正确做法</b>：在指数接近重要整数关口时（如3000、4000、5000点），
      提前减仓20-30%，等突破确认后再加回来。
      虽然可能少赚几个点，但避免了冲高回落的回撤。
      在股市里，少亏=多赚。
    </p>
  </div>

  <div class="bg-yellow-500/10 border border-yellow-500/30 rounded-lg p-3">
    <p class="text-yellow-300 font-semibold mb-1">教训#3：科技拥挤度99%分位=随时可能踩踏</p>
    <p class="text-white/60 text-xs">
      半导体/算力板块成交额占比处于历史99%分位，这意味着全市场的钱都在往科技股里挤。
      拥挤交易的特征是涨的时候一起涨（因为所有人都在买），跌的时候一起跌（因为所有人都在卖）。
      99%分位意味着什么？意味着历史上只有1%的时间比现在更拥挤，
      而那1%的时间之后几乎都出现了大幅调整。
      <b>正确做法</b>：拥挤度90%以上开始减仓，95%以上大幅减仓，99%以上只卖不买。
      不要因为"还在涨"就舍不得卖——涨得越凶，跌得越狠。
      在别人贪婪的时候恐惧，这句话在拥挤交易里尤其适用。
    </p>
  </div>

  <div class="bg-green-500/10 border border-green-500/30 rounded-lg p-3">
    <p class="text-green-300 font-semibold mb-1">教训#4：美股涨≠A股涨，但美股跌=A股大概率跌</p>
    <p class="text-white/60 text-xs">
      隔夜费半+1.64%、美光+4.13%、闪迪+8.88%，很多人又开始兴奋了，以为今天A股存储股一定大涨。
      但历史经验告诉我们：美股涨的时候，A股经常高开低走；美股跌的时候，A股大概率跟着跌。
      原因很简单：A股是"利好出尽"的市场，美股涨了=A股人都知道了=开盘就兑现。
      <b>正确做法</b>：隔夜美股大涨，A股开盘不是买入机会，而是卖出机会（尤其是高位股）。
      等高开低走、下午回落了，如果量能还行，再考虑要不要接回来。
      永远不要因为"美股涨了"就去追A股的高开。
    </p>
  </div>

  <div class="bg-blue-500/10 border border-blue-500/30 rounded-lg p-3">
    <p class="text-blue-300 font-semibold mb-1">教训#5：新股上市日=概念股见光死日</p>
    <p class="text-white/60 text-xs">
      宇树科技明天上市，人形机器人板块今天可能会提前炒作。
      但历史经验告诉我们：重磅新股上市的当天或次日，相关概念股往往"见光死"。
      因为概念股已经炒了很久了，所有人都在等新股上市这个"终极催化剂"来出货。
      长鑫科技上市前，存储概念股也炒了一波；上市后呢？自己去看看走势。
      <b>正确做法</b>：如果手里有机器人概念股，趁宇树上市前的情绪炒作卖出一部分。
      如果没有，不要追高进去"博上市行情"——上市当天就是利好出尽的日子。
      等回调10-15%后，如果产业逻辑还在，再考虑布局。
    </p>
  </div>

  <div class="bg-purple-500/10 border border-purple-500/30 rounded-lg p-3">
    <p class="text-purple-300 font-semibold mb-1">教训#6：地缘风险从来不"price in"，出事就是黑天鹅</p>
    <p class="text-white/60 text-xs">
      美伊谅解备忘录到期了，特朗普说不延长，伊朗说没谈过。
      市场好像完全不在乎，油价只涨了0.44%，科技股照样涨。
      但地缘风险的特点是：市场永远不会提前"price in"，
      因为大家都觉得"打不起来"、"只是嘴炮"。
      然后真打起来的时候，就是黑天鹅——油价暴涨、股市暴跌、黄金飙升。
      <b>正确做法</b>：不要因为"市场没反应"就觉得风险不存在。
      配置一小部分黄金/军工作为对冲（5-10%仓位），
      大部分时间可能没用，但一旦出事就是救命的。
      保险平时没用，但出事的时候你会感谢自己买了。
    </p>
  </div>

  <div class="bg-pink-500/10 border border-pink-500/30 rounded-lg p-3">
    <p class="text-pink-300 font-semibold mb-1">教训#7："XX第一股"上市后估值会锚定整个板块，但不一定是往上锚</p>
    <p class="text-white/60 text-xs">
      很多人觉得"人形机器人第一股"上市会给整个板块估值抬升。
      但现实可能更复杂——如果宇树科技上市后被爆炒到1000亿+市值，
      反而会让现有机器人公司显得"便宜"还是"贵"？
      参考长鑫科技上市后的情况：长鑫4万亿市值，反而让其他存储股显得"还能涨"。
      但如果宇树上市后大跌呢？那整个板块都会被带下来。
      <b>正确做法</b>：不要预设方向，观察市场的实际反应。
      如果宇树上市后大涨且稳住了，可以做多核心零部件（补涨逻辑）；
      如果宇树上市后高开低走，立即清仓所有机器人概念股。
      跟随市场，不要预判市场。
    </p>
  </div>

</div>
'''
gen.add_section("教训库引用", lesson_html, "📚")

# 生成+发布
output_path = os.path.join(WORK_DIR, 'docs/daily/20260818_每日新闻洞察.html')
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
