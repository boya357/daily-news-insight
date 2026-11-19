#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""盘后速递 2026-11-18 V3.0"""
import sys, os
sys.path.insert(0, 'v3')
os.chdir('/root/daily-news-insight')

from v3.generators.aftermarket import AftermarketGenerator
from components.layout import Section

DATE = "20261118"
SUBTITLE = "2026.11.18 · 盘后速递"

gen = AftermarketGenerator(date_str=DATE, subtitle=SUBTITLE)

# 1. 今日核心亮点
gen.add_today_highlight(
    "💥 今日A股三大指数集体收红，市场情绪较昨日明显回暖：上证指数收涨0.09%报3587.83点，"
    "深证成指涨0.20%报10659.41点，创业板指涨0.85%报2311.62点，终结了创业板指连续5日下跌的颓势。"
    "盘面上，元件板块暴涨4.90%领涨全市场，博通概念+7.30%、覆铜板+4.02%、超节点+3.66%、算力租赁+3.20%、靶材+3.14%全线爆发，"
    "生益电子科创板大涨18.53%、沪电股份涨停（10%）、华工科技涨8.93%、工业富联涨5.68%、生益科技涨3.91%。"
    "核心催化：博通AI芯片对PCB/HDI需求超预期，叠加AI服务器PCB国产替代加速，PCB/覆铜板/元件板块今日成为市场最强主线。"
    "半导体板块整体涨1.59%，主力资金净流入45.13亿元，元件板块净流入46.18亿元居首。"
    "跌幅方面，稀土/黄金/煤炭等资源股领跌，中国稀土跌停、紫金矿业跌5.66%。"
    "两市合计成交约1.37万亿，较昨日略有缩量；涨停股约45只，跌停约20只，市场结构性行情特征明显。"
)

# 2. 市场收盘总结
gen.add_market_summary(
    indices=[
        {"name": "上证指数", "value": "3587.83", "change": "+0.09%", "up": True, "icon": "trending_up"},
        {"name": "深证成指", "value": "10659.41", "change": "+0.20%", "up": True, "icon": "trending_up"},
        {"name": "创业板指", "value": "2311.62", "change": "+0.85%", "up": True, "icon": "trending_up"},
        {"name": "科创50", "value": "886.34", "change": "+0.45%", "up": True, "icon": "trending_up"},
    ],
    volume="约1.37万亿（缩量约900亿）",
    northbound="龙虎榜个股口径：深股通净卖出约1.10亿（沪电股份），整体北向待盘后披露"
)

# 3. 情绪温度计
gen.add_sentiment_thermometer(temperature=52, volume="1.37万亿", up_count=2876, down_count=2458, limit_up_count=45)

# 4. 板块排行
gen.add_sector_performance(
    up_sectors=[
        {"name": "元件（PCB/覆铜板）", "change": "+4.90%", "up": True, "leader": "生益电子+18.53%/沪电股份+10%"},
        {"name": "博通概念", "change": "+7.30%", "up": True, "leader": "生益电子/沪电股份领涨"},
        {"name": "通信服务", "change": "+3.01%", "up": True, "leader": "平治信息+13.95%"},
        {"name": "黑色家电", "change": "+2.84%", "up": True, "leader": "四川长虹+10.08%"},
        {"name": "靶材", "change": "+3.14%", "up": True, "leader": "阿石创+6.64%/有研新材+5.82%"},
        {"name": "算力租赁", "change": "+3.20%", "up": True, "leader": "旋极信息+20%/青云科技+20%"},
    ],
    down_sectors=[
        {"name": "稀土永磁", "change": "-3.50%", "up": False, "leader": "中国稀土跌停"},
        {"name": "黄金/贵金属", "change": "-2.80%", "up": False, "leader": "紫金矿业-5.66%"},
        {"name": "煤炭开采", "change": "-2.10%", "up": False, "leader": "新大洲A/郑州煤电下跌"},
        {"name": "油气开采", "change": "-1.80%", "up": False, "leader": "中国石油/中国海油回调"},
        {"name": "银行", "change": "-0.30%", "up": False, "leader": "权重股无弹性"},
    ]
)

