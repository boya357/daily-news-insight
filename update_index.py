#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
首页自动更新脚本
策略：读取现有index.html，只更新【第一区】最新发布横幅内容
其他所有模块完全保持原样，不做任何修改
用法: python3 update_index.py
"""

import os
import glob
import re

# 最新报告卡片模板（保持原有样式）
FEATURED_REPORT_TEMPLATE = '''<a href="{filepath}" class="block bg-gradient-to-r from-blue-500/20 to-cyan-500/20 border border-blue-400/30 rounded-xl p-4 hover:from-blue-500/30 hover:to-cyan-500/30 transition-all group">
    <div class="flex items-center gap-3 mb-2">
        <span class="text-3xl">{icon}</span>
        <div>
            <h3 class="font-bold text-lg group-hover:text-yellow-300 transition-colors">{title}</h3>
            <p class="text-white/70 text-sm">{desc}</p>
        </div>
    </div>
</a>
'''

def get_latest_report(directory, icon, title_prefix, desc):
    """获取指定目录下最新的报告文件（排除latest.html）"""
    # 只匹配YYYYMMDD开头的报告文件，排除latest.html
    all_files = [f for f in glob.glob(f'{directory}/*.html') if os.path.basename(f).startswith('202')]
    if not all_files:
        return None
    
    # 按时间倒序排序，取最新
    all_files.sort(reverse=True)
    latest_file = all_files[0]
    filename = os.path.basename(latest_file)
    date_str = filename[:8]
    
    # 转换为相对路径（相对于docs目录）
    rel_path = os.path.relpath(latest_file, 'docs')
    
    return FEATURED_REPORT_TEMPLATE.format(
        filepath=rel_path,
        icon=icon,
        title=f'{date_str} {title_prefix}',
        desc=desc
    )

def main():
    # 切换到脚本所在目录
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    # 1. 读取现有的index.html文件
    index_path = 'docs/index.html'
    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 2. 获取最新报告
    reports = []
    
    # S级催化扫描
    s_report = get_latest_report('docs/s级催化扫描', '⭐', 'S级催化扫描', '超级催化事件深度挖掘')
    if s_report:
        reports.append(s_report)
    
    # 每日新闻洞察
    daily_report = get_latest_report('docs/daily', '📰', '每日新闻洞察', '早间市场综述与机会挖掘')
    if daily_report:
        reports.append(daily_report)
    
    # 产业链报告
    chain_report = get_latest_report('docs/industry_chain', '🔗', '产业链深度研究', '产业逻辑与弹性测算')
    if chain_report:
        reports.append(chain_report)
    
    # 只取最新的2个显示在横幅
    latest_reports = reports[:2]
    
    print(f'✅ 扫描到 {len(latest_reports)} 个最新报告')
    
    # 3. 生成新的最新发布HTML
    report_html = '\n'.join(latest_reports)
    
    # 4. 构建新的【第一区】最新发布横幅
    new_featured_section = f'''<!-- 【第一区】最新发布横幅 - 突出显示最新报告 -->
        <div class="featured-banner rounded-2xl p-6 mb-6 text-white shadow-2xl">
            <div class="flex items-center justify-between mb-4">
                <div class="flex items-center gap-3">
                    <div class="relative">
                        <div class="w-4 h-4 bg-yellow-400 rounded-full"></div>
                        <div class="pulse-ring absolute inset-0 w-4 h-4 bg-yellow-400 rounded-full opacity-75"></div>
                    </div>
                    <span class="text-yellow-300 font-bold text-sm">✨ 最新发布</span>
                </div>
                <span class="text-white/60 text-xs">刚刚更新</span>
            </div>
            <div class="grid grid-cols-2 gap-4">
                {report_html}
            </div>
        </div>'''
    
    # 5. 用正则替换【第一区】的内容
    # 匹配从"<!-- 【第一区】"开始到下一个"<!-- 【第二区】"或"<!-- 【"之前的内容
    pattern = r'<!-- 【第一区】最新发布横幅.*?--\>\s*<div class="featured-banner.*?</div>'
    new_content = re.sub(pattern, new_featured_section, content, flags=re.DOTALL)
    
    # 6. 写回文件
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f'✅ 已更新 {index_path}')
    print(f'✅ 仅更新了【第一区】最新发布横幅，其他所有模块完全保持原样')

if __name__ == '__main__':
    main()