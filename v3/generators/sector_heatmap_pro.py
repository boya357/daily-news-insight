"""
板块热力图生成器 - Pro版
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


class SectorHeatmapProGenerator(ProGenerator):
    """板块热力图 - Pro版生成器"""
    
    data_type = "market"
    
    def __init__(self, data_dir: str = "data"):
        super().__init__(
            title="板块热力图",
            active_page="日报",
            footer_text="板块热力图 · 洞察市场热点轮动",
            data_dir=data_dir,
            show_toc=True,
        )
    
    def load_data(self):
        """加载市场数据"""
        super().load_data()
        self.data = self.data_loader.get_data('market')
        self.indices = self.data.get('indices', [])
        self.market_data = self.data.get('market_data', {})
        self.sentiment = self.data.get('sentiment', {})
        self.sectors_hot = self.data.get('sectors_hot', [])
        self.sectors_cold = self.data.get('sectors_cold', [])
    
    def _generate_market_overview(self) -> str:
        """生成市场总览区域"""
        # 指数卡片
        indices_html = ''
        for idx in self.indices:
            name = idx.get('name', '')
            price = idx.get('price', '')
            change = idx.get('change_pct', '')
            is_up = idx.get('up', True)
            color = 'text-green-400' if is_up else 'text-red-400'
            arrow = '↑' if is_up else '↓'
            
            indices_html += f'''
            <div class="bg-white/5 border border-white/10 rounded-xl p-4 text-center">
                <div class="text-white/60 text-sm mb-1">{name}</div>
                <div class="text-xl font-bold text-white mb-1">{price}</div>
                <div class="{color} font-medium">{arrow} {change}</div>
            </div>
            '''
        
        # 市场数据
        md = self.market_data
        turnover = md.get('turnover', '')
        up_count = md.get('up_count', 0)
        down_count = md.get('down_count', 0)
        limit_up = md.get('limit_up_count', 0)
        limit_down = md.get('limit_down_count', 0)
        
        # 情绪指标
        sentiment = self.sentiment
        fear_greed = sentiment.get('fear_greed', 50)
        ad_ratio = sentiment.get('advance_decline_ratio', 1.0)
        
        # 情绪颜色
        if fear_greed >= 70:
            fg_color = 'text-green-400'
            fg_text = '贪婪'
        elif fear_greed >= 50:
            fg_color = 'text-yellow-400'
            fg_text = '中性'
        elif fear_greed >= 30:
            fg_color = 'text-orange-400'
            fg_text = '恐惧'
        else:
            fg_color = 'text-red-400'
            fg_text = '极度恐惧'
        
        content = f'''
            {SectionTitle(text='📊 市场概览', icon='📊').render()}
            
            <!-- 主要指数 -->
            <div class="grid grid-cols-2 md:grid-cols-4 gap-3 mb-6">
                {indices_html}
            </div>
            
            <!-- 市场数据 -->
            <div class="grid grid-cols-3 gap-4 mb-6">
                <div class="text-center p-4 bg-white/5 rounded-xl">
                    <div class="text-2xl font-bold text-white">{turnover}</div>
                    <div class="text-sm text-white/50 mt-1">成交额</div>
                </div>
                <div class="text-center p-4 bg-white/5 rounded-xl">
                    <div class="text-2xl font-bold text-green-400">{up_count}</div>
                    <div class="text-sm text-white/50 mt-1">上涨家数</div>
                </div>
                <div class="text-center p-4 bg-white/5 rounded-xl">
                    <div class="text-2xl font-bold text-red-400">{down_count}</div>
                    <div class="text-sm text-white/50 mt-1">下跌家数</div>
                </div>
            </div>
            
            <!-- 涨跌停 -->
            <div class="grid grid-cols-2 gap-4 mb-6">
                <div class="text-center p-4 bg-gradient-to-br from-red-500/20 to-orange-500/20 border border-red-500/30 rounded-xl">
                    <div class="text-3xl font-black text-red-400">{limit_up}</div>
                    <div class="text-sm text-white/60 mt-1">涨停板</div>
                </div>
                <div class="text-center p-4 bg-gradient-to-br from-green-500/20 to-emerald-500/20 border border-green-500/30 rounded-xl">
                    <div class="text-3xl font-black text-green-400">{limit_down}</div>
                    <div class="text-sm text-white/60 mt-1">跌停板</div>
                </div>
            </div>
            
            <!-- 情绪指标 -->
            <div class="bg-white/5 rounded-xl p-5">
                <div class="flex items-center justify-between mb-3">
                    <span class="text-white/70">恐惧贪婪指数</span>
                    <span class="{fg_color} font-bold">{fear_greed} · {fg_text}</span>
                </div>
                <div class="w-full h-3 bg-gradient-to-r from-red-500 via-yellow-500 to-green-500 rounded-full relative">
                    <div class="absolute top-1/2 -translate-y-1/2 w-4 h-4 bg-white rounded-full shadow-lg" 
                         style="left: {fear_greed}%; transform: translateX(-50%) translateY(-50%);"></div>
                </div>
                <div class="flex justify-between text-xs text-white/40 mt-1">
                    <span>极度恐惧</span>
                    <span>中性</span>
                    <span>极度贪婪</span>
                </div>
                
                <div class="mt-4 pt-4 border-t border-white/10 flex justify-between">
                    <span class="text-white/60">涨跌比</span>
                    <span class="text-white font-medium">{ad_ratio}</span>
                </div>
            </div>
        '''
        
        return GlassCard(content=content, padding="p-6", extra_class="mb-6").render()
    
    def _generate_sector_heatmap(self, sectors: list, is_hot: bool = True) -> str:
        """生成板块热力图格子"""
        if not sectors:
            return ''
        
        # 找出最大涨幅用于计算颜色深度
        max_change = max([abs(s.get('change_pct', 0)) for s in sectors]) if sectors else 5
        
        cells_html = ''
        for sector in sectors:
            name = sector.get('name', '')
            change_pct = sector.get('change_pct', 0)
            leader = sector.get('leader', '')
            reason = sector.get('reason', '')
            fund_flow = sector.get('fund_flow', '')
            
            is_up = change_pct >= 0
            change_abs = abs(change_pct)
            
            # 计算颜色深度
            intensity = min(change_abs / max_change * 0.8 + 0.2, 1) if max_change > 0 else 0.3
            
            if is_up:
                bg_color = f'rgba(239, 68, 68, {intensity})'
                text_color = 'text-red-200'
            else:
                bg_color = f'rgba(16, 185, 129, {intensity})'
                text_color = 'text-green-200'
            
            cells_html += f'''
            <div class="relative p-4 rounded-xl transition-all hover:scale-105 cursor-pointer"
                 style="background: {bg_color};">
                <div class="text-white font-bold text-lg mb-1">{name}</div>
                <div class="{text_color} font-bold text-xl">{"+" if is_up else ""}{change_pct}%</div>
                <div class="text-white/70 text-xs mt-2">
                    龙头: {leader}
                </div>
                {reason and f'<div class="text-white/50 text-xs mt-1 line-clamp-2">{reason}</div>'}
                {fund_flow and f'<div class="text-white/60 text-xs mt-1">资金: {fund_flow}</div>'}
            </div>
            '''
        
        return cells_html
    
    def _generate_hot_sectors(self) -> str:
        """生成热门板块区域"""
        if not self.sectors_hot:
            return ''
        
        cells = self._generate_sector_heatmap(self.sectors_hot, is_hot=True)
        
        content = f'''
            {SectionTitle(text='🔥 热门板块', icon='🔥').render()}
            <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-5 gap-3">
                {cells}
            </div>
        '''
        
        return GlassCard(content=content, padding="p-6", extra_class="mb-6").render()
    
    def _generate_cold_sectors(self) -> str:
        """生成冷门板块区域"""
        if not self.sectors_cold:
            return ''
        
        cells = self._generate_sector_heatmap(self.sectors_cold, is_hot=False)
        
        content = f'''
            {SectionTitle(text='🧊 弱势板块', icon='🧊').render()}
            <div class="grid grid-cols-2 md:grid-cols-3 gap-3">
                {cells}
            </div>
        '''
        
        return GlassCard(content=content, padding="p-6", extra_class="mb-6").render()
    
    def _content(self) -> str:
        """页面主要内容"""
        overview = self._generate_market_overview()
        hot_sectors = self._generate_hot_sectors()
        cold_sectors = self._generate_cold_sectors()
        
        return f'''
            {overview}
            {hot_sectors}
            {cold_sectors}
        '''
    
    def publish(self, output_path: str = "docs/sector_heatmap/index_pro.html"):
        """发布到生产路径"""
        return super().publish(output_path)


if __name__ == '__main__':
    generator = SectorHeatmapProGenerator()
    html = generator.render()
    
    output_path = '/tmp/test_sector_heatmap_pro.html'
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"✅ 生成完成")
    print(f"   输出文件: {output_path}")
    print(f"   文件大小: {len(html)} 字节")
    print(f"   热门板块: {len(generator.sectors_hot)} 个")
    print(f"   弱势板块: {len(generator.sectors_cold)} 个")
