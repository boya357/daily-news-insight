#!/usr/bin/env python3
"""手动更新S级催化列表页"""
import os

filepath = '/root/daily-news-insight/docs/s_level_catalyst/latest.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 新报告卡片
new_card = '''<a href="20260708_盘后_S级催化扫描_美伊冲突科技股回调.html" class="report-card is-latest">
<div class="report-icon">⚡</div>
<div class="report-date"><i class="fas fa-calendar-day"></i>2026-07-08</div>
<div class="report-name">美伊冲突升级引爆油价 全球科技股承压回调</div>
<div class="report-badges"><span class="badge badge-post">盘后</span><span class="badge badge-new">NEW</span></div>
<div class="report-size"><i class="fas fa-file-alt" style="margin-right:4px;"></i>约100KB</div>
</a>
'''

# 1. 更新newest-card（最新报告）
old_newest = '<a href="20260708_S级催化扫描.html" class="newest-card">'
new_newest = '<a href="20260708_盘后_S级催化扫描_美伊冲突科技股回调.html" class="newest-card">'
content = content.replace(old_newest, new_newest)

# 更新newest-title
old_title = '<div class="newest-title">20260708_S级催化扫描</div>'
new_title = '<div class="newest-title">20260708_盘后_S级催化扫描_美伊冲突科技股回调</div>'
content = content.replace(old_title, new_title)

# 更新数量
content = content.replace('共 65 份', '共 66 份')
content = content.replace('共 65 份归档', '共 66 份归档')

# 2. 在report-grid开头插入新卡片
insert_marker = '<div class="report-grid">'
idx = content.find(insert_marker)
if idx != -1:
    insert_pos = idx + len(insert_marker)
    content = content[:insert_pos] + new_card + content[insert_pos:]

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"列表页已更新: {filepath}")
