#!/usr/bin/env python3
"""
各类型报告专用模板
"""
import re


class BaseTemplate:
    """基础模板 - 提供通用的内容渲染方法"""
    
    @staticmethod
    def render_content(content: str) -> str:
        """智能渲染Markdown内容 - 支持表格、列表、加粗等格式"""
        if not content:
            return ''
        
        lines = content.split('\n')
        html = []
        
        in_list = False
        table_buffer = []
        in_table = False
        
        for line in lines:
            stripped = line.strip()
            
            # 检测表格行
            is_table_line = '|' in stripped and stripped.count('|') >= 3
            is_table_separator = is_table_line and all(c in '|:- ' for c in stripped)
            
            if is_table_line:
                if not in_table:
                    if in_list:
                        html.append('</ul>')
                        in_list = False
                    in_table = True
                table_buffer.append(stripped)
            elif in_table:
                # 表格结束
                if len(table_buffer) >= 3:
                    html.append(BaseTemplate._render_table(table_buffer))
                table_buffer = []
                in_table = False
                
                if not stripped:
                    continue
                
                # 处理当前行
                if stripped.startswith('- ') or stripped.startswith('* '):
                    if not in_list:
                        html.append('<ul class="mb-4">')
                        in_list = True
                    html.append(f'<li class="text-gray-700 mb-2 ml-4">{BaseTemplate._render_inline_markdown(stripped[2:].strip())}</li>')
                else:
                    if in_list:
                        html.append('</ul>')
                        in_list = False
                    html.append(f'<p class="text-gray-700 mb-4 leading-relaxed">{BaseTemplate._render_inline_markdown(stripped)}</p>')
            else:
                # 普通文本行
                if not stripped:
                    continue
                
                if stripped.startswith('- ') or stripped.startswith('* '):
                    if not in_list:
                        html.append('<ul class="mb-4">')
                        in_list = True
                    html.append(f'<li class="text-gray-700 mb-2 ml-4">{BaseTemplate._render_inline_markdown(stripped[2:].strip())}</li>')
                else:
                    if in_list:
                        html.append('</ul>')
                        in_list = False
                    html.append(f'<p class="text-gray-700 mb-4 leading-relaxed">{BaseTemplate._render_inline_markdown(stripped)}</p>')
        
        # 处理末尾状态
        if in_table and len(table_buffer) >= 3:
            html.append(BaseTemplate._render_table(table_buffer))
        if in_list:
            html.append('</ul>')
        
        return '\n'.join(html)
    
    @staticmethod
    def _render_table(table_lines: list) -> str:
        """渲染HTML表格"""
        headers = [h.strip() for h in table_lines[0].split('|')[1:-1]]
        
        rows = []
        for line in table_lines[2:]:
            cells = [c.strip() for c in line.split('|')[1:-1]]
            rows.append(cells)
        
        if not headers:
            return ''
        
        header_cells = ''.join([f'<th class="px-4 py-3 text-left text-sm font-semibold text-gray-700 bg-gray-50">{BaseTemplate._render_inline_markdown(h)}</th>' for h in headers])
        
        body_rows = []
        for row in rows:
            cells = ''.join([f'<td class="px-4 py-3 text-sm text-gray-600 border-t border-gray-100">{BaseTemplate._render_inline_markdown(c)}</td>' for c in row])
            body_rows.append(f'<tr class="hover:bg-gray-50">{cells}</tr>')
        
        return f'''
        <div class="bg-white rounded-xl shadow-lg overflow-hidden mb-6 border border-gray-100">
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
    
    @staticmethod
    def _render_inline_markdown(text: str) -> str:
        """渲染行内Markdown格式"""
        text = re.sub(r'\*\*(.+?)\*\*', r'<strong class="font-bold">\1</strong>', text)
        text = re.sub(r'\*(.+?)\*', r'<em>\1</em>', text)
        text = re.sub(r'`(.+?)`', r'<code class="bg-gray-100 px-1 rounded text-pink-600 text-sm">\1</code>', text)
        text = re.sub(r'\[(.+?)\]\((.+?)\)', r'<a href="\2" class="text-indigo-600 hover:underline">\1</a>', text)
        return text


class DailyNewsTemplate:
    """每日新闻洞察模板"""
    
    @staticmethod
    def render_section(title: str, content: str, section_type: str) -> str:
        """渲染新闻卡片"""
        news_items = DailyNewsTemplate._extract_news_items(content)
        
        cards_html = []
        for item in news_items[:8]:
            tags_html = ''.join([f'<span class="px-2 py-0.5 bg-indigo-100 text-indigo-700 text-xs rounded-full mx-0.5">{tag}</span>' for tag in item.get('tags', [])])
            
            cards_html.append(f'''
            <div class="bg-white rounded-2xl p-5 shadow-lg hover:shadow-xl transition-all mb-4">
                <div class="font-bold text-gray-800 mb-3 leading-snug text-lg">{item.get('title', title)}</div>
                <div class="flex items-center justify-between mb-3">
                    <div class="flex items-center space-x-3 text-sm text-gray-500">
                        <span>{item.get('source', '')}</span>
                        <span>{item.get('time', '')}</span>
                    </div>
                    <div class="flex items-center flex-wrap gap-1">
                        {tags_html}
                    </div>
                </div>
                <div class="text-gray-600 text-sm leading-relaxed">{BaseTemplate._render_inline_markdown(item.get('content', ''))}</div>
            </div>
            ''')
        
        icon = '📰'
        return f'''
        <div class="mb-8 mt-10">
            <div class="flex items-center space-x-3 mb-4">
                <span class="text-3xl">{icon}</span>
                <h2 class="text-2xl font-bold text-gray-800">{title}</h2>
            </div>
            <div class="h-1 w-24 bg-gradient-to-r from-indigo-500 to-purple-600 rounded-full mb-6 ml-1"></div>
            {''.join(cards_html)}
        </div>
        '''
    
    @staticmethod
    def _extract_news_items(content: str) -> list:
        """提取新闻条目"""
        items = []
        lines = content.split('\n')
        
        current_item = {'title': '', 'content': '', 'tags': [], 'source': '', 'time': ''}
        
        for line in lines:
            line = line.strip()
            if not line:
                continue
            
            # 新闻标题
            if line.startswith('- **') or line.startswith('* **'):
                if current_item['title']:
                    items.append(current_item.copy())
                title_match = re.search(r'\*\*(.+?)\*\*', line)
                current_item['title'] = title_match.group(1) if title_match else line
                current_item['content'] = ''
                current_item['tags'] = DailyNewsTemplate._extract_tags(line)
            
            # 新闻内容
            elif current_item['title']:
                if '来源' in line or 'Source' in line:
                    current_item['source'] = line.replace('来源：', '').replace('来源:', '')
                elif '时间' in line or 'Time' in line:
                    current_item['time'] = line.replace('时间：', '').replace('时间:', '')
                else:
                    current_item['content'] += ' ' + line
        
        if current_item['title']:
            items.append(current_item)
        
        return items
    
    @staticmethod
    def _extract_tags(text: str) -> list:
        """提取标签"""
        tags = []
        tag_patterns = ['AI', '算力', '芯片', '存储', 'HBM', 'MLCC', 'PCB', '机器人', '新能源', '汽车']
        for pattern in tag_patterns:
            if pattern in text:
                tags.append(pattern)
        return tags


class IntradayTemplate:
    """盘中快报模板 - 强调时效性"""
    
    @staticmethod
    def render_section(title: str, content: str, section_type: str) -> str:
        """渲染快报表单"""
        icon = '⚡'
        
        # 提取快讯
        items = []
        lines = content.split('\n')
        for line in lines:
            line = line.strip()
            if line and not line.startswith('##') and not line.startswith('###'):
                items.append(BaseTemplate._render_inline_markdown(line))
        
        timeline_html = []
        for i, item in enumerate(items[:10]):
            is_first = (i == 0)
            timeline_html.append(IntradayTemplate._render_timeline_item(item, is_first))
        
        return f'''
        <div class="mb-8 mt-10">
            <div class="flex items-center space-x-3 mb-4">
                <span class="text-3xl">{icon}</span>
                <h2 class="text-2xl font-bold text-gray-800">{title}</h2>
                <span class="px-3 py-1 bg-red-100 text-red-700 text-xs font-bold rounded-full animate-pulse">实时</span>
            </div>
            <div class="h-1 w-24 bg-gradient-to-r from-orange-500 to-red-600 rounded-full mb-6 ml-1"></div>
            
            <div class="bg-gradient-to-br from-orange-50 to-red-50 rounded-2xl p-6 border border-orange-200">
                {''.join(timeline_html)}
            </div>
        </div>
        '''
    
    @staticmethod
    def _render_timeline_item(content: str, is_first: bool = False) -> str:
        """渲染时间线条目"""
        return f'''
        <div class="relative pl-8 pb-5 {'pt-2' if is_first else ''}">
            <div class="absolute left-0 top-0 bottom-0 w-0.5 bg-gradient-to-b from-orange-500 to-red-500"></div>
            <div class="absolute left-0 top-2 w-4 h-4 rounded-full bg-gradient-to-br from-orange-500 to-red-600 -translate-x-1/2 ring-4 ring-orange-100"></div>
            <div class="text-gray-700 leading-relaxed">{content}</div>
        </div>
        '''


class AftermarketTemplate:
    """盘后速递模板 - 数据汇总"""
    
    @staticmethod
    def render_section(title: str, content: str, section_type: str) -> str:
        """渲染盘后数据 - 智能渲染Markdown"""
        icon = '📊'
        
        # 使用基础模板智能渲染内容
        content_html = BaseTemplate.render_content(content)
        
        return f'''
        <div class="mb-8 mt-10">
            <div class="flex items-center space-x-3 mb-4">
                <span class="text-3xl">{icon}</span>
                <h2 class="text-2xl font-bold text-gray-800">{title}</h2>
            </div>
            <div class="h-1 w-24 bg-gradient-to-r from-blue-500 to-indigo-600 rounded-full mb-6 ml-1"></div>
            
            <div class="bg-gradient-to-br from-blue-50 to-indigo-50 rounded-2xl p-6 border border-blue-200">
                {content_html}
            </div>
        </div>
        '''


class WeeklyReviewTemplate:
    """周复盘模板 - 完整回顾"""
    
    @staticmethod
    def render_section(title: str, content: str, section_type: str) -> str:
        """渲染周复盘 - 智能渲染Markdown"""
        if '持仓' in title or '操作' in title:
            bg_class = 'bg-gradient-to-br from-purple-50 to-pink-50 border-purple-200'
            icon = '💼'
        elif '风险' in title or '教训' in title:
            bg_class = 'bg-gradient-to-br from-red-50 to-orange-50 border-red-200'
            icon = '⚠️'
        elif '市场' in title or '行情' in title:
            bg_class = 'bg-gradient-to-br from-blue-50 to-cyan-50 border-blue-200'
            icon = '📈'
        else:
            bg_class = 'bg-gradient-to-br from-gray-50 to-slate-50 border-gray-200'
            icon = '📋'
        
        # 使用基础模板智能渲染内容
        content_html = BaseTemplate.render_content(content)
        
        return f'''
        <div class="mb-8 mt-10">
            <div class="flex items-center space-x-3 mb-4">
                <span class="text-3xl">{icon}</span>
                <h2 class="text-2xl font-bold text-gray-800">{title}</h2>
            </div>
            <div class="h-1 w-24 bg-gradient-to-r from-purple-500 to-pink-600 rounded-full mb-6 ml-1"></div>
            
            <div class="{bg_class} rounded-2xl p-6 border">
                {content_html}
            </div>
        </div>
        '''


# 模板映射
TEMPLATE_MAPPING = {
    'daily': DailyNewsTemplate,
    'intraday': IntradayTemplate,
    'aftermarket': AftermarketTemplate,
    'weekly_review': WeeklyReviewTemplate,
    'industry_chain': None  # 使用通用模板
}
