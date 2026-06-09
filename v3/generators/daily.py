"""
每日新闻洞察生成器 - V3.0 精致增强版
最核心、最高频的报告类型
已整合：StatCard渐变统计卡、SplitLayout分栏、SubCard嵌套卡片、CardGrid网格、Sparkline迷你图、Tabs标签页、全局动效
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.report import Report
from components.layout import Section, Card, HighlightBox, SubCard, CardGrid, SplitLayout, ChartCard
from components.data import DataCard, DataGrid, KeyPoints, StockTags, MetricsRow, Badge, StatCard, Sparkline, Tabs, GaugeChart, ProgressBar
from components.special import RiskAlert, NewsItem


class DailyReportGenerator:
    """每日新闻洞察生成器 - V3.0精致增强版"""
    
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
    
    def add_overseas_market(self, indices: list, key_events: list = None, sparkline_data: dict = None):
        """添加隔夜全球市场（V3.0增强版：渐变统计卡 + 迷你走势图）
        
        Args:
            indices: [{"name": "道琼斯", "value": "39,876.54", "change": "+0.52%", "up": True, "icon": "trending_up"}, ...]
            key_events: [{"tag": "重磅", "title": "...", "content": "...", "tag_color": "red"}, ...]
            sparkline_data: {"道琼斯": [value1, value2, ...], ...} 各指数的迷你走势数据（可选）
        """
        cards = []
        for idx in indices:
            variant = "success" if idx.get('up', True) else "danger"
            name = idx['name']
            
            # 迷你图（如果有数据）
            spark_html = ""
            if sparkline_data and name in sparkline_data:
                spark = Sparkline(
                    data=sparkline_data[name],
                    width=100,
                    height=30,
                    color="#10b981" if idx.get('up', True) else "#ef4444",
                    fill=True
                )
                spark_html = spark.render()
            
            cards.append(StatCard(
                title=name,
                value=idx.get('value', ''),
                subtitle=idx.get('change', ''),
                icon=idx.get('icon', 'trending_up'),
                variant=variant,
                trend=idx.get('change', ''),
                trend_up=idx.get('up', True)
            ))
        
        grid = CardGrid(cards, cols=min(len(cards), 4))
        
        events_html = ''
        if key_events:
            events_html = '<div style="margin-top: 20px;">'
            for event in key_events:
                tag = event.get('tag', '重磅')
                tag_color = event.get('tag_color', 'red')
                
                events_html += f'''
                <div style="display: flex; margin-bottom: 16px; 
                          padding: 14px 16px; 
                          background: #fafafa; border-radius: 12px;
                          transition: all 0.3s ease;"
                     onmouseover="this.style.transform='translateY(-2px)'; this.style.boxShadow='0 4px 12px rgba(0,0,0,0.06)';"
                     onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='none';">
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
    
    def add_market_sentiment(self, sentiment_score: float, risk_level: str, volume_ratio: float = None):
        """添加市场情绪仪表盘（V3.0新增）
        
        Args:
            sentiment_score: 情绪分数 0-100
            risk_level: 风险等级（低/中/高）
            volume_ratio: 量比（可选）
        """
        # 情绪仪表盘
        gauge = GaugeChart(
            value=sentiment_score,
            max_value=100,
            label="市场情绪",
            size=140,
            stroke_width=10,
            color=None  # 自动根据分数变色
        )
        
        # 风险等级卡片
        risk_colors = {"低": "success", "中": "warning", "高": "danger"}
        risk_variant = risk_colors.get(risk_level, "warning")
        risk_card = StatCard(
            title="风险等级",
            value=risk_level,
            subtitle="当前评估",
            icon="shield",
            variant=risk_variant
        )
        
        # 量比卡片（可选）
        volume_card_html = ""
        if volume_ratio is not None:
            vol_variant = "success" if volume_ratio > 1 else "default"
            vol_card = StatCard(
                title="量比",
                value=str(volume_ratio),
                subtitle="相对昨日",
                icon="bar-chart",
                variant=vol_variant
            )
            volume_card_html = vol_card.render()
        
        content = f'''
        <div style="display: flex; align-items: center; justify-content: center; gap: 30px; flex-wrap: wrap;">
            <div style="text-align: center;">
                {gauge.render()}
            </div>
            <div style="display: flex; flex-direction: column; gap: 12px; min-width: 180px;">
                {risk_card.render()}
                {volume_card_html}
            </div>
        </div>
        '''
        
        section = Section(title="📊 市场情绪", content=content, icon="activity")
        self._components.append(section)
    
    def add_import_news(self, news_list: list, category_tabs: bool = False):
        """添加重要新闻汇总（V3.0增强版：支持标签页分类）
        
        Args:
            news_list: [{"tag": "AI", "importance": "high", "title": "...", "content": "...", "source": "财联社", "time": "08:30", "category": "宏观"}, ...]
            category_tabs: 是否按分类用标签页展示
        """
        if category_tabs:
            # 按分类分组
            categories = {}
            for news in news_list:
                cat = news.get('category', '其他')
                if cat not in categories:
                    categories[cat] = []
                categories[cat].append(news)
            
            tab_list = []
            for cat, cat_news in categories.items():
                news_html = '<div style="display: flex; flex-direction: column;">'
                for news in cat_news:
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
                tab_list.append((cat, news_html))
            
            tabs = Tabs(tabs=tab_list, default_index=0)
            content = tabs.render()
        else:
            # 原有列表模式
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
            content = news_html
        
        section = Section(title="📰 重要新闻汇总", content=content, icon="news")
        self._components.append(section)
    
    def add_sector_analysis(self, sectors: list, view_mode: str = "card"):
        """添加板块机会分析（V3.0增强版：SubCard嵌套卡片 + 标签页分类）
        
        Args:
            sectors: [{"name": "AI算力", "rating": "强烈推荐", "stocks": [...], "logic": "...", "icon": "chip", "category": "科技"}, ...]
            view_mode: "card"（卡片模式）或 "tab"（标签页模式）
        """
        from components.icons import icon_svg
        
        if view_mode == "tab":
            # 按分类标签页展示
            categories = {}
            for sector in sectors:
                cat = sector.get('category', '其他')
                if cat not in categories:
                    categories[cat] = []
                categories[cat].append(sector)
            
            tab_list = []
            for cat, cat_sectors in categories.items():
                content_html = self._render_sector_cards(cat_sectors)
                tab_list.append((cat, content_html))
            
            tabs = Tabs(tabs=tab_list, default_index=0)
            content = tabs.render()
        else:
            # 卡片列表模式（增强版SubCard）
            content = self._render_sector_cards(sectors)
        
        section = Section(title="🎯 板块机会分析", content=content, icon="sector")
        self._components.append(section)
    
    def _render_sector_cards(self, sectors: list) -> str:
        """渲染板块卡片列表（内部方法）"""
        from components.icons import icon_svg
        
        content_html = '<div style="display: flex; flex-direction: column; gap: 14px;">'
        for sector in sectors:
            rating = sector.get('rating', '关注')
            rating_colors = {
                '强烈推荐': ('success', 'white'),
                '推荐': ('primary', 'white'),
                '关注': ('warning', 'white'),
                '谨慎': ('danger', 'white'),
            }
            r_variant, _ = rating_colors.get(rating, rating_colors['关注'])
            
            stock_tags = StockTags(sector.get("stocks", []), label="相关标的")
            sector_icon = sector.get('icon', 'sector')
            
            # 使用SubCard组件替代硬编码
            header_html = f'''
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
                           background: {self._get_rating_bg(rating)}; color: white;">
                    {rating}
                </span>
            </div>
            <div style="font-size: 13px; color: #6b7280; line-height: 1.7; 
                       margin-bottom: 4px;">
                💡 {sector.get("logic", "")}
            </div>
            {stock_tags.render()}
            '''
            
            sub_card = SubCard(
                content=header_html,
                variant="white"
            )
            content_html += sub_card.render()
        
        content_html += '</div>'
        return content_html
    
    def _get_rating_bg(self, rating: str) -> str:
        """获取评级背景色"""
        colors = {
            '强烈推荐': 'linear-gradient(135deg, #10b981 0%, #059669 100%)',
            '推荐': 'linear-gradient(135deg, #3b82f6 0%, #2563eb 100%)',
            '关注': 'linear-gradient(135deg, #f59e0b 0%, #d97706 100%)',
            '谨慎': 'linear-gradient(135deg, #ef4444 0%, #dc2626 100%)',
        }
        return colors.get(rating, colors['关注'])
    
    def add_holdings_tracking(self, holdings: list, position_info: dict = None):
        """添加持仓跟踪（V3.0增强版：左右分栏 + 仓位仪表盘）
        
        Args:
            holdings: [{"name": "英维克", "code": "002837", "price": "68.32", "change": "-5.23%", "up": False, "comment": "...", "ratio": 30}, ...]
            position_info: {"total": 85, "cash": 15, "risk_level": "中"} 仓位信息（可选）
        """
        from components.icons import icon_svg
        
        # 左侧：持仓列表
        holdings_html = '<div style="display: flex; flex-direction: column; gap: 12px;">'
        for h in holdings:
            change_class = "#10b981" if h.get('up', True) else "#ef4444"
            name = h["name"]
            code = h.get("code", "")
            price = h.get("price", "")
            change = h.get("change", "")
            comment = h.get("comment", "")
            ratio = h.get("ratio", None)
            
            # 仓位占比进度条（可选）
            ratio_html = ""
            if ratio is not None:
                pb = ProgressBar(
                    value=ratio,
                    max_value=100,
                    label=f"仓位 {ratio}%",
                    variant="primary",
                    show_percent=False,
                    height="4px"
                )
                ratio_html = f'<div style="margin-top: 8px;">{pb.render()}</div>'
            
            holdings_html += f'''
            <div style="background: #fafafa; border-radius: 14px; padding: 16px 18px;
                       display: flex; align-items: center;
                       transition: all 0.3s ease;"
                 onmouseover="this.style.background='#'f0f9ff';this.style.transform='translateX(4px)';"
                 onmouseout="this.style.background='#'fafafa';this.style.transform='translateX(0)';">
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
                              max-width: 300px;">
                        {comment}
                    </div>
                    {ratio_html}
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
        holdings_html += '</div>'
        
        # 右侧：仓位分析（如果有数据）
        if position_info:
            total_pos = position_info.get('total', 0)
            cash = position_info.get('cash', 0)
            risk_level = position_info.get('risk_level', '中')
            
            # 仓位仪表盘
            pos_gauge = GaugeChart(
                value=total_pos,
                max_value=100,
                label="总仓位",
                size=120,
                stroke_width=8,
                color="#4f46e5"
            )
            
            # 现金占比
            cash_card = StatCard(
                title="现金占比",
                value=f"{cash}%",
                subtitle="可用资金",
                icon="dollar-sign",
                variant="default"
            )
            
            # 风险等级
            risk_colors = {"低": "success", "中": "warning", "高": "danger"}
            risk_card = StatCard(
                title="组合风险",
                value=risk_level,
                subtitle="综合评估",
                icon="shield",
                variant=risk_colors.get(risk_level, "warning")
            )
            
            right_html = f'''
            <div style="display: flex; flex-direction: column; gap: 12px; align-items: center;">
                {pos_gauge.render()}
                <div style="display: flex; gap: 10px; width: 100%;">
                    {cash_card.render()}
                    {risk_card.render()}
                </div>
            </div>
            '''
            
            # 使用SplitLayout左右分栏
            split = SplitLayout(
                left=holdings_html,
                right=right_html,
                left_width="66%",
                gap="24px"
            )
            content = split.render()
        else:
            content = holdings_html
        
        section = Section(title="💼 持仓跟踪", content=content, icon="briefcase")
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
