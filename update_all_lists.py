#!/usr/bin/env python3
"""
通用列表页面更新脚本
彻底解决所有报告类型latest.html被覆盖成重定向页面的问题

支持的报告类型：
- daily: 每日新闻洞察
- intraday: 盘中快报  
- aftermarket: 盘后速递

使用方法：
    python update_all_lists.py [--type daily]  # 只更新指定类型
    python update_all_lists.py                  # 更新所有类型
"""

import os
import re
import glob
import argparse
from datetime import datetime

# 报告类型配置
REPORT_TYPES = {
    'daily': {
        'pattern': '*_每日新闻洞察.html',
        'title': '每日新闻洞察',
        'subtitle': '隔夜新闻与当日操作策略',
    },
    'intraday': {
        'pattern': '*_盘中快报.html',
        'title': '盘中快报',
        'subtitle': '午间市场点评与操作建议',
    },
    'aftermarket': {
        'pattern': '*_盘后速递.html',
        'title': '盘后速递',
        'subtitle': '收盘总结与明日策略',
    },
}

NAV_ITEMS = [
    ('首页', '/daily-news-insight/'),
    ('每日新闻洞察', '/daily-news-insight/daily/latest.html'),
    ('盘中快报', '/daily-news-insight/intraday/latest.html'),
    ('盘后速递', '/daily-news-insight/aftermarket/latest.html'),
    ('产业链', '/daily-news-insight/industry_chain/latest.html'),
    ('催化日历', '/daily-news-insight/催化日历/latest.html'),
]


def extract_report_info(html_path, report_type):
    """从HTML文件中提取报告信息"""
    try:
        with open(html_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 提取标题
        title_match = re.search(r'<title>(.+?)</title>', content)
        title = title_match.group(1) if title_match else os.path.basename(html_path).replace('.html', '')
        
        return {
            'filename': os.path.basename(html_path),
            'title': title,
            'path': html_path
        }
    except Exception as e:
        print(f"⚠️  解析文件失败 {html_path}: {e}")
        return None


def generate_list_page(report_type, reports):
    """生成列表页面HTML"""
    config = REPORT_TYPES[report_type]
    
    # 按日期排序（最新的在前面）
    reports.sort(key=lambda x: x['filename'], reverse=True)
    
    # 生成报告卡片HTML
    cards_html = ""
    for i, report in enumerate(reports):
        tag_html = '<span class="card-tag">今日</span>' if i == 0 else ''
        icon = '🆕' if i == 0 else '📅'
        subtitle = '市场分析与操作策略'
        
        card_html = f'''
        <a href="/daily-news-insight/{report_type}/{report['filename']}" class="card">
            <div class="card-icon">{icon}</div>
            <div class="card-content">
                <div class="card-title">{report['title']}</div>
                <div class="card-subtitle">{subtitle}</div>
            </div>
            {tag_html}
            <span class="card-arrow">›</span>
        </a>'''
        cards_html += card_html
    
    # 生成导航HTML
    nav_html = ''
    for name, href in NAV_ITEMS:
        is_current = href.endswith(f'{report_type}/latest.html')
        active_class = 'nav-item current' if is_current else 'nav-item'
        nav_html += f'        <a href="{href}" class="{active_class}">{name}</a>\n'
    
    html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{config['title']}</title>
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
        .card-icon {{ width: 48px; height: 48px; border-radius: 14px; display: flex; align-items: center; justify-content: center; font-size: 22px; flex-shrink: 0; background: linear-gradient(135deg, #6366f1, #8b5cf6); color: white; }}
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
{nav_html}    </div>
    <div class="container">
        <h1 class="page-title">📰 {config['title']}</h1>
        <p class="page-subtitle">{config['subtitle']}</p>
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


def update_report_type(base_dir, report_type):
    """更新指定类型的报告列表"""
    config = REPORT_TYPES[report_type]
    dir_path = os.path.join(base_dir, report_type)
    
    # 扫描所有HTML报告文件
    pattern = os.path.join(dir_path, config['pattern'])
    html_files = glob.glob(pattern)
    
    if not html_files:
        print(f"⚠️  {report_type}: 未找到任何报告文件")
        return False
    
    # 提取报告信息
    reports = []
    for html_file in html_files:
        info = extract_report_info(html_file, report_type)
        if info:
            reports.append(info)
    
    # 生成列表页面
    list_html = generate_list_page(report_type, reports)
    
    # 写入latest.html
    output_path = os.path.join(dir_path, 'latest.html')
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(list_html)
    
    print(f"✅ {report_type}: 已更新列表页，包含 {len(reports)} 个历史报告")
    return True


def main():
    parser = argparse.ArgumentParser(description='更新所有报告类型的列表页面')
    parser.add_argument('--type', type=str, choices=REPORT_TYPES.keys(),
                        help='只更新指定类型的报告（daily/intraday/aftermarket）')
    args = parser.parse_args()
    
    base_dir = '/app/data/所有对话/主对话/docs'
    
    if args.type:
        # 只更新指定类型
        update_report_type(base_dir, args.type)
    else:
        # 更新所有类型
        print("=" * 50)
        print("🔄 开始更新所有报告类型的列表页面...")
        print("=" * 50)
        
        for report_type in REPORT_TYPES.keys():
            update_report_type(base_dir, report_type)
        
        print("=" * 50)
        print("✅ 所有列表页面更新完成！")
        print("=" * 50)


if __name__ == '__main__':
    main()