import sys, os
sys.path.insert(0, '/root/daily-news-insight')
sys.path.insert(0, '/root/daily-news-insight/v3')
os.chdir('/root/daily-news-insight')

from v3.generators.aftermarket import AftermarketGenerator

gen = AftermarketGenerator(date_str="20260909", subtitle="2026.09.09 · 盘后速递")

# ============ 1. 今日核心亮点 ============
gen.add_today_highlight("""
权重护盘、题材普跌的「二八分化」延续！沪指微涨0.28%收3951点，深成指涨0.15%，创业板指跌0.14%、科创50跌0.69%。个股跌多涨少，赚钱效应仅34%。
煤炭暴涨3.35%领涨两市，橡胶/黄金/航运港口午后全线爆发，湖南黄金、黑猫股份、彤程新材涨停。糖业/农业持续强势，中粮科技、红棉股份、华康股份全部2连板。
科技成长继续承压，半导体主力净流出超65亿元，传媒/计算机/医药集体走弱。龙虎榜60只个股上榜，席位资金净买入5.61亿元，机构净流入6.07亿、北向净流入8.29亿。
成交额约1.86万亿较昨日缩量1000亿，存量博弈格局未改，资金从高位科技流向低估值周期与农业防御板块，风格切换持续进行中。
""")

# ============ 2. 市场收盘总结 ============
indices = [
    {"name": "上证指数", "value": "3951.51", "change": "+0.28%", "up": True, "icon": "trending_up"},
    {"name": "深证成指", "value": "13723.32", "change": "+0.15%", "up": True, "icon": "trending_up"},
    {"name": "创业板指", "value": "3354.97", "change": "-0.14%", "up": False, "icon": "trending_down"},
    {"name": "科创50", "value": "1580.06", "change": "-0.69%", "up": False, "icon": "trending_down"},
]
gen.add_market_summary(indices, volume="约1.86万亿（缩量约1000亿）", northbound="龙虎榜口径净买入8.29亿元")

# ============ 3. 市场情绪温度计 ============
gen.add_sentiment_thermometer(
    temperature=45,
    volume="1.86万亿",
    up_count="1728",
    down_count="3369",
    limit_up_count="49"
)

# ============ 4. 晚间重要新闻 ============
gen.add_evening_news([
    {
        "title": "2连板众泰汽车发异动公告 推进整车复工复产",
        "content": "众泰汽车连续2日累计涨幅超20%，公司公告称正全力推进整车板块复工复产，全新A0级车型已进入批量试制阶段，主要面向海外市场，但尚未形成销售且资金到位情况存在不确定性，可能影响海外销售进度。",
        "time": "2026-09-09 19:00",
        "source": "公司公告",
        "tag": "异动公告",
        "tag_variant": "warning"
    },
    {
        "title": "5连板百大集团提示风险 短期涨幅超60%",
        "content": "百大集团自9月2日以来累计上涨61.09%，平均换手率8.46%，公司公告称股价短期涨幅较大，存在市场情绪过热及非理性炒作情形，可能存在后续下跌风险。主营业务未发生重大变化。",
        "time": "2026-09-09 19:10",
        "source": "公司公告",
        "tag": "风险提示",
        "tag_variant": "warning"
    },
    {
        "title": "3连板华脉科技：光缆涨价不具备可持续性",
        "content": "华脉科技3连板累计涨幅超40%，公司公告称光纤概念市场关注度较高，信息通信行业发展十五五规划落地推升通信行业关注度，但数据中心及算力相关领域收入占比较小，光缆产品涨价受多重因素影响不具备可持续性。",
        "time": "2026-09-09 19:20",
        "source": "公司公告",
        "tag": "风险提示",
        "tag_variant": "warning"
    },
    {
        "title": "财政部发行2026年第七/八期储蓄国债",
        "content": "财政部决定发行2026年第七期和第八期储蓄国债（电子式）。第七期期限3年，票面年利率1.63%，最大发行额248亿元；第八期期限5年，票面年利率1.7%，最大发行额302亿元。发行期为9月10日至9月19日。利率继续下行反映宽松货币环境。",
        "time": "2026-09-09 17:40",
        "source": "财政部",
        "tag": "货币政策",
        "tag_variant": "info"
    },
    {
        "title": "龙虎榜60股上榜 机构净流入6.07亿",
        "content": "9月9日沪深两市共60只个股登上龙虎榜，席位总买入147.81亿、总卖出142.17亿，合计净买入5.61亿元。其中机构专用席位净买入6.07亿元（现身41只个股），北向资金净买入8.29亿元，知名游资净买入0.46亿元。机构回流入场信号明显。",
        "time": "2026-09-09 19:30",
        "source": "东方财富Choice数据",
        "tag": "资金面",
        "tag_variant": "primary"
    },
])

