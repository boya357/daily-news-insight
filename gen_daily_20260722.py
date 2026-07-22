#!/usr/bin/env python3
"""2026年7月22日 每日新闻洞察生成 - 周三·美股半导体暴力反攻·存储芯片全线涨停·美光+12%闪迪+14%·A股科技股修复延续·隔夜全球风险偏好回升"""
import sys, os, shutil, json
WORK_DIR = '/root/daily-news-insight'
sys.path.insert(0, os.path.join(WORK_DIR, 'v3'))
from generators.daily_pro import DailyReportProGenerator

gen = DailyReportProGenerator(
    date_str='2026年7月22日', weekday='星期三',
    subtitle='2026年7月22日 星期三 · 美股半导体暴力反攻费半+5.21%·存储芯片全线爆发美光+12.17%闪迪+14.27%·英伟达发布Vera CPU·证监会三场座谈释放维稳信号·A股科技修复延续 · 持仓普涨反弹日',
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
    {"name":"道琼斯","change":"+0.74%","up":True},
    {"name":"标普500","change":"+0.89%","up":True},
    {"name":"纳斯达克","change":"+1.29%","up":True},
    {"name":"费城半导体","change":"+5.21%","up":True},
    {"name":"恒生指数","change":"-0.04%","up":False},
    {"name":"日经225","change":"-0.90%","up":False},
])
global_list1 = render_list([
    {"name":"WTI原油","change":"+0.39%/84.67","up":True},
    {"name":"布伦特原油","change":"+0.60%/91.56","up":True},
    {"name":"COMEX黄金","change":"+0.63%/4102","up":True},
    {"name":"COMEX白银","change":"+0.46%/59.38","up":True},
])
global_list2 = render_list([
    {"name":"三星电子","change":"+6.15%","up":True},
    {"name":"SK海力士","change":"+4.08%","up":True},
    {"name":"三星SDI","change":"+3.87%","up":True},
    {"name":"LG新能源","change":"-0.16%","up":False},
])
global_list3 = render_list([
    {"name":"美光科技","change":"+12.17%","up":True},
    {"name":"闪迪(SanDisk)","change":"+14.27%","up":True},
    {"name":"西部数据","change":"+11.03%","up":True},
    {"name":"AMD","change":"+8.11%","up":True},
    {"name":"英特尔","change":"+8.64%","up":True},
    {"name":"英伟达","change":"+1.97%","up":True},
])
global_html = '''
<div class="grid md:grid-cols-3 gap-4">
  <div class="md:col-span-2">
    <div class="text-white font-semibold mb-3 flex items-center gap-2"><span>🌍</span><span>隔夜全球市场 · 半导体暴力反攻·存储芯片全线爆发·费半创六周最大涨幅</span></div>
    <div class="grid grid-cols-3 md:grid-cols-6 gap-2">{0}</div>
    <p class="text-xs text-white/50 mt-3 leading-relaxed">
      ⚡ <b class="text-yellow-400">核心要点：美股半导体板块暴力反弹，AI交易大反攻，存储芯片领涨</b>——
      ①<b class="text-red-400">费城半导体指数暴涨5.21%</b>，创6月22日以来最大单日涨幅，彻底扭转上周五跌入熊市区域的颓势。
      30只成分股集体收高，英特尔+8.64%、AMD+8.11%、Arm+7.46%、应用材料+7.39%、台积电ADR+5.55%。<br>
      ②<b class="text-red-400">存储芯片全线涨停式暴涨</b>：闪迪+14.27%（全天成交额210亿美元）、美光科技+12.17%（成交额458亿美元，市值重返万亿美元）、
      SK海力士ADR+13.75%、西部数据+11.03%、希捷科技+8.92%。Roundhill存储ETF大涨10.91%。<br>
      ③<b class="text-yellow-400">三大催化剂共振</b>：
      摩根士丹利研报称数据中心存储芯片短缺持续恶化，Q2-Q3价格环比上涨至少25%，短缺延续至2028年；
      SK集团会长崔泰源称2027年AI半导体需求增长60%-100%，存储需求增幅50%-60%，全球存储芯片争夺接近"恐慌"状态；
      高盛/瑞银认为动量去风险进入末段，对冲基金已大幅减仓动量股，半导体接近底部。<br>
      ④<b>英伟达发布Vera CPU</b>：首款自主设计CPU核心的服务器处理器，针对AI智能体优化，性能较x86提升约50%，
      已交付OpenAI/Anthropic/SpaceX等客户，单颗均价约5000美元，预计今年出货130万颗，直接挑战AMD/英特尔。<br>
      ⑤<b>大宗商品</b>：油价高位震荡布油91.56美元（+0.60%），黄金+0.63%至4102美元/盎司，
      中东局势仍有不确定性但市场视之为短期扰动。<br>
      ⑥<b class="text-yellow-400">A股影响</b>：隔夜美股半导体/存储暴涨直接提振A股科技情绪，
      叠加国内证监会三场座谈释放维稳信号、ETF连续11日净流入3567亿、万亿打新资金解冻回流，
      今日A股科技板块有望延续修复行情。重点关注：存储芯片、半导体设备、AI算力、先进封装。
    </p>
  </div>
  <div class="space-y-4">
    <div>
    <div class="text-white font-semibold mb-3 flex items-center gap-2"><span>🛢️</span><span>大宗商品</span></div>
      <div class="bg-white/5 rounded-lg p-3">{1}</div></div>
    <div>
    <div class="text-white font-semibold mb-3 flex items-center gap-2"><span>🇰🇷</span><span>韩股核心（半导体反弹）</span></div>
      <div class="bg-white/5 rounded-lg p-3">{2}</div></div>
    <div>
    <div class="text-white font-semibold mb-3 flex items-center gap-2"><span>💾</span><span>美股存储/芯片龙头</span></div>
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
    <div class="text-xl font-bold text-red-400">3864.37</div>
    <div class="text-xs text-red-400 mt-1">+1.61% / 收复3850</div>
  </div>
  <div class="bg-gradient-to-br from-red-500/20 to-orange-500/10 border border-red-500/30 rounded-xl p-3 text-center">
    <div class="text-xs text-white/60 mb-1">深证成指</div>
    <div class="text-xl font-bold text-red-400">14465.82</div>
    <div class="text-xs text-red-400 mt-1">+5.54%</div>
  </div>
  <div class="bg-gradient-to-br from-red-500/20 to-orange-500/10 border border-red-500/30 rounded-xl p-3 text-center">
    <div class="text-xs text-white/60 mb-1">创业板指</div>
    <div class="text-xl font-bold text-red-400">3622.15</div>
    <div class="text-xs text-red-400 mt-1">+5.64%</div>
  </div>
  <div class="bg-gradient-to-br from-yellow-500/20 to-amber-500/10 border border-yellow-500/30 rounded-xl p-3 text-center">
    <div class="text-xs text-white/60 mb-1">成交额</div>
    <div class="text-xl font-bold text-yellow-400">2.97万亿</div>
    <div class="text-xs text-white/60 mt-1">放量反弹</div>
  </div>
</div>
<div class="bg-white/5 rounded-xl p-4">
  <h4 class="text-white font-semibold mb-3 text-sm">📊 周二（7/21）A股复盘：科技股暴力反攻·科创50暴涨10.73%·14股地天板·政策底+资金底共振</h4>
  <div class="grid md:grid-cols-2 gap-4 text-xs">
    <div>
      <p class="text-white/80 font-semibold mb-2">📈 最强方向</p>
      <p class="text-white/60 leading-relaxed mb-2">
      <b class="text-yellow-400">①半导体/芯片（涨停潮）</b>：科创50暴涨10.73%，半导体ETF+9%，
      雅克科技/长电科技/有研新材/光迅科技等14只科技股上演"地天板"，从跌停拉到涨停。<br>
      <b class="text-yellow-400">②AI算力/液冷</b>：英维克+8.17%探底50元后大反弹，日内振幅超18%，
      寒武纪/海光信息等算力标的全线大涨。<br>
      ③存储芯片/先进封装：长电科技地天板，通富微电/华天科技跟涨，
      存储产业链情绪受美股美光大涨预期推动。<br>
      ④人形机器人：三花智控/拓普集团领涨，特斯拉Optimus量产预期升温。
      </p>
    </div>
    <div>
      <p class="text-white/80 font-semibold mb-2">📉 相对弱势</p>
      <p class="text-white/60 leading-relaxed mb-2">
      <b class="text-green-400">①银行/高股息</b>：防御板块资金流出转向成长，工商银行等微涨或持平；<br>
      <b>②*ST建艺</b>：继续阴跌-1.64%收8.41元，盘中探底7.83元创60日新低，
      退市风险未解除，浮亏扩大至-37.5%；<br>
      ③消费/医药：相对滞涨，资金集中涌入科技成长赛道；<br>
      <b class="text-yellow-400">特征</b>：超3000只个股上涨、涨停超百只、
      涨跌比约2.5（情绪修复），恐惧贪婪指数从22（恐惧）回升至45（中性偏谨慎），
      核心驱动：证监会三场座谈释放维稳信号+万亿打新资金解冻+ETF连续11日净流入+美股科技股反弹预期。
      </p>
    </div>
  </div>
  <p class="text-xs text-white/50 mt-3 leading-relaxed">
    ⚡ <b class="text-yellow-400">盘口解读：</b>周二是典型的"政策底+资金底"双重确认后的暴力修复行情，
    科创50单日暴涨10.73%创历史最大单日涨幅之一，半导体板块14只地天板极为罕见。
    但<b>反弹不是反转</b>：上周五刚经历暴跌（创业板-7.15%），技术性反抽后仍有震荡整固需求。
    <b class="text-yellow-400">关键信号：隔夜美股存储/半导体再涨5%+，今日A股科技情绪有望延续，
    但需警惕冲高回落——大涨后获利盘兑现压力大。</b>
    沪指关键压力位3900-3950，支撑位3800-3830。
  </p>
</div>
</div>'''
gen.add_section("昨日A股复盘（7/21）", ashare_html, "📈")

