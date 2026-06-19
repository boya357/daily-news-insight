"""
明日催化剂 - V4版（新版设计）
基于V4BaseGenerator基类，采用v4_test.html设计风格
特色：Tab分类展示、时间轴设计、催化事件卡片
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from generators.v4_base import V4BaseGenerator


class TomorrowCatalystV4(V4BaseGenerator):
    """明日催化剂V4生成器"""
    
    def __init__(self, data_dir: str = "data"):
        super().__init__(data_dir)
        self.page_title = "⏰ 明日催化剂"
        self.page_subtitle = "提前布局市场机会 · 催化事件一网打尽"
        self.active_nav_key = "tomorrow_catalyst"
        self.toc_items = [
            ("明日概览", "section-overview"),
            ("重点催化", "section-catalysts"),
            ("投资日历", "section-calendar"),
            ("策略建议", "section-strategy"),
            ("风险提示", "section-risk"),
        ]
    
    def render_catalysts_with_tabs(self) -> str:
        """渲染带Tab切换的催化剂列表"""
        catalysts = {
            "policy": [
                {
                    "time": "14:00",
                    "title": "人形机器人产业政策吹风会",
                    "type": "政策发布",
                    "impact": "高",
                    "related": "人形机器人、智能制造",
                    "desc": "工信部将召开人形机器人产业发展政策吹风会，解读最新支持政策和产业规划。",
                },
                {
                    "time": "15:30",
                    "title": "新能源汽车购置税减免细则",
                    "type": "政策发布",
                    "impact": "高",
                    "related": "新能源汽车、锂电池",
                    "desc": "财政部将发布新能源汽车车辆购置税减免政策细则，明确减免范围和期限。",
                },
            ],
            "industry": [
                {
                    "time": "09:30",
                    "title": "AI算力行业峰会召开",
                    "type": "行业会议",
                    "impact": "高",
                    "related": "AI算力、半导体",
                    "desc": "2026全球AI算力峰会将于明日召开，预计发布最新算力技术和应用进展。",
                },
                {
                    "time": "10:30",
                    "title": "半导体产业链论坛",
                    "type": "行业会议",
                    "impact": "中",
                    "related": "半导体、先进封装",
                    "desc": "中国半导体行业协会举办产业链论坛，探讨先进封装和Chiplet技术发展。",
                },
            ],
            "data": [
                {
                    "time": "10:00",
                    "title": "新能源汽车销量数据发布",
                    "type": "数据发布",
                    "impact": "中",
                    "related": "新能源汽车",
                    "desc": "中汽协将发布5月新能源汽车销量数据，市场预期同比增长30%。",
                },
                {
                    "time": "11:00",
                    "title": "房地产开发投资数据",
                    "type": "数据发布",
                    "impact": "中",
                    "related": "房地产、建材",
                    "desc": "国家统计局发布1-5月房地产开发投资和销售数据。",
                },
            ],
            "earnings": [
                {
                    "time": "15:00",
                    "title": "存储芯片大厂财报发布",
                    "type": "财报发布",
                    "impact": "中",
                    "related": "存储芯片",
                    "desc": "美光科技发布最新财报，市场关注AI存储需求增长情况。",
                },
            ],
        }
        
        tab_config = [
            ("policy", "📋 政策", len(catalysts["policy"])),
            ("industry", "🏭 行业", len(catalysts["industry"])),
            ("data", "📊 数据", len(catalysts["data"])),
            ("earnings", "💰 财报", len(catalysts["earnings"])),
        ]
        
        # Tab按钮
        tab_buttons = ""
        for tab_id, tab_name, count in tab_config:
            active_class = "active" if tab_id == "policy" else ""
            tab_buttons += f'''
            <button class="card-tab-btn {active_class}" data-tab="catalyst-{tab_id}" onclick="switchCardTab('catalyst', '{tab_id}')">
                {tab_name}
                <span class="card-tab-count">{count}条</span>
            </button>
            '''
        
        # Tab内容
        tab_contents = ""
        for tab_id, _, _ in tab_config:
            active_class = "active" if tab_id == "policy" else ""
            cats = catalysts[tab_id]
            
            cats_html = ""
            for cat in cats:
                impact_colors = {
                    "高": "#DC2626",
                    "中": "#F59E0B",
                    "低": "#10B981",
                }
                impact_color = impact_colors.get(cat["impact"], "#64748B")
                impact_bg = f"rgba(220, 38, 38, 0.1)" if cat["impact"] == "高" else f"rgba(245, 158, 11, 0.1)" if cat["impact"] == "中" else f"rgba(16, 185, 129, 0.1)"
                
                cats_html += f'''
                <div class="catalyst-card">
                    <div class="catalyst-time-section">
                        <span class="catalyst-time">{cat["time"]}</span>
                        <span class="catalyst-type-badge">{cat["type"]}</span>
                    </div>
                    <div class="catalyst-content">
                        <h3 class="catalyst-title">{cat["title"]}</h3>
                        <p class="catalyst-desc">{cat["desc"]}</p>
                        <div class="catalyst-footer">
                            <span class="catalyst-related">📌 {cat["related"]}</span>
                            <span class="catalyst-impact" style="background: {impact_bg}; color: {impact_color};">影响{cat["impact"]}</span>
                        </div>
                    </div>
                </div>
                '''
            
            tab_contents += f'''
            <div class="card-tab-content {active_class}" id="catalyst-{tab_id}">
                <div class="catalyst-list">
                    {cats_html}
                </div>
            </div>
            '''
        
        return f'''
        <section class="v4-section" id="section-catalysts">
            {self.render_section_header("🔥 重点催化事件", "明日关注", "v4-tag-red")}
            <div class="card-tabs-container">
                <div class="card-tabs-header">
                    {tab_buttons}
                </div>
                <div class="card-tabs-body">
                    {tab_contents}
                </div>
            </div>
        </section>
        '''
    
    def render_calendar(self) -> str:
        """渲染投资日历模块 - 新版设计"""
        events = [
            {"date": "6月15日", "event": "美联储议息会议", "type": "宏观", "impact": "高"},
            {"date": "6月18日", "event": "AI技术大会", "type": "行业", "impact": "中"},
            {"date": "6月20日", "event": "新能源车展", "type": "行业", "impact": "中"},
            {"date": "6月25日", "event": "半年报披露开始", "type": "财报", "impact": "高"},
            {"date": "6月28日", "event": "光伏产业峰会", "type": "行业", "impact": "中"},
            {"date": "7月1日", "event": "新能源车补贴政策调整", "type": "政策", "impact": "高"},
        ]
        
        events_html = ""
        for e in events:
            type_colors = {
                "宏观": "#8B5CF6",
                "行业": "#3B82F6",
                "财报": "#F59E0B",
                "政策": "#EF4444",
            }
            type_color = type_colors.get(e["type"], "#64748B")
            impact_dot = "#DC2626" if e["impact"] == "高" else "#F59E0B"
            
            events_html += f'''
            <div class="calendar-item">
                <div class="calendar-date">
                    <span class="calendar-date-text">{e["date"]}</span>
                </div>
                <div class="calendar-timeline">
                    <div class="calendar-dot" style="background: {impact_dot};"></div>
                    <div class="calendar-line"></div>
                </div>
                <div class="calendar-event-card">
                    <span class="calendar-event-title">{e["event"]}</span>
                    <span class="calendar-event-type" style="background: {type_color}15; color: {type_color};">{e["type"]}</span>
                </div>
            </div>
            '''
        
        return f'''
        <section class="v4-section" id="section-calendar">
            {self.render_section_header("📅 投资日历", "未来一周", "v4-tag-blue")}
            <div class="v4-card">
                <div class="calendar-list">
                    {events_html}
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
                <div class="v4-stat-value" style="color: #EF4444;">8</div>
                <div class="v4-stat-label">重点催化</div>
            </div>
            <div class="v4-stat-card">
                <div class="v4-stat-value" style="color: #F59E0B;">4</div>
                <div class="v4-stat-label">高影响</div>
            </div>
            <div class="v4-stat-card">
                <div class="v4-stat-value" style="color: #10B981;">6</div>
                <div class="v4-stat-label">关注板块</div>
            </div>
            <div class="v4-stat-card">
                <div class="v4-stat-value" style="color: #8B5CF6;">6</div>
                <div class="v4-stat-label">日历事件</div>
            </div>
        </div>
        '''
        
        header = self.render_page_header(extra_html=header_stats)
        market_overview = self.render_market_overview_v2()
        catalysts_tabs = self.render_catalysts_with_tabs()
        calendar = self.render_calendar()
        strategy_section = self.render_strategy_section()
        risk_warning = self.render_risk_warning()
        
        return f'''
        {header}
        {market_overview}
        {catalysts_tabs}
        {calendar}
        {strategy_section}
        {risk_warning}
        '''
    
    def get_page_css(self) -> str:
        """页面特有CSS - 新版设计风格"""
        return '''
        /* 催化剂卡片 */
        .catalyst-list {
            display: flex;
            flex-direction: column;
            gap: 14px;
        }
        .catalyst-card {
            display: flex;
            gap: 16px;
            padding: 18px;
            background: #F8FAFC;
            border-radius: 14px;
            transition: all 0.2s ease;
        }
        .catalyst-card:hover {
            background: #F1F5F9;
        }
        .catalyst-time-section {
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 6px;
            flex-shrink: 0;
            min-width: 70px;
        }
        .catalyst-time {
            font-size: 18px;
            font-weight: 700;
            color: #1E293B;
        }
        .catalyst-type-badge {
            font-size: 11px;
            padding: 3px 8px;
            background: #E0E7FF;
            color: #4F46E5;
            border-radius: 4px;
            font-weight: 500;
        }
        .catalyst-content {
            flex: 1;
            min-width: 0;
        }
        .catalyst-title {
            font-size: 15px;
            font-weight: 600;
            color: #1E293B;
            margin: 0 0 6px 0;
        }
        .catalyst-desc {
            font-size: 13px;
            color: #64748B;
            margin: 0 0 10px 0;
            line-height: 1.6;
        }
        .catalyst-footer {
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-size: 12px;
        }
        .catalyst-related {
            color: #475569;
        }
        .catalyst-impact {
            padding: 3px 10px;
            border-radius: 6px;
            font-weight: 600;
        }
        
        /* 投资日历 */
        .calendar-list {
            display: flex;
            flex-direction: column;
            gap: 0;
        }
        .calendar-item {
            display: flex;
            gap: 16px;
            position: relative;
            padding-bottom: 20px;
        }
        .calendar-item:last-child {
            padding-bottom: 0;
        }
        .calendar-item:last-child .calendar-line {
            display: none;
        }
        .calendar-date {
            min-width: 60px;
            padding-top: 2px;
        }
        .calendar-date-text {
            font-size: 13px;
            font-weight: 600;
            color: #64748B;
        }
        .calendar-timeline {
            display: flex;
            flex-direction: column;
            align-items: center;
            width: 20px;
        }
        .calendar-dot {
            width: 12px;
            height: 12px;
            border-radius: 50%;
            flex-shrink: 0;
            z-index: 1;
            box-shadow: 0 0 0 3px rgba(220, 38, 38, 0.1);
        }
        .calendar-line {
            flex: 1;
            width: 2px;
            background: #E2E8F0;
            margin-top: 6px;
        }
        .calendar-event-card {
            flex: 1;
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 12px 14px;
            background: #F8FAFC;
            border-radius: 10px;
        }
        .calendar-event-title {
            font-size: 14px;
            font-weight: 500;
            color: #1E293B;
        }
        .calendar-event-type {
            font-size: 11px;
            padding: 3px 10px;
            border-radius: 6px;
            font-weight: 500;
        }
        
        /* 标签颜色 */
        .v4-tag-red {
            background: rgba(239, 68, 68, 0.1);
            color: #EF4444;
        }
        .v4-tag-blue {
            background: rgba(37, 99, 235, 0.1);
            color: #2563EB;
        }
        
        /* 响应式 */
        @media (max-width: 640px) {
            .catalyst-card {
                flex-direction: column;
                gap: 12px;
            }
            .catalyst-time-section {
                flex-direction: row;
                align-items: center;
            }
            .calendar-event-card {
                flex-direction: column;
                align-items: flex-start;
                gap: 8px;
            }
        }
        '''


if __name__ == '__main__':
    generator = TomorrowCatalystV4(data_dir='data')
    html = generator.generate()
    output_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '..', 'docs', 'tomorrow_catalyst_v4.html')
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"✅ 明日催化剂V4已生成 -> {output_path}")
