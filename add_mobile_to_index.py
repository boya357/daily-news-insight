#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
为首页index.html添加移动端适配
"""
# 移动端CSS样式
MOBILE_CSS = '''        
        /* ========== 汉堡菜单样式 ========== */
        .hamburger-btn {
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
        }
        
        .mobile-menu {
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
        }
        
        .mobile-menu.show {
            display: block;
        }
        
        .mobile-menu-item {
            display: block;
            color: white !important;
            padding: 16px 24px;
            text-decoration: none;
            font-size: 18px;
            border-bottom: 1px solid rgba(255,255,255,0.1);
        }
        
        .mobile-menu-item:hover {
            background: rgba(255,255,255,0.1);
        }
        
        .close-menu-btn {
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
        }
        
        /* ========== 移动端响应式优化 ========== */
        @media (max-width: 768px) {
            /* 导航栏：隐藏按钮，显示汉堡 */
            .nav-links {
                display: none !important;
            }
            .hamburger-btn {
                display: block !important;
            }
            
            /* 卡片网格改为2列 */
            .grid-cols-2, .grid-cols-3, .grid-cols-4 {
                grid-template-columns: repeat(2, 1fr) !important;
            }
            
            /* 字体响应式缩放 */
            .text-4xl { font-size: 1.875rem !important; }
            .text-3xl { font-size: 1.5rem !important; }
            .text-2xl { font-size: 1.25rem !important; }
            
            /* 内边距紧凑化 */
            .p-8 { padding: 1.5rem !important; }
            .p-6 { padding: 1.25rem !important; }
            
            /* 表格横向滚动 */
            table { 
                display: block; 
                overflow-x: auto;
                -webkit-overflow-scrolling: touch;
            }
            
            /* 增大点击区域 */
            a, button { 
                min-height: 44px; 
                display: inline-flex;
                align-items: center;
            }
        }
        
        /* ========== 平板端专用样式 ========== */
        @media (min-width: 769px) and (max-width: 1024px) {
            .grid-cols-4 { grid-template-columns: repeat(3, 1fr) !important; }
        }'''

# 移动端菜单HTML（在</nav>之后插入）
MOBILE_MENU_HTML = '''    <button class="hamburger-btn" onclick="toggleMobileMenu()">☰</button>
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

def main():
    with open('docs/index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. 在</style>之前插入移动端CSS
    content = content.replace('    </style>', MOBILE_CSS + '\n    </style>')
    
    # 2. 给导航栏div添加nav-links类
    content = content.replace(
        '<div class="flex items-center space-x-1 flex-wrap gap-1">',
        '<div class="nav-links flex items-center space-x-1 flex-wrap gap-1">'
    )
    
    # 3. 在导航链接结束后添加汉堡按钮，在</nav>后添加移动端菜单
    # 找到 </nav> 位置，在它之前添加汉堡按钮，之后添加菜单
    nav_end_pattern = '            </div>\n        </div>\n    </nav>'
    content = content.replace(nav_end_pattern, '            </div>\n' + MOBILE_MENU_HTML)
    
    with open('docs/index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print('✅ 首页index.html移动端适配完成！')

if __name__ == '__main__':
    main()
