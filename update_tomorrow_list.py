import sys
import os
sys.path.insert(0, '/root/daily-news-insight')

from v3.generators.list_page_pro import ListPageProGenerator

# 创建明日催化剂频道的列表页生成器
generator = ListPageProGenerator('明日催化剂', docs_dir='docs')

# 发布列表页（默认保存到对应频道的 latest.html）
result = generator.publish()

print(f"✅ 列表页已生成：{result['output_path']}")
print(f"📊 报告数量：{result.get('file_count', '未知')}")

# 验证文件
file_size = os.path.getsize(result['output_path'])
print(f"📁 文件大小：{file_size} 字节 ({file_size/1024:.1f} KB)")
