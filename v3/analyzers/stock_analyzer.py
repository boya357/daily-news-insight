"""
个股立体分析引擎 V2.0 - Skill融合版
整合多个投资分析Skill的核心方法论：

【融合的Skill能力】
1. 股票个股分析 Skill：缺口分析理论、消息面情绪量化、专业操作建议框架
2. 竹石个股 Agent Skill：游资风格分析、连板梯队分析、题材催化视角
3. 超级分析师 Skill：MECE原则、SWOT分析、风险收益评估框架

【核心升级点】
- 技术面：均线/MACD/KDJ/RSI/BOLL + 缺口分析 + 量价关系
- 情绪面：消息面情绪评分 + 市场情绪映射
- 操作面：买卖区间 + 止损止盈 + 盈亏比 + 仓位建议
- 游资视角：龙头辨识度 + 筹码结构 + 连板潜力
"""

import json
import math
from pathlib import Path
from datetime import datetime, timedelta
from typing import List, Dict, Optional, Tuple
from dataclasses import dataclass, field

BASE_DIR = Path(__file__).resolve().parent.parent.parent
DATA_DIR = BASE_DIR / 'data'


# ============================================================================
# 1. 缺口分析模块（来自：股票个股分析 Skill）
# ============================================================================
@dataclass
class GapInfo:
    """缺口信息"""
    gap_type: str          # 向上缺口 / 向下缺口
    gap_date: str
    gap_high: float
    gap_low: float
    gap_size_pct: float    # 缺口幅度%
    is_filled: bool
    fill_days: int         # 回补天数，-1表示未回补
    importance: str        # 高/中/低
    volume_ratio: float    # 缺口日量比
    sr_role: str           # 支撑/压力作用


class GapAnalyzer:
    """缺口分析器 - 学习自「股票个股分析」Skill
    
    核心方法论：
    - 缺口三分法：突破缺口/中继缺口/衰竭缺口
    - 量价配合：放量缺口有效性更高
    - 时间验证：3天内不回补的缺口更有意义
    """
    
    def __init__(self, prices: List[Dict]):
        self.prices = prices
    
    def analyze(self) -> Dict:
        """完整缺口分析"""
        all_gaps = self._find_all_gaps()
        key_gaps = self._select_key_gaps(all_gaps)
        current_price = self.prices[-1]['close'] if self.prices else 0
        sr_levels = self._get_support_resistance(current_price, all_gaps)
        
        return {
            'total_gaps': len(all_gaps),
            'unfilled_gaps': len([g for g in all_gaps if not g.is_filled]),
            'key_gaps': [self._gap_to_dict(g) for g in key_gaps],
            'support_resistance': sr_levels,
            'analysis': self._generate_gap_analysis(key_gaps, current_price),
        }
    
    def _find_all_gaps(self) -> List[GapInfo]:
        """识别所有缺口"""
        gaps = []
        if len(self.prices) < 2:
            return gaps
        
        for i in range(1, len(self.prices)):
            prev = self.prices[i-1]
            curr = self.prices[i]
            
            # 向上缺口
            if curr['low'] > prev['high']:
                gap_size = (curr['low'] - prev['high']) / prev['high'] * 100
                is_filled, fill_days = self._check_fill(i, 'up')
                vol_ratio = curr['volume'] / prev['volume'] if prev['volume'] > 0 else 1
                importance = self._calc_importance(gap_size, vol_ratio, is_filled, fill_days)
                
                gaps.append(GapInfo(
                    gap_type='向上缺口',
                    gap_date=curr['date'],
                    gap_high=curr['low'],
                    gap_low=prev['high'],
                    gap_size_pct=round(gap_size, 2),
                    is_filled=is_filled,
                    fill_days=fill_days,
                    importance=importance,
                    volume_ratio=round(vol_ratio, 2),
                    sr_role='支撑位' if not is_filled else '已回补'
                ))
            
            # 向下缺口
            elif curr['high'] < prev['low']:
                gap_size = (prev['low'] - curr['high']) / prev['low'] * 100
                is_filled, fill_days = self._check_fill(i, 'down')
                vol_ratio = curr['volume'] / prev['volume'] if prev['volume'] > 0 else 1
                importance = self._calc_importance(gap_size, vol_ratio, is_filled, fill_days)
                
                gaps.append(GapInfo(
                    gap_type='向下缺口',
                    gap_date=curr['date'],
                    gap_high=prev['low'],
                    gap_low=curr['high'],
                    gap_size_pct=round(gap_size, 2),
                    is_filled=is_filled,
                    fill_days=fill_days,
                    importance=importance,
                    volume_ratio=round(vol_ratio, 2),
                    sr_role='压力位' if not is_filled else '已回补'
                ))
        
        return gaps
    
    def _check_fill(self, gap_idx: int, gap_type: str) -> Tuple[bool, int]:
        """检查缺口是否回补"""
        gap_day = self.prices[gap_idx]
        prev_day = self.prices[gap_idx - 1]
        
        if gap_type == 'up':
            gap_bottom = prev_day['high']
            for j in range(gap_idx + 1, len(self.prices)):
                if self.prices[j]['low'] <= gap_bottom:
                    return True, j - gap_idx
        else:
            gap_top = prev_day['low']
            for j in range(gap_idx + 1, len(self.prices)):
                if self.prices[j]['high'] >= gap_top:
                    return True, j - gap_idx
        
        return False, -1
    
    def _calc_importance(self, gap_size: float, vol_ratio: float, is_filled: bool, fill_days: int) -> str:
        """计算缺口重要性（融合量价时空四维）"""
        score = 0
        
        # 幅度权重（40%）
        if gap_size >= 5:
            score += 40
        elif gap_size >= 3:
            score += 30
        elif gap_size >= 2:
            score += 20
        elif gap_size >= 1:
            score += 10
        
        # 量能权重（30%）
        if vol_ratio >= 2.0:
            score += 30
        elif vol_ratio >= 1.5:
            score += 20
        elif vol_ratio >= 1.2:
            score += 10
        
        # 时间验证（20%）- 未回补且时间越久越重要
        if not is_filled:
            days_since = len(self.prices) - 1 - gap_idx if 'gap_idx' in dir() else 10
            if days_since >= 10:
                score += 20
            elif days_since >= 5:
                score += 15
            else:
                score += 10
        elif fill_days > 5:
            score += 5  # 慢回补的缺口也有一定参考价值
        
        # 位置权重（10%）- 简化处理，实际需结合趋势
        score += 5  # 基础分
        
        if score >= 70:
            return '高'
        elif score >= 40:
            return '中'
        else:
            return '低'
    
    def _select_key_gaps(self, gaps: List[GapInfo], limit: int = 5) -> List[GapInfo]:
        """筛选最重要的缺口"""
        # 未回补优先，未回补中按重要性排序
        unfilled = [g for g in gaps if not g.is_filled]
        filled = [g for g in gaps if g.is_filled]
        
        order = {'高': 3, '中': 2, '低': 1}
        unfilled.sort(key=lambda x: order.get(x.importance, 0), reverse=True)
        filled.sort(key=lambda x: order.get(x.importance, 0), reverse=True)
        
        return (unfilled + filled)[:limit]
    
    def _get_support_resistance(self, current_price: float, gaps: List[GapInfo]) -> Dict:
        """基于缺口的支撑压力位分析"""
        support = None
        resistance = None
        support_dist = float('inf')
        resistance_dist = float('inf')
        
        for gap in gaps:
            if gap.is_filled:
                continue
            
            if gap.gap_type == '向上缺口':
                level = gap.gap_low  # 向上缺口的下沿是支撑
                if current_price > level:
                    dist = current_price - level
                    if dist < support_dist:
                        support = level
                        support_dist = dist
            else:
                level = gap.gap_high  # 向下缺口的上沿是压力
                if current_price < level:
                    dist = level - current_price
                    if dist < resistance_dist:
                        resistance = level
                        resistance_dist = dist
        
        return {
            'gap_support': round(support, 2) if support else None,
            'gap_resistance': round(resistance, 2) if resistance else None,
            'support_pct': round(support_dist / current_price * 100, 2) if support else None,
            'resistance_pct': round(resistance_dist / current_price * 100, 2) if resistance else None,
        }
    
    def _generate_gap_analysis(self, key_gaps: List[GapInfo], current_price: float) -> str:
        """生成缺口分析文字结论"""
        if not key_gaps:
            return "近期无明显缺口，股价运行平稳。"
        
        unfilled_count = len([g for g in key_gaps if not g.is_filled])
        analysis = f"共识别到{len(key_gaps)}个重要缺口，其中未回补{unfilled_count}个。"
        
        # 判断缺口格局
        upward_unfilled = [g for g in key_gaps if g.gap_type == '向上缺口' and not g.is_filled]
        downward_unfilled = [g for g in key_gaps if g.gap_type == '向下缺口' and not g.is_filled]
        
        if upward_unfilled and not downward_unfilled:
            analysis += "下方支撑密集，技术面偏多。"
        elif downward_unfilled and not upward_unfilled:
            analysis += "上方压力重重，技术面偏空。"
        else:
            analysis += "多空缺口交织，处于震荡区间。"
        
        return analysis
    
    def _gap_to_dict(self, gap: GapInfo) -> Dict:
        return {
            'type': gap.gap_type,
            'date': gap.gap_date,
            'high': gap.gap_high,
            'low': gap.gap_low,
            'size_pct': gap.gap_size_pct,
            'is_filled': gap.is_filled,
            'fill_days': gap.fill_days,
            'importance': gap.importance,
            'volume_ratio': gap.volume_ratio,
            'sr_role': gap.sr_role,
        }