# 5. 盘面深度解读
strong_sectors = [
    {"name": "PCB/覆铜板/元件（今日最强主线）",
     "reason": "元件板块暴涨4.90%，博通概念+7.30%，覆铜板+4.02%，生益电子科创板大涨18.53%、沪电股份10cm涨停、华工科技+8.93%、工业富联+5.68%、生益科技+3.91%。核心催化：博通AI芯片对高端PCB/HDI需求超预期，AI服务器PCB量价齐升逻辑强化；AI算力建设加速，高端PCB供需紧张，加工费有望进入涨价周期；国内PCB龙头在全球AI服务器供应链中的份额持续提升。板块主力资金净流入46.18亿元，是今日资金最集中方向，上涨家数54/61，板块效应极强。"},
    {"name": "半导体/先进封装",
     "reason": "半导体板块整体涨1.59%，主力资金净流入45.13亿元。昨日爆发的光刻胶/光刻机今日分化（雅克科技冲高回落-1.25%），但资金向PCB/先进封装等业绩更确定方向扩散。长电科技+1.89%、华海诚科+2.42%、中芯国际+1.45%、寒武纪+4.89%。核心逻辑延续：半导体国产替代+AI算力硬件需求双重驱动，但板块内部轮动明显，从昨日的光刻胶/光刻机切换到今日的PCB/覆铜板。"},
    {"name": "算力/AI基础设施",
     "reason": "算力租赁+3.20%，超节点+3.66%，OpenClaw概念+3.38%，旋极信息、青云科技20cm涨停。算力板块经过前一段时间调整后，随着AI应用用户规模快速增长，算力需求持续上行，板块有企稳反弹迹象。但整体仍处于震荡筑底阶段，尚未形成趋势性行情。"},
    {"name": "黑色家电/家电",
     "reason": "黑色家电+2.84%，四川长虹涨停（+10.08%），小熊电器+4.06%，海立股份+4.58%。以旧换新政策持续兑现，家电板块作为防御性消费品种在震荡市中获得资金青睐。"},
]
weak_sectors = [
    {"name": "稀土/黄金/煤炭等资源股（集中杀跌）",
     "reason": "中国稀土跌停（-10%）、紫金矿业跌5.66%、稀土永磁板块跌3.50%、黄金板块跌2.80%、煤炭跌2.10%。资源股集体下挫的核心原因：美元指数反弹，大宗商品承压；市场风险偏好回升，资金从避险的黄金/稀土流向成长板块（半导体/PCB）；稀土价格前期涨幅较大，获利盘兑现。这是典型的风格切换——从防御性资源股流向科技成长股。"},
    {"name": "银行/权重股（无弹性）",
     "reason": "银行板块微跌0.3%，工商银行平收，权重股整体表现平淡。在科技成长股活跃的市场环境下，权重股缺乏资金关注，指数涨幅有限但个股机会丰富。"},
    {"name": "ST/问题股（分化）",
     "reason": "*ST建艺大跌5.82%，ST板块整体分化。在市场风险偏好回升、主线明确的环境下，资金倾向于流向有基本面支撑的成长股，ST股等投机品种被抛弃。"},
]
core_view = ("今日市场呈现典型的「科技成长回归」特征：PCB/覆铜板/元件板块在博通AI芯片催化下全线爆发，"
             "成为继昨日光刻胶之后半导体大板块内又一个强势分支，半导体整体净流入45亿元说明资金在持续加仓科技方向。"
             "与此同时，稀土、黄金、煤炭等资源股集体杀跌，资金从防御性品种向科技成长股切换的趋势非常明确。"
             "需要注意的是，半导体板块内部轮动很快（昨日光刻胶→今日PCB），追高风险较大，操作上应沿主线低吸而非追涨。"
             "持仓中铜冠铜箔（PCB上游铜箔）、长电科技（先进封装）、华海诚科（封装材料）今日表现较好，"
             "雅克科技（光刻胶）冲高回落属于正常轮动调整，英维克（液冷）反弹+3.93%属超跌修复。"
             "明日重点观察PCB板块持续性（若生益电子/沪电股份继续强势则主线确立）以及半导体板块能否形成普涨格局。")
gen.add_market_deep_analysis(strong_sectors=strong_sectors, weak_sectors=weak_sectors, core_view=core_view)

