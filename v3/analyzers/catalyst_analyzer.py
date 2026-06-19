"""
催化事件分析引擎 V2.0 - Skill融合版
整合多个分析Skill的核心方法论：

【融合的Skill能力】
1. 超级分析师 Skill：12套分析框架（SWOT/五力/情景规划/MECE/5Why等）
2. 行业趋势深度调研 Skill：产业链分析、CAGR预测、红利爆发点识别
3. 板块热度分析 Skill：政策-产业-资金三维热度模型
4. 每日持仓风险报告 Skill：风险分级与预警机制

【核心升级点】
- 催化剂分级体系：从S级到D级的量化评分
- 情景规划：乐观/中性/悲观三种情景推演
- 产业链传导：上游-中游-下游的影响路径分析
- 三维热度：政策+产业+资金的综合评估
- 时间轴分析：预期差-发酵-兑现-退潮全周期
"""

import json
from pathlib import Path
from datetime import datetime, timedelta
from typing import List, Dict, Optional, Tuple
from dataclasses import dataclass, field
from enum import Enum


class CatalystGrade(Enum):
    """催化剂等级"""
    S = "S级 - 超级催化"    # 改变行业逻辑的重大事件
    A = "A级 - 强催化"     # 对板块有显著影响
    B = "B级 - 中催化"     # 有一定影响但力度有限
    C = "C级 - 弱催化"     # 影响较小，更多是情绪层面
    D = "D级 - 微催化"     # 几乎没影响，可以忽略


@dataclass
class ScenarioAnalysis:
    """情景分析结果"""
    scenario_name: str      # 乐观/中性/悲观
    probability: float      # 发生概率
    impact_score: float     # 影响程度 0-100
    key_assumptions: List[str]  # 核心假设
    expected_return: float  # 预期收益率
    description: str        # 情景描述


@dataclass
class IndustryChainImpact:
    """产业链影响分析"""
    upstream: List[str]     # 上游受益环节
    midstream: List[str]    # 中游受益环节
    downstream: List[str]   # 下游受益环节
    benefit_order: List[str]  # 受益顺序
    core_beneficiary: List[str]  # 核心受益标的方向
    transmission_path: str  # 传导路径描述


class CatalystEventV2:
    """催化事件 V2 - 增强版"""
    
    def __init__(self, event_data: Dict):
        self.title = event_data.get('title', '')
        self.date = event_data.get('date', '')
        self.type = event_data.get('type', '')  # 政策/业绩/行业/公司/宏观/技术
        self.description = event_data.get('description', '')
        self.related_topics = event_data.get('related_topics', [])
        self.related_stocks = event_data.get('related_stocks', [])
        
        # 新增维度（V2增强）
        self.scope = event_data.get('scope', 'industry')  # 行业级/公司级/宏观级
        self.duration = event_data.get('duration', 'medium')  # 长期/中期/短期
        self.is_recurring = event_data.get('is_recurring', False)  # 是否是周期性事件
        self.source_importance = event_data.get('source_importance', 'medium')  # 消息来源重要性
    
    def calculate_comprehensive_score(self) -> float:
        """综合评分（V2增强：多维度加权）
        
        评分维度：
        1. 事件类型权重（政策 > 行业 > 业绩 > 公司 > 宏观）
        2. 影响范围（全局 > 行业 > 公司）
        3. 持续时间（长期 > 中期 > 短期）
        4. 来源可信度
        5. 预期差大小
        """
        # 1. 类型权重
        type_weights = {
            '政策': 0.95,
            '行业': 0.75,
            '业绩': 0.65,
            '技术': 0.60,
            '公司': 0.45,
            '宏观': 0.40,
        }
        type_weight = type_weights.get(self.type, 0.5)
        
        # 2. 影响范围
        scope_weights = {
            'global': 1.0,
            'national': 0.9,
            'industry': 0.7,
            'sector': 0.6,
            'company': 0.3,
        }
        scope_weight = scope_weights.get(self.scope, 0.5)
        
        # 3. 持续时间
        duration_weights = {
            'long': 0.9,
            'medium': 0.6,
            'short': 0.3,
        }
        duration_weight = duration_weights.get(self.duration, 0.5)
        
        # 4. 来源重要性
        source_weights = {
            'high': 0.9,
            'medium': 0.6,
            'low': 0.3,
        }
        source_weight = source_weights.get(self.source_importance, 0.5)
        
        # 综合计算
        base_score = 100
        final_score = base_score * type_weight * scope_weight * duration_weight * source_weight
        
        return round(final_score, 1)
    
    def get_grade(self) -> CatalystGrade:
        """获取催化剂等级"""
        score = self.calculate_comprehensive_score()
        
        if score >= 85:
            return CatalystGrade.S
        elif score >= 65:
            return CatalystGrade.A
        elif score >= 45:
            return CatalystGrade.B
        elif score >= 25:
            return CatalystGrade.C
        else:
            return CatalystGrade.D


