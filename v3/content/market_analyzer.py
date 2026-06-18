"""
市场分析引擎 - V4 内容层
统一的市场整体分析逻辑，包括指数、板块、情绪等

分析维度：
1. 指数行情 - 主要指数涨跌幅、成交额
2. 市场情绪 - 涨跌家数、涨停跌停、赚钱效应
3. 板块热点 - 涨幅居前板块、资金流向
4. 量能分析 - 成交额变化、量价配合
5. 操作策略 - 基于市场状况的策略建议
"""
import sys
import os
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, field
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from content.base import ContentModel, ContentAnalyzer, AnalysisDimension


@dataclass
class IndexInfo:
    """指数信息"""
    name: str
    code: str
    price: float
    change_pct: float
    volume: float = 0  # 成交额（亿）
    trend: str = ""  # 趋势：上涨/下跌/震荡


@dataclass
class SectorInfo:
    """板块信息"""
    name: str
    change_pct: float
    lead_stock: str = ""  # 龙头股
    reason: str = ""  # 上涨原因
    fund_flow: float = 0  # 资金流向（亿）


@dataclass
class MarketSentiment:
    """市场情绪"""
    up_count: int = 0  # 上涨家数
    down_count: int = 0  # 下跌家数
    limit_up: int = 0  # 涨停家数
    limit_down: int = 0  # 跌停家数
    total_volume: float = 0  # 总成交额（亿）
    sentiment_level: str = "中性"  # 情绪等级：恐慌/谨慎/中性/贪婪/狂热
    profit_effect: str = "一般"  # 赚钱效应：差/一般/好/极好


@dataclass
class MarketAnalysisResult(ContentModel):
    """市场分析结果"""
    indices: List[IndexInfo] = field(default_factory=list)
    hot_sectors: List[SectorInfo] = field(default_factory=list)
    sentiment: MarketSentiment = field(default_factory=MarketSentiment)
    market_trend: str = ""  # 市场整体趋势判断
    strategy_suggestion: str = ""  # 操作策略建议
    
    def to_dict(self) -> Dict:
        data = super().to_dict()
        data.update({
            'indices': [i.__dict__ for i in self.indices],
            'hot_sectors': [s.__dict__ for s in self.hot_sectors],
            'sentiment': self.sentiment.__dict__,
            'market_trend': self.market_trend,
            'strategy_suggestion': self.strategy_suggestion,
        })
        return data


