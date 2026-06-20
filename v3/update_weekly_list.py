"""
更新周复盘列表页
在 latest.html 顶部插入新报告卡片
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from generators.list_page import ListPageGenerator

# 创建列表页生成器
gen = ListPageGenerator(report_type="weekly_review")

# 插入新报告
list_filepath = "/root/daily-news-insight/docs/weekly_review/latest.html"

success = gen.insert_report(
    list_filepath=list_filepath,
    title="2026年第25周周复盘",
    date="2026年6月20日",
    url="20260620_周复盘.html",
    excerpt="本周A股延续强势，科创50单周涨14.93%，创业板涨11.02%。AI算力、存储芯片等主线爆发，铜冠铜箔周涨超40%。",
    tag="新发布"
)

if success:
    print("✅ 列表页更新成功")
else:
    print("❌ 列表页更新失败")
