"""
S级催化生成器 - V3.0 精致增强版
重大题材深度分析 + 产业链梳理 + 投资机会
已整合：StatCard渐变统计卡、Tabs标签页、SplitLayout分栏、SubCard嵌套卡片、全局动效
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.report import Report
from components.layout import Section, HighlightBox, SubCard, CardGrid, SplitLayout, Card
from components.data import DataCard, DataGrid, KeyPoints, StockTags, CompareTable, Badge, StatCard, Sparkline, Tabs, GaugeChart, ProgressBar
from components.special import RiskAlert, QuoteBlock


class SLevelCatalystGenerator:
    """S级催化生成器 - V3.0精致增强版"""
    
    def __init__(self, date_str: str, catalyst_title: str = None, subtitle: str = None):
        self.date_str = date_str
        self.catalyst_title = catalyst_title or "重大催化事件"
        self.subtitle = subtitle or f"{date_str} · S级催化深度分析"
        self.report = Report(
            title="S级催化",
            report_type="s_level_catalyst",
            subtitle=self.subtitle
        )
        self._components = []
    
    def add_catalyst_overview(self, overview: str, importance: str = "高"):
        """添加催化事件概述"""
        box = HighlightBox(
            content=overview,
            icon="zap",
            variant="danger",
            title=f"⚡ S级催化 - {self.catalyst_title}"
        )
        self._components.append(box)
    
    def add_catalyst_details(self, background: str, trigger: str):
        """添加催化事件详细分析（V3.0增强：SplitLayout左右分栏）
        
        Args:
            background: 事件背景
            trigger: 触发因素
        """
        # 左侧：事件背景
        left_html = f'''
        <div style="background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%); 
                    border-radius: 14px; padding: 20px; height: 100%;
                    border: 1px solid #bae6fd;">
            <div style="display: flex; align-items: center; margin-bottom: 12px;">
                <div style="width: 36px; height: 36px; 
                           background: linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%); 
                           border-radius: 10px; display: flex; align-items: center; justify-content: center; 
                           margin-right: 12px;">
                    📚
                </div>
                <span style="font-size: 16px; font-weight: 700; color: #1e40af;">
                    事件背景
                </span>
            </div>
            <div style="font-size: 13px; color: #374151; line-height: 1.8;">
                {background}
            </div>
        </div>
        '''
        
        # 右侧：触发因素
        right_html = f'''
        <div style="background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%); 
                    border-radius: 14px; padding: 20px; height: 100%;
                    border: 1px solid #fcd34d;">
            <div style="display: flex; align-items: center; margin-bottom: 12px;">
                <div style="width: 36px; height: 36px; 
                           background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%); 
                           border-radius: 10px; display: flex; align-items: center; justify-content: center; 
                           margin-right: 12px;">
                    🔥
                </div>
                <span style="font-size: 16px; font-weight: 700; color: #92400e;">
                    触发因素
                </span>
            </div>
            <div style="font-size: 13px; color: #78350f; line-height: 1.8;">
                {trigger}
            </div>
        </div>
        '''
        
        split = SplitLayout(left=left_html, right=right_html, left_width="50%", gap="16px")
        content = split.render()
        
        section = Section(title="🔍 催化事件详解", content=content, icon="search")
        self._components.append(section)
    
    def add_industry_chain_analysis(self, upstream: list, midstream: list, downstream: list):
        """添加产业链分析（V3.0增强：Tabs标签页分类 + SubCard卡片）
        
        Args:
            upstream: 上游环节列表
            midstream: 中游环节列表
            downstream: 下游环节列表
        """
        from components.icons import icon_svg
        
        def render_chain_layer(items, color_from, color_to):
            """渲染单个产业链层级"""
            items_html = '<div style="display: flex; flex-direction: column; gap: 10px;">'
            for item in items:
                stocks_html = ''
                if item.get('stocks'):
                    tags = StockTags(item['stocks'], label="核心标的")
                    stocks_html = tags.render()
                
                item_html = f'''
                <div style="background: white; border-radius: 12px; padding: 14px 16px;
                          box-shadow: 0 1px 3px rgba(0,0,0,0.05);
                          border: 1px solid rgba(0,0,0,0.04);
                          transition: all 0.3s ease;"
                     onmouseover="this.style.transform='translateY(-2px)'; this.style.boxShadow='0 4px 12px rgba(0,0,0,0.08)';"
                     onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 1px 3px rgba(0,0,0,0.05)';">
                    <div style="font-size: 14px; font-weight: 600; color: #1f2937; margin-bottom: 6px;">
                        {item.get("name", "")}
                    </div>
                    <div style="font-size: 12px; color: #6b7280; line-height: 1.5; margin-bottom: 8px;">
                        {item.get("desc", "")}
                    </div>
                    {stocks_html}
                </div>
                '''
                items_html += item_html
            items_html += '</div>'
            return items_html
        
        # 生成三个标签页
        tab_list = [
            ("上游", render_chain_layer(upstream, "#10b981", "#059669")),
            ("中游", render_chain_layer(midstream, "#3b82f6", "#2563eb")),
            ("下游", render_chain_layer(downstream, "#f59e0b", "#d97706")),
        ]
        
        tabs = Tabs(tabs=tab_list, default_index=1)  # 默认显示中游
        content = tabs.render()
        
        section = Section(title="🔗 产业链梳理", content=content, icon="git-branch")
        self._components.append(section)
    
    def add_investment_opportunities(self, opportunities: list, view_mode: str = "card"):
        """添加投资机会分析（V3.0增强：支持卡片模式/标签页模式）
        
        Args:
            opportunities: 投资机会列表
            view_mode: "card"（卡片列表）或 "tab"（按优先级标签页）
        """
        from components.icons import icon_svg
        
        if view_mode == "tab":
            # 按优先级分组
            priority_groups = {}
            for opp in opportunities:
                priority = opp.get('priority', '中')
                if priority not in priority_groups:
                    priority_groups[priority] = []
                priority_groups[priority].append(opp)
            
            # 按优先级排序：高 > 中 > 低
            priority_order = ['高', '中', '低']
            tab_list = []
            for p in priority_order:
                if p in priority_groups:
                    tab_content = self._render_opportunity_cards(priority_groups[p])
                    tab_list.append((f"{p}优先级", tab_content))
            
            tabs = Tabs(tabs=tab_list, default_index=0)
            content = tabs.render()
        else:
            # 卡片列表模式
            content = self._render_opportunity_cards(opportunities)
        
        section = Section(title="💰 投资机会分析", content=content, icon="dollar-sign")
        self._components.append(section)
    
    def _render_opportunity_cards(self, opportunities: list) -> str:
        """渲染投资机会卡片列表（内部方法）"""
        from components.icons import icon_svg
        
        content_html = '<div style="display: flex; flex-direction: column; gap: 14px;">'
        for opp in opportunities:
            priority = opp.get('priority', '高')
            priority_colors = {
                '高': ('#ef4444', '#fee2e2', '#991b1b'),
                '中': ('#f59e0b', '#fef3c7', '#92400e'),
                '低': ('#3b82f6', '#dbeafe', '#1e40af'),
            }
            p_color, p_bg, p_text = priority_colors.get(priority, priority_colors['中'])
            
            stocks_html = ''
            if opp.get('stocks'):
                tags = StockTags(opp['stocks'], label="核心标的")
                stocks_html = tags.render()
            
            card_content = f'''
            <div style="display: flex; align-items: flex-start; margin-bottom: 10px;">
                <div style="flex: 1;">
                    <span style="font-size: 16px; font-weight: 700; color: #1f2937;">
                        {opp.get("name", "")}
                    </span>
                </div>
                <span style="padding: 4px 10px; border-radius: 20px; 
                           font-size: 11px; font-weight: 700;
                           background: linear-gradient(135deg, {p_color} 0%, {p_text} 100%); 
                           color: white;">
                    {priority}优先级
                </span>
            </div>
            <div style="font-size: 13px; color: #6b7280; line-height: 1.7; margin-bottom: 10px;">
                {opp.get("logic", "")}
            </div>
            {stocks_html}
            '''
            
            sub_card = SubCard(content=card_content, variant="white")
            # 左边框颜色
            card_html = f'''
            <div style="border-left: 4px solid {p_color}; border-radius: 0 12px 12px 0;
                       transition: all 0.3s ease;"
                 onmouseover="this.style.transform='translateX(4px)';"
                 onmouseout="this.style.transform='translateX(0)';">
                {sub_card.render()}
            </div>
            '''
            content_html += card_html
        content_html += '</div>'
        return content_html
    
    def add_risk_warning(self, risks: list):
        """添加风险提示"""
        risk = RiskAlert(level="danger", title="⚠️ 重要风险提示", text="；".join(risks) if isinstance(risks, list) else risks)
        self._components.append(risk)
    
    def add_investment_strategy(self, strategy: str):
        """添加投资策略建议"""
        content = f'<div style="line-height: 1.8; color: #374151; font-size: 14px;">{strategy}</div>'
        section = Section(title="🎯 投资策略建议", content=content, icon="target", variant="highlight")
        self._components.append(section)
    
    def generate(self) -> str:
        """生成完整HTML"""
        self.report.components.clear()  # 清空避免重复添加
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
