"""
工具函数
"""
import re
import os
from datetime import datetime


def sanitize_filename(filename: str) -> str:
    """清理文件名，移除非法字符"""
    # 替换空格和特殊字符
    filename = re.sub(r'[\\/*?:"<>|]', '_', filename)
    return filename


def format_date(date_str: str = None, format: str = "%Y-%m-%d") -> str:
    """格式化日期"""
    if date_str is None:
        return datetime.now().strftime(format)
    
    if isinstance(date_str, datetime):
        return date_str.strftime(format)
    
    return date_str


def get_project_root() -> str:
    """获取项目根目录"""
    # 向上找两层（v3/utils/ -> v3/ -> 项目根）
    current = os.path.dirname(os.path.abspath(__file__))
    return os.path.dirname(os.path.dirname(current))


def ensure_dir(path: str) -> str:
    """确保目录存在，返回路径"""
    if not os.path.exists(path):
        os.makedirs(path, exist_ok=True)
    return path


def html_to_text(html: str) -> str:
    """简单的HTML转纯文本"""
    text = re.sub(r'<[^>]+>', '', html)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()


def truncate_text(text: str, max_length: int = 100) -> str:
    """截断文本"""
    if len(text) <= max_length:
        return text
    return text[:max_length] + "..."
