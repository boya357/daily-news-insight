"""
boya投资策略引擎 - 核心分析引擎
将boya的投资体系（龙空龙、止损纪律、主线思维）编码为可复用的分析模块

核心能力：
1. 主线评级体系 - 量化评估题材级别
2. 龙头梯队识别 - 龙空龙策略标的筛选
3. 买点评级 - 技术面+情绪面买点判断
4. 止损纪律 - 动态止损位计算
5. 弹性测算 - 空间/风险/盈亏比评估
6. 组合影响分析 - 结合现有持仓的风险评估
7. 预判记录系统 - 预判-验证-复盘闭环
"""

import json
from pathlib import Path
from datetime import datetime, timedelta
from typing import List, Dict, Optional, Tuple
from dataclasses import dataclass, asdict


BASE_DIR = Path(__file__).resolve().parent.parent.parent
DATA_DIR = BASE_DIR / 'data'


# ========== 数据结构 ==========

@dataclass
class MainThemeRating:
    """主线评级"""
    level: str  # S/A/B/C
    score: float  # 0-100
    dimensions: Dict[str, float]  # 各维度得分
    summary: str


@dataclass
class DragonTroupe:
    """龙头梯队"""
    dragon_one: Dict  # 龙一
    dragon_two: Dict  # 龙二
    dragon_three: Dict  # 龙三
    rationale: str  # 梯队逻辑


@dataclass
class BuyPointRating:
    """买点评级"""
    score: float  # 0-100
    level: str  # 强烈推荐/谨慎追高/观望/回避
    suggest_price: Optional[float]  # 建议买入价
    support_level: Optional[float]  # 支撑位
    rationale: str


@dataclass
class StopLossConfig:
    """止损配置"""
    fixed_stop_pct: float  # 固定止损比例
    ma_stop: Optional[int]  # 均线止损（日均线）
    position_limit_pct: float  # 单票仓位上限
    rationale: str


@dataclass
class FlexibilityCalc:
    """弹性测算"""
    short_term_upside: float  # 短期上涨空间 %
    mid_term_upside: float  # 中期上涨空间 %
    drawdown_risk: float  # 回调风险 %
    risk_reward_ratio: float  # 盈亏比
    rationale: str


@dataclass
class PortfolioImpact:
    """组合影响分析"""
    concentration_risk: str  # 集中度风险
    correlation_risk: str  # 相关性风险
    suggestion: str  # 操作建议


@dataclass
class PredictionRecord:
    """预判记录"""
    id: str
    content: str
    confidence: float  # 0-1
    verify_date: str  # 验证日期
    category: str  # 分类
    status: str = 'pending'  # pending/right/wrong/partial
    result_note: str = ''


@dataclass
class BoyaStrategyReport:
    """boya策略完整报告"""
    theme_rating: MainThemeRating
    dragon_troupe: DragonTroupe
    buy_point: BuyPointRating
    stop_loss: StopLossConfig
    flexibility: FlexibilityCalc
    portfolio: PortfolioImpact
    predictions: List[PredictionRecord]
    chapter_perspectives: Dict[str, str]  # 各章节视角批注


# ========== 主线评级引擎 ==========

