"""
预判验证中心生成器 - Pro版
基于Pro组件库重构，深色玻璃态风格
"""
import sys
import os
import json
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from components.pro import (
    get_pro_theme_css, GlassCard, SectionTitle, TagBadge, 
    RiskBar, DiagnosisItem, FundRow, LhbCard, AlertSection
)
from generators.pro_base import ProGenerator


class PredictionCenterProGenerator(ProGenerator):
    data_type = "predictions"
    
    """预判验证中心 - Pro版生成器"""
    
    def __init__(self, data_dir: str = "data"):
        super().__init__(
            title="PredictionCenter",
            active_page="首页",
            footer_text="",
            data_dir=data_dir,
            show_toc=True,
        )
    def load_data(self):
        """加载预判数据"""
        super().load_data()
        self.data = self.data_loader.get_data("predictions")
        self.system_info = self.data.get('system_info', {})
        self.pending = self.data.get('pending_predictions', [])
        self.history = self.data.get('history_records', [])
        self.trends = self.data.get('accuracy_trends', {})
        self.progress = self.data.get('analyst_progress', {})
    
    def _generate_hero_section(self) -> str:
        """生成英雄区 - 大数字+统计卡片"""
        info = self.system_info
        accuracy = info.get('accuracy', '0%')
        level = info.get('analyst_level', 'C')
        total = info.get('total_predictions', 0)
        correct = info.get('correct_count', 0)
        wrong = info.get('wrong_count', 0)
        pending = info.get('pending_count', 0)
        streak = info.get('streak', 0)
        
        # 等级颜色
        level_colors = {
            'S': ('#8b5cf6', '#c026d3'),
            'A': ('#3b82f6', '#8b5cf6'),
            'B': ('#10b981', '#059669'),
            'C': ('#f59e0b', '#d97706'),
            'D': ('#ef4444', '#dc2626'),
        }
        color1, color2 = level_colors.get(level, level_colors['C'])
        
        # 统计卡片
        stats = [
            ('📊', '总预判', f'{total}次', 'from-blue-500/20 to-indigo-500/20'),
            ('✅', '正确', f'{correct}次', 'from-green-500/20 to-emerald-500/20'),
            ('❌', '错误', f'{wrong}次', 'from-red-500/20 to-orange-500/20'),
            ('⏳', '待验证', f'{pending}次', 'from-yellow-500/20 to-amber-500/20'),
            ('🔥', '连续正确', f'{streak}次', 'from-purple-500/20 to-violet-500/20'),
        ]
        
        stats_html = ''
        for icon, label, value, gradient in stats:
            stats_html += f'''
            <div class="p-4 bg-gradient-to-br {gradient} border border-white/10 rounded-2xl text-center">
                <div class="text-2xl mb-1">{icon}</div>
                <div class="text-sm text-white/70 mb-1">{label}</div>
                <div class="text-2xl font-black text-white">{value}</div>
            </div>
            '''
        
        content = f'''
            <div class="text-center mb-8">
                <div class="text-sm text-white/60 mb-3 font-medium">📊 综合预判准确率</div>
                <div class="text-6xl font-black text-white mb-4" style="text-shadow: 0 0 40px rgba(139, 92, 246, 0.5);">
                    {accuracy}
                </div>
                <div class="inline-block px-6 py-2 bg-gradient-to-r from-indigo-500 to-purple-600 text-white rounded-full text-lg font-bold shadow-lg">
                    🏆 {level}级分析师
                </div>
            </div>
            
            <div class="grid grid-cols-5 gap-4">
                {stats_html}
            </div>
        '''
        
        return GlassCard(content=content, padding="p-8", extra_class="mb-6").render()
    
    def _generate_pending_section(self) -> str:
        """生成待验证预判区域"""
        if not self.pending:
            content = '<p class="text-white/60 text-center py-8">暂无待验证预判</p>'
            return GlassCard(content=content, padding="p-6", extra_class="mb-6").render()
        
        pending_cards = ''
        for pred in self.pending:
            title = pred.get('title', '')
            level = pred.get('level', 'B')
            cycle = pred.get('verify_cycle', '')
            progress = pred.get('progress', 0)
            latest = pred.get('latest_observation', {})
            latest_date = latest.get('date', '')
            latest_content = latest.get('content', '')
            
            # 等级标签颜色
            level_colors = {
                'S': 'bg-purple-500',
                'A': 'bg-blue-500',
                'B': 'bg-green-500',
                'C': 'bg-yellow-500',
                'D': 'bg-red-500',
            }
            level_color = level_colors.get(level, 'bg-gray-500')
            
            pending_cards += f'''
            <div class="bg-white/5 border border-white/10 rounded-xl p-5 mb-4 last:mb-0">
                <div class="flex items-start justify-between mb-3">
                    <h3 class="text-white font-bold text-lg flex-1">{title}</h3>
                    <span class="px-3 py-1 {level_color} text-white text-xs font-bold rounded-full ml-3 flex-shrink-0">
                        {level}级 · {cycle}
                    </span>
                </div>
                
                <div class="mb-3">
                    <div class="flex justify-between text-sm text-white/60 mb-1">
                        <span>验证进度</span>
                        <span>{progress}%</span>
                    </div>
                    <div class="w-full h-2 bg-white/10 rounded-full overflow-hidden">
                        <div class="h-full bg-gradient-to-r from-yellow-400 to-orange-500 rounded-full transition-all" style="width: {progress}%"></div>
                    </div>
                </div>
                
                {latest_content and f'''
                <div class="bg-white/5 rounded-lg p-3 border-l-4 border-yellow-400">
                    <div class="text-xs text-yellow-400 font-medium mb-1">📅 {latest_date} 最新观察</div>
                    <p class="text-sm text-white/80">{latest_content}</p>
                </div>
                '''}
            </div>
            '''
        
        content = f'''
            {SectionTitle(text='⏳ 待验证预判', icon='⏳').render()}
            {pending_cards}
        '''
        
        return GlassCard(content=content, padding="p-6", extra_class="mb-6").render()
    
    def _generate_history_section(self) -> str:
        """生成历史记录区域"""
        if not self.history:
            content = '<p class="text-white/60 text-center py-8">暂无历史记录</p>'
            return GlassCard(content=content, padding="p-6", extra_class="mb-6").render()
        
        # 只显示最近5条
        recent_history = self.history[:5]
        
        history_items = ''
        for record in recent_history:
            title = record.get('title', '')
            result = record.get('result', '')
            predict_date = record.get('predict_date', '')
            verify_date = record.get('verify_date', '')
            price_change = record.get('price_change', '')
            description = record.get('description', '')
            pred_type = record.get('type', '')
            
            is_correct = result == '正确'
            result_color = 'text-green-400' if is_correct else 'text-red-400'
            result_bg = 'bg-green-500/20' if is_correct else 'bg-red-500/20'
            result_icon = '✅' if is_correct else '❌'
            
            history_items += f'''
            <div class="flex items-start gap-4 p-4 bg-white/5 rounded-xl border border-white/10 mb-3 last:mb-0 hover:bg-white/10 transition-colors">
                <div class="flex-shrink-0 w-12 h-12 {result_bg} rounded-xl flex items-center justify-center text-2xl">
                    {result_icon}
                </div>
                <div class="flex-1 min-w-0">
                    <div class="flex items-center gap-2 mb-1">
                        <h4 class="text-white font-semibold truncate">{title}</h4>
                        <span class="px-2 py-0.5 bg-purple-500/20 text-purple-300 text-xs rounded-full flex-shrink-0">{pred_type}</span>
                    </div>
                    <p class="text-sm text-white/60 mb-2 line-clamp-2">{description}</p>
                    <div class="flex items-center gap-4 text-xs text-white/40">
                        <span>📅 预判: {predict_date}</span>
                        <span>🎯 验证: {verify_date}</span>
                        <span class="{result_color} font-medium">📈 {price_change}</span>
                    </div>
                </div>
            </div>
            '''
        
        content = f'''
            {SectionTitle(text='📜 历史验证记录', icon='📜').render()}
            {history_items}
        '''
        
        return GlassCard(content=content, padding="p-6", extra_class="mb-6").render()
    
    def _generate_trends_section(self) -> str:
        """生成准确率趋势区域"""
        by_month = self.trends.get('by_month', [])
        by_type = self.trends.get('by_type', [])
        
        # 月度趋势
        month_bars = ''
        max_accuracy = max([m.get('accuracy', 0) for m in by_month]) if by_month else 100
        for month_data in by_month:
            month = month_data.get('month', '')
            acc = month_data.get('accuracy', 0)
            height_pct = (acc / max_accuracy) * 100 if max_accuracy else 0
            
            month_bars += f'''
            <div class="flex flex-col items-center flex-1">
                <div class="text-xs text-white/60 mb-1">{acc}%</div>
                <div class="w-full bg-white/10 rounded-t-lg relative" style="height: 120px;">
                    <div class="absolute bottom-0 left-0 right-0 bg-gradient-to-t from-indigo-500 to-purple-500 rounded-t-lg transition-all" style="height: {height_pct}%"></div>
                </div>
                <div class="text-xs text-white/60 mt-2">{month}</div>
            </div>
            '''
        
        # 按类型
        type_items = ''
        for type_data in by_type:
            name = type_data.get('name', '')
            acc = type_data.get('accuracy', 0)
            trend = type_data.get('trend', 'stable')
            
            trend_icon = {'up': '📈', 'down': '📉', 'stable': '➡️'}.get(trend, '➡️')
            trend_color = {'up': 'text-green-400', 'down': 'text-red-400', 'stable': 'text-yellow-400'}.get(trend, 'text-white/60')
            
            type_items += f'''
            <div class="flex items-center justify-between p-3 bg-white/5 rounded-lg mb-2 last:mb-0">
                <span class="text-white/80">{name}</span>
                <div class="flex items-center gap-2">
                    <span class="text-white font-bold">{acc}%</span>
                    <span class="{trend_color}">{trend_icon}</span>
                </div>
            </div>
            '''
        
        content = f'''
            <div class="grid grid-cols-2 gap-6">
                <div>
                    {SectionTitle(text='📊 月度准确率走势', icon='📊').render()}
                    <div class="flex items-end gap-2 h-40">
                        {month_bars}
                    </div>
                </div>
                <div>
                    {SectionTitle(text='🎯 按类型准确率', icon='🎯').render()}
                    {type_items}
                </div>
            </div>
        '''
        
        return GlassCard(content=content, padding="p-6", extra_class="mb-6").render()
    
    def _generate_progress_section(self) -> str:
        """生成分析师升级进度区域"""
        prog = self.progress
        current_level = prog.get('current_level', 'C')
        next_level = prog.get('next_level', 'B')
        next_level_name = prog.get('next_level_name', '')
        progress_bar = prog.get('progress_bar', 0)
        gap_desc = prog.get('gap_description', '')
        current_acc = prog.get('current_accuracy', 0)
        target_acc = prog.get('target_accuracy', 0)
        
        content = f'''
            {SectionTitle(text='🚀 分析师升级进度', icon='🚀').render()}
            
            <div class="flex items-center gap-6 mb-4">
                <div class="text-center">
                    <div class="w-16 h-16 rounded-full bg-gradient-to-br from-indigo-500 to-purple-600 flex items-center justify-center text-white text-2xl font-black shadow-lg">
                        {current_level}
                    </div>
                    <div class="text-sm text-white/60 mt-2">当前等级</div>
                </div>
                
                <div class="flex-1">
                    <div class="flex justify-between text-sm mb-2">
                        <span class="text-white/60">升级到 {next_level_name}</span>
                        <span class="text-white font-medium">{progress_bar}%</span>
                    </div>
                    <div class="w-full h-3 bg-white/10 rounded-full overflow-hidden">
                        <div class="h-full bg-gradient-to-r from-indigo-500 via-purple-500 to-pink-500 rounded-full" style="width: {progress_bar}%"></div>
                    </div>
                    <div class="flex justify-between text-xs text-white/40 mt-2">
                        <span>当前: {current_acc}%</span>
                        <span>目标: {target_acc}%</span>
                    </div>
                </div>
                
                <div class="text-center">
                    <div class="w-16 h-16 rounded-full bg-gradient-to-br from-yellow-400 to-orange-500 flex items-center justify-center text-white text-2xl font-black shadow-lg opacity-60">
                        {next_level}
                    </div>
                    <div class="text-sm text-white/60 mt-2">下一等级</div>
                </div>
            </div>
            
            <div class="text-center text-sm text-white/60 bg-white/5 rounded-lg py-3">
                💡 {gap_desc}
            </div>
        '''
        
        return GlassCard(content=content, padding="p-6", extra_class="mb-6").render()
    
    def generate(self) -> str:
        """生成完整的HTML页面"""
        if not self._data_loaded:
            self.load_data()

        # 主题CSS
        theme_css = get_pro_theme_css()
        
        # 各区域
        hero_section = self._generate_hero_section()
        pending_section = self._generate_pending_section()
        history_section = self._generate_history_section()
        trends_section = self._generate_trends_section()
        progress_section = self._generate_progress_section()
        
        # 更新时间
        update_time = self.system_info.get('update_time', datetime.now().strftime('%Y年%m月%d日 %H:%M'))
        
        # 页面底部
        footer = f'''
        <div class="text-center text-white/40 text-sm py-10">
            <p>预判验证系统 V2.1 · 认知飞轮持续进化</p>
            <p class="text-xs mt-2">数据更新时间：{update_time}</p>
        </div>
        '''
        
        # 组装完整页面
        html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>预判验证中心 - 投资研究中心</title>
    <script src="https://cdn.tailwindcss.com"></script>
    {theme_css}
    <style>
        .line-clamp-2 {{
            display: -webkit-box;
            -webkit-line-clamp: 2;
            -webkit-box-orient: vertical;
            overflow: hidden;
        }}
    </style>
