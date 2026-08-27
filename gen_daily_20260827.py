#!/usr/bin/env python3
"""2026年8月27日 每日新闻洞察生成 - 周四"""
import sys, os, shutil, json
WORK_DIR = '/root/daily-news-insight'
sys.path.insert(0, os.path.join(WORK_DIR, 'v3'))
from generators.daily_pro import DailyReportProGenerator

gen = DailyReportProGenerator(
    date_str='2026年8月27日', weekday='星期四',
    subtitle='2026年8月27日 周四 · 英伟达Q2超预期盘后涨4%+2028财年指引+70%·Vera Rubin量产·铜冠铜箔半年报+514%·十五五新型工业化',
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
        '英伟达Q2财报全面超预期：营收962亿美元（+106%）超预期924亿，数据中心890亿（+117%），盘后大涨超4%；首次提前一年给指引：2028财年营收+70%，云服务未完成订单超2万亿美元',
        'Vera Rubin全面量产：英伟达CEO黄仁勋宣布Vera Rubin已全面投入生产，获所有主要云厂商订单，预计Q3占数据中心收入约20%，将成为史上最快量产产品；GPU单价从Hopper 180亿/吉瓦→Blackwell 250亿→Vera Rubin 400亿',
        '存储供应瓶颈加剧：英伟达CFO警告内存价格"极端高企"，超出此前预期且明年更高，供应承诺金额从1190亿增至2790亿美元；美光+0.58%、西部数据+4%、闪迪+1%，存储芯片板块涨多跌少',
        'A股昨日缩量收红：沪指+0.59%收3912点（站上3900），深成指+0.69%，创业板+0.51%，科创50+1.71%领涨；两市成交1.81万亿缩量230亿，券商半年报爆发驱动大金融领涨，有色/绿电/核聚变走强',
        '今日三大焦点：①英伟达超预期财报催化AI算力链反弹（关注半导体设备/光模块/存储）；②铜冠铜箔半年报+514%但Q2环比仅+2%，产能天花板隐忧；③十五五新型工业化政策落地，集成电路/低空经济/机器人/6G等新兴产业加速'
    ],
    operation_advice='周四开盘：英伟达Q2财报全面超预期+Vera Rubin量产催化，AI算力链有望迎来反弹。但昨日A股缩量上涨、量能不足1.9万亿，且PCE通胀高于预期引发美联储加息担忧，反弹高度存疑。操作策略：①持仓股英维克关注63-65元压力位，铜冠铜箔半年报利好出尽注意短期回调风险，雅克科技中报稳健可持有；②英伟达超预期利好半导体设备/光模块/HBM材料链，但高开不追高，观察量能；③大金融/贵金属等防御方向已有获利可部分止盈；④仓位控制在5-6成，重点关注AI算力链反弹持续性',
    risk_level='中等偏高',
    suggested_position='5-6成'
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
    description='每日新闻洞察 2026年8月27日：英伟达Q2超预期盘后涨4%、Vera Rubin全面量产、2028财年指引+70%、铜冠铜箔半年报+514%、十五五新型工业化',
)

gen.add_global_market()

global_cards1 = render_cards([
    {"name":"道琼斯","change":"-0.21%","up":False},
    {"name":"标普500","change":"-0.02%","up":False},
    {"name":"纳斯达克","change":"-0.08%","up":False},
    {"name":"费城半导体","change":"+0.20%","up":True},
    {"name":"日经225","change":"-0.90%","up":False},
    {"name":"恒生指数","change":"+0.56%","up":True},
])
global_list1 = render_list([
    {"name":"WTI原油","change":"-0.75%/$81.61","up":False},
    {"name":"布伦特原油","change":"-0.68%/$86.35","up":False},
    {"name":"COMEX黄金","change":"+0.45%/$4674.10","up":True},
    {"name":"COMEX白银","change":"+1.08%/$69.56","up":True},
])
global_list2 = render_list([
    {"name":"三星电子","change":"+1.75%","up":True},
    {"name":"SK海力士","change":"+0.60%","up":True},
    {"name":"美光科技","change":"+0.58%","up":True},
    {"name":"台积电ADR","change":"+0.07%","up":True},
])
global_list3 = render_list([
    {"name":"英伟达","change":"-1.59%/$209.66(盘后+4%+)","up":False},
    {"name":"AMD","change":"+0.37%/$480.93","up":True},
    {"name":"微软","change":"+0.95%/$496.37","up":True},
    {"name":"苹果","change":"+1.15%/$313.45","up":True},
    {"name":"博通","change":"-0.32%/$355.59","up":False},
    {"name":"英特尔","change":"+0.87%/$88.24","up":True},
    {"name":"应用材料","change":"-0.06%/$479.76","up":False},
    {"name":"阿斯麦","change":"+0.08%/$1745.64","up":True},
])

