#!/usr/bin/env python3
"""
20260728 盘后S级催化扫描生成脚本
事件：全球科技股共振暴跌，创业板单日跌7.35%
"""
import sys, os
sys.path.insert(0, 'v3')
os.chdir('/app/data/所有对话/主对话')

from v3.generators.s_level_catalyst import SLevelCatalystGenerator

# 初始化生成器
gen = SLevelCatalystGenerator(
    date_str="20260728",
    catalyst_title="全球科技股共振暴跌：创业板单日跌7.35% + 光模块双雄跌停机构60亿逆势接盘",
    subtitle="2026.07.28 · 盘后S级催化"
)

# ===== 1. 催化事件概述 =====
gen.add_catalyst_overview(
    overview="""
    <p><strong>【S级重大催化】</strong>2026年7月28日，全球科技股遭遇"黑色星期二"。韩国KOSPI指数单日暴跌10.84%触发年内第8次熔断，SK海力士跌14.65%、三星电子跌13.39%；日经225跌3.95%，铠侠跌超18%；隔夜美股英伟达重挫4.99%，费城半导体指数较6月高点回撤超20%进入技术性熊市。</p>
    <p style="margin-top:8px;">传导至A股，<strong>创业板指单日暴跌7.35%</strong>创年内最大跌幅，科创50跌6.33%，CPO/光模块板块领跌——中际旭创-15.69%成交516亿创A股单日记录、新易盛-17.13%。<strong>但龙虎榜显示机构在跌停板逆势扫货：中际旭创+37.32亿、新易盛+21.42亿，光模块双雄合计获机构净买入近60亿</strong>，北向资金同步净买入中际旭创10.28亿。</p>
    <p style="margin-top:8px;"><strong>核心矛盾</strong>：英伟达7500亿美元AI交易引发"循环融资"模式质疑 → 全球科技股估值体系重估 → A股科技成长板块获利盘集中兑现 → 机构资金借暴跌抢筹核心龙头。这是牛市中期调整的极端释放，还是趋势反转的开始？</p>
    """,
    importance="S级"
)

# ===== 2. 催化事件详解 =====
gen.add_catalyst_details(
    background="""
    <p><strong>1. 导火索：英伟达"循环融资"模式遭质疑</strong></p>
    <p>《华尔街日报》报道英伟达正就为OpenAI提供约2500亿美元财务担保进行磋商，叠加此前与SK集团5000亿美元合作协议，英伟达AI交易总规模超7500亿美元。市场担忧这种"供应商+投资者+担保方"三重角色的资金循环模式，若AI业务盈利兑现周期拉长，存储与算力全产业链或将面临过度投资与产能过剩风险。英伟达CDS价差单日飙升14个基点。</p>
    <p style="margin-top:8px;"><strong>2. 放大效应：韩国股市熔断 + 亚太科技股集体崩盘</strong></p>
    <p>韩国KOSPI开盘即跌5.3%，跌幅扩大至8%触发全市场熔断，恢复后继续下挫，全天多次临时停盘，最终收跌10.84%报6023.63点，失守6000点关口。SK海力士-14.65%、三星电子-13.39%。日经225跌3.95%，铠侠跌超18%，东京电子跌近11%。亚太科技股恐慌情绪快速向全球传导。</p>
    <p style="margin-top:8px;"><strong>3. 内部因素：长鑫科技上市虹吸 + 赛道获利盘拥挤</strong></p>
    <p>长鑫科技7月27日科创板上市，首日成交1411.87亿创A股历史记录，对存量科技股形成资金虹吸与比价压力。光模块/存储/算力前期累计涨幅巨大（中际旭创年内涨49%、新易盛涨32%），估值处于历史高位，在外围恐慌催化下获利盘集中兑现，叠加量化和融资盘被动平仓形成"多杀多"负反馈。</p>
    <p style="margin-top:8px;"><strong>4. 宏观背景：美联储议息会议前夕</strong></p>
    <p>美联储7月28-29日议息会议，市场定价7月不加息但年内仍有加息可能。全球科技股高估值对利率敏感，会议前风险偏好下降、资金避险情绪升温。</p>
    """,
    trigger="""
    <p><strong>🔥 触发因素一：机构60亿逆势接盘光模块双雄（超预期信号）</strong></p>
    <p>龙虎榜数据极为罕见：中际旭创机构净买入37.32亿（8家机构买、8家机构卖，净买额压倒性领先），新易盛机构净买入21.42亿，两只光模块龙头合计获机构净买入近60亿。北向资金同步净买入中际旭创10.28亿。这是机构对AI算力产业趋势的"集体定价"行为——不是抄底，是在跌停板上承接天量抛盘。</p>
    <p style="margin-top:8px;"><strong>🔥 触发因素二：长鑫科技纳入MSCI（产业地位确认）</strong></p>
    <p>MSCI宣布长鑫科技因完成IPO新股上市，将于8月10日正式纳入MSCI中国全股票指数。上市仅1天即获国际指数纳入，确认其作为全球第四大DRAM厂商的产业地位。长鑫科技3.28万亿市值登顶A股，标志着中国硬科技企业首次站上市场价值制高点，对半导体板块估值体系形成长期重构效应。</p>
    <p style="margin-top:8px;"><strong>🔥 触发因素三：增持潮开启（产业资本护盘信号）</strong></p>
    <p>盘后多家公司发布增持/回购公告：京东方A控股股东拟增持5-10亿元、燕东微控股股东一致行动人拟增持1.5-3亿元、中国中车控股股东首次增持0.02%。产业资本在大跌之际出手，释放政策底+市场底共振信号。</p>
    <p style="margin-top:8px;"><strong>🔥 触发因素四：存储产业基本面向好未变</strong></p>
    <p>Q3服务器DRAM合约价仍处于涨价通道，HBM紧平衡延续；台积电上调年度CAPEX，ASML年内二度上修指引，SEMI预测2026年全球设备销售额同比增23%创新高。产业景气度并未因股价调整而逆转。</p>
    """
)

