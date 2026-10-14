import sys, os
sys.path.insert(0, '/root/daily-news-insight/v3')
os.chdir('/root/daily-news-insight')

from v3.generators.s_level_catalyst import SLevelCatalystGenerator

gen = SLevelCatalystGenerator(
    date_str="20261015",
    catalyst_title="全球存储芯片暴跌·CPI超预期加息升温",
    subtitle="2026.10.15 · 盘前S级催化"
)

# === 催化概述 ===
gen.add_catalyst_overview(
    overview="""
    <strong>三重利空共振：</strong>隔夜美股纳指大跌1.88%，费城半导体指数暴跌4.3%创去年5月以来最长六连跌纪录。核心驱动：①美国9月CPI同比3.7%超预期，12月加息概率飙升至68.7%；②长鑫科技4F² DRAM架构突破引发全球存储定价权重估，三星跌超7%、SK海力士跌超10%、美光跌超4%；③博通CEO警示AI资本制约。<br><br>
    <strong>结构性亮点：</strong>阿斯麦Q3净利润暴增133%，订单已排至2030年，2028年产能需超30%扩产才能满足需求，验证AI半导体设备长周期景气。国内存储国产替代逻辑进一步强化。
    """,
    importance="极高"
)

# === 催化详解 ===
gen.add_catalyst_details(
    background="""
    10月10日长鑫科技总裁曹堪宇在第四届集成芯片和芯粒大会上公布4F² DRAM架构关键进展，自研VSG垂直包围沟道晶体管使单胞面积缩减约33%，晶圆位元密度提升30%-50%，预计年底推出DDR5 RDIMM产品。<br><br>
    该技术绕开EUV光刻限制，用DUV多重曝光+架构创新实现战略"换道"，海外巨头原计划2027-2028年才导入该路线。长鑫上半年营收1503亿元同比+874%，全球DRAM份额已升至10%。
    """,
    trigger="""
    ① <strong>CPI超预期：</strong>美国9月CPI同比3.7%（预期3.6%），核心CPI同比2.6%（预期2.5%），美联储12月加息概率升至68.7%<br>
    ② <strong>长鑫4F²冲击波：</strong>三星跌7.4%、SK海力士暴跌10.1%，韩国股市触发熔断暂停程序化卖盘，外资年内已抛售韩股近万亿人民币<br>
    ③ <strong>AI资本约束：</strong>博通CEO称"很多投资者不知道自己投的是什么"，英特尔CEO称存储可能最先降温<br>
    ④ <strong>三星回购终止：</strong>三星约200亿美元回购10月6日提前终止，托底力量消失<br>
    ⑤ <strong>安徽省委书记调研长鑫：</strong>10月14日李乐成赴长鑫调研，要求全链条关键核心技术攻关，国产替代政策面持续加码
    """
)

# === 隔夜外盘扫描模块（强制要求）===
from components.layout import Section, SubCard
from components.data import DataGrid, StockTags, CompareTable

overnight_data = [
    {"label": "费城半导体(SOX)", "value": "-4.30%", "sub": "六连跌，创2025年5月以来最长纪录", "variant": "danger"},
    {"label": "纳斯达克", "value": "-1.88%", "sub": "AI股全面承压", "variant": "danger"},
    {"label": "英伟达 NVDA", "value": "-3.16%", "sub": "报$221.30，市值5.33万亿", "variant": "danger"},
    {"label": "AMD", "value": "-5.42%", "sub": "报$572.73", "variant": "danger"},
    {"label": "美光科技 MU", "value": "-4.00%+", "sub": "盘后再跌2.5%，距高点回撤20%+", "variant": "danger"},
    {"label": "SK海力士", "value": "-6%+", "sub": "Nextrade盘前续跌，两日累跌16%+", "variant": "danger"},
    {"label": "阿斯麦 ASML", "value": "Q3业绩超预期", "sub": "净利+133%，订单排到2030年", "variant": "success"},
    {"label": "美国10月CPI", "value": "3.7%", "sub": "超预期0.1个百分点，12月加息概率68.7%", "variant": "danger"},
]

datagrid = DataGrid(cards=overnight_data, cols=4)
section = Section(title="🌍 隔夜全球市场扫描（强制核查）", content=datagrid.render(), icon="globe", variant="highlight")
gen._components.append(section)

