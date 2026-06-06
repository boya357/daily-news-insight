"""
周复盘生成器 - V3.0 高级版
一周市场总结 + 热点回顾 + 下周展望
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.report import Report
from components.layout import Section, HighlightBox
from components.data import DataCard, DataGrid, KeyPoints, StockTags
from components.special import RiskAlert, NewsItem, Timeline


class WeeklyReviewGenerator:
    """周复盘生成器 - V3.0高级版"""
    
    def __init__(self, date_str: str, week_num: str = None, subtitle: str = None):
        self.date_str = date_str
        self.week_num = week_num or ""
        self.subtitle = subtitle or f"{date_str} · 周度复盘"
        self.report = Report(
            title="周复盘",
            report_type="weekly_review",
            subtitle=self.subtitle
        )
        self._components = []
    
    def add_week_summary(self, summary: str):
        """添加本周核心总结"""
        box = HighlightBox(content=summary, icon="check-circle", variant="primary", title="本周核心总结")
        self._components.append(box)
    
    def add_market_review(self, indices: list):
        """添加本周市场表现"""
        cards = []
        for idx in indices:
            variant = "success" if idx.get('up', True) else "danger"
            cards.append(DataCard(
                title=idx['name'],
                value=idx.get('current', ''),
                trend=idx.get('change', ''),
                trend_up=idx.get('up', True),
                variant=variant,
                subtitle=idx.get('subtitle', '')
            ))
        
        grid = DataGrid(cards, cols=min(len(cards), 4))
        section = Section(title="📊 本周市场表现", content=grid.render(), icon="chart")
        self._components.append(section)
    
    def add_hot_topics_review(self, topics: list):
        """添加本周热点题材回顾"""
        from components.icons import icon_svg
        
        content_html = '<div style="display: flex; flex-direction: column; gap: 14px;">'
        for i, topic in enumerate(topics):
            stocks_html = ''
            if topic.get('stocks'):
                stock_tags = StockTags(topic['stocks'], label="龙头标的")
                stocks_html = stock_tags.render()
            
            content_html += f'''
            <div style="background: white; border: 1px solid rgba(0, 0, 0, 0.06);
                       border-radius: 16px; padding: 20px;
                       box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
                       transition: all 0.3s ease;"
                 onmouseover="this.style.transform='translateY(-2px)'; this.style.boxShadow='0 8px 24px rgba(0, 0, 0, 0.08)';"
                 onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 2px 8px rgba(0, 0, 0, 0.04)';">
                <div style="display: flex; align-items: center; margin-bottom: 12px;">
                    <div style="width: 36px; height: 36px; background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%); 
                               border-radius: 10px; display: flex; align-items: center; justify-content: center; 
                               margin-right: 12px; flex-shrink: 0;
                               box-shadow: 0 4px 12px rgba(79, 70, 229, 0.25);">
                        {icon_svg("topic", 18, "white")}
                    </div>
                    <div style="flex: 1;">
                        <div style="font-size: 16px; font-weight: 700; color: #1f2937;">
                            <span style="display: inline-block; width: 22px; height: 22px; border-radius: 50%; 
                                       background: #4f46e5; color: white; font-size: 12px; font-weight: 700;
                                       text-align: center; line-height: 22px; margin-right: 8px;">{i+1}</span>
                            {topic.get("name", "")}
                        </div>
                    </div>
                    <span style="padding: 4px 10px; border-radius: 20px; font-size: 12px; font-weight: 600;
                               background: #f0fdf4; color: #059669;">
                        {topic.get("performance", "")}
                    </span>
                </div>
                <div style="font-size: 13px; color: #6b7280; line-height: 1.7; margin-bottom: 8px;">
                    {topic.get("logic", "")}
                </div>
                {stocks_html}
            </div>'''
        content_html += '</div>'
        
        section = Section(title="🔥 本周热点题材回顾", content=content_html, icon="flame")
        self._components.append(section)
    
    def add_important_events(self, events: list):
        """添加本周重要事件时间线"""
        timeline = Timeline(events)
        section = Section(title="📅 本周重要事件", content=timeline.render(), icon="calendar")
        self._components.append(section)
    
    def add_holdings_review(self, holdings: list):
        """添加持仓周度回顾"""
        content_html = '<div style="display: flex; flex-direction: column; gap: 12px;">'
        for h in holdings:
            change_color = "#10b981" if h.get('up', True) else "#ef4444"
            
            content_html += f'''
            <div style="background: #fafafa; border-radius: 14px; padding: 16px 18px;">
                <div style="display: flex; align-items: center;">
                    <div style="flex: 1;">
                        <div style="display: flex; align-items: center; margin-bottom: 4px;">
                            <span style="font-size: 15px; font-weight: 600; color: #1f2937;">{h["name"]}</span>
                            <span style="font-size: 12px; color: #9ca3af; margin-left: 8px;">{h.get("code", "")}</span>
                        </div>
                        <div style="font-size: 12px; color: #6b7280; line-height: 1.5;">
                            周{h.get("change_type", "涨")}幅：{h.get("weekly_change", "")}
                        </div>
                    </div>
                    <div style="text-align: right;">
                        <div style="font-size: 18px; font-weight: 700; color: {change_color};">{h.get("price", "")}</div>
                        <div style="font-size: 13px; font-weight: 500; color: {change_color};">{h.get("weekly_change", "")}</div>
                    </div>
                </div>
                <div style="font-size: 12px; color: #6b7280; line-height: 1.6; margin-top: 8px; padding-top: 8px; border-top: 1px dashed #e5e7eb;">
                    💡 {h.get("comment", "")}
                </div>
            </div>'''
        content_html += '</div>'
        
        section = Section(title="💼 持仓周度回顾", content=content_html, icon="briefcase")
        self._components.append(section)
    
    def add_next_week_outlook(self, outlook: str):
        """添加下周展望"""
        content = f'<div style="line-height: 1.8; color: #374151; font-size: 14px;">{outlook}</div>'
        section = Section(title="🔮 下周市场展望", content=content, icon="compass", variant="highlight")
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