# ===== 3. 产业链梳理 =====
gen.add_industry_chain_analysis(
    upstream=[
        {
            "name": "半导体设备 & 材料",
            "desc": "国产替代逻辑最硬，长鑫科技大规模扩产直接受益。设备零部件厂商同时享受订单上修与海外交期拉长带来的替代加速与涨价红利。",
            "stocks": [
                {"code": "688072", "name": "拓荆科技", "impact": "正面"},
                {"code": "002371", "name": "北方华创", "impact": "正面"},
                {"code": "688120", "name": "华海诚科", "impact": "中性偏正面"},
                {"code": "002409", "name": "雅克科技", "impact": "正面（HBM前驱体龙头）"},
            ]
        },
        {
            "name": "电子铜箔 & 基板材料",
            "desc": "AI算力基础设施核心上游，高端铜箔需求随HBM和先进封装扩产持续增长，但短期受板块情绪压制明显。",
            "stocks": [
                {"code": "301217", "name": "铜冠铜箔", "impact": "负面（情绪拖累）"},
            ]
        },
    ],
    midstream=[
        {
            "name": "存储芯片制造（DRAM/NAND）",
            "desc": "产业核心环节，长鑫科技上市重构A股存储板块估值体系。短期资金虹吸效应明显，中长期带动全产业链国产化加速。",
            "stocks": [
                {"code": "688003", "name": "长鑫科技", "impact": "正面（市值登顶A股）"},
                {"code": "300831", "name": "派瑞股份", "impact": "中性"},
            ]
        },
        {
            "name": "光模块/CPO",
            "desc": "本次暴跌重灾区，但机构逆势60亿接盘显示产业趋势未改。800G/1.6T需求确定性高，AI算力扩张支撑长期增长。短期估值消化压力大。",
            "stocks": [
                {"code": "300308", "name": "中际旭创", "impact": "短期负面/长期正面（机构接盘）"},
                {"code": "300502", "name": "新易盛", "impact": "短期负面/长期正面（机构接盘）"},
                {"code": "300394", "name": "天孚通信", "impact": "负面（情绪拖累）"},
            ]
        },
        {
            "name": "液冷散热",
            "desc": "AI算力配套基础设施，短期跟随科技股板块系统性调整，液冷渗透率提升长期逻辑不变。",
            "stocks": [
                {"code": "002837", "name": "英维克", "impact": "负面（深度调整）"},
                {"code": "300648", "name": "申菱环境", "impact": "负面"},
            ]
        },
    ],
    downstream=[
        {
            "name": "AI算力服务 & 云计算",
            "desc": "短期受资本支出可持续性质疑，但云厂商资本开支周期未结束。本周谷歌/微软/亚马逊财报将给出关键验证。",
            "stocks": [
                {"code": "603019", "name": "中科曙光", "impact": "中性偏负面"},
                {"code": "000977", "name": "浪潮信息", "impact": "中性偏负面"},
            ]
        },
        {
            "name": "AI应用端",
            "desc": "硬件调整对应用端传导有限，反而可能因硬件成本下降利好应用落地。但市场情绪恐慌期无差别杀跌。",
            "stocks": [
                {"code": "300229", "name": "拓尔思", "impact": "中性偏负面（情绪拖累）"},
            ]
        },
    ]
)

