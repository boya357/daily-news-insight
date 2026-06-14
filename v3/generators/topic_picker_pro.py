"""
智能选题助手生成器 - Pro版
基于Pro组件库重构，深色玻璃态风格
"""
import sys
import os
import json
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from components.pro import (
    GlassCard, SectionTitle, TagBadge, 
    RiskBar, DiagnosisItem
)
from generators.pro_base import ProGenerator


class TopicPickerProGenerator(ProGenerator):
    """智能选题助手 - Pro版生成器"""
    
    data_type = "topics"
    
    def __init__(self, data_dir: str = "data"):
        super().__init__(
            title="智能选题助手",
            active_page="产业链",
            footer_text="智能选题 · 发现投资机会",
            data_dir=data_dir,
            show_toc=True,
        )
    def load_data(self):
        """加载选题数据"""
        super().load_data()
        self.data = self.data_loader.get_data("topics")
        self.system_info = self.data.get('system_info', {})
        self.rating_defs = self.data.get('rating_definitions', [])
        self.s_topics = self.data.get('s_level_topics', [])
        self.a_topics = self.data.get('a_level_topics', [])
        self.b_topics = self.data.get('b_level_topics', [])
        self.catalyst_calendar = self.data.get('catalyst_calendar', [])
        self.dimension_config = self.data.get('dimension_config', {})
        self.allocation_strategy = self.data.get('allocation_strategy', {})
    
    def _generate_overview(self) -> str:
        """生成总览区域"""
        info = self.system_info
        total = info.get('total_topics', 0)
        s_count = info.get('s_level_count', 0)
        a_count = info.get('a_level_count', 0)
        b_count = info.get('b_level_count', 0)
        
        content = f'''
            <div class="text-center mb-6">
                <h1 class="text-3xl font-black text-white mb-2">🎯 智能选题助手</h1>
                <p class="text-white/70">多维度量化评级，精准捕捉市场主线</p>
            </div>
            
            <div class="grid grid-cols-2 md:grid-cols-4 gap-4">
                <div class="bg-gradient-to-br from-purple-500/20 to-indigo-500/20 border border-purple-500/30 rounded-2xl p-5 text-center">
                    <div class="text-3xl font-black text-white mb-1">{total}</div>
                    <div class="text-sm text-white/60">总题材数</div>
                </div>
                <div class="bg-gradient-to-br from-red-500/20 to-orange-500/20 border border-red-500/30 rounded-2xl p-5 text-center">
                    <div class="text-3xl font-black text-red-400 mb-1">{s_count}</div>
                    <div class="text-sm text-white/60">S级最强主线</div>
                </div>
                <div class="bg-gradient-to-br from-yellow-500/20 to-amber-500/20 border border-yellow-500/30 rounded-2xl p-5 text-center">
                    <div class="text-3xl font-black text-yellow-400 mb-1">{a_count}</div>
                    <div class="text-sm text-white/60">A级核心题材</div>
                </div>
                <div class="bg-gradient-to-br from-green-500/20 to-emerald-500/20 border border-green-500/30 rounded-2xl p-5 text-center">
                    <div class="text-3xl font-black text-green-400 mb-1">{b_count}</div>
                    <div class="text-sm text-white/60">B级观察题材</div>
                </div>
            </div>
        '''
        
        return GlassCard(content=content, padding="p-8", extra_class="mb-6").render()
    
    def _generate_topic_card(self, topic: dict, is_s: bool = False) -> str:
        """生成单个题材卡片"""
        name = topic.get('name', '')
        level = topic.get('level', '')
        score = topic.get('total_score', 0)
        icon = topic.get('icon', '📊')
        color = topic.get('color', 'purple')
        core_logic = topic.get('core_logic', '')
        leader = topic.get('leader_stock', '')
        mid_cap = topic.get('mid_cap_stock', '')
        flexible = topic.get('flexible_stock', '')
        allocation = topic.get('allocation_suggestion', '')
        recent_catalyst = topic.get('recent_catalyst', '')
        health_score = topic.get('health_score', 0)
        dimension_scores = topic.get('dimension_scores', {})
        link = topic.get('link', '')
        
        # 颜色映射
        color_map = {
            'red': ('from-red-500 to-orange-500', 'text-red-400', 'bg-red-500/20'),
            'orange': ('from-orange-500 to-yellow-500', 'text-orange-400', 'bg-orange-500/20'),
            'yellow': ('from-yellow-500 to-amber-500', 'text-yellow-400', 'bg-yellow-500/20'),
            'green': ('from-green-500 to-emerald-500', 'text-green-400', 'bg-green-500/20'),
            'blue': ('from-blue-500 to-cyan-500', 'text-blue-400', 'bg-blue-500/20'),
            'purple': ('from-purple-500 to-indigo-500', 'text-purple-400', 'bg-purple-500/20'),
        }
        gradient, text_color, bg_color = color_map.get(color, color_map['purple'])
        
        # 维度分数条
        dim_names = self.dimension_config.get('names', {})
        dim_bars = ''
        for dim_key, dim_name in dim_names.items():
            dim_score = dimension_scores.get(dim_key, 0)
            dim_bars += f'''
            <div class="mb-2 last:mb-0">
                <div class="flex justify-between text-xs text-white/60 mb-1">
                    <span>{dim_name}</span>
                    <span>{dim_score}</span>
                </div>
                <div class="w-full h-1.5 bg-white/10 rounded-full overflow-hidden">
                    <div class="h-full bg-gradient-to-r {gradient} rounded-full" style="width: {dim_score}%"></div>
                </div>
            </div>
            '''
        
        # 标的标签
        stocks_html = ''
        if leader:
            stocks_html += f'<span class="px-2 py-1 {bg_color} {text_color} text-xs font-medium rounded-lg">🏆 {leader}</span>'
        if mid_cap:
            stocks_html += f'<span class="px-2 py-1 bg-white/10 text-white/70 text-xs rounded-lg">{mid_cap}</span>'
        if flexible:
            stocks_html += f'<span class="px-2 py-1 bg-white/10 text-white/70 text-xs rounded-lg">{flexible}</span>'
        
        # 健康度
        health_color = 'text-green-400' if health_score >= 70 else ('text-yellow-400' if health_score >= 50 else 'text-red-400')
        
        return f'''
        <div class="bg-white/5 border border-white/10 rounded-2xl p-6 hover:bg-white/10 transition-all hover:scale-[1.02] cursor-pointer" onclick="location.href='../{link}'">
            <div class="flex items-start justify-between mb-4">
                <div class="flex items-center gap-3">
                    <div class="w-12 h-12 bg-gradient-to-br {gradient} rounded-xl flex items-center justify-center text-2xl">
                        {icon}
                    </div>
                    <div>
                        <h3 class="text-white font-bold text-lg">{name}</h3>
                        <div class="flex items-center gap-2 mt-1">
                            <span class="px-2 py-0.5 {bg_color} {text_color} text-xs font-bold rounded-full">
                                {level}级
                            </span>
                            <span class="text-white/40 text-xs">健康度 {health_score}</span>
                        </div>
                    </div>
                </div>
                <div class="text-right">
                    <div class="text-3xl font-black {text_color}">{score}</div>
                    <div class="text-xs text-white/40">综合评分</div>
                </div>
            </div>
            
            <p class="text-sm text-white/70 mb-4 line-clamp-2">{core_logic}</p>
            
            <!-- 维度评分 -->
            <div class="mb-4">
                {dim_bars}
            </div>
            
            <!-- 核心标的 -->
            <div class="flex flex-wrap gap-2 mb-3">
                {stocks_html}
            </div>
            
            <!-- 配置建议 -->
            {allocation and f'''
            <div class="text-xs text-white/50 mb-2">
                💡 配置建议：<span class="text-white/70">{allocation}</span>
            </div>
            '''}
            
            <!-- 近期催化 -->
            {recent_catalyst and f'''
            <div class="p-3 bg-gradient-to-r from-purple-500/10 to-transparent border-l-2 border-purple-400 rounded-r-lg">
                <div class="text-xs text-purple-400 font-medium mb-1">⚡ 近期催化</div>
                <p class="text-xs text-white/70">{recent_catalyst}</p>
            </div>
            
            <!-- 查看报告按钮 -->
            <div class="mt-4 pt-4 border-t border-white/10">
                <div class="flex items-center justify-between">
                    <span class="text-xs text-white/50">查看完整深度报告</span>
                    <span class="text-sm text-white/70 font-medium">→</span>
                </div>
            </div>
            
            '''}
        </div>
        '''
    
    def _generate_topics_section(self, title: str, icon: str, topics: list, is_s: bool = False) -> str:
        """生成题材列表区域"""
        if not topics:
            return ''
        
        cards_html = ''
        for topic in topics:
            cards_html += self._generate_topic_card(topic, is_s=is_s)
        
        content = f'''
            {SectionTitle(text=f'{icon} {title}', icon=icon).render()}
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                {cards_html}
            </div>
        '''
        
        return GlassCard(content=content, padding="p-6", extra_class="mb-6").render()
    
    def _generate_catalyst_calendar(self) -> str:
        """生成催化剂日历"""
        if not self.catalyst_calendar:
            return ''
        
        events_html = ''
        for event in self.catalyst_calendar:
            date = event.get('date', '')
            title = event.get('title', event.get('event', ''))
            impact = event.get('impact', '')
            related = event.get('related_topics', [])
            
            related_html = ''
            for topic in related[:3]:
                related_html += f'<span class="px-2 py-0.5 bg-white/10 text-white/60 text-xs rounded-full">{topic}</span>'
            
            events_html += f'''
            <div class="flex gap-4 p-4 bg-white/5 rounded-xl border border-white/10 mb-3 last:mb-0 hover:bg-white/10 transition-colors">
                <div class="flex-shrink-0 text-center">
                    <div class="text-lg font-bold text-purple-400">{date.split("-")[-1] if "-" in date else date}</div>
                    <div class="text-xs text-white/40">{date.split("-")[1] + "月" if "-" in date else ""}</div>
                </div>
                <div class="flex-1 min-w-0">
                    <h4 class="text-white font-medium mb-1">{title}</h4>
                    <p class="text-xs text-white/50 mb-2">{impact}</p>
                    <div class="flex flex-wrap gap-1">
                        {related_html}
                    </div>
                </div>
            </div>
            '''
        
        content = f'''
            {SectionTitle(text='📅 催化剂日历', icon='📅').render()}
            {events_html}
        '''
        
        return GlassCard(content=content, padding="p-6", extra_class="mb-6").render()
    
    def _generate_allocation_strategy(self) -> str:
        """生成配置策略"""
        if not self.allocation_strategy:
            return ''
        
        strategies = [
            ('offensive', '🔥 进攻型', 'from-red-500/20 to-orange-500/20', 'border-red-500/30'),
            ('trend', '📈 趋势型', 'from-yellow-500/20 to-amber-500/20', 'border-yellow-500/30'),
            ('defensive', '🛡️ 防御型', 'from-green-500/20 to-emerald-500/20', 'border-green-500/30'),
            ('warning', '⚠️ 预警型', 'from-gray-500/20 to-slate-500/20', 'border-gray-500/30'),
        ]
        
        strategy_cards = ''
        for key, title, gradient, border in strategies:
            data = self.allocation_strategy.get(key, {})
            if isinstance(data, str):
                desc = data
                positions = ''
            elif isinstance(data, dict):
                desc = data.get('description', '')
                positions = data.get('position', '')
            else:
                desc = str(data)
                positions = ''
            
            strategy_cards += f'''
            <div class="bg-gradient-to-br {gradient} border {border} rounded-xl p-5">
                <h3 class="text-white font-bold mb-2">{title}</h3>
                <p class="text-sm text-white/70">{desc}</p>
                {positions and f'<div class="mt-2 text-xs text-white/50">建议仓位: {positions}</div>'}
            </div>
            '''
        
        content = f'''
            {SectionTitle(text='💼 配置策略', icon='💼').render()}
            <div class="grid grid-cols-2 md:grid-cols-4 gap-4">
                {strategy_cards}
            </div>
        '''
        
        return GlassCard(content=content, padding="p-6", extra_class="mb-6").render()
    
    def _content(self) -> str:
        """页面主要内容"""
        overview = self._generate_overview()
        s_section = self._generate_topics_section('S级最强主线', '🏆', self.s_topics, is_s=True)
        a_section = self._generate_topics_section('A级核心题材', '⭐', self.a_topics)
        b_section = self._generate_topics_section('B级观察题材', '👀', self.b_topics)
        catalyst_section = self._generate_catalyst_calendar()
        allocation_section = self._generate_allocation_strategy()
        
        return f'''
            {overview}
            {s_section}
            {a_section}
            {b_section}
            {catalyst_section}
            {allocation_section}
        '''
    
    def publish(self, output_path: str = None):
        """发布到生产路径"""
        if output_path is None:
            output_path = "docs/topics/index_pro.html"
        return super().publish(output_path)


if __name__ == '__main__':
    generator = TopicPickerProGenerator()
    html = generator.render()
    
    output_path = '/tmp/test_topic_picker_pro.html'
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"✅ 生成完成")
    print(f"   输出文件: {output_path}")
    print(f"   文件大小: {len(html)} 字节")
    print(f"   S级题材: {len(generator.s_topics)} 个")
    print(f"   A级题材: {len(generator.a_topics)} 个")
    print(f"   B级题材: {len(generator.b_topics)} 个")
