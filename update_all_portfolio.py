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



def extract_card_html(html, topic_id):
    """根据data-topic-id提取单个题材卡片的HTML，返回起止位置和卡片内容"""
    start_pattern = re.compile(r'<div data-topic-id="' + re.escape(topic_id) + r'"[^>]*>')
    match = start_pattern.search(html)
    if not match:
        return None, None, None
    
    start_pos = match.start()
    # 从start_pos开始找匹配的闭合div
    depth = 1
    pos = match.end()
    while depth > 0 and pos < len(html):
        if html[pos:pos+4] == '<div':
            depth += 1
            pos += 4
        elif html[pos:pos+6] == '</div>':
            depth -= 1
            pos += 6
        elif html[pos:pos+5] == '</div':
            # 可能遇到</div后面还有>的情况，兼容处理
            depth -= 1
            pos += 5
            if pos < len(html) and html[pos] == '>':
                pos += 1
        else:
            pos += 1
    
    if depth == 0:
        card_html = html[start_pos:pos]
        return start_pos, pos, card_html
    return None, None, None


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
    """更新智能选题助手页面 - 按data-topic-id精准更新全字段"""
    print("🔄 更新智能选题助手...")
    
    html_path = 'docs/智能选题助手/index.html'
    backup_file(html_path)
    
    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    s_topics = data.get('s_level_topics', [])
    a_topics = data.get('a_level_topics', [])
    b_topics = data.get('b_level_topics', [])
    update_time = data.get('system_info', {}).get('update_time', datetime.now().strftime('%Y年%-m月%-d日 %H:%M'))
    
    # ===== 1. 更新顶部统计数字 =====
    # S级题材数量
    html = re.sub(
        r'(text-3xl font-black text-red-600">)(\d+)(</div>\s*<div class="text-sm text-gray-500">S级题材)',
        lambda m: f'{m.group(1)}{len(s_topics)}{m.group(3)}', html
    )
    # A级题材数量
    html = re.sub(
        r'(text-3xl font-black text-yellow-600">)(\d+)(</div>\s*<div class="text-sm text-gray-500">A级题材)',
        lambda m: f'{m.group(1)}{len(a_topics)}{m.group(3)}', html
    )
    # B级题材数量
    html = re.sub(
        r'(text-3xl font-black text-blue-600">)(\d+)(</div>\s*<div class="text-sm text-gray-500">B级题材)',
        lambda m: f'{m.group(1)}{len(b_topics)}{m.group(3)}', html
    )
    # 监控题材总数
    html = re.sub(
        r'(text-3xl font-black text-green-600">)(\d+)(</div>\s*<div class="text-sm text-gray-500">监控题材)',
        lambda m: f'{m.group(1)}{len(s_topics)+len(a_topics)+len(b_topics)}{m.group(3)}', html
    )
    
    # ===== 2. 更新区域数量标签 =====
    html = re.sub(
        r'(S级核心题材\s*<span class="bg-red-100 text-red-700 text-xs px-2 py-0\.5 rounded-full font-bold ml-2">)(\d+)(个</span>)',
        lambda m: f'{m.group(1)}{len(s_topics)}{m.group(3)}', html
    )
    html = re.sub(
        r'(A级重点题材\s*<span class="bg-yellow-100 text-yellow-700 text-xs px-2 py-0\.5 rounded-full font-bold ml-2">)(\d+)(个</span>)',
        lambda m: f'{m.group(1)}{len(a_topics)}{m.group(3)}', html
    )
    
    # ===== 3. 逐卡更新S级题材 =====
    s_updated = 0
    for topic in s_topics:
        tid = topic.get('id', '')
        if not tid:
            continue
        start, end, card_html = extract_card_html(html, tid)
        if not card_html:
            continue
        
        # 更新标题
        card_html = re.sub(
            r'(<h3 class="text-xl font-black text-gray-800">)[^<]+(</h3>)',
            lambda m: f'{m.group(1)}{topic.get("name", "")}{m.group(2)}',
            card_html
        )
        
        # 更新副标题
        card_html = re.sub(
            r'(<p class="text-gray-500 text-sm mt-1">)[^<]+(</p>)',
            lambda m: f'{m.group(1)}{topic.get("core_logic", "")}{m.group(2)}',
            card_html
        )
        
        # 更新综合评分
        total_score = topic.get('total_score', 0)
        card_html = re.sub(
            r'(text-4xl font-black text-[a-z]+-600">)(\d+)(分</div>)',
            lambda m: f'{m.group(1)}{total_score}{m.group(3)}',
            card_html
        )
        
        # 更新三维度评分和进度条
        dim_scores = topic.get('dimension_scores', {})
        policy_score = dim_scores.get('policy', 0)
        industry_score = dim_scores.get('industry', 0)
        capital_score = dim_scores.get('capital', 0)
        
        # 政策强度
        dim_pattern = re.compile(
            r'(政策强度</span>\s*<span class="font-bold text-[a-z]+-600">)(\d+)(分</span>.*?style="width: )(\d+)(%;")',
            re.DOTALL
        )
        card_html = dim_pattern.sub(
            lambda m: f'{m.group(1)}{policy_score}{m.group(3)}{policy_score}{m.group(5)}',
            card_html
        )
        
        # 产业逻辑
        dim_pattern2 = re.compile(
            r'(产业逻辑</span>\s*<span class="font-bold text-[a-z]+-600">)(\d+)(分</span>.*?style="width: )(\d+)(%;")',
            re.DOTALL
        )
        card_html = dim_pattern2.sub(
            lambda m: f'{m.group(1)}{industry_score}{m.group(3)}{industry_score}{m.group(5)}',
            card_html
        )
        
        # 资金关注
        dim_pattern3 = re.compile(
            r'(资金关注</span>\s*<span class="font-bold text-[a-z]+-600">)(\d+)(分</span>.*?style="width: )(\d+)(%;")',
            re.DOTALL
        )
        card_html = dim_pattern3.sub(
            lambda m: f'{m.group(1)}{capital_score}{m.group(3)}{capital_score}{m.group(5)}',
            card_html
        )
        
        # 更新近期催化
        recent_catalyst = topic.get('recent_catalyst', '')
        if recent_catalyst:
            catalyst_pattern = re.compile(
                r'(<strong>)(今日催化|近期催化)(：</strong>\s*)[^<]+(</span>)',
                re.DOTALL
            )
            card_html = catalyst_pattern.sub(
                lambda m: f'{m.group(1)}{m.group(2)}{m.group(3)}{recent_catalyst}{m.group(4)}',
                card_html
            )
        
        # 替换回原HTML
        html = html[:start] + card_html + html[end:]
        s_updated += 1
    
    # ===== 4. 逐卡更新A级题材 =====
    a_updated = 0
    for topic in a_topics:
        tid = topic.get('id', '')
        if not tid:
            continue
        start, end, card_html = extract_card_html(html, tid)
        if not card_html:
            continue
        
        # 更新标题
        card_html = re.sub(
            r'(<h3 class="font-bold text-gray-800">)[^<]+(</h3>)',
            lambda m: f'{m.group(1)}{topic.get("name", "")}{m.group(2)}',
            card_html
        )
        
        # 更新副标题
        card_html = re.sub(
            r'(<p class="text-xs text-gray-500">)[^<]+(</p>)',
            lambda m: f'{m.group(1)}{topic.get("subtitle", "")}{m.group(2)}',
            card_html
        )
        
        # 更新综合评分
        total_score = topic.get('total_score', 0)
        card_html = re.sub(
            r'(<span class="text-2xl font-black text-yellow-600">)(\d+)(分</span>)',
            lambda m: f'{m.group(1)}{total_score}{m.group(3)}',
            card_html
        )
        
        # 更新标的标签
        tags = topic.get('tags', [])
        if tags:
            tags_pattern = re.compile(
                r'(<div class="flex gap-2">)(.*?)(</div>)',
                re.DOTALL
            )
            tags_html = '\n'
            for tag in tags:
                tags_html += f'                            <span class="bg-yellow-100 text-yellow-700 px-2 py-0.5 rounded-full text-xs">{tag}</span>\n'
            tags_html += '                        '
            card_html = tags_pattern.sub(
                lambda m: f'{m.group(1)}{tags_html}{m.group(3)}',
                card_html,
                count=1
            )
        
        # 替换回原HTML
        html = html[:start] + card_html + html[end:]
        a_updated += 1
    
    # ===== 5. 更新时间戳 =====
    html = re.sub(
        r'(数据更新时间：)([^<]+)(</p>)',
        lambda m: f'{m.group(1)}{update_time}{m.group(3)}',
        html
    )
    
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"  ✅ 智能选题助手更新完成（S级：{s_updated}个，A级：{a_updated}个）")