global_html = '''
<div class="grid md:grid-cols-3 gap-4">
  <div class="md:col-span-2">
    <div class="text-white font-semibold mb-3 flex items-center gap-2"><span>🌍</span><span>隔夜全球市场 · 英伟达财报超预期盘后暴涨·Vera Rubin全面量产·存储供应瓶颈加剧</span></div>
    <div class="grid grid-cols-3 md:grid-cols-6 gap-2">{0}</div>
    <p class="text-xs text-white/50 mt-3 leading-relaxed">
      ⚡ <b class="text-yellow-400">核心要点：美股三大指数小幅收跌，道指-0.21%、纳指-0.08%、标普-0.02%。但盘后英伟达财报全面超预期，股价盘后大涨超4%。费半+0.20%收11611点，存储芯片板块涨多跌少（西部数据+4%、美光+0.58%）。光通信板块走强（Lumentum+6%、康宁+3%）。黄金+0.45%、白银+1.08%。</b>——<br>
      ①<b>英伟达Q2财报全面超预期</b>：<br>
      ·营收962亿美元，同比+106%，环比+18%，市场预期924亿；净利润597亿美元，同比+126%<br>
      ·数据中心收入890亿美元（+117%），超大规模客户487亿、AI云/工业/企业403亿<br>
      ·Q3指引营收1080亿美元（±2%），远超市场预期；毛利率预计74%<br>
      ·首次提前一年指引：2028财年营收增长约70%，云服务未完成订单超2万亿美元<br>
      ②<b>Vera Rubin全面量产，AI算力进入新阶段</b>：<br>
      ·黄仁勋宣布Vera Rubin已全面投入生产，获所有主要云厂商和AI实验室订单<br>
      ·预计Q3占数据中心收入约20%，将成为英伟达史上最快量产产品<br>
      ·GPU价值量跃升：Hopper 180亿美元/吉瓦→Blackwell 250亿→Vera Rubin 400亿<br>
      ·AWS宣布将部署200万个英伟达GPU（从当前季度至2029财年）<br>
      ③<b>存储供应瓶颈加剧，价格持续上涨逻辑强化</b>：<br>
      ·英伟达CFO警告内存价格"极端高企"，超出此前预期且2027年价格还会更高<br>
      ·供应承诺金额从1190亿美元增至2790亿美元，主要与存储器采购有关<br>
      ·预计Q4毛利率触底（71-72%），2028财年稳定在72-73%<br>
      ·"需求增长大于70%，供应限制导致可交付订单增长70%"——黄仁勋<br>
      ④<b>PCE通胀略超预期，美联储加息担忧升温</b>：<br>
      ·7月PCE物价指数环比+0.2%（预期+0.1%），同比3.7%；核心PCE环比+0.2%、同比3.3%<br>
      ·通胀黏性增强，杰克逊霍尔年会前市场观望情绪浓，美元指数+0.25%<br>
      ⑤<b>光通信板块走强</b>：Lumentum+6.3%、康宁+3.2%、Coherent+2.5%，AI算力光互联需求持续验证。
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
    <div class="text-xl font-bold text-red-400">3912.52</div>
    <div class="text-xs text-red-400">+0.59%</div>
  </div>
  <div class="bg-gradient-to-br from-red-500/20 to-orange-500/10 border border-red-500/30 rounded-xl p-3 text-center">
    <div class="text-xs text-white/60 mb-1">深证成指</div>
    <div class="text-xl font-bold text-red-400">13841.33</div>
    <div class="text-xs text-red-400">+0.69%</div>
  </div>
  <div class="bg-gradient-to-br from-red-500/20 to-orange-500/10 border border-red-500/30 rounded-xl p-3 text-center">
    <div class="text-xs text-white/60 mb-1">创业板指</div>
    <div class="text-xl font-bold text-red-400">3414.88</div>
    <div class="text-xs text-red-400">+0.51%</div>
  </div>
  <div class="bg-gradient-to-br from-red-500/20 to-orange-500/10 border border-red-500/30 rounded-xl p-3 text-center">
    <div class="text-xs text-white/60 mb-1">科创50</div>
    <div class="text-xl font-bold text-red-400">1632.02</div>
    <div class="text-xs text-red-400">+1.71%</div>
  </div>
</div>

<div class="grid md:grid-cols-2 gap-4">
  <div class="bg-white/5 rounded-xl p-4">
    <h4 class="text-white font-semibold mb-3 flex items-center gap-2"><span>📈</span> 领涨板块</h4>
    <div class="space-y-1 text-xs">
      <div class="flex justify-between"><span class="text-white/70">证券/大金融</span><span class="text-red-400 font-semibold">+49.2亿净流入</span></div>
      <div class="flex justify-between"><span class="text-white/70">消费电子</span><span class="text-red-400 font-semibold">+19.3亿净流入</span></div>
      <div class="flex justify-between"><span class="text-white/70">黄金/有色</span><span class="text-red-400 font-semibold">+14.5亿净流入</span></div>
      <div class="flex justify-between"><span class="text-white/70">绿电/电网设备</span><span class="text-red-400 font-semibold">+13.4亿净流入</span></div>
      <div class="flex justify-between"><span class="text-white/70">可控核聚变</span><span class="text-red-400 font-semibold">概念活跃</span></div>
      <div class="flex justify-between"><span class="text-white/70">科创50</span><span class="text-red-400 font-semibold">+1.71%</span></div>
    </div>
  </div>
  <div class="bg-white/5 rounded-xl p-4">
    <h4 class="text-white font-semibold mb-3 flex items-center gap-2"><span>📉</span> 领跌/资金流出板块</h4>
    <div class="space-y-1 text-xs">
      <div class="flex justify-between"><span class="text-white/70">通信设备</span><span class="text-green-400 font-semibold">-16.8亿净流出</span></div>
      <div class="flex justify-between"><span class="text-white/70">半导体</span><span class="text-green-400 font-semibold">-8.9亿净流出</span></div>
      <div class="flex justify-between"><span class="text-white/70">贵金属(获利回吐)</span><span class="text-green-400 font-semibold">-13.9亿净流出</span></div>
      <div class="flex justify-between"><span class="text-white/70">医疗服务/CRO</span><span class="text-green-400 font-semibold">领跌</span></div>
      <div class="flex justify-between"><span class="text-white/70">航运港口</span><span class="text-green-400 font-semibold">-11.2亿净流出</span></div>
      <div class="flex justify-between"><span class="text-white/70">地面兵装</span><span class="text-green-400 font-semibold">领跌</span></div>
    </div>
  </div>
</div>

<div class="bg-white/5 rounded-xl p-4">
  <h4 class="text-white font-semibold mb-3 flex items-center gap-2"><span>📊</span> 市场概况与解读</h4>
  <div class="text-xs text-white/70 space-y-2 leading-relaxed">
    <p><b class="text-white">成交额1.81万亿</b>：较昨日缩量约230亿元，沪市约8200亿、深市约9900亿。全市场上涨2900+只、下跌2200+只，涨跌比约1.3:1，赚钱效应中等。涨停50+家、跌停家数较少。</p>
    <p><b class="text-yellow-400">券商半年报爆发驱动大金融</b>：21家券商半年报营收2071亿、净利888亿，同比+53%，证券板块领涨两市，主力资金净流入49.2亿。江西铜业半年报净利+106.77%带动有色板块。</p>
    <p><b class="text-white">政策暖风频吹</b>：国新办解读"十五五"新型工业化，集成电路/低空经济/机器人/6G/核聚变等新兴产业加快布局；发改委"六张网"投融资政策；银行法草案修订。政策底信号明确。</p>
    <p><b class="text-orange-400">技术面</b>：沪指站上3900点（收3912.52），逼近3912前高压力位，3950-4000点区域为强压力。缩量上涨说明追高意愿不足，量能能否重回1.9-2万亿是突破关键。科创50+1.71%领涨，科技成长有回暖迹象。</p>
    <p><b class="text-blue-400">结构特征</b>：早盘冲高、午后震荡回落，分时白线强于黄线（权重强于题材）。大金融+有色双线领涨，科技板块分化（半导体小幅流出但科创50领涨说明硬科技方向有资金布局）。结构性行情特征明显。</p>
  </div>
</div>

<div class="grid md:grid-cols-2 gap-4">
  <div class="bg-yellow-500/10 border border-yellow-500/30 rounded-xl p-4">
    <h4 class="text-yellow-300 font-semibold mb-2 flex items-center gap-2"><span>☀️</span> 今日展望</h4>
    <div class="text-xs text-white/70 space-y-1.5 leading-relaxed">
      <p>· 英伟达财报超预期+Vera Rubin量产催化，AI算力链有望高开反弹</p>
      <p>· 但昨日缩量上涨、量能不足，且PCE通胀超预期加息担忧压制风险偏好</p>
      <p>· 关注3912-3950压力位能否放量突破，无量则警惕冲高回落</p>
      <p>· 十五五新型工业化政策利好持续发酵，关注半导体设备/机器人/低空经济</p>
      <p>· 铜冠铜箔半年报+514%但Q2环比仅+2%，警惕利好出尽回调</p>
    </div>
  </div>
  <div class="bg-blue-500/10 border border-blue-500/30 rounded-xl p-4">
    <h4 class="text-blue-300 font-semibold mb-2 flex items-center gap-2"><span>🎯</span> 今日关注点</h4>
    <div class="text-xs text-white/70 space-y-1.5 leading-relaxed">
      <p>· <b>英伟达财报传导</b>：半导体设备/光模块/HBM/AI算力链开盘反应</p>
      <p>· <b>铜冠铜箔半年报</b>：+514%但Q2环比仅+2%，产能天花板隐忧</p>
      <p>· <b>量能变化</b>：能否重回1.9万亿以上决定反弹高度</p>
      <p>· <b>大金融持续性</b>：券商/保险能否延续，还是一日游</p>
      <p>· <b>北向资金</b>：外资动向观察风险偏好变化</p>
    </div>
  </div>
</div>
</div>'''
gen.add_section("A股昨日复盘与今日展望", ashare_html, "📊")

