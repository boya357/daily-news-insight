"""
数据时光机生成器 - Pro版
基于Pro组件库和ProPage基类构建
"""
import sys
import os
import json
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from components.pro import (
    ProPage, GlassCard, SectionTitle, TagBadge, 
    RiskBar, DiagnosisItem, FundRow, LhbCard
)


class TimeMachinePage(ProPage):
    """数据时光机页面 - Pro版"""
    
    def __init__(self, data_dir: str = "data/history"):
        super().__init__(
            title="数据时光机",
            active_page="首页",
            footer_text="数据时光机 · 回溯历史 · 见证成长"
        )
        self.data_dir = data_dir
        self.dates = self._get_available_dates()
        self.current_date = self.dates[-1] if self.dates else None
        self.data = self._load_date_data(self.current_date) if self.current_date else None
    
    def _get_available_dates(self) -> list:
        """获取所有可用日期"""
        dates = []
        if os.path.exists(self.data_dir):
            for f in os.listdir(self.data_dir):
                if f.endswith('.json'):
                    dates.append(f.replace('.json', ''))
        return sorted(dates)
    
    def _load_date_data(self, date_str: str) -> dict:
        """加载指定日期的数据"""
        filepath = os.path.join(self.data_dir, f'{date_str}.json')
        if os.path.exists(filepath):
            with open(filepath, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {}
    
    def _generate_date_selector(self) -> str:
        """生成日期选择器"""
        if not self.dates:
            return '<p class="text-white/60">暂无历史数据</p>'
        
        # 日期按钮
        date_buttons = ''
        for i, date in enumerate(reversed(self.dates[-7:])):  # 最近7天
            is_active = date == self.current_date
            active_class = 'bg-gradient-to-r from-indigo-500 to-purple-600 text-white border-transparent' if is_active else 'bg-white/5 text-white/70 border-white/10 hover:bg-white/10'
            
            # 格式化日期显示
            try:
                dt = datetime.strptime(date, '%Y-%m-%d')
                display_date = dt.strftime('%m月%d日')
                weekday = ['周一', '周二', '周三', '周四', '周五', '周六', '周日'][dt.weekday()]
            except:
                display_date = date
                weekday = ''
            
            date_buttons += f'''
            <button class="px-4 py-2 rounded-xl border text-sm font-medium transition-all {active_class}" 
                    onclick="selectDate('{date}')">
                <div>{display_date}</div>
                <div class="text-xs opacity-70">{weekday}</div>
            </button>
            '''
        
        return f'''
        <div class="mb-6">
            {SectionTitle(text='📅 选择日期', icon='📅').render()}
            <div class="flex gap-2 overflow-x-auto pb-2">
                {date_buttons}
            </div>
        </div>
        '''
    
    def _generate_overview(self) -> str:
        """生成组合概览"""
        if not self.data:
            return ''
        
        portfolio = self.data.get('portfolio', {})
        total_return = portfolio.get('total_return', 0)
        health_score = portfolio.get('health_score', 0)
        stock_count = portfolio.get('stock_count', 0)
        profit_count = portfolio.get('profit_count', 0)
        loss_count = portfolio.get('loss_count', 0)
        total_value = portfolio.get('total_value', 0)
        update_time = portfolio.get('update_time', '')
        
        self.update_time = update_time
        
        return_pct = f'+{total_return*100:.2f}%' if total_return >= 0 else f'{total_return*100:.2f}%'
        return_color = 'text-green-400' if total_return >= 0 else 'text-red-400'
        
        content = f'''
            <div class="flex items-center justify-between flex-wrap gap-4">
                <div>
                    <div class="text-sm text-white/60 mb-1">📊 组合总收益</div>
                    <div class="text-4xl font-black {return_color}">{return_pct}</div>
                    <div class="text-sm text-white/60 mt-1">总资产: ¥{total_value:,.0f}</div>
                </div>
                
                <div class="flex items-center gap-6">
                    <div class="text-center">
                        <div class="w-16 h-16 rounded-full bg-gradient-to-br from-green-400 to-emerald-600 flex items-center justify-center text-white text-xl font-black shadow-lg">
                            {health_score}
                        </div>
                        <div class="text-xs text-white/60 mt-2">健康分</div>
                    </div>
                    
                    <div class="grid grid-cols-3 gap-3">
                        <div class="text-center p-2 bg-white/5 rounded-lg">
                            <div class="text-lg font-bold text-white">{stock_count}</div>
                            <div class="text-xs text-white/60">持仓</div>
                        </div>
                        <div class="text-center p-2 bg-white/5 rounded-lg">
                            <div class="text-lg font-bold text-green-400">{profit_count}</div>
                            <div class="text-xs text-white/60">盈利</div>
                        </div>
                        <div class="text-center p-2 bg-white/5 rounded-lg">
                            <div class="text-lg font-bold text-red-400">{loss_count}</div>
                            <div class="text-xs text-white/60">亏损</div>
                        </div>
                    </div>
                </div>
            </div>
        '''
        
        return GlassCard(content=content, padding="p-6", extra_class="mb-6").render()
    
    def _generate_stocks_list(self) -> str:
        """生成持仓股票列表"""
        if not self.data:
            return ''
        
        stocks = self.data.get('stocks', [])
        if not stocks:
            return ''
        
        stocks_html = ''
        for stock in stocks:
            name = stock.get('name', '')
            code = stock.get('code', '')
            current_price = stock.get('current_price', 0)
            cost_price = stock.get('cost_price', 0)
            profit_pct = stock.get('profit_pct', 0)
            today_change = stock.get('today_change', 0)
            tag = stock.get('tag', '')
            tag_color = stock.get('tag_color', 'bg-purple-500')
            
            profit_text = f'+{profit_pct*100:.2f}%' if profit_pct >= 0 else f'{profit_pct*100:.2f}%'
            profit_color = 'text-green-400' if profit_pct >= 0 else 'text-red-400'
            
            today_text = f'+{today_change*100:.2f}%' if today_change >= 0 else f'{today_change*100:.2f}%'
            today_color = 'text-green-400' if today_change >= 0 else 'text-red-400'
            
            stocks_html += f'''
            <div class="p-4 bg-white/5 rounded-xl border border-white/10 mb-3 last:mb-0 hover:bg-white/10 transition-colors">
                <div class="flex items-center justify-between mb-2">
                    <div class="flex items-center gap-3">
                        <div class="w-10 h-10 bg-gradient-to-br from-indigo-500 to-purple-600 rounded-xl flex items-center justify-center text-white font-bold">
                            {name[:2]}
                        </div>
                        <div>
                            <div class="text-white font-semibold">{name}</div>
                            <div class="text-xs text-white/50">{code}</div>
                        </div>
                    </div>
                    {tag and f'<span class="px-2 py-1 {tag_color} text-white text-xs font-medium rounded-full">{tag}</span>'}
                </div>
                
                <div class="grid grid-cols-3 gap-4 mt-3 pt-3 border-t border-white/10">
                    <div>
                        <div class="text-xs text-white/50 mb-1">现价</div>
                        <div class="text-white font-semibold">¥{current_price:.2f}</div>
                    </div>
                    <div>
                        <div class="text-xs text-white/50 mb-1">今日涨跌</div>
                        <div class="font-semibold {today_color}">{today_text}</div>
                    </div>
                    <div>
                        <div class="text-xs text-white/50 mb-1">累计收益</div>
                        <div class="font-semibold {profit_color}">{profit_text}</div>
                    </div>
                </div>
            </div>
            '''
        
        content = f'''
            {SectionTitle(text='📈 持仓明细', icon='📈').render()}
            {stocks_html}
        '''
        
        return GlassCard(content=content, padding="p-6", extra_class="mb-6").render()
    
    def _generate_longhubang(self) -> str:
        """生成龙虎榜数据"""
        if not self.data:
            return ''
        
        lhb = self.data.get('longhubang', {})
        if not lhb:
            return ''
        
        # 简化版龙虎榜
        stocks = lhb.get('stocks', [])
        if not stocks:
            return ''
        
        lhb_html = ''
        for stock in stocks[:3]:  # 只显示前3个
            name = stock.get('name', '')
            reason = stock.get('reason', '')
            net_buy = stock.get('net_buy', 0)
            
            # 确保是数字
            if isinstance(net_buy, str):
                try:
                    net_buy = float(net_buy.replace('万', '').replace('+', ''))
                    if '万' in stock.get('net_buy', ''):
                        net_buy = net_buy * 10000
                except:
                    net_buy = 0
            
            net_buy = float(net_buy) if net_buy else 0
            
            net_text = f'+{net_buy/10000:.2f}万' if net_buy >= 0 else f'{net_buy/10000:.2f}万'
            net_color = 'text-red-400' if net_buy >= 0 else 'text-green-400'
            
            lhb_html += f'''
            <div class="p-3 bg-white/5 rounded-lg mb-2 last:mb-0">
                <div class="flex items-center justify-between">
                    <span class="text-white font-medium">{name}</span>
                    <span class="{net_color} text-sm font-semibold">{net_text}</span>
                </div>
                <div class="text-xs text-white/50 mt-1">{reason}</div>
            </div>
            '''
        
        content = f'''
            {SectionTitle(text='🐉 龙虎榜快照', icon='🐉').render()}
            {lhb_html}
        '''
        
        return GlassCard(content=content, padding="p-6", extra_class="mb-6").render()
    
    def _content(self) -> str:
        """页面主要内容"""
        date_selector = self._generate_date_selector()
        overview = self._generate_overview()
        stocks_list = self._generate_stocks_list()
        longhubang = self._generate_longhubang()
        
        return f'''
            {date_selector}
            {overview}
            {stocks_list}
            {longhubang}
            
            <script>
                function selectDate(date) {{
                    // 实际项目中这里会有AJAX加载或页面跳转
                    console.log('选择日期:', date);
                    alert('时间旅行到 ' + date + '！\\n(完整功能需后端支持)');
                }}
            </script>
        '''


if __name__ == '__main__':
    page = TimeMachinePage()
    html = page.render()
    
    output_path = '/tmp/test_time_machine_pro.html'
    page.save(output_path)
    
    print(f"✅ 生成完成")
    print(f"   输出文件: {output_path}")
    print(f"   文件大小: {len(html)} 字节")
    print(f"   可用日期数: {len(page.dates)}")
    print(f"   当前日期: {page.current_date}")
