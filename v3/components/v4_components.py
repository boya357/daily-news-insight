"""
V4 组件库
========
V4设计系统的核心组件集合，提供统一的视觉风格和交互体验。

设计原则：
- 内容优先：白底深色文字，高可读性
- 卡片化设计：信息分组清晰
- 柔和阴影：轻盈有层次
- 圆角适中：12-16px
- 红涨绿跌：符合A股投资习惯

组件分类：
- 基础组件：Card、Tag、Button、Badge
- 数据展示：RadarChart、DataGrid、ProgressBar、BarChart
- 导航组件：Tabs、Breadcrumb、Pagination
- 业务组件：StockCard、TopicCard、MarketOverview、SectorRanking
- 页面布局：Section、PageHeader、Footer
"""

from typing import List, Dict, Optional, Tuple, Any
from datetime import datetime


# ============================================================================
# 基础样式常量
# ============================================================================

V4_COLORS = {
    'primary': '#8B5CF6',      # 主色 - 紫色
    'secondary': '#6366F1',    # 次色 - 靛蓝
    'success': '#10B981',      # 成功 - 绿色
    'warning': '#F59E0B',      # 警告 - 橙色
    'danger': '#EF4444',       # 危险 - 红色
    'info': '#3B82F6',         # 信息 - 蓝色
    'text_primary': '#1F2937', # 主要文字
    'text_secondary': '#6B7280',# 次要文字
    'text_muted': '#9CA3AF',   # 弱化文字
    'bg_card': '#FFFFFF',      # 卡片背景
    'bg_page': '#F8FAFC',      # 页面背景
    'border': '#E5E7EB',       # 边框色
}

V4_RADIUS = {
    'sm': '8px',
    'md': '12px',
    'lg': '16px',
    'xl': '20px',
}

V4_SHADOW = {
    'sm': '0 1px 2px rgba(0, 0, 0, 0.05)',
    'md': '0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)',
    'lg': '0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05)',
    'xl': '0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04)',
}


# ============================================================================
# 基础组件
# ============================================================================

class V4Component:
    """V4组件基类"""
    
    def __init__(self, class_name: str = ""):
        self.class_name = class_name
        self.styles = []
    
    def add_style(self, css: str):
        """添加组件样式"""
        if css not in self.styles:
            self.styles.append(css)
    
    def render(self) -> str:
        """渲染组件HTML"""
        raise NotImplementedError
    
    def get_styles(self) -> str:
        """获取组件CSS样式"""
        return "\n".join(self.styles)


class V4Card(V4Component):
    """卡片组件
    
    V4设计系统的基础容器，白底+柔和阴影+圆角
    """
    
    def __init__(self, content: str = "", class_name: str = "", 
                 padding: str = "24px", shadow: str = "md"):
        super().__init__(class_name)
        self.content = content
        self.padding = padding
        self.shadow = shadow
        
        self.add_style(f'''
        .v4-card {{
            background: {V4_COLORS['bg_card']};
            border-radius: {V4_RADIUS['lg']};
            box-shadow: {V4_SHADOW[shadow]};
            padding: {padding};
            margin-bottom: 16px;
            border: 1px solid {V4_COLORS['border']};
            transition: all 0.3s ease;
        }}
        .v4-card:hover {{
            box-shadow: {V4_SHADOW['lg']};
        }}
        ''')
    
    def render(self) -> str:
        base_class = f"v4-card {self.class_name}".strip()
        return f'<div class="{base_class}">{self.content}</div>'


class V4Tag(V4Component):
    """标签组件
    
    用于状态标记、分类标签等
    """
    
    VARIANTS = {
        'primary': ('#8B5CF6', 'rgba(139, 92, 246, 0.1)'),
        'success': ('#10B981', 'rgba(16, 185, 129, 0.1)'),
        'warning': ('#F59E0B', 'rgba(245, 158, 11, 0.1)'),
        'danger': ('#EF4444', 'rgba(239, 68, 68, 0.1)'),
        'info': ('#3B82F6', 'rgba(59, 130, 246, 0.1)'),
        'gray': ('#6B7280', 'rgba(107, 114, 128, 0.1)'),
        'green': ('#10B981', 'rgba(16, 185, 129, 0.1)'),  # 涨
        'red': ('#EF4444', 'rgba(239, 68, 68, 0.1)'),      # 跌
        'blue': ('#3B82F6', 'rgba(59, 130, 246, 0.1)'),
        'orange': ('#F59E0B', 'rgba(245, 158, 11, 0.1)'),
        'purple': ('#8B5CF6', 'rgba(139, 92, 246, 0.1)'),
    }
    
    def __init__(self, text: str, variant: str = "primary", 
                 size: str = "md", class_name: str = ""):
        super().__init__(class_name)
        self.text = text
        self.variant = variant
        self.size = size
        
        # 尺寸映射
        size_map = {
            'sm': 'font-size: 12px; padding: 2px 8px;',
            'md': 'font-size: 14px; padding: 4px 12px;',
            'lg': 'font-size: 16px; padding: 6px 16px;',
        }
        self.size_style = size_map.get(size, size_map['md'])
        
        # 颜色
        color, bg_color = self.VARIANTS.get(variant, self.VARIANTS['primary'])
        self.color = color
        self.bg_color = bg_color
        
        self.add_style(f'''
        .v4-tag {{
            display: inline-block;
            font-weight: 500;
            border-radius: 20px;
            line-height: 1.4;
            transition: all 0.2s ease;
        }}
        ''')
    
    def render(self) -> str:
        style = f'{self.size_style} color: {self.color}; background: {self.bg_color};'
        base_class = f"v4-tag {self.class_name}".strip()
        return f'<span class="{base_class}" style="{style}">{self.text}</span>'


