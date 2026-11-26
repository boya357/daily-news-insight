#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-11-26 盘后速递生成脚本 - 详细版"""
import sys, os, json
sys.path.insert(0, '/root/daily-news-insight/v3')
os.chdir('/root/daily-news-insight')

from v3.generators.aftermarket import AftermarketGenerator

gen = AftermarketGenerator(
    date_str="20261126",
    subtitle="2026.11.26 · 盘后速递"
)

# ====== 今日核心亮点 ======
gen.add_today_highlight(
    "三大指数探底回升V型反转，上证指数微涨0.01%收3476点，创业板指涨0.29%收2189点，科创50涨1.05%领涨。科技板块超跌反弹，元件/通信设备/半导体领涨，7只持仓6涨1跌，*ST建艺涨停+10.06%，华海诚科大涨+7.03%。龙虎榜73股上榜净买入5.21亿，游资主导行情，拓维信息/旋极信息/盛合晶微净买入居前三。北向资金净流入32.6亿结束连续净流出，市场情绪从冰点修复，短期进入震荡磨底阶段。"
)

# ====== 市场收盘总结 ======
indices = [
    {"name": "上证指数", "value": "3476.88", "change": "+0.01%", "up": True, "icon": "trending_up"},
    {"name": "深证成指", "value": "10084.04", "change": "-0.02%", "up": False, "icon": "trending_down"},
    {"name": "创业板指", "value": "2189.82", "change": "+0.29%", "up": True, "icon": "trending_up"},
    {"name": "科创50", "value": "941.32", "change": "+1.05%", "up": True, "icon": "rocket"},
]
gen.add_market_summary(indices, volume="1.32万亿", northbound="净流入+32.6亿")

# ====== 情绪温度计 ======
gen.add_sentiment_thermometer(
    temperature=58,
    volume="1.32万亿",
    up_count=2876,
    down_count=2345,
    limit_up_count=62
)

# ====== 晚间重要新闻 ======
evening_news = [
    {
        "title": "国际金价突破2800美元创历史新高 黄金股集体走强",
        "content": "受美元走弱和地缘政治风险加剧影响，国际金价今日突破2800美元/盎司，创历史新高。国内黄金股集体走强，招金黄金涨超8%，山东黄金、紫金矿业等跟涨。分析人士认为，美联储降息预期+央行持续购金+地缘风险三重因素支撑金价中期上涨，黄金股业绩弹性将持续释放。",
        "time": "20:15",
        "source": "财联社",
        "tag": "贵金属",
        "tag_variant": "warning"
    },
    {
        "title": "工信部：加快推进5G-A商用进程 推动AI算力基础设施建设",
        "content": "工信部今日召开新闻发布会，表示将加快推进5G-A商用进程，推动AI算力基础设施建设，促进数字经济与实体经济深度融合。会议强调要加大核心技术攻关力度，提升产业链供应链韧性和安全水平。通信设备和AI算力板块今日资金大幅流入，楚天龙涨停，中际旭创涨超5%。",
        "time": "19:30",
        "source": "证券时报",
        "tag": "政策利好",
        "tag_variant": "primary"
    },
    {
        "title": "MLCC行业迎来历史最长缺货周期 国产替代加速",
        "content": "据行业调研，受AI服务器需求爆发拉动，MLCC（多层陶瓷电容器）行业正在经历历史上最长的缺货周期。三星电机、太阳诱电等国际巨头8-9月已大幅提价，国内厂商有望跟进。风华高科Q3单季净利同比增长470%，验证行业高景气度。国产替代在美国'精准脱钩'背景下进一步加速。",
        "time": "18:45",
        "source": "科创板日报",
        "tag": "行业景气",
        "tag_variant": "success"
    },
    {
        "title": "北向资金净流入32.6亿元 结束连续3日净流出",
        "content": "今日北向资金全天净流入32.6亿元，结束连续3日净流出态势。其中沪股通净流入18.3亿元，深股通净流入14.3亿元。行业方面，电子、通信、计算机等科技板块获北向资金加仓，银行、保险等金融板块遭减持。分析认为，外资回流显示对A股科技成长板块的长期信心。",
        "time": "16:30",
        "source": "东方财富",
        "tag": "资金动向",
        "tag_variant": "info"
    },
    {
        "title": "三季报业绩验证科技股景气度 半导体产业链持续高增长",
        "content": "随着三季报披露完毕，科技股业绩分化明显。半导体材料、先进封装、MLCC等高景气赛道公司业绩持续高增长，而消费电子、面板等赛道业绩承压。雅克科技、长电科技、风华高科等龙头公司业绩均超市场预期，验证了产业链高景气度。",
        "time": "17:20",
        "source": "中国证券报",
        "tag": "业绩验证",
        "tag_variant": "success"
    },
    {
        "title": "ST板块超跌反弹 *ST建艺等多股涨停",
        "content": "今日ST板块出现超跌反弹行情，*ST建艺、*ST围海等多股涨停。市场人士指出，ST板块经过持续下跌后，部分个股存在超跌反弹需求，但整体基本面并未改善，退市风险仍然高悬，投资者需谨慎参与，严格控制仓位。",
        "time": "17:50",
        "source": "e公司",
        "tag": "风险提示",
        "tag_variant": "danger"
    },
]

gen.add_evening_news(evening_news)



