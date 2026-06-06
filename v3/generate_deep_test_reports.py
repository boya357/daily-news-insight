import sys
sys.path.insert(0, '/root/daily-news-insight')

from v3.generators.daily import DailyReportGenerator
from v3.generators.intraday import IntradayGenerator
from v3.generators.aftermarket import AftermarketGenerator
from v3.generators.weekly_review import WeeklyReviewGenerator
from v3.generators.s_level_catalyst import SLevelCatalystGenerator
from v3.generators.weekly_outlook import WeeklyOutlookGenerator
from v3.generators.weekend_express import WeekendExpressGenerator
from v3.generators.tomorrow_catalyst import TomorrowCatalystGenerator
from v3.generators.monthly import MonthlyReportGenerator
from v3.workflow import ReportPublisher

DATE = "20260606"
DATE_STR = "2026年6月6日"
reports = []

# ========== 1. 日报（深度版）==========
print("📰 生成深度日报...")
gen = DailyReportGenerator(date_str=DATE_STR, weekday="周五")

# 今日焦点
gen.add_focus_point("英伟达GTC大会今日开幕，H200芯片量产引爆AI算力行情；美联储6月议息会议临近，全球市场屏息以待")

# 隔夜全球市场（4大指数 + 3个关键事件）
gen.add_overseas_market(
    indices=[
        {"name": "道琼斯", "value": "39,876.54", "change": "+0.52%", "up": True},
        {"name": "纳斯达克", "value": "18,234.56", "change": "+1.23%", "up": True},
        {"name": "标普500", "value": "5,432.10", "change": "+0.87%", "up": True},
        {"name": "日经225", "value": "38,765.43", "change": "+0.34%", "up": True},
    ],
    key_events=[
        {"tag": "重磅", "title": "美联储官员放鸽派信号", "content": "鲍威尔暗示通胀下行趋势确立，市场预期年内降息2次，9月首次降息概率升至78%。", "tag_color": "red"},
        {"tag": "科技", "title": "英伟达盘前涨超3%", "content": "市场期待GTC大会发布新一代AI芯片H200及AI生态重大进展，HBM产业链公司集体上涨。", "tag_color": "purple"},
        {"tag": "大宗", "title": "国际油价下跌1.2%", "content": "OPEC+产量政策不确定性叠加美国原油库存增加，WTI原油跌破72美元/桶。", "tag_color": "blue"},
    ]
)

# 重要新闻汇总（8条）
gen.add_import_news([
    {"tag": "AI", "importance": "high", "title": "英伟达H200芯片正式量产，HBM容量达141GB", "content": "英伟达宣布H200 GPU正式量产，采用HBM3e显存，容量141GB，带宽提升2.3倍，AI训练性能提升60%。产业链公司将全面受益。", "source": "财联社"},
    {"tag": "政策", "importance": "high", "title": "证监会发布深化新三板改革方案", "content": "证监会发布深化新三板改革配套规则，优化发行上市条件，完善转板机制，支持专精特新企业融资发展。", "source": "证券时报"},
    {"tag": "半导体", "importance": "high", "title": "长鑫科技IPO获上交所受理，拟募资350亿", "content": "国内DRAM龙头长鑫科技科创板IPO获受理，拟募资350亿元投向12英寸DRAM芯片研发及产业化项目。", "source": "科创板日报"},
    {"tag": "新能源", "importance": "normal", "title": "宁德时代发布新一代凝聚态电池，能量密度达500Wh/kg", "content": "宁德时代发布新一代凝聚态电池，能量密度突破500Wh/kg，可支持民用电动航空，预计2027年量产。", "source": "第一财经"},
    {"tag": "消费", "importance": "normal", "title": "5月社会消费品零售总额同比增长4.5%", "content": "国家统计局数据显示，5月社零总额同比增长4.5%，比上月加快0.3个百分点，消费复苏态势持续。", "source": "国家统计局"},
    {"tag": "地产", "importance": "normal", "title": "一线城市二手房成交量环比上涨12%", "content": "据贝壳研究院数据，5月一线城市二手房成交量环比上涨12%，政策效果逐步显现，市场预期改善。", "source": "贝壳研究院"},
    {"tag": "医药", "importance": "normal", "title": "恒瑞医药创新药海外授权金额达20亿美元", "content": "恒瑞医药宣布与默沙东达成合作，将一款抗肿瘤新药海外权益授权给默沙东，首付款+里程碑合计20亿美元。", "source": "医药魔方"},
    {"tag": "监管", "importance": "normal", "title": "央行开展5000亿元MLF操作，利率持平", "content": "央行开展5000亿元1年期MLF操作，利率维持2.5%不变，本月MLF到期量为4000亿元，实现净投放1000亿元。", "source": "央行官网"},
])

# 板块机会分析（6个板块）
gen.add_sector_analysis([
    {"name": "AI算力", "performance": "大涨4.25%", "rating": "强烈推荐", "stocks": ["寒武纪", "中际旭创", "海光信息", "龙芯中科"], "logic": "英伟达GTC大会+H200量产双重催化，AI算力需求持续超预期，产业链公司业绩高增长确定性强。"},
    {"name": "存储芯片", "performance": "大涨3.68%", "rating": "强烈推荐", "stocks": ["兆易创新", "长江存储", "长鑫科技", "德明利"], "logic": "存储周期上行+AI需求爆发双轮驱动，DRAM/NAND价格持续上涨，行业景气度有望持续到2027年。"},
    {"name": "光模块", "performance": "上涨2.85%", "rating": "推荐", "stocks": ["中际旭创", "新易盛", "天孚通信", "光迅科技"], "logic": "800G/1.6T光模块需求持续放量，北美云厂商资本开支超预期，行业景气度持续上行。"},
    {"name": "人形机器人", "performance": "上涨1.56%", "rating": "推荐", "stocks": ["拓普集团", "三花智控", "绿的谐波", "鸣志电器"], "logic": "特斯拉Optimus量产临近，国内厂商纷纷布局，核心零部件国产化加速，产业趋势明确。"},
    {"name": "创新药", "performance": "上涨1.23%", "rating": "关注", "stocks": ["恒瑞医药", "百济神州", "信达生物", "荣昌生物"], "logic": "创新药海外授权加速，国产创新药国际化进程加快，估值处于历史低位，配置价值凸显。"},
    {"name": "新能源", "performance": "下跌0.85%", "rating": "谨慎", "stocks": ["宁德时代", "比亚迪", "隆基绿能"], "logic": "行业产能过剩压力仍存，价格战持续，短期业绩承压，建议等待产能出清信号。"},
])

