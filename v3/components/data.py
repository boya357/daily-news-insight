"""
数据展示组件 - DataCard, DataGrid, CompareTable, MetricsRow
升级为高级感设计
"""
from .base import Component
from core.config import COLORS


class DataCard(Component):
    """
    数据卡片 - 展示关键指标
    """
    
    def __init__(self, title: str, value: str, trend: str = None, 
                 trend_up: bool = True, unit: str = "", 
                 icon: str = None, variant: str = "default"):
        super().__init__()
        self.title = title
        self.value = value
        self.trend = trend
        self.trend_up = trend_up
        self.unit = unit
        self.icon = icon
        self.variant = variant
    
    def render(self) -> str:
        trend_class = "text-green-600" if self.trend_up else "text-red-600"
        trend_icon = "↑" if self.trend_up else "↓"
        trend_html = f'<span class="{trend_class} text-sm font-medium">{trend_icon} {self.trend}</span>' if self.trend else ''
        
        icon_html = f'<span class="text-2xl mb-2">{self.icon}</span>' if self.icon else ''
        
        variants = {
            "default": "bg-white border border-gray-100",
            "primary": "bg-gradient-to-br from-indigo-50 to-purple-50 border border-indigo-100",
            "success": "bg-gradient-to-br from-green-50 to-emerald-50 border border-green-100",
            "warning": "bg-gradient-to-br from-amber-50 to-orange-50 border border-amber-100",
            "danger": "bg-gradient-to-br from-red-50 to-rose-50 border border-red-100",
        }
        
        card_class = variants.get(self.variant, variants["default"])
        
        return f"""
        <div class="{card_class} rounded-xl p-5 text-center shadow-sm hover:shadow-md transition-all duration-300 hover:-translate-y-0.5">
            {icon_html}
            <div class="text-3xl font-bold text-gray-800 mb-1">
                {self.value}<span class="text-sm font-normal text-gray-500 ml-1">{self.unit}</span>
            </div>
            <div class="text-sm text-gray-500 mb-2">{self.title}</div>
            {trend_html}
        </div>
        """


class DataGrid(Component):
    """
    数据卡片网格 - 展示多个数据卡片
    """
    
    def __init__(self, cards: list, cols: int = 4):
        super().__init__()
        self.cards = cards
        self.cols = cols
    
    def render(self) -> str:
        cards_html = "".join(
            card.render() if hasattr(card, 'render') else str(card) 
            for card in self.cards
        )
        
        # 响应式列数
        if self.cols == 2:
            grid_class = "grid grid-cols-1 sm:grid-cols-2 gap-4"
        elif self.cols == 3:
            grid_class = "grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4"
        elif self.cols == 4:
            grid_class = "grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4"
        else:
            grid_class = f"grid grid-cols-2 md:grid-cols-{self.cols} gap-4"
        
        return f"""
        <div class="{grid_class}">
            {cards_html}
        </div>
        """


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
                trend_class = "text-green-600" if trend_up else "text-red-600"
                trend_icon = "↑" if trend_up else "↓"
                trend_html = f'<span class="{trend_class} text-xs ml-1">{trend_icon}</span>'
            
            # 分隔线（最后一个不加）
            border_class = "" if i == len(self.metrics) - 1 else "border-r border-gray-100"
            
            items_html += f"""
                <div class="flex-1 text-center px-4 {border_class}">
                    <div class="text-2xl font-bold text-gray-800">
                        {value}
                        {trend_html}
                    </div>
                    <div class="text-xs text-gray-500 mt-1">{label}</div>
                </div>
            """
        
        return f"""
        <div class="bg-white/80 rounded-xl p-4 border border-gray-100 flex items-center">
            {items_html}
        </div>
        """


class CompareTable(Component):
    """
    对比表格 - 多列数据对比
    升级为更美观的表格样式
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
            f'<th class="px-4 py-3 text-left text-xs font-semibold text-gray-600 uppercase tracking-wider bg-gray-50">{h}</th>'
            for h in self.headers
        )
        
        # 表行
        rows_html = ""
        for i, row in enumerate(self.rows):
            highlight = i in self.highlight_rows
            row_class = "bg-indigo-50/50" if highlight else ("bg-white" if i % 2 == 0 or not self.striped else "bg-gray-50/50")
            
            cells_html = ""
            for j, cell in enumerate(row):
                cell_class = ""
                if self.highlight_col is not None and j == self.highlight_col:
                    cell_class = "font-semibold text-indigo-600"
                
                cells_html += f'<td class="px-4 py-3 text-sm text-gray-700 {cell_class}">{cell}</td>'
            
            rows_html += f'<tr class="{row_class} hover:bg-gray-50 transition-colors">{cells_html}</tr>'
        
        return f"""
        <div class="overflow-x-auto rounded-xl border border-gray-100 shadow-sm">
            <table class="min-w-full divide-y divide-gray-200">
                <thead>
                    <tr>
                        {headers_html}
                    </tr>
                </thead>
                <tbody class="divide-y divide-gray-100">
                    {rows_html}
                </tbody>
            </table>
        </div>
        """
