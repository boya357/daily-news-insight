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
        import html as _html

        # ========== 深色主题配色（全站统一）==========
        if self.variant == "gradient":
            tag_bg = "linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%)"
            tag_color = "white"
            tag_border = "rgba(255,255,255,.15)"
            text_color = "#94a3b8"
            icon_color = "#94a3b8"
            divider = "rgba(255,255,255,.1)"
        else:
            tag_bg = "linear-gradient(135deg, rgba(79,70,229,.25) 0%, rgba(124,58,237,.25) 100%)"
            tag_color = "#c4b5fd"
            tag_border = "rgba(124,58,237,.35)"
            text_color = "#94a3b8"
            icon_color = "#94a3b8"
            divider = "rgba(255,255,255,.1)"

        def _fmt(s):
            if isinstance(s, dict):
                code = str(s.get("code", "")).strip()
                name = str(s.get("name", "")).strip()
                impact = s.get("impact")
                impact = str(impact).strip() if impact else ""
                if code and (code == name or not code[:1].isdigit()):
                    code = ""
                if code and code[:1].isdigit() and name and name != code:
                    d = _html.escape(name) + '<span style="opacity:.65;font-weight:400;margin-left:4px;">' + _html.escape(code) + '</span>'
                elif name:
                    d = _html.escape(name)
                elif code:
                    d = _html.escape(code)
                else:
                    d = _html.escape(str(s))
                tip = ' title="' + _html.escape(impact) + '"' if impact else ""
                return "<span" + tip + ">" + d + "</span>"
            elif isinstance(s, (list, tuple)):
                return _html.escape(" / ".join(str(x) for x in s))
            else:
                return _html.escape(str(s))

        tag_parts = []
        for stock in self.stocks:
            inner = _fmt(stock)
            tag_parts.append(
                '<span style="display:inline-block;padding:5px 12px;border-radius:16px;'
                'font-size:12px;font-weight:600;margin:3px 6px 3px 0;transition:all .2s ease;'
                'background:' + tag_bg + ';color:' + tag_color + ';border:1px solid ' + tag_border + ';" '
                'onmouseover="this.style.transform=\'translateY(-1px)\';this.style.boxShadow=\'0 6px 16px rgba(79,70,229,.4)\';this.style.borderColor=\'rgba(255,255,255,.3)\';" '
                'onmouseout="this.style.transform=\'translateY(0)\';this.style.boxShadow=\'0 2px 8px rgba(79,70,229,.3)\';this.style.borderColor=\'' + tag_border + '\';">'
                + inner + '</span>'
            )
        tags_html = "".join(tag_parts)

        return (
            '<div style="padding-top:16px;border-top:1px solid ' + divider + ';margin-top:16px;">'
            '<div style="display:flex;align-items:center;margin-bottom:10px;">'
            '<div style="width:16px;height:16px;margin-right:6px;">'
            + icon_svg("stock", 16, icon_color) +
            '</div>'
            '<span style="font-size:13px;color:' + text_color + ';font-weight:500;">'
            + _html.escape(self.label) +
            '</span>'
            '</div>'
            '<div style="display:flex;flex-wrap:wrap;">'
            + tags_html +
            '</div>'
            '</div>'
        )



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


class ProgressBar(Component):
    """
    渐变进度条组件 - 展示百分比数据
    """
    
    def __init__(self, value: float, max_value: float = 100, 
                 label: str = None, show_percent: bool = True,
                 variant: str = "default", height: str = "8px"):
        super().__init__()
        self.value = value
        self.max_value = max_value
        self.label = label
        self.show_percent = show_percent
        self.variant = variant
        self.height = height
    
    def render(self) -> str:
        percent = min((self.value / self.max_value) * 100, 100)
        
        variants = {
            "default": "linear-gradient(90deg, #4f46e5 0%, #7c3aed 100%)",
            "success": "linear-gradient(90deg, #10b981 0%, #059669 100%)",
            "warning": "linear-gradient(90deg, #f59e0b 0%, #ea580c 100%)",
            "danger": "linear-gradient(90deg, #ef4444 0%, #dc2626 100%)",
            "rainbow": "linear-gradient(90deg, #ef4444 0%, #f59e0b 50%, #10b981 100%)",
        }
        
        gradient = variants.get(self.variant, variants["default"])
        
        label_html = ''
        if self.label:
            percent_html = f'<span style="font-weight: 600; color: #4f46e5;">{percent:.0f}%</span>' if self.show_percent else ''
            label_html = f'''
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                <span style="font-size: 13px; font-weight: 500; color: #374151;">{self.label}</span>
                {percent_html}
            </div>
            '''
        
        return f'''
        <div style="width: 100%;">
            {label_html}
            <div style="width: 100%; height: {self.height}; 
                        background: #f3f4f6; border-radius: 999px; 
                        overflow: hidden; box-shadow: inset 0 1px 2px rgba(0,0,0,0.06);">
                <div style="width: {percent}%; height: 100%; 
                            background: {gradient};
                            border-radius: 999px; 
                            transition: width 1s ease-out;
                            box-shadow: 0 1px 3px rgba(0,0,0,0.1);">
                </div>
            </div>
        </div>
        '''


