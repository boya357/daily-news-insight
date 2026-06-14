"""
Pro深色玻璃态组件库
专业投资监控界面组件，统一深色玻璃态视觉风格

【重要】为保证与现有Pro页面100%视觉兼容，
      组件CSS类名与原始portfolio_dashboard_pro保持一致。
      后续可逐步迁移到统一的pro-*命名规范。
"""
from .base import Component


class ProTheme:
    """Pro主题配置常量"""
    PRIMARY_COLOR = '#667eea'
    SECONDARY_COLOR = '#764ba2'
    ACCENT_COLOR = '#f093fb'
    
    BG_GRADIENT = 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)'
    
    GLASS_BG = 'rgba(139, 92, 246, 0.15)'
    GLASS_BORDER = 'rgba(255, 255, 255, 0.15)'
    GLASS_SHADOW = '0 15px 40px rgba(102, 126, 234, 0.4)'
    
    TEXT_PRIMARY = 'rgba(255, 255, 255, 0.95)'
    TEXT_SECONDARY = 'rgba(255, 255, 255, 0.8)'
    TEXT_MUTED = 'rgba(255, 255, 255, 0.6)'
    
    SUCCESS = '#10b981'
    WARNING = '#f59e0b'
    DANGER = '#ef4444'
    INFO = '#3b82f6'