# 核心题材与今日催化
topics_html = '''
<div class="space-y-4">

<div class="bg-gradient-to-br from-red-500/10 to-orange-500/5 border border-red-500/30 rounded-xl p-4">
  <h4 class="text-red-400 font-bold mb-3 flex items-center gap-2"><span class="text-lg">🔴</span> S级催化 · AI算力/Vera Rubin量产/存储瓶颈</h4>
  <div class="space-y-3 text-xs text-white/70 leading-relaxed">
    <div class="bg-white/5 rounded-lg p-3">
      <p class="text-white font-semibold mb-1">🔥 英伟达Q2财报全面超预期，AI算力景气度再验证</p>
      <p>营收962亿美元（+106%），数据中心890亿（+117%），双双超预期。Q3指引1080亿美元（环比+12%），2028财年指引营收+70%，未完成订单超2万亿美元。AI算力需求不仅没有放缓，反而在加速增长。Vera Rubin全面量产，GPU价值量从180亿/吉瓦跃升至400亿/吉瓦，单机价值量翻倍以上。</p>
      <p class="text-yellow-400 mt-2">影响链条：GPU→AI服务器→光模块/光互联→HBM/存储→先进封装→半导体设备→液冷散热</p>
      <p class="text-orange-400">相关标的：英维克（液冷）、雅克科技（HBM材料/前驱体）、铜冠铜箔（AI服务器高端铜箔）、中际旭创、天孚通信、北方华创、中微公司</p>
    </div>
    <div class="bg-white/5 rounded-lg p-3">
      <p class="text-white font-semibold mb-1">💎 存储供应瓶颈加剧，价格持续上涨逻辑强化</p>
      <p>英伟达CFO明确警告内存价格"极端高企"，超出此前预期且明年还会更高。供应承诺金额从1190亿激增至2790亿美元，主要是存储器采购。这验证了存储芯片超级周期的核心逻辑——AI算力爆发→存储需求爆发→供应跟不上→价格持续上涨。</p>
      <p class="text-yellow-400">存储产业链：HBM＞DDR5/NAND＞高端铜箔/ABF/封装材料＞存储设备</p>
      <p class="text-orange-400">相关标的：美光/三星/SK海力士（海外）、长鑫科技、江波龙、德明利、雅克科技（HBM前驱体）、华海诚科（HBM环氧塑封料）、铜冠铜箔（高端铜箔）</p>
    </div>
  </div>
</div>

<div class="bg-gradient-to-br from-yellow-500/10 to-amber-500/5 border border-yellow-500/30 rounded-xl p-4">
  <h4 class="text-yellow-400 font-bold mb-3 flex items-center gap-2"><span class="text-lg">🟡</span> A级催化 · 十五五新型工业化/铜冠铜箔半年报/脑机接口</h4>
  <div class="space-y-3 text-xs text-white/70 leading-relaxed">
    <div class="bg-white/5 rounded-lg p-3">
      <p class="text-white font-semibold mb-1">🏭 "十五五"新型工业化规划落地，多产业加速</p>
      <p>国新办发布会明确"十五五"时期加快打造集成电路、航空航天、生物医药、低空经济、新型储能、智能机器人等新兴支柱产业，推动量子科技、生物制造、氢能和核聚变能、脑机接口、具身智能、6G等未来产业成为新增长点。上海"十五五"战略新兴产业增加值目标2.1万亿，三大先导产业制造业年均增速10%+。</p>
      <p class="text-blue-400">重点方向：半导体设备/材料（国产替代加速）、人形机器人（量产验证期）、低空经济（政策持续催化）、6G（与AI/卫星互联网融合）</p>
    </div>
    <div class="bg-white/5 rounded-lg p-3">
      <p class="text-white font-semibold mb-1">📄 铜冠铜箔半年报：净利润+514.75%，但Q2环比仅+2%</p>
      <p>营收40.21亿（+34.16%），归母净利润2.15亿（+514.75%），扣非2.07亿（+754.21%）。但拆解来看：Q1净利1.06亿、Q2 1.09亿，环比仅增长2%，几乎原地踏步。高增长部分来自低基数（去年上半年仅3495万）。出货主力仍为HVLP2代，HVLP4/5代放量节奏不确定。且公司"暂无新增扩产计划"，产能8万吨/年已到天花板。</p>
      <p class="text-red-400">风险提示：利好出尽+产能天花板+行业扩产潮中落后，短期注意回调风险。长期需关注HVLP5代放量节奏。</p>
    </div>
    <div class="bg-white/5 rounded-lg p-3">
      <p class="text-white font-semibold mb-1">🧠 京津冀脑机接口跨区域质量强链方案印发</p>
      <p>围绕神经信号采集、解码、控制和反馈等关键环节，推动新型干电极、柔性电极、脑机接口信号采集芯片、计算解码芯片等技术突破。2026年是脑机接口从技术探索迈向产业落地的关键一年。</p>
    </div>
  </div>
</div>

<div class="bg-gradient-to-br from-green-500/10 to-emerald-500/5 border border-green-500/30 rounded-xl p-4">
  <h4 class="text-green-400 font-bold mb-3 flex items-center gap-2"><span class="text-lg">🟢</span> B级关注 · 大金融/有色/光通信</h4>
  <div class="space-y-3 text-xs text-white/70 leading-relaxed">
    <div class="bg-white/5 rounded-lg p-3">
      <p class="text-white font-semibold mb-1">🏦 券商半年报爆发，大金融持续性待观察</p>
      <p>21家券商半年报净利同比+53%，驱动券商板块领涨。但券商板块持续性历来偏弱，需观察今日能否延续放量上涨。保险板块同步走强。银行法草案修订或带来长期估值修复。</p>
    </div>
    <div class="bg-white/5 rounded-lg p-3">
      <p class="text-white font-semibold mb-1">🥇 光通信板块隔夜走强，Lumentum+6%</p>
      <p>AI算力光互联需求持续验证，Lumentum涨超6%、康宁+3%、Coherent+2%。光模块是AI算力链中业绩确定性最高的环节之一，中际旭创/天孚通信等半年报业绩亮眼。</p>
    </div>
  </div>
</div>

</div>'''
gen.add_section("核心题材与今日催化", topics_html, "🔥")

