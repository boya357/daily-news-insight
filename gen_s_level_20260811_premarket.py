#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S级催化扫描 - 2026年8月11日 盘前
美股半导体重挫+油价暴涨+英伟达5000亿AI融资+韩国半导体特别法实施
"""
import sys, os
sys.path.insert(0, '/root/daily-news-insight/v3')
os.chdir('/root/daily-news-insight')

from v3.generators.s_level_catalyst import SLevelCatalystGenerator

gen = SLevelCatalystGenerator(
    date_str="20260811",
    catalyst_title="美股半导体重挫+油价暴涨5%+英伟达5000亿AI融资 科技板块承压分化",
    subtitle="2026.08.11 · 盘前S级催化"
)

# ========== 1. 催化概述 ==========
gen.add_catalyst_overview(
    overview=(
        "隔夜全球市场再现剧烈波动：美股费城半导体指数暴跌2.94%全线收绿，英伟达-2.86%、应用材料-3.15%、"
        "英特尔-4.06%；WTI原油暴涨5.1%报82.13美元/桶，霍尔木兹海峡局势再度紧张。英伟达联合六家华尔街巨头"
        "设立5000亿美元AI基础设施基金，引发'循环融资'模式质疑。国内方面，央行印发《'十五五'改革发展规划》，"
        "重点打造科技金融体系支持硬科技创新；韩国《半导体特别法》今日正式实施，非首都圈半导体集群基建补贴50-100%。"
        "三星HBM4良率突破80%黄金关口，SK海力士深陷劳资对峙HBM4扩产存变数。"
        "整体判断：外部情绪承压+内部政策托底，A股科技板块或呈现低开高走分化格局，聚焦半导体设备/材料国产替代主线。"
    ),
    importance="高"
)

# ========== 2. 催化详情 ==========
gen.add_catalyst_details(
    background=(
        "8月以来全球科技股经历剧烈震荡，7月费城半导体指数暴跌21%后，8月初迎来超跌反弹。"
        "霍尔木兹海峡局势反复成为油价与通胀预期的核心变量。AI产业链'循环融资'模式（英伟达联合金融机构为客户融资采购芯片）"
        "的可持续性遭遇市场质疑，叠加半导体板块前期反弹幅度较大，获利回吐压力显现。"
        "国内政策面持续释放稳市场信号，央行'十五五'规划明确科技金融为头号重点，大基金三期加速落地。"
    ),
    trigger=(
        "① 费城半导体指数暴跌2.94%报11994点，30只成份股全线走低，Arm-5%+、英特尔-4%+、高通/应用材料-3%+；<br>"
        "② 英伟达联合Apollo/黑石/贝莱德GIP/Brookfield/高盛/KKR六巨头，设立5000亿美元AI基础设施基金，'循环融资'模式遭质疑；<br>"
        "③ WTI原油暴涨5.1%报82.13美元，霍尔木兹海峡通行量降至每日6艘，特朗普称'百分百控制'海峡；<br>"
        "④ 克利夫兰联储主席：美联储可能需要多次加息才能将通胀降至2%目标，加息预期重燃；<br>"
        "⑤ 韩国《半导体特别法》8月11日正式实施，非首都圈半导体集群基建费用国家承担50-100%；<br>"
        "⑥ 三星HBM4良率突破80%黄金关口，Q3 HBM4营收将环比增两倍，年底目标份额38%；SK海力士劳资对峙3500人申请组建工会；<br>"
        "⑦ 央行印发《'十五五'改革发展规划》，构建科技金融体系，扩容科创再贷款，支持硬科技企业融资；<br>"
        "⑧ 微软自研Maia 300 AI芯片秋季发布，正与台积电洽谈2027年30万枚产能，较英伟达芯片成本低30-40%；<br>"
        "⑨ 英特尔发行150亿美元股票融资，支撑芯片代工业务扩张，股价盘中跌超5%；<br>"
        "⑩ SK海力士批准54万亿韩元（384亿美元）扩产计划，清州M17+龙仁Y2厂，HBM/下一代DRAM扩产加速。"
    )
)

# ========== 3. 隔夜外盘扫描模块 ==========
overnight_html = """
<div class="grid grid-cols-2 md:grid-cols-4 gap-3 mb-4">
    <div style="background: linear-gradient(135deg, rgba(239,68,68,0.15) 0%, rgba(220,38,38,0.08) 100%); 
                border-radius: 12px; padding: 16px; border: 1px solid rgba(239,68,68,0.3);">
        <div style="font-size: 12px; color: #fca5a5; margin-bottom: 6px;">费城半导体SOX</div>
        <div style="font-size: 22px; font-weight: 800; color: #f87171;">-2.94%</div>
        <div style="font-size: 11px; color: #fca5a5; margin-top: 4px;">报11994点 全线收绿</div>
    </div>
    <div style="background: linear-gradient(135deg, rgba(239,68,68,0.15) 0%, rgba(220,38,38,0.08) 100%); 
                border-radius: 12px; padding: 16px; border: 1px solid rgba(239,68,68,0.3);">
        <div style="font-size: 12px; color: #fca5a5; margin-bottom: 6px;">纳斯达克</div>
        <div style="font-size: 22px; font-weight: 800; color: #f87171;">-0.32%</div>
        <div style="font-size: 11px; color: #fca5a5; margin-top: 4px;">报26605点 芯片拖累</div>
    </div>
    <div style="background: linear-gradient(135deg, rgba(239,68,68,0.15) 0%, rgba(220,38,38,0.08) 100%); 
                border-radius: 12px; padding: 16px; border: 1px solid rgba(239,68,68,0.3);">
        <div style="font-size: 12px; color: #fca5a5; margin-bottom: 6px;">道琼斯</div>
        <div style="font-size: 22px; font-weight: 800; color: #f87171;">-0.11%</div>
        <div style="font-size: 11px; color: #fca5a5; margin-top: 4px;">报53976点 小幅收跌</div>
    </div>
    <div style="background: linear-gradient(135deg, rgba(239,68,68,0.15) 0%, rgba(220,38,38,0.08) 100%); 
                border-radius: 12px; padding: 16px; border: 1px solid rgba(239,68,68,0.3);">
        <div style="font-size: 12px; color: #fca5a5; margin-bottom: 6px;">WTI原油</div>
        <div style="font-size: 22px; font-weight: 800; color: #f87171;">+5.10%</div>
        <div style="font-size: 11px; color: #fca5a5; margin-top: 4px;">报82.13美元 海峡紧张</div>
    </div>
