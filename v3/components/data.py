"""
数据展示组件 - DataCard, DataGrid, CompareTable, MetricsRow
高级感设计版本
"""
from .base import Component
from core.config import COLORS


class DataCard(Component):
    """
    精致数据卡片 - 展示关键指标
    升级为精美渐变设计，带图标、趋势指示
    """
    
    def __init__(self, title: str, value: str, trend: str = None, 
                 trend_up: bool = True, unit: str = "", 
                 icon: str = None, variant: str = "default",
                 subtitle: str = None):
        super().__init__()
        self.title = title
        self.value = value
        self.trend = trend
        self.trend_up = trend_up
        self.unit = unit
        self.icon = icon
        self.variant = variant
        self.subtitle = subtitle
    
    def render(self) -> str:
        # 趋势样式
        trend_color = "#10b981" if self.trend_up else "#ef4444"
        trend_icon = "↑" if self.trend_up else "↓"
        trend_html = f'''
        <div style="display: flex; align-items: center; color: {trend_color}; 
                    font-size: 13px; font-weight: 600; margin-top: 4px;">
            <span style="margin-right: 2px;">{trend_icon}</span>
            <span>{self.trend}</span>
        </div>
        ''' if self.trend else ''
        
        # 图标
        icon_html = ''
        if self.icon:
            from .icons import icon_svg
            icon_html = f'''
            <div style="width: 40px; height: 40px; 
                        background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%); 
                        border-radius: 12px; display: flex; align-items: center; 
                        justify-content: center; margin-bottom: 12px;">
                {icon_svg(self.icon, 20, "white")}
            </div>
            '''
        
        variants = {
            "default": {
                "bg": "white",
                "border": "rgba(0, 0, 0, 0.06)",
                "value_color": "#1f2937"
            },
            "primary": {
                "bg": "linear-gradient(135deg, #f0f4ff 0%, #f5f3ff 100%)",
                "border": "rgba(79, 70, 229, 0.1)",
                "value_color": "#4f46e5"
            },
            "success": {
                "bg": "linear-gradient(135deg, #f0fdf4 0%, #ecfdf5 100%)",
                "border": "rgba(16, 185, 129, 0.1)",
                "value_color": "#059669"
            },
            "warning": {
                "bg": "linear-gradient(135deg, #fffbeb 0%, #fff7ed 100%)",
                "border": "rgba(245, 158, 11, 0.1)",
                "value_color": "#d97706"
            },
            "danger": {
                "bg": "linear-gradient(135deg, #fef2f2 0%, #fef2f2 100%)",
                "border": "rgba(239, 68, 68, 0.1)",
                "value_color": "#dc2626"
            },
        }
        
        v = variants.get(self.variant, variants["default"])
        
        subtitle_html = f'<div style="font-size: 12px; color: #9ca3af; margin-top: 2px;">{self.subtitle}</div>' if self.subtitle else ''
        
        return f'''
        <div style="background: {v["bg"]}; 
                    border: 1px solid {v["border"]};
                    border-radius: 16px; 
                    padding: 20px; 
                    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
                    transition: all 0.3s ease;
                    cursor: default;"
             onmouseover="this.style.transform='translateY(-2px)'; this.style.boxShadow='0 8px 24px rgba(0, 0, 0, 0.08)';"
             onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 2px 8px rgba(0, 0, 0, 0.04)';">
            {icon_html}
            <div style="font-size: 13px; color: #6b7280; margin-bottom: 6px;">
                {self.title}
            </div>
            <div style="font-size: 24px; font-weight: 700; color: {v["value_color"]}; line-height: 1.2;">
                {self.value}<span style="font-size: 13px; font-weight: 400; color: #9ca3af; margin-left: 2px;">{self.unit}</span>
            </div>
            {subtitle_html}
            {trend_html}
        </div>
        '''


class DataGrid(Component):
    """
    数据卡片网格 - 展示多个数据卡片
    """
    
    def __init__(self, cards: list, cols: int = 4, gap: str = "16px"):
        super().__init__()
        self.cards = cards
        self.cols = cols
        self.gap = gap
    
    def render(self) -> str:
        cards_html = "".join(
            f'<div style="flex: 1; min-width: 0;">{card.render() if hasattr(card, "render") else str(card)}</div>'
            for card in self.cards
        )
        
        return f'''
        <div style="display: flex; gap: {self.gap}; flex-wrap: wrap;">
            {cards_html}
        </div>
        '''


