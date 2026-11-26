# -*- coding: utf-8 -*-
"""
国产算力双雄：华为HBM × 壁仞BR20X 产业链共振分析
"""
import sys
sys.path.insert(0, '/root/daily-news-insight/v3')
from generators.deep_dive import DeepDiveGenerator
from components.data import StatCard, CompareTable
from components.layout import Section

gen = DeepDiveGenerator(
    title="国产算力双雄：华为HBM×壁仞BR20X产业链共振深度分析",
    subtitle="两大自主可控里程碑同日发酵，先进封装/HBM材料/国产GPU全链条受益排序"
)

# ===== 1. 核心观点 =====
gen.add_summary(
    core_view=(
        "11月25-26日，国产算力迎来两大里程碑级催化同日发酵："
        "①华为ISSCC 2027连发四篇3D集成论文，自研HBM五层W2W混合键合+4096bit位宽，技术路线换道超车；"
        "②壁仞科技主动回应股价异动，BR20X开箱性能达H200水平、已向多个头部客户送测、BIS清单后全面国产替代。"
        "两条消息看似独立，实则指向同一个核心逻辑——**国产算力自主可控正在从「有没有」进入「行不行」的验证期**。"
        "产业链受益顺序：先进封装（量价齐升确定性最高）> HBM材料（前驱体/塑封料/次磷酸钠）> "
        "国产GPU（弹性大但分化剧烈）> 设备/测试（长期替代空间）。"
    ),
    bull_points=[
        "双催化同日发酵：华为HBM技术突破+壁仞BR20X送测，国产算力自主可控叙事持续强化",
        "先进封装是共同受益环节：无论华为昇腾还是壁仞BR20X，都需要高端先进封测产能",
        "壁仞BIS清单后全面国产替代：自2023年入清单以来未采购受管制物项，供应链安全得到厂方确认",
        "国产GPU份额逼近90%：TrendForce预计2026年中国高端AI芯片市场国产份额接近90%",
        "政策+产业共振：十五五规划将先进封装上升为独立战略方向，大基金三期持续加码",
        "持仓直接受益：长电科技（封装）、雅克科技（前驱体）、华海诚科（塑封料）三箭齐发"
    ],
    bear_points=[
        "短期情绪驱动大于业绩兑现：壁仞BR20X 2027年才商业化，华为HBM当前产能有限",
        "国产GPU板块估值回调：壁仞从高点跌81%，A股GPU公司跌幅45-70%，板块风险偏好下行",
        "BIS管制实际影响仍存：虽然壁仞称已替代，但先进制程产能和良率仍是瓶颈",
        "技术代差仍显著：华为HBM和壁仞BR20X对标H200水平，英伟达Rubin/HBM4E已在路上",
        "良率是最大不确定性：华为W2W混合键合五层良率、壁仞BR20X量产良率均待验证",
        "全球AI资本开支预期分化：近期算力供给过剩讨论升温，可能压制板块整体估值"
    ]
)

# ===== 2. 关键数据 =====
gen.add_stat_cards([
    StatCard(title="华为HBM位宽", value="4096bit", subtitle="HBM4标准的2倍", trend_up=True, variant="purple"),
    StatCard(title="壁仞BR20X性能", value="H200级", subtitle="已向头部客户送测", trend_up=True, variant="blue"),
    StatCard(title="国产GPU份额", value="~90%", subtitle="2026年中国高端AI芯片", trend_up=True, variant="green"),
    StatCard(title="壁仞H1营收", value="12.36亿", subtitle="同比+1997.6%", trend_up=True, variant="indigo"),
], cols=4)

