import sys, os, json
sys.path.insert(0, 'v3')
os.chdir('/root/daily-news-insight')

from v3.generators.aftermarket import AftermarketGenerator

DATE = "20260827"
SUBTITLE = "2026.08.27 · 盘后速递"

gen = AftermarketGenerator(date_str=DATE, subtitle=SUBTITLE)

# ============ 1. 今日核心亮点 ============
gen.add_today_highlight("""
<div style="line-height:1.9; font-size:14px;">
<p><strong style="color:#f59e0b; font-size:16px;">🔥 英伟达"核弹级"财报点燃全场！</strong> 隔夜英伟达Q2营收962亿美元同比+106%，Q3指引1080亿美元首破千亿，2028财年增速指引70%（大超预期45%），直接点燃全球AI算力链。A股三大指数单边上扬，<strong style="color:#ef4444;">科创50暴涨3.77%</strong>领跑全场，半导体/CPO/PCB/存储全线爆发。</p>
<p><strong style="color:#10b981;">📊 量价齐升格局确认：</strong>两市成交2.13万亿放量3172亿，主力资金净流入589亿连续3日净流入，电子板块单日吸金398亿。全市场3394只上涨、77只涨停、仅4只跌停，赚钱效应大幅回暖，恐贪指数从8/19冰点27.3修复至61.5。</p>
<p><strong style="color:#60a5fa;">💼 持仓4只表现亮眼：</strong>英维克+6.28%、铜冠铜箔+6.22%、雅克科技+6.42%，三大持仓均大涨6%+；*ST建艺-1.46%继续地量阴跌。持仓组合今日暴力回血。</p>
<p><strong style="color:#a855f7;">⚠️ 风格剧烈切换：</strong>银行-1.04%、电力设备-0.71%、阳光电源-12.24%、思源电气跌停，资金从防御板块大举撤出转攻科技主线。</p>
</div>
""")

# ============ 2. 市场收盘总结 ============
gen.add_market_summary(
    indices=[
        {"name":"上证指数","value":"3,956.57","change":"+1.13% (+44.05)","up":True,"icon":"trending_up"},
        {"name":"深证成指","value":"14,048.88","change":"+1.50% (+207.55)","up":True,"icon":"trending_up"},
        {"name":"创业板指","value":"3,473.35","change":"+1.71% (+58.47)","up":True,"icon":"trending_up"},
        {"name":"科创50","value":"1,693.48","change":"+3.77% (+61.46)","up":True,"icon":"rocket_launch"},
    ],
    volume="2.13万亿（+3172亿）",
    northbound="净买入约62亿"
)

# ============ 3. 盘面深度解读 ============
gen.add_market_deep_analysis(
    strong_sectors=[
        {"name":"半导体/芯片（+5.13%，主力净买496亿）","reason":"英伟达财报直接催化+1-7月集成电路利润暴增18.5倍双轮驱动。赛微电子、昂瑞微、晶丰明源20cm涨停，澜起科技+10.06%、兆易创新+4.76%、长鑫科技放量走强、中芯国际+1.76%。半导体板块成交2881亿居全市场之首，设备/材料/设计/封测/存储全链条爆发，是今日行情绝对主力。"},
        {"name":"CPO/光通信（+5.33%，主力净买296亿）","reason":"英伟达Vera Rubin平台开始发货，CPO交换机进入商业化元年。赛微电子20cm涨停，长飞光纤涨停（净买18.61亿），亨通光电+9.98%，杭电股份2连板，法尔胜涨停。但高位核心\"易中天\"相对克制：中际旭创+1.79%、新易盛+2.59%、天孚通信+5.36%，显示资金从核心向二线扩散补涨。"},
        {"name":"PCB/覆铜板/铜箔（+5.09%，元件主力净买125亿）","reason":"AI服务器高层板需求沿产业链向上游材料传导。金安国纪、宏昌电子、嘉立创、协和电子、昊华科技集体涨停，生益科技+8.43%（净买24.15亿居全市场首位）、胜宏科技+（净买19.55亿）、深南电路+4.90%、沪电股份+2.35%。铜冠铜箔+6.22%跟随板块上涨，PCB龙头中报高增提供业绩背书。"},
        {"name":"存储芯片/HBM（板块涨停潮）","reason":"英伟达与三星/SK海力士/美光三大存储厂达成深度长期合作，8层HBM4供应放量，存储价格上行趋势延续。德明利涨停（净买7.36亿、机构净买5.99亿）、大普微20cm涨停（机构净买4342万）、江波龙+6.05%、澜起科技+10%，雅克科技+6.42%作为HBM前驱体龙头获资金认可。"},
        {"name":"贵金属/农业（防御补涨）","reason":"黄金受美债收益率新高+美元信用担忧催化，东方钽业涨停（净买2.88亿），湖南黄金涨停。农业受全球粮价上涨+FAO指数连涨三月催化，万向德农3连板，金健米业9天6板，神农种业+9.05%。属于非AI方向的辅助主线。"},
    ],
    weak_sectors=[
        {"name":"银行（-1.04%，主力净流出39亿）","reason":"前期防御抱团资金大幅兑现，风格切换的典型标志。华夏银行、民生银行跌超2%，银行股是今日调整最深的板块，显示资金风险偏好明显回升，从高股息防御转向科技成长进攻。"},
        {"name":"电力设备/光伏（-0.71%，主力净流出34亿）","reason":"阳光电源单日暴跌-12.24%，思源电气跌停，电网设备板块情绪承压。宁德时代主力净流出13.98亿，新能源赛道在风格切换中遭遇资金抛售，但属于短期情绪波动，长期逻辑未破坏。"},
        {"name":"食品饮料/白酒（小幅调整）","reason":"五粮液主力净流出5.42亿，消费白马在科技主线虹吸效应下被资金阶段性冷落。白酒板块前期防御属性较强，今日风险偏好提升后资金流出属于正常轮动。"},
    ],
    core_view="""<strong style="font-size:15px;">🎯 核心观点：放量突破确立，AI算力主升浪重启</strong><br><br>
今日行情不是简单的超跌反弹，而是<strong style="color:#ef4444;">\"产业催化+业绩验证+资金共识\"三重共振</strong>下的趋势性突破：①英伟达Q2/Q3/2028三档指引全面超预期，全球AI算力资本开支上修逻辑得到硬数据确认；②国内1-7月集成电路利润同比+18.5倍，电子行业利润翻倍，基本面与海外映射共振；③两市成交时隔多日重回2.13万亿，主力连续3日净流入，电子板块单日吸金近400亿，增量资金入场信号明确。<br><br>
<strong>技术面看</strong>，沪指3900点支撑确认有效，科创50单日+3.77%放量突破1650-1680平台压力位，向上空间打开。今日与8/19暴跌-6.26%形成鲜明对照，8个交易日内恐贪指数从27.3冰点修复至61.5，V型反转结构清晰。<br><br>
<strong>风格判断</strong>，市场从\"缩量防御\"正式切换为\"放量进攻\"，科技成长主线确立，短期应顺势而为，仓位向AI算力链（半导体设备/PCB/HBM/CPO）集中，但需警惕明日高开冲高后的分化回踩，切忌追高。
"""
)

