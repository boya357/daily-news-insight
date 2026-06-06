"""
内容校验器 - 检查内容完整性、命名规范等
"""
import re
from core.config import FILENAME_PATTERN, DEPRECATED_DIRS


class ContentValidator:
    """内容校验器"""
    
    @staticmethod
    def validate(html: str) -> list:
        """执行所有内容校验"""
        errors = []
        
        errors.extend(ContentValidator._check_title(html))
        errors.extend(ContentValidator._check_deprecated_links(html))
        errors.extend(ContentValidator._check_template_placeholder(html))
        
        return errors
    
    @staticmethod
    def _check_title(html: str) -> list:
        """检查标题"""
        errors = []
        
        title_match = re.search(r"<title>(.*?)</title>", html)
        if not title_match:
            errors.append("[内容] 缺少title标签")
        elif not title_match.group(1).strip():
            errors.append("[内容] title标签为空")
        
        # 检查h1标题
        if "<h1" not in html:
            errors.append("[内容] 缺少h1标题")
        
        return errors
    
    @staticmethod
    def _check_deprecated_links(html: str) -> list:
        """检查是否有指向已废弃目录的链接"""
        errors = []
        
        for dep_dir in DEPRECATED_DIRS:
            if dep_dir in html:
                errors.append(f"[内容] 包含指向已废弃目录的链接: {dep_dir}")
        
        return errors
    
    @staticmethod
    def _check_template_placeholder(html: str) -> list:
        """检查是否有模板占位符残留"""
        errors = []
        
        placeholders = [
            "{{title}}",
            "{{content}}",
            "Lorem ipsum",
            "占位符",
            "template",
            "TODO",
        ]
        
        text_only = re.sub(r'<[^>]+>', '', html)  # 移除HTML标签
        
        for ph in placeholders:
            if ph.lower() in text_only.lower():
                errors.append(f"[内容] 可能包含模板占位符: '{ph}'")
        
        return errors
