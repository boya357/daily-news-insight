# -*- coding: utf-8 -*-
"""
华为自研HBM深度分析报告生成脚本
"""
import sys
import os
sys.path.insert(0, '/root/daily-news-insight/v3')
from generators.deep_dive import DeepDiveGenerator
from components.data import StatCard, CompareTable
from components.special import RiskAlert

gen = DeepDiveGenerator(
    title="华为自研HBM深度分析与产业链TOP10",
    subtitle="五层W2W混合键合·4096bit位宽·内存控制器集成"
)

# ===== 1. 核心观点 =====
gen.add_summary(
    core_view=(
        "华为自研HBM不是追赶者，而是换道者。ISSCC 2027披露的五层W2W混合键合、4096bit位宽、"
        "内存控制器集成三件套，走出了一条与三星/海力士TSV+微凸块完全不同的技术路线。"
        "核心结论：①前驱体要用，而且用量结构发生变化——DRAM制造端前驱体需求与常规HBM一致，"
        "但封装端从微凸块UBM转向混合键合界面，次磷酸钠等化学镀耗材不降反升；"
        "②受益排序：长电科技（封装）> 雅克科技（前驱体）> 华海诚科（塑封料）> 兴发集团（次磷酸钠）；"
        "③短期是情绪催化，真正订单兑现要看2027下半年昇腾960放量。"
    ),
    bull_points=[
        "技术路线换道超车：W2W混合键合+内存控制器集成，位宽是HBM4标准的2倍",
        "昇腾950已量产搭载：950PR(128GB/1.6TB/s)和950DT(144GB/4TB/s)在售，不是PPT",
        "国产替代刚需：美国HBM出口管制下，华为自研是国内AI算力的唯一高端路径",
        "产业链带动明确：先进封装、前驱体、塑封料、键合设备全链条受益",
        "ISSCC 2027四篇论文连发：3D集成路线图完整，不是单点突破"
    ],
    bear_points=[
        "良率不确定性：五层W2W混合键合良率爬坡难度大，量产规模受限于良率",
        "DRAM颗粒仍依赖外部：华为做的是架构和封装，DRAM颗粒仍需长鑫等供应",
        "短期情绪大于业绩：当前昇腾950HBM产能有限，订单贡献2027年才会显著",
        "海外技术迭代快：三星/海力士HBM4已量产，HBM4E/HBM5在路上，代差仍存",
        "设备封锁风险：高端混合键合设备仍依赖进口，存在断供风险"
    ]
)

# ===== 2. 关键数据 =====
gen.add_stat_cards([
    StatCard(title="位宽", value="4096bit", subtitle="HBM4标准的2倍", trend_up=True, variant="purple"),
    StatCard(title="堆叠层数", value="5层", subtitle="W2W晶圆混合键合", trend_up=True, variant="blue"),
    StatCard(title="通道数", value="64通道", subtitle="集成内存控制器", trend_up=True, variant="indigo"),
    StatCard(title="昇腾950DT带宽", value="4TB/s", subtitle="950PR为1.6TB/s", trend_up=True, variant="blue"),
], cols=4)

