#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
修复format大括号问题，改为replace方式
"""
import os

FILES = [
    'update_daily_list.py',
    'update_intraday_list.py',
    'update_aftermarket_list.py',
    'update_weekly_review_list.py',
    'update_weekly_outlook_list.py',
    'update_weekend_express_list.py',
    'update_tomorrow_catalyst_list.py',
    'update_slevel_catalyst_list.py',
    'update_monthly_list.py',
]

def fix_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # 找到final_html那行开始的位置，替换成正确的代码
    new_lines = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if 'final_html = PAGE_TEMPLATE' in line:
            # 替换成正确的一行
            new_lines.append("    final_html = PAGE_TEMPLATE.replace('__REPORT_CARDS__', '\\n'.join(report_cards))\n")
            # 跳过接下来的几行（直到空行或下一个逻辑）
            i += 1
            while i < len(lines) and not lines[i].strip() == '' and 'output_path' not in lines[i]:
                i += 1
            continue
        new_lines.append(line)
        i += 1
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    
    print(f'✅ {filename} 已修复')

for f in FILES:
    if os.path.exists(f):
        fix_file(f)
print('\n✅ 所有文件修复完成！')
