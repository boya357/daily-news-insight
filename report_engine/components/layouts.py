"""
布局组件库 - 页面结构组件
"""

def standard_navigation():
    """
    标准导航栏 - 所有报告共用
    """
    return '''
    <!-- ========== 玻璃态导航栏 ========== -->
    <nav class="glass-nav fixed top-0 left-0 right-0 z-50">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex items-center justify-between h-16">
                <div class="flex items-center">
                    <span class="text-white text-lg font-bold">📊 产业链深度研究</span>
                </div>
                <div class="hidden md:flex items-center space-x-1">
                    <a href="../daily/latest.html" class="px-3 py-2 text-white/80 hover:text-white text-sm">每日快讯</a>
                    <a href="../intraday/latest.html" class="px-3 py-2 text-white/80 hover:text-white text-sm">盘中快报</a>
                    <a href="../s级催化扫描/latest.html" class="px-3 py-2 text-white/80 hover:text-white text-sm">S级催化</a>
                    <a href="../industry_chain/latest.html" class="px-3 py-2 text-white bg-white/20 rounded-lg text-sm font-medium">产业链总览</a>
                    <a href="../weekly_outlook/latest.html" class="px-3 py-2 text-white/80 hover:text-white text-sm">周三前瞻</a>
                    <a href="../周末速递/latest.html" class="px-3 py-2 text-white/80 hover:text-white text-sm">周末速递</a>
                    <a href="../明日催化剂/latest.html" class="px-3 py-2 text-white/80 hover:text-white text-sm">明日催化</a>
                </div>
                <button class="hamburger-btn" onclick="toggleMobileMenu()">
                    <i class="fa fa-bars"></i>
                </button>
            </div>
        </div>
    </nav>
    
    <!-- 移动端菜单 -->
    <div id="mobileMenu" class="mobile-menu">
        <button class="close-menu-btn" onclick="toggleMobileMenu()">
            <i class="fa fa-times"></i>
        </button>
        <a href="../daily/latest.html" class="mobile-menu-item">每日快讯</a>
        <a href="../intraday/latest.html" class="mobile-menu-item">盘中快报</a>
        <a href="../s级催化扫描/latest.html" class="mobile-menu-item">S级催化</a>
        <a href="../industry_chain/latest.html" class="mobile-menu-item">产业链总览</a>
        <a href="../weekly_outlook/latest.html" class="mobile-menu-item">周三前瞻</a>
        <a href="../周末速递/latest.html" class="mobile-menu-item">周末速递</a>
        <a href="../明日催化剂/latest.html" class="mobile-menu-item">明日催化</a>
    </div>
    '''


def standard_footer():
    """
    标准页脚 - 所有报告共用
    """
    return '''
    <!-- ========== 页脚 ========== -->
    <footer class="mt-16 pb-8 text-center">
        <div class="text-gray-500 text-sm">
            <p>本报告由AI生成，仅供参考，不构成投资建议</p>
            <p class="mt-1">数据来源：公开信息、公司公告、行业研报</p>
        </div>
    </footer>
    '''


def report_page(title, subtitle, content_sections, metrics=None):
    """
    完整报告页面生成器 - 内容驱动，自动适配最佳布局
    
    Args:
        title: 报告主标题
        subtitle: 报告副标题
        content_sections: 内容区块列表，每个区块是组件HTML
        metrics: 顶部指标数据
    """
    from .core import gradient_banner
    
    nav = standard_navigation()
    banner = gradient_banner(title, subtitle, metrics)
    footer = standard_footer()
    
    # 内容区域
    content_html = ''.join(content_sections)
    
    return f'''
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
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
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            z-index: 0;
            pointer-events: none;
        }}
        
        .glass-nav {{
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            border-bottom: 1px solid rgba(255, 255, 255, 0.2);
            z-index: 2147483647 !important;
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
        
        @media (max-width: 768px) {{
            .hamburger-btn {{
                display: block;
            }}
            .hidden.md\\:flex {{
                display: none !important;
            }}
        }}
    </style>
</head>
<body class="relative z-10 min-h-screen font-sans">
    {nav}
    
    <div class="pt-24 pb-8 px-4">
        <div class="max-w-6xl mx-auto">
            {banner}
            
            <!-- 内容区域 -->
            <div class="mt-12 space-y-0">
                {content_html}
            </div>
            
            {footer}
        </div>
    </div>
    
    <script>
        function toggleMobileMenu() {{
            document.getElementById('mobileMenu').classList.toggle('show');
        }}
    </script>
</body>
</html>
    '''
