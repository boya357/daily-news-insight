"""
首页生成器 - Pro版
基于Pro组件库重构，深色玻璃态风格
投资研究中心首页
"""
import sys
import os
import json
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from components.pro import GlassCard, SectionTitle
from generators.pro_base import ProGenerator


class HomePageProGenerator(ProGenerator):
    """首页 - Pro版生成器"""
    
    data_type = "home"
    
    def __init__(self, data_dir: str = "data", config_dir: str = "config"):
        super().__init__(
            title="投资研究中心",
            active_page="首页",
            footer_text="投资研究中心 · 数据驱动决策",
            data_dir=data_dir,
            show_toc=False,
        )
        self.config_dir = config_dir
        self._load_config()
    
    def _load_config(self):
        """加载首页配置"""
        # 配置文件路径
        config_path = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            '..', '..', self.config_dir, 'home_config.json'
        )
        config_path = os.path.abspath(config_path)
        
        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                self.home_config = json.load(f)
        except:
            # 默认配置
            self.home_config = {
                'hero': {'title': '投资研究中心', 'subtitle': '数据驱动 · 智能分析 · 科学决策'},
                'core_features': [],
                'tool_box': [],
                'report_types': [],
            }
    
    def load_data(self):
        """加载首页数据"""
        super().load_data()
        
        # 加载市场数据
        try:
            self.market_data = self.data_loader.get_data("market") or {}
        except:
            self.market_data = {}
        
        self.indices = self.market_data.get('indices', [])
        self.market_overview = self.market_data.get('market_data', {})
        
        # 从配置获取
        config = self.home_config
        self.hero = config.get('hero', {})
        self.core_features = config.get('core_features', [])
        self.tool_box = config.get('tool_box', [])
        self.report_types = config.get('report_types', [])
    
    def _generate_hero(self) -> str:
        """生成头部英雄区域"""
        title = self.hero.get('title', '投资研究中心')
        subtitle = self.hero.get('subtitle', '')
        
        today = datetime.now().strftime('%Y年%m月%d日')
        weekday_map = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
        weekday = weekday_map[datetime.now().weekday()]
        
        return f'''
        <div class="text-center mb-10">
            <h1 class="text-4xl md:text-5xl font-black text-white mb-3">
                {title}
            </h1>
            <p class="text-white/70 text-lg mb-2">
                {subtitle}
            </p>
            <p class="text-white/50 text-sm">
                {today} {weekday}
            </p>
        </div>
        '''
    
    def _generate_core_features(self) -> str:
        """生成核心功能区域"""
        if not self.core_features:
            return ''
        
        cards_html = ''
        for feature in self.core_features:
            title = feature.get('title', '')
            subtitle = feature.get('subtitle', '')
            icon = feature.get('icon', '')
            url = feature.get('url', '#')
            color = feature.get('color', 'blue')
            desc = feature.get('desc', '')
            
            color_map = {
                'red': 'from-red-500/20 to-transparent border-red-500/30',
                'green': 'from-green-500/20 to-transparent border-green-500/30',
                'blue': 'from-blue-500/20 to-transparent border-blue-500/30',
                'purple': 'from-purple-500/20 to-transparent border-purple-500/30',
                'yellow': 'from-yellow-500/20 to-transparent border-yellow-500/30',
                'orange': 'from-orange-500/20 to-transparent border-orange-500/30',
            }
            border_class = color_map.get(color, color_map['blue'])
            
            cards_html += f'''
            <a href="{url}" class="block bg-gradient-to-br {border_class} border rounded-2xl p-6 hover:scale-105 transition-all duration-300 hover:shadow-xl">
                <div class="text-3xl mb-3">{icon}</div>
                <h3 class="font-bold text-white text-lg mb-1">{title}</h3>
                <p class="text-white/70 text-sm mb-3">{subtitle}</p>
                <p class="text-white/50 text-xs">{desc}</p>
            </a>
            '''
        
        content = f'''
            <div class="flex items-center justify-between mb-5">
                <h2 class="text-lg font-bold text-white">
                <span class="text-blue-400 mr-2">⭐</span>核心功能
            </h2>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
                {cards_html}
            </div>
        '''
        
        return GlassCard(content=content, padding="p-6", extra_class="mb-6").render()
    
    def _generate_market_overview(self) -> str:
        """生成市场概览区域"""
        if not self.indices:
            # 默认数据
            indices_html = '''
                <div class="bg-white/5 rounded-xl p-4 text-center">
                    <div class="text-sm text-white/60 mb-1">上证指数</div>
                    <div class="text-xl font-bold text-white">--</div>
                    <div class="text-sm text-white/50">--</div>
                </div>
                <div class="bg-white/5 rounded-xl p-4 text-center">
                    <div class="text-sm text-white/60 mb-1">深证成指</div>
                    <div class="text-xl font-bold text-white">--</div>
                    <div class="text-sm text-white/50">--</div>
                </div>
                <div class="bg-white/5 rounded-xl p-4 text-center">
                    <div class="text-sm text-white/60 mb-1">创业板指</div>
                    <div class="text-xl font-bold text-white">--</div>
                    <div class="text-sm text-white/50">--</div>
                </div>
                <div class="bg-white/5 rounded-xl p-4 text-center">
                    <div class="text-sm text-white/60 mb-1">科创50</div>
                    <div class="text-xl font-bold text-white">--</div>
                    <div class="text-sm text-white/50">--</div>
                </div>
            '''
        else:
            indices_html = ''
            for idx in self.indices[:4]:
                name = idx.get('name', '')
                price = idx.get('price', '--')
                change_pct = idx.get('change_pct', 0)
                up = idx.get('up', True)
                color_class = 'text-green-400' if up else 'text-red-400'
                sign = '+' if up and change_pct >= 0 else ''
                
                indices_html += f'''
                <div class="bg-white/5 rounded-xl p-4 text-center">
                    <div class="text-sm text-white/60 mb-1">{name}</div>
                    <div class="text-xl font-bold text-white mb-1">{price}</div>
                    <div class="text-sm {color_class} font-semibold">
                        {sign}{change_pct}%
                    </div>
                </div>
                '''
        
        # 市场概况数据
        turnover = self.market_overview.get('turnover', '--')
        up_count = self.market_overview.get('up_count', '--')
        down_count = self.market_overview.get('down_count', '--')
        
        overview_html = f'''
        <div class="grid grid-cols-3 gap-4 mt-6 pt-6 border-t border-white/10">
            <div class="text-center">
                <div class="text-2xl font-bold text-white">{turnover}</div>
                <div class="text-sm text-white/60 mt-1">成交额</div>
            </div>
            <div class="text-center">
                <div class="text-2xl font-bold text-green-400">{up_count}</div>
                <div class="text-sm text-white/60 mt-1">上涨家数</div>
            </div>
            <div class="text-center">
                <div class="text-2xl font-bold text-red-400">{down_count}</div>
                <div class="text-sm text-white/60 mt-1">下跌家数</div>
            </div>
        </div>
        '''
        
        content = f'''
            <h2 class="text-lg font-bold text-white mb-4">
                <span class="text-blue-400 mr-2">📊</span>市场概览
            </h2>
            <div class="grid grid-cols-2 md:grid-cols-4 gap-3">
                {indices_html}
            </div>
            {overview_html}
        '''
        
        return GlassCard(content=content, padding="p-6", extra_class="mb-6").render()
    
    def _generate_tool_box(self) -> str:
        """生成系统工具箱区域"""
        if not self.tool_box:
            return ''
        
        tools_html = ''
        for tool in self.tool_box:
            name = tool.get('name', '')
            icon = tool.get('icon', '')
            url = tool.get('url', '#')
            
            tools_html += f'''
            <a href="{url}" class="block bg-white/5 hover:bg-white/10 border border-white/10 rounded-xl p-4 text-center transition-all duration-300 hover:scale-105">
                <div class="text-2xl mb-2">{icon}</div>
                <div class="font-semibold text-white text-sm">{name}</div>
            </a>
            '''
        
        content = f'''
            <div class="flex items-center justify-between mb-5">
                <h2 class="text-base font-bold text-white">
                    <span class="text-purple-400 mr-2">🛠️</span>系统工具箱
                </h2>
                <span class="text-xs text-white/40">Pro v3.0 架构</span>
            </div>
            <div class="grid grid-cols-3 md:grid-cols-4 gap-3">
                {tools_html}
            </div>
        '''
        
        return GlassCard(content=content, padding="p-6", extra_class="mb-6").render()
    
    def _generate_report_entry(self) -> str:
        """生成报告快捷入口区域"""
        if not self.report_types:
            return ''
        
        reports_html = ''
        for report in self.report_types:
            name = report.get('name', '')
            icon = report.get('icon', '')
            url = report.get('url', '#')
            
            reports_html += f'''
            <a href="{url}" class="block bg-white/5 hover:bg-white/10 border border-white/10 rounded-xl p-3 text-center transition-all duration-300 hover:scale-105">
                <div class="text-xl mb-1">{icon}</div>
                <div class="font-medium text-white text-xs">{name}</div>
            </a>
            '''
        
        content = f'''
            <h2 class="text-base font-bold text-white mb-4">
                <span class="text-indigo-400 mr-2">📁</span>报告类型快速导航
            </h2>
            <div class="grid grid-cols-5 gap-2">
                {reports_html}
            </div>
        '''
        
        return GlassCard(content=content, padding="p-6").render()
    
    def _content(self) -> str:
        """页面主要内容"""
        return f'''
        <div class="max-w-5xl mx-auto">
            {self._generate_hero()}
            {self._generate_core_features()}
            {self._generate_market_overview()}
            {self._generate_tool_box()}
            {self._generate_report_entry()}
        </div>
        '''
    
    def publish(self, output_path: str) -> dict:
        """发布页面"""
        result = super().publish(output_path)
        return result


if __name__ == "__main__":
    # 测试生成
    generator = HomePageProGenerator()
    result = generator.publish('../../docs/index_pro.html')
    print(f"生成结果: {result}")
