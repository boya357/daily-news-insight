import sys, os
sys.path.insert(0, '/root/daily-news-insight')
sys.path.insert(0, '/root/daily-news-insight/v3')
os.chdir('/root/daily-news-insight')

from v3.generators.s_level_catalyst import SLevelCatalystGenerator
from components.layout import Section

gen = SLevelCatalystGenerator(
    date_str="20260909",
    catalyst_title="北京双规划+存储历史性短缺",
    subtitle="2026.09.09 · 盘后S级催化"
)

# 1. Catalyst overview
gen.add_catalyst_overview(
    "盘后双重S级催化落地：<strong>①北京\"十五五\"高精尖产业+数字经济双规划重磅发布</strong>，"
    "明确2030年高精尖产业占GDP40%、数字经济占比超50%，重点布局AI全栈自主、十万卡算力集群、"
    "RISC-V/Chiplet/先进封装、商业航天等方向，京津冀\"银河算廊\"工程首次披露；"
    "<strong>②存储芯片历史性短缺加剧</strong>——KB证券最新报告显示三星+SK海力士存储库存已降至不足10天，"
    "2027年或出现\"无货可卖\"极端局面，HBM4挤占传统DRAM产能形成\"挤出效应\"，存储涨价周期确定性进一步强化。"
    "隔夜费城半导体逆势涨1.3%，英特尔暴涨9%、AMD涨6%、SK海力士涨3.5%，外盘半导体强势映射。"
)

# 2. Catalyst details
gen.add_catalyst_details(
    background=(
        "\"十五五\"开局之年政策密集落地。9月9日北京市人民政府同日印发《高精尖产业发展规划》和"
        "《数字经济发展规划》两份重磅文件，构建\"2261\"高精尖产业结构：新一代信息技术+医药健康两大万亿级优势引领产业，"
        "人工智能+机器人和智能制造两大新兴支柱产业，绿色低碳等6个能级跃升产业，以及商业航天等未来产业成长方阵。"
        "与此同时，全球存储行业供需矛盾持续激化——AI资本开支爆发推动HBM需求暴增，HBM4单颗晶圆消耗量是传统DRAM的3倍，"
        "先进产能严重挤占传统DRAM/NAND供给，存储行业从\"补库存周期\"转向\"AI驱动的历史性短缺新周期\"。"
    ),
    trigger=(
        "【政策端】北京双规划同日发布，明确：十万卡算力集群+京津冀\"银河算廊\"工程；RISC-V/Chiplet/先进封装/EDA全链条突破；"
        "词元工厂+智能体经济新形态；2030年数字经济占GDP超50%。\n"
        "【产业端】KB证券预警：三星+SK海力士存储库存不足10天，2027年DRAM/NAND需求增速比供给高10个百分点以上；"
        "TrendForce预计2027年存储占云厂资本开支68%。\n"
        "【资金端】隔夜费半逆势涨1.3%与大盘分化（道指跌1.18%），英特尔+9%、AMD+6%、SK海力士+3.5%，"
        "产业资金与宏观资金\"各走各的路\"，半导体产业逻辑独立行情验证。\n"
        "【公司端】雅克科技盘后披露机构调研：中韩双基地扩产明年年底前建成，钼前驱体在300层以上NAND应用前景广阔；"
        "深科技子公司18.5亿扩高端存储封测产能。"
    )
)

