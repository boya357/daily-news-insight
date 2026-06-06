"""
特殊组件 - RiskAlert, QuoteBlock, Timeline, CatalystTag, ButtonGroup
升级为高级感设计
"""
from .base import Component
from core.config import COLORS


class RiskAlert(Component):
    """
    风险提示组件
    """
    
    def __init__(self, level: str, text: str, title: str = None):
        super().__init__()
        self.level = level  # high, medium, low
        self.text = text
        self.title = title or "风险提示"
    
    def render(self) -> str:
        level_configs = {
            "high": {
                "bg": "bg-gradient-to-r from-red-50 to-rose-50",
                "border": "border-red-200",
                "text": "text-red-700",
                "icon": "⚠️",
                "accent": "bg-red-500"
            },
            "medium": {
                "bg": "bg-gradient-to-r from-amber-50 to-orange-50",
                "border": "border-amber-200",
                "text": "text-amber-700",
                "icon": "⚡",
                "accent": "bg-amber-500"
            },
            "low": {
                "bg": "bg-gradient-to-r from-blue-50 to-indigo-50",
                "border": "border-blue-200",
                "text": "text-blue-700",
                "icon": "ℹ️",
                "accent": "bg-blue-500"
            }
        }
        
        config = level_configs.get(self.level, level_configs["medium"])
        
        return f"""
        <div class="{config['bg']} border {config['border']} rounded-xl p-5 flex items-start shadow-sm">
            <div class="flex-shrink-0 mr-4">
                <span class="text-2xl">{config['icon']}</span>
            </div>
            <div class="flex-1">
                <h4 class="font-bold {config['text']} mb-2">{self.title}</h4>
                <p class="text-gray-700 text-sm leading-relaxed">{self.text}</p>
            </div>
        </div>
        """


class QuoteBlock(Component):
    """
    引用块组件
    """
    
    def __init__(self, text: str, author: str = None, source: str = None):
        super().__init__()
        self.text = text
        self.author = author
        self.source = source
    
    def render(self) -> str:
        author_html = f'<p class="text-gray-600 text-sm mt-3 italic">— {self.author}</p>' if self.author else ''
        source_html = f'<p class="text-gray-400 text-xs mt-1">{self.source}</p>' if self.source else ''
        
        return f"""
        <div class="bg-gradient-to-r from-indigo-50/80 to-purple-50/80 border-l-4 border-indigo-400 rounded-r-xl p-6 my-4">
            <p class="text-gray-700 leading-relaxed italic text-lg">"{self.text}"</p>
            {author_html}
            {source_html}
        </div>
        """


class Timeline(Component):
    """
    时间线组件
    """
    
    def __init__(self, items: list, title: str = None):
        super().__init__()
        self.items = items  # [{time, title, content, type?}, ...]
        self.title = title
    
    def render(self) -> str:
        items_html = ""
        
        type_colors = {
            "default": "bg-gray-400",
            "primary": "bg-indigo-500",
            "success": "bg-green-500",
            "warning": "bg-amber-500",
            "danger": "bg-red-500"
        }
        
        for i, item in enumerate(self.items):
            item_type = item.get("type", "default")
            dot_color = type_colors.get(item_type, type_colors["default"])
            is_last = i == len(self.items) - 1
            
            line_html = '' if is_last else '<div class="absolute left-[11px] top-6 bottom-0 w-0.5 bg-gray-200"></div>'
            
            items_html += f"""
            <div class="relative pl-8 pb-6 last:pb-0">
                {line_html}
                <div class="absolute left-0 top-1 w-6 h-6 rounded-full {dot_color} flex items-center justify-center ring-4 ring-white shadow-sm">
                    <div class="w-2 h-2 rounded-full bg-white"></div>
                </div>
                <div class="bg-white rounded-xl p-4 border border-gray-100 shadow-sm">
                    <div class="flex items-center justify-between mb-2">
                        <h4 class="font-semibold text-gray-800">{item['title']}</h4>
                        <span class="text-xs text-gray-500 bg-gray-100 px-2 py-1 rounded-full">{item['time']}</span>
                    </div>
                    <p class="text-gray-600 text-sm leading-relaxed">{item['content']}</p>
                </div>
            </div>
            """
        
        title_html = f'<h3 class="text-lg font-bold text-gray-800 mb-6">{self.title}</h3>' if self.title else ''
        
        return f"""
        <div class="bg-white/80 rounded-2xl p-6 border border-gray-100 shadow-sm">
            {title_html}
            <div class="relative">
                {items_html}
            </div>
        </div>
        """


class CatalystTag(Component):
    """
    催化剂标签组件
    """
    
    def __init__(self, tags: list, title: str = None):
        super().__init__()
        self.tags = tags
        self.title = title or "核心催化剂"
    
    def render(self) -> str:
        tags_html = "".join(
            f'<span class="inline-block px-4 py-2 m-1 rounded-full text-sm font-medium bg-gradient-to-r from-indigo-500 to-purple-500 text-white shadow-sm hover:shadow-md transition-shadow">{tag}</span>'
            for tag in self.tags
        )
        
        return f"""
        <div class="bg-gradient-to-br from-indigo-50/80 to-purple-50/80 rounded-2xl p-6 border border-indigo-100">
            <h4 class="font-bold text-indigo-800 mb-4 flex items-center">
                <span class="mr-2">⭐</span>
                {self.title}
            </h4>
            <div class="flex flex-wrap -m-1">
                {tags_html}
            </div>
        </div>
        """


class ButtonGroup(Component):
    """
    按钮组组件
    """
    
    def __init__(self, buttons: list):
        super().__init__()
        self.buttons = buttons  # [{text, href, variant?}, ...]
    
    def render(self) -> str:
        variants = {
            "primary": "bg-gradient-to-r from-indigo-500 to-purple-500 text-white hover:from-indigo-600 hover:to-purple-600 shadow-md hover:shadow-lg",
            "secondary": "bg-white text-gray-700 border border-gray-200 hover:bg-gray-50",
            "outline": "bg-transparent border-2 border-white text-white hover:bg-white/10",
        }
        
        buttons_html = ""
        for btn in self.buttons:
            variant = btn.get("variant", "secondary")
            btn_class = variants.get(variant, variants["secondary"])
            href = btn.get("href", "#")
            target = 'target="_blank"' if btn.get("external", False) else ''
            
            buttons_html += f"""
            <a href="{href}" {target} class="inline-flex items-center px-5 py-2.5 rounded-xl font-medium text-sm transition-all duration-300 {btn_class}">
                {btn['text']}
            </a>
            """
        
        return f"""
        <div class="flex flex-wrap gap-3">
            {buttons_html}
        </div>
        """
