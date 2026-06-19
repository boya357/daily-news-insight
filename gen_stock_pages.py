import os
import json

def gen_page(name, code, data):
    tech = data.get('technical', {})
    fund = data.get('fundamental', {})
    market = data.get('market', {})
    overall = data.get('overall', {})
    themes = data.get('themes', [])
    sector = data.get('sector', '')
    
    # 价格
    price = market.get('current_price', tech.get('current_price', 0))
    if not isinstance(price, (int, float)):
        price = float(price) if price else 0
    
    # 涨跌幅
    change = overall.get('change_pct', market.get('change_pct', 0))
    if change == 0:
        change = market.get('change_percent', 0)
    if not isinstance(change, (int, float)):
        change = float(change) if change else 0
    
    change_color = '#4ade80' if change >= 0 else '#f87171'
    change_icon = '📈' if change >= 0 else '📉'
    
    rating = overall.get('rating', '暂无')
    score = overall.get('score', 50)
    if not isinstance(score, (int, float)):
        score = float(score) if score else 50
    
    # 支撑压力位 - 可能是列表也可能是单个值
    sr = tech.get('support_resistance', {})
    if isinstance(sr, dict):
        resistance = sr.get('resistance', [])
        support = sr.get('support', [])
    else:
        resistance = []
        support = []
    
    # 统一转成列表
    if isinstance(resistance, (int, float)):
        resistance = [resistance]
    if isinstance(support, (int, float)):
        support = [support]
    if not isinstance(resistance, list):
        resistance = []
    if not isinstance(support, list):
        support = []
    
    # 压力位HTML
    p_html = ''
    for i, r in enumerate(resistance[:3]):
        if isinstance(r, (int, float)):
            p_html += f'<div class="flex justify-between bg-red-500/10 border border-red-500/20 rounded-lg px-4 py-2 mb-2"><span class="text-red-400 font-semibold">{r:.2f}</span><span class="text-red-400/60 text-xs">压力 {i+1}</span></div>'
    if not p_html:
        p_html = '<div class="text-white/40 text-sm">暂无数据</div>'
    
    s_html = ''
    for i, s in enumerate(support[:3]):
        if isinstance(s, (int, float)):
            s_html += f'<div class="flex justify-between bg-green-500/10 border border-green-500/20 rounded-lg px-4 py-2 mb-2"><span class="text-green-400 font-semibold">{s:.2f}</span><span class="text-green-400/60 text-xs">支撑 {i+1}</span></div>'
    if not s_html:
        s_html = '<div class="text-white/40 text-sm">暂无数据</div>'
    
    # 题材标签
    if isinstance(themes, list):
        t_html = ''.join([f'<span class="inline-block px-3 py-1 bg-blue-500/20 text-blue-300 text-xs rounded-full mr-1 mb-1">{t}</span>' for t in themes[:8] if isinstance(t, str)])
    else:
        t_html = ''
    
    # 技术指标
    tech_items = []
    macd = tech.get('macd', {})
    if isinstance(macd, dict):
        macd_val = macd.get('macd', 0)
        signal_val = macd.get('signal', 0)
        if isinstance(macd_val, (int, float)) and isinstance(signal_val, (int, float)):
            if macd_val > signal_val:
                tech_items.append(('MACD金叉', '多头趋势', 'text-green-400'))
            else:
                tech_items.append(('MACD死叉', '空头趋势', 'text-red-400'))
    
    rsi_data = tech.get('rsi', {})
    rsi_val = 50
    if isinstance(rsi_data, dict):
        rsi_val = rsi_data.get('rsi', 50)
    elif isinstance(rsi_data, (int, float)):
        rsi_val = rsi_data
    
    if isinstance(rsi_val, (int, float)):
        if rsi_val > 70:
            tech_items.append(('RSI超买', '短期或回调', 'text-yellow-400'))
        elif rsi_val < 30:
            tech_items.append(('RSI超卖', '短期或反弹', 'text-green-400'))
        else:
            tech_items.append(('RSI中性', '正常区间', 'text-white/60'))
    
    tech_html = ''.join([f'<div class="bg-white/5 rounded-lg p-3 border border-white/10"><div class="font-semibold {c} text-sm">{t}</div><div class="text-white/60 text-xs mt-1">{d}</div></div>' for t, d, c in tech_items])
    
    # MA均线
    ma = tech.get('ma', {})
    ma_items = []
    if isinstance(ma, dict):
        for k, label in [('ma5', 'MA5'), ('ma10', 'MA10'), ('ma20', 'MA20'), ('ma60', 'MA60')]:
            if k in ma and isinstance(ma[k], (int, float)):
                ma_items.append(f'<div class="text-center"><div class="text-white/50 text-xs">{label}</div><div class="font-semibold text-sm">{ma[k]:.2f}</div></div>')
    
    ma_html = ''.join(ma_items) if ma_items else '<div class="text-white/40 text-sm col-span-4 text-center">暂无数据</div>'
    
    # 基本面
    pe = fund.get('pe_ratio', '--')
    pb = fund.get('pb_ratio', '--')
    mcap = fund.get('market_cap', '--')
    roe = fund.get('roe', '--')
    summary = fund.get('summary', '暂无基本面分析数据')
    
    time = data.get('analyze_time', data.get('update_time', '未知'))
    
    html = f'''<!DOCTYPE html>
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
background: linear-gradient(135deg, #1e1b4b 0%, #312e81 50%, #4c1d95 100%);
min-height: 100vh; padding-top: 80px;
}}
.card-glass {{
background: rgba(255,255,255,0.08);
backdrop-filter: blur(20px);
border: 1px solid rgba(255,255,255,0.15);
box-shadow: 0 8px 32px rgba(0,0,0,0.3);
border-radius: 20px; color: white;
}}
.pro-container {{ max-width: 64rem; margin: 0 auto; padding: 0 1.5rem; }}
.section-title {{ font-size: 1.25rem; font-weight: 700; color: white; margin-bottom: 1rem; display: flex; align-items: center; gap: 0.5rem; }}
.nav-bar {{ position: fixed; top: 0; left: 0; right: 0; z-index: 100; background: rgba(15,23,42,0.8); backdrop-filter: blur(20px); border-bottom: 1px solid rgba(255,255,255,0.1); }}
.nav-link {{ color: rgba(255,255,255,0.7); padding: 0.75rem 1rem; text-decoration: none; font-size: 14px; transition: all 0.2s; }}
.nav-link:hover {{ color: white; background: rgba(255,255,255,0.1); }}
.nav-link.active {{ color: white; font-weight: 600; }}
</style>
</head>
<body class="text-white">

<div class="nav-bar">
<div class="max-w-6xl mx-auto px-4 h-16 flex items-center justify-between">
<div class="flex items-center gap-2">
<span class="text-xl font-bold bg-gradient-to-r from-purple-400 to-pink-400 bg-clip-text text-transparent">📊 投资研究中心</span>
</div>
<div class="flex items-center gap-1">
<a href="../index.html" class="nav-link">首页</a>
<a href="index.html" class="nav-link active">个股分析</a>
</div>
</div>
</div>

<div class="pro-container pb-20">

<div class="card-glass p-8 mb-6">
<div class="flex items-start justify-between flex-wrap gap-4">
<div>
<div class="flex items-center gap-3 mb-2 flex-wrap">
<h1 class="text-3xl font-bold">{name}</h1>
<span class="inline-block px-3 py-1 bg-white/10 text-white/70 text-xs rounded-full font-semibold">{code}</span>
{f'<span class="inline-block px-3 py-1 bg-purple-500/20 text-purple-300 text-xs rounded-full font-semibold">{sector}</span>' if sector else ''}
</div>
<div class="flex items-center gap-6 mt-4">
<div class="text-5xl font-black" style="color: {change_color}">{price:.2f}</div>
<div class="text-xl font-semibold" style="color: {change_color}">{change_icon} {change:+.2f}%</div>
</div>
</div>
<div class="flex items-center gap-6">
<div class="text-center">
<div class="text-white/50 text-sm mb-1">综合评级</div>
<div class="text-2xl font-bold text-white">{rating}</div>
</div>
<div class="text-center">
<div class="text-white/50 text-sm mb-1">综合评分</div>
<div class="text-3xl font-black text-yellow-400">{score:.0f}</div>
</div>
</div>
</div>
{f'''
<div class="mt-6 pt-6 border-t border-white/10">
<div class="text-sm text-white/50 mb-3">核心题材</div>
<div class="flex flex-wrap gap-2">{t_html}</div>
</div>
''' if themes and isinstance(themes, list) else ''}
</div>

<div class="grid grid-cols-2 md:grid-cols-4 gap-4 mb-6">
<div class="bg-white/5 backdrop-blur-sm rounded-xl p-4 text-center border border-white/10">
<div class="text-white/50 text-sm mb-2">市盈率 (TTM)</div>
<div class="text-2xl font-bold text-white">{pe}</div>
</div>
<div class="bg-white/5 backdrop-blur-sm rounded-xl p-4 text-center border border-white/10">
<div class="text-white/50 text-sm mb-2">市净率</div>
<div class="text-2xl font-bold text-white">{pb}</div>
</div>
<div class="bg-white/5 backdrop-blur-sm rounded-xl p-4 text-center border border-white/10">
<div class="text-white/50 text-sm mb-2">总市值</div>
<div class="text-2xl font-bold text-white">{mcap}</div>
</div>
<div class="bg-white/5 backdrop-blur-sm rounded-xl p-4 text-center border border-white/10">
<div class="text-white/50 text-sm mb-2">ROE</div>
<div class="text-2xl font-bold text-white">{roe}</div>
</div>
</div>

<div class="card-glass p-6 mb-6">
<h2 class="section-title">📊 技术面分析</h2>
<div class="grid md:grid-cols-2 gap-4 mb-4">
<div class="bg-white/5 rounded-xl p-4 border border-white/10">
<div class="font-semibold text-white mb-3">均线系统</div>
<div class="grid grid-cols-4 gap-2">{ma_html}</div>
</div>
</div>
<div class="grid grid-cols-2 md:grid-cols-3 gap-3">{tech_html}</div>
</div>

<div class="card-glass p-6 mb-6">
<h2 class="section-title">🎯 支撑位与压力位</h2>
<div class="grid md:grid-cols-2 gap-6">
<div>
<div class="text-sm text-white/50 mb-3">压力位</div>
{p_html}
</div>
<div>
<div class="text-sm text-white/50 mb-3">支撑位</div>
{s_html}
</div>
</div>
</div>

<div class="card-glass p-6 mb-6">
<h2 class="section-title">💰 基本面概览</h2>
<div class="bg-white/5 rounded-xl p-4 border border-white/10">
<div class="text-white/70 text-sm leading-relaxed">{summary}</div>
</div>
</div>

<div class="text-center text-white/40 text-sm mt-8">
<p>数据来源：自动化分析系统 | 分析时间：{time}</p>
<p class="mt-1">⚠️ 以上分析仅供参考，不构成投资建议。投资有风险，入市需谨慎。</p>
</div>

</div>

<script src="../js/stock-hover-card.js" defer></script>
</body>
</html>'''
    
    return html