# 3. Overnight market
overnight_html = """
<div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 12px; margin-bottom: 16px;">
    <div style="background: linear-gradient(135deg, rgba(16,185,129,0.15) 0%, rgba(5,150,105,0.08) 100%); border-radius: 12px; padding: 16px; border: 1px solid rgba(16,185,129,0.25); text-align: center;">
        <div style="font-size: 12px; color: #6ee7b7; margin-bottom: 6px;">费城半导体</div>
        <div style="font-size: 22px; font-weight: 800; color: #34d399;">+1.30%</div>
        <div style="font-size: 11px; color: #6ee7b7; margin-top: 4px;">逆势走强</div>
    </div>
    <div style="background: linear-gradient(135deg, rgba(239,68,68,0.12) 0%, rgba(185,28,28,0.06) 100%); border-radius: 12px; padding: 16px; border: 1px solid rgba(239,68,68,0.25); text-align: center;">
        <div style="font-size: 12px; color: #fca5a5; margin-bottom: 6px;">纳斯达克</div>
        <div style="font-size: 22px; font-weight: 800; color: #f87171;">-0.32%</div>
        <div style="font-size: 11px; color: #fca5a5; margin-top: 4px;">大盘承压</div>
    </div>
    <div style="background: linear-gradient(135deg, rgba(245,158,11,0.15) 0%, rgba(217,119,6,0.08) 100%); border-radius: 12px; padding: 16px; border: 1px solid rgba(245,158,11,0.25); text-align: center;">
        <div style="font-size: 12px; color: #fcd34d; margin-bottom: 6px;">英特尔</div>
        <div style="font-size: 22px; font-weight: 800; color: #fbbf24;">+9.05%</div>
        <div style="font-size: 11px; color: #fcd34d; margin-top: 4px;">CPU涨价预期</div>
    </div>
    <div style="background: linear-gradient(135deg, rgba(168,85,247,0.15) 0%, rgba(126,34,206,0.08) 100%); border-radius: 12px; padding: 16px; border: 1px solid rgba(168,85,247,0.25); text-align: center;">
        <div style="font-size: 12px; color: #d8b4fe; margin-bottom: 6px;">SK海力士</div>
        <div style="font-size: 22px; font-weight: 800; color: #c084fc;">+3.51%</div>
        <div style="font-size: 11px; color: #d8b4fe; margin-top: 4px;">存储短缺受益</div>
    </div>
</div>
<div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 14px;">
    <div style="background: rgba(255,255,255,0.04); border-radius: 12px; padding: 16px; border: 1px solid rgba(255,255,255,0.08);">
        <div style="font-size: 14px; font-weight: 700; color: #f1f5f9; margin-bottom: 10px;">全球半导体表现</div>
        <div style="display: flex; flex-direction: column; gap: 8px;">
            <div style="display: flex; justify-content: space-between;"><span style="font-size: 13px; color: #94a3b8;">台积电ADR</span><span style="font-size: 13px; font-weight: 600; color: #34d399;">+2.35%</span></div>
            <div style="display: flex; justify-content: space-between;"><span style="font-size: 13px; color: #94a3b8;">美光科技</span><span style="font-size: 13px; font-weight: 600; color: #34d399;">+2.91%</span></div>
            <div style="display: flex; justify-content: space-between;"><span style="font-size: 13px; color: #94a3b8;">博通</span><span style="font-size: 13px; font-weight: 600; color: #34d399;">+2.80%</span></div>
            <div style="display: flex; justify-content: space-between;"><span style="font-size: 13px; color: #94a3b8;">高通</span><span style="font-size: 13px; font-weight: 600; color: #34d399;">+3.20%</span></div>
            <div style="display: flex; justify-content: space-between;"><span style="font-size: 13px; color: #94a3b8;">英伟达</span><span style="font-size: 13px; font-weight: 600; color: #f87171;">-2.10%</span></div>
            <div style="display: flex; justify-content: space-between;"><span style="font-size: 13px; color: #94a3b8;">三星电子</span><span style="font-size: 13px; font-weight: 600; color: #94a3b8;">持平</span></div>
        </div>
    </div>
    <div style="background: rgba(255,255,255,0.04); border-radius: 12px; padding: 16px; border: 1px solid rgba(255,255,255,0.08);">
        <div style="font-size: 14px; font-weight: 700; color: #f1f5f9; margin-bottom: 10px;">外盘关键消息</div>
        <div style="display: flex; flex-direction: column; gap: 10px;">
            <div style="font-size: 12px; color: #cbd5e1; line-height: 1.6;"><span style="color: #f59e0b; font-weight: 600;">英特尔暴涨9%</span> 传PC CPU可能涨价，市场重新定价PC需求复苏预期，市值一夜增加2900亿元</div>
            <div style="font-size: 12px; color: #cbd5e1; line-height: 1.6;"><span style="color: #f59e0b; font-weight: 600;">高通+亚马逊合作</span> 联合开发AI数据中心芯片与1.6T光互连方案，AI芯片版图再添新玩家</div>
            <div style="font-size: 12px; color: #cbd5e1; line-height: 1.6;"><span style="color: #f59e0b; font-weight: 600;">三星4nm半数给HBM4</span> 存储与逻辑代工争抢先进制程，高通/AMD等客户产能或受挤压</div>
            <div style="font-size: 12px; color: #cbd5e1; line-height: 1.6;"><span style="color: #f59e0b; font-weight: 600;">油价破100美元</span> 布油+3%逼近101美元，美伊局势紧张推升通胀预期，美债承压</div>
        </div>
    </div>
</div>
"""

