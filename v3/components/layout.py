"""
布局组件 - Navbar, Footer, Section, Card
升级后的高级感设计
"""
from .base import Component


class Navbar(Component):
    """
    导航栏组件 - 全站统一导航
    11个导航项，玻璃态效果，移动端汉堡菜单
    """
    
    def __init__(self, active_key: str = None):
        super().__init__()
        self.active_key = active_key
    
    @staticmethod
    def get_css() -> str:
        """获取导航栏所需的CSS样式"""
        return """
        <style>
            .glass-nav {
                background: rgba(255, 255, 255, 0.08);
                backdrop-filter: blur(20px);
                -webkit-backdrop-filter: blur(20px);
                border-bottom: 1px solid rgba(255, 255, 255, 0.15);
                z-index: 2147483647 !important;
                isolation: isolate !important;
                pointer-events: auto !important;
            }
            .glass-nav * {
                position: relative;
                z-index: 2147483647 !important;
                pointer-events: auto !important;
            }
            .hamburger-btn {
                display: none;
                background: rgba(255,255,255,0.15);
                border: none;
                color: white;
                width: 44px;
                height: 44px;
                border-radius: 12px;
                cursor: pointer;
                font-size: 20px;
                z-index: 99999;
                align-items: center;
                justify-content: center;
            }
            .mobile-menu {
                position: fixed;
                top: 0;
                left: 0;
                right: 0;
                bottom: 0;
                background: linear-gradient(135deg, rgba(79, 70, 229, 0.98) 0%, rgba(124, 58, 237, 0.98) 100%);
                backdrop-filter: blur(20px);
                -webkit-backdrop-filter: blur(20px);
                z-index: 99998;
                display: none;
                flex-direction: column;
                align-items: stretch;
                padding: 20px;
                overflow-y: auto;
            }
            .mobile-menu.show {
                display: flex;
            }
            .mobile-menu-item {
                display: flex;
                align-items: center;
                color: white !important;
                padding: 16px 20px;
                text-decoration: none;
                font-size: 16px;
                font-weight: 500;
                border-bottom: 1px solid rgba(255,255,255,0.1);
                border-radius: 12px;
                margin-bottom: 4px;
                transition: all 0.2s;
            }
            .mobile-menu-item:hover {
                background: rgba(255,255,255,0.1);
            }
            .close-menu-btn {
                position: absolute;
                top: 16px;
                right: 16px;
                background: rgba(255,255,255,0.15);
                border: none;
                color: white;
                width: 44px;
                height: 44px;
                border-radius: 12px;
                cursor: pointer;
                font-size: 20px;
                display: flex;
                align-items: center;
                justify-content: center;
                z-index: 99999;
            }
            .mobile-menu-items {
                flex: 1;
                display: flex;
                flex-direction: column;
                justify-content: center;
            }
            @media (max-width: 1024px) {
                .nav-links {
                    display: none !important;
                }
                .hamburger-btn {
                    display: flex !important;
                }
            }
        </style>
        """
    
    def render(self) -> str:
        from core.config import NAV_ITEMS
        
        nav_items_html = ""
        mobile_items_html = ""
        
        for item in NAV_ITEMS:
            is_active = item["key"] == self.active_key
            active_class = "text-white bg-white/15" if is_active else "text-white/80 hover:text-white hover:bg-white/10"
            
            nav_items_html += f'''
                <a href="{item["path"]}" class="{active_class} text-sm transition-colors px-3 py-2 rounded-lg whitespace-nowrap">
                    {item["label"]}
                </a>
            '''
            
            mobile_active_class = "bg-white/20 text-white" if is_active else "text-white/90"
            mobile_items_html += f'''
                <a href="{item["path"]}" class="mobile-menu-item {mobile_active_class}" onclick="toggleMobileMenu()">
                    {item["icon"]} {item["label"]}
                </a>
            '''
        
        return f'''
        <nav class="fixed top-0 left-0 right-0 z-50 glass-nav">
            <div class="max-w-5xl mx-auto px-4 py-3 flex items-center justify-between">
                <div class="flex items-center space-x-3">
                    <div class="w-9 h-9 rounded-xl bg-gradient-to-br from-white/30 to-white/10 flex items-center justify-center backdrop-blur-sm">
                        <span class="text-white text-lg">📊</span>
                    </div>
                    <span class="text-white font-bold text-lg">投资研究中心</span>
                </div>
                
                <!-- 桌面端导航 -->
                <div class="nav-links hidden lg:flex items-center space-x-1 flex-wrap gap-1">
                    {nav_items_html}
                </div>
                
                <!-- 移动端汉堡按钮 -->
                <button class="hamburger-btn lg:hidden" onclick="toggleMobileMenu()" aria-label="菜单">
                    <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"/>
                    </svg>
                </button>
            </div>
        </nav>
        
        <!-- 移动端全屏菜单 -->
        <div id="mobileMenu" class="mobile-menu">
            <button class="close-menu-btn" onclick="toggleMobileMenu()" aria-label="关闭">
                <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/>
                </svg>
            </button>
            <div class="mobile-menu-items pt-20">
                {mobile_items_html}
            </div>
        </div>
        
        <script>
            function toggleMobileMenu() {{
                const menu = document.getElementById('mobileMenu');
                menu.classList.toggle('show');
                document.body.style.overflow = menu.classList.contains('show') ? 'hidden' : '';
            }}
            
            // 点击菜单项后自动关闭
            document.querySelectorAll('.mobile-menu-item').forEach(item => {{
                item.addEventListener('click', () => {{
                    document.getElementById('mobileMenu').classList.remove('show');
                    document.body.style.overflow = '';
                }});
            }});
        </script>
        '''