# ========== 产业链时钟模块 ==========

def load_industry_chain_data():
    """加载产业链时钟数据"""
    with open('data/industry_chain.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def update_industry_chain_page(data):
    """更新产业链时钟页面 - 按data-chain-id精准更新"""
    print("🔄 更新产业链时钟...")
    
    html_path = 'docs/产业链时钟/index.html'
    backup_file(html_path)
    
    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    chains = data.get('core_chains', [])
    update_time = data.get('system_info', {}).get('update_time', datetime.now().strftime('%Y年%-m月%-d日 %H:%M'))
    
    updated = 0
    for chain in chains:
        cid = chain.get('id', '')
        if not cid:
            continue
        
        # 按data-chain-id提取卡片
        start, end, card_html = extract_chain_card(html, cid)
        if not card_html:
            continue
        
        # 1. 更新阶段名称
        stage_name = chain.get('stage_name', '')
        if stage_name:
            card_html = re.sub(
                r'(<span class="phase-\d+ text-white px-4 py-2 rounded-full text-sm font-bold">)[^<]+(</span>)',
                lambda m: f'{m.group(1)}{stage_name}{m.group(2)}',
                card_html
            )
        
        # 2. 更新周期位置文字和进度条位置
        progress = chain.get('progress', 0)
        stage = chain.get('stage', 1)
        # 更新文字：周期位置：2/4 → 25%
        pos_pattern = re.compile(r'(周期位置：)(\d+)(/4 → )(\d+)(%)')
        card_html = pos_pattern.sub(
            lambda m: f'{m.group(1)}{stage}{m.group(3)}{progress}{m.group(5)}',
            card_html
        )
        
        # 更新进度条指示器位置
        card_html = re.sub(
            r'(<div class="absolute -top-3" style="left: )(\d+)(%;")',
            lambda m: f'{m.group(1)}{progress}{m.group(3)}',
            card_html
        )
        
        # 3. 更新配置策略中的建议仓位
        allocation = str(chain.get('allocation_ratio', '0%')).rstrip('%')
        card_html = re.sub(
            r'(建议仓位：)(\d+)(%)',
            lambda m: f'{m.group(1)}{allocation}{m.group(3)}',
            card_html
        )
        
        # 替换回原HTML
        html = html[:start] + card_html + html[end:]
        updated += 1
    
    # 更新配置策略汇总区的比例
    for chain in chains:
        name = chain.get('name', '')
        allocation = str(chain.get('allocation_ratio', '0%')).rstrip('%')
        if name and allocation:
            alloc_pattern = re.compile(
                r'(<strong>' + re.escape(name) + r'</strong>（)(\d+)(%）)',
            )
            html = alloc_pattern.sub(
                lambda m: f'{m.group(1)}{allocation}{m.group(3)}', 
                html
            )
    
    # 更新时间戳
    html = re.sub(
        r'(数据更新时间：)([^<]+)(</p>)',
        lambda m: f'{m.group(1)}{update_time}{m.group(3)}',
        html
    )
    
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"  ✅ 产业链时钟更新完成（共{len(chains)}个，已更新：{updated}个）")


