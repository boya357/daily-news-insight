"""
S级催化扫描生成器 - V4版
基于内容引擎 + V4白底主题的新一代页面

架构特点：
- 内容层：TopicAnalyzer 生成结构化分析内容
- 展现层：V4主题组件渲染
- 数据层：统一数据源
"""
import sys
import os
from datetime import datetime
from typing import List, Dict, Optional

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from components.v4_theme import V4Theme, get_v4_theme_css
from content.portfolio_analyzer import PortfolioAnalyzer, PortfolioAnalysisResult
from content.market_analyzer import MarketAnalyzer, MarketAnalysisResult


class SLevelCatalystV4Generator:
    """S级催化扫描 V4 生成器"""
    
    def __init__(self, data_dir: str = "data"):
        self.data_dir = data_dir
        self.portfolio_result: Optional[PortfolioAnalysisResult] = None
        self.market_result: Optional[MarketAnalysisResult] = None
        self.topics_data = None
        
    def load_data(self):
        """加载所有数据"""
        # 加载持仓分析
        portfolio_analyzer = PortfolioAnalyzer(data_dir=self.data_dir)
        self.portfolio_result = portfolio_analyzer.analyze()
        
        # 加载市场分析
        market_analyzer = MarketAnalyzer(data_dir=self.data_dir)
        self.market_result = market_analyzer.analyze()
        
        # 加载题材数据
        self._load_topics_data()
    
    def _load_topics_data(self):
        """加载题材数据"""
        import json
        
        possible_paths = [
            os.path.join(os.getcwd(), self.data_dir, 'topics.json'),
            '/app/data/所有对话/主对话/data/topics.json',
        ]
        
        data_path = None
        for path in possible_paths:
            if os.path.exists(path):
                data_path = path
                break
        
        if data_path:
            with open(data_path, 'r', encoding='utf-8') as f:
                self.topics_data = json.load(f)
    
    def _render_nav(self, active: str = "S级催化") -> str:
        """渲染导航栏"""
        nav_items = [
            ("首页", "index.html"),
            ("盘中快报", "intraday/latest.html"),
            ("S级催化", "s-level-catalyst/latest.html"),
            ("持仓仪表盘", "portfolio/index.html"),
            ("明日催化剂", "tomorrow-catalyst/index.html"),
            ("题材健康度", "topic-health/index.html"),
            ("预判验证", "prediction-verification/index.html"),
        ]
        
        items_html = ""
        for name, url in nav_items:
            active_class = "active" if name == active else ""
            items_html += f'<a class="v4-nav-item {active_class}" href="/{url}">{name}</a>'
        
        return f'''
        <div class="v4-nav">
            <div class="v4-nav-logo">📈 投资研究中心</div>
            <div class="v4-nav-menu">
                {items_html}
            </div>
        </div>
        '''
    
    def _render_page_header(self) -> str:
        """渲染页面头部"""
        update_time = self.market_result.update_time if self.market_result else datetime.now().strftime('%Y-%m-%d %H:%M')
        
        return f'''
        <div class="v4-page-header">
            <h1>🔴 S级催化扫描</h1>
            <p class="subtitle">深度挖掘超级题材机会 · 把握市场主线行情</p>
            <p class="update-time">数据更新时间：{update_time}</p>
        </div>
        '''
    
    def _render_market_overview(self) -> str:
        """渲染市场概览模块"""
        if not self.market_result:
            return ""
        
        indices = self.market_result.indices[:4]
        sentiment = self.market_result.sentiment
        
        indices_html = ""
        for idx in indices:
            color_class = "text-up" if idx.change_pct >= 0 else "text-down"
            change_str = f"+{idx.change_pct:.2f}%" if idx.change_pct >= 0 else f"{idx.change_pct:.2f}%"
            
            indices_html += f'''
            <div class="v4-data-item">
                <div class="label">{idx.name}</div>
                <div class="value">{idx.price:.2f}</div>
                <div class="stock-change {color_class}">{change_str}</div>
            </div>
            '''
        
        return f'''
        <div class="v4-card mb-6">
            <div class="v4-card-header">
                <span>📊</span> 市场概览
            </div>
            <div class="v4-card-body">
                <div class="v4-data-grid cols-4">
                    {indices_html}
                </div>
                
                <div class="v4-divider"></div>
                
                <div class="v4-data-grid cols-4">
                    <div class="v4-data-item">
                        <div class="label">上涨家数</div>
                        <div class="value text-up">{sentiment.up_count}</div>
                    </div>
                    <div class="v4-data-item">
                        <div class="label">下跌家数</div>
                        <div class="value text-down">{sentiment.down_count}</div>
                    </div>
                    <div class="v4-data-item">
                        <div class="label">涨停</div>
                        <div class="value text-up">{sentiment.limit_up}</div>
                    </div>
                    <div class="v4-data-item">
                        <div class="label">跌停</div>
                        <div class="value text-down">{sentiment.limit_down}</div>
                    </div>
                </div>
                
                <div class="v4-divider"></div>
                
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <div>
                        <span class="text-secondary">市场情绪：</span>
                        <span class="v4-tag v4-tag-orange">{sentiment.sentiment_level}</span>
                        <span class="v4-tag v4-tag-blue" style="margin-left: 8px;">赚钱效应：{sentiment.profit_effect}</span>
                    </div>
                    <div>
                        <span class="text-secondary">趋势判断：</span>
                        <span class="font-semibold">{self.market_result.market_trend}</span>
                    </div>
                </div>
            </div>
        </div>
        '''
    
    def _render_portfolio_section(self) -> str:
        """渲染持仓跟踪模块"""
        if not self.portfolio_result:
            return ""
        
        stocks = self.portfolio_result.stocks
        
        stocks_html = ""
        for stock in stocks:
            # 涨跌幅颜色
            change_class = "text-up" if stock.today_change_pct >= 0 else "text-down"
            change_str = f"+{stock.today_change_pct:.2f}%" if stock.today_change_pct >= 0 else f"{stock.today_change_pct:.2f}%"
            
            # 盈亏颜色
            profit_class = "text-up" if stock.profit_loss_pct >= 0 else "text-down"
            profit_str = f"+{stock.profit_loss_pct:.2f}%" if stock.profit_loss_pct >= 0 else f"{stock.profit_loss_pct:.2f}%"
            
            # 建议标签
            if stock.advice_type == "buy":
                advice_tag = f'<span class="v4-tag v4-tag-green">{stock.advice_type.upper()} 加仓</span>'
            elif stock.advice_type == "sell":
                advice_tag = f'<span class="v4-tag v4-tag-red">{stock.advice_type.upper()} 减仓</span>'
            else:
                advice_tag = f'<span class="v4-tag v4-tag-blue">HOLD 持有</span>'
            
            # 风险等级
            if stock.risk_level == "高":
                risk_tag = '<span class="v4-tag v4-tag-red">高风险</span>'
            elif stock.risk_level == "中":
                risk_tag = '<span class="v4-tag v4-tag-orange">中风险</span>'
            else:
                risk_tag = '<span class="v4-tag v4-tag-green">低风险</span>'
            
            # 诊断指标
            diagnosis_html = f'''
            <div class="v4-diagnosis-grid">
                <div class="v4-diagnosis-item {"good" if stock.technical_status == "强势" else "bad" if stock.technical_status == "弱势" else "neutral"}">
                    <div class="dim-name">技术面</div>
                    <div class="dim-value">{stock.technical_status or "-"}</div>
                </div>
                <div class="v4-diagnosis-item {"good" if stock.fund_status == "流入" else "bad"}">
                    <div class="dim-name">资金面</div>
                    <div class="dim-value">{stock.fund_status or "-"}</div>
                </div>
                <div class="v4-diagnosis-item">
                    <div class="dim-name">消息面</div>
                    <div class="dim-value">{stock.news_status or "-"}</div>
                </div>
                <div class="v4-diagnosis-item">
                    <div class="dim-name">产业面</div>
                    <div class="dim-value">{stock.industry_status or "-"}</div>
                </div>
            </div>
            '''
            
            stocks_html += f'''
            <div class="v4-stock-card">
                <div class="stock-header">
                    <div>
                        <span class="stock-name">{stock.name}</span>
                        <span class="stock-code" style="margin-left: 8px;">{stock.code}</span>
                    </div>
                    <div style="display: flex; gap: 6px;">
                        {risk_tag}
                        {advice_tag}
                    </div>
                </div>
                
                <div style="display: flex; justify-content: space-between; align-items: flex-end;">
                    <div>
                        <div class="stock-price {change_class}">{stock.current_price:.2f}</div>
                        <div class="stock-change {change_class}">今日 {change_str}</div>
                    </div>
                    <div style="text-align: right;">
                        <div class="text-secondary" style="font-size: 0.875rem;">持仓盈亏</div>
                        <div class="font-semibold {profit_class}" style="font-size: 1.125rem;">{profit_str}</div>
                    </div>
                </div>
                
                {diagnosis_html}
                
                <div class="v4-divider"></div>
                
                <div style="display: flex; justify-content: space-between; font-size: 0.875rem;">
                    <div>
                        <span class="text-secondary">止损价：</span>
                        <span class="font-medium">{stock.stop_loss_price:.2f}</span>
                    </div>
                    <div>
                        <span class="text-secondary">距止损：</span>
                        <span class="font-medium">{"{:.2f}%".format(stock.distance_to_stop_loss * 100) if stock.distance_to_stop_loss else "-"}</span>
                    </div>
                </div>
                
                <div class="v4-alert info" style="margin-top: 16px; margin-bottom: 0;">
                    💡 {stock.advice_text}
                </div>
            </div>
            '''
        
        # 整体总结
        total_return = self.portfolio_result.total_return_pct
        total_return_class = "text-up" if total_return >= 0 else "text-down"
        total_return_str = f"+{total_return:.2f}%" if total_return >= 0 else f"{total_return:.2f}%"
        
        return f'''
        <div class="v4-card mb-6">
            <div class="v4-card-header">
                <span>💼</span> 持仓股跟踪
                <span class="v4-tag v4-tag-blue" style="margin-left: auto;">共 {len(stocks)} 只</span>
            </div>
            <div class="v4-card-body">
                <!-- 整体概览 -->
                <div class="v4-data-grid cols-3" style="margin-bottom: 24px;">
                    <div class="v4-data-item">
                        <div class="label">组合收益</div>
                        <div class="value {total_return_class}">{total_return_str}</div>
                    </div>
                    <div class="v4-data-item">
                        <div class="label">整体风险</div>
                        <div class="value">{self.portfolio_result.overall_risk_level}风险</div>
                    </div>
                    <div class="v4-data-item">
                        <div class="label">内容深度</div>
                        <div class="value text-blue">{self.portfolio_result.depth_score:.0f}分</div>
                    </div>
                </div>
                
                <!-- 股票列表 -->
                <div style="display: grid; gap: 16px;">
                    {stocks_html}
                </div>
            </div>
        </div>
        '''
    
    def _render_hot_sectors(self) -> str:
        """渲染热门板块模块"""
        if not self.market_result or not self.market_result.hot_sectors:
            # 没有数据时显示占位
            sectors_html = '''
            <div class="v4-list-item">
                <span class="item-label">暂无热门板块数据</span>
                <span class="text-muted">数据更新中</span>
            </div>
            '''
        else:
            sectors = self.market_result.hot_sectors[:8]
            sectors_html = ""
            for i, sector in enumerate(sectors):
                change_class = "text-up" if sector.change_pct >= 0 else "text-down"
                change_str = f"+{sector.change_pct:.2f}%" if sector.change_pct >= 0 else f"{sector.change_pct:.2f}%"
                
                rank_badge = ""
                if i < 3:
                    colors = ['#EF4444', '#F97316', '#EAB308']
                    rank_badge = f'<span style="display: inline-block; width: 24px; height: 24px; line-height: 24px; text-align: center; background: {colors[i]}; color: white; border-radius: 50%; font-size: 12px; font-weight: 600; margin-right: 12px;">{i+1}</span>'
                else:
                    rank_badge = f'<span style="display: inline-block; width: 24px; height: 24px; line-height: 24px; text-align: center; background: #E2E8F0; color: #64748B; border-radius: 50%; font-size: 12px; font-weight: 600; margin-right: 12px;">{i+1}</span>'
                
                sectors_html += f'''
                <div class="v4-list-item">
                    <div style="display: flex; align-items: center;">
                        {rank_badge}
                        <div>
                            <div class="font-medium text-primary">{sector.name}</div>
                            {f'<div class="text-xs text-secondary">{sector.reason}</div>' if sector.reason else ''}
                        </div>
                    </div>
                    <span class="item-value {change_class}">{change_str}</span>
                </div>
                '''
        
        return f'''
        <div class="v4-card mb-6">
            <div class="v4-card-header">
                <span>🔥</span> 热点板块扫描
            </div>
            <div class="v4-card-body">
                {sectors_html}
            </div>
        </div>
        '''
    
    def _render_strategy_section(self) -> str:
        """渲染操作策略模块"""
        if not self.market_result:
            return ""
        
        return f'''
        <div class="v4-card mb-6">
            <div class="v4-card-header">
                <span>📝</span> 操作策略建议
            </div>
            <div class="v4-card-body">
                <div class="v4-alert info">
                    <strong>核心策略：</strong>{self.market_result.strategy_suggestion}
                </div>
                
                <div style="margin-top: 20px;">
                    <h4 style="margin: 0 0 12px 0; color: #1E293B;">📌 今日关注要点</h4>
                    <ul style="color: #64748B; line-height: 2; padding-left: 20px; margin: 0;">
                        <li>市场整体处于{self.market_result.market_trend}格局，情绪{self.market_result.sentiment.sentiment_level}</li>
                        <li>持仓以结构性机会为主，重点关注科技成长方向</li>
                        <li>严格执行止损纪律，跌破止损位的标的及时减仓</li>
                        <li>关注量能变化，放量突破可适当加仓，缩量反弹需谨慎</li>
                    </ul>
                </div>
            </div>
        </div>
        '''
    
    def _render_risk_warning(self) -> str:
        """渲染风险警示模块"""
        if not self.portfolio_result:
            return ""
        
        high_risk_stocks = [s for s in self.portfolio_result.stocks if s.risk_level == "高"]
        
        risk_items = []
        risk_items.append("市场波动风险：外围市场不确定性可能导致A股大幅波动")
        risk_items.append("板块轮动风险：热点切换频繁，追高容易被套")
        
        if high_risk_stocks:
            stock_names = "、".join([s.name for s in high_risk_stocks])
            risk_items.append(f"个股风险：{stock_names} 处于高风险状态，需密切关注")
        
        risk_items.append("政策不及预期风险：重要政策落地时间或力度可能不达预期")
        
        risks_html = ""
        for risk in risk_items:
            risks_html += f'<li style="margin-bottom: 8px;">{risk}</li>'
        
        return f'''
        <div class="v4-card mb-6">
            <div class="v4-card-header">
                <span>⚠️</span> 风险提示
            </div>
            <div class="v4-card-body">
                <div class="v4-alert warning">
                    <ul style="margin: 0; padding-left: 20px;">
                        {risks_html}
                    </ul>
                </div>
                <p style="font-size: 0.75rem; color: #94A3B8; margin: 12px 0 0 0;">
                    免责声明：本报告仅供参考，不构成投资建议。投资有风险，入市需谨慎。
                </p>
            </div>
        </div>
        '''
    
    def _render_footer(self) -> str:
        """渲染页脚"""
        return f'''
        <div style="text-align: center; padding: 40px 0; color: #94A3B8; font-size: 0.875rem;">
            <p>投资研究中心 · S级催化扫描 V4</p>
            <p style="margin-top: 4px;">数据来源：腾讯财经、东方财富 · 仅供参考，不构成投资建议</p>
        </div>
        '''
    
    def generate(self) -> str:
        """生成完整页面"""
        # 加载数据
        self.load_data()
        
        # 构建页面各部分
        nav = self._render_nav("S级催化")
        header = self._render_page_header()
        market_overview = self._render_market_overview()
        portfolio = self._render_portfolio_section()
        hot_sectors = self._render_hot_sectors()
        strategy = self._render_strategy_section()
        risk_warning = self._render_risk_warning()
        footer = self._render_footer()
        
        # 获取主题CSS
        theme_css = get_v4_theme_css()
        
        html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>S级催化扫描 - 投资研究中心</title>
    {theme_css}
    <style>
        body {{
            margin: 0;
            padding: 0;
        }}
        .mb-6 {{ margin-bottom: 24px; }}
        .font-semibold {{ font-weight: 600; }}
        .font-medium {{ font-weight: 500; }}
        .text-xs {{ font-size: 0.75rem; }}
    </style>
