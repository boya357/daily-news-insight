import sys, os
sys.path.insert(0, 'v3')
os.chdir('/root/daily-news-insight')

from v3.generators.s_level_catalyst import SLevelCatalystGenerator

gen = SLevelCatalystGenerator(
    date_str="20260928",
    catalyst_title="电子行业利润增1.1倍+PCB急跌 分化加剧",
    subtitle="2026.09.28 · 盘后S级催化"
)

gen.add_catalyst_overview(
    overview="国家统计局9月28日公布2026年1—8月规上工业企业利润数据：电子行业利润同比增长1.1倍，对全部规上工业利润增长贡献率达62.0%，为工业利润核心引擎。与此同时，A股PCB/铜箔板块出现急跌，铜冠铜箔跌10.51%，板块内多股跌幅超9%。一面对比产业基本面持续高景气，一面是高位股情绪面剧烈调整。盘后芯联集成预告前三季度净利6.81亿同比扭亏，粤芯半导体IPO申购倍数超2359倍，验证半导体制造端景气度。",
    importance="高"
)

gen.add_catalyst_details(
    background="""
    <b>宏观基本面：</b>1—8月全国规上工业利润总额52719.8亿元，同比增长15.7%，持续维持两位数增速。电子行业成为最大增长引擎，利润同比+109.9%，贡献62%增量。细分领域：光电子器件制造+72%、半导体分立器件制造+51.8%、电子专用材料制造+230%、电子电路制造+49.1%。光纤制造+530%、光缆制造+100%，算力基建上游材料全面爆发。<br><br>
    <b>板块调整背景：</b>PCB/铜箔板块今日出现大面积回调，迅捷兴跌超13%、燕麦科技跌12%、集泰股份/大亚圣象/澳弘电子10CM跌停，铜冠铜箔跌10.51%报100.50元。铜冠铜箔年内累计涨幅仍超200%，PE(TTM)高达343倍，估值消化压力持续。
    """,
    trigger="""
    <b>触发因素1：统计局数据验证电子高景气</b><br>
    电子专用材料利润增2.3倍，光电子器件增72%，半导体分立器件增51.8%，数据验证AI算力链上游材料端盈利爆发式增长，为半导体材料/设备提供基本面锚点。<br><br>
    <b>触发因素2：PCB高位股获利回吐</b><br>
    铜冠铜箔等标的前期涨幅过大（年内+214%），融资余额占流通市值比例超90%分位，高位筹码松动引发板块性调整，属于情绪面+资金面双重驱动。<br><br>
    <b>触发因素3：芯联集成扭亏验证制造端景气</b><br>
    盘后芯联集成公告前三季度净利6.81亿同比扭亏，Q3净利约4.03亿环比+9%，AI业务增速超80%，毛利率提升9.17pct，国产模拟晶圆代工迎来盈利拐点。
    """
)

gen.add_industry_chain_analysis(
    upstream=[
        {
            "name": "电子专用材料",
            "desc": "利润同比+230%，增速最快细分。前驱体、光刻胶、高纯试剂、电子特气",
            "stocks": [
                {"code": "002409", "name": "雅克科技", "impact": "利好"},
                {"code": "688535", "name": "华海诚科", "impact": "利好"},
                {"code": "300346", "name": "南大光电", "impact": "利好"}
            ]
        },
        {
            "name": "高端电子铜箔",
            "desc": "AI服务器拉动高端铜箔需求增260%，HVLP铜箔供不应求",
            "stocks": [
                {"code": "301217", "name": "铜冠铜箔", "impact": "景气但估值高"},
                {"code": "688700", "name": "东威科技", "impact": "景气"}
            ]
        },
        {
            "name": "光纤光缆",
            "desc": "利润同比+530%/+100%，算力基建核心基础设施",
            "stocks": [
                {"code": "601869", "name": "长飞光纤", "impact": "利好"},
                {"code": "002281", "name": "光迅科技", "impact": "利好"}
            ]
        }
    ],
    midstream=[
        {
            "name": "晶圆制造",
            "desc": "芯联集成扭亏为盈，粤芯半导体IPO超2360倍申购",
            "stocks": [
                {"code": "688469", "name": "芯联集成", "impact": "扭亏利好"},
                {"code": "688981", "name": "中芯国际", "impact": "利好"}
            ]
        },
        {
            "name": "半导体分立器件",
            "desc": "利润同比+51.8%，功率器件/AI芯片需求拉动",
            "stocks": [
                {"code": "600584", "name": "长电科技", "impact": "利好"},
                {"code": "002079", "name": "苏州固锝", "impact": "利好"}
            ]
        },
        {
            "name": "光电子器件",
            "desc": "利润同比+72%，800G/1.6T光模块+硅光双轮驱动",
            "stocks": [
                {"code": "300308", "name": "中际旭创", "impact": "利好"},
                {"code": "300502", "name": "新易盛", "impact": "利好"}
            ]
        }
    ],
    downstream=[
        {
            "name": "AI算力中心",
            "desc": "液冷/服务器/光模块全链条高景气，算力投资持续超预期",
            "stocks": [
                {"code": "002837", "name": "英维克", "impact": "液冷龙头"},
                {"code": "000977", "name": "浪潮信息", "impact": "服务器龙头"}
            ]
        },
        {
            "name": "新能源汽车",
            "desc": "车规芯片/功率器件需求稳定增长，电动车渗透率提升",
            "stocks": [
                {"code": "300750", "name": "宁德时代", "impact": "电池龙头"},
                {"code": "002594", "name": "比亚迪", "impact": "整车龙头"}
            ]
        },
        {
            "name": "物联网终端",
            "desc": "低功耗芯片需求扩张，AI终端催生新增长点",
            "stocks": [
                {"code": "603501", "name": "韦尔股份", "impact": "CIS龙头"},
                {"code": "300223", "name": "北京君正", "impact": "存储芯片"}
            ]
        }
    ]
)

