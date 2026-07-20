#!/usr/bin/env python3
"""2026年7月20日 每日新闻洞察生成 - 周一·韩股半导体暴挫·全球科技承压·万亿资金回流+国家队托底·A股绝地反击日"""
import sys, os, shutil, json
WORK_DIR = '/root/daily-news-insight'
sys.path.insert(0, os.path.join(WORK_DIR, 'v3'))
from generators.daily_pro import DailyReportProGenerator

gen = DailyReportProGenerator(
    date_str='2026年7月20日', weekday='星期一',
    subtitle='2026年7月20日 星期一 · 韩股半导体暴挫SK海力士-11.5%三星-8.8%·油价破90美元·万亿打新资金回流+国家队600亿托市·沪深港通扩容·存储情绪修复 · 持仓普跌承压日',
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
    {"name":"道琼斯","change":"-0.77%","up":False},
    {"name":"标普500","change":"-1.01%","up":False},
    {"name":"纳斯达克","change":"-1.40%","up":False},
    {"name":"费城半导体","change":"-1.63%","up":False},
    {"name":"恒生指数","change":"-1.78%","up":False},
    {"name":"日经225","change":"-0.90%","up":False},
])
global_list1 = render_list([
    {"name":"WTI原油","change":"+2.11%/83.50","up":True},
    {"name":"布伦特原油","change":"+2.76%/90.53","up":True},
    {"name":"COMEX黄金","change":"-0.27%/4008","up":False},
    {"name":"COMEX白银","change":"+0.78%/56.77","up":True},
])
global_list2 = render_list([
    {"name":"三星电子","change":"-8.77%","up":False},
    {"name":"SK海力士","change":"-11.53%","up":False},
    {"name":"三星SDI","change":"-4.30%","up":False},
    {"name":"LG新能源","change":"-0.30%","up":False},
])
global_html = '''
<div class="grid md:grid-cols-3 gap-4">
  <div class="md:col-span-2">
    <div class="text-white font-semibold mb-3 flex items-center gap-2"><span>🌍</span><span>隔夜全球市场 · 韩股半导体暴挫·油价破90美元·科技股普跌</span></div>
    <div class="grid grid-cols-3 md:grid-cols-6 gap-2">{0}</div>
    <p class="text-xs text-white/50 mt-3 leading-relaxed">
      ⚡ <b class="text-yellow-400">核心要点：海外风险偏好下降，但国内多重利好对冲</b>——
      ①<b class="text-red-400">韩股半导体暴挫</b>：三星电子-8.77%、SK海力士-11.53%（7/16数据），
      导火索：三星Q2营业利润89.4万亿韩元（同比+1810%）但低于市场预期的90-100万亿，
      韩国央行42个月来首次加息（2.50%→2.75%）推高贴现率，
      叠加韩国金融委员会收紧杠杆交易新规，引发杠杆ETF强制平仓踩踏。
      <b class="text-yellow-400">关键判断：这是情绪杀+杠杆去化，非产业逻辑反转</b>——HBM产能仍然紧缺，存储涨价周期未结束。<br>
      ②<b>美股三大指数收跌</b>：道指-0.77%、标普-1.01%、纳指-1.40%、费半-1.63%，
      应用材料大跌-5.57%（半导体设备估值压力）、英伟达-2.21%、台积电ADR-2.77%。
      但<b class="text-green-400">美股存储板块盘前超跌反弹</b>：SK海力士ADR盘前涨5.5%+，美光/西部数据/闪迪全线翻红，
      SK集团会长崔泰源喊话"AI存储需求指数级增长，市场过度看空是误判"，
      HBM4已向英伟达批量供货12层规格，订单排至2027年。<br>
      ③<b class="text-red-400">油价暴涨</b>：布油+2.76%突破90美元/桶、WTI+2.11%至83.50美元，
      伊朗革命卫队宣布"完全封锁"霍尔木兹海峡（美军空袭不停则一滴油不过），
      两艘油轮爆炸起火，中东地缘风险急剧升温。<br>
      ④<b>黄金微跌</b>：COMEX黄金-0.27%至4008美元/盎司，白银+0.78%。
      油价上涨推升通胀预期→美联储降息推迟→金价短期承压，但地缘风险提供支撑。<br>
      ⑤<b class="text-yellow-400">A股影响</b>：海外科技股下跌对A股半导体/算力有情绪压制，
      但<b>国内多重利好集中落地（万亿资金回流+国家队600亿增持+沪深港通扩容+算力政策）</b>，
      预计今日低开高走，修复行情可期。优先关注内资独立主线（人形机器人、中报业绩、国产替代）。
    </p>
  </div>
  <div class="space-y-4">
    <div>
    <div class="text-white font-semibold mb-3 flex items-center gap-2"><span>🛢️</span><span>大宗商品（油价破90）</span></div>
      <div class="bg-white/5 rounded-lg p-3">{1}</div></div>
    <div>
    <div class="text-white font-semibold mb-3 flex items-center gap-2"><span>🇰🇷</span><span>韩股核心（半导体暴挫）</span></div>
      <div class="bg-white/5 rounded-lg p-3">{2}</div></div>
  </div>
</div>'''.format(global_cards1, global_list1, global_list2)
gen.add_section("隔夜全球市场深度解读", global_html, "🌍")