# === 产业链梳理 ===
upstream = [
    {
        "name": "半导体设备（国产替代加速）",
        "desc": "ASML产能紧张+出口管制双重驱动，国产设备验证窗口扩大。超高深宽比刻蚀、ALD、混合键合、CMP设备需求明确。2026-2027年中国大陆晶圆厂设备销售额预计4414/4736亿元。",
        "stocks": [
            {"code": "688012", "name": "中微公司", "impact": "核心受益"},
            {"code": "002371", "name": "北方华创", "impact": "核心受益"},
            {"code": "688072", "name": "拓荆科技", "impact": "薄膜沉积"},
            {"code": "688200", "name": "华峰测控", "impact": "测试设备"},
            {"code": "688120", "name": "华海清科", "impact": "CMP设备"},
        ]
    },
    {
        "name": "半导体材料",
        "desc": "长鑫扩产+国产替代双驱动，光刻胶、CMP抛光液、电子特气、前驱体等材料需求持续增长。",
        "stocks": [
            {"code": "300655", "name": "晶瑞电材", "impact": "光刻胶"},
            {"code": "688538", "name": "安集科技", "impact": "CMP抛光液"},
            {"code": "688268", "name": "华特气体", "impact": "电子特气"},
        ]
    },
]

midstream = [
    {
        "name": "存储芯片（国产替代主线）",
        "desc": "长鑫4F²突破证明国产存储技术追赶加速，自主可控逻辑强化。短期情绪承压但基本面未变：DRAM供需缺口至少延续至2028年，美光已签26份长期供货协议覆盖2030年35%以上收入。",
        "stocks": [
            {"code": "688825", "name": "长鑫科技", "impact": "技术突破主体"},
            {"code": "603986", "name": "兆易创新", "impact": "NOR Flash+DRAM"},
            {"code": "300346", "name": "南大光电", "impact": "MO源+光刻胶"},
        ]
    },
    {
        "name": "先进封装/HBM产业链",
        "desc": "长鑫突破集中在通用DRAM领域，不直接冲击HBM。HBM供给仍紧张，SK海力士HBM4扩产节奏推迟反而验证供需紧平衡。先进封装设备与材料持续受益。",
        "stocks": [
            {"code": "002409", "name": "雅克科技", "impact": "前驱体+HBM材料"},
            {"code": "600584", "name": "长电科技", "impact": "封测龙头"},
            {"code": "002185", "name": "华天科技", "impact": "封测"},
        ]
    },
    {
        "name": "液冷散热（AI算力基础设施）",
        "desc": "阿斯麦订单排至2030年验证AI算力长周期景气，液冷作为算力基础设施刚需逻辑不变。短期受板块情绪影响，但产业趋势坚实。",
        "stocks": [
            {"code": "002837", "name": "英维克", "impact": "液冷龙头"},
            {"code": "300787", "name": "海象新材", "impact": "散热材料"},
        ]
    },
]

downstream = [
    {
        "name": "AI算力/服务器",
        "desc": "短期受加息预期和AI资本约束言论压制。但微软新增1300亿美金数据中心租约、Anthropic Q3营收168亿美元盈利，基本面依然强劲。",
        "stocks": [
            {"code": "000977", "name": "浪潮信息", "impact": "服务器龙头"},
            {"code": "300496", "name": "中科创达", "impact": "AI解决方案"},
        ]
    },
    {
        "name": "铜箔/PCB（AI硬件链）",
        "desc": "嘉元科技前三季度净利预增1197%-1319%，验证铜箔需求景气。AI服务器PCB供需结构性失衡持续。",
        "stocks": [
            {"code": "301217", "name": "铜冠铜箔", "impact": "电子铜箔"},
            {"code": "688388", "name": "嘉元科技", "impact": "锂电铜箔+电子铜箔"},
            {"code": "002463", "name": "沪电股份", "impact": "PCB龙头"},
        ]
    },
]

gen.add_industry_chain_analysis(upstream=upstream, midstream=midstream, downstream=downstream)

# === 催化深度分析（3个事件）===
gen.add_catalyst_deep_analysis([
    {
        "title": "长鑫4F²架构突破·全球存储定价权重估",
        "type": "policy",
        "description": "国产DRAM技术突破引发全球存储芯片集体暴跌，自主可控逻辑强化",
        "category": "半导体/存储"
    },
    {
        "title": "美国CPI超预期·美联储加息升温",
        "type": "data",
        "description": "9月CPI同比3.7%超预期，12月加息概率升至68.7%，全球风险资产承压",
        "category": "宏观/流动性"
    },
    {
        "title": "阿斯麦订单排至2030年·AI设备长周期景气",
        "type": "earnings",
        "description": "ASML Q3净利+133%超预期，2028年产能需超30%扩产，验证AI半导体设备长景气",
        "category": "半导体设备"
    },
])