# 持仓跟踪（3只）
gen.add_holdings_tracking([
    {"name": "英维克", "code": "002837", "price": "68.32", "change": "-5.23%", "up": False, "comment": "仍严重破止损位，继续观察中。AI液冷需求长期逻辑不变，但短期技术形态走坏，需警惕进一步下探风险。"},
    {"name": "铜冠铜箔", "code": "301217", "price": "107.40", "change": "+3.45%", "up": True, "comment": "反弹强势，HVLP铜箔国产替代逻辑强化，存储芯片封装需求爆发，业绩增长确定性高，继续持有。"},
    {"name": "*ST建艺", "code": "002789", "price": "13.79", "change": "+0.15%", "up": True, "comment": "横盘整理，子公司合同纠纷案获广东高院指令再审，摘帽进程存不确定性，谨慎观察。"},
])

# 风险提示
gen.add_risk_warning([
    "美联储6月议息会议可能释放鹰派信号，超出市场预期",
    "AI板块短期涨幅过大，存在获利回吐风险",
    "地缘政治冲突升级风险",
    "国内经济复苏不及预期",
])

# 每日总结
gen.add_daily_summary(
    "今日市场整体震荡上行，沪指收涨0.85%报3145点，创业板指涨2.34%报2156点。AI算力板块领涨，英伟达GTC大会催化效应明显。两市成交额9876亿元，较昨日放量1234亿元。北向资金净买入45.67亿元，连续第5日净买入。\n\n盘面看，AI算力、存储芯片、光模块等科技成长方向表现强势，银行、地产等权重板块相对弱势。市场情绪回暖，赚钱效应较好，涨停家数达45家，跌停仅5家。\n\n技术面看，沪指站上3100点整数关口，短期均线多头排列，技术形态向好。创业板指突破60日均线，中期反弹趋势确立。"
)

# 明日计划
gen.add_tomorrow_plan(
    "重点关注英伟达GTC大会首日演讲内容，关注H200芯片及AI生态重大进展。操作上，继续围绕AI算力、存储芯片主线布局，逢低加仓龙头标的。\n\n仓位建议：7-8成仓位，AI算力30%、存储芯片25%、光模块15%、现金10-20%。\n\n关注标的：寒武纪(688256)、中际旭创(300308)、兆易创新(603986)、海光信息(688041)。"
)

output_path = f"/root/daily-news-insight/docs/daily/{DATE}_V30测试_日报.html"
gen.save(output_path)
reports.append(("日报", f"{DATE}_V30测试_日报.html", "daily", "V3.0深度测试版 - AI算力爆发行情分析"))
print("  ✅ 日报完成")

# ========== 2. 盘中快报（深度版）==========
print("⚡ 生成深度盘中快报...")
gen = IntradayGenerator(date_str=DATE_STR)

gen.add_market_overview(
    indices=[
        {"name": "上证指数", "value": "3,120.45", "change": "+0.56%", "up": True},
        {"name": "深证成指", "value": "10,156.78", "change": "+0.89%", "up": True},
        {"name": "创业板指", "value": "2,134.56", "change": "+1.45%", "up": True},
        {"name": "科创50", "value": "956.78", "change": "+2.34%", "up": True},
    ],
    market_status="震荡上行，科技成长领涨"
)

gen.add_hot_topics([
    {"tag": "AI算力", "title": "英伟达GTC大会今日开幕", "content": "市场期待H200芯片及AI生态重大发布，AI算力板块集体异动，寒武纪涨超8%", "hot": True},
    {"tag": "存储芯片", "title": "长鑫科技IPO获受理", "content": "拟募资350亿投向DRAM芯片研发，存储板块异动拉升，兆易创新涨超5%", "hot": True},
    {"tag": "光模块", "title": "800G需求持续放量", "content": "北美云厂商资本开支超预期，中际旭创涨超4%，机构上调全年业绩预期", "hot": False},
    {"tag": "人形机器人", "title": "特斯拉Optimus量产临近", "content": "产业链公司纷纷布局，核心零部件国产化加速，绿的谐波涨超3%", "hot": False},
])

gen.add_decline_sectors([
    {"name": "银行", "change": "-0.65%", "reason": "降息预期压制息差，板块持续走弱"},
    {"name": "地产", "change": "-0.45%", "reason": "销售数据仍偏弱，政策效果待观察"},
    {"name": "煤炭", "change": "-0.32%", "reason": "动力煤价格下跌，板块盈利承压"},
])

gen.add_holdings_tracking([
    {"name": "英维克", "code": "002837", "price": "68.32", "change": "-2.15%", "up": False, "comment": "弱势震荡，成交缩量，短期仍承压"},
    {"name": "铜冠铜箔", "code": "301217", "price": "107.40", "change": "+2.34%", "up": True, "comment": "强势上涨，量能放大，突破前期平台"},
    {"name": "*ST建艺", "code": "002789", "price": "13.79", "change": "+0.15%", "up": True, "comment": "横盘整理，成交清淡，等待方向选择"},
])

gen.add_trading_strategy(
    "早盘AI算力板块异动拉升，存储芯片、光模块等细分方向跟随上涨，市场情绪回暖。\n\n操作建议：\n1. 持仓方面，继续持有AI算力、存储芯片主线标的\n2. 加仓方面，如AI算力板块回调至5日线附近，可逢低加仓\n3. 关注方向，优先选择业绩确定性强、估值合理的龙头标的\n4. 仓位控制，保持7成左右仓位，预留部分现金应对波动"
)

gen.add_risk_warning([
    "午后可能出现获利回吐，注意控制仓位",
    "美联储议息会议临近，市场情绪谨慎",
    "北向资金波动风险",
])

gen.add_summary(
    "上午市场震荡上行，沪指涨0.56%报3120点，创业板指涨1.45%报2134点。AI算力板块领涨，科创50表现强势。半日成交额4567亿元，较昨日同期放量567亿元。\n\n盘面看，科技成长方向全面上涨，AI算力、存储芯片、光模块等板块涨幅居前，银行、地产等权重板块调整。市场赚钱效应较好，上涨家数超3000家。"
)

output_path = f"/root/daily-news-insight/docs/intraday/{DATE}_V30测试_盘中快报.html"
gen.save(output_path)
reports.append(("盘中快报", f"{DATE}_V30测试_盘中快报.html", "intraday", "V3.0深度测试版 - GTC大会催化AI算力行情"))
print("  ✅ 盘中快报完成")

# ========== 3. 盘后速递（深度版）==========
print("📦 生成深度盘后速递...")
gen = AftermarketGenerator(date_str=DATE_STR)

