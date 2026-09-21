#!/usr/bin/env python3
"""
每日新闻洞察 - 2026-09-21 周一
基于 V3.0 Pro 生成器 + V5.0 L2 特性
"""
import sys, os
sys.path.insert(0, 'v3')
os.chdir('/root/daily-news-insight')

from generators.daily_pro import DailyReportProGenerator
from datetime import datetime

DATE_STR = "2026-09-21"
WEEKDAY = "周一"
OUTPUT_FILE = "docs/daily/20260921_每日新闻洞察.html"

print(f"=" * 60)
print(f"📰 每日新闻洞察 - {DATE_STR} {WEEKDAY}")
print(f"=" * 60)

# 初始化生成器
gen = DailyReportProGenerator(
    date_str=DATE_STR,
    weekday=WEEKDAY,
    subtitle=f"{DATE_STR} {WEEKDAY} · 龙空龙策略专用 · 费城半导体+2.78% 存储芯片再爆发",
    data_dir='/root/daily-news-insight/data'
)

# V5.0 L2: TL;DR 核心结论卡片
gen.set_tldr(
    key_points=[
        "隔夜美股科技股再度走强，费城半导体+2.78%创阶段新高，美光+3.92%、SK海力士+6.42%，存储芯片超级周期逻辑持续强化",
        "长鑫科技第五代DRAM G5平台量产，北京发布词元经济行动方案支持词元工厂，AI算力产业链政策+产业双催化共振",
        "LPR连续16个月维持不变，国内流动性环境宽松，市场主线重回业绩景气，资金回流高景气科技板块",
        "液冷赛道持续升温但盈利承压，英维克H1增收不增利毛利率压缩至24.93%，铜冠铜箔HVLP4代量产高端铜箔供不应求"
    ],
    operation_advice="科技主线明确但切忌追高，开盘冲高先减仓，回调至支撑位再加仓；优先配置存储产业链（铜箔>HBM材料>封测），液冷关注业绩兑现拐点",
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
