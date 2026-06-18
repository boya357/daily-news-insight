"""
题材/产业链深度研究生成器 - Pro Ultra版
基于Pro组件库重构，深色玻璃态风格
全内容展开 + 自适应模块 + 高级视觉层次感
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

    """题材深度研究 - Pro Ultra版生成器"""
    
    def __init__(self, data_dir: str = "data"):
        super().__init__(
            title="产业链深度研究",
            active_page="产业链",
            footer_text="产业链深度研究 · 洞察投资价值",
            data_dir=data_dir,
            show_toc=True,
        )
        self.topics = {}
        self.current_topic = {}
        self.current_topic_id = ""

    def load_data(self):
        """加载题材详情数据"""
        super().load_data()
        self.data = self.data_loader.get_data("topic_details")
        self.topics = self.data.get('topics', {})
        if self.topics:
            if self.current_topic_id and self.current_topic_id in self.topics:
                self.current_topic = self.topics[self.current_topic_id]
            else:
                first_key = next(iter(self.topics.keys()))
                self.current_topic = self.topics[first_key]
                self.current_topic_id = first_key
        else:
            self.current_topic = {}
            self.current_topic_id = '' 

    def set_topic(self, topic_id: str):
        """设置当前要生成的题材"""
        if not self._data_loaded:
            self.load_data()
        if topic_id in self.topics:
            self.current_topic = self.topics[topic_id]
            self.current_topic_id = topic_id
            topic_name = self.current_topic.get('name', '')
            if '深度研究' in topic_name:
                self.title = topic_name
            else:
                self.title = f"{topic_name}深度研究"
        else:
            raise ValueError(f"题材ID {topic_id} 不存在，可用: {list(self.topics.keys())}")
        return self

    def get_topic_list(self):
        """获取所有可用题材列表"""
        if not self._data_loaded:
            self.load_data()
        return [(tid, t.get('name', '')) for tid, t in self.topics.items()]

    def _has_content(self, data) -> bool:
        """检查数据是否有实质内容"""
        if not data:
            return False
        if isinstance(data, list):
            return len(data) > 0
        if isinstance(data, dict):
            return any(v for v in data.values() if v)
        if isinstance(data, str):
            return len(data.strip()) > 0
        return True

    def _generate_toc(self) -> str:
        """生成题材导航 - 卡片组风格"""
        if not self.topics:
            return ''
        
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
        """生成题材概览 - 豪华大标题+数据网格+摘要"""
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
        
        # 补充默认数据项
        if len(data_items) < 4:
            default_items = [
                {'title': '题材级别', 'value': f'{level}级', 'icon': '⭐'},
                {'title': '覆盖标的', 'value': f"{len(topic.get('target_stocks_analysis', []))}只", 'icon': '🎯'},
                {'title': '催化事件', 'value': f"{len(topic.get('catalyst_timeline', []))}个", 'icon': '⏰'},
                {'title': '风险因素', 'value': f"{len(topic.get('core_risks', []))}项", 'icon': '⚠️'},
            ]
            for item in default_items:
                if len(data_items) >= 4:
                    break
                data_items.append(item)
        
        grid_html = self.create_data_grid(items=data_items[:4], cols=4)
        
        content = f'''
            <!-- 豪华标题区 -->
            <div class="text-center mb-10 relative">
                <!-- 背景装饰 -->
                <div class="absolute inset-0 bg-gradient-to-r {gradient} opacity-5 blur-3xl rounded-3xl"></div>
                
                <div class="relative z-10">
                    <span class="px-5 py-2 bg-gradient-to-r {gradient} text-white text-sm font-bold rounded-full mb-5 inline-block shadow-lg shadow-black/20">
                        🏆 {level}级题材
                    </span>
                    <h1 class="text-4xl md:text-5xl font-black text-white mb-4 bg-gradient-to-r from-white via-white to-white/70 bg-clip-text text-transparent">
                        {name}
                    </h1>
                    <p class="text-white/70 max-w-3xl mx-auto leading-relaxed text-lg">
                        {summary}
                    </p>
                </div>
            </div>
            
            <!-- 核心数据卡片 -->
            <div class="mb-10">
                {grid_html}
            </div>
        '''
        
        return content
    
    def _generate_investment_highlights(self) -> str:
        """生成投资要点 - 豪华卡片组带图标背景"""
        topic = self.current_topic
        if not topic:
            return ''
        
        highlights = topic.get('investment_highlights', [])
        
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
        
        icon_gradients = [
            'from-blue-500 to-cyan-500',
            'from-purple-500 to-pink-500',
            'from-orange-500 to-yellow-500',
            'from-green-500 to-emerald-500',
            'from-red-500 to-rose-500',
            'from-indigo-500 to-violet-500',
        ]
        
        cards_html = ''
        for i, h in enumerate(highlights):
            title = h.get('title', '')
            content = h.get('content', '')
            icon = h.get('icon', '📌')
            gradient = icon_gradients[i % len(icon_gradients)]
            
            cards_html += f'''
            <div class="relative bg-white/5 backdrop-blur-sm border border-white/10 rounded-2xl p-6 hover:bg-white/10 hover:border-white/20 transition-all duration-300 group overflow-hidden">
                <!-- 装饰背景 -->
                <div class="absolute -right-4 -top-4 w-24 h-24 bg-gradient-to-br {gradient} opacity-10 rounded-full blur-xl group-hover:opacity-20 transition-opacity"></div>
                
                <div class="relative z-10">
                    <div class="flex items-center gap-4 mb-4">
                        <div class="w-14 h-14 rounded-2xl bg-gradient-to-br {gradient} flex items-center justify-center text-2xl shadow-lg shadow-black/20">
                            {icon}
                        </div>
                        <h3 class="text-xl font-bold text-white">{title}</h3>
                    </div>
                    <p class="text-white/70 leading-relaxed text-sm">
                        {content}
                    </p>
                </div>
            </div>
            '''
        
        cols = 'grid-cols-1 md:grid-cols-2' if len(highlights) >= 2 else 'grid-cols-1'
        
        content = f'''
            <div class="mb-10">
                {SectionTitle(text='💡 投资要点', icon='💡', subtitle='核心投资逻辑与价值亮点').render()}
                <div class="grid {cols} gap-5">
                    {cards_html}
                </div>
            </div>
        '''
        
        return content
    
    def _generate_industry_chain(self) -> str:
        """生成产业链分析 - 全展开可视化流程+详细卡片"""
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
        section_gradients = {
            'upstream': 'from-blue-600 to-cyan-500',
            'midstream': 'from-purple-600 to-pink-500',
            'downstream': 'from-orange-600 to-yellow-500',
        }
        section_icons = {
            'upstream': '⛏️',
            'midstream': '🏭',
            'downstream': '📦',
        }
        
        # 检查是否有实际内容
        has_content = False
        for section_key in sections:
            section = chain.get(section_key, {})
            if section and (section.get('description') or section.get('companies') or section.get('name')):
                has_content = True
                break
        
        if not has_content:
            return ''
        
        # 生成各环节内容
        sections_html = ''
        for section_key in sections:
            section = chain.get(section_key, {})
            if not section:
                continue
            
            section_name = section.get('name', section_names.get(section_key, section_key))
            description = section.get('description', '') or section.get('desc', '')
            companies = section.get('companies', [])
            
            # 公司卡片
            companies_html = ''
            if companies:
                for comp in companies:
                    comp_name = comp.get('name', '')
                    role = comp.get('role', '') or comp.get('desc', '') or comp.get('tag', '')
                    importance = comp.get('importance', self._tag_to_importance(comp.get('tag', '')))
                    market_share = comp.get('market_share', '')
                    
                    imp_label = {'high': '核心', 'medium': '重要', 'low': '一般'}.get(importance, '重要')
                    imp_color = {'high': 'red', 'medium': 'yellow', 'low': 'green'}.get(importance, 'blue')
                    
                    companies_html += f'''
                    <div class="bg-white/5 border border-white/10 rounded-xl p-4 hover:bg-white/10 transition-colors">
                        <div class="flex items-center justify-between mb-2">
                            <span class="text-white font-semibold">{comp_name}</span>
                            <span class="px-2 py-0.5 bg-{imp_color}-500/20 text-{imp_color}-400 text-xs font-medium rounded-full">{imp_label}</span>
                        </div>
                        <p class="text-xs text-white/60 leading-relaxed">{role}</p>
                        {market_share and f'<div class="mt-2 text-xs text-blue-400 font-medium">市占率: {market_share}</div>'}
                    </div>
                    '''
            
            gradient = section_gradients.get(section_key, 'from-gray-500 to-gray-600')
            icon = section_icons.get(section_key, '🔗')
            
            sections_html += f'''
            <!-- {section_name}环节 -->
            <div class="mb-8 last:mb-0">
                <!-- 环节标题 -->
                <div class="flex items-center gap-4 mb-5">
                    <div class="w-12 h-12 rounded-xl bg-gradient-to-br {gradient} flex items-center justify-center text-xl shadow-lg">
                        {icon}
                    </div>
                    <div>
                        <h3 class="text-xl font-bold text-white">{section_name}</h3>
                        <div class="text-xs text-white/50">{len(companies)}家代表企业</div>
                    </div>
                    <div class="flex-1 h-px bg-gradient-to-r from-white/20 to-transparent ml-4"></div>
                </div>
                
                <!-- 环节描述 -->
                {description and f'''
                <div class="mb-5 p-5 bg-gradient-to-r {gradient}/5 border-l-4 border-{gradient.split('-')[1]}-500/50 rounded-r-xl">
                    <p class="text-white/80 leading-relaxed text-sm">{description}</p>
                </div>
                '''}
                
                <!-- 代表企业网格 -->
                {companies and f'''
                <div class="grid grid-cols-1 md:grid-cols-2 gap-3">
                    {companies_html}
                </div>
                '''}
            </div>
            '''
        
        content = f'''
            <div class="mb-10">
                {SectionTitle(text='🔗 产业链分析', icon='🔗', subtitle='上中下游全产业链梳理').render()}
                <div class="bg-white/[0.03] backdrop-blur-sm border border-white/10 rounded-3xl p-8">
                    {sections_html}
                </div>
            </div>
        '''
        
        return content
    
    def _generate_competitive_landscape(self) -> str:
        """生成竞争格局分析 - 全展开多维度对比"""
        topic = self.current_topic
        if not topic:
            return ''
        
        landscape = topic.get('competitive_landscape', {})
        
        # 收集所有有内容的维度
        dimensions = []
        
        # 全球竞争
        global_companies = landscape.get('global', [])
        if global_companies:
            dimensions.append(('global', '全球厂商', global_companies, '🌍', 'from-blue-500 to-indigo-500'))
        
        # 国内竞争
        domestic_companies = landscape.get('domestic', [])
        if domestic_companies:
            dimensions.append(('domestic', '国内厂商', domestic_companies, '🇨🇳', 'from-red-500 to-orange-500'))
        
        # 价值链
        value_chain = landscape.get('value_chain', [])
        if value_chain:
            dimensions.append(('value_chain', '价值链分析', value_chain, '💰', 'from-purple-500 to-pink-500'))
        
        # 如果没有专门的竞争格局数据，从产业链提取
        if not dimensions:
            chain = topic.get('industry_chain', {})
            all_companies = []
            for section_key in ['upstream', 'midstream', 'downstream']:
                section = chain.get(section_key, {})
                section_name = section.get('name', section_key)
                companies = section.get('companies', [])
                for comp in companies:
                    comp['section'] = section_name
                    all_companies.append(comp)
            
            if all_companies:
                high_importance = [c for c in all_companies if c.get('importance') == 'high']
                if high_importance:
                    dimensions.append(('core', '核心厂商', high_importance, '⭐', 'from-yellow-500 to-orange-500'))
                
                medium_importance = [c for c in all_companies if c.get('importance') == 'medium']
                if medium_importance:
                    dimensions.append(('important', '重要厂商', medium_importance, '📌', 'from-blue-500 to-cyan-500'))
                
                if not dimensions:
                    dimensions.append(('all', '全部厂商', all_companies, '🏢', 'from-gray-500 to-gray-600'))
        
        if not dimensions:
            return ''
        
        # 生成各维度内容
        dimensions_html = ''
        for dim_key, dim_label, items, icon, gradient in dimensions:
            # 生成项目卡片
            items_html = ''
            for item in items:
                name = item.get('name', '')
                desc = item.get('desc', '') or item.get('role', '')
                market_share = item.get('market_share', '')
                value_ratio = item.get('value_ratio', '')
                section = item.get('section', '')
                
                # 市占率进度条
                progress_bar = ''
                if market_share:
                    try:
                        # 提取数字
                        import re
                        num = float(re.findall(r'[\d.]+', str(market_share))[0])
                        if num <= 100:
                            progress_width = min(num, 100)
                            progress_bar = f'''
                            <div class="mt-2">
                                <div class="flex justify-between text-xs mb-1">
                                    <span class="text-white/50">市占率</span>
                                    <span class="text-blue-400 font-medium">{market_share}</span>
                                </div>
                                <div class="h-1.5 bg-white/10 rounded-full overflow-hidden">
                                    <div class="h-full bg-gradient-to-r {gradient} rounded-full" style="width: {progress_width}%"></div>
                                </div>
                            </div>
                            '''
                    except:
                        progress_bar = f'<div class="mt-2 text-xs text-blue-400 font-medium">市占率: {market_share}</div>'
                
                if value_ratio:
                    try:
                        import re
                        num = float(re.findall(r'[\d.]+', str(value_ratio))[0])
                        if num <= 100:
                            progress_width = min(num, 100)
                            progress_bar = f'''
                            <div class="mt-2">
                                <div class="flex justify-between text-xs mb-1">
                                    <span class="text-white/50">价值占比</span>
                                    <span class="text-purple-400 font-medium">{value_ratio}</span>
                                </div>
                                <div class="h-1.5 bg-white/10 rounded-full overflow-hidden">
                                    <div class="h-full bg-gradient-to-r {gradient} rounded-full" style="width: {progress_width}%"></div>
                                </div>
                            </div>
                            '''
                    except:
                        progress_bar = f'<div class="mt-2 text-xs text-purple-400 font-medium">价值占比: {value_ratio}</div>'
                
                items_html += f'''
                <div class="bg-white/5 border border-white/10 rounded-xl p-5 hover:bg-white/10 hover:border-white/20 transition-all duration-300">
                    <div class="flex items-start justify-between mb-2">
                        <h4 class="text-white font-semibold text-base">{name}</h4>
                        {section and f'<span class="text-xs text-white/40 bg-white/5 px-2 py-0.5 rounded-full">{section}</span>'}
                    </div>
                    <p class="text-sm text-white/60 leading-relaxed">{desc}</p>
                    {progress_bar}
                </div>
                '''
            
            dimensions_html += f'''
            <!-- {dim_label} -->
            <div class="mb-8 last:mb-0">
                <div class="flex items-center gap-3 mb-5">
                    <div class="w-10 h-10 rounded-lg bg-gradient-to-br {gradient} flex items-center justify-center text-lg">
                        {icon}
                    </div>
                    <h3 class="text-lg font-bold text-white">{dim_label}</h3>
                    <span class="text-xs text-white/40 bg-white/5 px-2.5 py-1 rounded-full">{len(items)}家</span>
                </div>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-3">
                    {items_html}
                </div>
            </div>
            '''
        
        content = f'''
            <div class="mb-10">
                {SectionTitle(text='🏢 竞争格局', icon='🏢', subtitle='全球与国内厂商对比分析').render()}
                <div class="bg-white/[0.03] backdrop-blur-sm border border-white/10 rounded-3xl p-8">
                    {dimensions_html}
                </div>
            </div>
        '''
        
        return content
    
    def _generate_downstream_demand(self) -> str:
        """生成下游需求/应用分析 - 全展开卡片"""
        topic = self.current_topic
        if not topic:
            return ''
        
        downstream = topic.get('downstream_demand', []) or topic.get('downstream_applications', [])
        
        # 如果没有专门数据，从产业链下游提取
        if not downstream:
            chain = topic.get('industry_chain', {})
            down_section = chain.get('downstream', {})
            companies = down_section.get('companies', [])
            if companies:
                downstream = [{'title': c.get('name', ''), 'content': c.get('role', '') or c.get('desc', ''), 'icon': '📦'} for c in companies[:6]]
        
        if not downstream:
            return ''
        
        cards_html = ''
        icon_gradients = [
            'from-orange-500 to-red-500',
            'from-green-500 to-emerald-500',
            'from-blue-500 to-cyan-500',
            'from-purple-500 to-pink-500',
            'from-yellow-500 to-orange-500',
            'from-indigo-500 to-purple-500',
        ]
        
        for i, item in enumerate(downstream):
            if isinstance(item, dict):
                title = item.get('title', '')
                content = item.get('content', '') or item.get('description', '')
                icon = item.get('icon', '📦')
            else:
                title = str(item)
                content = ''
                icon = '📦'
            
            gradient = icon_gradients[i % len(icon_gradients)]
            
            cards_html += f'''
            <div class="relative bg-white/5 border border-white/10 rounded-2xl p-6 hover:bg-white/10 hover:border-white/20 transition-all duration-300 group overflow-hidden">
                <div class="absolute -right-3 -bottom-3 w-20 h-20 bg-gradient-to-br {gradient} opacity-10 rounded-full blur-xl group-hover:opacity-20 transition-opacity"></div>
                
                <div class="relative z-10 flex items-start gap-4">
                    <div class="w-12 h-12 rounded-xl bg-gradient-to-br {gradient} flex items-center justify-center text-xl flex-shrink-0 shadow-lg">
                        {icon}
                    </div>
                    <div>
                        <h4 class="text-white font-semibold mb-2">{title}</h4>
                        <p class="text-sm text-white/60 leading-relaxed">{content}</p>
                    </div>
                </div>
            </div>
            '''
        
        content = f'''
            <div class="mb-10">
                {SectionTitle(text='📦 下游应用', icon='📦', subtitle='主要应用场景与需求分析').render()}
                <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                    {cards_html}
                </div>
            </div>
        '''
        
        return content
    
    def _tag_to_importance(self, tag: str) -> str:
        """将标签转换为importance等级"""
        if not tag:
            return 'medium'
        if '核心' in tag or '龙头' in tag:
            return 'high'
        elif '重要' in tag or '中军' in tag:
            return 'medium'
        elif tag:
            return 'low'
        return 'medium'

    def _generate_target_stocks(self) -> str:
        """生成核心标的分析 - 全展开豪华卡片"""
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
        
        tier_order = ['龙头', '中军', '弹性', '受益']
        sorted_tiers = [t for t in tier_order if t in tier_groups] + [t for t in tier_groups if t not in tier_order]
        
        tier_colors = {
            '龙头': 'from-yellow-500 to-orange-500',
            '中军': 'from-blue-500 to-cyan-500',
            '弹性': 'from-purple-500 to-pink-500',
            '受益': 'from-green-500 to-emerald-500',
        }
        
        # 生成各梯队内容
        tiers_html = ''
        for tier in sorted_tiers:
            tier_stocks = tier_groups[tier]
            gradient = tier_colors.get(tier, 'from-gray-500 to-gray-600')
            
            stocks_html = ''
            for stock in tier_stocks:
                name = stock.get('name', '')
                code = stock.get('code', '')
                logic = stock.get('logic', '')
                target_price = stock.get('target_price', '')
                rating = stock.get('rating', '')
                pe_ratio = stock.get('pe_ratio', '')
                market_cap = stock.get('market_cap', '')
                advantage = stock.get('advantage', '')
                risk = stock.get('risk', '')
                
                stocks_html += f'''
                <div class="relative bg-white/5 border border-white/10 rounded-2xl p-6 hover:bg-white/[0.08] hover:border-white/20 transition-all duration-300 overflow-hidden">
                    <!-- 顶部装饰条 -->
                    <div class="absolute top-0 left-0 right-0 h-1 bg-gradient-to-r {gradient}"></div>
                    
                    <!-- 头部信息 -->
                    <div class="flex items-start justify-between mb-4">
                        <div>
                            <h4 class="text-xl font-bold text-white mb-1">{name}</h4>
                            <p class="text-sm text-white/50">{code}</p>
                        </div>
                        <div class="text-right">
                            <div class="text-lg font-bold text-white">{market_cap}</div>
                            <div class="text-xs text-white/40">市值</div>
                        </div>
                    </div>
                    
                    <!-- 关键指标行 -->
                    <div class="grid grid-cols-3 gap-3 mb-4 pb-4 border-b border-white/10">
                        <div class="text-center">
                            <div class="text-purple-400 font-bold text-lg">{pe_ratio}</div>
                            <div class="text-xs text-white/40">PE</div>
                        </div>
                        <div class="text-center">
                            <div class="text-green-400 font-bold text-lg">{rating}</div>
                            <div class="text-xs text-white/40">评级</div>
                        </div>
                        <div class="text-center">
                            <div class="text-yellow-400 font-bold text-lg">{target_price}</div>
                            <div class="text-xs text-white/40">目标价</div>
                        </div>
                    </div>
                    
                    <!-- 投资逻辑 -->
                    <div class="mb-3">
                        <div class="text-xs text-blue-400 font-medium mb-2 flex items-center gap-1">
                            <span>💡</span> 投资逻辑
                        </div>
                        <p class="text-sm text-white/70 leading-relaxed">{logic}</p>
                    </div>
                    
                    <!-- 优势与风险 -->
                    <div class="grid grid-cols-2 gap-3 mt-4">
                        {advantage and f'''
                        <div class="bg-green-500/10 border border-green-500/20 rounded-lg p-3">
                            <div class="text-xs text-green-400 font-medium mb-1">✅ 核心优势</div>
                            <p class="text-xs text-white/60">{advantage}</p>
                        </div>
                        '''}
                        {risk and f'''
                        <div class="bg-red-500/10 border border-red-500/20 rounded-lg p-3">
                            <div class="text-xs text-red-400 font-medium mb-1">⚠️ 主要风险</div>
                            <p class="text-xs text-white/60">{risk}</p>
                        </div>
                        '''}
                    </div>
                </div>
                '''
            
            tiers_html += f'''
            <!-- {tier}梯队 -->
            <div class="mb-10 last:mb-0">
                <div class="flex items-center gap-3 mb-5">
                    <div class="w-10 h-10 rounded-lg bg-gradient-to-br {gradient} flex items-center justify-center text-white font-bold text-sm">
                        {tier[0]}
                    </div>
                    <div>
                        <h3 class="text-lg font-bold text-white">{tier}标的</h3>
                        <p class="text-xs text-white/40">{len(tier_stocks)}只</p>
                    </div>
                </div>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-5">
                    {stocks_html}
                </div>
            </div>
            '''
        
        content = f'''
            <div class="mb-10">
                {SectionTitle(text='🎯 核心标的', icon='🎯', subtitle='分梯队详细分析与投资建议').render()}
                <div class="bg-white/[0.02] backdrop-blur-sm border border-white/10 rounded-3xl p-8">
                    {tiers_html}
                </div>
            </div>
        '''
        
        return content
    
    def _generate_catalyst_timeline(self) -> str:
        """生成催化剂时间线 - 豪华时间轴"""
        topic = self.current_topic
        catalysts = topic.get('catalyst_timeline', [])
        if not catalysts:
            return ''
        
        timeline_html = ''
        for i, cat in enumerate(catalysts):
            date = cat.get('time', cat.get('date', ''))
            event = cat.get('event', '')
            impact = cat.get('impact', '')
            importance = cat.get('importance', 'medium')
            
            is_last = i == len(catalysts) - 1
            
            imp_colors = {
                'high': 'from-red-500 to-orange-500',
                'medium': 'from-yellow-500 to-amber-500',
                'low': 'from-green-500 to-emerald-500',
            }
            imp_labels = {
                'high': '高',
                'medium': '中',
                'low': '低',
            }
            dot_gradient = imp_colors.get(importance, 'from-purple-500 to-indigo-500')
            imp_label = imp_labels.get(importance, '中')
            
            timeline_html += f'''
            <div class="flex gap-5 {"pb-8" if not is_last else ""} relative">
                <!-- 时间轴线 -->
                <div class="flex flex-col items-center">
                    <div class="w-5 h-5 rounded-full bg-gradient-to-br {dot_gradient} flex-shrink-0 shadow-lg shadow-black/30 relative z-10 ring-4 ring-black/20"></div>
                    {'' if is_last else '<div class="w-0.5 flex-1 bg-gradient-to-b from-white/20 to-white/5 mt-2"></div>'}
                </div>
                
                <!-- 内容卡片 -->
                <div class="flex-1 bg-white/5 border border-white/10 rounded-xl p-5 hover:bg-white/10 transition-colors -mt-1">
                    <div class="flex items-center justify-between mb-2">
                        <span class="text-sm text-white/50 font-medium">{date}</span>
                        <span class="text-xs px-2 py-0.5 bg-gradient-to-r {dot_gradient} text-white rounded-full font-medium">
                            {imp_label}影响
                        </span>
                    </div>
                    <h4 class="text-white font-semibold text-base mb-2">{event}</h4>
                    {impact and f'<p class="text-sm text-white/60 leading-relaxed">{impact}</p>'}
                </div>
            </div>
            '''
        
        content = f'''
            <div class="mb-10">
                {SectionTitle(text='⏰ 催化剂时间线', icon='⏰', subtitle='重要事件与催化节点梳理').render()}
                <div class="bg-white/[0.03] backdrop-blur-sm border border-white/10 rounded-3xl p-8 pl-10">
                    {timeline_html}
                </div>
            </div>
        '''
        
        return content
    
    def _generate_risks(self) -> str:
        """生成核心风险 - 警告风格卡片"""
        topic = self.current_topic
        risks = topic.get('core_risks', [])
        if not risks:
            return ''
        
        cards_html = ''
        for risk in risks:
            if isinstance(risk, dict):
                title = risk.get('title', '')
                description = risk.get('description', '') or risk.get('content', '')
                level = risk.get('level', 'medium')
            else:
                title = str(risk)
                description = ''
                level = 'medium'
            
            level_colors = {
                'high': 'from-red-600 to-rose-600',
                'medium': 'from-orange-500 to-amber-500',
                'low': 'from-yellow-500 to-lime-500',
            }
            gradient = level_colors.get(level, 'from-orange-500 to-amber-500')
            
            cards_html += f'''
            <div class="relative bg-gradient-to-br from-red-500/[0.08] to-orange-500/[0.05] border border-red-500/20 rounded-2xl p-6 hover:from-red-500/10 hover:to-orange-500/[0.08] transition-all duration-300 overflow-hidden">
                <!-- 装饰 -->
                <div class="absolute top-0 right-0 w-32 h-32 bg-gradient-to-br {gradient} opacity-5 rounded-full blur-2xl -translate-y-1/2 translate-x-1/2"></div>
                
                <div class="relative z-10">
                    <div class="flex items-center gap-3 mb-3">
                        <div class="w-10 h-10 rounded-xl bg-gradient-to-br {gradient} flex items-center justify-center">
                            ⚠️
                        </div>
                        <h4 class="text-white font-semibold text-lg">{title}</h4>
                    </div>
                    <p class="text-sm text-white/70 leading-relaxed pl-13">
                        {description}
                    </p>
                </div>
            </div>
            '''
        
        content = f'''
            <div class="mb-10">
                {SectionTitle(text='⚠️ 核心风险', icon='⚠️', subtitle='投资需关注的主要风险因素').render()}
                <div class="grid grid-cols-1 md:grid-cols-2 gap-5">
                    {cards_html}
                </div>
            </div>
        '''
        
        return content
    
    def _generate_charts(self) -> str:
        """生成数据可视化图表 - 使用Pro图表组件"""
        from components.pro import ProLineChart, ProPieChart, ProBarChart
        
        topic = self.current_topic
        if not topic:
            return ''
        
        charts = []
        market_size = topic.get('market_size', {})
        landscape = topic.get('competitive_landscape', {})
        
        # 1. 市场规模增长趋势图
        if market_size:
            total_2026 = market_size.get('total_2026', '')
            growth_rate = market_size.get('growth_rate', '')
            
            try:
                import re
                if total_2026 and growth_rate:
                    val_2026 = float(re.findall(r'[\d.]+', str(total_2026))[0])
                    growth = float(re.findall(r'[\d.]+', str(growth_rate))[0]) / 100
                    
                    # 倒推和预测
                    val_2023 = round(val_2026 / ((1 + growth) ** 3), 1)
                    val_2024 = round(val_2023 * (1 + growth), 1)
                    val_2025 = round(val_2024 * (1 + growth), 1)
                    val_2027 = round(val_2026 * (1 + growth), 1)
                    
                    chart = ProLineChart(
                        labels=['2023', '2024', '2025', '2026E', '2027E'],
                        datasets=[{
                            'label': '市场规模（亿美元）',
                            'data': [val_2023, val_2024, val_2025, val_2026, val_2027],
                        }],
                        title='HBM市场规模趋势',
                        height=260
                    )
                    charts.append(chart.render())
            except:
                pass
        
        # 2. 竞争格局饼图
        if landscape:
            global_companies = landscape.get('global', [])
            if global_companies and len(global_companies) >= 2:
                pie_labels = []
                pie_values = []
                for comp in global_companies:
                    name = comp.get('name', '')
                    ms = comp.get('market_share', '')
                    try:
                        import re
                        val = float(re.findall(r'[\d.]+', str(ms))[0])
                        pie_labels.append(name)
                        pie_values.append(val)
                    except:
                        pass
                
                if len(pie_labels) >= 2:
                    chart = ProPieChart(
                        labels=pie_labels,
                        data=pie_values,
                        title='全球厂商市占率',
                        height=260,
                        donut=True
                    )
                    charts.append(chart.render())
        
        # 3. 价值链分析柱状图
        if landscape:
            value_chain = landscape.get('value_chain', [])
            if value_chain and len(value_chain) >= 2:
                bar_labels = []
                bar_values = []
                for item in value_chain:
                    name = item.get('name', '')
                    ratio = item.get('value_ratio', '')
                    try:
                        import re
                        val = float(re.findall(r'[\d.]+', str(ratio))[0])
                        bar_labels.append(name)
                        bar_values.append(val)
                    except:
                        pass
                
                if bar_labels:
                    chart = ProBarChart(
                        labels=bar_labels,
                        datasets=[{'label': '价值占比（%）', 'data': bar_values}],
                        title='产业链价值分布',
                        height=260,
                        horizontal=True
                    )
                    charts.append(chart.render())
        
        if not charts:
            return ''
        
        # 组装图表卡片
        charts_html = ''
        for chart_html in charts:
            charts_html += f'''
            <div class="bg-white/5 border border-white/10 rounded-2xl p-6 hover:bg-white/[0.08] transition-all">
                {chart_html}
            </div>
            '''
        
        # Chart.js CDN 会在基类中统一引入
        content = f'''
            <div class="mb-10">
                {SectionTitle(text='📊 数据洞察', icon='📊', subtitle='关键数据可视化分析').render()}
                <div class="grid grid-cols-1 md:grid-cols-{min(len(charts), 2)} gap-5">
                    {charts_html}
                </div>
            </div>
        '''
        
        return content
    
    def _generate_strategy(self) -> str:
        """生成投资策略 - 数据网格+策略说明"""
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
            time_horizon = strategy.get('time_horizon', '') or strategy.get('investment_cycle', '')
            if time_horizon:
                items.append({'title': '投资周期', 'value': time_horizon, 'icon': '⏳'})
            core_logic = strategy.get('core_logic', '')
            if core_logic:
                items.append({'title': '核心逻辑', 'value': core_logic, 'icon': '💡'})
            
            if items:
                grid_html = self.create_data_grid(items=items, cols=min(len(items), 4))
                
                content = f'''
                    <div class="mb-10">
                        {SectionTitle(text='📈 投资策略', icon='📈', subtitle='操作建议与仓位管理').render()}
                        {grid_html}
                    </div>
                '''
            else:
                return ''
        else:
            # 字符串格式，用卡片展示
            content = f'''
                <div class="mb-10">
                    {SectionTitle(text='📈 投资策略', icon='📈', subtitle='操作建议与仓位管理').render()}
                    <div class="bg-gradient-to-r from-purple-500/10 via-indigo-500/10 to-blue-500/10 border border-purple-500/20 rounded-2xl p-8">
                        <p class="text-white/80 leading-relaxed text-base">{strategy}</p>
                    </div>
                </div>
            '''
        
        return content

    def _content(self) -> str:
        """页面主要内容 - 自适应模块渲染"""
        topic = self.current_topic
        if not topic:
            return '<div class="text-center text-white/50 py-20">暂无数据</div>'
        
        # 按顺序收集有内容的模块
        modules = []
        
        # 题材导航（可选）
        toc = self._generate_toc()
        if toc and len(self.topics) > 1:
            modules.append(toc)
        
        # 题材概览 - 必须有
        overview = self._generate_topic_overview()
        if overview:
            modules.append(overview)
        
        # 投资要点
        highlights = self._generate_investment_highlights()
        if highlights:
            modules.append(highlights)
        
        # 数据洞察图表
        charts = self._generate_charts()
        if charts:
            modules.append(charts)
        
        # 产业链分析
        chain = self._generate_industry_chain()
        if chain:
            modules.append(chain)
        
        # 竞争格局
        competitive = self._generate_competitive_landscape()
        if competitive:
            modules.append(competitive)
        
        # 下游应用
        downstream = self._generate_downstream_demand()
        if downstream:
            modules.append(downstream)
        
        # 核心标的
        stocks = self._generate_target_stocks()
        if stocks:
            modules.append(stocks)
        
        # 催化剂时间线
        catalysts = self._generate_catalyst_timeline()
        if catalysts:
            modules.append(catalysts)
        
        # 核心风险
        risks = self._generate_risks()
        if risks:
            modules.append(risks)
        
        # 投资策略
        strategy = self._generate_strategy()
        if strategy:
            modules.append(strategy)
        
        return f'''
        <div class="max-w-5xl mx-auto">
            {''.join(modules)}
        </div>
        '''
    
    def publish(self, output_path: str = "docs/topic-depth/index.html"):
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
