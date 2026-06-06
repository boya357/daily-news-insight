#!/usr/bin/env python3
"""
标准导航栏批量修复工具
"""

import os
import re
import sys
import json

COMPONENTS_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'components')

def load_navbar_component():
    with open(os.path.join(COMPONENTS_DIR, 'navbar.json'), 'r', encoding='utf-8') as f:
        return json.load(f)

NAVBAR = load_navbar_component()

def has_standard_navbar(html_content):
    return 'glass-nav' in html_content and '投资研究中心' in html_content and 'max-w-5xl' in html_content

def has_tailwind(html_content):
    return 'tailwindcss' in html_content

def has_mobile_menu(html_content):
    return 'id="mobileMenu"' in html_content

def has_toggle_script(html_content):
    return 'toggleMobileMenu' in html_content

def remove_old_navbar(html_content):
    """移除旧的导航栏"""
    # 移除旧的nav标签
    html_content = re.sub(r'<nav class="nav">.*?</nav>', '', html_content, flags=re.DOTALL)
    html_content = re.sub(r'<div class="nav[^"]*">.*?</div>', '', html_content, flags=re.DOTALL)
    
    # 移除旧的导航相关CSS
    style_match = re.search(r'<style>(.*?)</style>', html_content, re.DOTALL)
    if style_match:
        style_content = style_match.group(1)
        css_patterns = [
            r'\.nav\s*\{[^}]*\}',
            r'\.nav-container\s*\{[^}]*\}',
            r'\.nav-logo\s*\{[^}]*\}',
            r'\.nav-link\s*\{[^}]*\}',
            r'\.nav-link\.active\s*\{[^}]*\}',
            r'\.nav-link:hover\s*\{[^}]*\}',
            r'\.nav-links\s*\{[^}]*\}',
        ]
        for pattern in css_patterns:
            style_content = re.sub(pattern, '', style_content)
        html_content = html_content[:style_match.start(1)] + style_content + html_content[style_match.end(1):]
    
    return html_content

def add_tailwind(html_content):
    """添加Tailwind CSS和Font Awesome"""
    tailwind = '<script src="https://cdn.tailwindcss.com"></script>'
    fontawesome = '<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.5.1/css/all.min.css">'
    
    head_end = html_content.find('</head>')
    if head_end == -1:
        return html_content
    
    additions = []
    if not has_tailwind(html_content):
        additions.append(tailwind)
    if 'font-awesome' not in html_content and 'fontawesome' not in html_content:
        additions.append(fontawesome)
    
    if additions:
        insert = '\n    ' + '\n    '.join(additions) + '\n    '
        html_content = html_content[:head_end] + insert + html_content[head_end:]
    
    return html_content

def add_navbar_css(html_content):
    """添加导航栏CSS"""
    if '.glass-nav' in html_content:
        return html_content
    
    style_match = re.search(r'<style>(.*?)</style>', html_content, re.DOTALL)
    navbar_css = NAVBAR['css']
    
    if style_match:
        insert_pos = style_match.start(1)
        new_css = '\n        /* ===== 标准导航栏样式 ===== */\n        ' + navbar_css + '\n'
        html_content = html_content[:insert_pos] + new_css + html_content[insert_pos:]
    else:
        head_end = html_content.find('</head>')
        if head_end != -1:
            style_tag = f'\n    <style>\n        {navbar_css}\n    </style>\n'
            html_content = html_content[:head_end] + style_tag + html_content[head_end:]
    
    return html_content

def add_navbar_html(html_content):
    """在body开头添加导航栏"""
    body_start = html_content.find('<body')
    if body_start == -1:
        return html_content
    
    body_tag_end = html_content.find('>', body_start)
    if body_tag_end == -1:
        return html_content
    
    insert_pos = body_tag_end + 1
    navbar_html = '\n    ' + NAVBAR['nav_html'] + '\n'
    html_content = html_content[:insert_pos] + navbar_html + html_content[insert_pos:]
    
    return html_content

def add_mobile_menu(html_content):
    """添加移动端菜单"""
    if has_mobile_menu(html_content):
        return html_content
    
    body_end = html_content.rfind('</body>')
    if body_end == -1:
        return html_content
    
    mobile_html = '\n    ' + NAVBAR['mobile_menu_html'] + '\n'
    html_content = html_content[:body_end] + mobile_html + html_content[body_end:]
    
    return html_content

