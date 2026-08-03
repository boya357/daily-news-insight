#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""盘后速递 2026-08-03 生成脚本"""
import sys, os
sys.path.insert(0, 'v3')
os.chdir('/root/daily-news-insight')

from v3.generators.aftermarket import AftermarketGenerator

gen = AftermarketGenerator(date_str="20260803", subtitle="2026.08.03 · 盘后速递")

# 1. 今日核心亮点
gen.add_today_highlight("""科创50暴跌5.08%创年内最大单日跌幅之一，半导体/存储/先进封装全线重挫，但全市场4005家上涨、83家涨停，资金从高位科技龙头急速切换至核电/电网/可控核聚变等低位主题，呈现极致"指数跌、个股嗨"分化格局。两市成交额1.997万亿缩量5446亿，兆易创新封死跌停、雅克科技机构深股通逆势净买入近5亿，龙虎榜显示游资作手新一3亿爆买富瀚微20cm涨停。""")

# 2. 市场收盘总结
gen.add_market_summary(
    indices=[
        {"name": "上证指数", "value": "3809.66", "change": "-0.59%", "icon": "trending_down", "up": False},
        {"name": "深证成指", "value": "13448.29", "change": "-0.96%", "icon": "trending_down", "up": False},
        {"name": "创业板指", "value": "3302.55", "change": "-1.24%", "icon": "trending_down", "up": False},
        {"name": "科创50", "value": "1552.89", "change": "-5.08%", "icon": "trending_down", "up": False},
    ],
    volume="1.997万亿元（缩量5446亿）",
    northbound="温和流出，南向净买入110亿港元"
)

# 3. 情绪温度计
gen.add_sentiment_thermometer(
    temperature=58,
    volume="1.997万亿",
    up_count="4005↑",
    down_count="1466↓",
    limit_up_count="83"
)

# 4. 盘面深度解读
gen.add_market_deep_analysis(
    strong_sectors=[
        {"name": "可控核聚变/核电", "reason": "国常会核准4个核电项目8台机组，总投资超1700亿，板块掀涨停潮，久盛电气/瑞迪智驱20cm涨停，十余只个股涨停，主力净流入超26亿，是今日最强主线。"},
        {"name": "电网设备/特高压", "reason": "电网投资预期升温，百利电气/长城电工/顺钠股份涨停，主力净流入约16.1亿居首，特高压概念涨2.65%，汇金通/长缆科技/华菱线缆涨停。"},
        {"name": "光伏设备", "reason": "通威股份涨停带动板块异动，国晟科技/福莱特涨停，大全能源/亚玛顿等跟涨，属低位赛道修复行情。"},
        {"name": "商业航天/SpaceX概念", "reason": "题材炒作升温，*ST航图20cm涨停，神剑股份涨停，天力复合涨超11%。"},
        {"name": "AI应用/传媒", "reason": "暑期档票房走高，传智教育6连板，传媒游戏震荡上行，AI教育/数字营销活跃。"},
    ],
    weak_sectors=[
        {"name": "半导体设备", "reason": "拓荆科技/长川科技跌超12%，中科飞测跌超10%，中微公司跌9.93%，科创50权重股集体重挫，公募高持仓+估值过高+韩国半导体暴跌多重利空。"},
        {"name": "存储芯片/HBM", "reason": "兆易创新跌停(-10%)、普冉股份跌超11%、德明利跌超9%，费城半导体指数7月暴跌21%、闪迪美光暴跌引发全球存储板块恐慌，去杠杆冲击传导。"},
        {"name": "先进封装", "reason": "通富微电跌9.50%、雅克科技跌9.63%，板块高位回调，主力单日大幅净流出，龙虎榜显示游资章盟主集中减持。"},
        {"name": "国家大基金持股", "reason": "板块跌4.49%，中芯国际概念跌3.81%，光刻机概念跌2.67%，科技成长整体承压。"},
        {"name": "贵金属/消费电子", "reason": "跟随大盘走弱，部分消费电子同步调整。"},
    ],
    core_view="""<p><strong>核心判断：</strong>今日市场呈现极致分化——指数层面受半导体权重股拖累大跌，但个股层面超72%上涨，本质是场内资金进行大规模"高低切换"：从高估值、高持仓、高涨幅的半导体/AI算力龙头，流向低估值、政策催化的核电/电网/可控核聚变等低位制造主题。</p>
<p><strong>三大信号值得关注：</strong>①科创50单日暴跌5.08%创年内最大跌幅之一，是趋势性破位还是情绪冰点需明日验证；②缩量5446亿至2万亿下方，说明高位抛压集中释放后追涨意愿下降，但未出现恐慌性踩踏；③中证1000逆势翻红与沪深300跌0.98%的剪刀差，确认风格切换正在深化。</p>
<p><strong>操作上</strong>，8月开局首日的风格巨变值得高度重视。半导体板块短期跌幅已深或有技术性反抽，但趋势性修复需要时间；核电/电网等新主线首日爆发，明日若能放量接力则持续性可期，否则需警惕一日游风险。</p>"""
)