# ============ 5. 板块涨跌幅排行 ============
gen.add_sector_performance(
    up_sectors=[
        {"name": "煤炭开采加工", "change": "+3.35%"},
        {"name": "橡胶/轮胎", "change": "+4.10%"},
        {"name": "航运港口", "change": "+2.87%"},
        {"name": "贵金属/黄金", "change": "+2.52%"},
        {"name": "糖业/代糖", "change": "+3.80%"},
        {"name": "农业种植", "change": "+1.95%"},
        {"name": "通信设备", "change": "+0.58%"},
        {"name": "银行", "change": "+0.42%"},
        {"name": "油气开采", "change": "+1.86%"},
        {"name": "化肥/农化", "change": "+2.30%"},
    ],
    down_sectors=[
        {"name": "半导体/芯片", "change": "-1.35%"},
        {"name": "传媒/短剧", "change": "-2.10%"},
        {"name": "计算机/IT服务", "change": "-0.94%"},
        {"name": "医药生物", "change": "-0.82%"},
        {"name": "消费电子", "change": "-1.15%"},
    ]
)

# ============ 6. 盘面深度解读 ============
gen.add_market_deep_analysis(
    strong_sectors=[
        {
            "name": "煤炭（+3.35%）",
            "reason": "旺季需求预期叠加估值修复，中国神华涨2.18%领涨。夏季用煤高峰尾声但冬季采暖预期提前，叠加高股息防御属性吸引资金流入。动力煤价格企稳回升，行业盈利确定性强。"
        },
        {
            "name": "橡胶/轮胎（+4.1%）",
            "reason": "厄尔尼诺影响橡胶主产区供给，上期所橡胶期货8月以来大涨14%创2年新高。轮胎行业第三轮集中涨价2%-3%，黑猫股份2连板、彤程新材涨停。供给收缩+需求复苏双重逻辑。"
        },
        {
            "name": "糖业/代糖（+3.8%）",
            "reason": "全球甘蔗减产预期推升国际糖价，国内白糖期货同步走强。中粮科技、红棉股份、华康股份全部2连板。代糖概念叠加消费复苏预期，成为当前市场最强主线之一。"
        },
        {
            "name": "贵金属/黄金（+2.52%）",
            "reason": "全球央行购金潮延续+地缘风险升温，金价突破关键阻力位。湖南黄金涨停（龙虎榜净买4.39亿），莱绅通灵涨停。黄金股兼具抗通胀与避险属性，获机构+北向双重加仓。"
        },
        {
            "name": "航运港口（+2.87%）",
            "reason": "运价指数持续回升，招商轮船获超10亿主力资金净流入。全球贸易复苏预期+红海局势扰动供给端，航运景气度上行。中远海控、招商港口等龙头同步走强。"
        },
    ],
    weak_sectors=[
        {
            "name": "半导体/芯片（-1.35%）",
            "reason": "主力资金净流出超65亿元，长鑫科技特大单净流出14.43亿居首。前期涨幅较大的存储/先进封装标的获利回吐压力大，兆易创新、兴森科技领跌。行业景气度虽在但估值偏高，资金阶段性兑现。"
        },
        {
            "name": "传媒/短剧（-2.10%）",
            "reason": "龙版传媒停牌核查引爆板块分歧，中信出版、中国出版、读者传媒集体大跌。AI短剧概念股前期涨幅过大，监管风险升温，资金集中出逃。板块进入退潮期。"
        },
        {
            "name": "计算机/IT服务（-0.94%）",
            "reason": "AI应用端整体回调，主力净流出19.08亿元。市场担忧AI商业化进度不及预期，从主题炒作转向业绩验证阶段。缺乏业绩支撑的纯概念股承压明显。"
        },
    ],
    core_view="""
    <strong>核心判断：</strong>当前市场处于典型的「权重护盘、题材退潮」阶段，二八分化特征明显。沪指靠煤炭、银行等权重股维持红盘，但个股层面跌多涨少（1728涨/3369跌），赚钱效应仅34%。
    <br><br>
    <strong>风格切换持续：</strong>资金从高位科技成长（半导体、AI）持续流向低估值防御板块（煤炭、农业、黄金）。这一趋势已连续3个交易日强化，建议降低成长仓位、增加周期与防御配置。
    <br><br>
    <strong>积极信号：</strong>龙虎榜机构席位今日净流入6.07亿元，为近期首次大规模净流入，显示机构资金在低位开始逐步回补仓位，对市场中期不宜过度悲观。
    <br><br>
    <strong>操作建议：</strong>当前位置建议半仓观望，控制仓位在5成以下。重点关注两条线：低估值周期（煤炭、黄金、航运）的防御属性；科技成长的超跌反弹机会，但需等明确企稳信号。
    """
)

