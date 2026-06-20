#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
重构半年报业绩预增深度研究报告 - 使用存储芯片报告的Pro版框架
"""

import re
from pathlib import Path

# 读取文件
storage_report_path = Path("docs/industry_chain/20260619_存储芯片产业链深度研究报告.html")
halfyear_report_path = Path("docs/industry_chain/20260619_半年报业绩预增深度研究报告.html")

with open(storage_report_path, 'r', encoding='utf-8') as f:
    storage_html = f.read()

with open(halfyear_report_path, 'r', encoding='utf-8') as f:
    halfyear_html = f.read()

# ========== 第一步：从半年报报告中提取各章节内容 ==========

# 提取section1: 核心观点摘要
section1_match = re.search(r'<div id="section1".*?>(.*?)</div>\s*</div>\s*<div id="section2"', halfyear_html, re.DOTALL)
section1_content = section1_match.group(1) if section1_match else ""

# 提取section2: 核心研究结论
section2_match = re.search(r'<div id="section2".*?>(.*?)</div>\s*<div id="section3"', halfyear_html, re.DOTALL)
section2_content = section2_match.group(1) if section2_match else ""

# 提取section3: 净利润增幅排行榜
section3_match = re.search(r'<div id="section3".*?>(.*?)</div>\s*<div id="section4"', halfyear_html, re.DOTALL)
section3_content = section3_match.group(1) if section3_match else ""

# 提取section4: 高增长行业分布
section4_match = re.search(r'<div id="section4".*?>(.*?)</div>\s*<div id="section5"', halfyear_html, re.DOTALL)
section4_content = section4_match.group(1) if section4_match else ""

# 提取section5: 三大高增长赛道深度剖析
section5_match = re.search(r'<div id="section5".*?>(.*?)</div>\s*<div id="section6"', halfyear_html, re.DOTALL)
section5_content = section5_match.group(1) if section5_match else ""

# 提取section6: 重点标的深度分析
section6_match = re.search(r'<div id="section6".*?>(.*?)</div>\s*<!--\s*投资策略\s*-->', halfyear_html, re.DOTALL)
section6_content = section6_match.group(1) if section6_match else ""

# 提取section7: 投资策略建议
section7_match = re.search(r'<div id="section7".*?>(.*?)</div>\s*<div id="section8"', halfyear_html, re.DOTALL)
section7_content = section7_match.group(1) if section7_match else ""

print(f"提取到的章节内容长度:")
print(f"  section1 (核心观点): {len(section1_content)} 字符")
print(f"  section2 (研究结论): {len(section2_content)} 字符")
print(f"  section3 (增幅排行): {len(section3_content)} 字符")
print(f"  section4 (行业分布): {len(section4_content)} 字符")
print(f"  section5 (赛道剖析): {len(section5_content)} 字符")
print(f"  section6 (标的分析): {len(section6_content)} 字符")
print(f"  section7 (投资策略): {len(section7_content)} 字符")

# ========== 第二步：构建新的报告内容 ==========

# 从存储芯片报告中提取头部（head + 导航栏 + 封面Banner之前的部分）
head_match = re.search(r'(<!DOCTYPE html>.*?<div class="pt-20 pb-16">)', storage_html, re.DOTALL)
head_part = head_match.group(1) if head_match else ""

# 修改标题和副标题
head_part = head_part.replace("存储芯片产业链深度研究报告", "2026年A股半年报业绩预增深度研究报告")
head_part = head_part.replace("AI驱动超级周期，供需重构万亿赛道", "挖掘高增长金矿，布局业绩爆发标的")

# 修改标签
old_tags = '<span class="tag-badge" style="background: rgba(255,255,255,0.2); color: white;">存储芯片</span>\n<span class="tag-badge" style="background: rgba(255,255,255,0.2); color: white;">HBM</span>\n<span class="tag-badge" style="background: rgba(255,255,255,0.2); color: white;">DRAM</span>\n<span class="tag-badge" style="background: rgba(255,255,255,0.2); color: white;">NAND Flash</span>\n<span class="tag-badge" style="background: rgba(255,255,255,0.2); color: white;">国产替代</span>'

new_tags = '<span class="tag-badge" style="background: rgba(255,255,255,0.2); color: white;">半年报</span>\n<span class="tag-badge" style="background: rgba(255,255,255,0.2); color: white;">业绩预增</span>\n<span class="tag-badge" style="background: rgba(255,255,255,0.2); color: white;">高增长</span>\n<span class="tag-badge" style="background: rgba(255,255,255,0.2); color: white;">半导体</span>\n<span class="tag-badge" style="background: rgba(255,255,255,0.2); color: white;">新能源</span>'

head_part = head_part.replace(old_tags, new_tags)

# 修改封面数据卡片
old_stats = '''<div class="grid grid-cols-2 md:grid-cols-4 gap-4 mb-8">
<div class="stat-card p-4 text-center">
<div class="text-3xl font-black text-indigo-600">5516亿</div>
<div class="text-sm text-gray-500 mt-1">2026年全球市场规模(美元)</div>
</div>
<div class="stat-card p-4 text-center">
<div class="text-3xl font-black text-purple-600">+134%</div>
<div class="text-sm text-gray-500 mt-1">同比增速</div>
</div>
<div class="stat-card p-4 text-center">
<div class="text-3xl font-black text-violet-600">5.1%</div>
<div class="text-sm text-gray-500 mt-1">HBM供需缺口</div>
</div>
<div class="stat-card p-4 text-center">
<div class="text-3xl font-black text-fuchsia-600">70%</div>
<div class="text-sm text-gray-500 mt-1">数据中心DRAM占比</div>
</div>
</div>'''

new_stats = '''<div class="grid grid-cols-2 md:grid-cols-4 gap-4 mb-8">
<div class="stat-card p-4 text-center">
<div class="text-3xl font-black text-indigo-600">2845%</div>
<div class="text-sm text-gray-500 mt-1">最高净利润增幅</div>
</div>
<div class="stat-card p-4 text-center">
<div class="text-3xl font-black text-purple-600">12个</div>
<div class="text-sm text-gray-500 mt-1">高增长行业</div>
</div>
<div class="stat-card p-4 text-center">
<div class="text-3xl font-black text-violet-600">6只</div>
<div class="text-sm text-gray-500 mt-1">重点关注标的</div>
</div>
<div class="stat-card p-4 text-center">
<div class="text-3xl font-black text-fuchsia-600">3大赛道</div>
<div class="text-sm text-gray-500 mt-1">核心增长引擎</div>
</div>
</div>'''

head_part = head_part.replace(old_stats, new_stats)

# 修改目录
old_toc = '''<a class="toc-item" href="#section1">一、核心观点摘要</a>
<a class="toc-item" href="#section2">二、行业概述与市场规模</a>
<a class="toc-item" href="#section3">三、产业链全景分析</a>
<a class="toc-item" href="#section4">四、细分产品深度解析</a>
<a class="toc-item" href="#section5">五、全球竞争格局</a>
<a class="toc-item" href="#section6">六、国产替代进程</a>
<a class="toc-item" href="#section7">七、技术发展趋势</a>
<a class="toc-item" href="#section8">八、投资机会与风险</a>
<a class="toc-item" href="#section9">九、重点标的分析</a>
<a class="toc-item" href="#section10">十、boya 投资策略总纲</a>'''

new_toc = '''<a class="toc-item" href="#section1">一、核心观点摘要</a>
<a class="toc-item" href="#section2">二、核心研究结论</a>
<a class="toc-item" href="#section3">三、净利润增幅排行榜 TOP20</a>
<a class="toc-item" href="#section4">四、高增长行业分布</a>
<a class="toc-item" href="#section5">五、三大高增长赛道深度剖析</a>
<a class="toc-item" href="#section6">六、重点标的深度分析</a>
<a class="toc-item" href="#section7">七、投资策略建议</a>
<a class="toc-item" href="#section8">八、boya 投资策略总纲</a>'''

head_part = head_part.replace(old_toc, new_toc)

# ========== 第三步：构建各章节内容 ==========

# 章节标题样式
def make_section_title(num, title):
    return f'<h2 id="section{num}"><span style="display:inline-block;width:4px;height:1.1em;background:linear-gradient(to bottom,#8b5cf6,#3b82f6);margin-right:10px;vertical-align:middle;border-radius:2px;"></span>{title}</h2>'

# 构建完整的章节HTML
def build_section(num, title, content):
    return f'''<div class="glass-card p-6 md:p-8">
{make_section_title(num, title)}
{content}
</div>'''

# 清理section内容中的标题（因为我们已经加了统一的标题）
def clean_section_title(content):
    # 移除section-title div
    content = re.sub(r'<div class="section-title"[^>]*>.*?</h2>\s*</div>', '', content, flags=re.DOTALL)
    # 移除h2标题
    content = re.sub(r'<h2[^>]*>.*?</h2>', '', content, flags=re.DOTALL)
    return content.strip()

# 构建各章节
section1_html = build_section(1, "一、核心观点摘要", clean_section_title(section1_content))
section2_html = build_section(2, "二、核心研究结论", clean_section_title(section2_content))
section3_html = build_section(3, "三、净利润增幅排行榜 TOP 20", clean_section_title(section3_content))
section4_html = build_section(4, "四、高增长行业分布", clean_section_title(section4_content))
section5_html = build_section(5, "五、三大高增长赛道深度剖析", clean_section_title(section5_content))
section6_html = build_section(6, "六、重点标的深度分析", clean_section_title(section6_content))
section7_html = build_section(7, "七、投资策略建议", clean_section_title(section7_content))

# ========== 第四步：构建boya投资策略总纲（基于存储芯片报告的结构，替换内容） ==========

# 从存储芯片报告中提取boya投资策略总纲模块
boya_section_match = re.search(r'<div class="glass-card p-6 md:p-8">\s*<h2 id="section10"[^>]*>.*?boya 投资策略总纲.*?</h2>(.*?)</div>\s*</div>\s*<!--\s*页脚\s*-->', storage_html, re.DOTALL)
boya_template = boya_section_match.group(1) if boya_section_match else ""

# 替换评级卡片内容
boya_template = boya_template.replace("存储芯片", "半年报高增长")
boya_template = boya_template.replace("存储芯片行业", "半年报高增长赛道")
boya_template = boya_template.replace("存储板块", "高增长板块")

# 构建完整的boya章节
boya_section_html = f'''<div class="glass-card p-6 md:p-8">
{make_section_title(8, "八、boya 投资策略总纲")}
{boya_template}
</div>'''

# ========== 第五步：提取页脚和脚本 ==========

footer_match = re.search(r'(<!--\s*页脚\s*-->.*?</html>)', storage_html, re.DOTALL)
footer_part = footer_match.group(1) if footer_match else ""

# 修改页脚中的标题
footer_part = footer_part.replace("存储芯片产业链深度研究报告", "2026年A股半年报业绩预增深度研究报告")

# ========== 第六步：组装完整HTML ==========

# 组装内容
main_content = f'''
{section1_html}
{section2_html}
{section3_html}
{section4_html}
{section5_html}
{section6_html}
{section7_html}
{boya_section_html}
'''

# 完整HTML
new_html = f'''{head_part}
{main_content}
{footer_part}'''

# 修复可能的问题：确保只有一个report-content div
# 检查head_part结尾
if 'report-content space-y-6' in head_part:
    # 移除可能重复的report-content开头
    new_html = new_html.replace('<div class="report-content space-y-6"><div class="glass-card p-6 md:p-8">', 
                               '<div class="report-content space-y-6"><div class="glass-card p-6 md:p-8">', 1)

# 保存文件
output_path = Path("docs/industry_chain/20260619_半年报业绩预增深度研究报告_v2.html")
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(new_html)

print(f"\n✅ 报告重构完成，已保存到: {output_path}")
print(f"   文件大小: {len(new_html)} 字符")

# 检查HTML基本结构
if '<!DOCTYPE html>' in new_html and '</html>' in new_html:
    print("   ✅ HTML结构完整")
else:
    print("   ❌ HTML结构不完整")

if 'boya 投资策略总纲' in new_html:
    print("   ✅ boya投资策略总纲已包含")
else:
    print("   ❌ boya投资策略总纲缺失")

if '目录导航' in new_html:
    print("   ✅ 侧边目录已包含")
else:
    print("   ❌ 侧边目录缺失")

if 'glass-nav' in new_html:
    print("   ✅ 导航栏已包含")
else:
    print("   ❌ 导航栏缺失")