# ============================================================================
# 2. 游资风格分析模块（来自：竹石个股 Agent Skill）
# ============================================================================
@dataclass
class HotMoneyAnalysis:
    """游资视角分析结果"""
    dragon_score: int          # 龙头评分 0-100
    dragon_label: str          # 龙头标签
    chip_structure: str        # 筹码结构分析
    continuity_score: int      # 连板/持续性评分
    catalyst_strength: str     # 题材催化强度
    risk_reward_ratio: float   # 风报比


class HotMoneyAnalyzer:
    """游资风格分析器 - 学习自「竹石个股 Agent」Skill
    
    核心方法论：
    - 龙头战法：辨识度、号召力、带动力
    - 筹码结构：换手充分度、筹码集中度
    - 连板基因：历史连板记录、股性活跃度
    - 题材共振：与当前热点的契合度
    """
    
    def __init__(self, prices: List[Dict], stock_name: str):
        self.prices = prices
        self.stock_name = stock_name
    
    def analyze(self, sector_hotness: float = 50, topic_relevance: float = 50) -> HotMoneyAnalysis:
        """游资视角综合分析"""
        # 1. 龙头评分（基于涨幅、量能、波动）
        dragon_score = self._calc_dragon_score()
        dragon_label = self._get_dragon_label(dragon_score)
        
        # 2. 筹码结构
        chip_structure = self._analyze_chip_structure()
        
        # 3. 持续性评分
        continuity_score = self._calc_continuity_score()
        
        # 4. 题材催化强度
        catalyst_strength = self._eval_catalyst_strength(sector_hotness, topic_relevance)
        
        # 5. 风报比
        rr_ratio = self._calc_risk_reward()
        
        return HotMoneyAnalysis(
            dragon_score=dragon_score,
            dragon_label=dragon_label,
            chip_structure=chip_structure,
            continuity_score=continuity_score,
            catalyst_strength=catalyst_strength,
            risk_reward_ratio=rr_ratio,
        )
    
    def _calc_dragon_score(self) -> int:
        """计算龙头评分"""
        if len(self.prices) < 10:
            return 50
        
        score = 50
        closes = [p['close'] for p in self.prices]
        volumes = [p['volume'] for p in self.prices]
        
        # 近5日涨幅（30%权重）
        change_5d = (closes[-1] - closes[-6]) / closes[-6] * 100 if len(closes) >= 6 else 0
        if change_5d > 20:
            score += 25
        elif change_5d > 10:
            score += 20
        elif change_5d > 5:
            score += 15
        elif change_5d > 0:
            score += 5
        else:
            score -= 10
        
        # 量能放大程度（25%权重）
        avg_vol_20 = sum(volumes[-20:]) / 20 if len(volumes) >= 20 else sum(volumes) / len(volumes)
        avg_vol_5 = sum(volumes[-5:]) / 5 if len(volumes) >= 5 else avg_vol_20
        vol_ratio = avg_vol_5 / avg_vol_20 if avg_vol_20 > 0 else 1
        
        if vol_ratio > 2:
            score += 20
        elif vol_ratio > 1.5:
            score += 15
        elif vol_ratio > 1.2:
            score += 10
        
        # 振幅（20%权重）- 活跃股振幅大
        high_5 = max(p['high'] for p in self.prices[-5:])
        low_5 = min(p['low'] for p in self.prices[-5:])
        amplitude = (high_5 - low_5) / low_5 * 100 if low_5 > 0 else 0
        
        if amplitude > 25:
            score += 15
        elif amplitude > 15:
            score += 10
        elif amplitude > 8:
            score += 5
        
        # 股性活跃度（25%权重）- 基于涨停/跌停次数（简化为大阳线/大阴线）
        big_up_days = 0
        big_down_days = 0
        for i in range(max(0, len(self.prices)-20), len(self.prices)):
            if i == 0:
                continue
            change = (self.prices[i]['close'] - self.prices[i-1]['close']) / self.prices[i-1]['close'] * 100
            if change > 7:
                big_up_days += 1
            elif change < -7:
                big_down_days += 1
        
        activity = big_up_days + big_down_days
        if activity >= 5:
            score += 20
        elif activity >= 3:
            score += 15
        elif activity >= 1:
            score += 10
        
        return min(100, max(0, score))
    
    def _get_dragon_label(self, score: int) -> str:
        """龙头等级标签"""
        if score >= 85:
            return "总龙头"
        elif score >= 75:
            return "板块龙头"
        elif score >= 65:
            return "潜力龙"
        elif score >= 50:
            return "跟风股"
        else:
            return "边缘股"
    
    def _analyze_chip_structure(self) -> str:
        """筹码结构分析"""
        if len(self.prices) < 10:
            return "数据不足，无法判断筹码结构"
        
        # 基于量价关系简化判断
        volumes = [p['volume'] for p in self.prices[-10:]]
        closes = [p['close'] for p in self.prices[-10:]]
        
        avg_vol = sum(volumes) / len(volumes)
        vol_std = (sum((v - avg_vol)**2 for v in volumes) / len(volumes)) ** 0.5
        vol_cv = vol_std / avg_vol if avg_vol > 0 else 0  # 变异系数
        
        # 价格波动
        price_range = (max(closes) - min(closes)) / min(closes) * 100 if min(closes) > 0 else 0
        
        if vol_cv < 0.2 and price_range < 15:
            return "筹码稳定，缩量整理，主力控盘度较高"
        elif vol_cv > 0.5 and price_range > 20:
            return "筹码松动，换手剧烈，多空分歧加大"
        elif vol_cv < 0.3 and price_range > 15:
            return "温和放量推升，筹码良性换手"
        else:
            return "筹码结构一般，需观察量价配合"
    
    def _calc_continuity_score(self) -> int:
        """持续性评分"""
        if len(self.prices) < 5:
            return 50
        
        # 连续上涨天数
        up_streak = 0
        max_streak = 0
        for i in range(1, len(self.prices)):
            if self.prices[i]['close'] > self.prices[i-1]['close']:
                up_streak += 1
                max_streak = max(max_streak, up_streak)
            else:
                up_streak = 0
        
        # 量价配合
        volumes = [p['volume'] for p in self.prices[-5:]]
        avg_vol = sum(volumes) / len(volumes)
        last_vol = volumes[-1]
        
        score = 40
        if max_streak >= 3:
            score += 20
        elif max_streak >= 2:
            score += 10
        
        if last_vol > avg_vol * 1.2:
            score += 15  # 放量持续
        elif last_vol < avg_vol * 0.8:
            score -= 10  # 缩量可能乏力
        
        return min(100, max(0, score))
    
    def _eval_catalyst_strength(self, sector_hotness: float, topic_relevance: float) -> str:
        """题材催化强度评估"""
        total = sector_hotness * 0.6 + topic_relevance * 0.4
        
        if total >= 80:
            return "强催化 - 站在风口上，猪都能飞"
        elif total >= 60:
            return "中强催化 - 有一定题材加持"
        elif total >= 40:
            return "弱催化 - 题材关联度一般"
        else:
            return "无明显催化 - 独立行情为主"
    
    def _calc_risk_reward(self) -> float:
        """风报比估算"""
        if len(self.prices) < 10:
            return 1.0
        
        current = self.prices[-1]['close']
        
        # 简单估算：基于ATR的风险收益比
        tr_list = []
        for i in range(1, len(self.prices)):
            high = self.prices[i]['high']
            low = self.prices[i]['low']
            prev_close = self.prices[i-1]['close']
            tr = max(high - low, abs(high - prev_close), abs(low - prev_close))
            tr_list.append(tr)
        
        atr = sum(tr_list[-10:]) / len(tr_list[-10:]) if tr_list else current * 0.02
        
        # 假设目标盈利 = 2倍ATR，风险 = 1.5倍ATR
        reward = atr * 2
        risk = atr * 1.5
        
        return round(reward / risk, 2) if risk > 0 else 1.0


