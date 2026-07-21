#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""生成 2026-07-21 盘后速递 - V3.0统一标准"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'v3'))
os.chdir(os.path.dirname(os.path.abspath(__file__)))

from generators.aftermarket import AftermarketGenerator
from components.layout import Section

DATE = "20260721"
SUBTITLE = "2026.07.21 · 盘后速递 · 周二"
gen = AftermarketGenerator(date_str=DATE, subtitle=SUBTITLE)

# ===== 1. 今日核心亮点 =====
highlight = '''
<div style="font-size: 14px; line-height: 1.8; color: var(--text-secondary);">
<p style="margin: 0 0 12px 0;"><strong style="color: #4ade80;">📈 今日定性：深V大奇迹日，科技股暴力反弹</strong>。上证指数收3864.37点(+1.79%)，深成指+4.81%报14264.29，创业板指+7.05%，科创50暴涨10.73%。全市场3100+只上涨，181只涨停，仅20只跌停，与昨日全线跌停形成惊天逆转。</p>
<p style="margin: 0 0 12px 0;"><strong style="color: #c084fc;">🔥 核心主线：半导体/存储/算力全线爆发</strong>。存储芯片涨近9%，半导体设备批量20cm涨停。长鑫IPO打新资金解冻、台积电上调资本开支、海外存储涨价、政策维稳，四大因素共振。</p>
<p style="margin: 0 0 12px 0;"><strong style="color: #60a5fa;">💵 资金面：北向+ETF双重流入</strong>。北向净流入72-412亿，重仓回流半导体；股票ETF净流入超600亿。两市成交2.96万亿，放量2550亿。</p>
<p style="margin: 0;"><strong style="color: #fb923c;">⚠️ 持仓：三涨一跌，雅克地天板</strong>。雅克科技+10%地天板、英维克+8.17%、铜冠铜箔+4.17%、*ST建艺-1.64%。</p>
</div>'''
gen.add_today_highlight(highlight)

# ===== 2. 市场收盘总结 =====
indices = [
    {"name": "上证指数", "value": "3864.37", "change": "+1.79%", "icon": "trending_up", "up": True},
    {"name": "深证成指", "value": "14264.29", "change": "+4.81%", "icon": "trending_up", "up": True},
    {"name": "创业板指", "value": "3685.97", "change": "+7.05%", "icon": "trending_up", "up": True},
    {"name": "科创50", "value": "1903.16", "change": "+10.73%", "icon": "trending_up", "up": True},
]
gen.add_market_summary(indices, volume="2.96万亿(放量+2550亿)", northbound="净流入72-412亿")

print("Step 1-2 done")
