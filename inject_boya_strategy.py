#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
存储芯片报告 - boya投资体系专属研判模块植入
将用户的龙空龙策略、止损纪律、主线思维编码为标准化分析框架
"""

import re

FILE_PATH = "/app/data/所有对话/主对话/docs/industry_chain/20260619_存储芯片产业链深度研究报告.html"

# ============================================================
# boya投资体系分析框架 - 存储芯片产业链专项研判
# ============================================================
BOYA_STRATEGY_SECTION = '''
                        <h2 id="section10">十、boya 独家策略研判</h2>
                        <div class="section-divider"></div>
                        
                        <div class="glass-card p-6 mb-6" style="background: linear-gradient(135deg, rgba(139, 92, 246, 0.15), rgba(59, 130, 246, 0.15)); border-left: 4px solid #8b5cf6;">
                            <p class="text-white font-bold text-lg mb-2">🎯 主线评级：<span style="color: #fbbf24;">S级 · 核心主线</span></p>
                            <p class="text-gray-300">存储芯片属于「AI算力 + 科技自主可控」双主线叠加，是当前市场确定性最高的赛道之一。符合boya投资体系中「只做核心主线」的原则。</p>
                        </div>
                        
                        <!-- 六大维度分析网格 -->
                        <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mb-6">
                            
                            <!-- 维度1：主线评级 -->
                            <div class="glass-card p-5">
                                <div class="flex items-center gap-2 mb-3">
                                    <span style="font-size: 1.5rem;">🏆</span>
                                    <h3 class="text-white font-bold text-lg">一、主线评级</h3>
                                </div>
                                <div class="space-y-2 text-sm">
                                    <div class="flex justify-between">
                                        <span class="text-gray-400">主线级别</span>
                                        <span class="text-yellow-400 font-bold">S级（核心主线）</span>
                                    </div>
                                    <div class="flex justify-between">
                                        <span class="text-gray-400">催化密度</span>
                                        <span class="text-green-400">★★★★★ 高频</span>
                                    </div>
                                    <div class="flex justify-between">
                                        <span class="text-gray-400">资金关注度</span>
                                        <span class="text-green-400">★★★★★ 极高</span>
                                    </div>
                                    <div class="flex justify-between">
                                        <span class="text-gray-400">业绩兑现度</span>
                                        <span class="text-green-400">★★★★☆ 高</span>
                                    </div>
                                    <div class="flex justify-between">
                                        <span class="text-gray-400">政策友好度</span>
                                        <span class="text-green-400">★★★★★ 极高</span>
                                    </div>
                                </div>
                                <div class="mt-3 pt-3 border-t border-gray-700">
                                    <p class="text-gray-300 text-xs"><strong>研判逻辑：</strong>HBM需求爆发+国产替代加速+周期上行共振，三大逻辑同时验证，属于「多重确认」的顶级主线。</p>
                                </div>
                            </div>
                            
                            <!-- 维度2：龙头梯队 -->
                            <div class="glass-card p-5">
                                <div class="flex items-center gap-2 mb-3">
                                    <span style="font-size: 1.5rem;">🐉</span>
                                    <h3 class="text-white font-bold text-lg">二、龙头梯队识别</h3>
                                </div>
                                <div class="space-y-2 text-sm">
                                    <div class="flex items-center gap-2 p-2 rounded" style="background: rgba(251, 191, 36, 0.1);">
                                        <span class="text-yellow-400 font-bold w-8">龙一</span>
                                        <span class="text-white font-medium">佰维存储</span>
                                        <span class="text-yellow-400 text-xs ml-auto">HBM+AI存储</span>
                                    </div>
                                    <div class="flex items-center gap-2 p-2 rounded" style="background: rgba(148, 163, 184, 0.1);">
                                        <span class="text-gray-400 font-bold w-8">龙二</span>
                                        <span class="text-white font-medium">江波龙</span>
                                        <span class="text-gray-400 text-xs ml-auto">企业级存储</span>
                                    </div>
                                    <div class="flex items-center gap-2 p-2 rounded" style="background: rgba(205, 127, 50, 0.1);">
                                        <span class="text-orange-400 font-bold w-8">龙三</span>
                                        <span class="text-white font-medium">德明利</span>
                                        <span class="text-orange-400 text-xs ml-auto">存储主控</span>
                                    </div>
                                    <div class="flex items-center gap-2 p-2 rounded" style="background: rgba(139, 92, 246, 0.1);">
                                        <span class="text-purple-400 font-bold w-8">趋势</span>
                                        <span class="text-white font-medium">雅克科技</span>
                                        <span class="text-purple-400 text-xs ml-auto">HBM材料+持仓</span>
                                    </div>
                                </div>
                                <div class="mt-3 pt-3 border-t border-gray-700">
                                    <p class="text-gray-300 text-xs"><strong>龙空龙适配：</strong>板块辨识度高，龙头明确，符合「做龙头不做中位股」的策略原则。</p>
                                </div>
                            </div>
                            
                            <!-- 维度3：买点判断 -->
                            <div class="glass-card p-5">
                                <div class="flex items-center gap-2 mb-3">
                                    <span style="font-size: 1.5rem;">💰</span>
                                    <h3 class="text-white font-bold text-lg">三、买点评级</h3>
                                </div>
                                <div class="space-y-3 text-sm">
                                    <div>
                                        <div class="flex justify-between mb-1">
                                            <span class="text-gray-400">整体买点评级</span>
                                            <span class="text-yellow-400 font-bold">★★★★☆ 谨慎追高</span>
                                        </div>
                                        <div class="w-full h-2 bg-gray-700 rounded-full overflow-hidden">
                                            <div class="h-full bg-gradient-to-r from-yellow-500 to-yellow-400" style="width: 70%;"></div>
                                        </div>
                                    </div>
                                    <div class="grid grid-cols-2 gap-2">
                                        <div class="p-2 rounded text-center" style="background: rgba(34, 197, 94, 0.1);">
                                            <p class="text-green-400 text-xs font-medium">低吸区域</p>
                                            <p class="text-white font-bold">10日均线</p>
                                        </div>
                                        <div class="p-2 rounded text-center" style="background: rgba(239, 68, 68, 0.1);">
                                            <p class="text-red-400 text-xs font-medium">追高风险</p>
                                            <p class="text-white font-bold">较高</p>
                                        </div>
                                    </div>
                                </div>
                                <div class="mt-3 pt-3 border-t border-gray-700">
                                    <p class="text-gray-300 text-xs"><strong>操作策略：</strong>板块处于周期上行中期，累计涨幅较大，不建议追高。等待回调至10/20日均线的低吸机会，符合「不追高脉冲股」原则。</p>
                                </div>
                            </div>
                            
                            <!-- 维度4：止损纪律 -->
                            <div class="glass-card p-5">
                                <div class="flex items-center gap-2 mb-3">
                                    <span style="font-size: 1.5rem;">🛡️</span>
                                    <h3 class="text-white font-bold text-lg">四、止损设置</h3>
                                </div>
                                <div class="space-y-2 text-sm">
                                    <div class="p-3 rounded" style="background: rgba(239, 68, 68, 0.1); border: 1px solid rgba(239, 68, 68, 0.3);">
                                        <p class="text-red-400 font-bold text-center text-lg">-10% 铁律止损</p>
                                        <p class="text-gray-400 text-xs text-center mt-1">买入成本下跌10%无条件止损</p>
                                    </div>
                                    <div class="flex justify-between">
                                        <span class="text-gray-400">龙头止损位</span>
                                        <span class="text-white">20日均线</span>
                                    </div>
                                    <div class="flex justify-between">
                                        <span class="text-gray-400">趋势股止损位</span>
                                        <span class="text-white">30日均线</span>
                                    </div>
                                    <div class="flex justify-between">
                                        <span class="text-gray-400">单票仓位上限</span>
                                        <span class="text-yellow-400 font-bold">25%</span>
                                    </div>
                                </div>
                                <div class="mt-3 pt-3 border-t border-gray-700">
                                    <p class="text-gray-300 text-xs"><strong>纪律执行：</strong>严格执行止损，跌破止损位无条件卖出，不抱有侥幸心理。止损是保护本金的最后防线。</p>
                                </div>
                            </div>
                            
                            <!-- 维度5：弹性测算 -->
                            <div class="glass-card p-5">
                                <div class="flex items-center gap-2 mb-3">
                                    <span style="font-size: 1.5rem;">📈</span>
                                    <h3 class="text-white font-bold text-lg">五、弹性与盈亏比</h3>
                                </div>
                                <div class="space-y-2 text-sm">
                                    <div class="flex justify-between">
                                        <span class="text-gray-400">短期上涨空间</span>
                                        <span class="text-green-400">+20% ~ +30%</span>
                                    </div>
                                    <div class="flex justify-between">
                                        <span class="text-gray-400">中期上涨空间</span>
                                        <span class="text-green-400">+50% ~ +80%</span>
                                    </div>
                                    <div class="flex justify-between">
                                        <span class="text-gray-400">短期回调风险</span>
                                        <span class="text-red-400">-15% ~ -20%</span>
                                    </div>
                                    <div class="flex justify-between">
                                        <span class="text-gray-400">盈亏比（中期）</span>
                                        <span class="text-yellow-400 font-bold">3 : 1 以上</span>
                                    </div>
                                    <div class="w-full h-2 bg-gray-700 rounded-full overflow-hidden mt-2">
                                        <div class="h-full" style="width: 75%; background: linear-gradient(to right, #22c55e, #eab308);"></div>
                                    </div>
                                </div>
                                <div class="mt-3 pt-3 border-t border-gray-700">
                                    <p class="text-gray-300 text-xs"><strong>测算依据：</strong>基于行业增速（30%+）+ 国产替代空间 + 周期上行弹性，中期维度盈亏比优异，符合高胜率高赔率原则。</p>
                                </div>
                            </div>
                            
                            <!-- 维度6：持仓与组合影响 -->
                            <div class="glass-card p-5">
                                <div class="flex items-center gap-2 mb-3">
                                    <span style="font-size: 1.5rem;">💼</span>
                                    <h3 class="text-white font-bold text-lg">六、组合操作建议</h3>
                                </div>
                                <div class="space-y-2 text-sm">
                                    <div class="p-2 rounded" style="background: rgba(139, 92, 246, 0.15);">
                                        <p class="text-purple-300 font-medium">当前持仓暴露：<span class="text-white">高（雅克科技+铜冠铜箔）</span></p>
                                    </div>
                                    <div class="space-y-1 text-xs">
                                        <p class="text-gray-300">• <strong class="text-white">雅克科技</strong>：HBM核心材料标的，已持仓浮盈，建议继续持有，设好止盈</p>
                                        <p class="text-gray-300">• <strong class="text-white">铜冠铜箔</strong>：HVLP铜箔+存储封装链条，已持仓浮盈，续创新高</p>
                                        <p class="text-gray-300">• <strong class="text-white">英维克</strong>：液冷+AI算力，与存储有联动性，破位反弹中</p>
                                    </div>
                                    <div class="mt-2 p-2 rounded" style="background: rgba(251, 191, 36, 0.1);">
                                        <p class="text-yellow-300 text-xs font-medium">⚠️ 组合集中度提醒</p>
                                        <p class="text-gray-300 text-xs">科技赛道占比较高，注意分散风险，避免单赛道过度暴露。</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                        
                        <!-- 操作策略总结卡 -->
                        <div class="glass-card p-6 mb-6" style="background: linear-gradient(135deg, rgba(34, 197, 94, 0.1), rgba(59, 130, 246, 0.1)); border: 1px solid rgba(34, 197, 94, 0.3);">
                            <h3 class="text-white font-bold text-lg mb-4">📋 最终操作策略（符合龙空龙体系）</h3>
                            <div class="grid grid-cols-1 md:grid-cols-3 gap-4 text-sm">
                                <div class="text-center">
                                    <p class="text-green-400 font-bold text-2xl mb-1">持有</p>
                                    <p class="text-gray-400 text-xs">已有持仓继续持有<br/>不轻易下车</p>
                                </div>
                                <div class="text-center">
                                    <p class="text-yellow-400 font-bold text-2xl mb-1">低吸</p>
                                    <p class="text-gray-400 text-xs">等待回调机会<br/>不追高脉冲</p>
                                </div>
                                <div class="text-center">
                                    <p class="text-red-400 font-bold text-2xl mb-1">止损</p>
                                    <p class="text-gray-400 text-xs">严格执行10%铁律<br/>保护本金安全</p>
                                </div>
                            </div>
                        </div>
                        
                        <!-- 预判记录 -->
                        <div class="glass-card p-5">
                            <div class="flex items-center gap-2 mb-3">
                                <span style="font-size: 1.25rem;">🔮</span>
                                <h3 class="text-white font-bold">预判记录（将用于T+N验证）</h3>
                            </div>
                            <div class="space-y-2 text-sm">
                                <div class="flex gap-3 p-2 rounded" style="background: rgba(139, 92, 246, 0.1);">
                                    <span class="text-purple-400 font-bold whitespace-nowrap">预判#1</span>
                                    <div>
                                        <p class="text-white">存储板块中期（3-6个月）仍有50%+上涨空间</p>
                                        <p class="text-gray-500 text-xs mt-1">置信度：75% · 验证时间：2026年12月</p>
                                    </div>
                                </div>
                                <div class="flex gap-3 p-2 rounded" style="background: rgba(59, 130, 246, 0.1);">
                                    <span class="text-blue-400 font-bold whitespace-nowrap">预判#2</span>
                                    <div>
                                        <p class="text-white">HBM方向龙头股年内有望翻倍</p>
                                        <p class="text-gray-500 text-xs mt-1">置信度：65% · 验证时间：2026年12月</p>
                                    </div>
                                </div>
                                <div class="flex gap-3 p-2 rounded" style="background: rgba(251, 191, 36, 0.1);">
                                    <span class="text-yellow-400 font-bold whitespace-nowrap">预判#3</span>
                                    <div>
                                        <p class="text-white">短期（1-2周）有回调风险，建议等待低吸机会</p>
                                        <p class="text-gray-500 text-xs mt-1">置信度：70% · 验证时间：2026年7月上旬</p>
                                    </div>
                                </div>
                            </div>
                            <div class="mt-3 pt-3 border-t border-gray-700">
                                <p class="text-gray-500 text-xs">以上预判将记录到预判验证系统，到期自动核验，持续优化模型准确率。</p>
                            </div>
                        </div>
                        
                        <div class="section-divider"></div>
'''

def inject_boya_strategy():
    """注入boya投资体系研判模块"""
    
    with open(FILE_PATH, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. 在TOC中添加第10章链接（在section9之后）
    toc_pattern = r'(<a href="#section9" class="toc-item">九、重点标的分析</a>)'
    toc_replacement = r'''
                        <a href="#section9" class="toc-item">九、重点标的分析</a>
                        <a href="#section10" class="toc-item">十、boya 独家策略研判</a>
    '''
    content = re.sub(toc_pattern, toc_replacement.strip(), content)
    
    # 2. 在报告末尾插入第10章内容
    # 插入点：报告信息之前，section-divider之后
    insert_pattern = r'(<div class="section-divider"></div>\s*\n\s*<!-- 报告信息 -->)'
    insert_replacement = BOYA_STRATEGY_SECTION + r'\n\n                        \1'
    content = re.sub(insert_pattern, insert_replacement, content)
    
    with open(FILE_PATH, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✅ boya独家策略研判模块注入成功")
    print(f"   文件：{FILE_PATH}")
    print(f"   新增：第10章「boya 独家策略研判」")
    print(f"   包含：6大维度 + 操作策略总结 + 预判记录")

if __name__ == "__main__":
    inject_boya_strategy()
