#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pro版列表页统一生成脚本（已迁移到Pro生成器架构）
使用 v3/generators/list_page_pro.py 中的标准生成器

核心设计原则：
- 卡片套卡片的层次感
- 深色玻璃态风格
- 图表可视化的高级感
- 统一导航系统
"""
import os
import sys

# 添加v3模块路径
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'v3'))

from generators.list_page_pro import generate_all_list_pages, ListPageProGenerator, CHANNEL_CONFIGS


def main():
    docs_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'docs')
    
    if len(sys.argv) > 1:
        channel = sys.argv[1]
        if channel in CHANNEL_CONFIGS:
            generator = ListPageProGenerator(channel, docs_dir=docs_dir)
            result = generator.publish()
            print(f"✅ {CHANNEL_CONFIGS[channel]['title']} → {result['file_count']} 份报告")
        else:
            print(f"❌ 未知栏目: {channel}")
            print(f"可用栏目: {', '.join(CHANNEL_CONFIGS.keys())}")
    else:
        generate_all_list_pages(docs_dir=docs_dir)


if __name__ == '__main__':
    main()
