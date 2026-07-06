#!/usr/bin/env python3
"""重建首页：深色玻璃态 + 今日报告快速入口 + 精简导航 + 核心数据卡"""
import os, re
from pathlib import Path
from datetime import datetime, date

ROOT = Path(__file__).parent
DOCS = ROOT / "docs"

today = date(2026, 7, 3)
TODAY_STR = today.strftime("%Y%m%d")
TODAY_DISPLAY = today.strftime("%Y年%m月%d日")
WEEKDAYS = ["周一","周二","周三","周四","周五","周六","周日"]
WEEKDAY = WEEKDAYS[today.weekday()]
UPDATE_TIME = datetime.now().strftime("%Y-%m-%d %H:%M")


def latest_report(d, name_filter=None):
    """获取目录下最新报告"""
    files = []
    for f in (DOCS/d).glob("*.html"):
        fn = f.name
        if fn in ("index.html","latest.html"): continue
        if fn.startswith("list_") or fn.startswith("test_") or fn.endswith(".bak") or "list_bak" in fn: continue
        if name_filter and name_filter not in fn: continue
        files.append(f)
    if not files: return None, None
    def date_key(fn):
        m = re.match(r"(\d{8})_", fn)
        return m.group(1) if m else "00000000"
    files.sort(key=lambda f: date_key(f.name), reverse=True)
    f = files[0]
    # 日期格式化
    m = re.match(r"(\d{4})(\d{2})(\d{2})_", f.name)
    dt = f"{m.group(1)}-{m.group(2)}-{m.group(3)}" if m else ""
    return f, dt


# ==== 收集"今日报告" ====
today_reports = []
for d, label, icon in [
    ("s_level_catalyst", "盘前S级催化扫描", "⚡"),
    ("daily", "每日新闻洞察", "📰"),
    ("tomorrow_catalyst", "明日催化剂", "🎯"),
    ("intraday", "盘中快报", "📡"),
    ("aftermarket", "盘后速递", "📊"),
]:
    f, dt = latest_report(d)
    if f and TODAY_STR in f.name:
        size = f.stat().st_size
        size_str = f"{size//1024}KB" if size < 1024*1024 else f"{size/1024/1024:.1f}MB"
        today_reports.append({
            "icon": icon,
            "label": label,
            "title": f.stem.replace(TODAY_STR+"_","").replace("_"," "),
            "url": f"{d}/{f.name}",
            "size": size_str,
        })

# ==== 最近可用报告（今日无则显示最近）====
recent_reports = []
for d, label, icon in [
    ("industry_chain", "产业链深度", "🔬"),
    ("weekly_review", "周复盘", "📅"),
    ("weekly_outlook", "周三前瞻", "🔮"),
    ("weekend_express", "周末速递", "🎉"),
    ("monthly", "月度报告", "📋"),
]:
    f, dt = latest_report(d)
    if f:
        size = f.stat().st_size
        size_str = f"{size//1024}KB"
        recent_reports.append({
            "icon": icon,
            "label": label,
            "title": f.stem,
            "url": f"{d}/latest.html",
            "date": dt,
            "size": size_str,
        })


def report_card(r, highlight=False):
    cls = "today-report" if highlight else ""
    star = '<span class="new-badge">NEW</span>' if highlight else ""
    return f'''<a href="{r['url']}" class="report-entry {cls}">
    <div class="re-icon">{r['icon']}</div>
    <div class="re-info">
        <div class="re-label">{r['label']} {star}</div>
        <div class="re-title">{r['title']}</div>
        <div class="re-meta"><i class="fas fa-file-alt"></i> {r['size']}</div>
    </div>
    <div class="re-arrow"><i class="fas fa-chevron-right"></i></div>
</a>'''


# 高频核心入口
core_tools = [
    ("💼", "持仓预警仪表盘", "portfolio_dashboard/index.html", "每日更新 · 持仓信号/止盈止损"),
    ("🔥", "龙虎榜", "longhubang/index.html", "每日更新 · 席位/资金流向"),
    ("🎯", "智能选题助手", "topic-picker/index.html", "每日更新 · 题材强度/机会"),
    ("🗺️", "板块热力图", "sector_heatmap/index_pro.html", "每日更新 · 板块轮动"),
    ("⏰", "业绩预告预警", "alert-system/index.html", "每日更新 · 业绩暴雷扫描"),
    ("📈", "个股深度分析", "stock_analysis/", "持仓股 · 基本面/技术面"),
    ("💓", "题材健康度", "topic-health/", "题材生命周期"),
    ("🕐", "数据时光机", "time-machine/index.html", "历史数据回溯"),
    ("🔬", "产业链时钟", "industry_chain_clock/index.html", "月度更新 · 产业链全景"),
    ("🧪", "预判验证中心", "prediction-center/index.html", "预判准确率跟踪"),
]

