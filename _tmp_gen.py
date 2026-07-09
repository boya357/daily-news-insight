import sys, os
os.chdir('/root/daily-news-insight')
sys.path.insert(0, '/root/daily-news-insight/v3')

from v3.generators.s_level_catalyst import SLevelCatalystGenerator

gen = SLevelCatalystGenerator(
    date_str="20260709",
    catalyst_title="长鑫科技IPO+兆易创新11倍业绩引爆存储超级周期",
    subtitle="2026.07.09 · 盘后S级催化"
)

# === 1. 催化事件概述 ===
gen.add_catalyst_overview(
    overview="今日三大重磅催化共振，存储产业链迎来史诗级行情：① 国产DRAM龙头长鑫科技凌晨披露科创板IPO招股意向书，7月16日申购，募资295亿元创科创板史上第二大IPO，带动半导体设备、材料、先进封装全产业链爆发；② 盘后兆易创新发布2026半年报业绩预告，归母净利润69亿元同比暴增1099%，Q2单季环比+272%，大幅超出市场全年盈利预期，正式验证存储超级周期盈利弹性；③ 隔夜美股半导体板块全面反弹，费城半导体指数涨2.23%，英伟达涨3.65%，美光涨1.11%，美股盘前存储芯片继续走强（美光涨近4%）。科创50单日大涨8.41%创历史第四大涨幅，两市成交2.91万亿放量3500亿。",
    importance="极高"
)

# === 2. 催化事件详解 ===
gen.add_catalyst_details(
    background="本轮存储上行周期始于2025年Q4，由AI算力基础设施建设驱动的HBM/DDR5需求爆发叠加行业供给端收缩共同推动。长鑫科技作为国内最大DRAM厂商，2025年营收617.99亿元，同比高速增长，2026年上半年预计营收1100-1200亿元，归母净利润500-570亿元。公司IPO将成为科创板第二大募资项目（仅次于中芯国际），战略配售比例高达50%。与此同时，兆易创新作为国内存储设计龙头，半年报业绩暴增11倍，其中扣非净利润48.5亿同比+791%，验证了存储芯片量价齐升的行业景气度。",
    trigger="三大触发因素集中爆发：① 长鑫科技7月9日凌晨正式披露招股意向书及发行安排，明确7月16日申购，引发市场对国产存储产业链的全面重估；② 兆易创新7月9日盘后发布半年报业绩预告，净利润69亿同比+1099%，大幅超出市场全年45-61亿的一致预期，直接引爆存储板块情绪；③ 隔夜美股半导体板块在美伊冲突背景下逆势走强，费半涨2.23%，英伟达涨3.65%，博通获苹果300亿美元大单涨4.83%，美股盘前存储芯片继续拉升（美光涨近4%），为A股半导体提供正向映射。"
)

# === 3. 产业链梳理 ===
upstream = [
    {
        "name": "半导体设备",
        "desc": "晶圆制造核心设备，长鑫扩产直接受益。光刻、刻蚀、薄膜沉积、清洗设备需求持续放量",
        "stocks": [
            {"code": "688012", "name": "中微公司", "impact": "核心刻蚀设备供应商"},
            {"code": "603690", "name": "至纯科技", "impact": "清洗设备"},
            {"code": "688082", "name": "盛美上海", "impact": "清洗/电镀设备"},
        ]
    },
    {
        "name": "半导体材料",
        "desc": "晶圆制造耗材，包括前驱体、光刻胶、电子特气、靶材等，国产替代空间巨大",
        "stocks": [
            {"code": "002409", "name": "雅克科技", "impact": "HBM前驱体+光刻胶（持仓）"},
            {"code": "300655", "name": "晶瑞电材", "impact": "光刻胶+电子材料"},
            {"code": "688268", "name": "华特气体", "impact": "电子特气"},
        ]
    },
    {
        "name": "硅片/硅料",
        "desc": "半导体硅片是晶圆制造基础材料，大硅片国产替代加速",
        "stocks": [
            {"code": "688584", "name": "上海合晶", "impact": "半导体硅片"},
            {"code": "600206", "name": "有研硅", "impact": "硅材料"},
            {"code": "300236", "name": "上海新阳", "impact": "半导体化学品"},
        ]
    },
]

