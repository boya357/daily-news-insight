#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
2026-07-24 每日新闻洞察生成脚本
"""
import sys, os
sys.path.insert(0, 'v3')
os.chdir('/root/daily-news-insight')

from generators.daily_pro import DailyReportProGenerator

# 创建生成器
gen = DailyReportProGenerator(
    date_str="2026-07-24",
    weekday="周五",
    subtitle="2026-07-24 周五 · 龙空龙策略专用 · 存储链暴涨+政策组合拳落地",
    data_dir='/root/daily-news-insight/data'
)

# 构建标准报告（包含全部板块）
gen.build_standard_report()

# 发布 - 保存到日报目录
output_path = '/root/daily-news-insight/docs/daily/20260724_每日新闻洞察.html'
result = gen.publish(output_path)

if result.get('success'):
    print(f"✅ 报告生成完成！")
    print(f"   文件：{output_path}")
    print(f"   大小：{result.get('file_size', 0)} 字节")
else:
    print(f"❌ 生成失败：{result}")

# 更新 latest.html 副本
import shutil
latest_path = '/root/daily-news-insight/docs/daily/latest.html'
shutil.copy2(output_path, latest_path)
print(f"   latest.html 已更新")
