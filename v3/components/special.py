"""
特殊组件 - RiskAlert, Timeline, CatalystTag, QuoteBlock等
高级感设计版本
"""
from .base import Component
from core.config import COLORS


class RiskAlert(Component):
    """
    风险提示组件
    """
    
    def __init__(self, text: str, level: str = "warning", title: str = None):
        super().__init__()
        self.text = text
        self.level = level
        self.title = title or "风险提示"
    
    def render(self) -> str:
        levels = {
            "warning": {
                "bg": "linear-gradient(135deg, rgba(245,158,11,0.12) 0%, rgba(234,88,12,0.08) 100%)",
                "border": "rgba(245, 158, 11, 0.2)",
                "icon": "⚠️",
                "title_color": "#fbbf24",
                "text_color": "#b45309",
            },
            "danger": {
                "bg": "linear-gradient(135deg, rgba(239,68,68,0.12) 0%, rgba(220,38,38,0.08) 100%)",
                "border": "rgba(239, 68, 68, 0.2)",
                "icon": "🚨",
                "title_color": "#f87171",
                "text_color": "#b91c1c",
            },
            "info": {
                "bg": "linear-gradient(135deg, #eff6ff 0%, #dbeafe 100%)",
                "border": "rgba(59, 130, 246, 0.2)",
                "icon": "ℹ️",
                "title_color": "#60a5fa",
                "text_color": "#1d4ed8",
            },
        }
        
        v = levels.get(self.level, levels["warning"])
        
        return f'''
        <div style="background: {v["bg"]}; 
                    border: 1px solid {v["border"]};
                    border-radius: 14px; 
                    padding: 18px 20px;
                    margin: 16px 0;">
            <div style="display: flex; align-items: flex-start;">
                <span style="font-size: 20px; margin-right: 12px; flex-shrink: 0; margin-top: -2px;">
                    {v["icon"]}
                </span>
                <div style="flex: 1;">
                    <div style="font-weight: 600; color: {v["title_color"]}; 
                               font-size: 14px; margin-bottom: 6px;">
                        {self.title}
                    </div>
                    <div style="color: {v["text_color"]}; 
                               font-size: 13px; line-height: 1.6;">
                        {self.text}
                    </div>
                </div>
            </div>
        </div>
        '''


class Timeline(Component):
    """
    时间线组件 - 展示重要事件时间线
    """
    
    def __init__(self, items: list):
        super().__init__()
        self.items = items  # [{time, title, content, type}]
    
    def render(self) -> str:
        type_colors = {
            "primary": "#4f46e5",
            "success": "#10b981",
            "warning": "#f59e0b",
            "danger": "#ef4444",
            "info": "#3b82f6",
        }
        
        items_html = ""
        for i, item in enumerate(self.items):
            item_type = item.get("type", "primary")
            color = type_colors.get(item_type, type_colors["primary"])
            is_last = i == len(self.items) - 1
            
            line_html = ''
            if not is_last:
                line_html = f'''
                <div style="position: absolute; left: 9px; top: 28px; 
                           width: 2px; height: calc(100% - 8px); 
                           background: linear-gradient(to bottom, {color}, #e5e7eb);">
                </div>
                '''
            
            items_html += f'''
            <div style="position: relative; padding-left: 32px; padding-bottom: 24px;">
                {line_html}
                <div style="position: absolute; left: 0; top: 4px; 
                           width: 20px; height: 20px; 
                           background: {color};
                           border-radius: 50%;
                           border: 3px solid white;
                           box-shadow: 0 2px 8px rgba(0, 0, 0, 0.15);
                           z-index: 1;">
                </div>
                <div style="font-size: 12px; color: #94a3b8; font-weight: 500; 
                           margin-bottom: 4px;">
                    {item.get("time", "")}
                </div>
                <div style="font-size: 15px; font-weight: 600; color: #e2e8f0; 
                           margin-bottom: 6px;">
                    {item.get("title", "")}
                </div>
                <div style="font-size: 13px; color: #94a3b8; line-height: 1.6;">
                    {item.get("content", "")}
                </div>
            </div>
            '''
        
        return f'''
        <div style="padding: 8px 0;">
            {items_html}
        </div>
        '''


class CatalystTag(Component):
    """
    催化标签 - 用于展示题材、概念等
    """
    
    def __init__(self, text: str, hot: bool = False):
        super().__init__()
        self.text = text
        self.hot = hot
    
    def render(self) -> str:
        if self.hot:
            style = '''
            background: linear-gradient(135deg, #ef4444 0%, #dc2626 100%);
            color: white;
            box-shadow: 0 2px 8px rgba(239, 68, 68, 0.3);
            '''
        else:
            style = '''
            background: linear-gradient(135deg, rgba(79,70,229,0.15) 0%, rgba(124,58,237,0.1) 100%);
            color: #4f46e5;
            border: 1px solid rgba(79, 70, 229, 0.15);
            '''
        
        return f'''
        <span style="display: inline-block; padding: 6px 14px; 
                    border-radius: 20px; font-size: 13px; font-weight: 500;
                    margin: 4px 8px 4px 0;
                    transition: all 0.2s ease;
                    {style}"
             onmouseover="this.style.transform='translateY(-1px)';"
             onmouseout="this.style.transform='translateY(0)';">
            {self.text}
        </span>
        '''


