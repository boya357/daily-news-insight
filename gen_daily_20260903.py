#!/usr/bin/env python3
"""2026年9月3日 每日新闻洞察生成 - 周四"""
import sys, os, shutil, json
WORK_DIR = '/root/daily-news-insight'
sys.path.insert(0, os.path.join(WORK_DIR, 'v3'))
from generators.daily_pro import DailyReportProGenerator

gen = DailyReportProGenerator(
    date_str='2026年9月3日', weekday='星期四',
    subtitle='2026年9月3日 周四 · 美股终结三连跌·博通AI收入指引翻倍·英伟达G20放话万亿美元投入·存储芯片集体回血·美伊冲突升级',
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
        '美股终结三连跌：道指+0.56%、纳指+0.45%、标普+0.46%；AI硬件狂飙，英伟达涨3.21%、美光+2.43%、SK海力士+1.86%，存储芯片集体回血；戴尔科技因AI服务器订单创纪录暴涨15.8%',
        '博通Q3财报炸裂：营收295.91亿（+86%），AI半导体收入167亿（+221%）占比56%；上调2026财年AI收入指引至580亿，2027财年1150亿、2028财年2300亿（两年翻倍）；预计未来两年交付3500亿美元AI半导体产品',
        '黄仁勋G20放话：英伟达今年向美国基础设施投入近万亿美元，AI如同水电等公共基础设施，每个国家都要建设；韩国820万亿韩元主权AI预算落地，SK集团承诺采购2吉瓦Rubin系统',
        '美伊冲突升级：美军完成对伊朗新一轮军事打击（6.5小时），目标包括防空阵地/雷达/海上资产；伊朗击落美军MQ-9无人机并开始回应；WTI原油90.77美元、布伦特95.24美元',
        '今日三大焦点：①博通AI收入指引超预期+英伟达大涨催化AI算力链反弹；②美伊冲突升级→油价上涨→通胀担忧→对A股形成扰动；③央行表态持续宽松，国内政策底明确'
    ],
    operation_advice='周四开盘：美股科技股反弹+博通AI指引炸裂，AI算力链有望高开。但美伊冲突升级推升油价和通胀担忧，叠加A股量能不足，反弹高度受限。操作策略：①英维克关注65-68元压力位，借反弹减仓机动仓；铜冠铜箔关注110-115元压力，产能天花板逻辑未变；雅克科技存储链利好催化但需观察量能；②AI硬件/存储/博通链高开不追高，观察30分钟量能；③美伊冲突升级利好黄金/原油/军工，但不建议追高；④仓位控制5-6成，冲高减仓、回踩再加',
    risk_level='中等偏高',
    suggested_position='5-6成'
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
    description='每日新闻洞察 2026年9月3日：美股终结三连跌、博通AI收入指引两年翻倍、英伟达G20万亿美元投入、存储芯片集体回血、美伊冲突升级',
)

gen.add_global_market()

global_cards1 = render_cards([
    {"name":"道琼斯","change":"+0.56%","up":True},
    {"name":"标普500","change":"+0.46%","up":True},
    {"name":"纳斯达克","change":"+0.45%","up":True},
    {"name":"费城半导体","change":"+0.45%","up":True},
    {"name":"日经225","change":"-0.90%","up":False},
    {"name":"恒生指数","change":"-0.07%","up":False},
])
global_list1 = render_list([
    {"name":"WTI原油","change":"-0.26%/$90.77","up":False},
    {"name":"布伦特原油","change":"-0.40%/$95.24","up":False},
    {"name":"COMEX黄金","change":"+0.42%/$4433.04","up":True},
    {"name":"COMEX白银","change":"+0.70%/$65.92","up":True},
])
global_list2 = render_list([
    {"name":"三星电子","change":"+1.20%","up":True},
    {"name":"SK海力士","change":"+1.86%","up":True},
    {"name":"美光科技","change":"+2.43%","up":True},
    {"name":"台积电ADR","change":"+0.36%","up":True},
])
global_list3 = render_list([
    {"name":"英伟达","change":"+3.21%/$224.41","up":True},
    {"name":"AMD","change":"-0.55%/$457.06","up":False},
    {"name":"微软","change":"-0.84%/$496.82","up":False},
    {"name":"苹果","change":"-0.05%/$324.96","up":False},
    {"name":"博通","change":"-0.66%/$367.24(盘后转涨)","up":False},
    {"name":"英特尔","change":"+1.21%/$90.05","up":True},
    {"name":"应用材料","change":"-0.77%/$438.46","up":False},
    {"name":"阿斯麦","change":"+1.03%/$1682.30","up":True},
])

