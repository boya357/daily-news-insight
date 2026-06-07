"""
周末速递生成器 - V3.0 高级版
周末资讯汇总 + 政策解读 + 下周题材预判
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.report import Report
from components.layout import Section, HighlightBox, SubCard, CardGrid, SplitLayout
from components.data import DataCard, DataGrid, StockTags, Badge, StatCard, Sparkline, Tabs, GaugeChart, ProgressBar
from components.special import RiskAlert, NewsItem


class WeekendExpressGenerator:
    """周末速递生成器 - V3.0高级版"""
    
    def __init__(self, date_str: str, subtitle: str = None):
        self.date_str = date_str
        self.subtitle = subtitle or f"{date_str} · 周末资讯速递"
        self.report = Report(
            title="周末速递",
            report_type="weekend_express",
            subtitle=self.subtitle
        )
        self._components = []
    
    def add_weekend_highlights(self, highlights: list):
        """添加周末要闻亮点"""
        content = '<div style="display: flex; flex-direction: column; gap: 10px;">'
        for h in highlights:
            content += f'''
            <div style="display: flex; padding: 12px 16px; 
                      background: #f8fafc; border-radius: 12px;">
                <span style="font-size: 16px; margin-right: 10px;">{h.get("icon", "📰")}</span>
                <div style="flex: 1;">
                    <div style="font-size: 13px; font-weight: 600; color: #1f2937; margin-bottom: 2px;">
                        {h.get("title", "")}
                    </div>
                    <div style="font-size: 12px; color: #6b7280;">
                        {h.get("content", "")}
                    </div>
                </div>
            </div>'''
        content += '</div>'
        
        section = Section(title="📰 周末要闻速览", content=content, icon="newspaper")
        self._components.append(section)
    
    def add_policy_interpretation(self, policies: list):
        """添加政策解读"""
        from components.icons import icon_svg
        
        content_html = '<div style="display: flex; flex-direction: column; gap: 14px;">'
        for policy in policies:
            content_html += f'''
            <div style="background: white; border: 1px solid rgba(0, 0, 0, 0.06);
                       border-radius: 14px; padding: 18px;
                       box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
                       border-left: 4px solid #3b82f6;">
                <div style="font-size: 15px; font-weight: 600; color: #1f2937; margin-bottom: 8px;">
                    {policy.get("title", "")}
                </div>
                <div style="font-size: 13px; color: #6b7280; line-height: 1.7; margin-bottom: 8px;">
                    {policy.get("content", "")}
                </div>
                <div style="font-size: 12px; color: #3b82f6; font-weight: 500;">
                    💡 影响解读：{policy.get("impact", "")}
                </div>
            </div>'''
        content_html += '</div>'
        
        section = Section(title="🏛️ 政策解读", content=content_html, icon="building")
        self._components.append(section)
    
    def add_next_week_topics(self, topics: list):
        """添加下周题材预判"""
        content_html = '<div style="display: flex; flex-direction: column; gap: 12px;">'
        for topic in topics:
            stocks_html = ''
            if topic.get('stocks'):
                tags = StockTags(topic['stocks'], label="受益标的")
                stocks_html = tags.render()
            
            content_html += f'''
            <div style="background: #f0fdf4; border: 1px solid #bbf7d0;
                       border-radius: 14px; padding: 16px;">
                <div style="display: flex; align-items: center; margin-bottom: 8px;">
                    <span style="font-size: 15px; font-weight: 600; color: #166534; flex: 1;">
                        {topic.get("name", "")}
                    </span>
                    <span style="padding: 3px 10px; border-radius: 20px; 
                               font-size: 11px; font-weight: 600;
                               background: #16a34a; color: white;">
                        {topic.get("probability", "高确定性")}
                    </span>
                </div>
                <div style="font-size: 13px; color: #15803d; line-height: 1.6; margin-bottom: 8px;">
                    {topic.get("logic", "")}
                </div>
                {stocks_html}
            </div>'''
        content_html += '</div>'
        
        section = Section(title="🔮 下周题材预判", content=content_html, icon="zap", variant="highlight")
        self._components.append(section)
    
    def add_risk_warning(self, risks: list):
        """添加风险提示"""
        risk_text = "；".join(risks) if isinstance(risks, list) else risks
        risk = RiskAlert(level="warning", title="⚠️ 风险提示", text=risk_text)
        self._components.append(risk)
    
    def add_trading_plan(self, plan: str):
        """添加下周操作计划"""
        content = f'<div style="line-height: 1.8; color: #374151; font-size: 14px;">{plan}</div>'
        section = Section(title="🎯 下周操作计划", content=content, icon="target")
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
