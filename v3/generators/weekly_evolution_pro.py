"""
周度进化报告生成器 - Pro版
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


class WeeklyEvolutionProGenerator(ProGenerator):
    data_type = "predictions"
    
    """周度进化报告 - Pro版生成器"""
    
    def __init__(self, data_dir: str = "data"):
        super().__init__(
            title="WeeklyEvolution",
            active_page="",
            footer_text="",
            data_dir=data_dir
        )
    def load_data(self):
        """加载数据"""
        super().load_data()
        self.data = self.data_loader.get_data("predictions")
        self.system_info = self.data.get('system_info', {})
        self.pending = self.data.get('pending_predictions', [])
        self.history = self.data.get('history_records', [])
        self.trends = self.data.get('accuracy_trends', {})
        self.progress = self.data.get('analyst_progress', {})
    
    def _generate_hero_section(self) -> str:
        """生成英雄区 - 本周评级"""
        info = self.system_info
        level = info.get('analyst_level', 'C')
        accuracy = info.get('accuracy', '0%')
        total = info.get('total_predictions', 0)
        correct = info.get('correct_count', 0)
        streak = info.get('streak', 0)
        week_num = info.get('week_num', '第1期')
        
        # 等级颜色
        level_colors = {
            'S': ('#8b5cf6', '#c026d3'),
            'A': ('#3b82f6', '#8b5cf6'),
            'B': ('#10b981', '#059669'),
            'C': ('#f59e0b', '#d97706'),
            'D': ('#ef4444', '#dc2626'),
        }
        color1, color2 = level_colors.get(level, level_colors['C'])
        
        content = f'''
            <div class="text-center">
                <div class="text-sm text-white/60 mb-2 font-medium">📅 {week_num} · 系统周度进化报告</div>
                <div class="text-4xl font-black text-white mb-4">持续进化 · 追求卓越</div>
                
                <div class="inline-block px-8 py-4 bg-gradient-to-r from-yellow-400/20 to-orange-500/20 rounded-2xl border border-yellow-400/30 mb-6">
                    <div class="text-sm text-yellow-300 mb-1">🏆 本周系统综合评级</div>
                    <div class="text-5xl font-black text-yellow-400" style="text-shadow: 0 0 30px rgba(250, 204, 21, 0.5);">
                        {level}级
                    </div>
                    <div class="text-sm text-yellow-200/80 mt-1">综合准确率 {accuracy}</div>
                </div>
                
                <div class="grid grid-cols-4 gap-4 max-w-2xl mx-auto">
                    <div class="p-4 bg-white/5 rounded-xl border border-white/10">
                        <div class="text-3xl font-black text-white">{total}</div>
                        <div class="text-xs text-white/60 mt-1">总预判数</div>
                    </div>
                    <div class="p-4 bg-white/5 rounded-xl border border-white/10">
                        <div class="text-3xl font-black text-green-400">{correct}</div>
                        <div class="text-xs text-white/60 mt-1">正确预判</div>
                    </div>
                    <div class="p-4 bg-white/5 rounded-xl border border-white/10">
                        <div class="text-3xl font-black text-yellow-400">{streak}</div>
                        <div class="text-xs text-white/60 mt-1">连续正确</div>
                    </div>
                    <div class="p-4 bg-white/5 rounded-xl border border-white/10">
                        <div class="text-3xl font-black text-purple-400">{len(self.history)}</div>
                        <div class="text-xs text-white/60 mt-1">历史记录</div>
                    </div>
                </div>
            </div>
        '''
        
        return GlassCard(content=content, padding="p-8", extra_class="mb-6").render()
    
    def _generate_review_section(self) -> str:
        """生成本周预判复盘区域"""
        # 取最近的几条历史记录作为本周复盘
        recent = self.history[:5] if len(self.history) >= 5 else self.history
        
        review_items = ''
        for i, record in enumerate(recent):
            title = record.get('title', '')
            result = record.get('result', '')
            price_change = record.get('price_change', '')
            description = record.get('description', '')
            
            is_correct = result == '正确'
            result_icon = '✅' if is_correct else '❌'
            result_color = 'border-green-400/30 bg-green-400/5' if is_correct else 'border-red-400/30 bg-red-400/5'
            text_color = 'text-green-400' if is_correct else 'text-red-400'
            
            review_items += f'''
            <div class="flex items-start gap-3 p-4 border-l-4 {result_color} rounded-r-lg mb-3 last:mb-0">
                <div class="text-xl flex-shrink-0">{result_icon}</div>
                <div class="flex-1 min-w-0">
                    <div class="flex items-center gap-2 mb-1">
                        <h4 class="text-white font-semibold">{title}</h4>
                        <span class="{text_color} text-sm font-medium">{price_change}</span>
                    </div>
                    <p class="text-sm text-white/60">{description}</p>
                </div>
            </div>
            '''
        
        content = f'''
            {SectionTitle(text='📊 本周预判复盘', icon='📊').render()}
            {review_items}
        '''
        
        return GlassCard(content=content, padding="p-6", extra_class="mb-6").render()
    
    def _generate_methodology_section(self) -> str:
        """生成方法论升级区域"""
        improvements = self.trends.get('improvement_directions', [])
        
        improvement_items = ''
        for i, item in enumerate(improvements):
            icons = ['🎯', '📈', '🔄', '⚡', '💡']
            icon = icons[i % len(icons)]
            improvement_items += f'''
            <div class="flex items-start gap-3 p-4 bg-white/5 rounded-xl border border-white/10 mb-3 last:mb-0">
                <div class="w-10 h-10 bg-gradient-to-br from-indigo-500 to-purple-600 rounded-xl flex items-center justify-center text-xl flex-shrink-0">
                    {icon}
                </div>
                <div class="flex-1">
                    <h4 class="text-white font-semibold mb-1">{item}</h4>
                    <p class="text-sm text-white/60">正在推进中 · 预计下周上线</p>
                </div>
                <div class="text-yellow-400 text-sm font-medium">进行中</div>
            </div>
            '''
        
        content = f'''
            {SectionTitle(text='🔧 方法论升级', icon='🔧').render()}
            {improvement_items}
        '''
        
        return GlassCard(content=content, padding="p-6", extra_class="mb-6").render()
    
    def _generate_outlook_section(self) -> str:
        """生成下周展望区域"""
        risks = self.trends.get('risk_types', [])
        
        risk_items = ''
        for i, risk in enumerate(risks):
            risk_items += f'''
            <div class="flex items-center gap-3 p-3 bg-red-500/10 border border-red-400/20 rounded-xl mb-2 last:mb-0">
                <span class="text-red-400 text-lg">⚠️</span>
                <span class="text-white/80 text-sm">{risk}</span>
            </div>
            '''
        
        # 下周重点关注
        focus_stocks = []
        for pred in self.pending:
            stocks = pred.get('related_stocks', [])
            focus_stocks.extend(stocks)
        
        focus_html = ''
        if focus_stocks:
            focus_tags = ''
            for stock in focus_stocks[:5]:
                focus_tags += f'<span class="px-3 py-1.5 bg-white/10 text-white text-sm rounded-full inline-block m-1">{stock}</span>'
            
            focus_html = f'''
            <div class="mt-6">
                <h4 class="text-white font-semibold mb-3">📌 下周重点关注</h4>
                <div class="flex flex-wrap gap-2">
                    {focus_tags}
                </div>
            </div>
            '''
        
        content = f'''
            {SectionTitle(text='🔮 下周展望', icon='🔮').render()}
            
            <div>
                <h4 class="text-white font-semibold mb-3">⚠️ 潜在风险提示</h4>
                {risk_items}
            </div>
            
            {focus_html}
        '''
        
        return GlassCard(content=content, padding="p-6", extra_class="mb-6").render()
    
    def generate(self) -> str:
        """生成完整的HTML页面"""
        # 主题CSS
        theme_css = get_pro_theme_css()
        
        # 各区域
        hero_section = self._generate_hero_section()
        review_section = self._generate_review_section()
        methodology_section = self._generate_methodology_section()
        outlook_section = self._generate_outlook_section()
        
        # 更新时间
        update_time = self.system_info.get('update_time', datetime.now().strftime('%Y年%m月%d日 %H:%M'))
        
        # 页面底部
        footer = f'''
        <div class="text-center text-white/40 text-sm py-10">
            <p>周度进化报告 · 认知飞轮持续迭代</p>
            <p class="text-xs mt-2">数据更新时间：{update_time}</p>
        </div>
        '''
        
        # 组装完整页面
        html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>周度进化报告 - 投资研究中心</title>
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
                <a href="/daily-news-insight/s级催化扫描/latest.html" class="text-white/80 hover:text-white hover:bg-white/10 text-sm transition-colors px-3 py-1.5 rounded-lg">S级催化</a>
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
        <a href="/daily-news-insight/s级催化扫描/latest.html" class="mobile-menu-item" onclick="toggleMobileMenu()">⭐ S级催化扫描</a>
        <a href="/daily-news-insight/monthly/latest.html" class="mobile-menu-item" onclick="toggleMobileMenu()">🗓️ 月度总结</a>
    </div>
    
    <div class="pro-container pt-20">
        {hero_section}
        {review_section}
        {methodology_section}
        {outlook_section}
        
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
    
    def publish(self, output_path: str = "docs/周度进化报告/index_pro.html"):
        """发布到生产路径"""
        return super().publish(output_path)


if __name__ == '__main__':
    generator = WeeklyEvolutionProGenerator()
    html = generator.generate()
    
    output_path = '/tmp/test_weekly_evolution_pro.html'
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"✅ 生成完成")
    print(f"   输出文件: {output_path}")
    print(f"   文件大小: {len(html)} 字节")
    print(f"   复盘项数: {len(generator.history)}")
    print(f"   升级项数: {len(generator.trends.get('improvement_directions', []))}")
