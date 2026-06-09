#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
更新盘中快报列表页
"""
import os

list_file = "/root/daily-news-insight/docs/intraday/latest.html"

# 读取原文件
with open(list_file, 'r', encoding='utf-8') as f:
    content = f.read()

# 新的报告卡片HTML
new_card = '''
            <!-- REPORT_CARD_START -->
            <a href="20260609_盘中快报.html" class="block bg-white/90 backdrop-blur-sm rounded-xl p-5 border border-gray-100 shadow-sm hover:shadow-md transition-all hover:-translate-y-0.5">
                <div class="flex items-start justify-between">
                    <div class="flex-1">
                        <h3 class="font-semibold text-gray-800 hover:text-indigo-600 transition-colors">2026年6月9日 盘中快报</h3>
                        <p class="text-gray-500 text-sm mt-2 line-clamp-2">科技成长领涨，半导体产业链爆发，创业板指涨近2%</p>
                    </div>
                    <span class="inline-block px-2 py-0.5 rounded-full text-xs font-medium bg-indigo-100 text-indigo-700">最新</span>
                </div>
                <p class="text-xs text-gray-400 mt-3">2026-06-09</p>
            </a>
            <!-- REPORT_CARD_END -->
'''

# 在LIST_START后插入新卡片
list_start_marker = "<!-- LIST_START -->"
if list_start_marker in content:
    # 找到LIST_START的位置，在后面插入新卡片
    insert_pos = content.find(list_start_marker) + len(list_start_marker)
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
else:
    print("错误：未找到LIST_START标记")
    # 检查文件大小
    print(f"文件大小: {os.path.getsize(list_file)} 字节")
