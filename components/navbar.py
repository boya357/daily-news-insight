"""
标准导航栏组件
提供统一的导航栏HTML、CSS、JS代码
所有新生成的页面都必须使用此组件
"""

import json
import os

_NAVBAR_DATA = None

def get_navbar():
    """获取完整的导航栏数据"""
    global _NAVBAR_DATA
    if _NAVBAR_DATA is None:
        json_path = os.path.join(os.path.dirname(__file__), 'navbar.json')
        with open(json_path, 'r', encoding='utf-8') as f:
            _NAVBAR_DATA = json.load(f)
    return _NAVBAR_DATA

def get_navbar_html():
    """获取导航栏HTML代码"""
    return get_navbar()['nav_html']

def get_navbar_css():
    """获取导航栏CSS代码"""
    return get_navbar()['css']

def get_mobile_menu_html():
    """获取移动端菜单HTML代码"""
    return get_navbar()['mobile_menu_html']

def get_toggle_script():
    """获取切换菜单的JS代码"""
    return '''function toggleMobileMenu() {
        var menu = document.getElementById('mobileMenu');
        menu.classList.toggle('show');
    }'''

def inject_into_html(html_content):
    """
    将标准导航栏注入到HTML内容中
    自动处理: 添加Tailwind、添加CSS、添加导航栏HTML、添加移动端菜单、添加JS
    """
    import re
    
    result = html_content
    
    # 1. 添加Tailwind CSS (如果没有的话)
    if 'tailwindcss' not in result:
        tailwind = '<script src="https://cdn.tailwindcss.com"></script>'
        head_end = result.find('</head>')
        if head_end != -1:
            result = result[:head_end] + tailwind + '\n    ' + result[head_end:]
    
    # 2. 添加Font Awesome (如果没有的话)
    if 'font-awesome' not in result and 'fontawesome' not in result:
        fa = '<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.5.1/css/all.min.css">'
        head_end = result.find('</head>')
        if head_end != -1:
            result = result[:head_end] + fa + '\n    ' + result[head_end:]
    
    # 3. 添加导航栏CSS (如果没有的话)
    navbar_css = get_navbar_css()
    if '.glass-nav' not in result:
        style_match = re.search(r'<style>(.*?)</style>', result, re.DOTALL)
        if style_match:
            insert_pos = style_match.start(1)
            result = result[:insert_pos] + '\n        /* ===== 标准导航栏样式 ===== */\n        ' + navbar_css + '\n' + result[insert_pos:]
        else:
            head_end = result.find('</head>')
            if head_end != -1:
                style_tag = f'\n    <style>\n        {navbar_css}\n    </style>\n'
                result = result[:head_end] + style_tag + result[head_end:]
    
    # 4. 添加导航栏HTML (如果没有的话)
    navbar_html = get_navbar_html()
    if 'glass-nav' not in result:
        body_start = result.find('<body')
        if body_start != -1:
            body_tag_end = result.find('>', body_start)
            if body_tag_end != -1:
                result = result[:body_tag_end+1] + '\n    ' + navbar_html + '\n' + result[body_tag_end+1:]
    
    # 5. 添加移动端菜单 (如果没有的话)
    mobile_html = get_mobile_menu_html()
    if 'id="mobileMenu"' not in result and 'mobile-menu' not in result:
        body_end = result.rfind('</body>')
        if body_end != -1:
            result = result[:body_end] + '\n    ' + mobile_html + '\n' + result[body_end:]
    
    # 6. 添加切换脚本 (如果没有的话)
    if 'toggleMobileMenu' not in result:
        body_end = result.rfind('</body>')
        if body_end != -1:
            script = f'\n    <script>\n        {get_toggle_script()}\n    </script>\n'
            result = result[:body_end] + script + result[body_end:]
    
    # 7. 确保内容区域有顶部间距
    if 'mt-24' not in result and 'pt-24' not in result:
        # 尝试给container添加mt-24
        if 'class="container"' in result:
            result = result.replace('class="container"', 'class="container mt-24"', 1)
        elif '<main>' in result:
            result = result.replace('<main>', '<main class="mt-24">', 1)
    
    return result

def has_standard_navbar(html_content):
    """检查HTML是否包含标准导航栏"""
    return all([
        'glass-nav' in html_content,
        '投资研究中心' in html_content,
        'max-w-5xl' in html_content,
        'mobileMenu' in html_content or 'mobile-menu' in html_content,
        'toggleMobileMenu' in html_content,
    ])

if __name__ == '__main__':
    # 测试
    print("导航栏组件加载成功")
    print(f"导航链接数量: {get_navbar_html().count('href=')}")
    print(f"CSS长度: {len(get_navbar_css())}")