def extract_chain_card(html, chain_id):
    """根据data-chain-id提取单个产业链卡片的HTML，返回起止位置和卡片内容"""
    start_pattern = re.compile(r'<div data-chain-id="' + re.escape(chain_id) + r'"[^>]*>')
    match = start_pattern.search(html)
    if not match:
        return None, None, None
    
    start_pos = match.start()
    depth = 1
    pos = match.end()
    while depth > 0 and pos < len(html):
        if html[pos:pos+4] == '<div':
            depth += 1
            pos += 4
        elif html[pos:pos+6] == '</div>':
            depth -= 1
            pos += 6
        elif html[pos:pos+5] == '</div':
            depth -= 1
            pos += 5
            if pos < len(html) and html[pos] == '>':
                pos += 1
        else:
            pos += 1
    
    if depth == 0:
        card_html = html[start_pos:pos]
        return start_pos, pos, card_html
    return None, None, None



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
    accuracy = system_info.get('accuracy', '72.7%')
    analyst_level = system_info.get('analyst_level', 'A')
    total_pred = system_info.get('total_predictions', len(pending) + len(history))
    correct_count = system_info.get('correct_count', 0)
    wrong_count = system_info.get('wrong_count', 0)
    
    level_names = {'S': 'S级', 'A': 'A级', 'B': 'B级', 'C': 'C级'}
    level_name = level_names.get(analyst_level, 'A级')
    
    # 更新综合准确率（百分比数字）
    acc_num = str(accuracy).rstrip('%')
    html = re.sub(
        r'(text-3xl font-black text-green-600">)(\d+\.?\d*)(%</div>)',
        lambda m: f'{m.group(1)}{acc_num}{m.group(3)}', html
    )
    
    # 更新环形进度条
    html = re.sub(
        r'(accuracy-ring.*?style="--p: )(\d+)(%)',
        lambda m: f'{m.group(1)}{int(float(acc_num))}{m.group(3)}', html
    )
    
    # 更新分析师等级
    html = re.sub(
        r'(text-4xl font-black text-purple-600">)([A-Z]级)(</div>)',
        lambda m: f'{m.group(1)}{level_name}{m.group(3)}', html
    )
    
    # 更新统计卡片：通过下方标签定位上方数字
    stats_map = {
        '累计预判': str(total_pred),
        '验证正确': str(correct_count),
        '验证错误': str(wrong_count),
        '待验证': str(len(pending)),
    }
    
    for label, value in stats_map.items():
        pattern = re.compile(
            rf'(text-3xl font-black text-[^"]+">)(\d+)(</div>\s*<div class="text-sm text-gray-500">{label})',
            re.DOTALL
        )
        html = pattern.sub(lambda m: f'{m.group(1)}{value}{m.group(3)}', html)
    
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"  ✅ 预判验证系统更新完成（累计：{total_pred}，正确：{correct_count}，错误：{wrong_count}，待验证：{len(pending)}）")


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
