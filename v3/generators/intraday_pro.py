"""
盘中快报生成器 - Pro版
基于ReportProGenerator基类重构，深色玻璃态风格
午间市场数据 + 热点解析 + 操作策略
"""
import sys
import os
import json
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from generators.report_pro_base import ReportProGenerator
from utils.data_loader import get_indices_for_daily, load_portfolio, get_hot_sectors


class IntradayProGenerator(ReportProGenerator):
    """盘中快报生成器 - Pro版"""
    
    def __init__(self, date_str: str = None, subtitle: str = None, data_dir: str = "data"):
        date = date_str or datetime.now().strftime('%Y-%m-%d')
        sub = subtitle or f"{date} · 午盘速递"
        
        super().__init__(
            title="盘中快报",
            report_type="intraday",
            subtitle=sub,
            date_str=date,
            data_dir=data_dir,
        )
        
        self.active_page = "盘中"
        self._load_data()
    
    def _load_data(self):
        """加载数据"""
        from utils.data_loader import get_market_summary
        
        self.indices = get_indices_for_daily()
        self.portfolio = load_portfolio()
        self.hot_sectors = get_hot_sectors()
        self.market_data = get_market_summary()
    
    def _generate_sector_reason(self, sector_name: str) -> str:
        """根据板块名称生成上涨原因描述"""
        reasons = {
            '半导体': 'AI算力需求持续爆发，芯片产业链景气度上行，国产替代加速推进，相关公司业绩有望超预期。',
            '集成电路': 'AI芯片需求旺盛，存储芯片价格触底回升，国产替代进程加快，板块估值具备吸引力。',
            '芯片': 'AI大模型训练与推理需求激增，带动算力芯片、存储芯片需求爆发，行业景气度持续上行。',
            '存储': '存储芯片周期见底回升，AI服务器需求爆发带动HBM量价齐升，行业基本面持续改善。',
            '人工智能': 'AI技术迭代加速，大模型应用落地加速，算力、数据、算法三大要素持续受益。',
            'AI': 'AI大模型加速落地，算力需求持续增长，应用场景不断拓展，行业天花板持续抬高。',
            '算力': 'AI大模型训练推理需求旺盛，算力基础设施建设加速，服务器、数据中心产业链受益。',
            '软件': 'AI赋能软件行业，生产力工具、企业服务等领域迎来新的增长机遇。',
            '计算机': 'AI产业趋势明确，信创、数据要素、AI应用等多轮驱动，行业景气度持续提升。',
            '通信': '算力网络建设加速，光模块、交换机需求旺盛，AI算力基础设施产业链持续受益。',
            '光模块': 'AI算力需求爆发带动光模块量价齐升，800G/1.6T产品加速渗透，行业景气度高企。',
            '电子': '消费电子复苏+AI硬件创新双轮驱动，半导体、消费电子产业链迎来估值修复。',
            '新能源': '行业基本面边际改善，产能出清加速，龙头企业竞争优势凸显，估值具备安全边际。',
            '光伏': '产业链价格触底，需求有望逐步回暖，N型技术迭代加速，头部企业优势明显。',
            '锂电': '新能源汽车销量稳步增长，储能需求爆发，锂电池产业链有望迎来量利齐升。',
            '汽车': '新能源汽车渗透率持续提升，智能化加速落地，自主品牌竞争力不断增强。',
            '医药': '创新药政策环境改善，医保谈判预期向好，中药、创新器械等细分领域有结构性机会。',
            '医疗': '医疗新基建持续推进，创新器械、IVD等细分领域需求旺盛，行业有望逐步复苏。',
            '消费': '消费复苏预期增强，政策刺激持续发力，必选消费相对稳健，可选消费弹性较大。',
            '食品饮料': '消费场景逐步恢复，高端白酒韧性较强，大众品成本压力缓解，盈利有望改善。',
            '银行': '估值处于历史低位，股息率具备吸引力，经济复苏预期下资产质量有望改善。',
            '非银金融': '资本市场改革持续推进，券商、保险板块估值修复，政策催化下具备弹性。',
            '房地产': '政策支持力度加大，行业基本面有望边际改善，龙头房企竞争优势凸显。',
            '建筑': '基建投资稳增长，一带一路催化，央企估值重塑，建筑板块具备配置价值。',
            '建材': '地产链边际改善，基建投资托底，新型建材、防水材料等细分领域有机会。',
            '钢铁': '需求预期改善，供给端约束仍在，行业盈利有望修复，龙头企业具备竞争力。',
            '有色': '新能源需求拉动，供需格局优化，铜、铝、锂等品种具备投资价值。',
            '稀土': '稀土永磁需求增长，供给格局持续优化，行业景气度有望维持高位。',
            '煤炭': '供需格局偏紧，煤价维持高位，高股息属性突出，具备防御配置价值。',
            '石油石化': '国际油价维持高位，国企改革深化，龙头企业盈利稳定，高股息属性明显。',
            '军工': '行业确定性强，十四五订单饱满，军工电子、新材料等细分领域增速较快。',
            '电力设备': '新能源发电装机持续增长，电网投资加大，电力设备行业需求稳定。',
            '机械': '设备更新换代需求+出口增长，工程机械、通用机械等板块有望复苏。',
            '基础化工': '化工品价格触底回升，新能源材料需求增长，细分龙头企业具备阿尔法机会。',
            '磨具磨料': '光伏、半导体等下游需求增长，行业集中度提升，龙头企业盈利能力改善。',
        }
        
        # 精确匹配
        if sector_name in reasons:
            return reasons[sector_name]
        
        # 模糊匹配
        for key, reason in reasons.items():
            if key in sector_name or sector_name in key:
                return reason
        
        # 默认描述
        return f"行业景气度提升，资金关注度上升，板块龙头企业表现亮眼，市场情绪回暖带动板块整体走强。"
    
    def add_focus_point(self, focus: str):
        """添加午盘焦点"""
        content = f'''
        <div class="bg-gradient-to-r from-yellow-500/20 to-orange-500/15 border border-yellow-500/30 rounded-xl p-5">
            <div class="flex items-center gap-2 mb-3">
                <span class="text-2xl">⚡</span>
                <span class="text-white font-bold">午盘焦点</span>
            </div>
            <p class="text-white/80 leading-relaxed text-sm">
                {focus}
            </p>
        </div>
        '''
        self.add_section("午盘焦点", content, "⚡")
    
    def add_market_overview(self):
        """添加市场概览 - Pro版"""
        # 计算市场状态
        up_count = sum(1 for idx in self.indices if idx.get('up', True))
        total = len(self.indices)
        
        if up_count == total:
            market_status = "上涨"
            status_color = "text-green-400"
            status_bg = "from-green-500/20 to-emerald-500/10"
        elif up_count == 0:
            market_status = "下跌"
            status_color = "text-red-400"
            status_bg = "from-red-500/20 to-orange-500/10"
        else:
            market_status = "震荡分化"
            status_color = "text-yellow-400"
            status_bg = "from-yellow-500/20 to-orange-500/10"
        
        # 指数卡片
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
        <div class="grid grid-cols-2 md:grid-cols-4 gap-3 mb-4">
            {cards_html}
        </div>
        <div class="text-center">
            <span class="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-white/10 {status_color} text-sm font-medium">
                <span>📊</span>
                市场状态：{market_status}
            </span>
        </div>
        '''
        
        self.add_section("市场概览", content, "📈")
    
    def add_hot_topics(self, topics: list = None):
        """添加市场热点解析"""
        if topics is None:
            # 从热门板块生成热点
            topics = []
            for sector in self.hot_sectors[:3]:
                name = sector.get('name', '')
                change_pct = sector.get('change_pct', '')
                leader = sector.get('leader', '')
                reason = sector.get('reason', '')
                
                # 如果没有reason，基于板块名称生成描述
                if not reason:
                    reason = self._generate_sector_reason(name)
                
                topic = {
                    'tag': name,
                    'title': f"{name}板块领涨",
                    'content': f"{name}板块今日表现强势，{change_pct}。{reason}",
                    'hot': True,
                    'stocks': [leader] if leader else []
                }
                topics.append(topic)
        
        if not topics:
            return
        
        topics_html = '<div class="space-y-3">'
        
        for topic in topics:
            is_hot = topic.get('hot', False)
            tag = topic.get('tag', '热点')
            stocks = topic.get('stocks', [])
            
            hot_badge = ''
            if is_hot:
                hot_badge = '<span class="bg-gradient-to-r from-red-500 to-orange-500 text-white text-xs font-bold px-2 py-0.5 rounded-full">🔥 热门</span>'
            
            stocks_html = ''
            if stocks:
                stock_tags = ' '.join([
                    f'<span class="bg-blue-500/20 text-blue-400 text-xs px-2 py-1 rounded-md border border-blue-500/30">{s}</span>'
                    for s in stocks
                ])
                stocks_html = f'''
                <div class="mt-3 pt-3 border-t border-white/10">
                    <div class="text-xs text-white/50 mb-2">相关标的</div>
                    <div class="flex flex-wrap gap-2">
                        {stock_tags}
                    </div>
                </div>
                '''
            
            topics_html += f'''
            <div class="bg-white/5 backdrop-blur-sm rounded-xl p-4 border border-white/10">
                <div class="flex items-center gap-3 mb-3">
                    <div class="w-9 h-9 bg-gradient-to-br from-blue-500 to-purple-500 rounded-lg flex items-center justify-center flex-shrink-0">
                        <span class="text-white text-sm">📌</span>
                    </div>
                    <div class="flex-1">
                        <div class="flex items-center gap-2">
                            <span class="text-xs font-semibold text-blue-400 bg-blue-500/20 px-2 py-0.5 rounded">{tag}</span>
                            <span class="text-white font-semibold text-sm">{topic.get("title", "")}</span>
                        </div>
                    </div>
                    {hot_badge}
                </div>
                <div class="text-sm text-white/70 leading-relaxed pl-12">
                    {topic.get("content", "")}
                </div>
                {stocks_html}
            </div>
            '''
        
        topics_html += '</div>'
        
        self.add_section("市场热点解析", topics_html, "🔥")
    
    def add_decline_sectors(self, sectors: list = None):
        """添加领跌板块警示"""
        if sectors is None:
            sectors = [
                {'name': '新能源', 'change': '-1.5%', 'reason': '板块轮动调整，短期资金流出'},
                {'name': '医药生物', 'change': '-0.8%', 'reason': '集采预期影响，观望情绪浓厚'},
            ]
        
        if not sectors:
            return
        
        sectors_html = '<div class="space-y-2">'
        
        for sector in sectors:
            sectors_html += f'''
            <div class="bg-gradient-to-r from-red-500/15 to-orange-500/10 border border-red-500/20 rounded-xl p-4">
                <div class="flex items-center justify-between mb-1">
                    <span class="text-red-400 font-semibold text-sm">{sector["name"]}</span>
                    <span class="text-red-400 font-bold text-sm">{sector.get("change", "")}</span>
                </div>
                <div class="text-xs text-red-300/70">
                    💡 {sector.get("reason", "")}
                </div>
            </div>
            '''
        
        sectors_html += '</div>'
        
        self.add_section("领跌板块警示", sectors_html, "⚠️")
    
    def add_holdings_tracking(self):
        """添加持仓股跟踪 - Pro版"""
        stocks = self.portfolio.get('stocks', [])
        
        if not stocks:
            return
        
        holdings_html = '<div class="space-y-3">'
        
        for stock in stocks:
            name = stock.get('name', '')
            code = stock.get('code', stock.get('id', ''))
            price = f"{stock.get('current_price', 0):.2f}"
            today_change = stock.get('today_change', 0) * 100
            up = today_change >= 0
            # 处理评论/建议字段，兼容字符串和字典两种格式
            raw_comment = stock.get('comment', '')
            if raw_comment and isinstance(raw_comment, str) and raw_comment != 'N/A':
                comment = raw_comment
            else:
                advice = stock.get('advice', {})
                if isinstance(advice, dict):
                    comment = advice.get('text', '')
                elif isinstance(advice, str):
                    comment = advice
                else:
                    comment = ''
            
            change_color = 'text-green-400' if up else 'text-red-400'
            change_sign = '+' if up else ''
            
            holdings_html += f'''
            <div class="bg-white/5 rounded-xl p-4 border border-white/10">
                <div class="flex items-center">
                    <div class="flex-1">
                        <div class="flex items-center gap-2 mb-1">
                            <span class="text-white font-semibold">{name}</span>
                            <span class="text-xs text-white/40">{code}</span>
                        </div>
                        <div class="text-xs text-white/50 leading-relaxed">
                            {comment}
                        </div>
                    </div>
                    <div class="text-right">
                        <div class="text-lg font-bold {change_color}">{price}</div>
                        <div class="text-xs {change_color} font-medium">{change_sign}{today_change:.2f}%</div>
                    </div>
                </div>
            </div>
            '''
        
        holdings_html += '</div>'
        
        self.add_section("持仓股跟踪", holdings_html, "💼")
    
    def add_trading_strategy(self, strategy: str = None):
        """添加午盘操作策略"""
        if strategy is None:
            strategy = """
            上午市场整体呈现震荡格局，板块轮动明显。操作上建议：
            1. 对于持仓标的，保持耐心，不盲目追涨杀跌
            2. 关注量能变化，若放量突破可适当加仓
            3. 高位股注意风险，避免追高
            4. 重点关注午后能否形成明确的方向选择
            """
        
        content = f'''
        <div class="bg-gradient-to-br from-purple-500/15 to-blue-500/10 border border-purple-500/20 rounded-xl p-5">
            <div class="flex items-center gap-2 mb-3">
                <span class="text-xl">📝</span>
                <span class="text-white font-bold">操作策略</span>
            </div>
            <div class="text-sm text-white/70 leading-relaxed space-y-2">
                {strategy.strip().replace(chr(10), '<br>')}
            </div>
        </div>
        '''
        
        self.add_section("午盘操作策略", content, "📝")
    
    def add_risk_warning(self, risks: list = None):
        """添加风险警示"""
        if risks is None:
            risks = [
                "市场波动风险：大盘震荡加剧，短期方向不明朗",
                "板块轮动风险：热点切换较快，追高容易被套",
                "外围市场风险：美股波动可能影响A股情绪",
                "政策不及预期风险：相关政策落地时间或力度存疑",
            ]
        
        risk_items = ''.join([
            f'<div class="flex items-start gap-2 mb-2"><span class="text-yellow-400 mt-0.5">⚠️</span><span class="text-sm text-white/70">{r}</span></div>'
            for r in risks
        ])
        
        content = f'''
        <div class="bg-gradient-to-br from-yellow-500/10 to-orange-500/5 border border-yellow-500/20 rounded-xl p-5">
            <div class="flex items-center gap-2 mb-4">
                <span class="text-xl">⚠️</span>
                <span class="text-white font-bold">风险提示</span>
            </div>
            <div class="space-y-1">
                {risk_items}
            </div>
        </div>
        '''
        
        self.add_section("风险警示", content, "⚠️")
    
    def add_summary(self, summary: str = None):
        """添加市场逻辑总结"""
        if summary is None:
            # 基于指数和板块生成总结
            indices = self.indices
            hot = self.hot_sectors
            
            summary_parts = []
            
            if indices and len(indices) >= 3:
                idx_summary = []
                for idx in indices[:3]:
                    name = idx.get('name', '')
                    # 兼容两种格式：change_pct(数值) 和 change_pct_str(字符串)
                    change_pct = idx.get('change_pct')
                    if change_pct is None:
                        change_str = idx.get('change_pct_str', idx.get('change', '0%'))
                    else:
                        if isinstance(change_pct, (int, float)):
                            change_str = f"{'+' if change_pct >= 0 else ''}{change_pct*100:.2f}%"
                        else:
                            change_str = str(change_pct)
                    
                    if '+' in change_str or '涨' in change_str:
                        idx_summary.append(f"{name}上涨{change_str.replace('+', '')}")
                    else:
                        idx_summary.append(f"{name}下跌{change_str.replace('-', '')}")
                
                if len(idx_summary) >= 3:
                    summary_parts.append(f"今日A股三大指数走势分化，{idx_summary[0]}，{idx_summary[1]}，{idx_summary[2]}。")
                else:
                    summary_parts.append(f"市场走势分化，{'，'.join(idx_summary)}。")
            
            if hot and len(hot) > 0:
                hot_names = [h.get('name', '') for h in hot[:3] if h.get('name')]
                if hot_names:
                    summary_parts.append(f"盘面上，{'、'.join(hot_names)}等板块表现活跃，领涨市场。")
            
            # 添加市场量能和结构性特征
            market_data = {}
            if hasattr(self, 'market_data') and self.market_data:
                market_data = self.market_data
            
            turnover = market_data.get('turnover', '')
            if turnover:
                summary_parts.append(f"半日成交约{turnover}，市场流动性保持充裕。")
            else:
                summary_parts.append("市场量能维持较高水平，交投活跃。")
            
            summary_parts.append("整体来看，市场呈现结构性行情特征，科技成长赛道相对强势，传统周期板块表现偏弱。")
            summary_parts.append("操作建议：轻指数、重个股，聚焦高景气赛道核心标的，逢低布局为主，避免追高。")
            
            summary = '\n'.join(summary_parts)
        
        content = f'''
        <div class="bg-gradient-to-br from-blue-500/10 to-cyan-500/5 border border-blue-500/20 rounded-xl p-5">
            <div class="flex items-center gap-2 mb-3">
                <span class="text-xl">📊</span>
                <span class="text-white font-bold">市场逻辑总结</span>
            </div>
            <div class="text-sm text-white/70 leading-relaxed space-y-2">
                {summary.strip().replace(chr(10), '<br>')}
            </div>
        </div>
        '''
        
        self.add_section("市场逻辑总结", content, "📊")
    
    def build_standard_report(self):
        """构建标准版本的盘中快报"""
        # 生成默认焦点
        hot = self.hot_sectors
        focus_text = '上午市场震荡运行，'
        if hot:
            focus_text += f"{hot[0].get('name', '')}等板块表现活跃，"
        focus_text += '关注午后量能变化和方向选择。'
        
        self.add_focus_point(focus_text)
        self.add_market_overview()
        self.add_hot_topics()
        self.add_holdings_tracking()
        self.add_trading_strategy()
        self.add_risk_warning()
        self.add_summary()
        
        return self


if __name__ == '__main__':
    # 测试生成
    gen = IntradayProGenerator('2026-06-15', '周一午盘')
    gen.build_standard_report()
    html = gen.render()
    print(f'Pro版盘中快报生成成功，长度: {len(html)} 字符')
    
    # 保存测试
    os.makedirs('../docs/intraday', exist_ok=True)
    with open('../docs/intraday/20260615_盘中快报.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print('已保存到 docs/intraday/20260615_盘中快报.html')
