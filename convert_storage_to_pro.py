#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
存储芯片报告 - V3.5 Pro 分模块卡片风格改造
"""

from bs4 import BeautifulSoup, Tag

SRC_PATH = "/app/data/所有对话/主对话/docs/industry_chain/20260619_存储芯片产业链深度研究报告.html"
DEST_PATH = "/root/daily-news-insight/docs/industry_chain/20260619_存储芯片产业链深度研究报告.html"

def convert_to_pro_cards():
    with open(SRC_PATH, 'r', encoding='utf-8') as f:
        content = f.read()
    
    soup = BeautifulSoup(content, 'html.parser')
    
    # 找到报告内容容器
    report_content = soup.find(class_='report-content')
    if not report_content:
        print("❌ 未找到report-content容器")
        return
    
    # 去掉外层大卡片的样式
    classes = report_content.get('class', [])
    classes = [c for c in classes if c not in ['glass-card-white', 'p-8', 'md:p-12']]
    classes.append('space-y-6')
    report_content['class'] = classes
    
    # 获取所有直接子元素
    children = list(report_content.children)
    
    # 分离前置内容和章节内容
    pre_section_items = []
    sections = []  # [(title_tag, content_items)]
    current_title = None
    current_contents = []
    
    for child in children:
        if isinstance(child, Tag) and child.name == 'h2' and child.get('id', '').startswith('section'):
            if current_title:
                sections.append((current_title, current_contents))
            current_title = child
            current_contents = []
        else:
            if current_title:
                current_contents.append(child)
            else:
                pre_section_items.append(child)
    
    if current_title:
        sections.append((current_title, current_contents))
    
    # 重建report_content
    report_content.clear()
    
    # 1. 前置内容卡片
    if pre_section_items:
        pre_card = soup.new_tag('div')
        pre_card['class'] = ['glass-card', 'p-6', 'md:p-8']
        for item in pre_section_items:
            pre_card.append(item)
        report_content.append(pre_card)
    
    # 2. 每个章节一个卡片
    for title, items in sections:
        card = soup.new_tag('div')
        card['class'] = ['glass-card', 'p-6', 'md:p-8']
        
        # 给标题加左侧装饰条
        # 创建新标题
        new_title = soup.new_tag('h2')
        new_title['id'] = title.get('id', '')
        for attr, val in title.attrs.items():
            if attr != 'id' and attr != 'class':
                new_title[attr] = val
        if title.get('class'):
            new_title['class'] = title.get('class')
        
        # 装饰条
        deco = soup.new_tag('span')
        deco['style'] = 'display:inline-block;width:4px;height:1.1em;background:linear-gradient(to bottom,#8b5cf6,#3b82f6);margin-right:10px;vertical-align:middle;border-radius:2px;'
        new_title.append(deco)
        
        # 原标题内容
        for child in title.children:
            new_title.append(child)
        
        card.append(new_title)
        
        # 章节内容
        for item in items:
            if isinstance(item, Tag) and 'section-divider' in item.get('class', []):
                item['style'] = (item.get('style') or '') + ' margin:1.5rem 0;'
            card.append(item)
        
        report_content.append(card)
    
    # 保存
    result = str(soup)
    
    with open(DEST_PATH, 'w', encoding='utf-8') as f:
        f.write(result)
    
    with open(SRC_PATH, 'w', encoding='utf-8') as f:
        f.write(result)
    
    print(f"✅ Pro卡片风格改造完成")
    print(f"   共 {len(sections)} 个章节卡片 + 1个概览卡片")

if __name__ == "__main__":
    convert_to_pro_cards()
