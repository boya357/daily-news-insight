"""
S级催化盘前生成 - 20260826
核心催化：发改委"六网协同"万亿算力网基建落地 + 美股半导体全线反弹 + 液冷板块业绩拐点
"""
import sys, os
sys.path.insert(0, 'v3')
os.chdir('/root/daily-news-insight')

from v3.generators.s_level_catalyst import SLevelCatalystGenerator
from components.layout import Section, HighlightBox, SubCard, CardGrid, SplitLayout, Card
from components.data import DataCard, DataGrid, KeyPoints, StockTags, CompareTable, Badge, StatCard, Sparkline, Tabs, GaugeChart, ProgressBar
from components.special import RiskAlert, QuoteBlock
from components.icons import icon_svg

gen = SLevelCatalystGenerator(
    date_str="20260826",
    catalyst_title="六网协同万亿算力网基建落地",
    subtitle="2026.08.26 · 盘前S级催化"
)

# ===== 1. 催化概述 =====
gen.add_catalyst_overview(
    overview="""
    <b>【S级催化】发改委"六网协同"协调推进会召开，万亿算力网基建进入实操阶段</b><br><br>
    8月25日，发改委副主任岳修虎主持召开"六网协同"协调推进工作会，专题研究算力网、新型电网、新一代通信网等六张网建设的投融资机制完善。十部门联合参会（含证监会、央行、财政部），标志着"六张网"从规划阶段进入实质性落地期。<br><br>
    据测算，"六张网"年度投资规模超7万亿元，十五五周期累计接近26万亿元。算力网作为新增战略性基础设施，与新型电网、通信网形成"2+3+N"协同机制，直接利好液冷散热、算力设备、光通信、电力设备等产业链。<br><br>
    隔夜美股半导体板块集体反弹（费半+1.44%、英伟达+2.19%终结七连跌、AMD+4.91%），叠加马斯克宣布SpaceX AI卫星搭载英伟达芯片，科技股风险偏好显著修复。
    """,
    importance="S级"
)

