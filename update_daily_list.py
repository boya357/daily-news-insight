#!/usr/bin/env python3
"""
每日新闻洞察列表页面更新脚本
彻底解决latest.html被覆盖成重定向页面的问题

使用方法：
    python update_daily_list.py [--date YYYY-MM-DD]

功能：
    1. 扫描docs/daily/目录下所有报告
    2. 按日期倒序排列，生成完整的历史报告列表页面
    3. 写入docs/daily/latest.html（列表页面，不是重定向！）
"""

import os
import re
import glob
from datetime import datetime

def extract_report_info(html_path):
    """从HTML文件中提取报告信息"""
    try:
        with open(html_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 提取标题
        title_match = re.search(r'<title>(.+?)</title>', content)
        title = title_match.group(1) if title_match else os.path.basename(html_path).replace('.html', '')
        
        # 提取日期（从文件名或内容中）
        date_match = re.search(r'(\d{4})年(\d{1,2})月(\d{1,2})日', title)
        if not date_match:
            # 尝试从文件名提取
            file_match = re.search(r'(\d{4})(\d{2})(\d{2})', os.path.basename(html_path))
            if file_match:
                y, m, d = file_match.groups()
                date_str = f"{y}年{m}月{d}日"
            else:
                date_str = "未知日期"
        else:
            date_str = f"{date_match.group(1)}年{date_match.group(2)}月{date_match.group(3)}日"
        
        # 提取副标题（从h1或其他位置）
        subtitle = "市场分析与操作策略"
        
        return {
            'filename': os.path.basename(html_path),
            'title': title,
            'date': date_str,
            'subtitle': subtitle,
            'path': html_path
        }
    except Exception as e:
        print(f"⚠️  解析文件失败 {html_path}: {e}")
        return None

def generate_list_page(reports):
    """生成列表页面HTML"""
    
    # 按日期排序（最新的在前面）
    reports.sort(key=lambda x: x['filename'], reverse=True)
    
    # 生成报告卡片HTML
    cards_html = ""
    for i, report in enumerate(reports):
        tag_html = '<span class="card-tag">今日</span>' if i == 0 else ''
        icon = '🆕' if i == 0 else '📅'
        
        card_html = f'''
        <a href="/daily-news-insight/daily/{report['filename']}" class="card">
            <div class="card-icon">{icon}</div>
            <div class="card-content">
                <div class="card-title">{report['title']}</div>
                <div class="card-subtitle">{report['subtitle']}</div>
            </div>
            {tag_html}
            <span class="card-arrow">›</span>
        </a>'''
        cards_html += card_html
    
    html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>每日新闻洞察</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; -webkit-tap-highlight-color: transparent; }}
        html, body {{ height: 100%; }}
        body {{ font-family: -apple-system, BlinkMacSystemFont, 'PingFang SC', sans-serif; background: #f8fafc; color: #334155; line-height: 1.6; min-height: 100vh; }}
        .header {{ position: sticky; top: 0; background: rgba(255,255,255,0.95); backdrop-filter: blur(20px); border-bottom: 1px solid rgba(0,0,0,0.06); z-index: 100; padding: 0 24px; }}
        .header-inner {{ max-width: 600px; margin: 0 auto; display: flex; align-items: center; justify-content: space-between; height: 56px; }}
        .header-title {{ font-size: 17px; font-weight: 700; background: linear-gradient(135deg, #6366f1, #8b5cf6); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }}
        .header-date {{ font-size: 13px; color: #94a3b8; }}
        .nav-bar {{ background: white; border-radius: 16px; padding: 12px 16px; margin: 16px 20px; box-shadow: 0 1px 3px rgba(0,0,0,0.04); display: flex; justify-content: center; flex-wrap: wrap; gap: 6px; }}
        .nav-item {{ padding: 8px 14px; border-radius: 20px; text-decoration: none; font-size: 13px; font-weight: 500; transition: all 0.2s; }}
        .nav-item:not(.current) {{ background: #f5f7fa; color: #64748b; }}
        .nav-item:not(.current):hover {{ background: #6366f1; color: white; }}
        .nav-item.current {{ background: linear-gradient(135deg, #6366f1, #8b5cf6); color: white; }}
        .container {{ max-width: 600px; margin: 0 auto; padding: 0 20px 100px; }}
        .page-title {{ font-size: 24px; font-weight: 700; margin-bottom: 8px; color: #1e293b; }}
        .page-subtitle {{ font-size: 14px; color: #64748b; margin-bottom: 24px; }}
        .card {{ display: flex; align-items: center; gap: 14px; padding: 16px 18px; background: #fff; border: 1px solid rgba(0,0,0,0.06); border-radius: 16px; text-decoration: none; color: inherit; transition: all 0.2s; box-shadow: 0 1px 3px rgba(0,0,0,0.04); margin-bottom: 12px; }}
        .card:hover {{ border-color: #6366f1; box-shadow: 0 4px 12px rgba(99,102,241,0.12); transform: translateY(-1px); }}
        .card-icon {{ width: 48px; height: 48px; border-radius: 14px; display: flex; align-items: center; justify-content: center; font-size: 22px; flex-shrink: 0; background: linear-gradient(135deg, #6366f1, #8b5cf6); }}
        .card-content {{ flex: 1; }}
        .card-title {{ font-size: 16px; font-weight: 600; color: #1e293b; margin-bottom: 2px; }}
        .card-subtitle {{ font-size: 13px; color: #94a3b8; }}
        .card-tag {{ padding: 4px 10px; border-radius: 6px; font-size: 11px; font-weight: 600; background: rgba(99,102,241,0.1); color: #6366f1; }}
        .card-arrow {{ color: #cbd5e1; font-size: 20px; font-weight: 300; }}
        footer {{ text-align: center; padding: 40px 20px; color: #94a3b8; font-size: 12px; }}
    </style>
</head>
<body>
    <header class="header">
        <div class="header-inner">
            <a href="/daily-news-insight/" style="text-decoration: none;">
                <span class="header-title">📊 市场洞察中心</span>
            </a>
            <span class="header-date" id="today"></span>
        </div>
    </header>
    <div class="nav-bar">
        <a href="/daily-news-insight/" class="nav-item">首页</a>
        <a href="/daily-news-insight/daily/latest.html" class="nav-item current">每日新闻洞察</a>
        <a href="/daily-news-insight/intraday/latest.html" class="nav-item">盘中快报</a>
        <a href="/daily-news-insight/aftermarket/latest.html" class="nav-item">盘后速递</a>
        <a href="/daily-news-insight/industry_chain/latest.html" class="nav-item">产业链</a>
        <a href="/daily-news-insight/催化日历/latest.html" class="nav-item">催化日历</a>
    </div>
    <div class="container">
        <h1 class="page-title">📰 每日新闻洞察</h1>
        <p class="page-subtitle">隔夜新闻与当日操作策略</p>
        {cards_html}
    </div>
    
    <footer>
        <p>仅供参考，不构成投资建议</p>
    </footer>
    
    <script>
        const now = new Date();
        const weekDay = ['周日','周一','周二','周三','周四','周五','周六'][now.getDay()];
        document.getElementById('today').textContent = `${{now.getMonth()+1}}月${{now.getDate()}}日 ${{weekDay}}`;
    </script>
</body>
</html>'''
    
    return html

def main():
    base_dir = '/app/data/所有对话/主对话/docs/daily'
    
    # 扫描所有HTML报告文件
    html_files = glob.glob(os.path.join(base_dir, '*_每日新闻洞察.html'))
    
    if not html_files:
        print("⚠️  未找到任何报告文件")
        return
    
    print(f"✅ 找到 {len(html_files)} 个报告文件")
    
    # 提取报告信息
    reports = []
    for html_file in html_files:
        info = extract_report_info(html_file)
        if info:
            reports.append(info)
    
    # 生成列表页面
    list_html = generate_list_page(reports)
    
    # 写入latest.html
    output_path = os.path.join(base_dir, 'latest.html')
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(list_html)
    
    print(f"✅ 已生成列表页面: {output_path}")
    print(f"✅ 包含 {len(reports)} 个历史报告")

if __name__ == '__main__':
    main()