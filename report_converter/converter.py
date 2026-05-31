#!/usr/bin/env python3
"""
完整版Markdown→HTML转换器
专业级深度研究报告生成器
支持5大报告类型：日报/盘中/盘后/产业链/周复盘
"""
import re
import sys
import os
import glob
from typing import Dict, List, Any, Optional

from report_templates import TEMPLATE_MAPPING


class ReportConverter:
    """专业级报告转换器 - 支持全部报告类型"""
    
    def __init__(self):
        self.section_patterns = {
            'core_summary': ['核心结论', '核心观点', '投资要点', '核心摘要', '核心判断', '投资逻辑'],
            'market_review': ['市场回顾', '行情回顾', '大盘表现', '市场概览', '行情综述'],
            'industry_chain': ['产业链全景', '产业链分析', '行业分析', '产业链梳理', '产业格局'],
            'stock_analysis': ['标的分析', '个股分析', '核心标的', '弹性测算', '业绩弹性', '投资标的', '个股精选'],
            'catalyst': ['催化剂', '催化因素', '事件日历', '前瞻', '催化逻辑', '投资时点'],
            'risk': ['风险提示', '风险因素', '免责声明', '风险警示'],
            'chart': ['图表', '对比图', '统计图', '走势图', '数据图表'],
            'timeline': ['时间线', '事件时间线', '时间轴', '重要事件'],
            'news': ['新闻汇总', '重要新闻', '新闻动态', '热点追踪', '行业新闻']
        }
        
        self.section_icons = {
            'core_summary': '🎯',
            'market_review': '📊',
            'industry_chain': '⛓️',
            'stock_analysis': '📈',
            'catalyst': '⚡',
            'risk': '⚠️',
            'chart': '📊',
            'timeline': '📅',
            'news': '📰',
            'general': '📋'
        }
    
    def convert(self, md_file: str, html_file: str, report_type: str = 'industry_chain'):
        """转换入口"""
        # 1. 读取Markdown
        with open(md_file, 'r', encoding='utf-8') as f:
            md_content = f.read()
        
        # 2. 解析报告结构
        parsed = self._parse_report(md_content)
        
        # 3. 渲染HTML
        full_html = self._render_report(parsed, report_type)
        
        # 4. 安全写入（先写临时文件，再原子替换）
        temp_file = html_file + '.tmp'
        with open(temp_file, 'w', encoding='utf-8') as f:
            f.write(full_html)
        
        os.replace(temp_file, html_file)
        
        print(f"✅ 转换完成: {html_file} ({len(full_html)} 字符)")
        return True
    
    def _parse_report(self, md_content: str) -> Dict[str, Any]:
        """解析完整报告结构"""
        lines = md_content.split('\n')
        
        result = {
            'title': '深度研究报告',
            'subtitle': '',
            'sections': [],
            'metadata': {}
        }
        
        current_section = None
        current_content = []
        
        for line in lines:
            line = line.rstrip()
            
            # 一级标题 = 报告主标题
            if line.startswith('# '):
                result['title'] = line[2:].strip()
                continue
            
            # 二级标题 = 章节
            elif line.startswith('## '):
                if current_section:
                    current_section['content'] = '\n'.join(current_content)
                    result['sections'].append(current_section)
                
                section_title = line[3:].strip()
                section_type = self._detect_section_type(section_title)
                current_section = {
                    'title': section_title,
                    'type': section_type,
                    'level': 2,
                    'subsections': []
                }
                current_content = []
            
            # 三级标题 = 子章节
            elif line.startswith('### '):
                if current_section and current_content:
                    current_section['content'] = '\n'.join(current_content)
                    result['sections'].append(current_section)
                    current_content = []
                
                subsection_title = line[4:].strip()
                subsection_type = self._detect_section_type(subsection_title)
                current_section = {
                    'title': subsection_title,
                    'type': subsection_type,
                    'level': 3
                }
            
            # 其他内容
            else:
                if line.strip():
                    current_content.append(line)
        
        # 处理最后一个章节
        if current_section:
            current_section['content'] = '\n'.join(current_content)
            result['sections'].append(current_section)
        
        return result
    
    def _detect_section_type(self, title: str) -> str:
        """根据标题检测章节类型"""
        title_lower = title.lower()
        
        for section_type, patterns in self.section_patterns.items():
            for pattern in patterns:
                if pattern in title or pattern.lower() in title_lower:
                    return section_type
        
        return 'general'
    
    def _render_report(self, parsed: Dict[str, Any], report_type: str) -> str:
        """渲染完整HTML报告"""
        sections_html = []
        
        for section in parsed['sections']:
            sections_html.append(self._render_section(section, report_type))
        
        return f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{parsed['title']}</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.5.1/css/all.min.css">
    <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
    {self._get_base_styles()}
