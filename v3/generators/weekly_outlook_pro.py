"""
周三前瞻生成器 - Pro版
基于Pro组件库重构，深色玻璃态风格
周中展望 + 题材预判 + 操作策略
V3.5升级：集成Tab切换、卡片组、数据网格通用组件
"""
import sys
import os
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from components.pro import GlassCard
from generators.report_pro_base import ReportProGenerator


class WeeklyOutlookProGenerator(ReportProGenerator):
    """周三前瞻生成器 - Pro版"""
    
    def __init__(self, date_str: str = None, data_dir: str = "data"):
        date = date_str or datetime.now().strftime('%Y-%m-%d')
        super().__init__(
            title="周三前瞻",
            report_type="weekly_outlook",
            subtitle="周中展望 · 题材预判 · 操作策略",
            date_str=date,
            data_dir=data_dir,
        )
        # 设置导航栏高亮
        self.active_page = "周三前瞻"
    
    def add_midweek_summary(self, summary: str):
        """添加周中总结"""
        content = f'''
            <div class="bg-gradient-to-r from-blue-500/20 to-purple-500/20 border border-blue-500/30 rounded-xl p-5">
                <div class="flex items-center gap-2 mb-3">
                    <span class="text-2xl">📌</span>
                    <span class="text-white font-bold">周中核心观察</span>
                </div>
                <p class="text-white/80 leading-relaxed">
                    {summary}
                </p>
            </div>
        '''
        self.add_section("周中核心观察", content, "📌")
    
    def add_market_status(self, indices: list):
        """添加当前市场状态 - 使用DataGrid组件"""
        data_items = []
        for idx in indices:
            name = idx.get('name', '')
            value = idx.get('value', '--')
            change = idx.get('change', '')
            up = idx.get('up', True)
            
            color_class = 'text-green-400' if up else 'text-red-400'
            
            data_items.append({
                'title': name,
                'value': str(value),
                'desc': f'<span class="{color_class} font-semibold">{change}</span>',
                'icon': '📈' if up else '📉'
            })
        
        content = self.create_data_grid(items=data_items, cols=4)
        self.add_section("周中市场概览", content, "📊")
    
    def add_focus_topics(self, topics: list):
        """添加重点关注题材 - 使用Tab切换+卡片组"""
        # 按关注度分类
        categories = {}
        for topic in topics:
            attention = topic.get('attention', '重点关注')
            if attention not in categories:
                categories[attention] = []
            categories[attention].append(topic)
        
        # 生成Tab内容
        tabs = []
        for attention, att_topics in categories.items():
            cards = []
            for topic in att_topics:
                name = topic.get('name', '')
                logic = topic.get('logic', '')
                stocks = topic.get('stocks', [])
                
                stocks_html = ''
                if stocks:
                    stocks_html = '<div class="flex flex-wrap gap-2 mt-3">'
                    for stock in stocks:
                        stocks_html += f'<span class="text-xs bg-blue-500/20 text-blue-400 px-2 py-1 rounded-md border border-blue-500/30">{stock}</span>'
                    stocks_html += '</div>'
                
                card_content = f'''
                <div class="flex items-center gap-2 mb-2">
                    <span class="text-lg">👁️</span>
                    <span class="text-white font-semibold">{name}</span>
                </div>
                <p class="text-white/60 text-sm leading-relaxed">
                    {logic}
                </p>
                {stocks_html}
                '''
                cards.append({
                    'content': card_content,
                })
            
            cards_html = self.create_card_group(cards=cards, cols=2, card_style='glass')
            tabs.append({
                'label': attention,
                'content': cards_html
            })
        
        # 使用Tab组件
        tab_content = self.create_tab_pane(tabs=tabs, tab_id="focus-topics", style="underline")
        self.add_section("重点关注题材", tab_content, "👁️")
    
    def add_second_half_strategy(self, strategy: str):
        """添加下半周操作策略"""
        content = f'''
            <div class="bg-gradient-to-r from-purple-500/20 to-pink-500/20 border border-purple-500/30 rounded-xl p-5">
                <div class="flex items-center gap-2 mb-3">
                    <span class="text-2xl">🎯</span>
                    <span class="text-white font-bold">下半周操作策略</span>
                </div>
                <div class="text-white/80 leading-relaxed">
                    {strategy}
                </div>
            </div>
        '''
        self.add_section("下半周操作策略", content, "🎯")
    
    def add_risk_warning(self, risks: list):
        """添加风险提示 - 使用卡片组"""
        cards = []
        if isinstance(risks, list):
            for i, risk in enumerate(risks):
                icons = ['⚠️', '📉', '🌍', '⚖️', '💹']
                icon = icons[i % len(icons)]
                cards.append({
                    'title': '',
                    'content': f'<p class="text-white/70 text-sm">{risk}</p>',
                    'icon': icon
                })
        else:
            cards.append({
                'content': f'<p class="text-white/70 text-sm">{risks}</p>',
                'icon': '⚠️'
            })
        
        cards_html = self.create_card_group(cards=cards, cols=3 if len(cards) >= 3 else len(cards), card_style='subtle')
        self.add_section("风险提示", cards_html, "⚠️")
    
    def add_strategy_points(self, points: list):
        """添加策略要点 - 使用卡片组"""
        cards = []
        for i, point in enumerate(points):
            icons = ['🎯', '📊', '🛡️', '💰', '⚡']
            icon = icons[i % len(icons)]
            cards.append({
                'title': point.get('title', ''),
                'content': f'<p class="text-white/70 text-sm">{point.get("content", "")}</p>',
                'icon': icon
            })
        
        cards_html = self.create_card_group(cards=cards, cols=3 if len(cards) >= 3 else len(cards), card_style='glass')
        self.add_section("操作要点", cards_html, "💡")
    
    def generate(self) -> str:
        """生成完整HTML"""
        return self.render()
    
    def save(self, filepath: str) -> str:
        """保存到文件"""
        html = self.render()
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
        return filepath


