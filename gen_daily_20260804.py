#!/usr/bin/env python3
"""2026年8月4日 每日新闻洞察生成 - 周二·韩股杠杆风暴二次发酵·FMS闪存峰会开幕·美股科技普涨A股分化·持仓雅克跌停机构抄底"""
import sys, os, shutil, json
WORK_DIR = '/app/data/所有对话/主对话'
sys.path.insert(0, os.path.join(WORK_DIR, 'v3'))
from generators.daily_pro import DailyReportProGenerator

gen = DailyReportProGenerator(
    date_str='2026年8月4日', weekday='星期二',
    subtitle='2026年8月4日 周二 · 韩股杠杆风暴二次发酵·三星SK双双跌近9%·FMS闪存峰会开幕HBF标准发布·美股科技普涨纳指+2.13%·雅克科技跌停机构抄底近5亿',
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
    {"name":"道琼斯","change":"+1.32%","up":True},
    {"name":"标普500","change":"+1.48%","up":True},
    {"name":"纳斯达克","change":"+2.13%","up":True},
    {"name":"费城半导体","change":"+1.05%","up":True},
    {"name":"韩国KOSPI","change":"-5.12%","up":False},
    {"name":"恒生指数","change":"+0.48%","up":True},
])
global_list1 = render_list([
    {"name":"WTI原油","change":"-5.11%/$80.71","up":False},
    {"name":"布伦特原油","change":"-4.73%/$84.25","up":False},
    {"name":"COMEX黄金","change":"+0.64%/$4116.54","up":True},
    {"name":"COMEX白银","change":"+1.23%/$58.57","up":True},
])
global_list2 = render_list([
    {"name":"三星电子","change":"-8.76%","up":False},
    {"name":"SK海力士","change":"-8.79%","up":False},
    {"name":"美光科技","change":"+0.79%","up":True},
    {"name":"铠侠ADR","change":"+14%","up":True},
])
global_list3 = render_list([
    {"name":"英伟达","change":"+2.93%/$206.64","up":True},
    {"name":"微软","change":"+4.93%/$487.65","up":True},
    {"name":"Meta","change":"+6.02%/$590.24","up":True},
    {"name":"AMD","change":"+1.78%/$484.64","up":True},
    {"name":"博通","change":"+0.76%/$392.23","up":True},
    {"name":"台积电ADR","change":"+0.46%/$406.11","up":True},
    {"name":"苹果","change":"-1.78%/$303.42","up":False},
    {"name":"应用材料","change":"+2.08%/$518.21","up":True},
])
global_html = '''
<div class="grid md:grid-cols-3 gap-4">
  <div class="md:col-span-2">
    <div class="text-white font-semibold mb-3 flex items-center gap-2"><span>🌍</span><span>隔夜全球市场 · 美股科技大爆发纳指+2.13%·韩股杠杆风暴二次发酵·原油暴跌黄金反弹</span></div>
    <div class="grid grid-cols-3 md:grid-cols-6 gap-2">{0}</div>
    <p class="text-xs text-white/50 mt-3 leading-relaxed">
      ⚡ <b class="text-yellow-400">核心要点：美股三大指数全线大涨，纳斯达克领涨2.13%创阶段新高；但韩国KOSPI暴跌5.12%，三星/SK海力士双双跌近9%，杠杆ETF负反馈再现</b>——<br>
      ①<b>美股科技普涨</b>：Meta+6%、微软+4.93%（财报超预期）、谷歌+4.88%、亚马逊+4.58%市值首破3万亿，英伟达+2.93%重回5万亿市值。
      七巨头仅苹果收跌-1.78%（两日累跌9%）。空头回补+财报超预期双重驱动。<br>
      ②<b>韩股杠杆风暴2.0</b>：KOSPI暴跌5.12%，三星电子-8.76%、SK海力士-8.79%，韩国交易所启动"边车机制"暂停程序化交易5分钟。
      上周五暴涨18%后周一暴跌，杠杆ETF负反馈螺旋再现——外资一日狂买创纪录、次日反手就抛。<br>
      ③<b>存储板块冰火分化</b>：DRAM方向的三星/SK海力士暴跌，但NAND方向的铠侠ADR+14%（回购+拆股+AI NAND预期），美光盘中V型反转从-6%收涨0.79%。
      市场开始区分DRAM和NAND的景气差异。<br>
      ④<b>原油暴跌黄金反弹</b>：WTI原油-5.11%至80.7美元（美伊谈判缓和+霍尔木兹海峡可能重开），黄金+0.64%至4116美元（避险需求+美元走弱）。<br>
      ⑤<b>对冲基金大抄底</b>：高盛交易台录得2020年11月以来最大单周净买入，几乎全部由空头回补驱动。
      但高盛同时警告：仍有超1000亿美元高杠杆芯片多头头寸悬而未决，强制平仓风险未完全消散。
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
  <div class="bg-gradient-to-br from-green-500/20 to-emerald-500/10 border border-green-500/30 rounded-xl p-3 text-center">
    <div class="text-xs text-white/60 mb-1">上证指数</div>
    <div class="text-xl font-bold text-green-400">3809.66</div>
    <div class="text-xs text-green-400">-0.59%</div>
  </div>
  <div class="bg-gradient-to-br from-green-500/20 to-emerald-500/10 border border-green-500/30 rounded-xl p-3 text-center">
    <div class="text-xs text-white/60 mb-1">深证成指</div>
    <div class="text-xl font-bold text-green-400">13448.29</div>
    <div class="text-xs text-green-400">-0.96%</div>
  </div>
  <div class="bg-gradient-to-br from-green-500/20 to-emerald-500/10 border border-green-500/30 rounded-xl p-3 text-center">
    <div class="text-xs text-white/60 mb-1">创业板指</div>
    <div class="text-xl font-bold text-green-400">3302.55</div>
    <div class="text-xs text-green-400">-1.24%</div>
  </div>
  <div class="bg-gradient-to-br from-green-500/20 to-emerald-500/10 border border-green-500/30 rounded-xl p-3 text-center">
    <div class="text-xs text-white/60 mb-1">科创50</div>
    <div class="text-xl font-bold text-green-400">—</div>
    <div class="text-xs text-green-400">-5.08%</div>
  </div>
</div>

<div class="grid md:grid-cols-2 gap-4">
  <div class="bg-white/5 rounded-xl p-4">
    <h4 class="text-white font-semibold mb-3 flex items-center gap-2"><span>📉</span> 领跌板块</h4>
    <div class="space-y-1 text-xs">
      <div class="flex justify-between"><span class="text-white/70">半导体材料</span><span class="text-green-400">—4%~6%</span></div>
      <div class="flex justify-between"><span class="text-white/70">存储芯片</span><span class="text-green-400">—3%~5%</span></div>
      <div class="flex justify-between"><span class="text-white/70">电子化学品</span><span class="text-green-400">—3%~5%</span></div>
      <div class="flex justify-between"><span class="text-white/70">光刻胶</span><span class="text-green-400">—3%~4%</span></div>
    </div>
  </div>
  <div class="bg-white/5 rounded-xl p-4">
    <h4 class="text-white font-semibold mb-3 flex items-center gap-2"><span>📈</span> 领涨板块</h4>
    <div class="space-y-1 text-xs">
      <div class="flex justify-between"><span class="text-white/70">核电/电网设备</span><span class="text-red-400">+3%~5%</span></div>
      <div class="flex justify-between"><span class="text-white/70">风电设备</span><span class="text-red-400">+2%~4%</span></div>
      <div class="flex justify-between"><span class="text-white/70">环保设备</span><span class="text-red-400">+2%~3%</span></div>
      <div class="flex justify-between"><span class="text-white/70">创新药</span><span class="text-red-400">+1%~2%</span></div>
    </div>
  </div>
</div>

<div class="bg-white/5 rounded-xl p-4">
  <h4 class="text-white font-semibold mb-2 flex items-center gap-2"><span>💡</span> 盘面关键观察</h4>
  <div class="text-xs text-white/70 space-y-2 leading-relaxed">
    <p>① <b class="text-yellow-400">缩量回调</b>：两市成交额约2.01万亿元，较前一交易日减少5488亿元，缩量回调≠恐慌出逃，资金在等中报答案。</p>
    <p>② <b class="text-yellow-400">83股涨停vs超4000只个股上涨</b>：指数跌但个股涨多跌少，市场从指数行情转向结构性行情，电力/电网/环保等低位板块接力。</p>
    <p>③ <b class="text-yellow-400">科创50暴跌5.08%</b>：再创本轮调整新低，兆易创新跌停，半导体产业链集体下挫，韩股暴跌传导效应明显。</p>
    <p>④ <b class="text-yellow-400">雅克科技跌停但机构抄底</b>：龙虎榜显示机构净买入2.73亿+深股通净买入2.17亿=合计近5亿抄底，跌停板上内外资机构联手接货。</p>
    <p>⑤ <b class="text-yellow-400">兆易创新跌停机构卖出8亿</b>：与雅克科技形成鲜明对比，机构对半导体内部的分化判断加剧——材料端被看好，设计端被抛弃。</p>
  </div>
</div>
</div>'''
gen.add_section("A股昨日复盘与今日展望", ashare_html, "📊")