# === 持仓股分析 ===
from components.data import StockTags
stock_tags = StockTags([
    {"code": "002837", "name": "英维克", "impact": "中性"},
    {"code": "301217", "name": "铜冠铜箔", "impact": "利空（情绪面）"},
    {"code": "002409", "name": "雅克科技", "impact": "利好（基本面）"},
    {"code": "002789", "name": "*ST建艺", "impact": "中性"}
])

holding_analysis = f'''
<div class="section-block">
    <h3 class="section-title" style="color: #e2e8f0; font-size: 18px; font-weight: 700; margin-bottom: 16px; display: flex; align-items: center;">
        <span style="margin-right: 8px;">💼</span>持仓股影响分析
    </h3>
    {stock_tags.render()}
    <div style="margin-top: 16px; display: grid; grid-template-columns: repeat(2, 1fr); gap: 12px;">
        <div style="background: linear-gradient(135deg, rgba(59,130,246,0.1), rgba(37,99,235,0.05)); border-radius: 12px; padding: 16px; border: 1px solid rgba(96,165,250,0.2);">
            <div style="font-size: 14px; font-weight: 600; color: #60a5fa; margin-bottom: 8px;">英维克（002837）</div>
            <div style="font-size: 12px; color: #cbd5e1; line-height: 1.7;">
                今日主力净卖出2.60亿元，技术面偏弱。电子行业高景气数据对液冷赛道形成长期基本面支撑，但短期需警惕情绪面传导。今日召开临时股东大会审议股权激励计划。<br>
                <b>估值锚：</b>2026E PE约60-70倍（一致预期0.7元EPS），历史中高分位。<br>
                <b>操作建议：</b>底仓持有，反弹至60日均线附近减仓机动部分。
            </div>
        </div>
        <div style="background: linear-gradient(135deg, rgba(239,68,68,0.1), rgba(220,38,38,0.05)); border-radius: 12px; padding: 16px; border: 1px solid rgba(248,113,113,0.2);">
            <div style="font-size: 14px; font-weight: 600; color: #f87171; margin-bottom: 8px;">铜冠铜箔（301217）</div>
            <div style="font-size: 12px; color: #cbd5e1; line-height: 1.7;">
                今日大跌10.51%报100.50元，成交额24.44亿。近3日主力净流入-2.22亿。<b>双重验证结论：</b>①未发现公司层面利空公告；②下跌为板块性调整（PCB全线下挫），属高位获利回吐；③产业基本面未变（电子专用材料利润+230%）。<br>
                <b>估值锚：</b>PE(TTM) 343倍，PB 14.85倍，估值极高。<br>
                <b>操作建议：</b>不建议急跌抄底，等待企稳信号。强支撑89.84元（跌停价）。
            </div>
        </div>
        <div style="background: linear-gradient(135deg, rgba(34,197,94,0.1), rgba(22,163,74,0.05)); border-radius: 12px; padding: 16px; border: 1px solid rgba(74,222,128,0.2);">
            <div style="font-size: 14px; font-weight: 600; color: #4ade80; margin-bottom: 8px;">雅克科技（002409）</div>
            <div style="font-size: 12px; color: #cbd5e1; line-height: 1.7;">
                今日跌5.97%报124.70元，成交额16.79亿。<b>利好催化：</b>电子专用材料利润增2.3倍，雅克为前驱体材料龙头直接受益。股价下跌跟随科技板块调整，非个股利空。<br>
                <b>估值锚：</b>PE(TTM) 57倍，PB 7.42倍，半导体材料行业中等偏高。<br>
                <b>操作建议：</b>维持底仓30%持有+反弹减仓机动仓+115-120元再评估。关注120元支撑。
            </div>
        </div>
        <div style="background: linear-gradient(135deg, rgba(245,158,11,0.1), rgba(217,119,6,0.05)); border-radius: 12px; padding: 16px; border: 1px solid rgba(251,191,36,0.2);">
            <div style="font-size: 14px; font-weight: 600; color: #fbbf24; margin-bottom: 8px;">*ST建艺（002789）</div>
            <div style="font-size: 12px; color: #cbd5e1; line-height: 1.7;">
                今日震荡后尾盘拉升收涨8.50%。近期公告均为诉讼进展，无重大事项。庭外重组申请已受理，撤销退市风险警示尚在深交所审核。<br>
                <b>估值锚：</b>PB 36.46倍（亏损），博弈重组/摘帽预期。<br>
                <b>操作建议：</b>维持投机仓位，严格止损，不建议追加。关注摘帽审核进展。
            </div>
        </div>
    </div>
</div>
'''
gen._components.append(holding_analysis)

