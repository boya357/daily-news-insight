"""
明日催化剂生成器 - V3.0 精致增强版
次日重要事件 + 业绩公告 + 数据发布
已整合：StatCard渐变统计卡、Tabs标签页、CardGrid网格、全局动效
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.report import Report
from components.layout import Section, HighlightBox, SubCard, CardGrid, SplitLayout
from components.data import DataCard, DataGrid, StockTags, Badge, StatCard, Sparkline, Tabs, GaugeChart, ProgressBar
from components.special import RiskAlert


class TomorrowCatalystGenerator:
    """明日催化剂生成器 - V3.0精致增强版"""
    
    def __init__(self, date_str: str, subtitle: str = None):
        self.date_str = date_str
        self.subtitle = subtitle or f"{date_str} · 明日催化事件"
        self.report = Report(
            title="明日催化剂",
            report_type="tomorrow_catalyst",
            subtitle=self.subtitle
        )
        self._components = []
    
    def add_key_catalyst(self, catalyst: str):
        """添加核心催化剂"""
        box = HighlightBox(content=catalyst, icon="zap", variant="warning", title="明日核心催化")
        self._components.append(box)
    
    def add_events_calendar(self, events: list):
        """添加明日事件日历（V3.0增强：Tabs分类 + SubCard卡片）
        
        Args:
            events: [{
                'type': 'policy'/'data'/'earnings'/'meeting'/'general',
                'title': '事件标题',
                'description': '事件描述',
                'category': '分类标签'
            }, ...]
        """
        from components.icons import icon_svg
        
        # 按类型分组
        type_groups = {}
        type_names = {
            'policy': '政策事件',
            'data': '数据发布',
            'earnings': '业绩公告',
            'meeting': '重要会议',
            'general': '综合事件'
        }
        type_colors = {
            'policy': ('#3b82f6', '#dbeafe', '#1e40af'),
            'data': ('#10b981', '#dcfce7', '#166534'),
            'earnings': ('#f59e0b', '#fef3c7', '#92400e'),
            'meeting': ('#8b5cf6', '#ede9fe', '#6d28d9'),
            'general': ('#6b7280', '#f3f4f6', '#374151'),
        }
        
        for event in events:
            event_type = event.get('type', 'general')
            if event_type not in type_groups:
                type_groups[event_type] = []
            type_groups[event_type].append(event)
        
        # 生成标签页内容
        tab_list = []
        for event_type, type_events in type_groups.items():
            type_name = type_names.get(event_type, '其他')
            icon_color, bg_color, text_color = type_colors.get(event_type, type_colors['general'])
            
            content_html = '<div style="display: flex; flex-direction: column; gap: 10px;">'
            for event in type_events:
                event_html = f'''
                <div style="background: white; border: 1px solid rgba(0, 0, 0, 0.06);
                           border-radius: 12px; padding: 14px 16px;
                           display: flex; align-items: flex-start;
                           box-shadow: 0 1px 3px rgba(0, 0, 0, 0.04);
                           transition: all 0.3s ease;"
                     onmouseover="this.style.transform='translateY(-2px)'; this.style.boxShadow='0 4px 12px rgba(0,0,0,0.06)';"
                     onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 1px 3px rgba(0, 0, 0, 0.04)';">
                    <div style="width: 32px; height: 32px; 
                               background: linear-gradient(135deg, {icon_color} 0%, {text_color} 100%); 
                               border-radius: 8px; display: flex; align-items: center; justify-content: center; 
                               margin-right: 12px; flex-shrink: 0;">
                        {icon_svg("calendar", 16, "white")}
                    </div>
                    <div style="flex: 1;">
                        <div style="font-size: 14px; font-weight: 600; color: #1f2937; margin-bottom: 4px;">
                            {event.get("title", "")}
                        </div>
                        <div style="font-size: 12px; color: #6b7280; line-height: 1.5;">
                            {event.get("description", "")}
                        </div>
                        <div style="margin-top: 6px;">
                            <span style="display: inline-block; padding: 2px 8px; 
                                       border-radius: 6px; background: {bg_color}; 
                                       color: {text_color}; font-size: 11px; font-weight: 500;">
                                {event.get("category", "事件")}
                            </span>
                        </div>
                    </div>
                </div>'''
                content_html += event_html
            content_html += '</div>'
            
            # 使用SubCard包装
            sub_card = SubCard(content=content_html, variant="white")
            tab_list.append((type_name, sub_card.render()))
        
        # 如果只有一类，不使用Tabs
        if len(tab_list) == 1:
            content = tab_list[0][1]
        else:
            tabs = Tabs(tabs=tab_list, default_index=0)
            content = tabs.render()
        
        section = Section(title="📅 明日事件日历", content=content, icon="calendar")
        self._components.append(section)
    
    def add_earnings_announcements(self, stocks: list):
        """添加业绩公告（V3.0增强：StatCard统计卡）
        
        Args:
            stocks: [{
                'name': '公司名称',
                'code': '股票代码',
                'type': '业绩预告/业绩快报/年报',
                'eps': '每股收益（可选）',
                'growth': '增长率（可选）'
            }, ...]
        """
        cards = []
        for stock in stocks:
            # 副标题信息
            subtitle_parts = []
            if stock.get('code'):
                subtitle_parts.append(stock['code'])
            if stock.get('growth'):
                subtitle_parts.append(stock['growth'])
            subtitle = " · ".join(subtitle_parts) if subtitle_parts else stock.get('type', '业绩公告')
            
            # 决定颜色
            variant = "warning"  # 默认黄色
            if stock.get('growth') and '+' in str(stock['growth']):
                variant = "success"
            elif stock.get('growth') and '-' in str(stock['growth']):
                variant = "danger"
            
            cards.append(StatCard(
                title=stock["name"],
                value=stock.get('type', '业绩公告'),
                subtitle=subtitle,
                icon="dollar-sign",
                variant=variant
            ))
        
        grid = CardGrid(cards, cols=min(len(cards), 3))
        section = Section(title="💰 业绩公告", content=grid.render(), icon="dollar-sign")
        self._components.append(section)
    
    def add_data_release(self, data_list: list):
        """添加重要数据发布（V3.0增强：StatCard统计卡 + 对比展示）
        
        Args:
            data_list: [{
                'name': '数据名称',
                'prev': '前值',
                'expect': '预期值',
                'actual': '实际值（可选，如果已公布）'
            }, ...]
        """
        cards = []
        for data in data_list:
            # 副标题：前值/预期
            subtitle_parts = []
            if data.get('prev'):
                subtitle_parts.append(f"前值: {data['prev']}")
            if data.get('expect'):
                subtitle_parts.append(f"预期: {data['expect']}")
            subtitle = " | ".join(subtitle_parts) if subtitle_parts else "待公布"
            
            # 主要显示值
            main_value = data.get('actual', data.get('expect', '待公布'))
            
            cards.append(StatCard(
                title=data["name"],
                value=main_value,
                subtitle=subtitle,
                icon="bar-chart",
                variant="info"
            ))
        
        grid = CardGrid(cards, cols=min(len(cards), 3))
        section = Section(title="📊 重要数据发布", content=grid.render(), icon="bar-chart")
        self._components.append(section)
    
    def add_impact_analysis(self, impact: str):
        """添加市场影响分析"""
        content = f'<div style="line-height: 1.8; color: #374151; font-size: 14px;">{impact}</div>'
        section = Section(title="🔍 市场影响分析", content=content, icon="search", variant="highlight")
        self._components.append(section)
    
    def add_risk_warning(self, risks: list):
        """添加风险提示"""
        risk_text = "；".join(risks) if isinstance(risks, list) else risks
        risk = RiskAlert(level="warning", title="⚠️ 风险提示", text=risk_text)
        self._components.append(risk)
    
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

    def publish(self, title=None, report_type=None, filename=None, excerpt=None, auto_deploy=True, docs_root="docs"):
        """一键发布"""
        html_content = self.generate()
        import sys, os
        sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        from workflow import ReportPublisher
        rtype = report_type or self.report.report_type
        display_title = title or self.report.title or rtype
        publisher = ReportPublisher(docs_root=docs_root)
        return publisher.publish(html_content=html_content, title=display_title, report_type=rtype, filename=filename, excerpt=excerpt, auto_deploy=auto_deploy)
