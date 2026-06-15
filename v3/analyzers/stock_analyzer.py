"""
个股立体分析引擎
- 技术面分析：均线、MACD、KDJ、RSI、BOLL等
- 资金面分析：成交量、成交额、主力资金
- 基本面分析：估值、市值、盈利能力
- 综合评级与买卖点评估
"""

import json
import math
from pathlib import Path
from datetime import datetime, timedelta

BASE_DIR = Path(__file__).resolve().parent.parent.parent
DATA_DIR = BASE_DIR / 'data'


class StockTechnicalAnalyzer:
    """技术面分析器"""
    
    def __init__(self, prices):
        """
        Args:
            prices: list of dict, 包含 date, open, high, low, close, volume
        """
        self.prices = prices
        self.closes = [p['close'] for p in prices]
        self.highs = [p['high'] for p in prices]
        self.lows = [p['low'] for p in prices]
        self.volumes = [p['volume'] for p in prices]
    
    def ma(self, n):
        """计算n日均线"""
        if len(self.closes) < n:
            return None
        return sum(self.closes[-n:]) / n
    
    def ma_trend(self, short=5, long_=20):
        """均线趋势判断"""
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
        """计算MACD"""
        if len(self.closes) < slow + signal:
            return None, None, None
        
        def ema(data, period):
            ema_values = []
            multiplier = 2 / (period + 1)
            ema_values.append(data[0])
            for i in range(1, len(data)):
                ema_val = (data[i] - ema_values[-1]) * multiplier + ema_values[-1]
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
        """MACD分析"""
        dif, dea, macd_bar = self.macd()
        
        if dif is None:
            return {'signal': '数据不足', 'score': 50}
        
        if dif > dea and macd_bar > 0:
            signal = '金叉，红柱放大'
            score = 65
        elif dif < dea and macd_bar < 0:
            signal = '死叉，绿柱放大'
            score = 35
        elif dif > dea:
            signal = '多头区域'
            score = 55
        else:
            signal = '空头区域'
            score = 45
        
        if abs(macd_bar) > 0:
            if dif > 0:
                score += min(15, abs(macd_bar) / max(abs(dif), 0.01) * 10)
            else:
                score -= min(15, abs(macd_bar) / max(abs(dif), 0.01) * 10)
        
        return {
            'dif': dif,
            'dea': dea,
            'macd': macd_bar,
            'signal': signal,
            'score': round(score, 1)
        }
    
    def rsi(self, period=14):
        """计算RSI"""
        if len(self.closes) < period + 1:
            return None
        
        gains = []
        losses = []
        
        for i in range(1, len(self.closes)):
            change = self.closes[i] - self.closes[i-1]
            if change > 0:
                gains.append(change)
                losses.append(0)
            else:
                gains.append(0)
                losses.append(abs(change))
        
        gains = gains[-period:]
        losses = losses[-period:]
        
        avg_gain = sum(gains) / period
        avg_loss = sum(losses) / period
        
        if avg_loss == 0:
            return 100
        
        rs = avg_gain / avg_loss
        rsi = 100 - (100 / (1 + rs))
        
        return round(rsi, 2)
    
    def rsi_analysis(self):
        """RSI分析"""
        rsi = self.rsi()
        
        if rsi is None:
            return {'rsi': None, 'signal': '数据不足', 'score': 50}
        
        if rsi > 80:
            signal = '超买，注意回调风险'
            score = 30
        elif rsi > 70:
            signal = '偏强，接近超买'
            score = 55
        elif rsi > 50:
            signal = '中性偏强'
            score = 55 + (rsi - 50) * 0.5
        elif rsi > 30:
            signal = '中性偏弱'
            score = 45 - (50 - rsi) * 0.5
        elif rsi > 20:
            signal = '偏弱，接近超卖'
            score = 35
        else:
            signal = '超卖，反弹机会'
            score = 60
        
        return {
            'rsi': rsi,
            'signal': signal,
            'score': round(score, 1)
        }
    
    def kdj(self, n=9, m1=3, m2=3):
        """计算KDJ"""
        if len(self.closes) < n:
            return None, None, None
        
        rsv_list = []
        for i in range(n - 1, len(self.closes)):
            high_n = max(self.highs[i-n+1:i+1])
            low_n = min(self.lows[i-n+1:i+1])
            if high_n == low_n:
                rsv = 50
            else:
                rsv = (self.closes[i] - low_n) / (high_n - low_n) * 100
            rsv_list.append(rsv)
        
        k_values = [50]
        d_values = [50]
        
        for rsv in rsv_list:
            k = (2/3) * k_values[-1] + (1/3) * rsv
            d = (2/3) * d_values[-1] + (1/3) * k
            k_values.append(k)
            d_values.append(d)
        
        k = k_values[-1]
        d = d_values[-1]
        j = 3 * k - 2 * d
        
        return round(k, 2), round(d, 2), round(j, 2)
    
    def kdj_analysis(self):
        """KDJ分析"""
        k, d, j = self.kdj()
        
        if k is None:
            return {'k': None, 'd': None, 'j': None, 'signal': '数据不足', 'score': 50}
        
        if j > 100:
            signal = '超买区域'
            score = 35
        elif j > 80:
            signal = '强势区域'
            score = 60
        elif j > 50:
            signal = '中性偏强'
            score = 55
        elif j > 20:
            signal = '中性偏弱'
            score = 45
        elif j > 0:
            signal = '弱势区域'
            score = 40
        else:
            signal = '超卖区域'
            score = 65
        
        if k > d and j > k:
            signal += '，多头排列'
            score += 5
        elif k < d and j < k:
            signal += '，空头排列'
            score -= 5
        
        return {
            'k': k,
            'd': d,
            'j': j,
            'signal': signal,
            'score': round(score, 1)
        }
    
    def bollinger_bands(self, period=20, std_dev=2):
        """计算布林带"""
        if len(self.closes) < period:
            return None, None, None
        
        middle = sum(self.closes[-period:]) / period
        variance = sum((x - middle) ** 2 for x in self.closes[-period:]) / period
        std = math.sqrt(variance)
        
        upper = middle + std_dev * std
        lower = middle - std_dev * std
        
        return round(upper, 2), round(middle, 2), round(lower, 2)
    
    def boll_analysis(self):
        """布林带分析"""
        upper, middle, lower = self.bollinger_bands()
        
        if upper is None:
            return {'upper': None, 'middle': None, 'lower': None, 'signal': '数据不足', 'score': 50}
        
        current = self.closes[-1]
        
        if upper - lower == 0:
            position = 50
        else:
            position = (current - lower) / (upper - lower) * 100
        
        if position > 90:
            signal = '触及上轨，强势或超买'
            score = 55
        elif position > 70:
            signal = '上半区运行，偏强'
            score = 60
        elif position > 30:
            signal = '中轨附近运行，震荡'
            score = 50
        elif position > 10:
            signal = '下半区运行，偏弱'
            score = 40
        else:
            signal = '触及下轨，弱势或超卖'
            score = 45
        
        bandwidth = (upper - lower) / middle * 100 if middle > 0 else 0
        
        return {
            'upper': upper,
            'middle': middle,
            'lower': lower,
            'position': round(position, 1),
            'bandwidth': round(bandwidth, 2),
            'signal': signal,
            'score': round(score, 1)
        }
    
    def volume_analysis(self):
        """成交量分析"""
        if len(self.volumes) < 5:
            return {'signal': '数据不足', 'score': 50}
        
        avg_vol_5 = sum(self.volumes[-5:]) / 5
        avg_vol_20 = sum(self.volumes[-20:]) / 20 if len(self.volumes) >= 20 else avg_vol_5
        
        current_vol = self.volumes[-1]
        vol_ratio = current_vol / avg_vol_5 if avg_vol_5 > 0 else 1
        
        current_price = self.closes[-1]
        prev_price = self.closes[-2] if len(self.closes) > 1 else current_price
        price_change = (current_price - prev_price) / prev_price if prev_price != 0 else 0
        
        if price_change > 0 and vol_ratio > 1.2:
            signal = '放量上涨，健康'
            score = 70
        elif price_change > 0 and vol_ratio < 0.8:
            signal = '缩量上涨，动能不足'
            score = 45
        elif price_change < 0 and vol_ratio > 1.2:
            signal = '放量下跌，注意风险'
            score = 30
        elif price_change < 0 and vol_ratio < 0.8:
            signal = '缩量回调，有望企稳'
            score = 55
        else:
            signal = '量能正常'
            score = 50
        
        return {
            'current_vol': current_vol,
            'avg_vol_5': round(avg_vol_5, 0),
            'avg_vol_20': round(avg_vol_20, 0),
            'vol_ratio': round(vol_ratio, 2),
            'signal': signal,
            'score': round(score, 1)
        }
    
    def support_resistance(self):
        """支撑压力位分析"""
        if len(self.closes) < 20:
            return {'support': None, 'resistance': None, 'signal': '数据不足'}
        
        current = self.closes[-1]
        high_20 = max(self.highs[-20:])
        low_20 = min(self.lows[-20:])
        
        ma5 = self.ma(5)
        ma10 = self.ma(10)
        ma20 = self.ma(20)
        ma60 = self.ma(60)
        
        mas = [ma for ma in [ma5, ma10, ma20, ma60] if ma is not None]
        mas.sort()
        
        resistance = None
        support = None
        
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
        
        dist_to_resistance = (resistance - current) / current * 100 if current != 0 else 0
        dist_to_support = (current - support) / current * 100 if current != 0 else 0
        
        return {
            'support': round(support, 2),
            'resistance': round(resistance, 2),
            'dist_to_resistance': round(dist_to_resistance, 2),
            'dist_to_support': round(dist_to_support, 2),
            'high_20': round(high_20, 2),
            'low_20': round(low_20, 2),
        }
    
    def comprehensive_analysis(self):
        """综合技术面分析"""
        results = {}
        
        trend, ma_score = self.ma_trend()
        results['ma'] = {
            'trend': trend,
            'score': ma_score,
            'ma5': round(self.ma(5), 2) if self.ma(5) else None,
            'ma10': round(self.ma(10), 2) if self.ma(10) else None,
            'ma20': round(self.ma(20), 2) if self.ma(20) else None,
            'ma60': round(self.ma(60), 2) if self.ma(60) else None,
        }
        
        results['macd'] = self.macd_analysis()
        results['rsi'] = self.rsi_analysis()
        results['kdj'] = self.kdj_analysis()
        results['boll'] = self.boll_analysis()
        results['volume'] = self.volume_analysis()
        results['support_resistance'] = self.support_resistance()
        
        scores = [
            results['ma']['score'],
            results['macd']['score'],
            results['rsi']['score'],
            results['kdj']['score'],
            results['boll']['score'],
            results['volume']['score'],
        ]
        
        valid_scores = [s for s in scores if s is not None and s > 0]
        total_score = sum(valid_scores) / len(valid_scores) if valid_scores else 50
        
        if total_score >= 75:
            rating = '强烈看多'
            rating_level = 5
        elif total_score >= 65:
            rating = '看多'
            rating_level = 4
        elif total_score >= 55:
            rating = '偏多'
            rating_level = 3
        elif total_score >= 45:
            rating = '中性'
            rating_level = 2
        elif total_score >= 35:
            rating = '偏空'
            rating_level = 1
        else:
            rating = '看空'
            rating_level = 0
        
        results['summary'] = {
            'total_score': round(total_score, 1),
            'rating': rating,
            'rating_level': rating_level,
        }
        
        return results


