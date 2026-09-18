import sys, os
sys.path.insert(0, '/root/daily-news-insight')
sys.path.insert(0, '/root/daily-news-insight/v3')
os.chdir('/root/daily-news-insight')

from v3.generators.s_level_catalyst import SLevelCatalystGenerator
from components.layout import Section

gen = SLevelCatalystGenerator(
    date_str="20260918",
    catalyst_title="黄仁勋芯片销量翻倍指引+存储超级周期确认",
    subtitle="2026.09.18 · 盘后S级催化"
)

gen.add_catalyst_overview(
    "盘后双重S级催化共振：<strong>①黄仁勋明确指引英伟达明年芯片销量翻倍</strong>——"
    "在苏格兰AI安全峰会上黄仁勋表态\"明年英伟达销售的芯片数量将是今年的两倍\"，"
    "对应FY2028营收指引约70%增长（约6730亿美元），远超市场此前44%的一致预期，AI资本开支放缓论被彻底证伪；"
    "<strong>②存储芯片超级周期确认</strong>——DRAM/NAND现货价格续创新高，HBM4现货价飙至3500美元/颗，"
    "十铨总经理明确表态\"DRAM缺口非常明显且庞大，2027年上半年缺货最严峻\"，"
    "原厂2027-2028年产能几乎被长约预订完毕。隔夜费城半导体大涨3.14%、纳指涨1.69%、"
    "英伟达+2.54%/美光+5.5%/SK海力士+6.42%，半导体板块情绪彻底反转。"
)

gen.add_catalyst_details(
    background=(
        "9月15日\"AI减速论\"曾引发费城半导体暴跌5.86%，市场担忧AI资本开支见顶。"
        "但仅三天后，黄仁勋在苏格兰AI安全峰会上用明确的销量指引（明年芯片销量翻倍）彻底击碎空头逻辑——"
        "AI需求正在向医疗、制造、金融等全行业扩散，当前瓶颈不是需求而是产能。"
        "与此同时，存储芯片超级周期进入纵深阶段：DRAM现货价格续涨、HBM供需极度紧张、"
        "原厂长约已锁至2027-2028年，十铨等模组厂预警2027年上半年缺货最严峻。"
        "今日A股存储芯片板块涨3.43%、获155.56亿主力净流入，国家大基金持股概念涨4.03%，"
        "雅克科技/铜冠铜箔等持仓标的全线飘红，半导体板块迎来估值修复+业绩上修的双重催化。"
    ),
    trigger=(
        "【外盘端·超级利好】9月17日美股：费城半导体+3.14%（+353点，收11599.49）、纳指+1.69%（收26418.3）、"
        "标普+1.14%、道指+0.61%。核心半导体标的全线大涨：英特尔+7.6%/美光+5.5%（收$977.50）/"
        "英伟达+2.54%（收$219.34，市值5.29万亿）/台积电ADR+3.0%（收$430.26）/"
        "阿斯麦+1.71%/应用材料+0.49%。韩股：SK海力士+6.42%、三星电子+3.37%。"
        "布油下跌0.96%至98.97美元，黄金微跌0.17%至4392美元。\n"
        "【黄仁勋重磅指引】黄仁勋在苏格兰国王查尔斯AI峰会上明确表示：\"我预计，明年英伟达销售的芯片数量将是今年的两倍。"
        "原因在于AI正在为不同行业和不同经济体带来巨大的价值贡献\"。"
        "这与英伟达FY2028约70%营收增长指引（约6730亿美元）一致，"
        "比市场此前44%的一致预期高出26个百分点。当前可见订单约5000亿美元（未来14个月）。\n"
        "【存储超级周期】DRAM/NAND现货续涨：DDR5 16Gb +7.31%/30日（$55.6）、"
        "DDR4 16Gb +5.47%/30日（$85.95）、企业级SSD 30TB +11.84%/30日（$4647）。"
        "十铨总经理陈庆文：DRAM缺口非常明显且庞大，Q4存储价格续涨，由单月大涨15-20%转为一季涨20-30%；"
        "2027上半年缺货最严峻，原厂2027-2028年产能几乎被长约包揽。"
        "HBM4现货报价已飙至3500美元/颗，SK海力士与英伟达HBM4供应价比HBM3E涨超50%。\n"
        "【政策催化】全国先进制造业大会9月16-17日召开，习近平就发展先进制造业作出重要指示，"
        "强调\"持续做大做强先进制造业、提升产业链自主可控水平\"；"
        "工信部公布第一批国家新兴产业发展示范基地（21个园区+112个企业）；"
        "十部门联合印发《医药工业发展\"十五五\"规划》，创新药产业规模年均增速20%以上。\n"
        "【公司端】雅克科技今日涨3.07%报138.83元，主力净流入2.78亿元，融资余额28.3亿元；"
        "铜冠铜箔涨1.29%报113.29元，成交额35.64亿，近5日主力净流入2.04亿；"
        "英维克涨1.85%报62.89元，融资余额38.47亿元（占流通市值4.87%）；"
        "格科微42亿定增预案、艾华集团18.8亿定增扩高端电容产能；"
        "新华传媒收购界面财联社100%股权，9月21日复牌；"
        "信达证券主动终止上市（中金吸收合并）。"
    )
)

