"""
报告生成器基类 - Pro版
所有Pro版报告生成器都继承自此基类
提供统一的报告结构、深色玻璃态风格
"""
import sys
import os
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from components.pro import GlassCard, SectionTitle, TagBadge
from generators.pro_base import ProGenerator


class ReportProGenerator(ProGenerator):
    """报告生成器基类 - Pro版"""
    
    def __init__(self, 
                 title: str = "报告",
                 report_type: str = "daily",
                 subtitle: str = "",
                 date_str: str = None,
                 data_dir: str = "data",
                 theme: str = "dark"):
        super().__init__(
            title=title,
            active_page="首页",
            footer_text=f"{title} · 投资研究中心",
            data_dir=data_dir,
            show_toc=True,
            theme=theme,
        )
        self.report_type = report_type
        self.subtitle = subtitle
        self.date_str = date_str or datetime.now().strftime('%Y-%m-%d')
        self._sections = []
    
    def add_section(self, title: str, content: str, icon: str = "📄", extra_class: str = ""):
        """添加一个章节"""
        self._sections.append({
            'title': title,
            'content': content,
            'icon': icon,
            'extra_class': extra_class,
        })
    
    def _generate_header(self) -> str:
        """生成报告头部"""
        return f'''
        <div class="text-center mb-10">
            <h1 class="text-3xl md:text-4xl font-black text-white mb-3">
                {self.title}
            </h1>
            <p class="text-white/70 text-lg">
                {self.subtitle}
            </p>
            <p class="text-white/50 text-sm mt-2">
                {self.date_str}
            </p>
        </div>
        '''
    
    def _generate_sections(self) -> str:
        """生成所有章节"""
        sections_html = ''
        for section in self._sections:
            content = f'''
                <h2 class="text-lg font-bold text-white mb-4">
                    <span class="text-blue-400 mr-2">{section['icon']}</span>
                    {section['title']}
                </h2>
                <div class="text-white/80">
                    {section['content']}
                </div>
            '''
            extra = section.get('extra_class', '')
            sections_html += GlassCard(
                content=content, 
                padding="p-6", 
                extra_class=f"mb-6 {extra}"
            ).render()
        
        return sections_html
    
    def _content(self) -> str:
        """页面主要内容"""
        return f'''
        <div class="max-w-4xl mx-auto">
            {self._generate_header()}
            {self._generate_sections()}
        </div>
        '''


if __name__ == "__main__":
    # 测试基类
    gen = ReportProGenerator(title="测试报告", subtitle="这是一个测试")
    gen.add_section("测试章节", "<p>这是测试内容</p>", "📊")
    html = gen.render()
    print(f"生成成功，长度：{len(html)}")
