#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
持仓智能预警仪表盘 - 数据更新脚本
基于原版HTML，只更新数据，不改动UI结构
"""

import json
import os
import re
from bs4 import BeautifulSoup, Tag
from copy import copy

def load_data():
    """加载持仓数据"""
    data_path = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'portfolio.json')
    with open(data_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def update_text_by_label(soup, label_text, new_value, new_color_class=None):
    """
    通过标签文字找到对应的数值元素并更新
    比如找到"最新价"标签，然后更新它后面的数值
    """
    # 找到包含label_text的div
    label_div = soup.find(string=re.compile(label_text))
    if not label_div:
        print(f"  ⚠️  未找到标签：{label_text}")
        return False
    
    # 向上找父元素的兄弟元素（数值在标签的下一个div里）
    parent = label_div.parent
    if parent and parent.get('class') and 'text-xs' in parent.get('class', []):
        # 数值div是下一个兄弟元素
        value_div = parent.find_next_sibling('div')
        if value_div and 'text-xl' in value_div.get('class', []):
            value_div.string = str(new_value)
            if new_color_class:
                # 更新颜色类
                value_div['class'] = [c for c in value_div.get('class', []) 
                                     if c not in ['text-red-600', 'text-green-600', 'text-yellow-600', 'text-gray-700']]
                value_div['class'].append(new_color_class)
            return True
    return False

def get_stock_card(soup, stock_name):
    """获取指定股票的卡片元素"""
    # 找到包含股票名称的h2元素
    h2 = soup.find('h2', string=stock_name)
    if not h2:
        return None
    # 向上找到stock-card容器
    card = h2
    while card and card.name != 'div':
        card = card.parent
    while card and 'stock-card' not in card.get('class', []):
        card = card.parent
    return card

def update_stock_card(card_soup, stock_data):
    """更新单个股票卡片的数据"""
    name = stock_data['name']
    print(f"  更新 {name}...")
    
    # 更新成本价
    update_text_by_label(card_soup, '成本价', f"{stock_data['cost_price']:.2f}")
    
    # 更新最新价
    price_color = 'text-green-600' if stock_data['current_price'] >= stock_data['cost_price'] else 'text-red-600'
    update_text_by_label(card_soup, '最新价', f"{stock_data['current_price']:.2f}", price_color)
    
    # 更新止损价
    update_text_by_label(card_soup, '止损价', f"{stock_data['stop_loss_price']:.2f}")
    
    # 更新距止损/安全边际
    if 'distance_to_stop_loss' in stock_data:
        value = stock_data['distance_to_stop_loss']
        color = 'text-red-600' if value < 0 else 'text-green-600'
        update_text_by_label(card_soup, '距止损', f"{value*100:.2f}%", color)
    elif 'safety_margin' in stock_data:
        value = stock_data['safety_margin']
        color = 'text-green-600' if value > 0 else 'text-red-600'
        update_text_by_label(card_soup, '安全边际', f"{value*100:.2f}%", color)
    
    # 更新今日涨跌
    today_change = stock_data['today_change']
    today_color = 'text-green-600' if today_change >= 0 else 'text-red-600'
    update_text_by_label(card_soup, '今日涨跌', f"{today_change*100:+.2f}%", today_color)
    
    # 更新主力资金
    if 'main_fund' in stock_data:
        update_text_by_label(card_soup, '主力资金', stock_data['main_fund'])
    
    # 更新风险程度文字
    if 'risk_level' in stock_data:
        risk_label = card_soup.find(string=re.compile('风险程度'))
        if risk_label:
            risk_text_span = risk_label.parent.find_next_sibling('span')
            if risk_text_span:
                risk_text_span.string = stock_data['risk_level']
                if 'risk_color' in stock_data:
                    risk_text_span['class'] = [c for c in risk_text_span.get('class', []) 
                                              if c not in ['text-red-600', 'text-green-600', 'text-yellow-600']]
                    risk_text_span['class'].append(stock_data['risk_color'])
    
    # 更新风险进度条位置
    if 'risk_progress' in stock_data:
        progress_dot = card_soup.select_one('.absolute.-top-1')
        if progress_dot:
            progress_dot['style'] = f"left: {stock_data['risk_progress']}%;"
    
    # 更新持仓盈亏百分比（右上角大数字）
    profit_pct = (stock_data['current_price'] - stock_data['cost_price']) / stock_data['cost_price']
    profit_color = 'text-green-600' if profit_pct >= 0 else 'text-red-600'
    profit_div = card_soup.select_one('.text-4xl.font-black')
    if profit_div:
        profit_div.string = f"{profit_pct*100:+.2f}%"
        profit_div['class'] = [c for c in profit_div.get('class', []) 
                              if c not in ['text-red-600', 'text-green-600']]
        profit_div['class'].append(profit_color)
    
    # 更新四维诊断
    if 'diagnosis' in stock_data:
        diag = stock_data['diagnosis']
        # 技术面、资金面、消息面、产业面
        for key, title in [('technical', '技术面'), ('fund', '资金面'), 
                           ('news', '消息面'), ('industry', '产业面')]:
            # 找到对应的诊断卡片
            diag_items = card_soup.select('.grid.grid-cols-4 > div')
            for item in diag_items:
                title_span = item.find(string=re.compile(title))
                if title_span:
                    # 更新值
                    value_div = item.select_one('.text-lg.font-bold')
                    if value_div and key in diag:
                        value_div.string = diag[key]['value']
                        # 更新颜色
                        status = diag[key].get('status', 'neutral')
                        color_map = {
                            'good': 'text-green-600',
                            'bad': 'text-red-600',
                            'neutral': 'text-gray-600'
                        }
                        if status in color_map:
                            value_div['class'] = [c for c in value_div.get('class', []) 
                                                 if c not in ['text-red-600', 'text-green-600', 'text-gray-600']]
                            value_div['class'].append(color_map[status])
                    
                    # 更新描述
                    desc_div = item.select_one('.text-xs.text-gray-500')
                    if desc_div and key in diag:
                        desc_div.string = diag[key]['desc']
                    
                    break
    
    # 更新调仓建议（在卡片底部？不，调仓建议在压力测试区）
    # 压力测试部分后面单独处理
    
    print(f"  ✅ {name} 更新完成")
    return True

def update_portfolio_overview(soup, portfolio):
    """更新组合总览部分"""
    print("更新组合总览...")
    
    # 组合总盈亏
    total_return = portfolio['total_return']
    return_color = 'text-green-600' if total_return >= 0 else 'text-red-600'
    return_div = soup.find(string=re.compile('组合总盈亏'))
    if return_div:
        parent = return_div.parent
        value_div = parent.find_previous_sibling('div')
        if value_div:
            value_div.string = f"{total_return*100:+.2f}%"
            value_div['class'] = [c for c in value_div.get('class', []) 
                                 if c not in ['text-red-600', 'text-green-600']]
            value_div['class'].append(return_color)
    
    # 健康分
    health_score = portfolio['health_score']
    health_color = 'text-green-600' if health_score >= 60 else 'text-yellow-600'
    health_div = soup.find(string=re.compile('健康分'))
    if health_div:
        parent = health_div.parent
        value_div = parent.find_previous_sibling('div')
        if value_div:
            value_div.string = str(health_score)
            value_div['class'] = [c for c in value_div.get('class', []) 
                                 if c not in ['text-red-600', 'text-green-600', 'text-yellow-600']]
            value_div['class'].append(health_color)
    
    # 更新健康环的进度
    health_ring = soup.select_one('.health-ring-green')
    if health_ring:
        health_ring['style'] = f"--p: {health_score}%;"
    
    # 更新5个统计卡片
    stats = {
        '持仓标的': f"{portfolio['stock_count']}只",
        '盈利标的': f"{portfolio['profit_count']}只",
        '亏损标的': f"{portfolio['loss_count']}只",
        '跌破止损': f"{portfolio['stop_loss_break_count']}只",
        '行业分布': f"{portfolio['industry_count']}个",
    }
    
    for label, value in stats.items():
        stat_div = soup.find(string=re.compile(label))
        if stat_div:
            parent = stat_div.parent
            value_div = parent.find_previous_sibling('div')
            if value_div:
                value_div.string = value
    
    print("✅ 组合总览更新完成")

def update_stress_test(soup, stocks):
    """更新压力测试部分"""
    print("更新压力测试...")
    
    # 找到压力测试区域
    stress_section = soup.find(string=re.compile('压力测试情景'))
    if not stress_section:
        print("  ⚠️  未找到压力测试区域")
        return
    
    # 找到极端情景和中性情景的网格
    grids = soup.select('.grid.grid-cols-4')
    if len(grids) >= 2:
        extreme_grid = grids[0]  # 第一个是极端情景
        neutral_grid = grids[1]  # 第二个是中性情景
        
        extreme_items = extreme_grid.select('div')
        neutral_items = neutral_grid.select('div')
        
        for i, stock in enumerate(stocks):
            if i < len(extreme_items):
                # 更新极端情景价格
                price_div = extreme_items[i].select_one('.text-lg.font-bold')
                if price_div and 'stress_test' in stock:
                    price_div.string = stock['stress_test']['extreme']
            
            if i < len(neutral_items):
                # 更新中性情景价格
                price_div = neutral_items[i].select_one('.text-lg.font-bold')
                if price_div and 'stress_test' in stock:
                    price_div.string = stock['stress_test']['neutral']
    
    print("✅ 压力测试更新完成")

def update_advice(soup, stocks, overall_advice):
    """更新调仓建议部分"""
    print("更新调仓建议...")
    
    advice_section = soup.find(string=re.compile('智能调仓建议'))
    if not advice_section:
        print("  ⚠️  未找到调仓建议区域")
        return
    
    # 找到所有建议段落
    advice_div = advice_section.find_next('div', class_='space-y-3')
    if not advice_div:
        print("  ⚠️  未找到建议内容区域")
        return
    
    p_tags = advice_div.find_all('p')
    
    # 前N个是各股票的建议，最后一个是总建议
    for i, stock in enumerate(stocks):
        if i < len(p_tags) - 1:  # 留最后一个给总建议
            p_tags[i].string = stock.get('advice', '')
    
    # 更新总建议
    if p_tags:
        p_tags[-1].string = overall_advice
    
    print("✅ 调仓建议更新完成")

def update_update_time(soup, update_time):
    """更新数据更新时间"""
    # 标题区的更新时间
    time_p = soup.find(string=re.compile('数据更新时间'))
    if time_p:
        time_p.replace_with(f"数据更新时间：{update_time}")
    
    # 页脚的更新时间
    footer_p = soup.find_all(string=re.compile('持仓智能预警仪表盘'))
    for p in footer_p:
        if '·' in str(p):
            p.replace_with(f"持仓智能预警仪表盘 · {update_time}")

def main():
    print("=" * 50)
    print("持仓智能预警仪表盘 - 数据更新")
    print("=" * 50)
    
    # 加载数据
    data = load_data()
    stocks = data['stocks']
    portfolio = data['portfolio']
    
    print(f"加载了 {len(stocks)} 只股票数据")
    
    # 读取原HTML
    html_path = os.path.join(os.path.dirname(__file__), '..', '..', 'docs', '持仓智能预警仪表盘', 'index.html.bak.original')
    if not os.path.exists(html_path):
        html_path = html_path.replace('.bak.original', '')
    
    print(f"读取模板：{html_path}")
    
    with open(html_path, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # 更新组合总览
    update_portfolio_overview(soup, portfolio)
    
    # 更新每个股票卡片
    for stock in stocks:
        card = get_stock_card(soup, stock['name'])
        if card:
            update_stock_card(card, stock)
        else:
            print(f"  ⚠️  未找到 {stock['name']} 的卡片")
    
    # 更新压力测试
    update_stress_test(soup, stocks)
    
    # 更新调仓建议
    update_advice(soup, stocks, portfolio['overall_advice'])
    
    # 更新更新时间
    update_update_time(soup, portfolio['update_time'])
    
    # 保存
    output_path = os.path.join(os.path.dirname(__file__), '..', '..', 'docs', '持仓智能预警仪表盘', 'index.html')
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(str(soup))
    
    print(f"\n✅ 更新完成！保存到：{output_path}")
    print(f"   共更新 {len(stocks)} 只股票数据")

if __name__ == '__main__':
    main()
