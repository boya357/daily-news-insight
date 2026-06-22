"""
明日催化剂生成器 - V3.0 精致增强版
次日重要事件 + 业绩公告 + 数据发布
已整合：StatCard渐变统计卡、Tabs标签页、CardGrid网格、全局动效
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.report import Report
from components.layout import Section, HighlightBox, SubCard, CardGrid, SplitLayout
from components.data import DataCard, DataGrid, StockTags, Badge, StatCard, Sparkline, Tabs, GaugeChart, ProgressBar
from components.special import RiskAlert
from components.skill_analysis import render_three_d_heat, render_swot, render_scenarios


class TomorrowCatalystGenerator:
    """明日催化剂生成器 - V3.0精致增强版"""
    
    def __init__(self, date_str: str, subtitle: str = None):
        self.date_str = date_str
        self.subtitle = subtitle or f"{date_str} · 明日催化事件"
        self.report = Report(
            title="明日催化剂",
            report_type="tomorrow_catalyst",
            subtitle=self.subtitle
        )
        self._components = []
    
    def add_key_catalyst(self, catalyst: str):
        """添加核心催化剂"""
        box = HighlightBox(content=catalyst, icon="zap", variant="warning", title="明日核心催化")
        self._components.append(box)
    
    def add_events_calendar(self, events: list):
        """添加明日事件日历（V3.0增强：Tabs分类 + SubCard卡片）
        
        Args:
            events: [{
                'type': 'policy'/'data'/'earnings'/'meeting'/'general',
                'title': '事件标题',
                'description': '事件描述',
                'category': '分类标签'
            }, ...]
        """
        from components.icons import icon_svg
        
        # 按类型分组
        type_groups = {}
        type_names = {
            'policy': '政策事件',
            'data': '数据发布',
            'earnings': '业绩公告',
            'meeting': '重要会议',
            'general': '综合事件'
        }
        type_colors = {
            'policy': ('#3b82f6', '#dbeafe', '#1e40af'),
            'data': ('#10b981', '#dcfce7', '#166534'),
            'earnings': ('#f59e0b', '#fef3c7', '#92400e'),
            'meeting': ('#8b5cf6', '#ede9fe', '#6d28d9'),
            'general': ('#6b7280', '#f3f4f6', '#374151'),
        }
        
        for event in events:
            event_type = event.get('type', 'general')
            if event_type not in type_groups:
                type_groups[event_type] = []
            type_groups[event_type].append(event)
        
        # 生成标签页内容
        tab_list = []
        for event_type, type_events in type_groups.items():
            type_name = type_names.get(event_type, '其他')
            icon_color, bg_color, text_color = type_colors.get(event_type, type_colors['general'])
            
            content_html = '<div style="display: flex; flex-direction: column; gap: 10px;">'
            for event in type_events:
                event_html = f'''
                <div style="background: white; border: 1px solid rgba(0, 0, 0, 0.06);
                           border-radius: 12px; padding: 14px 16px;
                           display: flex; align-items: flex-start;
                           box-shadow: 0 1px 3px rgba(0, 0, 0, 0.04);
                           transition: all 0.3s ease;"
                     onmouseover="this.style.transform='translateY(-2px)'; this.style.boxShadow='0 4px 12px rgba(0,0,0,0.06)';"
                     onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 1px 3px rgba(0, 0, 0, 0.04)';">
                    <div style="width: 32px; height: 32px; 
                               background: linear-gradient(135deg, {icon_color} 0%, {text_color} 100%); 
                               border-radius: 8px; display: flex; align-items: center; justify-content: center; 
                               margin-right: 12px; flex-shrink: 0;">
                        {icon_svg("calendar", 16, "white")}
                    </div>
                    <div style="flex: 1;">
                        <div style="font-size: 14px; font-weight: 600; color: #1f2937; margin-bottom: 4px;">
                            {event.get("title", "")}
                        </div>
                        <div style="font-size: 12px; color: #6b7280; line-height: 1.5;">
                            {event.get("description", "")}
                        </div>
                        <div style="margin-top: 6px;">
                            <span style="display: inline-block; padding: 2px 8px; 
                                       border-radius: 6px; background: {bg_color}; 
                                       color: {text_color}; font-size: 11px; font-weight: 500;">
                                {event.get("category", "事件")}
                            </span>
                        </div>
                    </div>
                </div>'''
                content_html += event_html
            content_html += '</div>'
            
            # 使用SubCard包装
            sub_card = SubCard(content=content_html, variant="white")
            tab_list.append((type_name, sub_card.render()))
        
        # 如果只有一类，不使用Tabs
        if len(tab_list) == 1:
            content = tab_list[0][1]
        else:
            tabs = Tabs(tabs=tab_list, default_index=0)
            content = tabs.render()
        
        section = Section(title="📅 明日事件日历", content=content, icon="calendar")
        self._components.append(section)
    
    def add_earnings_announcements(self, stocks: list):
        """添加业绩公告（V3.0增强：StatCard统计卡）
        
        Args:
            stocks: [{
                'name': '公司名称',
                'code': '股票代码',
                'type': '业绩预告/业绩快报/年报',
                'eps': '每股收益（可选）',
                'growth': '增长率（可选）'
            }, ...]
        """
        cards = []
        for stock in stocks:
            # 副标题信息
            subtitle_parts = []
            if stock.get('code'):
                subtitle_parts.append(stock['code'])
            if stock.get('growth'):
                subtitle_parts.append(stock['growth'])
            subtitle = " · ".join(subtitle_parts) if subtitle_parts else stock.get('type', '业绩公告')
            
            # 决定颜色
            variant = "warning"  # 默认黄色
            if stock.get('growth') and '+' in str(stock['growth']):
                variant = "success"
            elif stock.get('growth') and '-' in str(stock['growth']):
                variant = "danger"
            
            cards.append(StatCard(
                title=stock["name"],
                value=stock.get('type', '业绩公告'),
                subtitle=subtitle,
                icon="dollar-sign",
                variant=variant
            ))
        
        grid = CardGrid(cards, cols=min(len(cards), 3))
        section = Section(title="💰 业绩公告", content=grid.render(), icon="dollar-sign")
        self._components.append(section)
    
    def add_data_release(self, data_list: list):
        """添加重要数据发布（V3.0增强：StatCard统计卡 + 对比展示）
        
        Args:
            data_list: [{
                'name': '数据名称',
                'prev': '前值',
                'expect': '预期值',
                'actual': '实际值（可选，如果已公布）'
            }, ...]
        """
        cards = []
        for data in data_list:
            # 副标题：前值/预期
            subtitle_parts = []
            if data.get('prev'):
                subtitle_parts.append(f"前值: {data['prev']}")
            if data.get('expect'):
                subtitle_parts.append(f"预期: {data['expect']}")
            subtitle = " | ".join(subtitle_parts) if subtitle_parts else "待公布"
            
            # 主要显示值
            main_value = data.get('actual', data.get('expect', '待公布'))
            
            cards.append(StatCard(
                title=data["name"],
                value=main_value,
                subtitle=subtitle,
                icon="bar-chart",
                variant="info"
            ))
        
        grid = CardGrid(cards, cols=min(len(cards), 3))
        section = Section(title="📊 重要数据发布", content=grid.render(), icon="bar-chart")
        self._components.append(section)
    
    def add_impact_analysis(self, impact: str):
        """添加市场影响分析"""
        content = f'<div style="line-height: 1.8; color: #374151; font-size: 14px;">{impact}</div>'
        section = Section(title="🔍 市场影响分析", content=content, icon="search", variant="highlight")
        self._components.append(section)
    
    def _generate_catalyst_analysis_data(self, event: dict) -> dict:
        """根据催化事件智能生成分析数据"""
        event_type = event.get('type', 'general')
        title = event.get('title', '')
        description = event.get('description', '')
        category = event.get('category', '')
        
        # 根据事件类型和重要性设定基础分数
        type_base_scores = {
            'policy': {'policy': 85, 'industry': 60, 'capital': 70},
            'data': {'policy': 40, 'industry': 50, 'capital': 65},
            'earnings': {'policy': 30, 'industry': 55, 'capital': 60},
            'meeting': {'policy': 50, 'industry': 70, 'capital': 55},
            'general': {'policy': 40, 'industry': 40, 'capital': 45},
        }
        base = type_base_scores.get(event_type, type_base_scores['general'])
        
        # 根据关键词调整分数
        title_lower = title.lower()
        desc_lower = description.lower()
        
        # 正面/负面关键词调整
        positive_keywords = ['利好', '支持', '出台', '落地', '超预期', '增长', '爆发', '创新高']
        negative_keywords = ['加息', '利空', '下跌', '风险', '危机', '衰退', '紧缩', '超预期鹰派']
        
        pos_count = sum(1 for kw in positive_keywords if kw in title_lower or kw in desc_lower)
        neg_count = sum(1 for kw in negative_keywords if kw in title_lower or kw in desc_lower)
        
        adjustment = (pos_count - neg_count) * 5
        
        policy_score = max(0, min(100, base['policy'] + adjustment))
        industry_score = max(0, min(100, base['industry'] + adjustment))
        capital_score = max(0, min(100, base['capital'] + adjustment))
        overall_score = (policy_score * 0.35 + industry_score * 0.35 + capital_score * 0.3)
        
        # 热度结论
        if overall_score >= 80:
            heat_conclusion = "重大催化，预计显著影响市场"
        elif overall_score >= 60:
            heat_conclusion = "较强催化，关注相关板块机会"
        elif overall_score >= 40:
            heat_conclusion = "中等催化，存在结构性机会"
        else:
            heat_conclusion = "影响有限，短期情绪面为主"
        
        three_d_heat = {
            'policy_score': policy_score,
            'industry_score': industry_score,
            'capital_score': capital_score,
            'overall_score': overall_score,
            'conclusion': heat_conclusion,
        }
        
        # SWOT分析
        strengths = []
        weaknesses = []
        opportunities = []
        threats = []
        
        if event_type == 'policy':
            strengths.append("政策顶层设计明确，方向性强")
            opportunities.append("政策红利持续释放，相关板块受益")
            if 'AI' in title or '人工智能' in title:
                strengths.append("科技趋势明确，产业空间大")
                opportunities.append("应用场景持续扩容")
            if '消费' in title:
                strengths.append("内需拉动，政策支持力度大")
                opportunities.append("消费复苏弹性大")
        elif event_type == 'data':
            if 'PMI' in title or '经济数据' in title:
                opportunities.append("经济数据验证复苏逻辑")
                threats.append("数据不及预期引发情绪波动")
            if '通胀' in title or 'CPI' in title or 'PCE' in title:
                threats.append("通胀超预期可能引发政策收紧")
                strengths.append("数据透明，市场有预期管理")
        elif event_type == 'meeting':
            opportunities.append("会议可能释放超预期利好")
            threats.append("会议结果存在不确定性")
        else:
            strengths.append("事件关注度较高")
            opportunities.append("存在事件驱动型机会")
        
        if neg_count > pos_count:
            threats.append("短期可能对风险偏好形成压制")
        elif pos_count > neg_count:
            opportunities.append("事件催化有望提振板块情绪")
        
        # 确保每个维度至少有1条
        if not strengths:
            strengths.append("事件具有一定市场关注度")
        if not weaknesses:
            weaknesses.append("具体影响程度存在不确定性")
        if not opportunities:
            opportunities.append("关注事件后续进展带来的机会")
        if not threats:
            threats.append("需警惕预期兑现后的获利回吐")
        
        swot = {
            'strengths': strengths[:3],
            'weaknesses': weaknesses[:3],
            'opportunities': opportunities[:3],
            'threats': threats[:3],
        }
        
        # 情景推演
        base_return = 0.0
        if overall_score >= 70:
            base_return = 0.08 if pos_count >= neg_count else -0.06
        elif overall_score >= 50:
            base_return = 0.04 if pos_count >= neg_count else -0.03
        else:
            base_return = 0.02 if pos_count >= neg_count else -0.02
        
        scenarios = [
            {
                'scenario_name': '乐观情景',
                'probability': 0.25,
                'impact_score': min(100, overall_score + 15),
                'expected_return': base_return * 1.8,
                'key_assumptions': [
                    '事件进展超预期',
                    '资金关注度持续提升',
                    '政策/数据利好超预期'
                ],
                'description': f'{title}超预期落地，相关板块迎来估值业绩双升'
            },
            {
                'scenario_name': '中性情景',
                'probability': 0.5,
                'impact_score': overall_score,
                'expected_return': base_return,
                'key_assumptions': [
                    '事件符合市场预期',
                    '资金流入平稳',
                    '影响逐步消化'
                ],
                'description': f'{title}如期落地，市场按既有趋势运行'
            },
            {
                'scenario_name': '悲观情景',
                'probability': 0.25,
                'impact_score': max(0, overall_score - 20),
                'expected_return': base_return * -1.5,
                'key_assumptions': [
                    '事件不及预期',
                    '资金流出超预期',
                    '利好兑现或利空超预期'
                ],
                'description': f'{title}低于预期，相关板块短期承压回调'
            },
        ]
        
        return {
            'three_d_heat': three_d_heat,
            'swot': swot,
            'scenarios': scenarios,
        }
    
    def add_catalyst_deep_analysis(self, events: list):
        """添加催化事件深度分析模块（Skill增强）
        
        采用折叠式设计，默认收起，点击展开查看三维热度、SWOT、情景推演
        
        Args:
            events: 催化事件列表，每个事件为dict，包含title/type/description/category
        """
        if not events:
            return
        
        # 取前3个最重要的事件做深度分析
        top_events = events[:3]
        
        analysis_cards = ''
        for i, event in enumerate(top_events):
            title = event.get('title', '未知事件')
            category = event.get('category', '')
            analysis = self._generate_catalyst_analysis_data(event)
            
            heat_html = render_three_d_heat(analysis['three_d_heat'], f"{title} · 热度评估")
            swot_html = render_swot(analysis['swot'], f"{title} · SWOT分析")
            scenarios_html = render_scenarios(analysis['scenarios'], f"{title} · 情景推演")
            
            card_id = f"catalyst-skill-{i}"
            
            analysis_cards += f'''
            <div class="bg-white/5 backdrop-blur-sm rounded-xl border border-white/10 overflow-hidden mb-3 last:mb-0">
                <div class="p-4 flex items-center justify-between cursor-pointer" 
                     onclick="toggleCatalystAnalysis('{card_id}')">
                    <div class="flex items-center gap-2">
                        <span class="text-lg">🧠</span>
                        <span class="font-bold text-white">{title}</span>
                        <span class="text-xs bg-gradient-to-r from-purple-500/30 to-blue-500/30 text-purple-300 px-2 py-0.5 rounded-full border border-purple-500/30">
                            Skill增强
                        </span>
                    </div>
                    <span class="text-white/40 text-sm" id="{card_id}-arrow">▼</span>
                </div>
                <div id="{card_id}-content" class="px-4 pb-4 hidden">
                    <div class="grid md:grid-cols-2 gap-3">
                        {heat_html}
                        {swot_html}
                    </div>
                    <div class="mt-3">
                        {scenarios_html}
                    </div>
                </div>
            </div>
            '''
        
        # 交互脚本
        js = '''
        <script>
        function toggleCatalystAnalysis(id) {
            const panel = document.getElementById(id + '-content');
            const arrow = document.getElementById(id + '-arrow');
            if (panel.classList.contains('hidden')) {
                panel.classList.remove('hidden');
                arrow.textContent = '▲';
            } else {
                panel.classList.add('hidden');
                arrow.textContent = '▼';
            }
        }
        </script>
        '''
        
        content = f'''
        <div class="space-y-0">
            {analysis_cards}
        </div>
        {js}
        '''
        
        section = Section(title="🧠 催化深度分析", content=content, icon="brain", variant="dark")
        self._components.append(section)

    def add_risk_warning(self, risks: list):
        """添加风险提示"""
        risk_text = "；".join(risks) if isinstance(risks, list) else risks
        risk = RiskAlert(level="warning", title="⚠️ 风险提示", text=risk_text)
        self._components.append(risk)
    
    def generate(self) -> str:
        """生成完整HTML"""
        self.report.components.clear()  # 清空避免重复添加
        for comp in self._components:
            self.report.add(comp)
        return self.report.generate()
    
    def save(self, filepath: str) -> str:
        """保存到文件"""
        self.generate()
        return self.report.save(filepath)
    
    def validate(self) -> list:
        """验证报告"""
        self.generate()
        return self.report.validate()

    def publish(self, title=None, report_type=None, filename=None, excerpt=None, auto_deploy=True, docs_root="docs"):
        """一键发布"""
        html_content = self.generate()
        import sys, os
        sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        from workflow import ReportPublisher
        rtype = report_type or self.report.report_type
        display_title = title or self.report.title or rtype
        publisher = ReportPublisher(docs_root=docs_root)
        return publisher.publish(html_content=html_content, title=display_title, report_type=rtype, filename=filename, excerpt=excerpt, auto_deploy=auto_deploy)
