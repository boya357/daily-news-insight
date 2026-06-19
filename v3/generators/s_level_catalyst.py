"""
S级催化生成器 - V3.0 精致增强版
重大题材深度分析 + 产业链梳理 + 投资机会
已整合：StatCard渐变统计卡、Tabs标签页、SplitLayout分栏、SubCard嵌套卡片、全局动效
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.report import Report
from components.layout import Section, HighlightBox, SubCard, CardGrid, SplitLayout, Card
from components.data import DataCard, DataGrid, KeyPoints, StockTags, CompareTable, Badge, StatCard, Sparkline, Tabs, GaugeChart, ProgressBar
from components.special import RiskAlert, QuoteBlock
from components.skill_analysis import render_three_d_heat, render_swot, render_scenarios


class SLevelCatalystGenerator:
    """S级催化生成器 - V3.0精致增强版"""
    
    def __init__(self, date_str: str, catalyst_title: str = None, subtitle: str = None):
        self.date_str = date_str
        self.catalyst_title = catalyst_title or "重大催化事件"
        self.subtitle = subtitle or f"{date_str} · S级催化深度分析"
        self.report = Report(
            title="S级催化",
            report_type="s_level_catalyst",
            subtitle=self.subtitle
        )
        self._components = []
    
    def add_catalyst_overview(self, overview: str, importance: str = "高"):
        """添加催化事件概述"""
        box = HighlightBox(
            content=overview,
            icon="zap",
            variant="danger",
            title=f"⚡ S级催化 - {self.catalyst_title}"
        )
        self._components.append(box)
    
    def add_catalyst_details(self, background: str, trigger: str):
        """添加催化事件详细分析（V3.0增强：SplitLayout左右分栏）
        
        Args:
            background: 事件背景
            trigger: 触发因素
        """
        # 左侧：事件背景
        left_html = f'''
        <div style="background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%); 
                    border-radius: 14px; padding: 20px; height: 100%;
                    border: 1px solid #bae6fd;">
            <div style="display: flex; align-items: center; margin-bottom: 12px;">
                <div style="width: 36px; height: 36px; 
                           background: linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%); 
                           border-radius: 10px; display: flex; align-items: center; justify-content: center; 
                           margin-right: 12px;">
                    📚
                </div>
                <span style="font-size: 16px; font-weight: 700; color: #1e40af;">
                    事件背景
                </span>
            </div>
            <div style="font-size: 13px; color: #374151; line-height: 1.8;">
                {background}
            </div>
        </div>
        '''
        
        # 右侧：触发因素
        right_html = f'''
        <div style="background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%); 
                    border-radius: 14px; padding: 20px; height: 100%;
                    border: 1px solid #fcd34d;">
            <div style="display: flex; align-items: center; margin-bottom: 12px;">
                <div style="width: 36px; height: 36px; 
                           background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%); 
                           border-radius: 10px; display: flex; align-items: center; justify-content: center; 
                           margin-right: 12px;">
                    🔥
                </div>
                <span style="font-size: 16px; font-weight: 700; color: #92400e;">
                    触发因素
                </span>
            </div>
            <div style="font-size: 13px; color: #78350f; line-height: 1.8;">
                {trigger}
            </div>
        </div>
        '''
        
        split = SplitLayout(left=left_html, right=right_html, left_width="50%", gap="16px")
        content = split.render()
        
        section = Section(title="🔍 催化事件详解", content=content, icon="search")
        self._components.append(section)
    
    def add_industry_chain_analysis(self, upstream: list, midstream: list, downstream: list):
        """添加产业链分析（V3.0增强：Tabs标签页分类 + SubCard卡片）
        
        Args:
            upstream: 上游环节列表
            midstream: 中游环节列表
            downstream: 下游环节列表
        """
        from components.icons import icon_svg
        
        def render_chain_layer(items, color_from, color_to):
            """渲染单个产业链层级"""
            items_html = '<div style="display: flex; flex-direction: column; gap: 10px;">'
            for item in items:
                stocks_html = ''
                if item.get('stocks'):
                    tags = StockTags(item['stocks'], label="核心标的")
                    stocks_html = tags.render()
                
                item_html = f'''
                <div style="background: white; border-radius: 12px; padding: 14px 16px;
                          box-shadow: 0 1px 3px rgba(0,0,0,0.05);
                          border: 1px solid rgba(0,0,0,0.04);
                          transition: all 0.3s ease;"
                     onmouseover="this.style.transform='translateY(-2px)'; this.style.boxShadow='0 4px 12px rgba(0,0,0,0.08)';"
                     onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 1px 3px rgba(0,0,0,0.05)';">
                    <div style="font-size: 14px; font-weight: 600; color: #1f2937; margin-bottom: 6px;">
                        {item.get("name", "")}
                    </div>
                    <div style="font-size: 12px; color: #6b7280; line-height: 1.5; margin-bottom: 8px;">
                        {item.get("desc", "")}
                    </div>
                    {stocks_html}
                </div>
                '''
                items_html += item_html
            items_html += '</div>'
            return items_html
        
        # 生成三个标签页
        tab_list = [
            ("上游", render_chain_layer(upstream, "#10b981", "#059669")),
            ("中游", render_chain_layer(midstream, "#3b82f6", "#2563eb")),
            ("下游", render_chain_layer(downstream, "#f59e0b", "#d97706")),
        ]
        
        tabs = Tabs(tabs=tab_list, default_index=1)  # 默认显示中游
        content = tabs.render()
        
        section = Section(title="🔗 产业链梳理", content=content, icon="git-branch")
        self._components.append(section)
    
    def add_investment_opportunities(self, opportunities: list, view_mode: str = "card"):
        """添加投资机会分析（V3.0增强：支持卡片模式/标签页模式）
        
        Args:
            opportunities: 投资机会列表
            view_mode: "card"（卡片列表）或 "tab"（按优先级标签页）
        """
        from components.icons import icon_svg
        
        if view_mode == "tab":
            # 按优先级分组
            priority_groups = {}
            for opp in opportunities:
                priority = opp.get('priority', '中')
                if priority not in priority_groups:
                    priority_groups[priority] = []
                priority_groups[priority].append(opp)
            
            # 按优先级排序：高 > 中 > 低
            priority_order = ['高', '中', '低']
            tab_list = []
            for p in priority_order:
                if p in priority_groups:
                    tab_content = self._render_opportunity_cards(priority_groups[p])
                    tab_list.append((f"{p}优先级", tab_content))
            
            tabs = Tabs(tabs=tab_list, default_index=0)
            content = tabs.render()
        else:
            # 卡片列表模式
            content = self._render_opportunity_cards(opportunities)
        
        section = Section(title="💰 投资机会分析", content=content, icon="dollar-sign")
        self._components.append(section)
    
    def _render_opportunity_cards(self, opportunities: list) -> str:
        """渲染投资机会卡片列表（内部方法）"""
        from components.icons import icon_svg
        
        content_html = '<div style="display: flex; flex-direction: column; gap: 14px;">'
        for opp in opportunities:
            priority = opp.get('priority', '高')
            priority_colors = {
                '高': ('#ef4444', '#fee2e2', '#991b1b'),
                '中': ('#f59e0b', '#fef3c7', '#92400e'),
                '低': ('#3b82f6', '#dbeafe', '#1e40af'),
            }
            p_color, p_bg, p_text = priority_colors.get(priority, priority_colors['中'])
            
            stocks_html = ''
            if opp.get('stocks'):
                tags = StockTags(opp['stocks'], label="核心标的")
                stocks_html = tags.render()
            
            card_content = f'''
            <div style="display: flex; align-items: flex-start; margin-bottom: 10px;">
                <div style="flex: 1;">
                    <span style="font-size: 16px; font-weight: 700; color: #1f2937;">
                        {opp.get("name", "")}
                    </span>
                </div>
                <span style="padding: 4px 10px; border-radius: 20px; 
                           font-size: 11px; font-weight: 700;
                           background: linear-gradient(135deg, {p_color} 0%, {p_text} 100%); 
                           color: white;">
                    {priority}优先级
                </span>
            </div>
            <div style="font-size: 13px; color: #6b7280; line-height: 1.7; margin-bottom: 10px;">
                {opp.get("logic", "")}
            </div>
            {stocks_html}
            '''
            
            sub_card = SubCard(content=card_content, variant="white")
            # 左边框颜色
            card_html = f'''
            <div style="border-left: 4px solid {p_color}; border-radius: 0 12px 12px 0;
                       transition: all 0.3s ease;"
                 onmouseover="this.style.transform='translateX(4px)';"
                 onmouseout="this.style.transform='translateX(0)';">
                {sub_card.render()}
            </div>
            '''
            content_html += card_html
        content_html += '</div>'
        return content_html
    
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
        
        section = Section(title="🧠 催化深度分析", content=content, icon="brain", variant="highlight")
        self._components.append(section)

    def add_risk_warning(self, risks: list):
        """添加风险提示"""
        risk = RiskAlert(level="danger", title="⚠️ 重要风险提示", text="；".join(risks) if isinstance(risks, list) else risks)
        self._components.append(risk)
    
    def add_investment_strategy(self, strategy: str):
        """添加投资策略建议"""
        content = f'<div style="line-height: 1.8; color: #374151; font-size: 14px;">{strategy}</div>'
        section = Section(title="🎯 投资策略建议", content=content, icon="target", variant="highlight")
        self._components.append(section)
    
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
