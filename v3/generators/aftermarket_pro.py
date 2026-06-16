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
from utils.data_loader import get_indices_for_daily, load_portfolio, load_market_data, get_hot_sectors, get_cold_sectors


class AftermarketProGenerator(ReportProGenerator):
    """盘后速递生成器 - Pro版"""
    
    def __init__(self, date_str: str = None, subtitle: str = None, data_dir: str = "data"):
        date = date_str or datetime.now().strftime('%Y-%m-%d')
        sub = subtitle or f"{date} · 盘后速递"
        
        self.data_dir = data_dir

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
        self.market_data = load_market_data()
        self.hot_sectors = get_hot_sectors()
        self.cold_sectors = get_cold_sectors()
        
        # 题材数据
        try:
            data_path = os.path.join(self.data_dir, 'topics.json')
            with open(data_path, 'r', encoding='utf-8') as f:
                self.topics = json.load(f)
        except:
            self.topics = {}
        
        # 预判数据
        try:
            data_path = os.path.join(self.data_dir, 'predictions.json')
            with open(data_path, 'r', encoding='utf-8') as f:
                self.predictions = json.load(f)
        except:
            self.predictions = {}
    
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
    
    def add_sector_performance(self):
        """板块表现 - Pro版"""
        hot = self.hot_sectors
        cold = self.cold_sectors
        
        if not hot and not cold:
            return
        
        html = ''
        
        if hot:
            html += '<div class="mb-4"><div class="text-white font-semibold mb-3 flex items-center gap-2"><span>🔥</span><span>强势板块</span></div><div class="grid md:grid-cols-2 gap-3">'
            for sector in hot[:4]:
                name = sector.get('name', '')
                change = sector.get('change_pct', 0)
                reason = sector.get('reason', '')
                leader = sector.get('leader', '')
                change_str = f"+{change*100:.1f}%" if isinstance(change, (int, float)) else str(change)
                html += f'<div class="bg-red-500/10 border border-red-500/20 rounded-lg p-3"><div class="flex justify-between items-center mb-2"><span class="text-white font-medium text-sm">{name}</span><span class="text-red-400 font-bold text-sm">{change_str}</span></div><div class="text-xs text-white/60">领涨：{leader}</div></div>'
            html += '</div></div>'
        
        if cold:
            html += '<div><div class="text-white font-semibold mb-3 flex items-center gap-2"><span>🧊</span><span>弱势板块</span></div><div class="grid md:grid-cols-2 gap-3">'
            for sector in cold[:4]:
                name = sector.get('name', '')
                change = sector.get('change_pct', 0)
                change_str = f"{change*100:.1f}%" if isinstance(change, (int, float)) else str(change)
                html += f'<div class="bg-green-500/10 border border-green-500/20 rounded-lg p-3"><div class="flex justify-between items-center"><span class="text-white font-medium text-sm">{name}</span><span class="text-green-400 font-bold text-sm">{change_str}</span></div></div>'
            html += '</div></div>'
        
        self.add_section("板块表现", html, "📊")
    
    def add_market_sentiment(self):
        """市场情绪 - Pro版"""
        market = self.market_data
        sentiment = market.get('sentiment', {})
        market_data = market.get('market_data', {})
        
        fg_score = sentiment.get('fear_greed', 50)
        advance_decline = sentiment.get('advance_decline_ratio', 1.0)
        
        if fg_score >= 80:
            level = '极度贪婪'
            level_color = 'text-red-400'
            level_bg = 'from-red-500/30 to-orange-500/20'
        elif fg_score >= 60:
            level = '贪婪'
            level_color = 'text-orange-400'
            level_bg = 'from-orange-500/30 to-yellow-500/20'
        elif fg_score >= 40:
            level = '中性'
            level_color = 'text-blue-400'
            level_bg = 'from-blue-500/30 to-cyan-500/20'
        elif fg_score >= 20:
            level = '恐惧'
            level_color = 'text-green-400'
            level_bg = 'from-green-500/30 to-emerald-500/20'
        else:
            level = '极度恐惧'
            level_color = 'text-emerald-400'
            level_bg = 'from-emerald-500/30 to-teal-500/20'
        
        indicators = [
            ('涨跌家数比', f'{advance_decline:.2f}', '📈'),
            ('涨停数量', f"{market_data.get('limit_up_count', 0)}家", '🔥'),
            ('跌停数量', f"{market_data.get('limit_down_count', 0)}家", '❄️'),
            ('市场情绪', level, '💡'),
        ]
        
        ind_html = ''
        for label, value, icon in indicators:
            ind_html += f'<div class="text-center bg-white/5 rounded-lg p-3"><div class="text-lg mb-1">{icon}</div><div class="text-lg font-bold text-white">{value}</div><div class="text-xs text-white/50 mt-1">{label}</div></div>'
        
        html = f'''
        <div class="bg-gradient-to-r {level_bg} border border-white/10 rounded-xl p-5 mb-4">
            <div class="text-center">
                <div class="text-4xl font-black {level_color} mb-1">{fg_score}</div>
                <div class="text-sm text-white/70">恐惧贪婪指数 · {level}</div>
                <div class="w-full h-2 bg-white/10 rounded-full overflow-hidden mt-3">
                    <div class="h-full bg-gradient-to-r from-green-500 via-yellow-500 to-red-500 rounded-full" style="width: {fg_score}%"></div>
                </div>
            </div>
        </div>
        <div class="grid grid-cols-2 md:grid-cols-4 gap-3">
            {ind_html}
        </div>
        '''
        
        self.add_section("市场情绪", html, "🌡️")
    
    def add_tomorrow_prediction(self):
        """明日预判 - Pro版"""
        predictions = []
        market = self.market_data
        sentiment = market.get('sentiment', {})
        fg = sentiment.get('fear_greed', 50)
        
        if fg > 60:
            trend_pred = '震荡上行概率较大'
            trend_conf = 65
            trend_reason = '市场情绪偏乐观，资金活跃度较高，需警惕高位分歧。'
        elif fg > 40:
            trend_pred = '区间震荡概率较大'
            trend_conf = 70
            trend_reason = '情绪中性，市场缺乏明确方向，预计维持区间震荡格局。'
        else:
            trend_pred = '震荡调整概率较大'
            trend_conf = 60
            trend_reason = '市场情绪偏谨慎，风险偏好下降，注意控制仓位。'
        
        predictions.append({
            'direction': '大盘',
            'name': trend_pred,
            'confidence': trend_conf,
            'reason': trend_reason,
            'icon': '📊'
        })
        
        s_topics = self.topics.get('s_level_topics', [])
        if s_topics:
            topic = s_topics[0]
            predictions.append({
                'direction': '题材',
                'name': f"{topic.get('name', '')}有望延续强势",
                'confidence': 75,
                'reason': f"{topic.get('name', '')}当前处于高景气周期，政策和资金双重驱动，持续性值得期待。",
                'icon': '⚡'
            })
        
        predictions.append({
            'direction': '风险',
            'name': '注意高位股回调风险',
            'confidence': 65,
            'reason': '近期涨幅较大的个股存在获利回吐压力，建议回避纯题材炒作的高位股。',
            'icon': '⚠️'
        })
        
        pred_html = '<div class="space-y-3">'
        for p in predictions:
            direction = p.get('direction', '')
            name = p.get('name', '')
            confidence = p.get('confidence', 60)
            reason = p.get('reason', '')
            icon = p.get('icon', '📊')
            
            if direction == '大盘':
                bg_color = 'from-blue-500/20 to-cyan-500/10 border-blue-500/30'
            elif direction == '题材':
                bg_color = 'from-yellow-500/20 to-orange-500/10 border-yellow-500/30'
            else:
                bg_color = 'from-red-500/20 to-pink-500/10 border-red-500/30'
            
            pred_html += f'<div class="bg-gradient-to-r {bg_color} border rounded-xl p-4"><div class="flex items-center justify-between mb-2"><div class="flex items-center gap-2"><span class="text-lg">{icon}</span><span class="text-white font-semibold">{name}</span></div><div class="text-right"><span class="text-xs text-white/50">置信度</span><span class="text-white font-bold ml-1">{confidence}%</span></div></div><p class="text-sm text-white/70 leading-relaxed m-0">{reason}</p></div>'
        
        pred_html += '</div>'
        self.add_section("明日预判", pred_html, "🎯")
    
    def add_risk_warning(self):
        """风险提示 - Pro版"""
        risks = [
            {'level': '中', 'title': '市场波动风险', 'desc': '近期市场波动加大，注意控制仓位，避免追高。'},
            {'level': '低', 'title': '流动性风险', 'desc': '若成交额持续萎缩，需警惕市场活跃度下降。'},
            {'level': '中', 'title': '板块轮动风险', 'desc': '热点切换频繁，持续性较差，避免盲目追涨杀跌。'},
        ]
        
        level_colors = {
            '高': ('bg-red-500/20', 'text-red-400', 'border-red-500/30'),
            '中': ('bg-yellow-500/20', 'text-yellow-400', 'border-yellow-500/30'),
            '低': ('bg-green-500/20', 'text-green-400', 'border-green-500/30'),
        }
        
        risks_html = '<div class="grid md:grid-cols-3 gap-3">'
        for r in risks:
            level = r.get('level', '中')
            bg, text, border = level_colors.get(level, level_colors['中'])
            risks_html += f'<div class="{bg} {border} border rounded-xl p-4"><div class="flex items-center gap-2 mb-2"><span class="text-lg">⚠️</span><span class="text-white font-semibold">{r["title"]}</span><span class="ml-auto text-xs font-bold {text} px-2 py-0.5 rounded-full bg-white/10">{level}风险</span></div><p class="text-sm text-white/60 m-0">{r["desc"]}</p></div>'
        risks_html += '</div>'
        self.add_section("风险提示", risks_html, "⚠️")
    
    def add_trading_plan(self):
        """交易计划 - Pro版"""
        plans = [
            {'type': '持仓策略', 'content': '整体仓位控制在5-7成，保留部分现金应对波动。', 'icon': '💼'},
            {'type': '关注方向', 'content': '重点关注AI算力、存储芯片、人形机器人等主线赛道的低吸机会。', 'icon': '🎯'},
            {'type': '操作建议', 'content': '避免追高，逢低布局业绩确定性强的优质标的。', 'icon': '📝'},
        ]
        
        plans_html = '<div class="space-y-3">'
        for p in plans:
            plans_html += f'<div class="bg-white/5 border border-white/10 rounded-xl p-4"><div class="flex items-center gap-2 mb-2"><span class="text-lg">{p["icon"]}</span><span class="text-white font-semibold">{p["type"]}</span></div><p class="text-sm text-white/70 leading-relaxed m-0">{p["content"]}</p></div>'
        plans_html += '</div>'
        self.add_section("交易计划", plans_html, "📋")
    
    def add_daily_summary(self):
        """每日总结 - Pro版"""
        market = self.market_data
        market_data = market.get('market_data', {})
        sentiment = market.get('sentiment', {})
        turnover = market_data.get('turnover', '')
        fg = sentiment.get('fear_greed', 50)
        
        hot = self.hot_sectors
        hot_names = '、'.join([s.get('name', '') for s in hot[:3]]) if hot else ''
        
        summary = f"今日市场整体呈现情绪{'偏强' if fg > 50 else '偏弱'}格局，两市成交额{turnover}。{hot_names}等板块表现强势，市场结构性机会依然存在。操作上建议聚焦业绩确定性强的优质标的，避免追高，保持合理仓位。"
        
        content = f'<div class="bg-gradient-to-r from-purple-500/15 to-blue-500/10 border border-purple-500/20 rounded-xl p-5"><div class="text-white font-bold mb-3 flex items-center gap-2"><span>📝</span><span>今日总结</span></div><div class="text-white/70 leading-relaxed text-sm">{summary}</div></div>'
        self.add_section("每日总结", content, "📝")


    def build_standard_report(self):
        """构建标准版本的盘后速递"""
        self.add_today_highlight()
        self.add_market_summary()
        self.add_sector_performance()
        self.add_market_sentiment()
        self.add_longhubang_summary()
        self.add_evening_news()
        self.add_portfolio_summary()
        self.add_tomorrow_prediction()
        self.add_risk_warning()
        self.add_trading_plan()
        self.add_daily_summary()
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