overnight_html = """
<div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 12px; margin-bottom: 16px;">
    <div style="background: linear-gradient(135deg, rgba(16,185,129,0.18) 0%, rgba(5,150,105,0.08) 100%); border-radius: 12px; padding: 16px; border: 1px solid rgba(16,185,129,0.3); text-align: center;">
        <div style="font-size: 12px; color: #6ee7b7; margin-bottom: 6px;">费城半导体</div>
        <div style="font-size: 22px; font-weight: 800; color: #34d399;">+3.14%</div>
        <div style="font-size: 11px; color: #6ee7b7; margin-top: 4px;">收11,599</div>
    </div>
    <div style="background: linear-gradient(135deg, rgba(16,185,129,0.12) 0%, rgba(5,150,105,0.06) 100%); border-radius: 12px; padding: 16px; border: 1px solid rgba(16,185,129,0.25); text-align: center;">
        <div style="font-size: 12px; color: #6ee7b7; margin-bottom: 6px;">纳斯达克</div>
        <div style="font-size: 22px; font-weight: 800; color: #34d399;">+1.69%</div>
        <div style="font-size: 11px; color: #6ee7b7; margin-top: 4px;">收26,418</div>
    </div>
    <div style="background: linear-gradient(135deg, rgba(239,68,68,0.12) 0%, rgba(185,28,28,0.06) 100%); border-radius: 12px; padding: 16px; border: 1px solid rgba(239,68,68,0.25); text-align: center;">
        <div style="font-size: 12px; color: #fca5a5; margin-bottom: 6px;">布伦特原油</div>
        <div style="font-size: 22px; font-weight: 800; color: #f87171;">-0.96%</div>
        <div style="font-size: 11px; color: #fca5a5; margin-top: 4px;">$98.97/桶</div>
    </div>
    <div style="background: linear-gradient(135deg, rgba(168,85,247,0.12) 0%, rgba(126,34,206,0.06) 100%); border-radius: 12px; padding: 16px; border: 1px solid rgba(168,85,247,0.25); text-align: center;">
        <div style="font-size: 12px; color: #c4b5fd; margin-bottom: 6px;">COMEX黄金</div>
        <div style="font-size: 22px; font-weight: 800; color: #a78bfa;">-0.17%</div>
        <div style="font-size: 11px; color: #c4b5fd; margin-top: 4px;">$4,392</div>
    </div>
</div>
<div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 14px;">
    <div style="background: rgba(255,255,255,0.04); border-radius: 12px; padding: 16px; border: 1px solid rgba(255,255,255,0.08);">
        <div style="font-size: 14px; font-weight: 700; color: #f1f5f9; margin-bottom: 10px;">🚀 核心半导体标的（隔夜）</div>
        <div style="display: flex; flex-direction: column; gap: 6px;">
            <div style="display: flex; justify-content: space-between; font-size: 13px;">
                <span style="color: #94a3b8;">美光科技</span>
                <span style="color: #34d399; font-weight: 600;">+5.50%  $977.50</span>
            </div>
            <div style="display: flex; justify-content: space-between; font-size: 13px;">
                <span style="color: #94a3b8;">英特尔</span>
                <span style="color: #34d399; font-weight: 600;">+7.60%</span>
            </div>
            <div style="display: flex; justify-content: space-between; font-size: 13px;">
                <span style="color: #94a3b8;">英伟达 NVDA</span>
                <span style="color: #34d399; font-weight: 600;">+2.54%  $219.34</span>
            </div>
            <div style="display: flex; justify-content: space-between; font-size: 13px;">
                <span style="color: #94a3b8;">台积电 ADR</span>
                <span style="color: #34d399; font-weight: 600;">+3.00%  $430.26</span>
            </div>
            <div style="display: flex; justify-content: space-between; font-size: 13px;">
                <span style="color: #94a3b8;">阿斯麦 ASML</span>
                <span style="color: #34d399; font-weight: 600;">+1.71%  $1,629.67</span>
            </div>
        </div>
    </div>
    <div style="background: rgba(255,255,255,0.04); border-radius: 12px; padding: 16px; border: 1px solid rgba(255,255,255,0.08);">
        <div style="font-size: 14px; font-weight: 700; color: #f1f5f9; margin-bottom: 10px;">🇰🇷 亚太市场核心标的</div>
        <div style="display: flex; flex-direction: column; gap: 6px;">
            <div style="display: flex; justify-content: space-between; font-size: 13px;">
                <span style="color: #94a3b8;">SK海力士</span>
                <span style="color: #34d399; font-weight: 600;">+6.42%  1,857,000₩</span>
            </div>
            <div style="display: flex; justify-content: space-between; font-size: 13px;">
                <span style="color: #94a3b8;">三星电子</span>
                <span style="color: #34d399; font-weight: 600;">+3.37%  261,000₩</span>
            </div>
            <div style="display: flex; justify-content: space-between; font-size: 13px;">
                <span style="color: #94a3b8;">日经225</span>
                <span style="color: #f87171; font-weight: 600;">-0.90%  44,946</span>
            </div>
            <div style="display: flex; justify-content: space-between; font-size: 13px;">
                <span style="color: #94a3b8;">恒生指数</span>
                <span style="color: #34d399; font-weight: 600;">+0.60%  24,750</span>
            </div>
            <div style="display: flex; justify-content: space-between; font-size: 13px;">
                <span style="color: #94a3b8;">应用材料</span>
                <span style="color: #34d399; font-weight: 600;">+0.49%  $417.40</span>
            </div>
        </div>
    </div>
</div>
"""

