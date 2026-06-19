"""
预警系统 - V4版（新版设计）
基于V4BaseGenerator基类，采用v4_test.html设计风格
特色：多维度预警、实时监控、风险分级
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from generators.v4_base import V4BaseGenerator


class AlertSystemV4(V4BaseGenerator):
    """预警系统V4生成器"""
    
    def __init__(self, data_dir: str = "data"):
        super().__init__(data_dir)
        self.page_title = "🚨 智能预警系统"
        self.page_subtitle = "多维度风险监控 · 实时预警推送 · 智能风控管理"
        self.active_nav_key = "alert_system"
        self.toc_items = [
            ("市场概览", "section-overview"),
            ("持仓预警", "section-portfolio"),
            ("市场预警", "section-market"),
            ("板块预警", "section-sector"),
            ("预警历史", "section-history"),
            ("风险提示", "section-risk"),
        ]
    
    def render_portfolio_alerts(self) -> str:
        """渲染持仓预警模块"""
        alerts = [
            {
                "stock": "英维克",
                "code": "002837",
                "level": "warning",
                "type": "止损预警",
                "message": "当前价格74.37元，已低于止损位98元",
                "change": "-24.0%",
                "time": "持续中",
            },
            {
                "stock": "铜冠铜箔",
                "code": "301217",
                "level": "info",
                "type": "止盈提醒",
                "message": "当前价格200.00元，浮盈超过100%，建议分批止盈",
                "change": "+108.5%",
                "time": "今日",
            },
            {
                "stock": "雅克科技",
                "code": "002409",
                "level": "info",
                "type": "趋势追踪",
                "message": "连续3日上涨，趋势向上，可继续持有",
                "change": "+15.2%",
                "time": "3天",
            },
            {
                "stock": "*ST建艺",
                "code": "002789",
                "level": "warning",
                "type": "高风险提示",
                "message": "ST股票存在退市风险，注意仓位控制",
                "change": "+5.3%",
                "time": "持续关注",
            },
        ]
        
        alerts_html = ""
        for alert in alerts:
            level_colors = {
                "danger": ("#DC2626", "rgba(220, 38, 38, 0.1)"),
                "warning": ("#F59E0B", "rgba(245, 158, 11, 0.1)"),
                "info": ("#3B82F6", "rgba(59, 130, 246, 0.1)"),
                "success": ("#10B981", "rgba(16, 185, 129, 0.1)"),
            }
            primary_color, bg_color = level_colors.get(alert["level"], level_colors["info"])
            
            level_icons = {
                "danger": "🔴",
                "warning": "🟡",
                "info": "🔵",
                "success": "🟢",
            }
            icon = level_icons.get(alert["level"], "🔵")
            
            alerts_html += f'''
            <div class="alert-item" style="border-left: 4px solid {primary_color};">
                <div class="alert-header">
                    <span class="alert-icon">{icon}</span>
                    <div class="alert-stock-info">
                        <span class="alert-stock-name">{alert["stock"]}</span>
                        <span class="alert-stock-code">{alert["code"]}</span>
                    </div>
                    <span class="alert-type-badge" style="background: {bg_color}; color: {primary_color};">{alert["type"]}</span>
                </div>
                <p class="alert-message">{alert["message"]}</p>
                <div class="alert-footer">
                    <span class="alert-change" style="color: {primary_color};">{alert["change"]}</span>
                    <span class="alert-time">{alert["time"]}</span>
                </div>
            </div>
            '''
        
        return f'''
        <section class="v4-section" id="section-portfolio">
            {self.render_section_header("💼 持仓预警", "个股风险监控", "v4-tag-orange")}
            <div class="alert-list">
                {alerts_html}
            </div>
        </section>
        '''
    
    def render_market_alerts(self) -> str:
        """渲染市场预警模块"""
        market_alerts = [
            {"type": "市场情绪", "level": "info", "value": "62", "desc": "市场情绪处于偏乐观区间"},
            {"type": "涨跌停比", "level": "success", "value": "45/3", "desc": "涨停家数远多于跌停，赚钱效应好"},
            {"type": "成交量", "level": "info", "value": "1.2万亿", "desc": "成交量维持活跃水平"},
            {"type": "北向资金", "level": "success", "value": "+58亿", "desc": "北向资金持续流入"},
        ]
        
        items_html = ""
        for alert in market_alerts:
            level_colors = {
                "danger": "#DC2626",
                "warning": "#F59E0B",
                "info": "#3B82F6",
                "success": "#10B981",
            }
            color = level_colors.get(alert["level"], "#64748B")
            
            items_html += f'''
            <div class="market-alert-item">
                <div class="market-alert-type">{alert["type"]}</div>
                <div class="market-alert-value" style="color: {color};">{alert["value"]}</div>
                <div class="market-alert-desc">{alert["desc"]}</div>
            </div>
            '''
        
        return f'''
        <section class="v4-section" id="section-market">
            {self.render_section_header("📊 市场预警", "大盘风险监控", "v4-tag-blue")}
            <div class="market-alert-grid">
                {items_html}
            </div>
        </section>
        '''
    
    def render_alert_history(self) -> str:
        """渲染预警历史模块"""
        history = [
            {"date": "2026-06-15", "count": 3, "level": "warning", "desc": "铜冠铜箔止盈提醒、英维克止损预警等"},
            {"date": "2026-06-12", "count": 2, "level": "info", "desc": "雅克科技买入信号、存储板块机会提示"},
            {"date": "2026-06-10", "count": 1, "level": "success", "desc": "市场情绪回暖提示"},
            {"date": "2026-06-08", "count": 4, "level": "danger", "desc": "市场回调风险预警、多股止损提醒"},
        ]
        
        history_html = ""
        for item in history:
            level_dots = {
                "danger": "#DC2626",
                "warning": "#F59E0B",
                "info": "#3B82F6",
                "success": "#10B981",
            }
            dot_color = level_dots.get(item["level"], "#64748B")
            
            history_html += f'''
            <div class="history-item">
                <div class="history-dot" style="background: {dot_color};"></div>
                <div class="history-content">
                    <div class="history-header">
                        <span class="history-date">{item["date"]}</span>
                        <span class="history-count">{item["count"]}条预警</span>
                    </div>
                    <p class="history-desc">{item["desc"]}</p>
                </div>
            </div>
            '''
        
        return f'''
        <section class="v4-section" id="section-history">
            {self.render_section_header("📋 预警历史", "历史记录", "v4-tag-gray")}
            <div class="v4-card">
                <div class="alert-history-list">
                    {history_html}
                </div>
            </div>
        </section>
        '''
    
    def render_content(self) -> str:
        """渲染页面内容"""
        # 头部统计卡片
        header_stats = f'''
        <div class="v4-header-stats">
            <div class="v4-stat-card">
                <div class="v4-stat-value" style="color: #F59E0B;">2</div>
                <div class="v4-stat-label">活跃预警</div>
            </div>
            <div class="v4-stat-card">
                <div class="v4-stat-value" style="color: #10B981;">4</div>
                <div class="v4-stat-label">监控标的</div>
            </div>
            <div class="v4-stat-card">
                <div class="v4-stat-value" style="color: #8B5CF6;">10</div>
                <div class="v4-stat-label">预警维度</div>
            </div>
            <div class="v4-stat-card">
                <div class="v4-stat-value" style="color: #EC4899;">实时</div>
                <div class="v4-stat-label">监控频率</div>
            </div>
        </div>
        '''
        
        header = self.render_page_header(extra_html=header_stats)
        market_overview = self.render_market_overview_v2()
        portfolio_alerts = self.render_portfolio_alerts()
        market_alerts = self.render_market_alerts()
        alert_history = self.render_alert_history()
        risk_warning = self.render_risk_warning()
        
        return f'''
        {header}
        {market_overview}
        {portfolio_alerts}
        {market_alerts}
        {alert_history}
        {risk_warning}
        '''
    
    def get_page_css(self) -> str:
        """页面特有CSS - 新版设计风格"""
        return '''
        /* 预警列表 */
        .alert-list {
            display: flex;
            flex-direction: column;
            gap: 12px;
        }
        .alert-item {
            padding: 18px;
            background: white;
            border-radius: 12px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.06);
        }
        .alert-header {
            display: flex;
            align-items: center;
            gap: 12px;
            margin-bottom: 10px;
        }
        .alert-icon {
            font-size: 20px;
        }
        .alert-stock-info {
            flex: 1;
        }
        .alert-stock-name {
            font-size: 16px;
            font-weight: 600;
            color: #1E293B;
            margin-right: 8px;
        }
        .alert-stock-code {
            font-size: 12px;
            color: #94A3B8;
        }
        .alert-type-badge {
            padding: 4px 12px;
            border-radius: 6px;
            font-size: 12px;
            font-weight: 500;
        }
        .alert-message {
            font-size: 14px;
            color: #475569;
            margin: 0 0 12px 0;
            line-height: 1.5;
        }
        .alert-footer {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding-top: 10px;
            border-top: 1px solid #F1F5F9;
        }
        .alert-change {
            font-size: 14px;
            font-weight: 600;
        }
        .alert-time {
            font-size: 12px;
            color: #94A3B8;
        }
        
        /* 市场预警 */
        .market-alert-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 16px;
        }
        .market-alert-item {
            padding: 20px;
            background: white;
            border-radius: 12px;
            text-align: center;
            box-shadow: 0 2px 8px rgba(0,0,0,0.06);
        }
        .market-alert-type {
            font-size: 13px;
            color: #64748B;
            margin-bottom: 8px;
        }
        .market-alert-value {
            font-size: 24px;
            font-weight: 700;
            margin-bottom: 6px;
        }
        .market-alert-desc {
            font-size: 12px;
            color: #94A3B8;
        }
        
        /* 预警历史 */
        .alert-history-list {
            display: flex;
            flex-direction: column;
            gap: 0;
        }
        .history-item {
            display: flex;
            gap: 14px;
            padding: 14px 0;
            position: relative;
        }
        .history-item:not(:last-child)::after {
            content: '';
            position: absolute;
            left: 5px;
            top: 30px;
            bottom: -14px;
            width: 2px;
            background: #E2E8F0;
        }
        .history-dot {
            width: 12px;
            height: 12px;
            border-radius: 50%;
            flex-shrink: 0;
            margin-top: 4px;
        }
        .history-content {
            flex: 1;
        }
        .history-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 4px;
        }
        .history-date {
            font-size: 14px;
            font-weight: 600;
            color: #1E293B;
        }
        .history-count {
            font-size: 12px;
            color: #64748B;
        }
        .history-desc {
            font-size: 13px;
            color: #64748B;
            margin: 0;
        }
        
        /* 标签颜色 */
        .v4-tag-orange {
            background: rgba(245, 158, 11, 0.1);
            color: #D97706;
        }
        .v4-tag-blue {
            background: rgba(59, 130, 246, 0.1);
            color: #2563EB;
        }
        .v4-tag-gray {
            background: rgba(100, 116, 139, 0.1);
            color: #475569;
        }
        
        /* 响应式 */
        @media (max-width: 640px) {
            .market-alert-grid {
                grid-template-columns: repeat(2, 1fr);
            }
        }
        '''


if __name__ == '__main__':
    generator = AlertSystemV4(data_dir='data')
    html = generator.generate()
    output_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '..', 'docs', 'alert_system_v4.html')
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"✅ 预警系统V4已生成 -> {output_path}")
