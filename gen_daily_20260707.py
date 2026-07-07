#!/usr/bin/env python3
"""2026年7月7日 每日新闻洞察生成 - 周二·费半+4.5%暴力反弹·8000亿两重落地·液冷异军突起"""
import sys, os
WORK_DIR = '/root/daily-news-insight'
sys.path.insert(0, os.path.join(WORK_DIR, 'v3'))
from generators.daily_pro import DailyReportProGenerator

gen = DailyReportProGenerator(
    date_str='2026年7月7日', weekday='星期二',
    subtitle='2026年7月7日 星期二 · 费半+4.48%暴力反弹/AMD+10%/西数+10% · 高盛暴力拉目标价 · 8000亿两重全部下达 · SK海力士启动赴美IPO · 黄金4176回落 · *ST建艺-3.49%未跌停仍须清仓',
    data_dir=os.path.join(WORK_DIR, 'data')
)

def render_cards(items):
    out = ''
    for i in items:
        c = 'text-red-400' if i['up'] else 'text-green-400'
        bg = 'from-red-500/20 to-orange-500/10 border-red-500/20' if i['up'] else 'from-green-500/20 to-emerald-500/10 border-green-500/20'
        out += f'<div class="bg-gradient-to-br {bg} border rounded-lg p-3 text-center transition-all duration-300 hover:scale-105"><div class="text-xs text-white/60 mb-1">{i["name"]}</div><div class="text-sm font-bold {c}">{i["change"]}</div></div>'
    return out

def render_list(items):
    out = ''
    for i in items:
        c = 'text-red-400' if i['up'] else 'text-green-400'
        out += f'<div class="flex items-center justify-between py-2 border-b border-white/5 last:border-0"><span class="text-sm text-white/70">{i["name"]}</span><span class="text-sm font-semibold {c}">{i["change"]}</span></div>'
    return out

print("Script created successfully")