# ===== 2. 隔夜外盘扫描 =====
overnight_left = """
<div style="background: linear-gradient(135deg, rgba(59,130,246,0.12) 0%, rgba(37,99,235,0.08) 100%); 
            border-radius: 14px; padding: 20px; height: 100%;
            border: 1px solid rgba(96,165,250,0.25);">
    <div style="display: flex; align-items: center; margin-bottom: 16px;">
        <div style="width: 36px; height: 36px; 
                   background: linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%); 
                   border-radius: 10px; display: flex; align-items: center; justify-content: center; 
                   margin-right: 12px;">
            🇺🇸
        </div>
        <span style="font-size: 16px; font-weight: 700; color: #60a5fa;">
            美股科技股集体反弹
        </span>
    </div>
    <div style="font-size: 13px; color: #cbd5e1; line-height: 2;">
        <div style="display: flex; justify-content: space-between; border-bottom: 1px solid rgba(255,255,255,0.06); padding: 4px 0;">
            <span>道琼斯工业指数</span><span style="color: #22c55e;">+0.30%</span>
        </div>
        <div style="display: flex; justify-content: space-between; border-bottom: 1px solid rgba(255,255,255,0.06); padding: 4px 0;">
            <span>纳斯达克综合指数</span><span style="color: #22c55e;">+0.66%</span>
        </div>
        <div style="display: flex; justify-content: space-between; border-bottom: 1px solid rgba(255,255,255,0.06); padding: 4px 0;">
            <span>标普500指数</span><span style="color: #22c55e;">+0.32%</span>
        </div>
        <div style="display: flex; justify-content: space-between; border-bottom: 1px solid rgba(255,255,255,0.06); padding: 4px 0;">
            <span style="font-weight: 600; color: #fbbf24;">费城半导体指数(SOX)</span>
            <span style="font-weight: 600; color: #22c55e;">+1.44%</span>
        </div>
        <div style="display: flex; justify-content: space-between; border-bottom: 1px solid rgba(255,255,255,0.06); padding: 4px 0;">
            <span>英伟达 NVDA</span><span style="color: #22c55e;">+2.19%</span>
        </div>
        <div style="display: flex; justify-content: space-between; border-bottom: 1px solid rgba(255,255,255,0.06); padding: 4px 0;">
            <span>AMD</span><span style="color: #22c55e;">+4.91%</span>
        </div>
        <div style="display: flex; justify-content: space-between; border-bottom: 1px solid rgba(255,255,255,0.06); padding: 4px 0;">
            <span>美光科技 MU</span><span style="color: #22c55e;">+2.48%</span>
        </div>
        <div style="display: flex; justify-content: space-between; border-bottom: 1px solid rgba(255,255,255,0.06); padding: 4px 0;">
            <span>台积电ADR</span><span style="color: #22c55e;">+1.78%</span>
        </div>
        <div style="display: flex; justify-content: space-between; border-bottom: 1px solid rgba(255,255,255,0.06); padding: 4px 0;">
            <span>阿斯麦 ASML</span><span style="color: #22c55e;">+1.49%</span>
        </div>
        <div style="display: flex; justify-content: space-between; border-bottom: 1px solid rgba(255,255,255,0.06); padding: 4px 0;">
            <span>西部数据 WDC</span><span style="color: #22c55e;">+3.53%</span>
        </div>
        <div style="display: flex; justify-content: space-between; padding: 4px 0;">
            <span>迈威尔科技 MRVL</span><span style="color: #22c55e;">+4.84%</span>
        </div>
    </div>
    <div style="margin-top: 14px; padding: 10px 12px; background: rgba(34,197,94,0.1); border-radius: 8px; border: 1px solid rgba(34,197,94,0.2);">
        <div style="font-size: 12px; color: #86efac; line-height: 1.6;">
            ✅ 英伟达终结七连跌，市场等待8/26盘后Q2财报（预期营收920亿，yoy+96%）<br>
            ✅ 马斯克宣布SpaceX AI卫星搭载英伟达Vera Rubin芯片，2027年Q4首射<br>
            ✅ Groq 3 LPX推理芯片全面量产，英伟达AI推理布局加速
        </div>
    </div>
</div>
"""

overnight_right = """
<div style="background: linear-gradient(135deg, rgba(245,158,11,0.12) 0%, rgba(217,119,6,0.08) 100%); 
            border-radius: 14px; padding: 20px; height: 100%;
            border: 1px solid rgba(251,191,36,0.25);">
    <div style="display: flex; align-items: center; margin-bottom: 16px;">
        <div style="width: 36px; height: 36px; 
                   background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%); 
                   border-radius: 10px; display: flex; align-items: center; justify-content: center; 
                   margin-right: 12px;">
            🌏
        </div>
        <span style="font-size: 16px; font-weight: 700; color: #fbbf24;">
            亚洲半导体 & 产业消息
        </span>
    </div>
    <div style="font-size: 13px; color: #fde68a; line-height: 1.8;">
        <div style="margin-bottom: 12px;">
            <b style="color: #fcd34d;">🇰🇷 韩国市场</b><br>
            <span style="font-size: 12px; color: #fbbf24;">• 8/25韩国KOSPI跌2.44%，三星电子跌3.7%，SK海力士跌5.33%（受美股半导体前一日暴跌传导）</span><br>
            <span style="font-size: 12px; color: #fbbf24;">• SK海力士工会以50.08%微弱否决涨薪协议（60%股票形式奖金遭拒），短期增加供应不确定性</span><br>
            <span style="font-size: 12px; color: #fbbf24;">• 三星/SK海力士加码中国NAND产能：西安V9 NAND改造+大连二厂月产3万片</span>
        </div>
        <div style="margin-bottom: 12px;">
            <b style="color: #fcd34d;">🇹🇼 台湾半导体</b><br>
            <span style="font-size: 12px; color: #fbbf24;">• 台积电1.6nm A16工艺完成开发验证，目标Q4量产</span><br>
            <span style="font-size: 12px; color: #fbbf24;">• 台积电7月营收4675.8亿新台币，yoy+44.7%，1-7月累计+37%</span><br>
            <span style="font-size: 12px; color: #fbbf24;">• 供应商日亚化学将在台湾建厂，先进封装产业链本地化加速</span>
        </div>
        <div style="margin-bottom: 12px;">
            <b style="color: #fcd34d;">🏭 存储产业</b><br>
            <span style="font-size: 12px; color: #fbbf24;">• 三星确认HBM4E进展顺利，单针速率16Gbps，单堆栈带宽突破4TB/s</span><br>
            <span style="font-size: 12px; color: #fbbf24;">• TrendForce：存储器占CSP资本支出比重2027年将达68%</span><br>
            <span style="font-size: 12px; color: #fbbf24;">• 长江存储科创板IPO获受理，NAND Q2出货量超越铠侠跻身全球第三</span>
        </div>
        <div>
            <b style="color: #fcd34d;">🇨🇳 国内政策</b><br>
            <span style="font-size: 12px; color: #fbbf24;">• 发改委"六网协同"推进会：算力网+新型电网+通信网协同机制落地</span><br>
            <span style="font-size: 12px; color: #fbbf24;">• 人大常委会：上半年GDP同比增4.7%，增量3.6万亿创5年同期最高</span>
        </div>
    </div>
</div>
"""