# ===== 4. 投资机会分析 =====
gen.add_investment_opportunities(
    opportunities=[
        {
            "name": "光模块龙头跌停板机构接盘机会",
            "priority": "高",
            "logic": '中际旭创+新易盛合计获机构净买入近60亿，北向资金同步加仓。这不是散户抄底，是机构级别的"定价确认"——在跌停板上承接天量抛盘意味着机构认为当前价格已具中长期投资价值。光模块产业基本面并未改变：800G渗透率快速提升、1.6T明年放量、AI算力资本开支周期未结束。短期恐慌杀跌后，核心龙头有望率先企稳反弹。',
            "stocks": [
                {"code": "300308", "name": "中际旭创", "impact": "机构+北向双增持"},
                {"code": "300502", "name": "新易盛", "impact": "机构大笔买入"},
            ]
        },
        {
            "name": "存储产业链国产替代（长期主线）",
            "priority": "高",
            "logic": "长鑫科技3.28万亿市值登顶A股，MSCI快速纳入，标志着中国存储产业进入全球第一梯队。长鑫大规模扩产将带动上游设备、材料、零部件全链条国产替代加速。SEMI预测2026年全球半导体设备销售额同比增23%创新高，国内厂商替代空间巨大。短期虽受情绪拖累，但产业景气度上行趋势未变。",
            "stocks": [
                {"code": "002409", "name": "雅克科技", "impact": "HBM前驱体+电子特气双主线"},
                {"code": "002371", "name": "北方华创", "impact": "设备龙头"},
                {"code": "688120", "name": "华海诚科", "impact": "先进封装材料"},
            ]
        },
        {
            "name": "半导体设备材料超跌反弹",
            "priority": "中",
            "logic": "科技成长板块系统性调整中，设备材料端受产业景气度支撑（长鑫扩产+国产替代加速），业绩确定性相对更高。本轮调整后估值回归合理区间，一旦市场情绪企稳，设备材料有望率先修复。",
            "stocks": [
                {"code": "688072", "name": "拓荆科技", "impact": "薄膜沉积设备"},
                {"code": "688012", "name": "中微公司", "impact": "刻蚀设备"},
            ]
        },
        {
            "name": "避险/防御板块轮动",
            "priority": "低",
            "logic": "资金高低切换明显，银行、白酒、食品饮料、医药等防御性板块逆势吸金。但这是短期避险行为，不构成中期趋势。科技成长股调整到位后，资金大概率回流高景气赛道。",
            "stocks": [
                {"code": "601398", "name": "工商银行", "impact": "避险配置"},
                {"code": "000568", "name": "泸州老窖", "impact": "消费防御"},
            ]
        },
    ],
    view_mode="tab"
)

# ===== 5. 催化深度分析（Skill增强） =====
gen.add_catalyst_deep_analysis(
    events=[
        {
            "title": "全球科技股暴跌事件",
            "type": "policy",
            "description": "英伟达7500亿AI交易引发循环融资质疑，韩国股市熔断，全球科技股共振暴跌，A股创业板单日跌7.35%",
            "category": "系统性风险"
        },
        {
            "title": "机构60亿逆势接盘光模块龙头",
            "type": "data",
            "description": "中际旭创龙虎榜机构净买入37.32亿、新易盛21.42亿，北向同步加仓，跌停板上出现罕见机构大笔承接",
            "category": "资金面信号"
        },
        {
            "title": "长鑫科技上市+MSCI纳入",
            "type": "meeting",
            "description": "长鑫科技上市首日涨465%市值3.28万亿登顶A股，上市次日即获MSCI纳入，8月10日生效",
            "category": "产业里程碑"
        },
    ]
)

