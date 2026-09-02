"""
S级催化扫描 - 盘前 - 20260903
核心催化：博通AI半导体收入暴增221%+英伟达35亿投联发科+韩国管制落地+亚太股市大跌
"""
import sys
import os

os.chdir('/root/daily-news-insight')
sys.path.insert(0, 'v3')

from v3.generators.s_level_catalyst import SLevelCatalystGenerator

# ============================================================
# 初始化生成器
# ============================================================
gen = SLevelCatalystGenerator(
    date_str="20260903",
    catalyst_title="博通AI半导体暴增221%+英伟达35亿投联发科+亚太科技股深震",
    subtitle="2026.09.03 · 盘前S级催化"
)

# ============================================================
# 1. 催化事件概述
# ============================================================
overview = """
<b>【隔夜美股】</b>美股三大指数集体收涨终结三连跌：道指+0.56%、标普500+0.46%、纳指+0.45%。费城半导体指数+0.45%报11339点，呈现V型反转走势（盘中一度下探至11154点）。芯片股多数上涨，思佳讯+6%、美光+2.43%、英伟达+3.21%、高通+2%、闪迪+1.08%。

<b>【盘后重磅】</b>博通(AVGO)公布2026财年Q3财报：
① 营收295.91亿美元，同比+86%，超预期；
② AI半导体收入167亿美元，同比<b>+221%</b>、环比+54%，超市场预期159.3亿美元；
③ 上调全年AI业务指引至580亿美元（+186%），2027年AI营收将翻倍至1150亿美元，2028年再翻倍至2300亿美元；
④ 谷歌下一代TPU8I性能比肩英伟达Vera Rubin，已开始量产交付。
盘后股价一度跌6%（Q4指引略低于预期），但CEO电话会议后深V反弹，最终微跌0.9%。

<b>【亚太重挫】</b>日经225大跌2.85%，韩国KOSPI暴跌3.99%（SK海力士跌近10%）。A50期货夜盘跌1.23%。亚太科技股集体承压，主要受韩国管制新规落地+获利盘兑现双重冲击。

<b>【产业催化】</b>
① 英伟达35亿美元投资联发科，深化AI基础设施/本地AI/汽车三大领域合作，争夺"机架级"AI芯片入口；
② 台积电CoWoS明年产能配额全被预订，部分客户转向英特尔EMIB-T，先进封装供需紧张持续；
③ 韩国9月1日起实施新规，高性能AI芯片及先进半导体设备列入战略物项出口管制，国产替代逻辑进一步强化；
④ 富时A50指数季度调整：纳入中微公司、生益科技，剔除牧原股份、万华化学，半导体龙头获被动资金加持。

<b>【国内政策】</b>央行行长潘功胜G20会议表态：继续实施适度宽松货币政策，汇率稳定立场明确。工信部强调"十五五"着力加强产业创新和关键核心技术攻关。
"""
gen.add_catalyst_overview(overview, importance="高")

# ============================================================
# 2. 催化事件详解
# ============================================================
background = """
<b>隔夜全球半导体三重信号</b>

<b>1. 博通财报：AI算力需求持续超预期</b>
博通Q3 AI半导体收入167亿美元（+221% YoY），超市场预期约8亿美元。更重磅的是电话会议指引：
· 上调2026全年AI收入指引至580亿美元（此前560亿）
· 2027年AI营收将翻倍至1150亿美元
· 2028年再翻倍至2300亿美元
· 未来两年交付价值约3500亿美元AI半导体产品
CEO陈福阳明确表示"实际需求超过给出的指引，但只能按已锁定供应写财报指引"。

<b>2. 英伟达35亿投资联发科：AI生态扩张</b>
英伟达认购联发科35亿美元海外可转换公司债（接近九成），是英伟达迄今在美国以外最大的直接投资。双方将在AI基础设施、本地AI计算、汽车三大领域共同开发下一代计算平台。联发科披露B200加速器成本结构：排除内存后75%的成本...这意味着AI芯片的"机架级"竞争格局正在重塑。

<b>3. 韩国管制落地：国产替代加速</b>
韩国9月1日起实施新规，将高性能AI芯片（总处理性能≥6000）及先进半导体设备（曝光、刻蚀、沉积）列入战略物项，出口须获许可。三星HBM产能70%锁定至2031年（长约客户含英伟达、微软、谷歌），HBM3E现货价2100美元（是长约价4-5倍），HBM4现货价高达3500美元。

<b>亚太股市暴跌原因</b>
· 韩国KOSPI跌3.99%：SK海力士跌近10%，外资集中兑现+管制担忧
· 日经225跌2.85%：科技股跟随调整
· 本质：短期获利盘集中出逃，产业趋势未变
"""

