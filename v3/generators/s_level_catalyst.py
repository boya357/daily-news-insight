"""
S级催化生成器 - V3.0
超级催化事件深度分析
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.report import Report
from components.layout import Section
from components.data import DataCard, DataGrid
from components.special import RiskAlert


class SLevelCatalystGenerator:
    """
    S级催化生成器
    
    使用方法:
    gen = SLevelCatalystGenerator("AI算力行业超级催化")
    gen.add_catalyst_overview(overview)
    gen.add_impact_analysis(impact)
    gen.add_beneficiary_stocks(stocks)
    gen.add_risk_warning(risks)
    gen.save("output.html")
    """
    
    def __init__(self, title: str, subtitle: str = None):
        self.catalyst_title = title
        self.subtitle = subtitle or "S级超级催化事件"
        self.report = Report(
            title="S级催化",
            report_type="s_level_catalyst",
            subtitle=subtitle
        )
        self._components = []
    
    def add_catalyst_overview(self, overview: str, event_date: str = None, 
                              impact_level: str = "S级"):
        """
        添加催化事件概述
        """
        date_html = f'<p class="text-gray-500 text-sm mt-2">📅 事件时间：{event_date}</p>' if event_date else ''
        level_html = f'<span class="bg-red-100 text-red-800 text-xs px-2 py-1 rounded-full">{impact_level}</span>'
        
        content = f'''
        <div class="text-center py-6">
            {level_html}
            <h3 class="text-xl font-bold text-gray-800 mt-3">{self.catalyst_title}</h3>
            <div class="text-gray-600 mt-4 prose-content"><p>{overview}</p></div>
            {date_html}
        </div>
        '''
        
        section = Section(
            title="⭐ 催化事件概述",
            content=content
        )
        self._components.append(section)
    
    def add_impact_analysis(self, impact: str, dimensions: list = None):
        """
        添加影响分析
        
        Args:
            impact: 影响分析正文
            dimensions: 影响维度列表 [{"name": "行业影响", "level": "高", "desc": "..."}, ...]
        """
        dim_html = ''
        if dimensions:
            dim_html = '<div class="grid grid-cols-2 md:grid-cols-3 gap-4 mt-6">'
            for d in dimensions:
                level = d.get('level', '中')
                level_color = {
                    '高': 'bg-red-100 text-red-800',
                    '中': 'bg-amber-100 text-amber-800',
                    '低': 'bg-gray-100 text-gray-800'
                }.get(level, 'bg-gray-100 text-gray-800')
                
                dim_html += f'''
                <div class="bg-gray-50 rounded-xl p-4 text-center">
                    <div class="font-bold text-gray-800 mb-1">{d["name"]}</div>
                    <span class="text-xs px-2 py-1 rounded-full {level_color}">{level}</span>
                    <p class="text-gray-500 text-sm mt-2">{d.get("desc", "")}</p>
                </div>
                '''
            dim_html += '</div>'
        
        content = f'<div class="prose-content"><p>{impact}</p></div>{dim_html}'
        
        section = Section(
            title="📊 影响深度分析",
            content=content
        )
        self._components.append(section)
    
    def add_beneficiary_stocks(self, stocks: list):
        """
        添加受益标的分析
        
        Args:
            stocks: [{"name": "...", "code": "...", "logic": "...", "elasticity": "高", "rating": "推荐"}, ...]
        """
        content_html = '<div class="space-y-4">'
        for s in stocks:
            elasticity = s.get('elasticity', '中')
            elas_color = {
                '高': 'bg-red-100 text-red-800',
                '中': 'bg-amber-100 text-amber-800',
                '低': 'bg-green-100 text-green-800'
            }.get(elasticity, 'bg-gray-100 text-gray-800')
            
            rating = s.get('rating', '关注')
            rating_color = {
                '强烈推荐': 'bg-green-100 text-green-800',
                '推荐': 'bg-blue-100 text-blue-800',
                '关注': 'bg-amber-100 text-amber-800',
                '谨慎': 'bg-red-100 text-red-800',
            }.get(rating, 'bg-gray-100 text-gray-800')
            
            content_html += f'''
            <div class="border border-gray-100 rounded-xl p-5 hover:shadow-md transition-shadow">
                <div class="flex items-center justify-between mb-3">
                    <div>
                        <span class="font-bold text-lg text-gray-800">{s["name"]}</span>
                        <span class="text-gray-400 text-sm ml-2">{s.get("code", "")}</span>
                    </div>
                    <div class="flex gap-2">
                        <span class="text-xs px-2 py-1 rounded-full {elas_color}">弹性{elasticity}</span>
                        <span class="text-xs px-2 py-1 rounded-full {rating_color}">{rating}</span>
                    </div>
                </div>
                <p class="text-gray-600 text-sm">💡 {s.get("logic", "")}</p>
            </div>
            '''
        content_html += '</div>'
        
        section = Section(
            title="🎯 核心受益标的",
            content=content_html
        )
        self._components.append(section)
    
    def add_timeline_analysis(self, stages: list):
        """
        添加催化时间线分析
        """
        from components.special import Timeline
        
        timeline = Timeline(
            title="催化时间线",
            items=stages
        )
        self._components.append(timeline)
    
    def add_risk_warning(self, risks: list):
        """添加风险提示"""
        risk_text = "；".join(risks) if isinstance(risks, list) else risks
        risk = RiskAlert(
            level="danger",
            title="⚠️ 风险提示",
            text=risk_text
        )
        self._components.append(risk)
    
    def add_investment_strategy(self, strategy: str):
        """添加投资策略建议"""
        section = Section(
            title="📋 投资策略建议",
            content=f'<div class="prose-content"><p>{strategy}</p></div>',
            variant="highlight"
        )
        self._components.append(section)
    
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

