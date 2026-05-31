#!/usr/bin/env python3
"""
精简版Markdown→HTML转换器
最小可用，保证不出错
"""
import re
import sys
import os


class SimpleMarkdownConverter:
    """简单但可靠的转换器"""
    
    def __init__(self):
        self.components = {
            'navigation': self._get_navigation,
            'header': self._get_page_header,
            'footer': self._get_footer,
            'styles': self._get_base_styles
        }
    
    def convert(self, md_file: str, html_file: str, report_type: str = 'industry_chain'):
        """转换入口"""
        # 1. 读取Markdown
        with open(md_file, 'r', encoding='utf-8') as f:
            md_content = f.read()
        
        # 2. 提取标题
        title = self._extract_title(md_content)
        
        # 3. 转换内容
        content_html = self._markdown_to_html(md_content)
        
        # 4. 包装完整HTML
        full_html = self._wrap_html(title, content_html, report_type)
        
        # 5. 写入文件（安全写入：先写临时文件，再替换）
        temp_file = html_file + '.tmp'
        with open(temp_file, 'w', encoding='utf-8') as f:
            f.write(full_html)
        
        # 原子替换
        os.replace(temp_file, html_file)
        
        print(f"✅ 转换完成: {html_file}")
        return True
    
    def _extract_title(self, md_content: str) -> str:
        """提取主标题"""
        for line in md_content.split('\n'):
            if line.startswith('# '):
                return line[2:].strip()
        return '深度研究报告'
    
    def _markdown_to_html(self, md_content: str) -> str:
        """简单但可靠的Markdown转HTML"""
        html = []
        lines = md_content.split('\n')
        
        in_table = False
        table_lines = []
        
        for line in lines:
            line = line.rstrip()
            
            # 处理表格
            if '|' in line and line.count('|') > 2:
                in_table = True
                table_lines.append(line)
                continue
            elif in_table:
                # 表格结束
                html.append(self._render_table(table_lines))
                in_table = False
                table_lines = []
            
            # 空行
            if not line.strip():
                continue
            
            # 标题
            if line.startswith('# '):
                continue  # 主标题单独处理
            elif line.startswith('## '):
                html.append(self._render_section_title(line[3:].strip(), 2))
            elif line.startswith('### '):
                html.append(self._render_section_title(line[4:].strip(), 3))
            elif line.startswith('#### '):
                html.append(f'<h4 class="text-lg font-semibold text-gray-800 mt-4 mb-2">{line[5:].strip()}</h4>')
            
            # 分隔线
            elif line.startswith('---') or line.startswith('***'):
                html.append('<hr class="my-6 border-gray-200">')
            
            # 列表项
            elif line.startswith('- ') or line.startswith('* '):
                html.append(f'<li class="text-gray-700 mb-2 ml-4">{self._render_inline_markdown(line[2:].strip())}</li>')
            
            # 普通段落
            else:
                html.append(f'<p class="text-gray-700 mb-4 leading-relaxed">{self._render_inline_markdown(line)}</p>')
        
        # 处理可能剩余的表格
        if in_table and table_lines:
            html.append(self._render_table(table_lines))
        
        return '\n'.join(html)
    
    def _render_inline_markdown(self, text: str) -> str:
        """渲染行内Markdown格式"""
        # 粗体
        text = re.sub(r'\*\*(.+?)\*\*', r'<strong class="font-bold">\1</strong>', text)
        # 斜体
        text = re.sub(r'\*(.+?)\*', r'<em>\1</em>', text)
        # 代码
        text = re.sub(r'`(.+?)`', r'<code class="bg-gray-100 px-1 rounded text-pink-600">\1</code>', text)
        # 链接
        text = re.sub(r'\[(.+?)\]\((.+?)\)', r'<a href="\2" class="text-indigo-600 hover:underline">\1</a>', text)
        return text
    
    def _render_section_title(self, title: str, level: int) -> str:
        """渲染章节标题"""
        icons = {
            '核心': '🎯', '结论': '🎯', '摘要': '📋',
            '产业链': '⛓️', '行业': '🏭', '市场': '📊',
            '标的': '📈', '个股': '📈', '弹性': '💰',
            '风险': '⚠️', '提示': '⚠️', '免责': '📝',
            '催化': '⚡', '事件': '📅', '日历': '📆',
            '图表': '📊', '对比': '⚖️',
            '新闻': '📰', '动态': '🔔'
        }
        
        icon = '📋'
        for keyword, icon_candidate in icons.items():
            if keyword in title:
                icon = icon_candidate
                break
        
        size_class = 'text-2xl' if level == 2 else 'text-xl'
        
        return f'''
        <div class="mb-6 mt-10">
            <div class="flex items-center space-x-3">
                <span class="text-3xl">{icon}</span>
                <h{level} class="{size_class} font-bold text-gray-800">{title}</h{level}>
            </div>
            <div class="h-1 w-24 bg-gradient-to-r from-indigo-500 to-purple-600 rounded-full mt-3 ml-1"></div>
        </div>
        '''
    
    def _render_table(self, table_lines: list) -> str:
        """渲染表格"""
        if len(table_lines) < 3:
            return ''
        
        # 解析表头
        headers = [h.strip() for h in table_lines[0].split('|')[1:-1]]
        
        # 解析数据行
        rows = []
        for line in table_lines[2:]:
            cells = [c.strip() for c in line.split('|')[1:-1]]
            rows.append(cells)
        
        if not headers:
            return ''
        
        header_cells = ''.join([f'<th class="px-4 py-3 text-left text-sm font-semibold text-gray-700 bg-gray-50">{h}</th>' for h in headers])
        
        body_rows = []
        for row in rows:
            cells = ''.join([f'<td class="px-4 py-3 text-sm text-gray-600 border-t border-gray-100">{self._render_inline_markdown(c)}</td>' for c in row])
            body_rows.append(f'<tr class="hover:bg-gray-50">{cells}</tr>')
        
        return f'''
        <div class="bg-white rounded-2xl shadow-lg overflow-hidden mb-6">
            <div class="overflow-x-auto">
                <table class="w-full">
                    <thead>
                        <tr>{header_cells}</tr>
                    </thead>
                    <tbody>
                        {''.join(body_rows)}
                    </tbody>
                </table>
            </div>
        </div>
        '''
    
    def _wrap_html(self, title: str, content: str, report_type: str) -> str:
        """包装完整HTML"""
        return f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.5.1/css/all.min.css">
    {self._get_base_styles()}
