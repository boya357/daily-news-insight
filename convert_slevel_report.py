#!/usr/bin/env python3
"""
S级催化扫描报告转换脚本
将Markdown内容插入到标准HTML模板中
"""
import re

# 读取Markdown内容
with open("S级催化扫描/20260604_盘前_S级催化扫描.md", "r", encoding="utf-8") as f:
    md_content = f.read()

# 读取模板
with open("docs/s级催化扫描/20260604_盘前_S级催化扫描.html", "r", encoding="utf-8") as f:
    template = f.read()

# 修改标题
template = template.replace("每日新闻洞察 - 2026年6月4日", "S级催化扫描 - 2026年6月4日")
template = template.replace("<h1 class=\"text-4xl font-black gradient-text mb-3\">每日新闻洞察", "<h1 class=\"text-4xl font-black gradient-text mb-3\">S级催化扫描")
template = template.replace("早间市场新闻与机会挖掘", "盘前催化事件深度扫描与IMPS评级")
template = template.replace("2026年6月4日 星期四 早间版", "2026年6月4日 星期四 盘前版")

# 生成报告内容HTML
def md_to_html(md_text):
    html = md_text
    
    # 标题
    html = re.sub(r'^# (.*?)$', r'<h1 class="text-3xl font-bold text-gray-800 mb-4">\1</h1>', html, flags=re.MULTILINE)
    html = re.sub(r'^## (.*?)$', r'<h2 class="text-2xl font-bold text-gray-800 mt-8 mb-4 pb-2 border-b-2 border-indigo-200">\1</h2>', html, flags=re.MULTILINE)
    html = re.sub(r'^### (.*?)$', r'<h3 class="text-xl font-semibold text-gray-700 mt-6 mb-3">\1</h3>', html, flags=re.MULTILINE)
    html = re.sub(r'^#### (.*?)$', r'<h4 class="text-lg font-medium text-gray-600 mt-4 mb-2">\1</h4>', html, flags=re.MULTILINE)
    
    # 粗体
    html = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', html)
    
    # 列表
    html = re.sub(r'^- (.*?)$', r'<li class="text-gray-700 mb-2 ml-4">\1</li>', html, flags=re.MULTILINE)
    
    # 段落
    def replace_paragraph(match):
        text = match.group(1)
        if text.strip().startswith('<') or text.strip().startswith('|') or not text.strip():
            return match.group(0)
        return f'<p class="text-gray-700 mb-4 leading-relaxed">{text}</p>'
    
    # 分隔线
    html = re.sub(r'^---$', r'<hr class="my-6 border-gray-200">', html, flags=re.MULTILINE)
    
    return html

content_html = md_to_html(md_content)

# 处理表格（简单处理）
lines = content_html.split('\n')
in_table = False
table_html = []
result = []

for line in lines:
    if line.strip().startswith('|') and '---' not in line:
        if not in_table:
            in_table = True
            table_html = ['<table class="w-full border-collapse mb-6">']
        if '产业链' in line and '催化事件' in line:  # 表头
            cells = [c.strip() for c in line.strip().split('|')[1:-1]]
            table_html.append('<thead><tr>')
            for cell in cells:
                table_html.append(f'<th class="bg-gradient-to-r from-indigo-500 to-purple-500 text-white px-4 py-3 text-left font-semibold">{cell}</th>')
            table_html.append('</tr></thead><tbody>')
        else:
            cells = [c.strip() for c in line.strip().split('|')[1:-1]]
            if cells:
                table_html.append('<tr>')
                for cell in cells:
                    table_html.append(f'<td class="border border-gray-200 px-4 py-3 text-gray-700">{cell}</td>')
                table_html.append('</tr>')
    else:
        if in_table:
            table_html.append('</tbody></table>')
            result.append('\n'.join(table_html))
            in_table = False
        result.append(line)

content_html = '\n'.join(result)

# 找到内容区域并替换
# 找到第一个card-glass p-6 mb-8（摘要区域）之后的所有内容
# 替换从摘要区域开始到最后
new_content = f'''
            <div class="card-glass p-8 mb-8 border-2 border-white/20">
                <div class="text-center">
                    <h1 class="text-4xl font-black gradient-text mb-3">S级催化扫描</h1>
                    <p class="text-gray-600 text-lg">盘前催化事件深度扫描与IMPS评级</p>
                    <div class="flex items-center justify-center gap-4 mt-4">
                        <span class="text-gray-500 flex items-center gap-2">
                            <i class="fa fa-calendar"></i> 2026年6月4日 星期四 盘前版
                        </span>
                    </div>
                </div>
            </div>

            <div class="card-glass p-6">
                {content_html}
            </div>
'''

# 找到内容区域的开始和结束位置
# 从标题下的card-glass开始到</div>之前
start_pattern = r'            <div class="card-glass p-8 mb-8 border-2 border-white/20">.*?(?=\s+</div>\s+<!-- 页脚)'
match = re.search(start_pattern, template, re.DOTALL)
if match:
    template = template[:match.start()] + new_content + template[match.end():]

# 写入文件
with open("docs/s级催化扫描/20260604_盘前_S级催化扫描.html", "w", encoding="utf-8") as f:
    f.write(template)

print("✅ S级催化扫描报告已转换完成！")
