#!/usr/bin/env python3
"""
Markdown报告转HTML模板脚本
将产业链深度研究报告的Markdown转换成带网站统一样式的HTML
"""
import re
import sys

def markdown_to_html(md_content):
    """简单的Markdown转HTML转换"""
    html = md_content
    
    # 标题转换
    html = re.sub(r'^# (.*?)$', r'<h1 class="text-4xl font-bold text-white mb-4">\1</h1>', html, flags=re.MULTILINE)
    html = re.sub(r'^## (.*?)$', r'<h2 class="text-2xl font-bold text-dark mt-8 mb-4 pb-2 border-b-2 border-primary">\1</h2>', html, flags=re.MULTILINE)
    html = re.sub(r'^### (.*?)$', r'<h3 class="text-xl font-semibold text-dark mt-6 mb-3">\1</h3>', html, flags=re.MULTILINE)
    html = re.sub(r'^#### (.*?)$', r'<h4 class="text-lg font-medium text-dark mt-4 mb-2">\1</h4>', html, flags=re.MULTILINE)
    
    # 段落转换
    html = re.sub(r'^(?!<[hu])(.*\S.*)$', r'<p class="text-gray-700 mb-4 leading-relaxed">\1</p>', html, flags=re.MULTILINE)
    
    # 粗体转换
    html = re.sub(r'\*\*(.*?)\*\*', r'<strong class="font-bold">\1</strong>', html)
    
    # 表格转换（简单处理
    html = re.sub(r'\| (.*?) \|', r'<td class="border border-gray-300 px-4 py-2">\1</td>', html)
    
    # 列表转换
    html = re.sub(r'^- (.*?)$', r'<li class="text-gray-700 mb-2">\1</li>', html, flags=re.MULTILINE)
    
    # 分隔线
    html = re.sub(r'^---$', r'<hr class="my-8 border-gray-300">', html, flags=re.MULTILINE)
    
    return html

def main():
    if len(sys.argv) < 3:
        print("用法: python convert_md_to_html.py <输入md文件> <输出html文件>")
        sys.exit(1)
    
    md_file = sys.argv[1]
    html_file = sys.argv[2]
    
    # 读取Markdown
    with open(md_file, 'r', encoding='utf-8') as f:
        md_content = f.read()
    
    # 转换内容
    content_html = markdown_to_html(md_content)
    
    # HTML模板（从现有报告提取的头部和尾部
    template_head = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>英伟达N1X芯片与COMPUTEX深度研究报告</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.5.1/css/all.min.css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.5.1/css/v4-shims.min.css">
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        primary: '#6366f1',
                        secondary: '#8b5cf6',
                        accent: '#f59e0b',
                        dark: '#1f2937',
                    },
                }
            }
        }
    </script>
    <style type="text/tailwindcss">
        @layer utilities {
            .content-auto {
                content-visibility: auto;
            }
            .glass-nav {
                background: rgba(255, 255, 255, 0.1);
                backdrop-filter: blur(10px);
                -webkit-backdrop-filter: blur(10px);
            }
            .card-glass {
                background: rgba(255, 255, 255, 0.95);
                backdrop-filter: blur(10px);
            }
            .gradient-text {
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                background-clip: text;
            }
        }
    </style>
    <style>
        body {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
        }
        .new-badge {
            background: linear-gradient(135deg, #ff6b6b 0%, #ee5a24 100%);
            animation: pulse 2s ease-in-out infinite;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin-bottom: 1rem;
        }
        th {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 12px 16px;
            text-align: left;
        }
        td {
            border: 1px solid #e5e7eb;
            padding: 12px 16px;
        }
        tr:nth-child(even) {
            background-color: #f9fafb;
        }
    </style>
</head>
<body class="pb-20">
    <!-- 导航栏 -->
    <nav class="glass-nav fixed top-0 left-0 right-0 z-50">
        <div class="max-w-4xl mx-auto px-4 py-4 flex items-center justify-between">
            <div class="flex items-center space-x-3">
                <i class="fa fa-link text-white text-2xl pulse-icon"></i>
                <span class="text-white font-bold text-xl">🎮 英伟达N1X芯片深度研究</span>
            </div>
            <div class="flex items-center space-x-2 flex-wrap gap-2">
                <a href="../index.html" class="text-white/80 hover:text-white text-sm transition-colors px-2 py-1 rounded hover:bg-white/10">
                    <i class="fa fa-home mr-1"></i>首页
                </a>
                <a href="latest.html" class="text-white font-medium bg-white/20 text-sm transition-colors px-2 py-1 rounded">
                    <i class="fa fa-book mr-1"></i>产业链
                </a>
            </div>
        </div>
    </nav>

    <!-- 主内容区 -->
    <div class="max-w-4xl mx-auto px-4 pt-24">
        <!-- 页面标题 -->
        <div class="text-center mb-8">
            <h1 class="text-3xl font-black text-white mb-2">
                <i class="fa fa-microchip mr-2"></i>英伟达N1X芯片与COMPUTEX 2026
            </h1>
            <p class="text-white/80">Arm架构PC处理器 + Vera Rubin算力平台深度分析</p>
            <p class="text-white/60 text-sm mt-2">发布日期：2026年5月30日</p>
        </div>

        <!-- 报告内容容器 -->
        <div class="card-glass rounded-3xl p-8 shadow-2xl">
"""

    template_tail = """
        </div>
    </div>

    <!-- 页脚 -->
    <footer class="fixed bottom-0 left-0 right-0 glass-nav py-4">
        <div class="max-w-4xl mx-auto px-4 text-center">
            <p class="text-white/70 text-sm">数据来源：摩根士丹利研报、英伟达官方信息、产业链调研</p>
        </div>
    </footer>
</body>
</html>
"""
    
    # 组合完整HTML
    full_html = template_head + content_html + template_tail
    
    # 写入文件
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(full_html)
    
    print(f"转换完成: {html_file}")

if __name__ == "__main__":
    main()