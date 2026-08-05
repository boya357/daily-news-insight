#!/usr/bin/env python3
"""2026年8月5日 每日新闻洞察生成 - 周三·费城半导体暴涨6.55%·存储芯片超级周期确认·央行5000亿放水·A股科技高开待验证"""
import sys, os, shutil, json
WORK_DIR = '/app/data/所有对话/主对话'
sys.path.insert(0, os.path.join(WORK_DIR, 'v3'))
from generators.daily_pro import DailyReportProGenerator

gen = DailyReportProGenerator(
    date_str='2026年8月5日', weekday='星期三',
    subtitle='2026年8月5日 周三 · 费城半导体暴涨6.55%创年内最大单日涨幅·美股半导体全线爆发·央行5000亿逆回购净投放2000亿·存储芯片超级周期确认·A股科技高开',
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
    {"name":"道琼斯","change":"+1.71%","up":True},
    {"name":"标普500","change":"+1.79%","up":True},
    {"name":"纳斯达克","change":"+2.59%","up":True},
    {"name":"费城半导体","change":"+6.55%","up":True},
    {"name":"日经225","change":"-0.90%","up":False},
    {"name":"恒生指数","change":"-0.60%","up":False},
])
global_list1 = render_list([
    {"name":"WTI原油","change":"-6.47%/$75.38","up":False},
    {"name":"布伦特原油","change":"-6.00%/$79.03","up":False},
    {"name":"COMEX黄金","change":"-0.53%/$4130.43","up":False},
    {"name":"COMEX白银","change":"-0.90%/$59.70","up":False},
])
global_list2 = render_list([
    {"name":"三星电子","change":"+0.21%","up":True},
    {"name":"SK海力士","change":"+0.64%","up":True},
    {"name":"美光科技","change":"+7.62%","up":True},
    {"name":"闪迪(铠侠)","change":"+11.38%","up":True},
])
global_list3 = render_list([
    {"name":"英伟达","change":"+2.56%/$211.94","up":True},
    {"name":"AMD","change":"+7.00%/$518.58","up":True},
    {"name":"英特尔","change":"+10.84%/$100.86","up":True},
    {"name":"ARM","change":"+17.38%","up":True},
    {"name":"博通","change":"+6.61%/$418.16","up":True},
    {"name":"台积电ADR","change":"+2.72%/$417.17","up":True},
    {"name":"美光科技","change":"+7.62%/$892.67","up":True},
    {"name":"应用材料","change":"+5.48%/$546.62","up":True},
])
global_html = '''
<div class="grid md:grid-cols-3 gap-4">
  <div class="md:col-span-2">
    <div class="text-white font-semibold mb-3 flex items-center gap-2"><span>🌍</span><span>隔夜全球市场 · 费城半导体暴涨6.55%创年内最大单日涨幅·美股半导体全线爆发·油价暴跌</span></div>
    <div class="grid grid-cols-3 md:grid-cols-6 gap-2">{0}</div>
    <p class="text-xs text-white/50 mt-3 leading-relaxed">
      ⚡ <b class="text-yellow-400">核心要点：美股三大指数全线大涨创新高，费城半导体指数暴涨6.55%创年内最大单日涨幅，半导体全线爆发——ARM+17%、英特尔+10.84%、美光+7.62%、AMD+7%、闪迪+11%</b>——<br>
      ①<b>半导体超级反弹</b>：费城半导体指数单日涨6.55%，成分股几乎全红。ARM暴涨17.38%（AI边缘计算IP授权重估），英特尔涨10.84%（苹果代工传闻+盈利预期改善），美光涨7.62%（存储超级周期确认），AMD涨7%（财报前AI算力预期）。
      7月费城半导体指数累计下跌20.6%进入技术性熊市，8月初连续四日反弹属于超跌后的报复性修复。<br>
      ②<b>三大催化共振</b>：美伊霍尔木兹协议预期推动油价暴跌（WTI-6.47%）→ 通胀压力缓解→美联储降息预期升温；Palantir财报爆表（Q2营收+94%，上调全年指引至81.5亿）验证AI商业化落地；三星Q2利润暴增19倍确认存储超级周期基本面。<br>
      ③<b>存储超级周期确认</b>：闪迪+11.38%、美光+7.62%、SK海力士ADR+8%。三星/美光/SK海力士2027年DRAM和HBM产能已提前分配完毕，NAND产能8月底前分完。
      FMS 2026闪存峰会开幕，SK海力士+闪迪发布HBF（高带宽闪存）首个标准规范，AI推理新存储层级打开成长空间。<br>
      ④<b>油价暴跌利好成长股</b>：WTI原油单日跌6.47%至75.38美元，美伊谈判取得突破，霍尔木兹海峡可能重新开放。
      油价下跌缓解通胀压力，市场对美联储降息预期升温，成长股估值压力大幅缓解。<br>
      ⑤<b>亚太市场分化</b>：日经225跌0.9%、恒生指数跌0.6%，但韩国股市企稳（三星+0.21%、SK海力士+0.64%），杠杆风暴暂时缓解。
      港股科技股跟随美股盘后上涨。
    </p>
  </div>
  <div class="space-y-4">
    <div>
    <div class="text-white font-semibold mb-3 flex items-center gap-2"><span>🛢️</span><span>大宗商品</span></div>
      <div class="bg-white/5 rounded-lg p-3">{1}</div></div>
    <div>
    <div class="text-white font-semibold mb-3 flex items-center gap-2"><span>💾</span><span>存储双雄+韩股</span></div>
      <div class="bg-white/5 rounded-lg p-3">{2}</div></div>
    <div>
    <div class="text-white font-semibold mb-3 flex items-center gap-2"><span>💻</span><span>美股科技龙头</span></div>
      <div class="bg-white/5 rounded-lg p-3">{3}</div></div>
  </div>
</div>'''.format(global_cards1, global_list1, global_list2, global_list3)
gen.add_section("隔夜全球市场深度解读", global_html, "🌍")