global_html = '''
<div class="grid md:grid-cols-3 gap-4">
  <div class="md:col-span-2">
    <div class="text-white font-semibold mb-3 flex items-center gap-2"><span>🌍</span><span>隔夜全球市场 · 美股终结三连跌·博通AI指引炸裂·存储芯片集体回血·美伊冲突升级</span></div>
    <div class="grid grid-cols-3 md:grid-cols-6 gap-2">{0}</div>
    <p class="text-xs text-white/50 mt-3 leading-relaxed">
      ⚡ <b class="text-yellow-400">核心要点：美股三大指数集体收涨，终结三连跌。道指+0.56%、纳指+0.45%、标普+0.46%。AI硬件狂飙，英伟达涨3.21%、戴尔暴涨15.8%、美光+2.43%、SK海力士+1.86%。AI软件股暴跌，MongoDB跌超13%。美伊冲突升级。</b>来源：第一财经、华尔街见闻、中国证券报<br>
      ①<b>博通Q3财报炸裂，AI半导体收入指引两年翻倍</b>：<br>
      ·营收295.91亿美元（+86%），AI半导体收入167亿（+221%）占总营收56%<br>
      ·非GAAP EPS 3.32美元（+96%），高于市场预期<br>
      ·Q4指引348亿美元（+93%），略低于预期350.5亿<br>
      ·<b>长期指引炸裂</b>：2026财年AI收入从560亿上调至580亿，2027财年1150亿、2028财年2300亿<br>
      ·已开始向谷歌量产交付下一代TPU 8I，性能与Vera Rubin持平或更优<br>
      ·预计未来两年交付3500亿美元AI半导体产品<br>
      ②<b>英伟达+3.21%，黄仁勋G20放话万亿美元投入</b>：<br>
      ·英伟达CEO在G20科技峰会将AI比作水电等公共基础设施<br>
      ·英伟达今年将向美国基础设施投入近1万亿美元<br>
      ·呼吁政府针对"实际和具体的危害"监管而非"理论假设的危害"<br>
      ③<b>存储芯片集体回血，韩国主权AI投资加码</b>：<br>
      ·美光+2.43%、SK海力士+1.86%、三星+1.20%，存储板块全线反弹<br>
      ·韩国820万亿韩元预算落地，计划到2029年投资9190亿美元建8.4GW数据中心<br>
      ·SK集团承诺采购2吉瓦英伟达Rubin系统<br>
      ·SemiAnalysis：英伟达或已与SK海力士就SOCAMM达成长期协议，锁定2027年HBM定价<br>
      ④<b>美伊冲突升级，地缘风险升温</b>：<br>
      ·美军完成对伊朗新一轮军事打击（持续6.5小时），目标包括防空/雷达/海上资产<br>
      ·伊朗击落美军MQ-9无人机，伊斯兰革命卫队宣布已开始回应<br>
      ·特朗普表示打击不会"持续太久"，但随时准备再打击一次<br>
      ·WTI原油90.77美元（盘中探底回升），布伦特95.24美元<br>
      ⑤<b>经济数据：ADP不及预期，美联储褐皮书显示数据中心驱动增长</b>：<br>
      ·8月ADP新增就业3.7万人，创1月以来新低<br>
      ·美联储褐皮书：经济温和扩张，数据中心需求成为增长主要动力<br>
      ·10年期美债收益率回落至4.78%（盘中最高4.818%）<br>
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
  <div class="bg-gradient-to-br from-red-500/20 to-orange-500/10 border border-red-500/30 rounded-xl p-3 text-center">
    <div class="text-xs text-white/60 mb-1">上证指数</div>
    <div class="text-xl font-bold text-red-400">约3900点</div>
    <div class="text-xs text-red-400">待更新</div>
  </div>
  <div class="bg-gradient-to-br from-red-500/20 to-orange-500/10 border border-red-500/30 rounded-xl p-3 text-center">
    <div class="text-xs text-white/60 mb-1">深证成指</div>
    <div class="text-xl font-bold text-red-400">待更新</div>
    <div class="text-xs text-red-400">--</div>
  </div>
  <div class="bg-gradient-to-br from-red-500/20 to-orange-500/10 border border-red-500/30 rounded-xl p-3 text-center">
    <div class="text-xs text-white/60 mb-1">创业板指</div>
    <div class="text-xl font-bold text-red-400">待更新</div>
    <div class="text-xs text-red-400">--</div>
  </div>
  <div class="bg-gradient-to-br from-red-500/20 to-orange-500/10 border border-red-500/30 rounded-xl p-3 text-center">
    <div class="text-xs text-white/60 mb-1">科创50</div>
    <div class="text-xl font-bold text-red-400">待更新</div>
    <div class="text-xs text-red-400">--</div>
  </div>
</div>

<div class="bg-yellow-500/10 border border-yellow-500/30 rounded-xl p-4">
  <div class="flex items-center gap-2 mb-2">
    <span class="text-yellow-400">⚠️</span>
    <span class="text-yellow-300 font-semibold text-sm">数据说明</span>
  </div>
  <p class="text-xs text-white/60">今日A股行情数据因接口临时故障未能实时获取，将在盘中快报和盘后速递中更新。以下分析基于隔夜外盘和近期市场格局推演。</p>
</div>

<div class="grid md:grid-cols-2 gap-4">
  <div class="bg-white/5 rounded-xl p-4">
    <h4 class="text-white font-semibold mb-3 flex items-center gap-2"><span>📈</span> 今日大概率领涨方向</h4>
    <div class="space-y-1 text-xs">
      <div class="flex justify-between"><span class="text-white/70">AI算力/液冷</span><span class="text-red-400 font-semibold">英伟达+博通催化</span></div>
      <div class="flex justify-between"><span class="text-white/70">存储芯片/HBM</span><span class="text-red-400 font-semibold">美光+海力士大涨</span></div>
      <div class="flex justify-between"><span class="text-white/70">黄金/贵金属</span><span class="text-red-400 font-semibold">金价新高+避险</span></div>
      <div class="flex justify-between"><span class="text-white/70">光模块/光互联</span><span class="text-red-400 font-semibold">博通+英伟达链</span></div>
      <div class="flex justify-between"><span class="text-white/70">军工/国防</span><span class="text-red-400 font-semibold">美伊冲突升级</span></div>
    </div>
  </div>
  <div class="bg-white/5 rounded-xl p-4">
    <h4 class="text-white font-semibold mb-3 flex items-center gap-2"><span>📉</span> 今日承压方向</h4>
    <div class="space-y-1 text-xs">
      <div class="flex justify-between"><span class="text-white/70">AI应用/软件</span><span class="text-green-400 font-semibold">美股AI软件暴跌</span></div>
      <div class="flex justify-between"><span class="text-white/70">消费/出行链</span><span class="text-green-400 font-semibold">油价上涨压制</span></div>
      <div class="flex justify-between"><span class="text-white/70">航空/航运</span><span class="text-green-400 font-semibold">油价上涨成本端</span></div>
      <div class="flex justify-between"><span class="text-white/70">高估值成长</span><span class="text-green-400 font-semibold">美债收益率高位</span></div>
    </div>
  </div>
</div>

<div class="bg-white/5 rounded-xl p-4">
  <h4 class="text-white font-semibold mb-3 flex items-center gap-2"><span>📊</span> 市场概况与今日推演</h4>
  <div class="text-xs text-white/70 space-y-2 leading-relaxed">
    <p><b class="text-white">隔夜外盘正面催化：</b>美股终结三连跌，AI硬件板块大幅反弹（英伟达+3.2%、戴尔+15.8%、美光+2.4%）。博通盘后财报AI收入指引两年翻倍，进一步强化AI基础设施投资逻辑。对A股AI算力链形成正向催化。来源：第一财经、华尔街见闻</p>
    <p><b class="text-yellow-400">地缘风险升温：</b>美伊冲突升级，美军对伊朗发动新一轮军事打击（6.5小时），伊朗击落美军无人机并开始回应。原油价格维持90+美元高位，黄金上涨。通胀担忧+地缘风险或压制风险偏好。来源：央视新闻、新华社</p>
    <p><b class="text-white">国内政策面：</b>央行行长潘功胜表态将持续落实适度宽松货币政策，完善利率体系，持续为经济和A股营造稳定金融环境。国内宽松方向不变，政策底信号明确。来源：微博/财经博主</p>
    <p><b class="text-orange-400">技术面推演：</b>沪指在3850-3950区间震荡，3950-4000为强压力区。今日受外盘提振有望高开，但无量则警惕冲高回落。关注量能能否回到1.9万亿以上。</p>
    <p><b class="text-blue-400">结构特征推演：</b>AI硬件vs AI应用跷跷板效应延续——算力硬件反弹、AI应用调整。存储芯片/光模块/半导体设备受益于英伟达+博通双重催化。黄金/军工因地缘冲突避险需求升温。</p>
  </div>
</div>

<div class="grid md:grid-cols-2 gap-4">
  <div class="bg-yellow-500/10 border border-yellow-500/30 rounded-xl p-4">
    <h4 class="text-yellow-300 font-semibold mb-2 flex items-center gap-2"><span>☀️</span> 今日展望</h4>
    <div class="text-xs text-white/70 space-y-1.5 leading-relaxed">
      <p>· 美股AI硬件反弹+博通AI指引炸裂，算力链有望高开</p>
      <p>· 美伊冲突升级推升油价和通胀，压制风险偏好</p>
      <p>· 央行持续宽松表态，国内政策底明确</p>
      <p>· 关注3900-3950压力位能否放量突破</p>
      <p>· AI硬件/存储/光模块领涨，AI应用/消费承压</p>
    </div>
  </div>
  <div class="bg-blue-500/10 border border-blue-500/30 rounded-xl p-4">
    <h4 class="text-blue-300 font-semibold mb-2 flex items-center gap-2"><span>🎯</span> 今日关注点</h4>
    <div class="text-xs text-white/70 space-y-1.5 leading-relaxed">
      <p>· <b>博通AI指引传导</b>：光模块/交换芯片/博通链开盘反应</p>
      <p>· <b>存储芯片持续性</b>：美光+海力士大涨能否带动A股存储链</p>
      <p>· <b>美伊冲突进展</b>：地缘冲突是否进一步升级</p>
      <p>· <b>量能变化</b>：能否回到1.9万亿以上决定反弹高度</p>
      <p>· <b>北向资金</b>：外资动向观察风险偏好</p>
    </div>
  </div>
</div>
</div>'''
gen.add_section("A股昨日复盘与今日展望", ashare_html, "📊")

