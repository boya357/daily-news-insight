#!/usr/bin/env python3
"""生成 2026-07-10（周五）盘后速递 - V3.0统一标准"""
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'v3'))
os.chdir(os.path.dirname(os.path.abspath(__file__)))

from generators.aftermarket import AftermarketGenerator

DATE = "20260710"
SUBTITLE = "2026.07.10 · 盘后速递 · 周五"

gen = AftermarketGenerator(date_str=DATE, subtitle=SUBTITLE)

# ============================================================
# 1. 今日核心亮点
# ============================================================
highlight = """<div style="font-size: 14px; line-height: 1.7; color: var(--text-secondary);">
<p style="margin: 0 0 10px 0;"><strong style="color: #f87171;">📉 今日定性：放量长阴，科技主线遭重创</strong>。上证指数失守4000点报3996.16点(-1.00%)，深成指跌2.29%，创业板指重挫4.37%，科创50暴跌5.53%领跌全场。两市成交3.41万亿，较昨日放量4784亿，典型放量杀跌。但<strong style="color: #4ade80;">个股层面涨多跌少(3770涨/1672跌)</strong>，呈现"指数跌、小票活"的极致分化，资金高低切换极为剧烈。</p>
<p style="margin: 0 0 10px 0;"><strong style="color: #c084fc;">🔥 核心矛盾：</strong>前一日科创50单日暴涨8.41%后，周五资金集中兑现高位科技筹码——半导体产业链深度回调，电子板块跌5.32%领跌两市，通信跌3.51%，电力设备跌2.72%。与此同时，<strong style="color: #fbbf24;">低位防御与主题板块爆发</strong>：传媒(+2.60%)、国防军工(+2.56%)、医药生物、商业航天、房地产涨幅居前，资金从高位科技向低位板块大迁徙。</p>
<p style="margin: 0 0 10px 0;"><strong style="color: #60a5fa;">🐲 龙虎榜看点：</strong>紫光股份三日榜净买入22.48亿(北向+15.14亿+机构+2.86亿)，成为今日唯一百亿级成交+大资金抱团的AI算力中军；金风科技涨停+7.62亿净买入，风电链出现趋势资金回流；但兆易创新被机构净卖出5.01亿，晶合集成大跌17%，半导体高位筹码松动明显。</p>
<p style="margin: 0;"><strong style="color: #fb923c;">⚠️ 持仓预警：</strong>4只持仓股全部收跌——铜冠铜箔-5.43%(主力净流出3.32亿)、英维克-3.07%(跌破75支撑)、*ST建艺-1.64%(破位下行)、雅克科技-0.88%(相对抗跌)。下周一是风格切换关键观察日，科技能否止跌决定仓位去留。</p>
</div>"""
gen.add_today_highlight(highlight)

# ============================================================
# 2. 市场收盘总结
# ============================================================
indices = [
    {"name": "上证指数", "value": "3996.16", "change": "-1.00%", "icon": "trending_down", "up": False},
    {"name": "深证成指", "value": "15046.67", "change": "-2.29%", "icon": "trending_down", "up": False},
    {"name": "创业板指", "value": "3842.73", "change": "-4.37%", "icon": "trending_down", "up": False},
    {"name": "科创50", "value": "2064.98", "change": "-5.53%", "icon": "trending_down", "up": False},
]
gen.add_market_summary(indices, volume="3.41万亿(放量4784亿)", northbound="净流出102.66亿")