# ========== 2. A股昨日复盘与今日展望 ==========
ashare_html = '''
<div class="space-y-4">
<div class="grid md:grid-cols-4 gap-3">
  <div class="bg-gradient-to-br from-red-500/20 to-orange-500/10 border border-red-500/30 rounded-xl p-3 text-center">
    <div class="text-xs text-white/60 mb-1">上证指数</div>
    <div class="text-xl font-bold text-red-400">3822.28</div>
    <div class="text-xs text-red-400">+0.33%</div>
  </div>
  <div class="bg-gradient-to-br from-red-500/20 to-orange-500/10 border border-red-500/30 rounded-xl p-3 text-center">
    <div class="text-xs text-white/60 mb-1">深证成指</div>
    <div class="text-xl font-bold text-red-400">13895.72</div>
    <div class="text-xs text-red-400">+3.25%</div>
  </div>
  <div class="bg-gradient-to-br from-red-500/20 to-orange-500/10 border border-red-500/30 rounded-xl p-3 text-center">
    <div class="text-xs text-white/60 mb-1">创业板指</div>
    <div class="text-xl font-bold text-red-400">3489.21</div>
    <div class="text-xs text-red-400">+5.64%</div>
  </div>
  <div class="bg-gradient-to-br from-red-500/20 to-orange-500/10 border border-red-500/30 rounded-xl p-3 text-center">
    <div class="text-xs text-white/60 mb-1">科创50</div>
    <div class="text-xl font-bold text-red-400">—</div>
    <div class="text-xs text-red-400">+4.09%</div>
  </div>
</div>

<div class="grid md:grid-cols-2 gap-4">
  <div class="bg-white/5 rounded-xl p-4">
    <h4 class="text-white font-semibold mb-3 flex items-center gap-2"><span>📈</span> 领涨板块</h4>
    <div class="space-y-1 text-xs">
      <div class="flex justify-between"><span class="text-white/70">CPO/光模块</span><span class="text-red-400">+8%~12%</span></div>
      <div class="flex justify-between"><span class="text-white/70">存储芯片</span><span class="text-red-400">+6%~10%</span></div>
      <div class="flex justify-between"><span class="text-white/70">半导体设备</span><span class="text-red-400">+5%~8%</span></div>
      <div class="flex justify-between"><span class="text-white/70">PCB/铜箔</span><span class="text-red-400">+4%~7%</span></div>
    </div>
  </div>
  <div class="bg-white/5 rounded-xl p-4">
    <h4 class="text-white font-semibold mb-3 flex items-center gap-2"><span>📉</span> 领跌/弱势板块</h4>
    <div class="space-y-1 text-xs">
      <div class="flex justify-between"><span class="text-white/70">银行/保险</span><span class="text-green-400">-1%~-2%</span></div>
      <div class="flex justify-between"><span class="text-white/70">煤炭/石油</span><span class="text-green-400">-1%~-2%</span></div>
      <div class="flex justify-between"><span class="text-white/70">白酒/消费</span><span class="text-green-400">-0.5%~-1%</span></div>
      <div class="flex justify-between"><span class="text-white/70">房地产</span><span class="text-green-400">-1%左右</span></div>
    </div>
  </div>
</div>

<div class="bg-white/5 rounded-xl p-4">
  <h4 class="text-white font-semibold mb-2 flex items-center gap-2"><span>💡</span> 盘面关键观察（8月4日）</h4>
  <div class="text-xs text-white/70 space-y-2 leading-relaxed">
    <p>① <b class="text-yellow-400">深强沪弱格局极致</b>：沪指仅+0.33%，但创业板指+5.64%、科创50+4.09%，两市成交2.21万亿放量2174亿。资金全面涌向科技成长，权重股被抽血。</p>
    <p>② <b class="text-yellow-400">CPO板块大面积涨停</b>：英伟达官宣CPO步入量产阶段，光库科技20CM涨停，中际旭创、新易盛等龙头大涨。AI算力硬件链全面爆发。</p>
    <p>③ <b class="text-yellow-400">存储芯片强势反弹</b>：万得存储器指数涨6.02%，25只个股涨幅超10%，澜起科技、佰维存储、江波龙、深科技等20CM涨停。FMS峰会+HBF标准催化。</p>
    <p>④ <b class="text-yellow-400">科创板成主战场</b>：科创板成交额占比显著提升，半导体/AI硬件成为资金主攻方向。兆易创新涨4.48%（前一日跌停），日内反包力度强。</p>
    <p>⑤ <b class="text-yellow-400">风格切换确认</b>：从电力/电网等防御性板块切回科技成长，CPO/存储/半导体设备成为新主线。但需注意：8月4日科技大涨是在8月3日暴跌后的反弹，不是新一轮上涨的起点。</p>
  </div>
</div>

<div class="bg-gradient-to-br from-blue-500/10 to-indigo-500/5 border border-blue-500/30 rounded-xl p-4">
  <h4 class="text-blue-300 font-semibold mb-2 flex items-center gap-2"><span>🔮</span> 今日展望（8月5日）</h4>
  <div class="text-xs text-white/70 space-y-2 leading-relaxed">
    <p>• <b class="text-yellow-400">开盘预判</b>：受美股半导体暴涨+央行放水双重利好，A股今日大幅高开，半导体/CPO/存储等科技板块高开3%-5%。</p>
    <p>• <b class="text-yellow-400">走势判断</b>：高开后大概率震荡分化，连续上涨后获利盘有兑现压力。关键看量能能否维持在2万亿以上。</p>
    <p>• <b class="text-yellow-400">操作建议</b>：<b>不追高</b>，等回踩再布局。8月4日已经大涨过的标的，8月5日高开后追涨风险大。</p>
    <p>• <b class="text-yellow-400">关注方向</b>：半导体设备（国产替代+AI算力扩产）、液冷/温控（英维克等）、先进封装材料（雅克科技等）、存储产业链（但需警惕追高）。</p>
  </div>
</div>
</div>'''
gen.add_section("A股昨日复盘与今日展望", ashare_html, "📊")