class Footer(Component):
    """
    页脚组件
    """
    
    def __init__(self):
        super().__init__()
    
    @staticmethod
    def get_css() -> str:
        """获取页脚所需的CSS样式"""
        return ""  # 页脚样式已包含在基础CSS中
    
    def render(self) -> str:
        return '''
        <footer class="mt-16 pb-8 px-4">
            <div class="max-w-5xl mx-auto text-center">
                <div class="text-white/60 text-sm space-y-2">
                    <p>💡 投资研究中心 · 专业深度研究</p>
                    <p class="text-white/40 text-xs">数据仅供参考，不构成投资建议 | 投资有风险，入市需谨慎</p>
                </div>
            </div>
        </footer>
        '''


class Section(Component):
    """
    章节组件 - 带标题和内容的独立区块
    高级感设计：大圆角、柔和阴影、充足内边距
    """
    
    def __init__(self, title: str, content, subtitle: str = None, 
                 icon: str = None, variant: str = "default"):
        super().__init__()
        self.title = title
        self.content = content
        self.subtitle = subtitle
        self.icon = icon
        self.variant = variant  # default, highlight, subtle
    
    def render(self) -> str:
        # 处理内容：如果是Component就渲染，否则直接用
        content_html = self.content.render() if hasattr(self.content, 'render') else str(self.content)
        
        # 标题图标
        icon_html = f'<span class="mr-2">{self.icon}</span>' if self.icon else ''
        
        # 副标题
        subtitle_html = f'<p class="text-gray-500 text-sm mt-1">{self.subtitle}</p>' if self.subtitle else ''
        
        # 根据变体选择样式
        if self.variant == "highlight":
            # 高亮版本：带左侧色条
            header_class = "border-l-4 border-indigo-500 pl-4 mb-4"
            title_class = "text-xl font-bold text-gray-800"
        elif self.variant == "subtle":
            # 柔和版本
            header_class = "mb-4"
            title_class = "text-lg font-semibold text-gray-700"
        else:
            header_class = "mb-5 pb-3 border-b border-gray-100"
            title_class = "text-xl font-bold text-gray-800"
        
        return f"""
        <div class="bg-white/95 backdrop-blur-sm rounded-2xl p-6 shadow-md hover:shadow-lg transition-shadow duration-300 border border-gray-100">
            <div class="{header_class}">
                <h3 class="{title_class}">
                    {icon_html}{self.title}
                </h3>
                {subtitle_html}
            </div>
            <div class="prose-content">
                {content_html}
            </div>
        </div>
        """


class Card(Component):
    """
    卡片组件 - 通用信息卡片
    """
    
    def __init__(self, title: str = None, content = None, 
                 icon: str = None, variant: str = "default"):
        super().__init__()
        self.title = title
        self.content = content
        self.icon = icon
        self.variant = variant
    
    def render(self) -> str:
        content_html = self.content.render() if hasattr(self.content, 'render') else str(self.content)
        
        variants = {
            "default": "bg-white border border-gray-100",
            "primary": "bg-gradient-to-br from-indigo-50 to-purple-50 border border-indigo-100",
            "success": "bg-gradient-to-br from-green-50 to-emerald-50 border border-green-100",
            "warning": "bg-gradient-to-br from-amber-50 to-orange-50 border border-amber-100",
            "danger": "bg-gradient-to-br from-red-50 to-rose-50 border border-red-100",
        }
        
        card_class = variants.get(self.variant, variants["default"])
        icon_html = f'<span class="text-2xl mr-3">{self.icon}</span>' if self.icon else ''
        title_html = f'<h4 class="font-semibold text-gray-800">{self.title}</h4>' if self.title else ''
        
        return f"""
        <div class="{card_class} rounded-xl p-5 shadow-sm hover:shadow-md transition-all duration-300">
            <div class="flex items-start">
                {icon_html}
                <div class="flex-1">
                    {title_html}
                    <div class="text-gray-600 text-sm mt-2">
                        {content_html}
                    </div>
                </div>
            </div>
        </div>
        """
