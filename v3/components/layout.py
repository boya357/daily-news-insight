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
                "shadow": "0 4px 16px rgba(0, 0, 0, 0.04), 0 1px 0 rgba(255, 255, 255, 0.8) inset, 0 -1px 0 rgba(0, 0, 0, 0.02) inset",
                "title_color": "#1f2937",
            },
            "highlight": {
                "bg": "linear-gradient(135deg, #f0f4ff 0%, #f5f3ff 100%)",
                "padding": "28px",
                "border": "1px solid rgba(79, 70, 229, 0.1)",
                "radius": "20px",
                "shadow": "0 4px 16px rgba(79, 70, 229, 0.08), 0 1px 0 rgba(255, 255, 255, 0.6) inset",
                "title_color": "#1f2937",
            },
            "dark": {
                "bg": "linear-gradient(135deg, rgba(15, 23, 42, 0.95) 0%, rgba(30, 41, 59, 0.95) 100%)",
                "padding": "28px",
                "border": "1px solid rgba(255, 255, 255, 0.1)",
                "radius": "20px",
                "shadow": "0 8px 32px rgba(0, 0, 0, 0.3), 0 1px 0 rgba(255, 255, 255, 0.05) inset",
                "title_color": "white",
            },
            "subtle": {
                "bg": "transparent",
                "padding": "0",
                "border": "none",
                "radius": "0",
                "shadow": "none",
                "title_color": "#1f2937",
            },
        }
        
        v = variants.get(self.variant, variants["default"])
        
        # 更新标题颜色
        if self.title:
            title_html = title_html.replace(
                'color: #1f2937;',
                f'color: {v["title_color"]};'
            )
        
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
    导航栏组件 - 全站统一glass-nav玻璃态风格
    与首页标准完全一致
    """
    
    # 导航项配置（从core.config导入，单一数据源）
    from core.config import NAV_ITEMS as _NAV_ITEMS
    NAV_ITEMS = _NAV_ITEMS
    
    def __init__(self, active_key: str = "index"):
        super().__init__()
        self.active_key = active_key
    
    @classmethod
    def get_css(cls):
        """获取导航栏CSS样式 - glass-nav玻璃态风格"""
        return """
        <style>
            /* Glass-Nav 玻璃态导航栏 */
            .glass-nav {
                position: fixed;
                top: 0;
                left: 0;
                right: 0;
                z-index: 2147483647 !important;
                background: rgba(0, 0, 0, 0.3);
                backdrop-filter: blur(20px);
                -webkit-backdrop-filter: blur(20px);
                border-bottom: 1px solid rgba(255, 255, 255, 0.1);
                transition: background 0.3s ease;
                isolation: isolate !important;
                pointer-events: auto !important;
            }
            
            .glass-nav.scrolled {
                background: rgba(0, 0, 0, 0.7);
            }
            
            .glass-nav * {
                position: relative;
                z-index: 2147483647 !important;
                pointer-events: auto !important;
            }
            
            .glass-nav-inner {
                max-width: 80rem;
                margin: 0 auto;
                padding: 0 1rem;
                height: 60px;
                display: flex;
                align-items: center;
                justify-content: space-between;
            }
            
            .glass-nav-logo {
                display: flex;
                align-items: center;
                gap: 12px;
                text-decoration: none;
            }
            
            .glass-nav-logo-icon {
                width: 32px;
                height: 32px;
                border-radius: 8px;
                background: linear-gradient(135deg, #6366f1 0%, #a855f7 100%);
                display: flex;
                align-items: center;
                justify-content: center;
                font-size: 14px;
            }
            
            .glass-nav-logo-text {
                color: white;
                font-weight: 700;
                font-size: 18px;
            }
            
            .glass-nav-links {
                display: flex;
                align-items: center;
                gap: 4px;
                flex-wrap: wrap;
            }
            
            .glass-nav-link {
                padding: 6px 12px;
                border-radius: 8px;
                text-decoration: none;
                font-size: 14px;
                font-weight: 500;
                color: rgba(255, 255, 255, 0.8);
                transition: all 0.2s ease;
            }
            
            .glass-nav-link:hover {
                color: white;
                background: rgba(255, 255, 255, 0.1);
            }
            
            .glass-nav-link.active {
                color: white;
                background: rgba(255, 255, 255, 0.15);
            }
            
            .hamburger-btn {
                display: none;
                background: rgba(255, 255, 255, 0.1);
                border: none;
                width: 36px;
                height: 36px;
                border-radius: 8px;
                cursor: pointer;
                font-size: 16px;
                color: white;
                align-items: center;
                justify-content: center;
            }
            
            /* 移动端菜单 - 玻璃态深色 */
            .mobile-menu {
                display: none;
                position: fixed;
                top: 0;
                left: 0;
                right: 0;
                bottom: 0;
                background: rgba(15, 23, 42, 0.95);
                backdrop-filter: blur(20px);
                z-index: 2147483646;
                flex-direction: column;
                padding: 80px 24px 24px;
            }
            
            .mobile-menu.show {
                display: flex;
            }
            
            .mobile-menu-item {
                padding: 14px 16px;
                border-radius: 10px;
                text-decoration: none;
                font-size: 16px;
                font-weight: 500;
                color: rgba(255, 255, 255, 0.8);
                margin-bottom: 4px;
                display: flex;
                align-items: center;
                gap: 12px;
            }
            
            .mobile-menu-item:hover {
                color: white;
                background: rgba(255, 255, 255, 0.1);
            }
            
            .mobile-menu-item.active {
                color: white;
                background: rgba(255, 255, 255, 0.15);
            }
            
            .close-menu-btn {
                position: absolute;
                top: 16px;
                right: 16px;
                background: rgba(255, 255, 255, 0.1);
                border: none;
                width: 36px;
                height: 36px;
                border-radius: 8px;
                cursor: pointer;
                font-size: 16px;
                color: white;
            }
            
            @media (max-width: 768px) {
                .glass-nav-links {
                    display: none;
                }
                .hamburger-btn {
                    display: flex;
                }
            }
        </style>
        """
    
    def render(self) -> str:
        # 构建导航链接（与首页一致，纯文字无emoji图标）
        links_html = ""
        for item in self.NAV_ITEMS:
            active_class = "active" if item["key"] == self.active_key else ""
            links_html += f'\n            <a href="{item["path"]}" class="glass-nav-link {active_class}">{item["label"]}</a>'
        
        # 移动端菜单项
        mobile_links_html = ""
        for item in self.NAV_ITEMS:
            active_class = "active" if item["key"] == self.active_key else ""
            mobile_links_html += f'\n            <a href="{item["path"]}" class="mobile-menu-item {active_class}" onclick="toggleMenu()">{item["label"]}</a>'
        
        return f"""        <nav class="glass-nav">
            <div class="glass-nav-inner">
                <a href="/daily-news-insight/index.html" class="glass-nav-logo">
                    <div class="glass-nav-logo-icon">📊</div>
                    <span class="glass-nav-logo-text">投资研究中心</span>
                </a>
                <div class="glass-nav-links">
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
            }}
            
            // 导航栏滚动加深效果
            window.addEventListener('scroll', function() {{
                const nav = document.querySelector('.glass-nav');
                if (nav) {{
                    if (window.scrollY > 50) {{
                        nav.classList.add('scrolled');
                    }} else {{
                        nav.classList.remove('scrolled');
                    }}
                }}
            }});
        </script>
        """



class SubCard(Component):
    """
    子卡片组件 - 用于在Section内部做嵌套卡片，增强层次感
    浅灰背景 + 边框 + 圆角，营造大卡套小卡的视觉效果
    """
    
    def __init__(self, content=None, title=None, icon=None, variant="default",
                 subtitle=None, footer=None, extra=None):
        super().__init__()
        self.content = content
        self.title = title
        self.icon = icon
        self.variant = variant
        self.subtitle = subtitle
        self.footer = footer
        self.extra = extra
    
    def render(self):
        from .icons import icon_svg
        
        # 头部
        header_html = ""
        if self.title:
            icon_html = ""
            if self.icon:
                icon_html = (
                    '<div style="width: 32px; height: 32px; '
                    'background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%); '
                    'border-radius: 10px; display: flex; align-items: center; '
                    'justify-content: center; margin-right: 12px; flex-shrink: 0;'
                    'box-shadow: 0 2px 6px rgba(99, 102, 241, 0.25);">' +
                    icon_svg(self.icon, 16, "white") +
                    '</div>'
                )
            
            subtitle_html = ''
            if self.subtitle:
                subtitle_html = (
                    '<div style="font-size: 12px; color: #9ca3af; margin-top: 2px;">' +
                    self.subtitle + '</div>'
                )
            
            extra_html = ''
            if self.extra:
                extra_content = self.extra.render() if hasattr(self.extra, "render") else str(self.extra)
                extra_html = '<div style="margin-left: auto;">' + extra_content + '</div>'
            
            header_html = (
                '<div style="display: flex; align-items: center; margin-bottom: 14px;">' +
                icon_html +
                '<div style="flex: 1; min-width: 0;">' +
                '<h4 style="font-size: 15px; font-weight: 600; color: #374151; margin: 0;">' +
                self.title + '</h4>' +
                subtitle_html +
                '</div>' +
                extra_html +
                '</div>'
            )
        
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
            footer_html = (
                '<div style="margin-top: 14px; padding-top: 12px; border-top: 1px solid #e5e7eb;">' +
                footer_content + '</div>'
            )
        
        # 变体样式
        variants = {
            "default": {
                "bg": "#f9fafb",
                "padding": "18px 20px",
                "border": "1px solid rgba(0, 0, 0, 0.04)",
                "radius": "14px",
                "shadow": "0 1px 2px rgba(0, 0, 0, 0.02), 0 1px 0 rgba(255, 255, 255, 0.8) inset",
            },
            "primary": {
                "bg": "linear-gradient(135deg, #eff6ff 0%, #f0f4ff 100%)",
                "padding": "18px 20px",
                "border": "1px solid rgba(59, 130, 246, 0.08)",
                "radius": "14px",
                "shadow": "0 1px 2px rgba(59, 130, 246, 0.04), 0 1px 0 rgba(255, 255, 255, 0.6) inset",
            },
            "success": {
                "bg": "linear-gradient(135deg, #f0fdf4 0%, #ecfdf5 100%)",
                "padding": "18px 20px",
                "border": "1px solid rgba(16, 185, 129, 0.08)",
                "radius": "14px",
                "shadow": "0 1px 2px rgba(16, 185, 129, 0.04), 0 1px 0 rgba(255, 255, 255, 0.6) inset",
            },
            "warning": {
                "bg": "linear-gradient(135deg, #fffbeb 0%, #fef3c7 100%)",
                "padding": "18px 20px",
                "border": "1px solid rgba(245, 158, 11, 0.08)",
                "radius": "14px",
                "shadow": "0 1px 2px rgba(245, 158, 11, 0.04), 0 1px 0 rgba(255, 255, 255, 0.6) inset",
            },
            "danger": {
                "bg": "linear-gradient(135deg, #fef2f2 0%, #fee2e2 100%)",
                "padding": "18px 20px",
                "border": "1px solid rgba(239, 68, 68, 0.08)",
                "radius": "14px",
                "shadow": "0 1px 2px rgba(239, 68, 68, 0.04), 0 1px 0 rgba(255, 255, 255, 0.6) inset",
            },
        }
        
        v = variants.get(self.variant, variants["default"])
        
        return (
            '<div style="background: ' + v["bg"] + '; '
            'padding: ' + v["padding"] + '; '
            'border: ' + v["border"] + ';'
            'border-radius: ' + v["radius"] + ';'
            'box-shadow: ' + v["shadow"] + ';'
            'margin-bottom: 12px;">' +
            header_html +
            content_html +
            footer_html +
            '</div>'
        )


class CardGrid(Component):
    """卡片网格组件 - 在Section内排列多个SubCard"""
    def __init__(self, cards, cols=2, gap="16px"):
        super().__init__()
        self.cards = cards
        self.cols = cols
        self.gap = gap
    
    def render(self):
        cards_html = ""
        for card in self.cards:
            if hasattr(card, 'render'):
                c = card.render()
            else:
                c = str(card)
            cards_html += '<div style="min-width: 0;">' + c + '</div>'
        
        min_width = "260px" if self.cols >= 3 else "280px"
        grid_style = 'display: grid; grid-template-columns: repeat(auto-fit, minmax(' + min_width + ', 1fr)); gap: ' + self.gap + '; margin-bottom: 8px;'
        return '<div style="' + grid_style + '">' + cards_html + '</div>'


class DataTable(Component):
    """数据表格组件 - 美观的表格展示，支持不同行的颜色标识"""
    def __init__(self, headers, rows, row_variants=None):
        super().__init__()
        self.headers = headers
        self.rows = rows
        self.row_variants = row_variants or []
    
    def render(self):
        headers_html = ""
        for h in self.headers:
            th_style = "text-align:left;padding:10px 14px;font-weight:600;font-size:13px;color:#374151;background:#f9fafb;border-bottom:2px solid #e5e7eb;"
            headers_html += '<th style="' + th_style + '">' + h + '</th>'
        
        rows_html = ""
        row_styles = {
            "high": "background: linear-gradient(135deg, #fef2f2 0%, #fee2e2 100%); border-left: 3px solid #ef4444;",
            "medium": "background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%); border-left: 3px solid #f59e0b;",
            "low": "background: linear-gradient(135deg, #dcfce7 0%, #bbf7d0 100%); border-left: 3px solid #22c55e;",
            "default": "background: white; border-bottom: 1px solid #f3f4f6;",
            "primary": "background: linear-gradient(135deg, #eff6ff 0%, #dbeafe 100%); border-left: 3px solid #3b82f6;",
            "warning": "background: linear-gradient(135deg, #fff7ed 0%, #fed7aa 100%); border-left: 3px solid #f97316;",
        }
        
        for i, row in enumerate(self.rows):
            variant = self.row_variants[i] if i < len(self.row_variants) else "default"
            row_style = row_styles.get(variant, row_styles["default"])
            cells_html = ""
            for j, cell in enumerate(row):
                align = "text-align:center;" if j > 0 else "text-align:left;"
                td_style = "padding:10px 14px;font-size:13px;color:#4b5563;" + align
                cells_html += '<td style="' + td_style + '">' + str(cell) + '</td>'
            rows_html += '<tr style="' + row_style + '">' + cells_html + '</tr>'
        
        table_style = "width:100%;border-collapse:collapse;font-size:13px;"
        wrapper_style = "overflow-x:auto;border-radius:12px;border:1px solid #e5e7eb;box-shadow:0 1px 3px rgba(0,0,0,0.05);"
        return '<div style="' + wrapper_style + '"><table style="' + table_style + '"><thead><tr>' + headers_html + '</tr></thead><tbody>' + rows_html + '</tbody></table></div>'



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


class SplitLayout(Component):
    """
    左右分栏布局组件 - 实现左右两栏布局
    支持左图右文、左列表右详情等布局
    """
    
    def __init__(self, left=None, right=None, left_width="50%", gap="24px"):
        super().__init__()
        self.left = left
        self.right = right
        self.left_width = left_width
        self.gap = gap
    
    def render(self) -> str:
        left_html = ""
        if self.left is not None:
            if hasattr(self.left, 'render'):
                left_html = self.left.render()
            else:
                left_html = str(self.left)
        
        right_html = ""
        if self.right is not None:
            if hasattr(self.right, 'render'):
                right_html = self.right.render()
            else:
                right_html = str(self.right)
        
        return f'''
        <div style="display: flex; gap: {self.gap}; flex-wrap: wrap;">
            <div style="flex: 0 0 {self.left_width}; min-width: 280px;">
                {left_html}
            </div>
            <div style="flex: 1; min-width: 280px;">
                {right_html}
            </div>
        </div>
        '''


class ChartCard(Component):
    """
    图表卡片组件 - 将图表包装在卡片中，增强层次感
    带标题、描述和底部说明
    """
    
    def __init__(self, chart=None, title: str = None, subtitle: str = None, 
                 footer: str = None, variant: str = "default"):
        super().__init__()
        self.chart = chart
        self.title = title
        self.subtitle = subtitle
        self.footer = footer
        self.variant = variant
    
    def render(self) -> str:
        chart_html = ""
        if self.chart is not None:
            if hasattr(self.chart, 'render'):
                chart_html = self.chart.render()
            else:
                chart_html = str(self.chart)
        
        title_html = ""
        if self.title:
            subtitle_html = f'''
            <div style="font-size: 12px; color: #9ca3af; margin-top: 2px; font-weight: 400;">
                {self.subtitle}
            </div>
            ''' if self.subtitle else ''
            
            title_html = f'''
            <div style="margin-bottom: 16px;">
                <h4 style="font-size: 16px; font-weight: 600; color: #1f2937; margin: 0;">
                    {self.title}
                </h4>
                {subtitle_html}
            </div>
            '''
        
        footer_html = ""
        if self.footer:
            footer_html = f'''
            <div style="margin-top: 12px; padding-top: 12px; border-top: 1px solid #f3f4f6;
                        font-size: 12px; color: #9ca3af; text-align: center;">
                {self.footer}
            </div>
            '''
        
        variants = {
            "default": {
                "bg": "white",
                "padding": "20px",
                "border": "1px solid rgba(0, 0, 0, 0.06)",
                "radius": "16px",
                "shadow": "0 2px 8px rgba(0, 0, 0, 0.04)",
            },
            "primary": {
                "bg": "linear-gradient(135deg, #f0f4ff 0%, #f5f3ff 100%)",
                "padding": "20px",
                "border": "1px solid rgba(79, 70, 229, 0.1)",
                "radius": "16px",
                "shadow": "0 2px 8px rgba(79, 70, 229, 0.06)",
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
            {title_html}
            {chart_html}
            {footer_html}
        </div>
        '''