# ===== 3. 技术路线深度解析 =====
tech_analysis = """
<h3 class="text-xl font-bold mb-4 text-white">华为HBM技术路线：换道超车的三大核心创新</h3>

<p class="mb-4 text-gray-200 leading-relaxed">
传统HBM的标准路线是<strong>TSV硅通孔+微凸块</strong>——用TSV把多层DRAM垂直打通，
再通过微凸块（micro-bump）实现层间和芯片与中介层之间的连接。三星、SK海力士、美光三家都是这条路子。
华为走的是一条<strong>完全不同的定制化路线</strong>，核心创新有三点：
</p>

<div class="grid grid-cols-1 md:grid-cols-3 gap-4 mb-6">
    <div class="bg-white/5 backdrop-blur rounded-xl p-4 border border-purple-500/30">
        <div class="text-3xl mb-2">🔬</div>
        <h4 class="font-bold text-purple-300 mb-2">W2W混合键合</h4>
        <p class="text-sm text-gray-300">五层晶圆对晶圆（Wafer-on-Wafer）铜-铜直接键合，替代传统TSV+微凸块方案。
        理论上互连密度更高、信号距离更短、功耗更低。混合键合原本行业预期要到HBM4E/HBM5（16层以上）才会导入，
        华为在5层就用了，属于"提前下注"。</p>
    </div>
    <div class="bg-white/5 backdrop-blur rounded-xl p-4 border border-blue-500/30">
        <div class="text-3xl mb-2">📊</div>
        <h4 class="font-bold text-blue-300 mb-2">4096bit位宽</h4>
        <p class="text-sm text-gray-300">HBM4标准位宽是2048bit，华为直接翻倍到4096个DQ接口，
        64通道并行。这意味着在相同频率下，带宽就是标准HBM4的两倍。
        代价是I/O密度极高，对封装和测试的难度指数级上升。</p>
    </div>
    <div class="bg-white/5 backdrop-blur rounded-xl p-4 border border-indigo-500/30">
        <div class="text-3xl mb-2">🎮</div>
        <h4 class="font-bold text-indigo-300 mb-2">内存控制器集成</h4>
        <p class="text-sm text-gray-300">把内存控制器"塞进"堆叠体系内部，而不是放在CPU/GPU端。
        控制器靠近存储阵列，可以进一步降低延迟和功耗。
        这是架构层面的创新，不是简单的工艺升级，体现了华为的系统级设计能力。</p>
    </div>
</div>

<h4 class="font-bold text-lg mb-3 text-amber-300">⚠️ 关键问题：用不用前驱体？</h4>
<p class="mb-3 text-gray-200 leading-relaxed">
<strong>答案是：用，而且用量结构发生了重要变化。</strong>需要分两个层面来看：
</p>

<div class="bg-white/5 backdrop-blur rounded-xl p-4 border border-amber-500/30 mb-4">
    <h5 class="font-bold text-amber-300 mb-2">① DRAM制造端：前驱体用量与常规HBM基本一致</h5>
    <p class="text-sm text-gray-300 mb-2">
    HBM的核心是多层DRAM堆叠。不管用TSV还是混合键合，DRAM颗粒本身的制造工艺没有本质变化——
    都需要ALD/CVD沉积介电层、阻挡层、金属互连层，这些都离不开前驱体材料。
    </p>
    <p class="text-sm text-gray-300">
    <strong>雅克科技（UP Chemical）</strong>作为SK海力士HBM4/HBM5介电层High-k前驱体的核心供应商，
    其技术能力同样可以适配华为自研HBM的DRAM制造需求。市场传闻雅克正在联合华为开发HBM4级前驱体，
    如果属实，这将是国产HBM材料链的重要突破。
    </p>
</div>

<div class="bg-white/5 backdrop-blur rounded-xl p-4 border border-green-500/30">
    <h5 class="font-bold text-green-300 mb-2">② 封装端：微凸块减少≠化学镀耗材减少，反而可能增加</h5>
    <p class="text-sm text-gray-300 mb-2">
    一个常见的误读是：混合键合用铜-铜直接键合替代了微凸块，所以UBM（凸点下金属层）的化学镀耗材会减少。
    但实际情况恰恰相反——
    </p>
    <p class="text-sm text-gray-300">
    华为方案有4096个DQ超大I/O规模，晶圆边缘、划片道、可靠性监控阵列、海量测试PAD、
    RDL重布线引出焊盘数量<strong>成倍增加</strong>。这些焊盘和测试结构都需要
    <strong>ENEPIG化学镀镍钯金</strong>做防护，而<strong>次磷酸钠</strong>正是化学镀镍磷工艺的核心还原剂。
    叠加混合键合对晶圆界面洁净度、镀层均匀度、杂质控制的原子级要求，
    只能使用低重金属杂质的<strong>半导体存储专用高纯牌号</strong>次磷酸钠。
    </p>
    <p class="text-sm text-gray-300 mt-2">
    <strong>结论</strong>：封装端的化学镀耗材用量不是下降，而是因为I/O规模翻倍和更高的纯度要求而上升。
    这对<strong>兴发集团</strong>（国内存储级高纯次磷酸钠核心供应商，2万吨/年产能）是直接利好。
    </p>
</div>

<h4 class="font-bold text-lg mb-3 mt-6 text-cyan-300">📦 塑封料呢？华海诚科受益几何？</h4>
<p class="text-gray-200 leading-relaxed">
HBM封装最终还是需要环氧塑封料（EMC/GMC）来做保护和散热。HBM堆叠层数越多，
对塑封料的导热性、低应力、低α粒子要求就越高。华海诚科的颗粒状环氧塑封料（GMC）
可以用于HBM封装，已通过部分客户认证。其韩国子公司具备开发HBM所需高导热EMC的技术能力。
不过需要注意的是，华为W2W混合键合方案中，塑封料是必要但非核心增量环节，
弹性不如前驱体和封装环节那么大。
</p>
"""
gen.add_analysis_section("🔬 技术路线深度解析", tech_analysis, icon="chip")

