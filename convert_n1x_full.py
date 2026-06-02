#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
完整替换N1X报告内容
"""

# 读取当前HTML
with open('docs/industry_chain/20260530_英伟达N1X芯片与COMPUTEX深度研究报告.html', 'r', encoding='utf-8') as f:
    html = f.read()

# ========== 完整替换section1的内容（从1.1陶瓷粉体到section1结束） ==========
section1_old_start = '                <h3 class="text-2xl font-bold text-primary mb-6 border-l-4 border-primary pl-4">1.1 陶瓷粉体 — MLCC性能的核心基石</h3>'
section1_old_end = '                </div>\n            </div>\n        </div>\n    </section>\n\n    <!-- 第二部分：中游产业链 -->'

section1_new_content = '''                <h3 class="text-2xl font-bold text-primary mb-6 border-l-4 border-primary pl-4">1.1 核心规格参数 — 20核CPU+RTX 5070级GPU的超级SoC</h3>
                
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

                <div class="grid md:grid-cols-3 gap-6 mb-12">
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
                </div>

                <!-- 1.2 与H100/H200定位对比 -->
                <div>
                    <h3 class="text-2xl font-bold text-primary mb-6 border-l-4 border-primary pl-4">1.2 定位对比 — N1X vs H100/H200 差异分析</h3>
                    
                    <div class="overflow-x-auto mb-8">
                        <table class="w-full text-sm table-shadow rounded-xl overflow-hidden">
                            <thead class="bg-gradient-to-r from-primary to-secondary text-white">
                                <tr>
                                    <th class="px-6 py-4 text-left">对比维度</th>
                                    <th class="px-6 py-4 text-left">N1X（消费级PC）</th>
                                    <th class="px-6 py-4 text-left">H100/H200（数据中心）</th>
                                </tr>
                            </thead>
                            <tbody class="bg-white divide-y divide-gray-200">
                                <tr class="hover:bg-light/50 transition-colors">
                                    <td class="px-6 py-4 font-medium">目标市场</td>
                                    <td class="px-6 py-4">PC笔记本、桌面、边缘AI</td>
                                    <td class="px-6 py-4">数据中心、AI训练/推理</td>
                                </tr>
                                <tr class="hover:bg-light/50 transition-colors">
                                    <td class="px-6 py-4 font-medium">架构基础</td>
                                    <td class="px-6 py-4">Grace Blackwell消费级</td>
                                    <td class="px-6 py-4">Blackwell数据中心级</td>
                                </tr>
                                <tr class="hover:bg-light/50 transition-colors">
                                    <td class="px-6 py-4 font-medium">显存类型</td>
                                    <td class="px-6 py-4">LPDDR5X统一内存</td>
                                    <td class="px-6 py-4">HBM3e高带宽内存</td>
                                </tr>
                                <tr class="hover:bg-light/50 transition-colors">
                                    <td class="px-6 py-4 font-medium">显存带宽</td>
                                    <td class="px-6 py-4">301GB/s</td>
                                    <td class="px-6 py-4">H200达4.8TB/s</td>
                                </tr>
                                <tr class="hover:bg-light/50 transition-colors">
                                    <td class="px-6 py-4 font-medium">功耗范围</td>
                                    <td class="px-6 py-4">65-120W</td>
                                    <td class="px-6 py-4">700-1000W</td>
                                </tr>
                                <tr class="hover:bg-light/50 transition-colors">
                                    <td class="px-6 py-4 font-medium">AI算力重点</td>
                                    <td class="px-6 py-4">端侧本地AI推理</td>
                                    <td class="px-6 py-4">云端大规模训练/推理</td>
                                </tr>
                                <tr class="hover:bg-light/50 transition-colors">
                                    <td class="px-6 py-4 font-medium">CUDA核心</td>
                                    <td class="px-6 py-4">6144个</td>
                                    <td class="px-6 py-4">H100约14592个</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>

                    <div class="bg-light rounded-2xl p-6">
                        <h4 class="font-bold text-dark mb-4">💡 核心差异总结</h4>
                        <p class="text-gray-700 leading-relaxed">
                            N1X是面向消费级PC市场的Arm架构SoC，强调CPU+GPU+AI的一体化设计，开启"AI PC新时代"；
                            H100/H200是面向数据中心的专业级GPU，主打大规模AI训练和高吞吐量推理。
                            两者定位完全不同，N1X代表英伟达从云端向端侧的战略延伸，标志着AI算力的全面下沉。
                        </p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- 第二部分：演讲前瞻 -->'''

# 执行替换
start_idx = html.find(section1_old_start)
end_idx = html.find(section1_old_end, start_idx) + len(section1_old_end)

if start_idx != -1 and end_idx != -1:
    html = html[:start_idx] + section1_new_content + html[end_idx:]
    print("✅ section1内容替换完成")
else:
    print("❌ 未找到section1的起始/结束标记")

# ========== 替换section2的内容 ==========
section2_old_start = '                <h3 class="text-2xl font-bold text-secondary mb-6 border-l-4 border-secondary pl-4">2.1 全球竞争格局 — 五梯队分层明显</h3>'
section2_old_end = '    <!-- 第三部分：下游需求爆发 -->'

section2_new_content = '''                <h3 class="text-2xl font-bold text-secondary mb-6 border-l-4 border-secondary pl-4">2.1 五大重磅发布前瞻</h3>
                
                <div class="grid md:grid-cols-2 gap-6 mb-8">
                    <div class="bg-gradient-to-br from-red-50 to-pink-50 rounded-2xl p-6 border-l-4 border-red-500">
                        <h4 class="text-xl font-bold text-red-600 mb-4">🔥 N1X/N1 Arm PC处理器（确定性最高）</h4>
                        <p class="text-gray-700 mb-4">英伟达与微软已联合预热"A new era of PC"，明确指向N1X系列：</p>
                        <ul class="text-sm text-gray-600 space-y-2">
                            <li>• <strong>标准版N1</strong>：面向轻薄本市场，2026年Q2跟进</li>
                            <li>• <strong>高配版N1X</strong>：面向高性能游戏本和工作站，2026年Q4限量上市</li>
                            <li>• <strong>首发OEM伙伴</strong>：联想Legion拯救者、戴尔Alienware、华硕ROG</li>
                        </ul>
                    </div>
                    <div class="bg-gradient-to-br from-purple-50 to-indigo-50 rounded-2xl p-6 border-l-4 border-purple-500">
                        <h4 class="text-xl font-bold text-purple-600 mb-4">⚡ Vera Rubin新一代AI算力架构</h4>
                        <p class="text-gray-700 mb-4">以暗物质研究先驱天文学家薇拉·鲁宾命名的超级芯片平台：</p>
                        <ul class="text-sm text-gray-600 space-y-2">
                            <li>• <strong>Rubin GPU</strong>：台积电第三代3nm+CoWoS-L，首次支持HBM4</li>
                            <li>• <strong>Vera CPU</strong>：Arm架构独立数据中心CPU，市场机遇高达200亿美元</li>
                            <li>• <strong>性能突破</strong>：推理吞吐量比Blackwell高出35倍，每Token成本降至1/10</li>
                        </ul>
                    </div>
                </div>

                <div class="grid md:grid-cols-3 gap-6 mb-8">
                    <div class="bg-white border border-gray-200 rounded-2xl p-5 shadow-sm">
                        <div class="text-3xl mb-3">🖥️</div>
                        <h4 class="font-bold text-dark mb-2">NVL72超级计算机</h4>
                        <p class="text-sm text-gray-600 mb-3">COMPUTEX金奖+可持续技术特别奖，36个Vera CPU+72个Rubin GPU，无线缆模块化设计</p>
                        <p class="text-xs text-primary font-medium">组装时间从2小时缩短到5分钟</p>
                    </div>
                    <div class="bg-white border border-gray-200 rounded-2xl p-5 shadow-sm">
                        <div class="text-3xl mb-3">🤖</div>
                        <h4 class="font-bold text-dark mb-2">边缘AI与机器人</h4>
                        <p class="text-sm text-gray-600 mb-3">Jetson Thor平台，2070 FP4 TFLOPS性能，比Jetson Orin提升7.5倍</p>
                        <p class="text-xs text-primary font-medium">Alpamayo汽车开发平台同步发布</p>
                    </div>
                    <div class="bg-white border border-gray-200 rounded-2xl p-5 shadow-sm">
                        <div class="text-3xl mb-3">🏭</div>
                        <h4 class="font-bold text-dark mb-2">AI工厂解决方案</h4>
                        <p class="text-sm text-gray-600 mb-3">完整展示NVL+Vera CPU+BlueField组合，Spectrum-X1600网络升级</p>
                        <p class="text-xs text-primary font-medium">3.2T光模块时代正式开启</p>
                    </div>
                </div>

                <!-- 2.2 演讲时间与地点 -->
                <div class="mb-12">
                    <h3 class="text-2xl font-bold text-secondary mb-6 border-l-4 border-secondary pl-4">2.2 演讲详情信息</h3>
                    
                    <div class="bg-gradient-to-r from-primary/5 to-secondary/5 rounded-2xl p-8">
                        <div class="grid md:grid-cols-3 gap-8 text-center">
                            <div>
                                <div class="text-5xl mb-4">📅</div>
                                <h4 class="font-bold text-dark text-xl mb-2">演讲时间</h4>
                                <p class="text-2xl font-bold text-primary">2026年6月1日</p>
                                <p class="text-gray-500">上午11:00（北京时间）</p>
                            </div>
                            <div>
                                <div class="text-5xl mb-4">📍</div>
                                <h4 class="font-bold text-dark text-xl mb-2">演讲地点</h4>
                                <p class="text-2xl font-bold text-secondary">台北音乐中心</p>
                                <p class="text-gray-500">Taipei Music Center</p>
                            </div>
                            <div>
                                <div class="text-5xl mb-4">🎤</div>
                                <h4 class="font-bold text-dark text-xl mb-2">演讲者</h4>
                                <p class="text-2xl font-bold text-accent">黄仁勋</p>
                                <p class="text-gray-500">Jensen Huang，英伟达CEO</p>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- 2.3 市场影响 -->
                <div>
                    <h3 class="text-2xl font-bold text-secondary mb-6 border-l-4 border-secondary pl-4">2.3 演讲市场影响预判</h3>
                    
                    <div class="grid md:grid-cols-2 gap-6">
                        <div class="bg-gradient-to-br from-green-50 to-emerald-50 rounded-2xl p-6">
                            <h4 class="font-bold text-green-700 mb-4">✅ 确定性机会</h4>
                            <ul class="text-sm text-gray-700 space-y-2">
                                <li>• AI算力板块整体催化，PCB、光模块、液冷受益最直接</li>
                                <li>• 英伟达供应链标的二季度业绩验证，订单能见度高</li>
                                <li>• HBM产业链价值重估，内存占比从5%飙升至30%</li>
                                <li>• 3.2T光模块时代开启，高速互联需求爆发</li>
                            </ul>
                        </div>
                        <div class="bg-gradient-to-br from-yellow-50 to-amber-50 rounded-2xl p-6">
                            <h4 class="font-bold text-amber-700 mb-4">⚠️ 需要验证</h4>
                            <ul class="text-sm text-gray-700 space-y-2">
                                <li>• N1X对Arm PC生态的实际带动效应</li>
                                <li>• Vera Rubin的量产时间与客户订单情况</li>
                                <li>• Arm架构CPU对x86格局的冲击程度</li>
                                <li>• 3nm产能分配是否满足多产品线并行</li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- 第三部分：产业链全景 -->'''

# 执行section2替换
start_idx2 = html.find(section2_old_start)
end_idx2 = html.find(section2_old_end, start_idx2) + len(section2_old_end)

if start_idx2 != -1 and end_idx2 != -1:
    html = html[:start_idx2] + section2_new_content + html[end_idx2:]
    print("✅ section2内容替换完成")
else:
    print("❌ 未找到section2的起始/结束标记")

# 更新section3标题
html = html.replace('                    下游需求爆发', '                    上下游产业链全景分析')

# 写入文件
with open('docs/industry_chain/20260530_英伟达N1X芯片与COMPUTEX深度研究报告.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("✅ N1X报告HTML转换完成（前3章节）")
print("📄 文件路径：docs/industry_chain/20260530_英伟达N1X芯片与COMPUTEX深度研究报告.html")