</div>

<div class="grid grid-cols-2 md:grid-cols-4 gap-3 mb-4">
    <div style="background: rgba(239,68,68,0.08); border-radius: 10px; padding: 12px; border: 1px solid rgba(239,68,68,0.2);">
        <div style="font-size: 12px; color: #fca5a5;">英伟达 NVDA</div>
        <div style="font-size: 18px; font-weight: 700; color: #f87171;">-2.86%</div>
        <div style="font-size: 10px; color: #fca5a5;">5000亿AI基金引质疑</div>
    </div>
    <div style="background: rgba(239,68,68,0.08); border-radius: 10px; padding: 12px; border: 1px solid rgba(239,68,68,0.2);">
        <div style="font-size: 12px; color: #fca5a5;">AMD</div>
        <div style="font-size: 18px; font-weight: 700; color: #f87171;">-2.86%</div>
    </div>
    <div style="background: rgba(239,68,68,0.08); border-radius: 10px; padding: 12px; border: 1px solid rgba(239,68,68,0.2);">
        <div style="font-size: 12px; color: #fca5a5;">英特尔 INTC</div>
        <div style="font-size: 18px; font-weight: 700; color: #f87171;">-4.06%</div>
        <div style="font-size: 10px; color: #fca5a5;">150亿股票融资</div>
    </div>
    <div style="background: rgba(239,68,68,0.08); border-radius: 10px; padding: 12px; border: 1px solid rgba(239,68,68,0.2);">
        <div style="font-size: 12px; color: #fca5a5;">ARM</div>
        <div style="font-size: 18px; font-weight: 700; color: #f87171;">-5.0%+</div>
    </div>
</div>

