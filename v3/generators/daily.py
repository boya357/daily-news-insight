"""
每日新闻洞察生成器 - V3.0
最核心、最高频的报告类型
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.report import Report
from components.layout import Section
from components.data import DataCard, DataGrid
from components.special import RiskAlert


class DailyReportGenerator:
    """每日新闻洞察生成器"""
    
    def __init__(self, date_str: str, weekday: str = None, subtitle: str = None):
        self.date_str = date_str
        self.weekday = weekday or ""
        sub = subtitle or f"{date_str} {weekday} · 龙空龙策略专用"
        self.report = Report(title="每日新闻洞察", report_type="daily", subtitle=sub)
        self._components = []
    
    def add_focus_point(self, focus: str):
        """添加今日焦点"""
        content = '<div class="text-center py-4">'
        content += '<div class="inline-flex items-center px-4 py-2 rounded-full bg-amber-100 text-amber-800 text-sm">'
        content += '<span class="mr-2">⚠️</span>'
        content += '<strong>今日焦点：</strong>' + focus
        content += '</div></div>'
        
        section = Section(title="", content=content, variant="subtle")
        self._components.append(section)
    
    def add_overseas_market(self, indices: list, key_events: list = None):
        """添加隔夜全球市场"""
        cards = []
        for idx in indices:
            variant = "success" if idx.get('up', True) else "danger"
            cards.append(DataCard(
                title=idx['name'],
                value=idx.get('value', ''),
                trend=idx.get('change', ''),
                trend_up=idx.get('up', True),
                variant=variant
            ))
        
        grid = DataGrid(cards, cols=min(len(cards), 4))
        
        events_html = ''
        if key_events:
            events_html = '<div class="mt-6 space-y-3">'
            for event in key_events:
                tag = event.get('tag', '重磅')
                tag_color = event.get('tag_color', 'red')
                color_map = {
                    'red': 'bg-red-100 text-red-800',
                    'green': 'bg-green-100 text-green-800',
                    'blue': 'bg-blue-100 text-blue-800',
                    'purple': 'bg-purple-100 text-purple-800',
                }
                tag_class = color_map.get(tag_color, 'bg-red-100 text-red-800')
                
                events_html += '<div class="flex items-start">'
                events_html += f'<span class="{tag_class} text-xs px-2 py-1 rounded-full mr-3 mt-1 flex-shrink-0">{tag}</span>'
                events_html += '<div class="flex-1">'
                events_html += f'<strong class="text-gray-800">{event.get("title", "")}</strong>'
                events_html += f'<p class="text-gray-600 text-sm mt-1">{event.get("content", "")}</p>'
                events_html += '</div></div>'
            events_html += '</div>'
        
        content = grid.render() + events_html
        section = Section(title="🌍 隔夜全球市场", content=content)
        self._components.append(section)
    
    def add_import_news(self, news_list: list):
        """添加重要新闻汇总"""
        content_html = '<div class="space-y-4">'
        for news in news_list:
            tag = news.get('tag', '要闻')
            importance = news.get('importance', 'normal')
            
            importance_badge = ''
            if importance == 'high':
                importance_badge = '<span class="hot-tag text-white text-xs px-2 py-1 rounded-full mr-2">重磅</span>'
            
            title = news.get("title", "")
            news_content = news.get("content", "")
            
            content_html += '<div class="news-item p-4 bg-gray-50 rounded-xl hover:bg-gray-100 transition-colors">'
            content_html += '<h4 class="font-bold text-gray-800 mb-2">'
            content_html += importance_badge
            content_html += f'<span class="text-indigo-600 text-sm mr-2">[{tag}]</span>'
            content_html += title
            content_html += '</h4>'
            content_html += f'<p class="text-gray-600 text-sm leading-relaxed">{news_content}</p>'
            content_html += '</div>'
        content_html += '</div>'
        
        section = Section(title="📰 重要新闻汇总", content=content_html)
        self._components.append(section)
    
    def add_sector_analysis(self, sectors: list):
        """添加板块机会分析"""
        content_html = '<div class="space-y-4">'
        for sector in sectors:
            rating = sector.get('rating', '关注')
            rating_color_map = {
                '强烈推荐': 'bg-green-100 text-green-800',
                '推荐': 'bg-blue-100 text-blue-800',
                '关注': 'bg-amber-100 text-amber-800',
                '谨慎': 'bg-red-100 text-red-800',
            }
            rating_color = rating_color_map.get(rating, 'bg-gray-100 text-gray-800')
            
            stock_tags = ''
            for s in sector.get("stocks", []):
                stock_tags += f'<span class="text-xs px-2 py-1 bg-indigo-50 text-indigo-600 rounded">{s}</span>'
            
            sector_name = sector["name"]
            sector_logic = sector.get("logic", "")
            
            content_html += '<div class="border border-gray-100 rounded-xl p-5 hover:shadow-md transition-shadow">'
            content_html += '<div class="flex items-center justify-between mb-3">'
            content_html += f'<h4 class="font-bold text-lg text-gray-800">{sector_name}</h4>'
            content_html += f'<span class="text-xs px-2 py-1 rounded-full {rating_color}">{rating}</span>'
            content_html += '</div>'
            content_html += f'<p class="text-gray-600 text-sm mb-3">💡 {sector_logic}</p>'
            content_html += '<div class="flex flex-wrap gap-2">'
            content_html += '<span class="text-xs text-gray-500">相关标的：</span>'
            content_html += stock_tags
            content_html += '</div></div>'
        content_html += '</div>'
        
        section = Section(title="🎯 板块机会分析", content=content_html)
        self._components.append(section)
    
    def add_holdings_tracking(self, holdings: list):
        """添加持仓跟踪"""
        content_html = '<div class="space-y-3">'
        for h in holdings:
            change_class = 'text-green-600' if h.get('up', True) else 'text-red-600'
            name = h["name"]
            code = h.get("code", "")
            price = h.get("price", "")
            change = h.get("change", "")
            comment = h.get("comment", "")
            
            content_html += '<div class="flex items-center justify-between p-4 bg-gray-50 rounded-xl">'
            content_html += '<div>'
            content_html += f'<span class="font-bold text-gray-800">{name}</span>'
            content_html += f'<span class="text-gray-400 text-sm ml-1">{code}</span>'
            content_html += '</div>'
            content_html += '<div class="text-right">'
            content_html += f'<div class="text-lg font-bold {change_class}">{price}</div>'
            content_html += f'<div class="text-sm {change_class}">{change}</div>'
            content_html += '</div></div>'
            if comment:
                content_html += f'<p class="text-gray-500 text-sm pl-4">💡 {comment}</p>'
        content_html += '</div>'
        
        section = Section(title="💼 持仓跟踪", content=content_html)
        self._components.append(section)
    
    def add_risk_warning(self, risks: list):
        """添加风险提示"""
        risk_text = "；".join(risks) if isinstance(risks, list) else risks
        risk = RiskAlert(level="warning", title="⚠️ 风险提示", text=risk_text)
        self._components.append(risk)
    
    def add_daily_summary(self, summary: str):
        """添加每日总结"""
        content = f'<div class="prose-content"><p>{summary}</p></div>'
        section = Section(title="📝 今日总结", content=content, variant="highlight")
        self._components.append(section)
    
    def add_tomorrow_plan(self, plan: str):
        """添加明日操作计划"""
        content = f'<div class="prose-content"><p>{plan}</p></div>'
        section = Section(title="🎯 明日计划", content=content)
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

