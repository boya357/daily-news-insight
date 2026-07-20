#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""雅克科技深度研究报告 HTML生成器（2026-07-20版）"""
import sys, os, re, html as html_mod
from pathlib import Path

ROOT = Path("/root/daily-news-insight")
os.chdir(str(ROOT))
sys.path.insert(0, str(ROOT / "v3"))

MD_PATH = Path("/app/data/所有对话/主对话/雅克科技深度研究_report.md")
ASSETS_SRC = Path("/app/data/所有对话/主对话/雅克科技深度研究_assets")
OUT_DIR = ROOT / "docs" / "industry_chain"
OUT_DIR.mkdir(parents=True, exist_ok=True)
# Copy assets to public dir
ASSETS_DST = OUT_DIR / "assets" / "yake_20260720"
ASSETS_DST.mkdir(parents=True, exist_ok=True)
for img in ASSETS_SRC.glob("*.png"):
    import shutil
    shutil.copy(img, ASSETS_DST / img.name)

OUT = OUT_DIR / "20260720_雅克科技深度研究.html"

NAV_ITEMS = [
    ("/daily-news-insight/", "🏠 首页"),
    ("/daily-news-insight/s_level_catalyst/", "⚡ S级催化"),
    ("/daily-news-insight/daily/", "📰 每日洞察"),
    ("/daily-news-insight/intraday/", "📡 盘中快报"),
    ("/daily-news-insight/aftermarket/", "📊 盘后速递"),
    ("/daily-news-insight/tomorrow_catalyst/", "🎯 明日催化"),
    ("/daily-news-insight/industry_chain/", "🔬 产业链", True),
    ("/daily-news-insight/weekly_review/", "📋 周复盘"),
    ("/daily-news-insight/weekly_outlook/", "🔮 周三前瞻"),
    ("/daily-news-insight/weekend_express/", "🎉 周末速递"),
    ("/daily-news-insight/monthly/", "📅 月度报告"),
]

def build_nav():
    links = ""
    for item in NAV_ITEMS:
        if len(item)==3:
            url,label,_=item; active="active"
        else:
            url,label=item; active=""
        links += f'<a href="{url}" class="{active}">{label}</a>'
    mlinks = ""
    for item in NAV_ITEMS:
        if len(item)==3:
            url,label,_=item; active="active"
        else:
            url,label=item; active=""
        mlinks += f'<a href="{url}" class="{active}" onclick="document.getElementById(\'mobileMenu\').classList.remove(\'open\')">{label}</a>'
    return f"""
<nav class="glass-nav">
  <div class="nav-inner">
    <a href="/daily-news-insight/" class="nav-brand">
      <span class="nav-brand-icon">📊</span>
      <span>洞察研报中心</span>
    </a>
    <div class="nav-links">{links}</div>
    <button class="hamburger-btn" onclick="document.getElementById('mobileMenu').classList.add('open')">
      <i class="fa fa-bars"></i>
    </button>
  </div>
</nav>
<div id="mobileMenu" class="mobile-menu">
  <button class="close-menu-btn" onclick="document.getElementById('mobileMenu').classList.remove('open')">
    <i class="fa fa-times"></i>
  </button>
  {mlinks}
</div>
"""