# 5. 板块涨跌幅排行
gen.add_sector_performance(
    up_sectors=[
        {"name": "可控核聚变", "change": "+4.68%"},
        {"name": "中核工业集团", "change": "+4.93%"},
        {"name": "SpaceX概念", "change": "+4.80%"},
        {"name": "核电", "change": "+2.68%"},
        {"name": "电网设备", "change": "+2.68%"},
        {"name": "光热发电", "change": "+3.21%"},
        {"name": "柔性直流输电", "change": "+2.99%"},
        {"name": "风电设备", "change": "+3.73%"},
        {"name": "地下管网", "change": "+2.82%"},
        {"name": "共享单车", "change": "+3.97%"},
    ],
    down_sectors=[
        {"name": "国家大基金持股", "change": "-4.49%"},
        {"name": "中芯国际概念", "change": "-3.81%"},
        {"name": "存储芯片", "change": "-3.15%"},
        {"name": "光刻机", "change": "-2.67%"},
        {"name": "先进封装", "change": "-2.29%"},
    ]
)

# 6. 持仓股深度诊断
gen.add_holdings_tracking(holdings=[
    {
        "name": "英维克", "code": "002837",
        "price": "46.45", "change": "-2.11%", "up": False,
        "comment": """<strong>当日表现：</strong>收46.45元，跌2.11%，成交额17.86亿元，换手率3.37%，最高48.20元，最低45.82元。液冷板块跟随半导体整体调整，但跌幅明显收窄，较前期动辄10%暴跌已有显著改善，呈现低位震荡格局。<br>
<strong>技术面判断：</strong>日线级别连续下挫后在45-48元区间窄幅震荡，5日均线（约48元）构成短期压制，下方45元为近期低点支撑。MACD绿柱缩短，KDJ低位金叉迹象，短期或有技术性反抽需求。但中期下降通道完好，反弹压力重重。<br>
<strong>资金面：</strong>成交量较前期明显萎缩，说明抛压阶段性释放，但增量资金入场意愿不强。北向资金今日在科技板块整体流出背景下，对液冷龙头态度偏观望。<br>
<strong>操作建议：</strong><span style="color:#fbbf24">【持有观望】</span>底仓30%继续持有，不急于加仓。反弹至<strong>49元以上</strong>可减仓1/3锁定部分筹码；若跌破<strong>45元</strong>支撑位需进一步减仓至20%；真正安全的加仓点在<strong>42-44元</strong>区间（若能到达），届时可分批回补做T。止损位下移至<strong>43元</strong>，跌破则无条件离场。"""
    },
    {
        "name": "铜冠铜箔", "code": "301217",
        "price": "77.66", "change": "-6.00%", "up": False,
        "comment": """<strong>当日表现：</strong>收77.66元，跌6.00%，成交额21.52亿元，换手率3.27%，最高82.97元，最低77.37元。受覆铜板/PCB板块拖累，叠加半导体整体杀跌，铜箔龙头跟随重挫，创近期调整新低。<br>
<strong>技术面判断：</strong>跌破80元整数关口后加速下行，77元附近有前期平台支撑（7月中旬低点区域）。5日/10日/20日均线呈空头排列压制股价。MACD继续向下发散，RSI进入超卖区（约28），短期有技术性反抽需求。<br>
<strong>资金面：</strong>主力资金净流出约2.3亿元，机构与游资同步减仓。但成交量未异常放大，说明不是恐慌性出逃，更多是被动跟随板块调整。<br>
<strong>操作建议：</strong><span style="color:#fbbf24">【谨慎持有+小仓位做T】</span>77-78元为关键支撑区，若明日缩量企稳可在<strong>76-77元</strong>小仓位（10%以内）加仓做T；反弹至<strong>82元以上</strong>减仓做T部分；若有效跌破<strong>75元</strong>（连续两日收于下方），则需减仓至底仓20%防御；中期目标价上修至<strong>90-95元</strong>（需要存储产业链回暖催化）。"""
    },
    {
        "name": "雅克科技", "code": "002409",
        "price": "120.91", "change": "-9.63%", "up": False,
        "comment": """<strong>当日表现：</strong>收120.91元，跌9.63%，成交额47.64亿元，换手率12.07%，振幅9.33%。因日跌幅偏离值达-9.31%登上龙虎榜。先进封装/HBM材料板块集体重挫，雅克作为龙头之一放量大跌。<br>
<strong>龙虎榜亮点：</strong>机构净买入2.73亿元（5家机构现身，买入5.84亿/卖出3.11亿），深股通净买入2.17亿元（买一卖一），合计外资+机构逆势净买入近5亿元！这说明机构资金在暴跌中抄底，筹码从游资向机构集中。<br>
<strong>技术面判断：</strong>120元整数关口岌岌可危，下一档支撑在110-115元（60日均线附近）。短期超跌严重，RSI低于25，随时可能触发技术性反弹。但中期趋势转弱已确认。<br>
<strong>操作建议：</strong><span style="color:#10b981">【机构逆势买入=逢低加仓信号】</span>龙虎榜机构+深股通逆势净买近5亿是重要信号，说明机构认可当前估值。操作上：<strong>118-122元</strong>区间可加仓至40%仓位；若跌至<strong>110-115元</strong>加仓至60%（黄金击球区）；反弹目标<strong>135-140元</strong>分批减仓；止损位严格设在<strong>105元</strong>（跌破则机构抄底失败逻辑破）。注意：今日上榜后5日平均涨2.74%，历史规律偏正面。"""
    },
    {
        "name": "*ST建艺", "code": "002789",
        "price": "10.04", "change": "+4.91%", "up": True,
        "comment": """<strong>当日表现：</strong>收10.04元，涨4.91%，成交额2829.92万元，换手率1.85%。今日表现意外强势，是持仓中唯一上涨个股。建筑装饰板块整体偏弱，但*ST建艺逆势走强，疑似有资金在低位博弈。<br>
<strong>技术面判断：</strong>价格重返10元整数关，短期5日均线拐头向上。但ST股技术分析参考意义有限，更多受消息面和资金博弈驱动。上方压力在10.5-11元区间，下方支撑在9元。<br>
<strong>资金面：</strong>主力资金净流出73.79万元，游资净流入192.81万元，散户净流出119.02万元。游资在悄悄加仓，但绝对金额很小，说明还是小资金博弈。<br>
<strong>操作建议：</strong><span style="color:#ef4444">【逢高减仓，退市风险不可忽视】</span>借今日反弹之机减仓是明智选择。<strong>10元以上</strong>分批减仓，每涨0.5元减1/3；若反弹至<strong>11元</strong>附近则全部清仓；跌破<strong>9元</strong>也必须止损离场；核心逻辑：一季度亏损5311万、负债率94.38%、毛利率仅2.55%，退市风险真实存在，不可恋战。本次反弹是减仓良机，不是加仓理由。"""
    },
])