# ============ 4. 板块涨跌幅排行（更详细版，补充数据） ============
# 我们用更详细的自定义板块分析，所以直接使用add_market_deep_analysis覆盖
# 但为满足质量要求"板块分析≥5个"，上面已经有5+3=8个板块，足够
# 额外加一个板块资金流向的卡片
from components.layout import Section
from components.special import NewsItem

sector_html = '''
<div style="display:grid; grid-template-columns: repeat(2, 1fr); gap:14px;">
'''
sectors_data = [
    ("半导体/芯片", "+5.13%", "+496.1亿", "赛微电子/昂瑞微/晶丰明源/大普微20cm涨停", "#ef4444", True),
    ("PCB/覆铜板", "+5.09%", "+125.2亿", "生益科技+8.43%净买24亿/金安国纪/嘉立创/宏昌电子涨停", "#f97316", True),
    ("CPO/光通信", "+5.33%", "+296.1亿", "长飞光纤涨停/亨通光电+9.98%/赛微电子20cm", "#f59e0b", True),
    ("存储/HBM", "涨停潮", "+173.7亿", "德明利涨停机构净买6亿/大普微20cm/澜起科技+10%", "#eab308", True),
    ("电子化学品", "领涨", "+80亿+", "昊华科技涨停/联瑞新材20cm机构净买1.2亿", "#84cc16", True),
    ("通信设备", "+3.39%", "+101.3亿", "星网锐捷涨停机构净买7173万", "#22c55e", True),
    ("银行", "-1.04%", "-39亿", "华夏/民生银行-2%+/资金兑现防御仓位", "#10b981", False),
    ("电力设备/光伏", "-0.71%", "-34亿", "阳光电源-12.24%/思源电气跌停", "#06b6d4", False),
    ("食品饮料/白酒", "-0.48%", "流出", "五粮液净卖5.4亿/资金轮动至科技", "#3b82f6", False),
    ("贵金属", "涨停潮", "流入", "东方钽业/湖南黄金涨停/避险+工业属性双击", "#8b5cf6", True),
]
for name, chg, flow, leader, color, up in sectors_data:
    bg = "rgba(16,185,129,0.08)" if up else "rgba(239,68,68,0.08)"
    border = "rgba(16,185,129,0.25)" if up else "rgba(239,68,68,0.25)"
    arrow = "📈" if up else "📉"
    sector_html += f'''
    <div style="background:{bg}; border:1px solid {border}; border-radius:12px; padding:14px;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
            <span style="font-weight:600; font-size:14px; color:#f1f5f9;">{arrow} {name}</span>
            <span style="font-weight:700; font-size:15px; color:{color};">{chg}</span>
        </div>
        <div style="font-size:12px; color:#94a3b8; margin-bottom:4px;">主力净流入：{flow}</div>
        <div style="font-size:12px; color:#cbd5e1; line-height:1.5;">龙头：{leader}</div>
    </div>'''
sector_html += "</div>"
gen._components.append(Section(title="🏢 板块资金流向全景", content=sector_html, icon="building"))

# ============ 5. 持仓股深度诊断 ============
from components.data import StockTags

