#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
盘后速递 - 2026年9月11日
V3.0 统一标准
"""
import sys, os
sys.path.insert(0, 'v3')
os.chdir('/root/daily-news-insight')

from v3.generators.aftermarket import AftermarketGenerator

# 创建生成器
gen = AftermarketGenerator(date_str="20260911", subtitle="2026.09.11 · 盘后速递")

# ========== 1. 今日核心亮点 ==========
gen.add_today_highlight(
    "沪指失守3900点放量下跌1.18%，两市成交1.97万亿创近期天量，643只上涨4870只下跌呈普跌格局。"
    "PCB/MLCC/通信设备逆势走强，风华高科涨停成交近百亿，金安国纪龙虎榜三日净买8.12亿居首。"
    "北向资金逆势净买入7.48亿元，内资主力大幅出逃超520亿，防御属性板块成资金避风港。"
)

# ========== 2. 市场收盘总结 ==========
gen.add_market_summary(
    indices=[
        {"name": "上证指数", "value": "3888.11", "change": "-1.18%", "icon": "trending_down", "up": False},
        {"name": "深证成指", "value": "13471.26", "change": "-1.08%", "icon": "trending_down", "up": False},
        {"name": "创业板指", "value": "3322.04", "change": "-0.49%", "icon": "trending_down", "up": False},
        {"name": "科创50", "value": "1553.39", "change": "-1.01%", "icon": "trending_down", "up": False},
    ],
    volume="1.97万亿",
    northbound="净买入7.48亿"
)

# ========== 3. 情绪温度计 ==========
gen.add_sentiment_thermometer(
    temperature=22,
    volume="1.97万亿",
    up_count="643",
    down_count="4870",
    limit_up_count="40"
)

# ========== 4. 板块涨跌幅排行 ==========
gen.add_sector_performance(
    up_sectors=[
        {"name": "覆铜板", "change": "+4.31%"},
        {"name": "地面兵装", "change": "+4.44%"},
        {"name": "玻璃玻纤", "change": "+2.63%"},
        {"name": "通信设备", "change": "+1.66%"},
        {"name": "元件/MLCC", "change": "+1.80%"},
        {"name": "陶瓷基板", "change": "+1.74%"},
        {"name": "中兵系", "change": "+1.61%"},
        {"name": "风电设备", "change": "+0.97%"},
        {"name": "国有银行", "change": "+0.41%"},
        {"name": "电子布", "change": "+1.73%"},
    ],
    down_sectors=[
        {"name": "有色金属", "change": "-3.98%"},
        {"name": "基础化工", "change": "-2.98%"},
        {"name": "房地产", "change": "-2.93%"},
        {"name": "商贸零售", "change": "-2.78%"},
        {"name": "农业/农牧", "change": "-3.20%"},
    ]
)

print("步骤1-4完成")