midstream = [
    {
        "name": "存储芯片设计",
        "desc": "DRAM/NAND/NOR Flash芯片设计厂商，直接受益于存储涨价周期",
        "stocks": [
            {"code": "603986", "name": "兆易创新", "impact": "NOR Flash龙头+DRAM布局"},
            {"code": "688525", "name": "佰维存储", "impact": "存储模组"},
            {"code": "301308", "name": "江波龙", "impact": "存储模组"},
            {"code": "000021", "name": "深科技", "impact": "存储封测"},
        ]
    },
    {
        "name": "晶圆制造",
        "desc": "逻辑+存储晶圆代工，产能紧张背景下议价能力提升",
        "stocks": [
            {"code": "688981", "name": "中芯国际", "impact": "国内晶圆代工龙头"},
            {"code": "688347", "name": "华虹公司", "impact": "特色工艺代工"},
        ]
    },
    {
        "name": "先进封装",
        "desc": "HBM/2.5D/3D封装技术，AI算力核心瓶颈环节",
        "stocks": [
            {"code": "002156", "name": "通富微电", "impact": "AMD核心封测+HBM"},
            {"code": "600584", "name": "长电科技", "impact": "全球封测龙头"},
            {"code": "002185", "name": "华天科技", "impact": "封测"},
            {"code": "603005", "name": "晶方科技", "impact": "先进封装"},
        ]
    },
]

downstream = [
    {
        "name": "AI服务器/算力",
        "desc": "存储芯片最大增量需求来源，AI算力建设拉动HBM/DDR5需求",
        "stocks": [
            {"code": "000977", "name": "浪潮信息", "impact": "AI服务器龙头"},
            {"code": "002837", "name": "英维克", "impact": "液冷散热（持仓）"},
            {"code": "002281", "name": "光迅科技", "impact": "光模块"},
        ]
    },
    {
        "name": "PCB/CCL",
        "desc": "AI服务器PCB需求爆发，高端PCB量价齐升",
        "stocks": [
            {"code": "301217", "name": "铜冠铜箔", "impact": "电子铜箔（持仓）"},
            {"code": "002916", "name": "深南电路", "impact": "高端PCB"},
            {"code": "002463", "name": "沪电股份", "impact": "PCB"},
        ]
    },
    {
        "name": "消费电子/汽车电子",
        "desc": "传统存储需求复苏，去库存完成后需求回补",
        "stocks": [
            {"code": "002475", "name": "立讯精密", "impact": "消费电子代工"},
            {"code": "300782", "name": "卓胜微", "impact": "射频芯片"},
        ]
    },
]

gen.add_industry_chain_analysis(upstream=upstream, midstream=midstream, downstream=downstream)

# === 4. 持仓影响分析 ===
from components.layout import Section