# ===== 3. 双雄对比深度解析 =====
duel_analysis = """
<h3 class="text-xl font-bold mb-4 text-white">国产算力双雄对比：两条路线，同一个目标</h3>

<p class="mb-4 text-gray-200 leading-relaxed">
华为和壁仞代表了国产算力自主可控的两条不同路径——华为走的是<strong>「系统级整合+架构创新」</strong>路线，
从芯片设计到封装到HBM全栈自研，用架构创新弥补制程差距；壁仞走的是<strong>「通用GPU+全国产供应链」</strong>路线，
对标英伟达通用计算架构，在BIS管制下实现供应链全面国产化。两条路线各有优劣，但最终都指向同一个目标：
<strong>摆脱对海外先进制程和高端芯片的依赖。</strong>
</p>

<div class="grid grid-cols-1 md:grid-cols-2 gap-4 mb-6">
    <div class="bg-white/5 backdrop-blur rounded-xl p-5 border border-red-500/30">
        <div class="flex items-center gap-3 mb-4">
            <div class="w-12 h-12 bg-gradient-to-br from-red-500 to-orange-600 rounded-xl flex items-center justify-center text-2xl">
                🇨🇳
            </div>
            <div>
                <h4 class="font-bold text-lg text-red-300">华为昇腾路线</h4>
                <p class="text-xs text-gray-400">系统级整合 · 架构换道 · 全栈自研</p>
            </div>
        </div>
        <div class="space-y-2 text-sm text-gray-300">
            <p><strong>✅ 优势：</strong></p>
            <ul class="list-disc pl-5 space-y-1">
                <li>系统级设计能力强，从芯片到封装到软件全栈自研</li>
                <li>定制化路线（W2W混合键合+4096bit位宽）绕开EUV瓶颈</li>
                <li>客户基础深厚，政企/运营商市场绝对主导</li>
                <li>资金实力雄厚，研发投入可持续</li>
                <li>已有量产产品（昇腾950系列），不是纯PPT</li>
            </ul>
            <p class="mt-3"><strong>⚠️ 挑战：</strong></p>
            <ul class="list-disc pl-5 space-y-1">
                <li>DRAM颗粒仍需外购，长鑫良率是瓶颈</li>
                <li>通用GPU生态不如英伟达CUDA完善</li>
                <li>先进封装产能扩张速度可能跟不上需求</li>
            </ul>
        </div>
    </div>
    
    <div class="bg-white/5 backdrop-blur rounded-xl p-5 border border-blue-500/30">
        <div class="flex items-center gap-3 mb-4">
            <div class="w-12 h-12 bg-gradient-to-br from-blue-500 to-indigo-600 rounded-xl flex items-center justify-center text-2xl">
                ⚡
            </div>
            <div>
                <h4 class="font-bold text-lg text-blue-300">壁仞科技路线</h4>
                <p class="text-xs text-gray-400">通用GPU · Chiplet架构 · 国产供应链</p>
            </div>
        </div>
        <div class="space-y-2 text-sm text-gray-300">
            <p><strong>✅ 优势：</strong></p>
            <ul class="list-disc pl-5 space-y-1">
                <li>通用GPU路线，软件生态与CUDA兼容度高</li>
                <li>BR20X性能对标H200，进入第一梯队</li>
                <li>BIS清单后全面国产替代，供应链安全验证通过</li>
                <li>上半年营收+1997.6%，商业化加速明显</li>
                <li>Chiplet架构+NPO光互连，技术路线先进</li>
            </ul>
            <p class="mt-3"><strong>⚠️ 挑战：</strong></p>
            <ul class="list-disc pl-5 space-y-1">
                <li>制程依赖国内DUV，良率和成本压力大</li>
                <li>从送测到量产到订单确认，仍需时间</li>
                <li>国产GPU竞争加剧（寒武纪/沐曦/摩尔线程等）</li>
                <li>尚未盈利，持续高研发投入压力大</li>
            </ul>
        </div>
    </div>
</div>

<h4 class="font-bold text-lg mb-3 text-amber-300">🔗 产业链共振：两者的最大公约数是什么？</h4>
<p class="mb-3 text-gray-200 leading-relaxed">
华为和壁仞虽然技术路线不同，但有一个<strong>最重要的共同点：都需要高端先进封装产能，都依赖国产HBM供应链。</strong>
这就是为什么今天先进封装和HBM材料板块涨幅最大——它们是双雄的共同受益环节。
</p>

<div class="bg-white/5 backdrop-blur rounded-xl p-4 border border-amber-500/30">
    <h5 class="font-bold text-amber-300 mb-3">💰 产业链价值重估逻辑</h5>
    <div class="space-y-2 text-sm text-gray-300">
        <p><strong>① 先进封装：确定性最高的环节</strong></p>
        <p class="pl-4">无论是华为昇腾的HBM+混合键合，还是壁仞BR20X的Chiplet架构，
        都离不开高端先进封装。国内封测龙头<strong>长电科技</strong>是双方的共同供应商（华为合作已确认，壁仞合作概率高）。
        先进封装已从「后道工序」升级为「性能决定因素」，量价齐升逻辑最硬。</p>
        
        <p class="mt-3"><strong>② HBM材料：弹性最大的环节</strong></p>
        <p class="pl-4">HBM是AI芯片的「精饲料」，国产GPU性能越接近海外，对HBM的需求越旺盛。
        <strong>雅克科技</strong>（前驱体）、<strong>华海诚科</strong>（塑封料）、
        <strong>兴发集团</strong>（高纯次磷酸钠）、<strong>联瑞新材</strong>（Low-α硅微粉）
        是材料环节的核心标的。华为W2W混合键合路线反而增加了化学镀耗材需求，这是一个容易被忽视的增量。</p>
        
        <p class="mt-3"><strong>③ 国产GPU：弹性最大但分化最剧烈</strong></p>
        <p class="pl-4">壁仞BR20X送测+H200性能确认，会提升市场对国产GPU整体的预期。
        但分化会很严重——有量产能力、有客户验证、供应链安全的头部公司（寒武纪、壁仞、沐曦）会持续受益，
        而二线公司可能面临流片延期、量产困难等风险。</p>
    </div>
</div>
"""
gen.add_analysis_section("⚔️ 双雄对比与产业链共振", duel_analysis, icon="chip")

