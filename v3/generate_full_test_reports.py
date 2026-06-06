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
from v3.generators.list_page import ListPageGenerator

DATE = "20260606"
DATE_STR = "2026年6月6日"
reports = []

# 1. 日报
print("生成日报...")
gen = DailyReportGenerator(date_str=DATE_STR, weekday="周五")
gen.add_focus_point("英伟达H200芯片量产，AI算力产业链持续爆发")
gen.add_overseas_market(
    indices=[
        {"name": "道琼斯", "value": "39876.54", "change": "+0.52%", "up": True},
        {"name": "纳斯达克", "value": "18234.56", "change": "+1.23%", "up": True},
    ],
    key_events=[
        {"tag": "重磅", "title": "美联储官员放鸽", "content": "市场预期年内降息2次"},
    ]
)
gen.add_import_news([
    {"tag": "要闻", "importance": "high", "title": "英伟达H200芯片正式量产", "content": "HBM容量141GB，带宽提升2.3倍。", "source": "财联社"},
])
gen.add_sector_analysis([
    {"name": "AI算力", "performance": "大涨4.25%", "rating": "强烈推荐", "stocks": ["寒武纪", "中际旭创"], "logic": "英伟达H200量产刺激"},
])
gen.add_holdings_tracking([
    {"name": "英维克", "code": "002837", "price": "68.32", "change": "-5.23%", "up": False, "comment": "跌破止损，观察中"},
])
gen.add_risk_warning(["美联储6月议息会议可能释放鹰派信号"])
gen.add_daily_summary("今日市场整体震荡上行，AI算力板块领涨，成交额9876亿。")
gen.add_tomorrow_plan("重点关注英伟达GTC大会催化，逢低布局AI算力龙头。")
output_path = f"/root/daily-news-insight/docs/daily/{DATE}_V30测试_日报.html"
gen.save(output_path)
reports.append(("日报", f"{DATE}_V30测试_日报.html", "daily"))
print("  ✅ 完成")

# 2. 盘中快报
print("生成盘中快报...")
gen = IntradayGenerator(date_str=DATE_STR)
gen.add_market_overview(
    indices=[
        {"name": "上证指数", "value": "3120.45", "change": "+0.56%", "up": True},
        {"name": "深证成指", "value": "10156.78", "change": "+0.89%", "up": True},
    ],
    market_status="震荡上行"
)
gen.add_hot_topics([
    {"tag": "AI", "title": "英伟达H200量产", "content": "AI算力需求持续爆发", "hot": True},
])
gen.add_decline_sectors([
    {"name": "银行", "change": "-0.65%", "reason": "降息预期压制息差"},
])
gen.add_holdings_tracking([
    {"name": "英维克", "code": "002837", "price": "68.32", "change": "-2.15%", "up": False, "comment": "弱势震荡"},
])
gen.add_trading_strategy("早盘AI算力板块异动，可逢低关注存储芯片方向龙头。")
gen.add_risk_warning(["午后可能出现获利回吐"])
gen.add_summary("上午市场震荡上行，AI算力领涨，成交额4567亿。")
output_path = f"/root/daily-news-insight/docs/intraday/{DATE}_V30测试_盘中快报.html"
gen.save(output_path)
reports.append(("盘中快报", f"{DATE}_V30测试_盘中快报.html", "intraday"))
print("  ✅ 完成")

# 3. 盘后速递
print("生成盘后速递...")
gen = AftermarketGenerator(date_str=DATE_STR)
gen.add_market_summary(
    indices=[
        {"name": "上证指数", "value": "3145.68", "change": "+0.85%", "up": True},
        {"name": "深证成指", "value": "10234.56", "change": "+1.23%", "up": True},
    ],
    volume="9876亿"
)
gen.add_sector_performance(
    top_sectors=[
        {"name": "AI算力", "change": "4.25%", "reason": "英伟达H200量产"},
    ],
    bottom_sectors=[
        {"name": "银行", "change": "-0.85%", "reason": "息差收窄预期"},
    ]
)
gen.add_hot_topics([
    {"topic": "英伟达H200芯片", "impact": "AI算力产业链全面受益", "related_stocks": "寒武纪、中际旭创"},
])
gen.add_holdings_review([
    {"name": "英维克", "code": "002837", "change": "-5.23%", "performance": "弱于大盘", "action": "继续观察"},
])
gen.add_tomorrow_outlook("预计明日市场延续震荡上行格局，重点关注英伟达GTC大会。")
gen.add_risk_warning(["美联储议息会议临近"])
gen.add_operation_plan("继续持有主线标的，逢低加仓存储芯片方向。")
output_path = f"/root/daily-news-insight/docs/aftermarket/{DATE}_V30测试_盘后速递.html"
gen.save(output_path)
reports.append(("盘后速递", f"{DATE}_V30测试_盘后速递.html", "aftermarket"))
print("  ✅ 完成")

