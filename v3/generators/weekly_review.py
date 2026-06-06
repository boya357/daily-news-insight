"""
周复盘生成器 - V3.0
一周市场总结 + 数据复盘 + 机会总结 + 下周展望
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.report import Report
from components.layout import Section
from components.data import DataCard, DataGrid, CompareTable
from components.special import RiskAlert


class WeeklyReviewGenerator:
    """
    周复盘生成器
    
    使用方法:
    gen = WeeklyReviewGenerator("2026年第23周", "6月2日-6月6日")
    gen.add_week_summary(summary)
    gen.add_market_data(data)
    gen.add_sector_review(sectors)
    gen.add_next_week_outlook(outlook)
    gen.save("output.html")
    """
    
    def __init__(self, week_label: str, date_range: str = None, subtitle: str = None):
        self.week_label = week_label
        self.date_range = date_range or ""
        self.subtitle = subtitle or f"{week_label} {date_range} · 周度复盘"
        self.report = Report(
            title="周复盘",
            report_type="weekly_review",
            subtitle=self.subtitle
        )
        self._components = []
    
    def add_week_summary(self, summary: str):
        """添加一周总结"""
        section = Section(
            title="📋 一周总结",
            content=f'<div class="prose-content"><p>{summary}</p></div>',
            variant="highlight"
        )
        self._components.append(section)
    
    def add_index_performance(self, indices: list):
        """
        添加指数周表现
        
        Args:
            indices: [{"name": "上证指数", "weekly_change": "+2.35%", "current": "3200", "up": True}, ...]
        """
        cards = []
        for idx in indices:
            variant = "success" if idx.get('up', True) else "danger"
            cards.append(DataCard(
                title=idx['name'],
                value=idx.get('weekly_change', ''),
                trend=idx.get('current', ''),
                trend_up=idx.get('up', True),
                variant=variant
            ))
        
        grid = DataGrid(cards, cols=min(len(cards), 4))
        
        section = Section(
            title="📊 指数周表现",
            content=grid.render()
        )
        self._components.append(section)
    
    def add_sector_review(self, top_sectors: list, bottom_sectors: list):
        """
        添加板块周度表现
        """
        content = '<div class="grid md:grid-cols-2 gap-6">'
        
        # 涨幅榜
        content += '<div>'
        content += '<h4 class="font-bold text-red-600 mb-4">📈 周涨幅榜</h4>'
        content += '<div class="space-y-2">'
        for i, s in enumerate(top_sectors[:5]):
            content += f'''
            <div class="flex items-center justify-between p-3 bg-red-50 rounded-lg">
                <span class="text-gray-800 font-medium">{i+1}. {s["name"]}</span>
                <span class="text-red-600 font-bold">{s.get("change", "")}</span>
            </div>
            '''
        content += '</div></div>'
        
        # 跌幅榜
        content += '<div>'
        content += '<h4 class="font-bold text-green-600 mb-4">📉 周跌幅榜</h4>'
        content += '<div class="space-y-2">'
        for i, s in enumerate(bottom_sectors[:5]):
            content += f'''
            <div class="flex items-center justify-between p-3 bg-green-50 rounded-lg">
                <span class="text-gray-800 font-medium">{i+1}. {s["name"]}</span>
                <span class="text-green-600 font-bold">{s.get("change", "")}</span>
            </div>
            '''
        content += '</div></div>'
        content += '</div>'
        
        section = Section(
            title="🏭 板块周度表现",
            content=content
        )
        self._components.append(section)
    
    def add_hot_topics_review(self, topics: list):
        """
        添加本周热门题材回顾
        """
        content_html = '<div class="space-y-4">'
        for topic in topics:
            content_html += f'''
            <div class="border border-gray-100 rounded-xl p-5">
                <h4 class="font-bold text-gray-800 mb-2">{topic.get("name", "")}</h4>
                <p class="text-gray-600 text-sm mb-3">{topic.get("summary", "")}</p>
                <div class="flex items-center justify-between text-sm">
                    <span class="text-indigo-600">核心标的：{', '.join(topic.get("stocks", []))}</span>
                    <span class="text-gray-400">{topic.get("performance", "")}</span>
                </div>
            </div>
            '''
        content_html += '</div>'
        
        section = Section(
            title="🔥 本周热门题材",
            content=content_html
        )
        self._components.append(section)
    
    def add_important_events(self, events: list):
        """
        添加本周重要事件
        """
        content_html = '<div class="space-y-3">'
        for event in events:
            content_html += f'''
            <div class="flex items-start p-3 bg-gray-50 rounded-lg">
                <span class="text-indigo-600 font-mono text-sm mr-3">{event.get("date", "")}</span>
                <div class="flex-1">
                    <strong class="text-gray-800">{event.get("title", "")}</strong>
                    <p class="text-gray-500 text-sm mt-1">{event.get("content", "")}</p>
                </div>
            </div>
            '''
        content_html += '</div>'
        
        section = Section(
            title="📅 本周重要事件",
            content=content_html
        )
        self._components.append(section)
    
    def add_next_week_outlook(self, outlook: str, key_points: list = None):
        """
        添加下周展望
        """
        points_html = ''
        if key_points:
            points_html = '<ul class="list-disc list-inside text-gray-600 space-y-2 mt-4">'
            for p in key_points:
                points_html += f'<li>{p}</li>'
            points_html += '</ul>'
        
        content = f'<div class="prose-content"><p>{outlook}</p>{points_html}</div>'
        
        section = Section(
            title="🔮 下周展望",
            content=content,
            variant="highlight"
        )
        self._components.append(section)
    
    def add_risk_warning(self, risks: list):
        """添加风险提示"""
        risk_text = "；".join(risks) if isinstance(risks, list) else risks
        risk = RiskAlert(
            level="warning",
            title="⚠️ 风险提示",
            text=risk_text
        )
        self._components.append(risk)
    
    def add_operation_plan(self, plan: str):
        """添加操作计划"""
        section = Section(
            title="📋 下周操作计划",
            content=f'<div class="prose-content"><p>{plan}</p></div>'
        )
        self._components.append(section)
    
    def generate(self) -> str:
        """生成完整HTML"""
        for comp in self._components:
            self.report.add(comp)
        return self.report.generate()
    
    def save(self, filepath: str) -> str:
        """保存到文件"""
        self.generate()
        return self.report.save(filepath)
    
    def validate(self) -> list:
        """验证报告"""
        self.generate()
        return self.report.validate()

    def publish(self, title: str = None, report_type: str = None, 
                filename: str = None, excerpt: str = None,
                auto_deploy: bool = True, docs_root: str = "docs") -> dict:
        """
        一键发布：生成 → 归档 → 更新列表 → 校验 → Git部署
        
        Args:
            title: 报告标题（用于列表页显示）
            report_type: 报告类型（对应REPORT_TYPES的key），默认使用self.report.report_type
            filename: 文件名，不传则自动生成
            excerpt: 摘要（用于列表页展示）
            auto_deploy: 是否自动Git部署
            docs_root: docs目录路径
            
        Returns:
            发布结果字典
        """
        html_content = self.generate()
        
        import sys
        import os
        sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        from workflow import ReportPublisher
        
        rtype = report_type or self.report.report_type
        display_title = title or self.report.title or rtype
        
        publisher = ReportPublisher(docs_root=docs_root)
        return publisher.publish(
            html_content=html_content,
            title=display_title,
            report_type=rtype,
            filename=filename,
            excerpt=excerpt,
            auto_deploy=auto_deploy
        )

