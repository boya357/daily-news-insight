#!/usr/bin/env python3
"""2026-10-19 每日新闻洞察 - V3 Pro生成器"""
import sys, os
sys.path.insert(0, 'v3')
os.chdir('/root/daily-news-insight')
from generators.daily_pro import DailyReportProGenerator

gen = DailyReportProGenerator(
    date_str="2026-10-19",
    weekday="周一",
    subtitle="SOX八连跌创2006年以来最长纪录存储单周重挫14-18% | CoreWeave股债双杀AI债务恐慌蔓延 | 总书记考察乌兰察布算力网前景广阔 | 德明利前三季净利暴增320倍",
    data_dir='/root/daily-news-insight/data'
)