# ========== 3. 核心题材与今日催化 ==========
topic_html = '''
<div class="space-y-4">
  <!-- S级1：半导体超级反弹 -->
  <div class="bg-gradient-to-br from-red-500/10 to-orange-500/5 border border-red-500/30 rounded-xl p-4">
    <div class="flex items-center justify-between mb-3">
      <div class="flex items-center gap-2">
        <span class="bg-red-500 text-white text-xs px-2 py-0.5 rounded-full font-bold">S级</span>
        <span class="text-white font-semibold">费城半导体暴涨6.55% · 半导体全线爆发</span>
      </div>
      <span class="text-xs text-red-400">今日催化</span>
    </div>
    <div class="text-xs text-white/70 space-y-2 leading-relaxed">
      <p><b class="text-yellow-400">事件</b>：8月4日美股费城半导体指数暴涨6.55%，创年内最大单日涨幅。成分股几乎全红：
      ARM+17.38%、闪迪+11.38%、英特尔+10.84%、迈威尔科技+12%、Coherent+12%、美光+7.62%、AMD+7%、博通+6.61%。</p>
      <p><b class="text-yellow-400">三大催化共振</b>：
      ① 美伊霍尔木兹协议预期→油价暴跌→通胀压力缓解→降息预期升温；
      ② Palantir Q2营收+94%超预期，AI商业化标杆验证了AI基建投入的回报率；
      ③ 三星Q2利润暴增19倍，存储超级周期基本面确认。</p>
      <p><b class="text-yellow-400">对A股影响</b>：8月4日A股科技已大涨一波（创业板+5.64%、存储+6%、CPO大面积涨停），但8月4日白天收盘时还没吃到晚间美股这波主升浪。
      8月5日是A股第一次正面消化美股半导体暴涨6.55%的消息，预计高开幅度大。
      但注意：费城半导体已连续四日上涨，短期情绪过于亢奋，A股高开后低走风险需警惕。</p>
      <p><b class="text-yellow-400">A股映射方向</b>：
      芯原股份（ARM影子股）、海光信息（CPU/DCU国产替代）、兆易创新/江波龙（存储）、中际旭创（CPO）、北方华创/中微公司（设备）。</p>
    </div>
  </div>

  <!-- S级2：存储超级周期 -->
  <div class="bg-gradient-to-br from-red-500/10 to-orange-500/5 border border-red-500/30 rounded-xl p-4">
    <div class="flex items-center justify-between mb-3">
      <div class="flex items-center gap-2">
        <span class="bg-red-500 text-white text-xs px-2 py-0.5 rounded-full font-bold">S级</span>
        <span class="text-white font-semibold">FMS 2026闪存峰会 · HBF标准发布 · 存储超级周期确认</span>
      </div>
      <span class="text-xs text-red-400">进行中</span>
    </div>
    <div class="text-xs text-white/70 space-y-2 leading-relaxed">
      <p><b class="text-yellow-400">重磅消息</b>：
      ① SK海力士+闪迪联合发布HBF（高带宽闪存）首个标准规范，定义8层/16层NAND堆叠，最高512GB容量，带宽0.4~3.0TB/s，采用UCIe互联；
      ② 三星/美光/SK海力士2027年DRAM和HBM产能已提前分配完毕，NAND产能8月底前分完；
      ③ 全球存储芯片7月销售额达746亿美元创历史新高，连续三季度涨价；
      ④ 长鑫存储获75亿元增资，注册资本从238.88亿增至313.88亿，加速DRAM产能扩张。</p>
      <p><b class="text-yellow-400">HBF技术意义</b>：HBF是介于HBM和SSD之间的新型存储层级，面向AI推理场景下的KV缓存、大模型权重存储。
      闪迪预计首批产品2026下半年出样，2027年量产。HBF放量将拉动GMC塑封料、球形氧化铝填料、ALD前驱体等材料需求。</p>
      <p><b class="text-yellow-400">A股受益标的</b>：
      雅克科技（ALD前驱体，HBF制造必备材料，SK海力士核心供应商）、
      联瑞新材/壹石通（球形氧化铝填料）、
      江波龙/佰维存储（存储模组）、
      澜起科技（内存接口芯片）。</p>
    </div>
  </div>

  <!-- A级1：央行放水 -->
  <div class="bg-gradient-to-br from-yellow-500/10 to-amber-500/5 border border-yellow-500/30 rounded-xl p-4">
    <div class="flex items-center justify-between mb-3">
      <div class="flex items-center gap-2">
        <span class="bg-yellow-500/80 text-white text-xs px-2 py-0.5 rounded-full font-bold">A级</span>
        <span class="text-white font-semibold">央行5000亿买断式逆回购 · 净投放2000亿</span>
      </div>
      <span class="text-xs text-yellow-400">今日落地</span>
    </div>
    <div class="text-xs text-white/70 space-y-2 leading-relaxed">
      <p><b class="text-yellow-400">操作内容</b>：8月5日央行开展5000亿元3个月期买断式逆回购操作，当日到期3000亿元，<b>净投放2000亿元</b>中长期流动性。</p>
      <p><b class="text-yellow-400">市场解读</b>：央行在8月初加大中长期流动性投放，意在稳定银行体系流动性，支持实体经济融资。
      对A股资金面形成边际利好，有助于提升市场风险偏好。</p>
      <p><b class="text-yellow-400">对持仓影响</b>：流动性宽松利好成长股估值提升，科技股受益更直接。英维克、雅克科技等成长标的估值压力缓解。</p>
    </div>
  </div>

  <!-- A级2：集成电路布图设计条例修订 -->
  <div class="bg-gradient-to-br from-yellow-500/10 to-amber-500/5 border border-yellow-500/30 rounded-xl p-4">
    <div class="flex items-center justify-between mb-3">
      <div class="flex items-center gap-2">
        <span class="bg-yellow-500/80 text-white text-xs px-2 py-0.5 rounded-full font-bold">A级</span>
        <span class="text-white font-semibold">《集成电路布图设计保护条例》首次修订 · 10月15日施行</span>
      </div>
      <span class="text-xs text-yellow-400">政策催化</span>
    </div>
    <div class="text-xs text-white/70 space-y-2 leading-relaxed">
      <p><b class="text-yellow-400">核心内容</b>：国务院总理李强签署国务院令，公布修订后的《集成电路布图设计保护条例》，自2026年10月15日起施行。
      这是该条例2001年公布实施以来的首次修订，共6章54条，<b>加大侵权赔偿力度，引入惩罚性赔偿</b>。</p>
      <p><b class="text-yellow-400">产业意义</b>：标志着我国集成电路知识产权保护制度进一步完善，利好国内芯片设计公司的创新成果保护，
      长期推动国产芯片设计产业健康发展。</p>
    </div>
  </div>
</div>'''
gen.add_section("核心题材与今日催化", topic_html, "🔥")

