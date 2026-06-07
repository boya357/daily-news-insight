"""
深度研究报告生成器
专门用于生成产业链、个股深度研究报告
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core.report import Report
from components.layout import Section, Card, SubCard, CardGrid, SplitLayout
from components.data import DataCard, DataGrid, CompareTable, MetricsRow, StatCard, Sparkline, GaugeChart, Tabs, ProgressBar, Badge
from components.special import RiskAlert, QuoteBlock, Timeline, CatalystTag


class DeepDiveGenerator:
    """深度研究报告生成器"""
    
    def __init__(self, title: str, subtitle: str = None):
        self.report = Report(title=title, report_type="industry_chain", subtitle=subtitle)
        self._summary_added = False
    
    def add_summary(self, core_view: str, bull_points: list, bear_points: list):
        """添加核心观点摘要"""
        # 核心观点
        self.report.add_section(
            title="🎯 核心观点",
            content=f'<p class="text-lg leading-relaxed">{core_view}</p>',
        )
        
        # 多空逻辑
        bull_html = "<ul>" + "".join(f"<li class='mb-2'>{p}</li>" for p in bull_points) + "</ul>"
        bear_html = "<ul>" + "".join(f"<li class='mb-2'>{p}</li>" for p in bear_points) + "</ul>"
        
        content = f"""
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div class="bg-green-50 rounded-xl p-4 border border-green-200">
                <h3 class="font-semibold text-green-800 mb-3">📈 看多逻辑</h3>
                <div class="text-green-700 text-sm">{bull_html}</div>
            </div>
            <div class="bg-red-50 rounded-xl p-4 border border-red-200">
                <h3 class="font-semibold text-red-800 mb-3">📉 看空逻辑</h3>
                <div class="text-red-700 text-sm">{bear_html}</div>
            </div>
        </div>
        """
        
        self.report.add_html(content)
        self._summary_added = True
        return self
    
    def add_key_metrics(self, metrics: list):
        """添加关键指标
        
        Args:
            metrics: [(label, value, trend_up?), ...]
        """
        from components.data import MetricsRow
        self.report.add(MetricsRow(metrics))
        return self
    
    def add_data_cards(self, cards: list, cols: int = 4):
        """添加数据卡片网格
        
        Args:
            cards: [DataCard(...) or StatCard(...), ...]
        """
        # 自动检测卡片类型选择合适的网格
        has_stat = any('StatCard' in str(type(c)) for c in cards)
        if has_stat:
            self.report.add(CardGrid(cards, cols))
        else:
            self.report.add(DataGrid(cards, cols))
        return self
    
    def add_stat_cards(self, cards: list, cols: int = 4):
        """添加渐变统计卡片网格（V3.0新版）
        
        Args:
            cards: [StatCard(...), ...]
        """
        self.report.add(CardGrid(cards, cols))
        return self
    
    def add_gauge_chart(self, title: str, value: int, max_value: int = 100, 
                        label: str = None, color: str = "#3b82f6"):
        """添加仪表盘图表
        
        Args:
            title: 仪表盘标题
            value: 当前值
            max_value: 最大值
            label: 底部标签
            color: 主题色
        """
        gauge = GaugeChart(value=value, max_value=max_value, label=label, color=color)
        section = Section(title=title, content=gauge.render(), icon="gauge")
        self.report.add(section)
        return self
    
    def add_tabs_section(self, title: str, tabs: list, icon: str = None):
        """添加标签页内容
        
        Args:
            title: 章节标题
            tabs: [(标签名, 内容HTML), ...]
            icon: 图标
        """
        tabs_comp = Tabs(tabs)
        section = Section(title=title, content=tabs_comp.render(), icon=icon)
        self.report.add(section)
        return self
    
    def add_split_layout(self, title: str, left_content: str, right_content: str,
                        left_title: str = None, right_title: str = None, icon: str = None):
        """添加左右分栏布局
        
        Args:
            title: 章节标题
            left_content: 左侧内容HTML
            right_content: 右侧内容HTML
            left_title: 左侧小标题
            right_title: 右侧小标题
            icon: 图标
        """
        split = SplitLayout(left_content, right_content, left_title, right_title)
        section = Section(title=title, content=split.render(), icon=icon)
        self.report.add(section)
        return self
    
    def add_analysis_section(self, title: str, content: str, icon: str = None):
        """添加分析章节"""
        # 处理内容，保留HTML格式
        self.report.add(Section(title, content, icon=icon))
        return self
    
    def add_competitive_analysis(self, headers: list, rows: list, highlight_rows: list = None):
        """添加竞争格局分析（对比表格）"""
        table = CompareTable(headers=headers, rows=rows, highlight_rows=highlight_rows)
        self.report.add(Section("🏭 竞争格局", table))
        return self
    
    def add_timeline(self, items: list, title: str = "📅 重要事件时间线"):
        """添加时间线"""
        timeline = Timeline(items)
        self.report.add(Section(title, timeline))
        return self
    
    def add_risk_section(self, risks: list):
        """添加风险提示"""
        risk_items = "".join(
            f'<div class="flex items-start space-x-3 mb-3"><span class="text-red-500 mt-0.5">⚠️</span><span>{r}</span></div>'
            for r in risks
        )
        
        content = f'<div class="bg-red-50 rounded-xl p-4 border border-red-200">{risk_items}</div>'
        self.report.add(Section("⚠️ 风险提示", content))
        return self
    
    def add_catalyst_tags(self, tags: list, title: str = "🚀 催化因素"):
        """添加催化标签"""
        tags_html = " ".join(
            f'<span class="inline-block px-3 py-1 m-1 rounded-full text-xs font-medium bg-gradient-to-r from-purple-500 to-pink-500 text-white">{tag}</span>'
            for tag in tags
        )
        self.report.add(Section(title, tags_html))
        return self
    
    def add_chart_section(self, chart_component, title: str = "📊 图表分析"):
        """添加图表章节"""
        self.report.add(Section(title, chart_component))
        return self
    
    def add_conclusion(self, conclusion: str, rating: str = "中性"):
        """添加投资结论"""
        rating_colors = {
            "强烈推荐": "from-green-500 to-emerald-600",
            "推荐": "from-blue-500 to-indigo-600",
            "中性": "from-gray-500 to-gray-600",
            "谨慎": "from-amber-500 to-orange-600",
            "回避": "from-red-500 to-rose-600",
        }
        
        color_class = rating_colors.get(rating, rating_colors["中性"])
        
        content = f"""
        <div class="bg-gradient-to-r {color_class} rounded-2xl p-6 text-white">
            <div class="flex items-center space-x-4 mb-4">
                <span class="text-4xl">💡</span>
                <div>
                    <p class="text-white/80 text-sm">投资评级</p>
                    <p class="text-2xl font-bold">{rating}</p>
                </div>
            </div>
            <p class="leading-relaxed text-white/95">{conclusion}</p>
        </div>
        """
        
        self.report.add(Section("📌 投资结论", content))
        return self
    
    def generate(self) -> str:
        """生成完整报告"""
        return self.report.generate()
    
    def save(self, filepath: str) -> str:
        """保存报告"""
        return self.report.save(filepath)
    
    def validate(self) -> list:
        """验证报告"""
        return self.report.validate()
    
    def publish(self, title: str = None, report_type: str = None, 
                filename: str = None, excerpt: str = None,
                auto_deploy: bool = True) -> dict:
        """
        一键发布报告（归档 + 更新列表 + 校验 + 部署）
        
        Args:
            title: 报告标题（不传则用初始化时的title）
            report_type: 报告类型，默认industry_chain
            filename: 文件名，不传则自动生成
            excerpt: 摘要（用于列表页展示）
            auto_deploy: 是否自动Git部署
            
        Returns:
            发布结果字典
        """
        import sys
        import os
        sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        from workflow import publish_deep_dive
        
        if title is None:
            title = self.report.title
        if report_type is None:
            report_type = self.report.report_type
        
        return publish_deep_dive(
            generator=self,
            title=title,
            report_type=report_type,
            filename=filename,
            excerpt=excerpt,
            auto_deploy=auto_deploy
        )
