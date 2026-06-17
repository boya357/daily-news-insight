"""
产业链时钟生成器 - Pro版
基于Pro组件库重构，深色玻璃态风格
"""
import sys
import os
import json
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from components.pro import (
    GlassCard, SectionTitle, TagBadge, RiskBar
)
from generators.pro_base import ProGenerator


class IndustryChainClockProGenerator(ProGenerator):
    data_type = "industry_chain"

    """产业链时钟 - Pro版生成器"""
    
    def __init__(self, data_dir: str = "data"):
        super().__init__(
            title="产业链时钟",
            active_page="产业链",
            footer_text="产业链时钟 · 把握产业脉动",
            data_dir=data_dir,
            show_toc=True,
        )

    def load_data(self):
        """加载产业链数据"""
        super().load_data()
        self.data = self.data_loader.get_data("industry_chain")
        self.system_info = self.data.get('system_info', {})
        self.core_chains = self.data.get('core_chains', [])
        self.allocation_strategy = self.data.get('allocation_strategy', {})
    
    def _generate_clock_overview(self) -> str:
        """生成时钟总览区域"""
        # 阶段分布统计
        stages = {1: '萌芽期', 2: '成长期', 3: '成熟期', 4: '衰退期'}
        stage_counts = {1: 0, 2: 0, 3: 0, 4: 0}
        for chain in self.core_chains:
            stage = chain.get('stage', 2)
            if stage in stage_counts:
                stage_counts[stage] += 1
        
        # 阶段颜色
        stage_colors = {
            1: ('#6366f1', '#8b5cf6'),  # 萌芽期 - 紫色
            2: ('#10b981', '#059669'),  # 成长期 - 绿色
            3: ('#f59e0b', '#d97706'),  # 成熟期 - 黄色
            4: ('#ef4444', '#dc2626'),  # 衰退期 - 红色
        }
        
        # 生成阶段标签
        stage_cards = ''
        for stage_id, stage_name in stages.items():
            color1, color2 = stage_colors[stage_id]
            count = stage_counts[stage_id]
            stage_cards += f'''
            <div class="text-center">
                <div class="w-16 h-16 mx-auto rounded-full bg-gradient-to-br" 
                     style="background: linear-gradient(135deg, {color1}, {color2}); opacity: 0.3;">
                    <div class="w-full h-full flex items-center justify-center text-white font-bold text-xl">
                        {count}
                    </div>
                </div>
                <div class="text-sm text-white/70 mt-2">{stage_name}</div>
            </div>
            '''
        
        content = f'''
            <div class="text-center mb-8">
                <h1 class="text-3xl font-black text-white mb-2">⏱️ 产业链时钟</h1>
                <p class="text-white/70">追踪产业周期，把握阶段机遇</p>
            </div>
            
            <div class="flex justify-around items-center mb-6">
                {stage_cards}
            </div>
            
            <!-- 时钟示意图 -->
            <div class="relative w-64 h-64 mx-auto">
                <div class="absolute inset-0 rounded-full border-2 border-white/20"></div>
                <div class="absolute inset-4 rounded-full border border-white/10"></div>
                <div class="absolute inset-0 flex items-center justify-center">
                    <div class="text-center">
                        <div class="text-2xl font-black text-white">{len(self.core_chains)}</div>
                        <div class="text-xs text-white/50">核心产业链</div>
                    </div>
                </div>
            </div>
        '''
        
        return GlassCard(content=content, padding="p-8", extra_class="mb-6").render()
    
    def _generate_chain_card(self, chain: dict) -> str:
        """生成单个产业链卡片"""
        name = chain.get('name', '')
        short_name = chain.get('short_name', '')
        level = chain.get('level', '')
        stage = chain.get('stage', 2)
        stage_name = chain.get('stage_name', '')
        progress = chain.get('progress', 0)
        allocation_ratio = chain.get('allocation_ratio', 0)
        prosperity = chain.get('prosperity', '')
        prosperity_trend = chain.get('prosperity_trend', 'stable')
        leader_stock = chain.get('leader_stock', '')
        leader_change = chain.get('leader_change', '')
        icon = chain.get('icon', '📊')
        core_stocks = chain.get('core_stocks', [])
        stage_features = chain.get('stage_features', [])
        core_logic = chain.get('core_logic', '')
        hot_index = chain.get('hot_index', 0)
        
        # 阶段颜色
        stage_colors = {
            1: ('from-indigo-500 to-purple-500', 'text-indigo-400', 'bg-indigo-500/20', '#8b5cf6'),
            2: ('from-green-500 to-emerald-500', 'text-green-400', 'bg-green-500/20', '#10b981'),
            3: ('from-yellow-500 to-orange-500', 'text-yellow-400', 'bg-yellow-500/20', '#f59e0b'),
            4: ('from-red-500 to-rose-500', 'text-red-400', 'bg-red-500/20', '#ef4444'),
        }
        gradient, text_color, bg_color, accent_color = stage_colors.get(stage, stage_colors[2])
        
        # 景气趋势
        trend_icon = {'up': '📈', 'down': '📉', 'stable': '➡️'}.get(prosperity_trend, '➡️')
        trend_text = {'up': '上升', 'down': '下降', 'stable': '平稳'}.get(prosperity_trend, '平稳')
        
        # 核心标的
        stocks_html = ''
        for stock in core_stocks[:4]:
            stock_name = stock.get('name', '')
            change = stock.get('change', '')
            role = stock.get('role', '')
            is_up = change.startswith('+')
            change_color = 'text-green-400' if is_up else 'text-red-400'
            
            stocks_html += f'''
            <div class="flex items-center justify-between p-2 bg-white/5 rounded-lg">
                <div>
                    <div class="text-white text-sm font-medium">{stock_name}</div>
                    <div class="text-xs text-white/40">{role}</div>
                </div>
                <div class="{change_color} text-sm font-bold">{change}</div>
            </div>
            '''
        
        # 阶段特征
        features_html = ''
        for feature in stage_features[:3]:
            features_html += f'<span class="px-2 py-1 bg-white/10 text-white/60 text-xs rounded-full">{feature}</span>'
        
        return f'''
        <div class="bg-white/5 border border-white/10 rounded-2xl p-6 hover:bg-white/10 transition-all">
            <div class="flex items-start justify-between mb-4">
                <div class="flex items-center gap-3">
                    <div class="w-14 h-14 bg-gradient-to-br {gradient} rounded-xl flex items-center justify-center text-3xl">
                        {icon}
                    </div>
                    <div>
                        <h3 class="text-white font-bold text-lg">{name}</h3>
                        <div class="flex items-center gap-2 mt-1 flex-wrap">
                            <span class="px-2 py-0.5 {bg_color} {text_color} text-xs font-bold rounded-full">
                                {level}级
                            </span>
                            <span class="px-2 py-0.5 bg-white/10 text-white/60 text-xs rounded-full">
                                {stage_name}
                            </span>
                            <span class="text-xs text-white/40">
                                {trend_icon} {prosperity} · {trend_text}
                            </span>
                        </div>
                    </div>
                </div>
            </div>
            
            <!-- 阶段进度条 -->
            <div class="mb-4">
                <div class="flex justify-between text-xs text-white/50 mb-1">
                    <span>阶段进度</span>
                    <span>{progress}%</span>
                </div>
                <div class="w-full h-2 bg-white/10 rounded-full overflow-hidden">
                    <div class="h-full bg-gradient-to-r {gradient} rounded-full" style="width: {progress}%"></div>
                </div>
            </div>
            
            <p class="text-sm text-white/70 mb-4 line-clamp-2">{core_logic}</p>
            
            <!-- 阶段特征 -->
            <div class="flex flex-wrap gap-1 mb-4">
                {features_html}
            </div>
            
            <!-- 核心标的 -->
            <div class="space-y-2">
                <div class="text-xs text-white/50 font-medium">核心标的</div>
                {stocks_html}
            </div>
            
            <!-- 配置比例 -->
            <div class="mt-4 pt-4 border-t border-white/10 flex items-center justify-between">
                <span class="text-sm text-white/60">建议配置</span>
                <span class="text-xl font-bold {text_color}">{allocation_ratio}%</span>
            </div>
        </div>
        '''
    
    def _generate_chains_section(self) -> str:
        """生成产业链列表区域"""
        if not self.core_chains:
            return ''
        
        cards_html = ''
        for chain in self.core_chains:
            cards_html += self._generate_chain_card(chain)
        
        content = f'''
            {SectionTitle(text='🔗 核心产业链', icon='🔗').render()}
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
                {cards_html}
            </div>
        '''
        
        return GlassCard(content=content, padding="p-6", extra_class="mb-6").render()
    
    def _generate_allocation_section(self) -> str:
        """生成配置策略区域"""
        if not self.allocation_strategy:
            return ''
        
        strategies = [
            ('core', '🎯 核心配置', 'from-blue-500/20 to-indigo-500/20', 'border-blue-500/30', 'text-blue-400'),
            ('growth', '📈 成长配置', 'from-green-500/20 to-emerald-500/20', 'border-green-500/30', 'text-green-400'),
            ('theme', '⚡ 主题配置', 'from-purple-500/20 to-pink-500/20', 'border-purple-500/30', 'text-purple-400'),
        ]
        
        strategy_cards = ''
        for key, title, gradient, border, text_color in strategies:
            data = self.allocation_strategy.get(key, {})
            ratio = data.get('ratio', '') if isinstance(data, dict) else ''
            description = data.get('description', '') if isinstance(data, dict) else str(data)
            chains = data.get('chains', []) if isinstance(data, dict) else []
            
            chains_html = ''
            for chain in chains[:3]:
                chains_html += f'<span class="px-2 py-1 bg-white/10 text-white/60 text-xs rounded-full">{chain}</span>'
            
            strategy_cards += f'''
            <div class="bg-gradient-to-br {gradient} border {border} rounded-xl p-5">
                <div class="flex items-center justify-between mb-3">
                    <h3 class="text-white font-bold">{title}</h3>
                    {ratio and f'<span class="text-2xl font-black {text_color}">{ratio}</span>'}
                </div>
                <p class="text-sm text-white/70 mb-3">{description}</p>
                <div class="flex flex-wrap gap-1">
                    {chains_html}
                </div>
            </div>
            '''
        
        content = f'''
            {SectionTitle(text='💼 配置策略', icon='💼').render()}
            <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
                {strategy_cards}
            </div>
        '''
        
        return GlassCard(content=content, padding="p-6", extra_class="mb-6").render()
    
    def _content(self) -> str:
        """页面主要内容"""
        overview = self._generate_clock_overview()
        chains_section = self._generate_chains_section()
        allocation_section = self._generate_allocation_section()
        
        return f'''
            {overview}
            {chains_section}
            {allocation_section}
        '''
    
    def publish(self, output_path: str = "docs/industry-chain-clock/index.html"):
        """发布到生产路径"""
        return super().publish(output_path)


if __name__ == '__main__':
    generator = IndustryChainClockProGenerator()
    html = generator.render()
    
    output_path = '/tmp/test_industry_chain_pro.html'
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"✅ 生成完成")
    print(f"   输出文件: {output_path}")
    print(f"   文件大小: {len(html)} 字节")
    print(f"   核心产业链: {len(generator.core_chains)} 个")