trigger = """
<b>直接触发因素（多方共振）</b>

1️⃣ <b>基本面：博通财报验证AI算力需求韧性</b>
AI半导体收入+221%超预期，2026-2028年指引从580亿→1150亿→2300亿，两年翻倍再翻倍。谷歌TPU8I性能比肩英伟达Vera Rubin，说明AI芯片军备竞赛远未结束。利好A股：AI算力上游（PCB/铜箔/液冷/光模块）、国产AI芯片、先进封装。

2️⃣ <b>政策面：韩国管制落地+A50纳入半导体龙头</b>
韩国对华AI芯片和半导体设备管制9月1日正式生效，与日本8月管制形成叠加效应。国产替代逻辑从"可选"变为"必选"。富时A50纳入中微公司、生益科技，9月18日生效后被动资金流入。

3️⃣ <b>资金面：亚太科技股去杠杆传导</b>
韩国存储板块近一个月暴涨后外资集中兑现，SK海力士单周最大回撤超20%。A股半导体板块9月2日主力净流出超113亿元，CPO、存储、半导体设备集体调整。但需注意：缩量调整+博通盘后深V反弹=抛压衰竭信号。

4️⃣ <b>产业面：台积电CoWoS持续紧缺+散热升级</b>
台积电CoWoS明年产能配额全被预订，部分客户转向英特尔EMIB-T。台积电布局微通道散热技术，2029年CoWoS拟整合24颗HBM。液冷从\"可选项\"加速演变为\"必选项\"，英维克等国内厂商加速切入北美供应链。

<b>【反向支撑信号】</b>
· 博通盘后深V：财报指引虽略低预期，但中长期AI需求指引超强劲
· 戴尔大涨15.8%：上调全年营收至1920亿（市场预期1738亿），AI服务器需求爆发
· 富时A50纳入中微/生益：被动资金增量利好半导体龙头
· 央行适度宽松表态：国内货币政策环境友好
"""
gen.add_catalyst_details(background, trigger)

# ============================================================
# 3. 产业链梳理
# ============================================================
upstream = [
    {
        "name": "半导体设备（国产替代核心受益）",
        "desc": "韩国+日本双重管制落地，半导体设备国产替代进入加速期。富时A50纳入中微公司，被动资金加持。CSEAC 2026展会显示三季度设备订单景气度持续提升。",
        "stocks": [
            {"code": "688012", "name": "中微公司", "impact": "A50纳入+刻蚀龙头"},
            {"code": "002371", "name": "北方华创", "impact": "设备平台龙头"},
            {"code": "688072", "name": "拓荆科技", "impact": "薄膜设备"},
            {"code": "688361", "name": "中科飞测", "impact": "量检测高弹性"},
        ]
    },
    {
        "name": "半导体材料（供应链安全强化）",
        "desc": "HBM需求爆发+存储涨价周期+国产替代三重催化。雅克科技向长鑫供应high-k和硅基前驱体，长鑫扩产直接受益。鼎龙股份CMP抛光垫通过长鑫多轮验证。",
        "stocks": [
            {"code": "002409", "name": "雅克科技", "impact": "HBM前驱体龙头"},
            {"code": "688535", "name": "华海诚科", "impact": "先进封装材料"},
            {"code": "300054", "name": "鼎龙股份", "impact": "CMP抛光垫"},
            {"code": "688126", "name": "沪硅产业", "impact": "12英寸大硅片"},
        ]
    },
    {
        "name": "高端铜箔/PCB（AI算力上游）",
        "desc": "AI服务器高阶PCB/HVLP铜箔需求持续增长。铜冠铜箔HVLP1-4代全系列已完成客户供货布局，HVLP5代研发突破关键指标。半导体硅晶圆三年来首次全线涨价（6/8/12英寸全系列一成起步）。",
        "stocks": [
            {"code": "301217", "name": "铜冠铜箔", "impact": "HVLP铜箔龙头"},
            {"code": "600183", "name": "生益科技", "impact": "A50纳入+CCL龙头"},
        ]
    },
]

midstream = [
    {
        "name": "存储芯片/HBM（周期上行+国产替代）",
        "desc": "全球存储涨价周期延续，高盛给予三星/SK海力士'买入'评级。三星70%产能锁定至2031年，HBM3E现货价2100美元（长约价4-5倍）。长鑫科技扩产+技术升级带动A股产业链。",
        "stocks": [
            {"code": "688525", "name": "佰维存储", "impact": "存储模组+HBM"},
            {"code": "301308", "name": "江波龙", "impact": "存储龙头"},
            {"code": "603986", "name": "兆易创新", "impact": "利基存储+MCU"},
            {"code": "688825", "name": "长鑫科技", "impact": "DRAM国产替代"},
        ]
    },
    {
        "name": "先进封装/Chiplet（3D堆叠核心）",
        "desc": "台积电CoWoS明年产能全被预订，2029年扩至14倍光罩尺寸+整合24颗HBM。先进封装是EUV受限背景下的核心突围路径。通富微电、长电科技受益于国产替代+算力需求。",
        "stocks": [
            {"code": "002156", "name": "通富微电", "impact": "AMD封测主力"},
            {"code": "600584", "name": "长电科技", "impact": "封测龙头"},
            {"code": "002185", "name": "华天科技", "impact": "封测"},
        ]
    },
    {
        "name": "液冷散热（AI算力刚需）",
        "desc": "液冷从\"可选项\"加速演变为\"必选项\"。英伟达下一代Vera Rubin平台全面导入全液冷架构。台积电布局微通道散热技术。国内液冷供应商加速切入北美算力服务器供应链。英维克上半年营收30.17亿（+17.24%），Q2净利环比增1934%。",
        "stocks": [
            {"code": "002837", "name": "英维克", "impact": "液冷龙头+切入英伟达供应"},
            {"code": "300896", "name": "爱美客", "impact": "冷板式液冷"},
        ]
    },
]

