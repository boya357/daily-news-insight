"""
明日催化剂生成器 - V3.0
明日重要事件、财经日历、催化事件
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.report import Report
from components.layout import Section
from components.special import CatalystTag, Timeline


class TomorrowCatalystGenerator:
    """明日催化剂生成器"""
    
    def __init__(self, date_str: str, subtitle: str = None):
        self.date_str = date_str
        sub = subtitle or f"{date_str} · 明日投资日历"
        self.report = Report(title="明日催化剂", report_type="tomorrow_catalyst", subtitle=sub)
        self._components = []
    
    def add_key_events(self, events: list):
        """添加重点催化事件"""
        content_html = '<div class="space-y-4">'
        for event in events:
            impact = event.get('impact', '中')
            impact_color_map = {
                '高': 'bg-red-100 text-red-800',
                '中': 'bg-amber-100 text-amber-800',
                '低': 'bg-gray-100 text-gray-800'
            }
            impact_color = impact_color_map.get(impact, 'bg-gray-100 text-gray-800')
            
            title = event.get("title", "")
            event_content = event.get("content", "")
            
            # 生成板块标签
            sector_tags = ''
            for tag in event.get("sectors", []):
                sector_tags += f'<span class="text-xs px-2 py-1 bg-indigo-50 text-indigo-600 rounded">{tag}</span>'
            
            content_html += '<div class="bg-white border border-gray-100 rounded-xl p-5 shadow-sm">'
            content_html += '<div class="flex items-center justify-between mb-2">'
            content_html += f'<h4 class="font-bold text-gray-800">{title}</h4>'
            content_html += f'<span class="text-xs px-2 py-1 rounded-full {impact_color}">影响{impact}</span>'
            content_html += '</div>'
            content_html += f'<p class="text-gray-600 text-sm mb-3">{event_content}</p>'
            content_html += f'<div class="flex gap-2 flex-wrap">{sector_tags}</div>'
            content_html += '</div>'
        content_html += '</div>'
        
        section = Section(title="⭐ 重点催化事件", content=content_html)
        self._components.append(section)
    
    def add_economic_calendar(self, items: list):
        """添加财经日历"""
        content_html = '<div class="space-y-3">'
        for item in items:
            importance = item.get('importance', '中')
            dot_color_map = {
                '高': 'bg-red-500',
                '中': 'bg-amber-500',
                '低': 'bg-gray-400'
            }
            dot_color = dot_color_map.get(importance, 'bg-gray-400')
            
            time = item.get("time", "")
            event_title = item.get("event", "")
            country = item.get("country", "")
            
            content_html += '<div class="flex items-start space-x-4 p-3 bg-gray-50 rounded-lg">'
            content_html += f'<span class="text-indigo-600 font-mono font-bold text-sm">{time}</span>'
            content_html += f'<span class="w-2 h-2 rounded-full {dot_color} mt-2 flex-shrink-0"></span>'
            content_html += '<div class="flex-1">'
            content_html += f'<span class="text-gray-800 font-medium">{event_title}</span>'
            content_html += f'<span class="text-gray-400 text-sm ml-2">{country}</span>'
            content_html += '</div></div>'
        content_html += '</div>'
        
        section = Section(title="📅 财经日历", content=content_html)
        self._components.append(section)
    
    def add_sector_catalysts(self, sectors: list):
        """添加板块催化"""
        from components.data import DataGrid, DataCard
        
        cards = []
        for s in sectors:
            cards.append(DataCard(
                title=s['name'],
                value=s.get('catalyst', ''),
                trend=s.get('impact', ''),
                trend_up=s.get('positive', True),
                variant="primary"
            ))
        
        grid = DataGrid(cards, cols=min(len(cards), 3))
        section = Section(title="🏭 板块催化", content=grid.render())
        self._components.append(section)
    
    def add_notice(self, notice: str):
        """添加特别提醒"""
        from components.special import RiskAlert
        alert = RiskAlert(level="info", title="特别提醒", text=notice)
        self._components.append(alert)
    
    def generate(self) -> str:
        """生成完整HTML"""
        for comp in self._components:
            self.report.add(comp)
        return self.report.generate()
    
    def save(self, filepath: str) -> str:
        """保存到文件"""
        self.generate()
        return self.report.save(filepath)
    
    def validate(self) -> list:
        """验证报告"""
        self.generate()
        return self.report.validate()

    def publish(self, title: str = None, report_type: str = None, 
                filename: str = None, excerpt: str = None,
                auto_deploy: bool = True, docs_root: str = "docs") -> dict:
        """
        一键发布：生成 → 归档 → 更新列表 → 校验 → Git部署
        
        Args:
            title: 报告标题（用于列表页显示）
            report_type: 报告类型（对应REPORT_TYPES的key），默认使用self.report.report_type
            filename: 文件名，不传则自动生成
            excerpt: 摘要（用于列表页展示）
            auto_deploy: 是否自动Git部署
            docs_root: docs目录路径
            
        Returns:
            发布结果字典
        """
        html_content = self.generate()
        
        import sys
        import os
        sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        from workflow import ReportPublisher
        
        rtype = report_type or self.report.report_type
        display_title = title or self.report.title or rtype
        
        publisher = ReportPublisher(docs_root=docs_root)
        return publisher.publish(
            html_content=html_content,
            title=display_title,
            report_type=rtype,
            filename=filename,
            excerpt=excerpt,
            auto_deploy=auto_deploy
        )

