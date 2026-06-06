"""
盘后速递生成器 - V3.0
收盘数据 + 当日复盘 + 明日展望
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.report import Report
from components.layout import Section
from components.data import DataCard, DataGrid


class AftermarketGenerator:
    """
    盘后速递生成器
    
    使用方法:
    gen = AftermarketGenerator("2026年6月6日")
    gen.add_market_summary(indices, volume)
    gen.add_sector_performance(sectors)
    gen.add_hot_topics(topics)
    gen.add_tomorrow_outlook(outlook)
    gen.save("output.html")
    """
    
    def __init__(self, date_str: str, subtitle: str = None):
        self.date_str = date_str
        self.subtitle = subtitle or f"{date_str} · 收盘速递"
        self.report = Report(
            title="盘后速递",
            report_type="aftermarket",
            subtitle=self.subtitle
        )
        self._components = []
    
    def add_market_summary(self, indices: list, volume: str = None):
        """
        添加市场收盘总结
        
        Args:
            indices: 指数列表
            volume: 成交额描述
        """
        cards = []
        for idx in indices:
            variant = "success" if idx.get('up', True) else "danger"
            cards.append(DataCard(
                title=idx['name'],
                value=idx['value'],
                trend=idx.get('change', ''),
                trend_up=idx.get('up', True),
                variant=variant
            ))
        
        grid = DataGrid(cards, cols=min(len(cards), 4))
        
        extra = f'<p class="text-gray-500 text-sm mt-4 text-center">💵 今日成交额：{volume}</p>' if volume else ''
        content = grid.render() + extra
        
        section = Section(
            title="📊 收盘速览",
            content=content
        )
        self._components.append(section)
    
    def add_sector_performance(self, top_sectors: list, bottom_sectors: list):
        """
        添加板块涨跌幅排行
        
        Args:
            top_sectors: 涨幅居前板块
            bottom_sectors: 跌幅居前板块
        """
        content_html = '<div class="grid md:grid-cols-2 gap-6">'
        
        # 涨幅榜
        content_html += '<div>'
        content_html += '<h4 class="font-bold text-red-600 mb-3">📈 涨幅榜</h4>'
        content_html += '<div class="space-y-2">'
        for i, sector in enumerate(top_sectors[:5]):
            content_html += f'''
            <div class="flex items-center justify-between p-3 bg-red-50 rounded-lg">
                <span class="text-gray-800">{i+1}. {sector["name"]}</span>
                <span class="text-red-600 font-semibold">{sector.get("change", "")}</span>
            </div>
            '''
        content_html += '</div></div>'
        
        # 跌幅榜
        content_html += '<div>'
        content_html += '<h4 class="font-bold text-green-600 mb-3">📉 跌幅榜</h4>'
        content_html += '<div class="space-y-2">'
        for i, sector in enumerate(bottom_sectors[:5]):
            content_html += f'''
            <div class="flex items-center justify-between p-3 bg-green-50 rounded-lg">
                <span class="text-gray-800">{i+1}. {sector["name"]}</span>
                <span class="text-green-600 font-semibold">{sector.get("change", "")}</span>
            </div>
            '''
        content_html += '</div></div>'
        content_html += '</div>'
        
        section = Section(
            title="🏭 板块表现",
            content=content_html
        )
        self._components.append(section)
    
    def add_hot_topics(self, topics: list):
        """
        添加今日热点
        """
        content_html = '<div class="space-y-4">'
        for topic in topics:
            tag = topic.get('tag', '热点')
            content_html += f'''
            <div class="topic-card p-4 rounded-xl">
                <span class="inline-block bg-indigo-100 text-indigo-800 text-xs px-2 py-1 rounded-full mb-2">{tag}</span>
                <h4 class="font-bold text-gray-800 mb-2">{topic.get("title", "")}</h4>
                <p class="text-gray-600 text-sm leading-relaxed">{topic.get("content", "")}</p>
            </div>
            '''
        content_html += '</div>'
        
        section = Section(
            title="🔥 今日热点",
            content=content_html
        )
        self._components.append(section)
    
    def add_holdings_review(self, holdings: list):
        """
        添加持仓复盘
        """
        content_html = '<div class="space-y-3">'
        for h in holdings:
            change_class = 'text-green-600' if h.get('up', True) else 'text-red-600'
            content_html += f'''
            <div class="flex items-center justify-between p-4 bg-gray-50 rounded-xl">
                <div>
                    <span class="font-bold text-gray-800">{h["name"]}</span>
                    <span class="text-gray-400 text-sm ml-1">{h.get("code", "")}</span>
                </div>
                <div class="text-right">
                    <div class="text-lg font-bold {change_class}">{h.get("price", "")}</div>
                    <div class="text-sm {change_class}">{h.get("change", "")}</div>
                </div>
            </div>
            {f'<p class="text-gray-500 text-sm pl-4">💡 {h.get("comment", "")}</p>' if h.get("comment") else ''}
            '''
        content_html += '</div>'
        
        section = Section(
            title="💼 持仓复盘",
            content=content_html
        )
        self._components.append(section)
    
    def add_tomorrow_outlook(self, outlook: str):
        """
        添加明日展望
        """
        section = Section(
            title="🔮 明日展望",
            content=f'<div class="prose-content"><p>{outlook}</p></div>',
            variant="highlight"
        )
        self._components.append(section)
    
    def add_risk_warning(self, risks: list):
        """添加风险提示"""
        from components.special import RiskAlert
        risk = RiskAlert(
            level="warning",
            title="风险提示",
            text="；".join(risks) if isinstance(risks, list) else risks
        )
        self._components.append(risk)
    
    def add_operation_plan(self, plan: str):
        """添加操作计划"""
        section = Section(
            title="📋 操作计划",
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

