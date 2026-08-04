#!/usr/bin/env python3
"""更新日报列表页，插入今日报告卡片"""
import re

index_path = "docs/daily/index.html"
with open(index_path, "r", encoding="utf-8") as f:
    content = f.read()

new_card = '''            <a href="20260804_每日新闻洞察.html" class="block bg-white/5 hover:bg-white/10 border border-white/10 hover:border-white/20 rounded-xl p-4 transition-all duration-300 group">
              <div class="flex items-start justify-between mb-2">
                <div>
                  <div class="text-white font-semibold group-hover:text-blue-400 transition-colors">2026年8月4日 每日新闻洞察</div>
                  <div class="text-white/50 text-xs mt-1">周二 · 韩股杠杆风暴二次发酵·FMS闪存峰会开幕·美股科技普涨</div>
                </div>
                <div class="text-xs text-white/40">08-04</div>
              </div>
              <div class="flex gap-2 flex-wrap mt-2">
                <span class="text-xs bg-red-500/20 text-red-400 px-2 py-0.5 rounded">S级催化</span>
                <span class="text-xs bg-amber-500/20 text-amber-400 px-2 py-0.5 rounded">持仓诊断</span>
                <span class="text-xs bg-blue-500/20 text-blue-400 px-2 py-0.5 rounded">全球市场</span>
              </div>
            </a>
'''

# 查找第一个卡片之前插入
pattern = r'(<div class="grid md:grid-cols-2 lg:grid-cols-3 gap-4">)\s*<a href="20\d{6}'
match = re.search(pattern, content)
if match:
    insert_pos = match.start(1) + len(match.group(1))
    new_content = content[:insert_pos] + new_card + content[insert_pos:]
    with open(index_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("列表页已更新，插入今日报告卡片")
else:
    print("未找到插入位置，检查页面结构")
    idx = content.find("grid md:grid-cols")
    if idx > 0:
        print(content[idx:idx+300])