# 补充市场深度分析
market_deep_html = """
<div style="display: flex; flex-direction: column; gap: 16px;">
    <div style="background: var(--glass-bg); border: 1px solid var(--glass-border); border-radius: 12px; padding: 16px;">
        <div style="font-weight: 600; color: var(--text-primary); margin-bottom: 10px; display: flex; align-items: center; gap: 8px;">
            <span>🌡️</span><span>情绪温度计：由亢奋快速跌入冰点</span>
        </div>
        <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 10px; font-size: 13px;">
            <div style="background: rgba(239, 68, 68, 0.1); border-radius: 8px; padding: 10px; text-align: center;">
                <div style="color: #fca5a5; font-size: 11px; margin-bottom: 4px;">上涨/下跌</div>
                <div style="color: var(--text-primary); font-size: 16px; font-weight: 700;">3770 / 1672</div>
                <div style="color: var(--text-muted); font-size: 11px;">涨跌比2.25:1</div>
            </div>
            <div style="background: rgba(245, 158, 11, 0.1); border-radius: 8px; padding: 10px; text-align: center;">
                <div style="color: #fcd34d; font-size: 11px; margin-bottom: 4px;">涨停/跌停</div>
                <div style="color: var(--text-primary); font-size: 16px; font-weight: 700;">95 / 49</div>
                <div style="color: var(--text-muted); font-size: 11px;">跌扩大增</div>
            </div>
            <div style="background: rgba(59, 130, 246, 0.1); border-radius: 8px; padding: 10px; text-align: center;">
                <div style="color: #93c5fd; font-size: 11px; margin-bottom: 4px;">主力资金</div>
                <div style="color: #f87171; font-size: 16px; font-weight: 700;">-305.74亿</div>
                <div style="color: var(--text-muted); font-size: 11px;">全市场净流出</div>
            </div>
            <div style="background: rgba(168, 85, 247, 0.1); border-radius: 8px; padding: 10px; text-align: center;">
                <div style="color: #d8b4fe; font-size: 11px; margin-bottom: 4px;">北向资金</div>
                <div style="color: #f87171; font-size: 16px; font-weight: 700;">-102.66亿</div>
                <div style="color: var(--text-muted); font-size: 11px;">午后反手卖出</div>
            </div>
        </div>
    </div>
    
    <div style="background: var(--glass-bg); border: 1px solid var(--glass-border); border-radius: 12px; padding: 16px;">
        <div style="font-weight: 600; color: var(--text-primary); margin-bottom: 10px; display: flex; align-items: center; gap: 8px;">
            <span>🧭</span><span>今日走势深度复盘</span>
        </div>
        <div style="color: var(--text-secondary); font-size: 13px; line-height: 1.8;">
            <p style="margin: 0 0 8px 0;"><strong style="color: #fbbf24;">【早盘】风格突变，小票全面活跃</strong>：沪指高开后震荡上行，半日收涨0.76%报4067点。全市场近4500只个股上涨，黄线大幅领先蓝线，中小盘股普涨。医药、传媒、军工等低位板块领涨，科技权重走势偏弱。</p>
            <p style="margin: 0 0 8px 0;"><strong style="color: #4ade80;">【午间】商业航天异动</strong>：受长征十号乙运载火箭成功发射消息刺激，商业航天板块午后异动拉升，43只个股涨停或涨超10%，一度带动股指企稳回升。</p>
            <p style="margin: 0 0 8px 0;"><strong style="color: #f87171;">【午后】科技股跳水，指数单边下行</strong>：存储芯片等热门科技题材跌幅扩大，半导体板块集体跳水——兆易创新午后快速跳水收跌7.76%，成交额594亿创历史纪录；晶合集成跌超17%，中船特气跌超19%。三大股指震荡下行最终集体收跌。</p>
            <p style="margin: 0;"><strong style="color: #c084fc;">【收盘】极致分化</strong>：指数大跌但个股涨多跌少，黄线仍领先，表明下跌集中在少数权重科技股。成交额放量至3.41万亿，高位筹码大规模交换。</p>
        </div>
    </div>
    
    <div style="background: var(--glass-bg); border: 1px solid var(--glass-border); border-radius: 12px; padding: 16px;">
        <div style="font-weight: 600; color: var(--text-primary); margin-bottom: 10px; display: flex; align-items: center; gap: 8px;">
            <span>⚡</span><span>放量大跌的五大核心原因</span>
        </div>
        <div style="color: var(--text-secondary); font-size: 13px; line-height: 1.8;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #f87171;">1. 公募半年排名收官，高位赛道集中兑现</strong>：7月10日是公募半年业绩排名最后交易日，前期重仓半导体、算力的基金为锁定收益集中卖出，直接带动科创50、创业板权重大幅下挫。</p>
            <p style="margin: 0 0 6px 0;"><strong style="color: #f87171;">2. 周五避险情绪+获利盘出逃</strong>：前一日科创50暴涨8.41%积累了巨量获利盘，叠加周五天然避险需求，资金不愿持筹过周末，集中抛售高位科技股。</p>
            <p style="margin: 0 0 6px 0;"><strong style="color: #f87171;">3. 监管降温信号</strong>：中船特气等前期暴涨标的被交易所列入重点监控名单，短线游资恐慌出逃，高位次新股、题材股批量跌停。</p>
            <p style="margin: 0 0 6px 0;"><strong style="color: #f87171;">4. 北向资金午后反手卖出</strong>：早盘小幅流入后午后转为大幅净流出，全天净流出102.66亿，重点减持算力、存储龙头，放大了下跌动能。</p>
            <p style="margin: 0;"><strong style="color: #f87171;">5. 高低切换加速</strong>：资金从高位科技硬件板块加速流向低位防御板块（医药、传媒、军工、地产），形成跷跷板效应，指数被权重股拖累但个股活跃度不低。</p>
        </div>
    </div>
</div>
"""
from components.layout import Section
gen._components.append(Section(title="🧭 市场深度分析", content=market_deep_html, icon="analytics"))

# ============================================================
# 3. 板块涨幅榜 + 跌幅榜
# ============================================================
up_sectors = [
    {"name": "传媒", "change": "+2.60%", "up": True, "leader": "福石控股/欢瑞世纪", "fund_flow": "+28.7亿", "logic": "低位超跌修复+AI应用端资金切换+暑期档催化。福石控股、幸福蓝海、中国科传涨停，蓝色光标、浙文互联涨超5%。资金从硬件切向应用端的迹象明显。"},
    {"name": "国防军工", "change": "+2.56%", "up": True, "leader": "航天发展/高德红外", "fund_flow": "+35.2亿", "logic": "商业航天催化+军工中报业绩向好。长征十号乙火箭成功发射引爆板块，航天发展、航天环宇等43只个股涨停或涨超10%。地缘局势持续紧张叠加装备采购加速，军工板块估值修复空间大。"},
    {"name": "医药生物", "change": "+1.98%", "up": True, "leader": "常山药业/立方制药", "fund_flow": "+42.5亿", "logic": "创新药+医美+CXO全线上扬。常山药业、和元生物、益诺思、美迪西等近20股涨停或涨超10%。医药板块经历长期调整后估值处于历史低位，资金避险属性凸显。"},
    {"name": "房地产", "change": "+1.62%", "up": True, "leader": "粤宏远A/首开股份", "fund_flow": "+18.3亿", "logic": "政策预期升温+超跌反弹。粤宏远A、盈新发展、首开股份涨停，华发股份、市北高新涨超5%。地产板块处于政策底部区间，市场预期下半年可能有新一轮刺激政策。"},
    {"name": "食品饮料", "change": "+1.35%", "up": True, "leader": "白酒板块领涨", "fund_flow": "+15.6亿", "logic": "防御属性凸显+中报业绩稳健。白酒板块领涨，资金从科技股流出后选择消费白马避险。五粮液、泸州老窖等龙头表现稳健，板块整体估值合理。"},
    {"name": "电力设备(风电)", "change": "-2.72%", "up": False, "leader": "金风科技(涨停逆势)", "fund_flow": "-67.02亿(板块整体)", "logic": "板块整体下跌但内部分化剧烈——风电链(金风科技+9.99%、明阳智能+7.26%)逆势大涨，储能/锂电链(阳光电源-7.43%、宁德时代-7.12%)重挫。风电有海风装机加速+出海逻辑，锂电则受价格战压制。"},
    {"name": "商业航天", "change": "+5.80%", "up": True, "leader": "航天发展/航天环宇", "fund_flow": "+22.8亿", "logic": "长征十号乙运载火箭首飞成功直接催化，商业航天板块掀起涨停潮，43只个股涨停或涨超10%。低轨星座建设加速+卫星互联网产业化推进，行业进入0到1爆发期。"},
]

