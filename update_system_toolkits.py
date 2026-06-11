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
    return now.strftime('%Y年%-m月%-d日 %H:%M')

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
    old_time_pattern = r'数据更新时间：\d+年\d+月\d+日 \d+:\d+'
    new_time_text = f'数据更新时间：{update_time}'
    html = safe_replace(html, old_time_pattern, new_time_text, "更新时间戳")
    
    # 2. 更新大盘风险监控 - 风险事件
    old_market_event = r'沪指失守4000点，创业板跌2.7%，超3800股下跌，电子板块领跌'
    new_market_event = '指数微跌但个股普跌，超4000股下跌，结构性分化加剧'
    html = safe_replace(html, old_market_event, new_market_event, "大盘风险-风险事件")
    
    # 更新大盘风险-当前状态
    old_market_status = r'6月10日A股震荡调整，沪指跌0.42%失守4000点，创业板指跌2.7%。两市成交2.62万亿缩量，超3800股下跌。大金融护盘，科技股、煤炭、电力领跌。电子板块主力净流出339亿，市场观望情绪浓厚'
    new_market_status = '6月11日A股震荡分化，沪指跌0.16%收3987.01点，创业板指跌1.13%。两市成交2.55万亿缩量，超4000股下跌。半导体材料、小金属逆势走强，AI应用、文化传媒领跌。权重护盘但个股普跌，赚钱效应差'
    html = safe_replace(html, old_market_status, new_market_status, "大盘风险-当前状态")
    
    # 3. 更新资金流向监控 - 风险事件
    old_money_event = r'主力资金单日净流出超千亿，电子板块遭大幅抛售，科技ETF持续赎回'
    new_money_event = '主力净流出超400亿，AI题材持续失血，防御板块获资金青睐'
    html = safe_replace(html, old_money_event, new_money_event, "资金流向-风险事件")
    
    # 更新资金流向-当前状态
    old_money_status = r'今日主力净流出1050亿元，北向资金观望，资金向大金融防御板块切换，科技成长持续失血。电子板块净流出339亿居首，通信、电新板块也遭遇撤离。银行、保险获资金流入'
    new_money_status = '今日主力净流出约430亿元，北向资金小幅净流出。资金从高位AI题材向低位半导体材料、资源股切换。电子、计算机板块资金流出居前，银行、有色获小幅流入'
    html = safe_replace(html, old_money_status, new_money_status, "资金流向-当前状态")
    
    # 4. 更新持仓风险监控 - 风险事件
    old_portfolio_event = r'英维克下跌2.55%浮亏扩大至-18.9%、铜冠铜箔涨4.22%创新高、*ST建艺震荡摘帽窗口临近、雅克科技涨停HBM逻辑强化'
    new_portfolio_event = '英维克持续走弱浮亏扩大，雅克科技两连板累计涨21%，铜冠铜箔续创新高'
    html = safe_replace(html, old_portfolio_event, new_portfolio_event, "持仓风险-风险事件")
    
    # 更新持仓风险-当前状态
    old_portfolio_status = r'英维克69.72元 vs 止损98元，浮亏约-14%，震荡整理；铜冠铜箔122.76元创历史新高，持有；*ST建艺13.33元摘帽审核中；雅克科技约113元，小幅浮盈'
    new_portfolio_status = '英维克67.14元（-2.55%）vs 止损98元，浮亏约-31.5%，走势偏弱；铜冠铜箔127.98元（+4.22%）再创历史新高；*ST建艺12.99元（+1.88%）摘帽审核中；雅克科技134.81元（+10.00%）涨停，两连板累计涨21%'
    html = safe_replace(html, old_portfolio_status, new_portfolio_status, "持仓风险-当前状态")
    
    # 5. 更新题材热度监控 - 风险事件
    old_topic_event = r'科技题材集体退潮，AI算力/液冷/CPO调整，市场热点散乱持续性差'
    new_topic_event = '市场风格切换，AI题材退潮，半导体材料、资源股逆势走强'
    html = safe_replace(html, old_topic_event, new_topic_event, "题材热度-风险事件")
    
    # 更新题材热度-当前状态
    old_topic_status = r'英维克67.14元（-2.55%），铜冠铜箔127.98元（+4.22%）创历史新高，*ST建艺12.99元（+1.88%）摘帽审核中，雅克科技134.81元（+10.00%）涨停'
    new_topic_status = '今日半导体材料、光刻机、小金属板块涨幅居前，AI应用、文化传媒、算力租赁领跌。雅克科技（HBM）涨停带动半导体材料板块，英维克（液冷）跌2.55%'
    html = safe_replace(html, old_topic_status, new_topic_status, "题材热度-当前状态")
    
    # 6. 更新消息面监控 - 重大事件
    old_news_event = r'美国5月CPI同比升至4.2%超预期，美联储加息预期升温；工信部发布AI+信息通信创新发展意见'
    new_news_event = '美国5月CPI同比升至4.2%超预期，美联储降息预期降温；中东局势升级，霍尔木兹海峡关闭，油价大涨'
    html = safe_replace(html, old_news_event, new_news_event, "消息面-重大事件")
    
    # 更新消息面-市场反应
    old_news_reaction = r'美股纳指跌0.97%，费城半导体跌1.93%；A股创业板跌2.7%，科技股承压；黄金油价齐跌'
    new_news_reaction = '美股道指跌1.87%、纳指跌1.98%，费城半导体指数跌3.57%；A股创业板跌1.13%，半导体材料板块逆势上涨；布伦特原油涨超2%站上93美元'
    html = safe_replace(html, old_news_reaction, new_news_reaction, "消息面-市场反应")
    
    # 7. 更新事件日历监控 - 即将到来
    old_event_upcoming = r'6月12日美加墨世界杯开幕、6月16-17日美联储FOMC会议、6月17日沃什首场发布会'
    new_event_upcoming = '6月12日SpaceX上市、6月18日美联储议息会议、*ST建艺摘帽结果待公布'
    html = safe_replace(html, old_event_upcoming, new_event_upcoming, "事件日历-即将到来")
    
    # 更新事件日历-风险提示
    old_event_warning = r'警惕美联储议息会议释放鹰派信号，CPI超预期强化加息预期，中东局势持续紧张'
    new_event_warning = 'SpaceX IPO虹吸全球资本流动性，美联储政策不确定性，中东局势持续紧张升级'
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
    old_time_pattern = r'数据更新时间：\d+年\d+月\d+日 \d+:\d+'
    new_time_text = f'数据更新时间：{update_time}'
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
    old_time_pattern = r'数据更新时间：\d+年\d+月\d+日 \d+:\d+'
    new_time_text = f'数据更新时间：{update_time}'
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