# ========== 2. 上周五A股复盘 ==========
ashare_html = '''
<div class="space-y-4">
<div class="grid md:grid-cols-4 gap-3">
  <div class="bg-gradient-to-br from-green-500/20 to-emerald-500/10 border border-green-500/30 rounded-xl p-3 text-center">
    <div class="text-xs text-white/60 mb-1">上证指数</div>
    <div class="text-xl font-bold text-green-400">3764.15</div>
    <div class="text-xs text-green-400 mt-1">-3.05% / 失守3800</div>
  </div>
  <div class="bg-gradient-to-br from-green-500/20 to-emerald-500/10 border border-green-500/30 rounded-xl p-3 text-center">
    <div class="text-xs text-white/60 mb-1">深证成指</div>
    <div class="text-xl font-bold text-green-400">13706.88</div>
    <div class="text-xs text-green-400 mt-1">-5.40%</div>
  </div>
  <div class="bg-gradient-to-br from-green-500/20 to-emerald-500/10 border border-green-500/30 rounded-xl p-3 text-center">
    <div class="text-xs text-white/60 mb-1">创业板指</div>
    <div class="text-xl font-bold text-green-400">3428.63</div>
    <div class="text-xs text-green-400 mt-1">-7.15%</div>
  </div>
  <div class="bg-gradient-to-br from-yellow-500/20 to-amber-500/10 border border-yellow-500/30 rounded-xl p-3 text-center">
    <div class="text-xs text-white/60 mb-1">成交额</div>
    <div class="text-xl font-bold text-yellow-400">2.79万亿</div>
    <div class="text-xs text-white/60 mt-1">放量下杀</div>
  </div>
</div>
<div class="bg-white/5 rounded-xl p-4">
  <h4 class="text-white font-semibold mb-3 text-sm">📊 周五（7/17）A股复盘：科技成长股大溃败·沪指暴跌3%·创业板-7.15%·恐慌情绪蔓延</h4>
  <div class="grid md:grid-cols-2 gap-4 text-xs">
    <div>
      <p class="text-white/80 font-semibold mb-2">📈 相对抗跌方向</p>
      <p class="text-white/60 leading-relaxed mb-2">
      <b class="text-yellow-400">①银行/高股息（防御护盘）</b>：工商银行+0.3%，四大行尾盘护盘，避险资金涌入；<br>
      <b class="text-yellow-400">②AI算力（冲高回落）</b>：寒武纪领涨+4.2%，早盘一度强势但午后随大盘跳水；<br>
      ③存储芯片（雅克科技领涨+3.5%）：早盘强势，午后回落收窄涨幅；<br>
      ④人形机器人：三花智控领涨+2.8%，内资独立主线相对抗跌。
      </p>
    </div>
    <div>
      <p class="text-white/80 font-semibold mb-2">📉 重灾区（资金出逃）</p>
      <p class="text-white/60 leading-relaxed mb-2">
      <b class="text-green-400">①新能源（跌停潮）</b>：宁德时代/比亚迪大跌，创业板-7.15%创年内最大跌幅；<br>
      <b>②医药/消费</b>：全线普跌，防御属性失效；<br>
      ③科创50 -7.12%，半导体/芯片ETF普跌6%+；<br>
      <b class="text-yellow-400">特征</b>：约4950只个股下跌、跌停64只、放量至2.79万亿，
      涨跌比仅0.11（极度恐慌），恐惧贪婪指数22（恐惧级），
      导火索：长鑫科技IPO冻结1.7万亿资金+韩股半导体暴跌传导+获利盘集中兑现。
      </p>
    </div>
  </div>
  <p class="text-xs text-white/50 mt-3 leading-relaxed">
  ⚡ <b class="text-yellow-400">盘口解读：</b>周五是典型的"流动性抽离+情绪杀"双杀格局，
  长鑫IPO冻结万亿资金导致场内失血，叠加韩股半导体暴跌引发科技股获利盘集中出逃。
  但<b>中期逻辑未破</b>：政策底明确、产业趋势向上（AI/存储/机器人）、中报业绩支撑。
  <b class="text-yellow-400">关键信号：周末多重利好集中释放（万亿资金解冻+国家队增持+沪深港通扩容+算力政策），
  今日有望低开高走，迎来修复行情。</b>
  沪指关键支撑位3700-3750，压力位3850-3900。
  </p>
</div>
</div>'''
gen.add_section("上周五A股复盘（7/17）", ashare_html, "📉")

