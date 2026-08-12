#!/usr/bin/env python3
"""2026年8月12日 每日新闻洞察生成 - 周三·费半逆势涨0.87%·工业富联中报净利翻倍·CME推出算力期货·源杰科技43亿扩产·SK海力士大连NAND扩50%"""
import sys, os, shutil, json
WORK_DIR = '/root/daily-news-insight'
sys.path.insert(0, os.path.join(WORK_DIR, 'v3'))
from generators.daily_pro import DailyReportProGenerator

gen = DailyReportProGenerator(
    date_str='2026年8月12日', weekday='星期三',
    subtitle='2026年8月12日 周三 · 费半逆势涨0.87%阿斯麦+3.8%·工业富联中报净利+96%·CME推出算力期货·源杰科技43亿扩产·SK海力士大连NAND产能+50%',
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
        '美股震荡：三大指数微跌但费城半导体逆势涨0.87%，阿斯麦+3.8%美光+0.87%；谷歌-3.6%领跌七巨头；原油续涨黄金微跌',
        '工业富联中报：上半年净利237.4亿同比+96%创历史新高，云计算营收+75.7%，AI服务器出货量爆发，但股价先跌4.58%',
        '算力金融化：CME芝商所10月推出H100/B200算力期货合约，算力从资源变可交易大宗商品；SK海力士大连NAND扩产50%',
        '持仓策略：科技分化延续，半导体设备材料相对强势；铜冠铜箔/雅克科技逢高减仓，英维克反弹减仓，*ST建艺清仓'
    ],
    operation_advice='费半逆势走强+工业富联业绩验证+算力期货新物种，今日科技或有修复但分化加剧；逢高减仓高位股，关注半导体设备/光芯片方向机会',
    risk_level='中等',
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
    description='每日新闻洞察 2026年8月12日：费半逆势涨0.87%、工业富联中报净利+96%、CME推出算力期货、源杰科技43亿扩产',
)

gen.add_global_market()

global_cards1 = render_cards([
    {"name":"道琼斯","change":"-0.34%","up":False},
    {"name":"标普500","change":"-0.32%","up":False},
    {"name":"纳斯达克","change":"-0.60%","up":False},
    {"name":"费城半导体","change":"+0.87%","up":True},
    {"name":"日经225","change":"-0.90%","up":False},
    {"name":"恒生指数","change":"-1.10%","up":False},
])
global_list1 = render_list([
    {"name":"WTI原油","change":"+0.58%/$83.69","up":True},
    {"name":"布伦特原油","change":"+0.51%/$89.36","up":True},
    {"name":"COMEX黄金","change":"-0.08%/$4437.34","up":False},
    {"name":"COMEX白银","change":"+0.16%/$65.04","up":True},
])
global_list2 = render_list([
    {"name":"三星电子","change":"+4.13%","up":True},
    {"name":"SK海力士","change":"+0.35%","up":True},
    {"name":"美光科技","change":"+0.87%","up":True},
    {"name":"台积电ADR","change":"+0.86%","up":True},
])
global_list3 = render_list([
    {"name":"英伟达","change":"-0.02%/$217.50","up":False},
    {"name":"AMD","change":"+1.01%/$474.32","up":True},
    {"name":"微软","change":"-0.44%/$503.81","up":False},
    {"name":"苹果","change":"-1.09%/$304.91","up":False},
    {"name":"博通","change":"-1.50%/$416.08","up":False},
    {"name":"英特尔","change":"+0.19%/$97.71","up":True},
    {"name":"应用材料","change":"+0.67%/$525.61","up":True},
    {"name":"阿斯麦","change":"+3.80%/$1799.38","up":True},
])

