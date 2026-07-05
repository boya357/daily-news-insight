#!/usr/bin/env python3
"""生成 2026-07-04（周六·假期版）盘后速递"""
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'v3'))
os.chdir(os.path.dirname(os.path.abspath(__file__)))

from generators.aftermarket_pro import AftermarketProGenerator

DATE = "2026-07-04"
SUBTITLE = "周末假期版 · 周五复盘 + 中报季前瞻 + 新规解读"

gen = AftermarketProGenerator(date_str=DATE, subtitle=SUBTITLE, data_dir='docs/data')

# ===== 1. 今日核心亮点（假期版） =====
highlight = '''<div class="space-y-3">
<p><strong class="text-yellow-300">🏖️ 周末休市提示：</strong>今日为周六，A股休市。本报告为假期深度版，复盘7月3日（周五）行情，梳理周末重要政策/业绩/外盘动态，为下周一（7/6）开盘做准备。</p>
<p><strong class="text-red-300">📌 周五行情定性：</strong>A股在7/2暴跌后迎来缩量弱修复——上证+0.37%收4043.64点站稳4000，深成指+0.64%、创业板仅+0.07%（几乎未反弹），科创50逆势-0.59%；成交3.18万亿较昨日缩量2681亿，3800+只个股上涨但权重科技拖累指数，典型"指数虚涨、题材真热闹"。</p>
<p><strong class="text-purple-300">🔥 周末三大核心变量：</strong>①7/6周一交易新规落地（主板ST涨跌幅扩至10%，*ST建艺须无条件清仓）；②美国6月非农爆冷仅5.7万人，美联储加息预期延后、降息预期升温（花旗预测10月重启降息）；③中报预告进入密集披露期，江波龙暴增622-744倍引爆存储板块业绩预期。</p>
<p><strong class="text-blue-300">⚠️ 持仓紧急预警：</strong>*ST建艺下周一涨跌幅扩至10%，集合竞价必须不计成本清仓；英维克深度破止损-31.5%，周一反弹73-75坚决减仓≥1/2、破70无条件离场；铜冠铜箔移动止盈下移至150元；雅克科技底仓1/2观察200-205企稳。</p>
</div>'''
gen.add_today_highlight(highlight)

# ===== 2. 周五市场收盘总结 =====
market_summary_html = '''
<div class="grid grid-cols-2 md:grid-cols-4 gap-3">
    <div class="bg-gradient-to-br from-green-500/20 to-emerald-500/10 border border-green-500/30 rounded-xl p-4 text-center">
        <div class="text-sm text-white/60 mb-1">上证指数</div>
        <div class="text-xl font-bold text-white mb-1">4043.64</div>
        <div class="text-sm text-green-400 font-semibold">+0.37%</div>
    </div>
    <div class="bg-gradient-to-br from-green-500/20 to-emerald-500/10 border border-green-500/30 rounded-xl p-4 text-center">
        <div class="text-sm text-white/60 mb-1">深证成指</div>
        <div class="text-xl font-bold text-white mb-1">15597.51</div>
        <div class="text-sm text-green-400 font-semibold">+0.64%</div>
    </div>
    <div class="bg-gradient-to-br from-green-500/20 to-emerald-500/10 border border-green-500/30 rounded-xl p-4 text-center">
        <div class="text-sm text-white/60 mb-1">创业板指</div>
        <div class="text-xl font-bold text-white mb-1">4019.93</div>
        <div class="text-sm text-green-400 font-semibold">+0.07%</div>
    </div>
    <div class="bg-gradient-to-br from-red-500/20 to-orange-500/10 border border-red-500/30 rounded-xl p-4 text-center">
        <div class="text-sm text-white/60 mb-1">科创50</div>
        <div class="text-xl font-bold text-white mb-1">1975.60</div>
        <div class="text-sm text-red-400 font-semibold">-0.59%</div>
    </div>
</div>
<div class="grid grid-cols-2 md:grid-cols-5 gap-3 mt-4">
    <div class="bg-white/5 rounded-lg p-3 text-center">
        <div class="text-white/50 text-xs mb-1">成交额</div>
        <div class="text-white font-bold text-sm">3.18万亿</div>
        <div class="text-white/40 text-xs">缩量2681亿</div>
    </div>
    <div class="bg-white/5 rounded-lg p-3 text-center">
        <div class="text-white/50 text-xs mb-1">上涨/下跌</div>
        <div class="text-white font-bold text-sm">3804/1628</div>
        <div class="text-white/40 text-xs">涨跌比7:3</div>
    </div>
    <div class="bg-white/5 rounded-lg p-3 text-center">
        <div class="text-white/50 text-xs mb-1">涨停/跌停</div>
        <div class="text-white font-bold text-sm">160+/24</div>
        <div class="text-white/40 text-xs">小票修复</div>
    </div>
    <div class="bg-white/5 rounded-lg p-3 text-center">
        <div class="text-white/50 text-xs mb-1">主力资金</div>
        <div class="text-red-400 font-bold text-sm">-175.9亿</div>
        <div class="text-white/40 text-xs">净流出</div>
    </div>
    <div class="bg-white/5 rounded-lg p-3 text-center">
        <div class="text-white/50 text-xs mb-1">两融余额</div>
        <div class="text-white font-bold text-sm">3.01万亿</div>
        <div class="text-white/40 text-xs">-74.9亿</div>
    </div>
</div>
<div class="mt-4 bg-white/5 rounded-xl p-4 border border-white/10">
    <div class="text-white font-semibold mb-2 flex items-center gap-2"><span>🔍</span><span>周五走势定性：暴跌后的弱修复</span></div>
    <div class="text-white/70 text-sm leading-relaxed space-y-1">
        <p>• <strong>反弹力度极弱</strong>：创业板仅+0.07%（前日-5.71%几乎未反弹），科创板继续-0.59%，资金对科技成长信心未恢复</p>
        <p>• <strong>缩量反弹性质</strong>：成交额缩至3.18万亿（6月18日以来最低），场内资金腾挪而非增量入场，尾盘冲高回落留长上影</p>
        <p>• <strong>风格极致切换</strong>：资金从高位AI硬件出逃至低位机器人、有色、军工，属于典型高低切换而非全面反弹</p>
        <p>• <strong>上证50领涨</strong>：权重蓝筹修复最稳（+0.65%），高股息防御配置逻辑得到资金认可</p>
    </div>
</div>
'''
gen.add_section("📊 周五市场收盘总结（7月3日）", market_summary_html, "📊")