# 6. 持仓诊断（7只）
holdings = [
    {"name": "英维克 002837", "code": "002837", "price": "35.43", "change": "+3.93%", "up": True,
     "comment": "<b>【今日表现】</b>开盘34.65元，最低34.26元，最高36.20元，收盘35.43元，涨幅+3.93%，成交额13.31亿元，换手率3.33%，量能温和放大，走出一根探底回升的中阳线。"
     "<br><b>【资金面】</b>液冷板块今日跟随算力板块反弹，主力资金小幅净流入，成交较昨日（10.9亿）有所放大，说明有资金在低位承接。"
     "<br><b>【技术面】</b>今日收35.43元，成功收复5日线（34.5元附近），但仍在10日线（36.8元）和20日线下方运行。MACD绿柱继续缩短，KDJ从超卖区向上拐头，短期有技术性反弹需求。上方第一压力位36.2元（今日高点），第二压力位38元（20日线）；支撑位34元（5日线+今日开盘价）。"
     "<br><b>【核心催化】</b>AI算力需求持续增长，液冷渗透率提升的长期逻辑未变；板块经过近两个月深度调整（从68元跌到34元腰斩），估值风险大幅释放；算力租赁板块今日反弹+3.20%，算力基建链有企稳迹象。"
     "<br><b>【操作建议】</b>当前仓位较重者借反弹逐步减仓降低成本；反弹至36.2元（今日高点）减仓1/4，反弹至38元（20日线）再减1/4；若回落跌破34元（5日线）减仓1/3止损；33元以下不建议再割肉（已腰斩），但也不要抄底加仓；等待站上40元再考虑加仓。目标位40元，止损位32元（前低附近）。"},
    {"name": "铜冠铜箔 301217", "code": "301217", "price": "61.96", "change": "+2.97%", "up": True,
     "comment": "<b>【今日表现】</b>开盘60.69元，最低59.65元，最高63.33元，收盘61.96元，涨幅+2.97%，成交额9.46亿元，换手率1.86%，跟随PCB/覆铜板板块反弹，表现中规中矩。"
     "<br><b>【资金面】</b>PCB/覆铜板板块今日暴涨（元件+4.90%、覆铜板+4.02%），铜冠铜箔作为PCB上游原材料（电子铜箔）直接受益，但涨幅落后于板块龙头（生益电子+18.53%），说明资金更偏好PCB成品端而非上游材料端。"
     "<br><b>【技术面】</b>今日收盘61.96元，成功突破5日线和10日线（约60.5元），站上60元整数关口。MACD红柱扩大，KDJ金叉向上，短期反弹趋势确立。上方压力位63.33元（今日高点），第二压力位65元（前高）；支撑位60元（5日线）。"
     "<br><b>【核心催化】</b>AI服务器PCB需求爆发带动上游电子铜箔需求，高频高速铜箔加工费有望进入涨价周期；公司锂电铜箔+电子铜箔双轮驱动，电子铜箔占比约40%；PCB板块今日全面爆发，铜箔作为上游有补涨预期。"
     "<br><b>【操作建议】</b>仓位维持20%底仓；若明日放量突破63.33元可加仓10%，目标位68-70元；若回落至60元以下减仓1/3锁定利润；跌破58元（10日线+前期平台）减仓至10%底仓；55元以下可考虑加仓做反弹。止损位56元。"},
    {"name": "雅克科技 002409", "code": "002409", "price": "82.68", "change": "-1.25%", "up": False,
     "comment": "<b>【今日表现】</b>开盘84.00元，最高84.78元，最低80.72元，收盘82.68元，跌幅-1.25%，成交额15.04亿元，换手率5.71%，昨日大涨5.59%后今日冲高回落，属正常获利回吐。"
     "<br><b>【资金面】</b>半导体材料板块今日整体分化：光刻胶方向回调，PCB/覆铜板方向爆发。雅克作为半导体材料综合平台（前驱体+光刻胶+特气+LDS），今日受光刻胶板块回调影响冲高回落，但主力资金仍有净流入，未出现明显出货迹象。"
     "<br><b>【技术面】</b>今日收82.68元，仍在5日线（约80元）上方运行，5/10日均线金叉确认，MACD红柱扩大，短期趋势依然向上。但86-90元区间存在明显套牢盘压力（昨日高点86.5元附近），需要放量突破才能打开上行空间。支撑位80元（5日线+整数关口），第二支撑78元（10日线）；压力位86.5元（昨日高点）。"
     "<br><b>【核心催化】</b>上海微电子国产光刻机重大突破，半导体材料国产替代加速；公司前驱体+光刻胶+电子特气+LDS输送系统全产业链布局，深度绑定中芯国际、长存、长鑫；HBM前驱体材料进入SK海力士、三星供应链预期持续发酵；PCB板块爆发可能带动电子化学品整体估值修复。"
     "<br><b>【操作建议】</b>底仓30%继续持有，半导体材料国产替代中期逻辑不变；80元（5日线）以上持有不动，跌破80元减仓1/4；若明日放量突破86.5元可加仓15%，目标位95-100元；若回落至78元以下减仓至15%底仓观察；严格止损位75元（跌破说明短期趋势走坏）。"},
    {"name": "*ST建艺 002789", "code": "002789", "price": "6.80", "change": "-5.82%", "up": False,
     "comment": "<b>【今日表现】</b>开盘7.26元，最高7.27元，最低6.72元，收盘6.80元，跌幅-5.82%，成交额0.39亿元，换手率3.58%，今日大跌，明显弱于大盘。"
     "<br><b>【资金面】</b>ST板块今日整体偏弱，在市场风险偏好回升、科技主线明确的环境下，资金从ST等投机品种流向有基本面支撑的成长股。*ST建艺今日放量下跌，有资金出逃迹象。"
     "<br><b>【技术面】</b>今日大跌-5.82%，跌破7元整数关口，收6.80元，形态走坏。5日线（7.1元）拐头向下，MACD绿柱扩大，短期趋势转弱。支撑位6.5元（前期低点），压力位7.2元（今日开盘价）。"
     "<br><b>【核心问题】</b>公司基本面未有明显改善，摘帽预期仍不明朗；ST板块整体处于弱势，市场风格偏向科技成长股；公司主业装饰装修与地产链相关，房地产政策刺激有限。"
     "<br><b>【操作建议】</b>建议明日反弹至7元以上果断减仓至5%以内或清仓，腾出资金加仓半导体/PCB主线；跌破6.5元（前期低点）必须止损出局；ST股在当前市场环境下性价比极低，不建议继续持有。"},
    {"name": "华海诚科 688535", "code": "688535", "price": "72.27", "change": "+2.42%", "up": True,
     "comment": "<b>【今日表现】</b>开盘71.83元，最低69.23元，最高74.45元，收盘72.27元，涨幅+2.42%，成交额4.50亿元，换手率4.42%，振幅7.44%，跟随半导体/先进封装板块反弹。"
     "<br><b>【资金面】</b>半导体板块主力净流入45.13亿元，先进封装方向持续获得资金关注。华海诚科今日量能温和放大，机构资金仍在底部区域吸筹。"
     "<br><b>【技术面】</b>今日收72.27元，成功收复5日线和10日线，5日线金叉10日线确认，MACD红柱扩大，短期反弹趋势确立。上方压力位74.45元（今日高点），第二压力位78元（20日线）；支撑位70元（整数关口+5日线），第二支撑68元（10日线）。"
     "<br><b>【核心催化】</b>公司GMC塑封料已通过国内多家头部封测厂验证，先进封装材料国产替代加速；HBM封装材料正在送样SK海力士/长鑫存储，潜在弹性巨大；PCB/半导体板块全面爆发，公司作为封装材料标的估值有望修复；今日长电科技+1.89%验证封测链景气度。"
     "<br><b>【操作建议】</b>当前位置（72元附近）可加仓5-10%（从ST建艺等弱势标的腾仓位），目标位80-85元；若跌破70元减仓至10%底仓；反弹至78元附近减仓1/4锁定利润；80元以上再减1/4，保留底仓博弈HBM材料突破。止损位66元。"},
    {"name": "长电科技 600584", "code": "600584", "price": "52.96", "change": "+1.89%", "up": True,
     "comment": "<b>【今日表现】</b>开盘52.53元，最低51.70元，最高53.75元，收盘52.96元，涨幅+1.89%，成交额38.31亿元，换手率4.06%，先进封装板块龙头稳步上行。"
     "<br><b>【资金面】</b>半导体板块主力净流入45.13亿元，长电科技作为封测龙头获机构资金持续加仓，今日量价配合良好。"
     "<br><b>【技术面】</b>今日收52.96元，突破5日/10日线压制，5日线金叉10日线，MACD即将金叉，短期反弹趋势确立。上方压力位53.75元（今日高点），第二压力位55元（前高）；支撑位52元（5日线），第二支撑50元（20日线）。"
     "<br><b>【核心催化】</b>AI芯片带动先进封装（CoWoS/Chiplet/HBM）需求爆发，封测行业景气度持续上行；公司是国内封测龙头，XDFOI高密度多维异构集成平台已量产；中芯国际业绩高增验证晶圆厂扩产周期，封测环节直接受益；PCB板块爆发带动半导体设备材料链整体估值修复。"
     "<br><b>【操作建议】</b>底仓20%持有；放量突破55元（前高）可加仓10%，目标位60-62元；跌破50元（20日线）减仓1/3；50-53元区间可做T降低成本。止损位48元。"},
    {"name": "风华高科 000636", "code": "000636", "price": "28.12", "change": "+2.07%", "up": True,
     "comment": "<b>【今日表现】</b>开盘27.93元，最低27.31元，最高28.60元，收盘28.12元，涨幅+2.07%，成交额14.74亿元，换手率4.61%，元件板块今日大涨4.90%，风华高科作为MLCC龙头跟随上涨，但涨幅落后于板块。"
     "<br><b>【资金面】</b>元件板块主力净流入46.18亿元，但资金更偏好PCB方向（生益电子、沪电股份等），MLCC方向资金关注度相对较低，属被动跟涨。"
     "<br><b>【技术面】</b>今日收28.12元，站上5日线（27.5元），5日线有拐头向上迹象，MACD绿柱缩短，短期有企稳反弹迹象。上方压力位28.6元（今日高点），第二压力位30元（前高）；支撑位27元（20日线+前期平台）。"
     "<br><b>【核心催化】</b>MLCC国产替代加速，公司是国内MLCC龙头；Q3单季净利同比+470%，业绩拐点确立；AI服务器/汽车电子/消费电子三重需求拉动MLCC涨价周期；元件板块今日全面爆发，MLCC有补涨预期。"
     "<br><b>【操作建议】</b>底仓15%持有；若明日放量突破28.6元可加仓5%，目标位32-35元；跌破27元减仓1/3；反弹至30元以上减仓1/3锁定利润；26元以下可考虑加仓5%做反弹。止损位25元。"}
]
gen.add_holdings_tracking(holdings=holdings)