# ========== 3. 今日重磅新闻 ==========
news_items = [
    {"tag":"🚀","title":"美股存储芯片全线暴涨 闪迪+14%美光+12%","content":"费城半导体指数暴涨5.21%创六周最大涨幅，存储芯片领涨。摩根士丹利研报称数据中心存储短缺持续恶化，Q2-Q3价格环比涨至少25%，短缺延续至2028年。美光市值重返万亿美元。","source":"凤凰网/财联社"},
    {"tag":"🏛️","title":"证监会连开三场座谈会 释放五大维稳信号","content":"7月20-21日证监会连开三场座谈会，明确：①强化逆周期调节，大盘快速回调时出台对冲工具；②放宽社保/养老金/保险资金考核标准，倒逼长线资金布局；③约束破净破发/常年不分红企业减持；④简化散户维权，严打内幕交易；⑤督促券商下调两融利率。","source":"东方财富/证券时报"},
    {"tag":"💻","title":"英伟达发布Vera CPU 正式挑战AMD/英特尔","content":"英伟达公布数据中心CPU产品Vera技术细节，首款自主设计CPU核心的服务器处理器，针对AI智能体优化，性能较x86提升约50%。已交付OpenAI/Anthropic/SpaceX，单颗均价约5000美元，预计今年出货130万颗。","source":"每日经济新闻"},
    {"tag":"💰","title":"股票型ETF连续11日净流入 累计超3567亿","content":"全市场股票型ETF已连续11个交易日获资金净流入，累计规模达3567亿元，宽基ETF占比超七成。主力为国家队、保险社保等长线机构资金，市场底部信号进一步明确。","source":"新浪财经"},
    {"tag":"🤖","title":"特斯拉Optimus人形机器人7月启动SOP量产","content":"特斯拉副总裁陶琳确认Optimus将于2026年底正式规模化量产，弗里蒙特工厂远期年产能100万台。7月底至8月初将启动小批量SOP量产，首批按月滚动下单已下发供应链。国内拓普/三花/绿的谐波均获定点。","source":"金融界"},
    {"tag":"📡","title":"低轨卫星发射计划提速 300颗周期前置","content":"工信部通知全年300颗低轨通信卫星发射计划全部周期前置，下半年航天发射密度大幅提升，卫星互联网产业链迎来持续性催化行情。","source":"今日头条财经"},
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
<div class="bg-gradient-to-br from-red-500/20 to-orange-500/10 border border-red-500/30 rounded-xl p-4">
  <div class="flex items-center gap-2 mb-3">
    <span class="text-2xl">💾</span>
    <h4 class="text-white font-bold">存储芯片/HBM</h4>
    <span class="bg-red-500/30 text-red-300 text-xs px-2 py-0.5 rounded-full">🔥 爆发</span>
  </div>
  <p class="text-white/70 text-xs leading-relaxed mb-2">
    <b class="text-yellow-400">隔夜美股存储芯片全线暴涨</b>：闪迪+14.27%、美光+12.17%、SK海力士ADR+13.75%、西部数据+11%。
    三大核心驱动：
    ①摩根士丹利：数据中心存储短缺持续恶化，Q2-Q3价格环比涨至少25%，短缺延续至2028年；
    ②SK集团会长崔泰源：2027年AI半导体需求增60%-100%，存储需求增50%-60%，全球存储争夺接近"恐慌"状态；
    ③HBM4进展加速：三星HBM4良率已达70%，三大厂均推进良率攻坚战，HBM4搭载于英伟达Vera Rubin下半年推出。
  </p>
  <p class="text-white/50 text-xs">
    📌 A股受益方向：兆易创新（增资5亿推进DRAM）、雅克科技（前驱体+光刻胶）、长电科技/通富微电（先进封装）、
    北京君正（存储芯片设计）、华海诚科（环氧塑封料）。
  </p>
</div>

<div class="bg-gradient-to-br from-blue-500/20 to-cyan-500/10 border border-blue-500/30 rounded-xl p-4">
  <div class="flex items-center gap-2 mb-3">
    <span class="text-2xl">🤖</span>
    <h4 class="text-white font-bold">人形机器人</h4>
    <span class="bg-blue-500/30 text-blue-300 text-xs px-2 py-0.5 rounded-full">⭐ 重点</span>
  </div>
  <p class="text-white/70 text-xs leading-relaxed mb-2">
    <b class="text-yellow-400">特斯拉Optimus 7月启动SOP量产</b>：弗里蒙特工厂7月底-8月初启动小批量量产，
    周产100-200台，四季度目标周产2000台，2026年底规模化量产，远期年产能100万台。
    供应链定点已确认：拓普集团（执行器）、三花智控（热管理+执行器）、绿的谐波（减速器）。
    工信部数据显示2026年国内人形机器人产量有望突破10万台，同比增长超400%。
  </p>
  <p class="text-white/50 text-xs">
    📌 核心标的：三花智控、拓普集团、绿的谐波、鸣志电器、禾川科技。
  </p>
</div>

<div class="bg-gradient-to-br from-purple-500/20 to-indigo-500/10 border border-purple-500/30 rounded-xl p-4">
  <div class="flex items-center gap-2 mb-3">
    <span class="text-2xl">🧊</span>
    <h4 class="text-white font-bold">AI算力/液冷散热</h4>
    <span class="bg-purple-500/30 text-purple-300 text-xs px-2 py-0.5 rounded-full">⭐ 重点</span>
  </div>
  <p class="text-white/70 text-xs leading-relaxed mb-2">
    <b class="text-yellow-400">英伟达Vera CPU发布</b>：首款自主设计服务器CPU，AI智能体优化，x86性能提升50%，
    与GPU组成Vera Rubin计算平台。AI算力需求持续超预期，液冷作为算力基础设施景气度向上。
    AMD今日举办AI算力峰会，发布新一代Zen6架构服务器CPU，催化液冷/光模块/先进封装题材。
  </p>
  <p class="text-white/50 text-xs">
    📌 核心标的：英维克（液冷龙头）、中石科技、曙光数创、高澜股份。
  </p>
</div>

<div class="bg-gradient-to-br from-amber-500/20 to-yellow-500/10 border border-amber-500/30 rounded-xl p-4">
  <div class="flex items-center gap-2 mb-3">
    <span class="text-2xl">🏛️</span>
    <h4 class="text-white font-bold">政策维稳/长线资金入市</h4>
    <span class="bg-amber-500/30 text-amber-300 text-xs px-2 py-0.5 rounded-full">📌 支撑</span>
  </div>
  <p class="text-white/70 text-xs leading-relaxed mb-2">
    证监会三场座谈会落地五大维稳举措：逆周期调节、长线资金考核松绑、减持约束、严打操纵、两融降息。
    ETF连续11日净流入3567亿（国家队+险社保为主），股票型ETF规模突破3万亿。
    政策底明确，系统性大跌空间被封死，但反弹高度取决于基本面验证。
  </p>
  <p class="text-white/50 text-xs">
    📌 受益方向：高股息央企、半导体设备、储能（长线资金偏好方向）。
  </p>
</div>
'''
gen.add_section("核心题材动态", '<div class="grid md:grid-cols-2 gap-4">%s</div>' % topic_cards, "🔥")

# ========== 5. 今日/本周关键催化剂 ==========
catalyst_cards = '''
<div class="bg-white/5 rounded-xl p-4 border border-white/10">
  <div class="flex items-center gap-2 mb-3">
    <span class="bg-red-500/20 text-red-300 text-xs px-2 py-1 rounded">今日</span>
    <h4 class="text-white font-semibold text-sm">7月22日（周三）</h4>
  </div>
  <ul class="text-white/60 text-xs space-y-2">
    <li>🔴 AMD AI算力峰会，发布Zen6架构服务器CPU（催化：先进封装/液冷/光模块）</li>
    <li>🔴 上海国际核能产业博览会（7.22-7.24），发布核电国产化配套规划（催化：核电设备/核燃料）</li>
    <li>🔴 国际低空经济博览会，落地低空飞行试点+商用飞行器补贴细则（催化：低空经济/通航）</li>
    <li>🟡 美股Alphabet/谷歌财报盘后发布（关注AI CapEx支出指引）</li>
    <li>🟡 国内7月LPR报价（预计维持不变）</li>
  </ul>
</div>

<div class="bg-white/5 rounded-xl p-4 border border-white/10">
  <div class="flex items-center gap-2 mb-3">
    <span class="bg-yellow-500/20 text-yellow-300 text-xs px-2 py-1 rounded">本周</span>
    <h4 class="text-white font-semibold text-sm">7月23-25日</h4>
  </div>
  <ul class="text-white/60 text-xs space-y-2">
    <li>🔴 7/23 特斯拉Q2财报（关注Optimus量产进展+机器人业务）</li>
    <li>🔴 7/24 英特尔/德州仪器财报（关注PC/数据中心芯片景气度）</li>
    <li>🟡 7/25 美股微软/苹果财报（科技巨头财报高峰）</li>
    <li>🟡 7月下旬：中报预告密集披露期（业绩驱动行情展开）</li>
    <li>🟡 证监会座谈会后续细则落地预期</li>
  </ul>
</div>

<div class="bg-white/5 rounded-xl p-4 border border-white/10">
  <div class="flex items-center gap-2 mb-3">
    <span class="bg-purple-500/20 text-purple-300 text-xs px-2 py-1 rounded">本月</span>
    <h4 class="text-white font-semibold text-sm">7月下旬核心日历</h4>
  </div>
  <ul class="text-white/60 text-xs space-y-2">
    <li>⭐ 7/30-31 美联储议息会议（降息预期关键节点）</li>
    <li>⭐ 中报业绩密集披露期（7/25-8/15高峰）</li>
    <li>⭐ 长鑫科技IPO后续进展（巨额资金解冻回流）</li>
    <li>⚠️ 中东局势演变（霍尔木兹海峡/红海航运）</li>
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
      <span class="text-white/70">存储芯片（美股暴涨+大摩看多）</span>
      <span class="text-red-400 font-bold">S级</span>
    </div>
    <div class="w-full bg-white/10 rounded-full h-1.5">
      <div class="bg-gradient-to-r from-red-500 to-orange-500 h-1.5 rounded-full" style="width: 95%"></div>
    </div>
    <div class="flex justify-between items-center mt-2">
      <span class="text-white/70">人形机器人（特斯拉量产）</span>
      <span class="text-orange-400 font-bold">A级</span>
    </div>
    <div class="w-full bg-white/10 rounded-full h-1.5">
      <div class="bg-gradient-to-r from-orange-500 to-yellow-500 h-1.5 rounded-full" style="width: 80%"></div>
    </div>
    <div class="flex justify-between items-center mt-2">
      <span class="text-white/70">AI算力/液冷（英伟达Vera+AMD峰会）</span>
      <span class="text-yellow-400 font-bold">A级</span>
    </div>
    <div class="w-full bg-white/10 rounded-full h-1.5">
      <div class="bg-gradient-to-r from-yellow-500 to-amber-500 h-1.5 rounded-full" style="width: 75%"></div>
    </div>
  </div>
</div>
'''
gen.add_section("今日/本周关键催化剂", '<div class="grid md:grid-cols-2 gap-4">%s</div><p class="text-xs text-white/40 mt-4">💡 7月核心变量：中报业绩验证（决定反弹高度）、美联储7/30议息会议（降息幅度）、中东地缘风险（油价/通胀）、国内政策组合拳（维稳力度）。存储芯片为当前最强主线，但需注意短期涨速过快后的回调风险。</p>' % catalyst_cards, "📅")

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
      <span class="bg-green-500/30 text-green-300 text-xs px-2 py-1 rounded-full">+8.17%</span>
    </div>
    <div class="grid grid-cols-3 gap-2 text-center mb-3 text-xs">
      <div><div class="text-white/50">现价</div><div class="text-white font-bold">59.99</div></div>
      <div><div class="text-white/50">成本</div><div class="text-white/70">104.23</div></div>
      <div><div class="text-white/50">浮亏</div><div class="text-red-400 font-bold">-42.4%</div></div>
    </div>
    <div class="space-y-2 text-xs">
      <p class="text-white/60">
        <b class="text-yellow-400">最新动态：</b>7/21探底50元后暴力反弹+8.17%，日内振幅超18%，成交额39.74亿，换手率6.35%。
        主力资金净流入1.07亿，融资净流出4.32亿（杠杆资金出逃）。
        公司获液冷系统实用新型专利，海外布局泰国+美国生产基地。
        机构目标均价95.64元（10家机构，8买入2增持）。
      </p>
      <p class="text-white/60">
        <b class="text-yellow-400">催化：</b>美股半导体反弹→算力情绪修复；英伟达Vera CPU发布→AI算力需求确认；
        AMD今日AI算力峰会→液冷催化。
      </p>
      <p class="text-red-300 bg-red-500/10 rounded p-2">
        ⚠️ <b>风险提示：</b>深度破止损-42.4%，下降趋势未根本扭转，
        一季报净利-81.97%（汇兑损失+成本上升）。
        反弹至60-65区间坚决减仓，破55元无条件清仓。
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
      <span class="bg-green-500/30 text-green-300 text-xs px-2 py-1 rounded-full">+4.17%</span>
    </div>
    <div class="grid grid-cols-3 gap-2 text-center mb-3 text-xs">
      <div><div class="text-white/50">现价</div><div class="text-white font-bold">107.54</div></div>
      <div><div class="text-white/50">成本</div><div class="text-white/70">87.12</div></div>
      <div><div class="text-white/50">浮盈</div><div class="text-green-400 font-bold">+23.4%</div></div>
    </div>
    <div class="space-y-2 text-xs">
      <p class="text-white/60">
        <b class="text-yellow-400">最新动态：</b>7/20跌停（业绩不及预期）后7/21反弹+4.17%收107.54元，
        从82.59元低点反抽，振幅超26%。
        中报预增486%-544%（净利2.05-2.25亿），但Q2环比仅-7%至+12%，
        机构全年预测5.1亿，上半年仅完成约40%，低于预期导致跌停。
      </p>
      <p class="text-white/60">
        <b class="text-yellow-400">催化：</b>AI算力需求爆发→HVLP铜箔供不应求；
        高频高速铜箔量价齐升；母公司铜陵有色中报预增80%+。
      </p>
      <p class="text-orange-300 bg-orange-500/10 rounded p-2">
        ⚠️ <b>风险提示：</b>20cm跌停后修复力度偏弱，业绩不及预期的阴影仍在。
        反弹110-115区间减仓至底仓，破100元止盈离场。
        估值偏高（动态PE约200倍），需警惕回调风险。
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
      <span class="bg-red-500/30 text-red-300 text-xs px-2 py-1 rounded-full">+10.00% 涨停</span>
    </div>
    <div class="grid grid-cols-3 gap-2 text-center mb-3 text-xs">
      <div><div class="text-white/50">现价</div><div class="text-white font-bold">143.55</div></div>
      <div><div class="text-white/50">成本</div><div class="text-white/70">108.80</div></div>
      <div><div class="text-white/50">浮盈</div><div class="text-green-400 font-bold">+31.9%</div></div>
    </div>
    <div class="space-y-2 text-xs">
      <p class="text-white/60">
        <b class="text-yellow-400">最新动态：</b>7/21上演"地天板"极端走势，从跌停117.45元直线拉至涨停143.55元，
        日内振幅20%，成交额59.45亿，换手率14.35%。
        龙虎榜：深股通净买入8553万，机构席位分歧大（净卖出1.33亿），游资合力撬板。
        中信建投预计2026-2028年净利13/17.4/23.6亿，给予买入评级。
      </p>
      <p class="text-white/60">
        <b class="text-yellow-400">催化：</b>美股存储暴涨→半导体材料情绪传导；
        存储芯片短缺持续→前驱体需求旺盛；HBM4量产推进→先进封装材料受益。
      </p>
      <p class="text-yellow-300 bg-yellow-500/10 rounded p-2">
        ⚡ <b>操作策略：</b>地天板为板块共振+超跌修复，非趋势反转确认。
        今日若能连板则持有观察，不能连板则150-155区间减仓至底仓。
        第一支撑130元，第二支撑117元（跌破则修复逻辑不成立）。
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
      <span class="bg-green-500/30 text-green-300 text-xs px-2 py-1 rounded-full">-1.64%</span>
    </div>
    <div class="grid grid-cols-3 gap-2 text-center mb-3 text-xs">
      <div><div class="text-white/50">现价</div><div class="text-white font-bold">8.41</div></div>
      <div><div class="text-white/50">成本</div><div class="text-white/70">13.46</div></div>
      <div><div class="text-white/50">浮亏</div><div class="text-red-400 font-bold">-37.5%</div></div>
    </div>
    <div class="space-y-2 text-xs">
      <p class="text-white/60">
        <b class="text-yellow-400">最新动态：</b>7/21继续阴跌-1.64%收8.41元，盘中探底7.83元创60日新低，
        振幅10.53%。7/20被限制高消费，7/19持有股权被冻结（499.99万元）。
        上半年预亏1.1-1.6亿，净资产仍为负，退市风险未解除。
      </p>
      <p class="text-white/60">
        <b class="text-red-400">负面催化：</b>向原实控人刘海云追索20.43亿补偿款（仲裁中）；
        227场官司、40亿债务压顶；珠海国资刚保壳即"清算"；
        庭外重组推进中但不确定性极大。
      </p>
      <p class="text-red-300 bg-red-500/10 rounded p-2">
        🚫 <b>操作建议：坚决清仓，一股不留</b>。
        ST股=风险敞口，退市即归零。浮亏-37.5%虽痛，
        但继续持有可能血本无归。趁今日大盘反弹寻找任何反弹机会果断离场，
        将资金腾挪至确定性更高的科技成长标的。
      </p>
    </div>
  </div>
</div>

<!-- 持仓总览 -->
<div class="mt-4 bg-white/5 rounded-xl p-4 border border-white/10">
  <div class="flex items-center justify-between mb-3">
    <h4 class="text-white font-semibold">📊 持仓总览与操作建议</h4>
    <span class="text-xs text-yellow-400">整体仓位：建议控制在1-2成</span>
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
          <td class="text-right">59.99</td>
          <td class="text-right text-red-400">-42.4%</td>
          <td class="text-right text-red-400">🔴 止损破位</td>
          <td class="py-2">反弹60-65减仓，破55清仓</td>
        </tr>
        <tr class="border-b border-white/5">
          <td class="py-2">铜冠铜箔</td>
          <td class="text-right">107.54</td>
          <td class="text-right text-green-400">+23.4%</td>
          <td class="text-right text-yellow-400">🟡 业绩不及预期</td>
          <td class="py-2">110-115减仓至底仓，破100止盈</td>
        </tr>
        <tr class="border-b border-white/5">
          <td class="py-2">雅克科技</td>
          <td class="text-right">143.55</td>
          <td class="text-right text-green-400">+31.9%</td>
          <td class="text-right text-yellow-400">🟡 地天板修复</td>
          <td class="py-2">不能连板则150-155减仓</td>
        </tr>
        <tr>
          <td class="py-2">*ST建艺</td>
          <td class="text-right">8.41</td>
          <td class="text-right text-red-400">-37.5%</td>
          <td class="text-right text-red-400">🔴 退市风险</td>
          <td class="py-2">🚫 坚决清仓，任何反弹都是离场机会</td>
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
        <div><span class="text-white/50">准确率：</span><span class="text-green-400 font-bold">62.5%</span></div>
      </div>
    </div>
    <div class="grid grid-cols-4 gap-2 text-center text-xs">
      <div class="bg-white/5 rounded-lg p-2">
        <div class="text-white/50">总预判</div>
        <div class="text-white font-bold text-lg">12</div>
      </div>
      <div class="bg-white/5 rounded-lg p-2">
        <div class="text-white/50">正确</div>
        <div class="text-green-400 font-bold text-lg">5</div>
      </div>
      <div class="bg-white/5 rounded-lg p-2">
        <div class="text-white/50">部分正确</div>
        <div class="text-yellow-400 font-bold text-lg">5</div>
      </div>
      <div class="bg-white/5 rounded-lg p-2">
        <div class="text-white/50">错误</div>
        <div class="text-red-400 font-bold text-lg">2</div>
      </div>
    </div>
  </div>

  <div class="bg-white/5 rounded-xl p-4 border border-white/10">
    <h4 class="text-white font-semibold mb-3 flex items-center gap-2">
      <span>⏳</span> 待验证预判（进行中）
    </h4>
    <div class="bg-yellow-500/10 border border-yellow-500/30 rounded-lg p-3">
      <div class="flex items-center justify-between mb-2">
        <span class="text-yellow-400 font-semibold text-sm">pred_20260720_001 · A级</span>
        <span class="text-white/50 text-xs">验证日：2026-07-23</span>
      </div>
      <p class="text-white/80 text-sm mb-2"><b>科技成长股进入中期调整，高股息红利+医药防御成新主线</b></p>
      <p class="text-white/50 text-xs">预判逻辑：7/20市场极度割裂，沪指+0.85%但3700只股票下跌，
      银行/高股息领涨，科技成长暴跌。预判市场风格切换至防御。</p>
      <p class="text-white/50 text-xs mt-2">
        📌 <b>T+2验证进度（7/22）：</b>7/21科技股暴力反弹（科创50+10.73%），
        与"科技中期调整"预判矛盾。但单日反弹不足以确认反转，需观察后续3-5天持续性。
        当前暂判为"存疑"，等7/23验证日做最终判定。
      </p>
    </div>
  </div>

  <div class="bg-white/5 rounded-xl p-4 border border-white/10">
    <h4 class="text-white font-semibold mb-3 flex items-center gap-2">
      <span>🎯</span> 今日新增预判
    </h4>
    <div class="space-y-3">
      <div class="bg-red-500/10 border border-red-500/30 rounded-lg p-3">
        <div class="flex items-center justify-between mb-2">
          <span class="text-red-400 font-semibold text-sm">预判 #20260722_001 · A级</span>
          <span class="text-white/50 text-xs">验证日：2026-07-25（T+3）</span>
        </div>
        <p class="text-white/80 text-sm mb-2">
          <b>存储芯片板块短期见顶风险加大，追高需谨慎</b>
        </p>
        <p class="text-white/60 text-xs">
          逻辑：美股存储芯片单日暴涨（美光+12%/闪迪+14%）后，短期获利盘兑现压力大；
          A股存储概念股前期已有较大涨幅，叠加中报业绩验证窗口，
          预计T+3（7/25前）内出现5-10%级别的回调概率较高。
          但中期存储涨价逻辑未破，回调后仍是布局良机。
        </p>
      </div>
      <div class="bg-blue-500/10 border border-blue-500/30 rounded-lg p-3">
        <div class="flex items-center justify-between mb-2">
          <span class="text-blue-400 font-semibold text-sm">预判 #20260722_002 · B级</span>
          <span class="text-white/50 text-xs">验证日：2026-07-25（T+3）</span>
        </div>
        <p class="text-white/80 text-sm mb-2">
          <b>人形机器人板块7月下旬迎来主升浪行情</b>
        </p>
        <p class="text-white/60 text-xs">
          逻辑：特斯拉Optimus 7月启动SOP量产（产业里程碑）、
          7/23特斯拉Q2财报（机器人业务重点关注）、
          工信部人形机器人万台部署计划、国内产业链定点密集落地。
          预判T+3内人形机器人板块涨幅超存储/算力，成为最强主线之一。
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
      报告不仅要讲机会，更要讲风险。以下是空方可能证伪当前反弹逻辑的五大角度：
    </p>
  </div>

  <div class="bg-white/5 rounded-xl p-4 border border-white/10">
    <div class="flex items-start gap-3">
      <span class="text-red-400 text-lg font-bold">1</span>
      <div>
        <h5 class="text-white font-semibold text-sm mb-1">技术性反弹非反转：获利盘抛压巨大</h5>
        <p class="text-white/60 text-xs leading-relaxed">
          上周五（7/17）刚经历创业板-7.15%的暴跌，周二百股涨停+科创50+10.73%是暴跌后的技术性反抽。
          场内套牢盘体量巨大（上周五约4950只个股下跌），每一次反弹都是解套出逃的机会。
          隔夜美股半导体暴涨虽有助攻，但A股科技股7月初以来的涨幅已透支了部分预期，
          追高风险极大。历史经验：暴跌后的第一波反弹通常会有二次探底。
        </p>
      </div>
    </div>
  </div>

  <div class="bg-white/5 rounded-xl p-4 border border-white/10">
    <div class="flex items-start gap-3">
      <span class="text-red-400 text-lg font-bold">2</span>
      <div>
        <h5 class="text-white font-semibold text-sm mb-1">中报业绩验证期：题材股面临估值杀</h5>
        <p class="text-white/60 text-xs leading-relaxed">
          7月下旬进入中报密集披露期，业绩才是检验股价的唯一标准。
          铜冠铜箔就是先例：中报预增486%却20cm跌停，原因是增速环比放缓+低于机构全年预期。
          雅克科技动态PE仍有55倍（基于2026预测），英维克一季度净利-82%，
          一旦中报业绩不及预期，估值杀会非常惨烈。
          纯题材、无业绩支撑的小票将被无情抛弃。
        </p>
      </div>
    </div>
  </div>

  <div class="bg-white/5 rounded-xl p-4 border border-white/10">
    <div class="flex items-start gap-3">
      <span class="text-red-400 text-lg font-bold">3</span>
      <div>
        <h5 class="text-white font-semibold text-sm mb-1">美联储7/30议息：降息幅度不及预期风险</h5>
        <p class="text-white/60 text-xs leading-relaxed">
          市场当前定价7月降息25bp概率约70%，降息50bp概率约30%。
          但近期油价回升（布油91美元）+ 核心通胀粘性可能迫使美联储偏鹰。
          若只降息25bp且鲍威尔讲话偏鹰，全球风险资产将承压。
          更关键的是降息后经济走向：是软着陆还是硬着陆？
          若经济衰退预期升温，科技股估值会先于盈利下杀。
        </p>
      </div>
    </div>
  </div>

  <div class="bg-white/5 rounded-xl p-4 border border-white/10">
    <div class="flex items-start gap-3">
      <span class="text-red-400 text-lg font-bold">4</span>
      <div>
        <h5 class="text-white font-semibold text-sm mb-1">中东地缘风险：油价上涨→通胀→降息推迟</h5>
        <p class="text-white/60 text-xs leading-relaxed">
          布伦特原油已站上91美元/桶，中东局势持续紧张。
          若霍尔木兹海峡封锁升级或红海航运持续受扰，油价可能冲击100美元。
          高油价=输入性通胀=美联储降息推迟=全球流动性收紧=科技股估值承压。
          这是当前最大的黑天鹅变量。市场目前选择性忽视，但一旦油价破100，
          通胀交易将卷土重来，成长股会遭到抛售。
        </p>
      </div>
    </div>
  </div>

  <div class="bg-white/5 rounded-xl p-4 border border-white/10">
    <div class="flex items-start gap-3">
      <span class="text-red-400 text-lg font-bold">5</span>
      <div>
        <h5 class="text-white font-semibold text-sm mb-1">量化交易监管趋严：短期流动性冲击</h5>
        <p class="text-white/60 text-xs leading-relaxed">
          证监会三场座谈明确提出规范量化交易行为，沪深交易所已上调高频交易申报费率。
          若后续出台更严厉的量化监管措施（如限制换手率、提高保证金），
          市场短期流动性可能受到冲击，特别是量化资金占比较高的小盘股和热门赛道股。
          量化资金既是上涨的助推器，也是下跌的加速器，监管收紧可能加剧波动。
        </p>
      </div>
    </div>
  </div>

  <div class="bg-red-500/10 border border-red-500/30 rounded-xl p-4">
    <p class="text-red-300 text-sm font-semibold mb-2">⚠️ 空方结论</p>
    <p class="text-white/70 text-xs leading-relaxed">
      当前反弹是"政策底+超跌修复+美股助攻"的三重共振，可持续性有待验证。
      建议：<b>反弹减仓，控制仓位在1-2成，等待二次探底或趋势确认后再加仓</b>。
      不要被单日暴涨冲昏头脑，纪律比收益更重要。
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
      隔夜美股半导体暴涨+国内政策维稳，科技股情绪延续修复，但<b class="text-yellow-400">反弹不是反转</b>，
      操作上坚持"反弹减仓、控制仓位、严守纪律"十二字方针。
      整体仓位建议<b class="text-red-400">1-2成</b>，保留充足现金应对不确定性。
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
          <span><b class="text-red-300">*ST建艺：任何反弹坚决清仓</b>，退市风险敞口必须关闭，不留幻想</span>
        </li>
        <li class="flex items-start gap-2">
          <span class="text-yellow-400 mt-0.5">2.</span>
          <span><b class="text-yellow-300">英维克：60-65元区间减仓至1成以下</b>，深度破止损后反弹是离场机会</span>
        </li>
        <li class="flex items-start gap-2">
          <span class="text-yellow-400 mt-0.5">3.</span>
          <span><b class="text-yellow-300">铜冠铜箔：110-115元减仓至底仓</b>，业绩不及预期后估值偏高</span>
        </li>
        <li class="flex items-start gap-2">
          <span class="text-green-400 mt-0.5">4.</span>
          <span><b class="text-green-300">雅克科技：不能连板则150-155减仓</b>，地天板后分歧加大，不追高</span>
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
          <span><b class="text-red-300">存储芯片/HBM：</b>情绪最高但追高风险大，等回调后布局（预判短期见顶）</span>
        </li>
        <li class="flex items-start gap-2">
          <span class="text-orange-400 mt-0.5">⭐</span>
          <span><b class="text-orange-300">人形机器人：</b>特斯拉Optimus量产+Q2财报催化，内资独立主线</span>
        </li>
        <li class="flex items-start gap-2">
          <span class="text-blue-400 mt-0.5">🧊</span>
          <span><b class="text-blue-300">AI算力/液冷：</b>英伟达Vera+AMD峰会催化，但需先消化前期跌幅</span>
        </li>
        <li class="flex items-start gap-2">
          <span class="text-purple-400 mt-0.5">🛡️</span>
          <span><b class="text-purple-300">高股息防御：</b>作为底仓配置，对冲市场系统性风险</span>
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
        <div class="text-red-400 font-bold">3700-3750</div>
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
      ①<b>不追高</b>：隔夜美股暴涨后A股高开是大概率，追高易被套；
      ②<b>反弹减仓</b>：利用情绪高涨期降低仓位，落袋为安；
      ③<b>严守止损</b>：破位标的坚决执行纪律，不存侥幸；
      ④<b>现金为王</b>：保留充足弹药，等待更确定性的机会（如中报超预期、二次探底完成）。
    </p>
  </div>
</div>
'''
gen.add_section("今日操作策略", strategy_html, "🎯")

# ========== 10. 教训库引用 ==========
lesson_html = '''
<div class="space-y-3">
  <div class="bg-red-500/10 border border-red-500/30 rounded-lg p-3">
    <p class="text-red-300 font-semibold mb-1">教训#1：暴跌后不是抄底时机，等企稳信号</p>
    <p class="text-white/60 text-xs">
      上周五（7/17）创业板-7.15%暴跌后，很多人周一急着抄底结果7/20继续大跌。
      <b>正确做法</b>：暴跌后至少等3个交易日企稳信号（缩量+止跌+均线修复）再考虑进场，
      绝不接"飞刀"。7/21虽暴涨，但单日反转不足以确认底部，二次探底概率仍高。
    </p>
  </div>

  <div class="bg-orange-500/10 border border-orange-500/30 rounded-lg p-3">
    <p class="text-orange-300 font-semibold mb-1">教训#2：利好出尽是利空，业绩预告超预期≠股价涨</p>
    <p class="text-white/60 text-xs">
      铜冠铜箔中报预增486%却20cm跌停，原因是增速环比放缓+低于机构全年预期。
      <b>正确做法</b>：业绩预告要看"预期差"而非绝对增速，
      前期涨幅过大的标的，即便业绩好也可能"利好出尽"。
      买入前必须对标一致预期，确认是否真的超预期。
    </p>
  </div>

  <div class="bg-yellow-500/10 border border-yellow-500/30 rounded-lg p-3">
    <p class="text-yellow-300 font-semibold mb-1">教训#3：地天板不是买入信号，是情绪极端的表现</p>
    <p class="text-white/60 text-xs">
      雅克科技地天板（从跌停到涨停）看似强势，实则是多空激烈博弈的结果，
      机构席位净卖出1.33亿说明部分机构借流动性出逃。
      <b>正确做法</b>：地天板后不追高，观察次日能否延续强势（连板=强，冲高回落=弱），
      再决定操作方向。高波动往往意味着高风险。
    </p>
  </div>

  <div class="bg-amber-500/10 border border-amber-500/30 rounded-lg p-3">
    <p class="text-amber-300 font-semibold mb-1">教训#4：ST股不能碰，越跌越不能补</p>
    <p class="text-white/60 text-xs">
      *ST建艺从13.46元跌到8.41元，浮亏-37.5%，期间任何补仓只会扩大亏损。
      退市风险下，底部可能就是退市清零。
      <b>正确做法</b>：ST股坚决不碰，一旦持仓变ST必须第一时间清仓，不存任何幻想。
      退市股归零的风险是永久性损失，不值得用本金去赌重组概率。
    </p>
  </div>
</div>
'''
gen.add_section("教训库引用", lesson_html, "📚")

# ========== 生成+发布 ==========
output_path = os.path.join(WORK_DIR, 'docs/daily/20260722_每日新闻洞察.html')
result = gen.publish(output_path=output_path)
print("发布结果:", result)
print("成功:", result.get('success', False))
print("报告路径:", output_path)
print("文件大小:", os.path.getsize(output_path), "字节")

# 更新 latest.html
latest_path = os.path.join(WORK_DIR, 'docs/daily/latest.html')
shutil.copy2(output_path, latest_path)
print("latest.html 已更新")
