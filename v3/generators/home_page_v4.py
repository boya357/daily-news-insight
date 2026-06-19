"""
首页 - V4版（新版设计）
基于V4BaseGenerator基类，采用v4_test.html设计风格
特色：紫色渐变背景 + 白色卡片 + 深色文字 + 紫色投影
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from generators.v4_base import V4BaseGenerator
from components.v4_components import V4TopicCard, V4DataGrid


class HomePageV4(V4BaseGenerator):
    """首页V4生成器"""
    
    def __init__(self, data_dir: str = "data"):
        super().__init__(data_dir)
        self.page_title = "💎 投资洞察系统"
        self.page_subtitle = "AI驱动的智能投资决策助手 · 让投资更简单"
        self.active_nav_key = "home"
        self.toc_items = [
            ("功能导航", "section-quick"),
            ("市场概览", "section-overview"),
            ("热门题材", "section-topics"),
            ("系统工具箱", "section-tools"),
            ("报告中心", "section-reports"),
            ("持仓跟踪", "section-portfolio"),
        ]
    
    def render_quick_access(self) -> str:
        """渲染快速入口模块 - 新版卡片式设计"""
        # 三级导航架构：点击进入列表页
        cards = [
            {"icon": "📈", "title": "每日日报", "desc": "全景市场复盘", "link": "list_daily_v4.html", "color": "#3B82F6"},
            {"icon": "⚡", "title": "盘中快报", "desc": "实时行情追踪", "link": "list_intraday_v4.html", "color": "#F59E0B"},
            {"icon": "📊", "title": "持仓仪表盘", "desc": "多维持仓诊断", "link": "list_portfolio_dashboard_v4.html", "color": "#10B981"},
            {"icon": "🚀", "title": "S级催化", "desc": "顶级题材挖掘", "link": "list_s_catalyst_v4.html", "color": "#EF4444"},
            {"icon": "🏆", "title": "龙虎榜", "desc": "游资动向追踪", "link": "list_longhubang_v4.html", "color": "#8B5CF6"},
            {"icon": "🔥", "title": "板块热度", "desc": "行业轮动把握", "link": "list_sector_heatmap_v4.html", "color": "#EC4899"},
            {"icon": "🔮", "title": "预测中心", "desc": "AI智能预测", "link": "list_prediction_center_v4.html", "color": "#06B6D4"},
            {"icon": "🚨", "title": "预警系统", "desc": "智能风险监控", "link": "list_alert_system_v4.html", "color": "#F97316"},
            {"icon": "📅", "title": "周末速递", "desc": "周度投资策略", "link": "list_weekend_express_v4.html", "color": "#84CC16"},
            {"icon": "👁️", "title": "周三前瞻", "desc": "周中行情展望", "link": "list_weekly_outlook_v4.html", "color": "#14B8A6"},
            {"icon": "📚", "title": "周度复盘", "desc": "深度经验总结", "link": "list_weekly_review_v4.html", "color": "#6366F1"},
            {"icon": "⏰", "title": "明日催化", "desc": "事件驱动机会", "link": "list_tomorrow_catalyst_v4.html", "color": "#F43F5E"},
        ]
        
        cards_html = ""
        for card in cards:
            cards_html += f'''
            <a href="{card["link"]}" class="v4-quick-card">
                <div class="quick-card-icon" style="background: {card["color"]}15; color: {card["color"]};">
                    {card["icon"]}
                </div>
                <div class="quick-card-content">
                    <div class="quick-card-title">{card["title"]}</div>
                    <div class="quick-card-desc">{card["desc"]}</div>
                </div>
                <div class="quick-card-arrow" style="color: {card["color"]};">→</div>
            </a>
            '''
        
        return f'''
        <section class="v4-section" id="section-quick">
            {self.render_section_header("🎯 功能导航", "快速入口", "v4-tag-blue")}
            <div class="v4-quick-grid">
                {cards_html}
            </div>
        </section>
        '''
    
    def render_hot_topics(self) -> str:
        """渲染热门题材模块 - 使用新版题材卡片样式"""
        # 使用内容引擎获取热门题材
        topics_data = []
        try:
            if hasattr(self, 'topic_analyzer') and self.topic_analyzer:
                hot_topics = self.topic_analyzer.get_hot_topics(limit=4)
                for topic in hot_topics:
                    topics_data.append({
                        'name': topic.get('name', ''),
                        'level': topic.get('level', 'B'),
                        'level_name': topic.get('level_name', ''),
                        'icon': topic.get('icon', '🔥'),
                        'score': topic.get('score', 0),
                        'description': topic.get('description', ''),
                        'radar': topic.get('radar', {}),
                        'core_stocks': topic.get('core_stocks', []),
                    })
        except Exception:
            pass
        
        # 降级：使用默认题材
        if not topics_data:
            topics_data = [
                {
                    'name': 'AI算力',
                    'level': 'S',
                    'level_name': '最强主线',
                    'icon': '🤖',
                    'score': 94.5,
                    'description': '人工智能算力需求爆发，AI芯片供不应求',
                    'radar': {'政策': 90, '产业': 95, '资金': 92, '情绪': 88, '估值': 82, '催化': 96},
                    'core_stocks': ['英伟达', '寒武纪', '海光信息', '龙芯中科'],
                },
                {
                    'name': '人形机器人',
                    'level': 'A',
                    'level_name': '重要支线',
                    'icon': '💃',
                    'score': 88.0,
                    'description': '具身智能时代开启，产业加速落地',
                    'radar': {'政策': 85, '产业': 90, '资金': 88, '情绪': 86, '估值': 72, '催化': 92},
                    'core_stocks': ['特斯拉', '新松机器人', '埃斯顿', '绿的谐波'],
                },
                {
                    'name': '存储芯片',
                    'level': 'A',
                    'level_name': '重要支线',
                    'icon': '💾',
                    'score': 86.5,
                    'description': '存储周期反转，HBM需求爆发',
                    'radar': {'政策': 82, '产业': 92, '资金': 85, '情绪': 84, '估值': 78, '催化': 90},
                    'core_stocks': ['三星电子', 'SK海力士', '兆易创新', '长江存储'],
                },
                {
                    'name': '先进封装',
                    'level': 'B',
                    'level_name': '潜力题材',
                    'icon': '🔌',
                    'score': 82.0,
                    'description': 'Chiplet大势所趋，先进封装需求增长',
                    'radar': {'政策': 88, '产业': 84, '资金': 80, '情绪': 78, '估值': 75, '催化': 85},
                    'core_stocks': ['台积电', '长电科技', '通富微电', '华天科技'],
                },
            ]
        
        # 使用V4TopicCard组件渲染题材卡片
        topics_html = ""
        for topic_data in topics_data:
            # 补充深度报告链接
            topic_name = topic_data.get('name', '')
            topic_id = topic_data.get('id', '')
            if topic_id and topic_name:
                safe_name = ''.join(c for c in topic_name if c.isalnum() or c in ('_', '-'))
                topic_data['deep_dive_url'] = f"report_{topic_id}_{safe_name}.html"
            elif topic_name:
                # 根据名称推测链接
                topic_id_map = {
                    'AI PC/智能体PC': 'topic_s001',
                    '存储芯片超级周期': 'topic_s002', 
                    '人形机器人': 'topic_s003',
                }
                tid = topic_id_map.get(topic_name, '')
                if tid:
                    safe_name = ''.join(c for c in topic_name if c.isalnum() or c in ('_', '-'))
                    topic_data['deep_dive_url'] = f"report_{tid}_{safe_name}.html"
            
            card = V4TopicCard(topic_data, show_radar=True)
            topics_html += card.render()
        
        return f'''
        <section class="v4-section" id="section-topics">
            {self.render_section_header("🔥 热门题材", "重点关注", "v4-tag-red")}
            <div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(320px, 1fr)); gap: 20px;">
                {topics_html}
            </div>
        </section>
        '''
    
    def render_tool_box(self) -> str:
        """渲染系统工具箱模块"""
        # 三级导航架构：点击进入对应列表页或功能页
        tools = [
            {"icon": "⚠️", "name": "智能预警", "link": "list_alert_system_v4.html", "color": "#EF4444"},
            {"icon": "📊", "name": "持仓仪表盘", "link": "list_portfolio_dashboard_v4.html", "color": "#8B5CF6"},
            {"icon": "🎯", "name": "智能选股", "link": "#", "color": "#10B981"},
            {"icon": "🔮", "name": "预判验证", "link": "list_prediction_center_v4.html", "color": "#F59E0B"},
            {"icon": "🔥", "name": "板块热力图", "link": "list_sector_heatmap_v4.html", "color": "#F97316"},
            {"icon": "🐯", "name": "龙虎榜透视", "link": "list_longhubang_v4.html", "color": "#DC2626"},
            {"icon": "💚", "name": "题材健康度", "link": "#", "color": "#14B8A6"},
            {"icon": "⏰", "name": "数据时光机", "link": "#", "color": "#06B6D4"},
            {"icon": "📈", "name": "周度进化", "link": "#", "color": "#84CC16"},
            {"icon": "🔗", "name": "产业链分析", "link": "#", "color": "#3B82F6"},
            {"icon": "⚙️", "name": "工作流监控", "link": "#", "color": "#6B7280"},
            {"icon": "📝", "name": "更新日志", "link": "#", "color": "#6366F1"},
        ]
        
        tools_html = ""
        for tool in tools:
            tools_html += f'''
            <a href="{tool["link"]}" class="v4-tool-card">
                <div class="v4-tool-icon" style="background: {tool["color"]}15; color: {tool["color"]};">
                    {tool["icon"]}
                </div>
                <div class="v4-tool-name">{tool["name"]}</div>
            </a>
            '''
        
        return f'''
        <section class="v4-section" id="section-tools">
            {self.render_section_header("🛠️ 系统工具箱", "实用工具", "v4-tag-purple")}
            <div class="v4-tool-grid">
                {tools_html}
            </div>
        </section>
        '''
    
    def render_report_center(self) -> str:
        """渲染报告中心模块"""
        # 三级导航架构：点击进入对应列表页
        reports = [
            {"icon": "📰", "name": "每日日报", "link": "list_daily_v4.html", "desc": "全景市场复盘"},
            {"icon": "⚡", "name": "盘中快报", "link": "list_intraday_v4.html", "desc": "实时行情追踪"},
            {"icon": "📉", "name": "盘后速递", "link": "list_aftermarket_v4.html", "desc": "收盘数据总结"},
            {"icon": "📋", "name": "周度复盘", "link": "list_weekly_review_v4.html", "desc": "深度经验总结"},
            {"icon": "🔭", "name": "周三前瞻", "link": "list_weekly_outlook_v4.html", "desc": "周中行情展望"},
            {"icon": "📦", "name": "周末速递", "link": "list_weekend_express_v4.html", "desc": "周度投资策略"},
            {"icon": "💎", "name": "S级催化", "link": "list_s_catalyst_v4.html", "desc": "顶级题材挖掘"},
            {"icon": "⏰", "name": "明日催化", "link": "list_tomorrow_catalyst_v4.html", "desc": "事件驱动机会"},
            {"icon": "🔥", "name": "板块热度", "link": "list_sector_heatmap_v4.html", "desc": "行业轮动分析"},
            {"icon": "🏆", "name": "龙虎榜", "link": "list_longhubang_v4.html", "desc": "游资动向追踪"},
        ]
        
        reports_html = ""
        for report in reports:
            reports_html += f'''
            <a href="{report["link"]}" class="v4-report-card">
                <div class="v4-report-icon">{report["icon"]}</div>
                <div class="v4-report-info">
                    <div class="v4-report-name">{report["name"]}</div>
                    <div class="v4-report-desc">{report["desc"]}</div>
                </div>
            </a>
            '''
        
        return f'''
        <section class="v4-section" id="section-reports">
            {self.render_section_header("📁 报告中心", "全部报告", "v4-tag-blue")}
            <div class="v4-report-grid">
                {reports_html}
            </div>
        </section>
        '''
    
    def render_content(self) -> str:
        """渲染页面内容"""
        # Hero区域 - 新版紫色渐变设计
        hero_html = f'''
        <section class="v4-hero-section">
            <div class="v4-hero-content">
                <div class="v4-hero-badge">✨ AI智能投资平台</div>
                <h1 class="v4-hero-title">{self.page_title}</h1>
                <p class="v4-hero-subtitle">{self.page_subtitle}</p>
                <div class="v4-hero-stats">
                    <div class="v4-hero-stat">
                        <span class="v4-hero-stat-value">12+</span>
                        <span class="v4-hero-stat-label">功能模块</span>
                    </div>
                    <div class="v4-hero-stat">
                        <span class="v4-hero-stat-value">实时</span>
                        <span class="v4-hero-stat-label">数据更新</span>
                    </div>
                    <div class="v4-hero-stat">
                        <span class="v4-hero-stat-value">AI</span>
                        <span class="v4-hero-stat-label">智能分析</span>
                    </div>
                    <div class="v4-hero-stat">
                        <span class="v4-hero-stat-value">7×24</span>
                        <span class="v4-hero-stat-label">持续运行</span>
                    </div>
                </div>
            </div>
            <div class="v4-hero-decoration">
                <div class="hero-blob blob-1"></div>
                <div class="hero-blob blob-2"></div>
                <div class="hero-blob blob-3"></div>
            </div>
        </section>
        '''
        
        quick_access = self.render_quick_access()
        market_overview = self.render_market_overview_v2()
        hot_topics = self.render_hot_topics()
        tool_box = self.render_tool_box()
        report_center = self.render_report_center()
        portfolio_section = self.render_portfolio_section(show_diagnosis=False)
        
        return f'''
        {hero_html}
        {quick_access}
        {market_overview}
        {hot_topics}
        {tool_box}
        {report_center}
        {portfolio_section}
        '''
    
    def get_page_css(self) -> str:
        """页面特有CSS - 新版设计风格"""
        return '''
        /* Hero区域 */
        .v4-hero-section {
            position: relative;
            text-align: center;
            padding: 80px 24px 60px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            border-radius: 24px;
            color: white;
            margin-bottom: 40px;
            overflow: hidden;
        }
        .v4-hero-content {
            position: relative;
            z-index: 2;
        }
        .v4-hero-badge {
            display: inline-block;
            padding: 8px 20px;
            background: rgba(255, 255, 255, 0.2);
            backdrop-filter: blur(10px);
            border-radius: 20px;
            font-size: 13px;
            font-weight: 500;
            margin-bottom: 20px;
            border: 1px solid rgba(255, 255, 255, 0.3);
        }
        .v4-hero-title {
            font-size: 42px;
            font-weight: 800;
            margin: 0 0 16px 0;
            letter-spacing: -0.5px;
        }
        .v4-hero-subtitle {
            font-size: 18px;
            opacity: 0.9;
            margin: 0 0 40px 0;
            font-weight: 400;
        }
        .v4-hero-stats {
            display: flex;
            justify-content: center;
            gap: 60px;
            flex-wrap: wrap;
        }
        .v4-hero-stat {
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        .v4-hero-stat-value {
            font-size: 32px;
            font-weight: 700;
            margin-bottom: 4px;
        }
        .v4-hero-stat-label {
            font-size: 13px;
            opacity: 0.8;
        }
        .v4-hero-decoration {
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            overflow: hidden;
            z-index: 1;
        }
        .hero-blob {
            position: absolute;
            border-radius: 50%;
            background: rgba(255, 255, 255, 0.1);
            filter: blur(40px);
        }
        .blob-1 {
            width: 200px;
            height: 200px;
            top: -50px;
            left: 10%;
        }
        .blob-2 {
            width: 300px;
            height: 300px;
            bottom: -100px;
            right: 5%;
            background: rgba(255, 255, 255, 0.08);
        }
        .blob-3 {
            width: 150px;
            height: 150px;
            top: 30%;
            right: 20%;
            background: rgba(255, 255, 255, 0.12);
        }
        
        /* 快速入口网格 */
        .v4-quick-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
            gap: 16px;
        }
        .v4-quick-card {
            display: flex;
            align-items: center;
            gap: 16px;
            padding: 20px;
            background: white;
            border-radius: 16px;
            text-decoration: none;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.06);
            transition: all 0.3s ease;
            border: 1px solid rgba(0, 0, 0, 0.05);
        }
        .v4-quick-card:hover {
            transform: translateY(-3px);
            box-shadow: 0 12px 28px rgba(102, 126, 234, 0.2);
            border-color: rgba(102, 126, 234, 0.3);
        }
        .quick-card-icon {
            width: 52px;
            height: 52px;
            border-radius: 14px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 24px;
            flex-shrink: 0;
        }
        .quick-card-content {
            flex: 1;
            min-width: 0;
        }
        .quick-card-title {
            font-size: 16px;
            font-weight: 600;
            color: #1E293B;
            margin-bottom: 2px;
        }
        .quick-card-desc {
            font-size: 12px;
            color: #64748B;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }
        .quick-card-arrow {
            font-size: 20px;
            font-weight: 300;
            flex-shrink: 0;
            opacity: 0.6;
            transition: opacity 0.2s;
        }
        .v4-quick-card:hover .quick-card-arrow {
            opacity: 1;
        }
        
        /* 热门题材网格 */
        .v4-topics-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(340px, 1fr));
            gap: 20px;
        }
        
        /* 标签样式 */
        .v4-tag-blue {
            background: rgba(37, 99, 235, 0.1);
            color: #2563EB;
        }
        .v4-tag-red {
            background: rgba(220, 38, 38, 0.1);
            color: #DC2626;
        }
        .v4-tag-purple {
            background: rgba(139, 92, 246, 0.1);
            color: #8B5CF6;
        }
        
        /* 系统工具箱网格 */
        .v4-tool-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(100px, 1fr));
            gap: 12px;
        }
        .v4-tool-card {
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 10px;
            padding: 20px 12px;
            background: white;
            border-radius: 16px;
            text-decoration: none;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
            transition: all 0.3s ease;
            border: 1px solid rgba(0, 0, 0, 0.05);
        }
        .v4-tool-card:hover {
            transform: translateY(-3px);
            box-shadow: 0 8px 24px rgba(102, 126, 234, 0.15);
            border-color: rgba(102, 126, 234, 0.2);
        }
        .v4-tool-icon {
            width: 48px;
            height: 48px;
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 22px;
        }
        .v4-tool-name {
            font-size: 12px;
            font-weight: 500;
            color: #1E293B;
            text-align: center;
        }
        
        /* 报告中心网格 */
        .v4-report-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
            gap: 16px;
        }
        .v4-report-card {
            display: flex;
            align-items: center;
            gap: 14px;
            padding: 18px;
            background: white;
            border-radius: 16px;
            text-decoration: none;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
            transition: all 0.3s ease;
            border: 1px solid rgba(0, 0, 0, 0.05);
        }
        .v4-report-card:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 24px rgba(102, 126, 234, 0.15);
            border-color: rgba(102, 126, 234, 0.2);
        }
        .v4-report-icon {
            width: 46px;
            height: 46px;
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 22px;
            background: linear-gradient(135deg, #667eea15, #764ba215);
            flex-shrink: 0;
        }
        .v4-report-info {
            flex: 1;
            min-width: 0;
        }
        .v4-report-name {
            font-size: 15px;
            font-weight: 600;
            color: #1E293B;
            margin-bottom: 4px;
        }
        .v4-report-desc {
            font-size: 12px;
            color: #64748B;
        }
        
        /* 响应式适配 */
        @media (max-width: 768px) {
            .v4-hero-section {
                padding: 50px 20px 40px;
            }
            .v4-hero-title {
                font-size: 28px;
            }
            .v4-hero-subtitle {
                font-size: 14px;
            }
            .v4-hero-stats {
                gap: 30px;
            }
            .v4-hero-stat-value {
                font-size: 24px;
            }
            .v4-quick-grid {
                grid-template-columns: repeat(2, 1fr);
            }
            .v4-topics-grid {
                grid-template-columns: 1fr;
            }
            .v4-tool-grid {
                grid-template-columns: repeat(4, 1fr);
            }
            .v4-report-grid {
                grid-template-columns: 1fr;
            }
        }
        
        @media (max-width: 480px) {
            .v4-quick-grid {
                grid-template-columns: 1fr;
            }
        }
        '''


if __name__ == '__main__':
    generator = HomePageV4(data_dir='data')
    html = generator.generate()
    output_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '..', 'docs', 'index_v4.html')
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"✅ 首页V4测试页已生成 -> {output_path}")
