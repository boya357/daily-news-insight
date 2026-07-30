#!/usr/bin/env python3
"""2026年7月30日 每日新闻洞察生成 - 周四·存储芯片崩盘美光跌10%·美联储按兵不动3票反对·A股深V反转高低切换·持仓继续承压"""
import sys, os, shutil, json
WORK_DIR = '/root/daily-news-insight'
sys.path.insert(0, os.path.join(WORK_DIR, 'v3'))
from generators.daily_pro import DailyReportProGenerator

gen = DailyReportProGenerator(
    date_str='2026年7月30日', weekday='星期四',
    subtitle='2026年7月30日 星期四 · 存储芯片崩盘美光跌10%SK海力士连续暴跌·美联储按兵不动3票反对鹰派超预期·A股深V反转高低切换消费领涨·持仓：雅克-8.56%英维克-4.97%',
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
    {"name":"道琼斯","change":"-2.19%","up":False},
    {"name":"标普500","change":"-1.52%","up":False},
    {"name":"纳斯达克","change":"-1.74%","up":False},
    {"name":"费城半导体","change":"-5.33%","up":False},
    {"name":"恒生指数","change":"+1.96%","up":True},
    {"name":"日经225","change":"-0.90%","up":False},
])
global_list1 = render_list([
    {"name":"WTI原油","change":"-1.22%/$83.43","up":False},
    {"name":"布伦特原油","change":"-1.18%/$87.05","up":False},
    {"name":"COMEX黄金","change":"+0.92%/$4134.57","up":True},
    {"name":"COMEX白银","change":"+0.22%/$58.21","up":True},
])
global_list2 = render_list([
    {"name":"三星电子","change":"-5.23%","up":False},
    {"name":"SK海力士","change":"-9.61%","up":False},
    {"name":"三星SDI","change":"-4.71%","up":False},
    {"name":"LG新能源","change":"-4.30%","up":False},
])
global_list3 = render_list([
    {"name":"英伟达","change":"-3.55%","up":False},
    {"name":"博通","change":"-2.78%","up":False},
    {"name":"美光科技","change":"-9.94%","up":False},
    {"name":"AMD","change":"-5.51%","up":False},
    {"name":"英特尔","change":"-5.12%","up":False},
    {"name":"台积电ADR","change":"-4.50%","up":False},
])
global_html = '''
<div class="grid md:grid-cols-3 gap-4">
  <div class="md:col-span-2">
    <div class="text-white font-semibold mb-3 flex items-center gap-2"><span>🌍</span><span>隔夜全球市场 · 存储芯片崩盘式下跌·美联储鹰派超预期·科技股普跌</span></div>
    <div class="grid grid-cols-3 md:grid-cols-6 gap-2">{0}</div>
    <p class="text-xs text-white/50 mt-3 leading-relaxed">
      ⚡ <b class="text-red-400">核心要点：美股三大指数集体下跌，费城半导体暴跌5.33%，存储芯片板块崩盘式下跌，美光跌近10%创史上最大单日跌幅之一</b>——<br>
      ①<b>存储芯片大崩盘</b>：美光科技暴跌9.94%，SK海力士韩股暴跌9.61%（连续两日累计跌幅超20%），应用材料跌8.40%，闪迪暴跌14%+。
      触发因素：SK海力士Q2财报营收79.32万亿韩元（+257%）、营业利润60.54万亿韩元（+557%），但双双不及市场预期（预期营收84万亿/利润64万亿），
      引发「AI存储需求见顶」恐慌。叠加英伟达为OpenAI 2500亿美元数据中心提供资金担保的消息，市场担忧AI资本开支循环融资不可持续。<br>
      ②<b>美联储7月利率决议</b>：维持3.50%-3.75%不变，9:3分歧投票，3人反对（Hammack、Kashkari、Logan要求加息25bp），
      沃什记者会延续鹰派表态，强调坚守2%通胀目标，不排除后续加息。9月加息概率回落至59%，但长端美债收益率上行，通胀预期升温。<br>
      ③<b>油价回落</b>：WTI原油跌1.22%至83.43美元，布伦特跌1.18%至87.05美元，从前期高位回落，中东局势边际缓和。<br>
      ④<b>黄金逆势上涨</b>：COMEX黄金涨0.92%至4134.57美元/盎司，美联储鹰派但未实际加息+通胀预期升温+避险需求，黄金继续走强。<br>
      ⑤<b>港股反弹</b>：恒生指数涨1.96%至25807.92点，科技股反弹带动，外资回流港股抄底迹象明显。
    </p>
  </div>
  <div class="space-y-4">
    <div>
    <div class="text-white font-semibold mb-3 flex items-center gap-2"><span>🛢️</span><span>大宗商品</span></div>
      <div class="bg-white/5 rounded-lg p-3">{1}</div></div>
    <div>
    <div class="text-white font-semibold mb-3 flex items-center gap-2"><span>🇰🇷</span><span>韩股核心（暴跌）</span></div>
      <div class="bg-white/5 rounded-lg p-3">{2}</div></div>
    <div>
    <div class="text-white font-semibold mb-3 flex items-center gap-2"><span>💻</span><span>美股科技龙头（普跌）</span></div>
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
    <div class="text-xl font-bold text-red-400">3828.47</div>
    <div class="text-xs text-red-400 mt-1">+0.40% / 深V反转</div>
  </div>
  <div class="bg-gradient-to-br from-red-500/20 to-orange-500/10 border border-red-500/30 rounded-xl p-3 text-center">
    <div class="text-xs text-white/60 mb-1">深证成指</div>
    <div class="text-xl font-bold text-red-400">13658.44</div>
    <div class="text-xs text-red-400 mt-1">+1.10%</div>
  </div>
  <div class="bg-gradient-to-br from-red-500/20 to-orange-500/10 border border-red-500/30 rounded-xl p-3 text-center">
    <div class="text-xs text-white/60 mb-1">创业板指</div>
    <div class="text-xl font-bold text-red-400">3378.70</div>
    <div class="text-xs text-red-400 mt-1">+1.55% / 领涨</div>
  </div>
  <div class="bg-gradient-to-br from-yellow-500/20 to-amber-500/10 border border-yellow-500/30 rounded-xl p-3 text-center">
    <div class="text-xs text-white/60 mb-1">成交额</div>
    <div class="text-xl font-bold text-yellow-400">2.30万亿</div>
    <div class="text-xs text-white/60 mt-1">放量2700亿</div>
  </div>
</div>
<div class="bg-white/5 rounded-xl p-4">
  <h4 class="text-white font-semibold mb-3 text-sm">📊 周三（7/29）A股复盘：深V反转·高低切换·消费领涨科技承压</h4>
  <div class="grid md:grid-cols-2 gap-4 text-xs">
    <div>
      <p class="text-white/80 font-semibold mb-2">📈 最强方向</p>
      <p class="text-white/60 leading-relaxed mb-2">
      <b class="text-yellow-400">①大消费全线爆发</b>：乳业、食品饮料、零售、教育领涨，欢乐家/李子园/阳光乳业等多股涨停。催化：原奶周期改善+暑期消费回暖+内需预期提升。<br>
      <b class="text-yellow-400">②大金融午后发力</b>：券商、金融IT走强，华林证券涨停，市场情绪回暖带动。<br>
      ③游戏/传媒：游戏ETF大涨5.54%，超跌反弹+版号利好。<br>
      ④锂电池反弹：领湃科技/永杉锂业等多股涨停，超跌反弹。
      </p>
    </div>
    <div>
      <p class="text-white/80 font-semibold mb-2">📉 相对弱势</p>
      <p class="text-white/60 leading-relaxed mb-2">
      <b class="text-green-400">①半导体/存储</b>：存储芯片概念跌幅居前，通富微电跌停，兆易创新/雅克科技盘中触及跌停后打开。<br>
      <b>②算力硬件/PCB</b>：AI硬件方向继续承压，英维克大跌4.97%，铜冠铜箔继续下跌。<br>
      ③科创50：-0.87%，是唯一下跌的宽基指数，科技赛道仍弱。<br>
      <b class="text-yellow-400">特征</b>：早盘沪指探底3782点后深V反转，收盘涨0.40%收长下影线。
      4253只个股上涨，1212只下跌，涨跌中位数+1.58%，普涨格局。
      典型"高低切换"——资金从高位科技撤出，流向低位消费/金融/防御板块。
      </p>
    </div>
  </div>
  <p class="text-xs text-white/50 mt-3 leading-relaxed">
    ⚡ <b class="text-yellow-400">盘口解读：</b>7/29是典型的"深V反转+高低切换"行情。
    早盘受隔夜美股半导体大跌拖累，沪指探底3782点，但消费/煤炭/金融逆势护盘，
    午后资金集中抄底，指数逐级拉升完成反转。
    <b class="text-yellow-400">关键信号：</b>①成交额放量至2.3万亿（放量2700亿），增量资金进场迹象；
    ②超4200只个股上涨，赚钱效应明显改善；③科技股虽然下跌但跌幅收窄，有企稳迹象。
    但需注意：科创50仍是唯一下跌的宽基指数，说明科技赛道的调整还没结束，
    当前主线从高位科技转向大消费与防御，结构性行情特征明显。
    3800点支撑基本确认，但上方3900点压力较重，震荡磨底阶段。
  </p>
</div>
</div>'''
gen.add_section("昨日A股复盘（7/29）", ashare_html, "📈")

