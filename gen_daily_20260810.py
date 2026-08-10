#!/usr/bin/env python3
"""2026年8月10日 每日新闻洞察生成 - 周一·非农爆冷9月加息概率骤降·标普创新高·费半+2.56%·宇树科技申购人形机器人第一股·创业板算力ETF来袭·长鑫纳入MSCI"""
import sys, os, shutil, json
WORK_DIR = '/root/daily-news-insight'
sys.path.insert(0, os.path.join(WORK_DIR, 'v3'))
from generators.daily_pro import DailyReportProGenerator

gen = DailyReportProGenerator(
    date_str='2026年8月10日', weekday='星期一',
    subtitle='2026年8月10日 周一 · 非农爆冷-2.3万9月加息概率骤降40%·标普创历史新高·费半+2.56%光通信暴涨·宇树科技申购人形机器人第一股·创业板算力ETF密集申报·长鑫科技纳入MSCI',
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


# ========== V5.0 L2 特性配置 ==========
gen.set_tldr(
    key_points=[
        '非农爆冷：美国7月非农-2.3万（预期+8万），5-6月下修10.3万，9月加息概率从54%骤降至40%，美元跳水黄金暴涨',
        '美股科技全线反弹：标普创历史新高，纳指周涨5.19%，费半+2.56%周涨7.6%，光通信暴涨（Coherent+13%），存储分化（美光-0.44%）',
        '周末催化密集：央行下半年定调宽松+证监会10项两地合作新政+创业板算力ETF密集申报+宇树科技申购（人形机器人第一股610亿市值）+长鑫纳入MSCI',
        '持仓策略：铜冠铜箔/雅克科技趁反弹减仓机动仓，英维克50元防线持有观察，*ST建艺清仓纪律'
    ],
    operation_advice='外围利好+国内宽松双催化，周一高开概率大，但注意存储分化+光模块出口管制传闻，不追高，高开减仓机动仓做T',
    risk_level='中等',
    suggested_position='5-6成'
)

gen.set_quick_anchors([
    {'id': 'section-隔夜全球市场深度解读', 'title': '全球市场', 'icon': '🌍'},
    {'id': 'section-A股上周五复盘与今日展望', 'title': 'A股复盘', 'icon': '📊'},
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
    description='每日新闻洞察 2026年8月10日：非农爆冷9月加息概率骤降、标普创新高、费半+2.56%、宇树科技申购、创业板算力ETF来袭',
)

# ========== 1. 隔夜全球市场 ==========
gen.add_global_market()

global_cards1 = render_cards([
    {"name":"道琼斯","change":"+0.28%","up":True},
    {"name":"标普500","change":"+0.62%","up":True},
    {"name":"纳斯达克","change":"+1.30%","up":True},
    {"name":"费城半导体","change":"+2.56%","up":True},
    {"name":"日经225","change":"-0.90%","up":False},
    {"name":"恒生指数","change":"+0.54%","up":True},
])
global_list1 = render_list([
    {"name":"WTI原油","change":"+0.81%/$78.82","up":True},
    {"name":"布伦特原油","change":"+1.15%/$84.52","up":True},
    {"name":"COMEX黄金","change":"-0.02%/$4398.71","up":False},
    {"name":"COMEX白银","change":"+0.83%/$64.03","up":True},
])
global_list2 = render_list([
    {"name":"三星电子","change":"+0.22%","up":True},
    {"name":"SK海力士","change":"-4.88%","up":False},
    {"name":"美光科技","change":"-0.44%","up":False},
    {"name":"台积电ADR","change":"+0.44%","up":True},
])
global_list3 = render_list([
    {"name":"英伟达","change":"+2.27%/$223.96","up":True},
    {"name":"AMD","change":"-1.21%/$483.36","up":False},
    {"name":"微软","change":"+0.03%/$499.99","up":True},
    {"name":"苹果","change":"+0.29%/$313.33","up":True},
    {"name":"博通","change":"+1.71%/$427.76","up":True},
    {"name":"英特尔","change":"+1.84%/$101.65","up":True},
    {"name":"应用材料","change":"+2.21%/$539.14","up":True},
    {"name":"阿斯麦","change":"+2.15%/$1740.99","up":True},
])
global_html = '''
<div class="grid md:grid-cols-3 gap-4">
  <div class="md:col-span-2">
    <div class="text-white font-semibold mb-3 flex items-center gap-2"><span>🌍</span><span>隔夜全球市场 · 非农爆冷加息预期骤降·标普创历史新高·半导体光通信领涨·存储分化</span></div>
    <div class="grid grid-cols-3 md:grid-cols-6 gap-2">{0}</div>
    <p class="text-xs text-white/50 mt-3 leading-relaxed">
      ⚡ <b class="text-yellow-400">核心要点：美国7月非农就业-2.3万大爆冷（预期+8万），9月加息概率从54%骤降至40%，美元跳水黄金暴涨；美股三大指数全线收涨，标普500创历史新高，纳指+1.3%周涨5.19%，费城半导体+2.56%周涨7.6%</b>——<br>
      ①<b>非农史诗级爆冷</b>：美国7月非农就业减少2.3万人，为2026年2月以来首次负增长，远低于市场预期的+8万人。更关键的是5月和6月合计下修10.3万人（5月从12.9万下修至6.3万，6月从5.7万下修至2万）。失业率虽降至4.1%，但劳动参与率跌至61.4%（近50年新低），26.4万人退出劳动力市场——失业率下降是"人走了"而非"找到工作了"。<br>
      ②<b>加息预期彻底重估</b>：非农公布后，9月加息概率从约54%骤降至40%，市场开始押注美联储年内最多加息一次，甚至有降息预期。美元指数跳水至99.41，黄金白银暴涨，美债收益率下跌。全球流动性宽松预期升温，风险资产全面受益。<br>
      ③<b>半导体+光通信双轮驱动</b>：费城半导体指数+2.56%收12356.79，周涨7.6%。英伟达+2.27%周涨11.56%（SpaceX独家合作催化），博通+1.71%，应用材料+2.21%，阿斯麦+2.15%，英特尔+1.84%。光通信板块暴涨：Coherent+13.44%，应用光电+9.2%，Credo+8.45%，Lumentum+6.22%，康宁+5.4%。<br>
      ④<b>存储分化资金获利了结</b>：与半导体整体走强形成对比，存储板块周五承压：美光-0.44%，西部数据-3.81%，闪迪-3.68%，希捷-4.71%，SK海力士-4.88%（韩股-10.37%后反弹）。市场担忧Q3存储涨价幅度收窄，消费端PC/手机需求恢复不及预期，前期涨太多资金集中出逃。<br>
      ⑤<b>SpaceX暴涨+15.83%</b>：两日累涨22.94%，首次大规模限售股解禁后没有引发抛售潮。马斯克称V3卫星能力将比V2高一个数量级，带宽是V2的100倍以上，今年收入将达200亿美元。SpaceX独家采用英伟达处理器的合作也推动英伟达股价走强。<br>
      ⑥<b>韩股反弹但SK海力士继续承压</b>：韩国KOSPI上周五暴跌4.6%触发第十次熔断后，周一亚太市场情绪有所修复，但SK海力士仍跌4.88%，三星电子微涨0.22%。韩国半导体特别法8月11日正式施行，总统挂帅支持产业生态。
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

# ========== 2. A股上周五复盘 ==========
ashare_html = '''
<div class="space-y-4">
<div class="grid md:grid-cols-4 gap-3">
  <div class="bg-gradient-to-br from-red-500/20 to-orange-500/10 border border-red-500/30 rounded-xl p-3 text-center">
    <div class="text-xs text-white/60 mb-1">上证指数</div>
    <div class="text-xl font-bold text-red-400">3900.35</div>
    <div class="text-xs text-red-400">+0.57%</div>
  </div>
  <div class="bg-gradient-to-br from-green-500/20 to-emerald-500/10 border border-green-500/30 rounded-xl p-3 text-center">
    <div class="text-xs text-white/60 mb-1">深证成指</div>
    <div class="text-xl font-bold text-green-400">14110.12</div>
    <div class="text-xs text-green-400">-0.24%</div>
  </div>
  <div class="bg-gradient-to-br from-green-500/20 to-emerald-500/10 border border-green-500/30 rounded-xl p-3 text-center">
    <div class="text-xs text-white/60 mb-1">创业板指</div>
    <div class="text-xl font-bold text-green-400">3515.56</div>
    <div class="text-xs text-green-400">-0.55%</div>
  </div>
  <div class="bg-gradient-to-br from-red-500/20 to-orange-500/10 border border-red-500/30 rounded-xl p-3 text-center">
    <div class="text-xs text-white/60 mb-1">科创50</div>
    <div class="text-xl font-bold text-red-400">1701.29</div>
    <div class="text-xs text-red-400">+0.45%</div>
  </div>
</div>

<div class="grid md:grid-cols-2 gap-4">
  <div class="bg-white/5 rounded-xl p-4">
    <h4 class="text-white font-semibold mb-3 flex items-center gap-2"><span>📉</span> 领跌板块</h4>
    <div class="space-y-1 text-xs">
      <div class="flex justify-between"><span class="text-white/70">保险/金融</span><span class="text-green-400">-2%~-3%</span></div>
      <div class="flex justify-between"><span class="text-white/70">消费白酒</span><span class="text-green-400">-1%~-2%</span></div>
      <div class="flex justify-between"><span class="text-white/70">地产链</span><span class="text-green-400">-1%~-2%</span></div>
      <div class="flex justify-between"><span class="text-white/70">银行</span><span class="text-green-400">-1%左右</span></div>
    </div>
  </div>
  <div class="bg-white/5 rounded-xl p-4">
    <h4 class="text-white font-semibold mb-3 flex items-center gap-2"><span>📈</span> 领涨板块</h4>
    <div class="space-y-1 text-xs">
      <div class="flex justify-between"><span class="text-white/70">PCB/铜箔</span><span class="text-red-400">涨停潮+3%~+5%</span></div>
      <div class="flex justify-between"><span class="text-white/70">半导体材料</span><span class="text-red-400">+2%~+4%</span></div>
      <div class="flex justify-between"><span class="text-white/70">算力/光模块</span><span class="text-red-400">+1%~+3%</span></div>
      <div class="flex justify-between"><span class="text-white/70">贵金属</span><span class="text-red-400">+2%~+3%</span></div>
    </div>
  </div>
</div>

<div class="bg-white/5 rounded-xl p-4">
  <h4 class="text-white font-semibold mb-3 flex items-center gap-2"><span>📋</span> 上周五核心盘面回顾</h4>
  <div class="text-xs text-white/70 space-y-2 leading-relaxed">
    <p>① <b class="text-yellow-400">指数分化明显</b>：上证指数+0.57%收3900点，金融股护盘；深成指-0.24%、创业板-0.55%小幅调整；科创50+0.45%领涨。全市场成交约2.5万亿，量能维持高位。</p>
    <p>② <b class="text-yellow-400">PCB铜箔涨停潮</b>：高盛上调AI服务器PCB市场空间38%至2028年840亿美元，叠加刚果金禁运铜钴精矿LME铜创年内新高，PCB板块26股涨停，铜冠铜箔+16.98%领涨。</p>
    <p>③ <b class="text-yellow-400">科技板块探底回升</b>：半导体材料、算力硬件相对强势，雅克科技+2.6%HBM前驱体获资金认可；存储板块分化，铜箔强于存储芯片。</p>
    <p>④ <b class="text-yellow-400">金融消费走弱</b>：银行、保险、白酒、地产链调整，市场风格偏向成长，避险资金流向贵金属（黄金白银大涨）。</p>
    <p>⑤ <b class="text-yellow-400">龙虎榜</b>：机构合计净买入12.42亿（30净买/26净卖）；铜冠铜箔机构净卖2.47亿占比2.8%（属正常调仓范围）。</p>
  </div>
</div>

<div class="bg-gradient-to-br from-blue-500/10 to-cyan-500/10 border border-blue-500/30 rounded-xl p-4">
  <h4 class="text-blue-300 font-semibold mb-3 flex items-center gap-2"><span>🔭</span> 今日（周一）展望</h4>
  <div class="text-xs text-white/70 space-y-2 leading-relaxed">
    <p>① <b class="text-yellow-400">高开确定</b>：非农爆冷+美联储加息预期骤降+美股创历史新高，三重利好之下周一A股高开几无悬念。关注高开幅度和量能配合。</p>
    <p>② <b class="text-yellow-400">主线方向</b>：光通信/算力（海外光模块暴涨催化）、半导体设备材料（国产替代+大基金三期预期）、人形机器人（宇树科技申购）、贵金属（降息预期+美元走弱）。</p>
    <p>③ <b class="text-yellow-400">注意分化</b>：美股存储板块周五已出现获利了结迹象，A股存储/铜箔板块前期涨幅大，周一可能高开低走分化，不追高。</p>
    <p>④ <b class="text-yellow-400">催化剂日历</b>：8月10日宇树科技申购、长鑫科技纳入MSCI生效；8月11日韩国半导体特别法施行；本周关注国内7月金融数据、CPI数据。</p>
  </div>
</div>
</div>'''
gen.add_section("A股上周五复盘与今日展望", ashare_html, "📊")

# ========== 3. 核心题材与今日催化 ==========
catalyst_html = '''
<div class="space-y-4">
  <!-- 催化1：非农爆冷+流动性宽松 -->
  <div class="bg-gradient-to-br from-yellow-500/10 to-orange-500/10 border border-yellow-500/30 rounded-xl p-4">
    <div class="flex items-center justify-between mb-3">
      <h4 class="text-yellow-300 font-semibold flex items-center gap-2"><span>⭐</span> S级催化：非农爆冷改写全球流动性叙事</h4>
      <span class="text-xs bg-yellow-500/30 text-yellow-200 px-2 py-0.5 rounded">S级·宏观</span>
    </div>
    <div class="text-xs text-white/70 space-y-2 leading-relaxed">
      <p><b class="text-yellow-400">事件：</b>美国7月非农就业-2.3万（预期+8万），5-6月合计下修10.3万，9月加息概率从54%骤降至40%。美元跳水、黄金暴涨、美债收益率下行。</p>
      <p><b class="text-yellow-400">影响路径：</b></p>
      <p>① <b>全球流动性宽松预期升温</b> → 美元走弱 → 人民币升值 → 北向资金回流 → A股估值修复</p>
      <p>② <b>加息预期降温</b> → 科技成长股估值压制缓解 → AI算力/半导体/创新药受益</p>
      <p>③ <b>实际利率下行</b> → 黄金/白银/大宗商品上涨 → 贵金属板块/资源股受益</p>
      <p><b class="text-yellow-400">关联标的：</b>贵金属（山东黄金、赤峰黄金）、科技成长（AI算力、半导体）、北向重仓股</p>
    </div>
  </div>

  <!-- 催化2：央行下半年宽松 -->
  <div class="bg-gradient-to-br from-blue-500/10 to-indigo-500/10 border border-blue-500/30 rounded-xl p-4">
    <div class="flex items-center justify-between mb-3">
      <h4 class="text-blue-300 font-semibold flex items-center gap-2"><span>💰</span> A级催化：央行下半年工作会议定调持续宽松</h4>
      <span class="text-xs bg-blue-500/30 text-blue-200 px-2 py-0.5 rounded">A级·政策</span>
    </div>
    <div class="text-xs text-white/70 space-y-2 leading-relaxed">
      <p><b class="text-yellow-400">核心信号：</b>央行2026年下半年工作会议明确"维持适度宽松货币政策，若经济需要随时出台增量流动性工具"，定向加大科技创新、高端制造业专项再贷款。7月CPI同比+0.5%温和，无通胀约束。</p>
      <p><b class="text-yellow-400">市场意义：</b>直接打消资金收紧顾虑，流动性友好环境延续至下半年。科技研发、高端硬件赛道持续获得低成本产业资金支持。</p>
      <p><b class="text-yellow-400">证监会10项合作新政：</b>内地与香港资本市场10项合作举措，拓宽港股通、ETF互联互通，利好港股科技、AH溢价标的。</p>
    </div>
  </div>

  <!-- 催化3：创业板算力ETF -->
  <div class="bg-gradient-to-br from-purple-500/10 to-pink-500/10 border border-purple-500/30 rounded-xl p-4">
    <div class="flex items-center justify-between mb-3">
      <h4 class="text-purple-300 font-semibold flex items-center gap-2"><span>📊</span> A级催化：10家基金公司集中上报创业板算力ETF</h4>
      <span class="text-xs bg-purple-500/30 text-purple-200 px-2 py-0.5 rounded">A级·增量资金</span>
    </div>
    <div class="text-xs text-white/70 space-y-2 leading-relaxed">
      <p><b class="text-yellow-400">事件：</b>易方达、华夏、南方、广发、富国、国泰、嘉实、天弘、鹏华、大成共10家基金公司上报创业板算力基础设施指数ETF，选取算力基础设施领域50只创业板龙头（景嘉微、中际旭创、天孚通信等）。</p>
      <p><b class="text-yellow-400">意义：</b>继科创芯片、半导体设备之后，算力赛道再迎ETF增量资金。10家头部基金同时上报，预计募集规模可观，将为算力赛道带来持续被动配置需求。</p>
      <p><b class="text-yellow-400">关联标的：</b>算力硬件（景嘉微、中际旭创、天孚通信、工业富联）、PCB铜箔（沪电股份、胜宏科技、铜冠铜箔）</p>
    </div>
  </div>

  <!-- 催化4：宇树科技IPO -->
  <div class="bg-gradient-to-br from-green-500/10 to-emerald-500/10 border border-green-500/30 rounded-xl p-4">
    <div class="flex items-center justify-between mb-3">
      <h4 class="text-green-300 font-semibold flex items-center gap-2"><span>🤖</span> A级催化：宇树科技今日申购·人形机器人第一股</h4>
      <span class="text-xs bg-green-500/30 text-green-200 px-2 py-0.5 rounded">A级·IPO</span>
    </div>
    <div class="text-xs text-white/70 space-y-2 leading-relaxed">
      <p><b class="text-yellow-400">发行信息：</b>发行价150.80元/股，发行后市值约610亿元，募资60.99亿元，市盈率219倍（行业平均38.56倍）。申购代码787836，中一签需缴款7.54万元。</p>
      <p><b class="text-yellow-400">公司亮点：</b>A股首家人形机器人整机上市企业，2025年人形机器人出货量超5500台全球第一，海外收入占比约50%。从获受理到过会仅4个月，创科创板最快审核纪录。</p>
      <p><b class="text-yellow-400">产业链影响：</b>人形机器人赛道估值标杆确立，上游核心零部件（减速器、伺服电机、控制器、传感器）将受益于情绪催化。智元机器人已启动港股上市，具身智能赛道进入IPO密集期。</p>
      <p><b class="text-yellow-400">关联标的：</b>绿的谐波、双环传动、拓普集团、三花智控、鸣志电器、奥比中光</p>
    </div>
  </div>

  <!-- 催化5：光通信暴涨 -->
  <div class="bg-gradient-to-br from-cyan-500/10 to-blue-500/10 border border-cyan-500/30 rounded-xl p-4">
    <div class="flex items-center justify-between mb-3">
      <h4 class="text-cyan-300 font-semibold flex items-center gap-2"><span>🌐</span> A级催化：美股光通信暴涨·Coherent+13%·订单逻辑持续验证</h4>
      <span class="text-xs bg-cyan-500/30 text-cyan-200 px-2 py-0.5 rounded">A级·海外映射</span>
    </div>
    <div class="text-xs text-white/70 space-y-2 leading-relaxed">
      <p><b class="text-yellow-400">行情：</b>周五美股光通信板块集体大涨，Coherent+13.44%、应用光电+9.2%、Credo+8.45%、Lumentum+6.22%、康宁+5.4%。</p>
      <p><b class="text-yellow-400">驱动逻辑：</b>AI算力资本开支持续超预期，英伟达Rubin平台需求强劲，光模块订单饱满。摩根大通将2026年TMT债券发行预测上调至5400亿美元，侧面验证AI基建投资热度。</p>
      <p><b class="text-yellow-400">风险提示：</b>外媒持续传闻美方可能收紧高速光模块出口管制，光通信板块存在情绪分歧，周一容易分化。</p>
      <p><b class="text-yellow-400">关联标的：</b>中际旭创（摩根大通H股增持至15.02%）、新易盛、天孚通信、光迅科技、华工科技</p>
    </div>
  </div>

  <!-- 催化6：长鑫纳入MSCI -->
  <div class="bg-gradient-to-br from-red-500/10 to-orange-500/10 border border-red-500/30 rounded-xl p-4">
    <div class="flex items-center justify-between mb-3">
      <h4 class="text-red-300 font-semibold flex items-center gap-2"><span>💾</span> B级催化：长鑫科技今日纳入MSCI·瑞银给出70元目标价</h4>
      <span class="text-xs bg-red-500/30 text-red-200 px-2 py-0.5 rounded">B级·资金面</span>
    </div>
    <div class="text-xs text-white/70 space-y-2 leading-relaxed">
      <p><b class="text-yellow-400">MSCI纳入：</b>长鑫科技（688098）8月10日正式纳入MSCI全球标准指数，将带来被动增量资金。周五收盘价52.48元，市值约3.28万亿。</p>
      <p><b class="text-yellow-400">瑞银研报：</b>首次覆盖长鑫科技，给予70元目标价（约33%上行空间），预计2026-2028年净利润1397亿/3328亿/4282亿元，复合增速约75%。</p>
      <p><b class="text-yellow-400">影响：</b>作为国产存储龙头，长鑫纳入MSCI+机构持续看好，有助于提升存储板块整体估值中枢，利好上游材料设备国产替代。</p>
      <p><b class="text-yellow-400">关联标的：</b>雅克科技（HBM前驱体）、华海诚科（封装材料）、拓荆科技（薄膜沉积）、北方华创（设备）</p>
    </div>
  </div>
</div>'''
gen.add_section("核心题材与今日催化", catalyst_html, "🔥")

# ========== 4. 持仓诊断 ==========
portfolio_html = '''
<div class="space-y-4">
  <!-- 铜冠铜箔 -->
  <div class="bg-gradient-to-br from-green-500/20 to-emerald-500/10 border border-green-500/40 rounded-xl p-4">
    <div class="flex items-center justify-between mb-3">
      <div class="flex items-center gap-2">
        <span class="bg-green-500 text-white text-xs px-2 py-0.5 rounded-full font-bold">持仓</span>
        <span class="text-white font-bold text-lg">铜冠铜箔 (301217)</span>
      </div>
      <div class="text-right">
        <div class="text-xl font-bold text-red-400">115.81元</div>
        <div class="text-xs text-red-400">8月7日 +16.98% · PCB铜箔涨停潮·三重催化</div>
      </div>
    </div>
    <div class="grid md:grid-cols-3 gap-3 text-xs">
      <div class="bg-white/5 rounded-lg p-3">
        <div class="text-white/60 mb-1">最新评级</div>
        <div class="text-green-400 font-semibold">🟢 浮盈+32.9%·强势但需减仓</div>
      </div>
      <div class="bg-white/5 rounded-lg p-3">
        <div class="text-white/60 mb-1">关键价位</div>
        <div class="text-white font-semibold">压力120元 / 支撑100元</div>
      </div>
      <div class="bg-white/5 rounded-lg p-3">
        <div class="text-white/60 mb-1">操作建议</div>
        <div class="text-white font-semibold">高开冲120减至1/3底仓</div>
      </div>
    </div>
    <div class="mt-3 text-xs text-white/70 leading-relaxed">
      <p><b class="text-yellow-400">📊 盘面解读</b>：铜冠铜箔周五+16.98%收115.81元，成交额88.37亿换手率9.57%，放量大涨。三重催化共振：①高盛上调AI服务器PCB市场空间38%；②刚果金禁运铜钴精矿LME铜创年内新高；③马斯克定调存储是AI唯一瓶颈。PCB板块26股涨停。龙虎榜机构净卖2.8%<5%属正常调仓。</p>
      <p class="mt-2"><b class="text-yellow-400">🎯 今日策略</b>：周一外围利好+板块情绪高涨，大概率高开。但周五已大涨17%，短期获利盘丰厚，美股存储板块周五已出现获利了结迹象（美光-0.44%、西部数据-3.81%）。</p>
      <p class="mt-2"><b class="text-yellow-400">⚡ 操作方案</b>：<br>
      ① 高开冲120元附近坚决减仓至1/3底仓（约2万股），锁定30%+利润；<br>
      ② 若强势涨停或突破120元，可留1/2仓位博弈新高，但必须设止盈线110元；<br>
      ③ 回踩100-105元区间可接回机动仓做T；<br>
      ④ 跌破100元止盈至底仓，跌破90元全部清仓。</p>
    </div>
  </div>

  <!-- 雅克科技 -->
  <div class="bg-gradient-to-br from-green-500/20 to-emerald-500/10 border border-green-500/40 rounded-xl p-4">
    <div class="flex items-center justify-between mb-3">
      <div class="flex items-center gap-2">
        <span class="bg-green-500 text-white text-xs px-2 py-0.5 rounded-full font-bold">持仓</span>
        <span class="text-white font-bold text-lg">雅克科技 (002409)</span>
      </div>
      <div class="text-right">
        <div class="text-xl font-bold text-red-400">148.78元</div>
        <div class="text-xs text-red-400">8月7日 +2.60% · HBM前驱体龙头·机构抄底</div>
      </div>
    </div>
    <div class="grid md:grid-cols-3 gap-3 text-xs">
      <div class="bg-white/5 rounded-lg p-3">
        <div class="text-white/60 mb-1">最新评级</div>
        <div class="text-green-400 font-semibold">🟢 浮盈+36.7%·底仓持有</div>
      </div>
      <div class="bg-white/5 rounded-lg p-3">
        <div class="text-white/60 mb-1">关键价位</div>
        <div class="text-white font-semibold">压力155-160 / 支撑140</div>
      </div>
      <div class="bg-white/5 rounded-lg p-3">
        <div class="text-white/60 mb-1">操作建议</div>
        <div class="text-white font-semibold">150-155减仓1/3锁利</div>
      </div>
    </div>
    <div class="mt-3 text-xs text-white/70 leading-relaxed">
      <p><b class="text-yellow-400">📊 盘面解读</b>：雅克科技周五+2.60%收148.78元，成交额46.77亿换手率9.93%。HBM前驱体龙头地位稳固，马斯克定调存储供需剪刀差（供给20% vs 需求200%）利好长期逻辑。机构跌停板抄底后持续加仓，近5日累计净流入超7亿元。</p>
      <p class="mt-2"><b class="text-yellow-400">🎯 催化验证</b>：长鑫科技纳入MSCI（今日生效）+瑞银给长鑫70元目标价，国产存储产业链情绪有望持续修复，雅克科技作为上游材料龙头直接受益。韩国半导体特别法8月11日施行也利好全球存储产业链情绪。</p>
      <p class="mt-2"><b class="text-yellow-400">⚡ 操作方案</b>：<br>
      ① 150-155元区间减仓1/3锁定利润（底仓保留2/3）；<br>
      ② 若突破160元可留半仓博弈新高，155元为止盈线；<br>
      ③ 跌破142元止盈至底仓，跌破130元全部清仓；<br>
      ④ HBM长期逻辑不变，但短期存储板块情绪波动大，仓位管理优先。</p>
    </div>
  </div>

  <!-- 英维克 -->
  <div class="bg-gradient-to-br from-yellow-500/20 to-orange-500/10 border border-yellow-500/40 rounded-xl p-4">
    <div class="flex items-center justify-between mb-3">
      <div class="flex items-center gap-2">
        <span class="bg-yellow-500 text-white text-xs px-2 py-0.5 rounded-full font-bold">持仓</span>
        <span class="text-white font-bold text-lg">英维克 (002837)</span>
      </div>
      <div class="text-right">
        <div class="text-xl font-bold text-red-400">55.90元</div>
        <div class="text-xs text-red-400">8月7日 +5.61% · 超跌反弹·液冷跟随</div>
      </div>
    </div>
    <div class="grid md:grid-cols-3 gap-3 text-xs">
      <div class="bg-white/5 rounded-lg p-3">
        <div class="text-white/60 mb-1">最新评级</div>
        <div class="text-yellow-400 font-semibold">🟡 深度破止损-46.4%·反弹减仓</div>
      </div>
      <div class="bg-white/5 rounded-lg p-3">
        <div class="text-white/60 mb-1">关键价位</div>
        <div class="text-white font-semibold">压力60-65元 / 支撑52元</div>
      </div>
      <div class="bg-white/5 rounded-lg p-3">
        <div class="text-white/60 mb-1">操作建议</div>
        <div class="text-white font-semibold">60-65元减仓≥1/2</div>
      </div>
    </div>
    <div class="mt-3 text-xs text-white/70 leading-relaxed">
      <p><b class="text-yellow-400">📊 盘面解读</b>：英维克周五+5.61%收55.90元，成交额28.97亿换手率4.66%。液冷板块跟随科技修复但弱于PCB/铜箔。从高点回撤67.3%，深度破止损-46.4%。</p>
      <p class="mt-2"><b class="text-yellow-400">🎯 核心矛盾</b>：液冷板块前期跌幅过大，超跌后有反弹需求。英伟达30亿美元入股电力商Lancium锁定数据中心电力资源，长期利好液冷散热需求，但短期资金更偏好PCB、光通信等方向。</p>
      <p class="mt-2"><b class="text-yellow-400">⚡ 操作方案</b>：<br>
      ① 反弹至60-65元区间坚决减仓≥1/2，降低持仓风险；<br>
      ② 若强势突破65元，可少量留仓博弈70元，但58元为止盈线；<br>
      ③ 二次跌破52元无条件清仓，纪律第一；<br>
      ④ 严禁补仓抄底，下降趋势中任何反弹都是减仓机会。</p>
    </div>
  </div>

  <!-- *ST建艺 -->
  <div class="bg-gradient-to-br from-gray-500/20 to-slate-500/10 border border-gray-500/40 rounded-xl p-4">
    <div class="flex items-center justify-between mb-3">
      <div class="flex items-center gap-2">
        <span class="bg-gray-500 text-white text-xs px-2 py-0.5 rounded-full font-bold">持仓</span>
        <span class="text-white font-bold text-lg">*ST建艺 (002789)</span>
      </div>
      <div class="text-right">
        <div class="text-xl font-bold text-green-400">9.83元</div>
        <div class="text-xs text-green-400">8月7日 -5.30% · 退市风险·地量</div>
      </div>
    </div>
    <div class="bg-red-500/10 border border-red-500/30 rounded-lg p-3 mb-3">
      <p class="text-red-300 text-xs font-semibold">⚠️ 最高优先级：立即清仓止损，退市风险敞口必须关闭</p>
    </div>
    <div class="text-xs text-white/70 leading-relaxed">
      <p><b class="text-yellow-400">📰 最新动态</b>：*ST建艺周五-5.30%收9.83元，成交地量4280万。公司推进重组已提交摘帽申请但退市风险未解除。浮亏约-26.9%。</p>
      <p class="mt-2"><b class="text-yellow-400">⚡ 操作策略</b>：退市风险股，任何价格立即清仓。退市风险+债务问题未消除，不要抱有任何幻想。ST股的基本面不会因为股价反弹而改善，早一天减仓少一分风险。</p>
    </div>
  </div>

  <!-- 组合总览 -->
  <div class="bg-white/5 rounded-xl p-4">
    <h4 class="text-white font-semibold mb-3 flex items-center gap-2"><span>📋</span> 组合总览与今日策略</h4>
    <div class="text-xs text-white/70 space-y-2 leading-relaxed">
      <p><b class="text-yellow-400">上周五表现</b>：持仓全线反弹，铜冠铜箔+16.98%领涨（涨停潮核心标的），英维克+5.61%超跌反弹，雅克科技+2.60%稳健上涨，*ST建艺-5.30%弱势。组合整体跑赢大盘。</p>
      <p><b class="text-yellow-400">今日策略（8月10日周一）：</b><br>
      ① 外围利好（非农爆冷+美股创新高）+国内宽松，周一高开概率大，但注意美股存储分化+光模块出口管制传闻，<b>不追高、高开减仓</b>；<br>
      ② <b>铜冠铜箔</b>：高开冲120元减至1/3底仓锁定利润，回踩100-105元接回；<br>
      ③ <b>雅克科技</b>：150-155元减仓1/3锁利，长鑫纳入MSCI催化但存储板块情绪波动大；<br>
      ④ <b>英维克</b>：60-65元坚决减仓≥1/2，跌破52元清仓；<br>
      ⑤ <b>*ST建艺</b>：立即清仓（最高优先级）；<br>
      ⑥ 整体仓位5-6成，聚焦光通信/半导体材料主线，铜箔/存储冲高减仓。</p>
    </div>
  </div>
</div>'''
gen.add_section("持仓诊断与操作建议", portfolio_html, "💼")

# ========== 5. 空方视角 ==========
bear_html = '''
<div class="space-y-4">
  <div class="bg-red-500/10 border border-red-500/30 rounded-xl p-4">
    <h4 class="text-red-300 font-semibold mb-3 flex items-center gap-2"><span>🐻</span> 空方观点：非农"造假"嫌疑+存储见顶+AI泡沫三重风险</h4>
    <div class="text-xs text-white/70 space-y-3 leading-relaxed">
      <div class="bg-white/5 rounded-lg p-3">
        <p class="text-red-300 font-semibold mb-1">风险1：非农数据"人为制造"，降息预期可能是陷阱</p>
        <p>7月非农-2.3万+5-6月下修10.3万，数据"过于完美"地支撑了降息叙事。市场质疑数据真实性——为中期选举人为压低就业数据以推动降息。
        如果后续数据修正或通胀反弹，美联储可能重新转向鹰派，当前市场定价的宽松预期可能过于超前。</p>
      </div>
      <div class="bg-white/5 rounded-lg p-3">
        <p class="text-red-300 font-semibold mb-1">风险2：存储涨价周期见顶，资金正在获利了结</p>
        <p>美股存储板块周五集体下跌（西部数据-3.81%、闪迪-3.68%、希捷-4.71%、美光-0.44%），在半导体整体+2.56%的环境下逆势走弱。
        闪迪Q3指引刚到预期下限就暴跌，说明市场对存储涨价周期的持续性产生了怀疑。
        英伟达降配HBM（Rubin Ultra从12Hi降为8Hi）也是需求疲软的信号。</p>
      </div>
      <div class="bg-white/5 rounded-lg p-3">
        <p class="text-red-300 font-semibold mb-1">风险3：光模块出口管制传闻持续发酵</p>
        <p>外媒持续传闻美方可能收紧高速光模块出口管制，如果落地将对国内光模块企业造成重大冲击。
        虽然目前尚未有官方消息，但在中美博弈背景下，任何技术领域都可能成为新的制裁目标。
        光通信板块周五海外大涨，但国内周一可能因为管制传闻而分化。</p>
      </div>
      <div class="bg-white/5 rounded-lg p-3">
        <p class="text-red-300 font-semibold mb-1">风险4：宇树科技IPO抽血效应</p>
        <p>人形机器人第一股610亿市值募资61亿，加上长鑫科技3.28万亿巨无霸持续吸金，
        科技板块增量资金可能被IPO分流。7月以来硬科技IPO密集（长鑫、宇树、燧原排队），
        存量博弈下，新股抽血可能导致老股估值承压。</p>
      </div>
      <div class="bg-white/5 rounded-lg p-3">
        <p class="text-red-300 font-semibold mb-1">风险5：AI资本开支泡沫隐忧</p>
        <p>全球机构已经在警示AI资本开支泡沫风险，如果后续AI需求不及预期，大规模资本投入会快速收缩。
        英伟达+11.56%（周涨幅）但主要靠SpaceX合作消息驱动，而非基本面超预期。
        当市场开始从"订单驱动"转向"业绩验证"，估值偏高的科技股可能面临调整。</p>
      </div>
    </div>
  </div>

  <div class="bg-green-500/10 border border-green-500/30 rounded-xl p-4">
    <h4 class="text-green-300 font-semibold mb-3 flex items-center gap-2"><span>🐂</span> 多方反驳：流动性宽松+产业趋势不可逆转</h4>
    <div class="text-xs text-white/70 space-y-2 leading-relaxed">
      <p>① <b>全球流动性拐点确认</b>：非农数据不管真假，趋势是明确的——就业市场在走弱，美联储加息周期接近尾声。
      流动性宽松是支撑风险资产估值的最大利好，外资回流A股的大趋势已经形成。</p>
      <p>② <b>存储供需缺口仍在扩大</b>：三大原厂2027年DRAM和HBM产能已全部售罄，
      长鑫科技IPO募资扩产、SK海力士384亿美元新建晶圆厂，都说明产业端对未来需求有信心。
      短期股价调整是获利了结，不是基本面反转。</p>
      <p>③ <b>国产替代加速是长期逻辑</b>：美国出口管制越严，国产替代的紧迫性越强。
      从半导体设备到材料到芯片，国产替代空间巨大，雅克科技、华海诚科、北方华创等长期受益。</p>
      <p>④ <b>国内政策持续加码</b>：央行定调宽松+证监会10项合作新政+深圳半导体专项资金+韩国半导体特别法，
      全球范围内半导体都是战略重点，政策面持续友好。</p>
      <p>⑤ <b>A股已提前调整</b>：A股科技板块从7月高点已调整20-30%，估值回落至合理区间。
      相比美股半导体从高点跌20%进入技术性熊市，A股半导体的国产替代逻辑反而在强化。</p>
    </div>
  </div>

  <div class="bg-yellow-500/10 border border-yellow-500/30 rounded-xl p-4">
    <h4 class="text-yellow-300 font-semibold mb-2 flex items-center gap-2"><span>⚖️</span> 综合判断</h4>
    <p class="text-xs text-white/70 leading-relaxed">
      短期（1-2周）：非农爆冷+国内宽松双催化，科技板块情绪修复，反弹有望延续。
      但存储板块获利了结压力大，光模块有出口管制传闻，板块内部分化加剧。
      操作上逢高减仓机动仓，保留底仓，不追高、不加仓。<br>
      中期（1-3个月）：全球流动性宽松+国产替代+AI需求三逻辑不变，
      调整到位后优质标的将迎来布局机会。关注中报业绩验证和9月美联储议息会议。<br>
      <b class="text-yellow-400">核心结论：流动性拐点是最大利好，科技成长中期看好，
      但短期涨幅过大的品种有回调风险，仓位管理和波段操作比持有不动更重要。</b>
    </p>
  </div>
</div>'''
gen.add_section("空方视角与多空博弈", bear_html, "⚖️")

# ========== 6. 预判验证 ==========
prediction_html = '''
<div class="space-y-4">
  <div class="bg-white/5 rounded-xl p-4">
    <h4 class="text-white font-semibold mb-3 flex items-center gap-2"><span>🔮</span> 预判记录（T+N验证）</h4>
    <div class="space-y-3 text-xs">
      <div class="bg-green-500/10 border border-green-500/30 rounded-lg p-3">
        <div class="flex justify-between mb-2">
          <span class="text-green-300 font-semibold">预判#20260807-01：非农后科技股延续反弹</span>
          <span class="text-xs bg-green-500/30 text-green-200 px-2 py-0.5 rounded">验证中·T+1</span>
        </div>
        <p class="text-white/70">预判内容：非农数据公布后，若不及预期则加息概率下降、科技股延续反弹，光通信/半导体设备领涨。</p>
        <p class="text-white/50 mt-1">当前进度：非农-2.3万大爆冷，美股周五纳指+1.3%、费半+2.56%、光通信暴涨。初步验证正确，今日A股表现待验证。</p>
      </div>
      <div class="bg-yellow-500/10 border border-yellow-500/30 rounded-lg p-3">
        <div class="flex justify-between mb-2">
          <span class="text-yellow-300 font-semibold">预判#20260803-01：雅克科技跌停后3日内反弹</span>
          <span class="text-xs bg-yellow-500/30 text-yellow-200 px-2 py-0.5 rounded">验证中·T+5</span>
        </div>
        <p class="text-white/70">预判内容：雅克科技跌停板机构抄底近5亿，预计3个交易日内出现5-10%反弹。</p>
        <p class="text-white/50 mt-1">当前进度：从8月4日跌停价127元反弹至148.78元（+17%），远超预期，验证正确。但中间波动较大，不是直线反弹。</p>
      </div>
      <div class="bg-green-500/10 border border-green-500/30 rounded-lg p-3">
        <div class="flex justify-between mb-2">
          <span class="text-green-300 font-semibold">预判#20260730-02：存储板块调整期2-3周</span>
          <span class="text-xs bg-green-500/30 text-green-200 px-2 py-0.5 rounded">部分验证</span>
        </div>
        <p class="text-white/70">预判内容：7月30日科技股大跌后，存储板块进入2-3周调整期，调整幅度约15-25%。</p>
        <p class="text-white/50 mt-1">当前进度：第8个交易日，板块从高点回调约20-25%，幅度符合预期。
        但上周五铜冠铜箔+17%强力反弹，PCB铜箔方向率先走出调整。存储芯片方向仍在底部震荡。</p>
      </div>
      <div class="bg-green-500/10 border border-green-500/30 rounded-lg p-3">
        <div class="flex justify-between mb-2">
          <span class="text-green-300 font-semibold">预判#20260720-01：科技板块大跌后B浪反弹</span>
          <span class="text-xs bg-green-500/30 text-green-200 px-2 py-0.5 rounded">已验证·正确</span>
        </div>
        <p class="text-white/70">预判内容：7月20日科技板块大跌后，将出现B浪反弹，反弹幅度约10-15%，持续1-2周，然后进入C浪调整。</p>
        <p class="text-white/50 mt-1">实际走势：雅克科技从120反弹至150+（+25%），英维克从46反弹至60+（+30%），
        反弹幅度和持续时间均超预期。当前处于C浪调整后的第二波反弹。</p>
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
        <div class="text-lg font-bold text-blue-400">4</div>
        <div class="text-white/60">待验证</div>
      </div>
    </div>
  </div>
</div>'''
gen.add_section("预判验证闭环", prediction_html, "🔮")

# ========== 7. 教训库 ==========
lesson_html = '''
<div class="space-y-3">
  <div class="bg-red-500/10 border border-red-500/30 rounded-lg p-3">
    <p class="text-red-300 font-semibold mb-1">教训#1：非农前降低仓位是铁律</p>
    <p class="text-white/60 text-xs">
      每月第一个周五的美国非农数据，是全球市场的最大变量之一。
      数据超预期或不及预期，都可能引发市场剧烈波动。
      <b>正确做法</b>：非农日前一天降低高Beta仓位，
      保留现金等待数据落地后再决定方向。不要带着重仓赌数据方向。
      本次非农前如果减了仓，周五的大涨就能从容加仓。
    </p>
  </div>

  <div class="bg-orange-500/10 border border-orange-500/30 rounded-lg p-3">
    <p class="text-orange-300 font-semibold mb-1">教训#2：外围暴涨≠A股跟涨，看板块分化</p>
    <p class="text-white/60 text-xs">
      费半+2.56%但存储股跌，光通信涨。同样是半导体，
      不同子板块走势完全相反。A股开盘经常是"先全涨、再分化"，
      如果开盘追高了错误的方向，当天就会被套。
      <b>正确做法</b>：先看海外哪个细分方向最强，
      再找A股对应的标的。不要看到半导体涨就随便买，要精准到子赛道。
    </p>
  </div>

  <div class="bg-yellow-500/10 border border-yellow-500/30 rounded-lg p-3">
    <p class="text-yellow-300 font-semibold mb-1">教训#3：大涨次日是减仓机会，不是加仓时机</p>
    <p class="text-white/60 text-xs">
      铜冠铜箔周五+17%，周一大概率高开，但这是减仓机会不是加仓时机。
      历史经验表明，单日大涨15%+的股票，次日继续大涨的概率不到30%，
      高开低走的概率超过50%。
      <b>正确做法</b>：大涨次日高开减仓，回踩再接回。
      不要因为"情绪高涨"就追高，情绪来的快去的也快。
    </p>
  </div>

  <div class="bg-green-500/10 border border-green-500/30 rounded-lg p-3">
    <p class="text-green-300 font-semibold mb-1">教训#4：机构抄底≠马上V型反转</p>
    <p class="text-white/60 text-xs">
      雅克科技跌停机构抄底近5亿，确实是中长期看好的信号，
      但股价不会因为机构买了就马上V型反转。从127到148.78用了5个交易日，
      中间有反复震荡。机构建仓是一个过程，可能继续砸盘吸筹，也可能横盘很久。
      <b>正确做法</b>：机构抄底作为中长期看好的佐证，
      但短期操作还是要看技术面和情绪面。分批建仓、控制仓位、设置止损。
    </p>
  </div>

  <div class="bg-purple-500/10 border border-purple-500/30 rounded-lg p-3">
    <p class="text-purple-300 font-semibold mb-1">教训#5：ST股任何反弹都是减仓机会</p>
    <p class="text-white/60 text-xs">
      *ST建艺每次反弹都给了减仓机会，但每次都有人心存幻想不卖，
      结果越套越深，从13元套到9.83元，浮亏从-15%扩大到-27%。
      退市风险股的基本面不会因为股价反弹而改善。
      <b>正确做法</b>：ST股的任何反弹都是减仓机会，
      不要抱有"摘帽""重组"的幻想。早一天减仓，少一分风险。
      现在9.83元再不卖，可能跌到5元甚至退市。
    </p>
  </div>

  <div class="bg-blue-500/10 border border-blue-500/30 rounded-lg p-3">
    <p class="text-blue-300 font-semibold mb-1">教训#6：光模块出口管制是长期悬顶之剑</p>
    <p class="text-white/60 text-xs">
      外媒持续传闻美方可能收紧高速光模块出口管制，
      虽然一直没有落地，但每次传闻都会引发板块波动。
      在中美博弈背景下，任何高科技领域都可能成为制裁目标。
      <b>正确做法</b>：光模块仓位不宜过重，留有余地。
      关注国产替代方向（如光芯片、设备），这些方向受制裁影响较小。
    </p>
  </div>
</div>'''
gen.add_section("教训库引用", lesson_html, "📚")

# ========== 生成+发布 ==========
output_path = os.path.join(WORK_DIR, 'docs/daily/20260810_每日新闻洞察.html')
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
