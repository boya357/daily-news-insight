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

def backup_file(path, keep_count=10):
    """备份文件，自动清理旧备份（默认保留最近10个"""
    import os
    import glob
    
    # 创建新备份
    backup_path = path + f'.bak.{datetime.now().strftime("%Y%m%d_%H%M%S")}'
    shutil.copy2(path, backup_path)
    
    # 清理旧备份 - 只保留最近N个
    backup_pattern = path + '.bak.*'
    backups = sorted(glob.glob(backup_pattern), reverse=True)
    if len(backups) > keep_count:
        for old_backup in backups[keep_count:]:
            try:
                os.remove(old_backup)
            except:
                pass
    
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



def generate_s_chain_card_html(topic):
    """生成S级产业链卡片HTML"""
    icon = topic.get('icon', '📊')
    name = topic.get('name', '')
    description = topic.get('description', '')
    link = topic.get('link', '#')
    level = topic.get('level', 'S')
    
    html_parts = []
    html_parts.append('                    <a href="' + link + '" class="chain-card block p-5 bg-white border border-gray-100 rounded-2xl text-center hover:shadow-lg transition-all duration-300 hover:-translate-y-1">')
    html_parts.append('                        <div class="text-4xl mb-3">' + icon + '</div>')
    html_parts.append('                        <div class="font-bold text-gray-800 mb-2">' + name + '</div>')
    html_parts.append('                        <div class="flex justify-center gap-2 mb-2">')
    html_parts.append('                            <span class="text-xs text-white px-2 py-1 rounded-full tag-' + level + '">' + level + '级</span>')
    html_parts.append('                        </div>')
    html_parts.append('                        <p class="text-xs text-gray-500">' + description + '</p>')
    html_parts.append('                    </a>')
    return '\n'.join(html_parts)


def generate_catalyst_item_html(catalyst):
    """生成催化项HTML"""
    date_str = catalyst.get('date', '')
    # 将 2026-06-01 转为 6月1日 格式
    if date_str and '-' in date_str:
        parts = date_str.split('-')
        if len(parts) == 3:
            date_str = str(int(parts[1])) + '月' + str(int(parts[2])) + '日'
    
    title = catalyst.get('title', '')
    description = catalyst.get('description', '')
    status_label = catalyst.get('status_label', '')
    status_class = catalyst.get('status_class', 'bg-gray-100 text-gray-600')
    link = catalyst.get('link', '#')
    
    html_parts = []
    html_parts.append('                    <a href="' + link + '" class="block p-3 bg-white border border-gray-100 rounded-xl hover:bg-gray-50 transition-colors">')
    html_parts.append('                        <div class="flex items-center justify-between mb-1">')
    html_parts.append('                            <div class="flex items-center gap-2">')
    html_parts.append('                                <span class="text-gray-600 font-bold text-xs">' + date_str + '</span>')
    html_parts.append('                                <span class="text-sm font-semibold text-gray-800">' + title + '</span>')
    html_parts.append('                            </div>')
    html_parts.append('                            <span class="text-xs ' + status_class + ' px-2 py-1 rounded-full">' + status_label + '</span>')
    html_parts.append('                        </div>')
    html_parts.append('                        <p class="text-xs text-gray-500">' + description + '</p>')
    html_parts.append('                    </a>')
    return '\n'.join(html_parts)


def update_index_s_level_chains(html, topics):
    """更新首页S级产业链卡片"""
    # 找到S级产业链标题后的grid容器
    pattern = re.compile(
        r'(核心S级产业链.*?<div class="grid grid-cols-3 gap-4">).*?(</div>\s*</div>\s*<!-- 右侧：持仓概览)',
        re.DOTALL
    )
    
    if not pattern.search(html):
        print("  ⚠️ 未找到S级产业链网格位置，跳过更新")
        return html
    
    # 生成新的卡片HTML
    cards_html = '\n'.join([generate_s_chain_card_html(t) for t in topics])
    
    # 替换
    def replacer(m):
        return m.group(1) + '\n' + cards_html + '\n                ' + m.group(2)
    
    html = pattern.sub(replacer, html)
    print(f"  ✅ S级产业链卡片已更新（{len(topics)}个）")
    return html


def update_index_catalysts(html, catalysts):
    """更新首页近期催化列表"""
    # 找到近期重点催化标题后的space-y-3容器
    pattern = re.compile(
        r'(近期重点催化.*?<div class="space-y-3">).*?(</div>\s*</div>\s*<!-- 右侧：今日报告)',
        re.DOTALL
    )
    
    if not pattern.search(html):
        print("  ⚠️ 未找到近期催化列表位置，跳过更新")
        return html
    
    # 生成新的催化项HTML
    items_html = '\n'.join([generate_catalyst_item_html(c) for c in catalysts])
    
    # 替换
    def replacer(m):
        return m.group(1) + '\n' + items_html + '\n                ' + m.group(2)
    
    html = pattern.sub(replacer, html)
    print(f"  ✅ 近期催化列表已更新（{len(catalysts)}项）")
    return html




def generate_report_item_html(report):
    """生成单个今日报告项的HTML"""
    report_id = report.get('id', '')
    title = report.get('title', '')
    subtitle = report.get('subtitle', '')
    icon = report.get('icon', '📄')
    color = report.get('color', 'blue')
    url = report.get('url', '#')
    status = report.get('status', '')
    publish_time = report.get('publish_time', '')
    
    color_map = {
        'blue': 'from-blue-500 to-indigo-500',
        'green': 'from-green-500 to-emerald-500',
        'orange': 'from-orange-500 to-amber-500',
        'purple': 'from-purple-500 to-violet-500',
        'red': 'from-red-500 to-rose-500',
        'gray': 'from-gray-500 to-slate-500',
    }
    color_class = color_map.get(color, color_map['blue'])
    
    # 状态标签
    if status == '已发布':
        status_html = '<span class="text-xs text-green-600 font-medium">' + publish_time + ' 已发布</span>'
    elif status == '更新中':
        status_html = '<span class="text-xs text-orange-500 font-medium">更新中</span>'
    elif status == '待发布':
        status_html = '<span class="text-xs text-gray-400 font-medium">' + publish_time + ' 待发布</span>'
    else:
        status_html = ''
    
    item_html = '                    <a href="' + url + '" class="block card-mini p-3 bg-white border border-gray-100 rounded-xl hover:bg-gray-50 transition-colors">\n'
    item_html += '                        <div class="flex items-center gap-3">\n'
    item_html += '                            <div class="w-9 h-9 rounded-lg bg-gradient-to-r ' + color_class + ' flex items-center justify-center text-lg text-white">' + icon + '</div>\n'
    item_html += '                            <div class="flex-1">\n'
    item_html += '                                <div class="font-semibold text-gray-800 text-sm">' + title + '</div>\n'
    item_html += '                                <div class="text-xs text-gray-400">' + subtitle + '</div>\n'
    item_html += '                            </div>\n'
    if status_html:
        item_html += '                            <div class="text-right">\n'
        item_html += '                                ' + status_html + '\n'
        item_html += '                            </div>\n'
    item_html += '                        </div>\n'
    item_html += '                    </a>'
    
    return item_html


def update_index_today_reports(html, reports):
    """更新首页今日报告列表"""
    pattern = re.compile(
        r'(今日报告.*?<div id="todayReports" class="space-y-3">).*?(</div>\s*</div>\s*</div>\s*<!-- 【第四区】)',
        re.DOTALL
    )
    
    if not pattern.search(html):
        print("  ⚠️ 未找到今日报告列表位置，跳过更新")
        return html
    
    items_html = '\n'.join([generate_report_item_html(r) for r in reports])
    
    def replacer(m):
        return m.group(1) + '\n' + items_html + '\n                ' + m.group(2)
    
    html = pattern.sub(replacer, html)
    print(f"  ✅ 今日报告列表已更新（{len(reports)}项）")
    return html


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
        code = stock.get('id', '')
        
        # 方法：先找到股票对应的整个卡片div，然后在其中替换
        # 使用股票代码作为锚点，因为代码是唯一的
        if code:
            # 找到股票代码的位置
            code_pattern = re.compile(r'<span>' + re.escape(code) + r'</span>')
            code_match = code_pattern.search(html)
            if code_match:
                # 向前找最近的 p-3 bg- div
                start_pos = html.rfind('<div class="p-3', 0, code_match.start())
                if start_pos != -1:
                    # 向后找闭合div
                    depth = 1
                    pos = start_pos + 4
                    while depth > 0 and pos < len(html):
                        if html[pos:pos+4] == '<div':
                            depth += 1
                            pos += 4
                        elif html[pos:pos+6] == '</div>':
                            depth -= 1
                            pos += 6
                        else:
                            pos += 1
                    
                    if depth == 0:
                        card_html = html[start_pos:pos]
                        
                        # 在卡片内替换成本和现价
                        cost_pattern = re.compile(r'成本~?([0-9.]+)')
                        current_pattern = re.compile(r'现价([0-9.]+)')
                        
                        # 替换成本
                        new_card = cost_pattern.sub(f'成本{cost:.2f}', card_html, count=1)
                        # 替换现价
                        new_card = current_pattern.sub(f'现价{current:.2f}', new_card, count=1)
                        
                        # 更新状态颜色和标签
                        profit_pct = (current - cost) / cost * 100
                        if profit_pct > 0:
                            status_label = '🟢 持有'
                            status_color = 'text-green-600'
                            bg_color = 'bg-green-50'
                            border_color = 'border-green-100'
                        elif profit_pct > -10:
                            status_label = '🟡 观察'
                            status_color = 'text-yellow-600'
                            bg_color = 'bg-yellow-50'
                            border_color = 'border-yellow-100'
                        else:
                            status_label = '🔴 止损'
                            status_color = 'text-red-500'
                            bg_color = 'bg-red-50'
                            border_color = 'border-red-100'
                        
                        # 替换状态标签
                        status_pattern = re.compile(r'<span class="text-[a-z0-9-]+ font-bold text-sm">[^<]+</span>')
                        new_status = f'<span class="{status_color} font-bold text-sm">{status_label}</span>'
                        new_card = status_pattern.sub(new_status, new_card, count=1)
                        
                        # 替换背景色
                        bg_pattern = re.compile(r'<div class="p-3 bg-[a-z]+-50 border border-[a-z]+-100 rounded-xl">')
                        new_bg = f'<div class="p-3 {bg_color} border {border_color} rounded-xl">'
                        new_card = bg_pattern.sub(new_bg, new_card, count=1)
                        
                        # 替换回整个HTML
                        html = html[:start_pos] + new_card + html[pos:]
    
    # 更新S级产业链
    try:
        from v3.utils.data_loader import get_index_s_level_chains
        s_topics = get_index_s_level_chains()
        html = update_index_s_level_chains(html, s_topics)
    except Exception as e:
        print(f"  ⚠️  S级产业链更新失败: {e}")
    
    # 更新近期催化
    try:
        from v3.utils.data_loader import get_index_catalysts
        catalysts = get_index_catalysts(5)
        html = update_index_catalysts(html, catalysts)
    except Exception as e:
        print(f"  ⚠️  近期催化更新失败: {e}")
    
    # 更新今日报告
    try:
        import json
        with open('data/today_reports.json', 'r', encoding='utf-8') as f2:
            reports_data = json.load(f2)
        reports = reports_data.get('reports', [])
        html = update_index_today_reports(html, reports)
    except Exception as e:
        print(f"  ⚠️  今日报告更新失败: {e}")

    
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print("  ✅ 首页持仓概览更新完成")
def update_dashboard(data):
    """更新持仓智能预警仪表盘"""
    print("🔄 更新持仓智能预警仪表盘...")
    os.system('python3 v3/generators/update_portfolio_v3.py')
    print("  ✅ 持仓智能预警仪表盘更新完成")

