#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
统一更新所有列表页脚本
一键执行所有列表页的自动更新（布局固定，只更新报告卡片）
用法: python3 update_all_lists.py
"""

import subprocess
import sys

scripts = [
    ('每日新闻洞察', 'update_daily_list.py'),
    ('盘中快报', 'update_intraday_list.py'),
    ('盘后速递', 'update_aftermarket_list.py'),
    ('产业链总览', 'update_industry_chain_list.py'),
    ('周复盘', 'update_weekly_review_list.py'),
    ('周三前瞻', 'update_weekly_outlook_list.py'),
    ('周末速递', 'update_weekend_express_list.py'),
    ('明日催化剂', 'update_tomorrow_catalyst_list.py'),
    ('S级催化扫描', 'update_slevel_catalyst_list.py'),
    ('月报', 'update_monthly_list.py'),
    ('首页', 'update_index.py'),
]

print('=' * 60)
print('🚀 开始统一更新所有列表页...')
print('=' * 60)
print()

success_count = 0
fail_count = 0

for name, script in scripts:
    print(f'📦 更新 {name}...')
    try:
        result = subprocess.run(
            [sys.executable, script],
            capture_output=True,
            text=True,
            timeout=30
        )
        if result.returncode == 0:
            print(f'   ✅ {name} 更新成功')
            if result.stdout:
                for line in result.stdout.strip().split('\n'):
                    print(f'      {line}')
            success_count += 1
        else:
            print(f'   ❌ {name} 更新失败')
            if result.stderr:
                for line in result.stderr.strip().split('\n'):
                    print(f'      {line}')
            fail_count += 1
    except Exception as e:
        print(f'   ❌ {name} 执行异常: {e}')
        fail_count += 1
    print()

print('=' * 60)
print(f'✅ 更新完成！成功 {success_count} 个，失败 {fail_count} 个')
print('=' * 60)
print()
print('💡 所有页面布局已完全固定，以后只需运行此脚本即可更新所有报告卡片')
print('💡 无需再手动编辑HTML文件，彻底消除人工失误风险')
