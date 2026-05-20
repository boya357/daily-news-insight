#!/usr/bin/env python3
"""将MD文件转换为带沉浸光影风格HTML"""

import os
import re
import shutil
from datetime import datetime

# MD转HTML的基础转换函数
def md_to_html_basic(md_content):
    """简单的MD到HTML转换"""
    html = md_content
    
    # 标题转换
    html = re.sub(r'^# (.*)$', r'<h1>\1</h1>', html, flags=re.MULTILINE)
    html = re.sub(r'^## (.*)$', r'<h2>\1</h2>', html, flags=re.MULTILINE)
    html = re.sub(r'^### (.*)$', r'<h3>\1</h3>', html, flags=re.MULTILINE)
    html = re.sub(r'^#### (.*)$', r'<h4>\1</h4>', html, flags=re.MULTILINE)
    
    # 表格转换
    table_pattern = re.compile(r'\|(.+)\|\n\|[-:\s|]+\|\n((?:\|.+\|\n?)+)', re.MULTILINE)
    
    def convert_table(match):
        header = match.group(1)
        rows = match.group(2).strip().split('\n')
        
        header_html = '<tr>' + ''.join(f'<th>{cell.strip()}</th>' for cell in header.split('|') if cell.strip()) + '</tr>'
        rows_html = ''
        for row in rows:
            if row.strip():
                rows_html += '<tr>' + ''.join(f'<td>{cell.strip()}</td>' for cell in row.split('|') if cell.strip()) + '</tr>'
        
        return f'<table class="data-table"><thead>{header_html}</thead><tbody>{rows_html}</tbody></table>'
    
    html = table_pattern.sub(convert_table, html)
    
    # 列表转换
    ul_pattern = re.compile(r'((?:^[+-] .+\n?)+)', re.MULTILINE)
    def convert_ul(match):
        items = re.findall(r'^[+-] (.*)$', match.group(1), re.MULTILINE)
        return '<ul class="item-list">' + ''.join(f'<li>{item.strip()}</li>' for item in items) + '</ul>'
    html = ul_pattern.sub(convert_ul, html)
    
    # 有序列表
    ol_pattern = re.compile(r'((?:^\d+\. .+\n?)+)', re.MULTILINE)
    def convert_ol(match):
        items = re.findall(r'^\d+\. (.*)$', match.group(1), re.MULTILINE)
        return '<ol class="item-list numbered">' + ''.join(f'<li>{item.strip()}</li>' for item in items) + '</ol>'
    html = ol_pattern.sub(convert_ol, html)
    
    # 分隔线
    html = re.sub(r'^---$', '<hr>', html, flags=re.MULTILINE)
    html = re.sub(r'^\*\*\*$', '<hr class="bold">', html, flags=re.MULTILINE)
    
    # 引用块
    blockquote_pattern = re.compile(r'^> (.*)$', re.MULTILINE)
    def convert_blockquote(match):
        content = match.group(1)
        if content.startswith('⚠️') or content.startswith('⚠'):
            return f'<div class="alert alert-warning"><span class="alert-icon">⚠️</span><span class="alert-text">{content}</span></div>'
        elif content.startswith('📌') or content.startswith('🔥'):
            return f'<div class="alert alert-info"><span class="alert-icon">📌</span><span class="alert-text">{content}</span></div>'
        return f'<blockquote>{content}</blockquote>'
    html = blockquote_pattern.sub(convert_blockquote, html)
    
    # 加粗和斜体
    html = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', html)
    html = re.sub(r'\*(.+?)\*', r'<em>\1</em>', html)
    
    # 行内代码
    html = re.sub(r'`(.+?)`', r'<code>\1</code>', html)
    
    # 换行处理 - 将双换行转为段落
    paragraphs = html.split('\n\n')
    result = []
    for p in paragraphs:
        p = p.strip()
        if not p:
            continue
        if p.startswith('<h') or p.startswith('<ul') or p.startswith('<ol') or p.startswith('<table') or p.startswith('<blockquote') or p.startswith('<div') or p.startswith('<hr'):
            result.append(p)
        else:
            # 处理段落内的换行
            lines = p.split('\n')
            if len(lines) > 1:
                result.append('<p>' + '<br>'.join(lines) + '</p>')
            else:
                result.append(f'<p>{p}</p>')
    
    return '\n'.join(result)