global_html = '''
<div class="grid md:grid-cols-3 gap-4">
  <div class="md:col-span-2">
    <div class="text-white font-semibold mb-3 flex items-center gap-2"><span>🌍</span><span>隔夜全球市场 · 半导体逆势走强·算力金融化元年开启·谷歌大跌近4%</span></div>
    <div class="grid grid-cols-3 md:grid-cols-6 gap-2">{0}</div>
    <p class="text-xs text-white/50 mt-3 leading-relaxed">
      ⚡ <b class="text-yellow-400">核心要点：美股三大指数小幅收跌但费城半导体逆势涨0.87%，阿斯麦+3.8%、应用材料+0.67%、美光+0.87%；谷歌-3.6%领跌七巨头（近6个月最大单日跌幅）；CME推出算力期货，算力成为可交易大宗商品；原油续涨黄金微跌</b>——<br>
      ①<b>半导体逆势走强</b>：费城半导体指数+0.87%收12098.47，30只成分股24只上涨。阿斯麦+3.8%领涨（伯恩斯坦上调晶圆设备支出预测，2026年1480亿美元+26%，2027年2040亿+33%），应用材料+0.67%、美光+0.87%、AMD+1.01%。存储板块SK海力士+4.7%（盘前一度涨超6%，董事长称AI芯片需求明年翻倍）、闪迪+2.68%。<br>
      ②<b>科技七巨头多数下跌</b>：谷歌-3.61%领跌（近6个月最大单日跌幅），亚马逊-2.09%、博通-1.50%、苹果-1.09%、微软-0.44%、英伟达-0.02%；SpaceX-3.93%。AI产业链融资泡沫担忧持续打压科技巨头，但小盘股逆市上涨，市场风格从大盘科技向中小盘扩散。<br>
      ③<b>CME推出算力期货</b>：芝商所宣布10月5日推出Silicon Data H100和B200 GPU租赁指数期货合约，算力正式成为可交易大宗商品。CME高管称"算力是AI时代的货币"，如同石油推动20世纪经济发展，算力期货将提供对冲和价格发现功能。<br>
      ④<b>SK海力士大连扩产50%</b>：SK海力士旗下Solidigm重启停滞4年的中国大连NAND第二工厂建设，最早11月进设备、明年上半年量产。扩产后大连厂月产能增加约5万片晶圆（总产能+50%），主攻成熟NAND，高端NAND集中在韩国清州厂。<br>
      ⑤<b>原油续涨黄金回落</b>：WTI原油+0.58%收83.69美元，布伦特+0.51%收89.36美元，霍尔木兹海峡僵局仍未化解。COMEX黄金-0.08%收4437.34美元，从两个月高位小幅回落，市场等待美国CPI数据指引。<br>
      ⑥<b>中概股下跌</b>：纳斯达克中国金龙指数-2.94%，腾讯音乐跌近12%，哔哩哔哩跌超5%。港股恒生指数-1.10%，恒生科技指数-1.93%。
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
    <div class="text-xl font-bold text-green-400">3934.09</div>
    <div class="text-xs text-green-400">-0.82%</div>
  </div>
  <div class="bg-gradient-to-br from-green-500/20 to-emerald-500/10 border border-green-500/30 rounded-xl p-3 text-center">
    <div class="text-xs text-white/60 mb-1">深证成指</div>
    <div class="text-xl font-bold text-green-400">14259.44</div>
    <div class="text-xs text-green-400">-0.40%</div>
  </div>
  <div class="bg-gradient-to-br from-red-500/20 to-orange-500/10 border border-red-500/30 rounded-xl p-3 text-center">
    <div class="text-xs text-white/60 mb-1">创业板指</div>
    <div class="text-xl font-bold text-red-400">3549.16</div>
    <div class="text-xs text-red-400">+0.34%</div>
  </div>
  <div class="bg-gradient-to-br from-green-500/20 to-emerald-500/10 border border-green-500/30 rounded-xl p-3 text-center">
    <div class="text-xs text-white/60 mb-1">科创50</div>
    <div class="text-xl font-bold text-green-400">1709.00</div>
    <div class="text-xs text-green-400">-1.63%</div>
  </div>
</div>

<div class="grid md:grid-cols-2 gap-4">
  <div class="bg-white/5 rounded-xl p-4">
    <h4 class="text-white font-semibold mb-3 flex items-center gap-2"><span>📉</span> 领跌板块</h4>
    <div class="space-y-1 text-xs">
      <div class="flex justify-between"><span class="text-white/70">贵金属/黄金</span><span class="text-green-400">-3%~-5%</span></div>
      <div class="flex justify-between"><span class="text-white/70">军工/航天装备</span><span class="text-green-400">-2%~-3%</span></div>
      <div class="flex justify-between"><span class="text-white/70">有色金属/小金属</span><span class="text-green-400">-2%~-3%</span></div>
      <div class="flex justify-between"><span class="text-white/70">能源金属</span><span class="text-green-400">-2%左右</span></div>
    </div>
  </div>
  <div class="bg-white/5 rounded-xl p-4">
    <h4 class="text-white font-semibold mb-3 flex items-center gap-2"><span>📈</span> 领涨板块</h4>
    <div class="space-y-1 text-xs">
      <div class="flex justify-between"><span class="text-white/70">通信/光通信</span><span class="text-red-400">+1%~+2%</span></div>
      <div class="flex justify-between"><span class="text-white/70">医药/CRO/商业</span><span class="text-red-400">+1%~+3%</span></div>
      <div class="flex justify-between"><span class="text-white/70">机器人/减速器</span><span class="text-red-400">+1%~+2%</span></div>
      <div class="flex justify-between"><span class="text-white/70">影视院线/传媒</span><span class="text-red-400">+2%~+3%</span></div>
    </div>
  </div>
</div>

<div class="bg-white/5 rounded-xl p-4">
  <h4 class="text-white font-semibold mb-3 flex items-center gap-2"><span>📋</span> 昨日（周二）核心盘面回顾</h4>
  <div class="text-xs text-white/70 space-y-2 leading-relaxed">
    <p>① <b class="text-yellow-400">沪指5连阳终结</b>：上证指数-0.82%收3934点（权重蓝筹抛压大，白酒、金融、军工领跌），深成指-0.40%，创业板+0.34%逆势上涨。全市场成交2.32万亿缩量约2000亿，仅1615只上涨、3777只下跌，涨跌中位数约-1.1%。</p>
    <p>② <b class="text-yellow-400">成长风格相对抗跌</b>：创业板指唯一收涨，主力资金净流入7.42亿元（超大单+23.85亿），而主板主力净流出超250亿。资金从主板向创业板调仓，通信（+1.13%）、医药、机器人等成长赛道逆势走强。</p>
    <p>③ <b class="text-yellow-400">贵金属军工回调</b>：前期强势的贵金属、军工板块昨日获利了结，黄金股从周一领涨变周二领跌。原油暴涨后国内能源板块冲高回落，市场风格快速轮动。</p>
    <p>④ <b class="text-yellow-400">工业富联业绩炸但股价跌</b>：工业富联上半年净利237.4亿同比+96%创历史新高，但股价当日跌4.58%，市值蒸发超600亿。典型的"利好出尽"，7月初业绩预告已提前消化。</p>
    <p>⑤ <b class="text-yellow-400">涨停家数大幅减少</b>：从昨日约100家降至约60家，高位连板股集体断板，短线情绪从高潮转向分化。60只涨停、2只跌停，跌停数减少但赚钱效应差。</p>
  </div>
</div>

<div class="bg-gradient-to-br from-blue-500/10 to-cyan-500/10 border border-blue-500/30 rounded-xl p-4">
  <h4 class="text-blue-300 font-semibold mb-3 flex items-center gap-2"><span>🔭</span> 今日（周三）展望</h4>
  <div class="text-xs text-white/70 space-y-2 leading-relaxed">
    <p>① <b class="text-yellow-400">半导体设备材料有望修复</b>：隔夜费半逆势涨0.87%，阿斯麦+3.8%（设备支出上修），SK海力士+4.7%（AI芯片需求翻倍）。叠加源杰科技43亿扩产光芯片，半导体设备材料方向今日有修复动能。</p>
    <p>② <b class="text-yellow-400">工业富联业绩验证算力景气</b>：中报净利+96%、云计算营收+75.7%、AI服务器出货量2-3倍增长，验证AI算力需求真实爆发。但股价已提前反映，关注是"利好出尽"还是"超预期继续涨"。</p>
    <p>③ <b class="text-yellow-400">算力金融化新物种</b>：CME推出算力期货是里程碑事件，算力从"资源"变"大宗商品"，可能催生算力产业链的新投资逻辑。关注GPU租赁、算力调度、云厂商相关标的。</p>
    <p>④ <b class="text-yellow-400">催化剂日历</b>：本周关注美国7月CPI数据（周三晚）、国内7月金融数据；今日关注工业富联中报市场反应、源杰科技扩产情绪传导、SK海力士扩产对存储产业链影响。</p>
  </div>
</div>
</div>'''
gen.add_section("A股昨日复盘与今日展望", ashare_html, "📊")

