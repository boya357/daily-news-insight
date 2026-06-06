"""
月报生成器 - V3.0
月度总结 + 下月展望
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.report import Report
from components.layout import Section
from components.data import DataCard, DataGrid
from components.special import RiskAlert


class MonthlyReportGenerator:
    """月报生成器"""
    
    def __init__(self, month_str: str, subtitle: str = None):
        self.month_str = month_str
        self.subtitle = subtitle or f"{month_str} · 月度投资报告"
        self.report = Report(
            title="月度报告",
            report_type="monthly",
            subtitle=self.subtitle
        )
        self._components = []
    
    def add_month_overview(self, overview: str):
        """月度概览"""
        section = Section(
            title="📊 月度概览",
            content=f'<div class="prose-content"><p>{overview}</p></div>',
            variant="highlight"
        )
        self._components.append(section)
    
    def add_market_performance(self, indices: list):
        """市场表现"""
        cards = []
        for idx in indices:
            variant = "success" if idx.get('up', True) else "danger"
            cards.append(DataCard(
                title=idx['name'],
                value=idx.get('monthly_change', ''),
                trend=idx.get('current', ''),
                trend_up=idx.get('up', True),
                variant=variant
            ))
        
        grid = DataGrid(cards, cols=min(len(cards), 4))
        
        section = Section(
            title="📈 月度市场表现",
            content=grid.render()
        )
        self._components.append(section)
    
    def add_sector_review(self, sectors: list):
        """板块回顾"""
        content_html = '<div class="space-y-3">'
        for s in sectors:
            change_class = 'text-green-600' if s.get('up', True) else 'text-red-600'
            content_html += f'''
            <div class="flex items-center justify-between p-4 bg-gray-50 rounded-xl">
                <span class="font-medium text-gray-800">{s["name"]}</span>
                <span class="font-bold {change_class}">{s.get("change", "")}</span>
            </div>
            '''
        content_html += '</div>'
        
        section = Section(
            title="🏭 板块表现",
            content=content_html
        )
        self._components.append(section)
    
    def add_key_events_review(self, events: list):
        """重要事件回顾"""
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
            title="📅 重要事件回顾",
            content=content_html
        )
        self._components.append(section)
    
    def add_next_month_outlook(self, outlook: str):
        """下月展望"""
        section = Section(
            title="🔮 下月展望",
            content=f'<div class="prose-content"><p>{outlook}</p></div>'
        )
        self._components.append(section)
    
    def add_investment_strategy(self, strategy: str):
        """投资策略"""
        section = Section(
            title="🎯 投资策略",
            content=f'<div class="prose-content"><p>{strategy}</p></div>',
            variant="highlight"
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