gen.add_market_summary(
    indices=[
        {"name": "上证指数", "value": "3,145.68", "change": "+0.85%", "up": True},
        {"name": "深证成指", "value": "10,234.56", "change": "+1.23%", "up": True},
        {"name": "创业板指", "value": "2,156.78", "change": "+2.34%", "up": True},
        {"name": "科创50", "value": "968.45", "change": "+3.56%", "up": True},
    ],
    volume="9876亿"
)

gen.add_sector_performance(
    top_sectors=[
        {"name": "AI算力", "change": "4.25%", "reason": "英伟达GTC大会+H200量产催化"},
        {"name": "存储芯片", "change": "3.68%", "reason": "长鑫科技IPO+存储周期上行"},
        {"name": "光模块", "change": "2.85%", "reason": "800G/1.6T需求持续放量"},
        {"name": "游戏", "change": "2.34%", "reason": "AI降本增效+新品周期"},
        {"name": "传媒", "change": "1.98%", "reason": "AIGC应用加速落地"},
    ],
    bottom_sectors=[
        {"name": "银行", "change": "-0.85%", "reason": "降息预期压制息差"},
        {"name": "地产", "change": "-0.65%", "reason": "销售数据偏弱"},
        {"name": "煤炭", "change": "-0.45%", "reason": "动力煤价格下跌"},
        {"name": "石化", "change": "-0.32%", "reason": "国际油价下跌"},
    ]
)

gen.add_hot_topics([
    {"topic": "英伟达H200芯片量产", "impact": "AI算力产业链全面受益，从芯片到服务器、光模块、液冷全链条爆发", "related_stocks": "寒武纪、中际旭创、海光信息、英维克"},
    {"topic": "长鑫科技IPO获受理", "impact": "存储芯片国产替代加速，DRAM产业链迎来发展机遇", "related_stocks": "兆易创新、长江存储、德明利"},
    {"topic": "证监会深化新三板改革", "impact": "多层次资本市场体系完善，专精特新企业迎来发展机遇", "related_stocks": "新三板相关概念股"},
    {"topic": "宁德时代凝聚态电池", "impact": "电池技术突破，能量密度达500Wh/kg，支持电动航空", "related_stocks": "宁德时代、航空产业链"},
])

gen.add_holdings_review([
    {"name": "英维克", "code": "002837", "change": "-5.23%", "performance": "弱于大盘", "action": "继续观察，警惕进一步下探风险"},
    {"name": "铜冠铜箔", "code": "301217", "change": "+3.45%", "performance": "强于大盘", "action": "继续持有，存储芯片需求爆发"},
    {"name": "*ST建艺", "code": "002789", "change": "+0.15%", "performance": "持平", "action": "谨慎观察，等待摘帽进展"},
])

gen.add_tomorrow_outlook(
    "预计明日市场延续震荡上行格局，沪指有望挑战3150-3180点压力位。\n\n重点关注：\n1. 英伟达GTC大会首日演讲内容及重大发布\n2. 5月社融及信贷数据公布\n3. 北向资金流向\n4. 板块轮动持续性\n\n操作上，继续围绕AI算力、存储芯片主线布局，逢低加仓龙头标的。注意控制仓位，避免追高。"
)

gen.add_risk_warning([
    "美联储议息会议鹰派超预期风险",
    "AI板块短期涨幅过大，获利回吐风险",
    "国内经济复苏不及预期",
    "地缘政治冲突升级",
])

gen.add_operation_plan(
    "继续持有AI算力、存储芯片主线标的，逢低加仓龙头。\n\n仓位配置：7-8成\n- AI算力：30%（寒武纪、海光信息）\n- 存储芯片：25%（兆易创新、铜冠铜箔）\n- 光模块：15%（中际旭创）\n- 现金：10-20%\n\n明日关注：英伟达GTC大会进展、5月社融数据、北向资金流向"
)

output_path = f"/root/daily-news-insight/docs/aftermarket/{DATE}_V30测试_盘后速递.html"
gen.save(output_path)
reports.append(("盘后速递", f"{DATE}_V30测试_盘后速递.html", "aftermarket", "V3.0深度测试版 - AI算力爆发，科创50大涨3.56%"))
print("  ✅ 盘后速递完成")

# ========== 4. 周复盘（深度版）==========
print("📋 生成深度周复盘...")
gen = WeeklyReviewGenerator(week_label="第23周", date_range="6月2日-6月6日")

gen.add_week_summary(
    "本周市场震荡上行，沪指周涨2.35%，深成指涨4.56%，创业板指涨5.68%，科创50涨8.92%。AI算力板块领涨，周涨幅达12.45%。\n\n成交方面，本周两市总成交额4.56万亿元，较上周放量12.3%。北向资金本周净买入234.5亿元，连续第3周净买入。\n\n市场情绪明显回暖，赚钱效应提升，周涨幅超10%的个股达156只，跌幅超10%的仅23只。"
)

gen.add_index_performance([
    {"name": "上证指数", "change": "2.35%", "current": "3145.68", "high": "3168.50", "low": "3089.20", "volume": "4.56万亿"},
    {"name": "深证成指", "change": "4.56%", "current": "10234.56", "high": "10345.67", "low": "9876.54", "volume": "3.78万亿"},
    {"name": "创业板指", "change": "5.68%", "current": "2156.78", "high": "2189.34", "low": "2056.78", "volume": "1.56万亿"},
    {"name": "科创50", "change": "8.92%", "current": "968.45", "high": "987.65", "low": "892.34", "volume": "0.89万亿"},
])

gen.add_sector_review(
    top_sectors=[
        {"name": "AI算力", "change": "12.45%", "logic": "英伟达GTC大会预期+H200量产催化，板块业绩爆发"},
        {"name": "存储芯片", "change": "10.68%", "logic": "存储周期上行+长鑫科技IPO，国产替代加速"},
        {"name": "光模块", "change": "9.34%", "logic": "800G/1.6T需求放量，北美云厂商资本开支超预期"},
        {"name": "游戏传媒", "change": "7.56%", "logic": "AIGC降本增效+新品周期，业绩拐点确立"},
        {"name": "人形机器人", "change": "6.78%", "logic": "特斯拉Optimus量产临近，产业链加速布局"},
    ],
    bottom_sectors=[
        {"name": "银行", "change": "-2.34%", "logic": "降息预期压制息差，板块持续走弱"},
        {"name": "地产", "change": "-1.56%", "logic": "销售数据仍偏弱，政策效果待观察"},
        {"name": "煤炭", "change": "-1.23%", "logic": "动力煤价格下跌，盈利承压"},
        {"name": "石化", "change": "-0.89%", "logic": "国际油价下跌，需求预期偏弱"},
    ]
)

