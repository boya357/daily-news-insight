#!/usr/bin/env python3
"""2026年8月11日 每日新闻洞察生成 - 周二·美股半导体回调费半-2.94%·原油暴涨5%黄金破4400·江波龙半年暴增715倍·韩国5万亿半导体基金·阿里云产能翻倍"""
import sys, os, shutil, json
WORK_DIR = '/root/daily-news-insight'
sys.path.insert(0, os.path.join(WORK_DIR, 'v3'))
from generators.daily_pro import DailyReportProGenerator

gen = DailyReportProGenerator(
    date_str='2026年8月11日', weekday='星期二',
    subtitle='2026年8月11日 周二 · 美股半导体回调费半-2.94%英伟达-2.86%·原油暴涨5%黄金破4400·江波龙半年暴增715倍拟回购·韩国5万亿半导体材料基金·阿里云产能翻倍',
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
        '美股回调：费半-2.94%领跌，英伟达-2.86%、英特尔-4.06%，5000亿算力融资平台信用风险升温；原油暴涨5%黄金破4400美元',
        '江波龙暴增：上半年净利105.77亿同比+71529%，Q2环比+73%，拟回购4-8亿元，存储业绩兑现超预期',
        '政策密集落地：央行"十五五"规划+煤炭工业"十五五"规划+天津机器人行动方案+韩国5万亿韩元半导体材料基金',
        '持仓策略：半导体/科技短期承压，原油黄金避险走强，铜冠铜箔/雅克科技逢高减仓，英维克反弹减仓，*ST建艺清仓'
    ],
    operation_advice='美股半导体回调+A股科技分化，今日防御为主，不追高；原油黄金等避险品种可关注，持仓科技股逢高减仓机动仓',
    risk_level='中等偏高',
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
    description='每日新闻洞察 2026年8月11日：费半-2.94%、原油暴涨5%、黄金破4400、江波龙暴增715倍、韩国5万亿半导体基金',
)

# ========== 1. 隔夜全球市场 ==========
gen.add_global_market()

global_cards1 = render_cards([
    {"name":"道琼斯","change":"-0.11%","up":False},
    {"name":"标普500","change":"-0.06%","up":False},
    {"name":"纳斯达克","change":"-0.32%","up":False},
    {"name":"费城半导体","change":"-2.94%","up":False},
    {"name":"日经225","change":"-0.90%","up":False},
    {"name":"恒生指数","change":"+1.05%","up":True},
])
global_list1 = render_list([
    {"name":"WTI原油","change":"+5.05%/$82.09","up":True},
    {"name":"布伦特原油","change":"+4.99%/$87.70","up":True},
    {"name":"COMEX黄金","change":"+1.10%/$4468.44","up":True},
    {"name":"COMEX白银","change":"+1.50%/$66.25","up":True},
])
global_list2 = render_list([
    {"name":"三星电子","change":"-0.43%","up":False},
    {"name":"SK海力士","change":"-0.14%","up":False},
    {"name":"美光科技","change":"-1.89%","up":False},
    {"name":"台积电ADR","change":"-0.37%","up":False},
])
global_list3 = render_list([
    {"name":"英伟达","change":"-2.86%/$217.55","up":False},
    {"name":"AMD","change":"-2.86%/$469.56","up":False},
    {"name":"微软","change":"+1.21%/$506.06","up":True},
    {"name":"苹果","change":"-1.53%/$308.26","up":False},
    {"name":"博通","change":"-1.25%/$422.40","up":False},
    {"name":"英特尔","change":"-4.06%/$97.52","up":False},
    {"name":"应用材料","change":"-3.16%/$522.12","up":False},
    {"name":"阿斯麦","change":"-0.43%/$1733.48","up":False},
])
global_html = '''
<div class="grid md:grid-cols-3 gap-4">
  <div class="md:col-span-2">
    <div class="text-white font-semibold mb-3 flex items-center gap-2"><span>🌍</span><span>隔夜全球市场 · 半导体回调原油暴涨·避险情绪升温·5000亿算力融资信用风险</span></div>
    <div class="grid grid-cols-3 md:grid-cols-6 gap-2">{0}</div>
    <p class="text-xs text-white/50 mt-3 leading-relaxed">
      ⚡ <b class="text-yellow-400">核心要点：美股三大指数微跌但费城半导体暴跌2.94%，英伟达-2.86%英特尔-4.06%；原油暴涨5%创数月新高（霍尔木兹海峡僵局+SPR降至1980s以来最低）；黄金破4400美元白银跟涨；中概股逆势走强金龙指数+1.59%</b>——<br>
      ①<b>半导体板块重挫</b>：费城半导体指数-2.94%收11993.86，为近期最大单日跌幅。英伟达-2.86%、AMD-2.86%、英特尔-4.06%、应用材料-3.16%。光通信板块高开低走，Coherent跌超14%（上周五+13%后获利了结），Lumentum跌超8%。存储板块分化，闪迪涨超2%，SK海力士、希捷跌超1%。<br>
      ②<b>原油暴涨5%</b>：WTI原油+5.05%收82.09美元/桶，布伦特+4.99%收87.70美元。双重催化：霍尔木兹海峡重开协议仍未达成（伊朗与美国赔偿分歧）+美国战略石油储备(SPR)降至3亿桶以下（1980年代以来最低水平）。国内原油期货主力合约日内涨4%。<br>
      ③<b>黄金白银齐涨</b>：COMEX黄金+1.10%收4468.44美元/盎司，突破4400关口创6月5日以来新高；COMEX白银+1.50%收66.25美元。现货黄金日内涨幅0.91%，白银涨超3.9%。避险情绪+降息预期+美元走弱三重支撑。汇添富黄金LOF下调大额申购至100元（8月12日起）。<br>
      ④<b>5000亿算力融资信用风险</b>：英伟达宣布与Apollo、贝莱德、黑石等六家金融机构合作设立独立算力融资平台，拟筹集逾5000亿美元用于AI基础设施建设。但市场对其信用风险担忧升温，英伟达5年期信用违约互换价格一度升至77.215个基点，创两周最大升幅。黄仁勋称资金完全来自第三方资本。<br>
      ⑤<b>中概股逆势走强</b>：纳斯达克中国金龙指数+1.59%。中进医疗+36.74%、中比能源+17%、陆金所+11.33%领涨。港股方面恒生指数+1.05%报25937.49，黄金股领涨老铺黄金+12.39%，南向资金净买入20.21亿港元。<br>
      ⑥<b>韩股小幅调整</b>：三星电子-0.43%、SK海力士-0.14%。韩国总统办公室宣布将设立5万亿韩元（约35亿美元）新基金，重点投资半导体材料、零部件和设备领域。SK海力士将在韩国投资384亿美元建设晶圆厂。
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

# ========== 2. A股昨日复盘 ==========
ashare_html = '''
<div class="space-y-4">
<div class="grid md:grid-cols-4 gap-3">
  <div class="bg-gradient-to-br from-red-500/20 to-orange-500/10 border border-red-500/30 rounded-xl p-3 text-center">
    <div class="text-xs text-white/60 mb-1">上证指数</div>
    <div class="text-xl font-bold text-red-400">3966.59</div>
    <div class="text-xs text-red-400">+0.67%</div>
  </div>
  <div class="bg-gradient-to-br from-red-500/20 to-orange-500/10 border border-red-500/30 rounded-xl p-3 text-center">
    <div class="text-xs text-white/60 mb-1">深证成指</div>
    <div class="text-xl font-bold text-red-400">14316.96</div>
    <div class="text-xs text-red-400">+0.04%</div>
  </div>
  <div class="bg-gradient-to-br from-green-500/20 to-emerald-500/10 border border-green-500/30 rounded-xl p-3 text-center">
    <div class="text-xs text-white/60 mb-1">创业板指</div>
    <div class="text-xl font-bold text-green-400">3537.21</div>
    <div class="text-xs text-green-400">-0.73%</div>
  </div>
  <div class="bg-gradient-to-br from-red-500/20 to-orange-500/10 border border-red-500/30 rounded-xl p-3 text-center">
    <div class="text-xs text-white/60 mb-1">科创50</div>
    <div class="text-xl font-bold text-red-400">--</div>
    <div class="text-xs text-red-400">--</div>
  </div>