CSS = """
:root{--primary:#6366f1;--secondary:#a855f7;--accent:#f59e0b;--red:#ef4444;--green:#22c55e;--bg:#0b0820;--bg2:#12102d;--bg3:#1e1b4b;--text:#e5e7eb;--muted:#9ca3af;--border:rgba(255,255,255,0.1);}
*{box-sizing:border-box;}
body{margin:0;background:linear-gradient(180deg,#0b0820 0%,#12102d 50%,#0b0820 100%);color:var(--text);font-family:-apple-system,BlinkMacSystemFont,"Segoe UI","PingFang SC","Hiragino Sans GB","Microsoft YaHei",sans-serif;line-height:1.8;min-height:100vh;}
.glass-nav{position:fixed;top:0;left:0;right:0;z-index:2147483647;background:rgba(15,12,41,0.78);backdrop-filter:blur(30px);-webkit-backdrop-filter:blur(30px);border-bottom:1px solid var(--border);}
.nav-inner{max-width:1320px;margin:0 auto;padding:0 1.25rem;height:64px;display:flex;align-items:center;justify-content:space-between;}
.nav-brand{font-size:1.1rem;font-weight:700;color:#fff;text-decoration:none;display:flex;align-items:center;gap:8px;white-space:nowrap;}
.nav-brand:hover{color:#c4b5fd;}
.nav-brand-icon{width:32px;height:32px;border-radius:8px;background:linear-gradient(135deg,#6366f1,#a855f7);display:flex;align-items:center;justify-content:center;font-size:15px;}
.nav-links{display:flex;gap:4px;flex-wrap:wrap;}
.nav-links a{color:rgba(255,255,255,0.72);text-decoration:none;padding:7px 12px;border-radius:8px;font-size:.85rem;transition:all .2s;white-space:nowrap;}
.nav-links a:hover{background:rgba(255,255,255,0.1);color:#fff;}
.nav-links a.active{background:rgba(255,255,255,0.18);color:#fff;font-weight:600;box-shadow:0 0 0 1px rgba(167,139,250,0.35);}
.hamburger-btn{display:none;background:transparent;border:none;color:#fff;font-size:1.4rem;cursor:pointer;}
.mobile-menu{display:none;position:fixed;inset:0;background:rgba(15,12,41,0.97);z-index:2147483646;flex-direction:column;padding:80px 24px 24px;gap:6px;overflow-y:auto;}
.mobile-menu.open{display:flex;}
.mobile-menu a{color:#fff;text-decoration:none;padding:14px 18px;border-radius:12px;font-size:1rem;background:rgba(255,255,255,0.05);}
.mobile-menu a.active{background:rgba(167,139,250,0.25);}
.close-menu-btn{position:absolute;top:20px;right:24px;background:transparent;border:none;color:#fff;font-size:1.8rem;cursor:pointer;}
@media(max-width:900px){.nav-links{display:none;}.hamburger-btn{display:block;}}

.container{max-width:1100px;margin:0 auto;padding:84px 24px 60px;}
.hero{background:linear-gradient(135deg,rgba(99,102,241,0.25),rgba(168,85,247,0.2),rgba(239,68,68,0.15));border:1px solid var(--border);border-radius:20px;padding:48px 40px;margin-bottom:32px;position:relative;overflow:hidden;}
.hero::before{content:"";position:absolute;top:-50%;right:-20%;width:600px;height:600px;background:radial-gradient(circle,rgba(168,85,247,0.15),transparent 70%);pointer-events:none;}
.hero-tag{display:inline-block;background:rgba(239,68,68,0.25);color:#fca5a5;border:1px solid rgba(239,68,68,0.4);padding:6px 16px;border-radius:20px;font-size:0.85rem;font-weight:600;margin-bottom:16px;}
.hero h1{font-size:2.4rem;margin:0 0 12px;background:linear-gradient(90deg,#fff,#c4b5fd);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;font-weight:800;}
.hero .subtitle{font-size:1.1rem;color:#c4b5fd;margin:0 0 24px;}
.kpi-row{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:16px;margin-top:24px;}
.kpi{background:rgba(15,12,41,0.6);border:1px solid var(--border);border-radius:12px;padding:16px;}
.kpi-label{color:var(--muted);font-size:0.8rem;margin-bottom:4px;}
.kpi-value{font-size:1.4rem;font-weight:700;color:#fff;}
.kpi-value.red{color:#fca5a5;}
.kpi-value.green{color:#86efac;}
.kpi-value.amber{color:#fcd34d;}

.tldr{background:rgba(245,158,11,0.08);border:1px solid rgba(245,158,11,0.3);border-radius:12px;padding:20px 24px;margin-bottom:32px;}
.tldr-title{color:#fcd34d;font-weight:700;font-size:1.05rem;margin-bottom:12px;display:flex;align-items:center;gap:8px;}

h1.report-title{font-size:2rem;color:#fff;border-bottom:2px solid var(--primary);padding-bottom:12px;margin-top:48px;}
h2{font-size:1.6rem;color:#fff;margin:48px 0 20px;padding:12px 20px;background:linear-gradient(90deg,rgba(99,102,241,0.2),transparent);border-left:4px solid var(--primary);border-radius:4px;}
h3{font-size:1.25rem;color:#c4b5fd;margin:32px 0 16px;}
h4{font-size:1.1rem;color:#a5b4fc;margin:24px 0 12px;}
p{color:var(--text);margin:0 0 14px;}
strong{color:#fff;font-weight:600;}
em{color:#fcd34d;font-style:normal;}
blockquote{border-left:4px solid var(--accent);background:rgba(245,158,11,0.08);margin:16px 0;padding:12px 20px;border-radius:0 8px 8px 0;color:#fde68a;}
ul,ol{padding-left:24px;margin:12px 0;}
li{margin:8px 0;color:var(--text);}
a{color:#a5b4fc;text-decoration:none;}
a:hover{color:#c4b5fd;text-decoration:underline;}
hr{border:none;border-top:1px solid var(--border);margin:40px 0;}

table{width:100%;border-collapse:collapse;margin:20px 0;background:rgba(15,12,41,0.4);border-radius:8px;overflow:hidden;font-size:0.92rem;}
th{background:rgba(99,102,241,0.25);color:#fff;padding:12px 14px;text-align:left;font-weight:600;border-bottom:2px solid var(--primary);}
td{padding:10px 14px;border-bottom:1px solid var(--border);color:var(--text);}
tr:hover td{background:rgba(168,85,247,0.08);}
tr:last-child td{border-bottom:none;}

img.chart{max-width:100%;border-radius:12px;margin:20px 0;border:1px solid var(--border);box-shadow:0 8px 32px rgba(99,102,241,0.15);}

code{background:rgba(168,85,247,0.15);color:#c4b5fd;padding:2px 8px;border-radius:4px;font-size:0.9em;}

.warning-box{background:rgba(239,68,68,0.1);border:1px solid rgba(239,68,68,0.3);border-radius:10px;padding:16px 20px;margin:16px 0;}
.warning-box .title{color:#fca5a5;font-weight:700;margin-bottom:8px;}
.success-box{background:rgba(34,197,94,0.1);border:1px solid rgba(34,197,94,0.3);border-radius:10px;padding:16px 20px;margin:16px 0;}
.success-box .title{color:#86efac;font-weight:700;margin-bottom:8px;}

.footer{margin-top:60px;padding:24px;border-top:1px solid var(--border);text-align:center;color:var(--muted);font-size:0.9rem;}

.toc{background:rgba(15,12,41,0.5);border:1px solid var(--border);border-radius:12px;padding:20px 28px;margin:24px 0 40px;}
.toc-title{font-weight:700;color:#fff;font-size:1.1rem;margin-bottom:12px;}
.toc ol{padding-left:20px;columns:2;}
@media(max-width:700px){.toc ol{columns:1;}.hero{padding:28px 20px;}.hero h1{font-size:1.7rem;}}

.strategy-card{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:12px;margin:20px 0;}
.strategy-item{background:linear-gradient(135deg,rgba(99,102,241,0.15),rgba(168,85,247,0.08));border:1px solid var(--border);border-radius:10px;padding:14px 16px;}
.strategy-item .price{font-size:1.2rem;font-weight:700;color:#fff;}
.strategy-item .action{color:#fcd34d;font-size:0.9rem;margin:6px 0;}
.strategy-item .note{color:var(--muted);font-size:0.85rem;}
"""

