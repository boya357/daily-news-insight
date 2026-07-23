#!/usr/bin/env python3
"""2026年7月23日 每日新闻洞察生成 - 周四·特斯拉Q2盈利不及预期盘后大跌·油价暴涨布油94美元·A股科技分化杀跌·油气贵金属领涨·政策底持续托底·持仓继续分化"""
import sys, os, shutil, json
WORK_DIR = '/root/daily-news-insight'
sys.path.insert(0, os.path.join(WORK_DIR, 'v3'))
from generators.daily_pro import DailyReportProGenerator

gen = DailyReportProGenerator(
    date_str='2026年7月23日', weekday='星期四',
    subtitle='2026年7月23日 星期四 · 特斯拉Q2营收超预期盈利大降盘后跌5%·油价暴涨布油94美元·美联储加息预期升温·A股科技分化杀跌创业板-3.24%·油气贵金属领涨·政策底持续托底 · 持仓：雅克+4.4%铜冠-11.33%',
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

# ========== 1. 隔夜全球市场 ==========
gen.add_global_market()

global_cards1 = render_cards([
    {"name":"道琼斯","change":"-0.01%","up":False},
    {"name":"标普500","change":"-0.14%","up":False},
    {"name":"纳斯达克","change":"-0.57%","up":False},
    {"name":"费城半导体","change":"+0.44%","up":True},
    {"name":"恒生指数","change":"-0.95%","up":False},
    {"name":"日经225","change":"-0.90%","up":False},
])
global_list1 = render_list([
    {"name":"WTI原油","change":"+2.95%/86.83","up":True},
    {"name":"布伦特原油","change":"+3.36%/94.07","up":True},
    {"name":"COMEX黄金","change":"+1.44%/4135","up":True},
    {"name":"COMEX白银","change":"+1.57%/60.03","up":True},
])
global_list2 = render_list([
    {"name":"三星电子","change":"+2.88%","up":True},
    {"name":"SK海力士","change":"+4.21%","up":True},
    {"name":"三星SDI","change":"+0.24%","up":True},
    {"name":"LG新能源","change":"+0.78%","up":True},
])
global_list3 = render_list([
    {"name":"英伟达","change":"+2.30%","up":True},
    {"name":"博通","change":"+2.67%","up":True},
    {"name":"美光科技","change":"-1.17%","up":False},
    {"name":"AMD","change":"+1.45%","up":True},
    {"name":"英特尔","change":"-2.68%","up":False},
    {"name":"台积电ADR","change":"-0.80%","up":False},
])
global_html = '''
<div class="grid md:grid-cols-3 gap-4">
  <div class="md:col-span-2">
    <div class="text-white font-semibold mb-3 flex items-center gap-2"><span>🌍</span><span>隔夜全球市场 · 油价暴涨通胀担忧再起·科技股分化·加息预期升温</span></div>
    <div class="grid grid-cols-3 md:grid-cols-6 gap-2">{0}</div>
    <p class="text-xs text-white/50 mt-3 leading-relaxed">
      ⚡ <b class="text-yellow-400">核心要点：美股三大指数小幅收跌，油价暴涨引发通胀担忧，科技股分化加剧</b>——<br>
      ①<b>油价暴力拉升：布伦特原油暴涨3.36%至94.07美元/桶，创一个多月新高，WTI涨2.95%至86.83美元。中东地缘冲突持续发酵，特朗普威胁轰炸伊朗民用设施，伊朗反击称不允许一滴石油出口地区。油价上涨直接推升通胀预期，美联储9月加息概率升至80%，2年期美债收益率创2025年2月以来新高。<br>
      ②<b>特斯拉Q2财报爆雷</b>：营收282.4亿美元（+26%超预期），但调整后EPS仅0.33美元（低于预期0.51美元，-35%），营业利润率1.4%暴跌57%，毛利率16.8%不及预期。盘后大跌4-5%。马斯克称扩大Optimus产能将面临困难，TeraFab芯片厂选址即将公布。<br>
      ③<b>科技股分化</b>：费半逆势涨0.44%三连阳，英伟达+2.3%/博通+2.67%/超微电脑+19.84%（上调毛利率指引）强势；但存储芯片普跌，美光-1.17%/SK海力士ADR-3.88%（盘后反弹4%）。谷歌盘后跌约4%，虽然云业务收入暴增82%但上调资本开支指引至1950-2050亿美元引发利润率担忧。<br>
      ④<b>黄金白银大涨</b>：避险需求+通胀预期双轮驱动，COMEX黄金+1.44%至4135美元/盎司，白银+1.57%。地缘冲突+美债收益率走高的背景下黄金不跌反涨，显示市场避险情绪浓厚。<br>
      ⑤<b>A股影响</b>：隔夜美股走弱+油价上涨+加息预期升温，对A股科技成长股形成压制；但油气/贵金属/煤炭板块有望延续强势。政策底+北京国管百亿进场托底，系统性风险可控，但科技股分化调整压力仍大。
    </p>
  </div>
  <div class="space-y-4">
    <div>
    <div class="text-white font-semibold mb-3 flex items-center gap-2"><span>🛢️</span><span>大宗商品（暴涨）</span></div>
      <div class="bg-white/5 rounded-lg p-3">{1}</div></div>
    <div>
    <div class="text-white font-semibold mb-3 flex items-center gap-2"><span>🇰🇷</span><span>韩股核心（三星/海力士强）</span></div>
      <div class="bg-white/5 rounded-lg p-3">{2}</div></div>
    <div>
    <div class="text-white font-semibold mb-3 flex items-center gap-2"><span>💻</span><span>美股科技龙头（分化）</span></div>
      <div class="bg-white/5 rounded-lg p-3">{3}</div></div>
  </div>
</div>'''.format(global_cards1, global_list1, global_list2, global_list3)
gen.add_section("隔夜全球市场深度解读", global_html, "🌍")

# ========== 2. 昨日A股复盘 ==========
ashare_html = '''
<div class="space-y-4">
<div class="grid md:grid-cols-4 gap-3">
  <div class="bg-gradient-to-br from-red-500/20 to-orange-500/10 border border-red-500/30 rounded-xl p-3 text-center">
    <div class="text-xs text-white/60 mb-1">上证指数</div>
    <div class="text-xl font-bold text-red-400">3867.03</div>
    <div class="text-xs text-red-400 mt-1">+0.07% / 护盘权重</div>
  </div>
  <div class="bg-gradient-to-br from-green-500/20 to-emerald-500/10 border border-green-500/30 rounded-xl p-3 text-center">
    <div class="text-xs text-white/60 mb-1">深证成指</div>
    <div class="text-xl font-bold text-green-400">14061.44</div>
    <div class="text-xs text-green-400 mt-1">-1.42%</div>
  </div>
  <div class="bg-gradient-to-br from-green-500/20 to-emerald-500/10 border border-green-500/30 rounded-xl p-3 text-center">
    <div class="text-xs text-white/60 mb-1">创业板指</div>
    <div class="text-xl font-bold text-green-400">3566.73</div>
    <div class="text-xs text-green-400 mt-1">-3.24% / 科技杀跌</div>
  </div>
  <div class="bg-gradient-to-br from-yellow-500/20 to-amber-500/10 border border-yellow-500/30 rounded-xl p-3 text-center">
    <div class="text-xs text-white/60 mb-1">成交额</div>
    <div class="text-xl font-bold text-yellow-400">2.65万亿</div>
    <div class="text-xs text-white/60 mt-1">缩量3000亿</div>
  </div>
</div>
<div class="bg-white/5 rounded-xl p-4">
  <h4 class="text-white font-semibold mb-3 text-sm">📊 周三（7/22）A股复盘：极致分化·沪指红个股绿·油气贵金属领涨·科技成长杀跌</h4>
  <div class="grid md:grid-cols-2 gap-4 text-xs">
    <div>
      <p class="text-white/80 font-semibold mb-2">📈 最强方向</p>
      <p class="text-white/60 leading-relaxed mb-2">
      <b class="text-yellow-400">①贵金属/黄金</b>：国际金价突破4100美元，避险+通胀预期双驱动，黄金股全线大涨。<br>
      <b class="text-yellow-400">②油气开采/煤炭</b>：油价暴涨+地缘冲突，油气煤炭等能源股领涨两市。<br>
      ③电力/公用事业：防御属性+夏季用电高峰，电力板块逆势走强。<br>
      ④雅克科技+4.4%：半导体材料相对抗跌，地天板后延续强势。
      </p>
    </div>
    <div>
      <p class="text-white/80 font-semibold mb-2">📉 相对弱势</p>
      <p class="text-white/60 leading-relaxed mb-2">
      <b class="text-green-400">①创业板/科创50</b>：创业板-3.24%、科创50-2.26%，科技成长股集体杀跌。<br>
      <b>②存储/PCB/半导体设备</b>：铜冠铜箔-11.33%接近20cm跌停，存储板块再度崩盘，中报业绩证伪逻辑发酵。<br>
      ③游戏/传媒/自动化设备：跌幅居前，资金从成长撤出转向防御。<br>
      <b class="text-yellow-400">特征</b>：超3800只个股下跌，涨跌比约1:2.5，成交额缩量至2.65万亿（缩量3000亿），
      恐惧贪婪指数从45回落至22（恐惧），典型"指数红、账户绿"的极致分化行情。
      </p>
    </div>
  </div>
  <p class="text-xs text-white/50 mt-3 leading-relaxed">
    ⚡ <b class="text-yellow-400">盘口解读：</b>周三是典型的"政策底护盘+获利兑现"行情，沪指靠资源/金融权重守住3867点，
    但深市继续杀跌，创业板暴跌3.24%。昨日科创50暴涨10.73%后次日就分化杀跌，说明<b>反弹而非反转</b>。
    资金从科技成长撤出转向能源/贵金属/电力等防御板块，存量博弈特征明显。
    <b class="text-yellow-400">关键信号：缩量3000亿说明追高意愿不足，3800点支撑需继续考验。</b>
    但政策底明确（北京国管百亿进场+证监会维稳+保险资管净买入），
    系统性大跌空间有限，但结构性风险仍在科技成长股。
  </p>
</div>
</div>'''
gen.add_section("昨日A股复盘（7/22）", ashare_html, "📈")

# ========== 3. 今日重磅新闻 ==========
news_items = [
    {"tag":"🛢️","title":"油价暴涨布油94美元 中东地缘冲突升级","content":"布伦特原油暴涨3.36%至94.07美元/桶，创一个多月新高。特朗普威胁轰炸伊朗民用设施，伊朗反击称不允许地区出口一滴石油。油价上涨推升通胀预期，美联储9月加息概率升至80%。2年期美债收益率创2025年2月以来新高。","source":"新华社/财联社"},
    {"tag":"🚗","title":"特斯拉Q2盈利不及预期 盘后大跌5%","content":"特斯拉Q2营收282.4亿美元（+26%超预期），但调整后EPS仅0.33美元（低于预期0.51美元，-35%），营业利润率1.4%暴跌57%，毛利率16.8%不及预期。马斯克称扩大Optimus产能面临困难，TeraFab芯片厂选址即将公布。资本支出将超250亿美元。","source":"新浪财经/证券时报"},
    {"tag":"🏛️","title":"证监会主席吴清会见加拿大养老基金 释放维稳信号","content":"证监会主席吴清在京会见加拿大养老基金投资公司总裁格雷厄姆，表示坚决维护资本市场平稳健康运行，持续提升外资参与便利度。北京国管累计投入近百亿元布局股票市场。保险资管单日百亿元级净买入。政策底信号持续强化。","source":"中国证券报"},
    {"tag":"🌐","title":"谷歌Q2云业务收入暴增82% 上调资本开支指引","content":"Alphabet Q2营收1198亿美元（+24%超预期），云业务收入同比暴增82%。但公司将2026年资本开支指引从1800-1900亿上调至1950-2050亿美元，引发利润率压缩担忧。盘后跌约3-4%。合同积压规模突破5000亿美元。","source":"每日经济新闻"},
    {"tag":"📡","title":"东方空间引力一号首次远海发射成功","content":"引力一号遥四运载火箭在东海海域发射成功，标志着引力一号正式迈入规模化商业运营阶段。公司年内还计划实施三次卫星批量发射任务。商业航天产业链迎来持续性催化。","source":"金融界"},
    {"tag":"⚡","title":"中际旭创启动港股招股 最高募资624亿港元","content":"全球高速光模块龙头中际旭创正式开启H股公开发售，本次募资最高可达约624亿港元（约80亿美元），有望成为港股今年最大规模IPO。资金重点投向高速光互连技术研发和全球产能扩张。","source":"证券时报"},
]

news_cards = ''
for n in news_items:
    news_cards += '''
    <div class="bg-white/5 hover:bg-white/10 border border-white/10 rounded-xl p-4 transition-all duration-300">
      <div class="flex items-start gap-3">
        <span class="text-2xl">%s</span>
        <div class="flex-1">
          <h4 class="text-white font-semibold text-sm mb-1">%s</h4>
          <p class="text-white/60 text-xs leading-relaxed">%s</p>
          <p class="text-white/30 text-xs mt-2">来源：%s</p>
        </div>
      </div>
    </div>''' % (n['tag'], n['title'], n['content'], n['source'])

gen.add_section("今日重磅新闻", '<div class="space-y-3">%s</div>' % news_cards, "📰")

# ========== 4. 核心题材动态 ==========
topic_cards = '''
<div class="bg-gradient-to-br from-amber-500/20 to-yellow-500/10 border border-amber-500/30 rounded-xl p-4">
  <div class="flex items-center gap-2 mb-3">
    <span class="text-2xl">🛢️</span>
    <h4 class="text-white font-bold">油气/煤炭/贵金属</h4>
    <span class="bg-red-500/30 text-red-300 text-xs px-2 py-0.5 rounded-full">🔥 最强</span>
  </div>
  <p class="text-white/70 text-xs leading-relaxed mb-2">
    <b class="text-yellow-400">油价暴涨+地缘冲突升级</b>：布油94美元创一个多月新高，中东局势持续紧张。
    特朗普威胁轰炸伊朗民用设施，伊朗反击威胁封锁石油出口。
    黄金突破4135美元，避险+通胀双驱动。
    美联储加息预期升温，9月加息概率升至80%。
    能源/贵金属板块成为资金避风港。
  </p>
  <p class="text-white/50 text-xs">
    📌 A股受益：中国石油、中国海油、陕西煤业、山东黄金、紫金矿业等。
  </p>
</div>

<div class="bg-gradient-to-br from-purple-500/20 to-indigo-500/10 border border-purple-500/30 rounded-xl p-4">
  <div class="flex items-center gap-2 mb-3">
    <span class="text-2xl">💾</span>
    <h4 class="text-white font-bold">存储芯片/HBM</h4>
    <span class="bg-green-500/30 text-green-300 text-xs px-2 py-0.5 rounded-full">📉 调整</span>
  </div>
  <p class="text-white/70 text-xs leading-relaxed mb-2">
    <b class="text-green-400">存储板块再度杀跌</b>：铜冠铜箔-11.33%接近20cm跌停，
    美光科技-1.17%，SK海力士ADR-3.88%（盘后反弹4%）。
    中报业绩证伪逻辑发酵，前期涨幅过大的标的估值回调压力大。
    但中期存储涨价逻辑未破，谷歌云业务爆发+AI算力需求支撑长期向上。
  </p>
  <p class="text-white/50 text-xs">
    📌 关注：雅克科技（材料相对抗跌）、兆易创新、长电科技、通富微电。
  </p>
</div>

<div class="bg-gradient-to-br from-blue-500/20 to-cyan-500/10 border border-blue-500/30 rounded-xl p-4">
  <div class="flex items-center gap-2 mb-3">
    <span class="text-2xl">🤖</span>
    <h4 class="text-white font-bold">人形机器人</h4>
    <span class="bg-yellow-500/30 text-yellow-300 text-xs px-2 py-0.5 rounded-full">⭐ 观察</span>
  </div>
  <p class="text-white/70 text-xs leading-relaxed mb-2">
    <b class="text-yellow-400">特斯拉Q2财报提及Optimus进展</b>：马斯克称扩大Optimus产能将面临困难，
    TeraFab芯片制造设施选址即将公布，对扩大Optimus生产规模至关重要。
    已为奥斯汀开发晶圆厂订购设备。Optimus量产进度低于市场预期，
    对人形机器人板块形成短期压制，但长期逻辑未破。
  </p>
  <p class="text-white/50 text-xs">
    📌 核心标的：三花智控、拓普集团、绿的谐波、鸣志电器。
  </p>
</div>

<div class="bg-gradient-to-br from-cyan-500/20 to-teal-500/10 border border-cyan-500/30 rounded-xl p-4">
  <div class="flex items-center gap-2 mb-3">
    <span class="text-2xl">🧊</span>
    <h4 class="text-white font-bold">AI算力/液冷散热</h4>
    <span class="bg-yellow-500/30 text-yellow-300 text-xs px-2 py-0.5 rounded-full">📌 观望</span>
  </div>
  <p class="text-white/70 text-xs leading-relaxed mb-2">
    <b class="text-yellow-400">谷歌上调资本开支至1950-2050亿美元</b>：云业务收入暴增82%，
    AI算力需求持续超预期，长期景气度向上。
    但短期科技股整体调整，液冷板块跟随大盘回调。
    英伟达+2.3%逆势上涨，显示算力龙头仍受资金青睐。
    中际旭创港股招股最高624亿港元，光模块需求强劲。
  </p>
  <p class="text-white/50 text-xs">
    📌 核心标的：英维克（液冷）、中际旭创（光模块）、寒武纪、海光信息。
  </p>
</div>
'''
gen.add_section("核心题材动态", '<div class="grid md:grid-cols-2 gap-4">%s</div>' % topic_cards, "🔥")

# ========== 5. 今日/本周关键催化剂 ==========
catalyst_cards = '''
<div class="bg-white/5 rounded-xl p-4 border border-white/10">
  <div class="flex items-center gap-2 mb-3">
    <span class="bg-red-500/20 text-red-300 text-xs px-2 py-1 rounded">今日</span>
    <h4 class="text-white font-semibold text-sm">7月23日（周四）</h4>
  </div>
  <ul class="text-white/60 text-xs space-y-2">
    <li>🔴 特斯拉Q2财报解读（盘后已发布，关注Optimus量产进度+毛利率）</li>
    <li>🔴 谷歌Q2财报解读（云业务+资本开支指引，催化算力产业链）</li>
    <li>🟡 东方空间引力一号远海发射成功（商业航天催化）</li>
    <li>🟡 中际旭创港股招股启动（光模块/算力需求验证）</li>
    <li>🟡 体育强国"十五五"规划发布（体育产业催化）</li>
  </ul>
</div>

<div class="bg-white/5 rounded-xl p-4 border border-white/10">
  <div class="flex items-center gap-2 mb-3">
    <span class="bg-yellow-500/20 text-yellow-300 text-xs px-2 py-1 rounded">本周</span>
    <h4 class="text-white font-semibold text-sm">7月24-25日</h4>
  </div>
  <ul class="text-white/60 text-xs space-y-2">
    <li>🔴 7/24 英特尔/德州仪器财报（PC/数据中心芯片景气度）</li>
    <li>🔴 7/25 微软/苹果财报（科技巨头财报高峰）</li>
    <li>🟡 中报预告密集披露期（业绩驱动行情展开）</li>
    <li>🟡 中东局势演变（霍尔木兹海峡/红海航运）</li>
    <li>⚠️ 美联储7/29-30议息会议临近（加息预期升温）</li>
  </ul>
</div>

<div class="bg-white/5 rounded-xl p-4 border border-white/10">
  <div class="flex items-center gap-2 mb-3">
    <span class="bg-purple-500/20 text-purple-300 text-xs px-2 py-1 rounded">本月</span>
    <h4 class="text-white font-semibold text-sm">7月下旬核心日历</h4>
  </div>
  <ul class="text-white/60 text-xs space-y-2">
    <li>⭐ 7/29-30 美联储议息会议（加息概率飙升至80%！）</li>
    <li>⭐ 中报业绩密集披露期（7/25-8/15高峰）</li>
    <li>⭐ 长鑫科技IPO后续进展（巨额资金解冻回流）</li>
    <li>⚠️ 中东局势演变（油价/通胀/加息连锁反应）</li>
    <li>⚠️ 日本央行政策动向（日元贬值干预风险）</li>
  </ul>
</div>

<div class="bg-gradient-to-br from-red-500/20 to-orange-500/10 border border-red-500/30 rounded-xl p-4">
  <div class="flex items-center gap-2 mb-3">
    <span class="text-xl">⚡</span>
    <h4 class="text-white font-semibold text-sm">今日核心催化评级</h4>
  </div>
  <div class="space-y-2 text-xs">
    <div class="flex justify-between items-center">
      <span class="text-white/70">油气/贵金属（油价暴涨+地缘冲突）</span>
      <span class="text-red-400 font-bold">S级</span>
    </div>
    <div class="w-full bg-white/10 rounded-full h-1.5">
      <div class="bg-gradient-to-r from-red-500 to-orange-500 h-1.5 rounded-full" style="width: 95%"></div>
    </div>
    <div class="flex justify-between items-center mt-2">
      <span class="text-white/70">政策维稳（北京国管百亿+证监会维稳）</span>
      <span class="text-orange-400 font-bold">A级</span>
    </div>
    <div class="w-full bg-white/10 rounded-full h-1.5">
      <div class="bg-gradient-to-r from-orange-500 to-yellow-500 h-1.5 rounded-full" style="width: 80%"></div>
    </div>
    <div class="flex justify-between items-center mt-2">
      <span class="text-white/70">AI算力（谷歌云暴增82%+资本开支上调</span>
      <span class="text-yellow-400 font-bold">A级</span>
    </div>
    <div class="w-full bg-white/10 rounded-full h-1.5">
      <div class="bg-gradient-to-r from-yellow-500 to-amber-500 h-1.5 rounded-full" style="width: 75%"></div>
    </div>
  </div>
</div>
'''
gen.add_section("今日/本周关键催化剂", '<div class="grid md:grid-cols-2 gap-4">%s</div><p class="text-xs text-white/40 mt-4">💡 7月核心变量：油价暴涨→通胀→美联储加息预期升温（核心变量已从降息预期转向加息！）、中报业绩验证（决定科技股调整深度）、中东地缘风险（油价/通胀/加息连锁反应）、国内政策组合拳（维稳力度）。能源/防御为当前最强主线，科技成长需等待调整充分后再布局。</p>' % catalyst_cards, "📅")

# ========== 6. 持仓专项分析 ==========
portfolio_html = '''
<div class="grid md:grid-cols-2 gap-4">
  <!-- 英维克 -->
  <div class="bg-gradient-to-br from-orange-500/20 to-yellow-500/10 border border-orange-500/30 rounded-xl p-4">
    <div class="flex items-center justify-between mb-3">
      <div class="flex items-center gap-2">
        <span class="text-2xl">🧊</span>
        <div>
          <h4 class="text-white font-bold">英维克 (002837)</h4>
          <p class="text-white/50 text-xs">液冷龙头 · AI算力基础设施</p>
        </div>
      </div>
      <span class="bg-red-500/30 text-red-300 text-xs px-2 py-1 rounded-full">+0.87%</span>
    </div>
    <div class="grid grid-cols-3 gap-2 text-center mb-3 text-xs">
      <div><div class="text-white/50">现价</div><div class="text-white font-bold">60.51</div></div>
      <div><div class="text-white/50">成本</div><div class="text-white/70">104.23</div></div>
      <div><div class="text-white/50">浮亏</div><div class="text-red-400 font-bold">-41.9%</div></div>
    </div>
    <div class="space-y-2 text-xs">
      <p class="text-white/60">
        <b class="text-yellow-400">最新动态：</b>7/22+0.87%收60.51元，昨日V反后今日窄幅震荡，最高64.24最低58.69，振幅9.2%，
        多空博弈激烈。65元下方仍属弱势区间。
        主力资金净流出0.95亿，昨日反弹资金今日兑现离场。
        谷歌云业务暴增82%+上调资本开支，长期液冷需求景气度向上，但短期跟随科技板块整体调整。
      </p>
      <p class="text-white/60">
        <b class="text-yellow-400">催化：</b>谷歌云+英伟达+资本开支上调→AI算力需求确认；
        中际旭创港股招股→光模块/算力需求验证。
      </p>
      <p class="text-red-300 bg-red-500/10 rounded p-2">
        ⚠️ <b>风险提示：</b>深度破止损-41.9%，下降趋势未根本扭转，
        一季报净利-81.97%（汇兑损失+成本上升）。
        <b>反弹65-70元坚决减仓≥1/2，二次破58元无条件清仓</b>。
      </p>
    </div>
  </div>

  <!-- 铜冠铜箔 -->
  <div class="bg-gradient-to-br from-amber-500/20 to-orange-500/10 border border-amber-500/30 rounded-xl p-4">
    <div class="flex items-center justify-between mb-3">
      <div class="flex items-center gap-2">
        <span class="text-2xl">🔶</span>
        <div>
          <h4 class="text-white font-bold">铜冠铜箔 (301217)</h4>
          <p class="text-white/50 text-xs">高频高速铜箔 · AI服务器PCB</p>
        </div>
      </div>
      <span class="bg-green-500/30 text-green-300 text-xs px-2 py-1 rounded-full">-11.33%</span>
    </div>
    <div class="grid grid-cols-3 gap-2 text-center mb-3 text-xs">
      <div><div class="text-white/50">现价</div><div class="text-white font-bold">95.36</div></div>
      <div><div class="text-white/50">成本</div><div class="text-white/70">87.16</div></div>
      <div><div class="text-white/50">浮盈</div><div class="text-green-400 font-bold">+9.4%</div></div>
    </div>
    <div class="space-y-2 text-xs">
      <p class="text-white/60">
        <b class="text-yellow-400">最新动态：</b>7/22暴跌-11.33%收95.36元，从107.54直接砸穿100元关口，接近20cm跌停，成交巨量。
        存储/PCB板块再度崩盘，中报业绩证伪逻辑发酵。
        浮盈从+23.4%快速缩水至+9.4%，利润回吐过半。
        技术形态彻底走坏，短期趋势逆转信号明确。
      </p>
      <p class="text-white/60">
        <b class="text-yellow-400">催化：</b>AI算力需求爆发→HVLP铜箔供不应求；
        高频高速铜箔量价齐升（中期逻辑仍在）。
      </p>
      <p class="text-red-300 bg-red-500/10 rounded p-2">
        ⚠️ <b>风险提示：</b>接近20cm跌停后技术形态恶化，存储/PCB板块系统性回调，
        中报业绩证伪的负面催化集中释放。
        <b>反弹100-105元坚决减仓至底仓，破90元止盈全部离场</b>。
        估值偏高（动态PE仍高），需警惕进一步回调风险。
      </p>
    </div>
  </div>

  <!-- 雅克科技 -->
  <div class="bg-gradient-to-br from-purple-500/20 to-indigo-500/10 border border-purple-500/30 rounded-xl p-4">
    <div class="flex items-center justify-between mb-3">
      <div class="flex items-center gap-2">
        <span class="text-2xl">🔬</span>
        <div>
          <h4 class="text-white font-bold">雅克科技 (002409)</h4>
          <p class="text-white/50 text-xs">半导体材料平台 · 前驱体+光刻胶</p>
        </div>
      </div>
      <span class="bg-red-500/30 text-red-300 text-xs px-2 py-1 rounded-full">+4.40%</span>
    </div>
    <div class="grid grid-cols-3 gap-2 text-center mb-3 text-xs">
      <div><div class="text-white/50">现价</div><div class="text-white font-bold">149.86</div></div>
      <div><div class="text-white/50">成本</div><div class="text-white/70">108.80</div></div>
      <div><div class="text-white/50">浮盈</div><div class="text-green-400 font-bold">+37.7%</div></div>
    </div>
    <div class="space-y-2 text-xs">
      <p class="text-white/60">
        <b class="text-yellow-400">最新动态：</b>7/22+4.40%收149.86元，地天板后今日冲高回落，最高158元后回落，
        150元关口多空激战。半导体材料相对抗跌，在科技股普跌中表现强势。
        浮盈扩大至+37.7%，成为持仓中最赚钱标的。
      </p>
      <p class="text-white/60">
        <b class="text-yellow-400">催化：</b>存储芯片中期涨价逻辑→前驱体需求旺盛；
        HBM4量产推进→先进封装材料受益；
        半导体材料国产替代加速。
      </p>
      <p class="text-yellow-300 bg-yellow-500/10 rounded p-2">
        ⚡ <b>操作策略：</b>科技股分化中相对强势，但整体板块系统性风险下难独善其身。
        <b>150-155元减仓1/3锁利，破140元止盈减仓</b>。
        第一支撑140元，第二支撑130元（跌破则修复逻辑不成立）。
      </p>
    </div>
  </div>

  <!-- *ST建艺 -->
  <div class="bg-gradient-to-br from-gray-500/20 to-slate-500/10 border border-gray-500/30 rounded-xl p-4">
    <div class="flex items-center justify-between mb-3">
      <div class="flex items-center gap-2">
        <span class="text-2xl">⚠️</span>
        <div>
          <h4 class="text-white font-bold">*ST建艺 (002789)</h4>
          <p class="text-white/50 text-xs">退市风险 · 坚决清仓</p>
        </div>
      </div>
      <span class="bg-green-500/30 text-green-300 text-xs px-2 py-1 rounded-full">-3.92%</span>
    </div>
    <div class="grid grid-cols-3 gap-2 text-center mb-3 text-xs">
      <div><div class="text-white/50">现价</div><div class="text-white font-bold">8.08</div></div>
      <div><div class="text-white/50">成本</div><div class="text-white/70">13.45</div></div>
      <div><div class="text-white/50">浮亏</div><div class="text-red-400 font-bold">-39.9%</div></div>
    </div>
    <div class="space-y-2 text-xs">
      <p class="text-white/60">
        <b class="text-yellow-400">最新动态：</b>7/22继续下跌-3.92%收8.08元，再创调整新低，
        流动性枯竭，退市风险股被市场彻底抛弃。
        浮亏扩大至-39.9%。上半年预亏1.1-1.6亿，净资产仍为负，退市风险未解除。
      </p>
      <p class="text-white/60">
        <b class="text-red-400">负面催化：</b>227场官司、40亿债务压顶；
        庭外重组推进中但不确定性极大；
        市场风险偏好下降时ST股首当其冲被抛售。
      </p>
      <p class="text-red-300 bg-red-500/10 rounded p-2">
        🚫 <b>操作建议：坚决清仓，一股不留</b>。
        ST股=风险敞口，退市即归零。浮亏-39.9%虽痛，
        但继续持有可能血本无归。
        <b>任何价格都是离场机会</b>，将资金腾挪至确定性更高的标的。
      </p>
    </div>
  </div>
</div>

<!-- 持仓总览 -->
<div class="mt-4 bg-white/5 rounded-xl p-4 border border-white/10">
  <div class="flex items-center justify-between mb-3">
    <h4 class="text-white font-semibold">📊 持仓总览与操作建议</h4>
    <span class="text-xs text-yellow-400">整体仓位：建议控制在1成以内</span>
  </div>
  <div class="overflow-x-auto">
    <table class="w-full text-xs">
      <thead>
        <tr class="border-b border-white/10">
          <th class="text-left py-2 text-white/70 font-medium">标的</th>
          <th class="text-right py-2 text-white/70 font-medium">现价</th>
          <th class="text-right py-2 text-white/70 font-medium">浮盈亏</th>
          <th class="text-right py-2 text-white/70 font-medium">风险等级</th>
          <th class="text-left py-2 text-white/70 font-medium">操作建议</th>
        </tr>
      </thead>
      <tbody class="text-white/60">
        <tr class="border-b border-white/5">
          <td class="py-2">英维克</td>
          <td class="text-right">60.51</td>
          <td class="text-right text-red-400">-41.9%</td>
          <td class="text-right text-red-400">🔴 止损破位</td>
          <td class="py-2">反弹65-70减仓≥1/2，破58清仓</td>
        </tr>
        <tr class="border-b border-white/5">
          <td class="py-2">铜冠铜箔</td>
          <td class="text-right">95.36</td>
          <td class="text-right text-green-400">+9.4%</td>
          <td class="text-right text-red-400">🔴 趋势逆转</td>
          <td class="py-2">100-105减仓至底仓，破90止盈</td>
        </tr>
        <tr class="border-b border-white/5">
          <td class="py-2">雅克科技</td>
          <td class="text-right">149.86</td>
          <td class="text-right text-green-400">+37.7%</td>
          <td class="text-right text-yellow-400">🟡 相对强势</td>
          <td class="py-2">150-155减仓1/3锁利，破140止盈</td>
        </tr>
        <tr>
          <td class="py-2">*ST建艺</td>
          <td class="text-right">8.08</td>
          <td class="text-right text-red-400">-39.9%</td>
          <td class="text-right text-red-400">🔴 退市风险</td>
          <td class="py-2">🚫 坚决清仓，任何价格离场</td>
        </tr>
      </tbody>
    </table>
  </div>
</div>
'''
gen.add_section("持仓专项分析（4只）", portfolio_html, "💼")

# ========== 7. 预判验证闭环 ==========
verify_html = '''
<div class="space-y-4">
  <div class="bg-gradient-to-r from-blue-500/20 to-purple-500/20 border border-blue-500/30 rounded-xl p-4">
    <div class="flex items-center justify-between mb-3">
      <h4 class="text-white font-semibold flex items-center gap-2">
        <span>📊</span> 预判准确率统计
      </h4>
      <div class="flex items-center gap-4 text-xs">
        <div><span class="text-white/50">当前等级：</span><span class="text-yellow-400 font-bold">🥇 A级分析师</span></div>
        <div><span class="text-white/50">准确率：</span><span class="text-green-400 font-bold">待更新</span></div>
      </div>
    </div>
    <div class="grid grid-cols-4 gap-2 text-center text-xs">
      <div class="bg-white/5 rounded-lg p-2">
        <div class="text-white/50">总预判</div>
        <div class="text-white font-bold text-lg">14</div>
      </div>
      <div class="bg-white/5 rounded-lg p-2">
        <div class="text-white/50">正确</div>
        <div class="text-green-400 font-bold text-lg">6</div>
      </div>
      <div class="bg-white/5 rounded-lg p-2">
        <div class="text-white/50">部分正确</div>
        <div class="text-yellow-400 font-bold text-lg">5</div>
      </div>
      <div class="bg-white/5 rounded-lg p-2">
        <div class="text-white/50">错误</div>
        <div class="text-red-400 font-bold text-lg">3</div>
      </div>
    </div>
  </div>

  <div class="bg-white/5 rounded-xl p-4 border border-white/10">
    <h4 class="text-white font-semibold mb-3 flex items-center gap-2">
      <span>✅</span> 今日验证完成（pred_20260720_001）
    </h4>
    <div class="bg-red-500/10 border border-red-500/30 rounded-lg p-3">
      <div class="flex items-center justify-between mb-2">
        <span class="text-red-400 font-semibold text-sm">pred_20260720_001 · A级 · ❌ 验证失败</span>
        <span class="text-white/50 text-xs">验证日：2026-07-23</span>
      </div>
      <p class="text-white/80 text-sm mb-2"><b>预判：科技成长股进入中期调整，高股息红利+医药防御成新主线</b></p>
      <p class="text-white/50 text-xs">预判逻辑：7/20市场极度割裂，沪指+0.85%但3700只股票下跌，银行/高股息领涨，科技成长暴跌。预判市场风格切换至防御。</p>
      <p class="text-white/60 text-xs mt-2">
        📌 <b>T+3验证结果（7/23）：验证失败</b>。7/21科技股暴力反弹（科创50+10.73%），
        7/22虽回调但油气/贵金属领涨而非高股息红利+医药。
        市场风格切换至能源/贵金属（受地缘冲突驱动），并非预判中的"高股息红利+医药防御"。
        科技股虽有调整但属于波动而非中期调整确立，贵金属/能源领涨由外部事件驱动而非内部风格切换。
        <b>结论：预判失败，计入错误预判。</b>
      </p>
    </div>
  </div>

  <div class="bg-white/5 rounded-xl p-4 border border-white/10">
    <h4 class="text-white font-semibold mb-3 flex items-center gap-2">
      <span>⏳</span> 待验证预判（进行中）
    </h4>
    <div class="space-y-3">
    <div class="bg-yellow-500/10 border border-yellow-500/30 rounded-lg p-3">
      <div class="flex items-center justify-between mb-2">
        <span class="text-yellow-400 font-semibold text-sm">预判 #20260722_001 · A级</span>
        <span class="text-white/50 text-xs">验证日：2026-07-25（T+3）</span>
      </div>
      <p class="text-white/80 text-sm mb-2">
        <b>存储芯片板块短期见顶风险加大，追高需谨慎</b>
      </p>
      <p class="text-white/60 text-xs">
        逻辑：美股存储芯片单日暴涨后短期获利盘兑现压力大；
        A股存储概念股前期已有较大涨幅，叠加中报业绩验证窗口。
      </p>
      <p class="text-green-400 text-xs mt-2 bg-green-500/10 rounded p-2">
        📊 <b>T+1进展（7/23）：进展中，偏验证</b>。7/22铜冠铜箔-11.33%、存储板块再度杀跌，
        初步验证"短期见顶"预判正确，但需观察T+3确认是否持续回调5-10%级别。
        SK海力士盘后反弹4%（谷歌云催化），增加不确定性。
      </p>
    </div>
    <div class="bg-yellow-500/10 border border-yellow-500/30 rounded-lg p-3">
      <div class="flex items-center justify-between mb-2">
        <span class="text-yellow-400 font-semibold text-sm">预判 #20260722_002 · B级</span>
        <span class="text-white/50 text-xs">验证日：2026-07-25（T+3）</span>
      </div>
      <p class="text-white/80 text-sm mb-2">
        <b>人形机器人板块7月下旬迎来主升浪行情</b>
      </p>
      <p class="text-white/60 text-xs">
        逻辑：特斯拉Optimus 7月启动SOP量产、特斯拉Q2财报催化、工信部万台部署计划。
      </p>
      <p class="text-red-400 text-xs mt-2 bg-red-500/10 rounded p-2">
        📊 <b>T+1进展（7/23）：进展中，偏不利</b>。特斯拉Q2财报马斯克称扩大Optimus产能面临困难，
        量产进度低于市场预期，对人形机器人板块形成短期压制。
        需观察后续产业催化（如更多供应链定点消息）能否扭转预期。
      </p>
    </div>
    </div>
  </div>

  <div class="bg-white/5 rounded-xl p-4 border border-white/10">
    <h4 class="text-white font-semibold mb-3 flex items-center gap-2">
      <span>🎯</span> 今日新增预判
    </h4>
    <div class="space-y-3">
      <div class="bg-red-500/10 border border-red-500/30 rounded-lg p-3">
        <div class="flex items-center justify-between mb-2">
          <span class="text-red-400 font-semibold text-sm">预判 #20260723_001 · A级</span>
          <span class="text-white/50 text-xs">验证日：2026-07-28（T+3）</span>
        </div>
        <p class="text-white/80 text-sm mb-2">
          <b>油价突破95美元将触发美联储加息预期进一步升温，科技成长股继续承压</b>
        </p>
        <p class="text-white/60 text-xs">
          逻辑：布伦特原油已达94美元，中东局势持续紧张，油价上涨直接推升通胀预期。
          美联储9月加息概率已升至80%，若油价破95-100美元区间，
          加息预期将进一步强化甚至出现单次加息50bp的可能。
          高利率环境下科技成长股估值承压，
          预计T+3（7/28前）创业板/科创50继续弱于沪指，
          能源/贵金属/高股息防御板块相对收益更优。
        </p>
      </div>
      <div class="bg-blue-500/10 border border-blue-500/30 rounded-lg p-3">
        <div class="flex items-center justify-between mb-2">
          <span class="text-blue-400 font-semibold text-sm">预判 #20260723_002 · B级</span>
          <span class="text-white/50 text-xs">验证日：2026-07-28（T+3）</span>
        </div>
        <p class="text-white/80 text-sm mb-2">
          <b>政策底+资金底支撑沪指3800点不破，市场进入震荡磨底阶段</b>
        </p>
        <p class="text-white/60 text-xs">
          逻辑：北京国管百亿进场、证监会维稳表态、保险资管净买入、ETF持续净流入，
          政策底信号明确，系统性大跌空间被封死。
          但科技成长股结构性调整仍在，沪指靠权重护盘，
          预计T+3内沪指在3800-3950区间震荡，
          深市/创业板继续弱于沪指，市场呈现"指数稳、个股调"的格局。
        </p>
      </div>
    </div>
  </div>
</div>
'''
gen.add_section("预判验证闭环", verify_html, "🔄")

# ========== 8. 空方视角·风险提示 ==========
bear_html = '''
<div class="space-y-4">
  <div class="bg-gradient-to-br from-red-500/20 to-rose-500/10 border border-red-500/30 rounded-xl p-4">
    <h4 class="text-white font-semibold mb-3 flex items-center gap-2">
      <span>🐻</span> 空方视角：五大风险不容忽视
    </h4>
    <p class="text-white/50 text-xs mb-3">
      报告不仅要讲机会，更要讲风险。以下是空方可能证伪当前政策底逻辑的五大角度：
    </p>
  </div>

  <div class="bg-white/5 rounded-xl p-4 border border-white/10">
    <div class="flex items-start gap-3">
      <span class="text-red-400 text-lg font-bold">1</span>
      <div>
        <h5 class="text-white font-semibold text-sm mb-1">油价暴涨→通胀→美联储加息→全球流动性收紧</h5>
        <p class="text-white/60 text-xs leading-relaxed">
          布油94美元，若中东局势继续恶化油价冲击100美元，将直接推升全球通胀。
          美联储9月加息概率已从降息预期飙升至80%，
          这是今年最大的宏观预期反转——从"降息交易"转向"加息交易"。
          高利率环境下，科技成长股估值将持续承压，
          特别是A股科技股的调整可能比想象中更深、更久。
          这不是回调，可能是估值体系的重塑。
        </p>
      </div>
    </div>
  </div>

  <div class="bg-white/5 rounded-xl p-4 border border-white/10">
    <div class="flex items-start gap-3">
      <span class="text-red-400 text-lg font-bold">2</span>
      <div>
        <h5 class="text-white font-semibold text-sm mb-1">中报业绩证伪：科技股估值杀远未结束</h5>
        <p class="text-white/60 text-xs leading-relaxed">
          铜冠铜箔就是典型案例：中报预增486%却接近20cm跌停，
          因为增速环比放缓+低于机构全年预期。
          7月下旬进入中报密集披露期，更多科技股将面临业绩考验。
          英维克一季报-82%，中报能好转吗？雅克科技动态PE 55倍，
          一旦业绩不及预期，估值杀会非常惨烈。
          纯题材、无业绩支撑的小票将被无情抛弃。
        </p>
      </div>
    </div>
  </div>

  <div class="bg-white/5 rounded-xl p-4 border border-white/10">
    <div class="flex items-start gap-3">
      <span class="text-red-400 text-lg font-bold">3</span>
      <div>
        <h5 class="text-white font-semibold text-sm mb-1">科技股抱团松动：机构调仓引发连锁反应</h5>
        <p class="text-white/60 text-xs leading-relaxed">
          公募基金二季报显示主动基金前三大重仓股全部集中在CPO/光模块，
          出现严重的风格漂移。深度抱团AI算力后，
          一旦预期反转（如加息预期升温），机构集中抛售将引发踩踏。
          7月初以来科技股的暴跌已经验证了这一点，
          但调整幅度可能还不够——历史上抱团瓦解后的调整通常持续2-3个月，
          目前才调整了约1个月，可能还有下半场。
        </p>
      </div>
    </div>
  </div>

  <div class="bg-white/5 rounded-xl p-4 border border-white/10">
    <div class="flex items-start gap-3">
      <span class="text-red-400 text-lg font-bold">4</span>
      <div>
        <h5 class="text-white font-semibold text-sm mb-1">特斯拉Q2盈利不及预期：AI梦想vs盈利现实</h5>
        <p class="text-white/60 text-xs leading-relaxed">
          特斯拉Q2营业利润率仅1.4%，暴跌57%，
          Optimus量产面临困难。这给人形机器人/AI叙事泼了冷水。
          特斯拉作为全球科技股情绪风向标，其盈利不及预期+AI投入回报存疑，
          将影响全球市场对AI/机器人概念股的估值容忍度。
          国内人形机器人板块涨幅已大，一旦特斯拉财报后可能面临估值下修。
        </p>
      </div>
    </div>
  </div>

  <div class="bg-white/5 rounded-xl p-4 border border-white/10">
    <div class="flex items-start gap-3">
      <span class="text-red-400 text-lg font-bold">5</span>
      <div>
        <h5 class="text-white font-semibold text-sm mb-1">中东地缘黑天鹅：战争升级风险</h5>
        <p class="text-white/60 text-xs leading-relaxed">
          特朗普威胁轰炸伊朗民用设施，伊朗反击威胁封锁石油出口。
          局势在加速升级，一旦真的开打，油价可能瞬间破100甚至120美元。
          全球股市将面临系统性风险，A股也难以独善其身。
          虽然油气/黄金会涨，但其他板块会暴跌。
          这是当前最大的尾部风险，市场目前定价还不充分。
        </p>
      </div>
    </div>
  </div>

  <div class="bg-red-500/10 border border-red-500/30 rounded-xl p-4">
    <p class="text-red-300 text-sm font-semibold mb-2">⚠️ 空方结论</p>
    <p class="text-white/70 text-xs leading-relaxed">
      当前市场处于"政策底托底+宏观顶施压"的夹缝中，
      沪指有护盘但深市杀跌，结构性风险远大于系统性风险。
      建议：<b>严控仓位在1成以内，现金为王，等待更确定性机会</b>。
      不要被单日反弹诱惑，纪律比收益更重要。
      关注油价走势是当前最重要的宏观指标。
    </p>
  </div>
</div>
'''
gen.add_section("空方视角·风险提示", bear_html, "🐻")

# ========== 9. 今日操作策略 ==========
strategy_html = '''
<div class="space-y-4">
  <div class="bg-gradient-to-r from-yellow-500/20 to-orange-500/20 border border-yellow-500/30 rounded-xl p-4">
    <h4 class="text-white font-bold mb-2 flex items-center gap-2">
      <span>🎯</span> 今日操作总策略
    </h4>
    <p class="text-white/80 text-sm leading-relaxed">
      隔夜美股走弱+油价暴涨+加息预期升温，科技成长股继续承压，
      但政策底+北京国管百亿托底，沪指系统性风险可控。
      操作上坚持<b class="text-yellow-400">"严控仓位、反弹减仓、现金为王"</b>十二字方针。
      整体仓位建议<b class="text-red-400">1成以内</b>，保留充足现金应对不确定性。
    </p>
  </div>

  <div class="grid md:grid-cols-2 gap-4">
    <div class="bg-white/5 rounded-xl p-4 border border-white/10">
      <h5 class="text-white font-semibold mb-3 flex items-center gap-2">
        <span>✅</span> 优先操作
      </h5>
      <ul class="space-y-2 text-xs text-white/70">
        <li class="flex items-start gap-2">
          <span class="text-red-400 mt-0.5">1.</span>
          <span><b class="text-red-300">*ST建艺：任何价格坚决清仓</b>，退市风险敞口必须关闭，不留幻想</span>
        </li>
        <li class="flex items-start gap-2">
          <span class="text-yellow-400 mt-0.5">2.</span>
          <span><b class="text-yellow-300">铜冠铜箔：反弹100-105元减仓至底仓</b>，技术形态恶化破位后不能格局</span>
        </li>
        <li class="flex items-start gap-2">
          <span class="text-yellow-400 mt-0.5">3.</span>
          <span><b class="text-yellow-300">英维克：65-70元区间减仓≥1/2</b>，深度破止损后反弹是离场机会</span>
        </li>
        <li class="flex items-start gap-2">
          <span class="text-green-400 mt-0.5">4.</span>
          <span><b class="text-green-300">雅克科技：150-155元减仓1/3锁利</b>，相对强势但难独善其身</span>
        </li>
      </ul>
    </div>

    <div class="bg-white/5 rounded-xl p-4 border border-white/10">
      <h5 class="text-white font-semibold mb-3 flex items-center gap-2">
        <span>📌</span> 关注方向
      </h5>
      <ul class="space-y-2 text-xs text-white/70">
        <li class="flex items-start gap-2">
          <span class="text-red-400 mt-0.5">🔥</span>
          <span><b class="text-red-300">油气/煤炭/贵金属：</b>油价暴涨+地缘冲突+避险，当前最强主线</span>
        </li>
        <li class="flex items-start gap-2">
          <span class="text-orange-400 mt-0.5">⭐</span>
          <span><b class="text-orange-300">高股息防御：</b>电力/公用事业，加息环境下防御属性凸显</span>
        </li>
        <li class="flex items-start gap-2">
          <span class="text-blue-400 mt-0.5">🧊</span>
          <span><b class="text-blue-300">AI算力/液冷：</b>谷歌云暴增+资本开支上调，长期逻辑不变，等调整充分后布局</span>
        </li>
        <li class="flex items-start gap-2">
          <span class="text-purple-400 mt-0.5">🛡️</span>
          <span><b class="text-purple-300">政策维稳受益：</b>央企中特估，政策底托底方向</span>
        </li>
      </ul>
    </div>
  </div>

  <div class="bg-white/5 rounded-xl p-4 border border-white/10">
    <h5 class="text-white font-semibold mb-3 flex items-center gap-2">
      <span>📐</span> 关键点位参考
    </h5>
    <div class="grid grid-cols-2 md:grid-cols-4 gap-3 text-center text-xs">
      <div class="bg-white/5 rounded-lg p-3">
        <div class="text-white/50 mb-1">沪指压力</div>
        <div class="text-red-400 font-bold">3900-3950</div>
      </div>
      <div class="bg-white/5 rounded-lg p-3">
        <div class="text-white/50 mb-1">沪指支撑</div>
        <div class="text-green-400 font-bold">3800-3830</div>
      </div>
      <div class="bg-white/5 rounded-lg p-3">
        <div class="text-white/50 mb-1">创业板压力</div>
        <div class="text-red-400 font-bold">3650-3700</div>
      </div>
      <div class="bg-white/5 rounded-lg p-3">
        <div class="text-white/50 mb-1">创业板支撑</div>
        <div class="text-green-400 font-bold">3500-3550</div>
      </div>
    </div>
  </div>

  <div class="bg-amber-500/10 border border-amber-500/30 rounded-xl p-4">
    <p class="text-amber-300 text-sm font-semibold mb-2">💡 今日核心纪律</p>
    <p class="text-white/70 text-xs leading-relaxed">
      ①<b>不抄底</b>：科技股调整未结束，底部不是猜出来的，是走出来的；<br>
      ②<b>反弹减仓</b>：利用任何反弹降低仓位，落袋为安；<br>
      ③<b>严守止损</b>：破位标的坚决执行纪律，不存侥幸；<br>
      ④<b>关注油价</b>：油价是当前最重要的宏观指标，破95则加息预期进一步升温；<br>
      ⑤<b>现金为王</b>：保留充足弹药，等待更确定性的机会（中报超预期、调整充分后）。
    </p>
  </div>
</div>
'''
gen.add_section("今日操作策略", strategy_html, "🎯")

# ========== 10. 教训库引用 ==========
lesson_html = '''
<div class="space-y-3">
  <div class="bg-red-500/10 border border-red-500/30 rounded-lg p-3">
    <p class="text-red-300 font-semibold mb-1">教训#1：业绩好≠股价涨，要看预期差</p>
    <p class="text-white/60 text-xs">
      铜冠铜箔中报预增486%却接近20cm跌停，再次验证"业绩好不等于股价涨"。
      <b>正确做法</b>：业绩预告要看"预期差"而非绝对增速，
      前期涨幅过大的标的，即便业绩好也可能"利好出尽"。
      买入前必须对标机构一致预期，确认是否真的超预期。
      铜冠已经给了两次教训（第一次7/20跌停后7/21反弹，第二次7/22再跌-11.33%），
      趋势逆转信号明确后果断减仓才是正确选择。
    </p>
  </div>

  <div class="bg-orange-500/10 border border-orange-500/30 rounded-lg p-3">
    <p class="text-orange-300 font-semibold mb-1">教训#2：单日暴涨不是反转，是反弹</p>
    <p class="text-white/60 text-xs">
      7/21科创50暴涨10.73%，很多人以为反转了，结果7/22创业板-3.24%继续杀跌。
      <b>正确做法</b>：暴跌后的第一波反弹通常是技术性反抽，
      至少需要3-5个交易日企稳信号（缩量+止跌+均线修复）才能确认反转。
      绝不接"飞刀"，也不被单日暴涨冲昏头脑。
    </p>
  </div>

  <div class="bg-yellow-500/10 border border-yellow-500/30 rounded-lg p-3">
    <p class="text-yellow-300 font-semibold mb-1">教训#3：油价是科技股的天敌</p>
    <p class="text-white/60 text-xs">
      油价暴涨→通胀预期→美联储加息→科技成长股估值承压。这条链条反复被验证。
      当前布油94美元，若继续上涨将进一步压制科技股估值。
      <b>正确做法</b>：油价快速上涨阶段，回避科技成长股，
      转向能源/贵金属/高股息防御板块。
      等油价回落、通胀预期降温后再考虑布局科技股。
    </p>
  </div>

  <div class="bg-amber-500/10 border border-amber-500/30 rounded-lg p-3">
    <p class="text-amber-300 font-semibold mb-1">教训#4：ST股不能碰，越跌越不能补</p>
    <p class="text-white/60 text-xs">
      *ST建艺从13.45元跌到8.08元，浮亏-39.9%，期间任何补仓只会扩大亏损。
      退市风险下，底部可能就是退市清零。
      <b>正确做法</b>：ST股坚决不碰，一旦持仓变ST必须第一时间清仓，不存任何幻想。
      退市股归零的风险是永久性损失，不值得用本金去赌重组概率。
    </p>
  </div>
</div>
'''
gen.add_section("教训库引用", lesson_html, "📚")

# ========== 生成+发布 ==========
output_path = os.path.join(WORK_DIR, 'docs/daily/20260723_每日新闻洞察.html')
result = gen.publish(output_path=output_path)
print("发布结果:", result)
print("成功:", result.get('success', False))
print("报告路径:", output_path)
print("文件大小:", os.path.getsize(output_path), "字节")

# 更新 latest.html
latest_path = os.path.join(WORK_DIR, 'docs/daily/latest.html')
shutil.copy2(output_path, latest_path)
print("latest.html 已更新")
