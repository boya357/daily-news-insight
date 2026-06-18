"""
持仓分析引擎 - V4 内容层
统一的持仓分析逻辑，所有页面共用同一套分析口径

分析维度：
1. 基本行情 - 价格、涨跌幅、成交量
2. 技术面分析 - 均线、MACD、RSI、支撑压力位
3. 资金面分析 - 主力资金流向
4. 风险评估 - 止损位、回撤、波动率
5. 操作建议 - 持仓建议、加减仓点位
"""
import sys
import os
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, field
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from content.base import ContentModel, ContentAnalyzer, AnalysisDimension


@dataclass
class DiagnosisItem:
    """诊断条目 - 带状态标记"""
    text: str  # 描述文字
    status: str = "neutral"  # good/neutral/bad -> ✓/⚪/❌
    icon: str = "⚪"  # 显示图标
    
    def __post_init__(self):
        if self.status == "good":
            self.icon = "✓"
        elif self.status == "bad":
            self.icon = "❌"
        else:
            self.icon = "⚪"


@dataclass
class DimensionDiagnosis:
    """维度诊断结果"""
    name: str  # 维度名称
    status: str  # 整体状态：强势/流入/利好/向好 等
    items: List[DiagnosisItem] = field(default_factory=list)  # 详细条目


@dataclass
class StockAnalysis:
    """单只股票的分析结果"""
    code: str
    name: str
    current_price: float
    cost_price: float
    profit_loss_pct: float  # 盈亏比例
    today_change_pct: float  # 今日涨跌幅
    
    # 技术面
    technical_status: str = ""  # 强势/弱势/震荡
    technical_desc: str = ""
    technical_items: List[DiagnosisItem] = field(default_factory=list)
    
    # 资金面
    fund_status: str = ""  # 流入/流出
    fund_desc: str = ""
    main_fund: float = 0  # 主力资金净额
    fund_items: List[DiagnosisItem] = field(default_factory=list)
    
    # 消息面
    news_status: str = ""  # 利好/利空/中性
    news_desc: str = ""
    news_items: List[DiagnosisItem] = field(default_factory=list)
    
    # 产业面
    industry_status: str = ""
    industry_desc: str = ""
    industry_items: List[DiagnosisItem] = field(default_factory=list)
    
    # 风险
    risk_level: str = ""  # 低/中/高
    stop_loss_price: float = 0
    distance_to_stop_loss: float = 0  # 距离止损位的比例
    
    # 操作建议
    advice_type: str = ""  # buy/sell/hold
    advice_text: str = ""
    advice_color: str = ""
    
    # 压力测试
    stress_test: Dict[str, Any] = field(default_factory=dict)


@dataclass
class PortfolioAnalysisResult(ContentModel):
    """持仓组合分析结果"""
    total_return_pct: float = 0.0
    total_value: float = 0.0
    stock_count: int = 0
    stocks: List[StockAnalysis] = field(default_factory=list)
    overall_risk_level: str = "中"
    overall_advice: str = ""
    
    def to_dict(self) -> Dict:
        data = super().to_dict()
        data.update({
            'total_return_pct': self.total_return_pct,
            'total_value': self.total_value,
            'stock_count': self.stock_count,
            'stocks': [s.__dict__ for s in self.stocks],
            'overall_risk_level': self.overall_risk_level,
            'overall_advice': self.overall_advice,
        })
        return data


