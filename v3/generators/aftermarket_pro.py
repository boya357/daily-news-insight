"""
盘后速递生成器 - Pro版
基于ReportProGenerator基类重构，深色玻璃态风格
收盘数据总结 + 晚间公告 + 龙虎榜
"""
import sys
import os
import json
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from generators.report_pro_base import ReportProGenerator
from utils.data_loader import get_indices_for_daily, load_portfolio, get_market_summary


class AftermarketProGenerator(ReportProGenerator):
    """盘后速递生成器 - Pro版"""
    
    def __init__(self, date_str: str = None, subtitle: str = None, data_dir: str = "data"):
        date = date_str or datetime.now().strftime('%Y-%m-%d')
        sub = subtitle or f"{date} · 盘后速递"
        
        super().__init__(
            title="盘后速递",
            report_type="aftermarket",
            subtitle=sub,
            date_str=date,
            data_dir=data_dir,
        )
        
        self.active_page = "盘后"
        self._load_data()
    
    def _load_data(self):
        """加载数据"""
        self.indices = get_indices_for_daily()
        self.portfolio = load_portfolio()
        self.market_data = get_market_summary()
    
    def add_today_highlight(self, highlight: str = None):
        """添加今日核心亮点"""
        if highlight is None:
            # 基于市场数据生成
            market = self.market_data
            market_data = market.get('market_data', {})
            turnover = market_data.get('turnover', '')
            
            # 判断涨跌
            up_count = sum(1 for idx in self.indices if idx.get('up', True))
            if up_count >= 3:
                trend = "多数指数收涨"
            elif up_count <= 1:
                trend = "多数指数收跌"
            else:
                trend = "指数分化"
            
            highlight = f"今日A股{trend}，两市成交额{turnover}。市场结构性行情延续，板块轮动特征明显。"
        
        content = f'''
        <div class="bg-gradient-to-r from-blue-500/20 to-purple-500/15 border border-blue-500/30 rounded-xl p-5">
            <div class="flex items-center gap-2 mb-3">
                <span class="text-2xl">⭐</span>
                <span class="text-white font-bold">今日核心</span>
            </div>
            <p class="text-white/80 leading-relaxed text-sm">
                {highlight}
            </p>
        </div>
        '''
        self.add_section("今日核心亮点", content, "⭐")
    
    def add_market_summary(self):
        """添加市场收盘总结 - Pro版"""
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
        
        # 额外数据
        market_data = self.market_data.get('market_data', {})
        turnover = market_data.get('turnover', '—')
        up_count = market_data.get('up_count', 0)
        down_count = market_data.get('down_count', 0)
        limit_up = market_data.get('limit_up_count', 0)
        limit_down = market_data.get('limit_down_count', 0)
        
        extra_html = f'''
        <div class="grid grid-cols-2 md:grid-cols-4 gap-3 mt-4">
            <div class="bg-white/5 rounded-lg p-3 text-center">
                <div class="text-white/50 text-xs mb-1">成交额</div>
                <div class="text-white font-bold">{turnover}</div>
            </div>
            <div class="bg-white/5 rounded-lg p-3 text-center">
                <div class="text-white/50 text-xs mb-1">上涨/下跌</div>
                <div class="text-white font-bold">{up_count}/{down_count}</div>
            </div>
            <div class="bg-white/5 rounded-lg p-3 text-center">
                <div class="text-white/50 text-xs mb-1">涨停/跌停</div>
                <div class="text-white font-bold">{limit_up}/{limit_down}</div>
            </div>
            <div class="bg-white/5 rounded-lg p-3 text-center">
                <div class="text-white/50 text-xs mb-1">北向资金</div>
                <div class="text-white font-bold">--</div>
            </div>
        </div>
        '''
        
        content = f'''
        <div class="grid grid-cols-2 md:grid-cols-4 gap-3">
            {cards_html}
        </div>
        {extra_html}
        '''
        
        self.add_section("市场收盘总结", content, "📊")
    
    def add_evening_news(self, news_list: list = None):
        """添加晚间重要新闻"""
        if news_list is None:
            news_list = [
                {"title": "重要政策发布", "content": "相关部门发布新的监管政策，对市场产生深远影响。", "time": "20:00", "source": "财联社"},
                {"title": "行业动态", "content": "行业迎来重要发展机遇，多家上市公司积极布局新赛道。", "time": "19:30", "source": "上证报"},
                {"title": "公司公告", "content": "多家上市公司发布重要公告，涉及业绩预告和重大合同。", "time": "18:45", "source": "证券时报"},
            ]
        
        news_html = '<div class="space-y-3">'
        
        for i, news in enumerate(news_list):
            title = news.get("title", "")
            content = news.get("content", "")
            time = news.get("time", "")
            source = news.get("source", "")
            
            news_html += f'''
            <div class="bg-white/5 rounded-xl p-4 border border-white/10">
                <div class="flex items-start gap-3">
                    <div class="w-2 h-2 rounded-full bg-blue-400 mt-1.5 flex-shrink-0"></div>
                    <div class="flex-1">
                        <div class="text-white font-semibold text-sm mb-1">{title}</div>
                        <div class="text-white/60 text-xs leading-relaxed">{content}</div>
                        <div class="flex items-center gap-3 mt-2 text-xs text-white/40">
                            <span>⏰ {time}</span>
                            <span>📰 {source}</span>
                        </div>
                    </div>
                </div>
            </div>
            '''
        
        news_html += '</div>'
        
        self.add_section("晚间重要新闻", news_html, "📰")
    
    def add_longhubang_summary(self, data: dict = None):
        """添加龙虎榜摘要"""
        content = '''
        <div class="bg-gradient-to-br from-orange-500/15 to-red-500/10 border border-orange-500/20 rounded-xl p-5">
            <div class="flex items-center gap-2 mb-4">
                <span class="text-xl">🏆</span>
                <span class="text-white font-bold">龙虎榜概览</span>
            </div>
            <div class="grid grid-cols-2 gap-3 text-center">
                <div class="bg-white/5 rounded-lg p-3">
                <div class="text-2xl font-black text-green-400">--</div>
                <div class="text-xs text-white/50">机构净买入(亿)</div>
            </div>
            <div class="bg-white/5 rounded-lg p-3">
                <div class="text-2xl font-black text-red-400">--</div>
                <div class="text-xs text-white/50">机构净卖出(亿)</div>
            </div>
            <div class="bg-white/5 rounded-lg p-3">
                <div class="text-2xl font-black text-yellow-400">--</div>
                <div class="text-xs text-white/50">上榜个股数</div>
            </div>
            <div class="bg-white/5 rounded-lg p-3">
                <div class="text-2xl font-black text-blue-400">--</div>
                <div class="text-xs text-white/50">知名游资</div>
            </div>
            </div>
            <div class="mt-4 pt-4 border-t border-white/10 text-center">
                <span class="text-xs text-white/50">详细数据请查看「龙虎榜透视」工具</span>
            </div>
        </div>
        '''
        
        self.add_section("龙虎榜摘要", content, "🏆")
    
    def add_portfolio_summary(self):
        """添加持仓总结"""
        stocks = self.portfolio.get('stocks', [])
        
        if not stocks:
            return
        
        # 计算涨跌
        up_stocks = [s for s in stocks if s.get('today_change', 0) >= 0]
        down_stocks = [s for s in stocks if s.get('today_change', 0) < 0]
        
        stocks_html = '<div class="space-y-2">'
        
        for stock in stocks:
            name = stock.get('name', '')
            change = stock.get('today_change', 0) * 100
            up = change >= 0
            color = 'text-green-400' if up else 'text-red-400'
            sign = '+' if up else ''
            
            stocks_html += f'''
            <div class="flex items-center justify-between bg-white/5 rounded-lg px-4 py-3">
                <span class="text-white/80 text-sm">{name}</span>
                <span class="{color} font-semibold text-sm">{sign}{change:.2f}%</span>
            </div>
            '''
        
        stocks_html += '</div>'
        
        content = f'''
        <div class="flex items-center justify-between mb-3">
            <div class="flex items-center gap-2">
                <span class="text-lg">💼</span>
                <span class="text-white font-semibold">持仓表现</span>
            </div>
            <div class="flex gap-2 text-xs">
                <span class="text-green-400">{len(up_stocks)}只上涨</span>
                <span class="text-white/30">|</span>
                <span class="text-red-400">{len(down_stocks)}只下跌</span>
            </div>
        </div>
        {stocks_html}
        '''
        
        self.add_section("持仓表现总结", content, "💼")
    
    def build_standard_report(self):
        """构建标准版本的盘后速递"""
        self.add_today_highlight()
        self.add_market_summary()
        self.add_evening_news()
        self.add_longhubang_summary()
        self.add_portfolio_summary()
        
        return self


if __name__ == '__main__':
    # 测试生成
    gen = AftermarketProGenerator('2026-06-15', '周一盘后')
    gen.build_standard_report()
    html = gen.render()
    print(f'Pro版盘后速递生成成功，长度: {len(html)} 字符')
    
    # 保存测试
    os.makedirs('../docs/aftermarket', exist_ok=True)
    with open('../docs/aftermarket/20260615_盘后速递.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print('已保存到 docs/aftermarket/20260615_盘后速递.html')