class Sparkline(Component):
    """
    迷你趋势图组件 - 纯SVG实现的小型折线图
    """
    
    def __init__(self, data: list, width: int = 120, height: int = 40,
                 color: str = "#4f46e5", fill: bool = True,
                 stroke_width: int = 2):
        super().__init__()
        self.data = data
        self.width = width
        self.height = height
        self.color = color
        self.fill = fill
        self.stroke_width = stroke_width
    
    def render(self) -> str:
        if not self.data:
            return '<div style="width: {width}px; height: {height}px;"></div>'
        
        min_val = min(self.data)
        max_val = max(self.data)
        range_val = max_val - min_val if max_val != min_val else 1
        
        padding = self.stroke_width
        graph_width = self.width - padding * 2
        graph_height = self.height - padding * 2
        
        # 生成路径点
        points = []
        step = graph_width / (len(self.data) - 1) if len(self.data) > 1 else graph_width
        
        for i, val in enumerate(self.data):
            x = padding + i * step
            y = padding + graph_height - ((val - min_val) / range_val) * graph_height
            points.append((x, y))
        
        # 生成折线路径
        path_d = f"M {points[0][0]:.1f} {points[0][1]:.1f}"
        for i in range(1, len(points)):
            path_d += f" L {points[i][0]:.1f} {points[i][1]:.1f}"
        
        # 生成填充区域路径
        fill_d = ''
        if self.fill:
            fill_d = path_d + f" L {points[-1][0]:.1f} {padding + graph_height:.1f} L {points[0][0]:.1f} {padding + graph_height:.1f} Z"
        
        fill_color = self.color.replace(')', ', 0.1)').replace('rgb', 'rgba')
        if '#' in self.color:
            fill_color = self.color + '1A'  # 10% 透明度
        
        return f'''
        <svg width="{self.width}" height="{self.height}" viewBox="0 0 {self.width} {self.height}" style="display: block;">
            {'<path d="' + fill_d + '" fill="' + fill_color + '" />' if self.fill else ''}
            <path d="{path_d}" fill="none" stroke="{self.color}" stroke-width="{self.stroke_width}" stroke-linecap="round" stroke-linejoin="round" />
        </svg>
        '''


