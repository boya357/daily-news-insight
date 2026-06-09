"""
盘中快报生成器 - V3.0 高级版
午间市场数据 + 热点解析 + 操作策略
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.report import Report
from components.layout import Section, Card, HighlightBox, SubCard, CardGrid, SplitLayout
from components.data import DataCard, DataGrid, KeyPoints, StockTags, MetricsRow, Badge, StatCard, Sparkline, Tabs, GaugeChart, ProgressBar
from components.special import RiskAlert, NewsItem


class IntradayGenerator:
    """
    盘中快报生成器 - V3.0高级版
    
    使用方法:
    gen = IntradayGenerator("2026年6月6日")
    gen.add_market_overview(indices, market_status)
    gen.add_hot_topics(topics)
    gen.add_holdings_tracking(holdings)
    gen.add_trading_strategy(strategy)
    gen.save("output.html")
    """
    
    def __init__(self, date_str: str, subtitle: str = None):
        self.date_str = date_str
        self.subtitle = subtitle or f"{date_str} · 午盘速递"
        self.report = Report(
            title="盘中快报",
            report_type="intraday",
            subtitle=self.subtitle
        )
        self._components = []
    
    def add_focus_point(self, focus: str):
        """添加午盘焦点"""
        box = HighlightBox(
            content=focus,
            icon="zap",
            variant="warning",
            title="午盘焦点"
        )
        self._components.append(box)
    
    def add_market_overview(self, indices: list, market_status: str = "震荡", sparkline_data: dict = None):
        """添加市场概览（V3.0增强版：渐变统计卡）
        
        Args:
            indices: [{"name": "上证指数", "value": "3,200.50", "change": "+0.52%", "up": True}, ...]
            market_status: 市场状态（上涨/下跌/震荡）
            sparkline_data: 各指数迷你走势数据（可选）
        """
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
        
        # 市场状态标签
        status_colors = {"上涨": "success", "下跌": "danger", "震荡": "warning"}
        status_variant = status_colors.get(market_status, "default")
        status_badge = Badge(text=f"市场状态：{market_status}", variant=status_variant)
        
        content = grid.render() + '<div style="margin-top: 12px;">' + status_badge.render() + '</div>'
        section = Section(title="📈 市场概览", content=content, icon="trending-up")
        self._components.append(section)

    def add_hot_topics(self, topics: list):
        """
        添加市场热点解析
        
        Args:
            topics: 热点列表 [{"tag": "AI", "title": "...", "content": "...", "hot": True, "stocks": [...]}, ...]
        """
        from components.icons import icon_svg
        
        content_html = '<div style="display: flex; flex-direction: column; gap: 14px;">'
        for topic in topics:
            is_hot = topic.get('hot', False)
            tag = topic.get('tag', '热点')
            
            stocks_html = ''
            if topic.get('stocks'):
                stock_tags = StockTags(topic['stocks'], label="相关标的")
                stocks_html = stock_tags.render()
            
            hot_badge = ''
            if is_hot:
                hot_badge = '''
                <span style="padding: 3px 10px; border-radius: 20px; 
                           font-size: 11px; font-weight: 700;
                           background: linear-gradient(135deg, #ef4444 0%, #f97316 100%); 
                           color: white; flex-shrink: 0;">
                    🔥 热门
                </span>
                '''
            
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
                    <div style="width: 36px; height: 36px; 
                               background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%); 
                               border-radius: 10px; 
                               display: flex; align-items: center; justify-content: center; 
                               margin-right: 12px; flex-shrink: 0;
                               box-shadow: 0 4px 12px rgba(79, 70, 229, 0.25);">
                        {icon_svg("topic", 18, "white")}
                    </div>
                    <div style="flex: 1;">
                        <div style="font-size: 16px; font-weight: 700; color: #1f2937;">
                            <span style="display: inline-block; padding: 2px 8px; 
                                       border-radius: 6px; background: #eef2ff; 
                                       color: #4f46e5; font-size: 12px; font-weight: 600;
                                       margin-right: 8px;">{tag}</span>
                            {topic.get("title", "")}
                        </div>
                    </div>
                    {hot_badge}
                </div>
                <div style="font-size: 13px; color: #6b7280; line-height: 1.7; margin-bottom: 8px;">
                    {topic.get("content", "")}
                </div>
                {stocks_html}
            </div>
            '''
        content_html += '</div>'
        
        section = Section(
            title="🔥 市场热点解析",
            content=content_html,
            icon="flame"
        )
        self._components.append(section)
    
    def add_decline_sectors(self, sectors: list):
        """
        添加领跌板块警示
        
        Args:
            sectors: 领跌板块列表 [{"name": "新能源", "change": "-2.5%", "reason": "..."}, ...]
        """
        content_html = '<div style="display: flex; flex-direction: column; gap: 12px;">'
        for sector in sectors:
            content_html += f'''
            <div style="background: linear-gradient(135deg, #fef2f2 0%, #fee2e2 100%); 
                       border: 1px solid rgba(239, 68, 68, 0.1);
                       border-radius: 14px; 
                       padding: 16px 18px;">
                <div style="display: flex; align-items: center; margin-bottom: 6px;">
                    <span style="font-size: 15px; font-weight: 600; color: #991b1b; flex: 1;">
                        {sector["name"]}
                    </span>
                    <span style="font-size: 14px; font-weight: 700; color: #dc2626;">
                        {sector.get("change", "")}
                    </span>
                </div>
                <div style="font-size: 12px; color: #b91c1c; line-height: 1.5;">
                    💡 {sector.get("reason", "")}
                </div>
            </div>
            '''
        content_html += '</div>'
        
        section = Section(
            title="⚠️ 领跌板块警示",
            content=content_html,
            icon="alert-triangle"
        )
        self._components.append(section)
    
    def add_holdings_tracking(self, holdings: list):
        """
        添加持仓股跟踪
        
        Args:
            holdings: 持仓列表 [{"name": "英维克", "code": "002837", "price": "25.50", "change": "+1.2%", "up": True, "comment": "..."}, ...]
        """
        content_html = '<div style="display: flex; flex-direction: column; gap: 12px;">'
        for h in holdings:
            change_class = "#10b981" if h.get('up', True) else "#ef4444"
            name = h["name"]
            code = h.get("code", "")
            price = h.get("price", "")
            change = h.get("change", "")
            comment = h.get("comment", "")
            
            content_html += f'''
            <div style="background: #fafafa; border-radius: 14px; padding: 16px 18px;">
                <div style="display: flex; align-items: center;">
                    <div style="flex: 1;">
                        <div style="display: flex; align-items: center; margin-bottom: 4px;">
                            <span style="font-size: 15px; font-weight: 600; color: #1f2937;">
                                {name}
                            </span>
                            <span style="font-size: 12px; color: #9ca3af; margin-left: 8px;">
                                {code}
                            </span>
                        </div>
                        <div style="font-size: 12px; color: #6b7280; line-height: 1.5; max-width: 400px;">
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
            </div>
            '''
        content_html += '</div>'
        
        section = Section(
            title="💼 持仓股跟踪",
            content=content_html,
            icon="briefcase"
        )
        self._components.append(section)
    
    def add_trading_strategy(self, strategy: str):
        """
        添加午盘操作策略
        
        Args:
            strategy: 操作策略内容
        """
        content = f'''
        <div style="line-height: 1.8; color: #374151; font-size: 14px;">
            {strategy}
        </div>
        '''
        section = Section(
            title="🎯 午盘操作策略",
            content=content,
            icon="target",
            variant="highlight"
        )
        self._components.append(section)
    
    def add_risk_warning(self, risks: list):
        """
        添加风险提示
        
        Args:
            risks: 风险提示列表
        """
        risk_text = "；".join(risks) if isinstance(risks, list) else risks
        risk = RiskAlert(
            level="warning",
            title="⚠️ 风险提示",
            text=risk_text
        )
        self._components.append(risk)
    
    def add_summary(self, summary: str):
        """
        添加市场逻辑总结
        
        Args:
            summary: 总结内容
        """
        content = f'''
        <div style="line-height: 1.8; color: #374151; font-size: 14px;">
            {summary}
        </div>
        '''
        section = Section(
            title="📝 市场逻辑总结",
            content=content,
            icon="book"
        )
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

    def publish(self, title: str = None, report_type: str = None, 
                filename: str = None, excerpt: str = None,
                auto_deploy: bool = True, docs_root: str = "docs") -> dict:
        """
        一键发布：生成 → 归档 → 更新列表 → 校验 → Git部署
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