gen._components.append(Section(title="隔夜外盘跟踪", content=overnight_html, icon="globe"))

# 4. Industry chain
gen.add_industry_chain_analysis(
    upstream=[
        {
            "name": "半导体设备/材料",
            "desc": "存储扩产驱动设备需求，HBM堆叠层数提升增加测试设备、薄膜设备订单。存储材料如前驱体、湿化学品同步受益。",
            "stocks": [
                {"code": "002409", "name": "雅克科技", "impact": "强"},
                {"code": "688082", "name": "盛美上海", "impact": "中"},
                {"code": "603690", "name": "至纯科技", "impact": "中"},
            ]
        },
        {
            "name": "算力基础设施",
            "desc": "十万卡算力集群建设+算电协同，液冷温控、供配电、储能等配套设施需求明确。",
            "stocks": [
                {"code": "002837", "name": "英维克", "impact": "强"},
            ]
        },
        {
            "name": "AI芯片设计/RISC-V",
            "desc": "北京规划明确RISC-V智算指令集创新、存算一体芯片、Chiplet等前沿方向，国产算力新架构加速。",
            "stocks": [
                {"code": "688256", "name": "寒武纪", "impact": "中"},
            ]
        },
    ],
    midstream=[
        {
            "name": "存储芯片制造",
            "desc": "存储历史性短缺最直接受益环节。三星+SK海力士库存不足10天，HBM4涨价确定性最强，国产存储迎窗口期。",
            "stocks": [
                {"code": "603986", "name": "兆易创新", "impact": "强"},
                {"code": "688525", "name": "佰维存储", "impact": "强"},
            ]
        },
        {
            "name": "先进封装/HBM",
            "desc": "HBM4 8-Hi/12-Hi堆叠推动先进封装需求爆发，2.5D/3D封装、TSV、微凸块技术量价齐升。",
            "stocks": [
                {"code": "002156", "name": "通富微电", "impact": "强"},
                {"code": "600584", "name": "长电科技", "impact": "中"},
            ]
        },
        {
            "name": "铜箔/PCB（AI算力配套）",
            "desc": "AI服务器PCB和铜箔需求随算力扩张同步增长，高端高频高速材料紧缺。",
            "stocks": [
                {"code": "301217", "name": "铜冠铜箔", "impact": "中"},
            ]
        },
    ],
    downstream=[
        {
            "name": "AI服务器/智算中心",
            "desc": "北京银河算廊工程+十万卡集群，智算中心建设加速。AI推理向智能体应用转变，算力需求持续扩张。",
            "stocks": [
                {"code": "000977", "name": "浪潮信息", "impact": "强"},
                {"code": "603019", "name": "中科曙光", "impact": "强"},
            ]
        },
        {
            "name": "光通信/光模块",
            "desc": "高通+亚马逊联合研发1.6T光互连，光模块需求从800G向1.6T升级加速。昨夜美股光通信板块大涨。",
            "stocks": [
                {"code": "300308", "name": "中际旭创", "impact": "强"},
            ]
        },
        {
            "name": "商业航天/空天技术",
            "desc": "北京规划首次将商业航天列为重点产业，可重复使用火箭、大推力发动机、商业星座建设。",
            "stocks": [
                {"code": "600118", "name": "中国卫星", "impact": "中"},
            ]
        },
    ]
)