class KeyPoints(Component):
    """
    要点列表组件 - 带图标的要点列表
    类似旧版的 key-points 组件
    """
    
    def __init__(self, points: list, icon: str = "check", icon_color: str = None):
        super().__init__()
        self.points = points
        self.icon = icon
        self.icon_color = icon_color or "#4f46e5"
    
    def render(self) -> str:
        from .icons import icon_svg
        
        points_html = ""
        for i, point in enumerate(self.points):
            border_class = "" if i == len(self.points) - 1 else 'border-bottom: 1px dashed #e5e7eb;'
            
            points_html += f'''
            <div style="display: flex; align-items: flex-start; 
                        padding: 12px 0; {border_class}">
                <div style="width: 22px; height: 22px; 
                            background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%); 
                            border-radius: 6px; display: flex; align-items: center; 
                            justify-content: center; margin-right: 12px; flex-shrink: 0;
                            margin-top: 1px;">
                    {icon_svg("check", 12, "white")}
                </div>
                <div style="flex: 1; font-size: 14px; color: #374151; line-height: 1.6;">
                    {point}
                </div>
            </div>
            '''
        
        return f'''
        <div style="background: white; border-radius: 14px; padding: 4px 16px; 
                    border: 1px solid rgba(0, 0, 0, 0.04);">
            {points_html}
        </div>
        '''


class StockTags(Component):
    """
    股票标签组件 - 展示相关股票/标的
    """
    
    def __init__(self, stocks: list, label: str = "相关标的", 
                 variant: str = "default"):
        super().__init__()
        self.stocks = stocks
        self.label = label
        self.variant = variant
    
    def render(self) -> str:
        from .icons import icon_svg
        
        if self.variant == "gradient":
            tag_style = '''
                background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%);
                color: white;
                box-shadow: 0 2px 8px rgba(79, 70, 229, 0.3);
            '''
        else:
            tag_style = '''
                background: linear-gradient(135deg, #f0f4ff 0%, #f5f3ff 100%);
                color: #4f46e5;
                border: 1px solid rgba(79, 70, 229, 0.15);
            '''
        
        tags_html = ""
        for stock in self.stocks:
            tags_html += f'''
            <span style="display: inline-block; padding: 6px 14px; 
                        border-radius: 20px; font-size: 13px; font-weight: 500;
                        margin: 4px 6px 4px 0;
                        transition: all 0.2s ease;
                        {tag_style}"
                 onmouseover="this.style.transform='translateY(-1px)'; this.style.boxShadow='0 4px 12px rgba(79, 70, 229, 0.25)';"
                 onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 2px 8px rgba(79, 70, 229, 0.1)';">
                {stock}
            </span>
            '''
        
        return f'''
        <div style="padding-top: 16px; border-top: 1px solid #f3f4f6; margin-top: 16px;">
            <div style="display: flex; align-items: center; margin-bottom: 10px;">
                <div style="width: 16px; height: 16px; margin-right: 6px;">
                    {icon_svg("stock", 16, "#6b7280")}
                </div>
                <span style="font-size: 13px; color: #6b7280; font-weight: 500;">
                    {self.label}
                </span>
            </div>
            <div style="display: flex; flex-wrap: wrap;">
                {tags_html}
            </div>
        </div>
        '''