# 4. 周复盘
print("生成周复盘...")
gen = WeeklyReviewGenerator(week_label="第23周", date_range="6月2日-6月6日")
gen.add_week_summary("本周市场震荡上行，沪指周涨2.35%，创业板指周涨5.68%。AI算力板块领涨。")
gen.add_index_performance([
    {"name": "上证指数", "change": "2.35%", "current": "3145.68", "high": "3168.50", "low": "3089.20", "volume": "4.56万亿"},
])
gen.add_sector_review(
    top_sectors=[
        {"name": "AI算力", "change": "12.45%", "logic": "英伟达H200发布"},
    ],
    bottom_sectors=[
        {"name": "银行", "change": "-2.34%", "logic": "降息预期压制息差"},
    ]
)
gen.add_hot_topics_review([
    {"topic": "英伟达H200芯片", "impact": "AI算力产业链全面爆发"},
])
gen.add_important_events([
    {"date": "6月2日", "event": "英伟达发布H200 GPU", "impact": "AI算力板块大涨"},
])
gen.add_next_week_outlook(
    outlook="预计下周市场延续震荡上行，沪指有望挑战3200点。",
    key_points=["美联储议息会议", "5月CPI数据"]
)
gen.add_risk_warning(["美联储鹰派表态"])
gen.add_operation_plan("继续围绕AI算力、存储芯片布局，逢低加仓龙头。")
output_path = f"/root/daily-news-insight/docs/weekly_review/{DATE}_V30测试_周复盘.html"
gen.save(output_path)
reports.append(("周复盘", f"{DATE}_V30测试_周复盘.html", "weekly_review"))
print("  ✅ 完成")

# 5. S级催化
print("生成S级催化...")
gen = SLevelCatalystGenerator(title="S级催化：AI算力全面爆发")
gen.add_catalyst_overview(
    overview="英伟达正式发布H200 GPU，HBM容量提升至141GB，带宽提升2.3倍，将全面推动AI算力升级，带动整个产业链需求爆发。",
    event_date="2026年6月2日",
    impact_level="S级"
)
gen.add_impact_analysis(
    impact="H200芯片发布标志着AI算力进入新阶段，整个产业链将持续受益。",
    dimensions=[
        {"name": "市场空间", "level": 5, "desc": "全球AI芯片市场2026年预计达2500亿美元"},
        {"name": "产业成熟度", "level": 4, "desc": "大模型应用进入规模化落地期"},
    ]
)
gen.add_beneficiary_stocks([
    {"name": "寒武纪", "code": "688256", "logic": "国内AI芯片龙头", "elasticity": "目标涨幅50-80%", "rating": "强烈推荐"},
    {"name": "中际旭创", "code": "300308", "logic": "全球光模块龙头", "elasticity": "目标涨幅30-50%", "rating": "推荐"},
])
gen.add_timeline_analysis([
    {"time": "2023-2024", "title": "概念期", "content": "ChatGPT引爆AI概念", "type": "primary"},
    {"time": "2025-2026", "title": "成长期", "content": "大模型规模化落地", "type": "success"},
    {"time": "2026-2027", "title": "爆发期", "content": "H200量产，AI应用大规模落地", "type": "warning"},
])
gen.add_risk_warning(["AI芯片需求不及预期", "行业竞争加剧", "海外技术封锁风险"])
gen.add_investment_strategy("逢低布局，长期持有。建议配置仓位20-25%。")
output_path = f"/root/daily-news-insight/docs/s级催化扫描/{DATE}_V30测试_S级催化.html"
gen.save(output_path)
reports.append(("S级催化", f"{DATE}_V30测试_S级催化.html", "s级催化扫描"))
print("  ✅ 完成")

# 6. 周三前瞻
print("生成周三前瞻...")
gen = WeeklyOutlookGenerator(date_str=DATE_STR)
gen.add_halfweek_review("本周前半段市场震荡上行，AI算力和存储芯片表现强势。")
gen.add_second_half_outlook("下半周预计延续震荡上行，关注美联储议息会议。")
gen.add_key_events([
    {"date": "6月8日", "event": "美联储议息会议", "importance": "高", "impact": "决定全球流动性走向"},
])
gen.add_opportunity_focus([
    {"sector": "AI算力", "probability": "高", "catalyst": "英伟达GTC大会+H200量产", "risk_reward": "3:1"},
])
gen.add_risk_warning(["美联储鹰派表态", "AI板块获利回吐"])
gen.add_operation_strategy("7-8成仓位，AI算力为主线，搭配存储芯片。")
output_path = f"/root/daily-news-insight/docs/weekly_outlook/{DATE}_V30测试_周三前瞻.html"
gen.save(output_path)
reports.append(("周三前瞻", f"{DATE}_V30测试_周三前瞻.html", "weekly_outlook"))
print("  ✅ 完成")

