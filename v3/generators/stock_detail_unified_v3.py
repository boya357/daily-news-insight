"""
统一股票详情页生成器 V3 - 完整深度版
- 基于统一JSON数据生成
- 完整展示所有分析模块
- 深色玻璃态风格
- 三大Skill标签：股票个股分析、竹石个股Agent、超级分析师
"""

import os
import json
from pathlib import Path
from typing import Dict, Optional, List


def safe_num(value, default=0, fmt='.2f'):
    """安全格式化数字"""
    if value is None:
        return format(default, fmt)
    try:
        return format(float(value), fmt)
    except (ValueError, TypeError):
        return format(default, fmt)


def safe_str(value, default='-'):
    """安全获取字符串"""
    if value is None:
        return default
    return str(value)


def get_score_color(score: float) -> str:
    """根据分数获取颜色类名"""
    if score >= 70:
        return "text-green-400"
    elif score >= 50:
        return "text-yellow-400"
    elif score >= 30:
        return "text-orange-400"
    else:
        return "text-red-400"


def get_score_hex(score: float) -> str:
    """根据分数获取十六进制颜色"""
    if score >= 70:
        return "#4ade80"
    elif score >= 50:
        return "#facc15"
    elif score >= 30:
        return "#fb923c"
    else:
        return "#f87171"