# ===== 6. 持仓影响分析（自定义板块） =====
from components.layout import Section, SubCard, CardGrid
from components.data import StockTags, DataGrid

portfolio_html = '''
<div style="display: flex; flex-direction: column; gap: 14px;">
    <div style="background: linear-gradient(135deg, rgba(239,68,68,0.12) 0%, rgba(185,28,28,0.08) 100%); border-radius: 14px; padding: 20px; border: 1px solid rgba(248,113,113,0.25);">
        <div style="font-size: 16px; font-weight: 700; color: #fca5a5; margin-bottom: 12px;">
            🔴 英维克 (002837) — 跌停 -10.01% 收 55.13元
        </div>
        <div style="font-size: 13px; color: #fecaca; line-height: 1.8;">
            <p><strong>今日表现：</strong>跌停收盘55.13元，成交额26.88亿，换手率4.2%。主力资金净流出5.9亿元。液冷板块随科技股系统性崩盘。</p>
            <p style="margin-top:6px;"><strong>估值锚：</strong>动态PE 2159倍、PB 22.7倍（数据来源：证券时报/证券之星），估值仍处历史极高位。业绩方面2026Q1归母净利同比下滑超80%。</p>
            <p style="margin-top:6px;"><strong>技术位：</strong>今日跌停跌破前期低点58元支撑，下降通道完全打开。下一支撑位看50元整数关口（前低区域）。</p>
            <p style="margin-top:6px;"><strong>操作建议：</strong>已深度破止损（成本104.23元，浮亏-47.1%），<strong>无条件清仓纪律必须执行</strong>。任何反弹都是离场机会，严禁补仓抄底。液冷行业逻辑虽在，但公司业绩兑现跟不上估值，熊市中高估值是最大的利空。</p>
        </div>
    </div>
    
    <div style="background: linear-gradient(135deg, rgba(245,158,11,0.12) 0%, rgba(180,83,9,0.08) 100%); border-radius: 14px; padding: 20px; border: 1px solid rgba(251,191,36,0.25);">
        <div style="font-size: 16px; font-weight: 700; color: #fcd34d; margin-bottom: 12px;">
            🟡 铜冠铜箔 (301217) — 跌 -9.52% 收 87.66元
        </div>
        <div style="font-size: 13px; color: #fef3c7; line-height: 1.8;">
            <p><strong>今日表现：</strong>大跌9.52%收87.66元，成交额27.5亿，换手率3.65%。主力资金净流出2.83亿元（占成交额10.3%）。存储铜箔板块随大盘系统性调整。</p>
            <p style="margin-top:6px;"><strong>双重验证：</strong>① 证券时报数据宝确认主力净流出2.42亿 ② 证券之星确认主力净流出2.83亿，数据基本一致。③ 公司层面：目前未发布重大利空公告，下跌属板块系统性调整而非个股利空。</p>
            <p style="margin-top:6px;"><strong>估值锚：</strong>动态PE约175倍、PB 13.58倍（数据来源：证券时报网），仍处历史高位。中报预增486%-544%业绩已兑现，二季度环比下滑约7%是前期调整主因。</p>
            <p style="margin-top:6px;"><strong>技术位：</strong>今日跌破90元关键支撑位，创出调整新低87.66元。从高点202元回撤超56%。下一支撑位看80-85元区间（前低区域）。</p>
            <p style="margin-top:6px;"><strong>操作建议：</strong><strong>已破90元止盈线，明日开盘无条件止盈离场保住剩余利润</strong>（成本87.16元，浮盈仅剩0.6%）。存储产业逻辑虽硬，但短期趋势完全走坏，先出局观望，等板块企稳后再评估是否重新介入。</p>
        </div>
    </div>
    
    <div style="background: linear-gradient(135deg, rgba(16,185,129,0.12) 0%, rgba(5,150,105,0.08) 100%); border-radius: 14px; padding: 20px; border: 1px solid rgba(52,211,153,0.25);">
        <div style="font-size: 16px; font-weight: 700; color: #6ee7b7; margin-bottom: 12px;">
            🟢 雅克科技 (002409) — 跌 -1.72% 收 166.43元（相对抗跌）
        </div>
        <div style="font-size: 13px; color: #d1fae5; line-height: 1.8;">
            <p><strong>今日表现：</strong>仅跌1.72%收166.43元，成交额98.52亿（天量），换手率18.26%。主力资金净流出5.66亿，但近5日累计净流入14.72亿。大宗交易成交699万，卖方为机构专用，买方为华泰福建分公司。</p>
            <p style="margin-top:6px;"><strong>双重验证：</strong>① 证券时报确认大宗交易成交价166.43元 ② 东方财富财富号数据与收盘价一致。③ 公司层面：未发布利空公告，下跌属板块情绪带动，相对抗跌显示资金认可。</p>
            <p style="margin-top:6px;"><strong>龙虎榜验证：</strong>今日雅克科技未登上龙虎榜（龙虎榜76只个股中未见其名），说明单日跌幅未达异动标准，资金博弈相对温和。</p>
            <p style="margin-top:6px;"><strong>估值锚：</strong>动态PE约68倍、PB 9.2倍（数据来源：证券时报网），在半导体材料板块中估值相对合理。HBM前驱体+电子特气双主线逻辑硬，机构持仓集中。</p>
            <p style="margin-top:6px;"><strong>技术位：</strong>今日逆势抗跌收166.43元，5日累计涨15.94%（数据来源：证券时报），在板块暴跌中展现强势。关键支撑位155-160元，压力位175-180元。</p>
            <p style="margin-top:6px;"><strong>操作建议：</strong><strong>持仓中唯一抗跌标的，可继续持有底仓观察</strong>。HBM前驱体龙头地位稳固，长鑫科技扩产+存储产业链国产替代逻辑未变。若跌破155元则止盈减仓；若站稳170元以上可考虑小仓位加仓博弈反弹。</p>
        </div>
    </div>
    
    <div style="background: linear-gradient(135deg, rgba(220,38,38,0.15) 0%, rgba(153,27,27,0.1) 100%); border-radius: 14px; padding: 20px; border: 1px solid rgba(248,113,113,0.3);">
        <div style="font-size: 16px; font-weight: 700; color: #f87171; margin-bottom: 12px;">
            🚨 *ST建艺 (002789) — 退市风险股（最高优先级清仓）
        </div>
        <div style="font-size: 13px; color: #fecaca; line-height: 1.8;">
            <p><strong>核心判断：</strong>退市风险+债务问题未解，任何价格都应立即清仓止损。退市风险敞口必须关闭，绝不恋战。</p>
            <p style="margin-top:6px;"><strong>操作建议：</strong>明日开盘无条件清仓（最高优先级），退市风险股没有任何持有的理由。</p>
        </div>
    </div>
</div>
'''

