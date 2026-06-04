#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
最终版导航栏修复脚本
基于首页正确模板，完全重写所有页面的导航栏
"""

import os
import re

# 首页正确的导航栏模板
CORRECT_NAV_TEMPLATE = '''    <nav class="fixed top-0 left-0 right-0 z-50 glass-nav">
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
                <a href="/daily-news-insight/S级催化扫描/latest.html" class="text-white/80 hover:text-white hover:bg-white/10 text-sm transition-colors px-3 py-1.5 rounded-lg">S级催化</a>
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
        <a href="/daily-news-insight/S级催化扫描/latest.html" class="mobile-menu-item" onclick="toggleMobileMenu()">⭐ S级催化扫描</a>
        <a href="/daily-news-insight/monthly/latest.html" class="mobile-menu-item" onclick="toggleMobileMenu()">🗓️ 月度总结</a>
    </div>
    
    <script>
        function toggleMobileMenu() {
            document.getElementById('mobileMenu').classList.toggle('show');
        }
    </script>
'''

# 需要添加的CSS样式
MOBILE_CSS = '''        .hamburger-btn {
            display: none;
            background: rgba(102, 126, 234, 0.2);
            border: 1px solid rgba(102, 126, 234, 0.3);
            color: #667eea;
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
        }
'''

def fix_navbar_in_file(filepath):
    """修复单个文件的导航栏"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 1. 查找并替换导航栏部分
        # 找到<nav ...>开始标签（支持不同的class变体）
        nav_start = -1
        # 尝试不同的nav变体
        nav_patterns = [
            '<nav class="fixed top-0 left-0 right-0 z-50 glass-nav">',
            '<nav class="fixed top-0 left-0 right-0 z-50 glass-nav bg-white/80">',
            '<nav class="fixed top-0 left-0 right-0 z-50 glass-nav shadow-lg">',
        ]
        for pattern in nav_patterns:
            pos = content.find(pattern)
            if pos != -1:
                nav_start = pos
                break
        
        if nav_start == -1:
            # 尝试更宽泛的匹配
            nav_start = content.find('<nav class="fixed top-0')
        
        if nav_start == -1:
            print(f"  ⚠️ 未找到导航栏，跳过: {filepath}")
            return False
        
        # 找到</nav>结束标签
        nav_end = content.find('</nav>', nav_start) + len('</nav>')
        if nav_end == -1 + len('</nav>'):
            print(f"  ⚠️ 未找到</nav>标签，跳过: {filepath}")
            return False
        
        # 替换整个导航栏（包括nav和移动端菜单和脚本）
        # 先检查是否已有移动端菜单，如果有也要删除
        mobile_menu_start = content.find('<!-- 移动端全屏菜单 -->', nav_end)
        if mobile_menu_start != -1:
            # 找到script结束位置
            script_end = content.find('</script>', mobile_menu_start) + len('</script>')
            if script_end > mobile_menu_start:
                nav_end = script_end
        
        # 替换导航栏
        new_content = content[:nav_start] + CORRECT_NAV_TEMPLATE + content[nav_end:]
        content = new_content
        
        # 2. 添加CSS样式（如果没有）
        if '.hamburger-btn' not in content:
            # 找个合适的位置插入CSS（在</style>之前）
            style_end = content.find('</style>')
            if style_end != -1:
                content = content[:style_end] + MOBILE_CSS + '\n' + content[style_end:]
        
        # 3. 确保nav-links class存在（虽然模板里已经有了，双重保险）
        content = content.replace('<div class="flex items-center space-x-1 flex-wrap gap-1">', 
                                  '<div class="nav-links flex items-center space-x-1 flex-wrap gap-1">')
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"  ✅ 已修复: {filepath}")
        return True
    except Exception as e:
        print(f"  ❌ 失败: {filepath}, 错误: {e}")
        return False

def main():
    # 今日报告文件列表
    today_files = [
        'daily/20260604_每日新闻洞察.html',
        'intraday/20260604_盘中快报.html',
        'aftermarket/20260604_盘后速递.html',
        's级催化扫描/20260604_盘前_S级催化扫描.html',
        's级催化扫描/20260604_盘后_S级催化扫描.html',
        '明日催化剂/20260604_明日催化剂.html',
    ]
    
    docs_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    print("开始修复导航栏...\n")
    
    success_count = 0
    for f in today_files:
        filepath = os.path.join(docs_dir, f)
        if os.path.exists(filepath):
            if fix_navbar_in_file(filepath):
                success_count += 1
        else:
            print(f"  ⚠️ 文件不存在: {f}")
    
    print(f"\n完成！成功修复 {success_count}/{len(today_files)} 个文件")

if __name__ == '__main__':
    main()