stock_impact_html = """
<div class="grid grid-cols-2 md:grid-cols-4 gap-3">
    <div style="background: linear-gradient(135deg, rgba(16,185,129,0.2) 0%, rgba(5,150,105,0.12) 100%); 
                border-radius: 14px; padding: 16px; border: 1px solid rgba(16,185,129,0.3);">
        <div style="font-size: 15px; font-weight: 700; color: #34d399; margin-bottom: 8px;">🚀 雅克科技</div>
        <div style="font-size: 22px; font-weight: 800; color: #6ee7b7; margin-bottom: 4px;">+10.00% 涨停</div>
        <div style="font-size: 11.5px; color: #a7f3d0; line-height: 1.5;">HBM前驱体+光刻胶<br/>收盘价209.00元，封单3.18亿</div>
    </div>
    <div style="background: linear-gradient(135deg, rgba(59,130,246,0.2) 0%, rgba(37,99,235,0.12) 100%); 
                border-radius: 14px; padding: 16px; border: 1px solid rgba(59,130,246,0.3);">
        <div style="font-size: 15px; font-weight: 700; color: #60a5fa; margin-bottom: 8px;">📈 铜冠铜箔</div>
        <div style="font-size: 22px; font-weight: 800; color: #93c5fd; margin-bottom: 4px;">+4.24%</div>
        <div style="font-size: 11.5px; color: #bfdbfe; line-height: 1.5;">PCB铜箔间接受益<br/>收盘价139.68元，成交48.58亿</div>
    </div>
    <div style="background: linear-gradient(135deg, rgba(245,158,11,0.2) 0%, rgba(217,119,6,0.12) 100%); 
                border-radius: 14px; padding: 16px; border: 1px solid rgba(245,158,11,0.3);">
        <div style="font-size: 15px; font-weight: 700; color: #fbbf24; margin-bottom: 8px;">🌡️ 英维克</div>
        <div style="font-size: 22px; font-weight: 800; color: #fde68a; margin-bottom: 4px;">+5.20%</div>
        <div style="font-size: 11.5px; color: #fef3c7; line-height: 1.5;">液冷散热+算力基建<br/>收盘价75.87元，探底V反</div>
    </div>
    <div style="background: linear-gradient(135deg, rgba(239,68,68,0.2) 0%, rgba(220,38,38,0.12) 100%); 
                border-radius: 14px; padding: 16px; border: 1px solid rgba(239,68,68,0.3);">
        <div style="font-size: 15px; font-weight: 700; color: #f87171; margin-bottom: 8px;">⚠️ *ST建艺</div>
        <div style="font-size: 22px; font-weight: 800; color: #fca5a5; margin-bottom: 4px;">-1.61%</div>
        <div style="font-size: 11.5px; color: #fecaca; line-height: 1.5;">无直接关联<br/>收盘价10.38元，成交2114万</div>
    </div>
</div>
<div style="margin-top: 14px; font-size: 13px; color: #94a3b8; line-height: 1.8;">
    <strong style="color: #fbbf24;">持仓核心结论：</strong><br/>
    • <strong style="color: #34d399;">雅克科技（涨停）</strong>：HBM前驱体+光刻胶双轮驱动，直接受益存储大爆发，今日涨停验证逻辑，中期空间可期，明日高开减仓1/3锁定利润<br/>
    • <strong style="color: #93c5fd;">铜冠铜箔（+4.24%）</strong>：间接受益于AI PCB情绪，但关联度有限，继续执行140-145区间减仓策略<br/>
    • <strong style="color: #fde68a;">英维克（+5.20%）</strong>：超跌反弹性质，量能一般，75-77区间继续减仓至半仓以下<br/>
    • <strong style="color: #fca5a5;">*ST建艺（-1.61%）</strong>：无关联，继续执行清仓策略
</div>
"""

section = Section(
    title="📊 持仓影响评估",
    content=stock_impact_html,
    icon="pie-chart",
    variant="highlight"
)
gen._components.append(section)