# ========== 3. 今日重磅新闻 ==========
news_items = [
    {"tag":"💥","title":"存储芯片崩盘式下跌 美光跌10%SK海力士连续暴跌","content":"美股存储芯片板块遭遇历史性抛售，美光科技暴跌9.94%，创史上最大单日跌幅之一，从6月高点回撤超30%，市值跌破万亿美元。SK海力士韩股暴跌9.61%，连续两日累计跌幅超20%。闪迪暴跌14%+，应用材料跌8.40%。导火索：SK海力士Q2财报营收79.32万亿韩元（+257%）、营业利润60.54万亿韩元（+557%），双双创历史新高但不及市场预期（预期营收84万亿/利润64万亿）。市场担忧AI存储需求见顶+行业扩产导致产能过剩。","source":"新浪财经/21世纪经济报道"},
    {"tag":"🏦","title":"美联储按兵不动但3票反对 沃什鹰派表态超预期","content":"美联储7月FOMC以9:3分歧维持利率3.50%-3.75%不变，3人反对（Hammack、Kashkari、Logan要求加息25bp），显示内部分歧巨大。沃什记者会延续鹰派表态，强调坚守2%通胀目标，不排除后续加息，关注8月27日Jackson Hole讲话。9月加息概率回落至59%（此前80%），但长端美债收益率上行，通胀预期升温。2年期美债收益率下行8bp至4.24%，10年/30年期收益率上行。","source":"第一财经/华泰证券"},
    {"tag":"🤖","title":"英伟达2500亿美元OpenAI担保引发「循环融资」担忧","content":"据华尔街日报报道，英伟达正在洽谈为OpenAI俄亥俄州数据中心项目提供高达2500亿美元的资金担保。消息引发市场对AI资本开支「循环融资」模式的担忧——英伟达借钱给客户买自己的芯片，被类比为2000年电信泡沫的融资模式。英伟达信用违约互换（CDS）飙升至历史新高。英伟达当日跌3.55%，半导体板块普跌。这一模式若扩散，AI硬件需求的可持续性将受到质疑。","source":"华尔街日报/36氪"},
    {"tag":"🇰🇷","title":"SK海力士史上最强财报仍「不及预期」 利润增557%","content":"SK海力士2026年Q2财报：营收79.32万亿韩元（+257%YoY，+51%QoQ），营业利润60.54万亿韩元（+557%YoY，+61%QoQ），净利润93.92万亿韩元，日均赚约40亿人民币。营业利润率76%，净利润率118%。但营收低于市场预期的84万亿韩元，利润低于预期的64万亿韩元。原因：HBM销售占比高但通用DRAM/NAND涨价获益有限，二季度存储价格涨幅较一季度收窄，长单锁价牺牲了现货弹性。","source":"新浪财经/财联社"},
    {"tag":"🇨🇳","title":"A股深V反转放量修复 4200股普涨高低切换","content":"7月29日A股走出深V反转行情，沪指最低探至3782点后震荡回升，收盘涨0.40%报3828.47点，收出长下影阳线。创业板指涨1.55%领涨。两市成交2.30万亿元，较前日放量2708亿元，增量资金进场。全市场4253只个股上涨，1212只下跌，涨跌中位数+1.58%。大消费（乳业/食品/零售）领涨，半导体/算力硬件承压，资金完成高低切换。","source":"东方财富/凤凰网"},
    {"tag":"📊","title":"韩股暴跌触发第九次熔断 KOSPI较6月高点回撤超43%","content":"韩国股市7月29日再度暴跌，KOSPI指数盘中一度跌超6%，较6月高点最大回撤超43%，年内第九次触发全市场熔断。SK海力士跌超9%，三星电子跌超5%。分析认为韩股芯片股暴跌源于：前期涨幅过大估值透支+高杠杆资金踩踏+美联储加息预期+SK海力士财报不及预期。韩股调整幅度远超美股半导体，显示韩国市场杠杆率过高的脆弱性。","source":"央广网"},
]