# 7. 龙虎榜深度解读
gen.add_dragon_tiger_list(stocks=[
    {
        "name": "兆易创新", "code": "603986",
        "change": "-10.00%", "up": False,
        "institutions": 1,
        "reason": "日收盘价格跌幅偏离值达到7%",
        "net_buy": "+5.85亿元（营业部）",
        "analysis": """<strong>席位分析：</strong>今日封死跌停报340.74元，成交额近200亿。营业部净买入5.85亿元，占成交额2.54%，显示有游资在跌停板翘板抄底。但需注意，跌停板上的净买入更多是博弈超跌反弹，不代表趋势反转。<br>
<strong>持续性判断：</strong>存储芯片板块短期跌幅过深（兆易从高点回撤超40%），跌停板有资金翘板说明短期情绪接近冰点。明日若能低开高走放量收阳，则确认短期底部；若继续跌停则恐慌尚未释放完毕。<strong>建议观望，不急于抄底。</strong>"""
    },
    {
        "name": "雅克科技", "code": "002409",
        "change": "-9.63%", "up": False,
        "institutions": 5,
        "reason": "日跌幅偏离值达-9.31%",
        "net_buy": "+4.90亿元（机构+深股通）",
        "analysis": """<strong>席位分析：</strong>龙虎榜最大亮点！5家机构专用席位现身，合计净买入2.73亿元；深股通净买入2.17亿元（既是买一也是卖一，净买入显著）。机构+外资在暴跌日逆势净买入近5亿，<strong>是机构抄底的明确信号</strong>。<br>
<strong>持续性判断：</strong>历史数据显示该股上榜后5日平均涨2.74%，偏正面。机构抄底说明长期价值被认可，但短期是否立即反转还需看板块情绪。<strong>建议：118-122元区间分批布局，中长期持有逻辑不变。</strong>"""
    },
    {
        "name": "富瀚微", "code": "300613",
        "change": "+20.01%", "up": True,
        "institutions": 0,
        "reason": "日涨幅偏离值达7%",
        "net_buy": "+3.93亿元（营业部）",
        "analysis": """<strong>席位分析：</strong>作手新一（国泰君安南京太平南路）逆势爆买3.06亿元，直接带动个股20cm涨停。营业部净买入3.93亿元，占成交额52%，游资主导特征明显。富瀚微兼具AI芯片与车载ISP概念，属半导体板块内逆势突围的标的。<br>
<strong>持续性判断：</strong>作手新一的操作风格偏短线，连续涨停概率较低但可能维持强势震荡。明日冲高后需警惕游资兑现。<strong>建议：不追高，若回调至60元附近可关注低吸机会，止损位55元。</strong>"""
    },
    {
        "name": "百利电气", "code": "600468",
        "change": "+10.09%", "up": True,
        "institutions": 0,
        "reason": "日收盘价格涨幅偏离值达到7%",
        "net_buy": "+0.55亿元（西安太华路）",
        "analysis": """<strong>席位分析：</strong>开源证券西安太华路（上海超短帮）净买入5061万元，是主要买盘力量。沪股通净卖出80万元，北向态度偏中性。百利电气是可控核聚变+电网设备双概念龙头，流通市值67亿，适合游资炒作。<br>
<strong>持续性判断：</strong>核电/核聚变是今日最强主线，百利电气作为板块龙头有望享受溢价。西安太华路席位以短线快进快出著称，明日若继续放量涨停可看高一线，若缩量则需注意兑现风险。<strong>目标价7-7.5元，止损位5.8元。</strong>"""
    },
])