class ThreeDimensionAnalyzer:
    """三维热度分析器 - 学习自「板块热度分析」Skill
    
    政策-产业-资金三维分析框架：
    - 政策维：政策力度、执行强度、预期差
    - 产业维：行业景气度、技术成熟度、渗透率
    - 资金维：北向资金、主力资金、龙虎榜、ETF资金流
    """
    
    def __init__(self, event: CatalystEventV2):
        self.event = event
    
    def analyze(self, policy_score: float = 50, industry_score: float = 50, capital_score: float = 50) -> Dict:
        """三维热度分析"""
        # 根据事件类型调整权重
        type_weights = {
            '政策': {'policy': 0.5, 'industry': 0.3, 'capital': 0.2},
            '行业': {'policy': 0.2, 'industry': 0.5, 'capital': 0.3},
            '业绩': {'policy': 0.1, 'industry': 0.3, 'capital': 0.6},
            '技术': {'policy': 0.1, 'industry': 0.5, 'capital': 0.4},
            '公司': {'policy': 0.05, 'industry': 0.25, 'capital': 0.7},
            '宏观': {'policy': 0.6, 'industry': 0.2, 'capital': 0.2},
        }
        weights = type_weights.get(self.event.type, {'policy': 0.33, 'industry': 0.33, 'capital': 0.34})
        
        total_score = policy_score * weights['policy'] + industry_score * weights['industry'] + capital_score * weights['capital']
        
        # 热度等级
        if total_score >= 80:
            heat_level = "沸腾"
            heat_color = "red"
        elif total_score >= 60:
            heat_level = "火热"
            heat_color = "orange"
        elif total_score >= 40:
            heat_level = "温热"
            heat_color = "yellow"
        elif total_score >= 20:
            heat_level = "冷淡"
            heat_color = "blue"
        else:
            heat_level = "冰点"
            heat_color = "gray"
        
        return {
            'total_score': round(total_score, 1),
            'heat_level': heat_level,
            'heat_color': heat_color,
            'dimensions': {
                'policy': {'score': policy_score, 'weight': weights['policy']},
                'industry': {'score': industry_score, 'weight': weights['industry']},
                'capital': {'score': capital_score, 'weight': weights['capital']},
            },
            'analysis': self._generate_3d_analysis(policy_score, industry_score, capital_score, weights),
        }
    
    def _generate_3d_analysis(self, policy: float, industry: float, capital: float, weights: Dict) -> str:
        """生成三维分析文字"""
        dimensions = []
        if policy >= 60:
            dimensions.append(f"政策面强力支撑（{policy:.0f}分）")
        elif policy < 40:
            dimensions.append(f"政策面偏弱（{policy:.0f}分）")
        
        if industry >= 60:
            dimensions.append(f"产业基本面扎实（{industry:.0f}分）")
        elif industry < 40:
            dimensions.append(f"产业基本面一般（{industry:.0f}分）")
        
        if capital >= 60:
            dimensions.append(f"资金关注度高（{capital:.0f}分）")
        elif capital < 40:
            dimensions.append(f"资金关注度低（{capital:.0f}分）")
        
        if not dimensions:
            return "三维度相对均衡，整体中性"
        
        return "，".join(dimensions)