# 持仓股分析（4只，每只≥300字，具体到点位）
holdings = [
    {
        "name": "英维克",
        "code": "002837",
        "price": "65.97",
        "change": "+6.28%",
        "up": True,
        "turnover": "约6.0%（成交68.45亿）",
        "volume": "成交1.07亿股",
        "tag_color": "#f59e0b",
        "tag_text": "🟡 液冷超跌反弹",
        "analysis": """
<strong style="color:#f59e0b;">📊 今日表现</strong>：英维克今日开盘62.6元，最低探61.48后震荡走高，最高触及66.0元（涨停价附近），收盘65.97元大涨+6.28%，全天振幅7.31%，成交额68.45亿，换手率约13-15%（实际约6%流通盘计）。量能较前期明显放大，属于液冷板块跟随AI算力链的超跌反弹修复。<br><br>
<strong style="color:#60a5fa;">🔍 技术面判断</strong>：英维克从高点170元持续下跌至50.78元（7/29低点），最大回撤-70%，经历了漫长的下降通道。今日跟随AI算力主线强势反弹，收复5日均线（约62元）和10日均线（约63元），但60元下方仍属弱势反弹区，20日均线（约68元）、60日均线（约72元）将构成上方强压力。MACD在零轴下方金叉初现，但KDJ已进入超买区域，短期反弹持续性需观察。<br><br>
<strong style="color:#ef4444;">💰 资金面</strong>：液冷服务器/算力基础设施板块整体反弹，主力资金净流入英维克约2-3亿（估算），但对比历史套牢盘仍然较少。从资金博弈看，今日是机构超跌反弹减仓与游资短线博弈共存。<br><br>
<strong style="color:#10b981;">🎯 操作建议</strong>：英维克深度破止损（成本104.23元，当前浮亏-36.7%），下降趋势未根本扭转，<strong style="color:#ef4444;">反弹至68-70元区间坚决减仓1/2</strong>，若放量突破72元（60日线）可留1/4底仓博弈；<strong style="color:#ef4444;">二次跌破62元减半仓，跌破58元无条件清仓</strong>。严禁补仓抄底，液冷板块相对半导体/PCB强度明显偏弱，非当前主线核心。
        """,
        "support": "62元（5日线）/ 58元（前低）",
        "pressure": "68元（20日线）/ 72元（60日线）",
        "action": "反弹68-70元减仓1/2，破58清仓"
    },
    {
        "name": "铜冠铜箔",
        "code": "301217",
        "price": "114.53",
        "change": "+6.22%",
        "up": True,
        "turnover": "约5.9%（成交42.07亿）",
        "volume": "成交3754万股",
        "tag_color": "#10b981",
        "tag_text": "🟢 PCB铜箔核心标的",
        "analysis": """
<strong style="color:#10b981;">📊 今日表现</strong>：铜冠铜箔今日开盘110.03元（高开2.05%），最低回踩106.8元（10日线附近）获得强支撑后快速拉升，最高冲115.36元，收盘114.53元大涨+6.22%，全天振幅7.97%，成交额42.07亿，换手率约5.9%（以6.34亿流通盘计）。作为PCB/覆铜板上游铜箔核心标的，铜冠铜箔今日跟随PCB涨停潮同步大涨，但未涨停显示资金仍有分歧。<br><br>
<strong style="color:#60a5fa;">🔍 技术面判断</strong>：铜冠铜箔从高点202元跌至83.12元（7/29），最大回撤-58.8%，经历深度调整后企稳反弹。今日放量突破110元短期压力，5日/10日/20日均线呈多头排列（约104-108元），MACD零轴下方金叉向上，KDJ在60-70区间尚未超买。120元是前期反弹高点（8/7创出115.81后回落），将构成第一压力位；130元是7月密集成交区，将构成第二压力位。<br><br>
<strong style="color:#ef4444;">💰 资金面</strong>：铜箔/覆铜板板块今日整体吸金，生益科技净买24亿、胜宏科技19.55亿，铜冠铜箔主力净流入约3-5亿（估算）。PCB上游材料是今日资金共识度最高的方向之一，铜冠铜箔作为铜箔龙头直接受益。<br><br>
<strong style="color:#f59e0b;">🎯 操作建议</strong>：当前浮盈+31.4%（成本87.16元），PCB上游材料是本轮行情核心受益方向，逻辑硬、资金共识强。<strong style="color:#10b981;">建议持有至120元附近减仓1/3锁定利润</strong>，若放量突破120元并站稳则留1/2底仓博弈130元；<strong style="color:#ef4444;">回踩108-110元（20日线）可小仓位加仓</strong>，跌破105元（10日线）减仓至底仓，跌破100元全部止盈离场。
        """,
        "support": "108元（20日线）/ 105元（10日线）",
        "pressure": "120元（前高）/ 130元（密集成交区）",
        "action": "120元减1/3锁利，回踩108-110可加仓"
    },
    {
        "name": "雅克科技",
        "code": "002409",
        "price": "143.91",
        "change": "+6.42%",
        "up": True,
        "turnover": "约4.5%（成交28.07亿）",
        "volume": "成交1989万股",
        "tag_color": "#10b981",
        "tag_text": "🟢 HBM前驱体龙头",
        "analysis": """
<strong style="color:#10b981;">📊 今日表现</strong>：雅克科技开盘137.03元（高开1.33%），最低136.15元获得支撑后持续走高，最高封至144.0元涨停价，收盘143.91元大涨+6.42%，全天振幅5.83%，成交额28.07亿，换手率约4.5%（以4.47亿流通盘计）。HBM前驱体龙头直接受益于英伟达8层HBM4放量消息，半导体材料板块整体爆发。<br><br>
<strong style="color:#60a5fa;">🔍 技术面判断</strong>：雅克科技从历史高点229元（7/10）回调至132元（7/21），最大回撤-42.4%，深度调整后逐步企稳。今日放量收复140元整数关口，5日/10日/20日均线粘合于135-138元区间形成强支撑，MACD在零轴下方金叉且红柱放大，KDJ金叉向上发散至60-70区间。上方第一压力位148-150元（前期平台），第二压力位155元（7月平台）。<br><br>
<strong style="color:#ef4444;">💰 资金面</strong>：半导体材料板块今日集体走强，联瑞新材20cm涨停机构净买1.2亿，雅克科技作为HBM前驱体绝对龙头获机构资金重点加仓，主力净流入约3-4亿（估算）。英伟达与三大存储厂签订HBM长期供应协议，雅克科技前驱体材料直接受益于HBM4放量。<br><br>
<strong style="color:#f59e0b;">🎯 操作建议</strong>：当前浮盈+32.3%（成本108.8元），HBM前驱体是本轮AI算力链逻辑最硬的方向之一。<strong style="color:#10b981;">建议继续持有为主，148-150元区间减仓1/3锁利</strong>，若放量突破150元可加仓至6成博弈155-160元；<strong style="color:#ef4444;">回踩138-140元（20日线）可加仓</strong>，跌破135元减仓至1/3底仓，跌破130元全部止盈。
        """,
        "support": "138元（20日线）/ 135元（支撑）",
        "pressure": "150元（平台压力）/ 155元（前高）",
        "action": "148-150减1/3锁利，回踩138-140加仓"
    },
    {
        "name": "*ST建艺",
        "code": "002789",
        "price": "10.15",
        "change": "-1.46%",
        "up": False,
        "turnover": "约1.5%（成交1590万）",
        "volume": "成交157万股",
        "tag_color": "#ef4444",
        "tag_text": "🚨 退市风险股",
        "analysis": """
<strong style="color:#ef4444;">📊 今日表现</strong>：*ST建艺今日开盘10.21元，最高10.28元，最低10.06元，收盘10.15元下跌-1.46%，全天振幅仅2.14%，成交额仅1590万元，换手率约1.5%。继续地量阴跌，在科技主线全面爆发的市场环境下，ST股被资金彻底抛弃，与市场完全脱节。<br><br>
<strong style="color:#60a5fa;">🔍 技术面判断</strong>：*ST建艺从13.45元（成本）持续阴跌至8元附近，目前在10元左右震荡，日K线沿5日均线持续下行，所有均线呈空头排列，MACD在零轴下方死叉，无任何企稳信号。成交量持续萎缩至地量，流动性濒临枯竭。<br><br>
<strong style="color:#ef4444;">💰 资金面</strong>：无主力资金介入，散户交易为主，成交极度低迷。ST板块在市场行情向好时往往被抛弃，资金追逐高弹性科技股。退市风险+债务问题+诉讼三大雷未解，无资金愿意接盘。<br><br>
<strong style="color:#ef4444;">🎯 操作建议（最高优先级）</strong>：<strong style="color:#ef4444; font-size:15px;">明日任何价格立即清仓止损！</strong>当前浮亏-24.5%（成本约13.45元），退市风险敞口必须关闭。科技主线行情下ST股流动性只会越来越差，不要有任何幻想，不要等反弹，不要补仓摊低成本，<strong>集合竞价直接挂跌停价清仓</strong>，将资金转移至科技主线标的。
        """,
        "support": "10元（心理关口）/ 9.8元",
        "pressure": "10.3元（5日线）/ 10.5元",
        "action": "明日开盘立即清仓（最高优先级）"
    },
]