# ===== 4. 双催化产业链受益排序 =====
headers = ["受益层级", "代表标的", "代码", "华为HBM受益度", "壁仞BR20X受益度", "综合弹性", "核心逻辑"]
rows = [
    ["S级（封测）", "长电科技", "600584", "★★★★★", "★★★★☆", "S级",
     "国内封测龙头，双方共同供应商，先进封装量价齐升最确定"],
    ["S级（材料）", "雅克科技", "002409", "★★★★☆", "★★★★", "S级",
     "HBM前驱体全球核心供应商，华为+壁仞+HBM扩产三重受益"],
    ["S级（材料）", "兴发集团", "600141", "★★★★☆", "★★★☆", "A级",
     "存储级高纯次磷酸钠全球最大产能，W2W混合键合ENEPIG需求上升"],
    ["A级（材料）", "华海诚科", "688535", "★★★★", "★★★★", "A级",
     "国内唯一HBM专用GMC塑封料量产，国产GPU全面受益"],
    ["A级（设备）", "快克智能", "603203", "★★★★", "★★★☆", "A级",
     "TCB键合机已通过华为昇腾量产验证，壁仞Chiplet同样需要"],
    ["A级（材料）", "联瑞新材", "688300", "★★★☆", "★★★☆", "B级",
     "Low-α硅微粉全球仅三家量产，HBM+Chiplet双轮驱动"],
    ["B级（GPU）", "寒武纪", "688256", "★★☆", "★★★★★", "A级",
     "国产AI芯片龙头，壁仞送测提振板块情绪，但自身估值已高"],
    ["B级（测试）", "精智达", "688627", "★★★", "★★★", "B级",
     "HBM测试设备，深度绑定长鑫，国产GPU放量带动测试需求"],
    ["B级（封测）", "通富微电", "002156", "★★★", "★★★", "B级",
     "5nm Chiplet已量产，受益于先进封装整体景气度上行"],
    ["B级（分销）", "香农芯创", "300475", "★★", "★★★☆", "B级",
     "SK海力士授权代理商，国产HBM替代前仍有通道价值"],
]

