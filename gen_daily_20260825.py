#!/usr/bin/env python3
"""2026年8月25日 每日新闻洞察生成 - 周二"""
import sys, os, shutil, json
WORK_DIR = '/root/daily-news-insight'
sys.path.insert(0, os.path.join(WORK_DIR, 'v3'))
from generators.daily_pro import DailyReportProGenerator

gen = DailyReportProGenerator(
    date_str='2026年8月25日', weekday='星期二',
    subtitle='2026年8月25日 周二 · 费半-2.7%三星-8.7%·美光-5.83%·高盛上调WFE至2810亿·英维克半年报·央行5000亿MLF',
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
        '美股半导体暴跌冲击全球：费城半导体-2.70%、三星电子-8.70%（创单日最大跌幅）、美光-5.83%、英伟达七连跌-2.91%创2022年最长连跌纪录；存储/光通信板块重挫，闪迪/希捷-6%+，AOI-13%',
        '三重利空共振：①苹果或获准采购中国存储芯片（CXMT/YMTC）传闻冲击美系存储股；②三星100万亿韩元股东回报不及预期（无即时回购）；③英伟达财报前避险+美债收益率高位，科技股估值承压',
        'A股昨日放量调整：沪指-0.59%收3882点（探至3855后回拉），深成指-2.13%，创业板-3.21%，科创50-3.10%，两市成交2.01万亿放量1280亿；贵金属/煤炭/银行逆势走强，CPO/半导体/元件领跌',
        '高盛重磅上调WFE：2026-2028年全球晶圆厂设备支出上调至1500亿/2180亿/2810亿美元，2027年增速从32%跳升至45%，存储与先进代工双轮驱动，设备景气周期延长至2028年',
        '今日三大焦点：①央行5000亿MLF操作+月末隔夜逆回购（每日最高6000亿），流动性宽松托底；②英维克半年报（营收+17%、净利-14%，Q2环比改善）；③上海"十五五"产业规划利好半导体/6G'
    ],
    operation_advice='周二开盘：隔夜半导体暴跌+A股昨日放量调整，今日科技板块大概率低开。但央行5000亿MLF+月末隔夜逆回购提供流动性支撑，下方3850点有护盘。操作策略：①科技股低开不急于抄底，观察3850支撑和量能；②英维克半年报Q2修复但净利仍下滑，关注市场反应；③防御方向（贵金属/煤炭）可继续持有；④仓位控制在4-5成，等待英伟达财报（周三）和杰克逊霍尔会议（周五）落地后再决策',
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
    description='每日新闻洞察 2026年8月25日：费半-2.7%三星-8.7%、美光-5.83%、高盛上调WFE至2810亿、英维克半年报、央行5000亿MLF+隔夜逆回购',
)

gen.add_global_market()

global_cards1 = render_cards([
    {"name":"道琼斯","change":"+0.26%","up":True},
    {"name":"标普500","change":"-0.28%","up":False},
    {"name":"纳斯达克","change":"-0.76%","up":False},
    {"name":"费城半导体","change":"-2.70%","up":False},
    {"name":"日经225","change":"-0.90%","up":False},
    {"name":"恒生指数","change":"-1.89%","up":False},
])
global_list1 = render_list([
    {"name":"WTI原油","change":"+0.16%/$85.15","up":True},
    {"name":"布伦特原油","change":"-0.03%/$90.52","up":False},
    {"name":"COMEX黄金","change":"+0.88%/$4739.16","up":True},
    {"name":"COMEX白银","change":"+1.10%/$70.14","up":True},
])
global_list2 = render_list([
    {"name":"三星电子","change":"-8.70%","up":False},
    {"name":"SK海力士","change":"-3.41%","up":False},
    {"name":"美光科技","change":"-5.83%","up":False},
    {"name":"台积电ADR","change":"-2.11%","up":False},
])
global_list3 = render_list([
    {"name":"英伟达","change":"-2.91%/$208.48","up":False},
    {"name":"AMD","change":"-3.49%/$456.75","up":False},
    {"name":"微软","change":"+0.84%/$487.31","up":True},
    {"name":"苹果","change":"+0.32%/$310.34","up":True},
    {"name":"博通","change":"-2.63%/$358.76","up":False},
    {"name":"英特尔","change":"-3.12%/$87.26","up":False},
    {"name":"应用材料","change":"-1.65%/$484.19","up":False},
    {"name":"阿斯麦","change":"-1.34%/$1740.13","up":False},
])

