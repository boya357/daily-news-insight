"""
持仓智能预警仪表盘生成器 - Pro深色版 V2.0
基于Pro组件库重构，100%组件化，代码复用率高
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



class PortfolioDashboardProV2Generator:
    """持仓智能预警仪表盘 - Pro V2.0 组件化版本"""
    
    def __init__(self, data_path: str = "data/portfolio.json"):
        self.data_path = data_path
        self._load_data()
    
    def _load_data(self):
        """加载持仓数据"""
        with open(self.data_path, 'r', encoding='utf-8') as f:
            self.data = json.load(f)
        self.portfolio = self.data.get('portfolio', {})
        self.stocks = self.data.get('stocks', [])
        self.longhubang = self.data.get('longhubang', {})
    
    def _generate_overview_section(self) -> str:
        """生成第一区：组合总览"""
        portfolio = self.portfolio
        
        # 健康分圆环
        health_score = portfolio.get('health_score', 0)
        health_html = f'''
        <div class="relative">
            <div class="w-24 h-24 rounded-full flex items-center justify-center" 
                 style="background: conic-gradient(#10b981 {health_score}%, rgba(255,255,255,0.2) {health_score}%);">
                <div class="w-20 h-20 bg-white/10 backdrop-blur rounded-full flex items-center justify-center">
                    <div class="text-center">
                        <div class="text-2xl font-black text-white">{health_score}</div>
                        <div class="text-xs text-white/60">健康分</div>
                    </div>
                </div>
            </div>
        </div>
        '''
        
        # 统计卡片
        stats_html = ''
        stats = [
            ('📦', '持仓标的', f"{portfolio.get('stock_count', 0)}只", 'from-blue-500/20 to-indigo-500/20'),
            ('💰', '盈利标的', f"{portfolio.get('profit_count', 0)}只", 'from-green-500/20 to-emerald-500/20'),
            ('📉', '亏损标的', f"{portfolio.get('loss_count', 0)}只", 'from-red-500/20 to-orange-500/20'),
            ('⚠️', '跌破止损', f"{portfolio.get('stop_loss_break_count', 0)}只", 'from-yellow-500/20 to-amber-500/20'),
            ('🏭', '行业分布', f"{portfolio.get('industry_count', 0)}个", 'from-purple-500/20 to-violet-500/20'),
        ]
        
        for icon, label, value, gradient in stats:
            stats_html += f'''
            <div class="p-4 bg-gradient-to-br {gradient} border border-white/10 rounded-2xl text-center">
                <div class="text-2xl mb-1">{icon}</div>
                <div class="text-sm text-white/70 mb-1">{label}</div>
                <div class="text-2xl font-black text-white">{value}</div>
            </div>
            '''
        
        # 总收益
        total_return = portfolio.get('total_return', 0)
        return_pct = f"+{total_return*100:.2f}%" if total_return >= 0 else f"{total_return*100:.2f}%"
        return_color = 'text-green-400' if total_return >= 0 else 'text-red-400'
        
        content = f'''
            <div class="flex items-center justify-between mb-6">
                <div>
                    <h1 class="text-2xl font-black text-white mb-1">投资组合健康度分析</h1>
                    <p class="text-white/60 text-sm">多维度持仓诊断 · 风险实时预警 · 智能调仓建议</p>
                </div>
                <div class="flex items-center gap-6">
                    <div class="text-center">
                        <div class="text-3xl font-black {return_color}">{return_pct}</div>
                        <div class="text-sm text-white/60">组合总盈亏</div>
                    </div>
                    {health_html}
                </div>
            </div>
            
            <div class="grid grid-cols-5 gap-4">
                {stats_html}
            </div>
        '''
        
        return GlassCard(content=content, padding="p-6", extra_class="mb-6").render()
    
    def _generate_stock_card(self, stock: dict) -> str:
        """生成单个股票卡片"""
        name = stock.get('name', '')
        code = stock.get('code', '')
        icon = stock.get('icon', '📈')
        tag = stock.get('tag', '')
        tag_color = stock.get('tag_color', 'bg-purple-500')
        
        # 涨跌幅
        cost_price = stock.get('cost_price', 0)
        current_price = stock.get('current_price', 0)
        profit_pct = (current_price - cost_price) / cost_price * 100 if cost_price else 0
        profit_text = f"+{profit_pct:.2f}%" if profit_pct >= 0 else f"{profit_pct:.2f}%"
        profit_color = 'text-green-400' if profit_pct >= 0 else 'text-red-400'
        
        # 今日涨跌
        today_change = stock.get('today_change', 0)
        today_text = f"+{today_change*100:.2f}%" if today_change >= 0 else f"{today_change*100:.2f}%"
        today_color = 'text-green-400' if today_change >= 0 else 'text-red-400'
        
        # 距止损
        stop_loss_price = stock.get('stop_loss_price', 0)
        distance_to_stop = stock.get('distance_to_stop_loss', 0)
        distance_text = f"{distance_to_stop*100:.2f}%"
        
        # 主力资金
        main_fund = stock.get('main_fund', '-')
        fund_color = 'text-green-400' if main_fund.startswith('+') else 'text-red-400'
        
        # 风险进度条
        risk_progress = stock.get('risk_progress', 50)
        
        # 四维诊断
        diagnosis = stock.get('diagnosis', {})
        diagnosis_html = ''
        for key, diag in diagnosis.items():
            diagnosis_html += DiagnosisItem(
                icon=diag.get('icon', '📊'),
                title=diag.get('title', key),
                status=diag.get('status', 'neutral'),
                desc=diag.get('value', '')
            ).render()
        
        # 建议
        advice = stock.get('advice', {})
        advice_type = advice.get('type', 'watch')
        advice_text = advice.get('text', '')
        
        content = f'''
            <div class="flex items-start justify-between mb-6">
                <div class="flex items-center gap-4">
                    <div class="w-16 h-16 rounded-2xl bg-gradient-to-br from-purple-500 to-pink-500 flex items-center justify-center">
                        <span class="text-white text-3xl font-black">{icon}</span>
                    </div>
                    <div>
                        <div class="flex items-center gap-3">
                            <h2 class="text-2xl font-black text-white"><span class="stock-badge" data-code="{code}" data-name="{name}">{name}</span></h2>
                            <span class="text-white/60">{code}</span>
                            <span class="{tag_color} text-white text-xs px-3 py-1 rounded-full font-bold">{tag}</span>
                        </div>
                        <p class="text-white/50 text-sm mt-1">液冷散热 · 英伟达产业链 · 算力基础设施</p>
                    </div>
                </div>
                <div class="text-right">
                    <div class="text-4xl font-black {profit_color}">{profit_text}</div>
                    <div class="text-sm text-white/60">持仓盈亏</div>
                </div>
            </div>
            
            <div class="grid grid-cols-6 gap-4 mb-6">
                <div class="p-4 bg-white/5 rounded-xl text-center">
                    <div class="text-xs text-white/50 mb-1">成本价</div>
                    <div class="text-xl font-bold text-white/90">{cost_price:.2f}元</div>
                </div>
                <div class="p-4 bg-white/5 rounded-xl text-center">
                    <div class="text-xs text-white/50 mb-1">最新价</div>
                    <div class="text-xl font-bold text-white">{current_price:.2f}元</div>
                </div>
                <div class="p-4 bg-white/5 rounded-xl text-center">
                    <div class="text-xs text-white/50 mb-1">止损价</div>
                    <div class="text-xl font-bold text-orange-400">{stop_loss_price:.2f}元</div>
                </div>
                <div class="p-4 bg-white/5 rounded-xl text-center">
                    <div class="text-xs text-white/50 mb-1">距止损</div>
                    <div class="text-xl font-bold text-yellow-400">{distance_text}</div>
                </div>
                <div class="p-4 bg-white/5 rounded-xl text-center">
                    <div class="text-xs text-white/50 mb-1">今日涨跌</div>
                    <div class="text-xl font-bold {today_color}">{today_text}</div>
                </div>
                <div class="p-4 bg-white/5 rounded-xl text-center">
                    <div class="text-xs text-white/50 mb-1">主力资金</div>
                    <div class="text-xl font-bold {fund_color}">{main_fund}</div>
                </div>
            </div>
            
            <div class="mb-6">
                <div class="flex justify-between text-sm mb-2">
                    <span class="text-white/60">风险程度</span>
                    <span class="text-white font-bold">{stock.get('risk_level', '中风险')}</span>
                </div>
                {RiskBar(value=risk_progress, show_labels=True).render()}
            </div>
            
            <div class="grid grid-cols-4 gap-4">
                {diagnosis_html}
            </div>
        '''
        
        return GlassCard(content=content, padding="p-6", extra_class="stock-card mb-6", hover_effect=True).render()
    
    def _generate_stress_test_section(self) -> str:
        """生成第三区：压力测试"""
        stocks = self.stocks
        
        # 极端下跌情景
        extreme_rows = ''
        for stock in stocks:
            extreme_val = stock.get('stress_test', {}).get('extreme', '-')
            extreme_rows += f'''
            <div class="text-center">
                <div class="text-white/50 text-xs">{stock['name']}</div>
                <div class="font-bold text-yellow-400">{extreme_val}</div>
            </div>
            '''
        
        # 中性情景
        neutral_rows = ''
        for stock in stocks:
            neutral_val = stock.get('stress_test', {}).get('neutral', '-')
            neutral_rows += f'''
            <div class="text-center">
                <div class="text-white/50 text-xs">{stock['name']}</div>
                <div class="font-bold text-yellow-400">{neutral_val}</div>
            </div>
            '''
        
        content = f'''
            {SectionTitle(text='压力测试情景', icon='🚨').render()}
            
            <div class="space-y-4">
                <div class="p-4 bg-red-500/10 border border-red-500/20 rounded-xl">
                    <div class="font-bold text-red-400 mb-2">极端下跌情景：大盘回调10%</div>
                    <div class="grid grid-cols-4 gap-3 text-sm">
                        {extreme_rows}
                    </div>
                    <div class="text-sm text-white/60 mt-2 text-center font-semibold">组合最大回撤：约-16%</div>
                </div>
                
                <div class="p-4 bg-yellow-500/10 border border-yellow-500/20 rounded-xl">
                    <div class="font-bold text-yellow-400 mb-2">中性情景：板块震荡5%</div>
                    <div class="grid grid-cols-4 gap-3 text-sm">
                        {neutral_rows}
                    </div>
                    <div class="text-sm text-white/60 mt-2 text-center font-semibold">组合预计回撤：约-5%</div>
                </div>
            </div>
        '''
        
        return GlassCard(content=content, padding="p-6").render()
    
    def _generate_advice_section(self) -> str:
        """生成第三区：智能调仓建议"""
        stocks = self.stocks
        portfolio = self.portfolio
        
        advice_html = ''
        for stock in stocks:
            advice = stock.get('advice', {})
            advice_type = advice.get('type', 'watch')
            advice_label = advice.get('type_label', '持有观察')
            advice_text = advice.get('text', '')
            
            # 状态颜色
            if advice_type == 'sell':
                bg_class = 'bg-red-500/10 border-red-500/20 border-l-red-500'
                text_color = 'text-red-400'
            elif advice_type == 'buy':
                bg_class = 'bg-green-500/10 border-green-500/20 border-l-green-500'
                text_color = 'text-green-400'
            elif advice_type == 'hold':
                bg_class = 'bg-green-500/10 border-green-500/20 border-l-green-500'
                text_color = 'text-green-400'
            else:  # watch
                bg_class = 'bg-yellow-500/10 border-yellow-500/20 border-l-yellow-500'
                text_color = 'text-yellow-400'
            
            advice_html += f'''
            <div class="p-4 {bg_class} rounded-xl border-l-4">
                <div class="font-bold {text_color} mb-1">{advice_label}</div>
                <p class="text-sm text-white/80">{advice_text}</p>
            </div>
            '''
        
        # 总体建议
        overall_advice = portfolio.get('overall_advice', '')
        advice_html += f'''
        <div class="p-4 bg-blue-500/10 border border-blue-500/20 rounded-xl border-l-4 border-l-blue-500">
            <div class="font-bold text-blue-400 mb-1">🔵 再平衡建议</div>
            <p class="text-sm text-white/80">{overall_advice}</p>
        </div>
        '''
        
        content = f'''
            {SectionTitle(text='智能调仓建议', icon='💡').render()}
            <div class="space-y-4">
                {advice_html}
            </div>
        '''
        
        return GlassCard(content=content, padding="p-6").render()
    
    def _generate_longhubang_section(self) -> str:
        """生成第四区：龙虎榜追踪"""
        lhb_stocks = self.longhubang.get('stocks', [])
        
        lhb_html = ''
        for lhb in lhb_stocks:
            name = lhb.get('name', '')
            code = lhb.get('code', '')
            date = lhb.get('date', '')
            reason = lhb.get('list_reason', '')
            change_pct = lhb.get('change_pct', 0)
            net_buy = lhb.get('net_buy', '')
            analysis = lhb.get('analysis', {})
            
            change_text = f"+{change_pct:.2f}%" if change_pct >= 0 else f"{change_pct:.2f}%"
            change_color = 'text-red-400' if change_pct >= 0 else 'text-green-400'
            
            # 买卖席位
            buy_seats = lhb.get('buy_seats', [])
            sell_seats = lhb.get('sell_seats', [])
            
            buy_html = ''
            for seat in buy_seats[:3]:
                seat_name = seat.get('name', '')
                seat_net = seat.get('net', '')
                net_color = 'text-green-400' if seat_net.startswith('+') else 'text-red-400'
                buy_html += f'''
                <div class="flex justify-between text-xs py-1">
                    <span class="text-white/60">{seat_name}</span>
                    <span class="font-semibold {net_color}">{seat_net}</span>
                </div>
                '''
            
            sell_html = ''
            for seat in sell_seats[:3]:
                seat_name = seat.get('name', '')
                seat_net = seat.get('net', '')
                net_color = 'text-green-400' if seat_net.startswith('+') else 'text-red-400'
                sell_html += f'''
                <div class="flex justify-between text-xs py-1">
                    <span class="text-white/60">{seat_name}</span>
                    <span class="font-semibold {net_color}">{seat_net}</span>
                </div>
                '''
            
            # 核心结论
            key_conclusion = analysis.get('key_conclusion', '')
            
            lhb_html += f'''
            <div class="border border-orange-500/30 rounded-xl overflow-hidden">
                <div class="bg-gradient-to-r from-orange-500/10 to-red-500/10 px-4 py-3 flex items-center justify-between">
                    <div class="flex items-center gap-3">
                        <span class="text-xl">🔴</span>
                        <div>
                            <div class="font-bold text-white">{name} <span class="text-sm font-normal text-white/60">{code}</span></div>
                            <div class="text-xs text-white/50">{date} · {reason}</div>
                        </div>
                    </div>
                    <div class="text-right">
                        <div class="font-bold {change_color}">{change_text}</div>
                        <div class="text-xs text-white/50">净买入 {net_buy}</div>
                    </div>
                </div>
                <div class="p-4">
                    <div class="grid grid-cols-2 gap-4">
                        <div>
                            <div class="text-sm font-semibold text-green-400 mb-2">📈 买入席位</div>
                            {buy_html}
                        </div>
                        <div>
                            <div class="text-sm font-semibold text-red-400 mb-2">📉 卖出席位</div>
                            {sell_html}
                        </div>
                    </div>
                    <div class="mt-4 p-3 bg-yellow-500/10 rounded-lg">
                        <div class="text-sm font-bold text-yellow-400 mb-1">💡 龙虎榜解读</div>
                        <p class="text-xs text-white/70">{key_conclusion}</p>
                    </div>
                </div>
            </div>
            '''
        
        content = f'''
            {SectionTitle(text='龙虎榜追踪', icon='🐉').render()}
            <div class="space-y-4">
                {lhb_html}
            </div>
        '''
        
        return GlassCard(content=content, padding="p-6", extra_class="mt-6").render()
    
    def generate(self) -> str:
        """生成完整的HTML页面"""
        # 主题CSS
        theme_css = get_pro_theme_css()
        
        # 导航栏（Pro风格 - 完整11菜单项 + 移动端汉堡菜单）
        nav = """
    <nav class="fixed top-0 left-0 right-0 z-50 glass-nav">
        <div class="max-w-7xl mx-auto px-4 py-3 flex items-center justify-between">
            <div class="flex items-center space-x-3">
                <div class="w-8 h-8 rounded-lg bg-gradient-to-br from-indigo-500 to-purple-600 flex items-center justify-center">
                    <span class="text-white text-sm font-bold">📊</span>
                </div>
                <span class="text-white font-bold text-lg">投资研究中心</span>
            </div>
            <div class="nav-links flex items-center space-x-1 flex-wrap gap-1">
                <a href="/daily-news-insight/index.html" class="text-white/80 hover:text-white hover:bg-white/10 text-sm transition-colors px-3 py-1.5 rounded-lg">首页</a>
                <a href="/daily-news-insight/daily/index.html" class="text-white/80 hover:text-white hover:bg-white/10 text-sm transition-colors px-3 py-1.5 rounded-lg">日报</a>
                <a href="/daily-news-insight/intraday/index.html" class="text-white/80 hover:text-white hover:bg-white/10 text-sm transition-colors px-3 py-1.5 rounded-lg">盘中</a>
                <a href="/daily-news-insight/aftermarket/index.html" class="text-white/80 hover:text-white hover:bg-white/10 text-sm transition-colors px-3 py-1.5 rounded-lg">盘后</a>
                <a href="/daily-news-insight/industry_chain/index.html" class="text-white/80 hover:text-white hover:bg-white/10 text-sm transition-colors px-3 py-1.5 rounded-lg">产业链</a>
                <a href="/daily-news-insight/weekly_review/index.html" class="text-white/80 hover:text-white hover:bg-white/10 text-sm transition-colors px-3 py-1.5 rounded-lg">周复盘</a>
                <a href="/daily-news-insight/weekly_outlook/index.html" class="text-white/80 hover:text-white hover:bg-white/10 text-sm transition-colors px-3 py-1.5 rounded-lg">周三前瞻</a>
                <a href="/daily-news-insight/weekend_express/index.html" class="text-white/80 hover:text-white hover:bg-white/10 text-sm transition-colors px-3 py-1.5 rounded-lg">周末速递</a>
                <a href="/daily-news-insight/tomorrow_catalyst/index.html" class="text-white/80 hover:text-white hover:bg-white/10 text-sm transition-colors px-3 py-1.5 rounded-lg">明日催化</a>
                <a href="/daily-news-insight/s_level_catalyst/index.html" class="text-white/80 hover:text-white hover:bg-white/10 text-sm transition-colors px-3 py-1.5 rounded-lg">S级催化</a>
                <a href="/daily-news-insight/monthly/index.html" class="text-white/80 hover:text-white hover:bg-white/10 text-sm transition-colors px-3 py-1.5 rounded-lg">月报</a>
            </div>
            <button class="hamburger-btn" onclick="toggleMobileMenu()">☰</button>
        </div>
    </nav>
    
    <!-- 移动端全屏菜单 -->
    <div id="mobileMenu" class="mobile-menu">
        <button class="close-menu-btn" onclick="toggleMobileMenu()">✕</button>
        <a href="/daily-news-insight/index.html" class="mobile-menu-item" onclick="toggleMobileMenu()">🏠 首页</a>
        <a href="/daily-news-insight/daily/index.html" class="mobile-menu-item" onclick="toggleMobileMenu()">📰 日报</a>
        <a href="/daily-news-insight/intraday/index.html" class="mobile-menu-item" onclick="toggleMobileMenu()">📈 盘中快报</a>
        <a href="/daily-news-insight/aftermarket/index.html" class="mobile-menu-item" onclick="toggleMobileMenu()">📉 盘后速递</a>
        <a href="/daily-news-insight/industry_chain/index.html" class="mobile-menu-item" onclick="toggleMobileMenu()">🔗 产业链总览</a>
        <a href="/daily-news-insight/weekly_review/index.html" class="mobile-menu-item" onclick="toggleMobileMenu()">📋 周复盘</a>
        <a href="/daily-news-insight/weekly_outlook/index.html" class="mobile-menu-item" onclick="toggleMobileMenu()">🔮 周三前瞻</a>
        <a href="/daily-news-insight/weekend_express/index.html" class="mobile-menu-item" onclick="toggleMobileMenu()">📦 周末速递</a>
        <a href="/daily-news-insight/tomorrow_catalyst/index.html" class="mobile-menu-item" onclick="toggleMobileMenu()">⏰ 明日催化剂</a>
        <a href="/daily-news-insight/s_level_catalyst/index.html" class="mobile-menu-item" onclick="toggleMobileMenu()">⭐ S级催化扫描</a>
        <a href="/daily-news-insight/monthly/index.html" class="mobile-menu-item" onclick="toggleMobileMenu()">🗓️ 月度总结</a>
    </div>