news_html = '<div class="space-y-4">'
for idx, n in enumerate(news_items):
    news_html += '''
    <div class="bg-white/5 rounded-xl p-4 border border-white/10 hover:border-white/20 transition-all">
      <div class="flex items-start gap-3">
        <div class="text-2xl flex-shrink-0">{}</div>
        <div class="flex-1">
          <h4 class="text-white font-semibold text-sm mb-2">{}</h4>
          <p class="text-white/60 text-xs leading-relaxed">{}</p>
          <p class="text-white/30 text-xs mt-2">📰 来源：{}</p>
        </div>
      </div>
    </div>'''.format(n['tag'], n['title'], n['content'], n['source'])
news_html += '</div>'
gen.add_section("今日重磅新闻", news_html, "📰")

# ========== 4. 持仓诊断 ==========
holdings_html = '''
<div class="space-y-4">
  <div class="bg-gradient-to-r from-yellow-500/20 to-orange-500/20 border border-yellow-500/30 rounded-xl p-4">
    <h4 class="text-white font-bold mb-2 flex items-center gap-2">
      <span>💰</span> 持仓诊断总览（7月29日）
    </h4>
    <p class="text-white/80 text-sm leading-relaxed">
      持仓4只全部跑输大盘（沪指+0.40%），科技成长方向继续承压。
      雅克科技大跌8.56%，英维克跌4.97%，铜冠铜箔延续下跌趋势，仅*ST建艺微涨1.24%。
      当前持仓整体风险<b class="text-red-400">偏高</b>，存储/半导体/液冷方向均处于调整通道，
      建议严格执行止损纪律，反弹减仓为主。
    </p>
  </div>

  <div class="grid md:grid-cols-2 gap-4">
    <!-- 英维克 -->
    <div class="bg-white/5 rounded-xl p-4 border-l-4 border-green-500/50">
      <div class="flex items-center justify-between mb-2">
        <h5 class="text-yellow-400 font-semibold text-sm">英维克 (002837)</h5>
        <span class="text-green-400 font-bold text-sm">-4.97% → 52.39元</span>
      </div>
      <div class="text-xs text-white/60 space-y-1">
        <p>📊 <b class="text-white/80">趋势判断：</b>下跌趋势，从93.52元高点回撤约<b>44%</b>，持续创新低</p>
        <p>💡 <b class="text-white/80">核心逻辑：</b>液冷+AI算力散热，长期逻辑不变但短期业绩验证不足，一季报-82%</p>
        <p>⚠️ <b class="text-red-400">风险：</b>中报业绩可能继续承压，科技股整体调整，资金从高位撤出</p>
        <p>🎯 <b class="text-white/80">操作建议：</b>反弹55-60元区间减仓至底仓，深度破位后不可格局，等待中报验证</p>
        <p>📐 <b class="text-white/80">关键点位：</b>压力55/60元，支撑50/45元</p>
      </div>
    </div>

    <!-- 铜冠铜箔 -->
    <div class="bg-white/5 rounded-xl p-4 border-l-4 border-green-500/50">
      <div class="flex items-center justify-between mb-2">
        <h5 class="text-yellow-400 font-semibold text-sm">铜冠铜箔 (301217)</h5>
        <span class="text-green-400 font-bold text-sm">继续下跌 · 约85-87元</span>
      </div>
      <div class="text-xs text-white/60 space-y-1">
        <p>📊 <b class="text-white/80">趋势判断：</b>下跌趋势，从高位回撤超40%，中报预增486%利好出尽</p>
        <p>💡 <b class="text-white/80">核心逻辑：</b>锂电铜箔+PCB铜箔+AI服务器铜箔，中报大增但低于机构全年预期</p>
        <p>⚠️ <b class="text-red-400">风险：</b>存储/PCB板块调整，铜价波动，业绩增速环比放缓预期</p>
        <p>🎯 <b class="text-white/80">操作建议：</b>反弹90-95元减仓至底仓，趋势破位后不格局，教训已验证两次</p>
        <p>📐 <b class="text-white/80">关键点位：</b>压力90/95元，支撑80/75元</p>
      </div>
    </div>

    <!-- 雅克科技 -->
    <div class="bg-white/5 rounded-xl p-4 border-l-4 border-red-500/50">
      <div class="flex items-center justify-between mb-2">
        <h5 class="text-yellow-400 font-semibold text-sm">雅克科技 (002409)</h5>
        <span class="text-red-400 font-bold text-sm">-8.56% → 152.18元</span>
      </div>
      <div class="text-xs text-white/60 space-y-1">
        <p>📊 <b class="text-white/80">趋势判断：</b>放量大跌，盘中触及跌停，换手率16.23%，成交79.16亿，主力净流出3.33亿</p>
        <p>💡 <b class="text-white/80">核心逻辑：</b>半导体材料+HBM前驱体+光刻胶，存储链条核心标的</p>
        <p>⚠️ <b class="text-red-400">风险：</b>存储板块崩盘式下跌拖累，美光/SK海力士暴跌引发行业担忧，动态PE偏高</p>
        <p>🎯 <b class="text-white/80">操作建议：</b>150-160元区间减仓1/3锁利，剩余底仓观察140元支撑，破位继续减</p>
        <p>📐 <b class="text-white/80">关键点位：</b>压力160/170元，支撑140/130元</p>
      </div>
    </div>

    <!-- *ST建艺 -->
    <div class="bg-white/5 rounded-xl p-4 border-l-4 border-red-500/50">
      <div class="flex items-center justify-between mb-2">
        <h5 class="text-yellow-400 font-semibold text-sm">*ST建艺 (002789)</h5>
        <span class="text-red-400 font-bold text-sm">+1.24% → 8.97元</span>
      </div>
      <div class="text-xs text-white/60 space-y-1">
        <p>📊 <b class="text-white/80">趋势判断：</b>ST摘帽无望，退市风险高悬，任何反弹都是离场机会</p>
        <p>💡 <b class="text-white/80">核心逻辑：</b>建筑装饰+ST，无明确重组预期，退市风险敞口大</p>
        <p>⚠️ <b class="text-red-400">风险：</b>退市归零风险，浮亏已超30%，继续持有只会扩大亏损</p>
        <p>🎯 <b class="text-white/80">操作建议：</b><b class="text-red-400 font-bold">任何价格坚决清仓</b>，关闭退市风险敞口，不留幻想</p>
        <p>📐 <b class="text-white/80">关键点位：</b>9元附近反弹即是离场机会，无支撑可言</p>
      </div>
    </div>
  </div>

  <div class="bg-red-500/10 border border-red-500/30 rounded-xl p-4">
    <p class="text-red-300 text-sm font-semibold mb-2">⚠️ 持仓风险提示</p>
    <ul class="text-white/70 text-xs space-y-1">
      <li>• 四只持仓集中在科技成长方向，板块系统性调整下缺乏对冲</li>
      <li>• 存储/半导体板块崩盘式下跌，雅克科技/铜冠铜箔首当其冲</li>
      <li>• 英维克已从高点回撤44%，继续下跌空间仍需警惕</li>
      <li>• *ST建艺退市风险必须第一时间关闭，不存任何侥幸</li>
      <li>• <b>整体仓位建议降至1成以内</b>，保留充足现金等待更确定性机会</li>
    </ul>
  </div>
</div>'''
gen.add_section("持仓诊断", holdings_html, "💰")

