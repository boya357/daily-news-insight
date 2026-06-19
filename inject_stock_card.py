"""
批量注入全局股票悬浮卡片JS到所有HTML页面
"""
import os
import glob
from bs4 import BeautifulSoup

def inject_js_to_html(html_path, js_path):
    """将JS注入到HTML页面的</body>标签前"""
    try:
        with open(html_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 检查是否已经注入过
        if 'stock-hover-card.js' in content or 'StockHoverCard' in content:
            return False, '已存在'
        
        # 计算JS的相对路径
        html_dir = os.path.dirname(os.path.abspath(html_path))
        js_abs = os.path.abspath(js_path)
        rel_path = os.path.relpath(js_abs, html_dir)
        
        # 注入脚本
        script_tag = f'<script src="{rel_path}" defer></script>\n'
        
        if '</body>' in content:
            content = content.replace('</body>', script_tag + '</body>')
        elif '</html>' in content:
            content = content.replace('</html>', script_tag + '</html>')
        else:
            content += '\n' + script_tag
        
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return True, '成功'
    except Exception as e:
        return False, str(e)

def main():
    docs_dir = 'docs'
    js_path = os.path.join(docs_dir, 'js', 'stock-hover-card.js')
    
    if not os.path.exists(js_path):
        print(f"❌ JS文件不存在: {js_path}")
        return
    
    # 找出所有HTML文件
    html_files = glob.glob(os.path.join(docs_dir, '**/*.html'), recursive=True)
    print(f"📄 找到 {len(html_files)} 个HTML文件")
    
    success_count = 0
    skip_count = 0
    fail_count = 0
    
    for html_file in html_files:
        # 跳过一些特殊文件
        if 'stock-hover-card' in html_file:
            continue
            
        ok, msg = inject_js_to_html(html_file, js_path)
        rel_file = os.path.relpath(html_file, docs_dir)
        
        if ok:
            success_count += 1
            print(f"✅ {rel_file}")
        elif msg == '已存在':
            skip_count += 1
            print(f"⏭️  {rel_file} (已存在)")
        else:
            fail_count += 1
            print(f"❌ {rel_file}: {msg}")
    
    print(f"\n📊 完成: 成功{success_count}个, 跳过{skip_count}个, 失败{fail_count}个")

if __name__ == '__main__':
    main()