# 7. 龙虎榜卡片
dragon_stocks = [
    {"name": "沪电股份 002463", "code": "002463", "change": "+10.00%（涨停）", "up": True,
     "reason": "日涨幅偏离值达7%（PCB/AI服务器龙头）", "net_buy": "2.40亿元", "institutions": 5},
    {"name": "生益电子 688183", "code": "688183", "change": "+18.53%（科创板）", "up": True,
     "reason": "PCB/博通概念龙头", "net_buy": "1.56亿元", "institutions": 3},
    {"name": "华工科技 000988", "code": "000988", "change": "+8.93%", "up": True,
     "reason": "光模块/PCB/激光设备", "net_buy": "1.20亿元", "institutions": 2},
    {"name": "有研新材 600206", "code": "600206", "change": "+5.82%", "up": True,
     "reason": "半导体靶材/稀土（连板后分歧）", "net_buy": "0.85亿元", "institutions": 1},
    {"name": "中国稀土 000831", "code": "000831", "change": "-10.00%（跌停）", "up": False,
     "reason": "稀土板块集体杀跌", "net_buy": "-2.30亿元", "institutions": 0},
]
gen.add_dragon_tiger_list(stocks=dragon_stocks)

# 7b. 龙虎榜深度文字
lhb_deep_html = (
    '<div style="line-height:1.9; color:#cbd5e1; font-size:14px;">'
    '<p><b style="color:#f59e0b">▎沪电股份（002463）：5家机构集体买入，PCB中军龙头趋势确立</b><br>'
    '今日涨停收80.19元，成交额81.86亿元，换手率5.42%，龙虎榜净买入2.40亿元。'
    '<b>席位拆解：</b>买入榜上5家机构专用席位集体现身，买二机构净买3.32亿元、买四机构净买1.36亿元、买五机构净买1.17亿元，机构合计净买入超5亿元；'
    '但卖一深股通专用席位净卖出约1.10亿元（北向小幅兑现），卖二/卖三也有机构卖出。整体看机构分歧明显，但买入力度大于卖出。'
    '<b>持续性判断：</b>⭐⭐⭐⭐（4星）。PCB中军龙头，机构集体大买是今日板块爆发的核心推手。'
    '但成交额高达82亿，属于大市值品种，连续涨停概率不高，更可能走趋势慢牛。明日若高开3%以内可低吸，高开5%以上不追；支撑位75元（5日线），目标位90-95元。</p>'
    '<p><b style="color:#f59e0b">▎生益电子（688183）：科创板18.53%大涨，PCB弹性龙头</b><br>'
    '收盘约20.10元（+18.53%），科创板无涨跌幅限制品种，是今日PCB板块最强弹性标的。'
    '龙虎榜显示3家机构净买入，游资也积极参与。公司是生益科技旗下高端PCB子公司，主打AI服务器用高速高频PCB，直接受益于博通AI芯片需求爆发。'
    '<b>持续性判断：</b>⭐⭐⭐（3.5星）。科创板弹性标的，今日大涨后明日可能冲高回落，但中期趋势向好。'
    '适合作为PCB板块情绪风向标观察，若明日继续放量上攻则确认主线地位；回调至17-18元区间可低吸。</p>'
    '<p><b style="color:#f59e0b">▎华工科技（000988）：光模块+PCB双主线加持，机构净买1.2亿</b><br>'
    '收盘66.62元，涨8.93%，成交额约60亿元，龙虎榜净买入约1.20亿元，2家机构净买入。'
    '公司是激光设备龙头，同时布局光模块和PCB，双主线加持。今日放量突破前期平台，形态较好。'
    '<b>持续性判断：</b>⭐⭐⭐（3星）。双主线概念叠加有一定优势，但今日未涨停说明资金认可度略逊于纯PCB龙头。'
    '明日若能站稳65元以上可继续持有，目标位72-75元；跌破60元减仓。</p>'
    '<p><b style="color:#f59e0b">▎中国稀土（000831）：跌停板机构出逃，资源股短期承压</b><br>'
    '收盘跌停40.34元，龙虎榜净卖出约2.30亿元，无机构净买入，游资也以卖出为主。'
    '稀土板块今日集体杀跌，中国稀土跌停是板块情绪冰点。核心原因是前期涨幅过大+美元反弹+资金向科技成长股切换。'
    '<b>持续性判断：</b>⭐⭐（2星）。跌停板无机构抄底说明短期趋势走坏，下方支撑位35-36元。'
    '稀土长期逻辑（新能源+军工需求+供给约束）未变，但短期调整可能持续1-2周，不建议急于抄底。</p>'
    '<p><b style="color:#f59e0b">▎龙虎榜整体结论：</b>今日龙虎榜机构资金主要流向<b>PCB/AI服务器产业链</b>（沪电股份、生益电子、华工科技为代表），'
    '5家机构集体买入沪电股份是强烈信号。资源股（稀土、黄金）则遭遇机构抛售。'
    '整体看机构正在从防御性资源股向科技成长股（半导体/PCB方向）调仓，这一趋势短期不会改变。'
    '北向资金在龙虎榜个股上小幅净卖出（深股通在沪电股份上净卖1.1亿），但整体方向与机构一致。</p>'
    '</div>'
)
gen._components.append(Section(title="🐉 龙虎榜深度席位拆解", content=lhb_deep_html, icon="award"))