class V4Button(V4Component):
    """按钮组件"""
    
    VARIANTS = {
        'primary': ('#8B5CF6', '#7C3AED', '#FFFFFF'),
        'secondary': ('#F3F4F6', '#E5E7EB', '#1F2937'),
        'success': ('#10B981', '#059669', '#FFFFFF'),
        'danger': ('#EF4444', '#DC2626', '#FFFFFF'),
        'outline': ('transparent', '#8B5CF6', '#8B5CF6'),
    }
    
    def __init__(self, text: str, variant: str = "primary", 
                 size: str = "md", href: str = None, 
                 class_name: str = "", icon: str = ""):
        super().__init__(class_name)
        self.text = text
        self.variant = variant
        self.size = size
        self.href = href
        self.icon = icon
        
        size_map = {
            'sm': 'padding: 6px 14px; font-size: 13px;',
            'md': 'padding: 10px 20px; font-size: 14px;',
            'lg': 'padding: 14px 28px; font-size: 16px;',
        }
        self.size_style = size_map.get(size, size_map['md'])
        
        bg, hover_bg, color = self.VARIANTS.get(variant, self.VARIANTS['primary'])
        self.bg = bg
        self.hover_bg = hover_bg
        self.color = color
        
        self.add_style(f'''
        .v4-btn {{
            display: inline-flex;
            align-items: center;
            gap: 6px;
            font-weight: 500;
            border-radius: {V4_RADIUS['md']};
            cursor: pointer;
            text-decoration: none;
            border: none;
            transition: all 0.2s ease;
        }}
        .v4-btn:hover {{
            transform: translateY(-1px);
        }}
        ''')
    
    def render(self) -> str:
        style = f'{self.size_style} background: {self.bg}; color: {self.color};'
        base_class = f"v4-btn {self.class_name}".strip()
        
        icon_html = f'<span>{self.icon}</span>' if self.icon else ''
        content = f'{icon_html}<span>{self.text}</span>'
        
        if self.href:
            return f'<a href="{self.href}" class="{base_class}" style="{style}">{content}</a>'
        else:
            return f'<button class="{base_class}" style="{style}">{content}</button>'


# ============================================================================
# 数据可视化组件
# ============================================================================

class V4RadarChart(V4Component):
    """雷达图组件
    
    使用SVG实现的雷达图，支持任意数量维度（3-8维最佳）
    """
    
    def __init__(self, labels: List[str], values: List[float], 
                 size: int = 220, max_value: float = 100,
                 color: str = "#8B5CF6", class_name: str = ""):
        super().__init__(class_name)
        self.labels = labels
        self.values = values
        self.size = size
        self.max_value = max_value
        self.color = color
        
        if len(labels) != len(values):
            raise ValueError("labels和values长度必须一致")
        if len(labels) < 3:
            raise ValueError("雷达图至少需要3个维度")
    
    def render(self) -> str:
        n = len(self.labels)
        center_x = self.size / 2
        center_y = self.size / 2
        radius = self.size * 0.38
        
        # 生成多边形顶点
        def get_point(index, value_ratio):
            import math
            angle = (index * 2 * math.pi / n) - math.pi / 2
            r = radius * value_ratio
            x = center_x + r * math.cos(angle)
            y = center_y + r * math.sin(angle)
            return x, y
        
        # 背景网格（5层）
        grid_lines = []
        for level in range(5, 0, -1):
            ratio = level / 5
            points = []
            for i in range(n):
                x, y = get_point(i, ratio)
                points.append(f"{x:.1f},{y:.1f}")
            opacity = 0.1 + (level - 1) * 0.05
            grid_lines.append(
                f'<polygon points="{" ".join(points)}" fill="none" '
                f'stroke="#E5E7EB" stroke-width="1" opacity="{opacity}"/>'
            )
        
        # 轴线
        axis_lines = []
        for i in range(n):
            x, y = get_point(i, 1.0)
            axis_lines.append(
                f'<line x1="{center_x}" y1="{center_y}" x2="{x:.1f}" y2="{y:.1f}" '
                f'stroke="#E5E7EB" stroke-width="1"/>'
            )
        
        # 数据区域
        data_points = []
        for i, value in enumerate(self.values):
            ratio = min(value / self.max_value, 1.0)
            x, y = get_point(i, ratio)
            data_points.append(f"{x:.1f},{y:.1f}")
        
        # 数据点
        dot_points = []
        for i, value in enumerate(self.values):
            ratio = min(value / self.max_value, 1.0)
            x, y = get_point(i, ratio)
            dot_points.append(
                f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4" fill="{self.color}" '
                f'stroke="white" stroke-width="2"/>'
            )
        
        # 标签
        label_elements = []
        for i, label in enumerate(self.labels):
            x, y = get_point(i, 1.25)
            text_anchor = "middle"
            if x < center_x * 0.7:
                text_anchor = "end"
            elif x > center_x * 1.3:
                text_anchor = "start"
            
            label_elements.append(
                f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{text_anchor}" '
                f'dominant-baseline="middle" fill="#6B7280" font-size="12px" '
                f'font-weight="500">{label}</text>'
            )
        
        svg_content = f'''
        <svg width="{self.size}" height="{self.size}" viewBox="0 0 {self.size} {self.size}">
            {''.join(grid_lines)}
            {''.join(axis_lines)}
            <polygon points="{" ".join(data_points)}" fill="{self.color}" 
                     fill-opacity="0.2" stroke="{self.color}" stroke-width="2"/>
            {''.join(dot_points)}
            {''.join(label_elements)}
        </svg>
        '''
        
        base_class = f"v4-radar-chart {self.class_name}".strip()
        return f'<div class="{base_class}">{svg_content}</div>'