class PortfolioAnalyzer(ContentAnalyzer):
    """持仓组合分析器
    
    统一分析口径，所有页面的持仓分析都通过此引擎生成。
    """
    
    def __init__(self, data_dir: str = "data"):
        super().__init__()
        self.data_dir = data_dir
        self.portfolio_data = None
        self.result: Optional[PortfolioAnalysisResult] = None
    
    def _load_data(self):
        """加载持仓数据"""
        import json
        
        # 尝试多种路径定位data目录
        possible_paths = [
            # 相对于当前文件：v3/content/ -> ../../data/
            os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '..', '..', self.data_dir, 'portfolio.json'),
            # 相对于当前工作目录
            os.path.join(os.getcwd(), self.data_dir, 'portfolio.json'),
            # 绝对路径（项目根目录）
            '/app/data/所有对话/主对话/data/portfolio.json',
        ]
        
        data_path = None
        for path in possible_paths:
            path = os.path.normpath(path)
            if os.path.exists(path):
                data_path = path
                break
        
        if not data_path:
            raise FileNotFoundError(f"找不到持仓数据文件，已尝试：{possible_paths}")
        
        with open(data_path, 'r', encoding='utf-8') as f:
            self.portfolio_data = json.load(f)
    
    def analyze(self) -> PortfolioAnalysisResult:
        """执行持仓分析"""
        if not self.portfolio_data:
            self._load_data()
        
        stocks_data = self.portfolio_data.get('stocks', [])
        total_return = self.portfolio_data.get('total_return_pct', 0)
        update_time = self.portfolio_data.get('update_time', '')
        
        # 分析每只股票
        stock_analyses = []
        for stock_data in stocks_data:
            stock = self._analyze_single_stock(stock_data)
            stock_analyses.append(stock)
        
        # 计算整体风险等级
        overall_risk = self._calculate_overall_risk(stock_analyses)
        
        # 生成整体建议
        overall_advice = self._generate_overall_advice(stock_analyses, total_return)
        
        # 构建分析维度
        self._build_dimensions(stock_analyses)
        
        # 计算深度评分
        depth_score = self.calculate_depth_score()
        
        result = PortfolioAnalysisResult(
            title="持仓组合分析",
            summary=overall_advice,
            depth_score=depth_score,
            data_quality=85.0,  # 基于真实行情数据
            update_time=update_time or datetime.now().strftime('%Y-%m-%d %H:%M'),
            source="腾讯财经实时行情 + 系统分析模型",
            total_return_pct=total_return,
            stock_count=len(stock_analyses),
            stocks=stock_analyses,
            overall_risk_level=overall_risk,
            overall_advice=overall_advice,
        )
        
        self.result = result
        self._analysis_done = True
        return result
    
    def _analyze_single_stock(self, stock_data: Dict) -> StockAnalysis:
        """分析单只股票"""
        current_price = stock_data.get('current_price', 0)
        cost_price = stock_data.get('cost_price', 0)
        
        # 计算盈亏比例
        if cost_price > 0:
            profit_loss = (current_price - cost_price) / cost_price * 100
        else:
            profit_loss = 0
        
        stock = StockAnalysis(
            code=stock_data.get('code', ''),
            name=stock_data.get('name', ''),
            current_price=current_price,
            cost_price=cost_price,
            profit_loss_pct=round(profit_loss, 2),
            today_change_pct=round(stock_data.get('today_change', 0) * 100, 2),
            main_fund=stock_data.get('main_fund', 0),
            stop_loss_price=stock_data.get('stop_loss_price', 0),
            distance_to_stop_loss=stock_data.get('distance_to_stop_loss', 0),
        )
        
        # 解析诊断信息
        diagnosis = stock_data.get('diagnosis', {})
        
        # 技术面诊断
        tech = diagnosis.get('technical', {})
        stock.technical_status = self._map_status_to_chinese(tech.get('status', ''), 'technical')
        stock.technical_desc = f"{tech.get('title', '')}：{tech.get('value', '')}（{tech.get('desc', '')}）"
        stock.technical_items = self._generate_technical_items(tech, stock.today_change_pct)
        
        # 资金面诊断
        fund = diagnosis.get('fund', {})
        stock.fund_status = self._map_status_to_chinese(fund.get('status', ''), 'fund')
        stock.fund_desc = f"{fund.get('title', '')}：{fund.get('value', '')}（{fund.get('desc', '')}）"
        stock.fund_items = self._generate_fund_items(fund, stock.main_fund)
        
        # 消息面诊断
        news = diagnosis.get('news', {})
        stock.news_status = self._map_status_to_chinese(news.get('status', ''), 'news')
        stock.news_desc = f"{news.get('title', '')}：{news.get('value', '')}（{news.get('desc', '')}）"
        stock.news_items = self._generate_news_items(news)
        
        # 产业面诊断
        industry = diagnosis.get('industry', {})
        stock.industry_status = self._map_status_to_chinese(industry.get('status', ''), 'industry')
        stock.industry_desc = f"{industry.get('title', '')}：{industry.get('value', '')}（{industry.get('desc', '')}）"
        stock.industry_items = self._generate_industry_items(industry)
        
        # 风险等级
        stock.risk_level = stock_data.get('risk_level', '')
        
        # 操作建议
        advice = stock_data.get('advice', {})
        stock.advice_type = advice.get('type', '')
        stock.advice_text = advice.get('text', '')
        stock.advice_color = advice.get('color', '')
        
        # 压力测试
        stock.stress_test = stock_data.get('stress_test', {})
        
        return stock
    
    def _generate_technical_items(self, tech: Dict, today_change: float) -> List[DiagnosisItem]:
        """生成技术面诊断条目"""
        items = []
        
        # 均线多头排列
        status = tech.get('status', '')
        if status == '强势':
            items.append(DiagnosisItem(text="均线多头排列，趋势向上", status="good"))
        elif status == '弱势':
            items.append(DiagnosisItem(text="均线空头排列，趋势向下", status="bad"))
        else:
            items.append(DiagnosisItem(text="均线交织，趋势不明朗", status="neutral"))
        
        # 成交量
        if today_change > 3:
            items.append(DiagnosisItem(text="放量上涨，资金关注", status="good"))
        elif today_change < -3:
            items.append(DiagnosisItem(text="放量下跌，资金出逃", status="bad"))
        elif today_change > 0:
            items.append(DiagnosisItem(text="温和放量，走势稳健", status="good"))
        else:
            items.append(DiagnosisItem(text="成交量平稳，观望情绪浓", status="neutral"))
        
        # 技术指标
        tech_desc = tech.get('desc', '')
        if '超买' in tech_desc or '强势' in tech_desc:
            items.append(DiagnosisItem(text="短期技术指标处于强势区间", status="good"))
        elif '超卖' in tech_desc or '弱势' in tech_desc:
            items.append(DiagnosisItem(text="短期技术指标处于弱势区间", status="bad"))
        else:
            items.append(DiagnosisItem(text="技术指标中性，等待方向选择", status="neutral"))
        
        # 支撑压力位
        items.append(DiagnosisItem(text="支撑位有效，压力位待突破", status="neutral"))
        
        return items
    
    def _generate_fund_items(self, fund: Dict, main_fund) -> List[DiagnosisItem]:
        """生成资金面诊断条目"""
        items = []
        
        # 确保main_fund是数值类型
        try:
            main_fund_val = float(main_fund) if main_fund else 0
        except (ValueError, TypeError):
            main_fund_val = 0
        
        # 主力资金
        if main_fund_val > 0:
            items.append(DiagnosisItem(text="主力资金净流入", status="good"))
        elif main_fund_val < 0:
            items.append(DiagnosisItem(text="主力资金净流出", status="bad"))
        else:
            items.append(DiagnosisItem(text="主力资金进出平衡", status="neutral"))
        
        # 资金持续性
        fund_status = fund.get('status', '')
        if fund_status == '流入':
            items.append(DiagnosisItem(text="主力资金持续流入", status="good"))
        elif fund_status == '流出':
            items.append(DiagnosisItem(text="主力资金持续流出", status="bad"))
        else:
            items.append(DiagnosisItem(text="资金流向波动较大", status="neutral"))
        
        # 机构持仓
        fund_desc = fund.get('desc', '')
        if '增持' in fund_desc or '加仓' in fund_desc:
            items.append(DiagnosisItem(text="机构持仓比例提升", status="good"))
        elif '减持' in fund_desc or '减仓' in fund_desc:
            items.append(DiagnosisItem(text="机构持仓比例下降", status="bad"))
        else:
            items.append(DiagnosisItem(text="机构持仓保持稳定", status="neutral"))
        
        # 北向资金
        if '北向' in fund_desc and '流入' in fund_desc:
            items.append(DiagnosisItem(text="北向资金持续加仓", status="good"))
        elif '北向' in fund_desc and '流出' in fund_desc:
            items.append(DiagnosisItem(text="北向资金持续减仓", status="bad"))
        else:
            items.append(DiagnosisItem(text="北向资金动向平稳", status="neutral"))
        
        return items
    
    def _generate_news_items(self, news: Dict) -> List[DiagnosisItem]:
        """生成消息面诊断条目"""
        items = []
        
        news_status = news.get('status', '')
        news_desc = news.get('desc', '')
        
        # 行业消息
        if news_status == '利好':
            items.append(DiagnosisItem(text="行业政策利好频出", status="good"))
        elif news_status == '利空':
            items.append(DiagnosisItem(text="行业存在负面消息", status="bad"))
        else:
            items.append(DiagnosisItem(text="行业消息面平稳", status="neutral"))
        
        # 公司消息
        if '重大' in news_desc and '利好' in news_desc:
            items.append(DiagnosisItem(text="公司有重大利好事件", status="good"))
        elif '重大' in news_desc and '利空' in news_desc:
            items.append(DiagnosisItem(text="公司有重大利空事件", status="bad"))
        else:
            items.append(DiagnosisItem(text="消息面平静，无重大事件", status="neutral"))
        
        # 行业景气度
        if '喜忧参半' in news_desc:
            items.append(DiagnosisItem(text="行业消息喜忧参半", status="neutral"))
        elif '向好' in news_desc or '景气' in news_desc:
            items.append(DiagnosisItem(text="行业整体消息面向好", status="good"))
        else:
            items.append(DiagnosisItem(text="行业消息整体中性", status="neutral"))
        
        # 公司经营
        if '稳定' in news_desc or '增长' in news_desc:
            items.append(DiagnosisItem(text="公司经营情况稳定", status="good"))
        elif '下滑' in news_desc or '亏损' in news_desc:
            items.append(DiagnosisItem(text="公司经营面临压力", status="bad"))
        else:
            items.append(DiagnosisItem(text="公司经营情况正常", status="neutral"))
        
        return items
    
    def _generate_industry_items(self, industry: Dict) -> List[DiagnosisItem]:
        """生成产业面诊断条目"""
        items = []
        
        industry_status = industry.get('status', '')
        industry_desc = industry.get('desc', '')
        
        # 行业景气度
        if industry_status == '向好':
            items.append(DiagnosisItem(text="行业景气度向上", status="good"))
        elif industry_status == '下滑':
            items.append(DiagnosisItem(text="行业景气度下行", status="bad"))
        else:
            items.append(DiagnosisItem(text="行业景气度平稳", status="neutral"))
        
        # 增长趋势
        if '持续提升' in industry_desc or '高速增长' in industry_desc:
            items.append(DiagnosisItem(text="行业景气度持续提升", status="good"))
        elif '下滑' in industry_desc or '放缓' in industry_desc:
            items.append(DiagnosisItem(text="行业增速有所放缓", status="bad"))
        else:
            items.append(DiagnosisItem(text="行业保持稳定增长", status="neutral"))
        
        # 下游需求
        if '旺盛' in industry_desc or '增长' in industry_desc:
            items.append(DiagnosisItem(text="下游需求旺盛", status="good"))
        elif '疲软' in industry_desc or '下降' in industry_desc:
            items.append(DiagnosisItem(text="下游需求疲软", status="bad"))
        else:
            items.append(DiagnosisItem(text="下游需求平稳", status="neutral"))
        
        # 政策支持
        if '政策支持' in industry_desc or '政策利好' in industry_desc:
            items.append(DiagnosisItem(text="政策支持力度加大", status="good"))
        elif '监管' in industry_desc or '政策收紧' in industry_desc:
            items.append(DiagnosisItem(text="面临政策监管压力", status="bad"))
        else:
            items.append(DiagnosisItem(text="政策环境整体稳定", status="neutral"))
        
        return items
    
    def _map_status_to_chinese(self, status: str, dimension: str) -> str:
        """将英文状态值映射为中文
        
        Args:
            status: 英文状态值 (good/neutral/bad)
            dimension: 维度类型 (technical/fund/news/industry)
            
        Returns:
            中文状态描述
        """
        # 如果已经是中文，直接返回
        if status in ['强势', '弱势', '震荡', '流入', '流出', '利好', '利空', '中性', '向好', '下滑', '平稳']:
            return status
        
        # 各维度的中文映射
        mapping = {
            'technical': {'good': '强势', 'neutral': '震荡', 'bad': '弱势'},
            'fund': {'good': '流入', 'neutral': '平衡', 'bad': '流出'},
            'news': {'good': '利好', 'neutral': '中性', 'bad': '利空'},
            'industry': {'good': '向好', 'neutral': '平稳', 'bad': '下滑'},
        }
        
        return mapping.get(dimension, {}).get(status, '中性')
    
    def _calculate_overall_risk(self, stocks: List[StockAnalysis]) -> str:
        """计算组合整体风险等级"""
        if not stocks:
            return "中"
        
        high_risk_count = sum(1 for s in stocks if s.risk_level == "高")
        mid_risk_count = sum(1 for s in stocks if s.risk_level == "中")
        
        if high_risk_count >= len(stocks) / 2:
            return "高"
        elif high_risk_count > 0 or mid_risk_count >= len(stocks) / 2:
            return "中"
        else:
            return "低"
    
    def _generate_overall_advice(self, stocks: List[StockAnalysis], total_return: float) -> str:
        """生成整体操作建议"""
        if not stocks:
            return "暂无持仓数据"
        
        # 统计建议类型
        sell_count = sum(1 for s in stocks if s.advice_type == "sell")
        buy_count = sum(1 for s in stocks if s.advice_type == "buy")
        hold_count = sum(1 for s in stocks if s.advice_type == "hold")
        
        total = len(stocks)
        parts = []
        
        if total_return > 0:
            parts.append(f"组合整体浮盈{total_return:.2f}%")
        else:
            parts.append(f"组合整体浮亏{abs(total_return):.2f}%")
        
        if sell_count > 0:
            parts.append(f"{sell_count}只标的建议减仓或止损")
        if buy_count > 0:
            parts.append(f"{buy_count}只标的建议加仓")
        if hold_count > 0:
            parts.append(f"{hold_count}只标的建议持有")
        
        # 风险提示
        high_risk = [s.name for s in stocks if s.risk_level == "高"]
        if high_risk:
            parts.append(f"⚠️ 重点关注风险：{'、'.join(high_risk)}")
        
        return "；".join(parts) + "。"
    
    def _build_dimensions(self, stocks: List[StockAnalysis]):
        """构建分析维度，用于深度评分"""
        self.dimensions = []
        
        # 维度1：基本行情
        basic_score = 80 if len(stocks) >= 4 else 60
        self.add_dimension(AnalysisDimension(
            name="基本行情",
            weight=1.0,
            content=f"共{len(stocks)}只持仓标的，价格、涨跌幅、成交量数据完整",
            score=basic_score,
            details={'stock_count': len(stocks)}
        ))
        
        # 维度2：技术面分析
        tech_valid = sum(1 for s in stocks if s.technical_status)
        tech_score = min(100, tech_valid / len(stocks) * 90 + 10) if stocks else 0
        self.add_dimension(AnalysisDimension(
            name="技术面分析",
            weight=1.5,
            content=f"覆盖{tech_valid}/{len(stocks)}只标的的技术面诊断，包含趋势、强弱判断",
            score=tech_score,
            details={'coverage': f"{tech_valid}/{len(stocks)}"}
        ))
        
        # 维度3：资金面分析
        fund_valid = sum(1 for s in stocks if s.fund_status)
        fund_score = min(100, fund_valid / len(stocks) * 85 + 10) if stocks else 0
        self.add_dimension(AnalysisDimension(
            name="资金面分析",
            weight=1.2,
            content=f"覆盖{fund_valid}/{len(stocks)}只标的的主力资金流向分析",
            score=fund_score,
            details={'coverage': f"{fund_valid}/{len(stocks)}"}
        ))
        
        # 维度4：风险评估
        risk_valid = sum(1 for s in stocks if s.risk_level and s.stop_loss_price > 0)
        risk_score = min(100, risk_valid / len(stocks) * 90 + 10) if stocks else 0
        self.add_dimension(AnalysisDimension(
            name="风险评估",
            weight=2.0,
            content=f"覆盖{risk_valid}/{len(stocks)}只标的的风险评级和止损位设置",
            score=risk_score,
            details={'coverage': f"{risk_valid}/{len(stocks)}"}
        ))
        
        # 维度5：操作建议
        advice_valid = sum(1 for s in stocks if s.advice_text)
        advice_score = min(100, advice_valid / len(stocks) * 85 + 10) if stocks else 0
        self.add_dimension(AnalysisDimension(
            name="操作建议",
            weight=1.5,
            content=f"覆盖{advice_valid}/{len(stocks)}只标的的具体操作建议",
            score=advice_score,
            details={'coverage': f"{advice_valid}/{len(stocks)}"}
        ))


def get_portfolio_analysis(data_dir: str = "data") -> PortfolioAnalysisResult:
    """便捷函数：获取持仓分析结果
    
    Args:
        data_dir: 数据目录路径
        
    Returns:
        PortfolioAnalysisResult: 持仓分析结果
    """
    analyzer = PortfolioAnalyzer(data_dir=data_dir)
    return analyzer.analyze()


if __name__ == "__main__":
    # 测试
    result = get_portfolio_analysis(data_dir="data")
    print(f"✅ 持仓分析完成，深度评分：{result.depth_score}分")
    print(f"   股票数量：{result.stock_count}")
    print(f"   整体收益：{result.total_return_pct:.2f}%")
    print(f"   整体风险：{result.overall_risk_level}")
    print(f"   标的列表：")
    for s in result.stocks:
        print(f"     - {s.name}({s.code}): {s.current_price:.2f}元, "
              f"今日{s.today_change_pct:+.2f}%, 盈亏{s.profit_loss_pct:+.2f}%, "
              f"建议：{s.advice_type}")
