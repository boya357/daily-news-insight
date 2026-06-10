#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
统一持仓数据更新脚本
一个数据源（data/portfolio.json），同步更新所有页面
"""

import json
import os
import re
from datetime import datetime

def load_data():
    """加载统一持仓数据"""
    with open('data/portfolio.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def get_stock_by_name(stocks, name):
    """根据名称获取股票数据"""
    for s in stocks:
        if s['name'] == name:
            return s
    return None

def update_index_page(data):
    """更新首页持仓概览"""
    print("🔄 更新首页持仓概览...")
    
    html_path = 'docs/index.html'
    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    stocks = data['stocks']
    
    # 更新每只股票的价格信息
    for stock in stocks:
        name = stock['name']
        cost = float(stock['cost_price'])
        current = float(stock['current_price'])
        
        # 找到该股票的卡片，更新成本价和现价
        # 模式：成本X.XX → 现价Y.YY
        pattern = re.compile(
            rf'({re.escape(name)}.*?成本)([0-9.]+)(\s*→\s*现价)([0-9.]+)',
            re.DOTALL
        )
        if pattern.search(html):
            html = pattern.sub(
                lambda m: f'{m.group(1)}{cost:.2f}{m.group(3)}{current:.2f}',
                html
            )
            
            # 更新状态标签（根据盈亏情况）
            profit_pct = (current - cost) / cost * 100
            if profit_pct > 0:
                status_label = '🟢 持有'
                status_color = 'text-green-600'
            elif profit_pct > -10:
                status_label = '🟡 观察'
                status_color = 'text-yellow-600'
            else:
                status_label = '🔴 止损'
                status_color = 'text-red-500'
            
            # 更新状态标签
            label_pattern = re.compile(
                rf'({re.escape(name)}</span>\s*<span class=")([a-z0-9-]+)( font-bold text-sm">)([^<]+)(</span>)',
                re.DOTALL
            )
            if label_pattern.search(html):
                html = label_pattern.sub(
                    lambda m: f'{m.group(1)}{status_color}{m.group(3)}{status_label}{m.group(5)}',
                    html
                )
    
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print("  ✅ 首页持仓概览更新完成")

def update_dashboard(data):
    """更新持仓智能预警仪表盘（调用V3脚本）"""
    print("🔄 更新持仓智能预警仪表盘...")
    os.system('python3 v3/generators/update_portfolio_v3.py')
    print("  ✅ 持仓智能预警仪表盘更新完成")

def update_warning_system(data):
    """更新智能预警系统页面"""
    print("🔄 更新智能预警系统...")
    
    html_path = 'docs/智能预警系统/index.html'
    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    stocks = data['stocks']
    
    # 构建风险事件描述
    risk_events = []
    for stock in stocks:
        name = stock['name']
        current = float(stock['current_price'])
        cost = float(stock['cost_price'])
        profit_pct = (current - cost) / cost * 100
        
        if name == '英维克':
            if profit_pct < -20:
                risk_events.append(f"英维克反弹但仍破止损（浮亏{profit_pct:.1f}%）")
            else:
                risk_events.append(f"英维克反弹中（浮亏{profit_pct:.1f}%）")
        elif name == '铜冠铜箔':
            if profit_pct > 30:
                risk_events.append(f"铜冠铜箔创新高止盈压力")
            else:
                risk_events.append(f"铜冠铜箔上涨趋势中")
        elif name == '*ST建艺':
            risk_events.append(f"*ST建艺摘帽窗口期")
        elif name == '雅克科技':
            risk_events.append(f"雅克科技HBM赛道高景气")
    
    risk_events_str = "、".join(risk_events)
    
    # 更新风险事件
    pattern = re.compile(
        r'(风险事件：</b>)([^<]+)(</span>)',
    )
    html = pattern.sub(lambda m: f'{m.group(1)}{risk_events_str}{m.group(3)}', html)
    
    # 构建当前状态描述
    status_parts = []
    for stock in stocks:
        name = stock['name']
        current = float(stock['current_price'])
        today_change = float(stock.get('today_change', 0)) * 100
        
        if name == '英维克':
            stop_loss = float(stock.get('stop_loss_price', 98))
            status_parts.append(f"英维克{current:.2f}元（{today_change:+.2f}%）vs 止损{stop_loss:.2f}元")
        elif name == '铜冠铜箔':
            status_parts.append(f"铜冠铜箔{current:.2f}元（{today_change:+.2f}%）创历史新高")
        elif name == '*ST建艺':
            status_parts.append(f"*ST建艺{current:.2f}元（{today_change:+.2f}%），摘帽审核进行中")
        elif name == '雅克科技':
            status_parts.append(f"雅克科技{current:.2f}元（{today_change:+.2f}%），HBM前驱体龙头")
    
    status_str = "；".join(status_parts)
    
    # 更新当前状态
    pattern = re.compile(
        r'(当前状态：</b>)([^<]+)(</span>)',
    )
    html = pattern.sub(lambda m: f'{m.group(1)}{status_str}{m.group(3)}', html)
    
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print("  ✅ 智能预警系统更新完成")

def main():
    print("=" * 60)
    print("📊 统一持仓数据更新系统")
    print("=" * 60)
    
    # 加载统一数据
    data = load_data()
    print(f"\n📁 数据源：data/portfolio.json")
    print(f"📈 持仓股票：{len(data['stocks'])}只")
    print(f"⏰ 更新时间：{data['portfolio']['update_time']}")
    print()
    
    # 1. 更新持仓智能预警仪表盘
    update_dashboard(data)
    print()
    
    # 2. 更新首页
    update_index_page(data)
    print()
    
    # 3. 更新智能预警系统
    update_warning_system(data)
    print()
    
    print("=" * 60)

    # 4. 归档历史快照（数据回溯功能）
    archive_history_snapshot()
    print()
    print("✅ 所有页面数据更新完成！")
    print("=" * 60)


def archive_history_snapshot():
    """归档当日持仓数据快照，用于数据回溯"""
    import shutil
    from datetime import date
    
    history_dir = 'data/history'
    os.makedirs(history_dir, exist_ok=True)
    
    today = date.today().strftime("%Y-%m-%d")
    src = 'data/portfolio.json'
    dst = os.path.join(history_dir, f'{today}.json')
    
    # 同一天多次更新只保留最新版本
    shutil.copy2(src, dst)
    print(f"📦 历史快照已归档：{dst}")

if __name__ == '__main__':
    main()
