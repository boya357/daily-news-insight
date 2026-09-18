#!/usr/bin/env python3
"""
每日新闻洞察 - 2026-09-18 周五
基于 V3.0 Pro 生成器 + V5.0 L2 特性
"""
import sys, os
sys.path.insert(0, 'v3')
os.chdir('/root/daily-news-insight')

from generators.daily_pro import DailyReportProGenerator
from datetime import datetime

DATE_STR = "2026-09-18"
WEEKDAY = "周五"
OUTPUT_FILE = "docs/daily/20260918_每日新闻洞察.html"

print(f"=" * 60)
print(f"📰 每日新闻洞察 - {DATE_STR} {WEEKDAY}")
print(f"=" * 60)

# 初始化生成器
gen = DailyReportProGenerator(
    date_str=DATE_STR,
    weekday=WEEKDAY,
    subtitle=f"{DATE_STR} {WEEKDAY} · 龙空龙策略专用 · 隔夜纳指+1.69% 半导体爆发",
    data_dir='/root/daily-news-insight/data'
)

# V5.0 L2: TL;DR 核心结论卡片
gen.set_tldr(
    key_points=[
        "隔夜纳指+1.69%费城半导体+3.14%，英伟达AMD英特尔全线大涨，半导体板块迎来强催化",
        "A股科技主线确立，存储/先进封装/算力硬件三方向持续高景气，回调即是布局机会",
        "持仓4只按计划操作，英维克/雅克科技/铜冠铜箔震荡思路，*ST建艺逢高减仓"
    ],
    operation_advice="高开不追，回调加仓，聚焦存储产业链核心标的，控制仓位5成以内",
    risk_level="中高",
    suggested_position="4-5成"
)

# 构建标准报告（包含所有板块）
gen.build_standard_report()

# 发布
result = gen.publish(OUTPUT_FILE)

print(f"\n{'=' * 60}")
if result['success']:
    print(f"✅ 生成成功！")
    print(f"   文件: {result['output_path']}")
    print(f"   大小: {result['file_size']} bytes ({result['file_size']//1024} KB)")
    print(f"   时间: {result['update_time']}")
else:
    print(f"❌ 生成失败！")
    print(f"   错误: {result.get('error', result.get('errors', '未知错误'))}")
print(f"{'=' * 60}")
