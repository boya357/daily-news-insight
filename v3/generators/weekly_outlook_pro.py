"""
周三前瞻生成器 - Pro版
基于Pro组件库重构，深色玻璃态风格
周中展望 + 题材预判 + 操作策略
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
        """添加当前市场状态"""
        cards_html = ''
        for idx in indices:
            name = idx.get('name', '')
            value = idx.get('value', '--')
            change = idx.get('change', '')
            up = idx.get('up', True)
            
            color_class = 'text-green-400' if up else 'text-red-400'
            bg_class = 'from-green-500/20 to-green-600/10 border-green-500/30' if up else 'from-red-500/20 to-red-600/10 border-red-500/30'
            
            cards_html += f'''
            <div class="bg-gradient-to-br {bg_class} border rounded-xl p-4 text-center">
                <div class="text-sm text-white/60 mb-1">{name}</div>
                <div class="text-2xl font-bold text-white mb-1">{value}</div>
                <div class="text-sm {color_class} font-semibold">{change}</div>
            </div>
            '''
        
        content = f'''
            <div class="grid grid-cols-2 md:grid-cols-4 gap-3">
                {cards_html}
            </div>
        '''
        self.add_section("周中市场概览", content, "📊")
    
    def add_focus_topics(self, topics: list):
        """添加重点关注题材"""
        topics_html = ''
        for topic in topics:
            name = topic.get('name', '')
            logic = topic.get('logic', '')
            attention = topic.get('attention', '重点关注')
            stocks = topic.get('stocks', [])
            
            stocks_html = ''
            if stocks:
                stocks_html = '<div class="flex flex-wrap gap-2 mt-3">'
                for stock in stocks:
                    stocks_html += f'<span class="text-xs bg-white/10 text-white/70 px-2 py-1 rounded-md">{stock}</span>'
                stocks_html += '</div>'
            
            topics_html += f'''
            <div class="bg-white/5 border border-white/10 rounded-xl p-4 mb-3 last:mb-0">
                <div class="flex items-center justify-between mb-2">
                    <div class="flex items-center gap-2">
                        <span class="text-xl">👁️</span>
                        <span class="text-white font-semibold">{name}</span>
                    </div>
                    <span class="text-xs bg-yellow-500/20 text-yellow-400 px-2 py-1 rounded-full">
                        {attention}
                    </span>
                </div>
                <p class="text-white/60 text-sm leading-relaxed">
                    {logic}
                </p>
                {stocks_html}
            </div>
            '''
        
        content = f'<div class="space-y-3">{topics_html}</div>'
        self.add_section("重点关注题材", content, "👁️")
    
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
        """添加风险提示"""
        if isinstance(risks, list):
            risk_text = "；".join(risks)
        else:
            risk_text = risks
        
        content = f'''
            <div class="bg-gradient-to-r from-red-500/20 to-orange-500/20 border border-red-500/30 rounded-xl p-5">
                <div class="flex items-center gap-2 mb-3">
                    <span class="text-2xl">⚠️</span>
                    <span class="text-white font-bold">风险提示</span>
                </div>
                <p class="text-white/80 leading-relaxed">
                    {risk_text}
                </p>
            </div>
        '''
        self.add_section("风险提示", content, "⚠️")
    
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
        {'name': '人形机器人', 'logic': '特斯拉Optimus进展超预期，产业链受益', 'attention': '持续跟踪', 'stocks': ['拓普集团', '三花智控', '绿的谐波']},
    ])
    gen.add_second_half_strategy("下半周建议谨慎为主，控制仓位在5成左右。重点关注AI算力和新能源方向的结构性机会，避免追高。")
    gen.add_risk_warning(["外围市场波动风险", "国内经济数据不及预期", "题材轮动加快"])
    
    result = gen.save(f'../../docs/weekly_outlook/{datetime.now().strftime("%Y%m%d")}_周三前瞻.html')
    print(f"生成成功：{result}")
