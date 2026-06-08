"""
周末速递生成器 - V3.0 精致增强版
周末资讯汇总 + 政策解读 + 下周题材预判
已整合：StatCard渐变统计卡、Tabs标签页、SubCard嵌套卡片、CardGrid网格、全局动效
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.report import Report
from components.layout import Section, HighlightBox, SubCard, CardGrid, SplitLayout
from components.data import DataCard, DataGrid, StockTags, Badge, StatCard, Sparkline, Tabs, GaugeChart, ProgressBar
from components.special import RiskAlert, NewsItem


class WeekendExpressGenerator:
    """周末速递生成器 - V3.0精致增强版"""
    
    def __init__(self, date_str: str, subtitle: str = None):
        self.date_str = date_str
        self.subtitle = subtitle or f"{date_str} · 周末资讯速递"
        self.report = Report(
            title="周末速递",
            report_type="weekend_express",
            subtitle=self.subtitle
        )
        self._components = []
    
    def add_weekend_highlights(self, highlights: list):
        """添加周末要闻亮点（V3.0增强：NewsItem组件 + 分类标签）
        
        Args:
            highlights: [{
                'icon': '📰',
                'title': '新闻标题',
                'content': '新闻内容',
                'tag': '标签',
                'importance': 'high'/'normal',
                'source': '来源',
                'time': '时间'
            }, ...]
        """
        content = '<div style="display: flex; flex-direction: column; gap: 4px;">'
        for h in highlights:
            importance = h.get('importance', 'normal')
            tag = h.get('tag', '要闻')
            
            item = NewsItem(
                title=h.get("title", ""),
                content=h.get("content", ""),
                time=h.get("time", ""),
                source=h.get("source", ""),
                tag=tag,
                tag_variant="primary" if importance == "high" else "default",
                important=(importance == "high")
            )
            content += item.render()
        content += '</div>'
        
        section = Section(title="📰 周末要闻速览", content=content, icon="newspaper")
        self._components.append(section)
    
    def add_policy_interpretation(self, policies: list, view_mode: str = "card"):
        """添加政策解读（V3.0增强：支持卡片/标签页模式）
        
        Args:
            policies: [{
                'title': '政策标题',
                'content': '政策内容',
                'impact': '影响解读',
                'sector': '影响板块',
                'level': '国家/行业/地方'
            }, ...]
            view_mode: "card"（卡片列表）或 "tab"（按层级标签页）
        """
        if view_mode == "tab":
            # 按层级分组
            level_groups = {}
            for policy in policies:
                level = policy.get('level', '行业')
                if level not in level_groups:
                    level_groups[level] = []
                level_groups[level].append(policy)
            
            tab_list = []
            for level, level_policies in level_groups.items():
                tab_content = self._render_policy_cards(level_policies)
                tab_list.append((level, tab_content))
            
            tabs = Tabs(tabs=tab_list, default_index=0)
            content = tabs.render()
        else:
            content = self._render_policy_cards(policies)
        
        section = Section(title="🏛️ 政策解读", content=content, icon="building")
        self._components.append(section)
    
    def _render_policy_cards(self, policies: list) -> str:
        """渲染政策卡片列表（内部方法）"""
        content_html = '<div style="display: flex; flex-direction: column; gap: 14px;">'
        for policy in policies:
            # 影响板块标签
            sector_html = ''
            if policy.get('sector'):
                sectors = policy['sector'].split(',') if isinstance(policy['sector'], str) else policy['sector']
                sector_tags = []
                for s in sectors[:3]:  # 最多显示3个
                    sector_tags.append(f'<span style="display: inline-block; padding: 2px 8px; border-radius: 6px; background: #dbeafe; color: #1e40af; font-size: 11px; font-weight: 500; margin-right: 4px;">{s.strip()}</span>')
                sector_html = '<div style="margin-top: 10px;">' + ''.join(sector_tags) + '</div>'
            
            card_content = f'''
            <div style="font-size: 15px; font-weight: 600; color: #1f2937; margin-bottom: 8px;">
                {policy.get("title", "")}
            </div>
            <div style="font-size: 13px; color: #6b7280; line-height: 1.7; margin-bottom: 8px;">
                {policy.get("content", "")}
            </div>
            <div style="font-size: 12px; color: #3b82f6; font-weight: 500; line-height: 1.6;">
                💡 影响解读：{policy.get("impact", "")}
            </div>
            {sector_html}
            '''
            
            sub_card = SubCard(content=card_content, variant="white")
            # 左边框蓝色
            card_html = f'''
            <div style="border-left: 4px solid #3b82f6; border-radius: 0 12px 12px 0;
                       transition: all 0.3s ease;"
                 onmouseover="this.style.transform='translateX(4px)';"
                 onmouseout="this.style.transform='translateX(0)';">
                {sub_card.render()}
            </div>
            '''
            content_html += card_html
        content_html += '</div>'
        return content_html
    
    def add_next_week_topics(self, topics: list, view_mode: str = "card"):
        """添加下周题材预判（V3.0增强：支持卡片/标签页模式 + 渐变评级）
        
        Args:
            topics: [{
                'name': '题材名称',
                'probability': '高确定性/中确定性/低确定性',
                'logic': '核心逻辑',
                'stocks': ['标的1', '标的2', ...],
                'category': '分类',
                'rating': '强烈推荐/推荐/关注'
            }, ...]
            view_mode: "card"（卡片列表）或 "tab"（按分类标签页）
        """
        if view_mode == "tab":
            # 按分类分组
            category_groups = {}
            for topic in topics:
                cat = topic.get('category', '其他')
                if cat not in category_groups:
                    category_groups[cat] = []
                category_groups[cat].append(topic)
            
            tab_list = []
            for cat, cat_topics in category_groups.items():
                tab_content = self._render_topic_cards(cat_topics)
                tab_list.append((cat, tab_content))
            
            tabs = Tabs(tabs=tab_list, default_index=0)
            content = tabs.render()
        else:
            content = self._render_topic_cards(topics)
        
        section = Section(title="🔮 下周题材预判", content=content, icon="zap", variant="highlight")
        self._components.append(section)
    
    def _render_topic_cards(self, topics: list) -> str:
        """渲染题材卡片列表（内部方法）"""
        content_html = '<div style="display: flex; flex-direction: column; gap: 12px;">'
        for topic in topics:
            probability = topic.get('probability', '高确定性')
            rating = topic.get('rating', '关注')
            
            # 概率颜色
            prob_colors = {
                '高确定性': ('linear-gradient(135deg, #10b981 0%, #059669 100%)', 'white'),
                '中确定性': ('linear-gradient(135deg, #f59e0b 0%, #d97706 100%)', 'white'),
                '低确定性': ('linear-gradient(135deg, #6b7280 0%, #4b5563 100%)', 'white'),
            }
            prob_bg, prob_color = prob_colors.get(probability, prob_colors['中确定性'])
            
            stocks_html = ''
            if topic.get('stocks'):
                tags = StockTags(topic['stocks'], label="受益标的")
                stocks_html = tags.render()
            
            card_content = f'''
            <div style="display: flex; align-items: center; margin-bottom: 10px;">
                <span style="font-size: 16px; font-weight: 700; color: #166534; flex: 1;">
                    {topic.get("name", "")}
                </span>
                <span style="padding: 5px 12px; border-radius: 20px; 
                           font-size: 11px; font-weight: 700;
                           background: {prob_bg}; color: {prob_color};">
                    {probability}
                </span>
            </div>
            <div style="font-size: 13px; color: #15803d; line-height: 1.6; margin-bottom: 10px;">
                {topic.get("logic", "")}
            </div>
            {stocks_html}
            '''
            
            # 使用绿色渐变背景的卡片
            card_html = f'''
            <div style="background: linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%); 
                        border: 1px solid #bbf7d0; border-radius: 14px; padding: 16px 18px;
                        transition: all 0.3s ease;"
                 onmouseover="this.style.transform='translateY(-2px)'; this.style.boxShadow='0 4px 12px rgba(16, 185, 129, 0.15)';"
                 onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='none';">
                {card_content}
            </div>
            '''
            content_html += card_html
        content_html += '</div>'
        return content_html
    
    def add_risk_warning(self, risks: list):
        """添加风险提示"""
        risk_text = "；".join(risks) if isinstance(risks, list) else risks
        risk = RiskAlert(level="warning", title="⚠️ 风险提示", text=risk_text)
        self._components.append(risk)
    
    def add_trading_plan(self, plan: str):
        """添加下周操作计划"""
        content = f'<div style="line-height: 1.8; color: #374151; font-size: 14px;">{plan}</div>'
        section = Section(title="🎯 下周操作计划", content=content, icon="target")
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
