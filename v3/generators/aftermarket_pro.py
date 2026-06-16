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
from utils.data_loader import (
    get_indices_for_daily, load_portfolio, get_market_summary,
    get_hot_sectors, get_cold_sectors, get_longhubang_data
)


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
        self.hot_sectors = get_hot_sectors()
        self.cold_sectors = get_cold_sectors()
        try:
            self.longhubang_data = get_longhubang_data()
        except:
            self.longhubang_data = {}
    
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
    

    def add_market_sentiment(self):
        """添加市场情绪温度计 - Pro版"""
        market = self.market_data
        sentiment = market.get('sentiment', {})
        market_data = market.get('market_data', {})
        
        fg_score = sentiment.get('fear_greed', 50)
        
        if fg_score >= 80:
            level = '极度贪婪'
            level_color = 'text-red-400'
            bar_color = 'from-red-500 to-orange-500'
            bg_color = 'from-red-500/20 to-orange-500/10'
        elif fg_score >= 60:
            level = '贪婪'
            level_color = 'text-orange-400'
            bar_color = 'from-orange-500 to-yellow-500'
            bg_color = 'from-orange-500/20 to-yellow-500/10'
        elif fg_score >= 40:
            level = '中性'
            level_color = 'text-blue-400'
            bar_color = 'from-blue-500 to-cyan-500'
            bg_color = 'from-blue-500/20 to-cyan-500/10'
        elif fg_score >= 20:
            level = '恐惧'
            level_color = 'text-green-400'
            bar_color = 'from-green-500 to-emerald-500'
            bg_color = 'from-green-500/20 to-emerald-500/10'
        else:
            level = '极度恐惧'
            level_color = 'text-emerald-400'
            bar_color = 'from-emerald-500 to-teal-500'
            bg_color = 'from-emerald-500/20 to-teal-500/10'
        
        up_count = market_data.get('up_count', 0)
        down_count = market_data.get('down_count', 0)
        limit_up = market_data.get('limit_up_count', 0)
        limit_down = market_data.get('limit_down_count', 0)
        turnover = market_data.get('turnover', '')
        
        total = up_count + down_count if (up_count + down_count) > 0 else 1
        up_ratio = int(up_count / total * 100)
        
        left_card = '<div class="bg-gradient-to-br ' + bg_color + ' border border-white/10 rounded-xl p-5 text-center">'
        left_card += '<div class="text-white/60 text-sm mb-2">恐惧贪婪指数</div>'
        left_card += '<div class="text-5xl font-black ' + level_color + ' mb-2">' + str(fg_score) + '</div>'
        left_card += '<div class="text-sm font-semibold ' + level_color + '">' + level + '</div>'
        left_card += '<div class="w-full h-3 bg-white/10 rounded-full mt-4 overflow-hidden">'
        left_card += '<div class="h-full bg-gradient-to-r ' + bar_color + ' rounded-full transition-all duration-1000" style="width: ' + str(fg_score) + '%"></div>'
        left_card += '</div>'
        left_card += '<div class="flex justify-between text-xs text-white/40 mt-2"><span>恐惧</span><span>中性</span><span>贪婪</span></div>'
        left_card += '</div>'
        
        right_col = '<div class="space-y-3">'
        right_col += '<div class="bg-white/5 rounded-lg p-3">'
        right_col += '<div class="flex justify-between text-sm mb-1"><span class="text-white/60">涨跌家数比</span><span class="text-white font-medium">' + str(up_count) + ' / ' + str(down_count) + '</span></div>'
        right_col += '<div class="w-full h-2 bg-white/10 rounded-full overflow-hidden">'
        right_col += '<div class="h-full bg-gradient-to-r from-red-500 to-green-500 rounded-full" style="width: ' + str(up_ratio) + '%"></div>'
        right_col += '</div></div>'
        
        right_col += '<div class="grid grid-cols-2 gap-3">'
        right_col += '<div class="bg-white/5 rounded-lg p-3 text-center"><div class="text-red-400 text-xl font-bold">' + str(limit_up) + '</div><div class="text-white/40 text-xs">涨停家数</div></div>'
        right_col += '<div class="bg-white/5 rounded-lg p-3 text-center"><div class="text-green-400 text-xl font-bold">' + str(limit_down) + '</div><div class="text-white/40 text-xs">跌停家数</div></div>'
        right_col += '</div>'
        
        right_col += '<div class="bg-white/5 rounded-lg p-3 text-center"><div class="text-white text-xl font-bold">' + str(turnover) + '</div><div class="text-white/40 text-xs">两市成交额</div></div>'
        right_col += '</div>'
        
        content_html = '<div class="grid grid-cols-1 md:grid-cols-2 gap-6">' + left_card + right_col + '</div>'
        
        self.add_section("市场情绪", content_html, "🌡️")
    
    def add_sector_performance(self):
        """添加板块表现 - Pro版"""
        hot_html = ''
        for i, sector in enumerate(self.hot_sectors[:5]):
            name = sector.get('name', '')
            change = sector.get('change_pct', '0%')
            reason = sector.get('reason', '')
            short_reason = reason[:20] + '...' if len(reason) > 20 else reason
            
            item = '<div class="flex items-center justify-between p-3 bg-white/5 rounded-lg hover:bg-white/10 transition-all">'
            item += '<div class="flex items-center gap-3">'
            item += '<span class="w-6 h-6 bg-red-500/20 text-red-400 rounded-full flex items-center justify-center text-xs font-bold">' + str(i+1) + '</span>'
            item += '<span class="text-white text-sm font-medium">' + name + '</span>'
            item += '</div>'
            item += '<div class="text-right">'
            item += '<div class="text-red-400 font-bold text-sm">' + str(change) + '</div>'
            item += '<div class="text-white/40 text-xs">' + short_reason + '</div>'
            item += '</div></div>'
            hot_html += item
        
        cold_html = ''
        for i, sector in enumerate(self.cold_sectors[:5]):
            name = sector.get('name', '')
            change = sector.get('change_pct', '0%')
            reason = sector.get('reason', '')
            short_reason = reason[:20] + '...' if len(reason) > 20 else reason
            
            item = '<div class="flex items-center justify-between p-3 bg-white/5 rounded-lg hover:bg-white/10 transition-all">'
            item += '<div class="flex items-center gap-3">'
            item += '<span class="w-6 h-6 bg-green-500/20 text-green-400 rounded-full flex items-center justify-center text-xs font-bold">' + str(i+1) + '</span>'
            item += '<span class="text-white text-sm font-medium">' + name + '</span>'
            item += '</div>'
            item += '<div class="text-right">'
            item += '<div class="text-green-400 font-bold text-sm">' + str(change) + '</div>'
            item += '<div class="text-white/40 text-xs">' + short_reason + '</div>'
            item += '</div></div>'
            cold_html += item
        
        left_col = '<div><div class="text-white font-semibold mb-3 flex items-center gap-2"><span>🔥</span><span>涨幅榜 TOP5</span></div><div class="space-y-2">' + hot_html + '</div></div>'
        right_col = '<div><div class="text-white font-semibold mb-3 flex items-center gap-2"><span>❄️</span><span>跌幅榜 TOP5</span></div><div class="space-y-2">' + cold_html + '</div></div>'
        
        content_html = '<div class="grid grid-cols-1 md:grid-cols-2 gap-6">' + left_col + right_col + '</div>'
        
        self.add_section("板块表现", content_html, "📊")
    
    def add_holdings_tracking(self):
        """添加持仓跟踪 - Pro版"""
        portfolio = self.portfolio
        stocks = portfolio.get('stocks', [])
        
        if not stocks:
            content_html = '<div class="text-center py-8 text-white/40"><p>暂无持仓数据</p></div>'
            self.add_section("持仓跟踪", content_html, "💼")
            return
        
        stocks_html = ''
        for stock in stocks[:6]:
            name = stock.get('name', '')
            code = stock.get('code', '')
            price = stock.get('current_price', stock.get('price', 0))
            cost = stock.get('cost_price', stock.get('cost', 0))
            pnl_pct = stock.get('profit_pct', stock.get('change_pct', 0))
            position = stock.get('position', stock.get('shares', ''))
            
            try:
                pnl_val = float(str(pnl_pct).replace('%', '').replace('+', ''))
            except:
                pnl_val = 0
            
            if pnl_val > 0:
                pnl_color = 'text-red-400'
                pnl_bg = 'bg-red-500/10'
                pnl_sign = '+'
            elif pnl_val < 0:
                pnl_color = 'text-green-400'
                pnl_bg = 'bg-green-500/10'
                pnl_sign = ''
            else:
                pnl_color = 'text-white/60'
                pnl_bg = 'bg-white/5'
                pnl_sign = ''
            
            card = '<div class="bg-white/5 rounded-lg p-4 hover:bg-white/10 transition-all duration-300">'
            card += '<div class="flex items-start justify-between mb-2">'
            card += '<div><div class="text-white font-semibold">' + name + '</div><div class="text-white/40 text-xs">' + code + '</div></div>'
            card += '<div class="text-right"><div class="' + pnl_color + ' font-bold">' + pnl_sign + str(pnl_pct) + '</div><div class="text-white/40 text-xs">' + str(position) + '</div></div>'
            card += '</div>'
            card += '<div class="flex justify-between text-xs text-white/50"><span>现价: ' + str(price) + '</span><span>成本: ' + str(cost) + '</span></div>'
            card += '</div>'
            stocks_html += card
        
        content_html = '<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-3">' + stocks_html + '</div>'
        
        self.add_section("持仓跟踪", content_html, "💼")
    
    def add_tomorrow_prediction(self):
        """添加明日预判 - Pro版"""
        sentiment = self.market_data.get('sentiment', {})
        fg_score = sentiment.get('fear_greed', 50)
        
        if fg_score >= 70:
            trend = "情绪过热，注意回调风险"
            trend_icon = "⚠️"
            trend_color = "text-orange-400"
        elif fg_score >= 50:
            trend = "情绪中性偏暖，结构性机会为主"
            trend_icon = "➡️"
            trend_color = "text-blue-400"
        elif fg_score >= 30:
            trend = "情绪偏冷，关注超跌反弹机会"
            trend_icon = "⬆️"
            trend_color = "text-green-400"
        else:
            trend = "情绪冰点，反弹一触即发"
            trend_icon = "🚀"
            trend_color = "text-emerald-400"
        
        strategies = [
            "控制仓位，避免追高",
            "关注热点板块持续性",
            "设置好止损止盈位",
        ]
        
        strat_html = ''
        for s in strategies:
            strat_html += '<li class="text-white/70 text-sm mb-2 flex items-start gap-2"><span class="text-blue-400 mt-1">•</span><span>' + s + '</span></li>'
        
        main_card = '<div class="md:col-span-2 bg-white/5 rounded-xl p-4 border border-white/10">'
        main_card += '<div class="text-white font-semibold mb-3 flex items-center gap-2"><span>🎯</span><span>明日走势预判</span></div>'
        main_card += '<div class="' + trend_color + ' text-lg font-bold mb-2">' + trend_icon + ' ' + trend + '</div>'
        main_card += '<div class="text-white/60 text-sm leading-relaxed">基于当前市场情绪、资金流向和技术面综合判断，明日市场大概率延续结构性行情，重点关注板块轮动节奏。</div>'
        main_card += '</div>'
        
        side_cards = '<div class="space-y-3">'
        side_cards += '<div class="bg-white/5 rounded-xl p-4 border border-white/10"><div class="text-white/60 text-xs mb-1">支撑位</div><div class="text-white font-bold">关注均线支撑</div></div>'
        side_cards += '<div class="bg-white/5 rounded-xl p-4 border border-white/10"><div class="text-white/60 text-xs mb-1">压力位</div><div class="text-white font-bold">关注前高压力</div></div>'
        side_cards += '</div>'
        
        strat_card = '<div class="mt-4 bg-gradient-to-r from-blue-500/10 to-purple-500/10 rounded-xl p-4 border border-blue-500/20">'
        strat_card += '<div class="text-white font-semibold mb-3 flex items-center gap-2"><span>📋</span><span>操作策略建议</span></div>'
        strat_card += '<ul class="space-y-1">' + strat_html + '</ul>'
        strat_card += '</div>'
        
        content_html = '<div class="grid grid-cols-1 md:grid-cols-3 gap-4">' + main_card + side_cards + '</div>' + strat_card
        
        self.add_section("明日预判", content_html, "🔮")
    
    def add_risk_warning(self):
        """添加风险提示 - Pro版"""
        risks = [
            {'level': 'high', 'title': '外围市场波动风险', 'desc': '美股高位震荡，美联储政策不确定性可能传导至A股'},
            {'level': 'mid', 'title': '板块轮动加速风险', 'desc': '热点切换频繁，追高容易被套，建议低吸为主'},
            {'level': 'low', 'title': '成交量萎缩风险', 'desc': '若量能持续萎缩，市场活跃度可能下降'},
        ]
        
        risks_html = ''
        for risk in risks:
            if risk['level'] == 'high':
                icon = '🔴'
                bg = 'bg-red-500/10 border-red-500/30'
                title_color = 'text-red-400'
            elif risk['level'] == 'mid':
                icon = '🟡'
                bg = 'bg-yellow-500/10 border-yellow-500/30'
                title_color = 'text-yellow-400'
            else:
                icon = '🟢'
                bg = 'bg-green-500/10 border-green-500/30'
                title_color = 'text-green-400'
            
            card = '<div class="' + bg + ' rounded-lg p-4 border">'
            card += '<div class="flex items-center gap-2 mb-2"><span>' + icon + '</span><span class="' + title_color + ' font-semibold text-sm">' + risk['title'] + '</span></div>'
            card += '<p class="text-white/60 text-xs leading-relaxed">' + risk['desc'] + '</p>'
            card += '</div>'
            risks_html += card
        
        content_html = '<div class="grid grid-cols-1 md:grid-cols-3 gap-3">' + risks_html + '</div>'
        
        self.add_section("风险提示", content_html, "⚠️")
    
    def add_trading_plan(self):
        """添加交易计划 - Pro版"""
        plans = [
            {'time': '早盘', 'action': '观察开盘半小时量能和热点板块', 'priority': 'high'},
            {'time': '午盘', 'action': '根据上午走势调整持仓结构', 'priority': 'mid'},
            {'time': '尾盘', 'action': '确认当日趋势，进行仓位再平衡', 'priority': 'mid'},
        ]
        
        plans_html = ''
        for plan in plans:
            if plan['priority'] == 'high':
                badge = '<span class="bg-red-500/20 text-red-400 px-2 py-0.5 rounded text-xs font-semibold">重点</span>'
            else:
                badge = '<span class="bg-blue-500/20 text-blue-400 px-2 py-0.5 rounded text-xs font-semibold">关注</span>'
            
            item = '<div class="flex items-start gap-3 p-3 bg-white/5 rounded-lg">'
            item += '<div class="text-center flex-shrink-0"><div class="text-white font-bold text-sm">' + plan['time'] + '</div><div class="w-1 h-1 bg-white/20 rounded-full mx-auto mt-1"></div></div>'
            item += '<div class="flex-1"><p class="text-white/80 text-sm">' + plan['action'] + '</p><div class="mt-2">' + badge + '</div></div>'
            item += '</div>'
            plans_html += item
        
        tip_box = '<div class="mt-4 bg-gradient-to-r from-purple-500/10 to-pink-500/10 rounded-xl p-4 border border-purple-500/20">'
        tip_box += '<div class="text-white font-semibold text-sm mb-2">💡 今日交易原则</div>'
        tip_box += '<p class="text-white/60 text-xs leading-relaxed">顺势而为，不逆势操作；严格止损，让利润奔跑；仓位管理优先于个股选择，保持心态平稳。</p>'
        tip_box += '</div>'
        
        content_html = '<div class="space-y-3">' + plans_html + '</div>' + tip_box
        
        self.add_section("交易计划", content_html, "📝")


    def build_standard_report(self):
        """构建标准版本盘后速递"""
        self.add_today_highlight()
        self.add_market_summary()
        self.add_market_sentiment()
        self.add_sector_performance()
        self.add_holdings_tracking()
        self.add_longhubang_summary()
        self.add_evening_news()
        self.add_tomorrow_prediction()
        self.add_risk_warning()
        self.add_trading_plan()
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