# ========== 3. 今日重磅新闻 ==========
news_items = [
    ('万亿资金回流🔥S级','from-green-500 to-emerald-500','长鑫IPO万亿资金今日解冻回流+国家队600亿增持托市·多重利好共振',
     '周末四重利好集中落地：①<b class="text-red-400">长鑫科技IPO冻结的1.7万亿资金今日全额解冻</b>，保险/养老金等长线资金回流沪深300/央企ETF，短线机构回补科技赛道；②<b class="text-red-400">国家队大手笔进场</b>：中国国新累计投入超500亿增持央企权重/半导体/算力，中国诚通加码近百亿布局科技ETF；③<b>沪深港通今日升级</b>：扩容标的池+下调跨境手续费15%+简化外资入市流程，吸引海外长线资金；④<b>证监会重拳维稳</b>：召开券商基金座谈会+开出6.27亿操纵市场顶格罚单+收紧融券/管控量化。<b class="text-yellow-400">关键判断：多重利好叠加，今日修复行情确定性高，但反弹高度要看成交量能否回到3万亿+。</b>来源：证监会/交易所/中国证券报'),
    ('算力政策📈S级','from-blue-500 to-cyan-500','七部委算力基础设施行动方案正式执行·国产硬件采购不低于75%·最高30%补贴',
     '七部委《2026-2028算力基础设施行动方案》今日正式执行：①<b>新建智算/超算中心国产硬件采购占比不低于75%</b>；②采购国产服务器/光模块/HBM存储最高享受30%财政补贴；③上海世界人工智能大会发布八大AI行动计划，天地一体化太空算力项目落地；④长飞光纤披露AI集群带动保偏光纤需求暴涨10-20倍，半年报预增700%+。<b class="text-yellow-400">影响：</b>算力全产业链（服务器/光模块/液冷/存储）受益明确，国产替代加速，是今日最强修复赛道之一。来源：发改委/工信部/上海证券报'),
    ('存储修复💾A级','from-purple-500 to-indigo-500','SK海力士盘前涨5.5%+·HBM4批量供货英伟达·存储情绪触底反弹',
     '美股存储板块超跌反弹：SK海力士ADR盘前涨5.5%+，美光/西部数据/闪迪全线翻红。三重利好：①<b>SK集团会长崔泰源喊话</b>：AI产业带动存储需求指数级增长，市场过度看空是误判；②<b class="text-red-400">HBM4批量供货英伟达</b>：12层规格通过新一代AI服务器认证，9月扩大出货，订单排至2027年；③<b>机构集体看多</b>：SemiAnalysis测算SK海力士2027年PE仅3.5倍处于历史洼地，巴克莱/瑞银同步上调目标价。<b class="text-yellow-400">A股影响：</b>存储板块今日有望迎来超跌修复，关注长鑫产业链（兆易创新/北方华创/澜起科技）。来源：财联社/华尔街见闻'),
    ('中东局势💥A级','from-orange-500 to-red-600','伊朗宣布完全封锁霍尔木兹海峡·布油破90美元·两艘油轮爆炸',
     '中东地缘风险急剧升温：①伊朗革命卫队7月18日宣布"完全封锁"霍尔木兹海峡，美军空袭不停则一滴油不过；②两艘油轮爆炸起火；③<b class="text-red-400">布油+2.76%突破90美元/桶</b>，WTI+2.11%至83.50美元；④市场等待7/20三大裁决：USTR关税是否扩围、霍尔木兹是否实际封锁、外资是否继续抛售韩股。<b class="text-yellow-400">影响：</b>利好油服/石油石化/煤炭（能源价格上涨）；利空航空/化工（成本上升）；加剧通胀预期→美联储降息推迟→压制成长股估值。来源：华尔街见闻/新华网'),
    ('大基金三期🏭B级','from-amber-500 to-yellow-500','3440亿大基金三期全额投放·七成倾斜设备/光刻胶/存储材料',
     '国家大基金三期3440亿资金全额投放，七成资金倾斜半导体设备、光刻胶、存储材料。叠加政务算力中心强制采购国产存储，长鑫存储/封测/电子特气企业订单持续放量。<b class="text-yellow-400">国产替代是半导体中期最确定主线，设备/材料优先受益。</b>来源：证券时报'),
    ('人形机器人🤖B级','from-indigo-500 to-blue-500','万亿设备更新专项国债落地·机器人核心零部件长期受益',
     '高端制造/工业母机/人形机器人配套万亿设备更新专项国债，中长期持续受益。人形机器人作为内资主导、与美股联动弱的独立主线，在市场修复期弹性较大。<b class="text-yellow-400">今日若随大盘低开反而是低吸核心零部件龙头的机会。</b>来源：21世纪经济报道'),
    ('电池消费税🔋B级','from-green-500 to-teal-500','9月起传统锂电征消费税·钠电/固态/钙钛矿免征至2028年底',
     '财政部/海关总署发布电池消费税新规：9月起传统锂电征收消费税，钠离子/固态/钙钛矿电池免征至2028年底。政策定向扶持下一代电池技术，板块内部分化加剧。<b>短期对锂电板块有压制，新技术路线受益。</b>来源：财政部官网'),
]
news_cards = ''
for tag, grad, title, content in news_items:
    news_cards += '<div class="bg-gradient-to-br from-white/5 to-white/0 border border-white/10 rounded-xl p-4 mb-3"><div class="flex items-center gap-2 mb-2"><span class="text-[10px] px-2 py-0.5 rounded-full bg-gradient-to-r %s text-white font-bold whitespace-nowrap">%s</span><h4 class="text-white font-semibold text-sm">%s</h4></div><p class="text-white/60 text-xs leading-relaxed">%s</p></div>' % (grad, tag, title, content)
gen.add_section("今日重磅新闻", '<div class="space-y-3">%s</div>' % news_cards, "📰")