gen.add_catalyst_deep_analysis([
    {
        "title": "🌍 隔夜外盘全景扫描",
        "content": overnight_html,
        "level": "positive"
    }
])

gen.add_catalyst_deep_analysis([
    {
        "title": "🎯 黄仁勋销量翻倍指引：AI减速论被彻底证伪",
        "content": (
            "【核心观点】黄仁勋在苏格兰AI安全峰会上明确给出\"明年芯片销量翻倍\"的指引，这是自Q2财报给出FY2028营收70%增长指引后，"
            "又一次超预期的前瞻指引。当前市场一致预期仍在63%左右，与管理层70%目标有7个百分点差距，意味着预期仍有上修空间。\n\n"
            "【三大核心支撑】\n"
            "① <strong>订单可见度极高</strong>：未来14个月约5000亿美元可见订单，远超当前年营收基数；\n"
            "② <strong>需求结构多元化</strong>：从最初的4大云厂商（吸收68% Blackwell出货）扩展到医疗、制造、金融等全行业+主权AI（韩/澳/印）；\n"
            "③ <strong>供给瓶颈而非需求瓶颈</strong>：黄仁勋明确表示\"当前瓶颈是产能而非需求\"，Rubin量产爬坡是核心观察点。\n\n"
            "【对A股影响】AI算力链逻辑再度强化，前期因\"减速论\"造成的估值折价将快速修复。"
            "重点关注：①GPU供应链（PCB/铜箔/散热/光模块）；②国产算力替代（昇腾/寒武纪产业链）；"
            "③AI基础设施（液冷/电源/IDC）。持仓中的英维克（液冷）和铜冠铜箔（AI PCB铜箔）直接受益。"
        ),
        "level": "positive"
    },
    {
        "title": "💾 存储超级周期进入纵深：2027年缺货最严峻",
        "content": (
            "【现货价格持续攀升】截至9月18日，9个存储品种组合均值30日涨+5.06%、同比+332.56%。"
            "DDR5 16Gb现货$55.6（30日+7.31%，同比+480%）、DDR4 8Gb $45.8（30日+5.63%，同比+860%）、"
            "企业级SSD 30TB $4,647（30日+11.84%）。HBM3E 36GB现货$2,107，HBM4未量产现货已飙至$3,500/颗。\n\n"
            "【十铨总经理重磅表态】2027年上半年缺货最严峻：\n"
            "① DRAM缺口\"非常明显且庞大\"，NAND也有缺口但相对较轻；\n"
            "② Q4起涨幅由单月15-20%转为单季20-30%（涨价斜率放缓但趋势不改）；\n"
            "③ 原厂2027-2028年产能几乎被长约包揽，新客户拿不到货；\n"
            "④ 产能都被HBM占用，通用DRAM供给收缩更严重。\n\n"
            "【A股受益标的】存储芯片板块今日涨3.43%获155亿净流入。"
            "雅克科技（半导体前驱体+光刻胶）直接受益存储原厂扩产+价格上涨；"
            "华海诚科（环氧塑封料）受益HBM先进封装需求；长鑫/长存产业链整体受益。"
        ),
        "level": "positive"
    },
    {
        "title": "📊 持仓股盘后表现与操作建议",
        "content": (
            "【英维克 002837】收62.89元（+1.85%），成交额16.87亿，换手率2.39%。\n"
            "• 今日液冷板块延续强势，机构一周净买入1.37亿元，深股通净卖出1.08亿元\n"
            "• 融资余额38.47亿元（占流通市值4.87%，超近一年60%分位）\n"
            "• 技术面：站稳60元平台，5日均线拐头向上，Q2业绩拐点确认后进入右侧区间\n"
            "• 估值：PE(TTM)164倍，PB 22.4倍，液冷赛道高估值溢价合理\n"
            "• <strong>操作建议</strong>：底仓持有，60元以上不追高，回踩55-58元加仓\n\n"
            "【雅克科技 002409】收138.83元（+3.07%），主力净流入2.78亿，成交额30.65亿。\n"
            "• 存储+光刻胶+前驱体多重催化共振，今日半导体材料板块领涨\n"
            "• 中期分红10派3.5元（9月21日股权登记），中性事件\n"
            "• 技术面：140元附近有压力，今日最高触及140元后回落，需观察能否有效突破\n"
            "• 估值：PE(TTM)64倍，PB 8.26倍，半导体材料板块合理偏高\n"
            "• <strong>操作建议</strong>：持有不动，140元以上可考虑减仓20%锁定利润，"
            "回踩125-130元是加仓机会。不构成≥30%减仓建议，无需双重验证\n\n"
            "【铜冠铜箔 301217】收113.29元（+1.29%），成交额35.64亿，振幅6.69%。\n"
            "• AI PCB高端铜箔需求持续旺盛，近5日主力净流入2.04亿\n"
            "• 融资余额连续4天增加，市场人气旺盛\n"
            "• 技术面：高位震荡整理，110元支撑有效，118-120元压力较大\n"
            "• 估值：PE(TTM)387倍，PB 16.7倍，估值偏高，需业绩消化\n"
            "• <strong>操作建议</strong>：底仓持有，118-120元减仓20-30%做波段\n\n"
            "【*ST建艺 002789】今日无特别公告，ST板块整体偏弱，继续风控观察。"
        ),
        "level": "neutral"
    }
])

