"""
龙虎榜生成器 - Pro版（全市场扫描）
基于Pro组件库重构，深色玻璃态风格
从"持仓龙虎榜查询"升级为"全市场龙虎榜扫描+题材挖掘+龙头识别"
"""
import sys
import os
import json
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from components.pro import (
    GlassCard, SectionTitle, TagBadge
)
from generators.pro_base import ProGenerator


class LonghuBangProGenerator(ProGenerator):
    """龙虎榜 - 全市场扫描版"""
    
    data_type = "longhubang_market"
    
    def __init__(self, data_dir: str = "data"):
        super().__init__(
            title="龙虎榜透视",
            active_page="盘后",
            footer_text="龙虎榜透视 · 洞察主力资金动向",
            data_dir=data_dir,
            show_toc=True,
        )
        self.data_dir = data_dir
    
    def load_data(self):
        """加载龙虎榜数据"""
        data_path = os.path.join(self.data_dir, "longhubang_market.json")
        if os.path.exists(data_path):
            with open(data_path, 'r', encoding='utf-8') as f:
                self.data = json.load(f)
        else:
            self.data = {}
        
        self.overview = self.data.get('market_overview', {})
        self.hot_sectors = self.data.get('hot_sectors', [])
        self.dragon_heads = self.data.get('dragon_head_stocks', [])
        self.institution = self.data.get('institution_trends', {})
        self.hot_money = self.data.get('hot_money_tracking', {})
        self.predictions = self.data.get('topic_prediction', {})
        self.portfolio_stocks = self.data.get('portfolio_stocks', [])
        self.all_stocks = self.data.get('all_stocks', [])
    
    def _generate_overview_section(self) -> str:
        """生成市场总览模块"""
        overview = self.overview
        
        content = f'''
        {SectionTitle(text='📊 今日龙虎榜总览', icon='📊').render()}
        <div class="grid grid-cols-2 md:grid-cols-4 gap-4 mb-6">
            <div class="bg-gradient-to-br from-purple-500/20 to-purple-600/10 rounded-xl p-4 text-center border border-purple-500/20">
                <div class="text-2xl font-black text-white">{overview.get('total_stocks', 0)}</div>
                <div class="text-xs text-white/60 mt-1">上榜股票</div>
            </div>
            <div class="bg-gradient-to-br from-red-500/20 to-red-600/10 rounded-xl p-4 text-center border border-red-500/20">
                <div class="text-2xl font-black text-red-400">{overview.get('total_net_buy', '0')}</div>
                <div class="text-xs text-white/60 mt-1">净买入总额</div>
            </div>
            <div class="bg-gradient-to-br from-blue-500/20 to-blue-600/10 rounded-xl p-4 text-center border border-blue-500/20">
                <div class="text-2xl font-black text-blue-400">{overview.get('institution_net_buy', '0')}</div>
                <div class="text-xs text-white/60 mt-1">机构净买入</div>
            </div>
            <div class="bg-gradient-to-br from-green-500/20 to-green-600/10 rounded-xl p-4 text-center border border-green-500/20">
                <div class="text-2xl font-black text-green-400">{overview.get('northbound_net_buy', '0')}</div>
                <div class="text-xs text-white/60 mt-1">北向净买入</div>
            </div>
        </div>
        
        <div class="grid grid-cols-3 gap-4">
            <div class="bg-white/5 rounded-xl p-4 text-center">
                <div class="text-xl font-bold text-red-400">{overview.get('limit_up_count', 0)}</div>
                <div class="text-xs text-white/60 mt-1">涨停股数</div>
            </div>
            <div class="bg-white/5 rounded-xl p-4 text-center">
                <div class="text-xl font-bold text-green-400">{overview.get('limit_down_count', 0)}</div>
                <div class="text-xs text-white/60 mt-1">跌停股数</div>
            </div>
            <div class="bg-white/5 rounded-xl p-4 text-center">
                <div class="text-xl font-bold text-orange-400">{overview.get('market_sentiment', '-')}</div>
                <div class="text-xs text-white/60 mt-1">市场情绪</div>
                <div class="text-xs text-white/40">({overview.get('sentiment_score', 0)}分)</div>
            </div>
        </div>
        '''
        
        return GlassCard(content=content, padding="p-6", extra_class="mb-6").render()
    
    def _generate_hot_sectors_section(self) -> str:
        """生成热门板块挖掘模块"""
        if not self.hot_sectors:
            return ''
        
        sectors_html = ''
        for sector in self.hot_sectors:
            strength = sector.get('strength', '中')
            strength_color = {
                '强': 'text-red-400 bg-red-500/10',
                '中强': 'text-orange-400 bg-orange-500/10',
                '中': 'text-yellow-400 bg-yellow-500/10',
                '弱': 'text-green-400 bg-green-500/10'
            }.get(strength, 'text-white/60 bg-white/5')
            
            sectors_html += f'''
            <div class="bg-white/5 rounded-xl p-4 hover:bg-white/10 transition-colors">
                <div class="flex items-center justify-between mb-3">
                    <h4 class="text-white font-bold">{sector.get('name', '')}</h4>
                    <span class="px-2 py-1 {strength_color} text-xs rounded-full">{strength}</span>
                </div>
                <div class="grid grid-cols-2 gap-3 text-sm mb-3">
                    <div>
                        <span class="text-white/50">上榜数量</span>
                        <span class="text-white ml-2">{sector.get('stock_count', 0)}只</span>
                    </div>
                    <div>
                        <span class="text-white/50">净买入</span>
                        <span class="text-red-400 ml-2">{sector.get('total_net_buy', '0')}</span>
                    </div>
                    <div>
                        <span class="text-white/50">机构净额</span>
                        <span class="text-blue-400 ml-2">{sector.get('institution_net', '0')}</span>
                    </div>
                    <div>
                        <span class="text-white/50">龙头股</span>
                        <span class="text-yellow-400 ml-2">{sector.get('leading_stock', '')}</span>
                    </div>
                </div>
            </div>
            '''
        
        content = f'''
        {SectionTitle(text='💎 热门板块挖掘', icon='💎').render()}
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
            {sectors_html}
        </div>
        '''
        
        return GlassCard(content=content, padding="p-6", extra_class="mb-6").render()
    
    def _generate_dragon_heads_section(self) -> str:
        """生成龙头股识别模块"""
        if not self.dragon_heads:
            return ''
        
        stocks_html = ''
        for stock in self.dragon_heads:
            is_up = stock.get('change_pct', 0) >= 0
            change_color = 'text-red-400' if is_up else 'text-green-400'
            
            # 连板天数
            consecutive = stock.get('consecutive_days', 0)
            consecutive_badge = ''
            if consecutive >= 3:
                consecutive_badge = f'<span class="px-2 py-0.5 bg-red-500/20 text-red-400 text-xs rounded-full">{consecutive}连板</span>'
            elif consecutive >= 2:
                consecutive_badge = f'<span class="px-2 py-0.5 bg-orange-500/20 text-orange-400 text-xs rounded-full">{consecutive}连板</span>'
            
            stocks_html += f'''
            <div class="bg-white/5 rounded-xl p-4 hover:bg-white/10 transition-colors">
                <div class="flex items-center justify-between mb-2">
                    <div class="flex items-center gap-2">
                        <span class="w-6 h-6 flex items-center justify-center bg-gradient-to-br from-yellow-400 to-orange-500 text-white text-xs font-bold rounded-full">
                            {stock.get('rank', 0)}
                        </span>
                        <h4 class="text-white font-bold">{stock.get('name', '')}</h4>
                        <span class="text-white/40 text-xs">{stock.get('code', '')}</span>
                    </div>
                    <div class="text-right">
                        <div class="text-white font-bold">{stock.get('close_price', 0)}</div>
                        <div class="{change_color} text-sm">{'+' if is_up else ''}{stock.get('change_pct', 0)}%</div>
                    </div>
                </div>
                <div class="flex items-center gap-2 mb-2">
                    {consecutive_badge}
                    <span class="px-2 py-0.5 bg-purple-500/20 text-purple-400 text-xs rounded-full">{stock.get('topic', '')}</span>
                </div>
                <div class="grid grid-cols-2 gap-2 text-sm">
                    <div>
                        <span class="text-white/50">净买入</span>
                        <span class="text-red-400 ml-1">{stock.get('net_buy', '')}</span>
                    </div>
                    <div>
                        <span class="text-white/50">机构净额</span>
                        <span class="text-blue-400 ml-1">{stock.get('institution_net', '')}</span>
                    </div>
                </div>
                <div class="mt-3 flex items-center justify-between">
                    <span class="text-white/50 text-xs">综合评分</span>
                    <div class="flex items-center gap-2">
                        <div class="w-24 h-2 bg-white/10 rounded-full overflow-hidden">
                            <div class="h-full bg-gradient-to-r from-purple-500 to-pink-500 rounded-full" style="width: {stock.get('score', 0)}%"></div>
                        </div>
                        <span class="text-purple-400 text-sm font-bold">{stock.get('score', 0)}</span>
                    </div>
                </div>
            </div>
            '''
        
        content = f'''
        {SectionTitle(text='🐉 龙头股识别', icon='🐉').render()}
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
            {stocks_html}
        </div>
        '''
        
        return GlassCard(content=content, padding="p-6", extra_class="mb-6").render()
    
    def _generate_institution_section(self) -> str:
        """生成机构动向模块"""
        inst = self.institution
        if not inst:
            return ''
        
        # 买入榜
        buy_html = ''
        for i, stock in enumerate(inst.get('top_buy_stocks', []), 1):
            buy_html += f'''
            <div class="flex items-center justify-between py-2 border-b border-white/5 last:border-b-0">
                <div class="flex items-center gap-3">
                    <span class="w-5 h-5 flex items-center justify-center bg-red-500/20 text-red-400 text-xs rounded-full">{i}</span>
                    <span class="text-white/80">{stock.get('name', '')}</span>
                    <span class="text-white/40 text-xs">{stock.get('sector', '')}</span>
                </div>
                <span class="text-red-400 font-medium">{stock.get('net_buy', '')}</span>
            </div>
            '''
        
        # 卖出榜
        sell_html = ''
        for i, stock in enumerate(inst.get('top_sell_stocks', []), 1):
            sell_html += f'''
            <div class="flex items-center justify-between py-2 border-b border-white/5 last:border-b-0">
                <div class="flex items-center gap-3">
                    <span class="w-5 h-5 flex items-center justify-center bg-green-500/20 text-green-400 text-xs rounded-full">{i}</span>
                    <span class="text-white/80">{stock.get('name', '')}</span>
                    <span class="text-white/40 text-xs">{stock.get('sector', '')}</span>
                </div>
                <span class="text-green-400 font-medium">{stock.get('net_sell', '')}</span>
            </div>
            '''
        
        buy_sectors = '、'.join(inst.get('buy_dominant_sectors', []))
        sell_sectors = '、'.join(inst.get('sell_dominant_sectors', []))
        
        content = f'''
        {SectionTitle(text='🏛️ 机构动向', icon='🏛️').render()}
        <div class="grid grid-cols-3 gap-4 mb-6">
            <div class="bg-blue-500/10 rounded-xl p-4 text-center border border-blue-500/20">
                <div class="text-xl font-bold text-blue-400">{inst.get('total_buy', '0')}</div>
                <div class="text-xs text-white/60 mt-1">机构买入</div>
            </div>
            <div class="bg-green-500/10 rounded-xl p-4 text-center border border-green-500/20">
                <div class="text-xl font-bold text-green-400">{inst.get('total_sell', '0')}</div>
                <div class="text-xs text-white/60 mt-1">机构卖出</div>
            </div>
            <div class="bg-purple-500/10 rounded-xl p-4 text-center border border-purple-500/20">
                <div class="text-xl font-bold text-purple-400">{inst.get('net_buy', '0')}</div>
                <div class="text-xs text-white/60 mt-1">机构净额</div>
            </div>
        </div>
        
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div>
                <h4 class="text-red-400 font-bold mb-3 flex items-center gap-2">
                    <span>📈</span> 机构净买入TOP5
                </h4>
                <div class="bg-white/5 rounded-xl p-4">
                    {buy_html}
                </div>
                <div class="mt-3 text-xs text-white/50">
                    机构主攻方向：<span class="text-red-400">{buy_sectors}</span>
                </div>
            </div>
            <div>
                <h4 class="text-green-400 font-bold mb-3 flex items-center gap-2">
                    <span>📉</span> 机构净卖出TOP5
                </h4>
                <div class="bg-white/5 rounded-xl p-4">
                    {sell_html}
                </div>
                <div class="mt-3 text-xs text-white/50">
                    机构抛售方向：<span class="text-green-400">{sell_sectors}</span>
                </div>
            </div>
        </div>
        '''
        
        return GlassCard(content=content, padding="p-6", extra_class="mb-6").render()
    
    def _generate_hot_money_section(self) -> str:
        """生成游资追踪模块"""
        hm = self.hot_money
        if not hm:
            return ''
        
        seats_html = ''
        for seat in hm.get('famous_seats', []):
            success_rate = seat.get('recent_success_rate', '0%')
            rate_num = int(success_rate.replace('%', ''))
            rate_color = 'text-green-400' if rate_num >= 65 else 'text-yellow-400' if rate_num >= 55 else 'text-red-400'
            
            focus_stocks = '、'.join(seat.get('focus_stocks', []))
            
            seats_html += f'''
            <div class="bg-white/5 rounded-xl p-4">
                <div class="flex items-center justify-between mb-3">
                    <h4 class="text-white font-bold text-sm">{seat.get('name', '')}</h4>
                    <span class="{rate_color} text-xs">{success_rate}胜率</span>
                </div>
                <div class="grid grid-cols-3 gap-2 text-xs mb-2">
                    <div class="text-center">
                        <div class="text-red-400 font-medium">{seat.get('today_buy', '')}</div>
                        <div class="text-white/40">买入</div>
                    </div>
                    <div class="text-center">
                        <div class="text-green-400 font-medium">{seat.get('today_sell', '')}</div>
                        <div class="text-white/40">卖出</div>
                    </div>
                    <div class="text-center">
                        <div class="text-purple-400 font-medium">{seat.get('net_buy', '')}</div>
                        <div class="text-white/40">净额</div>
                    </div>
                </div>
                <div class="text-xs text-white/50 mt-2">
                    主攻：<span class="text-white/70">{focus_stocks}</span>
                </div>
            </div>
            '''
        
        focus_topics = '、'.join(hm.get('focus_topics', []))
        
        content = f'''
        {SectionTitle(text='⚡ 游资追踪', icon='⚡').render()}
        <div class="mb-4 text-sm text-white/60">
            今日游资风格：<span class="text-orange-400 font-medium">{hm.get('hot_money_style', '')}</span>
            &nbsp;|&nbsp;
            主攻题材：<span class="text-purple-400 font-medium">{focus_topics}</span>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
            {seats_html}
        </div>
        '''
        
        return GlassCard(content=content, padding="p-6", extra_class="mb-6").render()
    
    def _generate_prediction_section(self) -> str:
        """生成题材预判模块"""
        pred = self.predictions
        if not pred:
            return ''
        
        def render_predictions(items, level_color, level_label):
            html = ''
            for item in items:
                key_stocks = '、'.join(item.get('key_stocks', []))
                html += f'''
                <div class="bg-white/5 rounded-xl p-4 mb-3 last:mb-0">
                    <div class="flex items-center justify-between mb-2">
                        <h4 class="text-white font-bold">{item.get('topic', '')}</h4>
                        <span class="px-2 py-1 {level_color} text-xs rounded-full">{item.get('probability', '')}</span>
                    </div>
                    <div class="text-sm text-white/70 mb-2">{item.get('reason', '')}</div>
                    <div class="flex items-center justify-between text-xs">
                        <span class="text-white/50">持续性：<span class="text-white/70">{item.get('sustainability', '')}</span></span>
                        <span class="text-white/50">核心标的：<span class="text-purple-400">{key_stocks}</span></span>
                    </div>
                </div>
                '''
            return html
        
        high_html = render_predictions(pred.get('high_probability', []), 'bg-green-500/20 text-green-400', '高概率')
        medium_html = render_predictions(pred.get('medium_probability', []), 'bg-yellow-500/20 text-yellow-400', '中概率')
        low_html = render_predictions(pred.get('low_probability', []), 'bg-red-500/20 text-red-400', '低概率')
        
        content = f'''
        {SectionTitle(text='🔮 题材预判', icon='🔮').render()}
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
            <div>
                <h4 class="text-green-400 font-bold mb-3 flex items-center gap-2">
                    <span>🟢</span> 高概率 (70%+)
                </h4>
                {high_html}
            </div>
            <div>
                <h4 class="text-yellow-400 font-bold mb-3 flex items-center gap-2">
                    <span>🟡</span> 中概率 (50-70%)
                </h4>
                {medium_html}
            </div>
            <div>
                <h4 class="text-red-400 font-bold mb-3 flex items-center gap-2">
                    <span>🔴</span> 低概率 (<50%)
                </h4>
                {low_html}
            </div>
        </div>
        '''
        
        return GlassCard(content=content, padding="p-6", extra_class="mb-6").render()
    
    def _generate_portfolio_section(self) -> str:
        """生成自选股龙虎榜模块"""
        if not self.portfolio_stocks:
            return ''
        
        stocks_html = ''
        for stock in self.portfolio_stocks:
            name = stock.get('name', '')
            code = stock.get('code', '')
            close_price = stock.get('close_price', 0)
            change_pct = stock.get('change_pct', 0)
            net_buy = stock.get('net_buy', '')
            institution_net = stock.get('institution_net', '')
            analysis = stock.get('analysis', '')
            list_reason = stock.get('list_reason', '')
            
            is_up = change_pct >= 0
            change_color = 'text-red-400' if is_up else 'text-green-400'
            
            # 判断净买卖
            net_positive = not str(net_buy).startswith('-')
            net_color = 'text-red-400' if net_positive else 'text-green-400'
            
            stocks_html += f'''
            <div class="bg-white/5 rounded-xl p-4">
                <div class="flex items-center justify-between mb-3">
                    <div>
                        <h4 class="text-white font-bold">{name}</h4>
                        <p class="text-white/40 text-xs">{code}</p>
                    </div>
                    <div class="text-right">
                        <div class="text-white font-bold">{close_price}</div>
                        <div class="{change_color} text-sm">{'+' if is_up else ''}{change_pct}%</div>
                    </div>
                </div>
                <div class="text-xs text-white/50 mb-3">{list_reason}</div>
                <div class="grid grid-cols-2 gap-2 text-sm mb-3">
                    <div>
                        <span class="text-white/50">净买入</span>
                        <span class="{net_color} ml-1">{net_buy}</span>
                    </div>
                    <div>
                        <span class="text-white/50">机构净额</span>
                        <span class="text-blue-400 ml-1">{institution_net}</span>
                    </div>
                </div>
                {analysis and f'''
                <div class="p-3 bg-gradient-to-r from-purple-500/10 to-transparent border-l-2 border-purple-400 rounded-r-lg">
                    <p class="text-sm text-white/70">{analysis}</p>
                </div>
                '''}
            </div>
            '''
        
        content = f'''
        {SectionTitle(text='⭐ 持仓股龙虎榜', icon='⭐').render()}
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            {stocks_html}
        </div>
        '''
        
        return GlassCard(content=content, padding="p-6", extra_class="mb-6").render()
    
    def _content(self) -> str:
        """页面主要内容"""
        overview_section = self._generate_overview_section()
        hot_sectors_section = self._generate_hot_sectors_section()
        dragon_heads_section = self._generate_dragon_heads_section()
        institution_section = self._generate_institution_section()
        hot_money_section = self._generate_hot_money_section()
        prediction_section = self._generate_prediction_section()
        portfolio_section = self._generate_portfolio_section()
        
        return f'''
            <div class="text-center mb-8 pt-4">
                <h1 class="text-3xl font-black text-white mb-2">🐉 龙虎榜透视</h1>
                <p class="text-white/70">全市场龙虎榜扫描 · 主力资金动向追踪 · 题材挖掘预判</p>
                <p class="text-white/40 text-sm mt-2">数据更新时间：{self.data.get('update_time', '')}</p>
            </div>
            
            {overview_section}
            {hot_sectors_section}
            {dragon_heads_section}
            {institution_section}
            {hot_money_section}
            {prediction_section}
            {portfolio_section}
        '''
    
    def publish(self, output_path: str = None):
        """发布到生产路径"""
        if output_path is None:
            output_path = "docs/longhubang/index.html"
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        return super().publish(output_path)


if __name__ == '__main__':
    generator = LonghuBangProGenerator()
    html = generator.render()
    
    output_path = '/tmp/test_longhubang_pro.html'
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"✅ 生成完成")
    print(f"   输出文件: {output_path}")
    print(f"   文件大小: {len(html)} 字节")
    print(f"   上榜股票: {len(generator.all_stocks)} 只")
    print(f"   热门板块: {len(generator.hot_sectors)} 个")
    print(f"   龙头股票: {len(generator.dragon_heads)} 只")
