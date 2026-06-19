"""
周三前瞻 - V4版（新版设计）
基于V4BaseGenerator基类，采用v4_test.html设计风格
特色：周中行情展望、板块机会预判、策略调整建议
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from generators.v4_base import V4BaseGenerator


class WeeklyOutlookV4(V4BaseGenerator):
    """周三前瞻V4生成器"""
    
    def __init__(self, data_dir: str = "data"):
        super().__init__(data_dir)
        self.page_title = "👁️ 周三前瞻"
        self.page_subtitle = "周中行情展望 · 板块机会预判 · 策略调整建议"
        self.active_nav_key = "weekly_outlook"
        self.toc_items = [
            ("市场概览", "section-overview"),
            ("周中展望", "section-midweek"),
            ("板块机会", "section-sectors"),
            ("策略建议", "section-strategy"),
            ("风险提示", "section-risk"),
        ]
    
    def render_midweek_outlook(self) -> str:
        """渲染周中展望模块"""
        outlook_data = {
            "trend": "震荡上行",
            "confidence": "中等",
            "key_level": "4100点支撑有效",
            "momentum": "科技成长动能延续",
            "risk_point": "关注外围市场波动",
        }
        
        return f'''
        <section class="v4-section" id="section-midweek">
            {self.render_section_header("📈 周中展望", "趋势判断", "v4-tag-blue")}
            <div class="outlook-card-grid">
                <div class="outlook-main">
                    <div class="outlook-trend-badge">{outlook_data["trend"]}</div>
                    <div class="outlook-confidence">信心度：{outlook_data["confidence"]}</div>
                </div>
                <div class="outlook-points">
                    <div class="outlook-point-item">
                        <span class="point-icon">📍</span>
                        <div>
                            <div class="point-label">关键点位</div>
                            <div class="point-value">{outlook_data["key_level"]}</div>
                        </div>
                    </div>
                    <div class="outlook-point-item">
                        <span class="point-icon">💨</span>
                        <div>
                            <div class="point-label">市场动能</div>
                            <div class="point-value">{outlook_data["momentum"]}</div>
                        </div>
                    </div>
                    <div class="outlook-point-item">
                        <span class="point-icon">⚠️</span>
                        <div>
                            <div class="point-label">风险点</div>
                            <div class="point-value risk">{outlook_data["risk_point"]}</div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        '''
    
    def render_sector_opportunities(self) -> str:
        """渲染板块机会模块"""
        sectors = [
            {
                "name": "AI算力",
                "icon": "🤖",
                "opportunity": "高",
                "logic": "AI大模型持续迭代，算力需求保持高景气度，龙头标的有望继续走强",
                "strategy": "持有为主，逢低加仓",
            },
            {
                "name": "存储芯片",
                "icon": "💾",
                "opportunity": "高",
                "logic": "行业周期反转确立，HBM需求超预期，存储板块估值修复空间大",
                "strategy": "重点配置，积极做多",
            },
            {
                "name": "人形机器人",
                "icon": "🦾",
                "opportunity": "中",
                "logic": "产业政策催化不断，但是短期涨幅较大，注意回调风险",
                "strategy": "逢低布局，不追高",
            },
            {
                "name": "新能源",
                "icon": "🔋",
                "opportunity": "低",
                "logic": "行业竞争加剧，业绩增速放缓，整体缺乏明确催化",
                "strategy": "谨慎观望，等待转机",
            },
        ]
        
        cards_html = ""
        for s in sectors:
            opp_colors = {"高": "#DC2626", "中": "#F59E0B", "低": "#64748B"}
            opp_color = opp_colors.get(s["opportunity"], "#64748B")
            
            cards_html += f'''
            <div class="sector-opp-card">
                <div class="sector-opp-header">
                    <span class="sector-opp-icon">{s["icon"]}</span>
                    <span class="sector-opp-name">{s["name"]}</span>
                    <span class="sector-opp-level" style="background: {opp_color}15; color: {opp_color};">机会{s["opportunity"]}</span>
                </div>
                <p class="sector-opp-logic">{s["logic"]}</p>
                <div class="sector-opp-strategy">
                    <span class="strategy-label">操作策略：</span>
                    <span class="strategy-text">{s["strategy"]}</span>
                </div>
            </div>
            '''
        
        return f'''
        <section class="v4-section" id="section-sectors">
            {self.render_section_header("🔥 板块机会", "周中重点", "v4-tag-red")}
            <div class="sector-opp-grid">
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
                <div class="v4-stat-value" style="color: #10B981;">+1.2%</div>
                <div class="v4-stat-label">周累计涨幅</div>
            </div>
            <div class="v4-stat-card">
                <div class="v4-stat-value" style="color: #8B5CF6;">3</div>
                <div class="v4-stat-label">重点关注板块</div>
            </div>
            <div class="v4-stat-card">
                <div class="v4-stat-value" style="color: #F59E0B;">中等</div>
                <div class="v4-stat-label">操作难度</div>
            </div>
            <div class="v4-stat-card">
                <div class="v4-stat-value" style="color: #EC4899;">成长</div>
                <div class="v4-stat-label">主导风格</div>
            </div>
        </div>
        '''
        
        header = self.render_page_header(extra_html=header_stats)
        market_overview = self.render_market_overview_v2()
        midweek_outlook = self.render_midweek_outlook()
        sector_opportunities = self.render_sector_opportunities()
        strategy_section = self.render_strategy_section()
        risk_warning = self.render_risk_warning()
        
        return f'''
        {header}
        {market_overview}
        {midweek_outlook}
        {sector_opportunities}
        {strategy_section}
        {risk_warning}
        '''
    
    def get_page_css(self) -> str:
        """页面特有CSS - 新版设计风格"""
        return '''
        /* 周中展望卡片 */
        .outlook-card-grid {
            display: grid;
            grid-template-columns: 1fr 2fr;
            gap: 16px;
        }
        .outlook-main {
            background: linear-gradient(135deg, #3B82F6 0%, #6366F1 100%);
            border-radius: 14px;
            padding: 30px 20px;
            text-align: center;
            color: white;
        }
        .outlook-trend-badge {
            font-size: 28px;
            font-weight: 800;
            margin-bottom: 8px;
        }
        .outlook-confidence {
            font-size: 14px;
            opacity: 0.9;
            padding: 6px 16px;
            background: rgba(255,255,255,0.2);
            border-radius: 20px;
            display: inline-block;
        }
        .outlook-points {
            background: white;
            border-radius: 14px;
            padding: 20px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.06);
            display: flex;
            flex-direction: column;
            gap: 16px;
        }
        .outlook-point-item {
            display: flex;
            gap: 14px;
            align-items: center;
            padding: 12px;
            background: #F8FAFC;
            border-radius: 10px;
        }
        .point-icon {
            font-size: 24px;
        }
        .point-label {
            font-size: 12px;
            color: #94A3B8;
            margin-bottom: 2px;
        }
        .point-value {
            font-size: 14px;
            font-weight: 600;
            color: #1E293B;
        }
        .point-value.risk {
            color: #DC2626;
        }
        
        /* 板块机会卡片 */
        .sector-opp-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 16px;
        }
        .sector-opp-card {
            padding: 20px;
            background: white;
            border-radius: 14px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.06);
        }
        .sector-opp-header {
            display: flex;
            align-items: center;
            gap: 10px;
            margin-bottom: 12px;
        }
        .sector-opp-icon {
            font-size: 24px;
        }
        .sector-opp-name {
            flex: 1;
            font-size: 16px;
            font-weight: 600;
            color: #1E293B;
        }
        .sector-opp-level {
            padding: 4px 10px;
            border-radius: 6px;
            font-size: 12px;
            font-weight: 500;
        }
        .sector-opp-logic {
            font-size: 13px;
            color: #64748B;
            line-height: 1.6;
            margin: 0 0 14px 0;
        }
        .sector-opp-strategy {
            padding-top: 12px;
            border-top: 1px solid #F1F5F9;
            font-size: 13px;
        }
        .strategy-label {
            color: #94A3B8;
        }
        .strategy-text {
            color: #1E293B;
            font-weight: 500;
        }
        
        /* 标签颜色 */
        .v4-tag-blue {
            background: rgba(37, 99, 235, 0.1);
            color: #2563EB;
        }
        .v4-tag-red {
            background: rgba(220, 38, 38, 0.1);
            color: #DC2626;
        }
        
        /* 响应式 */
        @media (max-width: 640px) {
            .outlook-card-grid {
                grid-template-columns: 1fr;
            }
        }
        '''


if __name__ == '__main__':
    generator = WeeklyOutlookV4(data_dir='data')
    html = generator.generate()
    output_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '..', 'docs', 'weekly_outlook_v4.html')
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"✅ 周三前瞻V4已生成 -> {output_path}")