# ========== 4. 持仓诊断 ==========
portfolio_html = '''
<div class="space-y-4">
  <!-- 英维克 -->
  <div class="bg-gradient-to-br from-blue-500/20 to-cyan-500/10 border border-blue-500/40 rounded-xl p-4">
    <div class="flex items-center justify-between mb-3">
      <div class="flex items-center gap-2">
        <span class="bg-blue-500 text-white text-xs px-2 py-0.5 rounded-full font-bold">持仓</span>
        <span class="text-white font-bold text-lg">英维克 (002837)</span>
      </div>
      <div class="text-right">
        <div class="text-xl font-bold text-red-400">约49.5元</div>
        <div class="text-xs text-red-400">8月4日随液冷板块上涨·美股科技暴涨催化</div>
      </div>
    </div>
    <div class="grid md:grid-cols-3 gap-3 text-xs">
      <div class="bg-white/5 rounded-lg p-3">
        <div class="text-white/60 mb-1">最新评级</div>
        <div class="text-blue-400 font-semibold">✅ 政策利好+产业趋势向上</div>
      </div>
      <div class="bg-white/5 rounded-lg p-3">
        <div class="text-white/60 mb-1">催化因素</div>
        <div class="text-white font-semibold">美股科技暴涨+液冷放量元年</div>
      </div>
      <div class="bg-white/5 rounded-lg p-3">
        <div class="text-white/60 mb-1">操作建议</div>
        <div class="text-white font-semibold">持有·逢低加仓</div>
      </div>
    </div>
    <div class="mt-3 text-xs text-white/70 leading-relaxed">
      <p><b class="text-yellow-400">📰 最新催化</b>：
      ① 美股科技股全线暴涨，AI算力硬件链情绪高涨；
      ② 液冷服务器概念8月4日震荡拉升，冰轮环境逼近涨停，英维克跟涨；
      ③ 中金公司预测2026年将迎来液冷放量元年，全球智算中心液冷市场规模将达1147亿元，同比增长273%；
      ④ 东吴证券研报：国产液冷已由送样验证进入批量交付阶段，英维克等头部企业形成端到端产品体系，部分产品通过英特尔测试、UQD系列进入NVIDIA MGX生态。</p>
      <p class="mt-2"><b class="text-yellow-400">💹 技术面</b>：8月4日随液冷板块上涨，成交量温和放大，45-50元区间震荡筑底中。
      如果今日能有效突破50元，有望打开上行空间；否则继续区间震荡。</p>
      <p class="mt-2"><b class="text-yellow-400">⚡ 操作策略</b>：
      ① 继续持有底仓，液冷放量元年逻辑不变；
      ② 若回调至44-46元区间可加仓，52-55元压力位附近可减仓做T；
      ③ 第一目标位55元（前期高点），第二目标位65元（AI液冷需求释放后估值修复）；
      ④ 止损位40元（跌破则趋势破坏）。</p>
    </div>
  </div>

  <!-- 雅克科技 -->
  <div class="bg-gradient-to-br from-amber-500/20 to-yellow-500/10 border border-amber-500/40 rounded-xl p-4">
    <div class="flex items-center justify-between mb-3">
      <div class="flex items-center gap-2">
        <span class="bg-amber-500 text-white text-xs px-2 py-0.5 rounded-full font-bold">持仓</span>
        <span class="text-white font-bold text-lg">雅克科技 (002409)</span>
      </div>
      <div class="text-right">
        <div class="text-xl font-bold text-red-400">约75-80元</div>
        <div class="text-xs text-red-400">8月4日反弹·存储板块+6%·HBF催化</div>
      </div>
    </div>
    <div class="grid md:grid-cols-3 gap-3 text-xs">
      <div class="bg-white/5 rounded-lg p-3">
        <div class="text-white/60 mb-1">最新评级</div>
        <div class="text-amber-400 font-semibold">⚠️ 反弹中·关注量能配合</div>
      </div>
      <div class="bg-white/5 rounded-lg p-3">
        <div class="text-white/60 mb-1">关键支撑/压力</div>
        <div class="text-white font-semibold">支撑65元/压力85元</div>
      </div>
      <div class="bg-white/5 rounded-lg p-3">
        <div class="text-white/60 mb-1">操作建议</div>
        <div class="text-white font-semibold">底仓持有·反弹减仓机动仓</div>
      </div>
    </div>
    <div class="mt-3 text-xs text-white/70 leading-relaxed">
      <p><b class="text-yellow-400">📰 最新催化</b>：
      ① 8月4日存储芯片板块大涨6.02%，雅克科技作为存储材料龙头跟随反弹；
      ② HBF（高带宽闪存）标准发布，雅克科技是ALD薄膜前驱体龙头，供应HBF制造中薄膜沉积环节必需的前驱体材料，SK海力士核心供应商；
      ③ 8月3日跌停板上机构+深股通合计净买入近5亿抄底，机构中长期看好；
      ④ 长鑫存储获75亿增资加速扩产，国产存储材料需求持续增长。</p>
      <p class="mt-2"><b class="text-yellow-400">📊 龙虎榜回顾</b>：8月3日跌停板上，机构净买入2.73亿+深股通净买入2.17亿=近5亿抄底。
      同日兆易创新机构净卖出8.08亿，一买一卖反差强烈——机构从设计端切向材料端。</p>
      <p class="mt-2"><b class="text-yellow-400">⚡ 操作策略</b>：
      ① 底仓30%继续持有，中长期逻辑未变；
      ② 如果今日反弹至80-85元区间，机动仓减仓做T降低成本（参考7月20日深度报告策略）；
      ③ 如果继续下探65-70元，可考虑小仓位加仓，但需控制仓位不超过总仓位15%；
      ④ 止损位下移至60元（跌破则趋势破坏）。</p>
    </div>
  </div>

  <!-- 铜冠铜箔 -->
  <div class="bg-gradient-to-br from-purple-500/20 to-pink-500/10 border border-purple-500/40 rounded-xl p-4">
    <div class="flex items-center justify-between mb-3">
      <div class="flex items-center gap-2">
        <span class="bg-purple-500 text-white text-xs px-2 py-0.5 rounded-full font-bold">持仓</span>
        <span class="text-white font-bold text-lg">铜冠铜箔 (301217)</span>
      </div>
      <div class="text-right">
        <div class="text-xl font-bold text-red-400">数据获取中</div>
        <div class="text-xs text-red-400">8月4日PCB/铜箔板块大涨</div>
      </div>
    </div>
    <div class="grid md:grid-cols-3 gap-3 text-xs">
      <div class="bg-white/5 rounded-lg p-3">
        <div class="text-white/60 mb-1">最新评级</div>
        <div class="text-purple-400 font-semibold">⏸️ 观望·关注中报</div>
      </div>
      <div class="bg-white/5 rounded-lg p-3">
        <div class="text-white/60 mb-1">关注因素</div>
        <div class="text-white font-semibold">AI服务器PCB+存储载板需求</div>
      </div>
      <div class="bg-white/5 rounded-lg p-3">
        <div class="text-white/60 mb-1">操作建议</div>
        <div class="text-white font-semibold">底仓持有·不加仓</div>
      </div>
    </div>
    <div class="mt-3 text-xs text-white/70 leading-relaxed">
      <p><b class="text-yellow-400">📰 最新动态</b>：
      ① 8月3日投资者关系平台确认：公司生产经营正常，订单充足，高频高速铜箔等高附加值订单供不应求；
      ② 2026年Q1整体毛利率8.79%，二季度环比增速为负引发市场担忧（公司回应正常经营）；
      ③ 2026半年报预约披露时间为8月27日，中报业绩是关键验证点；
      ④ 8月4日PCB/铜箔板块随AI算力硬件链大涨，铜冠铜箔跟随上涨。</p>
      <p class="mt-2"><b class="text-yellow-400">⚡ 操作策略</b>：底仓继续持有，不急于加仓。
      等8月27日中报业绩验证后再考虑是否加仓。
      短期关注AI服务器PCB需求能否传导至铜箔环节。</p>
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
        <div class="text-xl font-bold text-red-400">约10.5元</div>
        <div class="text-xs text-red-400">8月4日跟随大盘波动</div>
      </div>
    </div>
    <div class="bg-red-500/10 border border-red-500/30 rounded-lg p-3 mb-3">
      <p class="text-red-300 text-xs font-semibold">⚠️ 高风险警示：ST股退市风险极高，反弹就是减仓机会</p>
    </div>
    <div class="text-xs text-white/70 leading-relaxed">
      <p><b class="text-yellow-400">📰 最新动态</b>：*ST建艺继续在10元附近震荡，基本面没有改善迹象。
      一季报营收-35%，净利润亏损5311万，负债率94.38%，退市风险极高。</p>
      <p class="mt-2"><b class="text-yellow-400">⚡ 操作策略</b>：坚决执行减仓纪律。
      每一次反弹都是减仓机会，目标是尽快清仓，避免退市归零风险。
      10元以上分批减仓，不要抱有幻想。</p>
    </div>
  </div>
</div>'''
gen.add_section("持仓诊断与操作建议", portfolio_html, "💼")

