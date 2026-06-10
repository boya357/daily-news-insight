#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
更新盘中快报列表页 - 2026年6月10日
在网格顶部插入新卡片，保持原有格式
"""
import os

list_file = "/root/daily-news-insight/docs/intraday/latest.html"

# 读取原文件
with open(list_file, 'r', encoding='utf-8') as f:
    content = f.read()

# 新的最新报告卡片（橙色高亮）
new_card = '''                <a href="20260610_盘中快报.html" class="report-card block p-5 bg-gradient-to-br from-orange-50 to-red-50 border-2 border-orange-200 rounded-xl text-center group hover:shadow-lg transition-all">
    <div class="text-3xl mb-2">⚡</div>
    <div class="font-semibold text-gray-800 text-sm mb-1 group-hover:text-orange-600 transition-colors line-clamp-2">20260610 盘中快报</div>
    <span class="inline-block px-2 py-1 text-xs font-bold bg-red-100 text-red-700 rounded">🆕 最新</span>
</a>
'''

# 找到网格开始的位置（第一个report-card之前）
grid_start = '<div class="grid grid-cols-2 md:grid-cols-4 gap-4">'
insert_pos = content.find(grid_start) + len(grid_start)

# 把原来的"最新"卡片改成普通样式（橙色渐变改成白色，标签改回普通）
old_latest_pattern = '''<a href="20260609_盘中快报.html" class="report-card block p-5 bg-gradient-to-br from-orange-50 to-red-50 border-2 border-orange-200 rounded-xl text-center group hover:shadow-lg transition-all">
    <div class="text-3xl mb-2">⚡</div>
    <div class="font-semibold text-gray-800 text-sm mb-1 group-hover:text-orange-600 transition-colors line-clamp-2">20260609 盘中快报</div>
    <span class="inline-block px-2 py-1 text-xs font-bold bg-red-100 text-red-700 rounded">🆕 最新</span>
</a>'''

normal_card = '''<a href="20260609_盘中快报.html" class="report-card block p-5 bg-white border border-gray-100 rounded-xl text-center group hover:shadow-lg transition-all">
    <div class="text-3xl mb-2">⚡</div>
    <div class="font-semibold text-gray-800 text-sm mb-1 group-hover:text-indigo-600 transition-colors line-clamp-2">20260609 盘中快报</div>
    <span class="inline-block px-2 py-1 text-xs font-bold bg-orange-100 text-orange-700 rounded">盘中快报</span>
</a>'''

# 替换旧的最新卡片为普通样式
if old_latest_pattern in content:
    content = content.replace(old_latest_pattern, normal_card)
    print("已将6月9日的最新标记改为普通样式")
else:
    print("警告：未找到6月9日的最新卡片样式，可能格式不同")

# 在网格顶部插入新卡片
new_content = content[:insert_pos] + "\n" + new_card + content[insert_pos:]

# 备份原文件
backup_file = list_file + ".bak"
with open(backup_file, 'w', encoding='utf-8') as f:
    f.write(content)

# 写入新文件
with open(list_file, 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f"列表页已更新，新报告已添加到顶部")
print(f"原文件已备份到: {backup_file}")
print(f"新文件大小: {os.path.getsize(list_file)} 字节")