class V4ProgressBar(V4Component):
    """进度条组件"""
    
    def __init__(self, value: float, max_value: float = 100, 
                 label: str = "", color: str = "#8B5CF6",
                 show_value: bool = True, class_name: str = ""):
        super().__init__(class_name)
        self.value = value
        self.max_value = max_value
        self.label = label
        self.color = color
        self.show_value = show_value
        
        self.add_style(f'''
        .v4-progress-bar {{
            margin-bottom: 12px;
        }}
        .v4-progress-bar-header {{
            display: flex;
            justify-content: space-between;
            margin-bottom: 6px;
            font-size: 14px;
        }}
        .v4-progress-bar-label {{
            color: {V4_COLORS['text_secondary']};
            font-weight: 500;
        }}
        .v4-progress-bar-value {{
            color: {V4_COLORS['text_primary']};
            font-weight: 600;
        }}
        .v4-progress-bar-track {{
            height: 8px;
            background: #F3F4F6;
            border-radius: 4px;
            overflow: hidden;
        }}
        .v4-progress-bar-fill {{
            height: 100%;
            border-radius: 4px;
            transition: width 0.6s ease;
        }}
        ''')
    
    def render(self) -> str:
        percentage = min(self.value / self.max_value * 100, 100)
        
        header_html = ''
        if self.label or self.show_value:
            label_html = f'<span class="v4-progress-bar-label">{self.label}</span>' if self.label else ''
            value_html = f'<span class="v4-progress-bar-value">{self.value:.1f}</span>' if self.show_value else ''
            header_html = f'<div class="v4-progress-bar-header">{label_html}{value_html}</div>'
        
        base_class = f"v4-progress-bar {self.class_name}".strip()
        return f'''
        <div class="{base_class}">
            {header_html}
            <div class="v4-progress-bar-track">
                <div class="v4-progress-bar-fill" style="width: {percentage}%; background: {self.color};"></div>
            </div>
        </div>
        '''


class V4DataGrid(V4Component):
    """数据网格组件
    
    展示多组关键指标数据
    """
    
    def __init__(self, items: List[Dict[str, Any]], 
                 columns: int = 3, class_name: str = ""):
        super().__init__(class_name)
        self.items = items
        self.columns = columns
        
        self.add_style(f'''
        .v4-data-grid {{
            display: grid;
            grid-template-columns: repeat({columns}, 1fr);
            gap: 12px;
            margin-bottom: 16px;
        }}
        .v4-data-grid-item {{
            background: {V4_COLORS['bg_card']};
            border-radius: {V4_RADIUS['md']};
            padding: 16px;
            border: 1px solid {V4_COLORS['border']};
            text-align: center;
        }}
        .v4-data-grid-value {{
            font-size: 24px;
            font-weight: 700;
            color: {V4_COLORS['text_primary']};
            margin-bottom: 4px;
        }}
        .v4-data-grid-label {{
            font-size: 13px;
            color: {V4_COLORS['text_secondary']};
        }}
        @media (max-width: 640px) {{
            .v4-data-grid {{
                grid-template-columns: repeat(2, 1fr);
            }}
        }}
        ''')
    
    def render(self) -> str:
        items_html = ''
        for item in self.items:
            value = item.get('value', '')
            label = item.get('label', '')
            value_color = item.get('color', V4_COLORS['text_primary'])
            
            items_html += f'''
            <div class="v4-data-grid-item">
                <div class="v4-data-grid-value" style="color: {value_color};">{value}</div>
                <div class="v4-data-grid-label">{label}</div>
            </div>
            '''
        
        base_class = f"v4-data-grid {self.class_name}".strip()
        return f'<div class="{base_class}">{items_html}</div>'


class V4HorizontalBarChart(V4Component):
    """横向柱状图组件"""
    
    def __init__(self, items: List[Dict[str, Any]], 
                 max_value: float = None, bar_color: str = "#8B5CF6",
                 show_value: bool = True, class_name: str = ""):
        super().__init__(class_name)
        self.items = items
        if max_value is not None:
            self.max_value = max_value
        elif items:
            self.max_value = max(item.get('value', 0) for item in items)
        else:
            self.max_value = 100
        self.bar_color = bar_color
        self.show_value = show_value
        
        self.add_style(f'''
        .v4-hbar-chart {{
            margin-bottom: 16px;
        }}
        .v4-hbar-item {{
            display: flex;
            align-items: center;
            margin-bottom: 10px;
            gap: 12px;
        }}
        .v4-hbar-label {{
            width: 80px;
            font-size: 13px;
            color: {V4_COLORS['text_secondary']};
            flex-shrink: 0;
            text-align: right;
        }}
        .v4-hbar-track {{
            flex: 1;
            height: 24px;
            background: #F3F4F6;
            border-radius: 12px;
            overflow: hidden;
            position: relative;
        }}
        .v4-hbar-fill {{
            height: 100%;
            border-radius: 12px;
            transition: width 0.6s ease;
            display: flex;
            align-items: center;
            justify-content: flex-end;
            padding-right: 8px;
        }}
        .v4-hbar-value {{
            font-size: 12px;
            font-weight: 600;
            color: white;
        }}
        ''')
    
    def render(self) -> str:
        items_html = ''
        for item in self.items:
            label = item.get('label', '')
            value = item.get('value', 0)
            color = item.get('color', self.bar_color)
            percentage = min(value / self.max_value * 100, 100)
            
            value_html = f'<span class="v4-hbar-value">{value:.1f}</span>' if self.show_value else ''
            
            items_html += f'''
            <div class="v4-hbar-item">
                <div class="v4-hbar-label">{label}</div>
                <div class="v4-hbar-track">
                    <div class="v4-hbar-fill" style="width: {percentage}%; background: {color};">
                        {value_html}
                    </div>
                </div>
            </div>
            '''
        
        base_class = f"v4-hbar-chart {self.class_name}".strip()
        return f'<div class="{base_class}">{items_html}</div>'


# ============================================================================
# 导航组件
# ============================================================================