# 核心题材与今日催化
catalyst_html = '''
<div class="space-y-4">
  <div class="bg-gradient-to-br from-purple-500/10 to-pink-500/10 border border-purple-500/30 rounded-xl p-4">
    <div class="flex items-center justify-between mb-3">
      <h4 class="text-purple-300 font-semibold flex items-center gap-2"><span>⚡</span> S级催化：CME推出算力期货·算力正式成为可交易大宗商品</h4>
      <span class="text-xs bg-purple-500/30 text-purple-200 px-2 py-0.5 rounded">S级·新物种</span>
    </div>
    <div class="text-xs text-white/70 space-y-2 leading-relaxed">
      <p><b class="text-yellow-400">核心事件：</b>芝商所（CME Group）宣布与Silicon Data合作，计划于2026年10月5日推出两项算力期货合约——Silicon Data H100租赁指数期货和B200租赁指数期货，目前正等待监管审核。</p>
      <p><b class="text-yellow-400">历史意义：</b></p>
      <p>① <b>算力=AI时代的石油</b>：CME高管称"算力已经成为AI时代的货币"，如同石油推动20世纪经济并从现货演变为全球衍生品市场，算力期货将把算力转变为标准化、可交易的大宗商品。这是算力金融化的里程碑。</p>
      <p>② <b>价格发现与对冲工具</b>：过去两家企业买同样的GPU算力可能价差巨大，没有判断标准。算力期货提供公开可交易的参考价格，AI开发商和云厂商可对冲算力成本波动风险。</p>
      <p>③ <b>产业链影响深远</b>：算力期货市场的建立将吸引大量金融资本进入AI算力领域，可能加速算力基础设施建设，也可能催生算力投机泡沫。对GPU厂商、IDC运营商、液冷散热等上游需求形成长期支撑。</p>
      <p><b class="text-yellow-400">关联标的：</b>GPU算力（工业富联、浪潮信息）、液冷散热（英维克、高澜股份）、IDC运营（宝信软件、光环新网）、光模块/光芯片（中际旭创、源杰科技）</p>
    </div>
  </div>

  <div class="bg-gradient-to-br from-cyan-500/10 to-blue-500/10 border border-cyan-500/30 rounded-xl p-4">
    <div class="flex items-center justify-between mb-3">
      <h4 class="text-cyan-300 font-semibold flex items-center gap-2"><span>🏭</span> A级催化：工业富联中报净利+96%·AI服务器出货量爆发·但利好出尽？</h4>
      <span class="text-xs bg-cyan-500/30 text-cyan-200 px-2 py-0.5 rounded">A级·业绩</span>
    </div>
    <div class="text-xs text-white/70 space-y-2 leading-relaxed">
      <p><b class="text-yellow-400">业绩数据：</b>工业富联上半年营收5578.6亿元同比+54.63%，归母净利润237.4亿元同比+95.99%，双双创历史同期新高。Q2单季营收3067.8亿（环比+22%），净利131.5亿（环比+24%），连续4个季度净利破百亿。</p>
      <p><b class="text-yellow-400">AI业务爆发：</b>云计算板块营收同比+75.7%；云服务商AI服务器营收同比+2.3倍，GPU AI机柜出货量同比+3.2倍，ASIC AI机柜出货量同比+3倍。毛利率从多年下滑拐头向上，AI产品结构优化效果显著。</p>
      <p><b class="text-yellow-400">市场反应：</b>8月11日股价跌4.58%，市值蒸发超600亿，典型的"利好出尽"。7月初业绩预告已提前释放增长预期，资金在正式报告落地时兑现。不分红也引发市场不满。</p>
      <p><b class="text-yellow-400">投资启示：</b>算力需求真实且强劲，但股价已充分反映。业绩好≠股价涨，尤其是在高位。对整个算力产业链而言，工业富联的财报验证了需求端的真实性，对上游供应链（PCB、铜箔、液冷、光模块）形成基本面支撑。</p>
      <p><b class="text-yellow-400">关联标的：</b>AI服务器（工业富联、浪潮信息）、PCB铜箔（铜冠铜箔、沪电股份）、液冷散热（英维克、申菱环境）、光模块（中际旭创、新易盛）</p>
    </div>
  </div>

  <div class="bg-gradient-to-br from-orange-500/10 to-red-500/10 border border-orange-500/30 rounded-xl p-4">
    <div class="flex items-center justify-between mb-3">
      <h4 class="text-orange-300 font-semibold flex items-center gap-2"><span>💾</span> A级催化：SK海力士大连NAND扩产50%·存储资本开支加速</h4>
      <span class="text-xs bg-orange-500/30 text-orange-200 px-2 py-0.5 rounded">A级·海外映射</span>
    </div>
    <div class="text-xs text-white/70 space-y-2 leading-relaxed">
      <p><b class="text-yellow-400">扩产计划：</b>SK海力士旗下Solidigm已重启停滞4年的中国大连NAND第二工厂建设，最早今年11月进驻设备、明年上半年量产。扩产后大连厂月产能增加约5万片晶圆（总产能提升50%），主攻基于浮栅结构的100层级成熟NAND。</p>
      <p><b class="text-yellow-400">行业意义：</b></p>
      <p>① <b>存储需求强劲</b>：SK海力士董事长称AI芯片需求明年将翻倍，全球存储芯片供不应求格局持续。重启停滞4年的工厂，说明需求端确实紧张。</p>
      <p>② <b>设备材料需求增量</b>：大连工厂扩产5万片/月，对半导体设备和材料形成新增需求。国产替代背景下，国内供应链受益更直接。</p>
      <p>③ <b>成熟制程NAND</b>：扩产的是成熟NAND（100层以下），不是高端3D NAND。说明成熟制程产品也供不应求，价格上涨空间可能超预期。对国内存储模组厂商是利好。</p>
      <p><b class="text-yellow-400">关联标的：</b>存储芯片（长鑫科技、江波龙、佰维存储）、存储材料（雅克科技、华海诚科）、存储设备（拓荆科技、北方华创）</p>
    </div>
  </div>

  <div class="bg-gradient-to-br from-green-500/10 to-emerald-500/10 border border-green-500/30 rounded-xl p-4">
    <div class="flex items-center justify-between mb-3">
      <h4 class="text-green-300 font-semibold flex items-center gap-2"><span>🔦</span> A级催化：源杰科技43亿建半导体产业园·高端光芯片扩产</h4>
      <span class="text-xs bg-green-500/30 text-green-200 px-2 py-0.5 rounded">A级·产业</span>
    </div>
    <div class="text-xs text-white/70 space-y-2 leading-relaxed">
      <p><b class="text-yellow-400">投资计划：</b>源杰科技拟投资42.68亿元在西咸新区建设半导体科技产业园，占地约126亩，建设周期24个月。聚焦高速激光器芯片领域，突破产能瓶颈，扩大高端激光器芯片生产规模。</p>
      <p><b class="text-yellow-400">公司背景：</b>源杰科技2022年底上市，首发价100.66元/市值45亿，目前市值约1682亿元，不到4年涨36倍。今年上半年归母净利预增1197%-1305%，是A股超级大牛股之一。</p>
      <p><b class="text-yellow-400">行业影响：</b>光芯片是光通信产业链的核心环节，源杰科技作为国内高端光芯片龙头，大手笔扩产说明行业需求确实旺盛（AI数据中心800G/1.6T光模块拉动）。8月11日光通信板块逆势上涨，与光芯片需求强劲有关。</p>
      <p><b class="text-yellow-400">风险点：</b>公司货币资金逐季减少（从10.83亿降至5.67亿），43亿投资主要靠自筹和银行贷款，资金压力较大。同时正在冲刺港股IPO。</p>
      <p><b class="text-yellow-400">关联标的：</b>光芯片（源杰科技、仕佳光子、长光华芯）、光模块（中际旭创、新易盛、天孚通信）</p>
    </div>
  </div>

  <div class="bg-gradient-to-br from-yellow-500/10 to-orange-500/10 border border-yellow-500/30 rounded-xl p-4">
    <div class="flex items-center justify-between mb-3">
      <h4 class="text-yellow-300 font-semibold flex items-center gap-2"><span>🌐</span> B级催化：Perplexity 345亿收购Chrome·AI搜索挑战谷歌</h4>
      <span class="text-xs bg-yellow-500/30 text-yellow-200 px-2 py-0.5 rounded">B级·科技事件</span>
    </div>
    <div class="text-xs text-white/70 space-y-2 leading-relaxed">
      <p><b class="text-yellow-400">事件：</b>成立仅三年的AI搜索企业Perplexity AI向谷歌母公司Alphabet递交全现金收购邀约，计划斥资345亿美元收购Chrome浏览器业务。Perplexity当前估值仅180亿美元，堪称"蛇吞象"。</p>
      <p><b class="text-yellow-400">背景：</b>美国司法部反垄断诉讼已判定谷歌利用Chrome构建搜索垄断，监管层提出强制剥离Chrome的整改方案。Perplexity抓住监管窗口期抛出收购方案。</p>
      <p><b class="text-yellow-400">市场影响：</b>落地概率极低（谷歌反对+资金存疑+监管未必批准），但事件本身反映了AI搜索对传统搜索的颠覆性挑战加速。Chrome全球22.5亿用户、占65%市场份额，是谷歌流量入口的核心。</p>
      <p><b class="text-yellow-400">关联标的：</b>AI搜索/大模型（百度、科大讯飞、三六零）</p>
    </div>
  </div>

  <div class="bg-gradient-to-br from-amber-500/10 to-yellow-500/10 border border-amber-500/30 rounded-xl p-4">
    <div class="flex items-center justify-between mb-3">
      <h4 class="text-amber-300 font-semibold flex items-center gap-2"><span>🥇</span> B级催化：百亿资金涌入黄金ETF·前7月进出口超30万亿</h4>
      <span class="text-xs bg-amber-500/30 text-amber-200 px-2 py-0.5 rounded">B级·资金面</span>
    </div>
    <div class="text-xs text-white/70 space-y-2 leading-relaxed">
      <p><b class="text-yellow-400">资金数据：</b>前7个月百亿资金涌入黄金ETF，投资者对贵金属的配置需求持续上升。黄金从年初的调整到近期突破4400美元，资金流入趋势明确。</p>
      <p><b class="text-yellow-400">外贸数据：</b>前7个月我国货物贸易进出口超30万亿元，外贸韧性强。出口结构持续优化，新能源汽车、锂电池、光伏"新三样"保持高增长。</p>
      <p><b class="text-yellow-400">中报披露：</b>A股已有180家上市公司披露半年报，中报密集披露期临近。业绩超预期的公司有望获得资金关注，业绩不及预期的高位股需警惕回调风险。</p>
    </div>
  </div>
</div>'''
gen.add_section("核心题材与今日催化", catalyst_html, "🔥")

