"""
盘中快报生成器 - Pro版
基于ReportProGenerator基类重构，深色玻璃态风格
午间市场数据 + 热点解析 + 操作策略
"""
import sys
import os
import json
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from generators.report_pro_base import ReportProGenerator
from utils.data_loader import get_indices_for_daily, load_portfolio, get_hot_sectors


class IntradayProGenerator(ReportProGenerator):
    """盘中快报生成器 - Pro版"""
    
    def __init__(self, date_str: str = None, subtitle: str = None, data_dir: str = "data"):
        date = date_str or datetime.now().strftime('%Y-%m-%d')
        sub = subtitle or f"{date} · 午盘速递"
        
        super().__init__(
            title="盘中快报",
            report_type="intraday",
            subtitle=sub,
            date_str=date,
            data_dir=data_dir,
        )
        
        self.active_page = "盘中"
        self._load_data()
    
    def _load_data(self):
        """加载数据"""
        self.indices = get_indices_for_daily()
        self.portfolio = load_portfolio()
        self.hot_sectors = get_hot_sectors()
    
    def add_focus_point(self, focus: str):
        """添加午盘焦点"""
        content = f'''
        <div class="bg-gradient-to-r from-yellow-500/20 to-orange-500/15 border border-yellow-500/30 rounded-xl p-5">
            <div class="flex items-center gap-2 mb-3">
                <span class="text-2xl">⚡</span>
                <span class="text-white font-bold">午盘焦点</span>
            </div>
            <p class="text-white/80 leading-relaxed text-sm">
                {focus}
            </p>
        </div>
        '''
        self.add_section("午盘焦点", content, "⚡")
    
    def add_market_overview(self):
        """添加市场概览 - Pro版"""
        # 计算市场状态
        up_count = sum(1 for idx in self.indices if idx.get('up', True))
        total = len(self.indices)
        
        if up_count == total:
            market_status = "上涨"
            status_color = "text-green-400"
            status_bg = "from-green-500/20 to-emerald-500/10"
        elif up_count == 0:
            market_status = "下跌"
            status_color = "text-red-400"
            status_bg = "from-red-500/20 to-orange-500/10"
        else:
            market_status = "震荡分化"
            status_color = "text-yellow-400"
            status_bg = "from-yellow-500/20 to-orange-500/10"
        
        # 指数卡片
        cards_html = ''
        for idx in self.indices:
            name = idx.get('name', '')
            value = idx.get('price', idx.get('value', '--'))
            change = idx.get('change_pct_str', idx.get('change', ''))
            up = idx.get('up', True)
            
            if up:
                gradient = 'from-green-500/20 to-emerald-500/10 border-green-500/30'
                text_color = 'text-green-400'
            else:
                gradient = 'from-red-500/20 to-orange-500/10 border-red-500/30'
                text_color = 'text-red-400'
            
            cards_html += f'''
            <div class="bg-gradient-to-br {gradient} border rounded-xl p-4 text-center">
                <div class="text-sm text-white/60 mb-1">{name}</div>
                <div class="text-xl font-bold text-white mb-1">{value}</div>
                <div class="text-sm {text_color} font-semibold">{change}</div>
            </div>
            '''
        
        content = f'''
        <div class="grid grid-cols-2 md:grid-cols-4 gap-3 mb-4">
            {cards_html}
        </div>
        <div class="text-center">
            <span class="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-white/10 {status_color} text-sm font-medium">
                <span>📊</span>
                市场状态：{market_status}
            </span>
        </div>
        '''
        
        self.add_section("市场概览", content, "📈")
    
    def add_hot_topics(self, topics: list = None):
        """添加市场热点解析"""
        if topics is None:
            # 从热门板块生成热点
            topics = []
            for sector in self.hot_sectors[:3]:
                topics.append({
                    'tag': sector.get('name', ''),
                    'title': sector.get('name', '') + '板块领涨',
                    'content': sector.get('reason', ''),
                    'hot': True,
                    'stocks': [sector.get('leader', '')] if sector.get('leader') else []
                })
        
        if not topics:
            return
        
        topics_html = '<div class="space-y-3">'
        
        for topic in topics:
            is_hot = topic.get('hot', False)
            tag = topic.get('tag', '热点')
            stocks = topic.get('stocks', [])
            
            hot_badge = ''
            if is_hot:
                hot_badge = '<span class="bg-gradient-to-r from-red-500 to-orange-500 text-white text-xs font-bold px-2 py-0.5 rounded-full">🔥 热门</span>'
            
            stocks_html = ''
            if stocks:
                stock_tags = ' '.join([
                    f'<span class="bg-blue-500/20 text-blue-400 text-xs px-2 py-1 rounded-md border border-blue-500/30">{s}</span>'
                    for s in stocks
                ])
                stocks_html = f'''
                <div class="mt-3 pt-3 border-t border-white/10">
                    <div class="text-xs text-white/50 mb-2">相关标的</div>
                    <div class="flex flex-wrap gap-2">
                        {stock_tags}
                    </div>
                </div>
                '''
            
            topics_html += f'''
            <div class="bg-white/5 backdrop-blur-sm rounded-xl p-4 border border-white/10">
                <div class="flex items-center gap-3 mb-3">
                    <div class="w-9 h-9 bg-gradient-to-br from-blue-500 to-purple-500 rounded-lg flex items-center justify-center flex-shrink-0">
                        <span class="text-white text-sm">📌</span>
                    </div>
                    <div class="flex-1">
                        <div class="flex items-center gap-2">
                            <span class="text-xs font-semibold text-blue-400 bg-blue-500/20 px-2 py-0.5 rounded">{tag}</span>
                            <span class="text-white font-semibold text-sm">{topic.get("title", "")}</span>
                        </div>
                    </div>
                    {hot_badge}
                </div>
                <div class="text-sm text-white/70 leading-relaxed pl-12">
                    {topic.get("content", "")}
                </div>
                {stocks_html}
            </div>
            '''
        
        topics_html += '</div>'
        
        self.add_section("市场热点解析", topics_html, "🔥")
    
    def add_decline_sectors(self, sectors: list = None):
        """添加领跌板块警示"""
        if sectors is None:
            sectors = [
                {'name': '新能源', 'change': '-1.5%', 'reason': '板块轮动调整，短期资金流出'},
                {'name': '医药生物', 'change': '-0.8%', 'reason': '集采预期影响，观望情绪浓厚'},
            ]
        
        if not sectors:
            return
        
        sectors_html = '<div class="space-y-2">'
        
        for sector in sectors:
            sectors_html += f'''
            <div class="bg-gradient-to-r from-red-500/15 to-orange-500/10 border border-red-500/20 rounded-xl p-4">
                <div class="flex items-center justify-between mb-1">
                    <span class="text-red-400 font-semibold text-sm">{sector["name"]}</span>
                    <span class="text-red-400 font-bold text-sm">{sector.get("change", "")}</span>
                </div>
                <div class="text-xs text-red-300/70">
                    💡 {sector.get("reason", "")}
                </div>
            </div>
            '''
        
        sectors_html += '</div>'
        
        self.add_section("领跌板块警示", sectors_html, "⚠️")
    
    def add_holdings_tracking(self):
        """添加持仓股跟踪 - Pro版"""
        stocks = self.portfolio.get('stocks', [])
        
        if not stocks:
            return
        
        holdings_html = '<div class="space-y-3">'
        
        for stock in stocks:
            name = stock.get('name', '')
            code = stock.get('code', stock.get('id', ''))
            price = f"{stock.get('current_price', 0):.2f}"
            today_change = stock.get('today_change', 0) * 100
            up = today_change >= 0
            comment = stock.get('comment', stock.get('advice', ''))
            
            change_color = 'text-green-400' if up else 'text-red-400'
            change_sign = '+' if up else ''
            
            holdings_html += f'''
            <div class="bg-white/5 rounded-xl p-4 border border-white/10">
                <div class="flex items-center">
                    <div class="flex-1">
                        <div class="flex items-center gap-2 mb-1">
                            <span class="text-white font-semibold">{name}</span>
                            <span class="text-xs text-white/40">{code}</span>
                        </div>
                        <div class="text-xs text-white/50 leading-relaxed">
                            {comment}
                        </div>
                    </div>
                    <div class="text-right">
                        <div class="text-lg font-bold {change_color}">{price}</div>
                        <div class="text-xs {change_color} font-medium">{change_sign}{today_change:.2f}%</div>
                    </div>
                </div>
            </div>
            '''
        
        holdings_html += '</div>'
        
        self.add_section("持仓股跟踪", holdings_html, "💼")
    
    def add_trading_strategy(self, strategy: str = None):
        """添加午盘操作策略"""
        if strategy is None:
            strategy = """
            上午市场整体呈现震荡格局，板块轮动明显。操作上建议：
            1. 对于持仓标的，保持耐心，不盲目追涨杀跌
            2. 关注量能变化，若放量突破可适当加仓
            3. 高位股注意风险，避免追高
            4. 重点关注午后能否形成明确的方向选择
            """
        
        content = f'''
        <div class="bg-gradient-to-br from-purple-500/15 to-blue-500/10 border border-purple-500/20 rounded-xl p-5">
            <div class="flex items-center gap-2 mb-3">
                <span class="text-xl">📝</span>
                <span class="text-white font-bold">操作策略</span>
            </div>
            <div class="text-sm text-white/70 leading-relaxed space-y-2">
                {strategy.strip().replace(chr(10), '<br>')}
            </div>
        </div>
        '''
        
        self.add_section("午盘操作策略", content, "📝")
    
    def build_standard_report(self):
        """构建标准版本的盘中快报"""
        # 生成默认焦点
        hot = self.hot_sectors
        focus_text = '上午市场震荡运行，'
        if hot:
            focus_text += f"{hot[0].get('name', '')}等板块表现活跃，"
        focus_text += '关注午后量能变化和方向选择。'
        
        self.add_focus_point(focus_text)
        self.add_market_overview()
        self.add_hot_topics()
        self.add_holdings_tracking()
        self.add_trading_strategy()
        
        return self


if __name__ == '__main__':
    # 测试生成
    gen = IntradayProGenerator('2026-06-15', '周一午盘')
    gen.build_standard_report()
    html = gen.render()
    print(f'Pro版盘中快报生成成功，长度: {len(html)} 字符')
    
    # 保存测试
    os.makedirs('../docs/intraday', exist_ok=True)
    with open('../docs/intraday/20260615_盘中快报.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print('已保存到 docs/intraday/20260615_盘中快报.html')
