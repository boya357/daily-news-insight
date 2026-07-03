"""
盘中快报 - V4版（新版设计）
基于V4BaseGenerator基类，采用v4_test.html设计风格
特色：实时行情追踪、盘中热点捕捉、异动提醒
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from generators.v4_base import V4BaseGenerator


class IntradayReportV4(V4BaseGenerator):
    """盘中快报V4生成器"""
    
    def __init__(self, data_dir: str = "data"):
        super().__init__(data_dir)
        self.page_title = "⚡ 盘中快报"
        self.page_subtitle = "实时行情追踪 · 盘中热点捕捉 · 异动及时提醒"
        self.active_nav_key = "intraday"
        self.toc_items = [
            ("市场概览", "section-overview"),
            ("板块异动", "section-sectors"),
            ("个股异动", "section-stocks"),
            ("资金流向", "section-fund"),
            ("午评策略", "section-strategy"),
        ]
    
    def render_sector_changes(self) -> str:
        """渲染板块异动模块"""
        gainers = [
            {"name": "AI算力", "change": "+3.8%", "lead_stock": "寒武纪", "reason": "AI算力需求持续爆发"},
            {"name": "存储芯片", "change": "+3.2%", "lead_stock": "铜冠铜箔", "reason": "HBM需求超预期"},
            {"name": "人形机器人", "change": "+2.9%", "lead_stock": "绿的谐波", "reason": "产业政策催化"},
            {"name": "半导体设备", "change": "+2.5%", "lead_stock": "北方华创", "reason": "国产替代加速"},
        ]
        
        losers = [
            {"name": "银行", "change": "-0.8%", "lead_stock": "招商银行", "reason": "息差压力"},
            {"name": "房地产", "change": "-0.6%", "lead_stock": "万科A", "reason": "销售数据疲软"},
            {"name": "煤炭", "change": "-0.5%", "lead_stock": "中国神华", "reason": "价格回调"},
        ]
        
        gainers_html = ""
        for s in gainers:
            gainers_html += f'''
            <div class="sector-change-item">
                <span class="sector-rank-up">{s["name"]}</span>
                <span class="sector-change-val up">{s["change"]}</span>
                <span class="sector-lead-stock">领涨：{s["lead_stock"]}</span>
            </div>
            '''
        
        losers_html = ""
        for s in losers:
            losers_html += f'''
            <div class="sector-change-item">
                <span class="sector-rank-down">{s["name"]}</span>
                <span class="sector-change-val down">{s["change"]}</span>
                <span class="sector-lead-stock">领跌：{s["lead_stock"]}</span>
            </div>
            '''
        
        return f'''
        <section class="v4-section" id="section-sectors">
            {self.render_section_header("🔥 板块异动", "实时热点", "v4-tag-red")}
            <div class="sector-changes-tabs">
                <div class="sector-changes-col">
                    <h4 class="col-title up">📈 涨幅居前</h4>
                    <div class="sector-change-list">
                        {gainers_html}
                    </div>
                </div>
                <div class="sector-changes-col">
                    <h4 class="col-title down">📉 跌幅居前</h4>
                    <div class="sector-change-list">
                        {losers_html}
                    </div>
                </div>
            </div>
        </section>
        '''
    
    def render_stock_changes(self) -> str:
        """渲染个股异动模块"""
        stocks = [
            {"name": "铜冠铜箔", "code": "301217", "change": "+20.00%", "reason": "存储芯片+HBM概念", "type": "limit_up"},
            {"name": "雅克科技", "code": "002409", "change": "+7.38%", "reason": "存储产业链龙头", "type": "big_gain"},
            {"name": "*ST建艺", "code": "002789", "change": "+5.02%", "reason": "摘帽预期+重组", "type": "big_gain"},
            {"name": "寒武纪", "code": "688256", "change": "+5.68%", "reason": "AI芯片龙头", "type": "big_gain"},
        ]
        
        stocks_html = ""
        for s in stocks:
            type_labels = {
                "limit_up": ("涨停", "#DC2626"),
                "big_gain": ("大涨", "#F59E0B"),
                "limit_down": ("跌停", "#16A34A"),
                "big_drop": ("大跌", "#10B981"),
            }
            label, color = type_labels.get(s["type"], ("异动", "#64748B"))
            
            stocks_html += f'''
            <div class="stock-change-card">
                <div class="stock-change-header">
                    <div class="stock-info">
                        <span class="stock-name">{s["name"]}</span>
                        <span class="stock-code">{s["code"]}</span>
                    </div>
                    <span class="stock-change-badge" style="background: {color}15; color: {color};">{label}</span>
                </div>
                <div class="stock-change-value" style="color: #DC2626;">{s["change"]}</div>
                <div class="stock-change-reason">
                    <span class="reason-label">异动原因：</span>
                    <span class="reason-text">{s["reason"]}</span>
                </div>
            </div>
            '''
        
        return f'''
        <section class="v4-section" id="section-stocks">
            {self.render_section_header("⚡ 个股异动", "重点关注", "v4-tag-orange")}
            <div class="stock-changes-grid">
                {stocks_html}
            </div>
        </section>
        '''
    
    def render_fund_flow(self) -> str:
        """渲染资金流向模块"""
        main_inflow = [
            {"name": "半导体", "inflow": "+38.5亿"},
            {"name": "AI算力", "inflow": "+28.3亿"},
            {"name": "新能源", "inflow": "+15.7亿"},
        ]
        
        main_outflow = [
            {"name": "银行", "outflow": "-12.3亿"},
            {"name": "房地产", "outflow": "-8.5亿"},
            {"name": "煤炭", "outflow": "-5.2亿"},
        ]
        
        inflow_html = ""
        for item in main_inflow:
            inflow_html += f'''
            <div class="fund-flow-row">
                <span class="fund-flow-name">{item["name"]}</span>
                <span class="fund-flow-val up">{item["inflow"]}</span>
            </div>
            '''
        
        outflow_html = ""
        for item in main_outflow:
            outflow_html += f'''
            <div class="fund-flow-row">
                <span class="fund-flow-name">{item["name"]}</span>
                <span class="fund-flow-val down">{item["outflow"]}</span>
            </div>
            '''
        
        return f'''
        <section class="v4-section" id="section-fund">
            {self.render_section_header("💰 资金流向", "主力动向", "v4-tag-blue")}
            <div class="fund-flow-grid">
                <div class="v4-card fund-flow-card">
                    <h4 class="card-title up">📈 主力流入</h4>
                    <div class="fund-flow-list">
                        {inflow_html}
                    </div>
                </div>
                <div class="v4-card fund-flow-card">
                    <h4 class="card-title down">📉 主力流出</h4>
                    <div class="fund-flow-list">
                        {outflow_html}
                    </div>
                </div>
            </div>
        </section>
        '''
    
    def render_midday_strategy(self) -> str:
        """渲染午评策略模块"""
        return f'''
        <section class="v4-section" id="section-strategy">
            {self.render_section_header("📝 午评策略", "操作建议", "v4-tag-purple")}
            <div class="v4-card strategy-card">
                <div class="strategy-summary">
                    <p class="strategy-text">
                        <strong>上午盘面：</strong>早盘两市高开后震荡走高，科技成长板块持续强势，
                        AI算力、存储芯片、人形机器人等板块领涨，市场赚钱效应良好。
                        成交量较昨日同期有所放大，北向资金持续流入。
                    </p>
                    <p class="strategy-text">
                        <strong>午后策略：</strong>整体市场氛围偏暖，科技成长主线明确。
                        建议持有核心标的，不要频繁换股；对于涨幅较大的品种可考虑分批止盈，
                        低位科技品种仍有补涨机会。注意控制仓位，避免追高。
                    </p>
                </div>
                <div class="strategy-tags">
                    <span class="strategy-tag">科技成长为主线</span>
                    <span class="strategy-tag">持有为主不追高</span>
                    <span class="strategy-tag">关注低位补涨</span>
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
                <div class="v4-stat-value" style="color: #DC2626;">+1.25%</div>
                <div class="v4-stat-label">上证指数</div>
            </div>
            <div class="v4-stat-card">
                <div class="v4-stat-value" style="color: #DC2626;">+2.18%</div>
                <div class="v4-stat-label">创业板指</div>
            </div>
            <div class="v4-stat-card">
                <div class="v4-stat-value" style="color: #10B981;">+68亿</div>
                <div class="v4-stat-label">北向资金</div>
            </div>
            <div class="v4-stat-card">
                <div class="v4-stat-value" style="color: #8B5CF6;">78%</div>
                <div class="v4-stat-label">赚钱效应</div>
            </div>
        </div>
        '''
        
        update_time = "2026-06-18 11:30:00"
        
        header = self.render_page_header(extra_html=header_stats)
        market_overview = self.render_market_overview_v2()
        sector_changes = self.render_sector_changes()
        stock_changes = self.render_stock_changes()
        fund_flow = self.render_fund_flow()
        midday_strategy = self.render_midday_strategy()
        
        return f'''
        {header}
        <div class="update-time">数据更新时间：{update_time}</div>
        {market_overview}
        {sector_changes}
        {stock_changes}
        {fund_flow}
        {midday_strategy}
        '''
    
    def get_page_css(self) -> str:
        """页面特有CSS - 新版设计风格"""
        return '''
        /* 更新时间 */
        .update-time {
            text-align: center;
            font-size: 12px;
            color: #94A3B8;
            margin-bottom: 20px;
            padding: 8px;
            background: rgba(255,255,255,0.8);
            border-radius: 8px;
        }
        
        /* 板块异动 */
        .sector-changes-tabs {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 16px;
        }
        .sector-changes-col {
            background: white;
            border-radius: 14px;
            padding: 20px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.06);
        }
        .col-title {
            font-size: 15px;
            font-weight: 600;
            margin: 0 0 14px 0;
        }
        .col-title.up { color: #DC2626; }
        .col-title.down { color: #16A34A; }
        .sector-change-list {
            display: flex;
            flex-direction: column;
            gap: 10px;
        }
        .sector-change-item {
            display: flex;
            flex-direction: column;
            gap: 4px;
            padding: 12px;
            background: #F8FAFC;
            border-radius: 10px;
        }
        .sector-rank-up, .sector-rank-down {
            font-size: 14px;
            font-weight: 600;
            color: #1E293B;
        }
        .sector-change-val {
            font-size: 16px;
            font-weight: 700;
        }
        .sector-change-val.up { color: #DC2626; }
        .sector-change-val.down { color: #16A34A; }
        .sector-lead-stock {
            font-size: 12px;
            color: #64748B;
        }
        
        /* 个股异动 */
        .stock-changes-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
            gap: 16px;
        }
        .stock-change-card {
            padding: 18px;
            background: white;
            border-radius: 14px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.06);
        }
        .stock-change-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 10px;
        }
        .stock-info {
            display: flex;
            flex-direction: column;
        }
        .stock-name {
            font-size: 16px;
            font-weight: 600;
            color: #1E293B;
        }
        .stock-code {
            font-size: 12px;
            color: #94A3B8;
        }
        .stock-change-badge {
            padding: 4px 10px;
            border-radius: 6px;
            font-size: 12px;
            font-weight: 500;
        }
        .stock-change-value {
            font-size: 24px;
            font-weight: 800;
            margin-bottom: 10px;
        }
        .stock-change-reason {
            padding-top: 10px;
            border-top: 1px solid #F1F5F9;
            font-size: 12px;
        }
        .reason-label {
            color: #94A3B8;
        }
        .reason-text {
            color: #475569;
        }
        
        /* 资金流向 */
        .fund-flow-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 16px;
        }
        .fund-flow-card {
            padding: 20px;
        }
        .card-title {
            font-size: 15px;
            font-weight: 600;
            margin: 0 0 14px 0;
        }
        .card-title.up { color: #DC2626; }
        .card-title.down { color: #16A34A; }
        .fund-flow-list {
            display: flex;
            flex-direction: column;
            gap: 10px;
        }
        .fund-flow-row {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 10px 12px;
            background: #F8FAFC;
            border-radius: 8px;
        }
        .fund-flow-name {
            font-size: 14px;
            color: #1E293B;
            font-weight: 500;
        }
        .fund-flow-val {
            font-size: 14px;
            font-weight: 600;
        }
        .fund-flow-val.up { color: #DC2626; }
        .fund-flow-val.down { color: #16A34A; }
        
        /* 午评策略 */
        .strategy-card {
            padding: 24px;
        }
        .strategy-summary {
            margin-bottom: 16px;
        }
        .strategy-text {
            font-size: 14px;
            line-height: 1.8;
            color: #475569;
            margin: 0 0 12px 0;
        }
        .strategy-text:last-child {
            margin-bottom: 0;
        }
        .strategy-text strong {
            color: #1E293B;
        }
        .strategy-tags {
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
            padding-top: 16px;
            border-top: 1px solid #F1F5F9;
        }
        .strategy-tag {
            padding: 6px 14px;
            background: rgba(139, 92, 246, 0.1);
            color: #7C3AED;
            border-radius: 20px;
            font-size: 12px;
            font-weight: 500;
        }
        
        /* 标签颜色 */
        .v4-tag-red {
            background: rgba(220, 38, 38, 0.1);
            color: #DC2626;
        }
        .v4-tag-orange {
            background: rgba(245, 158, 11, 0.1);
            color: #D97706;
        }
        .v4-tag-blue {
            background: rgba(37, 99, 235, 0.1);
            color: #2563EB;
        }
        .v4-tag-purple {
            background: rgba(139, 92, 246, 0.1);
            color: #7C3AED;
        }
        
        /* 响应式 */
        @media (max-width: 640px) {
            .sector-changes-tabs {
                grid-template-columns: 1fr;
            }
        }
        '''


if __name__ == '__main__':
    generator = IntradayReportV4(data_dir='data')
    html = generator.generate()
    output_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '..', 'docs', 'intraday_report_v4.html')
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"✅ 盘中快报V4已生成 -> {output_path}")
