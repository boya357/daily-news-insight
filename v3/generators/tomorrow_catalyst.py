"""
明日催化剂生成器 - V3.0 高级版
次日重要事件 + 业绩公告 + 数据发布
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.report import Report
from components.layout import Section, HighlightBox
from components.data import DataCard, DataGrid, StockTags
from components.special import RiskAlert


class TomorrowCatalystGenerator:
    """明日催化剂生成器 - V3.0高级版"""
    
    def __init__(self, date_str: str, subtitle: str = None):
        self.date_str = date_str
        self.subtitle = subtitle or f"{date_str} · 明日催化事件"
        self.report = Report(
            title="明日催化剂",
            report_type="tomorrow_catalyst",
            subtitle=self.subtitle
        )
        self._components = []
    
    def add_key_catalyst(self, catalyst: str):
        """添加核心催化剂"""
        box = HighlightBox(content=catalyst, icon="zap", variant="warning", title="明日核心催化")
        self._components.append(box)
    
    def add_events_calendar(self, events: list):
        """添加明日事件日历"""
        from components.icons import icon_svg
        
        content_html = '<div style="display: flex; flex-direction: column; gap: 10px;">'
        for event in events:
            event_type = event.get('type', 'general')
            type_colors = {
                'policy': ('#3b82f6', '#dbeafe', '#1e40af'),
                'data': ('#10b981', '#dcfce7', '#166534'),
                'earnings': ('#f59e0b', '#fef3c7', '#92400e'),
                'meeting': ('#8b5cf6', '#ede9fe', '#6d28d9'),
                'general': ('#6b7280', '#f3f4f6', '#374151'),
            }
            icon_color, bg_color, text_color = type_colors.get(event_type, type_colors['general'])
            
            content_html += f'''
            <div style="background: white; border: 1px solid rgba(0, 0, 0, 0.06);
                       border-radius: 12px; padding: 14px 16px;
                       display: flex; align-items: flex-start;
                       box-shadow: 0 1px 3px rgba(0, 0, 0, 0.04);">
                <div style="width: 32px; height: 32px; 
                           background: linear-gradient(135deg, {icon_color} 0%, {text_color} 100%); 
                           border-radius: 8px; display: flex; align-items: center; justify-content: center; 
                           margin-right: 12px; flex-shrink: 0;">
                    {icon_svg("calendar", 16, "white")}
                </div>
                <div style="flex: 1;">
                    <div style="font-size: 14px; font-weight: 600; color: #1f2937; margin-bottom: 4px;">
                        {event.get("title", "")}
                    </div>
                    <div style="font-size: 12px; color: #6b7280; line-height: 1.5;">
                        {event.get("description", "")}
                    </div>
                    <div style="margin-top: 6px;">
                        <span style="display: inline-block; padding: 2px 8px; 
                                   border-radius: 6px; background: {bg_color}; 
                                   color: {text_color}; font-size: 11px; font-weight: 500;">
                            {event.get("category", "事件")}
                        </span>
                    </div>
                </div>
            </div>'''
        content_html += '</div>'
        
        section = Section(title="📅 明日事件日历", content=content_html, icon="calendar")
        self._components.append(section)
    
    def add_earnings_announcements(self, stocks: list):
        """添加业绩公告"""
        content_html = '<div style="display: flex; flex-direction: column; gap: 8px;">'
        for stock in stocks:
            content_html += f'''
            <div style="display: flex; align-items: center; padding: 12px 16px; 
                      background: #f8fafc; border-radius: 12px;">
                <div style="flex: 1;">
                    <span style="font-size: 14px; font-weight: 500; color: #1f2937;">{stock["name"]}</span>
                    <span style="font-size: 12px; color: #9ca3af; margin-left: 6px;">{stock.get("code", "")}</span>
                </div>
                <span style="font-size: 12px; padding: 3px 8px; border-radius: 6px; 
                           background: #fef3c7; color: #92400e;">
                    {stock.get("type", "业绩预告")}
                </span>
            </div>'''
        content_html += '</div>'
        
        section = Section(title="💰 业绩公告", content=content_html, icon="dollar-sign")
        self._components.append(section)
    
    def add_data_release(self, data_list: list):
        """添加重要数据发布"""
        content_html = '<div style="display: flex; flex-direction: column; gap: 8px;">'
        for data in data_list:
            content_html += f'''
            <div style="display: flex; align-items: center; padding: 12px 16px; 
                      background: #f0fdf4; border-radius: 12px;">
                <div style="flex: 1;">
                    <span style="font-size: 14px; font-weight: 500; color: #166534;">{data["name"]}</span>
                </div>
                <span style="font-size: 12px; color: #15803d;">
                    前值：{data.get("prev", "")} / 预期：{data.get("expect", "")}
                </span>
            </div>'''
        content_html += '</div>'
        
        section = Section(title="📊 重要数据发布", content=content_html, icon="bar-chart")
        self._components.append(section)
    
    def add_impact_analysis(self, impact: str):
        """添加市场影响分析"""
        content = f'<div style="line-height: 1.8; color: #374151; font-size: 14px;">{impact}</div>'
        section = Section(title="🔍 市场影响分析", content=content, icon="search", variant="highlight")
        self._components.append(section)
    
    def add_risk_warning(self, risks: list):
        """添加风险提示"""
        risk_text = "；".join(risks) if isinstance(risks, list) else risks
        risk = RiskAlert(level="warning", title="⚠️ 风险提示", text=risk_text)
        self._components.append(risk)
    
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