gen.add_industry_chain_analysis(
    upstream=[
        {"name": "半导体设备", "desc": "阿斯麦+1.71%/应用材料+0.49%", "impact": "利好"},
        {"name": "半导体材料", "desc": "光刻胶/前驱体/电子特气", "impact": "利好"},
        {"name": "硅片", "desc": "中晶科技3连板/有研硅走强", "impact": "利好"},
    ],
    midstream=[
        {"name": "存储芯片", "desc": "美光+5.5%/SK海力士+6.42%/HBM4涨50%", "impact": "强利好"},
        {"name": "GPU/AI芯片", "desc": "英伟达+2.54%/销量翻倍指引", "impact": "强利好"},
        {"name": "晶圆制造", "desc": "台积电ADR+3%/产能满载", "impact": "利好"},
        {"name": "先进封装", "desc": "HBM产能持续扩张", "impact": "利好"},
    ],
    downstream=[
        {"name": "液冷散热", "desc": "英维克+1.85%/AI算力散热刚需", "impact": "利好"},
        {"name": "PCB/CCL", "desc": "铜冠铜箔+1.29%/高端铜箔紧缺", "impact": "利好"},
        {"name": "光模块", "desc": "Coherent/Ciena大涨", "impact": "利好"},
        {"name": "AI服务器", "desc": "浪潮信息等受益需求增长", "impact": "利好"},
    ]
)