# 8. 重点关注标的
from v3.components.layout import Section

watchlist_html = """<div style="display: flex; flex-direction: column; gap: 14px;">
<div style="background: rgba(30,30,50,0.5); border: 1px solid rgba(255,255,255,0.08); border-radius: 14px; padding: 18px;">
<div style="display: flex; align-items: center; margin-bottom: 10px;">
<span style="font-size: 16px; font-weight: 700; color: #f1f5f9;">🎯 久盛电气（301082）</span>
<span style="margin-left: 10px; font-size: 12px; padding: 2px 8px; border-radius: 8px; background: rgba(16,185,129,0.2); color: #10b981;">核电+20cm龙头</span>
</div>
<div style="font-size: 13px; color: #94a3b8; line-height: 1.7;">
<strong>买入逻辑：</strong>核电板块日内最强主线龙头，20cm涨停，国常会核准8台核电机组总投资1700亿催化，板块持续性可期。久盛电气主营核电用电缆，直接受益于核电建设提速。<br>
<strong>目标价：</strong>第一目标<strong>13-14元</strong>（+25-30%），第二目标16元<br>
<strong>止损位：</strong><strong>9.0元</strong>（跌破涨停开盘价止损）<br>
<strong>评级：</strong>⭐⭐⭐⭐（A级机会，首日爆发+政策催化+题材新颖）
</div></div>

<div style="background: rgba(30,30,50,0.5); border: 1px solid rgba(255,255,255,0.08); border-radius: 14px; padding: 18px;">
<div style="display: flex; align-items: center; margin-bottom: 10px;">
<span style="font-size: 16px; font-weight: 700; color: #f1f5f9;">🎯 中国核建（601611）</span>
<span style="margin-left: 10px; font-size: 12px; padding: 2px 8px; border-radius: 8px; background: rgba(59,130,246,0.2); color: #60a5fa;">核电工程龙头</span>
</div>
<div style="font-size: 13px; color: #94a3b8; line-height: 1.7;">
<strong>买入逻辑：</strong>核电工程建设绝对龙头，国内核岛建设市场占有率超90%。8台新机组核准直接利好公司订单，中长期受益于"十五五"核电常态化核准。市值适中、机构持仓稳定，适合中线布局。<br>
<strong>目标价：</strong><strong>12-13元</strong>（+20-30%）<br>
<strong>止损位：</strong><strong>8.5元</strong>（跌破20日线止损）<br>
<strong>评级：</strong>⭐⭐⭐⭐（A级机会，政策驱动+业绩确定性+低估值）
</div></div>

<div style="background: rgba(30,30,50,0.5); border: 1px solid rgba(255,255,255,0.08); border-radius: 14px; padding: 18px;">
<div style="display: flex; align-items: center; margin-bottom: 10px;">
<span style="font-size: 16px; font-weight: 700; color: #f1f5f9;">⚠️ 德明利（001309）</span>
<span style="margin-left: 10px; font-size: 12px; padding: 2px 8px; border-radius: 8px; background: rgba(239,68,68,0.2); color: #ef4444;">风险警示</span>
</div>
<div style="font-size: 13px; color: #94a3b8; line-height: 1.7;">
<strong>风险逻辑：</strong>存储芯片板块今日重灾区，跌9.56%报349元，换手率16.49%。龙虎榜显示机构净买入1.82亿元但股价仍大跌，多空分歧巨大。存储板块趋势性走弱背景下，个股难以独善其身。<br>
<strong>操作建议：</strong><strong>回避为主</strong>。若已持有，反弹至<strong>370元以上</strong>减仓；跌破<strong>330元</strong>止损。存储芯片板块调整尚未结束，左侧抄底风险极大。<br>
<strong>评级：</strong>⭐⭐（C级，趋势向下+板块拖累+估值偏高）
</div></div>
</div>"""
watch_section = Section(title="🔍 重点关注标的", content=watchlist_html, icon="search")
gen._components.append(watch_section)