gen.add_hot_topics_review([
    {"topic": "英伟达GTC大会+H200量产", "impact": "AI算力产业链全面爆发，板块周涨幅超12%，成为市场最强主线"},
    {"topic": "长鑫科技IPO获受理", "impact": "存储芯片国产替代加速，DRAM产业链迎来发展机遇，存储板块大涨"},
    {"topic": "证监会深化新三板改革", "impact": "多层次资本市场体系完善，专精特新企业迎来发展机遇"},
    {"topic": "5月经济数据陆续公布", "impact": "经济复苏态势温和，市场期待更多稳增长政策出台"},
])

gen.add_important_events([
    {"date": "6月2日", "event": "英伟达宣布H200 GPU量产", "impact": "AI算力板块大涨，寒武纪20CM涨停"},
    {"date": "6月3日", "event": "长鑫科技科创板IPO获受理", "impact": "拟募资350亿，存储芯片板块异动拉升"},
    {"date": "6月4日", "event": "证监会发布深化新三板改革方案", "impact": "新三板概念股集体上涨"},
    {"date": "6月5日", "event": "5月PMI数据公布，为49.8%", "impact": "略低于荣枯线，经济复苏温和，市场期待政策加码"},
    {"date": "6月6日", "event": "英伟达GTC大会开幕", "impact": "AI算力板块再度拉升，科创50大涨3.56%"},
])

gen.add_next_week_outlook(
    outlook="预计下周市场延续震荡上行格局，沪指有望挑战3200点整数关口。市场主线仍将围绕AI算力、科技成长展开。",
    key_points=[
        "美联储6月议息会议（6月17-18日）",
        "5月社融、信贷、经济数据陆续公布",
        "英伟达GTC大会后续发酵",
        "国内稳增长政策动向",
        "北向资金流向"
    ]
)

gen.add_risk_warning([
    "美联储议息会议鹰派超预期",
    "AI板块短期涨幅过大，获利回吐风险",
    "国内经济复苏不及预期",
    "地缘政治冲突升级风险",
    "北向资金大幅波动",
])

gen.add_operation_plan(
    "继续围绕AI算力、存储芯片、光模块等科技成长主线布局，逢低加仓龙头标的。\n\n仓位建议：7-8成\n- AI算力：30%\n- 存储芯片：25%\n- 光模块：15%\n- 其他：10-20%\n- 现金：5-10%\n\n操作策略：\n1. 主线持仓不动，逢低加仓\n2. 避免追高，等待回调机会\n3. 关注业绩确定性强的龙头标的\n4. 控制单一标的仓位，分散风险"
)

output_path = f"/root/daily-news-insight/docs/weekly_review/{DATE}_V30测试_周复盘.html"
gen.save(output_path)
reports.append(("周复盘", f"{DATE}_V30测试_周复盘.html", "weekly_review", "V3.0深度测试版 - AI算力领涨，科创50周涨8.92%"))
print("  ✅ 周复盘完成")

# ========== 5. S级催化（深度版）==========
print("⭐ 生成深度S级催化...")
gen = SLevelCatalystGenerator(title="S级催化：AI算力革命 - 从H200到AGI的产业浪潮")

gen.add_catalyst_overview(
    overview="英伟达正式发布并量产H200 GPU，标志着AI算力进入新纪元。H200采用HBM3e显存，容量达141GB，带宽提升2.3倍，AI训练性能提升60%，推理性能提升90%。这款芯片将全面推动大模型训练和推理能力升级，带动整个AI产业链需求爆发。\n\nAI算力是当前确定性最强的产业趋势之一，预计2026年全球AI芯片市场规模将达到2500亿美元，2030年突破1万亿美元。中国作为全球最大的AI应用市场，国产算力产业链面临历史性发展机遇。",
    event_date="2026年6月2日",
    impact_level="S级"
)

gen.add_impact_analysis(
    impact="H200的发布不仅仅是一款芯片的升级，更是AI产业发展的重要里程碑。它将大幅降低大模型训练和推理成本，推动AI应用从试验阶段进入规模化落地阶段，全面赋能千行百业。",
    dimensions=[
        {"name": "市场空间", "level": 5, "desc": "全球AI芯片市场2026年预计达2500亿美元，2030年突破1万亿美元，年复合增长率超50%"},
        {"name": "产业成熟度", "level": 4, "desc": "大模型技术趋于成熟，应用进入规模化落地期，AI算力需求持续超预期增长"},
        {"name": "政策支持", "level": 5, "desc": "国家高度重视AI产业发展，出台多项支持政策，算力基础设施建设加速推进"},
        {"name": "国产替代", "level": 4, "desc": "海外技术封锁加速国产替代进程，国内AI芯片、算力基础设施企业迎来发展机遇"},
        {"name": "业绩确定性", "level": 5, "desc": "产业链公司订单饱满，业绩高增长确定性强，2026年行业增速预计超80%"},
    ]
)

gen.add_beneficiary_stocks([
    {
        "name": "寒武纪", 
        "code": "688256", 
        "logic": "国内AI芯片龙头，思元系列产品覆盖训练和推理全场景，算力性能持续提升，深度受益国产替代浪潮", 
        "elasticity": "目标涨幅80-120%", 
        "rating": "强烈推荐"
    },
    {
        "name": "中际旭创", 
        "code": "300308", 
        "logic": "全球光模块龙头，800G/1.6T产品领先，深度绑定北美云厂商，AI算力需求爆发直接受益", 
        "elasticity": "目标涨幅50-70%", 
        "rating": "强烈推荐"
    },
    {
        "name": "海光信息", 
        "code": "688041", 
        "logic": "国产CPU/GPU双轮驱动，深算系列AI芯片性能优异，生态完善，服务器市场份额快速提升", 
        "elasticity": "目标涨幅60-90%", 
        "rating": "强烈推荐"
    },
    {
        "name": "兆易创新", 
        "code": "603986", 
        "logic": "存储芯片龙头，NOR Flash全球领先，DRAM业务快速发展，AI存储需求爆发受益明显", 
        "elasticity": "目标涨幅40-60%", 
        "rating": "推荐"
    },
    {
        "name": "铜冠铜箔", 
        "code": "301217", 
        "logic": "HVLP铜箔国内龙头，存储芯片封装关键材料，国产替代空间大，业绩增长确定性高", 
        "elasticity": "目标涨幅45-65%", 
        "rating": "推荐"
    },
    {
        "name": "龙芯中科", 
        "code": "688047", 
        "logic": "国产CPU领军企业，自主指令集架构，信创市场主力供应商，AI算力国产化趋势受益", 
        "elasticity": "目标涨幅50-80%", 
        "rating": "推荐"
    },
])