# 持仓诊断
holdings_html = '''
<div class="space-y-4">
<div class="grid md:grid-cols-2 gap-4">

  <div class="bg-gradient-to-br from-amber-500/10 to-yellow-500/5 border border-amber-500/40 rounded-xl p-4">
    <div class="flex items-center justify-between mb-2">
      <h4 class="text-amber-400 font-bold flex items-center gap-2"><span>💼</span> 英维克（002837）</h4>
      <span class="text-xs bg-amber-500/20 text-amber-400 px-2 py-0.5 rounded-full">液冷散热龙头</span>
    </div>
    <div class="flex items-end gap-3 mb-2">
      <span class="text-2xl font-bold text-white">62.07</span>
      <span class="text-sm text-red-400 font-semibold">+1.84 (+3.05%)</span>
    </div>
    <div class="text-xs text-white/70 space-y-1.5 leading-relaxed">
      <p><b class="text-white">基本面：</b>液冷散热龙头，AI算力液冷渗透率持续提升。半年报营收+17%、净利-14%，Q2环比改善。</p>
      <p><b class="text-green-400">利好催化：</b>英伟达Vera Rubin量产→AI算力建设加速→液冷需求增长；Vera Rubin功耗更高，液冷刚需更强。</p>
      <p><b class="text-red-400">风险点：</b>净利下滑说明价格战/毛利率承压；板块轮动较快。</p>
      <p><b class="text-yellow-400">操作建议：</b>持有观察，压力位63-65元，支撑位58-60元。英伟达利好催化下若放量突破65元可加仓，否则逢高减仓机动仓位。</p>
    </div>
  </div>

  <div class="bg-gradient-to-br from-amber-500/10 to-yellow-500/5 border border-amber-500/40 rounded-xl p-4">
    <div class="flex items-center justify-between mb-2">
      <h4 class="text-amber-400 font-bold flex items-center gap-2"><span>💼</span> 铜冠铜箔（301217）</h4>
      <span class="text-xs bg-amber-500/20 text-amber-400 px-2 py-0.5 rounded-full">AI铜箔/锂电铜箔</span>
    </div>
    <div class="flex items-end gap-3 mb-2">
      <span class="text-2xl font-bold text-white">107.82</span>
      <span class="text-sm text-green-400 font-semibold">-2.71 (-2.45%)</span>
    </div>
    <div class="text-xs text-white/70 space-y-1.5 leading-relaxed">
      <p><b class="text-white">基本面：</b>半年报净利+514.75%，但Q2环比仅+2%，低基数效应明显。产能8万吨/年已到天花板，暂无扩产计划。</p>
      <p><b class="text-green-400">利好催化：</b>AI服务器高端铜箔需求旺盛，HVLP铜箔供不应求；MSCI纳入带来被动资金。</p>
      <p><b class="text-red-400">风险点：</b>Q2环比停滞，产能天花板隐忧，行业扩产潮中掉队风险；年内涨幅已超214%，估值偏高。</p>
      <p><b class="text-yellow-400">操作建议：</b>半年报利好出尽，昨日已跌2.45%，短期注意回调风险。支撑位100-102元，压力位110-115元。底仓持有，机动仓位逢高减仓，待回调至100元附近再加仓。</p>
    </div>
  </div>

  <div class="bg-gradient-to-br from-amber-500/10 to-yellow-500/5 border border-amber-500/40 rounded-xl p-4">
    <div class="flex items-center justify-between mb-2">
      <h4 class="text-amber-400 font-bold flex items-center gap-2"><span>💼</span> 雅克科技（002409）</h4>
      <span class="text-xs bg-amber-500/20 text-amber-400 px-2 py-0.5 rounded-full">半导体材料平台</span>
    </div>
    <div class="flex items-end gap-3 mb-2">
      <span class="text-2xl font-bold text-white">135.23</span>
      <span class="text-sm text-green-400 font-semibold">-1.96 (-1.43%)</span>
    </div>
    <div class="text-xs text-white/70 space-y-1.5 leading-relaxed">
      <p><b class="text-white">基本面：</b>半年报归母净利润5.61亿（+7.29%），Q2单季净利同比+12.08%。半导体前驱体全球前三，光刻胶/电子特气/硅微粉多业务布局。</p>
      <p><b class="text-green-400">利好催化：</b>存储供应瓶颈加剧→HBM需求爆发→前驱体/封装材料需求增长；英伟达Vera Rubin量产催化AI算力链。</p>
      <p><b class="text-red-400">风险点：</b>昨日主力资金净流出2.55亿，连续多日流出；净利增速偏低（+7%）与高估值不匹配；股东户数大增152%，筹码分散。</p>
      <p><b class="text-yellow-400">操作建议：</b>底仓持有，关注130元支撑位。英伟达利好催化下若能反弹至145-150元可减仓机动仓。真正击球区115-120元。</p>
    </div>
  </div>

  <div class="bg-gradient-to-br from-amber-500/10 to-yellow-500/5 border border-amber-500/40 rounded-xl p-4">
    <div class="flex items-center justify-between mb-2">
      <h4 class="text-amber-400 font-bold flex items-center gap-2"><span>💼</span> *ST建艺（002789）</h4>
      <span class="text-xs bg-red-500/20 text-red-400 px-2 py-0.5 rounded-full">ST摘帽预期</span>
    </div>
    <div class="flex items-end gap-3 mb-2">
      <span class="text-2xl font-bold text-white">10.30</span>
      <span class="text-sm text-red-400 font-semibold">+0.07 (+0.68%)</span>
    </div>
    <div class="text-xs text-white/70 space-y-1.5 leading-relaxed">
      <p><b class="text-white">基本面：</b>建筑装饰+新能源业务双轮驱动，ST摘帽预期标的。</p>
      <p><b class="text-green-400">利好催化：</b>若摘帽成功将迎来估值修复；基建政策持续发力。</p>
      <p><b class="text-red-400">风险点：</b>ST股流动性差、波动大；摘帽时间不确定。</p>
      <p><b class="text-yellow-400">操作建议：</b>小仓位博弈，严格止损。支撑位9.5元，压力位11元。</p>
    </div>
  </div>

</div>

<div class="bg-white/5 rounded-xl p-4">
  <h4 class="text-white font-semibold mb-3 flex items-center gap-2"><span>📊</span> 持仓组合诊断</h4>
  <div class="grid md:grid-cols-3 gap-3 text-xs">
    <div class="bg-gradient-to-br from-blue-500/10 to-cyan-500/5 border border-blue-500/20 rounded-lg p-3">
      <div class="text-white/60 mb-1">组合仓位</div>
      <div class="text-lg font-bold text-white">5-6成</div>
      <div class="text-blue-400">中等仓位，灵活应对</div>
    </div>
    <div class="bg-gradient-to-br from-purple-500/10 to-pink-500/5 border border-purple-500/20 rounded-lg p-3">
      <div class="text-white/60 mb-1">风格偏向</div>
      <div class="text-lg font-bold text-white">科技成长</div>
      <div class="text-purple-400">AI算力链+半导体材料</div>
    </div>
    <div class="bg-gradient-to-br from-orange-500/10 to-red-500/5 border border-orange-500/20 rounded-lg p-3">
      <div class="text-white/60 mb-1">风险等级</div>
      <div class="text-lg font-bold text-white">中等偏高</div>
      <div class="text-orange-400">科技股波动大，注意风控</div>
    </div>
  </div>
  <div class="mt-3 text-xs text-white/70 leading-relaxed">
    <p><b class="text-white">组合诊断：</b>持仓4只全部集中在AI算力产业链（液冷/铜箔/半导体材料），Beta属性强，与科技板块高度绑定。英伟达财报超预期将带来正向催化，但需警惕"利好出尽"风险。建议：①利用英伟达利好冲高时适度减仓铜冠铜箔（产能天花板+涨幅已大）；②英维克和雅克科技底仓持有，关注量能变化；③整体仓位控制在5-6成，保留现金应对波动。</p>
  </div>
</div>
</div>'''
gen.add_section("持仓诊断与操作建议", holdings_html, "💼")