def update_warning_system(data):
    """更新智能预警系统页面 - 完整数据驱动版本"""
    print("🔄 更新智能预警系统...")
    
    html_path = 'docs/智能预警系统/index.html'
    backup_file(html_path)
    
    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    stocks = data['stocks']
    
    # ========== 分析持仓，生成三类预警 ==========
    critical_alerts = []   # 紧急预警（红色）
    warning_alerts = []    # 风险提醒（黄色）
    info_alerts = []       # 关注提示（蓝色）
    
    for stock in stocks:
        name = stock['name']
        current = float(stock['current_price'])
        cost = float(stock['cost_price'])
        profit_pct = (current - cost) / cost * 100
        today_change = float(stock.get('today_change', 0)) * 100
        stop_loss = float(stock.get('stop_loss_price', cost * 0.8))
        risk_level = stock.get('risk_level', '')
        stock_tag = stock.get('tag', '')
        
        # 判断距离止损的距离
        distance_to_stop = (current - stop_loss) / stop_loss * 100
        
        # ========== 紧急预警（红色）==========
        # 1. 跌破止损位
        if current <= stop_loss:
            critical_alerts.append({
                'title': name + '跌破止损位',
                'time': '今日收盘',
                'desc': '收盘价%.2f元已跌破止损位%.2f元，浮亏%.2f%%' % (current, stop_loss, profit_pct),
                'tags': ['建议：立即止损出局']
            })
        # 2. 单日跌幅超7%
        elif today_change <= -7:
            critical_alerts.append({
                'title': name + '单日暴跌',
                'time': '今日收盘',
                'desc': '收盘价%.2f元，今日下跌%.2f%%，放量下跌需警惕' % (current, today_change),
                'tags': ['建议：减仓规避风险']
            })
        # 3. 高位大幅回撤（从高点跌超20%）
        elif profit_pct <= -20:
            critical_alerts.append({
                'title': name + '深度套牢',
                'time': '今日收盘',
                'desc': '收盘价%.2f元，浮亏已达%.2f%%，严重套牢' % (current, profit_pct),
                'tags': ['建议：反弹减仓']
            })
        
        # ========== 风险提醒（黄色）==========
        # 1. 接近止损位（距离<10%）
        if 0 < distance_to_stop < 10 and current > stop_loss:
            warning_alerts.append({
                'title': name + '接近止损位',
                'time': '关注',
                'desc': '现价%.2f元，距离止损位%.2f元仅剩%.1f%%空间' % (current, stop_loss, distance_to_stop),
                'tags': []
            })
        # 2. 浮盈过高有回调风险（>40%）
        elif profit_pct > 40:
            warning_alerts.append({
                'title': name + '累计涨幅过大',
                'time': '关注',
                'desc': '现价%.2f元，累计浮盈%.1f%%，有获利回吐压力' % (current, profit_pct),
                'tags': ['建议：逐步减仓锁定利润']
            })
        # 3. 今日大幅波动（涨跌幅>5%）
        if abs(today_change) > 5 and current > stop_loss and profit_pct > -20:
            warning_alerts.append({
                'title': name + '大幅波动',
                'time': '今日',
                'desc': '今日涨跌幅%+.2f%%，波动加剧，注意风险' % today_change,
                'tags': []
            })
        
        # ========== 关注提示（蓝色）==========
        # 1. 创历史新高（或阶段新高）
        if '历史新高' in risk_level or '新高' in stock_tag:
            info_alerts.append({
                'title': name + '创历史新高',
                'time': '今日',
                'desc': '收盘价%.2f元创历史新高，趋势强劲，持有为主' % current,
                'tags': []
            })
        # 2. 有重要事件（如摘帽）
        if '*ST' in name or 'ST' in name:
            info_alerts.append({
                'title': name + '摘帽预期',
                'time': '待批复',
                'desc': '摘帽审核进行中，关注后续进展，当前价%.2f元' % current,
                'tags': []
            })
        # 3. 强势上涨（今日涨幅>3%且趋势向好）
        if today_change > 3 and profit_pct > 0:
            info_alerts.append({
                'title': name + '强势上涨',
                'time': '今日',
                'desc': '今日上涨%+.2f%%，表现强势，关注持续性' % today_change,
                'tags': []
            })
    
    # 如果没有生成任何预警，添加默认提示
    if not critical_alerts:
        critical_alerts.append({
            'title': '无紧急风险',
            'time': '今日',
            'desc': '当前持仓无紧急预警事项，整体风险可控',
            'tags': []
        })
    
    if not warning_alerts:
        warning_alerts.append({
            'title': '暂无重大风险',
            'time': '今日',
            'desc': '持仓整体风险可控，保持关注即可',
            'tags': []
        })
    
    if not info_alerts:
        info_alerts.append({
            'title': '无特别关注',
            'time': '今日',
            'desc': '当前无特别需要关注的事项',
            'tags': []
        })
    
    # ========== 生成预警卡片HTML ==========
    def generate_alert_cards(alerts, alert_type='critical'):
        """生成预警卡片HTML"""
        if alert_type == 'critical':
            bg_class = 'bg-red-50'
            text_class = 'text-red-600'
            tag_bg = 'bg-red-100'
            tag_text = 'text-red-600'
        elif alert_type == 'warning':
            bg_class = 'bg-yellow-50'
            text_class = 'text-yellow-700'
            tag_bg = 'bg-yellow-100'
            tag_text = 'text-yellow-700'
        else:
            bg_class = 'bg-blue-50'
            text_class = 'text-blue-600'
            tag_bg = 'bg-blue-100'
            tag_text = 'text-blue-600'
        
        html_parts = []
        for alert in alerts:
            tags_html = ''
            if alert.get('tags'):
                tags_html = '<div class="flex gap-2 flex-wrap">'
                for tag in alert['tags']:
                    tags_html += '<span class="text-xs %s %s px-2 py-0.5 rounded">%s</span>' % (tag_bg, tag_text, tag)
                tags_html += '</div>'
            
            card_lines = []
            card_lines.append('                    <div class="alert-item alert-%s p-4 %s rounded-xl">' % (alert_type, bg_class))
            card_lines.append('                        <div class="flex items-start justify-between mb-2">')
            card_lines.append('                            <span class="font-bold text-gray-800">%s</span>' % alert['title'])
            card_lines.append('                            <span class="text-xs %s font-semibold">%s</span>' % (text_class, alert['time']))
            card_lines.append('                        </div>')
            card_lines.append('                        <p class="text-sm text-gray-600 mb-2">%s</p>' % alert['desc'])
            if tags_html:
                card_lines.append('                        ' + tags_html)
            card_lines.append('                    </div>')
            html_parts.append('\n'.join(card_lines))
        
        return '\n'.join(html_parts), len(alerts)
    
    # 生成三类预警的HTML
    critical_html, critical_count = generate_alert_cards(critical_alerts, 'critical')
    warning_html, warning_count = generate_alert_cards(warning_alerts, 'warning')
    info_html, info_count = generate_alert_cards(info_alerts, 'info')
    
    # ========== 更新页面内容 ==========
    
    def find_matching_div_end(html, start_pos):
        """从start_pos开始找匹配的闭合div位置"""
        depth = 0
        pos = start_pos
        while pos < len(html):
            if html[pos:pos+4] == '<div':
                depth += 1
                pos += 4
            elif html[pos:pos+6] == '</div>':
                depth -= 1
                pos += 6
                if depth == 0:
                    return pos
            else:
                pos += 1
        return -1
    
    # 1. 更新紧急预警卡片和计数
    crit_marker = '🔴 紧急预警'
    warn_marker = '🟡 风险提醒'
    info_marker = '🔵 关注提示'
    section2_marker = '<!-- 【第三区：操作策略矩阵】'
    
    # 紧急预警
    crit_pos = html.find(crit_marker)
    warn_pos = html.find(warn_marker, crit_pos)
    
    if crit_pos != -1 and warn_pos != -1:
        # 找space-y-3
        sy3_start = html.find('<div class="space-y-3">', crit_pos)
        if sy3_start != -1 and sy3_start < warn_pos:
            sy3_end = find_matching_div_end(html, sy3_start)
            if sy3_end != -1:
                # 替换卡片内容
                new_content = '<div class="space-y-3">\n' + critical_html + '\n                </div>'
                html = html[:sy3_start] + new_content + html[sy3_end:]
                
                # 更新计数
                count_pattern = r'<span class="bg-red-100 text-red-600 text-xs px-2 py-0.5 rounded-full font-bold ml-auto">\d+条</span>'
                new_count = '<span class="bg-red-100 text-red-600 text-xs px-2 py-0.5 rounded-full font-bold ml-auto">%d条</span>' % critical_count
                html = re.sub(count_pattern, new_count, html, count=1)
    
    # 2. 更新风险提醒卡片和计数
    # 重新获取位置（因为HTML变了）
    warn_pos = html.find(warn_marker)
    info_pos = html.find(info_marker, warn_pos)
    
    if warn_pos != -1 and info_pos != -1:
        sy3_start = html.find('<div class="space-y-3">', warn_pos)
        if sy3_start != -1 and sy3_start < info_pos:
            sy3_end = find_matching_div_end(html, sy3_start)
            if sy3_end != -1:
                new_content = '<div class="space-y-3">\n' + warning_html + '\n                </div>'
                html = html[:sy3_start] + new_content + html[sy3_end:]
                
                count_pattern = r'<span class="bg-yellow-100 text-yellow-700 text-xs px-2 py-0.5 rounded-full font-bold ml-auto">\d+条</span>'
                new_count = '<span class="bg-yellow-100 text-yellow-700 text-xs px-2 py-0.5 rounded-full font-bold ml-auto">%d条</span>' % warning_count
                html = re.sub(count_pattern, new_count, html, count=1)
    
    # 3. 更新关注提示卡片和计数
    info_pos = html.find(info_marker)
    section2_pos = html.find(section2_marker, info_pos)
    
    if info_pos != -1 and section2_pos != -1:
        sy3_start = html.find('<div class="space-y-3">', info_pos)
        if sy3_start != -1 and sy3_start < section2_pos:
            sy3_end = find_matching_div_end(html, sy3_start)
            if sy3_end != -1:
                new_content = '<div class="space-y-3">\n' + info_html + '\n                </div>'
                html = html[:sy3_start] + new_content + html[sy3_end:]
                
                count_pattern = r'<span class="bg-blue-100 text-blue-600 text-xs px-2 py-0.5 rounded-full font-bold ml-auto">\d+条</span>'
                new_count = '<span class="bg-blue-100 text-blue-600 text-xs px-2 py-0.5 rounded-full font-bold ml-auto">%d条</span>' % info_count
                html = re.sub(count_pattern, new_count, html, count=1)
    
    # 4. 更新顶部的风险事件和当前状态文本
    risk_events = []
    for stock in stocks:
        name = stock['name']
        current = float(stock['current_price'])
        cost = float(stock['cost_price'])
        profit_pct = (current - cost) / cost * 100
        today_change = float(stock.get('today_change', 0)) * 100
        
        if profit_pct < -20:
            risk_events.append("%s深度套牢（浮亏%.1f%%）" % (name, profit_pct))
        elif profit_pct < -10:
            risk_events.append("%s浮亏扩大（%.1f%%）" % (name, profit_pct))
        elif profit_pct > 30:
            risk_events.append("%s累计涨幅较大（%.1f%%）" % (name, profit_pct))
        elif today_change > 3:
            risk_events.append("%s今日大涨（%+.1f%%）" % (name, today_change))
        elif today_change < -3:
            risk_events.append("%s今日大跌（%+.1f%%）" % (name, today_change))
    
    if not risk_events:
        risk_events.append("持仓整体平稳，无重大风险事件")
    
    risk_events_str = "、".join(risk_events)
    
    pattern = re.compile(r'(风险事件：<b>)([^<]+)(</span>)')
    if pattern.search(html):
        html = pattern.sub(lambda m: m.group(1) + risk_events_str + m.group(3), html)
    
    # 5. 更新当前状态
    status_parts = []
    for stock in stocks:
        name = stock['name']
        current = float(stock['current_price'])
        cost = float(stock['cost_price'])
        profit_pct = (current - cost) / cost * 100
        today_change = float(stock.get('today_change', 0)) * 100
        
        if name == '英维克':
            stop_loss = float(stock.get('stop_loss_price', 64))
            status_parts.append("英维克%.2f元（%+.2f%%）vs 止损%.2f元，浮亏%.1f%%" % (current, today_change, stop_loss, profit_pct))
        elif name == '铜冠铜箔':
            status_parts.append("铜冠铜箔%.2f元（%+.2f%%），浮盈%.1f%%" % (current, today_change, profit_pct))
        elif name == '*ST建艺':
            status_parts.append("*ST建艺%.2f元（%+.2f%%），摘帽审核中" % (current, today_change))
        elif name == '雅克科技':
            status_parts.append("雅克科技%.2f元（%+.2f%%），HBM赛道" % (current, today_change))
    
    status_str = "；".join(status_parts)
    
    pattern = re.compile(r'(当前状态：<b>)([^<]+)(</span>)')
    if pattern.search(html):
        html = pattern.sub(lambda m: m.group(1) + status_str + m.group(3), html)
    
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print("  ✅ 智能预警系统更新完成（%d紧急/%d风险/%d关注）" % (critical_count, warning_count, info_count))
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