def get_pro_theme_css() -> str:
    """获取Pro主题全局CSS
    
    与portfolio_dashboard_pro.py中的_generate_dark_theme_css完全一致
    确保视觉效果100%兼容
    """
    return '''
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@300;400;500;700;900&display=swap');
            
            * { font-family: 'Noto Sans SC', sans-serif; }
            
            body {
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
                padding-top: 80px;
            }
            
            .pro-container {
                max-width: 64rem;
                margin: 0 auto;
                padding: 0 1.5rem;
            }
            
            .card-glass {
                background: rgba(139, 92, 246, 0.15);
                backdrop-filter: blur(20px);
                -webkit-backdrop-filter: blur(20px);
                border: 1px solid rgba(255, 255, 255, 0.15);
                box-shadow: 0 15px 40px rgba(102, 126, 234, 0.4);
                border-radius: 20px;
                color: white;
            }
            
            .card-glass .text-gray-800,
            .card-glass .text-gray-700,
            .card-glass .text-gray-600,
            .card-glass .text-gray-500,
            .card-glass .text-gray-400 { color: rgba(255, 255, 255, 0.9) !important; }
            .card-glass .text-gray-500 { color: rgba(255, 255, 255, 0.75) !important; }
            .card-glass .text-gray-400 { color: rgba(255, 255, 255, 0.6) !important; }
            
            /* 修复浅色背景子卡片文字颜色 */
            .card-glass .bg-white .text-gray-800 { color: #1f2937 !important; }
            .card-glass .bg-white .text-gray-700 { color: #374151 !important; }
            .card-glass .bg-white .text-gray-600 { color: #4b5563 !important; }
            .card-glass .bg-white .text-gray-500 { color: #6b7280 !important; }
            .card-glass .bg-white .text-gray-400 { color: #9ca3af !important; }
            
            .stock-card {
                transition: transform 0.3s ease, box-shadow 0.3s ease;
            }
            .stock-card:hover {
                transform: translateY(-4px);
                box-shadow: 0 20px 60px rgba(102, 126, 234, 0.5);
            }
            
            .risk-bar {
                height: 8px;
                border-radius: 4px;
                background: rgba(255,255,255,0.2);
                overflow: hidden;
            }
            .risk-bar-fill {
                height: 100%;
                border-radius: 4px;
                transition: width 0.5s ease;
            }
            
            .diagnosis-item {
                text-align: center;
                padding: 12px 8px;
                background: rgba(255,255,255,0.1);
                border-radius: 12px;
            }
            
            .tag-badge {
                display: inline-block;
                padding: 4px 12px;
                border-radius: 20px;
                font-size: 12px;
                font-weight: 600;
            }
            
            .section-title {
                font-size: 1.25rem;
                font-weight: 700;
                color: white;
                margin-bottom: 1rem;
                display: flex;
                align-items: center;
                gap: 0.5rem;
            }
            
            .lhb-card {
                background: rgba(255,255,255,0.05);
                border-radius: 12px;
                padding: 1rem;
                border: 1px solid rgba(255,255,255,0.1);
            }
            
            .lhb-seat {
                font-size: 0.75rem;
                color: rgba(255,255,255,0.6);
                margin-bottom: 0.25rem;
            }
            
            .fund-row {
                display: flex;
                justify-content: space-between;
                align-items: center;
                padding: 0.75rem 0;
                border-bottom: 1px solid rgba(255,255,255,0.1);
            }
            .fund-row:last-child {
                border-bottom: none;
            }
            
            .fund-trend-up {
                color: #10b981;
                font-weight: 600;
            }
            .fund-trend-down {
                color: #ef4444;
                font-weight: 600;
            }
            
            .alert-section {
                border-left: 4px solid #ef4444;
                padding-left: 1rem;
                margin-bottom: 1rem;
            }
            
            .warning-section {
                border-left: 4px solid #f59e0b;
                padding-left: 1rem;
                margin-bottom: 1rem;
            }
            
            .safe-section {
                border-left: 4px solid #10b981;
                padding-left: 1rem;
                margin-bottom: 1rem;
            }
            
            /* 导航栏样式 */
            .glass-nav {
                background: rgba(0, 0, 0, 0.3);
                backdrop-filter: blur(20px);
                -webkit-backdrop-filter: blur(20px);
                border-bottom: 1px solid rgba(255, 255, 255, 0.1);
                transition: background 0.3s ease;
            }
            
            .glass-nav.scrolled {
                background: rgba(0, 0, 0, 0.7);
            }
            
            /* 汉堡菜单按钮 */
            .hamburger-btn {
                display: none;
                background: rgba(255, 255, 255, 0.1);
                border: 1px solid rgba(255, 255, 255, 0.2);
                color: white;
                width: 40px;
                height: 40px;
                border-radius: 8px;
                cursor: pointer;
                font-size: 18px;
                transition: all 0.3s;
            }
            
            .hamburger-btn:hover {
                background: rgba(255, 255, 255, 0.2);
            }
            
            /* 移动端菜单 */
            .mobile-menu {
                display: none;
                position: fixed;
                top: 0;
                left: 0;
                right: 0;
                bottom: 0;
                background: rgba(0, 0, 0, 0.95);
                backdrop-filter: blur(20px);
                -webkit-backdrop-filter: blur(20px);
                z-index: 100;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                padding: 2rem;
            }
            
            .mobile-menu.show {
                display: flex;
            }
            
            .mobile-menu-item {
                color: white;
                font-size: 18px;
                font-weight: 600;
                padding: 15px 30px;
                text-decoration: none;
                text-align: center;
                width: 100%;
                max-width: 300px;
                border-bottom: 1px solid rgba(255, 255, 255, 0.2);
                transition: all 0.3s;
            }
            
            .mobile-menu-item:hover {
                background: rgba(255, 255, 255, 0.1);
                color: #a78bfa;
            }
            
            .close-menu-btn {
                position: absolute;
                top: 20px;
                right: 20px;
                background: rgba(255, 255, 255, 0.1);
                border: 1px solid rgba(255, 255, 255, 0.2);
                color: white;
                width: 44px;
                height: 44px;
                border-radius: 8px;
                cursor: pointer;
                font-size: 20px;
                transition: all 0.3s;
            }
            
            .close-menu-btn:hover {
                background: rgba(255, 255, 255, 0.2);
            }
            
            /* 响应式断点 */
            @media (max-width: 768px) {
                .nav-links {
                    display: none !important;
                }
                
                .hamburger-btn {
                    display: block !important;
                }
                
                body {
                    padding-top: 70px;
                }
            }
        </style>
    '''


# ============================================================================
# 组件定义
# ============================================================================

class GlassCard(Component):
    """玻璃态卡片 - Pro风格基础容器
    
    对应原始CSS类: card-glass
    """
    
    def __init__(self, content: str = "", padding: str = "p-6", 
                 extra_class: str = "", hover_effect: bool = False):
        self.content = content
        self.padding = padding
        self.extra_class = extra_class
        self.hover_effect = hover_effect
    
    def render(self) -> str:
        hover_class = "transition-all duration-300 hover:scale-[1.02]" if self.hover_effect else ""
        return f'''
        <div class="card-glass {self.padding} {self.extra_class} {hover_class}">
            {self.content}
        </div>
        '''