# === 5. 隔夜外盘跟踪 ===
overnight_html = """
<div class="grid md:grid-cols-2 gap-3">
    <div style="background: linear-gradient(135deg, rgba(34,197,94,0.12) 0%, rgba(22,163,74,0.08) 100%); 
                border-radius: 14px; padding: 18px; border: 1px solid rgba(34,197,94,0.25);">
        <div style="font-size: 15px; font-weight: 700; color: #4ade80; margin-bottom: 12px;">📈 美股指数表现</div>
        <div style="display: flex; flex-direction: column; gap: 8px; font-size: 13px; color: #e2e8f0;">
            <div style="display: flex; justify-content: space-between;">
                <span style="color: #94a3b8;">费城半导体指数</span>
                <span style="color: #4ade80; font-weight: 600;">+2.23%</span>
            </div>
            <div style="display: flex; justify-content: space-between;">
                <span style="color: #94a3b8;">纳斯达克综合</span>
                <span style="color: #4ade80; font-weight: 600;">+0.20%</span>
            </div>
            <div style="display: flex; justify-content: space-between;">
                <span style="color: #94a3b8;">标普500</span>
                <span style="color: #f87171; font-weight: 600;">-0.28%</span>
            </div>
            <div style="display: flex; justify-content: space-between;">
                <span style="color: #94a3b8;">道琼斯工业</span>
                <span style="color: #f87171; font-weight: 600;">-1.09%</span>
            </div>
        </div>
    </div>
    <div style="background: linear-gradient(135deg, rgba(59,130,246,0.12) 0%, rgba(37,99,235,0.08) 100%); 
                border-radius: 14px; padding: 18px; border: 1px solid rgba(59,130,246,0.25);">
        <div style="font-size: 15px; font-weight: 700; color: #60a5fa; margin-bottom: 12px;">🔬 核心半导体标的</div>
        <div style="display: flex; flex-direction: column; gap: 8px; font-size: 13px; color: #e2e8f0;">
            <div style="display: flex; justify-content: space-between;">
                <span style="color: #94a3b8;">英伟达 NVDA</span>
                <span style="color: #4ade80; font-weight: 600;">+3.65%</span>
            </div>
            <div style="display: flex; justify-content: space-between;">
                <span style="color: #94a3b8;">博通 AVGO</span>
                <span style="color: #4ade80; font-weight: 600;">+4.83%（苹果300亿大单）</span>
            </div>
            <div style="display: flex; justify-content: space-between;">
                <span style="color: #94a3b8;">美光科技 MU</span>
                <span style="color: #4ade80; font-weight: 600;">+1.11%（盘前+4%）</span>
            </div>
            <div style="display: flex; justify-content: space-between;">
                <span style="color: #94a3b8;">台积电 TSM</span>
                <span style="color: #4ade80; font-weight: 600;">+1.02%</span>
            </div>
            <div style="display: flex; justify-content: space-between;">
                <span style="color: #94a3b8;">闪迪 SNDK</span>
                <span style="color: #4ade80; font-weight: 600;">+6.77%</span>
            </div>
        </div>
    </div>
</div>
<div style="margin-top: 12px; background: rgba(251,191,36,0.08); border-radius: 12px; padding: 14px; border: 1px solid rgba(251,191,36,0.2);">
    <div style="font-size: 13px; font-weight: 600; color: #fbbf24; margin-bottom: 6px;">⚠️ 关键关注点</div>
    <div style="font-size: 12.5px; color: #fef3c7; line-height: 1.7;">
        1. <strong>存储股反弹确认</strong>：闪迪+6.77%、希捷+3.91%、西部数据+3.42%，存储板块连续调整后企稳反弹，SK海力士美股发行定价为关键节点<br/>
        2. <strong>英伟达估值触底</strong>：前瞻PE降至18倍（标普500为20倍），为2019年以来最低，资金开始从"单一龙头"转向"全产业链扩散"<br/>
        3. <strong>地缘风险扰动</strong>：美伊冲突升级导致油价大涨5%+，道指承压，但科技股展现韧性，纳指深V反转<br/>
        4. <strong>美联储鹰派</strong>：6月会议纪要删除降息措辞，部分官员认为有理由加息，12月加息概率上升
    </div>
</div>
"""

section2 = Section(
    title="🌍 隔夜外盘跟踪",
    content=overnight_html,
    icon="globe"
)
gen._components.append(section2)

# === 6. 投资机会分析 ===
opportunities = [
    {
        "name": "存储芯片设计龙头",
        "priority": "高",
        "logic": "兆易创新半年报业绩暴增1099%，验证存储超级周期盈利弹性。存储芯片量价齐升趋势明确，国产替代加速推进，行业景气度有望持续至2028年。重点关注具备技术壁垒和客户资源的头部厂商。",
        "stocks": [
            {"code": "603986", "name": "兆易创新", "impact": "NOR龙头+DRAM"},
            {"code": "688525", "name": "佰维存储", "impact": "存储模组"},
        ]
    },
    {
        "name": "半导体设备（长鑫产业链核心受益）",
        "priority": "高",
        "logic": "长鑫科技IPO募资295亿将全部投入DRAM产能扩张，后续持续扩产确定性高。设备作为扩产先行环节，订单确定性最强，国产设备厂商受益于长鑫国产化率提升。",
        "stocks": [
            {"code": "688012", "name": "中微公司", "impact": "刻蚀设备龙头"},
            {"code": "603690", "name": "至纯科技", "impact": "清洗设备"},
        ]
    },
    {
        "name": "先进封装（HBM方向）",
        "priority": "高",
        "logic": "AI算力需求爆发带动HBM需求井喷，先进封装成为算力瓶颈。通富微电、长电科技等国内封测龙头积极布局HBM封装技术，叠加长鑫科技扩产带动存储封测需求，双重驱动下弹性巨大。",
        "stocks": [
            {"code": "002156", "name": "通富微电", "impact": "AMD核心+HBM"},
            {"code": "600584", "name": "长电科技", "impact": "全球封测龙头"},
        ]
    },
    {
        "name": "半导体材料（前驱体/光刻胶）",
        "priority": "中",
        "logic": "存储芯片扩产带动上游材料需求，国产替代空间巨大。雅克科技等前驱体龙头直接受益于HBM和先进制程芯片需求增长。",
        "stocks": [
            {"code": "002409", "name": "雅克科技", "impact": "HBM前驱体（持仓）"},
        ]
    },
    {
        "name": "液冷散热（算力基建）",
        "priority": "中",
        "logic": "AI算力密度持续提升，液冷散热成为刚需。但短期需注意前期涨幅过大后的消化，关注业绩兑现能力强的龙头。",
        "stocks": [
            {"code": "002837", "name": "英维克", "impact": "液冷龙头（持仓）"},
        ]
    },
]