down_sectors = [
    {"name": "电子(半导体)", "change": "-5.32%", "up": False, "leader": "中船特气/晶合集成", "fund_flow": "-186.5亿", "logic": "前一日暴涨后获利盘集中出逃+监管重点监控。中船特气跌超19%，晶合集成跌超17%，华润微跌超14%，兆易创新跌7.76%(成交594亿创纪录)。电子板块全市场资金净流出最大，高位筹码松动明显。"},
    {"name": "通信", "change": "-3.51%", "up": False, "leader": "中际旭创/天孚通信", "fund_flow": "-52.36亿", "logic": "光模块、AI服务器龙头放量大跌。中际旭创净流出20.55亿，算力硬件全线回调。板块前期累计涨幅巨大，在公募止盈+外资减仓双重压力下短期调整压力大。"},
    {"name": "电力设备(储能/锂电)", "change": "-2.72%", "up": False, "leader": "阳光电源/宁德时代", "fund_flow": "-67.02亿", "logic": "储能逆变器龙头阳光电源跌7.43%，宁德时代跌7.12%，行业价格战加剧+中报业绩下修预期。锂电中游持续失血，新能源赛道景气度下行。"},
    {"name": "非银金融", "change": "-2.15%", "up": False, "leader": "华安证券/中信建投", "fund_flow": "-28.4亿", "logic": "券商板块全线走弱，华安证券、长江证券、中信建投跌超6%。市场交投虽活跃但券商业绩分化，叠加指数大跌影响市场情绪，券商股承压。"},
    {"name": "银行", "change": "-0.85%", "up": False, "leader": "齐鲁银行/上海银行", "fund_flow": "-15.2亿", "logic": "权重股整体偏弱，齐鲁银行、渝农商行、上海银行下挫。银行板块估值虽低但缺乏催化，在风格切换行情中作为被动配置品种。"},
]
gen.add_sector_performance(up_sectors, down_sectors)