# === 投资机会 ===
gen.add_investment_opportunities([
    {
        "name": "半导体设备国产替代（高优先级）",
        "priority": "高",
        "logic": "ASML产能紧张+出口管制双重约束，国产设备验证窗口空前扩大。长鑫241亿研发+108亿测试基地扩产，设备采购需求明确。建议关注刻蚀、薄膜沉积、CMP、量检测等环节龙头。",
        "stocks": [
            {"code": "688012", "name": "中微公司", "impact": "刻蚀龙头"},
            {"code": "002371", "name": "北方华创", "impact": "设备平台"},
            {"code": "688072", "name": "拓荆科技", "impact": "薄膜沉积"},
        ]
    },
    {
        "name": "存储芯片国产替代（高优先级）",
        "priority": "高",
        "logic": "长鑫4F²突破验证国产技术追赶能力，自主可控逻辑进一步强化。短期情绪超调后，具备技术壁垒和业绩支撑的标的有望率先修复。DRAM供需缺口至少延续至2028年，行业基本面未变。",
        "stocks": [
            {"code": "603986", "name": "兆易创新", "impact": "存储设计龙头"},
            {"code": "688525", "name": "佰维存储", "impact": "存储模组"},
        ]
    },
    {
        "name": "先进封装/HBM材料（中优先级）",
        "priority": "中",
        "logic": "长鑫突破集中在通用DRAM，HBM赛道不受直接冲击。SK海力士HBM4扩产推迟反而验证供给紧张。HBM作为AI算力核心瓶颈，长期景气确定。关注前驱体、封装材料环节。",
        "stocks": [
            {"code": "002409", "name": "雅克科技", "impact": "前驱体+HBM材料"},
            {"code": "688538", "name": "安集科技", "impact": "CMP抛光液"},
        ]
    },
    {
        "name": "AI液冷散热（中优先级）",
        "priority": "中",
        "logic": "短期受板块情绪拖累，但AI算力长周期逻辑由ASML订单再次验证。液冷作为高算力密度刚需，产业趋势确定。英维克期权激励落地，管理层利益绑定。",
        "stocks": [
            {"code": "002837", "name": "英维克", "impact": "液冷龙头"},
            {"code": "603169", "name": "兰石重装", "impact": "液冷设备"},
        ]
    },
], view_mode="tab")

# === 持仓个股影响分析 ===
holdings_analysis = """
<div style="display: flex; flex-direction: column; gap: 12px;">
    <div style="background: rgba(255,255,255,0.04); border-radius: 12px; padding: 16px; border: 1px solid rgba(251,191,36,0.25);">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 8px;">
            <span style="font-size: 15px; font-weight: 700; color: #f1f5f9;">英维克（002837）</span>
            <span style="padding: 3px 10px; border-radius: 15px; font-size: 11px; font-weight: 600; background: rgba(251,191,36,0.15); color: #fbbf24;">注意风险 · 持有观察</span>
        </div>
        <div style="font-size: 13px; color: #94a3b8; line-height: 1.7;">
            <strong>影响判断：</strong>短期受科技板块整体回调压力，液冷逻辑未变。<br>
            <strong>关键催化：</strong>①股票期权激励完成登记（行权价46.73元，2200万份，765人），管理层利益绑定；②阿斯麦订单验证AI算力长周期，液冷需求刚性。<br>
            <strong>操作建议：</strong>底仓持有不动，若回调至45-46元附近（行权价附近）可考虑加仓机动仓。单一信号（板块回调）不构成减仓理由，产业趋势+公司业绩双验证。
        </div>
    </div>
    <div style="background: rgba(255,255,255,0.04); border-radius: 12px; padding: 16px; border: 1px solid rgba(239,68,68,0.25);">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 8px;">
            <span style="font-size: 15px; font-weight: 700; color: #f1f5f9;">雅克科技（002409）</span>
            <span style="padding: 3px 10px; border-radius: 15px; font-size: 11px; font-weight: 600; background: rgba(239,68,68,0.15); color: #f87171;">谨慎 · 反弹减仓机动仓</span>
        </div>
        <div style="font-size: 13px; color: #94a3b8; line-height: 1.7;">
            <strong>影响判断：</strong>存储板块情绪冲击+半导体整体回调双重压力。但HBM材料逻辑不受长鑫通用DRAM突破影响，SK海力士HBM4扩产推迟反而验证供给紧张。<br>
            <strong>估值锚：</strong>当前股价对应2026年PE约35-40倍，前驱体+HBM材料双轮驱动业绩增速约50%+，PEG＜1，估值基本合理。<br>
            <strong>操作建议：</strong>底仓30%持有，反弹时减仓机动仓。<span style="color: #f87171;">不触发铁律级减仓（单一信号：板块情绪回调，非产业逻辑破坏）</span>，若跌破关键支撑再评估。
        </div>
    </div>
    <div style="background: rgba(255,255,255,0.04); border-radius: 12px; padding: 16px; border: 1px solid rgba(16,185,129,0.25);">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 8px;">
            <span style="font-size: 15px; font-weight: 700; color: #f1f5f9;">铜冠铜箔（301217）</span>
            <span style="padding: 3px 10px; border-radius: 15px; font-size: 11px; font-weight: 600; background: rgba(16,185,129,0.15); color: #34d399;">相对抗跌 · 持有</span>
        </div>
        <div style="font-size: 13px; color: #94a3b8; line-height: 1.7;">
            <strong>影响判断：</strong>铜箔板块受益于AI服务器PCB需求，嘉元科技Q3净利预增12倍验证行业景气。相比存储芯片，铜箔受长鑫事件直接冲击小。<br>
            <strong>催化：</strong>嘉元科技前三季度净利5.3-5.8亿同比+1197%~1319%，铜箔行业量价齐升逻辑验证。<br>
            <strong>操作建议：</strong>继续持有，若板块错杀带来低吸机会可考虑加仓。
        </div>
    </div>
    <div style="background: rgba(255,255,255,0.04); border-radius: 12px; padding: 16px; border: 1px solid rgba(148,163,184,0.25);">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 8px;">
            <span style="font-size: 15px; font-weight: 700; color: #f1f5f9;">*ST建艺（002789）</span>
            <span style="padding: 3px 10px; border-radius: 15px; font-size: 11px; font-weight: 600; background: rgba(148,163,184,0.15); color: #94a3b8;">无直接影响</span>
        </div>
        <div style="font-size: 13px; color: #94a3b8; line-height: 1.7;">
            <strong>影响判断：</strong>建筑装饰行业，与科技板块关联度低，无直接影响。
        </div>
    </div>
</div>
"""
section2 = Section(title="📊 持仓个股影响评估（双重验证）", content=holdings_analysis, icon="briefcase", variant="highlight")
gen._components.append(section2)