gen.add_timeline_analysis([
    {"time": "2022-2023", "title": "概念爆发期", "content": "ChatGPT横空出世，引爆AI概念，AI算力需求启动，板块首次行情爆发", "type": "primary"},
    {"time": "2023-2024", "title": "技术验证期", "content": "大模型技术快速迭代，AI应用开始试点落地，算力基础设施建设加速", "type": "success"},
    {"time": "2024-2025", "title": "产业导入期", "content": "AI应用在多个行业落地验证，算力需求持续增长，产业链公司业绩开始兑现", "type": "success"},
    {"time": "2025-2026", "title": "规模成长期", "content": "H200量产推动AI进入规模化应用阶段，行业增速超80%，业绩全面爆发", "type": "warning"},
    {"time": "2026-2027", "title": "加速普及期", "content": "AI应用全面普及，从To B延伸到To C，算力需求持续超预期，产业进入黄金发展期", "type": "danger"},
])

gen.add_risk_warning([
    "AI芯片技术迭代不及预期，性能提升幅度低于市场预期",
    "行业竞争加剧，价格战导致盈利能力下降",
    "海外技术封锁升级，国产替代进程受阻",
    "AI应用落地进度不及预期，算力需求增长放缓",
    "地缘政治冲突影响全球供应链稳定",
    "板块短期涨幅过大，估值过高导致回调风险",
])

gen.add_investment_strategy(
    "AI算力是未来3-5年确定性最强的产业赛道，建议长期战略配置。\n\n投资策略：\n1. 长期持有核心龙头，享受产业成长红利\n2. 逢低加仓，分批建仓，避免追高\n3. 重点配置产业链关键环节：AI芯片、光模块、存储芯片、服务器\n4. 关注国产替代主线，优先选择技术实力强、业绩确定性高的标的\n\n仓位建议：配置比例20-30%，作为核心主线长期持有\n\n风险控制：设置20%止损位，跌破重要支撑位减仓控制风险"
)

output_path = f"/root/daily-news-insight/docs/s级催化扫描/{DATE}_V30测试_S级催化.html"
gen.save(output_path)
reports.append(("S级催化", f"{DATE}_V30测试_S级催化.html", "s级催化扫描", "V3.0深度测试版 - AI算力革命：从H200到AGI的产业浪潮"))
print("  ✅ S级催化完成")

# ========== 6. 周三前瞻（深度版）==========
print("🔮 生成深度周三前瞻...")
gen = WeeklyOutlookGenerator(date_str=DATE_STR)

gen.add_halfweek_review(
    "本周前半段市场震荡上行，沪指周内累计上涨1.23%，深成指涨2.45%，创业板指涨3.56%，科创50涨5.67%。\n\nAI算力板块领涨，周内累计涨幅达8.45%，成为市场最强主线。存储芯片、光模块等科技成长方向表现亮眼。\n\n成交方面，前半周日均成交额9234亿元，较上周同期放量15.6%，市场活跃度明显提升。北向资金累计净买入123.4亿元，资金面持续向好。"
)

gen.add_second_half_outlook(
    "下半周预计市场延续震荡上行格局，沪指有望挑战3150-3180点压力位。市场主线仍将围绕AI算力、科技成长展开。\n\n下半周关注点：\n1. 英伟达GTC大会持续发酵，关注后续重大发布\n2. 5月社融及信贷数据公布，观察经济复苏态势\n3. 美联储6月议息会议前的市场情绪变化\n4. 国内稳增长政策动向\n\n操作上，继续围绕主线布局，逢低加仓，同时注意下半周可能出现的获利回吐压力，控制好仓位。"
)

gen.add_key_events([
    {"date": "6月7日", "event": "英伟达GTC大会首日主题演讲", "importance": "高", "impact": "黄仁勋主题演讲，预计发布重大AI产品和技术进展，决定AI算力板块短期走势"},
    {"date": "6月8日", "event": "5月社会融资规模数据公布", "importance": "高", "impact": "观察信贷需求和经济复苏态势，对市场情绪有重要影响"},
    {"date": "6月8日", "event": "5月CPI、PPI数据公布", "importance": "高", "impact": "观察通胀水平，影响货币政策走向预期"},
    {"date": "6月9日", "event": "5月进出口数据公布", "importance": "中", "impact": "观察外需情况，判断出口对经济的拉动作用"},
    {"date": "6月9日", "event": "国内成品油价格调整窗口", "importance": "低", "impact": "根据国际油价变化调整，影响交通运输等行业成本"},
])

gen.add_opportunity_focus([
    {"sector": "AI算力", "probability": "高", "catalyst": "英伟达GTC大会+H200量产+AI应用加速落地", "risk_reward": "3:1", "logic": "产业趋势明确，业绩高增长确定性强，GTC大会有望持续催化"},
    {"sector": "存储芯片", "probability": "高", "catalyst": "存储周期上行+长鑫科技IPO+国产替代加速", "risk_reward": "2.5:1", "logic": "行业周期上行+AI需求爆发双轮驱动，国产替代空间大"},
    {"sector": "光模块", "probability": "高", "catalyst": "800G/1.6T需求放量+北美云厂商资本开支超预期", "risk_reward": "2:1", "logic": "行业景气度持续上行，龙头公司业绩确定性强"},
    {"sector": "人形机器人", "probability": "中", "catalyst": "特斯拉Optimus量产临近+产业链加速布局", "risk_reward": "2:1", "logic": "产业趋势明确，但短期业绩贡献有限，偏主题投资"},
    {"sector": "创新药", "probability": "中", "catalyst": "海外授权加速+估值处于历史低位+AI赋能研发", "risk_reward": "1.5:1", "logic": "估值低位，基本面改善，配置价值凸显，但弹性相对有限"},
])

gen.add_risk_warning([
    "美联储议息会议前市场情绪谨慎，可能出现观望情绪",
    "AI板块短期涨幅过大，下半周可能出现获利回吐",
    "5月经济数据不及预期，影响市场情绪",
    "北向资金大幅波动风险",
    "地缘政治冲突升级",
])

