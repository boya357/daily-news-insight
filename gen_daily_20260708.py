#!/usr/bin/env python3
"""2026年7月8日 每日新闻洞察生成 - 周三·费半-4.65%半导体血洗·韩股两度熔断·中东油价暴涨6%"""
import sys, os
WORK_DIR = '/root/daily-news-insight'
sys.path.insert(0, os.path.join(WORK_DIR, 'v3'))
from generators.daily_pro import DailyReportProGenerator

gen = DailyReportProGenerator(
    date_str='2026年7月8日', weekday='星期三',
    subtitle='2026年7月8日 星期三 · 费半-4.65%半导体血洗/韩股两度熔断/三星1810%利好兑现杀跌 · 中东战火重启油价+6% · 黄金跳水-1.5%/4104美元 · *ST建艺10%跌停 · 大基金减持沪硅产业 · 持仓承压日',
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
global_cards1 = render_cards([
    {"name":"道琼斯","change":"-0.25%","up":False},
    {"name":"标普500","change":"-0.45%","up":False},
    {"name":"纳斯达克","change":"-1.16%","up":False},
    {"name":"纳指100","change":"-1.77%","up":False},
    {"name":"费半SOX","change":"-4.65%","up":False},
    {"name":"存储概念","change":"-5.45%","up":False},
])
global_list1 = render_list([
    {"name":"WTI原油","change":"+2.76%/70.44","up":True},
    {"name":"布伦特原油","change":"+3.01%/74.16","up":True},
    {"name":"现货黄金","change":"-1.47%/4104","up":False},
    {"name":"现货白银","change":"-3.38%/59.96","up":False},
    {"name":"美元指数","change":"+0.20%/101.06","up":True},
    {"name":"离岸人民币","change":"-93bp/6.8035","up":False},
])
global_list2 = render_list([
    {"name":"KOSPI指数","change":"-4.91%","up":False},
    {"name":"三星电子","change":"-9%+","up":False},
    {"name":"SK海力士","change":"-10%+","up":False},
    {"name":"日经225","change":"-2%+","up":False},
])
global_html = '''
<div class="grid md:grid-cols-3 gap-4">
  <div class="md:col-span-2">
    <div class="text-white font-semibold mb-3 flex items-center gap-2"><span>🌍</span><span>隔夜全球市场 · 半导体血洗·费半-4.65%·韩股两度熔断·中东战火重启</span></div>
    <div class="grid grid-cols-3 md:grid-cols-6 gap-2">{0}</div>
    <p class="text-xs text-white/50 mt-3 leading-relaxed">
      ⚡ <b class="text-yellow-400">核心要点：全球半导体抛售潮+中东地缘风险双杀</b>——隔夜全球市场风险偏好骤降：
      ①<b>美股三大指数高开低走集体收跌</b>：道指-0.25%（早盘创历史新高后回落）、标普500-0.45%、纳指-1.16%、纳指100-1.77%，科技权重是主要拖累；
      ②<b class="text-green-400">费城半导体指数单日暴跌4.65%，盘中最大跌幅逼近7%</b>，为近一个月最大单日跌幅。存储概念大跌5.45%：闪迪-11%+、西部数据-9%+、美光-4.71%、希捷-7%+；通用芯片：英特尔-9.66%、AMD-6.51%、Arm-6%+；设备：应用材料/泛林-8%+；光通信：Coherent/Lumentum/Credo同步大跌。<b>AI七姐妹内部分化</b>：Meta+2%逆势收红、微软收红、英伟达逆市收涨0.71%（期权市场看涨押注升温）、特斯拉-4.02%；
      ③<b class="text-red-400">韩股两度熔断</b>：KOSPI周二盘中暴跌8.03%触发全市场熔断20分钟，收盘-4.91%，三星电子-9%+、SK海力士-10%+。周三开盘再跌3%（三星/SK海力士再跌4%）。导火索：<b>三星Q2营业利润89.4万亿韩元同比+1810%创历史新高，但"利好兑现"资金获利了结</b>，市场担忧存储涨价周期见顶；
      ④<b class="text-red-400">中东战火重启</b>：美军中央司令部宣布对伊朗发动"一系列强力打击"（回应霍尔木兹海峡袭船），美国财政部撤销伊朗石油销售豁免，<b>布油一度暴涨6%突破76美元/桶</b>，WTI涨5.3%至72.15美元；
      ⑤<b>黄金跳水</b>：现货黄金-1.47%至4104美元/盎司，白银-3.38%破60美元，美元指数+0.2%至101.06，离岸人民币跌93点至6.8035；
      ⑥<b>美债收益率飙升</b>：10年期美债收益率涨6.78bp至4.537%，30年期破5%，通胀预期升温+油价上涨双重打压。
      <br><b class="text-yellow-400">A股影响解读：</b>今日半导体/算力/存储板块承压最大，但<b>内资主导的人形机器人、中报业绩线、油服/黄金避险、防御板块</b>可能成为资金避风港。沪指4000点关口面临考验，3970为中期强支撑。<b>操作策略：不恐慌割肉、不抄底半导体，等情绪释放后择优加仓业绩确定性主线</b>。
    </p>
  </div>
  <div class="space-y-4">
    <div>
    <div class="text-white font-semibold mb-3 flex items-center gap-2"><span>🛢️</span><span>大宗商品（油价暴涨·黄金跳水）</span></div>
      <div class="bg-white/5 rounded-lg p-3">{1}</div></div>
    <div>
    <div class="text-white font-semibold mb-3 flex items-center gap-2"><span>🇰🇷</span><span>韩股核心（半导体暴跌）</span></div>
      <div class="bg-white/5 rounded-lg p-3">{2}</div></div>
  </div>
</div>'''.format(global_cards1, global_list1, global_list2)
gen.add_section("隔夜全球市场·半导体血洗", global_html, "🌍")

# ========== 2. 昨日A股复盘 ==========
ashare_html = '''
<div class="space-y-4">
<div class="grid md:grid-cols-4 gap-3">
  <div class="bg-gradient-to-br from-green-500/20 to-emerald-500/10 border border-green-500/30 rounded-xl p-3 text-center">
    <div class="text-xs text-white/60 mb-1">上证指数</div>
    <div class="text-xl font-bold text-green-400">3972.15</div>
    <div class="text-xs text-green-400 mt-1">-1.75% / 失守4000</div>
  </div>
  <div class="bg-gradient-to-br from-green-500/20 to-emerald-500/10 border border-green-500/30 rounded-xl p-3 text-center">
    <div class="text-xs text-white/60 mb-1">深证成指</div>
    <div class="text-xl font-bold text-green-400">15034.22</div>
    <div class="text-xs text-green-400 mt-1">-3.61%</div>
  </div>
  <div class="bg-gradient-to-br from-green-500/20 to-emerald-500/10 border border-green-500/30 rounded-xl p-3 text-center">
    <div class="text-xs text-white/60 mb-1">创业板指</div>
    <div class="text-xl font-bold text-green-400">3802.56</div>
    <div class="text-xs text-green-400 mt-1">-5.44%</div>
  </div>
  <div class="bg-gradient-to-br from-yellow-500/20 to-amber-500/10 border border-yellow-500/30 rounded-xl p-3 text-center">
    <div class="text-xs text-white/60 mb-1">成交额</div>
    <div class="text-xl font-bold text-yellow-400">3.52万亿</div>
    <div class="text-xs text-white/60 mt-1">放量下跌</div>
  </div>
</div>
<div class="bg-white/5 rounded-xl p-4">
  <h4 class="text-white font-semibold mb-3 text-sm">📊 周二（7/7）A股复盘：半导体带崩全市场·沪指四失4000点·创业板-5.44%</h4>
  <div class="grid md:grid-cols-2 gap-4 text-xs">
    <div>
      <p class="text-white/80 font-semibold mb-2">📈 相对抗跌方向</p>
      <p class="text-white/60 leading-relaxed mb-2">
      <b class="text-yellow-400">①银行/高股息（四大行尾盘拉升）</b>：避险资金涌入，工行/建行/农行微涨，防御属性凸显；<br>
      <b class="text-yellow-400">②石油石化/油服</b>：受中东局势+油价上涨预期支撑，中国海油/中石油相对抗跌；<br>
      ③贵金属（紫金/山金）：早盘冲高后随国际金价回落但相对跌幅较小；<br>
      ④部分低位中报预增股：业绩确定性资金抱团。
      </p>
    </div>
    <div>
      <p class="text-white/80 font-semibold mb-2">📉 重灾区（资金出逃）</p>
      <p class="text-white/60 leading-relaxed mb-2">
      <b class="text-green-400">①半导体/存储（跌停潮）</b>：韩股暴跌传导+大基金减持沪硅产业2%，半导体ETF单日-7%，存储-9%+，沪硅产业/兆易创新/江波龙/佰维存储等批量跌停；<br>
      <b>②AI算力/CPO</b>：中际旭创-10%+、新易盛-9%+，费半暴跌映射；<br>
      ③科创50 -6%+、创业板-5.44%；<br>
      <b class="text-yellow-400">特征</b>：约5000只个股下跌、跌停超200只、放量至3.52万亿，北向净流出约80亿，主力净流出超800亿，恐慌性抛售。
      </p>
    </div>
  </div>
  <p class="text-xs text-white/50 mt-3 leading-relaxed">
  ⚡ <b class="text-yellow-400">盘口解读：</b>沪指从4050开盘一路下杀至3972，4000点整数关口毫无抵抗，<b>短期进入情绪宣泄阶段</b>。
  但<b>中期逻辑未变</b>：流动性宽松（万亿逆回购）、政策底明确（新规+再融资改革+产业政策）、中报业绩支撑（存储/机器人/设备）。
  <b>关键位：沪指强支撑3930-3970，压力4000-4030。今日低开后看30分钟能否止跌，若早盘半小时成交萎缩+权重护盘，则短线反弹窗口开启。</b>
  若继续放量下杀，则等3930附近再考虑抄底。
  </p>
</div>
</div>'''
gen.add_section("昨日A股复盘（7/7）", ashare_html, "📉")

# ========== 3. 今日重磅新闻 ==========
news_items = [
    ('半导体抛售🔥S级','from-red-500 to-pink-500','全球半导体血洗：费半-4.65%韩股两度熔断·三星1810%利好兑现杀跌·大基金减持沪硅2%',
     '三重利空叠加引发全球半导体抛售潮：①<b class="text-green-400">三星Q2营业利润89.4万亿韩元同比+1810%创历史新高</b>，但"利好兑现"资金获利了结，市场担忧存储涨价周期见顶（涨价驱动利润≠销量驱动）；②<b>Meta对外出租闲置AI算力</b>引发"云厂商CAPEX见顶"担忧；③<b>大基金减持沪硅产业2%</b>（约6610万股）给A股雪上加霜。<b class="text-yellow-400">关键判断：</b>这是<b>季度调仓+情绪杀</b>，非产业逻辑反转——存储涨价趋势（三星Q3 DRAM+20%）、AI算力需求、国产替代三大核心逻辑未变。但<b>短期调整可能持续1-2周</b>，等机构调仓完成后企稳。来源：东方财富/36氪/每日经济新闻'),
    ('中东战火💥S级','from-orange-500 to-red-600','美军对伊朗发动系列打击·撤销石油制裁豁免·布油一度暴涨6%破76美元',
     '中东地缘风险骤升：①美军中央司令部宣布对伊朗发动"一系列强力打击"（回应霍尔木兹海峡袭船事件，三艘商船被袭）；②美国财政部撤销截至8月下旬的伊朗石油销售豁免；③<b class="text-red-400">布油盘中暴涨6%突破76美元/桶</b>，WTI涨5.3%至72.15美元；④卡塔尔LNG货轮遭导弹袭击；⑤伊朗最高领袖顾问称美伊谈判濒临失败。<b class="text-yellow-400">影响：</b>利好油服/石油石化/煤炭（能源价格上涨）；利空航空/化工（成本上升）；加剧通胀预期→美债收益率上行→压制成长股估值。<b>油服板块今日高开不追，若中东局势持续发酵则中线有机会。</b>来源：华尔街见闻/新华网'),
    ('黄金跳水🥇A级','from-yellow-400 to-amber-400','黄金暴跌-1.47%至4104美元·白银-3.4%破60·但央行连续20个月增持',
     '贵金属大幅回调：现货黄金-1.47%至4104.15美元/盎司，白银-3.38%破60美元。利空：美元+0.2%、美债收益率飙升（10年+6.8bp）、油价上涨引发通胀预期→美联储降息推迟。<b class="text-yellow-400">利好支撑：</b>中国央行6月买入48万盎司黄金（创2023年10月以来新高），连续20个月增持；香港黄金中央清算系统周二试运行；中东地缘风险。<b>策略：黄金中期逻辑不变（去美元化+央行购金+地缘），短期回调是上车机会，等3950-4000区间分批布局龙头。</b>来源：华尔街见闻/新浪财经'),
    ('大基金减持⚠️A级','from-gray-600 to-red-700','大基金减持沪硅产业2%·半导体情绪再承压·关注后续是否有更多减持',
     '沪硅产业公告：国家集成电路产业投资基金拟15个交易日后3个月内减持不超6610万股（占总股本2%）。当前大基金二期进入回收周期，此前已有多家公司被减持。<b class="text-red-400">对半导体板块情绪有压制作用</b>，尤其对设备/材料类高位股。<b>但</b>：大基金减持≠产业逻辑反转，更多是投资周期正常回收。关注后续是否有更多大基金减持公告。来源：每日经济新闻'),
    ('中报预增📈B级','from-emerald-500 to-teal-500','11家公司中报翻倍：浪潮信息+226-288%·复旦微电+313-416%·坤彩科技+254-305%',
     '7月7日晚间多家公司发布中报预告，业绩翻倍的有：浪潮信息（000977）净利26-31亿同比+226%~288%（AI服务器订单大增）；复旦微电（688385）净利8-10亿同比+313%~416%（FPGA+车规MCU放量）；坤彩科技（603826）净利1.75-2亿同比+254%~305%（钛白粉涨价+规模效应）。<b>中报业绩线仍是7月确定性最强主线，逢低布局超跌+高增标的。</b>来源：新浪财经'),
    ('人形机器人🤖B级','from-indigo-500 to-blue-500','发改委十五五AI五大思路·工信部：2026人形机器人整机产量有望破10万台·智元A链供应链',
     '发改委披露十五五AI发展五大思路：自主创新、应用牵引、生态协同、开放共赢、安全可控；工信部官宣2025年AI核心产业规模破1.2万亿，<b class="text-red-400">2026人形机器人整机产量有望突破10万台</b>。智元机器人"A链"供应链体系已达年10万台以上柔性生产能力，长三角一小时配套圈成型。<b class="text-yellow-400">人形机器人作为内资主导、与美股联动弱的独立主线，今日若随大盘低开反而是低吸机会。</b>来源：观澜志/21世纪经济报道'),
    ('商业航天🚀B级','from-purple-500 to-fuchsia-500','长征八号甲首飞成功1箭20星·千帆星座增至238颗·SpaceX获华尔街买入评级',
     '7月5日长征八号甲首飞成功，千帆组网卫星1箭20星（首次平板堆叠），千帆星座增至238颗。SpaceX获华尔街六家券商"买入"评级，大摩目标价300美元（+87%空间）。微光启航完成亿元天使++轮融资。<b>商业航天作为新增强催化赛道，低拥挤+高弹性，可轻仓布局。</b>来源：每日经济新闻'),
]
news_cards = ''
for tag, grad, title, content in news_items:
    news_cards += '<div class="bg-gradient-to-br from-white/5 to-white/0 border border-white/10 rounded-xl p-4 mb-3"><div class="flex items-center gap-2 mb-2"><span class="text-[10px] px-2 py-0.5 rounded-full bg-gradient-to-r %s text-white font-bold whitespace-nowrap">%s</span><h4 class="text-white font-semibold text-sm">%s</h4></div><p class="text-white/60 text-xs leading-relaxed">%s</p></div>' % (grad, tag, title, content)
gen.add_section("今日重磅新闻", '<div class="space-y-3">%s</div>' % news_cards, "📰")

# ========== 4. 核心题材动态 ==========
topics_data = [
    ('🛢️','石油石化/油服','中东战火+伊朗制裁豁免撤销·布油+6%·短期催化最强但持续性待观察','🔥S级-事件驱动','中国海油、中国石油、中曼石油、贝肯能源、中海油服',
     '美军打击伊朗+撤销石油制裁豁免+霍尔木兹海峡风险，布油一度涨6%破76美元。但EIA下调全年油价预期（布油82美元），认为霍尔木兹年底前恢复正常。<b class="text-red-400">策略：高开不追，等回踩确认再考虑。若局势持续升级（封锁海峡）则空间大，否则事件驱动后回落。关注今明两天中东局势发展。</b>'),
    ('🤖','人形机器人','内资主导独立主线·与美股联动弱·10万台产量预期·情绪宣泄后低吸','🟡 A级','埃斯顿、三花智控、绿的谐波、拓普集团、丰光精密、昊志机电',
     '发改委十五五AI规划+工信部10万台产量预期+智元A链供应链，产业催化持续。昨日随大盘下跌但<b>相对跌幅小于半导体</b>，内资主导的独立逻辑未破。<b class="text-yellow-400">策略：今日若继续低开，是分批低吸核心零部件龙头的机会，严格控制仓位（单票不超15%），止损位设在前期低点下方5%。</b>'),
    ('💾','存储芯片/HBM','费半-4.65%+韩股熔断+大基金减持·短期情绪杀·中期逻辑未变','⚠️ 观望-调整期','江波龙、兆易创新、聚辰股份、长电科技、北方华创（等企稳）',
     '三星1810%利润利好兑现杀跌+Meta算力出租引发CAPEX见顶担忧+大基金减持，三重利空叠加。<b>但中期产业逻辑未变</b>：三星Q3 DRAM+20%、聚辰NOR+25%、AI服务器需求刚性、国产替代加速。<b class="text-green-400">策略：持仓者不恐慌割肉在最低点，等反弹减仓；空仓者不抄底，等企稳信号（连续2天不创新低+量缩）再进场。设备+材料确定性优先于模组。</b>'),
    ('🏭','半导体设备/材料','国产替代逻辑最强·但短期受板块情绪拖累·等企稳再布局','🟢 B级-观望','北方华创、中微公司、盛美上海、拓荆科技、华海清科、雅克科技',
     '长鑫IPO预期+国产替代+存储涨价带动设备采购，中期逻辑最硬。但短期板块泥沙俱下，高位股有补跌风险。<b>等存储板块情绪企稳后低吸龙头，优先布局业绩确定性强的设备龙头。</b>'),
    ('🥇','黄金/贵金属','央行连续20个月增持·中东地缘支撑·但短期美债收益率上升压制','🟡 A级-回调布局','赤峰黄金、紫金矿业、山金国际、招金黄金、山东黄金',
     '短期利空：美债收益率飙升+美元走强→金价回调至4104美元。中期支撑：央行购金（6月+48万盎司）+去美元化+地缘风险+降息周期（虽推迟但方向不变）。<b class="text-yellow-400">策略：等回调到3950-4000区间分批布局龙头，中长线持有。</b>'),
    ('🏦','大金融/高股息','避险资金涌入·四大行尾盘拉升·防御配置首选','🟢 B级','中信证券、招商银行、工商银行、建设银行、中国平安',
     '昨日市场暴跌中银行/高股息相对抗跌，四大行尾盘拉升护盘。流动性宽松+防御需求支撑。<b>可作为底仓防御配置，降低组合波动。</b>'),
    ('🚀','商业航天','长征八号甲首飞+千帆238颗+SpaceX评级·新题材低拥挤','🟢 B级','上海瀚讯、海格通信、中国卫星、铖昌科技、航天电子',
     '新增强催化赛道，事件驱动型机会，拥挤度低弹性大。适合轻仓（5%以内）短线博弈，快进快出。'),
    ('💊','创新药/医疗','防御属性+政策底+业绩兑现·资金避险方向之一','🟢 B级','恒瑞医药、百济神州、信达生物、荣昌生物',
     '港股通创新药ETF周涨10%+，机构7月重点布局赛道之一。防御属性突出，与科技板块跷跷板效应明显。<b>市场调整期可作为防御配置。</b>'),
    ('⚠️','AI算力/CPO','费半暴跌+Meta算力出租·CAPEX见顶叙事强化·中期趋势未明','⚠️ 回避','中际旭创、新易盛、寒武纪、英维克',
     '费城半导体暴跌+Meta出租闲置算力引发云厂商CAPEX见顶担忧，光模块/服务器/液冷全链承压。<b class="text-red-400">持仓借反弹减仓，空仓不抄底。等Q2财报季验证后再判断方向。</b>'),
]
topic_cards = ''
for icon, name, change, level, leader, analysis in topics_data:
    topic_cards += '<div class="bg-white/5 rounded-xl p-4 border border-white/10"><div class="flex items-start justify-between mb-2"><div><div class="flex items-center gap-2 mb-1"><span class="text-xl">%s</span><h4 class="text-white font-semibold text-sm">%s</h4></div><p class="text-white/60 text-xs">%s</p></div><div class="flex flex-col items-end gap-1"><span class="text-xs font-bold text-white/80 bg-white/10 px-2 py-0.5 rounded-full">%s</span></div></div><div class="space-y-2 mb-3"><div class="flex items-center gap-2"><span class="text-white/50 text-xs">关注标的</span><span class="text-white/80 text-xs">%s</span></div></div><p class="text-white/60 text-xs leading-relaxed">%s</p></div>' % (icon, name, change, level, leader, analysis)
gen.add_section("核心题材动态", '<div class="grid md:grid-cols-2 gap-4">%s</div>' % topic_cards, "🔥")

# ========== 5. 催化剂日历 ==========
catalysts = [
    ('全天','💥 中东局势演变','美军打击伊朗+撤销石油豁免·霍尔木兹海峡风险','high','油服/石油/黄金/航空'),
    ('全天','📉 半导体情绪释放','费半-4.65%+韩股熔断+大基金减持·A股承压','high','半导体/存储/算力（承压）'),
    ('全天','🤖 人形机器人低吸窗口','内资独立主线·大盘错杀低吸机会','medium','机器人核心零部件'),
    ('全天','💀 *ST建艺10%跌停继续','昨日已跌停·新规10%跌幅·可能连续跌停','high','*ST建艺（必须清仓！）'),
    ('全天','📊 中报预告密集','11家公司中报翻倍·业绩线抱团','medium','中报高增标的'),
    ('本周','📊 7/9 6月CPI/PPI','影响国内政策预期','high','消费/周期/债券'),
    ('本周','📊 7/14 美国6月CPI','直接影响降息预期·油价上涨推升通胀','high','贵金属/科技/汇率'),
    ('本周','📋 7/15 中报预告集中','主板中报预告密集窗口+Q2 GDP','high','高景气龙头/规避纯概念'),
    ('本周','🔓 本周解禁','本周解禁约1016亿·屹唐653.6亿居前','high','规避解禁高位股'),
    ('下周','⚡ 美联储议息会议','7/30-31议息·通胀升温或推迟降息','high','贵金属/成长股'),
]
catalyst_cards = ''
for t,e,i,l,r in catalysts:
    lc = {'high':('from-red-500/20 to-orange-500/10 border-red-500/30','高','text-red-400'),
          'medium':('from-yellow-500/20 to-amber-500/10 border-yellow-500/30','中','text-yellow-400'),
          'low':('from-green-500/20 to-emerald-500/10 border-green-500/30','低','text-green-400')}[l]
    catalyst_cards += '<div class="bg-gradient-to-r %s border rounded-xl p-4"><div class="flex items-start justify-between"><div><div class="text-white/50 text-xs mb-1">%s</div><h4 class="text-white font-semibold text-sm mb-2">%s</h4><p class="text-white/60 text-xs">%s</p></div><span class="text-xs font-medium %s px-2 py-1 rounded-full bg-white/5">%s</span></div><div class="mt-2 pt-2 border-t border-white/10"><span class="text-white/50 text-xs">相关方向：</span><span class="text-white/70 text-xs">%s</span></div></div>' % (lc[0], t, e, i, lc[2], lc[1], r)
gen.add_section("今日/本周关键催化剂", '<div class="grid md:grid-cols-2 gap-4">%s</div><p class="text-xs text-white/40 mt-4">💡 7月核心日历：7/9 CPI/PPI；7/10-15中报预告密集；7/14美国CPI；7/15二季度GDP；7月中下旬长鑫IPO；7/22特斯拉Q2财报；7/30-31美联储议息。本周解禁40家合计约1016亿元（屹唐股份653.6亿、天承科技126.6亿）。中东局势演变是最大不确定性变量。</p>' % catalyst_cards, "📅")

# ========== 6. 持仓专项分析 ==========
portfolio_html = '''
<div class="space-y-4">
<div class="bg-gradient-to-r from-red-700/40 to-red-900/30 border-2 border-red-600 rounded-xl p-4">
  <div class="flex items-start gap-3"><span class="text-3xl">💀💀</span><div class="flex-1">
    <div class="flex items-center justify-between mb-1"><h4 class="text-white font-bold text-base">*ST建艺 (002789) — 新规10%跌停第二日！继续跌停！必须不计成本清仓！</h4>
    <span class="text-red-300 font-bold text-sm">10.20元 / 跌停 / 浮亏扩大</span></div>
    <p class="text-white/70 text-xs leading-relaxed mb-2">
    【昨日表现】7月7日一字跌停-9.97%报10.20元，成交额5373万，主力净流出1501万，买盘枯竭（跌停板封单907手）。
    新规下ST涨跌幅扩大至10%，<b class="text-red-400">跌幅空间翻倍，连续跌停风险极大</b>。
    </p>
    <p class="text-white/60 text-xs leading-relaxed mb-2">
    【利空逻辑】一季报亏损5311万、累计亏损超27亿、负债率94.38%、主业收缩、庭外重组不确定性高。<b>没有任何持有理由</b>。
    </p>
    <p class="text-yellow-300 text-xs font-bold leading-relaxed">
    🚨 今日操作建议：集合竞价任何价格挂单卖出！如果开盘继续跌停，每天挂跌停价排队卖出！不要再抱任何幻想！这只票的底在哪里没人知道，先出来再说！
    </p>
  </div></div>
</div>

<div class="bg-gradient-to-r from-orange-600/30 to-red-700/20 border border-orange-500/40 rounded-xl p-4">
  <div class="flex items-start gap-3"><span class="text-2xl">⚠️</span><div class="flex-1">
    <div class="flex items-center justify-between mb-1"><h4 class="text-white font-bold text-sm">英维克 (002837) — 液冷龙头·AI算力链承压·借反弹减仓</h4>
    <span class="text-orange-300 font-bold text-sm">约73元 / 高位回调中</span></div>
    <p class="text-white/70 text-xs leading-relaxed mb-2">
    【近期表现】7月6日涨3.68%（主力+4.51亿），7月7日随大盘调整（主力净卖出3.6亿）。AI液冷龙头，一季报营收+26%但净利-81.97%（增收不增利）。
    </p>
    <p class="text-white/60 text-xs leading-relaxed mb-2">
    【今日影响】费半暴跌+Meta算力出租→AI算力链整体承压，液冷作为算力配套也会受情绪影响。<b>但</b>英维克的液冷业务国内领先，数据中心/储能/通信多领域布局，中期成长逻辑仍在。
    </p>
    <p class="text-yellow-300 text-xs leading-relaxed">
    💡 操作建议：<b>反弹到73-75区间减仓1/3到1/2</b>，降低AI算力链敞口。<b>支撑位68-70元（前期平台），破位则继续减仓</b>。
    留底仓观察中报业绩，若中报验证液冷订单高增则再考虑加回。
    </p>
  </div></div>
</div>

<div class="bg-gradient-to-r from-yellow-600/30 to-orange-600/20 border border-yellow-500/40 rounded-xl p-4">
  <div class="flex items-start gap-3"><span class="text-2xl">⚠️</span><div class="flex-1">
    <div class="flex items-center justify-between mb-1"><h4 class="text-white font-bold text-sm">铜冠铜箔 (301217) — HVLP铜箔龙头·昨日抗跌·但大盘泥沙俱下难独善</h4>
    <span class="text-yellow-300 font-bold text-sm">144.82元 / +0.45%抗跌</span></div>
    <p class="text-white/70 text-xs leading-relaxed mb-2">
    【昨日表现】7月7日逆势红盘+0.45%收144.82元，早盘探底140.61后拉升至149.23，全天振幅6%，<b>大盘暴跌中抗跌属性凸显</b>。
    但主力资金仍净流出（冲高出逃），缩量至44亿（前一日63亿），说明买盘乏力。
    </p>
    <p class="text-white/60 text-xs leading-relaxed mb-2">
    【产业逻辑】HVLP高端铜箔缺口持续扩大，2026Q2供需缺口50%，加工费15-20万/吨，毛利率50%+。铜冠是国内唯一HVLP1-4代全谱系量产企业，HVLP5进入验证。<b>但国轩高科上半年减持840万股套现8.29亿，第二大股东持续减持是压制因素。</b>
    </p>
    <p class="text-yellow-300 text-xs leading-relaxed">
    💡 操作建议：<b>昨日抗跌不代表企稳，今日若随大盘低开，140元是关键支撑</b>（破位则下看130-135）。
    <b>反弹到149-155区间分批减仓</b>，不要抱有反转预期。留底仓等中报验证业绩弹性。
    <b>中期逻辑</b>：AI算力铜箔缺口持续至2028年，回调到位后仍是好标的。
    </p>
  </div></div>
</div>

<div class="bg-gradient-to-r from-yellow-600/30 to-orange-600/20 border border-yellow-500/40 rounded-xl p-4">
  <div class="flex items-start gap-3"><span class="text-2xl">⚠️</span><div class="flex-1">
    <div class="flex items-center justify-between mb-1"><h4 class="text-white font-bold text-sm">雅克科技 (002409) — 半导体材料平台·板块泥沙俱下·等企稳再加</h4>
    <span class="text-yellow-300 font-bold text-sm">约186元 / 高位回调</span></div>
    <p class="text-white/70 text-xs leading-relaxed mb-2">
    【近期表现】7月6日-6.54%（主力-4.38亿），7月7日继续下跌约-0.34%，从高点212回调约12%。
    公司已发风险提示：没有六氟化钨业务，电子材料业务短期存在过度解读。
    </p>
    <p class="text-white/60 text-xs leading-relaxed mb-2">
    【产业逻辑】中信建投最新研报（7/6）看好核心前驱体业务受益AI产业通胀，预计2026-2028年净利13.0/17.4/23.6亿，PE 73x/54x/40x。
    半导体材料平台型公司，光刻胶+电子特气+前驱体+硅微粉多管线推进。<b>但大基金减持沪硅产业引发对整个半导体材料板块的情绪压制。</b>
    </p>
    <p class="text-yellow-300 text-xs leading-relaxed">
    💡 操作建议：<b>当前处于板块情绪宣泄期，不急于加仓</b>。
    已持仓者：<b>反弹到200-210区间减仓1/3</b>，降低半导体材料敞口。
    空仓者：<b>等企稳信号（连续2天不创新低+量缩）再考虑</b>，170-180区间是较强支撑位（前期平台+20日均线）。
    中期看半导体材料国产替代逻辑不变，回调是布局优质龙头的机会。
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
          <th class="text-right py-2 px-2">现价(估)</th>
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
          <td class="text-right py-2 px-2 text-red-400">10.20(跌停)</td>
          <td class="text-center py-2 px-2 text-red-400">↓↓ 暴跌</td>
          <td class="text-center py-2 px-2">-</td>
          <td class="text-center py-2 px-2">无底</td>
          <td class="text-center py-2 px-2 text-red-400 font-bold">不计成本清仓！</td>
          <td class="text-center py-2 px-2 text-red-400 font-bold">🔴最高</td>
        </tr>
        <tr class="border-b border-white/5">
          <td class="py-2 px-2 font-medium">英维克</td>
          <td class="text-right py-2 px-2">~73</td>
          <td class="text-center py-2 px-2 text-yellow-400">↓ 回调</td>
          <td class="text-center py-2 px-2">75-77</td>
          <td class="text-center py-2 px-2">68-70</td>
          <td class="text-center py-2 px-2">反弹减仓1/3-1/2</td>
          <td class="text-center py-2 px-2">🟠高</td>
        </tr>
        <tr class="border-b border-white/5">
          <td class="py-2 px-2 font-medium">铜冠铜箔</td>
          <td class="text-right py-2 px-2">144.82</td>
          <td class="text-center py-2 px-2 text-yellow-400">→ 抗跌</td>
          <td class="text-center py-2 px-2">149-155</td>
          <td class="text-center py-2 px-2">140/130-135</td>
          <td class="text-center py-2 px-2">反弹减仓/留底仓</td>
          <td class="text-center py-2 px-2">🟡中</td>
        </tr>
        <tr>
          <td class="py-2 px-2 font-medium">雅克科技</td>
          <td class="text-right py-2 px-2">~186</td>
          <td class="text-center py-2 px-2 text-yellow-400">↓ 回调</td>
          <td class="text-center py-2 px-2">200-210</td>
          <td class="text-center py-2 px-2">170-180</td>
          <td class="text-center py-2 px-2">等企稳/反弹减仓</td>
          <td class="text-center py-2 px-2">🟡中</td>
        </tr>
      </tbody>
    </table>
  </div>
  <p class="text-xs text-white/40 mt-3">
  ⚠️ 今日整体策略：<b class="text-yellow-400">先处理风险最高的*ST建艺（集合竞价清仓），再看大盘情绪</b>。
  整体仓位控制在5成以内，现金为王，等30分钟级别止跌信号再考虑低吸。
  优先减持AI算力链（英维克），铜冠铜箔和雅克科技留底仓观察中报。
  腾出的仓位可布局人形机器人（核心零部件低吸）、黄金（回调分批）、防御性标的。
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
        <span class="text-xs font-bold text-red-400">❌ 验证失败 · T+1</span>
        <span class="text-[10px] text-white/40">7/6预判 → 7/7验证</span>
      </div>
      <p class="text-white/70 text-xs mb-1">
      <b>原预判：</b>7/6日报预判"人形机器人今日分化淘汰赛，核心龙头延续，跟风小票炸板"
      </p>
      <p class="text-white/70 text-xs mb-1">
      <b>实际走势：</b>7/7全市场暴跌，人形机器人板块普跌5-8%，<b>并非分化而是泥沙俱下</b>，核心龙头也未能幸免。
      </p>
      <p class="text-yellow-400 text-xs">
      <b>教训：</b>当全市场出现系统性风险（沪指-1.75%/创业板-5.44%）时，板块独立逻辑会被大盘情绪淹没，"分化"预判在系统性杀跌面前失效。
      <b>改进：</b>在外盘暴跌+期货大跌的情况下，应优先预判"全市场系统性风险"而非板块内部结构。
      </p>
    </div>
    <div class="bg-yellow-500/10 border border-yellow-500/30 rounded-lg p-3">
      <div class="flex items-center justify-between mb-1">
        <span class="text-xs font-bold text-yellow-400">⚠️ 部分兑现 · T+2</span>
        <span class="text-[10px] text-white/40">7/3预判 → 7/7验证</span>
      </div>
      <p class="text-white/70 text-xs mb-1">
      <b>原预判：</b>7/3预判"存储板块短期情绪企稳后可低吸设备+材料"
      </p>
      <p class="text-white/70 text-xs mb-1">
      <b>实际走势：</b>7/6存储板块因江波龙中报利好高开（如预期），但7/7因三星利好兑现+大基金减持暴跌（超预期）。
      </p>
      <p class="text-yellow-400 text-xs">
      <b>教训：</b>存储板块对海外情绪敏感度极高，"低吸"操作必须设置更严格的止损纪律。
      <b>改进：</b>半导体板块抄底必须等"连续2天不创新低+量缩"的企稳信号，单日反弹不构成入场条件。
      </p>
    </div>
  </div>
  <p class="text-xs text-white/40 mt-3">
  📊 当前准确率统计：S级分析师评级考核中，详见预判验证中心。
  </p>
</div>'''
gen.add_section("预判验证闭环", verify_html, "🔄")

# ========== 8. 空方视角 ==========
bear_html = '''
<div class="bg-gradient-to-br from-green-900/30 to-emerald-900/20 border border-green-500/30 rounded-xl p-4">
  <h4 class="text-green-400 font-semibold text-sm mb-3">🐻 空方视角（警惕这些风险）</h4>
  <div class="space-y-2 text-xs text-white/70 leading-relaxed">
    <p><b class="text-green-400">1. 全球半导体周期见顶风险：</b>三星1810%利润或为周期顶点，存储涨价由"单价驱动"而非"销量驱动"，一旦终端需求（手机/PC/服务器）跟不上，价格将快速回落。Meta出租闲置算力强化了"云厂商CAPEX见顶"叙事。</p>
    <p><b class="text-green-400">2. 中东局势失控风险：</b>美军打击伊朗+撤销石油豁免，若伊朗报复（封锁霍尔木兹海峡），油价可能暴涨至100+美元，全球通胀重燃→美联储被迫加息→全球股市估值下杀→A股也难以独善其身。</p>
    <p><b class="text-green-400">3. 大基金减持潮：</b>沪硅产业2%减持可能只是开始，若更多半导体公司被大基金减持，板块情绪将持续承压。大基金二期回收周期可能持续1-2年。</p>
    <p><b class="text-green-400">4. 中报"利好出尽"风险：</b>7月中报密集披露期，很多高景气赛道（存储/AI/机器人）的股价已提前反映预期，业绩公布后反而可能"利好出尽"下跌（参考三星走势）。</p>
    <p><b class="text-green-400">5. 人民币贬值压力：</b>美元走强+美债收益率上行+中美利差倒挂，离岸人民币跌破6.80，若继续贬值可能引发北向资金持续流出，压制A股。</p>
    <p><b class="text-green-400">6. 基金赎回负反馈：</b>科技主题基金前期涨幅大，若市场持续下跌引发基民赎回，将导致被动抛售，形成"下跌→赎回→更下跌"的负反馈循环。</p>
  </div>
  <p class="text-xs text-white/40 mt-3">
  ⚠️ 以上空方观点仅供风险参考，不代表看空市场。多方逻辑：政策底（流动性宽松+产业政策）、业绩底（中报高增）、估值底（沪指4000点下方安全边际）。操作上保持灵活，做好两手准备。
  </p>
</div>'''
gen.add_section("空方视角·风险提示", bear_html, "🐻")

# ========== 9. 操作策略总结 ==========
strategy_html = '''
<div class="bg-gradient-to-br from-blue-900/30 to-indigo-900/20 border border-blue-500/30 rounded-xl p-4">
  <h4 class="text-blue-300 font-semibold text-sm mb-3">🎯 今日操作策略（龙空龙纪律）</h4>
  <div class="grid md:grid-cols-2 gap-4 text-xs">
    <div>
      <p class="text-white/80 font-semibold mb-2">🔴 卖出优先级</p>
      <div class="space-y-1 text-white/70">
        <p>1. <b class="text-red-400">*ST建艺：集合竞价不计成本清仓！</b></p>
        <p>2. 英维克：反弹73-75元减仓1/3-1/2</p>
        <p>3. 铜冠铜箔：反弹149-155元减仓1/3</p>
        <p>4. 雅克科技：反弹200-210元减仓1/3</p>
        <p class="text-white/50">原则：先处理风险最高的，AI算力链优先减</p>
      </div>
    </div>
    <div>
      <p class="text-white/80 font-semibold mb-2">🟢 低吸观察（等企稳信号）</p>
      <div class="space-y-1 text-white/70">
        <p>1. 人形机器人核心：绿的谐波/三花/埃斯顿（30日线附近）</p>
        <p>2. 半导体材料龙头：雅克科技（170-180企稳后）</p>
        <p>3. 黄金龙头：紫金/赤峰（金价回调至3950-4000）</p>
        <p>4. 中报高增+超跌：浪潮信息/复旦微电等</p>
        <p class="text-white/50">原则：不抄底、等企稳、分批建、严止损</p>
      </div>
    </div>
  </div>
  <div class="mt-3 pt-3 border-t border-white/10">
    <p class="text-yellow-400 text-xs font-semibold mb-1">
    ⚡ 今日关键观察点
    </p>
    <p class="text-white/60 text-xs">
    ① 开盘半小时成交量（8500亿以上=有承接，以下=偏弱）；② 沪指3970支撑是否有效；
    ③ 半导体板块开盘跌幅及是否有资金低吸；④ 人形机器人是否走出独立行情；
    ⑤ 中东局势最新进展（影响油价和通胀预期）；⑥ 北向资金流向（连续流出则谨慎）。
    </p>
  </div>
  <div class="mt-3 pt-3 border-t border-white/10">
    <p class="text-white/80 text-xs font-semibold mb-1">
    💼 仓位建议：4-5成（防御为主）
    </p>
    <p class="text-white/50 text-xs">
    现金5-6成 / 核心持仓（铜冠+雅克底仓）2成 / 机器人低吸1成 / 防御1成 / 机动1成
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
      <p class="text-white/60">2026/06 多次在半导体板块单日反弹时抄底，结果次日继续下跌。
      <b>正确做法</b>：必须等连续2天不创新低+量缩+权重股止跌的三重确认信号。</p>
    </div>
    <div class="bg-amber-500/10 border border-amber-500/30 rounded-lg p-2">
      <p class="text-amber-300 font-semibold mb-1">教训#2：外盘暴跌日，A股难独善</p>
      <p class="text-white/60">费半-3%以上的交易日，A股半导体板块90%概率跟跌。
      <b>正确做法</b>：外盘暴跌当晚就应预判次日A股承压，提前减仓而非开盘后再卖。</p>
    </div>
    <div class="bg-amber-500/10 border border-amber-500/30 rounded-lg p-2">
      <p class="text-amber-300 font-semibold mb-1">教训#3：利好兑现=利好出尽</p>
      <p class="text-white/60">三星1810%利润/江波龙622倍中报等"明牌利好"，往往是股价高点。
      <b>正确做法</b>：买预期卖事实，在业绩公布前逐步兑现，不等到业绩公布当天才卖。</p>
    </div>
  </div>
</div>'''
gen.add_section("教训库引用", lesson_html, "📚")

# ========== 生成+发布 ==========
import shutil
output_path = os.path.join(WORK_DIR, 'docs/daily/20260708_每日新闻洞察.html')
result = gen.publish(output_path=output_path)
print("发布结果:", result)
print("成功:", result.get('success', False))
print("报告路径:", output_path)
print("文件大小:", os.path.getsize(output_path), "字节")

# 更新 latest.html
latest_path = os.path.join(WORK_DIR, 'docs/daily/latest.html')
shutil.copy2(output_path, latest_path)
print("latest.html 已更新")