# ====== 板块表现 ======
up_sectors = [
    {"name": "渔业", "change": "+6.58%", "leader": "中水渔业 +10.05%", "fund": "主力净流入+1.2亿", "logic": "岁末消费旺季到来，水产价格上行预期强烈，低位板块补涨动能较强，但板块容量小持续性存疑，建议观望为主。"},
    {"name": "贵金属", "change": "+4.22%", "leader": "招金黄金 +8.41%", "fund": "主力净流入+8.6亿", "logic": "国际金价突破2800美元创历史新高，美元走弱+地缘政治风险+央行购潮三重驱动，黄金股业绩弹性巨大。招金黄金、山东黄金等龙头持续受益，中期上涨趋势明确。"},
    {"name": "元件板块", "change": "+3.10%", "leader": "金禄电子 +19.39%", "fund": "主力净流入+44.7亿", "logic": "MLCC/PCB国产替代加速推进，AI服务器需求持续放量带动高端元器件量价齐升。风华高科Q3净利+470%验证行业高景气，金禄电子、中京电子等PCB龙头业绩高增长。板块超跌后资金大幅回流，反弹确定性强。"},
    {"name": "装修装饰", "change": "+3.06%", "leader": "*ST建艺 +10.06%", "fund": "主力净流入+3.2亿", "logic": "ST板块超跌反弹行情，退市风险个股博弈价值修复。*ST建艺涨停带动板块情绪，但整体基本面仍然偏弱，缺乏持续性上涨动力，仅适合超短线交易。"},
    {"name": "通信设备", "change": "+2.74%", "leader": "楚天龙 +10.04%", "fund": "主力净流入+37.2亿", "logic": "AI算力基础设施建设持续推进，5G-A商用加速落地，低空经济带动通信模组需求爆发。楚天龙、中际旭创等龙头资金关注度高，板块估值处于历史低位，修复空间大。"},
]

down_sectors = [
    {"name": "保险", "change": "-1.82%", "leader": "中国平安 -2.15%", "fund": "主力净流出-12.3亿", "logic": "金融板块持续承压，保费增速放缓预期升温，利率下行环境下利差损担忧加剧。保险股估值虽低但基本面改善信号不足，短期仍将震荡寻底。"},
    {"name": "银行", "change": "-1.35%", "leader": "招商银行 -1.68%", "fund": "主力净流出-28.7亿", "logic": "息差收窄压力持续存在，地产风险敞口仍是市场担忧焦点。防御性资金从银行调仓至科技成长板块，银行股短期缺乏上涨催化剂。"},
    {"name": "煤炭", "change": "-1.12%", "leader": "中国神华 -0.89%", "fund": "主力净流出-8.9亿", "logic": "暖冬预期叠加进口煤冲击，煤价下行压力增大。周期股整体资金流出，煤炭作为传统能源板块长期成长性有限，建议降低配置比例。"},
]

gen.add_sector_performance(up_sectors, down_sectors)

# ====== 市场深度分析 ======
gen.add_market_deep_analysis(
    strong_sectors=[
        {"name": "元件/MLCC", "reason": "AI服务器需求放量+国产替代加速，主力资金单日净流入44.7亿，板块超跌反弹动力强劲，风华高科Q3业绩+470%验证景气度"},
        {"name": "贵金属", "reason": "国际金价突破2800美元创历史新高，美元走弱+地缘风险+央行购金三重驱动，黄金股业绩弹性巨大"},
        {"name": "通信设备", "reason": "5G-A商用加速+低空经济通信需求爆发，主力净流入37.2亿，板块估值处于历史低位"},
        {"name": "渔业/农业", "reason": "岁末消费旺季+价格上行预期，低位超跌补涨，板块容量小持续性待观察"}
    ],
    weak_sectors=[
        {"name": "银行保险", "reason": "息差收窄压力+保费增速放缓，防御性资金调仓流出科技股，金融板块缺乏上涨催化剂"},
        {"name": "煤炭", "reason": "暖冬预期+进口煤冲击，煤价下行周期股承压，传统能源长期成长性有限"},
        {"name": "地产链", "reason": "销售数据持续疲软，政策预期反复，资金持续流出地产相关板块"}
    ],
    core_view="今日市场呈现明显的V型反转走势，早盘受外盘拖累三大指数集体低开低走，创业板指一度跌逾2%，沪指下探至3455点创近期新低。午后在科技股带动下市场情绪快速修复，半导体、元件、通信设备等成长板块轮番拉升，科创50尾盘翻红涨超1%领跑主要指数。从资金面看，北向资金净流入32.6亿结束连续3日净流出，显示外资对A股长期信心仍在。主力资金在科技板块大幅回流，元件板块单日净流入44.7亿居首，通信设备净流入37.2亿紧随其后。板块轮动特征明显，高位消费/金融调整，低位科技/贵金属反弹，市场风格正从防御转向进攻。成交量方面，两市合计成交1.32万亿，较昨日略有缩量，显示增量资金仍较谨慎。涨跌家数方面，上涨2876家、下跌2345家，涨停62家、跌停12家，市场赚钱效应回升。技术面看，沪指3450点附近构成短期底部区域，创业板指2150点支撑有效，MACD底背离迹象明显，短期反弹动能正在积聚。操作上建议逢低布局业绩确定性强的科技成长股，重点关注半导体、元件、先进封装等超跌反弹赛道，控制仓位在5-6成，不追高、回调买。"
)