# ============================================================
# 4. 持仓股深度诊断（4只）
# ============================================================
holdings = [
    {
        "name": "英维克",
        "code": "002837",
        "price": "73.54",
        "change": "-3.07%",
        "up": False,
        "volume": "54.95亿",
        "turnover": "6.37%",
        "high": "78.50",
        "low": "73.38",
        "analysis": """
        <div style="line-height: 1.8; font-size: 13px; color: var(--text-secondary);">
        <p style="margin: 0 0 8px 0;"><strong style="color: #f87171;">【当日表现】</strong>英维克今日收跌3.07%报73.54元，成交额54.95亿，换手率6.37%。盘中最高78.50元(早盘冲高+3.5%)，午后跟随科技板块跳水，最低探至73.38元，尾盘几乎收在最低点，呈现高开低走放量长阴的弱势形态。</p>
        <p style="margin: 0 0 8px 0;"><strong style="color: #fbbf24;">【技术面判断】</strong>
        <br>• 均线系统：MA5(73.38)已被跌破，MA10(74.07)和MA20(75.53)均失守，短期均线呈空头排列
        <br>• 支撑位：第一支撑73元(今日低点附近)，跌破则看68-70元区间(前期平台+跌停价68.28)
        <br>• 压力位：第一压力75-76元(MA10+MA20区域)，第二压力78.5元(今日高点)
        <br>• MACD：DIF-2.54，DEA-2.93，红柱缩小，多头动能减弱
        <br>• RSI：45.66，处于正常区间但偏弱势
        </p>
        <p style="margin: 0 0 8px 0;"><strong style="color: #60a5fa;">【资金面】</strong>液冷板块整体跟随AI硬件回调，主力资金净流出。但液冷中长期逻辑未变——英伟达Rubin全液冷方案+英特尔认证都是产业级利好，公司一季度营收+119%、净利+925%奠定高增长基调。</p>
        <p style="margin: 0 0 8px 0;"><strong style="color: #c084fc;">【操作建议】</strong>
        <br>• 当前已从高点93.52回撤约21%，跌破多条均线，短期进入调整通道
        <br>• 若周一反弹至<strong style="color: #4ade80;">76元以上</strong>，可减仓1/3降低仓位
        <br>• 若跌破<strong style="color: #f87171;">70元整数关口</strong>，应果断止损离场，不可恋战
        <br>• 中期逻辑仍在，但短期需等待止跌信号(缩量+站稳MA10)再考虑回补
        <br>• 仓位建议：从现有仓位降至1/3，保留底仓观察
        </p>
        </div>
        """
    },
    {
        "name": "铜冠铜箔",
        "code": "301217",
        "price": "132.09",
        "change": "-5.43%",
        "up": False,
        "volume": "49.93亿",
        "turnover": "4.32%",
        "high": "146.15",
        "low": "132.01",
        "analysis": """
        <div style="line-height: 1.8; font-size: 13px; color: var(--text-secondary);">
        <p style="margin: 0 0 8px 0;"><strong style="color: #f87171;">【当日表现】</strong>铜冠铜箔今日重挫5.43%报132.09元，成交额49.93亿，换手率4.32%。盘中最高146.15元(早盘冲高+4.6%)，午后随锂电+有色板块大幅跳水，最低探至132.01元，振幅高达10.12%，主力资金净流出3.32亿，属电力设备板块资金流出前列。</p>
        <p style="margin: 0 0 8px 0;"><strong style="color: #fbbf24;">【技术面判断】</strong>
        <br>• 均线系统：MA5(138.95)、MA10(149.79)、MA20(163.91)全部失守，短期均线空头排列
        <br>• 支撑位：130元附近为心理关口+前期平台，若跌破则看120元支撑
        <br>• 压力位：140-145元(MA5+今日开盘价区域)为短期强压力
        <br>• MACD：绿柱放大，DIF 4.03，DEA 11.54，空头动能增强
        <br>• RSI：22.14，已进入<strong style="color: #f87171;">超卖区域</strong>，短期或有技术性反弹
        </p>
        <p style="margin: 0 0 8px 0;"><strong style="color: #60a5fa;">【资金面与基本面】</strong>主力资金单日净流出3.32亿，国轩高科上半年减持839.95万股也给市场带来抛压预期。但公司Q1净利润同比+2138%，业绩爆发式增长，PET铜箔+高频高速PCB铜箔双轮驱动，长期成长逻辑清晰。</p>
        <p style="margin: 0 0 8px 0;"><strong style="color: #c084fc;">【操作建议】</strong>
        <br>• RSI超卖(22.14)，短期有技术性反弹需求，但下跌趋势已形成
        <br>• 反弹至<strong style="color: #4ade80;">140元以上</strong>时减仓1/3，降低持仓风险
        <br>• 若跌破<strong style="color: #f87171;">128元</strong>，坚决止损出局，下方空间打开
        <br>• 中期等企稳信号：缩量至20亿以下+站稳MA10再考虑
        <br>• 仓位建议：减至1/4仓位，严控风险
        </p>
        </div>
        """
    },
    {
        "name": "雅克科技",
        "code": "002409",
        "price": "207.17",
        "change": "-0.88%",
        "up": False,
        "volume": "约100.2亿",
        "turnover": "4.55%",
        "high": "229.00",
        "low": "207.00",
        "analysis": """
        <div style="line-height: 1.8; font-size: 13px; color: var(--text-secondary);">
        <p style="margin: 0 0 8px 0;"><strong style="color: #fbbf24;">【当日表现】</strong>雅克科技今日收跌0.88%报207.17元，成交额约100.2亿。盘中最高229元(早盘冲高+9.6%)，午后跟随半导体板块大幅回落，最低探至207元，振幅高达10.5%。在半导体板块整体暴跌5.32%的背景下，雅克科技仅跌0.88%，表现<strong style="color: #4ade80;">相对抗跌</strong>，显示资金认可度较高。</p>
        <p style="margin: 0 0 8px 0;"><strong style="color: #fbbf24;">【技术面判断】</strong>
        <br>• 均线系统：MA5(195.69)在上，MA10(205.85)今日盘中被短暂跌破后收回，MA20(181.57)支撑强劲
        <br>• 支撑位：<strong style="color: #4ade80;">200-205元</strong>(MA10区域)为第一支撑，跌破看175元强支撑
        <br>• 压力位：230元(今日高点+前期高点246.44元)为强压力区
        <br>• MACD：DIF 20.96，DEA 22.11，绿柱放大，短期调整信号
        <br>• RSI：62.97，处于正常区间，未超买
        <br>• 缺口：下方存在多个跳空缺口(85.5/116.9/110元)，中长期支撑稳固
        </p>
        <p style="margin: 0 0 8px 0;"><strong style="color: #60a5fa;">【基本面与资金面】</strong>雅克科技是半导体材料平台型龙头，覆盖光刻胶、电子特气、前驱体三大高景气赛道。存储芯片产业链景气上行+国产替代加速是核心逻辑。今日在板块暴跌中仍能维持近红盘，说明机构持仓稳定、抛压相对有限。</p>
        <p style="margin: 0 0 8px 0;"><strong style="color: #c084fc;">【操作建议】</strong>
        <br>• 四只持仓中<strong style="color: #4ade80;">最抗跌的标的</strong>，半导体材料龙头地位稳固
        <br>• 若回调至<strong style="color: #4ade80;">200元以下</strong>，可考虑加仓1/4，博弈半导体板块超跌反弹
        <br>• 若跌破<strong style="color: #f87171;">180元</strong>(MA20下方)，止损减仓至1/2
        <br>• 反弹至<strong style="color: #4ade80;">225元以上</strong>可减仓1/4做波段
        <br>• 中长期坚定看好，存储芯片产业链+半导体材料国产替代双逻辑
        </p>
        </div>
        """
    },
    {
        "name": "*ST建艺",
        "code": "002789",
        "price": "10.21",
        "change": "-1.64%",
        "up": False,
        "volume": "2164万",
        "turnover": "1.34%",
        "high": "10.50",
        "low": "10.17",
        "analysis": """
        <div style="line-height: 1.8; font-size: 13px; color: var(--text-secondary);">
        <p style="margin: 0 0 8px 0;"><strong style="color: #f87171;">【当日表现】</strong>*ST建艺今日收跌1.64%报10.21元，成交额2164万元，换手率1.34%。盘中最高10.50元，最低10.17元，继续沿下降通道下行。主力资金净流出213.52万，连续3日被主力资金减仓。公司Q1营收-35.21%、净利亏损5311万，基本面未见改善。</p>
        <p style="margin: 0 0 8px 0;"><strong style="color: #fbbf24;">【技术面判断】</strong>
        <br>• 均线系统：MA5(10.53)、MA10(11.15)、MA20(12.24)全部失守，典型空头排列
        <br>• 支撑位：10元整数关口为短期心理支撑，跌破看9.7元(前期低点)
        <br>• 压力位：10.5-11元(MA5+MA10区域)
        <br>• MACD：DIF-0.75，DEA-0.52，绿柱缩小但仍在零轴下方
        <br>• RSI：17.97，<strong style="color: #f87171;">严重超卖</strong>，但ST股超卖可能持续
        <br>• 筹码：平均成本12.43元，当前套牢盘沉重
        </p>
        <p style="margin: 0 0 8px 0;"><strong style="color: #60a5fa;">【基本面与风险】</strong>公司主营建筑装饰，受房地产行业下行冲击明显。一季度营收大幅下滑，持续亏损。虽有横琴新区、创投等概念，但主业不振难以支撑估值。ST身份意味着退市风险，需高度警惕。</p>
        <p style="margin: 0 0 8px 0;"><strong style="color: #c084fc;">【操作建议】</strong>
        <br>• <strong style="color: #f87171;">坚决回避，不可加仓</strong>，ST股在当前市场环境下风险收益比极差
        <br>• 若反弹至<strong style="color: #4ade80;">10.5元以上</strong>，应果断清仓离场
        <br>• 若跌破<strong style="color: #f87171;">10元整数关口</strong>，不计成本止损，下方空间巨大
        <br>• 主板ST涨跌幅已扩至10%，波动风险进一步加大
        <br>• 仓位建议：清仓，将资金转移至雅克科技等有基本面支撑的优质标的
        </p>
        </div>
        """
    },
]
gen.add_holdings_tracking(holdings)