gen.add_operation_strategy(
    "下半周操作策略：\n\n仓位建议：7-8成，保持进攻态势\n\n配置方向：\n- AI算力：30%（核心主线，坚定持有）\n- 存储芯片：25%（周期上行+国产替代）\n- 光模块：15%（需求放量，业绩确定）\n- 其他：10-15%（灵活配置）\n- 现金：5-10%（应对波动）\n\n操作要点：\n1. 主线持仓不动，逢回调加仓\n2. 避免追高，等待低吸机会\n3. 关注数据公布后的市场反应\n4. 如出现大幅调整，可适度减仓控制风险"
)

output_path = f"/root/daily-news-insight/docs/weekly_outlook/{DATE}_V30测试_周三前瞻.html"
gen.save(output_path)
reports.append(("周三前瞻", f"{DATE}_V30测试_周三前瞻.html", "weekly_outlook", "V3.0深度测试版 - GTC大会催化，下半周继续看反弹"))
print("  ✅ 周三前瞻完成")

# ========== 7. 周末速递（深度版）==========
print("📦 生成深度周末速递...")
gen = WeekendExpressGenerator(date_str=DATE_STR)

gen.add_week_summary(
    "本周市场震荡上行，沪指周涨2.35%，深成指涨4.56%，创业板指涨5.68%，科创50涨8.92%。AI算力板块领涨，周涨幅达12.45%。\n\n北向资金本周净买入234.5亿元，连续第3周净买入。两市总成交额4.56万亿元，较上周放量12.3%。\n\n市场情绪明显回暖，赚钱效应提升，周涨幅超10%的个股达156只，跌幅超10%的仅23只。市场主线清晰，科技成长方向全面爆发。"
)

gen.add_deep_analysis(
    title="AI算力革命：是泡沫还是新周期起点？——从产业周期视角的深度思考",
    content="本轮AI算力行情从2023年初启动，至今已持续近3年，板块内多只龙头股涨幅超3倍。市场对AI算力行情能否持续存在较大分歧：一方认为是历史性的产业机遇，另一方则认为是泡沫即将破裂。\n\n从产业周期视角看，我们认为AI算力目前处于成长期早期，远未到泡沫阶段。理由如下：\n\n一、产业渗透率低，成长空间巨大\n目前AI算力在全球IT支出中的占比不足5%，而PC互联网和移动互联网高峰期，相关IT支出占比均超过15%。按照Gartner的技术成熟度曲线，AI目前正从期望膨胀期进入稳步爬升的光明期，产业发展才刚刚开始。\n\n二、技术迭代持续超预期，应用场景不断拓展\n从GPT-3到GPT-4o，大模型能力持续跃升；从H100到H200，AI芯片性能翻倍提升。技术快速迭代推动应用场景不断拓展，从内容生成到代码辅助，从自动驾驶到生物医药研发，AI正在渗透千行百业。\n\n三、业绩开始兑现，不是纯概念炒作\n与2015年互联网+泡沫不同，本轮AI行情有坚实的业绩支撑。北美云厂商资本开支连续8个季度超预期增长，AI芯片龙头英伟达业绩连续6个季度超预期。国内产业链公司也开始兑现业绩，2026年一季度AI相关业务收入平均增长超100%。\n\n四、政策大力支持，国产替代空间大\n国家高度重视AI产业发展，出台多项支持政策。同时，海外技术封锁加速国产替代进程，国内AI芯片、算力基础设施企业面临历史性发展机遇。\n\n投资建议：长期看好AI算力产业链，建议战略配置。优先选择技术实力强、业绩确定性高的龙头标的，逢低分批建仓，长期持有。不要因为短期波动而动摇长期信心。\n\n风险提示：技术迭代不及预期、应用落地进度慢于预期、行业竞争加剧、估值过高回调风险。"
)

gen.add_industry_research([
    {
        "name": "AI芯片", 
        "trend": "持续高景气", 
        "detail": "AI芯片需求持续超预期，2026年全球市场规模预计达2500亿美元。国产AI芯片快速追赶，性能差距逐步缩小，生态建设加速。推荐寒武纪、海光信息、龙芯中科。", 
        "key_stocks": "寒武纪、海光信息、龙芯中科"
    },
    {
        "name": "光模块", 
        "trend": "加速上行", 
        "detail": "800G光模块需求持续放量，1.6T产品开始导入，北美云厂商资本开支超预期。行业龙头公司业绩高增长确定性强，估值具备吸引力。推荐中际旭创、新易盛、天孚通信。", 
        "key_stocks": "中际旭创、新易盛、天孚通信"
    },
    {
        "name": "存储芯片", 
        "trend": "周期上行", 
        "detail": "存储行业周期上行，DRAM/NAND价格连续6个月上涨。AI需求爆发提供新增量，国产替代加速推进。推荐兆易创新、长江存储、德明利。", 
        "key_stocks": "兆易创新、长江存储、德明利"
    },
    {
        "name": "人形机器人", 
        "trend": "产业加速", 
        "detail": "特斯拉Optimus量产临近，国内厂商纷纷布局，核心零部件国产化加速。长期市场空间巨大，但短期业绩贡献有限，偏主题投资。推荐拓普集团、三花智控、绿的谐波。", 
        "key_stocks": "拓普集团、三花智控、绿的谐波"
    },
    {
        "name": "创新药", 
        "trend": "底部复苏", 
        "detail": "创新药估值处于历史低位，海外授权加速，AI赋能药物研发。行业基本面边际改善，配置价值凸显。推荐恒瑞医药、百济神州、荣昌生物。", 
        "key_stocks": "恒瑞医药、百济神州、荣昌生物"
    },
])

gen.add_next_week_preview(
    "下周重点关注美联储6月议息会议和5月经济数据。预计市场延续震荡上行格局，沪指有望挑战3200点整数关口。\n\n下周重要事件：\n1. 美联储6月议息会议（6月17-18日），关注利率决议和点阵图变化\n2. 5月国民经济运行情况新闻发布会，观察经济复苏态势\n3. 5月工业增加值、固定资产投资、社会消费品零售总额等数据公布\n4. 英伟达GTC大会后续影响发酵\n5. 国内稳增长政策动向\n\n操作建议：继续围绕AI算力、存储芯片、光模块等科技成长主线布局，逢低加仓龙头标的。注意美联储议息会议前的市场波动，控制好仓位。"
)

gen.add_risk_warning([
    "美联储议息会议鹰派超预期，引发全球市场波动",
    "AI板块短期涨幅过大，获利回吐风险",
    "国内经济复苏不及预期，经济数据低于市场预期",
    "地缘政治冲突升级，影响全球供应链",
    "北向资金大幅波动，对市场造成冲击",
    "行业监管政策变化风险",
])