# ========== 4. 核心题材动态 ==========
topics_data = [
    ('🧊','AI算力/液冷','七部委算力方案+国产75%采购+30%补贴·今日最强修复赛道','🔥S级-政策驱动','寒武纪、浪潮信息、英维克、中际旭创、长飞光纤',
     '政策利好集中落地：算力基础设施行动方案今日执行，国产硬件采购≥75%+最高30%补贴。长飞光纤半年报预增700%+。<b class="text-yellow-400">策略：今日高开不追，等回踩确认再加仓。优先布局光模块/液冷/服务器龙头，中报业绩确定性是核心选股标准。注意英伟达-2.21%的情绪压制。</b>'),
    ('💾','存储芯片/HBM','SK海力士盘前涨5.5%+情绪修复·长鑫万亿资金回流·国产替代加速','🟡 A级-修复期','兆易创新、北方华创、澜起科技、雅克科技、长电科技',
     '韩股暴跌后美股存储盘前反弹，HBM4供货英伟达验证需求刚性。长鑫IPO万亿资金解冻回流，叠加3440亿大基金三期投放。<b class="text-green-400">策略：上周五暴跌后今日有望超跌反弹，但持续性待观察。持仓者借反弹减仓高位标的，空仓者等企稳信号（连续2天不创新低+量缩）再进场。优先布局设备+材料（国产替代逻辑最硬）。</b>'),
    ('🤖','人形机器人','内资独立主线·万亿设备更新国债·与美股联动弱·修复弹性大','🟢 A级','埃斯顿、三花智控、绿的谐波、拓普集团、丰光精密',
     '万亿设备更新专项国债+产业催化持续（10万台产量预期）。上周五相对抗跌（三花+2.8%），内资主导独立逻辑。<b class="text-yellow-400">策略：今日重点关注，若低开可分批低吸核心零部件龙头，严格控制仓位（单票不超15%），止损设前期低点下方5%。中长期逻辑最确定的内资主线。</b>'),
    ('🛢️','石油石化/油服','伊朗封锁霍尔木兹·布油破90美元·地缘风险驱动','🔥A级-事件驱动','中国海油、中国石油、中曼石油、贝肯能源、中海油服',
     '伊朗宣布完全封锁霍尔木兹海峡+两艘油轮爆炸，布油突破90美元/桶创近期新高。<b class="text-red-400">策略：高开不追，若中东局势持续升级（实际封锁海峡）则中线有空间，否则事件驱动后可能回落。关注今明两天局势发展。EIA下调全年油价预期（布油82美元）是反向指标。</b>'),
    ('🥇','黄金/贵金属','地缘风险+央行购金支撑·油价上涨推通胀→降息推迟压制','🟡 B级-震荡','赤峰黄金、紫金矿业、山金国际、招金黄金',
     '多空交织：地缘风险（中东）+央行购金支撑金价，但油价上涨→通胀预期→美联储降息推迟→金价承压。COMEX黄金微跌-0.27%至4008美元。<b class="text-yellow-400">策略：震荡格局，等回调到3900-3950区间分批布局中长线。中东局势若持续升级则金价可能破前高。</b>'),
    ('🏦','大金融/高股息','国家队增持+万亿资金回流·防御配置首选','🟢 B级','中信证券、招商银行、工商银行、中国平安',
     '上周五银行微涨护盘，国家队增持央企权重+科技ETF。万亿打新资金解冻后长线资金优先布局高股息蓝筹。<b>可作为底仓防御配置，降低组合波动。</b>'),
    ('🏭','半导体设备/材料','大基金三期+长鑫扩产·国产替代逻辑最硬·但短期情绪承压','🟡 B级-观望','北方华创、中微公司、拓荆科技、盛美上海、华海清科',
     '长鑫295亿IPO募资中设备采购占大头，大基金三期七成投设备/材料。中期逻辑最硬，但短期板块情绪宣泄未结束。<b class="text-yellow-400">策略：等企稳信号后低吸龙头，优先布局业绩确定性强的设备+材料。今日可能随板块反弹，但反转需确认。</b>'),
    ('🔋','电池新技术','钠电/固态/钙钛矿免征消费税·传统锂电征税·政策分化','🟢 B级','（关注钠电/固态相关标的）',
     '政策定向扶持下一代电池技术，传统锂电9月起征消费税，新技术路线免征至2028年底。<b>板块内部分化加剧，回避传统锂电，关注新技术方向。</b>'),
    ('⚠️','铜箔/HVLP','铜冠铜箔逆势+1.45%·高端铜箔缺口持续·但大盘泥沙俱下','🟡 B级-谨慎','铜冠铜箔（持仓）、嘉元科技、诺德股份',
     '上周五铜冠铜箔逆势+1.45%，主力资金净流入，HVLP高端铜箔缺口持续（Q2供需缺口50%）。但大盘系统性风险下难独善其身。<b class="text-yellow-400">策略：持仓者留底仓观察中报，反弹到140-150区间可减仓部分，120元以下是加仓区间。中期逻辑不变。</b>'),
]
topic_cards = ''
for icon, name, change, level, leader, analysis in topics_data:
    topic_cards += '<div class="bg-white/5 rounded-xl p-4 border border-white/10"><div class="flex items-start justify-between mb-2"><div><div class="flex items-center gap-2 mb-1"><span class="text-xl">%s</span><h4 class="text-white font-semibold text-sm">%s</h4></div><p class="text-white/60 text-xs">%s</p></div><div class="flex flex-col items-end gap-1"><span class="text-xs font-bold text-white/80 bg-white/10 px-2 py-0.5 rounded-full">%s</span></div></div><div class="space-y-2 mb-3"><div class="flex items-center gap-2"><span class="text-white/50 text-xs">关注标的</span><span class="text-white/80 text-xs">%s</span></div></div><p class="text-white/60 text-xs leading-relaxed">%s</p></div>' % (icon, name, change, level, leader, analysis)
gen.add_section("核心题材动态", '<div class="grid md:grid-cols-2 gap-4">%s</div>' % topic_cards, "🔥")

# ========== 5. 催化剂日历 ==========
catalysts = [
    ('全天','🔥 万亿资金解冻回流','长鑫IPO 1.7万亿资金今日全额解冻·流动性修复','high','全市场（尤其科技）'),
    ('全天','🏛️ 国家队托市效应','国新500亿+诚通百亿增持·信心修复','high','央企权重/科技ETF'),
    ('全天','🌐 沪深港通升级','扩容+降费15%·外资回流预期','medium','北向持仓标的'),
    ('全天','💻 算力政策执行','七部委算力基础设施行动方案今日落地','high','算力/光模块/液冷/存储'),
    ('全天','🛢️ 中东局势演变','伊朗封锁霍尔木兹·油价破90·三大裁决日','high','油服/石油/航空/通胀'),
    ('全天','📉 半导体情绪修复','SK海力士盘前涨5.5%+·存储触底反弹','medium','存储/半导体设备'),
    ('全天','🤖 机器人低吸窗口','内资独立主线·大盘错杀低吸机会','medium','机器人核心零部件'),
    ('本周','📊 中报预告密集','7月中下旬中报预告集中披露','high','高景气龙头/规避纯概念'),
    ('本周','🔓 本周解禁','本周解禁约600亿（较上周减少）','medium','规避解禁高位股'),
    ('下周','⚡ 美联储议息会议','7/30-31议息·油价上涨推升通胀或推迟降息','high','贵金属/成长股'),
]
catalyst_cards = ''
for t,e,i,l,r in catalysts:
    lc = {'high':('from-red-500/20 to-orange-500/10 border-red-500/30','高','text-red-400'),
          'medium':('from-yellow-500/20 to-amber-500/10 border-yellow-500/30','中','text-yellow-400'),
          'low':('from-green-500/20 to-emerald-500/10 border-green-500/30','低','text-green-400')}[l]
    catalyst_cards += '<div class="bg-gradient-to-r %s border rounded-xl p-4"><div class="flex items-start justify-between"><div><div class="text-white/50 text-xs mb-1">%s</div><h4 class="text-white font-semibold text-sm mb-2">%s</h4><p class="text-white/60 text-xs">%s</p></div><span class="text-xs font-medium %s px-2 py-1 rounded-full bg-white/5">%s</span></div><div class="mt-2 pt-2 border-t border-white/10"><span class="text-white/50 text-xs">相关方向：</span><span class="text-white/70 text-xs">%s</span></div></div>' % (lc[0], t, e, i, lc[2], lc[1], r)
gen.add_section("今日/本周关键催化剂", '<div class="grid md:grid-cols-2 gap-4">%s</div><p class="text-xs text-white/40 mt-4">💡 7月核心日历：7月中下旬中报预告密集；7/22特斯拉Q2财报；7/30-31美联储议息会议；长鑫科技IPO后续进展。中东局势演变是最大不确定性变量（霍尔木兹海峡封锁是否实际执行）。</p>' % catalyst_cards, "📅")

