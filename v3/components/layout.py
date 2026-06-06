"""
布局组件 - Section, Card, Navbar, Footer等
高级感设计版本
"""
from .base import Component
from core.config import COLORS, SIZES


class Section(Component):
    """
    章节组件 - 用于分隔内容区域
    带精致的标题图标和渐变设计
    """
    
    def __init__(self, title: str = "", content=None, 
                 icon: str = None, variant: str = "default",
                 subtitle: str = None, extra=None):
        super().__init__()
        self.title = title
        self.content = content
        self.icon = icon
        self.variant = variant
        self.subtitle = subtitle
        self.extra = extra  # 右侧额外内容，如徽章等
    
    def render(self) -> str:
        # 标题区域
        title_html = ""
        if self.title:
            from .icons import icon_svg
            
            icon_html = ""
            if self.icon:
                icon_html = f'''
                <div style="width: 40px; height: 40px; 
                            background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%); 
                            border-radius: 12px; display: flex; align-items: center; 
                            justify-content: center; margin-right: 14px; flex-shrink: 0;
                            box-shadow: 0 4px 12px rgba(79, 70, 229, 0.3);">
                    {icon_svg(self.icon, 20, "white")}
                </div>
                '''
            
            subtitle_html = f'''
            <div style="font-size: 13px; color: #9ca3af; margin-top: 2px; font-weight: 400;">
                {self.subtitle}
            </div>
            ''' if self.subtitle else ''
            
            extra_html = f'<div style="margin-left: auto;">{self.extra.render() if hasattr(self.extra, "render") else self.extra}</div>' if self.extra else ''
            
            title_html = f'''
            <div style="display: flex; align-items: center; margin-bottom: 20px;">
                {icon_html}
                <div style="flex: 1; min-width: 0;">
                    <h2 style="font-size: 20px; font-weight: 700; color: #1f2937; 
                               margin: 0; line-height: 1.3;">
                        {self.title}
                    </h2>
                    {subtitle_html}
                </div>
                {extra_html}
            </div>
            '''
        
        # 内容
        content_html = ""
        if self.content is not None:
            if hasattr(self.content, 'render'):
                content_html = self.content.render()
            else:
                content_html = str(self.content)
        
        # 变体样式
        variants = {
            "default": {
                "bg": "white",
                "padding": "28px",
                "border": "1px solid rgba(0, 0, 0, 0.06)",
                "radius": "20px",
                "shadow": "0 4px 16px rgba(0, 0, 0, 0.04)",
            },
            "highlight": {
                "bg": "linear-gradient(135deg, #f0f4ff 0%, #f5f3ff 100%)",
                "padding": "28px",
                "border": "1px solid rgba(79, 70, 229, 0.1)",
                "radius": "20px",
                "shadow": "0 4px 16px rgba(79, 70, 229, 0.08)",
            },
            "subtle": {
                "bg": "transparent",
                "padding": "0",
                "border": "none",
                "radius": "0",
                "shadow": "none",
            },
        }
        
        v = variants.get(self.variant, variants["default"])
        
        return f'''
        <section style="margin-bottom: 32px;">
            {title_html}
            <div style="background: {v["bg"]}; 
                        padding: {v["padding"]}; 
                        border: {v["border"]};
                        border-radius: {v["radius"]};
                        box-shadow: {v["shadow"]};">
                {content_html}
            </div>
        </section>
        '''


