"""
板块热度 - V4版（新版设计）
基于V4BaseGenerator基类，采用v4_test.html设计风格
特色：Tab切换涨跌榜、卡片化设计、资金流向可视化
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from generators.v4_base import V4BaseGenerator


class SectorHeatmapV4(V4BaseGenerator):
    """板块热度V4生成器"""
    
    def __init__(self, data_dir: str = "data"):
        super().__init__(data_dir)
        self.page_title = "🔥 板块热度"
        self.page_subtitle = "全行业板块热度排行 · 资金流向监控 · 轮动节奏把握"
        self.active_nav_key = "sector_heatmap"
        self.toc_items = [
            ("市场概览", "section-overview"),
            ("涨跌排行", "section-ranking"),
            ("资金流向", "section-fund"),
            ("轮动分析", "section-analysis"),
            ("策略建议", "section-strategy"),
        ]
    
    def render_sector_ranking_with_tabs(self) -> str:
        """渲染带Tab切换的板块排行 - 新版Tab组件"""
        # 涨幅榜
        gainers = [
            {"name": "半导体", "change": "+5.23%", "volume": "125亿", "lead_stocks": ["中芯国际", "北方华创"]},
            {"name": "AI算力", "change": "+4.85%", "volume": "98亿", "lead_stocks": ["寒武纪", "海光信息"]},
            {"name": "新能源", "change": "+3.67%", "volume": "76亿", "lead_stocks": ["宁德时代", "比亚迪"]},
            {"name": "军工", "change": "+2.91%", "volume": "45亿", "lead_stocks": ["中航沈飞", "航发动力"]},
            {"name": "医药生物", "change": "+1.85%", "volume": "62亿", "lead_stocks": ["恒瑞医药", "药明康德"]},
            {"name": "汽车零部件", "change": "+1.62%", "volume": "38亿", "lead_stocks": ["拓普集团", "旭升集团"]},
            {"name": "消费电子", "change": "+1.45%", "volume": "42亿", "lead_stocks": ["立讯精密", "歌尔股份"]},
            {"name": "机器人", "change": "+1.32%", "volume": "35亿", "lead_stocks": ["绿的谐波", "埃斯顿"]},
        ]
        
        # 跌幅榜
        losers = [
            {"name": "银行", "change": "-1.23%", "volume": "35亿"},
            {"name": "房地产", "change": "-0.98%", "volume": "28亿"},
            {"name": "煤炭", "change": "-0.76%", "volume": "22亿"},
            {"name": "钢铁", "change": "-0.65%", "volume": "18亿"},
            {"name": "石油石化", "change": "-0.52%", "volume": "25亿"},
        ]
        
        # 涨幅榜HTML
        gainers_html = ""
        for i, s in enumerate(gainers):
            rank_color = '#DC2626' if i < 3 else '#64748B'
            lead_stocks_str = "、".join(s.get("lead_stocks", [])[:2])
            gainers_html += f'''
            <div class="sector-rank-item">
                <span class="sector-rank-num" style="background: {rank_color};">{i+1}</span>
                <div class="sector-rank-info">
                    <span class="sector-rank-name">{s["name"]}</span>
                    <span class="sector-rank-lead">领涨：{lead_stocks_str}</span>
                </div>
                <div class="sector-rank-right">
                    <span class="sector-rank-change" style="color: #DC2626;">{s["change"]}</span>
                    <span class="sector-rank-volume">{s["volume"]}</span>
                </div>
            </div>
            '''
        
        # 跌幅榜HTML
        losers_html = ""
        for i, s in enumerate(losers):
            rank_color = '#16A34A' if i < 3 else '#64748B'
            losers_html += f'''
            <div class="sector-rank-item">
                <span class="sector-rank-num" style="background: {rank_color};">{i+1}</span>
                <div class="sector-rank-info">
                    <span class="sector-rank-name">{s["name"]}</span>
                    <span class="sector-rank-lead">领跌</span>
                </div>
                <div class="sector-rank-right">
                    <span class="sector-rank-change" style="color: #16A34A;">{s["change"]}</span>
                    <span class="sector-rank-volume">{s["volume"]}</span>
                </div>
            </div>
            '''
        
        return f'''
        <section class="v4-section" id="section-ranking">
            {self.render_section_header("📊 涨跌排行", "板块排名", "v4-tag-blue")}
            <div class="card-tabs-container">
                <div class="card-tabs-header">
                    <button class="card-tab-btn active" data-tab="ranking-gainers" onclick="switchCardTab('ranking', 'gainers')">
                        📈 涨幅榜
                        <span class="card-tab-count">{len(gainers)}个</span>
                    </button>
                    <button class="card-tab-btn" data-tab="ranking-losers" onclick="switchCardTab('ranking', 'losers')">
                        📉 跌幅榜
                        <span class="card-tab-count">{len(losers)}个</span>
                    </button>
                </div>
                <div class="card-tabs-body">
                    <div class="card-tab-content active" id="ranking-gainers">
                        <div class="sector-rank-list">
                            {gainers_html}
                        </div>
                    </div>
                    <div class="card-tab-content" id="ranking-losers">
                        <div class="sector-rank-list">
                            {losers_html}
                        </div>
                    </div>
                </div>
            </div>
        </section>
        '''
    
    def render_fund_flow(self) -> str:
        """渲染资金流向模块 - 新版卡片设计"""
        inflows = [
            {"name": "半导体", "inflow": "+25.6亿", "pct": "85"},
            {"name": "AI算力", "inflow": "+18.3亿", "pct": "72"},
            {"name": "新能源", "inflow": "+12.1亿", "pct": "58"},
            {"name": "机器人", "inflow": "+9.8亿", "pct": "45"},
            {"name": "医药生物", "inflow": "+7.5亿", "pct": "38"},
        ]
        
        outflows = [
            {"name": "银行", "inflow": "-8.5亿", "pct": "65"},
            {"name": "房地产", "inflow": "-6.2亿", "pct": "52"},
            {"name": "煤炭", "inflow": "-4.8亿", "pct": "42"},
            {"name": "钢铁", "inflow": "-3.2亿", "pct": "35"},
        ]
        
        inflow_items = ""
        for item in inflows:
            inflow_items += f'''
            <div class="fund-flow-item">
                <div class="fund-flow-header">
                    <span class="fund-flow-name">{item["name"]}</span>
                    <span class="fund-flow-value" style="color: #DC2626;">{item["inflow"]}</span>
                </div>
                <div class="fund-flow-bar">
                    <div class="fund-flow-fill inflow" style="width: {item["pct"]}%;"></div>
                </div>
            </div>
            '''
        
        outflow_items = ""
        for item in outflows:
            outflow_items += f'''
            <div class="fund-flow-item">
                <div class="fund-flow-header">
                    <span class="fund-flow-name">{item["name"]}</span>
                    <span class="fund-flow-value" style="color: #16A34A;">{item["inflow"]}</span>
                </div>
                <div class="fund-flow-bar">
                    <div class="fund-flow-fill outflow" style="width: {item["pct"]}%;"></div>
                </div>
            </div>
            '''
        
        return f'''
        <section class="v4-section" id="section-fund">
            {self.render_section_header("💰 主力资金流向", "资金监控", "v4-tag-orange")}
            <div class="fund-flow-grid">
                <div class="v4-card fund-flow-card">
                    <h4 class="v4-card-title">
                        <span class="title-icon" style="color: #DC2626;">📈</span>
                        主力流入
                    </h4>
                    <div class="fund-flow-list">
                        {inflow_items}
                    </div>
                </div>
                <div class="v4-card fund-flow-card">
                    <h4 class="v4-card-title">
                        <span class="title-icon" style="color: #16A34A;">📉</span>
                        主力流出
                    </h4>
                    <div class="fund-flow-list">
                        {outflow_items}
                    </div>
                </div>
            </div>
        </section>
        '''
    
    def render_rotation_analysis(self) -> str:
        """渲染轮动分析模块 - 新版设计"""
        rotation_stages = [
            {"stage": "启动期", "sectors": ["半导体", "AI算力"], "desc": "科技成长领涨，市场情绪回暖"},
            {"stage": "扩散期", "sectors": ["新能源", "机器人"], "desc": "行情扩散，板块轮动加快"},
            {"stage": "高位期", "sectors": ["医药", "消费"], "desc": "防御板块补涨，注意风险"},
        ]
        
        stages_html = ""
        for stage in rotation_stages:
            sectors_str = "、".join(stage["sectors"])
            stages_html += f'''
            <div class="rotation-stage-item">
                <div class="rotation-stage-label">{stage["stage"]}</div>
                <div class="rotation-stage-content">
                    <div class="rotation-stage-sectors">{sectors_str}</div>
                    <div class="rotation-stage-desc">{stage["desc"]}</div>
                </div>
            </div>
            '''
        
        return f'''
        <section class="v4-section" id="section-analysis">
            {self.render_section_header("🔄 轮动分析", "节奏把握", "v4-tag-purple")}
            <div class="v4-card">
                <div class="rotation-analysis-content">
                    <p class="rotation-summary">
                        本周市场风格明显偏向成长股，科技板块持续领涨。半导体、AI算力、新能源等赛道资金流入明显，
                        而银行、地产等价值板块表现相对较弱。当前处于<strong>科技成长主线</strong>明确，
                        建议关注主线赛道的轮动机会，避免追高，可逢低布局低位补涨品种。
                    </p>
                    <div class="rotation-stages">
                        {stages_html}
                    </div>
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
                <div class="v4-stat-value" style="color: #DC2626;">32</div>
                <div class="v4-stat-label">上涨板块</div>
            </div>
            <div class="v4-stat-card">
                <div class="v4-stat-value" style="color: #16A34A;">18</div>
                <div class="v4-stat-label">下跌板块</div>
            </div>
            <div class="v4-stat-card">
                <div class="v4-stat-value" style="color: #8B5CF6;">半导体</div>
                <div class="v4-stat-label">领涨板块</div>
            </div>
            <div class="v4-stat-card">
                <div class="v4-stat-value" style="color: #F59E0B;">+5.23%</div>
                <div class="v4-stat-label">最大涨幅</div>
            </div>
        </div>
        '''
        
        header = self.render_page_header(extra_html=header_stats)
        market_overview = self.render_market_overview_v2()
        ranking_tabs = self.render_sector_ranking_with_tabs()
        fund_flow = self.render_fund_flow()
        rotation = self.render_rotation_analysis()
        strategy_section = self.render_strategy_section()
        risk_warning = self.render_risk_warning()
        
        return f'''
        {header}
        {market_overview}
        {ranking_tabs}
        {fund_flow}
        {rotation}
        {strategy_section}
        {risk_warning}
        '''
    
    def get_page_css(self) -> str:
        """页面特有CSS - 新版设计风格"""
        return '''
        /* 板块排行列表 */
        .sector-rank-list {
            display: flex;
            flex-direction: column;
            gap: 10px;
        }
        .sector-rank-item {
            display: flex;
            align-items: center;
            gap: 14px;
            padding: 14px 16px;
            background: #F8FAFC;
            border-radius: 12px;
            transition: all 0.2s ease;
        }
        .sector-rank-item:hover {
            background: #F1F5F9;
        }
        .sector-rank-num {
            width: 28px;
            height: 28px;
            border-radius: 8px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 14px;
            font-weight: 700;
            color: white;
            flex-shrink: 0;
        }
        .sector-rank-info {
            flex: 1;
            min-width: 0;
        }
        .sector-rank-name {
            display: block;
            font-size: 15px;
            font-weight: 600;
            color: #1E293B;
            margin-bottom: 2px;
        }
        .sector-rank-lead {
            font-size: 12px;
            color: #64748B;
        }
        .sector-rank-right {
            text-align: right;
            flex-shrink: 0;
        }
        .sector-rank-change {
            display: block;
            font-size: 16px;
            font-weight: 700;
            margin-bottom: 2px;
        }
        .sector-rank-volume {
            font-size: 12px;
            color: #94A3B8;
        }
        
        /* 资金流向 */
        .fund-flow-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 16px;
        }
        .fund-flow-card {
            padding: 20px;
        }
        .v4-card-title {
            font-size: 16px;
            font-weight: 600;
            color: #1E293B;
            margin: 0 0 16px 0;
            display: flex;
            align-items: center;
            gap: 8px;
        }
        .title-icon {
            font-size: 18px;
        }
        .fund-flow-list {
            display: flex;
            flex-direction: column;
            gap: 14px;
        }
        .fund-flow-item {
            display: flex;
            flex-direction: column;
            gap: 8px;
        }
        .fund-flow-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .fund-flow-name {
            font-size: 14px;
            font-weight: 500;
            color: #1E293B;
        }
        .fund-flow-value {
            font-size: 14px;
            font-weight: 600;
        }
        .fund-flow-bar {
            height: 6px;
            background: #E2E8F0;
            border-radius: 3px;
            overflow: hidden;
        }
        .fund-flow-fill {
            height: 100%;
            border-radius: 3px;
            transition: width 0.5s ease;
        }
        .fund-flow-fill.inflow {
            background: linear-gradient(90deg, #DC2626, #F87171);
        }
        .fund-flow-fill.outflow {
            background: linear-gradient(90deg, #10B981, #34D399);
        }
        
        /* 轮动分析 */
        .rotation-analysis-content {
            padding: 8px 0;
        }
        .rotation-summary {
            font-size: 14px;
            line-height: 1.8;
            color: #475569;
            margin: 0 0 20px 0;
        }
        .rotation-summary strong {
            color: #1E293B;
        }
        .rotation-stages {
            display: flex;
            flex-direction: column;
            gap: 12px;
        }
        .rotation-stage-item {
            display: flex;
            gap: 16px;
            padding: 14px 16px;
            background: #F8FAFC;
            border-radius: 12px;
        }
        .rotation-stage-label {
            font-size: 13px;
            font-weight: 600;
            color: #8B5CF6;
            background: rgba(139, 92, 246, 0.1);
            padding: 4px 12px;
            border-radius: 6px;
            height: fit-content;
            white-space: nowrap;
        }
        .rotation-stage-content {
            flex: 1;
        }
        .rotation-stage-sectors {
            font-size: 14px;
            font-weight: 600;
            color: #1E293B;
            margin-bottom: 4px;
        }
        .rotation-stage-desc {
            font-size: 13px;
            color: #64748B;
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
        .v4-tag-orange {
            background: rgba(245, 158, 11, 0.1);
            color: #D97706;
        }
        .v4-tag-purple {
            background: rgba(139, 92, 246, 0.1);
            color: #7C3AED;
        }
        
        /* 响应式 */
        @media (max-width: 640px) {
            .fund-flow-grid {
                grid-template-columns: 1fr;
            }
            .rotation-stage-item {
                flex-direction: column;
                gap: 10px;
            }
        }
        '''


if __name__ == '__main__':
    generator = SectorHeatmapV4(data_dir='data')
    html = generator.generate()
    output_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '..', 'docs', 'sector_heatmap_v4.html')
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"✅ 板块热度V4已生成 -> {output_path}")