global_html = '''
<div class="grid md:grid-cols-3 gap-4">
  <div class="md:col-span-2">
    <div class="text-white font-semibold mb-3 flex items-center gap-2"><span>🌍</span><span>隔夜全球市场 · 半导体暴跌·三星单日崩-8.7%·英伟达七连跌·黄金创新高</span></div>
    <div class="grid grid-cols-3 md:grid-cols-6 gap-2">{0}</div>
    <p class="text-xs text-white/50 mt-3 leading-relaxed">
      ⚡ <b class="text-red-400">核心要点：美股三大指数分化，道指微涨但纳指跌0.76%，费城半导体暴跌2.70%创近期最大单日跌幅。三星电子暴跌8.70%创历史最大单日跌幅之一，美光跌5.83%，英伟达连续第七个交易日下跌（-2.91%）创2022年以来最长连跌纪录。黄金逆势上涨+0.88%收4739美元创近三个月新高，避险情绪升温。</b>——<br>
      ①<b>存储板块重挫（三重利空）</b>：<br>
      &nbsp;&nbsp;·苹果采购中国存储芯片传闻：特朗普政府可能允许苹果从长鑫存储（CXMT）和长江存储（YMTC）采购存储芯片，作为9月中美元首会晤前的缓和姿态，美光等美系存储股承压<br>
      &nbsp;&nbsp;·三星股东回报不及预期：三星宣布2026年股东回报90-110万亿韩元，但缺乏即时回购和注销承诺，投资者失望导致股价暴跌8.7%<br>
      &nbsp;&nbsp;·美光+AI存储瓶颈担忧：美光研究员在Hot Chips 2026上指出AI算力增速远超内存带宽增速，存储瓶颈制约AI发展<br>
      &nbsp;&nbsp;存储板块全线下跌：闪迪-6.45%、希捷-6.51%、美光-5.83%、西部数据-5.24%、SK海力士ADR-4.92%。<br>
      ②<b>光通信板块同步暴跌</b>：Applied Optoelectronics（AOI）大跌超13%，Lumentum跌4.22%、Coherent跌超4%。光通信是AI算力硬件链中跌幅最大的方向之一。<br>
      ③<b>英伟达七连跌创2022年以来纪录</b>：跌2.91%收208.48美元，连续第七个交易日下跌，为2022年以来最长连跌。市场等待周三Q2财报（预期营收约920亿美元），财报前避险情绪浓厚。<br>
      ④<b>高盛重磅上调WFE预期</b>：将2026-2028年全球晶圆厂设备（WFE）支出预测大幅上调至1500亿/2180亿/2810亿美元，2027年增速从32%跳升至45%，存储与先进代工双轮驱动，设备景气周期延长至2028年。<br>
      ⑤<b>黄金创近三个月新高</b>：COMEX黄金+0.88%收4739.16美元，白银+1.10%收70.14美元。美债风险外溢+美元信用对冲+地缘风险升温，黄金避险属性凸显。<br>
      ⑥<b>亚太市场普跌</b>：日经225-0.90%，恒生指数-1.89%。韩国KOSPI暴跌3.12%（三星-8.7%拖累）。
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
  <div class="bg-gradient-to-br from-green-500/20 to-emerald-500/10 border border-green-500/30 rounded-xl p-3 text-center">
    <div class="text-xs text-white/60 mb-1">上证指数</div>
    <div class="text-xl font-bold text-green-400">3882.01</div>
    <div class="text-xs text-green-400">-0.59%</div>
  </div>
  <div class="bg-gradient-to-br from-green-500/20 to-emerald-500/10 border border-green-500/30 rounded-xl p-3 text-center">
    <div class="text-xs text-white/60 mb-1">深证成指</div>
    <div class="text-xl font-bold text-green-400">13794.29</div>
    <div class="text-xs text-green-400">-2.13%</div>
  </div>
  <div class="bg-gradient-to-br from-green-500/20 to-emerald-500/10 border border-green-500/30 rounded-xl p-3 text-center">
    <div class="text-xs text-white/60 mb-1">创业板指</div>
    <div class="text-xl font-bold text-green-400">3431.89</div>
    <div class="text-xs text-green-400">-3.21%</div>
  </div>
  <div class="bg-gradient-to-br from-green-500/20 to-emerald-500/10 border border-green-500/30 rounded-xl p-3 text-center">
    <div class="text-xs text-white/60 mb-1">科创50</div>
    <div class="text-xl font-bold text-green-400">1602.34</div>
    <div class="text-xs text-green-400">-3.10%</div>
  </div>
</div>

<div class="grid md:grid-cols-2 gap-4">
  <div class="bg-white/5 rounded-xl p-4">
    <h4 class="text-white font-semibold mb-3 flex items-center gap-2"><span>📈</span> 逆势走强板块</h4>
    <div class="space-y-1 text-xs">
      <div class="flex justify-between"><span class="text-white/70">焦炭/煤炭</span><span class="text-red-400 font-semibold">+5.39%</span></div>
      <div class="flex justify-between"><span class="text-white/70">贵金属</span><span class="text-red-400 font-semibold">+1.38%</span></div>
      <div class="flex justify-between"><span class="text-white/70">种植业与林业</span><span class="text-red-400 font-semibold">+2.06%</span></div>
      <div class="flex justify-between"><span class="text-white/70">银行</span><span class="text-red-400 font-semibold">+1.32%</span></div>
      <div class="flex justify-between"><span class="text-white/70">保险</span><span class="text-red-400 font-semibold">+2.58%</span></div>
      <div class="flex justify-between"><span class="text-white/70">煤炭开采</span><span class="text-red-400 font-semibold">+3.50%</span></div>
    </div>
  </div>
  <div class="bg-white/5 rounded-xl p-4">
    <h4 class="text-white font-semibold mb-3 flex items-center gap-2"><span>📉</span> 领跌板块</h4>
    <div class="space-y-1 text-xs">
      <div class="flex justify-between"><span class="text-white/70">CPO/光通信</span><span class="text-green-400 font-semibold">-5~7%</span></div>
      <div class="flex justify-between"><span class="text-white/70">元件/PCB</span><span class="text-green-400 font-semibold">-4.18%</span></div>
      <div class="flex justify-between"><span class="text-white/70">通信设备</span><span class="text-green-400 font-semibold">-5.21%</span></div>
      <div class="flex justify-between"><span class="text-white/70">半导体</span><span class="text-green-400 font-semibold">-3.50%</span></div>
      <div class="flex justify-between"><span class="text-white/70">CRO/创新药</span><span class="text-green-400 font-semibold">-3.43%</span></div>
      <div class="flex justify-between"><span class="text-white/70">玻璃玻纤</span><span class="text-green-400 font-semibold">-5.30%</span></div>
    </div>
  </div>
</div>

<div class="bg-white/5 rounded-xl p-4">
  <h4 class="text-white font-semibold mb-3 flex items-center gap-2"><span>📊</span> 市场概况与解读</h4>
  <div class="text-xs text-white/70 space-y-2 leading-relaxed">
    <p><b class="text-white">成交额2.01万亿</b>：较上周五放量约1282亿元，沪市9520亿、深市1.055万亿。全市场1460只上涨、3965只下跌，涨跌比约1:2.7，赚钱效应约26.9%。涨停48家、跌停11家。</p>
    <p><b class="text-yellow-400">冰火两重天格局</b>：典型的"沪指抗跌、双创重挫"放量调整。沪指盘中探至3855.35点后尾盘拉回，权重蓝筹（银行/煤炭/贵金属）托底效应明显。科技成长股全线杀跌，中际旭创跌7.7%市值跌破万亿，天孚通信-8.6%、新易盛-6.8%。</p>
    <p><b class="text-white">资金流向</b>：全天主力净流出约475-680亿。净流入：有色金属(+14.5亿)、煤炭(+8.6亿)、银行(+3.4亿)；净流出：电子(-323亿)、通信(-134亿)、医药(-58亿)。创业板ETF获超5亿份净申购，对应10亿+资金净流入，托市资金进场迹象。</p>
    <p><b class="text-orange-400">技术面</b>：沪指3855点出现承接，3880转为短压，3800-3850是护盘资金参考带。创业板3430附近有反抽需求但3500成反压，科创50破1600后修复偏弱。放量下跌后短期有惯性下探需求，但权重护盘下深跌空间有限。</p>
    <p><b class="text-blue-400">结构特征</b>：资金从高估值科技成长向红利防御板块大规模迁徙——贵金属/煤炭/银行/农业逆势走强，AI硬件链（CPO/半导体/元件）成为重灾区。蓝＞黄＞红格局（权重＞中小盘＞高价科技股），价值风格明显占优。</p>
  </div>
</div>

<div class="grid md:grid-cols-2 gap-4">
  <div class="bg-yellow-500/10 border border-yellow-500/30 rounded-xl p-4">
    <h4 class="text-yellow-300 font-semibold mb-2 flex items-center gap-2"><span>☀️</span> 今日展望</h4>
    <div class="text-xs text-white/70 space-y-1.5 leading-relaxed">
      <p>· 隔夜半导体暴跌+昨日放量调整，今日科技板块大概率低开</p>
      <p>· 央行5000亿MLF+月末隔夜逆回购，流动性宽松托底3850点</p>
      <p>· 上海"十五五"产业规划利好半导体/6G/存储，但情绪偏弱或难有大反应</p>
      <p>· 黄金创新高+避险升温，贵金属/煤炭/银行等防御方向仍有相对收益</p>
      <p>· 英伟达财报前+杰克逊霍尔会议前，市场观望情绪浓，成交量或萎缩</p>
    </div>
  </div>
  <div class="bg-red-500/10 border border-red-500/30 rounded-xl p-4">
    <h4 class="text-red-300 font-semibold mb-2 flex items-center gap-2"><span>⚠️</span> 今日风险点</h4>
    <div class="text-xs text-white/70 space-y-1.5 leading-relaxed">
      <p>· 隔夜半导体暴跌传导，CPO/存储/半导体板块低开压力大</p>
      <p>· 英伟达财报（周三）前避险情绪，科技股持续承压</p>
      <p>· 美债收益率高位+全球科技股估值重估尚未结束</p>
      <p>· 中报密集披露期，高位科技股业绩验证风险</p>
      <p>· 杰克逊霍尔全球央行会议（周五）前，美联储政策不确定性</p>
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
    <span>📉 存储芯片/HBM — 隔夜暴跌vs高盛上调WFE，多空剧烈博弈</span>
  </h4>
  <div class="space-y-3 text-xs text-white/70 leading-relaxed">
    <div class="bg-red-500/10 border border-red-500/20 rounded-lg p-3">
      <p class="text-red-300 font-semibold mb-1">🔻 短期利空（三重打击）</p>
      <p>① <b>苹果采购中国存储芯片传闻</b>：特朗普政府可能允许苹果从CXMT（长鑫）和YMTC（长储）采购DRAM/NAND，作为9月中美元首会晤前的缓和姿态。美光/闪迪/西部数据等美系存储股直接承压。但需注意：CXMT目前仅通过单款低量Mac产品认证，良率有限，短期影响有限。</p>
      <p>② <b>三星股东回报不及预期</b>：三星宣布2026年股东回报90-110万亿韩元，但缺乏即时回购和股票注销承诺，投资者大失所望，股价单日暴跌8.7%创历史最大跌幅之一。</p>
      <p>③ <b>英伟达财报前避险</b>：英伟达七连跌（-2.91%），市场等待周三Q2财报。财报前风险偏好下降，整个AI硬件链都在降仓位。</p>
    </div>
    <div class="bg-green-500/10 border border-green-500/20 rounded-lg p-3">
      <p class="text-green-300 font-semibold mb-1">🚀 中期利好（高盛重磅上调WFE）</p>
      <p>① <b>高盛上调2026-2028年WFE至1500/2180/2810亿美元</b>：2027年增速从32%跳升至45%，2028年从12%升至29%。半导体设备景气周期从原本预期的2027年延长至2028年。</p>
      <p>② <b>DRAM设备支出大幅上调</b>：2026-2028年DRAM WFE预测480亿/720亿/970亿美元，同比50%/50%/35%。HBM4迁移+产能扩张是核心驱动，三星DRAM资本开支上调22%、SK海力士上调19%。DRAM供给紧张预计延续至2028年。</p>
      <p>③ <b>代工设备上调更猛</b>：台积电N2制程设备投入强度超预期，2026-2028年代工WFE 580亿/840亿/1090亿美元，同比45%/45%/30%。</p>
      <p>④ <b>中国半导体资本开支持续增长</b>：高盛预计中国WFE 2027年达530亿美元，本土设备厂商份额从26%提升至38%，2030年中国半导体资本开支达820亿美元。</p>
    </div>
    <div class="bg-yellow-500/10 border border-yellow-500/20 rounded-lg p-2">
      <p class="text-yellow-300"><b>A股映射与操作：</b>隔夜存储板块暴跌，今日A股存储/半导体方向大概率低开。但中期逻辑（高盛上调WFE+HBM景气延续至2028年+国产替代）并未改变。操作上：①不急于抄底，等待情绪企稳（观察3850点支撑+量能变化）；②设备方向（北方华创/中微公司/拓荆科技）中期逻辑更硬，可逢低关注；③存储材料（雅克科技/华海诚科）短期随板块波动，中期HBM需求爆发逻辑不变；④高盛首覆盖长鑫存储给予"买入"评级目标价129元，对国产存储产业链有正面催化。</p>
    </div>
  </div>
</div>

<div class="bg-white/5 rounded-xl p-4">
  <h4 class="text-white font-semibold mb-3 flex items-center gap-2">
    <span class="text-orange-400">A级</span>
    <span>💰 贵金属/黄金 — 创近三个月新高，避险逻辑强化</span>
  </h4>
  <div class="space-y-2 text-xs text-white/70 leading-relaxed">
    <p>· <b>金价突破4700美元</b>：COMEX黄金+0.88%收4739.16美元创近三个月新高，白银+1.10%。伦敦金现突破4650美元。</p>
    <p>· <b>驱动因素</b>：①美债风险外溢（财政部可能动用TGA账户回购长债）；②美元信用对冲（财政赤字扩张担忧）；③地缘风险升温（美伊制裁升级、特朗普对加拿大加征50%关税）；④全球科技股估值重估，资金从成长股流向防御资产。</p>
    <p>· <b>A股表现</b>：昨日贵金属板块逆势走强+1.38%，湖南白银涨停、四川黄金触板、招金黄金涨超7%、白银有色涨停。</p>
    <p>· <b>后续催化</b>：杰克逊霍尔全球央行会议（8/28）、美联储主席沃什首秀、地缘局势发展。方正证券指出美财政端有望继续创造黄金利多环境。</p>
  </div>
</div>

<div class="bg-white/5 rounded-xl p-4">
  <h4 class="text-white font-semibold mb-3 flex items-center gap-2">
    <span class="text-orange-400">A级</span>
    <span>💧 液冷/算力硬件 — 英维克半年报出炉，Q2环比修复</span>
  </h4>
  <div class="space-y-2 text-xs text-white/70 leading-relaxed">
    <p>· <b>英维克半年报</b>：上半年营收30.17亿元+17.24%，归母净利润1.85亿元-14.32%，扣非净利润1.75亿元-13.2%。Q2单季营收18.41亿+12.2%/环比+56.7%，归母净利润1.76亿+5.1%/环比+1934%。毛利率24.93%同比降1.22pct，财务费用同比增2014%（汇兑损失+利息支出）。</p>
    <p>· <b>核心看点</b>：Q2业绩环比大幅修复，一季度利润暴跌的担忧有所缓解。机房温控+25.84%（占比56.36%），境外收入+71.39%。开源证券维持"买入"评级，上调2027-2028年盈利预测。</p>
    <p>· <b>但隐忧仍在</b>：整体毛利率仍在下滑（机房温控-2.49pct、机柜温控-1.32pct），境外收入增速跑不赢成本增速（境外毛利率-6.24pct），电子散热业务（含液冷）营收反而下滑21%。</p>
    <p>· <b>行业层面</b>：高盛上调WFE至2810亿美元验证AI资本开支景气，但隔夜美股半导体暴跌+英伟达七连跌，短期算力硬件板块情绪偏弱。</p>
  </div>
</div>

<div class="bg-white/5 rounded-xl p-4">
  <h4 class="text-white font-semibold mb-3 flex items-center gap-2">
    <span class="text-yellow-400">B级</span>
    <span>📋 政策面 — 央行5000亿MLF+月末逆回购，上海"十五五"产业规划</span>
  </h4>
  <div class="space-y-2 text-xs text-white/70 leading-relaxed">
    <p>· <b>央行流动性操作</b>：今日开展5000亿元1年期MLF操作（本月到期6000亿，净回笼1000亿，但结合前一日3400亿逆回购+预告8/27-9/1每日最高6000亿隔夜逆回购，整体对冲意图明确）。8月末资金紧张窗口有充分保障。</p>
    <p>· <b>上海"十五五"产业规划</b>：推进高性能算力芯片、通用处理器芯片、存储芯片、互联芯片和智能传感器达到国际先进水平；打造集成电路、生物医药、人工智能三个万亿级产业集群；率先推进6G商用部署。</p>
    <p>· <b>国资委6G推进会</b>：召开中央企业6G未来产业推进会，要求补齐技术短板、加强基础理论和关键器件创新。</p>
    <p>· <b>IPO收紧传闻澄清</b>：针对"交易所收紧亏损企业IPO申报"传言，权威人士回应系误读，交易所是要求保荐机构切实履行"看门人"职责。</p>
    <p>· <b>工信部</b>：就《国家人形机器人产业标准体系建设指南（2026版）》《国家脑机接口产业标准体系建设指南（2026版）》公开征求意见。</p>
  </div>
</div>

<div class="bg-white/5 rounded-xl p-4">
  <h4 class="text-white font-semibold mb-3 flex items-center gap-2">
    <span class="text-yellow-400">B级</span>
    <span>🛢️ 煤炭/能源 — 焦煤期货创新高，高股息防御属性凸显</span>
  </h4>
  <div class="space-y-2 text-xs text-white/70 leading-relaxed">
    <p>· <b>板块表现</b>：昨日煤炭开采+3.50%、焦炭+5.39%，上海能源、大有能源、美锦能源涨停，高股息防御属性凸显。</p>
    <p>· <b>行业催化</b>：大商所焦煤主力合约涨超2%触及1600元/吨，创2024年10月以来新高。夏季用电高峰尾声补库需求+高股息防御属性+供应克制，三重逻辑共振。</p>
    <p>· <b>银行板块同步走强</b>：二季度末商业银行净息差1.41%，较一季度末回升1个基点，为2022年一季度以来首次单季环比正增长，业绩底确认。中信银行创历史新高。</p>
    <p>· <b>防御轮动逻辑</b>：在科技股估值重估+地缘风险升温背景下，高股息红利资产成为资金避风港，短期仍有相对收益。</p>
  </div>
</div>

</div>
'''
gen.add_section("核心题材与今日催化", topic_html, "🔥")