class MetricsRow(Component):
    """
    指标行 - 一行展示多个指标
    """
    
    def __init__(self, metrics: list):
        super().__init__()
        self.metrics = metrics  # [(label, value, trend_up?), ...]
    
    def render(self) -> str:
        items_html = ""
        for i, metric in enumerate(self.metrics):
            label = metric[0]
            value = metric[1]
            trend_up = metric[2] if len(metric) > 2 else None
            
            trend_html = ""
            if trend_up is not None:
                trend_color = "#10b981" if trend_up else "#ef4444"
                trend_icon = "↑" if trend_up else "↓"
                trend_html = f'<span style="color: {trend_color}; font-size: 12px; margin-left: 4px; font-weight: 600;">{trend_icon}</span>'
            
            # 分隔线（最后一个不加）
            border_style = "" if i == len(self.metrics) - 1 else 'border-right: 1px solid #f3f4f6;'
            
            items_html += f'''
                <div style="flex: 1; text-align: center; padding: 0 12px; {border_style}">
                    <div style="font-size: 20px; font-weight: 700; color: #1f2937;">
                        {value}
                        {trend_html}
                    </div>
                    <div style="font-size: 12px; color: #6b7280; margin-top: 4px;">{label}</div>
                </div>
            '''
        
        return f'''
        <div style="background: white; border-radius: 16px; 
                    padding: 20px 12px; border: 1px solid rgba(0, 0, 0, 0.06);
                    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
                    display: flex; align-items: center;">
            {items_html}
        </div>
        '''


class Badge(Component):
    """
    徽章/标签组件
    """
    
    def __init__(self, text: str, variant: str = "default"):
        super().__init__()
        self.text = text
        self.variant = variant
    
    def render(self) -> str:
        variants = {
            "default": {"bg": "#f3f4f6", "color": "#374151"},
            "primary": {"bg": "linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%)", "color": "white"},
            "success": {"bg": "linear-gradient(135deg, #10b981 0%, #059669 100%)", "color": "white"},
            "warning": {"bg": "linear-gradient(135deg, #f59e0b 0%, #ea580c 100%)", "color": "white"},
            "danger": {"bg": "linear-gradient(135deg, #ef4444 0%, #dc2626 100%)", "color": "white"},
            "info": {"bg": "linear-gradient(135deg, #3b82f6 0%, #2563eb 100%)", "color": "white"},
            "purple": {"bg": "linear-gradient(135deg, #8b5cf6 0%, #7c3aed 100%)", "color": "white"},
        }
        
        v = variants.get(self.variant, variants["default"])
        
        return f'''
        <span style="display: inline-block; padding: 4px 12px; 
                    border-radius: 16px; font-size: 11px; font-weight: 700;
                    background: {v["bg"]}; color: {v["color"]};
                    letter-spacing: 0.3px; text-transform: uppercase;">
            {self.text}
        </span>
        '''


class CompareTable(Component):
    """
    对比表格 - 多列数据对比
    """
    
    def __init__(self, headers: list, rows: list, 
                 highlight_rows: list = None, 
                 highlight_col: int = None,
                 striped: bool = True):
        super().__init__()
        self.headers = headers
        self.rows = rows
        self.highlight_rows = highlight_rows or []
        self.highlight_col = highlight_col
        self.striped = striped
    
    def render(self) -> str:
        # 表头
        headers_html = "".join(
            f'<th style="padding: 14px 16px; text-align: left; font-size: 12px; font-weight: 600; color: #6b7280; text-transform: uppercase; letter-spacing: 0.5px; background: #f9fafb;">{h}</th>'
            for h in self.headers
        )
        
        # 表行
        rows_html = ""
        for i, row in enumerate(self.rows):
            highlight = i in self.highlight_rows
            row_bg = "rgba(79, 70, 229, 0.04)" if highlight else ("white" if i % 2 == 0 or not self.striped else "#fafafa")
            
            cells_html = ""
            for j, cell in enumerate(row):
                cell_style = ""
                if self.highlight_col is not None and j == self.highlight_col:
                    cell_style = "font-weight: 600; color: #4f46e5;"
                
                cells_html += '<td style="padding: 14px 16px; font-size: 13px; color: #374151; ' + cell_style + '">' + str(cell) + '</td>'
            
            rows_html += '<tr style="background: ' + row_bg + '; transition: background 0.2s;">' + cells_html + '</tr>'
        
        return f'''
        <div style="overflow-x: auto; border-radius: 16px; 
                    border: 1px solid rgba(0, 0, 0, 0.06); 
                    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);">
            <table style="width: 100%; border-collapse: collapse;">
                <thead>
                    <tr style="border-bottom: 1px solid #e5e7eb;">
                        {headers_html}
                    </tr>
                </thead>
                <tbody>
                    {rows_html}
                </tbody>
            </table>
        </div>
        '''