# ========== 5. 空方视角 ==========
bear_html = '''
<div class="space-y-4">
  <div class="bg-red-500/10 border border-red-500/30 rounded-xl p-4">
    <h4 class="text-red-300 font-semibold mb-3 flex items-center gap-2"><span>🐻</span> 空方观点：报复性反弹后风险更大，追高必被套</h4>
    <div class="text-xs text-white/70 space-y-3 leading-relaxed">
      <div class="bg-white/5 rounded-lg p-3">
        <p class="text-red-300 font-semibold mb-1">风险1：连续四日上涨后情绪过于亢奋</p>
        <p>费城半导体指数已连续四日上涨，从底部反弹超过15%。8月4日单日暴涨6.55%后，
        市场情绪从极度悲观转向极度乐观，这种180度转弯往往意味着短期顶部临近。
        AMD盘后财报仅"略高于预期"就导致盘后跌8%，说明市场容错空间已经极小。</p>
      </div>
      <div class="bg-white/5 rounded-lg p-3">
        <p class="text-red-300 font-semibold mb-1">风险2：A股8月4日已大涨，8月5日高开后获利盘兑现压力大</p>
        <p>8月4日创业板已涨5.64%、存储+6%、CPO大面积涨停，A股科技板块已经提前涨了一波。
        8月5日高开后，8月4日抄底的资金有强烈的兑现欲望。
        "外围暴涨→A股高开→高开低走"这个剧本已经上演过无数次。</p>
      </div>
      <div class="bg-white/5 rounded-lg p-3">
        <p class="text-red-300 font-semibold mb-1">风险3：AMD盘后跌8%的警示信号</p>
        <p>AMD Q2营收同比增长50%、净利润增长246%，但盘后反而跌了8%——因为仅仅是"略高于预期"。
        当一家公司业绩增长246%都只能换来"略超预期"的评价时，说明市场期望值已经高到了任何不完美都会被惩罚的程度。
        这是典型的股价见顶信号。</p>
      </div>
      <div class="bg-white/5 rounded-lg p-3">
        <p class="text-red-300 font-semibold mb-1">风险4：韩股杠杆风险尚未完全解除</p>
        <p>韩国股市虽然8月4日小幅企稳，但高盛警告仍有超1000亿美元高杠杆芯片多头头寸悬而未决。
        如果美股科技股再次下跌，韩股可能触发新一轮强制平仓，形成负反馈螺旋。
        韩股的杠杆风暴对A股半导体有直接传导效应。</p>
      </div>
      <div class="bg-white/5 rounded-lg p-3">
        <p class="text-red-300 font-semibold mb-1">风险5：中报密集披露期临近，业绩雷可能集中爆发</p>
        <p>8月中下旬是中报密集披露期，部分科技公司业绩可能不及预期。
        当前市场情绪高涨，一旦业绩不及预期，股价可能出现剧烈调整。
        持仓中的铜冠铜箔（8月27日披露）需特别关注。</p>
      </div>
    </div>
  </div>

  <div class="bg-green-500/10 border border-green-500/30 rounded-xl p-4">
    <h4 class="text-green-300 font-semibold mb-3 flex items-center gap-2"><span>🐂</span> 多方反驳：AI周期才刚进入加速期，回调都是买入机会</h4>
    <div class="text-xs text-white/70 space-y-2 leading-relaxed">
      <p>① <b>AI算力需求才是真正的基本面</b>：全球Top5云服务巨头2026年合计资本开支预计突破6000亿美元，
      谷歌上调至1950-2050亿美元。AI基础设施建设才刚开始，半导体周期远未见顶。
      Palantir+94%的营收增长验证了AI商业化正在加速落地。</p>
      <p>② <b>存储超级周期确认，涨价持续到2027年</b>：三星Q2利润暴增19倍，三大原厂产能已分配至2027年。
      HBM、DDR5、HBF多线驱动，存储行业景气度将持续超预期。
      7月全球存储芯片销售额746亿美元创历史新高。</p>
      <p>③ <b>7月调整是健康的回调，不是趋势反转</b>：费城半导体指数7月跌20%，属于牛市中期正常调整。
      调整后估值更合理，资金重新进场。8月以来的反弹是趋势恢复，不是反弹出货。</p>
      <p>④ <b>国产替代加速，A股半导体有独立行情</b>：长鑫存储75亿增资、
      集成电路布图设计保护条例修订、国产设备材料渗透率持续提升。
      A股半导体不完全跟随海外，有自己的产业逻辑和政策支撑。</p>
    </div>
  </div>
</div>'''
gen.add_section("空方视角 vs 多方反驳", bear_html, "⚖️")