# ===== 3. 周五板块表现 =====
sector_html = '''
<div class="mb-4">
    <div class="text-white font-semibold mb-3 flex items-center gap-2"><span>🔥</span><span>强势板块（资金流入方向）</span></div>
    <div class="grid md:grid-cols-2 gap-3">
        <div class="bg-red-500/10 border border-red-500/20 rounded-lg p-3">
            <div class="flex justify-between items-center mb-2">
                <span class="text-white font-medium text-sm">人形机器人</span>
                <span class="text-red-400 font-bold text-sm">+5.21%</span>
            </div>
            <div class="text-xs text-white/60">催化：宇树科技IPO获批（募资42亿）+马斯克Optimus量产信号+大摩上调出货预测；埃斯顿4天3板、丰光精密30CM涨停，40余股涨停；主力净流入244.57亿</div>
        </div>
        <div class="bg-red-500/10 border border-red-500/20 rounded-lg p-3">
            <div class="flex justify-between items-center mb-2">
                <span class="text-white font-medium text-sm">贵金属/黄金</span>
                <span class="text-red-400 font-bold text-sm">+6.74%</span>
            </div>
            <div class="text-xs text-white/60">催化：COMEX黄金收4135.5美元（+1.49%）+美国非农爆冷降息预期升温；赤峰黄金/招金黄金2连板，四川/西部/山金国际涨停</div>
        </div>
        <div class="bg-red-500/10 border border-red-500/20 rounded-lg p-3">
            <div class="flex justify-between items-center mb-2">
                <span class="text-white font-medium text-sm">国防军工/航天</span>
                <span class="text-red-400 font-bold text-sm">+6.39%</span>
            </div>
            <div class="text-xs text-white/60">催化：长征十号乙首飞窗口7月10-13日锁定；商业航天+船舶海运低位补涨；中国船舶净流入11.43亿</div>
        </div>
        <div class="bg-red-500/10 border border-red-500/20 rounded-lg p-3">
            <div class="flex justify-between items-center mb-2">
                <span class="text-white font-medium text-sm">汽车零部件/减速器</span>
                <span class="text-red-400 font-bold text-sm">+4.17%</span>
            </div>
            <div class="text-xs text-white/60">催化：高端装备研发税收优惠延期至2028年+500亿技改专项资金；汽车零部件主力净流入68.93亿（全市场第一），三花智控净流入21.88亿</div>
        </div>
    </div>
</div>
<div>
    <div class="text-white font-semibold mb-3 flex items-center gap-2"><span>🧊</span><span>弱势板块（资金兑现方向）</span></div>
    <div class="grid md:grid-cols-2 gap-3">
        <div class="bg-green-500/10 border border-green-500/20 rounded-lg p-3">
            <div class="flex justify-between items-center mb-2">
                <span class="text-white font-medium text-sm">半导体（全板块）</span>
                <span class="text-green-400 font-bold text-sm">主力净流出194.77亿</span>
            </div>
            <div class="text-xs text-white/60">费城半导体隔夜-5.44%传导；京东方A净流出51.58亿、兆易创新-30.61亿、中际旭创-19.67亿；但存储板块午后分化（德明利涨停、江波龙+3.14%）</div>
        </div>
        <div class="bg-green-500/10 border border-green-500/20 rounded-lg p-3">
            <div class="flex justify-between items-center mb-2">
                <span class="text-white font-medium text-sm">氟化工/电子特气</span>
                <span class="text-green-400 font-bold text-sm">多氟多/巨化跌停</span>
            </div>
            <div class="text-xs text-white/60">多氟多跌停、三美股份跌停、巨化股份-9.99%；电子化学品主力净流出66.14亿；前期涨幅过大资金集中兑现</div>
        </div>
        <div class="bg-green-500/10 border border-green-500/20 rounded-lg p-3">
            <div class="flex justify-between items-center mb-2">
                <span class="text-white font-medium text-sm">光刻胶/电子化学品</span>
                <span class="text-green-400 font-bold text-sm">-5.74%</span>
            </div>
            <div class="text-xs text-white/60">晶瑞电材-12.59%、泰和科技-10.49%、广信材料-10.4%；雅克科技前日跌停后周五-6.11%险守200元</div>
        </div>
        <div class="bg-green-500/10 border border-green-500/20 rounded-lg p-3">
            <div class="flex justify-between items-center mb-2">
                <span class="text-white font-medium text-sm">光学光电子/CPO</span>
                <span class="text-green-400 font-bold text-sm">净流出95.87亿</span>
            </div>
            <div class="text-xs text-white/60">亨通光电-18.02亿、中际旭创-19.67亿、新易盛融资买入47亿但主力流出；Meta"卖算力"事件引发AI算力需求担忧</div>
        </div>
    </div>
</div>
'''
gen.add_section("📊 周五板块强弱拆解", sector_html, "📊")