# 9. 明日关键预判
gen.add_tomorrow_prediction(predictions=[
    {"name": "大盘走势", "direction": "震荡", "confidence": 65,
     "reason": "科创50单日暴跌5%后短期有技术性反抽需求，但缩量背景下难有大级别反弹。预计沪指在3780-3850区间震荡，创业板在3280-3350区间震荡，关注3800点整数关支撑。"},
    {"name": "核电/电网板块", "direction": "看涨", "confidence": 70,
     "reason": "今日首日爆发，政策催化明确（8台机组+1700亿投资），板块涨停数量多、资金流入大，持续性可期。明日若能放量上攻则确认主线地位，预计龙头继续涨停，板块内部分化。"},
    {"name": "半导体/存储芯片", "direction": "震荡", "confidence": 60,
     "reason": "单日暴跌后短期超卖严重，大概率有技术性反抽，但趋势性反转需要时间和量能配合。雅克科技机构逆势买入是积极信号，可作为板块风向标观察。重点关注兆易创新能否止跌企稳。"},
    {"name": "风格切换", "direction": "看涨（低位制造）", "confidence": 75,
     "reason": "中证1000逆势翻红+核电电网爆发，确认资金从高位科技向低位制造/公用事业切换。这种风格切换通常持续1-2周，建议顺应趋势，降低科技仓位、增加低位主题配置。"},
])