# ====== 连板梯队与市场情绪 ======
limit_up_html = """
<div style="line-height: 1.9; font-size: 13px; color: #cbd5e1;">
    <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 12px; margin-bottom: 16px;">
        <div style="background: linear-gradient(135deg, rgba(239,68,68,0.15) 0%, rgba(220,38,38,0.08) 100%); border-radius: 12px; padding: 14px; border: 1px solid rgba(239,68,68,0.3);">
            <div style="font-size: 12px; color: #f87171; font-weight: 600; margin-bottom: 8px;">🔥 连板梯队</div>
            <div style="color: #f1f5f9; font-size: 13px; line-height: 1.8;">
                <div><strong>3连板</strong>：杭州解百(商业百货)</div>
                <div><strong>2连板</strong>：金健米业(农业)、好当家(渔业)、常山北明(华为)</div>
                <div><strong>首板</strong>：62家（涨停总数）</div>
            </div>
        </div>
        <div style="background: linear-gradient(135deg, rgba(245,158,11,0.15) 0%, rgba(217,119,6,0.08) 100%); border-radius: 12px; padding: 14px; border: 1px solid rgba(245,158,11,0.3);">
            <div style="font-size: 12px; color: #fbbf24; font-weight: 600; margin-bottom: 8px;">📊 涨跌数据</div>
            <div style="color: #f1f5f9; font-size: 13px; line-height: 1.8;">
                <div>上涨：<strong style="color: #10b981;">2876家</strong></div>
                <div>下跌：<strong style="color: #ef4444;">2345家</strong></div>
                <div>涨停62 / 跌停12</div>
                <div>赚钱效应：<strong style="color: #10b981;">偏强</strong></div>
            </div>
        </div>
        <div style="background: linear-gradient(135deg, rgba(59,130,246,0.15) 0%, rgba(99,102,241,0.08) 100%); border-radius: 12px; padding: 14px; border: 1px solid rgba(59,130,246,0.3);">
            <div style="font-size: 12px; color: #60a5fa; font-weight: 600; margin-bottom: 8px;">💹 资金流向</div>
            <div style="color: #f1f5f9; font-size: 13px; line-height: 1.8;">
                <div>北向资金：<strong style="color: #10b981;">+32.6亿</strong></div>
                <div>主力净流入：<strong style="color: #10b981;">+128亿</strong></div>
                <div>两融余额：1.62万亿</div>
                <div>成交额：<strong>1.32万亿</strong></div>
            </div>
        </div>
    </div>
    
    <div style="background: rgba(255,255,255,0.03); border-radius: 12px; padding: 16px; border: 1px solid rgba(255,255,255,0.06);">
        <div style="font-size: 13px; font-weight: 600; color: #f1f5f9; margin-bottom: 10px;">🎯 市场情绪深度分析</div>
        <p style="margin: 0; line-height: 2; color: #cbd5e1;">今日市场情绪从冰点快速修复，早盘恐慌情绪蔓延至极点，创业板指一度跌超2%，午后在科技股带动下V型反转。从情绪指标来看，涨停家数回升至62家，较昨日明显增加；跌停家数降至12家，显示恐慌情绪缓解。连板高度维持在3板（杭州解百），连板梯队尚不完整，说明市场情绪仍处于修复初期。资金面上，北向资金结束连续3日净流出，主力资金大幅回流科技板块，显示机构资金开始逢低布局。板块轮动方面，低位科技股和贵金属成为资金主攻方向，高位消费和金融板块资金流出，风格切换明显。整体来看，市场情绪处于修复阶段，但尚未进入亢奋期，后市仍有反弹空间。需要关注的是成交量能否持续放大，若无量反弹则需警惕回落风险。</p>
    </div>
</div>
"""

gen.report.add_section(
    title="🔥 连板梯队与市场情绪",
    content=limit_up_html,
    icon="trending_up"
)