# 自定义持仓诊断HTML（因为需要更详细的分析）
holdings_html = '<div style="display:flex; flex-direction:column; gap:16px;">'
for h in holdings:
    change_color = "#10b981" if h['up'] else "#ef4444"
    holdings_html += f'''
    <div style="background: var(--glass-bg); border: 1px solid var(--glass-border); border-radius: 16px; padding: 20px; backdrop-filter: blur(10px);">
        <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:14px; flex-wrap:wrap; gap:10px;">
            <div>
                <span style="font-size:18px; font-weight:700; color:#f1f5f9;">{h['name']}</span>
                <span style="font-size:13px; color:#94a3b8; margin-left:8px;">{h['code']}</span>
                <span style="font-size:12px; padding:3px 10px; border-radius:12px; background:{h['tag_color']}22; color:{h['tag_color']}; margin-left:10px; font-weight:600;">{h['tag_text']}</span>
            </div>
            <div style="text-align:right;">
                <div style="font-size:22px; font-weight:700; color:{change_color};">{h['price']}元</div>
                <div style="font-size:14px; font-weight:600; color:{change_color};">{h['change']}</div>
            </div>
        </div>
        <div style="display:grid; grid-template-columns: repeat(3, 1fr); gap:10px; margin-bottom:14px; font-size:12px;">
            <div style="background:rgba(255,255,255,0.04); border-radius:8px; padding:8px 10px;">
                <div style="color:#94a3b8; margin-bottom:2px;">成交量额</div>
                <div style="color:#e2e8f0; font-weight:600;">{h['turnover']}</div>
            </div>
            <div style="background:rgba(255,255,255,0.04); border-radius:8px; padding:8px 10px;">
                <div style="color:#94a3b8; margin-bottom:2px;">支撑位</div>
                <div style="color:#10b981; font-weight:600;">{h['support']}</div>
            </div>
            <div style="background:rgba(255,255,255,0.04); border-radius:8px; padding:8px 10px;">
                <div style="color:#94a3b8; margin-bottom:2px;">压力位</div>
                <div style="color:#ef4444; font-weight:600;">{h['pressure']}</div>
            </div>
        </div>
        <div style="font-size:13.5px; color:#cbd5e1; line-height:1.8;">{h['analysis']}</div>
        <div style="margin-top:12px; padding:10px 14px; background:rgba(245,158,11,0.1); border-left:3px solid #f59e0b; border-radius:0 8px 8px 0; font-size:13px; color:#fbbf24; font-weight:600;">
            📌 操作建议：{h['action']}
        </div>
    </div>'''
holdings_html += "</div>"
gen._components.append(Section(title="💼 持仓股深度诊断（4只）", content=holdings_html, icon="briefcase"))

# ============ 6. 龙虎榜深度解读 ============
lhb_html = '''
<div style="margin-bottom:14px; padding:14px; background:rgba(99,102,241,0.1); border-radius:12px; border:1px solid rgba(99,102,241,0.25); font-size:13px; color:#c7d2fe; line-height:1.7;">
<strong style="color:#a5b4fc;">🐉 龙虎榜概况：</strong>今日共58只个股上榜，涨停29只/跌停3只。龙虎榜净买入总额<strong style="color:#10b981;">33.71亿元</strong>，其中机构席位净买入<strong style="color:#10b981;">8.53亿</strong>，北向资金净买2.13亿，游资席位净买25.18亿。市场情绪极度活跃（评分90），机构+游资+北向三线共振做多，集中涌入科技成长方向。
</div>
<div style="display:flex; flex-direction:column; gap:14px;">
'''

