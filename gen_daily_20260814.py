#!/usr/bin/env python3
"""2026年8月14日 每日新闻洞察生成 - 周五·费半逆势涨0.87%·工业富联中报净利翻倍·CME推出算力期货·源杰科技43亿扩产·SK海力士大连NAND扩50%"""
import sys, os, shutil, json
WORK_DIR = '/root/daily-news-insight'
sys.path.insert(0, os.path.join(WORK_DIR, 'v3'))
from generators.daily_pro import DailyReportProGenerator

gen = DailyReportProGenerator(
    date_str='2026年8月14日', weekday='星期五',
    subtitle='2026年8月14日 周五 · 美股齐涨纳指+0.81%·闪迪+13.67%引爆存储·央行1万亿买断式逆回购·A股放量跌4300股·算力成唯一科技活口',
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
        '美股全线收涨：道指+0.13%、标普+0.65%、纳指+0.81%；费城半导体+0.46%进入技术性牛市；存储板块大爆发，闪迪+13.67%、海力士+9%、美光+4.23%',
        '闪迪投资者日炸裂：NAND市场2027年将达5000亿美元，2028-2030年营收中高双位数增长、毛利率约80%、FCF利润率约50%；AI推理驱动存储需求爆发',
        '央行大动作：8月14日开展10000亿元6个月期买断式逆回购（等量续作），叠加3个月期加量2000亿，8月合计净投放2000亿，配合2.77万亿政府债发行',
        'A股放量跳水：沪指-0.50%失守3940，深成指-0.87%，两市成交2.55万亿放量下跌，4300+个股下跌；机器人/有色/军工重挫，算力液冷成唯一科技活口',
        '持仓策略：雅克科技-3.67%放量大跌，铜冠铜箔-1.06%，英维克-1%，科技高位股集体回调；逢高减仓纪律不变，关注存储板块外溢机会'
    ],
    operation_advice='隔夜美股存储大爆发+央行万亿流动性呵护，今日A股或有修复但分化加剧；科技高位股继续减仓，存储材料/设备方向关注外溢机会，仓位4成防御为主',
    risk_level='中等偏高',
    suggested_position='3-4成'
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
    description='每日新闻洞察 2026年8月14日：美股齐涨纳指+0.81%、闪迪+13.67%引爆存储、央行1万亿买断式逆回购、A股放量跌4300股',
)

gen.add_global_market()

global_cards1 = render_cards([
    {"name":"道琼斯","change":"+0.13%","up":True},
    {"name":"标普500","change":"+0.65%","up":True},
    {"name":"纳斯达克","change":"+0.81%","up":True},
    {"name":"费城半导体","change":"+0.46%","up":True},
    {"name":"日经225","change":"-0.90%","up":False},
    {"name":"恒生指数","change":"-0.17%","up":False},
])
global_list1 = render_list([
    {"name":"WTI原油","change":"-0.08%/$81.18","up":False},
    {"name":"布伦特原油","change":"-0.06%/$87.02","up":False},
    {"name":"COMEX黄金","change":"-0.37%/$4404","up":False},
    {"name":"COMEX白银","change":"-0.60%/$64.61","up":False},
])
global_list2 = render_list([
    {"name":"三星电子","change":"+4.89%","up":True},
    {"name":"SK海力士","change":"+5.92%","up":True},
    {"name":"美光科技","change":"+4.23%","up":True},
    {"name":"台积电ADR","change":"+0.31%","up":True},
])
global_list3 = render_list([
    {"name":"英伟达","change":"+0.54%/$225.30","up":True},
    {"name":"AMD","change":"+0.02%/$483.01","up":True},
    {"name":"微软","change":"+0.90%/$496.88","up":True},
    {"name":"苹果","change":"+1.00%/$305.26","up":True},
    {"name":"博通","change":"+0.43%/$417.82","up":True},
    {"name":"英特尔","change":"+3.58%/$104.56","up":True},
    {"name":"应用材料","change":"-2.48%/$534.54","up":False},
    {"name":"阿斯麦","change":"+2.09%/$1847.90","up":True},
])