# ========== 3. 核心题材与催化 ==========
topic_html = '''
<div class="space-y-4">
  <!-- S级1：存储芯片/闪存峰会 -->
  <div class="bg-gradient-to-br from-red-500/10 to-orange-500/5 border border-red-500/30 rounded-xl p-4">
    <div class="flex items-center justify-between mb-3">
      <div class="flex items-center gap-2">
        <span class="bg-red-500 text-white text-xs px-2 py-0.5 rounded-full font-bold">S级</span>
        <span class="text-white font-semibold">FMS 2026闪存峰会开幕 · HBF标准发布</span>
      </div>
      <span class="text-xs text-red-400">今日催化</span>
    </div>
    <div class="text-xs text-white/70 space-y-2 leading-relaxed">
      <p><b class="text-yellow-400">事件</b>：FMS 2026闪存峰会8月4-6日在美国硅谷开幕，三星、SK海力士、美光、铠侠等存储巨头悉数出席。</p>
      <p><b class="text-yellow-400">重磅发布</b>：SK海力士+闪迪联合发布HBF（高带宽闪存）首个标准规范——由OCP正式发布为行业通用开放标准。
      定义8层/16层NAND堆叠，最高512GB容量，带宽0.4~3.0TB/s，采用UCIe互联标准。HBF联盟已汇聚谷歌与Tenstorrent。</p>
      <p><b class="text-yellow-400">价格指引</b>：市场预期原厂将公布Q3-Q4 DRAM/NAND价格预期，DRAM Q3+13%~18%、NAND+10%~15%（涨幅收敛但高位延续）。</p>
      <p><b class="text-yellow-400">技术看点</b>：SK海力士将首次展示第十代(V10)375层4D NAND，性能功耗比提升2.5倍，明年初量产企业级SSD。
      三星将发布HBM4E和下一代V-NAND路线图。</p>
      <p><b class="text-yellow-400">对A股影响</b>：短期看韩股暴跌拖累情绪，但中期看存储景气周期仍在（涨价+AI需求+HBF新技术），
      回调后优质标的反而提供布局机会。关注：江波龙（端侧AI存储）、雅克科技（存储材料）、华海诚科（先进封装材料）。</p>
    </div>
  </div>

  <!-- A级1：电力系统十五五规划 -->
  <div class="bg-gradient-to-br from-yellow-500/10 to-amber-500/5 border border-yellow-500/30 rounded-xl p-4">
    <div class="flex items-center justify-between mb-3">
      <div class="flex items-center gap-2">
        <span class="bg-yellow-500/80 text-white text-xs px-2 py-0.5 rounded-full font-bold">A级</span>
        <span class="text-white font-semibold">新型电力系统建设"十五五"规划出炉</span>
      </div>
      <span class="text-xs text-yellow-400">政策催化</span>
    </div>
    <div class="text-xs text-white/70 space-y-2 leading-relaxed">
      <p><b class="text-yellow-400">核心目标</b>：到2030年新型电力系统初步建成，非化石能源发电量占比提升，新能源利用率锚定90%，实现28亿千瓦以上新能源高水平消纳。</p>
      <p><b class="text-yellow-400">关键方向</b>：煤电灵活性改造"应改尽改"、大规模建设抽水蓄能和新型储能、发展虚拟电厂与车网融合、全国统一电力市场、AI赋能电力与算力协同。</p>
      <p><b class="text-yellow-400">对持仓影响</b>：英维克（液冷温控）直接受益于"电力与算力协同融合"的政策导向，AI数据中心液冷需求与电网建设形成共振。</p>
    </div>
  </div>

  <!-- A级2：AI应用/中报业绩 -->
  <div class="bg-gradient-to-br from-yellow-500/10 to-amber-500/5 border border-yellow-500/30 rounded-xl p-4">
    <div class="flex items-center justify-between mb-3">
      <div class="flex items-center gap-2">
        <span class="bg-yellow-500/80 text-white text-xs px-2 py-0.5 rounded-full font-bold">A级</span>
        <span class="text-white font-semibold">中报业绩进入密集披露期 · 分化加剧</span>
      </div>
      <span class="text-xs text-yellow-400">进行中</span>
    </div>
    <div class="text-xs text-white/70 space-y-2 leading-relaxed">
      <p><b class="text-yellow-400">超预期</b>：药明康德（中报+29%，上调全年指引至+35~39%）、中微公司（中报+282%~311%，设备业务高增）、
      行云科技（154亿长单，订单全面进入加价期）。</p>
      <p><b class="text-yellow-400">不及预期</b>：部分半导体设计公司、消费电子链公司业绩承压，兆易创新跌停机构卖出8亿。</p>
      <p><b class="text-yellow-400">市场逻辑</b>：从"炒概念"转向"看业绩"，有真业绩的公司跌下来有机构接，纯题材股反弹后继续跌。
      持仓中雅克科技跌停机构抄底就是典型信号——机构看好其半导体材料的中长期价值。</p>
    </div>
  </div>
</div>'''
gen.add_section("核心题材与今日催化", topic_html, "🔥")