# === 投资策略 ===
gen.add_investment_strategy("""
<strong>一、总体判断：短期情绪冲击，不改中期产业趋势</strong><br>
本轮全球科技股回调由三重因素共振引发：CPI超预期（流动性）+ 长鑫技术突破（产业格局）+ 博通CEO言论（情绪面）。核心基本面未变——AI算力需求仍在增长，阿斯麦订单排至2030年就是最强验证。<br><br>

<strong>二、操作策略：</strong><br>
1. <strong>总体仓位：</strong>科技仓位维持中性，不盲目抄底也不恐慌割肉，等待市场消化CPI数据后再评估<br>
2. <strong>结构调整：</strong>从纯情绪驱动的存储标的，向<strong>业绩确定性强的半导体设备、铜箔、液冷</strong>倾斜<br>
3. <strong>左侧建仓条件：</strong>若科创50继续回调5%+，可考虑分批加仓半导体设备龙头（中微/北方华创），左侧仓位≤30%<br>
4. <strong>右侧确认信号：</strong>费城半导体指数止跌企稳 + 存储现货价未出现实质性下跌<br><br>

<strong>三、重点关注的两个验证节点：</strong><br>
• 台积电10月15日法说会：验证先进制程/封装需求强度<br>
• 英伟达中国开发者日（10月15-16日，苏州）：关注国内AI生态最新进展
""")

# === 风险提示 ===
gen.add_risk_warning([
    "美联储加息超预期导致全球流动性收紧，科技股估值承压",
    "长鑫技术突破进度快于预期，存储价格战提前到来",
    "AI资本开支不及预期，半导体设备需求下修",
    "地缘政治风险加剧，出口管制进一步升级",
    "持仓个股减仓建议严格遵守双重验证规则，单一信号不触发铁律级减仓"
])

# === 发布 ===
result = gen.publish(
    title="S级催化：全球存储芯片暴跌·CPI超预期加息升温",
    report_type="s_level_catalyst",
    excerpt="隔夜美股纳指跌1.88%，费城半导体指数暴跌4.3%六连跌。长鑫4F²架构突破引发全球存储芯片重估，三星跌7%、SK海力士跌10%。阿斯麦Q3净利+133%，订单排至2030年。",
    auto_deploy=True,
    docs_root="docs"
)

print("=== 发布结果 ===")
for k, v in result.items():
    if k != 'html_content':
        print(f"{k}: {v}")

# 验证
issues = gen.validate()
print(f"\n=== 质量验证 ===")
if issues:
    for issue in issues:
        print(f"  ⚠️  {issue}")
else:
    print("  ✅ 全部通过")