<div class="grid grid-cols-2 md:grid-cols-4 gap-3 mb-4">
    <div style="background: rgba(239,68,68,0.08); border-radius: 10px; padding: 12px; border: 1px solid rgba(239,68,68,0.2);">
        <div style="font-size: 12px; color: #fca5a5;">应用材料 AMAT</div>
        <div style="font-size: 18px; font-weight: 700; color: #f87171;">-3.15%</div>
        <div style="font-size: 10px; color: #fca5a5;">设备龙头领跌</div>
    </div>
    <div style="background: rgba(239,68,68,0.08); border-radius: 10px; padding: 12px; border: 1px solid rgba(239,68,68,0.2);">
        <div style="font-size: 12px; color: #fca5a5;">泛林集团 LRCX</div>
        <div style="font-size: 18px; font-weight: 700; color: #f87171;">-1%+</div>
    </div>
    <div style="background: rgba(239,68,68,0.08); border-radius: 10px; padding: 12px; border: 1px solid rgba(239,68,68,0.2);">
        <div style="font-size: 12px; color: #fca5a5;">台积电 TSM</div>
        <div style="font-size: 18px; font-weight: 700; color: #f87171;">-2.5%+</div>
    </div>
    <div style="background: rgba(34,197,94,0.08); border-radius: 10px; padding: 12px; border: 1px solid rgba(34,197,94,0.2);">
        <div style="font-size: 12px; color: #86efac;">阿斯麦 ASML</div>
        <div style="font-size: 18px; font-weight: 700; color: #4ade80;">+1%+</div>
        <div style="font-size: 10px; color: #86efac;">逆势上涨</div>
    </div>
</div>

<div class="grid grid-cols-2 md:grid-cols-4 gap-3 mb-4">
    <div style="background: rgba(34,197,94,0.08); border-radius: 10px; padding: 12px; border: 1px solid rgba(34,197,94,0.2);">
        <div style="font-size: 12px; color: #86efac;">闪迪 SNDK</div>
        <div style="font-size: 18px; font-weight: 700; color: #4ade80;">+2.12%</div>
        <div style="font-size: 10px; color: #86efac;">存储逆势反弹</div>
    </div>
    <div style="background: rgba(34,197,94,0.08); border-radius: 10px; padding: 12px; border: 1px solid rgba(34,197,94,0.2);">
        <div style="font-size: 12px; color: #86efac;">西部数据 WDC</div>
        <div style="font-size: 18px; font-weight: 700; color: #4ade80;">+0.93%</div>
    </div>
    <div style="background: rgba(239,68,68,0.08); border-radius: 10px; padding: 12px; border: 1px solid rgba(239,68,68,0.2);">
        <div style="font-size: 12px; color: #fca5a5;">美光 MU</div>
        <div style="font-size: 18px; font-weight: 700; color: #f87171;">-1.89%</div>
    </div>
    <div style="background: rgba(239,68,68,0.08); border-radius: 10px; padding: 12px; border: 1px solid rgba(239,68,68,0.2);">
        <div style="font-size: 12px; color: #fca5a5;">SK海力士 ADR</div>
        <div style="font-size: 18px; font-weight: 700; color: #f87171;">-1.90%</div>
    </div>
</div>

<div class="grid grid-cols-2 md:grid-cols-4 gap-3 mb-4">
    <div style="background: rgba(34,197,94,0.08); border-radius: 10px; padding: 12px; border: 1px solid rgba(34,197,94,0.2);">
        <div style="font-size: 12px; color: #86efac;">微软 MSFT</div>
        <div style="font-size: 18px; font-weight: 700; color: #4ade80;">+1.21%</div>
        <div style="font-size: 10px; color: #86efac;">自研Maia芯片利好</div>
    </div>
    <div style="background: rgba(239,68,68,0.08); border-radius: 10px; padding: 12px; border: 1px solid rgba(239,68,68,0.2);">
        <div style="font-size: 12px; color: #fca5a5;">苹果 AAPL</div>
        <div style="font-size: 18px; font-weight: 700; color: #f87171;">-1.53%</div>
        <div style="font-size: 10px; color: #fca5a5;">Jefferies下调评级</div>
    </div>
    <div style="background: rgba(34,197,94,0.08); border-radius: 10px; padding: 12px; border: 1px solid rgba(34,197,94,0.2);">
        <div style="font-size: 12px; color: #86efac;">SpaceX</div>
        <div style="font-size: 18px; font-weight: 700; color: #4ade80;">+4%+</div>
    </div>
    <div style="background: rgba(59,130,246,0.08); border-radius: 10px; padding: 12px; border: 1px solid rgba(59,130,246,0.2);">
        <div style="font-size: 12px; color: #93c5fd;">COMEX黄金</div>
        <div style="font-size: 18px; font-weight: 700; color: #60a5fa;">+1.11%</div>
        <div style="font-size: 10px; color: #93c5fd;">报4448.6美元/盎司</div>
    </div>