class MainThemeRater:
    """主线评级引擎 - 五维量化评分"""
    
    DIMENSIONS = {
        'catalyst_density': {'name': '催化密度', 'weight': 0.25},
        'capital_focus': {'name': '资金关注度', 'weight': 0.25},
        'performance_realization': {'name': '业绩兑现度', 'weight': 0.20},
        'policy_friendliness': {'name': '政策友好度', 'weight': 0.15},
        'story_telling': {'name': '故事想象空间', 'weight': 0.15},
    }
    
    @classmethod
    def rate(cls, theme_data: Dict) -> MainThemeRating:
        """
        对题材进行主线评级
        
        theme_data 包含:
        - catalyst_count: 近期催化事件数量
        - volume_ratio: 板块成交额占比
        - leader_gain: 龙头累计涨幅
        - pe_ttm: 板块PE
        - policy_support: 政策支持力度 0-10
        - market_space: 市场空间描述
        """
        scores = {}
        
        # 催化密度评分
        catalyst_count = theme_data.get('catalyst_count', 0)
        if catalyst_count >= 10:
            scores['catalyst_density'] = 95
        elif catalyst_count >= 7:
            scores['catalyst_density'] = 80
        elif catalyst_count >= 5:
            scores['catalyst_density'] = 65
        elif catalyst_count >= 3:
            scores['catalyst_density'] = 50
        else:
            scores['catalyst_density'] = 30
        
        # 资金关注度评分
        volume_ratio = theme_data.get('volume_ratio', 0)
        if volume_ratio >= 0.15:  # 占全市场15%以上
            scores['capital_focus'] = 95
        elif volume_ratio >= 0.10:
            scores['capital_focus'] = 80
        elif volume_ratio >= 0.07:
            scores['capital_focus'] = 65
        elif volume_ratio >= 0.04:
            scores['capital_focus'] = 50
        else:
            scores['capital_focus'] = 30
        
        # 业绩兑现度评分
        leader_gain = theme_data.get('leader_gain', 0)
        pe_ttm = theme_data.get('pe_ttm', 50)
        if pe_ttm <= 30 and leader_gain > 50:
            scores['performance_realization'] = 85
        elif pe_ttm <= 50:
            scores['performance_realization'] = 65
        elif pe_ttm <= 80:
            scores['performance_realization'] = 45
        else:
            scores['performance_realization'] = 25
        
        # 政策友好度评分
        policy_support = theme_data.get('policy_support', 5)
        scores['policy_friendliness'] = policy_support * 10
        
        # 故事想象空间评分
        market_space = theme_data.get('market_space', '')
        if '万亿' in market_space or '千亿级' in market_space:
            scores['story_telling'] = 90
        elif '百亿' in market_space:
            scores['story_telling'] = 70
        elif '数十' in market_space:
            scores['story_telling'] = 50
        else:
            scores['story_telling'] = 40
        
        # 计算加权总分
        total_score = 0
        for dim, info in cls.DIMENSIONS.items():
            total_score += scores.get(dim, 0) * info['weight']
        
        # 评级
        if total_score >= 85:
            level = 'S'
        elif total_score >= 70:
            level = 'A'
        elif total_score >= 55:
            level = 'B'
        elif total_score >= 40:
            level = 'C'
        else:
            level = 'D'
        
        summary = f"{level}级主线题材，综合评分{total_score:.1f}分。"
        if level == 'S':
            summary += "市场核心主线，资金高度共识，催化剂密集。"
        elif level == 'A':
            summary += "重要主线级别，关注度较高，有持续性机会。"
        elif level == 'B':
            summary += "支线级别，波动较大，适合波段操作。"
        else:
            summary += "非主流题材，以个股行情为主。"
        
        return MainThemeRating(
            level=level,
            score=round(total_score, 1),
            dimensions=scores,
            summary=summary
        )


# ========== 龙头梯队识别 ==========

class DragonTroupeIdentifier:
    """龙头梯队识别器 - 龙空龙策略核心"""
    
    @classmethod
    def identify(cls, stocks: List[Dict]) -> DragonTroupe:
        """
        从标的池中识别龙一龙二龙三
        
        选股标准（按优先级）：
        1. 最先涨停/连板数最多
        2. 市值适中（50-500亿最优）
        3. 股性活跃（历史涨停次数多）
        4. 题材正宗度
        5. 资金认可度（成交额/换手率）
        """
        # 计算每个标的的龙头评分
        scored_stocks = []
        for stock in stocks:
            score = 0
            
            # 连板数/涨幅（权重最高）
            gain = stock.get('gain', 0)
            limit_up_count = stock.get('limit_up_count', 0)
            if limit_up_count >= 5:
                score += 40
            elif limit_up_count >= 3:
                score += 35
            elif limit_up_count >= 2:
                score += 30
            elif gain > 20:  # 累计涨幅
                score += 25
            elif gain > 10:
                score += 20
            else:
                score += 15
            
            # 市值评分
            market_cap = stock.get('market_cap', 100)
            if 50 <= market_cap <= 200:
                score += 20  # 最优区间
            elif 200 < market_cap <= 500:
                score += 15
            elif market_cap < 50:
                score += 10
            else:
                score += 5
            
            # 股性评分
            turnover_rate = stock.get('turnover_rate', 5)
            if turnover_rate >= 20:
                score += 15
            elif turnover_rate >= 10:
                score += 12
            elif turnover_rate >= 5:
                score += 8
            else:
                score += 4
            
            # 题材正宗度
            purity = stock.get('theme_purity', 0.5)
            score += purity * 15
            
            # 资金认可度
            volume = stock.get('volume', 0)
            if volume > 50:  # 50亿以上
                score += 10
            elif volume > 20:
                score += 8
            elif volume > 10:
                score += 5
            else:
                score += 2
            
            scored_stocks.append({**stock, 'dragon_score': score})
        
        # 按龙头评分排序
        scored_stocks.sort(key=lambda x: x['dragon_score'], reverse=True)
        
        dragon_one = scored_stocks[0] if len(scored_stocks) > 0 else {}
        dragon_two = scored_stocks[1] if len(scored_stocks) > 1 else {}
        dragon_three = scored_stocks[2] if len(scored_stocks) > 2 else {}
        
        rationale = (
            f"龙一【{dragon_one.get('name', '')}】："
            f"累计涨幅{dragon_one.get('gain', 0):.1f}%，"
            f"题材正宗度{dragon_one.get('theme_purity', 0)*100:.0f}%。"
        )
        
        return DragonTroupe(
            dragon_one=dragon_one,
            dragon_two=dragon_two,
            dragon_three=dragon_three,
            rationale=rationale
        )


