#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
盘后速递生成脚本 - 2026-08-24
使用 V3.0 AftermarketGenerator
"""
import sys
import os

sys.path.insert(0, '/root/daily-news-insight/v3')
os.chdir('/root/daily-news-insight')

from v3.generators.aftermarket import AftermarketGenerator

gen = AftermarketGenerator(
    date_str="20260824",
    subtitle="2026.08.24 · 盘后速递"
)

# 1. 今日核心亮点
gen.add_today_highlight(
    "A股呈现沪指抗跌、双创重挫的分化格局，沪指跌0.59%报3882.01点，"
    "深成指跌2.13%报13794.29点，创业板指跌3.21%报3431.89点，科创50跌3.10%报1602.34点。"
    "两市成交额2.01万亿放量1282亿，1460家上涨、3965家下跌，涨停48家、跌停43家，赚钱效应仅26.9%。"
    "贵金属/煤炭/银行等防御板块逆势走强，AI算力/光通信/半导体等科技成长全线重挫。"
    "持仓股分化明显：英维克+1.16%逆势反弹、铜冠铜箔-3.21%探底回升、雅克科技+1.51%V型反转、*ST建艺-4.72%再创调整新低。"
    "龙虎榜机构净卖出9.44亿、北向净流出约47.82亿、游资净买入16.07亿，机构继续减仓科技成长。"
    "长江存储科创板IPO获受理拟募资330亿创纪录，美光HBM专家警示AI内存墙持续加剧，"
    "英伟达财报（8/27）成算力方向下一个关键锚点。"
)

# 2. 市场收盘总结
gen.add_market_summary(
    indices=[
        {"name": "上证指数", "value": "3882.01", "change": "-0.59%", "up": False, "icon": "trending_down"},
        {"name": "深证成指", "value": "13794.29", "change": "-2.13%", "up": False, "icon": "trending_down"},
        {"name": "创业板指", "value": "3431.89", "change": "-3.21%", "up": False, "icon": "trending_down"},
        {"name": "科创50", "value": "1602.34", "change": "-3.10%", "up": False, "icon": "trending_down"},
    ],
    volume="2.01万亿",
    northbound="净流出约47.82亿"
)

# 3. 情绪温度计
gen.add_sentiment_thermometer(
    temperature=22,
    volume="2.01万亿",
    up_count="1460家",
    down_count="3965家",
    limit_up_count="48只"
)

# 4. 板块涨跌幅排行
gen.add_sector_performance(
    up_sectors=[
        {"name": "贵金属/黄金", "change": "+4.82%"},
        {"name": "煤炭开采", "change": "+2.15%"},
        {"name": "银行", "change": "+0.30%"},
        {"name": "保险", "change": "+1.52%"},
        {"name": "种植业/农业", "change": "+1.85%"},
    ],
    down_sectors=[
        {"name": "CPO/光模块", "change": "-5.21%"},
        {"name": "通信设备", "change": "-4.83%"},
        {"name": "半导体/元件", "change": "-4.18%"},
        {"name": "CRO/医药生物", "change": "-3.85%"},
        {"name": "算力/AI硬件", "change": "-3.56%"},
        {"name": "玻璃玻纤", "change": "-5.30%"},
        {"name": "人形机器人", "change": "-2.97%"},
        {"name": "存储芯片", "change": "-2.35%"},
    ]
)

print('脚本初始化完成')
