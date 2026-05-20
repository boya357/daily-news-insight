#!/usr/bin/env python3
"""MD转HTML脚本 - 沉浸光影风格"""

import sys
import os

def md_to_html(md_path, html_path):
    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 简单MD解析
    html_content = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>盘中快报</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'PingFang SC', 'Microsoft YaHei', sans-serif;
            background: linear-gradient(135deg, #0a0a0a 0%, #1a1a2e 50%, #16213e 100%);
            min-height: 100vh;
            color: #e0e0e0;
            line-height: 1.8;
        }}
        .container {{
            max-width: 900px;
            margin: 0 auto;
            padding: 40px 20px;
        }}
        .header {{
            text-align: center;
            padding: 40px 0;
            border-bottom: 1px solid rgba(255,255,255,0.1);
            margin-bottom: 40px;
        }}
        .header h1 {{
            font-size: 2.2em;
            background: linear-gradient(90deg, #00d4ff, #7b2cbf);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 10px;
        }}
        .header .subtitle {{
            color: #888;
            font-size: 1.1em;
        }}
        .content {{
            background: rgba(255,255,255,0.03);
            border-radius: 16px;
            padding: 40px;
            border: 1px solid rgba(255,255,255,0.08);
            backdrop-filter: blur(10px);
        }}
        h2 {{
            color: #00d4ff;
            font-size: 1.4em;
            margin: 30px 0 15px 0;
            padding-left: 15px;
            border-left: 3px solid #00d4ff;
        }}
        h3 {{
            color: #7b2cbf;
            font-size: 1.2em;
            margin: 20px 0 10px 0;
        }}
        p {{
            margin: 10px 0;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 15px 0;
        }}
        th, td {{
            padding: 12px 15px;
            text-align: left;
            border-bottom: 1px solid rgba(255,255,255,0.1);
        }}
        th {{
            background: rgba(0,212,255,0.1);
            color: #00d4ff;
        }}
        tr:hover {{
            background: rgba(255,255,255,0.03);
        }}
        .up {{ color: #ff4757; }}
        .down {{ color: #2ed573; }}
        .highlight {{
            background: rgba(0,212,255,0.1);
            padding: 15px 20px;
            border-radius: 8px;
            margin: 15px 0;
        }}
        ul, ol {{
            margin: 10px 0 10px 25px;
        }}
        li {{
            margin: 5px 0;
        }}
        blockquote {{
            border-left: 4px solid #7b2cbf;
            padding: 10px 20px;
            margin: 15px 0;
            background: rgba(123,44,191,0.1);
            border-radius: 0 8px 8px 0;
        }}
        hr {{
            border: none;
            border-top: 1px solid rgba(255,255,255,0.1);
            margin: 30px 0;
        }}
        .footer {{
            text-align: center;
            margin-top: 40px;
            padding-top: 20px;
            border-top: 1px solid rgba(255,255,255,0.1);
            color: #666;
            font-size: 0.9em;
        }}
        a {{
            color: #00d4ff;
            text-decoration: none;
        }}
        a:hover {{
            text-decoration: underline;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>📊 盘中快报</h1>
            <div class="subtitle">2026年5月20日 12:30 | 市场弱势震荡，科创50逆势创新高</div>
        </div>
        <div class="content">
"""
    
    # 解析Markdown并转换
    import re
    lines = content.split('\n')
    in_table = False
    table_rows = []
    
    for line in lines:
        line = line.strip()
        if not line:
            html_content += '<br>'
            continue
        
        # 标题
        if line.startswith('# '):
            html_content += f'<h1 style="font-size:1.8em;margin:20px 0;">{line[2:]}</h1>'
        elif line.startswith('## '):
            html_content += f'<h2>{line[3:]}</h2>'
        elif line.startswith('### '):
            html_content += f'<h3>{line[4:]}</h3>'
        # 分隔线
        elif line.startswith('---'):
            html_content += '<hr>'
        # 引用
        elif line.startswith('>'):
            html_content += f'<blockquote>{line[1:].strip()}</blockquote>'
        # 表格
        elif line.startswith('|'):
            cells = [c.strip() for c in line.split('|')[1:-1]]
            if all(c.replace('-','') == '' for c in cells):
                continue  # 分隔行
            if '---' not in line:
                if '指数' in cells[0] or '项目' in cells[0]:
                    html_content += '<table><thead><tr>'
                    for c in cells:
                        html_content += f'<th>{c}</th>'
                    html_content += '</tr></thead><tbody>'
                else:
                    html_content += '<tr>'
                    for c in cells:
                        # 高亮数字
                        c = re.sub(r'([+\-])[\d.]+%', r'<span class="up">\1</span>', c)
                        html_content += f'<td>{c}</td>'
                    html_content += '</tr>'
        # 无序列表
        elif line.startswith('- ') or line.startswith('* '):
            html_content += f'<li>{line[2:]}</li>'
        # 其他段落
        else:
            html_content += f'<p>{line}</p>'
    
    html_content += """
        </div>
        <div class="footer">
            <p>数据来源：Wind/东方财富/同花顺（仅供参考，不构成投资建议）</p>
            <p style="margin-top:10px;"><a href="https://boya357.github.io/daily-news-insight/">← 返回首页</a></p>
        </div>
    </div>
</body>
</html>"""
    
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"HTML已生成: {html_path}")

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("用法: python3 md_to_html.py <md_path> <html_path>")
        sys.exit(1)
    md_to_html(sys.argv[1], sys.argv[2])