# ============================================================
# 5. 龙虎榜深度解读
# ============================================================
dragon_stocks = [
    {
        "name": "紫光股份",
        "code": "000938",
        "change": "+7.65%",
        "price": "38.41",
        "net_buy": "22.48亿(三日榜)",
        "analysis": """
        <div style="line-height: 1.8; font-size: 13px; color: var(--text-secondary);">
        <p><strong style="color: #fbbf24;">【席位拆解】</strong>三日榜数据显示，龙虎榜总净买入22.48亿：</p>
        <ul style="margin: 6px 0; padding-left: 20px;">
            <li>深股通(北向资金)：净买入<strong style="color: #4ade80;">15.14亿</strong>(买35.19亿/卖20.05亿)，北向资金大举加仓</li>
            <li>机构席位：3家机构合计净买入约<strong style="color: #4ade80;">2.86亿</strong>，机构态度偏多</li>
            <li>顶级游资：国泰海通湛江万豪世家净买入4.49亿(买4.52亿/卖247万)，"湛江帮"重仓押注</li>
        </ul>
        <p style="margin: 6px 0;"><strong style="color: #c084fc;">【持续性判断】</strong>
        <br>• <strong style="color: #4ade80;">持续性评级：A级</strong>——百亿级成交(185.73亿)+北向+机构+顶级游资三方共振，属于趋势性大资金配置而非纯游资炒作
        <br>• 公司Q1营收+34.61%、净利+126%，AI业务落地头部客户，基本面支撑强
        <br>• 与工业富联(中报预增93-101%)形成AI算力"算电协同"双龙头格局
        <br>• 风险点：三日榜累计涨幅已达20%偏离值，短期或有获利回吐压力
        </p>
        <p style="margin: 0;"><strong style="color: #fbbf24;">【操作参考】</strong>35-36元区间可低吸，目标价42-45元；跌破33元止损。</p>
        </div>
        """,
        "seats": "北向+机构+湛江帮(游资)"
    },
    {
        "name": "金风科技",
        "code": "002202",
        "change": "+9.99%",
        "price": "22.36",
        "net_buy": "7.62亿",
        "analysis": """
        <div style="line-height: 1.8; font-size: 13px; color: var(--text-secondary);">
        <p><strong style="color: #fbbf24;">【席位拆解】</strong>单日涨幅偏离榜，总净买入7.62亿：</p>
        <ul style="margin: 6px 0; padding-left: 20px;">
            <li>深股通(北向)：净买入<strong style="color: #4ade80;">4.28亿</strong>(买5.12亿/卖8438万)，北向大幅加仓</li>
            <li>机构席位：3家机构合计净买入约<strong style="color: #4ade80;">3.50亿</strong>，机构认可度高</li>
            <li>游资：国泰海通湛江万豪世家买入8997万，几乎无卖出</li>
        </ul>
        <p style="margin: 6px 0;"><strong style="color: #c084fc;">【持续性判断】</strong>
        <br>• <strong style="color: #4ade80;">持续性评级：A-级</strong>——北向+机构双主导，属于趋势性资金回流，而非纯题材炒作
        <br>• 催化因素：海风装机加速+风电出海逻辑+电力设备板块内高低切换
        <br>• 公司Q1营收+63.48%、净利+59.65%，基本面拐点确认
        <br>• 风电板块今日内部分化：金风、明阳强势，但储能/锂电链重挫，需关注板块联动性
        <br>• 风险点：成交额58.10亿属放量涨停，周一需观察封板资金承接力
        </p>
        <p style="margin: 0;"><strong style="color: #fbbf24;">【操作参考】</strong>20-21元区间可低吸，目标价26-28元；跌破19元止损。</p>
        </div>
        """,
        "seats": "北向+机构主导"
    },
    {
        "name": "中鼎股份",
        "code": "000887",
        "change": "+10.00%",
        "price": "待查",
        "net_buy": "4.65亿(三日榜)",
        "analysis": """
        <div style="line-height: 1.8; font-size: 13px; color: var(--text-secondary);">
        <p><strong style="color: #fbbf24;">【席位拆解】</strong>三日榜涨停偏离，机构净买入10.61亿(6家机构买入/6家卖出)：</p>
        <ul style="margin: 6px 0; padding-left: 20px;">
            <li>机构席位：6家机构买入、6家卖出，<strong style="color: #fbbf24;">净买入10.61亿</strong>，机构博弈剧烈但多头占优</li>
            <li>主题：人形机器人+汽车零部件+空气悬挂</li>
            <li>机器人链弹性标的，短线资金接力明显</li>
        </ul>
        <p style="margin: 6px 0;"><strong style="color: #c084fc;">【持续性判断】</strong>
        <br>• <strong style="color: #fbbf24;">持续性评级：B+级</strong>——机构多空博弈剧烈，说明分歧较大；但人形机器人是中长期主线
        <br>• 公司是汽车底盘+空气悬架龙头，人形机器人产业链核心零部件供应商
        <br>• 机构虽然净买入量大，但买卖双方都有6家，意味着部分机构在高位兑现
        <br>• 高波动特征明显，适合短线交易不适合追高
        </p>
        <p style="margin: 0;"><strong style="color: #fbbf24;">【操作参考】</strong>回调至5日均线可轻仓试错，目标价看前期高点；跌破10日线止损。</p>
        </div>
        """,
        "seats": "机构博弈(多头占优)"
    },
    {
        "name": "兆易创新",
        "code": "603986",
        "change": "-7.76%",
        "price": "待查",
        "net_buy": "机构净卖出5.01亿",
        "analysis": """
        <div style="line-height: 1.8; font-size: 13px; color: var(--text-secondary);">
        <p><strong style="color: #f87171;">【席位拆解】</strong>兆易创新今日暴跌7.76%，成交额594亿创历史纪录：</p>
        <ul style="margin: 6px 0; padding-left: 20px;">
            <li>机构席位：<strong style="color: #f87171;">净卖出5.01亿</strong>(1家机构买入/1家卖出)，机构态度偏空</li>
            <li>沪股通成交57.91亿，为今日沪股通成交榜首</li>
            <li>属于半导体板块集体回调的核心标的，公募基金集中止盈兑现</li>
        </ul>
        <p style="margin: 6px 0;"><strong style="color: #c084fc;">【持续性判断】</strong>
        <br>• <strong style="color: #f87171;">持续性评级：B-级(下跌趋势确认)</strong>——594亿天量成交意味着巨量筹码交换，短期抛压沉重
        <br>• 但公司存储芯片主业景气度向上，业绩高增长逻辑未变，中期价值仍在
        <br>• 短期属于情绪性杀跌+获利盘兑现，跌速快但不代表趋势反转
        <br>• 关注下周能否在关键支撑位止跌企稳
        </p>
        <p style="margin: 0;"><strong style="color: #fbbf24;">【操作参考】</strong>不建议抄底，等缩量企稳信号(成交缩至200亿以下+站稳5日线)再考虑。</p>
        </div>
        """,
        "seats": "机构净卖出+天量成交"
    },
]
gen.add_dragon_tiger_list(dragon_stocks)