class V4Tabs(V4Component):
    """Tab切换组件"""
    
    def __init__(self, tabs: List[Dict[str, str]], 
                 default_active: int = 0,
                 tab_style: str = "card",  # card, line, pill
                 class_name: str = ""):
        super().__init__(class_name)
        self.tabs = tabs
        self.default_active = default_active
        self.tab_style = tab_style
        
        self.add_style(f'''
        .v4-tabs {{
            margin-bottom: 20px;
        }}
        .v4-tabs-nav {{
            display: flex;
            gap: 8px;
            margin-bottom: 16px;
            flex-wrap: wrap;
        }}
        .v4-tab-item {{
            padding: 10px 20px;
            cursor: pointer;
            font-size: 14px;
            font-weight: 500;
            transition: all 0.3s ease;
            border: none;
            background: transparent;
            color: {V4_COLORS['text_secondary']};
        }}
        /* Card style */
        .v4-tabs-card .v4-tab-item {{
            background: #F3F4F6;
            border-radius: {V4_RADIUS['md']};
        }}
        .v4-tabs-card .v4-tab-item.active {{
            background: {V4_COLORS['primary']};
            color: white;
        }}
        /* Line style */
        .v4-tabs-line .v4-tab-item {{
            border-bottom: 2px solid transparent;
            border-radius: 0;
        }}
        .v4-tabs-line .v4-tab-item.active {{
            color: {V4_COLORS['primary']};
            border-bottom-color: {V4_COLORS['primary']};
        }}
        /* Pill style */
        .v4-tabs-pill .v4-tab-item {{
            border-radius: 20px;
            background: #F3F4F6;
        }}
        .v4-tabs-pill .v4-tab-item.active {{
            background: linear-gradient(135deg, {V4_COLORS['primary']}, {V4_COLORS['secondary']});
            color: white;
        }}
        .v4-tab-content {{
            display: none;
        }}
        .v4-tab-content.active {{
            display: block;
            animation: fadeIn 0.3s ease;
        }}
        @keyframes fadeIn {{
            from {{ opacity: 0; transform: translateY(10px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}
        ''')
    
    def render(self) -> str:
        # Tab导航
        nav_html = '<div class="v4-tabs-nav">'
        for i, tab in enumerate(self.tabs):
            active_class = 'active' if i == self.default_active else ''
            label = tab.get('label', f'Tab {i+1}')
            nav_html += f'<button class="v4-tab-item {active_class}" data-tab="v4-tab-{i}">{label}</button>'
        nav_html += '</div>'
        
        # Tab内容
        content_html = ''
        for i, tab in enumerate(self.tabs):
            active_class = 'active' if i == self.default_active else ''
            content = tab.get('content', '')
            content_html += f'<div class="v4-tab-content {active_class}" id="v4-tab-{i}">{content}</div>'
        
        base_class = f"v4-tabs v4-tabs-{self.tab_style} {self.class_name}".strip()
        
        # JS交互
        js = '''
        <script>
        document.querySelectorAll('.v4-tabs').forEach(tabsContainer => {
            const tabItems = tabsContainer.querySelectorAll('.v4-tab-item');
            const tabContents = tabsContainer.querySelectorAll('.v4-tab-content');
            
            tabItems.forEach((tab, index) => {
                tab.addEventListener('click', () => {
                    // 移除所有active
                    tabItems.forEach(t => t.classList.remove('active'));
                    tabContents.forEach(c => c.classList.remove('active'));
                    // 添加当前active
                    tab.classList.add('active');
                    const tabId = tab.getAttribute('data-tab');
                    document.getElementById(tabId).classList.add('active');
                });
            });
        });
        </script>
        '''
        
        return f'<div class="{base_class}">{nav_html}{content_html}</div>{js}'


class V4Breadcrumb(V4Component):
    """面包屑导航组件"""
    
    def __init__(self, items: List[Dict[str, str]], 
                 class_name: str = ""):
        super().__init__(class_name)
        self.items = items
        
        self.add_style(f'''
        .v4-breadcrumb {{
            display: flex;
            align-items: center;
            gap: 8px;
            font-size: 14px;
            color: {V4_COLORS['text_secondary']};
            margin-bottom: 16px;
        }}
        .v4-breadcrumb a {{
            color: {V4_COLORS['text_secondary']};
            text-decoration: none;
            transition: color 0.2s;
        }}
        .v4-breadcrumb a:hover {{
            color: {V4_COLORS['primary']};
        }}
        .v4-breadcrumb-separator {{
            color: {V4_COLORS['text_muted']};
        }}
        .v4-breadcrumb-current {{
            color: {V4_COLORS['text_primary']};
            font-weight: 500;
        }}
        ''')
    
    def render(self) -> str:
        items_html = ''
        for i, item in enumerate(self.items):
            label = item.get('label', '')
            href = item.get('href', '')
            
            if i < len(self.items) - 1:
                if href:
                    items_html += f'<a href="{href}">{label}</a>'
                else:
                    items_html += f'<span>{label}</span>'
                items_html += '<span class="v4-breadcrumb-separator">/</span>'
            else:
                items_html += f'<span class="v4-breadcrumb-current">{label}</span>'
        
        base_class = f"v4-breadcrumb {self.class_name}".strip()
        return f'<nav class="{base_class}">{items_html}</nav>'


# ============================================================================
# 业务组件
# ============================================================================

