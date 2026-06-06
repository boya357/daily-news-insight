"""
周三前瞻生成器 - V3.0
周中展望 + 后半周机会分析
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.report import Report
from components.layout import Section
from components.special import RiskAlert


class WeeklyOutlookGenerator:
    """周三前瞻生成器"""
    
    def __init__(self, date_str: str, subtitle: str = None):
        self.date_str = date_str
        self.subtitle = subtitle or f"{date_str} · 周中展望"
        self.report = Report(
            title="周三前瞻",
            report_type="weekly_outlook",
            subtitle=self.subtitle
        )
        self._components = []
    
    def add_halfweek_review(self, review: str):
        """前半周回顾"""
        section = Section(
            title="📊 前半周回顾",
            content=f'<div class="prose-content"><p>{review}</p></div>'
        )
        self._components.append(section)
    
    def add_second_half_outlook(self, outlook: str):
        """后半周展望"""
        section = Section(
            title="🔮 后半周展望",
            content=f'<div class="prose-content"><p>{outlook}</p></div>',
            variant="highlight"
        )
        self._components.append(section)
    
    def add_key_events(self, events: list):
        """后半周重要事件"""
        content_html = '<div class="space-y-3">'
        for event in events:
            content_html += f'''
            <div class="flex items-start p-3 bg-gray-50 rounded-lg">
                <span class="text-indigo-600 font-mono text-sm mr-3">{event.get("date", "")}</span>
                <div class="flex-1">
                    <strong class="text-gray-800">{event.get("title", "")}</strong>
                    <p class="text-gray-500 text-sm mt-1">{event.get("content", "")}</p>
                </div>
            </div>
            '''
        content_html += '</div>'
        
        section = Section(
            title="📅 重要事件日历",
            content=content_html
        )
        self._components.append(section)
    
    def add_opportunity_focus(self, opportunities: list):
        """机会关注点"""
        content_html = '<div class="space-y-4">'
        for opp in opportunities:
            content_html += f'''
            <div class="border border-gray-100 rounded-xl p-5">
                <h4 class="font-bold text-gray-800 mb-2">{opp.get("name", "")}</h4>
                <p class="text-gray-600 text-sm">{opp.get("logic", "")}</p>
            </div>
            '''
        content_html += '</div>'
        
        section = Section(
            title="🎯 机会关注点",
            content=content_html
        )
        self._components.append(section)
    
    def add_risk_warning(self, risks: list):
        """风险提示"""
        risk_text = "；".join(risks) if isinstance(risks, list) else risks
        risk = RiskAlert(
            level="warning",
            title="⚠️ 风险提示",
            text=risk_text
        )
        self._components.append(risk)
    
    def add_operation_strategy(self, strategy: str):
        """操作策略"""
        section = Section(
            title="📋 操作策略",
            content=f'<div class="prose-content"><p>{strategy}</p></div>'
        )
        self._components.append(section)
    
    def generate(self) -> str:
        for comp in self._components:
            self.report.add(comp)
        return self.report.generate()
    
    def save(self, filepath: str) -> str:
        self.generate()
        return self.report.save(filepath)
    
    def validate(self) -> list:
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