# 空方视角
bear_html = '''
<div class="space-y-4">
<div class="bg-gradient-to-br from-green-500/10 to-emerald-500/5 border border-green-500/30 rounded-xl p-4">
  <h4 class="text-green-400 font-bold mb-3 flex items-center gap-2"><span>🐻</span> 空方视角：四大风险不容忽视</h4>
  <div class="space-y-3 text-xs text-white/70 leading-relaxed">

    <div class="bg-white/5 rounded-lg p-3 border-l-2 border-green-500/50">
      <p class="text-white font-semibold mb-1">风险一：英伟达"利好出尽"，Buy the rumor, sell the news</p>
      <p>英伟达财报确实超预期，但市场已连续下跌7天后反弹，预期已部分消化。历史规律显示，财报超预期≠股价继续涨——过去几个季度英伟达财报后经常出现"利好兑现"式回调。尤其当前英伟达已连跌7天，盘后涨4%可能只是短期修复，而非新一轮上涨的开始。</p>
      <p class="text-green-400">应对：高开不追高，观察30分钟-1小时量能变化，无量冲高则减仓。</p>
    </div>

    <div class="bg-white/5 rounded-lg p-3 border-l-2 border-green-500/50">
      <p class="text-white font-semibold mb-1">风险二：PCE通胀超预期，美联储加息概率上升</p>
      <p>7月PCE物价指数环比+0.2%（预期+0.1%），通胀黏性超出市场预期。杰克逊霍尔年会即将召开，市场担忧美联储释放更鹰派信号。美元指数已上涨0.25%，美债收益率高位震荡。若美联储释放加息信号，全球风险资产将承压。</p>
      <p class="text-green-400">应对：关注杰克逊霍尔会议（周五），会前保持谨慎，避免重仓。</p>
    </div>

    <div class="bg-white/5 rounded-lg p-3 border-l-2 border-green-500/50">
      <p class="text-white font-semibold mb-1">风险三：A股缩量上涨，3900点上方压力重重</p>
      <p>昨日沪指站上3900点，但成交额缩量至1.81万亿（较前一日-230亿），缩量上涨说明追高意愿不足。3912-3950-4000点层层压力，无量难以突破。且昨日上涨主要由大金融（券商）驱动，题材股赚钱效应一般（白线＞黄线），结构性行情特征明显，指数行情＞个股行情。</p>
      <p class="text-green-400">应对：无量冲高减仓，等待回踩3850-3880支撑区再考虑加仓。</p>
    </div>

    <div class="bg-white/5 rounded-lg p-3 border-l-2 border-green-500/50">
      <p class="text-white font-semibold mb-1">风险四：存储/铜箔板块高位利好兑现压力</p>
      <p>铜冠铜箔半年报+514%但Q2环比仅+2%，且产能无扩张计划，增长天花板隐现。雅克科技半年报净利仅+7.29%，与高估值（PE＞100倍）不匹配。存储板块经历了近一年的持续上涨后，机构持仓拥挤，获利盘丰厚，任何利空都可能引发回调。</p>
      <p class="text-green-400">应对：持仓股逢高分批减仓，保护利润，不要等利润回吐再行动。</p>
    </div>

  </div>
</div>

<div class="bg-white/5 rounded-xl p-4">
  <h4 class="text-white font-semibold mb-3 flex items-center gap-2"><span>⚔️</span> 多空博弈与关键点位</h4>
  <div class="grid md:grid-cols-2 gap-4 text-xs">
    <div class="bg-red-500/5 border border-red-500/20 rounded-lg p-3">
      <p class="text-red-400 font-semibold mb-2">多方论据</p>
      <ul class="text-white/70 space-y-1 list-disc pl-4">
        <li>英伟达Q2全面超预期，AI算力景气度再验证</li>
        <li>Vera Rubin量产打开新一轮增长空间</li>
        <li>"十五五"新型工业化政策持续催化</li>
        <li>沪指站上3900点，技术形态偏强</li>
        <li>大金融+有色双线轮动，市场不缺热点</li>
      </ul>
    </div>
    <div class="bg-green-500/5 border border-green-500/20 rounded-lg p-3">
      <p class="text-green-400 font-semibold mb-2">空方论据</p>
      <ul class="text-white/70 space-y-1 list-disc pl-4">
        <li>英伟达利好出尽，buy the rumor sell the news</li>
        <li>PCE通胀超预期，美联储加息担忧升温</li>
        <li>A股缩量上涨，3900点上方压力大</li>
        <li>科技股估值偏高，获利盘丰厚</li>
        <li>杰克逊霍尔年会前市场观望情绪浓</li>
      </ul>
    </div>
  </div>
  <div class="mt-3 text-xs text-white/70">
    <p><b class="text-yellow-400">关键点位：</b>支撑位3880/3850，压力位3912/3950/4000。若今日放量突破3950且成交额回到2万亿以上，可看高一线；若无量冲高回落跌破3880，则需警惕短期调整。</p>
  </div>
</div>
</div>'''
gen.add_section("空方视角与多空博弈", bear_html, "⚖️")