class Card(Component):
    """
    卡片组件 - 基础容器
    """
    
    def __init__(self, content=None, title: str = None, 
                 icon: str = None, variant: str = "default",
                 subtitle: str = None, footer=None,
                 extra=None):
        super().__init__()
        self.content = content
        self.title = title
        self.icon = icon
        self.variant = variant
        self.subtitle = subtitle
        self.footer = footer
        self.extra = extra
    
    def render(self) -> str:
        # 头部
        header_html = ""
        if self.title:
            from .icons import icon_svg
            
            icon_html = ""
            if self.icon:
                icon_html = f'''
                <div style="width: 44px; height: 44px; 
                            background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%); 
                            border-radius: 14px; display: flex; align-items: center; 
                            justify-content: center; margin-right: 14px; flex-shrink: 0;
                            box-shadow: 0 4px 12px rgba(79, 70, 229, 0.25);">
                    {icon_svg(self.icon, 22, "white")}
                </div>
                '''
            
            subtitle_html = f'''
            <div style="font-size: 13px; color: #9ca3af; margin-top: 3px;">
                {self.subtitle}
            </div>
            ''' if self.subtitle else ''
            
            extra_html = f'<div style="margin-left: auto;">{self.extra.render() if hasattr(self.extra, "render") else self.extra}</div>' if self.extra else ''
            
            header_html = f'''
            <div style="display: flex; align-items: center; margin-bottom: 18px;">
                {icon_html}
                <div style="flex: 1; min-width: 0;">
                    <h3 style="font-size: 17px; font-weight: 700; color: #1f2937; margin: 0;">
                        {self.title}
                    </h3>
                    {subtitle_html}
                </div>
                {extra_html}
            </div>
            '''
        
        # 内容
        content_html = ""
        if self.content is not None:
            if hasattr(self.content, 'render'):
                content_html = self.content.render()
            else:
                content_html = str(self.content)
        
        # 底部
        footer_html = ""
        if self.footer is not None:
            footer_content = self.footer.render() if hasattr(self.footer, 'render') else str(self.footer)
            footer_html = f'''
            <div style="margin-top: 18px; padding-top: 16px; border-top: 1px solid #f3f4f6;">
                {footer_content}
            </div>
            '''
        
        # 变体样式
        variants = {
            "default": {
                "bg": "white",
                "padding": "24px",
                "border": "1px solid rgba(0, 0, 0, 0.06)",
                "radius": "18px",
                "shadow": "0 4px 12px rgba(0, 0, 0, 0.04)",
            },
            "primary": {
                "bg": "linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%)",
                "padding": "24px",
                "border": "none",
                "radius": "18px",
                "shadow": "0 8px 24px rgba(79, 70, 229, 0.3)",
            },
        }
        
        v = variants.get(self.variant, variants["default"])
        
        return f'''
        <div style="background: {v["bg"]}; 
                    padding: {v["padding"]}; 
                    border: {v["border"]};
                    border-radius: {v["radius"]};
                    box-shadow: {v["shadow"]};
                    transition: all 0.3s ease;"
             onmouseover="this.style.transform='translateY(-2px)'; this.style.boxShadow='0 8px 24px rgba(0, 0, 0, 0.08)';"
             onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='{v["shadow"]}';">
            {header_html}
            {content_html}
            {footer_html}
        </div>
        '''


class HighlightBox(Component):
    """
    高亮提示框 - 用于重点内容、今日焦点等
    """
    
    def __init__(self, content: str, icon: str = "zap", 
                 variant: str = "warning", title: str = None):
        super().__init__()
        self.content = content
        self.icon = icon
        self.variant = variant
        self.title = title
    
    def render(self) -> str:
        variants = {
            "warning": {
                "bg": "linear-gradient(135deg, #fffbeb 0%, #fef3c7 100%)",
                "border": "rgba(245, 158, 11, 0.2)",
                "icon_bg": "linear-gradient(135deg, #f59e0b 0%, #ea580c 100%)",
                "text": "#92400e",
            },
            "info": {
                "bg": "linear-gradient(135deg, #eff6ff 0%, #dbeafe 100%)",
                "border": "rgba(59, 130, 246, 0.2)",
                "icon_bg": "linear-gradient(135deg, #3b82f6 0%, #2563eb 100%)",
                "text": "#1e40af",
            },
            "success": {
                "bg": "linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%)",
                "border": "rgba(16, 185, 129, 0.2)",
                "icon_bg": "linear-gradient(135deg, #10b981 0%, #059669 100%)",
                "text": "#065f46",
            },
            "danger": {
                "bg": "linear-gradient(135deg, #fef2f2 0%, #fee2e2 100%)",
                "border": "rgba(239, 68, 68, 0.2)",
                "icon_bg": "linear-gradient(135deg, #ef4444 0%, #dc2626 100%)",
                "text": "#991b1b",
            },
            "primary": {
                "bg": "linear-gradient(135deg, #f0f4ff 0%, #ede9fe 100%)",
                "border": "rgba(79, 70, 229, 0.2)",
                "icon_bg": "linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%)",
                "text": "#3730a3",
            },
        }
        
        v = variants.get(self.variant, variants["primary"])
        
        from .icons import icon_svg
        
        title_html = f'<div style="font-weight: 600; margin-bottom: 4px;">{self.title}</div>' if self.title else ''
        
        return f'''
        <div style="background: {v["bg"]}; 
                    border: 1px solid {v["border"]};
                    border-radius: 14px; 
                    padding: 16px 20px;
                    display: flex; align-items: center;">
            <div style="width: 36px; height: 36px; 
                        background: {v["icon_bg"]};
                        border-radius: 10px; display: flex; align-items: center; 
                        justify-content: center; margin-right: 14px; flex-shrink: 0;
                        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);">
                {icon_svg(self.icon, 18, "white")}
            </div>
            <div style="flex: 1; font-size: 14px; color: {v["text"]}; line-height: 1.5; font-weight: 500;">
                {title_html}
                {self.content}
            </div>
        </div>
        '''