def generate_topic_card_html(topic, level='A'):
    """
    根据题材数据生成HTML卡片
    
    Args:
        topic: 题材数据字典
        level: 级别 'S', 'A', 'B'
    
    Returns:
        str: HTML卡片代码
    """
    tid = topic.get('id', '')
    name = topic.get('name', '新题材')
    core_logic = topic.get('core_logic', '')
    total_score = topic.get('total_score', 0)
    target_stocks = topic.get('target_stocks', [])
    recent_catalyst = topic.get('recent_catalyst', topic.get('catalyst_summary', ''))
    dimension_scores = topic.get('dimension_scores', {})
    prosperity_score = topic.get('prosperity_score', 0)
    prosperity_trend = topic.get('prosperity_trend', 'stable')
    fund_flow = topic.get('fund_flow', '')
    policy_support = topic.get('policy_support', '')
    leader_stock = topic.get('leader_stock', '')
    mid_cap_stock = topic.get('mid_cap_stock', '')
    flexible_stock = topic.get('flexible_stock', '')
    
    # 级别对应的颜色和样式
    level_configs = {
        'S': {
            'rating_class': 'rating-S',
            'card_class': 'topic-card p-6 bg-gradient-to-r from-purple-50 to-pink-50 border border-purple-200 rounded-2xl',
            'text_color': 'text-purple-600',
            'bg_color': 'bg-purple-100',
            'progress_color': 'from-purple-400 to-purple-600',
            'tag_class': 'bg-purple-100 text-purple-700'
        },
        'A': {
            'rating_class': 'rating-A',
            'card_class': 'topic-card p-4 bg-gradient-to-r from-yellow-50 to-amber-50 border border-yellow-200 rounded-xl',
            'text_color': 'text-yellow-600',
            'bg_color': 'bg-yellow-100',
            'progress_color': 'from-yellow-400 to-amber-500',
            'tag_class': 'bg-yellow-100 text-yellow-700'
        },
        'B': {
            'rating_class': 'rating-B',
            'card_class': 'topic-card p-4 bg-gradient-to-r from-purple-50 to-violet-50 border border-purple-200 rounded-xl',
            'text_color': 'text-purple-600',
            'bg_color': 'bg-purple-100',
            'progress_color': 'from-purple-400 to-violet-500',
            'tag_class': 'bg-purple-100 text-purple-700'
        }
    }
    
    config = level_configs.get(level, level_configs['A'])
    
    # 生成标的标签HTML
    tags_html = ''
    if target_stocks:
        for stock in target_stocks[:4]:
            stock_name = stock if isinstance(stock, str) else stock.get('name', '')
            if stock_name:
                tags_html += f'<span class="{config["tag_class"]} px-3 py-1 rounded-full text-sm font-semibold">{stock_name}</span>\n'
    
    # S级卡片有更丰富的内容
    if level == 'S':
        # 维度评分
        dims_html = ''
        dim_names = {
            'policy': '政策强度',
            'industry': '产业逻辑', 
            'capital': '资金关注',
            'technology': '技术成熟度',
            'performance': '业绩弹性'
        }
        dim_count = 0
        for dim_key, dim_name in dim_names.items():
            if dim_key in dimension_scores and dim_count < 3:
                score = dimension_scores[dim_key]
                dims_html += f'''
                        <div class="p-3 bg-white/60 rounded-xl">
                            <div class="flex items-center justify-between mb-1">
                                <span class="text-xs text-gray-500">{dim_name}</span>
                                <span class="font-bold {config["text_color"]}">{score}分</span>
                            </div>
                            <div class="h-2 bg-gray-200 rounded-full overflow-hidden">
                                <div class="h-full bg-gradient-to-r {config["progress_color"]} rounded-full" style="width: {score}%;"></div>
                            </div>
                        </div>
                '''
                dim_count += 1
        
        # 补满3个
        for i in range(3 - dim_count):
            dims_html += f'''
                        <div class="p-3 bg-white/60 rounded-xl">
                            <div class="flex items-center justify-between mb-1">
                                <span class="text-xs text-gray-500">维度{i+1}</span>
                                <span class="font-bold {config["text_color"]}">--分</span>
                            </div>
                            <div class="h-2 bg-gray-200 rounded-full overflow-hidden">
                                <div class="h-full bg-gradient-to-r {config["progress_color"]} rounded-full" style="width: 0%;"></div>
                            </div>
                        </div>
            '''
        
        catalyst_html = ''
        if recent_catalyst:
            catalyst_html = f'''
                    <div class="flex items-center gap-2 p-3 bg-green-50 rounded-xl border border-green-200">
                        <span class="text-lg">⚡</span>
                        <span class="text-sm text-gray-700"><strong>今日催化：</strong>{recent_catalyst}</span>
                    </div>
            '''
        
        # 额外信息卡片（景气度、资金、政策、龙头）
        extra_info_html = ""
        info_items = []
        if prosperity_score > 0:
            if prosperity_trend == "up":
                trend_icon = "📈"
            elif prosperity_trend == "down":
                trend_icon = "📉"
            else:
                trend_icon = "➡️"
            info_items.append(("景气度", f"{prosperity_score}分 {trend_icon}", "bg-orange-50 text-orange-700"))
        if fund_flow:
            info_items.append(("资金流向", fund_flow, "bg-blue-50 text-blue-700"))
        if policy_support:
            info_items.append(("政策支持", policy_support, "bg-purple-50 text-purple-700"))
        if leader_stock:
            info_items.append(("龙头标的", leader_stock, "bg-yellow-50 text-yellow-700"))
        
        if info_items:
            items_html = ""
            for label, value, color_class in info_items[:4]:
                items_html += '<div class="p-2 rounded-lg ' + color_class + '">'
                items_html += '<div class="text-xs opacity-75">' + label + '</div>'
                items_html += '<div class="font-bold text-sm">' + value + '</div>'
                items_html += '</div>'
            extra_info_html = '<div class="grid grid-cols-4 gap-2 mt-4">' + items_html + '</div>'
        
        # 深度分析链接
        safe_name = ''.join(c if c.isalnum() or c in '-_' else '_' for c in name)
        detail_url = f'../题材深度/{tid}_{safe_name}.html'
        depth_link_html = f'''
                    <a href="{detail_url}" class="mt-4 block w-full py-3 px-6 bg-gradient-to-r {config['progress_color']} text-white text-center font-bold rounded-xl hover:shadow-lg transition-all hover:scale-[1.02]">
                        🔍 查看题材深度分析
                    </a>
        '''

        card_html = f'''
                <div data-topic-id="{tid}" class="{config["card_class"]}">
                    <div class="flex items-start justify-between mb-4">
                        <div class="flex items-center gap-4">
                            <div class="{config["rating_class"]} w-14 h-14 rounded-2xl flex items-center justify-center text-white font-black text-2xl">{level}</div>
                            <div>
                                <h3 class="text-xl font-black text-gray-800">{name}</h3>
                                <p class="text-gray-500 text-sm mt-1">{core_logic}</p>
                            </div>
                        </div>
                        <div class="text-right">
                            <div class="text-4xl font-black {config["text_color"]}">{total_score}分</div>
                            <div class="text-sm text-gray-500">综合评分</div>
                        </div>
                    </div>
                    
                    <div class="grid grid-cols-3 gap-4 mb-4">
{dims_html}
                    </div>
                    
                    <div class="flex flex-wrap gap-3 mb-4">
{tags_html}
                    </div>
                    
                    {catalyst_html}
                    {extra_info_html}
                    {depth_link_html}
                </div>
                <!-- 新增题材卡片 end -->
        '''
    else:
        # A级和B级简化版
        card_html = f'''
                    <div data-topic-id="{tid}" class="{config["card_class"]}">
                        <div class="flex items-center justify-between mb-3">
                            <div class="flex items-center gap-3">
                                <div class="{config["rating_class"]} w-10 h-10 rounded-xl flex items-center justify-center text-white font-black">{level}</div>
                                <div>
                                    <h3 class="font-bold text-gray-800">{name}</h3>
                                    <p class="text-xs text-gray-500">{core_logic[:40]}...</p>
                                </div>
                            </div>
                            <span class="text-2xl font-black {config["text_color"]}">{total_score}分</span>
                        </div>
                        <div class="flex gap-2">
{tags_html}
                        <div class="text-xs text-gray-500 mt-2 flex flex-wrap gap-2">
                            {f'<span class="bg-white/60 px-2 py-1 rounded">景气度{prosperity_score}分</span>' if prosperity_score > 0 else ''}
                            {f'<span class="bg-white/60 px-2 py-1 rounded">龙头：{leader_stock}</span>' if leader_stock else ''}
                            {f'<span class="bg-white/60 px-2 py-1 rounded">催化：{recent_catalyst[:20]}...</span>' if recent_catalyst and len(recent_catalyst) > 20 else f'<span class="bg-white/60 px-2 py-1 rounded">催化：{recent_catalyst}</span>' if recent_catalyst else ''}
                        </div>
                        </div>
                    </div>
                    <!-- 新增题材卡片 end -->
        '''
    
    return card_html


def find_existing_topic_ids(html):
    """从HTML中提取所有已有的题材ID"""
    import re
    pattern = r'data-topic-id="([^"]+)"'
    return set(re.findall(pattern, html))