# 持仓诊断
portfolio_html = '''
<div class="space-y-4">
  <div class="bg-gradient-to-br from-yellow-500/20 to-orange-500/10 border border-yellow-500/40 rounded-xl p-4">
    <div class="flex items-center justify-between mb-3">
      <div class="flex items-center gap-2">
        <span class="bg-yellow-500 text-white text-xs px-2 py-0.5 rounded-full font-bold">持仓</span>
        <span class="text-white font-bold text-lg">铜冠铜箔 (301217)</span>
      </div>
      <div class="text-right">
        <div class="text-xl font-bold text-red-400">再创新高</div>
        <div class="text-xs text-red-400">8月11日 · +4.47%·收120.99·盘中最高126.4</div>
      </div>
    </div>
    <div class="grid md:grid-cols-3 gap-3 text-xs">
      <div class="bg-white/5 rounded-lg p-3">
        <div class="text-white/60 mb-1">最新评级</div>
        <div class="text-yellow-400 font-semibold">🟡 高位加速·逢高减仓</div>
      </div>
      <div class="bg-white/5 rounded-lg p-3">
        <div class="text-white/60 mb-1">关键价位</div>
        <div class="text-white font-semibold">压力130 / 支撑110</div>
      </div>
      <div class="bg-white/5 rounded-lg p-3">
        <div class="text-white/60 mb-1">操作建议</div>
        <div class="text-white font-semibold">125以上减仓至底仓</div>
      </div>
    </div>
    <div class="mt-3 text-xs text-white/70 leading-relaxed">
      <p><b class="text-yellow-400">📊 盘面解读</b>：铜冠铜箔周二再涨4.47%收120.99元，盘中最高126.4元再创历史新高。工业富联中报验证AI服务器需求爆发（铜箔是PCB上游核心材料），叠加存储产业链高景气，铜冠铜箔基本面持续向好。但短期涨幅过大，从7月底部累计涨幅超50%。</p>
      <p class="mt-2"><b class="text-yellow-400">🎯 催化验证</b>：工业富联中报AI服务器出货量增长2-3倍，验证PCB铜箔需求强劲。SK海力士大连扩产50%也间接验证存储产业链高景气。铜冠铜箔作为国内锂电+PCB铜箔双龙头，双重受益。</p>
      <p class="mt-2"><b class="text-yellow-400">⚡ 操作方案</b>：<br>
      ① 若冲高至125-130元区间，继续减仓至1/3底仓，锁定利润（从低点已涨50%+）；<br>
      ② 跌破115元减仓至底仓，跌破105元清仓；<br>
      ③ 工业富联业绩验证算力需求真实，但铜冠铜箔股价已反映充分，高位不追涨；<br>
      ④ 底仓可继续持有博弈中报行情（8月下旬披露），机动仓逢高兑现。</p>
    </div>
  </div>

  <div class="bg-gradient-to-br from-yellow-500/20 to-orange-500/10 border border-yellow-500/40 rounded-xl p-4">
    <div class="flex items-center justify-between mb-3">
      <div class="flex items-center gap-2">
        <span class="bg-yellow-500 text-white text-xs px-2 py-0.5 rounded-full font-bold">持仓</span>
        <span class="text-white font-bold text-lg">雅克科技 (002409)</span>
      </div>
      <div class="text-right">
        <div class="text-xl font-bold text-green-400">冲高回落</div>
        <div class="text-xs text-green-400">8月11日 · 收150.29·盘中最高156.3</div>
      </div>
    </div>
    <div class="grid md:grid-cols-3 gap-3 text-xs">
      <div class="bg-white/5 rounded-lg p-3">
        <div class="text-white/60 mb-1">最新评级</div>
        <div class="text-yellow-400 font-semibold">🟡 高位震荡·逢高减仓</div>
      </div>
      <div class="bg-white/5 rounded-lg p-3">
        <div class="text-white/60 mb-1">关键价位</div>
        <div class="text-white font-semibold">压力155-160 / 支撑142</div>
      </div>
      <div class="bg-white/5 rounded-lg p-3">
        <div class="text-white/60 mb-1">操作建议</div>
        <div class="text-white font-semibold">155以上减仓1/3</div>
      </div>
    </div>
    <div class="mt-3 text-xs text-white/70 leading-relaxed">
      <p><b class="text-yellow-400">📊 盘面解读</b>：雅克科技周二高开高走，盘中最高156.3元创反弹新高，但尾盘回落收150.29元（+4.34%），典型的冲高回落形态。SK海力士大连扩产50%对半导体材料板块情绪有支撑，但获利盘压力较大。</p>
      <p class="mt-2"><b class="text-yellow-400">🎯 核心催化</b>：①SK海力士大连NAND扩产50%，增加前驱体等材料需求；②江波龙业绩暴增验证存储产业链高景气，雅克作为上游材料间接受益；③8月26日中报披露，市场对HBM前驱体业务高度关注。</p>
      <p class="mt-2"><b class="text-yellow-400">⚡ 操作方案</b>：<br>
      ① 155-160元区间减仓1/3锁定利润，底仓保留2/3博弈中报；<br>
      ② 若受SK海力士扩产+工业富联业绩催化冲160元以上，可继续减仓至底仓；<br>
      ③ 跌破142元止盈至底仓，跌破130元全部清仓；<br>
      ④ 中报前可能有资金博弈业绩，但冲高回落说明上方压力大，不建议追高，逢高减仓为主。</p>
    </div>
  </div>

  <div class="bg-gradient-to-br from-yellow-500/20 to-orange-500/10 border border-yellow-500/40 rounded-xl p-4">
    <div class="flex items-center justify-between mb-3">
      <div class="flex items-center gap-2">
        <span class="bg-yellow-500 text-white text-xs px-2 py-0.5 rounded-full font-bold">持仓</span>
        <span class="text-white font-bold text-lg">英维克 (002837)</span>
      </div>
      <div class="text-right">
        <div class="text-xl font-bold text-green-400">继续弱势</div>
        <div class="text-xs text-green-400">8月11日 · 收54.68·跌1.18%</div>
      </div>
    </div>
    <div class="grid md:grid-cols-3 gap-3 text-xs">
      <div class="bg-white/5 rounded-lg p-3">
        <div class="text-white/60 mb-1">最新评级</div>
        <div class="text-yellow-400 font-semibold">🟡 深度套牢·反弹减仓</div>
      </div>
      <div class="bg-white/5 rounded-lg p-3">
        <div class="text-white/60 mb-1">关键价位</div>
        <div class="text-white font-semibold">压力60元 / 支撑50元</div>
      </div>
      <div class="bg-white/5 rounded-lg p-3">
        <div class="text-white/60 mb-1">操作建议</div>
        <div class="text-white font-semibold">58-60元减仓≥1/2</div>
      </div>
    </div>
    <div class="mt-3 text-xs text-white/70 leading-relaxed">
      <p><b class="text-yellow-400">📊 盘面解读</b>：英维克周二继续弱势，收54.68元跌1.18%，盘中最低54.08元。尽管CME推出算力期货（长期利好算力基础设施+液冷需求）、工业富联AI服务器出货量爆发，但液冷板块持续被资金冷落，英维克从高点回撤超60%。</p>
      <p class="mt-2"><b class="text-yellow-400">🎯 核心矛盾</b>：液冷长期逻辑不变（AI算力爆发+CME算力金融化验证需求），但短期资金偏好光通信/半导体设备/医药，液冷无人问津。英维克下降趋势未改，50元整数关岌岌可危。</p>
      <p class="mt-2"><b class="text-yellow-400">⚡ 操作方案</b>：<br>
      ① 若反弹至58-60元区间坚决减仓≥1/2，降低持仓风险；<br>
      ② 若突破60元可少量留仓博弈65元，但55元为止盈线；<br>
      ③ 跌破52元无条件减仓，跌破50元清仓，纪律第一；<br>
      ④ 严禁补仓抄底，下降趋势中任何反弹都是减仓机会。CME算力期货是长期利好，但短期救不了股价。</p>
    </div>
  </div>

  <div class="bg-gradient-to-br from-gray-500/20 to-slate-500/10 border border-gray-500/40 rounded-xl p-4">
    <div class="flex items-center justify-between mb-3">
      <div class="flex items-center gap-2">
        <span class="bg-gray-500 text-white text-xs px-2 py-0.5 rounded-full font-bold">持仓</span>
        <span class="text-white font-bold text-lg">*ST建艺 (002789)</span>
      </div>
      <div class="text-right">
        <div class="text-xl font-bold text-red-400">退市风险</div>
        <div class="text-xs text-red-400">立即清仓·不要抱幻想</div>
      </div>
    </div>
    <div class="bg-red-500/10 border border-red-500/30 rounded-lg p-3 mb-3">
      <p class="text-red-300 text-xs font-semibold">⚠️ 最高优先级：立即清仓止损，退市风险敞口必须关闭</p>
    </div>
    <div class="text-xs text-white/70 leading-relaxed">
      <p><b class="text-yellow-400">📰 最新动态</b>：*ST建艺周二微跌0.81%收10.03元，退市风险未解除。公司推进重组已提交摘帽申请但结果未知，存在重大不确定性。</p>
      <p class="mt-2"><b class="text-yellow-400">⚡ 操作策略</b>：退市风险股，任何价格立即清仓。退市风险+债务问题未消除，不要抱有任何幻想。ST股的基本面不会因为股价反弹而改善，早一天减仓少一分风险。</p>
    </div>
  </div>

  <div class="bg-white/5 rounded-xl p-4">
    <h4 class="text-white font-semibold mb-3 flex items-center gap-2"><span>📋</span> 组合总览与今日策略</h4>
    <div class="text-xs text-white/70 space-y-2 leading-relaxed">
      <p><b class="text-yellow-400">昨日表现</b>：持仓整体分化，铜冠铜箔+4.47%再创新高，雅克科技+4.34%冲高回落，英维克-1.18%继续弱势，*ST建艺微跌。铜冠/雅克贡献正收益，组合整体跑赢大盘（沪指-0.82%）。</p>
      <p><b class="text-yellow-400">今日策略（8月12日周三）：</b><br>
      ① 隔夜费半逆势涨0.87%+工业富联业绩验证+SK海力士扩产，半导体设备材料方向有修复动能，但工业富联"利好出尽"的教训要吸取，<b>不追高、逢高减仓</b>；<br>
      ② <b>铜冠铜箔</b>：再创新高但冲高回落压力大，125-130元区间继续减仓至1/3底仓；<br>
      ③ <b>雅克科技</b>：SK海力士扩产+江波龙业绩双催化，155元以上减仓1/3，中报前不追高；<br>
      ④ <b>英维克</b>：CME算力期货+工业富联AI服务器爆发是长期利好，但短期不涨，反弹到58元坚决减仓，跌破52元清仓；<br>
      ⑤ <b>*ST建艺</b>：立即清仓（最高优先级）；<br>
      ⑥ 整体仓位4-5成，结构性机会为主，关注光芯片（源杰科技扩产）和半导体设备（阿斯麦+3.8%）方向，科技股等待更好的买点。</p>
    </div>
  </div>
</div>'''
gen.add_section("持仓诊断与操作建议", portfolio_html, "💼")