# ===== 4. 周末重要新闻 =====
news_html = '''<div class="space-y-3">
<div class="bg-gradient-to-r from-red-500/15 to-orange-500/10 border border-red-500/30 rounded-xl p-4">
    <div class="flex items-center gap-2 mb-2">
        <span class="text-white font-semibold">🚨 【最高优先级】7月6日（周一）A股交易新规正式落地</span>
        <span class="text-xs px-2 py-0.5 rounded-full bg-red-500/30 text-red-300">P0紧急</span>
    </div>
    <div class="text-white/70 text-sm space-y-1">
        <p>• <strong>主板ST/*ST涨跌幅由5%扩至10%</strong>：沪深主板约157-211只ST股波动翻倍，*ST建艺在列！集合竞价必须不计成本清仓</p>
        <p>• <strong>盘后固定价格交易扩容至全部A股+ETF</strong>：15:05-15:30统一按收盘价成交，新增盘后调仓窗口</p>
        <p>• <strong>尾盘3分钟改收盘集合竞价</strong>：14:57-15:00仅限价单、不可撤单，收盘价由集合竞价撮合</p>
        <p>• <strong>ST异常波动阈值同步上调</strong>：从±12%上调至±20%；买入主板ST须重签风险揭示书</p>
        <p class="text-yellow-300">⚠️ 影响：ST板块波动加剧，*ST建艺周一跌幅可能放大至-10%，务必集合竞价直接挂跌停价出！</p>
    </div>
</div>

<div class="bg-gradient-to-r from-yellow-500/15 to-amber-500/10 border border-yellow-500/30 rounded-xl p-4">
    <div class="flex items-center gap-2 mb-2">
        <span class="text-white font-semibold">🇺🇸 美国6月非农爆冷+美联储降息预期升温</span>
        <span class="text-xs px-2 py-0.5 rounded-full bg-yellow-500/30 text-yellow-300">宏观核心</span>
    </div>
    <div class="text-white/70 text-sm space-y-1">
        <p>• 6月非农新增仅<strong>5.7万人</strong>（预期11.3万，近乎腰斩），前两月合计下修7.4万人</p>
        <p>• 失业率降至4.2%但源于劳动参与率骤降（83万人退出劳动力市场），含金量极低</p>
        <p>• <strong>花旗明确预测</strong>：加息理由已"不复存在"，美联储<strong>10月重启降息</strong>，年底前再降一次至3.0-3.25%</p>
        <p>• CME FedWatch：7月维持利率不变概率82.4%，加息预期推迟至12月</p>
        <p>• 市场反应：美元跌破101，COMEX黄金冲上4135美元（+1.49%），美债收益率下行，但美股半导体崩盘（费半-5.44%）</p>
        <p class="text-green-300">✅ 对A股影响：流动性预期边际宽松→利好黄金/贵金属/高股息；但半导体外盘大跌→周一科技股仍有承压</p>
    </div>
</div>

<div class="bg-gradient-to-r from-purple-500/15 to-pink-500/10 border border-purple-500/30 rounded-xl p-4">
    <div class="flex items-center gap-2 mb-2">
        <span class="text-white font-semibold">📈 中报业绩预告密集披露——存储板块业绩炸裂</span>
        <span class="text-xs px-2 py-0.5 rounded-full bg-purple-500/30 text-purple-300">业绩主线</span>
    </div>
    <div class="text-white/70 text-sm space-y-1">
        <p>• <strong class="text-yellow-200">江波龙</strong>：上半年净利92-110亿元，同比暴增<strong>62204%-74394%</strong>（622-744倍），暂居A股"预增王"；Q2单季53-71亿环比+38%~84%</p>
        <p>• <strong class="text-yellow-200">国泰海通</strong>：首份券商半年报预告，上半年净利200-205亿同比+27%-30%，Q2单季同比+290%-304%</p>
        <p>• <strong class="text-yellow-200">杭电股份</strong>：净利3.6-4亿，同比+852%-958%（光纤光缆量价齐升）</p>
        <p>• <strong class="text-yellow-200">东岳硅材</strong>：净利4.24-4.44亿，同比+905%-952%（有机硅涨价+成本下降）</p>
        <p>• <strong class="text-yellow-200">中金岭南</strong>：净利10.5-12亿，同比+88%-115%（金属价格上涨）</p>
        <p>• <strong class="text-yellow-200">中电港</strong>：净利5-5.3亿，同比+176%-193%（AI/数据中心存储需求强劲）</p>
        <p>• 截至目前A股59家披露中报预告，超320家预增超100%，<strong>存储芯片（41家翻倍）、半导体设备（32家翻倍）</strong>为两大核心赛道</p>
    </div>
</div>

<div class="bg-gradient-to-r from-blue-500/15 to-cyan-500/10 border border-blue-500/30 rounded-xl p-4">
    <div class="flex items-center gap-2 mb-2">
        <span class="text-white font-semibold">🏛️ 周末重要政策汇总</span>
        <span class="text-xs px-2 py-0.5 rounded-full bg-blue-500/30 text-blue-300">政策面</span>
    </div>
    <div class="text-white/70 text-sm space-y-1">
        <p>• <strong>证监会完善再融资规则征求意见</strong>：定增储架发行制度、小额快速融资上限3亿→6亿（百亿市值以上→10亿），募集资金强化主业投向</p>
        <p>• <strong>央行7/6开展1万亿买断式逆回购</strong>：3个月期（91天），维护银行体系流动性充裕</p>
        <p>• <strong>国务院印发《美丽中国建设"十五五"规划》</strong>：大气/水/土壤/固废/新污染物治理等重大工程</p>
        <p>• <strong>发改委印发《循环经济"十五五"规划》</strong>：2030年资源循环利用产业产值达8万亿</p>
        <p>• <strong>2000亿超长期特别国债设备更新资金全部下达</strong>：覆盖能源电力/物流/教育/养老/老旧小区改造</p>
        <p>• <strong>三部门：2027年起取消节能汽车减半征收车船税/新能源车船免征</strong></p>
        <p>• <strong>国内汽柴油价格"三连降"</strong>：每吨降950/915元，柴油回"6元时代"（近6年最大降幅）</p>
        <p>• <strong>鹏鼎控股拟定增96亿</strong>：用于AI服务器+高速光模块高密度互连积层板项目</p>
    </div>
</div>

<div class="bg-gradient-to-r from-pink-500/15 to-rose-500/10 border border-pink-500/30 rounded-xl p-4">
    <div class="flex items-center gap-2 mb-2">
        <span class="text-white font-semibold">🌍 隔夜外盘（7月3日凌晨，美股独立日补休）</span>
        <span class="text-xs px-2 py-0.5 rounded-full bg-pink-500/30 text-pink-300">外盘映射</span>
    </div>
    <div class="text-white/70 text-sm space-y-1">
        <p>• <strong>道指+1.14%创历史新高</strong>（52900点），苹果+4.84%领涨，防御性蓝筹（麦当劳/强生/可口可乐）涨3-4%</p>
        <p>• <strong>纳指-0.80%，费半-5.44%</strong>，芯片股连续第二日暴跌——闪迪-14%、泰瑞达-13.6%、科磊-11.5%、西部数据-9%、美光/英特尔-5%、AMD/阿斯麦-4%</p>
        <p>• <strong>特斯拉-7.49%</strong>（近一年最大单日跌幅），Meta-4.9%；但SpaceX+2.83%、奈飞+4.66%</p>
        <p>• <strong>黄金/白银/加密货币逆势上涨</strong>，美国黄金公司+5%、Coinbase+4%、泛美白银+4%</p>
        <p>• <strong>中概股多数下跌</strong>：纳斯达克金龙指数-1.77%，世纪互联-10%、蔚来/小鹏/百度-3%+</p>
        <p class="text-red-300">⚠️ 美股周五（7/4美国独立日）休市；周末外盘无新数据。周一A股开盘受周四晚美股芯片暴跌影响，科技股仍有低开压力</p>
    </div>
</div>
</div>'''
gen.add_section("🌙 周末重要新闻/政策汇总", news_html, "🌙")