def insert_new_topic_cards(html, new_topics, level):
    """
    在指定级别的区域插入新题材卡片
    """
    if not new_topics:
        return html
    
    # 生成所有新卡片的HTML
    new_cards_html = ''
    newline = chr(10)
    for topic in new_topics:
        new_cards_html += generate_topic_card_html(topic, level)
    
    if level == 'S':
        # 在S级区域最后，A级开始前插入
        a_section_start = html.find('A级题材')
        if a_section_start > 0:
            html = html[:a_section_start] + new_cards_html + newline + html[a_section_start:]
    
    elif level == 'A':
        # 在A级区域最后，B级开始前插入
        b_section_start = html.find('B级观察题材')
        if b_section_start > 0:
            html = html[:b_section_start] + new_cards_html + newline + html[b_section_start:]
    
    elif level == 'B':
        # 在B级区域最后，配置策略矩阵前插入
        config_start = html.find('配置策略建议')
        if config_start > 0:
            html = html[:config_start] + new_cards_html + newline + html[config_start:]
    
    return html



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
    
    # ===== 0. 检测并生成新增题材卡片 =====
    existing_ids = find_existing_topic_ids(html)
    
    new_s_topics = [t for t in s_topics if t.get('id') and t['id'] not in existing_ids]
    new_a_topics = [t for t in a_topics if t.get('id') and t['id'] not in existing_ids]
    new_b_topics = [t for t in b_topics if t.get('id') and t['id'] not in existing_ids]
    
    if new_s_topics or new_a_topics or new_b_topics:
        print(f"   🆕 发现新增题材：S级{len(new_s_topics)}个，A级{len(new_a_topics)}个，B级{len(new_b_topics)}个")
        
        if new_s_topics:
            html = insert_new_topic_cards(html, new_s_topics, 'S')
            for t in new_s_topics:
                print(f"      + S级: {t.get('name')} ({t.get('id')})")
        
        if new_a_topics:
            html = insert_new_topic_cards(html, new_a_topics, 'A')
            for t in new_a_topics:
                print(f"      + A级: {t.get('name')} ({t.get('id')})")
        
        if new_b_topics:
            html = insert_new_topic_cards(html, new_b_topics, 'B')
            for t in new_b_topics:
                print(f"      + B级: {t.get('name')} ({t.get('id')})")
        
        print("   ✅ 新增题材卡片已自动生成")
    
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
    
    # ===== 4.5 逐卡更新B级题材 =====
    b_topics = data.get('b_level_topics', [])
    b_updated = 0
    for topic in b_topics:
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
            lambda m: f'{m.group(1)}{topic.get("subtitle", topic.get("core_logic", ""))}{m.group(2)}',
            card_html
        )
        
        # 更新综合评分
        total_score = topic.get('total_score', 0)
        card_html = re.sub(
            r'(<span class="text-2xl font-black text-purple-600">)(\d+)(分</span>)',
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
                tags_html += f'                            <span class="bg-purple-100 text-purple-700 px-2 py-0.5 rounded-full text-xs">{tag}</span>\n'
            tags_html += '                        '
            card_html = tags_pattern.sub(
                lambda m: f'{m.group(1)}{tags_html}{m.group(3)}',
                card_html,
                count=1
            )
        
        # 替换回原HTML
        html = html[:start] + card_html + html[end:]
        b_updated += 1
    
    # ===== 5. 更新时间戳 =====
    html = re.sub(
        r'(数据更新时间：)([^<]+)(</p>)',
        lambda m: f'{m.group(1)}{update_time}{m.group(3)}',
        html
    )
    
    # ===== 6. 更新配置策略建议 =====
    allocation = data.get('allocation_strategy', {})
    if allocation:
        # 进攻配置
        off = allocation.get('offensive', {})
        if off:
            off_title = off.get('title', '🔥 进攻配置')
            off_ratio = off.get('ratio', '35%仓位')
            off_content = off.get('content', '')
            html = re.sub(
                r'(font-bold text-purple-700 mb-2">)[^<]+(（[^<]+）</div>)',
                lambda m: f'{m.group(1)}{off_title}（{off_ratio}）{m.group(2)[m.group(2).find("</div>"):]}',
                html
            )
            # 简化：直接替换标题行和内容
            off_header_pattern = re.compile(
                r'(<div class="p-4 bg-purple-50 border border-purple-200 rounded-xl">\s*<div class="font-bold text-purple-700 mb-2">)[^<]+(</div>\s*<p class="text-sm text-gray-700">)[^<]*(</p>)',
                re.DOTALL
            )
            html = off_header_pattern.sub(
                lambda m: f'{m.group(1)}{off_title}（{off_ratio}）{m.group(2)}{off_content}{m.group(3)}',
                html
            )
        
        # 趋势配置
        trend = allocation.get('trend', {})
        if trend:
            trend_title = trend.get('title', '📈 趋势配置')
            trend_ratio = trend.get('ratio', '25%仓位')
            trend_content = trend.get('content', '')
            trend_pattern = re.compile(
                r'(<div class="p-4 bg-red-50 border border-red-200 rounded-xl">\s*<div class="font-bold text-red-700 mb-2">)[^<]+(</div>\s*<p class="text-sm text-gray-700">)[^<]*(</p>)',
                re.DOTALL
            )
            html = trend_pattern.sub(
                lambda m: f'{m.group(1)}{trend_title}（{trend_ratio}）{m.group(2)}{trend_content}{m.group(3)}',
                html
            )
        
        # 防御配置
        defen = allocation.get('defensive', {})
        if defen:
            def_title = defen.get('title', '🛡️ 防御配置')
            def_ratio = defen.get('ratio', '45%仓位')
            def_content = defen.get('content', '')
            def_pattern = re.compile(
                r'(<div class="p-4 bg-yellow-50 border border-yellow-200 rounded-xl">\s*<div class="font-bold text-yellow-700 mb-2">)[^<]+(</div>\s*<p class="text-sm text-gray-700">)[^<]*(</p>)',
                re.DOTALL
            )
            html = def_pattern.sub(
                lambda m: f'{m.group(1)}{def_title}（{def_ratio}）{m.group(2)}{def_content}{m.group(3)}',
                html
            )
        
        # 重要警示
        warn = allocation.get('warning', {})
        if warn:
            warn_title = warn.get('title', '⚠️ 重要警示')
            warn_subtitle = warn.get('subtitle', '必须回避')
            warn_content = warn.get('content', '')
            warn_pattern = re.compile(
                r'(<div class="p-4 bg-red-100 border border-red-300 rounded-xl">\s*<div class="font-bold text-red-700 mb-2">)[^<]+(</div>\s*<p class="text-sm text-gray-700">)[^<]*(</p>)',
                re.DOTALL
            )
            html = warn_pattern.sub(
                lambda m: f'{m.group(1)}{warn_title}（{warn_subtitle}）{m.group(2)}{warn_content}{m.group(3)}',
                html
            )
    
    # ===== 7. 更新催化事件日历 =====
    catalyst_calendar = data.get('catalyst_calendar', [])
    if catalyst_calendar:
        # 找到催化事件日历区域
        cal_section_start = html.find('📅 近期催化事件日历')
        if cal_section_start > 0:
            # 找到grid容器
            grid_start = html.find('<div class="grid grid-cols-4 gap-4">', cal_section_start)
            if grid_start > 0:
                grid_end = html.find('</div>', grid_start)
                # 找到grid结束的位置（</div>后面应该是区域的闭合）
                # 先找到grid内所有内容的结束
                pos = grid_start + len('<div class="grid grid-cols-4 gap-4">')
                depth = 1
                while depth > 0 and pos < len(html):
                    if html[pos:pos+4] == '<div':
                        depth += 1
                        pos += 4
                    elif html[pos:pos+6] == '</div>':
                        depth -= 1
                        pos += 6
                    else:
                        pos += 1
                grid_end = pos
                
                # 生成新的事件卡片
                events_html = '\n'
                for event in catalyst_calendar[:4]:  # 最多4个
                    date = event.get('date', '')
                    title = event.get('title', event.get('event', ''))
                    impact = event.get('impact', '')
                    related = event.get('related_topics', [])
                    related_str = '、'.join(related) if related else ''
                    
                    events_html += f'''                <div class="p-4 bg-gradient-to-br from-gray-100 to-gray-200 border border-gray-300 rounded-2xl text-center">
                    <div class="text-3xl font-black text-gray-600 mb-1">{date}</div>
                    <div class="text-sm font-bold text-gray-800 mb-2">{title}</div>
                    <div class="text-xs text-gray-500 mb-2">{impact}</div>
                    <span class="bg-gray-200 text-gray-700 text-xs px-2 py-0.5 rounded-full font-semibold">{related_str}</span>
                </div>
'''
                events_html += '            '
                
                # 替换grid内容
                html = html[:grid_start] + f'<div class="grid grid-cols-4 gap-4">{events_html}</div>' + html[grid_end:]
    
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"  ✅ 智能选题助手更新完成（S级：{s_updated}个，A级：{a_updated}个，B级：{b_updated}个）")




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
    """更新预判验证页面 - 整体容器替换模式"""
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
        r'(text-3xl font-black text-green-600\">)(\d+\.?\d*)(%</div>)',
        lambda m: f'{m.group(1)}{acc_num}{m.group(3)}', html
    )
    
    # 更新环形进度条
    html = re.sub(
        r'(accuracy-ring.*?style=\"--p: )(\d+)(%)',
        lambda m: f'{m.group(1)}{int(float(acc_num))}{m.group(3)}', html
    )
    
    # 更新分析师等级
    html = re.sub(
        r'(text-4xl font-black text-purple-600\">)([A-Z]级)(</div>)',
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
            rf'(text-3xl font-black text[^\"]+\">)(\d+)(</div>\s*<div class=\"text-sm text-gray-500\">{label})',
            re.DOTALL
        )
        html = pattern.sub(lambda m: f'{m.group(1)}{value}{m.group(3)}', html)
    
    # ===== 生成待验证预判卡片 =====
    pending_html = ""
    for pred in pending:
        pred_id = pred.get('id', '')
        title = pred.get('title', '')
        verify_cycle = pred.get('verify_cycle', 'T+3')
        logic = pred.get('logic', '')
        progress = pred.get('progress', 0)
        related = pred.get('related_stocks', [])
        related_str = '、'.join(related) if related else ''
        verify_date = pred.get('verify_date', '')
        latest_obs = pred.get('latest_observation', {})
        obs_date = latest_obs.get('date', '')
        obs_content = latest_obs.get('content', '')
        
        verify_display = verify_date[5:] if verify_date else '待定'
        
        card_parts = []
        card_parts.append('                <div data-prediction-id="' + pred_id + '" class="prediction-card p-5 bg-gradient-to-r from-yellow-50 to-amber-50 border border-yellow-200 rounded-2xl">')
        card_parts.append('                    <div class="flex items-start justify-between mb-3">')
        card_parts.append('                        <div class="flex-1">')
        card_parts.append('                            <div class="flex items-center gap-3 mb-2">')
        card_parts.append('                                <span class="bg-yellow-100 text-yellow-700 text-xs px-3 py-1 rounded-full font-bold">' + verify_cycle + '验证</span>')
        card_parts.append('                                <span class="text-sm text-gray-500">' + related_str + '</span>')
        card_parts.append('                            </div>')
        card_parts.append('                            <h3 class="text-lg font-bold text-gray-800 mb-2">' + title + '</h3>')
        card_parts.append('                            <p class="text-sm text-gray-600">预判逻辑：' + logic + '</p>')
        card_parts.append('                        </div>')
        card_parts.append('                        <div class="text-right ml-6">')
        card_parts.append('                            <div class="text-sm text-gray-500 mb-1">验证时间</div>')
        card_parts.append('                            <div class="font-bold text-yellow-600">' + verify_display + '</div>')
        card_parts.append('                        </div>')
        card_parts.append('                    </div>')
        card_parts.append('                    <div class="mb-3">')
        card_parts.append('                        <div class="flex justify-between text-xs text-gray-500 mb-1">')
        card_parts.append('                            <span>验证进度</span>')
        card_parts.append('                            <span class="text-green-600 font-bold">' + str(progress) + '%</span>')
        card_parts.append('                        </div>')
        card_parts.append('                        <div class="w-full bg-gray-200 rounded-full h-2">')
        card_parts.append('                            <div class="bg-gradient-to-r from-green-400 to-emerald-500 rounded-full h-2" style="width: ' + str(progress) + '%"></div>')
        card_parts.append('                        </div>')
        card_parts.append('                    </div>')
        
        if obs_date or obs_content:
            card_parts.append('                    <div class="bg-white/60 rounded-lg p-3">')
            card_parts.append('                        <div class="text-xs text-gray-500 mb-1">📅 ' + obs_date + ' 最新观察</div>')
            card_parts.append('                        <p class="text-sm text-gray-600">' + obs_content + '</p>')
            card_parts.append('                    </div>')
        
        card_parts.append('                </div>')
        pending_html += '\n'.join(card_parts) + '\n'
    
    # 整体替换待验证列表容器
    pending_pattern = re.compile(
        r'(<div id=\"pendingList\" class=\"space-y-4\">).*?(</div>\s*\n\s*</div>\s*\n\s*<!-- 【第三区)',
        re.DOTALL
    )
    if pending_pattern.search(html):
        html = pending_pattern.sub(
            lambda m: m.group(1) + '\n' + pending_html + '                ' + m.group(2),
            html
        )
    
    # ===== 生成正确记录列表 =====
    correct_records = [h for h in history if h.get('result') == '正确']
    correct_html = ""
    for record in correct_records:
        rec_id = record.get('id', '')
        title = record.get('title', '')
        price_change = record.get('price_change', '')
        predict_date = record.get('predict_date', '')
        verify_date = record.get('verify_date', '')
        stocks = record.get('stocks', [])
        stocks_str = '、'.join(stocks) if stocks else ''
        
        pred_d = predict_date[5:] if predict_date else ''
        ver_d = verify_date[5:] if verify_date else ''
        
        item_parts = []
        item_parts.append('                    <div data-prediction-id="' + rec_id + '" class="p-4 bg-green-50 border-l-4 border-green-500 rounded-r-xl">')
        item_parts.append('                        <div class="flex items-start justify-between mb-2">')
        item_parts.append('                            <span class="font-bold text-gray-800">' + title + '</span>')
        item_parts.append('                            <span class="bg-green-100 text-green-700 text-xs px-2 py-0.5 rounded-full font-bold">' + price_change + ' 兑现</span>')
        item_parts.append('                        </div>')
        item_parts.append('                        <div class="text-xs text-gray-500">预判：' + pred_d + ' | 验证：' + ver_d + ' | 标的：' + stocks_str + '</div>')
        item_parts.append('                    </div>')
        correct_html += '\n'.join(item_parts) + '\n'
    
    # 整体替换正确记录容器
    correct_pattern = re.compile(
        r'(<div id=\"correctRecords\" class=\"space-y-3\">).*?(</div>\s*\n\s*</div>\s*\n\s*<div class=\"card-glass p-6\")',
        re.DOTALL
    )
    if correct_pattern.search(html):
        html = correct_pattern.sub(
            lambda m: m.group(1) + '\n' + correct_html + '                ' + m.group(2),
            html
        )
    
    # ===== 生成错误记录卡片 =====
    wrong_records = [h for h in history if h.get('result') == '错误']
    wrong_html = ""
    for record in wrong_records:
        rec_id = record.get('id', '')
        title = record.get('title', '')
        price_change = record.get('price_change', '')
        predict_date = record.get('predict_date', '')
        verify_date = record.get('verify_date', '')
        error_analysis = record.get('error_analysis', [])
        lessons = record.get('lessons', '')
        
        pred_d = predict_date[5:] if predict_date else ''
        ver_d = verify_date[5:] if verify_date else ''
        
        card_parts = []
        card_parts.append('                    <div data-prediction-id="' + rec_id + '" class="p-4 bg-red-50 border-l-4 border-red-500 rounded-r-xl">')
        card_parts.append('                        <div class="flex items-start justify-between mb-2">')
        card_parts.append('                            <span class="font-bold text-gray-800">' + title + '</span>')
        card_parts.append('                            <span class="bg-red-100 text-red-700 text-xs px-2 py-0.5 rounded-full font-bold">' + price_change + ' 未兑现</span>')
        card_parts.append('                        </div>')
        card_parts.append('                        <div class="text-xs text-gray-500 mb-2">预判：' + pred_d + ' | 验证：' + ver_d + '</div>')
        
        if error_analysis:
            items_html = ''.join('<li>• ' + item + '</li>\n' for item in error_analysis)
            card_parts.append('                        <div class="p-3 bg-white rounded-lg">')
            card_parts.append('                            <div class="text-sm font-bold text-red-700 mb-1">🔍 错误原因分析：</div>')
            card_parts.append('                            <ul class="text-xs text-gray-600 space-y-1">' + items_html + '</ul>')
            card_parts.append('                        </div>')
        
        if lessons:
            card_parts.append('                        <div class="p-3 bg-yellow-50 rounded-lg mt-2">')
            card_parts.append('                            <div class="text-sm font-bold text-yellow-700 mb-1">💡 重要经验教训：</div>')
            card_parts.append('                            <p class="text-xs text-gray-600">' + lessons + '</p>')
            card_parts.append('                        </div>')
        
        card_parts.append('                    </div>')
        wrong_html += '\n'.join(card_parts) + '\n'
    
    # 整体替换错误记录容器
    wrong_pattern = re.compile(
        r'(<div id=\"wrongRecords\" class=\"space-y-4\">).*?(</div>\s*\n\s*</div>\s*\n\s*</div>\s*\n\s*<!-- 【第四区)',
        re.DOTALL
    )
    if wrong_pattern.search(html):
        html = wrong_pattern.sub(
            lambda m: m.group(1) + '\n' + wrong_html + '                ' + m.group(2),
            html
        )
    
    # 更新badge数字
    html = re.sub(
        r'(<span id=\"pendingBadge\"[^>]*>)(\d+)(个</span>)',
        lambda m: m.group(1) + str(len(pending)) + m.group(3),
        html
    )
    
    # 更新正确/错误记录的'最近N个'标签
    html = re.sub(
        r'(✅ 验证正确记录\s*<span[^>]*>最近)\d+(个</span>)',
        lambda m: m.group(1) + str(len(correct_records)) + m.group(2),
        html
    )
    html = re.sub(
        r'(❌ 验证错误记录[^<]*<span[^>]*>最近)\d+(个</span>)',
        lambda m: m.group(1) + str(len(wrong_records)) + m.group(2),
        html
    )
    
    # ===== 准确率趋势数据更新 =====
    accuracy_trends = system_info.get('accuracy_trends', [])
    if accuracy_trends:
        by_month = {}
        for item in accuracy_trends:
            month = item.get('month', '')
            acc = item.get('accuracy', 0)
            if month:
                by_month[month] = acc
        
        for month, acc in by_month.items():
            pattern = month + '：\\d+%'
            html = re.sub(pattern, month + '：' + str(acc) + '%', html)
    
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"  ✅ 预判验证系统更新完成（累计：{total_pred}，正确：{correct_count}，错误：{wrong_count}，待验证：{len(pending)}）")