split_overnight = SplitLayout(left=overnight_left, right=overnight_right, left_width="50%", gap="16px")
section_overnight = Section(title="🌍 隔夜外盘扫描", content=split_overnight.render(), icon="globe")
gen._components.append(section_overnight)

# ===== 3. 催化事件详解 =====
gen.add_catalyst_details(
    background="""
    "六张网"（算力网、新型电网、新一代通信网、水网、城市地下管网、物流网）是"十五五"规划的核心基建方向。
    自2026年4月政治局会议首次提出以来，政策推进节奏明显加快：5月国常会细化、7月政治局会议强调扎实推进，到8月25日发改委召开"六网协同"协调推进工作会，
    重点已从"规划"转向"落地"。<br><br>
    本次会议的特殊性在于：<b>十部门联合参会</b>（发改委、工信部、财政部、住建部、交通部、水利部、央行、金融监管总局、证监会、能源局），
    核心议题是<b>完善多元化投融资模式</b>，分类细化财政、金融、投资、价格等支持政策，推动重大项目加快开工。
    据发改委测算，"六张网"年度投资规模超7万亿元，十五五周期累计接近26万亿元。
    """,
    trigger="""
    本次催化的三重共振：<br><br>
    ① <b>政策催化</b>：发改委"六网协同"推进会召开，多部门协同解决投融资问题，算力网作为新增战略性基础设施优先级突出；
    人大常委会确认上半年GDP增4.7%创5年同期最高，稳增长政策加码空间打开。<br><br>
    ② <b>外盘催化</b>：美股半导体集体反弹，费半+1.44%、英伟达终结七连跌+2.19%、AMD+4.91%；
    马斯克宣布SpaceX AI卫星搭载英伟达Vera Rubin芯片，打开太空AI新赛道想象力。<br><br>
    ③ <b>业绩催化</b>：液冷板块进入业绩拐点，英维克Q2净利润环比增1934%，中金预测全球液冷千亿市场；
    存储板块超级周期延续，长江存储IPO受理、三星确认供应紧张至2028年。
    """
)

# ===== 4. 产业链梳理 =====
upstream = [
    {
        "name": "电力基础设施（新型电网）",
        "desc": "算力网扩张带动电网扩容、新型配电、高可靠供电设备需求",
        "stocks": [
            {"code": "600089", "name": "特变电工", "impact": "电网设备"},
            {"code": "002452", "name": "长高电新", "impact": "输变电"},
        ]
    },
    {
        "name": "光通信（新一代通信网）",
        "desc": "算力互联核心基础设施，光模块/CPO/光纤光缆需求持续放量",
        "stocks": [
            {"code": "300308", "name": "中际旭创", "impact": "光模块龙头"},
            {"code": "300502", "name": "新易盛", "impact": "光模块"},
            {"code": "688548", "name": "长光华芯", "impact": "光芯片"},
        ]
    },
]

