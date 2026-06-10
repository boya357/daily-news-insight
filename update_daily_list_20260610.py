"""
更新每日新闻洞察列表页
增量插入新报告卡片
"""
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'v3'))

from generators.list_page import ListPageGenerator

# 创建列表页生成器
list_gen = ListPageGenerator("daily")

# 增量插入新报告
list_gen.insert_report(
    list_filepath="docs/daily/latest.html",
    title="20260610 每日新闻洞察",
    date="2026-06-10",
    url="20260610_每日新闻洞察.html",
    excerpt="隔夜美股科技股剧烈震荡，2万亿国产算力网规划出炉，存储芯片超级周期延续，英维克涨停",
    tag="🔥 最新"
)

print("列表页更新完成")