</div>

<div style="background: rgba(59,130,246,0.08); border-radius: 10px; padding: 14px; border-left: 3px solid #3b82f6;">
    <div style="font-size: 13px; color: #93c5fd; font-weight: 600; margin-bottom: 6px;">📰 隔夜重要产业消息</div>
    <ul style="font-size: 12px; color: #cbd5e1; line-height: 1.9; margin: 0; padding-left: 18px;">
        <li><b>英伟达5000亿AI基金</b>：联合Apollo/黑石/贝莱德GIP/Brookfield/高盛/KKR六家金融巨头签署谅解备忘录，设立大规模资金池为AI基础设施项目融资，"循环融资"模式可持续性遭质疑（来源：券商中国/新浪财经）</li>
        <li><b>油价暴涨5%霍尔木兹紧张</b>：特朗普称"百分百控制"霍尔木兹海峡，仅放行"想放行的船只"；海峡通行量降至每日6艘；克利夫兰联储主席称可能需多次加息（来源：新华社/21世纪经济报道）</li>
        <li><b>韩国半导体特别法今日实施</b>：8月11日起正式施行，非首都圈半导体集群基建费用国家承担50-100%，优先支持地方半导体产业（来源：Infostock Daily/EBN）</li>
        <li><b>三星HBM4良率突破80%</b>：HBM4达到"黄金良率"，Q3营收环比增两倍以上，下半年占比超60%，年底目标份额38%；SK海力士劳资对峙3500人申请建工会（来源：财联社/朝鲜日报）</li>
        <li><b>央行"十五五"规划</b>：构建科技金融体系，扩容科创再贷款，支持硬科技企业融资；货币政策总量充裕+精准滴灌，结构性宽松（来源：中国人民银行/上海证券报）</li>
        <li><b>微软Maia 300芯片秋季发布</b>：与台积电洽谈2027年30万枚产能，成本较英伟达低30-40%，正与Anthropic等云客户谈判（来源：The Information/券商中国）</li>
        <li><b>英特尔150亿股票融资</b>：发行普通股募资支撑代工业务扩张，年内涨幅超163%提供定价基础（来源：券商中国）</li>
        <li><b>SK海力士384亿美元扩产</b>：董事会批准54万亿韩元扩张计划，清州M17+龙仁Y2厂，HBM/下一代DRAM扩产加速（来源：上海证券报）</li>
        <li><b>光通信板块重挫</b>：Coherent-14%、Lumentum-8%+、迈威尔科技-4.65%，光模块产业链承压（来源：新浪财经）</li>
    </ul>
