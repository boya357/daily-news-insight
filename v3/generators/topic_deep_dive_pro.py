"""
题材/产业链深度研究生成器 - Pro版
基于Pro组件库重构，深色玻璃态风格
支持Tab切换、卡片组、数据网格等通用组件
"""
import sys
import os
import json
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from components.pro import (
    GlassCard, SectionTitle, TagBadge
)
from generators.pro_base import ProGenerator


class TopicDeepDiveProGenerator(ProGenerator):
    data_type = "topic_details"

    """题材深度研究 - Pro版生成器"""
    
    def __init__(self, data_dir: str = "data"):
        super().__init__(
            title="产业链深度研究",
            active_page="产业链",
            footer_text="产业链深度研究 · 洞察投资价值",
            data_dir=data_dir,
            show_toc=True,
        )

    def load_data(self):
        """加载题材详情数据"""
        super().load_data()
        self.data = self.data_loader.get_data("topic_details")
        self.topics = self.data.get('topics', {})
        # 获取第一个题材作为当前题材
        if self.topics:
            first_key = next(iter(self.topics.keys()))
            self.current_topic = self.topics[first_key]
            self.current_topic_id = first_key
        else:
            self.current_topic = {}
            self.current_topic_id = '' 
    
    def _generate_toc(self) -> str:
        """生成题材导航 - 卡片组风格"""
        if not self.topics:
            return ''
        
        # 按级别分组
        level_groups = {'S': [], 'A': [], 'B': []}
        for tid, topic in self.topics.items():
            level = topic.get('level', 'B')
            if level in level_groups:
                level_groups[level].append({'id': tid, **topic})
        
        tabs = []
        level_labels = {'S': 'S级题材', 'A': 'A级题材', 'B': 'B级题材'}
        level_colors = {'S': 'text-red-400', 'A': 'text-yellow-400', 'B': 'text-green-400'}
        
        for level in ['S', 'A', 'B']:
            topics = level_groups.get(level, [])
            if not topics:
                continue
            
            cards_html = ''
            for idx, topic in enumerate(topics):
                name = topic.get('name', '')
                summary = topic.get('summary', '')
                is_active = topic['id'] == self.current_topic_id
                
                active_border = 'border-white/30 bg-white/10' if is_active else 'border-white/10 hover:bg-white/5'
                
                cards_html += f'''
                <div class="{active_border} border rounded-xl p-4 cursor-pointer transition-all duration-300 hover:scale-[1.02]">
                    <div class="flex items-center justify-between mb-2">
                        <span class="text-white font-medium text-sm">{name}</span>
                        <span class="px-2 py-0.5 bg-{level_colors[level].replace('text-', '')}-500/20 text-{level_colors[level].replace('text-', '')} text-xs font-bold rounded-full">{level}级</span>
                    </div>
                    <p class="text-xs text-white/50 line-clamp-2">{summary}</p>
                </div>
                '''
            
            tabs.append({
                'label': f"{level_labels[level]} ({len(topics)})",
                'content': f'<div class="grid grid-cols-1 md:grid-cols-2 gap-3">{cards_html}</div>'
            })
        
        tab_content = self.create_tab_pane(tabs=tabs, tab_id="topics-nav", style="underline")
        
        content = f'''
            {SectionTitle(text='📋 题材导航', icon='📋').render()}
            {tab_content}
        '''
        
        return GlassCard(content=content, padding="p-6", extra_class="mb-6").render()
    
    def _generate_topic_overview(self) -> str:
        """生成题材概览 - 数据网格+摘要卡片"""
        topic = self.current_topic
        if not topic:
            return ''
        
        name = topic.get('name', '')
        level = topic.get('level', '')
        summary = topic.get('summary', '')
        market_size = topic.get('market_size', {})
        
        level_colors = {
            'S': 'from-red-500 to-orange-500',
            'A': 'from-yellow-500 to-amber-500',
            'B': 'from-green-500 to-emerald-500',
        }
        gradient = level_colors.get(level, 'from-purple-500 to-indigo-500')
        
        # 数据网格 - 关键指标
        data_items = []
        if market_size:
            total_2026 = market_size.get('total_2026', '')
            if total_2026:
                data_items.append({'title': '市场规模', 'value': total_2026, 'icon': '📊'})
            penetration = market_size.get('ai_pc_penetration', '') or market_size.get('penetration', '')
            if penetration:
                data_items.append({'title': '渗透率', 'value': penetration, 'icon': '📈'})
            growth_rate = market_size.get('growth_rate', '')
            if growth_rate:
                data_items.append({'title': '年增速', 'value': growth_rate, 'icon': '🚀'})
            market_value = market_size.get('market_value', '')
            if market_value:
                data_items.append({'title': '产业价值', 'value': market_value, 'icon': '💰'})
        
        # 如果没有足够的数据项，补充默认项
        if len(data_items) < 4:
            default_items = [
                {'title': '题材级别', 'value': f'{level}级', 'icon': '⭐'},
                {'title': '覆盖标的', 'value': f"{len(topic.get('target_stocks_analysis', []))}只", 'icon': '🎯'},
                {'title': '催化事件', 'value': f"{len(topic.get('catalyst_timeline', []))}个", 'icon': '⏰'},
                {'title': '风险因素', 'value': f"{len(topic.get('core_risks', []))}项", 'icon': '⚠️'},
            ]
            # 填充到4个
            for item in default_items:
                if len(data_items) >= 4:
                    break
                data_items.append(item)
        
        grid_html = self.create_data_grid(items=data_items[:4], cols=4)
        
        content = f'''
            <div class="text-center mb-8">
                <span class="px-4 py-1.5 bg-gradient-to-r {gradient} text-white text-sm font-bold rounded-full mb-4 inline-block">
                    {level}级题材
                </span>
                <h1 class="text-3xl md:text-4xl font-black text-white mb-4">{name}</h1>
                <p class="text-white/70 max-w-2xl mx-auto leading-relaxed">{summary}</p>
            </div>
            {grid_html}
        '''
        
        return content
    
    def _generate_investment_highlights(self) -> str:
        """生成投资要点 - 卡片组"""
        topic = self.current_topic
        if not topic:
            return ''
        
        highlights = topic.get('investment_highlights', [])
        
        # 如果没有数据，从summary和其他字段推断
        if not highlights:
            highlights = []
            summary = topic.get('summary', '')
            if summary:
                highlights.append({'title': '核心逻辑', 'content': summary, 'icon': '💡'})
            
            market_size = topic.get('market_size', {})
            if market_size:
                growth = market_size.get('growth_rate', '') or market_size.get('market_value', '')
                if growth:
                    highlights.append({'title': '增长潜力', 'content': f'预计市场规模增长强劲，{growth}', 'icon': '📈'})
            
            stocks = topic.get('target_stocks_analysis', [])
            if stocks:
                highlights.append({'title': '标的丰富', 'content': f'覆盖{len(stocks)}只核心标的，多梯队选择', 'icon': '🎯'})
            
            catalysts = topic.get('catalyst_timeline', [])
            if catalysts:
                highlights.append({'title': '催化密集', 'content': f'近期{len(catalysts)}个重要催化剂事件', 'icon': '⚡'})
        
        if not highlights:
            return ''
        
        cards = []
        for h in highlights:
            title = h.get('title', '')
            content = h.get('content', '')
            icon = h.get('icon', '📌')
            card_content = f'''
            <div class="flex items-start gap-3">
                <div class="text-2xl flex-shrink-0">{icon}</div>
                <div>
                    <h4 class="text-white font-medium mb-1">{title}</h4>
                    <p class="text-sm text-white/60">{content}</p>
                </div>
            </div>
            '''
            cards.append({'content': card_content})
        
        cards_html = self.create_card_group(cards=cards, cols=2, card_style='glass')
        
        content = f'''
            {SectionTitle(text='💡 投资要点', icon='💡').render()}
            {cards_html}
        '''
        
        return GlassCard(content=content, padding="p-6", extra_class="mb-6").render()
    
    def _generate_competitive_landscape(self) -> str:
        """生成竞争格局分析 - Tab切换 + 卡片组"""
        topic = self.current_topic
        if not topic:
            return ''
        
        landscape = topic.get('competitive_landscape', {})
        
        # 如果没有专门的竞争格局数据，尝试从产业链提取
        if not landscape:
            chain = topic.get('industry_chain', {})
            # 汇总各环节的头部公司作为竞争格局
            all_companies = []
            for section_key in ['upstream', 'midstream', 'downstream']:
                section = chain.get(section_key, {})
                section_name = section.get('name', section_key)
                companies = section.get('companies', [])
                for comp in companies:
                    comp['section'] = section_name
                    all_companies.append(comp)
            
            if not all_companies:
                return ''
            
            # 按重要性分组
            high_importance = [c for c in all_companies if c.get('importance') == 'high']
            medium_importance = [c for c in all_companies if c.get('importance') == 'medium']
            
            tabs = []
            
            if high_importance:
                cards = []
                for comp in high_importance:
                    card_content = f'''
                    <div class="font-medium text-white mb-1">{comp.get('name', '')}</div>
                    <div class="text-xs text-white/50 mb-1">{comp.get('role', '')}</div>
                    <div class="text-xs text-blue-400">{comp.get('section', '')}</div>
                    '''
                    cards.append({'content': card_content})
                
                tabs.append({
                    'label': f'核心厂商 ({len(high_importance)})',
                    'content': self.create_card_group(cards=cards, cols=2, card_style='subtle')
                })
            
            if medium_importance:
                cards = []
                for comp in medium_importance:
                    card_content = f'''
                    <div class="font-medium text-white mb-1">{comp.get('name', '')}</div>
                    <div class="text-xs text-white/50 mb-1">{comp.get('role', '')}</div>
                    <div class="text-xs text-blue-400">{comp.get('section', '')}</div>
                    '''
                    cards.append({'content': card_content})
                
                tabs.append({
                    'label': f'重要厂商 ({len(medium_importance)})',
                    'content': self.create_card_group(cards=cards, cols=2, card_style='subtle')
                })
            
            if not tabs:
                return ''
            
            tab_html = self.create_tab_pane(tabs=tabs, tab_id="competitive", style="default")
            
            content = f'''
                {SectionTitle(text='🏢 竞争格局', icon='🏢').render()}
                {tab_html}
            '''
            
            return GlassCard(content=content, padding="p-6", extra_class="mb-6").render()
        
        # 如果有完整的竞争格局数据（待扩展）
        return ''
    
    def _generate_downstream_demand(self) -> str:
        """生成下游需求分析 - 卡片组"""
        topic = self.current_topic
        if not topic:
            return ''
        
        downstream = topic.get('downstream_demand', [])
        
        # 如果没有专门数据，从产业链下游提取
        if not downstream:
            chain = topic.get('industry_chain', {})
            down_section = chain.get('downstream', {})
            companies = down_section.get('companies', [])
            
            if not companies:
                return ''
            
            cards = []
            for comp in companies[:6]:  # 最多显示6个
                name = comp.get('name', '')
                role = comp.get('role', '')
                importance = comp.get('importance', 'medium')
                
                imp_color = {'high': 'text-green-400', 'medium': 'text-yellow-400', 'low': 'text-gray-400'}.get(importance, 'text-white/60')
                
                card_content = f'''
                <div class="flex items-center gap-3">
                    <div class="w-10 h-10 rounded-lg bg-gradient-to-br from-blue-500/20 to-purple-500/20 flex items-center justify-center text-lg">
                        📦
                    </div>
                    <div>
                        <div class="font-medium text-white">{name}</div>
                        <div class="text-xs text-white/50">{role}</div>
                    </div>
                </div>
                '''
                cards.append({'content': card_content})
            
            if not cards:
                return ''
            
            cards_html = self.create_card_group(cards=cards, cols=3, card_style='subtle')
            
            content = f'''
                {SectionTitle(text='📦 下游应用', icon='📦').render()}
                {cards_html}
            '''
            
            return GlassCard(content=content, padding="p-6", extra_class="mb-6").render()
        
        return ''
    
    def _generate_industry_chain(self) -> str:
        """生成产业链分析 - Tab切换 + 卡片组"""
        topic = self.current_topic
        chain = topic.get('industry_chain', {})
        if not chain:
            return ''
        
        sections = ['upstream', 'midstream', 'downstream']
        section_names = {
            'upstream': '上游',
            'midstream': '中游',
            'downstream': '下游',
        }
        
        tabs = []
        for section_key in sections:
            section = chain.get(section_key, {})
            if not section:
                continue
            
            section_name = section.get('name', section_names.get(section_key, section_key))
            description = section.get('description', '')
            companies = section.get('companies', [])
            
            # 公司卡片组
            cards = []
            for comp in companies:
                comp_name = comp.get('name', '')
                role = comp.get('role', '')
                importance = comp.get('importance', 'medium')
                
                imp_label = {'high': '核心', 'medium': '重要', 'low': '一般'}.get(importance, '重要')
                imp_color = {'high': 'red', 'medium': 'yellow', 'low': 'green'}.get(importance, 'blue')
                
                card_content = f'''
                <div class="mb-2 text-sm">
                    <span class="text-white font-medium">{comp_name}</span>
                    <span class="ml-2 px-2 py-0.5 bg-{imp_color}-500/20 text-{imp_color}-400 text-xs rounded-full">{imp_label}</span>
                </div>
                <div class="text-xs text-white/50">{role}</div>
                '''
                cards.append({'content': card_content})
            
            # 描述+卡片组
            tab_content = f'''
            <div class="mb-4">
                <p class="text-sm text-white/70 leading-relaxed">{description}</p>
            </div>
            {self.create_card_group(cards=cards, cols=2, card_style='subtle') if cards else ''}
            '''
            
            tabs.append({
                'label': section_name,
                'content': tab_content
            })
        
        tab_html = self.create_tab_pane(tabs=tabs, tab_id="industry-chain", style="default")
        
        content = f'''
            {SectionTitle(text='🔗 产业链分析', icon='🔗').render()}
            {tab_html}
        '''
        
        return GlassCard(content=content, padding="p-6", extra_class="mb-6").render()
    
    def _generate_target_stocks(self) -> str:
        """生成核心标的分析 - Tab切换（按梯队） + 卡片组"""
        topic = self.current_topic
        stocks = topic.get('target_stocks_analysis', [])
        if not stocks:
            return ''
        
        # 按梯队分组
        tier_groups = {}
        for stock in stocks:
            tier = stock.get('tier', '受益')
            if tier not in tier_groups:
                tier_groups[tier] = []
            tier_groups[tier].append(stock)
        
        # 定义梯队顺序
        tier_order = ['龙头', '中军', '弹性', '受益']
        sorted_tiers = [t for t in tier_order if t in tier_groups] + [t for t in tier_groups if t not in tier_order]
        
        tabs = []
        for tier in sorted_tiers:
            tier_stocks = tier_groups[tier]
            
            cards = []
            for stock in tier_stocks:
                name = stock.get('name', '')
                role = stock.get('role', '')
                logic = stock.get('logic', '')
                target_price = stock.get('target_price', '')
                elasticity = stock.get('elasticity_score', '')
                risk_level = stock.get('risk_level', '')
                market_cap = stock.get('market_cap', '')
                
                card_content = f'''
                <div class="flex items-center justify-between mb-3">
                    <div>
                        <h4 class="text-white font-bold">{name}</h4>
                        <p class="text-xs text-white/50">{role}</p>
                    </div>
                    <div class="text-right">
                        <div class="text-sm text-purple-400 font-medium">{market_cap}</div>
                        <div class="text-xs text-white/40">风险: {risk_level}</div>
                    </div>
                </div>
                <div class="mb-2">
                    <div class="text-xs text-blue-400 font-medium mb-1">💡 投资逻辑</div>
                    <p class="text-xs text-white/70">{logic}</p>
                </div>
                <div class="flex items-center justify-between text-xs">
                    <span class="text-white/50">弹性评分</span>
                    <span class="text-green-400 font-medium">{elasticity}分</span>
                </div>
                {target_price and f'<div class="mt-2 text-xs text-yellow-400">🎯 {target_price}</div>'}
                '''
                cards.append({'content': card_content})
            
            tabs.append({
                'label': f"{tier} ({len(tier_stocks)})",
                'content': self.create_card_group(cards=cards, cols=1, card_style='subtle')
            })
        
        tab_html = self.create_tab_pane(tabs=tabs, tab_id="target-stocks", style="default")
        
        content = f'''
            {SectionTitle(text='🎯 核心标的', icon='🎯').render()}
            {tab_html}
        '''
        
        return GlassCard(content=content, padding="p-6", extra_class="mb-6").render()
    
    def _generate_catalyst_timeline(self) -> str:
        """生成催化剂时间线"""
        topic = self.current_topic
        catalysts = topic.get('catalyst_timeline', [])
        if not catalysts:
            return ''
        
        timeline_html = ''
        for i, cat in enumerate(catalysts):
            date = cat.get('date', '')
            event = cat.get('event', '')
            impact = cat.get('impact', '')
            importance = cat.get('importance', 'medium')
            
            is_last = i == len(catalysts) - 1
            
            imp_colors = {
                'high': 'bg-red-500',
                'medium': 'bg-yellow-500',
                'low': 'bg-green-500',
            }
            dot_color = imp_colors.get(importance, 'bg-purple-500')
            
            timeline_html += f'''
            <div class="flex gap-4 {"pb-6" if not is_last else ""}">
                <div class="flex flex-col items-center">
                    <div class="w-3 h-3 {dot_color} rounded-full flex-shrink-0"></div>
                    {'' if is_last else '<div class="w-0.5 flex-1 bg-white/10 mt-1"></div>'}
                </div>
                <div class="flex-1 pb-2">
                    <div class="text-sm text-white/50 mb-1">{date}</div>
                    <h4 class="text-white font-medium mb-1">{event}</h4>
                    {impact and f'<p class="text-sm text-white/60">{impact}</p>'}
                </div>
            </div>
            '''
        
        content = f'''
            {SectionTitle(text='⏰ 催化剂时间线', icon='⏰').render()}
            <div class="pl-2">
                {timeline_html}
            </div>
        '''
        
        return GlassCard(content=content, padding="p-6", extra_class="mb-6").render()
    
    def _generate_risks(self) -> str:
        """生成核心风险 - 卡片组"""
        topic = self.current_topic
        risks = topic.get('core_risks', [])
        if not risks:
            return ''
        
        cards = []
        for risk in risks:
            if isinstance(risk, dict):
                title = risk.get('title', '')
                description = risk.get('description', '')
            else:
                title = str(risk)
                description = ''
            
            card_content = f'''
            <div class="text-red-400 font-medium mb-1">⚠️ {title}</div>
            {description and f'<p class="text-sm text-white/60">{description}</p>'}
            '''
            cards.append({'content': card_content})
        
        cards_html = self.create_card_group(cards=cards, cols=2, card_style='subtle')
        
        content = f'''
            {SectionTitle(text='⚠️ 核心风险', icon='⚠️').render()}
            {cards_html}
        '''
        
        return GlassCard(content=content, padding="p-6", extra_class="mb-6").render()
    
    def _generate_strategy(self) -> str:
        """生成投资策略 - 数据网格+卡片"""
        topic = self.current_topic
        strategy = topic.get('investment_strategy', '')
        if not strategy:
            return ''
        
        # 如果是字典格式，用数据网格展示
        if isinstance(strategy, dict):
            items = []
            position = strategy.get('position', '')
            if position:
                items.append({'title': '建议仓位', 'value': position, 'icon': '📊'})
            entry_point = strategy.get('entry_point', '')
            if entry_point:
                items.append({'title': '入场点位', 'value': entry_point, 'icon': '🎯'})
            stop_loss = strategy.get('stop_loss', '')
            if stop_loss:
                items.append({'title': '止损位', 'value': stop_loss, 'icon': '🛑'})
            take_profit = strategy.get('take_profit', '')
            if take_profit:
                items.append({'title': '止盈位', 'value': take_profit, 'icon': '💰'})
            time_horizon = strategy.get('time_horizon', '')
            if time_horizon:
                items.append({'title': '投资周期', 'value': time_horizon, 'icon': '⏳'})
            
            grid_html = self.create_data_grid(items=items, cols=min(len(items), 4))
            
            content = f'''
                {SectionTitle(text='📈 投资策略', icon='📈').render()}
                {grid_html}
            '''
        else:
            # 字符串格式，用卡片展示
            content = f'''
                {SectionTitle(text='📈 投资策略', icon='📈').render()}
                <div class="p-5 bg-gradient-to-r from-purple-500/10 to-indigo-500/10 border border-purple-500/20 rounded-xl">
                    <p class="text-white/80 leading-relaxed">{strategy}</p>
                </div>
            '''
        
        return GlassCard(content=content, padding="p-6", extra_class="mb-6").render()
    
    def _content(self) -> str:
        """页面主要内容"""
        toc = self._generate_toc()
        overview = self._generate_topic_overview()
        highlights = self._generate_investment_highlights()
        chain = self._generate_industry_chain()
        competitive = self._generate_competitive_landscape()
        downstream = self._generate_downstream_demand()
        stocks = self._generate_target_stocks()
        catalysts = self._generate_catalyst_timeline()
        risks = self._generate_risks()
        strategy = self._generate_strategy()
        
        return f'''
        <div class="max-w-4xl mx-auto">
            {toc}
            {overview}
            {highlights}
            {chain}
            {competitive}
            {downstream}
            {stocks}
            {catalysts}
            {risks}
            {strategy}
        </div>
        '''
    
    def publish(self, output_path: str = "docs/题材深度/index_pro.html"):
        """发布到生产路径"""
        return super().publish(output_path)


if __name__ == '__main__':
    generator = TopicDeepDiveProGenerator()
    html = generator.render()
    
    output_path = '/tmp/test_topic_deep_pro.html'
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"✅ 生成完成")
    print(f"   输出文件: {output_path}")
    print(f"   文件大小: {len(html)} 字节")
    print(f"   题材数量: {len(generator.topics)} 个")
    print(f"   当前题材: {generator.current_topic.get('name', '')}")