</head>
<body>
    <!-- 导航栏 -->
    <nav class="fixed top-0 left-0 right-0 z-50 glass-nav">
        <div class="max-w-5xl mx-auto px-4 py-3 flex items-center justify-between">
            <div class="flex items-center space-x-3">
                <div class="w-8 h-8 rounded-lg bg-gradient-to-br from-indigo-500 to-purple-600 flex items-center justify-center">
                    <span class="text-white text-sm font-bold">📊</span>
                </div>
                <span class="text-white font-bold text-lg">投资研究中心</span>
            </div>
            <div class="nav-links flex items-center space-x-1 flex-wrap gap-1">
                <a href="/daily-news-insight/index.html" class="text-white/80 hover:text-white hover:bg-white/10 text-sm transition-colors px-3 py-1.5 rounded-lg">首页</a>
                <a href="/daily-news-insight/daily/latest.html" class="text-white/80 hover:text-white hover:bg-white/10 text-sm transition-colors px-3 py-1.5 rounded-lg">日报</a>
                <a href="/daily-news-insight/intraday/latest.html" class="text-white/80 hover:text-white hover:bg-white/10 text-sm transition-colors px-3 py-1.5 rounded-lg">盘中</a>
                <a href="/daily-news-insight/aftermarket/latest.html" class="text-white/80 hover:text-white hover:bg-white/10 text-sm transition-colors px-3 py-1.5 rounded-lg">盘后</a>
                <a href="/daily-news-insight/industry_chain/latest.html" class="text-white/80 hover:text-white hover:bg-white/10 text-sm transition-colors px-3 py-1.5 rounded-lg">产业链</a>
                <a href="/daily-news-insight/weekly_review/latest.html" class="text-white/80 hover:text-white hover:bg-white/10 text-sm transition-colors px-3 py-1.5 rounded-lg">周复盘</a>
                <a href="/daily-news-insight/weekly_outlook/latest.html" class="text-white/80 hover:text-white hover:bg-white/10 text-sm transition-colors px-3 py-1.5 rounded-lg">周三前瞻</a>
                <a href="/daily-news-insight/周末速递/latest.html" class="text-white/80 hover:text-white hover:bg-white/10 text-sm transition-colors px-3 py-1.5 rounded-lg">周末速递</a>
                <a href="/daily-news-insight/明日催化剂/latest.html" class="text-white/80 hover:text-white hover:bg-white/10 text-sm transition-colors px-3 py-1.5 rounded-lg">明日催化</a>
                <a href="/daily-news-insight/s_level_catalyst/latest.html" class="text-white/80 hover:text-white hover:bg-white/10 text-sm transition-colors px-3 py-1.5 rounded-lg">S级催化</a>
                <a href="/daily-news-insight/monthly/latest.html" class="text-white/80 hover:text-white hover:bg-white/10 text-sm transition-colors px-3 py-1.5 rounded-lg">月报</a>
            </div>
            <button class="hamburger-btn" onclick="toggleMobileMenu()">☰</button>
        </div>
    </nav>
    
    <!-- 移动端全屏菜单 -->
    <div id="mobileMenu" class="mobile-menu">
        <button class="close-menu-btn" onclick="toggleMobileMenu()">✕</button>
        <a href="/daily-news-insight/index.html" class="mobile-menu-item" onclick="toggleMobileMenu()">🏠 首页</a>
        <a href="/daily-news-insight/daily/latest.html" class="mobile-menu-item" onclick="toggleMobileMenu()">📰 日报</a>
        <a href="/daily-news-insight/intraday/latest.html" class="mobile-menu-item" onclick="toggleMobileMenu()">📈 盘中快报</a>
        <a href="/daily-news-insight/aftermarket/latest.html" class="mobile-menu-item" onclick="toggleMobileMenu()">📉 盘后速递</a>
        <a href="/daily-news-insight/industry_chain/latest.html" class="mobile-menu-item" onclick="toggleMobileMenu()">🔗 产业链总览</a>
        <a href="/daily-news-insight/weekly_review/latest.html" class="mobile-menu-item" onclick="toggleMobileMenu()">📋 周复盘</a>
        <a href="/daily-news-insight/weekly_outlook/latest.html" class="mobile-menu-item" onclick="toggleMobileMenu()">🔮 周三前瞻</a>
        <a href="/daily-news-insight/周末速递/latest.html" class="mobile-menu-item" onclick="toggleMobileMenu()">📦 周末速递</a>
        <a href="/daily-news-insight/明日催化剂/latest.html" class="mobile-menu-item" onclick="toggleMobileMenu()">⏰ 明日催化剂</a>
        <a href="/daily-news-insight/s_level_catalyst/latest.html" class="mobile-menu-item" onclick="toggleMobileMenu()">⭐ S级催化扫描</a>
        <a href="/daily-news-insight/monthly/latest.html" class="mobile-menu-item" onclick="toggleMobileMenu()">🗓️ 月度总结</a>
    </div>
    
    <div class="pro-container pt-20">
        {hero_section}
        {pending_section}
        {trends_section}
        {progress_section}
        {history_section}
        
        {footer}
    </div>
    
    <script>
        // 移动端菜单切换
        function toggleMobileMenu() {{
            const menu = document.getElementById('mobileMenu');
            if (menu) {{
                menu.classList.toggle('show');
                document.body.style.overflow = menu.classList.contains('show') ? 'hidden' : '';
            }}
        }}
        
        // 导航栏滚动效果
        window.addEventListener('scroll', function() {{
            const nav = document.querySelector('.glass-nav');
            if (nav) {{
                if (window.scrollY > 10) {{
                    nav.classList.add('scrolled');
                }} else {{
                    nav.classList.remove('scrolled');
                }}
            }}
        }});
    </script>
</body>
</html>
'''
        
        return html
    
    def save(self, filepath: str) -> str:
        """保存到文件"""
        html = self.generate()
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
        return filepath
    
    def _content(self) -> str:
        """页面主要内容"""
        return self.generate()
    
    def publish(self, output_path: str = "docs/prediction-center/index.html"):
        """发布到生产路径"""
        return super().publish(output_path)


if __name__ == '__main__':
    generator = PredictionCenterProGenerator()
    html = generator.generate()
    
    output_path = '/tmp/test_prediction_center_pro.html'
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"✅ 生成完成")
    print(f"   输出文件: {output_path}")
    print(f"   文件大小: {len(html)} 字节")
    print(f"   待验证预判: {len(generator.pending)} 条")
    print(f"   历史记录: {len(generator.history)} 条")