# ========== 买点评级引擎 ==========

class BuyPointAnalyzer:
    """买点评级引擎"""
    
    @classmethod
    def analyze(cls, stock_data: Dict, theme_rating: MainThemeRating) -> BuyPointRating:
        """
        分析买入时机
        
        stock_data包含:
        - current_price: 当前价格
        - ma5/ma10/ma20/ma60: 各均线价格
        - rsi: RSI指标
        - recent_gain: 近期涨幅
        - volume_ratio: 量比
        """
        score = 50  # 基准分
        
        current_price = stock_data.get('current_price', 0)
        ma10 = stock_data.get('ma10', 0)
        ma20 = stock_data.get('ma20', 0)
        rsi = stock_data.get('rsi', 50)
        recent_gain = stock_data.get('recent_gain', 0)
        volume_ratio = stock_data.get('volume_ratio', 1)
        
        # 均线位置评分
        if ma10 and current_price <= ma10 * 1.02:  # 在10均线附近或下方
            score += 15
        elif current_price <= ma10 * 1.05:
            score += 8
        elif current_price > ma10 * 1.15:
            score -= 10
        
        # RSI评分
        if 30 <= rsi <= 50:
            score += 15
        elif rsi < 30:
            score += 10  # 超卖，但要警惕
        elif 50 < rsi <= 70:
            score += 5
        elif rsi > 80:
            score -= 15
        
        # 近期涨幅评分（涨太多的减分）
        if recent_gain > 50:
            score -= 15
        elif recent_gain > 30:
            score -= 8
        elif recent_gain < -15:
            score += 10  # 回调充分
        elif recent_gain < -5:
            score += 5
        
        # 量比评分
        if 0.8 <= volume_ratio <= 1.5:
            score += 5  # 量能平稳
        elif volume_ratio > 2:
            score -= 5  # 放量过猛
        
        # 主线级别加分
        theme_bonus = {'S': 20, 'A': 12, 'B': 5, 'C': 0, 'D': -5}
        score += theme_bonus.get(theme_rating.level, 0)
        
        # 评级
        if score >= 80:
            level = '强烈推荐'
        elif score >= 65:
            level = '谨慎追高'
        elif score >= 50:
            level = '观望为主'
        elif score >= 35:
            level = '建议回避'
        else:
            level = '坚决不碰'
        
        # 建议买入价（10均线附近）
        suggest_price = ma10 if ma10 else None
        
        # 支撑位（20均线）
        support_level = ma20 if ma20 else None
        
        rationale = f"买点评分{score:.0f}分，{level}。"
        if suggest_price:
            rationale += f"建议在{suggest_price:.2f}元附近（10日均线）低吸。"
        if support_level:
            rationale += f"第一支撑位{support_level:.2f}元。"
        
        return BuyPointRating(
            score=round(score, 1),
            level=level,
            suggest_price=round(suggest_price, 2) if suggest_price else None,
            support_level=round(support_level, 2) if support_level else None,
            rationale=rationale
        )


# ========== 止损纪律引擎 ==========