class SectionTitle(Component):
    """章节标题
    
    对应原始CSS类: section-title
    """
    
    def __init__(self, text: str, icon: str = ""):
        self.text = text
        self.icon = icon
    
    def render(self) -> str:
        icon_html = f'<span class="text-xl">{self.icon}</span>' if self.icon else ''
        return f'<h2 class="section-title">{icon_html}{self.text}</h2>'


class TagBadge(Component):
    """标签徽章
    
    对应原始CSS类: tag-badge
    """
    
    def __init__(self, text: str, color: str = "purple"):
        """
        Args:
            text: 标签文字
            color: 背景色: green, red, yellow, blue, purple
        """
        self.text = text
        self.color = color
    
    def render(self) -> str:
        color_map = {
            'green': 'bg-green-500/20 text-green-400',
            'red': 'bg-red-500/20 text-red-400',
            'yellow': 'bg-yellow-500/20 text-yellow-400',
            'blue': 'bg-blue-500/20 text-blue-400',
            'purple': 'bg-purple-500/30 text-purple-300',
        }
        color_class = color_map.get(self.color, color_map['purple'])
        return f'<span class="tag-badge {color_class}">{self.text}</span>'


class RiskBar(Component):
    """风险进度条
    
    对应原始CSS类: risk-bar, risk-bar-fill
    """
    
    def __init__(self, value: int, max_value: int = 100, 
                 label: str = "", show_labels: bool = False):
        """
        Args:
            value: 当前值
            max_value: 最大值
            label: 标签文字（显示在左侧）
            show_labels: 是否显示底部标签（安全/警戒/危险）
        """
        self.value = value
        self.max_value = max_value
        self.label = label
        self.show_labels = show_labels
    
    def render(self) -> str:
        percentage = (self.value / self.max_value * 100) if self.max_value else 0
        
        label_html = ''
        if self.label:
            label_html = f'<div class="text-sm text-white/70 mb-1">{self.label}</div>'
        
        bottom_labels = ''
        if self.show_labels:
            bottom_labels = '''
            <div class="flex justify-between text-xs text-white/40 mt-1">
                <span>安全</span>
                <span>警戒</span>
                <span>危险</span>
            </div>
            '''
        
        return f'''
        {label_html}
        <div class="risk-bar">
            <div class="risk-bar-fill bg-gradient-to-r from-green-500 via-yellow-500 to-red-500" 
                 style="width: {percentage}%"></div>
        </div>
        {bottom_labels}
        '''


class DiagnosisItem(Component):
    """诊断项 - 用于四维诊断等
    
    对应原始CSS类: diagnosis-item
    """
    
    def __init__(self, icon: str, title: str, status: str = "neutral", desc: str = ""):
        """
        Args:
            icon: emoji图标
            title: 标题（如技术面）
            status: 状态: good, warning, danger, neutral
            desc: 描述文字
        """
        self.icon = icon
        self.title = title
        self.status = status
        self.desc = desc
    
    def render(self) -> str:
        status_colors = {
            'good': 'text-green-400',
            'warning': 'text-yellow-400',
            'danger': 'text-red-400',
            'neutral': 'text-gray-400',
        }
        color = status_colors.get(self.status, 'text-white/70')
        
        return f'''
        <div class="diagnosis-item">
            <div class="text-2xl mb-1">{self.icon}</div>
            <div class="text-sm font-medium {color}">{self.title}</div>
            <div class="text-xs text-white/50 mt-1">{self.desc}</div>
        </div>
        '''


class FundRow(Component):
    """资金流向行
    
    对应原始CSS类: fund-row, fund-trend-up, fund-trend-down
    """
    
    def __init__(self, label: str, value: str, trend: str = "up"):
        """
        Args:
            label: 标签文字
            value: 数值
            trend: 趋势: up 或 down
        """
        self.label = label
        self.value = value
        self.trend = trend
    
    def render(self) -> str:
        trend_class = 'fund-trend-up' if self.trend == 'up' else 'fund-trend-down'
        return f'''
        <div class="fund-row">
            <span class="text-white/70">{self.label}</span>
            <span class="{trend_class}">{self.value}</span>
        </div>
        '''