class V4StockCard(V4Component):
    """股票卡片组件
    
    支持精简版和完整版两种模式：
    - 精简版：股票名称、代码、价格、涨跌幅 + 3个指标
    - 完整版：包含成本价、止损价、盈亏、风险等级、操作建议等完整持仓信息
    """
    
    def __init__(self, stock_data: Dict[str, Any], 
                 variant: str = "compact",  # compact, full
                 class_name: str = ""):
        super().__init__(class_name)
        self.stock = stock_data
        self.variant = variant
        
        self.add_style(f'''
        .v4-stock-card {{
            background: {V4_COLORS['bg_card']};
            border-radius: {V4_RADIUS['lg']};
            padding: 20px;
            border: 1px solid {V4_COLORS['border']};
            transition: all 0.3s ease;
        }}
        .v4-stock-card:hover {{
            box-shadow: {V4_SHADOW['md']};
            transform: translateY(-2px);
        }}
        .v4-stock-header {{
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            margin-bottom: 12px;
        }}
        .v4-stock-name {{
            font-size: 18px;
            font-weight: 700;
            color: {V4_COLORS['text_primary']};
        }}
        .v4-stock-code {{
            font-size: 13px;
            color: {V4_COLORS['text_muted']};
            margin-top: 2px;
        }}
        .v4-stock-price {{
            text-align: right;
        }}
        .v4-stock-price-value {{
            font-size: 24px;
            font-weight: 700;
        }}
        .v4-stock-price-change {{
            font-size: 14px;
            font-weight: 500;
            margin-top: 2px;
        }}
        .v4-stock-body {{
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 12px;
            padding-top: 12px;
            border-top: 1px solid {V4_COLORS['border']};
        }}
        .v4-stock-metric {{
            text-align: center;
        }}
        .v4-stock-metric-value {{
            font-size: 15px;
            font-weight: 600;
            color: {V4_COLORS['text_primary']};
        }}
        .v4-stock-metric-label {{
            font-size: 12px;
            color: {V4_COLORS['text_secondary']};
            margin-top: 2px;
        }}
        .stock-up {{ color: {V4_COLORS['danger']}; }}
        .stock-down {{ color: {V4_COLORS['success']}; }}
        
        /* 完整版特有样式 */
        .v4-stock-tags {{
            display: flex;
            gap: 6px;
            margin-bottom: 12px;
            flex-wrap: wrap;
        }}
        .v4-stock-detail-grid {{
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 12px;
            padding-top: 16px;
            border-top: 1px solid {V4_COLORS['border']};
        }}
        .v4-stock-detail-item {{
            text-align: center;
        }}
        .v4-stock-detail-label {{
            font-size: 12px;
            color: {V4_COLORS['text_secondary']};
            margin-bottom: 4px;
        }}
        .v4-stock-detail-value {{
            font-size: 15px;
            font-weight: 600;
            color: {V4_COLORS['text_primary']};
        }}
        .v4-stock-footer {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding-top: 16px;
            margin-top: 16px;
            border-top: 1px solid {V4_COLORS['border']};
        }}
        .v4-stock-risk-bar {{
            height: 6px;
            background: #E5E7EB;
            border-radius: 3px;
            overflow: hidden;
            flex: 1;
            margin: 0 12px;
        }}
        .v4-stock-risk-fill {{
            height: 100%;
            border-radius: 3px;
            transition: width 0.3s ease;
        }}
        .v4-stock-advice {{
            padding: 6px 16px;
            border-radius: 20px;
            font-size: 13px;
            font-weight: 600;
        }}
        .v4-stock-advice.buy {{
            background: rgba(239, 68, 68, 0.1);
            color: #EF4444;
        }}
        .v4-stock-advice.sell {{
            background: rgba(16, 185, 129, 0.1);
            color: #10B981;
        }}
        .v4-stock-advice.hold {{
            background: rgba(59, 130, 246, 0.1);
            color: #3B82F6;
        }}
        ''')
    
    def _render_compact(self) -> str:
        """渲染精简版股票卡片"""
        name = self.stock.get('name', '')
        code = self.stock.get('code', '')
        price = self.stock.get('price', 0)
        change_pct = self.stock.get('change_pct', 0)
        change = self.stock.get('change', 0)
        
        is_up = change_pct >= 0
        price_class = 'stock-up' if is_up else 'stock-down'
        sign = '+' if is_up else ''
        
        # 额外指标
        metrics = self.stock.get('metrics', [])
        metrics_html = ''
        for metric in metrics[:3]:
            metric_color = metric.get('color', V4_COLORS['text_primary'])
            metrics_html += f'''
            <div class="v4-stock-metric">
                <div class="v4-stock-metric-value" style="color: {metric_color};">{metric.get('value', '')}</div>
                <div class="v4-stock-metric-label">{metric.get('label', '')}</div>
            </div>
            '''
        
        base_class = f"v4-stock-card {self.class_name}".strip()
        return f'''
        <div class="{base_class}">
            <div class="v4-stock-header">
                <div>
                    <div class="v4-stock-name">{name}</div>
                    <div class="v4-stock-code">{code}</div>
                </div>
                <div class="v4-stock-price">
                    <div class="v4-stock-price-value {price_class}">{price:.2f}</div>
                    <div class="v4-stock-price-change {price_class}">{sign}{change_pct:.2f}% ({sign}{change:.2f})</div>
                </div>
            </div>
            <div class="v4-stock-body">
                {metrics_html}
            </div>
        </div>
        '''
    
    def _render_full(self) -> str:
        """渲染完整版股票卡片（持仓详情）"""
        stock = self.stock
        
        name = stock.get('name', '')
        code = stock.get('code', '')
        current_price = stock.get('current_price', stock.get('price', 0))
        change_pct = stock.get('today_change_pct', stock.get('change_pct', 0))
        change = stock.get('today_change', stock.get('change', 0))
        cost_price = stock.get('cost_price', 0)
        profit_loss_pct = stock.get('profit_loss_pct', 0)
        stop_loss_price = stock.get('stop_loss_price', 0)
        distance_to_sl = stock.get('distance_to_stop_loss', 0)
        risk_level = stock.get('risk_level', '中')
        advice_type = stock.get('advice_type', 'hold')
        advice_text = stock.get('advice_text', '')
        
        is_up = change_pct >= 0
        price_class = 'stock-up' if is_up else 'stock-down'
        sign = '+' if is_up else ''
        
        is_profit = profit_loss_pct >= 0
        profit_class = 'stock-up' if is_profit else 'stock-down'
        profit_sign = '+' if is_profit else ''
        
        # 风险等级颜色
        risk_colors = {
            '高': '#EF4444',
            '中': '#F59E0B',
            '低': '#10B981',
        }
        risk_color = risk_colors.get(risk_level, '#6B7280')
        
        # 风险百分比（用于进度条）
        risk_pct = min(distance_to_sl, 100) if distance_to_sl > 0 else 0
        
        # 建议标签
        advice_map = {
            'buy': ('加仓', 'buy'),
            'sell': ('减仓', 'sell'),
            'hold': ('持有', 'hold'),
            'watch': ('观察', 'hold'),
        }
        advice_label, advice_class = advice_map.get(advice_type, ('观察', 'hold'))
        
        # 详细指标
        detail_items = [
            ('成本价', f'{cost_price:.2f}', V4_COLORS['text_primary']),
            ('止损价', f'{stop_loss_price:.2f}', '#EF4444'),
            ('累计盈亏', f'{profit_sign}{profit_loss_pct:.2f}%', V4_COLORS['danger'] if is_profit else V4_COLORS['success']),
            ('距止损', f'{distance_to_sl:.1f}%', risk_color),
        ]
        
        detail_html = ''
        for label, value, color in detail_items:
            detail_html += f'''
            <div class="v4-stock-detail-item">
                <div class="v4-stock-detail-label">{label}</div>
                <div class="v4-stock-detail-value" style="color: {color};">{value}</div>
            </div>
            '''
        
        # 标签
        tags_html = ''
        if risk_level:
            tags_html += f'<span class="v4-tag" style="background: rgba(239, 68, 68, 0.1); color: #EF4444; font-size: 12px; padding: 2px 8px;">{risk_level}风险</span>'
        
        # 行业标签
        industry = stock.get('industry', '')
        if industry:
            tags_html += f'<span class="v4-tag" style="background: rgba(139, 92, 246, 0.1); color: #8B5CF6; font-size: 12px; padding: 2px 8px;">{industry}</span>'
        
        base_class = f"v4-stock-card {self.class_name}".strip()
        return f'''
        <div class="{base_class}">
            <div class="v4-stock-header">
                <div>
                    <div class="v4-stock-name">{name}</div>
                    <div class="v4-stock-code">{code}</div>
                </div>
                <div class="v4-stock-price">
                    <div class="v4-stock-price-value {price_class}">{current_price:.2f}</div>
                    <div class="v4-stock-price-change {price_class}">{sign}{change_pct:.2f}% ({sign}{change:.2f})</div>
                </div>
            </div>
            
            <div class="v4-stock-tags">
                {tags_html}
            </div>
            
            <div class="v4-stock-detail-grid">
                {detail_html}
            </div>
            
            <div class="v4-stock-footer">
                <span style="font-size: 13px; color: #6B7280;">风险度</span>
                <div class="v4-stock-risk-bar">
                    <div class="v4-stock-risk-fill" style="width: {risk_pct}%; background: {risk_color};"></div>
                </div>
                <span class="v4-stock-advice {advice_class}">{advice_label}</span>
            </div>
        </div>
        '''
    
    def render(self) -> str:
        """渲染股票卡片"""
        if self.variant == 'full':
            return self._render_full()
        else:
            return self._render_compact()