lhb_stocks = [
    {
        "name":"德明利","code":"001309","price":"429.76","change":"+10.00%（涨停）",
        "reason":"日涨幅偏离值达7%（存储芯片龙头）","net_buy":"7.36亿","inst_net":"+5.99亿（机构大幅净买）",
        "turnover":"87.62亿","turnover_rate":"12.72%",
        "analysis":"存储芯片绝对龙头，今日一字涨停封死，龙虎榜显示<strong style='color:#10b981;'>3家机构席位净买入5.99亿</strong>，占净买总额的81%，属于机构主导型涨停。德明利二季度净利润环比有所下滑引发前期调整（7/15一字跌停），但本次受益于英伟达HBM4长期合作+存储涨价超预期，机构大举回补。筹码从游资炒作转向机构配置，<strong style='color:#f59e0b;'>持续性较强，可关注明日开板后的低吸机会</strong>，但429元高位追涨风险较大，回踩380-400元区间可关注。止损位360元。",
        "sustainability":"⭐⭐⭐⭐⭐（机构主导，持续性强）"
    },
    {
        "name":"联瑞新材","code":"688300","price":"106.80","change":"+20.00%（20cm涨停）",
        "reason":"日涨幅偏离值达7%（电子化学品/硅微粉龙头）","net_buy":"1.34亿","inst_net":"+1.20亿（机构净买1.2亿）",
        "turnover":"37.70亿","turnover_rate":"9.04%",
        "analysis":"电子化学品/球形硅微粉龙头，20cm涨停，<strong style='color:#10b981;'>2家机构席位净买入1.2亿</strong>，占净买额的90%，机构主导封板。联瑞新材的球形硅微粉用于HBM封装填料，直接受益于HBM4放量+先进封装国产化，是半导体材料分支的隐形冠军。机构大举扫货显示对HBM材料链的中长期看好。<strong style='color:#f59e0b;'>持续性强</strong>，明日若高开不超5%可关注，回调至95元附近可低吸，目标价120元，止损位88元。",
        "sustainability":"⭐⭐⭐⭐⭐（机构+题材双驱动）"
    },
    {
        "name":"金安国纪","code":"002636","price":"69.41","change":"+10.00%（涨停）",
        "reason":"日涨幅偏离值达7%（覆铜板龙头）","net_buy":"2.75亿","inst_net":"+1859万（小量机构参与）",
        "turnover":"34.80亿","turnover_rate":"7.15%",
        "analysis":"覆铜板（CCL）龙头，涨停封板，龙虎榜显示<strong style='color:#f59e0b;'>1家机构净买1860万+游资主导</strong>，属于游资主导的PCB上游材料涨停。金安国纪是国内覆铜板二线龙头，直接受益于AI服务器高层板需求爆发。但机构参与度较低，主要是游资打板，<strong style='color:#ef4444;'>持续性存疑</strong>，明日开板后不建议追高，可等待回调至60-62元区间观察。相比之下，生益科技+8.43%机构净买24亿更具持续性。",
        "sustainability":"⭐⭐⭐（游资主导，谨慎追高）"
    },
    {
        "name":"大普微","code":"301666","price":"117.68","change":"+20.00%（20cm涨停）",
        "reason":"日涨幅偏离值达7%（企业级SSD存储芯片）","net_buy":"2.03亿","inst_net":"+4342万（机构小幅净买）",
        "turnover":"9.62亿","turnover_rate":"7.81%",
        "analysis":"企业级SSD主控+存储模组芯片标的，20cm涨停，1家机构净买4342万，游资参与为主。大普微是存储芯片板块的20cm弹性标的，受益于AI服务器企业级SSD需求爆发。<strong style='color:#f59e0b;'>弹性大但波动也大</strong>，适合风险偏好高的投资者短线博弈，回调至100元附近可关注，止损位90元。",
        "sustainability":"⭐⭐⭐⭐（存储题材+弹性标的）"
    },
    {
        "name":"思源电气","code":"002028","price":"36.50（跌停）","change":"-10.00%（跌停）",
        "reason":"日跌幅偏离值达7%（电网设备）","net_buy":"-1.25亿","inst_net":"-1.25亿（机构大幅净卖）",
        "turnover":"—","turnover_rate":"—",
        "analysis":"电网设备龙头跌停，<strong style='color:#ef4444;'>机构席位净卖出1.25亿</strong>，属于资金从电网设备/新能源方向大举撤离的典型信号。阳光电源-12.24%、宁德时代净卖14亿，整个电力设备/新能源板块遭遇集中抛售。思源电气跌停显示机构在风格切换中坚决调仓，<strong style='color:#ef4444;'>短期规避电力设备/光伏/电网方向</strong>，资金已明确转向科技成长。",
        "sustainability":"⚠️ 机构大幅抛售，短期规避"
    },
]

for s in lhb_stocks:
    is_up = "跌停" not in s['change'] and "-10" not in s['change']
    color = "#10b981" if is_up else "#ef4444"
    lhb_html += f'''
    <div style="background: rgba(30,30,50,0.5); border:1px solid rgba(255,255,255,0.08); border-radius:14px; padding:18px;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;">
            <div>
                <span style="font-size:16px; font-weight:700; color:#f1f5f9;">{s['name']}</span>
                <span style="font-size:12px; color:#94a3b8; margin-left:6px;">{s['code']}</span>
                <span style="font-size:11px; padding:2px 8px; border-radius:10px; background:rgba(99,102,241,0.15); color:#a5b4fc; margin-left:8px;">{s['sustainability']}</span>
            </div>
            <span style="font-size:17px; font-weight:700; color:{color};">{s['change']}</span>
        </div>
        <div style="display:flex; gap:12px; font-size:12px; color:#94a3b8; margin-bottom:10px; flex-wrap:wrap;">
            <span>📋 上榜原因：{s['reason']}</span>
            <span>💰 净买入：<strong style="color:{color};">{s['net_buy']}</strong></span>
            <span>🏛️ {s['inst_net']}</span>
        </div>
        <div style="font-size:13px; color:#cbd5e1; line-height:1.75;">{s['analysis']}</div>
    </div>'''