</div>

<div class="grid md:grid-cols-2 gap-4">
  <div class="bg-white/5 rounded-xl p-4">
    <h4 class="text-white font-semibold mb-3 flex items-center gap-2"><span>📉</span> 领跌板块</h4>
    <div class="space-y-1 text-xs">
      <div class="flex justify-between"><span class="text-white/70">保险/金融</span><span class="text-green-400">-2%~-3%</span></div>
      <div class="flex justify-between"><span class="text-white/70">光通信/存储</span><span class="text-green-400">-1%~-3%</span></div>
      <div class="flex justify-between"><span class="text-white/70">自动化设备</span><span class="text-green-400">-1%~-2%</span></div>
      <div class="flex justify-between"><span class="text-white/70">通信设备</span><span class="text-green-400">-1%左右</span></div>
    </div>
  </div>
  <div class="bg-white/5 rounded-xl p-4">
    <h4 class="text-white font-semibold mb-3 flex items-center gap-2"><span>📈</span> 领涨板块</h4>
    <div class="space-y-1 text-xs">
      <div class="flex justify-between"><span class="text-white/70">贵金属/黄金</span><span class="text-red-400">+3%~+5%</span></div>
      <div class="flex justify-between"><span class="text-white/70">地面兵装/军工</span><span class="text-red-400">+2%~+4%</span></div>
      <div class="flex justify-between"><span class="text-white/70">养殖业</span><span class="text-red-400">+2%~+3%</span></div>
      <div class="flex justify-between"><span class="text-white/70">煤炭/能源</span><span class="text-red-400">+1%~+3%</span></div>
    </div>
  </div>
</div>

<div class="bg-white/5 rounded-xl p-4">
  <h4 class="text-white font-semibold mb-3 flex items-center gap-2"><span>📋</span> 昨日（周一）核心盘面回顾</h4>
  <div class="text-xs text-white/70 space-y-2 leading-relaxed">
    <p>① <b class="text-yellow-400">指数分化黄白线劈叉</b>：上证指数+0.67%收3966点（金融护盘+周期股走强），深成指微涨0.04%，创业板-0.73%（盘中一度跌超2.5%尾盘收窄）。全市场成交2.52万亿缩量1413亿，超4000只个股上涨，中小盘股强于大盘。</p>
    <p>② <b class="text-yellow-400">贵金属领涨</b>：非农爆冷+降息预期+美元走弱，黄金白银暴涨。老铺黄金+12.39%，山东黄金、赤峰黄金等领涨。汇添富黄金LOF限购至100元侧面印证资金涌入。</p>
    <p>③ <b class="text-yellow-400">科技板块高开低走</b>：PCB、光通信、存储等科技方向周一高开后大幅回落，创业板算力ETF利好兑现变利空，资金获利了结。宇树科技申购抽血效应显现，算力硬件方向表现疲软。</p>
    <p>④ <b class="text-yellow-400">军工/煤炭/养殖走强</b>：地面兵装板块领涨（军工资产注入预期），煤炭板块跟随原油上涨，养殖业因鸡苗涨价（益生股份鸡苗收入+113%）走强。市场风格偏向防御和周期。</p>
    <p>⑤ <b class="text-yellow-400">人民币创2023年2月以来新高</b>：在岸人民币兑美元收报6.7442（+0.09%），创2023年2月以来盘中新高。北向资金回流趋势延续。</p>
  </div>
</div>