</head>
<body>
    {self._get_navigation(report_type)}
    
    <main class="content-area">
        {self._get_page_header(parsed['title'])}
        
        <div class="max-w-5xl mx-auto px-4">
            <div class="bg-white/95 backdrop-blur-sm rounded-3xl shadow-2xl p-8 md:p-10">
                {''.join(sections_html)}
            </div>
        </div>
    </main>
    
    {self._get_footer()}
</body>
</html>'''
    
    def _render_section(self, section: Dict[str, Any], report_type: str = 'industry_chain') -> str:
        """渲染章节 - 根据报告类型选择模板"""
        section_type = section['type']
        content = section.get('content', '')
        
        # 如果有专用模板，使用专用模板
        template = TEMPLATE_MAPPING.get(report_type)
        if template and hasattr(template, 'render_section'):
            try:
                return template.render_section(section['title'], content, section_type)
            except Exception as e:
                print(f"⚠️  专用模板渲染失败，使用通用模板: {e}")
        
        # 默认使用通用模板
        if section_type == 'core_summary':
            return self._render_core_summary_section(section)
        elif section_type == 'stock_analysis':
            return self._render_stock_analysis_section(section)
        elif section_type == 'risk':
            return self._render_risk_section(section)
        elif '|' in content and content.count('|') > 5:
            return self._render_table_section(section)
        else:
            return self._render_general_section(section)
    
    def _render_general_section(self, section: Dict[str, Any]) -> str:
        """渲染通用章节"""
        icon = self.section_icons.get(section['type'], '📋')
        level = section.get('level', 2)
        size_class = 'text-2xl' if level == 2 else 'text-xl'
        
        content_html = self._render_text_content(section.get('content', ''))
        
        return f'''
        <div class="mb-8 mt-10">
            <div class="flex items-center space-x-3 mb-4">
                <span class="text-3xl">{icon}</span>
                <h{level} class="{size_class} font-bold text-gray-800">{section['title']}</h{level}>
            </div>
            <div class="h-1 w-24 bg-gradient-to-r from-indigo-500 to-purple-600 rounded-full mb-6 ml-1"></div>
            <div class="section-content">
                {content_html}
            </div>
        </div>
        '''
    
    def _render_core_summary_section(self, section: Dict[str, Any]) -> str:
        """渲染核心摘要章节"""
        content = section.get('content', '')
        points = self._extract_list_items(content)
        
        points_html = []
        for i, point in enumerate(points, 1):
            points_html.append(f'''
            <div class="flex items-start space-x-3 py-3 border-b border-indigo-100 last:border-0">
                <div class="w-6 h-6 rounded-full bg-gradient-to-br from-indigo-500 to-purple-600 flex items-center justify-center flex-shrink-0 mt-0.5">
                    <span class="text-white text-xs font-bold">{i}</span>
                </div>
                <div class="text-gray-700 leading-relaxed">{self._render_inline_markdown(point)}</div>
            </div>
            ''')
        
        return f'''
        <div class="mb-8 mt-10">
            <div class="flex items-center space-x-3 mb-4">
                <span class="text-3xl">🎯</span>
                <h2 class="text-2xl font-bold text-gray-800">{section['title']}</h2>
            </div>
            <div class="h-1 w-24 bg-gradient-to-r from-indigo-500 to-purple-600 rounded-full mb-6 ml-1"></div>
            
            <div class="bg-gradient-to-br from-indigo-50 to-purple-50 rounded-2xl p-6 border border-indigo-100">
                {''.join(points_html)}
            </div>
        </div>
        '''
    
    def _render_stock_analysis_section(self, section: Dict[str, Any]) -> str:
        """渲染标的分析章节"""
        content = section.get('content', '')
        stocks = self._extract_stock_info(content)
        
        cards_html = []
        for stock in stocks[:8]:  # 最多显示8个标的
            metrics_html = []
            for key, value in stock.get('metrics', {}).items():
                metrics_html.append(f'''
                <div class="flex items-center justify-between py-2 border-b border-gray-100 last:border-0">
                    <span class="text-gray-500 text-sm">{key}</span>
                    <span class="font-semibold text-gray-800">{value}</span>
                </div>
                ''')
            
            cards_html.append(f'''
            <div class="bg-white rounded-2xl p-6 shadow-lg hover:shadow-xl transition-all hover:-translate-y-1 border border-gray-100">
                <div class="flex items-center justify-between mb-4">
                    <div>
                        <h4 class="font-bold text-xl text-gray-800">{stock['name']}</h4>
                        <span class="text-sm text-gray-500">{stock['code']}</span>
                    </div>
                    <div class="w-12 h-12 rounded-xl bg-gradient-to-br from-purple-500 to-pink-500 flex items-center justify-center">
                        <span class="text-white text-xl">📈</span>
                    </div>
                </div>
                <div class="space-y-1">
                    {''.join(metrics_html)}
                </div>
            </div>
            ''')
        
        return f'''
        <div class="mb-8 mt-10">
            <div class="flex items-center space-x-3 mb-4">
                <span class="text-3xl">📈</span>
                <h2 class="text-2xl font-bold text-gray-800">{section['title']}</h2>
            </div>
            <div class="h-1 w-24 bg-gradient-to-r from-indigo-500 to-purple-600 rounded-full mb-6 ml-1"></div>
            
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                {''.join(cards_html)}
            </div>
        </div>
        '''
    
    def _render_risk_section(self, section: Dict[str, Any]) -> str:
        """渲染风险提示章节"""
        content = section.get('content', '')
        points = self._extract_list_items(content)
        
        points_html = []
        for point in points:
            points_html.append(f'''
            <div class="flex items-start space-x-3 py-2">
                <span class="text-red-500 mt-1">⚠️</span>
                <div class="text-red-800 leading-relaxed">{self._render_inline_markdown(point)}</div>
            </div>
            ''')
        
        return f'''
        <div class="mb-8 mt-10">
            <div class="flex items-center space-x-3 mb-4">
                <span class="text-3xl">⚠️</span>
                <h2 class="text-2xl font-bold text-gray-800">{section['title']}</h2>
            </div>
            <div class="h-1 w-24 bg-gradient-to-r from-red-500 to-orange-500 rounded-full mb-6 ml-1"></div>
            
            <div class="bg-red-50 rounded-2xl p-6 border border-red-200">
                {''.join(points_html)}
            </div>
        </div>
        '''
    
    def _render_table_section(self, section: Dict[str, Any]) -> str:
        """渲染表格章节"""
        content = section.get('content', '')
        lines = content.split('\n')
        
        table_lines = []
        text_before = []
        in_table = False
        
        for line in lines:
            if '|' in line and line.count('|') > 2:
                in_table = True
                table_lines.append(line)
            elif in_table:
                break
            else:
                text_before.append(line)
        
        table_html = self._render_table(table_lines) if table_lines else ''
        text_html = self._render_text_content('\n'.join(text_before))
        
        return f'''
        <div class="mb-8 mt-10">
            <div class="flex items-center space-x-3 mb-4">
                <span class="text-3xl">📊</span>
                <h2 class="text-2xl font-bold text-gray-800">{section['title']}</h2>
            </div>
            <div class="h-1 w-24 bg-gradient-to-r from-indigo-500 to-purple-600 rounded-full mb-6 ml-1"></div>
            {text_html}
            {table_html}
        </div>
        '''
    
    def _render_text_content(self, content: str) -> str:
        """渲染文本内容"""
        if not content:
            return ''
        
        lines = content.split('\n')
        html = []
        
        in_list = False
        for line in lines:
            line = line.strip()
            if not line:
                continue
            
            if line.startswith('- ') or line.startswith('* '):
                if not in_list:
                    html.append('<ul class="mb-4">')
                    in_list = True
                html.append(f'<li class="text-gray-700 mb-2 ml-4">{self._render_inline_markdown(line[2:].strip())}</li>')
            else:
                if in_list:
                    html.append('</ul>')
                    in_list = False
                html.append(f'<p class="text-gray-700 mb-4 leading-relaxed">{self._render_inline_markdown(line)}</p>')
        
        if in_list:
            html.append('</ul>')
        
        return '\n'.join(html)
    
    def _render_table(self, table_lines: list) -> str:
        """渲染表格"""
        if len(table_lines) < 3:
            return ''
        
        headers = [h.strip() for h in table_lines[0].split('|')[1:-1]]
        
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
        <div class="bg-white rounded-2xl shadow-lg overflow-hidden mb-6 border border-gray-100">
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
    
    def _render_inline_markdown(self, text: str) -> str:
        """渲染行内Markdown格式"""
        text = re.sub(r'\*\*(.+?)\*\*', r'<strong class="font-bold">\1</strong>', text)
        text = re.sub(r'\*(.+?)\*', r'<em>\1</em>', text)
        text = re.sub(r'`(.+?)`', r'<code class="bg-gray-100 px-1 rounded text-pink-600 text-sm">\1</code>', text)
        text = re.sub(r'\[(.+?)\]\((.+?)\)', r'<a href="\2" class="text-indigo-600 hover:underline">\1</a>', text)
        return text
    
    def _extract_list_items(self, content: str) -> list:
        """提取列表项"""
        items = []
        for line in content.split('\n'):
            line = line.strip()
            if line.startswith('- ') or line.startswith('* '):
                items.append(line[2:].strip())
            elif line and not line.startswith('|'):
                items.append(line)
        return items
    
    def _extract_stock_info(self, content: str) -> list:
        """提取标的信息"""
        stocks = []
        lines = content.split('\n')
        
        current_stock = None
        for line in lines:
            line = line.strip()
            
            # 匹配标的名称+代码模式
            stock_match = re.match(r'^[*-]?\s*(.+?)\s*[（(](\d{6})[）)]', line)
            if stock_match:
                if current_stock:
                    stocks.append(current_stock)
                current_stock = {
                    'name': stock_match.group(1),
                    'code': stock_match.group(2),
                    'metrics': {}
                }
            elif current_stock and ':' in line:
                # 提取键值对指标
                parts = line.split(':', 1)
                if len(parts) == 2:
                    key = parts[0].strip('-* ')
                    value = parts[1].strip()
                    if key and value and len(key) < 10:
                        current_stock['metrics'][key] = value
        
        if current_stock:
            stocks.append(current_stock)
        
        # 如果没找到结构化标的，尝试简单匹配
        if not stocks:
            for line in lines:
                simple_match = re.search(r'(.+?)\s*[（(](\d{6})[）)]', line)
                if simple_match:
                    stocks.append({
                        'name': simple_match.group(1),
                        'code': simple_match.group(2),
                        'metrics': {}
                    })
        
        return stocks
    
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
            nav_items.append(f'<a href="{page_url}" class="{active_class} text-sm transition-colors px-3 py-1.5 rounded-lg">{page_name}</a>')
        
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
            
            .section-content h4 {
                font-size: 1.125rem;
                font-weight: 600;
                color: #1f2937;
                margin-top: 1rem;
                margin-bottom: 0.5rem;
            }
            
            * {
                scrollbar-width: thin;
                scrollbar-color: rgba(255,255,255,0.3) transparent;
            }
        </style>'''


def main():
    if len(sys.argv) < 3:
        print("用法: python converter.py <输入md文件> <输出html文件> [报告类型]")
        print("报告类型: daily / intraday / aftermarket / industry_chain / weekly_review")
        sys.exit(1)
    
    md_file = sys.argv[1]
    html_file = sys.argv[2]
    report_type = sys.argv[3] if len(sys.argv) > 3 else 'industry_chain'
    
    if not os.path.exists(md_file):
        print(f"❌ 文件不存在: {md_file}")
        sys.exit(1)
    
    converter = ReportConverter()
    converter.convert(md_file, html_file, report_type)


if __name__ == '__main__':
    main()