midstream = [
    {
        "name": "算力设备（核心受益）",
        "desc": "AI服务器、GPU、推理芯片等算力硬件，直接受益算力网建设",
        "stocks": [
            {"code": "603019", "name": "中科曙光", "impact": "服务器"},
            {"code": "000977", "name": "浪潮信息", "impact": "AI服务器"},
        ]
    },
    {
        "name": "液冷散热（最强弹性）",
        "desc": "算力功耗突破风冷极限，液冷成为数据中心标配，千亿市场爆发",
        "stocks": [
            {"code": "002837", "name": "英维克", "impact": "液冷龙头★持仓"},
            {"code": "300834", "name": "申菱环境", "impact": "液冷"},
            {"code": "300499", "name": "高澜股份", "impact": "液冷"},
        ]
    },
    {
        "name": "存储芯片/HBM",
        "desc": "AI算力核心瓶颈，超级周期延续至2028年，国产替代加速",
        "stocks": [
            {"code": "301217", "name": "铜冠铜箔", "impact": "HBM铜箔★持仓"},
            {"code": "002409", "name": "雅克科技", "impact": "HBM前驱体★持仓"},
            {"code": "301308", "name": "江波龙", "impact": "存储模组"},
        ]
    },
]

downstream = [
    {
        "name": "先进封装",
        "desc": "HBM、CoWoS等先进封装产能紧张，台积电A16工艺量产在即",
        "stocks": [
            {"code": "600584", "name": "长电科技", "impact": "封测龙头"},
            {"code": "002185", "name": "华天科技", "impact": "封测"},
        ]
    },
    {
        "name": "半导体设备/材料",
        "desc": "晶圆厂扩产+国产替代双重驱动，长江存储IPO带动设备需求",
        "stocks": [
            {"code": "002371", "name": "北方华创", "impact": "设备平台龙头"},
            {"code": "688072", "name": "拓荆科技", "impact": "薄膜沉积"},
            {"code": "688396", "name": "华润微", "impact": "功率器件"},
        ]
    },
]

gen.add_industry_chain_analysis(upstream=upstream, midstream=midstream, downstream=downstream)

# ===== 5. 投资机会分析 =====
opportunities = [
    {
        "name": "液冷散热：业绩拐点+政策催化双共振",
        "priority": "高",
        "logic": "①发改委算力网建设带动液冷需求加速释放；②英维克Q2净利润环比暴增1934%，验证行业进入业绩兑现期；③中金预测液冷千亿市场，26Q3开始业绩批量兑现；④产品进入英伟达、英特尔供应链，认证壁垒高；⑤股价从高点回撤超50%，估值处于历史低位。",
        "stocks": [
            {"code": "002837", "name": "英维克", "impact": "液冷龙头"},
            {"code": "300834", "name": "申菱环境", "impact": "数据中心温控"},
            {"code": "300499", "name": "高澜股份", "impact": "液冷散热"},
            {"code": "301126", "name": "佳力图", "impact": "精密温控"},
        ]
    },
    {
        "name": "算力网络基础设施：万亿投资启动",
        "priority": "高",
        "logic": "①发改委'六网协同'推进会明确算力网为核心基建方向，年度投资超7万亿；②'2+3+N'协调机制落地，电网/通信/算力协同推进；③REITs、PPP、绿色债券等多元投融资工具创新，加速项目落地；④算力网直接带动服务器、交换机、温控、光模块全产业链需求。",
        "stocks": [
            {"code": "603019", "name": "中科曙光", "impact": "算力服务器"},
            {"code": "000977", "name": "浪潮信息", "impact": "AI服务器"},
            {"code": "300308", "name": "中际旭创", "impact": "光模块"},
        ]
    },
    {
        "name": "存储/HBM：超级周期+国产替代",
        "priority": "高",
        "logic": "①三星确认供应紧张至2028年，HBM4E速率突破16Gbps；②TrendForce预测2027年存储占CSP资本开支68%；③长江存储科创板IPO获受理，NAND跻身全球第三；④国产存储链扩产带动设备/材料/封装全产业链受益；⑤铜箔/前驱体等环节供需紧张，量价齐升逻辑持续。",
        "stocks": [
            {"code": "301217", "name": "铜冠铜箔", "impact": "HBM铜箔"},
            {"code": "002409", "name": "雅克科技", "impact": "HBM前驱体"},
            {"code": "301308", "name": "江波龙", "impact": "存储模组"},
            {"code": "603986", "name": "兆易创新", "impact": "存储芯片"},
        ]
    },
]