# ===== 5. 中报业绩预增 =====
earnings_html = '''
<div class="grid grid-cols-2 gap-3 mb-4">
    <div class="bg-white/5 rounded-lg p-3 text-center border border-white/10">
        <div class="text-2xl font-bold text-green-400">59+</div>
        <div class="text-xs text-white/50">已披露半年报预告公司</div>
    </div>
    <div class="bg-white/5 rounded-lg p-3 text-center border border-white/10">
        <div class="text-2xl font-bold text-purple-400">320+</div>
        <div class="text-xs text-white/50">预增超100%公司</div>
    </div>
</div>
<div class="mb-2 text-white/80 text-sm font-semibold">🏆 核心预增标的（周末最新披露）</div>
<div class="space-y-3">
<div class="bg-white/5 rounded-xl p-4 border border-purple-500/30 hover:bg-white/10 transition-colors">
    <div class="flex items-start justify-between gap-3">
        <div class="flex-1">
            <div class="flex items-center gap-2 mb-1">
                <span class="text-white font-semibold">江波龙</span>
                <span class="text-white/40 text-xs">301308</span>
                <span class="text-xs px-2 py-0.5 rounded-full bg-purple-500/20 text-purple-300">预增王👑</span>
                <span class="text-xs px-2 py-0.5 rounded-full bg-red-500/20 text-red-300">存储芯片</span>
            </div>
            <div class="text-white/70 text-xs leading-relaxed mb-2">上半年净利92-110亿，同比+62204%~74394%；Q2单季53-71亿环比+38%~84%；存储晶圆涨价+LTA长协续签+自有封测产能+HLC技术（端侧AI DRAM用量-40%）。市值2615亿，年内+152.9%。</div>
            <div class="flex items-center gap-4 text-xs text-white/40">
                <span>📅 披露: 2026-07-03</span>
                <span>💰 最新价: 618.02元</span>
            </div>
        </div>
        <div class="text-right flex-shrink-0">
            <div class="text-lg font-bold text-purple-400">62204%~74394%</div>
            <div class="text-xs text-white/40">净利润增幅</div>
        </div>
    </div>
</div>
<div class="bg-white/5 rounded-xl p-4 border border-pink-500/30 hover:bg-white/10 transition-colors">
    <div class="flex items-start justify-between gap-3">
        <div class="flex-1">
            <div class="flex items-center gap-2 mb-1">
                <span class="text-white font-semibold">东岳硅材</span>
                <span class="text-white/40 text-xs">300821</span>
                <span class="text-xs px-2 py-0.5 rounded-full bg-pink-500/20 text-pink-300">大幅预增</span>
                <span class="text-xs px-2 py-0.5 rounded-full bg-cyan-500/20 text-cyan-300">有机硅</span>
            </div>
            <div class="text-white/70 text-xs leading-relaxed mb-2">净利4.24-4.44亿，同比+905%-952%；有机硅产品涨价+工业硅成本下降+毛利率提升。</div>
            <div class="flex items-center gap-4 text-xs text-white/40">
                <span>📅 披露: 2026-07-03</span>
            </div>
        </div>
        <div class="text-right flex-shrink-0">
            <div class="text-lg font-bold text-pink-400">905%~952%</div>
            <div class="text-xs text-white/40">净利润增幅</div>
        </div>
    </div>
</div>
<div class="bg-white/5 rounded-xl p-4 border border-pink-500/30 hover:bg-white/10 transition-colors">
    <div class="flex items-start justify-between gap-3">
        <div class="flex-1">
            <div class="flex items-center gap-2 mb-1">
                <span class="text-white font-semibold">杭电股份</span>
                <span class="text-white/40 text-xs">603618</span>
                <span class="text-xs px-2 py-0.5 rounded-full bg-pink-500/20 text-pink-300">大幅预增</span>
                <span class="text-xs px-2 py-0.5 rounded-full bg-blue-500/20 text-blue-300">光纤光缆</span>
            </div>
            <div class="text-white/70 text-xs leading-relaxed mb-2">净利3.6-4.0亿，同比+852%-958%；光纤光缆市场回暖，光纤产品量价齐升，数据中心建设带动需求。</div>
            <div class="flex items-center gap-4 text-xs text-white/40">
                <span>📅 披露: 2026-07-03</span>
            </div>
        </div>
        <div class="text-right flex-shrink-0">
            <div class="text-lg font-bold text-pink-400">852%~958%</div>
            <div class="text-xs text-white/40">净利润增幅</div>
        </div>
    </div>
</div>
<div class="bg-white/5 rounded-xl p-4 border border-green-500/30 hover:bg-white/10 transition-colors">
    <div class="flex items-start justify-between gap-3">
        <div class="flex-1">
            <div class="flex items-center gap-2 mb-1">
                <span class="text-white font-semibold">国泰海通</span>
                <span class="text-white/40 text-xs">601211</span>
                <span class="text-xs px-2 py-0.5 rounded-full bg-green-500/20 text-green-300">预增</span>
                <span class="text-xs px-2 py-0.5 rounded-full bg-yellow-500/20 text-yellow-300">券商龙头</span>
            </div>
            <div class="text-white/70 text-xs leading-relaxed mb-2">上半年净利200-205亿同比+27%-30%，Q2单季136-141亿同比+290%-304%；财富管理/投行/机构交易/投资管理全面增长，创同期历史新高。</div>
            <div class="flex items-center gap-4 text-xs text-white/40">
                <span>📅 披露: 2026-07-03</span>
            </div>
        </div>
        <div class="text-right flex-shrink-0">
            <div class="text-lg font-bold text-green-400">27%~30%</div>
            <div class="text-xs text-white/40">净利润增幅</div>
        </div>
    </div>
</div>
<div class="bg-white/5 rounded-xl p-4 border border-green-500/30 hover:bg-white/10 transition-colors">
    <div class="flex items-start justify-between gap-3">
        <div class="flex-1">
            <div class="flex items-center gap-2 mb-1">
                <span class="text-white font-semibold">中金岭南</span>
                <span class="text-white/40 text-xs">000060</span>
                <span class="text-xs px-2 py-0.5 rounded-full bg-green-500/20 text-green-300">预增</span>
                <span class="text-xs px-2 py-0.5 rounded-full bg-amber-500/20 text-amber-300">贵金属</span>
            </div>
            <div class="text-white/70 text-xs leading-relaxed mb-2">净利10.5-12亿，同比+88%-115%；稀有稀散贵金属价格同比上升+交易性金融资产公允价值收益。</div>
            <div class="flex items-center gap-4 text-xs text-white/40">
                <span>📅 披露: 2026-07-03</span>
            </div>
        </div>
        <div class="text-right flex-shrink-0">
            <div class="text-lg font-bold text-green-400">88%~115%</div>
            <div class="text-xs text-white/40">净利润增幅</div>
        </div>
    </div>
</div>
</div>
<div class="mt-4 bg-yellow-500/10 border border-yellow-500/20 rounded-xl p-3">
    <div class="text-yellow-300 text-xs leading-relaxed">
        💡 <strong>中报季核心逻辑：</strong>7月市场从"资金驱动"切向"业绩驱动"。存储芯片（全板块41家翻倍，DRAM/NAND价格Q2跳涨58-70%）和半导体设备（国产替代32家翻倍）是两大业绩确定性最强主线。但需注意低基数效应——增速上万倍≠盈利能力无敌，核心看<strong>扣非利润+Q2环比+产能/订单真实性</strong>。
    </div>
</div>
'''
gen.add_section("📈 中报业绩预增追踪", earnings_html, "📈")