downstream = [
    {
        "name": "国产AI芯片（军备竞赛加速）",
        "desc": "谷歌TPU8I性能比肩英伟达Vera Rubin，AI芯片多极化竞争格局形成。华为Mate 90预计搭载韬定律芯片9月23日发布。燧原科技IPO发行价142.18元/股，国产AI芯片密集资本化。瑞银称国产GPU下半年将大规模放量。",
        "stocks": [
            {"code": "603019", "name": "中科曙光", "impact": "国产算力"},
            {"code": "688041", "name": "海光信息", "impact": "国产CPU/GPU"},
            {"code": "688256", "name": "寒武纪", "impact": "AI芯片"},
        ]
    },
    {
        "name": "军工/防务科技（避险+地缘催化）",
        "desc": "中东地缘冲突升级，避险资金流入军工板块。建军百年节点临近，军贸、军用材料、航空发动机等细分环节持续催化。9月2日军工板块逆势活跃，内蒙一机2连板。",
        "stocks": [
            {"code": "600967", "name": "内蒙一机", "impact": "2连板+军贸"},
            {"code": "601698", "name": "中国卫通", "impact": "卫星互联网"},
        ]
    },
]

gen.add_industry_chain_analysis(upstream, midstream, downstream)

# ============================================================
# 4. 隔夜外盘扫描模块
# ============================================================
from components.layout import Section