# ========== 6. 持仓专项分析 ==========
portfolio_html = '''
<div class="space-y-4">
<div class="bg-gradient-to-r from-red-700/40 to-red-900/30 border-2 border-red-600 rounded-xl p-4">
  <div class="flex items-start gap-3"><span class="text-3xl">💀💀</span><div class="flex-1">
    <div class="flex items-center justify-between mb-1"><h4 class="text-white font-bold text-base">*ST建艺 (002789) — 止损破位·继续下探·必须不计成本清仓！</h4>
    <span class="text-red-300 font-bold text-sm">9.50元 / -8.65% / 浮亏扩大</span></div>
    <p class="text-white/70 text-xs leading-relaxed mb-2">
    【近期表现】7月17日大跌-8.65%报9.50元，主力资金大幅流出，继续创出新低。
    新规下ST涨跌幅扩大至10%，<b class="text-red-400">跌幅空间翻倍，连续下跌风险极大</b>。
    已跌破止损价12.50元，距止损位-29.4%，处于止损破位区。
    </p>
    <p class="text-white/60 text-xs leading-relaxed mb-2">
    【利空逻辑】一季报亏损5311万、累计亏损超27亿、负债率94.38%、主业持续收缩、
    庭外重组不确定性高。<b>没有任何持有理由，典型的价值毁灭标的。</b>
    </p>
    <p class="text-yellow-300 text-xs font-bold leading-relaxed">
    🚨 今日操作建议：集合竞价任何价格挂单卖出！如果开盘继续下跌，每天挂跌停价排队卖出！
    不要再抱任何幻想！这只票的底在哪里没人知道，先出来再说！
    （龙空龙纪律：破位必须止损，纪律高于一切）
    </p>
  </div></div>
</div>

<div class="bg-gradient-to-r from-orange-600/30 to-red-700/20 border border-orange-500/40 rounded-xl p-4">
  <div class="flex items-start gap-3"><span class="text-2xl">⚠️</span><div class="flex-1">
    <div class="flex items-center justify-between mb-1"><h4 class="text-white font-bold text-sm">英维克 (002837) — 液冷龙头·止损破位·借反弹大幅减仓</h4>
    <span class="text-orange-300 font-bold text-sm">61.57元 / -9.27% / 止损破位</span></div>
    <p class="text-white/70 text-xs leading-relaxed mb-2">
    【近期表现】7月17日大跌-9.27%报61.57元，主力资金大幅净流出13.4亿+，
    已跌破止损价98.0元，距止损位-37.2%，处于<b class="text-red-400">止损破位区</b>。
    从高点回撤超40%，AI液冷龙头但增收不增利（一季报净利-81.97%）。
    </p>
    <p class="text-white/60 text-xs leading-relaxed mb-2">
    【今日影响】七部委算力政策利好液冷赛道，但英伟达-2.21%+海外科技股普跌压制情绪。
    上周五随大盘暴跌，<b>短期进入超跌区域</b>，今日有望随板块反弹。
    但中期面临AI算力CAPEX见顶担忧+行业竞争加剧。
    </p>
    <p class="text-yellow-300 text-xs leading-relaxed">
    💡 操作建议：<b class="text-red-400">已严重破位，必须执行纪律减仓</b>。
    <b>今日若反弹到68-72元区间，减仓1/2到2/3</b>，将仓位降至可控范围。
    <b>支撑位58-60元（前低附近），破位继续减仓</b>。
    留小底仓观察中报业绩，若中报验证液冷订单高增则再考虑加回。
    （教训：破位不止损，亏损会扩大。严格执行龙空龙纪律！）
    </p>
  </div></div>
</div>

<div class="bg-gradient-to-r from-yellow-600/30 to-orange-600/20 border border-yellow-500/40 rounded-xl p-4">
  <div class="flex items-start gap-3"><span class="text-2xl">⚠️</span><div class="flex-1">
    <div class="flex items-center justify-between mb-1"><h4 class="text-white font-bold text-sm">雅克科技 (002409) — 半导体材料平台·暴跌-7.05%·等企稳再加</h4>
    <span class="text-yellow-300 font-bold text-sm">145.00元 / -7.05% / 盈利回吐</span></div>
    <p class="text-white/70 text-xs leading-relaxed mb-2">
    【近期表现】7月17日大跌-7.05%报145.00元，主力资金大幅净流出22.4亿+，
    从高点200+回调约30%。成本108.8元，仍盈利约33%，处于安全盈利区。
    上周五早盘一度领涨存储板块+3.5%，午后随大盘跳水翻绿。
    </p>
    <p class="text-white/60 text-xs leading-relaxed mb-2">
    【产业逻辑】半导体材料平台型公司，光刻胶+电子特气+前驱体+硅微粉多管线推进。
    大基金三期3440亿七成投设备/材料，中期受益明确。长鑫扩产带动前驱体需求。
    <b>但短期板块情绪宣泄未结束，高位股有补跌风险。</b>
    </p>
    <p class="text-yellow-300 text-xs leading-relaxed">
    💡 操作建议：<b>当前处于板块情绪宣泄期，不急于加仓</b>。
    已持仓者：<b>反弹到160-170区间减仓1/3</b>，锁定部分利润，降低半导体材料敞口。
    空仓者：<b>等企稳信号（连续2天不创新低+量缩）再考虑</b>，130-140区间是较强支撑位。
    中期看半导体材料国产替代逻辑不变，回调是布局优质龙头的机会，但需择时。
    </p>
  </div></div>
</div>

<div class="bg-gradient-to-r from-emerald-600/30 to-teal-600/20 border border-emerald-500/40 rounded-xl p-4">
  <div class="flex items-start gap-3"><span class="text-2xl">✅</span><div class="flex-1">
    <div class="flex items-center justify-between mb-1"><h4 class="text-white font-bold text-sm">铜冠铜箔 (301217) — HVLP铜箔龙头·逆势+1.45%·抗跌属性凸显</h4>
    <span class="text-emerald-300 font-bold text-sm">129.05元 / +1.45% / 盈利扩大</span></div>
    <p class="text-white/70 text-xs leading-relaxed mb-2">
    【近期表现】7月17日逆势上涨+1.45%报129.05元，主力资金净流入9.8亿+，
    成本87.16元，盈利约48%，处于安全盈利区。
    在大盘暴跌-3%/创业板-7%的环境下逆势收红，<b class="text-emerald-400">抗跌属性极强</b>。
    早盘探底后拉升，全天振幅较大，说明有资金护盘。
    </p>
    <p class="text-white/60 text-xs leading-relaxed mb-2">
    【产业逻辑】HVLP高端铜箔缺口持续扩大，2026Q2供需缺口50%，加工费15-20万/吨，毛利率50%+。
    铜冠是国内唯一HVLP1-4代全谱系量产企业，HVLP5进入验证。
    AI算力/存储HBM带动高端铜箔需求爆发，中期逻辑最硬。
    <b>注意：国轩高科上半年减持840万股套现8.29亿，第二大股东持续减持是压制因素。</b>
    </p>
    <p class="text-yellow-300 text-xs leading-relaxed">
    💡 操作建议：<b class="text-emerald-400">持仓中表现最好的标的，继续持有为主</b>。
    <b>反弹到140-150区间可减仓1/4-1/3</b>，锁定部分利润。
    <b>支撑位120元（20日线附近），回调到115-120可加仓</b>。
    中期逻辑：AI算力铜箔缺口持续至2028年，是持仓中确定性最高的标的。
    留底仓+波段操作的策略不变。
    </p>
  </div></div>
</div>

<div class="bg-white/5 rounded-xl p-4 border border-white/10">
  <h4 class="text-white font-semibold text-sm mb-3">📊 持仓总诊断（4只）</h4>
  <div class="overflow-x-auto">
    <table class="w-full text-xs">
      <thead>
        <tr class="text-white/50 border-b border-white/10">
          <th class="text-left py-2 px-2">标的</th>
          <th class="text-right py-2 px-2">现价</th>
          <th class="text-center py-2 px-2">成本</th>
          <th class="text-center py-2 px-2">盈亏</th>
          <th class="text-center py-2 px-2">趋势</th>
          <th class="text-center py-2 px-2">今日压力</th>
          <th class="text-center py-2 px-2">今日支撑</th>
          <th class="text-center py-2 px-2">操作建议</th>
          <th class="text-center py-2 px-2">优先级</th>
        </tr>
      </thead>
      <tbody class="text-white/70">
        <tr class="border-b border-white/5 bg-red-900/20">
          <td class="py-2 px-2 font-bold text-red-400">*ST建艺</td>
          <td class="text-right py-2 px-2 text-red-400">9.50</td>
          <td class="text-center py-2 px-2">13.45</td>
          <td class="text-center py-2 px-2 text-red-400">-29.4%</td>
          <td class="text-center py-2 px-2 text-red-400">↓↓ 暴跌</td>
          <td class="text-center py-2 px-2">-</td>
          <td class="text-center py-2 px-2">无底</td>
          <td class="text-center py-2 px-2 text-red-400 font-bold">不计成本清仓！</td>
          <td class="text-center py-2 px-2 text-red-400 font-bold">🔴最高</td>
        </tr>
        <tr class="border-b border-white/5 bg-orange-900/10">
          <td class="py-2 px-2 font-medium">英维克</td>
          <td class="text-right py-2 px-2">61.57</td>
          <td class="text-center py-2 px-2">104.23</td>
          <td class="text-center py-2 px-2 text-red-400">-40.9%</td>
          <td class="text-center py-2 px-2 text-orange-400">↓↓ 破位</td>
          <td class="text-center py-2 px-2">68-72</td>
          <td class="text-center py-2 px-2">58-60</td>
          <td class="text-center py-2 px-2">反弹减仓1/2-2/3</td>
          <td class="text-center py-2 px-2 text-orange-400">🟠高</td>
        </tr>
        <tr class="border-b border-white/5">
          <td class="py-2 px-2 font-medium">雅克科技</td>
          <td class="text-right py-2 px-2">145.00</td>
          <td class="text-center py-2 px-2">108.80</td>
          <td class="text-center py-2 px-2 text-emerald-400">+33.3%</td>
          <td class="text-center py-2 px-2 text-yellow-400">↓ 回调</td>
          <td class="text-center py-2 px-2">160-170</td>
          <td class="text-center py-2 px-2">130-140</td>
          <td class="text-center py-2 px-2">反弹减仓/等企稳</td>
          <td class="text-center py-2 px-2">🟡中</td>
        </tr>
        <tr class="bg-emerald-900/10">
          <td class="py-2 px-2 font-medium text-emerald-400">铜冠铜箔</td>
          <td class="text-right py-2 px-2 text-emerald-400">129.05</td>
          <td class="text-center py-2 px-2">87.16</td>
          <td class="text-center py-2 px-2 text-emerald-400">+48.1%</td>
          <td class="text-center py-2 px-2 text-emerald-400">↑ 抗跌</td>
          <td class="text-center py-2 px-2">140-150</td>
          <td class="text-center py-2 px-2">115-120</td>
          <td class="text-center py-2 px-2">持有为主/逢高减仓</td>
          <td class="text-center py-2 px-2 text-emerald-400">🟢低</td>
        </tr>
      </tbody>
    </table>
  </div>
  <p class="text-xs text-white/40 mt-3">
  ⚠️ 今日整体策略：<b class="text-yellow-400">先处理风险最高的*ST建艺（集合竞价清仓），英维克借反弹大幅减仓止损</b>。
  整体仓位控制在4-5成，现金为王，等30分钟级别止跌信号再考虑低吸。
  铜冠铜箔继续持有（抗跌+业绩确定性强），雅克科技留底仓等企稳。
  腾出的仓位可布局人形机器人（核心零部件低吸）、算力（政策受益龙头）、防御性标的。
  </p>
</div>
</div>'''
gen.add_section("持仓专项分析（4只）", portfolio_html, "💼")

