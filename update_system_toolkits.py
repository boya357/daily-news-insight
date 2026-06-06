#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
系统工具箱统一更新脚本
- 智能预警系统
- 持仓智能预警仪表盘  
- 智能选题助手

策略：只更新标记区域，绝不碰布局结构
"""

import os
import re
import sys
from datetime import datetime

# 基础路径
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DOCS_DIR = os.path.join(BASE_DIR, 'docs')

# ============================================================
# 工具函数
# ============================================================

def read_file(filepath):
    """读取文件"""
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(filepath, content):
    """写入文件"""
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def get_update_time():
    """获取当前更新时间字符串"""
    now = datetime.now()
    return now.strftime('%m月%d日 %H:%M')

def safe_replace(html, pattern, replacement, description=""):
    """安全替换，如果找不到模式则警告但不中断"""
    if re.search(pattern, html):
        html = re.sub(pattern, replacement, html)
        print(f"   ✅ {description}")
    else:
        print(f"   ⚠️  未找到匹配项: {description}")
    return html

# ============================================================
# 智能预警系统更新
# ============================================================

def update_alert_system():
    """更新智能预警系统"""
    filepath = os.path.join(DOCS_DIR, '智能预警系统', 'index.html')
    if not os.path.exists(filepath):
        print(f"❌ 智能预警系统页面不存在: {filepath}")
        return False
    
    html = read_file(filepath)
    update_time = get_update_time()
    
    print("📊 更新智能预警系统...")
    
    # 1. 更新最后更新时间
    old_time_pattern = r'最后更新：\d+月\d+日 \d+:\d+'
    new_time_text = f'最后更新：{update_time}'
    html = safe_replace(html, old_time_pattern, new_time_text, "更新时间戳")
    
    # 2. 更新综合风险指数 (68 -> 75)
    old_risk_score = r'<div class="text-2xl font-black text-red-600">68</div>'
    new_risk_score = '<div class="text-2xl font-black text-red-600">75</div>'
    html = safe_replace(html, old_risk_score, new_risk_score, "综合风险指数 68→75")
    
    # 3. 更新风险等级描述
    old_risk_level = r'较高风险 · 严格风控'
    new_risk_level = '高风险 · 严控仓位'
    html = safe_replace(html, old_risk_level, new_risk_level, "风险等级描述")
    
    # 4. 更新建议仓位
    old_position = r'建议仓位：30-50%'
    new_position = '建议仓位：20-30%'
    html = safe_replace(html, old_position, new_position, "建议仓位")
    
    # 5. 更新大盘风险监控 - 风险事件
    old_market_event = r'科技股集体暴跌，PCB/CPO/光模块跌5-8%，高低切换剧烈'
    new_market_event = '美股黑色星期五，纳指暴跌4.18%，半导体指数跌10.26%，AI股集体重挫'
    html = safe_replace(html, old_market_event, new_market_event, "大盘风险-风险事件")
    
    # 更新当前状态
    old_market_status = r'英伟达COMPUTEX演讲后出现明显"利好兑现"行情，高位科技股集体遭抛售'
    new_market_status = '美国非农数据大超预期，加息预期急剧升温，全球科技股遭遇恐慌性抛售'
    html = safe_replace(html, old_market_status, new_market_status, "大盘风险-当前状态")
    
    # 6. 更新资金流向监控
    old_money_event = r'科技板块主力资金净流出超200亿，北向资金净卖出'
    new_money_event = '全球科技股遭遇抛售潮，单日市值蒸发1.75万亿美元，流动性冲击显现'
    html = safe_replace(html, old_money_event, new_money_event, "资金流向-风险事件")
    
    old_money_status = r'AI硬件端遭遇资金大幅撤离，资金向低位防御板块（煤炭/电力）切换'
    new_money_status = '避险资产（黄金/白银）与风险资产齐跌，现金为王，美元指数大涨站上100'
    html = safe_replace(html, old_money_status, new_money_status, "资金流向-当前状态")
    
    # 7. 更新持仓风险监控
    old_portfolio_status = r'英维克66\.06元 vs 止损98元，浮亏-36\.62%，严重破止损需立即执行'
    new_portfolio_status = '英维克68.32元 vs 止损98元，浮亏-34.45%，严重破止损；铜冠铜箔需警惕科技股回调风险'
    html = safe_replace(html, old_portfolio_status, new_portfolio_status, "持仓风险-当前状态")
    
    # 8. 更新消息面监控
    old_news_event = r'英伟达COMPUTEX大会圆满落幕'
    new_news_event = '美国非农数据大超预期，加息预期骤升'
    html = safe_replace(html, old_news_event, new_news_event, "消息面-重大事件")
    
    old_news_content = r'RTX Spark超级芯片、Vera CPU、Isaac GR00T人形机器人'
    new_news_content = '5月非农新增17.2万人（预期8.8万），11月加息概率升至65%'
    html = safe_replace(html, old_news_content, new_news_content, "消息面-数据详情")
    
    old_news_reaction = r'利好兑现，硬件端集体回调，AI PC逆势上涨'
    new_news_reaction = '全球市场恐慌性下跌，科技股遭血洗，VIX恐慌指数飙升60%+'
    html = safe_replace(html, old_news_reaction, new_news_reaction, "消息面-市场反应")
    
    # 9. 更新事件日历监控
    old_event_upcoming = r'6月3日苹果WWDC大会、6月18日美联储议息'
    new_event_upcoming = '6月18日美联储议息、6月12日SpaceX上市'
    html = safe_replace(html, old_event_upcoming, new_event_upcoming, "事件日历-即将到来")
    
    old_event_warning = r'警惕苹果AI功能发布不及预期风险'
    new_event_warning = '警惕美联储加息预期进一步升温，中东局势持续紧张'
    html = safe_replace(html, old_event_warning, new_event_warning, "事件日历-风险提示")
    
    # 写回文件
    write_file(filepath, html)
    
    print(f"✅ 智能预警系统更新完成（更新时间: {update_time}）")
    print(f"   页面路径: {filepath}")
    return True

# ============================================================
# 持仓智能预警仪表盘更新
# ============================================================

def update_portfolio_dashboard():
    """更新持仓智能预警仪表盘"""
    filepath = os.path.join(DOCS_DIR, '持仓智能预警仪表盘', 'index.html')
    if not os.path.exists(filepath):
        print(f"❌ 持仓智能预警仪表盘页面不存在: {filepath}")
        return False
    
    html = read_file(filepath)
    update_time = get_update_time()
    
    print("📊 更新持仓智能预警仪表盘...")
    
    # 更新最后更新时间
    old_time_pattern = r'最后更新：\d+月\d+日 \d+:\d+'
    new_time_text = f'最后更新：{update_time}'
    html = safe_replace(html, old_time_pattern, new_time_text, "更新时间戳")
    
    write_file(filepath, html)
    
    print(f"✅ 持仓智能预警仪表盘更新完成（更新时间: {update_time}）")
    print(f"   页面路径: {filepath}")
    return True

# ============================================================
# 智能选题助手更新
# ============================================================

def update_topic_helper():
    """更新智能选题助手"""
    filepath = os.path.join(DOCS_DIR, '智能选题助手', 'index.html')
    if not os.path.exists(filepath):
        print(f"❌ 智能选题助手页面不存在: {filepath}")
        return False
    
    html = read_file(filepath)
    update_time = get_update_time()
    
    print("📊 更新智能选题助手...")
    
    # 更新最后更新时间
    old_time_pattern = r'最后更新：\d+月\d+日 \d+:\d+'
    new_time_text = f'最后更新：{update_time}'
    html = safe_replace(html, old_time_pattern, new_time_text, "更新时间戳")
    
    write_file(filepath, html)
    
    print(f"✅ 智能选题助手更新完成（更新时间: {update_time}）")
    print(f"   页面路径: {filepath}")
    return True

# ============================================================
# 主函数
# ============================================================

def main():
    if len(sys.argv) > 1:
        mode = sys.argv[1]
    else:
        mode = 'all'
    
    print("=" * 60)
    print("📊 系统工具箱更新脚本 v1.0")
    print("=" * 60)
    print()
    
    success_count = 0
    
    if mode == 'all' or mode == 'alert':
        if update_alert_system():
            success_count += 1
        print()
    
    if mode == 'all' or mode == 'portfolio':
        if update_portfolio_dashboard():
            success_count += 1
        print()
    
    if mode == 'all' or mode == 'topic':
        if update_topic_helper():
            success_count += 1
        print()
    
    print("=" * 60)
    print(f"✅ 更新完成，成功更新 {success_count} 个工具")
    print("=" * 60)
    
    return success_count

if __name__ == '__main__':
    main()