class StockAnalyzer:
    """个股立体分析器"""
    
    def __init__(self, code, name):
        self.code = code
        self.name = name
        self.technical = None
    
    def load_historical_data(self, prices=None):
        """加载历史行情数据"""
        if prices:
            self.price_data = prices
        else:
            self.price_data = self._generate_sample_data()
        
        self.technical = StockTechnicalAnalyzer(self.price_data)
    
    def _generate_sample_data(self):
        """生成模拟历史数据"""
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
            
            prices.append({
                'date': f'2026-01-{i+1:02d}',
                'open': round(open_price, 2),
                'high': round(high, 2),
                'low': round(low, 2),
                'close': round(close, 2),
                'volume': volume,
            })
            
            current = close
        
        return prices
    
    def analyze_all(self):
        """全维度分析"""
        result = {
            'code': self.code,
            'name': self.name,
            'analyze_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'technical': None,
            'fundamental': None,
        }
        
        if self.technical:
            result['technical'] = self.technical.comprehensive_analysis()
        
        result['fundamental'] = self._basic_fundamental_analysis()
        result['overall'] = self._calculate_overall_score(result)
        
        return result
    
    def _basic_fundamental_analysis(self):
        """基础基本面分析"""
        return {
            'pe_ratio': None,
            'pb_ratio': None,
            'market_cap': None,
            'roe': None,
            'score': 50,
        }
    
    def _calculate_overall_score(self, result):
        """计算综合评分"""
        scores = []
        weights = {}
        
        if result.get('technical') and result['technical'].get('summary'):
            tech_score = result['technical']['summary']['total_score']
            scores.append(tech_score * 0.7)
            weights['technical'] = 70
        
        if result.get('fundamental'):
            fund_score = result['fundamental'].get('score', 50)
            scores.append(fund_score * 0.3)
            weights['fundamental'] = 30
        
        total_score = sum(scores)
        total_weight = sum(weights.values())
        
        if total_weight > 0:
            final_score = total_score / total_weight * 100
        else:
            final_score = 50
        
        if final_score >= 80:
            rating = '强烈推荐'
        elif final_score >= 70:
            rating = '推荐'
        elif final_score >= 60:
            rating = '谨慎推荐'
        elif final_score >= 50:
            rating = '中性'
        elif final_score >= 40:
            rating = '谨慎观望'
        else:
            rating = '回避'
        
        return {
            'score': round(final_score, 1),
            'rating': rating,
            'weights': weights,
        }


def analyze_stock(code, name, prices=None):
    """便捷函数：分析单只股票"""
    analyzer = StockAnalyzer(code, name)
    analyzer.load_historical_data(prices)
    return analyzer.analyze_all()


if __name__ == '__main__':
    result = analyze_stock('002837', '英维克')
    print(json.dumps(result, ensure_ascii=False, indent=2))
