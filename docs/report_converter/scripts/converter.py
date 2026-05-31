#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MLCC Pro v2.0 报告转换工具
将旧版HTML报告批量升级为统一的MLCC Pro模板

三级模板体系：
- Level 1: 深度研报（完整功能 + 图表支持）
- Level 2: 标准报告（周复盘、月报等）
- Level 3: 轻量快报（日报、盘中、盘后）
"""

import os
import re
from pathlib import Path

class ReportConverter:
    def __init__(self, templates_dir):
        self.templates_dir = Path(templates_dir)
        self._load_templates()
    
    def _load_templates(self):
        """加载三级模板"""
        self.templates = {}
        
        # Level 1: 深度研报模板
        level1_path = self.templates_dir / 'level1_deep_report.html'
        if level1_path.exists():
            with open(level1_path, 'r', encoding='utf-8') as f:
                self.templates['level1'] = f.read()
        
        # Level 2: 标准报告模板
        level2_path = self.templates_dir / 'level2_standard_report.html'
        if level2_path.exists():
            with open(level2_path, 'r', encoding='utf-8') as f:
                self.templates['level2'] = f.read()
        
        # Level 3: 轻量快报模板
        level3_path = self.templates_dir / 'level3_quick_report.html'
        if level3_path.exists():
            with open(level3_path, 'r', encoding='utf-8') as f:
                self.templates['level3'] = f.read()
        
        print(f"✅ 已加载 {len(self.templates)} 个模板")
    
    def detect_level(self, file_path):
        """根据文件名自动判断报告级别"""
        path_str = str(file_path).lower()
        
        # 深度研报
        if any(x in path_str for x in ['深度', 'deep', '产业链', 'n1x', 'hbm']):
            return 'level1'
        
        # 轻量快报
        if any(x in path_str for x in ['daily', '盘中', '盘后', 'intraday', 'aftermarket']):
            return 'level3'
        
        # 默认标准报告
        return 'level2'
    
    def extract_content(self, old_html):
        """从旧HTML中提取核心内容"""
        # 提取标题
        title_match = re.search(r'<title>(.*?)</title>', old_html)
        title = title_match.group(1).split('|')[0].strip() if title_match else '未命名报告'
        
        # 提取主体内容（简单提取容器内的内容）
        content = ''
        
        # 尝试多种容器模式
        patterns = [
            r'<div class="container.*?">(.*?)</div>\s*</body>',
            r'<div class="max-w-4xl.*?">(.*?)</div>\s*</body>',
            r'<body.*?>(.*?)</body>'
        ]
        
        for pattern in patterns:
            match = re.search(pattern, old_html, re.DOTALL)
            if match:
                content = match.group(1)
                # 移除导航栏
                content = re.sub(r'<nav.*?</nav>', '', content, flags=re.DOTALL)
                # 移除header
                content = re.sub(r'<header.*?</header>', '', content, flags=re.DOTALL)
                # 移除script
                content = re.sub(r'<script.*?</script>', '', content, flags=re.DOTALL)
                break
        
        return {
            'title': title,
            'content': content.strip()
        }
    
    def convert_file(self, input_path, output_path=None, level=None):
        """转换单个文件"""
        input_path = Path(input_path)
        
        # 读取旧文件
        with open(input_path, 'r', encoding='utf-8') as f:
            old_html = f.read()
        
        # 自动判断级别
        if level is None:
            level = self.detect_level(input_path)
        
        # 提取内容
        data = self.extract_content(old_html)
        
        # 获取模板
        template = self.templates.get(level, self.templates.get('level2'))
        
        # 填充模板
        new_html = template
        new_html = new_html.replace('{{REPORT_TITLE}}', data['title'])
        new_html = new_html.replace('{{REPORT_DATE}}', '')
        new_html = new_html.replace('{{REPORT_CONTENT}}', data['content'])
        new_html = new_html.replace('{{REPORT_TYPE}}', f'{level.upper()} 报告')
        new_html = new_html.replace('{{REPORT_TAGS}}', '<span class="tag tag-primary">已升级</span>')
        
        # 清理空的模板变量
        new_html = re.sub(r'{{.*?}}', '', new_html)
        
        # 保存
        if output_path is None:
            output_path = input_path.parent / f'{input_path.stem}_pro{input_path.suffix}'
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(new_html)
        
        print(f"✅ {input_path.name} → {output_path.name} ({level})")
        return output_path
    
    def batch_convert(self, directory, pattern='*.html', output_dir=None):
        """批量转换目录下的所有报告"""
        directory = Path(directory)
        html_files = list(directory.rglob(pattern))
        
        # 排除模板文件和已转换的文件
        html_files = [f for f in html_files if '_templates' not in str(f) and '_pro' not in str(f)]
        
        print(f"\n🔍 找到 {len(html_files)} 个待转换文件")
        
        if output_dir:
            output_dir = Path(output_dir)
            output_dir.mkdir(parents=True, exist_ok=True)
        else:
            output_dir = directory
        
        results = []
        for html_file in html_files:
            try:
                output_path = output_dir / html_file.name
                result = self.convert_file(html_file, output_path)
                results.append(result)
            except Exception as e:
                print(f"❌ {html_file.name}: {e}")
        
        print(f"\n🎉 批量转换完成！共 {len(results)} 个文件已升级为MLCC Pro标准")
        return results

def main():
    """命令行入口"""
    import sys
    
    # 默认模板目录
    script_dir = Path(__file__).parent
    templates_dir = script_dir.parent / 'templates'
    
    converter = ReportConverter(templates_dir)
    
    if len(sys.argv) < 2:
        print("""
MLCC Pro v2.0 报告批量转换工具

使用方法:
  python converter.py <文件或目录> [输出目录]
  
示例:
  python converter.py daily/20260530_每日新闻洞察.html
  python converter.py daily/ converted/

        """)
        return
    
    input_path = Path(sys.argv[1])
    output_dir = sys.argv[2] if len(sys.argv) > 2 else None
    
    if input_path.is_file():
        converter.convert_file(input_path, output_dir)
    elif input_path.is_dir():
        converter.batch_convert(input_path, output_dir=output_dir)
    else:
        print(f"❌ 路径不存在: {input_path}")

if __name__ == '__main__':
    main()
