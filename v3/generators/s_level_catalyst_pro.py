"""
S级催化扫描生成器 - Pro版
基于ReportProGenerator基类重构，深色玻璃态风格
深度挖掘S级别重大催化事件，把握超级题材机会
"""
import sys
import os
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from generators.report_pro_base import ReportProGenerator


class SLevelCatalystProGenerator(ReportProGenerator):
    """S级催化扫描生成器 - Pro版"""
    
    def __init__(self, date_str: str = None, subtitle: str = None, data_dir: str = "data"):
        date = date_str or datetime.now().strftime('%Y-%m-%d')
        sub = subtitle or f"{date} · S级催化深度扫描"
        
        super().__init__(
            title="S级催化扫描",
            report_type="s_level_catalyst",
            subtitle=sub,
            date_str=date,
            data_dir=data_dir,
        )
        
        self.active_page = "S级催化"
    
    def add_scan_summary(self, count: int = 3, top_topic: str = "AI算力"):
        """添加扫描总览"""
        content = f'''
        <div class="bg-gradient-to-r from-red-500/25 via-orange-500/20 to-yellow-500/15 border border-red-500/30 rounded-xl p-5">
            <div class="flex items-center gap-2 mb-3">
                <span class="text-2xl">🚀</span>
                <span class="text-white font-bold">S级催化扫描总览</span>
                <span class="ml-auto bg-red-500/30 text-red-400 text-xs font-bold px-2 py-0.5 rounded-full border border-red-500/50">
                    S级
                </span>
            </div>
            <p class="text-white/80 leading-relaxed text-sm">
                本期扫描发现 <span class="text-red-400 font-bold">{count}</span> 个S级催化事件，
                其中 <span class="text-yellow-400 font-semibold">{top_topic}</span> 方向确定性最高，
                建议重点关注。
            </p>
        </div>
        '''
        self.add_section("扫描总览", content, "🚀")
    
    def add_s_level_topics(self, topics: list = None):
        """添加S级题材深度分析"""
        if topics is None:
            topics = [
                {
                    "name": "AI算力革命",
                    "level": "S+",
                    "score": 95,
                    "core_logic": "AI大模型持续迭代，算力需求呈指数级增长。GPU供应紧张，算力租赁价格持续上涨，产业链上下游全面受益。",
                    "catalysts": ["GPT-5发布预期", "算力需求爆发", "国产GPU突破"],
                    "leader_stocks": ["英伟达", "寒武纪", "海光信息"],
                    "mid_stocks": ["浪潮信息", "紫光股份"],
                    "flexible_stocks": ["中贝通信", "鸿博股份"],
                    "time_window": "6-12个月",
                    "risk": "技术迭代不及预期",
                },
                {
                    "name": "人形机器人产业化",
                    "level": "S",
                    "score": 88,
                    "core_logic": "特斯拉Optimus量产临近，国内厂商加速跟进。核心零部件国产化空间巨大，产业链迎来爆发期。",
                    "catalysts": ["特斯拉Optimus量产", "国内厂商跟进", "成本下降超预期"],
                    "leader_stocks": ["拓普集团", "三花智控"],
                    "mid_stocks": ["绿的谐波", "双环传动"],
                    "flexible_stocks": ["丰立智能", "步科股份"],
                    "time_window": "3-6个月",
                    "risk": "量产进度不及预期",
                },
                {
                    "name": "存储周期反转",
                    "level": "S",
                    "score": 85,
                    "core_logic": "存储行业周期见底回升，DRAM和NAND价格持续上涨。AI服务器需求爆发，HMB供不应求，国产替代加速。",
                    "catalysts": ["价格持续上涨", "AI需求爆发", "国产替代加速"],
                    "leader_stocks": ["兆易创新", "北京君正"],
                    "mid_stocks": ["长鑫存储", "长江存储"],
                    "flexible_stocks": ["万润科技", "德明利"],
                    "time_window": "6-12个月",
                    "risk": "需求复苏不及预期",
                },
            ]
        
        topics_html = '<div class="space-y-5">'
        
        for i, topic in enumerate(topics):
            name = topic.get("name", "")
            level = topic.get("level", "S")
            score = topic.get("score", 0)
            core_logic = topic.get("core_logic", "")
            catalysts = topic.get("catalysts", [])
            leader_stocks = topic.get("leader_stocks", [])
            mid_stocks = topic.get("mid_stocks", [])
            flexible_stocks = topic.get("flexible_stocks", [])
            time_window = topic.get("time_window", "")
            risk = topic.get("risk", "")
            
            # 等级样式
            level_colors = {
                "S+": ("from-red-500 to-orange-500", "S+级"),
                "S": ("from-orange-500 to-yellow-500", "S级"),
                "A+": ("from-yellow-500 to-green-500", "A+级"),
            }
            gradient, level_text = level_colors.get(level, level_colors["S"])
            
            # 催化剂标签
            cat_tags = ' '.join([
                f'<span class="bg-purple-500/20 text-purple-400 text-xs px-2 py-1 rounded-full border border-purple-500/30">⚡ {c}</span>'
                for c in catalysts
            ])
            
            # 标的标签
            def stock_tags(stocks, label, color):
                if not stocks:
                    return ''
                tags = ' '.join([
                    f'<span class="bg-{color}-500/20 text-{color}-400 text-xs px-2 py-1 rounded">{s}</span>'
                    for s in stocks
                ])
                return f'''
                <div>
                    <div class="text-xs text-white/40 mb-1">{label}</div>
                    <div class="flex flex-wrap gap-1.5">{tags}</div>
                </div>
                '''
            
            topics_html += f'''
            <div class="bg-gradient-to-br from-white/5 to-white/0 rounded-xl p-5 border border-white/10">
                <!-- 头部 -->
                <div class="flex items-start justify-between mb-4">
                    <div class="flex items-center gap-3">
                        <div class="w-10 h-10 bg-gradient-to-br {gradient} rounded-xl flex items-center justify-center">
                            <span class="text-white font-black text-lg">{i+1}</span>
                        </div>
                        <div>
                            <div class="text-white font-bold text-lg">{name}</div>
                            <div class="flex items-center gap-2 mt-1">
                                <span class="bg-gradient-to-r {gradient} text-white text-xs font-bold px-2 py-0.5 rounded-full">
                                    {level_text}
                                </span>
                                <span class="text-white/40 text-xs">综合评分 {score}分</span>
                            </div>
                        </div>
                    </div>
                    <div class="text-right">
                        <div class="text-2xl font-black text-transparent bg-clip-text bg-gradient-to-r {gradient}">
                            {score}
                        </div>
                        <div class="text-xs text-white/40">确定性评分</div>
                    </div>
                </div>
                
                <!-- 核心逻辑 -->
                <div class="mb-4">
                    <div class="text-white/60 text-xs mb-2">核心逻辑</div>
                    <p class="text-white/80 text-sm leading-relaxed m-0">{core_logic}</p>
                </div>
                
                <!-- 催化剂 -->
                <div class="mb-4">
                    <div class="text-white/60 text-xs mb-2">核心催化剂</div>
                    <div class="flex flex-wrap gap-2">{cat_tags}</div>
                </div>
                
                <!-- 投资标的 -->
                <div class="space-y-3 mb-4">
                    {stock_tags(leader_stocks, "龙头标的", "green")}
                    {stock_tags(mid_stocks, "中坚标的", "blue")}
                    {stock_tags(flexible_stocks, "弹性标的", "yellow")}
                </div>
                
                <!-- 底部信息 -->
                <div class="flex items-center justify-between pt-3 border-t border-white/10">
                    <div class="text-xs">
                        <span class="text-white/40">时间窗口：</span>
                        <span class="text-white/70">{time_window}</span>
                    </div>
                    <div class="text-xs">
                        <span class="text-white/40">主要风险：</span>
                        <span class="text-red-400/70">{risk}</span>
                    </div>
                </div>
            </div>
            '''
        
        topics_html += '</div>'
        
        self.add_section("S级题材深度分析", topics_html, "💎")
    
    def add_catalysts_calendar(self, events: list = None):
        """添加S级催化日历"""
        if events is None:
            events = [
                {"date": "6月15日", "event": "AI开发者大会", "topic": "AI算力", "impact": "重大"},
                {"date": "6月20日", "event": "机器人行业峰会", "topic": "人形机器人", "impact": "重大"},
                {"date": "6月25日", "event": "存储产业论坛", "topic": "存储芯片", "impact": "重要"},
                {"date": "6月30日", "event": "新能源车销量数据", "topic": "新能源", "impact": "重要"},
                {"date": "7月5日", "event": "半年度经济数据", "topic": "宏观经济", "impact": "重大"},
            ]
        
        calendar_html = '<div class="space-y-2">'
        
        for event in events:
            impact_colors = {
                "重大": ("bg-red-500/20", "text-red-400", "border-red-500/30"),
                "重要": ("bg-yellow-500/20", "text-yellow-400", "border-yellow-500/30"),
                "一般": ("bg-blue-500/20", "text-blue-400", "border-blue-500/30"),
            }
            bg, text, border = impact_colors.get(event.get("impact", "重要"), impact_colors["重要"])
            
            calendar_html += f'''
            <div class="flex items-center gap-4 bg-white/5 rounded-lg px-4 py-3 border {border}/30">
                <div class="w-16 text-center flex-shrink-0">
                    <div class="text-white font-bold text-sm">{event.get("date", "")}</div>
                </div>
                <div class="w-px h-8 bg-white/10"></div>
                <div class="flex-1">
                    <div class="text-white/90 text-sm font-medium">{event.get("event", "")}</div>
                    <div class="text-xs text-white/40 mt-0.5">{event.get("topic", "")}</div>
                </div>
                <span class="{bg} {text} text-xs font-medium px-2 py-1 rounded-full">
                    {event.get("impact", "")}
                </span>
            </div>
            '''
        
        calendar_html += '</div>'
        
        self.add_section("S级催化日历", calendar_html, "📅")
    
    def add_risk_warning(self):
        """添加风险提示"""
        content = '''
        <div class="bg-gradient-to-r from-red-500/15 to-orange-500/10 border border-red-500/20 rounded-xl p-5">
            <div class="flex items-center gap-2 mb-3">
                <span class="text-xl">⚠️</span>
                <span class="text-white font-bold">特别风险提示</span>
            </div>
            <div class="text-sm text-white/60 leading-relaxed space-y-2">
                <p>1. S级催化事件具有高度不确定性，实际影响可能与预期存在较大差异</p>
                <p>2. 题材炒作往往伴随高波动，注意追高风险和情绪退潮风险</p>
                <p>3. 建议结合基本面和技术面综合判断，切勿盲目跟风</p>
                <p>4. 本内容仅做信息整理，不构成任何投资建议</p>
            </div>
        </div>
        '''
        
        self.add_section("特别风险提示", content, "⚠️")
    

    def add_industry_chain_analysis(self):
        """添加产业链分析 - Pro版"""
        # 基于S级题材生成产业链分析
        topics = self.topics if hasattr(self, 'topics') and self.topics else []
        if not topics:
            topics = [{'name': 'AI算力', 'logic': '算力需求爆发，产业链上下游受益'}]
        
        chains_html = ''
        for topic in topics[:2]:
            name = topic.get('name', '')
            
            # 模拟产业链环节
            upstream = ['芯片', '光模块', '服务器']
            midstream = ['IDC', '云计算', '运营商']
            downstream = ['AI应用', '互联网', '企业服务']
            
            chain_html = '<div class="bg-white/5 rounded-xl p-4 mb-4">'
            chain_html += '<div class="text-white font-semibold mb-3 flex items-center gap-2"><span>🔗</span>' + name + ' 产业链</div>'
            
            # 上游
            chain_html += '<div class="mb-3">'
            chain_html += '<div class="text-xs text-white/50 mb-2">上游</div>'
            chain_html += '<div class="flex flex-wrap gap-2">'
            for item in upstream:
                chain_html += '<span class="bg-blue-500/20 text-blue-300 px-3 py-1 rounded-full text-xs">' + item + '</span>'
            chain_html += '</div></div>'
            
            # 中游
            chain_html += '<div class="mb-3">'
            chain_html += '<div class="text-xs text-white/50 mb-2">中游</div>'
            chain_html += '<div class="flex flex-wrap gap-2">'
            for item in midstream:
                chain_html += '<span class="bg-purple-500/20 text-purple-300 px-3 py-1 rounded-full text-xs">' + item + '</span>'
            chain_html += '</div></div>'
            
            # 下游
            chain_html += '<div>'
            chain_html += '<div class="text-xs text-white/50 mb-2">下游</div>'
            chain_html += '<div class="flex flex-wrap gap-2">'
            for item in downstream:
                chain_html += '<span class="bg-green-500/20 text-green-300 px-3 py-1 rounded-full text-xs">' + item + '</span>'
            chain_html += '</div></div>'
            
            chain_html += '</div>'
            chains_html += chain_html
        
        content_html = chains_html
        
        self.add_section("产业链分析", content_html, "🔗")
    
    def add_investment_strategy(self):
        """添加投资策略 - Pro版"""
        strategies = [
            {
                'title': '进攻策略',
                'icon': '⚡',
                'desc': '聚焦高弹性赛道龙头，把握主升浪行情',
                'stocks': ['光模块龙头', 'AI芯片龙头', '算力租赁龙头'],
                'color': 'from-red-500/20 to-orange-500/10 border-red-500/30'
            },
            {
                'title': '稳健策略',
                'icon': '🛡️',
                'desc': '配置行业ETF和核心资产，降低波动风险',
                'stocks': ['科创50ETF', '半导体ETF', '沪深300ETF'],
                'color': 'from-blue-500/20 to-cyan-500/10 border-blue-500/30'
            },
            {
                'title': '埋伏策略',
                'icon': '🎯',
                'desc': '提前布局有催化预期的低位板块，等待轮动',
                'stocks': ['人形机器人', '储能', '创新药'],
                'color': 'from-green-500/20 to-emerald-500/10 border-green-500/30'
            },
        ]
        
        strats_html = ''
        for strat in strategies:
            card = '<div class="bg-gradient-to-br ' + strat['color'] + ' border rounded-xl p-4">'
            card += '<div class="flex items-center gap-2 mb-3">'
            card += '<span class="text-2xl">' + strat['icon'] + '</span>'
            card += '<span class="text-white font-bold">' + strat['title'] + '</span>'
            card += '</div>'
            card += '<p class="text-white/60 text-sm mb-3">' + strat['desc'] + '</p>'
            card += '<div class="flex flex-wrap gap-1">'
            for stock in strat['stocks']:
                card += '<span class="bg-white/10 text-white/70 px-2 py-0.5 rounded text-xs">' + stock + '</span>'
            card += '</div></div>'
            strats_html += card
        
        content_html = '<div class="grid grid-cols-1 md:grid-cols-3 gap-4">' + strats_html + '</div>'
        
        self.add_section("投资策略建议", content_html, "📈")


    def build_standard_report(self):
        """构建标准版本的S级催化扫描"""
        self.add_scan_summary()
        self.add_s_level_topics()
        self.add_catalysts_calendar()
        self.add_risk_warning()
        
        return self


if __name__ == '__main__':
    # 测试生成
    gen = SLevelCatalystProGenerator('2026-06-15')
    gen.build_standard_report()
    html = gen.render()
    print(f'Pro版S级催化扫描生成成功，长度: {len(html)} 字符')
    
    # 保存测试
    os.makedirs('../docs/s级催化扫描', exist_ok=True)
    with open('../docs/s级催化扫描/20260615_S级催化扫描.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print('已保存到 docs/s级催化扫描/20260615_S级催化扫描.html')