</div>
"""

gen._components.append(
    type('obj', (object,), {
        'render': lambda self: f'<div class="report-section"><div class="section-header"><span class="section-icon">🌍</span><span class="section-title">隔夜全球市场扫描</span></div><div class="section-content">{overnight_html}</div></div>'
    })()
)

# ========== 4. 产业链分析 ==========
gen.add_industry_chain_analysis(
    upstream=[
        {"name": "半导体设备/零部件", "impact": "⭐⭐⭐⭐⭐", "desc": "全球存储三巨头全部宣布大额扩产（三星110万亿韩元+美光270亿美元+SK海力士384亿美元），设备投资超七成，国产设备替代加速"},
        {"name": "半导体材料/HBM材料", "impact": "⭐⭐⭐⭐⭐", "desc": "HBM供需缺口扩大+三星HBM4良率突破量产加速，前驱体、光刻胶、电子特气等上游材料量价齐升逻辑强化"},
    ],
    midstream=[
        {"name": "先进封装/HBM封装", "impact": "⭐⭐⭐⭐", "desc": "HBM扩产加速+存储三巨头资本开支大增，CoWoS、2.5D/3D封装需求持续扩张，国内封测链受益"},
        {"name": "存储芯片（结构性机会）", "impact": "⭐⭐⭐", "desc": "三星HBM4良率突破+SK海力士扩产，HBM紧缺逻辑不变但竞争加剧；关注有国产替代+长鑫产业链逻辑的标的"},
        {"name": "AI芯片设计/国产替代", "impact": "⭐⭐⭐⭐", "desc": "微软自研芯片+英伟达循环融资模式存疑，国产AI芯片替代紧迫性提升，政策+资本双重驱动"},
    ],
    downstream=[
        {"name": "光模块/CPO", "impact": "⭐⭐⭐", "desc": "隔夜光通信板块重挫（Coherent-14%），短期情绪承压，但AI算力扩张长期需求逻辑未变"},
        {"name": "AI算力基建/液冷", "impact": "⭐⭐", "desc": "油价暴涨推升通胀预期+加息担忧，压制成长股估值；液冷板块前期调整深，需等待企稳信号"},
        {"name": "高端铜箔/PCB材料", "impact": "⭐⭐⭐⭐", "desc": "AI服务器铜箔用量是传统5-10倍，HVLP高端铜箔缺口持续，叠加三星/SK海力士扩产带动封装基板需求"},
    ]
)

# ========== 5. 投资机会（StockTags组件） ==========
gen.add_investment_opportunities(
    opportunities=[
        {
            "title": "半导体设备（全球扩产+国产替代双主线）",
            "level": "S级",
            "logic": "存储三巨头全部宣布大额扩产（合计超千亿美元），设备投资占比超70%；大基金三期70%投向设备材料，国产替代加速；SEMI预测2026全球设备销售额1659亿美元创历史新高",
            "stocks": [
                {"code": "688012", "name": "中微公司", "impact": "刻蚀设备龙头"},
                {"code": "300604", "name": "长川科技", "impact": "测试设备"},
                {"code": "688082", "name": "盛美上海", "impact": "清洗/电镀设备 半年报+42%"},
                {"code": "603690", "name": "至纯科技", "impact": "湿法设备"},
            ]
        },
        {
            "title": "HBM材料/先进封装（供给缺口+扩产加速）",
            "level": "S级",
            "logic": "三星HBM4良率突破80%量产加速+SK海力士384亿美元扩产，HBM供给缺口持续扩大；上游材料/封装环节是确定性最强的受益方向",
            "stocks": [
                {"code": "002409", "name": "雅克科技", "impact": "HBM前驱体龙头+光刻胶"},
                {"code": "688525", "name": "佰维存储", "impact": "存储模组+HBM封测"},
                {"code": "600584", "name": "长电科技", "impact": "先进封装龙头"},
                {"code": "002156", "name": "通富微电", "impact": "AMD核心封测+HBM封装"},
            ]
        },
        {
            "title": "高端铜箔/PCB材料（AI服务器刚需）",
            "level": "A级",
            "logic": "AI服务器铜箔用量5-10倍于传统，HVLP高端铜箔全球缺口1500吨；全球存储扩产带动封装基板需求，国产铜箔厂商量价齐升",
            "stocks": [
                {"code": "301217", "name": "铜冠铜箔", "impact": "HBM/HBF铜箔核心供应商"},
                {"code": "600183", "name": "生益科技", "impact": "覆铜板龙头 英伟达认证"},
                {"code": "002463", "name": "沪电股份", "impact": "AI算力PCB龙头"},
            ]
        },
        {
            "title": "国产AI芯片/信创（替代紧迫性提升）",
            "level": "A级",
            "logic": "微软自研芯片+英伟达循环融资模式暴露供应链风险，国产AI芯片替代紧迫性提升；央行科技金融规划定向支持硬科技",
            "stocks": [
                {"code": "688981", "name": "中芯国际", "impact": "晶圆制造龙头"},
                {"code": "688256", "name": "寒武纪", "impact": "AI芯片设计"},
                {"code": "688047", "name": "龙芯中科", "impact": "CPU国产替代"},
            ]
        },
    ],
    view_mode="card"
)

# ========== 6. 催化深度分析 ==========
gen.add_catalyst_deep_analysis(
    events=[
        {
            "title": "半导体全球重挫：获利回吐+加息担忧，而非景气拐点",
            "type": "市场情绪",
            "description": "费城半导体指数暴跌2.94%全线收绿，主要受三重因素压制：①前期反弹后获利回吐压力；②油价暴涨5%推升通胀预期，美联储官员表态可能多次加息；③英伟达5000亿AI基金引发'循环融资'模式可持续性质疑。但产业基本面未变——三星HBM4良率突破、SK海力士384亿扩产、设备订单饱满，回调是情绪面驱动而非景气见顶",
            "category": "宏观/市场"
        },
        {
            "title": "英伟达5000亿AI基金：双刃剑效应",
            "type": "产业催化",
            "description": "英伟达联合六大金融巨头设立5000亿美元AI基础设施基金，正面意义是降低客户采购门槛、加速AI算力普及；但市场担忧形成'英伟达-金融机构-客户'的循环融资结构——客户用借来的钱买英伟达芯片，一旦AI需求不及预期可能引发连锁反应。这一模式的可持续性将持续影响AI板块估值",
            "category": "AI算力"
        },
        {
            "title": "韩国半导体特别法+三巨头扩产：设备材料确定性最强",
            "type": "产业催化",
            "description": "韩国《半导体特别法》今日实施+SK海力士384亿美元扩产+三星110万亿韩元资本开支+美光270亿美元，存储三巨头全部加码扩产。全球半导体设备市场2026年预计1659亿美元（+23.2%），2028年有望达2295亿美元。A股半导体设备/材料国产替代逻辑在全球扩产周期下确定性最强，大基金三期同步加持",
            "category": "半导体设备"
        },
        {
            "title": "三星HBM4良率80%：HBM竞争进入产能争夺战",
            "type": "产业催化",
            "description": "三星HBM4良率突破80%黄金关口，Q3营收环比增两倍，下半年占比超60%，年底目标份额38%。SK海力士HBM4良率同样进入80%区间，但深陷劳资对峙3500人申请建工会，扩产节奏存变数。HBM市场从技术比拼转向产能争夺，第四季度供货速度决定市场格局，上游材料/设备端充分受益",
            "category": "HBM/存储"
        },
        {
            "title": "央行'十五五'规划：科技金融成头号重点",
            "type": "政策催化",
            "description": "央行印发《'十五五'改革发展规划》，头号重点是构建科技金融体系——扩容科创再贷款、设立科创企业债券风险分担工具、降低科技企业融资成本。结合7月证监会再融资新政（小额快速融资上限提升+储架发行），政策合力解决半导体/AI算力行业融资痛点，硬科技产业链从题材炒作转向业绩驱动",
            "category": "政策/国内"
        },
    ]
)

# ========== 7. 风险提示 ==========
gen.add_risk_warning(
    risks=[
        "美股半导体集体重挫情绪可能向A股传导，科技板块开盘面临低开压力",
        "油价暴涨5%推升通胀预期，美联储官员表态可能多次加息，全球成长股估值承压",
        "霍尔木兹海峡局势持续紧张，油价若继续上行可能引发通胀失控担忧，触发美联储更激进加息",
        "英伟达'循环融资'模式若持续被市场质疑，AI板块整体估值可能面临调整压力",
        "光通信板块隔夜重挫（Coherent-14%），光模块概念股可能受情绪拖累低开",
        "三星HBM4良率突破可能引发'存储竞争加剧'担忧，对部分存储概念股形成压力",
        "A股连续9日成交2万亿以上但个股分化严重，赚指数不赚钱，追高风险大",
        "持仓个股需严格执行止损纪律，尤其英维克下降趋势未改，铜冠铜箔涨幅较大需锁利"
    ]
)

# ========== 8. 投资策略（含持仓建议） ==========
strategy_text = """
<b>【整体策略】外跌内稳分化加剧，利用回调布局设备/材料主线，控制仓位不追高</b><br><br>

