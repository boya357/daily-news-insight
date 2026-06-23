#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
智能选题助手每日更新脚本
"""

import re
from datetime import datetime

def update_topic_picker():
    html_path = "docs/topic-picker/index.html"
    
    # 读取文件
    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 备份原文件
    backup_path = html_path + ".bak." + datetime.now().strftime("%Y%m%d_%H%M%S")
    with open(backup_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"✅ 已备份原文件到 {backup_path}")
    
    # ========== 更新数据时间 ==========
    content = content.replace(
        '数据更新时间：2026年6月9日 07:51',
        '数据更新时间：2026年6月9日 21:30'
    )
    
    # ========== S级题材评分调整 ==========
    # 存储芯片超级周期 - 今日表现强劲，上调评分
    # 先找到存储芯片的评分并更新
    content = content.replace(
        '英伟达RTX Spark发布+Windows on Arm生态突破+智能体时代开启',
        '英伟达RTX Spark发布+Windows on Arm生态突破+AI Agent加速渗透'
    )
    
    # 存储芯片评分调整（根据今日铜冠铜箔等存储链大涨）
    # 查找并更新存储芯片相关的描述
    content = content.replace(
        'HBM3E量产出货+AI服务器需求爆发+存储涨价周期确认',
        'HBM3E量产出货+AI服务器需求爆发+铜箔/PCB量价齐升'
    )
    
    # ========== A级题材调整 ==========
    # AI应用端评分从87分上调到89分
    content = content.replace(
        '商业落地加速，资金从硬件转向应用',
        'AI Agent应用爆发+端侧AI落地加速'
    )
    # 调整AI应用端评分
    old = '<span class="text-2xl font-black text-yellow-600">87分</span>'
    new = '<span class="text-2xl font-black text-yellow-600">89分</span>'
    # 只替换第一个（AI应用端）
    content = content.replace(old, new, 1)
    
    # 电力/算电协同评分从82上调到84
    old = '<span class="text-2xl font-black text-yellow-600">82分</span>'
    new = '<span class="text-2xl font-black text-yellow-600">84分</span>'
    # 找到第三个（电力）
    parts = content.split(old, 3)
    if len(parts) >= 3:
        content = old.join(parts[:2]) + new + old.join(parts[2:])
    
    # 城市更新评分从80下调到78
    old = '<span class="text-2xl font-black text-yellow-600">80分</span>'
    new = '<span class="text-2xl font-black text-yellow-600">78分</span>'
    # 第四个是城市更新
    parts = content.split(old, 4)
    if len(parts) >= 4:
        content = old.join(parts[:3]) + new + old.join(parts[3:])
    
    # 保存更新后的文件
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✅ 智能选题助手更新完成")
    print("   - 更新时间：2026年6月9日 21:30")
    print("   - AI应用端评分：87→89分")
    print("   - 电力/算电协同评分：82→84分")
    print("   - 城市更新评分：80→78分")
    
    return True

if __name__ == "__main__":
    update_topic_picker()