# ========== 7. 预判验证闭环 ==========
verify_html = '''
<div class="bg-white/5 rounded-xl p-4 border border-white/10">
  <h4 class="text-white font-semibold text-sm mb-3">🔄 预判验证闭环（T+N回顾）</h4>
  <div class="space-y-3">
    <div class="bg-red-500/10 border border-red-500/30 rounded-lg p-3">
      <div class="flex items-center justify-between mb-1">
        <span class="text-xs font-bold text-red-400">❌ 验证失败 · T+7</span>
        <span class="text-[10px] text-white/40">7/10预判 → 7/17验证</span>
      </div>
      <p class="text-white/70 text-xs mb-1">
      <b>原预判：</b>7/10预判"存储板块短期情绪杀后企稳，等连续2天不创新低再低吸设备+材料"
      </p>
      <p class="text-white/70 text-xs mb-1">
      <b>实际走势：</b>7月中旬存储板块持续下跌，SK海力士单月回撤近40%，
      韩股多次熔断，<b class="text-red-400">调整幅度和时间远超预期</b>。
      雅克科技从高点回调约30%，设备/材料板块未能幸免。
      </p>
      <p class="text-yellow-400 text-xs">
      <b>教训：</b>存储板块调整周期比预期更长，"等企稳"策略虽然正确但低估了调整幅度。
      当全球半导体板块出现系统性风险（韩股熔断+费半暴跌）时，
      国产替代逻辑也会被大盘情绪淹没，泥沙俱下没有避风港。
      <b>改进：</b>在海外半导体大幅调整期间，应将半导体仓位降至最低（2成以内），
      等明确的企稳信号（费半连续3天反弹+韩股止跌+A股半导体放量收阳）再加仓。
      </p>
    </div>
    <div class="bg-emerald-500/10 border border-emerald-500/30 rounded-lg p-3">
      <div class="flex items-center justify-between mb-1">
        <span class="text-xs font-bold text-emerald-400">✅ 验证成功 · T+7</span>
        <span class="text-[10px] text-white/40">7/10预判 → 7/17验证</span>
      </div>
      <p class="text-white/70 text-xs mb-1">
      <b>原预判：</b>铜冠铜箔(HVLP铜箔)中期逻辑最硬，大盘调整中抗跌性强
      </p>
      <p class="text-white/70 text-xs mb-1">
      <b>实际走势：</b>7月17日大盘暴跌-3%/创业板-7%，铜冠铜箔逆势上涨+1.45%，
      <b class="text-emerald-400">抗跌属性完全验证</b>，主力资金净流入9.8亿+。
      是持仓4只中唯一收红的标的。
      </p>
      <p class="text-emerald-400 text-xs">
      <b>经验：</b>供需缺口明确+业绩弹性大+行业壁垒高的标的，
      在大盘系统性风险中表现出更强的抗跌性。
      <b>强化逻辑：</b>HVLP高端铜箔是AI算力基础设施的"血管"，
      供需缺口持续至2028年，是确定性最高的细分赛道之一。
      </p>
    </div>
  </div>
  <p class="text-xs text-white/40 mt-3">
  📊 当前准确率统计：S级分析师评级考核中，详见预判验证中心。
  7月以来预判准确率约65%（A级分析师区间），需继续提升系统性风险识别能力。
  </p>
</div>'''
gen.add_section("预判验证闭环", verify_html, "🔄")