# 核心题材与今日催化
topics_html = '''
<div class="space-y-4">

<div class="bg-gradient-to-br from-red-500/10 to-orange-500/5 border border-red-500/30 rounded-xl p-4">
  <h4 class="text-red-400 font-bold mb-3 flex items-center gap-2"><span class="text-lg">🔴</span> S级催化 · 博通AI指引翻倍/英伟达G20万亿投入/存储反弹</h4>
  <div class="space-y-3 text-xs text-white/70 leading-relaxed">
    <div class="bg-white/5 rounded-lg p-3">
      <p class="text-white font-semibold mb-1">🚀 博通Q3财报炸裂：AI半导体收入指引两年翻倍至2300亿</p>
      <p>博通第三财季营收295.91亿美元（+86%），AI半导体收入167亿美元（+221%），占总营收56%。更重磅的是长期指引：2026财年AI收入从560亿上调至580亿，2027财年1150亿、2028财年达2300亿美元（两年翻倍）。已开始向谷歌量产下一代TPU 8I，Q4加快向Anthropic交付Ironwood芯片，大规模量产Meta定制版MTIA。预计未来两年交付约3500亿美元AI半导体产品。来源：华尔街见闻、中国证券报</p>
      <p class="text-yellow-400 mt-2">影响链条：博通ASIC→光模块/高速互联→定制AI芯片→交换芯片→HBM/存储→先进封装</p>
      <p class="text-orange-400">相关标的：中际旭创、天孚通信（光模块）、胜宏科技/沪电股份（PCB）、雅克科技（前驱体）、长电科技（先进封装）</p>
    </div>
    <div class="bg-white/5 rounded-lg p-3">
      <p class="text-white font-semibold mb-1">💎 存储芯片集体回血，韩国主权AI投资加码</p>
      <p>美光科技+2.43%、SK海力士+1.86%、三星电子+1.20%，存储板块全线反弹。韩国820万亿韩元预算落地，计划到2029年投资9190亿美元建成8.4GW数据中心算力，SK集团承诺采购2吉瓦英伟达Rubin系统。SemiAnalysis认为英伟达或已与SK海力士就SOCAMM达成长期协议。SK海力士拟深化与铠侠合作，考虑在日本建设NAND芯片工厂。来源：华尔街见闻</p>
      <p class="text-yellow-400">存储产业链：HBM＞DDR5/NAND＞高端铜箔/ABF/封装材料＞存储设备</p>
      <p class="text-orange-400">相关标的：雅克科技（HBM前驱体）、华海诚科（HBM环氧塑封料）、铜冠铜箔（高端铜箔）、长电科技（先进封装）、北方华创/中微公司（设备）</p>
    </div>
    <div class="bg-white/5 rounded-lg p-3">
      <p class="text-white font-semibold mb-1">⚡ 英伟达G20放话：今年投入近万亿美元，AI如同水电基础设施</p>
      <p>黄仁勋在美国主办的G20科技峰会上表示，英伟达仅今年就将向美国基础设施投入近1万亿美元。将AI比作水电等公共基础设施、称之为"最大的均衡器"，强调每个国家都需要建设基础设施。特朗普政府正借峰会推动"卡罗来纳原则"轻监管AI治理框架。来源：华尔街见闻</p>
      <p class="text-yellow-400">算力基础设施：GPU/AI服务器→液冷散热→光互联→电力供应→数据中心建设</p>
      <p class="text-orange-400">相关标的：英维克（液冷）、工业富联（AI服务器）、中际旭创（光模块）、科华数据（IDC）</p>
    </div>
  </div>
</div>

<div class="bg-gradient-to-br from-yellow-500/10 to-amber-500/5 border border-yellow-500/30 rounded-xl p-4">
  <h4 class="text-yellow-400 font-bold mb-3 flex items-center gap-2"><span class="text-lg">🟡</span> A级催化 · 美伊冲突升级/液冷产业大会/谷歌Gemini迭代</h4>
  <div class="space-y-3 text-xs text-white/70 leading-relaxed">
    <div class="bg-white/5 rounded-lg p-3">
      <p class="text-white font-semibold mb-1">⚔️ 美伊冲突升级，地缘风险推升油价金价</p>
      <p>美军中央司令部完成对伊朗新一轮军事打击（持续6.5小时），目标包括防空阵地、雷达系统、海上资产、布雷能力和通信站点。伊朗伊斯兰革命卫队宣布已开始回应美方袭击，击落一架美军MQ-9无人机。特朗普表示打击不会"持续太久"但随时准备再打击。WTI原油90.77美元、布伦特95.24美元，COMEX黄金4433美元（+0.42%）。来源：央视新闻、第一财经</p>
      <p class="text-red-400">影响：油价上涨→通胀压力→美债收益率上行→风险资产承压；黄金/军工/石油受益</p>
    </div>
    <div class="bg-white/5 rounded-lg p-3">
      <p class="text-white font-semibold mb-1">🧊 第三届中国国际液冷技术创新论坛9月10-11日上海召开</p>
      <p>2026年9月10-11日第三届中国国际液冷技术创新发展论坛将在上海召开，汇聚产业链头部企业。中国信通院数据显示，2026年中国液冷市场规模预计达716亿元，同比增长超70%，AI训练服务器液冷渗透率高达74%。工信部规定2026年新建数据中心液冷渗透率不低于60%。来源：搜狐财经</p>
      <p class="text-blue-400">关注：英维克、高澜股份、申菱环境、曙光数创等液冷龙头会前催化</p>
    </div>
    <div class="bg-white/5 rounded-lg p-3">
      <p class="text-white font-semibold mb-1">🤖 谷歌发布Gemini 3.8 Flash，六周内第三次迭代</p>
      <p>谷歌发布Gemini 3.8 Flash及网络安全版Flash Cyber，距3.7 Flash仅三周。3.8 Flash主打长周期软件工程与自主智能体，网安版生成正确补丁数量是规模更大商业模型的2.6倍。650多家政府与关键基础设施机构获网安AI优先通道。来源：华尔街见闻</p>
    </div>
    <div class="bg-white/5 rounded-lg p-3">
      <p class="text-white font-semibold mb-1">🏦 央行表态持续宽松，政策底明确</p>
      <p>央行行长潘功胜公开表态：将持续落实适度宽松的货币政策，完善利率体系，持续为经济和A股营造稳定的金融环境。7月油价低位时累计放水8000亿托底市场，8月油价冲高缩量至1000亿维稳。来源：微博/财经博主</p>
    </div>
  </div>
</div>

<div class="bg-gradient-to-br from-green-500/10 to-emerald-500/5 border border-green-500/30 rounded-xl p-4">
  <h4 class="text-green-400 font-bold mb-3 flex items-center gap-2"><span class="text-lg">🟢</span> B级关注 · 戴尔暴涨/Snowflake超预期/谷歌投资</h4>
  <div class="space-y-3 text-xs text-white/70 leading-relaxed">
    <div class="bg-white/5 rounded-lg p-3">
      <p class="text-white font-semibold mb-1">🖥️ 戴尔科技暴涨15.8%，AI服务器订单创纪录</p>
      <p>戴尔二季度非GAAP盈利与营收双双超预期，同时上调2027财年业绩指引。AI服务器需求爆发，订单创纪录。印证AI算力基础设施投资持续高景气。来源：第一财经</p>
    </div>
    <div class="bg-white/5 rounded-lg p-3">
      <p class="text-white font-semibold mb-1">❄️ Snowflake盘后大涨22%，业绩与指引全面超预期</p>
      <p>AI数据云龙头Snowflake二季度营收15.5亿美元（+35%），产品收入14.9亿（+37%）连续三个季度加速。上调2027财年产品收入指引至60.7亿，CFO称AI收入出现"显著跃升"。来源：中国证券报</p>
    </div>
    <div class="bg-white/5 rounded-lg p-3">
      <p class="text-white font-semibold mb-1">💰 伯克希尔15个月前以100亿美元投资谷歌获6.5%折扣</p>
      <p>伯克希尔CEO阿贝尔披露，巴菲特参与了投资决策，AI数据中心带来的电力需求正成为公司能源业务的新机遇。能源+AI算力的结合正在成为新的投资方向。来源：华尔街见闻</p>
    </div>
  </div>
</div>

</div>'''
gen.add_section("核心题材与今日催化", topics_html, "🔥")

