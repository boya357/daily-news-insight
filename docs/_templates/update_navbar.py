#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
统一更新所有HTML页面的导航栏为固定7项格式
"""
import os
import re

# 统一的导航栏模板（注意：每个页面需要根据所在目录调整相对路径）
NAV_TEMPLATE = '''    <div class="nav-bar">
        <a href="{prefix}index.html" class="nav-item">首页</a>
        <a href="{prefix}daily/latest.html" class="nav-item">日报</a>
        <a href="{prefix}intraday/latest.html" class="nav-item">盘中</a>
        <a href="{prefix}aftermarket/latest.html" class="nav-item">盘后</a>
        <a href="{prefix}industry_chain/latest.html" class="nav-item">产业链</a>
        <a href="{prefix}催化日历/latest.html" class="nav-item">催化日历</a>
        <a href="{prefix}周末速递/latest.html" class="nav-item">周末速递</a>
    </div>'''

# 匹配nav-bar的正则表达式
NAV_PATTERN = re.compile(r'    <div class="nav-bar">.*?    </div>', re.DOTALL)

def get_prefix(filepath):
    """根据文件路径计算相对路径前缀"""
    # 路径格式: ./intraday/xxx.html 或 intraday/xxx.html
    # 去掉开头的 ./ 后计算深度
    if filepath.startswith('./'):
        filepath = filepath[2:]
    depth = filepath.count(os.sep)
    if depth == 0:
        return ''
    else:
        return '../' * depth

def update_navbar(filepath):
    """更新单个文件的导航栏"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 检查是否有导航栏
        if 'class="nav-bar"' not in content:
            print(f"⚠️  {filepath} - 没有找到导航栏，跳过")
            return False
        
        # 计算前缀
        prefix = get_prefix(filepath)
        new_nav = NAV_TEMPLATE.format(prefix=prefix)
        
        # 替换导航栏
        new_content = NAV_PATTERN.sub(new_nav, content)
        
        if new_content == content:
            print(f"✅  {filepath} - 导航栏已是最新，无需更新")
            return True
        
        # 写入文件
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"✅  {filepath} - 导航栏已更新")
        return True
        
    except Exception as e:
        print(f"❌  {filepath} - 更新失败: {e}")
        return False

def main():
    """主函数：遍历所有HTML文件"""
    print("=" * 60)
    print("统一更新所有HTML页面导航栏")
    print("=" * 60)
    
    # 遍历当前目录（docs）下所有HTML文件
    html_files = []
    for root, dirs, files in os.walk('.'):
        # 排除_templates目录
        if '_templates' in root:
            continue
        for file in files:
            if file.endswith('.html'):
                html_files.append(os.path.join(root, file))
    
    print(f"\n找到 {len(html_files)} 个HTML文件\n")
    
    # 逐个更新
    success = 0
    for f in sorted(html_files):
        if update_navbar(f):
            success += 1
    
    print("\n" + "=" * 60)
    print(f"完成：成功处理 {success}/{len(html_files)} 个文件")
    print("=" * 60)

if __name__ == '__main__':
    main()