# ============================================================
# 6. 重点关注标的（3只）
# ============================================================
focus_html = """
<div style="display: flex; flex-direction: column; gap: 16px;">
    
    <div style="background: linear-gradient(135deg, rgba(34, 197, 94, 0.1), rgba(16, 185, 129, 0.05)); border: 1px solid rgba(34, 197, 94, 0.3); border-radius: 12px; padding: 16px;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
            <div style="display: flex; align-items: center; gap: 8px;">
                <span style="background: #22c55e; color: white; padding: 2px 8px; border-radius: 4px; font-size: 11px; font-weight: 700;">关注1</span>
                <span style="font-weight: 700; color: var(--text-primary); font-size: 16px;">紫光股份 000938</span>
                <span style="color: #fbbf24; font-size: 12px;">AI算力·机构抱团</span>
            </div>
            <div style="text-align: right;">
                <div style="font-size: 18px; font-weight: 700; color: var(--text-primary);">38.41</div>
                <div style="color: #22c55e; font-size: 12px;">+7.65%</div>
            </div>
        </div>
        <div style="color: var(--text-secondary); font-size: 13px; line-height: 1.7;">
            <p style="margin: 0 0 8px 0;"><strong style="color: #4ade80;">核心逻辑：</strong></p>
            <ul style="margin: 0 0 8px 0; padding-left: 18px;">
                <li>AI算力基础设施龙头，ICT全栈布局，受益于智算中心建设大潮</li>
                <li>Q1营收+34.61%、净利+126%，AI业务已落地头部互联网客户</li>
                <li>龙虎榜三日净买入22.48亿，北向+机构+顶级游资三方共振，趋势性大资金配置</li>
                <li>与工业富联(中报预增93-101%)形成AI算力"算电协同"双龙头</li>
            </ul>
            <p style="margin: 0 0 6px 0;"><strong style="color: #4ade80;">目标价：</strong>42-45元(对应2026年35-38倍PE)</p>
            <p style="margin: 0 0 6px 0;"><strong style="color: #f87171;">止损位：</strong>33元(跌破20日线止损)</p>
            <p style="margin: 0;"><strong style="color: #fbbf24;">买点建议：</strong>回调至35-36元区间分批建仓，仓位不超过总仓位15%</p>
        </div>
    </div>
    
    <div style="background: linear-gradient(135deg, rgba(59, 130, 246, 0.1), rgba(99, 102, 241, 0.05)); border: 1px solid rgba(59, 130, 246, 0.3); border-radius: 12px; padding: 16px;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
            <div style="display: flex; align-items: center; gap: 8px;">
                <span style="background: #3b82f6; color: white; padding: 2px 8px; border-radius: 4px; font-size: 11px; font-weight: 700;">关注2</span>
                <span style="font-weight: 700; color: var(--text-primary); font-size: 16px;">金风科技 002202</span>
                <span style="color: #93c5fd; font-size: 12px;">风电·趋势资金回流</span>
            </div>
            <div style="text-align: right;">
                <div style="font-size: 18px; font-weight: 700; color: var(--text-primary);">22.36</div>
                <div style="color: #22c55e; font-size: 12px;">+9.99%</div>
            </div>
        </div>
        <div style="color: var(--text-secondary); font-size: 13px; line-height: 1.7;">
            <p style="margin: 0 0 8px 0;"><strong style="color: #60a5fa;">核心逻辑：</strong></p>
            <ul style="margin: 0 0 8px 0; padding-left: 18px;">
                <li>风电整机龙头，Q1营收+63.48%、净利+59.65%，行业拐点确认</li>
                <li>海风装机加速+大兆瓦机组占比提升+海外订单增长，三重驱动</li>
                <li>龙虎榜北向净买入4.28亿+机构净买入3.50亿，趋势资金回流明显</li>
                <li>电力设备板块内高低切换——资金从高估值储能/锂电转向低估值风电</li>
            </ul>
            <p style="margin: 0 0 6px 0;"><strong style="color: #4ade80;">目标价：</strong>26-28元(对应2026年20-22倍PE)</p>
            <p style="margin: 0 0 6px 0;"><strong style="color: #f87171;">止损位：</strong>19元(跌破10日线止损)</p>
            <p style="margin: 0;"><strong style="color: #fbbf24;">买点建议：</strong>20-21元区间低吸，仓位不超过总仓位10%</p>
        </div>
    </div>
    
    <div style="background: linear-gradient(135deg, rgba(168, 85, 247, 0.1), rgba(139, 92, 246, 0.05)); border: 1px solid rgba(168, 85, 247, 0.3); border-radius: 12px; padding: 16px;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
            <div style="display: flex; align-items: center; gap: 8px;">
                <span style="background: #a855f7; color: white; padding: 2px 8px; border-radius: 4px; font-size: 11px; font-weight: 700;">关注3</span>
                <span style="font-weight: 700; color: var(--text-primary); font-size: 16px;">常山药业 300255</span>
                <span style="color: #d8b4fe; font-size: 12px;">创新药·板块爆发龙头</span>
            </div>
            <div style="text-align: right;">
                <div style="font-size: 18px; font-weight: 700; color: var(--text-primary);">涨停</div>
                <div style="color: #22c55e; font-size: 12px;">+20.00%</div>
            </div>
        </div>
        <div style="color: var(--text-secondary); font-size: 13px; line-height: 1.7;">
            <p style="margin: 0 0 8px 0;"><strong style="color: #c084fc;">核心逻辑：</strong></p>
            <ul style="margin: 0 0 8px 0; padding-left: 18px;">
                <li>医药板块今日爆发，常山药业20cm涨停领涨，机构净买入4.09亿</li>
                <li>GLP-1减肥药龙头之一，艾本那肽三期临床推进中，市场空间广阔</li>
                <li>医药板块经历两年调整后估值处于历史低位，具备超跌反弹基础</li>
                <li>资金从高位科技流向低位医药的趋势性切换，板块持续性值得关注</li>
            </ul>
            <p style="margin: 0 0 6px 0;"><strong style="color: #fbbf24;">风险提示：</strong>纯题材炒作性质较重，医药板块反转尚需业绩验证，不建议追高</p>
            <p style="margin: 0 0 6px 0;"><strong style="color: #4ade80;">目标价：</strong>短期看前高附近，空间约15-20%</p>
            <p style="margin: 0;"><strong style="color: #f87171;">止损位：</strong>跌破5日线止损，短线快进快出</p>
        </div>
    </div>
    
</div>
"""
gen._components.append(Section(title="🎯 重点关注标的", content=focus_html, icon="target"))