# 空方视角
bear_html = '''
<div class="space-y-4">
  <div class="bg-red-500/10 border border-red-500/30 rounded-xl p-4">
    <h4 class="text-red-300 font-semibold mb-3 flex items-center gap-2"><span>🐻</span> 空方观点：科技股利好出尽·IPO抽血·高位回调风险</h4>
    <div class="text-xs text-white/70 space-y-3 leading-relaxed">
      <div class="bg-white/5 rounded-lg p-3">
        <p class="text-red-300 font-semibold mb-1">风险1：工业富联"利好出尽"，科技股业绩兑现即见顶</p>
        <p>工业富联上半年净利+96%创历史新高，但股价当日跌4.58%，市值蒸发超600亿。这是典型的"利好出尽"信号——业绩再好，只要市场已经预期到了，公布就是出货时机。江波龙暴增715倍后股价如何走？如果也是高开低走，说明科技股整体处于"利好兑现期"。</p>
      </div>
      <div class="bg-white/5 rounded-lg p-3">
        <p class="text-red-300 font-semibold mb-1">风险2：IPO密集抽血，存量博弈下老股承压</p>
        <p>宇树科技（610亿市值募资61亿）刚上市，长鑫科技（3.28万亿巨无霸）持续交易，加上源杰科技冲刺港股IPO，硬科技IPO一个接一个。8月11日沪指-0.82%、3777只股票下跌，主力资金净流出超345亿，抽血效应明显。</p>
      </div>
      <div class="bg-white/5 rounded-lg p-3">
        <p class="text-red-300 font-semibold mb-1">风险3：CPI数据前市场谨慎，美股科技七巨头下跌</p>
        <p>美国7月CPI数据今晚公布，市场观望情绪浓厚。谷歌-3.6%创近6个月最大单日跌幅，科技七巨头多数下跌。如果CPI超预期，美联储可能维持高利率更久，对科技成长股估值形成压制。</p>
      </div>
      <div class="bg-white/5 rounded-lg p-3">
        <p class="text-red-300 font-semibold mb-1">风险4：5000亿算力融资信用风险发酵</p>
        <p>英伟达联合六大金融机构设立5000亿美元算力融资平台，但市场对信用风险担忧持续。CME推出算力期货，虽然是金融创新，但也可能加剧算力市场的投机和泡沫。AI资本开支的可持续性存疑。</p>
      </div>
      <div class="bg-white/5 rounded-lg p-3">
        <p class="text-red-300 font-semibold mb-1">风险5：地缘冲突仍存变数</p>
        <p>霍尔木兹海峡僵局持续，特朗普与伊朗互相要求赔偿。WTI原油继续上涨至83.69美元，如果油价持续走高将推高通胀，影响降息节奏。地缘风险升温时，资金往往从科技成长股流向避险品种。</p>
      </div>
    </div>
  </div>

  <div class="bg-green-500/10 border border-green-500/30 rounded-xl p-4">
    <h4 class="text-green-300 font-semibold mb-3 flex items-center gap-2"><span>🐂</span> 多方反驳：业绩真实+算力金融化+国产替代三引擎</h4>
    <div class="text-xs text-white/70 space-y-2 leading-relaxed">
      <p>① <b>工业富联验证算力需求真实爆发</b>：营收+54.6%、净利+96%、AI服务器出货量2-3倍增长，这不是讲故事，是真金白银的业绩。整个算力产业链的景气度有基本面支撑，不是泡沫。</p>
      <p>② <b>CME算力期货是产业级利好</b>：算力从"资源"变成"可交易大宗商品"，这是历史性事件。期货市场的建立将吸引更多资本进入算力领域，加速AI基础设施建设，长期利好整个算力产业链。</p>
      <p>③ <b>SK海力士扩产验证存储供不应求</b>：重启停滞4年的工厂、扩产50%，说明需求端确实紧张。三大原厂产能售罄，存储涨价周期还在延续。</p>
      <p>④ <b>全球流动性宽松方向不变</b>：非农爆冷后加息周期基本结束，虽然CPI数据可能有波动，但大方向是降息。人民币持续走强（创2023年以来新高），北向资金回流趋势不变。</p>
      <p>⑤ <b>国产替代加速推进</b>：源杰科技43亿扩产高端光芯片，SK海力士大连扩产带动上游材料设备需求，大基金三期70%投向设备材料，国产替代是长期趋势。</p>
    </div>
  </div>

  <div class="bg-yellow-500/10 border border-yellow-500/30 rounded-xl p-4">
    <h4 class="text-yellow-300 font-semibold mb-2 flex items-center gap-2"><span>⚖️</span> 综合判断</h4>
    <p class="text-xs text-white/70 leading-relaxed">
      短期（1-2周）：科技股处于"业绩验证期"，工业富联的"利好出尽"效应可能扩散。隔夜费半逆势上涨给A股科技带来情绪支撑，但持续性有待观察。操作上控制仓位，逢高减仓高位股，等待中报密集披露后的布局机会。<br>
      中期（1-3个月）：算力需求真实爆发（工业富联验证）+算力金融化（CME期货）+国产替代加速，三引擎驱动科技成长股中期向好。调整后优质标的将迎来更好的布局机会。<br>
      <b class="text-yellow-400">核心结论：短期谨慎乐观，仓位4-5成，结构性机会为主。
      半导体设备材料（阿斯麦+3.8%+SK海力士扩产）和光芯片（源杰科技扩产）相对强势，
      高位股逢高减仓，关注调整到位后的优质标的。</b>
    </p>
  </div>
</div>'''
gen.add_section("空方视角与多空博弈", bear_html, "⚖️")