overnight_html = """
<div style="display: flex; flex-direction: column; gap: 16px;">
    
    <!-- 美股三大指数 -->
    <div style="background: linear-gradient(135deg, rgba(16,185,129,0.10) 0%, rgba(5,150,105,0.06) 100%); 
                border-radius: 14px; padding: 18px 20px; border: 1px solid rgba(16,185,129,0.25);">
        <div style="display: flex; align-items: center; margin-bottom: 14px;">
            <div style="width: 36px; height: 36px; background: linear-gradient(135deg, #10b981, #059669); 
                       border-radius: 10px; display: flex; align-items: center; justify-content: center; margin-right: 12px;">
                🇺🇸
            </div>
            <span style="font-size: 16px; font-weight: 700; color: #6ee7b7;">美股隔夜（9月2日收盘）· 终结三连跌</span>
        </div>
        <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 12px;">
            <div style="background: rgba(0,0,0,0.25); border-radius: 10px; padding: 12px; text-align: center;">
                <div style="font-size: 11px; color: #94a3b8; margin-bottom: 4px;">道琼斯</div>
                <div style="font-size: 17px; font-weight: 800; color: #34d399;">+0.56%</div>
                <div style="font-size: 10px; color: #64748b;">53,061.95</div>
            </div>
            <div style="background: rgba(0,0,0,0.25); border-radius: 10px; padding: 12px; text-align: center;">
                <div style="font-size: 11px; color: #94a3b8; margin-bottom: 4px;">纳斯达克</div>
                <div style="font-size: 17px; font-weight: 800; color: #34d399;">+0.45%</div>
                <div style="font-size: 10px; color: #64748b;">26,217.83</div>
            </div>
            <div style="background: rgba(0,0,0,0.25); border-radius: 10px; padding: 12px; text-align: center;">
                <div style="font-size: 11px; color: #94a3b8; margin-bottom: 4px;">标普500</div>
                <div style="font-size: 17px; font-weight: 800; color: #34d399;">+0.46%</div>
                <div style="font-size: 10px; color: #64748b;">7,666.60</div>
            </div>
            <div style="background: rgba(0,0,0,0.25); border-radius: 10px; padding: 12px; text-align: center;">
                <div style="font-size: 11px; color: #94a3b8; margin-bottom: 4px;">费半SOX</div>
                <div style="font-size: 17px; font-weight: 800; color: #34d399;">+0.45%</div>
                <div style="font-size: 10px; color: #64748b;">11,339.25</div>
            </div>
        </div>
        <div style="font-size: 11px; color: #64748b; margin-top: 10px; font-style: italic;">
            数据来源：Wind / TradingKey · 2026-09-03 更新
        </div>
    </div>

    <!-- 半导体核心个股 -->
    <div style="background: linear-gradient(135deg, rgba(139,92,246,0.10) 0%, rgba(124,58,237,0.06) 100%); 
                border-radius: 14px; padding: 18px 20px; border: 1px solid rgba(139,92,246,0.25);">
        <div style="display: flex; align-items: center; margin-bottom: 14px;">
            <div style="width: 36px; height: 36px; background: linear-gradient(135deg, #8b5cf6, #7c3aed); 
                       border-radius: 10px; display: flex; align-items: center; justify-content: center; margin-right: 12px;">
                🔬
            </div>
            <span style="font-size: 16px; font-weight: 700; color: #c4b5fd;">半导体核心个股表现</span>
        </div>
        <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 10px;">
            <div style="background: rgba(0,0,0,0.25); border-radius: 10px; padding: 10px; text-align: center;">
                <div style="font-size: 11px; color: #94a3b8; margin-bottom: 3px;">英伟达 NVDA</div>
                <div style="font-size: 15px; font-weight: 800; color: #34d399;">+3.21%</div>
            </div>
            <div style="background: rgba(0,0,0,0.25); border-radius: 10px; padding: 10px; text-align: center;">
                <div style="font-size: 11px; color: #94a3b8; margin-bottom: 3px;">博通 AVGO</div>
                <div style="font-size: 15px; font-weight: 800; color: #f87171;">-0.66%</div>
            </div>
            <div style="background: rgba(0,0,0,0.25); border-radius: 10px; padding: 10px; text-align: center;">
                <div style="font-size: 11px; color: #94a3b8; margin-bottom: 3px;">AMD</div>
                <div style="font-size: 15px; font-weight: 800; color: #34d399;">+2.0%+</div>
            </div>
            <div style="background: rgba(0,0,0,0.25); border-radius: 10px; padding: 10px; text-align: center;">
                <div style="font-size: 11px; color: #94a3b8; margin-bottom: 3px;">美光 MU</div>
                <div style="font-size: 15px; font-weight: 800; color: #34d399;">+2.43%</div>
            </div>
            <div style="background: rgba(0,0,0,0.25); border-radius: 10px; padding: 10px; text-align: center;">
                <div style="font-size: 11px; color: #94a3b8; margin-bottom: 3px;">应用材料</div>
                <div style="font-size: 15px; font-weight: 800; color: #f87171;">~-1%</div>
            </div>
            <div style="background: rgba(0,0,0,0.25); border-radius: 10px; padding: 10px; text-align: center;">
                <div style="font-size: 11px; color: #94a3b8; margin-bottom: 3px;">泛林 LRCX</div>
                <div style="font-size: 15px; font-weight: 800; color: #f87171;">-0.65%</div>
            </div>
            <div style="background: rgba(0,0,0,0.25); border-radius: 10px; padding: 10px; text-align: center;">
                <div style="font-size: 11px; color: #94a3b8; margin-bottom: 3px;">科磊 KLAC</div>
                <div style="font-size: 15px; font-weight: 800; color: #34d399;">+0.80%</div>
            </div>
            <div style="background: rgba(0,0,0,0.25); border-radius: 10px; padding: 10px; text-align: center;">
                <div style="font-size: 11px; color: #94a3b8; margin-bottom: 3px;">台积电 TSM</div>
                <div style="font-size: 15px; font-weight: 800; color: #fbbf24;">~持平</div>
            </div>
        </div>
        <div style="font-size: 11px; color: #64748b; margin-top: 10px; font-style: italic;">
            注：博通为盘后走势，财报公布后一度跌6%，CEO电话会指引超预期后深V反弹最终微跌0.9%
        </div>
    </div>

    <!-- 亚太市场 -->
    <div style="background: linear-gradient(135deg, rgba(239,68,68,0.10) 0%, rgba(220,38,38,0.06) 100%); 
                border-radius: 14px; padding: 18px 20px; border: 1px solid rgba(239,68,68,0.25);">
        <div style="display: flex; align-items: center; margin-bottom: 14px;">
            <div style="width: 36px; height: 36px; background: linear-gradient(135deg, #ef4444, #dc2626); 
                       border-radius: 10px; display: flex; align-items: center; justify-content: center; margin-right: 12px;">
                🌏
            </div>
            <span style="font-size: 16px; font-weight: 700; color: #fca5a5;">亚太市场（9月2日收盘）· 集体大跌</span>
        </div>
        <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 12px;">
            <div style="background: rgba(0,0,0,0.25); border-radius: 10px; padding: 12px; text-align: center;">
                <div style="font-size: 11px; color: #94a3b8; margin-bottom: 4px;">日经225</div>
                <div style="font-size: 17px; font-weight: 800; color: #f87171;">-2.85%</div>
            </div>
            <div style="background: rgba(0,0,0,0.25); border-radius: 10px; padding: 12px; text-align: center;">
                <div style="font-size: 11px; color: #94a3b8; margin-bottom: 4px;">韩国KOSPI</div>
                <div style="font-size: 17px; font-weight: 800; color: #f87171;">-3.99%</div>
            </div>
            <div style="background: rgba(0,0,0,0.25); border-radius: 10px; padding: 12px; text-align: center;">
                <div style="font-size: 11px; color: #94a3b8; margin-bottom: 4px;">SK海力士</div>
                <div style="font-size: 17px; font-weight: 800; color: #f87171;">~-10%</div>
            </div>
            <div style="background: rgba(0,0,0,0.25); border-radius: 10px; padding: 12px; text-align: center;">
                <div style="font-size: 11px; color: #94a3b8; margin-bottom: 4px;">A50期货</div>
                <div style="font-size: 17px; font-weight: 800; color: #f87171;">-1.23%</div>
            </div>
        </div>
        <div style="font-size: 12px; color: #cbd5e1; margin-top: 10px; line-height: 1.6;">
            <b>核心原因</b>：韩国半导体出口管制新规落地+前期暴涨后外资集中兑现获利盘。韩国KOSPI近一个月累计涨幅超20%，技术性调整需求强烈。
        </div>
    </div>

    <!-- 韩国/亚洲产业政策 -->
    <div style="background: linear-gradient(135deg, rgba(245,158,11,0.10) 0%, rgba(217,119,6,0.06) 100%); 
                border-radius: 14px; padding: 18px 20px; border: 1px solid rgba(245,158,11,0.25);">
        <div style="display: flex; align-items: center; margin-bottom: 14px;">
            <div style="width: 36px; height: 36px; background: linear-gradient(135deg, #f59e0b, #d97706); 
                       border-radius: 10px; display: flex; align-items: center; justify-content: center; margin-right: 12px;">
                📋
            </div>
            <span style="font-size: 16px; font-weight: 700; color: #fcd34d;">韩国/亚洲半导体产业动态</span>
        </div>
        <div style="display: flex; flex-direction: column; gap: 10px;">
            <div style="background: rgba(0,0,0,0.2); border-radius: 10px; padding: 12px 14px;">
                <div style="font-size: 13px; font-weight: 600; color: #fbbf24; margin-bottom: 4px;">🇰🇷 韩国9月1日实施芯片出口管制新规</div>
                <div style="font-size: 12px; color: #94a3b8; line-height: 1.6;">
                    高性能AI芯片（总处理性能≥6000）及先进半导体设备（曝光/刻蚀/沉积）列入战略物项，出口须获许可。同步上调高能电池管制门槛，新增核酸合成仪等管控。约80项国际管制调整纳入。
                </div>
            </div>
            <div style="background: rgba(0,0,0,0.2); border-radius: 10px; padding: 12px 14px;">
                <div style="font-size: 13px; font-weight: 600; color: #fbbf24; margin-bottom: 4px;">🇰🇷 三星70%产能锁定至2031年</div>
                <div style="font-size: 12px; color: #94a3b8; line-height: 1.6;">
                    三星存储部门已将2031年前约70%产能分配给长约订单（英伟达、微软、谷歌等）。HBM3E现货价2100美元（长约价4-5倍），HBM4现货价高达3500美元。HBM生产吸收大量DRAM产能，加剧整体供应短缺。
                </div>
            </div>
            <div style="background: rgba(0,0,0,0.2); border-radius: 10px; padding: 12px 14px;">
                <div style="font-size: 13px; font-weight: 600; color: #fbbf24; margin-bottom: 4px;">🇯🇵 SK海力士考虑与铠侠在日本建NAND工厂</div>
                <div style="font-size: 12px; color: #94a3b8; line-height: 1.6;">
                    SK集团会长崔泰源称与铠侠联合生产是"选项之一"，日本地方政府积极招商。若合作落地，SK海力士+铠侠NAND市场份额将超三星，全球存储格局迎变局。
                </div>
            </div>
            <div style="background: rgba(0,0,0,0.2); border-radius: 10px; padding: 12px 14px;">
                <div style="font-size: 13px; font-weight: 600; color: #fbbf24; margin-bottom: 4px;">🇹🇼 台积电高雄建先进封装中心</div>
                <div style="font-size: 12px; color: #94a3b8; line-height: 1.6;">
                    台积电与高雄市政府合作在白蒲工业园建先进封装中心，CoWoS产能CAGR超80%至2027年。微通道散热技术纳入研发蓝图，2029年CoWoS拟整合24颗HBM。
                </div>
            </div>
        </div>
    </div>
</div>
"""