global_html = '''
<div class="grid md:grid-cols-3 gap-4">
  <div class="md:col-span-2">
    <div class="text-white font-semibold mb-3 flex items-center gap-2"><span>🌍</span><span>隔夜全球市场 · 存储史诗级暴涨·闪迪+13.67%·NAND开启5000亿时代</span></div>
    <div class="grid grid-cols-3 md:grid-cols-6 gap-2">{0}</div>
    <p class="text-xs text-white/50 mt-3 leading-relaxed">
      ⚡ <b class="text-yellow-400">核心要点：美股三大指数全线收涨，纳指+0.81%；费城半导体指数+0.46%正式进入技术性牛市；存储板块史诗级爆发，闪迪+13.67%、SK海力士+5.92%、美光+4.23%；特斯拉+3.8%领涨七巨头；黄金微跌原油持平</b>——<br>
      ①<b>存储板块大爆发</b>：闪迪投资者日公布超级指引，NAND市场2027年将达5000亿美元，2028-2030年营收中高双位数增长、毛利率约80%、FCF利润率约50%。股价单日暴涨13.67%创数月最大涨幅。SK海力士+5.92%、美光科技+4.23%、西部数据+7%。AI推理驱动数据中心存储需求爆发，KV Cache重塑存储架构，企业级SSD供不应求。<br>
      ②<b>费半进入技术性牛市</b>：费城半导体指数+0.46%收12456点，较近期低点反弹超20%，正式宣告技术性牛市。CoreWeave、超微电脑等AI算力公司财报超预期，验证AI资本开支依然强劲。英特尔+3.58%、阿斯麦+2.09%。<br>
      ③<b>科技七巨头多数上涨</b>：特斯拉+3.80%（马斯克称AI收入9月首超其他业务）、Meta+2.74%、苹果+1.00%、微软+0.90%、英伟达+0.54%；仅亚马逊-0.80%下跌。整体风险偏好回升。<br>
      ④<b>经济数据温和</b>：美国7月PPI同比+4.7%低于预期4.9%，初请失业金20.9万人高于预期。美联储9月加息概率维持低位（约38%），市场预期通胀压力逐步缓解。<br>
      ⑤<b>原油黄金小幅回落</b>：WTI原油微跌0.08%收81.18美元，布伦特-0.06%收87.02美元。霍尔木兹海峡僵局仍存但市场逐步消化。COMEX黄金-0.37%收4404美元。<br>
      ⑥<b>中概股下跌</b>：纳斯达克中国金龙指数-1.84%，京东-7.31%、拼多多-5.46%、阿里巴巴-2.44%。
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
    <div class="text-xl font-bold text-green-400">3926.96</div>
    <div class="text-xs text-green-400">-0.50%</div>
  </div>
  <div class="bg-gradient-to-br from-green-500/20 to-emerald-500/10 border border-green-500/30 rounded-xl p-3 text-center">
    <div class="text-xs text-white/60 mb-1">深证成指</div>
    <div class="text-xl font-bold text-green-400">14289.44</div>
    <div class="text-xs text-green-400">-0.87%</div>
  </div>
  <div class="bg-gradient-to-br from-green-500/20 to-emerald-500/10 border border-green-500/30 rounded-xl p-3 text-center">
    <div class="text-xs text-white/60 mb-1">创业板指</div>
    <div class="text-xl font-bold text-green-400">3586.04</div>
    <div class="text-xs text-green-400">-0.45%</div>
  </div>
  <div class="bg-gradient-to-br from-green-500/20 to-emerald-500/10 border border-green-500/30 rounded-xl p-3 text-center">
    <div class="text-xs text-white/60 mb-1">科创50</div>
    <div class="text-xl font-bold text-green-400">1709.00</div>
    <div class="text-xs text-green-400">-1.11%</div>
  </div>
</div>

<div class="grid md:grid-cols-2 gap-4">
  <div class="bg-white/5 rounded-xl p-4">
    <h4 class="text-white font-semibold mb-3 flex items-center gap-2"><span>📉</span> 领跌板块</h4>
    <div class="space-y-1 text-xs">
      <div class="flex justify-between"><span class="text-white/70">人形机器人/自动化</span><span class="text-green-400">-3%~-5%</span></div>
      <div class="flex justify-between"><span class="text-white/70">有色金属/稀土</span><span class="text-green-400">-2%~-4%</span></div>
      <div class="flex justify-between"><span class="text-white/70">军工/航天装备</span><span class="text-green-400">-2%~-3%</span></div>
      <div class="flex justify-between"><span class="text-white/70">锂电/新能源车</span><span class="text-green-400">-2%~-3%</span></div>
      <div class="flex justify-between"><span class="text-white/70">半导体设备材料</span><span class="text-green-400">-1%~-2%</span></div>
    </div>
  </div>
  <div class="bg-white/5 rounded-xl p-4">
    <h4 class="text-white font-semibold mb-3 flex items-center gap-2"><span>📈</span> 领涨/抗跌板块</h4>
    <div class="space-y-1 text-xs">
      <div class="flex justify-between"><span class="text-white/70">医药生物/CRO</span><span class="text-red-400">+1%~+3%</span></div>
      <div class="flex justify-between"><span class="text-white/70">白酒/食品饮料</span><span class="text-red-400">+0.5%~+1%</span></div>
      <div class="flex justify-between"><span class="text-white/70">电力/公用事业</span><span class="text-red-400">+0.3%~+0.8%</span></div>
      <div class="flex justify-between"><span class="text-white/70">算力租赁/液冷</span><span class="text-red-400">相对抗跌</span></div>
      <div class="flex justify-between"><span class="text-white/70">PCB/铜箔</span><span class="text-yellow-400">分化震荡</span></div>
    </div>
  </div>
</div>

<div class="bg-white/5 rounded-xl p-4">
  <h4 class="text-white font-semibold mb-3 flex items-center gap-2"><span>🔍</span> 昨日核心逻辑深度拆解</h4>
  <div class="text-xs text-white/70 space-y-3 leading-relaxed">
    <div class="bg-white/5 rounded-lg p-3">
      <p class="text-yellow-400 font-semibold mb-1">① 放量下跌=资金集中兑现，2.55万亿成交天量</p>
      <p>两市成交2.55万亿较前日放量近4000亿，但下跌个股超4300只，属于典型的"放量调整"。主力资金净流出452亿元，尾盘出逃力度放大，内资集中结账离场是核心原因。赚钱效应极差，涨跌中位数-1.12%。</p>
    </div>
    <div class="bg-white/5 rounded-lg p-3">
      <p class="text-yellow-400 font-semibold mb-1">② 热门赛道集体退潮，高低切换极致明显</p>
      <p>前期最强主线人形机器人集体重挫（宇树科技打新落地利好出尽），有色金属/军工/锂电等高位赛道同步杀估值。资金从高位成长全面转向防御——医药超跌反弹、白酒电力抗跌。风格切换速度极快，市场无主流抱团主线。</p>
    </div>
    <div class="bg-white/5 rounded-lg p-3">
      <p class="text-yellow-400 font-semibold mb-1">③ 中报窗口+新股抽血，双重压制市场情绪</p>
      <p>8月中下旬进入中报密集披露期，资金对高位题材、业绩不确定个股提前避险。叠加新股密集发行（长鑫科技、宇树科技等巨无霸），场内资金被持续分流。当前市场处于"炒业绩、炒超跌"而非"炒题材"阶段。</p>
    </div>
    <div class="bg-white/5 rounded-lg p-3">
      <p class="text-yellow-400 font-semibold mb-1">④ 算力液冷成唯一科技活口，资金抱团取暖</p>
      <p>在全市场题材退潮环境下，AI算力/液冷/租赁是科技赛道唯一保持相对强势的方向。行业数据持续验证高景气（液冷从可选方案升级为刚性基础设施），叠加下半年AI算力需求旺季预期，成为资金唯一愿意坚守的科技主线。</p>
    </div>
  </div>
</div>

<div class="bg-yellow-500/10 border border-yellow-500/30 rounded-xl p-4">
  <h4 class="text-yellow-300 font-semibold mb-2 flex items-center gap-2"><span>🎯</span> 今日展望（8月14日周五）</h4>
  <p class="text-xs text-white/70 leading-relaxed">
    隔夜美股全线收涨+存储板块大爆发+央行1万亿买断式逆回购，三重利好给今日A股提供情绪支撑。但昨日放量下跌后，市场信心需要修复，预计今日大概率震荡反弹而非V型反转。<br>
    <b class="text-yellow-400">操作策略：</b>仓位控制在3-4成防御为主，不追高任何反弹。关注存储板块外溢机会（材料/设备），但昨日雅克科技-3.67%已提前反映"利好出尽"风险，不要追涨。
    医药/电力防御方向可继续持有，等待市场新主线确立。周五注意控制仓位过周末。
  </p>
</div>
</div>
'''
gen.add_section("A股昨日复盘与今日展望", ashare_html, "📊")

