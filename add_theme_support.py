"""
批量给所有Pro生成器添加theme参数支持
默认theme='dark'，完全向后兼容，不影响V3.5现有功能
"""
import os
import re

GENERATORS_DIR = "/app/data/所有对话/主对话/v3/generators"

def add_theme_to_init(filepath):
    """给生成器的__init__方法添加theme参数"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # 1. 在__init__方法的参数列表最后添加 theme: str = "dark"
    # 找到def __init__(self, ...)这一行，在最后一个参数后添加
    init_pattern = r'(def __init__\(self[^)]*?)(\s*\):)'
    
    def add_theme_param(match):
        params_part = match.group(1)
        end_part = match.group(2)
        # 如果已经有theme参数了，跳过
        if 'theme' in params_part:
            return match.group(0)
        # 在参数列表最后添加theme参数
        # 处理换行和缩进的情况
        return params_part.rstrip() + ',\n                 theme: str = "dark"' + end_part
    
    content = re.sub(init_pattern, add_theme_param, content, count=1)
    
    # 2. 在super().__init__()调用中添加theme=theme参数
    super_pattern = r'(super\(\)\.__init__\([^)]*?)(\s*\))'
    
    def add_theme_super(match):
        args_part = match.group(1)
        end_part = match.group(2)
        # 如果已经有theme了，跳过
        if 'theme=' in args_part:
            return match.group(0)
        # 在参数列表最后添加theme=theme
        return args_part.rstrip() + ',\n            theme=theme' + end_part
    
    content = re.sub(super_pattern, add_theme_super, content, count=1)
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

# 遍历所有Pro生成器
modified = []
for filename in sorted(os.listdir(GENERATORS_DIR)):
    if filename.endswith('_pro.py') and filename != 'pro_base.py' and filename != 'report_pro_base.py':
        filepath = os.path.join(GENERATORS_DIR, filename)
        if add_theme_to_init(filepath):
            modified.append(filename)
            print(f"✅ {filename} - 已添加theme参数支持")
        else:
            print(f"⏭️  {filename} - 已有theme参数或无需修改")

print(f"\n共修改 {len(modified)} 个文件")
print("所有修改均为向后兼容，默认theme='dark'，不影响V3.5现有功能")