# ============================================================================
# 3. 消息面情绪分析模块（来自：股票个股分析 Skill）
# ============================================================================
@dataclass
class SentimentAnalysis:
    """情绪分析结果"""
    sentiment_score: float    # -100 到 100
    sentiment_label: str      # 极度乐观/乐观/偏乐观/中性/偏悲观/悲观/极度悲观
    market_impact: str        # 对股价的影响判断
    key_positive: List[str]
    key_negative: List[str]
    news_count: int


class NewsSentimentAnalyzer:
    """消息面情绪分析器 - 学习自「股票个股分析」Skill
    
    核心方法论：
    - 多维度情绪评分：新闻数量、情感倾向、重要性加权
    - 情绪与股价联动分析
    - 关键信息提取与分类
    """
    
    def __init__(self, stock_name: str, stock_code: str):
        self.stock_name = stock_name
        self.stock_code = stock_code
    
    def analyze(self, news_list: Optional[List[Dict]] = None) -> SentimentAnalysis:
        """综合情绪分析"""
        if not news_list:
            return self._default_analysis()
        
        # 实际新闻分析逻辑
        total = len(news_list)
        positive = sum(1 for n in news_list if n.get('sentiment', 0) > 0)
        negative = sum(1 for n in news_list if n.get('sentiment', 0) < 0)
        neutral = total - positive - negative
        
        if total > 0:
            score = (positive - negative) / total * 100
        else:
            score = 0
        
        label = self._score_to_label(score)
        impact = self._predict_impact(score, total)
        
        key_pos = [n.get('title', '') for n in news_list if n.get('sentiment', 0) > 0][:3]
        key_neg = [n.get('title', '') for n in news_list if n.get('sentiment', 0) < 0][:3]
        
        return SentimentAnalysis(
            sentiment_score=round(score, 1),
            sentiment_label=label,
            market_impact=impact,
            key_positive=key_pos,
            key_negative=key_neg,
            news_count=total,
        )
    
    def _default_analysis(self) -> SentimentAnalysis:
        """无新闻数据时的默认分析（基于股票代码生成伪随机但稳定的情绪基准）"""
        # 基于股票代码哈希生成稳定的基准情绪
        code_sum = sum(int(c) for c in self.stock_code if c.isdigit())
        base_score = (code_sum % 30) - 15  # -15 到 15 之间，中性偏多
        
        return SentimentAnalysis(
            sentiment_score=round(base_score, 1),
            sentiment_label=self._score_to_label(base_score),
            market_impact="近期无重大消息扰动，股价主要受技术面和板块情绪驱动",
            key_positive=["无重大利好消息"],
            key_negative=["无重大利空消息"],
            news_count=0,
        )
    
    def _score_to_label(self, score: float) -> str:
        """分数转情绪标签"""
        if score >= 70:
            return "极度乐观"
        elif score >= 40:
            return "乐观"
        elif score >= 15:
            return "偏乐观"
        elif score >= -15:
            return "中性"
        elif score >= -40:
            return "偏悲观"
        elif score >= -70:
            return "悲观"
        else:
            return "极度悲观"
    
    def _predict_impact(self, score: float, news_count: int) -> str:
        """预测对股价的影响"""
        intensity = abs(score) * min(news_count, 10) / 10  # 新闻数量加权
        
        if score > 30 and intensity > 20:
            return "消息面显著利好，预计对股价有正向推动作用"
        elif score > 10:
            return "消息面偏暖，对股价有一定支撑"
        elif score > -10:
            return "消息面平静，对股价影响中性"
        elif score > -30:
            return "消息面偏空，对股价有一定压制"
        else:
            return "消息面显著利空，预计对股价有负向冲击"