class LhbCard(Component):
    """龙虎榜卡片
    
    对应原始CSS类: lhb-card, lhb-seat
    """
    
    def __init__(self, seat: str, stock_name: str, reason: str, 
                 net_buy: str = "", net_sell: str = ""):
        self.seat = seat
        self.stock_name = stock_name
        self.reason = reason
        self.net_buy = net_buy
        self.net_sell = net_sell
    
    def render(self) -> str:
        buy_html = f'<div class="text-green-400 text-sm">净买入: {self.net_buy}</div>' if self.net_buy else ''
        sell_html = f'<div class="text-red-400 text-sm">净卖出: {self.net_sell}</div>' if self.net_sell else ''
        
        return f'''
        <div class="lhb-card">
            <div class="lhb-seat">{self.seat}</div>
            <div class="text-white font-medium mb-1">{self.stock_name}</div>
            <div class="text-xs text-white/60 mb-2">{self.reason}</div>
            {buy_html}
            {sell_html}
        </div>
        '''


class AlertSection(Component):
    """警告/提示区域
    
    对应原始CSS类: alert-section, warning-section, safe-section
    """
    
    def __init__(self, title: str, content: str, level: str = "warning"):
        """
        Args:
            title: 标题
            content: 内容HTML
            level: 级别: danger(红), warning(黄), safe(绿)
        """
        self.title = title
        self.content = content
        self.level = level
    
    def render(self) -> str:
        level_class = {
            'danger': 'alert-section',
            'warning': 'warning-section',
            'safe': 'safe-section',
        }.get(self.level, 'warning-section')
        
        title_color = {
            'danger': 'text-red-400',
            'warning': 'text-yellow-400',
            'safe': 'text-green-400',
        }.get(self.level, 'text-yellow-400')
        
        return f'''
        <div class="{level_class}">
            <h3 class="font-semibold {title_color} mb-2">{self.title}</h3>
            <div class="text-white/80 text-sm">
                {self.content}
            </div>
        </div>
        '''


def get_pro_components_css() -> str:
    """获取所有Pro组件的完整CSS（对外统一入口）"""
    return get_pro_theme_css()



class NavBar(Component):
    """导航栏组件 - 包含桌面导航和移动端汉堡菜单"""
    
    def __init__(self, active_page: str = ""):
        self.active_page = active_page
    
    def render(self) -> str:
        nav_items = [
            ('首页', '/daily-news-insight/index.html'),
            ('日报', '/daily-news-insight/daily/latest.html'),
            ('盘中', '/daily-news-insight/intraday/latest.html'),
            ('盘后', '/daily-news-insight/aftermarket/latest.html'),
            ('产业链', '/daily-news-insight/industry_chain/latest.html'),
            ('周复盘', '/daily-news-insight/weekly_review/latest.html'),
            ('周三前瞻', '/daily-news-insight/weekly_outlook/latest.html'),
            ('周末速递', '/daily-news-insight/周末速递/latest.html'),
            ('明日催化', '/daily-news-insight/明日催化剂/latest.html'),
            ('S级催化', '/daily-news-insight/s级催化扫描/latest.html'),
            ('月报', '/daily-news-insight/monthly/latest.html'),
        ]
        
        nav_links = ''
        for name, url in nav_items:
            is_active = self.active_page == name
            active_class = 'text-white bg-white/20' if is_active else 'text-white/80 hover:text-white hover:bg-white/10'
            nav_links += f'<a href="{url}" class="{active_class} text-sm transition-colors px-3 py-1.5 rounded-lg">{name}</a>'
        
        # 移动端菜单项
        mobile_items = [
            ('🏠 首页', '/daily-news-insight/index.html'),
            ('📰 日报', '/daily-news-insight/daily/latest.html'),
            ('📈 盘中快报', '/daily-news-insight/intraday/latest.html'),
            ('📉 盘后速递', '/daily-news-insight/aftermarket/latest.html'),
            ('🔗 产业链总览', '/daily-news-insight/industry_chain/latest.html'),
            ('📋 周复盘', '/daily-news-insight/weekly_review/latest.html'),
            ('🔮 周三前瞻', '/daily-news-insight/weekly_outlook/latest.html'),
            ('📦 周末速递', '/daily-news-insight/周末速递/latest.html'),
            ('⏰ 明日催化剂', '/daily-news-insight/明日催化剂/latest.html'),
            ('⭐ S级催化扫描', '/daily-news-insight/s级催化扫描/latest.html'),
            ('🗓️ 月度总结', '/daily-news-insight/monthly/latest.html'),
        ]
        
        mobile_links = ''
        for name, url in mobile_items:
            mobile_links += f'<a href="{url}" class="mobile-menu-item" onclick="toggleMobileMenu()">{name}</a>'
        
        return f'''
    <nav class="fixed top-0 left-0 right-0 z-50 glass-nav">
        <div class="max-w-5xl mx-auto px-4 py-3 flex items-center justify-between">
            <div class="flex items-center space-x-3">
                <div class="w-8 h-8 rounded-lg bg-gradient-to-br from-indigo-500 to-purple-600 flex items-center justify-center">
                    <span class="text-white text-sm font-bold">📊</span>
                </div>
                <span class="text-white font-bold text-lg">投资研究中心</span>
            </div>
            <div class="nav-links flex items-center space-x-1 flex-wrap gap-1">
                {nav_links}
            </div>
            <button class="hamburger-btn" onclick="toggleMobileMenu()">☰</button>
        </div>
    </nav>
    
    <!-- 移动端全屏菜单 -->
    <div id="mobileMenu" class="mobile-menu">
        <button class="close-menu-btn" onclick="toggleMobileMenu()">✕</button>
        {mobile_links}
    </div>
        '''