portfolio_section = Section(title="📊 持仓影响诊断与操作建议", content=portfolio_html, icon="briefcase", variant="highlight")
gen._components.append(portfolio_section)

# ===== 7. 隔夜外盘跟踪 =====
overnight_html = '''
<div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 12px;">
    <div style="background: rgba(239,68,68,0.08); border-radius: 12px; padding: 16px; border: 1px solid rgba(239,68,68,0.2);">
        <div style="font-size: 14px; font-weight: 700; color: #fca5a5; margin-bottom: 10px;">📉 美股主要指数（7/27收盘）</div>
        <div style="font-size: 13px; color: #cbd5e1; line-height: 2;">
            <p>纳斯达克综合指数：<span style="color:#fca5a5;">-0.18%</span> 24932.08点</p>
            <p>费城半导体指数：<span style="color:#fca5a5;">-2.23%</span>（较6月高点回撤超20%，进入技术性熊市）</p>
            <p>道琼斯工业指数：<span style="color:#6ee7b7;">+0.51%</span> 52210.08点</p>
            <p>标普500指数：<span style="color:#6ee7b7;">+0.02%</span> 7413.18点</p>
        </div>
    </div>
    
    <div style="background: rgba(245,158,11,0.08); border-radius: 12px; padding: 16px; border: 1px solid rgba(245,158,11,0.2);">
        <div style="font-size: 14px; font-weight: 700; color: #fcd34d; margin-bottom: 10px;">🔥 核心半导体标的</div>
        <div style="font-size: 13px; color: #cbd5e1; line-height: 2;">
            <p>英伟达 NVDA：<span style="color:#fca5a5;">-4.99%</span>（循环融资质疑拖累）</p>
            <p>台积电 TSM：<span style="color:#fca5a5;">-1.07%</span></p>
            <p>美光 MU：<span style="color:#fca5a5;">-2%</span>（盘前再跌5.24%）</p>
            <p>AMD：<span style="color:#fca5a5;">-5.17%</span></p>
            <p>闪迪：<span style="color:#fca5a5;">-11.02%</span></p>
            <p>SK海力士 ADR：<span style="color:#fca5a5;">-7.47%</span>（跌破发行价149美元）</p>
            <p>博通 AVGO：<span style="color:#6ee7b7;">+0.34%</span></p>
        </div>
    </div>
    
    <div style="background: rgba(239,68,68,0.08); border-radius: 12px; padding: 16px; border: 1px solid rgba(239,68,68,0.2);">
        <div style="font-size: 14px; font-weight: 700; color: #fca5a5; margin-bottom: 10px;">🇰🇷 亚太市场（7/28收盘）</div>
        <div style="font-size: 13px; color: #cbd5e1; line-height: 2;">
            <p>韩国KOSPI：<span style="color:#f87171;">-10.84%</span> 6023.63点（年内第8次熔断）</p>
            <p>SK海力士韩股：<span style="color:#f87171;">-14.65%</span></p>
            <p>三星电子：<span style="color:#f87171;">-13.39%</span></p>
            <p>日经225：<span style="color:#fca5a5;">-3.95%</span> 62364.92点</p>
            <p>铠侠：<span style="color:#f87171;">-18%+</span></p>
            <p>东京电子：<span style="color:#fca5a5;">-11%</span></p>
        </div>
    </div>
    
    <div style="background: rgba(59,130,246,0.08); border-radius: 12px; padding: 16px; border: 1px solid rgba(59,130,246,0.2);">
        <div style="font-size: 14px; font-weight: 700; color: #93c5fd; margin-bottom: 10px;">📰 关键政策/事件</div>
        <div style="font-size: 13px; color: #cbd5e1; line-height: 2;">
            <p>美联储议息会议（7/28-29）：市场定价7月不加息（62.6%概率），但年内仍存加息预期</p>
            <p>美伊停火：油价下跌2.8%至一周低位，停火协议脆弱维持</p>
            <p>特朗普称与伊朗"谈得不错"，有达成协议可能</p>
            <p>MSCI纳入长鑫科技：8月10日生效</p>
            <p>美股盘前：存储板块集体续跌5%+，英特尔/AMD跌超4%</p>
        </div>
    </div>
</div>
<p style="margin-top: 10px; font-size: 12px; color: #94a3b8;">数据来源：Reuters、澎湃新闻、财联社、证券时报、21世纪经济报道 | 2026.07.28</p>
'''

