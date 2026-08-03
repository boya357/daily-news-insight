#!/usr/bin/env python3
"""2026年8月3日 每日新闻洞察生成 - 周一·央行定调适度宽松增量政策·美日联手干预日元·7月收官冲高回落8月开门·持仓分化明显"""
import sys, os, shutil, json
WORK_DIR = '/app/data/所有对话/主对话'
sys.path.insert(0, os.path.join(WORK_DIR, 'v3'))
from generators.daily_pro import DailyReportProGenerator

gen = DailyReportProGenerator(
    date_str='2026年8月3日', weekday='星期一',
    subtitle='2026年8月3日 周一 · 央行定调适度宽松+增量政策·美日联手干预日元近30年首次·亚马逊暴涨15%验证AI云需求·7月收官冲高回落8月开门怎么看',
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
    {"name":"道琼斯","change":"+0.53%","up":True},
    {"name":"标普500","change":"+0.70%","up":True},
    {"name":"纳斯达克","change":"+1.00%","up":True},
    {"name":"费城半导体","change":"+0.07%","up":True},
    {"name":"韩国KOSPI","change":"+18% (7/30)","up":True},
    {"name":"恒生指数","change":"+0.10%","up":True},
])
global_list1 = render_list([
    {"name":"WTI原油","change":"+3.84%/$86.80","up":True},
    {"name":"布伦特原油","change":"+3.86%/$90.23","up":True},
    {"name":"COMEX黄金","change":"-1.49%/$4098.60","up":False},
    {"name":"COMEX白银","change":"-2.10%/$57.77","up":False},
])
global_list2 = render_list([
    {"name":"亚马逊","change":"+15.32%","up":True},
    {"name":"谷歌","change":"+6.73%","up":True},
    {"name":"苹果","change":"-7.35%","up":False},
    {"name":"美光科技","change":"-5.90%","up":False},
])
global_list3 = render_list([
    {"name":"英伟达","change":"+2.93%","up":True},
    {"name":"微软","change":"+3.02%","up":True},
    {"name":"Meta","change":"+3.28%","up":True},
    {"name":"AMD","change":"-1.13%","up":False},
    {"name":"博通","change":"+0.37%","up":True},
    {"name":"台积电ADR","change":"-4.50%","up":False},
])
global_html = '''
<div class="grid md:grid-cols-3 gap-4">
  <div class="md:col-span-2">
    <div class="text-white font-semibold mb-3 flex items-center gap-2"><span>🌍</span><span>隔夜全球市场 · 亚马逊暴涨15%点燃AI云信心·费半高开低走分化加剧·美日联手干预日元</span></div>
    <div class="grid grid-cols-3 md:grid-cols-6 gap-2">{0}</div>
    <p class="text-xs text-white/50 mt-3 leading-relaxed">
      ⚡ <b class="text-yellow-400">核心要点：美股三大指数全线收涨，亚马逊暴涨15%创2012年以来最大单日涨幅，但费城半导体指数高开低走仅收涨0.07%，存储芯片继续走弱</b>——<br>
      ①<b>亚马逊财报大超预期</b>：Q2营收+13%超预期，云计算AWS增速加快，上调2026全年资本开支指引，
      AI算力供不应求趋势延续至2028年。单日市值增加超4200亿美元，创美股历史最大单日市值增幅之一。<br>
      ②<b>苹果暴跌7.35%</b>：创2025年4月以来最大跌幅。Q3营收+16%超预期但下季指引低于预期，
      存储芯片短缺影响业绩展望。单日市值蒸发超3500亿美元。<br>
      ③<b>费半指数高开低走</b>：盘中一度涨超8%（受日元干预+SK海力士暴涨带动），收盘仅涨0.07%，
      30只成分股16涨14跌，美光跌5.9%，恩智浦跌超6%，英伟达涨2.93%。
      市场对存储板块反弹的持续性存疑——脉冲式干预不等于趋势反转。<br>
      ④<b>美日联手干预日元</b>：近30年来首次联合干预，日元大幅升值，缓解全球半导体产业链成本压力，
      但市场对干预效果的持续性存在分歧。<br>
      ⑤<b>原油暴涨黄金大跌</b>：WTI原油+3.84%至86.8美元，COMEX黄金-1.49%至4098.6美元，
      风险偏好回升+通胀预期升温下贵金属承压。
    </p>
  </div>
  <div class="space-y-4">
    <div>
    <div class="text-white font-semibold mb-3 flex items-center gap-2"><span>🛢️</span><span>大宗商品</span></div>
      <div class="bg-white/5 rounded-lg p-3">{1}</div></div>
    <div>
    <div class="text-white font-semibold mb-3 flex items-center gap-2"><span>🚀</span><span>明星科技股（分化）</span></div>
      <div class="bg-white/5 rounded-lg p-3">{2}</div></div>
    <div>
    <div class="text-white font-semibold mb-3 flex items-center gap-2"><span>💻</span><span>半导体龙头（涨跌互现）</span></div>
      <div class="bg-white/5 rounded-lg p-3">{3}</div></div>
  </div>
</div>'''.format(global_cards1, global_list1, global_list2, global_list3)
gen.add_section("隔夜全球市场深度解读", global_html, "🌍")

