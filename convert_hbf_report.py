#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Convert HBF Markdown report to dark glass-style HTML page matching reference template.
"""
import re
import html as html_mod
from pathlib import Path

MD_PATH = Path("/app/data/所有对话/主对话/HBF产业链深度研究_report.md")
OUT_PATH = Path("/root/daily-news-insight/docs/industry_chain/20260804_HBF高带宽闪存产业链深度研究.html")


def slugify(text: str) -> str:
    s = re.sub(r"\s+", "", text)
    return s


def inline_md(text: str) -> str:
    out = html_mod.escape(text, quote=False)
    # images
    def img_repl(m):
        alt = m.group(1); url = m.group(2)
        alt_e = html_mod.escape(alt, quote=True)
        return f'<img src="{url}" alt="{alt_e}" style="max-width:100%;border-radius:10px;margin:1rem 0;box-shadow:0 8px 24px rgba(0,0,0,.35);" loading="lazy"/>'
    out = re.sub(r"!\[([^\]]*)\]\(([^)\s]+)\)", img_repl, out)
    # links
    def link_repl(m):
        t = m.group(1); u = m.group(2)
        return f'<a href="{u}" target="_blank" rel="noopener" class="text-indigo-300 hover:text-indigo-200 underline decoration-indigo-400/40 underline-offset-2">{t}</a>'
    out = re.sub(r"\[([^\]]+)\]\((https?://[^)\s]+)\)", link_repl, out)
    # bold **
    out = re.sub(r"\*\*([^*]+)\*\*", r'<strong class="text-white/95 font-semibold">\1</strong>', out)
    out = re.sub(r"__([^_]+)__", r'<strong class="text-white/95 font-semibold">\1</strong>', out)
    # italic *
    out = re.sub(r"(?<!\*)\*([^*\n]+)\*(?!\*)", r"<em>\1</em>", out)
    # inline code
    out = re.sub(r"`([^`]+)`", r'<code style="background:rgba(255,255,255,.08);padding:.15rem .35rem;border-radius:4px;font-size:.88em;color:#e9d5ff;">\1</code>', out)
    return out


def parse_md(md: str):
    blocks = []
    lines = md.split("\n")
    i = 0
    n = len(lines)
    while i < n:
        line = lines[i]
        stripped = line.rstrip()
        if not stripped.strip():
            i += 1; continue
        if stripped.strip() == "---":
            blocks.append(("hr",)); i += 1; continue
        if stripped.startswith("# "):
            i += 1; continue
        if stripped.startswith("## "):
            text = stripped[3:].strip()
            blocks.append(("h2", slugify(text), text)); i += 1; continue
        if stripped.startswith("### "):
            text = stripped[4:].strip()
            blocks.append(("h3", slugify(text), text)); i += 1; continue
        if stripped.startswith("> "):
            qlines = []
            while i < n and lines[i].startswith(">"):
                q = re.sub(r"^>\s?", "", lines[i].rstrip())
                qlines.append(q); i += 1
            blocks.append(("quote", qlines)); continue
        # table
        if "|" in stripped and i + 1 < n and re.match(r"^\s*\|?\s*:?-+:?\s*(\|\s*:?-+:?\s*)+\|?\s*$", lines[i+1]):
            headers = [c.strip() for c in stripped.strip().strip("|").split("|")]
            rows = []; i += 2
            while i < n and "|" in lines[i] and lines[i].strip():
                row = [c.strip() for c in lines[i].strip().strip("|").split("|")]
                if len(row) < len(headers):
                    row += [""] * (len(headers) - len(row))
                rows.append(row[:len(headers)]); i += 1
            blocks.append(("table", headers, rows)); continue
        m_ul = re.match(r"^\s*[-*]\s+(.*)$", stripped)
        m_ol = re.match(r"^\s*\d+\.\s+(.*)$", stripped)
        if m_ul:
            items = []
            while i < n:
                m = re.match(r"^\s*[-*]\s+(.*)$", lines[i].rstrip())
                if not m: break
                items.append(m.group(1).strip()); i += 1
            blocks.append(("ul", items)); continue
        if m_ol:
            items = []
            while i < n:
                m = re.match(r"^\s*\d+\.\s+(.*)$", lines[i].rstrip())
                if not m: break
                items.append(m.group(1).strip()); i += 1
            blocks.append(("ol", items)); continue
        m_img = re.match(r"^\s*!\[([^\]]*)\]\(([^)\s]+)\)\s*$", stripped)
        if m_img:
            blocks.append(("img", m_img.group(1), m_img.group(2))); i += 1; continue
        para_lines = [stripped]; i += 1
        while i < n and lines[i].strip() and not lines[i].startswith("#") and not lines[i].startswith("---") and not lines[i].startswith(">") and not re.match(r"^\s*[-*]\s+", lines[i]) and not re.match(r"^\s*\d+\.\s+", lines[i]) and not (("|" in lines[i]) and i+1 < n and re.match(r"^\s*\|?\s*:?-+:?\s*(\|\s*:?-+:?\s*)+\|?\s*$", lines[i+1])):
            para_lines.append(lines[i].rstrip()); i += 1
        para = " ".join(para_lines)
        blocks.append(("p", para))
    return blocks


def render_blocks(blocks):
    html_parts = []
    toc = []
    for b in blocks:
        typ = b[0]
        if typ == "h2":
            _, aid, text = b
            toc.append((2, aid, text))
            html_parts.append(
                f'<h2 class="text-2xl font-bold text-white mb-4 mt-12 pb-3 border-b border-white/10 flex items-center gap-2" id="{html_mod.escape(aid, quote=True)}">'
                f'<span class="w-1 h-7 bg-gradient-to-b from-indigo-400 to-purple-500 rounded-full flex-shrink-0"></span>'
                f'{inline_md(text)}</h2>')
        elif typ == "h3":
            _, aid, text = b
            toc.append((3, aid, text))
            html_parts.append(
                f'<h3 class="text-xl font-semibold text-white/95 mb-3 mt-8 pl-3 border-l-4 border-indigo-400/70" id="{html_mod.escape(aid, quote=True)}">{inline_md(text)}</h3>')
        elif typ == "p":
            _, text = b
            html_parts.append(f'<p class="text-white/75 leading-relaxed my-3">{inline_md(text)}</p>')
        elif typ == "hr":
            html_parts.append('<hr class="border-white/10 my-8" />')
        elif typ == "quote":
            _, qlines = b
            q_html = " ".join(inline_md(l) for l in qlines)
            html_parts.append(
                '<div style="background:rgba(99,102,241,.1);border-left:4px solid rgba(139,92,246,.6);padding:1rem 1.25rem;border-radius:0 12px 12px 0;margin:1rem 0;color:rgba(255,255,255,.85);">'
                f'{q_html}</div>')
        elif typ == "ul":
            _, items = b
            lis = "".join(f'<li class="leading-relaxed">{inline_md(it)}</li>' for it in items)
            html_parts.append(f'<ul class="list-disc list-outside pl-6 space-y-2 my-3 text-white/75">{lis}</ul>')
        elif typ == "ol":
            _, items = b
            lis = "".join(f'<li class="leading-relaxed">{inline_md(it)}</li>' for it in items)
            html_parts.append(f'<ol class="list-decimal list-outside pl-6 space-y-2 my-3 text-white/75">{lis}</ol>')
        elif typ == "img":
            _, alt, url = b
            alt_e = html_mod.escape(alt, quote=True)
            html_parts.append(
                f'<div style="margin:1.25rem 0;text-align:center;">'
                f'<img src="{url}" alt="{alt_e}" style="max-width:100%;border-radius:12px;box-shadow:0 10px 30px rgba(0,0,0,.45);" loading="lazy"/>'
                f'<div style="font-size:.82rem;color:rgba(255,255,255,.55);margin-top:.5rem;">{inline_md(alt)}</div>'
                f'</div>')
        elif typ == "table":
            _, headers, rows = b
            th_html = "".join(f"<th>{inline_md(h)}</th>" for h in headers)
            trs = []
            for row in rows:
                tds = "".join(f"<td>{inline_md(c)}</td>" for c in row)
                trs.append(f"<tr>{tds}</tr>")
            tbody = "".join(trs)
            html_parts.append(
                f'<div class="table-wrap"><table class="glass-table"><thead><tr>{th_html}</tr></thead><tbody>{tbody}</tbody></table></div>')
    return "\n".join(html_parts), toc


def build_html():
    md = MD_PATH.read_text(encoding="utf-8")
    blocks = parse_md(md)
    content_html, toc = render_blocks(blocks)
    toc_parts = []
    for level, aid, text in toc:
        cls = "toc-h2" if level == 2 else "toc-h3"
        plain = re.sub(r"<[^>]+>", "", inline_md(text))
        toc_parts.append(f'<a href="#{html_mod.escape(aid, quote=True)}" class="{cls}">{html_mod.escape(plain)}</a>')
    toc_html = "\n".join(toc_parts)

    html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0">
<meta name="theme-color" content="#0f0c29">
<title>HBF高带宽闪存产业链深度研究 - 投资研究中心</title>
<meta name="description" content="2026.08.04 · SK海力士+闪迪发布HBF首版标准·AI推理存储新赛道">
<meta property="og:title" content="HBF高带宽闪存产业链深度研究">
<meta property="og:description" content="2026.08.04 · SK海力士+闪迪发布HBF首版标准·AI推理存储新赛道">
<meta property="og:image" content="/daily-news-insight/assets/default-og.png">
<meta property="og:type" content="article">
<script src="https://cdn.tailwindcss.com"></script>
<link rel="stylesheet" href="/daily-news-insight/assets/global-dark.css">
<link rel="stylesheet" href="/daily-news-insight/assets/stock-popup.css">
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@300;400;500;700;900&display=swap');
*{{font-family:'Noto Sans SC',sans-serif;}}
html{{scroll-behavior:smooth;}}
body{{background:linear-gradient(135deg,#0f0c29 0%,#1a1740 35%,#302b63 65%,#24243e 100%)!important;min-height:100vh;color:rgba(255,255,255,.95);}}
.pro-container{{max-width:64rem;margin:0 auto;padding:0 1.25rem;}}
.hero{{position:relative;padding:5rem 1.25rem 3rem;text-align:center;overflow:hidden;}}
.hero::before{{content:"";position:absolute;inset:0;background:radial-gradient(ellipse at 20% 30%,rgba(99,102,241,.25),transparent 60%),radial-gradient(ellipse at 80% 70%,rgba(168,85,247,.22),transparent 60%),radial-gradient(ellipse at 50% 100%,rgba(236,72,153,.15),transparent 70%);pointer-events:none;}}
.hero-title{{font-size:clamp(1.8rem,4.2vw,2.8rem);font-weight:900;background:linear-gradient(120deg,#fff 0%,#c7d2fe 40%,#a78bfa 70%,#f0abfc 100%);-webkit-background-clip:text;background-clip:text;color:transparent;line-height:1.25;margin-bottom:1rem;}}
.hero-sub{{font-size:1.05rem;color:rgba(255,255,255,.78);margin-bottom:1.25rem;}}
.hero-meta{{display:inline-flex;flex-wrap:wrap;gap:.5rem;justify-content:center;}}
.hero-chip{{padding:.35rem .8rem;background:rgba(255,255,255,.07);border:1px solid rgba(255,255,255,.12);border-radius:999px;font-size:.8rem;color:rgba(255,255,255,.78);backdrop-filter:blur(12px);}}
.hero-chip.accent{{background:linear-gradient(120deg,rgba(99,102,241,.25),rgba(168,85,247,.25));border-color:rgba(139,92,246,.45);color:#e9d5ff;}}
.card-glass{{background:rgba(255,255,255,.06)!important;backdrop-filter:blur(24px);-webkit-backdrop-filter:blur(24px);border:1px solid rgba(255,255,255,.10)!important;box-shadow:0 12px 40px rgba(0,0,0,.45);border-radius:22px;color:rgba(255,255,255,.95)!important;padding:1.75rem 1.5rem;margin-bottom:1.5rem;}}
@media(min-width:768px){{.card-glass{{padding:2.25rem 2.5rem;}}}}
.card-glass .text-gray-800,.card-glass .text-gray-700{{color:rgba(255,255,255,.92)!important;}}
.card-glass .text-gray-600,.card-glass .text-gray-500{{color:rgba(255,255,255,.7)!important;}}
.table-wrap{{overflow-x:auto;margin:1rem 0;border-radius:12px;border:1px solid rgba(255,255,255,.1);}}
table.glass-table{{width:100%;border-collapse:collapse;font-size:.9rem;}}
table.glass-table thead th{{background:linear-gradient(135deg,rgba(99,102,241,.22),rgba(139,92,246,.22));color:#fff;font-weight:600;text-align:left;padding:.75rem .9rem;border-bottom:1px solid rgba(255,255,255,.15);white-space:nowrap;}}
table.glass-table tbody td{{padding:.7rem .9rem;border-bottom:1px solid rgba(255,255,255,.06);color:rgba(255,255,255,.82);vertical-align:top;}}
table.glass-table tbody tr:hover{{background:rgba(255,255,255,.04);}}
table.glass-table tbody tr:nth-child(even) td{{background:rgba(255,255,255,.02);}}
.toc-card{{position:sticky;top:80px;background:rgba(255,255,255,.04);border:1px solid rgba(255,255,255,.08);border-radius:16px;padding:1rem 1.1rem;max-height:calc(100vh - 100px);overflow-y:auto;}}
.toc-title{{font-size:.95rem;font-weight:700;color:#fff;margin-bottom:.75rem;display:flex;align-items:center;gap:.4rem;}}
.toc-h2{{display:block;padding:.3rem .4rem;color:rgba(255,255,255,.85);font-size:.85rem;font-weight:500;border-radius:6px;text-decoration:none;}}
.toc-h2:hover{{background:rgba(99,102,241,.18);color:#fff;}}
.toc-h3{{display:block;padding:.2rem .4rem .2rem 1rem;color:rgba(255,255,255,.6);font-size:.78rem;border-radius:6px;text-decoration:none;}}
.toc-h3:hover{{background:rgba(255,255,255,.05);color:rgba(255,255,255,.88);}}
.glass-nav{{background:rgba(15,12,41,.72)!important;backdrop-filter:blur(30px);-webkit-backdrop-filter:blur(20px);border-bottom:1px solid rgba(255,255,255,.08);}}
.nav-link{{padding:.4rem .75rem;border-radius:8px;font-size:.85rem;color:rgba(255,255,255,.78);transition:all .2s;display:inline-block;text-decoration:none;}}
.nav-link:hover{{color:#fff;background:rgba(255,255,255,.08);}}
.nav-link.active{{color:#fff;background:rgba(255,255,255,.15);}}
.history-entry-wrap{{margin:2.5rem auto 1rem;text-align:center;}}
.history-entry-link{{display:inline-flex;align-items:center;gap:.5rem;padding:.7rem 1.4rem;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.14);border-radius:999px;color:rgba(255,255,255,.82);font-size:.92rem;font-weight:500;text-decoration:none;backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px);box-shadow:0 6px 20px rgba(0,0,0,.25);transition:all .25s ease;}}
.history-entry-link:hover{{background:rgba(102,126,234,.22);border-color:rgba(139,92,246,.45);color:#fff;transform:translateY(-1px);box-shadow:0 10px 28px rgba(102,126,234,.35);}}
.float-actions{{position:fixed;right:1.25rem;bottom:1.5rem;z-index:40;display:flex;flex-direction:column;gap:.6rem;}}
.float-btn{{width:44px;height:44px;border-radius:50%;background:rgba(255,255,.08);border:1px solid rgba(255,255,.18);color:#fff;display:flex;align-items:center;justify-content:center;cursor:pointer;backdrop-filter:blur(16px);box-shadow:0 8px 20px rgba(0,0,0,.35);transition:all .2s;font-size:16px;}}
.float-btn:hover{{background:rgba(99,102,241,.35);border-color:rgba(139,92,246,.5);transform:translateY(-2px);}}
#progressBar{{position:fixed;top:0;left:0;height:3px;background:linear-gradient(90deg,#6366f1,#a855f7,#ec4899);z-index:9999;width:0%;transition:width .08s ease;}}
@media(max-width:1024px){{.toc-col{{display:none;}}}}
@media(max-width:640px){{.hero{{padding:4rem 1rem 2rem;}}.card-glass{{padding:1.25rem 1rem;border-radius:16px;}}table.glass-table{{font-size:.8rem;}}}}
img{{max-width:100%;height:auto;border-radius:8px;}}
sup{{font-size:.7em;color:#a5b4fc;}}
</style>
</head>
<body>
<div id="progressBar"></div>
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
<a href="/daily-news-insight/industry_chain/index.html" class="block nav-link active">🔗 产业链</a>
<a href="/daily-news-insight/daily/index.html" class="block nav-link">日报</a>
<a href="/daily-news-insight/intraday/index.html" class="block nav-link">盘中</a>
<a href="/daily-news-insight/aftermarket/index.html" class="block nav-link">盘后</a>
<a href="/daily-news-insight/weekly_review/index.html" class="block nav-link">周复盘</a>
<a href="/daily-news-insight/weekend_express/index.html" class="block nav-link">周末速递</a>
<a href="/daily-news-insight/tomorrow_catalyst/index.html" class="block nav-link">明日催化</a>
<a href="/daily-news-insight/s_level_catalyst/index.html" class="block nav-link">S级催化</a>
</div>
</nav>

<section class="hero">
<div class="relative z-10 max-w-4xl mx-auto">
<div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-indigo-500/15 border border-indigo-400/30 text-indigo-200 text-xs font-medium mb-5"><span>🔬</span><span>产业链深度研究</span></div>
<h1 class="hero-title">HBF高带宽闪存产业链深度研究</h1>
<p class="hero-sub">SK海力士+闪迪发布全球首份标准 · AI推理存储千亿新赛道 · 核心标的排序与操作建议</p>
<div class="hero-meta">
<span class="hero-chip accent">📅 2026.08.04</span>
<span class="hero-chip">🏷️ S级催化 · HBF高带宽闪存 · AI推理存储</span>
<span class="hero-chip">⚠️ 本文仅作研究参考，不构成投资建议</span>
</div>
</div>
</section>

<main class="pro-container pb-16">
<div class="grid grid-cols-1 lg:grid-cols-[minmax(0,1fr)_240px] gap-8">
<div>
<div class="card-glass">
{content_html}

<hr class="border-white/10 my-8" />
<p class="text-white/75 leading-relaxed my-3"><strong class="text-white/95 font-semibold">报告字数统计</strong>：约3.4万字（含图表标题、表格、引用）<br/>
<strong class="text-white/95 font-semibold">报告类型</strong>：产业链深度研究 / S级题材投资策略报告<br/>
<strong class="text-white/95 font-semibold">数据截止</strong>：2026年8月4日A股盘中
</p>

<div class="history-entry-wrap">
<a href="./latest.html" class="history-entry-link">
<span>🔗</span>
<span>返回产业链总览</span>
<span style="opacity:.75">→</span>
</a>
</div>
<div class="text-center text-white/40 text-sm py-6">
<p>HBF高带宽闪存产业链深度研究 · 2026年8月4日</p>
<p class="text-xs mt-2">数据来源：公开信息整理 · 仅作研究参考，不构成投资建议</p>
</div>
</div>
</div>
<aside class="toc-col"><div class="toc-card">
<div class="toc-title"><span>📑</span>目录导航</div>
{toc_html}
</div></aside>
</div>
</main>

<div class="float-actions">
<button class="float-btn" onclick="window.scrollTo({{top:0,behavior:'smooth'}})" title="回到顶部">↑</button>
<button class="float-btn" onclick="navigator.clipboard.writeText(location.href).then(()=>alert('链接已复制'))" title="分享">🔗</button>
</div>

<script src="/daily-news-insight/assets/stock-popup.js"></script>
<script>
window.addEventListener('scroll',()=>{{const h=document.documentElement;const pct=(h.scrollTop/(h.scrollHeight-h.clientHeight))*100;document.getElementById('progressBar').style.width=pct+'%';const nav=document.querySelector('.glass-nav');if(nav)nav.classList.toggle('scrolled',window.scrollY>10);}},{{passive:true}});
</script>
</body>
</html>
"""
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(html, encoding="utf-8")
    print(f"Written: {OUT_PATH}, size={OUT_PATH.stat().st_size} bytes")


if __name__ == "__main__":
    build_html()