def render_md(md:str)->str:
    """简化的 markdown -> HTML，支持标题/列表/表格/粗体/引用/图片/分隔线"""
    lines = md.split('\n')
    out = []
    i = 0
    in_table = False
    table_rows = []
    in_list = False
    list_type = None
    in_para = False
    para_buf = []

    def flush_para():
        nonlocal para_buf, in_para
        if para_buf:
            text = ' '.join(para_buf)
            text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
            text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2" target="_blank">\1</a>', text)
            text = re.sub(r'`([^`]+)`', r'<code>\1</code>', text)
            out.append(f'<p>{text}</p>')
            para_buf = []
            in_para = False

    def flush_list():
        nonlocal in_list, list_type
        if in_list:
            tag = 'ul' if list_type=='ul' else 'ol'
            out.append(f'</{tag}>')
            in_list = False

    def flush_table():
        nonlocal table_rows, in_table
        if in_table and table_rows:
            html = '<table>'
            for ri,row in enumerate(table_rows):
                cells = [c.strip() for c in row.strip('|').split('|')]
                # Skip separator row
                if ri==1 and all(re.match(r'^[\s:-]+$',c) for c in cells):
                    continue
                tag = 'th' if ri==0 else 'td'
                cells_html = ''
                for c in cells:
                    c2 = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', c)
                    c2 = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2" target="_blank">\1</a>', c2)
                    cells_html += f'<{tag}>{c2}</{tag}>'
                html += f'<tr>{cells_html}</tr>'
            html += '</table>'
            out.append(html)
            table_rows = []
            in_table = False

    while i < len(lines):
        ln = lines[i]
        s = ln.strip()

        # Table
        if s.startswith('|') and s.endswith('|'):
            flush_para(); flush_list()
            in_table = True
            table_rows.append(s)
            i += 1
            continue
        elif in_table:
            flush_table()

        # Headings
        m = re.match(r'^(#{1,6})\s+(.*)$', s)
        if m:
            flush_para(); flush_list()
            lvl = len(m.group(1))
            txt = m.group(2)
            if lvl==1:
                out.append(f'<h1 class="report-title">{txt}</h1>')
            elif lvl==2:
                out.append(f'<h2>{txt}</h2>')
            elif lvl==3:
                out.append(f'<h3>{txt}</h3>')
            else:
                out.append(f'<h{lvl}>{txt}</h{lvl}>')
            i += 1
            continue

        # Blockquote
        if s.startswith('>'):
            flush_para(); flush_list()
            qt = s.lstrip('>').strip()
            qt = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', qt)
            out.append(f'<blockquote>{qt}</blockquote>')
            i += 1
            continue

        # HR
        if s == '---':
            flush_para(); flush_list()
            out.append('<hr>')
            i += 1
            continue

        # Image  ![](./xxx/01_kline.png)
        m = re.match(r'^!\[([^\]]*)\]\(([^)]+)\)', s)
        if m:
            flush_para(); flush_list()
            alt, src = m.group(1), m.group(2)
            # rewrite relative chart paths
            if src.startswith('./雅克科技深度研究_assets/'):
                fname = src.split('/')[-1]
                src = f'assets/yake_20260720/{fname}'
            out.append(f'<img class="chart" src="{src}" alt="{html_mod.escape(alt)}">')
            i += 1
            continue

        # List
        m = re.match(r'^[-*]\s+(.*)$', s)
        if m:
            flush_para()
            if not in_list or list_type!='ul':
                flush_list()
                out.append('<ul>')
                in_list=True; list_type='ul'
            item = m.group(1)
            item = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', item)
            item = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2" target="_blank">\1</a>', item)
            out.append(f'<li>{item}</li>')
            i += 1
            continue
        m = re.match(r'^(\d+)\.\s+(.*)$', s)
        if m:
            flush_para()
            if not in_list or list_type!='ol':
                flush_list()
                out.append('<ol>')
                in_list=True; list_type='ol'
            item = m.group(2)
            item = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', item)
            item = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2" target="_blank">\1</a>', item)
            out.append(f'<li>{item}</li>')
            i += 1
            continue

        # Empty line
        if not s:
            flush_para(); flush_list()
            i += 1
            continue

        # Paragraph
        flush_list()
        para_buf.append(s)
        in_para = True
        i += 1

    flush_para(); flush_list(); flush_table()
    return '\n'.join(out)

