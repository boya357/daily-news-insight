"""
使用Pro版生成器重新生成S级催化扫描列表页
"""
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'v3'))

from generators.list_page_pro import ListPageProGenerator

# 创建Pro版列表页生成器
generator = ListPageProGenerator('s级催化扫描', docs_dir='docs')

# 加载数据（扫描报告文件）
generator.load_data()

# 发布列表页
result = generator.publish()

print(f'✅ 列表页生成完成')
print(f'   输出路径: {result.get("output_path", "未知")}')
print(f'   报告数量: {result.get("file_count", 0)} 份')
print(f'   文件大小: {os.path.getsize(result["output_path"])} 字节')