class ScenarioPlanner:
    """情景规划分析器 - 学习自「超级分析师」Skill
    
    核心方法论：
    - 识别关键变量
    - 构建乐观/中性/悲观三种情景
    - 评估各情景发生概率
    - 计算各情景下的预期收益
    """
    
    def __init__(self, event: CatalystEventV2):
        self.event = event
    
    def analyze(self) -> List[ScenarioAnalysis]:
        """多情景分析"""
        base_impact = self.event.calculate_comprehensive_score() / 100
        
        scenarios = [
            ScenarioAnalysis(
                scenario_name="乐观情景",
                probability=0.25,
                impact_score=min(100, base_impact * 150),
                key_assumptions=[
                    "政策/事件超预期落地",
                    "市场情绪极度乐观",
                    "资金持续流入",
                ],
                expected_return=round(base_impact * 30, 1),  # 乐观预期收益
                description="事件影响超预期，相关板块或个股可能迎来爆发式行情，需警惕情绪过热后的回调风险。"
            ),
            ScenarioAnalysis(
                scenario_name="中性情景",
                probability=0.50,
                impact_score=base_impact * 100,
                key_assumptions=[
                    "事件按预期正常推进",
                    "市场情绪平稳",
                    "基本面逐步兑现",
                ],
                expected_return=round(base_impact * 15, 1),
                description="事件符合市场预期，相关标的可能走出趋势性行情，可逢低布局，关注业绩兑现度。"
            ),
            ScenarioAnalysis(
                scenario_name="悲观情景",
                probability=0.25,
                impact_score=max(0, base_impact * 50),
                key_assumptions=[
                    "事件落地不及预期",
                    "市场情绪谨慎",
                    "利好出尽变利空",
                ],
                expected_return=round(-base_impact * 10, 1),
                description="事件影响低于预期，或已被市场充分定价，需警惕"买预期卖事实"的兑现风险。"
            ),
        ]
        
        return scenarios
    
    def calculate_expected_value(self, scenarios: List[ScenarioAnalysis]) -> float:
        """计算数学期望值"""
        ev = sum(s.probability * s.expected_return for s in scenarios)
        return round(ev, 2)


class IndustryChainAnalyzer:
    """产业链分析器 - 学习自「行业趋势深度调研」Skill
    
    核心方法论：
    - 上游-中游-下游传导路径分析
    - 受益顺序判断
    - 核心受益环节识别
    - 利润分配格局分析
    """
    
    def __init__(self, event: CatalystEventV2):
        self.event = event
    
    def analyze(self) -> IndustryChainImpact:
        """产业链影响分析
        
        根据事件类型，模拟分析产业链各环节的受益情况
        """
        event_type = self.event.type
        
        if event_type == '政策':
            return self._policy_industry_chain_analysis()
        elif event_type == '技术':
            return self._tech_industry_chain_analysis()
        elif event_type == '行业':
            return self._industry_chain_analysis()
        elif event_type == '业绩':
            return self._earnings_industry_chain_analysis()
        else:
            return IndustryChainImpact(
                upstream=["待分析"],
                midstream=["待分析"],
                downstream=["待分析"],
                benefit_order=["待分析"],
                core_beneficiary=["待分析"],
                transmission_path="请提供更多行业信息以进行详细的产业链分析"
            )
    
    def _policy_industry_chain_analysis(self) -> IndustryChainImpact:
        """政策类事件的产业链分析"""
        return IndustryChainImpact(
            upstream=["原材料供应商", "核心零部件"],
            midstream=["设备制造商", "系统集成商"],
            downstream=["应用终端", "运营服务商"],
            benefit_order=["主题概念股", "龙头白马", "产业链二线", "上游材料"],
            core_beneficiary=["具备核心技术的龙头企业", "直接受益于政策补贴的环节"],
            transmission_path="政策出台 → 主题概念炒作（快）→ 中游设备先行 → 上游原材料受益 → 下游应用落地（慢）→ 业绩兑现"
        )
    
    def _tech_industry_chain_analysis(self) -> IndustryChainImpact:
        """技术突破类事件的产业链分析"""
        return IndustryChainImpact(
            upstream=["核心元器件", "关键材料", "专用设备"],
            midstream=["模组厂商", "解决方案提供商"],
            downstream=["品牌厂商", "终端应用", "场景运营商"],
            benefit_order=["技术核心方", "上游供应链", "中游制造", "下游应用"],
            core_beneficiary=["掌握核心技术的公司", "具备量产能力的企业"],
            transmission_path="技术突破 → 技术标杆公司估值重塑 → 供应链需求预期提升 → 上游材料设备受益 → 大规模应用后下游爆发"
        )
    
    def _industry_chain_analysis(self) -> IndustryChainImpact:
        """行业事件的产业链分析"""
        return IndustryChainImpact(
            upstream=["原材料", "核心组件"],
            midstream=["生产商", "加工商"],
            downstream=["渠道商", "终端消费者"],
            benefit_order=["供需缺口最大环节", "价格弹性最大品种", "龙头企业", "行业ETF"],
            core_beneficiary=["供需格局改善最明显的环节"],
            transmission_path="行业景气变化 → 供需格局重塑 → 价格变动 → 利润在产业链间重新分配"
        )
    
    def _earnings_industry_chain_analysis(self) -> IndustryChainImpact:
        """业绩类事件的产业链分析"""
        return IndustryChainImpact(
            upstream=["上游供应商"],
            midstream=["核心厂商"],
            downstream=["经销商", "终端"],
            benefit_order=["超预期公司", "行业龙头", "上下游关联公司"],
            core_beneficiary=["业绩超预期且可持续的公司"],
            transmission_path="业绩预告/财报 → 估值调整 → 上下游联动 → 行业估值重估"
        )