class StopLossEngine:
    """止损纪律引擎 - 严格执行铁律"""
    
    @classmethod
    def calculate(cls, stock_data: Dict, theme_rating: MainThemeRating) -> StopLossConfig:
        """
        计算止损配置
        
        铁律：
        1. 单票仓位不超过25%
        2. 龙头股10%固定止损/趋势股20日均线
        3. 破位必须无条件执行
        """
        # 固定止损比例
        if theme_rating.level in ['S', 'A']:
            fixed_stop_pct = 10.0  # 主线龙头容忍度高一些
        else:
            fixed_stop_pct = 8.0
        
        # 均线止损
        stock_type = stock_data.get('type', 'trend')  # leader/trend
        if stock_type == 'leader':
            ma_stop = 20  # 龙头看20日线
        else:
            ma_stop = 30  # 趋势股看30日线
        
        # 仓位限制
        if theme_rating.level == 'S':
            position_limit_pct = 25
        elif theme_rating.level == 'A':
            position_limit_pct = 20
        elif theme_rating.level == 'B':
            position_limit_pct = 15
        else:
            position_limit_pct = 10
        
        rationale = (
            f"{fixed_stop_pct}%铁律止损，{ma_stop}日均线趋势止损。"
            f"单票仓位上限{position_limit_pct}%。"
            f"破位必须无条件执行，绝不抱有侥幸心理。"
        )
        
        return StopLossConfig(
            fixed_stop_pct=fixed_stop_pct,
            ma_stop=ma_stop,
            position_limit_pct=position_limit_pct,
            rationale=rationale
        )


# ========== 弹性测算引擎 ==========

class FlexibilityCalculator:
    """弹性测算引擎 - 空间/风险/盈亏比"""
    
    @classmethod
    def calculate(cls, stock_data: Dict, theme_data: Dict) -> FlexibilityCalc:
        """计算上涨空间与风险"""
        
        current_price = stock_data.get('current_price', 1)
        target_price_short = stock_data.get('target_price_short', current_price * 1.2)
        target_price_mid = stock_data.get('target_price_mid', current_price * 1.5)
        support_price = stock_data.get('support_price', current_price * 0.85)
        
        # 短期上涨空间
        short_term_upside = round((target_price_short - current_price) / current_price * 100, 1)
        
        # 中期上涨空间
        mid_term_upside = round((target_price_mid - current_price) / current_price * 100, 1)
        
        # 回调风险（到支撑位的跌幅）
        drawdown_risk = round((current_price - support_price) / current_price * 100, 1)
        
        # 盈亏比（中期空间 / 回调风险）
        if drawdown_risk > 0:
            risk_reward_ratio = round(mid_term_upside / drawdown_risk, 2)
        else:
            risk_reward_ratio = 1.0
        
        rationale = (
            f"短期上涨空间{short_term_upside}%，中期上涨空间{mid_term_upside}%，"
            f"回调风险{drawdown_risk}%，盈亏比{risk_reward_ratio}:1。"
        )
        if risk_reward_ratio >= 3:
            rationale += "盈亏比优秀，值得布局。"
        elif risk_reward_ratio >= 2:
            rationale += "盈亏比尚可，可轻仓参与。"
        else:
            rationale += "盈亏比不佳，谨慎参与。"
        
        return FlexibilityCalc(
            short_term_upside=short_term_upside,
            mid_term_upside=mid_term_upside,
            drawdown_risk=drawdown_risk,
            risk_reward_ratio=risk_reward_ratio,
            rationale=rationale
        )


# ========== 组合影响分析 ==========

class PortfolioImpactAnalyzer:
    """组合影响分析"""
    
    @classmethod
    def analyze(cls, new_stock: Dict, holdings: List[Dict], theme_data: Dict) -> PortfolioImpact:
        """
        分析新标的对现有组合的影响
        
        holdings: 现有持仓列表
        """
        # 计算同题材集中度
        same_theme_count = 0
        total_position = 0
        same_theme_position = 0
        
        theme_name = theme_data.get('name', '')
        
        for holding in holdings:
            position_pct = holding.get('position_pct', 0)
            total_position += position_pct
            
            holding_theme = holding.get('theme', '')
            if theme_name in holding_theme or holding_theme in theme_name:
                same_theme_count += 1
                same_theme_position += position_pct
        
        # 集中度风险
        if same_theme_position >= 50:
            concentration_risk = '高'
            concentration_detail = f"同题材仓位已达{same_theme_position:.1f}%，集中度风险较高"
        elif same_theme_position >= 30:
            concentration_risk = '中'
            concentration_detail = f"同题材仓位{same_theme_position:.1f}%，集中度适中"
        else:
            concentration_risk = '低'
            concentration_detail = f"同题材仓位仅{same_theme_position:.1f}%，分散度良好"
        
        # 相关性风险（简化：同行业数量）
        if same_theme_count >= 3:
            correlation_risk = '较高'
        elif same_theme_count >= 2:
            correlation_risk = '中等'
        else:
            correlation_risk = '较低'
        
        # 操作建议
        if concentration_risk == '高':
            suggestion = '建议控制仓位，避免同一题材过度集中。可考虑分批减仓涨幅较大的持仓。'
        elif concentration_risk == '中':
            suggestion = '仓位适中，可正常配置，但需密切关注板块整体风险。'
        else:
            suggestion = '组合分散度良好，可积极配置主线标的。'
        
        return PortfolioImpact(
            concentration_risk=f"{concentration_risk}（{concentration_detail}）",
            correlation_risk=correlation_risk,
            suggestion=suggestion
        )