# ========== 5. 题材深度分析 ==========
topic_html = '''
<div class="space-y-5">
  <!-- 存储芯片 -->
  <div class="bg-white/5 rounded-xl p-4 border border-white/10">
    <div class="flex items-center justify-between mb-3">
      <h4 class="text-white font-semibold flex items-center gap-2">
        <span class="text-red-400">💾</span> 存储芯片：崩盘式下跌，是上车机会还是趋势反转？
      </h4>
      <span class="px-2 py-0.5 bg-red-500/20 text-red-400 text-xs rounded-full border border-red-500/30">高风险</span>
    </div>
    <div class="grid md:grid-cols-2 gap-4 text-xs">
      <div>
        <p class="text-white/80 font-semibold mb-2">📉 空方逻辑</p>
        <ul class="text-white/60 space-y-1.5 leading-relaxed">
          <li>• SK海力士Q2创纪录利润仍不及预期，说明市场预期过高</li>
          <li>• 存储价格季度涨幅收窄，涨价红利边际减弱</li>
          <li>• 头部企业激进扩产，2027年后可能产能过剩</li>
          <li>• AI资本开支「循环融资」模式存疑，需求可持续性担忧</li>
          <li>• 美光从高点回撤30%+，韩股芯片股回撤40%+，趋势已破</li>
          <li>• 美联储鹰派，高利率环境压制成长股估值</li>
        </ul>
      </div>
      <div>
        <p class="text-white/80 font-semibold mb-2">📈 多方逻辑</p>
        <ul class="text-white/60 space-y-1.5 leading-relaxed">
          <li>• 基本面未变：SK海力士利润增557%，美光营收增346%，行业高景气</li>
          <li>• AI需求强劲：HBM4供不应求，DRAM供需紧张持续到2027年以后</li>
          <li>• 长单锁价：美光16份多年期"照付不议"合同锁定约1000亿美元收入</li>
          <li>• 国产替代：中国存储芯片企业技术迭代超预期，长鑫上市催化</li>
          <li>• 短期超跌：30%+回撤后估值泡沫已部分消化</li>
          <li>• 美光CEO亲口确认：DRAM/NAND供需紧张持续到2027年以后</li>
        </ul>
      </div>
    </div>
    <div class="mt-3 p-3 bg-amber-500/10 border border-amber-500/30 rounded-lg">
      <p class="text-amber-300 text-sm font-semibold mb-1">💡 判断结论</p>
      <p class="text-white/70 text-xs leading-relaxed">
        存储芯片当前处于<b>"基本面强+情绪面弱+估值面下修"</b>的复杂阶段。
        短期受情绪和资金面驱动可能继续下跌，但中长期AI存储需求逻辑未破。
        操作建议：<b class="text-red-400">不抄底，等右侧信号</b>——至少需要3个条件同时满足：
        ①美光/SK海力士止跌企稳（连续3日不创新低）；②费城半导体指数收复20日线；
        ③A股存储板块放量反弹。满足前先观望，保留弹药。
        关注国产替代线（长鑫产业链）可能先于海外存储股企稳。
      </p>
    </div>
  </div>

  <!-- 大消费 -->
  <div class="bg-white/5 rounded-xl p-4 border border-white/10">
    <div class="flex items-center justify-between mb-3">
      <h4 class="text-white font-semibold flex items-center gap-2">
        <span class="text-green-400">🛒</span> 大消费：高低切换的新主线？可持续性如何？
      </h4>
      <span class="px-2 py-0.5 bg-green-500/20 text-green-400 text-xs rounded-full border border-green-500/30">观察</span>
    </div>
    <p class="text-white/60 text-xs leading-relaxed mb-3">
      7月29日大消费全线爆发，乳业/食品饮料/零售/教育领涨，游戏/传媒同步走强。
      这是典型的"高低切换"行情——资金从高位科技撤出，流向调整充分、估值低的消费板块。
    </p>
    <div class="grid md:grid-cols-3 gap-3 text-xs">
      <div class="bg-white/5 rounded-lg p-3">
        <p class="text-white/80 font-semibold mb-2">催化因素</p>
        <ul class="text-white/60 space-y-1">
          <li>• 暑期消费旺季来临</li>
          <li>• 原奶周期拐点预期</li>
          <li>• 内需刺激政策预期</li>
          <li>• 估值处于历史低位</li>
        </ul>
      </div>
      <div class="bg-white/5 rounded-lg p-3">
        <p class="text-white/80 font-semibold mb-2">持续性判断</p>
        <ul class="text-white/60 space-y-1">
          <li>• 短期：超跌反弹，持续性有限</li>
          <li>• 中期：看政策力度和消费数据</li>
          <li>• 长期：消费复苏慢变量，非主线</li>
          <li>• 定性：防御性配置而非进攻</li>
        </ul>
      </div>
      <div class="bg-white/5 rounded-lg p-3">
        <p class="text-white/80 font-semibold mb-2">操作建议</p>
        <ul class="text-white/60 space-y-1">
          <li>• 不追高，回调可小仓位配置</li>
          <li>• 优选估值低+业绩稳的龙头</li>
          <li>• 不作为核心仓位，仅做对冲</li>
          <li>• 科技企稳后仍优先切回科技</li>
        </ul>
      </div>
    </div>
  </div>

  <!-- 美联储 -->
  <div class="bg-white/5 rounded-xl p-4 border border-white/10">
    <div class="flex items-center justify-between mb-3">
      <h4 class="text-white font-semibold flex items-center gap-2">
        <span class="text-blue-400">🏦</span> 美联储7月决议：按兵不动但内部分歧巨大，9月加不加？
      </h4>
      <span class="px-2 py-0.5 bg-blue-500/20 text-blue-400 text-xs rounded-full border border-blue-500/30">关键变量</span>
    </div>
    <p class="text-white/60 text-xs leading-relaxed mb-3">
      美联储7月FOMC以9:3分歧维持利率3.50%-3.75%不变，3人反对（要求加息25bp），创2019年以来最大分歧。
      沃什记者会延续鹰派表态，强调坚守2%通胀目标，不排除后续加息。
    </p>
    <div class="grid md:grid-cols-2 gap-3 text-xs">
      <div class="bg-white/5 rounded-lg p-3">
        <p class="text-white/80 font-semibold mb-2">📊 市场定价</p>
        <ul class="text-white/60 space-y-1">
          <li>• 9月加息概率：59%（前80%）</li>
          <li>• 2年美债收益率：4.24%（-8bp）</li>
          <li>• 长端收益率：上行（通胀预期升温）</li>
          <li>• 美元指数：100.9（-0.5%）</li>
          <li>• 黄金：4068美元（+0.5%）</li>
        </ul>
      </div>
      <div class="bg-white/5 rounded-lg p-3">
        <p class="text-white/80 font-semibold mb-2">🎯 对A股影响</p>
        <ul class="text-white/60 space-y-1">
          <li>• 短期：加息预期降温，利好成长股估值</li>
          <li>• 中期：鹰派立场未变，压制空间有限</li>
          <li>• 关注Jackson Hole讲话（8月27日）</li>
          <li>• 油价是关键变量，决定通胀走势</li>
          <li>• 人民币汇率压力边际缓解</li>
        </ul>
      </div>
    </div>
  </div>
</div>'''
gen.add_section("题材深度分析", topic_html, "🔍")