# ============ 7. 持仓股深度诊断 ============
gen.add_holdings_tracking([
    {
        "name": "英维克",
        "code": "002837",
        "price": "62.43",
        "change": "-0.90%",
        "up": False,
        "comment": """
        <strong>今日表现：</strong>收62.43元跌0.90%，今开63.05，最高64.10，最低61.93，成交额23.18亿，换手率约3.3%。延续震荡筑底格局，成交量较昨日有所萎缩。
        <br><br>
        <strong>技术面判断：</strong>日线级别处于下降通道中，5日线下穿20日线形成死叉，MACD绿柱仍在扩大。支撑位60元（前期低点），压力位66元（20日线）。KDJ指标处于超卖区域，有技术性反弹需求。
        <br><br>
        <strong>资金面：</strong>液冷板块整体走弱，主力资金持续流出。今日缩量调整显示抛压有所减轻，但尚未出现明显的资金回流迹象。北向资金持仓变动需进一步观察。
        <br><br>
        <strong>操作建议：</strong>
        <br>• 当前价位62.43元处于底部震荡区间，不建议在当前位置割肉
        <br>• <strong>支撑位60元</strong>：若跌破60元且放量，需减仓1/3控制风险
        <br>• <strong>反弹目标66-68元</strong>：反弹至该区间可减仓20-30%，降低持仓成本
        <br>• <strong>补仓时机</strong>：跌破58元可考虑小仓位（10%）补仓做T，55元以下再补10%
        <br>• 总体策略：底仓持有+高抛低吸降低成本，等待液冷板块情绪回暖
        """
    },
    {
        "name": "铜冠铜箔",
        "code": "301217",
        "price": "107.21",
        "change": "+1.62%",
        "up": True,
        "comment": """
        <strong>今日表现：</strong>收107.21元涨1.62%，今开107.62，最高110.54，最低106.00。逆势走强，在科技股普跌背景下表现相对强势，显示资金对锂电铜箔+存储铜箔双逻辑的认可。
        <br><br>
        <strong>技术面判断：</strong>日线级别站稳105元平台，5日线拐头向上。支撑位103元（5日线），压力位112元（前期高点）。MACD金叉形成，红柱放大，技术形态向好。
        <br><br>
        <strong>资金面：</strong>3日主力资金净流入5248万元，5日虽然净流出6.34亿但近期明显有资金回流迹象。存储HBM铜箔需求增长逻辑持续兑现，公司产能扩张进展顺利。
        <br><br>
        <strong>操作建议：</strong>
        <br>• 持仓盈利状态良好，继续持有为主
        <br>• <strong>第一目标位115元</strong>：突破后可看高至125元（历史新高区域）
        <br>• <strong>止损位上移至100元</strong>：跌破100元减仓1/3，跌破95元再减1/3
        <br>• <strong>加仓建议</strong>：回踩103-105元区间可加仓10-15%
        <br>• 总体策略：锂电铜箔底部反转+存储铜箔高增长双逻辑，中期持有
        """
    },
    {
        "name": "雅克科技",
        "code": "002409",
        "price": "131.52",
        "change": "-0.45%",
        "up": False,
        "comment": """
        <strong>今日表现：</strong>收131.52元跌0.45%，在半导体板块整体调整背景下跌幅小于板块平均，表现相对抗跌。半导体板块主力净流出超65亿，雅克作为HBM材料龙头有一定资金护盘。
        <br><br>
        <strong>技术面判断：</strong>日线在130元附近获得支撑，该位置为前期平台上沿。支撑位128元（60日线），压力位138元（20日线）。MACD处于零轴附近，方向待选择。成交量温和，多空博弈均衡。
        <br><br>
        <strong>资金面：</strong>半导体板块整体资金流出，但雅克作为HBM前驱体龙头，机构持仓比例较高，相对抗跌。存储产业链景气度持续上行，长期逻辑未变，短期受板块情绪拖累。
        <br><br>
        <strong>操作建议：</strong>
        <br>• 当前价位处于合理估值区间，底仓继续持有
        <br>• <strong>强支撑位125-128元</strong>：回踩该区间可加仓10%
        <br>• <strong>止损位120元</strong>：有效跌破则减仓1/2
        <br>• <strong>反弹目标140-145元</strong>：反弹至该区间可减仓20%做波段
        <br>• 总体策略：HBM材料国产替代核心标的，中期看好，短期随板块震荡，逢低分批布局
        """
    },
    {
        "name": "*ST建艺",
        "code": "002789",
        "price": "13.28",
        "change": "-2.35%",
        "up": False,
        "comment": """
        <strong>今日表现：</strong>收13.28元跌2.35%。ST板块整体情绪偏弱，退市风险仍是最大不确定性。公司基本面持续恶化，经营状况堪忧，仅适合极小仓位博弈。
        <br><br>
        <strong>技术面判断：</strong>股价处于下降趋势中，5日、10日、20日均线呈空头排列。支撑位12.5元（前期低点），压力位14元（20日线）。成交量低迷，流动性差，进出不便。
        <br><br>
        <strong>资金面：</strong>成交极度低迷，日均成交额不足1亿，机构早已离场，仅散户博弈。无主力资金关注，股价走势随机性强。
        <br><br>
        <strong>操作建议：</strong>
        <br>• <strong>核心判断：退市风险高悬，建议逢反弹减仓离场</strong>
        <br>• <strong>反弹减仓位13.5-14元</strong>：反弹至该区间坚决减仓至少2/3
        <br>• <strong>止损位12元</strong>：跌破12元立即清仓，不可抱有幻想
        <br>• 仓位控制：建议仓位≤5%，仅作为极小仓位博弈，绝不加仓
        <br>• 总体策略：以风控为第一优先，任何反弹都是减仓机会，逐步清仓退出
        """
    },
])

