#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
持仓智能预警仪表盘每日更新脚本
"""

import re
from datetime import datetime

def update_portfolio_dashboard():
    html_path = "docs/portfolio_dashboard/index.html"
    
    # 读取文件
    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 备份原文件
    backup_path = html_path + ".bak." + datetime.now().strftime("%Y%m%d_%H%M%S")
    with open(backup_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"✅ 已备份原文件到 {backup_path}")
    
    # ========== 英维克数据更新 ==========
    # 最新价：63.38 → 69.72
    old = '<div class="text-xs text-gray-500 mb-1">最新价</div>\n                        <div class="text-xl font-bold text-red-600">63.38</div>'
    new = '<div class="text-xs text-gray-500 mb-1">最新价</div>\n                        <div class="text-xl font-bold text-red-600">69.72</div>'
    content = content.replace(old, new)
    
    # 今日涨跌：-3.82% → +10.0%
    old = '<div class="text-xs text-gray-500 mb-1">今日涨跌</div>\n                        <div class="text-xl font-bold text-red-600">-3.82%</div>'
    new = '<div class="text-xs text-gray-500 mb-1">今日涨跌</div>\n                        <div class="text-xl font-bold text-green-600">+10.0%</div>'
    content = content.replace(old, new)
    
    # 距止损：-35.33% → -28.86%
    old = '<div class="text-xs text-gray-500 mb-1">距止损</div>\n                        <div class="text-xl font-bold text-red-600">-35.33%</div>'
    new = '<div class="text-xs text-gray-500 mb-1">距止损</div>\n                        <div class="text-xl font-bold text-red-600">-28.86%</div>'
    content = content.replace(old, new)
    
    # 风险程度
    content = content.replace('高危区 - 严重跌破止损线', '高危区 - 已跌破止损线')
    
    # ========== 铜冠铜箔数据更新 ==========
    # 最新价：113.10 → 122.76
    old = '<div class="text-xs text-gray-500 mb-1">最新价</div>\n                        <div class="text-xl font-bold text-green-600">113.10</div>'
    new = '<div class="text-xs text-gray-500 mb-1">最新价</div>\n                        <div class="text-xl font-bold text-green-600">122.76</div>'
    content = content.replace(old, new)
    
    # 安全边际：+33.06% → +44.42%
    old = '<div class="text-xs text-gray-500 mb-1">安全边际</div>\n                        <div class="text-xl font-bold text-green-600">+33.06%</div>'
    new = '<div class="text-xs text-gray-500 mb-1">安全边际</div>\n                        <div class="text-xl font-bold text-green-600">+44.42%</div>'
    content = content.replace(old, new)
    
    # 今日涨跌：+1.65% → +8.54%
    old = '<div class="text-xs text-gray-500 mb-1">今日涨跌</div>\n                        <div class="text-xl font-bold text-green-600">+1.65%</div>'
    new = '<div class="text-xs text-gray-500 mb-1">今日涨跌</div>\n                        <div class="text-xl font-bold text-green-600">+8.54%</div>'
    content = content.replace(old, new)
    
    # ========== *ST建艺数据更新 ==========
    # 最新价：13.02 → 13.33
    old = '<div class="text-xs text-gray-500 mb-1">最新价</div>\n                        <div class="text-xl font-bold text-green-600">13.02</div>'
    new = '<div class="text-xs text-gray-500 mb-1">最新价</div>\n                        <div class="text-xl font-bold text-green-600">13.33</div>'
    content = content.replace(old, new)
    
    # 安全边际：+4.16% → +6.64%
    old = '<div class="text-xs text-gray-500 mb-1">安全边际</div>\n                        <div class="text-xl font-bold text-green-600">+4.16%</div>'
    new = '<div class="text-xs text-gray-500 mb-1">安全边际</div>\n                        <div class="text-xl font-bold text-green-600">+6.64%</div>'
    content = content.replace(old, new)
    
    # 今日涨跌：-2.62% → +2.38%
    old = '<div class="text-xs text-gray-500 mb-1">今日涨跌</div>\n                        <div class="text-xl font-bold text-green-600">-2.62%</div>'
    new = '<div class="text-xs text-gray-500 mb-1">今日涨跌</div>\n                        <div class="text-xl font-bold text-green-600">+2.38%</div>'
    content = content.replace(old, new)
    
    # ========== 组合总览数据更新 ==========
    # 组合总盈亏：-9.91% → +2.28%
    old = '<div class="text-4xl font-black text-red-600">-9.91%</div>'
    new = '<div class="text-4xl font-black text-green-600">+2.28%</div>'
    content = content.replace(old, new)
    
    # 健康分：57 → 65
    content = content.replace(
        'health-ring-yellow w-24 h-24 rounded-full flex items-center justify-center" style="--p: 57%;"',
        'health-ring-green w-24 h-24 rounded-full flex items-center justify-center" style="--p: 65%;"'
    )
    content = content.replace(
        '<div class="text-2xl font-black text-yellow-600">57</div>',
        '<div class="text-2xl font-black text-green-600">65</div>'
    )
    
    # ========== 智能调仓建议更新 ==========
    # 英维克建议
    content = content.replace(
        '英维克已严重跌破止损位，亏损幅度达-39.19%，建议明日开盘立即执行止损操作，避免亏损进一步扩大。',
        '英维克今日强势涨停（+10%），AI液冷散热概念持续发酵，短期反弹动能强劲，建议持有观察，若能站上75元可考虑加仓，止损位维持85元。'
    )
    
    # 铜冠铜箔建议
    content = content.replace(
        '铜冠铜箔今日低开高走收涨1.65%，储能+PCB铜箔需求持续增长，建议继续持有，止损位上调至95元保护利润。',
        '铜冠铜箔今日大涨+8.54%，创上市新高，储能+AI服务器PCB铜箔需求爆发，建议继续持有，止损位上调至105元保护利润。'
    )
    
    # *ST建艺建议
    content = content.replace(
        '*ST建艺今日小幅回调2.62%，摘帽预期仍在，建议继续持有，跌破12.5元止损。',
        '*ST建艺今日收涨+2.38%，摘帽审核进行中，预期近期将有结果，建议继续持有，跌破12.5元止损。'
    )
    
    # 再平衡建议
    content = content.replace(
        '止损英维克后腾出的资金，建议分散配置到低位防御板块（消费/医药），降低组合整体波动率，规避科技股高位回调风险。',
        '科技成长赛道今日全面反弹，AI算力链表现强劲，建议维持当前持仓结构，重点关注铜冠铜箔的趋势性机会，英维克反弹后可考虑逐步减仓降低亏损。'
    )
    
    # 建议类型标签
    content = content.replace(
        '<div class="p-4 bg-red-50 border border-red-200 rounded-xl border-l-4 border-l-red-500">\n                        <div class="font-bold text-red-700 mb-1">🔴 卖出建议</div>',
        '<div class="p-4 bg-yellow-50 border border-yellow-200 rounded-xl border-l-4 border-l-yellow-500">\n                        <div class="font-bold text-yellow-700 mb-1">🟡 持有观察</div>'
    )
    
    # ========== 数据更新时间 ==========
    content = re.sub(
        r'数据更新时间：2026年\d+月\d+日 \d+:\d+',
        '数据更新时间：2026年6月9日 21:30',
        content
    )
    content = re.sub(
        r'（数据截至\d+月\d+日收盘）',
        '（数据截至6月9日收盘）',
        content
    )
    
    # 保存更新后的文件
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✅ 持仓智能预警仪表盘更新完成")
    print("   - 英维克：69.72元 (+10.0%)")
    print("   - 铜冠铜箔：122.76元 (+8.54%)")
    print("   - *ST建艺：13.33元 (+2.38%)")
    print("   - 组合总盈亏：+2.28%")
    print("   - 健康分：65分")
    
    return True

if __name__ == "__main__":
    update_portfolio_dashboard()