隔夜美股半导体重挫+油价暴涨，外部情绪承压；但国内央行'十五五'科技金融规划+韩国半导体特别法实施提供产业支撑，A股大概率呈现低开高走分化格局。操作策略：<br>
① 整体仓位控制在4-5成，利用低开回调分批布局，严禁追高；<br>
② 主线聚焦半导体设备/材料（全球扩产+国产替代双逻辑）、HBM产业链、高端铜箔/PCB；<br>
③ 回避光模块短期情绪冲击、纯存储概念股竞争加剧风险；<br>
④ 严格执行持仓止损纪律，高位股逢高分批减仓锁定利润。<br><br>

<b>【持仓个股操作建议】</b><br><br>

<b>🔴 英维克（002837）：下降趋势未改，反弹继续减仓</b><br>
液冷板块虽受益于AI算力长期逻辑，但个股下降趋势完全失控，从高点回撤超67%。8月7日收55.90元超跌反弹+5.61%，但成交缩量缺乏主动买盘。隔夜美股半导体+光通信重挫，科技板块整体承压，液冷作为弱势板块反弹高度有限。<br>
<b>操作：</b>反弹至60-65元区间坚决减仓≥1/2，二次破52元无条件清仓，严禁补仓抄底。<br>
<b>估值锚：</b>当前PE（TTM）约140倍，2026年业绩增速约30%，PEG≈4.7倍严重偏高。合理估值区间35-45元（对应25-30x 2027E PE）。<br><br>