# ============ 8. 龙虎榜深度解读 ============
gen.add_dragon_tiger_list([
    {
        "name": "华正新材",
        "code": "603186",
        "change": "+10.00%",
        "up": True,
        "institutions": 2,
        "reason": "3日涨幅偏离值累计20%",
        "net_buy": "4.89亿元",
    },
    {
        "name": "湖南黄金",
        "code": "002155",
        "change": "+10.02%",
        "up": True,
        "institutions": 3,
        "reason": "日涨幅偏离值达7%",
        "net_buy": "4.39亿元",
    },
    {
        "name": "崇达技术",
        "code": "002815",
        "change": "+5.74%",
        "up": True,
        "institutions": 3,
        "reason": "3日涨幅偏离值累计20%",
        "net_buy": "3.29亿元（3日）",
    },
])

# 龙虎榜深度解读
from components.layout import Section

lhb_detail_html = """
<div style="display: flex; flex-direction: column; gap: 16px;">
    
    <div style="background: rgba(30,30,50,0.5); border: 1px solid rgba(255,255,255,0.08);
                border-radius: 14px; padding: 18px; box-shadow: 0 2px 8px rgba(0,0,0,0.2);">
        <div style="display: flex; align-items: center; margin-bottom: 12px;">
            <span style="font-size: 16px; font-weight: 600; color: #f1f5f9;">🔥 华正新材（603186）</span>
            <span style="font-size: 13px; color: #10b981; margin-left: 12px; font-weight: 600;">+10.00% 涨停</span>
            <span style="font-size: 12px; color: #f59e0b; margin-left: 8px;">🏛️ 机构+北向双重加仓</span>
        </div>
        <div style="font-size: 13px; color: #94a3b8; line-height: 1.7;">
            <strong>📊 席位解读：</strong>龙虎榜净买入4.89亿元居首，换手率14.4%。买一沪股通净买入10.34亿，买二东方证券杭州龙井路（章盟主系）买入4.25亿，买三高盛上海买入4.15亿。
            卖方方面，紫阳东路3日净卖出1.66亿元获利了结。北向资金+机构+顶级游资三方共振，资金强度极高。
            <br><br>
            <strong>💡 逻辑分析：</strong>CCL（覆铜板）+高速材料+AI算力产业链，受益于AI服务器需求爆发，高速高频材料国产替代加速。
            3日累计涨幅超20%，放量突破平台，趋势性行情确立。但短期涨幅较大，获利盘丰厚，需警惕回调风险。
            <br><br>
            <strong>🎯 持续性判断：</strong><span style="color: #10b981;">★★★★☆ 较强</span>
            <br>机构+北向+游资三方合力，资金基础扎实。行业逻辑（AI算力+国产替代）清晰，中期持续性可期。
            但短期涨幅过大，建议回调至5日线附近再考虑介入，不追高。
        </div>
    </div>
    
    <div style="background: rgba(30,30,50,0.5); border: 1px solid rgba(255,255,255,0.08);
                border-radius: 14px; padding: 18px; box-shadow: 0 2px 8px rgba(0,0,0,0.2);">
        <div style="display: flex; align-items: center; margin-bottom: 12px;">
            <span style="font-size: 16px; font-weight: 600; color: #f1f5f9;">🥇 湖南黄金（002155）</span>
            <span style="font-size: 13px; color: #10b981; margin-left: 12px; font-weight: 600;">+10.02% 涨停</span>
            <span style="font-size: 12px; color: #f59e0b; margin-left: 8px;">🏛️ 机构净买2.01亿</span>
        </div>
        <div style="font-size: 13px; color: #94a3b8; line-height: 1.7;">
            <strong>📊 席位解读：</strong>龙虎榜净买入4.39亿元，占总成交10.84%，换手率9.47%。机构席位净买入2.01亿元（买二、买五均为机构），
            北向资金净买入1.35亿元。量化打板席位净买入6186万。机构+北向+量化三方入场，资金属性多元，承接力强。
            <br><br>
            <strong>💡 逻辑分析：</strong>全球央行持续购金+地缘政治风险升温+美元走弱预期，金价中长期上行趋势明确。
            湖南黄金兼具黄金+锑矿双资源属性，锑价同样处于上升周期。金价突破关键阻力位后，黄金股迎来估值修复行情。
            <br><br>
            <strong>🎯 持续性判断：</strong><span style="color: #10b981;">★★★★★ 强</span>
            <br>机构大举加仓+北向资金配置+行业基本面改善，三重共振。黄金作为防御性资产，在市场风格切换期更受青睐。
            建议关注回调机会，支撑位26元可考虑分批建仓，目标位32-35元。
        </div>
    </div>
    
    <div style="background: rgba(30,30,50,0.5); border: 1px solid rgba(255,255,255,0.08);
                border-radius: 14px; padding: 18px; box-shadow: 0 2px 8px rgba(0,0,0,0.2);">
        <div style="display: flex; align-items: center; margin-bottom: 12px;">
            <span style="font-size: 16px; font-weight: 600; color: #f1f5f9;">🏭 崇达技术（002815）</span>
            <span style="font-size: 13px; color: #10b981; margin-left: 12px; font-weight: 600;">+5.74%</span>
            <span style="font-size: 12px; color: #f59e0b; margin-left: 8px;">🏛️ 机构净买2.17亿（3日）</span>
        </div>
        <div style="font-size: 13px; color: #94a3b8; line-height: 1.7;">
            <strong>📊 席位解读：</strong>3日龙虎榜净买入3.29亿元，成交额24.33亿，换手率17.28%。
            机构席位3日合计净买入2.17亿元（3家机构买入，1家卖出），北向资金3日净买入1.91亿元。
            佛山系净买入1.06亿。机构+北向合力加仓，外资认可度高。
            <br><br>
            <strong>💡 逻辑分析：</strong>PCB板块3日累计涨幅超20%，受益于AI服务器需求爆发+通信设备升级周期。
            崇达技术主营高端PCB，产品覆盖服务器、通信设备领域，直接受益于AI算力建设。公司海外收入占比高，汇率贬值也有贡献。
            <br><br>
            <strong>🎯 持续性判断：</strong><span style="color: #f59e0b;">★★★☆☆ 中性</span>
            <br>机构认可度高，行业逻辑通顺，但3日累计涨幅已超20%，短期获利盘较多。
            且今日放量滞涨（涨5.74%但换手率达17.28%），显示上方抛压较重。建议观望为主，等待回调至16-17元区间再考虑。
        </div>
    </div>
    
    <div style="background: linear-gradient(135deg, rgba(59,130,246,0.1), rgba(139,92,246,0.1));
                border: 1px solid rgba(96,165,250,0.3); border-radius: 14px; padding: 18px;">
        <div style="font-size: 14px; font-weight: 600; color: #93c5fd; margin-bottom: 10px;">📋 龙虎榜总评</div>
        <div style="font-size: 13px; color: #cbd5e1; line-height: 1.8;">
            今日60只个股上榜，席位资金<strong style="color: #10b981;">净买入5.61亿元</strong>，为近期首次出现较大规模净流入。
            <br>• <strong>机构席位</strong>：净买入6.07亿元（现身41只个股），结束连续多日净流出，机构回补信号明确
            <br>• <strong>北向资金</strong>：净买入8.29亿元，重点加仓华正新材、崇达技术、湖南黄金
            <br>• <strong>知名游资</strong>：净买入0.46亿元，章盟主重仓中粮糖业（+1.03亿），成都系大幅出货亚盛集团（-1.76亿）
            <br><br>
            <strong style="color: #f59e0b;">核心结论：</strong>机构资金回流是今日最大亮点，显示机构在市场调整中开始逐步建仓。
            资金方向集中在周期资源（黄金、煤炭、糖）和高端制造（PCB/CCL），科技成长仍以流出为主。
            建议跟随机构方向，关注低估值周期板块的中期配置机会。
        </div>
    </div>
</div>
"""