<div class="bg-gradient-to-br from-blue-500/10 to-cyan-500/10 border border-blue-500/30 rounded-xl p-4">
  <h4 class="text-blue-300 font-semibold mb-3 flex items-center gap-2"><span>🔭</span> 今日（周二）展望</h4>
  <div class="text-xs text-white/70 space-y-2 leading-relaxed">
    <p>① <b class="text-yellow-400">科技承压</b>：隔夜美股半导体大跌（费半-2.94%）+昨日A股科技高开低走，今日科技板块可能继续调整。关注半导体设备材料是否相对抗跌（韩国5万亿基金催化）。</p>
    <p>② <b class="text-yellow-400">原油黄金延续</b>：原油暴涨5%+黄金破4400，能源、贵金属板块有望延续强势。煤炭"十五五"规划也利好上游资源股。</p>
    <p>③ <b class="text-yellow-400">江波龙业绩催化</b>：江波龙上半年净利105.77亿同比+71529%，Q2环比+73%，拟回购4-8亿。存储板块业绩超预期，可能带动存储方向情绪修复。</p>
    <p>④ <b class="text-yellow-400">催化剂日历</b>：今日2026博鳌系列活动开幕、能源科技创融合大会举办、第六届全球固态电池峰会（芝加哥）；本周关注国内7月金融数据、CPI数据，江波龙等存储公司中报。</p>
  </div>
