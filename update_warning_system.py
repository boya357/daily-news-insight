#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
智能预警系统每日更新脚本
"""

import re
from datetime import datetime

def update_warning_system():
    html_path = "docs/智能预警系统/index.html"
    
    # 读取文件
    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 备份原文件
    backup_path = html_path + ".bak." + datetime.now().strftime("%Y%m%d_%H%M%S")
    with open(backup_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"✅ 已备份原文件到 {backup_path}")
    
    # ========== 风险指数更新 ==========
    # 从75下调到65（科技股反弹，市场情绪修复）
    content = content.replace(
        '<div class="text-2xl font-black text-red-600">75</div>',
        '<div class="text-2xl font-black text-yellow-600">65</div>'
    )
    
    # 风险等级标签更新
    old_risk_label = """<div class="inline-flex items-center gap-2 px-4 py-2 bg-red-100 text-red-700 rounded-full font-bold">
                            <span class="w-3 h-3 bg-red-500 rounded-full pulse-dot"></span>
                            高风险 · 严控仓位
                        </div>"""
    new_risk_label = """<div class="inline-flex items-center gap-2 px-4 py-2 bg-yellow-100 text-yellow-700 rounded-full font-bold">
                            <span class="w-3 h-3 bg-yellow-500 rounded-full pulse-dot"></span>
                            中高风险 · 谨慎参与
                        </div>"""
    content = content.replace(old_risk_label, new_risk_label)
    
    # 建议仓位更新
    content = content.replace(
        '<div class="text-sm text-gray-500 mt-2">建议仓位：20-30%</div>',
        '<div class="text-sm text-gray-500 mt-2">建议仓位：30-50%</div>'
    )
    
    # ========== 大盘风险监控更新 ==========
    # 评分从85下调到70
    content = content.replace(
        '<div class="text-2xl font-black text-red-600">85</div>\n                            <div class="text-xs text-red-500">高风险</div>',
        '<div class="text-2xl font-black text-yellow-600">70</div>\n                            <div class="text-xs text-yellow-500">中高风险</div>',
        1  # 只替换第一个（大盘风险）
    )
    
    # 更新大盘风险当前状态
    old_market_status = '6月8日A股大幅调整，沪指失守4000点收跌1.70%，创业板指暴跌3.69%，科创50重挫4.3%。全市场超4500只个股下跌，仅银行、煤炭等防御板块逆势上涨。科技板块集体重挫，半导体、AI算力、存储器板块领跌。成交额2.82万亿，较前一交易日缩量'
    new_market_status = '6月9日A股探底回升，科技成长领涨。创业板指涨超1.5%，科创50涨超2.5%。AI算力、存储芯片、液冷散热板块强势反弹，英维克涨停、铜冠铜箔创历史新高。市场情绪有所修复，但量能略有萎缩，仍需警惕二次探底风险'
    content = content.replace(old_market_status, new_market_status)
    
    # ========== 资金流向监控更新 ==========
    # 评分从82下调到75
    content = content.replace(
        '<div class="text-2xl font-black text-red-600">82</div>\n                            <div class="text-xs text-red-600">高风险</div>',
        '<div class="text-2xl font-black text-yellow-600">75</div>\n                            <div class="text-xs text-yellow-600">中高风险</div>',
        1
    )
    
    # 更新资金流向状态
    old_money_status = 'A股主力资金大幅流出，半导体板块净流出超200亿，北向资金净卖出。避险情绪升温，资金向银行、煤炭等低位防御板块切换，市场呈现典型的"高切低"格局'
    new_money_status = 'A股主力资金小幅净流入，科技板块获资金回流，半导体、AI算力板块主力净流入超80亿。北向资金小幅净买入，市场情绪有所修复，但资金分歧仍存，防御板块仍有资金布局'
    content = content.replace(old_money_status, new_money_status)
    
    # ========== 持仓风险监控更新 ==========
    # 评分从85下调到70
    content = content.replace(
        '<div class="text-2xl font-black text-red-600">85</div>\n                            <div class="text-xs text-red-600">高危</div>',
        '<div class="text-2xl font-black text-yellow-600">70</div>\n                            <div class="text-xs text-yellow-600">中高风险</div>',
        1
    )
    
    # 更新持仓风险事件描述
    old_position_risk = '英维克严重破止损（浮亏-35%）、科技板块分化、*ST建艺摘帽窗口期'
    new_position_risk = '英维克反弹但仍破止损（浮亏-29%）、铜冠铜箔创新高止盈压力、*ST建艺摘帽窗口期'
    content = content.replace(old_position_risk, new_position_risk)
    
    # 更新持仓当前状态
    old_position_status = '英维克63.38元 vs 止损98元，浮亏-35.35%，严重破止损需严格执行纪律；铜冠铜箔113.10元（+1.65%），HVLP铜箔国产替代逻辑坚挺；*ST建艺13.02元，摘帽窗口期临近'
    new_position_status = '英维克69.72元（+10%涨停）vs 止损98元，浮亏-28.86%，反弹后亏损收窄但仍破止损；铜冠铜箔122.76元（+8.54%）创历史新高，储能+AI服务器铜箔需求爆发；*ST建艺13.33元（+2.38%），摘帽审核进行中'
    content = content.replace(old_position_status, new_position_status)
    
    # ========== 数据更新时间 ==========
    content = re.sub(
        r'数据更新时间：2026年\d+月\d+日 \d+:\d+',
        '数据更新时间：2026年6月9日 21:30',
        content
    )
    
    # 保存更新后的文件
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✅ 智能预警系统更新完成")
    print("   - 综合风险指数：75 → 65")
    print("   - 大盘风险：85 → 70（高风险→中高风险）")
    print("   - 资金流向：82 → 75（高风险→中高风险）")
    print("   - 持仓风险：85 → 70（高危→中高风险）")
    print("   - 建议仓位：20-30% → 30-50%")
    
    return True

if __name__ == "__main__":
    update_warning_system()