# 5. Investment opportunities
gen.add_investment_opportunities([
    {
        "name": "存储产业链（最高优先级）",
        "priority": "高",
        "logic": "三星+SK海力士库存不足10天，KB证券警告2027年或无货可卖。存储行业从补库存周期转向AI驱动的历史性短缺新周期，涨价确定性极强。HBM4产能挤出效应+AI服务器DDR5/企业级SSD需求爆发形成供需闭环。重点关注存储芯片设计、设备材料、先进封装三个方向。",
        "stocks": [
            {"code": "002409", "name": "雅克科技", "impact": "持仓强"},
            {"code": "603986", "name": "兆易创新", "impact": "强"},
            {"code": "688525", "name": "佰维存储", "impact": "强"},
        ]
    },
    {
        "name": "北京算力+液冷温控",
        "priority": "高",
        "logic": "北京十五五规划明确十万卡算力集群建设+京津冀银河算廊工程，算电协同绿色转型。新建智算中心100%用绿电，800V高压直流供电架构探索。液冷作为高密度算力的刚需解决方案，政策+需求双轮驱动。英维克作为液冷龙头直接受益。",
        "stocks": [
            {"code": "002837", "name": "英维克", "impact": "持仓强"},
        ]
    },
    {
        "name": "先进封装/Chiplet",
        "priority": "中",
        "logic": "北京规划明确发展先进封装技术和芯粒（Chiplet），系统打造全栈交付体系。HBM堆叠层数提升（8-Hi/12-Hi）+3D封装加速渗透，先进封装量价齐升。深科技18.5亿扩存储封测产能验证行业景气。",
        "stocks": [
            {"code": "002156", "name": "通富微电", "impact": "强"},
            {"code": "600584", "name": "长电科技", "impact": "中"},
        ]
    },
    {
        "name": "铜箔/PCB（AI算力传导）",
        "priority": "中",
        "logic": "AI服务器算力扩张传导至PCB/铜箔环节，高端高频高速材料紧缺。铜冠铜箔布局锂电+电子铜箔双赛道，AI算力需求提升电子铜箔高端化需求。需关注下游需求传导节奏。",
        "stocks": [
            {"code": "301217", "name": "铜冠铜箔", "impact": "持仓中"},
        ]
    },
    {
        "name": "商业航天/低空经济",
        "priority": "低",
        "logic": "北京规划首次将商业航天列为重点发展方向，可重复使用火箭、大推力发动机、商业星座建设。题材属性较强，业绩兑现需时，适合风险偏好高的投资者短线关注。",
        "stocks": [
            {"code": "600118", "name": "中国卫星", "impact": "中"},
        ]
    },
], view_mode="tab")

# 6. Deep analysis
gen.add_catalyst_deep_analysis([
    {
        "title": "存储历史性短缺",
        "type": "industry",
        "description": "三星+SK海力士库存不足10天，HBM4挤占产能，2027年或出现极端供需缺口",
        "category": "semiconductor"
    },
    {
        "title": "北京双规划政策催化",
        "type": "policy",
        "description": "十五五高精尖+数字经济双规划，AI/芯片/算力全链条政策支持",
        "category": "policy"
    },
    {
        "title": "外盘半导体逆势走强",
        "type": "data",
        "description": "费半+1.3%与大盘分化，产业逻辑独立行情验证",
        "category": "market"
    },
])