# 持仓诊断
holdings_html = '''
<div class="space-y-4">
<div class="grid md:grid-cols-2 gap-4">

  <div class="bg-gradient-to-br from-amber-500/10 to-yellow-500/5 border border-amber-500/40 rounded-xl p-4">
    <div class="flex items-center justify-between mb-2">
      <h4 class="text-amber-400 font-bold flex items-center gap-2"><span>💼</span> 英维克（002837）</h4>
      <span class="text-xs bg-amber-500/20 text-amber-400 px-2 py-0.5 rounded-full">液冷散热龙头</span>
    </div>
    <div class="flex items-end gap-3 mb-2">
      <span class="text-2xl font-bold text-white">65.97</span>
      <span class="text-sm text-red-400 font-semibold">+3.05%</span>
      <span class="text-xs text-white/40">(8月26日数据)</span>
    </div>
    <div class="text-xs text-white/70 space-y-1.5 leading-relaxed">
      <p><b class="text-white">基本面：</b>液冷散热龙头，AI算力液冷渗透率持续提升。工信部规定2026年新建数据中心液冷渗透率不低于60%。</p>
      <p><b class="text-green-400">利好催化：</b>①英伟达+3.21%+黄仁勋G20万亿投入→AI算力建设加速→液冷需求增长；②第三届中国国际液冷技术创新论坛9月10-11日上海召开，会前催化；③Vera Rubin功耗更高（2300W），液冷刚需更强。</p>
      <p><b class="text-red-400">风险点：</b>净利下滑说明价格战/毛利率承压；板块轮动较快；浮亏较深。</p>
      <p><b class="text-yellow-400">操作建议：</b>持有观察，压力位65-68元，强压力70元，支撑位60元。英伟达+液冷大会双重催化下若放量突破68元可加仓，否则逢高减仓机动仓位，保护底仓。</p>
    </div>
  </div>

  <div class="bg-gradient-to-br from-amber-500/10 to-yellow-500/5 border border-amber-500/40 rounded-xl p-4">
    <div class="flex items-center justify-between mb-2">
      <h4 class="text-amber-400 font-bold flex items-center gap-2"><span>💼</span> 铜冠铜箔（301217）</h4>
      <span class="text-xs bg-amber-500/20 text-amber-400 px-2 py-0.5 rounded-full">AI铜箔/锂电铜箔</span>
    </div>
    <div class="flex items-end gap-3 mb-2">
      <span class="text-2xl font-bold text-white">114.53</span>
      <span class="text-sm text-green-400 font-semibold">-2.45%</span>
      <span class="text-xs text-white/40">(8月26日数据)</span>
    </div>
    <div class="text-xs text-white/70 space-y-1.5 leading-relaxed">
      <p><b class="text-white">基本面：</b>半年报净利+514.75%但Q2环比仅+2%，低基数效应明显。产能8万吨/年已到天花板，暂无扩产计划。</p>
      <p><b class="text-green-400">利好催化：</b>存储芯片板块反弹→AI服务器高端铜箔需求预期改善；MSCI纳入带来被动资金。</p>
      <p><b class="text-red-400">风险点：</b>Q2环比停滞，产能天花板隐忧，行业扩产潮中掉队风险；年内涨幅已超214%，估值偏高；利好出尽后短期回调压力大。</p>
      <p><b class="text-yellow-400">操作建议：</b>半年报利好出尽，产能天花板逻辑未变。借存储板块反弹逢高减仓机动仓。支撑位100-105元，压力位115-120元。底仓持有，机动仓位逢高减仓，待回调至100元附近再加仓。</p>
    </div>
  </div>

  <div class="bg-gradient-to-br from-amber-500/10 to-yellow-500/5 border border-amber-500/40 rounded-xl p-4">
    <div class="flex items-center justify-between mb-2">
      <h4 class="text-amber-400 font-bold flex items-center gap-2"><span>💼</span> 雅克科技（002409）</h4>
      <span class="text-xs bg-amber-500/20 text-amber-400 px-2 py-0.5 rounded-full">半导体材料平台</span>
    </div>
    <div class="flex items-end gap-3 mb-2">
      <span class="text-2xl font-bold text-white">143.91</span>
      <span class="text-sm text-green-400 font-semibold">-1.43%</span>
      <span class="text-xs text-white/40">(8月26日数据)</span>
    </div>
    <div class="text-xs text-white/70 space-y-1.5 leading-relaxed">
      <p><b class="text-white">基本面：</b>半年报归母净利润5.61亿（+7.29%），Q2单季净利同比+12.08%。半导体前驱体全球前三，光刻胶/电子特气/硅微粉多业务布局。</p>
      <p><b class="text-green-400">利好催化：</b>①美光+2.43%、SK海力士+1.86%，存储芯片集体回血→HBM需求预期改善→前驱体需求增长；②博通AI收入指引翻倍→AI算力链整体景气度提升；③韩国主权AI投资加码→HBM需求增量。</p>
      <p><b class="text-red-400">风险点：</b>净利增速偏低（+7%）与高估值不匹配；股东户数大增，筹码分散；板块轮动快。</p>
      <p><b class="text-yellow-400">操作建议：</b>底仓持有，存储板块反弹催化下关注150元压力位。若能反弹至150-160元可减仓机动仓。真正击球区115-120元。</p>
    </div>
  </div>

  <div class="bg-gradient-to-br from-amber-500/10 to-yellow-500/5 border border-amber-500/40 rounded-xl p-4">
    <div class="flex items-center justify-between mb-2">
      <h4 class="text-amber-400 font-bold flex items-center gap-2"><span>💼</span> *ST建艺（002789）</h4>
      <span class="text-xs bg-red-500/20 text-red-400 px-2 py-0.5 rounded-full">ST摘帽预期</span>
    </div>
    <div class="flex items-end gap-3 mb-2">
      <span class="text-2xl font-bold text-white">10.15</span>
      <span class="text-sm text-red-400 font-semibold">+0.68%</span>
      <span class="text-xs text-white/40">(8月26日数据)</span>
    </div>
    <div class="text-xs text-white/70 space-y-1.5 leading-relaxed">
      <p><b class="text-white">基本面：</b>建筑装饰+新能源业务双轮驱动，ST摘帽预期标的。</p>
      <p><b class="text-green-400">利好催化：</b>若摘帽成功将迎来估值修复；基建政策持续发力。</p>
      <p><b class="text-red-400">风险点：</b>ST股流动性差、波动大；摘帽时间不确定。</p>
      <p><b class="text-yellow-400">操作建议：</b>小仓位博弈，严格止损。支撑位9.5元，压力位11元。</p>
    </div>
  </div>

</div>

<div class="bg-white/5 rounded-xl p-4">
  <h4 class="text-white font-semibold mb-3 flex items-center gap-2"><span>📊</span> 持仓组合诊断</h4>
  <div class="grid md:grid-cols-3 gap-3 text-xs">
    <div class="bg-gradient-to-br from-blue-500/10 to-cyan-500/5 border border-blue-500/20 rounded-lg p-3">
      <div class="text-white/60 mb-1">组合仓位</div>
      <div class="text-lg font-bold text-white">5-6成</div>
      <div class="text-blue-400">中等仓位，灵活应对</div>
    </div>
    <div class="bg-gradient-to-br from-purple-500/10 to-pink-500/5 border border-purple-500/20 rounded-lg p-3">
      <div class="text-white/60 mb-1">风格偏向</div>
      <div class="text-lg font-bold text-white">科技成长</div>
      <div class="text-purple-400">AI算力链+半导体材料</div>
    </div>
    <div class="bg-gradient-to-br from-orange-500/10 to-red-500/5 border border-orange-500/20 rounded-lg p-3">
      <div class="text-white/60 mb-1">风险等级</div>
      <div class="text-lg font-bold text-white">中等偏高</div>
      <div class="text-orange-400">科技股波动大，注意风控</div>
    </div>
  </div>
  <div class="mt-3 text-xs text-white/70 leading-relaxed">
    <p><b class="text-white">组合诊断：</b>持仓4只全部集中在AI算力产业链（液冷/铜箔/半导体材料），Beta属性强，与科技板块高度绑定。今日英伟达+博通+存储多重催化，有望迎来反弹。但需警惕：①美伊冲突升级压制风险偏好；②"利好出尽"效应；③A股量能不足。建议：①借反弹减仓铜冠铜箔机动仓（产能天花板+涨幅已大）；②英维克和雅克科技底仓持有，关注68元/150元压力位；③整体仓位控制5-6成，冲高减仓、回踩再加；④关注美伊冲突进展，若进一步升级则降低仓位。</p>
  </div>
</div>
</div>'''
gen.add_section("持仓诊断与操作建议", holdings_html, "💼")