table = CompareTable(headers=headers, rows=rows, highlight_rows=[0, 1, 2])
gen.report.add(Section("🏆 双催化产业链受益排序TOP10", table))

# ===== 5. 持仓股影响 =====
holding_analysis = """
<h3 class="text-xl font-bold mb-4 text-white">持仓股双催化影响深度分析</h3>

<div class="space-y-4">
    <div class="bg-white/5 backdrop-blur rounded-xl p-4 border border-green-500/30">
        <div class="flex justify-between items-center mb-2">
            <h4 class="font-bold text-green-300">✅ 长电科技（600584）：双催化最核心标的</h4>
            <span class="px-3 py-1 rounded-full bg-green-500/20 text-green-300 text-sm font-bold">S级双受益</span>
        </div>
        <p class="text-sm text-gray-300 mb-2">
        <strong>华为侧</strong>：昇腾芯片核心封装合作伙伴，XDFOI平台适配华为HBM封装需求。
        华为HBM量产规模扩大直接拉动长电先进封装业务量。
        </p>
        <p class="text-sm text-gray-300 mb-2">
        <strong>壁仞侧</strong>：壁仞BR100/BR166的封装供应商（行业普遍认知），
        BR20X Chiplet架构需要更高端的先进封装能力，长电是最可能的国内合作伙伴。
        壁仞科技COO张凌岚在2026半导体封测大会上明确提到"封装可行性前移到架构规划阶段"，
        说明封测厂与设计公司的协同非常紧密。
        </p>
        <p class="text-sm text-amber-300">
        📈 当前价47.19元。操作建议：45元以下加仓1/4，42元以下再加1/4，跌破40元止损；
        反弹49元以上减1/4。今天午盘已涨1.19%，关注下午能否放量突破50元整数关。
        </p>
    </div>
    
    <div class="bg-white/5 backdrop-blur rounded-xl p-4 border border-purple-500/30">
        <div class="flex justify-between items-center mb-2">
            <h4 class="font-bold text-purple-300">✅ 雅克科技（002409）：HBM材料最硬卡位</h4>
            <span class="px-3 py-1 rounded-full bg-purple-500/20 text-purple-300 text-sm font-bold">S级双受益</span>
        </div>
        <p class="text-sm text-gray-300 mb-2">
        <strong>华为侧</strong>：DRAM制造端前驱体需求与常规HBM一致，
        雅克UP Chemical是SK海力士HBM4前驱体核心供应商，技术能力同样适配华为需求。
        市场传闻正在联合华为开发HBM级前驱体。
        </p>
        <p class="text-sm text-gray-300 mb-2">
        <strong>壁仞侧</strong>：壁仞BR20X同样需要HBM（或同类高带宽内存），
        只要国产GPU性能上去，对HBM的需求就会持续增长。雅克作为HBM前驱体龙头，
        是国产GPU整体放量的上游受益者。
        </p>
        <p class="text-sm text-amber-300">
        📈 当前价71.68元（昨日跌停）。操作建议：70元以下轻仓1/5，65元以下加1/5，跌破60元止损；
        反弹75元以上减1/3，80元以上再减1/3。今日午盘已涨2.46%，反弹减仓纪律不变。
        </p>
    </div>
    
    <div class="bg-white/5 backdrop-blur rounded-xl p-4 border border-blue-500/30">
        <div class="flex justify-between items-center mb-2">
            <h4 class="font-bold text-blue-300">✅ 华海诚科（688535）：塑封料环节弹性标的</h4>
            <span class="px-3 py-1 rounded-full bg-blue-500/20 text-blue-300 text-sm font-bold">A级双受益</span>
        </div>
        <p class="text-sm text-gray-300 mb-2">
        <strong>华为侧</strong>：HBM封装需要高端GMC塑封料，华海诚科是国内唯一量产品种，
        已通过部分客户认证。华为HBM量产增加对高端塑封料的需求。
        </p>
        <p class="text-sm text-gray-300 mb-2">
        <strong>壁仞侧</strong>：BR20X的Chiplet封装同样需要高端塑封料，
        且AI芯片封装尺寸越大、堆叠越多，对塑封料的导热性和低应力要求越高，
        华海诚科韩国子公司的高导热EMC技术可以适配。
        </p>
        <p class="text-sm text-amber-300">
        📈 当前价61.00元（昨日跌停-10.43%）。操作建议：60元以下轻仓1/5，
        55元以下加1/5，跌破50元止损；反弹65元以上减1/3。今日午盘涨6.56%领涨持仓，
        关注能否延续反弹至70元以上。
        </p>
    </div>
    
    <div class="bg-white/5 backdrop-blur rounded-xl p-4 border border-gray-500/30">
        <div class="flex justify-between items-center mb-2">
            <h4 class="font-bold text-gray-300">➖ 风华高科、铜冠铜箔、英维克、*ST建艺</h4>
            <span class="px-3 py-1 rounded-full bg-gray-500/20 text-gray-300 text-sm font-bold">弱受益/无关</span>
        </div>
        <p class="text-sm text-gray-300">
        <strong>风华高科</strong>：MLCC与HBM/先进封装无直接关联，AI算力扩张是间接利好。
        Q3净利+470%业绩拐点明确，优先加仓逻辑不变，今日午盘+1.74%。
        </p>
        <p class="text-sm text-gray-300 mt-2">
        <strong>铜冠铜箔</strong>：PCB铜箔与HBM无直接关系，AI服务器PCB用铜箔有间接利好，
        今日午盘+2.23%，主要受PCB板块（全球紧缺警报）带动。
        </p>
        <p class="text-sm text-gray-300 mt-2">
        <strong>英维克</strong>：液冷散热，AI算力扩张间接受益，但逻辑链条较长，
        今日午盘+0.10%，表现最弱。
        </p>
        <p class="text-sm text-gray-300 mt-2">
        <strong>*ST建艺</strong>：完全无关，今日+3.30%属个股自身行情。
        </p>
    </div>
</div>
"""
gen.add_analysis_section("📊 持仓股双催化影响分析", holding_analysis, icon="chart")

