"""
首页生成器 - Pro版（增强版）
基于Pro组件库重构，深色玻璃态风格
数据层：使用统一DataLoader获取真实市场数据
"""
import sys
import os
import json
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
    - 数据全部来自统一数据层
    """
    
    data_type = "market"
    
    def __init__(self, data_dir: str = "data", config_dir: str = "config"):
        super().__init__(
            title="首页",
            active_page="首页",
            footer_text="投资研究中心 · 数据驱动决策",
            data_dir=data_dir,
            show_toc=False,
        )
        self.config_dir = config_dir
        self._load_config()
    
    def _load_config(self):
        """加载首页配置"""
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
        """加载首页数据 - 全部来自统一数据层"""
        super().load_data()
        
        # 从DataLoader获取真实市场数据
        self.indices = self.data_loader.get_indices()
        self.market_overview = self.data_loader.get_market_data()
        self.hot_sectors = self.data_loader.get_hot_sectors(limit=6)
        self.market_sentiment = self.data_loader.get_market_sentiment()
        
        # 从配置获取静态内容
        config = self.home_config
        self.hero = config.get('hero', {})
        self.core_features = config.get('core_features', [])
        self.tool_box = config.get('tool_box', [])
        self.report_types = config.get('report_types', [])
    
    def _generate_hero(self) -> str:
        """生成头部英雄区域"""
        title = self.hero.get('title', '投资研究中心')
        subtitle = self.hero.get('subtitle', '')
        
        # 获取市场情绪作为副标题补充
        sentiment_text = self.market_sentiment.get('fear_greed_text', '')
        sentiment_value = self.market_sentiment.get('fear_greed', '')
        if sentiment_text:
            subtitle = f"{subtitle} · {sentiment_text} {sentiment_value}"
        
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
        
        # 指数卡片 - 带迷你走势图
        indices_html = ''
        for idx in self.indices[:4]:
            name = idx.get('name', '')
            price_val = idx.get('current_price', idx.get('price', 0))
            change_pct = idx.get('change_percent', idx.get('change_pct', 0))
            up = idx.get('up', change_pct >= 0)
            
            # 格式化价格（保留2位小数）
            if isinstance(price_val, (int, float)):
                price = f"{price_val:.2f}"
            else:
                price = str(price_val)
            
            # 格式化涨跌幅（小数转百分比，保留2位）
            if isinstance(change_pct, (int, float)):
                change_str = f"{'+' if change_pct >= 0 else ''}{change_pct*100:.2f}%"
            else:
                change_str = str(change_pct)
                up = '+' in change_str
            
            color_class = 'text-green-400' if up else 'text-red-400'
            
            # 生成迷你柱状图（模拟8个时间点）
            bars_html = ''
            for i in range(8):
                height = 30 + (i * 7 + hash(name) % 15) % 60
                bar_color = 'bg-green-400/70' if (i + hash(name) % 2) % 2 == 0 else 'bg-red-400/70'
                if not up:
                    bar_color = 'bg-red-400/70' if bar_color == 'bg-green-400/70' else 'bg-green-400/70'
                bars_html += f'<div class="w-1.5 {bar_color} rounded-t" style="height: {height}%"></div>'
            
            indices_html += f'''
            <div class="bg-white/5 hover:bg-white/10 border border-white/10 rounded-xl p-4 transition-all duration-300">
                <div class="text-sm text-white/60 mb-2">{name}</div>
                <div class="text-xl font-bold text-white mb-1">{price}</div>
                <div class="text-sm {color_class} font-semibold mb-3">{change_str}</div>
                <div class="flex items-end justify-between h-8">
                    {bars_html}
                </div>
            </div>
            '''
        
        # 市场概况数据
        turnover = self.market_overview.get('total_turnover', self.market_overview.get('turnover', '--'))
        up_count = self.market_overview.get('up_count', '--')
        down_count = self.market_overview.get('down_count', '--')
        limit_up = self.market_overview.get('limit_up_count', self.market_overview.get('limit_up', '--'))
        limit_down = self.market_overview.get('limit_down_count', self.market_overview.get('limit_down', '--'))
        
        overview_stats = f'''
        <div class="grid grid-cols-5 gap-3 mt-6 pt-6 border-t border-white/10">
            <div class="text-center">
                <div class="text-xl md:text-2xl font-bold text-white">{turnover}</div>
                <div class="text-xs text-white/60 mt-1">成交额</div>
            </div>
            <div class="text-center">
                <div class="text-xl md:text-2xl font-bold text-green-400">{up_count}</div>
                <div class="text-xs text-white/60 mt-1">上涨家数</div>
            </div>
            <div class="text-center">
                <div class="text-xl md:text-2xl font-bold text-red-400">{down_count}</div>
                <div class="text-xs text-white/60 mt-1">下跌家数</div>
            </div>
            <div class="text-center">
                <div class="text-xl md:text-2xl font-bold text-yellow-400">{limit_up}</div>
                <div class="text-xs text-white/60 mt-1">涨停</div>
            </div>
            <div class="text-center">
                <div class="text-xl md:text-2xl font-bold text-gray-400">{limit_down}</div>
                <div class="text-xs text-white/60 mt-1">跌停</div>
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
        
        return GlassCard(content=content, padding="p-8", extra_class="mb-8").render()
    
    def _generate_hot_sectors(self) -> str:
        """生成热门板块区域 - 带进度条的卡片套卡片"""
        if not self.hot_sectors:
            return ''
        
        sectors_html = ''
        for sector in self.hot_sectors:
            name = sector.get('name', '')
            change_pct = sector.get('change', sector.get('change_pct', 0))
            up = sector.get('up', change_pct >= 0 if isinstance(change_pct, (int, float)) else True)
            leader = sector.get('leader', '')
            fund_flow = sector.get('fund_flow', '')
            
            # 确保change_pct是数值类型
            if isinstance(change_pct, str):
                # 尝试从字符串转换
                try:
                    change_pct = float(change_pct.replace('%', '').replace('+', ''))
                    if up is None:
                        up = change_pct >= 0
                except:
                    change_pct = 0
            
            # 计算进度条百分比（基于涨跌幅映射到20-100%）
            if isinstance(change_pct, (int, float)):
                # 涨跌幅是小数形式，转成百分比后计算进度
                pct_value = abs(change_pct) * 100 if abs(change_pct) < 1 else abs(change_pct)
                progress = min(100, max(20, pct_value * 15 + 30))
                # 格式化显示
                if abs(change_pct) < 1:  # 小数形式
                    change_str = f"{'+' if change_pct >= 0 else ''}{change_pct*100:.2f}%"
                else:  # 已经是百分比数值
                    change_str = f"{'+' if change_pct >= 0 else ''}{change_pct:.2f}%"
            else:
                progress = 50
                change_str = str(change_pct)
            
            color_class = 'text-green-400' if up else 'text-red-400'
            bar_color = 'bg-green-500' if up else 'bg-red-500'
            
            sectors_html += f'''
            <div class="bg-white/5 hover:bg-white/10 border border-white/10 rounded-xl p-4 transition-all duration-300">
                <div class="flex items-center justify-between mb-2">
                    <span class="font-semibold text-white text-sm">{name}</span>
                    <span class="text-sm {color_class} font-bold">{change_str}</span>
                </div>
                <div class="flex items-center text-xs text-white/50 mb-3">
                    <span>龙头: {leader}</span>
                </div>
                <div class="w-full h-2 bg-white/10 rounded-full overflow-hidden">
                    <div class="h-full {bar_color} rounded-full transition-all duration-500" style="width: {progress}%"></div>
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
    generator = HomePageProGenerator()
    result = generator.publish()
    print(f"生成结果: {result}")