# 8. 重点关注标的
focus_html = (
    '<div style="display:flex;flex-direction:column;gap:14px;">'
    '<div style="background:rgba(30,30,50,0.5);border:1px solid rgba(255,255,255,0.08);border-radius:14px;padding:16px 18px;">'
    '  <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px;">'
    '    <span style="font-size:15px;font-weight:700;color:#f1f5f9;">① 深南电路 002916 <span style="color:#10b981;font-size:12px;margin-left:6px;">PCB/AI服务器龙头</span></span>'
    '    <span style="font-size:14px;font-weight:700;color:#10b981;">+5.80%</span>'
    '  </div>'
    '  <div style="font-size:13px;color:#cbd5e1;line-height:1.7;">'
    '  <b>核心逻辑：</b>国内高端PCB龙头，AI服务器PCB核心供应商，深度绑定英伟达/AMD/博通等海外大客户。PCB板块今日全面爆发，深南电路作为行业龙头涨幅相对落后，存在补涨预期。'
    '  <br><b>技术面：</b>今日放量突破120元整数关口，5日线金叉10日线，短期反弹趋势确立。上方压力130元（前高），支撑115元（5日线）。'
    '  <br><b>操作建议：</b>明日开盘价≤122元可建仓10%，目标位135-140元；跌破115元减仓；止损位110元。'
    '  <br><b>风险：</b>板块冲高回落、海外AI需求不及预期。'
    '  </div>'
    '</div>'
    '<div style="background:rgba(30,30,50,0.5);border:1px solid rgba(255,255,255,0.08);border-radius:14px;padding:16px 18px;">'
    '  <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px;">'
    '    <span style="font-size:15px;font-weight:700;color:#f1f5f9;">② 兴森科技 002436 <span style="color:#f59e0b;font-size:12px;margin-left:6px;">IC载板/先进封装</span></span>'
    '    <span style="font-size:14px;font-weight:700;color:#f59e0b;">+3.50%</span>'
    '  </div>'
    '  <div style="font-size:13px;color:#cbd5e1;line-height:1.7;">'
    '  <b>核心逻辑：</b>国内IC载板龙头，先进封装（FCBGA/Chiplet）核心材料供应商。AI芯片带动先进封装需求爆发，IC载板是先进封装关键环节，国产替代空间巨大。PCB板块爆发后，IC载板作为PCB高端细分领域有望接力。'
    '  <br><b>技术面：</b>今日涨3.5%收14.8元，底部区域逐步抬升，5日线拐头向上。上方压力16元（前高），支撑14元（5日线）。'
    '  <br><b>操作建议：</b>14.5元以下可建仓8%，目标位17-18元；跌破13.5元止损。'
    '  <br><b>风险：</b>IC载板国产替代进度慢于预期、行业竞争加剧。'
    '  </div>'
    '</div>'
    '<div style="background:rgba(30,30,50,0.5);border:1px solid rgba(255,255,255,0.08);border-radius:14px;padding:16px 18px;">'
    '  <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px;">'
    '    <span style="font-size:15px;font-weight:700;color:#f1f5f9;">③ 中际旭创 300308 <span style="color:#60a5fa;font-size:12px;margin-left:6px;">光模块龙头/AI算力</span></span>'
    '    <span style="font-size:14px;font-weight:700;color:#60a5fa;">+0.84%</span>'
    '  </div>'
    '  <div style="font-size:13px;color:#cbd5e1;line-height:1.7;">'
    '  <b>核心逻辑：</b>全球光模块龙头，800G/1.6T光模块全球市占率第一，直接受益于AI算力建设。光模块板块经过近两个月调整，估值风险大幅释放，随着PCB/半导体板块爆发，光模块作为AI算力核心环节有补涨需求。'
    '  <br><b>技术面：</b>今日微涨0.84%收396.30元，底部区域震荡整理，380元附近支撑较强。MACD绿柱缩短，KDJ金叉，有企稳反弹迹象。压力位420元（20日线），支撑380元（前期低点）。'
    '  <br><b>操作建议：</b>390元以下可建仓8%，目标位430-450元；跌破375元止损。'
    '  <br><b>风险：</b>北美云厂商资本支出不及预期、光模块价格战加剧。'
    '  </div>'
    '</div>'
    '<div style="background:rgba(30,30,50,0.5);border:1px solid rgba(255,255,255,0.08);border-radius:14px;padding:16px 18px;">'
    '  <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px;">'
    '    <span style="font-size:15px;font-weight:700;color:#f1f5f9;">④ 东山精密 002384 <span style="color:#ef4444;font-size:12px;margin-left:6px;">风险提示股/FPC龙头</span></span>'
    '    <span style="font-size:14px;font-weight:700;color:#ef4444;">+0.06%</span>'
    '  </div>'
    '  <div style="font-size:13px;color:#cbd5e1;line-height:1.7;">'
    '  <b>风险提示：</b>FPC（柔性电路板）龙头，今日仅涨0.06%，明显弱于PCB板块整体（+4.90%）。'
    '  公司Q3业绩增速放缓，且FPC业务受消费电子需求疲软影响较大，与AI服务器PCB逻辑关联度较低。'
    '  在PCB板块集体爆发的背景下，东山精密涨幅垫底说明资金不认可其AI算力逻辑。'
    '  <br><b>操作建议：</b>持有该股者建议借板块热度减仓换股，优先选择纯AI服务器PCB标的（沪电股份、深南电路、生益电子）。'
    '  <br><b>风险：</b>消费电子需求持续疲软、FPC价格竞争加剧。'
    '  </div>'
    '</div>'
    '</div>'
)
gen._components.append(Section(title="🎯 重点关注标的（3+1只）", content=focus_html, icon="target"))

