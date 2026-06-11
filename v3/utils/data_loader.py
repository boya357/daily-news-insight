"""
统一数据加载器
从统一数据层（data/*.json）加载数据，转换为各生成器需要的格式
保证所有报告和工具页面使用同源数据，杜绝不一致
"""

import json
import os
from pathlib import Path


def get_data_dir():
    """获取数据目录的绝对路径"""
    # 当前文件在 v3/utils/，数据在 ../../data/
    current_dir = Path(__file__).resolve().parent
    data_dir = current_dir.parent.parent / "data"
    return data_dir


def load_portfolio():
    """加载完整的持仓数据"""
    data_path = get_data_dir() / "portfolio.json"
    with open(data_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def get_holdings_for_daily(include_comments=True):
    """
    获取日报格式的持仓列表
    
    Returns:
        list: [{name, code, price, change, up, comment, ratio}, ...]
    """
    data = load_portfolio()
    stocks = data['stocks']
    portfolio = data['portfolio']
    
    holdings = []
    # 计算总仓位分配（根据持仓数量平均分配，或者从JSON读取）
    # 目前JSON中没有单只仓位占比，使用默认分配
    default_ratios = {
        "英维克": 30,
        "铜冠铜箔": 30,
        "雅克科技": 25,
        "*ST建艺": 15
    }
    
    for stock in stocks:
        name = stock['name']
        code = stock['id']
        price = f"{stock['current_price']:.2f}"
        
        # 涨跌幅
        change_pct = stock.get('today_change', 0)
        if change_pct >= 0:
            change = f"+{change_pct*100:.2f}%"
            up = True
        else:
            change = f"{change_pct*100:.2f}%"
            up = False
        
        # 评论/描述
        if include_comments:
            # 使用advice中的文本作为评论
            comment = stock.get('advice', {}).get('text', '')
            if not comment:
                # 拼接诊断信息
                diagnosis = stock.get('diagnosis', {})
                parts = []
                for key in ['technical', 'fund', 'industry']:
                    if key in diagnosis:
                        d = diagnosis[key]
                        parts.append(f"{d['title']}{d['value']}（{d['desc']}）")
                comment = "；".join(parts)
        else:
            comment = ""
        
        # 仓位占比
        ratio = default_ratios.get(name, 25)
        
        holdings.append({
            "name": name,
            "code": code,
            "price": price,
            "change": change,
            "up": up,
            "comment": comment,
            "ratio": ratio
        })
    
    return holdings


def get_position_info():
    """
    获取仓位信息
    
    Returns:
        dict: {total, cash, risk_level}
    """
    data = load_portfolio()
    portfolio = data['portfolio']
    health_score = portfolio.get('health_score', 60)
    
    # 根据健康分判断风险等级
    if health_score >= 80:
        risk_level = "低"
    elif health_score >= 60:
        risk_level = "中"
    elif health_score >= 40:
        risk_level = "中高"
    else:
        risk_level = "高"
    
    return {
        "total": 100,  # 假设满仓
        "cash": 0,
        "risk_level": risk_level
    }


def get_holdings_for_intraday(include_comments=True):
    """
    获取盘中快报格式的持仓列表（与日报格式相同，只是没有position_info）
    
    Returns:
        list: [{name, code, price, change, up, comment}, ...]
    """
    holdings = get_holdings_for_daily(include_comments=include_comments)
    # 移除ratio字段，因为盘中快报不需要
    for h in holdings:
        h.pop('ratio', None)
    return holdings


def get_portfolio_overview():
    """获取组合概览信息"""
    data = load_portfolio()
    return data['portfolio']


def get_longhubang_data():
    """获取龙虎榜数据"""
    data = load_portfolio()
    return data.get('longhubang', {})


if __name__ == "__main__":
    # 测试
    print("=== 测试日报持仓数据 ===")
    holdings = get_holdings_for_daily()
    for h in holdings:
        print(f"{h['name']} ({h['code']}): {h['price']} {h['change']}")
    
    print("\n=== 测试仓位信息 ===")
    pos = get_position_info()
    print(pos)


def get_holdings_for_weekly_review():
    """
    获取周复盘格式的持仓列表
    
    Returns:
        list: [{name, code, price, weekly_change, change_type, up, comment}, ...]
    """
    holdings = get_holdings_for_daily(include_comments=True)
    result = []
    
    for h in holdings:
        # 周涨跌幅暂时用今日涨跌幅代替，后续接入行情数据后完善
        weekly_change = h['change']
        change_type = '涨' if h['up'] else '跌'
        
        result.append({
            'name': h['name'],
            'code': h['code'],
            'price': h['price'],
            'weekly_change': weekly_change,
            'change_type': change_type,
            'up': h['up'],
            'comment': h['comment']
        })
    
    return result


def load_market_data():
    """加载完整的市场数据"""
    data_path = get_data_dir() / "market.json"
    with open(data_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def get_indices_for_daily():
    """
    获取日报格式的大盘指数数据
    
    Returns:
        list: [{name, code, price, change, change_pct_str, up}, ...]
    """
    data = load_market_data()
    indices = data['indices']
    result = []
    
    for idx in indices:
        change_pct = idx['change_pct']
        if change_pct >= 0:
            change_pct_str = f"+{change_pct*100:.2f}%"
            up = True
        else:
            change_pct_str = f"{change_pct*100:.2f}%"
            up = False
        
        result.append({
            'name': idx['name'],
            'code': idx['code'],
            'price': f"{idx['price']:.2f}",
            'change': f"{'+' if up else ''}{idx['change']:.2f}",
            'change_pct_str': change_pct_str,
            'up': up
        })
    
    return result


def get_market_summary():
    """获取市场概览数据"""
    data = load_market_data()
    return data['market_data']


def get_hot_sectors(limit=5):
    """获取热门板块"""
    data = load_market_data()
    sectors = data.get('sectors_hot', [])
    result = []
    
    for s in sectors[:limit]:
        change_pct = s['change_pct']
        result.append({
            'name': s['name'],
            'change_pct': f"{'+' if change_pct >= 0 else ''}{change_pct*100:.2f}%",
            'up': change_pct >= 0,
            'leader': s.get('leader', ''),
            'fund_flow': s.get('fund_flow', '')
        })
    
    return result


def get_cold_sectors(limit=3):
    """获取跌幅居前板块"""
    data = load_market_data()
    sectors = data.get('sectors_cold', [])
    result = []
    
    for s in sectors[:limit]:
        change_pct = s['change_pct']
        result.append({
            'name': s['name'],
            'change_pct': f"{'+' if change_pct >= 0 else ''}{change_pct*100:.2f}%",
            'up': change_pct >= 0,
            'leader': s.get('leader', ''),
            'fund_flow': s.get('fund_flow', '')
        })
    
    return result


def get_market_sentiment():
    """获取市场情绪数据"""
    data = load_market_data()
    return data.get('sentiment', {})


def load_topics_data():
    """加载完整的题材数据"""
    data_path = get_data_dir() / "topics.json"
    with open(data_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def get_topics_by_level(level='S'):
    """
    获取指定级别的题材列表
    
    Args:
        level: 'S', 'A', 'B'
    """
    data = load_topics_data()
    key = f'{level.lower()}_level_topics'
    return data.get(key, [])


def get_all_topics():
    """获取所有级别的题材"""
    data = load_topics_data()
    all_topics = []
    for level in ['s', 'a', 'b']:
        key = f'{level}_level_topics'
        all_topics.extend(data.get(key, []))
    return all_topics


def get_hot_topics_for_daily(limit=5):
    """
    获取日报用的热门题材列表
    
    Returns:
        list: [{name, level, score, leader, core_logic, change, up}, ...]
    """
    topics = get_all_topics()
    # 按总分排序
    sorted_topics = sorted(topics, key=lambda x: x.get('total_score', 0), reverse=True)
    
    result = []
    for t in sorted_topics[:limit]:
        result.append({
            'name': t['name'],
            'level': t.get('level', 'A'),
            'score': t.get('total_score', 0),
            'leader': t.get('leader_stock', ''),
            'core_logic': t.get('core_logic', ''),
            'health_score': t.get('health_score', 0),
            'icon': t.get('icon', ''),
            'color': t.get('color', 'blue')
        })
    
    return result


def get_catalyst_calendar(days=7):
    """
    获取催化日历数据
    
    Args:
        days: 获取未来N天的催化事件
        
    Returns:
        list: [{date, title, description, impact, related_topics}, ...]
    """
    data = load_topics_data()
    catalysts = data.get('catalyst_calendar', [])
    
    from datetime import datetime, date
    today = date.today()
    
    result = []
    for c in catalysts:
        try:
            cat_date = datetime.strptime(c['date'], '%Y-%m-%d').date()
            days_diff = (cat_date - today).days
            if 0 <= days_diff <= days:
                # 统一字段名：优先用title，没有就用event
                title = c.get('title') or c.get('event', '')
                # 描述用impact
                description = c.get('impact', '')
                result.append({
                    'date': c['date'],
                    'title': title,
                    'description': description,
                    'impact': c.get('impact', ''),
                    'related_topics': c.get('related_topics', [])
                })
        except:
            continue
    
    # 按日期排序
    result.sort(key=lambda x: x['date'])
    return result

def get_allocation_strategy():
    """获取配置策略建议"""
    data = load_topics_data()
    return data.get('allocation_strategy', {})


# ==================== 首页专用数据格式 ====================

def get_index_s_level_chains():
    """
    获取首页核心S级产业链卡片数据
    
    Returns:
        list: [{id, name, icon, level, description, link, tags}, ...]
    """
    topics = get_topics_by_level('S')
    result = []
    for t in topics:
        result.append({
            'id': t.get('id', ''),
            'name': t.get('name', ''),
            'icon': t.get('icon', '📊'),
            'level': t.get('level', 'S'),
            'description': t.get('description', ''),
            'link': t.get('link', '#'),
            'tags': t.get('tags', [])
        })
    return result


def get_index_holdings_overview():
    """
    获取首页持仓概览数据
    
    Returns:
        list: [{name, code, cost_price, current_price, change_pct, status, status_color, bg_color, border_color}, ...]
    """
    data = load_portfolio()
    stocks = data['stocks']
    
    holdings = []
    for stock in stocks:
        name = stock['name']
        code = stock.get('id', '')
        cost_price = stock.get('cost_price', 0)
        current_price = stock.get('current_price', 0)
        today_change = stock.get('today_change', 0)
        
        # 计算涨跌幅
        change_pct = (current_price - cost_price) / cost_price * 100
        
        # 状态判断
        risk_level = stock.get('risk_level', 'medium')
        if risk_level == 'high':
            status = '🔴 止损'
            status_color = 'text-red-500'
            bg_color = 'bg-red-50'
            border_color = 'border-red-100'
        elif risk_level == 'warning':
            status = '🟡 警告'
            status_color = 'text-yellow-600'
            bg_color = 'bg-yellow-50'
            border_color = 'border-yellow-100'
        elif change_pct > 20:
            status = '🟢 盈利'
            status_color = 'text-green-600'
            bg_color = 'bg-green-50'
            border_color = 'border-green-100'
        else:
            status = '🟢 持有'
            status_color = 'text-green-600'
            bg_color = 'bg-gray-50'
            border_color = 'border-gray-100'
        
        holdings.append({
            'name': name,
            'code': code,
            'cost_price': cost_price,
            'current_price': current_price,
            'change_pct': change_pct,
            'today_change': today_change,
            'status': status,
            'status_color': status_color,
            'bg_color': bg_color,
            'border_color': border_color
        })
    
    return holdings


def get_index_catalysts(limit=5):
    """
    获取首页近期重点催化数据
    
    Returns:
        list: [{date, title, description, status, status_label}, ...]
    """
    catalysts = get_catalyst_calendar(14)
    result = []
    
    from datetime import datetime, date
    today = date.today()
    
    for c in catalysts[:limit]:
        catalyst_date = c.get('date', '')
        title = c.get('title', '')
        description = c.get('description', '')
        
        # 计算状态
        try:
            cat_date = datetime.strptime(catalyst_date, '%Y-%m-%d').date()
            days_diff = (cat_date - today).days
            
            if days_diff < 0:
                status = '已结束'
                status_label = '已结束'
                status_class = 'bg-gray-200 text-gray-600'
            elif days_diff == 0:
                status = '今天'
                status_label = '今天'
                status_class = 'bg-orange-100 text-orange-600'
            elif days_diff == 1:
                status = '明天'
                status_label = '明天'
                status_class = 'bg-yellow-100 text-yellow-600'
            elif days_diff <= 7:
                status = f'{days_diff}天后'
                status_label = f'{days_diff}天后'
                status_class = 'bg-blue-100 text-blue-600'
            else:
                status = '即将到来'
                status_label = '即将'
                status_class = 'bg-gray-100 text-gray-600'
        except:
            status = ''
            status_label = ''
            status_class = 'bg-gray-100 text-gray-600'
        
        result.append({
            'date': catalyst_date,
            'title': title,
            'description': description,
            'status': status,
            'status_label': status_label,
            'status_class': status_class
        })
    
    return result

