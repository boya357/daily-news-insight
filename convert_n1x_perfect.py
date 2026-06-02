#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
基于MLCC完美模板的N1X报告转换脚本
确保样式100%一致
"""

import re

def convert_markdown_to_html(md_content):
    """将Markdown内容转换为适配模板的HTML"""
    
    # 处理表格
    def replace_table(match):
        table_content = match.group(1)
        lines = [l.strip() for l in table_content.strip().split('\n') if l.strip()]
        
        if len(lines) < 3:
            return match.group(0)
        
        # 表头
        headers = [h.strip() for h in lines[0].split('|')[1:-1]]
        
        # 数据行
        rows = []
        for line in lines[2:]:
            cells = [c.strip() for c in line.split('|')[1:-1]]
            rows.append(cells)
        
        # 生成HTML表格
        html = '<div class="overflow-x-auto mb-8"><table class="w-full text-sm table-shadow rounded-xl overflow-hidden">'
        html += '<thead class="bg-gradient-to-r from-primary to-secondary text-white"><tr>'
        for h in headers:
            html += f'<th class="px-6 py-4 text-left">{h}</th>'
        html += '</tr></thead><tbody class="bg-white divide-y divide-gray-200">'
        
        for row in rows:
            html += '<tr class="hover:bg-light/50 transition-colors">'
            for i, cell in enumerate(row):
                if i == 0:
                    html += f'<td class="px-6 py-4 font-medium">{cell}</td>'
                else:
                    html += f'<td class="px-6 py-4">{cell}</td>'
            html += '</tr>'
        
        html += '</tbody></table></div>'
        return html
    
    # 替换表格
    md_content = re.sub(r'((?:\|.*?\|\n)+)', replace_table, md_content, flags=re.DOTALL)
    
    # 处理标题
    md_content = re.sub(r'^### (.*?)$', r'<h4 class="font-bold text-dark mb-4">\1</h4>', md_content, flags=re.MULTILINE)
    md_content = re.sub(r'^## (.*?)$', r'<h3 class="text-2xl font-bold text-primary mb-6 border-l-4 border-primary pl-4">\1</h3>', md_content, flags=re.MULTILINE)
    md_content = re.sub(r'^# (.*?)$', r'<h2 class="text-4xl font-bold text-dark mb-8">\1</h2>', md_content, flags=re.MULTILINE)
    
    # 处理列表项
    md_content = re.sub(r'^- (.*?)$', r'<li class="flex items-start"><span class="text-accent mr-2">▸</span>\1</li>', md_content, flags=re.MULTILINE)
    
    # 处理粗体
    md_content = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', md_content)
    
    # 处理段落
    lines = md_content.split('\n')
    in_list = False
    result = []
    
    for line in lines:
        if line.strip().startswith('<li'):
            if not in_list:
                result.append('<ul class="space-y-3 text-gray-700">')
                in_list = True
            result.append(line)
        elif line.strip().startswith('<h') or line.strip().startswith('<div') or line.strip().startswith('<table') or line.strip().startswith('</div') or line.strip().startswith('</table'):
            if in_list:
                result.append('</ul>')
                in_list = False
            result.append(line)
        elif line.strip():
            if in_list:
                result.append('</ul>')
                in_list = False
            result.append(f'<p class="text-gray-700 mb-6 leading-relaxed">{line}</p>')
    
    if in_list:
        result.append('</ul>')
    
    return '\n'.join(result)

# 读取MLCC模板
with open('docs/industry_chain/20260529_MLCC全产业链深度研究报告.html', 'r', encoding='utf-8') as f:
    template = f.read()

# 读取N1X报告
with open('recent_memory/project/20260530_英伟达N1X芯片与COMPUTEX深度研究报告.md', 'r', encoding='utf-8') as f:
    n1x_md = f.read()

# ========== 1. 替换标题和导航 ==========
template = template.replace('MLCC全产业链深度研究报告 | 2026年5月', '英伟达N1X芯片与COMPUTEX 2026深度研究报告')
template = template.replace('📊 MLCC产业链深度研究', '🚀 英伟达N1X深度研究')
template = template.replace('发布日期：2026年5月29日', '发布日期：2026年5月30日')

# ========== 2. 替换主标题区 ==========
old_header = '''            <h1 class="text-5xl font-bold text-white mb-6 text-shadow">
                MLCC全产业链深度研究报告
            </h1>
            <p class="text-2xl text-white/90 mb-8">
                片式多层陶瓷电容器 — AI算力时代的"电子工业大米"
            </p>
            <div class="flex justify-center gap-8 flex-wrap">
                <div class="bg-white/20 backdrop-blur-sm rounded-2xl px-8 py-4 text-white">
                    <div class="text-3xl font-bold">1.28万亿颗</div>
                    <div class="text-sm opacity-80">国产替代空间（50%替代）</div>
                </div>
                <div class="bg-white/20 backdrop-blur-sm rounded-2xl px-8 py-4 text-white">
                    <div class="text-3xl font-bold">77.3%</div>
                    <div class="text-sm opacity-80">日韩厂商全球市占率(CR5)</div>
                </div>
                <div class="bg-white/20 backdrop-blur-sm rounded-2xl px-8 py-4 text-white">
                    <div class="text-3xl font-bold">44万颗</div>
                    <div class="text-sm opacity-80">AI机柜MLCC用量</div>
                </div>
                <div class="bg-white/20 backdrop-blur-sm rounded-2xl px-8 py-4 text-white">
                    <div class="text-3xl font-bold">15%-35%</div>
                    <div class="text-sm opacity-80">本轮涨价幅度</div>
                </div>
            </div>'''

new_header = '''            <h1 class="text-5xl font-bold text-white mb-6 text-shadow">
                英伟达N1X芯片与COMPUTEX 2026深度研究报告
            </h1>
            <p class="text-2xl text-white/90 mb-8">
                Arm PC新时代 + Vera Rubin超级算力 — 黄仁勋6月1日台北演讲前瞻
            </p>
            <div class="flex justify-center gap-8 flex-wrap">
                <div class="bg-white/20 backdrop-blur-sm rounded-2xl px-8 py-4 text-white">
                    <div class="text-3xl font-bold">200 TOPS</div>
                    <div class="text-sm opacity-80">N1X端侧AI算力</div>
                </div>
                <div class="bg-white/20 backdrop-blur-sm rounded-2xl px-8 py-4 text-white">
                    <div class="text-3xl font-bold">35×</div>
                    <div class="text-sm opacity-80">Rubin推理吞吐量提升</div>
                </div>
                <div class="bg-white/20 backdrop-blur-sm rounded-2xl px-8 py-4 text-white">
                    <div class="text-3xl font-bold">6月1日</div>
                    <div class="text-sm opacity-80">黄仁勋台北演讲</div>
                </div>
                <div class="bg-white/20 backdrop-blur-sm rounded-2xl px-8 py-4 text-white">
                    <div class="text-3xl font-bold">435%</div>
                    <div class="text-sm opacity-80">HBM内存价值量涨幅</div>
                </div>
            </div>'''

template = template.replace(old_header, new_header)

# ========== 3. 替换核心摘要 ==========
old_summary = '''                <h3 class="text-xl font-semibold text-primary mb-4">投资要点</h3>
                        <ul class="space-y-3 text-gray-700">
                            <li class="flex items-start">
                                <span class="text-accent mr-2">▸</span>
                                <strong>AI算力爆发</strong>：AI服务器MLCC用量是传统服务器10倍，单机价值量增长182%
                            </li>
                            <li class="flex items-start">
                                <span class="text-accent mr-2">▸</span>
                                <strong>供需缺口扩大</strong>：2026年全球MLCC需求1.61万亿颗，供给1.57万亿颗，缺口400亿颗
                            </li>
                            <li class="flex items-start">
                                <span class="text-accent mr-2">▸</span>
                                <strong>涨价周期开启</strong>：村田、三星电机启动涨价，高端型号涨幅15%-35%，交期延至16-24周
                            </li>
                            <li class="flex items-start">
                                <span class="text-accent mr-2">▸</span>
                                <strong>国产替代加速</strong>：地缘政治推动供应链自主，AI+车规高端市场突破在即
                            </li>
                        </ul>
                    </div>
                    <div>
                        <h3 class="text-xl font-semibold text-primary mb-4">五星标的推荐</h3>
                        <div class="space-y-3">
                            <div class="flex items-center justify-between bg-light rounded-xl p-4">
                                <div>
                                    <span class="font-bold text-dark">风华高科</span>
                                    <span class="text-sm text-gray-500 ml-2">000636</span>
                                </div>
                                <span class="bg-primary text-white px-3 py-1 rounded-full text-sm">AI+车规双认证</span>
                            </div>
                            <div class="flex items-center justify-between bg-light rounded-xl p-4">
                                <div>
                                    <span class="font-bold text-dark">国瓷材料</span>
                                    <span class="text-sm text-gray-500 ml-2">300285</span>
                                </div>
                                <span class="bg-secondary text-white px-3 py-1 rounded-full text-sm">陶瓷粉体龙头</span>
                            </div>
                            <div class="flex items-center justify-between bg-light rounded-xl p-4">
                                <div>
                                    <span class="font-bold text-dark">三环集团</span>
                                    <span class="text-sm text-gray-500 ml-2">300408</span>
                                </div>
                                <span class="bg-accent text-white px-3 py-1 rounded-full text-sm">全产业链优势</span>
                            </div>
                        </div>'''

new_summary = '''                <h3 class="text-xl font-semibold text-primary mb-4">投资要点</h3>
                        <ul class="space-y-3 text-gray-700">
                            <li class="flex items-start">
                                <span class="text-accent mr-2">▸</span>
                                <strong>N1X Arm PC发布</strong>：英伟达首款自研Arm架构PC处理器，20核CPU+RTX 5070级GPU，开启PC新时代
                            </li>
                            <li class="flex items-start">
                                <span class="text-accent mr-2">▸</span>
                                <strong>Vera Rubin超级架构</strong>：Rubin GPU采用HBM4+CoWoS-L，推理吞吐量提升35倍，每Token成本降至1/10
                            </li>
                            <li class="flex items-start">
                                <span class="text-accent mr-2">▸</span>
                                <strong>产业链价值重构</strong>：GPU成本占比从65%降至51%，HBM内存暴涨435%，PCB暴涨233%
                            </li>
                            <li class="flex items-start">
                                <span class="text-accent mr-2">▸</span>
                                <strong>COMPUTEX催化</strong>：黄仁勋6月1日台北演讲将点燃AI算力板块，供应链二季度业绩验证在即
                            </li>
                        </ul>
                    </div>
                    <div>
                        <h3 class="text-xl font-semibold text-primary mb-4">五星标的推荐</h3>
                        <div class="space-y-3">
                            <div class="flex items-center justify-between bg-light rounded-xl p-4">
                                <div>
                                    <span class="font-bold text-dark">胜宏科技</span>
                                    <span class="text-sm text-gray-500 ml-2">300476</span>
                                </div>
                                <span class="bg-primary text-white px-3 py-1 rounded-full text-sm">GPU PCB全球第一</span>
                            </div>
                            <div class="flex items-center justify-between bg-light rounded-xl p-4">
                                <div>
                                    <span class="font-bold text-dark">工业富联</span>
                                    <span class="text-sm text-gray-500 ml-2">601138</span>
                                </div>
                                <span class="bg-secondary text-white px-3 py-1 rounded-full text-sm">AI服务器代工70%+</span>
                            </div>
                            <div class="flex items-center justify-between bg-light rounded-xl p-4">
                                <div>
                                    <span class="font-bold text-dark">中际旭创</span>
                                    <span class="text-sm text-gray-500 ml-2">300308</span>
                                </div>
                                <span class="bg-accent text-white px-3 py-1 rounded-full text-sm">1.6T光模块龙头</span>
                            </div>
                        </div>'''

template = template.replace(old_summary, new_summary)

# ========== 4. 替换目录导航 ==========
old_toc = '''                <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-4">
                    <a href="#section1" class="group bg-gradient-to-r from-primary/5 to-secondary/5 hover:from-primary/10 hover:to-secondary/10 rounded-xl p-5 transition-all border border-primary/10">
                        <div class="text-2xl mb-2">一</div>
                        <h3 class="font-bold text-dark group-hover:text-primary transition-colors">上游产业链分析</h3>
                        <p class="text-sm text-gray-500 mt-2">陶瓷粉体、电极材料、生产设备、辅材</p>
                    </a>
                    <a href="#section2" class="group bg-gradient-to-r from-primary/5 to-secondary/5 hover:from-primary/10 hover:to-secondary/10 rounded-xl p-5 transition-all border border-primary/10">
                        <div class="text-2xl mb-2">二</div>
                        <h3 class="font-bold text-dark group-hover:text-primary transition-colors">中游制造格局</h3>
                        <p class="text-sm text-gray-500 mt-2">全球五梯队、技术壁垒、产能分析、价格周期</p>
                    </a>
                    <a href="#section3" class="group bg-gradient-to-r from-primary/5 to-secondary/5 hover:from-primary/10 hover:to-secondary/10 rounded-xl p-5 transition-all border border-primary/10">
                        <div class="text-2xl mb-2">三</div>
                        <h3 class="font-bold text-dark group-hover:text-primary transition-colors">下游需求爆发</h3>
                        <p class="text-sm text-gray-500 mt-2">消费电子、汽车电子、AI服务器、增量场景</p>
                    </a>
                    <a href="#section4" class="group bg-gradient-to-r from-primary/5 to-secondary/5 hover:from-primary/10 hover:to-secondary/10 rounded-xl p-5 transition-all border border-primary/10">
                        <div class="text-2xl mb-2">四</div>
                        <h3 class="font-bold text-dark group-hover:text-primary transition-colors">产业链对比与预判</h3>
                        <p class="text-sm text-gray-500 mt-2">国产化率、传导时序、业绩弹性、投资时钟</p>
                    </a>
                    <a href="#section5" class="group bg-gradient-to-r from-primary/5 to-secondary/5 hover:from-primary/10 hover:to-secondary/10 rounded-xl p-5 transition-all border border-primary/10">
                        <div class="text-2xl mb-2">五</div>
                        <h3 class="font-bold text-dark group-hover:text-primary transition-colors">价值分布图</h3>
                        <p class="text-sm text-gray-500 mt-2">利润分配、成本结构、价值传导</p>
                    </a>
                    <a href="#section6" class="group bg-gradient-to-r from-primary/5 to-secondary/5 hover:from-primary/10 hover:to-secondary/10 rounded-xl p-5 transition-all border border-primary/10">
                        <div class="text-2xl mb-2">六</div>
                        <h3 class="font-bold text-dark group-hover:text-primary transition-colors">风险与投资策略</h3>
                        <p class="text-sm text-gray-500 mt-2">风险提示、投资策略、核心标的组合</p>
                    </a>
                </div>'''

new_toc = '''                <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-4">
                    <a href="#section1" class="group bg-gradient-to-r from-primary/5 to-secondary/5 hover:from-primary/10 hover:to-secondary/10 rounded-xl p-5 transition-all border border-primary/10">
                        <div class="text-2xl mb-2">一</div>
                        <h3 class="font-bold text-dark group-hover:text-primary transition-colors">N1X芯片规格详解</h3>
                        <p class="text-sm text-gray-500 mt-2">核心参数、性能对比、能效优势、与H100定位差异</p>
                    </a>
                    <a href="#section2" class="group bg-gradient-to-r from-primary/5 to-secondary/5 hover:from-primary/10 hover:to-secondary/10 rounded-xl p-5 transition-all border border-primary/10">
                        <div class="text-2xl mb-2">二</div>
                        <h3 class="font-bold text-dark group-hover:text-primary transition-colors">黄仁勋演讲前瞻</h3>
                        <p class="text-sm text-gray-500 mt-2">N1X发布、Vera Rubin、NVL72超级计算机、AI工厂</p>
                    </a>
                    <a href="#section3" class="group bg-gradient-to-r from-primary/5 to-secondary/5 hover:from-primary/10 hover:to-secondary/10 rounded-xl p-5 transition-all border border-primary/10">
                        <div class="text-2xl mb-2">三</div>
                        <h3 class="font-bold text-dark group-hover:text-primary transition-colors">上下游产业链全景</h3>
                        <p class="text-sm text-gray-500 mt-2">晶圆封装、HBM存储、PCB载板、整机代工、光模块</p>
                    </a>
                    <a href="#section4" class="group bg-gradient-to-r from-primary/5 to-secondary/5 hover:from-primary/10 hover:to-secondary/10 rounded-xl p-5 transition-all border border-primary/10">
                        <div class="text-2xl mb-2">四</div>
                        <h3 class="font-bold text-dark group-hover:text-primary transition-colors">A股标的弹性测算</h3>
                        <p class="text-sm text-gray-500 mt-2">核心受益标的、业绩弹性系数、价值重构分析</p>
                    </a>
                    <a href="#section5" class="group bg-gradient-to-r from-primary/5 to-secondary/5 hover:from-primary/10 hover:to-secondary/10 rounded-xl p-5 transition-all border border-primary/10">
                        <div class="text-2xl mb-2">五</div>
                        <h3 class="font-bold text-dark group-hover:text-primary transition-colors">市场影响分析</h3>
                        <p class="text-sm text-gray-500 mt-2">短期催化、中期趋势、板块轮动、投资策略</p>
                    </a>
                    <a href="#section6" class="group bg-gradient-to-r from-primary/5 to-secondary/5 hover:from-primary/10 hover:to-secondary/10 rounded-xl p-5 transition-all border border-primary/10">
                        <div class="text-2xl mb-2">六</div>
                        <h3 class="font-bold text-dark group-hover:text-primary transition-colors">风险提示与结论</h3>
                        <p class="text-sm text-gray-500 mt-2">产能风险、估值风险、地缘政治、核心结论</p>
                    </a>
                </div>'''

template = template.replace(old_toc, new_toc)

# ========== 5. 生成第一章节内容（N1X芯片规格） ==========
section1_content = '''                <h3 class="text-2xl font-bold text-primary mb-6 border-l-4 border-primary pl-4">1.1 核心规格参数 — 20核CPU+RTX 5070级GPU的超级SoC</h3>
                
                <div class="grid lg:grid-cols-2 gap-8 mb-8">
                    <div>
                        <p class="text-gray-700 mb-6 leading-relaxed">
                            N1X是英伟达首款自研Arm架构PC处理器，由英伟达与联发科联合开发，基于Grace Blackwell架构修改而来，定位Windows on ARM旗舰SoC。
                            这是英伟达首次进军消费级PC市场，标志着"AI PC新时代"的正式开启。
                        </p>
                        <div class="bg-light rounded-xl p-6">
                            <h4 class="font-bold text-dark mb-4">N1X核心规格表</h4>
                            <table class="w-full text-sm">
                                <thead>
                                    <tr class="border-b border-gray-300">
                                        <th class="text-left py-2 text-gray-600">项目</th>
                                        <th class="text-left py-2 text-gray-600">详细规格</th>
                                    </tr>
                                </thead>
                                <tbody class="text-gray-700">
                                    <tr class="border-b border-gray-200">
                                        <td class="py-2 font-medium">制程工艺</td>
                                        <td>台积电N3B（3nm）</td>
                                    </tr>
                                    <tr class="border-b border-gray-200">
                                        <td class="py-2 font-medium">CPU架构</td>
                                        <td>20核异构设计，ARMv9.2架构</td>
                                    </tr>
                                    <tr class="border-b border-gray-200">
                                        <td class="py-2 font-medium">CPU核心</td>
                                        <td>10颗Cortex-X925性能大核 + 10颗Cortex-A725能效小核</td>
                                    </tr>
                                    <tr class="border-b border-gray-200">
                                        <td class="py-2 font-medium">GPU规格</td>
                                        <td>Blackwell架构，6144个CUDA核心，RTX 5070级性能</td>
                                    </tr>
                                    <tr class="border-b border-gray-200">
                                        <td class="py-2 font-medium">AI算力</td>
                                        <td>180-200 TOPS</td>
                                    </tr>
                                    <tr class="border-b border-gray-200">
                                        <td class="py-2 font-medium">内存规格</td>
                                        <td>最高128GB LPDDR5X统一内存，带宽301GB/s</td>
                                    </tr>
                                    <tr class="border-b border-gray-200">
                                        <td class="py-2 font-medium">功耗范围</td>
                                        <td>动态TDP 65W-120W，配套245W氮化镓电源</td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                    </div>
                    <div>
                        <div class="bg-dark/5 rounded-2xl p-6 h-full">
                            <h4 class="font-bold text-dark mb-4">N1X与H100定位对比</h4>
                            <canvas id="compareChart" height="250"></canvas>
                            <p class="text-xs text-gray-500 mt-4 text-center">数据来源：英伟达官方技术文档</p>
                        </div>
                    </div>
                </div>

                <div class="grid md:grid-cols-3 gap-6">
                    <div class="bg-gradient-to-br from-primary/10 to-secondary/10 rounded-2xl p-6">
                        <div class="text-4xl mb-3">💻</div>
                        <h4 class="font-bold text-dark mb-2">图形性能</h4>
                        <p class="text-primary text-2xl font-bold mb-2">RTX 5070级</p>
                        <p class="text-sm text-gray-600">受限于1048MHz频率及LPDDR5X带宽，实际约为桌面版60-80%，3DMark跑分约22000分</p>
                    </div>
                    <div class="bg-gradient-to-br from-primary/10 to-secondary/10 rounded-2xl p-6">
                        <div class="text-4xl mb-3">⚡</div>
                        <h4 class="font-bold text-dark mb-2">能效优势</h4>
                        <p class="text-primary text-2xl font-bold mb-2">+80%</p>
                        <p class="text-sm text-gray-600">65W功耗下即可实现接近RTX 4070移动版（140W）的性能，每瓦性能提升约80%</p>
                    </div>
                    <div class="bg-gradient-to-br from-primary/10 to-secondary/10 rounded-2xl p-6">
                        <div class="text-4xl mb-3">🎮</div>
                        <h4 class="font-bold text-dark mb-2">游戏表现</h4>
                        <p class="text-primary text-2xl font-bold mb-2">160 FPS</p>
                        <p class="text-sm text-gray-600">《赛博朋克2077》2K光追场景帧率可达160帧，《黑神话：悟空》1080P高画质稳定100-120帧</p>
                    </div>
                </div>'''

# 替换第一章节
old_section1_start = '                <h3 class="text-2xl font-bold text-primary mb-6 border-l-4 border-primary pl-4">1.1 陶瓷粉体 — MLCC性能的核心基石</h3>'
old_section1_end = '                </div>\n            </div>\n        </div>\n    </section>'

# 找到section1的起始和结束位置，替换内容
section1_start_idx = template.find(old_section1_start)
section1_end_idx = template.find(old_section1_end, section1_start_idx + 1000)

# 保留section的外层结构
section1_prefix = template[:section1_start_idx]
section1_suffix = template[section1_end_idx:]

# 构建新的section1内容
new_section1_full = section1_content + '\n' + old_section1_end

# 替换第二章节标题
template = template.replace('                    上游产业链分析（最详细）', '                    N1X芯片规格详解与性能对比')

# 替换第二章节标题
template = template.replace('                    中游产业链分析（最核心）', '                    黄仁勋COMPUTEX 2026演讲前瞻')

# 写入文件
with open('docs/industry_chain/20260530_英伟达N1X芯片与COMPUTEX深度研究报告.html', 'w', encoding='utf-8') as f:
    f.write(template)

print("✅ 第一阶段转换完成：头部、摘要、目录、第一章节标题已替换")
print("📄 文件已保存：docs/industry_chain/20260530_英伟达N1X芯片与COMPUTEX深度研究报告.html")
