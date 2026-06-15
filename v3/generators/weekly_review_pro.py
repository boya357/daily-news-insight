"""
周复盘生成器 - Pro版
基于ReportProGenerator基类重构，深色玻璃态风格
一周市场总结 + 热点回顾 + 下周展望
"""
import sys
import os
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from generators.report_pro_base import ReportProGenerator
from utils.data_loader import get_indices_for_daily


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
        """添加本周市场表现 - Pro版"""
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
        <div class="grid grid-cols-2 md:grid-cols-4 gap-3">
            {cards_html}
        </div>
        '''
        
        self.add_section("本周市场表现", content, "📊")
    
    def add_hot_topics_review(self, topics: list = None):
        """添加本周热点题材回顾"""
        if topics is None:
            topics = [
                {"name": "AI算力", "performance": "+8.5%", "logic": "AI大模型持续迭代，算力需求爆发增长", "stocks": ["英伟达", "寒武纪"]},
                {"name": "人形机器人", "performance": "+6.2%", "logic": "特斯拉Optimus进展超预期，产业链加速落地", "stocks": ["拓普集团", "三花智控"]},
                {"name": "存储芯片", "performance": "+5.8%", "logic": "行业周期反转，价格持续上涨", "stocks": ["兆易创新", "北京君正"]},
                {"name": "先进封装", "performance": "+4.5%", "logic": "Chiplet技术加速渗透，国产替代加速", "stocks": ["长电科技", "通富微电"]},
            ]
        
        topics_html = '<div class="space-y-3">'
        
        for i, topic in enumerate(topics):
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
            
            topics_html += f'''
            <div class="bg-white/5 backdrop-blur-sm rounded-xl p-4 border border-white/10">
                <div class="flex items-center gap-3 mb-2">
                    <div class="w-7 h-7 bg-gradient-to-br from-blue-500 to-purple-500 rounded-full flex items-center justify-center flex-shrink-0">
                        <span class="text-white text-xs font-bold">{i+1}</span>
                    </div>
                    <div class="flex-1">
                        <span class="text-white font-semibold text-sm">{name}</span>
                    </div>
                    <span class="text-xs font-bold {perf_color} bg-white/10 px-2.5 py-1 rounded-full">
                        {performance}
                    </span>
                </div>
                <div class="text-sm text-white/60 leading-relaxed pl-10">
                    {logic}
                </div>
                {stocks_html}
            </div>
            '''
        
        topics_html += '</div>'
        
        self.add_section("本周热点题材回顾", topics_html, "🔥")
    
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
            <div class="relative pb-5 {"pb-0" if is_last else ""}>
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
        """添加风险提示"""
        content = '''
        <div class="bg-gradient-to-r from-red-500/15 to-orange-500/10 border border-red-500/20 rounded-xl p-5">
            <div class="flex items-center gap-2 mb-3">
                <span class="text-xl">⚠️</span>
                <span class="text-white font-bold">风险提示</span>
            </div>
            <ul class="text-sm text-white/70 leading-relaxed space-y-2 m-0 pl-4">
                <li>宏观经济不及预期风险</li>
                <li>政策变动风险</li>
                <li>海外市场波动风险</li>
                <li>行业竞争加剧风险</li>
            </ul>
        </div>
        '''
        
        self.add_section("风险提示", content, "⚠️")
    
    def build_standard_report(self):
        """构建标准版本的周复盘"""
        self.add_week_summary()
        self.add_market_review()
        self.add_hot_topics_review()
        self.add_important_events()
        self.add_next_week_outlook()
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
