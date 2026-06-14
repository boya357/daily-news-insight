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
            
            /* 响应式断点 - 平板 */
            @media (max-width: 1024px) {
                .pro-container {
                    max-width: 100%;
                    padding: 0 1rem;
                }
            }
            
            /* 响应式断点 - 手机 */
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
                
                .pro-container {
                    padding: 0 0.75rem;
                }
                
                .card-glass {
                    border-radius: 16px;
                    padding: 1.25rem;
                }
                
                /* 移动端网格优化 */
                .grid-cols-2,
                .grid-cols-3,
                .grid-cols-4,
                .grid-cols-5 {
                    grid-template-columns: 1fr !important;
                }
                
                /* 移动端字体优化 */
                h1 { font-size: 1.75rem !important; }
                h2 { font-size: 1.35rem !important; }
                h3 { font-size: 1.15rem !important; }
            }
            
            /* 响应式断点 - 小屏手机 */
            @media (max-width: 480px) {
                body {
                    padding-top: 60px;
                }
                
                .pro-container {
                    padding: 0 0.5rem;
                }
                
                .card-glass {
                    border-radius: 12px;
                    padding: 1rem;
                }
                
                h1 { font-size: 1.5rem !important; }
                h2 { font-size: 1.2rem !important; }
            }

            /* ===== 交互动效增强 ===== */
            
            /* 卡片入场动画 */
            @keyframes fadeInUp {
                from {
                    opacity: 0;
                    transform: translateY(20px);
                }
                to {
                    opacity: 1;
                    transform: translateY(0);
                }
            }
            
            .animate-fade-in-up {
                animation: fadeInUp 0.6s ease-out forwards;
            }
            
            /* 数字滚动动画容器 */
            .counter-value {
                font-variant-numeric: tabular-nums;
            }
            
            /* 脉冲动画 */
            @keyframes pulse {
                0%, 100% { opacity: 1; }
                50% { opacity: 0.5; }
            }
            
            .animate-pulse {
                animation: pulse 2s cubic-bezier(0.4, 0, 0.6, 1) infinite;
            }
            
            /* 骨架屏加载效果 */
            @keyframes shimmer {
                0% { background-position: -200% 0; }
                100% { background-position: 200% 0; }
            }
            
            .skeleton {
                background: linear-gradient(90deg, rgba(255,255,255,0.1) 25%, rgba(255,255,255,0.2) 50%, rgba(255,255,255,0.1) 75%);
                background-size: 200% 100%;
                animation: shimmer 1.5s infinite;
                border-radius: 8px;
            }
            
            /* 按钮点击效果 */
            .btn-press:active {
                transform: scale(0.95);
            }
            
            /* 标签悬浮效果 */
            .tag-badge {
                transition: all 0.2s ease;
            }
            
            .tag-badge:hover {
                transform: translateY(-2px);
                box-shadow: 0 4px 12px rgba(102, 126, 234, 0.4);
            }
            

            /* 阅读进度条 */
            #progressBar {
                position: fixed;
                top: 0;
                left: 0;
                height: 3px;
                background: linear-gradient(90deg, #6366f1, #a855f7, #ec4899);
                z-index: 9999;
                width: 0%;
                transition: width 0.1s ease;
            }
            
            /* 回到顶部按钮 */
            #backToTop {
                position: fixed;
                bottom: 30px;
                right: 30px;
                width: 50px;
                height: 50px;
                background: linear-gradient(135deg, #6366f1, #a855f7);
                border-radius: 50%;
                display: flex;
                align-items: center;
                justify-content: center;
                color: white;
                cursor: pointer;
                z-index: 9998;
                opacity: 0;
                transform: translateY(20px);
                transition: all 0.3s ease;
                box-shadow: 0 4px 15px rgba(99, 102, 241, 0.4);
                border: none;
            }
            #backToTop:hover {
                transform: translateY(-3px);
                box-shadow: 0 6px 20px rgba(99, 102, 241, 0.5);
            }
            #backToTop.visible {
                opacity: 1;
                transform: translateY(0);
            }
            
            /* 操作按钮组 */
            .action-buttons {
                position: fixed;
                bottom: 30px;
                left: 30px;
                display: flex;
                flex-direction: column;
                gap: 12px;
                z-index: 9998;
            }
            .action-btn {
                width: 50px;
                height: 50px;
                background: rgba(30, 30, 50, 0.8);
                backdrop-filter: blur(20px);
                -webkit-backdrop-filter: blur(20px);
                border: 1px solid rgba(255, 255, 255, 0.1);
                border-radius: 50%;
                display: flex;
                align-items: center;
                justify-content: center;
                color: white;
                cursor: pointer;
                transition: all 0.3s ease;
                box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
            }
            .action-btn:hover {
                background: rgba(99, 102, 241, 0.8);
                transform: translateY(-3px);
                box-shadow: 0 6px 20px rgba(99, 102, 241, 0.4);
            }
            
            /* 打印优化 */
            @media print {
                #progressBar, #backToTop, .action-buttons, .glass-nav, .pro-footer {
                    display: none !important;
                }
                body {
                    background: white !important;
                    color: black !important;
                }
                .card-glass {
                    background: white !important;
                    border: 1px solid #ddd !important;
                    box-shadow: none !important;
                }
            }
            
            /* 移动端适配 */
            @media (max-width: 768px) {
                #backToTop {
                    bottom: 20px;
                    right: 20px;
                    width: 44px;
                    height: 44px;
                }
                .action-buttons {
                    bottom: 20px;
                    left: 20px;
                    gap: 10px;
                }
                .action-btn {
                    width: 44px;
                    height: 44px;
                }
            }
            /* 进度条动画增强 */
            .risk-bar-fill {
                transition: width 1s cubic-bezier(0.4, 0, 0.2, 1);
            }
            
            /* 卡片悬浮增强 */
            .card-glass {
                transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            }
            
            .card-glass:hover {
                transform: translateY(-4px);
                box-shadow: 0 20px 40px rgba(102, 126, 234, 0.3);
            }
            
            /* 导航项下划线动画 */
            .nav-links a {
                position: relative;
            }
            
            .nav-links a::after {
                content: '';
                position: absolute;
                bottom: -2px;
                left: 50%;
                width: 0;
                height: 2px;
                background: linear-gradient(90deg, #667eea, #764ba2);
                transition: all 0.3s ease;
                transform: translateX(-50%);
                border-radius: 1px;
            }
            
            .nav-links a:hover::after,
            .nav-links a.bg-white\/20::after {
                width: 60%;
            }
            
            /* 滚动显示动画 */
            .reveal {
                opacity: 0;
                transform: translateY(30px);
                transition: all 0.8s cubic-bezier(0.4, 0, 0.2, 1);
            }
            
            .reveal.visible {
                opacity: 1;
                transform: translateY(0);
            }
            
            /* 弹跳效果 */
            @keyframes bounce {
                0%, 100% { transform: translateY(0); }
                50% { transform: translateY(-10px); }
            }
            
            .animate-bounce {
                animation: bounce 2s infinite;
            }
            
            /* 旋转动画 */
            @keyframes spin {
                from { transform: rotate(0deg); }
                to { transform: rotate(360deg); }
            }
            
            .animate-spin {
                animation: spin 1s linear infinite;
            }
            
            /* ===== 移动端体验优化 ===== */
            
            /* 触摸区域优化 - 最小44px点击区域 */
            @media (max-width: 768px) {
                .mobile-menu-item {
                    min-height: 44px;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    padding: 12px 20px;
                    -webkit-tap-highlight-color: transparent;
                }
                
                .hamburger-btn,
                .close-menu-btn {
                    min-width: 44px;
                    min-height: 44px;
                    -webkit-tap-highlight-color: transparent;
                }
                
                /* 移动端卡片点击反馈 */
                .card-glass:active {
                    transform: scale(0.98);
                    transition: transform 0.1s ease;
                }
                
                /* 禁止双击缩放 */
                * {
                    touch-action: manipulation;
                }
                
                /* 底部安全区域适配 */
                .pro-container {
                    padding-bottom: calc(1rem + env(safe-area-inset-bottom, 0px));
                }
                
                /* 移动端滚动条隐藏 */
                ::-webkit-scrollbar {
                    width: 4px;
                    height: 4px;
                }
                
                ::-webkit-scrollbar-track {
                    background: transparent;
                }
                
                ::-webkit-scrollbar-thumb {
                    background: rgba(255, 255, 255, 0.3);
                    border-radius: 2px;
                }
                
                /* 移动端标题截断 */
                .section-title {
                    font-size: 1.1rem !important;
                }
                
                /* 移动端网格优化 - 2列布局 */
                .mobile-grid-2 {
                    grid-template-columns: repeat(2, 1fr) !important;
                }
                
                /* 移动端字体优化 */
                body {
                    font-size: 15px;
                    -webkit-font-smoothing: antialiased;
                    -moz-osx-font-smoothing: grayscale;
                }
            }
            
            /* 小屏手机额外优化 */
            @media (max-width: 480px) {
                .mobile-grid-2 {
                    grid-template-columns: 1fr !important;
                }
                
                /* 更小的内边距 */
                .card-glass {
                    padding: 0.875rem !important;
                }
                
                .section-title {
                    font-size: 1rem !important;
                }
            }
            
            /* ===== 深色模式优化 ===== */
            @media (prefers-color-scheme: dark) {
                .text-white\/60 {
                    color: rgba(255, 255, 255, 0.7) !important;
                }
            }
            
            /* ===== 减少动效模式 ===== */
            @media (prefers-reduced-motion: reduce) {
                *,
                *::before,
                *::after {
                    animation-duration: 0.01ms !important;
                    animation-iteration-count: 1 !important;
                    transition-duration: 0.01ms !important;
                }
            }
        
            /* ===== 悬浮目录导航 ===== */
            .toc-wrapper {
                position: fixed;
                top: 120px;
                width: 220px;
                max-height: calc(100vh - 160px);
                background: rgba(139, 92, 246, 0.15);
                backdrop-filter: blur(20px);
                -webkit-backdrop-filter: blur(20px);
                border: 1px solid rgba(255, 255, 255, 0.15);
                border-radius: 16px;
                box-shadow: 0 10px 40px rgba(102, 126, 234, 0.3);
                z-index: 90;
                overflow: hidden;
                transition: all 0.3s ease;
            }
            
            .toc-right {
                right: 20px;
            }
            
            .toc-left {
                left: 20px;
            }
            
            .toc-header {
                display: flex;
                align-items: center;
                justify-content: space-between;
                padding: 12px 16px;
                cursor: pointer;
                border-bottom: 1px solid rgba(255, 255, 255, 0.1);
                user-select: none;
            }
            
            .toc-title {
                font-size: 0.875rem;
                font-weight: 600;
                color: white;
            }
            
            .toc-header svg {
                color: rgba(255, 255, 255, 0.7);
                transition: transform 0.3s ease;
            }
            
            .toc-wrapper.collapsed .toc-header svg {
                transform: rotate(-90deg);
            }
            
            .toc-content {
                max-height: calc(100vh - 220px);
                overflow-y: auto;
                padding: 8px 0;
                transition: max-height 0.3s ease;
            }
            
            .toc-wrapper.collapsed .toc-content {
                max-height: 0;
                padding: 0;
                overflow: hidden;
            }
            
            .toc-item {
                display: block;
                padding: 8px 16px;
                font-size: 0.8125rem;
                color: rgba(255, 255, 255, 0.7);
                text-decoration: none;
                border-left: 3px solid transparent;
                transition: all 0.2s ease;
                cursor: pointer;
            }
            
            .toc-item:hover {
                color: white;
                background: rgba(255, 255, 255, 0.08);
                border-left-color: rgba(255, 255, 255, 0.3);
            }
            
            .toc-item.active {
                color: white;
                font-weight: 500;
                background: rgba(102, 126, 234, 0.3);
                border-left-color: #667eea;
            }
            
            .toc-item.pl-4 {
                padding-left: 32px;
                font-size: 0.75rem;
            }
            
            /* 滚动条样式 */
            .toc-content::-webkit-scrollbar {
                width: 4px;
            }
            
            .toc-content::-webkit-scrollbar-track {
                background: transparent;
            }
            
            .toc-content::-webkit-scrollbar-thumb {
                background: rgba(255, 255, 255, 0.2);
                border-radius: 2px;
            }
            
            .toc-content::-webkit-scrollbar-thumb:hover {
                background: rgba(255, 255, 255, 0.4);
            }
            
            /* 大屏显示优化 */
            @media (min-width: 1400px) {
                .toc-wrapper {
                    width: 260px;
                }
                .toc-right {
                    right: calc((100vw - 64rem) / 2 - 300px);
                }
                .toc-left {
                    left: calc((100vw - 64rem) / 2 - 300px);
                }
            }
            
            /* 平板端隐藏目录 */
            @media (max-width: 1200px) {
                .toc-wrapper {
                    display: none;
                }
            }
            
            /* 页面内容区域适配 - 避免被目录遮挡 */
            @media (min-width: 1200px) {
                .pro-container.has-toc {
                    max-width: 48rem;
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




class FloatingButtons(Component):
    """悬浮按钮组 - 阅读进度条、回到顶部、操作按钮"""
    
    def __init__(self, show_print=True, show_share=True, show_back_to_top=True):
        self.show_print = show_print
        self.show_share = show_share
        self.show_back_to_top = show_back_to_top
    
    def render(self):
        progress_bar = '<div id="progressBar"></div>'
        
        action_buttons = ''
        if self.show_print or self.show_share:
            buttons_html = ''
            if self.show_print:
                buttons_html += '<button onclick="exportPDF()" class="action-btn" title="打印/导出PDF"><span style="font-size:20px">&#x1F4C4;</span></button>'
            if self.show_share:
                buttons_html += '<button onclick="shareReport()" class="action-btn" title="分享报告"><span style="font-size:20px">&#x1F517;</span></button>'
            action_buttons = '<div class="action-buttons">' + buttons_html + '</div>'
        
        back_to_top = ''
        if self.show_back_to_top:
            back_to_top = '<button id="backToTop" onclick="scrollToTop()" title="回到顶部"><svg width="24" height="24" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 10l7-7m0 0l7 7m-7-7v18"></path></svg></button>'
        
        return progress_bar + action_buttons + back_to_top



class TableOfContents(Component):
    """悬浮目录导航 - 页面内锚点跳转+滚动高亮
    
    支持自动提取标题或手动传入目录项
    """
    
    def __init__(self, items: list = None, title: str = "目录", 
                 position: str = "right", auto_extract: bool = True,
                 max_depth: int = 2):
        """
        Args:
            items: 手动目录项列表，每项为 {"title": "", "id": "", "level": 2}
                   为None时自动提取页面h2/h3标题
            title: 目录标题
            position: 位置: left 或 right
            max_depth: 自动提取时的最大深度（2=h2, 3=h2+h3）
        """
        self.items = items or []
        self.title = title
        self.position = position
        self.auto_extract = auto_extract
        self.max_depth = max_depth
    
    def render(self) -> str:
        position_class = 'toc-right' if self.position == 'right' else 'toc-left'
        
        # 生成目录项HTML
        items_html = ''
        if self.items:
            for item in self.items:
                level = item.get('level', 2)
                indent = 'pl-4' if level == 3 else ''
                item_html = '<a href="#' + item['id'] + '" class="toc-item ' + indent + '" data-level="' + str(level) + '">' + item['title'] + '</a>'
                items_html += item_html + '\n'
        
        # 如果自动提取，添加空容器由JS填充
        if self.auto_extract and not self.items:
            items_html = '<div id="tocContainer" class="toc-container"></div>'
        
        html = '<!-- 悬浮目录导航 -->\n'
        html += '<div id="tableOfContents" class="toc-wrapper ' + position_class + '">\n'
        html += '  <div class="toc-header" onclick="toggleTOC()">\n'
        html += '    <span class="toc-title">' + self.title + '</span>\n'
        html += '    <svg id="tocToggleIcon" width="16" height="16" fill="none" stroke="currentColor" viewBox="0 0 24 24" class="transition-transform duration-300">\n'
        html += '      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path>\n'
        html += '    </svg>\n'
        html += '  </div>\n'
        html += '  <div id="tocContent" class="toc-content">\n'
        html += '    ' + items_html + '\n'
        html += '  </div>\n'
        html += '</div>\n'
        
        return html

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
    """页面JavaScript脚本 - 包含菜单切换、滚动效果和交互动效"""
    
    def render(self) -> str:
        return '''
    <script>
        // ==================== 移动端菜单切换 ====================
        function toggleMobileMenu() {
            const menu = document.getElementById('mobileMenu');
            if (menu) {
                menu.classList.toggle('show');
                document.body.style.overflow = menu.classList.contains('show') ? 'hidden' : '';
            }
        }
        
        // 点击菜单项后关闭菜单
        document.addEventListener('click', function(e) {
            if (e.target.classList.contains('mobile-menu-item')) {
                setTimeout(toggleMobileMenu, 100);
            }
        });
        
        // ==================== 导航栏滚动效果 ====================
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
        
        // ==================== 滚动触发动画 ====================
        function initScrollReveal() {
            if ('IntersectionObserver' in window) {
                const observer = new IntersectionObserver(function(entries) {
                    entries.forEach(function(entry) {
                        if (entry.isIntersecting) {
                            entry.target.classList.add('visible');
                        }
                    });
                }, {
                    threshold: 0.1,
                    rootMargin: '0px 0px -50px 0px'
                });
                
                document.querySelectorAll('.reveal, .card-glass').forEach(function(el, index) {
                    observer.observe(el);
                    el.style.animationDelay = (index * 0.1) + 's';
                });
            }
        }
        
        // ==================== 数字滚动动画 ====================
        function animateValue(element, start, end, duration) {
            var startTimestamp = null;
            var step = function(timestamp) {
                if (!startTimestamp) startTimestamp = timestamp;
                var progress = Math.min((timestamp - startTimestamp) / duration, 1);
                var value = Math.floor(progress * (end - start) + start);
                element.textContent = value.toLocaleString();
                if (progress < 1) {
                    window.requestAnimationFrame(step);
                }
            };
            window.requestAnimationFrame(step);
        }
        
        function initCounters() {
            var counters = document.querySelectorAll('.counter-value');
            if ('IntersectionObserver' in window) {
                var observer = new IntersectionObserver(function(entries) {
                    entries.forEach(function(entry) {
                        if (entry.isIntersecting && !entry.target.dataset.animated) {
                            entry.target.dataset.animated = 'true';
                            var target = parseInt(entry.target.dataset.target || entry.target.textContent);
                            animateValue(entry.target, 0, target, 1500);
                        }
                    });
                }, { threshold: 0.5 });
                
                counters.forEach(function(counter) { observer.observe(counter); });
            }
        }
        
        // ==================== 进度条动画 ====================
        function initProgressBars() {
            var bars = document.querySelectorAll('.risk-bar-fill');
            if ('IntersectionObserver' in window) {
                var observer = new IntersectionObserver(function(entries) {
                    entries.forEach(function(entry) {
                        if (entry.isIntersecting && !entry.target.dataset.animated) {
                            entry.target.dataset.animated = 'true';
                            var width = entry.target.style.width;
                            entry.target.style.width = '0%';
                            setTimeout(function() {
                                entry.target.style.width = width;
                            }, 100);
                        }
                    });
                }, { threshold: 0.5 });
                
                bars.forEach(function(bar) { observer.observe(bar); });
            }
        }
        
        // ==================== 卡片入场动画 ====================
        function initCardAnimations() {
            var cards = document.querySelectorAll('.card-glass');
            cards.forEach(function(card, index) {
                card.style.opacity = '0';
                card.style.transform = 'translateY(20px)';
                card.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
                
                setTimeout(function() {
                    card.style.opacity = '1';
                    card.style.transform = 'translateY(0)';
                }, 100 + index * 100);
            });
        }
        

        // ==================== 阅读进度条 & 回到顶部 ====================
        function initProgressAndBackToTop() {
            const progressBar = document.getElementById('progressBar');
            const backToTop = document.getElementById('backToTop');
            
            function updateProgress() {
                const winScroll = document.body.scrollTop || document.documentElement.scrollTop;
                const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
                const scrolled = height > 0 ? (winScroll / height) * 100 : 0;
                
                if (progressBar) {
                    progressBar.style.width = scrolled + '%';
                }
                
                if (backToTop) {
                    if (winScroll > 300) {
                        backToTop.classList.add('visible');
                    } else {
                        backToTop.classList.remove('visible');
                    }
                }
            }
            
            window.addEventListener('scroll', updateProgress);
            updateProgress();
        }
        
        function scrollToTop() {
            window.scrollTo({ top: 0, behavior: 'smooth' });
        }
        
        function exportPDF() {
            window.print();
        }
        
        function shareReport() {
            const url = window.location.href;
            if (navigator.share) {
                navigator.share({ title: document.title, url: url });
            } else {
                navigator.clipboard.writeText(url).then(function() {
                    alert('链接已复制到剪贴板！');
                }).catch(function() {
                    prompt('复制以下链接分享：', url);
                });
            }
        }
        
        // ==================== 平滑滚动 ====================
        function initSmoothScroll() {
            document.querySelectorAll('a[href^="#"]').forEach(function(anchor) {
                anchor.addEventListener('click', function(e) {
                    e.preventDefault();
                    var target = document.querySelector(this.getAttribute('href'));
                    if (target) {
                        target.scrollIntoView({
                            behavior: 'smooth',
                            block: 'start'
                        });
                    }
                });
            });
        }
        
        
        // ==================== 悬浮目录导航 ====================
        function toggleTOC() {
            const toc = document.getElementById('tableOfContents');
            const icon = document.getElementById('tocToggleIcon');
            if (toc) {
                toc.classList.toggle('collapsed');
            }
        }
        
        function initTableOfContents() {
            const tocContainer = document.getElementById('tocContainer');
            if (!tocContainer) return;
            
            // 自动提取页面中的h2和h3标题
            const headings = document.querySelectorAll('.pro-container h2, .pro-container h3');
            if (headings.length === 0) {
                // 没有标题则隐藏目录
                const toc = document.getElementById('tableOfContents');
                if (toc) toc.style.display = 'none';
                return;
            }
            
            // 为标题生成id（如果没有的话）
            headings.forEach(function(heading, index) {
                if (!heading.id) {
                    const text = heading.textContent || heading.innerText;
                    heading.id = 'section-' + index + '-' + text.trim().replace(/\s+/g, '-').replace(/[^\w\-\u4e00-\u9fa5]/g, '').substring(0, 30);
                }
            });
            
            // 生成目录HTML
            var tocHTML = '';
            headings.forEach(function(heading) {
                const level = parseInt(heading.tagName.substring(1));
                const title = heading.textContent || heading.innerText;
                const indent = level === 3 ? 'pl-4' : '';
                tocHTML += '<a href="#' + heading.id + '" class="toc-item ' + indent + '" data-level="' + level + '">' + title.trim() + '</a>';
            });
            
            tocContainer.innerHTML = tocHTML;
            
            // 为目录项添加平滑滚动
            tocContainer.querySelectorAll('.toc-item').forEach(function(item) {
                item.addEventListener('click', function(e) {
                    e.preventDefault();
                    var target = document.querySelector(this.getAttribute('href'));
                    if (target) {
                        // 考虑导航栏高度
                        var offset = 100;
                        var targetPosition = target.getBoundingClientRect().top + window.pageYOffset - offset;
                        window.scrollTo({
                            top: targetPosition,
                            behavior: 'smooth'
                        });
                    }
                });
            });
            
            // 初始化滚动高亮
            initTOCScrollSpy();
        }
        
        function initTOCScrollSpy() {
            const tocItems = document.querySelectorAll('.toc-item');
            if (tocItems.length === 0) return;
            
            // 获取所有章节
            const sections = [];
            tocItems.forEach(function(item) {
                const id = item.getAttribute('href').substring(1);
                const section = document.getElementById(id);
                if (section) {
                    sections.push({
                        element: section,
                        navItem: item,
                        top: section.offsetTop - 120
                    });
                }
            });
            
            if (sections.length === 0) return;
            
            // 滚动时更新高亮
            function updateActiveTOC() {
                const scrollPosition = window.pageYOffset;
                
                // 找到当前处于视口的章节
                var currentIndex = 0;
                for (var i = 0; i < sections.length; i++) {
                    if (scrollPosition >= sections[i].top) {
                        currentIndex = i;
                    }
                }
                
                // 更新高亮状态
                tocItems.forEach(function(item, index) {
                    item.classList.remove('active');
                });
                if (sections[currentIndex]) {
                    sections[currentIndex].navItem.classList.add('active');
                }
            }
            
            window.addEventListener('scroll', updateActiveTOC);
            updateActiveTOC();
        }
// ==================== 页面加载完成后初始化 ====================
        function initAllAnimations() {
            initProgressAndBackToTop();
            initScrollReveal();
            initCounters();
            initProgressBars();
            initCardAnimations();
            initSmoothScroll();
            initTableOfContents();

        }
        
        document.addEventListener('DOMContentLoaded', function() {
            setTimeout(initAllAnimations, 100);
        });
        
        if (document.readyState !== 'loading') {
            setTimeout(initAllAnimations, 100);
        }
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
                 footer_text: str = "", update_time: str = "",
                 show_toc: bool = False, toc_items: list = None,
                 toc_position: str = "right"):
        self.title = title
        self.active_page = active_page
        self.footer_text = footer_text
        self.update_time = update_time
        self.show_toc = show_toc
        self.toc_items = toc_items
        self.toc_position = toc_position
    
    def _content(self) -> str:
        """页面主要内容 - 子类重写此方法"""
        return ""
    
    def render(self) -> str:
        """渲染完整HTML页面"""
        theme_css = get_pro_theme_css()
        nav = NavBar(active_page=self.active_page).render()
        footer = Footer(text=self.footer_text, update_time=self.update_time).render()
        script = PageScript().render()
        floating = FloatingButtons().render()
        content = self._content()
        
        # 渲染目录（如果启用）
        toc_html = ""
        if self.show_toc:
            toc = TableOfContents(items=self.toc_items, position=self.toc_position)
            toc_html = toc.render()
        
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
    
    {floating}
    {toc_html}
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