def build_hero():
    return """
<div class="hero">
  <div class="hero-tag">⚠️ 持仓深度决策 · 跌停后紧急复盘</div>
  <h1>雅克科技(002409.SZ) 深度研究报告</h1>
  <p class="subtitle">HBM泡沫破裂之后：价值重估还是价值陷阱？</p>
  <div class="kpi-row">
    <div class="kpi"><div class="kpi-label">最新股价 (7/20收盘)</div><div class="kpi-value red">130.50 元 跌停 -10%</div></div>
    <div class="kpi"><div class="kpi-label">距高点回撤</div><div class="kpi-value red">-47.04% (246.44→130.50)</div></div>
    <div class="kpi"><div class="kpi-label">总市值</div><div class="kpi-value amber">≈ 622 亿元</div></div>
    <div class="kpi"><div class="kpi-label">TTM PE (2025 EPS 2.10)</div><div class="kpi-value">62.1x</div></div>
    <div class="kpi"><div class="kpi-label">持仓成本</div><div class="kpi-value green">108.8 元 (浮盈≈20%)</div></div>
    <div class="kpi"><div class="kpi-label">评级</div><div class="kpi-value amber">中性偏观望</div></div>
  </div>
</div>
"""

def build_tldr():
    return """
<div class="tldr">
  <div class="tldr-title">🎯 核心结论速览</div>
  <p><strong>短期(1-4周)：</strong>技术面严重超卖但情绪未稳，不排除继续探底MA120=112元一线；融资盘强平风险未释放完毕。</p>
  <p><strong>中期(3-6月)：</strong>HBM4逻辑未死但已切换到业绩验证期。中性预期2026年归母13-15亿（对应PE 41-48x），乐观20亿+预期兑现概率&lt;15%。</p>
  <p><strong>长期(1-3年)：</strong>半导体材料平台雏形已现，LNG+前驱体+光刻胶三驾马车成型，但21亿商誉+41%资产负债率构成天花板。</p>
  <p><strong>操作建议：</strong>底仓30%不割肉，反弹140-160分3批减仓50%机动仓，等115-120元(MA120)再评估；严格止损105元。<strong>跌停日不抄底</strong>。</p>
</div>
"""

