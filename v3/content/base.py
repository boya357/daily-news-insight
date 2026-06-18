"""
内容引擎基类模块 - V4 架构
所有内容分析引擎的基础，定义统一的内容模型接口

核心原则：
- 内容层纯逻辑，不包含任何HTML/UI代码
- 输出结构化内容模型，由展现层决定如何展示
- 统一数据来源，统一分析口径
"""
from typing import Dict, List, Optional, Any, Union
from datetime import datetime
from dataclasses import dataclass, field


@dataclass
class ContentModel:
    """内容模型基类
    
    所有分析引擎的输出都应该是ContentModel的子类，
    包含结构化的分析结论和元数据。
    """
    title: str = ""
    summary: str = ""
    depth_score: float = 0.0  # 内容深度评分 0-100
    data_quality: float = 0.0  # 数据质量评分 0-100
    update_time: str = ""
    source: str = ""  # 数据来源说明
    
    def to_dict(self) -> Dict:
        """转换为字典格式"""
        return {
            'title': self.title,
            'summary': self.summary,
            'depth_score': self.depth_score,
            'data_quality': self.data_quality,
            'update_time': self.update_time,
            'source': self.source,
        }
    
    def is_valid(self) -> bool:
        """内容是否有效（达到最低质量要求）"""
        return self.depth_score >= 30 and self.data_quality >= 50


@dataclass
class AnalysisDimension:
    """分析维度
    
    每个分析模块可以包含多个分析维度，
    每个维度有独立的评分和内容。
    """
    name: str
    weight: float = 1.0  # 权重，用于计算整体深度评分
    content: str = ""
    score: float = 0.0  # 该维度的评分 0-100
    details: Dict[str, Any] = field(default_factory=dict)
    
    def to_dict(self) -> Dict:
        return {
            'name': self.name,
            'weight': self.weight,
            'content': self.content,
            'score': self.score,
            'details': self.details,
        }


class ContentAnalyzer:
    """内容分析器基类
    
    所有内容分析引擎都继承自此类，
    提供统一的分析接口和质量评估。
    """
    
    def __init__(self, data_loader=None):
        self.data_loader = data_loader
        self.dimensions: List[AnalysisDimension] = []
        self._analysis_done = False
    
    def analyze(self) -> ContentModel:
        """执行分析，返回内容模型
        
        子类必须实现此方法。
        """
        raise NotImplementedError("子类必须实现 analyze 方法")
    
    def add_dimension(self, dimension: AnalysisDimension):
        """添加一个分析维度"""
        self.dimensions.append(dimension)
    
    def calculate_depth_score(self) -> float:
        """根据各维度加权计算整体深度评分"""
        if not self.dimensions:
            return 0.0
        
        total_weight = sum(d.weight for d in self.dimensions)
        if total_weight == 0:
            return 0.0
        
        weighted_score = sum(d.score * d.weight for d in self.dimensions)
        return round(weighted_score / total_weight, 1)
    
    def get_dimension(self, name: str) -> Optional[AnalysisDimension]:
        """按名称获取分析维度"""
        for d in self.dimensions:
            if d.name == name:
                return d
        return None
    
    def generate_summary(self) -> str:
        """生成内容摘要
        
        基于各维度的核心结论生成整体摘要。
        子类可重写此方法。
        """
        if not self.dimensions:
            return ""
        
        key_points = []
        for d in self.dimensions:
            if d.score >= 70 and d.content:
                # 只取高分维度的核心结论
                key_points.append(d.content[:100])
        
        if key_points:
            return "；".join(key_points) + "。"
        return ""
    
    def validate(self) -> List[str]:
        """验证分析结果的质量
        
        Returns:
            问题列表，如果为空则表示质量合格
        """
        issues = []
        
        if not self.dimensions:
            issues.append("没有任何分析维度")
        
        if self.calculate_depth_score() < 30:
            issues.append(f"内容深度评分过低：{self.calculate_depth_score()}分")
        
        return issues


class ContentSection:
    """内容章节
    
    用于组织多个内容模块，形成完整的报告结构。
    """
    
    def __init__(self, title: str, icon: str = "📄", level: int = 1):
        self.title = title
        self.icon = icon
        self.level = level
        self.sections: List['ContentSection'] = []
        self.content: Optional[ContentModel] = None
        self.extra: Dict[str, Any] = {}
    
    def add_section(self, section: 'ContentSection'):
        """添加子章节"""
        self.sections.append(section)
    
    def set_content(self, content: ContentModel):
        """设置章节内容"""
        self.content = content
    
    def to_dict(self) -> Dict:
        return {
            'title': self.title,
            'icon': self.icon,
            'level': self.level,
            'content': self.content.to_dict() if self.content else None,
            'sections': [s.to_dict() for s in self.sections],
            'extra': self.extra,
        }