<b>🟡 铜冠铜箔（301217）：冲高减仓锁定利润，回踩再接回</b><br>
高端铜箔量价齐升逻辑不变，上半年净利同比+540%以上，HVLP全谱系量产。8月7日放量大涨+16.98%收115.81元，成交额88.37亿换手率9.57%，机构净卖2.8%<5%属正常调仓。但短期涨幅过大（从85元涨至116元涨幅36%），隔夜美股科技股回调可能对情绪造成扰动。<br>
<b>操作：</b>高开冲120元减仓至1/3底仓锁定利润，回踩100-105元接回，跌破100止盈。不建议追高加仓。<br>
<b>估值锚：</b>当前PE（2026E）约22-28x，高端铜箔涨价周期下业绩弹性大，PEG≈0.5-0.8低估。但短期涨幅较大，需警惕回调风险，持续跟踪HBM铜箔放量进度。<br><br>

<b>🟢 雅克科技（002409）：HBM前驱体龙头，全球扩产核心受益</b><br>
三星HBM4良率突破80%+SK海力士384亿美元扩产+HBM供给缺口持续扩大，雅克作为HBM前驱体全球核心供应商，中长期逻辑进一步强化。8月7日收148.78元+2.60%，主力净流出5811万（8月5日净流入4.86亿后正常回调），技术面150元附近震荡整理。<br>
<b>操作：</b>145元以上持有底仓，若回调至140-145元可适度加仓机动仓，反弹至155-160元减仓机动仓做T。站稳165元看高一线。<br>
<b>估值锚：</b>当前PE（2026E）约35-40x，HBM前驱体全球份额领先，业绩增速40%+，PEG≈1合理。HBM紧缺加剧+全球扩产背景下，目标价180-200元（2027年25-30x PE）。<br>
<b>双重验证：</b>产业逻辑（三星HBM4量产加速+SK海力士扩产+HBM供需缺口）+业绩验证（前驱体订单增长+Q2业绩预期），两个独立信号源交叉确认，持有逻辑稳固。<br><br>

<b>🚨 *ST建艺（002789）：立即清仓，退市风险敞口必须关闭</b><br>
退市风险+债务问题未消除，地量成交流动性极差，与科技主线完全无关。<b>最高优先级：无条件清仓止损</b>，绝不恋战。<br><br>

<b>【仓位建议】</b>整体仓位4-5成，核心配置半导体设备（盛美上海/中微公司）+HBM材料（雅克科技）+高端铜箔（铜冠铜箔底仓）。利用低开回调分批布局，不追高不抄底，严格执行止损纪律。关注油价走势+美联储加息预期变化+国内政策面后续落地情况。
"""

gen.add_investment_strategy(strategy_text)

# ========== 9. 发布 ==========
result = gen.publish(
    title="S级催化盘前 - 半导体重挫+油价暴涨+AI基金+半导体法",
    excerpt="美股费城半导体暴跌2.94%全线收绿，油价暴涨5%霍尔木兹紧张，英伟达5000亿AI基金引循环融资质疑，韩国半导体特别法今日实施，三星HBM4良率突破80%",
    filename="20260811_盘前_S级催化扫描_半导体重挫+油价暴涨+AI基金.html"
)

print(f"发布结果: {result}")
