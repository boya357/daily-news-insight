"""
周三前瞻生成器 - V3.0 高级版
周中展望 + 题材预判 + 操作策略
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.report import Report
from components.layout import Section, HighlightBox
from components.data import DataCard, DataGrid, StockTags
from components.special import RiskAlert, NewsItem


class WeeklyOutlookGenerator:
    """周三前瞻生成器 - V3.0高级版"""
    
    def __init__(self, date_str: str, subtitle: str = None):
        self.date_str = date_str
        self.subtitle = subtitle or f"{date_str} · 周中展望"
        self.report = Report(
            title="周三前瞻",
            report_type="weekly_outlook",
            subtitle=self.subtitle
        )
        self._components = []
    
    def add_midweek_summary(self, summary: str):
        """添加周中总结"""
        box = HighlightBox(content=summary, icon="activity", variant="primary", title="周中核心观察")
        self._components.append(box)
    
    def add_market_status(self, indices: list):
        """添加当前市场状态（V3.0增强版：渐变统计卡）"""
        cards = []
        for idx in indices:
            variant = "success" if idx.get('up', True) else "danger"
            cards.append(StatCard(
                title=idx['name'],
                value=idx.get('value', ''),
                subtitle=idx.get('change', ''),
                icon=idx.get('icon', 'trending_up'),
                variant=variant,
                trend=idx.get('change', ''),
                trend_up=idx.get('up', True)
            ))
        
        grid = CardGrid(cards, cols=min(len(cards), 4))
        section = Section(title="📊 周中市场概览", content=grid.render(), icon="chart")
        self._components.append(section)
    
    def add_focus_topics(self, topics: list):
        """添加重点关注题材"""
        from components.icons import icon_svg
        
        content_html = '<div style="display: flex; flex-direction: column; gap: 12px;">'
        for topic in topics:
            stocks_html = ''
            if topic.get('stocks'):
                tags = StockTags(topic['stocks'], label="关注标的")
                stocks_html = tags.render()
            
            content_html += f'''
            <div style="background: rgba(30,30,50,0.5); border: 1px solid rgba(255,255,255,0.08);
                       border-radius: 14px; padding: 16px 18px;
                       box-shadow: 0 2px 8px rgba(0,0,0,0.2);">
                <div style="display: flex; align-items: center; margin-bottom: 8px;">
                    <div style="width: 32px; height: 32px; 
                               background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%); 
                               border-radius: 8px; display: flex; align-items: center; justify-content: center; 
                               margin-right: 10px; flex-shrink: 0;">
                        {icon_svg("eye", 16, "white")}
                    </div>
                    <div style="flex: 1;">
                        <span style="font-size: 15px; font-weight: 600; color: #f1f5f9;">{topic.get("name", "")}</span>
                    </div>
                    <span style="padding: 3px 10px; border-radius: 20px; 
                               font-size: 11px; font-weight: 600;
                               background: rgba(245,158,11,0.15); color: #fbbf24;">
                        {topic.get("attention", "重点关注")}
                    </span>
                </div>
                <div style="font-size: 13px; color: #94a3b8; line-height: 1.6; margin-bottom: 8px;">
                    {topic.get("logic", "")}
                </div>
                {stocks_html}
            </div>'''
        content_html += '</div>'
        
        section = Section(title="👁️ 重点关注题材", content=content_html, icon="eye")
        self._components.append(section)
    
    def add_second_half_strategy(self, strategy: str):
        """添加下半周操作策略"""
        content = f'<div style="line-height: 1.8; color: #e2e8f0; font-size: 14px;">{strategy}</div>'
        section = Section(title="🎯 下半周操作策略", content=content, icon="target", variant="highlight")
        self._components.append(section)
    
    def add_risk_warning(self, risks: list):
        """添加风险提示"""
        risk_text = "；".join(risks) if isinstance(risks, list) else risks
        risk = RiskAlert(level="warning", title="⚠️ 风险提示", text=risk_text)
        self._components.append(risk)
    
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
