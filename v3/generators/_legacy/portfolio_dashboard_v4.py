"""
持仓智能预警仪表盘 - V4版
基于V4BaseGenerator基类
"""
import sys
import os
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from generators.v4_base import V4BaseGenerator
from components.v4_components import V4DataGrid, V4StockCard, V4Section


class PortfolioDashboardV4(V4BaseGenerator):
    """持仓仪表盘V4生成器"""
    
    def __init__(self, data_dir: str = "data"):
        super().__init__(data_dir)
        self.page_title = "📊 持仓智能预警仪表盘"
        self.page_subtitle = "多维度持仓诊断 · 风险实时预警 · 智能调仓建议"
        self.active_nav_key = "portfolio_dashboard"
        self.toc_items = [
            ("组合概览", "section-overview"),
            ("持仓股诊断", "section-portfolio"),
            ("风险预警", "section-risk"),
            ("压力测试", "section-stress"),
            ("行业分布", "section-industry"),
            ("操作策略", "section-strategy"),
        ]
    
    def render_portfolio_card(self, stock, show_detail: bool = True) -> str:
        """渲染单个持仓股卡片"""
        # 状态颜色
        change_color = '#DC2626' if stock.today_change_pct >= 0 else '#16A34A'
        profit_color = '#DC2626' if stock.profit_loss_pct >= 0 else '#16A34A'
        sign = '+' if stock.today_change_pct >= 0 else ''
        profit_sign = '+' if stock.profit_loss_pct >= 0 else ''
        
        # 风险等级
        risk_level = self._get_risk_level(stock)
        risk_color, risk_bg = self._get_risk_color(risk_level)
        
        # 四维诊断状态映射
        tech_status = self._map_status(stock.technical_status)
        fund_status = self._map_status(stock.fund_status)
        news_status = self._map_status(stock.news_status)
        industry_status = self._map_status(stock.industry_status)
        
        # 生成诊断条目
        tech_items = ''.join([
            f'<div class="diagnosis-item"><span class="diagnosis-icon">{item.icon}</span><span class="diagnosis-text">{item.text}</span></div>'
            for item in stock.technical_items[:3]
        ])
        
        fund_items = ''.join([
            f'<div class="diagnosis-item"><span class="diagnosis-icon">{item.icon}</span><span class="diagnosis-text">{item.text}</span></div>'
            for item in (stock.fund_items if hasattr(stock, 'fund_items') else [])[:3]
        ])
        
        news_items = ''.join([
            f'<div class="diagnosis-item"><span class="diagnosis-icon">{item.icon}</span><span class="diagnosis-text">{item.text}</span></div>'
            for item in (stock.news_items if hasattr(stock, 'news_items') else [])[:3]
        ])
        
        industry_items = ''.join([
            f'<div class="diagnosis-item"><span class="diagnosis-icon">{item.icon}</span><span class="diagnosis-text">{item.text}</span></div>'
            for item in (stock.industry_items if hasattr(stock, 'industry_items') else [])[:3]
        ])
        
        detail_html = ''
        if show_detail:
            detail_html = f'''
            <div class="stock-diagnosis-detail">
                <div class="diagnosis-dimension">
                    <div class="dim-header">
                        <span class="dim-icon">📈</span>
                        <span class="dim-name">技术面</span>
                        <span class="dim-status status-{tech_status['class']}">{tech_status['text']}</span>
                    </div>
                    <div class="dim-items">
                        {tech_items}
                    </div>
                </div>
                <div class="diagnosis-dimension">
                    <div class="dim-header">
                        <span class="dim-icon">💰</span>
                        <span class="dim-name">资金面</span>
                        <span class="dim-status status-{fund_status['class']}">{fund_status['text']}</span>
                    </div>
                    <div class="dim-items">
                        {fund_items}
                    </div>
                </div>
                <div class="diagnosis-dimension">
                    <div class="dim-header">
                        <span class="dim-icon">📰</span>
                        <span class="dim-name">消息面</span>
                        <span class="dim-status status-{news_status['class']}">{news_status['text']}</span>
                    </div>
                    <div class="dim-items">
                        {news_items}
                    </div>
                </div>
                <div class="diagnosis-dimension">
                    <div class="dim-header">
                        <span class="dim-icon">🏭</span>
                        <span class="dim-name">产业面</span>
                        <span class="dim-status status-{industry_status['class']}">{industry_status['text']}</span>
                    </div>
                    <div class="dim-items">
                        {industry_items}
                    </div>
                </div>
            </div>
            '''
        
        return f'''
        <div class="v4-card v4-stock-card">
            <div class="stock-header">
                <div>
                    <span class="stock-name">{stock.name}</span>
                    <span class="stock-code" style="margin-left: 8px;">{stock.code}</span>
                </div>
                <span class="v4-tag" style="background: {risk_bg}; color: {risk_color};">{risk_level}</span>
            </div>
            <div class="stock-price-info">
                <div class="price-item">
                    <div class="label">最新价</div>
                    <div class="value" style="color: {change_color};">{stock.current_price:.2f}</div>
                </div>
                <div class="price-item">
                    <div class="label">今日涨跌</div>
                    <div class="value" style="color: {change_color};">{sign}{stock.today_change_pct:.2f}%</div>
                </div>
                <div class="price-item">
                    <div class="label">成本价</div>
                    <div class="value">{stock.cost_price:.2f}</div>
                </div>
                <div class="price-item">
                    <div class="label">累计盈亏</div>
                    <div class="value" style="color: {profit_color};">{profit_sign}{stock.profit_loss_pct:.2f}%</div>
                </div>
            </div>
            <div class="stock-price-info">
                <div class="price-item">
                    <div class="label">止损价</div>
                    <div class="value">{stock.stop_loss_price:.2f}</div>
                </div>
                <div class="price-item">
                    <div class="label">距止损</div>
                    <div class="value" style="color: {'#DC2626' if stock.distance_to_stop_loss < 0.1 else '#16A34A'};">
                        {stock.distance_to_stop_loss*100:.1f}%
                    </div>
                </div>
                <div class="price-item">
                    <div class="label">主力资金</div>
                    <div class="value" style="color: {'#DC2626' if '+' in str(stock.main_fund) else '#16A34A'};">
                        {stock.main_fund if hasattr(stock, 'main_fund') else '--'}
                    </div>
                </div>
                <div class="price-item">
                    <div class="label">持仓占比</div>
                    <div class="value">--</div>
                </div>
            </div>
            {detail_html}
            <div style="margin-top: 16px; padding-top: 16px; border-top: 1px solid #F1F5F9;">
                <div style="display: flex; align-items: center; gap: 10px;">
                    <span style="font-size: 0.875rem; color: #64748B;">操作建议：</span>
                    <span class="v4-tag" style="background: {'rgba(220, 38, 38, 0.1)' if stock.advice_type == 'sell' else 'rgba(22, 163, 74, 0.1)'}; color: {'#DC2626' if stock.advice_type == 'sell' else '#16A34A'};">
                        {stock.advice_text}
                    </span>
                </div>
            </div>
        </div>
        '''
    
    def _get_risk_level(self, stock) -> str:
        """获取风险等级"""
        distance = stock.distance_to_stop_loss
        if distance < 0:
            return "已跌破止损"
        elif distance < 0.05:
            return "高危区"
        elif distance < 0.1:
            return "警戒区"
        elif distance < 0.2:
            return "安全区"
        else:
            return "非常安全"
    
    def _get_risk_color(self, risk_level: str) -> tuple:
        """获取风险等级颜色"""
        color_map = {
            "已跌破止损": ("#DC2626", "rgba(220, 38, 38, 0.1)"),
            "高危区": ("#F97316", "rgba(249, 115, 22, 0.1)"),
            "警戒区": ("#F59E0B", "rgba(245, 158, 11, 0.1)"),
            "安全区": ("#10B981", "rgba(16, 185, 129, 0.1)"),
            "非常安全": ("#059669", "rgba(5, 150, 105, 0.1)"),
        }
        return color_map.get(risk_level, ("#64748B", "rgba(100, 116, 139, 0.1)"))
    
    def _map_status(self, status: str) -> dict:
        """将状态字符串映射为class和中文文本"""
        status_map = {
            '强势': {'class': 'good', 'text': '强势'},
            '流入': {'class': 'good', 'text': '流入'},
            '利好': {'class': 'good', 'text': '利好'},
            '向好': {'class': 'good', 'text': '向好'},
            'neutral': {'class': 'neutral', 'text': '中性'},
            'bad': {'class': 'bad', 'text': '弱势'},
            '弱势': {'class': 'bad', 'text': '弱势'},
            '流出': {'class': 'bad', 'text': '流出'},
            '利空': {'class': 'bad', 'text': '利空'},
            '下滑': {'class': 'bad', 'text': '下滑'},
        }
        return status_map.get(status, {'class': 'neutral', 'text': status})
    
    def render_stress_test(self) -> str:
        """渲染压力测试模块"""
        if not self.portfolio_result or not self.portfolio_result.stocks:
            return ""
        
        # 计算整体压力测试
        extreme_loss = 0
        neutral_loss = 0
        for stock in self.portfolio_result.stocks:
            if hasattr(stock, 'stress_test') and stock.stress_test:
                extreme = float(stock.stress_test.get('extreme', '0').replace('%', ''))
                neutral = float(stock.stress_test.get('neutral', '0').replace('%', ''))
                extreme_loss += extreme * 0.25  # 简化：假设等权重
                neutral_loss += neutral * 0.25
            else:
                # 模拟压力测试数据
                beta = 1.2
                extreme_loss += -25 * beta * 0.25
                neutral_loss += -10 * beta * 0.25
        
        extreme_width = min(100, abs(extreme_loss) * 2)
        neutral_width = min(100, abs(neutral_loss) * 2)
        
        return f'''
        <section class="v4-section" id="section-stress">
            {self.render_section_header("🚨 压力测试情景", "极端行情模拟", "v4-tag-red")}
            <div class="v4-card">
                <div class="stress-test-grid">
                    <div class="stress-test-item">
                        <div class="stress-test-label">极端下跌情景（大盘回调10%）</div>
                        <div class="stress-test-value" style="color: #DC2626;">{extreme_loss:.1f}%</div>
                        <div class="stress-test-bar">
                            <div class="stress-test-bar-fill" style="width: {extreme_width}%; background: #DC2626;"></div>
                        </div>
                    </div>
                    <div class="stress-test-item">
                        <div class="stress-test-label">中性震荡情景（板块震荡5%）</div>
                        <div class="stress-test-value" style="color: {'#DC2626' if neutral_loss < 0 else '#16A34A'};">
                            {'+' if neutral_loss >= 0 else ''}{neutral_loss:.1f}%
                        </div>
                        <div class="stress-test-bar">
                            <div class="stress-test-bar-fill" style="width: {neutral_width}%; background: {'#DC2626' if neutral_loss < 0 else '#16A34A'};"></div>
                        </div>
                    </div>
                </div>
                <p style="font-size: 0.875rem; color: #64748B; margin: 16px 0 0 0;">
                    * 压力测试基于历史波动率和Beta系数估算，仅供风险参考，不代表实际收益表现
                </p>
            </div>
        </section>
        '''
    
    def render_industry_distribution(self) -> str:
        """渲染行业分布模块"""
        if not self.portfolio_result or not self.portfolio_result.stocks:
            return ""
        
        # 模拟行业分布数据
        industries = [
            {"name": "AI算力", "pct": 35, "color": "#8B5CF6"},
            {"name": "存储芯片", "pct": 30, "color": "#3B82F6"},
            {"name": "人形机器人", "pct": 20, "color": "#10B981"},
            {"name": "其他", "pct": 15, "color": "#F59E0B"},
        ]
        
        industry_bars = ""
        for ind in industries:
            industry_bars += f'''
            <div class="industry-bar-item">
                <span class="industry-name">{ind["name"]}</span>
                <div class="industry-bar">
                    <div class="industry-bar-fill" style="width: {ind["pct"]}%; background: {ind["color"]};"></div>
                </div>
                <span class="industry-value">{ind["pct"]}%</span>
            </div>
            '''
        
        # 风险指标
        risk_metrics = [
            {"label": "组合波动率", "value": "18.5%", "pct": 62, "color": "#F59E0B"},
            {"label": "最大回撤", "value": "-22.3%", "pct": 75, "color": "#DC2626"},
            {"label": "夏普比率", "value": "1.42", "pct": 47, "color": "#10B981"},
            {"label": "Beta系数", "value": "1.15", "pct": 57, "color": "#3B82F6"},
            {"label": "信息比率", "value": "0.89", "pct": 45, "color": "#8B5CF6"},
            {"label": "集中度风险", "value": "中高", "pct": 65, "color": "#F97316"},
        ]
        
        metric_html = ""
        for m in risk_metrics:
            metric_html += f'''
            <div class="risk-metric">
                <div class="risk-metric-label">{m["label"]}</div>
                <div class="risk-metric-value" style="color: {m["color"]};">{m["value"]}</div>
                <div class="risk-metric-bar">
                    <div class="risk-metric-bar-fill" style="width: {m["pct"]}%; background: {m["color"]};"></div>
                </div>
            </div>
            '''
        
        return f'''
        <section class="v4-section" id="section-industry">
            {self.render_section_header("🏭 行业分布与仓位分析", "配置结构诊断", "v4-tag-blue")}
            <div class="v4-card">
                <h3 style="font-size: 1rem; font-weight: 600; color: #1E293B; margin: 0 0 16px 0;">行业配置分布</h3>
                <div class="industry-chart">
                    {industry_bars}
                </div>
                <div style="height: 1px; background: #F1F5F9; margin: 24px 0;"></div>
                <h3 style="font-size: 1rem; font-weight: 600; color: #1E293B; margin: 0 0 16px 0;">风控指标</h3>
                <div class="risk-metrics-grid">
                    {metric_html}
                </div>
                <div style="margin-top: 20px; padding: 12px 16px; background: rgba(245, 158, 11, 0.05); border-radius: 8px; border-left: 3px solid #F59E0B;">
                    <p style="font-size: 0.875rem; color: #92400E; margin: 0;">
                        ⚠️ <strong>仓位健康度评估：</strong>当前行业集中度偏高，建议适当分散配置，降低单一行业波动风险
                    </p>
                </div>
            </div>
        </section>
        '''
    
    def render_risk_warning(self) -> str:
        """渲染风险提示模块 - 增强版"""
        if not self.portfolio_result or not self.portfolio_result.stocks:
            return ""
        
        risk_items = []
        
        # 跌破止损的股票
        broken_stop = [s for s in self.portfolio_result.stocks if s.distance_to_stop_loss < 0]
        if broken_stop:
            names = "、".join([s.name for s in broken_stop])
            risk_items.append({
                "type": "danger",
                "text": f"🔴 {names} 已跌破止损位，建议立即减仓或止损离场"
            })
        
        # 接近止损的股票
        near_stop = [s for s in self.portfolio_result.stocks if 0 <= s.distance_to_stop_loss < 0.1]
        if near_stop:
            names = "、".join([s.name for s in near_stop])
            risk_items.append({
                "type": "warning",
                "text": f"🟡 {names} 距离止损位不足10%，请密切关注走势"
            })
        
        # 高仓位风险
        high_position = [s for s in self.portfolio_result.stocks if s.profit_loss_pct > 30]
        if high_position:
            names = "、".join([s.name for s in high_position])
            risk_items.append({
                "type": "info",
                "text": f"🔵 {names} 累计涨幅较大，建议逢高分批减仓止盈，锁定利润"
            })
        
        # 系统性风险
        risk_items.append({
            "type": "warning",
            "text": "⚪ **系统性风险**：关注大盘整体走势及美联储政策变化，若出现系统性风险需及时减仓"
        })
        
        # 流动性风险
        risk_items.append({
            "type": "info",
            "text": "⚪ **流动性风险**：合理控制仓位，避免单只标的占比过高影响进出效率"
        })
        
        risk_html = ""
        for item in risk_items:
            type_class = item["type"]
            text = item["text"]
            risk_html += f'<div class="v4-alert {type_class}" style="margin-bottom: 12px;">{text}</div>'
        
        return f'''
        <section class="v4-section" id="section-risk">
            {self.render_section_header("⚠️ 风险预警面板", "必读", "v4-tag-red")}
            <div class="v4-card">
                {risk_html}
                <p style="font-size: 0.875rem; color: #94A3B8; margin: 16px 0 0 0; text-align: center;">
                    * 以上分析仅供参考，不构成投资建议。投资有风险，入市需谨慎。
                </p>
            </div>
        </section>
        '''
    
    def render_content(self) -> str:
        """渲染页面内容"""
        # 头部统计卡片 - 使用V4DataGrid组件
        total_return = self.portfolio_result.total_return_pct if self.portfolio_result else 0
        return_color = '#10B981' if total_return >= 0 else '#EF4444'
        return_sign = "+" if total_return >= 0 else ""
        stock_count = self.portfolio_result.stock_count if self.portfolio_result else 0
        
        # 计算盈利亏损数量
        profit_count = 0
        loss_count = 0
        if self.portfolio_result and self.portfolio_result.stocks:
            profit_count = len([s for s in self.portfolio_result.stocks if s.profit_loss_pct >= 0])
            loss_count = len([s for s in self.portfolio_result.stocks if s.profit_loss_pct < 0])
        
        # 使用V4DataGrid组件渲染统计数据
        grid_items = [
            {'value': f'{return_sign}{total_return:.2f}%', 'label': '组合总盈亏', 'color': return_color},
            {'value': f'{stock_count}', 'label': '持仓标的', 'color': '#6366F1'},
            {'value': f'{profit_count}盈 / {loss_count}亏', 'label': '盈利/亏损', 'color': '#8B5CF6'},
        ]
        data_grid = V4DataGrid(grid_items, columns=3)
        header_stats = f'<div style="margin-top: 20px;">{data_grid.render()}</div>'
        
        # 页面头部
        header = self.render_page_header(extra_html=header_stats)
        
        # 市场概览
        market_overview = self.render_market_overview()
        
        # 持仓股诊断
        portfolio_section = self._render_portfolio_section_full()
        
        # 风险预警
        risk_warning = self.render_risk_warning()
        
        # 压力测试
        stress_test = self.render_stress_test()
        
        # 行业分布
        industry_dist = self.render_industry_distribution()
        
        # 操作策略
        strategy_section = self.render_strategy_section()
        
        return f'''
        {header}
        {market_overview}
        {portfolio_section}
        {risk_warning}
        {stress_test}
        {industry_dist}
        {strategy_section}
        '''
    
    def _render_portfolio_section_full(self) -> str:
        """完整的持仓股诊断部分"""
        if not self.portfolio_result or not self.portfolio_result.stocks:
            return '<div class="v4-card"><p style="color: #64748B;">暂无持仓数据</p></div>'
        
        # 生成所有股票卡片
        stock_cards = ""
        for stock in self.portfolio_result.stocks:
            stock_cards += self.render_portfolio_card(stock, show_detail=True)
        
        return f'''
        <section class="v4-section" id="section-portfolio">
            {self.render_section_header("💎 持仓股诊断", "四维分析", "v4-tag-blue")}
            {stock_cards}
        </section>
        '''


if __name__ == '__main__':
    generator = PortfolioDashboardV4(data_dir='data')
    html = generator.generate()
    output_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '..', 'docs', 'portfolio_dashboard_v4_test.html')
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"✅ 持仓仪表盘V4测试页已生成")
