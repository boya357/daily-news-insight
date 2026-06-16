"""
周末速递生成器 - Pro版
基于ReportProGenerator基类重构，深色玻璃态风格
周末资讯汇总 + 下周前瞻 + 投资日历
V3.5升级：集成Tab切换、卡片组、数据网格通用组件
"""
import sys
import os
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from generators.report_pro_base import ReportProGenerator


class WeekendExpressProGenerator(ReportProGenerator):
    """周末速递生成器 - Pro版"""
    
    def __init__(self, date_str: str = None, subtitle: str = None, data_dir: str = "data"):
        date = date_str or datetime.now().strftime('%Y-%m-%d')
        sub = subtitle or f"{date} · 周末资讯速递"
        
        super().__init__(
            title="周末速递",
            report_type="weekend_express",
            subtitle=sub,
            date_str=date,
            data_dir=data_dir,
        )
        
        self.active_page = "周末"
    
    def add_weekend_summary(self, summary: str = None):
        """添加周末资讯总览 - 使用DataGrid展示关键数据"""
        if summary is None:
            summary = """
            本周末重要资讯汇总，涵盖政策、行业、公司等多个维度，
            帮助您快速把握周末重要信息，为下周投资决策提供参考。
            """
        
        data_items = [
            {'title': '政策要闻', 'value': '5', 'icon': '🏛️', 'unit': '条'},
            {'title': '行业动态', 'value': '8', 'icon': '🏭', 'unit': '条'},
            {'title': '公司公告', 'value': '12', 'icon': '🏢', 'unit': '条'},
            {'title': '下周事件', 'value': '6', 'icon': '📅', 'unit': '个'},
        ]
        
        grid_html = self.create_data_grid(items=data_items, cols=4)
        
        content = f'''
        <div class="bg-gradient-to-r from-purple-500/20 to-pink-500/15 border border-purple-500/30 rounded-xl p-5 mb-4">
            <div class="flex items-center gap-2 mb-3">
                <span class="text-2xl">📰</span>
                <span class="text-white font-bold">周末资讯总览</span>
            </div>
            <p class="text-white/80 leading-relaxed text-sm">
                {summary.strip()}
            </p>
        </div>
        {grid_html}
        '''
        self.add_section("周末资讯总览", content, "📰")
    
    def add_policy_news(self, news: list = None):
        """添加政策要闻 - 使用Tab切换分类"""
        if news is None:
            news = [
                {"title": "重大政策发布", "desc": "相关部门发布重要政策文件，支持实体经济发展。", "level": "重要"},
                {"title": "行业监管动态", "desc": "监管部门发布新的行业监管指引，规范市场秩序。", "level": "一般"},
                {"title": "地方政策支持", "desc": "多地出台支持政策，推动当地产业升级和经济发展。", "level": "关注"},
                {"title": "货币政策动态", "desc": "央行发布最新货币政策执行报告，释放重要信号。", "level": "重要"},
            ]
        
        # 按等级分类
        categories = {}
        for item in news:
            level = item.get("level", "一般")
            if level not in categories:
                categories[level] = []
            categories[level].append(item)
        
        # 生成Tab内容
        tabs = []
        for level in ["重要", "关注", "一般"]:
            if level not in categories:
                continue
            
            items = categories[level]
            cards = []
            for item in items:
                card_content = f'''
                <div class="flex items-start gap-3">
                    <div class="w-1.5 h-1.5 rounded-full bg-red-400 mt-2 flex-shrink-0"></div>
                    <div class="flex-1">
                        <div class="text-white font-semibold text-sm mb-1">{item.get("title", "")}</div>
                        <div class="text-white/60 text-xs leading-relaxed">{item.get("desc", "")}</div>
                    </div>
                </div>
                '''
                cards.append({
                    'content': card_content,
                })
            
            cards_html = self.create_card_group(cards=cards, cols=1, card_style='subtle')
            tabs.append({
                'label': level,
                'content': cards_html
            })
        
        tab_content = self.create_tab_pane(tabs=tabs, tab_id="policy-news", style="default")
        self.add_section("政策要闻", tab_content, "🏛️")
    
    def add_industry_news(self, news: list = None):
        """添加行业动态 - 使用Tab切换行业分类"""
        if news is None:
            news = [
                {"industry": "科技", "title": "AI技术新突破", "desc": "AI大模型技术取得新进展，多家公司发布新产品。"},
                {"industry": "科技", "title": "芯片产能扩张", "desc": "国内芯片厂商加速产能扩张，国产替代进程加快。"},
                {"industry": "新能源", "title": "新能源车销量增长", "desc": "新能源车销量持续增长，渗透率不断提升。"},
                {"industry": "医药", "title": "创新药研发进展", "desc": "多款创新药临床试验取得积极结果。"},
            ]
        
        # 按行业分类
        categories = {}
        for item in news:
            industry = item.get("industry", "其他")
            if industry not in categories:
                categories[industry] = []
            categories[industry].append(item)
        
        # 生成Tab内容
        tabs = []
        for industry, items in categories.items():
            cards = []
            for item in items:
                card_content = f'''
                <div class="flex items-start gap-3">
                    <div class="w-1.5 h-1.5 rounded-full bg-green-400 mt-2 flex-shrink-0"></div>
                    <div class="flex-1">
                        <div class="text-white font-semibold text-sm mb-1">{item.get("title", "")}</div>
                        <div class="text-white/60 text-xs leading-relaxed">{item.get("desc", "")}</div>
                    </div>
                </div>
                '''
                cards.append({
                    'content': card_content,
                })
            
            cards_html = self.create_card_group(cards=cards, cols=1, card_style='subtle')
            tabs.append({
                'label': industry,
                'content': cards_html
            })
        
        tab_content = self.create_tab_pane(tabs=tabs, tab_id="industry-news", style="underline")
        self.add_section("行业动态", tab_content, "🏭")
    
    def add_company_news(self, news: list = None):
        """添加公司重要公告 - 使用卡片组"""
        if news is None:
            news = [
                {"name": "某上市公司", "type": "业绩预告", "desc": "发布半年度业绩预告，净利润同比大幅增长。"},
                {"name": "某科技公司", "type": "重大合同", "desc": "签署重大合作协议，金额占上年营收比例较高。"},
                {"name": "某医药公司", "type": "研发进展", "desc": "新药临床试验取得积极进展，即将进入下一阶段。"},
                {"name": "某新能源公司", "type": "产能扩张", "desc": "宣布投资建设新产能，预计明年投产。"},
            ]
        
        cards = []
        for item in news:
            card_content = f'''
            <div class="flex items-center justify-between mb-2">
                <span class="text-white font-semibold text-sm">{item.get("name", "")}</span>
                <span class="text-xs text-blue-400 bg-blue-500/20 px-2 py-0.5 rounded">
                    {item.get("type", "")}
                </span>
            </div>
            <p class="text-white/60 text-xs m-0">{item.get("desc", "")}</p>
            '''
            cards.append({
                'content': card_content,
            })
        
        cards_html = self.create_card_group(cards=cards, cols=2, card_style='glass')
        self.add_section("公司重要公告", cards_html, "🏢")
    
    def add_next_week_calendar(self, events: list = None):
        """添加下周投资日历 - 时间线风格"""
        if events is None:
            events = [
                {"date": "周一", "event": "重要经济数据公布", "impact": "中"},
                {"date": "周二", "event": "行业大会召开", "impact": "高"},
                {"date": "周三", "event": "美联储议息会议", "impact": "高"},
                {"date": "周四", "event": "新股申购", "impact": "低"},
                {"date": "周五", "event": "股指期货交割", "impact": "中"},
            ]
        
        calendar_html = '<div class="space-y-2">'
        
        for event in events:
            impact_colors = {
                "高": ("bg-red-500/20", "text-red-400"),
                "中": ("bg-yellow-500/20", "text-yellow-400"),
                "低": ("bg-green-500/20", "text-green-400"),
            }
            bg, text = impact_colors.get(event.get("impact", "中"), impact_colors["中"])
            
            calendar_html += f'''
            <div class="flex items-center gap-4 bg-white/5 rounded-lg px-4 py-3">
                <div class="w-12 text-center flex-shrink-0">
                    <div class="text-white font-bold text-sm">{event.get("date", "")}</div>
                </div>
                <div class="flex-1">
                    <div class="text-white/80 text-sm">{event.get("event", "")}</div>
                </div>
                <span class="{bg} {text} text-xs font-medium px-2 py-0.5 rounded-full flex-shrink-0">
                    {event.get("impact", "")}影响
                </span>
            </div>
            '''
        
        calendar_html += '</div>'
        
        self.add_section("下周投资日历", calendar_html, "📅")
    
    def add_next_week_topics(self):
        """添加下周重点题材 - 使用数据网格+热度条"""
        topics = [
            {'name': 'AI算力', 'catalyst': '算力需求持续高增', 'hot': 95},
            {'name': '存储芯片', 'catalyst': '价格周期反转确认', 'hot': 88},
            {'name': '人形机器人', 'catalyst': '产业政策利好预期', 'hot': 82},
            {'name': '先进封装', 'catalyst': '技术突破+产能扩张', 'hot': 78},
        ]
        
        cards = []
        for topic in topics:
            hot_bar = min(100, topic['hot'])
            
            card_content = f'''
            <div class="flex items-center justify-between mb-2">
                <span class="text-white font-semibold">{topic['name']}</span>
                <span class="text-orange-400 text-sm font-bold">{topic['hot']}°</span>
            </div>
            <div class="text-white/50 text-xs mb-2">{topic['catalyst']}</div>
            <div class="w-full h-1.5 bg-white/10 rounded-full overflow-hidden">
                <div class="h-full bg-gradient-to-r from-orange-500 to-red-500 rounded-full" style="width: {hot_bar}%"></div>
            </div>
            '''
            cards.append({
                'content': card_content,
            })
        
        cards_html = self.create_card_group(cards=cards, cols=2, card_style='glass')
        self.add_section("下周重点题材", cards_html, "🔥")
    
    def add_trading_plan_weekend(self):
        """添加下周交易计划 - 使用卡片组"""
        plans = [
            {'title': '仓位控制', 'content': '建议仓位60%-70%，预留部分现金应对波动', 'icon': '📊'},
            {'title': '方向选择', 'content': '重点关注科技成长方向，逢低布局核心资产', 'icon': '🎯'},
            {'title': '节奏把握', 'content': '避免追高，回调时分批介入，做好高低切换', 'icon': '⚡'},
            {'title': '风控原则', 'content': '单票仓位不超20%，止损线设置在8%-10%', 'icon': '🛡️'},
        ]
        
        cards_html = self.create_card_group(cards=plans, cols=2, card_style='glass')
        self.add_section("下周交易计划", cards_html, "📋")
    
    def build_standard_report(self):
        """构建标准版本的周末速递"""
        self.add_weekend_summary()
        self.add_policy_news()
        self.add_industry_news()
        self.add_company_news()
        self.add_next_week_topics()
        self.add_next_week_calendar()
        self.add_trading_plan_weekend()
        
        return self


if __name__ == '__main__':
    # 测试生成
    gen = WeekendExpressProGenerator('2026-06-14', '周末资讯速递')
    gen.build_standard_report()
    html = gen.render()
    print(f'Pro版周末速递生成成功，长度: {len(html)} 字符')
    
    # 保存测试
    os.makedirs('../docs/weekend_express', exist_ok=True)
    with open('../docs/weekend_express/20260614_周末速递.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print('已保存到 docs/weekend_express/20260614_周末速递.html')