# ===== 6. 竞争格局对比 =====
gpu_headers = ["公司", "代表产品", "性能对标", "制程工艺", "封装方案", "量产状态", "优势", "劣势"]
gpu_rows = [
    ["华为海思", "昇腾950系列", "H100/H200级", "国产DUV N+2", "自研W2W混合键合HBM", "已量产",
     "全栈自研+政企市场+资金雄厚", "DRAM外购+通用生态弱"],
    ["壁仞科技", "BR20X", "H200级", "国产工艺", "Chiplet+先进封装", "送测中/2027量产",
     "通用GPU路线+CUDA兼容+供应链已替代", "未盈利+竞争激烈+良率待验证"],
    ["寒武纪", "思元590/690", "H100级", "国产工艺", "Chiplet+CoWoS级", "已量产",
     "A股AI芯片龙头+估值最高+政企客户", "亏损持续+客户集中+估值偏高"],
    ["沐曦股份", "曦云C600", "A100级", "全国产工艺", "先进封装", "已量产出货",
     "全国产供应链闭环+联通等运营商客户", "性能落后一代+市值高"],
    ["摩尔线程", "MTT S80等", "消费级为主", "国产工艺", "常规封装", "已量产",
     "消费级GPU布局广+图形渲染能力", "AI算力弱+转型中"],
]
gen.add_competitive_analysis(headers=gpu_headers, rows=gpu_rows, highlight_rows=[0, 1])