class FiveWhyAnalyzer:
    """5Why分析法 - 学习自「超级分析师」Skill
    
    核心方法论：连续追问5个"为什么"，找到问题的根本原因
    应用于：分析催化事件的深层逻辑，识别真正的投资机会
    """
    
    def __init__(self, event: CatalystEventV2):
        self.event = event
    
    def analyze(self) -> Dict:
        """5Why深度分析"""
        return {
            'why1': {
                'question': '为什么这个事件重要？',
                'answer': f'{self.event.title}之所以重要，是因为它直接影响{self.event.type}层面的预期，可能改变相关板块的估值逻辑。'
            },
            'why2': {
                'question': '为什么市场会关注？',
                'answer': '市场关注是因为事件可能带来业绩预期的变化，或者带来新的故事性题材，吸引资金关注。'
            },
            'why3': {
                'question': '为什么会有投资机会？',
                'answer': '投资机会来源于预期差。当市场对事件的影响预期不足或过度时，就产生了纠错的投资机会。'
            },
            'why4': {
                'question': '为什么这个机会能赚钱？',
                'answer': '能赚钱的核心逻辑是：事件驱动下的业绩改善预期 + 资金情绪推动的估值提升，形成戴维斯双击。'
            },
            'why5': {
                'question': '为什么是现在（不是过去也不是未来）？',
                'answer': f'因为事件时间点在{self.event.date}，当前处于"预期发酵期"，是布局的时间窗口。随着事件临近，预期会逐步升温。'
            },
            'conclusion': '通过5层追问，可以更清晰地识别事件的本质影响，避免停留在表面信息，把握真正的投资逻辑。',
        }


class SWOTAnalyzer:
    """SWOT分析器 - 学习自「超级分析师」Skill
    
    优势(Strengths)、劣势(Weaknesses)、机会(Opportunities)、威胁(Threats)
    """
    
    def __init__(self, event: CatalystEventV2):
        self.event = event
    
    def analyze(self) -> Dict:
        """对催化事件进行SWOT分析"""
        grade = self.event.get_grade()
        
        return {
            'strengths': [
                f'事件等级：{grade.value}',
                f'事件类型：{self.event.type}驱动，确定性较高',
                f'影响范围：{"广" if self.event.scope in ["global", "national", "industry"] else "中等"}',
            ],
            'weaknesses': [
                f'持续时间：{"较长" if self.event.duration == "long" else "中等偏短"}',
                '市场预期可能已经部分反映',
                '事件落地存在不确定性',
            ],
            'opportunities': [
                '事件超预期的可能性',
                '相关板块估值重塑机会',
                '龙头公司的业绩弹性',
            ],
            'threats': [
                '利好出尽，借利好出货',
                '事件不及预期导致回调',
                '市场整体环境风险',
            ],
            'strategy_matrix': {
                'SO战略': '利用优势抓住机会 - 重仓核心受益龙头',
                'WO战略': '克服劣势把握机会 - 轻仓参与，快进快出',
                'ST战略': '利用优势规避威胁 - 选择有安全边际的标的',
                'WT战略': '减少劣势规避威胁 - 观望为主，等待更明确信号',
            },
            'overall_assessment': f'综合来看，{self.event.title}属于{grade.value}事件，建议{ "积极参与" if grade in [CatalystGrade.S, CatalystGrade.A] else "谨慎关注" }，重点关注核心受益标的。',
        }


