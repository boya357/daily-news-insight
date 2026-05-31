#!/usr/bin/env python3
"""
统一报告生成入口
一键生成任何类型的HTML报告
"""
import sys
import os

# 添加当前目录到路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from converter import ReportConverter
from list_updater import ListPageUpdater


def generate_single_report(md_file: str, html_file: str, report_type: str = 'industry_chain'):
    """生成单篇报告"""
    if not os.path.exists(md_file):
        print(f"❌ 文件不存在: {md_file}")
        return False
    
    converter = ReportConverter()
    return converter.convert(md_file, html_file, report_type)


def update_list_pages(docs_dir: str, *page_types):
    """更新列表页"""
    updater = ListPageUpdater(docs_dir)
    
    if page_types:
        for page_type in page_types:
            updater.update_single(page_type)
    else:
        updater.update_all()


def main():
    """主入口"""
    if len(sys.argv) < 2:
        print("""
📊 专业报告生成工具 - 完整版本

用法:
  1. 生成单篇报告:
     python generate_report.py convert <md文件> <html输出文件> [报告类型]
     
     报告类型: daily, intraday, aftermarket, industry_chain, weekly_review
  
  2. 更新列表页:
     python generate_report.py update-list <docs目录> [页面类型...]
     
  3. 完整流程（转换 + 更新列表）:
     python generate_report.py full <md文件> <html输出文件> <报告类型> <docs目录>

示例:
  # 生成产业链深度报告
  python generate_report.py convert docs/industry_chain/n1x.md docs/industry_chain/n1x.html industry_chain
  
  # 更新所有列表页
  python generate_report.py update-list docs
  
  # 完整流程
  python generate_report.py full docs/daily/20260531.md docs/daily/20260531.html daily docs
        """)
        return
    
    command = sys.argv[1]
    
    if command == 'convert':
        if len(sys.argv) < 4:
            print("❌ 请指定MD文件和HTML文件")
            return
        md_file = sys.argv[2]
        html_file = sys.argv[3]
        report_type = sys.argv[4] if len(sys.argv) > 4 else 'industry_chain'
        generate_single_report(md_file, html_file, report_type)
    
    elif command == 'update-list':
        if len(sys.argv) < 3:
            print("❌ 请指定docs目录")
            return
        docs_dir = sys.argv[2]
        page_types = sys.argv[3:] if len(sys.argv) > 3 else None
        update_list_pages(docs_dir, *page_types)
    
    elif command == 'full':
        if len(sys.argv) < 6:
            print("❌ 完整用法: python generate_report.py full <md文件> <html文件> <报告类型> <docs目录>")
            return
        md_file = sys.argv[2]
        html_file = sys.argv[3]
        report_type = sys.argv[4]
        docs_dir = sys.argv[5]
        
        # 1. 生成报告
        success = generate_single_report(md_file, html_file, report_type)
        if not success:
            print("❌ 报告生成失败")
            return
        
        # 2. 更新列表页
        update_list_pages(docs_dir, report_type)
        print("✅ 完整流程完成！")
    
    else:
        print(f"❌ 未知命令: {command}")


if __name__ == '__main__':
    main()