# === 隔夜外盘扫描 ===
overnight_html = '''
<div class="section-block">
    <h3 class="section-title" style="color: #e2e8f0; font-size: 18px; font-weight: 700; margin-bottom: 16px; display: flex; align-items: center;">
        <span style="margin-right: 8px;">🌍</span>隔夜外盘扫描（强制）
    </h3>
    <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 14px; margin-bottom: 14px;">
        <div style="background: linear-gradient(135deg, rgba(168,85,247,0.12), rgba(139,92,246,0.06)); border-radius: 14px; padding: 18px; border: 1px solid rgba(192,132,252,0.25);">
            <div style="font-size: 13px; color: #a78bfa; font-weight: 600; margin-bottom: 10px;">📈 费城半导体指数 (SOX)</div>
            <div style="font-size: 26px; font-weight: 700; color: #fff; margin-bottom: 4px;">12,668.93 <span style="font-size: 14px; color: #4ade80;">+1.41%</span></div>
            <div style="font-size: 11px; color: #94a3b8;">9月25日收盘 · 周线四连涨 · 本周 +6.27%</div>
            <div style="font-size: 11px; color: #64748b; margin-top: 6px;">创5月以来最长周线连涨纪录</div>
        </div>
        <div style="background: linear-gradient(135deg, rgba(236,72,153,0.12), rgba(219,39,119,0.06)); border-radius: 14px; padding: 18px; border: 1px solid rgba(244,114,182,0.25);">
            <div style="font-size: 13px; color: #f472b6; font-weight: 600; margin-bottom: 10px;">💾 存储芯片表现</div>
            <div style="font-size: 16px; font-weight: 700; color: #fff; margin-bottom: 6px;">SK海力士 +2.78%</div>
            <div style="font-size: 12px; color: #cbd5e1; line-height: 1.7;">
                西部数据 +1.44% · 闪迪 +1.38%<br>
                催化：Solidigm拟2027年赴美IPO<br>
                高通 +3.97%（领涨半导体）
            </div>
        </div>
    </div>
    <div style="background: rgba(255,255,255,0.04); border-radius: 12px; padding: 16px; border: 1px solid rgba(255,255,255,0.08);">
        <div style="font-size: 13px; font-weight: 600; color: #e2e8f0; margin-bottom: 10px;">📰 核心要点 & 对A股映射</div>
        <div style="font-size: 12px; color: #94a3b8; line-height: 2;">
            • <b style="color: #f1f5f9;">费半周线四连涨</b>：本周累计涨6.27%，AI算力需求支撑科技股估值<br>
            • <b style="color: #f1f5f9;">存储芯片普涨</b>：Solidigm IPO预期+AI数据中心NAND/HBM需求，利好国内存储产业链（雅克/长电等）<br>
            • <b style="color: #f1f5f9;">Meta Muse引爆AI Agent</b>：CPU需求预期升温，AMD、Intel受益，映射国产CPU/算力链<br>
            • <b style="color: #f1f5f9;">中美贸易休战延长</b>：至2027年1月10日，建立AI对话渠道，但高端芯片出口管制未放松<br>
            • <b style="color: #f1f5f9;">今晚关注</b>：9月28日美股周一开盘后半导体板块能否延续涨势
        </div>
    </div>
</div>
'''
gen._components.append(overnight_html)

