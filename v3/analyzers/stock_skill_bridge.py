"""
股票个股分析 Skill 桥接层
将 stock-analysis Skill 的核心能力整合到V3.5系统中
包括：多数据源切换、缺口分析、消息面分析、专业操作建议
"""

import json
from pathlib import Path
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, field


@dataclass
class GapAnalysis:
    """缺口分析结果"""
    gap_type: str  # 向上缺口 / 向下缺口
    gap_date: str
    gap_high: float
    gap_low: float
    gap_size: float  # 缺口幅度
    is_filled: bool  # 是否已回补
    support_resistance: str  # 支撑/压力作用
    importance: str  # 重要性: 高/中/低


@dataclass
class NewsSentiment:
    """消息面情绪分析"""
    total_news: int = 0
    positive: int = 0
    negative: int = 0
    neutral: int = 0
    sentiment_score: float = 0.0  # -100 到 100
    impact_on_open: str = ""  # 对开盘的影响判断
    key_news: List[Dict] = field(default_factory=list)


class StockSkillEnhancer:
    """
    股票个股分析Skill增强器
    基于stock-analysis Skill的能力模型，增强现有个股分析
    """
    
    # 数据源配置
    DATA_SOURCES = ['sina', 'eastmoney', 'xueqiu']
    CURRENT_SOURCE = 'sina'
    
    def __init__(self, stock_data: Dict):
        """
        Args:
            stock_data: 股票基础数据 (name, code, price, etc.)
        """
        self.stock_data = stock_data
        self.name = stock_data.get('name', '')
        self.code = stock_data.get('code', '')
    
    def analyze_gaps(self, prices: List[Dict]) -> List[GapAnalysis]:
        """
        缺口分析 - stock-analysis Skill核心能力
        
        识别向上缺口和向下缺口，判断回补状态，评估支撑压力作用
        """
        gaps = []
        
        if len(prices) < 2:
            return gaps
        
        for i in range(1, len(prices)):
            prev = prices[i-1]
            curr = prices[i]
            
            # 向上缺口：今日最低价 > 昨日最高价
            if curr['low'] > prev['high']:
                gap_size = (curr['low'] - prev['high']) / prev['high'] * 100
                is_filled = self._check_gap_filled(prices, i, 'up')
                importance = self._calc_gap_importance(gap_size, prices[i]['volume'])
                
                gaps.append(GapAnalysis(
                    gap_type='向上缺口',
                    gap_date=curr['date'],
                    gap_high=curr['low'],  # 缺口上沿是今日最低
                    gap_low=prev['high'],   # 缺口下沿是昨日最高
                    gap_size=round(gap_size, 2),
                    is_filled=is_filled,
                    support_resistance='支撑位' if not is_filled else '（已回补）',
                    importance=importance
                ))
            
            # 向下缺口：今日最高价 < 昨日最低价
            elif curr['high'] < prev['low']:
                gap_size = (prev['low'] - curr['high']) / prev['low'] * 100
                is_filled = self._check_gap_filled(prices, i, 'down')
                importance = self._calc_gap_importance(gap_size, prices[i]['volume'])
                
                gaps.append(GapAnalysis(
                    gap_type='向下缺口',
                    gap_date=curr['date'],
                    gap_high=prev['low'],    # 缺口上沿是昨日最低
                    gap_low=curr['high'],    # 缺口下沿是今日最高
                    gap_size=round(gap_size, 2),
                    is_filled=is_filled,
                    support_resistance='压力位' if not is_filled else '（已回补）',
                    importance=importance
                ))
        
        # 只保留未回补的重要缺口（最近的3个）
        active_gaps = [g for g in gaps if not g.is_filled]
        return sorted(active_gaps, key=lambda x: x.gap_date, reverse=True)[:3]
    
    def _check_gap_filled(self, prices: List[Dict], gap_index: int, gap_type: str) -> bool:
        """检查缺口是否已回补"""
        gap_high = prices[gap_index]['low'] if gap_type == 'up' else prices[gap_index-1]['low']
        gap_low = prices[gap_index-1]['high'] if gap_type == 'up' else prices[gap_index]['high']
        
        # 检查后续价格是否回补
        for i in range(gap_index + 1, len(prices)):
            if gap_type == 'up':
                # 向上缺口回补：价格跌破缺口下沿
                if prices[i]['low'] <= gap_low:
                    return True
            else:
                # 向下缺口回补：价格涨破缺口上沿
                if prices[i]['high'] >= gap_high:
                    return True
        return False
    
    def _calc_gap_importance(self, gap_size: float, volume: float) -> str:
        """计算缺口重要性"""
        if gap_size > 3 and volume > 0:  # 缺口大+放量
            return '高'
        elif gap_size > 1.5:
            return '中'
        else:
            return '低'
    
    def analyze_news_sentiment(self, news_list: List[Dict] = None) -> NewsSentiment:
        """
        消息面情绪分析 - stock-analysis Skill核心能力
        
        分析资讯情绪分布，预测对开盘的影响
        """
        if news_list is None:
            news_list = self._get_sample_news()
        
        result = NewsSentiment(total_news=len(news_list))
        
        for news in news_list:
            sentiment = news.get('sentiment', 'neutral')
            if sentiment == 'positive':
                result.positive += 1
            elif sentiment == 'negative':
                result.negative += 1
            else:
                result.neutral += 1
        
        # 计算情绪得分
        if result.total_news > 0:
            result.sentiment_score = round(
                (result.positive - result.negative) / result.total_news * 100, 1
            )
        
        # 判断对开盘的影响
        score = result.sentiment_score
        if score > 60:
            result.impact_on_open = '高开概率大，情绪面强劲'
        elif score > 30:
            result.impact_on_open = '小幅高开，情绪偏多'
        elif score > -30:
            result.impact_on_open = '平开为主，情绪中性'
        elif score > -60:
            result.impact_on_open = '小幅低开，情绪偏空'
        else:
            result.impact_on_open = '低开概率大，情绪面承压'
        
        result.key_news = news_list[:3]  # 前3条重要新闻
        return result
    
    def _get_sample_news(self) -> List[Dict]:
        """获取示例新闻数据（实际应用中从搜索/数据源获取）"""
        return [
            {'title': f'{self.name}发布最新公告', 'sentiment': 'neutral', 'source': '公司公告'},
            {'title': f'{self.name}所属板块今日走强', 'sentiment': 'positive', 'source': '财联社'},
            {'title': f'{self.name}获机构调研', 'sentiment': 'positive', 'source': '证券时报'},
        ]
    
    def generate_trading_advice(self, technical_score: float, sentiment_score: float, 
                                current_price: float, support: float, resistance: float) -> Dict:
        """
        生成专业操作建议 - stock-analysis Skill核心能力
        
        综合技术面和消息面，给出买入/持有/卖出建议和具体价位
        """
        # 综合得分
        total_score = technical_score * 0.7 + sentiment_score * 0.3
        
        # 操作建议
        if total_score > 70:
            action = '买入'
            action_desc = '趋势向好，可逢低布局'
        elif total_score > 50:
            action = '持有'
            action_desc = '趋势尚可，继续持有观察'
        elif total_score > 30:
            action = '观望'
            action_desc = '方向不明，建议观望等待'
        else:
            action = '减仓/规避'
            action_desc = '趋势走弱，建议减仓规避'
        
        # 买卖价位
        buy_zone = [round(support * 0.98, 2), round(support * 1.02, 2)]
        sell_zone = [round(resistance * 0.98, 2), round(resistance * 1.02, 2)]
        
        # 止损设置（龙空龙策略）
        stop_loss = round(support * 0.95, 2)  # 支撑位下方5%止损
        
        return {
            'action': action,
            'action_description': action_desc,
            'total_score': round(total_score, 1),
            'technical_score': technical_score,
            'sentiment_score': sentiment_score,
            'buy_zone': buy_zone,
            'sell_zone': sell_zone,
            'stop_loss': stop_loss,
            'stop_loss_pct': round((current_price - stop_loss) / current_price * 100, 2),
            'risk_reward_ratio': round((sell_zone[1] - current_price) / (current_price - stop_loss), 2),
        }
    
    def get_multi_source_info(self) -> Dict:
        """多数据源信息"""
        return {
            'current_source': self.CURRENT_SOURCE,
            'available_sources': self.DATA_SOURCES,
            'auto_switch': True,
            'last_update': '',
        }


