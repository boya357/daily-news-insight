"""
S级催化题材列表页 - V4版（使用V4组件库）
展示所有S级和A级题材卡片，点击进入深度研究报告
"""
import sys
import os
import json
from datetime import datetime
from typing import List, Dict, Optional

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from generators.v4_base import V4BaseGenerator
from components.v4_components import (
    V4PageHeader, V4Section, V4TopicCard, V4Tag, V4DataGrid, V4Tabs
)


class SCatalystTopicsV4(V4BaseGenerator):
    """S级催化题材列表页生成器"""
    
    def __init__(self, data_dir: str = "data"):
        super().__init__(data_dir)
        self.page_title = "S级催化 · 题材研究"
        self.page_subtitle = "深度挖掘超级题材机会 · 把握市场主线行情"
        self.active_nav_key = "s_catalyst"
        self.toc_items = [
            ("S级题材", "section-s-level"),
            ("A级题材", "section-a-level"),
            ("市场概览", "section-market"),
            ("配置策略", "section-strategy"),
        ]
        self.topics_data = None
        self._load_topics_data()
    
    def _load_topics_data(self):
        """加载题材数据"""
        possible_paths = [
            os.path.join(self.data_dir, 'topics.json'),
            '/app/data/所有对话/主对话/data/topics.json',
        ]
        
        for path in possible_paths:
            if os.path.exists(path):
                with open(path, 'r', encoding='utf-8') as f:
                    self.topics_data = json.load(f)
                break
    
    def _convert_topic_to_card_data(self, topic: Dict) -> Dict:
        """将题材数据转换为V4TopicCard需要的格式"""
        dimension_scores = topic.get('dimension_scores', {})
        
        # 构建雷达图数据
        radar = {}
        if isinstance(dimension_scores, dict):
            for key, value in dimension_scores.items():
                if isinstance(value, (int, float)):
                    radar[key] = value
                elif isinstance(value, dict) and 'score' in value:
                    radar[key] = value['score']
        
        # 如果没有雷达数据，使用默认值
        if not radar:
            radar = {
                '政策': 85,
                '产业': 80,
                '资金': 75,
                '情绪': 78,
                '估值': 70,
                '催化': 82,
            }
        
        # 核心标的
        core_stocks = []
        for stock_type in ['leader_stock', 'mid_cap_stock', 'flexible_stock']:
            stock = topic.get(stock_type, '')
            if stock:
                core_stocks.append(stock)
        if not core_stocks:
            core_stocks = topic.get('target_stocks', [])[:5]
        
        # 级别名称
        level = topic.get('level', 'B')
        level_names = {
            'S': '最强主线',
            'A': '核心题材',
            'B': '关注题材',
            'C': '观察题材',
        }
        
        # 总分
        score = topic.get('total_score', 0)
        if not score:
            score = sum(radar.values()) / len(radar) if radar else 75
        
        # 最新催化
        catalyst = topic.get('recent_catalyst', '')
        if not catalyst:
            events = topic.get('catalyst_events', [])
            if events and isinstance(events, list):
                catalyst = events[0].get('event', '') if isinstance(events[0], dict) else str(events[0])
        
        # 深度报告链接
        topic_id = topic.get('id', '')
        deep_dive_url = f"topic_deep_dive_{topic_id}.html" if topic_id else "#"
        
        return {
            'level': level,
            'level_name': level_names.get(level, '题材'),
            'name': topic.get('name', '未知题材'),
            'icon': topic.get('icon', '📊'),
            'score': float(score),
            'description': topic.get('description', topic.get('core_logic', '')),
            'core_stocks': core_stocks[:5],
            'catalyst': catalyst,
            'radar': radar,
            'deep_dive_url': deep_dive_url,
        }
    
    def render_topic_cards(self, level: str) -> str:
        """渲染指定级别的题材卡片列表"""
        if not self.topics_data:
            return '<div class="v4-card"><p style="color: #64748B; text-align: center; padding: 40px;">暂无题材数据</p></div>'
        
        key_map = {
            'S': 's_level_topics',
            'A': 'a_level_topics',
            'B': 'b_level_topics',
        }
        
        topics_key = key_map.get(level, 'b_level_topics')
        topics = self.topics_data.get(topics_key, [])
        
        if not topics:
            return f'<div class="v4-card"><p style="color: #64748B; text-align: center; padding: 40px;">暂无{level}级题材</p></div>'
        
        # 转换为卡片数据并渲染
        cards_html = '<div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(350px, 1fr)); gap: 20px;">'
        for topic in topics:
            card_data = self._convert_topic_to_card_data(topic)
            card = V4TopicCard(card_data, show_radar=True)
            cards_html += card.render()
        cards_html += '</div>'
        
        return cards_html
    
    def render_market_overview_section(self) -> str:
        """渲染市场概览部分"""
        if not self.market_result:
            return ""
        
        # 简单的市场数据展示
        up_count = getattr(self.market_result, 'up_count', 0)
        down_count = getattr(self.market_result, 'down_count', 0)
        sentiment = getattr(self.market_result, 'sentiment', None)
        sentiment_level = getattr(sentiment, 'sentiment_level', '中性') if sentiment else '中性'
        
        grid_items = [
            {'value': f'{up_count}', 'label': '上涨家数', 'color': '#EF4444'},
            {'value': f'{down_count}', 'label': '下跌家数', 'color': '#10B981'},
            {'value': sentiment_level, 'label': '市场情绪', 'color': '#F59E0B'},
            {'value': f'{len(self.topics_data.get("s_level_topics", []))}', 'label': 'S级题材', 'color': '#8B5CF6'},
            {'value': f'{len(self.topics_data.get("a_level_topics", []))}', 'label': 'A级题材', 'color': '#F59E0B'},
            {'value': f'{len(self.topics_data.get("b_level_topics", []))}', 'label': 'B级题材', 'color': '#6B7280'},
        ]
        
        data_grid = V4DataGrid(grid_items, columns=6)
        
        section = V4Section(
            title="🌐 市场概览",
            icon="",
            content=data_grid.render(),
            tag_text="数据看板",
            id_attr="section-market"
        )
        
        return section.render()
    
    def render_strategy_section(self) -> str:
        """渲染配置策略部分"""
        if not self.topics_data:
            return ""
        
        strategy = self.topics_data.get('allocation_strategy', {})
        
        if isinstance(strategy, str):
            strategy_text = strategy
        elif isinstance(strategy, dict):
            strategy_text = strategy.get('summary', strategy.get('description', ''))
        else:
            strategy_text = ""
        
        if not strategy_text:
            strategy_text = "当前市场处于结构性行情，建议重点配置S级主线题材，同时关注A级题材的轮动机会。严格执行止损纪律，控制单一个股仓位。"
        
        content = f'''
        <div class="v4-card" style="padding: 24px;">
            <div style="display: flex; align-items: flex-start; gap: 16px;">
                <div style="font-size: 40px;">💡</div>
                <div>
                    <h3 style="margin: 0 0 8px 0; color: #1F2937; font-size: 18px;">配置策略建议</h3>
                    <p style="margin: 0; color: #4B5563; line-height: 1.8;">{strategy_text}</p>
                </div>
            </div>
        </div>
        '''
        
        section = V4Section(
            title="📋 配置策略",
            icon="",
            content=content,
            tag_text="投资建议",
            id_attr="section-strategy"
        )
        
        return section.render()
    
    def render_content(self) -> str:
        """渲染页面主体内容"""
        # 页面头部
        header = V4PageHeader(
            title=self.page_title,
            subtitle=self.page_subtitle,
        )
        
        # 快速统计
        s_count = len(self.topics_data.get('s_level_topics', [])) if self.topics_data else 0
        a_count = len(self.topics_data.get('a_level_topics', [])) if self.topics_data else 0
        b_count = len(self.topics_data.get('b_level_topics', [])) if self.topics_data else 0
        
        stats_html = f'''
        <div style="margin-bottom: 32px;">
            <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px; text-align: center;">
                <div style="background: linear-gradient(135deg, rgba(239, 68, 68, 0.1), rgba(239, 68, 68, 0.05)); border-radius: 16px; padding: 24px;">
                    <div style="font-size: 36px; font-weight: 800; color: #EF4444;">{s_count}</div>
                    <div style="font-size: 14px; color: #6B7280; margin-top: 4px;">S级题材</div>
                </div>
                <div style="background: linear-gradient(135deg, rgba(245, 158, 11, 0.1), rgba(245, 158, 11, 0.05)); border-radius: 16px; padding: 24px;">
                    <div style="font-size: 36px; font-weight: 800; color: #F59E0B;">{a_count}</div>
                    <div style="font-size: 14px; color: #6B7280; margin-top: 4px;">A级题材</div>
                </div>
                <div style="background: linear-gradient(135deg, rgba(107, 114, 128, 0.1), rgba(107, 114, 128, 0.05)); border-radius: 16px; padding: 24px;">
                    <div style="font-size: 36px; font-weight: 800; color: #6B7280;">{b_count}</div>
                    <div style="font-size: 14px; color: #6B7280; margin-top: 4px;">B级题材</div>
                </div>
            </div>
        </div>
        '''
        
        # S级题材
        s_cards = self.render_topic_cards('S')
        s_section = V4Section(
            title="🚀 S级题材",
            icon="",
            content=s_cards,
            tag_text=f"{s_count}个主线",
            id_attr="section-s-level"
        )
        
        # A级题材
        a_cards = self.render_topic_cards('A')
        a_section = V4Section(
            title="⭐ A级题材",
            icon="",
            content=a_cards,
            tag_text=f"{a_count}个核心",
            id_attr="section-a-level"
        )
        
        # 市场概览
        market_section = self.render_market_overview_section()
        
        # 配置策略
        strategy_section = self.render_strategy_section()
        
        return f'''
        {header.render()}
        {stats_html}
        {s_section.render()}
        {a_section.render()}
        {market_section}
        {strategy_section}
        '''
    
    def generate(self) -> str:
        """生成完整页面"""
        return super().generate()


def generate_page(output_path: str = None):
    """生成S级催化题材列表页"""
    generator = SCatalystTopicsV4(data_dir='data')
    html = generator.generate()
    
    if output_path is None:
        output_path = '/app/data/所有对话/主对话/docs/s_catalyst_topics_v4.html'
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"✅ S级催化题材列表页已生成: {output_path}")
    print(f"   文件大小: {os.path.getsize(output_path)} 字节")
    
    return output_path


if __name__ == '__main__':
    generate_page()