# 9. 明日关键预判
predictions = [
    {"name": "PCB/覆铜板（S级新主线？）", "direction": "看涨", "confidence": 78,
     "reason": "今日板块暴涨4.90%，5家机构集体买入沪电股份，主力净流入46亿元，是近期最强板块性行情。博通AI芯片催化+AI服务器PCB需求爆发逻辑硬核，明日若生益电子/沪电股份继续强势上涨（涨幅>5%），则确认PCB为新的S级主线。预计明日板块分化，前排龙头继续强势，后排跟风股冲高回落。"},
    {"name": "半导体/先进封装", "direction": "震荡偏多", "confidence": 65,
     "reason": "半导体板块连续两日净流入（昨日光刻胶爆发、今日PCB爆发），说明资金在持续加仓半导体方向。但板块内部轮动很快，追高风险大。明日光刻胶/光刻机方向（雅克科技、有研新材等）可能因PCB板块吸金而继续调整，先进封装/封测方向（长电科技、华海诚科）则可能跟随PCB板块补涨。"},
    {"name": "算力/液冷", "direction": "震荡反弹", "confidence": 55,
     "reason": "算力租赁今日涨3.2%，液冷龙头英维克反弹+3.93%，算力链有企稳迹象。但整体仍处于底部震荡阶段，尚未形成趋势性行情。明日若PCB/半导体持续强势，算力板块可能被带动继续反弹；但需警惕资金虹吸效应——PCB太强会吸引其他科技板块资金流出。"},
    {"name": "稀土/黄金/资源股", "direction": "看跌（继续调整）", "confidence": 62,
     "reason": "今日中国稀土跌停、紫金矿业跌5.66%，资源股集体杀跌。资金正从防御性资源股向科技成长股切换，这一趋势短期不会逆转。预计明日资源股继续弱势调整，稀土可能再跌3-5%探底。不建议抄底，等待企稳信号（如缩量止跌、资金回流）。"},
]
gen.add_tomorrow_prediction(predictions=predictions)

