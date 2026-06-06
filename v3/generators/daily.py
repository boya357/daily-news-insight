"""
每日新闻洞察生成器 - V3.0 高级版
最核心、最高频的报告类型
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.report import Report
from components.layout import Section, Card, HighlightBox
from components.data import DataCard, DataGrid, KeyPoints, StockTags, MetricsRow, Badge
from components.special import RiskAlert, NewsItem


class DailyReportGenerator:
    """每日新闻洞察生成器 - V3.0高级版"""
    
    def __init__(self, date_str: str, weekday: str = None, subtitle: str = None):
        self.date_str = date_str
        self.weekday = weekday or ""
        sub = subtitle or f"{date_str} {weekday} · 龙空龙策略专用"
        self.report = Report(title="每日新闻洞察", report_type="daily", subtitle=sub)
        self._components = []
    
    def add_focus_point(self, focus: str):
        """添加今日焦点"""
        box = HighlightBox(
            content=focus,
            icon="zap",
            variant="warning",
            title="今日焦点"
        )
        self._components.append(box)
    
    def add_overseas_market(self, indices: list, key_events: list = None):
        """添加隔夜全球市场
        
        Args:
            indices: [{"name": "道琼斯", "value": "39,876.54", "change": "+0.52%", "up": True, "icon": "trending_up"}, ...]
            key_events: [{"tag": "重磅", "title": "...", "content": "...", "tag_color": "red"}, ...]
        """
        cards = []
        for idx in indices:
            variant = "success" if idx.get('up', True) else "danger"
            cards.append(DataCard(
                title=idx['name'],
                value=idx.get('value', ''),
                trend=idx.get('change', ''),
                trend_up=idx.get('up', True),
                variant=variant
            ))
        
        grid = DataGrid(cards, cols=len(cards))
        
        events_html = ''
        if key_events:
            events_html = '<div style="margin-top: 20px;">'
            for event in key_events:
                tag = event.get('tag', '重磅')
                tag_color = event.get('tag_color', 'red')
                
                events_html += f'''
                <div style="display: flex; margin-bottom: 16px; 
                          padding: 14px 16px; 
                          background: #fafafa; border-radius: 12px;">
                    <div style="margin-right: 12px;">
                        <span style="display: inline-block; 
                                   padding: 2px 8px; 
                                   border-radius: 8px; 
                                   font-size: 11px; 
                                   font-weight: 700;
                                   background: #fee2e2; 
                                   color: #dc2626;
                                   flex-shrink: 0;">
                            {tag}
                        </span>
                    </div>
                    <div style="flex: 1;">
                        <div style="font-size: 14px; font-weight: 600; 
                                   color: #1f2937; margin-bottom: 4px;">
                            {event.get("title", "")}
                        </div>
                        <div style="font-size: 13px; color: #6b7280; line-height: 1.6;">
                            {event.get("content", "")}
                        </div>
                    </div>
                </div>
                '''
            events_html += '</div>'
        
        content = grid.render() + events_html
        section = Section(title="🌍 隔夜全球市场", content=content, icon="globe")
        self._components.append(section)
    
    def add_import_news(self, news_list: list):
        """添加重要新闻汇总
        
        Args:
            news_list: [{"tag": "AI", "importance": "high", "title": "...", "content": "...", "source": "财联社", "time": "08:30"}, ...]
        """
        news_html = '<div style="display: flex; flex-direction: column;">'
        for news in news_list:
            importance = news.get('importance', 'normal')
            tag = news.get('tag', '要闻')
            
            item = NewsItem(
                title=news.get("title", ""),
                content=news.get("content", ""),
                time=news.get("time", ""),
                source=news.get("source", ""),
                tag=tag,
                tag_variant="primary" if importance == "high" else "default",
                important=(importance == "high")
            )
            news_html += item.render()
        news_html += '</div>'
        
        section = Section(title="📰 重要新闻汇总", content=news_html, icon="news")
        self._components.append(section)
    
    def add_sector_analysis(self, sectors: list):
        """添加板块机会分析
        
        Args:
            sectors: [{"name": "AI算力", "rating": "强烈推荐", "stocks": [...], "logic": "...", "icon": "chip"}, ...]
        """
        from ..components.icons import icon_svg
        
        content_html = '<div style="display: flex; flex-direction: column; gap: 14px;">'
        for sector in sectors:
            rating = sector.get('rating', '关注')
            rating_colors = {
                '强烈推荐': ('bg-gradient-to-r from-green-500 to-emerald-600', 'white'),
                '推荐': ('bg-gradient-to-r from-blue-500 to-indigo-600', 'white'),
                '关注': ('bg-gradient-to-r from-amber-500 to-orange-600', 'white'),
                '谨慎': ('bg-gradient-to-r from-red-500 to-rose-600', 'white'),
            }
            r_bg, r_color = rating_colors.get(rating, rating_colors['关注'])
            
            stock_tags = StockTags(sector.get("stocks", []), label="相关标的")
            
            sector_icon = sector.get('icon', 'sector')
            
            content_html += f'''
            <div style="background: white; 
                       border: 1px solid rgba(0, 0, 0, 0.06);
                       border-radius: 16px; 
                       padding: 20px;
                       box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
                       transition: all 0.3s ease;"
                 onmouseover="this.style.transform='translateY(-2px)'; this.style.boxShadow='0 8px 24px rgba(0, 0, 0, 0.08)';"
                 onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 2px 8px rgba(0, 0, 0, 0.04)';">
                <div style="display: flex; align-items: center; margin-bottom: 12px;">
                    <div style="width: 40px; height: 40px; 
                               background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%); 
                               border-radius: 12px; 
                               display: flex; align-items: center; justify-content: center; 
                               margin-right: 14px; flex-shrink: 0;
                               box-shadow: 0 4px 12px rgba(79, 70, 229, 0.25);">
                        {icon_svg(sector_icon, 20, "white")}
                    </div>
                    <div style="flex: 1;">
                        <div style="font-size: 17px; font-weight: 700; color: #1f2937;">
                            {sector["name"]}
                        </div>
                    </div>
                    <span style="padding: 5px 12px; border-radius: 20px; 
                               font-size: 12px; font-weight: 700;
                               background: {r_bg}; color: {r_color};">
                        {rating}
                    </span>
                </div>
                <div style="font-size: 13px; color: #6b7280; line-height: 1.7; 
                           margin-bottom: 4px;">
                    💡 {sector.get("logic", "")}
                </div>
                {stock_tags.render()}
            </div>
            '''
        content_html += '</div>'
        
        section = Section(title="🎯 板块机会分析", content=content_html, icon="sector")
        self._components.append(section)
    
    def add_holdings_tracking(self, holdings: list):
        """添加持仓跟踪
        
        Args:
            holdings: [{"name": "英维克", "code": "002837", "price": "68.32", "change": "-5.23%", "up": False, "comment": "..."}, ...]
        """
        from ..components.icons import icon_svg
        
        content_html = '<div style="display: flex; flex-direction: column; gap: 12px;">'
        for h in holdings:
            change_class = "#10b981" if h.get('up', True) else "#ef4444"
            name = h["name"]
            code = h.get("code", "")
            price = h.get("price", "")
            change = h.get("change", "")
            comment = h.get("comment", "")
            
            content_html += f'''
            <div style="background: #fafafa; border-radius: 14px; padding: 16px 18px;
                       display: flex; align-items: center;">
                <div style="flex: 1;">
                    <div style="display: flex; align-items: center; margin-bottom: 4px;">
                        <span style="font-size: 15px; font-weight: 600; color: #1f2937;">
                            {name}
                        </span>
                        <span style="font-size: 12px; color: #9ca3af; margin-left: 8px;">
                            {code}
                        </span>
                    </div>
                    <div style="font-size: 12px; color: #6b7280; line-height: 1.5; 
                              max-width: 400px;">
                        {comment}
                    </div>
                </div>
                <div style="text-align: right;">
                    <div style="font-size: 18px; font-weight: 700; color: {change_class};">
                        {price}
                    </div>
                    <div style="font-size: 13px; font-weight: 500; color: {change_class};">
                        {change}
                    </div>
                </div>
            </div>
            '''
        content_html += '</div>'
        
        section = Section(title="💼 持仓跟踪", content=content_html, icon="briefcase")
        self._components.append(section)
    
    def add_risk_warning(self, risks: list):
        """添加风险提示"""
        if isinstance(risks, list):
            risk_text = "；".join(risks)
        else:
            risk_text = risks
        
        risk = RiskAlert(level="warning", title="⚠️ 风险提示", text=risk_text)
        self._components.append(risk)
    
    def add_daily_summary(self, summary: str):
        """添加每日总结"""
        content = f'''
        <div style="line-height: 1.8; color: #374151; font-size: 14px;">
            {summary}
        </div>
        '''
        section = Section(title="📝 今日总结", content=content, icon="book", variant="highlight")
        self._components.append(section)
    
    def add_tomorrow_plan(self, plan: str):
        """添加明日操作计划"""
        content = f'''
        <div style="line-height: 1.8; color: #374151; font-size: 14px;">
            {plan}
        </div>
        '''
        section = Section(title="🎯 明日计划", content=content, icon="target")
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
        """一键发布"""
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