# ========== 4. 持仓诊断 ==========
portfolio_html = '''
<div class="space-y-4">
  <!-- 雅克科技 -->
  <div class="bg-gradient-to-br from-amber-500/20 to-yellow-500/10 border border-amber-500/40 rounded-xl p-4">
    <div class="flex items-center justify-between mb-3">
      <div class="flex items-center gap-2">
        <span class="bg-amber-500 text-white text-xs px-2 py-0.5 rounded-full font-bold">持仓</span>
        <span class="text-white font-bold text-lg">雅克科技 (002409)</span>
      </div>
      <div class="text-right">
        <div class="text-xl font-bold text-green-400">68.98 → 120.91</div>
        <div class="text-xs text-green-400">8月3日跌9.63%·龙虎榜机构+深股通净买入近5亿</div>
      </div>
    </div>
    <div class="grid md:grid-cols-3 gap-3 text-xs">
      <div class="bg-white/5 rounded-lg p-3">
        <div class="text-white/60 mb-1">最新评级</div>
        <div class="text-amber-400 font-semibold">⚠️ 短期承压·中长期看好</div>
      </div>
      <div class="bg-white/5 rounded-lg p-3">
        <div class="text-white/60 mb-1">关键支撑位</div>
        <div class="text-white font-semibold">60元（前低）/ 65元（心理位）</div>
      </div>
      <div class="bg-white/5 rounded-lg p-3">
        <div class="text-white/60 mb-1">操作建议</div>
        <div class="text-white font-semibold">底仓持有·反弹减仓机动仓</div>
      </div>
    </div>
    <div class="mt-3 text-xs text-white/70 leading-relaxed">
      <p><b class="text-yellow-400">📊 龙虎榜深度解读</b>：8月3日跌停板上，5家机构席位合计买入5.84亿、卖出3.11亿，<b>机构净买入2.73亿</b>；
      深股通买入4.05亿、卖出1.88亿，<b>北向净买入2.17亿</b>。内外资机构合计净买入近5亿元抄底。
      同日兆易创新机构净卖出8.08亿，一买一卖反差强烈——机构在半导体内部做了剧烈的调仓，从设计端切向材料端。</p>
      <p class="mt-2"><b class="text-yellow-400">🎯 核心逻辑</b>：雅克科技是A股唯一同时布局光刻胶+电子特气+前驱体+LDS输送系统的半导体材料平台型公司，
      深度受益于国内晶圆厂扩产+国产替代加速。短期受板块情绪拖累下跌，但机构用真金白银表达了对中长期价值的认可。</p>
      <p class="mt-2"><b class="text-yellow-400">⚡ 操作策略</b>：
      ① 底仓30%继续持有，中长期逻辑未变；
      ② 如果今日继续下探60-65元区间，可考虑小仓位（10%）左侧加仓；
      ③ 如果反弹至80-85元，机动仓减仓做T降低成本；
      ④ 止损位下移至55元（跌破则趋势破坏）。</p>
    </div>
  </div>

  <!-- 英维克 -->
  <div class="bg-gradient-to-br from-blue-500/20 to-cyan-500/10 border border-blue-500/40 rounded-xl p-4">
    <div class="flex items-center justify-between mb-3">
      <div class="flex items-center gap-2">
        <span class="bg-blue-500 text-white text-xs px-2 py-0.5 rounded-full font-bold">持仓</span>
        <span class="text-white font-bold text-lg">英维克 (002837)</span>
      </div>
      <div class="text-right">
        <div class="text-xl font-bold text-green-400">46.45元</div>
        <div class="text-xs text-green-400">8月3日跌1.00%·电力规划利好</div>
      </div>
    </div>
    <div class="grid md:grid-cols-3 gap-3 text-xs">
      <div class="bg-white/5 rounded-lg p-3">
        <div class="text-white/60 mb-1">最新评级</div>
        <div class="text-blue-400 font-semibold">✅ 政策利好+业绩驱动</div>
      </div>
      <div class="bg-white/5 rounded-lg p-3">
        <div class="text-white/60 mb-1">催化因素</div>
        <div class="text-white font-semibold">十五五电力规划+FMS峰会</div>
      </div>
      <div class="bg-white/5 rounded-lg p-3">
        <div class="text-white/60 mb-1">操作建议</div>
        <div class="text-white font-semibold">持有·逢低加仓</div>
      </div>
    </div>
    <div class="mt-3 text-xs text-white/70 leading-relaxed">
      <p><b class="text-yellow-400">📰 最新催化</b>：新型电力系统建设"十五五"规划明确提出"电力与算力协同融合"，
      AI数据中心+电网建设双轮驱动液冷温控需求。英维克作为液冷龙头直接受益。</p>
      <p class="mt-2"><b class="text-yellow-400">💹 技术面</b>：46元附近是前期平台支撑位，昨日缩量下跌1%，属于被动跟跌，抛压不重。
      如果大盘企稳，液冷板块有望率先反弹。</p>
      <p class="mt-2"><b class="text-yellow-400">⚡ 操作策略</b>：继续持有，若回调至42-44元区间可加仓。
      第一目标位55元（前期高点附近），第二目标位65元（AI液冷需求释放后估值修复）。</p>
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
        <div class="text-xl font-bold text-white/60">数据获取中</div>
        <div class="text-xs text-white/50">API连接异常·以行情软件为准</div>
      </div>
    </div>
    <div class="grid md:grid-cols-3 gap-3 text-xs">
      <div class="bg-white/5 rounded-lg p-3">
        <div class="text-white/60 mb-1">最新评级</div>
        <div class="text-purple-400 font-semibold">⏸️ 观望·等待企稳信号</div>
      </div>
      <div class="bg-white/5 rounded-lg p-3">
        <div class="text-white/60 mb-1">关注因素</div>
        <div class="text-white font-semibold">存储涨价传导+PCB需求</div>
      </div>
      <div class="bg-white/5 rounded-lg p-3">
        <div class="text-white/60 mb-1">操作建议</div>
        <div class="text-white font-semibold">底仓持有·不加仓</div>
      </div>
    </div>
    <div class="mt-3 text-xs text-white/70 leading-relaxed">
      <p><b class="text-yellow-400">📊 基本面</b>：铜冠铜箔是国内电子铜箔龙头，受益于AI服务器PCB需求增长+存储芯片封装载板需求。
      但短期受大盘情绪影响，铜箔板块随科技股整体调整。</p>
      <p class="mt-2"><b class="text-yellow-400">⚡ 操作策略</b>：底仓继续持有，不急于加仓。
      等存储板块企稳+中报业绩验证后再考虑加仓。关注FMS峰会对存储产业链的情绪传导。</p>
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
        <div class="text-xl font-bold text-red-400">10.04元</div>
        <div class="text-xs text-red-400">8月3日涨4.91%·游资主导</div>
      </div>
    </div>
    <div class="bg-red-500/10 border border-red-500/30 rounded-lg p-3 mb-3">
      <p class="text-red-300 text-xs font-semibold">⚠️ 高风险警示：ST股退市风险极高，反弹就是减仓机会</p>
    </div>
    <div class="text-xs text-white/70 leading-relaxed">
      <p><b class="text-yellow-400">📰 最新动态</b>：8月3日上涨4.91%，主力资金净流出73.79万，游资净流入192.81万——典型的游资炒作行情，没有机构参与。
      一季报营收-35%，净利润亏损5311万，负债率94.38%，基本面持续恶化。</p>
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
    <h4 class="text-red-300 font-semibold mb-3 flex items-center gap-2"><span>🐻</span> 空方观点：存储周期见顶信号增多，调整可能尚未结束</h4>
    <div class="text-xs text-white/70 space-y-3 leading-relaxed">
      <div class="bg-white/5 rounded-lg p-3">
        <p class="text-red-300 font-semibold mb-1">风险1：DRAM涨价到客户拒绝接受的地步</p>
        <p>手机DRAM价格二季度环比涨超80%，OPPO、vivo已明确拒绝三星三季度的涨价报价，国内头部手机厂商多家跟进。
        大摩明确警告内存合约价格或在四季度见顶。传统DRAM合约价季度涨幅已从Q1的93%-98%骤降至Q2的58%-63%，Q3预计进一步放缓至13%-18%。</p>
      </div>
      <div class="bg-white/5 rounded-lg p-3">
        <p class="text-red-300 font-semibold mb-1">风险2：英伟达砍HBM配置，AI硬件"降本"潮开始</p>
        <p>SemiAnalysis报告显示，英伟达Rubin Ultra从HBM4E 12-Hi 384GB降为HBM4 8-Hi 192GB，容量直接砍半，功耗从2300W降到1800W。
        AMD MI455X也在做同样的事。内存成本占比从接近40%降到28%——这意味着存储涨价的天花板已经被客户用脚投票了。</p>
      </div>
      <div class="bg-white/5 rounded-lg p-3">
        <p class="text-red-300 font-semibold mb-1">风险3：韩股杠杆暴雷可能传导至A股</p>
        <p>韩国还有超1000亿美元高杠杆芯片多头头寸悬而未决，高盛警告强制平仓风险未完全消散。
        如果韩股继续暴跌，外资可能在全球范围内减持半导体仓位，A股半导体板块难以独善其身。
        昨日科创50暴跌5.08%已经是预警信号。</p>
      </div>
      <div class="bg-white/5 rounded-lg p-3">
        <p class="text-red-300 font-semibold mb-1">风险4：苹果考虑增加DRAM供应商，三寡头格局松动</p>
        <p>苹果CEO库克在财报会上表示"正在评估增加DRAM供应商的选项"，被市场解读为可能引入第四家供应商打破三星/SK海力士/美光的寡头垄断。
        如果CXM（长鑫存储）进入苹果供应链，对现有三巨头的定价权是重大打击。</p>
      </div>
      <div class="bg-white/5 rounded-lg p-3">
        <p class="text-red-300 font-semibold mb-1">风险5：中报暴雷潮尚未结束</p>
        <p>8月中下旬是中报密集披露期，部分半导体公司业绩可能不及预期。
        兆易创新跌停机构卖出8亿只是开始，后续可能还有更多业绩雷。
        在业绩全部落地前，资金不敢重仓做多。</p>
      </div>
    </div>
  </div>

  <div class="bg-green-500/10 border border-green-500/30 rounded-xl p-4">
    <h4 class="text-green-300 font-semibold mb-3 flex items-center gap-2"><span>🐂</span> 多方反驳：景气周期未结束，调整是买入机会</h4>
    <div class="text-xs text-white/70 space-y-2 leading-relaxed">
      <p>① <b>HBM需求依然紧缺</b>：英伟达降配是个别产品的成本优化，不代表整体HBM需求下降。
      五大云厂商2026年资本开支合计预计达7300亿美元，同比接近翻倍，存储龙头景气叙事仍成立。
      三星把60%-70%的存储产能锁入长期协议，下调幅度限5%、上行空间可达20%。</p>
      <p>② <b>韩股跌的是杠杆不是基本面</b>：日本半导体股V型反弹，铠侠+9%大涨，说明存储的景气没变，
      跌的是韩国的杠杆泡沫。去杠杆完成后，真正的基本面行情才会展开。</p>
      <p>③ <b>国产替代加速</b>：海外巨头涨价+供应紧张，反而加速了国内晶圆厂和存储厂的国产替代进程，
      雅克科技、华海诚科等国内材料公司长期受益。机构跌停板抄底雅克科技就是明证。</p>
      <p>④ <b>新的增长点正在出现</b>：HBF（高带宽闪存）标准发布，打开NAND新增长空间；
      端侧AI存储需求爆发，江波龙等公司受益。存储行业不只有DRAM涨价一条逻辑。</p>
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
      <p class="mb-2">美股大涨提供正面情绪，但A股自身处于中报验证期+半导体调整期，<b class="text-yellow-400">高开不等于高走</b>，
      重点关注半导体板块能否在FMS峰会催化下止跌企稳。</p>
      <p><b class="text-yellow-400">核心思路</b>：不追高，等回踩；有业绩的跌下来敢买，没业绩的涨起来要卖。
      当前阶段：结构性行情为主，指数震荡，板块轮动快。</p>
    </div>
  </div>

  <div class="grid md:grid-cols-2 gap-4">
    <div class="bg-white/5 rounded-xl p-4">
      <h4 class="text-green-400 font-semibold mb-3 text-sm">✅ 可以做的</h4>
      <div class="text-xs text-white/70 space-y-2">
        <p>• 雅克科技如继续下探60-65元，小仓位左侧加仓（不超过总仓位10%）</p>
        <p>• 英维克回调至42-44元区间加仓，持有待涨</p>
        <p>• 关注电力/电网板块的政策催化机会（十五五规划落地）</p>
        <p>• 中报超预期的品种回调即是买点</p>
        <p>• FMS峰会相关的存储/先进封装材料标的观察低吸机会</p>
      </div>
    </div>
    <div class="bg-white/5 rounded-xl p-4">
      <h4 class="text-red-400 font-semibold mb-3 text-sm">❌ 不要做的</h4>
      <div class="text-xs text-white/70 space-y-2">
        <p>• 不要因为美股大涨就追高A股半导体，情绪只影响开盘</p>
        <p>• 不要抄底纯题材的半导体设计股，机构在减持</p>
        <p>• 不要重仓单一个股，保持仓位分散</p>
        <p>• *ST建艺反弹要减仓，不要加仓ST股</p>
        <p>• 不要在成交量萎缩时追涨，量价背离是危险信号</p>
      </div>
    </div>
  </div>

  <div class="bg-white/5 rounded-xl p-4">
    <h4 class="text-white font-semibold mb-3 flex items-center gap-2"><span>📋</span> 今日关注事件时间表</h4>
    <div class="grid md:grid-cols-2 gap-3 text-xs text-white/70">
      <div>
        <p><b class="text-yellow-400">08:00</b> FMS 2026闪存峰会开幕（美国硅谷，夜间继续）</p>
        <p><b class="text-yellow-400">10:30</b> 中国气象局8月新闻发布会</p>
        <p><b class="text-yellow-400">全天</b> 中报密集披露：中孚实业、有研新材、东方电缆等</p>
      </div>
      <div>
        <p><b class="text-yellow-400">20:30</b> 美国6月贸易帐、加拿大6月贸易帐</p>
        <p><b class="text-yellow-400">22:00</b> 美国JOLTS职位空缺、工厂订单</p>
        <p><b class="text-yellow-400">盘后</b> AMD财报、SpaceX上市后首份季报</p>
      </div>
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
          <span class="text-green-400 font-semibold">✅ T+3验证：存储板块暴跌后反弹（7/31预判）</span>
          <span class="text-white/50 text-xs">部分验证</span>
        </div>
        <p class="text-white/60 text-xs">
          7月31日预判"存储板块超跌后将迎来技术反弹"，实际8月1-2日韩股暴涨18%、A股存储板块跟涨，
          但8月3日韩股二次暴跌、A股存储继续下跌。反弹确实发生了，但持续性很差，属于脉冲式反弹。
          <b class="text-yellow-400">评级：部分正确</b>——反弹方向对了，但低估了杠杆风暴的二次冲击。
        </p>
      </div>
      <div class="bg-amber-500/10 border border-amber-500/30 rounded-lg p-3">
        <div class="flex items-center justify-between mb-1">
          <span class="text-amber-400 font-semibold">⏳ T+1验证：8月开门震荡分化（8/3预判）</span>
          <span class="text-white/50 text-xs">验证中</span>
        </div>
        <p class="text-white/60 text-xs">
          8月3日预判"8月开门红但创业板继续弱势，结构性分化"，实际8月3日沪指-0.59%、创业板-1.24%、科创50-5.08%，
          电力/电网板块大涨、半导体板块大跌——分化格局完全符合预期。
        </p>
      </div>
      <div class="bg-blue-500/10 border border-blue-500/30 rounded-lg p-3">
        <div class="flex items-center justify-between mb-1">
          <span class="text-blue-400 font-semibold">🔄 待验证：液冷板块业绩验证后反弹（7/31预判）</span>
          <span class="text-white/50 text-xs">观察中</span>
        </div>
        <p class="text-white/60 text-xs">
          7月31日预判"液冷板块超跌后可能迎来政策催化反弹"，
          周末发改委算力网政策+十五五电力规划，双重政策催化已落地，
          观察英维克等液冷龙头能否在本周走出独立行情。
        </p>
      </div>
    </div>
  </div>

  <div class="bg-white/5 rounded-xl p-4">
    <h4 class="text-white font-semibold mb-2 flex items-center gap-2">
      <span>🔮</span> 今日预判（8/4）
    </h4>
    <div class="text-xs text-white/70 space-y-2">
      <p><b class="text-yellow-400">预判1：</b>受美股大涨影响，A股今日高开，但半导体板块高开低走概率大，
      韩股暴跌的阴影仍在，FMS峰会催化不足以扭转短期趋势</p>
      <p><b class="text-yellow-400">预判2：</b>电力/电网/液冷板块继续走强，十五五规划+AI算力需求双催化，
      英维克等龙头有望在今日表现强于大盘</p>
      <p><b class="text-yellow-400">预判3：</b>雅克科技在机构抄底支撑下，今日可能止跌企稳或小幅反弹，
      65-70元区间形成短期底部，但反转还需要量能配合</p>
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
    <p class="text-yellow-300 font-semibold mb-1">教训#3：杠杆市的暴涨暴跌都要远离</p>
    <p class="text-white/60 text-xs">
      韩股40天从高点跌近40%、单日暴涨18%又单日暴跌5%，这是典型的杠杆市特征。
      在高杠杆市场里，暴涨和暴跌都是风险信号，不是机会信号。
      <b>正确做法</b>：远离高杠杆标的和高杠杆市场，
      不要试图在赌场里算概率。宁可错过，不要做错。
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
</div>'''
gen.add_section("教训库引用", lesson_html, "📚")

# ========== 生成+发布 ==========
output_path = os.path.join(WORK_DIR, 'docs/daily/20260804_每日新闻洞察.html')
result = gen.publish(output_path=output_path)
print("发布结果:", result)
print("成功:", result.get('success', False))
print("报告路径:", output_path)
print("文件大小:", os.path.getsize(output_path), "字节")

# 更新 latest.html
latest_path = os.path.join(WORK_DIR, 'docs/daily/latest.html')
shutil.copy2(output_path, latest_path)
print("latest.html 已更新")
