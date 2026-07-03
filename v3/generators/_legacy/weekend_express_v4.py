"""
周末速递 - V4版（新版设计）
基于V4BaseGenerator基类，采用v4_test.html设计风格
特色：周度策略、板块机会、个股精选
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from generators.v4_base import V4BaseGenerator


class WeekendExpressV4(V4BaseGenerator):
    """周末速递V4生成器"""
    
    def __init__(self, data_dir: str = "data"):
        super().__init__(data_dir)
        self.page_title = "📅 周末速递"
        self.page_subtitle = "周度投资策略 · 板块机会挖掘 · 个股精选推荐"
        self.active_nav_key = "weekend_express"
        self.toc_items = [
            ("本周回顾", "section-review"),
            ("下周展望", "section-outlook"),
            ("重点板块", "section-sectors"),
            ("个股精选", "section-stocks"),
            ("策略建议", "section-strategy"),
            ("风险提示", "section-risk"),
        ]
    
    def render_week_review(self) -> str:
        """渲染本周回顾模块"""
        review_points = [
            {"title": "市场表现", "desc": "本周上证指数上涨2.3%，创业板指上涨4.5%，科技成长领涨"},
            {"title": "板块轮动", "desc": "AI算力、存储芯片、人形机器人等科技板块持续强势"},
            {"title": "资金流向", "desc": "北向资金本周净买入125亿，机构加仓科技成长方向"},
            {"title": "情绪指标", "desc": "市场情绪回暖，赚钱效应良好，两市成交额维持在1.2万亿"},
        ]
        
        points_html = ""
        for p in review_points:
            points_html += f'''
            <div class="review-point-item">
                <span class="review-point-icon">📌</span>
                <div class="review-point-content">
                    <h4 class="review-point-title">{p["title"]}</h4>
                    <p class="review-point-desc">{p["desc"]}</p>
                </div>
            </div>
            '''
        
        return f'''
        <section class="v4-section" id="section-review">
            {self.render_section_header("📊 本周回顾", "市场总结", "v4-tag-blue")}
            <div class="v4-card">
                <div class="review-points">
                    {points_html}
                </div>
            </div>
        </section>
        '''
    
    def render_next_week_outlook(self) -> str:
        """渲染下周展望模块"""
        outlook = {
            "trend": "震荡上行",
            "trend_prob": "65%",
            "key_point": "关注4200点压力位",
            "style": "科技成长占优",
            "risk": "外围市场波动",
        }
        
        return f'''
        <section class="v4-section" id="section-outlook">
            {self.render_section_header("🔮 下周展望", "趋势预判", "v4-tag-purple")}
            <div class="outlook-grid">
                <div class="outlook-main-card">
                    <div class="outlook-trend-label">预计走势</div>
                    <div class="outlook-trend-value">{outlook["trend"]}</div>
                    <div class="outlook-trend-prob">概率 {outlook["trend_prob"]}</div>
                </div>
                <div class="outlook-info-card">
                    <div class="outlook-info-item">
                        <span class="info-icon">📈</span>
                        <div>
                            <div class="info-label">关键点位</div>
                            <div class="info-value">{outlook["key_point"]}</div>
                        </div>
                    </div>
                    <div class="outlook-info-item">
                        <span class="info-icon">🎯</span>
                        <div>
                            <div class="info-label">主导风格</div>
                            <div class="info-value">{outlook["style"]}</div>
                        </div>
                    </div>
                    <div class="outlook-info-item">
                        <span class="info-icon">⚠️</span>
                        <div>
                            <div class="info-label">主要风险</div>
                            <div class="info-value risk">{outlook["risk"]}</div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        '''
    
    def render_key_sectors(self) -> str:
        """渲染重点板块模块"""
        sectors = [
            {
                "name": "AI算力",
                "icon": "🤖",
                "logic": "AI大模型持续迭代，算力需求爆发式增长",
                "rating": "强烈推荐",
                "core_stocks": ["寒武纪", "海光信息", "龙芯中科"],
            },
            {
                "name": "存储芯片",
                "icon": "💾",
                "logic": "行业周期反转，HBM需求超预期",
                "rating": "强烈推荐",
                "core_stocks": ["三星电子", "SK海力士", "兆易创新"],
            },
            {
                "name": "人形机器人",
                "icon": "🦾",
                "logic": "产业政策支持，特斯拉Optimus量产临近",
                "rating": "推荐",
                "core_stocks": ["绿的谐波", "埃斯顿", "拓普集团"],
            },
            {
                "name": "先进封装",
                "icon": "🔌",
                "logic": "Chiplet趋势明确，封装技术价值量提升",
                "rating": "推荐",
                "core_stocks": ["台积电", "长电科技", "通富微电"],
            },
        ]
        
        cards_html = ""
        for s in sectors:
            rating_color = "#DC2626" if s["rating"] == "强烈推荐" else "#F59E0B"
            
            stocks_html = ""
            for stock in s["core_stocks"]:
                stocks_html += f'<span class="sector-stock-tag">{stock}</span>'
            
            cards_html += f'''
            <div class="key-sector-card">
                <div class="sector-card-header">
                    <span class="sector-icon">{s["icon"]}</span>
                    <div class="sector-info">
                        <h4 class="sector-name">{s["name"]}</h4>
                        <span class="sector-rating" style="color: {rating_color};">{s["rating"]}</span>
                    </div>
                </div>
                <p class="sector-logic">{s["logic"]}</p>
                <div class="sector-stocks">
                    <span class="sector-stocks-label">核心标的：</span>
                    {stocks_html}
                </div>
            </div>
            '''
        
        return f'''
        <section class="v4-section" id="section-sectors">
            {self.render_section_header("🔥 重点板块", "机会挖掘", "v4-tag-red")}
            <div class="key-sectors-grid">
                {cards_html}
            </div>
        </section>
        '''
    
    def render_content(self) -> str:
        """渲染页面内容"""
        # 头部统计卡片
        header_stats = f'''
        <div class="v4-header-stats">
            <div class="v4-stat-card">
                <div class="v4-stat-value" style="color: #10B981;">+2.3%</div>
                <div class="v4-stat-label">本周涨跌幅</div>
            </div>
            <div class="v4-stat-card">
                <div class="v4-stat-value" style="color: #8B5CF6;">4</div>
                <div class="v4-stat-label">重点板块</div>
            </div>
            <div class="v4-stat-card">
                <div class="v4-stat-value" style="color: #F59E0B;">12</div>
                <div class="v4-stat-label">精选个股</div>
            </div>
            <div class="v4-stat-card">
                <div class="v4-stat-value" style="color: #EC4899;">65%</div>
                <div class="v4-stat-label">上涨概率</div>
            </div>
        </div>
        '''
        
        header = self.render_page_header(extra_html=header_stats)
        week_review = self.render_week_review()
        next_outlook = self.render_next_week_outlook()
        key_sectors = self.render_key_sectors()
        strategy_section = self.render_strategy_section()
        risk_warning = self.render_risk_warning()
        
        return f'''
        {header}
        {week_review}
        {next_outlook}
        {key_sectors}
        {strategy_section}
        {risk_warning}
        '''
    
    def get_page_css(self) -> str:
        """页面特有CSS - 新版设计风格"""
        return '''
        /* 本周回顾 */
        .review-points {
            display: flex;
            flex-direction: column;
            gap: 16px;
        }
        .review-point-item {
            display: flex;
            gap: 14px;
            padding: 16px;
            background: #F8FAFC;
            border-radius: 12px;
        }
        .review-point-icon {
            font-size: 20px;
            flex-shrink: 0;
        }
        .review-point-content {
            flex: 1;
        }
        .review-point-title {
            font-size: 15px;
            font-weight: 600;
            color: #1E293B;
            margin: 0 0 6px 0;
        }
        .review-point-desc {
            font-size: 13px;
            color: #64748B;
            margin: 0;
            line-height: 1.6;
        }
        
        /* 下周展望 */
        .outlook-grid {
            display: grid;
            grid-template-columns: 1fr 2fr;
            gap: 16px;
        }
        .outlook-main-card {
            background: linear-gradient(135deg, #8B5CF6 0%, #6366F1 100%);
            border-radius: 14px;
            padding: 30px 20px;
            text-align: center;
            color: white;
        }
        .outlook-trend-label {
            font-size: 14px;
            opacity: 0.8;
            margin-bottom: 8px;
        }
        .outlook-trend-value {
            font-size: 32px;
            font-weight: 800;
            margin-bottom: 8px;
        }
        .outlook-trend-prob {
            font-size: 14px;
            opacity: 0.9;
            padding: 4px 12px;
            background: rgba(255,255,255,0.2);
            border-radius: 12px;
            display: inline-block;
        }
        .outlook-info-card {
            background: white;
            border-radius: 14px;
            padding: 20px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.06);
            display: flex;
            flex-direction: column;
            gap: 16px;
        }
        .outlook-info-item {
            display: flex;
            gap: 14px;
            align-items: center;
        }
        .info-icon {
            font-size: 24px;
        }
        .info-label {
            font-size: 12px;
            color: #94A3B8;
            margin-bottom: 2px;
        }
        .info-value {
            font-size: 15px;
            font-weight: 600;
            color: #1E293B;
        }
        .info-value.risk {
            color: #DC2626;
        }
        
        /* 重点板块 */
        .key-sectors-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 16px;
        }
        .key-sector-card {
            padding: 20px;
            background: white;
            border-radius: 14px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.06);
        }
        .sector-card-header {
            display: flex;
            gap: 14px;
            align-items: center;
            margin-bottom: 12px;
        }
        .sector-icon {
            font-size: 32px;
        }
        .sector-info {
            flex: 1;
        }
        .sector-name {
            font-size: 16px;
            font-weight: 600;
            color: #1E293B;
            margin: 0 0 4px 0;
        }
        .sector-rating {
            font-size: 12px;
            font-weight: 600;
        }
        .sector-logic {
            font-size: 13px;
            color: #64748B;
            margin: 0 0 14px 0;
            line-height: 1.6;
        }
        .sector-stocks {
            display: flex;
            flex-wrap: wrap;
            gap: 6px;
            align-items: center;
        }
        .sector-stocks-label {
            font-size: 12px;
            color: #94A3B8;
        }
        .sector-stock-tag {
            padding: 3px 10px;
            background: #F1F5F9;
            color: #475569;
            border-radius: 6px;
            font-size: 12px;
        }
        
        /* 标签颜色 */
        .v4-tag-blue {
            background: rgba(37, 99, 235, 0.1);
            color: #2563EB;
        }
        .v4-tag-purple {
            background: rgba(139, 92, 246, 0.1);
            color: #7C3AED;
        }
        .v4-tag-red {
            background: rgba(220, 38, 38, 0.1);
            color: #DC2626;
        }
        
        /* 响应式 */
        @media (max-width: 640px) {
            .outlook-grid {
                grid-template-columns: 1fr;
            }
        }
        '''


if __name__ == '__main__':
    generator = WeekendExpressV4(data_dir='data')
    html = generator.generate()
    output_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '..', 'docs', 'weekend_express_v4.html')
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"✅ 周末速递V4已生成 -> {output_path}")
