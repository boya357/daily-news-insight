#!/usr/bin/env python3
"""
Markdown智能解析器
识别报告结构、章节、组件类型
"""
import re
from typing import Dict, List, Any, Optional


class MarkdownParser:
    """智能Markdown解析器"""
    
    def __init__(self):
        self.sections = []
        self.metadata = {}
    
    def parse(self, md_content: str) -> Dict[str, Any]:
        """解析完整的Markdown内容"""
        lines = md_content.split('\n')
        
        result = {
            'title': '',
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
                if current_section:
                    current_section['content'] = '\n'.join(current_content)
                    result['sections'].append(current_section)
                title = line[2:].strip()
                result['title'] = title
                current_section = None
                current_content = []
            
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
                if current_section:
                    if current_content:
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
            
            # 四级标题 = 小节标题
            elif line.startswith('#### '):
                subsection_title = line[5:].strip()
                if current_section:
                    current_section.setdefault('subsections', []).append({
                        'title': subsection_title,
                        'type': self._detect_section_type(subsection_title)
                    })
            
            # 其他内容
            else:
                if line.strip():
                    current_content.append(line)
        
        # 处理最后一个章节
        if current_section:
            current_section['content'] = '\n'.join(current_content)
            result['sections'].append(current_section)
        
        # 提取元数据
        result['metadata'] = self._extract_metadata(result['sections'])
        
        return result
    
    def _detect_section_type(self, title: str) -> str:
        """根据标题检测章节类型"""
        title_lower = title.lower()
        
        type_patterns = {
            'core_summary': ['核心结论', '核心观点', '投资要点', '核心摘要', '核心判断'],
            'market_review': ['市场回顾', '行情回顾', '大盘表现', '市场概览'],
            'industry_chain': ['产业链全景', '产业链分析', '行业分析', '产业链梳理'],
            'stock_analysis': ['标的分析', '个股分析', '核心标的', '弹性测算', '业绩弹性'],
            'catalyst': ['催化剂', '催化因素', '事件日历', '前瞻'],
            'risk': ['风险提示', '风险因素', '免责声明'],
            'chart': ['图表', '对比图', '统计图', '走势图'],
            'table': ['表格', '一览表', '清单', '对比表'],
            'timeline': ['时间线', '事件时间线', '时间轴'],
            'news': ['新闻汇总', '重要新闻', '新闻动态', '热点追踪']
        }
        
        for section_type, patterns in type_patterns.items():
            for pattern in patterns:
                if pattern in title or pattern.lower() in title_lower:
                    return section_type
        
        return 'general'
    
    def _extract_metadata(self, sections: List[Dict]) -> Dict[str, Any]:
        """从章节内容中提取元数据"""
        metadata = {
            'date': '',
            'author': '',
            'tags': []
        }
        
        # 从标题或内容提取日期
        for section in sections:
            content = section.get('content', '')
            date_match = re.search(r'(\d{4}年\d{1,2}月\d{1,2}日|\d{4}-\d{2}-\d{2})', content)
            if date_match:
                metadata['date'] = date_match.group(1)
                break
        
        return metadata
    
    def parse_table(self, table_content: str) -> Dict[str, Any]:
        """解析Markdown表格"""
        lines = [line.strip() for line in table_content.split('\n') if line.strip()]
        lines = [line for line in lines if line.startswith('|')]
        
        if len(lines) < 3:
            return {'headers': [], 'rows': []}
        
        # 解析表头
        headers = [h.strip() for h in lines[0].split('|')[1:-1]]
        
        # 解析数据行
        rows = []
        for line in lines[2:]:
            cells = [c.strip() for c in line.split('|')[1:-1]]
            rows.append(cells)
        
        return {'headers': headers, 'rows': rows}
    
    def detect_component_type(self, content: str) -> str:
        """检测内容块应该渲染成什么组件"""
        if '|' in content and content.count('|') > 3:
            return 'table'
        if '✅' in content or '❌' in content or '⚠️' in content:
            return 'risk_alert'
        if content.count('**') > 4:
            return 'highlight_box'
        if '→' in content or '➡️' in content or len(re.findall(r'\d{2}:\d{2}', content)) > 2:
            return 'timeline'
        return 'text'
