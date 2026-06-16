"""
周复盘生成器 - Pro版
基于ReportProGenerator基类重构，深色玻璃态风格
一周市场总结 + 热点回顾 + 下周展望
V3.5升级：集成Tab切换、卡片组、数据网格通用组件
"""
import sys
import os
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from generators.report_pro_base import ReportProGenerator
from utils.data_loader import get_indices_for_daily, load_portfolio, get_hot_sectors


class WeeklyReviewProGenerator(ReportProGenerator):
    """周复盘生成器 - Pro版"""
    
    def __init__(self, date_str: str = None, week_num: str = None, subtitle: str = None, data_dir: str = "data"):
        date = date_str or datetime.now().strftime('%Y-%m-%d')
        sub = subtitle or f"{date} · 周度复盘"
        
        super().__init__(
            title="周复盘",
            report_type="weekly_review",
            subtitle=sub,
            date_str=date,
            data_dir=data_dir,
        )
        
        self.active_page = "周复盘"
        self.indices = get_indices_for_daily()
        self.portfolio = load_portfolio()
    
    def add_week_summary(self, summary: str = None):
        """添加本周核心总结"""
        if summary is None:
            summary = """
            本周市场整体呈现震荡格局，板块轮动明显。AI算力、人形机器人等科技主线延续强势，
            传统周期板块表现分化。市场情绪整体平稳，结构性机会依然丰富。
            """
        
        content = f'''
        <div class="bg-gradient-to-r from-blue-500/20 to-purple-500/15 border border-blue-500/30 rounded-xl p-5">
            <div class="flex items-center gap-2 mb-3">
                <span class="text-2xl">✅</span>
                <span class="text-white font-bold">本周核心总结</span>
            </div>
            <p class="text-white/80 leading-relaxed text-sm">
                {summary.strip()}
            </p>
        </div>
        '''
        self.add_section("本周核心总结", content, "✅")
    
    def add_market_review(self):
        """添加本周市场表现 - 使用DataGrid组件"""
        data_items = []
        for idx in self.indices:
            name = idx.get('name', '')
            value = idx.get('price', idx.get('value', '--'))
            change = idx.get('change_pct_str', idx.get('change', ''))
            up = idx.get('up', True)
            
            change_val = change.replace('%', '').replace('+', '')
            try:
                change_num = float(change_val)
                if up or change_num > 0:
                    color = 'text-green-400'
                else:
                    color = 'text-red-400'
            except:
                color = 'text-white/60'
            
            data_items.append({
                'title': name,
                'value': str(value),
                'unit': '',
                'desc': f'<span class="{color} font-semibold">{change}</span>',
                'icon': '📈' if up else '📉'
            })
        
        # 使用DataGrid组件
        content = self.create_data_grid(items=data_items, cols=4)
        
        self.add_section("本周市场表现", content, "📊")
    
    def add_hot_topics_review(self, topics: list = None):
        """添加本周热点题材回顾 - 使用Tab切换+卡片组"""
        if topics is None:
            topics = [
                {"name": "AI算力", "performance": "+8.5%", "logic": "AI大模型持续迭代，算力需求爆发增长", "stocks": ["英伟达", "寒武纪"], "category": "科技"},
                {"name": "人形机器人", "performance": "+6.2%", "logic": "特斯拉Optimus进展超预期，产业链加速落地", "stocks": ["拓普集团", "三花智控"], "category": "科技"},
                {"name": "存储芯片", "performance": "+5.8%", "logic": "行业周期反转，价格持续上涨", "stocks": ["兆易创新", "北京君正"], "category": "科技"},
                {"name": "先进封装", "performance": "+4.5%", "logic": "Chiplet技术加速渗透，国产替代加速", "stocks": ["长电科技", "通富微电"], "category": "科技"},
                {"name": "新能源", "performance": "+2.1%", "logic": "政策支持持续，销量数据向好", "stocks": ["宁德时代", "比亚迪"], "category": "新能源"},
                {"name": "医药生物", "performance": "-1.2%", "logic": "集采政策影响，板块承压", "stocks": ["恒瑞医药", "药明康德"], "category": "消费"},
            ]
        
        # 按分类整理
        categories = {}
        for topic in topics:
            cat = topic.get('category', '其他')
            if cat not in categories:
                categories[cat] = []
            categories[cat].append(topic)
        
        # 生成Tab内容
        tabs = []
        for cat, cat_topics in categories.items():
            cards = []
            for topic in cat_topics:
                name = topic.get("name", "")
                performance = topic.get("performance", "")
                logic = topic.get("logic", "")
                stocks = topic.get("stocks", [])
                
                is_up = performance.startswith('+')
                perf_color = 'text-green-400' if is_up else 'text-red-400'
                
                stocks_html = ''
                if stocks:
                    stock_tags = ' '.join([
                        f'<span class="bg-blue-500/20 text-blue-400 text-xs px-2 py-1 rounded-md border border-blue-500/30">{s}</span>'
                        for s in stocks
                    ])
                    stocks_html = f'''
                    <div class="mt-3 pt-3 border-t border-white/10">
                        <div class="text-xs text-white/50 mb-2">龙头标的</div>
                        <div class="flex flex-wrap gap-2">{stock_tags}</div>
                    </div>
                    '''
                
                card_content = f'''
                <div class="flex items-center gap-3 mb-2">
                    <span class="text-white font-semibold text-sm">{name}</span>
                    <span class="text-xs font-bold {perf_color} bg-white/10 px-2.5 py-1 rounded-full">
                        {performance}
                    </span>
                </div>
                <div class="text-sm text-white/60 leading-relaxed">
                    {logic}
                </div>
                {stocks_html}
                '''
                
                cards.append({
                    'title': '',
                    'content': card_content,
                    'icon': '🔥'
                })
            
            cards_html = self.create_card_group(cards=cards, cols=2, card_style='glass')
            tabs.append({
                'label': cat,
                'content': cards_html
            })
        
        # 使用Tab组件
        tab_content = self.create_tab_pane(tabs=tabs, tab_id="hot-topics", style="default")
        
        self.add_section("本周热点题材回顾", tab_content, "🔥")
    
    def add_important_events(self, events: list = None):
        """添加本周重要事件时间线"""
        if events is None:
            events = [
                {"date": "周一", "title": "重要政策发布", "desc": "相关部门发布新政策，支持科技创新和产业升级。"},
                {"date": "周二", "title": "经济数据公布", "desc": "多项经济数据公布，整体符合市场预期。"},
                {"date": "周三", "title": "行业大会召开", "desc": "重要行业大会召开，多家巨头发布新产品。"},
                {"date": "周四", "title": "海外市场波动", "desc": "美股市场波动，对A股产生一定影响。"},
                {"date": "周五", "title": "资金面变化", "desc": "北向资金流向变化，市场情绪有所转向。"},
            ]
        
        events_html = '<div class="relative pl-6">'
        
        for i, event in enumerate(events):
            is_last = i == len(events) - 1
            date = event.get("date", "")
            title = event.get("title", "")
            desc = event.get("desc", "")
            
            events_html += f'''
            <div class="relative pb-5 {"pb-0" if is_last else ""}">
                <!-- 时间线竖线 -->
                <div class="absolute left-[-1.5rem] top-2 w-0.5 h-full bg-gradient-to-b from-blue-500 to-purple-500 {"h-0" if is_last else ""}"></div>
                <!-- 时间点 -->
                <div class="absolute left-[-1.75rem] top-1 w-3.5 h-3.5 rounded-full bg-gradient-to-br from-blue-500 to-purple-500 border-2 border-purple-900"></div>
                <!-- 内容 -->
                <div class="bg-white/5 rounded-lg p-3 ml-2 border border-white/10">
                    <div class="flex items-center gap-2 mb-1">
                        <span class="text-xs font-semibold text-blue-400">{date}</span>
                        <span class="text-white font-medium text-sm">{title}</span>
                    </div>
                    <p class="text-xs text-white/60 m-0">{desc}</p>
                </div>
            </div>
            '''
        
        events_html += '</div>'
        
        self.add_section("本周重要事件", events_html, "📅")
    
    def add_next_week_outlook(self, outlook: str = None):
        """添加下周展望"""
        if outlook is None:
            outlook = """
            预计下周市场仍将以震荡为主，关注以下方向值得重点关注：
            1. AI算力产业链：持续高景气，关注业绩兑现情况
            2. 人形机器人：产业催化不断，关注核心标的
            3. 存储芯片：周期反转确立，逢低布局
            4. 注意控制仓位，避免追高，把握结构性机会
            """
        
        content = f'''
        <div class="bg-gradient-to-br from-green-500/15 to-emerald-500/10 border border-green-500/20 rounded-xl p-5">
            <div class="flex items-center gap-2 mb-3">
                <span class="text-xl">🔮</span>
                <span class="text-white font-bold">下周展望</span>
            </div>
            <div class="text-sm text-white/70 leading-relaxed space-y-2">
                {outlook.strip().replace(chr(10), '<br>')}
            </div>
        </div>
        '''
        
        self.add_section("下周展望", content, "🔮")
    
    def add_risk_warning(self):
        """添加风险提示 - 使用卡片组"""
        risks = [
            {'title': '宏观风险', 'content': '宏观经济不及预期可能影响市场整体表现', 'icon': '📉'},
            {'title': '政策风险', 'content': '政策变动可能对相关行业产生重大影响', 'icon': '⚖️'},
            {'title': '海外风险', 'content': '海外市场波动可能传导至A股市场', 'icon': '🌍'},
            {'title': '行业风险', 'content': '行业竞争加剧可能导致盈利能力下降', 'icon': '⚠️'},
        ]
        
        cards_html = self.create_card_group(cards=risks, cols=2, card_style='subtle')
        self.add_section("风险提示", cards_html, "⚠️")
    
    def add_holdings_review(self):
        """添加持仓复盘 - 使用数据网格+卡片组"""
        portfolio = self.portfolio
        stocks = portfolio.get('stocks', [])
        
        if not stocks:
            content_html = '<div class="text-center py-8 text-white/40"><p>暂无持仓数据</p></div>'
            self.add_section("持仓复盘", content_html, "💼")
            return
        
        # 计算统计数据
        total_pnl = 0
        winners = 0
        losers = 0
        
        for stock in stocks:
            pnl_pct = stock.get('weekly_pnl', stock.get('profit_pct', '0%'))
            try:
                pnl_val = float(str(pnl_pct).replace('%', '').replace('+', ''))
            except:
                pnl_val = 0
            
            if pnl_val > 0:
                winners += 1
            elif pnl_val < 0:
                losers += 1
        
        # 使用DataGrid展示汇总数据
        summary_items = [
            {'title': '持仓总数', 'value': str(len(stocks)), 'icon': '📊', 'unit': '只'},
            {'title': '上涨', 'value': str(winners), 'icon': '📈', 'unit': '只', 'desc': '<span class="text-green-400">盈利</span>'},
            {'title': '下跌', 'value': str(losers), 'icon': '📉', 'unit': '只', 'desc': '<span class="text-red-400">亏损</span>'},
        ]
        
        summary_grid = self.create_data_grid(items=summary_items, cols=3)
        
        # 使用卡片组展示个股
        cards = []
        for stock in stocks[:6]:
            name = stock.get('name', '')
            code = stock.get('code', '')
            pnl_pct = stock.get('weekly_pnl', stock.get('profit_pct', '0%'))
            
            try:
                pnl_val = float(str(pnl_pct).replace('%', '').replace('+', ''))
            except:
                pnl_val = 0
            
            if pnl_val > 0:
                pnl_color = 'text-red-400'
                pnl_sign = '+'
            elif pnl_val < 0:
                pnl_color = 'text-green-400'
                pnl_sign = ''
            else:
                pnl_color = 'text-white/60'
                pnl_sign = ''
            
            card_content = f'''
            <div class="flex items-center justify-between">
                <div>
                    <div class="text-white font-medium">{name}</div>
                    <div class="text-white/40 text-xs">{code}</div>
                </div>
                <div class="{pnl_color} font-bold text-lg">{pnl_sign}{pnl_pct}</div>
            </div>
            '''
            cards.append({
                'content': card_content,
            })
        
        stocks_grid = self.create_card_group(cards=cards, cols=3, card_style='glass')
        
        content_html = f'''
        <div class="space-y-6">
            <div>
                <h3 class="text-white font-semibold mb-3 text-sm">持仓概览</h3>
                {summary_grid}
            </div>
            <div>
                <h3 class="text-white font-semibold mb-3 text-sm">个股表现</h3>
                {stocks_grid}
            </div>
        </div>
        '''
        
        self.add_section("持仓复盘", content_html, "💼")
    
    def add_trading_plan(self):
        """添加下周交易计划 - 使用卡片组"""
        plans = [
            {'title': '仓位管理', 'content': '保持中性仓位，根据市场情绪动态调整，建议仓位控制在50%-70%', 'icon': '📊'},
            {'title': '板块配置', 'content': '关注科技成长方向，均衡配置消费和周期，避免单一赛道过度集中', 'icon': '🎯'},
            {'title': '风险控制', 'content': '严格执行止损纪律，单只个股止损线不超过8%，组合最大回撤控制在5%以内', 'icon': '🛡️'},
        ]
        
        plans_html = self.create_card_group(cards=plans, cols=3, card_style='glass')
        self.add_section("下周交易计划", plans_html, "📋")
    
    def build_standard_report(self):
        """构建标准版本的周复盘"""
        self.add_week_summary()
        self.add_market_review()
        self.add_hot_topics_review()
        self.add_important_events()
        self.add_holdings_review()
        self.add_next_week_outlook()
        self.add_trading_plan()
        self.add_risk_warning()
        
        return self


if __name__ == '__main__':
    # 测试生成
    gen = WeeklyReviewProGenerator('2026-06-14', '第24周')
    gen.build_standard_report()
    html = gen.render()
    print(f'Pro版周复盘生成成功，长度: {len(html)} 字符')
    
    # 保存测试
    os.makedirs('../docs/weekly_review', exist_ok=True)
    with open('../docs/weekly_review/20260614_周复盘.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print('已保存到 docs/weekly_review/20260614_周复盘.html')
