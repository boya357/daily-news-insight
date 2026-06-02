#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
完成N1X报告的第4-6章节
"""

# 读取当前HTML
with open('docs/industry_chain/20260530_英伟达N1X芯片与COMPUTEX深度研究报告.html', 'r', encoding='utf-8') as f:
    html = f.read()

# ========== 替换section3到结束 ==========
section3_old_start = '                <!-- 3.1 AI服务器 -->'
section3_old_end = '</body>\n</html>'

section3_to_end_content = '''                <!-- 3.1 上游核心环节 -->
                <div class="mb-12">
                    <h3 class="text-2xl font-bold text-accent mb-6 border-l-4 border-accent pl-4">3.1 上游核心环节 — 晶圆制造与先进封装</h3>
                    
                    <div class="grid lg:grid-cols-2 gap-8 mb-8">
                        <div>
                            <p class="text-gray-700 mb-6 leading-relaxed">
                                英伟达产业链上游是本轮价值重构的最大受益者。HBM内存价值量暴涨435%，PCB载板暴涨233%，
                                上游零部件在AI机架成本中的占比大幅提升，A股在这些领域已实现技术突破并深度绑定英伟达。
                            </p>
                            <div class="bg-light rounded-xl p-6">
                                <h4 class="font-bold text-dark mb-4">上游核心环节价值变化</h4>
                                <table class="w-full text-sm">
                                    <thead>
                                        <tr class="border-b border-gray-300">
                                            <th class="text-left py-2 text-gray-600">环节</th>
                                            <th class="text-left py-2 text-gray-600">价值涨幅</th>
                                            <th class="text-left py-2 text-gray-600">核心标的</th>
                                        </tr>
                                    </thead>
                                    <tbody class="text-gray-700">
                                        <tr class="border-b border-gray-200">
                                            <td class="py-2 font-medium">HBM存储及材料</td>
                                            <td class="py-2 text-red-600 font-bold">435%</td>
                                            <td class="py-2">雅克科技、澜起科技</td>
                                        </tr>
                                        <tr class="border-b border-gray-200">
                                            <td class="py-2 font-medium">PCB/ABF载板</td>
                                            <td class="py-2 text-red-600 font-bold">233%</td>
                                            <td class="py-2">胜宏科技、沪电股份、深南电路</td>
                                        </tr>
                                        <tr class="border-b border-gray-200">
                                            <td class="py-2 font-medium">液冷散热</td>
                                            <td class="py-2 text-orange-600 font-bold">150%</td>
                                            <td class="py-2">英维克、飞荣达</td>
                                        </tr>
                                        <tr class="border-b border-gray-200">
                                            <td class="py-2 font-medium">1.6T/3.2T光模块</td>
                                            <td class="py-2 text-orange-600 font-bold">100%</td>
                                            <td class="py-2">中际旭创、新易盛、天孚通信</td>
                                        </tr>
                                        <tr class="border-b border-gray-200">
                                            <td class="py-2 font-medium">高功率电源</td>
                                            <td class="py-2 text-orange-600 font-bold">120%</td>
                                            <td class="py-2">麦格米特</td>
                                        </tr>
                                    </tbody>
                                </table>
                            </div>
                        </div>
                        <div>
                            <div class="bg-dark/5 rounded-2xl p-6 h-full">
                                <h4 class="font-bold text-dark mb-4">产业链价值重构对比</h4>
                                <canvas id="valueChart" height="250"></canvas>
                                <p class="text-xs text-gray-500 mt-4 text-center">数据来源：英伟达供应链深度调研</p>
                            </div>
                        </div>
                    </div>

                    <div class="grid md:grid-cols-3 gap-6">
                        <div class="bg-gradient-to-br from-blue-50 to-cyan-50 rounded-2xl p-6">
                            <div class="text-4xl mb-3">🔬</div>
                            <h4 class="font-bold text-dark mb-2">晶圆制造</h4>
                            <p class="text-blue-600 text-xl font-bold mb-2">台积电N3B</p>
                            <p class="text-sm text-gray-600">N1X与GB10（DGX Spark）、联发科C1X共享3nm产能，CoWoS先进封装2027年达每月20万片晶圆</p>
                        </div>
                        <div class="bg-gradient-to-br from-blue-50 to-cyan-50 rounded-2xl p-6">
                            <div class="text-4xl mb-3">💾</div>
                            <h4 class="font-bold text-dark mb-2">HBM高带宽存储</h4>
                            <p class="text-blue-600 text-xl font-bold mb-2">HBM4量产</p>
                            <p class="text-sm text-gray-600">美光、三星、SK海力士三大供应商，VR200机架中内存成本占比从5%飙升至30%</p>
                        </div>
                        <div class="bg-gradient-to-br from-blue-50 to-cyan-50 rounded-2xl p-6">
                            <div class="text-4xl mb-3">🏭</div>
                            <h4 class="font-bold text-dark mb-2">PCB材料</h4>
                            <p class="text-blue-600 text-xl font-bold mb-2">高端板材</p>
                            <p class="text-sm text-gray-600">生益科技（M9级大陆唯一认证）、隆扬电子（HVLP5全球唯二）、菲利华（Q布全球唯二）</p>
                        </div>
                    </div>
                </div>

                <!-- 3.2 中游核心组件 -->
                <div>
                    <h3 class="text-2xl font-bold text-accent mb-6 border-l-4 border-accent pl-4">3.2 中游核心组件 — PCB与整机代工</h3>
                    
                    <div class="grid md:grid-cols-2 gap-6 mb-8">
                        <div class="bg-white border border-gray-200 rounded-2xl p-6 shadow-sm">
                            <h4 class="font-bold text-dark mb-4">🏆 GPU PCB全球第一 — 胜宏科技</h4>
                            <ul class="text-sm text-gray-700 space-y-2">
                                <li>• GB300五阶HDI板独家供应商</li>
                                <li>• Rubin架构PCB份额50%+</li>
                                <li>• PCB业务2026年预计增长80%+</li>
                                <li>• 深度绑定英伟达所有产品线</li>
                            </ul>
                        </div>
                        <div class="bg-white border border-gray-200 rounded-2xl p-6 shadow-sm">
                            <h4 class="font-bold text-dark mb-4">🏆 AI服务器代工龙头 — 工业富联</h4>
                            <ul class="text-sm text-gray-700 space-y-2">
                                <li>• 英伟达全球最大代工厂，份额70%+</li>
                                <li>• 全球唯一可大规模量产Blackwell服务器</li>
                                <li>• 2026年营收增长35-40%，净利润增长45-55%</li>
                                <li>• Rubin架构服务器订单饱满</li>
                            </ul>
                        </div>
                    </div>

                    <div class="grid md:grid-cols-3 gap-6">
                        <div class="bg-gradient-to-br from-green-50 to-emerald-50 rounded-2xl p-6">
                            <div class="text-3xl mb-3">❄️</div>
                            <h4 class="font-bold text-dark mb-2">英维克 — 液冷龙头</h4>
                            <p class="text-green-600 text-lg font-bold mb-2">Rubin平台核心供应商</p>
                            <p class="text-sm text-gray-600">浸没式方案市占40%，2026年液冷业务预计增长80%+</p>
                        </div>
                        <div class="bg-gradient-to-br from-green-50 to-emerald-50 rounded-2xl p-6">
                            <div class="text-3xl mb-3">🔌</div>
                            <h4 class="font-bold text-dark mb-2">麦格米特 — 电源专家</h4>
                            <p class="text-green-600 text-lg font-bold mb-2">英伟达指定供应商</p>
                            <p class="text-sm text-gray-600">12kW高功率电源独家供应，2026年AI电源收入突破100亿元</p>
                        </div>
                        <div class="bg-gradient-to-br from-green-50 to-emerald-50 rounded-2xl p-6">
                            <div class="text-3xl mb-3">🌐</div>
                            <h4 class="font-bold text-dark mb-2">中际旭创 — 光模块</h4>
                            <p class="text-green-600 text-lg font-bold mb-2">全球龙头地位稳固</p>
                            <p class="text-sm text-gray-600">英伟达800G/1.6T主力供应商，3.2T产品领先布局，订单排至2026年底</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- 第四部分：A股标的弹性 -->
    <section id="section4" class="py-12 px-4">
        <div class="max-w-7xl mx-auto">
            <div class="bg-white/95 rounded-3xl p-8 shadow-2xl">
                <h2 class="text-4xl font-bold text-dark mb-8 flex items-center">
                    <span class="bg-red-500 text-white w-12 h-12 rounded-full flex items-center justify-center mr-4 text-2xl">四</span>
                    A股相关标的弹性测算
                </h2>

                <!-- 4.1 核心受益标的 -->
                <div class="mb-12">
                    <h3 class="text-2xl font-bold text-red-600 mb-6 border-l-4 border-red-500 pl-4">4.1 核心受益标的清单与业绩弹性</h3>
                    
                    <div class="overflow-x-auto mb-8">
                        <table class="w-full text-sm table-shadow rounded-xl overflow-hidden">
                            <thead class="bg-gradient-to-r from-red-500 to-orange-500 text-white">
                                <tr>
                                    <th class="px-6 py-4 text-left">代码</th>
                                    <th class="px-6 py-4 text-left">公司名称</th>
                                    <th class="px-6 py-4 text-left">英伟达供应链地位</th>
                                    <th class="px-6 py-4 text-left">2026年业绩弹性</th>
                                    <th class="px-6 py-4 text-left">弹性星级</th>
                                </tr>
                            </thead>
                            <tbody class="bg-white divide-y divide-gray-200">
                                <tr class="hover:bg-light/50 transition-colors">
                                    <td class="px-6 py-4 font-medium">300476</td>
                                    <td class="px-6 py-4 font-bold">胜宏科技</td>
                                    <td class="px-6 py-4">GPU PCB全球第一，GB300五阶HDI板独家</td>
                                    <td class="px-6 py-4">PCB业务+80~100%，净利润+70~90%</td>
                                    <td class="px-6 py-4">⭐⭐⭐⭐⭐</td>
                                </tr>
                                <tr class="hover:bg-light/50 transition-colors">
                                    <td class="px-6 py-4 font-medium">601138</td>
                                    <td class="px-6 py-4 font-bold">工业富联</td>
                                    <td class="px-6 py-4">全球最大AI服务器代工厂，份额70%+</td>
                                    <td class="px-6 py-4">营收+35~40%，净利润+45~55%</td>
                                    <td class="px-6 py-4">⭐⭐⭐⭐☆</td>
                                </tr>
                                <tr class="hover:bg-light/50 transition-colors">
                                    <td class="px-6 py-4 font-medium">002463</td>
                                    <td class="px-6 py-4 font-bold">沪电股份</td>
                                    <td class="px-6 py-4">Rubin机架PCB核心供应商</td>
                                    <td class="px-6 py-4">AI服务器PCB营收+150%，整体+50~60%</td>
                                    <td class="px-6 py-4">⭐⭐⭐⭐⭐</td>
                                </tr>
                                <tr class="hover:bg-light/50 transition-colors">
                                    <td class="px-6 py-4 font-medium">300308</td>
                                    <td class="px-6 py-4 font-bold">中际旭创</td>
                                    <td class="px-6 py-4">全球光模块龙头，800G/1.6T主力</td>
                                    <td class="px-6 py-4">1.6T营收+200%+，净利润+50~65%</td>
                                    <td class="px-6 py-4">⭐⭐⭐⭐☆</td>
                                </tr>
                                <tr class="hover:bg-light/50 transition-colors">
                                    <td class="px-6 py-4 font-medium">002837</td>
                                    <td class="px-6 py-4 font-bold">英维克</td>
                                    <td class="px-6 py-4">Rubin平台液冷方案核心供应商</td>
                                    <td class="px-6 py-4">液冷业务+80~100%，净利润+50~70%</td>
                                    <td class="px-6 py-4">⭐⭐⭐⭐☆</td>
                                </tr>
                                <tr class="hover:bg-light/50 transition-colors">
                                    <td class="px-6 py-4 font-medium">002409</td>
                                    <td class="px-6 py-4 font-bold">雅克科技</td>
                                    <td class="px-6 py-4">国内唯一批量供应HBM前驱体</td>
                                    <td class="px-6 py-4">HBM相关+90~110%，净利润+40~50%</td>
                                    <td class="px-6 py-4">⭐⭐⭐⭐⭐</td>
                                </tr>
                                <tr class="hover:bg-light/50 transition-colors">
                                    <td class="px-6 py-4 font-medium">002851</td>
                                    <td class="px-6 py-4 font-bold">麦格米特</td>
                                    <td class="px-6 py-4">英伟达指定电源供应商</td>
                                    <td class="px-6 py-4">AI电源收入突破100亿，净利润+60~80%</td>
                                    <td class="px-6 py-4">⭐⭐⭐⭐☆</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>

                <!-- 4.2 价值重构分析 -->
                <div>
                    <h3 class="text-2xl font-bold text-red-600 mb-6 border-l-4 border-red-500 pl-4">4.2 产业链价值重构核心逻辑</h3>
                    
                    <div class="grid lg:grid-cols-2 gap-8">
                        <div class="bg-gradient-to-br from-red-50 to-orange-50 rounded-2xl p-6">
                            <h4 class="font-bold text-red-700 mb-4">旧格局（Blackwell时代）</h4>
                            <div class="space-y-3">
                                <div class="flex items-center justify-between">
                                    <span class="text-gray-700">GPU</span>
                                    <span class="text-red-600 font-bold text-xl">65%+</span>
                                </div>
                                <div class="flex items-center justify-between">
                                    <span class="text-gray-700">内存</span>
                                    <span class="text-gray-500 font-bold">5-10%</span>
                                </div>
                                <div class="flex items-center justify-between">
                                    <span class="text-gray-700">PCB/载板</span>
                                    <span class="text-gray-500 font-bold">~5%</span>
                                </div>
                                <div class="flex items-center justify-between">
                                    <span class="text-gray-700">其他零部件</span>
                                    <span class="text-gray-500 font-bold">~15%</span>
                                </div>
                            </div>
                            <p class="text-sm text-gray-500 mt-4">GPU一家独大，A股多处于低附加值环节</p>
                        </div>
                        <div class="bg-gradient-to-br from-green-50 to-emerald-50 rounded-2xl p-6">
                            <h4 class="font-bold text-green-700 mb-4">新格局（Rubin时代）</h4>
                            <div class="space-y-3">
                                <div class="flex items-center justify-between">
                                    <span class="text-gray-700">GPU</span>
                                    <span class="text-green-600 font-bold text-xl">~51%</span>
                                </div>
                                <div class="flex items-center justify-between">
                                    <span class="text-gray-700">内存</span>
                                    <span class="text-green-600 font-bold text-xl">25-30% 📈</span>
                                </div>
                                <div class="flex items-center justify-between">
                                    <span class="text-gray-700">PCB/载板</span>
                                    <span class="text-green-600 font-bold text-xl">~12% 📈</span>
                                </div>
                                <div class="flex items-center justify-between">
                                    <span class="text-gray-700">其他零部件</span>
                                    <span class="text-green-600 font-bold">~7%</span>
                                </div>
                            </div>
                            <p class="text-sm text-gray-500 mt-4">上游零部件价值暴增，A股国产替代迎黄金期</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- 第五部分：市场影响分析 -->
    <section id="section5" class="py-12 px-4">
        <div class="max-w-7xl mx-auto">
            <div class="bg-white/95 rounded-3xl p-8 shadow-2xl">
                <h2 class="text-4xl font-bold text-dark mb-8 flex items-center">
                    <span class="bg-amber-500 text-white w-12 h-12 rounded-full flex items-center justify-center mr-4 text-2xl">五</span>
                    AI算力板块市场影响分析
                </h2>

                <!-- 5.1 短期催化 -->
                <div class="mb-12">
                    <h3 class="text-2xl font-bold text-amber-600 mb-6 border-l-4 border-amber-500 pl-4">5.1 短期催化（1-3个月）</h3>
                    
                    <div class="grid md:grid-cols-2 gap-6">
                        <div class="bg-gradient-to-br from-amber-50 to-yellow-50 rounded-2xl p-6">
                            <h4 class="font-bold text-amber-700 mb-4">📅 COMPUTEX发布会催化（6月1-5日）</h4>
                            <ul class="text-sm text-gray-700 space-y-2">
                                <li>• 黄仁勋演讲将成为AI算力板块核心催化剂</li>
                                <li>• 重点关注：PCB（胜宏、沪电）、液冷（英维克）、光模块（中际）</li>
                                <li>• 历史规律：英伟达重大发布会前后1-2周相关标的平均涨幅15-25%</li>
                            </ul>
                        </div>
                        <div class="bg-gradient-to-br from-amber-50 to-yellow-50 rounded-2xl p-6">
                            <h4 class="font-bold text-amber-700 mb-4">📊 供应链业绩验证（7-8月中报）</h4>
                            <ul class="text-sm text-gray-700 space-y-2">
                                <li>• 二季度英伟达供应链订单开始反映Rubin新品备货</li>
                                <li>• 中报业绩高增长标的有望迎来估值修复</li>
                                <li>• 重点验证：Rubin订单落地情况、毛利率变化趋势</li>
                            </ul>
                        </div>
                    </div>
                </div>

                <!-- 5.2 中期趋势 -->
                <div class="mb-8">
                    <h3 class="text-2xl font-bold text-amber-600 mb-6 border-l-4 border-amber-500 pl-4">5.2 中期趋势（3-12个月）</h3>
                    
                    <div class="bg-light rounded-2xl p-6">
                        <h4 class="font-bold text-dark mb-4">🔮 三大核心投资逻辑</h4>
                        <div class="grid md:grid-cols-3 gap-6">
                            <div>
                                <h5 class="font-bold text-primary mb-2">价值重构逻辑</h5>
                                <p class="text-sm text-gray-600">HBM、PCB等上游环节价值量暴增，相关标的业绩弹性远超市场预期</p>
                            </div>
                            <div>
                                <h5 class="font-bold text-secondary mb-2">国产替代逻辑</h5>
                                <p class="text-sm text-gray-600">地缘政治推动供应链自主，A股在多个核心环节已实现技术突破并通过认证</p>
                            </div>
                            <div>
                                <h5 class="font-bold text-accent mb-2">业绩兑现逻辑</h5>
                                <p class="text-sm text-gray-600">英伟达供应链订单能见度高，Rubin架构量产将带来明确的业绩增量</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- 第六部分：风险与结论 -->
    <section id="section6" class="py-12 px-4">
        <div class="max-w-7xl mx-auto">
            <div class="bg-white/95 rounded-3xl p-8 shadow-2xl">
                <h2 class="text-4xl font-bold text-dark mb-8 flex items-center">
                    <span class="bg-gray-600 text-white w-12 h-12 rounded-full flex items-center justify-center mr-4 text-2xl">六</span>
                    风险提示与核心结论
                </h2>

                <!-- 6.1 风险提示 -->
                <div class="mb-12">
                    <h3 class="text-2xl font-bold text-gray-600 mb-6 border-l-4 border-gray-500 pl-4">6.1 风险提示</h3>
                    
                    <div class="grid md:grid-cols-2 lg:grid-cols-4 gap-6">
                        <div class="bg-red-50 rounded-2xl p-6 border border-red-200">
                            <div class="text-3xl mb-3">⚠️</div>
                            <h4 class="font-bold text-red-700 mb-2">产能风险</h4>
                            <p class="text-sm text-gray-600">3nm产能紧张可能影响N1X和Rubin量产进度，CoWoS封装产能是核心瓶颈</p>
                        </div>
                        <div class="bg-red-50 rounded-2xl p-6 border border-red-200">
                            <div class="text-3xl mb-3">📉</div>
                            <h4 class="font-bold text-red-700 mb-2">估值风险</h4>
                            <p class="text-sm text-gray-600">部分AI算力标的估值已处于历史高位，需警惕业绩不及预期带来的回调风险</p>
                        </div>
                        <div class="bg-red-50 rounded-2xl p-6 border border-red-200">
                            <div class="text-3xl mb-3">🌐</div>
                            <h4 class="font-bold text-red-700 mb-2">地缘政治</h4>
                            <p class="text-sm text-gray-600">中美科技博弈可能影响供应链稳定性，出口管制政策存在不确定性</p>
                        </div>
                        <div class="bg-red-50 rounded-2xl p-6 border border-red-200">
                            <div class="text-3xl mb-3">💻</div>
                            <h4 class="font-bold text-red-700 mb-2">需求不及预期</h4>
                            <p class="text-sm text-gray-600">Arm PC市场接受度、主权AI采购力度可能低于市场乐观预期</p>
                        </div>
                    </div>
                </div>

                <!-- 6.2 核心结论 -->
                <div>
                    <h3 class="text-2xl font-bold text-gray-600 mb-6 border-l-4 border-gray-500 pl-4">6.2 核心结论</h3>
                    
                    <div class="bg-gradient-to-r from-primary/10 to-secondary/10 rounded-2xl p-8">
                        <div class="text-center mb-8">
                            <div class="text-5xl mb-4">🎯</div>
                            <h4 class="text-2xl font-bold text-dark mb-4">投资评级：强烈推荐</h4>
                        </div>
                        <div class="max-w-4xl mx-auto text-gray-700 leading-relaxed space-y-4">
                            <p>
                                <strong>黄仁勋COMPUTEX 2026演讲将成为AI算力板块的重大催化剂。</strong>
                                N1X Arm PC处理器开启消费级AI新时代，Vera Rubin架构实现35倍推理吞吐量提升，
                                标志着英伟达从云端向端侧的战略延伸全面启动。
                            </p>
                            <p>
                                <strong>产业链价值重构是本轮最大的投资机会。</strong>
                                GPU成本占比从65%下降至51%的同时，HBM内存价值暴涨435%、PCB载板暴涨233%，
                                上游零部件环节迎来历史性发展机遇。A股在这些领域已实现深度绑定，国产替代进入黄金期。
                            </p>
                            <p>
                                <strong>重点关注两条投资主线：</strong>
                                ① 价值量暴增环节：HBM材料（雅克科技）、PCB载板（胜宏科技、沪电股份）；
                                ② 英伟达核心供应链：AI服务器代工（工业富联）、液冷（英维克）、光模块（中际旭创）、电源（麦格米特）。
                            </p>
                            <p class="text-center font-bold text-primary text-lg mt-6">
                                6月1日黄仁勋台北演讲在即，AI算力板块的新一轮行情正在孕育！🚀
                            </p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- 页脚 -->
    <footer class="py-8 px-4">
        <div class="max-w-7xl mx-auto text-center text-white/70">
            <p class="mb-2">📅 发布时间：2026年5月30日</p>
            <p class="text-sm">⚠️ 免责声明：本报告仅供参考，不构成任何投资建议。投资有风险，入市需谨慎。</p>
            <p class="text-sm mt-2">🔗 数据来源：英伟达官方文档、供应链深度调研、各公司公告、公开信息整理</p>
        </div>
    </footer>

</body>
</html>'''

# 执行替换
start_idx3 = html.find(section3_old_start)
end_idx3 = html.find(section3_old_end, start_idx3) + len(section3_old_end)

if start_idx3 != -1 and end_idx3 != -1:
    html = html[:start_idx3] + section3_to_end_content + html[end_idx3:]
    print("✅ section3到结尾内容替换完成")
else:
    print("❌ 未找到section3的起始/结束标记")
    print(f"start_idx3: {start_idx3}")

# 写入文件
with open('docs/industry_chain/20260530_英伟达N1X芯片与COMPUTEX深度研究报告.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("✅ N1X报告HTML转换全部完成！")
print("📄 文件路径：docs/industry_chain/20260530_英伟达N1X芯片与COMPUTEX深度研究报告.html")
print(f"📊 文件大小：{len(html)} 字节")