gen._components.append(Section(title="🌍 隔夜全球扫描", content=overnight_html, icon="globe"))

# ============================================================
# 5. 持仓股分析
# ============================================================
portfolio_html = """
<div style="display: flex; flex-direction: column; gap: 14px;">

    <!-- 雅克科技 -->
    <div style="border-left: 4px solid #ef4444; border-radius: 0 12px 12px 0;">
        <div style="background: rgba(255,255,255,0.04); border-radius: 0 12px 12px 0; padding: 16px 20px; backdrop-filter: blur(10px); border: 1px solid rgba(255,255,255,0.06); border-left: none;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
                <div>
                    <span style="font-size: 18px; font-weight: 700; color: #f1f5f9;">雅克科技 (002409)</span>
                    <span style="margin-left: 12px; padding: 3px 10px; background: linear-gradient(135deg, #f59e0b, #d97706); color: white; border-radius: 20px; font-size: 12px; font-weight: 700;">-5.72%（9/1）</span>
                </div>
                <span style="font-size: 22px; font-weight: 800; color: #fbbf24;">134.23元</span>
            </div>
            <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 12px; margin-bottom: 12px;">
                <div style="background: rgba(0,0,0,0.2); border-radius: 8px; padding: 10px; text-align: center;">
                    <div style="font-size: 11px; color: #94a3b8; margin-bottom: 4px;">TTM市盈率</div>
                    <div style="font-size: 15px; font-weight: 700; color: #60a5fa;">55.5倍</div>
                </div>
                <div style="background: rgba(0,0,0,0.2); border-radius: 8px; padding: 10px; text-align: center;">
                    <div style="font-size: 11px; color: #94a3b8; margin-bottom: 4px;">融资余额</div>
                    <div style="font-size: 15px; font-weight: 700; color: #fbbf24;">28.76亿</div>
                </div>
                <div style="background: rgba(0,0,0,0.2); border-radius: 8px; padding: 10px; text-align: center;">
                    <div style="font-size: 11px; color: #94a3b8; margin-bottom: 4px;">H1营收增速</div>
                    <div style="font-size: 15px; font-weight: 700; color: #34d399;">+5.12%</div>
                </div>
                <div style="background: rgba(0,0,0,0.2); border-radius: 8px; padding: 10px; text-align: center;">
                    <div style="font-size: 11px; color: #94a3b8; margin-bottom: 4px;">H1净利增速</div>
                    <div style="font-size: 15px; font-weight: 700; color: #34d399;">+7.29%</div>
                </div>
            </div>
            <div style="font-size: 13px; color: #cbd5e1; line-height: 1.8;">
                <b>【隔夜催化影响】</b>博通AI半导体收入+221%超预期+三星HBM产能锁定，存储/HBM产业链需求逻辑进一步强化。
                <br>✅ <b>产业逻辑</b>：雅克科技向长鑫供应high-k和硅基前驱体，长鑫扩产+技术升级直接受益。韩国管制加速国产替代，半导体材料供应链安全重要性提升。
                <br>✅ <b>估值锚</b>：TTM 55.5倍PE，处于半导体材料板块中等水平。HBM前驱体国产替代空间大，中期成长逻辑未变。
                <br>⚠️ <b>短期风险</b>：融资余额28.76亿（占流通市值6.73%），连续2日净偿还，杠杆资金有松动迹象。亚太科技股暴跌或带来情绪冲击。
                <br>🎯 <b>操作建议</b>：<b>底仓持有观望</b>。若早盘低开至125-128元区间且企稳，可考虑小仓位加仓做T；若跌破120元（前期平台）则减仓至1/4底仓。上方压力位140元（5日线），强压力位150元。
                <br><span style="color: #94a3b8; font-size: 11px;">【双重验证说明】当前为产业逻辑强化+股价回调的背离状态，无明确减仓信号。单一融资净偿还不构成看空信号（占比<1%成交额）。</span>
            </div>
        </div>
    </div>

    <!-- 铜冠铜箔 -->
    <div style="border-left: 4px solid #f59e0b; border-radius: 0 12px 12px 0;">
        <div style="background: rgba(255,255,255,0.04); border-radius: 0 12px 12px 0; padding: 16px 20px; backdrop-filter: blur(10px); border: 1px solid rgba(255,255,255,0.06); border-left: none;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
                <div>
                    <span style="font-size: 18px; font-weight: 700; color: #f1f5f9;">铜冠铜箔 (301217)</span>
                    <span style="margin-left: 12px; padding: 3px 10px; background: linear-gradient(135deg, #f87171, #ef4444); color: white; border-radius: 20px; font-size: 12px; font-weight: 700;">-4.67%（9/2）</span>
                </div>
                <span style="font-size: 22px; font-weight: 800; color: #f87171;">108.89元</span>
            </div>
            <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 12px; margin-bottom: 12px;">
                <div style="background: rgba(0,0,0,0.2); border-radius: 8px; padding: 10px; text-align: center;">
                    <div style="font-size: 11px; color: #94a3b8; margin-bottom: 4px;">3日主力</div>
                    <div style="font-size: 15px; font-weight: 700; color: #f87171;">-2.09亿</div>
                </div>
                <div style="background: rgba(0,0,0,0.2); border-radius: 8px; padding: 10px; text-align: center;">
                    <div style="font-size: 11px; color: #94a3b8; margin-bottom: 4px;">5日主力</div>
                    <div style="font-size: 15px; font-weight: 700; color: #34d399;">+2.89亿</div>
                </div>
                <div style="background: rgba(0,0,0,0.2); border-radius: 8px; padding: 10px; text-align: center;">
                    <div style="font-size: 11px; color: #94a3b8; margin-bottom: 4px;">动态PE</div>
                    <div style="font-size: 15px; font-weight: 700; color: #fbbf24;">>200倍</div>
                </div>
                <div style="background: rgba(0,0,0,0.2); border-radius: 8px; padding: 10px; text-align: center;">
                    <div style="font-size: 11px; color: #94a3b8; margin-bottom: 4px;">高点回撤</div>
                    <div style="font-size: 15px; font-weight: 700; color: #f87171;">~12%</div>
                </div>
            </div>
            <div style="font-size: 13px; color: #cbd5e1; line-height: 1.8;">
                <b>【隔夜催化影响】</b>戴尔上调全年AI服务器收入至740亿美元（当前已达600亿）+博通AI半导体收入暴增，AI算力上游铜箔需求逻辑再获验证。
                <br>✅ <b>产业逻辑</b>：AI服务器高阶PCB/HVLP铜箔需求持续增长。铜冠铜箔HVLP1-4代全系列已完成客户供货布局，HVLP5代研发突破关键指标。半导体硅晶圆三年来首次全线涨价（6/8/12英寸一成起步）。
                <br>⚠️ <b>估值压力</b>：动态PE超200倍处于极高区间，需业绩持续超预期消化估值。短期股价从高点回撤12%，技术面与估值压力共振。
                <br>🎯 <b>操作建议</b>：<b>持有底仓观察</b>。重点关注107元（昨日低点）支撑力度，若企稳可观察反弹力度；若有效跌破则短期调整可能深化，减仓至1/4底仓。上方压力位120元（5日线）。
                <br><span style="color: #94a3b8; font-size: 11px;">【双重验证说明】主力3日净流出2.09亿但5日仍净流入2.89亿，属短期调仓而非趋势性出逃。结合产业逻辑未破坏，暂不触发≥30%减仓指令。</span>
            </div>
        </div>
    </div>

    <!-- 英维克 -->
    <div style="border-left: 4px solid #3b82f6; border-radius: 0 12px 12px 0;">
        <div style="background: rgba(255,255,255,0.04); border-radius: 0 12px 12px 0; padding: 16px 20px; backdrop-filter: blur(10px); border: 1px solid rgba(255,255,255,0.06); border-left: none;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
                <div>
                    <span style="font-size: 18px; font-weight: 700; color: #f1f5f9;">英维克 (002837)</span>
                    <span style="margin-left: 12px; padding: 3px 10px; background: linear-gradient(135deg, #10b981, #059669); color: white; border-radius: 20px; font-size: 12px; font-weight: 700;">+0.50%（9/2）</span>
                </div>
                <span style="font-size: 22px; font-weight: 800; color: #60a5fa;">66.23元</span>
            </div>
            <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 12px; margin-bottom: 12px;">
                <div style="background: rgba(0,0,0,0.2); border-radius: 8px; padding: 10px; text-align: center;">
                    <div style="font-size: 11px; color: #94a3b8; margin-bottom: 4px;">换手率</div>
                    <div style="font-size: 15px; font-weight: 700; color: #fbbf24;">5.42%</div>
                </div>
                <div style="background: rgba(0,0,0,0.2); border-radius: 8px; padding: 10px; text-align: center;">
                    <div style="font-size: 11px; color: #94a3b8; margin-bottom: 4px;">成交额</div>
                    <div style="font-size: 15px; font-weight: 700; color: #60a5fa;">40.87亿</div>
                </div>
                <div style="background: rgba(0,0,0,0.2); border-radius: 8px; padding: 10px; text-align: center;">
                    <div style="font-size: 11px; color: #94a3b8; margin-bottom: 4px;">H1营收增速</div>
                    <div style="font-size: 15px; font-weight: 700; color: #34d399;">+17.24%</div>
                </div>
                <div style="background: rgba(0,0,0,0.2); border-radius: 8px; padding: 10px; text-align: center;">
                    <div style="font-size: 11px; color: #94a3b8; margin-bottom: 4px;">动态PE</div>
                    <div style="font-size: 15px; font-weight: 700; color: #fbbf24;">228.9倍</div>
                </div>
            </div>
            <div style="font-size: 13px; color: #cbd5e1; line-height: 1.8;">
                <b>【隔夜催化影响】</b>台积电布局微通道散热技术+英伟达Vera Rubin全液冷架构+液冷概念股活跃，液冷产业趋势持续强化。新朋股份、康盛股份等密集披露液冷业务进展，板块热度回升。
                <br>✅ <b>产业逻辑</b>：液冷从\"可选项\"加速演变为\"必选项\"。TrendForce数据显示液冷在AI芯片中渗透率持续提升。中金预测2026年液冷放量元年，全球智算中心液冷市场超千亿元。
                <br>✅ <b>基本面</b>：上半年营收30.17亿（+17.24%），Q2净利环比大增1934%，业绩拐点显现。
                <br>⚠️ <b>估值风险</b>：动态PE 228.9倍，估值极高，需持续高增长消化。液冷板块交易热度较高，股价波动风险大。
                <br>🎯 <b>操作建议</b>：<b>持有观察，不追高</b>。放量站稳67元上方可小仓位跟进；若持续在66元附近缩量震荡则观望。上方压力位70元（前期平台），下方支撑60元。
                <br><span style="color: #94a3b8; font-size: 11px;">【双重验证说明】仍深度破止损状态，产业逻辑回暖但技术面未确认企稳。单一液冷板块热度回升不足以作为加仓依据，需量价配合确认。</span>
            </div>
        </div>
    </div>

    <!-- *ST建艺 -->
    <div style="border-left: 4px solid #7c3aed; border-radius: 0 12px 12px 0;">
        <div style="background: rgba(255,255,255,0.04); border-radius: 0 12px 12px 0; padding: 16px 20px; backdrop-filter: blur(10px); border: 1px solid rgba(255,255,255,0.06); border-left: none;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
                <div>
                    <span style="font-size: 18px; font-weight: 700; color: #f1f5f9;">*ST建艺 (002789)</span>
                    <span style="margin-left: 12px; padding: 3px 10px; background: linear-gradient(135deg, #7c3aed, #6d28d9); color: white; border-radius: 20px; font-size: 12px; font-weight: 700;">退市风险</span>
                </div>
                <span style="font-size: 22px; font-weight: 800; color: #c084fc;">—</span>
            </div>
            <div style="font-size: 13px; color: #cbd5e1; line-height: 1.8;">
                ⚠️ <b>退市风险股，最高优先级清仓</b>。退市风险+债务问题未消除，任何价格立即离场，绝不恋战。
            </div>
        </div>
    </div>
</div>
"""

