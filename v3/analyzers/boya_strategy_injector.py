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
        'gold_report': 'medium',         # 黄金投资报告
        'deep_analysis': 'medium',       # 超级分析师深度分析
        'portfolio_dashboard': 'medium',
        'weekly_outlook': 'medium',
        'weekly_review': 'medium',
        
        # 资讯简报类 - 轻量策略
        'daily_report': 'medium',        # 每日新闻报告
        'intraday_report': 'light',
        'aftermarket_report': 'light',
        'weekend_express': 'light',
        'tomorrow_catalyst': 'light',
        'topic_tracking': 'medium',      # 话题追踪
        
        # 工具类 - 无策略
        'data_tool': 'none',
        'company_research': 'medium',    # 公司竞品调研
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
# 三层Skill架构：核心投资层 / 信息资讯层 / 工具辅助层
SKILL_PAGE_TYPE_MAP = {
    # === 核心投资层（full级boya策略）===
    'a-stock-risk-report': 'risk_report',           # 每日持仓风险报告 - full
    'stock-analysis': 'stock_detail',               # 股票个股分析 - full（新升级）
    'multi-agent-dialogue-system': 'topic_deep_dive',  # 竹石个股Agent - full
    'sector-hotness-analysis': 'sector_heatmap',    # 板块热度分析 - full
    'gold-market-analyzer': 'gold_report',          # 黄金投资分析 - full
    
    # === 信息资讯层（medium级boya策略）===
    'industry-trend-research': 'industry_report',   # 行业趋势深度调研 - full
    'company-competitor-research': 'company_research',  # 公司竞品调研 - medium
    'daily-news-report': 'daily_report',            # 全球热点新闻日报 - medium
    'topic_tracking': 'topic_tracking',             # 话题追踪 - medium
    'super-analyst': 'deep_analysis',               # 超级分析师 - medium（深度分析工具）
    
    # === 工具辅助层（light/none级）===
    'stock-data-skill': 'data_tool',                # 实时行情数据 - light
    'toutiao-hot-article': 'content_tool',          # 今日头条爆文 - none
}

# Skill能力等级定义（用于分层注入决策）
SKILL_CAPABILITY_LEVELS = {
    # 核心投资层 - 直接产生投资决策
    'a-stock-risk-report': {'tier': 'core', 'strategy_level': 'full', 'has_technical': True, 'has_sentiment': True},
    'stock-analysis': {'tier': 'core', 'strategy_level': 'full', 'has_technical': True, 'has_sentiment': True, 'has_gaps': True},
    'multi-agent-dialogue-system': {'tier': 'core', 'strategy_level': 'full', 'has_technical': True, 'has_sentiment': True},
    'sector-hotness-analysis': {'tier': 'core', 'strategy_level': 'full', 'has_sector': True},
    'gold-market-analyzer': {'tier': 'core', 'strategy_level': 'full', 'has_macro': True},
    
    # 信息资讯层 - 提供分析框架与资讯
    'industry-trend-research': {'tier': 'info', 'strategy_level': 'full', 'has_framework': True},
    'company-competitor-research': {'tier': 'info', 'strategy_level': 'medium', 'has_framework': True},
    'daily-news-report': {'tier': 'info', 'strategy_level': 'medium', 'has_news': True},
    'topic_tracking': {'tier': 'info', 'strategy_level': 'medium', 'has_tracking': True},
    'super-analyst': {'tier': 'info', 'strategy_level': 'medium', 'has_framework': True, 'frameworks': 12},
    
    # 工具辅助层 - 数据与内容工具
    'stock-data-skill': {'tier': 'tool', 'strategy_level': 'light', 'has_realtime': True},
    'toutiao-hot-article': {'tier': 'tool', 'strategy_level': 'none', 'has_content': True},
}


def get_injector_for_skill(skill_name: str) -> BoyaStrategyInjector:
    """根据Skill名称创建对应的策略注入器"""
    page_type = SKILL_PAGE_TYPE_MAP.get(skill_name, 'none')
    return BoyaStrategyInjector(page_type=page_type)