</head>
<body>
    <!-- 阅读进度条 -->
    <div id="progressBar"></div>
    
    <!-- 导航栏 -->
    {nav}
    
    <!-- 主内容区 -->
    <div class="v4-container narrow">
        {header}
        {market_overview}
        {portfolio}
        {hot_sectors}
        {strategy}
        {risk_warning}
        {footer}
    </div>
    
    <!-- 回到顶部按钮 -->
    <button id="backToTop" onclick="scrollToTop()">↑</button>
    
    <script>
        // 阅读进度条
        window.onscroll = function() {{
            var scrollTop = document.documentElement.scrollTop || document.body.scrollTop;
            var scrollHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight;
            var progress = (scrollTop / scrollHeight) * 100;
            document.getElementById("progressBar").style.width = progress + "%";
            
            // 回到顶部按钮
            var backBtn = document.getElementById("backToTop");
            if (scrollTop > 300) {{
                backBtn.classList.add("visible");
            }} else {{
                backBtn.classList.remove("visible");
            }}
        }};
        
        function scrollToTop() {{
            window.scrollTo({{ top: 0, behavior: "smooth" }});
        }}
    </script>
</body>
</html>'''
        
        return html
    
    def save(self, filepath: str) -> str:
        """保存到文件"""
        html = self.generate()
        
        # 确保目录存在
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
        
        return filepath


if __name__ == "__main__":
    # 测试生成
    generator = SLevelCatalystV4Generator(data_dir="data")
    output_path = generator.save("../../docs/s-level-catalyst/test_v4.html")
    print(f"✅ V4页面已生成：{output_path}")