# ========== 6. 今日操作策略 ==========
strategy_html = '''
<div class="space-y-4">
  <div class="bg-gradient-to-br from-blue-500/20 to-indigo-500/10 border border-blue-500/30 rounded-xl p-4">
    <h4 class="text-white font-semibold mb-3 flex items-center gap-2"><span>🎯</span> 今日操作总策略</h4>
    <div class="text-sm text-white/80 leading-relaxed">
      <p class="mb-2">美股半导体暴涨6.55%+央行放水2000亿，双重利好下今日<b class="text-yellow-400">高开是必然，但高开不追高</b>。
      8月4日A股科技已大涨一波，8月5日属于"二次发酵"，追涨风险大于收益。
      重点观察：半导体板块高开后的承接力度，以及量能能否维持在2万亿以上。</p>
      <p><b class="text-yellow-400">核心思路</b>：
      不追高、等回踩；有业绩的跌下来敢买，没业绩的涨起来要卖；
      持仓以"持有为主+机动仓做T"策略应对震荡。</p>
    </div>
  </div>

  <div class="grid md:grid-cols-2 gap-4">
    <div class="bg-white/5 rounded-xl p-4">
      <h4 class="text-green-400 font-semibold mb-3 text-sm">✅ 可以做的</h4>
      <div class="text-xs text-white/70 space-y-2">
        <p>• 英维克回调至44-46元区间可加仓，持有待涨</p>
        <p>• 雅克科技反弹至80-85元区间，机动仓减仓做T</p>
        <p>• 关注半导体设备板块的国产替代机会（中微公司、北方华创等）</p>
        <p>• 关注HBF新材料方向（雅克科技、联瑞新材等）</p>
        <p>• 液冷板块调整到位后可加仓（产业趋势明确）</p>
        <p>• 中报超预期的品种回调即是买点</p>
      </div>
    </div>
    <div class="bg-white/5 rounded-xl p-4">
      <h4 class="text-red-400 font-semibold mb-3 text-sm">❌ 不要做的</h4>
      <div class="text-xs text-white/70 space-y-2">
        <p>• 不要因为美股暴涨就追高A股半导体，情绪只影响开盘</p>
        <p>• 不要追高CPO/存储等8月4日已经大涨的板块</p>
        <p>• 不要重仓单一个股，保持仓位分散</p>
        <p>• *ST建艺反弹要减仓，不要加仓ST股</p>
        <p>• 不要在高开时冲动买入，等30分钟看承接力度</p>
        <p>• 不要因为连续上涨就放松风控，止损纪律必须严格执行</p>
      </div>
    </div>
  </div>

  <div class="bg-white/5 rounded-xl p-4">
    <h4 class="text-white font-semibold mb-3 flex items-center gap-2"><span>📋</span> 今日关注事件时间表</h4>
    <div class="grid md:grid-cols-2 gap-3 text-xs text-white/70">
      <div>
        <p><b class="text-yellow-400">09:30</b> A股开盘，观察半导体高开幅度和承接力度</p>
        <p><b class="text-yellow-400">10:30</b> 中国气象局8月新闻发布会</p>
        <p><b class="text-yellow-400">全天</b> FMS 2026闪存峰会（美国硅谷，夜间还有演讲）</p>
        <p><b class="text-yellow-400">全天</b> 中报密集披露期</p>
      </div>
      <div>
        <p><b class="text-yellow-400">20:30</b> 美国6月贸易帐、加拿大6月贸易帐</p>
        <p><b class="text-yellow-400">22:00</b> 美国JOLTS职位空缺、工厂订单</p>
        <p><b class="text-yellow-400">盘后</b> 美光财报（已发布，Q3超预期）</p>
        <p><b class="text-yellow-400">凌晨</b> 美联储官员讲话（关注降息信号）</p>
      </div>
    </div>
  </div>

  <div class="bg-amber-500/10 border border-amber-500/30 rounded-xl p-4">
    <h4 class="text-amber-300 font-semibold mb-2 flex items-center gap-2"><span>⚠️</span> 特别警示</h4>
    <div class="text-xs text-white/70 space-y-1">
      <p>• AMD盘后财报仅"略超预期"就跌8%，说明AI股估值已高，容错空间极小</p>
      <p>• 费城半导体已连涨四日，短期超买严重，回调风险累积</p>
      <p>• A股8月4日已大涨，8月5日高开后追高被套概率大</p>
      <p>• 仓位管理：总仓位建议控制在60%-70%，保留现金应对波动</p>
    </div>
  </div>
</div>'''
gen.add_section("今日操作策略与关注重点", strategy_html, "🎯")