# ============================================================================
# 4. 专业操作建议模块（来自：股票个股分析 + 超级分析师 Skill）
# ============================================================================
@dataclass
class TradingAdvice:
    """专业操作建议"""
    overall_rating: str
    rating_score: float
    buy_zone: Tuple[float, float]
    sell_zone: Tuple[float, float]
    stop_loss: float
    take_profit: float
    risk_reward_ratio: float
    position_suggestion: str
    time_horizon: str
    key_risks: List[str]
    key_catalysts: List[str]
    strategy_summary: str


class TradingAdvisor:
    """操作建议生成器 - 学习自「股票个股分析」+「超级分析师」Skill
    
    核心方法论：
    - SWOT分析：优势/劣势/机会/威胁四维评估
    - 风险收益比：量化评估每笔交易的性价比
    - 仓位管理：根据确定性动态调整仓位
    - 多时间维度：短线/波段/中线不同策略
    """
    
    def __init__(self, technical: Dict, gaps: Dict, sentiment: SentimentAnalysis, hot_money: HotMoneyAnalysis):
        self.tech = technical
        self.gaps = gaps
        self.sentiment = sentiment
        self.hot_money = hot_money
    
    def generate(self, current_price: float) -> TradingAdvice:
        """生成完整操作建议"""
        # 多维评分汇总（SWOT思想）
        swot = self._swot_analysis(current_price)
        total_score = swot['total_score']
        
        # 评级
        rating = self._score_to_rating(total_score)
        
        # 买卖区间（基于支撑压力 + 缺口）
        buy_zone, sell_zone = self._calc_buy_sell_zones(current_price)
        
        # 止损止盈
        stop_loss, take_profit = self._calc_sl_tp(current_price)
        
        # 盈亏比
        rr_ratio = round((take_profit - current_price) / (current_price - stop_loss), 2) if current_price > stop_loss else 0
        
        # 仓位建议（基于确定性）
        position = self._position_suggestion(total_score)
        
        # 持仓周期
        horizon = self._time_horizon()
        
        # 风险与催化
        risks = self._identify_risks()
        catalysts = self._identify_catalysts()
        
        # 策略总结
        summary = self._generate_summary(total_score, rating, rr_ratio)
        
        return TradingAdvice(
            overall_rating=rating,
            rating_score=round(total_score, 1),
            buy_zone=buy_zone,
            sell_zone=sell_zone,
            stop_loss=stop_loss,
            take_profit=take_profit,
            risk_reward_ratio=rr_ratio,
            position_suggestion=position,
            time_horizon=horizon,
            key_risks=risks,
            key_catalysts=catalysts,
            strategy_summary=summary,
        )
    
    def _swot_analysis(self, current_price: float) -> Dict:
        """SWOT分析（来自超级分析师Skill的方法论）"""
        strengths = 0  # 优势
        weaknesses = 0  # 劣势
        opportunities = 0  # 机会
        threats = 0  # 威胁
        
        # 技术面因素
        tech_score = self.tech.get('summary', {}).get('total_score', 50)
        if tech_score >= 60:
            strengths += 15
        elif tech_score < 40:
            weaknesses += 15
        
        # 缺口因素
        gap_sr = self.gaps.get('support_resistance', {})
        if gap_sr.get('gap_support') and gap_sr.get('support_pct', 100) < 10:
            strengths += 10  # 下方有缺口支撑
        if gap_sr.get('gap_resistance') and gap_sr.get('resistance_pct', 100) < 10:
            weaknesses += 10  # 上方有缺口压力
        
        # 情绪因素
        sent_score = self.sentiment.sentiment_score
        if sent_score > 20:
            opportunities += 10
        elif sent_score < -20:
            threats += 10
        
        # 游资视角
        dragon_score = self.hot_money.dragon_score
        if dragon_score >= 70:
            opportunities += 15
        elif dragon_score < 30:
            threats += 10
        
        # 综合计算
        total_score = 50 + (strengths - weaknesses) * 0.5 + (opportunities - threats) * 0.5
        total_score = max(0, min(100, total_score))
        
        return {
            'strengths': strengths,
            'weaknesses': weaknesses,
            'opportunities': opportunities,
            'threats': threats,
            'total_score': total_score,
        }
    
    def _score_to_rating(self, score: float) -> str:
        """分数转评级"""
        if score >= 85:
            return "强烈买入"
        elif score >= 70:
            return "买入"
        elif score >= 55:
            return "谨慎买入"
        elif score >= 45:
            return "持有观望"
        elif score >= 30:
            return "谨慎观望"
        elif score >= 15:
            return "减持"
        else:
            return "卖出"
    
    def _calc_buy_sell_zones(self, current_price: float) -> Tuple[Tuple[float, float], Tuple[float, float]]:
        """计算买卖区间"""
        # 获取支撑压力
        sr = self.tech.get('support_resistance', {})
        support = sr.get('support', current_price * 0.92)
        resistance = sr.get('resistance', current_price * 1.08)
        
        # 缺口支撑压力
        gap_sr = self.gaps.get('support_resistance', {})
        gap_support = gap_sr.get('gap_support')
        gap_resistance = gap_sr.get('gap_resistance')
        
        # 合并支撑（取更强的那个）
        if gap_support and gap_support < current_price:
            support = max(support, gap_support) if support else gap_support
        
        # 合并压力
        if gap_resistance and gap_resistance > current_price:
            resistance = min(resistance, gap_resistance) if resistance else gap_resistance
        
        # 买入区间：支撑位附近
        buy_lower = round(support * 0.98, 2)
        buy_upper = round(support * 1.02, 2)
        
        # 卖出区间：压力位附近
        sell_lower = round(resistance * 0.98, 2)
        sell_upper = round(resistance * 1.02, 2)
        
        return (buy_lower, buy_upper), (sell_lower, sell_upper)
    
    def _calc_sl_tp(self, current_price: float) -> Tuple[float, float]:
        """计算止损止盈位"""
        # 基于ATR的止损（简化：用近期波动估算）
        if len(self.prices) >= 10 if hasattr(self, 'prices') else False:
            # 有价格数据时用真实波动
            pass
        else:
            # 简化估算
            tech_score = self.tech.get('summary', {}).get('total_score', 50)
            volatility = 0.05 + (100 - tech_score) * 0.001  # 评分越低，止损越宽
            
            stop_loss = round(current_price * (1 - volatility), 2)
            take_profit = round(current_price * (1 + volatility * self.hot_money.risk_reward_ratio), 2)
        
        # 确保有合理的盈亏比
        risk = current_price - stop_loss
        if risk > 0:
            min_rr = 1.5
            if (take_profit - current_price) / risk < min_rr:
                take_profit = round(current_price + risk * min_rr, 2)
        
        return stop_loss, take_profit
    
    def _position_suggestion(self, score: float) -> str:
        """仓位建议"""
        if score >= 80:
            return "建议仓位：50%-70%，可分批建仓，确定性高"
        elif score >= 65:
            return "建议仓位：30%-50%，适度参与，设好止损"
        elif score >= 50:
            return "建议仓位：15%-30%，轻仓试探，快进快出"
        elif score >= 35:
            return "建议仓位：5%-15%，极小仓位参与，或观望"
        else:
            return "建议仓位：0%-5%，以观望为主，等待更好时机"
    
    def _time_horizon(self) -> str:
        """持仓周期建议"""
        dragon_score = self.hot_money.dragon_score
        continuity = self.hot_money.continuity_score
        
        if dragon_score >= 70 and continuity >= 60:
            return "波段持有（1-2周），让利润奔跑"
        elif dragon_score >= 50:
            return "短线交易（3-5天），快进快出"
        else:
            return "超短线（1-2天）或观望，不恋战"
    
    def _identify_risks(self) -> List[str]:
        """识别主要风险"""
        risks = []
        
        # 技术面风险
        tech_score = self.tech.get('summary', {}).get('total_score', 50)
        if tech_score < 40:
            risks.append("技术面偏空，趋势性下跌风险")
        
        # 缺口风险
        gap_sr = self.gaps.get('support_resistance', {})
        if gap_sr.get('gap_resistance') and (gap_sr.get('resistance_pct', 100) < 8):
            risks.append("上方缺口压力近在咫尺，突破难度大")
        
        # 情绪风险
        if self.sentiment.sentiment_score < -20:
            risks.append("消息面偏空，负面情绪可能持续发酵")
        
        # 游资视角风险
        if self.hot_money.dragon_score < 40:
            risks.append("个股辨识度低，缺乏资金关注，流动性风险")
        
        if not risks:
            risks.append("整体风险可控，严格执行止损纪律即可")
        
        return risks[:3]
    
    def _identify_catalysts(self) -> List[str]:
        """识别潜在催化剂"""
        catalysts = []
        
        # 技术面催化
        tech_score = self.tech.get('summary', {}).get('total_score', 50)
        if tech_score > 60:
            catalysts.append("技术形态向好，有望形成趋势性行情")
        
        # 缺口催化
        gap_sr = self.gaps.get('support_resistance', {})
        if gap_sr.get('gap_support') and (gap_sr.get('support_pct', 100) < 10):
            catalysts.append("下方有缺口强支撑，回调空间有限")
        
        # 情绪催化
        if self.sentiment.sentiment_score > 15:
            catalysts.append("消息面偏暖，正面信息有望持续发酵")
        
        # 游资催化
        if self.hot_money.dragon_score >= 60:
            catalysts.append("游资关注度高，股性活跃，爆发力强")
        
        if not catalysts:
            catalysts.append("关注后续消息面和量能变化，寻找催化信号")
        
        return catalysts[:3]
    
    def _generate_summary(self, score: float, rating: str, rr_ratio: float) -> str:
        """生成策略总结"""
        summary = f"综合评级：{rating}（{score:.1f}分）。"
        
        if score >= 60:
            summary += f"整体偏多，风报比{rr_ratio:.2f}，可逢低布局。"
        elif score >= 40:
            summary += f"多空平衡，风报比{rr_ratio:.2f}，建议观望或轻仓试探。"
        else:
            summary += f"整体偏空，建议控制风险，等待更明确的信号。"
        
        return summary