# ===== 6. 持仓诊断 =====
portfolio_html = '''
<div class="flex items-center justify-between mb-3">
    <div class="flex items-center gap-2">
        <span class="text-lg">💼</span>
        <span class="text-white font-semibold">持仓周末诊断（7月4日）</span>
    </div>
    <div class="flex gap-2 text-xs">
        <span class="text-red-400">🚨 1只必须清仓</span>
        <span class="text-white/30">|</span>
        <span class="text-red-400">🔴 2只破位减仓</span>
        <span class="text-white/30">|</span>
        <span class="text-yellow-400">🟡 1只移动止盈</span>
    </div>
</div>
<div class="space-y-3">

<div class="bg-gradient-to-r from-red-500/20 to-rose-500/10 border-2 border-red-500/50 rounded-xl p-4">
    <div class="flex items-center justify-between mb-2">
        <div class="flex items-center gap-2">
            <span class="text-lg">🚨</span>
            <span class="text-white font-bold">*ST建艺（002789）</span>
            <span class="text-xs px-2 py-0.5 rounded-full bg-red-500 text-white">P0紧急·周一必须清仓</span>
        </div>
        <div class="text-red-400 font-bold text-sm">最后收盘价 11.74元 | 浮亏-12.7%</div>
    </div>
    <div class="text-white/80 text-sm leading-relaxed space-y-1">
        <p>• <strong class="text-red-300">核心风险：</strong>7/6周一起主板ST涨跌幅从5%扩至<strong>10%</strong>，单日最大跌停幅度翻倍！</p>
        <p>• <strong class="text-red-300">操作铁律：</strong>周一集合竞价（9:15-9:25）<strong>必须直接挂跌停价不计成本卖出</strong>，任何价格都走，不要犹豫</p>
        <p>• <strong class="text-red-300">逻辑：</strong>ST股基本面持续恶化（已被*ST），涨跌幅扩大后流动性枯竭风险加剧，多等一天多10%跌停风险</p>
        <p>• <strong class="text-red-300">注意：</strong>重签风险揭示书后方可买入ST股，但持仓卖出不受影响；开盘前检查条件单，确保止损单调整为-10%</p>
    </div>
</div>

<div class="bg-gradient-to-r from-red-500/15 to-orange-500/10 border border-red-500/30 rounded-xl p-4">
    <div class="flex items-center justify-between mb-2">
        <div class="flex items-center gap-2">
            <span class="text-lg">🔴</span>
            <span class="text-white font-bold">英维克（002837）</span>
            <span class="text-xs px-2 py-0.5 rounded-full bg-red-500/30 text-red-300">深度破止损-31.5%</span>
        </div>
        <div class="text-red-400 font-bold text-sm">最新价 71.43元 | 成本104.23 | 止损98元</div>
    </div>
    <div class="text-white/80 text-sm leading-relaxed space-y-1">
        <p>• <strong>周五表现：</strong>+0.04%缩量十字星，盘中最高74.41触清仓窗口，近5日主力净流出14.86亿</p>
        <p>• <strong>板块环境：</strong>AI算力/液冷板块跟随半导体整体调整，费半隔夜-5.44%周一仍有压力；但7/2暴跌后超跌有技术性反弹需求</p>
        <p>• <strong class="text-yellow-300">周一操作计划：</strong>反弹至<strong>73-75区间坚决减仓≥1/2</strong>；若<strong>跌破70元无条件全部离场</strong>；不再恋战</p>
        <p>• <strong>空方视角：</strong>主力持续大额流出+板块高位补跌未结束+中报业绩未超预期前缺乏催化，纪律优先</p>
    </div>
</div>

<div class="bg-gradient-to-r from-red-500/15 to-orange-500/10 border border-red-500/30 rounded-xl p-4">
    <div class="flex items-center justify-between mb-2">
        <div class="flex items-center gap-2">
            <span class="text-lg">🔴</span>
            <span class="text-white font-bold">雅克科技（002409）</span>
            <span class="text-xs px-2 py-0.5 rounded-full bg-red-500/30 text-red-300">两日累跌-15.5%险守200</span>
        </div>
        <div class="text-red-400 font-bold text-sm">最新价 199.50元 | 成本108.8 | 浮盈+83.4%</div>
    </div>
    <div class="text-white/80 text-sm leading-relaxed space-y-1">
        <p>• <strong>周五表现：</strong>-6.11%险守200元整数关口，7/2跌停-10%（212.48元），两日累计-15.5%；主力净卖5.43亿，光刻胶流出榜第3</p>
        <p>• <strong>公司回应：</strong>7/2晚澄清"没有六氟化钨相关业务，也没有布局计划"（六氟是7/2杀跌导火索）</p>
        <p>• <strong>基本面：</strong>机构测算H1净利8.05-8.42亿同比+54%-61%，HBM特气/湿电子化学品长协满产，全球仅默克/信越/雅克三家能做高端HBM前驱体</p>
        <p>• <strong class="text-yellow-300">周一操作计划：</strong>底仓1/2观察<strong>200-205元</strong>能否企稳；若反弹至<strong>210-215减1/3</strong>；若<strong>跌破195减至1/4以下</strong>（认错修正）</p>
        <p>• <strong>风险点：</strong>光刻胶/电子化学品板块周五继续大跌-5.74%，板块调整未结束，江波龙业绩炸裂能否带动存储链情绪修复是关键</p>
    </div>
</div>

<div class="bg-gradient-to-r from-yellow-500/15 to-amber-500/10 border border-yellow-500/30 rounded-xl p-4">
    <div class="flex items-center justify-between mb-2">
        <div class="flex items-center gap-2">
            <span class="text-lg">🟡</span>
            <span class="text-white font-bold">铜冠铜箔（301217）</span>
            <span class="text-xs px-2 py-0.5 rounded-full bg-yellow-500/30 text-yellow-300">浮盈+77.4%移动止盈</span>
        </div>
        <div class="text-yellow-400 font-bold text-sm">最新价 154.63元 | 成本87.16 | 止损78.44</div>
    </div>
    <div class="text-white/80 text-sm leading-relaxed space-y-1">
        <p>• <strong>周五表现：</strong>-2.08%盘中击穿150至150.0元获支撑；主力连续3日净卖合计8.3亿</p>
        <p>• <strong>利好：</strong>高频高速铜箔已开始批量供应AI服务器/数据中心客户；公司公告募投项目结项+节余资金补流</p>
        <p>• <strong>板块环境：</strong>铜箔/PCB板块周五获资金净流入（消费电子+39.92亿、元件+28.23亿），深南电路涨停、东山精密净流入15.62亿</p>
        <p>• <strong class="text-yellow-300">操作计划：</strong>移动止盈下移至<strong>150元</strong>（之前160-165减仓窗口已出最高164.56）；反弹至160-165继续减仓；跌破150减仓至底仓</p>
        <p>• <strong>中期逻辑：</strong>AI服务器PCB+高频高速铜箔需求确定性高，但短期涨幅过大（成本→154已+77%）需分批兑现利润</p>
    </div>
</div>

</div>
<div class="mt-4 bg-white/5 rounded-xl p-4 border border-white/10">
    <div class="text-white/80 text-sm font-semibold mb-2">📋 周一操作优先级排序</div>
    <div class="text-white/70 text-xs space-y-1">
        <p><span class="text-red-400 font-bold">9:15-9:25 集合竞价：</span>*ST建艺挂跌停价全部清仓（最高优先级！）</p>
        <p><span class="text-yellow-400 font-bold">9:30-10:00 开盘观察：</span>英维克若高开冲高73-75减仓≥1/2；雅克科技观察200-205支撑</p>
        <p><span class="text-yellow-400 font-bold">盘中：</span>铜冠铜箔反弹160-165继续减仓；英维克破70无条件离场</p>
        <p><span class="text-blue-400 font-bold">整体仓位：</span>周一减仓后控制在3-4成，保留现金等待中报业绩方向明确后再加仓</p>
    </div>
</div>
'''
gen.add_section("💼 持仓周末诊断与周一操作计划", portfolio_html, "💼")