gen._components.append(Section(title="🐉 龙虎榜深度解读", content=lhb_detail_html, icon="award"))

# ============ 9. 重点关注标的 ============
focus_html = """
<div style="display: flex; flex-direction: column; gap: 16px;">
    
    <div style="background: rgba(30,30,50,0.5); border: 1px solid rgba(255,255,255,0.08);
                border-radius: 14px; padding: 18px; box-shadow: 0 2px 8px rgba(0,0,0,0.2);">
        <div style="display: flex; align-items: center; margin-bottom: 10px;">
            <span style="font-size: 16px; font-weight: 600; color: #f1f5f9;">🥇 湖南黄金（002155）</span>
            <span style="font-size: 12px; background: rgba(16,185,129,0.2); color: #10b981; 
                         padding: 3px 8px; border-radius: 6px; margin-left: 10px;">关注评级：★★★★☆</span>
        </div>
        <div style="font-size: 13px; color: #94a3b8; line-height: 1.8;">
            <strong>📌 买入逻辑：</strong>
            <br>① 全球央行购金潮延续，美联储降息预期升温，金价中长期上行趋势明确
            <br>② 公司黄金+锑双资源属性，锑价同样处于上升周期，双重受益
            <br>③ 龙虎榜机构净买2.01亿+北向净买1.35亿，机构认可度高
            <br>④ 估值相对合理，2026年PE约25-30倍，低于历史均值
            <br><br>
            <strong>🎯 目标价：</strong>第一目标 <span style="color: #10b981; font-weight: 600;">32-35元</span>（+12%~23%）
            <br>
            <strong>🛑 止损位：</strong><span style="color: #ef4444; font-weight: 600;">24元</span>（跌破则止损，约-16%）
            <br>
            <strong>💡 操作建议：</strong>回调至26-27元区间可分批建仓（建议10-15%仓位），跌破24元止损。
        </div>
    </div>
    
    <div style="background: rgba(30,30,50,0.5); border: 1px solid rgba(255,255,255,0.08);
                border-radius: 14px; padding: 18px; box-shadow: 0 2px 8px rgba(0,0,0,0.2);">
        <div style="display: flex; align-items: center; margin-bottom: 10px;">
            <span style="font-size: 16px; font-weight: 600; color: #f1f5f9;">🏭 中国神华（601088）</span>
            <span style="font-size: 12px; background: rgba(59,130,246,0.2); color: #60a5fa; 
                         padding: 3px 8px; border-radius: 6px; margin-left: 10px;">关注评级：★★★★☆</span>
        </div>
        <div style="font-size: 13px; color: #94a3b8; line-height: 1.8;">
            <strong>📌 买入逻辑：</strong>
            <br>① 煤炭行业高景气，旺季需求预期强，动力煤价格企稳回升
            <br>② 高股息防御标的，股息率超8%，在市场震荡期具备避险属性
            <br>③ 煤炭板块今日领涨（+3.35%），资金持续流入低估值周期股
            <br>④ 估值便宜，PE不到10倍，PB约1.5倍，安全边际高
            <br><br>
            <strong>🎯 目标价：</strong>第一目标 <span style="color: #10b981; font-weight: 600;">45-48元</span>（+10%~17%）
            <br>
            <strong>🛑 止损位：</strong><span style="color: #ef4444; font-weight: 600;">38元</span>（跌破则止损，约-7%）
            <br>
            <strong>💡 操作建议：</strong>当前价位41元附近可小仓位建仓（建议10%仓位），作为防御配置。
            适合中线持有，享受分红+估值修复双重收益。
        </div>
    </div>
    
    <div style="background: rgba(30,30,50,0.5); border: 1px solid rgba(255,255,255,0.08);
                border-radius: 14px; padding: 18px; box-shadow: 0 2px 8px rgba(0,0,0,0.2);">
        <div style="display: flex; align-items: center; margin-bottom: 10px;">
            <span style="font-size: 16px; font-weight: 600; color: #f1f5f9;">🔬 彤程新材（603650）</span>
            <span style="font-size: 12px; background: rgba(168,85,247,0.2); color: #c084fc; 
                         padding: 3px 8px; border-radius: 6px; margin-left: 10px;">关注评级：★★★☆☆</span>
        </div>
        <div style="font-size: 13px; color: #94a3b8; line-height: 1.8;">
            <strong>📌 买入逻辑：</strong>
            <br>① 橡胶产业链景气度上行，天然橡胶价格大涨14%创2年新高，轮胎企业第三轮涨价
            <br>② 公司光刻胶+特种橡胶双主业，半导体光刻胶国产替代空间大
            <br>③ 今日涨停突破平台，量能配合良好，资金关注度提升
            <br>④ 位置相对不高，前期调整充分，有补涨需求
            <br><br>
            <strong>🎯 目标价：</strong>第一目标 <span style="color: #10b981; font-weight: 600;">35-38元</span>（+15%~25%）
            <br>
            <strong>🛑 止损位：</strong><span style="color: #ef4444; font-weight: 600;">28元</span>（跌破则止损，约-8%）
            <br>
            <strong>💡 操作建议：</strong>不建议追高，等待回调至30-31元区间再考虑介入（建议5-8%仓位）。
            短期涨幅较大，需警惕回调风险。
        </div>
    </div>
    
    <div style="background: linear-gradient(135deg, rgba(239,68,68,0.1), rgba(249,115,22,0.1));
                border: 1px solid rgba(248,113,113,0.3); border-radius: 14px; padding: 16px;">
        <div style="font-size: 13px; font-weight: 600; color: #fca5a5; margin-bottom: 8px;">⚠️ 关注标的说明</div>
        <div style="font-size: 12px; color: #fecaca; line-height: 1.7;">
            以上标的仅供参考，不构成投资建议。当前市场处于风格切换期，波动加大，
            建议控制总仓位在5成以下，单只标的仓位不超过15%，严格执行止损纪律。
            数据来源：东方财富Choice、证券时报、21世纪经济报道（2026-09-09）
        </div>
    </div>
</div>
"""
gen._components.append(Section(title="🎯 重点关注标的", content=focus_html, icon="target"))

