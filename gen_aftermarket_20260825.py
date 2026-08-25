#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
盘后速递生成驱动脚本 - 2026-08-25
从JSON数据文件读取内容，调用V3.0生成器生成报告
"""
import sys
import os
import json

sys.path.insert(0, '/root/daily-news-insight/v3')
os.chdir('/root/daily-news-insight')

from v3.generators.aftermarket import AftermarketGenerator

# 读取数据
print("正在加载数据...")
with open('report_data_0825.json', 'r', encoding='utf-8') as f:
    basic = json.load(f)
with open('holdings_0825.json', 'r', encoding='utf-8') as f:
    holdings = json.load(f)
with open('longhubang_0825.json', 'r', encoding='utf-8') as f:
    lhb = json.load(f)
with open('news_0825.json', 'r', encoding='utf-8') as f:
    news = json.load(f)
with open('extra_data_0825.json', 'r', encoding='utf-8') as f:
    extra = json.load(f)

print("数据加载完成，开始生成报告...")

# 初始化生成器
gen = AftermarketGenerator(
    date_str=basic['date_str'],
    subtitle=basic['subtitle']
)

# 1. 今日核心亮点
gen.add_today_highlight(basic['highlight'])
print("  + 今日核心亮点")

# 2. 市场收盘总结
gen.add_market_summary(
    indices=basic['indices'],
    volume=basic['volume'],
    northbound=basic['northbound']
)
print("  + 市场收盘总结")

# 3. 情绪温度计
gen.add_sentiment_thermometer(
    temperature=basic['sentiment_temp'],
    volume=basic['volume'],
    up_count=basic['up_count'],
    down_count=basic['down_count'],
    limit_up_count=basic['limit_up_count']
)
print("  + 情绪温度计")

# 4. 板块涨跌幅排行
gen.add_sector_performance(
    up_sectors=extra['up_sectors'],
    down_sectors=extra['down_sectors']
)
print("  + 板块涨跌幅排行")

# 5. 盘面深度解读
gen.add_market_deep_analysis(
    strong_sectors=extra['strong_sectors'],
    weak_sectors=extra['weak_sectors'],
    core_view=extra['core_view']
)
print("  + 盘面深度解读")

# 6. 持仓股深度诊断
gen.add_holdings_tracking(holdings)
print("  + 持仓股深度诊断 ({}只)".format(len(holdings)))

# 7. 龙虎榜深度解读
gen.add_dragon_tiger_list(lhb)
print("  + 龙虎榜深度解读 ({}只)".format(len(lhb)))

# 8. 晚间重要新闻
gen.add_evening_news(news)
print("  + 晚间重要新闻 ({}条)".format(len(news)))

# 9. 业绩预告
gen.add_earnings_forecast()
print("  + 业绩预告")

# 10. 重点关注标的

# 11. 明日操作策略
gen.add_trading_plan(extra['trading_plan'])
print("  + 明日操作策略")

# 12. 明日预测
gen.add_tomorrow_prediction(extra['predictions'])
print("  + 明日预测 ({}项)".format(len(extra['predictions'])))

# 13. 风险提示
gen.add_risk_warning(extra['risks'])
print("  + 风险提示 ({}条)".format(len(extra['risks'])))

# 发布
print("\n正在生成报告HTML...")
result = gen.publish(
    title="盘后速递",
    report_type="aftermarket",
    auto_deploy=True
)
print("发布结果:", result)
print("\n报告生成完成！")