# ========== 6. 今日操作策略 ==========
strategy_html = '''
<div class="space-y-4">
  <div class="bg-gradient-to-r from-yellow-500/20 to-orange-500/20 border border-yellow-500/30 rounded-xl p-4">
    <h4 class="text-white font-bold mb-2 flex items-center gap-2">
      <span>🎯</span> 今日操作总策略
    </h4>
    <p class="text-white/80 text-sm leading-relaxed">
      隔夜美股半导体崩盘+美联储鹰派，A股面临外围压力，但昨日深V反转显示内生韧性。
      预计今日科技股承压，消费/防御板块可能延续强势。
      操作上坚持<b class="text-yellow-400">"严控仓位、反弹减仓、观望为主"</b>十二字方针。
      整体仓位建议<b class="text-red-400">1成以内</b>，保留充足现金等待更确定性机会。
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
          <span><b class="text-yellow-300">雅克科技：160-170元反弹减仓1/3</b>，存储板块崩盘拖累，降低仓位</span>
        </li>
        <li class="flex items-start gap-2">
          <span class="text-yellow-400 mt-0.5">3.</span>
          <span><b class="text-yellow-300">英维克：55-60元区间减仓≥1/2</b>，深度回撤44%后反弹是离场机会</span>
        </li>
        <li class="flex items-start gap-2">
          <span class="text-yellow-400 mt-0.5">4.</span>
          <span><b class="text-yellow-300">铜冠铜箔：90-95元反弹减仓至底仓</b>，两次教训后必须执行纪律</span>
        </li>
        <li class="flex items-start gap-2">
          <span class="text-green-400 mt-0.5">5.</span>
          <span><b class="text-green-300">观望为主</b>：不抄底科技股，等右侧信号确认后再进场</span>
        </li>
      </ul>
    </div>

    <div class="bg-white/5 rounded-xl p-4 border border-white/10">
      <h5 class="text-white font-semibold mb-3 flex items-center gap-2">
        <span>📌</span> 关注方向
      </h5>
      <ul class="space-y-2 text-xs text-white/70">
        <li class="flex items-start gap-2">
          <span class="text-orange-400 mt-0.5">⭐</span>
          <span><b class="text-orange-300">贵金属/黄金：</b>通胀预期+避险+美联储不加息，黄金继续强势</span>
        </li>
        <li class="flex items-start gap-2">
          <span class="text-green-400 mt-0.5">🛒</span>
          <span><b class="text-green-300">大消费（观察）：</b>高低切换的受益者，但持续性待验证，不追高</span>
        </li>
        <li class="flex items-start gap-2">
          <span class="text-blue-400 mt-0.5">🏦</span>
          <span><b class="text-blue-300">大金融/券商：</b>政策维稳+情绪修复，脉冲式机会，不追高</span>
        </li>
        <li class="flex items-start gap-2">
          <span class="text-purple-400 mt-0.5">💾</span>
          <span><b class="text-purple-300">国产存储替代：</b>长鑫产业链，可能先于海外存储股企稳，观察名单</span>
        </li>
        <li class="flex items-start gap-2">
          <span class="text-gray-400 mt-0.5">⏸️</span>
          <span><b class="text-gray-400">AI算力/存储（回避）：</b>板块趋势已破，等企稳信号再考虑</span>
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
        <div class="text-red-400 font-bold">3880-3920</div>
      </div>
      <div class="bg-white/5 rounded-lg p-3">
        <div class="text-white/50 mb-1">沪指支撑</div>
        <div class="text-green-400 font-bold">3780-3800</div>
      </div>
      <div class="bg-white/5 rounded-lg p-3">
        <div class="text-white/50 mb-1">创业板压力</div>
        <div class="text-red-400 font-bold">3450-3500</div>
      </div>
      <div class="bg-white/5 rounded-lg p-3">
        <div class="text-white/50 mb-1">创业板支撑</div>
        <div class="text-green-400 font-bold">3300-3350</div>
      </div>
    </div>
  </div>

  <div class="bg-amber-500/10 border border-amber-500/30 rounded-xl p-4">
    <p class="text-amber-300 text-sm font-semibold mb-2">💡 今日核心纪律</p>
    <p class="text-white/70 text-xs leading-relaxed">
      ①<b>不抄底</b>：存储/半导体崩盘式下跌，底部不是猜出来的，等右侧信号；<br>
      ②<b>反弹减仓</b>：利用任何反弹降低科技成长仓位，落袋为安；<br>
      ③<b>严守止损</b>：破位标的坚决执行纪律，不存侥幸；<br>
      ④<b>关注外围</b>：美股半导体走势是当前最重要的领先指标，费半指数企稳前不轻言底；<br>
      ⑤<b>现金为王</b>：保留充足弹药，等待更确定性的机会（8月中报季+科技股企稳）。
    </p>
  </div>
</div>'''
gen.add_section("今日操作策略", strategy_html, "🎯")

