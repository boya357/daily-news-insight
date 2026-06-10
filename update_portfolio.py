#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
持仓智能预警仪表盘 - 完整数据更新脚本
基于原版HTML，数据驱动，UI保持100%一致
"""

import json
import os
import re

def load_data():
    """加载持仓数据"""
    data_path = 'data/portfolio.json'
    with open(data_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def update_portfolio(html, portfolio):
    """更新组合总览"""
    # 总盈亏
    total_return = portfolio['total_return']
    return_color = 'text-green-600' if total_return >= 0 else 'text-red-600'
    return_text = f"{total_return*100:+.2f}%"
    
    # 找到并替换总盈亏（第一个text-4xl font-black
    pattern = re.compile(r'<div class="text-4xl font-black [^"]+">[^<]+</div>(?=\s*<div class="text-sm text-gray-500">组合总盈亏</div>)')
    html = pattern.sub(f'<div class="text-4xl font-black {return_color}">{return_text}</div>', html)
    
    # 健康分
    health_score = portfolio['health_score']
    health_color = 'text-green-600' if health_score >= 60 else 'text-yellow-600'
    
    pattern = re.compile(r'<div class="text-2xl font-black [^"]+">\d+</div>(?=\s*<div class="text-xs text-gray-500">健康分</div>)')
    html = pattern.sub(f'<div class="text-2xl font-black {health_color}">{health_score}</div>', html)
    
    # 健康环
    pattern = re.compile(r'health-ring-green[^"]*"[^>]*style="--p: \d+%;')
    html = pattern.sub(f'health-ring-green" style="--p: {health_score}%;', html)
    
    # 5个统计卡片
    stats = [
        ('持仓标的', f"{portfolio['stock_count']}只", 'text-gray-800'),
        ('盈利标的', f"{portfolio['profit_count']}只", 'text-green-600'),
        ('亏损标的', f"{portfolio['loss_count']}只", 'text-red-600'),
        ('跌破止损', f"{portfolio['stop_loss_break_count']}只", 'text-yellow-600'),
        ('行业分布', f"{portfolio['industry_count']}个", 'text-purple-600'),
    ]
    
    for label, value, color in stats:
        pattern = re.compile(
            rf'(<div class="text-sm text-gray-600 mb-1">{re.escape(label)}</div>\s*<div class="text-2xl font-black )([a-z0-9-]+)(">)([^<]+)(</div>)',
            re.DOTALL
        )
        html = pattern.sub(rf'\1{color}\3{value}\5', html)
    
    # 更新时间
    html = html.replace('数据更新时间：2026年6月10日 21:30', f'数据更新时间：{portfolio["update_time"]}')
    
    return html

def extract_card_html(html, stock_name):
    """提取指定股票卡片的HTML"""
    start_marker = f'<!-- {stock_name} -->'
    start_idx = html.find(start_marker)
    if start_idx == -1:
        return None, None, None
    
    # 找到下一个卡片或下一个主要区域的开始
    next_markers = [
        '<!-- 铜冠铜箔 -->',
        '<!-- *ST建艺 -->', 
        '<!-- 雅克科技 -->',
        '<!-- 【第三区：压力测试与调仓建议】 -->',
    ]
    
    end_idx = len(html)
    for marker in next_markers:
        if marker == start_marker:
            continue
        idx = html.find(marker, start_idx + len(start_marker))
        if idx != -1 and idx < end_idx:
            end_idx = idx
    
    return start_idx, end_idx, html[start_idx:end_idx]

def update_stock_card(card_html, stock):
    """更新单个股票卡片"""
    name = stock['name']
    
    # 成本价
    pattern = re.compile(
        r'(<div class="text-xs text-gray-500 mb-1">成本价</div>\s*<div class="text-xl font-bold )([a-z0-9-]+)(">)([^<]+)(</div>)',
        re.DOTALL
    )
    card_html = pattern.sub(rf'\1text-gray-700\3{stock["cost_price"]:.2f}\5', card_html)
    
    # 最新价
    price_color = 'text-green-600' if stock['current_price'] >= stock['cost_price'] else 'text-red-600'
    pattern = re.compile(
        r'(<div class="text-xs text-gray-500 mb-1">最新价</div>\s*<div class="text-xl font-bold )([a-z0-9-]+)(">)([^<]+)(</div>)',
        re.DOTALL
    )
    card_html = pattern.sub(rf'\1{price_color}\3{stock["current_price"]:.2f}\5', card_html)
    
    # 止损价
    pattern = re.compile(
        r'(<div class="text-xs text-gray-500 mb-1">止损价</div>\s*<div class="text-xl font-bold )([a-z0-9-]+)(">)([^<]+)(</div>)',
        re.DOTALL
    )
    card_html = pattern.sub(rf'\1text-gray-700\3{stock["stop_loss_price"]:.2f}\5', card_html)
    
    # 距止损 / 安全边际
    if 'distance_to_stop_loss' in stock:
        value = stock['distance_to_stop_loss']
        label = '距止损'
        color = 'text-red-600' if value < 0 else 'text-green-600'
        text = f"{value*100:.2f}%"
    else:
        value = stock['safety_margin']
        label = '安全边际'
        color = 'text-green-600' if value > 0 else 'text-red-600'
        text = f"{value*100:.2f}%"
    
    pattern = re.compile(
        rf'(<div class="text-xs text-gray-500 mb-1">{re.escape(label)}</div>\s*<div class="text-xl font-bold )([a-z0-9-]+)(">)([^<]+)(</div>)',
        re.DOTALL
    )
    card_html = pattern.sub(rf'\1{color}\3{text}\5', card_html)
    
    # 今日涨跌
    today_change = stock['today_change']
    today_color = 'text-green-600' if today_change >= 0 else 'text-red-600'
    today_text = f"{today_change*100:+.2f}%"
    pattern = re.compile(
        r'(<div class="text-xs text-gray-500 mb-1">今日涨跌</div>\s*<div class="text-xl font-bold )([a-z0-9-]+)(">)([^<]+)(</div>)',
        re.DOTALL
    )
    card_html = pattern.sub(rf'\1{today_color}\3{today_text}\5', card_html)
    
    # 主力资金
    if 'main_fund' in stock:
        pattern = re.compile(
            r'(<div class="text-xs text-gray-500 mb-1">主力资金</div>\s*<div class="text-xl font-bold )([a-z0-9-]+)(">)([^<]+)(</div>)',
            re.DOTALL
        )
        fund_color = 'text-red-600' if stock['main_fund'].startswith('-') else 'text-green-600'
        card_html = pattern.sub(rf'\1{fund_color}\3{stock["main_fund"]}\5', card_html)
    
    # 右上角持仓盈亏
    profit_pct = (stock['current_price'] - stock['cost_price']) / stock['cost_price']
    profit_color = 'text-green-600' if profit_pct >= 0 else 'text-red-600'
    profit_text = f"{profit_pct*100:+.2f}%"
    
    # 找到第一个text-4xl font-black（持仓盈亏
    pattern = re.compile(
        r'(<div class="text-4xl font-black )([a-z0-9-]+)(">)([+-]?\d+\.\d+%)(</div>)',
    )
    # 只替换第一个匹配（卡片内的）
    card_html = pattern.sub(rf'\1{profit_color}\3{profit_text}\5', card_html, count=1)
    
    # 风险程度
    if 'risk_level' in stock:
        risk_color = stock.get('risk_color', 'text-yellow-600')
        pattern = re.compile(
            r'(<span class=")([a-z0-9-]+)( font-bold">)([^<]+)(</span>)',
        )
        # 找到风险程度附近的span
        risk_idx = card_html.find('风险程度')
        if risk_idx != -1:
            nearby = card_html[risk_idx:risk_idx+300]
            match = pattern.search(nearby)
            if match:
                old_span = match.group(0)
                new_span = f'{match.group(1)}{risk_color}{match.group(3)}{stock["risk_level"]}{match.group(5)}'
                card_html = card_html[:risk_idx] + nearby.replace(old_span, new_span) + card_html[risk_idx+300:]
    
    # 风险进度条位置
    if 'risk_progress' in stock:
        progress = stock['risk_progress']
        pattern = re.compile(
            r'(<div class="absolute -top-1" style="left: )(\d+)(%;")',
        )
        risk_idx = card_html.find('风险程度')
        if risk_idx != -1:
            nearby = card_html[risk_idx:risk_idx+400]
            match = pattern.search(nearby)
            if match:
                old = match.group(0)
                new = f'{match.group(1)}{progress}{match.group(3)}'
                card_html = card_html[:risk_idx] + nearby.replace(old, new) + card_html[risk_idx+400:]
    
    # 四维诊断 - 技术面、资金面、消息面、产业面
    if 'diagnosis' in stock:
        diag = stock['diagnosis']
        diag_items = re.findall(r'<div class="p-4.*?</div>\s*</div>', card_html, re.DOTALL)
        
        # 四个诊断项，按顺序对应
        diag_keys = ['technical', 'fund', 'news', 'industry']
        
        for i, key in enumerate(diag_keys):
            if i >= len(diag_items):
                break
            item_html = diag_items[i]
            d = diag[key]
            
            # 更新值和颜色
            status = d.get('status', 'neutral')
            color_map = {
                'good': ('text-green-600', 'bg-green-50', 'border-green-100'
            ,
            }
            if status == 'bad':
                value_color = 'text-red-600'
                bg_color = 'bg-red-50'
                border_color = 'border-red-100'
            elif status == 'good':
                value_color = 'text-green-600'
                bg_color = 'bg-green-50'
                border_color = 'border-green-100'
            else:
                value_color = 'text-gray-600'
                bg_color = 'bg-gray-50'
                border_color = 'border-gray-100'
            
            # 更新值
            old_value_pattern = re.compile(r'<div class="text-lg font-bold [^"]+">[^<]+</div>')
            item_html = value_pattern.search(item_html)
            if value_match:
                old_value = value_match.group(0)
                new_value = f'<div class="text-lg font-bold {value_color}">{d["value"]}</div>'
                item_html = item_html.replace(old_value, new_value)
            
            # 更新描述
            desc_pattern = re.compile(r'<div class="text-xs text-gray-500">[^<]+</div>')
            desc_match = desc_pattern.search(item_html)
            if desc_match:
                old_desc = desc_match.group(0)
                new_desc = f'<div class="text-xs text-gray-500">{d["desc"]}</div>'
                item_html = item_html.replace(old_desc, new_desc)
            
            # 替换回卡片
            card_html = card_html.replace(diag_items[i], item_html)
    
    return card_html

def update_stress_test(html, stocks):
    """更新压力测试"""
    
    # 极端情景
    extreme_values = [s['stress_test']['extreme'] for s in stocks]
    neutral_values = [s['stress_test']['neutral'] for s in stocks]
    
    # 找到极端情景部分
    extreme_start = html.find('极端下跌情景')
    neutral_start = html.find('中性情景')
    
    if extreme_start == -1 or neutral_start == -1:
        print("  ⚠️  未找到压力测试区域")
        return html
    
    # 提取极端情景网格
    extreme_section = html[extreme_start:neutral_start]
    # 找到所有font-bold的数值
    # 按顺序替换
    extreme_pattern = re.compile(r'<div class="font-bold text-red-600">([^<]+</div>|<div class="font-bold text-yellow-600">([^<]+)</div>')
    
    # 简化：直接按股票名称定位数值
    stock_names = [s['name'] for s in stocks]
    for i, name in enumerate(stock_names):
        # 找到股票名称后的第一个font-bold div
        pattern = re.compile(rf'{re.escape(name)}</div>\s*<div class="font-bold text-[a-z0-9-]+">([^<]+)</div>')
        match = pattern.search(extreme_section)
        if match:
            old_val = match.group(1)
            new_val = extreme_values[i]
            extreme_section = extreme_section.replace(old_val, new_val, 1)
    
    # 替换回html
    html = html[:extreme_start] + extreme_section + html[extreme_start + len(extreme_section):]
    
    # 中性情景
    # 找到中性情景到下一个大标题
    advice_start = html.find('智能调仓建议', neutral_start)
    if advice_start == -1:
        advice_start = len(html)
    
    neutral_section = html[neutral_start:advice_start]
    
    for i, name in enumerate(stock_names):
        pattern = re.compile(rf'{re.escape(name)}</div>\s*<div class="font-bold text-[a-z0-9-]+">([^<]+)</div>')
        match = pattern.search(neutral_section)
        if match:
            old_val = match.group(1)
            new_val = neutral_values[i]
            neutral_section = neutral_section.replace(old_val, new_val, 1)
    
    html = html[:neutral_start] + neutral_section + html[neutral_start + len(neutral_section):]
    
    return html

def update_advice(html, stocks, overall_advice):
    """更新调仓建议"""
    
    # 找到智能调仓建议区域
    advice_start = html.find('智能调仓建议')
    if advice_start == -1:
        print("  ⚠️  未找到调仓建议区域")
        return html
    
    # 找到区域结束位置（页脚之前）
    footer_start = html.find('MLCC Pro v2.0', advice_start)
    if footer_start == -1:
        footer_start = len(html)
    
    advice_section = html[advice_start:footer_start]
    
    # 找到所有建议卡片（p标签里的文本
    # 前4个是个股建议，最后1个是总建议
    
    # 简单方法：按股票名称替换对应建议文本
    for stock in stocks:
        name = stock['name']
        advice_text = stock['advice']['text']
        
        # 找到包含该股票名称的p标签，替换整个p标签内容
        # 找到股票名称后面的建议文本
        # 简化：直接替换股票名称开头的句子
        # 这比较麻烦，简化处理，直接替换包含股票名称的整个p标签内容
        
        # 找到包含该股票名的p标签
        pattern = re.compile(rf'<p class="text-sm text-gray-700">[^<]*{re.escape(name)}[^<]*</p>')
        match = pattern.search(advice_section)
        if match:
            old_p = match.group(0)
            new_p = f'<p class="text-sm text-gray-700">{advice_text}</p>'
            advice_section = advice_section.replace(old_p, new_p)
    
    # 更新总建议（包含"科技成长赛道"或"建议"
    # 找最后一个p标签
    # 简化：直接找包含"建议维持"或最后一个p
    overall_idx = advice_section.rfind('<p class="text-sm text-gray-700">')
    if overall_idx != -1:
        # 找到这个p的闭合
        p_end = advice_section.find('</p>', overall_idx)
        if p_end != -1:
            old_p = advice_section[overall_idx:p_end+4]
            new_p = f'<p class="text-sm text-gray-700">{overall_advice}</p>'
            advice_section = advice_section[:overall_idx] + new_p + advice_section[p_end+4:]
    
    # 替换回html
    html = html[:advice_start] + advice_section + html[advice_start + len(advice_section):]
    
    return html

def main():
    print("=" * 50)
    print("持仓智能预警仪表盘 - 数据更新")
    print("=" * 50)
    
    # 加载数据
    data = load_data()
    stocks = data['stocks']
    portfolio = data['portfolio']
    
    print(f"加载了 {len(stocks)} 只股票数据")
    
    # 读取原HTML模板
    template_path = 'docs/持仓智能预警仪表盘/index.html.bak.original'
    if not os.path.exists(template_path):
        template_path = 'templates/portfolio_dashboard.html'
    
    print(f"读取模板：{template_path}")
    
    with open(template_path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    original_size = len(html)
    
    # 更新组合总览
    print("\n1. 更新组合总览...")
    html = update_portfolio(html, portfolio)
    print("   ✅ 完成")
    
    # 更新每个股票卡片
    print("\n2. 更新持仓卡片...")
    for stock in stocks:
        print(f"   处理 {stock['name']}...")
        start_idx, end_idx, card_html = extract_card_html(html, stock['name'])
        if card_html:
            new_card = update_stock_card(card_html, stock)
            html = html[:start_idx] + new_card + html[end_idx:]
            print(f"   ✅ {stock['name']} 更新完成")
        else:
            print(f"   ⚠️  未找到 {stock['name']} 的卡片")
    
    # 更新压力测试
    print("\n3. 更新压力测试...")
    html = update_stress_test(html, stocks)
    print("   ✅ 完成")
    
    # 更新调仓建议
    print("\n4. 更新调仓建议...")
    html = update_advice(html, stocks, portfolio['overall_advice'])
    print("   ✅ 完成")
    
    # 保存
    output_path = 'docs/持仓智能预警仪表盘/index.html'
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
    
    new_size = len(html)
    diff_pct = (new_size - original_size) / original_size * 100
    
    print(f"\n✅ 更新完成！保存到：{output_path}")
    print(f"   原文件大小：{original_size/1024:.1f}KB")
    print(f"   新文件大小：{new_size/1024:.1f}KB")
    print(f"   大小差异：{diff_pct:+.1f}%")

if __name__ == '__main__':
    main()