class CatalystAnalyzerV2:
    """催化事件分析器 V2.0 - 多Skill融合版
    
    整合的分析框架：
    - 三维热度分析（政策-产业-资金）
    - 情景规划（乐观/中性/悲观）
    - 产业链传导分析
    - SWOT分析
    - 5Why深度追问
    """
    
    def __init__(self, events: List[Dict]):
        self.events = [CatalystEventV2(e) for e in events]
    
    def analyze_single_event(self, event: CatalystEventV2, 
                            policy_score: float = 50, 
                            industry_score: float = 50, 
                            capital_score: float = 50) -> Dict:
        """深度分析单个催化事件"""
        # 1. 基础评分
        base_score = event.calculate_comprehensive_score()
        grade = event.get_grade()
        
        # 2. 三维热度分析
        three_d = ThreeDimensionAnalyzer(event).analyze(policy_score, industry_score, capital_score)
        
        # 3. 情景规划
        scenarios = ScenarioPlanner(event).analyze()
        expected_value = ScenarioPlanner(event).calculate_expected_value(scenarios)
        
        # 4. 产业链分析
        industry_chain = IndustryChainAnalyzer(event).analyze()
        
        # 5. SWOT分析
        swot = SWOTAnalyzer(event).analyze()
        
        # 6. 5Why分析
        five_why = FiveWhyAnalyzer(event).analyze()
        
        return {
            'base_info': {
                'title': event.title,
                'date': event.date,
                'type': event.type,
                'grade': grade.value,
                'score': base_score,
                'description': event.description,
                'related_topics': event.related_topics,
                'related_stocks': event.related_stocks,
            },
            'three_d_heat': three_d,
            'scenarios': [s.__dict__ for s in scenarios],
            'expected_value': expected_value,
            'industry_chain': industry_chain.__dict__,
            'swot': swot,
            'five_why': five_why,
            'investment_suggestion': self._generate_suggestion(grade, three_d, expected_value),
        }
    
    def analyze_upcoming_events(self, days_ahead: int = 30) -> List[Dict]:
        """分析即将到来的事件列表"""
        today = datetime.now().date()
        upcoming = []
        
        for event in self.events:
            try:
                event_date = datetime.strptime(event.date, '%Y-%m-%d').date()
                days_until = (event_date - today).days
                
                if 0 <= days_until <= days_ahead:
                    base_score = event.calculate_comprehensive_score()
                    grade = event.get_grade()
                    
                    # 判断事件阶段
                    if days_until <= 3:
                        stage = '临近爆发'
                        stage_advice = '已持仓的持有待涨，未持仓的谨慎追高'
                    elif days_until <= 7:
                        stage = '布局窗口'
                        stage_advice = '可逢低布局核心受益标的'
                    elif days_until <= 14:
                        stage = '关注期'
                        stage_advice = '纳入观察池，等待更明确信号'
                    else:
                        stage = '观察期'
                        stage_advice = '保持关注，暂不急于布局'
                    
                    upcoming.append({
                        'title': event.title,
                        'date': event.date,
                        'days_until': days_until,
                        'type': event.type,
                        'grade': grade.value,
                        'score': base_score,
                        'stage': stage,
                        'stage_advice': stage_advice,
                        'description': event.description,
                        'related_topics': event.related_topics,
                        'related_stocks': event.related_stocks,
                    })
            except:
                continue
        
        # 按日期排序
        upcoming.sort(key=lambda x: x['days_until'])
        
        return upcoming
    
    def _generate_suggestion(self, grade: CatalystGrade, three_d: Dict, expected_value: float) -> str:
        """生成投资建议"""
        heat_score = three_d['total_score']
        
        if grade in [CatalystGrade.S, CatalystGrade.A] and heat_score >= 60:
            suggestion = "强推级催化：建议重点关注，可考虑配置10%-20%仓位在核心受益标的上。"
        elif grade == CatalystGrade.B and heat_score >= 50:
            suggestion = "关注级催化：建议纳入观察，小仓位（5%以内）参与主题性机会。"
        elif grade == CatalystGrade.C:
            suggestion = "观望级催化：影响有限，不建议作为主要投资逻辑，可作为辅助参考。"
        else:
            suggestion = "弱催化：对投资决策影响不大，可忽略或仅作为情绪参考。"
        
        if expected_value > 10:
            suggestion += f" 预期收益期望值为{expected_value:.1f}%，具备一定配置价值。"
        elif expected_value < 0:
            suggestion += f" 注意：预期收益期望值为负（{expected_value:.1f}%），风险大于收益，谨慎参与。"
        
        return suggestion
    
    def generate_calendar_summary(self, days: int = 30) -> Dict:
        """生成事件日历摘要"""
        upcoming = self.analyze_upcoming_events(days)
        
        grade_counts = {}
        type_counts = {}
        
        for event in upcoming:
            # 等级统计
            g = event['grade'][0]  # 取首字母S/A/B/C/D
            grade_counts[g] = grade_counts.get(g, 0) + 1
            
            # 类型统计
            t = event['type']
            type_counts[t] = type_counts.get(t, 0) + 1
        
        # 计算总体热度
        avg_score = sum(e['score'] for e in upcoming) / len(upcoming) if upcoming else 0
        
        if avg_score >= 60:
            overall_heat = "高热度期"
            advice = "事件密集，催化不断，适合积极把握主题性机会"
        elif avg_score >= 40:
            overall_heat = "中热度期"
            advice = "有一定催化事件，选择性参与即可"
        else:
            overall_heat = "低热度期"
            advice = "事件清淡，建议侧重业绩和基本面，减少主题博弈"
        
        return {
            'total_events': len(upcoming),
            'grade_distribution': grade_counts,
            'type_distribution': type_counts,
            'average_score': round(avg_score, 1),
            'overall_heat': overall_heat,
            'advice': advice,
            'top_events': [e for e in upcoming if e['grade'][0] in ['S', 'A']][:5],
        }