# 空方视角
bear_html = '''
<div class="space-y-4">
<div class="bg-gradient-to-br from-green-500/10 to-emerald-500/5 border border-green-500/30 rounded-xl p-4">
  <h4 class="text-green-400 font-bold mb-3 flex items-center gap-2"><span>🐻</span> 空方视角：四大风险不容忽视</h4>
  <div class="space-y-3 text-xs text-white/70 leading-relaxed">

    <div class="bg-white/5 rounded-lg p-3 border-l-2 border-green-500/50">
      <p class="text-white font-semibold mb-1">风险一：AI硬件反弹是真反转还是死猫跳？</p>
      <p>美股科技股连续三天下跌后反弹，博通财报虽然炸裂但盘后一度跌超6%才转涨，说明市场对AI高估值已有分歧。英伟达涨3.21%很大程度上是超跌反弹（连续下跌后），而非新一轮上涨的开始。A股AI算力链经历了多轮调整后，套牢盘众多，高开后容易遭遇解套盘抛压。</p>
      <p class="text-green-400">应对：高开不追高，观察30分钟-1小时量能变化，无量冲高则减仓。</p>
    </div>

    <div class="bg-white/5 rounded-lg p-3 border-l-2 border-green-500/50">
      <p class="text-white font-semibold mb-1">风险二：美伊冲突升级→油价上涨→通胀回升→加息担忧</p>
      <p>美军对伊朗发动新一轮军事打击（6.5小时），伊朗击落美军无人机并开始回应。特朗普虽表示打击不会持续太久，但随时准备再打击。冲突升级推高油价（WTI 90+美元），而油价是通胀的重要组成部分。若油价持续上涨，将加剧通胀压力，倒逼美联储维持高利率甚至加息，对全球风险资产形成压制。</p>
      <p class="text-green-400">应对：关注美伊冲突进展和油价走势，若油价突破95美元则需警惕通胀预期升温。</p>
    </div>

    <div class="bg-white/5 rounded-lg p-3 border-l-2 border-green-500/50">
      <p class="text-white font-semibold mb-1">风险三：美银警告——美股仅剩约90亿美元买盘空间</p>
      <p>美银策略师测算显示，系统性策略在市场上涨情景下仅余约90亿美元净买入空间，持平情景转为净卖出，下跌情景下CTA与波动率控制策略抛售规模可能高达1630亿美元。企业回购支撑也在9月静默期快速消退，波动率控制策略的股票仓位已达第100百分位历史最高。野村策略师警告"史诗级"波动率崩塌可能伴随重大交易损失。来源：华尔街见闻</p>
      <p class="text-green-400">应对：美股上涨空间有限，A股难以独善其身，保持谨慎仓位。</p>
    </div>

    <div class="bg-white/5 rounded-lg p-3 border-l-2 border-green-500/50">
      <p class="text-white font-semibold mb-1">风险四：持仓股高位利好兑现压力</p>
      <p>铜冠铜箔产能天花板已现（8万吨/年，暂无扩产计划），Q2环比仅+2%，增长停滞信号明确。雅克科技半年报净利仅+7.29%，与高估值不匹配。英维克净利下滑，价格战压力显现。三只科技持仓均面临"高位+增速放缓+估值偏高"的组合，任何利空都可能引发回调。</p>
      <p class="text-green-400">应对：借反弹分批减仓高位股，保护利润，不要等利润回吐再行动。</p>
    </div>

  </div>
</div>

<div class="bg-white/5 rounded-xl p-4">
  <h4 class="text-white font-semibold mb-3 flex items-center gap-2"><span>⚔️</span> 多空博弈与关键点位</h4>
  <div class="grid md:grid-cols-2 gap-4 text-xs">
    <div class="bg-red-500/5 border border-red-500/20 rounded-lg p-3">
      <p class="text-red-400 font-semibold mb-2">多方论据</p>
      <ul class="text-white/70 space-y-1 list-disc pl-4">
        <li>博通AI收入指引两年翻倍，AI基础设施景气度再验证</li>
        <li>英伟达+3.21%+黄仁勋G20万亿投入，算力链催化密集</li>
        <li>存储芯片集体回血，美光+2.43%、海力士+1.86%</li>
        <li>央行持续宽松表态，国内政策底明确</li>
        <li>韩国820万亿韩元主权AI投资，需求增量可观</li>
        <li>美股终结三连跌，短期恐慌情绪缓解</li>
      </ul>
    </div>
    <div class="bg-green-500/5 border border-green-500/20 rounded-lg p-3">
      <p class="text-green-400 font-semibold mb-2">空方论据</p>
      <ul class="text-white/70 space-y-1 list-disc pl-4">
        <li>美伊冲突升级，地缘风险推升油价和通胀</li>
        <li>美股仅剩90亿美元买盘空间，上涨动能有限</li>
        <li>AI应用股暴跌（MongoDB -13%），AI板块内部分化</li>
        <li>博通盘后一度跌6%，市场对高估值有分歧</li>
        <li>A股量能不足，3900-4000点压力重重</li>
        <li>持仓股高位+增速放缓，利好兑现压力大</li>
      </ul>
    </div>
  </div>
  <div class="mt-3 text-xs text-white/70">
    <p><b class="text-yellow-400">关键点位：</b>支撑位3880/3850，压力位3920/3950/4000。若今日放量突破3950且成交额回到2万亿以上，可看高一线；若无量冲高回落跌破3880，则需警惕短期调整。</p>
  </div>
</div>
</div>'''
gen.add_section("空方视角与多空博弈", bear_html, "⚖️")