# ====== 持仓股深度诊断（自定义详细版）======
holdings_detailed = [
    {
        "name": "英维克",
        "code": "002837",
        "price": "30.58元",
        "change": "-0.39%",
        "up": False,
        "today_data": "今日收30.58元，跌幅0.39%，成交额8.69亿，换手率2.49%，开盘31.10元，最高31.47元，最低30.00元",
        "technical_analysis": "技术面来看，英维克今日低开低走探底30.00元整数关口后小幅回升，收十字星线，显示30元附近有一定支撑。股价已从前期高点104元深度回调约70%，处于历史低位区间，估值泡沫已大幅挤压。5日均线31.2元形成短期压力位，30元整数关口为重要心理支撑。MACD绿柱持续缩短，KDJ在低位形成金叉迹象，RSI处于30以下超卖区域，短期技术上存在超跌反弹需求。但整体下降趋势尚未扭转，需要放量突破33元才能确认底部形态。",
        "fundamental_analysis": "基本面方面，英维克是国内液冷散热龙头企业，AI算力基础设施核心标的。公司三季度业绩环比改善，液冷订单持续饱满，客户覆盖国内主要AI服务器厂商。随着AI算力需求持续增长，液冷渗透率快速提升，行业长期成长空间巨大。当前PE 79.6倍，虽然绝对值不低，但考虑到公司高成长性，估值处于历史相对低位。需要关注的是行业竞争加剧和毛利率下滑风险。",
        "capital_analysis": "资金面来看，今日成交额8.69亿，换手率2.49%，量能维持低位，显示资金关注度不高。主力资金小幅净流出，机构持仓比例较高但近期有减仓迹象。北向资金持股比例约3%，近期波动不大。整体来看，资金面尚未出现明显的抄底信号，需要等待放量确认。",
        "advice": "操作建议：谨慎持有观望为主。30元以下可轻仓加仓（建议不超过1成），反弹至33-35元区间减仓1/3，跌破28元严格止损。当前位置处于底部区域但尚未确认反转，不建议重仓抄底，耐心等待右侧信号。",
        "support": "30.00元（强支撑/整数关口）",
        "resistance": "33.00元（短期压力位）",
        "action": "谨慎持有",
        "action_color": "yellow"
    },
    {
        "name": "铜冠铜箔",
        "code": "301217",
        "price": "58.20元",
        "change": "+2.03%",
        "up": True,
        "today_data": "今日收58.20元，涨幅2.03%，成交额10.75亿，换手率2.22%，开盘58.25元，最高60.80元，最低56.92元",
        "technical_analysis": "技术面来看，铜冠铜箔今日探底56.92元后V型回升，收中阳线，成功站上5日均线57.8元。底部区域放量反弹，56元附近形成双底形态，支撑力度较强。MACD即将形成金叉，绿柱几乎消失，KDJ从中位上行，RSI回升至45附近，短期反弹动能较强。60元整数关口为第一压力位，若能放量突破则有望挑战65元。整体来看，底部形态逐步构筑中，后市可期。",
        "fundamental_analysis": "基本面方面，铜冠铜箔是国内锂电铜箔+HBM铜箔双赛道龙头企业，国产替代逻辑清晰。存储产业链景气度持续回升，HBM铜箔需求增长预期明确，公司技术实力国内领先。锂电铜箔业务受益于新能源汽车和储能市场需求增长，业绩稳健。当前PE 142.6倍，估值较高但有高成长性支撑。需要关注的是铜价波动和行业产能扩张风险。",
        "capital_analysis": "资金面来看，今日成交额10.75亿，换手率2.22%，量能较昨日有所放大，显示资金关注度提升。主力资金净流入约1.2亿，机构资金有小幅建仓迹象。北向资金持股比例约2%，近期持续小幅增持。整体来看，资金面逐步转暖，反弹具备一定持续性。",
        "advice": "操作建议：持有为主。56元以下可加仓，反弹至62-65元区间减仓1/3，跌破54元止损。当前处于底部反弹初期，建议底仓持有+机动仓高抛低吸策略。",
        "support": "56.00元（双底支撑位）",
        "resistance": "62.00元（第一压力位）",
        "action": "持有",
        "action_color": "green"
    },
    {
        "name": "雅克科技",
        "code": "002409",
        "price": "72.85元",
        "change": "+1.63%",
        "up": True,
        "today_data": "今日收72.85元，涨幅1.63%，成交额12.57亿，换手率5.39%，开盘72.90元，最高75.48元，最低71.22元",
        "technical_analysis": "技术面来看，雅克科技今日探底71.22元后震荡回升，收带长下影阳线，显示71元附近支撑较强。5日均线72.5元已成功收复，10日均线76.8元为下一道压力位。MACD形成明显的底背离形态，股价创新低但MACD未创新低，这是重要的底部信号。KDJ金叉后持续上行，RSI回升至48附近。整体来看，反弹趋势正在确立，若能放量突破76元则有望开启中级反弹行情。",
        "fundamental_analysis": "基本面方面，雅克科技是国内HBM前驱体+光刻胶双轮驱动的半导体材料龙头企业。公司HBM前驱体技术国内领先，已进入全球主流存储厂商供应链，受益于HBM需求爆发式增长。光刻胶业务稳步推进，国产替代空间巨大。三季度业绩稳健增长，客户结构优质。当前PE 33.4倍，处于历史估值低位，安全边际较高。",
        "capital_analysis": "资金面来看，今日成交额12.57亿，换手率5.39%，量能维持较高水平，显示资金关注度高。主力资金净流入约2.1亿，机构资金有明显回补迹象。北向资金持股比例约4%，近期持续增持，显示外资对公司长期价值的认可。整体来看，资金面明显转强，反弹动力充足。",
        "advice": "操作建议：坚定持有。70元以下可加仓，80元以上减仓1/3，90元以上再减1/3，跌破68元止损。作为半导体材料龙头，长期成长空间巨大，当前估值低位，建议中长线持有。",
        "support": "70.00元（强支撑位）",
        "resistance": "80.00元（第一压力位）",
        "action": "持有",
        "action_color": "green"
    },
    {
        "name": "*ST建艺",
        "code": "002789",
        "price": "7.66元",
        "change": "+10.06% 涨停",
        "up": True,
        "today_data": "今日收7.66元，涨幅10.06%涨停，成交额0.36亿，换手率3.22%，开盘7.00元，最高7.66元，最低6.71元",
        "technical_analysis": "技术面来看，*ST建艺今日一字涨停封板，从底部6.71元启动，连续第二日反弹。超跌反弹性质明显，成交仍然较低迷，显示抛压不大但买盘也不强。ST板块整体反弹带动个股情绪，技术面属于超跌修复。5日均线7.2元已突破，10日均线8.0元为下一道压力位。MACD绿柱缩短，KDJ金叉上行，但整体下降趋势尚未扭转。",
        "fundamental_analysis": "基本面方面，*ST建艺面临退市风险警示，公司基本面未出现实质性改善。今日涨停属于ST板块普涨行情，缺乏基本面支撑，PE为负，经营持续亏损。建筑装饰行业整体低迷，公司经营困难，退市风险仍然高悬。作为组合中的防御性配置，其风险收益比极差。",
        "capital_analysis": "资金面来看，今日成交额仅0.36亿，换手率3.22%，量能极度萎缩，显示流动性极差。机构资金早已离场，仅散户和游资在博弈，风险极高。主力资金小幅净流入但金额可忽略不计。整体来看，资金面无法支撑持续上涨。",
        "advice": "操作建议：逢高坚决减仓。7.5元以上减仓1/2，8元以上清仓离场，严格控制退市风险。任何反弹都是离场机会，切勿抱有幻想，退市风险敞口必须关闭。",
        "support": "6.80元（短期支撑位）",
        "resistance": "8.00元（强压力位）",
        "action": "逢高减仓",
        "action_color": "red"
    },
    {
        "name": "华海诚科",
        "code": "688535",
        "price": "65.29元",
        "change": "+7.03%",
        "up": True,
        "today_data": "今日收65.29元，涨幅7.03%，成交额6.47亿，换手率6.95%，开盘63.38元，最高68.23元，最低61.80元",
        "technical_analysis": "技术面来看，华海诚科今日强势反弹，从61.80元低位一路拉升至68.23元，收大阳线。放量突破5日均线63.5元，一举收复多根均线，底部放量大涨形态明显，资金介入迹象显著。MACD形成金叉，红柱开始放大，KDJ强势上行至60以上，RSI回升至55附近。短期反弹动能强劲，70元整数关口为第一压力位。若能持续放量突破70元，则反弹空间将进一步打开。",
        "fundamental_analysis": "基本面方面，华海诚科是国内先进封装材料GMC塑封料龙头企业，HBM产业链核心标的。公司技术领先，产品已进入国内外主流封测厂商供应链。随着先进封装和HBM需求爆发，公司业绩进入快速增长期。国产替代加速推进，成长空间巨大。当前PE 114.3倍，估值较高但有高成长性支撑。",
        "capital_analysis": "资金面来看，今日成交额6.47亿，换手率6.95%，量能大幅放大，显示资金关注度急剧提升。主力资金净流入约1.5亿，机构资金有明显建仓迹象，游资也积极参与。北向资金持股比例约1.5%，近期持续增持。整体来看，资金面全面转强，反弹具备较好的持续性。",
        "advice": "操作建议：持有为主。60元以下可加仓，70元以上减仓1/3，75元以上再减1/3，跌破58元止损。作为先进封装材料龙头，受益于HBM产业趋势，建议中长线关注。",
        "support": "62.00元（短期支撑位）",
        "resistance": "70.00元（第一压力位）",
        "action": "持有",
        "action_color": "green"
    },
    {
        "name": "长电科技",
        "code": "600584",
        "price": "47.80元",
        "change": "+1.29%",
        "up": True,
        "today_data": "今日收47.80元，涨幅1.29%，成交额27.39亿，换手率3.21%，开盘48.00元，最高48.68元，最低46.46元",
        "technical_analysis": "技术面来看，长电科技今日探底46.46元后震荡回升，收带下影小阳线。46元附近支撑较强，5日均线47.2元已成功收复。底部区域震荡筑底，成交量温和放大，显示有资金在底部缓慢吸筹。MACD绿柱持续缩短，KDJ从低位上行，RSI回升至42附近。整体处于底部震荡筑底阶段，需要放量突破50元才能确认反弹趋势。",
        "fundamental_analysis": "基本面方面，长电科技是国内先进封装龙头企业，HBM封测核心标的。公司技术实力雄厚，在全球封测行业排名前列。随着AI算力需求爆发，先进封装和HBM封测需求快速增长，公司将充分受益。封测行业景气度正在回升，三季度业绩环比改善明显。当前PE 38.4倍，估值处于合理区间，安全边际较高。",
        "capital_analysis": "资金面来看，今日成交额27.39亿，换手率3.21%，量能温和放大，显示资金关注度逐步提升。主力资金净流入约3.5亿，机构资金有小幅回补迹象。北向资金持股比例约5%，近期持续增持，显示外资对公司长期价值的认可。整体来看，资金面逐步转暖，底部构筑中。",
        "advice": "操作建议：持有为主。46元以下可加仓，52元以上减仓1/3，跌破44元止损。作为先进封装龙头，长期成长空间大，当前估值合理，建议中长线持有。",
        "support": "46.00元（强支撑位）",
        "resistance": "52.00元（第一压力位）",
        "action": "持有",
        "action_color": "green"
    },
    {
        "name": "风华高科",
        "code": "000636",
        "price": "26.88元",
        "change": "+1.40%",
        "up": True,
        "today_data": "今日收26.88元，涨幅1.40%，成交额16.69亿，换手率5.39%，开盘27.02元，最高27.62元，最低26.37元",
        "technical_analysis": "技术面来看，风华高科今日探底26.37元后震荡回升，收带下影小阳线。26元附近支撑较强，5日均线26.5元已收复。MLCC板块今日整体反弹，元件板块涨幅居首，风华高科作为板块龙头受益明显。MACD即将形成金叉，KDJ从中位上行，RSI回升至50附近。短期反弹趋势良好，30元为第一压力位，若能突破则有望挑战前高。",
        "fundamental_analysis": "基本面方面，风华高科是国内MLCC国产龙头企业，Q3单季净利润同比增长470%，业绩爆发验证行业高景气度。AI服务器MLCC用量是PC的5-10倍，随着AI算力需求爆发，MLCC行业有望迎来历史最长缺货周期。三星电机、太阳诱电等国际巨头8-9月已大幅提价，国内厂商有望跟进。高端MLCC国产替代在美国'精准脱钩'背景下进一步加速。当前PE 44.3倍，估值相对合理。",
        "capital_analysis": "资金面来看，今日成交额16.69亿，换手率5.39%，量能维持较高水平，显示资金关注度高。主力资金净流入约2.8亿，机构资金有明显加仓迹象。北向资金持股比例约3%，近期持续增持。整体来看，资金面明显转强，反弹动力充足。",
        "advice": "操作建议：坚定持有。26元以下可加仓，30元以上减仓1/3，35元以上再减1/3，跌破24元止损。作为MLCC国产龙头，业绩爆发+行业景气共振，建议中长线重点配置。",
        "support": "26.00元（支撑位）",
        "resistance": "30.00元（第一压力位）",
        "action": "持有",
        "action_color": "green"
    },
]

