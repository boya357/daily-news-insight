"""
S级催化生成器 - V3.0 高级版
重大题材深度分析 + 产业链梳理 + 投资机会
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.report import Report
from components.layout import Section, HighlightBox, Card
from components.data import DataCard, DataGrid, KeyPoints, StockTags, CompareTable
from components.special import RiskAlert, QuoteBlock


class SLevelCatalystGenerator:
    """S级催化生成器 - V3.0高级版"""
    
    def __init__(self, date_str: str, catalyst_title: str = None, subtitle: str = None):
        self.date_str = date_str
        self.catalyst_title = catalyst_title or "重大催化事件"
        self.subtitle = subtitle or f"{date_str} · S级催化深度分析"
        self.report = Report(
            title="S级催化",
            report_type="s_level_catalyst",
            subtitle=self.subtitle
        )
        self._components = []
    
    def add_catalyst_overview(self, overview: str, importance: str = "高"):
        """添加催化事件概述"""
        box = HighlightBox(
            content=overview,
            icon="zap",
            variant="danger",
            title=f"⚡ S级催化 - {self.catalyst_title}"
        )
        self._components.append(box)
    
    def add_catalyst_details(self, background: str, trigger: str):
        """添加催化事件详细分析"""
        content = f'''
        <div style="display: flex; flex-direction: column; gap: 16px;">
            <div style="background: #f8fafc; border-radius: 14px; padding: 18px;">
                <div style="font-size: 14px; font-weight: 600; color: #1e293b; margin-bottom: 8px;">
                    📚 事件背景
                </div>
                <div style="font-size: 13px; color: #475569; line-height: 1.7;">
                    {background}
                </div>
            </div>
            <div style="background: #fef3c7; border-radius: 14px; padding: 18px;">
                <div style="font-size: 14px; font-weight: 600; color: #92400e; margin-bottom: 8px;">
                    🔥 触发因素
                </div>
                <div style="font-size: 13px; color: #b45309; line-height: 1.7;">
                    {trigger}
                </div>
            </div>
        </div>'''
        
        section = Section(title="🔍 催化事件详解", content=content, icon="search")
        self._components.append(section)
    
    def add_industry_chain_analysis(self, upstream: list, midstream: list, downstream: list):
        """添加产业链分析"""
        from components.icons import icon_svg
        
        def render_chain_layer(title, items, icon, color_from, color_to):
            items_html = ''
            for item in items:
                stocks_html = ''
                if item.get('stocks'):
                    tags = StockTags(item['stocks'], label="", )
                    stocks_html = tags.render()
                
                items_html += f'''
                <div style="background: white; border-radius: 12px; padding: 14px; 
                          box-shadow: 0 1px 3px rgba(0,0,0,0.05);">
                    <div style="font-size: 14px; font-weight: 600; color: #1f2937; margin-bottom: 6px;">
                        {item.get("name", "")}
                    </div>
                    <div style="font-size: 12px; color: #6b7280; line-height: 1.5; margin-bottom: 8px;">
                        {item.get("desc", "")}
                    </div>
                    {stocks_html}
                </div>'''
            
            return f'''
            <div style="margin-bottom: 16px;">
                <div style="display: flex; align-items: center; margin-bottom: 10px;">
                    <div style="width: 28px; height: 28px; 
                               background: linear-gradient(135deg, {color_from} 0%, {color_to} 100%); 
                               border-radius: 8px; display: flex; align-items: center; justify-content: center; 
                               margin-right: 10px;">
                        {icon_svg(icon, 14, "white")}
                    </div>
                    <span style="font-size: 14px; font-weight: 600; color: #374151;">{title}</span>
                </div>
                <div style="display: flex; flex-direction: column; gap: 8px; padding-left: 38px;">
                    {items_html}
                </div>
            </div>'''
        
        content = ''
        content += render_chain_layer("上游", upstream, "upstream", "#10b981", "#059669")
        content += render_chain_layer("中游", midstream, "layers", "#3b82f6", "#2563eb")
        content += render_chain_layer("下游", downstream, "downstream", "#f59e0b", "#d97706")
        
        section = Section(title="🔗 产业链梳理", content=content, icon="git-branch")
        self._components.append(section)
    
    def add_investment_opportunities(self, opportunities: list):
        """添加投资机会分析"""
        from components.icons import icon_svg
        
        content_html = '<div style="display: flex; flex-direction: column; gap: 14px;">'
        for opp in opportunities:
            priority = opp.get('priority', '高')
            priority_colors = {
                '高': ('#ef4444', '#fee2e2', '#991b1b'),
                '中': ('#f59e0b', '#fef3c7', '#92400e'),
                '低': ('#3b82f6', '#dbeafe', '#1e40af'),
            }
            p_color, p_bg, p_text = priority_colors.get(priority, priority_colors['中'])
            
            stocks_html = ''
            if opp.get('stocks'):
                tags = StockTags(opp['stocks'], label="核心标的")
                stocks_html = tags.render()
            
            content_html += f'''
            <div style="background: white; border: 1px solid rgba(0, 0, 0, 0.06);
                       border-radius: 16px; padding: 20px;
                       box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
                       border-left: 4px solid {p_color};">
                <div style="display: flex; align-items: center; margin-bottom: 10px;">
                    <div style="flex: 1;">
                        <span style="font-size: 16px; font-weight: 700; color: #1f2937;">
                            {opp.get("name", "")}
                        </span>
                    </div>
                    <span style="padding: 3px 10px; border-radius: 20px; 
                               font-size: 11px; font-weight: 700;
                               background: {p_bg}; color: {p_text};">
                        {priority}优先级
                    </span>
                </div>
                <div style="font-size: 13px; color: #6b7280; line-height: 1.7; margin-bottom: 10px;">
                    {opp.get("logic", "")}
                </div>
                {stocks_html}
            </div>'''
        content_html += '</div>'
        
        section = Section(title="💰 投资机会分析", content=content_html, icon="dollar-sign")
        self._components.append(section)
    
    def add_risk_warning(self, risks: list):
        """添加风险提示"""
        risk = RiskAlert(level="danger", title="⚠️ 重要风险提示", text="；".join(risks) if isinstance(risks, list) else risks)
        self._components.append(risk)
    
    def add_investment_strategy(self, strategy: str):
        """添加投资策略建议"""
        content = f'<div style="line-height: 1.8; color: #374151; font-size: 14px;">{strategy}</div>'
        section = Section(title="🎯 投资策略建议", content=content, icon="target", variant="highlight")
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

    def publish(self, title=None, report_type=None, filename=None, excerpt=None, auto_deploy=True, docs_root="docs"):
        """一键发布"""
        html_content = self.generate()
        import sys, os
        sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        from workflow import ReportPublisher
        rtype = report_type or self.report.report_type
        display_title = title or self.report.title or rtype
        publisher = ReportPublisher(docs_root=docs_root)
        return publisher.publish(html_content=html_content, title=display_title, report_type=rtype, filename=filename, excerpt=excerpt, auto_deploy=auto_deploy)