# ========== 8. 空方视角 ==========
bear_html = '''
<div class="bg-gradient-to-br from-green-900/30 to-emerald-900/20 border border-green-500/30 rounded-xl p-4">
  <h4 class="text-green-400 font-semibold text-sm mb-3">🐻 空方视角（警惕这些风险）</h4>
  <div class="space-y-2 text-xs text-white/70 leading-relaxed">
    <p><b class="text-green-400">1. 全球半导体周期见顶风险：</b>三星1810%利润或为周期顶点，存储涨价由"单价驱动"而非"销量驱动"。韩国央行加息+杠杆收紧，韩股半导体可能继续下跌并传导至A股。应用材料-5.57%显示半导体设备估值压力。</p>
    <p><b class="text-green-400">2. 中东局势失控风险：</b>伊朗宣布完全封锁霍尔木兹海峡，若实际执行，油价可能暴涨至100+美元，全球通胀重燃→美联储被迫加息→全球股市估值下杀→A股也难以独善其身。今日是三大裁决日之一。</p>
    <p><b class="text-green-400">3. 修复行情持续性存疑：</b>万亿资金回流+国家队增持是短期利好，但市场中期趋势是否反转还需观察。若成交量不能有效放大到3万亿+，反弹可能只是技术反抽，之后继续探底。</p>
    <p><b class="text-green-400">4. 中报"利好出尽"风险：</b>7月中下旬中报密集披露期，很多高景气赛道（存储/AI/机器人）的股价已提前反映预期，业绩公布后反而可能"利好出尽"下跌（参考三星走势）。</p>
    <p><b class="text-green-400">5. 基金赎回负反馈：</b>科技主题基金前期涨幅大，若市场持续下跌引发基民赎回，将导致被动抛售，形成"下跌→赎回→更下跌"的负反馈循环。上周五放量大跌可能包含部分赎回压力。</p>
    <p><b class="text-green-400">6. 美国关税扩围风险：</b>今日USTR将就46个国家12.5%关税是否扩围作出裁决，若落地将对全球贸易和科技产业链造成冲击，需警惕黑天鹅。</p>
  </div>
  <p class="text-xs text-white/40 mt-3">
  ⚠️ 以上空方观点仅供风险参考，不代表看空市场。多方逻辑：政策底（万亿流动性+产业政策）、
  业绩底（中报高增）、估值底（回调后安全边际提升）、国家队托底。操作上保持灵活，做好两手准备。
  </p>
</div>'''
gen.add_section("空方视角·风险提示", bear_html, "🐻")

