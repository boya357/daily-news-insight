"""
生成器基类
所有专用生成器都继承自此基类，提供统一的 generate/save/validate/publish 接口
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.report import Report


class BaseGenerator:
    """生成器基类"""
    
    def __init__(self, report_type: str):
        self.report_type = report_type
        self.report = None  # 子类必须初始化
        self._components = []
    
    def generate(self) -> str:
        """生成HTML内容 - 子类必须实现"""
        raise NotImplementedError("子类必须实现 generate 方法")
    
    def save(self, filepath: str) -> str:
        """保存到文件"""
        self.generate()
        return self.report.save(filepath)
    
    def validate(self) -> list:
        """验证报告"""
        self.generate()
        return self.report.validate()
    
    def publish(self, title: str = None, report_type: str = None, 
                filename: str = None, excerpt: str = None,
                auto_deploy: bool = True, docs_root: str = "docs") -> dict:
        """
        一键发布：生成 → 归档 → 更新列表 → 校验 → Git部署
        
        Args:
            title: 报告标题（用于列表页显示）
            report_type: 报告类型（对应REPORT_TYPES的key），默认使用self.report_type
            filename: 文件名，不传则自动生成
            excerpt: 摘要（用于列表页展示）
            auto_deploy: 是否自动Git部署
            docs_root: docs目录路径
            
        Returns:
            发布结果字典
        """
        # 生成HTML
        html_content = self.generate()
        
        # 导入发布器（延迟导入避免循环导入）
        from workflow import ReportPublisher
        
        # 使用传入的类型或默认类型
        rtype = report_type or self.report_type
        display_title = title or getattr(self, 'display_title', '') or rtype
        
        # 发布
        publisher = ReportPublisher(docs_root=docs_root)
        return publisher.publish(
            html_content=html_content,
            title=display_title,
            report_type=rtype,
            filename=filename,
            excerpt=excerpt,
            auto_deploy=auto_deploy
        )