class GaugeChart(Component):
    """
    仪表盘组件 - SVG环形仪表盘，展示指数类数据
    """
    
    def __init__(self, value: float, max_value: float = 100,
                 label: str = "", size: int = 100, stroke_width: int = 8,
                 color: str = None, show_value: bool = True):
        super().__init__()
        self.value = min(value, max_value)
        self.max_value = max_value
        self.label = label
        self.size = size
        self.stroke_width = stroke_width
        self.show_value = show_value
        
        # 根据数值自动变色
        if color is None:
            percent = value / max_value
            if percent >= 0.8:
                self.color = "#ef4444"  # 红色 - 高风险
            elif percent >= 0.6:
                self.color = "#f59e0b"  # 黄色 - 中等
            elif percent >= 0.4:
                self.color = "#3b82f6"  # 蓝色 - 正常
            else:
                self.color = "#10b981"  # 绿色 - 低风险
        else:
            self.color = color
    
    def render(self) -> str:
        percent = self.value / self.max_value
        radius = (self.size - self.stroke_width) / 2
        center_x = self.size / 2
        center_y = self.size / 2
        
        # 计算圆弧起点和终点（270度为起点，顺时针画225度范围）
        start_angle = 135  # 左下起点
        end_angle = start_angle + 270 * percent  # 终点角度
        bg_end_angle = start_angle + 270  # 背景弧终点
        
        # 转换为弧度
        import math
        
        def angle_to_point(angle_deg, r):
            angle_rad = math.radians(angle_deg - 90)  # -90让0度在顶部
            x = center_x + r * math.cos(angle_rad)
            y = center_y + r * math.sin(angle_rad)
            return x, y
        
        # 背景弧
        bg_start = angle_to_point(start_angle, radius)
        bg_end = angle_to_point(bg_end_angle, radius)
        bg_large_arc = 1 if 270 > 180 else 0
        
        # 前景弧
        fg_end = angle_to_point(end_angle, radius)
        fg_large_arc = 1 if (270 * percent) > 180 else 0
        
        value_html = ''
        if self.show_value:
            value_html = f'''
            <div style="position: absolute; top: 55%; left: 50%; 
                        transform: translate(-50%, -50%); text-align: center; width: 100%;">
                <div style="font-size: {int(self.size * 0.28)}px; font-weight: 700; 
                            color: {self.color}; line-height: 1;">
                    {int(self.value)}
                </div>
            </div>
            '''
        
        return f'''
        <div style="text-align: center;">
            <div style="position: relative; width: {self.size}px; height: {self.size}px; margin: 0 auto;">
                <svg width="{self.size}" height="{self.size}" viewBox="0 0 {self.size} {self.size}">
                    <!-- 背景弧 -->
                    <path d="M {bg_start[0]:.1f} {bg_start[1]:.1f} 
                             A {radius:.1f} {radius:.1f} 0 {bg_large_arc} 1 {bg_end[0]:.1f} {bg_end[1]:.1f}"
                          fill="none" stroke="#f3f4f6" stroke-width="{self.stroke_width}" 
                          stroke-linecap="round" />
                    
                    <!-- 前景弧 -->
                    <path d="M {bg_start[0]:.1f} {bg_start[1]:.1f} 
                             A {radius:.1f} {radius:.1f} 0 {fg_large_arc} 1 {fg_end[0]:.1f} {fg_end[1]:.1f}"
                          fill="none" stroke="{self.color}" stroke-width="{self.stroke_width}" 
                          stroke-linecap="round"
                          style="filter: drop-shadow(0 2px 4px {self.color}40);" />
                </svg>
                {value_html}
            </div>
            {'<div style="font-size: 12px; color: #6b7280; margin-top: 4px;">' + self.label + '</div>' if self.label else ''}
        </div>
        '''


class Tabs(Component):
    """
    标签页组件 - 支持切换多个内容面板
    """
    
    def __init__(self, tabs: list, default_index: int = 0):
        super().__init__()
        self.tabs = tabs  # [(label, content), ...]
        self.default_index = default_index
    
    def render(self) -> str:
        # 生成唯一ID，避免页面内多个Tabs冲突
        import random
        tab_id = f"tabs_{random.randint(10000, 99999)}"
        
        # 标签按钮
        tab_buttons = ""
        for i, (label, _) in enumerate(self.tabs):
            active_class = "active" if i == self.default_index else ""
            active_style = ""
            if i == self.default_index:
                active_style = """
                    background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%);
                    color: white;
                    box-shadow: 0 2px 8px rgba(79, 70, 229, 0.3);
                """
            else:
                active_style = """
                    background: transparent;
                    color: #6b7280;
                """
            
            tab_buttons += f'''
            <button class="tab-btn {active_class}" 
                    style="padding: 10px 20px; border: none; border-radius: 10px;
                           font-size: 13px; font-weight: 600; cursor: pointer;
                           transition: all 0.3s ease; {active_style}"
                    onclick="switchTab_{tab_id}({i})">
                {label}
            </button>
            '''
        
        # 内容面板
        tab_panels = ""
        for i, (_, content) in enumerate(self.tabs):
            display_style = "block" if i == self.default_index else "none"
            content_html = content.render() if hasattr(content, "render") else str(content)
            tab_panels += f'''
            <div class="tab-panel" id="{tab_id}_panel_{i}" style="display: {display_style}; padding-top: 20px;">
                {content_html}
            </div>
            '''
        
        # JavaScript
        js_script = f'''
        <script>
        function switchTab_{tab_id}(index) {{
            const container = document.getElementById("{tab_id}");
            const buttons = container.querySelectorAll(".tab-btn");
            const panels = container.querySelectorAll(".tab-panel");
            
            buttons.forEach((btn, i) => {{
                if (i === index) {{
                    btn.style.background = "linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%)";
                    btn.style.color = "white";
                    btn.style.boxShadow = "0 2px 8px rgba(79, 70, 229, 0.3)";
                }} else {{
                    btn.style.background = "transparent";
                    btn.style.color = "#6b7280";
                    btn.style.boxShadow = "none";
                }}
            }});
            
            panels.forEach((panel, i) => {{
                panel.style.display = i === index ? "block" : "none";
            }});
        }}
        </script>
        '''
        
        return f'''
        <div id="{tab_id}" style="width: 100%;">
            <div style="display: flex; gap: 6px; padding: 4px; 
                        background: #f3f4f6; border-radius: 12px; flex-wrap: wrap;">
                {tab_buttons}
            </div>
            {tab_panels}
            {js_script}
        </div>
        '''


