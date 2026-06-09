"""
月报生成器 - V3.0 高级版
月度市场总结 + 大类资产表现 + 下月展望
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.report import Report
from components.layout import Section, HighlightBox
from components.data import DataCard, DataGrid, StockTags
from components.special import RiskAlert


class MonthlyReportGenerator:
    """月报生成器 - V3.0高级版"""
    
    def __init__(self, date_str: str, month: str = None, subtitle: str = None):
        self.date_str = date_str
        self.month = month or date_str
        self.subtitle = subtitle or f"{self.month} · 月度投资报告"
        self.report = Report(
            title="月报",
            report_type="monthly",
            subtitle=self.subtitle
        )
        self._components = []
    
    def add_month_summary(self, summary: str):
        """添加月度核心总结"""
        box = HighlightBox(content=summary, icon="award", variant="primary", title="月度核心总结")
        self._components.append(box)
    
    def add_market_performance(self, indices: list):
        """添加市场表现（V3.0增强版：渐变统计卡）"""
        cards = []
        for idx in indices:
            variant = "success" if idx.get('up', True) else "danger"
            cards.append(StatCard(
                title=idx['name'],
                value=idx.get('current', ''),
                subtitle=idx.get('change', ''),
                icon=idx.get('icon', 'trending_up'),
                variant=variant,
                trend=idx.get('change', ''),
                trend_up=idx.get('up', True)
            ))
        
        grid = CardGrid(cards, cols=min(len(cards), 4))
        section = Section(title="📊 指数表现", content=grid.render(), icon="chart")
        self._components.append(section)
    
    def add_sector_review(self, sectors: list):
        """添加行业板块回顾"""
        content_html = '<div style="display: flex; flex-direction: column; gap: 10px;">'
        for sector in sectors:
            change_color = "#10b981" if sector.get('up', True) else "#ef4444"
            content_html += f'''
            <div style="background: white; border: 1px solid rgba(0, 0, 0, 0.06);
                       border-radius: 12px; padding: 14px 16px;
                       box-shadow: 0 1px 3px rgba(0, 0, 0, 0.04);">
                <div style="display: flex; align-items: center; margin-bottom: 6px;">
                    <span style="font-size: 14px; font-weight: 600; color: #1f2937; flex: 1;">
                        {sector["name"]}
                    </span>
                    <span style="font-size: 14px; font-weight: 600; color: {change_color};">
                        {sector.get("change", "")}
                    </span>
                </div>
                <div style="font-size: 12px; color: #6b7280; line-height: 1.5;">
                    {sector.get("comment", "")}
                </div>
            </div>'''
        content_html += '</div>'
        
        section = Section(title="🏢 行业板块回顾", content=content_html, icon="building")
        self._components.append(section)
    
    def add_asset_allocation(self, assets: list):
        """添加大类资产表现"""
        content_html = '<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px;">'
        for asset in assets:
            change_color = "#10b981" if asset.get('up', True) else "#ef4444"
            content_html += f'''
            <div style="background: #f8fafc; border-radius: 12px; padding: 14px;">
                <div style="font-size: 13px; color: #6b7280; margin-bottom: 4px;">{asset["name"]}</div>
                <div style="font-size: 18px; font-weight: 700; color: {change_color};">{asset.get("change", "")}</div>
                <div style="font-size: 11px; color: #9ca3af; margin-top: 2px;">{asset.get("note", "")}</div>
            </div>'''
        content_html += '</div>'
        
        section = Section(title="💼 大类资产表现", content=content_html, icon="pie-chart")
        self._components.append(section)
    
    def add_next_month_outlook(self, outlook: str):
        """添加下月展望"""
        content = f'<div style="line-height: 1.8; color: #374151; font-size: 14px;">{outlook}</div>'
        section = Section(title="🔮 下月市场展望", content=content, icon="compass", variant="highlight")
        self._components.append(section)
    
    def add_risk_warning(self, risks: list):
        """添加风险提示"""
        risk_text = "；".join(risks) if isinstance(risks, list) else risks
        risk = RiskAlert(level="warning", title="⚠️ 风险提示", text=risk_text)
        self._components.append(risk)
    
    def add_investment_strategy(self, strategy: str):
        """添加月度投资策略"""
        content = f'<div style="line-height: 1.8; color: #374151; font-size: 14px;">{strategy}</div>'
        section = Section(title="🎯 月度投资策略", content=content, icon="target")
        self._components.append(section)
    
    def generate(self) -> str:
        """生成完整HTML"""
        self.report.components.clear()  # 清空避免重复添加
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