# ===== 4. 竞争格局对比 =====
headers = ["维度", "华为定制HBM", "SK海力士HBM4", "三星HBM4", "长鑫HBM3E"]
rows = [
    ["技术路线", "W2W混合键合+控制器集成", "TSV+微凸块", "TSV+微凸块", "TSV+微凸块（DUV）"],
    ["位宽", "4096bit（64通道）", "2048bit", "2048bit", "1024bit"],
    ["堆叠层数", "5层（W2W）", "12层（HBM4）", "12层（HBM4）", "12层（HBM3E级）"],
    ["带宽/性能", "950DT: 4TB/s", "1.6TB/s+（单颗）", "1.6TB/s+", "对标HBM3水平"],
    ["量产状态", "昇腾950已搭载（小批量）", "2026年量产", "2026年量产", "良率20-30%，2027小规模"],
    ["代表客户", "华为昇腾/盘古", "英伟达、AMD", "微软、Meta", "华为、寒武纪、沐曦"],
    ["核心优势", "架构创新、位宽翻倍、自主可控", "良率70%+、产能最大、EUV制程", "产能扩张快、客户多元化", "本土唯一能量产、国产替代"],
    ["核心劣势", "DRAM颗粒仍需外购、良率待验证", "产能被长约锁定", "良率追赶中", "良率低（20-30%）、落后一代"],
]
gen.add_competitive_analysis(headers=headers, rows=rows, highlight_rows=[0, 1, 2])