</div>
</div>'''
gen.add_section("A股昨日复盘与今日展望", ashare_html, "📊")

# ========== 3. 核心题材与今日催化 ==========
catalyst_html = '''
<div class="space-y-4">
  <!-- 催化1：原油暴涨+能源 -->
  <div class="bg-gradient-to-br from-orange-500/10 to-red-500/10 border border-orange-500/30 rounded-xl p-4">
    <div class="flex items-center justify-between mb-3">
      <h4 class="text-orange-300 font-semibold flex items-center gap-2"><span>🛢️</span> S级催化：原油暴涨5%·霍尔木兹僵局+SPR新低·黄金破4400</h4>
      <span class="text-xs bg-orange-500/30 text-orange-200 px-2 py-0.5 rounded">S级·大宗</span>
    </div>
    <div class="text-xs text-white/70 space-y-2 leading-relaxed">
      <p><b class="text-yellow-400">行情：</b>WTI原油+5.05%收82.09美元/桶，布伦特+4.99%收87.70美元。COMEX黄金+1.10%破4400美元，现货白银涨超3.9%。国内原油期货主力合约涨4%，沪银涨超3%，沪金涨超2%。</p>
      <p><b class="text-yellow-400">驱动逻辑：</b></p>
      <p>① <b>霍尔木兹海峡僵局</b>：有关重开霍尔木兹海峡的协议仍未达成，伊朗与美国在赔偿问题上分歧严重。特朗普称"同样要求伊朗进行赔偿"，地缘风险持续升温。</p>
      <p>② <b>SPR创40年新低</b>：美国战略石油储备降至3亿桶以下，为1980年代以来最低水平。释放储备的"缓冲垫"已消耗殆尽，供应端更加脆弱。</p>
      <p>③ <b>黄金三重支撑</b>：降息预期（非农爆冷）+美元走弱+地缘避险，推动黄金突破4400关口。白银弹性更大，单日涨超3.9%。</p>
      <p><b class="text-yellow-400">关联标的：</b>石油（中国石油、中国海油）、黄金（山东黄金、赤峰黄金、老铺黄金）、煤炭（中国神华、陕西煤业）、白银（盛达资源、兴业银锡）</p>
    </div>
  </div>

  <!-- 催化2：江波龙业绩暴增 -->
  <div class="bg-gradient-to-br from-cyan-500/10 to-blue-500/10 border border-cyan-500/30 rounded-xl p-4">
    <div class="flex items-center justify-between mb-3">
      <h4 class="text-cyan-300 font-semibold flex items-center gap-2"><span>💾</span> A级催化：江波龙半年净利暴增715倍·存储业绩全面兑现</h4>
      <span class="text-xs bg-cyan-500/30 text-cyan-200 px-2 py-0.5 rounded">A级·业绩</span>
    </div>
    <div class="text-xs text-white/70 space-y-2 leading-relaxed">
      <p><b class="text-yellow-400">业绩数据：</b>江波龙上半年营收240.88亿元同比+136.26%，归母净利润105.77亿元同比+71528.66%。Q2净利润67.15亿，Q1为38.62亿，环比增长73%。公司拟4-8亿元回购股份。</p>
      <p><b class="text-yellow-400">市场意义：</b>存储涨价周期的业绩兑现能力远超预期。江波龙作为国内存储模组龙头，盈利能力爆发式增长验证了存储行业高景气度。摩根大通上调2026-2028年全球存储市场规模预测4-8%，预计2026年9690亿、2027年1.44万亿、2028年1.82万亿美元。</p>
      <p><b class="text-yellow-400">回购信号：</b>拟4-8亿元回购，叠加多家公司（兆驰股份3-5亿、国联民生1-2亿、永茂泰1.5-3亿等）密集发布回购方案，显示产业资本对当前估值的认可。</p>
      <p><b class="text-yellow-400">关联标的：</b>存储芯片（长鑫科技、佰维存储、德明利）、存储材料（雅克科技、华海诚科）、存储设备（拓荆科技、北方华创）</p>
    </div>
  </div>

  <!-- 催化3：韩国5万亿半导体基金 -->
  <div class="bg-gradient-to-br from-purple-500/10 to-pink-500/10 border border-purple-500/30 rounded-xl p-4">
    <div class="flex items-center justify-between mb-3">
      <h4 class="text-purple-300 font-semibold flex items-center gap-2"><span>🇰🇷</span> A级催化：韩国设5万亿韩元半导体材料基金·SK海力士384亿扩产</h4>
      <span class="text-xs bg-purple-500/30 text-purple-200 px-2 py-0.5 rounded">A级·海外映射</span>
    </div>
    <div class="text-xs text-white/70 space-y-2 leading-relaxed">
      <p><b class="text-yellow-400">韩国新基金：</b>韩国总统办公室宣布将设立价值5万亿韩元（约35亿美元）的新基金，重点投资于半导体材料、零部件和设备领域。半导体特别法今日（8月11日）正式施行，总统挂帅支持产业生态。</p>
      <p><b class="text-yellow-400">SK海力士扩产：</b>SK海力士将在韩国投资384亿美元建设晶圆厂，进一步扩大HBM和DRAM产能。三大原厂2027年产能已基本售罄，行业供需紧张格局延续。</p>
      <p><b class="text-yellow-400">国产替代映射：</b>全球半导体材料设备投资持续加码，国产替代紧迫性进一步提升。大基金三期70%投向设备材料，与韩国政策形成全球竞赛格局。</p>
      <p><b class="text-yellow-400">关联标的：</b>半导体材料（雅克科技、华海诚科、沪硅产业）、半导体设备（北方华创、拓荆科技、中微公司）、电子特气（中船特气、华特气体）</p>
    </div>
  </div>

  <!-- 催化4：央行十五五规划 -->
  <div class="bg-gradient-to-br from-blue-500/10 to-indigo-500/10 border border-blue-500/30 rounded-xl p-4">
    <div class="flex items-center justify-between mb-3">
      <h4 class="text-blue-300 font-semibold flex items-center gap-2"><span>💰</span> A级催化：央行"十五五"改革发展规划·构建现代货币政策框架</h4>
      <span class="text-xs bg-blue-500/30 text-blue-200 px-2 py-0.5 rounded">A级·政策</span>
    </div>
    <div class="text-xs text-white/70 space-y-2 leading-relaxed">
      <p><b class="text-yellow-400">核心内容：</b>央行印发《中国人民银行"十五五"改革发展规划》，配套9份细分领域行动方案。要点：构建科学稳健的货币政策体系和宏观审慎管理体系；健全中国特色现代货币政策框架，完善基础货币投放机制；健全市场化利率形成、调控和传导机制；稳妥推进金融高水平对外开放。</p>
      <p><b class="text-yellow-400">市场解读：</b>"十五五"期间货币政策将继续保持灵活适度，强调结构性工具支持科技创新和高端制造。金融对外开放持续推进，有利于外资持续流入A股。</p>
      <p><b class="text-yellow-400">煤炭工业规划：</b>发改委、能源局印发《煤炭工业发展"十五五"规划》，到2030年大型现代化煤矿产能比重提升至87%，智能化煤矿产能比例提升至75%。煤炭兜底保障能力增强，行业集中度进一步提升。</p>
    </div>
  </div>

  <!-- 催化5：阿里云产能翻倍 -->
  <div class="bg-gradient-to-br from-green-500/10 to-emerald-500/10 border border-green-500/30 rounded-xl p-4">
    <div class="flex items-center justify-between mb-3">
      <h4 class="text-green-300 font-semibold flex items-center gap-2"><span>☁️</span> B级催化：阿里云模块化数据中心产能翻倍·交付周期缩至100天</h4>
      <span class="text-xs bg-green-500/30 text-green-200 px-2 py-0.5 rounded">B级·产业</span>
    </div>
    <div class="text-xs text-white/70 space-y-2 leading-relaxed">
      <p><b class="text-yellow-400">核心信息：</b>阿里云首创全模块化设计架构，将大型AIDC数据中心交付工期缩短至100天（国内传统6-12个月、美国12-18个月），建设成本降低10%以上。今年计划将模块化数据中心全球产能提升两倍以上。</p>
      <p><b class="text-yellow-400">产业链影响：</b>国内云厂商资本开支持续加码，数据中心建设加速，利好液冷散热、UPS电源、PCB铜箔等上游供应链。液冷板块（英维克、高澜股份）长期需求逻辑进一步验证。</p>
      <p><b class="text-yellow-400">关联标的：</b>液冷散热（英维克、高澜股份）、数据中心（宝信软件、光环新网）、PCB铜箔（铜冠铜箔、沪电股份）</p>
    </div>
  </div>

  <!-- 催化6：ETF规模逼近5万亿 -->
  <div class="bg-gradient-to-br from-yellow-500/10 to-orange-500/10 border border-yellow-500/30 rounded-xl p-4">
    <div class="flex items-center justify-between mb-3">
      <h4 class="text-yellow-300 font-semibold flex items-center gap-2"><span>📊</span> B级催化：ETF规模逼近5万亿·半导体材料份额增长最快</h4>
      <span class="text-xs bg-yellow-500/30 text-yellow-200 px-2 py-0.5 rounded">B级·资金面</span>
    </div>
    <div class="text-xs text-white/70 space-y-2 leading-relaxed">
      <p><b class="text-yellow-400">规模数据：</b>截至8月10日，下半年以来ETF份额增加3742亿份至3.4万亿份，总规模增长2534亿元至4.99万亿元，逼近5万亿大关。下半年新发行48只ETF，总数达1629只。</p>
      <p><b class="text-yellow-400">资金流向：</b>金融主题ETF份额增加最多（31只基金跟踪），半导体材料设备指数标的份额增长居首，黄金股票指数标的收益表现最佳。被动资金持续涌入科技和资源赛道。</p>
      <p><b class="text-yellow-400">意义：</b>ETF已成为A股市场最重要的增量资金来源之一，机构化趋势加速。半导体材料设备ETF份额增长最快，说明机构资金最看好这一方向。</p>
    </div>
  </div>