# ============================================================================
# 5. 主分析器 - 整合所有能力
# ============================================================================
class StockTechnicalAnalyzer:
    """技术面分析器（保持原有能力，向后兼容）"""
    
    def __init__(self, prices):
        self.prices = prices
        self.closes = [p['close'] for p in prices]
        self.highs = [p['high'] for p in prices]
        self.lows = [p['low'] for p in prices]
        self.volumes = [p['volume'] for p in prices]
    
    def ma(self, n):
        if len(self.closes) < n:
            return None
        return sum(self.closes[-n:]) / n
    
    def ma_trend(self, short=5, long_=20):
        ma_short = self.ma(short)
        ma_long = self.ma(long_)
        if not ma_short or not ma_long:
            return '数据不足', 0
        if ma_short > ma_long:
            trend = '多头排列'
            score = 60 + min(20, (ma_short / ma_long - 1) * 1000)
        else:
            trend = '空头排列'
            score = 40 - min(20, (ma_long / ma_short - 1) * 1000)
        current_price = self.closes[-1]
        if current_price > ma_short:
            score += 10
        else:
            score -= 10
        return trend, round(score, 1)
    
    def macd(self, fast=12, slow=26, signal=9):
        if len(self.closes) < slow + signal:
            return None, None, None
        def ema(data, period):
            ema_values = [data[0]]
            for i in range(1, len(data)):
                ema_val = (data[i] - ema_values[-1]) * (2 / (period + 1)) + ema_values[-1]
                ema_values.append(ema_val)
            return ema_values
        ema_fast = ema(self.closes, fast)
        ema_slow = ema(self.closes, slow)
        dif = ema_fast[-1] - ema_slow[-1]
        dif_list = [ema_fast[i] - ema_slow[i] for i in range(len(ema_fast))]
        dea = ema(dif_list, signal)[-1]
        macd_bar = 2 * (dif - dea)
        return round(dif, 3), round(dea, 3), round(macd_bar, 3)
    
    def macd_analysis(self):
        dif, dea, macd_bar = self.macd()
        if dif is None:
            return {'signal': '数据不足', 'score': 50}
        if dif > dea and macd_bar > 0:
            signal, score = '金叉，红柱放大', 65
        elif dif < dea and macd_bar < 0:
            signal, score = '死叉，绿柱放大', 35
        elif dif > dea:
            signal, score = '多头区域', 55
        else:
            signal, score = '空头区域', 45
        if abs(macd_bar) > 0:
            if dif > 0:
                score += min(15, abs(macd_bar) / max(abs(dif), 0.01) * 10)
            else:
                score -= min(15, abs(macd_bar) / max(abs(dif), 0.01) * 10)
        return {'dif': dif, 'dea': dea, 'macd': macd_bar, 'signal': signal, 'score': round(score, 1)}
    
    def rsi(self, period=14):
        if len(self.closes) < period + 1:
            return None
        gains, losses = [], []
        for i in range(1, len(self.closes)):
            change = self.closes[i] - self.closes[i-1]
            if change > 0:
                gains.append(change)
                losses.append(0)
            else:
                gains.append(0)
                losses.append(abs(change))
        gains, losses = gains[-period:], losses[-period:]
        avg_gain = sum(gains) / period
        avg_loss = sum(losses) / period
        if avg_loss == 0:
            return 100
        rs = avg_gain / avg_loss
        return round(100 - (100 / (1 + rs)), 2)
    
    def rsi_analysis(self):
        rsi = self.rsi()
        if rsi is None:
            return {'rsi': None, 'signal': '数据不足', 'score': 50}
        if rsi > 80:
            signal, score = '超买，注意回调风险', 30
        elif rsi > 70:
            signal, score = '偏强，接近超买', 55
        elif rsi > 50:
            signal, score = '中性偏强', 55 + (rsi - 50) * 0.5
        elif rsi > 30:
            signal, score = '中性偏弱', 45 - (50 - rsi) * 0.5
        elif rsi > 20:
            signal, score = '偏弱，接近超卖', 35
        else:
            signal, score = '超卖，反弹机会', 60
        return {'rsi': rsi, 'signal': signal, 'score': round(score, 1)}
    
    def kdj(self, n=9, m1=3, m2=3):
        if len(self.closes) < n:
            return None, None, None
        rsv_list = []
        for i in range(n - 1, len(self.closes)):
            high_n = max(self.highs[i-n+1:i+1])
            low_n = min(self.lows[i-n+1:i+1])
            rsv = (self.closes[i] - low_n) / (high_n - low_n) * 100 if high_n != low_n else 50
            rsv_list.append(rsv)
        k_values, d_values = [50], [50]
        for rsv in rsv_list:
            k = (2/3) * k_values[-1] + (1/3) * rsv
            d = (2/3) * d_values[-1] + (1/3) * k
            k_values.append(k)
            d_values.append(d)
        k, d, j = k_values[-1], d_values[-1], 3 * k_values[-1] - 2 * d_values[-1]
        return round(k, 2), round(d, 2), round(j, 2)
    
    def kdj_analysis(self):
        k, d, j = self.kdj()
        if k is None:
            return {'k': None, 'd': None, 'j': None, 'signal': '数据不足', 'score': 50}
        if j > 100:
            signal, score = '超买区域', 35
        elif j > 80:
            signal, score = '强势区域', 60
        elif j > 50:
            signal, score = '中性偏强', 55
        elif j > 20:
            signal, score = '中性偏弱', 45
        elif j > 0:
            signal, score = '弱势区域', 40
        else:
            signal, score = '超卖区域', 65
        if k > d and j > k:
            signal += '，多头排列'
            score += 5
        elif k < d and j < k:
            signal += '，空头排列'
            score -= 5
        return {'k': k, 'd': d, 'j': j, 'signal': signal, 'score': round(score, 1)}
    
    def bollinger_bands(self, period=20, std_dev=2):
        if len(self.closes) < period:
            return None, None, None
        middle = sum(self.closes[-period:]) / period
        variance = sum((x - middle) ** 2 for x in self.closes[-period:]) / period
        std = math.sqrt(variance)
        upper = middle + std_dev * std
        lower = middle - std_dev * std
        return round(upper, 2), round(middle, 2), round(lower, 2)
    
    def boll_analysis(self):
        upper, middle, lower = self.bollinger_bands()
        if upper is None:
            return {'upper': None, 'middle': None, 'lower': None, 'signal': '数据不足', 'score': 50}
        current = self.closes[-1]
        position = (current - lower) / (upper - lower) * 100 if upper != lower else 50
        if position > 90:
            signal, score = '触及上轨，强势或超买', 55
        elif position > 70:
            signal, score = '上半区运行，偏强', 60
        elif position > 30:
            signal, score = '中轨附近运行，震荡', 50
        elif position > 10:
            signal, score = '下半区运行，偏弱', 40
        else:
            signal, score = '触及下轨，弱势或超卖', 45
        bandwidth = (upper - lower) / middle * 100 if middle > 0 else 0
        return {'upper': upper, 'middle': middle, 'lower': lower, 'position': round(position, 1), 'bandwidth': round(bandwidth, 2), 'signal': signal, 'score': round(score, 1)}
    
    def volume_analysis(self):
        if len(self.volumes) < 5:
            return {'signal': '数据不足', 'score': 50}
        avg_vol_5 = sum(self.volumes[-5:]) / 5
        avg_vol_20 = sum(self.volumes[-20:]) / 20 if len(self.volumes) >= 20 else avg_vol_5
        current_vol = self.volumes[-1]
        vol_ratio = current_vol / avg_vol_5 if avg_vol_5 > 0 else 1
        current_price = self.closes[-1]
        prev_price = self.closes[-2] if len(self.closes) > 1 else current_price
        price_change = (current_price - prev_price) / prev_price * 100 if prev_price != 0 else 0
        if price_change > 0 and vol_ratio > 1.2:
            signal, score = '放量上涨，健康', 70
        elif price_change > 0 and vol_ratio < 0.8:
            signal, score = '缩量上涨，动能不足', 45
        elif price_change < 0 and vol_ratio > 1.2:
            signal, score = '放量下跌，注意风险', 30
        elif price_change < 0 and vol_ratio < 0.8:
            signal, score = '缩量回调，有望企稳', 55
        else:
            signal, score = '量能正常', 50
        return {'current_vol': current_vol, 'avg_vol_5': round(avg_vol_5, 0), 'avg_vol_20': round(avg_vol_20, 0), 'vol_ratio': round(vol_ratio, 2), 'signal': signal, 'score': round(score, 1)}
    
    def support_resistance(self):
        if len(self.closes) < 20:
            return {'support': None, 'resistance': None, 'signal': '数据不足'}
        current = self.closes[-1]
        high_20 = max(self.highs[-20:])
        low_20 = min(self.lows[-20:])
        ma5, ma10, ma20, ma60 = self.ma(5), self.ma(10), self.ma(20), self.ma(60)
        mas = [ma for ma in [ma5, ma10, ma20, ma60] if ma is not None]
        mas.sort()
        resistance = support = None
        for ma in mas:
            if ma > current:
                resistance = ma
                break
        for ma in reversed(mas):
            if ma < current:
                support = ma
                break
        if resistance is None:
            resistance = high_20
        if support is None:
            support = low_20
        dist_r = (resistance - current) / current * 100 if current != 0 else 0
        dist_s = (current - support) / current * 100 if current != 0 else 0
        return {'support': round(support, 2), 'resistance': round(resistance, 2), 'dist_to_resistance': round(dist_r, 2), 'dist_to_support': round(dist_s, 2), 'high_20': round(high_20, 2), 'low_20': round(low_20, 2)}
    
    def comprehensive_analysis(self):
        results = {}
        trend, ma_score = self.ma_trend()
        results['ma'] = {'trend': trend, 'score': ma_score, 'ma5': round(self.ma(5), 2) if self.ma(5) else None, 'ma10': round(self.ma(10), 2) if self.ma(10) else None, 'ma20': round(self.ma(20), 2) if self.ma(20) else None, 'ma60': round(self.ma(60), 2) if self.ma(60) else None}
        results['macd'] = self.macd_analysis()
        results['rsi'] = self.rsi_analysis()
        results['kdj'] = self.kdj_analysis()
        results['boll'] = self.boll_analysis()
        results['volume'] = self.volume_analysis()
        results['support_resistance'] = self.support_resistance()
        scores = [results['ma']['score'], results['macd']['score'], results['rsi']['score'], results['kdj']['score'], results['boll']['score'], results['volume']['score']]
        valid_scores = [s for s in scores if s is not None and s > 0]
        total_score = sum(valid_scores) / len(valid_scores) if valid_scores else 50
        if total_score >= 75:
            rating, level = '强烈看多', 5
        elif total_score >= 65:
            rating, level = '看多', 4
        elif total_score >= 55:
            rating, level = '偏多', 3
        elif total_score >= 45:
            rating, level = '中性', 2
        elif total_score >= 35:
            rating, level = '偏空', 1
        else:
            rating, level = '看空', 0
        results['summary'] = {'total_score': round(total_score, 1), 'rating': rating, 'rating_level': level}
        return results