# ========== 9. 操作策略总结 ==========
strategy_html = '''
<div class="bg-gradient-to-br from-blue-900/30 to-indigo-900/20 border border-blue-500/30 rounded-xl p-4">
  <h4 class="text-blue-300 font-semibold text-sm mb-3">🎯 今日操作策略（龙空龙纪律）</h4>
  <div class="grid md:grid-cols-2 gap-4 text-xs">
    <div>
      <p class="text-white/80 font-semibold mb-2">🔴 卖出优先级（必须执行纪律）</p>
      <div class="space-y-1 text-white/70">
        <p>1. <b class="text-red-400">*ST建艺：集合竞价不计成本清仓！</b></p>
        <p>2. 英维克：反弹68-72元减仓1/2-2/3（破位止损）</p>
        <p>3. 雅克科技：反弹160-170元减仓1/3（止盈部分）</p>
        <p>4. 铜冠铜箔：反弹140-150元减仓1/4（留底仓）</p>
        <p class="text-white/50">原则：先处理风险最高的，严格执行止损纪律</p>
      </div>
    </div>
    <div>
      <p class="text-white/80 font-semibold mb-2">🟢 低吸观察（等企稳信号+控制仓位）</p>
      <div class="space-y-1 text-white/70">
        <p>1. 人形机器人核心：绿的谐波/三花/埃斯顿（低开低吸）</p>
        <p>2. 算力光模块龙头：中际旭创/长飞光纤（回踩后）</p>
        <p>3. 半导体材料：雅克科技（130-140企稳后）</p>
        <p>4. 铜冠铜箔：回调115-120加仓（中期确定性最高）</p>
        <p class="text-white/50">原则：不抄底、等企稳、分批建、严止损</p>
      </div>
    </div>
  </div>
  <div class="mt-3 pt-3 border-t border-white/10">
    <p class="text-yellow-400 text-xs font-semibold mb-1">
    ⚡ 今日关键观察点
    </p>
    <p class="text-white/60 text-xs">
    ① 开盘半小时成交量（能否到8000亿+，判断资金参与度）；② 沪指3750支撑是否有效；
    ③ 半导体板块开盘跌幅及修复力度；④ 人形机器人/算力是否领涨；
    ⑤ 中东局势最新进展+美国关税裁决；⑥ 北向资金流向（净流入则反弹持续性强）。
    </p>
  </div>
  <div class="mt-3 pt-3 border-t border-white/10">
    <p class="text-white/80 text-xs font-semibold mb-1">
    💼 仓位建议：4-5成（防御为主，留足现金）
    </p>
    <p class="text-white/50 text-xs">
    现金5-6成 / 核心持仓（铜冠+雅克底仓）2成 / 机器人低吸1成 / 防御0.5成 / 机动1.5成
    </p>
  </div>
  <div class="mt-3 pt-3 border-t border-white/10">
    <p class="text-emerald-400 text-xs font-semibold mb-1">
    ✅ 今日乐观情景（概率40%）
    </p>
    <p class="text-white/60 text-xs">
    万亿资金回流+国家队托市+政策利好共振，沪指低开高走收涨1-2%，
    科技成长股大幅反弹，成交量回到3万亿+。操作：借反弹减仓高位标的，优化持仓结构。
    </p>
  </div>
  <div class="mt-2">
    <p class="text-red-400 text-xs font-semibold mb-1">
    ⚠️ 今日悲观情景（概率30%）
    </p>
    <p class="text-white/60 text-xs">
    海外半导体继续下跌+中东局势恶化+关税利空，沪指继续下探考验3700点。
    操作：严格执行止损，继续降仓位，现金为王，等3700附近再考虑低吸。
    </p>
  </div>
</div>'''
gen.add_section("今日操作策略", strategy_html, "🎯")

# ========== 10. 教训库引用 ==========
lesson_html = '''
<div class="bg-white/5 rounded-xl p-4 border border-white/10">
  <h4 class="text-white font-semibold text-sm mb-3">📚 教训库引用（历史错误提醒）</h4>
  <div class="space-y-2 text-xs">
    <div class="bg-amber-500/10 border border-amber-500/30 rounded-lg p-2">
      <p class="text-amber-300 font-semibold mb-1">教训#1：半导体单日反弹≠企稳</p>
      <p class="text-white/60">2026/06-07 多次在半导体板块单日反弹时抄底，结果次日继续下跌。
      <b>正确做法</b>：必须等连续2天不创新低+量缩+权重股止跌的三重确认信号。</p>
    </div>
    <div class="bg-amber-500/10 border border-amber-500/30 rounded-lg p-2">
      <p class="text-amber-300 font-semibold mb-1">教训#2：破位不止损，亏损会扩大</p>
      <p class="text-white/60">英维克跌破止损价98元后未执行纪律，从98元跌到61元，亏损从10%扩大到40%+。
      <b>正确做法</b>：龙空龙纪律——跌破止损位必须第一时间减仓，纪律高于判断。</p>
    </div>
    <div class="bg-amber-500/10 border border-amber-500/30 rounded-lg p-2">
      <p class="text-amber-300 font-semibold mb-1">教训#3：利好兑现=利好出尽</p>
      <p class="text-white/60">三星1810%利润/江波龙中报等"明牌利好"，往往是股价高点。
      <b>正确做法</b>：买预期卖事实，在业绩公布前逐步兑现，不等到业绩公布当天才卖。</p>
    </div>
    <div class="bg-amber-500/10 border border-amber-500/30 rounded-lg p-2">
      <p class="text-amber-300 font-semibold mb-1">教训#4：ST股不能碰，越跌越不能补</p>
      <p class="text-white/60">*ST建艺从13元跌到9.5元，期间越跌越补只会扩大亏损。
      <b>正确做法</b>：ST股坚决不碰，一旦持仓变ST必须第一时间清仓，不存任何幻想。</p>
    </div>
  </div>
</div>'''
gen.add_section("教训库引用", lesson_html, "📚")

# ========== 生成+发布 ==========
output_path = os.path.join(WORK_DIR, 'docs/daily/20260720_每日新闻洞察.html')
result = gen.publish(output_path=output_path)
print("发布结果:", result)
print("成功:", result.get('success', False))
print("报告路径:", output_path)
print("文件大小:", os.path.getsize(output_path), "字节")

# 更新 latest.html
latest_path = os.path.join(WORK_DIR, 'docs/daily/latest.html')
shutil.copy2(output_path, latest_path)
print("latest.html 已更新")
