#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
智能选题助手 - 2026年6月10日盘前更新
"""

import re
from datetime import datetime

def update_topic_picker():
    html_path = "docs/智能选题助手/index.html"
    
    # 读取文件
    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 备份原文件
    backup_path = html_path + ".bak." + datetime.now().strftime("%Y%m%d_%H%M%S")
    with open(backup_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"✅ 已备份原文件到 {backup_path}")
    
    # ========== 1. 更新数据时间 ==========
    content = content.replace(
        '数据更新时间：2026年6月9日 21:30',
        '数据更新时间：2026年6月10日 07:55'
    )
    print("✅ 更新时间戳")
    
    # ========== 2. 更新存储芯片超级周期 ==========
    # 更新副标题描述
    content = content.replace(
        'HBM3E需求爆发+厂商连续提价+AI服务器加速渗透',
        'HBM4竞争格局确立+AI服务器硅需求暴增3.8倍+存储涨价周期延续'
    )
    print("✅ 更新存储芯片副标题")
    
    # 更新近期催化
    old_catalyst = '隔夜美光科技涨超9%带动芯片股反弹，存储超级周期逻辑不变。但短期受全球风险偏好下降压制，板块波动加剧，建议逢低分批布局，不追高。'
    new_catalyst = 'HBM4三家供应商（SK海力士/三星/美光）全部通过英伟达认证，行业进入第二增长曲线；AI服务器硅消耗量是传统服务器的3.8倍，硅片需求爆发式增长。但昨夜美股芯片股再度大跌（美光-9.5%、AMD-10%），短期情绪承压，建议控制仓位逢低布局。'
    content = content.replace(old_catalyst, new_catalyst)
    print("✅ 更新存储芯片近期催化")
    
    # ========== 3. 更新人形机器人催化 ==========
    old_robot_catalyst = '机器人板块逆势爆发，成为弱势市场中最强主线。华为云发布行业AI梦工厂具身智能专区，英伟达与宇树科技合作推进人形机器人量产。产业趋势明确，资金认可度高。'
    new_robot_catalyst = '机器人产业趋势持续强化，英伟达Isaac GR00T生态加速落地。昨日科技股普涨背景下机器人板块同步反弹，长期成长逻辑清晰。但短期受美股科技股下跌影响，板块波动加大，建议以长期视角分批布局。'
    content = content.replace(old_robot_catalyst, new_robot_catalyst)
    print("✅ 更新人形机器人催化")
    
    # ========== 4. 更新配置策略建议 ==========
    # 进攻配置
    old_attack = '人形机器人（15%）+ AI应用端（10%），机器人板块逆势走强，成为弱势中最强主线；AI应用端位置相对较低，具备防御属性'
    new_attack = '存储芯片/HBM（15%）+ 人形机器人（15%），存储超级周期第二曲线（HBM4）逻辑强化，机器人产业趋势明确，科技成长主线地位稳固'
    content = content.replace(old_attack, new_attack)
    print("✅ 更新进攻配置")
    
    # 趋势配置
    old_trend = '存储芯片/HBM（15%）+ 煤炭/高股息（10%），存储超级周期逻辑不变但短期承压，煤炭高股息防御属性突出，进可攻退可守'
    new_trend = '光通信/CPO（10%）+ 消费电子/苹果链（10%），华为今日发布新一代光通信架构，苹果WWDC大会催化消费电子，两大事件驱动短线机会'
    content = content.replace(old_trend, new_trend)
    print("✅ 更新趋势配置")
    
    # 防御配置
    old_defense = '煤炭/高股息（25%）+ 电力/算电协同（20%），市场避险情绪浓厚，高股息板块成为资金避风港；电力迎峰度夏确定性强，建议超配'
    new_defense = '煤炭/高股息（15%）+ 电力/算电协同（10%），昨夜美股大跌提升避险需求，高股息板块具备防御属性；电力迎峰度夏逻辑不变'
    content = content.replace(old_defense, new_defense)
    print("✅ 更新防御配置")
    
    # ========== 5. 更新重要警示 ==========
    old_warning = 'A股跌破4000点，高风险区域严控仓位。上证指数收3959点（-1.7%），创业板指跌3.69%，科创50重挫4.3%，两市超4600只个股下跌。外围方面，美股芯片股昨夜反弹（费城半导体+5.6%），但整体趋势仍弱。操作上建议：①整体仓位控制在3成以下，现金为王；②重点配置煤炭、电力、高股息等防御板块；③机器人、存储等长期赛道逢急跌分批低吸，不追高；④关注量能变化，缩量下跌后等待明确企稳信号再考虑加仓。'
    new_warning = 'A股站上4000点但外围风险加剧，震荡市中严控仓位。上证指数收4010点（+1.28%），科创50大涨4.17%，但昨夜纳指跌超3%，美光科技跌9.5%，AMD跌10%，全球科技股波动加剧。今日关键事件：华为光通信架构发布、苹果WWDC26开幕、5月CPI数据公布。操作上建议：①整体仓位控制在5成左右，进退有度；②科技主线聚焦存储、机器人等有业绩支撑的赛道，规避纯题材炒作；③利用震荡低吸核心标的，冲高不追涨；④密切关注美股走势和CPI数据，防范外围风险传导。'
    content = content.replace(old_warning, new_warning)
    print("✅ 更新重要警示")
    
    # ========== 6. 更新催化事件日历 ==========
    # 更新WWDC状态 - 从"进行中"改为"今日开幕"
    content = content.replace(
        '<div class="text-3xl font-black text-blue-600 mb-1">6/3-7</div>',
        '<div class="text-3xl font-black text-blue-600 mb-1">6/10</div>'
    )
    content = content.replace(
        '<div class="text-sm font-bold text-gray-800 mb-2">WWDC苹果大会</div>',
        '<div class="text-sm font-bold text-gray-800 mb-2">苹果WWDC26</div>'
    )
    content = content.replace(
        '<div class="text-xs text-gray-500 mb-2">iOS 18 AI功能发布</div>',
        '<div class="text-xs text-gray-500 mb-2">Vision Pro/AI/新系统</div>'
    )
    content = content.replace(
        '<span class="bg-orange-100 text-orange-700 text-xs px-2 py-0.5 rounded-full font-semibold">进行中</span>',
        '<span class="bg-green-100 text-green-700 text-xs px-2 py-0.5 rounded-full font-semibold">今日开幕</span>'
    )
    print("✅ 更新WWDC催化事件")
    
    # 新增华为光通信事件 - 替换COMPUTEX（已过期）
    content = content.replace(
        '<div class="text-3xl font-black text-gray-600 mb-1">6/2 ✓</div>',
        '<div class="text-3xl font-black text-purple-600 mb-1">6/10</div>'
    )
    content = content.replace(
        '<div class="text-sm font-bold text-gray-800 mb-2">COMPUTEX闭幕</div>',
        '<div class="text-sm font-bold text-gray-800 mb-2">华为光通信</div>'
    )
    content = content.replace(
        '<div class="text-xs text-gray-500 mb-2">英伟达发布全系列新品</div>',
        '<div class="text-xs text-gray-500 mb-2">新一代光模块/CPO架构</div>'
    )
    content = content.replace(
        '<span class="bg-gray-200 text-gray-700 text-xs px-2 py-0.5 rounded-full font-semibold">已发生</span>',
        '<span class="bg-purple-100 text-purple-700 text-xs px-2 py-0.5 rounded-full font-semibold">今日发布</span>'
    )
    print("✅ 新增华为光通信催化事件")
    
    # 保存更新后的文件
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("\n" + "="*60)
    print("✅ 智能选题助手更新完成")
    print("="*60)
    print("更新要点：")
    print("1. 时间戳：6月9日21:30 → 6月10日07:55")
    print("2. 存储芯片：HBM4竞争格局+硅需求暴增3.8倍")
    print("3. 配置策略：科技成长为主，事件驱动为辅")
    print("4. 风险警示：美股科技股大跌，外围风险加剧")
    print("5. 催化日历：华为光通信今日发布、苹果WWDC26今日开幕")
    print("="*60)
    
    return True

if __name__ == "__main__":
    update_topic_picker()
