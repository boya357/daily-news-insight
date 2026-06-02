#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

def add_charts_to_n1x_report():
    input_file = 'docs/industry_chain/20260530_英伟达N1X芯片与COMPUTEX深度研究报告.html'
    
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. 添加Chart.js脚本引入（在<head>的最后一个script之后）
    chartjs_script = '<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.8/dist/chart.umd.min.js"></script>'
    if chartjs_script not in content:
        # 在</head>之前插入
        content = content.replace('</head>', f'    {chartjs_script}\n</head>')
        print('✅ 已添加Chart.js脚本')
    
    # 2. 在"1.2 性能表现与能效优势"部分添加性能对比图表
    performance_chart_html = '''
                    <!-- 性能对比图表 -->
                    <div class="my-10">
                        <h4 class="text-xl font-bold text-gray-800 mb-6">📊 GPU性能对比（Time Spy跑分）</h4>
                        <div class="bg-white rounded-2xl p-6 shadow-lg">
                            <canvas id="performanceChart" height="300"></canvas>
                            <p class="text-xs text-gray-500 mt-4 text-center">数据来源：英伟达官方数据、3DMark预估跑分</p>
                        </div>
                    </div>
'''
    
    # 找到"1.2 性能表现与能效优势"部分的位置
    if '性能表现与能效优势' in content and 'performanceChart' not in content:
        # 在该部分的表格后面插入图表
        insert_pos = content.find('每瓦性能提升约80%')
        if insert_pos > 0:
            insert_pos += len('每瓦性能提升约80%**')
            content = content[:insert_pos] + performance_chart_html + content[insert_pos:]
            print('✅ 已添加性能对比图表')
    
    # 3. 在"3.1 上游核心环节"部分添加产业链价值分布图表
    value_chart_html = '''
                    <!-- 产业链价值分布图表 -->
                    <div class="my-10">
                        <h4 class="text-xl font-bold text-gray-800 mb-6">📊 产业链价值分布（VR200机架）</h4>
                        <div class="grid lg:grid-cols-2 gap-8">
                            <div class="bg-white rounded-2xl p-6 shadow-lg">
                                <canvas id="valueChart" height="280"></canvas>
                                <p class="text-xs text-gray-500 mt-4 text-center">数据来源：英伟达供应链成本拆分</p>
                            </div>
                            <div class="bg-white rounded-2xl p-6 shadow-lg">
                                <canvas id="growthChart" height="280"></canvas>
                                <p class="text-xs text-gray-500 mt-4 text-center">VR200 vs GB200 各环节价值量增长</p>
                            </div>
                        </div>
                    </div>
'''
    
    if '上游核心环节' in content and 'valueChart' not in content:
        insert_pos = content.find('单机价值量从传统几千元攀升至万元级别')
        if insert_pos > 0:
            insert_pos += len('单机价值量从传统几千元攀升至万元级别')
            content = content[:insert_pos] + value_chart_html + content[insert_pos:]
            print('✅ 已添加产业链价值分布图表')
    
    # 4. 在文件末尾添加图表初始化JavaScript
    chart_init_js = '''
<script>
document.addEventListener('DOMContentLoaded', function() {
    // 性能对比柱状图
    if (document.getElementById('performanceChart')) {
        new Chart(document.getElementById('performanceChart'), {
            type: 'bar',
            data: {
                labels: ['N1X (65W)', 'RTX 5070移动版', 'RTX 4070移动版', 'RTX 5070桌面版'],
                datasets: [{
                    label: 'Time Spy跑分',
                    data: [22000, 17550, 14500, 28000],
                    backgroundColor: [
                        'rgba(139, 92, 246, 0.8)',
                        'rgba(59, 130, 246, 0.8)',
                        'rgba(16, 185, 129, 0.8)',
                        'rgba(245, 158, 11, 0.8)'
                    ],
                    borderColor: [
                        'rgba(139, 92, 246, 1)',
                        'rgba(59, 130, 246, 1)',
                        'rgba(16, 185, 129, 1)',
                        'rgba(245, 158, 11, 1)'
                    ],
                    borderWidth: 2,
                    borderRadius: 8
                }]
            },
            options: {
                responsive: true,
                plugins: {
                    legend: { display: false },
                    title: { display: false }
                },
                scales: {
                    y: {
                        beginAtZero: true,
                        grid: { color: 'rgba(0,0,0,0.05)' }
                    },
                    x: {
                        grid: { display: false }
                    }
                }
            }
        });
    }

    // 产业链价值分布饼图
    if (document.getElementById('valueChart')) {
        new Chart(document.getElementById('valueChart'), {
            type: 'doughnut',
            data: {
                labels: ['HBM存储', 'PCB/载板', 'GPU芯片', '液冷散热', '电源', '光模块', '其他'],
                datasets: [{
                    data: [30, 20, 18, 12, 8, 7, 5],
                    backgroundColor: [
                        '#ef4444', '#3b82f6', '#8b5cf6', '#10b981', 
                        '#f59e0b', '#06b6d4', '#9ca3af'
                    ]
                }]
            },
            options: {
                responsive: true,
                plugins: {
                    legend: { 
                        position: 'bottom', 
                        labels: { padding: 15, font: { size: 11 } } 
                    }
                }
            }
        });
    }

    // 价值量增长对比图
    if (document.getElementById('growthChart')) {
        new Chart(document.getElementById('growthChart'), {
            type: 'bar',
            data: {
                labels: ['HBM存储', 'PCB/载板', '液冷散热', '光模块', '电源'],
                datasets: [{
                    label: 'VR200 vs GB200 价值量增长%',
                    data: [435, 233, 180, 150, 120],
                    backgroundColor: 'rgba(139, 92, 246, 0.8)',
                    borderColor: 'rgba(139, 92, 246, 1)',
                    borderWidth: 2,
                    borderRadius: 8
                }]
            },
            options: {
                responsive: true,
                indexAxis: 'y',
                plugins: {
                    legend: { display: false }
                },
                scales: {
                    x: {
                        beginAtZero: true,
                        grid: { color: 'rgba(0,0,0,0.05)' },
                        ticks: { callback: function(value) { return value + '%'; } }
                    },
                    y: {
                        grid: { display: false }
                    }
                }
            }
        });
    }
});
</script>
'''
    
    # 在</body>之前插入JS代码
    if '</body>' in content and 'performanceChart' in content:
        content = content.replace('</body>', chart_init_js + '\n</body>')
        print('✅ 已添加图表初始化JS')
    
    # 保存文件
    with open(input_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print('\n🎉 所有图表已成功添加到N1X报告！')

if __name__ == '__main__':
    add_charts_to_n1x_report()