class V4TopicCard(V4Component):
    """题材卡片组件"""
    
    def __init__(self, topic_data: Dict[str, Any], 
                 show_radar: bool = True, class_name: str = ""):
        super().__init__(class_name)
        self.topic = topic_data
        self.show_radar = show_radar
        
        self.add_style(f'''
        .v4-topic-card {{
            background: {V4_COLORS['bg_card']};
            border-radius: {V4_RADIUS['lg']};
            padding: 24px;
            border: 1px solid {V4_COLORS['border']};
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
        }}
        .v4-topic-card:hover {{
            box-shadow: {V4_SHADOW['lg']};
            transform: translateY(-4px);
        }}
        .v4-topic-level-badge {{
            position: absolute;
            top: 0;
            right: 0;
            padding: 4px 12px;
            font-size: 12px;
            font-weight: 600;
            color: white;
            border-bottom-left-radius: {V4_RADIUS['lg']};
        }}
        .v4-topic-header {{
            display: flex;
            align-items: center;
            gap: 12px;
            margin-bottom: 16px;
        }}
        .v4-topic-icon {{
            font-size: 32px;
        }}
        .v4-topic-info {{
            flex: 1;
        }}
        .v4-topic-name {{
            font-size: 18px;
            font-weight: 700;
            color: {V4_COLORS['text_primary']};
            margin-bottom: 4px;
        }}
        .v4-topic-score {{
            font-size: 14px;
            color: {V4_COLORS['text_secondary']};
        }}
        .v4-topic-score-value {{
            font-weight: 700;
            color: {V4_COLORS['primary']};
            font-size: 16px;
        }}
        .v4-topic-description {{
            color: {V4_COLORS['text_secondary']};
            font-size: 14px;
            line-height: 1.6;
            margin-bottom: 16px;
        }}
        .v4-topic-stocks {{
            display: flex;
            flex-wrap: wrap;
            gap: 6px;
            margin-bottom: 12px;
        }}
        .v4-topic-footer {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding-top: 12px;
            border-top: 1px solid {V4_COLORS['border']};
        }}
        .v4-topic-catalyst {{
            font-size: 13px;
            color: {V4_COLORS['text_secondary']};
            flex: 1;
        }}
        .v4-topic-action {{
            flex-shrink: 0;
        }}
        ''')
    
    def render(self) -> str:
        level = self.topic.get('level', 'A')
        level_name = self.topic.get('level_name', '')
        name = self.topic.get('name', '')
        icon = self.topic.get('icon', '📊')
        score = self.topic.get('score', 0)
        description = self.topic.get('description', '')
        core_stocks = self.topic.get('core_stocks', [])
        catalyst = self.topic.get('catalyst', '')
        deep_dive_url = self.topic.get('deep_dive_url', '')
        
        # 级别颜色
        level_colors = {
            'S': '#EF4444',
            'A': '#F59E0B',
            'B': '#3B82F6',
            'C': '#6B7280',
        }
        level_color = level_colors.get(level, level_colors['C'])
        
        # 级别标签
        level_badge = f'''
        <div class="v4-topic-level-badge" style="background: {level_color};">
            {level}级 · {level_name}
        </div>
        '''
        
        # 核心股票标签
        stocks_html = ''
        for stock in core_stocks[:5]:
            stocks_html += f'<span class="v4-tag" style="font-size: 12px; padding: 2px 8px; background: rgba(139, 92, 246, 0.1); color: #8B5CF6; border-radius: 12px;">{stock}</span>'
        
        # 深度报告按钮
        action_html = ''
        if deep_dive_url:
            action_html = f'''
            <a href="{deep_dive_url}" class="v4-btn" 
               style="padding: 8px 16px; font-size: 13px; background: linear-gradient(135deg, #8B5CF6, #6366F1); color: white; border-radius: 8px; text-decoration: none;">
                深度分析 →
            </a>
            '''
        
        # 雷达图
        radar_html = ''
        if self.show_radar:
            radar_data = self.topic.get('radar', {})
            if radar_data:
                labels = list(radar_data.keys())
                values = list(radar_data.values())
                radar = V4RadarChart(labels, values, size=140, color=level_color)
                radar_html = f'<div style="text-align: center; margin: 12px 0;">{radar.render()}</div>'
        
        base_class = f"v4-topic-card {self.class_name}".strip()
        return f'''
        <div class="{base_class}">
            {level_badge}
            <div class="v4-topic-header">
                <div class="v4-topic-icon">{icon}</div>
                <div class="v4-topic-info">
                    <div class="v4-topic-name">{name}</div>
                    <div class="v4-topic-score">综合评分: <span class="v4-topic-score-value">{score:.1f}</span> 分</div>
                </div>
            </div>
            {radar_html}
            <div class="v4-topic-description">{description}</div>
            <div class="v4-topic-stocks">{stocks_html}</div>
            <div class="v4-topic-footer">
                <div class="v4-topic-catalyst">💡 {catalyst}</div>
                <div class="v4-topic-action">{action_html}</div>
            </div>
        </div>
        '''