# ========== 7. 预判验证闭环 ==========
verify_html = '''
<div class="space-y-4">
  <div class="bg-white/5 rounded-xl p-4 border border-white/10">
    <h4 class="text-white font-semibold mb-3 flex items-center gap-2">
      <span>📋</span> 历史预判验证
    </h4>
    <div class="grid md:grid-cols-2 gap-3">
    <div class="bg-white/5 rounded-lg p-3 border border-white/10">
      <div class="flex items-center justify-between mb-2">
        <span class="text-blue-400 font-semibold text-xs">预判 #20260723_001 · A级</span>
        <span class="text-white/50 text-xs">原验证日：7/28</span>
      </div>
      <p class="text-white/80 text-sm mb-2">
        <b>油价突破95美元将触发美联储加息预期进一步升温，科技成长股继续承压</b>
      </p>
      <p class="text-white/60 text-xs">
        逻辑：布油94美元→加息预期→科技股估值承压
      </p>
      <p class="text-yellow-400 text-xs mt-2 bg-yellow-500/10 rounded p-2">
        📊 <b>T+7进展（7/30）：部分兑现</b>。
        油价从94美元回落至87美元，但加息预期仍然存在（9月加息概率59%）。
        科技成长股确实继续承压，存储芯片崩盘式下跌，但主因是行业自身（SK海力士不及预期+英伟达融资担忧）
        而非油价驱动。美联储7月按兵不动，加息预期较前期降温。
        结论：方向对但驱动因素不同，存储下跌更多是行业周期+估值原因。
      </p>
    </div>
    <div class="bg-white/5 rounded-lg p-3 border border-white/10">
      <div class="flex items-center justify-between mb-2">
        <span class="text-blue-400 font-semibold text-xs">预判 #20260723_002 · B级</span>
        <span class="text-white/50 text-xs">原验证日：7/28</span>
      </div>
      <p class="text-white/80 text-sm mb-2">
        <b>政策底+资金底支撑沪指3800点不破，市场进入震荡磨底阶段</b>
      </p>
      <p class="text-white/60 text-xs">
        逻辑：政策底明确→沪指3800-3950震荡→深市弱于沪市
      </p>
      <p class="text-green-400 text-xs mt-2 bg-green-500/10 rounded p-2">
        ✅ <b>T+7进展（7/30）：验证正确</b>。
        沪指7/29探底3782点后迅速回升收3828点，3800点支撑基本确认。
        深市/创业板继续弱于沪指（科创50唯一下跌），呈现"指数稳、个股调"格局。
        震荡磨底阶段特征明显，符合预判。
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
          <span class="text-red-400 font-semibold text-sm">预判 #20260730_001 · A级</span>
          <span class="text-white/50 text-xs">验证日：2026-08-04（T+3）</span>
        </div>
        <p class="text-white/80 text-sm mb-2">
          <b>存储芯片板块短期仍有下行空间，美光目标位650-700美元，A股存储板块继续调整</b>
        </p>
        <p class="text-white/60 text-xs">
          逻辑：SK海力士财报不及预期+英伟达融资担忧+行业扩产预期+高估值消化+美联储鹰派，
          多重利空叠加。美光从1213美元高点已跌至739美元（-39%），但参照历史周期调整幅度，
          可能还有10-15%下行空间。A股存储板块（雅克/兆易/长鑫等）受情绪传导，
          预计T+3内继续弱于大盘，不排除二次探底。
        </p>
      </div>
      <div class="bg-blue-500/10 border border-blue-500/30 rounded-lg p-3">
        <div class="flex items-center justify-between mb-2">
          <span class="text-blue-400 font-semibold text-sm">预判 #20260730_002 · B级</span>
          <span class="text-white/50 text-xs">验证日：2026-08-04（T+3）</span>
        </div>
        <p class="text-white/80 text-sm mb-2">
          <b>A股高低切换行情延续，消费/金融/防御板块相对收益优于科技成长</b>
        </p>
        <p class="text-white/60 text-xs">
          逻辑：外围科技股暴跌压制A股科技板块情绪，资金从高位科技撤出流向低位消费/金融，
          这种风格切换不会一两天结束。叠加中报季临近，业绩确定性高的消费/高股息板块更受青睐。
          预计T+3内消费ETF/红利指数跑赢科创50/创业板5%以上。
        </p>
      </div>
      <div class="bg-yellow-500/10 border border-yellow-500/30 rounded-lg p-3">
        <div class="flex items-center justify-between mb-2">
          <span class="text-yellow-400 font-semibold text-sm">预判 #20260730_003 · B级</span>
          <span class="text-white/50 text-xs">验证日：2026-08-06（T+5）</span>
        </div>
        <p class="text-white/80 text-sm mb-2">
          <b>黄金价格突破4200美元/盎司，创历史新高</b>
        </p>
        <p class="text-white/60 text-xs">
          逻辑：美联储按兵不动但通胀预期升温+地缘政治风险+全球央行去美元化购金+避险需求，
          多重利好叠加。COMEX黄金已达4134美元，距离4200仅一步之遥。
          若8月Jackson Hole沃什偏鸽或地缘局势升级，黄金有望快速突破。
          预计T+5内黄金冲击4200美元并站稳。
        </p>
      </div>
    </div>
  </div>
</div>'''
gen.add_section("预判验证闭环", verify_html, "🔄")