gen.add_investment_opportunities(opportunities, view_mode="tab")

# ===== 6. 持仓个股影响分析 =====
stk1 = StockTags([{"code": "002837", "name": "英维克", "impact": "液冷龙头★持仓"}], label="持仓标的").render()
stk2 = StockTags([{"code": "301217", "name": "铜冠铜箔", "impact": "HBM铜箔★持仓"}], label="持仓标的").render()
stk3 = StockTags([{"code": "002409", "name": "雅克科技", "impact": "HBM前驱体★持仓"}], label="持仓标的").render()

portfolio_analysis = f"""
<div style="display: flex; flex-direction: column; gap: 16px;">
    <!-- 英维克 -->
    <div style="background: rgba(255,255,255,0.04); border-radius: 14px; padding: 18px; border: 1px solid rgba(255,255,255,0.08);">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px;">
            <div style="display: flex; align-items: center;">
                <span style="font-size: 18px; font-weight: 700; color: #f1f5f9;">英维克 002837</span>
                <span style="margin-left: 10px; padding: 3px 10px; background: linear-gradient(135deg, #22c55e, #16a34a); border-radius: 20px; font-size: 12px; font-weight: 700; color: white;">液冷龙头 直接受益</span>
            </div>
            <span style="font-size: 14px; color: #94a3b8;">成本104.23元 | 参考价54.75元（8/25收）</span>
        </div>
        <div style="font-size: 13px; color: #cbd5e1; line-height: 1.8;">
            <b style="color: #22c55e;">利好逻辑：</b>①发改委算力网建设直接拉动液冷需求，行业景气度确认向上；②公司Q2净利润环比暴增1934%，业绩拐点确立；③液冷产品通过英特尔认证，进入英伟达MGX生态；④8/25涨停，主力净流入16.36亿，资金关注度骤升。<br>
            <b style="color: #f59e0b;">操作建议：</b>深度破止损状态下的超跌反弹，<b>60-65元区间坚决减仓至1/2底仓</b>，反弹至70元以上清仓离场，严禁追高补仓。本次反弹为政策催化+业绩拐点双重驱动，可利用反弹窗口优化持仓结构，液冷板块长期逻辑未变但短期需消化估值。
        </div>
        <div style="margin-top: 10px;">{stk1}</div>
    </div>
    
    <!-- 铜冠铜箔 -->
    <div style="background: rgba(255,255,255,0.04); border-radius: 14px; padding: 18px; border: 1px solid rgba(255,255,255,0.08);">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px;">
            <div style="display: flex; align-items: center;">
                <span style="font-size: 18px; font-weight: 700; color: #f1f5f9;">铜冠铜箔 301217</span>
                <span style="margin-left: 10px; padding: 3px 10px; background: linear-gradient(135deg, #3b82f6, #2563eb); border-radius: 20px; font-size: 12px; font-weight: 700; color: white;">HBM铜箔 间接受益</span>
            </div>
            <span style="font-size: 14px; color: #94a3b8;">成本87.16元 | 参考价111.11元（8/25收）</span>
        </div>
        <div style="font-size: 13px; color: #cbd5e1; line-height: 1.8;">
            <b style="color: #22c55e;">利好逻辑：</b>①存储超级周期延续，三星HBM4E进展顺利+TrendForce上调存储资本开支预期；②长江存储IPO带动国内存储产业链扩产；③公司AI高端铜箔量价齐升，上半年净利润预增486%-544%；④存储/HBM需求拉动高端铜箔供需紧张。<br>
            <b style="color: #f59e0b;">操作建议：</b>当前浮盈约27%，<b>冲高至120元附近减仓至1/3底仓锁定利润</b>，回踩100-105元可接回，跌破100元止盈。PCB铜箔板块前期涨幅较大，需警惕获利回吐压力，滚动操作降低持仓成本。
        </div>
        <div style="margin-top: 10px;">{stk2}</div>
    </div>
    
    <!-- 雅克科技 -->
    <div style="background: rgba(255,255,255,0.04); border-radius: 14px; padding: 18px; border: 1px solid rgba(255,255,255,0.08);">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px;">
            <div style="display: flex; align-items: center;">
                <span style="font-size: 18px; font-weight: 700; color: #f1f5f9;">雅克科技 002409</span>
                <span style="margin-left: 10px; padding: 3px 10px; background: linear-gradient(135deg, #8b5cf6, #7c3aed); border-radius: 20px; font-size: 12px; font-weight: 700; color: white;">HBM前驱体 核心受益</span>
            </div>
            <span style="font-size: 14px; color: #94a3b8;">成本108.80元 | 中报发布中</span>
        </div>
        <div style="font-size: 13px; color: #cbd5e1; line-height: 1.8;">
            <b style="color: #22c55e;">利好逻辑：</b>①HBM需求爆发，前驱体作为关键材料量价齐升；②公司发布2026中报：净利润5.61亿元同比+7.29%，Q2单季净利润同比+12.08%；③长江存储IPO+国内存储扩产带动前驱体国产替代加速；④大基金持股，机构认可度高。<br>
            <b style="color: #f59e0b;">操作建议：</b>HBM前驱体龙头地位稳固，中报业绩平稳增长符合预期。<b>150元以上维持半仓持有</b>，反弹至160-170元可减仓1/3锁利，跌破140元止盈至底仓。需注意前十大流通股东中部分机构减持，短期或有抛压。
        </div>
        <div style="margin-top: 10px;">{stk3}</div>
    </div>
    
    <!-- *ST建艺 -->
    <div style="background: rgba(239,68,68,0.06); border-radius: 14px; padding: 18px; border: 1px solid rgba(239,68,68,0.2);">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px;">
            <div style="display: flex; align-items: center;">
                <span style="font-size: 18px; font-weight: 700; color: #f1f5f9;">*ST建艺 002789</span>
                <span style="margin-left: 10px; padding: 3px 10px; background: linear-gradient(135deg, #ef4444, #dc2626); border-radius: 20px; font-size: 12px; font-weight: 700; color: white;">退市风险 立即清仓</span>
            </div>
            <span style="font-size: 14px; color: #94a3b8;">成本~13.45元 | 退市高风险</span>
        </div>
        <div style="font-size: 13px; color: #fca5a5; line-height: 1.8;">
            ⚠️ <b>退市风险未解除，任何价格立即清仓（最高优先级）</b>，本次六网协同催化与ST建艺无任何关联，退市风险敞口必须关闭，绝不恋战。
        </div>
    </div>
</div>
"""

