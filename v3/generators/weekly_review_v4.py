"""
周复盘 - V4版（新版设计）
基于V4BaseGenerator基类，采用v4_test.html设计风格
特色：深度复盘、经验总结、模式识别、交易反思
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from generators.v4_base import V4BaseGenerator


class WeeklyReviewV4(V4BaseGenerator):
    """周复盘V4生成器"""
    
    def __init__(self, data_dir: str = "data"):
        super().__init__(data_dir)
        self.page_title = "📚 周度复盘"
        self.page_subtitle = "深度交易复盘 · 经验教训总结 · 模式识别优化"
        self.active_nav_key = "weekly_review"
        self.toc_items = [
            ("本周概览", "section-overview"),
            ("交易总结", "section-trades"),
            ("经验教训", "section-lessons"),
            ("模式识别", "section-patterns"),
            ("改进计划", "section-improve"),
            ("风险提示", "section-risk"),
        ]
    
    def render_weekly_overview(self) -> str:
        """渲染本周概览模块"""
        stats = [
            {"label": "本周收益", "value": "+5.8%", "color": "#DC2626"},
            {"label": "交易次数", "value": "8次", "color": "#3B82F6"},
            {"label": "胜率", "value": "62.5%", "color": "#10B981"},
            {"label": "盈亏比", "value": "2.3", "color": "#8B5CF6"},
        ]
        
        stats_html = ""
        for s in stats:
            stats_html += f'''
            <div class="review-stat-card">
                <div class="review-stat-value" style="color: {s["color"]};">{s["value"]}</div>
                <div class="review-stat-label">{s["label"]}</div>
            </div>
            '''
        
        return f'''
        <section class="v4-section" id="section-overview">
            {self.render_section_header("📊 本周概览", "交易数据", "v4-tag-blue")}
            <div class="review-stats-grid">
                {stats_html}
            </div>
        </section>
        '''
    
    def render_trade_summary(self) -> str:
        """渲染交易总结模块"""
        trades = [
            {"date": "6/17", "stock": "铜冠铜箔", "action": "加仓", "result": "盈利", "pct": "+15%", "reason": "存储芯片板块强势，龙头突破"},
            {"date": "6/16", "stock": "雅克科技", "action": "持有", "result": "盈利", "pct": "+8%", "reason": "HBM概念持续发酵"},
            {"date": "6/14", "stock": "英维克", "action": "止损", "result": "亏损", "pct": "-5%", "reason": "跌破止损位，纪律执行"},
        ]
        
        trades_html = ""
        for t in trades:
            result_color = "#DC2626" if t["result"] == "盈利" else "#16A34A"
            
            trades_html += f'''
            <div class="trade-item">
                <div class="trade-date">{t["date"]}</div>
                <div class="trade-stock">{t["stock"]}</div>
                <div class="trade-action">{t["action"]}</div>
                <div class="trade-result" style="color: {result_color};">{t["result"]} {t["pct"]}</div>
                <div class="trade-reason">{t["reason"]}</div>
            </div>
            '''
        
        return f'''
        <section class="v4-section" id="section-trades">
            {self.render_section_header("📋 交易总结", "操作记录", "v4-tag-orange")}
            <div class="v4-card">
                <div class="trade-list-header">
                    <span>日期</span>
                    <span>标的</span>
                    <span>操作</span>
                    <span>结果</span>
                    <span>逻辑</span>
                </div>
                <div class="trade-list">
                    {trades_html}
                </div>
            </div>
        </section>
        '''
    
    def render_lessons_learned(self) -> str:
        """渲染经验教训模块"""
        lessons = [
            {
                "type": "success",
                "title": "趋势持仓的重要性",
                "desc": "铜冠铜箔从买入后一直持有，没有因为短期波动而频繁交易，最终获得了丰厚的收益。",
            },
            {
                "type": "success",
                "title": "止损纪律执行到位",
                "desc": "英维克跌破止损位后坚决卖出，避免了后续更大的亏损，保护了资金安全。",
            },
            {
                "type": "failure",
                "title": "板块轮动把握不足",
                "desc": "错过了新能源汽车板块的反弹机会，对市场风格切换的敏感度需要提升。",
            },
            {
                "type": "failure",
                "title": "仓位管理有待优化",
                "desc": "单只个股仓位过重，导致整体组合波动较大，需要更均衡的仓位配置。",
            },
        ]
        
        lessons_html = ""
        for lesson in lessons:
            icon = "✅" if lesson["type"] == "success" else "❌"
            border_color = "#10B981" if lesson["type"] == "success" else "#F59E0B"
            bg_color = "rgba(16, 185, 129, 0.05)" if lesson["type"] == "success" else "rgba(245, 158, 11, 0.05)"
            
            lessons_html += f'''
            <div class="lesson-item" style="border-left: 4px solid {border_color}; background: {bg_color};">
                <span class="lesson-icon">{icon}</span>
                <div class="lesson-content">
                    <h4 class="lesson-title">{lesson["title"]}</h4>
                    <p class="lesson-desc">{lesson["desc"]}</p>
                </div>
            </div>
            '''
        
        return f'''
        <section class="v4-section" id="section-lessons">
            {self.render_section_header("💡 经验教训", "得失总结", "v4-tag-green")}
            <div class="lessons-list">
                {lessons_html}
            </div>
        </section>
        '''
    
    def render_improvement_plan(self) -> str:
        """渲染改进计划模块"""
        plans = [
            {"priority": "高", "item": "建立板块轮动监控机制，每周评估各板块强弱", "status": "pending"},
            {"priority": "高", "item": "优化仓位管理模型，单只个股仓位不超过20%", "status": "pending"},
            {"priority": "中", "item": "增加对中小市值股票的研究覆盖", "status": "ongoing"},
            {"priority": "中", "item": "完善交易日志记录格式", "status": "done"},
            {"priority": "低", "item": "学习量化交易基础知识", "status": "pending"},
        ]
        
        plans_html = ""
        for p in plans:
            priority_colors = {"高": "#DC2626", "中": "#F59E0B", "低": "#64748B"}
            priority_color = priority_colors.get(p["priority"], "#64748B")
            
            status_icons = {"pending": "⏳", "ongoing": "🔄", "done": "✅"}
            icon = status_icons.get(p["status"], "⏳")
            
            plans_html += f'''
            <div class="improvement-item">
                <span class="improve-priority" style="background: {priority_color}15; color: {priority_color};">{p["priority"]}</span>
                <span class="improve-item">{p["item"]}</span>
                <span class="improve-status">{icon}</span>
            </div>
            '''
        
        return f'''
        <section class="v4-section" id="section-improve">
            {self.render_section_header("🎯 改进计划", "下周行动", "v4-tag-purple")}
            <div class="v4-card">
                <div class="improvement-list">
                    {plans_html}
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
                <div class="v4-stat-value" style="color: #DC2626;">+5.8%</div>
                <div class="v4-stat-label">本周收益</div>
            </div>
            <div class="v4-stat-card">
                <div class="v4-stat-value" style="color: #10B981;">62.5%</div>
                <div class="v4-stat-label">胜率</div>
            </div>
            <div class="v4-stat-card">
                <div class="v4-stat-value" style="color: #8B5CF6;">2.3</div>
                <div class="v4-stat-label">盈亏比</div>
            </div>
            <div class="v4-stat-card">
                <div class="v4-stat-value" style="color: #F59E0B;">4</div>
                <div class="v4-stat-label">经验总结</div>
            </div>
        </div>
        '''
        
        header = self.render_page_header(extra_html=header_stats)
        market_overview = self.render_market_overview_v2()
        weekly_overview = self.render_weekly_overview()
        trade_summary = self.render_trade_summary()
        lessons = self.render_lessons_learned()
        improvement = self.render_improvement_plan()
        risk_warning = self.render_risk_warning()
        
        return f'''
        {header}
        {market_overview}
        {weekly_overview}
        {trade_summary}
        {lessons}
        {improvement}
        {risk_warning}
        '''
    
    def get_page_css(self) -> str:
        """页面特有CSS - 新版设计风格"""
        return '''
        /* 复盘统计 */
        .review-stats-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
            gap: 16px;
        }
        .review-stat-card {
            padding: 24px 20px;
            background: white;
            border-radius: 14px;
            text-align: center;
            box-shadow: 0 2px 8px rgba(0,0,0,0.06);
        }
        .review-stat-value {
            font-size: 28px;
            font-weight: 800;
            margin-bottom: 8px;
        }
        .review-stat-label {
            font-size: 13px;
            color: #64748B;
        }
        
        /* 交易列表 */
        .trade-list-header {
            display: grid;
            grid-template-columns: 50px 80px 60px 80px 1fr;
            gap: 12px;
            padding: 12px 16px;
            font-size: 12px;
            font-weight: 600;
            color: #64748B;
            background: #F8FAFC;
            border-radius: 8px;
            margin-bottom: 8px;
        }
        .trade-list {
            display: flex;
            flex-direction: column;
            gap: 8px;
        }
        .trade-item {
            display: grid;
            grid-template-columns: 50px 80px 60px 80px 1fr;
            gap: 12px;
            padding: 12px 16px;
            background: white;
            border-radius: 8px;
            align-items: center;
            font-size: 13px;
        }
        .trade-date {
            color: #64748B;
        }
        .trade-stock {
            font-weight: 600;
            color: #1E293B;
        }
        .trade-action {
            color: #475569;
        }
        .trade-result {
            font-weight: 600;
        }
        .trade-reason {
            color: #64748B;
            font-size: 12px;
        }
        
        /* 经验教训 */
        .lessons-list {
            display: flex;
            flex-direction: column;
            gap: 12px;
        }
        .lesson-item {
            display: flex;
            gap: 14px;
            padding: 18px;
            border-radius: 12px;
        }
        .lesson-icon {
            font-size: 20px;
            flex-shrink: 0;
        }
        .lesson-content {
            flex: 1;
        }
        .lesson-title {
            font-size: 15px;
            font-weight: 600;
            color: #1E293B;
            margin: 0 0 6px 0;
        }
        .lesson-desc {
            font-size: 13px;
            color: #64748B;
            margin: 0;
            line-height: 1.6;
        }
        
        /* 改进计划 */
        .improvement-list {
            display: flex;
            flex-direction: column;
            gap: 10px;
        }
        .improvement-item {
            display: flex;
            align-items: center;
            gap: 14px;
            padding: 12px 16px;
            background: #F8FAFC;
            border-radius: 10px;
        }
        .improve-priority {
            padding: 3px 10px;
            border-radius: 6px;
            font-size: 11px;
            font-weight: 600;
            flex-shrink: 0;
        }
        .improve-item {
            flex: 1;
            font-size: 14px;
            color: #1E293B;
        }
        .improve-status {
            font-size: 16px;
        }
        
        /* 标签颜色 */
        .v4-tag-blue {
            background: rgba(37, 99, 235, 0.1);
            color: #2563EB;
        }
        .v4-tag-orange {
            background: rgba(245, 158, 11, 0.1);
            color: #D97706;
        }
        .v4-tag-green {
            background: rgba(16, 185, 129, 0.1);
            color: #10B981;
        }
        .v4-tag-purple {
            background: rgba(139, 92, 246, 0.1);
            color: #7C3AED;
        }
        
        /* 响应式 */
        @media (max-width: 640px) {
            .trade-list-header,
            .trade-item {
                grid-template-columns: 40px 70px 50px 70px 1fr;
                font-size: 11px;
            }
        }
        '''


if __name__ == '__main__':
    generator = WeeklyReviewV4(data_dir='data')
    html = generator.generate()
    output_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '..', 'docs', 'weekly_review_v4.html')
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"✅ 周复盘V4已生成 -> {output_path}")
