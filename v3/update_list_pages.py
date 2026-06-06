import sys
sys.path.insert(0, '/root/daily-news-insight')

from v3.generators.list_page import ListPageGenerator
from v3.core.config import REPORT_TYPES

DATE = "20260606"
reports = [
    ("daily", "日报", f"{DATE}_V30测试_日报.html"),
    ("intraday", "盘中快报", f"{DATE}_V30测试_盘中快报.html"),
    ("aftermarket", "盘后速递", f"{DATE}_V30测试_盘后速递.html"),
    ("weekly_review", "周复盘", f"{DATE}_V30测试_周复盘.html"),
    ("s_level_catalyst", "S级催化", f"{DATE}_V30测试_S级催化.html"),
    ("weekly_outlook", "周三前瞻", f"{DATE}_V30测试_周三前瞻.html"),
    ("weekend_express", "周末速递", f"{DATE}_V30测试_周末速递.html"),
    ("tomorrow_catalyst", "明日催化剂", f"{DATE}_V30测试_明日催化剂.html"),
    ("monthly", "月报", f"{DATE}_V30测试_月报.html"),
]

print("📋 更新各类型列表页...")
for report_type, report_name, filename in reports:
    try:
        type_info = REPORT_TYPES.get(report_type, {})
        dir_name = type_info.get('dir', report_type)
        list_file = type_info.get('list_file', 'latest.html')
        list_page_path = f"/root/daily-news-insight/docs/{dir_name}/{list_file}"
        
        list_gen = ListPageGenerator(report_type=report_type)
        list_gen.insert_report(
            list_filepath=list_page_path,
            title=f"{report_name}测试报告(V3.0)",
            date="2026-06-06",
            url=filename,
            excerpt=f"V3.0系统{report_name}类型完整内容测试报告",
            tag="V3.0"
        )
        print(f"   ✅ {report_name} 列表页已更新")
    except Exception as e:
        print(f"   ❌ {report_name} 列表页更新失败: {e}")

print("\n🎉 列表页更新完成！")
