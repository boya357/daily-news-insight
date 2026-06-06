"""
盘中快报生成器 - V3.0
午间市场数据 + 热点解析 + 操作策略
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.report import Report
from components.layout import Section, Card
from components.data import DataCard, DataGrid, MetricsRow
from components.special import RiskAlert, CatalystTag, ButtonGroup


class IntradayGenerator:
    """
    盘中快报生成器
    
    使用方法:
    gen = IntradayGenerator("2026年6月6日")
    gen.add_market_overview(indices, market_status)
    gen.add_hot_topics(topics)
    gen.add_holdings_tracking(holdings)
    gen.add_trading_strategy(strategy)
    gen.save("output.html")
    """
    
    def __init__(self, date_str: str, subtitle: str = None):
        self.date_str = date_str
        self.subtitle = subtitle or f"{date_str} · 午盘速递"
        self.report = Report(
            title="盘中快报",
            report_type="intraday",
            subtitle=self.subtitle
        )
        self._components = []
    
    def add_market_overview(self, indices: list, market_status: str = "震荡"):
        """
        添加市场全景
        
        Args:
            indices: 指数列表 [{"name": "上证指数", "value": "3200.50", "change": "+0.52%", "up": True}, ...]
            market_status: 市场状态描述
        """
        # 指数数据卡片
        cards = []
        for idx in indices:
            variant = "success" if idx.get('up', True) else "danger"
            trend = idx.get('change', '')
            cards.append(DataCard(
                title=idx['name'],
                value=idx['value'],
                trend=trend,
                trend_up=idx.get('up', True),
                variant=variant
            ))
        
        grid = DataGrid(cards, cols=min(len(cards), 4))
        
        section = Section(
            title="📊 市场全景",
            content=grid.render(),
            subtitle=f"午盘市场状态：{market_status}"
        )
        self._components.append(section)
    
    def add_hot_topics(self, topics: list):
        """
        添加市场热点解析
        
        Args:
            topics: 热点列表 [{"tag": "AI", "title": "...", "content": "...", "hot": True}, ...]
        """
        content_html = '<div class="space-y-4">'
        for topic in topics:
            tag_class = 'hot-tag' if topic.get('hot', False) else 'bg-indigo-100 text-indigo-800'
            tag_html = f'<span class="{tag_class} text-white text-xs px-2 py-1 rounded-full mr-2">{topic.get("tag", "热点")}</span>'
            content_html += f'''
            <div class="topic-card p-4 rounded-xl">
                <div class="flex items-start">
                    <div class="flex-1">
                        <h4 class="font-bold text-gray-800 mb-2">{tag_html}{topic.get("title", "")}</h4>
                        <p class="text-gray-600 text-sm leading-relaxed">{topic.get("content", "")}</p>
                    </div>
                </div>
            </div>
            '''
        content_html += '</div>'
        
        section = Section(
            title="🔥 市场热点解析",
            content=content_html
        )
        self._components.append(section)
    
    def add_decline_sectors(self, sectors: list):
        """
        添加领跌板块警示
        
        Args:
            sectors: 领跌板块列表 [{"name": "新能源", "change": "-2.5%", "reason": "..."}, ...]
        """
        content_html = '<div class="space-y-3">'
        for sector in sectors:
            content_html += f'''
            <div class="flex items-center justify-between p-3 bg-red-50 rounded-xl border border-red-100">
                <div>
                    <span class="font-semibold text-gray-800">{sector["name"]}</span>
                    <span class="text-red-600 text-sm ml-2">{sector.get("change", "")}</span>
                </div>
                <p class="text-gray-500 text-sm">{sector.get("reason", "")}</p>
            </div>
            '''
        content_html += '</div>'
        
        section = Section(
            title="⚠️ 领跌板块警示",
            content=content_html
        )
        self._components.append(section)
    
    def add_holdings_tracking(self, holdings: list):
        """
        添加持仓股跟踪
        
        Args:
            holdings: 持仓列表 [{"name": "英维克", "code": "002837", "price": "25.50", "change": "+1.2%", "up": True, "comment": "..."}, ...]
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
            title="💼 持仓股跟踪",
            content=content_html
        )
        self._components.append(section)
    
    def add_trading_strategy(self, strategy: str):
        """
        添加操作策略
        
        Args:
            strategy: 操作策略内容
        """
        section = Section(
            title="🎯 午盘操作策略",
            content=f'<div class="prose-content"><p>{strategy}</p></div>',
            variant="highlight"
        )
        self._components.append(section)
    
    def add_risk_warning(self, risks: list):
        """
        添加风险提示
        
        Args:
            risks: 风险提示列表
        """
        risk = RiskAlert(
            level="warning",
            title="风险提示",
            text="；".join(risks) if isinstance(risks, list) else risks
        )
        self._components.append(risk)
    
    def add_summary(self, summary: str):
        """
        添加市场逻辑总结
        
        Args:
            summary: 总结内容
        """
        section = Section(
            title="📝 市场逻辑总结",
            content=f'<div class="prose-content"><p>{summary}</p></div>'
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

