"""
测试：创建生成器后修改theme属性是否能切换到V4风格
"""
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'v3'))

from generators.daily_pro import DailyReportProGenerator

DATA_DIR = os.path.join(os.path.dirname(__file__), 'v3', 'example_data')
os.makedirs(DATA_DIR, exist_ok=True)

# 创建一个日报生成器（默认dark主题）
daily = DailyReportProGenerator(data_dir=DATA_DIR)
print(f"默认主题: {daily.theme}")

# 切换到light主题
daily.theme = 'light'
print(f"切换后主题: {daily.theme}")

# 尝试渲染（看看会不会报错）
try:
    html = daily.render()
    # 检查是否包含V4主题CSS
    if 'get_v4_theme_css' in html or 'background: #FFFFFF' in html:
        print("✅ V4主题CSS已生效！")
    else:
        print("❌ V4主题CSS未找到")
        # 看看实际生成的CSS是什么
        import re
        style_match = re.search(r'<style>(.*?)</style>', html, re.DOTALL)
        if style_match:
            print(f"CSS长度: {len(style_match.group(1))}")
        else:
            print("没有找到style标签")
except Exception as e:
    print(f"❌ 渲染失败: {e}")
    import traceback
    traceback.print_exc()