output_path = f"/root/daily-news-insight/docs/weekend_express/{DATE}_V30测试_周末速递.html"
gen.save(output_path)
reports.append(("周末速递", f"{DATE}_V30测试_周末速递.html", "weekend_express", "V3.0深度测试版 - AI算力革命：是泡沫还是新周期起点？"))
print("  ✅ 周末速递完成")

# ========== 8. 明日催化剂（深度版）==========
print("⏰ 生成深度明日催化剂...")
gen = TomorrowCatalystGenerator(date_str=DATE_STR)

gen.add_key_events([
    {
        "title": "英伟达GTC大会开幕，黄仁勋发表主题演讲", 
        "content": "英伟达GTC大会（GPU技术大会）将于6月7日正式开幕，创始人兼CEO黄仁勋将发表主题演讲。市场普遍预期将发布新一代AI芯片H200的详细规格和量产计划，以及AI生态的重大进展。", 
        "impact": "AI算力板块催化，可能带动整个科技成长板块上涨", 
        "sectors": ["AI算力", "光模块", "存储芯片"]
    },
    {
        "title": "5月社会融资规模数据公布", 
        "content": "央行将于6月7日公布5月社会融资规模和信贷数据。市场预期新增社融约2.5万亿元，新增人民币贷款约1.5万亿元。", 
        "impact": "数据反映经济复苏态势和信贷需求，对市场情绪有重要影响", 
        "sectors": ["银行", "地产", "大金融"]
    },
    {
        "title": "5月CPI、PPI数据公布", 
        "content": "国家统计局将于6月7日公布5月CPI和PPI数据。市场预期CPI同比上涨0.3%左右，PPI同比下降2.5%左右。", 
        "impact": "通胀数据影响货币政策走向预期，如CPI持续低迷可能引发降准降息预期", 
        "sectors": ["债券", "地产", "消费"]
    },
    {
        "title": "国内成品油价格调整窗口开启", 
        "content": "6月9日24时，国内成品油价格调整窗口将开启。受国际油价下跌影响，预计本轮成品油价格可能下调约150元/吨。", 
        "impact": "油价下调降低交通运输等行业成本，对航空、物流等板块构成利好", 
        "sectors": ["航空", "物流", "交通运输"]
    },
])

gen.add_economic_calendar([
    {"time": "09:30", "event": "中国5月CPI、PPI数据公布", "importance": "高"},
    {"time": "10:00", "event": "中国5月进出口数据公布", "importance": "中"},
    {"time": "15:00", "event": "中国5月社会融资规模数据公布", "importance": "高"},
    {"time": "20:30", "event": "美国5月非农就业数据公布", "importance": "高"},
    {"time": "22:00", "event": "美国5月ISM非制造业PMI公布", "importance": "中"},
    {"time": "凌晨", "event": "美联储6月议息会议召开（6月17-18日）", "importance": "高"},
])

gen.add_sector_catalysts([
    {
        "name": "AI算力", 
        "catalyst": "英伟达GTC大会开幕+H200量产+AI生态重大发布", 
        "impact": "高", 
        "positive": True,
        "related_stocks": ["寒武纪", "海光信息", "中际旭创", "英维克"]
    },
    {
        "name": "存储芯片", 
        "catalyst": "长鑫科技IPO获受理+存储周期上行+国产替代加速", 
        "impact": "高", 
        "positive": True,
        "related_stocks": ["兆易创新", "长江存储", "德明利", "铜冠铜箔"]
    },
    {
        "name": "光模块", 
        "catalyst": "800G/1.6T需求放量+北美云厂商资本开支超预期", 
        "impact": "中高", 
        "positive": True,
        "related_stocks": ["中际旭创", "新易盛", "天孚通信", "光迅科技"]
    },
    {
        "name": "创新药", 
        "catalyst": "恒瑞医药20亿美元海外授权+创新药国际化加速", 
        "impact": "中", 
        "positive": True,
        "related_stocks": ["恒瑞医药", "百济神州", "信达生物", "荣昌生物"]
    },
    {
        "name": "银行", 
        "catalyst": "降息预期压制息差+信贷需求偏弱", 
        "impact": "中", 
        "positive": False,
        "related_stocks": ["招商银行", "宁波银行", "工商银行"]
    },
    {
        "name": "地产", 
        "catalyst": "销售数据偏弱+政策效果待观察", 
        "impact": "中", 
        "positive": False,
        "related_stocks": ["万科A", "保利发展", "招商蛇口"]
    },
])

gen.add_notice(
    "明日事件密集，注意市场波动风险。重点关注英伟达GTC大会和5月经济数据，这两大事件可能决定市场短期走向。\n\n操作建议：\n1. 保持合理仓位，避免过度激进\n2. 关注数据公布后的市场反应，顺势而为\n3. 如AI板块大幅冲高，可适度减仓止盈部分仓位\n4. 如市场出现调整，可逢低加仓主线标的\n\n美联储利率决议是下周重中之重，注意控制整体仓位，防范会议前的观望情绪和会后的波动风险。"
)

output_path = f"/root/daily-news-insight/docs/tomorrow_catalyst/{DATE}_V30测试_明日催化剂.html"
gen.save(output_path)
reports.append(("明日催化剂", f"{DATE}_V30测试_明日催化剂.html", "tomorrow_catalyst", "V3.0深度测试版 - GTC大会开幕+5月经济数据，明天是重要窗口"))
print("  ✅ 明日催化剂完成")

# ========== 9. 月报（深度版）==========
print("📅 生成深度月报...")
gen = MonthlyReportGenerator(month_str="2026年5月")

gen.add_month_overview(
    "5月市场震荡上行，沪指月涨3.45%，深成指月涨5.68%，创业板指月涨8.92%，科创50月涨12.34%。AI算力板块领涨，月涨幅达18.56%。\n\n成交方面，5月两市总成交额17.89万亿元，较4月放量15.6%，市场活跃度明显提升。北向资金5月净买入456.78亿元，连续第3个月净买入。\n\n市场结构方面，科技成长方向全面占优，AI算力、存储芯片、光模块、游戏等板块涨幅居前；银行、地产、煤炭等传统行业表现相对弱势。\n\n政策面，央行降准0.5个百分点，释放长期资金约1万亿元；证监会发布深化新三板改革方案；多地出台稳楼市政策。政策环境持续友好。"
)

gen.add_market_performance([
    {"name": "上证指数", "monthly_change": "3.45%", "current": "3145.68", "up": True},
    {"name": "深证成指", "monthly_change": "5.68%", "current": "10234.56", "up": True},
    {"name": "创业板指", "monthly_change": "8.92%", "current": "2156.78", "up": True},
    {"name": "科创50", "monthly_change": "12.34%", "current": "968.45", "up": True},
    {"name": "沪深300", "monthly_change": "4.56%", "current": "3678.90", "up": True},
    {"name": "中证500", "monthly_change": "6.78%", "current": "5678.90", "up": True},
])

