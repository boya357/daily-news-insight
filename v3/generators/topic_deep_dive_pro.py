"""
题材深度生成器 - Pro版
基于Pro组件库重构，深色玻璃态风格
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

    """题材深度 - Pro版生成器"""
    
    def __init__(self, data_dir: str = "data"):
        super().__init__(
            title="题材深度研究",
            active_page="产业链",
            footer_text="题材深度研究 · 洞察投资价值",
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
        """生成题材导航"""
        if not self.topics:
            return ''
        
        tabs_html = ''
        for tid, topic in self.topics.items():
            name = topic.get('name', '')
            level = topic.get('level', '')
            is_active = tid == self.current_topic_id
            
            level_colors = {
                'S': 'bg-red-500/20 text-red-400',
                'A': 'bg-yellow-500/20 text-yellow-400',
                'B': 'bg-green-500/20 text-green-400',
            }
            level_color = level_colors.get(level, 'bg-gray-500/20 text-gray-400')
            
            active_class = 'bg-white/20 border-white/30' if is_active else 'bg-white/5 border-white/10 hover:bg-white/10'
            
            tabs_html += f'''
            <div class="{active_class} border rounded-xl p-4 cursor-pointer transition-all">
                <div class="flex items-center justify-between">
                    <span class="text-white font-medium">{name}</span>
                    <span class="px-2 py-0.5 {level_color} text-xs font-bold rounded-full">{level}级</span>
                </div>
            </div>
            '''
        
        content = f'''
            {SectionTitle(text='📋 题材列表', icon='📋').render()}
            <div class="grid grid-cols-2 md:grid-cols-4 gap-3">
                {tabs_html}
            </div>
        '''
        
        return GlassCard(content=content, padding="p-6", extra_class="mb-6").render()
    
    def _generate_topic_overview(self) -> str:
        """生成题材概览"""
        topic = self.current_topic
        if not topic:
            return ''
        
        name = topic.get('name', '')
        level = topic.get('level', '')
        summary = topic.get('summary', '')
        market_size = topic.get('market_size', '')
        
        level_colors = {
            'S': 'from-red-500 to-orange-500',
            'A': 'from-yellow-500 to-amber-500',
            'B': 'from-green-500 to-emerald-500',
        }
        gradient = level_colors.get(level, 'from-purple-500 to-indigo-500')
        
        content = f'''
            <div class="text-center mb-8">
                <span class="px-4 py-1.5 bg-gradient-to-r {gradient} text-white text-sm font-bold rounded-full mb-4 inline-block">
                    {level}级题材
                </span>
                <h1 class="text-3xl md:text-4xl font-black text-white mb-4">{name}</h1>
                <p class="text-white/70 max-w-2xl mx-auto">{summary}</p>
                {market_size and f'<div class="mt-4 text-lg text-purple-400 font-medium">市场空间: {market_size}</div>'}
            </div>
        '''
        
        return content
    
    def _generate_industry_chain(self) -> str:
        """生成产业链分析"""
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
        section_colors = {
            'upstream': 'from-blue-500 to-cyan-500',
            'midstream': 'from-purple-500 to-pink-500',
            'downstream': 'from-orange-500 to-red-500',
        }
        
        chain_html = ''
        for section_key in sections:
            section = chain.get(section_key, {})
            if not section:
                continue
            
            section_name = section.get('name', section_names.get(section_key, section_key))
            description = section.get('description', '')
            companies = section.get('companies', [])
            
            companies_html = ''
            for comp in companies:
                comp_name = comp.get('name', '')
                role = comp.get('role', '')
                importance = comp.get('importance', '')
                
                imp_color = {
                    'high': 'bg-red-500/20 text-red-400',
                    'medium': 'bg-yellow-500/20 text-yellow-400',
                    'low': 'bg-green-500/20 text-green-400',
                }.get(importance, 'bg-gray-500/20 text-gray-400')
                
                imp_text = {'high': '核心', 'medium': '重要', 'low': '一般'}.get(importance, '')
                
                companies_html += f'''
                <div class="flex items-center justify-between p-3 bg-white/5 rounded-lg mb-2 last:mb-0">
                    <div>
                        <div class="text-white font-medium">{comp_name}</div>
                        <div class="text-xs text-white/50">{role}</div>
                    </div>
                    {imp_text and f'<span class="px-2 py-0.5 {imp_color} text-xs rounded-full">{imp_text}</span>'}
                </div>
                '''
            
            gradient = section_colors.get(section_key, 'from-purple-500 to-indigo-500')
            
            chain_html += f'''
            <div class="bg-white/5 border border-white/10 rounded-xl p-5">
                <div class="flex items-center gap-2 mb-3">
                    <div class="w-2 h-2 bg-gradient-to-r {gradient} rounded-full"></div>
                    <h3 class="text-white font-bold">{section_name}</h3>
                </div>
                <p class="text-sm text-white/60 mb-4">{description}</p>
                {companies_html}
            </div>
            '''
        
        content = f'''
            {SectionTitle(text='🔗 产业链分析', icon='🔗').render()}
            <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
                {chain_html}
            </div>
        '''
        
        return GlassCard(content=content, padding="p-6", extra_class="mb-6").render()
    
    def _generate_target_stocks(self) -> str:
        """生成核心标的分析"""
        topic = self.current_topic
        stocks = topic.get('target_stocks_analysis', [])
        if not stocks:
            return ''
        
        stocks_html = ''
        for stock in stocks:
            name = stock.get('name', '')
            code = stock.get('code', '')
            role = stock.get('role', '')
            logic = stock.get('investment_logic', '')
            advantage = stock.get('core_advantage', '')
            risk = stock.get('risk', '')
            rating = stock.get('rating', '')
            
            stocks_html += f'''
            <div class="bg-white/5 border border-white/10 rounded-xl p-5">
                <div class="flex items-center justify-between mb-3">
                    <div>
                        <h3 class="text-white font-bold text-lg">{name}</h3>
                        <p class="text-sm text-white/50">{code} · {role}</p>
                    </div>
                    {rating and f'<span class="px-3 py-1 bg-purple-500/20 text-purple-400 text-sm font-bold rounded-full">{rating}</span>'}
                </div>
                
                {logic and f'''
                <div class="mb-3">
                    <div class="text-xs text-purple-400 font-medium mb-1">💡 投资逻辑</div>
                    <p class="text-sm text-white/70">{logic}</p>
                </div>
                '''}
                
                {advantage and f'''
                <div class="mb-3">
                    <div class="text-xs text-green-400 font-medium mb-1">✅ 核心优势</div>
                    <p class="text-sm text-white/70">{advantage}</p>
                </div>
                '''}
                
                {risk and f'''
                <div>
                    <div class="text-xs text-red-400 font-medium mb-1">⚠️ 风险提示</div>
                    <p class="text-sm text-white/70">{risk}</p>
                </div>
                '''}
            </div>
            '''
        
        content = f'''
            {SectionTitle(text='🎯 核心标的', icon='🎯').render()}
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                {stocks_html}
            </div>
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
        """生成核心风险"""
        topic = self.current_topic
        risks = topic.get('core_risks', [])
        if not risks:
            return ''
        
        risks_html = ''
        for risk in risks:
            if isinstance(risk, dict):
                title = risk.get('title', '')
                description = risk.get('description', '')
            else:
                title = str(risk)
                description = ''
            
            risks_html += f'''
            <div class="bg-red-500/10 border border-red-500/20 rounded-xl p-4">
                <h4 class="text-red-400 font-medium mb-1">⚠️ {title}</h4>
                {description and f'<p class="text-sm text-white/60">{description}</p>'}
            </div>
            '''
        
        content = f'''
            {SectionTitle(text='⚠️ 核心风险', icon='⚠️').render()}
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                {risks_html}
            </div>
        '''
        
        return GlassCard(content=content, padding="p-6", extra_class="mb-6").render()
    
    def _generate_strategy(self) -> str:
        """生成投资策略"""
        topic = self.current_topic
        strategy = topic.get('investment_strategy', '')
        if not strategy:
            return ''
        
        if isinstance(strategy, str):
            strategy_text = strategy
        elif isinstance(strategy, dict):
            strategy_text = strategy.get('description', str(strategy))
        else:
            strategy_text = str(strategy)
        
        content = f'''
            {SectionTitle(text='📈 投资策略', icon='📈').render()}
            <div class="p-5 bg-gradient-to-r from-purple-500/10 to-indigo-500/10 border border-purple-500/20 rounded-xl">
                <p class="text-white/80 leading-relaxed">{strategy_text}</p>
            </div>
        '''
        
        return GlassCard(content=content, padding="p-6", extra_class="mb-6").render()
    
    def _content(self) -> str:
        """页面主要内容"""
        toc = self._generate_toc()
        overview = self._generate_topic_overview()
        chain = self._generate_industry_chain()
        stocks = self._generate_target_stocks()
        catalysts = self._generate_catalyst_timeline()
        risks = self._generate_risks()
        strategy = self._generate_strategy()
        
        return f'''
            {toc}
            {overview}
            {chain}
            {stocks}
            {catalysts}
            {risks}
            {strategy}
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