# 预判验证
prediction_html = '''
<div class="space-y-4">
  <div class="bg-white/5 rounded-xl p-4">
    <h4 class="text-white font-semibold mb-3 flex items-center gap-2"><span>🔮</span> 预判记录（T+N验证）</h4>
    <div class="space-y-3 text-xs">
      <div class="bg-green-500/10 border border-green-500/30 rounded-lg p-3">
        <div class="flex justify-between mb-2">
          <span class="text-green-300 font-semibold">预判#20260811-01：江波龙业绩催化存储修复</span>
          <span class="text-xs bg-green-500/30 text-green-200 px-2 py-0.5 rounded">验证中·T+1</span>
        </div>
        <p class="text-white/70">预判内容：江波龙半年净利暴增715倍+回购，将催化存储板块情绪修复，存储材料和芯片方向有望迎来3-5%的反弹。</p>
        <p class="text-white/50 mt-1">当前进度：T+1验证，雅克科技+4.34%、铜冠铜箔+4.47%，存储材料方向反弹幅度符合预期。整体验证偏正面。</p>
      </div>
      <div class="bg-yellow-500/10 border border-yellow-500/30 rounded-lg p-3">
        <div class="flex justify-between mb-2">
          <span class="text-yellow-300 font-semibold">预判#20260810-01：非农后科技股延续反弹</span>
          <span class="text-xs bg-yellow-500/30 text-yellow-200 px-2 py-0.5 rounded">验证中·T+2</span>
        </div>
        <p class="text-white/70">预判内容：非农爆冷+美股创新高后，A股科技高开但分化，光通信/半导体设备相对强势，存储冲高回落。</p>
        <p class="text-white/50 mt-1">当前进度：T+2验证，周二沪指-0.82%但创业板+0.34%，通信板块+1.13%领涨（光通信强势）。预判的"分化"和"光通信/设备强势"基本验证，但主板弱于预期。</p>
      </div>
      <div class="bg-green-500/10 border border-green-500/30 rounded-lg p-3">
        <div class="flex justify-between mb-2">
          <span class="text-green-300 font-semibold">预判#20260803-01：雅克科技跌停后3日内反弹</span>
          <span class="text-xs bg-green-500/30 text-green-200 px-2 py-0.5 rounded">已验证·正确</span>
        </div>
        <p class="text-white/70">预判内容：雅克科技跌停板机构抄底近5亿，预计3个交易日内出现5-10%反弹。</p>
        <p class="text-white/50 mt-1">实际走势：从8月4日跌停价127元反弹至最高156.3元（+23%），远超预期。验证正确，反弹力度和持续性均超预期。</p>
      </div>
      <div class="bg-green-500/10 border border-green-500/30 rounded-lg p-3">
        <div class="flex justify-between mb-2">
          <span class="text-green-300 font-semibold">预判#20260730-02：存储板块调整期2-3周</span>
          <span class="text-xs bg-green-500/30 text-green-200 px-2 py-0.5 rounded">已验证·正确</span>
        </div>
        <p class="text-white/70">预判内容：7月30日科技股大跌后，存储板块进入2-3周调整期，调整幅度约15-25%。</p>
        <p class="text-white/50 mt-1">当前进度：第10个交易日，板块从高点回调约20%后开始反弹。PCB铜箔（铜冠铜箔+50%）率先启动，存储材料（雅克科技+23%）紧随其后。时间和幅度均验证正确。</p>
      </div>
      <div class="bg-red-500/10 border border-red-500/30 rounded-lg p-3">
        <div class="flex justify-between mb-2">
          <span class="text-red-300 font-semibold">新增预判#20260812-01：算力期货催化算力产业链</span>
          <span class="text-xs bg-red-500/30 text-red-200 px-2 py-0.5 rounded">待验证·T+2</span>
        </div>
        <p class="text-white/70">预判内容：CME推出算力期货（H100/B200）是里程碑事件，将催化算力产业链情绪修复，GPU/服务器/液冷/光模块方向有望迎来2-3%的反弹，持续1-2个交易日。</p>
        <p class="text-white/50 mt-1">验证时间：8月14日（T+2）验证反弹幅度和持续性</p>
      </div>
      <div class="bg-red-500/10 border border-red-500/30 rounded-lg p-3">
        <div class="flex justify-between mb-2">
          <span class="text-red-300 font-semibold">新增预判#20260812-02：SK海力士扩产催化存储材料</span>
          <span class="text-xs bg-red-500/30 text-red-200 px-2 py-0.5 rounded">待验证·T+3</span>
        </div>
        <p class="text-white/70">预判内容：SK海力士大连NAND扩产50%，将催化半导体材料板块情绪，雅克科技、华海诚科等存储材料标的有望持续走强，中期（1-2周）涨幅5-10%。</p>
        <p class="text-white/50 mt-1">验证时间：8月15日（T+3）验证中期涨幅</p>
      </div>
    </div>
  </div>

  <div class="bg-white/5 rounded-xl p-4">
    <h4 class="text-white font-semibold mb-2 flex items-center gap-2"><span>📊</span> 准确率统计</h4>
    <div class="grid grid-cols-3 gap-3 text-center text-xs">
      <div class="bg-white/5 rounded-lg p-2">
        <div class="text-lg font-bold text-yellow-400">71%</div>
        <div class="text-white/60">总体准确率</div>
      </div>
      <div class="bg-white/5 rounded-lg p-2">
        <div class="text-lg font-bold text-green-400">12/17</div>
        <div class="text-white/60">已验证正确/总数</div>
      </div>
      <div class="bg-white/5 rounded-lg p-2">
        <div class="text-lg font-bold text-blue-400">6</div>
        <div class="text-white/60">待验证</div>
      </div>
    </div>
  </div>
</div>'''
gen.add_section("预判验证闭环", prediction_html, "🔮")

