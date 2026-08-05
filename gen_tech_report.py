#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""将科技板块反弹龙头深度调研报告MD转换为深色玻璃态HTML（沿用HBF模板）"""
import re, os, sys, html
from pathlib import Path

MD_PATH = "/app/data/所有对话/主对话/科技板块反弹龙头调研_report.md"
OUT_PATH = "/root/daily-news-insight/docs/industry_chain/20260805_科技反弹龙头深度研究.html"

CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@300;400;500;700;900&display=swap');
*{font-family:'Noto Sans SC',sans-serif;}
html{scroll-behavior:smooth;}
body{background:linear-gradient(135deg,#0f0c29 0%,#1a1740 35%,#302b63 65%,#24243e 100%)!important;min-height:100vh;color:rgba(255,255,255,.95);}
.pro-container{max-width:64rem;margin:0 auto;padding:0 1.25rem;}
.hero{position:relative;padding:5rem 1.25rem 3rem;text-align:center;overflow:hidden;}
.hero::before{content:"";position:absolute;inset:0;background:radial-gradient(ellipse at 20% 30%,rgba(99,102,241,.25),transparent 60%),radial-gradient(ellipse at 80% 70%,rgba(168,85,247,.22),transparent 60%),radial-gradient(ellipse at 50% 100%,rgba(236,72,153,.15),transparent 70%);pointer-events:none;}
.hero-title{font-size:clamp(1.8rem,4.2vw,2.8rem);font-weight:900;background:linear-gradient(120deg,#fff 0%,#c7d2fe 40%,#a78bfa 70%,#f0abfc 100%);-webkit-background-clip:text;background-clip:text;color:transparent;line-height:1.25;margin-bottom:1rem;}
.hero-sub{font-size:1.05rem;color:rgba(255,255,255,.78);margin-bottom:1.25rem;}
.hero-meta{display:inline-flex;flex-wrap:wrap;gap:.5rem;justify-content:center;}
.hero-chip{padding:.35rem .8rem;background:rgba(255,255,255,.07);border:1px solid rgba(255,255,255,.12);border-radius:999px;font-size:.8rem;color:rgba(255,255,255,.78);backdrop-filter:blur(12px);}
.hero-chip.accent{background:linear-gradient(120deg,rgba(99,102,241,.25),rgba(168,85,247,.25));border-color:rgba(139,92,246,.45);color:#e9d5ff;}
.card-glass{background:rgba(255,255,255,.06)!important;backdrop-filter:blur(24px);-webkit-backdrop-filter:blur(24px);border:1px solid rgba(255,255,255,.10)!important;box-shadow:0 12px 40px rgba(0,0,0,.45);border-radius:22px;color:rgba(255,255,255,.95)!important;padding:1.75rem 1.5rem;margin-bottom:1.5rem;}
@media(min-width:768px){.card-glass{padding:2.25rem 2.5rem;}}
.card-glass .text-gray-800,.card-glass .text-gray-700{color:rgba(255,255,255,.92)!important;}
.card-glass .text-gray-600,.card-glass .text-gray-500{color:rgba(255,255,255,.7)!important;}
.table-wrap{overflow-x:auto;margin:1rem 0;border-radius:12px;border:1px solid rgba(255,255,255,.1);}
table.glass-table{width:100%;border-collapse:collapse;font-size:.9rem;}
table.glass-table thead th{background:linear-gradient(135deg,rgba(99,102,241,.22),rgba(139,92,246,.22));color:#fff;font-weight:600;text-align:left;padding:.75rem .9rem;border-bottom:1px solid rgba(255,255,255,.15);white-space:nowrap;}
table.glass-table tbody td{padding:.7rem .9rem;border-bottom:1px solid rgba(255,255,255,.06);color:rgba(255,255,255,.82);vertical-align:top;}
table.glass-table tbody tr:hover{background:rgba(255,255,255,.04);}
table.glass-table tbody tr:nth-child(even) td{background:rgba(255,255,255,.02);}
.strategy-card{background:linear-gradient(135deg,rgba(16,185,129,.10),rgba(59,130,246,.10));border:1px solid rgba(16,185,129,.30);border-radius:14px;padding:1rem 1.25rem;margin:1rem 0;}
.strategy-card.warn{background:linear-gradient(135deg,rgba(239,68,68,.10),rgba(251,146,60,.10));border-color:rgba(239,68,68,.30);}
.strategy-card.hold{background:linear-gradient(135deg,rgba(59,130,246,.10),rgba(139,92,246,.10));border-color:rgba(59,130,246,.30);}
.price-tag{display:inline-block;padding:.15rem .55rem;border-radius:6px;font-size:.85rem;font-weight:600;margin:0 .15rem;}
.price-tag.buy{background:rgba(16,185,129,.25);color:#6ee7b7;border:1px solid rgba(16,185,129,.4);}
.price-tag.target{background:rgba(59,130,246,.25);color:#93c5fd;border:1px solid rgba(59,130,246,.4);}
.price-tag.stop{background:rgba(239,68,68,.25);color:#fca5a5;border:1px solid rgba(239,68,68,.4);}
.stock-name{color:#fde68a;font-weight:600;}
.toc-card{position:sticky;top:80px;background:rgba(255,255,255,.04);border:1px solid rgba(255,255,255,.08);border-radius:16px;padding:1rem 1.1rem;max-height:calc(100vh - 100px);overflow-y:auto;}
.toc-title{font-size:.95rem;font-weight:700;color:#fff;margin-bottom:.75rem;display:flex;align-items:center;gap:.4rem;}
.toc-h2{display:block;padding:.3rem .4rem;color:rgba(255,255,255,.85);font-size:.85rem;font-weight:500;border-radius:6px;text-decoration:none;}
.toc-h2:hover{background:rgba(99,102,241,.18);color:#fff;}
.toc-h3{display:block;padding:.2rem .4rem .2rem 1rem;color:rgba(255,255,255,.6);font-size:.78rem;border-radius:6px;text-decoration:none;}
.toc-h3:hover{background:rgba(255,255,255,.05);color:rgba(255,255,255,.88);}
.glass-nav{background:rgba(15,12,41,.72)!important;backdrop-filter:blur(30px);-webkit-backdrop-filter:blur(20px);border-bottom:1px solid rgba(255,255,255,.08);}
.nav-link{padding:.4rem .75rem;border-radius:8px;font-size:.85rem;color:rgba(255,255,255,.78);transition:all .2s;display:inline-block;text-decoration:none;}
.nav-link:hover{color:#fff;background:rgba(255,255,255,.08);}
.nav-link.active{color:#fff;background:rgba(255,255,255,.15);}
.history-entry-wrap{margin:2.5rem auto 1rem;text-align:center;}
.history-entry-link{display:inline-flex;align-items:center;gap:.5rem;padding:.7rem 1.4rem;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.14);border-radius:999px;color:rgba(255,255,255,.82);font-size:.92rem;font-weight:500;text-decoration:none;backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px);box-shadow:0 6px 20px rgba(0,0,0,.25);transition:all .25s ease;}
.history-entry-link:hover{background:rgba(102,126,234,.22);border-color:rgba(139,92,246,.45);color:#fff;transform:translateY(-1px);box-shadow:0 10px 28px rgba(102,126,234,.35);}
.float-actions{position:fixed;right:1.25rem;bottom:1.5rem;z-index:40;display:flex;flex-direction:column;gap:.6rem;}
.float-btn{width:44px;height:44px;border-radius:50%;background:rgba(255,255,.08);border:1px solid rgba(255,255,.18);color:#fff;display:flex;align-items:center;justify-content:center;cursor:pointer;backdrop-filter:blur(16px);box-shadow:0 8px 20px rgba(0,0,0,.35);transition:all .2s;font-size:16px;}
.float-btn:hover{background:rgba(99,102,241,.35);border-color:rgba(139,92,246,.5);transform:translateY(-2px);}
#progressBar{position:fixed;top:0;left:0;height:3px;background:linear-gradient(90deg,#6366f1,#a855f7,#ec4899);z-index:9999;width:0%;transition:width .08s ease;}
.score-badge{display:inline-block;padding:.15rem .5rem;border-radius:6px;font-weight:700;font-size:.85rem;background:linear-gradient(120deg,rgba(251,191,36,.25),rgba(245,158,11,.25));color:#fcd34d;border:1px solid rgba(251,191,36,.4);}
.tier-badge{display:inline-block;padding:.2rem .6rem;border-radius:8px;font-weight:700;font-size:.8rem;margin-right:.4rem;}
.tier-1{background:linear-gradient(120deg,rgba(239,68,68,.25),rgba(220,38,38,.25));color:#fca5a5;border:1px solid rgba(239,68,68,.45);}
.tier-2{background:linear-gradient(120deg,rgba(251,146,60,.25),rgba(245,158,11,.25));color:#fdba74;border:1px solid rgba(251,146,60,.45);}
.tier-3{background:linear-gradient(120deg,rgba(148,163,184,.25),rgba(100,116,139,.25));color:#cbd5e1;border:1px solid rgba(148,163,184,.4);}
.warn-signal{display:inline-block;padding:.1rem .4rem;border-radius:4px;font-size:.8rem;font-weight:600;}
.warn-yellow{background:rgba(250,204,21,.2);color:#fde047;border:1px solid rgba(250,204,21,.4);}
.warn-red{background:rgba(239,68,68,.2);color:#fca5a5;border:1px solid rgba(239,68,68,.4);}
@media(max-width:1024px){.toc-col{display:none;}}
@media(max-width:640px){.hero{padding:4rem 1rem 2rem;}.card-glass{padding:1.25rem 1rem;border-radius:16px;}table.glass-table{font-size:.8rem;}}
img{max-width:100%;height:auto;border-radius:8px;}
sup{font-size:.7em;color:#a5b4fc;}
.blockquote{border-left:3px solid rgba(139,92,246,.55);padding:.6rem 1rem;margin:1rem 0;background:rgba(139,92,246,.08);border-radius:0 10px 10px 0;color:rgba(255,255,255,.75);font-style:italic;}
.content-body h2{scroll-margin-top:70px;}
.content-body h3{scroll-margin-top:70px;}
a{color:#a5b4fc;}
a:hover{color:#c7d2fe;}
</style>
"""

NAV = """
<nav class="fixed top-0 left-0 right-0 z-50 glass-nav">
<div class="max-w-6xl mx-auto px-4 py-3 flex items-center justify-between">
<div class="flex items-center gap-2.5">
<div class="w-8 h-8 rounded-lg bg-gradient-to-br from-indigo-500 to-purple-600 flex items-center justify-center"><span class="text-white text-sm font-bold">📊</span></div>
<span class="text-white font-bold text-lg">投资研究中心</span>
</div>
<div class="hidden md:flex items-center gap-1">
<a href="/daily-news-insight/index.html" class="nav-link">首页</a>
<a href="/daily-news-insight/daily/index.html" class="nav-link">日报</a>
<a href="/daily-news-insight/intraday/index.html" class="nav-link">盘中</a>
<a href="/daily-news-insight/aftermarket/index.html" class="nav-link">盘后</a>
<a href="/daily-news-insight/industry_chain/index.html" class="nav-link active">🔗 产业链</a>
<a href="/daily-news-insight/weekly_review/index.html" class="nav-link">周复盘</a>
<a href="/daily-news-insight/weekend_express/index.html" class="nav-link">周末速递</a>
<a href="/daily-news-insight/tomorrow_catalyst/index.html" class="nav-link">明日催化</a>
<a href="/daily-news-insight/s_level_catalyst/index.html" class="nav-link">S级催化</a>
</div>
<button class="md:hidden text-white text-xl px-2" onclick="document.getElementById('mMenu').classList.toggle('hidden')">☰</button>
</div>
<div id="mMenu" class="hidden md:hidden border-t border-white/10 px-4 py-3 space-y-1" style="background:rgba(15,12,41,.95);">
<a href="/daily-news-insight/index.html" class="block nav-link">🏠 首页</a>
<a href="/daily-news-insight/daily/index.html" class="block nav-link">日报</a>
<a href="/daily-news-insight/intraday/index.html" class="block nav-link">盘中</a>
<a href="/daily-news-insight/aftermarket/index.html" class="block nav-link">盘后</a>
<a href="/daily-news-insight/industry_chain/index.html" class="block nav-link active">🔗 产业链</a>
<a href="/daily-news-insight/weekly_review/index.html" class="block nav-link">周复盘</a>
<a href="/daily-news-insight/weekend_express/index.html" class="block nav-link">周末速递</a>
<a href="/daily-news-insight/tomorrow_catalyst/index.html" class="block nav-link">明日催化</a>
<a href="/daily-news-insight/s_level_catalyst/index.html" class="block nav-link">S级催化</a>
</div>
</nav>
"""

FLOAT_BTN = """
<div class="float-actions">
<button class="float-btn" onclick="window.scrollTo({top:0,behavior:'smooth'})" title="回到顶部">↑</button>
<button class="float-btn" onclick="navigator.clipboard.writeText(location.href).then(()=>alert('链接已复制'))" title="分享">🔗</button>
</div>
"""

FOOTER_SCRIPT = """
<script src="/daily-news-insight/assets/stock-popup.js"></script>
<script>
window.addEventListener('scroll',()=>{const h=document.documentElement;const pct=(h.scrollTop/(h.scrollHeight-h.clientHeight))*100;document.getElementById('progressBar').style.width=pct+'%';const nav=document.querySelector('.glass-nav');if(nav)nav.classList.toggle('scrolled',window.scrollY>10);},{passive:true});
</script>
"""

KEY_STOCKS = ['中微公司','胜宏科技','海光信息','风华高科','澜起科技','北方华创','中际旭创','雅克科技',
              '英维克','铜冠铜箔','*ST建艺','通富微电','江波龙','寒武纪','新易盛','沪电股份','佰维存储',
              '长电科技','太极实业','华海诚科']

# 关键词替换时要避免嵌套：先处理长名后短名
KEY_STOCKS_SORTED = sorted(KEY_STOCKS, key=len, reverse=True)


def md_inline(text: str) -> str:
    # 图片 ![alt](url)
    def img_repl(m):
        alt = html.escape(m.group(1))
        url = m.group(2)
        return f'<img src="{html.escape(url)}" alt="{alt}" loading="lazy"/>'
    text = re.sub(r'!\[([^\]]*)\]\(([^)]+)\)', img_repl, text)

    # 链接 [text](url)
    def link_repl(m):
        t = m.group(1)
        url = html.escape(m.group(2))
        # 链接内文本只处理加粗斜体代码，不处理股票高亮避免嵌套
        inner = t
        inner = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', inner)
        inner = re.sub(r'(?<!\*)\*([^*\n]+)\*(?!\*)', r'<em>\1</em>', inner)
        inner = re.sub(r'`([^`]+)`', r'<code class="px-1 py-0.5 rounded bg-white/10 text-pink-200 text-sm">\1</code>', inner)
        return f'<a href="{url}" target="_blank" rel="noopener" class="text-indigo-300 hover:text-indigo-200 underline decoration-indigo-400/40 underline-offset-2">{inner}</a>'
    text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', link_repl, text)

    # 加粗 **xx**
    text = re.sub(r'\*\*([^*]+)\]\([^)]+\)\*\*', lambda m: m.group(0), text)  # 安全，避免已在链接内
    text = re.sub(r'\*\*([^*]+)\*\*', r'<strong class="text-white/95 font-semibold">\1</strong>', text)
    # 斜体 *xx*
    text = re.sub(r'(?<![\*\w])\*([^*\n]+)\*(?!\*)', r'<em>\1</em>', text)
    # 行内代码
    text = re.sub(r'`([^`]+)`', r'<code class="px-1.5 py-0.5 rounded bg-white/10 text-pink-200 text-sm">\1</code>', text)
    # 评分加粗（如 90分、86分）
    text = re.sub(r'(\*\*)?(\d{2,3})分(\*\*)?', r'<span class="score-badge">\2分</span>', text)
    # 关键标的高亮
    for s in KEY_STOCKS_SORTED:
        # 简单替换，避免嵌套span
        if s in text:
            text = text.replace(s, f'§§STOCK_{s}§§')
    for s in KEY_STOCKS_SORTED:
        text = text.replace(f'§§STOCK_{s}§§', f'<span class="stock-name">{s}</span>')
    # 黄色/红色预警信号（先处理，避免标签嵌套干扰）
    text = text.replace('⚠️', '<span class="warn-signal warn-yellow">⚠️ 黄色预警</span>')
    text = text.replace('🔴', '<span class="warn-signal warn-red">🔴 红色预警</span>')
    return text


def parse_md(md: str):
    lines = md.split('\n')
    blocks = []
    i = 0
    in_table = False
    table_rows = []
    in_list = False
    list_type = None
    list_items = []
    in_blockquote = False
    bq_text = []

    def flush_list():
        nonlocal in_list, list_items, list_type
        if in_list and list_items:
            blocks.append(('list', list_type, list_items))
            in_list = False
            list_items = []
            list_type = None

    def flush_table():
        nonlocal in_table, table_rows
        if in_table and table_rows:
            blocks.append(('table', table_rows))
            in_table = False
            table_rows = []

    def flush_bq():
        nonlocal in_blockquote, bq_text
        if in_blockquote and bq_text:
            blocks.append(('blockquote', '\n'.join(bq_text)))
            in_blockquote = False
            bq_text = []

    while i < len(lines):
        line = lines[i].rstrip()
        if re.match(r'^---+\s*$', line):
            flush_list(); flush_table(); flush_bq()
            blocks.append(('hr',))
            i += 1; continue
        if line.startswith('> '):
            flush_list(); flush_table()
            if not in_blockquote:
                flush_bq(); in_blockquote = True; bq_text = []
            bq_text.append(line[2:])
            i += 1; continue
        else:
            flush_bq()
        m = re.match(r'^(#{1,4})\s+(.*)$', line)
        if m:
            flush_list(); flush_table()
            blocks.append(('h', len(m.group(1)), m.group(2).strip()))
            i += 1; continue
        if '|' in line and line.strip().startswith('|'):
            if not in_table:
                flush_list(); in_table = True; table_rows = []
            if re.match(r'^\|[\s\-:|]+\|\s*$', line):
                i += 1; continue
            cells = [c.strip() for c in line.strip().strip('|').split('|')]
            table_rows.append(cells)
            i += 1; continue
        else:
            flush_table()
        m_ul = re.match(r'^[\-\*]\s+(.*)$', line)
        m_ol = re.match(r'^(\d+)\.\s+(.*)$', line)
        if m_ul or m_ol:
            if not in_list:
                flush_list(); in_list = True; list_items = []; list_type = 'ol' if m_ol else 'ul'
            list_items.append(m_ol.group(2) if m_ol else m_ul.group(1))
            i += 1; continue
        else:
            flush_list()
        if re.match(r'^!\[', line.strip()):
            blocks.append(('p', line.strip()))
            i += 1; continue
        if line.strip() == '':
            i += 1; continue
        para = [line]
        j = i + 1
        while j < len(lines):
            nxt = lines[j].rstrip()
            if nxt.strip() == '' or re.match(r'^#{1,4}\s', nxt) or re.match(r'^---+\s*$', nxt) or \
               nxt.startswith('> ') or re.match(r'^[\-\*]\s+', nxt) or re.match(r'^\d+\.\s+', nxt) or \
               (nxt.strip().startswith('|') and '|' in nxt) or re.match(r'^!\[', nxt.strip()):
                break
            para.append(nxt); j += 1
        blocks.append(('p', ' '.join(para)))
        i = j
    flush_list(); flush_table(); flush_bq()
    return blocks


def anchor_id(title: str) -> str:
    return re.sub(r'[^\w\u4e00-\u9fa5]+', '', title)


def render_blocks(blocks):
    out = []
    toc = []
    i = 0
    while i < len(blocks):
        b = blocks[i]
        if b[0] == 'h':
            level, title = b[1], b[2]
            aid = anchor_id(title)
            if level == 1:
                i += 1; continue
            if level == 2:
                toc.append((2, aid, title))
                out.append(f'<hr class="border-white/10 my-8"/>')
                out.append(f'<h2 class="text-2xl font-bold text-white mb-4 mt-12 pb-3 border-b border-white/10 flex items-center gap-2" id="{aid}">')
                out.append(f'<span class="w-1 h-7 bg-gradient-to-b from-indigo-400 to-purple-500 rounded-full flex-shrink-0"></span>{html.escape(title)}</h2>')
            elif level == 3:
                toc.append((3, aid, title))
                out.append(f'<h3 class="text-xl font-semibold text-white/95 mb-3 mt-8 pl-3 border-l-4 border-indigo-400/70" id="{aid}">{html.escape(title)}</h3>')
            elif level == 4:
                out.append(f'<h4 class="text-lg font-semibold text-white/90 mb-2 mt-5">{html.escape(title)}</h4>')
            i += 1; continue
        if b[0] == 'hr':
            i += 1; continue
        if b[0] == 'p':
            out.append(f'<p class="text-white/75 leading-relaxed my-3">{md_inline(b[1])}</p>')
            i += 1; continue
        if b[0] == 'blockquote':
            out.append(f'<div class="blockquote">{md_inline(b[1])}</div>')
            i += 1; continue
        if b[0] == 'table':
            rows = b[1]
            t = ['<div class="table-wrap"><table class="glass-table"><thead><tr>']
            if rows:
                for c in rows[0]:
                    t.append(f'<th>{md_inline(c)}</th>')
                t.append('</tr></thead><tbody>')
                for r in rows[1:]:
                    t.append('<tr>')
                    for c in r:
                        t.append(f'<td>{md_inline(c)}</td>')
                    t.append('</tr>')
                t.append('</tbody>')
            t.append('</table></div>')
            out.append('\n'.join(t))
            i += 1; continue
        if b[0] == 'list':
            tag, items = b[1], b[2]
            out.append(f'<{tag} class="list-{"disc" if tag=="ul" else "decimal"} list-outside pl-6 space-y-2 my-3 text-white/75">')
            for it in items:
                out.append(f'<li class="leading-relaxed">{md_inline(it)}</li>')
            out.append(f'</{tag}>')
            i += 1; continue
        i += 1
    return '\n'.join(out), toc


def post_process_price_tags(html_text: str) -> str:
    """对生成后的HTML做关键价位标签高亮"""
    label_map = {
        '最佳买点': ('buy', '🎯 买点'),
        '第一目标价': ('target', '🎯 第一目标'),
        '第二目标价': ('target', '🎯 第二目标'),
        '止损位': ('stop', '🛑 止损位'),
    }
    for label, (cls, display) in label_map.items():
        # 匹配 <strong ...>最佳买点</strong>：XXX</li>
        pattern = re.compile(
            r'<strong class="text-white/95 font-semibold">' + re.escape(label) + r'</strong>：([^<]+)</li>'
        )
        def repl(m, cls=cls, display=display):
            content = m.group(1)
            return (f'<span class="price-tag {cls}">{display}</span>'
                    f'<span class="text-white/85">：{content}</span></li>')
        html_text = pattern.sub(repl, html_text)
    # 为风险信号表中⚠️/🔴添加样式（表格单元格中的）
    html_text = html_text.replace('<td>⚠️', '<td><span class="warn-signal warn-yellow">⚠️ 黄色</span>')
    html_text = html_text.replace('<td>🔴', '<td><span class="warn-signal warn-red">🔴 红色</span>')
    return html_text


def build_html(md_text: str) -> str:
    blocks = parse_md(md_text)
    body, toc = render_blocks(blocks)
    toc_html = ['<div class="toc-card"><div class="toc-title"><span>📑</span>目录导航</div>']
    for lvl, aid, title in toc:
        esc = html.escape(title)
        cls = 'toc-h2' if lvl == 2 else 'toc-h3'
        toc_html.append(f'<a href="#{aid}" class="{cls}">{esc}</a>')
    toc_html.append('</div>')
    toc_sidebar = '\n'.join(toc_html)

    hero = """
    <section class="hero">
      <h1 class="hero-title">科技板块反弹龙头深度调研</h1>
      <p class="hero-sub">风华高科 &amp; 科技全赛道反弹龙头候选 · TOP10评分+操作策略</p>
      <div class="hero-meta">
        <span class="hero-chip accent">📅 2026年8月5日</span>
        <span class="hero-chip">🔥 费城半导体+6.55% · 科创50五连阳</span>
        <span class="hero-chip">🏆 TOP1：中微公司 90分</span>
        <span class="hero-chip">💡 MLCC/AI算力/PCB/半导体设备</span>
      </div>
    </section>
    """
    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0">
<meta name="theme-color" content="#0f0c29">
<title>科技板块反弹龙头深度调研 - 投资研究中心</title>
<meta name="description" content="2026.08.05 · 科技反弹龙头TOP10评分+关键标的操作策略·风华高科深度分析">
<meta property="og:title" content="科技板块反弹龙头深度调研">
<meta property="og:description" content="2026.08.05 · 科技反弹龙头TOP10评分+关键标的操作策略">
<meta property="og:image" content="/daily-news-insight/assets/default-og.png">
<meta property="og:type" content="article">
<script src="https://cdn.tailwindcss.com"></script>
<link rel="stylesheet" href="/daily-news-insight/assets/global-dark.css">
<link rel="stylesheet" href="/daily-news-insight/assets/stock-popup.css">
{CSS}
</head>
<body>
<div id="progressBar"></div>
{NAV}
<main class="pt-16">
<div class="pro-container">
<div class="grid grid-cols-1 lg:grid-cols-[1fr_240px] gap-6">
<div class="content-body">
{hero}
<div class="card-glass">
{body}
<hr class="border-white/10 my-8"/>
<p class="text-white/75 leading-relaxed my-3"><em>风险提示：本报告基于公开市场信息和历史数据进行研究分析，所有观点和判断仅供参考，不构成任何投资建议。股市有风险，投资需谨慎。投资者应根据自身风险承受能力独立做出投资决策。</em></p>
<hr class="border-white/10 my-8"/>
<p class="text-white/75 leading-relaxed my-3">
<strong class="text-white/95">报告字数</strong>：约1.5万字<br/>
<strong class="text-white/95">报告类型</strong>：科技板块反弹龙头深度调研 / 龙头战法操作策略<br/>
<strong class="text-white/95">数据截止</strong>：2026年8月5日收盘
</p>
<div class="history-entry-wrap">
<a href="./latest.html" class="history-entry-link">
<span>🔗</span><span>返回产业链总览</span><span style="opacity:.75">→</span>
</a>
</div>
<div class="text-center text-white/40 text-sm py-6">
<p>科技板块反弹龙头深度调研 · 2026年8月5日</p>
<p class="text-xs mt-2">数据来源：腾讯自选股、上交所公告、东方财富等公开信息整理 · 仅作研究参考，不构成投资建议</p>
</div>
</div>
</div>
<aside class="toc-col">{toc_sidebar}</aside>
</div>
</div>
</main>
{FLOAT_BTN}
{FOOTER_SCRIPT}
</body>
</html>"""


def main():
    md = Path(MD_PATH).read_text(encoding='utf-8')
    md = re.sub(r'^#\s+科技板块反弹龙头深度调研报告\s*\n+', '', md)
    html_text = build_html(md)
    html_text = post_process_price_tags(html_text)
    Path(OUT_PATH).write_text(html_text, encoding='utf-8')
    sz = os.path.getsize(OUT_PATH)
    print(f"OK: {OUT_PATH}")
    print(f"SIZE: {sz} bytes ({sz/1024:.1f} KB)")


if __name__ == '__main__':
    main()
