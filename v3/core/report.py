"""
Report 核心类 - V3.0报告生成器核心
所有报告都通过此类生成，保证样式、结构、导航栏完全统一
"""
import sys
import os
import re

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core.config import SITE_NAME, SITE_ICON, COLORS, SIZES, BASE_PATH, REPORT_TYPES, BASE_CSS
from components.layout import Navbar, Footer, Section
from components.charts import get_chartjs_cdn


class Report:
    """
    报告生成器核心类
    
    使用方法:
    report = Report(title="报告标题", type="industry_chain")
    report.add(Section("标题", "内容"))
    report.add_data_card("市值", "1000亿")
    html = report.generate()
    """
    
    def __init__(self, title: str, report_type: str = "industry_chain", subtitle: str = None):
        self.title = title
        self.report_type = report_type
        self.subtitle = subtitle
        self.components = []  # 所有内容组件
        self._has_chart = False  # 是否包含图表（决定是否加载Chart.js）
    
    def add(self, component):
        """添加一个组件到报告中"""
        # 检查是否是图表组件
        component_name = type(component).__name__
        if "Chart" in component_name:
            self._has_chart = True
        
        self.components.append(component)
        return self  # 支持链式调用
    
    def add_section(self, title: str, content, subtitle: str = None, icon: str = None):
        """快捷添加Section"""
        from components.layout import Section
        self.add(Section(title, content, subtitle, icon))
        return self
    
    def add_data_grid(self, cards: list, cols: int = 4):
        """快捷添加数据卡片网格"""
        from components.data import DataGrid
        self.add(DataGrid(cards, cols))
        return self
    
    def add_risk_alert(self, level: str, text: str, title: str = None):
        """快捷添加风险提示"""
        from components.special import RiskAlert
        self.add(RiskAlert(level, text, title))
        return self
    
    def add_compare_table(self, headers: list, rows: list, **kwargs):
        """快捷添加对比表格"""
        from components.data import CompareTable
        self.add(CompareTable(headers, rows, **kwargs))
        return self
    
    def add_html(self, html: str):
        """直接添加原始HTML"""
        from components.base import HTMLComponent
        self.add(HTMLComponent(html))
        return self
    
    def _generate_head(self, force_chart: bool = False) -> str:
        """生成HTML头部
        
        Args:
            force_chart: 是否强制加载Chart.js（当检测到body中有图表时使用）
        """
        has_chart = self._has_chart or force_chart
        chart_js = get_chartjs_cdn() if has_chart else ""
        
        return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{self.title} - {SITE_NAME}</title>
    <meta name="description" content="{self.subtitle or self.title}">
    
    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    
    <!-- Chart.js -->
    {chart_js}
    
    <!-- 标准导航栏样式 -->
    {Navbar.get_css()}
    
    <!-- 基础样式 -->
    <style>
        body {{
            background: linear-gradient(135deg, {COLORS['gradient_start']} 0%, {COLORS['gradient_end']} 100%);
            min-height: 100vh;
            font-family: -apple-system, BlinkMacSystemFont, 'PingFang SC', 'Helvetica Neue', sans-serif;
            padding-top: 80px;
        }}
        
        .content-area {{
            max-width: 64rem;
            margin: 0 auto;
            padding: 0 1.5rem;
        }}
        
        /* 报告标题样式 */
        .report-header {{
            text-align: center;
            color: white;
            margin-bottom: 2rem;
        }}
        
        .report-header h1 {{
            font-size: 2rem;
            font-weight: 700;
            margin-bottom: 0.5rem;
            text-shadow: 0 2px 10px rgba(0,0,0,0.2);
        }}
        
        .report-header p {{
            opacity: 0.9;
            font-size: 1rem;
        }}
        
        /* 内容排版优化 */
        .prose-content p {{
            margin-bottom: 1.5rem;
            line-height: 1.8;
        }}
        
        .prose-content h3 {{
            font-size: 1.125rem;
            font-weight: 600;
            margin-top: 1.5rem;
            margin-bottom: 0.75rem;
            color: #1f2937;
        }}
        
        .prose-content h4 {{
            font-size: 1rem;
            font-weight: 600;
            margin-top: 1rem;
            margin-bottom: 0.5rem;
            color: #374151;
        }}
        
        .prose-content ul, .prose-content ol {{
            margin-bottom: 1.5rem;
            padding-left: 1.5rem;
        }}
        
        .prose-content li {{
            margin-bottom: 0.5rem;
            line-height: 1.7;
        }}
        
        .prose-content strong {{
            color: #1f2937;
            font-weight: 600;
        }}
        
        /* 代码块 */
        .prose-content code {{
            background: #f3f4f6;
            padding: 0.125rem 0.375rem;
            border-radius: 0.25rem;
            font-size: 0.875rem;
            font-family: 'SF Mono', Monaco, 'Courier New', monospace;
        }}
        
        .prose-content pre {{
            background: #1f2937;
            color: #e5e7eb;
            padding: 1rem;
            border-radius: 0.5rem;
            overflow-x: auto;
            margin-bottom: 1.5rem;
        }}
        
        .prose-content pre code {{
            background: none;
            padding: 0;
            color: inherit;
        }}
        
        /* 返回按钮 */
        .back-button {{
            display: inline-flex;
            align-items: center;
            color: white;
            opacity: 0.9;
            text-decoration: none;
            margin-bottom: 1.5rem;
            transition: opacity 0.2s;
        }}
        
        .back-button:hover {{
            opacity: 1;
        }}
        
        /* 移动端适配 */
        @media (max-width: 768px) {{
            .report-header h1 {{
                font-size: 1.5rem;
            }}
            
            body {{
                padding-top: 70px;
            }}
        }}
    </style>