# 7. Portfolio impact
portfolio_html = """
<div style="display: flex; flex-direction: column; gap: 12px;">
    <div style="background: linear-gradient(135deg, rgba(16,185,129,0.10) 0%, rgba(5,150,105,0.05) 100%); border-radius: 12px; padding: 16px; border: 1px solid rgba(16,185,129,0.25);">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
            <div style="display: flex; align-items: center; gap: 8px;">
                <span style="font-size: 18px;">🧪</span>
                <span style="font-size: 15px; font-weight: 700; color: #f1f5f9;">雅克科技（002409）</span>
                <span style="padding: 3px 8px; border-radius: 12px; font-size: 11px; font-weight: 600; background: rgba(16,185,129,0.2); color: #6ee7b7;">利好</span>
            </div>
            <span style="font-size: 13px; font-weight: 700; color: #fbbf24;">★★★★★ 强受益</span>
        </div>
        <div style="font-size: 13px; color: #cbd5e1; line-height: 1.7;">
            <strong>催化逻辑：</strong>存储历史性短缺最直接受益标的。公司半导体材料（前驱体+湿化学品）深度绑定存储晶圆厂客户，中韩双基地扩产明年年底前建成，匹配客户未来3-5年产能翻倍计划。<br>
            <strong>新增亮点：</strong>钼前驱体在300层以上NAND应用前景广阔，将带来多元新业务机会。9月8日接待泰康资产等3家机构调研，机构关注度持续提升。<br>
            <strong>双重验证：</strong>①公司官方公告确认扩产计划（来源：深交所公告）；②KB证券/TrendForce/Counterpoint三方独立研报验证存储短缺逻辑；③雅克科技半年度营收45.13亿+净利润5.61亿，业绩已开始兑现。
        </div>
    </div>
    <div style="background: linear-gradient(135deg, rgba(59,130,246,0.10) 0%, rgba(37,99,235,0.05) 100%); border-radius: 12px; padding: 16px; border: 1px solid rgba(59,130,246,0.25);">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
            <div style="display: flex; align-items: center; gap: 8px;">
                <span style="font-size: 18px;">❄️</span>
                <span style="font-size: 15px; font-weight: 700; color: #f1f5f9;">英维克（002837）</span>
                <span style="padding: 3px 8px; border-radius: 12px; font-size: 11px; font-weight: 600; background: rgba(59,130,246,0.2); color: #93c5fd;">偏利好</span>
            </div>
            <span style="font-size: 13px; font-weight: 700; color: #fbbf24;">★★★★ 中度受益</span>
        </div>
        <div style="font-size: 13px; color: #cbd5e1; line-height: 1.7;">
            <strong>催化逻辑：</strong>北京十五五规划十万卡算力集群+京津冀银河算廊工程，液冷温控作为高密度算力刚需直接受益。规划明确新建智算中心100%使用绿电、探索800V高压直流供电，间接利好温控方案升级。<br>
            <strong>短期压力：</strong>今日半导体板块整体回调（-1.35%），液冷板块随科技成长承压。当前股价63元，距前期高点回调超30%，需警惕短期情绪面压力。<br>
            <strong>双重验证：</strong>①北京政府官网发布《高精尖产业发展规划》和《数字经济发展规划》（来源：北京市人民政府）；②中报营收30.17亿+17.24%增长，机房温控产品收入占比过半（来源：公司半年报）。
        </div>
    </div>
    <div style="background: linear-gradient(135deg, rgba(245,158,11,0.10) 0%, rgba(217,119,6,0.05) 100%); border-radius: 12px; padding: 16px; border: 1px solid rgba(245,158,11,0.25);">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
            <div style="display: flex; align-items: center; gap: 8px;">
                <span style="font-size: 18px;">🔩</span>
                <span style="font-size: 15px; font-weight: 700; color: #f1f5f9;">铜冠铜箔（301217）</span>
                <span style="padding: 3px 8px; border-radius: 12px; font-size: 11px; font-weight: 600; background: rgba(245,158,11,0.2); color: #fcd34d;">中性偏多</span>
            </div>
            <span style="font-size: 13px; font-weight: 700; color: #fbbf24;">★★★ 间接受益</span>
        </div>
        <div style="font-size: 13px; color: #cbd5e1; line-height: 1.7;">
            <strong>催化逻辑：</strong>AI算力扩张传导至PCB/铜箔环节，高端电子铜箔需求有望随AI服务器和高速PCB增长。但公司当前锂电铜箔占比较高，电子铜箔占比提升需要时间。<br>
            <strong>关注重点：</strong>电子铜箔产能释放进度与高端产品认证进展；锂电铜箔价格走势对盈利的影响。<br>
            <strong>双重验证：</strong>①铜冠铜箔半年度报告已披露（来源：深交所）；②AI服务器PCB需求增长逻辑获多家机构研报验证（中信建投/国盛证券）。
        </div>
    </div>
    <div style="background: linear-gradient(135deg, rgba(107,114,128,0.10) 0%, rgba(75,85,99,0.05) 100%); border-radius: 12px; padding: 16px; border: 1px solid rgba(107,114,128,0.25);">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
            <div style="display: flex; align-items: center; gap: 8px;">
                <span style="font-size: 18px;">🏗️</span>
                <span style="font-size: 15px; font-weight: 700; color: #f1f5f9;">*ST建艺（002789）</span>
                <span style="padding: 3px 8px; border-radius: 12px; font-size: 11px; font-weight: 600; background: rgba(107,114,128,0.2); color: #9ca3af;">中性</span>
            </div>
            <span style="font-size: 13px; font-weight: 700; color: #9ca3af;">★ 影响有限</span>
        </div>
        <div style="font-size: 13px; color: #cbd5e1; line-height: 1.7;">
            <strong>催化评估：</strong>北京规划主要聚焦高精尖产业和数字经济，对建筑装饰行业直接影响有限。公司核心逻辑仍在于摘帽预期和主业恢复，与今日S级催化关联度较低。继续作为组合防御端配置观察。
        </div>
    </div>
</div>
"""