# ========== 8. 空方视角·风险提示 ==========
bear_html = '''
<div class="space-y-4">
  <div class="bg-gradient-to-br from-red-500/20 to-rose-500/10 border border-red-500/30 rounded-xl p-4">
    <h4 class="text-white font-semibold mb-3 flex items-center gap-2">
      <span>🐻</span> 空方视角：五大风险不容忽视
    </h4>
    <p class="text-white/50 text-xs mb-3">
      报告不仅要讲机会，更要讲风险。以下是空方可能证伪当前判断的五大角度：
    </p>
  </div>

  <div class="bg-white/5 rounded-xl p-4 border border-white/10">
    <div class="flex items-start gap-3">
      <span class="text-red-400 text-lg font-bold">1</span>
      <div>
        <h5 class="text-white font-semibold text-sm mb-1">AI资本开支泡沫破裂：存储芯片只是第一张多米诺骨牌</h5>
        <p class="text-white/60 text-xs leading-relaxed">
          英伟达为OpenAI提供2500亿美元融资担保，这种"借钱给客户买自己芯片"的模式，
          被市场类比为2000年电信泡沫。如果AI资本开支的真实需求被证伪，
          整个半导体产业链都将面临估值重构。存储芯片只是第一个倒下的，
          接下来可能是算力芯片（英伟达）、光模块、服务器……整条AI硬件链条都面临巨大调整风险。
          当前全球AI科技股市值已超15万亿美元，一旦泡沫破裂，A股科技股也无法独善其身。
        </p>
      </div>
    </div>
  </div>

  <div class="bg-white/5 rounded-xl p-4 border border-white/10">
    <div class="flex items-start gap-3">
      <span class="text-red-400 text-lg font-bold">2</span>
      <div>
        <h5 class="text-white font-semibold text-sm mb-1">美联储9月加息靴子落地+缩表加速，全球流动性收紧</h5>
        <p class="text-white/60 text-xs leading-relaxed">
          虽然7月按兵不动，但3票反对+沃什鹰派表态显示加息周期并未结束。
          若8月通胀数据反弹，9月加息几乎板上钉钉。
          更可怕的是缩表加速——美联储资产负债表仍在以每月950亿美元的速度缩减。
          全球美元流动性收紧，新兴市场面临资本外流压力，A股也将受到波及。
          历史上美联储加息周期末期往往伴随金融危机，当前韩国股市已率先崩盘（年内九次熔断）。
        </p>
      </div>
    </div>
  </div>

  <div class="bg-white/5 rounded-xl p-4 border border-white/10">
    <div class="flex items-start gap-3">
      <span class="text-red-400 text-lg font-bold">3</span>
      <div>
        <h5 class="text-white font-semibold text-sm mb-1">中报业绩雷区：科技股估值杀远未结束</h5>
        <p class="text-white/60 text-xs leading-relaxed">
          铜冠铜箔中报预增486%却接近跌停的案例表明，市场对科技股的业绩预期已经拔得极高。
          7-8月是中报密集披露期，更多科技股将面临"业绩好但不及预期"的尴尬。
          英维克一季报-82%，中报能转正吗？雅克科技动态PE 55倍，一旦业绩增速放缓，
          估值杀会非常惨烈。纯题材、无业绩支撑的小票将被无情抛弃。
          中报季可能是科技股调整的下半场催化剂。
        </p>
      </div>
    </div>
  </div>

  <div class="bg-white/5 rounded-xl p-4 border border-white/10">
    <div class="flex items-start gap-3">
      <span class="text-red-400 text-lg font-bold">4</span>
      <div>
        <h5 class="text-white font-semibold text-sm mb-1">韩股崩盘传导：高杠杆踩踏的连锁反应</h5>
        <p class="text-white/60 text-xs leading-relaxed">
          韩国KOSPI指数较6月高点回撤超43%，年内第九次触发熔断。
          韩国股市以高杠杆著称，下跌中的"追保平仓"负反馈螺旋已经启动。
          韩股芯片股（三星/SK海力士）是全球半导体板块的风向标，
          如果韩股继续崩盘，将通过情绪传导→外资流出→产业链估值下修等多渠道影响A股半导体板块。
          A股半导体/存储板块虽然有国产替代逻辑，但估值体系锚定海外，不可能完全脱钩。
        </p>
      </div>
    </div>
  </div>

  <div class="bg-white/5 rounded-xl p-4 border border-white/10">
    <div class="flex items-start gap-3">
      <span class="text-red-400 text-lg font-bold">5</span>
      <div>
        <h5 class="text-white font-semibold text-sm mb-1">地缘政治黑天鹅：中东/台海/中美关系</h5>
        <p class="text-white/60 text-xs leading-relaxed">
          中东局势虽然边际缓和（油价回落），但根本矛盾未解决，随时可能再度升级。
          中美关系在科技领域的博弈持续加码，芯片出口管制可能进一步升级。
          台海局势也是潜在风险点。任何一个黑天鹅事件爆发，
          都可能引发全球股市剧烈波动，A股科技股首当其冲。
          当前市场对地缘风险的定价并不充分，投资者应保持警惕。
        </p>
      </div>
    </div>
  </div>

  <div class="bg-red-500/10 border border-red-500/30 rounded-xl p-4">
    <p class="text-red-300 text-sm font-semibold mb-2">⚠️ 空方结论</p>
    <p class="text-white/70 text-xs leading-relaxed">
      当前市场处于"政策底托底+外围顶施压"的夹缝中，
      沪指有护盘但科技股继续杀跌，结构性风险远大于系统性风险。
      存储芯片崩盘可能只是AI硬件泡沫破裂的开始，而非结束。
      建议：<b>严控仓位在1成以内，现金为王，等待更确定性机会</b>。
      不要被单日反弹诱惑，纪律比收益更重要。
      关注费城半导体指数走势是当前最重要的领先指标。
    </p>
  </div>
</div>'''
gen.add_section("空方视角·风险提示", bear_html, "🐻")