# 超级分析师 Skill 整合模块
class SuperAnalystFramework:
    """
    超级分析师 Skill - 12套分析框架整合
    可用于行业报告、公司分析的深度思考
    """
    
    FRAMEWORKS = {
        'swot': {
            'name': 'SWOT分析',
            'description': '优势、劣势、机会、威胁四维度分析',
            'use_cases': ['战略评估', '竞争定位', '投资决策'],
            'dimensions': ['优势(Strengths)', '劣势(Weaknesses)', '机会(Opportunities)', '威胁(Threats)'],
        },
        'porter_five_forces': {
            'name': '波特五力模型',
            'description': '行业竞争格局分析',
            'use_cases': ['行业分析', '进入壁垒评估', '竞争战略'],
            'dimensions': ['供应商议价能力', '购买者议价能力', '潜在进入者威胁', '替代品威胁', '同业竞争程度'],
        },
        'first_principles': {
            'name': '第一性原理',
            'description': '从基本事实出发，拆解问题本质',
            'use_cases': ['创新突破', '价值重估', '行业重构'],
            'dimensions': ['核心假设', '基本事实', '推理链条', '创新机会'],
        },
        'scenario_planning': {
            'name': '情景规划',
            'description': '多情景推演，应对不确定性',
            'use_cases': ['长期预测', '风险预案', '战略规划'],
            'dimensions': ['乐观情景', '基准情景', '悲观情景', '风险预警'],
        },
        'cost_benefit': {
            'name': '成本收益分析',
            'description': '量化评估投入产出比',
            'use_cases': ['投资决策', '项目评估', '资源配置'],
            'dimensions': ['直接收益', '间接收益', '直接成本', '隐性成本'],
        },
        'pareto': {
            'name': '帕累托分析',
            'description': '80/20法则，识别关键驱动因素',
            'use_cases': ['优先级排序', '资源优化', '效率提升'],
            'dimensions': ['核心驱动因素', '次要因素', '边际因素'],
        },
        'five_whys': {
            'name': '5Why分析法',
            'description': '层层追问，找到问题根因',
            'use_cases': ['问题诊断', '风险溯源', '改进分析'],
            'dimensions': ['现象', '第一层原因', '第二层原因', '第三层原因', '根本原因'],
        },
        'design_thinking': {
            'name': '设计思维',
            'description': '以用户为中心的创新方法论',
            'use_cases': ['产品创新', '用户体验', '商业模式'],
            'dimensions': ['同理心', '定义问题', '构思方案', '原型测试', '落地推广'],
        },
        'systems_thinking': {
            'name': '系统思维',
            'description': '全局视角，看清系统互联',
            'use_cases': ['复杂问题', '生态分析', '长期趋势'],
            'dimensions': ['系统要素', '连接关系', '反馈回路', '杠杆点'],
        },
        'socratic_method': {
            'name': '苏格拉底提问法',
            'description': '通过提问深化理解，挑战假设',
            'use_cases': ['深度思考', '观点验证', '假设挑战'],
            'dimensions': ['核心假设', '证据检验', '反方观点', '认知边界'],
        },
        'mece': {
            'name': 'MECE原则',
            'description': '相互独立，完全穷尽',
            'use_cases': ['问题拆解', '分类梳理', '结构化表达'],
            'dimensions': ['分解维度', '子项独立性', '覆盖完整性', '优化建议'],
        },
        'hypothesis_driven': {
            'name': '假设驱动分析',
            'description': '提出假设，验证真伪',
            'use_cases': ['研究分析', '决策验证', '数据探索'],
            'dimensions': ['核心假设', '验证指标', '数据支撑', '结论判断'],
        },
    }
    
    @classmethod
    def get_recommended_frameworks(cls, analysis_type: str) -> List[str]:
        """根据分析类型推荐适用的分析框架"""
        recommendations = {
            'industry': ['porter_five_forces', 'swot', 'scenario_planning', 'systems_thinking'],
            'company': ['swot', 'cost_benefit', 'pareto', 'hypothesis_driven'],
            'investment': ['swot', 'scenario_planning', 'first_principles', 'cost_benefit'],
            'problem': ['five_whys', 'first_principles', 'socratic_method', 'mece'],
            'strategy': ['swot', 'porter_five_forces', 'scenario_planning', 'systems_thinking'],
            'innovation': ['first_principles', 'design_thinking', 'socratic_method', 'pareto'],
        }
        return recommendations.get(analysis_type, ['swot', 'scenario_planning'])
    
    @classmethod
    def generate_framework_html(cls, framework_id: str, data: Dict = None) -> str:
        """生成分析框架的HTML展示模块"""
        fw = cls.FRAMEWORKS.get(framework_id)
        if not fw:
            return ''
        
        data = data or {}
        dimensions_html = ''
        
        for dim in fw['dimensions']:
            dim_content = data.get(dim, '待补充分析...')
            dimensions_html += f'''
            <div class="bg-white/5 rounded-lg p-3 border border-white/10">
                <div class="text-blue-400 font-medium text-sm mb-1">{dim}</div>
                <div class="text-white/70 text-xs">{dim_content}</div>
            </div>
            '''
        
        grid_cols = len(fw['dimensions'])
        if grid_cols > 4:
            grid_cols = 2
        
        return f'''
        <div class="boya-strategy-section bg-gradient-to-r from-purple-500/10 to-blue-500/10 rounded-xl p-4 border border-purple-500/20">
            <div class="flex items-center gap-2 mb-3">
                <span class="text-xl">🧠</span>
                <span class="text-white font-semibold">{fw['name']}</span>
                <span class="text-white/50 text-xs px-2 py-0.5 bg-white/10 rounded-full">超级分析师框架</span>
            </div>
            <p class="text-white/60 text-sm mb-3">{fw['description']}</p>
            <div class="grid grid-cols-{grid_cols} gap-2">
                {dimensions_html}
            </div>
        </div>
        '''


# 导出
def get_stock_enhancer(stock_data: Dict) -> StockSkillEnhancer:
    """获取股票分析增强器"""
    return StockSkillEnhancer(stock_data)


def get_super_analyst() -> type:
    """获取超级分析师框架"""
    return SuperAnalystFramework


# 版本信息
__version__ = '2.0.0'
__skills__ = ['stock-analysis', 'super-analyst']