def main():
    data_dir = 'docs/data/stock_analysis'
    output_dir = 'docs/个股分析'
    
    with open(f'{data_dir}/stock_list.json', 'r', encoding='utf-8') as f:
        stocks = json.load(f).get('stocks', {})
    
    print(f'股票总数: {len(stocks)}')
    
    missing = []
    for name, info in stocks.items():
        page_path = f'{output_dir}/{name}.html'
        if not os.path.exists(page_path):
            code = info.get('code', '') if isinstance(info, dict) else info
            missing.append((name, code))
    
    print(f'缺失页面数: {len(missing)}')
    
    success = 0
    for name, code in missing:
        data_file = f'{data_dir}/{code}.json'
        if not os.path.exists(data_file):
            print(f'  ⚠️ {name} 无数据')
            continue
        try:
            with open(data_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            html = gen_page(name, code, data)
            with open(f'{output_dir}/{name}.html', 'w', encoding='utf-8') as f:
                f.write(html)
            print(f'  ✅ {name}')
            success += 1
        except Exception as e:
            print(f'  ❌ {name}: {e}')
            import traceback
            traceback.print_exc()
    
    print(f'\n完成: 成功{success}个')
    total = len([f for f in os.listdir(output_dir) if f.endswith('.html')])
    print(f'总页面数: {total}')

if __name__ == '__main__':
    main()