class QuoteBlock(Component):
    """
    引用块 - 用于引用重要观点或金句
    """
    
    def __init__(self, text: str, author: str = None, source: str = None):
        super().__init__()
        self.text = text
        self.author = author
        self.source = source
    
    def render(self) -> str:
        author_html = ""
        if self.author:
            source_text = f' · {self.source}' if self.source else ''
            author_html = f'''
            <div style="text-align: right; font-size: 13px; color: #9ca3af; 
                       margin-top: 12px; font-style: italic;">
                —— {self.author}{source_text}
            </div>
            '''
        
        return f'''
        <div style="background: linear-gradient(135deg, rgba(168,85,247,0.1) 0%, rgba(139,92,246,0.08) 100%); 
                    border-left: 4px solid #8b5cf6;
                    border-radius: 0 12px 12px 0; 
                    padding: 20px 24px;
                    margin: 16px 0;">
            <div style="font-size: 15px; color: #581c87; line-height: 1.8; 
                       font-weight: 500; font-style: italic;">
                "{self.text}"
            </div>
            {author_html}
        </div>
        '''


class SectionHeader(Component):
    """
    分组标题 - 用于在卡片内部分组内容
    """
    
    def __init__(self, title: str, icon: str = None, badge: str = None,
                 badge_variant: str = "primary"):
        super().__init__()
        self.title = title
        self.icon = icon
        self.badge = badge
        self.badge_variant = badge_variant
    
    def render(self) -> str:
        from .icons import icon_svg
        from .data import Badge
        
        icon_html = ""
        if self.icon:
            icon_html = f'''
            <div style="width: 20px; height: 20px; margin-right: 8px;
                       display: flex; align-items: center; justify-content: center;">
                {icon_svg(self.icon, 16, "#6b7280")}
            </div>
            '''
        
        badge_html = ""
        if self.badge:
            badge_html = f'<div style="margin-left: 10px;">{Badge(self.badge, self.badge_variant).render()}</div>'
        
        return f'''
        <div style="display: flex; align-items: center; 
                   margin-bottom: 14px; margin-top: 20px;">
            {icon_html}
            <h4 style="font-size: 15px; font-weight: 600; color: #e2e8f0; 
                      margin: 0; display: flex; align-items: center;">
                {self.title}
                {badge_html}
            </h4>
        </div>
        '''


class NewsItem(Component):
    """
    新闻条目组件 - 用于新闻列表
    """
    
    def __init__(self, title: str, content: str = None, 
                 time: str = None, source: str = None,
                 tag: str = None, tag_variant: str = "default",
                 important: bool = False):
        super().__init__()
        self.title = title
        self.content = content
        self.time = time
        self.source = source
        self.tag = tag
        self.tag_variant = tag_variant
        self.important = important
    
    def render(self) -> str:
        from .data import Badge
        
        tag_html = ""
        if self.tag:
            tag_html = f'<div style="margin-right: 10px;">{Badge(self.tag, self.tag_variant).render()}</div>'
        
        meta_html = ""
        if self.time or self.source:
            parts = []
            if self.time:
                parts.append(self.time)
            if self.source:
                parts.append(self.source)
            meta_html = f'''
            <div style="font-size: 12px; color: #9ca3af; margin-top: 6px;">
                {" · ".join(parts)}
            </div>
            '''
        
        content_html = ""
        if self.content:
            content_html = f'''
            <div style="font-size: 13px; color: #94a3b8; line-height: 1.6; 
                       margin-top: 8px;">
                {self.content}
            </div>
            '''
        
        title_weight = "700" if self.important else "600"
        title_color = "#1f2937" if self.important else "#374151"
        
        return f'''
        <div style="padding: 14px 16px; 
                    border-radius: 12px;
                    background: rgba(255,255,255,0.04);
                    margin-bottom: 10px;
                    transition: all 0.2s ease;"
             onmouseover="this.style.background='rgba(255,255,255,0.08)';"
             onmouseout="this.style.background='rgba(255,255,255,0.04)';">
            <div style="display: flex; align-items: flex-start;">
                {tag_html}
                <div style="flex: 1; min-width: 0;">
                    <div style="font-size: 14px; font-weight: {title_weight}; 
                               color: {title_color}; line-height: 1.5;">
                        {self.title}
                    </div>
                    {content_html}
                    {meta_html}
                </div>
            </div>
        </div>
        '''


class ButtonGroup(Component):
    """
    按钮组组件 - 用于操作按钮组
    """
    
    def __init__(self, buttons: list = None):
        super().__init__()
        self.buttons = buttons or []  # [{"text": "按钮", "url": "#", "variant": "primary"}, ...]
    
    def render(self) -> str:
        buttons_html = ""
        for btn in self.buttons:
            variant = btn.get("variant", "default")
            text = btn.get("text", "")
            url = btn.get("url", "#")
            
            variants = {
                "primary": "background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%); color: white;",
                "success": "background: linear-gradient(135deg, #10b981 0%, #059669 100%); color: white;",
                "warning": "background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%); color: white;",
                "danger": "background: linear-gradient(135deg, #ef4444 0%, #dc2626 100%); color: white;",
                "default": "background: rgba(255,255,255,0.1); color: #e2e8f0;",
            }
            
            style = variants.get(variant, variants["default"])
            
            buttons_html += f'''
            <a href="{url}" style="
                display: inline-block;
                padding: 10px 20px;
                border-radius: 10px;
                font-size: 14px;
                font-weight: 500;
                text-decoration: none;
                {style}
                transition: all 0.2s ease;
                margin-right: 8px;
            " onmouseover="this.style.opacity='0.9'; this.style.transform='translateY(-1px)';"
               onmouseout="this.style.opacity='1'; this.style.transform='translateY(0)';">
                {text}
            </a>
            '''
        
        return f'''
        <div style="display: flex; align-items: center; flex-wrap: wrap; gap: 8px;">
            {buttons_html}
        </div>
        '''