section_portfolio = Section(title="📊 持仓影响与操作指引", content=portfolio_analysis, icon="pie-chart", variant="highlight")
gen._components.append(section_portfolio)

# ===== 7. 催化深度分析（Skill增强） =====
events = [
    {
        "title": "发改委'六网协同'万亿算力网基建",
        "type": "policy",
        "description": "发改委召开六网协同协调推进会，算力网纳入国家战略性基础设施，年度投资规模超7万亿元，十五五周期累计接近26万亿元。十部门联合参会，完善多元化投融资模式，推动重大项目加快开工建设。",
        "category": "政策催化"
    },
    {
        "title": "美股半导体集体反弹 英伟达终结七连跌",
        "type": "data",
        "description": "费城半导体指数涨1.44%，英伟达涨2.19%终结七连跌，AMD涨4.91%，美光涨2.48%。马斯克宣布SpaceX AI卫星搭载英伟达Vera Rubin芯片，2027年Q4首射。市场等待8/26盘后英伟达Q2财报。",
        "category": "外盘催化"
    },
    {
        "title": "液冷板块业绩拐点 英维克Q2环比暴增",
        "type": "earnings",
        "description": "英维克Q2净利润环比暴增1934%，液冷进入业绩兑现期。中金预测全球液冷千亿市场，26Q3开始业绩批量兑现。产品进入英伟达、英特尔供应链。8/25涨停，主力净流入16.36亿。",
        "category": "业绩催化"
    },
]

