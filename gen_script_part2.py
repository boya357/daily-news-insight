#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""盘后速递生成脚本 - 2026-11-23"""
import sys, os
sys.path.insert(0, "v3")
os.chdir("/root/daily-news-insight")

from v3.generators.aftermarket import AftermarketGenerator
from v3.components.layout import Section

gen = AftermarketGenerator(date_str="20261123", subtitle="2026.11.23 · 盘后速递")

# 1. 今日核心亮点
gen.add_today_highlight(
    "创业板指暴涨3.08%领跑两市，华为机器人/物理AI/数字媒体板块全线爆发，"
    "风华高科(000636)涨停登龙虎榜，深股通+机构净买1.8亿。"
    "科技成长主线全面回暖，7只持仓6红1绿（长电科技仅微涨0.22%跑输），"
    "铜冠铜箔+3.53%、华海诚科+3.89%、雅克科技+2.28%集体反弹。"
    "深强沪弱格局明显，沪指+0.15% vs 创业板+3.08%，两市成交约1.55万亿放量。"
)

# 2. 市场收盘总结
gen.add_market_summary(
    indices=[
        {"name": "上证指数", "value": "3538.95", "change": "+5.16 (+0.15%)", "up": True, "icon": "trending_up"},
        {"name": "深证成指", "value": "10454.37", "change": "+197.98 (+1.93%)", "up": True, "icon": "trending_up"},
        {"name": "创业板指", "value": "2280.20", "change": "+68.07 (+3.08%)", "up": True, "icon": "trending_up"},
        {"name": "科创50", "value": "1227.89", "change": "-3.20 (-0.26%)", "up": False, "icon": "trending_down"},
    ],
    volume="约1.55万亿（放量）",
    northbound="净流入约68亿（估算）"
)

# 3. 情绪温度计
gen.add_sentiment_thermometer(
    temperature=72,
    volume="1.55万亿",
    up_count="3200+",
    down_count="1800+",
    limit_up_count="85"
)

# 4. 板块涨跌幅排行
gen.add_sector_performance(
    up_sectors=[
        {"name": "华为机器人", "change": "+10.98%"},
        {"name": "空心杯电机", "change": "+10.44%"},
        {"name": "电子鼻", "change": "+10.20%"},
        {"name": "物理AI", "change": "+9.62%"},
        {"name": "机器人执行器", "change": "+9.60%"},
        {"name": "数字媒体", "change": "+9.18%"},
        {"name": "影视院线", "change": "+6.91%"},
        {"name": "电机II", "change": "+6.78%"},
        {"name": "自动化设备", "change": "+6.60%"},
        {"name": "贵金属", "change": "+5.25%"},
    ],
    down_sectors=[
        {"name": "保险II", "change": "-2.86%"},
        {"name": "白酒II", "change": "-1.98%"},
        {"name": "国有大型银行", "change": "-1.20%"},
        {"name": "电力", "change": "-0.97%"},
        {"name": "银行", "change": "-0.80%"},
    ]
)