gen._components.append(Section(title="💼 持仓股分析", content=portfolio_html, icon="briefcase"))

# ============================================================
# 6. 催化深度分析（Skill增强）
# ============================================================
events = [
    {
        "title": "博通AI半导体收入暴增221%",
        "type": "data",
        "description": "博通Q3 AI半导体收入167亿美元超预期，上调2026-2028年AI收入指引从580亿到2300亿美元，两年翻倍再翻倍",
        "category": "AI算力",
    },
    {
        "title": "英伟达35亿美元投资联发科",
        "type": "policy",
        "description": "英伟达35亿认购联发科可转债，深化AI基础设施/汽车/本地AI三大领域合作，争夺机架级AI芯片入口",
        "category": "AI芯片",
    },
    {
        "title": "韩国半导体出口管制落地",
        "type": "policy",
        "description": "韩国9月1日起对高性能AI芯片和先进半导体设备实施出口管制，国产替代逻辑强化",
        "category": "国产替代",
    },
]

gen.add_catalyst_deep_analysis(events)

# ============================================================
# 7. 投资机会分析
# ============================================================
opportunities = [
    {
        "name": "半导体设备/材料（国产替代+A50纳入）",
        "priority": "高",
        "logic": "日韩双重管制落地+富时A50纳入中微/生益，半导体设备和材料国产替代进入加速期。设备龙头中报业绩验证景气度（中微净利增282%-311%）。CSEAC 2026展会显示三季度订单景气度持续提升。3D NAND架构升级、HBM及先进封装持续打开设备新品类及价值量空间。",
        "stocks": [
            {"code": "688012", "name": "中微公司", "impact": "A50纳入+刻蚀龙头"},
            {"code": "002371", "name": "北方华创", "impact": "平台型龙头"},
            {"code": "002409", "name": "雅克科技", "impact": "HBM前驱体"},
        ]
    },
    {
        "name": "AI算力上游（PCB铜箔+液冷）",
        "priority": "高",
        "logic": "博通AI半导体收入+221%+戴尔上调全年AI服务器收入至740亿，AI算力需求持续超预期。铜冠铜箔HVLP全系列完成客户布局，液冷从可选项变必选项。短期板块调整后性价比提升。",
        "stocks": [
            {"code": "301217", "name": "铜冠铜箔", "impact": "HVLP铜箔龙头"},
            {"code": "002837", "name": "英维克", "impact": "液冷龙头"},
            {"code": "600183", "name": "生益科技", "impact": "A50纳入+CCL"},
        ]
    },
    {
        "name": "先进封装/存储（HBM+Chiplet）",
        "priority": "中",
        "logic": "台积电CoWoS产能持续紧缺，2029年扩至14倍光罩尺寸。三星HBM产能70%锁定至2031年，现货价是长约价4-5倍。存储涨价周期延续，高盛维持买入评级。",
        "stocks": [
            {"code": "002156", "name": "通富微电", "impact": "封测龙头"},
            {"code": "301308", "name": "江波龙", "impact": "存储龙头"},
            {"code": "688525", "name": "佰维存储", "impact": "HBM+存储模组"},
        ]
    },
    {
        "name": "军工/防务科技（避险+地缘催化）",
        "priority": "中",
        "logic": "中东地缘冲突升级+建军百年节点临近，军工板块逆势走强。内蒙一机2连板，军贸、军用材料、航空发动机等细分环节持续催化。在科技股调整期，军工可作为避险配置方向。",
        "stocks": [
            {"code": "600967", "name": "内蒙一机", "impact": "军贸+2连板"},
            {"code": "601698", "name": "中国卫通", "impact": "卫星互联网"},
        ]
    },
]

