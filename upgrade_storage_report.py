#!/usr/bin/env python3
"""
将原版存储芯片报告升级为V3.5 Pro版
保留所有原始内容和图表，仅替换导航栏和调整样式
"""
import re
import os

def upgrade_storage_report():
    # 读取原版报告
    with open('original_storage_report.html', 'r', encoding='utf-8') as f:
        html = f.read()
    
    # ========== 1. 替换导航栏 ==========
    # 找到原始导航栏
    nav_pattern = r'<nav class="fixed top-0 left-0 right-0 z-50 glass-nav">.*?</nav>'
    nav_match = re.search(nav_pattern, html, re.DOTALL)
    
    # 从Pro生成器获取标准导航
    import sys
    sys.path.insert(0, 'v3')
    from generators.pro_base import ProGenerator
    
    class DummyPro(ProGenerator):
        def _content(self):
            return ''
    
    pro = DummyPro(title='存储芯片产业链深度研究报告', active_page='产业链', show_toc=False)
    pro_html = pro.render()
    
    # 提取Pro版导航
    pro_nav_match = re.search(r'<nav class="fixed top-0 left-0 right-0 z-50 glass-nav">.*?</nav>', pro_html, re.DOTALL)
    if pro_nav_match and nav_match:
        pro_nav = pro_nav_match.group(0)
        html = html.replace(nav_match.group(0), pro_nav)
        print('✅ 导航栏已替换为全站统一版本')
    
    # ========== 2. 替换移动端菜单 ==========
    mobile_pattern = r'<div class="mobile-menu" id="mobileMenu">.*?</div>\s*</div>\s*</div>'
    mobile_match = re.search(mobile_pattern, html, re.DOTALL)
    
    pro_mobile_match = re.search(r'<div class="mobile-menu" id="mobileMenu">.*?</div>\s*</div>\s*</div>', pro_html, re.DOTALL)
    if pro_mobile_match and mobile_match:
        pro_mobile = pro_mobile_match.group(0)
        html = html.replace(mobile_match.group(0), pro_mobile)
        print('✅ 移动端菜单已更新')
    
    # ========== 3. 更新背景样式为深色渐变 ==========
    # 替换body背景
    old_body_bg = r'background: linear-gradient\(135deg, #1e1b4b 0%, #312e81 50%, #4c1d95 100%\);'
    new_body_bg = '''background: linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%);
        min-height: 100vh;
        padding-top: 80px;'''
    
    html = html.replace(old_body_bg, new_body_bg)
    
    # ========== 4. 将白色卡片改为玻璃态效果 ==========
    # 替换glass-card-white样式
    old_glass_card_white = r'''\.glass-card-white \{
            background: rgba\(255, 255, 255, 0\.95\);
            border-radius: 16px;
            box-shadow: 0 20px 60px rgba\(0, 0, 0, 0\.3\);
        \}'''
    
    new_glass_card_white = r'''.glass-card-white {
            background: rgba(255, 255, 255, 0.06);
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 16px;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
        }'''
    
    html = re.sub(old_glass_card_white, new_glass_card_white, html)
    
    # ========== 5. 调整报告内容文字颜色为浅色 ==========
    # 添加深色主题下的文字样式
    dark_text_css = '''
        /* 深色主题文字样式 */
        .report-content h1,
        .report-content h2,
        .report-content h3,
        .report-content h4 {
            color: rgba(255, 255, 255, 0.95) !important;
        }
        
        .report-content p,
        .report-content li {
            color: rgba(255, 255, 255, 0.75) !important;
            line-height: 1.8;
        }
        
        .report-content strong {
            color: #a78bfa !important;
        }
        
        .report-content .text-gray-500,
        .report-content .text-gray-600,
        .report-content .text-gray-700 {
            color: rgba(255, 255, 255, 0.6) !important;
        }
        
        .report-content .text-indigo-600,
        .report-content .text-purple-600,
        .report-content .text-violet-600,
        .report-content .text-fuchsia-600 {
            color: #c4b5fd !important;
        }
        
        .report-content .text-indigo-500,
        .report-content .text-purple-500 {
            color: #a78bfa !important;
        }
        
        .highlight-box {
            background: rgba(139, 92, 246, 0.1) !important;
            border-left: 4px solid #8b5cf6 !important;
            border-radius: 0 8px 8px 0;
        }
        
        .highlight-box p {
            color: rgba(255, 255, 255, 0.85) !important;
            margin-bottom: 0;
        }
        
        .stat-card {
            background: rgba(255, 255, 255, 0.05) !important;
            border: 1px solid rgba(255, 255, 255, 0.1) !important;
            border-radius: 12px;
        }
        
        .tag-badge {
            background: rgba(139, 92, 246, 0.2) !important;
            color: #c4b5fd !important;
        }
        
        .section-divider {
            height: 1px;
            background: linear-gradient(90deg, transparent, rgba(139, 92, 246, 0.5), transparent) !important;
            margin: 40px 0;
        }
        
        .chart-container {
            background: rgba(255, 255, 255, 0.03);
            border-radius: 12px;
            padding: 20px;
            border: 1px solid rgba(255, 255, 255, 0.1);
            margin: 20px 0;
        }
        
        /* 目录导航样式 */
        .toc-nav {
            background: rgba(255, 255, 255, 0.05) !important;
            border: 1px solid rgba(255, 255, 255, 0.1) !important;
        }
        
        .toc-nav a {
            color: rgba(255, 255, 255, 0.7) !important;
        }
        
        .toc-nav a:hover {
            color: #a78bfa !important;
            background: rgba(139, 92, 246, 0.1) !important;
        }
        
        .toc-nav a.active {
            color: #8b5cf6 !important;
            background: rgba(139, 92, 246, 0.15) !important;
            border-left: 3px solid #8b5cf6 !important;
        }
    '''
    
    # 在</style>前插入深色主题样式
    html = html.replace('</style>', dark_text_css + '\n    </style>')
    
    # ========== 6. 添加右侧TOC目录 ==========
    # 先提取所有h2标题
    h2_pattern = r'<h2 id="(section\d+)">(.*?)</h2>'
    h2_matches = re.findall(h2_pattern, html)
    
    if h2_matches:
        toc_items = ''
        for h2_id, h2_title in h2_matches:
            # 去掉序号前缀
            title_text = re.sub(r'^[一二三四五六七八九十]+、', '', h2_title).strip()
            toc_items += f'<a href="#{h2_id}" class="block py-1.5 px-3 text-sm rounded-lg transition-colors" onclick="highlightToc(this)">{title_text}</a>\n'
        
        toc_html = f'''
        <!-- 右侧目录 -->
        <div class="fixed right-4 top-24 w-56 toc-nav p-4 rounded-xl hidden lg:block z-40">
            <div class="text-white/80 font-semibold mb-3 text-sm flex items-center">
                <span class="mr-2">📑</span>目录导航
            </div>
            <div class="space-y-1">
                {toc_items}
            </div>
        </div>
        
        <script>
            // TOC高亮
            function highlightToc(el) {{
                document.querySelectorAll('.toc-nav a').forEach(a => a.classList.remove('active'));
                el.classList.add('active');
            }}
            
            // 滚动时自动高亮
            window.addEventListener('scroll', function() {{
                const sections = document.querySelectorAll('.report-content h2');
                const tocLinks = document.querySelectorAll('.toc-nav a');
                
                let currentSection = '';
                sections.forEach(section => {{
                    const sectionTop = section.offsetTop - 100;
                    if (window.scrollY >= sectionTop) {{
                        currentSection = section.id;
                    }}
                }});
                
                tocLinks.forEach(link => {{
                    link.classList.remove('active');
                    if (link.getAttribute('href') === '#' + currentSection) {{
                        link.classList.add('active');
                    }}
                }});
            }});
        </script>
        '''
        
        # 在内容容器后插入TOC
        # 找到内容主容器
        content_container_pattern = r'(<div class="container mx-auto px-4 py-8 max-w-4xl">)'
        if re.search(content_container_pattern, html):
            html = re.sub(content_container_pattern, toc_html + '\n' + r'\1', html)
            print('✅ 右侧TOC目录已添加')
    
    # ========== 7. 调整整体布局 ==========
    # 给主内容区域添加右边距，为TOC留出空间
    container_pattern = r'max-w-4xl'
    html = re.sub(container_pattern, 'max-w-4xl lg:mr-64', html)
    
    # 保存
    output_path = 'docs/industry_chain/20260619_存储芯片产业链深度研究报告.html'
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
    
    file_size = os.path.getsize(output_path)
    print(f'✅ 升级完成！保存到: {output_path} ({file_size} 字节)')
    print(f'   保留 {len(h2_matches)} 个章节 + 所有图表 + 完整分析内容')
    print(f'   新增：全站统一导航栏(11个入口) + 深色玻璃态风格 + 右侧TOC目录')

if __name__ == '__main__':
    upgrade_storage_report()