# 7. 周末速递
print("生成周末速递...")
gen = WeekendExpressGenerator(date_str=DATE_STR)
gen.add_week_summary("本周市场震荡上行，AI算力板块领涨，周涨幅达12.45%。北向资金净流入234.5亿。")
gen.add_deep_analysis(
    title="AI算力革命：是泡沫还是新周期起点？",
    content="本轮AI算力行情持续近一年，板块涨幅巨大。从产业趋势看，AI算力需求是确定性最强的产业趋势之一。虽然短期估值较高，但产业趋势才刚刚开始。\n\n投资建议：长期看好AI算力产业链，分批建仓，逢低加仓，长期持有。"
)
gen.add_industry_research([
    {"name": "AI算力", "trend": "持续高景气", "detail": "AI芯片需求超预期，产业链公司业绩高增长可期。", "key_stocks": "寒武纪、中际旭创"},
])
gen.add_next_week_preview("下周重点关注美联储议息会议和国内经济数据，预计市场延续震荡上行。")
gen.add_risk_warning(["美联储鹰派政策", "AI板块估值过高"])
output_path = f"/root/daily-news-insight/docs/weekend_express/{DATE}_V30测试_周末速递.html"
gen.save(output_path)
reports.append(("周末速递", f"{DATE}_V30测试_周末速递.html", "weekend_express"))
print("  ✅ 完成")

# 8. 明日催化剂
print("生成明日催化剂...")
gen = TomorrowCatalystGenerator(date_str=DATE_STR)
gen.add_key_events([
    {"title": "英伟达GTC大会开幕", "content": "预计发布新一代AI芯片和AI生态进展。", "impact": "AI算力板块催化", "sectors": ["AI算力", "存储芯片"]},
])
gen.add_economic_calendar([
    {"time": "09:30", "event": "中国5月进出口数据", "importance": "高"},
    {"time": "20:30", "event": "美国非农就业数据", "importance": "高"},
])
gen.add_sector_catalysts([
    {"name": "AI算力", "catalyst": "英伟达GTC大会+H200量产", "impact": "高", "positive": True, "related_stocks": ["寒武纪", "中际旭创"]},
])
gen.add_notice("明日事件密集，注意市场波动风险。美联储利率决议是重中之重。")
output_path = f"/root/daily-news-insight/docs/tomorrow_catalyst/{DATE}_V30测试_明日催化剂.html"
gen.save(output_path)
reports.append(("明日催化剂", f"{DATE}_V30测试_明日催化剂.html", "tomorrow_catalyst"))
print("  ✅ 完成")

# 9. 月报
print("生成月报...")
gen = MonthlyReportGenerator(month_str="2026年5月")
gen.add_month_overview("5月市场震荡上行，沪指月涨3.45%，创业板指月涨8.92%。AI算力板块领涨。")
gen.add_market_performance([
    {"name": "上证指数", "monthly_change": "3.45%", "current": "3145.68", "up": True},
    {"name": "深证成指", "monthly_change": "5.68%", "current": "10234.56", "up": True},
])
gen.add_sector_review([
    {"name": "AI算力", "change": "25.6%", "up": True},
    {"name": "光模块", "change": "22.4%", "up": True},
    {"name": "银行", "change": "-4.5%", "up": False},
])
gen.add_key_events_review([
    {"date": "5月8日", "title": "英伟达财报超预期", "content": "营收同比增长234%"},
    {"date": "5月20日", "title": "央行降准0.5个百分点", "content": "释放长期资金约1万亿元"},
])
gen.add_next_month_outlook("预计6月市场延续震荡上行，沪指有望挑战3200-3300点。AI算力、存储芯片仍是主线。")
gen.add_investment_strategy("主线持股，逢低加仓，控制仓位在7-8成。重点配置AI算力和存储芯片龙头。")
gen.add_risk_warning(["美联储鹰派政策", "国内经济复苏不及预期", "地缘政治风险"])
output_path = f"/root/daily-news-insight/docs/monthly/{DATE}_V30测试_月报.html"
gen.save(output_path)
reports.append(("月报", f"{DATE}_V30测试_月报.html", "monthly"))
print("  ✅ 完成")

# 更新所有列表页
print("\n📋 更新各类型列表页...")
for report_name, filename, dir_name in reports:
    try:
        list_gen = ListPageGenerator(report_type=report_name)
        list_page_path = f"/root/daily-news-insight/docs/{dir_name}/index.html"
        list_gen.add_report_entry(
            title=f"{report_name}测试报告(V3.0)",
            date="2026-06-06",
            filename=filename,
            description=f"V3.0系统{report_name}类型完整内容测试报告"
        )
        list_gen.save(list_page_path)
        print(f"   ✅ {report_name} 列表页已更新")
    except Exception as e:
        print(f"   ❌ {report_name} 列表页更新失败: {e}")

print(f"\n🎉 全部完成！共生成 {len(reports)} 份测试报告")
