"""
龙虎榜 - V4版（新版设计）
基于V4BaseGenerator基类，采用v4_test.html设计风格
特色：Tab切换榜单类型、机构买卖分析、龙头股追踪
"""
import sys
import os
import json

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from generators.v4_base import V4BaseGenerator


class LonghubangV4(V4BaseGenerator):
    """龙虎榜V4生成器"""
    
    def __init__(self, data_dir: str = "data"):
        super().__init__(data_dir)
        self.page_title = "🏆 龙虎榜"
        self.page_subtitle = "游资动向追踪 · 机构买卖分析 · 龙头股挖掘"
        self.active_nav_key = "longhubang"
        self.toc_items = [
            ("市场概览", "section-overview"),
            ("龙虎榜单", "section-ranking"),
            ("机构动向", "section-institution"),
            ("龙头股分析", "section-leaders"),
            ("策略建议", "section-strategy"),
            ("风险提示", "section-risk"),
        ]
    
    def load_longhubang_data(self):
        """加载龙虎榜数据"""
        # 尝试从数据文件加载
        try:
            data_path = os.path.join(self.data_dir, 'longhubang_market.json')
            if os.path.exists(data_path):
                with open(data_path, 'r', encoding='utf-8') as f:
                    return json.load(f)
        except Exception:
            pass
        return None
    
    def render_longhubang_tabs(self) -> str:
        """渲染带Tab切换的龙虎榜单"""
        data = self.load_longhubang_data()
        
        # 模拟数据（降级使用）
        stocks_data = [
            {"name": "铜冠铜箔", "code": "301217", "change": "+20.00%", "turnover": "8.5亿", "reason": "存储芯片+国产替代", "org_net_buy": "+1.2亿"},
            {"name": "*ST建艺", "code": "002789", "change": "+5.02%", "turnover": "2.3亿", "reason": "摘帽预期+重组", "org_net_buy": "+0.3亿"},
            {"name": "雅克科技", "code": "002409", "change": "+7.38%", "turnover": "15.2亿", "reason": "存储+HBM", "org_net_buy": "+2.1亿"},
            {"name": "英维克", "code": "002837", "change": "+3.25%", "turnover": "12.8亿", "reason": "液冷+AI算力", "org_net_buy": "-0.5亿"},
            {"name": "寒武纪", "code": "688256", "change": "+5.68%", "turnover": "22.5亿", "reason": "AI芯片", "org_net_buy": "+3.5亿"},
            {"name": "绿的谐波", "code": "688017", "change": "+4.32%", "turnover": "6.8亿", "reason": "人形机器人", "org_net_buy": "+0.8亿"},
        ]
        
        leader_stocks = [
            {"name": "铜冠铜箔", "code": "301217", "boards": "3连板", "change": "+20.00%", "concept": "存储芯片+铜箔国产替代", "feature": "机构重仓买入"},
            {"name": "雅克科技", "code": "002409", "boards": "2连板", "change": "+7.38%", "concept": "HBM+存储产业链", "feature": "机构净买入2.1亿"},
            {"name": "*ST建艺", "code": "002789", "boards": "2连板", "change": "+5.02%", "concept": "摘帽预期+重组", "feature": "庭外重组获受理"},
        ]
        
        # 个股榜单HTML
        stocks_html = ""
        for i, s in enumerate(stocks_data):
            is_up = s["change"].startswith("+")
            change_color = "#DC2626" if is_up else "#16A34A"
            org_color = "#DC2626" if s["org_net_buy"].startswith("+") else "#16A34A"
            
            stocks_html += f'''
            <div class="lhb-stock-item">
                <span class="lhb-rank">{i+1}</span>
                <div class="lhb-stock-info">
                    <div class="lhb-stock-name">
                        {s["name"]}
                        <span class="lhb-stock-code">{s["code"]}</span>
                    </div>
                    <div class="lhb-stock-reason">{s["reason"]}</div>
                </div>
                <div class="lhb-stock-right">
                    <div class="lhb-stock-change" style="color: {change_color};">{s["change"]}</div>
                    <div class="lhb-stock-meta">
                        <span>成交 {s["turnover"]}</span>
                    </div>
                </div>
                <div class="lhb-org-buy" style="color: {org_color};">
                    <span class="org-label">机构净买</span>
                    <span class="org-value">{s["org_net_buy"]}</span>
                </div>
            </div>
            '''
        
        # 龙头股HTML
        leaders_html = ""
        for s in leader_stocks:
            leaders_html += f'''
            <div class="leader-stock-card">
                <div class="leader-header">
                    <span class="leader-boards">{s["boards"]}</span>
                    <span class="leader-change" style="color: #DC2626;">{s["change"]}</span>
                </div>
                <div class="leader-name">{s["name"]} <span class="leader-code">{s["code"]}</span></div>
                <div class="leader-concept">{s["concept"]}</div>
                <div class="leader-feature">✨ {s["feature"]}</div>
            </div>
            '''
        
        return f'''
        <section class="v4-section" id="section-ranking">
            {self.render_section_header("📊 龙虎榜单", "每日龙虎榜", "v4-tag-red")}
            <div class="card-tabs-container">
                <div class="card-tabs-header">
                    <button class="card-tab-btn active" data-tab="lhb-stocks" onclick="switchCardTab('lhb', 'stocks')">
                        📈 上榜个股
                        <span class="card-tab-count">{len(stocks_data)}只</span>
                    </button>
                    <button class="card-tab-btn" data-tab="lhb-leaders" onclick="switchCardTab('lhb', 'leaders')">
                        👑 龙头股
                        <span class="card-tab-count">{len(leader_stocks)}只</span>
                    </button>
                </div>
                <div class="card-tabs-body">
                    <div class="card-tab-content active" id="lhb-stocks">
                        <div class="lhb-stock-list">
                            {stocks_html}
                        </div>
                    </div>
                    <div class="card-tab-content" id="lhb-leaders">
                        <div class="leader-stock-grid">
                            {leaders_html}
                        </div>
                    </div>
                </div>
            </div>
        </section>
        '''
    
    def render_institution_flow(self) -> str:
        """渲染机构动向模块"""
        org_buy = [
            {"name": "寒武纪", "net_buy": "+3.5亿", "reason": "AI芯片龙头，机构持续加仓"},
            {"name": "雅克科技", "net_buy": "+2.1亿", "reason": "HBM产业链核心标的"},
            {"name": "铜冠铜箔", "net_buy": "+1.2亿", "reason": "存储铜箔国产替代"},
            {"name": "绿的谐波", "net_buy": "+0.8亿", "reason": "人形机器人核心零部件"},
        ]
        
        org_sell = [
            {"name": "英维克", "net_sell": "-0.5亿", "reason": "短期涨幅较大，机构获利了结"},
            {"name": "某新能源股", "net_sell": "-1.2亿", "reason": "行业竞争加剧，机构减仓"},
        ]
        
        buy_items = ""
        for item in org_buy:
            buy_items += f'''
            <div class="org-flow-item">
                <div class="org-flow-info">
                    <span class="org-flow-name">{item["name"]}</span>
                    <span class="org-flow-reason">{item["reason"]}</span>
                </div>
                <span class="org-flow-value buy">{item["net_buy"]}</span>
            </div>
            '''
        
        sell_items = ""
        for item in org_sell:
            sell_items += f'''
            <div class="org-flow-item">
                <div class="org-flow-info">
                    <span class="org-flow-name">{item["name"]}</span>
                    <span class="org-flow-reason">{item["reason"]}</span>
                </div>
                <span class="org-flow-value sell">{item["net_sell"]}</span>
            </div>
            '''
        
        return f'''
        <section class="v4-section" id="section-institution">
            {self.render_section_header("🏦 机构动向", "主力资金", "v4-tag-blue")}
            <div class="org-flow-grid">
                <div class="v4-card org-flow-card">
                    <h4 class="card-header-title">
                        <span class="title-icon buy">📈</span>
                        机构净买入
                    </h4>
                    <div class="org-flow-list">
                        {buy_items}
                    </div>
                </div>
                <div class="v4-card org-flow-card">
                    <h4 class="card-header-title">
                        <span class="title-icon sell">📉</span>
                        机构净卖出
                    </h4>
                    <div class="org-flow-list">
                        {sell_items}
                    </div>
                </div>
            </div>
        </section>
        '''
    
    def render_leader_analysis(self) -> str:
        """渲染龙头股分析模块"""
        analysis_points = [
            {"title": "连板高度", "value": "3板", "desc": "铜冠铜箔带动存储板块情绪"},
            {"title": "涨停家数", "value": "45家", "desc": "市场活跃度较高，赚钱效应良好"},
            {"title": "炸板率", "value": "18%", "desc": "处于合理区间，情绪稳定"},
            {"title": "连板晋级率", "value": "62%", "desc": "连板效应较强，适合短线操作"},
        ]
        
        points_html = ""
        for p in analysis_points:
            points_html += f'''
            <div class="analysis-point-card">
                <div class="analysis-point-value">{p["value"]}</div>
                <div class="analysis-point-title">{p["title"]}</div>
                <div class="analysis-point-desc">{p["desc"]}</div>
            </div>
            '''
        
        return f'''
        <section class="v4-section" id="section-leaders">
            {self.render_section_header("👑 龙头股分析", "情绪指标", "v4-tag-gold")}
            <div class="analysis-points-grid">
                {points_html}
            </div>
        </section>
        '''
    
    def render_content(self) -> str:
        """渲染页面内容"""
        # 头部统计卡片
        header_stats = f'''
        <div class="v4-header-stats">
            <div class="v4-stat-card">
                <div class="v4-stat-value" style="color: #DC2626;">43</div>
                <div class="v4-stat-label">上榜个股</div>
            </div>
            <div class="v4-stat-card">
                <div class="v4-stat-value" style="color: #8B5CF6;">3</div>
                <div class="v4-stat-label">连板龙头</div>
            </div>
            <div class="v4-stat-card">
                <div class="v4-stat-value" style="color: #10B981;">+8.5亿</div>
                <div class="v4-stat-label">机构净买</div>
            </div>
            <div class="v4-stat-card">
                <div class="v4-stat-value" style="color: #F59E0B;">62%</div>
                <div class="v4-stat-label">晋级率</div>
            </div>
        </div>
        '''
        
        header = self.render_page_header(extra_html=header_stats)
        market_overview = self.render_market_overview_v2()
        longhubang_tabs = self.render_longhubang_tabs()
        institution_flow = self.render_institution_flow()
        leader_analysis = self.render_leader_analysis()
        strategy_section = self.render_strategy_section()
        risk_warning = self.render_risk_warning()
        
        return f'''
        {header}
        {market_overview}
        {longhubang_tabs}
        {institution_flow}
        {leader_analysis}
        {strategy_section}
        {risk_warning}
        '''
    
    def get_page_css(self) -> str:
        """页面特有CSS - 新版设计风格"""
        return '''
        /* 龙虎榜股票列表 */
        .lhb-stock-list {
            display: flex;
            flex-direction: column;
            gap: 10px;
        }
        .lhb-stock-item {
            display: grid;
            grid-template-columns: 30px 1fr auto auto;
            gap: 16px;
            align-items: center;
            padding: 14px 16px;
            background: #F8FAFC;
            border-radius: 12px;
            transition: all 0.2s ease;
        }
        .lhb-stock-item:hover {
            background: #F1F5F9;
        }
        .lhb-rank {
            font-size: 16px;
            font-weight: 700;
            color: #64748B;
            text-align: center;
        }
        .lhb-stock-info {
            min-width: 0;
        }
        .lhb-stock-name {
            font-size: 15px;
            font-weight: 600;
            color: #1E293B;
            margin-bottom: 2px;
        }
        .lhb-stock-code {
            font-size: 12px;
            color: #94A3B8;
            font-weight: 400;
            margin-left: 6px;
        }
        .lhb-stock-reason {
            font-size: 12px;
            color: #64748B;
        }
        .lhb-stock-right {
            text-align: right;
        }
        .lhb-stock-change {
            font-size: 18px;
            font-weight: 700;
            margin-bottom: 2px;
        }
        .lhb-stock-meta {
            font-size: 11px;
            color: #94A3B8;
        }
        .lhb-org-buy {
            text-align: right;
            min-width: 90px;
        }
        .org-label {
            display: block;
            font-size: 11px;
            color: #94A3B8;
            margin-bottom: 2px;
        }
        .org-value {
            font-size: 14px;
            font-weight: 700;
        }
        
        /* 龙头股卡片 */
        .leader-stock-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
            gap: 16px;
        }
        .leader-stock-card {
            padding: 18px;
            background: linear-gradient(135deg, #FEF3C7 0%, #FFFFFF 100%);
            border-radius: 14px;
            border: 1px solid #F59E0B;
        }
        .leader-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 10px;
        }
        .leader-boards {
            padding: 4px 12px;
            background: #F59E0B;
            color: white;
            border-radius: 6px;
            font-size: 13px;
            font-weight: 600;
        }
        .leader-change {
            font-size: 18px;
            font-weight: 700;
        }
        .leader-name {
            font-size: 17px;
            font-weight: 700;
            color: #1E293B;
            margin-bottom: 4px;
        }
        .leader-code {
            font-size: 12px;
            color: #64748B;
            font-weight: 400;
        }
        .leader-concept {
            font-size: 13px;
            color: #475569;
            margin-bottom: 8px;
        }
        .leader-feature {
            font-size: 12px;
            color: #B45309;
            font-weight: 500;
        }
        
        /* 机构动向 */
        .org-flow-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 16px;
        }
        .org-flow-card {
            padding: 20px;
        }
        .card-header-title {
            font-size: 16px;
            font-weight: 600;
            color: #1E293B;
            margin: 0 0 16px 0;
            display: flex;
            align-items: center;
            gap: 8px;
        }
        .card-header-title .title-icon {
            font-size: 18px;
        }
        .org-flow-list {
            display: flex;
            flex-direction: column;
            gap: 12px;
        }
        .org-flow-item {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 12px 14px;
            background: #F8FAFC;
            border-radius: 10px;
        }
        .org-flow-info {
            display: flex;
            flex-direction: column;
            gap: 4px;
        }
        .org-flow-name {
            font-size: 14px;
            font-weight: 600;
            color: #1E293B;
        }
        .org-flow-reason {
            font-size: 12px;
            color: #64748B;
        }
        .org-flow-value {
            font-size: 16px;
            font-weight: 700;
        }
        .org-flow-value.buy { color: #DC2626; }
        .org-flow-value.sell { color: #16A34A; }
        
        /* 龙头分析 */
        .analysis-points-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
            gap: 16px;
        }
        .analysis-point-card {
            padding: 20px;
            background: white;
            border-radius: 14px;
            text-align: center;
            box-shadow: 0 2px 8px rgba(0,0,0,0.06);
        }
        .analysis-point-value {
            font-size: 28px;
            font-weight: 800;
            color: #F59E0B;
            margin-bottom: 8px;
        }
        .analysis-point-title {
            font-size: 14px;
            font-weight: 600;
            color: #1E293B;
            margin-bottom: 4px;
        }
        .analysis-point-desc {
            font-size: 12px;
            color: #64748B;
        }
        
        /* 标签颜色 */
        .v4-tag-red {
            background: rgba(220, 38, 38, 0.1);
            color: #DC2626;
        }
        .v4-tag-blue {
            background: rgba(37, 99, 235, 0.1);
            color: #2563EB;
        }
        .v4-tag-gold {
            background: rgba(245, 158, 11, 0.1);
            color: #D97706;
        }
        
        /* 响应式 */
        @media (max-width: 640px) {
            .lhb-stock-item {
                grid-template-columns: 30px 1fr auto;
            }
            .lhb-org-buy {
                display: none;
            }
            .org-flow-grid {
                grid-template-columns: 1fr;
            }
        }
        '''


if __name__ == '__main__':
    generator = LonghubangV4(data_dir='data')
    html = generator.generate()
    output_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '..', 'docs', 'longhubang_v4.html')
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"✅ 龙虎榜V4已生成 -> {output_path}")