# ========== 2. 周五A股复盘 ==========
ashare_html = '''
<div class="space-y-4">
<div class="grid md:grid-cols-4 gap-3">
  <div class="bg-gradient-to-br from-green-500/20 to-emerald-500/10 border border-green-500/30 rounded-xl p-3 text-center">
    <div class="text-xs text-white/60 mb-1">上证指数</div>
    <div class="text-xl font-bold text-green-400">3815.99</div>
    <div class="text-xs text-green-400 mt-1">-0.33% / 权重砸盘</div>
  </div>
  <div class="bg-gradient-to-br from-green-500/20 to-emerald-500/10 border border-green-500/30 rounded-xl p-3 text-center">
    <div class="text-xs text-white/60 mb-1">深证成指</div>
    <div class="text-xl font-bold text-green-400">13352.40</div>
    <div class="text-xs text-green-400 mt-1">-2.24%</div>
  </div>
  <div class="bg-gradient-to-br from-green-500/20 to-emerald-500/10 border border-green-500/30 rounded-xl p-3 text-center">
    <div class="text-xs text-white/60 mb-1">创业板指</div>
    <div class="text-xl font-bold text-green-400">3255.42</div>
    <div class="text-xs text-green-400 mt-1">-3.65% / 重挫</div>
  </div>
  <div class="bg-gradient-to-br from-yellow-500/20 to-amber-500/10 border border-yellow-500/30 rounded-xl p-3 text-center">
    <div class="text-xs text-white/60 mb-1">成交额</div>
    <div class="text-xl font-bold text-yellow-400">2.54万亿</div>
    <div class="text-xs text-white/60 mt-1">放量1991亿</div>
  </div>
</div>
<div class="bg-white/5 rounded-xl p-4">
  <h4 class="text-white font-semibold mb-3 text-sm">📊 周五（7/31）A股复盘：指数跌个股涨·冲高回落·半导体惨烈套人</h4>
  <div class="grid md:grid-cols-2 gap-4 text-xs">
    <div>
      <p class="text-white/80 font-semibold mb-2">📈 最强方向</p>
      <p class="text-white/60 leading-relaxed mb-2">
      <b class="text-yellow-400">①电力/煤炭</b>：电力板块逆势走强，乐山电力/华银电力等涨停，防御属性+夏季用电高峰催化。<br>
      <b class="text-yellow-400">②银行/大金融</b>：银行板块护盘，建行/中行/工行/农行领涨，权重股托底沪指。<br>
      ③ST板块：*ST建艺+8.5%，超跌反弹+投机资金博弈。<br>
      ④人形机器人：绿的谐波+4.2%，汇川技术+2.8%，板块相对抗跌。
      </p>
    </div>
    <div>
      <p class="text-white/80 font-semibold mb-2">📉 相对弱势</p>
      <p class="text-white/60 leading-relaxed mb-2">
      <b class="text-red-400">①半导体/存储：冲高回落惨剧</b>：早盘受韩股半导体暴涨刺激全线高开，
      雅克科技/风华高科涨停开盘，尾盘全部收跌，打板资金单日亏损超12%。
      德明利从涨停到-1.06%，普冉股份从20cm涨停到+0.41%，追高套牢惨烈。<br>
      <b class="text-red-400">②算力/光模块</b>：AI硬件方向继续调整，创业板指暴跌3.65%，科创50同步重挫。<br>
      <b class="text-red-400">③CRO/医药</b>：CRO概念大幅回调，昭衍新药/百诚医药等跌停。<br>
      <b>特征</b>：极端分化——指数大跌但4691只个股上涨、728只下跌，
      涨停101家、跌停0家，说明是权重砸盘而非普跌，中小盘在修复。
      典型"指数熊、个股牛"的背离格局。
      </p>
    </div>
  </div>
  <p class="text-xs text-white/50 mt-3 leading-relaxed">
    ⚡ <b class="text-yellow-400">盘口解读：</b>7/31是7月收官日，走出了"指数跌、个股涨"的极端背离行情。
    沪指仅跌0.33%但创业板暴跌3.65%，权重股砸盘压指数，中小盘趁机修复。
    最值得警惕的是半导体板块的"高开低走套人"走势——
    早盘韩股半导体暴涨（SK海力士+30%）刺激下全线高开，涨停板一大片，
    结果全天一路回落，收盘悉数收跌，打板资金单日最大亏损接近20%。
    这说明市场对科技股的反弹信心极度脆弱，一有反弹就有人抢跑出货。
    <b class="text-yellow-400">关键信号：</b>①成交额2.54万亿继续放量，多空博弈激烈；
    ②涨跌家数4691:728，个股赚钱效应其实不错；③零跌停说明没有系统性风险；
    ④但半导体这种冲高回落是典型的"套人K线"，短期科技股仍难有像样反弹。
  </p>
</div>
</div>'''
gen.add_section("周五A股复盘（7/31）", ashare_html, "📈")