</head>
<body>
"""
    
    def _generate_body(self) -> str:
        """生成HTML主体"""
        # 导航栏
        navbar_html = Navbar(active_key=self.report_type).render()
        
        # 返回链接
        type_info = REPORT_TYPES.get(self.report_type, {})
        list_path = type_info.get("list_file", "")
        dir_name = type_info.get("dir", "")
        
        if list_path and dir_name:
            back_url = f"{BASE_PATH}/{dir_name}/{list_path}"
            back_html = f'<a href="{back_url}" class="back-button">← 返回列表</a>'
        else:
            back_html = ""
        
        # 报告标题
        subtitle_html = f'<p class="text-white/80">{self.subtitle}</p>' if self.subtitle else ""
        header_html = f"""
        <div class="content-area">
            {back_html}
            <div class="report-header">
                <h1>{self.title}</h1>
                {subtitle_html}
            </div>
        </div>
        """
        
        # 内容区
        components_html = "\n".join(
            f'<div class="mb-10 last:mb-0">{comp.render() if hasattr(comp, "render") else str(comp)}</div>'
            for comp in self.components
        )
        
        content_html = f"""
        <div class="content-area">
            {components_html}
        </div>
        """
        
        # 页脚
        footer_html = Footer().render()
        
        return navbar_html + header_html + content_html + footer_html
    
    def generate(self) -> str:
        """生成完整的HTML报告"""
        # 先生成body，检测是否包含图表
        body_html = self._generate_body()
        has_chart = "<canvas" in body_html or "new Chart(" in body_html
        
        # 再生成head（根据是否有图表决定是否加载Chart.js）
        head_html = self._generate_head(force_chart=has_chart)
        
        return head_html + body_html + "\n</body>\n</html>"
    
    def save(self, filepath: str) -> str:
        """保存报告到文件，返回文件路径
        会检查受保护文件，防止意外覆盖
        """
        # 检查是否是受保护文件
        from core.config import PROTECTED_FILES
        filename = os.path.basename(filepath)
        for protected in PROTECTED_FILES:
            if filename == protected:
                raise PermissionError(f"不能覆盖受保护文件: {filepath}")
        
        html = self.generate()
        
        # 确保目录存在
        dir_path = os.path.dirname(filepath)
        if dir_path and not os.path.exists(dir_path):
            os.makedirs(dir_path, exist_ok=True)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
        
        return filepath
    
    def validate(self) -> list:
        """
        验证报告是否符合规范
        返回错误列表，空列表表示验证通过
        """
        from validators.structure import StructureValidator
        from validators.links import LinkValidator
        from validators.content import ContentValidator
        
        html = self.generate()
        errors = []
        
        errors.extend(StructureValidator.validate(html))
        errors.extend(LinkValidator.validate(html))
        errors.extend(ContentValidator.validate(html))
        
        return errors


class ReportBuilder:
    """
    报告构建器 - 用于快速构建特定类型的报告
    提供更高级的API
    """
    
    @staticmethod
    def deep_dive(title: str, **kwargs) -> Report:
        """创建深度研究报告"""
        return Report(title=title, report_type="industry_chain", **kwargs)
    
    @staticmethod
    def daily_report(title: str, **kwargs) -> Report:
        """创建日报"""
        return Report(title=title, report_type="daily", **kwargs)
    
    @staticmethod
    def catalyst(title: str, **kwargs) -> Report:
        """创建催化报告"""
        return Report(title=title, report_type="s_level_catalyst", **kwargs)