# 构建详细的持仓诊断HTML
holdings_html = '<div style="display: flex; flex-direction: column; gap: 20px;">'
for h in holdings_detailed:
    color = "#10b981" if h['up'] else "#ef4444"
    action_colors = {"green": "#10b981", "red": "#ef4444", "yellow": "#f59e0b"}
    acolor = action_colors.get(h['action_color'], "#f59e0b")
    
    holdings_html += f'''
    <div style="background: rgba(30,30,50,0.6); border: 1px solid rgba(255,255,255,0.08);
               border-radius: 16px; padding: 20px 24px;
               box-shadow: 0 4px 16px rgba(0,0,0,0.3);">
        <div style="display: flex; align-items: flex-start; justify-content: space-between; margin-bottom: 14px;">
            <div>
                <div style="display: flex; align-items: center; margin-bottom: 6px;">
                    <span style="font-size: 17px; font-weight: 700; color: #f1f5f9;">{h["name"]}</span>
                    <span style="font-size: 13px; color: #94a3b8; margin-left: 10px;">{h["code"]}</span>
                    <span style="font-size: 12px; background: {acolor}22; color: {acolor}; padding: 2px 8px; border-radius: 6px; margin-left: 10px; font-weight: 600;">{h["action"]}</span>
                </div>
                <div style="font-size: 13px; color: #94a3b8;">{h["today_data"]}</div>
            </div>
            <div style="text-align: right;">
                <div style="font-size: 20px; font-weight: 700; color: {color};">{h["price"]}</div>
                <div style="font-size: 14px; font-weight: 600; color: {color};">{h["change"]}</div>
            </div>
        </div>
        
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-bottom: 14px;">
            <div style="background: rgba(59,130,246,0.08); border-radius: 10px; padding: 12px 14px; border: 1px solid rgba(59,130,246,0.2);">
                <div style="font-size: 12px; font-weight: 600; color: #60a5fa; margin-bottom: 6px;">📊 技术面</div>
                <div style="font-size: 12px; color: #cbd5e1; line-height: 1.7;">{h["technical_analysis"]}</div>
            </div>
            <div style="background: rgba(16,185,129,0.08); border-radius: 10px; padding: 12px 14px; border: 1px solid rgba(16,185,129,0.2);">
                <div style="font-size: 12px; font-weight: 600; color: #34d399; margin-bottom: 6px;">🏭 基本面</div>
                <div style="font-size: 12px; color: #cbd5e1; line-height: 1.7;">{h["fundamental_analysis"]}</div>
            </div>
        </div>
        
        <div style="background: rgba(168,85,247,0.08); border-radius: 10px; padding: 12px 14px; border: 1px solid rgba(168,85,247,0.2); margin-bottom: 14px;">
            <div style="font-size: 12px; font-weight: 600; color: #a855f7; margin-bottom: 6px;">💰 资金面</div>
            <div style="font-size: 12px; color: #cbd5e1; line-height: 1.7;">{h["capital_analysis"]}</div>
        </div>
        
        <div style="display: flex; gap: 12px; align-items: stretch;">
            <div style="flex: 1; background: rgba(245,158,11,0.1); border-radius: 10px; padding: 12px 14px; border: 1px solid rgba(245,158,11,0.25);">
                <div style="font-size: 12px; font-weight: 600; color: #f59e0b; margin-bottom: 6px;">🎯 操作建议</div>
                <div style="font-size: 12px; color: #fef3c7; line-height: 1.7; font-weight: 500;">{h["advice"]}</div>
            </div>
            <div style="width: 180px; background: rgba(255,255,255,0.03); border-radius: 10px; padding: 12px 14px; border: 1px solid rgba(255,255,255,0.08);">
                <div style="font-size: 11px; color: #10b981; margin-bottom: 4px;">支撑位</div>
                <div style="font-size: 13px; font-weight: 600; color: #f1f5f9; margin-bottom: 8px;">{h["support"]}</div>
                <div style="font-size: 11px; color: #ef4444; margin-bottom: 4px;">压力位</div>
                <div style="font-size: 13px; font-weight: 600; color: #f1f5f9;">{h["resistance"]}</div>
            </div>
        </div>
    </div>
    '''