lhb_html += "</div>"
gen._components.append(Section(title="🐉 龙虎榜深度解读（5只）", content=lhb_html, icon="award"))

# ============ 7. 重点关注标的（3只非持仓股） ============
watch_html = '<div style="display:flex; flex-direction:column; gap:14px;">'

watch_stocks = [
    {
        "name":"生益科技","code":"600183","price":"42.63","change":"+8.43%","sector":"覆铜板/PCB上游",
        "logic":"""全球第二大覆铜板龙头，AI服务器高层板核心受益标的。龙虎榜主力资金净买入<strong style='color:#10b981;'>24.15亿元</strong>居全市场首位，机构大举扫货。中报业绩高增验证：沪电/深南/天津普林等PCB厂商业绩全部大超预期，生益科技作为上游材料龙头业绩弹性最大。今日+8.43%放量突破，量价配合完美，属于PCB板块中军。""",
        "target":"第一目标48元（+12.6%），第二目标55元（+29%）",
        "stop_loss":"跌破38元（10日线）止损",
        "action":"回调至40-41元区间逢低买入，仓位10-15%"
    },
    {
        "name":"澜起科技","code":"688008","price":"83.50","change":"+10.06%","sector":"内存接口芯片/HBM",
        "logic":""""全球内存接口芯片（DDR5 RCD/MRCD/MDB）绝对龙头，HBM配套芯片核心供应商。今日+10.06%逼近涨停，直接受益于英伟达HBM4放量+全球AI服务器DDR5渗透加速。澜起科技是内存接口芯片全球三巨头之一，HBM4时代需要更多MRCD/MDB芯片配套，单机价值量翻倍。机构今日大举加仓，科创板芯片中军，流动性好、业绩确定性强。""",
        "target":"第一目标92元（+10.2%），第二目标105元（+25.7%）",
        "stop_loss":"跌破75元（20日线）止损",
        "action":"回调至78-80元区间建仓，仓位10%"
    },
    {
        "name":"胜宏科技","code":"300476","price":"约56元（估算）","change":"约+7%","sector":"HDI/高端PCB",
        "logic":"""AI服务器HDI板核心供应商，主力资金净买入<strong style='color:#10b981;'>19.55亿元</strong>居全市场第二，机构+游资合力买入。胜宏科技是AI服务器GPU载板、高层高密HDI核心供应商，直接受益于英伟达Vera Rubin平台放量。相比沪电/深南，胜宏科技市值更小、弹性更大，机构目标价一致上看70元+。""",
        "target":"第一目标62元（+10.7%），第二目标70元（+25%）",
        "stop_loss":"跌破50元止损",
        "action":"回调至52-53元区间建仓，仓位8-10%"
    },
]

for s in watch_stocks:
    watch_html += f'''
    <div style="background: linear-gradient(135deg, rgba(59,130,246,0.08) 0%, rgba(139,92,246,0.06) 100%); border:1px solid rgba(59,130,246,0.2); border-radius:14px; padding:18px;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;">
            <div>
                <span style="font-size:16px; font-weight:700; color:#f1f5f9;">{s['name']}</span>
                <span style="font-size:12px; color:#94a3b8; margin-left:6px;">{s['code']}</span>
                <span style="font-size:11px; padding:2px 8px; border-radius:10px; background:rgba(59,130,246,0.15); color:#60a5fa; margin-left:8px;">{s['sector']}</span>
            </div>
            <span style="font-size:16px; font-weight:700; color:#10b981;">{s['price']}元 {s['change']}</span>
        </div>
        <div style="font-size:13px; color:#cbd5e1; line-height:1.75; margin-bottom:12px;">{s['logic']}</div>
        <div style="display:grid; grid-template-columns: repeat(3, 1fr); gap:10px; font-size:12px;">
            <div style="background:rgba(16,185,129,0.08); border-radius:8px; padding:8px 10px;">
                <div style="color:#6ee7b7; margin-bottom:2px;">🎯 目标价</div>
                <div style="color:#10b981; font-weight:600;">{s['target']}</div>
            </div>
            <div style="background:rgba(239,68,68,0.08); border-radius:8px; padding:8px 10px;">
                <div style="color:#fca5a5; margin-bottom:2px;">🛑 止损位</div>
                <div style="color:#ef4444; font-weight:600;">{s['stop_loss']}</div>
            </div>
            <div style="background:rgba(245,158,11,0.08); border-radius:8px; padding:8px 10px;">
                <div style="color:#fcd34d; margin-bottom:2px;">📌 买入策略</div>
                <div style="color:#f59e0b; font-weight:600;">{s['action']}</div>
            </div>
        </div>
    </div>'''
watch_html += "</div>"
gen._components.append(Section(title="🔭 重点关注标的（3只）", content=watch_html, icon="star"))

