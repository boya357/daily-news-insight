"""
基础组件类
所有组件继承自 Component，提供统一的渲染接口
"""

class Component:
    """组件基类"""
    
    def __init__(self, **kwargs):
        self.props = kwargs
    
    def render(self) -> str:
        """渲染组件为HTML字符串"""
        raise NotImplementedError("子类必须实现 render 方法")
    
    def __str__(self) -> str:
        return self.render()
    
    def __add__(self, other):
        """支持组件相加拼接"""
        if isinstance(other, Component):
            return self.render() + other.render()
        elif isinstance(other, str):
            return self.render() + other
        return NotImplemented


class HTMLComponent(Component):
    """纯HTML包装组件，直接返回HTML字符串"""
    
    def __init__(self, html: str):
        super().__init__()
        self.html = html
    
    def render(self) -> str:
        return self.html