class MarketAnalyzer(ContentAnalyzer):
    """市场分析器
    
    统一市场分析口径，所有页面的市场分析都通过此引擎生成。
    """
    
    def __init__(self, data_dir: str = "data"):
        super().__init__()
        self.data_dir = data_dir
        self.market_data = None
        self.result: Optional[MarketAnalysisResult] = None
    
    def _load_data(self):
        """加载市场数据"""
        import json
        
        # 尝试多种路径
        possible_paths = [
            os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '..', '..', self.data_dir, 'market.json'),
            os.path.join(os.getcwd(), self.data_dir, 'market.json'),
            '/app/data/所有对话/主对话/data/market.json',
        ]
        
        data_path = None
        for path in possible_paths:
            path = os.path.normpath(path)
            if os.path.exists(path):
                data_path = path
                break
        
        if not data_path:
            raise FileNotFoundError(f"找不到市场数据文件")
        
        with open(data_path, 'r', encoding='utf-8') as f:
            self.market_data = json.load(f)
    
    def analyze(self) -> MarketAnalysisResult:
        """执行市场分析"""
        if not self.market_data:
            self._load_data()
        
        market_data = self.market_data.get('market_data', {})
        indices_data = self.market_data.get('indices', [])
        sectors_data = self.market_data.get('hot_sectors', [])
        update_time = self.market_data.get('update_time', '')
        
        # 解析指数
        indices = []
        for idx in indices_data:
            index = IndexInfo(
                name=idx.get('name', ''),
                code=idx.get('code', ''),
                price=float(idx.get('price', 0)),
                change_pct=float(idx.get('change_pct', 0)) * 100,  # 转换为百分比
            )
            # 判断趋势
            if index.change_pct > 1:
                index.trend = "上涨"
            elif index.change_pct < -1:
                index.trend = "下跌"
            else:
                index.trend = "震荡"
            indices.append(index)
        
        # 解析热门板块
        hot_sectors = []
        for sec in sectors_data[:10]:  # 取前10个
            sector = SectorInfo(
                name=sec.get('name', ''),
                change_pct=float(sec.get('change_pct', 0)) * 100 if sec.get('change_pct', 0) <= 1 else float(sec.get('change_pct', 0)),
                lead_stock=sec.get('lead_stock', ''),
                reason=sec.get('reason', ''),
            )
            hot_sectors.append(sector)
        
        # 计算市场情绪
        sentiment = self._calculate_sentiment(market_data, indices)
        
        # 判断市场趋势
        market_trend = self._judge_market_trend(indices, sentiment)
        
        # 生成策略建议
        strategy = self._generate_strategy(market_trend, sentiment, hot_sectors)
        
        # 构建分析维度
        self._build_dimensions(indices, hot_sectors, sentiment)
        
        # 计算深度评分
        depth_score = self.calculate_depth_score()
        
        result = MarketAnalysisResult(
            title="市场整体分析",
            summary=f"{market_trend}，{sentiment.sentiment_level}情绪，策略：{strategy[:50]}",
            depth_score=depth_score,
            data_quality=80.0,
            update_time=update_time or datetime.now().strftime('%Y-%m-%d %H:%M'),
            source="腾讯财经实时行情 + 东方财富板块数据",
            indices=indices,
            hot_sectors=hot_sectors,
            sentiment=sentiment,
            market_trend=market_trend,
            strategy_suggestion=strategy,
        )
        
        self.result = result
        self._analysis_done = True
        return result
    
    def _calculate_sentiment(self, market_data: Dict, indices: List[IndexInfo]) -> MarketSentiment:
        """计算市场情绪"""
        sentiment = MarketSentiment()
        
        # 涨跌家数
        sentiment.up_count = int(market_data.get('up_count', 0))
        sentiment.down_count = int(market_data.get('down_count', 0))
        sentiment.limit_up = int(market_data.get('limit_up', 0))
        sentiment.limit_down = int(market_data.get('limit_down', 0))
        sentiment.total_volume = float(market_data.get('total_volume', 0))
        
        # 计算情绪等级
        total = sentiment.up_count + sentiment.down_count
        if total == 0:
            up_ratio = 0.5
        else:
            up_ratio = sentiment.up_count / total
        
        if up_ratio > 0.8 and sentiment.limit_up > 100:
            sentiment.sentiment_level = "狂热"
        elif up_ratio > 0.7:
            sentiment.sentiment_level = "贪婪"
        elif up_ratio > 0.55:
            sentiment.sentiment_level = "偏多"
        elif up_ratio > 0.45:
            sentiment.sentiment_level = "中性"
        elif up_ratio > 0.3:
            sentiment.sentiment_level = "谨慎"
        else:
            sentiment.sentiment_level = "恐慌"
        
        # 赚钱效应
        if up_ratio > 0.7 and sentiment.limit_up > 80:
            sentiment.profit_effect = "极好"
        elif up_ratio > 0.6:
            sentiment.profit_effect = "好"
        elif up_ratio > 0.4:
            sentiment.profit_effect = "一般"
        else:
            sentiment.profit_effect = "差"
        
        return sentiment
    
    def _judge_market_trend(self, indices: List[IndexInfo], sentiment: MarketSentiment) -> str:
        """判断市场整体趋势"""
        if not indices:
            return "震荡"
        
        # 计算主要指数的平均涨幅
        main_indices = [i for i in indices if i.name in ['上证指数', '深证成指', '创业板指']]
        if not main_indices:
            main_indices = indices[:3]
        
        avg_change = sum(i.change_pct for i in main_indices) / len(main_indices)
        
        if avg_change > 2:
            trend = "大幅上涨"
        elif avg_change > 1:
            trend = "上涨"
        elif avg_change > 0.3:
            trend = "小幅上涨"
        elif avg_change > -0.3:
            trend = "震荡整理"
        elif avg_change > -1:
            trend = "小幅下跌"
        elif avg_change > -2:
            trend = "下跌"
        else:
            trend = "大幅下跌"
        
        return trend
    
    def _generate_strategy(self, trend: str, sentiment: MarketSentiment, sectors: List[SectorInfo]) -> str:
        """生成操作策略建议"""
        parts = []
        
        # 基于趋势的仓位建议
        if "上涨" in trend:
            parts.append("市场偏强，可保持适度仓位")
        elif "下跌" in trend:
            parts.append("市场偏弱，注意控制仓位，谨慎追高")
        else:
            parts.append("震荡行情，高抛低吸为主")
        
        # 基于情绪的操作建议
        if sentiment.sentiment_level in ["狂热", "贪婪"]:
            parts.append("情绪偏热，注意追高风险")
        elif sentiment.sentiment_level in ["恐慌", "谨慎"]:
            parts.append("情绪偏冷，可关注错杀机会")
        
        # 热门板块建议
        if sectors:
            top_sectors = [s.name for s in sectors[:3]]
            parts.append(f"关注方向：{'、'.join(top_sectors)}")
        
        return "；".join(parts) + "。"
    
    def _build_dimensions(self, indices: List[IndexInfo], sectors: List[SectorInfo], sentiment: MarketSentiment):
        """构建分析维度"""
        self.dimensions = []
        
        # 维度1：指数行情
        idx_score = 85 if len(indices) >= 4 else 65
        self.add_dimension(AnalysisDimension(
            name="指数行情",
            weight=1.5,
            content=f"覆盖{len(indices)}个主要指数，包含价格、涨跌幅、趋势判断",
            score=idx_score,
            details={'index_count': len(indices)}
        ))
        
        # 维度2：市场情绪
        sent_score = 80 if sentiment.up_count > 0 else 40
        self.add_dimension(AnalysisDimension(
            name="市场情绪",
            weight=2.0,
            content=f"涨跌家数对比：{sentiment.up_count}/{sentiment.down_count}，情绪等级：{sentiment.sentiment_level}，赚钱效应：{sentiment.profit_effect}",
            score=sent_score,
            details={
                'up_count': sentiment.up_count,
                'down_count': sentiment.down_count,
                'limit_up': sentiment.limit_up,
                'limit_down': sentiment.limit_down,
            }
        ))
        
        # 维度3：板块热点
        sec_score = 75 if len(sectors) >= 5 else 50
        self.add_dimension(AnalysisDimension(
            name="板块热点",
            weight=1.5,
            content=f"覆盖{len(sectors)}个热门板块，包含涨幅、龙头股、上涨逻辑",
            score=sec_score,
            details={'sector_count': len(sectors)}
        ))
        
        # 维度4：量能分析
        vol_score = 70 if sentiment.total_volume > 0 else 30
        self.add_dimension(AnalysisDimension(
            name="量能分析",
            weight=1.0,
            content=f"两市成交额{sentiment.total_volume:.1f}亿元" if sentiment.total_volume > 0 else "成交额数据暂缺",
            score=vol_score,
            details={'total_volume': sentiment.total_volume}
        ))
        
        # 维度5：操作策略
        strat_score = 80
        self.add_dimension(AnalysisDimension(
            name="操作策略",
            weight=1.8,
            content="基于市场趋势、情绪、板块热点的综合策略建议",
            score=strat_score,
            details={}
        ))


def get_market_analysis(data_dir: str = "data") -> MarketAnalysisResult:
    """便捷函数：获取市场分析结果
    
    Args:
        data_dir: 数据目录路径
        
    Returns:
        MarketAnalysisResult: 市场分析结果
    """
    analyzer = MarketAnalyzer(data_dir=data_dir)
    return analyzer.analyze()


if __name__ == "__main__":
    # 测试
    result = get_market_analysis(data_dir="data")
    print(f"✅ 市场分析完成，深度评分：{result.depth_score}分")
    print(f"   市场趋势：{result.market_trend}")
    print(f"   情绪等级：{result.sentiment.sentiment_level}")
    print(f"   赚钱效应：{result.sentiment.profit_effect}")
    print(f"   涨跌家数：{result.sentiment.up_count}/{result.sentiment.down_count}")
    print(f"   主要指数：")
    for idx in result.indices[:4]:
        print(f"     - {idx.name}: {idx.price:.2f}点, {idx.change_pct:+.2f}%, {idx.trend}")
    print(f"   热门板块TOP5：")
    for sec in result.hot_sectors[:5]:
        print(f"     - {sec.name}: {sec.change_pct:+.2f}%")
    print(f"   策略建议：{result.strategy_suggestion}")
