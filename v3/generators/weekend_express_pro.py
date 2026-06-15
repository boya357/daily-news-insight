"""
周末速递生成器 - Pro版
基于ReportProGenerator基类重构，深色玻璃态风格
周末资讯汇总 + 下周前瞻 + 投资日历
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
        """添加周末资讯总览"""
        if summary is None:
            summary = """
            本周末重要资讯汇总，涵盖政策、行业、公司等多个维度，
            帮助您快速把握周末重要信息，为下周投资决策提供参考。
            """
        
        content = f'''
        <div class="bg-gradient-to-r from-purple-500/20 to-pink-500/15 border border-purple-500/30 rounded-xl p-5">
            <div class="flex items-center gap-2 mb-3">
                <span class="text-2xl">📰</span>
                <span class="text-white font-bold">周末资讯总览</span>
            </div>
            <p class="text-white/80 leading-relaxed text-sm">
                {summary.strip()}
            </p>
        </div>
        '''
        self.add_section("周末资讯总览", content, "📰")
    
    def add_policy_news(self, news: list = None):
        """添加政策要闻"""
        if news is None:
            news = [
                {"title": "重大政策发布", "desc": "相关部门发布重要政策文件，支持实体经济发展。", "level": "重要"},
                {"title": "行业监管动态", "desc": "监管部门发布新的行业监管指引，规范市场秩序。", "level": "一般"},
                {"title": "地方政策支持", "desc": "多地出台支持政策，推动当地产业升级和经济发展。", "level": "关注"},
            ]
        
        news_html = '<div class="space-y-3">'
        
        for item in news:
            level_colors = {
                "重要": ("bg-red-500/20", "text-red-400", "border-red-500/30"),
                "关注": ("bg-yellow-500/20", "text-yellow-400", "border-yellow-500/30"),
                "一般": ("bg-blue-500/20", "text-blue-400", "border-blue-500/30"),
            }
            bg, text, border = level_colors.get(item.get("level", "一般"), level_colors["一般"])
            
            news_html += f'''
            <div class="bg-white/5 rounded-xl p-4 border border-white/10">
                <div class="flex items-start gap-3">
                    <span class="{bg} {text} text-xs font-bold px-2 py-0.5 rounded-full border {border} flex-shrink-0 mt-0.5">
                        {item.get("level", "")}
                    </span>
                    <div class="flex-1">
                        <div class="text-white font-semibold text-sm mb-1">{item.get("title", "")}</div>
                        <div class="text-white/60 text-xs leading-relaxed">{item.get("desc", "")}</div>
                    </div>
                </div>
            </div>
            '''
        
        news_html += '</div>'
        
        self.add_section("政策要闻", news_html, "🏛️")
    
    def add_industry_news(self, news: list = None):
        """添加行业动态"""
        if news is None:
            news = [
                {"industry": "科技", "title": "AI技术新突破", "desc": "AI大模型技术取得新进展，多家公司发布新产品。"},
                {"industry": "新能源", "title": "新能源车销量增长", "desc": "新能源车销量持续增长，渗透率不断提升。"},
                {"industry": "医药", "title": "创新药研发进展", "desc": "多款创新药临床试验取得积极结果。"},
            ]
        
        news_html = '<div class="space-y-3">'
        
        for item in news:
            industry = item.get("industry", "")
            
            news_html += f'''
            <div class="bg-white/5 rounded-xl p-4 border border-white/10">
                <div class="flex items-start gap-3">
                    <div class="w-1.5 h-1.5 rounded-full bg-green-400 mt-2 flex-shrink-0"></div>
                    <div class="flex-1">
                        <div class="flex items-center gap-2 mb-1">
                            <span class="text-xs font-semibold text-green-400 bg-green-500/20 px-2 py-0.5 rounded">
                                {industry}
                            </span>
                            <span class="text-white font-medium text-sm">{item.get("title", "")}</span>
                        </div>
                        <div class="text-white/60 text-xs leading-relaxed">{item.get("desc", "")}</div>
                    </div>
                </div>
            </div>
            '''
        
        news_html += '</div>'
        
        self.add_section("行业动态", news_html, "🏭")
    
    def add_company_news(self, news: list = None):
        """添加公司重要公告"""
        if news is None:
            news = [
                {"name": "某上市公司", "type": "业绩预告", "desc": "发布半年度业绩预告，净利润同比大幅增长。"},
                {"name": "某科技公司", "type": "重大合同", "desc": "签署重大合作协议，金额占上年营收比例较高。"},
                {"name": "某医药公司", "type": "研发进展", "desc": "新药临床试验取得积极进展，即将进入下一阶段。"},
            ]
        
        news_html = '<div class="space-y-3">'
        
        for item in news:
            news_html += f'''
            <div class="bg-white/5 rounded-xl p-4 border border-white/10">
                <div class="flex items-center justify-between mb-2">
                    <span class="text-white font-semibold text-sm">{item.get("name", "")}</span>
                    <span class="text-xs text-blue-400 bg-blue-500/20 px-2 py-0.5 rounded">
                        {item.get("type", "")}
                    </span>
                </div>
                <p class="text-white/60 text-xs m-0">{item.get("desc", "")}</p>
            </div>
            '''
        
        news_html += '</div>'
        
        self.add_section("公司重要公告", news_html, "🏢")
    
    def add_next_week_calendar(self, events: list = None):
        """添加下周投资日历"""
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
    
    def build_standard_report(self):
        """构建标准版本的周末速递"""
        self.add_weekend_summary()
        self.add_policy_news()
        self.add_industry_news()
        self.add_company_news()
        self.add_next_week_calendar()
        
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
