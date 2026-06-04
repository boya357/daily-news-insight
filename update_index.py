#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
首页自动更新脚本
布局完全固定，只自动扫描并更新最新发布模块
用法: python3 update_index.py
"""

import os
import glob

# 固定页面模板（布局永远不变）
PAGE_TEMPLATE = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>投资研究中心</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.5.1/css/all.min.css">
    <style>
        body::before {{
            content: '';
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            z-index: 0;
            pointer-events: none;
        }}
        
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
        
        body {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            font-family: -apple-system, BlinkMacSystemFont, 'PingFang SC', 'Helvetica Neue', sans-serif;
        }}
        
        .line-clamp-2 {{
            display: -webkit-box;
            -webkit-line-clamp: 2;
            -webkit-box-orient: vertical;
            overflow: hidden;
        }}
    </style>
</head>
<body>
    <nav class="fixed top-0 left-0 right-0 z-50 glass-nav">
        <div class="max-w-5xl mx-auto px-4 py-3 flex items-center justify-between">
            <div class="flex items-center space-x-3">
                <div class="w-8 h-8 rounded-lg bg-gradient-to-br from-indigo-500 to-purple-600 flex items-center justify-center">
                    <span class="text-white text-sm font-bold">📊</span>
                </div>
                <span class="text-white font-bold text-lg">投资研究中心</span>
            </div>
            <div class="flex items-center space-x-1 flex-wrap gap-1">
                <a href="/daily-news-insight/index.html" class="text-white/80 hover:text-white hover:bg-white/10 text-sm transition-colors px-3 py-1.5 rounded-lg">首页</a>
                <a href="/daily-news-insight/daily/latest.html" class="text-white/80 hover:text-white hover:bg-white/10 text-sm transition-colors px-3 py-1.5 rounded-lg">日报</a>
                <a href="/daily-news-insight/intraday/latest.html" class="text-white/80 hover:text-white hover:bg-white/10 text-sm transition-colors px-3 py-1.5 rounded-lg">盘中</a>
                <a href="/daily-news-insight/aftermarket/latest.html" class="text-white/80 hover:text-white hover:bg-white/10 text-sm transition-colors px-3 py-1.5 rounded-lg">盘后</a>
                <a href="/daily-news-insight/industry_chain/latest.html" class="text-white/80 hover:text-white hover:bg-white/10 text-sm transition-colors px-3 py-1.5 rounded-lg">产业链</a>
                <a href="/daily-news-insight/weekly_review/latest.html" class="text-white/80 hover:text-white hover:bg-white/10 text-sm transition-colors px-3 py-1.5 rounded-lg">周复盘</a>
                <a href="/daily-news-insight/weekly_outlook/latest.html" class="text-white/80 hover:text-white hover:bg-white/10 text-sm transition-colors px-3 py-1.5 rounded-lg">周三前瞻</a>
                <a href="/daily-news-insight/周末速递/latest.html" class="text-white/80 hover:text-white hover:bg-white/10 text-sm transition-colors px-3 py-1.5 rounded-lg">周末速递</a>
                <a href="/daily-news-insight/明日催化剂/latest.html" class="text-white/80 hover:text-white hover:bg-white/10 text-sm transition-colors px-3 py-1.5 rounded-lg">明日催化</a>
                <a href="/daily-news-insight/s级催化扫描/latest.html" class="text-white/80 hover:text-white hover:bg-white/10 text-sm transition-colors px-3 py-1.5 rounded-lg">S级催化</a>
                <a href="/daily-news-insight/monthly/latest.html" class="text-white/80 hover:text-white hover:bg-white/10 text-sm transition-colors px-3 py-1.5 rounded-lg">月报</a>
            </div>
        </div>
    </nav>

    <div class="pt-24 pb-8 px-4">
        <div class="max-w-6xl mx-auto text-center">
            <h1 class="text-4xl md:text-5xl font-black text-white mb-4 leading-tight">
                <i class="fa fa-line-chart mr-3"></i>投资研究中心
            </h1>
            <p class="text-white/80 text-lg">专业、深度、及时的市场研究与机会挖掘</p>
        </div>
    </div>

    <div class="max-w-6xl mx-auto px-4 pb-20">
        <!-- 最新发布模块 -->
        <div class="bg-white/95 backdrop-blur-sm rounded-3xl shadow-2xl p-8 mb-8">
            <h2 class="text-lg font-bold text-indigo-800 uppercase tracking-wider mb-6">
                <i class="fa fa-fire mr-2"></i>最新发布
            </h2>
            
            <div class="grid grid-cols-2 md:grid-cols-4 gap-4">
                {latest_reports}
            </div>
        </div>

        <!-- 快速入口 -->
        <div class="bg-white/95 backdrop-blur-sm rounded-3xl shadow-2xl p-8">
            <h2 class="text-lg font-bold text-indigo-800 uppercase tracking-wider mb-6">
                <i class="fa fa-th-large mr-2"></i>研究分类
            </h2>
            
            <div class="grid grid-cols-2 md:grid-cols-5 gap-4">
                <a href="daily/latest.html" class="block p-6 bg-gradient-to-br from-blue-50 to-indigo-50 rounded-2xl text-center hover:shadow-lg transition-all group">
                    <div class="text-4xl mb-3">📰</div>
                    <div class="font-bold text-gray-800 group-hover:text-blue-600 transition-colors">每日新闻洞察</div>
                </a>
                <a href="intraday/latest.html" class="block p-6 bg-gradient-to-br from-orange-50 to-red-50 rounded-2xl text-center hover:shadow-lg transition-all group">
                    <div class="text-4xl mb-3">⚡</div>
                    <div class="font-bold text-gray-800 group-hover:text-orange-600 transition-colors">盘中快报</div>
                </a>
                <a href="aftermarket/latest.html" class="block p-6 bg-gradient-to-br from-yellow-50 to-orange-50 rounded-2xl text-center hover:shadow-lg transition-all group">
                    <div class="text-4xl mb-3">☀️</div>
                    <div class="font-bold text-gray-800 group-hover:text-yellow-600 transition-colors">盘后速递</div>
                </a>
                <a href="industry_chain/latest.html" class="block p-6 bg-gradient-to-br from-green-50 to-emerald-50 rounded-2xl text-center hover:shadow-lg transition-all group">
                    <div class="text-4xl mb-3">🔗</div>
                    <div class="font-bold text-gray-800 group-hover:text-green-600 transition-colors">产业链</div>
                </a>
                <a href="s级催化扫描/latest.html" class="block p-6 bg-gradient-to-br from-rose-50 to-red-50 rounded-2xl text-center hover:shadow-lg transition-all group">
                    <div class="text-4xl mb-3">⭐</div>
                    <div class="font-bold text-gray-800 group-hover:text-rose-600 transition-colors">S级催化</div>
                </a>
            </div>
        </div>
    </div>

    <div class="text-center py-10 px-4">
        <div class="text-white/60 text-sm">
            <p class="mb-2">💡 投资研究中心 · 专业深度研究</p>
            <p class="text-xs text-white/40">数据仅供参考，不构成投资建议</p>
        </div>
    </div>
</body>
</html>
'''

# 最新报告卡片模板
LATEST_CARD_TEMPLATE = '''<a href="{filepath}" class="block p-5 bg-gradient-to-br {gradient} border-2 {border_color} rounded-xl text-center group hover:shadow-lg transition-all">
    <div class="text-3xl mb-2">{icon}</div>
    <div class="font-semibold text-gray-800 text-sm mb-1 group-hover:text-indigo-600 transition-colors line-clamp-2">{title}</div>
    <span class="inline-block px-2 py-1 text-xs font-bold bg-indigo-100 text-indigo-700 rounded">{label}</span>
</a>
'''

def get_latest_report(directory, icon, title_prefix, label, gradient, border_color):
    """获取指定目录下最新的报告文件"""
    all_files = glob.glob(f'{directory}/20*.html')
    if not all_files:
        return None
    
    # 按时间倒序排序，取最新
    all_files.sort(reverse=True)
    latest_file = all_files[0]
    filename = os.path.basename(latest_file)
    date_str = filename[:8]
    
    # 转换为相对路径（相对于docs目录）
    rel_path = os.path.relpath(latest_file, 'docs')
    
    return LATEST_CARD_TEMPLATE.format(
        filepath=rel_path,
        icon=icon,
        title=f'{date_str} {title_prefix}',
        label=label,
        gradient=gradient,
        border_color=border_color
    )

def main():
    # 切换到脚本所在目录
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    # 获取各个模块的最新报告
    modules = [
        ('docs/s级催化扫描', '⭐', 'S级催化扫描', '🔥 超级催化', 'from-rose-50 to-red-50', 'border-rose-200'),
        ('docs/daily', '📰', '每日新闻洞察', '📅 每日', 'from-blue-50 to-indigo-50', 'border-blue-200'),
        ('docs/intraday', '⚡', '盘中快报', '⚡ 盘中', 'from-orange-50 to-red-50', 'border-orange-200'),
        ('docs/aftermarket', '☀️', '盘后速递', '☀️ 盘后', 'from-yellow-50 to-orange-50', 'border-yellow-200'),
        ('docs/industry_chain', '🔗', '产业链', '🔗 深度', 'from-green-50 to-emerald-50', 'border-green-200'),
        ('docs/weekly_review', '🔄', '周复盘', '📊 周度', 'from-purple-50 to-pink-50', 'border-purple-200'),
        ('docs/weekly_outlook', '🔭', '周三前瞻', '🔭 前瞻', 'from-cyan-50 to-blue-50', 'border-cyan-200'),
        ('docs/周末速递', '🚀', '周末速递', '🚀 周末', 'from-amber-50 to-orange-50', 'border-amber-200'),
    ]
    
    # 生成卡片
    report_cards = []
    for module in modules:
        card = get_latest_report(*module)
        if card:
            report_cards.append(card)
    
    print(f'✅ 扫描到 {len(report_cards)} 个最新报告')
    
    # 插入到模板中
    final_html = PAGE_TEMPLATE.format(
        latest_reports='\n'.join(report_cards)
    )
    
    # 5. 写入文件
    output_path = 'docs/index.html'
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(final_html)
    
    print(f'✅ 已写入 {output_path}')
    print(f'✅ 首页布局完全固定，只自动更新了最新报告模块')

if __name__ == '__main__':
    main()