# ===== 7. 下周一预判 =====
pred_html = '''<div class="space-y-3">
<div class="bg-gradient-to-r from-blue-500/20 to-cyan-500/10 border border-blue-500/30 border rounded-xl p-4">
    <div class="flex items-center justify-between mb-2">
        <div class="flex items-center gap-2">
            <span class="text-lg">📊</span>
            <span class="text-white font-semibold">大盘预判：缩量震荡、结构分化延续</span>
        </div>
        <div class="text-right">
            <span class="text-xs text-white/50">置信度</span>
            <span class="text-white font-bold ml-1">65%</span>
        </div>
    </div>
    <p class="text-sm text-white/70 leading-relaxed m-0">
        <strong>多空博弈：</strong>利多（美国非农爆冷→流动性宽松预期+央行1万亿逆回购+中报预增密集披露）vs 利空（费半隔夜-5.44%压制科技+新规落地ST波动+缩量反弹持续性存疑）。预计上证在4000-4080区间震荡，创业板/科创板受半导体拖累或低开后修复。<strong>关键看点：</strong>4000点支撑、3万亿成交能否守住、江波龙业绩能否带动存储链反弹。
    </p>
</div>

<div class="bg-gradient-to-r from-yellow-500/20 to-orange-500/10 border border-yellow-500/30 border rounded-xl p-4">
    <div class="flex items-center justify-between mb-2">
        <div class="flex items-center gap-2">
            <span class="text-lg">⚡</span>
            <span class="text-white font-semibold">题材预判：中报业绩线+机器人/黄金延续</span>
        </div>
        <div class="text-right">
            <span class="text-xs text-white/50">置信度</span>
            <span class="text-white font-bold ml-1">70%</span>
        </div>
    </div>
    <p class="text-sm text-white/70 leading-relaxed m-0">
        <strong>核心主线：</strong>①<strong>中报业绩预增</strong>——存储芯片（江波龙业绩炸裂）、光纤光缆（杭电股份）、券商（国泰海通）；②<strong>人形机器人</strong>——宇树IPO+Optimus量产+大摩上调出货预测，产业趋势最强；③<strong>贵金属/黄金</strong>——降息预期+金价创高，避险逻辑持续；④<strong>军工/商业航天</strong>——长征十号乙7月10-13日首飞窗口。<strong>回避方向：</strong>高位纯题材无业绩兑现的半导体材料/氟化工（补跌未完）、ST板块（新规波动）。
    </p>
</div>

<div class="bg-gradient-to-r from-red-500/20 to-pink-500/10 border border-red-500/30 border rounded-xl p-4">
    <div class="flex items-center justify-between mb-2">
        <div class="flex items-center gap-2">
            <span class="text-lg">⚠️</span>
            <span class="text-white font-semibold">风险预警：四大风险点</span>
        </div>
        <div class="text-right">
            <span class="text-xs text-white/50">置信度</span>
            <span class="text-white font-bold ml-1">75%</span>
        </div>
    </div>
    <p class="text-sm text-white/70 leading-relaxed m-0">
        ①<strong>ST股波动加剧：</strong>周一157+只主板ST涨跌幅翻倍，*ST建艺不计成本清仓，注意ST板块整体可能出现流动性踩踏；②<strong>半导体补跌未结束：</strong>费半-5.44%+SMH连续两日大跌，光刻胶/电子特气高位补跌或延续；③<strong>成交缩量风险：</strong>3.18万亿是6/18以来最低，若继续缩至3万亿以下则反弹乏力；④<strong>中报业绩证伪：</strong>7月中旬后业绩不达预期的高位股可能补跌。
    </p>
</div>
</div>'''
gen.add_section("🎯 下周一（7/6）开盘预判", pred_html, "🎯")

