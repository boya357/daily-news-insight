"""
V4 页面生成基类 - 所有V4页面的通用框架
统一封装：导航栏、TOC目录、操作按钮、页脚、JS交互、主题CSS
所有V4页面继承此类，只需实现特有内容模块
"""
import sys
import os
from datetime import datetime
from typing import List, Dict, Optional, Tuple

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from components.v4_theme import V4Theme, get_v4_theme_css
from components.v4_components import (
    V4Card, V4Tag, V4Button, V4Tabs, V4Breadcrumb,
    V4RadarChart, V4ProgressBar, V4DataGrid, V4HorizontalBarChart,
    V4StockCard, V4TopicCard, V4Section, V4PageHeader, V4MarketOverview,
    get_all_component_styles, render_card, render_tag, render_section
)
from content.portfolio_analyzer import PortfolioAnalyzer, PortfolioAnalysisResult, StockAnalysis
from content.market_analyzer import MarketAnalyzer, MarketAnalysisResult
from content.news_analyzer import NewsAnalyzer, NewsAnalysisResult, NewsItem


class V4BaseGenerator:
    """V4页面生成器基类"""
    
    def __init__(self, data_dir: str = "data"):
        self.data_dir = data_dir
        self.portfolio_result: Optional[PortfolioAnalysisResult] = None
        self.market_result: Optional[MarketAnalysisResult] = None
        self.news_result: Optional[NewsAnalysisResult] = None
        self.page_title = "V4 页面"
        self.page_subtitle = ""
        self.active_nav_key = ""
        self.toc_items: List[Tuple[str, str]] = []
        
    def load_data(self):
        """加载基础数据（可被子类扩展）"""
        try:
            portfolio_analyzer = PortfolioAnalyzer(data_dir=self.data_dir)
            self.portfolio_result = portfolio_analyzer.analyze()
        except Exception:
            self.portfolio_result = None
            
        try:
            market_analyzer = MarketAnalyzer(data_dir=self.data_dir)
            self.market_result = market_analyzer.analyze()
        except Exception:
            self.market_result = None
            
        try:
            news_analyzer = NewsAnalyzer(data_dir=self.data_dir)
            self.news_result = news_analyzer.analyze()
        except Exception:
            self.news_result = None
    
    # ==================== 通用组件 ====================
    
    # ==================== V4导航配置 ====================
    
    # V4版本导航项目配置 - 三级导航架构：首页 → 列表页 → 详情页
    V4_NAV_ITEMS = [
        {"key": "home", "label": "首页", "icon": "🏠", "path": "index_v4.html"},
        {"key": "daily", "label": "日报", "icon": "📰", "path": "list_daily_v4.html"},
        {"key": "intraday", "label": "盘中", "icon": "⚡", "path": "list_intraday_v4.html"},
        {"key": "aftermarket", "label": "盘后", "icon": "📊", "path": "list_aftermarket_v4.html"},
        {"key": "s_catalyst", "label": "S级催化", "icon": "🚀", "path": "list_s_catalyst_v4.html"},
        {"key": "sector_heatmap", "label": "板块热度", "icon": "🔥", "path": "list_sector_heatmap_v4.html"},
        {"key": "tomorrow_catalyst", "label": "明日催化", "icon": "⏰", "path": "list_tomorrow_catalyst_v4.html"},
        {"key": "weekend_express", "label": "周末速递", "icon": "📦", "path": "list_weekend_express_v4.html"},
        {"key": "weekly_outlook", "label": "周三前瞻", "icon": "👁️", "path": "list_weekly_outlook_v4.html"},
        {"key": "weekly_review", "label": "周复盘", "icon": "📋", "path": "list_weekly_review_v4.html"},
        {"key": "longhubang", "label": "龙虎榜", "icon": "🏆", "path": "list_longhubang_v4.html"},
        {"key": "portfolio_dashboard", "label": "持仓", "icon": "📊", "path": "list_portfolio_dashboard_v4.html"},
        {"key": "prediction_center", "label": "预测", "icon": "🔮", "path": "list_prediction_center_v4.html"},
        {"key": "alert_system", "label": "预警", "icon": "🚨", "path": "list_alert_system_v4.html"},
    ]
    
    def render_nav(self) -> str:
        """渲染导航栏"""
        try:
            from core.config import SITE_ICON, SITE_NAME
        except ImportError:
            SITE_ICON = "💎"
            SITE_NAME = "投资洞察系统"
        
        items_html = ""
        for item in self.V4_NAV_ITEMS:
            active_class = "active" if item["key"] == self.active_nav_key else ""
            label = f'{item["icon"]} {item["label"]}'
            items_html += f'<a class="v4-nav-item {active_class}" href="{item["path"]}">{label}</a>'
        
        return f'''
        <nav class="v4-nav" id="topNav">
            <div class="v4-nav-logo">{SITE_ICON} {SITE_NAME}</div>
            <div class="v4-nav-menu">
                {items_html}
            </div>
        </nav>
        '''
    
    def render_toc(self) -> str:
        """渲染悬浮目录导航"""
        items_html = ""
        for label, section_id in self.toc_items:
            items_html += f'<a href="#{section_id}" class="v4-toc-item" data-section="{section_id}">{label}</a>'
        
        return f'''
        <div class="v4-toc" id="toc">
            <div class="v4-toc-header">
                <span>📑 目录导航</span>
                <button class="v4-toc-toggle" onclick="toggleToc()">−</button>
            </div>
            <div class="v4-toc-items" id="tocItems">
                {items_html}
            </div>
        </div>
        '''
    
    def render_action_buttons(self) -> str:
        """渲染左下角操作按钮组"""
        return '''
        <div class="v4-action-buttons">
            <button class="v4-action-btn" onclick="refreshPage()" title="刷新">🔄</button>
            <button class="v4-action-btn" onclick="toggleTheme()" title="主题切换">🌓</button>
            <button class="v4-action-btn" onclick="sharePage()" title="分享">📤</button>
            <button class="v4-action-btn" onclick="scrollToTop()" title="回到顶部">⬆️</button>
        </div>
        '''
    
    def render_page_header(self, title: str = None, subtitle: str = None, extra_html: str = "") -> str:
        """渲染页面头部"""
        title = title or self.page_title
        subtitle = subtitle or self.page_subtitle
        
        return f'''
        <section class="v4-section" id="section-header">
            <div class="v4-page-header">
                <div class="v4-page-title">
                    <h1>{title}</h1>
                    <p class="v4-page-subtitle">{subtitle}</p>
                </div>
                {extra_html}
            </div>
        </section>
        '''
    
    def render_section_header(self, title: str, tag_text: str = "", tag_class: str = "v4-tag-blue") -> str:
        """渲染区块标题"""
        tag_html = f'<span class="v4-section-tag {tag_class}">{tag_text}</span>' if tag_text else ""
        return f'''
        <div class="v4-section-header">
            <h2 class="v4-section-title">{title}</h2>
            {tag_html}
        </div>
        '''
    
    def render_footer(self) -> str:
        """渲染页脚"""
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return f'''
        <footer class="v4-footer">
            <p>数据更新时间：{now}</p>
            <p>📌 投资有风险，入市需谨慎 | 本报告仅供参考，不构成投资建议</p>
        </footer>
        '''
    
    def render_js(self) -> str:
        """渲染JavaScript交互逻辑"""
        return '''
        <script>
            // 导航栏滚动效果
            window.addEventListener('scroll', function() {
                const nav = document.getElementById('topNav');
                nav.classList.toggle('scrolled', window.scrollY > 50);
            });
            
            // TOC目录高亮
            window.addEventListener('scroll', function() {
                const sections = document.querySelectorAll('.v4-section');
                const tocItems = document.querySelectorAll('.v4-toc-item');
                let currentSection = '';
                sections.forEach(section => {
                    if (window.scrollY >= section.offsetTop - 100) {
                        currentSection = section.getAttribute('id');
                    }
                });
                tocItems.forEach(item => {
                    item.classList.toggle('active', item.getAttribute('data-section') === currentSection);
                });
            });
            
            // 平滑滚动
            document.querySelectorAll('a[href^="#"]').forEach(anchor => {
                anchor.addEventListener('click', function(e) {
                    e.preventDefault();
                    const target = document.querySelector(this.getAttribute('href'));
                    if (target) target.scrollIntoView({ behavior: 'smooth', block: 'start' });
                });
            });
            
            // TOC展开收起
            function toggleToc() {
                const tocItems = document.getElementById('tocItems');
                const toggleBtn = document.querySelector('.v4-toc-toggle');
                if (tocItems.style.display === 'none') {
                    tocItems.style.display = 'block';
                    toggleBtn.textContent = '−';
                } else {
                    tocItems.style.display = 'none';
                    toggleBtn.textContent = '+';
                }
            }
            
            // 回到顶部
            function scrollToTop() { window.scrollTo({ top: 0, behavior: 'smooth' }); }
            
            // 刷新页面
            function refreshPage() { window.location.reload(); }
            
            // 主题切换（占位）
            function toggleTheme() { alert('主题切换功能开发中...'); }
            
            // 分享
            function sharePage() {
                if (navigator.share) {
                    navigator.share({ title: document.title, url: window.location.href });
                } else {
                    navigator.clipboard.writeText(window.location.href);
                    alert('链接已复制到剪贴板');
                }
            }
            
            // Tab切换功能
            function switchNewsTab(tabId) {
                // 隐藏所有tab内容
                document.querySelectorAll('.v4-tab-content').forEach(content => {
                    content.classList.remove('active');
                });
                // 取消所有tab按钮激活状态
                document.querySelectorAll('.v4-tab-btn').forEach(btn => {
                    btn.classList.remove('active');
                });
                // 显示选中的tab内容
                const targetContent = document.getElementById(tabId);
                if (targetContent) {
                    targetContent.classList.add('active');
                }
                // 激活对应的tab按钮
                const targetBtn = document.querySelector(`[data-tab="${tabId}"]`);
                if (targetBtn) {
                    targetBtn.classList.add('active');
                }
            }
            
            // 通用Tab切换（支持多组Tab）
            function switchTab(tabGroup, tabId) {
                const group = document.getElementById(tabGroup);
                if (!group) return;
                
                // 隐藏该组所有tab内容
                group.querySelectorAll('.v4-tab-content').forEach(content => {
                    content.classList.remove('active');
                });
                // 取消该组所有tab按钮激活状态
                group.querySelectorAll('.v4-tab-btn').forEach(btn => {
                    btn.classList.remove('active');
                });
                // 显示选中的tab内容
                const targetContent = document.getElementById(tabId);
                if (targetContent) {
                    targetContent.classList.add('active');
                }
                // 激活对应的tab按钮
                const targetBtn = group.querySelector(`[data-tab="${tabId}"]`);
                if (targetBtn) {
                    targetBtn.classList.add('active');
                }
            }
            
            // 卡片式Tab切换
            function switchCardTab(tabGroup, tabId) {
                const group = document.getElementById(tabGroup);
                if (!group) return;
                
                // 隐藏该组所有tab内容
                group.querySelectorAll('.card-tab-content').forEach(content => {
                    content.classList.remove('active');
                });
                // 取消该组所有tab按钮激活状态
                group.querySelectorAll('.card-tab-btn').forEach(btn => {
                    btn.classList.remove('active');
                });
                // 显示选中的tab内容
                const targetContent = document.getElementById(tabId);
                if (targetContent) {
                    targetContent.classList.add('active');
                }
                // 激活对应的tab按钮
                const targetBtn = group.querySelector(`[data-tab="${tabId}"]`);
                if (targetBtn) {
                    targetBtn.classList.add('active');
                }
            }
        </script>
        '''
    
    # ==================== 通用内容模块 ====================
    
    def render_market_overview(self) -> str:
        """渲染市场概览模块"""
        if not self.market_result or not self.market_result.indices:
            return ""
        
        # 指数柱状图
        chart_bars = ""
        max_change = max(abs(idx.change_pct) for idx in self.market_result.indices) if self.market_result.indices else 1
        if max_change == 0:
            max_change = 1
        
        for idx in self.market_result.indices:
            color = V4Theme.UP_COLOR if idx.change_pct >= 0 else V4Theme.DOWN_COLOR
            height = abs(idx.change_pct) / max_change * 80
            sign = "+" if idx.change_pct >= 0 else ""
            
            chart_bars += f'''
            <div class="v4-bar-item">
                <div class="v4-bar-value" style="color: {color};">{sign}{idx.change_pct:.2f}%</div>
                <div class="v4-bar-chart">
                    <div class="v4-bar" style="height: {height}px; background: {color};"></div>
                </div>
                <div class="v4-bar-label">{idx.name}</div>
            </div>
            '''
        
        # 市场情绪
        sentiment = self.market_result.sentiment
        sentiment_level = getattr(sentiment, 'sentiment_level', '中性')
        up_count = getattr(sentiment, 'up_count', 0)
        down_count = getattr(sentiment, 'down_count', 0)
        flat_count = getattr(sentiment, 'flat_count', 0)
        profit_effect = getattr(sentiment, 'profit_effect', '')
        
        sentiment_color = V4Theme.UP_COLOR if up_count > down_count else V4Theme.DOWN_COLOR
        
        return f'''
        <section class="v4-section" id="section-overview">
            {self.render_section_header("📈 市场概览", "实时", "v4-tag-blue")}
            <div class="v4-card v4-market-overview">
                <div class="v4-market-chart">
                    <h3 class="v4-card-subtitle">主要指数</h3>
                    <div class="v4-bar-chart-container">
                        {chart_bars}
                    </div>
                </div>
                <div class="v4-market-stats">
                    <h3 class="v4-card-subtitle">市场情绪</h3>
                    <div class="v4-sentiment-score">
                        <span class="v4-sentiment-value" style="color: {sentiment_color};">{sentiment_level}</span>
                        {f'<div class="v4-sentiment-desc">{profit_effect}</div>' if profit_effect else ''}
                    </div>
                    <div class="v4-market-counts">
                        <div class="v4-count-item">
                            <span class="v4-count-value" style="color: {V4Theme.UP_COLOR};">{up_count}</span>
                            <span class="v4-count-label">上涨</span>
                        </div>
                        <div class="v4-count-item">
                            <span class="v4-count-value" style="color: {V4Theme.DOWN_COLOR};">{down_count}</span>
                            <span class="v4-count-label">下跌</span>
                        </div>
                        <div class="v4-count-item">
                            <span class="v4-count-value" style="color: {V4Theme.TEXT_SECONDARY};">{flat_count}</span>
                            <span class="v4-count-label">平盘</span>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        '''
    
    def render_stock_diagnosis(self, stock: StockAnalysis) -> str:
        """渲染单只股票的四维诊断 - 1x4横向布局"""
        
        def render_dimension(name: str, status: str, items: list, icon: str) -> str:
            status_colors = {
                '强势': V4Theme.UP_COLOR, '流入': V4Theme.UP_COLOR,
                '利好': V4Theme.UP_COLOR, '向好': V4Theme.UP_COLOR,
                '震荡': V4Theme.WARNING, '平衡': V4Theme.WARNING,
                '中性': V4Theme.WARNING, '平稳': V4Theme.WARNING,
                '弱势': V4Theme.DOWN_COLOR, '流出': V4Theme.DOWN_COLOR,
                '利空': V4Theme.DOWN_COLOR, '下滑': V4Theme.DOWN_COLOR,
            }
            status_color = status_colors.get(status, V4Theme.TEXT_SECONDARY)
            
            items_html = ""
            for item in items[:4]:
                items_html += f'<div class="v4-diagnosis-item"><span class="v4-diagnosis-icon">{item.icon}</span><span class="v4-diagnosis-text">{item.text}</span></div>'
            
            return f'''
            <div class="v4-diagnosis-card">
                <div class="v4-diagnosis-header">
                    <span class="v4-diagnosis-icon">{icon}</span>
                    <span class="v4-diagnosis-name">{name}</span>
                    <span class="v4-diagnosis-status" style="color: {status_color};">{status}</span>
                </div>
                <div class="v4-diagnosis-items">
                    {items_html}
                </div>
            </div>
            '''
        
        dim_technical = render_dimension('技术面', stock.technical_status, stock.technical_items, '📊')
        dim_fund = render_dimension('资金面', stock.fund_status, stock.fund_items, '💰')
        dim_news = render_dimension('消息面', stock.news_status, stock.news_items, '📰')
        dim_industry = render_dimension('产业面', stock.industry_status, stock.industry_items, '🏭')
        
        return f'''
        <div class="v4-diagnosis-grid">
            {dim_technical}
            {dim_fund}
            {dim_news}
            {dim_industry}
        </div>
        '''
    
    def render_portfolio_section(self, show_diagnosis: bool = True) -> str:
        """渲染持仓股跟踪模块"""
        if not self.portfolio_result or not self.portfolio_result.stocks:
            return ""
        
        stocks_html = ""
        for stock in self.portfolio_result.stocks:
            change_color = V4Theme.UP_COLOR if stock.today_change_pct >= 0 else V4Theme.DOWN_COLOR
            change_sign = "+" if stock.today_change_pct >= 0 else ""
            
            profit_color = V4Theme.UP_COLOR if stock.profit_loss_pct >= 0 else V4Theme.DOWN_COLOR
            profit_sign = "+" if stock.profit_loss_pct >= 0 else ""
            
            advice_tags = {
                'buy': ('买入', 'v4-tag-green'),
                'sell': ('卖出', 'v4-tag-red'),
                'hold': ('持有', 'v4-tag-blue'),
            }
            advice_text, advice_class = advice_tags.get(stock.advice_type, ('观察', 'v4-tag-gray'))
            
            sl_distance = stock.distance_to_stop_loss
            sl_color = V4Theme.DOWN_COLOR if sl_distance < 5 else V4Theme.TEXT_SECONDARY
            
            diagnosis_html = self.render_stock_diagnosis(stock) if show_diagnosis else ""
            
            stocks_html += f'''
            <div class="v4-card v4-stock-card">
                <div class="v4-stock-header">
                    <div class="v4-stock-info">
                        <h3 class="v4-stock-name">{stock.name}</h3>
                        <span class="v4-stock-code">{stock.code}</span>
                        <span class="v4-tag {advice_class}">{advice_text}</span>
                    </div>
                    <div class="v4-stock-prices">
                        <div class="v4-price-current">¥{stock.current_price:.2f}</div>
                        <div class="v4-price-change" style="color: {change_color};">
                            {change_sign}{stock.today_change_pct:.2f}% 今日
                        </div>
                    </div>
                </div>
                <div class="v4-stock-metrics">
                    <div class="v4-metric">
                        <span class="v4-metric-label">成本价</span>
                        <span class="v4-metric-value">¥{stock.cost_price:.2f}</span>
                    </div>
                    <div class="v4-metric">
                        <span class="v4-metric-label">盈亏比例</span>
                        <span class="v4-metric-value" style="color: {profit_color};">{profit_sign}{stock.profit_loss_pct:.2f}%</span>
                    </div>
                    <div class="v4-metric">
                        <span class="v4-metric-label">止损位</span>
                        <span class="v4-metric-value" style="color: {sl_color};">¥{stock.stop_loss_price:.2f}</span>
                    </div>
                    <div class="v4-metric">
                        <span class="v4-metric-label">距止损</span>
                        <span class="v4-metric-value" style="color: {sl_color};">{sl_distance:.1f}%</span>
                    </div>
                </div>
                {diagnosis_html}
                <div class="v4-stock-advice">
                    <div class="v4-advice-text">💡 {stock.advice_text}</div>
                </div>
            </div>
            '''
        
        return f'''
        <section class="v4-section" id="section-portfolio">
            {self.render_section_header("📋 持仓股诊断", f"{len(self.portfolio_result.stocks)} 只标的", "v4-tag-orange")}
            <div class="v4-portfolio-list">
                {stocks_html}
            </div>
        </section>
        '''
    
    def render_strategy_section(self) -> str:
        """渲染操作策略建议模块"""
        if not self.portfolio_result:
            return ""
        
        overall_advice = self.portfolio_result.overall_advice
        
        strategy_points = []
        for stock in self.portfolio_result.stocks:
            if stock.advice_type == 'sell':
                strategy_points.append(f"🔴 **{stock.name}**：{stock.advice_text}")
            elif stock.advice_type == 'buy':
                strategy_points.append(f"🟢 **{stock.name}**：{stock.advice_text}")
            else:
                strategy_points.append(f"🔵 **{stock.name}**：{stock.advice_text}")
        
        points_html = "".join(f'<li>{p}</li>' for p in strategy_points)
        
        return f'''
        <section class="v4-section" id="section-strategy">
            {self.render_section_header("🎯 操作策略建议", "今日策略", "v4-tag-green")}
            <div class="v4-card">
                <div class="v4-strategy-overview">
                    <p class="v4-strategy-text">{overall_advice}</p>
                </div>
                <div class="v4-strategy-points">
                    <h3 class="v4-card-subtitle">个股操作要点</h3>
                    <ul class="v4-point-list">{points_html}</ul>
                </div>
            </div>
        </section>
        '''
    
    def render_risk_warning(self, custom_risks: List[str] = None) -> str:
        """渲染风险提示模块"""
        risk_items = []
        
        if self.portfolio_result and self.portfolio_result.stocks:
            high_risk = [s for s in self.portfolio_result.stocks if s.distance_to_stop_loss < 10]
            medium_risk = [s for s in self.portfolio_result.stocks if 10 <= s.distance_to_stop_loss < 20]
            
            if high_risk:
                names = "、".join([s.name for s in high_risk])
                risk_items.append(f"🔴 **高风险警示**：{names} 距离止损位不足10%，请密切关注")
            if medium_risk:
                names = "、".join([s.name for s in medium_risk])
                risk_items.append(f"🟡 **中风险提示**：{names} 距离止损位10%-20%，建议设置预警")
        
        if custom_risks:
            risk_items.extend(custom_risks)
        
        risk_items.extend([
            "⚪ **系统性风险**：关注大盘整体走势，若出现系统性风险需及时减仓",
            "⚪ **流动性风险**：合理控制仓位，避免单只标的占比过高",
        ])
        
        risk_html = "".join(f'<li class="v4-risk-item">{item}</li>' for item in risk_items)
        
        return f'''
        <section class="v4-section" id="section-risk">
            {self.render_section_header("⚠️ 风险提示", "必读", "v4-tag-red")}
            <div class="v4-card v4-risk-card">
                <ul class="v4-risk-list">{risk_html}</ul>
                <p class="v4-risk-disclaimer">* 以上分析仅供参考，不构成投资建议。投资有风险，入市需谨慎。</p>
            </div>
        </section>
        '''
    
    def render_hot_sectors(self) -> str:
        """渲染热点板块排行"""
        if not self.market_result or not self.market_result.hot_sectors:
            return ""
        
        sectors = self.market_result.hot_sectors
        max_change = max(abs(getattr(s, 'change_pct', 0)) for s in sectors) if sectors else 1
        if max_change == 0:
            max_change = 1
        
        sectors_html = ""
        for i, sector in enumerate(sectors[:10]):
            name = getattr(sector, 'name', '')
            change = getattr(sector, 'change_pct', 0)
            color = V4Theme.UP_COLOR if change >= 0 else V4Theme.DOWN_COLOR
            bar_width = abs(change) / max_change * 100
            sign = "+" if change >= 0 else ""
            
            rank_color = V4Theme.UP_COLOR if i < 3 else V4Theme.TEXT_SECONDARY
            
            sectors_html += f'''
            <div class="v4-sector-item">
                <span class="v4-sector-rank" style="color: {rank_color};">{i+1}</span>
                <span class="v4-sector-name">{name}</span>
                <div class="v4-sector-bar">
                    <div class="v4-sector-bar-fill" style="width: {bar_width}%; background: {color};"></div>
                </div>
                <span class="v4-sector-change" style="color: {color};">{sign}{change:.2f}%</span>
            </div>
            '''
        
        return f'''
        <section class="v4-section" id="section-sectors">
            {self.render_section_header("🔥 热点板块排行", "涨幅榜", "v4-tag-red")}
            <div class="v4-card">
                <div class="v4-hot-sectors">
                    {sectors_html}
                </div>
            </div>
        </section>
        '''
    
    # ==================== 新闻相关模块 ====================
    
    def render_news_summary(self) -> str:
        """渲染新闻概览模块"""
        if not self.news_result:
            return ""
        
        result = self.news_result
        
        # 情绪颜色
        if result.positive_ratio > result.negative_ratio + 20:
            sentiment_color = V4Theme.UP_COLOR
            sentiment_icon = "🟢"
        elif result.negative_ratio > result.positive_ratio + 20:
            sentiment_color = V4Theme.DOWN_COLOR
            sentiment_icon = "🔴"
        else:
            sentiment_color = V4Theme.WARNING
            sentiment_icon = "🟡"
        
        # 核心主题标签
        theme_tags = ""
        for theme in result.key_themes[:5]:
            theme_tags += f'<span class="v4-theme-tag">{theme}</span>'
        
        return f'''
        <section class="v4-section" id="section-news-summary">
            {self.render_section_header("📰 新闻全景概览", f"{result.total_news_count}条资讯", "v4-tag-blue")}
            <div class="v4-card">
                <div class="v4-news-summary">
                    <div class="v4-news-sentiment">
                        <div class="v4-sentiment-gauge">
                            <span class="v4-sentiment-icon">{sentiment_icon}</span>
                            <div class="v4-sentiment-label">整体情绪</div>
                            <div class="v4-sentiment-value" style="color: {sentiment_color};">
                                {result.sentiment_overview.split("，")[0]}
                            </div>
                        </div>
                        <div class="v4-sentiment-bars">
                            <div class="v4-sentiment-bar-item">
                                <div class="v4-sentiment-bar-label">正面</div>
                                <div class="v4-sentiment-bar-track">
                                    <div class="v4-sentiment-bar-fill v4-bar-positive" style="width: {result.positive_ratio}%;"></div>
                                </div>
                                <div class="v4-sentiment-bar-value">{result.positive_ratio}%</div>
                            </div>
                            <div class="v4-sentiment-bar-item">
                                <div class="v4-sentiment-bar-label">负面</div>
                                <div class="v4-sentiment-bar-track">
                                    <div class="v4-sentiment-bar-fill v4-bar-negative" style="width: {result.negative_ratio}%;"></div>
                                </div>
                                <div class="v4-sentiment-bar-value">{result.negative_ratio}%</div>
                            </div>
                        </div>
                    </div>
                    <div class="v4-news-themes">
                        <h4 class="v4-card-subtitle">核心主题</h4>
                        <div class="v4-theme-tags">
                            {theme_tags}
                        </div>
                        <p class="v4-news-summary-text">{result.market_impact_summary}</p>
                    </div>
                </div>
            </div>
        </section>
        '''
    
    def render_important_news(self, limit: int = 8) -> str:
        """渲染重要新闻列表"""
        if not self.news_result or not self.news_result.important_news:
            return ""
        
        news_list = self.news_result.important_news[:limit]
        
        news_html = ""
        for news in news_list:
            # 重要性标签
            importance_map = {
                'critical': ('重大', 'v4-tag-red'),
                'important': ('重要', 'v4-tag-orange'),
                'normal': ('一般', 'v4-tag-gray'),
            }
            imp_text, imp_class = importance_map.get(news.importance, ('一般', 'v4-tag-gray'))
            
            # 情绪颜色
            if news.sentiment == 'positive':
                sentiment_color = V4Theme.UP_COLOR
                sentiment_icon = "↑"
            elif news.sentiment == 'negative':
                sentiment_color = V4Theme.DOWN_COLOR
                sentiment_icon = "↓"
            else:
                sentiment_color = V4Theme.TEXT_SECONDARY
                sentiment_icon = "→"
            
            # 影响板块标签
            sector_tags = ""
            for sector in news.affected_sectors[:3]:
                sector_tags += f'<span class="v4-sector-mini-tag">{sector}</span>'
            
            news_html += f'''
            <div class="v4-news-item">
                <div class="v4-news-header">
                    <span class="v4-tag {imp_class}">{imp_text}</span>
                    <span class="v4-news-category">[{news.category}]</span>
                    <span class="v4-news-source">{news.source}</span>
                    <span class="v4-news-time">{news.publish_time}</span>
                </div>
                <h4 class="v4-news-title">
                    <span class="v4-news-sentiment-icon" style="color: {sentiment_color};">{sentiment_icon}</span>
                    {news.title}
                </h4>
                <p class="v4-news-desc">{news.content}</p>
                <div class="v4-news-footer">
                    {sector_tags}
                    <span class="v4-news-catalytic">{news.catalytic_effect}</span>
                </div>
            </div>
            '''
        
        return f'''
        <section class="v4-section" id="section-important-news">
            {self.render_section_header("⚡ 重要新闻速递", f"精选{len(news_list)}条", "v4-tag-red")}
            <div class="v4-card">
                <div class="v4-news-list">
                    {news_html}
                </div>
            </div>
        </section>
        '''
    
    def render_news_by_category(self, categories: List[str] = None) -> str:
        """渲染分类新闻（带Tab切换）"""
        if not self.news_result or not self.news_result.categorized_news:
            return ""
        
        cat_news = self.news_result.categorized_news
        
        # 默认显示所有分类
        if categories is None:
            categories = list(cat_news.keys())
        
        # 生成Tab标签
        tab_labels = ""
        tab_contents = ""
        for i, cat in enumerate(categories):
            news_list = cat_news.get(cat, [])
            if not news_list:
                continue
            
            active_class = "active" if i == 0 else ""
            
            tab_labels += f'<button class="v4-tab-btn {active_class}" data-tab="news-{cat}" onclick="switchNewsTab(\'news-{cat}\')">{cat} ({len(news_list)})</button>'
            
            # Tab内容
            news_items_html = ""
            for news in news_list[:6]:
                sentiment_color = V4Theme.UP_COLOR if news.sentiment == 'positive' else V4Theme.DOWN_COLOR if news.sentiment == 'negative' else V4Theme.TEXT_SECONDARY
                
                news_items_html += f'''
                <div class="v4-news-item-simple">
                    <span class="v4-news-dot" style="background: {sentiment_color};"></span>
                    <span class="v4-news-title-simple">{news.title}</span>
                    <span class="v4-news-time-simple">{news.publish_time}</span>
                </div>
                '''
            
            tab_contents += f'''
            <div class="v4-tab-content {active_class}" id="news-{cat}">
                {news_items_html}
            </div>
            '''
        
        return f'''
        <section class="v4-section" id="section-news-categories">
            {self.render_section_header("📂 分类新闻", "多维度覆盖", "v4-tag-blue")}
            <div class="v4-card">
                <div class="v4-tabs">
                    {tab_labels}
                </div>
                <div class="v4-tab-panels">
                    {tab_contents}
                </div>
            </div>
        </section>
        '''
    
    def render_sector_news_impact(self) -> str:
        """渲染板块新闻影响分析"""
        if not self.news_result or not self.news_result.sector_impact_map:
            return ""
        
        sector_map = self.news_result.sector_impact_map
        
        sectors_html = ""
        for i, (sector, news_list) in enumerate(list(sector_map.items())[:8]):
            # 计算该板块的整体情绪
            if news_list:
                avg_sentiment = sum(n.sentiment_score for n in news_list) / len(news_list)
            else:
                avg_sentiment = 50
            
            sentiment_color = V4Theme.UP_COLOR if avg_sentiment > 55 else V4Theme.DOWN_COLOR if avg_sentiment < 45 else V4Theme.WARNING
            sentiment_text = "偏多" if avg_sentiment > 55 else "偏空" if avg_sentiment < 45 else "中性"
            
            sectors_html += f'''
            <div class="v4-sector-impact-item">
                <div class="v4-sector-impact-header">
                    <span class="v4-sector-rank">{i+1}</span>
                    <span class="v4-sector-name">{sector}</span>
                    <span class="v4-sector-news-count">{len(news_list)}条新闻</span>
                    <span class="v4-sector-sentiment" style="color: {sentiment_color};">{sentiment_text}</span>
                </div>
                <div class="v4-sector-impact-news">
                    {"、".join([n.title[:25] + "..." if len(n.title) > 25 else n.title for n in news_list[:3]])}
                </div>
            </div>
            '''
        
        return f'''
        <section class="v4-section" id="section-sector-impact">
            {self.render_section_header("🎯 板块影响追踪", "新闻催化排行", "v4-tag-purple")}
            <div class="v4-card">
                <div class="v4-sector-impact-list">
                    {sectors_html}
                </div>
            </div>
        </section>
        '''
    
    # ==================== 图表组件 ====================
    
    def render_radar_chart(self, labels: list, values: list, size: int = 220) -> str:
        """渲染通用雷达图（支持任意3-8个维度）
        
        Args:
            labels: 维度标签列表
            values: 各维度数值（0-100）
            size: 图表大小
        """
        import math
        
        n = len(labels)
        if n != len(values) or n < 3 or n > 8:
            return ""
        
        center = size / 2
        radius = size * 0.32  # 数据区域半径
        
        # 计算数据点和标签位置
        data_points = []
        label_positions = []
        
        for i in range(n):
            # 从顶部开始，顺时针分布
            angle = -90 + i * (360 / n)
            rad = angle * math.pi / 180
            
            # 数据点
            r = radius * values[i] / 100
            x = center + r * math.cos(rad)
            y = center + r * math.sin(rad)
            data_points.append(f"{x:.1f},{y:.1f}")
            
            # 标签位置（外圈，留出边距）
            label_r = radius * 1.28
            lx = center + label_r * math.cos(rad)
            ly = center + label_r * math.sin(rad)
            label_positions.append((lx, ly, labels[i], values[i]))
        
        # 网格线（4层）
        grid_polygons = []
        for level in [25, 50, 75, 100]:
            grid_points = []
            r = radius * level / 100
            for i in range(n):
                angle = -90 + i * (360 / n)
                rad = angle * math.pi / 180
                x = center + r * math.cos(rad)
                y = center + r * math.sin(rad)
                grid_points.append(f"{x:.1f},{y:.1f}")
            grid_polygons.append(" ".join(grid_points))
        
        # 轴线
        axis_lines = ""
        for i in range(n):
            angle = -90 + i * (360 / n)
            rad = angle * math.pi / 180
            x = center + radius * math.cos(rad)
            y = center + radius * math.sin(rad)
            axis_lines += f'<line x1="{center}" y1="{center}" x2="{x:.1f}" y2="{y:.1f}" class="radar-axis" />'
        
        # 网格多边形
        grid_svg = ""
        for points in grid_polygons:
            grid_svg += f'<polygon points="{points}" class="radar-grid" />'
        
        # 数据多边形
        data_polygon = f'<polygon points="{" ".join(data_points)}" class="radar-polygon" />'
        
        # 数据点
        data_dots = ""
        for point in data_points:
            x, y = point.split(',')
            data_dots += f'<circle cx="{x}" cy="{y}" r="3" fill="#667eea" />'
        
        # 标签
        labels_svg = ""
        for lx, ly, label, value in label_positions:
            # 根据位置调整文本锚点
            if abs(lx - center) < 10:
                text_anchor = "middle"
            elif lx > center:
                text_anchor = "start"
            else:
                text_anchor = "end"
            
            labels_svg += f'''
            <text x="{lx:.1f}" y="{ly:.1f}" text-anchor="{text_anchor}" dominant-baseline="middle" class="radar-label">
                {label}
            </text>
            '''
        
        return f'''
        <div class="radar-chart-container" style="width: {size}px; height: {size}px;">
            <svg class="radar-chart" viewBox="0 0 {size} {size}" xmlns="http://www.w3.org/2000/svg">
                {grid_svg}
                {axis_lines}
                {data_polygon}
                {data_dots}
                {labels_svg}
            </svg>
        </div>
        '''
    
    # ==================== 题材分析组件 ====================
    
    def render_dimension_bars(self, labels: list, values: list, bar_color: str = "#667eea") -> str:
        """渲染六维评分条组件
        
        Args:
            labels: 维度标签列表
            values: 各维度数值（0-100）
            bar_color: 进度条颜色
        """
        if len(labels) != len(values):
            return ""
        
        bars_html = ""
        for label, value in zip(labels, values):
            # 根据分值变色
            if value >= 90:
                color = "#10B981"  # 绿色
            elif value >= 75:
                color = "#667eea"  # 紫色
            elif value >= 60:
                color = "#F59E0B"  # 橙色
            else:
                color = "#EF4444"  # 红色
            
            bars_html += f'''
            <div class="dim-bar-item">
                <div class="dim-bar-label">{label}</div>
                <div class="dim-bar-track">
                    <div class="dim-bar-fill" style="width: {value}%; background: {color};"></div>
                </div>
                <div class="dim-bar-score">{int(value)}分</div>
            </div>
            '''
        
        return f'<div class="dim-bars-container">{bars_html}</div>'
    
    def render_topic_card(self, topic_data: dict) -> str:
        """渲染题材卡片（S级/A级/B级题材通用
        
        Args:
            topic_data: 题材数据字典
        """
        name = topic_data.get('name', '未知题材')
        level = topic_data.get('level', 'B')
        level_name = topic_data.get('level_name', '')
        icon = topic_data.get('icon', '🔥')
        score = topic_data.get('score', 0)
        description = topic_data.get('description', '')
        radar = topic_data.get('radar', {})
        
        # 等级颜色
        level_colors = {
            'S': ('#DC2626', 'rgba(220, 38, 38, 0.1)'),
            'A': ('#F59E0B', 'rgba(245, 158, 11, 0.1)'),
            'B': ('#8B5CF6', 'rgba(139, 92, 246, 0.1)'),
            'C': ('#64748B', 'rgba(100, 116, 139, 0.1)'),
        }
        primary_color, bg_color = level_colors.get(level, level_colors['B'])
        
        # 六维评分条
        radar_labels = list(radar.keys())
        radar_values = list(radar.values())
        dim_bars = self.render_dimension_bars(radar_labels, radar_values, primary_color)
        
        # 雷达图
        radar_html = self.render_radar_chart(radar_labels, radar_values, size=200) if radar else ""
        
        # 核心标的
        core_stocks = topic_data.get('core_stocks', [])
        stocks_html = ""
        for stock in core_stocks[:4]:
            stocks_html += f'<span class="topic-stock-tag">{stock}</span>'
        
        # 催化事件
        catalyst = topic_data.get('catalyst', '')
        risk = topic_data.get('risk', '')
        
        # 产业链
        industry_chain = topic_data.get('industry_chain', {})
        chain_html = ""
        if industry_chain:
            upstream = "、".join(industry_chain.get('upstream', [])[:3])
            midstream = "、".join(industry_chain.get('midstream', [])[:3])
            downstream = "、".join(industry_chain.get('downstream', [])[:3])
            
            chain_html = f'''
            <div class="topic-chain-section">
                <h4 class="topic-section-title">🏭 产业链图谱</h4>
                <div class="chain-flow">
                    <div class="chain-node">
                        <div class="chain-node-title">上游</div>
                        <div class="chain-node-desc">{upstream}</div>
                    </div>
                    <div class="chain-arrow">→</div>
                    <div class="chain-node">
                        <div class="chain-node-title">中游</div>
                        <div class="chain-node-desc">{midstream}</div>
                    </div>
                    <div class="chain-arrow">→</div>
                    <div class="chain-node">
                        <div class="chain-node-title">下游</div>
                        <div class="chain-node-desc">{downstream}</div>
                    </div>
                </div>
            </div>
            '''
        
        # 投资策略
        strategy = topic_data.get('strategy', '')
        strategy_html = ""
        if strategy:
            strategy_html = f'''
            <div class="topic-strategy-section">
                <h4 class="topic-section-title">💡 投资策略</h4>
                <p class="strategy-text">{strategy}</p>
            </div>
            '''
        
        # 风险提示
        risk_html = ""
        if risk:
            risk_html = f'''
            <div class="topic-risk-section">
                <h4 class="topic-section-title">⚠️ 核心风险</h4>
                <p class="risk-text">{risk}</p>
            </div>
            '''
        
        return f'''
        <div class="topic-card-v4">
            <div class="topic-card-header" style="background: linear-gradient(135deg, {bg_color}, #ffffff);">
                <div class="topic-header-content">
                    <span class="topic-icon">{icon}</span>
                    <div class="topic-header-info">
                        <div class="topic-header-top">
                            <h3 class="topic-name">{name}</h3>
                            <div class="topic-badges">
                                <span class="level-badge" style="background: {primary_color}; color: white;">{level}级 · {level_name}</span>
                                <span class="score-badge">{score:.1f}分</span>
                            </div>
                        </div>
                        <p class="topic-desc">{description}</p>
                    </div>
                </div>
            </div>
            
            <div class="topic-card-body">
                <div class="topic-score-row">
                    <div class="topic-dim-bars">
                        <h4 class="topic-section-title">📊 六维评分</h4>
                        {dim_bars}
                    </div>
                    <div class="topic-radar-wrap">
                        {radar_html}
                    </div>
                </div>
                
                <div class="topic-stocks-section">
                    <h4 class="topic-section-title">🎯 核心标的</h4>
                    <div class="topic-stocks-grid">
                        {stocks_html}
                    </div>
                </div>
                
                {chain_html}
                
                {strategy_html}
                
                {risk_html}
            </div>
        </div>
        '''
    # ==================== 板块排行 ====================
    
    def render_sector_ranking(self, sectors: list, title: str = "热点板块", 
                             subtitle: str = "", show_rank: bool = True,
                             max_items: int = 10) -> str:
        """渲染板块热度排行
        
        Args:
            sectors: 板块列表，每项包含 name, change_pct, 可选的其他字段
            title: 标题
            subtitle: 副标题
            show_rank: 是否显示排名
            max_items: 最多显示数量
        """
        if not sectors:
            return ""
        
        # 计算最大涨跌幅用于柱状图宽度
        max_change = max(abs(s.get('change_pct', 0)) for s in sectors) if sectors else 1
        if max_change == 0:
            max_change = 1
        
        sectors_html = ""
        for i, sector in enumerate(sectors[:max_items]):
            name = sector.get('name', '')
            change = sector.get('change_pct', 0)
            color = V4Theme.UP_COLOR if change >= 0 else V4Theme.DOWN_COLOR
            bar_width = abs(change) / max_change * 100
            sign = "+" if change >= 0 else ""
            
            # 排名样式
            rank_class = f"top{i+1}" if i < 3 else "normal"
            
            sectors_html += f'''
            <div class="sector-rank-item">
                {f'<span class="rank-number {rank_class}">{i+1}</span>' if show_rank else ''}
                <span class="sector-name">{name}</span>
                <div class="sector-bar-container">
                    <div class="sector-bar-fill" style="width: {bar_width}%; background: {color};"></div>
                </div>
                <span class="sector-change" style="color: {color};">{sign}{change:.2f}%</span>
            </div>
            '''
        
        return f'''
        <div class="v4-card">
            {self.render_section_header(title, subtitle, "v4-tag-red") if subtitle else f'<h3 class="v4-section-title">{title}</h3>'}
            <div class="sector-ranking-list">
                {sectors_html}
            </div>
        </div>
        '''
    
    # ==================== 市场概览升级版 ====================
    
    def render_market_overview_v2(self) -> str:
        """渲染升级版市场概览 - 指数卡片 + 横向柱状图 + 数据网格 + 情绪标签"""
        if not self.market_result or not self.market_result.indices:
            return self.render_market_overview()  # 降级到旧版本
        
        # 取前4个主要指数
        indices = self.market_result.indices[:4]
        
        # 指数卡片
        index_cards = ""
        for idx in indices:
            is_up = idx.change_pct >= 0
            change_class = "up" if is_up else "down"
            sign = "+" if is_up else ""
            index_cards += f'''
            <div class="market-index-card">
                <div class="index-name">{idx.name}</div>
                <div class="index-value">{idx.price:,.2f}</div>
                <div class="index-change {change_class}">{sign}{idx.change_pct:.2f}%</div>
            </div>
            '''
        
        # 横向柱状图
        max_change = max(abs(idx.change_pct) for idx in indices) if indices else 1
        if max_change == 0:
            max_change = 1
        
        bar_chart_rows = ""
        for idx in indices:
            is_up = idx.change_pct >= 0
            bar_class = "up" if is_up else "down"
            bar_width = max(abs(idx.change_pct) / max_change * 100, 15)  # 最小15%宽度
            sign = "+" if is_up else ""
            bar_chart_rows += f'''
            <div class="bar-chart-row">
                <div class="bar-label">{idx.name}</div>
                <div class="bar-track">
                    <div class="bar-fill {bar_class}" style="width: {bar_width}%;">
                        <span class="bar-value">{sign}{idx.change_pct:.2f}%</span>
                    </div>
                </div>
            </div>
            '''
        
        # 市场情绪
        sentiment = self.market_result.sentiment
        sentiment_level = getattr(sentiment, 'sentiment_level', '中性')
        profit_effect = getattr(sentiment, 'profit_effect', '一般')
        
        # 情绪标签颜色
        if '偏多' in sentiment_level or '强' in sentiment_level:
            sentiment_tag_class = 'v4-tag-red'
        elif '偏空' in sentiment_level or '弱' in sentiment_level:
            sentiment_tag_class = 'v4-tag-green'
        else:
            sentiment_tag_class = 'v4-tag-orange'
        
        # 赚钱效应标签颜色
        if '好' in profit_effect or '强' in profit_effect:
            profit_tag_class = 'v4-tag-blue'
        elif '差' in profit_effect:
            profit_tag_class = 'v4-tag-gray'
        else:
            profit_tag_class = 'v4-tag-blue'
        
        # 市场统计数据
        up_count = getattr(sentiment, 'up_count', 0)
        down_count = getattr(sentiment, 'down_count', 0)
        limit_up = getattr(sentiment, 'limit_up', 0)
        limit_down = getattr(sentiment, 'limit_down', 0)
        
        # 市场判断
        market_judgment = getattr(self.market_result, 'market_judgment', '震荡整理')
        
        return f'''
        <section class="v4-section" id="section-overview">
            {self.render_section_header("📊 市场概览", "实时行情", "v4-tag-blue")}
            <div class="v4-card">
                <div class="v4-card-body">
                    <div class="market-overview-v3">
                        <!-- 指数卡片 -->
                        <div class="market-index-cards">
                            {index_cards}
                        </div>
                        
                        <!-- 分割线 -->
                        <div class="v4-divider"></div>
                        
                        <!-- 指数涨跌幅柱状图 -->
                        <div class="horizontal-bar-chart">
                            <div class="chart-title">📈 指数涨跌幅</div>
                            {bar_chart_rows}
                        </div>
                        
                        <!-- 分割线 -->
                        <div class="v4-divider"></div>
                        
                        <!-- 市场数据网格 -->
                        <div class="market-data-grid">
                            <div class="market-data-item">
                                <div class="data-label">上涨家数</div>
                                <div class="data-value up">{up_count}</div>
                            </div>
                            <div class="market-data-item">
                                <div class="data-label">下跌家数</div>
                                <div class="data-value down">{down_count}</div>
                            </div>
                            <div class="market-data-item">
                                <div class="data-label">涨停</div>
                                <div class="data-value up">{limit_up}</div>
                            </div>
                            <div class="market-data-item">
                                <div class="data-label">跌停</div>
                                <div class="data-value down">{limit_down}</div>
                            </div>
                        </div>
                        
                        <!-- 分割线 -->
                        <div class="v4-divider"></div>
                        
                        <!-- 市场情绪栏 -->
                        <div class="market-sentiment-bar">
                            <div class="sentiment-tags">
                                <span class="text-secondary">市场情绪：</span>
                                <span class="v4-tag {sentiment_tag_class}">{sentiment_level}</span>
                                <span class="v4-tag {profit_tag_class}">赚钱效应：{profit_effect}</span>
                            </div>
                            <div class="trend-judgment">
                                趋势判断：<strong>{market_judgment}</strong>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        '''
    
    # ==================== 通用CSS ====================
    
    def get_common_css(self) -> str:
        """获取通用页面CSS"""
        return f'''
        .v4-page-header {{
            text-align: center;
            padding: 60px 20px 40px;
        }}
        .v4-page-title h1 {{
            font-size: 36px;
            font-weight: 800;
            color: {V4Theme.TEXT_PRIMARY};
            margin: 0 0 8px 0;
        }}
        .v4-page-subtitle {{
            font-size: 16px;
            color: {V4Theme.TEXT_SECONDARY};
            margin: 0;
        }}
        .v4-header-stats {{
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 20px;
            max-width: 600px;
            margin: 30px auto 0;
        }}
        .v4-stat-card {{
            background: {V4Theme.BG_CARD};
            border-radius: {V4Theme.RADIUS_LG};
            padding: 24px;
            box-shadow: {V4Theme.SHADOW_CARD};
            text-align: center;
        }}
        .v4-stat-value {{
            font-size: 32px;
            font-weight: 800;
            color: {V4Theme.TEXT_PRIMARY};
            line-height: 1.2;
        }}
        .v4-stat-label {{
            font-size: 13px;
            color: {V4Theme.TEXT_SECONDARY};
            margin-top: 4px;
        }}
        .v4-market-overview {{
            display: grid;
            grid-template-columns: 2fr 1fr;
            gap: 30px;
        }}
        .v4-bar-chart-container {{
            display: flex;
            align-items: flex-end;
            justify-content: space-around;
            height: 120px;
            padding: 20px 0;
        }}
        .v4-bar-item {{
            display: flex;
            flex-direction: column;
            align-items: center;
            flex: 1;
        }}
        .v4-bar-value {{
            font-size: 12px;
            font-weight: 600;
            margin-bottom: 8px;
        }}
        .v4-bar-chart {{
            width: 30px;
            height: 80px;
            background: {V4Theme.BG_SUBTLE};
            border-radius: 4px;
            position: relative;
            overflow: hidden;
        }}
        .v4-bar {{
            width: 100%;
            position: absolute;
            bottom: 0;
            left: 0;
            transition: height 0.3s ease;
        }}
        .v4-bar-label {{
            font-size: 12px;
            color: {V4Theme.TEXT_SECONDARY};
            margin-top: 8px;
        }}
        .v4-market-stats {{
            background: {V4Theme.BG_SUBTLE};
            border-radius: {V4Theme.RADIUS_DEFAULT};
            padding: 20px;
        }}
        .v4-sentiment-score {{
            text-align: center;
            padding: 20px 0;
        }}
        .v4-sentiment-value {{
            font-size: 24px;
            font-weight: 700;
        }}
        .v4-sentiment-desc {{
            font-size: 12px;
            color: {V4Theme.TEXT_SECONDARY};
            margin-top: 4px;
        }}
        .v4-market-counts {{
            display: flex;
            justify-content: space-around;
            margin-top: 16px;
        }}
        .v4-count-item {{
            text-align: center;
        }}
        .v4-count-value {{
            display: block;
            font-size: 18px;
            font-weight: 700;
        }}
        .v4-count-label {{
            font-size: 12px;
            color: {V4Theme.TEXT_SECONDARY};
        }}
        .v4-portfolio-list {{
            display: flex;
            flex-direction: column;
            gap: 20px;
        }}
        .v4-stock-card {{
            padding: 24px;
        }}
        .v4-stock-header {{
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            margin-bottom: 16px;
        }}
        .v4-stock-info {{
            display: flex;
            align-items: center;
            gap: 12px;
            flex-wrap: wrap;
        }}
        .v4-stock-name {{
            font-size: 20px;
            font-weight: 700;
            color: {V4Theme.TEXT_PRIMARY};
            margin: 0;
        }}
        .v4-stock-code {{
            font-size: 13px;
            color: {V4Theme.TEXT_MUTED};
        }}
        .v4-stock-prices {{
            text-align: right;
        }}
        .v4-price-current {{
            font-size: 24px;
            font-weight: 800;
            color: {V4Theme.TEXT_PRIMARY};
        }}
        .v4-price-change {{
            font-size: 13px;
            font-weight: 600;
            margin-top: 4px;
        }}
        .v4-stock-metrics {{
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 16px;
            padding: 16px 0;
            border-top: 1px solid {V4Theme.BORDER_LIGHT};
            border-bottom: 1px solid {V4Theme.BORDER_LIGHT};
            margin-bottom: 16px;
        }}
        .v4-metric {{
            text-align: center;
        }}
        .v4-metric-label {{
            display: block;
            font-size: 12px;
            color: {V4Theme.TEXT_SECONDARY};
            margin-bottom: 4px;
        }}
        .v4-metric-value {{
            font-size: 15px;
            font-weight: 600;
            color: {V4Theme.TEXT_PRIMARY};
        }}
        .v4-diagnosis-grid {{
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 12px;
            margin: 16px 0;
        }}
        .v4-diagnosis-card {{
            background: {V4Theme.BG_SUBTLE};
            border-radius: {V4Theme.RADIUS_DEFAULT};
            padding: 12px;
        }}
        .v4-diagnosis-header {{
            display: flex;
            align-items: center;
            gap: 6px;
            margin-bottom: 8px;
            flex-wrap: wrap;
        }}
        .v4-diagnosis-name {{
            font-size: 13px;
            font-weight: 600;
            color: {V4Theme.TEXT_PRIMARY};
        }}
        .v4-diagnosis-status {{
            font-size: 11px;
            font-weight: 600;
            padding: 2px 6px;
            background: currentColor;
            opacity: 0.15;
            border-radius: 4px;
            margin-left: auto;
        }}
        .v4-diagnosis-items {{
            display: flex;
            flex-direction: column;
            gap: 4px;
        }}
        .v4-diagnosis-item {{
            display: flex;
            align-items: flex-start;
            gap: 6px;
            font-size: 11px;
            color: {V4Theme.TEXT_SECONDARY};
            line-height: 1.4;
        }}
        .v4-diagnosis-icon {{
            flex-shrink: 0;
            font-size: 10px;
        }}
        .v4-stock-advice {{
            margin-top: 12px;
            padding-top: 12px;
            border-top: 1px solid {V4Theme.BORDER_LIGHT};
        }}
        .v4-advice-text {{
            font-size: 13px;
            color: {V4Theme.TEXT_SECONDARY};
            line-height: 1.6;
        }}
        .v4-strategy-overview {{
            margin-bottom: 20px;
            padding-bottom: 16px;
            border-bottom: 1px solid {V4Theme.BORDER_LIGHT};
        }}
        .v4-strategy-text {{
            font-size: 15px;
            line-height: 1.8;
            color: {V4Theme.TEXT_PRIMARY};
            margin: 0;
        }}
        .v4-point-list {{
            list-style: none;
            padding: 0;
            margin: 0;
            display: flex;
            flex-direction: column;
            gap: 10px;
        }}
        .v4-point-list li {{
            font-size: 14px;
            color: {V4Theme.TEXT_SECONDARY};
            line-height: 1.6;
        }}
        .v4-risk-list {{
            list-style: none;
            padding: 0;
            margin: 0 0 16px 0;
            display: flex;
            flex-direction: column;
            gap: 10px;
        }}
        .v4-risk-item {{
            font-size: 14px;
            color: {V4Theme.TEXT_SECONDARY};
            line-height: 1.6;
        }}
        .v4-risk-disclaimer {{
            font-size: 12px;
            color: {V4Theme.TEXT_MUTED};
            margin: 0;
            padding-top: 12px;
            border-top: 1px solid {V4Theme.BORDER_LIGHT};
        }}
        .v4-card-subtitle {{
            font-size: 14px;
            font-weight: 600;
            color: {V4Theme.TEXT_PRIMARY};
            margin: 0 0 12px 0;
        }}
        .v4-hot-sectors {{
            display: flex;
            flex-direction: column;
            gap: 10px;
        }}
        .v4-sector-item {{
            display: flex;
            align-items: center;
            gap: 12px;
            padding: 8px 0;
            border-bottom: 1px solid {V4Theme.BORDER_LIGHT};
        }}
        .v4-sector-item:last-child {{
            border-bottom: none;
        }}
        .v4-sector-rank {{
            font-size: 16px;
            font-weight: 700;
            width: 24px;
            text-align: center;
        }}
        .v4-sector-name {{
            font-size: 14px;
            color: {V4Theme.TEXT_PRIMARY};
            width: 120px;
            flex-shrink: 0;
        }}
        .v4-sector-bar {{
            flex: 1;
            height: 8px;
            background: {V4Theme.BG_SUBTLE};
            border-radius: 4px;
            overflow: hidden;
        }}
        .v4-sector-bar-fill {{
            height: 100%;
            border-radius: 4px;
            transition: width 0.3s ease;
        }}
        .v4-sector-change {{
            font-size: 13px;
            font-weight: 600;
            width: 70px;
            text-align: right;
        }}
        
        /* 新闻模块样式 */
        .v4-news-summary {{
            display: grid;
            grid-template-columns: 1fr 2fr;
            gap: 30px;
        }}
        .v4-news-sentiment {{
            display: flex;
            flex-direction: column;
            gap: 20px;
        }}
        .v4-sentiment-gauge {{
            text-align: center;
            padding: 20px;
            background: {V4Theme.BG_SUBTLE};
            border-radius: {V4Theme.RADIUS_LG};
        }}
        .v4-sentiment-icon {{
            font-size: 48px;
            display: block;
            margin-bottom: 8px;
        }}
        .v4-sentiment-label {{
            font-size: 13px;
            color: {V4Theme.TEXT_SECONDARY};
            margin-bottom: 4px;
        }}
        .v4-sentiment-value {{
            font-size: 20px;
            font-weight: 700;
        }}
        .v4-sentiment-bars {{
            display: flex;
            flex-direction: column;
            gap: 10px;
        }}
        .v4-sentiment-bar-item {{
            display: flex;
            align-items: center;
            gap: 10px;
        }}
        .v4-sentiment-bar-label {{
            width: 40px;
            font-size: 12px;
            color: {V4Theme.TEXT_SECONDARY};
        }}
        .v4-sentiment-bar-track {{
            flex: 1;
            height: 8px;
            background: {V4Theme.BG_SUBTLE};
            border-radius: 4px;
            overflow: hidden;
        }}
        .v4-sentiment-bar-fill {{
            height: 100%;
            border-radius: 4px;
            transition: width 0.5s ease;
        }}
        .v4-bar-positive {{
            background: {V4Theme.UP_COLOR};
        }}
        .v4-bar-negative {{
            background: {V4Theme.DOWN_COLOR};
        }}
        .v4-sentiment-bar-value {{
            width: 40px;
            text-align: right;
            font-size: 12px;
            font-weight: 600;
            color: {V4Theme.TEXT_PRIMARY};
        }}
        .v4-news-themes {{
            display: flex;
            flex-direction: column;
            gap: 12px;
        }}
        .v4-theme-tags {{
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
        }}
        .v4-theme-tag {{
            padding: 4px 12px;
            background: rgba(139, 92, 246, 0.1);
            color: #7C3AED;
            border-radius: 20px;
            font-size: 12px;
            font-weight: 500;
        }}
        .v4-news-summary-text {{
            font-size: 13px;
            color: {V4Theme.TEXT_SECONDARY};
            line-height: 1.6;
            margin: 0;
        }}
        
        /* 新闻列表样式 */
        .v4-news-list {{
            display: flex;
            flex-direction: column;
            gap: 16px;
        }}
        .v4-news-item {{
            padding: 16px;
            background: {V4Theme.BG_SUBTLE};
            border-radius: {V4Theme.RADIUS_DEFAULT};
            transition: all 0.2s ease;
        }}
        .v4-news-item:hover {{
            background: #F1F5F9;
        }}
        .v4-news-header {{
            display: flex;
            align-items: center;
            gap: 10px;
            margin-bottom: 8px;
            flex-wrap: wrap;
        }}
        .v4-news-category {{
            font-size: 12px;
            color: {V4Theme.TEXT_SECONDARY};
        }}
        .v4-news-source {{
            font-size: 12px;
            color: {V4Theme.TEXT_MUTED};
        }}
        .v4-news-time {{
            font-size: 12px;
            color: {V4Theme.TEXT_MUTED};
        }}
        .v4-news-title {{
            font-size: 15px;
            font-weight: 600;
            color: {V4Theme.TEXT_PRIMARY};
            margin: 0 0 8px 0;
            line-height: 1.5;
            display: flex;
            align-items: flex-start;
            gap: 6px;
        }}
        .v4-news-sentiment-icon {{
            font-size: 16px;
            font-weight: 800;
            flex-shrink: 0;
        }}
        .v4-news-desc {{
            font-size: 13px;
            color: {V4Theme.TEXT_SECONDARY};
            line-height: 1.6;
            margin: 0 0 10px 0;
        }}
        .v4-news-footer {{
            display: flex;
            align-items: center;
            gap: 8px;
            flex-wrap: wrap;
        }}
        .v4-sector-mini-tag {{
            padding: 2px 8px;
            background: rgba(59, 130, 246, 0.1);
            color: #3B82F6;
            border-radius: 4px;
            font-size: 11px;
            font-weight: 500;
        }}
        .v4-news-catalytic {{
            font-size: 12px;
            color: #F59E0B;
            margin-left: auto;
        }}
        
        /* Tab切换样式 */
        .v4-tabs {{
            display: flex;
            gap: 4px;
            border-bottom: 2px solid {V4Theme.BORDER_LIGHT};
            margin-bottom: 16px;
            overflow-x: auto;
        }}
        .v4-tab-btn {{
            padding: 10px 16px;
            background: none;
            border: none;
            font-size: 13px;
            font-weight: 500;
            color: {V4Theme.TEXT_SECONDARY};
            cursor: pointer;
            border-bottom: 2px solid transparent;
            margin-bottom: -2px;
            white-space: nowrap;
            transition: all 0.2s ease;
        }}
        .v4-tab-btn:hover {{
            color: {V4Theme.TEXT_PRIMARY};
        }}
        .v4-tab-btn.active {{
            color: #7C3AED;
            border-bottom-color: #7C3AED;
            font-weight: 600;
        }}
        .v4-tab-panels {{
            min-height: 200px;
        }}
        .v4-tab-content {{
            display: none;
        }}
        .v4-tab-content.active {{
            display: block;
        }}
        .v4-news-item-simple {{
            display: flex;
            align-items: center;
            gap: 10px;
            padding: 10px 0;
            border-bottom: 1px solid {V4Theme.BORDER_LIGHT};
        }}
        .v4-news-item-simple:last-child {{
            border-bottom: none;
        }}
        .v4-news-dot {{
            width: 6px;
            height: 6px;
            border-radius: 50%;
            flex-shrink: 0;
        }}
        .v4-news-title-simple {{
            flex: 1;
            font-size: 13px;
            color: {V4Theme.TEXT_PRIMARY};
            line-height: 1.4;
        }}
        .v4-news-time-simple {{
            font-size: 12px;
            color: {V4Theme.TEXT_MUTED};
            flex-shrink: 0;
        }}
        
        /* 板块影响追踪 */
        .v4-sector-impact-list {{
            display: flex;
            flex-direction: column;
            gap: 12px;
        }}
        .v4-sector-impact-item {{
            padding: 12px 16px;
            background: {V4Theme.BG_SUBTLE};
            border-radius: {V4Theme.RADIUS_DEFAULT};
        }}
        .v4-sector-impact-header {{
            display: flex;
            align-items: center;
            gap: 10px;
            margin-bottom: 6px;
        }}
        .v4-sector-impact-header .v4-sector-rank {{
            width: 24px;
            height: 24px;
            line-height: 24px;
            text-align: center;
            background: #EEF2FF;
            color: #4F46E5;
            border-radius: 6px;
            font-size: 12px;
            font-weight: 700;
        }}
        .v4-sector-impact-header .v4-sector-name {{
            font-size: 14px;
            font-weight: 600;
            color: {V4Theme.TEXT_PRIMARY};
            width: auto;
        }}
        .v4-sector-news-count {{
            font-size: 12px;
            color: {V4Theme.TEXT_SECONDARY};
        }}
        .v4-sector-sentiment {{
            margin-left: auto;
            font-size: 12px;
            font-weight: 600;
        }}
        .v4-sector-impact-news {{
            font-size: 12px;
            color: {V4Theme.TEXT_SECONDARY};
            line-height: 1.5;
            padding-left: 34px;
        }}
        
        @media (max-width: 768px) {{
            .v4-header-stats {{ grid-template-columns: 1fr; gap: 12px; }}
            .v4-market-overview {{ grid-template-columns: 1fr; }}
            .v4-stock-metrics {{ grid-template-columns: repeat(2, 1fr); }}
            .v4-diagnosis-grid {{ grid-template-columns: repeat(2, 1fr); }}
            .v4-page-title h1 {{ font-size: 28px; }}
            .v4-sector-name {{ width: 100px; font-size: 13px; }}
        }}
        '''
    
    # ==================== 页面生成入口 ====================
    
    def generate(self) -> str:
        """生成完整HTML页面 - 子类需实现 render_content 方法"""
        self.load_data()
        
        nav = self.render_nav()
        toc = self.render_toc()
        action_buttons = self.render_action_buttons()
        footer = self.render_footer()
        js = self.render_js()
        theme_css = get_v4_theme_css()
        components_css = get_all_component_styles()
        common_css = self.get_common_css()
        page_css = self.get_page_css()
        content = self.render_content()
        
        return f'''
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{self.page_title}</title>
    <style>
        {theme_css}
        {components_css}
        {common_css}
        {page_css}
    </style>
</head>
<body class="v4-body">
    {nav}
    <main class="v4-main">
        <div class="v4-container">
            {content}
            {footer}
        </div>
    </main>
    {toc}
    {action_buttons}
    {js}
</body>
</html>
        '''
    
    def render_content(self) -> str:
        """渲染页面主体内容 - 子类必须重写此方法"""
        raise NotImplementedError("子类必须实现 render_content 方法")
    
    def get_page_css(self) -> str:
        """获取页面特有CSS - 子类可重写"""
        return ""
