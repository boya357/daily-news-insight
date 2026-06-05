#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S级催化扫描报告转换脚本
将Markdown内容转换为标准HTML模板
"""

import re

# 读取Markdown内容
with open("S级催化扫描/20260605_盘前_S级催化扫描.md", "r", encoding="utf-8") as f:
    md_content = f.read()

# Markdown转HTML函数
def md_to_html(md_text):
    html = md_text
    
    # 标题处理
    html = re.sub(r'^# (.*?)$', r'<h1 class="text-3xl font-bold text-gray-800 mb-6">\1</h1>', html, flags=re.MULTILINE)
    html = re.sub(r'^## (.*?)$', r'<h2 class="text-2xl font-bold gradient-text mt-8 mb-4 pb-2 border-b-2 border-indigo-200">\1</h2>', html, flags=re.MULTILINE)
    html = re.sub(r'^### (.*?)$', r'<h3 class="text-xl font-semibold text-gray-700 mt-6 mb-3">\1</h3>', html, flags=re.MULTILINE)
    html = re.sub(r'^#### (.*?)$', r'<h4 class="text-lg font-medium text-gray-600 mt-4 mb-2">\1</h4>', html, flags=re.MULTILINE)
    
    # 粗体
    html = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', html)
    
    # 列表处理
    html = re.sub(r'^- (.*?)$', r'<li class="text-gray-700 mb-2 ml-4">\1</li>', html, flags=re.MULTILINE)
    
    # 分隔线
    html = re.sub(r'^---$', r'<hr class="my-6 border-gray-200">', html, flags=re.MULTILINE)
    
    # 段落处理（简单处理，保留换行）
    lines = html.split('\n')
    result = []
    in_table = False
    
    for line in lines:
        stripped = line.strip()
        if stripped.startswith('|') and '---' not in stripped:
            if not in_table:
                in_table = True
                result.append('<table class="w-full border-collapse mb-6">')
            if '标的' in stripped or '指数' in stripped:
                cells = [c.strip() for c in stripped.split('|')[1:-1]]
                result.append('<thead><tr>')
                for cell in cells:
                    result.append(f'<th class="bg-gradient-to-r from-indigo-500 to-purple-500 text-white px-4 py-3 text-left font-semibold">{cell}</th>')
                result.append('</tr></thead><tbody>')
            else:
                cells = [c.strip() for c in stripped.split('|')[1:-1]]
                if cells:
                    result.append('<tr>')
                    for cell in cells:
                        # 处理表格中的emoji和标记
                        cell_html = cell.replace('✅', '<span class="text-green-600">✅</span>')
                        cell_html = cell_html.replace('❌', '<span class="text-red-600">❌</span>')
                        cell_html = cell_html.replace('⏸️', '<span class="text-yellow-600">⏸️</span>')
                        cell_html = cell_html.replace('⭐', '<span class="text-yellow-500">⭐</span>')
                        result.append(f'<td class="border border-gray-200 px-4 py-3 text-gray-700">{cell_html}</td>')
                    result.append('</tr>')
        else:
            if in_table:
                result.append('</tbody></table>')
                in_table = False
            if stripped and not stripped.startswith('<') and not stripped.startswith('|'):
                result.append(f'<p class="text-gray-700 mb-4 leading-relaxed">{line}</p>')
            elif stripped:
                result.append(line)
    
    if in_table:
        result.append('</tbody></table>')
    
    return '\n'.join(result)

# 转换内容
content_html = md_to_html(md_content)

# 完整HTML模板（包含标准11按钮玻璃态导航栏）
html_template = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>S级催化扫描 - 2026年6月5日</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://cdn.jsdelivr.net/npm/font-awesome@4.7.0/css/font-awesome.min.css" rel="stylesheet">
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@300;400;500;700;900&display=swap');
        
        * {{ font-family: 'Noto Sans SC', sans-serif; }}
        
        body {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            position: relative;
            overflow-x: hidden;
        }}
        
        body::before {{
            content: '';
            position: fixed;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: radial-gradient(circle at 30% 20%, rgba(255,255,255,0.1) 0%, transparent 50%),
                        radial-gradient(circle at 70% 80%, rgba(118,75,162,0.3) 0%, transparent 50%);
            animation: float 20s ease-in-out infinite;
            z-index: 0;
            pointer-events: none;
        }}
        
        @keyframes float {{
            0%, 100% {{ transform: translate(0, 0) rotate(0deg); }}
            25% {{ transform: translate(2%, 2%) rotate(1deg); }}
            50% {{ transform: translate(0, 4%) rotate(0deg); }}
            75% {{ transform: translate(-2%, 2%) rotate(-1deg); }}
        }}
        
        @keyframes pulse {{
            0%, 100% {{ transform: scale(1); }}
            50% {{ transform: scale(1.05); }}
        }}
        
        /* 悬浮功能按钮 */
        .float-btn-group {{
            position: fixed;
            right: 24px;
            bottom: 24px;
            z-index: 9999;
            display: flex;
            flex-direction: column;
            gap: 12px;
        }}
        
        .float-btn {{
            width: 52px;
            height: 52px;
            border-radius: 50%;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 20px;
            transition: all 0.3s ease;
        }}
        
        .float-btn:hover {{
            transform: scale(1.1);
            box-shadow: 0 6px 20px rgba(102, 126, 234, 0.6);
        }}
        
        .float-btn.print {{
            background: linear-gradient(135deg, #10b981 0%, #059669 100%);
            box-shadow: 0 4px 15px rgba(16, 185, 129, 0.4);
        }}
        
        .float-btn.print:hover {{
            box-shadow: 0 6px 20px rgba(16, 185, 129, 0.6);
        }}
        
        .float-btn.share {{
            background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%);
            box-shadow: 0 4px 15px rgba(245, 158, 11, 0.4);
        }}
        
        .float-btn.share:hover {{
            box-shadow: 0 6px 20px rgba(245, 158, 11, 0.6);
        }}
        
        .float-btn.top {{
            background: linear-gradient(135deg, #6366f1 0%, #4f46e5 100%);
            box-shadow: 0 4px 15px rgba(99, 102, 241, 0.4);
        }}
        
        .float-btn.top:hover {{
            box-shadow: 0 6px 20px rgba(99, 102, 241, 0.6);
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
        
        .card-glass {{
            background: rgba(255, 255, 255, 0.95);
            box-shadow: 0 15px 40px rgba(118, 75, 162, 0.35);
            border-radius: 20px;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }}
        
        .card-glass:hover {{
            transform: translateY(-3px);
            box-shadow: 0 20px 50px rgba(118, 75, 162, 0.45);
        }}
        
        .gradient-text {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }}
        
        .hot-tag {{
            background: linear-gradient(135deg, #ff6b6b 0%, #ee5a24 100%);
            animation: pulse 2s ease-in-out infinite;
        }}
        
        .market-card-up {{
            background: linear-gradient(135deg, #22c55e 0%, #16a34a 100%);
        }}
        
        .market-card-down {{
            background: linear-gradient(135deg, #ef4444 0%, #dc2626 100%);
        }}
        
        .market-card-neutral {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        }}
        
        .topic-card {{
            border-left: 4px solid #667eea;
            background: linear-gradient(90deg, rgba(102, 126, 234, 0.08) 0%, transparent 100%);
        }}
        
        .risk-box {{
            background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%);
            border: 2px solid #f59e0b;
        }}
        
        .diamond-card {{
            background: linear-gradient(135deg, #0ea5e9 0%, #0284c7 100%);
        }}
        
        /* 汉堡菜单样式 */
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
        
        /* 响应式媒体查询 */
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
        }}
        
        @media (min-width: 769px) and (max-width: 1024px) {{
            .grid-cols-4 {{
                grid-template-columns: repeat(3, 1fr) !important;
            }}
        }}
    </style>
</head>
<body class="pb-20">
    <!-- 导航栏 -->
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
                <a href="/daily-news-insight/intraday/latest.html" class="text-white/80 hover:text-white hover:bg-white/10 text-sm transition-colors px-3 py-1.5 rounded-lg">盘中快报</a>
                <a href="/daily-news-insight/aftermarket/latest.html" class="text-white/80 hover:text-white hover:bg-white/10 text-sm transition-colors px-3 py-1.5 rounded-lg">盘后速递</a>
                <a href="/daily-news-insight/industry_chain/latest.html" class="text-white/80 hover:text-white hover:bg-white/10 text-sm transition-colors px-3 py-1.5 rounded-lg">产业链</a>
                <a href="/daily-news-insight/weekly_review/latest.html" class="text-white/80 hover:text-white hover:bg-white/10 text-sm transition-colors px-3 py-1.5 rounded-lg">周复盘</a>
                <a href="/daily-news-insight/weekly_outlook/latest.html" class="text-white/80 hover:text-white hover:bg-white/10 text-sm transition-colors px-3 py-1.5 rounded-lg">周三前瞻</a>
                <a href="/daily-news-insight/weekend_express/latest.html" class="text-white/80 hover:text-white hover:bg-white/10 text-sm transition-colors px-3 py-1.5 rounded-lg">周末速递</a>
                <a href="/daily-news-insight/tomorrow_catalyst/latest.html" class="text-white/80 hover:text-white hover:bg-white/10 text-sm transition-colors px-3 py-1.5 rounded-lg">明日催化</a>
                <a href="/daily-news-insight/s_level_catalyst/latest.html" class="text-white/80 hover:text-white hover:bg-white/10 text-sm transition-colors px-3 py-1.5 rounded-lg">S级催化</a>
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
        <a href="/daily-news-insight/weekend_express/latest.html" class="mobile-menu-item" onclick="toggleMobileMenu()">📦 周末速递</a>
        <a href="/daily-news-insight/tomorrow_catalyst/latest.html" class="mobile-menu-item" onclick="toggleMobileMenu()">⏰ 明日催化剂</a>
        <a href="/daily-news-insight/s_level_catalyst/latest.html" class="mobile-menu-item" onclick="toggleMobileMenu()">⭐ S级催化扫描</a>
        <a href="/daily-news-insight/monthly/latest.html" class="mobile-menu-item" onclick="toggleMobileMenu()">🗓️ 月度总结</a>
    </div>
    
    <script>
        function toggleMobileMenu() {{
            document.getElementById('mobileMenu').classList.toggle('show');
            document.body.style.overflow = document.getElementById('mobileMenu').classList.contains('show') ? 'hidden' : '';
        }}
    </script>

    <!-- 主内容区 -->
    <div class="pt-24 px-4 relative z-10">
        <div class="max-w-5xl mx-auto">
            <!-- 头部 -->
            <div class="card-glass p-8 mb-8 border-2 border-white/20">
                <div class="text-center">
                    <div class="w-20 h-20 mx-auto mb-6 rounded-2xl bg-gradient-to-br from-indigo-500 to-purple-600 flex items-center justify-center shadow-2xl" style="animation: pulse 3s ease-in-out infinite;">
                        <i class="fa fa-star text-white text-4xl"></i>
                    </div>
                    <h1 class="text-4xl font-black gradient-text mb-3">S级催化扫描</h1>
                    <p class="text-gray-500 text-lg">📅 2026年6月5日 · 星期五 · 盘前版</p>
                    <div class="mt-4 inline-flex items-center px-4 py-2 rounded-full bg-amber-100 text-amber-800 text-sm">
                        <i class="fa fa-exclamation-triangle mr-2"></i>
                        <strong>今日焦点：存储超级周期持续深化，HBM价格暴涨500%，美股风格大切换</strong>
                    </div>
                </div>
            </div>

            <!-- 报告内容 -->
            <div class="card-glass p-6">
                {content_html}
            </div>
        </div>
    </div>

    <!-- 悬浮功能按钮组 -->
    <div class="float-btn-group">
        <button class="float-btn print" onclick="window.print()" title="打印/导出PDF">
            <i class="fa fa-print"></i>
        </button>
        <button class="float-btn share" onclick="navigator.clipboard.writeText(window.location.href)" title="分享链接">
            <i class="fa fa-share-alt"></i>
        </button>
        <button class="float-btn top" onclick="window.scrollTo({{top: 0, behavior: 'smooth'}})" title="返回顶部">
            <i class="fa fa-arrow-up"></i>
        </button>
    </div>

</body>
</html>'''

# 写入文件
with open("docs/s级催化扫描/20260605_盘前_S级催化扫描.html", "w", encoding="utf-8") as f:
    f.write(html_template)

print("✅ S级催化扫描报告HTML已生成完成！")
print(f"📄 文件路径：docs/s级催化扫描/20260605_盘前_S级催化扫描.html")