# ===== 5. 产业链价值分布 =====
chain_analysis = """
<h3 class="text-xl font-bold mb-4 text-white">华为HBM产业链价值分布与A股标的映射</h3>

<p class="mb-4 text-gray-200 leading-relaxed">
华为自研HBM产业链可以分为<strong>五个层级</strong>：DRAM颗粒→制造材料→封装材料→封装代工→测试设备。
国产替代程度从下往上递减，真正有业绩弹性的集中在材料和封装环节。
</p>

<div class="space-y-3">
    <div class="bg-white/5 backdrop-blur rounded-xl p-4 border border-purple-500/30">
        <div class="flex justify-between items-center mb-2">
            <h4 class="font-bold text-purple-300">第1层：DRAM颗粒（国产化率最低）</h4>
            <span class="text-xs px-2 py-1 rounded bg-red-500/20 text-red-300">国产替代早期</span>
        </div>
        <p class="text-sm text-gray-300">
        华为自研HBM的核心是架构设计和封装集成，但DRAM颗粒本身仍需外部供应。
        国内主要依赖<strong>长鑫存储</strong>（已上市，HBM3E良率20-30%，2027年小规模量产）。
        这一层A股标的最少，但弹性最大——一旦良率突破，空间巨大。
        </p>
    </div>
    
    <div class="bg-white/5 backdrop-blur rounded-xl p-4 border border-blue-500/30">
        <div class="flex justify-between items-center mb-2">
            <h4 class="font-bold text-blue-300">第2层：制造材料（前驱体/靶材/特气）</h4>
            <span class="text-xs px-2 py-1 rounded bg-yellow-500/20 text-yellow-300">部分国产替代</span>
        </div>
        <p class="text-sm text-gray-300">
        DRAM制造所需的前驱体、靶材、电子特气等。<strong>雅克科技</strong>（UP Chemical）
        是SK海力士HBM4/HBM5前驱体核心供应商，同时联合华为开发，卡位最硬。
        <strong>江丰电子</strong>超高纯靶材已批量应用于HBM制造。
        <strong>金宏气体</strong>高纯二氧化碳供应SK海力士。
        </p>
    </div>
    
    <div class="bg-white/5 backdrop-blur rounded-xl p-4 border border-green-500/30">
        <div class="flex justify-between items-center mb-2">
            <h4 class="font-bold text-green-300">第3层：封装材料（塑封料/硅微粉/化学镀）</h4>
            <span class="text-xs px-2 py-1 rounded bg-green-500/20 text-green-300">国产替代加速</span>
        </div>
        <p class="text-sm text-gray-300">
        <strong>华海诚科</strong>：国内唯一量产HBM专用GMC塑封料，已过长电/通富认证。
        <strong>联瑞新材</strong>：Low-α球形硅微粉/氧化铝，全球仅三家量产。
        <strong>兴发集团</strong>：存储级高纯次磷酸钠核心供应商，2万吨/年产能全球最大，
        W2W混合键合路线下ENEPIG化学镀需求上升反而更受益。
        </p>
    </div>
    
    <div class="bg-white/5 backdrop-blur rounded-xl p-4 border border-orange-500/30">
        <div class="flex justify-between items-center mb-2">
            <h4 class="font-bold text-orange-300">第4层：封装代工（先进封装/混合键合）</h4>
            <span class="text-xs px-2 py-1 rounded bg-blue-500/20 text-blue-300">直接受益最大</span>
        </div>
        <p class="text-sm text-gray-300">
        <strong>长电科技</strong>：国内封测龙头，XDFOI先进封装平台，华为核心合作伙伴，
        HBM封装+机器人芯片封测双线卡位，是华为HBM封装最直接的受益标的。
        <strong>通富微电</strong>：5nm Chiplet已量产，HBM封测布局者。
        <strong>盛合晶微</strong>（未上市）：混合键合3DIC技术平台。
        </p>
    </div>
    
    <div class="bg-white/5 backdrop-blur rounded-xl p-4 border border-pink-500/30">
        <div class="flex justify-between items-center mb-2">
            <h4 class="font-bold text-pink-300">第5层：测试与设备（测试机/键合设备/量测）</h4>
            <span class="text-xs px-2 py-1 rounded bg-purple-500/20 text-purple-300">国产替代空间大</span>
        </div>
        <p class="text-sm text-gray-300">
        <strong>精智达</strong>：HBM测试设备，深度绑定长鑫。
        <strong>赛腾股份</strong>：子公司Optima国内唯一HBM量测设备量产企业。
        <strong>快克智能</strong>：TCB热压键合机适配HBM3E/HBM4，已通过华为昇腾量产验证。
        <strong>拓荆科技</strong>：混合键合设备研发中。
        </p>
    </div>
</div>
"""
gen.add_analysis_section("🏭 产业链价值分布", chain_analysis, icon="factory")