holdings_html += '</div>'

gen.report.add_section(
    title="💼 持仓股深度诊断",
    content=holdings_html,
    icon="briefcase"
)

# ====== 龙虎榜深度解读 ======
lhb_stocks = [
    {
        "name": "拓维信息",
        "code": "002261",
        "change": "+10.03%",
        "close": "20.96元",
        "net_buy": "3.99亿",
        "institution": "机构净买入1.21亿",
        "hot_money": "游资净买入2.78亿",
        "analysis": "拓维信息今日强势涨停登上龙虎榜，净买入金额3.99亿位居今日榜首。买入席位方面，机构席位净买入1.21亿，显示机构资金对公司未来发展看好。游资合力拉升，中信证券上海溧阳路等知名游资现身买入榜。拓维信息涉及华为算力+AI应用+鸿蒙概念，多重题材共振，短期强势有望延续。技术面来看，股价突破前期平台整理，放量涨停确认突破有效。明日关注能否连板，若放量冲高回落则警惕板块分歧风险。支撑位19.5元，压力位23元。",
        "sustainability": "高",
        "reason": "机构+游资合力买入，多重题材共振"
    },
    {
        "name": "旋极信息",
        "code": "300324",
        "change": "+20.00%（20cm涨停）",
        "close": "5.04元",
        "net_buy": "3.34亿",
        "institution": "机构净买入6021万",
        "hot_money": "游资净买入2.74亿",
        "analysis": "旋极信息今日20cm涨停，龙虎榜净买入3.34亿位居第二。机构买入6021万，游资主导拉升行情。公司涉及AI+军工+信创多重概念，低价股弹性大，容易受到游资青睐。成交放大明显，资金关注度高。但需要注意的是，股价长期处于低位，基本面改善有待验证，业绩支撑不足。技术面来看，今日放量突破前期高点，短期上涨动能充足。明日关注5.5元压力位，若能突破则有望挑战6元。支撑位4.5元。",
        "sustainability": "中",
        "reason": "低价题材股，游资主导，持续性需看板块情绪"
    },
    {
        "name": "盛合晶微",
        "code": "688820",
        "change": "+18.94%",
        "close": "101.10元",
        "net_buy": "3.20亿",
        "institution": "机构净卖出2531万",
        "hot_money": "游资净买入3.45亿",
        "analysis": "盛合晶微今日大涨18.94%登上龙虎榜，净买入3.20亿位居第三。值得注意的是，机构席位净卖出2531万，而游资大举买入3.45亿，呈现机构出货、游资接盘的格局。公司是先进封装概念股，与长电科技、华天科技等同属半导体封测赛道。近期半导体板块超跌反弹，先进封装作为高弹性方向受到资金关注。短期游资推动上涨，但中期需警惕机构抛压。技术面来看，股价从低位强势反弹，短期上涨动能强劲。明日关注105元压力位，若回落至95元以下则反弹可能结束。支撑位90元。",
        "sustainability": "中低",
        "reason": "机构卖出游资接力，持续性存疑，建议谨慎追高"
    },
    {
        "name": "冰山冷热",
        "code": "000530",
        "change": "+10.00%",
        "close": "16.17元",
        "net_buy": "1.19亿",
        "institution": "机构净买入2.00亿",
        "hot_money": "游资净卖出8100万",
        "analysis": "冰山冷热今日涨停，龙虎榜显示机构净买入2.00亿，为当日机构买入金额最高的个股，而游资净卖出8100万。机构大举买入是非常积极的信号，说明有机构资金在低位建仓。公司涉及制冷设备+冰雪经济+机器人概念，冰雪经济受益于冬奥会后的产业发展，机器人业务布局前瞻。机构主导的行情通常持续性更好，中期上涨基础更扎实。技术面来看，股价突破前期整理平台，放量涨停确认突破。明日关注17元压力位，回调至15元附近可考虑低吸。支撑位14.5元。",
        "sustainability": "高",
        "reason": "机构主导大额买入，基本面有支撑，中期看好"
    },
]