class Navbar(Component):
    """
    导航栏组件 - 全站统一导航
    """
    
    # 导航项配置
    NAV_ITEMS = [
        {"key": "index", "label": "首页", "icon": "🏠", "path": "/daily-news-insight/index.html"},
        {"key": "daily", "label": "日报", "icon": "📰", "path": "/daily-news-insight/daily/latest.html"},
        {"key": "intraday", "label": "盘中", "icon": "📈", "path": "/daily-news-insight/intraday/latest.html"},
        {"key": "aftermarket", "label": "盘后", "icon": "📉", "path": "/daily-news-insight/aftermarket/latest.html"},
        {"key": "industry_chain", "label": "产业链", "icon": "🔗", "path": "/daily-news-insight/industry_chain/latest.html"},
        {"key": "weekly_review", "label": "周复盘", "icon": "📋", "path": "/daily-news-insight/weekly_review/latest.html"},
        {"key": "weekly_outlook", "label": "周三前瞻", "icon": "🔮", "path": "/daily-news-insight/weekly_outlook/latest.html"},
        {"key": "weekend_express", "label": "周末速递", "icon": "📦", "path": "/daily-news-insight/周末速递/latest.html"},
        {"key": "tomorrow_catalyst", "label": "明日催化", "icon": "⏰", "path": "/daily-news-insight/明日催化剂/latest.html"},
        {"key": "s_level_catalyst", "label": "S级催化", "icon": "⭐", "path": "/daily-news-insight/s级催化扫描/latest.html"},
        {"key": "monthly", "label": "月报", "icon": "🗓️", "path": "/daily-news-insight/monthly/latest.html"},
    ]
    
    def __init__(self, active_key: str = "index"):
        super().__init__()
        self.active_key = active_key
    
    @classmethod
    def get_css(cls):
        """获取导航栏CSS样式"""
        return '''
        <style>
            .navbar {
                position: fixed;
                top: 0;
                left: 0;
                right: 0;
                z-index: 1000;
                background: rgba(255, 255, 255, 0.9);
                backdrop-filter: blur(20px);
                -webkit-backdrop-filter: blur(20px);
                border-bottom: 1px solid rgba(0, 0, 0, 0.06);
            }
            .navbar-inner {
                max-width: 64rem;
                margin: 0 auto;
                padding: 0 24px;
                height: 64px;
                display: flex;
                align-items: center;
                justify-content: space-between;
            }
            .navbar-logo {
                font-size: 18px;
                font-weight: 700;
                background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                background-clip: text;
                display: flex;
                align-items: center;
            }
            .navbar-logo-icon {
                font-size: 22px;
                margin-right: 8px;
            }
            .navbar-links {
                display: flex;
                align-items: center;
                gap: 4px;
            }
            .nav-link {
                padding: 8px 14px;
                border-radius: 10px;
                text-decoration: none;
                font-size: 13px;
                font-weight: 500;
                color: #6b7280;
                transition: all 0.2s ease;
                display: flex;
                align-items: center;
                gap: 6px;
            }
            .nav-link:hover {
                background: #f3f4f6;
                color: #374151;
            }
            .nav-link.active {
                background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%);
                color: white;
                box-shadow: 0 4px 12px rgba(79, 70, 229, 0.3);
            }
            .hamburger-btn {
                display: none;
                background: #f3f4f6;
                border: none;
                width: 40px;
                height: 40px;
                border-radius: 10px;
                cursor: pointer;
                font-size: 18px;
                align-items: center;
                justify-content: center;
            }
            .mobile-menu {
                display: none;
                position: fixed;
                top: 0;
                left: 0;
                right: 0;
                bottom: 0;
                background: rgba(255, 255, 255, 0.98);
                backdrop-filter: blur(20px);
                z-index: 999;
                flex-direction: column;
                padding: 80px 24px 24px;
            }
            .mobile-menu.show {
                display: flex;
            }
            .mobile-menu-item {
                padding: 16px 20px;
                border-radius: 12px;
                text-decoration: none;
                font-size: 16px;
                font-weight: 500;
                color: #374151;
                margin-bottom: 4px;
                display: flex;
                align-items: center;
                gap: 12px;
            }
            .mobile-menu-item.active {
                background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%);
                color: white;
            }
            .close-menu-btn {
                position: absolute;
                top: 16px;
                right: 16px;
                background: #f3f4f6;
                border: none;
                width: 40px;
                height: 40px;
                border-radius: 10px;
                cursor: pointer;
                font-size: 18px;
            }
            @media (max-width: 768px) {
                .navbar-links {
                    display: none;
                }
                .hamburger-btn {
                    display: flex;
                }
                body {
                    padding-top: 64px !important;
                }
            }
        </style>
        '''
    
    def render(self) -> str:
        # 构建导航链接
        links_html = ""
        for item in self.NAV_ITEMS:
            active_class = "active" if item["key"] == self.active_key else ""
            links_html += f'''
            <a href="{item["path"]}" class="nav-link {active_class}">
                <span>{item["icon"]}</span>
                <span>{item["label"]}</span>
            </a>
            '''
        
        # 移动端菜单项
        mobile_links_html = ""
        for item in self.NAV_ITEMS:
            active_class = "active" if item["key"] == self.active_key else ""
            mobile_links_html += f'''
            <a href="{item["path"]}" class="mobile-menu-item {active_class}" onclick="toggleMenu()">
                <span>{item["icon"]}</span>
                <span>{item["label"]}</span>
            </a>
            '''
        
        return f'''
        <nav class="navbar">
            <div class="navbar-inner">
                <a href="/daily-news-insight/index.html" class="navbar-logo">
                    <span class="navbar-logo-icon">📊</span>
                    <span>投资研究中心</span>
                </a>
                <div class="navbar-links">
                    {links_html}
                </div>
                <button class="hamburger-btn" onclick="toggleMenu()">
                    ☰
                </button>
            </div>
        </nav>
        
        <!-- 移动端菜单 -->
        <div class="mobile-menu" id="mobileMenu">
            <button class="close-menu-btn" onclick="toggleMenu()">✕</button>
            {mobile_links_html}
        </div>
        
        <script>
            function toggleMenu() {{
                const menu = document.getElementById('mobileMenu');
                menu.classList.toggle('show');
                document.body.style.overflow = menu.classList.contains('show') ? 'hidden' : '';
            }}
        </script>
        '''


class Footer(Component):
    """
    页脚组件
    """
    
    def __init__(self):
        super().__init__()
    
    def render(self) -> str:
        return f'''
        <footer style="max-width: 64rem; margin: 40px auto 0; 
                     padding: 32px 24px;
                     border-top: 1px solid rgba(0, 0, 0, 0.06);">
            <div style="text-align: center; color: #9ca3af; font-size: 13px; line-height: 1.8;">
                <div style="margin-bottom: 8px;">
                    <span style="background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%); 
                               -webkit-background-clip: text; -webkit-text-fill-color: transparent;
                               font-weight: 700; font-size: 16px;">投资研究中心</span>
                </div>
                <div>AI驱动 · 数据驱动 · 价值投资</div>
                <div style="margin-top: 8px; font-size: 12px;">
                    投资有风险，入市需谨慎。本报告仅供参考，不构成投资建议。
                </div>
            </div>
        </footer>
        '''