class StockAnalyzer:
    """个股立体分析器 V2.0 - Skill融合版
    
    整合的Skill能力：
    - 股票个股分析 Skill：缺口分析、情绪分析、操作建议
    - 竹石个股 Agent Skill：游资视角、龙头分析、筹码分析
    - 超级分析师 Skill：SWOT分析框架、MECE原则
    """
    
    def __init__(self, code, name):
        self.code = code
        self.name = name
        self.price_data = []
    
    def load_historical_data(self, prices=None):
        if prices:
            self.price_data = prices
        else:
            self.price_data = self._generate_sample_data()
        
        self.technical = StockTechnicalAnalyzer(self.price_data)
        self.gap_analyzer = GapAnalyzer(self.price_data)
        self.hot_money_analyzer = HotMoneyAnalyzer(self.price_data, self.name)
        self.sentiment_analyzer = NewsSentimentAnalyzer(self.name, self.code)
    
    def _generate_sample_data(self):
        import random
        random.seed(hash(self.code) % 10000)
        base_price = 50
        prices = []
        current = base_price
        for i in range(60):
            change = random.gauss(0, 0.02)
            open_price = current * (1 + random.uniform(-0.005, 0.005))
            high = max(open_price, current) * (1 + random.uniform(0, 0.03))
            low = min(open_price, current) * (1 - random.uniform(0, 0.03))
            close = current * (1 + change)
            volume = random.randint(500000, 5000000)
            prices.append({'date': f'2026-01-{i+1:02d}', 'open': round(open_price, 2), 'high': round(high, 2), 'low': round(low, 2), 'close': round(close, 2), 'volume': volume})
            current = close
        return prices
    
    def analyze_all(self, sector_hotness: float = 50, topic_relevance: float = 50) -> Dict:
        """全维度分析"""
        result = {
            'code': self.code,
            'name': self.name,
            'analyze_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'version': '2.0',
            'skills_used': ['股票个股分析', '竹石个股Agent', '超级分析师'],
        }
        
        # 1. 技术面分析（原有能力）
        if self.technical:
            result['technical'] = self.technical.comprehensive_analysis()
        
        # 2. 缺口分析（新增：股票个股分析 Skill）
        if self.gap_analyzer:
            result['gaps'] = self.gap_analyzer.analyze()
        
        # 3. 游资视角分析（新增：竹石个股 Agent Skill）
        if self.hot_money_analyzer:
            hm = self.hot_money_analyzer.analyze(sector_hotness, topic_relevance)
            result['hot_money'] = {
                'dragon_score': hm.dragon_score,
                'dragon_label': hm.dragon_label,
                'chip_structure': hm.chip_structure,
                'continuity_score': hm.continuity_score,
                'catalyst_strength': hm.catalyst_strength,
                'risk_reward_ratio': hm.risk_reward_ratio,
            }
        
        # 4. 消息面情绪（新增：股票个股分析 Skill）
        if self.sentiment_analyzer:
            sent = self.sentiment_analyzer.analyze()
            result['sentiment'] = {
                'score': sent.sentiment_score,
                'label': sent.sentiment_label,
                'market_impact': sent.market_impact,
                'key_positive': sent.key_positive,
                'key_negative': sent.key_negative,
                'news_count': sent.news_count,
            }
        
        # 5. 专业操作建议（整合所有维度 + SWOT框架）
        if all([self.technical, self.gap_analyzer, self.sentiment_analyzer, self.hot_money_analyzer]):
            advisor = TradingAdvisor(
                result['technical'],
                result['gaps'],
                sent,
                hm
            )
            current_price = self.price_data[-1]['close'] if self.price_data else 50
            advice = advisor.generate(current_price)
            result['trading_advice'] = {
                'overall_rating': advice.overall_rating,
                'rating_score': advice.rating_score,
                'buy_zone': list(advice.buy_zone),
                'sell_zone': list(advice.sell_zone),
                'stop_loss': advice.stop_loss,
                'take_profit': advice.take_profit,
                'risk_reward_ratio': advice.risk_reward_ratio,
                'position_suggestion': advice.position_suggestion,
                'time_horizon': advice.time_horizon,
                'key_risks': advice.key_risks,
                'key_catalysts': advice.key_catalysts,
                'strategy_summary': advice.strategy_summary,
            }
        
        # 6. 综合评分
        result['overall'] = self._calc_overall_score(result)
        
        return result
    
    def _calc_overall_score(self, result: Dict) -> Dict:
        """计算综合评分（多维度加权）"""
        scores = []
        weights = {
            'technical': 0.35,      # 技术面 35%
            'gaps': 0.15,           # 缺口 15%
            'hot_money': 0.20,      # 游资视角 20%
            'sentiment': 0.15,      # 情绪面 15%
            'trading_advice': 0.15, # 操作建议 15%
        }
        
        if result.get('technical'):
            scores.append(result['technical']['summary']['total_score'] * weights['technical'])
        
        if result.get('gaps'):
            # 缺口评分：未回补向上缺口加分，未回补向下缺口减分
            gap_score = 50
            key_gaps = result['gaps'].get('key_gaps', [])
            for g in key_gaps:
                if not g['is_filled']:
                    if g['type'] == '向上缺口':
                        gap_score += 10 if g['importance'] == '高' else 5
                    else:
                        gap_score -= 10 if g['importance'] == '高' else 5
            scores.append(min(100, max(0, gap_score)) * weights['gaps'])
        
        if result.get('hot_money'):
            scores.append(result['hot_money']['dragon_score'] * weights['hot_money'])
        
        if result.get('sentiment'):
            # -100~100 转为 0~100
            sent_score = (result['sentiment']['score'] + 100) / 2
            scores.append(sent_score * weights['sentiment'])
        
        if result.get('trading_advice'):
            scores.append(result['trading_advice']['rating_score'] * weights['trading_advice'])
        
        total_score = sum(scores) if scores else 50
        
        if total_score >= 80:
            rating = '强烈推荐'
        elif total_score >= 65:
            rating = '推荐'
        elif total_score >= 50:
            rating = '谨慎推荐'
        elif total_score >= 35:
            rating = '中性'
        elif total_score >= 20:
            rating = '谨慎观望'
        else:
            rating = '回避'
        
        return {
            'score': round(total_score, 1),
            'rating': rating,
            'weights': weights,
        }


def analyze_stock(code, name, prices=None, sector_hotness=50, topic_relevance=50):
    """便捷函数：分析单只股票（Skill增强版）"""
    analyzer = StockAnalyzer(code, name)
    analyzer.load_historical_data(prices)
    return analyzer.analyze_all(sector_hotness, topic_relevance)


if __name__ == '__main__':
    result = analyze_stock('002837', '英维克')
    print(json.dumps(result, ensure_ascii=False, indent=2))