</head>
<body>
    {self._get_navigation(report_type)}
    
    <main class="content-area">
        {self._get_page_header(title)}
        
        <div class="max-w-5xl mx-auto px-4">
            <div class="bg-white/95 backdrop-blur-sm rounded-3xl shadow-2xl p-8 md:p-10">
                {content}
            </div>
        </div>
    </main>
    
    {self._get_footer()}
</body>
</html>'''
    
    def _get_navigation(self, current_page: str) -> str:
        """导航栏"""
        pages = [
            ('daily', '日报', '/daily-news-insight/daily/latest.html'),
            ('intraday', '盘中', '/daily-news-insight/intraday/latest.html'),
            ('aftermarket', '盘后', '/daily-news-insight/aftermarket/latest.html'),
            ('industry_chain', '产业链', '/daily-news-insight/industry_chain/latest.html'),
            ('weekly_review', '周复盘', '/daily-news-insight/weekly_review/latest.html'),
        ]
        
        nav_items = []
        for page_id, page_name, page_url in pages:
            active_class = 'bg-white/20 text-white' if page_id == current_page else 'text-white/80 hover:text-white hover:bg-white/10'
            nav_items.append(f'''<a href="{page_url}" class="{active_class} text-sm transition-colors px-3 py-1.5 rounded-lg">{page_name}</a>''')
        
        return f'''
        <nav class="fixed top-0 left-0 right-0 z-50 glass-nav">
            <div class="max-w-5xl mx-auto px-4 py-3 flex items-center justify-between">
                <div class="flex items-center space-x-3">
                    <div class="w-8 h-8 rounded-lg bg-gradient-to-br from-indigo-500 to-purple-600 flex items-center justify-center">
                        <span class="text-white text-sm font-bold">📊</span>
                    </div>
                    <span class="text-white font-bold text-lg">投资研究中心</span>
                </div>
                <div class="flex items-center space-x-1 flex-wrap gap-1">
                    {''.join(nav_items)}
                </div>
            </div>
        </nav>'''
    
    def _get_page_header(self, title: str) -> str:
        """页面标题区"""
        return f'''
        <div class="pt-24 pb-8 px-4">
            <div class="max-w-5xl mx-auto text-center">
                <h1 class="text-3xl md:text-4xl font-black text-white mb-3 leading-tight">
                    {title}
                </h1>
            </div>
        </div>'''
    
    def _get_footer(self) -> str:
        """页脚"""
        return '''
        <div class="text-center py-10 px-4">
            <div class="text-white/60 text-sm">
                <p class="mb-2">💡 投资研究中心 · 专业深度研究</p>
                <p class="text-xs text-white/40">数据仅供参考，不构成投资建议</p>
            </div>
        </div>'''
    
    def _get_base_styles(self) -> str:
        """基础样式"""
        return '''
        <style>
            .glass-nav {
                background: rgba(255, 255, 255, 0.1);
                backdrop-filter: blur(20px);
                -webkit-backdrop-filter: blur(20px);
                border-bottom: 1px solid rgba(255, 255, 255, 0.2);
            }
            
            body {
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
                font-family: -apple-system, BlinkMacSystemFont, 'PingFang SC', 'Helvetica Neue', sans-serif;
            }
            
            .content-area {
                min-height: calc(100vh - 200px);
            }
            
            * {
                scrollbar-width: thin;
                scrollbar-color: rgba(255,255,255,0.3) transparent;
            }
        </style>'''


def main():
    if len(sys.argv) < 3:
        print("用法: python simple_converter.py <输入md文件> <输出html文件> [报告类型]")
        print("报告类型: daily / intraday / aftermarket / industry_chain / weekly_review")
        sys.exit(1)
    
    md_file = sys.argv[1]
    html_file = sys.argv[2]
    report_type = sys.argv[3] if len(sys.argv) > 3 else 'industry_chain'
    
    if not os.path.exists(md_file):
        print(f"❌ 文件不存在: {md_file}")
        sys.exit(1)
    
    converter = SimpleMarkdownConverter()
    converter.convert(md_file, html_file, report_type)


if __name__ == '__main__':
    main()