# ========== 3. 周末重磅新闻 ==========
news_items = [
    {"tag":"🏦","title":"央行下半年工作会议定调：适度宽松+增量政策","content":"8月1日央行召开2026年下半年工作会议，核心要点：①坚定不移实施好适度宽松的货币政策，加大逆周期调节力度；②盘活存量政策+谋划增量政策；③综合运用各类工具保持流动性充裕；④用好资本市场专项支持工具，稳定和增强资本市场信心；⑤高质量建设债券市场科技板，加大科创企业金融扶持。市场解读：下半年仍有降准降息空间，流动性环境偏暖，对A股整体利好。","source":"央行官网/东方财富"},
    {"tag":"💱","title":"美日联手干预日元汇率 近30年来首次","content":"7月31日纽约交易时段，日本当局进场买日元卖美元，纽约联储代表美国财政部抛售欧元买入日元。8月2日美财长贝森特公开确认美日协调干预有效，特朗普政府强烈支持日本纠正日元大幅低估。日本财务大臣片山皋月证实联手干预，表态今后将毫不犹豫进一步联手干预。影响：日元升值缓解全球半导体产业链成本压力，但脉冲式干预不等于趋势反转，半导体高开低走已反映市场分歧。","source":"东方财富/财联社"},
    {"tag":"🤖","title":"亚马逊暴涨15% AI云业务验证资本开支兑现","content":"亚马逊Q2营收超预期+13%，云计算AWS增速加快，上调2026全年资本开支指引，明确AI算力供不应求趋势延续至2028年。单日股价+15.32%创2012年以来最大单日涨幅，市值增加超4200亿美元。谷歌同步大涨6.73%，微软+3.02%，Meta+3.28%。AI云需求的强劲验证缓解了市场对「AI资本开支不可持续」的担忧，但美光等存储芯片股仍下跌，说明板块内部分化加剧。","source":"凤凰网/第一财经"},
    {"tag":"🇰🇷","title":"韩国7月芯片出口同比+179% 连续两月破400亿美元","content":"8月1日发布的数据显示，得益于AI数据中心需求旺盛，全球存储芯片价格持续高企，韩国7月芯片出口同比飙升179%，达410亿美元，连续第二个月突破400亿美元关口。SK海力士股价7月30日暴涨30%，三星电子大涨超26%，带动韩国KOSPI指数单日暴涨近18%创历史最大单日涨幅。但7月31日高开低走，市场对持续性存疑。","source":"券商中国微博/新浪财经"},
    {"tag":"⚡","title":"发改委：十五五算力网直接投资4万亿元","content":"发改委明确「十五五」算力网直接投资4万亿元，叠加政治局会议「人工智能+」行动，算力基础设施、液冷、服务器、光模块、国产存储迎来长期政策支撑。全国一体化算力网配套细则8月1日正式公示，明确2026年9月起国内政务、央企智算中心硬件国产采购比例不低于75%，液冷作为算力机房强制配套设施，需求从可选升级为硬性合规要求。","source":"发改委/赛迪顾问"},
    {"tag":"☢️","title":"国常会一次性核准4个核电项目 总投资超1700亿","content":"国务院常务会议一次性核准4个核电项目共8台百万千瓦机组，总投资超1700亿元，核电审批常态化提速。催化核电设备、核级材料、储能、电网配套产业链。同时会议审议通过《住房公积金管理条例》修改草案，拓宽提取使用范围，托底地产链。","source":"新华社/央视新闻"},
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
gen.add_section("周末重磅新闻", news_html, "📰")

# ========== 4. 持仓诊断 ==========
holdings_html = '''
<div class="space-y-4">
  <div class="bg-gradient-to-r from-yellow-500/20 to-orange-500/20 border border-yellow-500/30 rounded-xl p-4">
    <h4 class="text-white font-bold mb-2 flex items-center gap-2">
      <span>💰</span> 持仓诊断总览（7月31日）
    </h4>
    <p class="text-white/80 text-sm leading-relaxed">
      持仓4只继续分化：*ST建艺+8.5%领涨，英维克微涨0.64%，
      雅克科技冲高回落收跌2.31%（连续3日跌幅偏离超20%触发异常波动公告），
      铜冠铜箔延续弱势。整体处于"超跌后企稳但未反转"阶段，
      操作上保持谨慎，不抄底，等右侧信号确认。
    </p>
  </div>

  <div class="grid md:grid-cols-2 gap-4">
    <!-- 英维克 -->
    <div class="bg-white/5 rounded-xl p-4 border-l-4 border-green-500/50">
      <div class="flex items-center justify-between mb-2">
        <h5 class="text-yellow-400 font-semibold text-sm">英维克 (002837)</h5>
        <span class="text-red-400 font-bold text-sm">+0.64% → 47.45元</span>
      </div>
      <div class="text-xs text-white/60 space-y-1">
        <p>📊 <b class="text-white/80">趋势判断：</b>止跌企稳迹象，从93.52元高点回撤约<b>49%</b>，47元附近有支撑</p>
        <p>💡 <b class="text-white/80">核心逻辑：</b>液冷+AI算力散热，发改委十五五算力网4万亿投资+液冷强制配套政策长期利好</p>
        <p>⚠️ <b class="text-red-400">风险：</b>中报业绩承压，科技股整体调整未结束，板块情绪仍弱</p>
        <p>🎯 <b class="text-white/80">操作建议：</b>底仓持有观望，反弹至55-60元区间减仓机动仓，不破45元不补仓</p>
        <p>📐 <b class="text-white/80">关键点位：</b>压力50/55元，支撑45/40元</p>
      </div>
    </div>

    <!-- 铜冠铜箔 -->
    <div class="bg-white/5 rounded-xl p-4 border-l-4 border-green-500/50">
      <div class="flex items-center justify-between mb-2">
        <h5 class="text-yellow-400 font-semibold text-sm">铜冠铜箔 (301217)</h5>
        <span class="text-green-400 font-bold text-sm">约82.62元 · 周线+3.91%</span>
      </div>
      <div class="text-xs text-white/60 space-y-1">
        <p>📊 <b class="text-white/80">趋势判断：</b>超跌后弱势震荡，从154元高点回撤约46%，中报利好出尽</p>
        <p>💡 <b class="text-white/80">核心逻辑：</b>锂电铜箔+PCB铜箔+AI服务器铜箔，中报预增486%但已充分兑现</p>
        <p>⚠️ <b class="text-red-400">风险：</b>PCB/存储板块调整，铜价波动，国轩高科等股东减持</p>
        <p>🎯 <b class="text-white/80">操作建议：</b>反弹85-90元减仓至底仓，80元以下关注支撑力度，不急于抄底</p>
        <p>📐 <b class="text-white/80">关键点位：</b>压力85/90元，支撑75/70元</p>
      </div>
    </div>

    <!-- 雅克科技 -->
    <div class="bg-white/5 rounded-xl p-4 border-l-4 border-red-500/50">
      <div class="flex items-center justify-between mb-2">
        <h5 class="text-yellow-400 font-semibold text-sm">雅克科技 (002409)</h5>
        <span class="text-green-400 font-bold text-sm">-2.31% → 133.80元</span>
      </div>
      <div class="text-xs text-white/60 space-y-1">
        <p>📊 <b class="text-white/80">趋势判断：</b>连续3日跌幅偏离超20%触发异常波动公告，涨停开盘跳水收跌，套人K线</p>
        <p>💡 <b class="text-white/80">核心逻辑：</b>半导体材料+HBM前驱体+光刻胶，存储链条核心标的，8月26日披露中报</p>
        <p>⚠️ <b class="text-red-400">风险：</b>融资盘踩踏（近月超70亿资金出局），存储板块情绪脆弱，机构净卖出</p>
        <p>🎯 <b class="text-white/80">操作建议：</b>底仓持有观望，反弹至150-160元减仓机动仓，130元支撑需关注，破位减仓</p>
        <p>📐 <b class="text-white/80">关键点位：</b>压力145/155元，支撑130/120元</p>
      </div>
    </div>

    <!-- *ST建艺 -->
    <div class="bg-white/5 rounded-xl p-4 border-l-4 border-red-500/50">
      <div class="flex items-center justify-between mb-2">
        <h5 class="text-yellow-400 font-semibold text-sm">*ST建艺 (002789)</h5>
        <span class="text-red-400 font-bold text-sm">+8.50% → 9.57元</span>
      </div>
      <div class="text-xs text-white/60 space-y-1">
        <p>📊 <b class="text-white/80">趋势判断：</b>ST板块超跌反弹，单日+8.5%但无基本面支撑，退市风险仍在</p>
        <p>💡 <b class="text-white/80">核心逻辑：</b>建筑装饰+ST，无明确重组预期，新增诉讼仲裁4401万元（占净资产21%）</p>
        <p>⚠️ <b class="text-red-400">风险：</b>退市归零风险，反弹是离场机会而非反转信号</p>
        <p>🎯 <b class="text-white/80">操作建议：</b><b class="text-red-400 font-bold">趁反弹坚决清仓</b>，关闭退市风险敞口，不存任何幻想</p>
        <p>📐 <b class="text-white/80">关键点位：</b>9.5-10元区间是难得的离场机会，无支撑可言</p>
      </div>
    </div>
  </div>

  <div class="bg-red-500/10 border border-red-500/30 rounded-xl p-4">
    <p class="text-red-300 text-sm font-semibold mb-2">⚠️ 持仓风险提示</p>
    <ul class="text-white/70 text-xs space-y-1">
      <li>• 四只持仓集中科技成长方向，板块系统性调整未结束</li>
      <li>• 半导体冲高回落套人K线，说明市场信心极度脆弱，反弹即有人抢跑</li>
      <li>• 雅克科技连续3日跌幅偏离超20%，融资盘踩踏风险需警惕</li>
      <li>• *ST建艺趁反弹坚决清仓，退市风险必须第一时间关闭</li>
      <li>• <b>整体仓位建议维持2成以内</b>，保留充足现金等待右侧信号确认</li>
    </ul>
  </div>
</div>'''
gen.add_section("持仓诊断", holdings_html, "💰")

# ========== 5. 题材深度分析 ==========
topic_html = '''
<div class="space-y-5">
  <!-- AI算力/液冷 -->
  <div class="bg-white/5 rounded-xl p-4 border border-white/10">
    <div class="flex items-center justify-between mb-3">
      <h4 class="text-white font-semibold flex items-center gap-2">
        <span class="text-blue-400">🧊</span> AI算力/液冷：4万亿算力网+亚马逊验证，能成为8月主线吗？
      </h4>
      <span class="px-2 py-0.5 bg-blue-500/20 text-blue-400 text-xs rounded-full border border-blue-500/30">重点关注</span>
    </div>
    <div class="grid md:grid-cols-2 gap-4 text-xs">
      <div>
        <p class="text-white/80 font-semibold mb-2">📈 催化因素</p>
        <ul class="text-white/60 space-y-1.5 leading-relaxed">
          <li>• 发改委"十五五"算力网直接投资4万亿元</li>
          <li>• 政务/央企智算中心国产采购比例≥75%</li>
          <li>• 新建大型算力中心PUE必须低于1.25</li>
          <li>• 东数西算八大枢纽液冷渗透率最低70%</li>
          <li>• 亚马逊Q2 AWS超预期，AI算力需求验证至2028年</li>
          <li>• 赛迪预测：2026年国内液冷市场规模突破1100亿，同比+270%</li>
        </ul>
      </div>
      <div>
        <p class="text-white/80 font-semibold mb-2">⚠️ 风险因素</p>
        <ul class="text-white/60 space-y-1.5 leading-relaxed">
          <li>• 板块前期涨幅大，英维克从高点已回撤49%</li>
          <li>• 中报业绩可能继续承压（一季报英维克-82%）</li>
          <li>• 政策从出台到落地有时间差，短期难有业绩兑现</li>
          <li>• 科技股整体调整，板块β压制个股α</li>
          <li>• 市场情绪脆弱，一有反弹就有人出货</li>
          <li>• 光模块等高位标的仍在调整，拖累整个算力链条</li>
        </ul>
      </div>
    </div>
    <div class="mt-3 p-3 bg-amber-500/10 border border-amber-500/30 rounded-lg">
      <p class="text-amber-300 text-sm font-semibold mb-1">💡 判断结论</p>
      <p class="text-white/70 text-xs leading-relaxed">
        AI算力/液冷是8月最值得关注的方向之一——政策面有4万亿算力网支撑，
        基本面有亚马逊验证AI需求持续性，技术面有超跌反弹需求。
        但需要注意：<b class="text-yellow-400">左侧机会不等于右侧确认</b>。
        操作建议：底仓可布局液冷龙头（英维克等），但机动仓等右侧信号——
        ①板块连续3日放量上涨；②龙头股收复20日线；③中报业绩验证。
        重点跟踪：液冷温控（英维克/高澜股份）、算力硬件、国产替代线。
        优先选择业绩能在半年报兑现的标的，纯概念标的谨慎参与。
      </p>
    </div>
  </div>

  <!-- 存储芯片 -->
  <div class="bg-white/5 rounded-xl p-4 border border-white/10">
    <div class="flex items-center justify-between mb-3">
      <h4 class="text-white font-semibold flex items-center gap-2">
        <span class="text-red-400">💾</span> 存储芯片：冲高回落套人惨案，是机会还是陷阱？
      </h4>
      <span class="px-2 py-0.5 bg-red-500/20 text-red-400 text-xs rounded-full border border-red-500/30">高风险</span>
    </div>
    <div class="grid md:grid-cols-2 gap-4 text-xs">
      <div>
        <p class="text-white/80 font-semibold mb-2">📉 空方逻辑</p>
        <ul class="text-white/60 space-y-1.5 leading-relaxed">
          <li>• 周五半导体冲高回落，打板资金单日亏近20%</li>
          <li>• 雅克科技连续3日跌幅偏离超20%，融资盘踩踏</li>
          <li>• 7月存储器指数跌近30%，半导体指数跌24%</li>
          <li>• 美光7月跌28.7%，SK海力士回撤超40%</li>
          <li>• 脉冲式日元干预不等于趋势反转，市场分歧大</li>
          <li>• 大量套牢盘，每一次反弹都是减仓机会</li>
        </ul>
      </div>
      <div>
        <p class="text-white/80 font-semibold mb-2">📈 多方逻辑</p>
        <ul class="text-white/60 space-y-1.5 leading-relaxed">
          <li>• 韩国7月芯片出口+179%，连续两月破400亿美元</li>
          <li>• 存储芯片价格仍在上涨通道，行业景气度未变</li>
          <li>• 亚马逊验证AI算力需求持续到2028年</li>
          <li>• 长江存储128层3D NAND良率90%+，月产能破10万片</li>
          <li>• 个股最大回撤50-70%，估值已大幅消化</li>
          <li>• ETF当月净买入超5050亿，机构在疯狂抄底</li>
        </ul>
      </div>
    </div>
    <div class="mt-3 p-3 bg-amber-500/10 border border-amber-500/30 rounded-lg">
      <p class="text-amber-300 text-sm font-semibold mb-1">💡 判断结论</p>
      <p class="text-white/70 text-xs leading-relaxed">
        存储芯片处于"基本面强+情绪面极弱"的背离状态。
        周五的冲高回落是典型的套人K线，说明市场信心极度脆弱——
        外围一有刺激就高开，一高开就有人抢跑出货。
        <b class="text-red-400">操作建议：不抄底，等右侧</b>。
        右侧确认条件：①美光/SK海力士连续3日不创新低；
        ②费城半导体指数收复20日线；③A股存储板块放量反弹+涨停板梯队。
        耐心等待是当前最优策略，宁可错过也不做错。
        关注国产替代线（长鑫产业链/长江存储概念）可能先于海外企稳。
      </p>
    </div>
  </div>

  <!-- 人形机器人 -->
  <div class="bg-white/5 rounded-xl p-4 border border-white/10">
    <div class="flex items-center justify-between mb-3">
      <h4 class="text-white font-semibold flex items-center gap-2">
        <span class="text-purple-400">🤖</span> 人形机器人：宇树科技8月打新催化，能否成为新主线？
      </h4>
      <span class="px-2 py-0.5 bg-purple-500/20 text-purple-400 text-xs rounded-full border border-purple-500/30">观察</span>
    </div>
    <div class="grid md:grid-cols-3 gap-3 text-xs">
      <div class="bg-white/5 rounded-lg p-3">
        <p class="text-white/80 font-semibold mb-2">催化因素</p>
        <ul class="text-white/60 space-y-1">
          <li>• 宇树科技8月10日打新上市</li>
          <li>• 政治局会议定调"AI+"行动</li>
          <li>• 机器人量产验证期到来</li>
          <li>• 板块调整充分，位置相对低</li>
        </ul>
      </div>
      <div class="bg-white/5 rounded-lg p-3">
        <p class="text-white/80 font-semibold mb-2">持续性判断</p>
        <ul class="text-white/60 space-y-1">
          <li>• 短期：事件催化型反弹</li>
          <li>• 中期：看量产进度和订单</li>
          <li>• 长期：大赛道但商业化初期</li>
          <li>• 定性：题材炒作+业绩验证期</li>
        </ul>
      </div>
      <div class="bg-white/5 rounded-lg p-3">
        <p class="text-white/80 font-semibold mb-2">操作建议</p>
        <ul class="text-white/60 space-y-1">
          <li>• 提前布局核心零部件龙头</li>
          <li>• 绿的谐波/拓普集团/汇川技术</li>
          <li>• 事件兑现前减仓，不追高</li>
          <li>• 小仓位参与，控制风险</li>
        </ul>
      </div>
    </div>
  </div>

  <!-- 美日汇率干预 -->
  <div class="bg-white/5 rounded-xl p-4 border border-white/10">
    <div class="flex items-center justify-between mb-3">
      <h4 class="text-white font-semibold flex items-center gap-2">
        <span class="text-cyan-400">💱</span> 美日联手干预日元：对半导体和A股的影响几何？
      </h4>
      <span class="px-2 py-0.5 bg-cyan-500/20 text-cyan-400 text-xs rounded-full border border-cyan-500/30">宏观变量</span>
    </div>
    <p class="text-white/60 text-xs leading-relaxed mb-3">
      美日近30年来首次联手干预日元汇率，日元大幅升值。这是周末最重要的宏观事件之一，
      直接影响全球半导体产业链成本结构和资金流向。
    </p>
    <div class="grid md:grid-cols-2 gap-3 text-xs">
      <div class="bg-white/5 rounded-lg p-3">
        <p class="text-white/80 font-semibold mb-2">📊 对半导体影响</p>
        <ul class="text-white/60 space-y-1">
          <li>• 日元升值→日本半导体设备商成本下降</li>
          <li>• 缓解韩国/台湾存储厂商价格竞争压力</li>
          <li>• 但脉冲式干预≠趋势反转，效果存疑</li>
          <li>• 费半高开低走已反映市场分歧</li>
          <li>• 真正影响要看干预是否持续</li>
        </ul>
      </div>
      <div class="bg-white/5 rounded-lg p-3">
        <p class="text-white/80 font-semibold mb-2">🎯 对A股影响</p>
        <ul class="text-white/60 space-y-1">
          <li>• 人民币汇率压力边际缓解</li>
          <li>• 外资流动可能改善</li>
          <li>• 半导体板块情绪面短期利好</li>
          <li>• 但持续性需要观察干预力度</li>
          <li>• 不宜过度解读，核心还是基本面</li>
        </ul>
      </div>
    </div>
  </div>
</div>'''
gen.add_section("题材深度分析", topic_html, "🔍")

# ========== 6. 今日操作策略 ==========
strategy_html = '''
<div class="space-y-4">
  <div class="bg-gradient-to-r from-blue-500/20 to-cyan-500/20 border border-blue-500/30 rounded-xl p-4">
    <h4 class="text-white font-bold mb-3 flex items-center gap-2">
      <span>🎯</span> 8月3日（周一）操作策略
    </h4>
    <div class="grid md:grid-cols-2 gap-4 text-xs">
      <div>
        <p class="text-white/80 font-semibold mb-2">📌 大盘判断</p>
        <ul class="text-white/60 space-y-1.5 leading-relaxed">
          <li>• 政策面偏暖（央行宽松+4万亿算力网），但市场信心仍弱</li>
          <li>• 沪指3800点附近有支撑，上方3900点压力较重</li>
          <li>• 8月开门红概率大但力度存疑，预计震荡为主</li>
          <li>• 结构性行情特征明显，权重搭台题材唱戏</li>
        </ul>
      </div>
      <div>
        <p class="text-white/80 font-semibold mb-2">⚡ 今日关注</p>
        <ul class="text-white/60 space-y-1.5 leading-relaxed">
          <li>• 全球未来存储峰会（早盘催化）</li>
          <li>• 央行3000亿隔夜逆回购操作</li>
          <li>• 中报披露进入密集期（防雷）</li>
          <li>• 北向资金流向（上周五净卖57亿）</li>
        </ul>
      </div>
    </div>
  </div>

  <div class="bg-white/5 rounded-xl p-4">
    <h5 class="text-yellow-400 font-semibold text-sm mb-3">📋 操作建议（按优先级排序）</h5>
    <div class="space-y-3 text-xs">
      <div class="flex gap-3">
        <span class="bg-red-500/20 text-red-400 px-2 py-0.5 rounded text-xs flex-shrink-0">最高优先级</span>
        <p class="text-white/70 leading-relaxed">
          <b class="text-red-400">*ST建艺趁反弹坚决清仓</b>——周五+8.5%是难得的离场机会，
          退市风险敞口必须第一时间关闭，不存任何重组幻想。
          即使亏损也要认栽，避免归零风险（永久性损失）。
        </p>
      </div>
      <div class="flex gap-3">
        <span class="bg-orange-500/20 text-orange-400 px-2 py-0.5 rounded text-xs flex-shrink-0">次优先级</span>
        <p class="text-white/70 leading-relaxed">
          <b class="text-orange-400">持仓股反弹减仓机动仓</b>——英维克/铜冠铜箔/雅克科技，
          若今日反弹至压力位（英维克50+、铜冠85+、雅克140+），
          果断减仓机动仓锁定现金，底仓保留观察。
          当前不具备全面加仓条件，现金为王。
        </p>
      </div>
      <div class="flex gap-3">
        <span class="bg-yellow-500/20 text-yellow-400 px-2 py-0.5 rounded text-xs flex-shrink-0">关注机会</span>
        <p class="text-white/70 leading-relaxed">
          <b class="text-yellow-400">液冷/算力温控方向</b>——发改委4万亿算力网+液冷强制配套政策，
          是8月最明确的政策催化方向。可小仓位关注调整充分的液冷龙头，
          但不追高，等回调再布局。优先选择有业绩支撑的标的。
        </p>
      </div>
      <div class="flex gap-3">
        <span class="bg-blue-500/20 text-blue-400 px-2 py-0.5 rounded text-xs flex-shrink-0">题材观察</span>
        <p class="text-white/70 leading-relaxed">
          <b class="text-blue-400">人形机器人</b>——宇树科技8月10日打新催化，
          可提前小仓位布局核心零部件（绿的谐波/拓普集团等），
          事件兑现前减仓，不追高。
        </p>
      </div>
    </div>
  </div>

  <div class="bg-yellow-500/10 border border-yellow-500/30 rounded-xl p-4">
    <p class="text-yellow-300 text-sm font-semibold mb-2">⚠️ 今日风险提醒</p>
    <ul class="text-white/70 text-xs space-y-1">
      <li>• 中报密集披露期，小心业绩雷，回避高位+高估值+业绩不确定的标的</li>
      <li>• 半导体冲高回落套人模式可能重演，切勿追高开盘涨幅大的科技股</li>
      <li>• 北向资金近期流出明显，关注外资动向对大盘的影响</li>
      <li>• 8月大小非解禁高峰，部分个股可能承压</li>
      <li>• <b>仓位控制在2成以内</b>，保住本金比赚钱更重要</li>
    </ul>
  </div>
</div>'''
gen.add_section("今日操作策略", strategy_html, "🎯")

# ========== 7. 预判验证闭环 ==========
prediction_html = '''
<div class="space-y-4">
  <div class="bg-white/5 rounded-xl p-4">
    <h4 class="text-white font-semibold mb-3 flex items-center gap-2">
      <span>📊</span> 预判验证 · T+N回顾
    </h4>
    <div class="space-y-3 text-xs">
      <div class="bg-red-500/10 border border-red-500/30 rounded-lg p-3">
        <div class="flex items-center justify-between mb-1">
          <span class="text-red-400 font-semibold">❌ T+5验证失败：存储芯片超级周期继续上行（7/24预判）</span>
          <span class="text-white/50">准确率: 下降中</span>
        </div>
        <p class="text-white/60 leading-relaxed">
          7月24日S级催化预判"存储芯片超级周期继续上行"，但实际7月下旬存储板块暴跌30%+，
          美光跌28.7%，SK海力士回撤超40%。
          <b class="text-red-400">失败原因</b>：忽略了市场情绪和估值层面的极端性，
          过度依赖基本面逻辑，忽视了高杠杆资金踩踏的系统性风险。
          <b>教训</b>：再好的基本面也扛不住估值泡沫+情绪反转，趋势破位时必须先减仓观望。
        </p>
      </div>
      <div class="bg-green-500/10 border border-green-500/30 rounded-lg p-3">
        <div class="flex items-center justify-between mb-1">
          <span class="text-green-400 font-semibold">✅ T+3验证成功：科技板块高低切换消费防御（7/28预判）</span>
          <span class="text-white/50">命中</span>
        </div>
        <p class="text-white/60 leading-relaxed">
          7月28日预判"科技板块高位调整，资金流向消费/金融等低位防御板块"，
          随后一周大消费/乳业/食品饮料全线爆发，银行/电力板块逆势走强，
          与预判完全一致。高低切换行情持续了一周以上。
        </p>
      </div>
      <div class="bg-amber-500/10 border border-amber-500/30 rounded-lg p-3">
        <div class="flex items-center justify-between mb-1">
          <span class="text-amber-400 font-semibold">⏳ T+2观察中：液冷板块业绩验证后反弹（7/31预判）</span>
          <span class="text-white/50">待验证</span>
        </div>
        <p class="text-white/60 leading-relaxed">
          7月31日预判"液冷板块超跌后可能迎来政策催化反弹"，
          周末发改委4万亿算力网+液冷强制配套政策落地，
          今日是验证日，观察液冷板块能否走出独立行情。
        </p>
      </div>
    </div>
  </div>
  <div class="bg-white/5 rounded-xl p-4">
    <h4 class="text-white font-semibold mb-2 flex items-center gap-2">
      <span>🔮</span> 今日预判（8/3）
    </h4>
    <div class="text-xs text-white/70 space-y-2">
      <p><b class="text-yellow-400">预判1：</b>液冷/算力温控板块今日表现强于大盘，可能成为8月首个热点方向
      （催化：发改委4万亿算力网+全球存储峰会+亚马逊AI需求验证）</p>
      <p><b class="text-yellow-400">预判2：</b>沪指8月开门红，但创业板继续弱势震荡，结构性分化延续</p>
      <p><b class="text-yellow-400">预判3：</b>半导体板块冲高回落概率大，不宜追高，等回踩再考虑</p>
    </div>
    <p class="text-white/40 text-xs mt-3">⚠️ 预判仅供参考，不构成投资建议，T+2/T+3验证后更新准确率</p>
  </div>
</div>'''
gen.add_section("预判验证闭环", prediction_html, "📊")

# ========== 8. 教训库引用 ==========
lesson_html = '''
<div class="space-y-3">
  <div class="bg-red-500/10 border border-red-500/30 rounded-lg p-3">
    <p class="text-red-300 font-semibold mb-1">教训#1：半导体高开低走是套人陷阱</p>
    <p class="text-white/60 text-xs">
      7月31日半导体板块早盘全线高开（雅克科技涨停开盘），结果收盘悉数收跌，
      打板资金单日最大亏损接近20%。这不是第一次，也不会是最后一次。
      <b>正确做法</b>：板块一致性高开时切忌追高，尤其是连续大跌后的首板，
      资金分歧极大，风险远高于机会。耐心等待回踩和充分换手，看清承接力度再进场。
    </p>
  </div>

  <div class="bg-orange-500/10 border border-orange-500/30 rounded-lg p-3">
    <p class="text-orange-300 font-semibold mb-1">教训#2：外围暴涨不等于A股跟涨</p>
    <p class="text-white/60 text-xs">
      韩股半导体暴涨30%→A股半导体高开→然后回落收跌，这个剧本已经上演过N次。
      外围情绪只能影响开盘，A股有自己的节奏和资金结构。
      <b>正确做法</b>：不因为隔夜外盘大涨就追高A股，要看A股自身的量价结构。
      真正的反转需要A股自身放量+板块联动+资金流入三重确认。
    </p>
  </div>

  <div class="bg-yellow-500/10 border border-yellow-500/30 rounded-lg p-3">
    <p class="text-yellow-300 font-semibold mb-1">教训#3：ST股反弹就是离场机会</p>
    <p class="text-white/60 text-xs">
      *ST建艺7月31日+8.5%，这是难得的离场机会，不是反转信号。
      ST股在退市风险下，任何反弹都应该减仓或清仓。
      <b>正确做法</b>：ST股坚决不碰，一旦持仓变ST必须第一时间清仓。
      退市股归零的风险是永久性损失，不值得用本金去赌重组概率。
    </p>
  </div>

  <div class="bg-green-500/10 border border-green-500/30 rounded-lg p-3">
    <p class="text-green-300 font-semibold mb-1">教训#4：政策底≠市场底</p>
    <p class="text-white/60 text-xs">
      央行定调宽松+发改委4万亿投资，这些都是政策利好，
      但政策底到市场底之间往往还有距离，中间可能还有最后一跌。
      <b>正确做法</b>：政策利好可以乐观但不要激进，
      等市场底确认（放量+趋势反转）后再加仓不迟。
      左侧布局控制仓位，右侧确认再重仓。
    </p>
  </div>

  <div class="bg-purple-500/10 border border-purple-500/30 rounded-lg p-3">
    <p class="text-purple-300 font-semibold mb-1">教训#5：亚马逊大涨≠存储芯片跟涨</p>
    <p class="text-white/60 text-xs">
      亚马逊暴涨15%验证了AI云需求，但美光还是跌了5.9%。
      这说明AI产业链内部也在分化——云厂商的盈利兑现≠硬件厂的估值修复。
      <b>正确做法</b>：区分AI产业链不同环节的逻辑和节奏，
      不要因为一个环节利好就认为整条链都会涨。
      当前阶段：应用层＞云服务层＞硬件层。
    </p>
  </div>
</div>'''
gen.add_section("教训库引用", lesson_html, "📚")

# ========== 生成+发布 ==========
output_path = os.path.join(WORK_DIR, 'docs/daily/20260803_每日新闻洞察.html')
result = gen.publish(output_path=output_path)
print("发布结果:", result)
print("成功:", result.get('success', False))
print("报告路径:", output_path)
print("文件大小:", os.path.getsize(output_path), "字节")

# 更新 latest.html
latest_path = os.path.join(WORK_DIR, 'docs/daily/latest.html')
shutil.copy2(output_path, latest_path)
print("latest.html 已更新")