# 预判验证闭环
prediction_html = '''
<div class="space-y-4">
<div class="bg-white/5 rounded-xl p-4">
  <h4 class="text-white font-semibold mb-3 flex items-center gap-2"><span>🔮</span> 预判验证闭环</h4>
  <div class="text-xs text-white/70 space-y-3 leading-relaxed">

    <div class="bg-yellow-500/10 border border-yellow-500/30 rounded-lg p-3">
      <div class="flex items-center justify-between mb-2">
        <span class="text-yellow-400 font-semibold">📌 新预判记录（本期新增）</span>
        <span class="text-xs bg-yellow-500/20 text-yellow-400 px-2 py-0.5 rounded">待验证</span>
      </div>
      <div class="space-y-2">
        <div class="bg-white/5 rounded p-2">
          <p><b>预判1：</b>英伟达Q2超预期+Vera Rubin量产催化下，AI算力链将迎来一波反弹，半导体设备/光模块/HBM材料弹性最大，持续时间约3-5天。</p>
          <p class="text-yellow-300">验证时点：T+3（8月29日）观察反弹持续性</p>
        </div>
        <div class="bg-white/5 rounded p-2">
          <p><b>预判2：</b>铜冠铜箔半年报利好出尽，Q2环比仅+2%+产能天花板，短期将回调至100-102元支撑区间。</p>
          <p class="text-yellow-300">验证时点：T+5（9月2日）观察股价走势</p>
        </div>
        <div class="bg-white/5 rounded p-2">
          <p><b>预判3：</b>沪指3912-3950区间压力较大，无量难突破，短期将在3850-3950区间震荡整理。</p>
          <p class="text-yellow-300">验证时点：T+5（9月2日）观察指数运行区间</p>
        </div>
        <div class="bg-white/5 rounded p-2">
          <p><b>预判4：</b>存储供应瓶颈加剧的逻辑将持续强化，美光/三星/SK海力士股价中期仍有上行空间，A股存储链（雅克科技/华海诚科等）调整后仍有机会。</p>
          <p class="text-yellow-300">验证时点：T+10（9月9日）中期验证</p>
        </div>
      </div>
    </div>

    <div class="bg-blue-500/10 border border-blue-500/30 rounded-lg p-3">
      <div class="flex items-center justify-between mb-2">
        <span class="text-blue-400 font-semibold">📊 历史预判验证汇总</span>
        <span class="text-xs bg-blue-500/20 text-blue-400 px-2 py-0.5 rounded">持续跟踪</span>
      </div>
      <p class="text-white/60 text-xs mb-2">完整预判验证数据见「预判验证中心」页面</p>
      <div class="grid grid-cols-4 gap-2 text-center">
        <div class="bg-white/5 rounded-lg p-2">
          <div class="text-lg font-bold text-green-400">--</div>
          <div class="text-xs text-white/60">正确</div>
        </div>
        <div class="bg-white/5 rounded-lg p-2">
          <div class="text-lg font-bold text-red-400">--</div>
          <div class="text-xs text-white/60">错误</div>
        </div>
        <div class="bg-white/5 rounded-lg p-2">
          <div class="text-lg font-bold text-yellow-400">--</div>
          <div class="text-xs text-white/60">待验证</div>
        </div>
        <div class="bg-white/5 rounded-lg p-2">
          <div class="text-lg font-bold text-blue-400">--</div>
          <div class="text-xs text-white/60">准确率</div>
        </div>
      </div>
    </div>

  </div>
</div>
</div>'''
gen.add_section("预判验证闭环", prediction_html, "🔮")

