#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
批量为所有列表页脚本添加移动端适配（汉堡菜单+响应式CSS）
"""
import re
import os

# 需要处理的文件列表
FILES = [
    'update_daily_list.py',
    'update_intraday_list.py',
    'update_aftermarket_list.py',
    'update_weekly_review_list.py',
    'update_weekly_outlook_list.py',
    'update_weekend_express_list.py',
    'update_tomorrow_catalyst_list.py',
    'update_slevel_catalyst_list.py',
    'update_monthly_list.py',
]

# 新的CSS样式（替换原来的.line-clamp-2部分）
NEW_CSS = '''        .line-clamp-2 {{
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
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            z-index: 99998;
            display: none;
            padding-top: 80px;
            overflow-y: auto;
        }}
        
        .mobile-menu.show {{
            display: block;
        }}
        
        .mobile-menu-item {{
            display: block;
            color: white !important;
            padding: 16px 24px;
            text-decoration: none;
            font-size: 18px;
            border-bottom: 1px solid rgba(255,255,255,0.1);
        }}
        
        .mobile-menu-item:hover {{
            background: rgba(255,255,255,0.1);
        }}
        
        .close-menu-btn {{
            position: absolute;
            top: 16px;
            right: 16px;
            background: rgba(255,255,255,0.2);
            border: none;
            color: white;
            width: 44px;
            height: 44px;
            border-radius: 8px;
            cursor: pointer;
            font-size: 20px;
        }}
        
        /* ========== 移动端响应式优化 ========== */
        @media (max-width: 768px) {{
            /* 导航栏：隐藏按钮，显示汉堡 */
            .nav-links {{
                display: none !important;
            }}
            .hamburger-btn {{
                display: block !important;
            }}
            
            /* 卡片网格改为2列 */
            .grid-cols-4 {{
                grid-template-columns: repeat(2, 1fr) !important;
            }}
            
            /* 字体响应式缩放 */
            .text-4xl {{ font-size: 1.875rem !important; }}
            .text-3xl {{ font-size: 1.5rem !important; }}
            .text-2xl {{ font-size: 1.25rem !important; }}
            
            /* 内边距紧凑化 */
            .p-8 {{ padding: 1.5rem !important; }}
            .p-6 {{ padding: 1.25rem !important; }}
            
            /* 表格横向滚动 */
            table {{ 
                display: block; 
                overflow-x: auto;
                -webkit-overflow-scrolling: touch;
            }}
            
            /* 增大点击区域 */
            a, button {{ 
                min-height: 44px; 
                display: inline-flex;
                align-items: center;
            }}
        }}
        
        /* ========== 平板端专用样式 ========== */
        @media (min-width: 769px) and (max-width: 1024px) {{
            .grid-cols-4 {{ grid-template-columns: repeat(3, 1fr) !important; }}
        }}'''

# 导航栏替换：添加nav-links类 + 汉堡按钮 + 移动端菜单
# 匹配原来的导航栏结束位置：</div>\n    </nav>
NAV_PATTERN = r'(            <div class="flex items-center space-x-1 flex-wrap gap-1">\n.*?</div>\n        </div>\n    </nav>)'

NEW_NAV = '''            <div class="nav-links flex items-center space-x-1 flex-wrap gap-1">
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
    </script>'''

def process_file(filename):
    """处理单个文件"""
    if not os.path.exists(filename):
        print(f'❌ {filename} 不存在，跳过')
        return False
    
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. 替换CSS部分：找到.line-clamp-2并扩展
    old_css_pattern = r'(        \.line-clamp-2 \{\n            display: -webkit-box;\n            -webkit-line-clamp: 2;\n            -webkit-box-orient: vertical;\n            overflow: hidden;\n        \}\n    </style>)'
    
    if re.search(old_css_pattern, content, re.DOTALL):
        content = re.sub(old_css_pattern, NEW_CSS + '\n    </style>', content, flags=re.DOTALL)
        print(f'✅ {filename}: CSS样式已更新')
    else:
        print(f'⚠️ {filename}: 未找到CSS样式，跳过CSS')
    
    # 2. 替换导航栏部分：添加nav-links类 + 汉堡按钮 + 移动端菜单
    if '<div class="flex items-center space-x-1 flex-wrap gap-1">' in content:
        # 找到导航栏div，添加nav-links类
        content = content.replace(
            '<div class="flex items-center space-x-1 flex-wrap gap-1">',
            '<div class="nav-links flex items-center space-x-1 flex-wrap gap-1">'
        )
        
        # 在</nav>前添加汉堡按钮，在</nav>后添加移动端菜单和JS
        nav_end_pattern = r'(            </div>\n        </div>\n    </nav>)'
        if re.search(nav_end_pattern, content):
            # 在导航链接的</div>之后添加汉堡按钮
            hamburger_insert = '''            </div>
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
        function toggleMobileMenu() {
            document.getElementById('mobileMenu').classList.toggle('show');
            document.body.style.overflow = document.getElementById('mobileMenu').classList.contains('show') ? 'hidden' : '';
        }
    </script>'''
            
            content = re.sub(nav_end_pattern, hamburger_insert, content)
            print(f'✅ {filename}: 导航栏已更新')
        else:
            print(f'⚠️ {filename}: 未找到导航栏结束位置')
    else:
        print(f'⚠️ {filename}: 未找到导航栏div')
    
    # 写回文件
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return True

def main():
    print('=' * 50)
    print('开始批量添加移动端适配...')
    print('=' * 50)
    
    success_count = 0
    for f in FILES:
        if process_file(f):
            success_count += 1
        print('---')
    
    print('=' * 50)
    print(f'完成！成功处理 {success_count}/{len(FILES)} 个文件')
    print('=' * 50)

if __name__ == '__main__':
    main()
