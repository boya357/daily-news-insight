"""
首页生成器 - Pro版（增强版）
基于Pro组件库重构，深色玻璃态风格
增强：图表可视化、卡片套卡片层次感、市场数据展示
"""
import sys
import os
import json
import random
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from components.pro import GlassCard, SectionTitle
from generators.pro_base import ProGenerator


class HomePageProGenerator(ProGenerator):
    """首页 - Pro版生成器
    
    核心设计原则：
    - 卡片套卡片的层次感
    - 深色玻璃态风格
    - 图表可视化的高级感
    - 统一导航系统
    """
    
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
        # 配置文件路径 - 相对于项目根目录
        # __file__ 在 v3/generators/ 下，向上两级到项目根目录
        project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        config_path = os.path.join(project_root, self.config_dir, 'home_config.json')
        
        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                self.home_config = json.load(f)
        except Exception as e:
            print(f"警告: 加载配置失败 {e}，使用默认配置")
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
        
        # 如果没有真实数据，生成模拟数据用于展示图表效果
        if not self.indices:
            self.indices = self._generate_mock_indices()
            self.market_overview = self._generate_mock_market_overview()
        
        # 从配置获取
        config = self.home_config
        self.hero = config.get('hero', {})
        self.core_features = config.get('core_features', [])
        self.tool_box = config.get('tool_box', [])
        self.report_types = config.get('report_types', [])
        
        # 生成热门板块模拟数据
        self.hot_sectors = self._generate_mock_hot_sectors()
    
    def _generate_mock_indices(self):
        """生成模拟指数数据"""
        return [
            {'name': '上证指数', 'price': '3,186.52', 'change_pct': '+0.85%', 'up': True},
            {'name': '深证成指', 'price': '10,523.18', 'change_pct': '+1.23%', 'up': True},
            {'name': '创业板指', 'price': '2,156.87', 'change_pct': '+1.56%', 'up': True},
            {'name': '科创50', 'price': '912.34', 'change_pct': '-0.32%', 'up': False},
        ]
    
    def _generate_mock_market_overview(self):
        """生成模拟市场概况数据"""
        return {
            'turnover': '9,856亿',
            'up_count': '2,845',
            'down_count': '1,523',
            'limit_up': '45',
            'limit_down': '12',
        }
    
    def _generate_mock_hot_sectors(self):
        """生成模拟热门板块数据"""
        return [
            {'name': 'AI算力', 'change': '+3.25%', 'stocks': 128, 'up_stocks': 98},
            {'name': '人形机器人', 'change': '+2.87%', 'stocks': 56, 'up_stocks': 42},
            {'name': '存储芯片', 'change': '+2.15%', 'stocks': 45, 'up_stocks': 35},
            {'name': '先进封装', 'change': '+1.96%', 'stocks': 38, 'up_stocks': 28},
            {'name': '6G', 'change': '+1.54%', 'stocks': 67, 'up_stocks': 45},
            {'name': '金刚石散热', 'change': '-0.85%', 'stocks': 23, 'up_stocks': 8},
        ]
    
    def _generate_hero(self) -> str:
        """生成头部英雄区域"""
        title = self.hero.get('title', '投资研究中心')
        subtitle = self.hero.get('subtitle', '')
        
        today = datetime.now().strftime('%Y年%m月%d日')
        weekday_map = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
        weekday = weekday_map[datetime.now().weekday()]
        
        return f'''
        <div class="text-center mb-12">
            <h1 class="text-4xl md:text-5xl font-black text-white mb-3 bg-clip-text text-transparent bg-gradient-to-r from-blue-400 via-purple-400 to-pink-400">
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
        """生成核心功能区域 - 卡片套卡片"""
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
                'red': 'from-red-500/30 to-red-600/10 border-red-500/30 hover:border-red-400/50',
                'green': 'from-green-500/30 to-green-600/10 border-green-500/30 hover:border-green-400/50',
                'blue': 'from-blue-500/30 to-blue-600/10 border-blue-500/30 hover:border-blue-400/50',
                'purple': 'from-purple-500/30 to-purple-600/10 border-purple-500/30 hover:border-purple-400/50',
                'yellow': 'from-yellow-500/30 to-yellow-600/10 border-yellow-500/30 hover:border-yellow-400/50',
                'orange': 'from-orange-500/30 to-orange-600/10 border-orange-500/30 hover:border-orange-400/50',
            }
            border_class = color_map.get(color, color_map['blue'])
            
            cards_html += f'''
            <a href="{url}" class="block bg-gradient-to-br {border_class} border rounded-2xl p-6 hover:scale-105 transition-all duration-300 hover:shadow-2xl hover:shadow-purple-500/20">
                <div class="text-4xl mb-4">{icon}</div>
                <h3 class="font-bold text-white text-lg mb-2">{title}</h3>
                <p class="text-white/70 text-sm mb-3">{subtitle}</p>
                <p class="text-white/50 text-xs">{desc}</p>
            </a>
            '''
        
        content = f'''
            <h2 class="text-xl font-bold text-white mb-6 flex items-center">
                <span class="text-blue-400 mr-2">⭐</span>核心功能
            </h2>
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-5">
                {cards_html}
            </div>
        '''
        
        return GlassCard(content=content, padding="p-8", extra_class="mb-8").render()
    
    def _generate_market_overview(self) -> str:
        """生成市场概览区域 - 图表+数据的卡片套卡片"""
        
        # 指数卡片
        indices_html = ''
        for idx in self.indices[:4]:
            name = idx.get('name', '')
            price = idx.get('price', '--')
            change_pct = idx.get('change_pct', '0.00%')
            up = idx.get('up', True)
            color_class = 'text-green-400' if up else 'text-red-400'
            
            # 生成迷你柱状图（用CSS模拟）
            bars_html = ''
            for i in range(8):
                height = random.randint(20, 80)
                bar_color = 'bg-green-400/70' if random.random() > 0.4 else 'bg-red-400/70'
                bars_html += f'<div class="w-1.5 {bar_color} rounded-t" style="height: {height}%"></div>'
            
            indices_html += f'''
            <div class="bg-white/5 hover:bg-white/10 border border-white/10 rounded-xl p-4 transition-all duration-300">
                <div class="text-sm text-white/60 mb-2">{name}</div>
                <div class="text-xl font-bold text-white mb-1">{price}</div>
                <div class="text-sm {color_class} font-semibold mb-3">{change_pct}</div>
                <div class="flex items-end justify-between h-8">
                    {bars_html}
                </div>
            </div>
            '''
        
        # 市场概况数据
        turnover = self.market_overview.get('turnover', '--')
        up_count = self.market_overview.get('up_count', '--')
        down_count = self.market_overview.get('down_count', '--')
        limit_up = self.market_overview.get('limit_up', '--')
        limit_down = self.market_overview.get('limit_down', '--')
        
        overview_stats = f'''
        <div class="grid grid-cols-5 gap-3 mt-6 pt-6 border-t border-white/10">
            <div class="text-center">
                <div class="text-2xl font-bold text-white">{turnover}</div>
                <div class="text-xs text-white/60 mt-1">成交额</div>
            </div>
            <div class="text-center">
                <div class="text-2xl font-bold text-green-400">{up_count}</div>
                <div class="text-xs text-white/60 mt-1">上涨家数</div>
            </div>
            <div class="text-center">
                <div class="text-2xl font-bold text-red-400">{down_count}</div>
                <div class="text-xs text-white/60 mt-1">下跌家数</div>
            </div>
            <div class="text-center">
                <div class="text-2xl font-bold text-yellow-400">{limit_up}</div>
                <div class="text-xs text-white/60 mt-1">涨停</div>
            </div>
            <div class="text-center">
                <div class="text-2xl font-bold text-gray-400">{limit_down}</div>
                <div class="text-xs text-white/60 mt-1">跌停</div>
            </div>
        </div>
        '''
        
        # 涨跌分布饼图（用CSS实现）
        up_pct = 65  # 模拟上涨占比
        pie_chart = f'''
        <div class="relative w-24 h-24 mx-auto">
            <div class="absolute inset-0 rounded-full bg-gradient-to-br from-green-400 to-green-600" 
                 style="clip-path: polygon(50% 50%, 50% 0%, {50 + 50 * (up_pct/100)}% 0%, 100% {100 * (up_pct/100)}%, 50% 100%, 0% 100%, 0% 0%, 50% 0%)"></div>
            <div class="absolute inset-0 rounded-full border-4 border-white/10"></div>
            <div class="absolute inset-3 rounded-full bg-white/5 backdrop-blur-sm flex items-center justify-center">
                <span class="text-lg font-bold text-white">{up_pct}%</span>
            </div>
        </div>
        '''
        
        content = f'''
            <h2 class="text-xl font-bold text-white mb-6 flex items-center">
                <span class="text-green-400 mr-2">📊</span>市场概览
            </h2>
            <div class="grid grid-cols-2 md:grid-cols-4 gap-4 mb-6">
                {indices_html}
            </div>
            {overview_stats}
        '''
        
        # 外层大卡片 - 卡片套卡片
        return GlassCard(content=content, padding="p-8", extra_class="mb-8").render()
    
    def _generate_hot_sectors(self) -> str:
        """生成热门板块区域 - 带进度条的卡片套卡片"""
        if not self.hot_sectors:
            return ''
        
        sectors_html = ''
        for sector in self.hot_sectors:
            name = sector.get('name', '')
            change = sector.get('change', '0.00%')
            stocks = sector.get('stocks', 0)
            up_stocks = sector.get('up_stocks', 0)
            up_ratio = int(up_stocks / stocks * 100) if stocks > 0 else 0
            is_up = change.startswith('+')
            color_class = 'text-green-400' if is_up else 'text-red-400'
            bar_color = 'bg-green-500' if is_up else 'bg-red-500'
            
            sectors_html += f'''
            <div class="bg-white/5 hover:bg-white/10 border border-white/10 rounded-xl p-4 transition-all duration-300">
                <div class="flex items-center justify-between mb-2">
                    <span class="font-semibold text-white text-sm">{name}</span>
                    <span class="text-sm {color_class} font-bold">{change}</span>
                </div>
                <div class="flex items-center text-xs text-white/50 mb-2">
                    <span>{stocks}只成分股</span>
                    <span class="mx-2">·</span>
                    <span>{up_stocks}只上涨</span>
                </div>
                <div class="w-full h-2 bg-white/10 rounded-full overflow-hidden">
                    <div class="h-full {bar_color} rounded-full transition-all duration-500" style="width: {up_ratio}%"></div>
                </div>
            </div>
            '''
        
        content = f'''
            <h2 class="text-xl font-bold text-white mb-6 flex items-center">
                <span class="text-orange-400 mr-2">🔥</span>热门板块
            </h2>
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
                {sectors_html}
            </div>
        '''
        
        return GlassCard(content=content, padding="p-8", extra_class="mb-8").render()
    
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
            <a href="{url}" class="block bg-white/5 hover:bg-white/10 border border-white/10 rounded-xl p-4 text-center transition-all duration-300 hover:scale-105 hover:border-white/20">
                <div class="text-2xl mb-2">{icon}</div>
                <div class="font-medium text-white text-xs">{name}</div>
            </a>
            '''
        
        content = f'''
            <div class="flex items-center justify-between mb-6">
                <h2 class="text-lg font-bold text-white flex items-center">
                    <span class="text-purple-400 mr-2">🛠️</span>系统工具箱
                </h2>
                <span class="text-xs text-white/40">Pro v3.5 架构</span>
            </div>
            <div class="grid grid-cols-3 md:grid-cols-4 lg:grid-cols-6 gap-3">
                {tools_html}
            </div>
        '''
        
        return GlassCard(content=content, padding="p-6", extra_class="mb-8").render()
    
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
            <h2 class="text-lg font-bold text-white mb-4 flex items-center">
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
        <div class="max-w-6xl mx-auto">
            {self._generate_hero()}
            {self._generate_core_features()}
            {self._generate_market_overview()}
            {self._generate_hot_sectors()}
            {self._generate_tool_box()}
            {self._generate_report_entry()}
        </div>
        '''
    
    def publish(self, output_path: str = None) -> dict:
        """发布页面"""
        if output_path is None:
            project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
            output_path = os.path.join(project_root, 'docs', 'index.html')
        
        result = super().publish(output_path)
        return result


if __name__ == "__main__":
    # 测试生成
    generator = HomePageProGenerator()
    result = generator.publish()
    print(f"生成结果: {result}")
