#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
更新S级催化扫描列表页
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'v3'))

from generators.list_page import ListPageGenerator

# 初始化列表页生成器
list_gen = ListPageGenerator("s_level_catalyst")

# 插入新报告
result = list_gen.insert_report(
    list_filepath="docs/s级催化扫描/latest.html",
    title="工信部发布AI+信息通信三年行动方案",
    date="2026-06-10",
    url="20260610_工信部AI+信息通信三年行动方案.html",
    excerpt="2026年6月10日，工信部印发《人工智能+信息通信创新发展实施意见（2026—2028年）》，部署17项重点任务，攻坚高速光电芯片、CPO、智能体互联网等核心技术，构建三级算力设施体系，直接利好光通信、算力、CPO等产业链。",
    tag="🔥 S级催化"
)

print(f"列表页更新结果：{'成功' if result else '失败'}")

# 验证列表完整性
is_valid = list_gen.validate_list_integrity("docs/s级催化扫描/latest.html")
print(f"列表完整性验证：{'通过' if is_valid else '失败'}")
