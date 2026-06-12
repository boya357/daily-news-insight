#!/usr/bin/env python3
"""
首页"最新发布"模块自动更新工具

扫描所有报告目录，找到最新发布的报告，自动更新首页的"最新发布"模块。
用法：
    python3 v3/tools/update_homepage_latest.py [--count N] [--max-per-category N]
"""

import os
import re
import glob
import argparse
from datetime import datetime

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DOCS_DIR = os.path.join(ROOT_DIR, 'docs')

# 报告目录配置
REPORT_CONFIG = {
    's级催化扫描': {
        'name': 'S级催化',
        'icon': '⭐',
        'desc': '超级催化事件深度挖掘',
        'pattern': '*_*.html',
        'exclude': ['latest.html', 'index.html'],
    },
    'daily': {
        'name': '每日新闻洞察',
        'icon': '📰',
        'desc': '早间市场综述与机会挖掘',
        'pattern': '*_每日新闻洞察.html',
        'exclude': ['latest.html'],
    },
    'aftermarket': {
        'name': '盘后速递',
        'icon': '🌅',
        'desc': '收盘总结与明日策略',
        'pattern': '*_盘后速递.html',
        'exclude': ['latest.html'],
    },
    'intraday': {
        'name': '盘中快报',
        'icon': '⚡',
        'desc': '盘中实时热点追踪',
        'pattern': '*_盘中快报.html',
        'exclude': ['latest.html'],
    },
    'industry_chain': {
        'name': '产业链深度',
        'icon': '🔗',
        'desc': '产业链全景分析报告',
        'pattern': '*_*.html',
        'exclude': ['latest.html', 'index.html'],
    },
    'weekly_review': {
        'name': '周复盘',
        'icon': '📋',
        'desc': '一周市场回顾与总结',
        'pattern': '*_周复盘.html',
        'exclude': ['latest.html'],
    },
    'weekly_outlook': {
        'name': '周三前瞻',
        'icon': '👁️',
        'desc': '下周市场前瞻与机会',
        'pattern': '*_周三前瞻.html',
        'exclude': ['latest.html'],
    },
    '周末速递': {
        'name': '周末速递',
        'icon': '📦',
        'desc': '周末重磅消息汇总',
        'pattern': '*_周末速递.html',
        'exclude': ['latest.html'],
    },
    '明日催化剂': {
        'name': '明日催化剂',
        'icon': '⏰',
        'desc': '明日重要事件与催化',
        'pattern': '*_明日催化剂.html',
        'exclude': ['latest.html'],
    },
    'monthly': {
        'name': '月度报告',
        'icon': '📅',
        'desc': '月度市场全景分析',
        'pattern': '*_月度报告.html',
        'exclude': ['latest.html'],
    },
    '题材深度': {
        'name': '题材深度分析',
        'icon': '🎯',
        'desc': '热点题材深度研究',
        'pattern': 'topic_*.html',
        'exclude': ['index.html'],
    },
    '题材健康度报告': {
        'name': '题材健康度',
        'icon': '💓',
        'desc': '题材热度与健康度评分',
        'pattern': 'health_report_*.html',
        'exclude': ['latest.html'],
    },
}


def extract_date_from_filename(filename):
    """从文件名中提取日期（用于显示）"""
    match = re.search(r'(\d{8})', filename)
    if match:
        date_str = match.group(1)
        try:
            return datetime.strptime(date_str, '%Y%m%d')
        except ValueError:
            pass
    
    match = re.search(r'(\d{4}-\d{2}-\d{2})', filename)
    if match:
        date_str = match.group(1)
        try:
            return datetime.strptime(date_str, '%Y-%m-%d')
        except ValueError:
            pass
    
    return None


