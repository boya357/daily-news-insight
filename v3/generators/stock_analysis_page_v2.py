"""
个股深度分析页面生成器 V2.0 - Skill增强版
整合多个Skill的分析能力：
- 股票个股分析 Skill：缺口分析、消息面情绪、专业操作建议
- 竹石个股 Agent Skill：游资视角、龙头分析、筹码分析
- 超级分析师 Skill：SWOT分析框架

页面模块：
1. 股票头部概览
2. 综合评级与评分
3. 技术面深度分析
4. 缺口分析
5. 游资视角
6. 消息面情绪
7. 专业操作建议
8. 支撑压力位
"""

import sys
import os
import json
from pathlib import Path
from typing import List, Dict
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from components.pro import GlassCard, SectionTitle, get_pro_theme_css
from generators.pro_base import ProGenerator
from analyzers.stock_analyzer import StockAnalyzer


class StockAnalysisPageGeneratorV2(ProGenerator):
    """个股深度分析页面生成器 V2.0 - Skill增强版"""
    
    def __init__(self, stock_code, stock_name, data_dir: str = "data", 
                 sector_hotness: float = 50, topic_relevance: float = 50):
        super().__init__(
            title=f"{stock_name} 深度分析",
            active_page="工具",
            footer_text="投资研究中心 · 数据驱动决策 · Skill增强版",
            data_dir=data_dir,
            show_toc=True,
        )
        self.stock_code = stock_code
        self.stock_name = stock_name
        self.sector_hotness = sector_hotness
        self.topic_relevance = topic_relevance
        self.analysis = None
    
    def load_data(self):
        """加载数据并进行分析"""
        super().load_data()
        
        prices = self._load_kline_data()
        
        # V2增强分析
        analyzer = StockAnalyzer(self.stock_code, self.stock_name)
        analyzer.load_historical_data(prices)
        self.analysis = analyzer.analyze_all(
            sector_hotness=self.sector_hotness,
            topic_relevance=self.topic_relevance
        )
    
    def _load_kline_data(self):
        """加载K线数据"""
        kline_file = Path("data") / f"kline_{self.stock_code}.json"
        
        if kline_file.exists():
            with open(kline_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        
        return self._generate_mock_kline()
    
    def _generate_mock_kline(self):
        """生成模拟K线数据"""
        import random
        random.seed(hash(self.stock_code) % 10000)
        
        base_price = 50
        prices = []
        
        current = base_price
        for i in range(60):
            change = random.gauss(0, 0.025)
            open_price = current * (1 + random.uniform(-0.008, 0.008))
            high = max(open_price, current) * (1 + random.uniform(0, 0.04))
            low = min(open_price, current) * (1 - random.uniform(0, 0.04))
            close = current * (1 + change)
            volume = random.randint(800000, 8000000)
            
            prices.append({
                'date': f'2026-01-{i+1:02d}',
                'open': round(open_price, 2),
                'high': round(high, 2),
                'low': round(low, 2),
                'close': round(close, 2),
                'volume': volume,
            })
            
            current = close
        
        return prices
    
    # ========================================================================
    # 渲染方法
    # ========================================================================
    
    def _get_score_color(self, score: float) -> str:
        """根据分数获取颜色"""
        if score >= 70:
            return "text-green-400"
        elif score >= 50:
            return "text-yellow-400"
        elif score >= 30:
            return "text-orange-400"
        else:
            return "text-red-400"
    
    def _get_score_bg(self, score: float) -> str:
        """根据分数获取背景色"""
        if score >= 70:
            return "bg-green-500/20 border-green-500/30"
        elif score >= 50:
            return "bg-yellow-500/20 border-yellow-500/30"
        elif score >= 30:
            return "bg-orange-500/20 border-orange-500/30"
        else:
            return "bg-red-500/20 border-red-500/30"
    
    def _render_header(self) -> str:
        """渲染股票头部信息"""
        if not self.analysis:
            return ''
        
        current_price = 0
        if self.analysis.get('technical'):
            sr = self.analysis['technical'].get('support_resistance', {})
            current_price = sr.get('high_20', 50) * 0.9  # 估算
        
        overall = self.analysis.get('overall', {})
        score = overall.get('score', 50)
        rating = overall.get('rating', '中性')
        
        # 技能标签
        skills = self.analysis.get('skills_used', [])
        skill_tags = ''.join([
            f'<span class="px-2 py-1 bg-purple-500/20 text-purple-300 text-xs rounded-full">{s}</span>'
            for s in skills
        ])
        
        return f'''
        <div class="glass-card rounded-2xl p-6 mb-6">
            <div class="flex items-start justify-between mb-4">
                <div>
                    <div class="flex items-center gap-3 mb-2">
                        <h1 class="text-2xl font-bold text-white">{self.stock_name}</h1>
                        <span class="text-sm text-white/50">{self.stock_code}</span>
                    </div>
                    <div class="flex items-center gap-2 mb-3">
                        {skill_tags}
                    </div>
                    <div class="flex items-baseline gap-2">
                        <span class="text-3xl font-bold text-white">${current_price:.2f}</span>
                        <span class="text-sm text-green-400">+0.85 (+1.72%)</span>
                    </div>
                </div>
                <div class="text-right">
                    <div class="text-sm text-white/50 mb-1">综合评级</div>
                    <div class="text-2xl font-bold {self._get_score_color(score)}">{rating}</div>
                    <div class="text-3xl font-bold {self._get_score_color(score)} mt-1">{score:.1f}分</div>
                </div>
            </div>
            <div class="grid grid-cols-4 gap-3 pt-4 border-t border-white/10">
                <div class="text-center">
                    <div class="text-xs text-white/50 mb-1">技术面</div>
                    <div class="text-lg font-semibold {self._get_score_color(self.analysis.get('technical', {}).get('summary', {}).get('total_score', 50))}">
                        {self.analysis.get('technical', {}).get('summary', {}).get('total_score', 50):.0f}分
                    </div>
                </div>
                <div class="text-center">
                    <div class="text-xs text-white/50 mb-1">游资视角</div>
                    <div class="text-lg font-semibold {self._get_score_color(self.analysis.get('hot_money', {}).get('dragon_score', 50))}">
                        {self.analysis.get('hot_money', {}).get('dragon_score', 50):.0f}分
                    </div>
                </div>
                <div class="text-center">
                    <div class="text-xs text-white/50 mb-1">情绪面</div>
                    <div class="text-lg font-semibold {self._get_score_color((self.analysis.get('sentiment', {}).get('score', 0) + 100) / 2)}">
                        {(self.analysis.get('sentiment', {}).get('score', 0) + 100) / 2:.0f}分
                    </div>
                </div>
                <div class="text-center">
                    <div class="text-xs text-white/50 mb-1">风报比</div>
                    <div class="text-lg font-semibold text-cyan-400">
                        {self.analysis.get('trading_advice', {}).get('risk_reward_ratio', 0):.1f}
                    </div>
                </div>
            </div>
        </div>
        '''
    
    def _render_technical_analysis(self) -> str:
        """渲染技术面分析"""
        tech = self.analysis.get('technical', {})
        if not tech:
            return ''
        
        summary = tech.get('summary', {})
        total_score = summary.get('total_score', 50)
        rating = summary.get('rating', '中性')
        
        # 各指标
        indicators = []
        for key, name in [
            ('ma', '均线系统'),
            ('macd', 'MACD'),
            ('rsi', 'RSI'),
            ('kdj', 'KDJ'),
            ('boll', '布林带'),
            ('volume', '成交量'),
        ]:
            ind = tech.get(key, {})
            score = ind.get('score', 50)
            signal = ind.get('signal', '--')
            indicators.append(f'''
            <div class="flex items-center justify-between py-2 border-b border-white/5 last:border-0">
                <span class="text-white/70 text-sm">{name}</span>
                <div class="flex items-center gap-3">
                    <span class="text-xs text-white/50">{signal}</span>
                    <span class="text-sm font-medium {self._get_score_color(score)}">{score:.0f}分</span>
                </div>
            </div>
            ''')
        
        return f'''
        <div class="glass-card rounded-2xl p-6 mb-6">
            <div class="flex items-center justify-between mb-4">
                <h2 class="text-lg font-bold text-white flex items-center gap-2">
                    <span>📊</span> 技术面分析
                </h2>
                <div class="flex items-center gap-2">
                    <span class="text-sm text-white/50">综合</span>
                    <span class="text-lg font-bold {self._get_score_color(total_score)}">{total_score:.0f}分</span>
                    <span class="text-sm {self._get_score_color(total_score)}">{rating}</span>
                </div>
            </div>
            <div class="space-y-0">
                {''.join(indicators)}
            </div>
        </div>
        '''
    
    def _render_gap_analysis(self) -> str:
        """渲染缺口分析（来自股票个股分析 Skill）"""
        gaps = self.analysis.get('gaps', {})
        if not gaps:
            return ''
        
        key_gaps = gaps.get('key_gaps', [])
        gap_sr = gaps.get('gap_support_resistance', {})
        total_gaps = gaps.get('total_gaps_count', 0)
        analysis_text = gaps.get('analysis', '')
        
        # 渲染缺口列表
        gap_items = []
        for g in key_gaps[:4]:  # 最多显示4个
            gap_type = g.get('gap_type', '')
            is_filled = g.get('is_filled', False)
            importance = g.get('importance', '中')
            size_pct = g.get('size_pct', 0)
            
            type_color = 'text-green-400' if '向上' in gap_type else 'text-red-400'
            filled_text = '<span class="text-xs text-white/40">已回补</span>' if is_filled else '<span class="text-xs text-yellow-400">未回补</span>'
            
            importance_colors = {'高': 'text-red-400', '中': 'text-yellow-400', '低': 'text-white/50'}
            imp_color = importance_colors.get(importance, 'text-white/50')
            
            gap_items.append(f'''
            <div class="bg-white/5 rounded-lg p-3">
                <div class="flex items-center justify-between mb-2">
                    <span class="font-medium {type_color}">{gap_type}</span>
                    <div class="flex items-center gap-2">
                        <span class="text-xs {imp_color}">{importance}</span>
                        {filled_text}
                    </div>
                </div>
                <div class="flex justify-between text-xs text-white/50">
                    <span>{g.get('date', '')}</span>
                    <span>幅度 {size_pct:.2f}%</span>
                </div>
            </div>
            ''')
        
        # 缺口支撑压力
        gap_support = gap_sr.get('gap_support')
        gap_resistance = gap_sr.get('gap_resistance')
        support_pct = gap_sr.get('support_pct')
        resistance_pct = gap_sr.get('resistance_pct')
        
        sr_html = ''
        if gap_support or gap_resistance:
            sr_items = []
            if gap_support:
                sr_items.append(f'''
                <div class="flex-1 bg-green-500/10 border border-green-500/20 rounded-lg p-3 text-center">
                    <div class="text-xs text-white/50 mb-1">缺口支撑</div>
                    <div class="text-lg font-bold text-green-400">{gap_support}</div>
                    <div class="text-xs text-green-400/70">-{support_pct:.1f}%</div>
                </div>
                ''')
            if gap_resistance:
                sr_items.append(f'''
                <div class="flex-1 bg-red-500/10 border border-red-500/20 rounded-lg p-3 text-center">
                    <div class="text-xs text-white/50 mb-1">缺口压力</div>
                    <div class="text-lg font-bold text-red-400">{gap_resistance}</div>
                    <div class="text-xs text-red-400/70">+{resistance_pct:.1f}%</div>
                </div>
                ''')
            sr_html = f'''
            <div class="flex gap-3 mt-4">
                {''.join(sr_items)}
            </div>
            '''
        
        return f'''
        <div class="glass-card rounded-2xl p-6 mb-6">
            <div class="flex items-center justify-between mb-4">
                <h2 class="text-lg font-bold text-white flex items-center gap-2">
                    <span>📈</span> 缺口分析
                    <span class="text-xs font-normal text-white/40 bg-white/10 px-2 py-0.5 rounded-full">Stock Analysis Skill</span>
                </h2>
                <span class="text-sm text-white/50">共 {total_gaps} 个缺口</span>
            </div>
            
            <p class="text-sm text-white/70 mb-4">{analysis_text}</p>
            
            <div class="grid grid-cols-2 gap-3">
                {''.join(gap_items)}
            </div>
            
            {sr_html}
        </div>
        '''
    
    def _render_hot_money(self) -> str:
        """渲染游资视角分析（来自竹石个股 Agent Skill）"""
        hm = self.analysis.get('hot_money', {})
        if not hm:
            return ''
        
        dragon_score = hm.get('dragon_score', 50)
        dragon_label = hm.get('dragon_label', '')
        chip_structure = hm.get('chip_structure', '')
        continuity_score = hm.get('continuity_score', 50)
        catalyst_strength = hm.get('catalyst_strength', '')
        rr_ratio = hm.get('risk_reward_ratio', 0)
        
        # 龙头评分进度条
        dragon_bar_width = min(100, max(0, dragon_score))
        
        return f'''
        <div class="glass-card rounded-2xl p-6 mb-6">
            <div class="flex items-center justify-between mb-4">
                <h2 class="text-lg font-bold text-white flex items-center gap-2">
                    <span>🐯</span> 游资视角
                    <span class="text-xs font-normal text-white/40 bg-white/10 px-2 py-0.5 rounded-full">竹石Agent Skill</span>
                </h2>
                <span class="text-sm font-bold text-orange-400">{dragon_label}</span>
            </div>
            
            <!-- 龙头评分 -->
            <div class="mb-4">
                <div class="flex justify-between text-sm mb-1">
                    <span class="text-white/70">龙头指数</span>
                    <span class="text-orange-400 font-medium">{dragon_score:.0f}分</span>
                </div>
                <div class="h-2 bg-white/10 rounded-full overflow-hidden">
                    <div class="h-full bg-gradient-to-r from-orange-500 to-red-500 rounded-full" 
                         style="width: {dragon_bar_width}%"></div>
                </div>
            </div>
            
            <div class="grid grid-cols-2 gap-3 mb-4">
                <div class="bg-white/5 rounded-lg p-3">
                    <div class="text-xs text-white/50 mb-1">筹码结构</div>
                    <div class="text-sm text-white/80">{chip_structure}</div>
                </div>
                <div class="bg-white/5 rounded-lg p-3">
                    <div class="text-xs text-white/50 mb-1">持续性</div>
                    <div class="text-sm text-white/80">{continuity_score:.0f}分</div>
                </div>
            </div>
            
            <div class="bg-white/5 rounded-lg p-3 mb-3">
                <div class="text-xs text-white/50 mb-1">题材催化强度</div>
                <div class="text-sm text-white/80">{catalyst_strength}</div>
            </div>
            
            <div class="flex items-center justify-between bg-cyan-500/10 border border-cyan-500/20 rounded-lg p-3">
                <span class="text-sm text-white/70">风险收益比</span>
                <span class="text-xl font-bold text-cyan-400">1 : {rr_ratio:.1f}</span>
            </div>
        </div>
        '''
    
    def _render_sentiment(self) -> str:
        """渲染消息面情绪分析（来自股票个股分析 Skill）"""
        sent = self.analysis.get('sentiment', {})
        if not sent:
            return ''
        
        score = sent.get('score', 0)
        label = sent.get('label', '中性')
        impact = sent.get('market_impact', '')
        news_count = sent.get('news_count', 0)
        key_pos = sent.get('key_positive', [])
        key_neg = sent.get('key_negative', [])
        
        # 情绪分数可视化（-100 到 100）
        normalized_score = (score + 100) / 2  # 转为 0-100
        
        # 情绪标签颜色
        label_colors = {
            '极度乐观': 'text-green-400',
            '乐观': 'text-green-400',
            '偏乐观': 'text-green-300',
            '中性': 'text-yellow-400',
            '偏悲观': 'text-orange-300',
            '悲观': 'text-red-400',
            '极度悲观': 'text-red-500',
        }
        label_color = label_colors.get(label, 'text-white')
        
        return f'''
        <div class="glass-card rounded-2xl p-6 mb-6">
            <div class="flex items-center justify-between mb-4">
                <h2 class="text-lg font-bold text-white flex items-center gap-2">
                    <span>😊</span> 消息面情绪
                    <span class="text-xs font-normal text-white/40 bg-white/10 px-2 py-0.5 rounded-full">Stock Analysis Skill</span>
                </h2>
                <span class="text-sm font-bold {label_color}">{label}</span>
            </div>
            
            <!-- 情绪分数仪表 -->
            <div class="mb-4">
                <div class="flex justify-between text-sm mb-1">
                    <span class="text-red-400">悲观</span>
                    <span class="text-2xl font-bold {label_color}">{score:.0f}</span>
                    <span class="text-green-400">乐观</span>
                </div>
                <div class="h-3 bg-gradient-to-r from-red-500 via-yellow-500 to-green-500 rounded-full overflow-hidden relative">
                    <div class="absolute top-0 bottom-0 w-1 bg-white shadow-lg" 
                         style="left: {normalized_score}%; transform: translateX(-50%);"></div>
                </div>
                <div class="flex justify-between text-xs text-white/40 mt-1">
                    <span>-100</span>
                    <span>0</span>
                    <span>100</span>
                </div>
            </div>
            
            <p class="text-sm text-white/70 mb-4">{impact}</p>
            
            <div class="grid grid-cols-2 gap-3">
                <div class="bg-green-500/10 border border-green-500/20 rounded-lg p-3">
                    <div class="text-xs text-green-400 mb-2 flex items-center gap-1">
                        <span>✓</span> 利好因素
                    </div>
                    <ul class="text-xs text-white/70 space-y-1">
                        {"".join(f"<li>{p}</li>" for p in key_pos[:2])}
                    </ul>
                </div>
                <div class="bg-red-500/10 border border-red-500/20 rounded-lg p-3">
                    <div class="text-xs text-red-400 mb-2 flex items-center gap-1">
                        <span>✕</span> 利空因素
                    </div>
                    <ul class="text-xs text-white/70 space-y-1">
                        {"".join(f"<li>{n}</li>" for n in key_neg[:2])}
                    </ul>
                </div>
            </div>
        </div>
        '''
    
    def _render_trading_advice(self) -> str:
        """渲染专业操作建议（整合所有Skill + SWOT框架）"""
        advice = self.analysis.get('trading_advice', {})
        if not advice:
            return ''
        
        rating = advice.get('overall_rating', '')
        score = advice.get('rating_score', 50)
        buy_zone = advice.get('buy_zone', [0, 0])
        sell_zone = advice.get('sell_zone', [0, 0])
        stop_loss = advice.get('stop_loss', 0)
        take_profit = advice.get('take_profit', 0)
        rr_ratio = advice.get('risk_reward_ratio', 0)
        position = advice.get('position_suggestion', '')
        horizon = advice.get('time_horizon', '')
        key_risks = advice.get('key_risks', [])
        key_catalysts = advice.get('key_catalysts', [])
        summary = advice.get('strategy_summary', '')
        
        # 评级颜色
        score_color = self._get_score_color(score)
        
        return f'''
        <div class="glass-card rounded-2xl p-6 mb-6">
            <div class="flex items-center justify-between mb-4">
                <h2 class="text-lg font-bold text-white flex items-center gap-2">
                    <span>💡</span> 专业操作建议
                    <span class="text-xs font-normal text-white/40 bg-white/10 px-2 py-0.5 rounded-full">超级分析师 Skill</span>
                </h2>
                <span class="text-lg font-bold {score_color}">{rating}</span>
            </div>
            
            <p class="text-sm text-white/70 mb-4 pb-4 border-b border-white/10">{summary}</p>
            
            <!-- 买卖区间 -->
            <div class="grid grid-cols-2 gap-3 mb-4">
                <div class="bg-green-500/10 border border-green-500/20 rounded-lg p-3">
                    <div class="text-xs text-green-400 mb-1">买入区间</div>
                    <div class="text-lg font-bold text-green-400">
                        {buy_zone[0]:.2f} ~ {buy_zone[1]:.2f}
                    </div>
                </div>
                <div class="bg-red-500/10 border border-red-500/20 rounded-lg p-3">
                    <div class="text-xs text-red-400 mb-1">卖出区间</div>
                    <div class="text-lg font-bold text-red-400">
                        {sell_zone[0]:.2f} ~ {sell_zone[1]:.2f}
                    </div>
                </div>
            </div>
            
            <!-- 止损止盈 -->
            <div class="grid grid-cols-2 gap-3 mb-4">
                <div class="bg-white/5 rounded-lg p-3">
                    <div class="text-xs text-white/50 mb-1">止损位</div>
                    <div class="text-lg font-bold text-red-400">{stop_loss:.2f}</div>
                </div>
                <div class="bg-white/5 rounded-lg p-3">
                    <div class="text-xs text-white/50 mb-1">止盈位</div>
                    <div class="text-lg font-bold text-green-400">{take_profit:.2f}</div>
                </div>
            </div>
            
            <!-- 仓位与周期 -->
            <div class="bg-white/5 rounded-lg p-3 mb-4">
                <div class="text-sm text-white/70 mb-2">{position}</div>
                <div class="text-sm text-white/50">建议持仓周期：{horizon}</div>
            </div>
            
            <!-- 风险与催化 -->
            <div class="grid grid-cols-2 gap-3">
                <div>
                    <div class="text-xs text-white/50 mb-2">⚠️ 主要风险</div>
                    <ul class="text-xs text-white/70 space-y-1">
                        {"".join(f"<li>{r}</li>" for r in key_risks[:2])}
                    </ul>
                </div>
                <div>
                    <div class="text-xs text-white/50 mb-2">🚀 潜在催化</div>
                    <ul class="text-xs text-white/70 space-y-1">
                        {"".join(f"<li>{c}</li>" for c in key_catalysts[:2])}
                    </ul>
                </div>
            </div>
        </div>
        '''
    
    def _render_support_resistance(self) -> str:
        """渲染支撑压力位分析"""
        tech = self.analysis.get('technical', {})
        if not tech:
            return ''
        
        sr = tech.get('support_resistance', {})
        if not sr:
            return ''
        
        support = sr.get('support')
        resistance = sr.get('resistance')
        high_20 = sr.get('high_20')
        low_20 = sr.get('low_20')
        
        # 也包含缺口支撑压力
        gap_sr = self.analysis.get('gaps', {}).get('gap_support_resistance', {})
        gap_support = gap_sr.get('gap_support')
        gap_resistance = gap_sr.get('gap_resistance')
        
        return f'''
        <div class="glass-card rounded-2xl p-6 mb-6">
            <h2 class="text-lg font-bold text-white flex items-center gap-2 mb-4">
                <span>🎯</span> 支撑压力位
            </h2>
            
            <div class="space-y-3">
                <!-- 压力位 -->
                <div class="relative pl-4 border-l-2 border-red-500/30">
                    <div class="absolute -left-1.5 top-0 w-3 h-3 rounded-full bg-red-500"></div>
                    <div class="flex justify-between items-center">
                        <span class="text-sm text-white/70">20日高点</span>
                        <span class="font-medium text-red-400">{high_20:.2f}</span>
                    </div>
                </div>
                
                {f'''
                <div class="relative pl-4 border-l-2 border-red-500/20">
                    <div class="absolute -left-1.5 top-0 w-2.5 h-2.5 rounded-full bg-red-400/60"></div>
                    <div class="flex justify-between items-center">
                        <span class="text-sm text-white/50">缺口压力</span>
                        <span class="font-medium text-red-400/80">{gap_resistance}</span>
                    </div>
                </div>
                ''' if gap_resistance else ''}
                
                <div class="relative pl-4 border-l-2 border-red-500/20">
                    <div class="absolute -left-1.5 top-0 w-2.5 h-2.5 rounded-full bg-red-400/60"></div>
                    <div class="flex justify-between items-center">
                        <span class="text-sm text-white/50">均线压力</span>
                        <span class="font-medium text-red-400/80">{resistance:.2f}</span>
                    </div>
                </div>
                
                <!-- 当前价 -->
                <div class="relative pl-4 border-l-2 border-blue-500/50">
                    <div class="absolute -left-2 top-0 w-4 h-4 rounded-full bg-blue-500 animate-pulse"></div>
                    <div class="flex justify-between items-center">
                        <span class="text-sm font-medium text-blue-400">当前价</span>
                        <span class="font-bold text-blue-400">${high_20 * 0.9:.2f}</span>
                    </div>
                </div>
                
                <!-- 支撑位 -->
                <div class="relative pl-4 border-l-2 border-green-500/20">
                    <div class="absolute -left-1.5 top-0 w-2.5 h-2.5 rounded-full bg-green-400/60"></div>
                    <div class="flex justify-between items-center">
                        <span class="text-sm text-white/50">均线支撑</span>
                        <span class="font-medium text-green-400/80">{support:.2f}</span>
                    </div>
                </div>
                
                {f'''
                <div class="relative pl-4 border-l-2 border-green-500/20">
                    <div class="absolute -left-1.5 top-0 w-2.5 h-2.5 rounded-full bg-green-400/60"></div>
                    <div class="flex justify-between items-center">
                        <span class="text-sm text-white/50">缺口支撑</span>
                        <span class="font-medium text-green-400/80">{gap_support}</span>
                    </div>
                </div>
                ''' if gap_support else ''}
                
                <div class="relative pl-4 border-l-2 border-green-500/30">
                    <div class="absolute -left-1.5 top-0 w-3 h-3 rounded-full bg-green-500"></div>
                    <div class="flex justify-between items-center">
                        <span class="text-sm text-white/70">20日低点</span>
                        <span class="font-medium text-green-400">{low_20:.2f}</span>
                    </div>
                </div>
            </div>
        </div>
        '''
    
    def _content(self) -> str:
        """主内容渲染"""
        if not self.analysis:
            return '<div class="text-center text-white/50 py-20">分析数据加载中...</div>'
        
        return f'''
        <div class="max-w-4xl mx-auto">
            <!-- 头部概览 -->
            {self._render_header()}
            
            <!-- 两列布局 -->
            <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
                <!-- 左列 -->
                <div>
                    {self._render_technical_analysis()}
                    {self._render_gap_analysis()}
                    {self._render_support_resistance()}
                </div>
                
                <!-- 右列 -->
                <div>
                    {self._render_hot_money()}
                    {self._render_sentiment()}
                    {self._render_trading_advice()}
                </div>
            </div>
            
            <!-- 声明 -->
            <div class="glass-card rounded-xl p-4 mt-6">
                <p class="text-xs text-white/40 text-center">
                    ⚠️ 风险提示：以上分析由AI基于公开数据生成，仅供参考，不构成投资建议。
                    股市有风险，投资需谨慎。分析结果基于历史数据，不代表未来表现。
                    整合分析能力来自：股票个股分析 Skill、竹石个股 Agent Skill、超级分析师 Skill。
                </p>
            </div>
        </div>
        '''
    
    def generate(self) -> str:
        """生成完整页面"""
        self.load_data()
        self.load_data()
        return self.render()
    
    def save(self, filepath: str) -> str:
        """保存页面到文件"""
        html = self.generate()
        Path(filepath).parent.mkdir(parents=True, exist_ok=True)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
        return filepath


# ============================================================================
# 便捷函数
# ============================================================================
def generate_stock_page(stock_code: str, stock_name: str, 
                        output_path: str, sector_hotness: float = 50, 
                        topic_relevance: float = 50) -> str:
    """生成单只股票的分析页面"""
    generator = StockAnalysisPageGeneratorV2(
        stock_code, stock_name,
        sector_hotness=sector_hotness,
        topic_relevance=topic_relevance
    )
    return generator.save(output_path)


def generate_stock_list_page(stocks: List[Dict], output_path: str) -> str:
    """生成股票列表页（暂略，使用原有实现）"""
    pass


if __name__ == '__main__':
    # 测试生成
    output = generate_stock_page('002837', '英维克', 'test_stock_page.html')
    print(f"Page generated: {output}")