</div>'''
gen.add_section("核心题材与今日催化", catalyst_html, "🔥")

# ========== 4. 持仓诊断 ==========
portfolio_html = '''
<div class="space-y-4">
  <!-- 铜冠铜箔 -->
  <div class="bg-gradient-to-br from-yellow-500/20 to-orange-500/10 border border-yellow-500/40 rounded-xl p-4">
    <div class="flex items-center justify-between mb-3">
      <div class="flex items-center gap-2">
        <span class="bg-yellow-500 text-white text-xs px-2 py-0.5 rounded-full font-bold">持仓</span>
        <span class="text-white font-bold text-lg">铜冠铜箔 (301217)</span>
      </div>
      <div class="text-right">
        <div class="text-xl font-bold text-yellow-400">高位震荡</div>
        <div class="text-xs text-yellow-400">8月10日 · 高开低走·存储分化</div>
      </div>
    </div>
    <div class="grid md:grid-cols-3 gap-3 text-xs">
      <div class="bg-white/5 rounded-lg p-3">
        <div class="text-white/60 mb-1">最新评级</div>
        <div class="text-yellow-400 font-semibold">🟡 高位震荡·逢高减仓</div>
      </div>
      <div class="bg-white/5 rounded-lg p-3">
        <div class="text-white/60 mb-1">关键价位</div>
        <div class="text-white font-semibold">压力120 / 支撑105</div>
      </div>
      <div class="bg-white/5 rounded-lg p-3">
        <div class="text-white/60 mb-1">操作建议</div>
        <div class="text-white font-semibold">反弹减仓·控制仓位</div>
      </div>
    </div>
    <div class="mt-3 text-xs text-white/70 leading-relaxed">
      <p><b class="text-yellow-400">📊 盘面解读</b>：铜冠铜箔周五大涨17%后，周一高开低走，科技板块整体分化。费半隔夜-2.94%、存储板块美股表现分化（闪迪涨但SK海力士跌），短期获利盘丰厚，调整压力较大。</p>
      <p class="mt-2"><b class="text-yellow-400">🎯 催化验证</b>：江波龙上半年净利暴增715倍，存储业绩兑现超预期，对铜冠铜箔的材料需求逻辑形成支撑。但短期股价涨幅过大，业绩利好可能已提前price in。</p>
      <p class="mt-2"><b class="text-yellow-400">⚡ 操作方案</b>：<br>
      ① 若反弹至115-120元区间，继续减仓至1/3底仓，锁定利润；<br>
      ② 跌破105元止盈至底仓，跌破100元清仓；<br>
      ③ 江波龙业绩可能带动存储情绪，但高开仍是减仓机会而非加仓时机；<br>
      ④ 整体仓位控制，不要在高位追加。</p>
    </div>
  </div>

  <!-- 雅克科技 -->
  <div class="bg-gradient-to-br from-yellow-500/20 to-orange-500/10 border border-yellow-500/40 rounded-xl p-4">
    <div class="flex items-center justify-between mb-3">
      <div class="flex items-center gap-2">
        <span class="bg-yellow-500 text-white text-xs px-2 py-0.5 rounded-full font-bold">持仓</span>
        <span class="text-white font-bold text-lg">雅克科技 (002409)</span>
      </div>
      <div class="text-right">
        <div class="text-xl font-bold text-yellow-400">震荡整理</div>
        <div class="text-xs text-yellow-400">8月10日 · 半导体材料相对抗跌</div>
      </div>
    </div>
    <div class="grid md:grid-cols-3 gap-3 text-xs">
      <div class="bg-white/5 rounded-lg p-3">
        <div class="text-white/60 mb-1">最新评级</div>
        <div class="text-yellow-400 font-semibold">🟡 底仓持有·反弹减仓</div>
      </div>
      <div class="bg-white/5 rounded-lg p-3">
        <div class="text-white/60 mb-1">关键价位</div>
        <div class="text-white font-semibold">压力155-160 / 支撑140</div>
      </div>
      <div class="bg-white/5 rounded-lg p-3">
        <div class="text-white/60 mb-1">操作建议</div>
        <div class="text-white font-semibold">150上方减仓1/3</div>
      </div>
    </div>
    <div class="mt-3 text-xs text-white/70 leading-relaxed">
      <p><b class="text-yellow-400">📊 盘面解读</b>：雅克科技8月26日将披露中报，市场对HBM前驱体业务高度关注。韩国5万亿韩元半导体材料基金对材料板块情绪有支撑。江波龙暴增715倍验证存储产业链高景气，雅克作为上游材料间接受益。</p>
      <p class="mt-2"><b class="text-yellow-400">🎯 核心矛盾</b>：长期逻辑（HBM前驱体+国产替代+存储高景气）依然强劲，但短期股价从127反弹至150附近（+18%），积累了一定获利盘。隔夜美股半导体回调可能影响情绪。</p>
      <p class="mt-2"><b class="text-yellow-400">⚡ 操作方案</b>：<br>
      ① 150-155元区间减仓1/3锁定利润，底仓保留2/3；<br>
      ② 若受江波龙业绩催化冲160元，可继续减仓至底仓；<br>
      ③ 跌破142元止盈至底仓，跌破130元全部清仓；<br>
      ④ 中报前可能有资金博弈业绩，但不建议追高，逢高减仓为主。</p>
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
        <div class="text-xl font-bold text-yellow-400">弱势震荡</div>
        <div class="text-xs text-yellow-400">8月10日 · 液冷跟随·弱于大盘</div>
      </div>
    </div>
    <div class="grid md:grid-cols-3 gap-3 text-xs">
      <div class="bg-white/5 rounded-lg p-3">
        <div class="text-white/60 mb-1">最新评级</div>
        <div class="text-yellow-400 font-semibold">🟡 深度套牢·反弹减仓</div>
      </div>
      <div class="bg-white/5 rounded-lg p-3">
        <div class="text-white/60 mb-1">关键价位</div>
        <div class="text-white font-semibold">压力60元 / 支撑52元</div>
      </div>
      <div class="bg-white/5 rounded-lg p-3">
        <div class="text-white/60 mb-1">操作建议</div>
        <div class="text-white font-semibold">60元附近减仓≥1/2</div>
      </div>
    </div>
    <div class="mt-3 text-xs text-white/70 leading-relaxed">
      <p><b class="text-yellow-400">📊 盘面解读</b>：英维克液冷板块持续弱势，尽管阿里云数据中心产能翻倍（长期利好液冷需求），但短期资金不关注这个方向。英伟达5000亿算力融资计划侧面验证AI基建需求，但信用风险担忧升温。</p>
      <p class="mt-2"><b class="text-yellow-400">🎯 核心矛盾</b>：液冷长期逻辑不变（AI算力爆发+PUE限制+渗透率提升），但短期资金偏好周期/资源/贵金属，科技成长股承压。英维克从高点回撤超60%，下降趋势未改。</p>
      <p class="mt-2"><b class="text-yellow-400">⚡ 操作方案</b>：<br>
      ① 反弹至58-60元区间坚决减仓≥1/2，降低持仓风险；<br>
      ② 若突破60元可少量留仓博弈65元，但55元为止盈线；<br>
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
        <div class="text-xl font-bold text-red-400">退市风险</div>
        <div class="text-xs text-red-400">立即清仓·不要抱幻想</div>
      </div>
    </div>
    <div class="bg-red-500/10 border border-red-500/30 rounded-lg p-3 mb-3">
      <p class="text-red-300 text-xs font-semibold">⚠️ 最高优先级：立即清仓止损，退市风险敞口必须关闭</p>
    </div>
    <div class="text-xs text-white/70 leading-relaxed">
      <p><b class="text-yellow-400">📰 最新动态</b>：*ST建艺持续弱势，退市风险未解除。公司推进重组已提交摘帽申请但结果未知，存在重大不确定性。浮亏持续扩大。</p>
      <p class="mt-2"><b class="text-yellow-400">⚡ 操作策略</b>：退市风险股，任何价格立即清仓。退市风险+债务问题未消除，不要抱有任何幻想。ST股的基本面不会因为股价反弹而改善，早一天减仓少一分风险。</p>
    </div>
  </div>

  <!-- 组合总览 -->
  <div class="bg-white/5 rounded-xl p-4">
    <h4 class="text-white font-semibold mb-3 flex items-center gap-2"><span>📋</span> 组合总览与今日策略</h4>
    <div class="text-xs text-white/70 space-y-2 leading-relaxed">
      <p><b class="text-yellow-400">昨日表现</b>：科技板块高开低走，贵金属/能源走强。持仓整体表现分化，铜冠铜箔/雅克科技高开回落，英维克弱势震荡，*ST建艺持续走弱。组合跑输大盘（周期/防御领涨）。</p>
      <p><b class="text-yellow-400">今日策略（8月11日周二）：</b><br>
      ① 隔夜美股半导体大跌+原油黄金暴涨，市场风格继续偏向防御/周期，科技承压，<b>不追高、逢高减仓</b>；<br>
      ② <b>铜冠铜箔</b>：江波龙业绩可能催化存储情绪反弹，逢高（115-120）继续减仓至1/3底仓；<br>
      ③ <b>雅克科技</b>：韩国5万亿材料基金+江波龙业绩双催化，150-155元减仓1/3，中报前不追高；<br>
      ④ <b>英维克</b>：阿里云产能翻倍是长期利好但短期不涨，60元附近坚决减仓，跌破52元清仓；<br>
      ⑤ <b>*ST建艺</b>：立即清仓（最高优先级）；<br>
      ⑥ 整体仓位4-5成，防御为主，可关注黄金/原油等避险品种，科技股等待调整到位后的机会。</p>
    </div>
  </div>
