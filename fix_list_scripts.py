#!/usr/bin/env python3
"""
统一修复所有 update_*_list.py 脚本:
1. 列表页输出到 index.html（而不是latest.html）
2. 自动将最新报告复制为 latest.html
3. 列表模板强制深色玻璃态
4. 日频目录：latest=最新报告副本；周/月目录：latest=最新报告副本（非生成日也展示最近一期）
"""
import os, glob, shutil, sys, re
from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).parent
DOCS = ROOT / "docs"

# 统一的列表页深色模板
LIST_TEMPLATE_DARK = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} · 报告归档 - 投资研究中心</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.5.1/css/all.min.css">
    <link rel="stylesheet" href="/daily-news-insight/assets/global-dark.css">
    <style>
        body {{
            background: linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%);
            min-height: 100vh;
            padding-top: 80px;
            color: rgba(255,255,255,0.95);
            font-family: 'Noto Sans SC', sans-serif;
        }}
        .glass-nav {{
            background: rgba(15,12,41,0.75);
            backdrop-filter: blur(30px);
            border-bottom: 1px solid rgba(255,255,255,0.1);
            position: fixed; top:0; left:0; right:0; z-index:1000;
        }}
        .nav-inner {{ max-width:1280px; margin:0 auto; padding:0 1.5rem; height:64px; display:flex; align-items:center; justify-content:space-between; }}
        .nav-brand {{ font-size:1.2rem; font-weight:700; color:#fff; text-decoration:none; display:flex; align-items:center; gap:8px; }}
        .nav-links {{ display:flex; gap:4px; }}
        .nav-links a {{
            color: rgba(255,255,255,0.7); text-decoration:none; padding:8px 14px; border-radius:8px;
            font-size:0.9rem; transition: all 0.2s;
        }}
        .nav-links a:hover, .nav-links a.active {{ background:rgba(255,255,255,0.1); color:#fff; }}
        .container {{ max-width: 1200px; margin: 0 auto; padding: 2rem 1.5rem; }}
        .page-header {{ margin-bottom: 2rem; }}
        .page-title {{ font-size:2rem; font-weight:800; margin-bottom:0.5rem;
            background: linear-gradient(135deg, #a78bfa, #60a5fa); -webkit-background-clip:text;
            -webkit-text-fill-color: transparent; background-clip:text; }}
        .page-desc {{ color: rgba(255,255,255,0.6); font-size:0.95rem; }}
        .newest-card {{
            background: linear-gradient(135deg, rgba(99,102,241,0.2), rgba(168,85,247,0.15));
            border: 1px solid rgba(167,139,250,0.4);
            border-radius: 20px; padding: 24px 28px; margin-bottom: 2rem;
            backdrop-filter: blur(20px); transition: transform 0.2s;
        }}
        .newest-card:hover {{ transform: translateY(-3px); }}
        .newest-label {{ display:inline-block; background: linear-gradient(135deg,#6366f1,#a855f7);
            color:#fff; padding:4px 12px; border-radius:999px; font-size:0.75rem;
            font-weight:600; margin-bottom: 12px; }}
        .newest-title {{ font-size:1.4rem; font-weight:700; color:#fff; margin-bottom:8px; }}
        .newest-title a {{ color:#fff; text-decoration:none; }}
        .newest-title a:hover {{ color:#c4b5fd; }}
        .newest-meta {{ font-size:0.85rem; color:rgba(255,255,255,0.6); }}
        .section-title {{ font-size:1.1rem; font-weight:600; color:rgba(255,255,255,0.8);
            margin: 2rem 0 1rem; display:flex; align-items:center; gap:8px; padding-bottom:8px;
            border-bottom: 1px solid rgba(255,255,255,0.1); }}
        .report-grid {{ display:grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 16px; }}
        .report-card {{
            background: rgba(255,255,255,0.06);
            backdrop-filter: blur(12px);
            border: 1px solid rgba(255,255,255,0.1);
            border-radius: 14px; padding: 18px 20px;
            transition: all 0.25s;
            text-decoration: none; color: inherit; display:block;
        }}
        .report-card:hover {{
            background: rgba(255,255,255,0.1);
            transform: translateY(-2px);
            border-color: rgba(167,139,250,0.3);
            box-shadow: 0 12px 32px rgba(102,126,234,0.3);
        }}
        .report-date {{ font-size:0.8rem; color:#a78bfa; font-weight:600; margin-bottom:6px; }}
        .report-name {{ font-size:1rem; font-weight:600; color:#fff; line-height:1.4; margin-bottom:6px; }}
        .report-size {{ font-size:0.75rem; color: rgba(255,255,255,0.4); }}
        .pro-footer {{
            text-align:center; padding:2rem 0; color:rgba(255,255,255,0.4);
            font-size:0.85rem; margin-top: 3rem; border-top: 1px solid rgba(255,255,255,0.08);
        }}
        @media (max-width: 768px) {{
            .nav-links {{ display:none; }}
            .report-grid {{ grid-template-columns: 1fr; }}
            .page-title {{ font-size:1.5rem; }}
        }}
    </style>
</head>
<body>
    <nav class="glass-nav">
        <div class="nav-inner">
            <a href="/daily-news-insight/" class="nav-brand">
                <i class="fas fa-chart-line"></i> 投资研究中心
            </a>
            <div class="nav-links">
                <a href="/daily-news-insight/">🏠 首页</a>
                <a href="/daily-news-insight/s_level_catalyst/">⚡ S级催化</a>
                <a href="/daily-news-insight/daily/">📰 每日洞察</a>
                <a href="/daily-news-insight/intraday/">📡 盘中快报</a>
                <a href="/daily-news-insight/aftermarket/">📊 盘后速递</a>
                <a href="/daily-news-insight/tomorrow_catalyst/">🎯 明日催化</a>
                <a href="/daily-news-insight/portfolio_dashboard/">💼 持仓预警</a>
                <a href="/daily-news-insight/stock_analysis/">📈 个股</a>
                <a href="/daily-news-insight/longhubang/">🔥 龙虎榜</a>
            </div>
        </div>
    </nav>
    <div class="container">
        <div class="page-header">
            <h1 class="page-title"><i class="fas fa-folder-open"></i> {title} · 报告归档</h1>
            <p class="page-desc">共 {total} 份报告 · 最新更新：{latest_date}</p>
        </div>
        {newest_card}
        <h2 class="section-title"><i class="fas fa-history"></i> 历史报告</h2>
        <div class="report-grid">
            {report_cards}
        </div>
        <footer class="pro-footer">
            投资研究中心 · 数据仅供参考，不构成投资建议 · Generated at {gen_time}
        </footer>
    </div>
</body>
</html>'''

# 日频目录配置
CONFIGS = [
    {"dir": "daily", "title": "每日新闻洞察", "name_filter": "每日新闻洞察", "freq": "daily"},
    {"dir": "s_level_catalyst", "title": "S级催化扫描", "name_filter": None, "freq": "daily"},
    {"dir": "intraday", "title": "盘中快报", "name_filter": "盘中快报", "freq": "daily"},
    {"dir": "aftermarket", "title": "盘后速递", "name_filter": "盘后速递", "freq": "daily"},
    {"dir": "tomorrow_catalyst", "title": "明日催化剂", "name_filter": "明日催化剂", "freq": "daily"},
    {"dir": "industry_chain", "title": "产业链深度研究", "name_filter": None, "freq": "ad-hoc"},
    {"dir": "weekly_review", "title": "周复盘", "name_filter": "周复盘", "freq": "weekly"},
    {"dir": "weekend_express", "title": "周末速递", "name_filter": "周末速递", "freq": "weekly"},
    {"dir": "weekly_outlook", "title": "周三前瞻", "name_filter": "周三前瞻", "freq": "weekly"},
    {"dir": "monthly", "title": "月度报告", "name_filter": "月报", "freq": "monthly"},
    {"dir": "topic-health", "title": "题材健康度", "name_filter": None, "freq": "daily"},
]


def get_report_files(d: Path, name_filter=None):
    files = []
    for f in d.glob("*.html"):
        fn = f.name
        if fn in ("index.html", "latest.html"):
            continue
        if fn.startswith("list_") or fn.startswith("test_") or fn.endswith(".bak") or "list_bak" in fn:
            continue
        if name_filter and name_filter not in fn:
            continue
        files.append(f)
    files.sort(key=lambda f: f.stat().st_mtime, reverse=True)
    return files


def fmt_date(path: Path):
    """从文件名或mtime提取日期"""
    fn = path.name
    m = re.match(r"(\d{8})_", fn)
    if m:
        s = m.group(1)
        return f"{s[:4]}-{s[4:6]}-{s[6:8]}"
    return datetime.fromtimestamp(path.stat().st_mtime).strftime("%Y-%m-%d")


def fmt_size(size: int):
    if size < 1024:
        return f"{size}B"
    if size < 1024*1024:
        return f"{size//1024}KB"
    return f"{size/1024/1024:.1f}MB"


def build_list_page(cfg):
    d = DOCS / cfg["dir"]
    if not d.exists():
        print(f"  ⏭️  {cfg['dir']}: 目录不存在")
        return
    
    files = get_report_files(d, cfg.get("name_filter"))
    if not files:
        print(f"  ⚠️  {cfg['dir']}: 无报告")
        return
    
    total = len(files)
    newest = files[0]
    latest_date = fmt_date(newest)
    gen_time = datetime.now().strftime("%Y-%m-%d %H:%M")
    
    # 1. 复制最新报告到 latest.html（修复核心逻辑）
    latest_target = d / "latest.html"
    # 备份当前错误的
    if latest_target.exists():
        bak = d / "latest.html.list_bak"
        if not bak.exists():
            shutil.copy2(latest_target, bak)
    shutil.copy2(newest, latest_target)
    
    # 2. 构建index.html列表页
    newest_card = f'''<a href="{newest.name}" class="newest-card">
        <span class="newest-label"><i class="fas fa-star"></i> 最新报告</span>
        <div class="newest-title">{newest.stem}</div>
        <div class="newest-meta">
            <i class="fas fa-calendar"></i> {latest_date} ·
            <i class="fas fa-file-alt"></i> {fmt_size(newest.stat().st_size)} ·
            <i class="fas fa-external-link-alt"></i> 点击查看
        </div>
    </a>'''
    
    cards = []
    for f in files[1:]:  # 除最新外的历史报告
        date = fmt_date(f)
        size = fmt_size(f.stat().st_size)
        cards.append(f'''<a href="{f.name}" class="report-card">
            <div class="report-date"><i class="fas fa-calendar-day"></i> {date}</div>
            <div class="report-name">{f.stem}</div>
            <div class="report-size">{size}</div>
        </a>''')
    
    html = LIST_TEMPLATE_DARK.format(
        title=cfg["title"],
        total=total,
        latest_date=latest_date,
        newest_card=newest_card,
        report_cards="\n            ".join(cards),
        gen_time=gen_time
    )
    
    (d / "index.html").write_text(html, encoding='utf-8')
    print(f"  ✅ {cfg['dir']}: latest.html ← {newest.name} ({fmt_size(newest.stat().st_size)}); index.html 已更新 ({total}份)")


def main():
    print("=" * 60)
    print("🔧 重建所有列表页 & 修复 latest.html 逻辑")
    print("=" * 60)
    for cfg in CONFIGS:
        build_list_page(cfg)
    print("\n🎉 所有列表页已按新规则生成")
    print("   - latest.html = 最新报告的完整副本")
    print("   - index.html  = 深色玻璃态归档列表")


if __name__ == "__main__":
    main()