# === 投资机会 ===
gen.add_investment_opportunities(opportunities=[
    {
        "title": "半导体材料（确定性最高）",
        "level": "S级",
        "logic": "电子专用材料利润增2.3倍，数据验证景气度。存储+先进封装双轮驱动，前驱体、光刻胶、电子特气为核心受益方向。",
        "targets": ["雅克科技（前驱体龙头）", "华海诚科（先进封装材料）", "南大光电（电子特气）"]
    },
    {
        "title": "晶圆制造（拐点明确）",
        "level": "A级",
        "logic": "芯联集成扭亏验证国产晶圆代工盈利拐点，粤芯半导体IPO火爆印证赛道稀缺性。AI+汽车电子双驱动。",
        "targets": ["芯联集成（特色工艺龙头）", "中芯国际（先进制程）", "粤芯半导体（待上市）"]
    },
    {
        "title": "PCB/铜箔（左侧布局机会）",
        "level": "B级",
        "logic": "产业需求确定性高（AI服务器高端铜箔+260%），但估值过高需消化。急跌后或有反弹，需等待企稳。",
        "targets": ["铜冠铜箔（HVLP龙头）", "生益科技（覆铜板龙头）", "南亚新材（高速CCL）"]
    },
    {
        "title": "光模块/光电子（景气延续）",
        "level": "A级",
        "logic": "光电子器件利润增72%，光纤制造增5.3倍。800G/1.6T光模块需求持续释放，硅光加速渗透。",
        "targets": ["中际旭创（光模块龙头）", "新易盛（海外客户）", "天孚通信（光器件）"]
    }
])

gen.add_risk_warning(risks=[
    "估值风险：PCB/铜箔板块PE普遍超100倍，铜冠铜箔达343倍，估值消化需时间",
    "美债利率风险：10年期美债收益率接近5.2%，高利率压制成长股估值",
    "融资盘风险：铜冠铜箔融资余额处90%+分位，续跌可能触发平仓负反馈",
    "出口管制风险：中美贸易休战但高端芯片管制未放松，先进制程产业链存不确定性",
    "情绪面风险：科技板块高位震荡加剧，单日波动可能超预期，需严格止损"
])

gen.add_investment_strategy(
    strategy="""
    <b>总体判断：</b>电子行业利润增1.1倍的数据验证了AI算力链的产业景气度，为科技股提供了坚实的基本面锚。但短期市场处于高位震荡阶段，PCB/铜箔等前期涨幅过大的板块估值消化压力明显。<br><br>
    <b>操作策略：</b><br>
    1. <b>持仓策略</b>：底仓持有核心标的（雅克科技、英维克），机动仓位逢高减仓，保持灵活性。铜冠铜箔不建议急跌抄底，等待企稳信号。<br>
    2. <b>加仓方向</b>：优先考虑半导体材料（前驱体、电子特气）和晶圆制造（国产替代逻辑+盈利拐点），有明确的基本面数据支撑。<br>
    3. <b>风险控制</b>：单只股票仓位不超过30%，整体科技股仓位不超过70%，预留现金应对极端波动。严格执行止损纪律。<br>
    4. <b>关注时间窗口</b>：9月底为三季度业绩预告密集期，关注各公司Q3业绩验证。10月三季报正式披露期，业绩超预期标的有望迎来新一轮行情。
    """
)

# 发布
gen.publish(
    title="电子利润增1.1倍+PCB急跌 分化加剧",
    filename="20260928_盘后_S级催化扫描_电子利润增1.1倍+PCB急跌.html",
    excerpt="1-8月电子行业利润增1.1倍，贡献率62%；PCB板块急跌铜冠铜箔跌10.5%；芯联集成扭亏验证晶圆制造拐点"
)

print("✅ S级催化报告V2生成并发布成功")