# ==================== 题材深度分析模块 ====================

def load_topic_details_data():
    """加载题材深度分析数据"""
    with open('data/topic_details.json', 'r', encoding='utf-8') as f:
        return json.load(f)


def generate_topic_detail_page(topic_basic, detail_data):
    """
    生成题材深度分析详情页
    
    Args:
        topic_basic: 题材基础数据（来自topics.json）
        detail_data: 题材深度分析数据（来自topic_details.json）
    
    Returns:
        str: 完整的HTML页面代码
    """
    tid = topic_basic.get('id', '')
    name = detail_data.get('name', topic_basic.get('name', ''))
    level = detail_data.get('level', topic_basic.get('level', 'A'))
    summary = detail_data.get('summary', '')
    update_time = detail_data.get('update_time', '2026年06月12日')
    
    # 级别颜色配置
    level_colors = {
        'S': {'bg': 'from-red-500 to-pink-600', 'text': 'text-red-600', 'light': 'bg-red-50', 'border': 'border-red-200'},
        'A': {'bg': 'from-yellow-500 to-orange-500', 'text': 'text-yellow-600', 'light': 'bg-yellow-50', 'border': 'border-yellow-200'},
        'B': {'bg': 'from-purple-500 to-indigo-600', 'text': 'text-purple-600', 'light': 'bg-purple-50', 'border': 'border-purple-200'},
    }
    colors = level_colors.get(level, level_colors['A'])
    
    # 产业链分析HTML
    industry_chain = detail_data.get('industry_chain', {})
    chain_html = ''
    chain_order = ['upstream', 'midstream', 'downstream']
    
    for chain_key in chain_order:
        chain = industry_chain.get(chain_key, {})
        if not chain:
            continue
        companies = chain.get('companies', [])
        comp_html = ''
        for comp in companies:
            imp_class = 'bg-purple-100 text-purple-700' if comp.get('importance') == 'high' else 'bg-gray-100 text-gray-600'
            comp_html += f'''
                        <div class="flex items-center gap-2 p-2 bg-white/50 rounded-lg">
                            <span class="text-lg">🏭</span>
                            <div>
                                <div class="font-semibold text-gray-800">{comp.get('name', '')}</div>
                                <div class="text-xs text-gray-500">{comp.get('role', '')}</div>
                            </div>
                        </div>
            '''
        
        chain_html += f'''
                <div class="bg-white/80 backdrop-blur rounded-2xl p-6 border {colors['border']}">
                    <h3 class="text-xl font-bold text-gray-800 mb-2">{chain.get('name', '')}</h3>
                    <p class="text-gray-600 mb-4">{chain.get('description', '')}</p>
                    <div class="grid grid-cols-2 gap-3">
                        {comp_html}
                    </div>
                </div>
        '''
    
    # 标的分析HTML
    stocks = detail_data.get('target_stocks_analysis', [])
    stocks_html = ''
    tier_colors = {
        '龙头': 'from-red-500 to-pink-500',
        '中军': 'from-blue-500 to-cyan-500',
        '弹性': 'from-green-500 to-emerald-500',
        '受益': 'from-gray-500 to-slate-500'
    }
    
    for stock in stocks:
        tier = stock.get('tier', '')
        tier_color = tier_colors.get(tier, 'from-gray-500 to-slate-500')
        risk_color = 'text-green-600' if stock.get('risk_level') == '低' else 'text-yellow-600' if stock.get('risk_level') == '中' else 'text-red-600'
        
        stocks_html += f'''
                <div class="bg-white rounded-2xl p-6 shadow-lg hover:shadow-xl transition-shadow border border-gray-100">
                    <div class="flex items-start justify-between mb-4">
                        <div>
                            <div class="flex items-center gap-2 mb-1">
                                <h4 class="text-xl font-bold text-gray-800">{stock.get('name', '')}</h4>
                                <span class="px-3 py-1 bg-gradient-to-r {tier_color} text-white text-xs font-bold rounded-full">{tier}</span>
                            </div>
                            <p class="text-gray-500 text-sm">{stock.get('role', '')}</p>
                        </div>
                        <div class="text-right">
                            <div class="text-lg font-bold {colors['text']}">{stock.get('market_cap', '')}</div>
                            <div class="text-xs text-gray-400">市值</div>
                        </div>
                    </div>
                    
                    <div class="grid grid-cols-3 gap-4 mb-4">
                        <div class="text-center p-3 bg-gray-50 rounded-xl">
                            <div class="text-2xl font-bold {colors['text']}">{stock.get('elasticity_score', 0)}</div>
                            <div class="text-xs text-gray-500">弹性评分</div>
                        </div>
                        <div class="text-center p-3 bg-gray-50 rounded-xl">
                            <div class="text-lg font-bold {risk_color}">{stock.get('risk_level', '')}</div>
                            <div class="text-xs text-gray-500">风险等级</div>
                        </div>
                        <div class="text-center p-3 bg-gray-50 rounded-xl">
                            <div class="text-sm font-bold text-green-600">{stock.get('target_price', '')}</div>
                            <div class="text-xs text-gray-500">目标空间</div>
                        </div>
                    </div>
                    
                    <div class="p-4 bg-gradient-to-r from-purple-50 to-pink-50 rounded-xl">
                        <div class="text-sm font-semibold text-purple-700 mb-1">💡 核心逻辑</div>
                        <p class="text-sm text-gray-700">{stock.get('logic', '')}</p>
                    </div>
                </div>
        '''
    
    # 催化剂时间线HTML
    catalysts = detail_data.get('catalyst_timeline', [])
    catalyst_html = ''
    for i, cat in enumerate(catalysts):
        impact_class = 'bg-red-100 text-red-700 border-red-300' if '强' in cat.get('impact', '') else 'bg-yellow-100 text-yellow-700 border-yellow-300' if '中' in cat.get('impact', '') else 'bg-gray-100 text-gray-600 border-gray-300'
        is_last = 'border-l-2 border-transparent' if i == len(catalysts) - 1 else 'border-l-2 border-purple-200'
        catalyst_html += f'''
                    <div class="relative pl-8 pb-6 {is_last}">
                        <div class="absolute left-[-9px] top-0 w-5 h-5 bg-gradient-to-r from-purple-500 to-pink-500 rounded-full border-4 border-white shadow"></div>
                        <div class="bg-white rounded-xl p-4 shadow-md border border-gray-100">
                            <div class="flex items-center justify-between mb-2">
                                <span class="text-sm font-bold text-gray-800">{cat.get('date', '')}</span>
                                <span class="px-2 py-1 text-xs font-semibold rounded-full border {impact_class}">{cat.get('impact', '')}</span>
                            </div>
                            <p class="text-gray-700">{cat.get('event', '')}</p>
                        </div>
                    </div>
        '''
    
    # 核心风险HTML
    risks = detail_data.get('core_risks', [])
    risks_html = ''
    for risk in risks:
        risks_html += f'''
                    <div class="flex items-start gap-3 p-3 bg-red-50 rounded-xl border border-red-100">
                        <span class="text-lg">⚠️</span>
                        <span class="text-gray-700">{risk}</span>
                    </div>
        '''
    
    # 投资策略HTML
    strategy = detail_data.get('investment_strategy', {})
    strategy_html = f'''
                <div class="grid grid-cols-2 md:grid-cols-4 gap-4">
                    <div class="bg-white rounded-xl p-4 text-center border border-gray-100">
                        <div class="text-2xl mb-2">🎯</div>
                        <div class="text-sm text-gray-500 mb-1">仓位建议</div>
                        <div class="font-bold text-gray-800">{strategy.get('position', '')}</div>
                    </div>
                    <div class="bg-white rounded-xl p-4 text-center border border-gray-100">
                        <div class="text-2xl mb-2">📈</div>
                        <div class="text-sm text-gray-500 mb-1">入场时机</div>
                        <div class="font-bold text-gray-800">{strategy.get('entry_point', '')}</div>
                    </div>
                    <div class="bg-white rounded-xl p-4 text-center border border-gray-100">
                        <div class="text-2xl mb-2">🛑</div>
                        <div class="text-sm text-gray-500 mb-1">止损设置</div>
                        <div class="font-bold text-red-600">{strategy.get('stop_loss', '')}</div>
                    </div>
                    <div class="bg-white rounded-xl p-4 text-center border border-gray-100">
                        <div class="text-2xl mb-2">⏰</div>
                        <div class="text-sm text-gray-500 mb-1">投资周期</div>
                        <div class="font-bold text-gray-800">{strategy.get('time_horizon', '')}</div>
                    </div>
                </div>
                <div class="mt-4 p-4 bg-gradient-to-r from-green-50 to-emerald-50 rounded-xl border border-green-100">
                    <div class="font-semibold text-green-700 mb-1">💰 止盈策略</div>
                    <p class="text-green-600">{strategy.get('take_profit', '')}</p>
                </div>
    '''
    
    # 市场规模HTML
    market_size = detail_data.get('market_size', {})
    market_html = ''
    if market_size:
        market_items = [
            ('总市场规模', market_size.get('total_2026', '')),
            ('同比增长', market_size.get('growth_rate', '')),
        ]
        if 'ai_pc_penetration' in market_size:
            market_items.append(('AI PC渗透率', market_size['ai_pc_penetration']))
        if 'ai_storage_ratio' in market_size:
            market_items.append(('AI存储占比', market_size['ai_storage_ratio']))
        if 'market_value' in market_size:
            market_items.append(('市场价值', market_size['market_value']))
        if 'cagr_5year' in market_size:
            market_items.append(('5年CAGR', market_size['cagr_5year']))
        
        items_html = ''
        for label, value in market_items:
            items_html += f'''
                        <div class="text-center">
                            <div class="text-2xl font-bold text-white">{value}</div>
                            <div class="text-sm text-white/80">{label}</div>
                        </div>
            '''
        
        market_html = f'''
            <div class="bg-gradient-to-r {colors['bg']} rounded-3xl p-8 text-white">
                <h2 class="text-2xl font-bold mb-6">📊 市场规模与增长</h2>
                <div class="grid grid-cols-2 md:grid-cols-4 gap-6">
                    {items_html}
                </div>
            </div>
        '''
    
    # 维度评分
    dim_scores = topic_basic.get('dimension_scores', {})
    dim_names = {
        'policy': ('政策强度', '📋'),
        'industry': ('产业逻辑', '🏭'),
        'capital': ('资金关注', '💰'),
        'technology': ('技术成熟度', '🔬'),
        'performance': ('业绩弹性', '📈'),
        'catalyst': ('催化密度', '⚡')
    }
    
    dims_html = ''
    dim_count = 0
    for dim_key, (dim_name, dim_icon) in dim_names.items():
        if dim_key in dim_scores and dim_count < 6:
            score = dim_scores[dim_key]
            dims_html += f'''
                        <div class="bg-white/60 backdrop-blur rounded-xl p-4">
                            <div class="flex items-center gap-2 mb-2">
                                <span class="text-xl">{dim_icon}</span>
                                <span class="font-semibold text-gray-700">{dim_name}</span>
                            </div>
                            <div class="flex items-center gap-3">
                                <div class="flex-1 h-3 bg-gray-200 rounded-full overflow-hidden">
                                    <div class="h-full bg-gradient-to-r {colors['bg']}" style="width: {score}%"></div>
                                </div>
                                <span class="font-bold {colors['text']}">{score}分</span>
                            </div>
                        </div>
            '''
            dim_count += 1
    
    # 构建完整页面
    page_html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{name} - 题材深度分析 | 智能选题助手</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://cdn.jsdelivr.net/npm/font-awesome@4.7.0/css/font-awesome.min.css" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.8/dist/chart.umd.min.js"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@300;400;500;700;900&display=swap');
        * {{ font-family: 'Noto Sans SC', sans-serif; }}
        body {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
        }}
        .glass-nav {{
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(20px);
            border-bottom: 1px solid rgba(255, 255, 255, 0.2);
        }}
        .card-glass {{
            background: rgba(255, 255, 255, 0.95);
            box-shadow: 0 15px 40px rgba(118, 75, 162, 0.3);
            border-radius: 24px;
        }}
        .section-title {{
            position: relative;
            display: inline-block;
        }}
        .section-title::after {{
            content: '';
            position: absolute;
            bottom: -8px;
            left: 0;
            width: 60px;
            height: 4px;
            background: linear-gradient(90deg, #667eea, #764ba2);
            border-radius: 2px;
        }}
    </style>
</head>
<body class="pb-16">
    <!-- 导航栏 -->
    <nav class="fixed top-0 left-0 right-0 z-50 glass-nav">
        <div class="max-w-5xl mx-auto px-4 py-3 flex items-center justify-between">
            <div class="flex items-center space-x-3">
                <div class="w-8 h-8 rounded-lg bg-gradient-to-br from-indigo-500 to-purple-600 flex items-center justify-center">
                    <span class="text-white text-sm font-bold">📊</span>
                </div>
                <span class="text-white font-bold text-lg">投资研究中心</span>
            </div>
            <div class="nav-links flex items-center space-x-1 flex-wrap gap-1">
                <a href="../index.html" class="text-white/80 hover:text-white hover:bg-white/10 text-sm transition-colors px-3 py-1.5 rounded-lg">首页</a>
                <a href="../daily/latest.html" class="text-white/80 hover:text-white hover:bg-white/10 text-sm transition-colors px-3 py-1.5 rounded-lg">日报</a>
                <a href="../intraday/latest.html" class="text-white/80 hover:text-white hover:bg-white/10 text-sm transition-colors px-3 py-1.5 rounded-lg">盘中</a>
                <a href="../aftermarket/latest.html" class="text-white/80 hover:text-white hover:bg-white/10 text-sm transition-colors px-3 py-1.5 rounded-lg">盘后</a>
                <a href="../industry_chain/latest.html" class="text-white/80 hover:text-white hover:bg-white/10 text-sm transition-colors px-3 py-1.5 rounded-lg">产业链</a>
                <a href="../weekly_review/latest.html" class="text-white/80 hover:text-white hover:bg-white/10 text-sm transition-colors px-3 py-1.5 rounded-lg">周复盘</a>
                <a href="../weekly_outlook/latest.html" class="text-white/80 hover:text-white hover:bg-white/10 text-sm transition-colors px-3 py-1.5 rounded-lg">周三前瞻</a>
                <a href="../周末速递/latest.html" class="text-white/80 hover:text-white hover:bg-white/10 text-sm transition-colors px-3 py-1.5 rounded-lg">周末速递</a>
                <a href="../明日催化剂/latest.html" class="text-white/80 hover:text-white hover:bg-white/10 text-sm transition-colors px-3 py-1.5 rounded-lg">明日催化</a>
                <a href="../s级催化扫描/latest.html" class="text-white/80 hover:text-white hover:bg-white/10 text-sm transition-colors px-3 py-1.5 rounded-lg">S级催化</a>
                <a href="../数据时光机/index.html" class="text-white/80 hover:text-white hover:bg-white/10 text-sm transition-colors px-3 py-1.5 rounded-lg">时光机</a>
                <a href="../monthly/latest.html" class="text-white/80 hover:text-white hover:bg-white/10 text-sm transition-colors px-3 py-1.5 rounded-lg">月报</a>
            </div>
            <button class="hamburger-btn" onclick="toggleMobileMenu()">☰</button>
            </div>
    </nav>
    
    <!-- 移动端全屏菜单 -->
    <div id="mobileMenu" class="mobile-menu">
        <button class="close-menu-btn" onclick="toggleMobileMenu()">✕</button>
        <a href="../index.html" class="mobile-menu-item" onclick="toggleMobileMenu()">🏠 首页</a>
        <a href="../daily/latest.html" class="mobile-menu-item" onclick="toggleMobileMenu()">📰 日报</a>
        <a href="../intraday/latest.html" class="mobile-menu-item" onclick="toggleMobileMenu()">📈 盘中快报</a>
        <a href="../aftermarket/latest.html" class="mobile-menu-item" onclick="toggleMobileMenu()">📉 盘后速递</a>
        <a href="../industry_chain/latest.html" class="mobile-menu-item" onclick="toggleMobileMenu()">🔗 产业链总览</a>
        <a href="../weekly_review/latest.html" class="mobile-menu-item" onclick="toggleMobileMenu()">📋 周复盘</a>
        <a href="../weekly_outlook/latest.html" class="mobile-menu-item" onclick="toggleMobileMenu()">🔮 周三前瞻</a>
        <a href="../周末速递/latest.html" class="mobile-menu-item" onclick="toggleMobileMenu()">📦 周末速递</a>
        <a href="../明日催化剂/latest.html" class="mobile-menu-item" onclick="toggleMobileMenu()">⏰ 明日催化剂</a>
        <a href="../s级催化扫描/latest.html" class="mobile-menu-item" onclick="toggleMobileMenu()">⭐ S级催化扫描</a>
        <a href="../数据时光机/index.html" class="mobile-menu-item" onclick="toggleMobileMenu()">⏳ 数据时光机</a>
        <a href="../monthly/latest.html" class="mobile-menu-item" onclick="toggleMobileMenu()">🗓️ 月度总结</a>
    </div>
    
    <script>
        function toggleMobileMenu() {{
            document.getElementById('mobileMenu').classList.toggle('show');
            document.body.style.overflow = document.getElementById('mobileMenu').classList.contains('show') ? 'hidden' : '';
        }}
    </script>

    <!-- 主内容区 -->
    <main class="max-w-7xl mx-auto px-4 pt-24 pb-12">
        
        <!-- 头部Banner -->
        <div class="card-glass p-8 mb-8">
            <div class="flex flex-col md:flex-row items-start md:items-center justify-between gap-6">
                <div class="flex-1">
                    <div class="flex items-center gap-3 mb-4">
                        <span class="px-4 py-2 bg-gradient-to-r {colors['bg']} text-white rounded-full font-bold text-lg">{level}级</span>
                        <span class="text-gray-500">题材深度分析报告</span>
                    </div>
                    <h1 class="text-4xl md:text-5xl font-black text-gray-800 mb-4">{name}</h1>
                    <p class="text-xl text-gray-600 leading-relaxed">{summary}</p>
                    <div class="flex items-center gap-6 mt-6">
                        <div class="text-sm text-gray-500">
                            <i class="fa fa-clock-o mr-2"></i>更新时间：{update_time}
                        </div>
                        <div class="text-sm text-gray-500">
                            <i class="fa fa-star mr-2"></i>综合评分：<span class="font-bold {colors['text']} text-lg">{topic_basic.get('total_score', 0)}分</span>
                        </div>
                    </div>
                </div>
                <div class="flex-shrink-0">
                    <div class="w-32 h-32 rounded-3xl bg-gradient-to-br {colors['bg']} flex items-center justify-center text-white text-6xl shadow-2xl">
                        {topic_basic.get('icon', '📈')}
                    </div>
                </div>
            </div>
            
            <!-- 六维评分 -->
            <div class="mt-8 grid grid-cols-2 md:grid-cols-3 gap-4">
                {dims_html}
            </div>
        </div>

        <!-- 市场规模 -->
        {market_html}

        <!-- 产业链分析 -->
        <section class="mt-12">
            <h2 class="section-title text-3xl font-black text-white mb-8">🏭 产业链全景图</h2>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
                {chain_html}
            </div>
        </section>

        <!-- 核心标的分析 -->
        <section class="mt-12">
            <h2 class="section-title text-3xl font-black text-white mb-8">🎯 核心标的分析</h2>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                {stocks_html}
            </div>
        </section>

        <!-- 催化剂时间线 -->
        <section class="mt-12">
            <h2 class="section-title text-3xl font-black text-white mb-8">⚡ 催化剂时间线</h2>
            <div class="card-glass p-8">
                <div class="max-w-2xl mx-auto">
                    {catalyst_html}
                </div>
            </div>
        </section>

        <!-- 投资策略 -->
        <section class="mt-12">
            <h2 class="section-title text-3xl font-black text-white mb-8">💰 投资策略建议</h2>
            <div class="card-glass p-8">
                {strategy_html}
            </div>
        </section>

        <!-- 风险提示 -->
        <section class="mt-12">
            <h2 class="section-title text-3xl font-black text-white mb-8">⚠️ 核心风险提示</h2>
            <div class="card-glass p-8">
                <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                    {risks_html}
                </div>
            </div>
        </section>

    </main>

    <!-- 返回顶部按钮 -->
    <button onclick="window.scrollTo({{top: 0, behavior: 'smooth'}})" 
            class="fixed bottom-8 right-8 w-14 h-14 bg-white rounded-full shadow-2xl flex items-center justify-center text-purple-600 hover:bg-purple-50 transition-all hover:scale-110">
        <i class="fa fa-arrow-up text-xl"></i>
    </button>

</body>
</html>'''
    
    return page_html


def update_topic_detail_pages(topics_data, details_data):
    """更新所有题材深度分析详情页"""
    print("🔄 生成题材深度分析页面...")
    
    import os
    output_dir = 'docs/题材深度'
    os.makedirs(output_dir, exist_ok=True)
    
    # 合并所有题材
    all_topics = []
    for level_key in ['s_level_topics', 'a_level_topics', 'b_level_topics']:
        all_topics.extend(topics_data.get(level_key, []))
    
    topics_dict = details_data.get('topics', {})
    generated = 0
    
    for topic in all_topics:
        tid = topic.get('id', '')
        if not tid or tid not in topics_dict:
            continue
        
        detail = topics_dict[tid]
        page_html = generate_topic_detail_page(topic, detail)
        
        # 生成文件名
        safe_name = ''.join(c if c.isalnum() or c in '-_' else '_' for c in topic.get('name', ''))
        file_path = f'{output_dir}/{tid}_{safe_name}.html'
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(page_html)
        
        generated += 1
        print(f"   ✅ 已生成：{topic.get('name')} ({file_path})")
    
    print(f"   📊 共生成 {generated} 个题材深度分析页面")
    
    # 生成索引页
    generate_topic_index_page(all_topics, topics_dict, output_dir)
    
    return generated


def generate_topic_index_page(all_topics, topics_dict, output_dir):
    """生成题材深度分析索引页"""
    print("   📑 生成题材深度分析索引页...")
    
    # 按级别分组
    s_topics = [t for t in all_topics if t.get('level') == 'S' and t.get('id') in topics_dict]
    a_topics = [t for t in all_topics if t.get('level') == 'A' and t.get('id') in topics_dict]
    b_topics = [t for t in all_topics if t.get('level') == 'B' and t.get('id') in topics_dict]
    
    def generate_topic_cards(topics):
        cards = ''
        for t in topics:
            tid = t.get('id', '')
            detail = topics_dict.get(tid, {})
            safe_name = ''.join(c if c.isalnum() or c in '-_' else '_' for c in t.get('name', ''))
            file_name = f'{tid}_{safe_name}.html'
            
            level = t.get('level', 'A')
            level_colors = {
                'S': 'from-red-500 to-pink-600',
                'A': 'from-yellow-500 to-orange-500',
                'B': 'from-purple-500 to-indigo-600',
            }
            bg = level_colors.get(level, level_colors['A'])
            
            cards += f'''
                <a href="{file_name}" class="block bg-white rounded-2xl p-6 shadow-lg hover:shadow-xl transition-all hover:-translate-y-1 border border-gray-100">
                    <div class="flex items-center gap-4 mb-4">
                        <div class="w-14 h-14 rounded-2xl bg-gradient-to-br {bg} flex items-center justify-center text-white text-2xl">
                            {t.get('icon', '📈')}
                        </div>
                        <div class="flex-1">
                            <div class="flex items-center gap-2">
                                <h3 class="text-xl font-bold text-gray-800">{t.get('name', '')}</h3>
                                <span class="px-2 py-1 bg-gradient-to-r {bg} text-white text-xs font-bold rounded-full">{level}级</span>
                            </div>
                            <p class="text-gray-500 text-sm mt-1 line-clamp-2">{detail.get('summary', t.get('core_logic', ''))}</p>
                        </div>
                    </div>
                    <div class="flex items-center justify-between text-sm">
                        <span class="text-gray-500">
                            <i class="fa fa-star text-yellow-400 mr-1"></i>
                            综合评分 {t.get('total_score', 0)}分
                        </span>
                        <span class="text-purple-600 font-semibold">
                            查看详情 <i class="fa fa-arrow-right ml-1"></i>
                        </span>
                    </div>
                </a>
            '''
        return cards
    
    s_section = ''
    if s_topics:
        s_section = f'''
        <section class="mb-12">
            <h2 class="text-2xl font-bold text-white mb-6 flex items-center gap-3">
                <span class="px-4 py-2 bg-gradient-to-r from-red-500 to-pink-600 rounded-full text-white font-bold">S</span>
                最强主线题材
            </h2>
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                {generate_topic_cards(s_topics)}
            </div>
        </section>
        '''
    
    a_section = ''
    if a_topics:
        a_section = f'''
        <section class="mb-12">
            <h2 class="text-2xl font-bold text-white mb-6 flex items-center gap-3">
                <span class="px-4 py-2 bg-gradient-to-r from-yellow-500 to-orange-500 rounded-full text-white font-bold">A</span>
                重要支线题材
            </h2>
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                {generate_topic_cards(a_topics)}
            </div>
        </section>
        '''
    
    b_section = ''
    if b_topics:
        b_section = f'''
        <section class="mb-12">
            <h2 class="text-2xl font-bold text-white mb-6 flex items-center gap-3">
                <span class="px-4 py-2 bg-gradient-to-r from-purple-500 to-indigo-600 rounded-full text-white font-bold">B</span>
                观察类题材
            </h2>
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                {generate_topic_cards(b_topics)}
            </div>
        </section>
        '''
    
    index_html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>题材深度分析 - 智能选题助手</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://cdn.jsdelivr.net/npm/font-awesome@4.7.0/css/font-awesome.min.css" rel="stylesheet">
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@300;400;500;700;900&display=swap');
        * {{ font-family: 'Noto Sans SC', sans-serif; }}
        body {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
        }}
        .glass-nav {{
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(20px);
            border-bottom: 1px solid rgba(255, 255, 255, 0.2);
        }}
        /* 移动端菜单样式 */
        .hamburger-btn {{
            display: none;
            background: rgba(255,255,255,0.2);
            border: none;
            color: white;
            width: 44px;
            height: 44px;
            border-radius: 8px;
            cursor: pointer;
            font-size: 20px;
            z-index: 99999;
        }}
        .mobile-menu {{
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            z-index: 99998;
            display: none;
            padding-top: 80px;
            overflow-y: auto;
        }}
        .mobile-menu.show {{
            display: block;
        }}
        .mobile-menu-item {{
            display: block;
            padding: 16px 24px;
            color: white;
            text-decoration: none;
            font-size: 18px;
            border-bottom: 1px solid rgba(255,255,255,0.1);
            transition: background 0.2s;
        }}
        .mobile-menu-item:hover {{
            background: rgba(255,255,255,0.1);
        }}
        .close-menu-btn {{
            position: absolute;
            top: 20px;
            right: 20px;
            background: rgba(255,255,255,0.2);
            border: none;
            color: white;
            width: 44px;
            height: 44px;
            border-radius: 8px;
            cursor: pointer;
            font-size: 24px;
        }}
        @media (max-width: 768px) {{
            .hamburger-btn {{
                display: block;
            }}
            .nav-links {{
                display: none !important;
            }}
        }}
    </style>
</head>
<body class="pb-16">
    <!-- 导航栏 -->
    <nav class="fixed top-0 left-0 right-0 z-50 glass-nav">
        <div class="max-w-5xl mx-auto px-4 py-3 flex items-center justify-between">
            <div class="flex items-center space-x-3">
                <div class="w-8 h-8 rounded-lg bg-gradient-to-br from-indigo-500 to-purple-600 flex items-center justify-center">
                    <span class="text-white text-sm font-bold">📊</span>
                </div>
                <span class="text-white font-bold text-lg">投资研究中心</span>
            </div>
            <div class="nav-links flex items-center space-x-1 flex-wrap gap-1">
                <a href="../index.html" class="text-white/80 hover:text-white hover:bg-white/10 text-sm transition-colors px-3 py-1.5 rounded-lg">首页</a>
                <a href="../daily/latest.html" class="text-white/80 hover:text-white hover:bg-white/10 text-sm transition-colors px-3 py-1.5 rounded-lg">日报</a>
                <a href="../intraday/latest.html" class="text-white/80 hover:text-white hover:bg-white/10 text-sm transition-colors px-3 py-1.5 rounded-lg">盘中</a>
                <a href="../aftermarket/latest.html" class="text-white/80 hover:text-white hover:bg-white/10 text-sm transition-colors px-3 py-1.5 rounded-lg">盘后</a>
                <a href="../industry_chain/latest.html" class="text-white/80 hover:text-white hover:bg-white/10 text-sm transition-colors px-3 py-1.5 rounded-lg">产业链</a>
                <a href="../weekly_review/latest.html" class="text-white/80 hover:text-white hover:bg-white/10 text-sm transition-colors px-3 py-1.5 rounded-lg">周复盘</a>
                <a href="../weekly_outlook/latest.html" class="text-white/80 hover:text-white hover:bg-white/10 text-sm transition-colors px-3 py-1.5 rounded-lg">周三前瞻</a>
                <a href="../周末速递/latest.html" class="text-white/80 hover:text-white hover:bg-white/10 text-sm transition-colors px-3 py-1.5 rounded-lg">周末速递</a>
                <a href="../明日催化剂/latest.html" class="text-white/80 hover:text-white hover:bg-white/10 text-sm transition-colors px-3 py-1.5 rounded-lg">明日催化</a>
                <a href="../s级催化扫描/latest.html" class="text-white/80 hover:text-white hover:bg-white/10 text-sm transition-colors px-3 py-1.5 rounded-lg">S级催化</a>
                <a href="../数据时光机/index.html" class="text-white/80 hover:text-white hover:bg-white/10 text-sm transition-colors px-3 py-1.5 rounded-lg">时光机</a>
                <a href="../monthly/latest.html" class="text-white/80 hover:text-white hover:bg-white/10 text-sm transition-colors px-3 py-1.5 rounded-lg">月报</a>
            </div>
            <button class="hamburger-btn" onclick="toggleMobileMenu()">☰</button>
            </div>
    </nav>
    
    <!-- 移动端全屏菜单 -->
    <div id="mobileMenu" class="mobile-menu">
        <button class="close-menu-btn" onclick="toggleMobileMenu()">✕</button>
        <a href="../index.html" class="mobile-menu-item" onclick="toggleMobileMenu()">🏠 首页</a>
        <a href="../daily/latest.html" class="mobile-menu-item" onclick="toggleMobileMenu()">📰 日报</a>
        <a href="../intraday/latest.html" class="mobile-menu-item" onclick="toggleMobileMenu()">📈 盘中快报</a>
        <a href="../aftermarket/latest.html" class="mobile-menu-item" onclick="toggleMobileMenu()">📉 盘后速递</a>
        <a href="../industry_chain/latest.html" class="mobile-menu-item" onclick="toggleMobileMenu()">🔗 产业链总览</a>
        <a href="../weekly_review/latest.html" class="mobile-menu-item" onclick="toggleMobileMenu()">📋 周复盘</a>
        <a href="../weekly_outlook/latest.html" class="mobile-menu-item" onclick="toggleMobileMenu()">🔮 周三前瞻</a>
        <a href="../周末速递/latest.html" class="mobile-menu-item" onclick="toggleMobileMenu()">📦 周末速递</a>
        <a href="../明日催化剂/latest.html" class="mobile-menu-item" onclick="toggleMobileMenu()">⏰ 明日催化剂</a>
        <a href="../s级催化扫描/latest.html" class="mobile-menu-item" onclick="toggleMobileMenu()">⭐ S级催化扫描</a>
        <a href="../数据时光机/index.html" class="mobile-menu-item" onclick="toggleMobileMenu()">⏳ 数据时光机</a>
        <a href="../monthly/latest.html" class="mobile-menu-item" onclick="toggleMobileMenu()">🗓️ 月度总结</a>
    </div>
    
    <script>
        function toggleMobileMenu() {{
            document.getElementById('mobileMenu').classList.toggle('show');
            document.body.style.overflow = document.getElementById('mobileMenu').classList.contains('show') ? 'hidden' : '';
        }}
    </script>

    <main class="max-w-7xl mx-auto px-4 pt-24 pb-12">
        <div class="text-center mb-12">
            <h1 class="text-5xl font-black text-white mb-4">📚 题材深度分析库</h1>
            <p class="text-xl text-white/80">深入解析每个题材的产业链、核心标的、催化剂与投资策略</p>
        </div>

        {s_section}
        {a_section}
        {b_section}

    </main>
</body>
</html>'''
    
    with open(f'{output_dir}/index.html', 'w', encoding='utf-8') as f:
        f.write(index_html)
    
    print(f"   ✅ 索引页已生成：{output_dir}/index.html")


def validate_data():
    """
    校验所有数据文件的完整性
    - 检查ID唯一性
    - 检查必要字段
    - 返回错误列表
    """
    errors = []
    warnings = []
    
    print("\n🔍 [数据校验]")
    
    # 1. 校验持仓数据
    try:
        portfolio_data = load_portfolio_data()
        stock_ids = set()
        for stock in portfolio_data.get('stocks', []):
            sid = stock.get('id')
            name = stock.get('name', '未知')
            if not sid:
                errors.append(f"持仓股 {name} 缺少ID")
            elif sid in stock_ids:
                errors.append(f"持仓股 {name} ID重复: {sid}")
            else:
                stock_ids.add(sid)
            
            # 检查必要字段
            required_fields = ['name', 'cost_price', 'current_price']
            for field in required_fields:
                if field not in stock:
                    errors.append(f"持仓股 {name} 缺少必要字段: {field}")
        print(f"   ✅ 持仓数据校验通过（{len(stock_ids)}只股票）")
    except Exception as e:
        errors.append(f"持仓数据加载失败: {e}")
    
    # 2. 校验题材数据
    try:
        topics_data = load_topics_data()
        topic_ids = set()
        all_topics = []
        for level in ['s', 'a', 'b']:
            key = f'{level}_level_topics'
            all_topics.extend(topics_data.get(key, []))
        
        for topic in all_topics:
            tid = topic.get('id')
            name = topic.get('name', '未知')
            if not tid:
                errors.append(f"题材 {name} 缺少ID")
            elif tid in topic_ids:
                errors.append(f"题材 {name} ID重复: {tid}")
            else:
                topic_ids.add(tid)
        print(f"   ✅ 题材数据校验通过（{len(topic_ids)}个题材）")
    except Exception as e:
        errors.append(f"题材数据加载失败: {e}")
    
    # 3. 校验产业链数据
    try:
        chain_data = load_industry_chain_data()
        chain_ids = set()
        chains = chain_data.get('core_chains', []) if isinstance(chain_data, dict) else []
        for chain in chains:
            cid = chain.get('id')
            name = chain.get('name', '未知')
            if not cid:
                warnings.append(f"产业链 {name} 缺少ID")
            elif cid in chain_ids:
                errors.append(f"产业链 {name} ID重复: {cid}")
            else:
                chain_ids.add(cid)
        print(f"   ✅ 产业链数据校验通过（{len(chain_ids)}条产业链）")
    except Exception as e:
        errors.append(f"产业链数据加载失败: {e}")
    
    # 4. 校验预判数据
    try:
        pred_data = load_predictions_data()
        pred_ids = set()
        # 待验证预判 + 历史记录
        predictions = []
        if isinstance(pred_data, dict):
            predictions.extend(pred_data.get('pending_predictions', []))
            predictions.extend(pred_data.get('history_records', []))
        elif isinstance(pred_data, list):
            predictions = pred_data
        
        for pred in predictions:
            pid = pred.get('id')
            title = pred.get('title', '未知')
            if not pid:
                warnings.append(f"预判 {title} 缺少ID")
            elif pid in pred_ids:
                errors.append(f"预判 {title} ID重复: {pid}")
            else:
                pred_ids.add(pid)
        print(f"   ✅ 预判数据校验通过（{len(pred_ids)}条预判）")
    except Exception as e:
        errors.append(f"预判数据加载失败: {e}")
    
    # 5. 校验市场数据
    try:
        market_data = load_market_data()
        index_names = set()
        for idx in market_data.get('indices', []):
            name = idx.get('name', '未知')
            if name in index_names:
                warnings.append(f"大盘指数 {name} 名称重复")
            else:
                index_names.add(name)
        print(f"   ✅ 市场数据校验通过（{len(index_names)}个指数）")
    except Exception as e:
        errors.append(f"市场数据加载失败: {e}")
    
    # 输出结果
    if errors:
        print(f"\n   ❌ 发现 {len(errors)} 个错误:")
        for e in errors:
            print(f"      - {e}")
    
    if warnings:
        print(f"\n   ⚠️  发现 {len(warnings)} 个警告:")
        for w in warnings:
            print(f"      - {w}")
    
    if not errors and not warnings:
        print("   ✅ 全部数据校验通过，无错误无警告")
    
    return len(errors) == 0


# ========== 市场数据模块 ==========

def load_market_data():
    """加载市场数据"""
    with open('data/market.json', 'r', encoding='utf-8') as f:
        return json.load(f)


def archive_market_snapshot(data):
    """归档当日市场数据快照（时光机功能）"""
    today = datetime.now().strftime('%Y-%m-%d')
    history_dir = 'data/history/market'
    os.makedirs(history_dir, exist_ok=True)
    
    archive_path = f'{history_dir}/{today}.json'
    with open(archive_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"  ✅ 市场数据已归档到 {archive_path}")


# ========== 主函数 ==========

def main():
    print("=" * 60)
    print("📊 统一数据层更新系统 V2.1")
    print("=" * 60)
    
    # ========== 数据校验 ==========
    is_valid = validate_data()
    if not is_valid:
        print("\n❌ 数据校验失败，请修复错误后再运行！")
        return
    
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

    
    # ========== 题材深度分析模块 ==========
    print("\n📁 [题材深度分析模块]")
    topic_details_data = load_topic_details_data()
    print(f"   数据源：data/topic_details.json")
    detail_count = update_topic_detail_pages(topics_data, topic_details_data)
    print(f"   ✅ 已生成 {detail_count} 个题材深度分析页面")
    
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
    
    # ========== 市场数据模块 ==========
    print("\n📁 [市场数据模块]")
    market_data = load_market_data()
    print(f"   数据源：data/market.json")
    print(f"   大盘指数：{len(market_data['indices'])}个")
    print(f"   热门板块：{len(market_data.get('sectors_hot', []))}个")
    archive_market_snapshot(market_data)
    print("   ✅ 市场数据加载并归档完成")
    
    # 更新首页市场概览
    import subprocess
    import os
    script_dir = os.path.dirname(os.path.abspath(__file__))
    update_script = os.path.join(script_dir, 'scripts', 'update_home_market.py')
    subprocess.run(['python3', update_script], cwd=script_dir, capture_output=True)
    
    # ========== 时光机模块 ==========
    print("\n📁 [时光机模块]")
    from v3.generators.time_machine import TimeMachineGenerator
    tm_generator = TimeMachineGenerator()
    tm_generator.generate()
    dates_count = len(tm_generator.get_available_dates())
    print(f"   ✅ 时光机页面已更新（{dates_count}个历史快照）")

    # ========== 图表数据绑定 ==========
    print("\n📈 [图表数据绑定]")
    try:
        import subprocess
        from pathlib import Path
        result = subprocess.run(
            ['python3', 'scripts/bind_chart_data.py'],
            capture_output=True,
            text=True,
            cwd=str(Path(__file__).resolve().parent)
        )
        if result.returncode == 0:
            print("   ✅ 图表数据绑定完成")
        else:
            print(f"   ⚠️  图表绑定异常")
    except Exception as e:
        print(f"   ⚠️  图表绑定跳过: {e}")
    
    
    # ========== 数据质量检查 ==========
    print("\n📊 [数据质量检查]")
    try:
        import subprocess
        from pathlib import Path
        result = subprocess.run(
            ["python3", "scripts/data_quality_monitor.py"],
            capture_output=True,
            text=True,
            cwd=str(Path(__file__).resolve().parent)
        )
        if result.returncode == 0:
            # 提取评分行
            for line in result.stdout.split("\n"):
                if "综合评分" in line:
                    print(f"   {line.strip()}")
                    break
            print("   ✅ 数据质量检查通过")
        else:
            print(f"   ⚠️  数据质量存在问题，请检查")
    except Exception as e:
        print(f"   ⚠️  质量检查跳过: {e}")
    
    print("\n" + "=" * 60)
    print("✅ 所有页面数据更新完成！")
    print("=" * 60)
    
    # ========== 数据校验模块 ==========

def validate_data():
    """
    校验所有数据文件的完整性
    - 检查ID唯一性
    - 检查必要字段
    - 返回错误列表
    """
    errors = []
    warnings = []
    
    print("\n🔍 [数据校验]")
    
    # 1. 校验持仓数据
    try:
        portfolio_data = load_portfolio_data()
        stock_ids = set()
        for stock in portfolio_data.get('stocks', []):
            sid = stock.get('id')
            name = stock.get('name', '未知')
            if not sid:
                errors.append(f"持仓股 {name} 缺少ID")
            elif sid in stock_ids:
                errors.append(f"持仓股 {name} ID重复: {sid}")
            else:
                stock_ids.add(sid)
            
            # 检查必要字段
            required_fields = ['name', 'cost_price', 'current_price']
            for field in required_fields:
                if field not in stock:
                    errors.append(f"持仓股 {name} 缺少必要字段: {field}")
        print(f"   ✅ 持仓数据校验通过（{len(stock_ids)}只股票）")
    except Exception as e:
        errors.append(f"持仓数据加载失败: {e}")
    
    # 2. 校验题材数据
    try:
        topics_data = load_topics_data()
        topic_ids = set()
        all_topics = []
        for level in ['s', 'a', 'b']:
            key = f'{level}_level_topics'
            all_topics.extend(topics_data.get(key, []))
        
        for topic in all_topics:
            tid = topic.get('id')
            name = topic.get('name', '未知')
            if not tid:
                errors.append(f"题材 {name} 缺少ID")
            elif tid in topic_ids:
                errors.append(f"题材 {name} ID重复: {tid}")
            else:
                topic_ids.add(tid)
        print(f"   ✅ 题材数据校验通过（{len(topic_ids)}个题材）")
    except Exception as e:
        errors.append(f"题材数据加载失败: {e}")
    
    # 3. 校验产业链数据
    try:
        chain_data = load_industry_chain_data()
        chain_ids = set()
        chains = chain_data.get('core_chains', []) if isinstance(chain_data, dict) else []
        for chain in chains:
            cid = chain.get('id')
            name = chain.get('name', '未知')
            if not cid:
                warnings.append(f"产业链 {name} 缺少ID")
            elif cid in chain_ids:
                errors.append(f"产业链 {name} ID重复: {cid}")
            else:
                chain_ids.add(cid)
        print(f"   ✅ 产业链数据校验通过（{len(chain_ids)}条产业链）")
    except Exception as e:
        errors.append(f"产业链数据加载失败: {e}")
    
    # 4. 校验预判数据
    try:
        pred_data = load_predictions_data()
        pred_ids = set()
        # 待验证预判 + 历史记录
        predictions = []
        if isinstance(pred_data, dict):
            predictions.extend(pred_data.get('pending_predictions', []))
            predictions.extend(pred_data.get('history_records', []))
        elif isinstance(pred_data, list):
            predictions = pred_data
        
        for pred in predictions:
            pid = pred.get('id')
            title = pred.get('title', '未知')
            if not pid:
                warnings.append(f"预判 {title} 缺少ID")
            elif pid in pred_ids:
                errors.append(f"预判 {title} ID重复: {pid}")
            else:
                pred_ids.add(pid)
        print(f"   ✅ 预判数据校验通过（{len(pred_ids)}条预判）")
    except Exception as e:
        errors.append(f"预判数据加载失败: {e}")
    
    # 5. 校验市场数据
    try:
        market_data = load_market_data()
        index_names = set()
        for idx in market_data.get('indices', []):
            name = idx.get('name', '未知')
            if name in index_names:
                warnings.append(f"大盘指数 {name} 名称重复")
            else:
                index_names.add(name)
        print(f"   ✅ 市场数据校验通过（{len(index_names)}个指数）")
    except Exception as e:
        errors.append(f"市场数据加载失败: {e}")
    
    # 输出结果
    if errors:
        print(f"\n   ❌ 发现 {len(errors)} 个错误:")
        for e in errors:
            print(f"      - {e}")
    
    if warnings:
        print(f"\n   ⚠️  发现 {len(warnings)} 个警告:")
        for w in warnings:
            print(f"      - {w}")
    
    if not errors and not warnings:
        print("   ✅ 全部数据校验通过，无错误无警告")
    
    return len(errors) == 0


if __name__ == '__main__':
    main()
