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

# 列表页路径
list_filepath = "docs/daily/latest.html"

# 插入新报告
success = list_gen.insert_report(
    list_filepath=list_filepath,
    title="20260608 每日新闻洞察",
    date="2026-06-08",
    url="20260608_每日新闻洞察.html",
    excerpt="美股黑色星期五纳指暴跌4.18%，AI科技股集体重挫；存储超级周期强化，英伟达SK集团战略合作；A股承压防御为主",
    tag="日报"
)

if success:
    print("✅ 列表页更新成功")
    print(f"列表页大小: {os.path.getsize(list_filepath)} 字节")
else:
    print("❌ 列表页更新失败")