# 预判验证闭环
prediction_html = '''
<div class="space-y-4">
<div class="bg-white/5 rounded-xl p-4">
  <h4 class="text-white font-semibold mb-3 flex items-center gap-2"><span>🔮</span> 预判验证闭环</h4>
  <div class="text-xs text-white/70 space-y-3 leading-relaxed">

    <div class="bg-green-500/10 border border-green-500/30 rounded-lg p-3">
      <div class="flex items-center justify-between mb-2">
        <span class="text-green-400 font-semibold">✅ 已到期预判验证</span>
        <span class="text-xs bg-green-500/20 text-green-400 px-2 py-0.5 rounded">T+5验证</span>
      </div>
      <div class="space-y-2">
        <div class="bg-white/5 rounded p-2">
          <p><b>预判2（8月27日）：</b>铜冠铜箔半年报利好出尽，Q2环比仅+2%+产能天花板，短期将回调至100-102元支撑区间。</p>
          <p class="text-yellow-300">验证时点：T+5（9月2日）观察股价走势</p>
          <p class="text-orange-400">验证结果：待确认（8月26日收盘价114.53元，今日盘后验证9月2日实际走势）</p>
        </div>
        <div class="bg-white/5 rounded p-2">
          <p><b>预判3（8月27日）：</b>沪指3912-3950区间压力较大，无量难突破，短期将在3850-3950区间震荡整理。</p>
          <p class="text-yellow-300">验证时点：T+5（9月2日）观察指数运行区间</p>
          <p class="text-orange-400">验证结果：待确认（因行情数据接口故障，今日盘后验证）</p>
        </div>
      </div>
    </div>

    <div class="bg-yellow-500/10 border border-yellow-500/30 rounded-lg p-3">
      <div class="flex items-center justify-between mb-2">
        <span class="text-yellow-400 font-semibold">📌 新预判记录（本期新增）</span>
        <span class="text-xs bg-yellow-500/20 text-yellow-400 px-2 py-0.5 rounded">待验证</span>
      </div>
      <div class="space-y-2">
        <div class="bg-white/5 rounded p-2">
          <p><b>预判1：</b>博通AI收入指引两年翻倍（2028年2300亿）将强化AI基础设施投资逻辑，光模块/高速互联/存储链受益，A股AI算力链将迎来一波反弹，持续时间约3-5天。</p>
          <p class="text-yellow-300">验证时点：T+3（9月8日）观察反弹持续性</p>
        </div>
        <div class="bg-white/5 rounded p-2">
          <p><b>预判2：</b>美伊冲突升级将推高油价至95美元以上，通胀预期升温导致美债收益率维持高位，对A股科技成长股形成压制，沪指难以有效突破4000点。</p>
          <p class="text-yellow-300">验证时点：T+5（9月10日）观察油价和指数走势</p>
        </div>
        <div class="bg-white/5 rounded p-2">
          <p><b>预判3：</b>9月10-11日上海液冷技术论坛召开前，液冷板块将有会前催化行情，英维克等液冷龙头有望提前启动。</p>
          <p class="text-yellow-300">验证时点：T+5（9月10日）观察液冷板块表现</p>
        </div>
        <div class="bg-white/5 rounded p-2">
          <p><b>预判4：</b>存储芯片超级周期逻辑持续强化（韩国820万亿韩元AI投资+博通AI指引翻倍），美光/SK海力士中期仍有上行空间，A股存储链调整后将再创高点。</p>
          <p class="text-yellow-300">验证时点：T+10（9月17日）中期验证</p>
        </div>
      </div>
    </div>

    <div class="bg-blue-500/10 border border-blue-500/30 rounded-lg p-3">
      <div class="flex items-center justify-between mb-2">
        <span class="text-blue-400 font-semibold">📊 历史预判验证汇总</span>
        <span class="text-xs bg-blue-500/20 text-blue-400 px-2 py-0.5 rounded">持续跟踪</span>
      </div>
      <p class="text-white/60 text-xs mb-2">完整预判验证数据见「预判验证中心」页面</p>
      <div class="grid grid-cols-4 gap-2 text-center">
        <div class="bg-white/5 rounded-lg p-2">
          <div class="text-lg font-bold text-green-400">--</div>
          <div class="text-xs text-white/60">正确</div>
        </div>
        <div class="bg-white/5 rounded-lg p-2">
          <div class="text-lg font-bold text-red-400">--</div>
          <div class="text-xs text-white/60">错误</div>
        </div>
        <div class="bg-white/5 rounded-lg p-2">
          <div class="text-lg font-bold text-yellow-400">--</div>
          <div class="text-xs text-white/60">待验证</div>
        </div>
        <div class="bg-white/5 rounded-lg p-2">
          <div class="text-lg font-bold text-blue-400">--</div>
          <div class="text-xs text-white/60">准确率</div>
        </div>
      </div>
    </div>

  </div>
</div>
</div>'''
gen.add_section("预判验证闭环", prediction_html, "🔮")

