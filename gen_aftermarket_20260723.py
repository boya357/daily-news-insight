#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
2026年7月23日 盘后速递报告生成脚本
使用 V3.0 AftermarketGenerator 生成
"""
import sys
import os

sys.path.insert(0, '/root/daily-news-insight/v3')
os.chdir('/root/daily-news-insight')

from v3.generators.aftermarket import AftermarketGenerator
from components.layout import Section, HighlightBox, CardGrid, SubCard
from components.data import DataCard, Badge

# ==================== 初始化生成器 ====================
gen = AftermarketGenerator(
    date_str="20260723",
    subtitle="2026.07.23 · 盘后速递"
)

# ==================== 1. 今日核心亮点 ====================
gen.add_today_highlight(
    "缩量震荡收红：沪指涨0.25%收3876.78点，深成指涨0.44%，创业板涨0.25%，科创50大跌3.78%。"
    "高低切换极致演绎：电网设备/锂矿/油气/贵金属领涨，半导体/先进封装/存储芯片领跌。"
    "成交2.21万亿，较昨日缩量4591亿。全市场超4200只个股上涨，涨停54家，跌停34家。"
    "持仓分化：英维克+0.99%震荡，铜冠铜箔-2.29%续跌，雅克科技-0.53%高位整固，*ST建艺+9.03%涨停。"
)

print("1/12 核心亮点完成")