def generate_html(title, content_html, nav_type='daily'):
    """生成完整HTML页面"""
    
    # 根据类型确定当前导航项
    nav_items = [
        ('首页', '/daily-news-insight/'),
        ('每日洞察', '/daily-news-insight/daily/latest.html'),
        ('盘中快报', '/daily-news-insight/intraday/latest.html'),
        ('盘后速递', '/daily-news-insight/aftermarket/latest.html'),
        ('产业链', '/daily-news-insight/industry_chain/latest.html'),
        ('前瞻催化', '/daily-news-insight/weekly_review/latest.html'),
    ]
    
    current_map = {
        'daily': '每日洞察',
        'intraday': '盘中快报',
        'aftermarket': '盘后速递',
        'industry_chain': '产业链',
        'weekly_review': '前瞻催化',
    }
    
    current_nav = current_map.get(nav_type, '首页')
    
    nav_html = ''
    for name, href in nav_items:
        if name == current_nav:
            nav_html += f'<a href="{href}" class="nav-item current">{name}</a>\n            '
        else:
            nav_html += f'<a href="{href}" class="nav-item">{name}</a>\n            '
    
    today = datetime.now()
    week_days = ['周日', '周一', '周二', '周三', '周四', '周五', '周六']
    date_str = f"{today.month}月{today.day}日 {week_days[today.weekday()]}"
    
    html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; -webkit-tap-highlight-color: transparent; }}
        html, body {{ height: 100%; }}
        body {{ 
            font-family: -apple-system, BlinkMacSystemFont, "PingFang SC", "Microsoft YaHei", sans-serif; 
            background: linear-gradient(135deg, #f8fafc 0%, #eef1f8 50%, #f0f4ff 100%);
            color: #334155; 
            line-height: 1.7; 
            min-height: 100vh;
        }}
        
        /* 沉浸光影效果 */
        body::before {{
            content: '';
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            height: 400px;
            background: linear-gradient(180deg, 
                rgba(99, 102, 241, 0.08) 0%, 
                rgba(139, 92, 246, 0.05) 40%,
                transparent 100%);
            pointer-events: none;
            z-index: 0;
        }}
        
        body::after {{
            content: '';
            position: fixed;
            bottom: 0;
            right: 0;
            width: 600px;
            height: 600px;
            background: radial-gradient(circle at center, 
                rgba(34, 197, 94, 0.06) 0%, 
                rgba(16, 185, 129, 0.03) 40%,
                transparent 70%);
            pointer-events: none;
            z-index: 0;
        }}
        
        .header {{
            position: sticky; 
            top: 0; 
            background: rgba(255,255,255,0.92);
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            border-bottom: 1px solid rgba(99, 102, 241, 0.1);
            z-index: 100; 
            padding: 0 24px;
            box-shadow: 0 4px 20px rgba(99, 102, 241, 0.08);
        }}
        
        .header-inner {{ 
            max-width: 900px; 
            margin: 0 auto; 
            display: flex; 
            align-items: center; 
            justify-content: space-between; 
            height: 56px; 
        }}
        
        .header-title {{ 
            font-size: 17px; 
            font-weight: 700; 
            background: linear-gradient(135deg, #6366f1, #8b5cf6);
            -webkit-background-clip: text; 
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }}
        
        .header-date {{ font-size: 13px; color: #94a3b8; }}
        
        .nav-bar {{ 
            background: white; 
            border-radius: 16px; 
            padding: 12px 16px; 
            margin: 16px 20px; 
            box-shadow: 0 4px 20px rgba(99, 102, 241, 0.08);
            display: flex; 
            justify-content: center; 
            flex-wrap: wrap; 
            gap: 6px;
            position: relative;
            z-index: 1;
        }}
        
        .nav-item {{ 
            padding: 8px 14px; 
            border-radius: 20px; 
            text-decoration: none; 
            font-size: 13px; 
            font-weight: 500; 
            transition: all 0.25s ease;
        }}
        
        .nav-item:not(.current) {{ 
            background: #f5f7fa; 
            color: #64748b; 
        }}
        
        .nav-item:not(.current):hover {{ 
            background: linear-gradient(135deg, #6366f1, #8b5cf6);
            color: white;
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(99, 102, 241, 0.3);
        }}
        
        .nav-item.current {{ 
            background: linear-gradient(135deg, #6366f1, #8b5cf6); 
            color: white;
            box-shadow: 0 4px 15px rgba(99, 102, 241, 0.35);
        }}
        
        .container {{ 
            max-width: 900px; 
            margin: 0 auto; 
            padding: 0 20px 60px;
            position: relative;
            z-index: 1;
        }}
        
        .report-header {{
            text-align: center;
            margin-bottom: 32px;
            padding: 40px 20px;
            position: relative;
        }}
        
        .report-header::before {{
            content: '';
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            width: 120px;
            height: 120px;
            background: linear-gradient(135deg, rgba(99, 102, 241, 0.1), rgba(139, 92, 246, 0.1));
            border-radius: 50%;
            filter: blur(40px);
            z-index: -1;
        }}
        
        .report-icon {{
            font-size: 48px;
            margin-bottom: 16px;
            display: inline-block;
            animation: float 3s ease-in-out infinite;
        }}
        
        @keyframes float {{
            0%, 100% {{ transform: translateY(0); }}
            50% {{ transform: translateY(-8px); }}
        }}
        
        .report-title {{
            font-size: 28px;
            font-weight: 800;
            background: linear-gradient(135deg, #1e293b 0%, #475569 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 8px;
        }}
        
        .report-meta {{
            font-size: 14px;
            color: #64748b;
        }}
        
        /* 内容样式 */
        .content {{
            background: white;
            border-radius: 20px;
            padding: 32px;
            box-shadow: 0 4px 24px rgba(99, 102, 241, 0.08);
            border: 1px solid rgba(99, 102, 241, 0.06);
        }}
        
        h1 {{
            font-size: 24px;
            font-weight: 700;
            color: #1e293b;
            margin: 24px 0 16px;
            padding-bottom: 12px;
            border-bottom: 2px solid #6366f1;
        }}
        
        h1:first-child {{
            margin-top: 0;
        }}
        
        h2 {{
            font-size: 20px;
            font-weight: 700;
            color: #1e293b;
            margin: 28px 0 14px;
            padding-bottom: 8px;
            border-bottom: 1px solid #e2e8f0;
            display: flex;
            align-items: center;
            gap: 8px;
        }}
        
        h2::before {{
            content: '';
            width: 4px;
            height: 20px;
            background: linear-gradient(180deg, #6366f1, #8b5cf6);
            border-radius: 2px;
        }}
        
        h3 {{
            font-size: 17px;
            font-weight: 600;
            color: #334155;
            margin: 20px 0 12px;
        }}
        
        h4 {{
            font-size: 15px;
            font-weight: 600;
            color: #475569;
            margin: 16px 0 10px;
        }}
        
        p {{
            margin: 12px 0;
            color: #475569;
        }}
        
        /* 表格样式 */
        .data-table {{
            width: 100%;
            border-collapse: collapse;
            margin: 16px 0;
            font-size: 14px;
            border-radius: 12px;
            overflow: hidden;
            box-shadow: 0 2px 8px rgba(0,0,0,0.04);
        }}
        
        .data-table th {{
            background: linear-gradient(135deg, #6366f1, #8b5cf6);
            color: white;
            padding: 14px 12px;
            text-align: left;
            font-weight: 600;
        }}
        
        .data-table td {{
            padding: 12px;
            border-bottom: 1px solid #f1f5f9;
        }}
        
        .data-table tr:nth-child(even) td {{
            background: #fafbff;
        }}
        
        .data-table tr:hover td {{
            background: #f0f4ff;
        }}
        
        /* 列表样式 */
        .item-list {{
            margin: 12px 0;
            padding-left: 20px;
        }}
        
        .item-list li {{
            margin: 8px 0;
            color: #475569;
            position: relative;
        }}
        
        .item-list li::marker {{
            color: #6366f1;
        }}
        
        .item-list.numbered li::marker {{
            color: #6366f1;
            font-weight: 600;
        }}
        
        /* 引用/提示框 */
        blockquote {{
            background: linear-gradient(135deg, #f8faff, #f0f4ff);
            border-left: 4px solid #6366f1;
            padding: 16px 20px;
            margin: 16px 0;
            border-radius: 0 12px 12px 0;
        }}
        
        .alert {{
            padding: 16px 20px;
            margin: 16px 0;
            border-radius: 12px;
            display: flex;
            align-items: flex-start;
            gap: 12px;
        }}
        
        .alert-warning {{
            background: linear-gradient(135deg, #fff7ed, #ffedd5);
            border: 1px solid #fb923c;
        }}
        
        .alert-warning .alert-icon {{
            font-size: 20px;
        }}
        
        .alert-warning .alert-text {{
            color: #c2410c;
        }}
        
        .alert-info {{
            background: linear-gradient(135deg, #f0f9ff, #e0f2fe);
            border: 1px solid #38bdf8;
        }}
        
        .alert-icon {{ font-size: 20px; }}
        
        .alert-text {{
            flex: 1;
            color: #334155;
        }}
        
        strong {{ color: #1e293b; font-weight: 600; }}
        
        code {{
            background: #f1f5f9;
            padding: 2px 6px;
            border-radius: 4px;
            font-family: 'SF Mono', Consolas, monospace;
            font-size: 13px;
            color: #6366f1;
        }}
        
        hr {{
            border: none;
            height: 1px;
            background: linear-gradient(90deg, transparent, #e2e8f0, transparent);
            margin: 24px 0;
        }}
        
        hr.bold {{
            height: 3px;
            background: linear-gradient(90deg, transparent, #6366f1, transparent);
        }}
        
        /* 风险提示 */
        .disclaimer {{
            margin-top: 32px;
            padding: 20px;
            background: linear-gradient(135deg, #fef3c7, #fde68a);
            border-radius: 12px;
            border-left: 4px solid #f59e0b;
        }}
        
        .disclaimer-title {{
            font-weight: 700;
            color: #92400e;
            margin-bottom: 8px;
            display: flex;
            align-items: center;
            gap: 8px;
        }}
        
        .disclaimer-text {{
            font-size: 13px;
            color: #a16207;
        }}
        
        footer {{
            text-align: center; 
            padding: 40px 20px; 
            color: #94a3b8; 
            font-size: 12px;
        }}
        
        .back-link {{
            display: inline-flex;
            align-items: center;
            padding: 10px 20px;
            background: white;
            border-radius: 20px;
            text-decoration: none;
            color: #6366f1;
            font-weight: 500;
            margin-top: 24px;
            transition: all 0.25s ease;
            box-shadow: 0 2px 8px rgba(99, 102, 241, 0.1);
        }}
        
        .back-link:hover {{
            transform: translateX(-4px);
            box-shadow: 0 4px 12px rgba(99, 102, 241, 0.2);
        }}
        
        /* 响应式 */
        @media (max-width: 640px) {{
            .container {{ padding: 0 12px 40px; }}
            .content {{ padding: 20px; border-radius: 16px; }}
            .report-title {{ font-size: 22px; }}
            h1 {{ font-size: 20px; }}
            h2 {{ font-size: 17px; }}
            .data-table {{ font-size: 12px; }}
            .data-table th, .data-table td {{ padding: 10px 8px; }}
        }}
    </style>
</head>
<body>
    <header class="header">
        <div class="header-inner">
            <a href="/daily-news-insight/" style="text-decoration: none;">
                <span class="header-title">📊 市场洞察中心</span>
            </a>
            <span class="header-date">{date_str}</span>
        </div>
    </header>

    <div class="nav-bar">
        {nav_html}
    </div>

    <div class="container">
        <div class="report-header">
            <div class="report-icon">📰</div>
            <h1 class="report-title">{title}</h1>
            <p class="report-meta">数据来源：公开市场信息整理</p>
        </div>
        
        <div class="content">
            {content_html}
        </div>
        
        <footer>
            <p>⚠️ 仅供参考，不构成投资建议</p>
            <a href="/daily-news-insight/" class="back-link">← 返回首页</a>
        </footer>
    </div>
</body>
</html>'''
    return html


def convert_md_to_html(md_path, html_path, nav_type='daily'):
    """转换单个MD文件到HTML"""
    print(f"Converting: {md_path} -> {html_path}")
    
    # 读取MD文件
    with open(md_path, 'r', encoding='utf-8') as f:
        md_content = f.read()
    
    # 提取标题（从第一行h1或标题）
    title_match = re.search(r'^# (.*)$', md_content, re.MULTILINE)
    if title_match:
        title = title_match.group(1).strip()
    else:
        title = os.path.basename(md_path).replace('.md', '')
    
    # 转换为HTML内容
    content_html = md_to_html_basic(md_content)
    
    # 生成完整HTML
    full_html = generate_html(title, content_html, nav_type)
    
    # 确保目录存在
    os.makedirs(os.path.dirname(html_path), exist_ok=True)
    
    # 写入HTML文件
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(full_html)
    
    print(f"  ✓ Done: {html_path}")
    return True


def main():
    base_dir = '/app/data/所有对话/主对话/docs'
    
    # 定义转换任务
    conversions = [
        # (源MD路径, 目标HTML路径, 导航类型)
        (f'{base_dir}/daily/20260515.md', f'{base_dir}/daily/20260515.html', 'daily'),
        (f'{base_dir}/intraday/20260507.md', f'{base_dir}/intraday/20260507.html', 'intraday'),
        (f'{base_dir}/intraday/20260510.md', f'{base_dir}/intraday/20260510.html', 'intraday'),
        (f'{base_dir}/intraday/20260513.md', f'{base_dir}/intraday/20260513.html', 'intraday'),
        (f'{base_dir}/aftermarket/2026-05-18_盘后速递.md', f'{base_dir}/aftermarket/2026-05-18.html', 'aftermarket'),
    ]
    
    for md_path, html_path, nav_type in conversions:
        if os.path.exists(md_path):
            convert_md_to_html(md_path, html_path, nav_type)
        else:
            print(f"  ✗ File not found: {md_path}")
    
    print("\nAll conversions completed!")
    
    # 同步到git目录
    git_dir = os.path.expanduser('~/daily-news-insight-git')
    if os.path.exists(git_dir):
        print(f"\nSyncing to {git_dir}...")
        for md_path, html_path, _ in conversions:
            if os.path.exists(html_path):
                target_path = html_path.replace(base_dir, git_dir)
                os.makedirs(os.path.dirname(target_path), exist_ok=True)
                shutil.copy2(html_path, target_path)
                print(f"  ✓ Synced: {target_path}")
    else:
        print(f"\n⚠️ Git directory not found: {git_dir}")
        print("   Skipping sync. Please ensure the directory exists.")


if __name__ == '__main__':
    main()