# ========== 9. 教训库引用 ==========
lesson_html = '''
<div class="space-y-3">
  <div class="bg-red-500/10 border border-red-500/30 rounded-lg p-3">
    <p class="text-red-300 font-semibold mb-1">教训#1：业绩好≠股价涨，要看预期差</p>
    <p class="text-white/60 text-xs">
      SK海力士Q2利润增557%、营收增257%，创历史新高，但股价暴跌9.61%。
      美光科技营收增346%，从高点回撤39%。再次验证"业绩好不等于股价涨"。
      <b>正确做法</b>：业绩要看"预期差"而非绝对增速，
      前期涨幅过大的标的，即便业绩好也可能"利好出尽"。
      铜冠铜箔预增486%跌停、SK海力士增557%暴跌——
      当市场预期已经打满，任何「不够好」都会引发抛售。
      买入前必须对标机构一致预期，确认是否真的超预期。
    </p>
  </div>

  <div class="bg-orange-500/10 border border-orange-500/30 rounded-lg p-3">
    <p class="text-orange-300 font-semibold mb-1">教训#2：不要接"飞刀"，趋势破了就先出来</p>
    <p class="text-white/60 text-xs">
      存储芯片板块从高点回撤30-40%，英维克回撤44%，
      每一次"抄底"的人都被套在半山腰。
      <b>正确做法</b>：趋势破位后第一时间减仓，
      不要有"跌了这么多应该反弹了"的侥幸心理。
      底部不是猜出来的，是走出来的——
      至少需要连续3日不创新低+缩量企稳+均线修复才能确认。
      宁可错过底部反弹10%，也不要在下跌途中被深套30%。
    </p>
  </div>

  <div class="bg-yellow-500/10 border border-yellow-500/30 rounded-lg p-3">
    <p class="text-yellow-300 font-semibold mb-1">教训#3：AI硬件泡沫的警钟已响</p>
    <p class="text-white/60 text-xs">
      英伟达为OpenAI提供2500亿美元融资担保，被市场类比为2000年电信泡沫。
      历史总是惊人地相似——运营商借钱买设备→设备商股价暴涨→泡沫破裂。
      <b>正确做法</b>：对AI硬件链保持清醒，长期逻辑不代表短期没有大调整。
      2000年互联网泡沫破裂后，亚马逊从107美元跌到6美元（-94%），
      但最终成为万倍股。问题是：你能扛住94%的回撤吗？
      控制仓位+顺势而为比信仰更重要。
    </p>
  </div>

  <div class="bg-amber-500/10 border border-amber-500/30 rounded-lg p-3">
    <p class="text-amber-300 font-semibold mb-1">教训#4：ST股不能碰，越跌越不能补</p>
    <p class="text-white/60 text-xs">
      *ST建艺从13.45元跌到8.97元，浮亏约-33%，期间任何补仓只会扩大亏损。
      退市风险下，底部可能就是退市清零。
      <b>正确做法</b>：ST股坚决不碰，一旦持仓变ST必须第一时间清仓，不存任何幻想。
      退市股归零的风险是永久性损失，不值得用本金去赌重组概率。
      今天*ST建艺微涨1.24%，不要被迷惑——这是离场机会，不是反转信号。
    </p>
  </div>

  <div class="bg-purple-500/10 border border-purple-500/30 rounded-lg p-3">
    <p class="text-purple-300 font-semibold mb-1">教训#5：外围是A股科技股的风向标</p>
    <p class="text-white/60 text-xs">
      费城半导体指数走势是A股半导体板块的领先指标。
      美股存储芯片崩盘，A股存储板块第二天必然跟跌。
      韩股芯片股崩盘（年内九次熔断），A股也会受情绪传导。
      <b>正确做法</b>：做A股科技股必须看隔夜美股和韩股走势。
      费半指数趋势向下时，不抄底A股半导体；
      等外围企稳后再考虑进场，宁可错过也不做错。
      昨晚费半跌5.33%，今天A股科技股压力山大。
    </p>
  </div>
</div>'''
gen.add_section("教训库引用", lesson_html, "📚")

# ========== 生成+发布 ==========
output_path = os.path.join(WORK_DIR, 'docs/daily/20260730_每日新闻洞察.html')
result = gen.publish(output_path=output_path)
print("发布结果:", result)
print("成功:", result.get('success', False))
print("报告路径:", output_path)
print("文件大小:", os.path.getsize(output_path), "字节")

# 更新 latest.html
latest_path = os.path.join(WORK_DIR, 'docs/daily/latest.html')
shutil.copy2(output_path, latest_path)
print("latest.html 已更新")
