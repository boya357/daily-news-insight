#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
持仓智能预警仪表盘生成器
基于Jinja2模板，数据驱动
保证UI与原版100%一致
"""

import json
import os
from datetime import datetime
from jinja2 import Environment, FileSystemLoader

def load_data():
    """加载持仓数据"""
    data_path = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'portfolio.json')
    with open(data_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def generate():
    """生成页面"""
    data = load_data()
    
    # 设置Jinja2环境
    template_dir = os.path.join(os.path.dirname(__file__), '..', '..', 'templates')
    env = Environment(loader=FileSystemLoader(template_dir))
    template = env.get_template('portfolio_dashboard.html')
    
    # 渲染
    html = template.render(
        portfolio=data['portfolio'],
        stocks=data['stocks']
    )
    
    # 保存
    output_path = os.path.join(os.path.dirname(__file__), '..', '..', 'docs', '持仓智能预警仪表盘', 'index.html')
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"✅ 持仓智能预警仪表盘已生成：{output_path}")
    print(f"   持仓标的：{data['portfolio']['stock_count']}只")
    print(f"   组合盈亏：{data['portfolio']['total_return']*100:+.2f}%")
    
    return output_path

if __name__ == '__main__':
    generate()
