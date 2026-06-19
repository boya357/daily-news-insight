#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
存储芯片报告 - boya投资体系沉浸式融入
1. 给每个章节添加boya视角批注
2. 升级第10章为投资策略总纲
"""

from bs4 import BeautifulSoup, Tag

FILE_PATH = "/app/data/所有对话/主对话/docs/industry_chain/20260619_存储芯片产业链深度研究报告.html"
GIT_PATH = "/root/daily-news-insight/docs/industry_chain/20260619_存储芯片产业链深度研究报告.html"

# 每个章节的boya视角批注
BOYA_INSIGHTS = {
    'section2': {
        'icon': '📈',
        'title': 'boya视角 · 行业定位',
        'content': '存储芯片是AI算力底座的核心，行业增速30%+，属于<strong>高景气主线赛道</strong>，符合「只做核心主线」的投资原则。全球市场规模快速扩张，行业β足够大，能容纳大资金，是必配级别的赛道。'
    },
    'section3': {
        'icon': '⛓️',
        'title': 'boya视角 · 产业链价值',
        'content': '产业链上游设备材料<strong>价值量最高</strong>，设备（光刻/刻蚀/CVD）和高端材料（光刻胶/特种气体）是卡脖子环节，国产替代空间最大、利润率最高。中游制造环节<strong>关注有核心技术壁垒的公司</strong>，避免纯加工类公司。'
    },
    'section4': {
        'icon': '🔄',
        'title': 'boya视角 · 周期与成长',
        'content': '存储是典型的<strong>周期+成长</strong>双属性行业。HBM是成长曲线，DRAM/NAND是周期反转。选股优先级：<strong>HBM > 利基型 > 通用型</strong>。当前处于周期上行期，AI催化加速，景气度最高的细分方向弹性最大。'
    },
    'section5': {
        'icon': '🐉',
        'title': 'boya视角 · 竞争格局',
        'content': '全球存储是<strong>三寡头垄断</strong>（三星/海力士/美光），国内厂商目前还在追赶期。A股有全球竞争力的公司少，<strong>投资国内龙头才有长期价值</strong>，二三线公司只能做波段。龙空龙策略下只选各细分方向的龙一。'
    },
    'section6': {
        'icon': '🇨🇳',
        'title': 'boya视角 · 国产替代',
        'content': '国产替代是<strong>长期确定性逻辑</strong>，地缘政治越紧张，替代速度越快。关注两个方向：1) 已经有突破、能进入主流供应链的；2) 卡脖子最严重、政策扶持力度最大的。<strong>有实质进展的比纯概念的更值得重仓</strong>。'
    },
    'section7': {
        'icon': '⚡',
        'title': 'boya视角 · 技术趋势',
        'content': 'HBM是当前最强技术趋势，<strong>技术迭代快的公司弹性大</strong>，但也要注意技术路线风险。投资上优先选<strong>技术领先+产能落地</strong>双重验证的标的，避免纯PPT公司。技术迭代期是选股的关键窗口期。'
    },
    'section8': {
        'icon': '⚠️',
        'title': 'boya视角 · 风险评估',
        'content': '三大核心风险：<strong>AI需求不及预期、地缘政治黑天鹅、产能过剩周期下行</strong>。应对策略：1) 分散持仓不all-in；2) 设好止损纪律，跌破10%无条件止损；3) 跟踪行业景气度变化，及时止盈。'
    },
    'section9': {
        'icon': '🎯',
        'title': 'boya视角 · 标的选择',
        'content': '选股优先级：<strong>HBM相关 > 存储设计 > 设备材料 > 封测</strong>。重点关注有核心技术壁垒+业绩兑现能力强的龙头。<strong>雅克科技</strong>是HBM材料核心标的，已持仓继续持有；<strong>佰维存储</strong>是HBM模组弹性标的，等待低吸机会。'
    }
}

# 第10章升级 - 投资策略总纲（替换原有内容
SECTION10_NEW_CONTENT = '''
                        <div class="glass-card p-6 mb-6" style="background: linear-gradient(135deg, rgba(139, 92, 246, 0.15), rgba(59, 130, 246, 0.15)); border-left: 4px solid #8b5cf6;">
                            <p class="text-white font-bold text-xl mb-2">🎯 主线定级：<span style="color: #fbbf24;">S级 · 核心主线</span></p>
                            <p class="text-gray-300">存储芯片 + AI双主线叠加，周期上行 + 国产替代共振，是当前市场确定性最高的赛道之一。</p>
                        </div>
                        
                        <!-- 核心投资逻辑汇总 -->
                        <div class="mb-6">
                            <h3 class="text-white font-bold text-lg mb-4">📋 核心投资逻辑</h3>
                            <div class="space-y-3">
                                <div class="flex items-start gap-3 p-3 rounded-lg" style="background: rgba(255,255,255,0.03);">
                                    <span style="color: #22c55e;">●</span>
                                    <div>
                                        <p class="text-white font-medium">AI算力大爆发</p>
                                        <p class="text-gray-400 text-sm">大模型训练推理需要海量HBM显存，需求呈指数级增长</p>
                                    </div>
                                </div>
                                <div class="flex items-start gap-3 p-3 rounded-lg" style="background: rgba(255,255,255,0.03);">
                                    <span style="color: #3b82f6;">●</span>
                                    <div>
                                        <p class="text-white font-medium">周期上行拐点</p>
                                        <p class="text-gray-400 text-sm">存储价格触底回升，行业进入新一轮上行周期</p>
                                    </div>
                                </div>
                                <div class="flex items-start gap-3 p-3 rounded-lg" style="background: rgba(255,255,255,0.03);">
                                    <span style="color: #f59e0b;">●</span>
                                    <div>
                                        <p class="text-white font-medium">国产替代加速</p>
                                        <p class="text-gray-400 text-sm">地缘政治驱动下，国内厂商迎来历史性发展机遇</p>
                                    </div>
                                </div>
                                <div class="flex items-start gap-3 p-3 rounded-lg" style="background: rgba(255,255,255,0.03);">
                                    <span style="color: #8b5cf6;">●</span>
                                    <div>
                                        <p class="text-white font-medium">业绩逐步兑现</p>
                                        <p class="text-gray-400 text-sm">从炒预期走向兑现阶段，有真实业绩的公司走得更远</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                        
                        <!-- 龙头梯队 -->
                        <div class="mb-6">
                            <h3 class="text-white font-bold text-lg mb-4">🐉 龙头梯队与优先级</h3>
                            <div class="space-y-2">
                                <div class="flex items-center justify-between p-3 rounded-lg" style="background: rgba(251, 191, 36, 0.1); border: 1px solid rgba(251, 191, 36, 0.3);">
                                    <div class="flex items-center gap-3">
                                        <span class="text-yellow-400 font-bold">龙一</span>
                                        <span class="text-white font-medium">雅克科技</span>
                                        <span class="text-xs text-purple-300 px-2 py-0.5 rounded-full" style="background: rgba(139, 92, 246, 0.2);">已持仓</span>
                                    </div>
                                    <span class="text-yellow-400 text-sm">HBM材料核心</span>
                                </div>
                                <div class="flex items-center justify-between p-3 rounded-lg" style="background: rgba(148, 163, 184, 0.1); border: 1px solid rgba(148, 163, 184, 0.2);">
                                    <div class="flex items-center gap-3">
                                        <span class="text-gray-400 font-bold">龙二</span>
                                        <span class="text-white font-medium">佰维存储</span>
                                        <span class="text-xs text-blue-300 px-2 py-0.5 rounded-full" style="background: rgba(59, 130, 246, 0.2);">关注</span>
                                    </div>
                                    <span class="text-gray-400 text-sm">HBM模组弹性</span>
                                </div>
                                <div class="flex items-center justify-between p-3 rounded-lg" style="background: rgba(205, 127, 50, 0.1); border: 1px solid rgba(205, 127, 50, 0.2);">
                                    <div class="flex items-center gap-3">
                                        <span class="text-orange-400 font-bold">龙三</span>
                                        <span class="text-white font-medium">江波龙</span>
                                        <span class="text-xs text-gray-400 px-2 py-0.5 rounded-full" style="background: rgba(156, 163, 175, 0.2);">观察</span>
                                    </div>
                                    <span class="text-orange-400 text-sm">企业级存储</span>
                                </div>
                            </div>
                        </div>
                        
                        <!-- 操作策略 -->
                        <div class="grid grid-cols-1 md:grid-cols-3 gap-4 mb-6">
                            <div class="glass-card p-4 text-center" style="background: rgba(34, 197, 94, 0.1); border: 1px solid rgba(34, 197, 94, 0.3);">
                                <p class="text-green-400 font-bold text-2xl mb-1">持有</p>
                                <p class="text-gray-400 text-xs">已有持仓继续持有<br/>不轻易下车</p>
                            </div>
                            <div class="glass-card p-4 text-center" style="background: rgba(251, 191, 36, 0.1); border: 1px solid rgba(251, 191, 36, 0.3);">
                                <p class="text-yellow-400 font-bold text-2xl mb-1">低吸</p>
                                <p class="text-gray-400 text-xs">回调至10/20日线<br/>分批建仓</p>
                            </div>
                            <div class="glass-card p-4 text-center" style="background: rgba(239, 68, 68, 0.1); border: 1px solid rgba(239, 68, 68, 0.3);">
                                <p class="text-red-400 font-bold text-2xl mb-1">止损</p>
                                <p class="text-gray-400 text-xs">10%铁律止损<br/>保护本金安全</p>
                            </div>
                        </div>
                        
                        <!-- 仓位建议 -->
                        <div class="glass-card p-5 mb-6">
                            <h3 class="text-white font-bold text-lg mb-3">💼 仓位配置建议</h3>
                            <div class="space-y-2 text-sm">
                                <div class="flex justify-between">
                                    <span class="text-gray-400">赛道总仓位上限</span>
                                    <span class="text-white font-medium">不超过总仓位30%</span>
                                </div>
                                <div class="flex justify-between">
                                    <span class="text-gray-400">单票最高仓位</span>
                                    <span class="text-white font-medium">不超过总仓位15%</span>
                                </div>
                                <div class="flex justify-between">
                                    <span class="text-gray-400">龙头配置比例</span>
                                    <span class="text-white font-medium">龙一60% / 龙二30% / 龙三10%</span>
                                </div>
                                <div class="w-full h-2 bg-gray-700 rounded-full mt-3">
                                    <div class="h-full rounded-full" style="width: 60%; background: linear-gradient(to right, #22c55e, #eab308);"></div>
                                </div>
                                <p class="text-gray-500 text-xs text-center">当前配置进度：已持有雅克科技，等待加仓机会</p>
                            </div>
                        </div>
                        
                        <!-- 预判记录 -->
                        <div class="glass-card p-5">
                            <h3 class="text-white font-bold text-lg mb-3">🔮 预判与验证</h3>
                            <div class="space-y-2 text-sm">
                                <div class="p-3 rounded-lg" style="background: rgba(139, 92, 246, 0.1);">
                                    <div class="flex justify-between items-center mb-1">
                                        <span class="text-white font-medium">预判#1：存储板块中期上涨空间50%+</span>
                                        <span class="text-purple-400 text-xs">置信度75%</span>
                                    </div>
                                    <p class="text-gray-400 text-xs">验证时间：2026年12月 · 基于行业增速+国产替代空间测算</p>
                                </div>
                                <div class="p-3 rounded-lg" style="background: rgba(59, 130, 246, 0.1);">
                                    <div class="flex justify-between items-center mb-1">
                                        <span class="text-white font-medium">预判#2：HBM龙头年内有望翻倍</span>
                                        <span class="text-blue-400 text-xs">置信度65%</span>
                                    </div>
                                    <p class="text-gray-400 text-xs">验证时间：2026年12月 · HBM需求爆发超预期的话可能更快</p>
                                </div>
                                <div class="p-3 rounded-lg" style="background: rgba(251, 191, 36, 0.1);">
                                    <div class="flex justify-between items-center mb-1">
                                        <span class="text-white font-medium">预判#3：短期有回调风险，低吸为主</span>
                                        <span class="text-yellow-400 text-xs">置信度70%</span>
                                    </div>
                                    <p class="text-gray-400 text-xs">验证时间：2026年7月上旬 · 累计涨幅较大，获利盘有兑现需求</p>
                                </div>
                            </div>
                        </div>
'''

def upgrade_report():
    with open(FILE_PATH, 'r', encoding='utf-8') as f:
        content = f.read()
    
    soup = BeautifulSoup(content, 'html.parser')
    
    # ========== 第一部分：给第2-9章添加boya视角 ==========
    for section_id, insight in BOYA_INSIGHTS.items():
        title_elem = soup.find('h2', id=section_id)
        if not title_elem:
            continue
        
        # 找到父级卡片
        card = title_elem.parent
        while card and 'glass-card' not in card.get('class', []):
            card = card.parent
        
        if not card:
            continue
        
        # 找到章节内的最后一个 section-divider
        dividers = card.find_all(class_='section-divider')
        if dividers:
            insert_before = dividers[-1]
        else:
            insert_before = None
        
        # 创建boya视角卡片
        boya_card = soup.new_tag('div')
        boya_card['class'] = ['glass-card', 'p-4', 'mt-6', 'mb-2']
        boya_card['style'] = 'background: linear-gradient(135deg, rgba(139, 92, 246, 0.15), rgba(59, 130, 246, 0.15)); border-left: 4px solid #8b5cf6; border-radius: 8px;'
        
        # 标题行
        header = soup.new_tag('div')
        header['class'] = ['flex', 'items-center', 'gap-2', 'mb-2']
        
        icon_span = soup.new_tag('span')
        icon_span.string = insight['icon']
        icon_span['style'] = 'font-size: 1.2rem;'
        
        title_span = soup.new_tag('span')
        title_span.string = insight['title']
        title_span['style'] = 'color: #c4b5fd; font-weight: 600; font-size: 0.95rem;'
        
        header.append(icon_span)
        header.append(title_span)
        boya_card.append(header)
        
        # 内容 - 用BeautifulSoup解析HTML内容
        content_soup = BeautifulSoup(f'<p style="color: #d1d5db; font-size: 0.9rem; line-height: 1.7; margin: 0;">{insight["content"]}</p>', 'html.parser')
        boya_card.append(content_soup.p)
        
        # 插入
        if insert_before:
            insert_before.insert_before(boya_card)
        else:
            card.append(boya_card)
    
    # ========== 第二部分：升级第10章 ==========
    section10_title = soup.find('h2', id='section10')
    if section10_title:
        # 找到卡片
        card10 = section10_title.parent
        while card10 and 'glass-card' not in card10.get('class', []):
            card10 = card10.parent
        
        if card10:
            # 清空卡片内容（保留标题）
            # 找到标题之后的所有内容，替换掉
            # 先保留标题
            title_html = str(section10_title)
            # 解析新内容
            new_content_soup = BeautifulSoup(SECTION10_NEW_CONTENT, 'html.parser')
            
            # 清空卡片中标题之后的内容
            found_title = False
            to_remove = []
            for child in card10.children:
                if found_title:
                    to_remove.append(child)
                if child == section10_title:
                    found_title = True
            
            for elem in to_remove:
                elem.decompose()
            
            # 添加新内容
            for child in new_content_soup.contents:
                card10.append(child)
    
    # 保存
    result = str(soup)
    
    with open(FILE_PATH, 'w', encoding='utf-8') as f:
        f.write(result)
    
    with open(GIT_PATH, 'w', encoding='utf-8') as f:
        f.write(result)
    
    print("✅ boya投资体系沉浸式融入完成")
    print(f"   - {len(BOYA_INSIGHTS)} 个章节视角批注")
    print(f"   - 第10章升级为投资策略总纲")

if __name__ == "__main__":
    upgrade_report()