# 10. 明日操作计划
plan_html = (
    '<div style="line-height:1.9; font-size:14px;">'
    '<p><b style="color:#f59e0b;font-size:15px;">📌 整体策略：</b></p>'
    '<p>今日PCB/覆铜板板块爆发，确认了科技成长方向的回归。操作上要顺势而为，把仓位从弱势股（*ST建艺等）向半导体/PCB主线集中。'
    '但注意板块内部分化很快（昨日光刻胶→今日PCB），<b>不追高、沿主线低吸</b>是核心原则。整体仓位建议维持60-70%（半导体/PCB主线40%+液冷/算力15%+防御10%）。</p>'
    '<p><b style="color:#f59e0b;font-size:15px;">📈 加仓计划（优先级从高到低）：</b></p>'
    '<p><b>① PCB主线：</b>沪电股份、深南电路回调至5日线可加仓10-15%。沪电股份75-77元区间低吸，深南电路115-118元区间低吸。目标收益15-20%。</p>'
    '<p><b>② 先进封装/封测：</b>长电科技51-52元加仓5%，华海诚科70元以下加仓5%。目标收益10-15%。</p>'
    '<p><b>③ 铜冠铜箔：</b>60元附近（5日线）可加仓5%，PCB上游补涨逻辑。目标收益10%。</p>'
    '<p><b style="color:#f59e0b;font-size:15px;">📉 减仓/止损计划：</b></p>'
    '<p><b>① *ST建艺：</b>明日反弹至7元以上果断减仓至5%以内或清仓，腾出资金加仓主线。跌破6.5元必须止损。</p>'
    '<p><b>② 英维克：</b>反弹至38元（20日线）减仓1/4，降低持仓成本。跌破32元止损。</p>'
    '<p><b>③ 雅克科技：</b>跌破80元（5日线）减仓1/4，跌破75元止损。若明日放量突破86.5元则持有不动甚至加仓。</p>'
    '<p><b>④ 风华高科：</b>反弹至30元减仓1/3，跌破27元减仓。</p>'
    '<p><b style="color:#f59e0b;font-size:15px;">🎯 关键价位一览：</b></p>'
    '<table style="width:100%;border-collapse:collapse;font-size:13px;margin-top:8px;">'
    '<tr style="background:rgba(255,255,255,0.05);">'
    '<th style="padding:8px;text-align:left;border-bottom:1px solid rgba(255,255,255,0.1);">标的</th>'
    '<th style="padding:8px;text-align:center;border-bottom:1px solid rgba(255,255,255,0.1);">支撑位</th>'
    '<th style="padding:8px;text-align:center;border-bottom:1px solid rgba(255,255,255,0.1);">压力位</th>'
    '<th style="padding:8px;text-align:center;border-bottom:1px solid rgba(255,255,255,0.1);">止损位</th>'
    '<th style="padding:8px;text-align:center;border-bottom:1px solid rgba(255,255,255,0.1);">目标位</th>'
    '</tr>'
    '<tr><td style="padding:8px;border-bottom:1px solid rgba(255,255,255,0.05);">英维克</td><td style="padding:8px;text-align:center;color:#10b981;">34元</td><td style="padding:8px;text-align:center;color:#ef4444;">38元</td><td style="padding:8px;text-align:center;color:#ef4444;">32元</td><td style="padding:8px;text-align:center;color:#f59e0b;">40元</td></tr>'
    '<tr><td style="padding:8px;border-bottom:1px solid rgba(255,255,255,0.05);">铜冠铜箔</td><td style="padding:8px;text-align:center;color:#10b981;">60元</td><td style="padding:8px;text-align:center;color:#ef4444;">65元</td><td style="padding:8px;text-align:center;color:#ef4444;">56元</td><td style="padding:8px;text-align:center;color:#f59e0b;">68-70元</td></tr>'
    '<tr><td style="padding:8px;border-bottom:1px solid rgba(255,255,255,0.05);">雅克科技</td><td style="padding:8px;text-align:center;color:#10b981;">80元</td><td style="padding:8px;text-align:center;color:#ef4444;">86.5元</td><td style="padding:8px;text-align:center;color:#ef4444;">75元</td><td style="padding:8px;text-align:center;color:#f59e0b;">95-100元</td></tr>'
    '<tr><td style="padding:8px;border-bottom:1px solid rgba(255,255,255,0.05);">*ST建艺</td><td style="padding:8px;text-align:center;color:#10b981;">6.5元</td><td style="padding:8px;text-align:center;color:#ef4444;">7.2元</td><td style="padding:8px;text-align:center;color:#ef4444;">6.5元</td><td style="padding:8px;text-align:center;color:#f59e0b;">减仓为主</td></tr>'
    '<tr><td style="padding:8px;border-bottom:1px solid rgba(255,255,255,0.05);">华海诚科</td><td style="padding:8px;text-align:center;color:#10b981;">70元</td><td style="padding:8px;text-align:center;color:#ef4444;">78元</td><td style="padding:8px;text-align:center;color:#ef4444;">66元</td><td style="padding:8px;text-align:center;color:#f59e0b;">80-85元</td></tr>'
    '<tr><td style="padding:8px;border-bottom:1px solid rgba(255,255,255,0.05);">长电科技</td><td style="padding:8px;text-align:center;color:#10b981;">52元</td><td style="padding:8px;text-align:center;color:#ef4444;">55元</td><td style="padding:8px;text-align:center;color:#ef4444;">48元</td><td style="padding:8px;text-align:center;color:#f59e0b;">60-62元</td></tr>'
    '<tr><td style="padding:8px;border-bottom:1px solid rgba(255,255,255,0.05);">风华高科</td><td style="padding:8px;text-align:center;color:#10b981;">27元</td><td style="padding:8px;text-align:center;color:#ef4444;">30元</td><td style="padding:8px;text-align:center;color:#ef4444;">25元</td><td style="padding:8px;text-align:center;color:#f59e0b;">32-35元</td></tr>'
    '</table>'
    '<p style="margin-top:16px;"><b style="color:#f59e0b;font-size:15px;">⏰ 明日关注时间点：</b></p>'
    '<p>• 9:25 集合竞价：观察PCB板块龙头（沪电股份、生益电子）竞价强度，判断板块持续性</p>'
    '<p>• 10:00 半小时成交量：若PCB板块半小时成交超昨日全天30%，则确认主线地位</p>'
    '<p>• 14:00 午后资金流向：观察是否有新板块接力（如先进封装、光模块）</p>'
    '</div>'
)
gen._components.append(Section(title="🎯 明日操作策略", content=plan_html, icon="target", variant="highlight"))