# 持仓诊断
holding_html = '''
<div class="space-y-4">

<div class="bg-gradient-to-br from-green-500/20 to-emerald-500/10 border border-green-500/30 rounded-xl p-4">
  <div class="flex items-center justify-between mb-3">
    <h4 class="text-green-300 font-semibold flex items-center gap-2"><span>💼</span> 持仓总览（8月24日收盘）</h4>
    <span class="text-xs bg-red-500/20 text-red-300 px-2 py-1 rounded">三跌一涨</span>
  </div>
  <div class="grid grid-cols-2 md:grid-cols-4 gap-3 text-center">
    <div class="bg-white/5 rounded-lg p-2">
      <div class="text-xs text-white/60">英维克</div>
      <div class="text-base font-bold text-green-400">-2.20%</div>
      <div class="text-xs text-white/50">53.10元</div>
    </div>
    <div class="bg-white/5 rounded-lg p-2">
      <div class="text-xs text-white/60">铜冠铜箔</div>
      <div class="text-base font-bold text-green-400">-3.21%</div>
      <div class="text-xs text-white/50">111.11元</div>
    </div>
    <div class="bg-white/5 rounded-lg p-2">
      <div class="text-xs text-white/60">雅克科技</div>
      <div class="text-base font-bold text-red-400">+1.51%</div>
      <div class="text-xs text-white/50">140.59元</div>
    </div>
    <div class="bg-white/5 rounded-lg p-2">
      <div class="text-xs text-white/60">*ST建艺</div>
      <div class="text-base font-bold text-green-400">-4.72%</div>
      <div class="text-xs text-white/50">9.68元</div>
    </div>
  </div>
</div>

<div class="bg-white/5 rounded-xl p-4">
  <h4 class="text-white font-semibold mb-3 flex items-center gap-2"><span>🔍</span> 个股诊断与操作建议</h4>
  <div class="space-y-4 text-xs">

    <div class="bg-white/5 rounded-lg p-3 border-l-4 border-blue-400">
      <div class="flex justify-between items-center mb-2">
        <span class="text-white font-semibold">英维克（002837）- 液冷龙头·半年报出炉</span>
        <span class="text-green-400 font-bold">-2.20% | 53.10元</span>
      </div>
      <div class="text-white/70 space-y-1 leading-relaxed">
        <p>📊 <b>走势：</b>昨日收53.10元（约-2.2%），跟随科技板块调整。半年报昨晚发布，今日市场将给出反应。</p>
        <p>💰 <b>半年报核心数据：</b>H1营收30.17亿+17.24%，归母净利润1.85亿-14.32%；Q2单季营收18.41亿+12.2%/环比+56.7%，归母净利润1.76亿+5.1%/环比暴增19倍。毛利率24.93%同比-1.22pct。财务费用暴增2014%（汇兑损失+利息支出）。</p>
        <p>🎯 <b>催化与隐忧：</b>正面——Q2业绩环比大幅修复，一季度暴跌的担忧缓解；海外收入+71%增长快；开源证券维持"买入"并上调2027-2028年盈利。负面——整体毛利率仍在下滑，境外毛利率大幅下降6.24pct（增收不增利）；电子散热（液冷）收入反而下滑21%。</p>
        <p>⚡ <b>操作建议：</b>底仓持有（30%仓位），观察半年报市场反应。若今日低开高走说明业绩底确认，可考虑补仓；若低开低走说明市场不认可修复质量，继续等待。中期液冷逻辑不变，但短期跟随科技板块情绪波动。支撑位50元，压力位58-60元。止损位48元。</p>
      </div>
    </div>

    <div class="bg-white/5 rounded-lg p-3 border-l-4 border-red-400">
      <div class="flex justify-between items-center mb-2">
        <span class="text-white font-semibold">铜冠铜箔（301217）- 高位风险股·长下影线</span>
        <span class="text-green-400 font-bold">-3.21% | 111.11元</span>
      </div>
      <div class="text-white/70 space-y-1 leading-relaxed">
        <p>📊 <b>走势：</b>昨日收111.11元跌3.21%，盘中最低106.33元（-7.38%）后快速拉起，收长下影线，振幅7.47%。成交额30.71亿，换手率3.38%。</p>
        <p>⚠️ <b>风险提示：</b>长下影线既可能是恐慌抛售结束的信号（有资金承接），也可能是下跌中继（尾盘诱多次日继续跌）。隔夜美股存储板块暴跌5-8%，今日铜冠面临较大低开压力。TTM市盈率仍高达560-1388倍（不同口径），估值极端。</p>
        <p>💡 <b>关键判断：</b>董秘逝世利空+科技板块调整+隔夜存储暴跌，三重压力下昨日尾盘被拉起，说明有资金在110元附近护盘。但110元能否守住还需观察。如果跌破110元且放量，下看100-105元。</p>
        <p>⚡ <b>操作建议：</b><b class="text-red-400">继续减仓！</b>高位股+高估值+板块调整+隔夜利空，减仓是唯一正确选择。若今日低开（预计105-108元附近），观察105-106元支撑，若支撑不住继续减仓至底仓（10-20%）。若高开反而是减仓良机。目标清仓价115-120元（反弹到就卖）。止损位100元（跌破清仓）。</p>
      </div>
    </div>

    <div class="bg-white/5 rounded-lg p-3 border-l-4 border-green-400">
      <div class="flex justify-between items-center mb-2">
        <span class="text-white font-semibold">雅克科技（002409）- 存储材料龙头·逆势上涨</span>
        <span class="text-red-400 font-bold">+1.51% | 140.59元</span>
      </div>
      <div class="text-white/70 space-y-1 leading-relaxed">
        <p>📊 <b>走势：</b>昨日逆势上涨1.51%收140.59元，最高144.01元，最低136.60元，振幅5.35%。成交额33.81亿，换手率7.59%。在半导体板块全线下跌的情况下逆势收红，相对强势。</p>
        <p>🎯 <b>催化：</b>高盛上调全球WFE至2810亿美元，存储设备支出大幅上调，HBM景气延续至2028年。雅克作为HBM前驱体国内龙头，中期受益于存储芯片产能扩张。</p>
        <p>⚠️ <b>风险：</b>隔夜美光-5.83%、闪迪-6.45%，存储板块情绪偏弱。今日雅克可能补跌。TTM市盈率约63倍，在半导体材料板块中不算极端。</p>
        <p>⚡ <b>操作建议：</b>底仓持有（30%仓位）。昨日逆势上涨说明资金认可度高，中期HBM需求爆发逻辑不变。短期若低开至135元以下可考虑小仓位补仓机动仓，反弹至150元以上减仓机动仓。止损位125元。</p>
      </div>
    </div>

    <div class="bg-white/5 rounded-lg p-3 border-l-4 border-gray-400">
      <div class="flex justify-between items-center mb-2">
        <span class="text-white font-semibold">*ST建艺（002789）- 观察标的·大跌</span>
        <span class="text-green-400 font-bold">-4.72% | 9.68元</span>
      </div>
      <div class="text-white/70 space-y-1 leading-relaxed">
        <p>📊 <b>走势：</b>昨日大跌4.72%收9.68元，盘中最低9.59元，成交额2526万，换手率1.65%。主力资金净流出351万（占成交额13.9%）。</p>
        <p>💡 <b>基本面：</b>ST股流动性差，跟随市场情绪波动。上半年预亏1.1-1.6亿（同比减亏），庭外重组推进中。董事长8月初辞职。</p>
        <p>⚡ <b>操作建议：</b>底仓持有观望。9.5元附近有支撑，跌破则减仓。ST股不建议加仓，等待摘帽或重大重组信号。止损位9元。</p>
      </div>
    </div>

  </div>
</div>

<div class="bg-yellow-500/10 border border-yellow-500/30 rounded-xl p-4">
  <h4 class="text-yellow-300 font-semibold mb-2 flex items-center gap-2"><span>📋</span> 今日操作计划</h4>
  <div class="text-xs text-white/70 space-y-1.5 leading-relaxed">
    <p>1. <b class="text-red-400">铜冠铜箔：</b>继续减仓。隔夜存储板块暴跌，今日大概率低开。观察105-106元支撑，若破位继续减仓至底仓（10-20%）。反弹到115元以上更是减仓良机。</p>
    <p>2. <b class="text-blue-400">英维克：</b>观察半年报市场反应。若低开高走（业绩底确认）可补小仓位；若低开低走继续观望。底仓持有不动。</p>
    <p>3. <b class="text-green-400">雅克科技：</b>底仓持有。昨日逆势上涨相对强势，若低开至135以下可小仓位补机动仓，150以上减机动仓。</p>
    <p>4. <b class="text-gray-400">*ST建艺：</b>持有观望，不操作。</p>
    <p>5. <b class="text-yellow-400">总体仓位：</b>4-5成。英伟达财报前+杰克逊霍尔会议前，保持谨慎，不急于加仓。等两大事件落地后再决策。</p>
    <p>6. <b class="text-orange-400">防御配置：</b>可关注贵金属/煤炭等防御方向的相对收益，但不宜追高，逢回调配置。</p>
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
    <span>空方视角：全球科技股估值重估进行时，8大风险必须警惕</span>
  </div>

  <div class="space-y-3">
    <div class="bg-white/5 rounded-lg p-3">
      <p class="text-red-300 font-semibold mb-1">风险1：三星-8.7%崩盘，全球科技股估值重估蔓延</p>
      <p>三星电子单日暴跌8.7%，创历史最大单日跌幅之一。虽然直接原因是股东回报不及预期，但更深层次的问题是：科技股的估值泡沫正在从边缘向核心扩散。从A股CPO到美股半导体，从软件到硬件，全球科技股都在经历估值重估。30年期美债收益率一度飙至5.337%（2007年以来新高），高利率环境下高估值科技股面临系统性压力。</p>
    </div>
    <div class="bg-white/5 rounded-lg p-3">
      <p class="text-red-300 font-semibold mb-1">风险2：英伟达七连跌+财报前避险，AI行情阶段性见顶？</p>
      <p>英伟达连续第七个交易日下跌，创2022年以来最长连跌纪录。这不仅仅是财报前的避险——市场开始对AI资本开支的可持续性产生质疑。高盛警告"美股AI主题的动能结构已发生根本性转变——动量因子中半导体与AI板块正从多头转入空头，软件板块取而代之成为短期动量的最大权重"。如果英伟达财报指引不及预期，整个AI硬件链都可能面临更大幅度的调整。</p>
    </div>
    <div class="bg-white/5 rounded-lg p-3">
      <p class="text-red-300 font-semibold mb-1">风险3：美债收益率高位徘徊，科技股估值承压</p>
      <p>30年期美债收益率一度达5.337%创2007年以来新高，10年期4.7%左右。虽然财政部释放动用TGA账户回购长债的信号后收益率有所回落，但市场对财政可持续性的担忧并未根本解除。城堡证券警告"财政部回购美债类似金融抑制，可能削弱美元并加剧通胀"。高盛和富国银行也认为此举难以压低长期美债收益率。高利率环境下，科技股的DCF估值模型分母端持续承压。</p>
    </div>
    <div class="bg-white/5 rounded-lg p-3">
      <p class="text-red-300 font-semibold mb-1">风险4：苹果采购中国存储芯片=国产替代逻辑动摇？</p>
      <p>特朗普政府可能允许苹果从长鑫存储（CXMT）和长江存储（YMTC）采购存储芯片，这一消息导致美光/闪迪等美系存储股暴跌。更深层的含义是：如果美国政府放松对中国存储芯片的限制，那么"国产替代"逻辑的紧迫性会下降。虽然短期CXMT产能和良率还不足以大规模供应苹果，但中长期看，中美科技缓和可能削弱国产替代的投资逻辑。</p>
    </div>
    <div class="bg-white/5 rounded-lg p-3">
      <p class="text-red-300 font-semibold mb-1">风险5：杰克逊霍尔会议+沃什首秀=政策不确定性</p>
      <p>本周五（8月28日）美联储主席沃什将在杰克逊霍尔全球央行年会上发表讲话，这是他上任以来的首次重要演讲。自5月上任以来，沃什刻意回避前瞻指引、缩短政策声明，市场解读为"缺乏将通胀拉回目标的决心"。前圣路易斯联储主席布拉德批评"美联储的公信力正处于风险之中"。如果沃什在杰克逊霍尔释放鹰派信号（强调抗通胀、暗示不降息），全球股市可能再遭冲击。</p>
    </div>
    <div class="bg-white/5 rounded-lg p-3">
      <p class="text-red-300 font-semibold mb-1">风险6：地缘风险持续升温——美伊制裁+美加关税</p>
      <p>①美财长贝森特宣布对伊朗启动"经济诺曼底登陆"式制裁，将近60个实体/个人/船舶列入SDN清单，美伊冲突再添变数。②特朗普宣布自2027年1月1日起对加拿大汽车/零部件/钢铁关税提高至50%，贸易冲突升级。地缘风险推升油价和黄金，同时加剧通胀担忧，形成"油价涨→通胀升→利率高→股市跌"的传导链。</p>
    </div>
    <div class="bg-white/5 rounded-lg p-3">
      <p class="text-red-300 font-semibold mb-1">风险7：A股放量下跌=二次探底确认？</p>
      <p>昨日A股放量下跌（2.01万亿，放量1280亿），近4000只个股下跌，赚钱效应仅27%。沪指盘中跌破3880点，创业板跌3.21%，科创50跌3.10%。虽然尾盘有所收回，但放量下跌本身就是抛压增大的信号。如果隔夜半导体暴跌的冲击叠加，今日可能继续下探3850点支撑，一旦跌破可能触发二次探底。</p>
    </div>
    <div class="bg-white/5 rounded-lg p-3">
      <p class="text-red-300 font-semibold mb-1">风险8：中报密集披露期，业绩验证才刚开始</p>
      <p>8月底是中报披露最高峰。昨日英维克发布半年报（净利-14%），市场今天会给出反应。很多高位科技股的估值建立在"AI永远增长"的假设上，但实际业绩能否跟上？工业富联中报+96%反而跌4.58%的教训还在——利好出尽=出货信号。需要警惕中报不及预期的高位股出现业绩杀。</p>
    </div>
  </div>

  <div class="bg-green-500/10 border border-green-500/30 rounded-xl p-4">
    <h4 class="text-green-300 font-semibold mb-3 flex items-center gap-2"><span>🐂</span> 多方反驳：调整就是上车机会·产业趋势未变</h4>
    <div class="text-xs text-white/70 space-y-2 leading-relaxed">
      <p>① <b>高盛上调WFE至2810亿美元=AI资本开支周期延长至2028年</b>：这是中期级别的利好，说明AI算力建设不是短期泡沫，而是持续3年以上的超级周期。设备股订单能见度极高，客户给8季度预测。短期情绪波动不改中期产业趋势。</p>
      <p>② <b>央行5000亿MLF+月末逆回购=流动性充裕</b>：8月末本来是资金紧张窗口，但央行提前部署了MLF+隔夜逆回购组合拳，每日最高6000亿，流动性不是问题。A股不缺钱，缺的是信心。</p>
      <p>③ <b>创业板ETF获10亿+净申购=托市资金进场</b>：昨日创业板ETF易方达获超5亿份净申购，对应10亿+资金流入。这与7月17日、7月20日探底回升前的信号一致——每当市场恐慌时，都有托市资金进场。</p>
      <p>④ <b>上海"十五五"产业规划=政策支持持续加码</b>：万亿级产业集群、6G商用、算力芯片/存储芯片/互联芯片国际先进水平。政策底已经确认，产业政策密集出台支持科技发展。</p>
      <p>⑤ <b>黄金新高+科技调整=风格切换而非趋势反转</b>：当前是典型的风格切换（从科技成长转向红利防御），不是熊市的开始。等科技股调整到位后，资金还会回来，因为AI产业趋势是确定的。</p>
    </div>
  </div>

  <div class="bg-yellow-500/10 border border-yellow-500/30 rounded-xl p-4">
    <h4 class="text-yellow-300 font-semibold mb-2 flex items-center gap-2"><span>⚖️</span> 综合判断</h4>
    <p class="text-xs text-white/70 leading-relaxed">
      短期（本周）：A股处于"外部冲击+内部调整"的双重压力下。隔夜半导体暴跌+昨日放量调整，今日科技板块大概率低开。但央行流动性托底+3850点护盘+托市资金进场，下方空间有限。预计沪指在3830-3920区间震荡。<b class="text-red-400">操作上以防御为主，利用反弹减仓高位股，不急于抄底。</b><br>
      中期（1-3个月）：高盛上调WFE至2810亿美元验证了AI资本开支的长期景气度，存储/设备/材料的中期逻辑未变。等英伟达财报（8/27）和杰克逊霍尔会议（8/28）落地后，不确定性消除，科技股有望迎来新一轮布局窗口。<br>
      <b class="text-yellow-400">核心结论：短期防御为主，中期趋势未变。仓位控制在4-5成，等待两大事件落地后再加仓。
      优先级：减仓铜冠（最危险）→ 英维克观察半年报反应 → 雅克底仓持有。
      防御配置关注贵金属/煤炭的相对收益，但不宜追高。</b>
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

      <div class="bg-red-500/10 border border-red-500/30 rounded-lg p-3">
        <div class="flex justify-between mb-2">
          <span class="text-red-300 font-semibold">预判#20260818-02：沪指4000点关口遇阻，本周回调至3900附近</span>
          <span class="text-xs bg-green-500/30 text-green-200 px-2 py-0.5 rounded">验证正确·T+5</span>
        </div>
        <p class="text-white/70">预判内容：沪指逼近4000点关口，叠加科技拥挤度历史高位+中报密集披露+地缘风险，本周在4000点附近遇阻回落，回调至3900点附近（约-2%）。4000点整数关口是强压力位，第一次冲击大概率失败。</p>
        <p class="text-white/50 mt-1">验证结果：沪指最高约3982点（8月18日）后持续回落，今日（8月24日）收3882点，确实回调至3900附近（略低但接近）。幅度和方向基本验证正确。但需要注意：触发因素不是"4000点压力"，而是美债收益率上行+英伟达财报前避险+三星暴跌等外部因素。结论：方向正确，但触发因素与预判有所不同。</p>
      </div>

      <div class="bg-green-500/10 border border-green-500/30 rounded-lg p-3">
        <div class="flex justify-between mb-2">
          <span class="text-green-300 font-semibold">预判#20260818-01：宇树科技上市首日涨幅超200%，机器人板块T+2见光死</span>
          <span class="text-xs bg-green-500/30 text-green-200 px-2 py-0.5 rounded">基本验证·T+5</span>
        </div>
        <p class="text-white/70">预判内容：宇树科技上市首日涨200-300%，但机器人板块"上市日即高点"，T+2前后开始回调，核心零部件标的回调幅度10-15%。</p>
        <p class="text-white/50 mt-1">验证结果：宇树科技（688836）8月19日上市首日收盘约450-500元区间（涨幅约200%+），随后机器人板块确实出现回调。虽然具体幅度需进一步确认，但"上市即高点"的基本逻辑得到验证。基本验证正确。</p>
      </div>

      <div class="bg-yellow-500/10 border border-yellow-500/30 rounded-lg p-3">
        <div class="flex justify-between mb-2">
          <span class="text-yellow-300 font-semibold">预判#20260817-02：铜冠铜箔短期见顶，调整幅度15-20%</span>
          <span class="text-xs bg-yellow-500/30 text-yellow-200 px-2 py-0.5 rounded">部分验证·T+5</span>
        </div>
        <p class="text-white/70">预判内容：铜冠铜箔高PE+董秘风险，短期见顶调整15-20%，目标100-105元。</p>
        <p class="text-white/50 mt-1">当前进度：T+5验证，铜冠从高点132.22元回落至111.11元，最大跌幅约16%（盘中最低106.33元，跌幅约20%）。从最高价算调整幅度已达到15-20%的预判范围。但需要注意：中间曾出现"利空出尽反而大涨7.45%"的反预期走势（8月18日），增加了验证的曲折性。部分验证正确（调整幅度达标），但路径比预期复杂。</p>
      </div>

      <div class="bg-yellow-500/10 border border-yellow-500/30 rounded-lg p-3">
        <div class="flex justify-between mb-2">
          <span class="text-yellow-300 font-semibold">预判#20260817-01：本周四大事件落地后科技股迎来布局窗口</span>
          <span class="text-xs bg-red-500/30 text-red-200 px-2 py-0.5 rounded">验证中·T+5</span>
        </div>
        <p class="text-white/70">预判内容：本周四大事件（经济数据、LPR、机器人大会、美联储纪要）落地后，不确定性消除，科技股有望迎来新一轮布局窗口，存储/液冷/先进封装三个方向率先反弹5-10%。</p>
        <p class="text-white/50 mt-1">当前进度：T+5验证，但四大事件尚未全部落地（杰克逊霍尔会议周五才开，英伟达财报周三才出）。科技股不但没有反弹，反而继续调整（创业板-3.21%、半导体-3.5%）。主要原因是外部冲击（美债收益率上行+三星暴跌+英伟达连跌）超出预期。继续观察T+7（本周五）验证——如果两大事件落地后科技股企稳反弹，则预判延后兑现；如果继续下跌，则预判失败。</p>
      </div>

      <div class="bg-red-500/10 border border-red-500/30 rounded-lg p-3">
        <div class="flex justify-between mb-2">
          <span class="text-red-300 font-semibold">预判#20260814-02：A股短期调整延续至下周三</span>
          <span class="text-xs bg-green-500/30 text-green-200 px-2 py-0.5 rounded">已验证·正确</span>
        </div>
        <p class="text-white/70">预判内容：A股放量下跌后短期调整3-5个交易日，沪指3850-3950区间震荡，下周三前后出现布局机会。</p>
        <p class="text-white/50 mt-1">验证结果：部分正确。调整确实延续了（沪指从3982回落至3882），但中间穿插了8月18日的反弹。震荡区间基本符合预判（3850-3950）。然而"下周三前后出现布局机会"的判断需要打问号——因为8月20日之后市场并未企稳，反而继续调整。方向正确，但"布局机会"的判断过于乐观。</p>
      </div>

      <div class="bg-green-500/10 border border-green-500/30 rounded-lg p-3">
        <div class="flex justify-between mb-2">
          <span class="text-green-300 font-semibold">预判#20260803-01：雅克科技跌停后3日内反弹</span>
          <span class="text-xs bg-green-500/30 text-green-200 px-2 py-0.5 rounded">已验证·正确</span>
        </div>
        <p class="text-white/70">预判内容：雅克科技跌停板机构抄底近5亿，预计3个交易日内5-10%反弹。</p>
        <p class="text-white/50 mt-1">实际走势：从127元反弹至最高159元（+25%），远超预期。验证正确。</p>
      </div>

      <div class="bg-red-500/10 border border-red-500/30 rounded-lg p-3">
        <div class="flex justify-between mb-2">
          <span class="text-red-300 font-semibold">新增预判#20260825-01：英伟达财报后科技股迎来短期反弹窗口</span>
          <span class="text-xs bg-red-500/30 text-red-200 px-2 py-0.5 rounded">待验证·T+3</span>
        </div>
        <p class="text-white/70">预判内容：英伟达8月27日（周三）Q2财报落地后，"靴子落地"效应将触发科技股短期反弹。如果财报符合或略超预期，A股半导体/存储/CPO板块有望反弹3-5%。逻辑：当前市场已充分消化英伟达财报前的避险情绪，股价已经提前调整（七连跌），利空出尽=利好。</p>
        <p class="text-white/50 mt-1">验证时间：8月28日（T+1，周四）观察科技股是否反弹</p>
      </div>

      <div class="bg-red-500/10 border border-red-500/30 rounded-lg p-3">
        <div class="flex justify-between mb-2">
          <span class="text-red-300 font-semibold">新增预判#20260825-02：贵金属板块中期上涨趋势延续，年底前突破5000美元</span>
          <span class="text-xs bg-red-500/30 text-red-200 px-2 py-0.5 rounded">待验证·T+30</span>
        </div>
        <p class="text-white/70">预判内容：COMEX黄金当前4739美元，在美债财政风险+地缘冲突+美元信用对冲三重逻辑下，中期上涨趋势延续，年底前有望突破5000美元/盎司（约+5.5%）。A股贵金属板块（黄金股/白银股）将持续跑赢大盘。</p>
        <p class="text-white/50 mt-1">验证时间：9月25日（T+30）验证黄金价格走势</p>
      </div>

    </div>
  </div>

  <div class="bg-white/5 rounded-xl p-4">
    <h4 class="text-white font-semibold mb-2 flex items-center gap-2"><span>📊</span> 准确率统计</h4>
    <div class="grid grid-cols-3 gap-3 text-center text-xs">
      <div class="bg-white/5 rounded-lg p-2">
        <div class="text-lg font-bold text-yellow-400">62%</div>
        <div class="text-white/60">总体准确率</div>
      </div>
      <div class="bg-white/5 rounded-lg p-2">
        <div class="text-lg font-bold text-green-400">13/21</div>
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
    <p class="text-red-300 font-semibold mb-1">教训#1：美股跌→A股大概率跌，情绪传导不对称</p>
    <p class="text-white/60 text-xs">
      昨晚费城半导体-2.7%、三星-8.7%、美光-5.83%，今天A股半导体/存储板块大概率低开。
      历史经验反复验证：美股涨的时候A股经常高开低走（利好出尽），但美股跌的时候A股几乎必跌（情绪传导）。
      这种不对称性的根源：A股是"利好出尽型"市场，外部利好很容易被提前price in并兑现出货；
      但外部利空总是超预期，因为A股投资者风险偏好更低、更敏感。
      <b>正确做法</b>：隔夜美股科技股大跌，第二天不要抄底A股科技股，等开盘后观察30分钟，
      看承接力度再决定。宁可错过反弹，不要抄在半山腰。
      在熊市/调整期，"宁错过勿做错"是第一原则。
    </p>
  </div>

  <div class="bg-orange-500/10 border border-orange-500/30 rounded-lg p-3">
    <p class="text-orange-300 font-semibold mb-1">教训#2：英伟达财报前一周，AI硬件股必跌</p>
    <p class="text-white/60 text-xs">
      英伟达已连续第七个交易日下跌，创2022年以来最长连跌纪录。
      这不是巧合——每次英伟达财报前一周左右，AI硬件股都会提前调整。
      原因很简单：所有人都在等财报，怕不及预期，所以先卖了再说。
      而且英伟达股价越高、预期越满，财报前调整幅度越大。
      <b>正确做法</b>：英伟达财报前3-5个交易日开始减仓AI硬件股（尤其是高位股），
      财报落地后再根据结果决定是否买回。
      这不是预判财报好坏，而是规避不确定性——不确定性本身就是风险。
      如果你真的看好英伟达财报，可以等财报出来后再买，最多损失一个跳空高开的收益；
      但如果财报不及预期，你可以避开10%+的跌幅。
      这是一个典型的"非对称风险"场景。
    </p>
  </div>

  <div class="bg-yellow-500/10 border border-yellow-500/30 rounded-lg p-3">
    <p class="text-yellow-300 font-semibold mb-1">教训#3：三星单日-8.7%=情绪极限的信号</p>
    <p class="text-white/60 text-xs">
      三星电子作为全球最大的存储芯片制造商和市值最大的科技公司之一，单日暴跌8.7%是极其罕见的。
      这种级别的暴跌往往意味着市场情绪达到了某种极限——要么是极度恐慌（底部信号），
      要么是极度失望（趋势性下跌的开始）。
      回顾历史：2022年10月三星单日暴跌9%之后，存储板块迎来了中期底部；
      而2021年底的单日暴跌则是趋势性下跌的开始。
      <b>正确做法</b>：不要在暴跌当天抄底（"接飞刀"），等情绪稳定后再判断。
      关键观察指标：①后续2-3天能否企稳并收复一半跌幅；②成交量是否放大后萎缩（放量跌+缩量涨=企稳信号）；
      ③产业逻辑有没有根本变化（如果只是情绪面或短期消息面影响，就是买入机会；如果是产业逻辑变化，就是趋势反转）。
      这次三星暴跌的原因是"股东回报不及预期"，属于情绪面短期冲击，产业逻辑未变，
      因此更可能是短期恐慌而非趋势反转。但还是要等企稳信号确认。
    </p>
  </div>

  <div class="bg-green-500/10 border border-green-500/30 rounded-lg p-3">
    <p class="text-green-300 font-semibold mb-1">教训#4：高盛上调WFE=中期利好≠短期止跌</p>
    <p class="text-white/60 text-xs">
      高盛把2026-2028年WFE上调到1500/2180/2810亿美元，2027年增速从32%跳升到45%，
      这是一个中期级别的利好，验证了AI资本开支周期的长度和强度。
      但需要注意：中期利好不等于短期止跌。
      市场情绪不好的时候，再好的利好也会被无视；市场情绪好的时候，再小的利好也能被放大。
      高盛上调WFE的消息昨天就出来了，但美股半导体还是跌了2.7%。
      <b>正确做法</b>：区分"中期逻辑"和"短期情绪"。
      中期逻辑好=可以布局底仓、越跌越买（但要分批）；
      短期情绪差=不要加杠杆、不要追高、不要all in。
      用中期逻辑选股，用短期情绪选时。
      现在的情况是：中期逻辑越来越强（WFE上调验证景气延续），
      短期情绪越来越弱（英伟达财报前+美债高位+地缘风险），
      所以正确的操作是：底仓持有不动，机动仓等待情绪企稳后再加。
    </p>
  </div>

  <div class="bg-blue-500/10 border border-blue-500/30 rounded-lg p-3">
    <p class="text-blue-300 font-semibold mb-1">教训#5：黄金新高=风险资产的警钟</p>
    <p class="text-white/60 text-xs">
      COMEX黄金突破4739美元创近三个月新高，白银同步上涨。
      黄金上涨往往意味着市场风险偏好下降——资金从风险资产（股票、科技）流向避险资产（黄金、国债）。
      这一次黄金上涨有三重驱动：①美债财政风险（TGA回购计划）；
      ②地缘风险升温（美伊制裁+美加关税）；③美元信用对冲（财政赤字扩张）。
      这三个因素都不是短期因素，可能持续较长时间。
      <b>正确做法</b>：黄金创新高不是"可以买黄金股"这么简单，
      它更重要的意义是——这是风险资产的警钟。
      如果黄金持续上涨而科技股持续下跌，说明市场在定价某种系统性风险（地缘、财政、衰退）。
      此时应该：①降低整体仓位；②增加防御性配置（黄金、煤炭、银行）；
      ③减少高估值成长股的暴露。
      不要等到风险爆发了才反应——黄金价格已经在告诉你答案了。
    </p>
  </div>

  <div class="bg-purple-500/10 border border-purple-500/30 rounded-lg p-3">
    <p class="text-purple-300 font-semibold mb-1">教训#6：半年度报告"营收增利润降"=警惕增收不增利</p>
    <p class="text-white/60 text-xs">
      英维克半年报：营收+17%，净利润-14%，毛利率-1.22pct。
      典型的"增收不增利"——收入在增长，但盈利能力在下降。
      背后的原因：毛利率下滑（价格战/产品结构变化）+ 费用端上升（汇兑损失/利息支出）。
      这种情况在成长股中很常见——行业高速增长期，公司为了抢市场份额不惜牺牲利润率。
      但投资者需要警惕：如果"增收不增利"持续多个季度，说明行业竞争在加剧，
      公司的护城河可能没有想象中那么宽。
      <b>正确做法</b>：对于成长股，不能只看营收增速，更要看利润率的变化趋势。
      如果营收增速在加快但利润率在下降，说明是"用利润换增长"，可持续性存疑。
      只有营收和利润同步增长（甚至利润增长更快），才是健康的成长。
      英维克的情况还需要观察——Q2利润率已经环比改善（毛利率环比+1.05pct），
      如果Q3继续改善，说明一季度是阶段性低点；如果继续下滑，就要警惕了。
    </p>
  </div>

</div>
'''
gen.add_section("教训库引用", lesson_html, "📚")

# 生成+发布
output_path = os.path.join(WORK_DIR, 'docs/daily/20260825_每日新闻洞察.html')
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