# 核心题材与今日催化
catalyst_html = '''
<div class="space-y-4">
  <div class="bg-gradient-to-br from-red-500/20 to-orange-500/10 border border-red-500/30 rounded-xl p-4">
    <h4 class="text-white font-semibold mb-3 flex items-center gap-2"><span>🔥</span> 催化一：闪迪投资者日炸裂，NAND市场2027年达5000亿美元【S级】</h4>
    <div class="text-xs text-white/70 space-y-2 leading-relaxed">
      <p><b class="text-yellow-400">事件：</b>闪迪周四在2026年投资者日公布长期增长战略：①NAND总市场2026年超3000亿、2027年达5000亿美元；②2028-2030财年营收中高双位数增长；③非GAAP毛利率约80%、营业利润率约75%；④FCF利润率约50%，超额现金100%返还股东。股价单日暴涨13.67%。</p>
      <p><b class="text-yellow-400">核心逻辑：</b>AI从训练向推理转移，KV Cache正在重塑AI系统的内存和存储层级，未来AI数据中心将变得更加"存储密集型"。企业级SSD占总位元出货量已达48%，供应紧张推动行业营收创历史新高。闪迪已与8家客户签署NBM长期供应协议，覆盖2027财年一半以上出货量。</p>
      <p><b class="text-yellow-400">A股映射：</b>存储芯片/材料/设备方向有望受益。但注意A股存储板块昨日已下跌（雅克科技-3.67%），说明国内资金更关注中报业绩而非远期预期。短线可能高开，但持续性需要观察。</p>
      <p><b class="text-yellow-400">受益标的：</b>雅克科技（前驱体）、华海诚科（塑封料）、长江存储产业链、北方华创（设备）、中微公司（刻蚀）</p>
    </div>
  </div>

  <div class="bg-gradient-to-br from-orange-500/20 to-yellow-500/10 border border-orange-500/30 rounded-xl p-4">
    <h4 class="text-white font-semibold mb-3 flex items-center gap-2"><span>💰</span> 催化二：央行1万亿买断式逆回购+8月合计净投放2000亿【A级】</h4>
    <div class="text-xs text-white/70 space-y-2 leading-relaxed">
      <p><b class="text-yellow-400">事件：</b>8月14日央行开展10000亿元6个月期买断式逆回购操作（等量续作），叠加8月5日3个月期加量2000亿，8月合计净投放2000亿元。同时8月14/17/18/19日开展隔夜逆回购（每日上限6000亿）。</p>
      <p><b class="text-yellow-400">政策意图：</b>配合2.77万亿政府债发行，对冲MLF等1.9万亿到期资金，保持流动性充裕。体现二季度货币政策执行报告中"加大逆周期调节力度"的表态。货币、财政政策协同发力。</p>
      <p><b class="text-yellow-400">市场影响：</b>流动性充裕支撑市场估值，对债市和股市均构成利好。但昨日A股放量下跌说明流动性宽松不等于股市上涨，关键还看盈利预期和风险偏好。对今日市场有托底作用。</p>
    </div>
  </div>

  <div class="bg-gradient-to-br from-blue-500/20 to-cyan-500/10 border border-blue-500/30 rounded-xl p-4">
    <h4 class="text-white font-semibold mb-3 flex items-center gap-2"><span>📊</span> 催化三：费半指数进入技术性牛市，AI资本开支超预期【A级】</h4>
    <div class="text-xs text-white/70 space-y-2 leading-relaxed">
      <p><b class="text-yellow-400">事件：</b>费城半导体指数周四收涨0.46%报12456点，较近期低点反弹超20%，正式进入技术性牛市。CoreWeave、超微电脑等AI算力公司财报超预期。</p>
      <p><b class="text-yellow-400">核心逻辑：</b>AI资本开支依然强劲，不是泡沫而是真实业绩。CoreWeave Q2营收同比翻倍，超微电脑EPS超预期84%。这些数据直接验证了AI算力需求的真实性，为整个产业链提供基本面支撑。</p>
      <p><b class="text-yellow-400">A股映射：</b>算力硬件/液冷/服务器方向有情绪支撑，但A股科技股昨日集体回调，能否跟涨取决于内资信心。英维克/液冷方向是A股算力产业链中最有业绩验证的环节。</p>
    </div>
  </div>

  <div class="bg-gradient-to-br from-purple-500/20 to-pink-500/10 border border-purple-500/30 rounded-xl p-4">
    <h4 class="text-white font-semibold mb-3 flex items-center gap-2"><span>⚔️</span> 催化四：地缘风险升温——霍尔木兹+黑海+红海三线并发【B级】</h4>
    <div class="text-xs text-white/70 space-y-2 leading-relaxed">
      <p><b class="text-yellow-400">事件：</b>四大地缘冲突集中爆发：①美伊对峙升级，伊朗议会通过霍尔木兹海峡管控法案；②黑海双向打击，俄乌互袭港口；③红海袭船，胡塞武装打击沙特油轮；④格陵兰叫停美企石油勘探。</p>
      <p><b class="text-yellow-400">影响：</b>原油维持高位（布伦特87美元），全球供应链承压，避险情绪升温。如果地缘冲突进一步恶化，可能推高通胀预期，影响全球央行降息节奏。</p>
      <p><b class="text-yellow-400">A股影响：</b>油气/黄金/军工等避险板块可能有脉冲行情，但持续性取决于局势发展。对科技成长股偏利空。</p>
    </div>
  </div>

  <div class="bg-white/5 rounded-xl p-4">
    <h4 class="text-white font-semibold mb-3">📅 今日重要事件日历</h4>
    <div class="text-xs text-white/70 space-y-1">
      <p>• <b>09:20</b> 央行10000亿元6个月期买断式逆回购招标</p>
      <p>• <b>晚间</b> 美国7月零售销售数据</p>
      <p>• <b>盘后</b> 中国移动、海光信息披露2026半年报</p>
      <p>• <b>全天</b> 中报密集披露期</p>
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
          <div class="text-xl font-bold text-green-400">55.45</div>
          <div class="text-xs text-green-400">-1.00%</div>
        </div>
      </div>
      <div class="text-xs text-white/60 mb-2">总市值 707亿 | 换手率 3.87% | 成交额 24.89亿</div>
      <div class="bg-yellow-500/10 border border-yellow-500/30 rounded-lg p-2 mb-2">
        <p class="text-yellow-300 text-xs font-semibold">⚡ 状态：冲高回落·弱势震荡·筹码成本63.83元</p>
      </div>
      <div class="text-xs text-white/70 leading-relaxed space-y-1">
        <p><b>昨日走势：</b>开盘56.82→最高57.87→最低55.37→收55.45元，冲高回落2.42元，典型的高位遇阻形态。</p>
        <p><b>利好：</b>①隔夜美股AI算力股大涨（CoreWeave+19%），液冷赛道基本面持续验证；②国产液冷从送样进入批量交付阶段；③32位分析师一致买入（目标价113元）。</p>
        <p><b>风险：</b>①股价从低点反弹已20%+，但成交量未放大，反弹力度偏弱；②筹码平均成本63.83元，上方套牢盘沉重；③A股科技股整体退潮，液冷难以独善其身。</p>
        <p><b class="text-yellow-400">操作建议：</b>反弹减仓策略不变。57-58元区间继续减仓，跌破52元清仓止损。隔夜美股算力大涨可能带来高开，但高开就是减仓机会，不要追涨。</p>
      </div>
    </div>

    <!-- 铜冠铜箔 -->
    <div class="bg-white/5 rounded-xl p-4 border border-orange-500/20">
      <div class="flex items-center justify-between mb-2">
        <h4 class="text-white font-semibold flex items-center gap-2"><span>🟠</span> 铜冠铜箔 (301217)</h4>
        <div class="text-right">
          <div class="text-xl font-bold text-green-400">119.23</div>
          <div class="text-xs text-green-400">-1.06%</div>
        </div>
      </div>
      <div class="text-xs text-white/60 mb-2">总市值 1005亿 | 换手率 3.60% | 成交额 37亿</div>
      <div class="bg-yellow-500/10 border border-yellow-500/30 rounded-lg p-2 mb-2">
        <p class="text-yellow-300 text-xs font-semibold">⚡ 状态：高位震荡·冲高回落·千亿市值后分化</p>
      </div>
      <div class="text-xs text-white/70 leading-relaxed space-y-1">
        <p><b>昨日走势：</b>开盘121.50→最高126.35→最低121.28→收119.23元，再次冲高回落，上影线7.12元，上方压力巨大。</p>
        <p><b>利好：</b>①PCB铜箔供需紧张逻辑不变，AI服务器带动高端铜箔需求；②市值突破千亿后进入机构视野；③业绩弹性大。</p>
        <p><b>风险：</b>①连续两日冲高回落，高位放量滞涨信号明显；②市盈率236倍严重透支；③覆铜板概念股盘初走弱，板块联动风险。</p>
        <p><b class="text-yellow-400">操作建议：</b>高位股冲高回落=减仓信号，严格执行。120元以上继续减仓至1/3底仓。不要抱有"明天还会涨"的幻想，减仓后等调整到位再接回更主动。</p>
      </div>
    </div>

    <!-- 雅克科技 -->
    <div class="bg-white/5 rounded-xl p-4 border border-purple-500/20">
      <div class="flex items-center justify-between mb-2">
        <h4 class="text-white font-semibold flex items-center gap-2"><span>🔬</span> 雅克科技 (002409)</h4>
        <div class="text-right">
          <div class="text-xl font-bold text-green-400">149.50</div>
          <div class="text-xs text-green-400">-3.67%</div>
        </div>
      </div>
      <div class="text-xs text-white/60 mb-2">总市值 712亿 | 换手率 10.19% | 成交额 50.16亿</div>
      <div class="bg-red-500/10 border border-red-500/30 rounded-lg p-2 mb-2">
        <p class="text-red-300 text-xs font-semibold">⚠️ 警报：放量大跌3.67%·换手率超10%·主力出逃</p>
      </div>
      <div class="text-xs text-white/70 leading-relaxed space-y-1">
        <p><b>昨日走势：</b>开盘158.10→最高158.60→最低149.38→收149.50元，高开低走放量大跌9.1元，换手率10.19%创近期新高，主力大幅出逃。</p>
        <p><b>利好：</b>①隔夜闪迪+13.67%+存储超级周期逻辑，今日可能有反弹；②SK海力士扩产+存储涨价周期，前驱体材料需求确定性强。</p>
        <p><b>风险：</b>①放量大跌是明确的短期见顶信号，换手率10%+意味着筹码大规模交换；②从跌停价127元反弹至158元（+24%），反弹幅度已经不小；③中报临近，业绩能否支撑70倍PE存疑。</p>
        <p><b class="text-yellow-400">操作建议：</b>隔夜存储板块大涨可能带来高开反弹，但<b class="text-red-400">高开就是减仓机会</b>。150-155元区间坚决减仓，高开高走也不要追，逢高分批减。
        教训库第2条：高位股冲高回落=见顶信号，立即减仓。如果今天低开，观察145元支撑，破位继续减。</p>
      </div>
    </div>

    <!-- *ST建艺 -->
    <div class="bg-white/5 rounded-xl p-4 border border-red-500/30">
      <div class="flex items-center justify-between mb-2">
        <h4 class="text-white font-semibold flex items-center gap-2"><span>⚠️</span> *ST建艺 (002789)</h4>
        <div class="text-right">
          <div class="text-xl font-bold text-red-400">退市风险</div>
          <div class="text-xs text-red-400">立即清仓·不要抱幻想</div>
        </div>
      </div>
      <div class="bg-red-500/10 border border-red-500/30 rounded-lg p-3 mb-3">
        <p class="text-red-300 text-xs font-semibold">⚠️ 最高优先级：立即清仓止损，退市风险敞口必须关闭</p>
      </div>
      <div class="text-xs text-white/70 leading-relaxed">
        <p><b class="text-yellow-400">📰 最新动态</b>：退市风险股，公司推进重组已提交摘帽申请但结果未知，存在重大不确定性。</p>
        <p class="mt-2"><b class="text-yellow-400">⚡ 操作策略</b>：退市风险股，任何价格立即清仓。退市风险+债务问题未消除，不要抱有任何幻想。ST股的基本面不会因为股价反弹而改善，早一天减仓少一分风险。</p>
      </div>
    </div>
  </div>

  <div class="bg-white/5 rounded-xl p-4">
    <h4 class="text-white font-semibold mb-3 flex items-center gap-2"><span>📋</span> 组合总览与今日策略</h4>
    <div class="text-xs text-white/70 space-y-2 leading-relaxed">
      <p><b class="text-yellow-400">昨日表现</b>：持仓全线下跌，雅克科技-3.67%领跌（放量大跌），铜冠铜箔-1.06%、英维克-1.00%，*ST建艺风险持续。组合整体跑输大盘（沪指-0.50%），科技高位股回调压力加大。</p>
      <p><b class="text-yellow-400">今日策略（8月14日周五）：</b><br>
      ① 隔夜美股存储大爆发+央行万亿流动性，今日A股科技股或有高开反弹。但<b class="text-red-400">反弹=减仓机会</b>，不是加仓理由。昨日放量下跌+4300股下跌，市场信心需要时间修复；<br>
      ② <b>雅克科技</b>：隔夜闪迪+13%可能带来高开，150-155元区间坚决减仓，高开高走也不要追，逢高分批减；<br>
      ③ <b>铜冠铜箔</b>：连续两日冲高回落，高位见顶信号明确，120元以上继续减仓至1/3底仓；<br>
      ④ <b>英维克</b>：算力液冷是唯一科技活口，但个股走势偏弱，57-58元反弹减仓，跌破52元清仓；<br>
      ⑤ <b>*ST建艺</b>：立即清仓（最高优先级）；<br>
      ⑥ 整体仓位3-4成，防御为主。周五尾盘通常有资金避险，注意控制仓位过周末。
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
    <h4 class="text-red-300 font-semibold mb-3 flex items-center gap-2"><span>🐻</span> 空方观点：放量下跌信号危险·科技股估值回归·中报暴雷潮来袭</h4>
    <div class="text-xs text-white/70 space-y-3 leading-relaxed">
      <div class="bg-white/5 rounded-lg p-3">
        <p class="text-red-300 font-semibold mb-1">风险1：2.55万亿放量下跌=主力大规模出逃，不是洗盘</p>
        <p>昨日两市成交2.55万亿放量下跌，主力资金净流出452亿，4300+个股下跌。放量下跌是真金白银的出逃，不是"洗盘"。前几日2万亿左右的成交量还能维持普涨，昨日放量反而普跌，说明增量资金已经不来了，剩下的都是存量博弈中的互相踩踏。</p>
      </div>
      <div class="bg-white/5 rounded-lg p-3">
        <p class="text-red-300 font-semibold mb-1">风险2：科技高位股集体回调，估值回归才刚刚开始</p>
        <p>雅克科技70倍PE、铜冠铜箔236倍PE、英维克146倍PE——这些估值都是建立在"AI超级周期永远持续"的假设上。一旦市场开始怀疑需求增速，估值回归的空间巨大。美股闪迪即使涨13%，其估值也远低于A股科技股的泡沫水平。</p>
      </div>
      <div class="bg-white/5 rounded-lg p-3">
        <p class="text-red-300 font-semibold mb-1">风险3：中报密集披露期，业绩暴雷潮来袭</p>
        <p>8月中下旬进入中报密集披露窗口。很多"AI概念股"业绩根本跟不上股价涨幅，一旦中报低于预期，就是戴维斯双杀。工业富联"利好出尽"的教训还在眼前，接下来会有更多公司上演"业绩越炸股价越跌"的戏码。</p>
      </div>
      <div class="bg-white/5 rounded-lg p-3">
        <p class="text-red-300 font-semibold mb-1">风险4：新股抽血效应加剧，存量资金不堪重负</p>
        <p>长鑫科技（3.28万亿市值）、宇树科技（610亿）、源杰科技港股IPO……硬科技IPO一个接一个，从A股市场抽血。2.55万亿的成交量看似很大，但架不住IPO+解禁+减持三大抽水机同时运转。存量博弈下，重心只能下移。</p>
      </div>
      <div class="bg-white/5 rounded-lg p-3">
        <p class="text-red-300 font-semibold mb-1">风险5：地缘风险黑天鹅随时可能升级</p>
        <p>霍尔木兹海峡、黑海、红海三战并发。如果局势进一步恶化，油价飙升→通胀回升→美联储推迟降息→科技股杀估值，传导链条非常清晰。当前市场对地缘风险定价严重不足。</p>
      </div>
    </div>
  </div>

  <div class="bg-green-500/10 border border-green-500/30 rounded-xl p-4">
    <h4 class="text-green-300 font-semibold mb-3 flex items-center gap-2"><span>🐂</span> 多方反驳：存储超级周期+流动性宽松+政策托底三支撑</h4>
    <div class="text-xs text-white/70 space-y-2 leading-relaxed">
      <p>① <b>存储超级周期才刚开始</b>：闪迪投资者日明确NAND市场2027年达5000亿美元，整个行业的景气度才走了一半。A股存储材料/设备公司的业绩爆发期还在后面，现在的估值不算贵。</p>
      <p>② <b>央行流动性呵护力度加大</b>：8月合计净投放2000亿买断式逆回购+隔夜逆回购每日6000亿，流动性非常充裕。二季度货币政策执行报告明确"加大逆周期调节力度"，政策底非常明确。</p>
      <p>③ <b>经济基本面在改善</b>：广东1-7月外贸+20.5%、人民币创2023年以来新高、企业利润逐步修复。经济企稳回升的大方向不变，股市调整后还会创新高。</p>
      <p>④ <b>美股技术性牛市带动全球风险偏好</b>：费城半导体进入技术性牛市，纳指继续走高。美股的科技牛市会通过港股和北向资金传导到A股，科技成长股中期向上趋势不变。</p>
      <p>⑤ <b>调整是健康的</b>：连续上涨后的正常回调，释放短线获利盘，有利于行情走得更远。沪指3900点支撑强劲，下跌空间有限。</p>
    </div>
  </div>

  <div class="bg-yellow-500/10 border border-yellow-500/30 rounded-xl p-4">
    <h4 class="text-yellow-300 font-semibold mb-2 flex items-center gap-2"><span>⚖️</span> 综合判断</h4>
    <p class="text-xs text-white/70 leading-relaxed">
      短期（1-2周）：A股处于"放量下跌后的修复期"，市场信心需要时间恢复。隔夜美股上涨+央行流动性呵护提供支撑，但上方3960-3980压力明显。科技高位股继续减仓，防御板块相对安全。<br>
      中期（1-3个月）：存储超级周期+AI算力需求爆发+国产替代加速，三大逻辑支撑科技成长股中期向好。但当前估值偏高，需要业绩中报验证，调整后优质标的将迎来更好的布局机会。<br>
      <b class="text-yellow-400">核心结论：短期谨慎，仓位3-4成防御为主。
      利用反弹减仓高位科技股，等待中报披露后的布局机会。
      关注存储板块外溢和医药超跌修复两个方向。</b>
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
          <span class="text-red-300 font-semibold">预判#20260812-01：算力期货催化算力产业链</span>
          <span class="text-xs bg-red-500/30 text-red-200 px-2 py-0.5 rounded">验证中·T+2</span>
        </div>
        <p class="text-white/70">预判内容：CME推出算力期货（H100/B200）是里程碑事件，将催化算力产业链情绪修复，GPU/服务器/液冷/光模块方向有望迎来2-3%的反弹，持续1-2个交易日。</p>
        <p class="text-white/50 mt-1">当前进度：T+2验证，周三A股科技股冲高回落、周四大面积下跌，算力期货题材未能形成持续反弹。验证结果偏负面——"新物种"题材发酵需要时间，短期催化效应有限。</p>
      </div>
      <div class="bg-yellow-500/10 border border-yellow-500/30 rounded-lg p-3">
        <div class="flex justify-between mb-2">
          <span class="text-yellow-300 font-semibold">预判#20260812-02：SK海力士扩产催化存储材料</span>
          <span class="text-xs bg-yellow-500/30 text-yellow-200 px-2 py-0.5 rounded">验证中·T+2</span>
        </div>
        <p class="text-white/70">预判内容：SK海力士大连NAND扩产50%，将催化半导体材料板块情绪，雅克科技、华海诚科等存储材料标的有望持续走强，中期（1-2周）涨幅5-10%。</p>
        <p class="text-white/50 mt-1">当前进度：T+2验证，周三雅克科技冲高回落（最高158.6元）、周四大跌3.67%（收149.5元）。短期来看催化效应不及预期，反而因为"利好出尽"导致资金出逃。中期（1-2周）仍有待观察。</p>
      </div>
      <div class="bg-green-500/10 border border-green-500/30 rounded-lg p-3">
        <div class="flex justify-between mb-2">
          <span class="text-green-300 font-semibold">预判#20260811-01：江波龙业绩催化存储修复</span>
          <span class="text-xs bg-green-500/30 text-green-200 px-2 py-0.5 rounded">验证中·T+2</span>
        </div>
        <p class="text-white/70">预判内容：江波龙半年净利暴增715倍+回购，将催化存储板块情绪修复，存储材料和芯片方向有望迎来3-5%的反弹。</p>
        <p class="text-white/50 mt-1">当前进度：T+2验证，周一雅克科技+4.34%、铜冠铜箔+4.47%（反弹幅度符合预期），但周二周三连续回调（雅克累计-5%+）。整体呈现"一日游"行情，反弹持续性不足。</p>
      </div>
      <div class="bg-green-500/10 border border-green-500/30 rounded-lg p-3">
        <div class="flex justify-between mb-2">
          <span class="text-green-300 font-semibold">预判#20260803-01：雅克科技跌停后3日内反弹</span>
          <span class="text-xs bg-green-500/30 text-green-200 px-2 py-0.5 rounded">已验证·正确</span>
        </div>
        <p class="text-white/70">预判内容：雅克科技跌停板机构抄底近5亿，预计3个交易日内出现5-10%反弹。</p>
        <p class="text-white/50 mt-1">实际走势：从8月4日跌停价127元反弹至最高158.6元（+25%），远超预期。验证正确，但反弹后回落速度也快。</p>
      </div>
      <div class="bg-green-500/10 border border-green-500/30 rounded-lg p-3">
        <div class="flex justify-between mb-2">
          <span class="text-green-300 font-semibold">预判#20260730-02：存储板块调整期2-3周</span>
          <span class="text-xs bg-green-500/30 text-green-200 px-2 py-0.5 rounded">已验证·正确</span>
        </div>
        <p class="text-white/70">预判内容：7月30日科技股大跌后，存储板块进入2-3周调整期，调整幅度约15-25%。</p>
        <p class="text-white/50 mt-1">当前进度：第11个交易日，板块从高点回调约20%后出现反弹但持续性不足。时间和幅度均验证正确，目前仍在调整周期内。</p>
      </div>
      <div class="bg-red-500/10 border border-red-500/30 rounded-lg p-3">
        <div class="flex justify-between mb-2">
          <span class="text-red-300 font-semibold">新增预判#20260814-01：闪迪投资者日催化存储板块二次反弹</span>
          <span class="text-xs bg-red-500/30 text-red-200 px-2 py-0.5 rounded">待验证·T+2</span>
        </div>
        <p class="text-white/70">预判内容：闪迪投资者日公布NAND 5000亿市场+80%毛利率超级指引，股价+13.67%创数月最大涨幅，将催化A股存储板块情绪修复。存储材料/设备方向有望迎来3-5%的高开反弹，但持续性取决于成交量和内资承接力度。</p>
        <p class="text-white/50 mt-1">验证时间：8月18日（T+2，下周一）验证反弹幅度和持续性</p>
      </div>
      <div class="bg-red-500/10 border border-red-500/30 rounded-lg p-3">
        <div class="flex justify-between mb-2">
          <span class="text-red-300 font-semibold">新增预判#20260814-02：A股短期调整延续至下周三</span>
          <span class="text-xs bg-red-500/30 text-red-200 px-2 py-0.5 rounded">待验证·T+5</span>
        </div>
        <p class="text-white/70">预判内容：A股昨日放量下跌（2.55万亿+4300股跌）后，短期调整需要3-5个交易日消化。沪指将在3850-3950区间震荡，科技高位股继续回调，防御板块相对抗跌。下周三前后可能出现新一轮布局机会。</p>
        <p class="text-white/50 mt-1">验证时间：8月21日（T+5）验证调整时间和空间</p>
      </div>
    </div>
  </div>

  <div class="bg-white/5 rounded-xl p-4">
    <h4 class="text-white font-semibold mb-2 flex items-center gap-2"><span>📊</span> 准确率统计</h4>
    <div class="grid grid-cols-3 gap-3 text-center text-xs">
      <div class="bg-white/5 rounded-lg p-2">
        <div class="text-lg font-bold text-yellow-400">67%</div>
        <div class="text-white/60">总体准确率</div>
      </div>
      <div class="bg-white/5 rounded-lg p-2">
        <div class="text-lg font-bold text-green-400">12/18</div>
        <div class="text-white/60">已验证正确/总数</div>
      </div>
      <div class="bg-white/5 rounded-lg p-2">
        <div class="text-lg font-bold text-blue-400">7</div>
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
      雅克科技昨日换手率10.19%、成交额50亿、BBD净流出3.83亿，这三个数据加在一起就是明确的见顶信号。
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
      铜冠铜箔连续两日冲高回落（8月12日最高126.4→收120.99，8月13日最高126.35→收119.23），
      雅克科技也是高开低走放量大跌。连续冲高回落不是巧合，是主力在"边拉边出"。
      <b>正确做法</b>：连续两天以上冲高回落，第三天开盘就应该减仓，
      不要等到"再涨一点就卖"——往往等不到再涨，就直接下去了。
      冲高回落的本质是：上方有大量抛压，每一次上涨都有人在卖。
      连续出现说明卖方力量远大于买方，短期见顶概率极大。
    </p>
  </div>

  <div class="bg-blue-500/10 border border-blue-500/30 rounded-lg p-3">
    <p class="text-blue-300 font-semibold mb-1">教训#5：周五要降仓，周末不确定性太多</p>
    <p class="text-white/60 text-xs">
      今天是周五！周末两天可能发生任何事情——地缘冲突升级、政策变动、海外市场波动。
      最近几个周末都出了大事（霍尔木兹海峡危机、美联储鹰派表态等）。
      很多人喜欢满仓过周末，赌周末出利好，结果往往是赌错了。
      <b>正确做法</b>：周五下午根据情况适当降低仓位，尤其是高位股和高波动股。
      留一部分现金，周末如果真出利好，周一追进去也来得及；
      如果出利空，你已经减仓了，损失可控。
      记住：在股市里，活着比赚快钱更重要。
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
</div>
'''
gen.add_section("教训库引用", lesson_html, "📚")

# 生成+发布
output_path = os.path.join(WORK_DIR, 'docs/daily/20260814_每日新闻洞察.html')
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