gen.add_investment_opportunities(opportunities, view_mode="tab")

# === 7. 催化深度分析（Skill增强） ===
gen.add_catalyst_deep_analysis([
    {
        "title": "长鑫科技IPO催化",
        "type": "policy",
        "description": "国产DRAM龙头长鑫科技启动科创板IPO，募资295亿创科创板第二大记录，7月16日申购，战略配售50%",
        "category": "国产存储"
    },
    {
        "title": "兆易创新业绩超预期",
        "type": "earnings",
        "description": "兆易创新半年报净利69亿同比+1099%，Q2单季环比+272%，大幅超出市场全年盈利预期",
        "category": "存储周期"
    },
    {
        "title": "美股半导体反弹",
        "type": "data",
        "description": "费城半导体指数涨2.23%，英伟达涨3.65%，美光盘前再涨4%，全球半导体情绪回暖",
        "category": "海外映射"
    },
])

# === 8. 风险提示 ===
gen.add_risk_warning([
    "存储芯片行业具有强周期性，若下游AI需求不及预期或产能扩张过快，价格可能快速回落",
    "短期涨幅过大，科创50单日涨8.41%创历史第四大涨幅，获利盘抛压较大，警惕冲高回落",
    "美伊冲突升级可能引发全球市场风险偏好下降，油价大涨推升通胀预期，美联储加息压力增大",
    "长鑫科技IPO可能对市场资金形成虹吸效应，短期分流二级市场资金",
    "部分个股估值已处于历史高位，需警惕业绩兑现不及预期的风险"
])

# === 9. 投资策略建议 ===
gen.add_investment_strategy("""
<strong>【总体策略】</strong>今日存储产业链全面爆发属于S级事件驱动，但短期涨幅过大不宜盲目追高，建议分化对待：<br/><br/>

<strong>【持仓操作建议】</strong><br/>
1. <strong style="color: #4ade80;">雅克科技（涨停）</strong>：今日一字涨停封板力度强，HBM前驱体+光刻胶双逻辑共振，叠加兆易创新业绩验证存储周期，中期仍有空间。明日若高开超5%可减仓1/3锁定利润，回踩200元附近接回；若继续强势封板则持有。PE(TTM)约93倍，PB约8.8倍，处于历史高位，需警惕回调风险。<br/>
2. <strong style="color: #fbbf24;">铜冠铜箔（+4.24%）</strong>：间接受益于半导体板块整体情绪，但铜箔主业与存储芯片关联度有限。140-145区间继续执行减仓策略，降至1/3底仓以下，保留对AI PCB行情的暴露但控制风险。PE约261倍，估值偏高。<br/>
3. <strong style="color: #fbbf24;">英维克（+5.20%）</strong>：探底V反但量能一般，属于超跌反弹性质。75-77区间继续减仓至半仓以下，液冷逻辑虽在但短期缺乏独立催化。PE(TTM)高达2792倍，估值严重偏离基本面，必须严格风控。<br/>
4. <strong style="color: #f87171;">*ST建艺（-1.61%）</strong>：继续执行清仓策略，任何反弹都是离场机会。<br/><br/>

<strong>【新建仓方向】</strong>优先考虑半导体设备和存储设计龙头，回调时分批布局。重点关注：中微公司、通富微电、兆易创新（需等回调）。<br/><br/>

<strong>【仓位管理】</strong>整体仓位控制在5-6成，半导体方向不超过总仓位的40%，留足弹药应对可能的回调机会。
""")

# === 发布 ===
result = gen.publish(
    title="长鑫IPO+兆易11倍业绩引爆存储超级周期",
    report_type="s_level_catalyst",
    filename="20260709_盘后_S级催化扫描_长鑫IPO+兆易11倍业绩引爆存储超级周期.html",
    excerpt="长鑫科技295亿IPO+兆易创新半年报暴增1099%+美股半导体反弹，三重重磅催化共振，科创50暴涨8.41%创历史第四大涨幅"
)

print("发布结果:", result)