gen.add_catalyst_deep_analysis(events)

# ===== 8. 风险提示 =====
gen.add_risk_warning([
    "英伟达8/26盘后财报不及预期风险：市场预期营收920亿美元（yoy+96%），若数据中心业务增速低于预期或指引不及，可能引发科技股回调",
    "美联储杰克逊霍尔年会（8/29）政策转向风险：若主席沃什释放鹰派信号，美债收益率上行将压制科技成长股估值",
    "六网协同政策落地不及预期：投融资机制完善需要时间，项目实际开工和订单兑现存在时滞",
    "液冷板块短期涨幅过大回调风险：英维克Q2业绩基数低，环比增长存在季节性因素，估值208倍PE偏高",
    "存储板块获利回吐压力：江波龙、兆易等标的前期涨幅巨大，中报业绩兑现后或有获利盘出逃",
    "持仓个股估值风险：英维克PE208倍/铜冠铜箔PE215倍/雅克科技估值偏高，需警惕业绩增速与估值不匹配",
])

# ===== 9. 投资策略建议 =====
gen.add_investment_strategy("""
<b>一、整体判断：S级政策催化+外盘情绪修复，科技成长股有望迎来反弹窗口</b><br><br>
本次"六网协同"推进会标志着算力网从规划进入落地阶段，叠加美股半导体反弹和液冷业绩拐点，形成三方面共振。但需注意：这是<b>政策驱动的反弹行情</b>而非趋势反转，操作上以<b>逢高减仓、滚动锁利</b>为主基调。<br><br>

<b>二、优先级排序</b><br>
1. 🥇 <b>第一优先级（高弹性）：液冷散热</b> — 政策最直接受益+业绩拐点确认+标的稀缺，英维克为核心标的，但估值偏高需谨慎<br>
2. 🥈 <b>第二优先级（确定性）：存储/HBM</b> — 超级周期逻辑未变+国产替代加速，雅克科技+铜冠铜箔双龙头组合<br>
3. 🥉 <b>第三优先级（补涨）：算力设备/光通信</b> — 算力网建设直接受益，但前期涨幅较大，需等待回调机会<br><br>

<b>三、仓位与操作策略</b><br>
- 整体仓位控制在<b>4-5成</b>，不宜满仓追高<br>
- 持仓操作：英维克反弹60-65元减仓≥1/2；铜冠铜箔冲高120元减至1/3底仓；雅克科技150以上持半仓观察；*ST建艺立即清仓<br>
- 新增关注：半导体设备（北方华创、拓荆科技）— 长江存储IPO+国产替代双驱动<br>
- 回避：高位光模块龙头（中际旭创等）— 机构净流出明显，逻辑松动<br><br>

<b>四、关键时间节点</b><br>
- 8/26盘后：英伟达Q2财报（关键风向标）<br>
- 8/29-30：杰克逊霍尔央行年会（美联储政策信号）<br>
- 9/1：私募基金信披新规实施<br>
- 9月：美联储议息会议
""")

# ===== 发布 =====
result = gen.publish(
    title="S级催化 - 六网协同万亿算力网",
    report_type="s_level_catalyst",
    filename="20260826_盘前_S级催化扫描_六网协同万亿算力网.html",
    excerpt="发改委六网协同推进会召开，万亿算力网基建进入实操阶段；美股半导体集体反弹，英伟达终结七连跌；液冷板块业绩拐点确认，英维克Q2环比暴增1934%"
)

print("发布结果:", result)