# ============ 8. 晚间重要新闻 ============
news_list = [
    {"title":"英伟达Q2财报全面炸裂：营收962亿同比+106%，2028财年指引增速70%","content":"英伟达2027财年Q2营收962.2亿美元（同比+106%，环比+18%），大超预期923.8亿；数据中心收入890亿（+117%）；毛利率75%；Q3营收指引中值1080亿美元首破千亿；2028财年营收增速指引约70%（大超市场预期45%）。CFO透露Vera Rubin平台已开始发货，存储芯片短缺将持续制约增长至2028年。","time":"08-27 04:30","source":"英伟达财报","tag":"S级催化","tag_variant":"danger"},
    {"title":"国家统计局：1-7月电子行业利润增长1.1倍，集成电路利润暴增18.5倍","content":"1-7月全国规上工业企业利润同比+17.6%，7月当月+11.2%。其中电子行业利润同比+110%，拉动规上工业利润增长9.3个百分点；集成电路行业利润同比+1850%，对电子行业利润增长贡献率超80%。算力芯片+存储芯片是核心增长引擎。","time":"08-27 09:30","source":"国家统计局","tag":"业绩验证","tag_variant":"success"},
    {"title":"国务院《深入实施「人工智能+」行动意见》落地","content":"国务院发布《关于深入实施「人工智能+」行动的意见》，提出到2027年AI与六大重点领域融合普及率超70%、2030年超90%，首次将智能终端普及率写入政府KPI。华泰证券认为是继「互联网+」之后国家层面推动产业变革的纲领性文件。","time":"08-26/27","source":"国务院","tag":"政策利好","tag_variant":"primary"},
    {"title":"央行开展1000亿3个月国库现金定存，中标利率1.67%","content":"2026年第13期中央国库现金管理商业银行定期存款招标完成，中标总量1000亿元，期限3个月，中标利率1.67%。维持流动性合理充裕。","time":"08-27 15:28","source":"央行","tag":"流动性","tag_variant":"default"},
    {"title":"智谱OxAlpha模型用量达DeepSeek两倍，GLM-5.3并列开源全球第一","content":"智谱正式认领神秘AI模型OxAlpha，市场使用量已达DeepSeek两倍；GLM-5.3在ArtificialAnalysis指数拿到60分，与KimiK3并列开源模型全球第一，国产大模型竞争力快速向全球第一梯队靠拢。","time":"08-27","source":"36氪","tag":"AI应用","tag_variant":"default"},
    {"title":"阳光电源暴跌12.24%，思源电气跌停，新能源赛道遭集中抛售","content":"电力设备/光伏板块今日大幅调整，阳光电源-12.24%，思源电气跌停，宁德时代主力净卖13.98亿。市场风格剧烈切换，资金从新能源防御方向大举撤离转攻科技主线。","time":"08-27 15:00","source":"财联社","tag":"风格切换","tag_variant":"warning"},
]
gen.add_evening_news(news_list)

# ============ 9. 情绪温度计 ============
gen.add_sentiment_thermometer(
    temperature=61.5,
    volume="2.13万亿（+3172亿）",
    up_count="3394只↑（61.2%）",
    down_count="1944只↓",
    limit_up_count="77家涨停"
)

# ============ 10. 明日操作策略 ============
plan_html = '''
<div style="background: linear-gradient(135deg, rgba(16,185,129,0.1) 0%, rgba(59,130,246,0.08) 100%); border:1px solid rgba(16,185,129,0.25); border-radius:16px; padding:22px; font-size:13.5px; line-height:1.85; color:#cbd5e1;">

<h4 style="color:#10b981; font-size:15px; margin:0 0 12px 0;">🎯 大盘判断：放量突破确立，顺势做多科技主线</h4>
<p>今日沪指放量+1.13%站稳3950，科创50暴涨+3.77%，两市成交重回2.13万亿，主力连续3日净流入589亿，从"缩量修复"正式切换为"放量上攻"。英伟达财报+国内集成电路利润暴增+国务院AI+政策三重共振，科技主升浪确认。但明日是周五，需警惕高开冲高后的获利回吐，操作上不宜追高，等待回调加仓。</p>

<h4 style="color:#f59e0b; font-size:15px; margin:16px 0 12px 0;">📊 仓位建议：6-7成仓位，集中科技主线</h4>
<ul style="padding-left:20px; margin:0;">
<li><strong style="color:#f1f5f9;">底仓（4成）：</strong>雅克科技（HBM前驱体）+ 铜冠铜箔（PCB铜箔），这两只持仓逻辑硬、资金共识强、中报有支撑，坚定持有</li>
<li><strong style="color:#f1f5f9;">机动仓（2-3成）：</strong>PCB（生益科技/胜宏科技）+ 半导体设备/材料（澜起科技/联瑞新材方向）</li>
<li><strong style="color:#f1f5f9;">现金（3-4成）：</strong>保留子弹等待回调加仓机会，*ST建艺清仓后释放的资金优先用于科技方向</li>
</ul>

<h4 style="color:#ef4444; font-size:15px; margin:16px 0 12px 0;">📋 具体买卖计划</h4>
<div style="display:grid; gap:10px;">
<div style="background:rgba(239,68,68,0.08); border-radius:10px; padding:10px 14px; border-left:3px solid #ef4444;">
<strong style="color:#fca5a5;">🚨 立即执行（明日开盘）：</strong>*ST建艺（002789）集合竞价挂跌停价<strong>清仓全部卖出</strong>，不抱任何幻想，释放资金
</div>
<div style="background:rgba(245,158,11,0.08); border-radius:10px; padding:10px 14px; border-left:3px solid #f59e0b;">
<strong style="color:#fcd34d;">⚡ 持仓操作：</strong>
①<strong>英维克</strong>：反弹至68-70元减仓1/2，二次破62元减仓，破58元无条件清仓；
②<strong>铜冠铜箔</strong>：120元减仓1/3锁利，回踩108-110元可加仓，跌破105元减仓；
③<strong>雅克科技</strong>：148-150元减仓1/3锁利，回踩138-140元加仓，跌破135元减仓至底仓
</div>
<div style="background:rgba(16,185,129,0.08); border-radius:10px; padding:10px 14px; border-left:3px solid #10b981;">
<strong style="color:#6ee7b7;">🟢 新建仓（回调买入）：</strong>
①<strong>生益科技</strong>：回调至40-41元买入10-15%仓位，目标48/55元，止损38元；
②<strong>澜起科技</strong>：回调至78-80元买入10%仓位，目标92/105元，止损75元；
③<strong>胜宏科技</strong>：回调至52-53元买入8-10%仓位，目标62/70元，止损50元
</div>
<div style="background:rgba(99,102,241,0.08); border-radius:10px; padding:10px 14px; border-left:3px solid #818cf8;">
<strong style="color:#c7d2fe;">🔄 明日重点观察：</strong>
①德明利/联瑞新材等涨停股开盘溢价幅度（判断板块强度）；
②英伟达今晚美股走势（盘后已涨4%+）；
③两市成交额能否维持2万亿以上；
④银行/新能源是否继续调整（确认风格切换）
</div>
</div>

<h4 style="color:#a855f7; font-size:15px; margin:16px 0 12px 0;">🔮 未来一周催化</h4>
<ul style="padding-left:20px; margin:0;">
<li>8/28周五：美联储主席鲍威尔在杰克逊霍尔年会讲话（降息信号）</li>
<li>8/31-9/1：中报密集披露最后窗口期（注意避雷）</li>
<li>9月初：8月PMI数据公布</li>
<li>持续：英伟达供应链订单向中国PCB/HBM厂传导</li>
</ul>
</div>
'''
gen.add_trading_plan(plan_html)