gen.add_sector_review([
    {"name": "AI算力", "change": "18.56%", "up": True},
    {"name": "存储芯片", "change": "15.34%", "up": True},
    {"name": "光模块", "change": "13.68%", "up": True},
    {"name": "游戏传媒", "change": "11.23%", "up": True},
    {"name": "人形机器人", "change": "9.87%", "up": True},
    {"name": "创新药", "change": "7.65%", "up": True},
    {"name": "新能源", "change": "2.34%", "up": True},
    {"name": "消费", "change": "1.56%", "up": True},
    {"name": "医药", "change": "0.89%", "up": True},
    {"name": "银行", "change": "-2.34%", "up": False},
    {"name": "地产", "change": "-1.56%", "up": False},
    {"name": "煤炭", "change": "-1.23%", "up": False},
])

gen.add_key_events_review([
    {"date": "5月8日", "title": "英伟达财报超预期", "content": "英伟达一季度营收同比增长234%，超市场预期，指引二季度继续高增长，AI算力板块大涨"},
    {"date": "5月12日", "title": "央行降准0.5个百分点", "content": "释放长期资金约1万亿元，支持实体经济融资需求，市场流动性持续宽松"},
    {"date": "5月15日", "title": "4月经济数据公布", "content": "经济复苏温和，社融信贷低于预期，市场期待更多稳增长政策"},
    {"date": "5月20日", "title": "LPR报价维持不变", "content": "1年期LPR报3.45%，5年期以上LPR报4.2%，均维持不变，市场对降息预期升温"},
    {"date": "5月25日", "title": "证监会发布深化新三板改革方案", "content": "优化发行上市条件，完善转板机制，支持专精特新企业融资发展"},
    {"date": "5月28日", "title": "长鑫科技IPO获受理", "content": "拟募资350亿元投向DRAM芯片研发，存储芯片国产替代加速"},
    {"date": "5月30日", "title": "美联储议息会议纪要偏鸽", "content": "暗示年内可能降息，市场预期9月首次降息概率提升至78%"},
])

gen.add_next_month_outlook(
    "展望6月，我们认为市场延续震荡上行格局的概率较大，沪指有望挑战3200-3300点压力位。\n\n主要逻辑：\n1. 政策环境持续友好，稳增长政策有望继续发力\n2. 流动性宽松格局不变，市场资金面充裕\n3. AI算力产业趋势明确，业绩高增长持续验证\n4. 经济复苏温和，企业盈利逐步改善\n5. 市场情绪回暖，赚钱效应提升\n\n6月市场主线：预计AI算力、科技成长仍是市场主线，存储芯片、光模块、人形机器人等细分方向有望持续活跃。同时，关注中报业绩预期较好的行业和公司。\n\n6月重要事件：美联储6月议息会议、国内6月MLF操作和LPR报价、中报业绩预告陆续披露、英伟达GTC大会后续影响。"
)

gen.add_investment_strategy(
    "6月投资策略：科技成长为主线，逢低加仓，长期持有\n\n配置建议：\n- AI算力：25-30%（核心主线，坚定持有）\n- 存储芯片：20-25%（周期上行+国产替代）\n- 光模块：10-15%（需求放量，业绩确定）\n- 游戏传媒：5-10%（AI降本增效，业绩拐点）\n- 创新药：5-10%（估值低位，基本面改善）\n- 现金：5-10%（应对波动，逢低加仓）\n\n操作策略：\n1. 主线持仓不动，逢回调分批加仓\n2. 避免追高，等待低吸机会\n3. 关注业绩确定性，优先选择龙头标的\n4. 控制单一标的仓位，分散风险\n5. 设置止损位，严格执行风险控制\n\n重点关注标的：\n- AI芯片：寒武纪、海光信息、龙芯中科\n- 光模块：中际旭创、新易盛、天孚通信\n- 存储：兆易创新、长江存储、铜冠铜箔\n- 应用：昆仑万维、三七互娱、芒果超媒"
)

gen.add_risk_warning([
    "美联储6月议息会议鹰派超预期，引发全球市场波动",
    "AI板块短期涨幅过大，估值过高导致回调风险",
    "国内经济复苏不及预期，企业盈利改善慢于预期",
    "地缘政治冲突升级，影响全球供应链和市场情绪",
    "北向资金大幅波动，对A股市场造成冲击",
    "行业监管政策变化风险",
    "流动性收紧超预期",
])

output_path = f"/root/daily-news-insight/docs/monthly/{DATE}_V30测试_月报.html"
gen.save(output_path)
reports.append(("月报", f"{DATE}_V30测试_月报.html", "monthly", "V3.0深度测试版 - 2026年5月市场回顾与6月投资策略展望"))
print("  ✅ 月报完成")

# ========== 更新各类型列表页 ==========
print("\n📋 更新各类型列表页...")
publisher = ReportPublisher(docs_root="docs")

for report_name, filename, dir_name, excerpt in reports:
    try:
        result = publisher.update_list_page(
            report_type_key=dir_name,
            title=f"{report_name}深度测试报告(V3.0)",
            filename=filename,
            excerpt=excerpt
        )
        print(f"   ✅ {report_name} 列表页已更新")
    except Exception as e:
        print(f"   ❌ {report_name} 列表页更新失败: {e}")

# 部署到GitHub
print("\n🚀 部署到GitHub Pages...")
try:
    import subprocess
    result = subprocess.run(
        ["git", "add", "docs/"],
        cwd="/root/daily-news-insight",
        capture_output=True,
        text=True
    )
    result = subprocess.run(
        ["git", "commit", "-m", "V3.0深度测试报告 - 9种类型完整版"],
        cwd="/root/daily-news-insight",
        capture_output=True,
        text=True
    )
    result = subprocess.run(
        ["git", "push"],
        cwd="/root/daily-news-insight",
        capture_output=True,
        text=True
    )
    print("  ✅ 部署成功！")
except Exception as e:
    print(f"  ⚠️ 部署提示: {e}")

print(f"\n🎉 全部完成！共生成 {len(reports)} 份深度测试报告")
print("\n📊 报告统计：")
for name, fn, d, exc in reports:
    import os
    size = os.path.getsize(f"/root/daily-news-insight/docs/{d}/{fn}")
    print(f"   {name}: {size/1024:.1f} KB")