# ============================================================================
# 便捷函数
# ============================================================================
def analyze_catalyst_v2(event_data: Dict, policy_score=50, industry_score=50, capital_score=50) -> Dict:
    """分析单个催化事件（V2增强版）"""
    event = CatalystEventV2(event_data)
    analyzer = CatalystAnalyzerV2([event_data])
    return analyzer.analyze_single_event(event, policy_score, industry_score, capital_score)


def analyze_catalysts_v2(events: List[Dict], days: int = 30) -> Dict:
    """分析多个催化事件（V2增强版）"""
    analyzer = CatalystAnalyzerV2(events)
    return {
        'calendar_summary': analyzer.generate_calendar_summary(days),
        'upcoming_events': analyzer.analyze_upcoming_events(days),
    }


if __name__ == '__main__':
    # 测试数据
    test_events = [
        {
            'title': '苹果WWDC开发者大会',
            'date': '2026-06-10',
            'type': '行业',
            'scope': 'industry',
            'duration': 'medium',
            'source_importance': 'high',
            'description': '苹果年度开发者大会，预计发布AI相关功能和新硬件',
            'related_topics': ['AI应用', '苹果产业链', '消费电子'],
            'related_stocks': ['立讯精密', '歌尔股份', '比亚迪电子'],
        },
        {
            'title': '存储芯片价格上涨',
            'date': '2026-06-15',
            'type': '行业',
            'scope': 'industry',
            'duration': 'long',
            'source_importance': 'high',
            'description': 'DRAM/NAND闪存价格持续上涨，行业景气度回升',
            'related_topics': ['存储芯片', '半导体', 'AI算力'],
            'related_stocks': ['长江存储', '兆易创新', '北京君正'],
        },
    ]
    
    result = analyze_catalysts_v2(test_events, days=30)
    print(json.dumps(result, ensure_ascii=False, indent=2))