gen.add_investment_opportunities(opportunities, view_mode="tab")

# ============================================================
# 8. 风险提示
# ============================================================
risks = [
    "亚太股市暴跌（韩股-3.99%、日股-2.85%）或对A股科技股形成情绪冲击，低开概率较大",
    "博通Q4营收指引348亿美元略低于市场预期350.5亿美元，盘后一度跌6%",
    "半导体板块9月2日主力净流出超113亿元，短期获利盘仍有兑现压力",
    "铜冠铜箔动态PE超200倍，估值处于极高区间，需警惕估值回调风险",
    "英维克动态PE 228.9倍+深度破止损状态，技术面未确认企稳前不建议加仓",
    "美联储政策不确定性仍存，若通胀未降温可能引发加息预期升温",
]
gen.add_risk_warning(risks)

# ============================================================
# 9. 投资策略建议
# ============================================================
strategy = """
<b>【整体判断】</b>隔夜外盘整体偏暖（美股终结三连跌+博通AI收入暴增），但亚太股市大跌+A50期货跌1.23%，今日A股开盘承压概率较大。产业层面AI算力需求持续超预期（博通指引2028年AI半导体收入2300亿美元），国产替代逻辑强化（韩国管制落地），但短期板块调整尚未结束，需等待企稳信号。

<b>【仓位建议】</b>整体仓位控制在4-5成，以雅克科技为核心底仓（HBM前驱体+长鑫双主线），铜冠铜箔和英维克控制仓位参与反弹。不追高，等待明确企稳信号再加仓。

<b>【今日操作策略】</b>
1️⃣ <b>开盘观察期（前30分钟）</b>：关注科技板块开盘跌幅是否收窄、量能是否异常放大。若低开后快速企稳（不破昨日低点），可小仓位试探；若低开低走放量，则继续观望。

2️⃣ <b>分标的操作</b>：
· <b>雅克科技</b>：底仓持有。低开至125-128企稳可小加做T，跌破120减仓。压力位140元。
· <b>铜冠铜箔</b>：底仓持有观察。107元（昨日低点）是关键支撑，企稳可逢低布局，有效跌破则减仓。
· <b>英维克</b>：深度破止损状态，反弹减仓为主。放量站稳67元以上可小仓跟进，否则观望。
· <b>*ST建艺</b>：立即清仓（最高优先级）。

3️⃣ <b>关注方向</b>：半导体设备/材料（国产替代+A50纳入）、军工（避险+地缘）、AI算力上游（PCB铜箔+液冷）。

4️⃣ <b>今日重点数据/事件</b>：
· 中国8月财新服务业PMI（09:45）
· 美国8月ADP就业数据（今晚）
· 美联储官员讲话
· 博通财报后续影响发酵

<b>【中期观点】</b>AI算力产业趋势未变（博通指引验证），国产替代加速（日韩管制），半导体板块中期逻辑依然坚实。短期调整是上涨过程中的正常消化，等待缩量止跌信号出现后可逐步加仓。
"""

gen.add_investment_strategy(strategy)

# ============================================================
# 发布
# ============================================================
print("开始生成S级催化盘前扫描报告...")
result = gen.publish(
    title="博通AI暴增+英伟达投联发科+亚太深震",
    report_type="s_level_catalyst",
    filename="20260903_盘前_S级催化扫描_博通AI暴增221%+英伟达35亿投联发科.html",
    excerpt="隔夜美股V型反弹+博通AI半导体收入暴增221%+英伟达35亿投联发科+韩国管制落地+亚太股市大跌",
    auto_deploy=True,
    docs_root="docs"
)
print(f"发布结果: {result}")

# 验证
errors = gen.validate()
if errors:
    print(f"验证发现问题: {errors}")
else:
    print("✅ 验证通过，无问题")

