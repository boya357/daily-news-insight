import sys
import os
sys.path.insert(0, '/root/daily-news-insight')

from v3.generators.list_page import ListPageGenerator
from v3.core.config import REPORT_TYPES

DATE = "20260606"
DATE_DISPLAY = "2026-06-06"

reports = [
    ("daily", "日报深度测试报告(V3.0)", f"{DATE}_V30测试_日报.html", "V3.0深度测试版 - AI算力爆发行情分析，8条新闻6个板块深度解读"),
    ("intraday", "盘中快报深度测试报告(V3.0)", f"{DATE}_V30测试_盘中快报.html", "V3.0深度测试版 - GTC大会催化AI算力行情，4大指数实时跟踪"),
    ("aftermarket", "盘后速递深度测试报告(V3.0)", f"{DATE}_V30测试_盘后速递.html", "V3.0深度测试版 - AI算力爆发，科创50大涨3.56%，5大板块分析"),
    ("weekly_review", "周复盘深度测试报告(V3.0)", f"{DATE}_V30测试_周复盘.html", "V3.0深度测试版 - AI算力领涨，科创50周涨8.92%，5大维度复盘"),
    ("s_level_catalyst", "S级催化深度测试报告(V3.0)", f"{DATE}_V30测试_S级催化.html", "V3.0深度测试版 - AI算力革命：从H200到AGI的产业浪潮深度分析"),
    ("weekly_outlook", "周三前瞻深度测试报告(V3.0)", f"{DATE}_V30测试_周三前瞻.html", "V3.0深度测试版 - GTC大会催化，下半周继续看反弹，5大机会方向"),
    ("weekend_express", "周末速递深度测试报告(V3.0)", f"{DATE}_V30测试_周末速递.html", "V3.0深度测试版 - AI算力革命：是泡沫还是新周期起点？深度研报"),
    ("tomorrow_catalyst", "明日催化剂深度测试报告(V3.0)", f"{DATE}_V30测试_明日催化剂.html", "V3.0深度测试版 - GTC大会开幕+5月经济数据，明天是重要窗口"),
    ("monthly", "月报深度测试报告(V3.0)", f"{DATE}_V30测试_月报.html", "V3.0深度测试版 - 2026年5月市场回顾与6月投资策略展望"),
]

print("📋 更新各类型列表页...\n")

for type_key, title, filename, excerpt in reports:
    type_info = REPORT_TYPES.get(type_key, {})
    category_dir = type_info.get("dir", "")
    list_file = type_info.get("list_file", "latest.html")
    tag_name = type_info.get("name", "")
    
    list_filepath = f"/root/daily-news-insight/docs/{category_dir}/{list_file}"
    
    if not os.path.exists(list_filepath):
        print(f"⚠️  {type_key} 列表页不存在: {list_filepath}")
        continue
    
    try:
        gen = ListPageGenerator(type_key)
        success = gen.insert_report(
            list_filepath=list_filepath,
            title=title,
            date=DATE_DISPLAY,
            url=filename,
            excerpt=excerpt,
            tag=tag_name
        )
        if success:
            print(f"✅ {type_key} 列表页更新成功: {list_filepath}")
        else:
            print(f"❌ {type_key} 列表页更新失败")
    except Exception as e:
        print(f"❌ {type_key} 列表页更新异常: {e}")
        import traceback
        traceback.print_exc()

print("\n🚀 提交到GitHub...")
import subprocess
subprocess.run(["git", "add", "docs/"], cwd="/root/daily-news-insight")
subprocess.run(["git", "commit", "-m", "更新V3.0深度测试报告列表页"], cwd="/root/daily-news-insight")
subprocess.run(["git", "push"], cwd="/root/daily-news-insight")
print("✅ 部署完成！")