# 教训库引用
lesson_html = '''
<div class="space-y-4">
<div class="bg-white/5 rounded-xl p-4">
  <h4 class="text-white font-semibold mb-3 flex items-center gap-2"><span>📚</span> 教训库引用</h4>
  <div class="space-y-3 text-xs text-white/70 leading-relaxed">

    <div class="bg-orange-500/10 border border-orange-500/30 rounded-lg p-3">
      <p class="text-orange-400 font-semibold mb-2">💡 教训1：利好出尽是利空——财报季的经典陷阱</p>
      <p><b>历史教训：</b>每次英伟达/博通/苹果等科技巨头财报超预期后，股价经常出现"利好兑现"式回调。原因是财报前预期已经炒高，利好落地后获利盘出逃。博通今日盘后一度跌超6%才转涨，说明市场分歧加大。</p>
      <p><b>本次启示：</b>不要因为"博通指引翻倍""英伟达涨3%"就冲动追高。先观察30分钟-1小时量能和持续性，无量高开就是陷阱。历史上AI硬件的财报行情，高开低走的概率远高于持续上涨。</p>
    </div>

    <div class="bg-orange-500/10 border border-orange-500/30 rounded-lg p-3">
      <p class="text-orange-400 font-semibold mb-2">💡 教训2：地缘冲突——黑天鹅的温床</p>
      <p><b>历史教训：</b>中东冲突、俄乌战争等地缘事件往往引发市场剧烈波动。2024-2025年多次出现"周末地缘冲突→周一A股大跌"的模式。油价上涨→通胀回升→加息预期→风险资产下跌，这条传导链条屡试不爽。</p>
      <p><b>本次启示：</b>美伊冲突升级是当前最大的不确定性。美军打击伊朗6.5小时，伊朗已开始回应。若冲突进一步升级（如封锁霍尔木兹海峡），油价可能飙升至100+美元，对全球股市形成重大冲击。保持谨慎仓位，不要忽视地缘风险。</p>
    </div>

    <div class="bg-orange-500/10 border border-orange-500/30 rounded-lg p-3">
      <p class="text-orange-400 font-semibold mb-2">💡 教训3：高位股逢高分批减仓，不要等利润回吐</p>
      <p><b>历史教训：</b>铜冠铜箔年内涨幅已超200%、雅克科技从底部涨近5倍。历史经验表明，涨幅超过200%的股票，一旦进入调整期，回撤幅度往往达到30-50%。很多投资者因为"还会涨"的执念，从盈利50%拿到亏损20%。</p>
      <p><b>本次启示：</b>严格执行"高位股逢高分批减仓"纪律。借博通+英伟达利好反弹之机，减仓铜冠铜箔和雅克科技的机动仓位，保护利润。底仓保留、机动仓位获利了结，是牛市中期的正确姿势。</p>
    </div>

    <div class="bg-orange-500/10 border border-orange-500/30 rounded-lg p-3">
      <p class="text-orange-400 font-semibold mb-2">💡 教训4：美银"90亿美元买盘"警告——市场顶部信号</p>
      <p><b>历史教训：</b>当系统性策略（CTA、波动率控制、风险平价）的仓位达到历史极值时，往往意味着市场处于顶部区域。一旦风向逆转，这些策略会从"净买入"转为"净卖出"，形成踩踏。2025年多次出现类似信号后市场大幅回调。</p>
      <p><b>本次启示：</b>美银测算美股仅剩约90亿美元买盘空间，波动率控制策略仓位已达第100百分位历史最高。这是一个重要的顶部信号。A股虽然不完全同步，但美股下跌必然带来跟跌压力。保持5-6成仓位，不要满仓。</p>
    </div>

  </div>
</div>
</div>'''
gen.add_section("教训库引用", lesson_html, "📚")

# 添加重要新闻汇总
gen.add_important_news()

# 发布
output_path = os.path.join(WORK_DIR, "docs/daily/20260903_每日新闻洞察.html")
result = gen.publish(output_path=output_path)
print("发布结果:", result)
print(f"文件大小: {result.get('file_size', 0)} 字节")
print(f"输出路径: {result.get('output_path', '')}")
