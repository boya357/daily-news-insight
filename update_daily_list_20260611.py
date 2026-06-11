"""
更新每日新闻洞察列表页
"""
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'v3'))

from generators.list_page import ListPageGenerator

# 创建列表页生成器
list_gen = ListPageGenerator("daily")

# 插入新报告
result = list_gen.insert_report(
    list_filepath="docs/daily/latest.html",
    title="2026年6月11日 每日新闻洞察",
    date="2026-06-11",
    url="20260611_每日新闻洞察.html",
    excerpt="美股暴跌道指跌近千点，CPI爆表加息预期升温；中东局势升级油价大涨黄金暴跌；工信部发布AI+信息通信三年方案，光电芯片人形机器人迎政策催化",
    tag="🔥 最新"
)

print(f"列表页更新结果: {result}")

# 验证列表页
if os.path.exists("docs/daily/latest.html"):
    size = os.path.getsize("docs/daily/latest.html")
    print(f"列表页大小: {size} 字节")