# ===== 8. 交易计划 =====
plan_html = '''<div class="space-y-3">
<div class="bg-white/5 border border-white/10 rounded-xl p-4">
    <div class="flex items-center gap-2 mb-2">
        <span class="text-lg">🚨</span>
        <span class="text-white font-semibold">P0 紧急任务（9:15集合竞价）</span>
    </div>
    <p class="text-sm text-white/70 leading-relaxed m-0">
        <strong>*ST建艺（002789）集合竞价挂跌停价全部清仓！</strong>这是周一最高优先级任务，涨跌幅扩至10%后晚一天可能多亏10%。提前在9:15前设置条件单，不要等开盘观察。
    </p>
</div>
<div class="bg-white/5 border border-white/10 rounded-xl p-4">
    <div class="flex items-center gap-2 mb-2">
        <span class="text-lg">💼</span>
        <span class="text-white font-semibold">持仓减仓计划</span>
    </div>
    <div class="text-sm text-white/70 leading-relaxed space-y-1 m-0">
        <p>• <strong>英维克：</strong>反弹73-75减仓≥1/2；破70无条件全部离场；盘中不抄底不加仓</p>
        <p>• <strong>雅克科技：</strong>底仓1/2观察200-205企稳；反弹210-215减1/3；破195减至1/4以下</p>
        <p>• <strong>铜冠铜箔：</strong>反弹160-165继续减仓；跌破150减至底仓；150为止盈线</p>
    </div>
</div>
<div class="bg-white/5 border border-white/10 rounded-xl p-4">
    <div class="flex items-center gap-2 mb-2">
        <span class="text-lg">🎯</span>
        <span class="text-white font-semibold">新仓方向（轻仓试探）</span>
    </div>
    <div class="text-sm text-white/70 leading-relaxed space-y-1 m-0">
        <p>• <strong>黄金/贵金属：</strong>降息预期升温+金价4135美元，可关注赤峰黄金/四川黄金回调低吸（不追高）</p>
        <p>• <strong>人形机器人：</strong>宇树IPO+Optimus催化最强，但周一可能高开，等分歧后低吸龙头（埃斯顿/三花智控/绿的谐波）</p>
        <p>• <strong>中报业绩线：</strong>存储芯片（江波龙已大涨，关注佰维存储/香农芯创补涨）、光纤光缆（杭电股份）</p>
        <p>• <strong>券商：</strong>国泰海通业绩炸裂，关注低估值券商补涨机会</p>
    </div>
</div>
<div class="bg-white/5 border border-white/10 rounded-xl p-4">
    <div class="flex items-center gap-2 mb-2">
        <span class="text-lg">📝</span>
        <span class="text-white font-semibold">仓位与纪律</span>
    </div>
    <div class="text-sm text-white/70 leading-relaxed space-y-1 m-0">
        <p>• <strong>目标仓位：</strong>周一减仓后整体仓位降至3-4成，保留6-7成现金</p>
        <p>• <strong>仓位原则：</strong>在英维克/雅克科技/铜冠铜箔未完成减仓前，不开新仓</p>
        <p>• <strong>风控铁律：</strong>任何新仓位不超过总仓位10%；中报季严格止损，业绩证伪个股绝不补仓</p>
        <p>• <strong>时间窗口：</strong>7月中旬前主动披露业绩公司以预喜为主；7月下旬-8月是业绩证伪高发期</p>
    </div>
</div>
</div>'''
gen.add_section("📋 周一交易计划", plan_html, "📋")

