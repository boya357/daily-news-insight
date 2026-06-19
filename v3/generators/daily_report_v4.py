"""
每日市场日报 - V4版（新版设计）
基于V4BaseGenerator基类，遵循内容驱动架构
使用四大内容引擎：市场分析、持仓分析、题材分析、新闻分析
特色：Tab切换新闻分类、卡片化设计、数据可视化
"""
import sys
import os
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from generators.v4_base import V4BaseGenerator
from content.topic_analyzer import TopicListAnalyzer


class DailyReportV4(V4BaseGenerator):
    """每日市场日报V4生成器"""
    
    def __init__(self, data_dir: str = "data"):
        super().__init__(data_dir)
        self.page_title = "📰 每日市场日报"
        self.page_subtitle = "全景市场复盘 · 核心题材挖掘 · 明日策略前瞻"
        self.active_nav_key = "daily"
        self.toc_items = [
            ("今日概览", "section-header"),
            ("市场复盘", "section-overview"),
            ("新闻全景", "section-news-summary"),
            ("重要资讯", "section-important-news"),
            ("热点板块", "section-sectors"),
            ("核心题材", "section-topics"),
            ("持仓诊断", "section-portfolio"),
            ("操作策略", "section-strategy"),
            ("明日展望", "section-outlook"),
            ("风险提示", "section-risk"),
        ]
        self.topics_result = None
    
    def load_data(self):
        """加载数据 - 调用四大内容引擎"""
        super().load_data()
        
        # 加载题材分析
        try:
            topic_analyzer = TopicListAnalyzer(data_dir=self.data_dir)
            self.topics_result = topic_analyzer.analyze()
        except Exception:
            self.topics_result = None
    
    def render_market_summary_card(self) -> str:
        """渲染市场摘要卡片（页面头部统计）"""
        if not self.market_result:
            return ""
        
        sentiment = self.market_result.sentiment
        up_count = getattr(sentiment, 'up_count', 0)
        down_count = getattr(sentiment, 'down_count', 0)
        flat_count = getattr(sentiment, 'flat_count', 0)
        sentiment_level = getattr(sentiment, 'sentiment_level', '中性')
        
        # 获取主要指数
        main_idx = self.market_result.indices[0] if self.market_result.indices else None
        idx_change = main_idx.change_pct if main_idx else 0
        idx_color = '#10B981' if idx_change >= 0 else '#EF4444'
        idx_sign = "+" if idx_change >= 0 else ""
        
        # 计算涨跌比
        total = up_count + down_count + flat_count
        up_ratio = round(up_count / total * 100, 1) if total > 0 else 50
        
        # 新闻情绪
        news_sentiment = "中性"
        if self.news_result:
            news_sentiment = self.news_result.sentiment_overview.split("，")[0] if "，" in self.news_result.sentiment_overview else self.news_result.sentiment_overview
        
        # 板块数量
        sector_count = len(self.market_result.hot_sectors) if self.market_result and self.market_result.hot_sectors else 0
        
        # 题材数量
        topic_count = len(self.topics_result.topics) if self.topics_result and hasattr(self.topics_result, 'topics') else 0
        
        return f'''
        <div class="v4-header-stats">
            <div class="v4-stat-card">
                <div class="v4-stat-value" style="color: {idx_color};">{idx_sign}{idx_change:.2f}%</div>
                <div class="v4-stat-label">上证指数</div>
            </div>
            <div class="v4-stat-card">
                <div class="v4-stat-value" style="color: #10B981;">{up_count}</div>
                <div class="v4-stat-label">上涨家数</div>
            </div>
            <div class="v4-stat-card">
                <div class="v4-stat-value" style="color: #EF4444;">{down_count}</div>
                <div class="v4-stat-label">下跌家数</div>
            </div>
            <div class="v4-stat-card">
                <div class="v4-stat-value">{sentiment_level}</div>
                <div class="v4-stat-label">市场情绪</div>
            </div>
            <div class="v4-stat-card">
                <div class="v4-stat-value">{topic_count}</div>
                <div class="v4-stat-label">核心题材</div>
            </div>
            <div class="v4-stat-card">
                <div class="v4-stat-value">{sector_count}</div>
                <div class="v4-stat-label">热点板块</div>
            </div>
        </div>
        '''
    
    def render_topics_section(self) -> str:
        """渲染核心题材模块（卡片式设计）"""
        if not self.topics_result or not hasattr(self.topics_result, 'topics') or not self.topics_result.topics:
            return ""
        
        topics = self.topics_result.topics[:4]  # 取前4个题材
        
        topics_html = ""
        for topic in topics:
            name = getattr(topic, 'name', '')
            rating = getattr(topic, 'rating', 'B')
            summary = getattr(topic, 'summary', '')
            catalytic = getattr(topic, 'catalytic_factor', '')
            
            # 评级颜色
            rating_colors = {
                'S': ('#DC2626', 'rgba(220, 38, 38, 0.1)'),
                'A+': ('#EA580C', 'rgba(234, 88, 12, 0.1)'),
                'A': ('#F59E0B', 'rgba(245, 158, 11, 0.1)'),
                'B+': ('#EAB308', 'rgba(234, 179, 8, 0.1)'),
                'B': ('#84CC16', 'rgba(132, 204, 22, 0.1)'),
                'C': ('#64748B', 'rgba(100, 116, 139, 0.1)'),
            }
            primary_color, bg_color = rating_colors.get(rating, ('#64748B', 'rgba(100, 116, 139, 0.1)'))
            
            topics_html += f'''
            <div class="daily-topic-card">
                <div class="daily-topic-header">
                    <div class="daily-topic-name">{name}</div>
                    <span class="daily-topic-rating" style="background: {bg_color}; color: {primary_color};">{rating}级</span>
                </div>
                <p class="daily-topic-summary">{summary}</p>
                <div class="daily-topic-catalyst">
                    <span class="catalyst-icon">⚡</span>
                    <span class="catalyst-text">{catalytic}</span>
                </div>
            </div>
            '''
        
        return f'''
        <section class="v4-section" id="section-topics">
            {self.render_section_header("💡 核心题材挖掘", "今日主线", "v4-tag-orange")}
            <div class="v4-card">
                <div class="v4-card-body">
                    <div class="daily-topics-grid">
                        {topics_html}
                    </div>
                </div>
            </div>
        </section>
        '''
    
    def render_outlook_section(self) -> str:
        """渲染明日展望模块"""
        if not self.market_result:
            return ""
        
        # 从市场分析结果获取策略建议
        strategy_suggestion = getattr(self.market_result, 'strategy_suggestion', '')
        if not strategy_suggestion:
            strategy_suggestion = "关注市场情绪变化，控制仓位，把握结构性机会。"
        
        # 市场判断
        market_judgment = getattr(self.market_result, 'market_judgment', '')
        if not market_judgment:
            market_judgment = "短期震荡整理，中期趋势待确认"
        
        # 明日关注
        tomorrow_focus = getattr(self.market_result, 'tomorrow_focus', [])
        if not tomorrow_focus:
            tomorrow_focus = ["关注量能变化", "观察板块轮动持续性", "留意北向资金流向"]
        
        focus_html = "".join(f'<div class="outlook-focus-item"><span class="focus-dot"></span><span class="focus-text">{item}</span></div>' for item in tomorrow_focus)
        
        return f'''
        <section class="v4-section" id="section-outlook">
            {self.render_section_header("🔮 明日展望", "策略前瞻", "v4-tag-purple")}
            <div class="v4-card">
                <div class="v4-card-body">
                    <div class="outlook-grid">
                        <div class="outlook-card">
                            <div class="outlook-icon">📊</div>
                            <div class="outlook-content">
                                <h4 class="outlook-title">市场判断</h4>
                                <p class="outlook-text">{market_judgment}</p>
                            </div>
                        </div>
                        <div class="outlook-card">
                            <div class="outlook-icon">🎯</div>
                            <div class="outlook-content">
                                <h4 class="outlook-title">操作策略</h4>
                                <p class="outlook-text">{strategy_suggestion}</p>
                            </div>
                        </div>
                    </div>
                    <div class="outlook-focus-section">
                        <h4 class="outlook-section-title">📌 明日关注</h4>
                        <div class="outlook-focus-list">
                            {focus_html}
                        </div>
                    </div>
                </div>
            </div>
        </section>
        '''
    
    def render_important_news(self, limit: int = 8) -> str:
        """渲染重要新闻列表（卡片式）"""
        if not self.news_result or not self.news_result.important_news:
            return ""
        
        news_list = self.news_result.important_news[:limit]
        
        news_html = ""
        for i, news in enumerate(news_list):
            title = getattr(news, 'title', '')
            summary = getattr(news, 'summary', '')
            source = getattr(news, 'source', '')
            time_str = getattr(news, 'time', '')
            importance = getattr(news, 'importance', 'normal')
            sentiment = getattr(news, 'sentiment', 'neutral')
            
            # 重要性样式
            imp_styles = {
                'critical': ('#DC2626', '重大'),
                'important': ('#F59E0B', '重要'),
                'normal': ('#64748B', '一般'),
            }
            imp_color, imp_text = imp_styles.get(importance, ('#64748B', '一般'))
            
            # 情绪图标
            sentiment_icons = {
                'positive': '📈',
                'negative': '📉',
                'neutral': '📰',
            }
            sent_icon = sentiment_icons.get(sentiment, '📰')
            
            news_html += f'''
            <div class="news-card">
                <div class="news-card-header">
                    <span class="news-icon">{sent_icon}</span>
                    <span class="news-tag" style="background: {imp_color}20; color: {imp_color};">{imp_text}</span>
                    <span class="news-source">{source}</span>
                    <span class="news-time">{time_str}</span>
                </div>
                <h4 class="news-title">{title}</h4>
                <p class="news-summary">{summary}</p>
            </div>
            '''
        
        return f'''
        <section class="v4-section" id="section-important-news">
            {self.render_section_header("📰 重要资讯", "必读新闻", "v4-tag-blue")}
            <div class="news-list">
                {news_html}
            </div>
        </section>
        '''
    
    def render_content(self) -> str:
        """渲染页面内容 - 按内容重要性排序"""
        # 页面头部
        header_stats = self.render_market_summary_card()
        header = self.render_page_header(extra_html=header_stats)
        
        # 市场分析模块
        market_overview = self.render_market_overview()
        hot_sectors = self.render_hot_sectors()
        
        # 新闻分析模块
        news_summary = self.render_news_summary()
        important_news = self.render_important_news(limit=8)
        
        # 题材分析模块
        topics_section = self.render_topics_section()
        
        # 持仓分析模块
        portfolio_section = self.render_portfolio_section(show_diagnosis=True)
        
        # 策略与风险
        strategy_section = self.render_strategy_section()
        outlook_section = self.render_outlook_section()
        risk_warning = self.render_risk_warning()
        
        return f'''
        {header}
        {market_overview}
        {news_summary}
        {important_news}
        {hot_sectors}
        {topics_section}
        {portfolio_section}
        {strategy_section}
        {outlook_section}
        {risk_warning}
        '''
    
    def get_page_css(self) -> str:
        """页面特有CSS"""
        return '''
        /* 头部统计卡片 */
        .v4-header-stats {
            display: flex;
            justify-content: center;
            gap: 12px;
            margin-top: 20px;
            flex-wrap: wrap;
        }
        .v4-stat-card {
            background: rgba(255, 255, 255, 0.15);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.2);
            border-radius: 12px;
            padding: 14px 20px;
            text-align: center;
            min-width: 90px;
            transition: all 0.3s ease;
        }
        .v4-stat-card:hover {
            background: rgba(255, 255, 255, 0.25);
            transform: translateY(-2px);
        }
        .v4-stat-value {
            font-size: 1.5rem;
            font-weight: 700;
            color: white;
            line-height: 1.2;
            margin-bottom: 4px;
        }
        .v4-stat-label {
            font-size: 0.75rem;
            color: rgba(255, 255, 255, 0.8);
        }
        
        /* 题材卡片网格 */
        .daily-topics-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 16px;
        }
        .daily-topic-card {
            background: #F8FAFC;
            border-radius: 12px;
            padding: 20px;
            transition: all 0.3s ease;
            border: 1px solid #E2E8F0;
        }
        .daily-topic-card:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 25px rgba(0, 0, 0, 0.08);
            border-color: #CBD5E1;
        }
        .daily-topic-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 12px;
        }
        .daily-topic-name {
            font-size: 1rem;
            font-weight: 700;
            color: #1E293B;
        }
        .daily-topic-rating {
            padding: 4px 10px;
            border-radius: 20px;
            font-size: 0.75rem;
            font-weight: 600;
        }
        .daily-topic-summary {
            font-size: 0.875rem;
            color: #64748B;
            line-height: 1.6;
            margin: 0 0 12px 0;
        }
        .daily-topic-catalyst {
            display: flex;
            align-items: flex-start;
            gap: 6px;
            font-size: 0.8125rem;
            color: #F59E0B;
            background: rgba(245, 158, 11, 0.08);
            padding: 8px 12px;
            border-radius: 8px;
        }
        .catalyst-icon {
            flex-shrink: 0;
        }
        .catalyst-text {
            flex: 1;
            line-height: 1.5;
        }
        
        /* 新闻卡片 */
        .news-list {
            display: flex;
            flex-direction: column;
            gap: 12px;
        }
        .news-card {
            background: white;
            border-radius: 12px;
            padding: 20px;
            border: 1px solid #E2E8F0;
            transition: all 0.3s ease;
        }
        .news-card:hover {
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.06);
            border-color: #CBD5E1;
        }
        .news-card-header {
            display: flex;
            align-items: center;
            gap: 10px;
            margin-bottom: 10px;
            flex-wrap: wrap;
        }
        .news-icon {
            font-size: 1rem;
        }
        .news-tag {
            padding: 2px 8px;
            border-radius: 12px;
            font-size: 0.6875rem;
            font-weight: 600;
        }
        .news-source {
            font-size: 0.75rem;
            color: #94A3B8;
        }
        .news-time {
            font-size: 0.75rem;
            color: #94A3B8;
            margin-left: auto;
        }
        .news-title {
            font-size: 1rem;
            font-weight: 600;
            color: #1E293B;
            margin: 0 0 8px 0;
            line-height: 1.5;
        }
        .news-summary {
            font-size: 0.875rem;
            color: #64748B;
            line-height: 1.6;
            margin: 0;
        }
        
        /* 明日展望 */
        .outlook-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 16px;
            margin-bottom: 20px;
        }
        .outlook-card {
            display: flex;
            gap: 14px;
            padding: 18px;
            background: #F8FAFC;
            border-radius: 12px;
            border: 1px solid #E2E8F0;
        }
        .outlook-icon {
            font-size: 1.75rem;
            flex-shrink: 0;
        }
        .outlook-content {
            flex: 1;
        }
        .outlook-title {
            font-size: 0.9375rem;
            font-weight: 600;
            color: #1E293B;
            margin: 0 0 6px 0;
        }
        .outlook-text {
            font-size: 0.875rem;
            color: #64748B;
            line-height: 1.6;
            margin: 0;
        }
        .outlook-focus-section {
            padding-top: 20px;
            border-top: 1px solid #E2E8F0;
        }
        .outlook-section-title {
            font-size: 1rem;
            font-weight: 600;
            color: #1E293B;
            margin: 0 0 12px 0;
        }
        .outlook-focus-list {
            display: flex;
            flex-direction: column;
            gap: 8px;
        }
        .outlook-focus-item {
            display: flex;
            align-items: center;
            gap: 10px;
            padding: 10px 14px;
            background: #F8FAFC;
            border-radius: 8px;
        }
        .focus-dot {
            width: 6px;
            height: 6px;
            background: #667eea;
            border-radius: 50%;
            flex-shrink: 0;
        }
        .focus-text {
            font-size: 0.875rem;
            color: #475569;
        }
        
        /* 响应式调整 */
        @media (max-width: 768px) {
            .daily-topics-grid {
                grid-template-columns: 1fr;
            }
            .v4-header-stats {
                gap: 8px;
            }
            .v4-stat-card {
                padding: 10px 14px;
                min-width: 70px;
            }
            .v4-stat-value {
                font-size: 1.125rem;
            }
            .outlook-grid {
                grid-template-columns: 1fr;
            }
        }
        '''


if __name__ == '__main__':
    generator = DailyReportV4(data_dir='data')
    generator.load_data()
    html = generator.generate()
    output_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '..', 'docs', 'daily_report_v4.html')
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"✅ 每日市场日报V4已生成")
    print(f"📊 市场分析：{'已加载' if generator.market_result else '未加载'}")
    print(f"📰 新闻分析：{'已加载' if generator.news_result else '未加载'}")
    print(f"💼 持仓分析：{'已加载' if generator.portfolio_result else '未加载'}")
    print(f"💡 题材分析：{'已加载' if generator.topics_result else '未加载'}")