gen.add_investment_opportunities([
    {
        "name": "🔥 存储芯片链",
        "priority": "高",
        "logic": "存储超级周期确认，2027年缺货最严峻，原厂长约锁至2028年，价格趋势明确向上。HBM供需极度紧张，DDR5/DDR4现货同步上涨。",
        "stocks": [
            {"code": "002409", "name": "雅克科技", "impact": "半导体前驱体+光刻胶双受益"},
            {"code": "688535", "name": "华海诚科", "impact": "HBM环氧塑封料"},
            {"code": "688825", "name": "长鑫科技", "impact": "DRAM国产替代龙头"},
        ]
    },
    {
        "name": "🚀 AI算力基础设施",
        "priority": "高",
        "logic": "黄仁勋销量翻倍指引击碎AI减速论，FY2028营收70%增长远超预期，AI资本开支确定性大幅提升。液冷、PCB、光模块等上游供应链直接受益。",
        "stocks": [
            {"code": "002837", "name": "英维克", "impact": "液冷龙头+海外加速放量"},
            {"code": "301217", "name": "铜冠铜箔", "impact": "AI PCB高端铜箔国产替代"},
        ]
    },
    {
        "name": "💎 半导体设备材料",
        "priority": "中",
        "logic": "全国先进制造业大会定调，自主可控政策加码+全球半导体景气上行双轮驱动。设备、零部件、材料国产替代加速。",
        "stocks": [
            {"code": "002371", "name": "北方华创", "impact": "设备平台龙头"},
            {"code": "688012", "name": "中微公司", "impact": "刻蚀设备"},
            {"code": "600584", "name": "长电科技", "impact": "先进封装龙头"},
        ]
    },
])

gen.add_risk_warning([
    "美联储加息超预期：10年期美债收益率仍处高位，高利率环境压制成长股估值",
    "AI需求验证风险：黄仁勋指引乐观，但季度营收仍需实际验证，若大型云厂商资本开支不及预期将回调",
    "存储价格波动：现货价格涨幅从单月15-20%降为单季20-30%，斜率放缓可能引发市场情绪波动",
    "出口管制风险：美国对华半导体出口管制政策仍存不确定性",
    "持仓个股估值偏高：铜冠铜箔PE 387倍/英维克PE 164倍，高估值对业绩兑现要求极高",
    "地缘政治风险：中东局势、中美关系等外部因素仍可能冲击市场情绪",
])

gen.add_investment_strategy(
    "【总体判断】AI减速论被证伪+存储超级周期确认，半导体板块迎来双重催化，前期因\"AI恐慌\"造成的估值折价将快速修复。"
    "今日A股存储板块已获155亿主力净流入，属于资金左侧确认信号。\n\n"
    "【操作策略】\n"
    "• <strong>持仓策略</strong>：4只持仓全部持有不动。雅克科技140元以上可减仓20%做波段（非≥30%大幅减仓，不触发双重验证要求）；"
    "铜冠铜箔118-120元压力位可减仓20%；英维克60元以上不追高，回踩再加。\n"
    "• <strong>仓位建议</strong>：半导体总仓位维持60-70%，存储+算力双主线配置，不留现金踏空风险。\n"
    "• <strong>关注时点</strong>：下周一（9月21日）关注新华传媒复牌对传媒板块影响、雅克科技分红股权登记；"
    "下周重点关注英伟达GTC Berlin（10月1日）、存储原厂Q3业绩指引、国内大基金三期进展。\n\n"
    "【核心结论】隔夜外盘大涨+黄仁勋销量指引+存储超级周期三重利好共振，"
    "9月15日的\"AI减速恐慌\"已被证伪，半导体板块有望重回上升通道。"
    "持仓策略从\"防守反击\"转为\"积极持有\"，但严格执行高位减仓纪律，不追高、不满仓。"
)

output_path = gen.publish(
    title="黄仁勋芯片销量翻倍指引+存储超级周期确认",
    filename="20260918_盘后_S级催化扫描_黄仁勋指引+存储超级周期.html",
    excerpt="隔夜费城半导体大涨3.14%，黄仁勋明言明年芯片销量翻倍，存储超级周期确认2027年缺货最严峻"
)
print(f"✅ 报告已生成: {output_path}")