"""
        
        # 第一区：组合总览
        overview_section = self._generate_overview_section()
        
        # 第二区：持仓股票卡片
        stocks_section = ''
        for stock in self.stocks:
            stocks_section += self._generate_stock_card(stock)
        
        # 第三区：压力测试 + 调仓建议（两列布局）
        stress_section = self._generate_stress_test_section()
        advice_section = self._generate_advice_section()
        
        # 第四区：龙虎榜
        longhubang_section = self._generate_longhubang_section()
        
        # 页面底部
        update_time = datetime.now().strftime('%Y年%m月%d日 %H:%M')
        footer = f'''
        <div class="text-center text-white/40 text-sm py-10">
            <p>MLCC Pro v2.0 · 持仓智能预警仪表盘 Professional</p>
            <p class="text-xs mt-2">四维诊断 · 压力测试 · 智能调仓建议 · 龙虎榜追踪 · 风险实时监控</p>
            <p class="text-xs mt-1">数据更新时间：{update_time}</p>
        </div>
        '''
        
        # 组装完整页面
        html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>持仓智能预警仪表盘 - Pro</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="/daily-news-insight/assets/stock-popup.css">
    {theme_css}
</head>
<body>
    {nav}
    
    <div class="pro-container">
        {overview_section}
        {stocks_section}
        
        <div class="grid grid-cols-2 gap-6 mb-6">
            {stress_section}
            {advice_section}
        </div>
        
        {longhubang_section}
        
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
    <script src="/daily-news-insight/assets/stock-popup.js"></script>
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
    
    def publish(self, output_path: str = "docs/portfolio_dashboard/index_pro.html"):
        """发布到生产路径"""
        return self.save(output_path)


if __name__ == '__main__':
    generator = PortfolioDashboardProV2Generator()
    html = generator.generate()
    
    output_path = '/tmp/test_pro_v2_dashboard.html'
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"✅ 生成完成")
    print(f"   输出文件: {output_path}")
    print(f"   文件大小: {len(html)} 字节")
    print(f"   股票数量: {len(generator.stocks)}")
    print(f"   龙虎榜数量: {len(generator.longhubang['stocks'])}")