# ===== 6. 核心标的排序TOP10 =====
top10_headers = ["排名", "标的", "代码", "受益环节", "关联度", "核心逻辑", "弹性评级"]
top10_rows = [
    ["S1", "长电科技", "600584", "先进封装代工", "★★★★★",
     "华为HBM封装核心合作伙伴，XDFOI平台+混合键合布局，昇腾链直接受益", "S级"],
    ["S2", "雅克科技", "002409", "HBM前驱体材料", "★★★★☆",
     "SK海力士HBM4前驱体核心供应商，联合华为开发HBM前驱体，卡位最硬", "S级"],
    ["S3", "兴发集团", "600141", "高纯次磷酸钠", "★★★★☆",
     "存储级高纯次磷酸钠全球最大产能(2万吨/年)，W2W混合键合ENEPIG需求上升受益", "S级"],
    ["A1", "华海诚科", "688535", "HBM塑封料GMC", "★★★★",
     "国内唯一量产HBM专用GMC塑封料，已过长电/通富认证，韩国子公司高导热EMC技术", "A级"],
    ["A2", "快克智能", "603203", "键合设备", "★★★★",
     "TCB热压键合机适配HBM3E/HBM4堆叠，已通过华为昇腾量产验证并联合申报专利", "A级"],
    ["A3", "联瑞新材", "688300", "Low-α硅微粉", "★★★☆",
     "全球仅三家量产Low-α球形二氧化硅/氧化铝，HBM封装填料用量随层数增长", "A级"],
    ["B1", "精智达", "688627", "HBM测试设备", "★★★",
     "HBM测试机，深度绑定长鑫，存储测试机国产化率仅8-10%，替代空间最大", "B级"],
    ["B2", "赛腾股份", "603283", "HBM量测设备", "★★★",
     "子公司Optima国内唯一HBM量测设备量产企业，键合空洞检测需求随层数增长", "B级"],
    ["B3", "江丰电子", "300666", "超高纯靶材", "★★☆",
     "超高纯硅靶、钨靶、铜锰合金靶已批量应用于HBM制造，材料平台型公司", "B级"],
    ["B4", "通富微电", "002156", "先进封测", "★★☆",
     "5nm Chiplet已大规模量产，HBM封测布局者，受益于封测景气度整体上行", "B级"],
]

table = CompareTable(headers=top10_headers, rows=top10_rows, highlight_rows=[0, 1, 2])
from components.layout import Section
gen.report.add(Section("🏆 核心标的排序TOP10", table))