# ===== 7. 催化时间线 =====
gen.add_timeline([
    {"date": "2026年11月16日", "title": "BIS发布远程算力管制新规，14nm及以下代工须审批", "type": "danger"},
    {"date": "2026年11月23日", "title": "IEEE公布ISSCC 2027议程，华为4篇3D集成论文入选", "type": "info"},
    {"date": "2026年11月25日", "title": "壁仞科技回应：BR20X性能达H200水平、已向头部客户送测", "type": "success"},
    {"date": "2026年11月25日", "title": "壁仞确认：BIS清单后未采购受管制物项，已全面国产替代", "type": "success"},
    {"date": "2026年11月26日", "title": "华为HBM细节披露：五层W2W混合键合+4096bit位宽+内存控制器集成", "type": "warning"},
    {"date": "2027年2月16日", "title": "ISSCC 2027华为正式发表论文，披露完整技术细节", "type": "warning"},
    {"date": "2027年Q1", "title": "壁仞BR20X预计量产验证；昇腾960预计送样", "type": "warning"},
    {"date": "2027年Q2-Q3", "title": "壁仞BR20X预计规模化部署，全年出货有望达7万颗（星展预测）", "type": "danger"},
    {"date": "2027年下半年", "title": "长鑫HBM3E产能爬坡至月产5万片，国产HBM供需缓解", "type": "info"},
], title="📅 双催化时间线与操作节奏")

# ===== 8. 风险提示 =====
gen.add_risk_section([
    "**量产进度不及预期**：壁仞BR20X从送测到规模量产仍有不确定性，华为HBM良率爬坡也需要时间",
    "**BIS管制升级风险**：虽然壁仞称已完成替代，但管制可能进一步收紧到更上游的设备/材料",
    "**国产GPU竞争加剧**：寒武纪/壁仞/沐曦/摩尔线程/燧原多家竞争，价格战可能压缩利润",
    "**技术迭代风险**：英伟达Rubin+HBM4E已在路上，国产追赶速度能否跟上海外存疑",
    "**估值回调风险**：国产GPU板块从高点回撤45-85%，风险偏好下行阶段估值可能继续承压",
    "**全球AI资本开支分化**：近期算力供给过剩讨论升温，可能影响板块整体估值",
    "**信息来源风险**：部分信息来自渠道调研和公司回应，具体指标以官方公告和财报为准",
])

# ===== 9. 投资结论 =====
gen.add_conclusion(
    conclusion=(
        "华为HBM突破+壁仞BR20X送测，两大催化同日发酵，标志着国产算力自主可控进入「性能验证期」。"
        "最确定的受益环节是先进封装（量价齐升逻辑最硬），弹性最大的是HBM材料（前驱体/塑封料），"
        "国产GPU本身则分化加剧——头部强者恒强，尾部面临淘汰。\n\n"
        "操作策略：①核心持仓（长电科技、雅克科技、华海诚科）利用本轮情绪修复"
        "按纪律做T，底仓持有+反弹减机动仓，不追高；"
        "②风华高科优先加仓逻辑不变（业绩确定性最强），趁科技反弹时调仓优化结构；"
        "③总仓位控制在5-6成，保留现金应对美联储加息和全球AI估值回调的宏观风险；"
        "④真正的趋势性买点要看2027年Q2-Q3壁仞BR20X和昇腾960的量产验证，"
        "在此之前以波段操作为主，不做长期单边all in。"
    ),
    rating="推荐"
)

# 保存并发布
result = gen.publish(
    title="国产算力双雄：华为HBM×壁仞BR20X产业链共振深度分析",
    report_type="industry_chain",
    filename="20261126_国产算力双雄_华为HBMx壁仞BR20X产业链共振深度分析.html",
    excerpt="双催化同日发酵：华为HBM五层W2W混合键合+4096bit位宽，壁仞BR20X性能达H200水平且已送测。先进封装/HBM材料/国产GPU全链条受益排序，7只持仓股逐只诊断与操作策略。",
    auto_deploy=True
)

print("发布结果：", result)