# ============================================================================
# 布局组件
# ============================================================================

class V4Section(V4Component):
    """章节组件
    
    页面的主要内容区块
    """
    
    def __init__(self, title: str, content: str = "", 
                 tag_text: str = "", tag_class: str = "v4-tag-blue",
                 icon: str = "", class_name: str = "",
                 id_attr: str = ""):
        super().__init__(class_name)
        self.title = title
        self.content = content
        self.tag_text = tag_text
        self.tag_class = tag_class
        self.icon = icon
        self.id_attr = id_attr
        
        self.add_style(f'''
        .v4-section {{
            margin-bottom: 24px;
            scroll-margin-top: 80px;
        }}
        .v4-section-header {{
            display: flex;
            align-items: center;
            gap: 12px;
            margin-bottom: 16px;
            padding-bottom: 12px;
            border-bottom: 2px solid {V4_COLORS['border']};
        }}
        .v4-section-title {{
            font-size: 20px;
            font-weight: 700;
            color: {V4_COLORS['text_primary']};
            margin: 0;
            display: flex;
            align-items: center;
            gap: 8px;
        }}
        .v4-section-icon {{
            font-size: 24px;
        }}
        .v4-section-body {{
            padding: 0;
        }}
        ''')
    
    def render(self) -> str:
        # 标题
        title_html = ''
        if self.title:
            icon_html = f'<span class="v4-section-icon">{self.icon}</span>' if self.icon else ''
            tag_html = f'<span class="v4-tag {self.tag_class}" style="font-size: 12px; padding: 2px 10px;">{self.tag_text}</span>' if self.tag_text else ''
            title_html = f'''
            <div class="v4-section-header">
                <h2 class="v4-section-title">{icon_html}{self.title}</h2>
                {tag_html}
            </div>
            '''
        
        id_attr = f' id="{self.id_attr}"' if self.id_attr else ''
        base_class = f"v4-section {self.class_name}".strip()
        
        return f'''
        <section{id_attr} class="{base_class}">
            {title_html}
            <div class="v4-section-body">
                {self.content}
            </div>
        </section>
        '''


class V4PageHeader(V4Component):
    """页面头部组件"""
    
    def __init__(self, title: str, subtitle: str = "", 
                 extra_html: str = "", class_name: str = ""):
        super().__init__(class_name)
        self.title = title
        self.subtitle = subtitle
        self.extra_html = extra_html
        
        self.add_style(f'''
        .v4-page-header {{
            text-align: center;
            margin-bottom: 32px;
            padding: 32px 24px;
            background: linear-gradient(135deg, rgba(139, 92, 246, 0.1), rgba(99, 102, 241, 0.05));
            border-radius: {V4_RADIUS['xl']};
        }}
        .v4-page-header-title {{
            font-size: 32px;
            font-weight: 800;
            color: {V4_COLORS['text_primary']};
            margin: 0 0 8px 0;
            background: linear-gradient(135deg, {V4_COLORS['primary']}, {V4_COLORS['secondary']});
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }}
        .v4-page-header-subtitle {{
            font-size: 16px;
            color: {V4_COLORS['text_secondary']};
            margin: 0;
        }}
        @media (max-width: 640px) {{
            .v4-page-header-title {{
                font-size: 24px;
            }}
            .v4-page-header-subtitle {{
                font-size: 14px;
            }}
        }}
        ''')
    
    def render(self) -> str:
        base_class = f"v4-page-header {self.class_name}".strip()
        return f'''
        <div class="{base_class}">
            <h1 class="v4-page-header-title">{self.title}</h1>
            <p class="v4-page-header-subtitle">{self.subtitle}</p>
            {self.extra_html}
        </div>
        '''