# ===== 7. 持仓股影响分析 =====
holding_analysis = """
<h3 class="text-xl font-bold mb-4 text-white">持仓股影响深度分析</h3>

<div class="space-y-4">
    <div class="bg-white/5 backdrop-blur rounded-xl p-4 border border-green-500/30">
        <div class="flex justify-between items-center mb-2">
            <h4 class="font-bold text-green-300">✅ 雅克科技（002409）：最直接受益，前驱体卡位最硬</h4>
            <span class="px-3 py-1 rounded-full bg-green-500/20 text-green-300 text-sm font-bold">S级受益</span>
        </div>
        <p class="text-sm text-gray-300 mb-2">
        <strong>影响性质：实质性利好</strong>。雅克子公司UP Chemical是SK海力士HBM4/HBM5前驱体的核心供应商，
        技术能力全球领先。同时市场传闻雅克正在联合华为开发HBM级前驱体，如果属实，
        意味着其前驱体技术将同时覆盖海外龙头和国产自主两条线。
        </p>
        <p class="text-sm text-gray-300 mb-2">
        <strong>用量判断</strong>：DRAM制造端前驱体用量与常规HBM基本一致，
        因为DRAM颗粒本身的沉积工艺没有本质变化。封装端W2W混合键合虽然减少了微凸块，
        但增加了大量测试PAD和RDL引出焊盘的化学镀需求，前驱体总体需求不减反增。
        </p>
        <p class="text-sm text-amber-300">
        ⚠️ 短期催化：昨日跌停（-9.92%）主要受费城半导体暴跌和TrendForce存储下修影响，
        华为HBM消息有望成为反弹催化剂。但需注意当前71.68元已接近前期低点，
        反弹减仓纪律不变——75元以上减1/3，80元以上再减1/3。
        </p>
    </div>
    
    <div class="bg-white/5 backdrop-blur rounded-xl p-4 border border-blue-500/30">
        <div class="flex justify-between items-center mb-2">
            <h4 class="font-bold text-blue-300">✅ 长电科技（600584）：封装环节最大受益方</h4>
            <span class="px-3 py-1 rounded-full bg-blue-500/20 text-blue-300 text-sm font-bold">S级受益</span>
        </div>
        <p class="text-sm text-gray-300 mb-2">
        <strong>影响性质：实质性利好</strong>。长电是国内封测龙头，XDFOI先进封装平台已量产，
        与华为在昇腾芯片封装上有长期合作。华为自研HBM采用W2W混合键合路线，
        需要先进封装厂配合完成晶圆键合、堆叠、测试等环节，长电是最可能的国内合作伙伴。
        </p>
        <p class="text-sm text-gray-300 mb-2">
        <strong>催化剂</strong>：华为HBM量产规模扩大将直接拉动长电先进封装业务量。
        长电今年资本开支已上调至182亿，65亿定增投向高性能计算封装，产能储备充足。
        </p>
        <p class="text-sm text-amber-300">
        ⚠️ 操作建议：现价47.19元，处于历史低位。45元以下可加仓1/4，
        42元以下再加1/4，跌破40元止损。反弹至49元以上减1/4。
        </p>
    </div>
    
    <div class="bg-white/5 backdrop-blur rounded-xl p-4 border border-purple-500/30">
        <div class="flex justify-between items-center mb-2">
            <h4 class="font-bold text-purple-300">✅ 华海诚科（688535）：塑封料环节受益，弹性次之</h4>
            <span class="px-3 py-1 rounded-full bg-purple-500/20 text-purple-300 text-sm font-bold">A级受益</span>
        </div>
        <p class="text-sm text-gray-300 mb-2">
        <strong>影响性质：情绪+基本面双重利好</strong>。华海诚科GMC塑封料可用于HBM封装，
        已通过部分客户认证。韩国子公司具备开发HBM高导热EMC的技术能力。
        华为HBM量产将增加对高端塑封料的需求。
        </p>
        <p class="text-sm text-gray-300 mb-2">
        <strong>注意事项</strong>：塑封料在HBM总价值量中的占比低于前驱体和封装代工，
        弹性相对较小。而且华海诚科HBM相关收入目前占比仍低，需要跟踪认证和放量进度。
        </p>
        <p class="text-sm text-amber-300">
        ⚠️ 操作建议：现价61.00元，昨日跌停（-10.43%）。60元以下轻仓1/5，
        55元以下加1/5，跌破50元止损。反弹65元以上减1/3。
        </p>
    </div>
    
    <div class="bg-white/5 backdrop-blur rounded-xl p-4 border border-gray-500/30">
        <div class="flex justify-between items-center mb-2">
            <h4 class="font-bold text-gray-300">➖ 风华高科、铜冠铜箔、英维克、*ST建艺：弱关联或间接影响</h4>
            <span class="px-3 py-1 rounded-full bg-gray-500/20 text-gray-300 text-sm font-bold">弱受益</span>
        </div>
        <p class="text-sm text-gray-300">
        <strong>风华高科</strong>（MLCC）：与HBM无直接关联，MLCC是被动元件，
        受益于AI算力整体扩张但不是HBM直接标的。Q3净利+470%业绩拐点明确，优先加仓标的不变。
        </p>
        <p class="text-sm text-gray-300 mt-2">
        <strong>铜冠铜箔</strong>：PCB铜箔与HBM无直接关系。AI服务器PCB用铜箔有间接利好，
        但HBM本身不需要铜箔。
        </p>
        <p class="text-sm text-gray-300 mt-2">
        <strong>英维克</strong>：液冷散热。HBM功耗高、散热需求大，对液冷是间接利好，
        但逻辑链条较长，主要还是看AI算力整体扩张。
        </p>
        <p class="text-sm text-gray-300 mt-2">
        <strong>*ST建艺</strong>：建筑装饰，与HBM完全无关。
        </p>
    </div>
</div>
"""
gen.add_analysis_section("📊 持仓股影响分析", holding_analysis, icon="chart")

