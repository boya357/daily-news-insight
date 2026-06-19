"""
统一股票详情页生成器 V2
- 修复空值处理
- 基于统一JSON数据生成
- 深色玻璃态风格
"""

import os
import json
from pathlib import Path
from typing import Dict, Optional


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


class StockDetailPageGenerator:
    """股票详情页生成器"""
    
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
        
        technical = data.get('technical', {})
        fundamental = data.get('fundamental', {})
        sr = technical.get('support_resistance', {}) if technical else {}
        themes = data.get('themes', [])
        
        head_section = self._render_head(name, code, sector, price, change_pct, change_amount, total_score, total_rating, price_color)
        tech_section = self._render_technical(technical, price_color)
        sr_section = self._render_sr(sr, price, price_color)
        fund_section = self._render_fundamental(fundamental)
        themes_section = self._render_themes(themes, sector, business)
        
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
            background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 50%, #312e81 100%);
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
            background: rgba(15, 23, 42, 0.9);
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
            </div>
        </div>
    </div>

    <div class="max-w-4xl mx-auto px-4 pb-20">
        {head_section}
        
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div class="md:col-span-1 reveal">
                {tech_section}
            </div>
            <div class="md:col-span-1 reveal">
                {sr_section}
                {fund_section}
            </div>
        </div>
        
        <div class="reveal">
            {themes_section}
        </div>
    </div>

    <script>
        function initReveal() {{
            const reveals = document.querySelectorAll('.reveal');
            const observer = new IntersectionObserver((entries) => {{
                entries.forEach(entry => {{
                    if (entry.isIntersecting) {{
                        entry.target.classList.add('visible');
                    }}
                }});
            }}, {{ threshold: 0.1 }});
            reveals.forEach(el => observer.observe(el));
        }}
        document.addEventListener('DOMContentLoaded', function() {{
            initReveal();
        }});
    </script>