tool_cards_html = []
for icon, name, url, desc in core_tools:
    tool_cards_html.append(f'''<a href="{url}" class="tool-card">
    <div class="tc-icon">{icon}</div>
    <div class="tc-name">{name}</div>
    <div class="tc-desc">{desc}</div>
</a>''')

# 报告归档入口
archive_links = [
    ("📰", "每日洞察归档", "daily/"),
    ("⚡", "S级催化归档", "s_level_catalyst/"),
    ("📡", "盘中快报归档", "intraday/"),
    ("📊", "盘后速递归档", "aftermarket/"),
    ("🎯", "明日催化归档", "tomorrow_catalyst/"),
    ("🔬", "产业链归档", "industry_chain/"),
    ("📅", "周复盘归档", "weekly_review/"),
    ("🔮", "周三前瞻归档", "weekly_outlook/"),
    ("🎉", "周末速递归档", "weekend_express/"),
    ("📋", "月度报告归档", "monthly/"),
]
archive_html = ""
for icon, name, url in archive_links:
    archive_html += f'<a href="{url}" class="archive-link"><span class="al-icon">{icon}</span>{name}</a>\n'


HTML = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>投资研究中心 · {TODAY_DISPLAY} {WEEKDAY}</title>
<script src="https://cdn.tailwindcss.com"></script>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.5.1/css/all.min.css">
<link rel="stylesheet" href="assets/global-dark.css">
<style>
*{{box-sizing:border-box;}}
body{{
    background:linear-gradient(135deg,#0f0c29 0%,#302b63 50%,#24243e 100%);
    min-height:100vh;
    color:rgba(255,255,255,0.95);
    font-family:'Noto Sans SC',-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;
    margin:0;
    padding-top:72px;
}}

/* ====== 顶部导航 ====== */
.glass-nav{{
    position:fixed;top:0;left:0;right:0;z-index:1000;
    background:rgba(15,12,41,0.8);backdrop-filter:blur(30px);-webkit-backdrop-filter:blur(30px);
    border-bottom:1px solid rgba(255,255,255,0.1);
}}
.nav-inner{{max-width:1320px;margin:0 auto;padding:0 1.5rem;height:64px;display:flex;align-items:center;justify-content:space-between;}}
.nav-brand{{font-size:1.2rem;font-weight:800;color:#fff;text-decoration:none;display:flex;align-items:center;gap:10px;}}
.nav-brand .logo{{
    width:36px;height:36px;border-radius:10px;
    background:linear-gradient(135deg,#6366f1,#a855f7);
    display:flex;align-items:center;justify-content:center;font-size:18px;
}}
.nav-brand:hover{{color:#c4b5fd;}}
.nav-links{{display:flex;gap:4px;}}
.nav-links a{{color:rgba(255,255,255,0.75);text-decoration:none;padding:8px 14px;border-radius:10px;font-size:0.9rem;transition:all 0.2s;white-space:nowrap;font-weight:500;}}
.nav-links a:hover,.nav-links a.active{{background:rgba(255,255,255,0.1);color:#fff;}}
.hamburger{{display:none;background:rgba(255,255,255,0.1);border:1px solid rgba(255,255,255,0.2);color:#fff;width:40px;height:40px;border-radius:10px;cursor:pointer;font-size:18px;}}

/* ====== 主体容器 ====== */
.container{{max-width:1320px;margin:0 auto;padding:2rem 1.5rem 3rem;}}

/* ====== Hero区 ====== */
.hero{{
    background:linear-gradient(135deg,rgba(99,102,241,0.2),rgba(168,85,247,0.15));
    border:1px solid rgba(167,139,250,0.3);border-radius:24px;
    padding:40px 44px;margin-bottom:2rem;
    backdrop-filter:blur(20px);position:relative;overflow:hidden;
}}
.hero::before{{
    content:'';position:absolute;top:-50%;right:-20%;width:500px;height:500px;
    background:radial-gradient(circle,rgba(168,85,247,0.2),transparent 70%);
    pointer-events:none;
}}
.hero-date{{
    display:inline-block;background:linear-gradient(135deg,#6366f1,#a855f7);
    color:#fff;padding:6px 16px;border-radius:999px;font-size:0.85rem;font-weight:600;margin-bottom:16px;
}}
.hero h1{{
    font-size:2.5rem;font-weight:900;margin:0 0 10px;line-height:1.2;
    background:linear-gradient(135deg,#fff 0%,#c4b5fd 50%,#93c5fd 100%);
    -webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;
}}
.hero p{{color:rgba(255,255,255,0.7);font-size:1.05rem;margin:0;line-height:1.6;max-width:700px;}}

/* ====== Section ====== */
.section{{margin-bottom:2.5rem;}}
.section-header{{display:flex;align-items:center;justify-content:space-between;margin-bottom:1rem;}}
.section-title{{font-size:1.3rem;font-weight:700;color:#fff;display:flex;align-items:center;gap:10px;margin:0;}}
.section-title .st-icon{{
    width:32px;height:32px;border-radius:9px;
    background:linear-gradient(135deg,rgba(99,102,241,0.3),rgba(168,85,247,0.2));
    display:flex;align-items:center;justify-content:center;font-size:16px;
}}
.section-more{{color:#a78bfa;font-size:0.85rem;text-decoration:none;display:flex;align-items:center;gap:4px;}}
.section-more:hover{{color:#c4b5fd;}}

/* ====== 今日报告列表 ====== */
.today-grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(320px,1fr));gap:14px;}}
.report-entry{{
    display:flex;align-items:center;gap:16px;padding:18px 22px;
    background:rgba(255,255,255,0.06);backdrop-filter:blur(12px);
    border:1px solid rgba(255,255,255,0.1);border-radius:16px;
    text-decoration:none;color:inherit;transition:all 0.25s;
    position:relative;
}}
.report-entry:hover{{background:rgba(255,255,255,0.1);transform:translateY(-2px);border-color:rgba(167,139,250,0.3);box-shadow:0 12px 32px rgba(102,126,234,0.3);}}
.report-entry.today-report{{background:linear-gradient(135deg,rgba(16,185,129,0.15),rgba(52,211,153,0.08));border-color:rgba(16,185,129,0.3);}}
.report-entry.today-report:hover{{border-color:rgba(16,185,129,0.5);box-shadow:0 12px 32px rgba(16,185,129,0.25);}}
.re-icon{{
    width:48px;height:48px;border-radius:12px;font-size:22px;
    background:rgba(255,255,255,0.08);
    display:flex;align-items:center;justify-content:center;flex-shrink:0;
}}
.report-entry.today-report .re-icon{{background:rgba(16,185,129,0.2);}}
.re-info{{flex:1;min-width:0;}}
.re-label{{font-size:0.78rem;color:#a78bfa;font-weight:600;margin-bottom:4px;display:flex;align-items:center;gap:8px;}}
.re-title{{font-size:1rem;font-weight:600;color:#fff;line-height:1.4;
    overflow:hidden;text-overflow:ellipsis;white-space:nowrap;}}
.re-meta{{font-size:0.78rem;color:rgba(255,255,255,0.4);margin-top:4px;}}
.re-arrow{{color:rgba(255,255,255,0.3);font-size:0.8rem;transition:transform 0.2s;flex-shrink:0;}}
.report-entry:hover .re-arrow{{color:#a78bfa;transform:translateX(3px);}}
.new-badge{{background:linear-gradient(135deg,#10b981,#059669);color:#fff;font-size:0.65rem;padding:2px 7px;border-radius:4px;font-weight:700;letter-spacing:0.5px;}}

/* ====== 工具箱 ====== */
.tools-grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:14px;}}
.tool-card{{
    background:rgba(255,255,255,0.06);backdrop-filter:blur(12px);
    border:1px solid rgba(255,255,255,0.1);border-radius:16px;
    padding:22px 18px;text-decoration:none;color:inherit;
    transition:all 0.25s;text-align:center;
}}
.tool-card:hover{{background:rgba(255,255,255,0.1);transform:translateY(-3px);border-color:rgba(167,139,250,0.3);box-shadow:0 12px 32px rgba(102,126,234,0.3);}}
.tc-icon{{font-size:32px;margin-bottom:10px;}}
.tc-name{{font-size:1rem;font-weight:700;color:#fff;margin-bottom:6px;}}
.tc-desc{{font-size:0.78rem;color:rgba(255,255,255,0.55);line-height:1.4;}}

/* ====== 归档区 ====== */
.archive-section{{
    background:rgba(255,255,255,0.04);backdrop-filter:blur(12px);
    border:1px solid rgba(255,255,255,0.08);border-radius:16px;
    padding:24px;
}}
.archive-grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(180px,1fr));gap:10px;}}
.archive-link{{
    display:flex;align-items:center;gap:8px;padding:10px 14px;
    background:rgba(255,255,255,0.05);border-radius:10px;
    color:rgba(255,255,255,0.8);text-decoration:none;font-size:0.9rem;font-weight:500;
    transition:all 0.2s;border:1px solid transparent;
}}
.archive-link:hover{{background:rgba(167,139,250,0.15);color:#fff;border-color:rgba(167,139,250,0.3);}}
.al-icon{{font-size:16px;}}

/* ====== 数据状态卡 ====== */
.stats-row{{display:grid;grid-template-columns:repeat(auto-fit,minmax(160px,1fr));gap:12px;margin-bottom:2rem;}}
.stat-card{{
    background:rgba(255,255,255,0.06);backdrop-filter:blur(12px);
    border:1px solid rgba(255,255,255,0.1);border-radius:14px;
    padding:16px 18px;text-align:center;
}}
.stat-value{{font-size:1.6rem;font-weight:800;background:linear-gradient(135deg,#a78bfa,#60a5fa);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;}}
.stat-label{{font-size:0.78rem;color:rgba(255,255,255,0.55);margin-top:4px;}}

/* ====== Footer ====== */
.footer{{
    text-align:center;padding:2.5rem 0 1.5rem;
    color:rgba(255,255,255,0.35);font-size:0.82rem;
    border-top:1px solid rgba(255,255,255,0.08);margin-top:2rem;
}}
.footer a{{color:rgba(255,255,255,0.5);text-decoration:none;margin:0 8px;}}
.footer a:hover{{color:#a78bfa;}}
.disclaimer{{margin-top:8px;font-size:0.75rem;color:rgba(255,255,255,0.25);}}

@media(max-width:768px){{
    .nav-links{{display:none;}}
    .hamburger{{display:flex;align-items:center;justify-content:center;}}
    .hero{{padding:28px 22px;}}
    .hero h1{{font-size:1.8rem;}}
    .today-grid{{grid-template-columns:1fr;}}
    .tools-grid{{grid-template-columns:repeat(2,1fr);}}
    .archive-grid{{grid-template-columns:repeat(2,1fr);}}
    .stats-row{{grid-template-columns:repeat(2,1fr);}}
    body{{padding-top:64px;}}
}}
</style>
</head>
<body>

<nav class="glass-nav"><div class="nav-inner">
    <a href="./" class="nav-brand"><div class="logo"><i class="fas fa-chart-line"></i></div> 投资研究中心</a>
    <div class="nav-links">
        <a href="#today" class="active">📋 今日</a>
        <a href="#tools">🧰 工具箱</a>
        <a href="portfolio_dashboard/index.html">💼 持仓</a>
        <a href="s_level_catalyst/latest.html">⚡ S级</a>
        <a href="daily/latest.html">📰 日报</a>
        <a href="longhubang/index.html">🔥 龙虎榜</a>
        <a href="#archive">📂 归档</a>
    </div>
    <button class="hamburger" onclick="document.getElementById('mmenu').style.display='flex'"><i class="fas fa-bars"></i></button>
</div></nav>

<div class="container">

<!-- Hero -->
<div class="hero">
    <div class="hero-date"><i class="fas fa-calendar-day"></i> {TODAY_DISPLAY} · {WEEKDAY}</div>
    <h1>AI 驱动的 A 股投资研究中枢</h1>
    <p>每日盘前/盘后全自动扫描催化事件、资金流向、龙虎榜异动、题材轮动与持仓风险，为您提供机构级研究洞察与操作信号。</p>
</div>

<!-- 核心数据概览 -->
<div class="stats-row">
    <div class="stat-card"><div class="stat-value">{len(today_reports)}</div><div class="stat-label">今日已出报告</div></div>
    <div class="stat-card"><div class="stat-value">{len(recent_reports)}</div><div class="stat-label">本期周报/月报</div></div>
    <div class="stat-card"><div class="stat-value">{len(core_tools)}</div><div class="stat-label">核心工具</div></div>
    <div class="stat-card"><div class="stat-value">7×24</div><div class="stat-label">市场监测</div></div>
</div>

<!-- 今日报告 -->
<div class="section" id="today">
    <div class="section-header">
        <h2 class="section-title"><span class="st-icon">🔥</span>今日报告 · {TODAY_DISPLAY}</h2>
        <a href="daily/" class="section-more">查看全部 <i class="fas fa-arrow-right"></i></a>
    </div>
    <div class="today-grid">
        {''.join(report_card(r, highlight=True) for r in today_reports)}
    </div>
</div>

<!-- 本期周报/月报 -->
<div class="section">
    <div class="section-header">
        <h2 class="section-title"><span class="st-icon">📚</span>本期深度报告</h2>
    </div>
    <div class="today-grid">
        {''.join(report_card(r, highlight=False) for r in recent_reports[:5])}
    </div>
</div>

<!-- 工具箱 -->
<div class="section" id="tools">
    <div class="section-header">
        <h2 class="section-title"><span class="st-icon">🧰</span>研究工具箱</h2>
    </div>
    <div class="tools-grid">
        {''.join(tool_cards_html)}
    </div>
</div>

<!-- 归档 -->
<div class="section" id="archive">
    <div class="section-header">
        <h2 class="section-title"><span class="st-icon">📂</span>报告归档</h2>
    </div>
    <div class="archive-section">
        <div class="archive-grid">
            {archive_html}
        </div>
    </div>
</div>

<!-- Footer -->
<footer class="footer">
    <div>
        <a href="./">🏠 首页</a>·
        <a href="https://github.com/boya357/daily-news-insight" target="_blank"><i class="fab fa-github"></i> GitHub</a>·
        <a href="changelog.html">更新日志</a>
    </div>
    <div style="margin-top:8px;">最后更新：{UPDATE_TIME}</div>
    <div class="disclaimer">⚠️ 本系统所有数据与分析仅供研究参考，不构成任何投资建议。投资有风险，决策需谨慎。</div>
</footer>

</div>

<!-- Mobile Menu -->
<div class="mobile-menu" id="mmenu" style="display:none;position:fixed;top:0;left:0;right:0;bottom:0;background:rgba(15,12,41,0.97);backdrop-filter:blur(30px);z-index:2000;flex-direction:column;align-items:center;justify-content:center;gap:20px;padding:2rem;">
    <button style="position:absolute;top:20px;right:20px;background:transparent;border:none;color:#fff;font-size:24px;cursor:pointer;" onclick="document.getElementById('mmenu').style.display='none'"><i class="fas fa-times"></i></button>
    <a href="#today" onclick="document.getElementById('mmenu').style.display='none'" style="color:#fff;font-size:1.2rem;text-decoration:none;font-weight:600;">📋 今日报告</a>
    <a href="portfolio_dashboard/index.html" style="color:#fff;font-size:1.2rem;text-decoration:none;font-weight:600;">💼 持仓预警</a>
    <a href="s_level_catalyst/latest.html" style="color:#fff;font-size:1.2rem;text-decoration:none;font-weight:600;">⚡ S级催化</a>
    <a href="daily/latest.html" style="color:#fff;font-size:1.2rem;text-decoration:none;font-weight:600;">📰 每日洞察</a>
    <a href="longhubang/index.html" style="color:#fff;font-size:1.2rem;text-decoration:none;font-weight:600;">🔥 龙虎榜</a>
    <a href="#tools" onclick="document.getElementById('mmenu').style.display='none'" style="color:#fff;font-size:1.2rem;text-decoration:none;font-weight:600;">🧰 工具箱</a>
    <a href="#archive" onclick="document.getElementById('mmenu').style.display='none'" style="color:#fff;font-size:1.2rem;text-decoration:none;font-weight:600;">📂 归档</a>
</div>

</body>
</html>'''

# 备份现有index
import shutil
existing = DOCS / "index.html"
if existing.exists():
    shutil.copy2(existing, DOCS / "index.html.pre_rebuild_bak")

(DOCS / "index.html").write_text(HTML, encoding='utf-8')
print(f"✅ 首页已重建: {len(HTML)//1024}KB")
print(f"   今日报告: {len(today_reports)} 份")
for r in today_reports:
    print(f"     - {r['icon']} {r['label']}: {r['title'][:60]}")
print(f"   工具箱: {len(core_tools)} 个")
