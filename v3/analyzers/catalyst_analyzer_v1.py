"""
催化事件推演引擎
- 事件影响分析
- 情绪周期判断
- 买卖点量化评估
- 历史事件回测
"""

import json
from pathlib import Path
from datetime import datetime, timedelta
from typing import List, Dict, Optional

BASE_DIR = Path(__file__).resolve().parent.parent.parent
DATA_DIR = BASE_DIR / 'data'


class CatalystEvent:
    """催化事件"""
    
    def __init__(self, event_data):
        self.title = event_data.get('title', '')
        self.date = event_data.get('date', '')
        self.type = event_data.get('type', '')  # 政策/业绩/行业/公司/宏观
        self.impact_level = event_data.get('impact_level', 'medium')  # high/medium/low
        self.description = event_data.get('description', '')
        self.related_topics = event_data.get('related_topics', [])
        self.related_stocks = event_data.get('related_stocks', [])
    
    def calculate_impact_score(self) -> float:
        """计算事件影响分值"""
        type_weights = {
            '政策': 0.9,
            '行业': 0.7,
            '业绩': 0.8,
            '公司': 0.6,
            '宏观': 0.5,
        }
        
        level_weights = {
            'high': 1.0,
            'medium': 0.6,
            'low': 0.3,
        }
        
        type_weight = type_weights.get(self.type, 0.5)
        level_weight = level_weights.get(self.impact_level, 0.5)
        
        return type_weight * level_weight * 100


class CatalystAnalyzer:
    """催化事件分析器"""
    
    def __init__(self, events: List[Dict]):
        self.events = [CatalystEvent(e) for e in events]
    
    def analyze_upcoming_events(self, days_ahead: int = 30) -> List[Dict]:
        """分析即将到来的催化事件"""
        today = datetime.now().date()
        upcoming = []
        
        for event in self.events:
            try:
                event_date = datetime.strptime(event.date, '%Y-%m-%d').date()
                days_until = (event_date - today).days
                
                if 0 <= days_until <= days_ahead:
                    impact_score = event.calculate_impact_score()
                    
                    # 判断事件阶段
                    if days_until <= 3:
                        stage = '临近爆发'
                        stage_color = 'red'
                    elif days_until <= 7:
                        stage = '布局窗口'
                        stage_color = 'orange'
                    elif days_until <= 14:
                        stage = '关注期'
                        stage_color = 'yellow'
                    else:
                        stage = '观察期'
                        stage_color = 'blue'
                    
                    upcoming.append({
                        'title': event.title,
                        'date': event.date,
                        'days_until': days_until,
                        'type': event.type,
                        'impact_level': event.impact_level,
                        'impact_score': round(impact_score, 1),
                        'stage': stage,
                        'stage_color': stage_color,
                        'description': event.description,
                        'related_topics': event.related_topics,
                        'related_stocks': event.related_stocks,
                    })
            except:
                continue
        
        # 按日期排序
        upcoming.sort(key=lambda x: x['days_until'])
        
        return upcoming
    
    def analyze_sentiment_cycle(self) -> Dict:
        """分析当前情绪周期"""
        today = datetime.now().date()
        
        # 统计不同时间窗口的事件数量和强度
        windows = [
            {'name': '过去7天', 'start': -7, 'end': 0},
            {'name': '未来7天', 'start': 0, 'end': 7},
            {'name': '未来8-14天', 'start': 7, 'end': 14},
            {'name': '未来15-30天', 'start': 14, 'end': 30},
        ]
        
        window_stats = []
        for w in windows:
            events_in_window = []
            total_impact = 0
            
            for event in self.events:
                try:
                    event_date = datetime.strptime(event.date, '%Y-%m-%d').date()
                    days_diff = (event_date - today).days
                    
                    if w['start'] <= days_diff < w['end']:
                        events_in_window.append(event)
                        total_impact += event.calculate_impact_score()
                except:
                    continue
            
            window_stats.append({
                'window': w['name'],
                'event_count': len(events_in_window),
                'total_impact': round(total_impact, 1),
                'avg_impact': round(total_impact / max(len(events_in_window), 1), 1),
            })
        
        # 判断情绪周期阶段
        future_7d = window_stats[1] if len(window_stats) > 1 else {'total_impact': 0}
        future_14d = window_stats[2] if len(window_stats) > 2 else {'total_impact': 0}
        past_7d = window_stats[0] if len(window_stats) > 0 else {'total_impact': 0}
        
        # 简单的情绪周期判断
        if future_7d['total_impact'] > past_7d['total_impact'] * 1.5:
            cycle = '情绪升温期'
            suggestion = '可积极布局相关题材'
            cycle_color = 'green'
        elif future_7d['total_impact'] > 50 and future_14d['total_impact'] > 50:
            cycle = '情绪高涨期'
            suggestion = '持仓为主，注意高潮后兑现'
            cycle_color = 'red'
        elif future_7d['total_impact'] < 30:
            cycle = '情绪低谷期'
            suggestion = '控制仓位，等待新催化'
            cycle_color = 'gray'
        else:
            cycle = '情绪平稳期'
            suggestion = '结构性机会为主'
            cycle_color = 'yellow'
        
        return {
            'current_cycle': cycle,
            'cycle_color': cycle_color,
            'suggestion': suggestion,
            'window_stats': window_stats,
        }
    
    def analyze_topic_calendar(self, topic_name: str) -> Dict:
        """分析特定题材的催化日历"""
        topic_events = [
            e for e in self.events 
            if topic_name in e.related_topics or topic_name in e.title
        ]
        
        today = datetime.now().date()
        upcoming = []
        past = []
        
        for event in topic_events:
            try:
                event_date = datetime.strptime(event.date, '%Y-%m-%d').date()
                days_diff = (event_date - today).days
                
                event_dict = {
                    'title': event.title,
                    'date': event.date,
                    'days_diff': days_diff,
                    'type': event.type,
                    'impact_level': event.impact_level,
                    'impact_score': round(event.calculate_impact_score(), 1),
                }
                
                if days_diff >= 0:
                    upcoming.append(event_dict)
                else:
                    past.append(event_dict)
            except:
                continue
        
        upcoming.sort(key=lambda x: x['days_diff'])
        past.sort(key=lambda x: x['days_diff'], reverse=True)
        
        return {
            'topic': topic_name,
            'upcoming_count': len(upcoming),
            'past_count': len(past),
            'upcoming_events': upcoming[:10],
            'past_events': past[:5],
        }
    
    def generate_trading_suggestion(self) -> Dict:
        """生成交易建议"""
        sentiment = self.analyze_sentiment_cycle()
        upcoming = self.analyze_upcoming_events(days_ahead=30)
        
        # 高影响事件统计
        high_impact_events = [e for e in upcoming if e['impact_score'] >= 60]
        
        # 计算风险等级
        high_impact_count = len(high_impact_events)
        if high_impact_count >= 5:
            risk_level = '高波动'
            position_suggestion = '控制仓位，快进快出'
        elif high_impact_count >= 3:
            risk_level = '中等波动'
            position_suggestion = '适中仓位，波段操作'
        else:
            risk_level = '低波动'
            position_suggestion = '可持有为主'
        
        # 重点关注事件
        focus_events = sorted(upcoming, key=lambda x: x['impact_score'], reverse=True)[:5]
        
        return {
            'risk_level': risk_level,
            'position_suggestion': position_suggestion,
            'high_impact_count': high_impact_count,
            'focus_events': focus_events,
            'sentiment_cycle': sentiment['current_cycle'],
            'overall_suggestion': sentiment['suggestion'],
        }