class StatCard(Component):
    """
    渐变统计卡片 - 大号数字 + 渐变背景，冲击力强
    """
    
    def __init__(self, title: str, value: str, subtitle: str = None,
                 icon: str = None, variant: str = "purple",
                 trend: str = None, trend_up: bool = True):
        super().__init__()
        self.title = title
        self.value = value
        self.subtitle = subtitle
        self.icon = icon
        self.variant = variant
        self.trend = trend
        self.trend_up = trend_up
    
    def render(self) -> str:
        variants = {
            "purple": {
                "bg": "linear-gradient(135deg, #8b5cf6 0%, #6366f1 100%)",
                "glow": "rgba(139, 92, 246, 0.4)"
            },
            "blue": {
                "bg": "linear-gradient(135deg, #3b82f6 0%, #2563eb 100%)",
                "glow": "rgba(59, 130, 246, 0.4)"
            },
            "green": {
                "bg": "linear-gradient(135deg, #10b981 0%, #059669 100%)",
                "glow": "rgba(16, 185, 129, 0.4)"
            },
            "orange": {
                "bg": "linear-gradient(135deg, #f59e0b 0%, #ea580c 100%)",
                "glow": "rgba(245, 158, 11, 0.4)"
            },
            "red": {
                "bg": "linear-gradient(135deg, #ef4444 0%, #dc2626 100%)",
                "glow": "rgba(239, 68, 68, 0.4)"
            },
            "indigo": {
                "bg": "linear-gradient(135deg, #6366f1 0%, #4f46e5 100%)",
                "glow": "rgba(99, 102, 241, 0.4)"
            },
        }
        
        v = variants.get(self.variant, variants["purple"])
        
        icon_html = ''
        if self.icon:
            from .icons import icon_svg
            icon_html = f'''
            <div style="width: 48px; height: 48px; 
                        background: rgba(255, 255, 255, 0.2); 
                        border-radius: 14px; display: flex; align-items: center; 
                        justify-content: center; margin-bottom: 16px;
                        backdrop-filter: blur(10px);">
                {icon_svg(self.icon, 24, "white")}
            </div>
            '''
        
        trend_html = ''
        if self.trend:
            trend_color = "rgba(255,255,255,0.9)"
            trend_icon = "↑" if self.trend_up else "↓"
            trend_html = f'''
            <div style="display: flex; align-items: center; color: {trend_color}; 
                        font-size: 14px; font-weight: 600; margin-top: 8px;">
                <span style="margin-right: 4px;">{trend_icon}</span>
                <span>{self.trend}</span>
            </div>
            '''
        
        subtitle_html = f'<div style="font-size: 13px; color: rgba(255,255,255,0.7); margin-top: 4px;">{self.subtitle}</div>' if self.subtitle else ''
        
        return f'''
        <div style="background: {v["bg"]}; 
                    border-radius: 18px; 
                    padding: 24px; 
                    color: white;
                    box-shadow: 0 8px 24px {v["glow"]}, 0 2px 8px rgba(0,0,0,0.1);
                    transition: all 0.3s ease;
                    position: relative;
                    overflow: hidden;"
             onmouseover="this.style.transform='translateY(-4px)'; this.style.boxShadow='0 12px 32px {v["glow"]}, 0 4px 12px rgba(0,0,0,0.15)';"
             onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 8px 24px {v["glow"]}, 0 2px 8px rgba(0,0,0,0.1)';">
            
            <!-- 装饰光效 -->
            <div style="position: absolute; top: -50%; right: -20%; 
                        width: 200px; height: 200px; 
                        background: radial-gradient(circle, rgba(255,255,255,0.15) 0%, transparent 70%);
                        border-radius: 50%; pointer-events: none;"></div>
            
            {icon_html}
            
            <div style="position: relative; z-index: 1;">
                <div style="font-size: 14px; color: rgba(255,255,255,0.8); margin-bottom: 8px; font-weight: 500;">
                    {self.title}
                </div>
                <div style="font-size: 36px; font-weight: 800; line-height: 1.1; 
                            text-shadow: 0 2px 10px rgba(0,0,0,0.1);">
                    {self.value}
                </div>
                {subtitle_html}
                {trend_html}
            </div>
        </div>
        '''
