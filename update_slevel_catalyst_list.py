#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S级催化扫描列表页自动更新脚本
布局完全固定，只自动扫描并更新报告卡片
用法: python3 update_slevel_catalyst_list.py
"""

import os
import glob

# 固定页面模板（布局永远不变）
PAGE_TEMPLATE = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>S级催化扫描</title>
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
    
        /* ========== 汉堡菜单样式 ========== */
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
        
        .mobile-menu-item:hover {{
            background: rgba(255,255,255,0.1);
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
        
        /* ========== 响应式媒体查询 ========== */
        @media (max-width: 768px) {{
            .nav-links {{
                display: none !important;
            }}
            
            .hamburger-btn {{
                display: block !important;
            }}
            
            .grid-cols-4 {{
                grid-template-columns: repeat(2, 1fr) !important;
            }}
            
            .text-4xl {{
                font-size: 1.875rem !important;
            }}
            
            .text-3xl {{
                font-size: 1.5rem !important;
            }}
            
            .text-2xl {{
                font-size: 1.25rem !important;
            }}
            
            .p-8 {{
                padding: 1.5rem !important;
            }}
            
            .p-6 {{
                padding: 1.25rem !important;
            }}
            
            table {{
                display: block;
                overflow-x: auto;
            }}
            
            a, button {{
                min-height: 44px;
                min-width: 44px;
            }}
        }}
        
        @media (min-width: 769px) and (max-width: 1024px) {{
            .grid-cols-4 {{
                grid-template-columns: repeat(3, 1fr) !important;
            }}
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
            <div class="nav-links flex items-center space-x-1 flex-wrap gap-1">
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
            <button class="hamburger-btn" onclick="toggleMobileMenu()">☰</button>
        </div>
    </nav>
    
    <!-- 移动端全屏菜单 -->
    <div id="mobileMenu" class="mobile-menu">
        <button class="close-menu-btn" onclick="toggleMobileMenu()">✕</button>
        <a href="/daily-news-insight/index.html" class="mobile-menu-item" onclick="toggleMobileMenu()">🏠 首页</a>
        <a href="/daily-news-insight/daily/latest.html" class="mobile-menu-item" onclick="toggleMobileMenu()">📰 日报</a>
        <a href="/daily-news-insight/intraday/latest.html" class="mobile-menu-item" onclick="toggleMobileMenu()">📈 盘中快报</a>
        <a href="/daily-news-insight/aftermarket/latest.html" class="mobile-menu-item" onclick="toggleMobileMenu()">📉 盘后速递</a>
        <a href="/daily-news-insight/industry_chain/latest.html" class="mobile-menu-item" onclick="toggleMobileMenu()">🔗 产业链总览</a>
        <a href="/daily-news-insight/weekly_review/latest.html" class="mobile-menu-item" onclick="toggleMobileMenu()">📋 周复盘</a>
        <a href="/daily-news-insight/weekly_outlook/latest.html" class="mobile-menu-item" onclick="toggleMobileMenu()">🔮 周三前瞻</a>
        <a href="/daily-news-insight/周末速递/latest.html" class="mobile-menu-item" onclick="toggleMobileMenu()">📦 周末速递</a>
        <a href="/daily-news-insight/明日催化剂/latest.html" class="mobile-menu-item" onclick="toggleMobileMenu()">⏰ 明日催化剂</a>
        <a href="/daily-news-insight/s级催化扫描/latest.html" class="mobile-menu-item" onclick="toggleMobileMenu()">⭐ S级催化扫描</a>
        <a href="/daily-news-insight/monthly/latest.html" class="mobile-menu-item" onclick="toggleMobileMenu()">🗓️ 月度总结</a>
    </div>
    
    <script>
        function toggleMobileMenu() {{
            document.getElementById('mobileMenu').classList.toggle('show');
            document.body.style.overflow = document.getElementById('mobileMenu').classList.contains('show') ? 'hidden' : '';
        }}
    </script>

    <div class="pt-24 pb-8 px-4">
        <div class="max-w-6xl mx-auto text-center">
            <h1 class="text-3xl md:text-4xl font-black text-white mb-3 leading-tight">
                <i class="fa fa-star mr-2"></i>S级催化扫描
            </h1>
            <p class="text-white/80">超级催化事件深度追踪与预警</p>
        </div>
    </div>

    <div class="max-w-6xl mx-auto px-4 pb-20">
        <div class="bg-white/95 backdrop-blur-sm rounded-3xl shadow-2xl p-8">
            <h2 class="text-sm font-bold text-indigo-800 uppercase tracking-wider mb-6">
                <i class="fa fa-file-text-o mr-2"></i>报告列表 · 按时间倒序
            </h2>
            
            <div class="grid grid-cols-2 md:grid-cols-4 gap-4">
                __REPORT_CARDS__
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

# 卡片模板（最新报告）
NEWEST_CARD_TEMPLATE = '''<a href="{filename}" class="report-card block p-5 bg-gradient-to-br from-rose-50 to-red-50 border-2 border-rose-200 rounded-xl text-center group hover:shadow-lg transition-all">
    <div class="text-3xl mb-2">⭐</div>
    <div class="font-semibold text-gray-800 text-sm mb-1 group-hover:text-rose-600 transition-colors line-clamp-2">{title}</div>
    <span class="inline-block px-2 py-1 text-xs font-bold bg-red-100 text-red-700 rounded">🆕 最新</span>
</a>
'''

# 卡片模板（普通报告）
NORMAL_CARD_TEMPLATE = '''<a href="{filename}" class="report-card block p-5 bg-white border border-gray-100 rounded-xl text-center group hover:shadow-lg transition-all">
    <div class="text-3xl mb-2">⭐</div>
    <div class="font-semibold text-gray-800 text-sm mb-1 group-hover:text-indigo-600 transition-colors line-clamp-2">{title}</div>
    <span class="inline-block px-2 py-1 text-xs font-bold bg-rose-100 text-rose-700 rounded">S级催化</span>
</a>
'''

def main():
    # 切换到脚本所在目录
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    slevel_dir = 'docs/s级催化扫描'
    
    # 1. 扫描目录下所有报告文件（排除latest.html）
    all_files = glob.glob(f'{slevel_dir}/20*.html')
    all_files = [f for f in all_files if 'latest.html' not in f]
    
    # 2. 按时间倒序排序
    all_files.sort(reverse=True)
    
    print(f'✅ 扫描到 {len(all_files)} 份报告')
    
    # 3. 生成卡片HTML
    report_cards = []
    for i, filepath in enumerate(all_files):
        filename = os.path.basename(filepath)
        date_str = filename[:8]
        # 从文件名中提取真正的标题，保留"盘前"和"盘后"标识
        # 格式：YYYYMMDD_盘前_S级催化扫描.html -> 提取"盘前 S级催化扫描"
        name_without_date = filename[9:].replace('.html', '')
        # 把下划线换成空格
        name_without_date = name_without_date.replace('_', ' ')
        title = f'{date_str} {name_without_date}'
        
        if i == 0:
            # 最新报告
            card = NEWEST_CARD_TEMPLATE.format(
                filename=filename,
                title=title
            )
        else:
            # 普通报告
            card = NORMAL_CARD_TEMPLATE.format(
                filename=filename,
                title=title
            )
        report_cards.append(card)
    
    # 4. 插入到模板中
    final_html = PAGE_TEMPLATE.replace('__REPORT_CARDS__', '\n'.join(report_cards))
    
    # 5. 写入文件
    output_path = f'{slevel_dir}/latest.html'
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(final_html)
    
    print(f'✅ 已写入 {output_path}')
    print(f'✅ 布局完全固定，只自动更新了报告卡片')

if __name__ == '__main__':
    main()
