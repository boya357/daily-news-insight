"""
图表组件 - 基于Chart.js的封装
升级为更美观的图表样式
修复历史问题：maintainAspectRatio 必须为 true，图表高度固定
"""
import json
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from .base import Component
from core.config import COLORS, SIZES

# 图表全局计数器，避免ID冲突
_chart_counter = 0


def _get_chart_id():
    global _chart_counter
    _chart_counter += 1
    return f"chart_{_chart_counter}"


def get_chartjs_cdn() -> str:
    """获取Chart.js CDN引用"""
    return '<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>'


class BaseChart(Component):
    """图表基类"""
    
    def __init__(self, title: str = None, height: str = None):
        super().__init__()
        self.title = title
        self.height = height or SIZES["chart_height"]
        self.chart_id = _get_chart_id()
    
    def _get_options(self) -> dict:
        """获取图表配置选项 - 子类可覆盖"""
        return {
            "responsive": True,
            "maintainAspectRatio": True,  # ⚠️ 必须为true，历史教训
            "plugins": {
                "legend": {
                    "display": True,
                    "position": "bottom",
                    "labels": {
                        "usePointStyle": True,
                        "padding": 20,
                        "font": {
                            "size": 12,
                            "family": "-apple-system, BlinkMacSystemFont, 'PingFang SC', sans-serif"
                        },
                        "color": "#6b7280"
                    }
                },
                "title": {
                    "display": bool(self.title),
                    "text": self.title or "",
                    "font": {
                        "size": 16,
                        "weight": "bold",
                        "family": "-apple-system, BlinkMacSystemFont, 'PingFang SC', sans-serif"
                    },
                    "padding": {"bottom": 20},
                    "color": "#1f2937"
                },
                "tooltip": {
                    "backgroundColor": "rgba(31, 41, 55, 0.95)",
                    "titleFont": {
                        "size": 13,
                        "weight": "600",
                        "family": "-apple-system, BlinkMacSystemFont, 'PingFang SC', sans-serif"
                    },
                    "bodyFont": {
                        "size": 12,
                        "family": "-apple-system, BlinkMacSystemFont, 'PingFang SC', sans-serif"
                    },
                    "padding": 12,
                    "cornerRadius": 8,
                    "displayColors": True
                }
            },
            "scales": {
                "y": {
                    "beginAtZero": False,
                    "grid": {
                        "color": "rgba(0,0,0,0.05)",
                        "drawBorder": False
                    },
                    "ticks": {
                        "font": {
                            "size": 11,
                            "family": "-apple-system, BlinkMacSystemFont, 'PingFang SC', sans-serif"
                        },
                        "color": "#9ca3af"
                    }
                },
                "x": {
                    "grid": {
                        "display": False,
                        "drawBorder": False
                    },
                    "ticks": {
                        "font": {
                            "size": 11,
                            "family": "-apple-system, BlinkMacSystemFont, 'PingFang SC', sans-serif"
                        },
                        "color": "#9ca3af"
                    }
                }
            },
            "elements": {
                "point": {
                    "radius": 3,
                    "hoverRadius": 5,
                    "pointStyle": "circle"
                },
                "line": {
                    "tension": 0.4,
                    "borderWidth": 2
                }
            }
        }
    
    def _get_chart_config(self) -> dict:
        """获取完整的图表配置 - 子类需实现"""
        raise NotImplementedError
    
    def render(self) -> str:
        """渲染图表HTML"""
        config = self._get_chart_config()
        config_json = json.dumps(config, ensure_ascii=False)
        
        return f"""
        <div class="bg-white rounded-2xl p-6 border border-gray-100 shadow-sm">
            <div class="chart-wrapper" style="height: {self.height}px;">
                <canvas id="{self.chart_id}"></canvas>
            </div>
            <script>
                (function() {{
                    const ctx = document.getElementById('{self.chart_id}').getContext('2d');
                    new Chart(ctx, {config_json});
                }})();
            </script>
        </div>
        """


class LineChart(BaseChart):
    """折线图"""
    
    def __init__(self, labels: list, datasets: list, title: str = None, 
                 height: str = None, fill: bool = True):
        super().__init__(title=title, height=height)
        self.labels = labels
        self.datasets = datasets  # [{label, data, color?}, ...]
        self.fill = fill
    
    def _get_chart_config(self) -> dict:
        config = self._get_options()
        
        default_colors = [
            COLORS["primary"],
            COLORS["success"],
            COLORS["warning"],
            COLORS["danger"],
            COLORS["secondary"],
            COLORS["info"],
        ]
        
        chart_datasets = []
        for i, ds in enumerate(self.datasets):
            color = ds.get("color", default_colors[i % len(default_colors)])
            chart_datasets.append({
                "label": ds["label"],
                "data": ds["data"],
                "borderColor": color,
                "backgroundColor": color.replace(")", ", 0.1)").replace("rgb", "rgba") if "rgb" in color else f"{color}20",
                "fill": self.fill,
                "tension": 0.4,
                "pointRadius": 3,
                "pointHoverRadius": 5,
                "borderWidth": 2
            })
        
        config["type"] = "line"
        config["data"] = {
            "labels": self.labels,
            "datasets": chart_datasets
        }
        
        return config


class BarChart(BaseChart):
    """柱状图"""
    
    def __init__(self, labels: list, datasets: list, title: str = None, 
                 horizontal: bool = False, height: str = None):
        super().__init__(title=title, height=height)
        self.labels = labels
        self.datasets = datasets
        self.horizontal = horizontal
    
    def _get_chart_config(self) -> dict:
        config = self._get_options()
        
        default_colors = [
            COLORS["primary"],
            COLORS["success"],
            COLORS["warning"],
            COLORS["danger"],
            COLORS["secondary"],
            COLORS["info"],
        ]
        
        chart_datasets = []
        for i, ds in enumerate(self.datasets):
            color = ds.get("color", default_colors[i % len(default_colors)])
            chart_datasets.append({
                "label": ds["label"],
                "data": ds["data"],
                "backgroundColor": color,
                "borderRadius": 6,
                "barThickness": "flex"
            })
        
        if self.horizontal:
            config["indexAxis"] = "y"
        
        config["type"] = "bar"
        config["data"] = {
            "labels": self.labels,
            "datasets": chart_datasets
        }
        
        return config


class PieChart(BaseChart):
    """饼图/环形图"""
    
    def __init__(self, labels: list, data: list, title: str = None, 
                 donut: bool = True, height: str = None):
        super().__init__(title=title, height=height)
        self.labels = labels
        self.data = data
        self.donut = donut
    
    def _get_options(self) -> dict:
        options = super()._get_options()
        if self.donut:
            options["cutout"] = "65%"
        options["scales"] = {}  # 饼图不需要坐标轴
        return options
    
    def _get_chart_config(self) -> dict:
        config = self._get_options()
        
        default_colors = [
            "#4f46e5",  # indigo
            "#10b981",  # emerald
            "#f59e0b",  # amber
            "#ef4444",  # red
            "#8b5cf6",  # violet
            "#ec4899",  # pink
            "#06b6d4",  # cyan
            "#84cc16",  # lime
            "#f97316",  # orange
            "#6366f1",  # indigo light
        ]
        
        config["type"] = "doughnut" if self.donut else "pie"
        config["data"] = {
            "labels": self.labels,
            "datasets": [{
                "data": self.data,
                "backgroundColor": default_colors[:len(self.data)],
                "borderWidth": 0,
                "borderRadius": 4,
                "hoverOffset": 8
            }]
        }
        
        return config