def extract_title_from_html(filepath, default_title):
    """从HTML文件中提取简洁标题"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 先找 <title> 标签
        title_match = re.search(r'<title>([^<]+)</title>', content)
        if title_match:
            title = title_match.group(1).strip()
            # 去掉后缀
            title = re.sub(r'\s*[-|]\s*投资研究中心$', '', title)
            title = re.sub(r'\s*[-|]\s*市场洞察中心$', '', title)
            # 去掉前缀日期
            title = re.sub(r'^\d{6,8}\s*[-_ ]?', '', title)
            return title.strip()
        
        # 再找 <h1> 标签
        h1_match = re.search(r'<h1[^>]*>([^<]+)</h1>', content)
        if h1_match:
            title = h1_match.group(1).strip()
            title = re.sub(r'^\d{6,8}\s*[-_ ]?', '', title)
            return title.strip()
    except Exception as e:
        print(f"  ⚠️ 读取标题失败: {filepath}, {e}")
    
    return default_title


def get_latest_reports(count=4, max_per_category=1):
    """获取最新的报告列表"""
    all_reports = []
    
    for dirname, config in REPORT_CONFIG.items():
        dirpath = os.path.join(DOCS_DIR, dirname)
        if not os.path.isdir(dirpath):
            continue
        
        pattern = config['pattern']
        files = glob.glob(os.path.join(dirpath, pattern))
        
        cat_reports = []
        for filepath in files:
            filename = os.path.basename(filepath)
            
            if filename in config.get('exclude', []):
                continue
            
            # 使用文件实际修改时间排序（最准确）
            mtime = os.path.getmtime(filepath)
            sort_date = datetime.fromtimestamp(mtime)
            
            # 显示用日期：优先文件名中的日期，其次修改时间
            display_date = extract_date_from_filename(filename)
            if display_date is None:
                display_date = sort_date
            
            rel_path = f"{dirname}/{filename}"
            title = extract_title_from_html(filepath, config['name'])
            
            # 标题过长时截断
            if len(title) > 20:
                title = title[:18] + '...'
            
            cat_reports.append({
                'dir': dirname,
                'path': rel_path,
                'filename': filename,
                'sort_date': sort_date,
                'display_date': display_date,
                'title': title,
                'icon': config['icon'],
                'desc': config['desc'],
                'category': config['name'],
            })
        
        # 每个类别内按时间排序
        cat_reports.sort(key=lambda x: x['sort_date'], reverse=True)
        
        # 每个类别取前N条
        all_reports.extend(cat_reports[:max_per_category])
    
    # 全局排序
    all_reports.sort(key=lambda x: x['sort_date'], reverse=True)
    
    return all_reports[:count]


def generate_latest_section_html(reports):
    """生成最新发布模块的HTML"""
    cards_html = ''
    for report in reports:
        card = f'''
<a href="{report['path']}" class="block bg-gradient-to-r from-blue-500/20 to-cyan-500/20 border border-blue-400/30 rounded-xl p-4 hover:from-blue-500/30 hover:to-cyan-500/30 transition-all group">
    <div class="flex items-center gap-3 mb-2">
        <span class="text-3xl">{report['icon']}</span>
        <div>
            <h3 class="font-bold text-lg group-hover:text-yellow-300 transition-colors">{report['title']}</h3>
            <p class="text-white/70 text-sm">{report['desc']}</p>
        </div>
    </div>
</a>
'''
        cards_html += card
    
    update_time = datetime.now().strftime('%Y-%m-%d %H:%M')
    
    html = f'''
        <!-- 【第一区】最新发布横幅 - 突出显示最新报告 -->
        <div class="featured-banner rounded-2xl p-6 mb-6 text-white shadow-2xl">
            <div class="flex items-center justify-between mb-4">
                <div class="flex items-center gap-3">
                    <div class="relative">
                        <div class="w-4 h-4 bg-yellow-400 rounded-full"></div>
                        <div class="pulse-ring absolute inset-0 w-4 h-4 bg-yellow-400 rounded-full opacity-75"></div>
                    </div>
                    <span class="text-yellow-300 font-bold text-sm">✨ 最新发布</span>
                </div>
                <span class="text-white/60 text-xs">{update_time} 更新</span>
            </div>
            <div class="grid grid-cols-2 gap-4">
                {cards_html.strip()}
            </div>
        </div>
'''
    return html


def update_homepage(count=4, max_per_category=1):
    """更新首页的最新发布模块"""
    index_path = os.path.join(DOCS_DIR, 'index.html')
    
    if not os.path.exists(index_path):
        print(f"❌ 首页文件不存在: {index_path}")
        return False
    
    reports = get_latest_reports(count=count, max_per_category=max_per_category)
    if not reports:
        print("❌ 没有找到任何报告")
        return False
    
    print(f"📊 找到 {len(reports)} 个最新报告:")
    for r in reports:
        print(f"  - {r['sort_date'].strftime('%Y-%m-%d %H:%M')} | {r['title']} ({r['category']})")
    
    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_section = generate_latest_section_html(reports)
    
    pattern = r'(\s*<!-- 【第一区】最新发布横幅.*?</div>\s*</div>\s*)'
    
    match = re.search(pattern, content, re.DOTALL)
    if match:
        old_section = match.group(1)
        content = content.replace(old_section, '\n' + new_section + '\n')
        
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ 首页最新发布模块已更新 ({len(reports)} 条)")
        return True
    else:
        print("❌ 未找到最新发布模块的标记")
        return False


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='更新首页"最新发布"模块')
    parser.add_argument('--count', type=int, default=4, help='显示的报告数量（默认4条）')
    parser.add_argument('--max-per-category', type=int, default=1, help='每个类别最多显示几条（默认1条）')
    args = parser.parse_args()
    
    success = update_homepage(count=args.count, max_per_category=args.max_per_category)
    exit(0 if success else 1)
