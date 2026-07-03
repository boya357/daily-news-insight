#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
统一更新所有列表页 v3 - 深色玻璃态卡片网格
"""
import os, sys, re, shutil
from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).parent
DOCS = ROOT / "docs"

CONFIGS = {
    "daily":             ("📰 每日新闻洞察", "每日新闻洞察", True),
    "s_level_catalyst":  ("⚡ S级催化扫描", None, False),
    "intraday":          ("📡 盘中快报", "盘中快报", True),
    "aftermarket":       ("📊 盘后速递", "盘后速递", True),
    "tomorrow_catalyst": ("🎯 明日催化剂", "明日催化剂", True),
    "industry_chain":    ("🔬 产业链深度研究", None, False),
    "weekly_review":     ("📋 周复盘", "周复盘", False),
    "weekend_express":   ("🎉 周末速递", "周末速递", False),
    "weekly_outlook":    ("🔮 周三前瞻", "周三前瞻", False),
    "monthly":           ("📅 月度报告", None, False),
}

NAV_ITEMS = [
    ("/daily-news-insight/",                            "🏠 首页"),
    ("/daily-news-insight/s_level_catalyst/",           "⚡ S级催化"),
    ("/daily-news-insight/daily/",                      "📰 每日洞察"),
    ("/daily-news-insight/intraday/",                   "📡 盘中快报"),
    ("/daily-news-insight/aftermarket/",                "📊 盘后速递"),
    ("/daily-news-insight/tomorrow_catalyst/",          "🎯 明日催化"),
    ("/daily-news-insight/industry_chain/",             "🔬 产业链"),
    ("/daily-news-insight/weekly_review/",              "📋 周复盘"),
    ("/daily-news-insight/weekly_outlook/",             "🔮 周三前瞻"),
    ("/daily-news-insight/weekend_express/",            "🎉 周末速递"),
    ("/daily-news-insight/monthly/",                    "📅 月度报告"),
]

GRID_CSS = r"""
*{box-sizing:border-box;}
body{background:linear-gradient(135deg,#0f0c29,#302b63,#24243e);min-height:100vh;padding-top:80px;color:rgba(255,255,255,0.95);font-family:'Noto Sans SC',-apple-system,BlinkMacSystemFont,'PingFang SC','Microsoft YaHei',sans-serif;margin:0;}
a{color:#a78bfa;text-decoration:none;transition:color .2s;}
a:hover{color:#c4b5fd;}
.glass-nav{position:fixed;top:0;left:0;right:0;z-index:1000;background:rgba(15,12,41,0.75);backdrop-filter:blur(30px);-webkit-backdrop-filter:blur(30px);border-bottom:1px solid rgba(255,255,255,0.1);}
.nav-inner{max-width:1320px;margin:0 auto;padding:0 1.5rem;height:64px;display:flex;align-items:center;justify-content:space-between;}
.nav-brand{font-size:1.15rem;font-weight:700;color:#fff;text-decoration:none;display:flex;align-items:center;gap:8px;}
.nav-brand:hover{color:#c4b5fd;}
.nav-links{display:flex;gap:4px;flex-wrap:wrap;}
.nav-links a{color:rgba(255,255,255,0.7);text-decoration:none;padding:8px 12px;border-radius:8px;font-size:0.85rem;transition:all .2s;white-space:nowrap;}
.nav-links a:hover,.nav-links a.active{background:rgba(255,255,255,0.1);color:#fff;}
.container{max-width:1320px;margin:0 auto;padding:2rem 1.5rem 3rem;}
.page-header{margin-bottom:1.5rem;}
.page-title{font-size:1.8rem;font-weight:800;margin:0 0 .5rem;background:linear-gradient(135deg,#a78bfa,#60a5fa);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;}
.page-desc{color:rgba(255,255,255,0.6);font-size:.95rem;margin:0;}
.newest-card{background:linear-gradient(135deg,rgba(99,102,241,0.22),rgba(168,85,247,0.15));border:1px solid rgba(167,139,250,0.4);border-radius:20px;padding:24px 28px;margin-bottom:1.5rem;backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px);transition:transform .25s,box-shadow .25s;text-decoration:none;color:inherit;display:block;}
.newest-card:hover{transform:translateY(-3px);box-shadow:0 16px 48px rgba(102,126,234,0.4);}
.newest-label{display:inline-block;background:linear-gradient(135deg,#6366f1,#a855f7);color:#fff;padding:5px 14px;border-radius:999px;font-size:.75rem;font-weight:600;margin-bottom:12px;}
.newest-title{font-size:1.35rem;font-weight:700;color:#fff;margin-bottom:8px;line-height:1.35;word-break:break-word;}
.newest-meta{font-size:.85rem;color:rgba(255,255,255,0.6);display:flex;gap:16px;flex-wrap:wrap;}
.newest-meta i{color:#a78bfa;margin-right:4px;}
.report-frame-wrap{margin:0 0 2rem;border-radius:20px;overflow:hidden;border:1px solid rgba(167,139,250,0.3);background:rgba(0,0,0,0.2);box-shadow:0 16px 48px rgba(0,0,0,0.3);}
.report-frame{width:100%;min-height:900px;border:0;display:block;background:#1a1625;}
.frame-toolbar{display:flex;align-items:center;justify-content:space-between;padding:10px 18px;background:rgba(15,12,41,0.8);border-bottom:1px solid rgba(255,255,255,0.08);font-size:.85rem;flex-wrap:wrap;gap:8px;}
.frame-toolbar .frame-title{color:rgba(255,255,255,0.75);font-weight:500;}
.frame-toolbar a.open-new{color:#a78bfa;display:inline-flex;align-items:center;gap:6px;padding:6px 14px;background:rgba(167,139,250,0.15);border:1px solid rgba(167,139,250,0.3);border-radius:8px;transition:all .2s;}
.frame-toolbar a.open-new:hover{background:rgba(167,139,250,0.25);color:#fff;}
.section-title{font-size:1.1rem;font-weight:600;color:rgba(255,255,255,0.85);margin:2rem 0 1rem;display:flex;align-items:center;gap:8px;padding-bottom:10px;border-bottom:1px solid rgba(255,255,255,0.1);}
.section-title i{color:#a78bfa;}
.report-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:16px;}
.report-card{position:relative;background:rgba(255,255,255,0.05);backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px);border:1px solid rgba(255,255,255,0.1);border-radius:12px;padding:20px;transition:transform .25s,border-color .25s,box-shadow .25s,background .25s;text-decoration:none;color:inherit;display:flex;flex-direction:column;min-height:150px;overflow:hidden;}
.report-card::before{content:'';position:absolute;top:0;left:0;right:0;height:3px;background:linear-gradient(90deg,rgba(99,102,241,0.5),rgba(168,85,247,0.5));opacity:.6;}
.report-card:hover{background:rgba(255,255,255,0.09);transform:translateY(-4px);border-color:rgba(99,102,241,0.4);box-shadow:0 8px 30px rgba(99,102,241,0.15);}
.report-card.is-latest{border-color:rgba(16,185,129,0.5);box-shadow:0 0 20px rgba(16,185,129,0.15);}
.report-card.is-latest::before{background:linear-gradient(90deg,rgba(16,185,129,0.7),rgba(52,211,153,0.7));opacity:1;}
.report-card.is-latest:hover{border-color:rgba(16,185,129,0.7);box-shadow:0 8px 30px rgba(16,185,129,0.25);}
.report-icon{font-size:1.6rem;margin-bottom:10px;}
.report-date{font-size:.78rem;color:#a78bfa;font-weight:600;margin-bottom:6px;display:flex;align-items:center;gap:6px;}
.report-date i{font-size:.75rem;}
.report-name{font-size:.92rem;font-weight:600;color:#fff;line-height:1.4;margin-bottom:8px;flex:1;word-break:break-word;display:-webkit-box;-webkit-line-clamp:3;-webkit-box-orient:vertical;overflow:hidden;}
.report-badges{display:flex;gap:6px;flex-wrap:wrap;margin-bottom:8px;}
.badge{display:inline-block;padding:2px 8px;border-radius:999px;font-size:.7rem;font-weight:600;}
.badge-new{background:rgba(16,185,129,0.2);color:#6ee7b7;border:1px solid rgba(16,185,129,0.3);}
.badge-hot{background:rgba(239,68,68,0.18);color:#fca5a5;border:1px solid rgba(239,68,68,0.3);}
.badge-pre{background:rgba(59,130,246,0.18);color:#93c5fd;border:1px solid rgba(59,130,246,0.3);}
.badge-post{background:rgba(245,158,11,0.18);color:#fcd34d;border:1px solid rgba(245,158,11,0.3);}
.report-size{font-size:.72rem;color:rgba(255,255,255,0.4);margin-top:auto;}
.pro-footer{text-align:center;padding:2rem 0;color:rgba(255,255,255,0.4);font-size:.85rem;margin-top:3rem;border-top:1px solid rgba(255,255,255,0.08);}
@media(max-width:1024px){.report-grid{grid-template-columns:repeat(3,1fr);}}
@media(max-width:768px){
  .nav-links{display:none;}
  .report-grid{grid-template-columns:repeat(2,1fr);gap:12px;}
  .page-title{font-size:1.4rem;}
  .newest-title{font-size:1.1rem;}
  .newest-card{padding:18px 20px;}
  .container{padding:1.25rem 1rem 2rem;}
  .report-frame{min-height:600px;}
}
@media(max-width:480px){.report-grid{grid-template-columns:1fr;}}
"""

def build_nav(active_slug):
    links = []
    for href, label in NAV_ITEMS:
        is_active = href.rstrip('/') == f'/daily-news-insight/{active_slug}'.rstrip('/')
        cls = ' class="active"' if is_active else ''
        links.append(f'<a href="{href}"{cls}>{label}</a>')
    return '<div class="nav-links">' + ''.join(links) + '</div>'

LIST_TPL = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>__TITLE__ · 报告归档 - 投资研究中心</title>
<script src="https://cdn.tailwindcss.com"></script>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.5.1/css/all.min.css">
<link rel="stylesheet" href="/daily-news-insight/assets/global-dark.css">
<style>{GRID_CSS}</style>
</head>
<body>
<nav class="glass-nav"><div class="nav-inner">
<a href="/daily-news-insight/" class="nav-brand"><i class="fas fa-chart-line"></i> 投资研究中心</a>
__NAV__
</div></nav>
<div class="container">
<div class="page-header">
<h1 class="page-title"><i class="fas fa-folder-open"></i> __TITLE__</h1>
<p class="page-desc">📂 报告归档 · 共 __TOTAL__ 份 · 最新更新：__LATEST_DATE__</p>
</div>
__NEWEST_CARD__
<h2 class="section-title"><i class="fas fa-history"></i> 历史报告</h2>
<div class="report-grid">__REPORT_CARDS__</div>
<footer class="pro-footer">投资研究中心 · 数据仅供参考，不构成投资建议 · __GEN_TIME__</footer>
</div>
</body>
</html>'''

COMBO_TPL = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>__TITLE__ · 最新报告 - 投资研究中心</title>
<script src="https://cdn.tailwindcss.com"></script>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.5.1/css/all.min.css">
<link rel="stylesheet" href="/daily-news-insight/assets/global-dark.css">
<style>{GRID_CSS}</style>
</head>
<body>
<nav class="glass-nav"><div class="nav-inner">
<a href="/daily-news-insight/" class="nav-brand"><i class="fas fa-chart-line"></i> 投资研究中心</a>
__NAV__
</div></nav>
<div class="container">
<div class="page-header">
<h1 class="page-title"><i class="fas fa-bolt"></i> __TITLE__</h1>
<p class="page-desc">⚡ 最新报告 · __LATEST_DATE__ · 共 __TOTAL__ 份归档</p>
</div>
<div class="report-frame-wrap">
  <div class="frame-toolbar">
    <span class="frame-title"><i class="fas fa-star" style="color:#fbbf24;margin-right:6px;"></i>最新报告：__LATEST_NAME__</span>
    <a href="__LATEST_HREF__" class="open-new" target="_blank"><i class="fas fa-external-link-alt"></i> 新窗口打开</a>
  </div>
  <iframe class="report-frame" id="reportFrame" src="__LATEST_HREF__" title="最新报告" loading="lazy"></iframe>
</div>
<h2 class="section-title"><i class="fas fa-history"></i> 历史报告归档</h2>
<div class="report-grid">__REPORT_CARDS__</div>
<footer class="pro-footer">投资研究中心 · 数据仅供参考，不构成投资建议 · __GEN_TIME__</footer>
</div>
<script>
window.addEventListener('load', function(){{
  var iframe = document.getElementById('reportFrame');
  function resize(){{
    try{{
      var h = Math.max(800, iframe.contentDocument.documentElement.scrollHeight);
      iframe.style.height = h + 'px';
    }}catch(e){{}}
  }}
  iframe.addEventListener('load', resize);
  setTimeout(resize, 800);
  setTimeout(resize, 2500);
}});
</script>
</body>
</html>'''


def date_key(name):
    m = re.match(r"(\d{8})_", name)
    if m: return m.group(1)
    m = re.match(r"(\d{6})_", name)
    if m: return m.group(1) + "00"
    return "00000000"

def fmt_date(fn):
    m = re.match(r"(\d{4})(\d{2})(\d{2})_", fn)
    if m: return f"{m.group(1)}-{m.group(2)}-{m.group(3)}"
    m = re.match(r"(\d{4})(\d{2})_", fn)
    if m: return f"{m.group(1)}-{m.group(2)}"
    return ""

def fmt_size(s):
    if s < 1024: return f"{s}B"
    if s < 1024*1024: return f"{s//1024}KB"
    return f"{s/1024/1024:.1f}MB"

def guess_icon(name):
    if any(k in name for k in ['盘前']): return '🌅'
    if any(k in name for k in ['盘后','速递']): return '📊'
    if any(k in name for k in ['日报','每日']): return '📰'
    if any(k in name for k in ['S级','催化']): return '⚡'
    if any(k in name for k in ['周复盘']): return '📋'
    if any(k in name for k in ['周末']): return '🎉'
    if any(k in name for k in ['周三','前瞻','outlook']): return '🔮'
    if any(k in name for k in ['月报','月度']): return '📅'
    if any(k in name for k in ['产业链','MLCC','AIPC','金刚石','散热','机器人','英伟达','芯片','存储','先进封装','沃什','四因素','华为','光器件','CCL','比亚迪','璇玑','N1X','COMPUTEX','人形']): return '🔬'
    if any(k in name for k in ['盘中','快报']): return '📡'
    return '📄'

def guess_badges(name):
    badges = []
    if '盘前' in name:
        badges.append('<span class="badge badge-pre">盘前</span>')
    elif '盘后' in name:
        badges.append('<span class="badge badge-post">盘后</span>')
    if any(k in name for k in ['S级','史诗级','炸裂','超级','集体重挫','集体','爆冷','爆']):
        badges.append('<span class="badge badge-hot">🔥 热点</span>')
    return ''.join(badges)

def build_card(f, is_latest=False):
    dt = fmt_date(f.name)
    sz = fmt_size(f.stat().st_size)
    icon = guess_icon(f.name)
    extra_cls = ' is-latest' if is_latest else ''
    badges = ''
    if is_latest:
        badges = '<span class="badge badge-new">✨ 最新</span>'
    badges += guess_badges(f.name)
    return f'''<a href="{f.name}" class="report-card{extra_cls}">
<div class="report-icon">{icon}</div>
<div class="report-date"><i class="fas fa-calendar-day"></i>{dt}</div>
<div class="report-name">{f.stem}</div>
<div class="report-badges">{badges}</div>
<div class="report-size"><i class="fas fa-file-alt" style="margin-right:4px;"></i>{sz}</div>
</a>'''

def update_one(dirname):
    if dirname not in CONFIGS:
        print(f"  ❌ 未知目录: {dirname}"); return False
    title, name_filter, is_highfreq = CONFIGS[dirname]
    d = DOCS / dirname
    if not d.exists():
        print(f"  ⚠️ {dirname}: 目录不存在"); return False
    files = []
    for f in d.glob("*.html"):
        fn = f.name
        if fn in ("index.html","latest.html"): continue
        if fn.startswith("list_") or fn.startswith("test_") or fn.endswith(".bak") or "list_bak" in fn: continue
        if fn.startswith("intraday_"): continue  # skip old intraday_latest
        if name_filter and name_filter not in fn: continue
        files.append(f)
    files.sort(key=lambda f: date_key(f.name), reverse=True)
    if not files:
        print(f"  ⚠️ {dirname}: 无报告文件"); return False
    newest = files[0]
    total = len(files)
    latest_date = fmt_date(newest.name) or datetime.fromtimestamp(newest.stat().st_mtime).strftime("%Y-%m-%d")
    gen_time = datetime.now().strftime("%Y-%m-%d %H:%M")
    nav_html = build_nav(dirname)

    newest_card = f'''<a href="{newest.name}" class="newest-card">
<span class="newest-label"><i class="fas fa-star"></i> 最新报告 · 点击查看</span>
<div class="newest-title">{newest.stem}</div>
<div class="newest-meta">
  <span><i class="fas fa-calendar"></i>{latest_date}</span>
  <span><i class="fas fa-file-alt"></i>{fmt_size(newest.stat().st_size)}</span>
  <span><i class="fas fa-bolt"></i>共 {total} 份归档</span>
</div>
</a>'''
    cards = []
    for f in files[1:]:
        cards.append(build_card(f, is_latest=False))
    if len(files) == 1:
        cards_html = build_card(newest, is_latest=True)
    else:
        cards_html = '\n'.join(cards)

    idx = LIST_TPL
    for k, v in {"__TITLE__":title,"__TOTAL__":str(total),"__LATEST_DATE__":latest_date,
                 "__NEWEST_CARD__":newest_card,"__REPORT_CARDS__":cards_html,
                 "__GEN_TIME__":gen_time,"__NAV__":nav_html}.items():
        idx = idx.replace(k, v)
    (d/"index.html").write_text(idx, encoding='utf-8')

    if is_highfreq:
        # 高频目录：latest.html 直达最新报告副本
        shutil.copy2(newest, d/"latest.html")
        mode = "高频(最新直达)"
    else:
        # 低频目录：latest.html = index.html 纯卡片网格列表页（无iframe无内嵌）
        (d/"latest.html").write_text(idx, encoding='utf-8')
        mode = "低频(卡片列表)"
    print(f"  ✅ {dirname} [{mode}]: {newest.name[:50]} ({fmt_size(newest.stat().st_size)}), {total}份")
    return True

def main():
    targets = sys.argv[1:] if len(sys.argv)>1 else list(CONFIGS.keys())
    print('='*60)
    print(f'🚀 更新列表页 v3（深色玻璃态4列卡片网格，{len(targets)}个目录）')
    print('='*60)
    ok=fail=0
    for name in targets:
        print(f'📦 {name}...')
        if update_one(name): ok+=1
        else: fail+=1
    print(f'\n✅ 完成：成功 {ok}，失败 {fail}')

if __name__ == "__main__":
    main()