# 11. 风险提示
gen.add_risk_warning(risks=[
    "PCB板块明日冲高回落风险：今日涨幅过大（元件+4.90%），且内部已出现分化（东山精密等仅微涨），明日若量能不济可能冲高回落，追高需谨慎",
    "半导体板块轮动过快风险：昨日光刻胶→今日PCB，资金在半导体内部快速轮动，持有非主线方向可能赚指数不赚钱",
    "*ST建艺继续下跌风险：今日大跌5.82%且跌破7元关口，ST板块整体弱势，若明日继续放量下跌可能触发止损",
    "外部市场风险：美股科技股波动、美元指数反弹可能影响A股科技板块情绪，需关注今晚纳斯达克表现",
    "年底资金面收紧风险：11月底临近年底，部分机构有兑现收益需求，可能对高位成长股形成压力"
])

# 12. 晚间重要新闻
evening_news = [
    {"title": "半导体设备材料国产替代加速推进", "content": "据行业消息，中芯国际、长江存储等国内头部晶圆厂持续推进设备材料国产化验证，多家半导体材料公司Q4订单环比增长超30%", "time": "18:30", "source": "财联社", "tag": "行业", "tag_variant": "primary"},
    {"title": "AI服务器PCB需求持续超预期", "content": "据供应链消息，博通AI芯片相关PCB订单饱满，头部PCB厂商Q4排产已超Q3，高端HDI板加工费环比上涨5-10%", "time": "19:00", "source": "科创板日报", "tag": "产业", "tag_variant": "success"},
    {"title": "国内大模型用户规模持续快速增长", "content": "最新数据显示，国内头部AI大模型月活用户已突破3亿，算力需求持续攀升，第三方算力租赁价格稳中有升", "time": "19:30", "source": "TheElec", "tag": "AI", "tag_variant": "warning"},
]
gen.add_evening_news(news_list=evening_news)

# 发布
result = gen.publish(title="盘后速递", auto_deploy=False, docs_root="docs")
print(f"✅ 盘后速递生成完成: {result}")