# ============ 10. 明日操作策略 ============
gen.add_tomorrow_prediction([
    {
        "title": "大盘走势判断",
        "content": "预计明日沪指继续在3900-4000点区间震荡，权重股仍有护盘动力但题材股可能继续分化。创业板指关注3300点支撑，若跌破可能进一步下探。整体仍处于存量博弈格局，缩量震荡概率大。"
    },
    {
        "title": "仓位建议",
        "content": "建议仓位控制在4-5成。当前市场风格切换剧烈，不宜重仓押注单一方向。保留足够现金等待更明确的趋势信号。科技成长仓位建议≤2成，周期防御仓位建议2-3成。"
    },
    {
        "title": "操作方向",
        "content": "低吸周期资源股（黄金、煤炭、航运）的回调机会；科技成长股反弹减仓，重点关注存储/PCB方向是否企稳；农业糖业板块前排标的可小仓位参与，但需警惕高位股回调风险。"
    },
])

gen.add_trading_plan("""
<strong>📋 明日操作计划（2026.09.10）</strong>
<br><br>
<strong>一、持仓操作计划</strong>
<br>1. <strong>英维克（002837）</strong>：当前62.43元，底部震荡。<span style="color: #10b981;">若跌破60元减仓1/3</span>，<span style="color: #f59e0b;">反弹至66元以上减仓20%</span>。
    底仓持有观望，不追高不盲目割肉，等待液冷板块情绪回暖。
<br>2. <strong>铜冠铜箔（301217）</strong>：当前107.21元，趋势向好。<span style="color: #10b981;">继续持有</span>，
    <span style="color: #f59e0b;">止损位上移至100元</span>，<span style="color: #10b981;">回踩103-105元可加仓10%</span>。第一目标115元。
<br>3. <strong>雅克科技（002409）</strong>：当前131.52元，相对抗跌。<span style="color: #10b981;">底仓持有</span>，
    <span style="color: #10b981;">回踩125-128元可加仓10%</span>，<span style="color: #ef4444;">跌破120元减仓1/2</span>。HBM材料逻辑中期不变。
<br>4. <strong>*ST建艺（002789）</strong>：当前13.28元，退市风险高。<span style="color: #ef4444;">任何反弹减仓</span>，
    <span style="color: #ef4444;">反弹至13.5-14元减仓2/3</span>，<span style="color: #ef4444;">跌破12元清仓</span>。风控第一。
<br><br>
<strong>二、关注标的操作计划</strong>
<br>1. <strong>湖南黄金（002155）</strong>：<span style="color: #10b981;">回调至26-27元区间可分批建仓</span>（建议10%仓位），目标32-35元，止损24元。
<br>2. <strong>中国神华（601088）</strong>：<span style="color: #10b981;">当前41元附近可小仓位建仓</span>（建议10%仓位），作为防御配置，目标45-48元，止损38元。
<br>3. <strong>彤程新材（603650）</strong>：<span style="color: #f59e0b;">不追高</span>，等待回调至30-31元再考虑（建议5-8%仓位），目标35-38元，止损28元。
<br><br>
<strong>三、风险控制</strong>
<br>• 单只标的仓位不超过15%，ST标的仓位≤5%
<br>• 总仓位控制在5成以下，保留足够现金
<br>• 严格执行止损纪律，不与趋势对抗
<br>• 关注晚间美股科技股表现，对明日A股科技板块有指引作用
""")

# ============ 11. 风险提示 ============
gen.add_risk_warning([
    "美联储9月议息会议临近，若降息不及预期可能引发全球市场波动，黄金及科技股均可能承压。",
    "国内经济复苏力度不及预期，上市公司三季报业绩可能低于市场预期，需警惕业绩雷风险。",
    "高位题材股（农业、糖业、黄金）短期涨幅较大，获利盘丰厚，存在集中兑现导致的回调风险。",
    "半导体板块持续调整，若龙头股进一步破位可能引发科技股系统性回调，注意控制仓位。",
    "地缘政治风险仍存，全球贸易摩擦可能升级，对出口相关板块造成冲击。",
])

# ============ 发布 ============
result = gen.publish()
print("发布结果:", result)