# ========== 7. 预判验证闭环 ==========
prediction_html = '''
<div class="space-y-4">
  <div class="bg-white/5 rounded-xl p-4">
    <h4 class="text-white font-semibold mb-3 flex items-center gap-2"><span>📝</span> 历史预判验证</h4>
    <div class="space-y-3">
      <div class="bg-green-500/10 border border-green-500/30 rounded-lg p-3">
        <div class="flex items-center justify-between mb-1">
          <span class="text-green-400 font-semibold">✅ T+1验证：8月开门震荡分化（8/3预判）</span>
          <span class="text-white/50 text-xs">验证完成</span>
        </div>
        <p class="text-white/60 text-xs">
          8月3日预判"8月开门红但创业板继续弱势，结构性分化"，实际8月3日沪指-0.59%、创业板-1.24%、科创50-5.08%，
          电力/电网板块大涨、半导体板块大跌——分化格局完全符合预期。
          <b class="text-yellow-400">评级：正确</b>。
        </p>
      </div>
      <div class="bg-green-500/10 border border-green-500/30 rounded-lg p-3">
        <div class="flex items-center justify-between mb-1">
          <span class="text-green-400 font-semibold">✅ T+1验证：雅克科技跌停后机构抄底（8/4预判）</span>
          <span class="text-white/50 text-xs">验证完成</span>
        </div>
        <p class="text-white/60 text-xs">
          8月3日预判"雅克科技在机构抄底支撑下可能止跌企稳"，实际8月4日雅克科技跟随存储板块反弹（存储指数+6%），
          机构抄底的支撑作用确实体现。
          <b class="text-yellow-400">评级：正确</b>。
        </p>
      </div>
      <div class="bg-amber-500/10 border border-amber-500/30 rounded-lg p-3">
        <div class="flex items-center justify-between mb-1">
          <span class="text-amber-400 font-semibold">⏳ T+3验证：液冷板块政策催化后反弹（7/31预判）</span>
          <span class="text-white/50 text-xs">验证中</span>
        </div>
        <p class="text-white/60 text-xs">
          7月31日预判"液冷板块超跌后可能迎来政策催化反弹"，
          发改委算力网政策+十五五电力规划双重催化已落地，
          8月4日液冷服务器概念拉升，英维克跟涨。观察能否持续走强。
        </p>
      </div>
      <div class="bg-red-500/10 border border-red-500/30 rounded-lg p-3">
        <div class="flex items-center justify-between mb-1">
          <span class="text-red-400 font-semibold">❌ T+1验证：半导体高开低走（8/4预判）</span>
          <span class="text-white/50 text-xs">验证失败</span>
        </div>
        <p class="text-white/60 text-xs">
          8月4日预判"半导体板块高开低走概率大"，实际8月4日半导体板块全天强势（存储+6%、CPO涨停潮），
          预判错误——低估了CPO量产消息的催化力度和存储板块的反弹力度。
          <b class="text-yellow-400">教训</b>：板块连续暴跌后的首次反弹，力度往往超出预期，不要轻易判断"高开低走"。
        </p>
      </div>
    </div>
  </div>

  <div class="bg-white/5 rounded-xl p-4">
    <h4 class="text-white font-semibold mb-2 flex items-center gap-2">
      <span>🔮</span> 今日预判（8/5）
    </h4>
    <div class="text-xs text-white/70 space-y-2">
      <p><b class="text-yellow-400">预判1：</b>受美股半导体暴涨6.55%+央行放水双重利好，A股今日大幅高开（沪指+1%左右、创业板+2%-3%），
      但高开后大概率震荡回落收上影线，全天呈现"高开低走"或"高开震荡"格局</p>
      <p><b class="text-yellow-400">预判2：</b>半导体板块高开后分化严重，设备/材料端强于设计端，
      HBF相关的存储材料标的（雅克科技等）表现优于纯存储设计标的</p>
      <p><b class="text-yellow-400">预判3：</b>英维克等液冷龙头今日表现强于大盘，
      在AI算力+电力规划双重催化下，有望走出独立行情</p>
      <p><b class="text-yellow-400">预判4：</b>两市成交额维持在2万亿以上，
      但增量资金主要集中在科技成长方向，权重股继续被抽血（深强沪弱格局延续）</p>
    </div>
    <p class="text-white/40 text-xs mt-3">⚠️ 预判仅供参考，不构成投资建议，T+1/T+2验证后更新准确率</p>
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
    <p class="text-yellow-300 font-semibold mb-1">教训#3：连续上涨后追高风险极大</p>
    <p class="text-white/60 text-xs">
      费城半导体指数已经连续四日上涨，从底部反弹超过15%。
      当所有人都在喊"牛市回来了"的时候，往往就是短期顶部。
      AMD盘后业绩增长246%却跌8%，就是典型的"利好出尽"。
      <b>正确做法</b>：连续上涨后不追高，等回调再进场。
      宁可错过，不要做错。
    </p>
  </div>

  <div class="bg-green-500/10 border border-green-500/30 rounded-lg p-3">
    <p class="text-green-300 font-semibold mb-1">教训#4：机构跌停板抄底≠马上反转</p>
    <p class="text-white/60 text-xs">
      雅克科技跌停机构抄底近5亿，这是中长期看好的信号，但不等于股价马上就会涨。
      机构建仓是一个过程，可能会继续砸盘吸筹，也可能横盘很久。
      <b>正确做法</b>：机构抄底可以作为中长期看好的佐证，
      但短期操作还是要看技术面和情绪面，不要因为机构买了就盲目抄底。
      分批建仓、控制仓位、设置止损，一样都不能少。
    </p>
  </div>

  <div class="bg-purple-500/10 border border-purple-500/30 rounded-lg p-3">
    <p class="text-purple-300 font-semibold mb-1">教训#5：存储不只有DRAM涨价一条逻辑</p>
    <p class="text-white/60 text-xs">
      市场把存储等同于DRAM涨价，一旦DRAM涨价放缓就觉得存储周期见顶了。
      但实际上存储行业有很多细分方向：HBM、NAND、HBF、端侧AI存储、企业级SSD……
      每一条线都有自己的周期和节奏。
      <b>正确做法</b>：不要用单一指标判断整个行业，
      要深入细分赛道找真正的增长点。当前HBF标准发布、端侧AI存储爆发，
      都是存储行业内部的新机会。
    </p>
  </div>

  <div class="bg-cyan-500/10 border border-cyan-500/30 rounded-lg p-3">
    <p class="text-cyan-300 font-semibold mb-1">教训#6：AMD盘后跌8%的启示——AI股容错空间极小</p>
    <p class="text-white/60 text-xs">
      AMD Q2营收+50%、净利润+246%，仅仅是"略高于预期"就导致盘后跌8%。
      这说明AI概念股的估值已经充分甚至过度反映了乐观预期，
      任何一点点"不够好"都会被市场放大解读。
      <b>正确做法</b>：对高估值的AI概念股保持谨慎，
      不要在业绩发布前重仓押注。
      优先选择估值合理、业绩确定性高的标的。
    </p>
  </div>
</div>'''
gen.add_section("教训库引用", lesson_html, "📚")

# ========== 生成+发布 ==========
output_path = os.path.join(WORK_DIR, 'docs/daily/20260805_每日新闻洞察.html')
result = gen.publish(output_path=output_path)
print("发布结果:", result)
print("成功:", result.get('success', False))
print("报告路径:", output_path)
print("文件大小:", os.path.getsize(output_path), "字节")

# 更新 latest.html
latest_path = os.path.join(WORK_DIR, 'docs/daily/latest.html')
shutil.copy2(output_path, latest_path)
print("latest.html 已更新")
