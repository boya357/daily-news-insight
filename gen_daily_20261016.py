#!/usr/bin/env python3
"""2026-10-16 每日新闻洞察 - V3 Pro生成器"""
import sys, os
sys.path.insert(0, 'v3')
os.chdir('/root/daily-news-insight')
from generators.daily_pro import DailyReportProGenerator

gen = DailyReportProGenerator(
    date_str="2026-10-16",
    weekday="周五",
    subtitle="韩国黑色星期四KOSPI暴跌7.57%三星跌9.5%SK海力士跌11% | 费半七连跌纳指触底反弹 | 长鑫4F2架构冲击存储垄断格局 | 江波龙前三季净利预增18倍",
    data_dir='/root/daily-news-insight/data'
)
print('Generator initialized OK')