# 教训库引用
lesson_html = '''
<div class="space-y-4">
<div class="bg-white/5 rounded-xl p-4">
  <h4 class="text-white font-semibold mb-3 flex items-center gap-2"><span>📚</span> 教训库引用</h4>
  <div class="space-y-3 text-xs text-white/70 leading-relaxed">

    <div class="bg-orange-500/10 border border-orange-500/30 rounded-lg p-3">
      <p class="text-orange-400 font-semibold mb-2">💡 教训1：利好出尽是利空——财报季的经典陷阱</p>
      <p><b>历史教训：</b>每次英伟达/苹果/特斯拉等科技巨头财报超预期后，股价经常出现"利好兑现"式回调。原因是财报前预期已经炒高，利好落地后获利盘出逃。2025-2026年多次出现"财报前涨、财报后跌"的模式。</p>
      <p><b>本次启示：</b>英伟达盘后涨4%，但今日A股AI算力链高开后需警惕追高风险。不要因为"英伟达超预期"就冲动加仓，先观察量能和持续性。</p>
    </div>

    <div class="bg-orange-500/10 border border-orange-500/30 rounded-lg p-3">
      <p class="text-orange-400 font-semibold mb-2">💡 教训2：高位股逢高分批减仓，不要等利润回吐</p>
      <p><b>历史教训：</b>铜冠铜箔年内涨幅已超214%、雅克科技从底部涨近5倍。历史经验表明，涨幅超过200%的股票，一旦进入调整期，回撤幅度往往达到30-50%。很多投资者因为"还会涨"的执念，从盈利50%拿到亏损20%。</p>
      <p><b>本次启示：</b>严格执行"高位股逢高分批减仓"纪律。铜冠铜箔半年报利好是很好的减仓时机，不要等跌下来再后悔。底仓保留、机动仓位获利了结，是牛市中期的正确姿势。</p>
    </div>

    <div class="bg-orange-500/10 border border-orange-500/30 rounded-lg p-3">
      <p class="text-orange-400 font-semibold mb-2">💡 教训3：缩量上涨不可持续，量价配合才是真突破</p>
      <p><b>历史教训：</b>A股市场历次重要突破（如3500、3700、3900）都需要放量确认。缩量上涨往往是"虚涨"，后续容易回踩确认。2025年底3600点缩量突破后回踩了200点。</p>
      <p><b>本次启示：</b>昨日1.81万亿成交额站上3900点，缩量+230亿，量能不足。若今日不能放量到1.9-2万亿，3912-3950点大概率遇阻回落。不要被指数上涨冲昏头脑，量价配合才是真突破。</p>
    </div>

    <div class="bg-orange-500/10 border border-orange-500/30 rounded-lg p-3">
      <p class="text-orange-400 font-semibold mb-2">💡 教训4：业绩≠股价，低基数效应需警惕</p>
      <p><b>历史教训：</b>"净利润同比增长500%"听起来很惊人，但如果去年基数只有3000万，今年也才1.8亿，对应近900亿市值仍然很贵。很多投资者被同比增速迷惑，忽略了绝对估值和环比变化。</p>
      <p><b>本次启示：</b>铜冠铜箔+514%看似惊人，但Q2环比仅+2%说明增长已经停滞。看业绩不能只看同比增速，还要看环比变化、绝对利润、产能天花板、估值水平。</p>
    </div>

  </div>
</div>
</div>'''
gen.add_section("教训库引用", lesson_html, "📚")

# 添加重要新闻汇总
gen.add_important_news()

# 发布
output_path = os.path.join(WORK_DIR, "docs/daily/20260827_每日新闻洞察.html")
result = gen.publish(output_path=output_path)
print("发布结果:", result)
print(f"文件大小: {result.get('file_size', 0)} 字节")
print(f"输出路径: {result.get('output_path', '')}")