</div>'''
gen.add_section("持仓诊断与操作建议", portfolio_html, "💼")

# ========== 5. 空方视角 ==========
bear_html = '''
<div class="space-y-4">
  <div class="bg-red-500/10 border border-red-500/30 rounded-xl p-4">
    <h4 class="text-red-300 font-semibold mb-3 flex items-center gap-2"><span>🐻</span> 空方观点：半导体回调开启·AI信用风险·科技估值重构</h4>
    <div class="text-xs text-white/70 space-y-3 leading-relaxed">
      <div class="bg-white/5 rounded-lg p-3">
        <p class="text-red-300 font-semibold mb-1">风险1：费半-2.94%，半导体开启调整浪</p>
        <p>费城半导体指数单日暴跌2.94%，英伟达-2.86%、英特尔-4.06%、应用材料-3.16%。
        光通信Coherent从+13%到-14%，两天波动超27%，说明市场情绪极度不稳定。
        如果半导体龙头开始回调，A股科技股很难独善其身，尤其是前期涨幅大的品种。</p>
      </div>
      <div class="bg-white/5 rounded-lg p-3">
        <p class="text-red-300 font-semibold mb-1">风险2：5000亿算力融资信用风险</p>
        <p>英伟达联合六大金融机构设立5000亿美元算力融资平台，但市场担忧信用风险——
        英伟达5年期CDS价格创两周最大升幅。AI资本开支泡沫担忧升温，如果这5000亿最终变成坏账，
        将对全球金融体系和AI产业链造成双重冲击。黄仁勋称"资金完全来自第三方"，侧面说明英伟达也不愿承担风险。</p>
      </div>
      <div class="bg-white/5 rounded-lg p-3">
        <p class="text-red-300 font-semibold mb-1">风险3：宇树科技+IPO抽血效应</p>
        <p>宇树科技申购中签率仅0.018%，说明资金极度追捧。但610亿市值募资61亿，
        加上长鑫科技3.28万亿巨无霸持续吸金，硬科技IPO密集，存量博弈下新股抽血导致老股估值承压。
        周一创业板-0.73%、科技股高开低走，已经反映了抽血效应。</p>
      </div>
      <div class="bg-white/5 rounded-lg p-3">
        <p class="text-red-300 font-semibold mb-1">风险4：地缘冲突升级风险</p>
        <p>霍尔木兹海峡僵局持续，特朗普与伊朗互相要求赔偿，地缘风险升温。
        原油暴涨5%如果持续，将推高通胀，影响美联储降息节奏。
        地缘冲突往往导致风险资产（尤其是科技成长股）承压，资金流向黄金、原油等避险品种。</p>
      </div>
      <div class="bg-white/5 rounded-lg p-3">
        <p class="text-red-300 font-semibold mb-1">风险5：中报密集披露期的业绩地雷</p>
        <p>8月中下旬进入中报密集披露期，很多科技股前期涨得多但业绩能否兑现存疑。
        江波龙暴增715倍是个案，大多数公司可能达不到市场预期。
        一旦业绩不及预期，前期涨幅大的股票可能出现暴跌。</p>
      </div>
    </div>
  </div>

  <div class="bg-green-500/10 border border-green-500/30 rounded-xl p-4">
    <h4 class="text-green-300 font-semibold mb-3 flex items-center gap-2"><span>🐂</span> 多方反驳：业绩兑现+流动性宽松+国产替代三逻辑不变</h4>
    <div class="text-xs text-white/70 space-y-2 leading-relaxed">
      <p>① <b>存储业绩全面爆发</b>：江波龙暴增715倍不是个案，而是行业性的。
      摩根大通上调存储市场规模预测4-8%，2028年达1.82万亿美元。
      三大原厂产能售罄、SK海力士384亿美元扩产，说明产业端对需求非常有信心。</p>
      <p>② <b>全球流动性拐点确认</b>：非农爆冷后加息周期基本结束，全球流动性宽松是大趋势。
      人民币创2023年以来新高，北向资金持续回流，A股估值修复的基础依然牢固。</p>
      <p>③ <b>国产替代加速</b>：韩国5万亿半导体材料基金+大基金三期，全球竞赛格局下国产替代只会加速不会减速。
      雅克科技、华海诚科、北方华创等龙头企业长期成长空间巨大。</p>
      <p>④ <b>短期回调是健康调整</b>：费半-2.94%是在连续上涨后的正常回调，不是趋势反转。
      从技术面看，半导体指数仍在上升通道中，回调是加仓机会不是清仓信号。</p>
      <p>⑤ <b>政策面持续友好</b>：央行"十五五"规划定调宽松+金融对外开放+产业政策持续加码，
      国内政策环境对科技成长股非常友好。</p>
    </div>
  </div>

  <div class="bg-yellow-500/10 border border-yellow-500/30 rounded-xl p-4">
    <h4 class="text-yellow-300 font-semibold mb-2 flex items-center gap-2"><span>⚖️</span> 综合判断</h4>
    <p class="text-xs text-white/70 leading-relaxed">
      短期（1-2周）：美股半导体回调+A股科技高开低走，科技板块短期承压，
      资金流向贵金属、能源等防御品种。但存储业绩超预期（江波龙）和国产替代逻辑（韩国基金）提供支撑。
      操作上控制仓位，逢高减仓机动仓，保留底仓观望。<br>
      中期（1-3个月）：全球流动性宽松+AI需求爆发+国产替代三逻辑不变，
      科技成长股中期向好。中报业绩验证后，优质标的将迎来更好的布局机会。<br>
      <b class="text-yellow-400">核心结论：短期防御为主，控制仓位在4-5成，
      科技股逢高减仓不追高，等待调整到位后的机会。关注中报业绩和原油价格走势。</b>
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
          <span class="text-green-300 font-semibold">预判#20260810-01：非农后科技股延续反弹</span>
          <span class="text-xs bg-green-500/30 text-green-200 px-2 py-0.5 rounded">验证中·T+1</span>
        </div>
        <p class="text-white/70">预判内容：非农爆冷+美股创新高后，周一A股高开但分化，光通信/半导体设备相对强势，存储冲高回落。</p>
        <p class="text-white/50 mt-1">当前进度：周一A股沪指+0.67%但创业板-0.73%，科技高开低走，贵金属/周期领涨。预判的"分化"验证正确，但方向上科技弱于预期，周期强于预期。</p>
      </div>
      <div class="bg-yellow-500/10 border border-yellow-500/30 rounded-lg p-3">
        <div class="flex justify-between mb-2">
          <span class="text-yellow-300 font-semibold">预判#20260807-01：非农后科技股延续反弹</span>
          <span class="text-xs bg-yellow-500/30 text-yellow-200 px-2 py-0.5 rounded">验证中·T+2</span>
        </div>
        <p class="text-white/70">预判内容：非农数据公布后，若不及预期则加息概率下降、科技股延续反弹，光通信/半导体设备领涨。</p>
        <p class="text-white/50 mt-1">当前进度：T+2验证，美股周五纳指+1.3%费半+2.56%验证正确，但周一美股回调费半-2.94%，A股也高开低走。反弹持续性存疑，需要更多时间验证。</p>
      </div>
      <div class="bg-green-500/10 border border-green-500/30 rounded-lg p-3">
        <div class="flex justify-between mb-2">
          <span class="text-green-300 font-semibold">预判#20260803-01：雅克科技跌停后3日内反弹</span>
          <span class="text-xs bg-green-500/30 text-green-200 px-2 py-0.5 rounded">已验证·正确</span>
        </div>
        <p class="text-white/70">预判内容：雅克科技跌停板机构抄底近5亿，预计3个交易日内出现5-10%反弹。</p>
        <p class="text-white/50 mt-1">实际走势：从8月4日跌停价127元反弹至最高155元附近（+22%），远超预期。验证正确，但中间波动较大。</p>
      </div>
      <div class="bg-green-500/10 border border-green-500/30 rounded-lg p-3">
        <div class="flex justify-between mb-2">
          <span class="text-green-300 font-semibold">预判#20260730-02：存储板块调整期2-3周</span>
          <span class="text-xs bg-green-500/30 text-green-200 px-2 py-0.5 rounded">已验证·正确</span>
        </div>
        <p class="text-white/70">预判内容：7月30日科技股大跌后，存储板块进入2-3周调整期，调整幅度约15-25%。</p>
        <p class="text-white/50 mt-1">当前进度：第9个交易日，板块从高点回调约20-25%，幅度和时间均符合预期。
        PCB铜箔方向率先反弹（铜冠铜箔+17%），存储芯片方向仍在底部震荡。江波龙业绩可能开启第二波。</p>
      </div>
      <div class="bg-red-500/10 border border-red-500/30 rounded-lg p-3">
        <div class="flex justify-between mb-2">
          <span class="text-red-300 font-semibold">新增预判#20260811-01：江波龙业绩催化存储修复</span>
          <span class="text-xs bg-red-500/30 text-red-200 px-2 py-0.5 rounded">待验证·T+2</span>
        </div>
        <p class="text-white/70">预判内容：江波龙半年净利暴增715倍+回购，将催化存储板块情绪修复，
        存储材料（雅克科技、华海诚科）和存储芯片方向有望迎来3-5%的反弹，持续2-3个交易日。</p>
        <p class="text-white/50 mt-1">验证时间：8月13日（T+2）验证反弹幅度和持续性</p>
      </div>
    </div>
  </div>

  <div class="bg-white/5 rounded-xl p-4">
    <h4 class="text-white font-semibold mb-2 flex items-center gap-2"><span>📊</span> 准确率统计</h4>
    <div class="grid grid-cols-3 gap-3 text-center text-xs">
      <div class="bg-white/5 rounded-lg p-2">
        <div class="text-lg font-bold text-yellow-400">70%</div>
        <div class="text-white/60">总体准确率</div>
      </div>
      <div class="bg-white/5 rounded-lg p-2">
        <div class="text-lg font-bold text-green-400">12/17</div>
        <div class="text-white/60">已验证正确/总数</div>
      </div>
      <div class="bg-white/5 rounded-lg p-2">
        <div class="text-lg font-bold text-blue-400">5</div>
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
    <p class="text-red-300 font-semibold mb-1">教训#1：大涨次日高开低走是常态，高开减仓铁律</p>
    <p class="text-white/60 text-xs">
      周一科技股高开低走完美应验了这条教训。上周五铜冠铜箔+17%，周一高开后低走；
      上周五费半+2.56%，周一美股回调-2.94%。大涨次日往往是情绪最高点，也是最好的减仓点。
      <b>正确做法</b>：大涨次日高开坚决减仓，不要等"再涨一点"，
      90%的情况下高开就是当天最高点。宁可卖飞不可被套。
    </p>
  </div>

  <div class="bg-orange-500/10 border border-orange-500/30 rounded-lg p-3">
    <p class="text-orange-300 font-semibold mb-1">教训#2：外围涨跌≠A股对应板块涨跌，看资金偏好</p>
    <p class="text-white/60 text-xs">
      上周五美股光通信暴涨（Coherent+13%），周一A股光通信反而高开低走。
      很多人看到外围涨就冲进去，结果当天被套。A股有自己的节奏和资金偏好，
      外围涨跌只是情绪催化，最终决定走势的是A股自己的资金面和技术面。
      <b>正确做法</b>：外围大涨只是高开的理由，不是追高的理由。
      要看A股对应板块的技术形态和资金流向，而不是简单照搬外围走势。
    </p>
  </div>

  <div class="bg-yellow-500/10 border border-yellow-500/30 rounded-lg p-3">
    <p class="text-yellow-300 font-semibold mb-1">教训#3：业绩暴增≠股价上涨，利好出尽是利空</p>
    <p class="text-white/60 text-xs">
      江波龙上半年净利暴增715倍，听起来很吓人，但股价未必涨。
      因为业绩好早已被市场预期到了，存储涨价周期是明牌，
      业绩公布反而可能是"利好出尽"，资金借利好出货。
      <b>正确做法</b>：业绩暴增但股价在高位的，不要追涨，
      反而可以考虑减仓。业绩好+股价在低位的，才是布局机会。
      江波龙从低点涨了多少？如果已经涨了好几倍，那业绩暴增就是出货信号。
    </p>
  </div>

  <div class="bg-green-500/10 border border-green-500/30 rounded-lg p-3">
    <p class="text-green-300 font-semibold mb-1">教训#4：地缘冲突买黄金原油，科技成长先回避</p>
    <p class="text-white/60 text-xs">
      霍尔木兹海峡僵局+原油暴涨5%+黄金破4400，这是典型的地缘风险升温场景。
      每次地缘冲突，都是科技成长股跌、黄金原油涨。
      但很多人第一反应是"买科技"而不是"买避险"，结果吃了大亏。
      <b>正确做法</b：地缘冲突时第一时间减仓科技成长股，
      加仓黄金、原油、军工等避险/受益品种。
      等冲突缓和、油价回落，再把科技加回来。
    </p>
  </div>

  <div class="bg-purple-500/10 border border-purple-500/30 rounded-lg p-3">
    <p class="text-purple-300 font-semibold mb-1">教训#5：5000亿融资≠利好，信用风险要警惕</p>
    <p class="text-white/60 text-xs">
      英伟达联合六大金融机构搞5000亿美元算力融资平台，听起来是"AI超级利好"，
      但市场反应是英伟达CDS飙升——市场担心的是信用风险。
      这5000亿如果变成坏账，对全球金融体系的冲击可比2008年次贷危机。
      <b>正确做法</b>：大规模融资/杠杆扩张，短期可能刺激需求，
      但长期累积信用风险。对AI资本开支的可持续性要保持警惕，
      不要盲目相信"永动机"式的增长故事。
    </p>
  </div>

  <div class="bg-blue-500/10 border border-blue-500/30 rounded-lg p-3">
    <p class="text-blue-300 font-semibold mb-1">教训#6：IPO密集期=老股抽血，减仓等待</p>
    <p class="text-white/60 text-xs">
      宇树科技、长鑫科技、燧原科技……硬科技IPO一个接一个，
      每一个都是几百亿上千亿的募资规模。存量博弈下，新股发行就是对老股的抽血。
      7月以来科技板块持续调整，IPO密集发行是重要原因之一。
      <b>正确做法</b>：IPO密集期适当降低科技股仓位，
      等待IPO高峰过去、市场资金面改善后再加仓。
      不要跟IPO抢资金，抢不过的。
    </p>
  </div>
</div>'''
gen.add_section("教训库引用", lesson_html, "📚")

# ========== 生成+发布 ==========
output_path = os.path.join(WORK_DIR, 'docs/daily/20260811_每日新闻洞察.html')
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