def main():
    md = MD_PATH.read_text(encoding='utf-8')
    # 切掉最头部的# H1+##副标题+>块引用+---，hero已展示这些信息
    # 找第一个---之后的正文起点
    m = re.search(r'^---\s*$', md, flags=re.MULTILINE)
    if m:
        md = md[m.end():]
    body_html = render_md(md)

    nav = build_nav()
    hero = build_hero()
    tldr = build_tldr()

    meta_tags = """
    <meta name="description" content="雅克科技(002409) 深度研究报告：HBM泡沫破裂之后，14个交易日-47%跌停复盘。覆盖公司全景/业务拆解/HBM绑定/财务/估值/337调查/技术面/风险/操作策略。">
    <meta name="keywords" content="雅克科技,002409,HBM前驱体,SK海力士,HBM4,337调查,半导体材料,跌停复盘,持仓分析">
    <meta property="og:title" content="🧪 雅克科技(002409) 深度研究报告 - 洞察研报中心">
    <meta property="og:description" content="14交易日-47%跌停深度复盘：HBM逻辑未死但泡沫已破，给持仓者的全套操作策略。">
    <meta property="og:type" content="article">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.5.1/css/all.min.css">
"""
    footer = """
<div class="footer">
  <p>本报告基于公开信息撰写，不构成任何投资建议。数据截至2026-07-20收盘。股市有风险，投资需谨慎。</p>
  <p>© 2026 洞察研报中心 · 产业链频道 · <a href="/daily-news-insight/">返回首页</a></p>
</div>
"""

    html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🧪 雅克科技(002409) 深度研究报告 - 洞察研报中心</title>
    {meta_tags}
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
{CSS}
    </style>
</head>
<body>
{nav}
<div class="container">
    {hero}
    {tldr}
    {body_html}
    {footer}
</div>
</body>
</html>
"""
    OUT.write_text(html, encoding='utf-8')
    size = OUT.stat().st_size
    print(f"✅ 生成: {OUT}")
    print(f"   大小: {size:,} 字节 ({size/1024:.1f} KB)")

if __name__=="__main__":
    main()