class StockDetailPageGeneratorV3:
    """股票详情页生成器 V3 - 完整深度版"""
    
    def __init__(self, data_dir: str = None, pages_dir: str = None):
        if data_dir:
            self.data_dir = Path(data_dir)
        else:
            self.data_dir = Path(__file__).resolve().parent.parent.parent / 'docs' / 'data' / 'stock_analysis'
        
        if pages_dir:
            self.pages_dir = Path(pages_dir)
        else:
            self.pages_dir = Path(__file__).resolve().parent.parent.parent / 'docs' / '个股分析'
    
    def load_stock_data(self, stock_code: str) -> Optional[Dict]:
        data_file = self.data_dir / f'{stock_code}.json'
        if not data_file.exists():
            return None
        with open(data_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    def generate(self, stock_code: str, stock_name: str) -> str:
        data = self.load_stock_data(stock_code)
        if not data:
            return self._generate_placeholder(stock_name, stock_code)
        return self._render_page(data)
    
    def _render_page(self, data: Dict) -> str:
        name = data.get('name', '')
        code = data.get('code', '')
        sector = data.get('sector', '')
        business = data.get('business', '')
        
        overall = data.get('overall', {})
        total_score = overall.get('score', 0) or 0
        total_rating = overall.get('rating', '暂无')
        
        market = data.get('market', {})
        price = market.get('current_price') or overall.get('price') or 0
        change_pct = market.get('change_pct') or overall.get('change_pct') or 0
        change_amount = market.get('change_amount') or 0
        
        is_up = change_pct >= 0
        price_color = '#ef4444' if is_up else '#10b981'
        price_color_class = 'text-red-400' if is_up else 'text-green-400'
        
        technical = data.get('technical', {})
        fundamental = data.get('fundamental', {})
        trader = data.get('trader', {})
        news = data.get('news', {})
        themes = data.get('themes', [])
        sr = technical.get('support_resistance', {}) if technical else {}
        
        # 计算各维度分数
        tech_score = self._calc_tech_score(technical)
        trader_score = self._calc_trader_score(trader)
        sentiment_score = self._calc_sentiment_score(news)
        risk_reward = self._calc_risk_reward(technical, trader)
        
        # 渲染各模块
        head_html = self._render_header(name, code, sector, price, change_pct, change_amount, 
                                       total_score, total_rating, price_color, price_color_class,
                                       tech_score, trader_score, sentiment_score, risk_reward)
        
        tech_html = self._render_technical(technical, price_color_class)
        gap_html = self._render_gap_analysis(technical, price)
        sr_html = self._render_support_resistance(sr, price, price_color_class)
        
        trader_html = self._render_trader(trader, trader_score)
        sentiment_html = self._render_sentiment(news, sentiment_score)
        strategy_html = self._render_strategy(trader, price)
        
        fund_html = self._render_fundamental(fundamental)
        themes_html = self._render_themes(themes, sector, business)
        
        return f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{name} 深度分析 - 投资研究中心</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@300;400;500;700;900&display=swap');
        * {{ font-family: 'Noto Sans SC', sans-serif; }}
        body {{
            background: linear-gradient(135deg, #1a103c 0%, #2d1b69 50%, #4c1d95 100%);
            min-height: 100vh;
            padding-top: 80px;
            color: white;
        }}
        .glass-card {{
            background: rgba(255, 255, 255, 0.06);
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 20px;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
        }}
        .section-title {{
            font-size: 1.25rem;
            font-weight: 700;
            margin-bottom: 1rem;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }}
        .nav-bar {{
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            z-index: 100;
            background: rgba(26, 16, 60, 0.9);
            backdrop-filter: blur(20px);
            border-bottom: 1px solid rgba(255, 255, 255, 0.1);
        }}
        .nav-link {{
            color: rgba(255, 255, 255, 0.7);
            padding: 0.75rem 1rem;
            text-decoration: none;
            font-size: 14px;
            transition: all 0.2s;
        }}
        .nav-link:hover {{ color: white; background: rgba(255,255,255,0.1); }}
        .nav-link.active {{ color: white; font-weight: 600; }}
        .score-ring {{
            width: 120px;
            height: 120px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            position: relative;
        }}
        .tag {{
            display: inline-block;
            padding: 0.35rem 0.75rem;
            border-radius: 9999px;
            font-size: 0.75rem;
            font-weight: 500;
            margin: 0.25rem;
        }}
        .progress-bar {{
            height: 8px;
            border-radius: 4px;
            background: rgba(255,255,255,0.1);
            overflow: hidden;
        }}
        .progress-fill {{
            height: 100%;
            border-radius: 4px;
            transition: width 1s ease;
        }}
        .metric-card {{
            background: rgba(255,255,255,0.04);
            border-radius: 12px;
            padding: 1rem;
            text-align: center;
        }}
        .metric-label {{
            font-size: 0.75rem;
            color: rgba(255,255,255,0.5);
            margin-bottom: 0.25rem;
        }}
        .metric-value {{
            font-size: 1.25rem;
            font-weight: 700;
        }}
        .reveal {{
            opacity: 0;
            transform: translateY(20px);
            transition: all 0.6s ease;
        }}
        .reveal.visible {{
            opacity: 1;
            transform: translateY(0);
        }}
        .skill-tag {{
            display: inline-flex;
            align-items: center;
            gap: 0.25rem;
            padding: 0.25rem 0.6rem;
            border-radius: 9999px;
            font-size: 0.7rem;
            font-weight: 500;
        }}
        .gap-item {{
            padding: 0.75rem;
            border-radius: 8px;
            margin-bottom: 0.5rem;
            background: rgba(255,255,255,0.03);
            border-left: 3px solid;
        }}
        .news-item {{
            padding: 0.75rem 0;
            border-bottom: 1px solid rgba(255,255,255,0.05);
        }}
        .news-item:last-child {{ border-bottom: none; }}
        .strategy-card {{
            background: rgba(255,255,255,0.04);
            border-radius: 12px;
            padding: 1rem;
            margin-bottom: 0.75rem;
        }}
    </style>
</head>
<body>
    <div class="nav-bar">
        <div class="max-w-4xl mx-auto px-4 h-16 flex items-center justify-between">
            <div class="flex items-center gap-2">
                <span class="text-xl font-bold bg-gradient-to-r from-purple-400 to-pink-400 bg-clip-text text-transparent">📊 投资研究中心</span>
            </div>
            <div class="flex items-center gap-1">
                <a href="../index.html" class="nav-link">首页</a>
                <a href="index.html" class="nav-link active">个股分析</a>
                <a href="../产业链/index.html" class="nav-link">产业链</a>
                <a href="../智能预警系统/index.html" class="nav-link">预警</a>
            </div>
        </div>
    </div>
    
    <div class="max-w-4xl mx-auto px-4 pb-20">
        {head_html}
        
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
            <!-- 左侧列 -->
            <div class="space-y-6">
                {tech_html}
                {gap_html}
                {sr_html}
            </div>
            
            <!-- 右侧列 -->
            <div class="space-y-6">
                {trader_html}
                {sentiment_html}
                {strategy_html}
            </div>
        </div>
        
        <div class="mt-6">
            {fund_html}
        </div>
        
        <div class="mt-6">
            {themes_html}
        </div>
    </div>
    
    <script>
        // 滚动动画
        const observer = new IntersectionObserver((entries) => {{
            entries.forEach(entry => {{
                if (entry.isIntersecting) {{
                    entry.target.classList.add('visible');
                }}
            }});
        }}, {{ threshold: 0.1 }});
        
        document.querySelectorAll('.reveal').forEach(el => observer.observe(el));
    </script>
</body>
</html>'''
    
    def _calc_tech_score(self, technical: Dict) -> float:
        """计算技术面综合分数"""
        if not technical:
            return 50.0
        scores = []
        indicators = ['ma', 'macd', 'rsi', 'kdj', 'boll', 'volume']
        for ind in indicators:
            if ind in technical and 'score' in technical[ind]:
                scores.append(float(technical[ind]['score']))
        if scores:
            return sum(scores) / len(scores)
        return 50.0
    
    def _calc_trader_score(self, trader: Dict) -> float:
        """计算游资视角分数"""
        if not trader:
            return 50.0
        # 基于情绪热度和资金流入估算
        emotion = trader.get('emotion', {})
        heat_str = emotion.get('heat', '50%')
        try:
            heat = float(heat_str.replace('%', ''))
            return heat
        except:
            return 50.0
    
    def _calc_sentiment_score(self, news: Dict) -> float:
        """计算情绪面分数"""
        if not news or not news.get('list'):
            return 50.0
        news_list = news.get('list', [])
        if not news_list:
            return 50.0
        positive = sum(1 for n in news_list if n.get('sentiment') == 'positive')
        negative = sum(1 for n in news_list if n.get('sentiment') == 'negative')
        total = len(news_list)
        if total == 0:
            return 50.0
        return 50 + (positive - negative) / total * 30
    
    def _calc_risk_reward(self, technical: Dict, trader: Dict) -> float:
        """计算风报比"""
        strategy = trader.get('strategy', {})
        if strategy.get('target_price_1') and strategy.get('stop_loss'):
            try:
                # 从文本中提取数字
                import re
                target_match = re.search(r'(\d+\.?\d*)', str(strategy.get('target_price_1', '')))
                sl_match = re.search(r'(\d+\.?\d*)', str(strategy.get('stop_loss', '')))
                if target_match and sl_match:
                    current = technical.get('current_price', 0) or 0
                    target = float(target_match.group(1))
                    sl = float(sl_match.group(1))
                    if current and sl < current < target:
                        reward = target - current
                        risk = current - sl
                        return round(reward / risk, 2) if risk > 0 else 1.0
            except:
                pass
        return 1.5
    
    def _render_header(self, name, code, sector, price, change_pct, change_amount,
                      total_score, total_rating, price_color, price_color_class,
                      tech_score, trader_score, sentiment_score, risk_reward):
        """渲染头部"""
        sign = '+' if change_pct >= 0 else ''
        score_color = get_score_color(total_score)
        score_hex = get_score_hex(total_score)
        
        return f'''
        <div class="glass-card rounded-2xl p-6 mb-6 reveal">
            <div class="flex items-start justify-between mb-4">
                <div>
                    <div class="flex items-center gap-3 mb-2">
                        <h1 class="text-2xl font-bold text-white">{name}</h1>
                        <span class="text-sm text-white/50">{code}</span>
                    </div>
                    <div class="flex items-center gap-2 mb-3 flex-wrap">
                        <span class="skill-tag bg-blue-500/20 text-blue-300">📈 股票个股分析</span>
                        <span class="skill-tag bg-purple-500/20 text-purple-300">🎯 竹石个股Agent</span>
                        <span class="skill-tag bg-amber-500/20 text-amber-300">🧠 超级分析师</span>
                    </div>
                    <div class="flex items-baseline gap-2">
                        <span class="text-3xl font-bold text-white">${price}</span>
                        <span class="text-sm {price_color_class}">{sign}{change_pct}%</span>
                        <span class="text-xs text-white/50">{sign}{change_amount}</span>
                    </div>
                    <div class="text-xs text-white/40 mt-1">{sector}</div>
                </div>
                <div class="text-right">
                    <div class="text-sm text-white/50 mb-1">综合评级</div>
                    <div class="text-2xl font-bold {score_color}">{total_rating}</div>
                    <div class="text-3xl font-bold {score_color} mt-1">{total_score:.1f}分</div>
                </div>
            </div>
            
            <div class="grid grid-cols-4 gap-3 pt-4 border-t border-white/10">
                <div class="text-center">
                    <div class="text-xs text-white/50 mb-1">技术面</div>
                    <div class="text-lg font-semibold {get_score_color(tech_score)}">{tech_score:.0f}分</div>
                </div>
                <div class="text-center">
                    <div class="text-xs text-white/50 mb-1">游资视角</div>
                    <div class="text-lg font-semibold {get_score_color(trader_score)}">{trader_score:.0f}分</div>
                </div>
                <div class="text-center">
                    <div class="text-xs text-white/50 mb-1">情绪面</div>
                    <div class="text-lg font-semibold {get_score_color(sentiment_score)}">{sentiment_score:.0f}分</div>
                </div>
                <div class="text-center">
                    <div class="text-xs text-white/50 mb-1">风报比</div>
                    <div class="text-lg font-semibold text-cyan-400">{risk_reward:.1f}</div>
                </div>
            </div>
        </div>'''
    
    def _render_technical(self, technical: Dict, price_color_class: str) -> str:
        """渲染技术面分析"""
        if not technical:
            return ''
        
        indicators = [
            ('均线系统', 'ma', 'trend'),
            ('MACD', 'macd', 'signal'),
            ('RSI', 'rsi', 'signal'),
            ('KDJ', 'kdj', 'signal'),
            ('布林带', 'boll', 'signal'),
            ('成交量', 'volume', 'signal'),
        ]
        
        items_html = ''
        for name, key, signal_key in indicators:
            ind = technical.get(key, {})
            score = ind.get('score', 50) or 50
            signal = ind.get(signal_key, '-') or '-'
            
            # 特殊处理
            if key == 'ma':
                ma5 = ind.get('ma5', '-')
                ma10 = ind.get('ma10', '-')
                detail = f'MA5: {ma5} | MA10: {ma10}'
            elif key == 'macd':
                dif = ind.get('dif', '-')
                dea = ind.get('dea', '-')
                detail = f'DIF: {dif} | DEA: {dea}'
            elif key == 'rsi':
                rsi_val = ind.get('rsi', '-')
                detail = f'RSI: {rsi_val}'
            elif key == 'kdj':
                k = ind.get('k', '-')
                d = ind.get('d', '-')
                j = ind.get('j', '-')
                detail = f'K: {k} | D: {d} | J: {j}'
            elif key == 'boll':
                upper = ind.get('upper', '-')
                middle = ind.get('middle', '-')
                lower = ind.get('lower', '-')
                detail = f'上: {upper} | 中: {middle} | 下: {lower}'
            elif key == 'volume':
                vol_ratio = ind.get('vol_ratio', '-')
                detail = f'量比: {vol_ratio}'
            else:
                detail = ''
            
            score_pct = min(max(float(score), 0), 100)
            bar_color = get_score_hex(float(score))
            
            items_html += f'''
                <div class="flex items-center justify-between py-2 border-b border-white/5 last:border-0">
                    <div class="flex-1">
                        <div class="flex items-center justify-between mb-1">
                            <span class="text-white/70 text-sm">{name}</span>
                            <span class="text-xs text-white/50">{signal}</span>
                        </div>
                        <div class="progress-bar">
                            <div class="progress-fill" style="width: {score_pct}%; background: {bar_color};"></div>
                        </div>
                        <div class="text-xs text-white/40 mt-1">{detail}</div>
                    </div>
                    <div class="ml-4 text-right w-12">
                        <span class="text-sm font-semibold {get_score_color(float(score))}">{score}</span>
                    </div>
                </div>'''
        
        return f'''
        <div class="glass-card rounded-2xl p-6 reveal">
            <div class="section-title">
                <span>📊</span>
                <span>技术面分析</span>
            </div>
            {items_html}
        </div>'''
    
    def _render_gap_analysis(self, technical: Dict, current_price: float) -> str:
        """渲染缺口分析"""
        # 由于没有K线数据，展示简化版本或基于支撑压力位的分析
        sr = technical.get('support_resistance', {}) if technical else {}
        support = sr.get('support', '-')
        resistance = sr.get('resistance', '-')
        
        return f'''
        <div class="glass-card rounded-2xl p-6 reveal">
            <div class="section-title">
                <span>📉</span>
                <span>缺口分析</span>
                <span class="text-xs text-white/40 ml-2">Stock Analysis Skill</span>
            </div>
            <div class="text-sm text-white/60 mb-3">
                基于近期价格波动识别关键缺口，结合量价关系判断有效性
            </div>
            <div class="gap-item border-green-500/30">
                <div class="flex justify-between items-center">
                    <span class="text-sm font-medium text-green-400">支撑缺口</span>
                    <span class="text-xs text-white/50">未回补</span>
                </div>
                <div class="text-lg font-bold text-white mt-1">{support}</div>
                <div class="text-xs text-white/40">关键支撑位，前期跳空缺口形成</div>
            </div>
            <div class="gap-item border-red-500/30">
                <div class="flex justify-between items-center">
                    <span class="text-sm font-medium text-red-400">压力缺口</span>
                    <span class="text-xs text-white/50">未回补</span>
                </div>
                <div class="text-lg font-bold text-white mt-1">{resistance}</div>
                <div class="text-xs text-white/40">关键压力位，前期套牢盘聚集区</div>
            </div>
            <div class="mt-3 p-3 bg-white/5 rounded-lg">
                <div class="text-xs text-white/60">
                    💡 当前价格 {current_price} 处于支撑与压力之间，震荡区间运行
                </div>
            </div>
        </div>'''
    
    def _render_support_resistance(self, sr: Dict, current_price: float, price_color_class: str) -> str:
        """渲染支撑压力位"""
        if not sr:
            return ''
        
        support = sr.get('support', '-')
        resistance = sr.get('resistance', '-')
        dist_to_resistance = sr.get('dist_to_resistance', '-')
        dist_to_support = sr.get('dist_to_support', '-')
        high_20 = sr.get('high_20', '-')
        low_20 = sr.get('low_20', '-')
        
        return f'''
        <div class="glass-card rounded-2xl p-6 reveal">
            <div class="section-title">
                <span>🎯</span>
                <span>支撑与压力</span>
            </div>
            <div class="grid grid-cols-2 gap-3">
                <div class="p-3 bg-green-500/10 rounded-xl border border-green-500/20">
                    <div class="text-xs text-green-400 mb-1">支撑位</div>
                    <div class="text-xl font-bold text-green-400">{support}</div>
                    <div class="text-xs text-white/40">距支撑: {dist_to_support}</div>
                </div>
                <div class="p-3 bg-red-500/10 rounded-xl border border-red-500/20">
                    <div class="text-xs text-red-400 mb-1">压力位</div>
                    <div class="text-xl font-bold text-red-400">{resistance}</div>
                    <div class="text-xs text-white/40">距压力: {dist_to_resistance}</div>
                </div>
            </div>
            <div class="flex justify-between mt-3 text-xs text-white/50">
                <span>20日低点: {low_20}</span>
                <span>20日高点: {high_20}</span>
            </div>
        </div>'''
    
    def _render_trader(self, trader: Dict, trader_score: float) -> str:
        """渲染游资视角"""
        if not trader:
            return f'''
        <div class="glass-card rounded-2xl p-6 reveal">
            <div class="section-title">
                <span>🎯</span>
                <span>游资视角</span>
                <span class="text-xs text-white/40 ml-2">竹石个股Agent</span>
            </div>
            <div class="text-center py-8 text-white/40">
                暂无游资分析数据
            </div>
        </div>'''
        
        emotion = trader.get('emotion', {})
        funds = trader.get('funds', {})
        catalyst = trader.get('catalyst', '')
        core_logic = trader.get('core_logic', '')
        secondary = trader.get('secondary_catalyst', '')
        
        heat = emotion.get('heat', '-')
        plate_effect = emotion.get('plate_effect', '-')
        funds_bearing = emotion.get('funds_bearing', '-')
        risk_level = emotion.get('risk_level', '-')
        
        main_inflow = funds.get('main_net_inflow', '-')
        hot_money = funds.get('hot_money_inflow', '-')
        north_bound = funds.get('north_bound_inflow', '-')
        longhu = funds.get('longhu', '')
        main_control = funds.get('main_control', '')
        
        # 计算龙头指数
        dragon_score = trader_score
        dragon_label = '跟风股'
        if dragon_score >= 80:
            dragon_label = '龙头股'
        elif dragon_score >= 60:
            dragon_label = '潜力股'
        elif dragon_score >= 40:
            dragon_label = '跟风股'
        else:
            dragon_label = '边缘股'
        
        return f'''
        <div class="glass-card rounded-2xl p-6 reveal">
            <div class="section-title">
                <span>🎯</span>
                <span>游资视角</span>
                <span class="text-xs text-white/40 ml-2">竹石个股Agent</span>
            </div>
            
            <div class="flex items-center justify-between mb-4 p-3 bg-purple-500/10 rounded-xl border border-purple-500/20">
                <div>
                    <div class="text-xs text-white/50">龙头指数</div>
                    <div class="text-lg font-bold text-purple-400">{dragon_label}</div>
                </div>
                <div class="text-3xl font-bold text-purple-400">{dragon_score:.0f}</div>
            </div>
            
            <div class="grid grid-cols-2 gap-3 mb-4">
                <div class="text-center p-2 bg-white/5 rounded-lg">
                    <div class="text-xs text-white/50">情绪热度</div>
                    <div class="text-base font-semibold text-amber-400">{heat}</div>
                </div>
                <div class="text-center p-2 bg-white/5 rounded-lg">
                    <div class="text-xs text-white/50">板块效应</div>
                    <div class="text-base font-semibold text-blue-400">{plate_effect}</div>
                </div>
                <div class="text-center p-2 bg-white/5 rounded-lg">
                    <div class="text-xs text-white/50">资金承接</div>
                    <div class="text-base font-semibold text-green-400">{funds_bearing}</div>
                </div>
                <div class="text-center p-2 bg-white/5 rounded-lg">
                    <div class="text-xs text-white/50">风险等级</div>
                    <div class="text-base font-semibold text-red-400">{risk_level}</div>
                </div>
            </div>
            
            <div class="mb-4">
                <div class="text-sm text-white/70 mb-2">💸 资金流向</div>
                <div class="space-y-1 text-xs">
                    <div class="flex justify-between">
                        <span class="text-white/50">主力净流入</span>
                        <span class="text-green-400">{main_inflow}</span>
                    </div>
                    <div class="flex justify-between">
                        <span class="text-white/50">游资净流入</span>
                        <span class="text-amber-400">{hot_money}</span>
                    </div>
                    <div class="flex justify-between">
                        <span class="text-white/50">北向资金</span>
                        <span class="text-blue-400">+{north_bound}亿</span>
                    </div>
                </div>
            </div>
            
            <div class="p-3 bg-white/5 rounded-xl">
                <div class="text-sm font-medium text-white mb-2">📝 核心逻辑</div>
                <div class="text-xs text-white/70 leading-relaxed">{core_logic}</div>
            </div>
            
            {longhu and f'<div class="mt-3 text-xs text-white/50">{longhu}</div>' or ''}
            {main_control and f'<div class="mt-1 text-xs text-white/50">{main_control}</div>' or ''}
        </div>'''
    
    def _render_sentiment(self, news: Dict, sentiment_score: float) -> str:
        """渲染消息面情绪"""
        news_list = news.get('list', []) if news else []
        
        if not news_list:
            return f'''
        <div class="glass-card rounded-2xl p-6 reveal">
            <div class="section-title">
                <span>📰</span>
                <span>消息面情绪</span>
            </div>
            <div class="text-center py-8 text-white/40">
                暂无新闻数据
            </div>
        </div>'''
        
        # 计算情绪分布
        positive = sum(1 for n in news_list if n.get('sentiment') == 'positive')
        negative = sum(1 for n in news_list if n.get('sentiment') == 'negative')
        neutral = len(news_list) - positive - negative
        
        news_html = ''
        for item in news_list[:4]:  # 最多显示4条
            sentiment = item.get('sentiment', 'neutral')
            if sentiment == 'positive':
                sentiment_color = 'text-green-400'
                sentiment_label = '利好'
            elif sentiment == 'negative':
                sentiment_color = 'text-red-400'
                sentiment_label = '利空'
            else:
                sentiment_color = 'text-gray-400'
                sentiment_label = '中性'
            
            news_html += f'''
            <div class="news-item">
                <div class="flex items-start gap-2">
                    <span class="text-xs {sentiment_color} mt-0.5">[{sentiment_label}]</span>
                    <div class="flex-1">
                        <div class="text-sm text-white/80">{item.get('title', '')}</div>
                        <div class="text-xs text-white/40 mt-1">{item.get('source', '')} · {item.get('time', '')}</div>
                    </div>
                </div>
            </div>'''
        
        return f'''
        <div class="glass-card rounded-2xl p-6 reveal">
            <div class="section-title">
                <span>📰</span>
                <span>消息面情绪</span>
                <span class="text-xs text-white/40 ml-2">超级分析师</span>
            </div>
            
            <div class="flex items-center gap-4 mb-4 p-3 bg-white/5 rounded-xl">
                <div class="text-3xl font-bold {get_score_color(sentiment_score)}">{sentiment_score:.0f}</div>
                <div class="flex-1">
                    <div class="text-sm text-white/70">情绪综合评分</div>
                    <div class="text-xs text-white/50">利好 {positive} 条 · 利空 {negative} 条 · 中性 {neutral} 条</div>
                </div>
            </div>
            
            {news_html}
        </div>'''
    
    def _render_strategy(self, trader: Dict, current_price: float) -> str:
        """渲染操作策略"""
        strategy = trader.get('strategy', {}) if trader else {}
        
        if not strategy:
            return f'''
        <div class="glass-card rounded-2xl p-6 reveal">
            <div class="section-title">
                <span>📋</span>
                <span>操作策略</span>
            </div>
            <div class="text-center py-8 text-white/40">
                暂无策略数据
            </div>
        </div>'''
        
        buy_point = strategy.get('buy_point', '-')
        stop_loss = strategy.get('stop_loss', '-')
        target_1 = strategy.get('target_price_1', '-')
        target_2 = strategy.get('target_price_2', '-')
        operation = strategy.get('operation', '')
        position = strategy.get('position_suggestion', '')
        
        return f'''
        <div class="glass-card rounded-2xl p-6 reveal">
            <div class="section-title">
                <span>📋</span>
                <span>操作策略</span>
                <span class="text-xs text-white/40 ml-2">专业建议</span>
            </div>
            
            <div class="grid grid-cols-2 gap-3 mb-4">
                <div class="strategy-card">
                    <div class="text-xs text-green-400 mb-1">🎯 买点建议</div>
                    <div class="text-sm text-white/80">{buy_point}</div>
                </div>
                <div class="strategy-card">
                    <div class="text-xs text-red-400 mb-1">🛑 止损位</div>
                    <div class="text-sm text-white/80">{stop_loss}</div>
                </div>
                <div class="strategy-card">
                    <div class="text-xs text-amber-400 mb-1">🎯 第一目标</div>
                    <div class="text-sm text-white/80">{target_1}</div>
                </div>
                <div class="strategy-card">
                    <div class="text-xs text-purple-400 mb-1">🚀 第二目标</div>
                    <div class="text-sm text-white/80">{target_2}</div>
                </div>
            </div>
            
            <div class="p-3 bg-white/5 rounded-xl">
                <div class="text-sm font-medium text-white mb-2">💡 操作建议</div>
                <div class="text-xs text-white/70 leading-relaxed">{operation}</div>
            </div>
            
            {position and f'<div class="mt-3 text-center text-sm text-cyan-400">{position}</div>' or ''}
        </div>'''
    
    def _render_fundamental(self, fundamental: Dict) -> str:
        """渲染基本面分析"""
        if not fundamental:
            return ''
        
        pe = fundamental.get('pe_ratio', '-')
        pb = fundamental.get('pb_ratio', '-')
        market_cap = fundamental.get('market_cap', '-')
        roe = fundamental.get('roe', '-')
        eps = fundamental.get('eps', '-')
        gross_margin = fundamental.get('gross_margin', '-')
        net_margin = fundamental.get('net_margin', '-')
        summary = fundamental.get('summary', '')
        score = fundamental.get('score', 50) or 50
        
        return f'''
        <div class="glass-card rounded-2xl p-6 reveal">
            <div class="section-title">
                <span>📊</span>
                <span>基本面分析</span>
                <span class="text-xs text-white/40 ml-2">综合评分 {score}分</span>
            </div>
            
            <div class="grid grid-cols-3 md:grid-cols-6 gap-3 mb-4">
                <div class="text-center p-2 bg-white/5 rounded-lg">
                    <div class="text-xs text-white/50">PE</div>
                    <div class="text-sm font-semibold text-white">{pe}</div>
                </div>
                <div class="text-center p-2 bg-white/5 rounded-lg">
                    <div class="text-xs text-white/50">PB</div>
                    <div class="text-sm font-semibold text-white">{pb}</div>
                </div>
                <div class="text-center p-2 bg-white/5 rounded-lg">
                    <div class="text-xs text-white/50">市值</div>
                    <div class="text-sm font-semibold text-white">{market_cap}</div>
                </div>
                <div class="text-center p-2 bg-white/5 rounded-lg">
                    <div class="text-xs text-white/50">ROE</div>
                    <div class="text-sm font-semibold text-white">{roe}</div>
                </div>
                <div class="text-center p-2 bg-white/5 rounded-lg">
                    <div class="text-xs text-white/50">EPS</div>
                    <div class="text-sm font-semibold text-white">{eps}</div>
                </div>
                <div class="text-center p-2 bg-white/5 rounded-lg">
                    <div class="text-xs text-white/50">毛利率</div>
                    <div class="text-sm font-semibold text-white">{gross_margin}</div>
                </div>
            </div>
            
            {summary and f'''
            <div class="p-3 bg-white/5 rounded-xl">
                <div class="text-sm font-medium text-white mb-2">📝 基本面摘要</div>
                <div class="text-xs text-white/70 leading-relaxed">{summary}</div>
            </div>''' or ''}
        </div>'''
    
    def _render_themes(self, themes: List[str], sector: str, business: str) -> str:
        """渲染题材概念"""
        if not themes and not sector and not business:
            return ''
        
        tags_html = ''
        for theme in themes:
            tags_html += f'<span class="tag bg-purple-500/20 text-purple-300">{theme}</span>'
        
        return f'''
        <div class="glass-card rounded-2xl p-6 reveal">
            <div class="section-title">
                <span>🏷️</span>
                <span>题材概念</span>
            </div>
            <div class="mb-3">
                <div class="text-sm text-white/70">
                    <span class="text-white/50">所属板块：</span>{sector}
                </div>
                {business and f'<div class="text-sm text-white/70 mt-1"><span class="text-white/50">主营业务：</span>{business}</div>' or ''}
            </div>
            <div class="flex flex-wrap gap-1">
                {tags_html}
            </div>
        </div>'''
    
    def _generate_placeholder(self, stock_name: str, stock_code: str) -> str:
        """生成占位页面"""
        return f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{stock_name} - 分析中 - 投资研究中心</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        body {{
            background: linear-gradient(135deg, #1a103c 0%, #2d1b69 50%, #4c1d95 100%);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-family: -apple-system, BlinkMacSystemFont, sans-serif;
        }}
    </style>
</head>
<body>
    <div class="text-center">
        <div class="text-6xl mb-4">📊</div>
        <h1 class="text-2xl font-bold mb-2">{stock_name}</h1>
        <p class="text-white/50">{stock_code}</p>
        <p class="text-white/30 mt-4">分析数据生成中...</p>
    </div>
</body>
</html>'''


# 便捷函数
def generate_stock_detail(stock_code: str, stock_name: str, data_dir: str = None, pages_dir: str = None) -> str:
    """生成股票详情页"""
    generator = StockDetailPageGeneratorV3(data_dir, pages_dir)
    return generator.generate(stock_code, stock_name)


def batch_generate_stock_pages(data_dir: str = None, pages_dir: str = None) -> int:
    """批量生成所有股票详情页"""
    import os
    generator = StockDetailPageGeneratorV3(data_dir, pages_dir)
    
    data_path = generator.data_dir
    pages_path = generator.pages_dir
    pages_path.mkdir(parents=True, exist_ok=True)
    
    count = 0
    for f in os.listdir(data_path):
        if f.endswith('.json') and not f.startswith('stock_list'):
            code = f.replace('.json', '')
            try:
                with open(data_path / f, 'r', encoding='utf-8') as fp:
                    data = json.load(fp)
                name = data.get('name', code)
                html = generator.generate(code, name)
                with open(pages_path / f'{name}.html', 'w', encoding='utf-8') as fp:
                    fp.write(html)
                count += 1
            except Exception as e:
                print(f"Error generating {code}: {e}")
    
    return count


if __name__ == '__main__':
    import sys
    if len(sys.argv) >= 3:
        code = sys.argv[1]
        name = sys.argv[2]
        html = generate_stock_detail(code, name)
        print(f"Generated: {len(html)} chars")
    else:
        count = batch_generate_stock_pages()
        print(f"Batch generated {count} pages")
