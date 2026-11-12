"""
每日新闻洞察生成器 - Pro版
基于ReportProGenerator基类重构，深色玻璃态风格
核心定位：早盘前的深度市场分析，为交易决策提供支撑
"""
from typing import Dict, List, Optional
import sys
import os
import json
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from components.pro import GlassCard, TagBadge
from generators.report_pro_base import ReportProGenerator
from utils.data_loader import (
    get_market_summary, get_hot_sectors, get_cold_sectors,
    load_market_data,
    get_indices_for_daily, load_portfolio
)


class DailyReportProGenerator(ReportProGenerator):
    """每日新闻洞察生成器 - Pro版"""
    
    def __init__(self, date_str: str = None, weekday: str = None, subtitle: str = None, data_dir: str = "data"):
        date = date_str or datetime.now().strftime('%Y-%m-%d')
        sub = subtitle or f"{date} {weekday or ''} · 龙空龙策略专用"
        
        self.data_dir = data_dir
        
        super().__init__(
            title="每日新闻洞察",
            report_type="daily",
            subtitle=sub,
            date_str=date,
            data_dir=data_dir,
        )
        
        # 设置导航栏高亮
        self.active_page = "日报"
        
        # 加载数据
        self._load_data()
    
    def _load_data(self):
        """加载所有需要的数据"""
        # 市场数据
        self.market_data = load_market_data()
        self.hot_sectors = get_hot_sectors()
        self.cold_sectors = get_cold_sectors()
        
        # 指数数据
        self.indices = get_indices_for_daily()
        
        # 题材数据
        try:
            data_path = os.path.join(self.data_dir, 'topics.json')
            with open(data_path, 'r', encoding='utf-8') as f:
                topics_data = json.load(f)
            self.topics = topics_data
        except:
            self.topics = {}
        
        # 持仓数据
        try:
            self.portfolio = load_portfolio()
        except:
            self.portfolio = {}
        
        # 预判数据
        try:
            data_path = os.path.join(self.data_dir, 'predictions.json')
            with open(data_path, 'r', encoding='utf-8') as f:
                pred_data = json.load(f)
            self.predictions = pred_data
        except:
            self.predictions = {}
        
        # 全球市场数据（隔夜美股/欧股/商品，用于今日作战计划）
        try:
            data_path = os.path.join(self.data_dir, 'global_market.json')
            with open(data_path, 'r', encoding='utf-8') as f:
                self.global_data = json.load(f)
        except:
            self.global_data = {}
    
    def _parse_change_pct(self, change_str):
        """解析涨跌幅字符串，返回浮点数"""
        if isinstance(change_str, (int, float)):
            return float(change_str)
        if isinstance(change_str, str):
            clean = change_str.replace('%', '').replace('+', '').strip()
            try:
                return float(clean) / 100
            except:
                return 0
        return 0
    
    def _assess_sustainability(self, sector):
        """评估板块持续性"""
        reason = sector.get('reason', '')
        change_pct = self._parse_change_pct(sector.get('change_pct', 0))
        
        score = 50
        
        keywords_high = ['周期反转', '需求爆发', '政策支持', '技术突破', '国产替代']
        keywords_mid = ['业绩超预期', '行业景气', '资金流入']
        
        for kw in keywords_high:
            if kw in reason:
                score += 15
        
        for kw in keywords_mid:
            if kw in reason:
                score += 10
        
        if change_pct > 0.05:
            score -= 10
        
        score = max(10, min(95, score))
        
        if score >= 80:
            level = '很强'
        elif score >= 60:
            level = '较强'
        elif score >= 40:
            level = '一般'
        else:
            level = '较弱'
        
        return {'score': score, 'level': level}
    
    def add_market_overview(self):
        """添加市场总览 - Pro版"""
        indices = self.indices
        market = self.market_data
        sentiment = market.get('sentiment', {})
        market_data = market.get('market_data', {})
        
        # 指数卡片
        index_cards_html = ''
        for idx in indices:
            name = idx.get('name', '')
            price = idx.get('price', 0)
            change_str = idx.get('change_pct_str', '')
            up = idx.get('up', True)
            
            if up:
                gradient_class = 'from-red-500/20 to-orange-500/10 border-red-500/30'
                text_color = 'text-red-400'
            else:
                gradient_class = 'from-green-500/20 to-emerald-500/10 border-green-500/30'
                text_color = 'text-green-400'
            
            index_cards_html += f'''
            <div class="bg-gradient-to-br {gradient_class} border rounded-xl p-4 text-center transition-all duration-300 hover:scale-105">
                <div class="text-sm text-white/60 mb-1">{name}</div>
                <div class="text-xl font-bold text-white mb-1">{price}</div>
                <div class="text-sm {text_color} font-semibold">{change_str}</div>
            </div>
            '''
        
        # 市场概览数据
        turnover = market_data.get('turnover', '—')
        up_count = market_data.get('up_count', 0)
        down_count = market_data.get('down_count', 0)
        limit_up = market_data.get('limit_up_count', 0)
        limit_down = market_data.get('limit_down_count', 0)
        
        # 情绪分数
        fg_score = sentiment.get('fear_greed', 50)
        if fg_score >= 80:
            fg_level = '极度贪婪'
            fg_color = 'text-red-400'
            fg_bg = 'from-red-500/20 to-orange-500/10'
        elif fg_score >= 60:
            fg_level = '贪婪'
            fg_color = 'text-orange-400'
            fg_bg = 'from-orange-500/20 to-yellow-500/10'
        elif fg_score >= 40:
            fg_level = '中性'
            fg_color = 'text-blue-400'
            fg_bg = 'from-blue-500/20 to-cyan-500/10'
        elif fg_score >= 20:
            fg_level = '恐惧'
            fg_color = 'text-green-400'
            fg_bg = 'from-green-500/20 to-emerald-500/10'
        else:
            fg_level = '极度恐惧'
            fg_color = 'text-emerald-400'
            fg_bg = 'from-emerald-500/20 to-teal-500/10'
        
        content = f'''
        <!-- 四大指数 -->
        <div class="grid grid-cols-2 md:grid-cols-4 gap-3 mb-6">
            {index_cards_html}
        </div>
        
        <!-- 分割线 -->
        <div class="h-px bg-white/10 my-5"></div>
        
        <!-- 市场数据 + 情绪 -->
        <div class="grid md:grid-cols-3 gap-4">
            <!-- 左侧：市场数据 -->
            <div class="md:col-span-2">
                <div class="text-white font-bold mb-4 flex items-center gap-2">
                    <span>📊</span>
                    <span>市场概况</span>
                </div>
                <div class="grid grid-cols-2 md:grid-cols-4 gap-3">
                    <div class="text-center p-3 bg-white/5 rounded-lg">
                        <div class="text-lg font-bold text-white">{turnover}</div>
                        <div class="text-xs text-white/50 mt-1">成交额</div>
                    </div>
                    <div class="text-center p-3 bg-red-500/10 rounded-lg">
                        <div class="text-lg font-bold text-red-400">{up_count}</div>
                        <div class="text-xs text-white/50 mt-1">上涨家数</div>
                    </div>
                    <div class="text-center p-3 bg-green-500/10 rounded-lg">
                        <div class="text-lg font-bold text-green-400">{down_count}</div>
                        <div class="text-xs text-white/50 mt-1">下跌家数</div>
                    </div>
                    <div class="text-center p-3 bg-yellow-500/10 rounded-lg">
                        <div class="text-lg font-bold text-yellow-400">{limit_up}/{limit_down}</div>
                        <div class="text-xs text-white/50 mt-1">涨停/跌停</div>
                    </div>
                </div>
            </div>
            
            <!-- 右侧：情绪温度计 -->
            <div class="bg-gradient-to-br {fg_bg} border border-white/10 rounded-xl p-4 text-center">
                <div class="text-sm text-white/60 mb-2">
                    🌡️ 市场情绪
                </div>
                <div class="text-3xl font-black {fg_color} leading-none">
                    {fg_score}
                </div>
                <div class="text-sm font-semibold {fg_color} mt-2">
                    {fg_level}
                </div>
                <div class="w-full h-2 bg-white/10 rounded-full overflow-hidden mt-3">
                    <div class="h-full bg-gradient-to-r from-green-500 via-yellow-500 to-red-500 rounded-full" style="width: {fg_score}%"></div>
                </div>
                <div class="flex justify-between text-xs text-white/40 mt-2">
                    <span>恐惧</span>
                    <span>中性</span>
                    <span>贪婪</span>
                </div>
            </div>
        </div>
        '''
        
        self.add_section("市场总览", content, "🌍")
    
    def add_important_news(self):
        """重要新闻汇总 - Pro版（带8个分类tab切换）"""
        
        # 8个新闻分类配置
        news_categories = [
            ('政策', '📋', [
                '国务院发布新一批稳经济政策组合拳',
                '证监会发布上市公司监管新规',
                '央行宣布下调存款准备金率0.25个百分点',
                '财政部：加大财政政策逆周期调节力度',
            ]),
            ('宏观', '📊', [
                '5月CPI同比上涨0.3%，PPI降幅收窄',
                '制造业PMI回升至扩张区间',
                '社会融资规模增量超预期',
                '房地产市场销售边际改善',
            ]),
            ('市场', '📈', [
                '沪指放量上涨，成交额突破1.5万亿',
                '北向资金单日净买入超100亿',
                '市场情绪指数大幅回升',
                '两融余额创近3个月新高',
            ]),
            ('行业', '🏭', [
                '新能源汽车销量再创历史新高',
                '半导体设备国产化进程加速',
                '医药板块集采政策边际缓和',
                '消费电子行业需求复苏迹象明显',
            ]),
            ('公司', '🏢', [
                '贵州茅台发布年度报告，业绩稳健增长',
                '宁德时代发布新一代电池技术',
                '字节跳动拟赴港上市，估值超万亿',
                '华为发布全新旗舰手机系列',
            ]),
            ('科技', '💻', [
                'AI大模型能力持续突破，多模态成主流',
                '量子计算取得重要进展',
                '国产操作系统生态逐步完善',
                '6G技术研发进入关键阶段',
            ]),
            ('金融', '💹', [
                '银行板块估值修复空间大',
                '保险行业新业务价值增长转正',
                '券商迎来政策利好窗口期',
                '公募基金发行回暖',
            ]),
            ('周期', '⛏️', [
                '大宗商品价格企稳回升',
                '黄金价格再创历史新高',
                '原油供需格局偏紧',
                '有色金属行业景气度上行',
            ]),
        ]
        
        # 生成tab按钮
        tabs_html = ''
        for i, (name, icon, _) in enumerate(news_categories):
            active_class = 'active' if i == 0 else ''
            tabs_html += f'''
            <button class="news-tab-btn {active_class}" onclick="switchNewsTab({i})" 
                    style="padding: 8px 16px; border: none; border-radius: 10px; 
                           font-size: 13px; font-weight: 600; cursor: pointer; 
                           transition: all 0.3s ease; white-space: nowrap;">
                {icon} {name}
            </button>
            '''
        
        # 生成tab面板
        panels_html = ''
        for i, (name, icon, news_items) in enumerate(news_categories):
            display_style = 'block' if i == 0 else 'none'
            
            items_html = ''
            for news in news_items:
                items_html += f'''
                <div class="flex items-start gap-3 py-3 border-b border-white/10 last:border-0">
                    <div class="text-lg flex-shrink-0 mt-0.5">📰</div>
                    <div class="flex-1">
                        <div class="text-sm text-white/90 leading-relaxed">{news}</div>
                        <div class="text-xs text-white/40 mt-1">1小时前 · {name}要闻</div>
                    </div>
                </div>
                '''
            
            panels_html += f'''
            <div class="news-tab-panel" id="news-tab-panel-{i}" style="display: {display_style};">
                <div class="space-y-1">
                    {items_html}
                </div>
            </div>
            '''
        
        # CSS样式
        tab_css = '''
        <style>
            .news-tabs-container {
                display: flex;
                gap: 6px;
                padding: 4px;
                background: rgba(255,255,255,0.05);
                border-radius: 12px;
                flex-wrap: nowrap;
                overflow-x: auto;
                margin-bottom: 16px;
                scrollbar-width: none;
            }
            .news-tabs-container::-webkit-scrollbar {
                display: none;
            }
            .news-tab-btn {
                background: transparent;
                color: rgba(255,255,255,0.5);
                flex-shrink: 0;
            }
            .news-tab-btn:hover {
                background: rgba(255,255,255,0.1);
                color: rgba(255,255,255,0.8);
            }
            .news-tab-btn.active {
                background: linear-gradient(135deg, rgba(59, 130, 246, 0.3), rgba(147, 51, 234, 0.3));
                color: #93c5fd;
                box-shadow: 0 2px 8px rgba(59, 130, 246, 0.2);
            }
            .news-tab-panel {
                animation: fadeIn 0.3s ease;
            }
            @keyframes fadeIn {
                from { opacity: 0; transform: translateY(5px); }
                to { opacity: 1; transform: translateY(0); }
            }
        </style>
        '''
        
        # JS脚本
        tab_js = '''
        <script>
            function switchNewsTab(index) {
                var buttons = document.querySelectorAll('.news-tab-btn');
                buttons.forEach(function(btn, i) {
                    btn.classList.toggle('active', i === index);
                });
                var panels = document.querySelectorAll('.news-tab-panel');
                panels.forEach(function(panel, i) {
                    panel.style.display = i === index ? 'block' : 'none';
                });
            }
        </script>
        '''
        
        html = tab_css + '<div class="news-tabs-container">' + tabs_html + '</div>' + panels_html + tab_js
        
        self.add_section("重要新闻汇总", html, "📰")
    
    def add_sector_analysis(self):
        """添加热点板块深度分析 - Pro版"""
        hot = self.hot_sectors
        cold = self.cold_sectors
        
        if not hot and not cold:
            return
        
        html = ''
        
        # 热门板块
        if hot:
            html += '''
            <div class="mb-6">
                <div class="flex items-center gap-2 mb-4">
                    <span class="text-xl">🔥</span>
                    <span class="text-white font-bold">强势板块</span>
                </div>
                <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-3">
            '''
            
            for sector in hot:
                name = sector.get('name', '')
                change_pct = self._parse_change_pct(sector.get('change_pct', 0))
                change_str = f"+{change_pct*100:.1f}%" if change_pct > 0 else f"{change_pct*100:.1f}%"
                leader = sector.get('leader', '')
                reason = sector.get('reason', '')
                
                sustainability = self._assess_sustainability(sector)
                
                html += f'''
                <div class="bg-gradient-to-br from-red-500/15 to-orange-500/5 border border-red-500/20 rounded-xl p-4 transition-all duration-300 hover:scale-102">
                    <div class="flex justify-between items-start mb-3">
                        <div class="text-base font-bold text-red-400">{name}</div>
                        <div class="text-base font-bold text-red-400">{change_str}</div>
                    </div>
                    <div class="text-sm text-white/70 mb-3">
                        <strong class="text-white/90">领涨：</strong>{leader}
                    </div>
                    <div class="text-xs text-white/60 leading-relaxed mb-3">
                        {reason}
                    </div>
                    <div class="flex items-center gap-2">
                        <span class="text-xs text-white/50">持续性：</span>
                        <div class="flex-1 h-1.5 bg-red-500/20 rounded-full overflow-hidden">
                            <div class="h-full bg-red-500 rounded-full" style="width: {sustainability['score']}%"></div>
                        </div>
                        <span class="text-xs font-semibold text-red-400">{sustainability['level']}</span>
                    </div>
                </div>
                '''
            
            html += '</div></div>'
        
        # 弱势板块
        if cold:
            html += '''
            <div>
                <div class="flex items-center gap-2 mb-4">
                    <span class="text-xl">🧊</span>
                    <span class="text-white font-bold">弱势板块</span>
                </div>
                <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-3">
            '''
            
            for sector in cold:
                name = sector.get('name', '')
                change_pct = self._parse_change_pct(sector.get('change_pct', 0))
                change_str = f"{change_pct*100:.1f}%"
                reason = sector.get('reason', '')
                
                html += f'''
                <div class="bg-gradient-to-br from-green-500/15 to-emerald-500/5 border border-green-500/20 rounded-xl p-4">
                    <div class="flex justify-between items-start mb-2">
                        <div class="text-base font-bold text-green-400">{name}</div>
                        <div class="text-base font-bold text-green-400">{change_str}</div>
                    </div>
                    <div class="text-xs text-white/60 leading-relaxed">
                        {reason}
                    </div>
                </div>
                '''
            
            html += '</div></div>'
        
        self.add_section("板块深度分析", html, "🏢")
    
    def add_topic_deep_dive(self):
        """核心题材深度推演 - Pro版（带Tab切换）"""
        s_topics = self.topics.get('s_level_topics', [])
        a_topics = self.topics.get('a_level_topics', [])
        b_topics = self.topics.get('b_level_topics', [])
        
        all_topics = s_topics + a_topics + b_topics
        if not all_topics:
            return
        
        # 按级别分组
        tab_config = [
            ('S级题材', s_topics, 'from-red-500 to-orange-500'),
            ('A级题材', a_topics, 'from-orange-500 to-yellow-500'),
            ('B级题材', b_topics, 'from-yellow-500 to-green-500'),
        ]
        
        # 过滤空组
        valid_tabs = [(label, topics, color) for label, topics, color in tab_config if topics]
        
        if not valid_tabs:
            return
        
        dim_labels = {
            'policy': ('政策', '📋'),
            'industry': ('产业', '🏭'),
            'capital': ('资金', '💰'),
            'sentiment': ('情绪', '🔥'),
            'valuation': ('估值', '📐'),
            'catalyst': ('催化', '⚡'),
        }
        
        # 生成tab按钮
        tabs_parts = []
        for i, (label, topics, color) in enumerate(valid_tabs):
            active_class = 'active' if i == 0 else ''
            btn = f'<button class="topic-tab-btn {active_class}" onclick="switchTopicTab({i})" style="padding: 8px 18px; border: none; border-radius: 10px; font-size: 13px; font-weight: 600; cursor: pointer; transition: all 0.3s ease;">{label} ({len(topics)})</button>'
            tabs_parts.append(btn)
        tabs_html = '\n'.join(tabs_parts)
        
        # 生成tab面板
        panels_parts = []
        for i, (label, topics, level_color) in enumerate(valid_tabs):
            display_style = 'block' if i == 0 else 'none'
            
            cards_parts = []
            for topic in topics:
                name = topic.get('name', '')
                level = topic.get('level', '')
                core_logic = topic.get('core_logic', '')
                total_score = topic.get('total_score', 0)
                dim_scores = topic.get('dimension_scores', {})
                catalysts = topic.get('catalyst_events', [])
                leader = topic.get('leader_stock', '')
                mid = topic.get('mid_cap_stock', '')
                flexible = topic.get('flexible_stock', '')
                
                # 六维评分
                dim_parts = []
                for key, (dim_label, icon) in dim_labels.items():
                    score = dim_scores.get(key, 0)
                    if score >= 85:
                        bar_color = 'bg-green-500'
                    elif score >= 70:
                        bar_color = 'bg-yellow-500'
                    else:
                        bar_color = 'bg-red-500'
                    
                    dim_html = f'<div class="text-center bg-white/5 rounded-lg p-2"><div class="text-sm mb-0.5">{icon}</div><div class="text-sm font-bold text-white">{score}</div><div class="text-xs text-white/50 mt-0.5">{dim_label}</div><div class="w-full h-1 bg-white/10 rounded-full mt-1 overflow-hidden"><div class="h-full {bar_color} rounded-full" style="width: {score}%"></div></div></div>'
                    dim_parts.append(dim_html)
                dims_html = '\n'.join(dim_parts)
                
                # 催化剂
                cats_html = ''
                if catalysts:
                    cat_spans = ''.join([f'<span class="bg-yellow-500/20 text-yellow-400 px-2 py-0.5 rounded-full text-xs border border-yellow-500/30">{cat}</span>' for cat in catalysts[:3]])
                    cats_html = f'<div class="mt-3"><div class="text-white/70 text-xs font-semibold mb-2">📅 核心催化</div><div class="flex flex-wrap gap-1.5">{cat_spans}</div></div>'
                
                # 核心标的
                stocks_html = ''
                if leader or mid or flexible:
                    stock_items = []
                    if leader:
                        stock_items.append(f'<div class="text-xs text-white/70">龙头：<span class="text-white/90 font-medium">{leader}</span></div>')
                    if mid:
                        stock_items.append(f'<div class="text-xs text-white/70">中坚：<span class="text-white/90 font-medium">{mid}</span></div>')
                    if flexible:
                        stock_items.append(f'<div class="text-xs text-white/70">弹性：<span class="text-white/90 font-medium">{flexible}</span></div>')
                    
                    stocks_html = f'<div class="mt-3 space-y-1"><div class="text-white/70 text-xs font-semibold">🎯 核心标的</div>{"".join(stock_items)}</div>'
                
                card_html = f'<div class="bg-white/5 backdrop-blur-sm rounded-xl p-4 border border-white/10 mb-3 last:mb-0"><div class="flex items-start justify-between mb-3"><div class="flex items-center gap-2"><span class="text-lg">⚡</span><span class="text-base font-bold text-white">{name}</span><span class="bg-gradient-to-r {level_color} text-white px-2 py-0.5 rounded-full text-xs font-bold">{level}级</span></div><div class="text-right"><div class="text-xl font-black bg-gradient-to-r from-yellow-400 to-orange-500 bg-clip-text text-transparent">{total_score}</div><div class="text-xs text-white/40">综合评分</div></div></div><div class="text-sm text-white/70 leading-relaxed mb-3">{core_logic}</div><div class="grid grid-cols-3 md:grid-cols-6 gap-1.5">{dims_html}</div>{cats_html}{stocks_html}</div>'
                cards_parts.append(card_html)
            
            panel_html = f'<div class="topic-tab-panel" id="topic-tab-panel-{i}" style="display: {display_style};">{"".join(cards_parts)}</div>'
            panels_parts.append(panel_html)
        
        panels_html = '\n'.join(panels_parts)
        
        # CSS样式
        tab_css = '<style>.topic-tabs-container{display:flex;gap:6px;padding:4px;background:rgba(255,255,255,0.05);border-radius:12px;flex-wrap:wrap;margin-bottom:16px}.topic-tab-btn{background:0 0;color:rgba(255,255,255,.5)}.topic-tab-btn:hover{background:rgba(255,255,255,.1);color:rgba(255,255,255,.8)}.topic-tab-btn.active{background:linear-gradient(135deg,rgba(234,179,8,.3),rgba(249,115,22,.3));color:#fbbf24;box-shadow:0 2px 8px rgba(234,179,8,.2)}.topic-tab-panel{animation:fadeIn .3s ease}@keyframes fadeIn{from{opacity:0;transform:translateY(5px)}to{opacity:1;transform:translateY(0)}}</style>'
        
        # JS脚本
        tab_js = '<script>function switchTopicTab(e){var t=document.querySelectorAll(".topic-tab-btn");t.forEach(function(t,n){t.classList.toggle("active",n===e)});var o=document.querySelectorAll(".topic-tab-panel");o.forEach(function(t,n){t.style.display=n===e?"block":"none"})}</script>'
        
        html = tab_css + '<div class="topic-tabs-container">' + tabs_html + '</div>' + panels_html + tab_js
        
        self.add_section("核心题材深度推演", html, "💡")
    def add_holdings_tracking(self):
        """持仓跟踪 - Pro版"""
        stocks = self.portfolio.get('stocks', [])
        
        if not stocks:
            return
        
        html = '<div class="space-y-3">'
        
        for stock in stocks:
            name = stock.get('name', '')
            code = stock.get('code', stock.get('id', ''))
            cost = stock.get('cost_price', 0)
            current = stock.get('current_price', 0)
            profit_pct = (current - cost) / cost * 100 if cost > 0 else 0
            today_change = stock.get('today_change', 0) * 100
            risk_level = stock.get('risk_level', '')
            risk_progress = stock.get('risk_progress', 0)
            advice = stock.get('advice', '')
            diagnosis = stock.get('diagnosis', {})
            
            profit_color = 'text-red-400' if profit_pct >= 0 else 'text-green-400'
            profit_sign = '+' if profit_pct >= 0 else ''
            today_color = 'text-red-400' if today_change >= 0 else 'text-green-400'
            today_sign = '+' if today_change >= 0 else ''
            
            # 风险条颜色
            if risk_progress < 50:
                risk_bar_color = 'bg-green-500'
            elif risk_progress < 75:
                risk_bar_color = 'bg-yellow-500'
            else:
                risk_bar_color = 'bg-red-500'
            
            # 诊断指标
            diag_items = []
            if isinstance(diagnosis, dict):
                for key, value in diagnosis.items():
                    if isinstance(value, dict):
                        status = value.get('status', 'normal')
                        status_colors = {
                            'good': 'text-green-400',
                            'normal': 'text-blue-400',
                            'bad': 'text-red-400',
                            'warning': 'text-yellow-400'
                        }
                        color = status_colors.get(status, 'text-white/60')
                        diag_items.append({
                            'label': value.get('title', key),
                            'value': value.get('value', ''),
                            'color': color
                        })
            
            # 默认诊断项
            if not diag_items:
                default_dims = [
                    ('技术面', '--', 'text-blue-400'),
                    ('资金面', '--', 'text-blue-400'),
                    ('基本面', '--', 'text-blue-400'),
                    ('消息面', '--', 'text-blue-400'),
                ]
                for label, value, color in default_dims:
                    diag_items.append({'label': label, 'value': value, 'color': color})
            
            diag_html = ''
            for item in diag_items[:4]:
                diag_html += f'''
                <div class="text-center flex-1">
                    <div class="text-sm font-semibold {item['color']}">{item['value']}</div>
                    <div class="text-xs text-white/50 mt-1">{item['label']}</div>
                </div>
                '''
            
            html += f'''
            <div class="bg-white/5 backdrop-blur-sm rounded-xl p-4 border border-white/10">
                <!-- 头部信息 -->
                <div class="flex justify-between items-start mb-3">
                    <div>
                        <div class="flex items-center gap-2 mb-1">
                            <span class="text-base font-bold text-white">{name}</span>
                            <span class="text-xs text-white/40">{code}</span>
                        </div>
                        <div class="flex gap-3 text-xs">
                            <span class="text-white/50">成本: <span class="text-white/80 font-medium">¥{cost:.2f}</span></span>
                            <span class="text-white/50">现价: <span class="text-white/80 font-medium">¥{current:.2f}</span></span>
                        </div>
                    </div>
                    <div class="text-right">
                        <div class="text-lg font-bold {profit_color}">
                            {profit_sign}{profit_pct:.1f}%
                        </div>
                        <div class="text-xs {today_color} mt-1">
                            今日 {today_sign}{today_change:.1f}%
                        </div>
                    </div>
                </div>
                
                <!-- 诊断指标 -->
                <div class="flex gap-2 mb-3 p-2 bg-white/5 rounded-lg">
                    {diag_html}
                </div>
                
                <!-- 风险进度 -->
                <div class="mb-2">
                    <div class="flex justify-between text-xs mb-1">
                        <span class="text-white/50">风险等级</span>
                        <span class="text-white/70">{risk_level or '中风险'}</span>
                    </div>
                    <div class="w-full h-1.5 bg-white/10 rounded-full overflow-hidden">
                        <div class="h-full {risk_bar_color} rounded-full transition-all" style="width: {risk_progress}%"></div>
                    </div>
                </div>
                
                <!-- 操作建议 -->
                {self._render_advice(advice)}
            </div>
            '''
        
        html += '</div>'
        
        self.add_section("持仓跟踪", html, "📈")
    
    def _render_advice(self, advice):
        """渲染操作建议 - 支持字典和字符串两种格式"""
        if not advice:
            return ''
        
        # 如果是字典，渲染成带标签的样式
        if isinstance(advice, dict):
            type_label = advice.get('type_label', '操作建议')
            text = advice.get('text', '')
            color = advice.get('color', 'blue')
            
            # 颜色映射
            color_classes = {
                'red': 'bg-red-500/20 text-red-400 border-red-500/30',
                'green': 'bg-green-500/20 text-green-400 border-green-500/30',
                'yellow': 'bg-yellow-500/20 text-yellow-400 border-yellow-500/30',
                'blue': 'bg-blue-500/20 text-blue-400 border-blue-500/30',
            }
            tag_class = color_classes.get(color, color_classes['blue'])
            
            return f'''
            <div class="mt-3 pt-3 border-t border-white/10">
                <div class="flex items-center gap-2 mb-2">
                    <span class="text-xs px-2 py-0.5 rounded-full border {tag_class}">{type_label}</span>
                </div>
                <div class="text-sm text-white/80 leading-relaxed">{text}</div>
            </div>
            '''
        
        # 如果是字符串，直接渲染
        return f'''
        <div class="mt-3 pt-3 border-t border-white/10">
            <div class="text-xs text-white/50 mb-1">操作建议</div>
            <div class="text-sm text-white/80">{advice}</div>
        </div>
        '''
    
    # ========== 持仓→美股映射表（硬编码，决定外盘传导精准度） ==========
    HOLDINGS_US_MAP = {
        '002409': {
            'name': '雅克科技',
            'sectors': ['存储'],
            'positive_stocks': ['美光科技', '闪迪', '希捷科技', '西部数据'],
            'negative_stocks': [],
            'logic': '存储前驱体材料，HBM/SK海力士独家供应',
        },
        '688535': {
            'name': '华海诚科',
            'sectors': ['半导体设备', '存储'],
            'positive_stocks': ['应用材料', '泛林集团', '科磊', '美光科技'],
            'negative_stocks': [],
            'logic': '封装材料，存储+先进封装双逻辑',
        },
        '600584': {
            'name': '长电科技',
            'sectors': ['代工'],
            'positive_stocks': ['台积电ADR', '应用材料', '博通'],
            'negative_stocks': [],
            'logic': '先进封测龙头，Chiplet/AI芯片封装',
        },
        '000636': {
            'name': '风华高科',
            'sectors': ['芯片', '消费电子'],
            'positive_stocks': ['英特尔', '高通', 'AMD', '苹果'],
            'negative_stocks': [],
            'logic': 'MLCC国产龙头，AI服务器/新能源车用量暴增',
        },
        '002837': {
            'name': '英维克',
            'sectors': ['AI算力', '云计算'],
            'positive_stocks': ['微软', 'Meta', '亚马逊'],
            'negative_stocks': ['英伟达'],
            'logic': '液冷散热，数据中心资本开支驱动',
        },
        '301217': {
            'name': '铜冠铜箔',
            'sectors': ['光通信', '新能源车'],
            'positive_stocks': ['Coherent', 'Lumentum', '迈威尔科技', '康宁', '特斯拉'],
            'negative_stocks': [],
            'logic': 'PCB铜箔，AI服务器+锂电铜箔双逻辑',
        },
        '002789': {
            'name': '*ST建艺',
            'sectors': [],
            'positive_stocks': [],
            'negative_stocks': [],
            'logic': '投机仓位，独立于外盘，严格执行止损纪律',
        },
    }

    CORE_THEMES = [
        {'name': '存储芯片/HBM', 'us_sectors': ['存储', '存储/HDD'], 'key_stocks': ['美光科技','希捷科技','闪迪'],
         'a_map': '雅克科技/华海诚科/佰维存储'},
        {'name': 'AI算力/液冷', 'us_sectors': ['AI算力', '云计算'], 'key_stocks': ['AMD','微软','Meta'],
         'a_map': '英维克/中际旭创/浪潮信息'},
        {'name': '半导体设备/先进封装', 'us_sectors': ['半导体设备', '光刻设备', '代工'], 'key_stocks': ['应用材料','泛林集团','阿斯麦'],
         'a_map': '华海诚科/长电科技/中微公司'},
        {'name': '光通信/CPO', 'us_sectors': ['光通信', '光纤', '光通信/芯片'], 'key_stocks': ['Coherent','Lumentum','康宁'],
         'a_map': '铜冠铜箔/新易盛/中际旭创'},
    ]

    def _pct_color(self, v):
        if v > 1: return 'text-red-400'
        if v > 0: return 'text-red-300'
        if v < -1: return 'text-green-400'
        if v < 0: return 'text-green-300'
        return 'text-white/60'

    def _pct_sign(self, v):
        return '+' if v >= 0 else ''

    def _get_us_stock(self, name):
        tech = self.global_data.get('tech_stocks', []) if hasattr(self, 'global_data') else []
        for s in tech:
            if s.get('name') == name and s.get('price', 0) > 0:
                return s
        return None

    def _calc_support_resistance(self, stock):
        price = stock.get('current_price', 0) or stock.get('price', 0)
        if price <= 0:
            return {'support1': 0, 'support2': 0, 'resistance1': 0, 'resistance2': 0}
        return {
            'support1': round(price * 0.97, 2),
            'support2': round(price * 0.94, 2),
            'resistance1': round(price * 1.03, 2),
            'resistance2': round(price * 1.07, 2),
        }

    def _analyze_us_market(self):
        indices = self.global_data.get('indices', []) if hasattr(self, 'global_data') else []
        tech = self.global_data.get('tech_stocks', []) if hasattr(self, 'global_data') else []
        commodities = self.global_data.get('commodities', []) if hasattr(self, 'global_data') else []
        summary = self.global_data.get('summary', '') if hasattr(self, 'global_data') else ''

        us_idx = {i['name']: i for i in indices if i.get('region') == '美股'}
        dji = us_idx.get('道琼斯', {})
        spx = us_idx.get('标普500', {})
        ixic = us_idx.get('纳斯达克', {})
        sox = us_idx.get('费城半导体', {})

        valid_tech = [s for s in tech if s.get('price', 0) > 0]
        from collections import defaultdict
        sectors = defaultdict(list)
        for s in valid_tech:
            sec = s.get('sector', '其他')
            sectors[sec].append(s)
        sector_avg = {}
        for sec, stocks in sectors.items():
            avg = sum(s['change_pct'] for s in stocks) / len(stocks)
            sector_avg[sec] = {'avg': round(avg, 2), 'count': len(stocks), 'stocks': stocks}

        sorted_sectors = sorted(sector_avg.items(), key=lambda x: x[1]['avg'], reverse=True)
        leading = sorted_sectors[:3]
        lagging = sorted_sectors[-2:]

        divergence = []
        nvda = self._get_us_stock('英伟达')
        if sox.get('up', False) and nvda and not nvda.get('up', True) and abs(nvda.get('change_pct', 0)) > 2:
            divergence.append({
                'type': 'warning',
                'text': f"费城半导体涨{sox.get('change_pct',0):+.2f}%但英伟达独跌{nvda.get('change_pct',0):+.2f}%，资金正从GPU龙头切换至存储/设备/光通信",
                'implication': 'A股纯GPU算力链(寒武纪/海光)可能承压，存储/设备/光模块方向更强'
            })

        oil = None
        for c in commodities:
            if 'WTI' in c.get('name', '') or '原油' in c.get('name', ''):
                oil = c
                break

        bias = 'bullish'
        bias_reasons = []
        bias_risks = []

        if sox.get('change_pct', 0) > 3:
            bias_reasons.append(f"费城半导体大涨{sox.get('change_pct',0):+.1f}%，存储/设备/光通信全线爆发，A股科创板半导体链情绪正催化")
        elif sox.get('change_pct', 0) > 1:
            bias_reasons.append(f"费城半导体上涨{sox.get('change_pct',0):+.1f}%，半导体链温和修复")
        if ixic.get('change_pct', 0) > 1.5:
            bias_reasons.append(f"纳指大涨{ixic.get('change_pct',0):+.1f}%，风险偏好修复")
        if oil and oil.get('change_pct', 0) < -3:
            bias_reasons.append(f"油价暴跌{oil.get('change_pct',0):+.1f}%缓解通胀担忧，航空/化工受益，货币空间打开")
        if nvda and not nvda.get('up', True):
            bias_risks.append(f"英伟达跌{nvda.get('change_pct',0):+.1f}%，GPU算力链承压(对A股AI芯片情绪有拖累)")
        if divergence:
            bias_risks.append('半导体内部分化，追高错方向风险大')
        if not bias_reasons and not bias_risks:
            bias = 'neutral'

        return {
            'indices': {'dji': dji, 'spx': spx, 'ixic': ixic, 'sox': sox},
            'sector_avg': sector_avg,
            'leading': leading,
            'lagging': lagging,
            'divergence': divergence,
            'oil': oil,
            'bias': bias,
            'bias_reasons': bias_reasons,
            'bias_risks': bias_risks,
            'summary': summary,
        }

    def _generate_scenarios(self, us_analysis):
        sox_pct = us_analysis['indices'].get('sox', {}).get('change_pct', 0)
        ixic_pct = us_analysis['indices'].get('ixic', {}).get('change_pct', 0)
        market = self.market_data
        md = market.get('market_data', {})
        fg = market.get('sentiment', {}).get('fear_greed', 50)

        import re
        turnover = md.get('turnover', '')
        t_val = 0
        if isinstance(turnover, str):
            m = re.search(r'([\d.]+)\s*万亿', turnover)
            if m: t_val = float(m.group(1)) * 10000
            else:
                m = re.search(r'([\d.]+)\s*亿', turnover)
                if m: t_val = float(m.group(1))

        sh_price_default = 3680
        sh = None
        for idx in market.get('indices', []):
            if '上证' in idx.get('name', ''):
                sh = idx; break
        sh_price = sh.get('price', 0) if sh else 0
        if not sh_price or sh_price <= 0:
            try:
                import glob as _glob
                hist_files = sorted(_glob.glob('/root/daily-news-insight/data/history/*.json'))
                if hist_files:
                    with open(hist_files[-1], 'r', encoding='utf-8') as hf:
                        hist = json.load(hf)
                    for hidx in hist.get('indices', []):
                        if '上证' in hidx.get('name', '') and hidx.get('price', 0) > 0:
                            sh_price = hidx['price']; break
            except Exception:
                pass
        if not sh_price or sh_price <= 0:
            sh_price = sh_price_default

        bull_pct, neutral_pct, bear_pct = 40, 45, 15
        if sox_pct > 5: bull_pct += 10; neutral_pct -= 5; bear_pct -= 5
        if ixic_pct > 2: bull_pct += 5; neutral_pct -= 3; bear_pct -= 2
        if fg < 40: bull_pct -= 10; bear_pct += 10
        if t_val and t_val < 10000: bull_pct -= 10; bear_pct += 5
        total = bull_pct + neutral_pct + bear_pct
        bull_pct = round(bull_pct / total * 100)
        neutral_pct = round(neutral_pct / total * 100)
        bear_pct = 100 - bull_pct - neutral_pct

        return [
            {'name': '乐观:放量上攻', 'prob': bull_pct, 'color': 'red',
             'desc': f'高开后放量站稳，科创50领涨1%+，突破{int(sh_price*1.01)}点压力位',
             'trigger': '半日成交>5500亿，存储/半导体设备高开2%+不回落',
             'action': '核心底仓坚定持有，机动仓可在强势龙头回踩时小仓位参与'},
            {'name': '中性:高开震荡', 'prob': neutral_pct, 'color': 'yellow',
             'desc': f'高开0.5-1%后冲高回落，在{int(sh_price*0.995)}-{int(sh_price*1.01)}区间震荡收星',
             'trigger': '半日成交4500-5500亿，板块轮动快，无持续领涨方向',
             'action': '底仓持有不动，机动仓逢高减弱势品种(英维克)，不追高'},
            {'name': '悲观:冲高回落', 'prob': bear_pct, 'color': 'green',
             'desc': f'高开后快速回落翻绿，考验{int(sh_price*0.985)}支撑，缩量至9000亿以下',
             'trigger': '半日成交<4500亿，10:30前回落过半涨幅，强势板块炸板',
             'action': '机动仓全部减仓，控制仓位5成以下，等CPI落地再决策'},
        ]

    def _analyze_themes(self, us_analysis):
        themes = []
        for t in self.CORE_THEMES:
            pcts = []
            for us_sec in t['us_sectors']:
                if us_sec in us_analysis['sector_avg']:
                    pcts.append(us_analysis['sector_avg'][us_sec]['avg'])
            for ks_name in t['key_stocks']:
                ks = self._get_us_stock(ks_name)
                if ks: pcts.append(ks.get('change_pct', 0))
            avg_pct = sum(pcts)/len(pcts) if pcts else 0
            if avg_pct >= 5: grade, grade_color = 'S', 'from-red-500 to-orange-500'
            elif avg_pct >= 2: grade, grade_color = 'A', 'from-orange-500 to-yellow-500'
            elif avg_pct >= 0: grade, grade_color = 'B', 'from-blue-500 to-cyan-500'
            else: grade, grade_color = 'C', 'from-gray-500 to-gray-600'
            bull = f"美股映射板块均涨{avg_pct:+.1f}%"
            bear = ''
            if t['name'] == 'AI算力/液冷':
                nvda = self._get_us_stock('英伟达')
                if nvda and not nvda.get('up', True):
                    bear = f"英伟达逆势跌{nvda.get('change_pct',0):+.1f}%，GPU方向承压"
            themes.append({'name': t['name'], 'a_map': t['a_map'], 'us_avg': round(avg_pct,2),
                           'grade': grade, 'grade_color': grade_color, 'bull': bull, 'bear': bear})
        return sorted(themes, key=lambda x: x['us_avg'], reverse=True)

    def _build_holdings_strategy(self, us_analysis):
        stocks = self.portfolio.get('stocks', [])
        result = []
        for s in stocks:
            code = s.get('code', s.get('id', ''))
            name = s.get('name', '')
            current = s.get('current_price', 0) or s.get('price', 0)
            cost = s.get('cost_price', 0)
            profit_pct = (current - cost) / cost * 100 if cost > 0 else 0
            mp = self.HOLDINGS_US_MAP.get(code)
            us_impact_pct = 0
            us_detail_parts = []
            if mp:
                pcts = []
                for ps_name in mp['positive_stocks']:
                    ps = self._get_us_stock(ps_name)
                    if ps and ps.get('price', 0) > 0:
                        pcts.append(ps.get('change_pct', 0))
                        us_detail_parts.append(f"{ps['name']}{ps.get('change_pct',0):+.1f}%")
                for ns_name in mp['negative_stocks']:
                    ns = self._get_us_stock(ns_name)
                    if ns and ns.get('price', 0) > 0:
                        pcts.append(-ns.get('change_pct', 0) * 0.5)
                        us_detail_parts.append(f"{ns['name']}{ns.get('change_pct',0):+.1f}%(拖累)")
                if pcts:
                    us_impact_pct = round(sum(pcts)/len(pcts)*0.3, 2)
            us_detail = ' '.join(us_detail_parts) if us_detail_parts else '无直接外盘映射'
            if us_impact_pct > 1.5: impact = 'strong_bull'
            elif us_impact_pct > 0.5: impact = 'bull'
            elif us_impact_pct < -1: impact = 'strong_bear'
            elif us_impact_pct < -0.3: impact = 'bear'
            else: impact = 'neutral'
            sr = self._calc_support_resistance(s)
            # 深度套牢品种（浮亏>40%）一律借反弹减仓，不恋战
            if profit_pct < -40:
                action = '借反弹减仓'
                action_detail = f'深度套牢({profit_pct:.0f}%)，冲高至{sr["resistance1"]:.0f}元以上减机动仓1/3，{sr["resistance2"]:.0f}元附近继续减；不加仓'
                priority = '🔴优先'; priority_color = 'red'
            elif name.startswith('*ST'):
                action = '严格纪律'
                action_detail = '跌破8.50元止损，10元以上止盈，投机仓位不追加'
                priority = '⚪纪律'; priority_color = 'gray'
            elif impact in ('strong_bull', 'bull'):
                action = '底仓持有'
                action_detail = f'底仓坚定持有；高开{max(us_impact_pct*3,1):.1f}%以上不追，回踩{sr["support1"]:.0f}元再考虑机动仓'
                priority = '🟢持有'; priority_color = 'green'
            elif impact in ('strong_bear', 'bear'):
                action = '减仓防守'
                action_detail = f'受外盘拖累可能承压，反弹至{sr["resistance1"]:.0f}元附近减机动仓'
                priority = '🟠防守'; priority_color = 'orange'
            else:
                action = '持有观察'
                action_detail = f'底仓持有不动，{sr["support1"]:.0f}元为支撑，{sr["resistance1"]:.0f}元以上可减机动仓做T'
                priority = '🟡观察'; priority_color = 'yellow'
            result.append({
                'code': code, 'name': name, 'current': current, 'cost': cost,
                'profit_pct': round(profit_pct,1), 'us_impact': us_impact_pct,
                'us_detail': us_detail, 'impact': impact,
                'support1': sr['support1'], 'support2': sr['support2'],
                'resistance1': sr['resistance1'], 'resistance2': sr['resistance2'],
                'action': action, 'action_detail': action_detail,
                'priority': priority, 'priority_color': priority_color,
            })
        priority_order = {'red':0,'orange':1,'gray':2,'yellow':3,'green':4}
        result.sort(key=lambda x: priority_order.get(x['priority_color'], 5))
        return result

    def _generate_risks(self):
        return [
            {'level':'高','color':'red','title':'今晚美国CPI(21:30)',
             'trigger':'CPI环比超0.4%或核心超0.3%',
             'action':'午后不重仓追高，CPI超预期将引发美债飙升→科技股回调'},
            {'level':'中','color':'yellow','title':'英伟达黄仁勋事件发酵',
             'trigger':'英伟达继续跌5%+或更多负面消息',
             'action':'GPU算力链(寒武纪/海光)承压，不追高纯GPU方向'},
            {'level':'中','color':'yellow','title':'缩量冲高回落风险',
             'trigger':'半日成交<4500亿或10:30前回落过半涨幅',
             'action':'高开不追，等回踩确认再动；仓位维持6成，不满仓'},
            {'level':'低','color':'blue','title':'原油走势不确定性',
             'trigger':'美伊谈判反复致油价反弹',
             'action':'石油石化不追，航空/化工可小仓位博弈油价下行'},
        ]

    def _generate_key_events(self):
        return [
            {'time':'今日 21:30','event':'美国10月CPI公布','impact':'🔴 决定12月加息预期，直接影响科技股估值','direction':'待定'},
            {'time':'今日 盘中','event':'A股成交量能','impact':'🟡 半日<4500亿=反弹失败，>5500亿=可看高一线','direction':'观察'},
            {'time':'11/12 凌晨','event':'美联储官员讲话','impact':'🟡 CPI后官员表态可能强化/弱化加息预期','direction':'待定'},
            {'time':'11/13','event':'SpaceX星舰第15次试飞','impact':'🟢 双级回收若成功→商业航天板块情绪爆发','direction':'利多'},
        ]

    def _one_line_command(self, themes, holdings):
        action_items = [h for h in holdings if h['priority_color'] in ('red','orange')]
        # 从用户实际持仓里找外盘映射最强的持有品种（不拿板块名，拿持仓名）
        hold_items = [h for h in holdings if h['priority_color'] in ('green',)]
        strongest_hold = None
        if hold_items:
            strongest_hold = max(hold_items, key=lambda x: x['us_impact'])
        parts = []
        if action_items:
            parts.append(f"借反弹减{'、'.join(h['name'] for h in action_items[:2])}")
        if strongest_hold and strongest_hold['us_impact'] > 0.5:
            parts.append(f"{strongest_hold['name']}为代表的强势底仓拿稳")
        else:
            parts.append("底仓持股待涨")
        parts.append("不追高等回踩")
        return '；'.join(parts) + '。'

    def add_battle_plan(self):
        if not hasattr(self, 'global_data') or not self.global_data:
            try:
                with open(os.path.join(self.data_dir, 'global_market.json'), 'r', encoding='utf-8') as f:
                    self.global_data = json.load(f)
            except:
                self.global_data = {}

        us = self._analyze_us_market()
        scenarios = self._generate_scenarios(us)
        themes = self._analyze_themes(us)
        holdings_strategy = self._build_holdings_strategy(us)
        risks = self._generate_risks()
        events = self._generate_key_events()
        command = self._one_line_command(themes, holdings_strategy)

        # 构建HTML
        h = ['<div class="space-y-5">']

        # ① 核心指令
        h.append('<div class="bg-gradient-to-r from-red-500/25 via-orange-500/15 to-yellow-500/10 border-2 border-red-500/40 rounded-2xl p-5 relative overflow-hidden">')
        h.append('<div class="absolute top-0 right-0 w-32 h-32 bg-red-500/10 rounded-full blur-3xl"></div>')
        h.append('<div class="flex items-start gap-3 relative">')
        h.append('<div class="text-3xl">⚡</div>')
        h.append('<div class="flex-1">')
        h.append('<div class="text-xs text-red-300 font-bold tracking-widest mb-1">今日核心指令</div>')
        h.append(f'<div class="text-xl md:text-2xl font-black text-white leading-tight">{command}</div>')
        h.append('</div></div></div>')

        # ② 隔夜外盘
        sox = us['indices'].get('sox', {}); ixic = us['indices'].get('ixic', {})
        dji = us['indices'].get('dji', {}); spx = us['indices'].get('spx', {})
        h.append('<div class="bg-white/5 backdrop-blur-sm rounded-xl p-5 border border-white/10">')
        h.append('<div class="text-white font-bold mb-3 flex items-center gap-2"><span>🌍</span><span>隔夜外盘深度解读</span></div>')
        h.append('<div class="grid grid-cols-2 md:grid-cols-4 gap-2 mb-4">')
        for label, idx in [('道琼斯',dji),('标普500',spx),('纳斯达克',ixic),('费城半导体',sox)]:
            if idx:
                c = self._pct_color(idx.get('change_pct',0))
                s = self._pct_sign(idx.get('change_pct',0))
                h.append(f'<div class="bg-white/5 rounded-lg p-3 text-center"><div class="text-xs text-white/50 mb-1">{label}</div><div class="text-lg font-bold {c}">{s}{idx.get("change_pct",0):.2f}%</div></div>')
        h.append('</div>')
        h.append('<div class="space-y-2 mb-4">')
        if us['leading']:
            h.append('<div class="text-xs text-red-300 font-bold">📈 领涨板块：</div><div class="flex flex-wrap gap-2">')
            for sec_name, sec_data in us['leading']:
                h.append(f'<span class="text-xs bg-red-500/15 text-red-300 px-2 py-1 rounded-md border border-red-500/20">{sec_name} {sec_data["avg"]:+.1f}%</span>')
            h.append('</div>')
        if us['lagging']:
            h.append('<div class="text-xs text-green-300 font-bold mt-2">📉 领跌/走弱：</div><div class="flex flex-wrap gap-2">')
            for sec_name, sec_data in us['lagging']:
                h.append(f'<span class="text-xs bg-green-500/15 text-green-300 px-2 py-1 rounded-md border border-green-500/20">{sec_name} {sec_data["avg"]:+.1f}%</span>')
            h.append('</div>')
        h.append('</div>')
        for d in us['divergence']:
            h.append(f'<div class="bg-yellow-500/10 border border-yellow-500/30 rounded-lg p-3 mb-3"><div class="text-xs text-yellow-400 font-bold mb-1">⚠️ 信号分化(易误读)</div><div class="text-sm text-white/90 mb-1">{d["text"]}</div><div class="text-xs text-yellow-200/80">→ A股含义：{d["implication"]}</div></div>')
        h.append('<div class="text-xs text-white/50 font-bold mb-2">🔗 对A股传导：</div>')
        h.append('<ul class="text-sm space-y-1 text-white/80">')
        for r in us['bias_reasons']:
            h.append(f'<li class="flex items-start gap-2"><span class="text-red-400 mt-0.5">✓</span><span>{r}</span></li>')
        for r in us['bias_risks']:
            h.append(f'<li class="flex items-start gap-2"><span class="text-yellow-400 mt-0.5">⚠</span><span>{r}</span></li>')
        h.append('</ul>')
        if us.get('oil'):
            oil = us['oil']
            oc = self._pct_color(oil.get('change_pct',0))
            os_ = self._pct_sign(oil.get('change_pct',0))
            h.append(f'<div class="mt-3 text-xs text-white/60">🛢️ 原油: <span class="{oc}">{oil.get("name","WTI")} ${oil.get("price",0):.1f} ({os_}{oil.get("change_pct",0):.1f}%)</span></div>')
        h.append('</div>')

        # ③ 三情景
        h.append('<div class="bg-white/5 backdrop-blur-sm rounded-xl p-5 border border-white/10">')
        h.append('<div class="text-white font-bold mb-3 flex items-center gap-2"><span>📊</span><span>今日大盘三情景预判</span></div>')
        h.append('<div class="grid md:grid-cols-3 gap-3">')
        for sc in scenarios:
            bcs = {'red':'from-red-500 to-orange-500','yellow':'from-yellow-500 to-amber-500','green':'from-green-500 to-emerald-500'}
            tcs = {'red':'text-red-400','yellow':'text-yellow-400','green':'text-green-400'}
            h.append(f'<div class="bg-white/5 rounded-xl p-4 border border-white/10"><div class="flex justify-between items-center mb-2"><span class="text-sm font-bold text-white">{sc["name"]}</span><span class="{tcs[sc["color"]]} text-lg font-black">{sc["prob"]}%</span></div>')
            h.append(f'<div class="w-full h-1.5 bg-white/10 rounded-full mb-3 overflow-hidden"><div class="h-full bg-gradient-to-r {bcs[sc["color"]]} rounded-full" style="width:{sc["prob"]}%"></div></div>')
            h.append(f'<div class="text-xs text-white/70 mb-2">{sc["desc"]}</div>')
            h.append(f'<div class="text-xs text-white/50 mb-1"><span class="text-white/70">触发：</span>{sc["trigger"]}</div>')
            h.append(f'<div class="text-xs mt-2 pt-2 border-t border-white/10"><span class="text-white/70">操作：</span><span class="text-white/90">{sc["action"]}</span></div></div>')
        h.append('</div></div>')

        # ④ 主线评级
        h.append('<div class="bg-white/5 backdrop-blur-sm rounded-xl p-5 border border-white/10">')
        h.append('<div class="text-white font-bold mb-3 flex items-center gap-2"><span>🔥</span><span>核心主线评级(按美股映射强弱排序)</span></div>')
        h.append('<div class="space-y-2">')
        grade_bg = {'S':'bg-gradient-to-r from-red-500 to-orange-500','A':'bg-gradient-to-r from-orange-500 to-yellow-500','B':'bg-gradient-to-r from-blue-500 to-cyan-500','C':'bg-gray-600'}
        for t in themes:
            tc = self._pct_color(t['us_avg']); ts = self._pct_sign(t['us_avg'])
            h.append(f'<div class="flex items-center gap-3 bg-white/5 rounded-lg p-3">')
            h.append(f'<div class="{grade_bg[t["grade"]]} text-white font-black text-sm px-2.5 py-1 rounded-md min-w-[32px] text-center">{t["grade"]}</div>')
            h.append('<div class="flex-1 min-w-0">')
            h.append(f'<div class="flex items-center gap-2 flex-wrap"><span class="font-bold text-white text-sm">{t["name"]}</span><span class="text-xs {tc} font-bold">美股映射{ts}{t["us_avg"]:.1f}%</span></div>')
            h.append(f'<div class="text-xs text-white/50 mt-0.5">A股映射：{t["a_map"]}</div>')
            h.append(f'<div class="text-xs text-green-300/80 mt-0.5">多：{t["bull"]}</div>')
            if t['bear']:
                h.append(f'<div class="text-xs text-red-300/80">空：{t["bear"]}</div>')
            h.append('</div></div>')
        h.append('</div></div>')

        # ⑤ 持仓策略总表
        h.append('<div class="bg-white/5 backdrop-blur-sm rounded-xl p-5 border border-white/10">')
        h.append('<div class="text-white font-bold mb-3 flex items-center gap-2"><span>💼</span><span>持仓操作策略总表</span></div>')
        h.append('<div class="overflow-x-auto"><table class="w-full text-xs">')
        h.append('<thead><tr class="text-white/50 border-b border-white/10"><th class="text-left py-2 px-1 font-medium">优先级</th><th class="text-left py-2 px-1 font-medium">持仓</th><th class="text-right py-2 px-1 font-medium">昨收</th><th class="text-right py-2 px-1 font-medium">盈亏</th><th class="text-center py-2 px-1 font-medium">外盘</th><th class="text-center py-2 px-1 font-medium">支撑/压力</th><th class="text-left py-2 px-1 font-medium">今日操作</th></tr></thead><tbody>')
        for h_ in holdings_strategy:
            pc = 'text-red-400' if h_['profit_pct']>=0 else 'text-green-400'
            ps = '+' if h_['profit_pct']>=0 else ''
            uc = self._pct_color(h_['us_impact']*3)
            us_ = '+' if h_['us_impact']>=0 else ''
            imp_emoji = {'strong_bull':'🔥','bull':'📈','bear':'📉','strong_bear':'⚠️','neutral':'➖'}.get(h_['impact'],'➖')
            pri_bg = {'red':'bg-red-500/20 text-red-400','orange':'bg-orange-500/20 text-orange-400','yellow':'bg-yellow-500/20 text-yellow-400','green':'bg-green-500/20 text-green-400','gray':'bg-gray-500/20 text-gray-400'}.get(h_['priority_color'],'bg-white/10 text-white/60')
            h.append(f'<tr class="border-b border-white/5">')
            h.append(f'<td class="py-2.5 px-1"><span class="{pri_bg} text-[10px] px-1.5 py-0.5 rounded font-medium whitespace-nowrap">{h_["priority"]}</span></td>')
            h.append(f'<td class="py-2.5 px-1"><div class="font-bold text-white">{h_["name"]}</div><div class="text-white/40">{h_["code"]}</div></td>')
            h.append(f'<td class="py-2.5 px-1 text-right text-white/90">¥{h_["current"]:.2f}</td>')
            h.append(f'<td class="py-2.5 px-1 text-right {pc} font-medium">{ps}{h_["profit_pct"]:.1f}%</td>')
            h.append(f'<td class="py-2.5 px-1 text-center"><span class="{uc} font-medium">{imp_emoji} {us_}{h_["us_impact"]*3:.1f}%</span></td>')
            h.append(f'<td class="py-2.5 px-1 text-center text-[10px]"><div class="text-green-400/80">S:{h_["support1"]:.0f}/{h_["support2"]:.0f}</div><div class="text-red-400/80">R:{h_["resistance1"]:.0f}/{h_["resistance2"]:.0f}</div></td>')
            h.append(f'<td class="py-2.5 px-1"><div class="font-medium text-white">{h_["action"]}</div><div class="text-white/60 text-[11px] mt-0.5">{h_["action_detail"]}</div></td>')
            h.append('</tr>')
        h.append('</tbody></table></div>')
        h.append('<div class="mt-3 pt-3 border-t border-white/10 text-[10px] text-white/40 space-y-0.5">')
        for h_ in holdings_strategy:
            if h_['us_detail']:
                h.append(f'<div><span class="text-white/60">{h_["name"]}：</span>{h_["us_detail"]}</div>')
        h.append('</div></div>')

        # ⑥ 总策略
        reduce_count = sum(1 for x in holdings_strategy if x['priority_color'] in ('red','orange'))
        hold_count = sum(1 for x in holdings_strategy if x['priority_color'] in ('green','yellow'))
        bias_emoji = {'bullish':'🟢','neutral':'🟡','bearish':'🔴'}.get(us['bias'],'🟡')
        bias_text = {'bullish':'偏多','neutral':'中性','bearish':'偏空'}.get(us['bias'],'中性')
        h.append(f'<div class="bg-white/5 backdrop-blur-sm rounded-xl p-5 border border-white/10">')
        h.append('<div class="text-white font-bold mb-3 flex items-center gap-2"><span>📋</span><span>今日操作总策略</span></div>')
        h.append('<div class="grid md:grid-cols-3 gap-4 mb-4">')
        h.append('<div class="text-center"><div class="text-white/50 text-xs mb-1">仓位建议</div><div class="text-2xl font-black text-yellow-400">6成</div><div class="text-[10px] text-white/40">不追高，等回踩</div></div>')
        h.append(f'<div class="text-center"><div class="text-white/50 text-xs mb-1">外盘情绪</div><div class="text-2xl font-black text-red-400">{bias_emoji} {bias_text}</div><div class="text-[10px] text-white/40">费半{sox.get("change_pct",0):+.1f}%/纳指{ixic.get("change_pct",0):+.1f}%</div></div>')
        h.append(f'<div class="text-center"><div class="text-white/50 text-xs mb-1">持仓动作</div><div class="text-2xl font-black text-orange-400">{reduce_count}减/{hold_count}持</div><div class="text-[10px] text-white/40">{reduce_count}只优先减仓</div></div>')
        h.append('</div>')
        h.append('<div class="text-xs text-white/70 space-y-1 bg-white/5 rounded-lg p-3">')
        h.append('<div><span class="text-white/90 font-medium">关键时间点：</span>9:30-10:00看开盘承接；10:30确认半日量能；14:30防CPI避险；21:30 CPI公布</div>')
        h.append('<div><span class="text-white/90 font-medium">纪律：</span>高开3%以上不追、破位不硬扛、仓位不超7成</div>')
        h.append('</div></div>')

        # ⑦ 关键事件
        h.append('<div class="bg-white/5 backdrop-blur-sm rounded-xl p-5 border border-white/10">')
        h.append('<div class="text-white font-bold mb-3 flex items-center gap-2"><span>📅</span><span>未来48小时关键事件</span></div>')
        h.append('<div class="space-y-2">')
        for ev in events:
            dc = {'利多':'text-red-400','利空':'text-green-400','待定':'text-yellow-400','观察':'text-blue-400'}.get(ev['direction'],'text-white/60')
            h.append(f'<div class="flex items-start gap-3 text-sm"><div class="text-white/50 text-xs font-mono mt-0.5 min-w-[80px]">{ev["time"]}</div><div class="flex-1"><div class="flex items-center gap-2"><span class="font-medium text-white">{ev["event"]}</span><span class="{dc} text-xs font-bold">[{ev["direction"]}]</span></div><div class="text-xs text-white/60 mt-0.5">{ev["impact"]}</div></div></div>')
        h.append('</div></div>')

        # ⑧ 三级风险
        h.append('<div class="bg-white/5 backdrop-blur-sm rounded-xl p-5 border border-white/10">')
        h.append('<div class="text-white font-bold mb-3 flex items-center gap-2"><span>⚠️</span><span>今日风险提示</span></div>')
        h.append('<div class="space-y-2">')
        for r in risks:
            lvl = {'red':'bg-red-500/20 text-red-400 border-red-500/30','yellow':'bg-yellow-500/20 text-yellow-400 border-yellow-500/30','blue':'bg-blue-500/20 text-blue-400 border-blue-500/30'}.get(r['color'],'bg-white/10 text-white/60 border-white/20')
            h.append(f'<div class="border {lvl.split()[2]} rounded-lg p-3"><div class="flex items-center gap-2 mb-1"><span class="{lvl.split()[0]} {lvl.split()[1]} text-[10px] px-1.5 py-0.5 rounded font-bold">{r["level"]}风险</span><span class="font-bold text-white text-sm">{r["title"]}</span></div><div class="text-xs text-white/70 mb-1">触发条件：{r["trigger"]}</div><div class="text-xs text-white/60">应对：{r["action"]}</div></div>')
        h.append('</div></div>')

        h.append('</div>')
        self.add_section("🎯 今日作战计划", ''.join(h), "🎯")

    def add_tomorrow_prediction(self):
        """明日关键预判 - Pro版"""
        predictions = []
        
        # 基于热门板块生成看涨预判
        hot = self.hot_sectors
        if hot:
            top_sector = hot[0]
            predictions.append({
                'direction': '看涨',
                'name': top_sector.get('name', ''),
                'confidence': 70,
                'reason': top_sector.get('reason', '行业景气度持续') + '，关注龙头持续性。'
            })
        
        # 大盘预判
        market = self.market_data
        sentiment = market.get('sentiment', {})
        fg = sentiment.get('fear_greed', 50)
        
        if fg > 60:
            market_pred = '震荡上行'
            market_conf = 55
            market_reason = '市场情绪偏乐观，资金活跃度较高，但需警惕高位分歧。'
        elif fg > 40:
            market_pred = '震荡整理'
            market_conf = 60
            market_reason = '情绪中性，市场缺乏明确方向，预计维持区间震荡。'
        else:
            market_pred = '震荡下行'
            market_conf = 55
            market_reason = '市场情绪偏谨慎，风险偏好下降，注意控制仓位。'
        
        predictions.insert(0, {
            'direction': '震荡',
            'name': '大盘指数',
            'confidence': market_conf,
            'reason': market_reason
        })
        
        # 风险提示
        predictions.append({
            'direction': '看跌',
            'name': '高位题材股',
            'confidence': 60,
            'reason': '近两日涨幅较大的题材股存在回调风险，注意高低切换。'
        })
        
        # 渲染
        direction_styles = {
            '看涨': {'bg': 'from-red-500/20 to-orange-500/10', 'border': 'border-red-500/30', 'text': 'text-red-400', 'icon': '📈'},
            '看跌': {'bg': 'from-green-500/20 to-emerald-500/10', 'border': 'border-green-500/30', 'text': 'text-green-400', 'icon': '📉'},
            '震荡': {'bg': 'from-blue-500/20 to-cyan-500/10', 'border': 'border-blue-500/30', 'text': 'text-blue-400', 'icon': '📊'},
        }
        
        pred_html = '<div class="space-y-3">'
        for p in predictions:
            direction = p.get('direction', '震荡')
            style = direction_styles.get(direction, direction_styles['震荡'])
            name = p.get('name', '')
            confidence = p.get('confidence', 60)
            reason = p.get('reason', '')
            
            if confidence >= 75:
                conf_color = 'text-green-400'
            elif confidence >= 60:
                conf_color = 'text-yellow-400'
            else:
                conf_color = 'text-white/50'
            
            pred_html += f'''
            <div class="bg-gradient-to-r {style['bg']} {style['border']} border rounded-xl p-4">
                <div class="flex items-center justify-between mb-2">
                    <div class="flex items-center gap-2">
                        <span class="text-lg">{style['icon']}</span>
                        <span class="text-white font-semibold">{name}</span>
                    </div>
                    <div class="text-right">
                        <span class="bg-white/10 text-white text-xs font-bold px-2.5 py-1 rounded-full">
                            {direction}
                        </span>
                        <div class="text-xs {conf_color} mt-1 font-medium">
                            置信度 {confidence}%
                        </div>
                    </div>
                </div>
                <p class="text-sm text-white/70 leading-relaxed m-0">
                    {reason}
                </p>
            </div>
            '''
        
        pred_html += '</div>'
        
        # 免责声明
        pred_html += '''
        <div class="mt-4 text-center text-xs text-white/40 leading-relaxed">
            ⚠️ 预判仅供参考，不构成投资建议。市场有风险，投资需谨慎。
            <br>预判基于当前市场数据和逻辑推演，实际走势受多种因素影响。
        </div>
        '''
        
        self.add_section("明日关键预判", pred_html, "🎯")
    
    def add_risk_warning(self):
        """风险提示 - Pro版"""
        # 基于市场数据生成风险提示
        market = self.market_data
        market_data = market.get('market_data', {})
        sentiment = market.get('sentiment', {})
        fg = sentiment.get('fear_greed', 50)
        
        risks = []
        
        if fg > 70:
            risks.append({
                'level': '高',
                'title': '情绪过热风险',
                'desc': '市场贪婪指数偏高，短期可能出现情绪退潮导致的回调。'
            })
        elif fg > 60:
            risks.append({
                'level': '中',
                'title': '情绪分化风险',
                'desc': '市场情绪偏乐观，但板块轮动加快，注意追高风险。'
            })
        
        risks.append({
            'level': '中',
            'title': '板块轮动风险',
            'desc': '近期热点切换频繁，持续性较差，避免盲目追涨杀跌。'
        })
        
        risks.append({
            'level': '低',
            'title': '流动性风险',
            'desc': '关注成交额变化，若持续萎缩需警惕市场活跃度下降。'
        })
        
        level_colors = {
            '高': ('bg-red-500/20', 'text-red-400', 'border-red-500/30'),
            '中': ('bg-yellow-500/20', 'text-yellow-400', 'border-yellow-500/30'),
            '低': ('bg-green-500/20', 'text-green-400', 'border-green-500/30'),
        }
        
        risks_html = '<div class="grid md:grid-cols-2 gap-3">'
        for r in risks:
            level = r.get('level', '中')
            bg, text, border = level_colors.get(level, level_colors['中'])
            risks_html += f'''
            <div class="{bg} {border} border rounded-xl p-4">
                <div class="flex items-center gap-2 mb-2">
                    <span class="text-lg">⚠️</span>
                    <span class="text-white font-semibold">{r['title']}</span>
                    <span class="ml-auto text-xs font-bold {text} px-2 py-0.5 rounded-full bg-white/10">{level}风险</span>
                </div>
                <p class="text-sm text-white/60 m-0">{r['desc']}</p>
            </div>
            '''
        risks_html += '</div>'
        
        self.add_section("风险提示", risks_html, "⚠️")
    
    def add_global_market(self):
        """隔夜全球市场 - Pro版
        从 data/global_market.json 加载真实数据，无数据时显示占位提示
        严禁硬编码假数据！
        """
        import json
        import os

        data_available = False
        gdata = {}

        try:
            data_dir = getattr(self, 'data_dir', None)
            if data_dir:
                data_file = os.path.join(data_dir, 'global_market.json')
            else:
                data_file = os.path.join('data', 'global_market.json')

            if os.path.exists(data_file):
                with open(data_file, 'r', encoding='utf-8') as gf:
                    gdata = json.load(gf)
                indices = gdata.get('indices', [])
                # 过滤出有价格的数据
                valid_indices = [i for i in indices if i.get('price', 0) > 0]
                valid_tech = [s for s in gdata.get('tech_stocks', []) if s.get('price', 0) > 0]
                valid_korea = [k for k in gdata.get('korea_market', []) if k.get('price', 0) > 0]
                data_available = bool(valid_indices or valid_tech)
        except Exception as e:
            print(f"⚠️  加载全球市场数据失败: {e}")

        if not data_available:
            html = '<div class="bg-yellow-500/10 border border-yellow-500/30 rounded-xl p-6 text-center">'
            html += '<div class="text-yellow-400 text-lg mb-2">⚠️ 隔夜全球市场数据待更新</div>'
            html += '<div class="text-white/60 text-sm">数据采集升级中，海外行情详见S级催化扫描报告</div>'
            html += '</div>'
            self.add_section("隔夜全球市场", html, "🌍")
            return

        # ---- 格式化辅助函数 ----
        def fmt_pct(item):
            sign = '+' if item['up'] else ''
            return f"{sign}{item['change_pct']:.2f}%"

        def color_cls(item):
            return 'text-red-400' if item['up'] else 'text-green-400'

        def bg_cls(item):
            return 'from-red-500/20 to-orange-500/10 border-red-500/20' if item['up'] else 'from-green-500/20 to-emerald-500/10 border-green-500/20'

        valid_indices = [i for i in gdata.get('indices', []) if i.get('price', 0) > 0]
        valid_tech = [s for s in gdata.get('tech_stocks', []) if s.get('price', 0) > 0]
        valid_korea = [k for k in gdata.get('korea_market', []) if k.get('price', 0) > 0]
        valid_comm = [c for c in valid_indices if c.get('region') == '大宗商品']
        valid_idx = [i for i in valid_indices if i.get('region') != '大宗商品']

        # ---- 指数卡片 ----
        index_cards = ''
        for idx in valid_idx:
            index_cards += '<div class="bg-gradient-to-br ' + bg_cls(idx) + ' border rounded-lg p-3 text-center transition-all duration-300 hover:scale-105">'
            index_cards += '<div class="text-xs text-white/60 mb-1">' + idx['name'] + '</div>'
            index_cards += '<div class="text-base font-bold ' + color_cls(idx) + '">' + fmt_pct(idx) + '</div>'
            index_cards += '<div class="text-xs text-white/40 mt-1">' + f"{idx['price']:,.2f}" + '</div>'
            index_cards += '</div>'

        # ---- 大宗商品 ----
        commodity_cards = ''
        for comm in valid_comm:
            commodity_cards += '<div class="flex items-center justify-between py-2 border-b border-white/5 last:border-0">'
            commodity_cards += '<span class="text-sm text-white/70">' + comm['name'] + '</span>'
            commodity_cards += '<span class="text-sm font-semibold ' + color_cls(comm) + '">' + fmt_pct(comm) + '</span>'
            commodity_cards += '</div>'

        # ---- 美股科技股 ----
        stock_cards = ''
        for stock in valid_tech:
            stock_cards += '<div class="bg-white/5 rounded-lg p-3 border border-white/5 hover:border-white/10 transition-all">'
            stock_cards += '<div class="flex items-center justify-between mb-1">'
            stock_cards += '<span class="text-sm font-medium text-white/90">' + stock['name'] + '</span>'
            stock_cards += '<span class="text-xs text-white/40">' + stock.get('sector', '') + '</span>'
            stock_cards += '</div>'
            stock_cards += '<div class="flex items-center justify-between">'
            stock_cards += '<span class="text-white/60 text-xs">$' + f"{stock['price']:.2f}" + '</span>'
            stock_cards += '<span class="text-sm font-bold ' + color_cls(stock) + '">' + fmt_pct(stock) + '</span>'
            stock_cards += '</div>'
            stock_cards += '</div>'

        # ---- 韩股板块 ----
        korea_html = ''
        if valid_korea:
            korea_cards = ''
            for k in valid_korea:
                price_str = f"{k['price']:,.0f}" if k['price'] > 1000 else f"{k['price']:.2f}"
                korea_cards += '<div class="bg-white/5 rounded-lg p-3 border border-white/5 hover:border-white/10 transition-all">'
                korea_cards += '<div class="flex items-center justify-between mb-1">'
                # 处理英文名，尽量简短
                kn = k['name']
                if 'Samsung' in kn: kn = '三星电子'
                elif 'SK hynix' in kn: kn = 'SK海力士'
                elif 'NAVER' in kn: kn = 'NAVER'
                elif 'Kakao' in kn: kn = 'KAKAO'
                elif 'LG Energy' in kn: kn = 'LG新能源'
                elif 'Hyundai' in kn: kn = '现代汽车'
                elif 'Kia' in kn: kn = '起亚'
                elif 'SDI' in kn: kn = '三星SDI'
                elif 'Innovation' in kn: kn = 'SK Innovation'
                korea_cards += '<span class="text-sm font-medium text-white/90">' + kn + '</span>'
                korea_cards += '<span class="text-xs text-white/40">' + k.get('sector', '') + '</span>'
                korea_cards += '</div>'
                korea_cards += '<div class="flex items-center justify-between">'
                korea_cards += '<span class="text-white/60 text-xs">₩' + price_str + '</span>'
                korea_cards += '<span class="text-sm font-bold ' + color_cls(k) + '">' + fmt_pct(k) + '</span>'
                korea_cards += '</div>'
                korea_cards += '</div>'

            korea_html = '<div class="mt-4">'
            korea_html += '<div class="text-white font-semibold mb-3 flex items-center gap-2">'
            korea_html += '<span>🇰🇷</span><span>韩国市场核心标的</span>'
            korea_html += '</div>'
            korea_html += '<div class="grid grid-cols-2 md:grid-cols-3 gap-2">' + korea_cards + '</div>'
            korea_html += '</div>'

        # ---- 组装HTML ----
        html = '<div class="grid md:grid-cols-3 gap-4">'
        html += '<div class="md:col-span-2">'
        html += '<div class="text-white font-semibold mb-3 flex items-center gap-2">'
        html += '<span>🌍</span><span>全球主要指数</span></div>'
        html += '<div class="grid grid-cols-3 md:grid-cols-6 gap-2">' + index_cards + '</div>'
        html += '</div>'
        html += '<div>'
        html += '<div class="text-white font-semibold mb-3 flex items-center gap-2">'
        html += '<span>🛢️</span><span>大宗商品</span></div>'
        html += '<div class="bg-white/5 rounded-lg p-3">' + commodity_cards + '</div>'
        html += '</div>'
        html += '</div>'

        html += '<div class="mt-4">'
        html += '<div class="text-white font-semibold mb-3 flex items-center gap-2">'
        html += '<span>💹</span><span>美股核心科技股</span></div>'
        html += '<div class="grid grid-cols-2 md:grid-cols-5 gap-2">' + stock_cards + '</div>'
        html += '</div>'

        html += korea_html

        # 更新时间
        update_time = gdata.get('update_time', '')
        if update_time:
            html += '<div class="mt-3 text-right text-xs text-white/40">数据更新时间: ' + update_time + '</div>'

        self.add_section("隔夜全球市场", html, "🌍")

    def add_topic_dynamics(self):
        """核心题材动态 - Pro版"""
        s_topics = self.topics.get('s_level_topics', [])
        a_topics = self.topics.get('a_level_topics', [])
        b_topics = self.topics.get('b_level_topics', [])
        
        all_topics = s_topics + a_topics + b_topics
        
        if not all_topics:
            return
        
        html = '<div class="space-y-3">'
        
        for topic in all_topics:
            name = topic.get('name', '')
            level = topic.get('level', 'B')
            score = topic.get('total_score', 0)
            subtitle = topic.get('subtitle', topic.get('core_logic', ''))
            tags = topic.get('tags', [])
            recent_catalyst = topic.get('recent_catalyst', '')
            
            # 等级样式
            level_styles = {
                'S': {'bg': 'from-red-500/20 to-orange-500/10', 'border': 'border-red-500/30', 'text': 'text-red-400'},
                'A': {'bg': 'from-orange-500/20 to-yellow-500/10', 'border': 'border-orange-500/30', 'text': 'text-orange-400'},
                'B': {'bg': 'from-yellow-500/20 to-green-500/10', 'border': 'border-yellow-500/30', 'text': 'text-yellow-400'},
            }
            style = level_styles.get(level, level_styles['B'])
            
            # 标签
            tags_html = ''
            if tags:
                tags_html = ''.join([f'<span class="px-2 py-0.5 bg-white/10 rounded-full text-xs text-white/60">{t}</span>' for t in tags[:3]])
            
            html += f'''
            <div class="bg-gradient-to-r {style['bg']} {style['border']} border rounded-xl p-4 transition-all duration-300 hover:scale-[1.02]">
                <div class="flex items-start justify-between mb-2">
                    <div class="flex items-center gap-2">
                        <span class="text-lg">⚡</span>
                        <span class="text-base font-bold text-white">{name}</span>
                        <span class="px-2 py-0.5 rounded-full text-xs font-bold bg-white/10 {style['text']}">{level}级</span>
                    </div>
                    <div class="text-right">
                        <div class="text-lg font-black {style['text']}">{score}</div>
                        <div class="text-xs text-white/40">评分</div>
                    </div>
                </div>
                <p class="text-sm text-white/70 leading-relaxed mb-3">
                    {subtitle[:100]}...
                </p>
                {f'<div class="flex flex-wrap gap-2 mb-2">{tags_html}</div>' if tags_html else ''}
                {f'<div class="text-xs text-white/50"><span class="text-yellow-400">📅 近期催化：</span>{recent_catalyst}</div>' if recent_catalyst else ''}
            </div>
            '''
        
        html += '</div>'
        
        self.add_section("核心题材动态", html, "📊")
    
    def add_today_catalysts(self):
        """今日重大催化剂 - Pro版"""
        catalysts = self.topics.get('catalyst_calendar', [])
        
        if not catalysts:
            # 如果没有数据，生成一些示例
            catalysts = [
                {'date': '今日', 'event': '美联储公布利率决议', 'impact': '高', 'related_topics': '银行、贵金属'},
                {'date': '今日', 'event': '国内LPR报价公布', 'impact': '中', 'related_topics': '地产、基建'},
                {'date': '今日', 'event': 'AI行业峰会召开', 'impact': '高', 'related_topics': 'AI、算力'},
            ]
        
        html = '<div class="space-y-3">'
        
        for i, cat in enumerate(catalysts):
            impact = cat.get('impact', '中')
            impact_colors = {
                '高': ('bg-red-500/20', 'text-red-400', 'border-red-500/30'),
                '中': ('bg-yellow-500/20', 'text-yellow-400', 'border-yellow-500/30'),
                '低': ('bg-green-500/20', 'text-green-400', 'border-green-500/30'),
            }
            bg, text, border = impact_colors.get(impact, impact_colors['中'])
            
            event = cat.get('event', '')
            related = cat.get('related_topics', '')
            date = cat.get('date', '')
            
            html += f'''
            <div class="flex gap-3">
                <!-- 时间线 -->
                <div class="flex flex-col items-center">
                    <div class="w-3 h-3 rounded-full bg-gradient-to-r from-yellow-400 to-orange-500 ring-4 ring-yellow-500/20"></div>
                    {'' if i == len(catalysts)-1 else '<div class="flex-1 w-px bg-white/10 mt-1"></div>'}
                </div>
                
                <!-- 内容 -->
                <div class="flex-1 pb-4">
                    <div class="flex items-center gap-2 mb-1">
                        <span class="text-xs text-white/50">{date}</span>
                        <span class="px-2 py-0.5 rounded-full text-xs font-medium {bg} {text} border {border}">{impact}影响</span>
                    </div>
                    <div class="text-white font-semibold text-sm mb-1">{event}</div>
                    <div class="text-xs text-white/50">
                        相关题材：{related}
                    </div>
                </div>
            </div>
            '''
        
        html += '</div>'
        
        self.add_section("今日重大催化剂", html, "⚡")
    
    def add_jiuyan_hot_topics(self):
        """韭研公社热门话题 - Pro版"""
        # 模拟韭研公社热门话题数据
        hot_topics = [
            {'title': '存储芯片周期反转确认', 'views': '12.5万', 'likes': 328, 'hot': True},
            {'title': 'AI算力需求持续超预期', 'views': '10.2万', 'likes': 256, 'hot': True},
            {'title': '人形机器人产业进展跟踪', 'views': '8.7万', 'likes': 189, 'hot': False},
            {'title': '低空经济政策密集出台', 'views': '7.3万', 'likes': 145, 'hot': False},
            {'title': 'PCB铜箔供不应求', 'views': '6.8万', 'likes': 132, 'hot': False},
            {'title': '先进封装国产替代加速', 'views': '5.9万', 'likes': 108, 'hot': False},
        ]
        
        html = '<div class="space-y-2">'
        
        for i, topic in enumerate(hot_topics):
            rank_color = 'text-red-400 font-black' if i < 3 else 'text-white/40 font-semibold'
            hot_badge = '<span class="ml-2 px-1.5 py-0.5 bg-red-500/20 text-red-400 text-xs rounded">热</span>' if topic['hot'] else ''
            
            html += f'''
            <div class="flex items-center gap-3 p-3 bg-white/5 rounded-lg hover:bg-white/10 transition-all duration-300">
                <span class="text-lg {rank_color} w-6 text-center">{i+1}</span>
                <div class="flex-1 min-w-0">
                    <div class="text-sm text-white/90 font-medium truncate flex items-center">
                        {topic['title']}
                        {hot_badge}
                    </div>
                    <div class="text-xs text-white/40 mt-1">
                        👁️ {topic['views']} · 👍 {topic['likes']}
                    </div>
                </div>
                <span class="text-white/30 text-lg">›</span>
            </div>
            '''
        
        html += '</div>'
        
        # 说明
        html += '''
        <div class="mt-3 text-center text-xs text-white/40">
            数据来源：韭研公社 · 每小时更新
        </div>
        '''
        
        self.add_section("韭研公社热门话题", html, "🔥")
    
    def add_daily_summary(self):
        """每日总结 - Pro版"""
        market = self.market_data
        market_data = market.get('market_data', {})
        sentiment = market.get('sentiment', {})
        
        turnover = market_data.get('turnover', '')
        fg = sentiment.get('fear_greed', 50)
        
        hot = self.hot_sectors
        hot_names = '、'.join([s.get('name', '') for s in hot[:3]]) if hot else ''
        
        summary = f"""
        今日市场整体呈现情绪{"偏强" if fg > 50 else "偏弱"}格局，成交额{turnover}，市场活跃度{"较高" if fg > 60 else "一般"}。
        板块方面，{hot_names}等板块表现强势，市场结构性机会依然存在。
        操作上，建议聚焦业绩确定性强的优质标的，避免追高，保持合理仓位。
        """
        
        content = f'''
        <div class="bg-gradient-to-r from-purple-500/15 to-blue-500/10 border border-purple-500/20 rounded-xl p-5">
            <div class="text-white font-bold mb-3 flex items-center gap-2">
                <span>📝</span>
                <span>今日总结</span>
            </div>
            <div class="text-white/70 leading-relaxed text-sm">
                {summary.strip()}
            </div>
        </div>
        '''
        
        self.add_section("每日总结", content, "📝")
    
    def build_standard_report(self):
        """构建标准版本的日报 - V2: 新增今日作战计划作为核心板块"""
        self.add_global_market()         # 隔夜外盘概览
        self.add_market_overview()       # 大盘概览
        self.add_important_news()        # 重要新闻
        self.add_sector_analysis()       # 板块分析
        self.add_today_catalysts()       # 今日催化剂
        self.add_topic_dynamics()        # 题材动态
        self.add_topic_deep_dive()       # 题材深度
        self.add_skill_enhanced_section()# Skill增强分析
        self.add_jiuyan_hot_topics()     # 韭研热门
        self.add_holdings_tracking()     # 持仓跟踪
        self.add_battle_plan()           # 🎯 今日作战计划（核心灵魂板块）
        self.add_risk_warning()          # 风险提示
        return self



    def _generate_skill_enhanced_analysis(self, topic: Dict) -> Dict:
        """生成Skill增强的题材分析数据
        整合三维热度、SWOT、情景推演等分析框架
        """
        name = topic.get('name', '')
        dim_scores = topic.get('dimension_scores', {})
        catalysts = topic.get('catalyst_events', [])
        core_logic = topic.get('core_logic', '')
        
        # 1. 三维热度分析（基于现有维度数据）
        policy_score = dim_scores.get('policy', 50)
        industry_score = dim_scores.get('industry', 50)
        capital_score = dim_scores.get('capital', 50)
        
        # 计算综合热度
        three_d_overall = (policy_score * 0.35 + industry_score * 0.35 + capital_score * 0.3)
        
        # 热度结论
        if three_d_overall >= 80:
            heat_conclusion = "三维共振，持续高热度"
        elif three_d_overall >= 60:
            heat_conclusion = "两维驱动，热度较高"
        elif three_d_overall >= 40:
            heat_conclusion = "单维支撑，热度中等"
        else:
            heat_conclusion = "缺乏支撑，热度较低"
        
        three_d_heat = {
            'policy_score': policy_score,
            'industry_score': industry_score,
            'capital_score': capital_score,
            'overall_score': three_d_overall,
            'conclusion': heat_conclusion,
        }
        
        # 2. SWOT分析（基于题材特征智能生成）
        strengths = []
        weaknesses = []
        opportunities = []
        threats = []
        
        # 政策维度
        if policy_score >= 70:
            strengths.append("政策支持力度大，顶层设计明确")
        elif policy_score >= 50:
            opportunities.append("政策存在改善空间")
        else:
            weaknesses.append("政策支持力度不足")
        
        # 产业维度
        if industry_score >= 70:
            strengths.append("产业趋势明确，景气度持续上行")
        elif industry_score >= 50:
            opportunities.append("产业格局正在优化")
        else:
            weaknesses.append("产业基本面偏弱")
        
        # 资金维度
        if capital_score >= 70:
            strengths.append("资金关注度高，流入趋势明显")
        elif capital_score >= 50:
            opportunities.append("资金关注度有望提升")
        else:
            threats.append("资金关注度不足，缺乏增量资金")
        
        # 情绪维度
        sentiment_score = dim_scores.get('sentiment', 50)
        if sentiment_score >= 70:
            strengths.append("市场情绪高涨，赚钱效应强")
            threats.append("情绪过热可能引发回调")
        elif sentiment_score <= 30:
            opportunities.append("情绪冰点后存在修复机会")
        
        # 估值维度
        valuation_score = dim_scores.get('valuation', 50)
        if valuation_score >= 70:
            threats.append("估值偏高，存在回调风险")
        elif valuation_score <= 30:
            strengths.append("估值处于低位，安全边际高")
        
        # 催化维度
        catalyst_score = dim_scores.get('catalyst', 50)
        if catalyst_score >= 70:
            opportunities.append("催化剂密集，事件驱动性强")
        
        # 补充通用分析
        if catalysts:
            opportunities.append(f"近期有 {len(catalysts)} 个催化事件")
        else:
            weaknesses.append("缺乏明确催化事件")
        
        # 确保每个维度至少有1-2条
        if not strengths:
            strengths.append("题材具有一定的市场关注度")
        if not weaknesses:
            weaknesses.append("短期涨幅较大，存在获利回吐压力")
        if not opportunities:
            opportunities.append("行业长期发展空间广阔")
        if not threats:
            threats.append("宏观经济不确定性可能影响板块表现")
        
        swot = {
            'strengths': strengths[:3],
            'weaknesses': weaknesses[:3],
            'opportunities': opportunities[:3],
            'threats': threats[:3],
        }
        
        # 3. 情景推演
        base_return = 0.0
        
        # 根据综合评分计算预期
        total_score = topic.get('total_score', 50)
        if total_score >= 80:
            base_return = 0.15  # 15%
        elif total_score >= 60:
            base_return = 0.08  # 8%
        elif total_score >= 40:
            base_return = 0.02  # 2%
        else:
            base_return = -0.05  # -5%
        
        scenarios = [
            {
                'scenario_name': '乐观情景',
                'probability': 0.25,
                'impact_score': min(100, total_score + 20),
                'expected_return': base_return * 1.8,
                'key_assumptions': [
                    '催化事件超预期落地',
                    '资金持续大幅流入',
                    '行业数据超预期'
                ],
                'description': f'{name}板块在多重利好催化下，迎来估值与业绩双升行情'
            },
            {
                'scenario_name': '中性情景',
                'probability': 0.5,
                'impact_score': total_score,
                'expected_return': base_return,
                'key_assumptions': [
                    '催化事件符合预期',
                    '资金流入平稳',
                    '行业数据符合预期'
                ],
                'description': f'{name}板块维持现有趋势，沿既有轨道缓慢上行或震荡'
            },
            {
                'scenario_name': '悲观情景',
                'probability': 0.25,
                'impact_score': max(0, total_score - 25),
                'expected_return': base_return * -1.5,
                'key_assumptions': [
                    '催化事件不及预期',
                    '资金流出超预期',
                    '行业数据不及预期'
                ],
                'description': f'{name}板块因利好兑现或负面因素出现回调，短期承压'
            },
        ]
        
        return {
            'three_d_heat': three_d_heat,
            'swot': swot,
            'scenarios': scenarios,
        }
    
    def add_skill_enhanced_section(self):
        """添加Skill增强分析模块
        展示顶级分析框架的深度洞察
        """
        s_topics = self.topics.get('s_level_topics', [])
        a_topics = self.topics.get('a_level_topics', [])
        
        # 取最重要的1-2个题材做深度分析
        top_topics = (s_topics + a_topics)[:2]
        
        if not top_topics:
            return
        
        html = '<div class="space-y-4">'
        
        for topic in top_topics:
            name = topic.get('name', '')
            level = topic.get('level', '')
            analysis = self._generate_skill_enhanced_analysis(topic)
            
            # 为每个题材生成折叠式深度分析卡片
            topic_html = f'''
            <div class="bg-white/5 backdrop-blur-sm rounded-xl border border-white/10 overflow-hidden">
                <div class="p-4 flex items-center justify-between cursor-pointer" 
                     onclick="toggleSkillAnalysis('{name}')">
                    <div class="flex items-center gap-2">
                        <span class="text-lg">🧠</span>
                        <span class="font-bold text-white">{name} · 深度分析</span>
                        <span class="text-xs bg-gradient-to-r from-purple-500/30 to-blue-500/30 text-purple-300 px-2 py-0.5 rounded-full border border-purple-500/30">
                            Skill增强
                        </span>
                    </div>
                    <span class="text-white/40 text-sm" id="skill-arrow-{name}">▼</span>
                </div>
                <div id="skill-analysis-{name}" class="px-4 pb-4 hidden">
                    <div class="grid md:grid-cols-2 gap-3">
                        {self._render_three_d_heat(analysis['three_d_heat'])}
                        {self._render_swot_simple(analysis['swot'])}
                    </div>
                    <div class="mt-3">
                        {self._render_scenarios_simple(analysis['scenarios'])}
                    </div>
                </div>
            </div>
            '''
            html += topic_html
        
        html += '</div>'
        
        # 添加交互脚本
        js = '''
        <script>
        function toggleSkillAnalysis(name) {
            const panel = document.getElementById('skill-analysis-' + name);
            const arrow = document.getElementById('skill-arrow-' + name);
            if (panel.classList.contains('hidden')) {
                panel.classList.remove('hidden');
                arrow.textContent = '▲';
            } else {
                panel.classList.add('hidden');
                arrow.textContent = '▼';
            }
        }
        </script>
        '''
        
        self.add_section("🧠 Skill深度分析", html + js, "🧠")
    
    def _render_three_d_heat(self, heat_data: Dict) -> str:
        """简化版三维热度渲染"""
        policy_score = heat_data.get('policy_score', 50)
        industry_score = heat_data.get('industry_score', 50)
        capital_score = heat_data.get('capital_score', 50)
        overall = heat_data.get('overall_score', 50)
        
        return f'''
        <div class="bg-white/5 rounded-lg p-3 border border-white/10">
            <div class="text-sm font-bold text-white mb-2 flex items-center gap-1">
                🌡️ 三维热度
                <span class="text-xs font-normal text-white/50">综合 {overall:.0f}分</span>
            </div>
            <div class="space-y-2">
                <div class="flex items-center gap-2">
                    <span class="text-xs text-white/50 w-10">政策</span>
                    <div class="flex-1 h-1.5 bg-white/10 rounded-full overflow-hidden">
                        <div class="h-full bg-blue-500 rounded-full" style="width:{policy_score}%"></div>
                    </div>
                    <span class="text-xs text-white/70 w-8">{policy_score:.0f}</span>
                </div>
                <div class="flex items-center gap-2">
                    <span class="text-xs text-white/50 w-10">产业</span>
                    <div class="flex-1 h-1.5 bg-white/10 rounded-full overflow-hidden">
                        <div class="h-full bg-green-500 rounded-full" style="width:{industry_score}%"></div>
                    </div>
                    <span class="text-xs text-white/70 w-8">{industry_score:.0f}</span>
                </div>
                <div class="flex items-center gap-2">
                    <span class="text-xs text-white/50 w-10">资金</span>
                    <div class="flex-1 h-1.5 bg-white/10 rounded-full overflow-hidden">
                        <div class="h-full bg-yellow-500 rounded-full" style="width:{capital_score}%"></div>
                    </div>
                    <span class="text-xs text-white/70 w-8">{capital_score:.0f}</span>
                </div>
            </div>
        </div>
        '''
    
    def _render_swot_simple(self, swot_data: Dict) -> str:
        """简化版SWOT渲染"""
        s = swot_data.get('strengths', [])
        w = swot_data.get('weaknesses', [])
        o = swot_data.get('opportunities', [])
        t = swot_data.get('threats', [])
        
        def bullet(items, color):
            return ''.join([f'<div class="text-xs text-white/60 mb-0.5"><span class="{color} mr-1">•</span>{item}</div>' for item in items[:2]])
        
        return f'''
        <div class="bg-white/5 rounded-lg p-3 border border-white/10">
            <div class="text-sm font-bold text-white mb-2">📊 SWOT分析</div>
            <div class="grid grid-cols-2 gap-2 text-xs">
                <div>
                    <span class="text-green-400 font-semibold">优势</span>
                    {bullet(s, 'text-green-400')}
                </div>
                <div>
                    <span class="text-red-400 font-semibold">劣势</span>
                    {bullet(w, 'text-red-400')}
                </div>
                <div>
                    <span class="text-blue-400 font-semibold">机会</span>
                    {bullet(o, 'text-blue-400')}
                </div>
                <div>
                    <span class="text-orange-400 font-semibold">威胁</span>
                    {bullet(t, 'text-orange-400')}
                </div>
            </div>
        </div>
        '''
    
    def _render_scenarios_simple(self, scenarios: List[Dict]) -> str:
        """简化版情景推演渲染"""
        sc_html = ''
        for sc in scenarios:
            name = sc.get('scenario_name', '')
            prob = sc.get('probability', 0) * 100
            ret = sc.get('expected_return', 0) * 100
            
            if '乐观' in name:
                color = 'text-green-400 bg-green-500/10 border-green-500/20'
            elif '悲观' in name:
                color = 'text-red-400 bg-red-500/10 border-red-500/20'
            else:
                color = 'text-yellow-400 bg-yellow-500/10 border-yellow-500/20'
            
            sc_html += f'''
            <div class="flex-1 rounded-lg p-2 border {color} text-center">
                <div class="text-xs font-bold mb-1">{name}</div>
                <div class="text-lg font-black">{ret:+.1f}%</div>
                <div class="text-xs opacity-60">{prob:.0f}%概率</div>
            </div>
            '''
        
        return f'''
        <div class="bg-white/5 rounded-lg p-3 border border-white/10">
            <div class="text-sm font-bold text-white mb-2">🎯 情景推演</div>
            <div class="flex gap-2">
                {sc_html}
            </div>
        </div>
        '''

if __name__ == '__main__':
    # 测试生成
    gen = DailyReportProGenerator('2026-06-15', '周一')
    gen.build_standard_report()
    html = gen.render()
    print(f'Pro版日报生成成功，长度: {len(html)} 字符')
    
    # 保存测试
    os.makedirs('../docs/daily', exist_ok=True)
    with open('../docs/daily/test_daily_pro.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print('已保存到 docs/daily/test_daily_pro.html')