# ===== 8. 催化时间线 =====
gen.add_timeline([
    {"date": "2026年11月23日", "title": "IEEE公布ISSCC 2027议程，华为4篇论文入选，含定制HBM方案", "type": "info"},
    {"date": "2026年11月25日", "title": "科创板日报报道：昇腾950系列已搭载自研HBM", "type": "success"},
    {"date": "2027年2月16日", "title": "ISSCC 2027华为正式发表论文，披露技术细节", "type": "warning"},
    {"date": "2027年Q1", "title": "昇腾960预计送样，下一代HBM容量翻倍、带宽2.5倍", "type": "warning"},
    {"date": "2027年Q3", "title": "昇腾960预计放量，全年规划出货40-50万张", "type": "danger"},
    {"date": "2027年下半年", "title": "长鑫HBM3E产能爬坡至月产5万片晶圆", "type": "info"},
], title="📅 催化时间线与操作节奏")

# ===== 9. 风险提示 =====
gen.add_risk_section([
    "**良率风险**：五层W2W混合键合工艺难度极高，良率爬坡不及预期将直接影响量产规模和成本",
    "**设备封锁风险**：高端混合键合设备仍依赖进口，美国进一步出口管制可能影响产能扩张",
    "**DRAM颗粒供应风险**：华为做架构但DRAM颗粒仍需外购，长鑫良率不足可能成为瓶颈",
    "**技术迭代风险**：三星/海力士HBM4已量产、HBM4E/HBM5在研，华为技术路线能否持续领先存疑",
    "**业绩兑现风险**：当前华为HBM出货量有限，对产业链公司的业绩贡献2027年才会显著，短期是情绪驱动",
    "**市场情绪风险**：当前科技板块处于下跌趋势中，利好可能被市场解读为「利好出尽」",
    "**信息来源风险**：部分信息来自渠道调研和会议议程草案，具体指标和量产时间以华为官方公告为准",
])

# ===== 10. 投资结论 =====
gen.add_conclusion(
    conclusion=(
        "华为自研HBM是国产AI算力自主可控的里程碑事件，技术路线选择W2W混合键合+4096bit位宽+内存控制器集成，"
        "走出了差异化路径。前驱体必用且封装端化学镀耗材需求上升，是最容易被误读的点。\n\n"
        "操作策略：①核心受益标的（长电科技、雅克科技）可利用本轮情绪修复"
        "逢低加仓底仓，但反弹后按纪律减仓机动仓，不追高；"
        "②弹性标的（兴发集团、华海诚科、快克智能）适合小仓位博弈；"
        "③真正的趋势性机会要看2027年Q3昇腾960放量和长鑫良率爬坡，"
        "在此之前以波段操作为主；④总仓位控制在5-6成，保留现金应对加息等宏观风险。"
    ),
    rating="推荐"
)

# 保存并发布
result = gen.publish(
    title="华为自研HBM深度分析与产业链TOP10",
    report_type="industry_chain",
    filename="20261126_华为自研HBM深度分析与产业链TOP10.html",
    excerpt="ISSCC 2027重磅：华为五层W2W混合键合+4096bit位宽+内存控制器集成，走出差异化HBM路线。前驱体必用且封装端化学镀需求上升，长电/雅克/兴发/华海诚科受益排序与持仓影响深度分析。",
    auto_deploy=True
)

print("发布结果：", result)
