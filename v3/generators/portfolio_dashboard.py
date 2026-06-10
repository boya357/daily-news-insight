#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
持仓智能预警仪表盘生成器
数据驱动，UI完全沿用现有设计
"""

import json
import os
from datetime import datetime
from html import escape

def load_portfolio_data():
    """加载持仓数据"""
    data_path = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'portfolio.json')
    with open(data_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def format_percent(value):
    """格式化百分比"""
    if value >= 0:
        return f"+{value*100:.2f}%"
    else:
        return f"{value*100:.2f}%"

def format_price(value):
    """格式化价格"""
    return f"{value:.2f}"

def get_color_class(value, positive_is_good=True):
    """根据正负返回颜色类"""
    if positive_is_good:
        return 'text-green-600' if value >= 0 else 'text-red-600'
    else:
        return 'text-red-600' if value >= 0 else 'text-green-600'

def get_diagnosis_bg_class(status):
    """根据诊断状态返回背景色"""
    if status == 'good':
        return 'bg-green-50 border-green-100'
    elif status == 'bad':
        return 'bg-red-50 border-red-100'
    else:
        return 'bg-gray-50 border-gray-100'

def get_diagnosis_text_class(status):
    """根据诊断状态返回文字颜色"""
    if status == 'good':
        return 'text-green-600'
    elif status == 'bad':
        return 'text-red-600'
    else:
        return 'text-gray-600'

def generate_stock_card(stock):
    """生成单个持仓卡片HTML"""
    # 判断是用"距止损"还是"安全边际"
    has_stop_loss_distance = 'distance_to_stop_loss' in stock
    has_safety_margin = 'safety_margin' in stock
    
    if has_stop_loss_distance:
        margin_label = '距止损'
        margin_value = format_percent(stock['distance_to_stop_loss'])
        margin_color = get_color_class(stock['distance_to_stop_loss'], positive_is_good=False)
    else:
        margin_label = '安全边际'
        margin_value = format_percent(stock['safety_margin'])
        margin_color = get_color_class(stock['safety_margin'], positive_is_good=True)
    
    # 今日涨跌颜色
    today_change_color = get_color_class(stock['today_change'])
    
    # 最新价颜色（相对于成本价）
    profit = stock['current_price'] - stock['cost_price']
    price_color = get_color_class(profit)
    
    diagnosis = stock['diagnosis']
    
    card_html = f'''
            <!-- {stock['name']} -->
            <div class="stock-card card-glass p-6">
                <div class="flex items-start justify-between mb-6">
                    <div class="flex items-center gap-4">
                        <div class="w-16 h-16 rounded-2xl bg-gradient-to-br {stock['gradient']} flex items-center justify-center">
                            <span class="text-white text-3xl font-black">{stock['icon']}</span>
                        </div>
                        <div>
                            <div class="flex items-center gap-3">
                                <h2 class="text-2xl font-black text-gray-800">{stock['name']}</h2>
                                <span class="text-gray-400">{stock['id']}</span>
                                <span class="{stock['tag_color']} text-white text-xs px-3 py-1 rounded-full font-bold">{stock['tag']}</span>
                            </div>
                        </div>
                    </div>
                </div>
                
                <div class="grid grid-cols-6 gap-4 mb-6">
                    <div class="p-4 bg-gray-50 rounded-xl text-center">
                        <div class="text-xs text-gray-500 mb-1">成本价</div>
                        <div class="text-xl font-bold text-gray-700">{format_price(stock['cost_price'])}</div>
                    </div>
                    <div class="p-4 bg-gray-50 rounded-xl text-center">
                        <div class="text-xs text-gray-500 mb-1">最新价</div>
                        <div class="text-xl font-bold {price_color}">{format_price(stock['current_price'])}</div>
                    </div>
                    <div class="p-4 bg-gray-50 rounded-xl text-center">
                        <div class="text-xs text-gray-500 mb-1">止损价</div>
                        <div class="text-xl font-bold text-gray-700">{format_price(stock['stop_loss_price'])}</div>
                    </div>
                    <div class="p-4 bg-gray-50 rounded-xl text-center">
                        <div class="text-xs text-gray-500 mb-1">{margin_label}</div>
                        <div class="text-xl font-bold {margin_color}">{margin_value}</div>
                    </div>
                    <div class="p-4 bg-gray-50 rounded-xl text-center">
                        <div class="text-xs text-gray-500 mb-1">今日涨跌</div>
                        <div class="text-xl font-bold {today_change_color}">{format_percent(stock['today_change'])}</div>
                    </div>
                    <div class="p-4 bg-gray-50 rounded-xl text-center">
                        <div class="text-xs text-gray-500 mb-1">主力资金</div>
                        <div class="text-xl font-bold text-red-600">{stock['main_fund']}</div>
                    </div>
                </div>
                
                <!-- 风险进度条 -->
                <div class="mb-6">
                    <div class="flex justify-between text-sm mb-2">
                        <span class="text-gray-500">风险程度</span>
                        <span class="{stock['risk_color']} font-bold">{stock['risk_level']}</span>
                    </div>
                    <div class="h-4 bg-gray-200 rounded-full overflow-hidden relative">
                        <div class="h-full progress-bar rounded-full"></div>
                        <div class="absolute top-0 h-full w-0.5 bg-white" style="left: 50%;"></div>
                        <div class="absolute -top-1" style="left: {stock['risk_progress']}%;">
                            <div class="w-4 h-4 bg-red-600 rounded-full border-2 border-white shadow-lg"></div>
                        </div>
                    </div>
                    <div class="flex justify-between text-xs text-gray-400 mt-1">
                        <span>安全区</span><span>警戒区</span><span>止损区</span>
                    </div>
                </div>
                
                <!-- 四维诊断 -->
                <div class="grid grid-cols-4 gap-4">
                    <div class="p-4 {get_diagnosis_bg_class(diagnosis['technical']['status'])} border rounded-xl">
                        <div class="flex items-center gap-2 mb-2">
                            <span class="text-lg">📈</span>
                            <span class="text-sm font-semibold text-gray-700">{diagnosis['technical']['title']}</span>
                        </div>
                        <div class="text-lg font-bold {get_diagnosis_text_class(diagnosis['technical']['status'])}">{diagnosis['technical']['value']}</div>
                        <div class="text-xs text-gray-500 mt-1">{diagnosis['technical']['desc']}</div>
                    </div>
                    <div class="p-4 {get_diagnosis_bg_class(diagnosis['fund']['status'])} border rounded-xl">
                        <div class="flex items-center gap-2 mb-2">
                            <span class="text-lg">💰</span>
                            <span class="text-sm font-semibold text-gray-700">{diagnosis['fund']['title']}</span>
                        </div>
                        <div class="text-lg font-bold {get_diagnosis_text_class(diagnosis['fund']['status'])}">{diagnosis['fund']['value']}</div>
                        <div class="text-xs text-gray-500 mt-1">{diagnosis['fund']['desc']}</div>
                    </div>
                    <div class="p-4 {get_diagnosis_bg_class(diagnosis['news']['status'])} border rounded-xl">
                        <div class="flex items-center gap-2 mb-2">
                            <span class="text-lg">📰</span>
                            <span class="text-sm font-semibold text-gray-700">{diagnosis['news']['title']}</span>
                        </div>
                        <div class="text-lg font-bold {get_diagnosis_text_class(diagnosis['news']['status'])}">{diagnosis['news']['value']}</div>
                        <div class="text-xs text-gray-500 mt-1">{diagnosis['news']['desc']}</div>
                    </div>
                    <div class="p-4 {get_diagnosis_bg_class(diagnosis['industry']['status'])} border rounded-xl">
                        <div class="flex items-center gap-2 mb-2">
                            <span class="text-lg">🏭</span>
                            <span class="text-sm font-semibold text-gray-700">{diagnosis['industry']['title']}</span>
                        </div>
                        <div class="text-lg font-bold {get_diagnosis_text_class(diagnosis['industry']['status'])}">{diagnosis['industry']['value']}</div>
                        <div class="text-xs text-gray-500 mt-1">{diagnosis['industry']['desc']}</div>
                    </div>
                </div>
            </div>
'''
    return card_html

def generate_stress_test(stocks, portfolio):
    """生成压力测试表格"""
    rows_extreme = []
    rows_neutral = []
    
    for stock in stocks:
        rows_extreme.append(f'''
                        <div class="p-3 bg-gray-50 rounded-lg text-center">
                            <div class="text-gray-500 text-xs">{stock['name']}</div>
                            <div class="text-lg font-bold text-red-600">{stock['stress_test']['extreme']}</div>
                        </div>
        ''')
        rows_neutral.append(f'''
                        <div class="p-3 bg-gray-50 rounded-lg text-center">
                            <div class="text-gray-500 text-xs">{stock['name']}</div>
                            <div class="text-lg font-bold text-yellow-600">{stock['stress_test']['neutral']}</div>
                        </div>
        ''')
    
    html = f'''
        <!-- 【第三区：压力测试与调仓建议】 -->
        <div class="card-glass p-6 mb-6">
            <div class="flex items-center gap-3 mb-6">
                <span class="text-2xl">🚨</span>
                <h2 class="text-xl font-bold text-gray-800">压力测试情景</h2>
            </div>
            
            <div class="space-y-4 mb-6">
                <div>
                    <div class="text-sm font-semibold text-gray-700 mb-2">极端情景（大盘跌10%）</div>
                    <div class="grid grid-cols-4 gap-3">
                        {''.join(rows_extreme)}
                    </div>
                </div>
                <div>
                    <div class="text-sm font-semibold text-gray-700 mb-2">中性情景（大盘震荡）</div>
                    <div class="grid grid-cols-4 gap-3">
                        {''.join(rows_neutral)}
                    </div>
                </div>
            </div>
            
            <!-- 调仓建议 -->
            <div class="border-t border-gray-200 pt-6">
                <div class="flex items-center gap-3 mb-4">
                    <span class="text-2xl">💡</span>
                    <h2 class="text-xl font-bold text-gray-800">智能调仓建议</h2>
                </div>
                <div class="space-y-3">
'''
    
    # 每个股票的建议
    for stock in stocks:
        html += f'''
                    <p class="text-sm text-gray-700">{stock['advice']}</p>
        '''
    
    # 总建议
    html += f'''
                    <p class="text-sm text-gray-700 font-medium pt-2 border-t border-gray-100">{portfolio['overall_advice']}</p>
                </div>
            </div>
        </div>
'''
    return html

def generate_full_page(data):
    """生成完整页面"""
    portfolio = data['portfolio']
    stocks = data['stocks']
    
    # 生成所有持仓卡片
    stock_cards = ''.join([generate_stock_card(s) for s in stocks])
    
    # 生成压力测试区
    stress_test_html = generate_stress_test(stocks, portfolio)
    
    # 计算组合数据
    total_return_color = get_color_class(portfolio['total_return'])
    health_color = 'text-green-600' if portfolio['health_score'] >= 60 else 'text-yellow-600'
    
    # 读取原页面的head和导航部分（保证UI一致）
    # 这里直接内嵌完整的CSS和导航，确保与原版一致
    html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>持仓智能预警仪表盘</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://cdn.jsdelivr.net/npm/font-awesome@4.7.0/css/font-awesome.min.css" rel="stylesheet">
    <style>
        /* ===== 标准导航栏样式 ===== */
        .glass-nav {{
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            border-bottom: 1px solid rgba(255, 255, 255, 0.2);
            z-index: 2147483647 !important;
            isolation: isolate !important;
            pointer-events: auto !important;
        }}
.glass-nav * {{
            position: relative;
            z-index: 2147483647 !important;
            pointer-events: auto !important;
        }}
.hamburger-btn {{
            display: none;
            background: rgba(255,255,255,0.2);
            border: none;
            color: white;
            width: 44px;
            height: 44px;
            border-radius: 8px;
            cursor: pointer;
            font-size: 20px;
            z-index: 99999;
        }}
.mobile-menu {{
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: linear-gradient(135deg, rgba(102,126,234,0.98) 0%, rgba(118,75,162,0.98) 100%);
            z-index: 99998;
            display: none;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }}
.mobile-menu.show {{
            display: flex;
        }}
.mobile-menu-item {{
            color: white;
            font-size: 18px;
            font-weight: 600;
            padding: 15px 30px;
            text-decoration: none;
            text-align: center;
            width: 100%;
            max-width: 300px;
            border-bottom: 1px solid rgba(255,255,255,0.2);
            transition: all 0.3s;
        }}
.close-menu-btn {{
            position: absolute;
            top: 20px;
            right: 20px;
            background: rgba(255,255,255,0.2);
            border: none;
            color: white;
            width: 44px;
            height: 44px;
            border-radius: 8px;
            cursor: pointer;
            font-size: 20px;
        }}
@media (max-width: 768px) {{
            .nav-links {{
                display: none !important;
            }}
            
            .hamburger-btn {{
                display: block !important;
        }}
            }}

        @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@300;400;500;700;900&display=swap');
        
        * {{ font-family: 'Noto Sans SC', sans-serif; }}
        
        body {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
        }}
        
        .card-glass {{
            background: rgba(255, 255, 255, 0.9);
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            border: 1px solid rgba(255, 255, 255, 0.3);
            border-radius: 20px;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
        }}
        
        .stock-card {{ transition: transform 0.2s ease; }}
        .stock-card:hover {{ transform: translateY(-2px); }}
        
        .progress-bar {{
            background: linear-gradient(90deg, #10b981 0%, #f59e0b 50%, #ef4444 100%);
            width: 100%;
        }}
        
        .health-ring-green {{
            --p: {portfolio['health_score']}%;
            background: conic-gradient(#10b981 var(--p), #e5e7eb var(--p));
        }}
        
        /* ===== V3.0 精致增强版样式 ===== */
        .stat-card-hover {{
            transition: all 0.3s ease;
        }}
        .stat-card-hover:hover {{
            transform: translateY(-3px);
            box-shadow: 0 10px 25px rgba(0,0,0,0.1);
        }}
    </style>
</head>
<body class="pb-20">
    <!-- 导航栏 -->
    <nav class="glass-nav fixed top-0 left-0 right-0 z-50">
        <div class="max-w-6xl mx-auto px-4 py-3 flex items-center justify-between">
            <div class="flex items-center gap-2">
                <span class="text-2xl">📊</span>
                <span class="text-white font-bold text-lg">持仓智能预警</span>
            </div>
            <button class="hamburger-btn" onclick="toggleMenu()">
                <i class="fa fa-bars"></i>
            </button>
            <div class="nav-links flex items-center gap-6">
                <a href="../index.html" class="text-white/80 hover:text-white text-sm font-medium transition">首页</a>
                <a href="../news/latest.html" class="text-white/80 hover:text-white text-sm font-medium transition">每日新闻</a>
                <a href="index.html" class="text-white font-bold text-sm">持仓预警</a>
                <a href="../industry_chain/latest.html" class="text-white/80 hover:text-white text-sm font-medium transition">产业链</a>
                <a href="../weekly_outlook/latest.html" class="text-white/80 hover:text-white text-sm font-medium transition">周前瞻</a>
            </div>
        </div>
    </nav>
    
    <!-- 移动端菜单 -->
    <div class="mobile-menu" id="mobileMenu">
        <button class="close-menu-btn" onclick="toggleMenu()">
            <i class="fa fa-times"></i>
        </button>
        <a href="../index.html" class="mobile-menu-item" onclick="toggleMenu()">首页</a>
        <a href="../news/latest.html" class="mobile-menu-item" onclick="toggleMenu()">每日新闻</a>
        <a href="index.html" class="mobile-menu-item" onclick="toggleMenu()">持仓预警</a>
        <a href="../industry_chain/latest.html" class="mobile-menu-item" onclick="toggleMenu()">产业链</a>
        <a href="../weekly_outlook/latest.html" class="mobile-menu-item" onclick="toggleMenu()">周前瞻</a>
    </div>
    
    <!-- 主内容区 -->
    <div class="max-w-6xl mx-auto px-4 pt-24">
        <!-- 标题区 -->
        <div class="card-glass p-6 mb-6">
            <div class="flex items-center gap-3">
                <div class="w-12 h-12 rounded-xl bg-gradient-to-br from-indigo-500 to-purple-600 flex items-center justify-center">
                    <span class="text-2xl">📊</span>
                </div>
                <div>
                    <div class="flex items-center gap-2">
                        <h1 class="text-xl font-bold text-gray-800">持仓智能预警仪表盘</h1>
                        <span class="bg-purple-500 text-white text-xs px-2 py-0.5 rounded-full font-semibold">Pro</span>
                    </div>
                    <p class="text-gray-500 text-sm mt-1">数据更新时间：{portfolio['update_time']}</p>
                </div>
            </div>
        </div>
        
        <!-- 组合总览 -->
        <div class="card-glass p-6 mb-6">
            <div class="flex items-center justify-between mb-6">
                <div>
                    <h1 class="text-2xl font-black text-gray-800 mb-1">投资组合健康度分析</h1>
                    <p class="text-gray-500 text-sm">多维度持仓诊断 · 风险实时预警 · 智能调仓建议</p>
                </div>
                <div class="flex items-center gap-6">
                    <div class="text-center">
                        <div class="text-4xl font-black {total_return_color}">{format_percent(portfolio['total_return'])}</div>
                        <div class="text-sm text-gray-500">组合总盈亏</div>
                    </div>
                    <div class="relative">
                        <div class="health-ring-green w-24 h-24 rounded-full flex items-center justify-center">
                            <div class="w-20 h-20 bg-white rounded-full flex items-center justify-center">
                                <div class="text-center">
                                    <div class="text-2xl font-black {health_color}">{portfolio['health_score']}</div>
                                    <div class="text-xs text-gray-500">健康分</div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            
            <div class="grid grid-cols-5 gap-4">
                <div class="p-4 bg-gradient-to-br from-blue-50 to-indigo-50 border border-blue-100 rounded-2xl text-center stat-card-hover">
                    <div class="text-2xl mb-1">📦</div>
                    <div class="text-sm text-gray-600 mb-1">持仓标的</div>
                    <div class="text-2xl font-black text-gray-800">{portfolio['stock_count']}只</div>
                </div>
                <div class="p-4 bg-gradient-to-br from-green-50 to-emerald-50 border border-green-100 rounded-2xl text-center stat-card-hover">
                    <div class="text-2xl mb-1">💰</div>
                    <div class="text-sm text-gray-600 mb-1">盈利标的</div>
                    <div class="text-2xl font-black text-green-600">{portfolio['profit_count']}只</div>
                </div>
                <div class="p-4 bg-gradient-to-br from-red-50 to-orange-50 border border-red-100 rounded-2xl text-center stat-card-hover">
                    <div class="text-2xl mb-1">📉</div>
                    <div class="text-sm text-gray-600 mb-1">亏损标的</div>
                    <div class="text-2xl font-black text-red-600">{portfolio['loss_count']}只</div>
                </div>
                <div class="p-4 bg-gradient-to-br from-yellow-50 to-amber-50 border border-yellow-100 rounded-2xl text-center stat-card-hover">
                    <div class="text-2xl mb-1">⚠️</div>
                    <div class="text-sm text-gray-600 mb-1">跌破止损</div>
                    <div class="text-2xl font-black text-yellow-600">{portfolio['stop_loss_break_count']}只</div>
                </div>
                <div class="p-4 bg-gradient-to-br from-purple-50 to-violet-50 border border-purple-100 rounded-2xl text-center stat-card-hover">
                    <div class="text-2xl mb-1">🏭</div>
                    <div class="text-sm text-gray-600 mb-1">行业分布</div>
                    <div class="text-2xl font-black text-purple-600">{portfolio['industry_count']}个</div>
                </div>
            </div>
        </div>
        
        <!-- 【第二区：持仓深度卡片】 -->
        <div class="space-y-6 mb-6">
            {stock_cards}
        </div>
        
        {stress_test_html}
        
        <!-- 页脚 -->
        <div class="text-center text-white/60 text-xs mt-8">
            <p>数据仅供参考，不构成投资建议 · 投资有风险，入市需谨慎</p>
            <p class="mt-2">持仓智能预警仪表盘 · {portfolio['update_time']}</p>
        </div>
    </div>
    
    <script>
        function toggleMenu() {{
            document.getElementById('mobileMenu').classList.toggle('show');
        }}
    </script>
</body>
</html>'''
    
    return html

def generate():
    """主生成函数"""
    data = load_portfolio_data()
    html = generate_full_page(data)
    
    # 输出路径
    output_path = os.path.join(os.path.dirname(__file__), '..', '..', 'docs', '持仓智能预警仪表盘', 'index.html')
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"✅ 持仓智能预警仪表盘已生成：{output_path}")
    print(f"   持仓标的：{data['portfolio']['stock_count']}只")
    print(f"   组合盈亏：{format_percent(data['portfolio']['total_return'])}")
    print(f"   健康评分：{data['portfolio']['health_score']}分")
    
    return output_path

if __name__ == '__main__':
    generate()