</body>
</html>'''
    
    def _render_head(self, name, code, sector, price, change_pct, change_amount, total_score, total_rating, price_color):
        change_sign = '+' if change_pct >= 0 else ''
        
        score_color = '#10b981' if total_score >= 70 else ('#f59e0b' if total_score >= 50 else '#ef4444')
        
        return f'''
        <div class="glass-card p-8 mb-6 reveal">
            <div class="flex flex-wrap items-start justify-between gap-6">
                <div>
                    <div class="flex items-center gap-3 mb-2 flex-wrap">
                        <h1 class="text-3xl font-bold">{name}</h1>
                        <span class="text-sm text-white/50">{code}</span>
                    </div>
                    <div class="flex items-center gap-2 mb-4">
                        <span class="px-3 py-1 bg-purple-500/20 text-purple-300 rounded-full text-xs font-medium">
                            {sector}
                        </span>
                    </div>
                    <div class="flex items-baseline gap-3">
                        <span class="text-4xl font-bold" style="color: {price_color}">{safe_num(price)}</span>
                        <span class="text-lg font-semibold" style="color: {price_color}">
                            {change_sign}{safe_num(change_pct)}%</span>
                        <span class="text-sm text-white/50">
                            {change_sign}{safe_num(change_amount)}
                        </span>
                    </div>
                </div>
                
                <div class="text-center">
                    <div class="score-ring" style="background: conic-gradient({score_color} {total_score * 3.6}deg, rgba(255,255,255,0.1) 0deg);">
                        <div style="background: #1e1b4b; width: 90px; height: 90px; border-radius: 50%; display: flex; align-items: center; justify-content: center;">
                            <span style="color: {score_color}; font-size: 1.8rem;">{safe_num(total_score, fmt='.1f')}</span>
                        </div>
                    </div>
                    <div class="mt-2 text-sm text-white/70">综合评分</div>
                    <div class="text-lg font-bold" style="color: {score_color}">{total_rating}</div>
                </div>
            </div>
        </div>
        '''
    
    def _render_technical(self, technical, price_color):
        if not technical:
            return ''
        
        indicators = []
        
        ma = technical.get('ma', {})
        if ma:
            indicators.append({
                'name': '均线系统',
                'score': ma.get('score', 50) or 50,
                'desc': ma.get('trend', ''),
                'details': [
                    ('MA5', safe_num(ma.get('ma5', 0))),
                    ('MA10', safe_num(ma.get('ma10', 0))),
                    ('MA20', safe_num(ma.get('ma20', 0))),
                    ('MA60', safe_num(ma.get('ma60', 0))),
                ]
            })
        
        macd = technical.get('macd', {})
        if macd:
            indicators.append({
                'name': 'MACD',
                'score': macd.get('score', 50) or 50,
                'desc': macd.get('signal', ''),
                'details': [
                    ('DIF', safe_num(macd.get('dif', 0), fmt='.3f')),
                    ('DEA', safe_num(macd.get('dea', 0), fmt='.3f')),
                    ('MACD', safe_num(macd.get('macd', 0), fmt='.3f')),
                ]
            })
        
        rsi = technical.get('rsi', {})
        if rsi:
            indicators.append({
                'name': 'RSI',
                'score': rsi.get('score', 50) or 50,
                'desc': rsi.get('signal', ''),
                'details': [
                    ('RSI', safe_num(rsi.get('rsi', 0))),
                ]
            })
        
        kdj = technical.get('kdj', {})
        if kdj:
            indicators.append({
                'name': 'KDJ',
                'score': kdj.get('score', 50) or 50,
                'desc': kdj.get('signal', ''),
                'details': [
                    ('K', safe_num(kdj.get('k', 0))),
                    ('D', safe_num(kdj.get('d', 0))),
                    ('J', safe_num(kdj.get('j', 0))),
                ]
            })
        
        boll = technical.get('boll', {})
        if boll:
            indicators.append({
                'name': '布林带',
                'score': boll.get('score', 50) or 50,
                'desc': boll.get('signal', ''),
                'details': [
                    ('上轨', safe_num(boll.get('upper', 0))),
                    ('中轨', safe_num(boll.get('middle', 0))),
                    ('下轨', safe_num(boll.get('lower', 0))),
                ]
            })
        
        vol = technical.get('volume', {})
        if vol:
            indicators.append({
                'name': '量能',
                'score': vol.get('score', 50) or 50,
                'desc': vol.get('signal', ''),
                'details': [
                    ('量比', safe_num(vol.get('vol_ratio', 0))),
                    ('5日均量', safe_num(vol.get('avg_vol_5', 0), fmt='.0f')),
                ]
            })
        
        tech_scores = [i['score'] for i in indicators]
        tech_total = sum(tech_scores) / len(tech_scores) if tech_scores else 50
        
        ind_html = ''
        for ind in indicators:
            sc = ind['score']
            sc_color = '#10b981' if sc >= 60 else ('#f59e0b' if sc >= 40 else '#ef4444')
            details_html = ''.join(
                f'<div class="flex justify-between text-xs py-1 border-b border-white/5 last:border-0"><span class="text-white/50">{d[0]}</span><span class="font-medium">{d[1]}</span></div>'
                for d in ind['details']
            )
            
            ind_html += f'''
            <div class="glass-card p-4">
                <div class="flex items-center justify-between mb-2">
                    <span class="font-semibold text-sm">{ind['name']}</span>
                    <span class="text-sm font-bold" style="color: {sc_color}">{safe_num(sc, fmt='.0f')}分</span>
                </div>
                <div class="progress-bar mb-2">
                    <div class="progress-fill" style="width: {sc}%; background: {sc_color};"></div>
                </div>
                <div class="text-xs text-white/60 mb-2">{ind['desc']}</div>
                {details_html}
            </div>
            '''
        
        return f'''
        <div class="glass-card p-6 mb-6">
            <h2 class="section-title">
                <span>📊</span> 技术面分析
                <span class="ml-auto text-sm font-normal text-white/50">
                    综合 <span class="font-bold text-white">{safe_num(tech_total, fmt='.0f')}</span> 分
                </span>
            </h2>
            <div class="grid grid-cols-2 gap-3">
                {ind_html}
            </div>
        </div>
        '''
    
    def _render_sr(self, sr, current_price, price_color):
        if not sr:
            return ''
        
        support = sr.get('support', 0) or 0
        resistance = sr.get('resistance', 0) or 0
        
        dist_to_resistance = sr.get('dist_to_resistance')
        dist_to_support = sr.get('dist_to_support')
        
        if dist_to_resistance is None and resistance and current_price:
            dist_to_resistance = (resistance - current_price) / current_price * 100
        if dist_to_support is None and support and current_price:
            dist_to_support = (current_price - support) / current_price * 100
        
        dist_to_resistance = dist_to_resistance or 0
        dist_to_support = dist_to_support or 0
        
        if resistance and support and resistance != support:
            position_pct = (current_price - support) / (resistance - support) * 100
            position_pct = max(5, min(95, position_pct))
        else:
            position_pct = 50
        
        return f'''
        <div class="glass-card p-6 mb-6">
            <h2 class="section-title">
                <span>🎯</span> 支撑位与压力位
            </h2>
            <div class="space-y-4">
                <div>
                    <div class="flex justify-between text-sm mb-1">
                        <span class="text-red-400">压力位</span>
                        <span class="font-bold text-red-400">{safe_num(resistance)}</span>
                    </div>
                    <div class="text-xs text-red-400/60">距当前价 {safe_num(dist_to_resistance)}%</div>
                </div>
                
                <div class="relative h-2 bg-white/10 rounded-full my-4">
                    <div class="absolute top-1/2 -translate-y-1/2 w-3 h-3 bg-white rounded-full shadow-lg" 
                         style="left: {position_pct}%;"></div>
                </div>
                
                <div>
                    <div class="flex justify-between text-sm mb-1">
                        <span class="text-green-400">支撑位</span>
                        <span class="font-bold text-green-400">{safe_num(support)}</span>
                    </div>
                    <div class="text-xs text-green-400/60">距当前价 {safe_num(dist_to_support)}%</div>
                </div>
                
                <div class="pt-3 mt-3 border-t border-white/10">
                    <div class="grid grid-cols-2 gap-3 text-xs">
                        <div>
                            <span class="text-white/50">20日高点</span>
                            <div class="font-medium">{safe_num(sr.get('high_20', 0))}</div>
                        </div>
                        <div>
                            <span class="text-white/50">20日低点</span>
                            <div class="font-medium">{safe_num(sr.get('low_20', 0))}</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        '''
    
    def _render_fundamental(self, fundamental):
        if not fundamental:
            return ''
        
        pe = fundamental.get('pe_ratio') or 0
        pb = fundamental.get('pb_ratio') or 0
        market_cap = fundamental.get('market_cap') or 0
        roe = fundamental.get('roe') or 0
        eps = fundamental.get('eps') or 0
        gross_margin = fundamental.get('gross_margin') or 0
        net_margin = fundamental.get('net_margin') or 0
        score = fundamental.get('score') or 0
        summary = fundamental.get('summary', '')
        
        return f'''
        <div class="glass-card p-6 mb-6">
            <h2 class="section-title">
                <span>💰</span> 基本面概览
                <span class="ml-auto text-sm font-normal text-white/50">
                    评分 <span class="font-bold text-white">{safe_num(score, fmt='.1f')}</span>
                </span>
            </h2>
            
            <div class="grid grid-cols-3 gap-3 mb-4">
                <div class="metric-card">
                    <div class="metric-label">市盈率(PE)</div>
                    <div class="metric-value">{safe_num(pe)}</div>
                </div>
                <div class="metric-card">
                    <div class="metric-label">市净率(PB)</div>
                    <div class="metric-value">{safe_num(pb)}</div>
                </div>
                <div class="metric-card">
                    <div class="metric-label">市值(亿)</div>
                    <div class="metric-value">{safe_num(market_cap, fmt='.1f')}</div>
                </div>
            </div>
            
            <div class="grid grid-cols-3 gap-3 mb-4">
                <div class="metric-card">
                    <div class="metric-label">ROE</div>
                    <div class="metric-value text-green-400">{safe_num(roe)}%</div>
                </div>
                <div class="metric-card">
                    <div class="metric-label">每股收益</div>
                    <div class="metric-value">{safe_num(eps)}</div>
                </div>
                <div class="metric-card">
                    <div class="metric-label">毛利率</div>
                    <div class="metric-value">{safe_num(gross_margin)}%</div>
                </div>
            </div>
            
            <p class="text-sm text-white/70 leading-relaxed">{summary}</p>
        </div>
        '''
    
    def _render_themes(self, themes, sector, business):
        if not themes and not sector:
            return ''
        
        tags_html = ''
        if sector:
            tags_html += f'<span class="tag bg-blue-500/20 text-blue-300">{sector}</span>'
        for theme in themes:
            if theme and theme != sector:
                tags_html += f'<span class="tag bg-purple-500/20 text-purple-300">{theme}</span>'
        
        business_html = f'<p class="mt-4 pt-4 border-t border-white/10 text-sm text-white/60">主营业务：{business}</p>' if business else ''
        
        return f'''
        <div class="glass-card p-6">
            <h2 class="section-title">
                <span>🏷️</span> 核心题材与概念
            </h2>
            <div class="flex flex-wrap gap-2">
                {tags_html}
            </div>
            {business_html}
        </div>
        '''
    
    def _generate_placeholder(self, stock_name, stock_code):
        return f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{stock_name} - 分析中</title>
</head>
<body>
    <h1>{stock_name} ({stock_code})</h1>
    <p>分析数据正在生成中...</p>
</body>
</html>'''
    
    def save_page(self, stock_name: str, stock_code: str) -> str:
        html = self.generate(stock_code, stock_name)
        output_path = self.pages_dir / f'{stock_name}.html'
        self.pages_dir.mkdir(parents=True, exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html)
        return str(output_path)


if __name__ == '__main__':
    gen = StockDetailPageGenerator()
    path = gen.save_page('英维克', '002837')
    print(f'页面已生成: {path}')