def add_toggle_script(html_content):
    """添加toggleMobileMenu函数"""
    if has_toggle_script(html_content):
        return html_content
    
    body_end = html_content.rfind('</body>')
    if body_end == -1:
        return html_content
    
    script = '\n    <script>\n        function toggleMobileMenu() {\n            var menu = document.getElementById("mobileMenu");\n            menu.classList.toggle("show");\n        }\n    </script>\n'
    html_content = html_content[:body_end] + script + html_content[body_end:]
    
    return html_content

def fix_content_padding(html_content):
    """修复内容顶部间距，避免被固定导航栏遮挡"""
    if 'mt-24' in html_content or 'pt-24' in html_content:
        return html_content
    
    # 尝试给container添加mt-24
    if 'class="container"' in html_content:
        html_content = html_content.replace('class="container"', 'class="container mt-24"', 1)
    elif '<main>' in html_content:
        html_content = html_content.replace('<main>', '<main class="mt-24">', 1)
    
    return html_content

def fix_navbar_file(filepath):
    """修复单个HTML文件"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        return False, f"读取失败: {e}"
    
    original = content
    
    # 检查是否已是标准导航栏
    if has_standard_navbar(content):
        complete = has_mobile_menu(content) and has_toggle_script(content) and has_tailwind(content)
        if complete:
            return True, "已是标准导航栏"
    
    # 执行修复步骤
    content = remove_old_navbar(content)
    content = add_tailwind(content)
    content = add_navbar_css(content)
    
    if not has_standard_navbar(content):
        content = add_navbar_html(content)
    
    content = add_mobile_menu(content)
    content = add_toggle_script(content)
    content = fix_content_padding(content)
    
    if content == original:
        return True, "无需修改"
    
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True, "修复成功"
    except Exception as e:
        return False, f"保存失败: {e}"

def process_path(path):
    """处理路径（文件或目录）"""
    if os.path.isfile(path):
        if path.endswith('.html'):
            success, msg = fix_navbar_file(path)
            status = "✅" if success else "❌"
            print(f"{status} {os.path.basename(path)} - {msg}")
            return 1 if success else 0
        return 0
    
    if os.path.isdir(path):
        count = 0
        skip = ['node_modules', '.git', '__pycache__']
        
        for root, dirs, files in os.walk(path):
            dirs[:] = [d for d in dirs if d not in skip]
            for file in files:
                if file.endswith('.html'):
                    fp = os.path.join(root, file)
                    success, msg = fix_navbar_file(fp)
                    if msg not in ["已是标准导航栏", "无需修改"]:
                        rel = os.path.relpath(fp, path)
                        status = "✅" if success else "❌"
                        print(f"{status} {rel} - {msg}")
                    if success:
                        count += 1
        return count
    
    return 0

def main():
    if len(sys.argv) < 2:
        print("用法:")
        print("  python tools/fix_navbar.py <文件或目录>")
        print("  python tools/fix_navbar.py --all   # 修复docs下所有HTML")
        print("  python tools/fix_navbar.py --check # 检查所有文件状态")
        return
    
    arg = sys.argv[1]
    
    if arg == '--all':
        docs_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'docs')
        print(f"批量修复所有HTML文件 (目录: docs/)")
        print("-" * 60)
        count = process_path(docs_dir)
        print("-" * 60)
        print(f"共处理 {count} 个文件")
    
    elif arg == '--check':
        docs_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'docs')
        print("检查导航栏状态...")
        standard = 0
        non_standard = 0
        
        for root, dirs, files in os.walk(docs_dir):
            dirs[:] = [d for d in dirs if d not in ['.git', '__pycache__']]
            for file in files:
                if file.endswith('.html'):
                    fp = os.path.join(root, file)
                    with open(fp, 'r', encoding='utf-8') as f:
                        c = f.read()
                    if has_standard_navbar(c):
                        standard += 1
                    else:
                        non_standard += 1
        
        print(f"\n标准: {standard} 个")
        print(f"需修复: {non_standard} 个")
    
    else:
        if not os.path.exists(arg):
            print(f"错误: 路径不存在 - {arg}")
            return
        process_path(arg)

if __name__ == '__main__':
    main()