# ============================================================================
# 复合业务组件
# ============================================================================

class V4MarketOverview(V4Component):
    """市场概览模块（V2版，对齐v4_test.html设计）
    
    包含：指数卡片 + 横向柱状图 + 数据网格 + 情绪栏
    """
    
    def __init__(self, market_data: Dict[str, Any], 
                 class_name: str = ""):
        super().__init__(class_name)
        self.market_data = market_data
    
    def render(self) -> str:
        indices = self.market_data.get('indices', [])
        up_count = self.market_data.get('up_count', 0)
        down_count = self.market_data.get('down_count', 0)
        flat_count = self.market_data.get('flat_count', 0)
        sentiment = self.market_data.get('sentiment', '中性')
        sectors = self.market_data.get('hot_sectors', [])
        volume = self.market_data.get('volume', '')
        
        # 主要指数卡片
        index_cards_html = ''
        for idx in indices[:4]:
            name = idx.get('name', '')
            value = idx.get('value', 0)
            change_pct = idx.get('change_pct', 0)
            is_up = change_pct >= 0
            color = '#EF4444' if is_up else '#10B981'
            sign = '+' if is_up else ''
            
            index_cards_html += f'''
            <div style="background: #F9FAFB; border-radius: 12px; padding: 16px; text-align: center;">
                <div style="font-size: 13px; color: #6B7280; margin-bottom: 4px;">{name}</div>
                <div style="font-size: 20px; font-weight: 700; color: {color};">{value:.2f}</div>
                <div style="font-size: 13px; font-weight: 500; color: {color};">{sign}{change_pct:.2f}%</div>
            </div>
            '''
        
        # 涨跌柱状图
        total = up_count + down_count + flat_count
        up_ratio = up_count / total * 100 if total > 0 else 50
        down_ratio = down_count / total * 100 if total > 0 else 50
        flat_ratio = flat_count / total * 100 if total > 0 else 0
        
        bar_html = f'''
        <div style="display: flex; height: 32px; border-radius: 16px; overflow: hidden; margin: 16px 0;">
            <div style="width: {up_ratio}%; background: #EF4444; display: flex; align-items: center; justify-content: center; color: white; font-size: 12px; font-weight: 500;">
                {up_count} 涨
            </div>
            <div style="width: {flat_ratio}%; background: #9CA3AF; display: flex; align-items: center; justify-content: center; color: white; font-size: 12px;">
                {flat_count} 平
            </div>
            <div style="width: {down_ratio}%; background: #10B981; display: flex; align-items: center; justify-content: center; color: white; font-size: 12px; font-weight: 500;">
                {down_count} 跌
            </div>
        </div>
        '''
        
        # 情绪标签
        sentiment_colors = {
            '极度贪婪': '#EF4444',
            '贪婪': '#F59E0B',
            '中性': '#6B7280',
            '恐惧': '#3B82F6',
            '极度恐惧': '#10B981',
        }
        sentiment_color = sentiment_colors.get(sentiment, '#6B7280')
        
        # 热点板块柱状图
        sector_bars = []
        for sector in sectors[:5]:
            sector_bars.append({
                'label': sector.get('name', ''),
                'value': abs(sector.get('change_pct', 0)),
                'color': '#EF4444' if sector.get('change_pct', 0) >= 0 else '#10B981',
            })
        
        sector_chart = V4HorizontalBarChart(sector_bars, show_value=True)
        
        # 数据网格
        grid_items = [
            {'value': volume, 'label': '成交额'},
            {'value': f'{len(sectors)}', 'label': '上涨板块'},
            {'value': sentiment, 'label': '市场情绪', 'color': sentiment_color},
        ]
        data_grid = V4DataGrid(grid_items, columns=3)
        
        base_class = f"v4-market-overview {self.class_name}".strip()
        return f'''
        <div class="{base_class}">
            <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 12px; margin-bottom: 16px;">
                {index_cards_html}
            </div>
            {bar_html}
            {data_grid.render()}
            <div style="margin-top: 16px;">
                <div style="font-size: 14px; font-weight: 600; color: #374151; margin-bottom: 12px;">🔥 热门板块</div>
                {sector_chart.render()}
            </div>
        </div>
        '''


# ============================================================================
# 组件库工具函数
# ============================================================================

def get_all_component_styles() -> str:
    """获取所有组件的样式集合"""
    components = [
        V4Card(),
        V4Tag(""),
        V4Button(""),
        V4RadarChart(['a', 'b', 'c'], [10, 20, 30]),
        V4ProgressBar(0),
        V4DataGrid([]),
        V4HorizontalBarChart([]),
        V4Tabs([]),
        V4Breadcrumb([]),
        V4StockCard({}),
        V4TopicCard({}),
        V4Section("", ""),
        V4PageHeader("", ""),
    ]
    
    styles = []
    for comp in components:
        styles.append(comp.get_styles())
    
    return "\n".join(styles)


def render_card(content: str, **kwargs) -> str:
    """快捷函数：渲染卡片"""
    return V4Card(content, **kwargs).render()


def render_tag(text: str, **kwargs) -> str:
    """快捷函数：渲染标签"""
    return V4Tag(text, **kwargs).render()


def render_section(title: str, content: str, **kwargs) -> str:
    """快捷函数：渲染章节"""
    return V4Section(title, content, **kwargs).render()


def render_radar_chart(labels: list, values: list, **kwargs) -> str:
    """快捷函数：渲染雷达图"""
    return V4RadarChart(labels, values, **kwargs).render()


def render_data_grid(items: list, **kwargs) -> str:
    """快捷函数：渲染数据网格"""
    return V4DataGrid(items, **kwargs).render()