# 10. 明日操作计划
gen.add_trading_plan(plan="""
<h4 style="color:#fbbf24; margin-bottom: 12px;">📌 总体策略：降低科技仓位，分批布局新主线</h4>
<p><strong>仓位建议：</strong>总仓位从当前5成降至4成，其中科技2成+新主线1.5成+现金0.5成。8月开局风格剧变，不宜硬扛原有持仓，需主动调仓适应新节奏。</p>

<h4 style="color:#fbbf24; margin: 16px 0 12px 0;">📊 持仓操作计划（按优先级）</h4>
<p><strong>1. 雅克科技（002409）—— 加仓，目标40%仓位</strong><br>
龙虎榜机构+深股通逆势净买近5亿是重磅利好信号，机构抄底说明长期价值认可。操作：<strong>118-122元</strong>区间加仓20%（从20%加到40%）；若跌至<strong>110-115元</strong>再加仓20%到60%；反弹至<strong>135-140元</strong>减仓至30%底仓；止损位<strong>105元</strong>（跌破则机构抄底失败，无条件离场）。</p>

<p><strong>2. 英维克（002837）—— 持有观望，反弹减仓</strong><br>
跌幅收窄但趋势未改，底仓30%持有。操作：反弹至<strong>49元以上</strong>减仓1/3（降至20%）；跌破<strong>45元</strong>再减1/3（降至10%）；<strong>43元</strong>为最终止损位，跌破清仓。不建议在当前位置加仓，等待趋势明确反转后再考虑。</p>

<p><strong>3. 铜冠铜箔（301217）—— 谨慎持有，小仓位做T</strong><br>
77元附近有支撑，但板块弱势未改。操作：<strong>76-77元</strong>可加10%仓位做T；反弹至<strong>82元以上</strong>卖出做T部分；跌破<strong>75元</strong>减仓至20%底仓；中期目标<strong>90-95元</strong>（需存储板块回暖配合）。</p>

<p><strong>4. *ST建艺（002789）—— 逢高减仓清仓</strong><br>
今日反弹是减仓良机，退市风险不可忽视。操作：<strong>10元以上</strong>开始分批减仓，每涨0.5元减1/3；<strong>11元</strong>附近全部清仓；跌破<strong>9元</strong>也必须止损；核心原则：ST股不可恋战，有反弹就减，留得青山在不怕没柴烧。</p>

<h4 style="color:#fbbf24; margin: 16px 0 12px 0;">🎯 新开仓计划</h4>
<p><strong>核电主线（10%仓位）：</strong>首选中国核建（601611），<strong>9.5-10元</strong>区间建仓5%，若回调至9元再加5%。中线目标12-13元，止损8.5元。</p>
<p><strong>弹性品种（5%仓位）：</strong>久盛电气（301082），若明日高开不超过5%可轻仓追涨，目标13-14元，止损9元。注意：20cm品种波动大，严格控制仓位。</p>

<h4 style="color:#fbbf24; margin: 16px 0 12px 0;">⚠️ 重点观察信号</h4>
<p>1. 明日两市成交额能否回到2.2万亿以上——放量则调整结束概率大，继续缩量则调整延伸<br>
2. 科创50能否止跌企稳，中微公司/兆易创新是风向标<br>
3. 核电板块龙头是否连板——百利电气/久盛电气/中国核建连板则持续性确认<br>
4. 北向资金流向——若连续2日加仓AI硬件，则内资只是短期调仓</p>
""")

# 11. 风险提示
gen.add_risk_warning(risks=[
    "半导体板块趋势性破位风险：科创50暴跌5.08%创年内最大跌幅，若明日继续下跌将确认中期调整，持仓科技股需严控仓位",
    "北向资金加速流出风险：外资若从观望转为集中减仓，将加剧A股科技板块调整压力",
    "核电/新主线一日游风险：今日首日爆发后，若明日无法放量接力则可能冲高回落，追高需谨慎",
    "中报业绩雷风险：8月进入中报密集披露期，高估值科技股若业绩不及预期可能面临戴维斯双杀",
    "全球科技股共振下跌风险：费城半导体7月暴跌21%、韩国综指暴跌5%、美光闪迪暴跌，海外风险传导需警惕",
])

# 12. 晚间重要新闻
gen.add_evening_news(news_list=[
    {
        "title": "国常会核准4个核电项目 8台机组总投资超1700亿",
        "content": "国务院常务会议决定核准浙江金七门核电二期、广东太平岭核电三期、辽宁庄河核电一期、山东莱阳核电一期，共计8台核电机组，总投资超1700亿元，为\"十五五\"首批核准项目。",
        "time": "2026-07-31",
        "source": "新华社",
        "tag": "政策利好",
        "tag_variant": "success"
    },
    {
        "title": "南向资金净买入超110亿港元 结束连续7日流出",
        "content": "南向资金今日净买入110.31亿港元，结束此前连续7个交易日的流出趋势。盈富基金、阿里巴巴-W分别获净买入约47.50亿港元、41.69亿港元；中芯国际遭净卖出10.64亿港元。",
        "time": "17:39",
        "source": "财联社",
        "tag": "资金动向",
        "tag_variant": "info"
    },
    {
        "title": "中微公司：截至6月底累计已有超8800个反应台在国内外生产线实现量产",
        "content": "中微公司披露，截至2026年6月底，公司累计已有超8800个反应台在国内外生产线实现量产，其中CCP反应台超过5900台，ICP反应台超过2900台。公司今日股价大跌9.93%。",
        "time": "18:48",
        "source": "东方财富网",
        "tag": "公司动态",
        "tag_variant": "default"
    },
    {
        "title": "山东高速：拟1亿元—2亿元回购股份 用于注销减少注册资本",
        "content": "山东高速公告，拟以1亿元-2亿元回购股份，回购价格不超过10元/股，回购股份将全部予以注销减少注册资本。",
        "time": "18:45",
        "source": "东方财富网",
        "tag": "公司公告",
        "tag_variant": "success"
    },
])

# 13. 业绩预增追踪
gen.add_earnings_forecast()

# 生成并发布
result = gen.publish()
print("发布结果:", result)
