"""
每日新闻洞察生成器 - Pro版
基于ReportProGenerator基类重构，深色玻璃态风格
核心定位：早盘前的深度市场分析，为交易决策提供支撑
"""
import sys
import os
import json
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from components.pro import GlassCard, TagBadge
from generators.report_pro_base import ReportProGenerator
from utils.data_loader import (
    get_market_summary, get_hot_sectors, get_cold_sectors,
    get_indices_for_daily, load_portfolio
)


class DailyReportProGenerator(ReportProGenerator):
    """每日新闻洞察生成器 - Pro版"""
    
    def __init__(self, date_str: str = None, weekday: str = None, subtitle: str = None, data_dir: str = "data"):
        date = date_str or datetime.now().strftime('%Y-%m-%d')
        sub = subtitle or f"{date} {weekday or ''} · 龙空龙策略专用"
        
        super().__init__(
            title="每日新闻洞察",
            report_type="daily",
            subtitle=sub,
            date_str=date,
            data_dir=data_dir,
        )
        
        # 设置导航栏高亮
        self.active_page = "日报"
        
        # 加载数据
        self._load_data()
    
    def _load_data(self):
        """加载所有需要的数据"""
        # 市场数据
        self.market_data = get_market_summary()
        self.hot_sectors = get_hot_sectors()
        self.cold_sectors = get_cold_sectors()
        
        # 指数数据
        self.indices = get_indices_for_daily()
        
        # 题材数据
        try:
            data_path = os.path.join(self.data_dir, 'topics.json')
            with open(data_path, 'r', encoding='utf-8') as f:
                topics_data = json.load(f)
            self.topics = topics_data
        except:
            self.topics = {}
        
        # 持仓数据
        try:
            self.portfolio = load_portfolio()
        except:
            self.portfolio = {}
        
        # 预判数据
        try:
            data_path = os.path.join(self.data_dir, 'predictions.json')
            with open(data_path, 'r', encoding='utf-8') as f:
                pred_data = json.load(f)
            self.predictions = pred_data
        except:
            self.predictions = {}
    
    def _parse_change_pct(self, change_str):
        """解析涨跌幅字符串，返回浮点数"""
        if isinstance(change_str, (int, float)):
            return float(change_str)
        if isinstance(change_str, str):
            clean = change_str.replace('%', '').replace('+', '').strip()
            try:
                return float(clean) / 100
            except:
                return 0
        return 0
    
    def _assess_sustainability(self, sector):
        """评估板块持续性"""
        reason = sector.get('reason', '')
        change_pct = self._parse_change_pct(sector.get('change_pct', 0))
        
        score = 50
        
        keywords_high = ['周期反转', '需求爆发', '政策支持', '技术突破', '国产替代']
        keywords_mid = ['业绩超预期', '行业景气', '资金流入']
        
        for kw in keywords_high:
            if kw in reason:
                score += 15
        
        for kw in keywords_mid:
            if kw in reason:
                score += 10
        
        if change_pct > 0.05:
            score -= 10
        
        score = max(10, min(95, score))
        
        if score >= 80:
            level = '很强'
        elif score >= 60:
            level = '较强'
        elif score >= 40:
            level = '一般'
        else:
            level = '较弱'
        
        return {'score': score, 'level': level}
    
    def add_market_overview(self):
        """添加市场总览 - Pro版"""
        indices = self.indices
        market = self.market_data
        sentiment = market.get('sentiment', {})
        market_data = market.get('market_data', {})
        
        # 指数卡片
        index_cards_html = ''
        for idx in indices:
            name = idx.get('name', '')
            price = idx.get('price', 0)
            change_str = idx.get('change_pct_str', '')
            up = idx.get('up', True)
            
            if up:
                gradient_class = 'from-red-500/20 to-orange-500/10 border-red-500/30'
                text_color = 'text-red-400'
            else:
                gradient_class = 'from-green-500/20 to-emerald-500/10 border-green-500/30'
                text_color = 'text-green-400'
            
            index_cards_html += f'''
            <div class="bg-gradient-to-br {gradient_class} border rounded-xl p-4 text-center transition-all duration-300 hover:scale-105">
                <div class="text-sm text-white/60 mb-1">{name}</div>
                <div class="text-xl font-bold text-white mb-1">{price}</div>
                <div class="text-sm {text_color} font-semibold">{change_str}</div>
            </div>
            '''
        
        # 市场概览数据
        turnover = market_data.get('turnover', '—')
        up_count = market_data.get('up_count', 0)
        down_count = market_data.get('down_count', 0)
        limit_up = market_data.get('limit_up_count', 0)
        limit_down = market_data.get('limit_down_count', 0)
        
        # 情绪分数
        fg_score = sentiment.get('fear_greed', 50)
        if fg_score >= 80:
            fg_level = '极度贪婪'
            fg_color = 'text-red-400'
            fg_bg = 'from-red-500/20 to-orange-500/10'
        elif fg_score >= 60:
            fg_level = '贪婪'
            fg_color = 'text-orange-400'
            fg_bg = 'from-orange-500/20 to-yellow-500/10'
        elif fg_score >= 40:
            fg_level = '中性'
            fg_color = 'text-blue-400'
            fg_bg = 'from-blue-500/20 to-cyan-500/10'
        elif fg_score >= 20:
            fg_level = '恐惧'
            fg_color = 'text-green-400'
            fg_bg = 'from-green-500/20 to-emerald-500/10'
        else:
            fg_level = '极度恐惧'
            fg_color = 'text-emerald-400'
            fg_bg = 'from-emerald-500/20 to-teal-500/10'
        
        content = f'''
        <!-- 四大指数 -->
        <div class="grid grid-cols-2 md:grid-cols-4 gap-3 mb-6">
            {index_cards_html}
        </div>
        
        <!-- 分割线 -->
        <div class="h-px bg-white/10 my-5"></div>
        
        <!-- 市场数据 + 情绪 -->
        <div class="grid md:grid-cols-3 gap-4">
            <!-- 左侧：市场数据 -->
            <div class="md:col-span-2">
                <div class="text-white font-bold mb-4 flex items-center gap-2">
                    <span>📊</span>
                    <span>市场概况</span>
                </div>
                <div class="grid grid-cols-2 md:grid-cols-4 gap-3">
                    <div class="text-center p-3 bg-white/5 rounded-lg">
                        <div class="text-lg font-bold text-white">{turnover}</div>
                        <div class="text-xs text-white/50 mt-1">成交额</div>
                    </div>
                    <div class="text-center p-3 bg-red-500/10 rounded-lg">
                        <div class="text-lg font-bold text-red-400">{up_count}</div>
                        <div class="text-xs text-white/50 mt-1">上涨家数</div>
                    </div>
                    <div class="text-center p-3 bg-green-500/10 rounded-lg">
                        <div class="text-lg font-bold text-green-400">{down_count}</div>
                        <div class="text-xs text-white/50 mt-1">下跌家数</div>
                    </div>
                    <div class="text-center p-3 bg-yellow-500/10 rounded-lg">
                        <div class="text-lg font-bold text-yellow-400">{limit_up}/{limit_down}</div>
                        <div class="text-xs text-white/50 mt-1">涨停/跌停</div>
                    </div>
                </div>
            </div>
            
            <!-- 右侧：情绪温度计 -->
            <div class="bg-gradient-to-br {fg_bg} border border-white/10 rounded-xl p-4 text-center">
                <div class="text-sm text-white/60 mb-2">
                    🌡️ 市场情绪
                </div>
                <div class="text-3xl font-black {fg_color} leading-none">
                    {fg_score}
                </div>
                <div class="text-sm font-semibold {fg_color} mt-2">
                    {fg_level}
                </div>
                <div class="w-full h-2 bg-white/10 rounded-full overflow-hidden mt-3">
                    <div class="h-full bg-gradient-to-r from-green-500 via-yellow-500 to-red-500 rounded-full" style="width: {fg_score}%"></div>
                </div>
                <div class="flex justify-between text-xs text-white/40 mt-2">
                    <span>恐惧</span>
                    <span>中性</span>
                    <span>贪婪</span>
                </div>
            </div>
        </div>
        '''
        
        self.add_section("市场总览", content, "🌍")
    
    def add_sector_analysis(self):
        """添加热点板块深度分析 - Pro版"""
        hot = self.hot_sectors
        cold = self.cold_sectors
        
        if not hot and not cold:
            return
        
        html = ''
        
        # 热门板块
        if hot:
            html += '''
            <div class="mb-6">
                <div class="flex items-center gap-2 mb-4">
                    <span class="text-xl">🔥</span>
                    <span class="text-white font-bold">强势板块</span>
                </div>
                <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-3">
            '''
            
            for sector in hot:
                name = sector.get('name', '')
                change_pct = self._parse_change_pct(sector.get('change_pct', 0))
                change_str = f"+{change_pct*100:.1f}%" if change_pct > 0 else f"{change_pct*100:.1f}%"
                leader = sector.get('leader', '')
                reason = sector.get('reason', '')
                
                sustainability = self._assess_sustainability(sector)
                
                html += f'''
                <div class="bg-gradient-to-br from-red-500/15 to-orange-500/5 border border-red-500/20 rounded-xl p-4 transition-all duration-300 hover:scale-102">
                    <div class="flex justify-between items-start mb-3">
                        <div class="text-base font-bold text-red-400">{name}</div>
                        <div class="text-base font-bold text-red-400">{change_str}</div>
                    </div>
                    <div class="text-sm text-white/70 mb-3">
                        <strong class="text-white/90">领涨：</strong>{leader}
                    </div>
                    <div class="text-xs text-white/60 leading-relaxed mb-3">
                        {reason}
                    </div>
                    <div class="flex items-center gap-2">
                        <span class="text-xs text-white/50">持续性：</span>
                        <div class="flex-1 h-1.5 bg-red-500/20 rounded-full overflow-hidden">
                            <div class="h-full bg-red-500 rounded-full" style="width: {sustainability['score']}%"></div>
                        </div>
                        <span class="text-xs font-semibold text-red-400">{sustainability['level']}</span>
                    </div>
                </div>
                '''
            
            html += '</div></div>'
        
        # 弱势板块
        if cold:
            html += '''
            <div>
                <div class="flex items-center gap-2 mb-4">
                    <span class="text-xl">🧊</span>
                    <span class="text-white font-bold">弱势板块</span>
                </div>
                <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-3">
            '''
            
            for sector in cold:
                name = sector.get('name', '')
                change_pct = self._parse_change_pct(sector.get('change_pct', 0))
                change_str = f"{change_pct*100:.1f}%"
                reason = sector.get('reason', '')
                
                html += f'''
                <div class="bg-gradient-to-br from-green-500/15 to-emerald-500/5 border border-green-500/20 rounded-xl p-4">
                    <div class="flex justify-between items-start mb-2">
                        <div class="text-base font-bold text-green-400">{name}</div>
                        <div class="text-base font-bold text-green-400">{change_str}</div>
                    </div>
                    <div class="text-xs text-white/60 leading-relaxed">
                        {reason}
                    </div>
                </div>
                '''
            
            html += '</div></div>'
        
        self.add_section("板块深度分析", html, "🏢")
    
    def add_topic_deep_dive(self):
        """核心题材深度推演 - Pro版"""
        s_topics = self.topics.get('s_level_topics', [])
        if not s_topics:
            return
        
        topic = s_topics[0]
        name = topic.get('name', '')
        level = topic.get('level', 'S')
        core_logic = topic.get('core_logic', '')
        total_score = topic.get('total_score', 0)
        dim_scores = topic.get('dimension_scores', {})
        
        # 六维评分
        dim_labels = {
            'policy': ('政策', '📋'),
            'industry': ('产业', '🏭'),
            'capital': ('资金', '💰'),
            'sentiment': ('情绪', '🔥'),
            'valuation': ('估值', '📐'),
            'catalyst': ('催化', '⚡'),
        }
        
        dims_html = ''
        for key, (label, icon) in dim_labels.items():
            score = dim_scores.get(key, 0)
            if score >= 85:
                bar_color = 'bg-green-500'
            elif score >= 70:
                bar_color = 'bg-yellow-500'
            else:
                bar_color = 'bg-red-500'
            
            dims_html += f'''
            <div class="text-center bg-white/5 rounded-lg p-3">
                <div class="text-lg mb-1">{icon}</div>
                <div class="text-lg font-bold text-white">{score}</div>
                <div class="text-xs text-white/50 mt-1">{label}</div>
                <div class="w-full h-1 bg-white/10 rounded-full mt-2 overflow-hidden">
                    <div class="h-full {bar_color} rounded-full" style="width: {score}%"></div>
                </div>
            </div>
            '''
        
        # 催化剂事件
        catalysts_html = ''
        catalysts = topic.get('catalyst_events', [])
        if catalysts:
            cats = ''.join([f'<span class="bg-yellow-500/20 text-yellow-400 px-3 py-1 rounded-full text-xs border border-yellow-500/30">{cat}</span>' for cat in catalysts])
            catalysts_html = f'''
            <div class="mt-5">
                <div class="text-white/80 text-sm font-semibold mb-3">📅 核心催化事件</div>
                <div class="flex flex-wrap gap-2">
                    {cats}
                </div>
            </div>
            '''
        
        # 核心标的
        leader = topic.get('leader_stock', '')
        mid = topic.get('mid_cap_stock', '')
        flexible = topic.get('flexible_stock', '')
        
        stocks_html = ''
        if leader or mid or flexible:
            stock_items = ''
            if leader:
                stock_items += f'''
                <div class="bg-white/10 rounded-lg p-3 text-center border border-yellow-500/20">
                    <div class="text-xs text-white/50 mb-1">龙头</div>
                    <div class="text-sm font-semibold text-white">{leader}</div>
                </div>
                '''
            if mid:
                stock_items += f'''
                <div class="bg-white/10 rounded-lg p-3 text-center border border-yellow-500/20">
                    <div class="text-xs text-white/50 mb-1">中坚</div>
                    <div class="text-sm font-semibold text-white">{mid}</div>
                </div>
                '''
            if flexible:
                stock_items += f'''
                <div class="bg-white/10 rounded-lg p-3 text-center border border-yellow-500/20">
                    <div class="text-xs text-white/50 mb-1">弹性</div>
                    <div class="text-sm font-semibold text-white">{flexible}</div>
                </div>
                '''
            
            stocks_html = f'''
            <div class="mt-5">
                <div class="text-white/80 text-sm font-semibold mb-3">🎯 核心标的</div>
                <div class="grid grid-cols-3 gap-2">
                    {stock_items}
                </div>
            </div>
            '''
        
        html = f'''
        <div class="bg-gradient-to-br from-yellow-500/15 to-orange-500/5 border border-yellow-500/20 rounded-xl p-5">
            <!-- 标题区 -->
            <div class="flex items-start justify-between mb-5">
                <div class="flex-1">
                    <div class="flex items-center gap-2 mb-2">
                        <span class="text-2xl">⚡</span>
                        <span class="text-xl font-bold text-yellow-400">{name}</span>
                        <span class="bg-gradient-to-r from-red-500 to-orange-500 text-white px-2 py-0.5 rounded-full text-xs font-bold">{level}级题材</span>
                    </div>
                    <div class="text-sm text-white/70 leading-relaxed">
                        {core_logic}
                    </div>
                </div>
                <div class="text-center ml-4 flex-shrink-0">
                    <div class="text-3xl font-black bg-gradient-to-r from-yellow-400 to-orange-500 bg-clip-text text-transparent">
                        {total_score}
                    </div>
                    <div class="text-xs text-white/50">综合评分</div>
                </div>
            </div>
            
            <!-- 六维评分 -->
            <div class="grid grid-cols-3 md:grid-cols-6 gap-2 mb-2">
                {dims_html}
            </div>
            
            {catalysts_html}
            {stocks_html}
        </div>
        '''
        
        self.add_section("核心题材深度推演", html, "💡")
    
    def add_holdings_tracking(self):
        """持仓跟踪 - Pro版"""
        stocks = self.portfolio.get('stocks', [])
        
        if not stocks:
            return
        
        html = '<div class="space-y-3">'
        
        for stock in stocks:
            name = stock.get('name', '')
            code = stock.get('code', stock.get('id', ''))
            cost = stock.get('cost_price', 0)
            current = stock.get('current_price', 0)
            profit_pct = (current - cost) / cost * 100 if cost > 0 else 0
            today_change = stock.get('today_change', 0) * 100
            risk_level = stock.get('risk_level', '')
            risk_progress = stock.get('risk_progress', 0)
            advice = stock.get('advice', '')
            diagnosis = stock.get('diagnosis', {})
            
            profit_color = 'text-red-400' if profit_pct >= 0 else 'text-green-400'
            profit_sign = '+' if profit_pct >= 0 else ''
            today_color = 'text-red-400' if today_change >= 0 else 'text-green-400'
            today_sign = '+' if today_change >= 0 else ''
            
            # 风险条颜色
            if risk_progress < 50:
                risk_bar_color = 'bg-green-500'
            elif risk_progress < 75:
                risk_bar_color = 'bg-yellow-500'
            else:
                risk_bar_color = 'bg-red-500'
            
            # 诊断指标
            diag_items = []
            if isinstance(diagnosis, dict):
                for key, value in diagnosis.items():
                    if isinstance(value, dict):
                        status = value.get('status', 'normal')
                        status_colors = {
                            'good': 'text-green-400',
                            'normal': 'text-blue-400',
                            'bad': 'text-red-400',
                            'warning': 'text-yellow-400'
                        }
                        color = status_colors.get(status, 'text-white/60')
                        diag_items.append({
                            'label': value.get('title', key),
                            'value': value.get('value', ''),
                            'color': color
                        })
            
            # 默认诊断项
            if not diag_items:
                default_dims = [
                    ('技术面', '--', 'text-blue-400'),
                    ('资金面', '--', 'text-blue-400'),
                    ('基本面', '--', 'text-blue-400'),
                    ('消息面', '--', 'text-blue-400'),
                ]
                for label, value, color in default_dims:
                    diag_items.append({'label': label, 'value': value, 'color': color})
            
            diag_html = ''
            for item in diag_items[:4]:
                diag_html += f'''
                <div class="text-center flex-1">
                    <div class="text-sm font-semibold {item['color']}">{item['value']}</div>
                    <div class="text-xs text-white/50 mt-1">{item['label']}</div>
                </div>
                '''
            
            html += f'''
            <div class="bg-white/5 backdrop-blur-sm rounded-xl p-4 border border-white/10">
                <!-- 头部信息 -->
                <div class="flex justify-between items-start mb-3">
                    <div>
                        <div class="flex items-center gap-2 mb-1">
                            <span class="text-base font-bold text-white">{name}</span>
                            <span class="text-xs text-white/40">{code}</span>
                        </div>
                        <div class="flex gap-3 text-xs">
                            <span class="text-white/50">成本: <span class="text-white/80 font-medium">¥{cost:.2f}</span></span>
                            <span class="text-white/50">现价: <span class="text-white/80 font-medium">¥{current:.2f}</span></span>
                        </div>
                    </div>
                    <div class="text-right">
                        <div class="text-lg font-bold {profit_color}">
                            {profit_sign}{profit_pct:.1f}%
                        </div>
                        <div class="text-xs {today_color} mt-1">
                            今日 {today_sign}{today_change:.1f}%
                        </div>
                    </div>
                </div>
                
                <!-- 诊断指标 -->
                <div class="flex gap-2 mb-3 p-2 bg-white/5 rounded-lg">
                    {diag_html}
                </div>
                
                <!-- 风险进度 -->
                <div class="mb-2">
                    <div class="flex justify-between text-xs mb-1">
                        <span class="text-white/50">风险等级</span>
                        <span class="text-white/70">{risk_level or '中风险'}</span>
                    </div>
                    <div class="w-full h-1.5 bg-white/10 rounded-full overflow-hidden">
                        <div class="h-full {risk_bar_color} rounded-full transition-all" style="width: {risk_progress}%"></div>
                    </div>
                </div>
                
                <!-- 操作建议 -->
                {f'''
                <div class="mt-3 pt-3 border-t border-white/10">
                    <div class="text-xs text-white/50 mb-1">操作建议</div>
                    <div class="text-sm text-white/80">{advice or '持有观察'}</div>
                </div>
                ''' if advice else ''}
            </div>
            '''
        
        html += '</div>'
        
        self.add_section("持仓跟踪", html, "📈")
    
    def add_tomorrow_prediction(self):
        """明日关键预判 - Pro版"""
        predictions = []
        
        # 基于热门板块生成看涨预判
        hot = self.hot_sectors
        if hot:
            top_sector = hot[0]
            predictions.append({
                'direction': '看涨',
                'name': top_sector.get('name', ''),
                'confidence': 70,
                'reason': top_sector.get('reason', '行业景气度持续') + '，关注龙头持续性。'
            })
        
        # 大盘预判
        market = self.market_data
        sentiment = market.get('sentiment', {})
        fg = sentiment.get('fear_greed', 50)
        
        if fg > 60:
            market_pred = '震荡上行'
            market_conf = 55
            market_reason = '市场情绪偏乐观，资金活跃度较高，但需警惕高位分歧。'
        elif fg > 40:
            market_pred = '震荡整理'
            market_conf = 60
            market_reason = '情绪中性，市场缺乏明确方向，预计维持区间震荡。'
        else:
            market_pred = '震荡下行'
            market_conf = 55
            market_reason = '市场情绪偏谨慎，风险偏好下降，注意控制仓位。'
        
        predictions.insert(0, {
            'direction': '震荡',
            'name': '大盘指数',
            'confidence': market_conf,
            'reason': market_reason
        })
        
        # 风险提示
        predictions.append({
            'direction': '看跌',
            'name': '高位题材股',
            'confidence': 60,
            'reason': '近两日涨幅较大的题材股存在回调风险，注意高低切换。'
        })
        
        # 渲染
        direction_styles = {
            '看涨': {'bg': 'from-red-500/20 to-orange-500/10', 'border': 'border-red-500/30', 'text': 'text-red-400', 'icon': '📈'},
            '看跌': {'bg': 'from-green-500/20 to-emerald-500/10', 'border': 'border-green-500/30', 'text': 'text-green-400', 'icon': '📉'},
            '震荡': {'bg': 'from-blue-500/20 to-cyan-500/10', 'border': 'border-blue-500/30', 'text': 'text-blue-400', 'icon': '📊'},
        }
        
        pred_html = '<div class="space-y-3">'
        for p in predictions:
            direction = p.get('direction', '震荡')
            style = direction_styles.get(direction, direction_styles['震荡'])
            name = p.get('name', '')
            confidence = p.get('confidence', 60)
            reason = p.get('reason', '')
            
            if confidence >= 75:
                conf_color = 'text-green-400'
            elif confidence >= 60:
                conf_color = 'text-yellow-400'
            else:
                conf_color = 'text-white/50'
            
            pred_html += f'''
            <div class="bg-gradient-to-r {style['bg']} {style['border']} border rounded-xl p-4">
                <div class="flex items-center justify-between mb-2">
                    <div class="flex items-center gap-2">
                        <span class="text-lg">{style['icon']}</span>
                        <span class="text-white font-semibold">{name}</span>
                    </div>
                    <div class="text-right">
                        <span class="bg-white/10 text-white text-xs font-bold px-2.5 py-1 rounded-full">
                            {direction}
                        </span>
                        <div class="text-xs {conf_color} mt-1 font-medium">
                            置信度 {confidence}%
                        </div>
                    </div>
                </div>
                <p class="text-sm text-white/70 leading-relaxed m-0">
                    {reason}
                </p>
            </div>
            '''
        
        pred_html += '</div>'
        
        # 免责声明
        pred_html += '''
        <div class="mt-4 text-center text-xs text-white/40 leading-relaxed">
            ⚠️ 预判仅供参考，不构成投资建议。市场有风险，投资需谨慎。
            <br>预判基于当前市场数据和逻辑推演，实际走势受多种因素影响。
        </div>
        '''
        
        self.add_section("明日关键预判", pred_html, "🎯")
    
    def add_risk_warning(self):
        """风险提示 - Pro版"""
        # 基于市场数据生成风险提示
        market = self.market_data
        market_data = market.get('market_data', {})
        sentiment = market.get('sentiment', {})
        fg = sentiment.get('fear_greed', 50)
        
        risks = []
        
        if fg > 70:
            risks.append({
                'level': '高',
                'title': '情绪过热风险',
                'desc': '市场贪婪指数偏高，短期可能出现情绪退潮导致的回调。'
            })
        elif fg > 60:
            risks.append({
                'level': '中',
                'title': '情绪分化风险',
                'desc': '市场情绪偏乐观，但板块轮动加快，注意追高风险。'
            })
        
        risks.append({
            'level': '中',
            'title': '板块轮动风险',
            'desc': '近期热点切换频繁，持续性较差，避免盲目追涨杀跌。'
        })
        
        risks.append({
            'level': '低',
            'title': '流动性风险',
            'desc': '关注成交额变化，若持续萎缩需警惕市场活跃度下降。'
        })
        
        level_colors = {
            '高': ('bg-red-500/20', 'text-red-400', 'border-red-500/30'),
            '中': ('bg-yellow-500/20', 'text-yellow-400', 'border-yellow-500/30'),
            '低': ('bg-green-500/20', 'text-green-400', 'border-green-500/30'),
        }
        
        risks_html = '<div class="grid md:grid-cols-2 gap-3">'
        for r in risks:
            level = r.get('level', '中')
            bg, text, border = level_colors.get(level, level_colors['中'])
            risks_html += f'''
            <div class="{bg} {border} border rounded-xl p-4">
                <div class="flex items-center gap-2 mb-2">
                    <span class="text-lg">⚠️</span>
                    <span class="text-white font-semibold">{r['title']}</span>
                    <span class="ml-auto text-xs font-bold {text} px-2 py-0.5 rounded-full bg-white/10">{level}风险</span>
                </div>
                <p class="text-sm text-white/60 m-0">{r['desc']}</p>
            </div>
            '''
        risks_html += '</div>'
        
        self.add_section("风险提示", risks_html, "⚠️")
    
    def add_daily_summary(self):
        """每日总结 - Pro版"""
        market = self.market_data
        market_data = market.get('market_data', {})
        sentiment = market.get('sentiment', {})
        
        turnover = market_data.get('turnover', '')
        fg = sentiment.get('fear_greed', 50)
        
        hot = self.hot_sectors
        hot_names = '、'.join([s.get('name', '') for s in hot[:3]]) if hot else ''
        
        summary = f"""
        今日市场整体呈现情绪{"偏强" if fg > 50 else "偏弱"}格局，成交额{turnover}，市场活跃度{"较高" if fg > 60 else "一般"}。
        板块方面，{hot_names}等板块表现强势，市场结构性机会依然存在。
        操作上，建议聚焦业绩确定性强的优质标的，避免追高，保持合理仓位。
        """
        
        content = f'''
        <div class="bg-gradient-to-r from-purple-500/15 to-blue-500/10 border border-purple-500/20 rounded-xl p-5">
            <div class="text-white font-bold mb-3 flex items-center gap-2">
                <span>📝</span>
                <span>今日总结</span>
            </div>
            <div class="text-white/70 leading-relaxed text-sm">
                {summary.strip()}
            </div>
        </div>
        '''
        
        self.add_section("每日总结", content, "📝")
    
    def build_standard_report(self):
        """构建标准版本的日报"""
        self.add_market_overview()
        self.add_sector_analysis()
        self.add_topic_deep_dive()
        self.add_holdings_tracking()
        self.add_tomorrow_prediction()
        self.add_risk_warning()
        self.add_daily_summary()
        return self


if __name__ == '__main__':
    # 测试生成
    gen = DailyReportProGenerator('2026-06-15', '周一')
    gen.build_standard_report()
    html = gen.render()
    print(f'Pro版日报生成成功，长度: {len(html)} 字符')
    
    # 保存测试
    os.makedirs('../docs/daily', exist_ok=True)
    with open('../docs/daily/test_daily_pro.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print('已保存到 docs/daily/test_daily_pro.html')