# ============================================================
# 7. 明日操作策略
# ============================================================
plan_html = """
<div style="line-height: 1.8; font-size: 13px; color: var(--text-secondary);">
    
    <div style="background: var(--glass-bg); border: 1px solid var(--glass-border); border-radius: 12px; padding: 16px; margin-bottom: 16px;">
        <div style="font-weight: 600; color: var(--text-primary); margin-bottom: 10px; display: flex; align-items: center; gap: 8px;">
            <span>📈</span><span>周一(7/13)大盘判断</span>
        </div>
        <ul style="margin: 0; padding-left: 18px;">
            <li><strong style="color: #fbbf24;">整体判断：</strong>震荡探底后有望企稳回升。周五放量大跌释放了大量抛压，下周一大盘大概率低开，3950-4000点区间是重要支撑区域</li>
            <li><strong style="color: #fbbf24;">沪指支撑：</strong>第一支撑<strong style="color: #f87171;">3950点</strong>，第二支撑<strong style="color: #f87171;">3900点</strong>(前期平台)</li>
            <li><strong style="color: #fbbf24;">沪指压力：</strong>第一压力<strong style="color: #4ade80;">4050点</strong>，第二压力<strong style="color: #4ade80;">4080点</strong></li>
            <li><strong style="color: #fbbf24;">成交量：</strong>预计缩量至2.8-3万亿区间，放量下跌后需缩量企稳</li>
            <li><strong style="color: #fbbf24;">关键变量：</strong>周末消息面(政策/外盘/业绩预告)、半导体板块能否止跌、北向资金流向</li>
        </ul>
    </div>
    
    <div style="background: var(--glass-bg); border: 1px solid var(--glass-border); border-radius: 12px; padding: 16px; margin-bottom: 16px;">
        <div style="font-weight: 600; color: var(--text-primary); margin-bottom: 10px; display: flex; align-items: center; gap: 8px;">
            <span>💰</span><span>仓位建议</span>
        </div>
        <ul style="margin: 0; padding-left: 18px;">
            <li><strong style="color: #c084fc;">总仓位：</strong>建议控制在<strong style="color: #fbbf24;">40%-50%</strong>区间，保持足够现金应对波动</li>
            <li><strong style="color: #c084fc;">持仓结构：</strong>从"高位科技单压"转向"科技+防御均衡配置"</li>
            <li><strong style="color: #c084fc;">科技仓位：</strong>降至20-25%，以雅克科技等半导体材料龙头为核心，减仓液冷/铜箔等高位标的</li>
            <li><strong style="color: #c084fc;">防御仓位：</strong>增配15-20%医药(创新药/CXO)+风电(金风/明阳)，对冲科技回调风险</li>
            <li><strong style="color: #c084fc;">现金仓位：</strong>保留30-40%，等待科技板块企稳后再加仓</li>
        </ul>
    </div>
    
    <div style="background: var(--glass-bg); border: 1px solid var(--glass-border); border-radius: 12px; padding: 16px; margin-bottom: 16px;">
        <div style="font-weight: 600; color: var(--text-primary); margin-bottom: 10px; display: flex; align-items: center; gap: 8px;">
            <span>📋</span><span>具体买卖计划</span>
        </div>
        <div style="display: flex; flex-direction: column; gap: 10px;">
            
            <div style="background: rgba(248, 113, 113, 0.08); border-left: 3px solid #f87171; padding: 10px 12px; border-radius: 0 8px 8px 0;">
                <div style="font-weight: 600; color: #fca5a5; margin-bottom: 4px;">🔴 减仓/止损计划</div>
                <ul style="margin: 0; padding-left: 18px; font-size: 12.5px;">
                    <li><strong>*ST建艺：</strong>反弹至<strong style="color: #fca5a5;">10.5元以上</strong>清仓；跌破<strong style="color: #fca5a5;">10元</strong>不计成本止损</li>
                    <li><strong>铜冠铜箔：</strong>反弹至<strong style="color: #fca5a5;">140元以上</strong>减仓1/3；跌破<strong style="color: #fca5a5;">128元</strong>止损</li>
                    <li><strong>英维克：</strong>反弹至<strong style="color: #fca5a5;">76元以上</strong>减仓1/3；跌破<strong style="color: #fca5a5;">70元</strong>止损离场</li>
                </ul>
            </div>
            
            <div style="background: rgba(34, 197, 94, 0.08); border-left: 3px solid #22c55e; padding: 10px 12px; border-radius: 0 8px 8px 0;">
                <div style="font-weight: 600; color: #4ade80; margin-bottom: 4px;">🟢 加仓/买入计划</div>
                <ul style="margin: 0; padding-left: 18px; font-size: 12.5px;">
                    <li><strong>雅克科技：</strong>回调至<strong style="color: #4ade80;">200元以下</strong>加仓1/4(从ST建艺腾出的资金)</li>
                    <li><strong>紫光股份：</strong>回调至<strong style="color: #4ade80;">35-36元区间</strong>建仓10%仓位</li>
                    <li><strong>金风科技：</strong>回调至<strong style="color: #4ade80;">20-21元区间</strong>建仓8%仓位</li>
                </ul>
            </div>
            
            <div style="background: rgba(251, 191, 36, 0.08); border-left: 3px solid #fbbf24; padding: 10px 12px; border-radius: 0 8px 8px 0;">
                <div style="font-weight: 600; color: #fcd34d; margin-bottom: 4px;">🟡 持有观察计划</div>
                <ul style="margin: 0; padding-left: 18px; font-size: 12.5px;">
                    <li><strong>雅克科技：</strong>200-230元区间持有，做核心底仓</li>
                    <li><strong>半导体板块整体：</strong>观察周一能否在大跌后缩量企稳，是判断调整深度的关键</li>
                    <li><strong>商业航天/军工：</strong>观察板块持续性，若周一继续涨停潮可小仓位参与龙头</li>
                </ul>
            </div>
            
        </div>
    </div>
    
    <div style="background: var(--glass-bg); border: 1px solid var(--glass-border); border-radius: 12px; padding: 16px;">
        <div style="font-weight: 600; color: var(--text-primary); margin-bottom: 10px; display: flex; align-items: center; gap: 8px;">
            <span>🧠</span><span>核心策略思路</span>
        </div>
        <p style="margin: 0 0 8px 0;">当前市场处于<strong style="color: #fbbf24;">风格切换的关键节点</strong>。周五的极致分化(指数跌、个股涨；科技跌、低位涨)不是一天就能完成切换的，需要时间验证。</p>
        <p style="margin: 0 0 8px 0;">短期操作上，<strong style="color: #f87171;">降低高位科技仓位、适度分散到低位防御板块</strong>是明智之举。但中期来看，AI算力、半导体国产替代、人形机器人等主线的产业逻辑没有变化，调整之后优质标的仍然是布局机会。</p>
        <p style="margin: 0;">关键原则：<strong style="color: #4ade80;">不追高、不抄底、等确认</strong>。高位科技股反弹减仓，低位新主线等确认后再介入，保持仓位灵活性，以应对市场的剧烈波动。</p>
    </div>
    
</div>
"""
gen.add_trading_plan(plan_html)