if __name__ == "__main__":
    # 测试生成
    gen = WeeklyOutlookProGenerator()
    gen.add_midweek_summary("本周市场整体呈现震荡格局，量能有所萎缩，资金观望情绪浓厚。")
    gen.add_market_status([
        {'name': '上证指数', 'value': '3,150.25', 'change': '+0.35%', 'up': True},
        {'name': '深证成指', 'value': '10,234.56', 'change': '-0.12%', 'up': False},
        {'name': '创业板指', 'value': '2,100.89', 'change': '+0.58%', 'up': True},
        {'name': '科创50', 'value': '950.34', 'change': '+1.23%', 'up': True},
    ])
    gen.add_focus_topics([
        {'name': 'AI算力', 'logic': '算力需求持续爆发，相关公司业绩超预期', 'attention': '重点关注', 'stocks': ['寒武纪', '海光信息', '中科曙光']},
        {'name': '人形机器人', 'logic': '特斯拉Optimus进展超预期，产业链受益', 'attention': '重点关注', 'stocks': ['拓普集团', '三花智控', '绿的谐波']},
        {'name': '存储芯片', 'logic': '行业周期反转，价格持续上涨', 'attention': '持续跟踪', 'stocks': ['兆易创新', '北京君正']},
        {'name': '先进封装', 'logic': 'Chiplet技术加速渗透', 'attention': '持续跟踪', 'stocks': ['长电科技', '通富微电']},
    ])
    gen.add_strategy_points([
        {'title': '仓位管理', 'content': '保持中性仓位，建议控制在50%-60%'},
        {'title': '板块配置', 'content': '科技为主，消费为辅，均衡配置'},
        {'title': '操作节奏', 'content': '低吸为主，避免追高，快进快出'},
    ])
    gen.add_second_half_strategy("下半周建议谨慎为主，控制仓位在5成左右。重点关注AI算力和新能源方向的结构性机会，避免追高。")
    gen.add_risk_warning(["外围市场波动风险", "国内经济数据不及预期", "题材轮动加快"])
    
    result = gen.save(f'../../docs/weekly_outlook/{datetime.now().strftime("%Y%m%d")}_周三前瞻.html')
    print(f"生成成功：{result}")