# ============ 11. 风险提示 ============
gen.add_risk_warning([
    "【英伟达财报利好兑现风险】英伟达盘后涨4%+，但需警惕美股开盘后「买预期卖事实」回调，若英伟达大跌将压制A股科技股情绪，高位股可能集体回调；",
    "【周五获利盘兑现压力】明日周五，连续大涨后短线获利盘丰厚，午后可能出现获利回吐，追高风险大，尤其是连板股（德明利/联瑞新材/赛微电子等）明日开板后波动加剧；",
    "【风格切换反复风险】今日银行/新能源大跌，若明日科技股冲高回落，资金可能回流防御板块，造成科技股短期调整；",
    "【中报业绩雷风险】8月底是中报密集披露最后窗口，部分科技股若中报不及预期可能出现业绩杀，特别是高估值标的；",
    "【*ST建艺退市风险】*ST建艺债务+诉讼+退市风险未解除，若不及时清仓可能面临连续跌停无法卖出的极端情况，最高优先级必须清仓。",
])

# ============ 12. 明日预判（TOPIC预测） ============
predictions_html = '''
<div style="display:grid; grid-template-columns: 1fr 1fr 1fr; gap:14px;">
<div style="background: linear-gradient(135deg, rgba(239,68,68,0.12), rgba(245,158,11,0.08)); border:1px solid rgba(239,68,68,0.3); border-radius:14px; padding:16px;">
<div style="font-size:14px; font-weight:700; color:#ef4444; margin-bottom:10px;">🔴 高概率延续（≥70%）</div>
<ul style="font-size:12.5px; color:#fca5a5; line-height:1.8; padding-left:18px; margin:0;">
<li>PCB/覆铜板继续强势（生益科技中军效应）</li>
<li>半导体设备/材料延续热度</li>
<li>HBM/存储芯片分化但龙头继续</li>
<li>两市成交维持2万亿左右</li>
</ul>
</div>
<div style="background: linear-gradient(135deg, rgba(245,158,11,0.12), rgba(234,179,8,0.08)); border:1px solid rgba(245,158,11,0.3); border-radius:14px; padding:16px;">
<div style="font-size:14px; font-weight:700; color:#f59e0b; margin-bottom:10px;">🟡 中概率（40-70%）</div>
<ul style="font-size:12.5px; color:#fcd34d; line-height:1.8; padding-left:18px; margin:0;">
<li>沪指挑战4000点整数关口</li>
<li>CPO光模块从补涨转为主升</li>
<li>高位连板股分化（部分开板调整）</li>
<li>农业/贵金属轮动补涨</li>
</ul>
</div>
<div style="background: linear-gradient(135deg, rgba(107,114,128,0.12), rgba(75,85,99,0.08)); border:1px solid rgba(107,114,128,0.3); border-radius:14px; padding:16px;">
<div style="font-size:14px; font-weight:700; color:#9ca3af; margin-bottom:10px;">⚪ 低概率（≤40%）</div>
<ul style="font-size:12.5px; color:#d1d5db; line-height:1.8; padding-left:18px; margin:0;">
<li>科技股全面回调跌2%+</li>
<li>银行/新能源大幅反弹</li>
<li>两市成交重回1.5万亿以下</li>
<li>北向资金大幅净卖出</li>
</ul>
</div>
</div>
'''
gen._components.append(Section(title="🔮 明日行情预判", content=predictions_html, icon="psychology"))

# ============ 发布 ============
print("正在生成HTML...")
html = gen.generate()
print(f"HTML长度: {len(html)} 字符")

# 统计中文字数
import re
text_only = re.sub(r'<[^>]+>','', html)
text_only = re.sub(r'<script[^>]*>.*?</script>','',text_only,flags=re.S)
text_only = re.sub(r'<style[^>]*>.*?</style>','',text_only,flags=re.S)
chinese_chars = re.findall(r'[\u4e00-\u9fff]', text_only)
print(f"中文字数: {len(chinese_chars)}")

filepath = gen.save(filepath=f"docs/aftermarket/{DATE}_盘后速递.html")
print(f"已保存到: {filepath}")

# publish
print("正在publish...")
result = gen.publish(
    filename=f"{DATE}_盘后速递.html",
    excerpt=f"【8.27盘后】英伟达财报点燃全场！科创50暴涨3.77%，两市2.13万亿放量上攻，持仓4只3涨1跌，半导体/PCB/CPO/HBM全线爆发，明日策略出炉"
)
print(f"publish结果: {result}")