# ============================================================
# 8. 风险提示
# ============================================================
risks = [
    "半导体板块调整风险：科创50单日暴跌5.53%，电子板块跌5.32%，高位科技股获利盘巨大，调整可能持续1-2周，需警惕进一步下探风险",
    "公募止盈压力：7月10日是半年排名收官日，但基金减仓可能延续到下周，高位赛道股抛压未完全释放",
    "北向资金流向不确定性：北向今日净流出102.66亿，若外资持续减仓A股科技龙头，将进一步压制指数",
    "监管风险：交易所对中船特气等暴涨标的实施重点监控，短线游资退潮可能引发高位次新股、题材股批量跌停",
    "外围市场风险：美股科技股高位震荡、美联储政策不确定性、地缘局势紧张，可能通过情绪面传导至A股",
    "*ST建艺退市风险：公司持续亏损、营收下滑，ST身份叠加主板10%涨跌幅，波动风险和退市风险并存，坚决回避",
]
gen.add_risk_warning(risks)

# ============================================================
# 晚间重要新闻
# ============================================================
evening_news = [
    {"title": "长征十号乙运载火箭首飞成功", "content": "我国新一代载人运载火箭长征十号乙遥一运载火箭在我国文昌航天发射场点火升空，成功将载有飞船的组合体送入预定轨道，发射任务获得圆满成功。商业航天板块午后掀起涨停潮。", "time": "14:30", "source": "新华社", "tag": "航天", "tag_variant": "primary"},
    {"title": "北向资金二季度持仓首破3万亿", "content": "截至2026年二季度末，北向资金持有A股市值首次突破3万亿达3.13万亿，创历史新高。电子行业增持最多，净买入2193亿创季度纪录。长线外资是回流主力。", "time": "盘后", "source": "界面新闻", "tag": "北向资金", "tag_variant": "success"},
    {"title": "兆易创新成交额594亿创历史纪录", "content": "兆易创新今日收跌7.76%，成交额达594亿元，创该股历史最高成交纪录。机构席位净卖出5.01亿，存储芯片板块高位筹码大规模交换。", "time": "收盘", "source": "东方财富", "tag": "半导体", "tag_variant": "warning"},
    {"title": "工业富联：上半年净利润同比预增93%-101%", "content": "预计2026年上半年归母净利润234亿-244亿元，同比增长93%-101%。AI服务器需求持续旺盛，云计算及企业网络业务收入大幅增长。", "time": "盘后", "source": "公司公告", "tag": "业绩", "tag_variant": "success"},
]
gen.add_evening_news(evening_news)

# ============================================================
# 业绩预增追踪
# ============================================================
gen.add_earnings_forecast()

# ============================================================
# 发布
# ============================================================
result = gen.publish(
    title="盘后速递",
    report_type="aftermarket",
    excerpt="2026.07.10 周五 · 沪指失守4000点跌1%，创业板指跌4.37%，科创50暴跌5.53%。半导体重挫，传媒军工医药爆发。4持仓全跌，龙虎榜紫光股份22亿净买入独撑AI算力。"
)

print("✅ 发布完成")
print(f"文件: {result.get('file_path', 'N/A')}")
print(f"latest: {result.get('latest_path', 'N/A')}")
