"""
boya策略分层注入器
根据页面类型和策略等级，决定注入哪些boya策略组件

策略等级：
- full: 完整策略（主线评级+龙头识别+买卖点+止损+弹性+组合+预判+视角批注）
- medium: 中等策略（主线评级+买卖点+止损+视角批注）
- light: 轻量策略（仅视角批注）
- none: 无策略
"""
from typing import Dict, List, Any, Optional
from dataclasses import dataclass


@dataclass
class StrategyComponent:
    """策略组件定义"""
    name: str
    description: str
    level: str  # 所属等级: full/medium/light
    requires_data: List[str]  # 需要的数据字段


class BoyaStrategyInjector:
    """boya策略分层注入器"""
    
    # 策略组件定义
    COMPONENTS = {
        'mainline_rating': StrategyComponent(
            'mainline_rating', '主线评级', 'medium',
            ['sector_data', 'market_trend']
        ),
        'dragon_identify': StrategyComponent(
            'dragon_identify', '龙头识别', 'full',
            ['stock_list', 'market_cap', 'turnover']
        ),
        'buy_point': StrategyComponent(
            'buy_point', '买点分析', 'medium',
            ['technical_analysis', 'support_resistance']
        ),
        'stop_loss': StrategyComponent(
            'stop_loss', '止损纪律', 'medium',
            ['risk_level', 'volatility']
        ),
        'elasticity': StrategyComponent(
            'elasticity', '弹性测算', 'full',
            ['price_target', 'upside_space', 'valuation']
        ),
        'portfolio_impact': StrategyComponent(
            'portfolio_impact', '组合影响', 'full',
            ['current_portfolio', 'correlation']
        ),
        'prediction_tracking': StrategyComponent(
            'prediction_tracking', '预判追踪', 'full',
            ['prediction_history', 'accuracy']
        ),
        'perspective_box': StrategyComponent(
            'perspective_box', 'boya视角批注', 'light',
            ['core_insight']
        ),
    }
    
    # 等级配置 - 每个等级包含哪些组件
    LEVEL_CONFIG = {
        'full': ['mainline_rating', 'dragon_identify', 'buy_point', 'stop_loss',
                 'elasticity', 'portfolio_impact', 'prediction_tracking', 'perspective_box'],
        'medium': ['mainline_rating', 'buy_point', 'stop_loss', 'perspective_box'],
        'light': ['perspective_box'],
        'none': [],
    }
    
    # 页面类型与默认策略等级映射
    PAGE_TYPE_LEVELS = {
        # 深度报告类 - 完整策略
        'industry_report': 'full',
        'stock_detail': 'full',
        'topic_deep_dive': 'full',
        'risk_report': 'full',
        's_level_catalyst': 'full',
        
        # 中等深度 - 中等策略
        'sector_heatmap': 'medium',
        'portfolio_dashboard': 'medium',
        'weekly_outlook': 'medium',
        'weekly_review': 'medium',
        
        # 资讯简报类 - 轻量策略
        'daily_report': 'light',
        'intraday_report': 'light',
        'aftermarket_report': 'light',
        'weekend_express': 'light',
        'tomorrow_catalyst': 'light',
        'topic_tracking': 'light',
        
        # 工具类 - 无策略
        'data_tool': 'none',
        'company_research': 'none',
        'content_tool': 'none',
        'prediction_center': 'none',
        'time_machine': 'none',
        'workflow_status': 'none',
    }
    
    def __init__(self, level: Optional[str] = None, page_type: Optional[str] = None):
        """
        Args:
            level: 直接指定策略等级，优先级高于page_type
            page_type: 页面类型，根据类型自动匹配对应等级
        """
        if level:
            self.level = level
        elif page_type:
            self.level = self.PAGE_TYPE_LEVELS.get(page_type, 'none')
        else:
            self.level = 'none'
        
        self.active_components = self.LEVEL_CONFIG.get(self.level, [])
    
    def get_components(self) -> List[str]:
        """获取当前等级的所有组件名称"""
        return self.active_components
    
    def get_component_details(self) -> List[StrategyComponent]:
        """获取当前等级的所有组件详情"""
        return [self.COMPONENTS[name] for name in self.active_components 
                if name in self.COMPONENTS]
    
    def has_component(self, component_name: str) -> bool:
        """检查是否包含某个组件"""
        return component_name in self.active_components
    
    def generate_injection_config(self, data: Dict = None) -> Dict[str, Any]:
        """生成注入配置
        
        根据可用数据，确定实际可以渲染哪些组件
        
        Args:
            data: 页面可用的数据
            
        Returns:
            注入配置字典
        """
        data = data or {}
        renderable = []
        
        for comp_name in self.active_components:
            comp = self.COMPONENTS.get(comp_name)
            if not comp:
                continue
            
            # 检查数据是否满足要求
            has_required = all(
                any(req in d for d in [data] + list(data.values()) if isinstance(d, dict))
                for req in comp.requires_data
            )
            
            # 即使数据不全也可以渲染（组件内部处理缺数据的情况）
            renderable.append({
                'name': comp_name,
                'description': comp.description,
                'level': comp.level,
                'has_full_data': has_required,
            })
        
        return {
            'strategy_level': self.level,
            'components_count': len(renderable),
            'components': renderable,
        }
    
    @classmethod
    def get_level_for_page_type(cls, page_type: str) -> str:
        """根据页面类型获取默认策略等级"""
        return cls.PAGE_TYPE_LEVELS.get(page_type, 'none')
    
    @classmethod
    def get_all_levels(cls) -> Dict[str, List[str]]:
        """获取所有等级及其包含的组件"""
        return cls.LEVEL_CONFIG


# Skill与页面类型映射
SKILL_PAGE_TYPE_MAP = {
    'a-stock-risk-report': 'risk_report',
    'stock-analysis': 'stock_detail',
    'multi-agent-dialogue-system': 'topic_deep_dive',
    'industry-trend-research': 'industry_report',
    'sector-hotness-analysis': 'sector_heatmap',
    'daily-news-report': 'daily_report',
    'topic_tracking': 'topic_tracking',
    'stock-data-skill': 'data_tool',
    'gold-market-analyzer': 'gold_report',  # 中等策略
    'company-competitor-research': 'company_research',
    'toutiao-hot-article': 'content_tool',
}


def get_injector_for_skill(skill_name: str) -> BoyaStrategyInjector:
    """根据Skill名称创建对应的策略注入器"""
    page_type = SKILL_PAGE_TYPE_MAP.get(skill_name, 'none')
    return BoyaStrategyInjector(page_type=page_type)