# ========== 预判记录系统 ==========

class PredictionTracker:
    """预判追踪系统 - 预判-验证-复盘闭环"""
    
    def __init__(self, record_file: str = None):
        if record_file:
            self.record_file = Path(record_file)
        else:
            self.record_file = DATA_DIR / 'predictions.json'
        self.predictions: List[PredictionRecord] = []
        self._load()
    
    def _load(self):
        if self.record_file.exists():
            try:
                with open(self.record_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                self.predictions = [PredictionRecord(**item) for item in data]
            except Exception:
                self.predictions = []
    
    def _save(self):
        self.record_file.parent.mkdir(parents=True, exist_ok=True)
        with open(self.record_file, 'w', encoding='utf-8') as f:
            json.dump(
                [asdict(p) for p in self.predictions],
                f, ensure_ascii=False, indent=2
            )
    
    def add_prediction(self, content: str, confidence: float, 
                       verify_days: int, category: str = 'general') -> PredictionRecord:
        """添加一条预判"""
        pred_id = f"pred_{datetime.now().strftime('%Y%m%d%H%M%S')}"
        verify_date = (datetime.now() + timedelta(days=verify_days)).strftime('%Y-%m-%d')
        
        pred = PredictionRecord(
            id=pred_id,
            content=content,
            confidence=confidence,
            verify_date=verify_date,
            category=category,
            status='pending'
        )
        self.predictions.append(pred)
        self._save()
        return pred
    
    def get_pending_predictions(self) -> List[PredictionRecord]:
        """获取待验证的预判"""
        return [p for p in self.predictions if p.status == 'pending']
    
    def verify_prediction(self, pred_id: str, status: str, note: str = ''):
        """验证预判结果"""
        for pred in self.predictions:
            if pred.id == pred_id:
                pred.status = status
                pred.result_note = note
                self._save()
                return True
        return False
    
    def get_accuracy_rate(self) -> Dict:
        """统计准确率"""
        verified = [p for p in self.predictions if p.status != 'pending']
        if not verified:
            return {'total': 0, 'right': 0, 'wrong': 0, 'partial': 0, 'accuracy': 0}
        
        right = sum(1 for p in verified if p.status == 'right')
        wrong = sum(1 for p in verified if p.status == 'wrong')
        partial = sum(1 for p in verified if p.status == 'partial')
        
        accuracy = right / len(verified) * 100
        
        return {
            'total': len(verified),
            'right': right,
            'wrong': wrong,
            'partial': partial,
            'accuracy': round(accuracy, 1)
        }


# ========== 统一策略分析门面 ==========

class BoyaStrategyEngine:
    """boya策略引擎 - 统一入口"""
    
    def __init__(self, holdings: List[Dict] = None):
        self.holdings = holdings or []
        self.prediction_tracker = PredictionTracker()
    
    def analyze_theme(self, theme_data: Dict, stocks: List[Dict], 
                     target_stock: Dict = None) -> BoyaStrategyReport:
        """
        完整分析一个主题投资机会
        
        Args:
            theme_data: 主题数据
            stocks: 相关标的列表
            target_stock: 重点分析标的（可选，默认龙一）
        """
        # 1. 主线评级
        theme_rating = MainThemeRater.rate(theme_data)
        
        # 2. 龙头梯队
        dragon_troupe = DragonTroupeIdentifier.identify(stocks)
        
        # 确定重点分析标的
        if target_stock is None:
            target_stock = dragon_troupe.dragon_one
        
        # 3. 买点评级
        buy_point = BuyPointAnalyzer.analyze(target_stock, theme_rating)
        
        # 4. 止损纪律
        stop_loss = StopLossEngine.calculate(target_stock, theme_rating)
        
        # 5. 弹性测算
        flexibility = FlexibilityCalculator.calculate(target_stock, theme_data)
        
        # 6. 组合影响
        portfolio = PortfolioImpactAnalyzer.analyze(target_stock, self.holdings, theme_data)
        
        # 7. 生成预判（自动生成3条核心预判）
        predictions = self._generate_predictions(theme_data, theme_rating, dragon_troupe)
        
        return BoyaStrategyReport(
            theme_rating=theme_rating,
            dragon_troupe=dragon_troupe,
            buy_point=buy_point,
            stop_loss=stop_loss,
            flexibility=flexibility,
            portfolio=portfolio,
            predictions=predictions,
            chapter_perspectives={}
        )
    
    def _generate_predictions(self, theme_data: Dict, theme_rating: MainThemeRating,
                              dragon_troupe: DragonTroupe) -> List[PredictionRecord]:
        """自动生成核心预判"""
        predictions = []
        theme_name = theme_data.get('name', '该题材')
        dragon_name = dragon_troupe.dragon_one.get('name', '龙头')
        
        # 预判1：短期走势（T+2）
        if theme_rating.level in ['S', 'A']:
            pred1 = self.prediction_tracker.add_prediction(
                content=f"{theme_name}主线持续活跃，{dragon_name}短期内有望继续创新高",
                confidence=0.75 if theme_rating.level == 'S' else 0.6,
                verify_days=2,
                category='短期走势'
            )
        else:
            pred1 = self.prediction_tracker.add_prediction(
                content=f"{theme_name}板块短期震荡为主，关注资金承接力度",
                confidence=0.6,
                verify_days=2,
                category='短期走势'
            )
        predictions.append(pred1)
        
        # 预判2：中期趋势（T+5）
        pred2 = self.prediction_tracker.add_prediction(
            content=f"{theme_name}中期趋势向好，催化剂持续释放将推动板块估值重塑",
            confidence=0.7,
            verify_days=5,
            category='中期趋势'
        )
        predictions.append(pred2)
        
        # 预判3：龙头表现（T+3）
        pred3 = self.prediction_tracker.add_prediction(
            content=f"{dragon_name}作为板块龙头，资金认可度高，有望走出独立行情",
            confidence=0.65,
            verify_days=3,
            category='龙头表现'
        )
        predictions.append(pred3)
        
        return predictions
    
    def generate_chapter_perspective(self, chapter_title: str, 
                                     chapter_content: str, theme_rating: MainThemeRating) -> str:
        """
        生成章节视角批注（给报告每个章节加boya视角点评）
        这是一个简化版本，实际使用时可结合LLM做深度解读
        """
        # 简化处理：根据章节类型生成对应的视角批注
        perspectives = {
            '市场规模': f"从资金容量角度看，这个市场规模足以支撑{theme_rating.level}级主线行情。大资金进出方便，不容易被操纵。",
            '产业链': '产业链上下游的利润分配格局，决定了哪个环节最有弹性。重点关注供需最紧张、议价能力最强的环节。',
            '竞争格局': '竞争格局决定了利润率和持续性。龙头溢价、老二喝汤、老三以后没肉吃，这是A股不变的规律。',
            '技术趋势': '技术路线的变化是最大的α来源。押对技术路线的公司会获得超额收益，押错的会被快速淘汰。',
            '政策环境': '政策是A股最大的β。政策支持的方向，哪怕暂时没业绩，也能炒出几倍行情；政策打压的方向，再便宜也不能碰。',
            '投资机会': '机会是给有准备的人的。但不是所有机会都值得参与，要学会放弃看不懂的钱，只赚自己能力圈里的钱。',
            '风险提示': '风险永远放在第一位。单笔交易可以亏，但不能亏得不明不白。止损纪律是保命的底线。',
            '重点公司': '龙空龙策略的核心是只做龙头。杂毛涨的时候慢，跌的时候快，性价比极低。宁可错过，不可做错。',
        }
        
        # 匹配章节关键词
        for keyword, perspective in perspectives.items():
            if keyword in chapter_title:
                return perspective
        
        # 默认视角
        return f"从{theme_rating.level}级主线的角度看，这部分内容是板块投资逻辑的重要组成部分，需要重点关注核心受益标的。"