gen.add_dragon_tiger_list(lhb_stocks)

# ====== 重点关注标的 ======
gen.add_tomorrow_prediction([
    {
        "name": "金禄电子",
        "code": "301282",
        "logic": "PCB+汽车电子龙头企业，今日元件板块领涨+19.39%。AI服务器PCB需求持续放量，公司高端PCB产品快速放量，业绩高速增长。底部放量突破前期平台，资金关注度大幅提升。技术面强势，短期上涨空间大。",
        "target": "38-40元（目标价）",
        "stop_loss": "30元（止损位）",
        "rating": "★★★★"
    },
    {
        "name": "中京电子",
        "code": "002579",
        "logic": "PCB+HDI核心标的，AI服务器+存储芯片封装基板双轮驱动。今日大涨7.91%，元件板块资金大幅流入。技术面突破长期平台整理，量能配合良好，主力资金建仓迹象明显。公司业绩持续增长，估值相对合理。",
        "target": "22-24元",
        "stop_loss": "17元",
        "rating": "★★★★"
    },
    {
        "name": "超声电子",
        "code": "000823",
        "logic": "覆铜板+PCB行业龙头，覆铜板概念板块今日涨幅+3.37%。AI算力需求推动高端PCB量价齐升，公司高端产品占比持续提升。估值处于历史低位，安全边际高。业绩稳健增长，分红率高，适合中长期配置。",
        "target": "15-16元",
        "stop_loss": "12元",
        "rating": "★★★"
    },
])