# 教训库
lesson_html = '''
<div class="space-y-3">
  <div class="bg-red-500/10 border border-red-500/30 rounded-lg p-3">
    <p class="text-red-300 font-semibold mb-1">教训#1：业绩炸≠股价涨，利好出尽是铁律</p>
    <p class="text-white/60 text-xs">
      工业富联上半年净利+96%创历史新高，但股价当日跌4.58%，市值蒸发超600亿。这是最新鲜的教训。
      江波龙暴增715倍、源杰科技预增13倍——这些"炸裂"的业绩，在股价已经涨了好几倍之后，
      公布出来就是出货的时机，不是加仓的理由。
      <b>正确做法</b>：业绩超预期但股价在高位的，不要追涨，反而考虑减仓。
      业绩好+股价在低位+没被炒作过的，才是布局机会。
      记住：市场永远在炒预期，业绩公布就是预期兑现的时候。
    </p>
  </div>

  <div class="bg-orange-500/10 border border-orange-500/30 rounded-lg p-3">
    <p class="text-orange-300 font-semibold mb-1">教训#2：高位股冲高回落=见顶信号，立即减仓</p>
    <p class="text-white/60 text-xs">
      雅克科技周二最高156.3元，收150.29元，冲高回落近6元。
      铜冠铜箔最高126.4元，收120.99元，也是冲高回落。
      在高位出现"长上影线+冲高回落"，往往是短期见顶信号，
      说明上方抛压沉重，多头力量耗尽。
      <b>正确做法</b>：高位股冲高回落当天，尾盘或次日开盘减仓，
      不要抱有"明天还会涨"的幻想。冲高回落之后，大概率要调整几天。
      减仓后等调整到位再接回来，比死扛不动更主动。
    </p>
  </div>

  <div class="bg-yellow-500/10 border border-yellow-500/30 rounded-lg p-3">
    <p class="text-yellow-300 font-semibold mb-1">教训#3：新物种≠立即涨，题材发酵需要时间</p>
    <p class="text-white/60 text-xs">
      CME推出算力期货是历史性事件，"算力=AI时代的石油"听起来很激动人心。
      但新题材、新概念从出现到市场认可，需要时间发酵。
      就像当年的NFT、元宇宙，刚出来时很多人看不懂，过了几个月才爆发。
      <b>正确做法</b>：对于"新物种"级别的事件，先加入观察池，不要第一时间冲进去。
      等市场验证（相关个股连续上涨、成交量放大、机构研报密集出现）后再跟进。
      新题材的第一个买点往往不是最低点，但却是最安全的点。
    </p>
  </div>

  <div class="bg-green-500/10 border border-green-500/30 rounded-lg p-3">
    <p class="text-green-300 font-semibold mb-1">教训#4：龙头扩产=上游受益，传导逻辑要顺</p>
    <p class="text-white/60 text-xs">
      SK海力士大连NAND扩产50%，直接利好的是半导体设备和材料，
      不是SK海力士本身（产能增加可能导致价格下跌）。
      同样，源杰科技扩产光芯片，利好的是上游的光芯片设备和材料，
      以及下游的光模块厂商（产能增加意味着供货更充足）。
      <b>正确做法</b>：遇到龙头扩产的消息，要顺着产业链找受益环节，
      不要直接买扩产的公司本身。扩产=资本开支增加=短期利润可能被摊薄，
      但上游设备材料=订单增加=业绩直接受益。
    </p>
  </div>

  <div class="bg-purple-500/10 border border-purple-500/30 rounded-lg p-3">
    <p class="text-purple-300 font-semibold mb-1">教训#5：不分红的"铁公鸡"要警惕</p>
    <p class="text-white/60 text-xs">
      工业富联上半年赚237亿，但一分钱不分红，评论区炸锅。
      "一边日赚1.3亿，一边中期一毛不拔"，市场用脚投票（股价跌4.58%）。
      不分红的公司，赚的钱是不是真的？是用来再投资还是拿去干别的？
      投资者心里打鼓，股价就会有压力。
      <b>正确做法</b>：对于长期不分红的"铁公鸡"公司，即使业绩再好，
      也要保持警惕。利润不分红=股东拿不到真金白银，
      只能靠股价上涨赚钱，一旦增长不及预期，股价就会戴维斯双杀。
    </p>
  </div>

  <div class="bg-blue-500/10 border border-blue-500/30 rounded-lg p-3">
    <p class="text-blue-300 font-semibold mb-1">教训#6：权重股跌≠行情结束，看创业板指</p>
    <p class="text-white/60 text-xs">
      周二沪指-0.82%（5连阳终结），但创业板+0.34%，
      3777只股票下跌但通信、医药、机器人等成长赛道逆势上涨。
      很多人一看到沪指跌就慌了，以为行情结束了，
      但其实只是市场风格在切换——从权重蓝筹向成长股切换。
      <b>正确做法</b>：不要只看沪指，要看创业板指和科创板指数。
      科技成长股的行情，创业板指比沪指更有参考价值。
      如果沪指跌但创业板涨，说明不是系统性风险，只是风格轮动。
    </p>
  </div>
</div>'''
gen.add_section("教训库引用", lesson_html, "📚")

# 生成+发布
output_path = os.path.join(WORK_DIR, 'docs/daily/20260812_每日新闻洞察.html')
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