class Footer(Component):
    """页脚组件"""
    
    def __init__(self, text: str = "", update_time: str = ""):
        self.text = text
        self.update_time = update_time
    
    def render(self) -> str:
        time_html = f'<p class="text-xs mt-2">数据更新时间：{self.update_time}</p>' if self.update_time else ''
        text_html = f'<p>{self.text}</p>' if self.text else '<p>投资研究中心 · 专业投资决策辅助</p>'
        
        return f'''
        <div class="text-center text-white/40 text-sm py-10">
            {text_html}
            {time_html}
        </div>
        '''


class PageScript(Component):
    """页面JavaScript脚本 - 包含菜单切换和滚动效果"""
    
    def render(self) -> str:
        return '''
    <script>
        // 移动端菜单切换
        function toggleMobileMenu() {
            const menu = document.getElementById('mobileMenu');
            if (menu) {
                menu.classList.toggle('show');
                document.body.style.overflow = menu.classList.contains('show') ? 'hidden' : '';
            }
        }
        
        // 导航栏滚动效果
        window.addEventListener('scroll', function() {
            const nav = document.querySelector('.glass-nav');
            if (nav) {
                if (window.scrollY > 10) {
                    nav.classList.add('scrolled');
                } else {
                    nav.classList.remove('scrolled');
                }
            }
        });
    </script>
        '''


class ProPage:
    """Pro页面基类 - 快速构建标准Pro页面
    
    使用方法:
    1. 继承ProPage
    2. 实现_content()方法，返回页面主要内容HTML
    3. 调用render()生成完整页面
    
    示例:
        class MyPage(ProPage):
            def __init__(self):
                super().__init__(title="我的页面", active_page="首页")
            
            def _content(self):
                return "<p>页面内容</p>"
    """
    
    def __init__(self, title: str = "投资研究中心", active_page: str = "", 
                 footer_text: str = "", update_time: str = ""):
        self.title = title
        self.active_page = active_page
        self.footer_text = footer_text
        self.update_time = update_time
    
    def _content(self) -> str:
        """页面主要内容 - 子类重写此方法"""
        return ""
    
    def render(self) -> str:
        """渲染完整HTML页面"""
        theme_css = get_pro_theme_css()
        nav = NavBar(active_page=self.active_page).render()
        footer = Footer(text=self.footer_text, update_time=self.update_time).render()
        script = PageScript().render()
        content = self._content()
        
        return f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{self.title} - 投资研究中心</title>
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
    {nav}
    
    <div class="pro-container pt-20">
        {content}
        
        {footer}
    </div>
    
    {script}
</body>
</html>
'''
    
    def save(self, filepath: str) -> str:
        """保存到文件"""
        import os
        html = self.render()
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
        return filepath