overnight_section = Section(title="🌍 隔夜外盘 & 亚太市场全景跟踪", content=overnight_html, icon="globe")
gen._components.append(overnight_section)

# ===== 8. 风险提示 =====
gen.add_risk_warning([
    '全球科技股系统性调整风险：英伟达"循环融资"质疑若持续发酵，全球半导体估值体系可能进一步下修，A股科技成长板块或继续承压',
    "美联储加息风险：若议息会议释放鹰派信号或暗示年内继续加息，高估值成长股将面临更大调整压力",
    "韩股流动性风险：韩国股市年内第8次熔断，外资持续流出可能引发亚太市场连锁反应",
    "长鑫科技虹吸效应：3.28万亿市值新股对存量科技股形成资金分流，中小市值科技股可能继续被边缘化",
    "持仓股风险：英维克已跌破所有支撑位，铜冠铜箔已破90元止盈线，严格执行纪律是第一要务",
    "业绩雷风险：中报最后披露期，部分科技股业绩可能不及预期，需警惕个股爆雷",
    "本报告不构成投资建议，股市有风险，投资需谨慎",
])

# ===== 9. 投资策略建议 =====
strategy_content = '''
<p><strong>【整体判断】</strong>今日全球科技股暴跌是多重因素共振的结果：外部（英伟达循环融资质疑+韩股熔断）+内部（长鑫上市虹吸+获利盘兑现+美联储议息前避险）。这是牛市中期调整的极端情绪释放，而非产业趋势逆转。核心判断依据：机构在跌停板大笔接盘光模块龙头、存储产业基本面向好未变、产业资本增持潮开启。</p>

<p style="margin-top:12px;"><strong>【仓位控制】</strong>整体仓位降至<strong>1-2成</strong>，现金为王，等待市场确认企稳信号（缩量+止跌+量价配合反弹）。在恐慌情绪未完全释放前，不急于抄底。</p>

<p style="margin-top:12px;"><strong>【分标的操作建议】</strong></p>
<ol style="margin-top:8px; padding-left: 20px; line-height: 2; color: #e2e8f0;">
    <li><strong>英维克 (002837)：🚨 无条件清仓</strong>——跌停破位，浮亏-47.1%，深度破止损。纪律比亏损更重要，任何反弹都是离场机会，严禁补仓抄底。</li>
    <li><strong>铜冠铜箔 (301217)：🚨 明日开盘止盈离场</strong>——已跌破90元关键支撑位，浮盈仅剩0.6%，几近归零。先出局保住本金，等板块企稳后再评估。存储产业逻辑虽硬，但短期趋势完全走坏，君子不立危墙之下。</li>
    <li><strong>雅克科技 (002409)：🟢 继续持有底仓观察</strong>——板块暴跌中仅跌1.72%，相对抗跌，HBM前驱体+长鑫扩产双主线逻辑硬。支撑位155-160元，跌破则减仓；站稳170元可考虑小仓位加仓。</li>
    <li><strong>*ST建艺 (002789)：🚨 立即清仓（最高优先级）</strong>——退市风险股，没有任何持有的理由。</li>
</ol>

<p style="margin-top:12px;"><strong>【关注重点】</strong></p>
<ul style="margin-top:8px; padding-left: 20px; line-height: 2; color: #e2e8f0;">
    <li>美联储7月议息会议结果（北京时间7/30凌晨）</li>
    <li>谷歌/微软/亚马逊/苹果Q2财报（本周发布）——验证AI资本开支可持续性</li>
    <li>A股科技股何时缩量止跌（确认调整底部）</li>
    <li>长鑫科技次新股走势对存储板块的牵引作用</li>
    <li>机构逆势接盘的光模块龙头能否率先企稳反弹</li>
</ul>

<p style="margin-top:12px;"><strong>【中期展望】</strong>AI算力+存储的产业大趋势并未逆转，Q3服务器DRAM合约价仍在涨价通道、HBM持续紧平衡、台积电上调CAPEX、SEMI上修设备销售额。调整是牛市中的正常现象，也是优质标的的"黄金坑"机会。但需要等待恐慌情绪充分释放后，再逐步左侧布局核心龙头。</p>
'''

gen.add_investment_strategy(strategy_content)

# ===== 生成并发布 =====
print("开始生成S级催化报告...")
html = gen.generate()
print(f"报告生成完成，长度: {len(html)} 字符")

# 发布
result = gen.publish(
    title="全球科技股共振暴跌：创业板单日跌7.35% + 光模块双雄跌停机构60亿逆势接盘",
    report_type="s_level_catalyst",
    filename="20260728_盘后_S级催化扫描_全球科技股共振暴跌.html",
    excerpt="S级重大催化：韩国股市熔断、英伟达重挫、A股创业板暴跌7.35%。但机构在跌停板逆势60亿接盘光模块双雄，长鑫科技MSCI快速纳入——这是牛市中期调整还是趋势反转？",
    auto_deploy=True,
    docs_root="docs"
)
print(f"发布结果: {result}")
print("任务完成！")
