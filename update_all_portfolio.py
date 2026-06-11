#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
统一数据层更新脚本
一个数据源，同步更新所有页面
涵盖：持仓、智能选题、产业链时钟、预判验证
"""

import json
import os
import re
import shutil
from datetime import datetime

# ========== 通用工具函数 ==========

def backup_file(path):
    """备份文件"""
    backup_path = path + f'.bak.{datetime.now().strftime("%Y%m%d_%H%M%S")}'
    shutil.copy2(path, backup_path)
    return backup_path


# ========== 持仓数据模块 ==========

def load_portfolio_data():
    """加载统一持仓数据"""
    with open('data/portfolio.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def update_index_page(data):
    """更新首页持仓概览"""
    print("🔄 更新首页持仓概览...")
    
    html_path = 'docs/index.html'
    backup_file(html_path)
    
    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    stocks = data['stocks']
    
    for stock in stocks:
        name = stock['name']
        cost = float(stock['cost_price'])
        current = float(stock['current_price'])
        
        pattern = re.compile(
            rf'({re.escape(name)}.*?成本)([0-9.]+)(\s*→\s*现价)([0-9.]+)',
            re.DOTALL
        )
        if pattern.search(html):
            html = pattern.sub(
                lambda m: f'{m.group(1)}{cost:.2f}{m.group(3)}{current:.2f}',
                html
            )
            
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
    """更新持仓智能预警仪表盘"""
    print("🔄 更新持仓智能预警仪表盘...")
    os.system('python3 v3/generators/update_portfolio_v3.py')
    print("  ✅ 持仓智能预警仪表盘更新完成")

def update_warning_system(data):
    """更新智能预警系统页面"""
    print("🔄 更新智能预警系统...")
    
    html_path = 'docs/智能预警系统/index.html'
    backup_file(html_path)
    
    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    stocks = data['stocks']
    
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
    
    pattern = re.compile(r'(风险事件：<b>)([^<]+)(</span>)')
    html = pattern.sub(lambda m: f'{m.group(1)}{risk_events_str}{m.group(3)}', html)
    
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
    
    pattern = re.compile(r'(当前状态：<b>)([^<]+)(</span>)')
    html = pattern.sub(lambda m: f'{m.group(1)}{status_str}{m.group(3)}', html)
    
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print("  ✅ 智能预警系统更新完成")

def archive_portfolio_snapshot(data):
    """归档当日持仓快照（时光机功能）"""
    today = datetime.now().strftime('%Y-%m-%d')
    history_dir = 'data/history'
    os.makedirs(history_dir, exist_ok=True)
    
    archive_path = f'{history_dir}/{today}.json'
    with open(archive_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"  ✅ 持仓数据已归档到 {archive_path}")


# ========== 智能选题助手模块 ==========

def load_topics_data():
    """加载智能选题助手数据"""
    with open('data/topics.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def update_topics_page(data):
    """更新智能选题助手页面 - 精确数据点替换"""
    print("🔄 更新智能选题助手...")
    
    html_path = 'docs/智能选题助手/index.html'
    backup_file(html_path)
    
    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    s_topics = data.get('s_level_topics', [])
    a_topics = data.get('a_level_topics', [])
    b_topics = data.get('b_level_topics', [])
    update_time = data.get('system_info', {}).get('update_time', datetime.now().strftime('%Y年%-m月%-d日 %H:%M'))
    
    # 更新顶部统计数字（数字在上，文字在下）
    html = re.sub(
        r'(text-3xl font-black text-red-600">)(\d+)(</div>\s*<div class="text-sm text-gray-500">S级题材)',
        lambda m: f'{m.group(1)}{len(s_topics)}{m.group(3)}', html
    )
    html = re.sub(
        r'(text-3xl font-black text-yellow-600">)(\d+)(</div>\s*<div class="text-sm text-gray-500">A级题材)',
        lambda m: f'{m.group(1)}{len(a_topics)}{m.group(3)}', html
    )
    html = re.sub(
        r'(text-3xl font-black text-blue-600">)(\d+)(</div>\s*<div class="text-sm text-gray-500">B级题材)',
        lambda m: f'{m.group(1)}{len(b_topics)}{m.group(3)}', html
    )
    # 监控题材总数
    html = re.sub(
        r'(text-3xl font-black text-green-600">)(\d+)(</div>\s*<div class="text-sm text-gray-500">监控题材)',
        lambda m: f'{m.group(1)}{len(s_topics)+len(a_topics)+len(b_topics)}{m.group(3)}', html
    )
    
    # 更新区域数量标签
    html = re.sub(
        r'(S级核心题材\s*<span class="bg-red-100 text-red-700 text-xs px-2 py-0\.5 rounded-full font-bold ml-2">)(\d+)(个</span>)',
        lambda m: f'{m.group(1)}{len(s_topics)}{m.group(3)}', html
    )
    html = re.sub(
        r'(A级重点题材\s*<span class="bg-yellow-100 text-yellow-700 text-xs px-2 py-0\.5 rounded-full font-bold ml-2">)(\d+)(个</span>)',
        lambda m: f'{m.group(1)}{len(a_topics)}{m.group(3)}', html
    )
    
    # 更新每个S级题材的综合评分（按顺序匹配，3个S级评分按顺序对应）
    s_updated = 0
    # 找到所有综合评分的位置
    score_pattern = re.compile(
        r'(综合评分.*?text-4xl font-black text-[a-z]+-600">)(\d+)(分)',
        re.DOTALL
    )
    scores = [t.get('total_score', 0) for t in s_topics]
    
    # 按顺序替换（假设页面上S级题材顺序与数据中一致）
    def replace_score(match, score_idx=[0]):
        if score_idx[0] < len(scores):
            result = f'{match.group(1)}{scores[score_idx[0]]}{match.group(3)}'
            score_idx[0] += 1
            return result
        return match.group(0)
    
    html = score_pattern.sub(replace_score, html)
    s_updated = min(len(scores), 3)  # 最多3个S级
    
    # 更新时间戳（p标签）
    html = re.sub(
        r'(数据更新时间：)([^<]+)(</p>)',
        lambda m: f'{m.group(1)}{update_time}{m.group(3)}', html
    )
    
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"  ✅ 智能选题助手更新完成（S级：{len(s_topics)}个，已更新评分：{s_updated}个）")


# ========== 产业链时钟模块 ==========

def load_industry_chain_data():
    """加载产业链时钟数据"""
    with open('data/industry_chain.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def update_industry_chain_page(data):
    """更新产业链时钟页面 - 精确数据点替换"""
    print("🔄 更新产业链时钟...")
    
    html_path = 'docs/产业链时钟/index.html'
    backup_file(html_path)
    
    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    chains = data.get('core_chains', [])
    update_time = data.get('system_info', {}).get('update_time', datetime.now().strftime('%Y年%-m月%-d日 %H:%M'))
    
    # 更新顶部统计数字
    html = re.sub(
        r'(跟踪产业链\s*</div>\s*<div class="text-3xl font-black text-indigo-600">)(\d+)(</div>)',
        lambda m: f'{m.group(1)}{len(chains)}{m.group(3)}', html
    )
    
    # 更新每个产业链的进度和配置
    updated = 0
    for chain in chains:
        name = chain['name']
        progress = chain.get('progress', 50)
        allocation = chain.get('allocation_ratio', '15%')
        
        # 更新进度条宽度
        pattern = re.compile(
            rf'({re.escape(name)}.*?width: )(\d+)(%)',
            re.DOTALL
        )
        if pattern.search(html):
            html = pattern.sub(lambda m: f'{m.group(1)}{progress}{m.group(3)}', html)
        
        # 更新配置比例
        alloc_pattern = re.compile(
            rf'({re.escape(name)}.*?建议配置.*?text-2xl font-black text-[a-z]+-600">)([^<]+)(</div>)',
            re.DOTALL
        )
        if alloc_pattern.search(html):
            html = alloc_pattern.sub(lambda m: f'{m.group(1)}{allocation}{m.group(3)}', html)
            updated += 1
    
    # 更新时间戳
    html = re.sub(
        r'(数据更新时间：)([^<]+)(</div>)',
        lambda m: f'{m.group(1)}{update_time}{m.group(3)}', html
    )
    
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"  ✅ 产业链时钟更新完成（共{len(chains)}个，已更新{updated}个）")


# ========== 预判验证模块 ==========

def load_predictions_data():
    """加载预判验证数据"""
    with open('data/predictions.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def update_predictions_page(data):
    """更新预判验证页面 - 精确数据点替换"""
    print("🔄 更新预判验证系统...")
    
    html_path = 'docs/预判验证/index.html'
    backup_file(html_path)
    
    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    system_info = data.get('system_info', {})
    pending = data.get('pending_predictions', [])
    history = data.get('history_records', [])
    accuracy = system_info.get('accuracy', '70%')
    analyst_level = system_info.get('analyst_level', 'A')
    update_time = system_info.get('update_time', datetime.now().strftime('%Y年%-m月%-d日 %H:%M'))
    
    level_names = {'S': 'S级分析师', 'A': 'A级分析师', 'B': 'B级分析师', 'C': 'C级分析师'}
    level_name = level_names.get(analyst_level, 'A级分析师')
    
    # 更新统计数字
    html = re.sub(
        r'(综合准确率\s*</div>\s*<div class="text-4xl font-black text-green-600">)(\d+\.?\d*)(%</div>)',
        lambda m: f'{m.group(1)}{str(accuracy).rstrip("%")}{m.group(3)}', html
    )
    html = re.sub(
        r'(待验证\s*</div>\s*<div class="text-2xl font-black text-yellow-600">)(\d+)(</div>)',
        lambda m: f'{m.group(1)}{len(pending)}{m.group(3)}', html
    )
    html = re.sub(
        r'(历史记录\s*</div>\s*<div class="text-2xl font-black text-gray-600">)(\d+)(</div>)',
        lambda m: f'{m.group(1)}{len(history)}{m.group(3)}', html
    )
    
    # 更新分析师等级
    html = re.sub(
        r'(当前等级\s*</div>\s*<div class="text-xl font-black text-purple-600">)([^<]+)(</div>)',
        lambda m: f'{m.group(1)}{level_name}{m.group(3)}', html
    )
    
    # 更新每个待验证预判的状态
    updated = 0
    for pred in pending:
        title = pred['title']
        status = pred.get('status', 'pending')
        
        if status == 'verified':
            badge_text = '已验证'
            badge_class = 'bg-green-100 text-green-700'
        elif status == 'wrong':
            badge_text = '已失败'
            badge_class = 'bg-red-100 text-red-700'
        else:
            badge_text = '待验证'
            badge_class = 'bg-yellow-100 text-yellow-700'
        
        badge_pattern = re.compile(
            rf'({re.escape(title)}.*?<span class=")bg-[a-z]+-100 text-[a-z]+-700( px-2 py-1 rounded-full text-xs font-bold">)([^<]+)(</span>)',
            re.DOTALL
        )
        if badge_pattern.search(html):
            html = badge_pattern.sub(
                lambda m: f'{m.group(1)}{badge_class}{m.group(2)}{badge_text}{m.group(4)}', 
                html
            )
            updated += 1
    
    # 更新时间戳
    html = re.sub(
        r'(数据更新时间：)([^<]+)(</div>)',
        lambda m: f'{m.group(1)}{update_time}{m.group(3)}', html
    )
    
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"  ✅ 预判验证系统更新完成（待验证：{len(pending)}个，历史：{len(history)}个，状态更新：{updated}个）")


# ========== 主函数 ==========

def main():
    print("=" * 60)
    print("📊 统一数据层更新系统 V2.0")
    print("=" * 60)
    
    # ========== 持仓模块 ==========
    print("\n📁 [持仓模块]")
    portfolio_data = load_portfolio_data()
    print(f"   数据源：data/portfolio.json")
    print(f"   持仓股票：{len(portfolio_data['stocks'])}只")
    
    update_dashboard(portfolio_data)
    update_index_page(portfolio_data)
    update_warning_system(portfolio_data)
    archive_portfolio_snapshot(portfolio_data)
    
    # ========== 智能选题模块 ==========
    print("\n📁 [智能选题模块]")
    topics_data = load_topics_data()
    print(f"   数据源：data/topics.json")
    update_topics_page(topics_data)
    
    # ========== 产业链时钟模块 ==========
    print("\n📁 [产业链时钟模块]")
    industry_data = load_industry_chain_data()
    print(f"   数据源：data/industry_chain.json")
    update_industry_chain_page(industry_data)
    
    # ========== 预判验证模块 ==========
    print("\n📁 [预判验证模块]")
    predictions_data = load_predictions_data()
    print(f"   数据源：data/predictions.json")
    update_predictions_page(predictions_data)
    
    print("\n" + "=" * 60)
    print("✅ 所有页面数据更新完成！")
    print("=" * 60)

if __name__ == '__main__':
    main()
