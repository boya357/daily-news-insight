"""
S级催化扫描生成器 - Pro版
基于ReportProGenerator基类重构，深色玻璃态风格
深度挖掘S级别重大催化事件，把握超级题材机会
V3.5升级：集成Tab切换、卡片组、数据网格通用组件
V5.0升级（2026-07-03 L1-1/L1-3/L1-5）：
- 所有核心数据标注来源+置信度
- 每个S级题材强制包含"🔴 证伪条件/空方逻辑"模块
- 报告末尾自动匹配历史教训
"""
import sys
import os
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from generators.report_pro_base import ReportProGenerator
from generators.pro_base import CONF_HIGH, CONF_MEDIUM, CONF_LOW, source_tag as _src, unverified as _unv


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
        self.topics = []
    
    def add_scan_summary(self, s_plus_count: int = 1, s_count: int = 3, a_plus_count: int = 2, top_topic: str = "AI算力"):
        """添加扫描总览 - 使用DataGrid展示关键数据"""
        data_items = [
            {'title': 'S+级催化', 'value': str(s_plus_count), 'icon': '🚀', 'unit': '个', 'desc': '<span class="text-red-400">最高等级</span>'},
            {'title': 'S级催化', 'value': str(s_count), 'icon': '⚡', 'unit': '个', 'desc': '<span class="text-orange-400">强烈推荐</span>'},
            {'title': 'A+级催化', 'value': str(a_plus_count), 'icon': '💎', 'unit': '个', 'desc': '<span class="text-yellow-400">值得关注</span>'},
            {'title': '最确定方向', 'value': top_topic, 'icon': '🎯', 'desc': '<span class="text-green-400">综合评分最高</span>'},
        ]
        
        grid_html = self.create_data_grid(items=data_items, cols=4)
        
        content = f'''
        <div class="bg-gradient-to-r from-red-500/25 via-orange-500/20 to-yellow-500/15 border border-red-500/30 rounded-xl p-5 mb-4">
            <div class="flex items-center gap-2 mb-3">
                <span class="text-2xl">🚀</span>
                <span class="text-white font-bold">S级催化扫描总览</span>
                <span class="ml-auto bg-red-500/30 text-red-400 text-xs font-bold px-2 py-0.5 rounded-full border border-red-500/50">
                    S级
                </span>
            </div>
            <p class="text-white/80 leading-relaxed text-sm">
                本期扫描发现 <span class="text-red-400 font-bold">{s_plus_count + s_count + a_plus_count}</span> 个重点催化事件，其中S+级{s_plus_count}个、S级{s_count}个、A+级{a_plus_count}个，
                其中 <span class="text-yellow-400 font-semibold">{top_topic}</span> 方向确定性最高，
                建议重点关注。
                {self.cite(source="综合研究", confidence=CONF_MEDIUM)}
            </p>
        </div>
        {grid_html}
        '''
        self.add_section("扫描总览", content, "🚀")
    
    def add_s_level_topics(self, topics: list = None):
        """添加S级题材深度分析 - 使用Tab切换+卡片组"""
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
        
        self.topics = topics
        
        # 按等级分类
        level_categories = {}
        for topic in topics:
            level = topic.get("level", "S")
            if level not in level_categories:
                level_categories[level] = []
            level_categories[level].append(topic)
        
        # 按等级分类展开显示（不用tab切换，确保100%可见）
        sections_html = ''
        for level in ["S+", "S", "A+"]:
            if level not in level_categories:
                continue
            
            level_topics = level_categories[level]
            cards = []
            
            for i, topic in enumerate(level_topics):
                name = topic.get("name", "")
                score = topic.get("score", 0)
                core_logic = topic.get("core_logic", "")
                catalysts = topic.get("catalysts", [])
                leader_stocks = topic.get("leader_stocks", [])
                mid_stocks = topic.get("mid_stocks", [])
                flexible_stocks = topic.get("flexible_stocks", [])
                time_window = topic.get("time_window", "")
                risk = topic.get("risk", "")
                
                # 催化剂标签
                cat_tags = ' '.join([
                    f'<span class="bg-purple-500/20 text-purple-400 text-xs px-2 py-1 rounded-full border border-purple-500/30">⚡ {c}</span>'
                    for c in catalysts
                ])
                
                # 标的标签
                leader_tags = ' '.join([
                    f'<span class="bg-green-500/20 text-green-400 text-xs px-2 py-1 rounded">{s}</span>'
                    for s in leader_stocks
                ])
                mid_tags = ' '.join([
                    f'<span class="bg-blue-500/20 text-blue-400 text-xs px-2 py-1 rounded">{s}</span>'
                    for s in mid_stocks
                ])
                flex_tags = ' '.join([
                    f'<span class="bg-yellow-500/20 text-yellow-400 text-xs px-2 py-1 rounded">{s}</span>'
                    for s in flexible_stocks
                ])
                
                card_content = f'''
                <div class="flex items-start justify-between mb-3">
                    <div class="flex items-center gap-2">
                        <span class="text-xl font-bold text-white/90">#{i+1}</span>
                        <span class="text-white font-bold">{name}</span>
                    </div>
                    <span class="text-lg font-black text-transparent bg-clip-text bg-gradient-to-r from-orange-500 to-red-500">{score}分</span>
                </div>
                <p class="text-white/70 text-sm leading-relaxed mb-3">
                    {core_logic}
                    {self.cite(source=topic.get('source', '综合研究'), confidence=topic.get('confidence', CONF_MEDIUM), verified=topic.get('verified', False), rumor=topic.get('rumor', False))}
                </p>
                <div class="mb-2">
                    <div class="text-xs text-white/40 mb-1">核心催化剂</div>
                    <div class="flex flex-wrap gap-1.5">{cat_tags}</div>
                </div>
                <div class="space-y-2">
                    <div>
                        <div class="text-xs text-white/40 mb-1">龙头标的</div>
                        <div class="flex flex-wrap gap-1">{leader_tags}</div>
                    </div>
                    <div>
                        <div class="text-xs text-white/40 mb-1">中坚标的</div>
                        <div class="flex flex-wrap gap-1">{mid_tags}</div>
                    </div>
                    <div>
                        <div class="text-xs text-white/40 mb-1">弹性标的</div>
                        <div class="flex flex-wrap gap-1">{flex_tags}</div>
                    </div>
                </div>
                <div class="flex items-center justify-between mt-3 pt-3 border-t border-white/10">
                    <div class="text-xs">
                        <span class="text-white/40">时间窗口：</span>
                        <span class="text-white/70">{time_window}</span>
                    </div>
                    <div class="text-xs">
                        <span class="text-white/40">常规风险：</span>
                        <span class="text-red-400/70">{risk}</span>
                    </div>
                </div>
                {self._risk_section(
                    title=f"🔴 {name} · 证伪条件/空方逻辑",
                    falsify_signals=topic.get('falsify_signals', [
                        f"{name}核心龙头放量跌破20日均线且2日不能收回",
                        f"{name}核心催化（政策/业绩/订单）被官方澄清或证伪",
                        "板块单日跌幅>5%且主力净流出超百亿",
                    ]),
                    stop_loss=topic.get('stop_loss', f"板块龙头买入后回撤超8%无条件止损"),
                    bear_logic=topic.get('bear_logic', [
                        f"{name}已被充分预期，利好兑现即出货（Buy the rumor, sell the news）",
                        "机构/北向资金连续净流出，筹码松动",
                        "大盘系统性风险（如外盘暴跌、流动性收紧）拖累",
                        "题材轮动过快，高标A杀情绪退潮",
                    ]),
                    contrarian_view=topic.get('contrarian_view', ""),
                )}
                '''
                
                cards.append({
                    'content': card_content,
                })
            
            cards_html = self.create_card_group(cards=cards, cols=1, card_style='glass')
            # 等级标题样式
            level_color = {
                'S+': 'from-orange-500 to-red-500',
                'S': 'from-purple-500 to-pink-500',
                'A+': 'from-blue-500 to-cyan-500',
            }.get(level, 'from-gray-500 to-gray-600')
            
            sections_html += f'''
            <div class="mb-6">
                <h3 class="text-lg font-bold mb-3 text-transparent bg-clip-text bg-gradient-to-r {level_color}">
                    {level}级题材
                </h3>
                {cards_html}
            </div>
            '''
        
        # 全部展开显示，不使用tab切换
        self.add_section("S级题材深度分析", sections_html, "💎")
    
    def add_a_plus_catalysts(self, catalysts: list = None):
        """添加A+级催化事件列表"""
        if catalysts is None:
            catalysts = [
                {
                    "name": "新能源汽车销量超预期",
                    "score": 82,
                    "summary": "5月新能源汽车销量同比增长超50%，出口量创新高",
                    "catalysts": ["销量超预期", "出口大增"],
                    "related_stocks": ["比亚迪", "宁德时代", "理想汽车"],
                    "time_window": "1-2个月",
                },
                {
                    "name": "半导体设备国产化加速",
                    "score": 80,
                    "summary": "国产半导体设备中标率持续提升，关键零部件取得突破",
                    "catalysts": ["国产化加速", "订单饱满"],
                    "related_stocks": ["中微公司", "北方华创", "拓荆科技"],
                    "time_window": "3-6个月",
                },
            ]
        
        cards_html = ''
        for i, cat in enumerate(catalysts):
            name = cat.get("name", "")
            score = cat.get("score", 0)
            summary = cat.get("summary", "")
            cat_list = cat.get("catalysts", [])
            stocks = cat.get("related_stocks", [])
            time_window = cat.get("time_window", "")
            
            cat_tags = ' '.join([
                '<span class="bg-yellow-500/20 text-yellow-400 text-xs px-2 py-1 rounded-full border border-yellow-500/30">⚡ ' + c + '</span>'
                for c in cat_list
            ])
            
            stock_tags = ' '.join([
                '<span class="bg-blue-500/20 text-blue-400 text-xs px-2 py-1 rounded">' + s + '</span>'
                for s in stocks
            ])
            
            card_html = '<div class="card-glass rounded-xl p-4">'
            card_html += '<div class="flex items-start justify-between mb-3">'
            card_html += '<div class="flex items-center gap-2">'
            card_html += '<span class="text-yellow-400 font-bold">A+</span>'
            card_html += '<span class="text-white font-bold">' + name + '</span>'
            card_html += '</div>'
            card_html += '<span class="text-sm font-bold text-yellow-400">' + str(score) + '分</span>'
            card_html += '</div>'
            card_html += '<p class="text-white/70 text-sm leading-relaxed mb-3">' + summary + '</p>'
            card_html += '<div class="mb-2">'
            card_html += '<div class="text-xs text-white/40 mb-1">核心催化</div>'
            card_html += '<div class="flex flex-wrap gap-1.5">' + cat_tags + '</div>'
            card_html += '</div>'
            card_html += '<div class="mb-2">'
            card_html += '<div class="text-xs text-white/40 mb-1">相关标的</div>'
            card_html += '<div class="flex flex-wrap gap-1">' + stock_tags + '</div>'
            card_html += '</div>'
            card_html += '<div class="text-xs text-white/40 mt-2">'
            card_html += '时间窗口：<span class="text-white/70">' + time_window + '</span>'
            card_html += '</div>'
            card_html += '</div>'
            
            cards_html += card_html
        
        content_html = '<div class="grid grid-cols-1 md:grid-cols-2 gap-4">' + cards_html + '</div>'
        
        self.add_section("A+级催化事件", content_html, "💎")

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
        """添加风险提示 - 使用卡片组"""
        risks = [
            {'title': '不确定性风险', 'content': 'S级催化事件具有高度不确定性，实际影响可能与预期存在较大差异', 'icon': '⚠️'},
            {'title': '高波动风险', 'content': '题材炒作往往伴随高波动，注意追高风险和情绪退潮风险', 'icon': '📉'},
            {'title': '基本面风险', 'content': '建议结合基本面和技术面综合判断，切勿盲目跟风', 'icon': '📊'},
            {'title': '合规提示', 'content': '本内容仅做信息整理，不构成任何投资建议', 'icon': '📜'},
        ]
        
        cards_html = self.create_card_group(cards=risks, cols=2, card_style='subtle')
        self.add_section("特别风险提示", cards_html, "⚠️")
    
    def add_industry_chain_analysis(self):
        """添加产业链分析 - 全部展开显示"""
        topics = self.topics if hasattr(self, 'topics') and self.topics else []
        if not topics:
            topics = [{'name': 'AI算力', 'logic': '算力需求爆发，产业链上下游受益'}]
        
        # 全部展开，每个题材一个产业链分析块
        sections_html = ''
        for topic in topics[:2]:
            name = topic.get('name', '')
            
            # 产业链环节
            upstream = ['芯片', '光模块', '服务器']
            midstream = ['IDC', '云计算', '运营商']
            downstream = ['AI应用', '互联网', '企业服务']
            
            # 使用卡片组展示各环节
            upstream_cards = [{'content': f'<span class="text-white/80 text-sm">{item}</span>'} for item in upstream]
            midstream_cards = [{'content': f'<span class="text-white/80 text-sm">{item}</span>'} for item in midstream]
            downstream_cards = [{'content': f'<span class="text-white/80 text-sm">{item}</span>'} for item in downstream]
            
            chain_content = f'''
            <div class="space-y-4">
                <div>
                    <div class="text-xs text-white/50 mb-2 flex items-center gap-2">
                        <span class="w-2 h-2 rounded-full bg-blue-500"></span>
                        上游
                    </div>
                    {self.create_card_group(cards=upstream_cards, cols=3, card_style='subtle')}
                </div>
                <div class="text-center text-white/30">↓</div>
                <div>
                    <div class="text-xs text-white/50 mb-2 flex items-center gap-2">
                        <span class="w-2 h-2 rounded-full bg-purple-500"></span>
                        中游
                    </div>
                    {self.create_card_group(cards=midstream_cards, cols=3, card_style='subtle')}
                </div>
                <div class="text-center text-white/30">↓</div>
                <div>
                    <div class="text-xs text-white/50 mb-2 flex items-center gap-2">
                        <span class="w-2 h-2 rounded-full bg-green-500"></span>
                        下游
                    </div>
                    {self.create_card_group(cards=downstream_cards, cols=3, card_style='subtle')}
                </div>
            </div>
            '''
            
            sections_html += f'''
            <div class="mb-8">
                <h4 class="text-base font-semibold text-white/90 mb-4">{name} 产业链</h4>
                {chain_content}
            </div>
            '''
        
        self.add_section("产业链分析", sections_html, "🔗")
    
    def add_investment_strategy(self):
        """添加投资策略 - 使用卡片组"""
        strategies = [
            {
                'title': '进攻策略',
                'content': '聚焦高弹性赛道龙头，把握主升浪行情。适合风险承受能力较高的投资者。',
                'icon': '⚡'
            },
            {
                'title': '稳健策略',
                'content': '配置行业ETF和核心资产，降低波动风险。适合追求稳健收益的投资者。',
                'icon': '🛡️'
            },
            {
                'title': '埋伏策略',
                'content': '提前布局有催化预期的低位板块，等待轮动。适合有耐心的投资者。',
                'icon': '🎯'
            },
        ]
        
        cards_html = self.create_card_group(cards=strategies, cols=3, card_style='glass')
        self.add_section("投资策略建议", cards_html, "📈")
    
    def build_standard_report(self, keywords: list = None):
        """构建标准版本的S级催化扫描（V5.0：自动注入教训回顾+数据来源统计）"""
        self.add_scan_summary()
        self.add_s_level_topics()
        self.add_a_plus_catalysts()
        self.add_catalysts_calendar()
        self.add_industry_chain_analysis()
        self.add_investment_strategy()
        
        # V5.0 L1-5：历史教训自动匹配
        ctx_keywords = keywords or ["S级催化", "题材", "连板", "涨停", "高位股", "情绪退潮"]
        ctx_keywords.extend([t.get("name", "") for t in (self.topics or [])])
        lessons_html = self.build_lessons_section(keywords=ctx_keywords, top_k=3)
        if lessons_html:
            wrap = f'<div class="card-glass p-6 mb-6">{lessons_html}</div>'
            self.add_section("🧠 系统复盘", wrap, "📚")
        
        # V5.0 L1-1：数据来源统计
        src_html = self._source_summary_section()
        if src_html:
            self.add_section("📡 数据溯源", src_html, "📡")
        
        self.add_risk_warning()
        
        return self


if __name__ == '__main__':
    # 测试生成
    gen = SLevelCatalystProGenerator('2026-06-15')
    gen.build_standard_report()
    html = gen.render()
    print(f'Pro版S级催化扫描生成成功，长度: {len(html)} 字符')
    
    # 保存测试
    os.makedirs('../docs/s_level_catalyst', exist_ok=True)
    with open('../docs/s_level_catalyst/20260615_S级催化扫描.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print('已保存到 docs/s_level_catalyst/20260615_S级催化扫描.html')
