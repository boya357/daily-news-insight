"""
龙虎榜生成器 - Pro版
基于Pro组件库重构，深色玻璃态风格
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
    """龙虎榜 - Pro版生成器"""
    
    data_type = "portfolio"
    
    def __init__(self, data_dir: str = "data"):
        super().__init__(
            title="龙虎榜追踪",
            active_page="盘后",
            footer_text="龙虎榜追踪 · 洞察主力动向",
            data_dir=data_dir,
            show_toc=True,
        )
    def load_data(self):
        """加载龙虎榜数据"""
        super().load_data()
        self.data = self.data_loader.get_data("portfolio")
        self.lhb_data = self.data.get('longhubang', {})
        self.stocks = self.lhb_data.get('stocks', [])
    
    def _generate_stock_card(self, stock: dict) -> str:
        """生成单只股票龙虎榜卡片"""
        name = stock.get('name', '')
        code = stock.get('code', '')
        date = stock.get('date', '')
        close_price = stock.get('close_price', '')
        change_pct = stock.get('change_pct', 0)
        turnover_rate = stock.get('turnover_rate', '')
        turnover_amount = stock.get('turnover_amount', '')
        list_reason = stock.get('list_reason', '')
        total_buy = stock.get('total_buy', '')
        total_sell = stock.get('total_sell', '')
        net_buy = stock.get('net_buy', '')
        institution_net = stock.get('institution_net', '')
        northbound_net = stock.get('northbound_net', '')
        business_department_net = stock.get('business_department_net', '')
        buy_seats = stock.get('buy_seats', [])
        sell_seats = stock.get('sell_seats', [])
        analysis = stock.get('analysis', '')
        
        is_up = change_pct >= 0
        change_color = 'text-red-400' if is_up else 'text-green-400'
        
        # 判断净买入正负
        net_buy_positive = not (str(net_buy).startswith('-'))
        net_buy_color = 'text-red-400' if net_buy_positive else 'text-green-400'
        
        # 席位列表
        def render_seats(seats, is_buy=True):
            if not seats:
                return ''
            html = ''
            for i, seat in enumerate(seats[:5]):
                seat_name = seat.get('name', '') if isinstance(seat, dict) else str(seat)
                amount = seat.get('amount', '') if isinstance(seat, dict) else ''
                seat_type = seat.get('type', '') if isinstance(seat, dict) else ''
                
                type_tag = ''
                if seat_type == 'institution':
                    type_tag = '<span class="px-1.5 py-0.5 bg-blue-500/20 text-blue-400 text-xs rounded">机构</span>'
                elif seat_type == 'northbound':
                    type_tag = '<span class="px-1.5 py-0.5 bg-green-500/20 text-green-400 text-xs rounded">北向</span>'
                elif seat_type == 'famous':
                    type_tag = '<span class="px-1.5 py-0.5 bg-purple-500/20 text-purple-400 text-xs rounded">游资</span>'
                
                html += f'''
                <div class="flex items-center justify-between py-2 border-b border-white/5 last:border-b-0">
                    <div class="flex items-center gap-2 min-w-0">
                        <span class="text-white/40 text-xs w-5">{i+1}</span>
                        <span class="text-sm text-white/80 truncate">{seat_name}</span>
                        {type_tag}
                    </div>
                    {amount and f'<span class="text-sm font-medium {"text-red-400" if is_buy else "text-green-400"}">{amount}</span>'}
                </div>
                '''
            return html
        
        content = f'''
        <div class="bg-white/5 border border-white/10 rounded-2xl overflow-hidden">
            <!-- 头部 -->
            <div class="p-6 bg-gradient-to-r from-purple-500/20 to-indigo-500/20 border-b border-white/10">
                <div class="flex items-center justify-between">
                    <div>
                        <h3 class="text-white font-bold text-xl">{name}</h3>
                        <p class="text-white/50 text-sm">{code} · {date}</p>
                    </div>
                    <div class="text-right">
                        <div class="text-2xl font-black {change_color}">{close_price}</div>
                        <div class="{change_color} text-sm">{"+" if is_up else ""}{change_pct}%</div>
                    </div>
                </div>
                <div class="mt-3 flex items-center gap-3 flex-wrap">
                    <span class="px-3 py-1 bg-white/10 text-white/70 text-xs rounded-full">
                        上榜原因: {list_reason}
                    </span>
                    <span class="px-3 py-1 bg-white/10 text-white/70 text-xs rounded-full">
                        换手率: {turnover_rate}%
                    </span>
                    <span class="px-3 py-1 bg-white/10 text-white/70 text-xs rounded-full">
                        成交额: {turnover_amount}
                    </span>
                </div>
            </div>
            
            <!-- 资金概览 -->
            <div class="p-6 grid grid-cols-2 md:grid-cols-4 gap-4 border-b border-white/10">
                <div class="text-center">
                    <div class="text-red-400 text-lg font-bold">{total_buy}</div>
                    <div class="text-xs text-white/50 mt-1">买入总额</div>
                </div>
                <div class="text-center">
                    <div class="text-green-400 text-lg font-bold">{total_sell}</div>
                    <div class="text-xs text-white/50 mt-1">卖出总额</div>
                </div>
                <div class="text-center">
                    <div class="{net_buy_color} text-lg font-bold">{net_buy}</div>
                    <div class="text-xs text-white/50 mt-1">净买入</div>
                </div>
                <div class="text-center">
                    <div class="text-blue-400 text-lg font-bold">{institution_net}</div>
                    <div class="text-xs text-white/50 mt-1">机构净额</div>
                </div>
            </div>
            
            <!-- 买卖席位 -->
            <div class="p-6 grid grid-cols-1 md:grid-cols-2 gap-6">
                <div>
                    <h4 class="text-red-400 font-bold mb-3 flex items-center gap-2">
                        <span>📈</span> 买入前五
                    </h4>
                    <div class="bg-white/5 rounded-xl p-3">
                        {render_seats(buy_seats, True) if buy_seats else '<p class="text-white/40 text-sm">暂无数据</p>'}
                    </div>
                </div>
                <div>
                    <h4 class="text-green-400 font-bold mb-3 flex items-center gap-2">
                        <span>📉</span> 卖出前五
                    </h4>
                    <div class="bg-white/5 rounded-xl p-3">
                        {render_seats(sell_seats, False) if sell_seats else '<p class="text-white/40 text-sm">暂无数据</p>'}
                    </div>
                </div>
            </div>
            
            <!-- 北向和营业部 -->
            <div class="px-6 pb-6 grid grid-cols-2 gap-4">
                <div class="bg-white/5 rounded-xl p-4 text-center">
                    <div class="text-green-400 font-bold">{northbound_net}</div>
                    <div class="text-xs text-white/50 mt-1">北向资金净额</div>
                </div>
                <div class="bg-white/5 rounded-xl p-4 text-center">
                    <div class="text-purple-400 font-bold">{business_department_net}</div>
                    <div class="text-xs text-white/50 mt-1">营业部净额</div>
                </div>
            </div>
            
            <!-- 分析 -->
            {analysis and f'''
            <div class="px-6 pb-6">
                <div class="p-4 bg-gradient-to-r from-purple-500/10 to-transparent border-l-2 border-purple-400 rounded-r-lg">
                    <div class="text-purple-400 text-sm font-medium mb-1">💡 综合分析</div>
                    <p class="text-sm text-white/70">{analysis}</p>
                </div>
            </div>
            '''}
        </div>
        '''
        
        return content
    
    def _generate_stocks_section(self) -> str:
        """生成股票列表区域"""
        if not self.stocks:
            content = '<p class="text-white/50 text-center py-8">暂无龙虎榜数据</p>'
            return GlassCard(content=content, padding="p-6", extra_class="mb-6").render()
        
        cards_html = ''
        for stock in self.stocks:
            cards_html += self._generate_stock_card(stock)
        
        content = f'''
            {SectionTitle(text='🐉 龙虎榜数据', icon='🐉').render()}
            <div class="space-y-6">
                {cards_html}
            </div>
        '''
        
        return GlassCard(content=content, padding="p-6", extra_class="mb-6").render()
    
    def _content(self) -> str:
        """页面主要内容"""
        stocks_section = self._generate_stocks_section()
        
        return f'''
            <div class="text-center mb-8 pt-4">
                <h1 class="text-3xl font-black text-white mb-2">🐉 龙虎榜</h1>
                <p class="text-white/70">追踪主力资金动向，洞察机构行为</p>
            </div>
            
            {stocks_section}
        '''
    
    def publish(self, output_path: str = None):
        """发布到生产路径"""
        if output_path is None:
            output_path = "docs/portfolio/index_pro.html"
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
    print(f"   上榜股票: {len(generator.stocks)} 只")