gen._components.append(Section(title="持仓股影响评估", content=portfolio_html, icon="pie-chart", variant="highlight"))

# 8. Risk warnings
gen.add_risk_warning([
    "宏观风险：油价突破100美元推升通胀预期，美债收益率上行可能压制成长股估值，大盘系统性回调风险",
    "短期情绪风险：半导体板块连续回调，主力资金净流出超65亿元，短期获利回吐压力仍在，注意节奏控制",
    "政策落地节奏风险：北京规划为十五五五年期规划，具体项目落地和资金到位需要时间，不宜过度透支预期",
    "技术面风险：半导体板块处于三角形震荡下沿，若跌破关键支撑可能触发技术性抛压，需设好止损",
    "持仓股风险：雅克科技需验证存储扩产对业绩的实际拉动；英维克短期股价超跌但情绪面仍弱，不宜急抄底"
])

# 9. Investment strategy
gen.add_investment_strategy(
    "<strong>整体策略：</strong>今日盘后双重S级催化（北京政策+存储短缺）对科技成长板块构成中期利好，"
    "但短期需警惕大盘承压和板块情绪偏弱的冲击。建议采取中期布局、短期控制节奏的策略，仓位控制在5成以下。"
    "<br><br><strong>核心方向排序：</strong>存储产业链 ＞ 液冷温控 ＞ 先进封装 ＞ 光通信 ＞ 铜箔/PCB"
    "<br><br><strong>持仓操作建议：</strong>"
    "<br>• <strong>雅克科技</strong>：存储短缺逻辑再度强化，中韩双基地扩产验证景气度，建议持有底仓+逢回调加仓策略，"
    "核心支撑位参考60日均线（约78-82元区间），PE历史分位约35%，估值尚合理"
    "<br>• <strong>英维克</strong>：北京算力政策利好中期逻辑，但短期股价超跌+情绪面偏弱，"
    "建议耐心等待企稳信号（放量阳线+站稳60元）再考虑加仓，技术支撑位58-60元，止损位55元"
    "<br>• <strong>铜冠铜箔</strong>：存储/算力传导逻辑偏间接，继续持有观察电子铜箔业务进展，支撑位参考前期低点"
    "<br>• <strong>*ST建艺</strong>：与催化关联度低，继续作为防御端持有，关注摘帽进展"
    "<br><br><strong>明日关注：</strong>"
    "<br>① 半导体板块是否在外盘利好下高开，以及高开后量能能否支撑（重点看成交额能否放大至2000亿以上）"
    "<br>② 存储板块龙头（兆易创新/佰维存储）能否领涨，验证资金认可度"
    "<br>③ 沪指3950点支撑有效性，若跌破需降低仓位"
    "<br><br><strong>数据来源：</strong>北京市人民政府官网、KB证券、TrendForce、Counterpoint、东方财富Choice、财联社、证券时报"
)

# Publish
result = gen.publish(
    title="北京双规划+存储历史性短缺",
    report_type="s_level_catalyst",
    filename="20260909_盘后_S级催化扫描_北京双规划+存储历史性短缺.html",
    excerpt="盘后双重S级催化：北京十五五高精尖+数字经济双规划重磅发布，十万卡算力集群+银河算廊工程首次披露；存储历史性短缺加剧，三星SK海力士库存不足10天。隔夜费半逆势涨1.3%。"
)

print(f"发布结果: {result}")