# ====== 明日操作策略 ======
plan_html = """
<div style="line-height: 2; font-size: 14px;">
    <h4 style="color: #f1f5f9; margin: 20px 0 12px 0; font-size: 15px;">📈 大盘判断与展望</h4>
    <p style="color: #cbd5e1; margin: 0;">今日市场探底回升V型反转，显示下方支撑较强。上证指数3450点附近构成短期底部区域，创业板指2150点支撑有效。市场情绪从冰点开始修复，涨停家数回升至62家，跌停家数降至12家，赚钱效应明显改善。北向资金净流入32.6亿结束连续净流出，外资回流释放积极信号。但整体来看，市场仍处于震荡磨底阶段，成交量1.32万亿较前期有所缩量，增量资金入场意愿不强。预计明日延续震荡反弹走势，沪指有望冲击3500点整数关口，创业板指有望挑战2250点。</p>
    
    <h4 style="color: #f1f5f9; margin: 20px 0 12px 0; font-size: 15px;">💼 仓位建议</h4>
    <p style="color: #cbd5e1; margin: 0;">建议仓位控制在5-6成，保持灵活机动。科技成长股为主要配置方向，占比4成左右，重点布局半导体、元件、先进封装、AI算力等超跌反弹赛道。消费/金融防御仓位降低至1成以内。保留4成现金等待更好的买点或应对市场波动。</p>
    
    <h4 style="color: #f1f5f9; margin: 20px 0 12px 0; font-size: 15px;">🎯 具体操作计划</h4>
    <ul style="padding-left: 20px; color: #cbd5e1; line-height: 2.2;">
        <li><strong>英维克(002837)</strong>：30元以下加仓1成仓位，33元以上减仓1/3，跌破28元严格止损，当前位置谨慎观望</li>
        <li><strong>铜冠铜箔(301217)</strong>：56元以下可加仓，62元以上减仓1/3，跌破54元止损，底部反弹初期持有为主</li>
        <li><strong>雅克科技(002409)</strong>：70元以下加仓，80元以上减仓1/3，90元以上再减1/3，跌破68元止损，半导体材料龙头坚定持有</li>
        <li><strong>华海诚科(688535)</strong>：62元以下加仓，70元以上减仓1/3，75元以上再减1/3，跌破58元止损，先进封装材料龙头看好</li>
        <li><strong>长电科技(600584)</strong>：46元以下加仓，52元以上减仓1/3，跌破44元止损，先进封装龙头底部布局</li>
        <li><strong>风华高科(000636)</strong>：26元以下加仓，30元以上减仓1/3，35元以上再减1/3，跌破24元止损，MLCC龙头业绩爆发</li>
        <li><strong>*ST建艺(002789)</strong>：7.5元以上减仓1/2，8元以上清仓离场，严格控制退市风险敞口</li>
        <li><strong>重点关注标的</strong>：金禄电子(301282)33元以下可轻仓介入，止损30元；中京电子(002579)19元以下关注，止损17元</li>
    </ul>
    
    <h4 style="color: #f1f5f9; margin: 20px 0 12px 0; font-size: 15px;">⚠️ 操作纪律</h4>
    <ul style="padding-left: 20px; color: #cbd5e1; line-height: 2.2;">
        <li>严格执行止损纪律，任何标的跌破止损位立即减仓，绝不补仓摊平</li>
        <li>不追高，回调买入，分批建仓，严禁满仓梭哈单一个股</li>
        <li>单只个股仓位不超过总仓位的20%，ST股总仓位不超过5%</li>
        <li>保持耐心，等待确定性机会，宁可错过不可做错</li>
        <li>每日复盘，总结交易得失，不断优化操作策略</li>
    </ul>
    
    <h4 style="color: #f1f5f9; margin: 20px 0 12px 0; font-size: 15px;">📅 明日关注</h4>
    <ul style="padding-left: 20px; color: #cbd5e1; line-height: 2.2;">
        <li>美股科技股表现：关注英伟达、AMD等AI龙头走势对A股科技板块的影响</li>
        <li>成交量变化：关注两市成交额能否放大至1.5万亿以上，确认反弹有效性</li>
        <li>板块持续性：观察元件/半导体/通信设备等领涨板块能否持续走强</li>
        <li>北向资金动向：关注北向资金能否持续净流入，确认外资回流趋势</li>
    </ul>
</div>
"""

gen.add_trading_plan(plan_html)

# ====== 风险提示 ======
risks = [
    "外部风险：美股科技股波动加剧，可能传导至A股科技板块，关注今晚美股表现，若纳指大跌可能影响明日开盘",
    "流动性风险：年末资金面偏紧，两市成交缩量至1.32万亿，增量资金不足制约反弹空间，需警惕无量反弹后的回落",
    "业绩风险：部分高位科技股估值仍偏高，三季报后业绩验证期需警惕不及预期风险，重点关注半导体设备/材料板块",
    "政策风险：半导体/AI行业政策变化可能引发板块波动，关注后续产业政策落地情况，美国出口管制政策变化",
    "退市风险：*ST建艺等ST股退市风险高悬，仓位必须严格控制在5%以内，建议逢高减仓，退市风险敞口必须关闭",
]
gen.add_risk_warning(risks)

# ====== 发布 ======
result = gen.publish(
    title="盘后速递",
    excerpt="三大指数探底回升V型反转，科技板块超跌反弹，7只持仓6涨1跌，*ST建艺涨停，华海诚科大涨7%。龙虎榜游资主导行情，拓维信息/旋极信息/盛合晶微净买入居前三。北向资金净流入32.6亿，市场情绪修复。"
)

print(f"✅ 报告生成完成: {result}")