class EventImpactBacktester:
    """事件影响回测器"""
    
    def __init__(self):
        pass
    
    def backtest_event(self, event_type: str, stock_code: str) -> Dict:
        """回测某类事件对个股的影响"""
        # 简化版：返回模拟的回测结果
        # 实际应用中需要历史事件数据和对应的股价表现
        
        patterns = {
            '政策利好': {
                'avg_return_1d': 2.5,
                'avg_return_3d': 4.2,
                'avg_return_5d': 5.1,
                'win_rate': 0.72,
                'max_drawdown': -3.5,
            },
            '业绩超预期': {
                'avg_return_1d': 4.8,
                'avg_return_3d': 6.1,
                'avg_return_5d': 7.3,
                'win_rate': 0.85,
                'max_drawdown': -2.8,
            },
            '行业景气': {
                'avg_return_1d': 1.8,
                'avg_return_3d': 3.2,
                'avg_return_5d': 4.5,
                'win_rate': 0.68,
                'max_drawdown': -4.2,
            },
        }
        
        return patterns.get(event_type, {
            'avg_return_1d': 2.0,
            'avg_return_3d': 3.0,
            'avg_return_5d': 3.5,
            'win_rate': 0.6,
            'max_drawdown': -5.0,
        })


def analyze_catalysts(events: List[Dict]) -> Dict:
    """便捷函数：分析催化事件"""
    analyzer = CatalystAnalyzer(events)
    
    return {
        'upcoming_events': analyzer.analyze_upcoming_events(30),
        'sentiment_cycle': analyzer.analyze_sentiment_cycle(),
        'trading_suggestion': analyzer.generate_trading_suggestion(),
        'analyze_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    }


if __name__ == '__main__':
    # 测试数据
    test_events = [
        {
            'title': '苹果WWDC开发者大会',
            'date': '2026-06-10',
            'type': '行业',
            'impact_level': 'high',
            'description': '苹果年度开发者大会，预计发布AI相关功能',
            'related_topics': ['AI应用', '苹果产业链'],
            'related_stocks': ['立讯精密', '歌尔股份'],
        },
        {
            'title': '央行MLF操作',
            'date': '2026-06-15',
            'type': '宏观',
            'impact_level': 'high',
            'description': '中期借贷便利操作，关注利率变化',
            'related_topics': ['大金融', '流动性'],
            'related_stocks': ['招商银行', '宁波银行'],
        },
        {
            'title': '存储芯片价格月度数据',
            'date': '2026-06-20',
            'type': '行业',
            'impact_level': 'medium',
            'description': 'DRAM/NAND闪存价格月度跟踪报告',
            'related_topics': ['存储芯片', '半导体'],
            'related_stocks': ['长江存储', '兆易创新'],
        },
        {
            'title': '特斯拉股东大会',
            'date': '2026-06-25',
            'type': '公司',
            'impact_level': 'medium',
            'description': '特斯拉年度股东大会，或有机器人相关消息',
            'related_topics': ['人形机器人', '新能源汽车'],
            'related_stocks': ['拓普集团', '三花智控'],
        },
        {
            'title': '中报业绩预告密集披露',
            'date': '2026-07-15',
            'type': '业绩',
            'impact_level': 'high',
            'description': '创业板中报业绩预告截止日',
            'related_topics': ['业绩预增'],
            'related_stocks': [],
        },
    ]
    
    result = analyze_catalysts(test_events)
    print(json.dumps(result, ensure_ascii=False, indent=2))