# ===== 9. 市场情绪 =====
sentiment_html = '''
<div class="bg-gradient-to-r from-blue-500/30 to-cyan-500/20 border border-white/10 rounded-xl p-5 mb-4">
    <div class="text-center">
        <div class="text-4xl font-black text-blue-400 mb-1">45</div>
        <div class="text-sm text-white/70">恐惧贪婪指数 · 偏恐惧（较周五60大幅回落）</div>
        <div class="w-full h-2 bg-white/10 rounded-full overflow-hidden mt-3">
            <div class="h-full bg-gradient-to-r from-green-500 via-yellow-500 to-red-500 rounded-full" style="width: 45%"></div>
        </div>
    </div>
</div>
<div class="grid grid-cols-2 md:grid-cols-4 gap-3">
    <div class="text-center bg-white/5 rounded-lg p-3">
        <div class="text-lg mb-1">📊</div>
        <div class="text-lg font-bold text-white">弱修复</div>
        <div class="text-xs text-white/50 mt-1">周五定性</div>
    </div>
    <div class="text-center bg-white/5 rounded-lg p-3">
        <div class="text-lg mb-1">📉</div>
        <div class="text-lg font-bold text-white">3.18万亿</div>
        <div class="text-xs text-white/50 mt-1">缩量警惕</div>
    </div>
    <div class="text-center bg-white/5 rounded-lg p-3">
        <div class="text-lg mb-1">🔄</div>
        <div class="text-lg font-bold text-white">高低切换</div>
        <div class="text-xs text-white/50 mt-1">风格特征</div>
    </div>
    <div class="text-center bg-white/5 rounded-lg p-3">
        <div class="text-lg mb-1">⏰</div>
        <div class="text-lg font-bold text-white">中报季</div>
        <div class="text-xs text-white/50 mt-1">核心主线</div>
    </div>
</div>
<div class="mt-4 bg-white/5 rounded-xl p-4 border border-white/10">
    <div class="text-white font-bold mb-2 flex items-center gap-2"><span>🌡️</span><span>周末情绪温度计</span></div>
    <div class="text-white/70 text-sm leading-relaxed">
        经历7/2暴跌+7/3弱修复后，市场情绪从恐慌（30以下）回升至中性偏弱。周末非农数据利好全球流动性但美股芯片崩盘形成对冲，中报业绩线（江波龙）提供新的做多方向。下周一是交易新规落地日+ST板块波动加剧日，整体以<strong>防御为主、减仓优先、仓位控制</strong>为核心策略。等待中报业绩进一步明朗、成交缩量企稳后再择机加仓。
    </div>
</div>
'''
gen.add_section("🌡️ 市场情绪温度计", sentiment_html, "🌡️")

# ===== 10. 风险提示 =====
risk_html = '''<div class="grid md:grid-cols-2 lg:grid-cols-4 gap-3">
<div class="bg-red-500/20 border border-red-500/30 border rounded-xl p-4">
    <div class="flex items-center gap-2 mb-2">
        <span class="text-lg">🚨</span>
        <span class="text-white font-semibold">ST股波动风险</span>
        <span class="ml-auto text-xs font-bold text-red-400 px-2 py-0.5 rounded-full bg-white/10">高风险</span>
    </div>
    <p class="text-sm text-white/60 m-0">7/6起主板ST涨跌幅翻倍至10%，*ST建艺必须周一集合竞价清仓，避免连续跌停损失扩大。</p>
</div>
<div class="bg-red-500/20 border border-red-500/30 border rounded-xl p-4">
    <div class="flex items-center gap-2 mb-2">
        <span class="text-lg">⚠️</span>
        <span class="text-white font-semibold">半导体补跌风险</span>
        <span class="ml-auto text-xs font-bold text-red-400 px-2 py-0.5 rounded-full bg-white/10">高风险</span>
    </div>
    <p class="text-sm text-white/60 m-0">费半隔夜-5.44%连续两日暴跌，光刻胶/电子特气/氟化工高位补跌未完，雅克科技承压。</p>
</div>
<div class="bg-yellow-500/20 border border-yellow-500/30 border rounded-xl p-4">
    <div class="flex items-center gap-2 mb-2">
        <span class="text-lg">📉</span>
        <span class="text-white font-semibold">成交缩量风险</span>
        <span class="ml-auto text-xs font-bold text-yellow-400 px-2 py-0.5 rounded-full bg-white/10">中风险</span>
    </div>
    <p class="text-sm text-white/60 m-0">成交缩至3.18万亿（6/18以来最低），若继续缩量至3万亿以下，反弹缺乏量能支撑难以持续。</p>
</div>
<div class="bg-yellow-500/20 border border-yellow-500/30 border rounded-xl p-4">
    <div class="flex items-center gap-2 mb-2">
        <span class="text-lg">📋</span>
        <span class="text-white font-semibold">中报业绩证伪</span>
        <span class="ml-auto text-xs font-bold text-yellow-400 px-2 py-0.5 rounded-full bg-white/10">中风险</span>
    </div>
    <p class="text-sm text-white/60 m-0">7月中下旬进入中报密集披露期，业绩不及预期的高位股可能出现大幅补跌，需回避纯题材炒作个股。</p>
</div>
</div>
<div class="mt-4 text-center text-xs text-white/30">
    ⚠️ 本报告基于公开信息整理，不构成投资建议。市场有风险，投资需谨慎。数据来源：财联社、东方财富、新华财经、华尔街见闻、新浪财经等。
</div>'''
gen.add_section("⚠️ 风险提示与免责声明", risk_html, "⚠️")

# ===== 生成并保存 =====
html = gen.render()

output_path = 'docs/aftermarket/20260704_盘后速递.html'
os.makedirs(os.path.dirname(output_path), exist_ok=True)
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(html)

print(f"✅ 盘后速递（假期版）生成成功！")
print(f"   路径: {output_path}")
print(f"   大小: {len(html):,} 字符 ({os.path.getsize(output_path):,} 字节)")
