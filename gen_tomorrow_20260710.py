#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
明日催化剂报告生成 - 2026年7月10日（周五）
使用V3.0 TomorrowCatalystGenerator + publish()方法
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'v3'))
os.chdir(os.path.dirname(os.path.abspath(__file__)))

from v3.generators.tomorrow_catalyst import TomorrowCatalystGenerator

# ==========================================
# 初始化生成器
# ==========================================
gen = TomorrowCatalystGenerator(
    date_str="20260710",
    subtitle="2026.07.10 · 明日催化剂 · 周五"
)

# ==========================================
# 1. 明日核心催化（HighlightBox）
# ==========================================
gen.add_key_catalyst("""
<strong>🔥 五大核心催化事件</strong><br>
<br>
1️⃣ <b>科创50暴涨8.41%后延续性验证</b>：7月9日科创50创历史最大单日涨幅，2.91万亿天量成交，明日是行情成色的关键检验日，关注量能能否维持在2.5万亿以上、科创50能否在2100点上方企稳。<br>
<br>
2️⃣ <b>泰诺麦博科创板申购（787806）</b>：7月10日发行价14.46元，募资约10亿元，创新药赛道标的，关注打新情绪对医药板块的带动。<br>
<br>
3️⃣ <b>TCL科技9.86亿股定增限售股解禁</b>：解禁市值约55亿元，占总股本4.74%，解禁主体含深圳国资产业基金，关注面板龙头解禁后的资金承接力度。<br>
<br>
4️⃣ <b>美国6月CPI数据公布</b>：北京时间7月10日晚间公布，是美联储7月议息会议前最重要的通胀数据，通胀走向直接影响全球流动性预期与科技股估值。<br>
<br>
5️⃣ <b>中报预告密集披露期开启</b>：截至7月9日已有171+家公司披露半年报预告，预喜率超87%，存储、化工、炼化赛道业绩炸裂，明日继续有批量公司披露，业绩线进入高潮。
""")

# ==========================================
# 2. 明日事件日历（Tabs分类）
# ==========================================
events = [
    # 政策事件
    {
        'type': 'policy',
        'title': '央行二季度货政例会定调宽松延续',
        'description': '7月8日央行发布二季度货币政策委员会例会纪要，明确继续实施适度宽松的货币政策，加大逆周期和跨周期调节，结构性支持顺序调整为"扩大内需>科技创新>中小微企业"，对A股流动性环境构成长期支撑。',
        'category': '货币政策'
    },
    {
        'type': 'policy',
        'title': '8000亿特别国债项目全部下达',
        'description': '2026年超长期特别国债8000亿元全部下达完毕，覆盖1417个重大项目，重点投向科创设备、水利管网、交通基建、新型储能、三北工程等领域，电网设备、绿电、储能链条持续受益。',
        'category': '财政政策'
    },
    {
        'type': 'policy',
        'title': '"人工智能+人社"五年规划印发',
        'description': '人社部、发改委、工信部、国家数据局联合印发《关于加快推进"人工智能+人社"应用发展的实施意见》，提出2026年打造20个行业大模型应用场景、2030年实现AI普遍应用，AI应用端再获政策催化。',
        'category': '产业政策'
    },
    # 数据发布
    {
        'type': 'data',
        'title': '6月CPI同比涨1.0%、PPI同比涨4.1%',
        'description': '7月9日国家统计局公布6月物价数据：CPI同比+1.0%（前值+1.2%），环比-0.3%；PPI同比+4.1%（前值+3.9%），环比-0.3%。PPI同比创2022年8月以来新高但环比转负，显示通胀整体温和，货币政策仍有宽松空间。',
        'category': '国内经济数据'
    },
    {
        'type': 'data',
        'title': '美国6月CPI数据公布（7/10晚间）',
        'description': '美东时间7月10日上午（北京时间晚间）公布美国6月CPI数据，市场预期核心PCE压力延续，通胀走向直接决定美联储7月议息会议基调，是影响全球风险资产定价的关键数据。',
        'category': '海外经济数据'
    },
    {
        'type': 'data',
        'title': '美国初请失业金人数21.5万',
        'description': '截至7月4日当周初请失业金人数降至21.5万，低于预期21.7万，劳动力市场维持稳定，为美联储政策调整提供缓冲空间。',
        'category': '海外经济数据'
    },
    # 业绩公告
    {
        'type': 'earnings',
        'title': '中报预告密集披露：27家晚盘披露23家预增',
        'description': '7月9日盘后27家公司披露中报预告，23家预增、4家下滑。华昌化工预增1026%、海思科预增513%-575%、宝鼎科技预增469%-560%、风语筑预增431%-696%、天风证券预增429%-694%。存储、化工、券商为高增主力赛道。',
        'category': '中报预告'
    },
    {
        'type': 'earnings',
        'title': '公募基金二季报披露启幕',
        'description': '同泰基金旗下4只基金7月9日率先披露二季报，正式拉开公募二季报披露序幕。同泰数字经济主题季内净值翻倍，科技成长方向成为公募加仓重点，后续关注头部基金公司的调仓动向。',
        'category': '基金季报'
    },
    # 重要会议
    {
        'type': 'meeting',
        'title': '2026世界人工智能大会7/17开幕（倒计时7天）',
        'description': 'WAIC 2026将于7月17-20日在上海世博、张江、西岸三地四馆举办，展览面积首破10万㎡，1100家企业参展，300+款产品全球首发。华为Atlas 950超级算力集群首秀、智算与具身智能两大特色专区各汇聚200+企业，AI产业链催化在即。',
        'category': '行业盛会'
    },
    {
        'type': 'meeting',
        'title': '长鑫科技科创板IPO 7/16申购（倒计时6天）',
        'description': '长鑫科技（688825）7月16日网上申购，发行66.88亿股，预计募资312亿元，将成为A股存储芯片第一股。作为国产DRAM龙头，上市后有望重塑半导体板块估值体系，带动存储产业链整体重估。',
        'category': 'IPO里程碑'
    },
    # 综合事件
    {
        'type': 'general',
        'title': '美光科技宣布2500亿美元美国本土投资计划',
        'description': '美光7月9日宣布加速美国本土晶圆厂投资，预计到2035年在美总投资超2500亿美元，新增30亿美元供应链生态投资。全球存储资本开支持续扩张，设备、材料产业链需求确定性增强。',
        'category': '海外产业'
    },
    {
        'type': 'general',
        'title': 'Meta 9月量产自研AI芯片IRIS',
        'description': 'Meta计划2026年9月启动自研AI芯片"Iris"量产，2027年数据中心总算力翻倍至14吉瓦。全球科技巨头加速AI芯片自研替代，算力产业链竞争格局生变，国产替代逻辑进一步强化。',
        'category': '海外产业'
    },
]

gen.add_events_calendar(events)

# ==========================================
# 3. 业绩公告（StatCard）
# ==========================================
gen.add_earnings_announcements([
    {'name': '华昌化工', 'code': '002274', 'type': '中报预告', 'growth': '+1026%', 'eps': '约0.13元'},
    {'name': '海思科', 'code': '002653', 'type': '中报预告', 'growth': '+513%~575%', 'eps': '7.9~8.7亿'},
    {'name': '宝鼎科技', 'code': '002552', 'type': '中报预告', 'growth': '+469%~560%', 'eps': '1.25~1.45亿'},
    {'name': '风语筑', 'code': '603466', 'type': '中报预告', 'growth': '+431%~696%', 'eps': '—'},
    {'name': '天风证券', 'code': '601162', 'type': '中报预告', 'growth': '+429%~694%', 'eps': '1.64~2.46亿'},
    {'name': '沧州大化', 'code': '600230', 'type': '中报预告', 'growth': '+331%', 'eps': '1.01亿'},
])

# ==========================================
# 4. 重要数据发布（StatCard）
# ==========================================
gen.add_data_release([
    {'name': '中国6月CPI', 'prev': '同比+1.2%', 'expect': '同比+1.1%', 'actual': '同比+1.0%'},
    {'name': '中国6月PPI', 'prev': '同比+3.9%', 'expect': '同比+4.0%', 'actual': '同比+4.1%'},
    {'name': '美国6月CPI', 'prev': '待公布', 'expect': '市场关注', 'actual': '7/10晚公布'},
    {'name': '美国初请失业金', 'prev': '21.7万', 'expect': '21.7万', 'actual': '21.5万'},
    {'name': '央行公开市场', 'prev': '净回笼2785亿', 'expect': '关注逆回购', 'actual': '7天逆回购到期'},
    {'name': '两市成交额', 'prev': '2.56万亿', 'expect': '需>2.5万亿', 'actual': '2.91万亿（7/9）'},
])

# ==========================================
# 5. 限售股解禁详情
# ==========================================
gen.add_impact_analysis = None  # 先重置

# 手动添加限售股解禁详情section
from v3.components.layout import Section, SubCard
from v3.components.data import DataCard, Badge

unlock_html = '''
<div style="overflow-x: auto;">
<table style="width: 100%; border-collapse: collapse; font-size: 13px; color: #e2e8f0;">
<thead>
<tr style="border-bottom: 2px solid rgba(255,255,255,0.15);">
<th style="text-align: left; padding: 12px 10px; font-weight: 600; color: #f1f5f9;">股票名称</th>
<th style="text-align: left; padding: 12px 10px; font-weight: 600; color: #f1f5f9;">代码</th>
<th style="text-align: right; padding: 12px 10px; font-weight: 600; color: #f1f5f9;">解禁数量(万股)</th>
<th style="text-align: right; padding: 12px 10px; font-weight: 600; color: #f1f5f9;">占总股本%</th>
<th style="text-align: right; padding: 12px 10px; font-weight: 600; color: #f1f5f9;">占流通股%</th>
<th style="text-align: center; padding: 12px 10px; font-weight: 600; color: #f1f5f9;">压力等级</th>
</tr>
</thead>
<tbody>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.06);">
<td style="padding: 10px;"><b>TCL科技</b></td>
<td style="padding: 10px; color: #94a3b8;">000100</td>
<td style="padding: 10px; text-align: right;">98,629</td>
<td style="padding: 10px; text-align: right;">4.74%</td>
<td style="padding: 10px; text-align: right;">5.16%</td>
<td style="padding: 10px; text-align: center;"><span style="background: rgba(239,68,68,0.15); color: #f87171; padding: 3px 10px; border-radius: 6px; font-size: 12px; font-weight: 500;">高</span></td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.06);">
<td style="padding: 10px;"><b>天承科技</b></td>
<td style="padding: 10px; color: #94a3b8;">688603</td>
<td style="padding: 10px; text-align: right;">7,730</td>
<td style="padding: 10px; text-align: right;">61.98%</td>
<td style="padding: 10px; text-align: right;">163.01%</td>
<td style="padding: 10px; text-align: center;"><span style="background: rgba(239,68,68,0.15); color: #f87171; padding: 3px 10px; border-radius: 6px; font-size: 12px; font-weight: 500;">极高</span></td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.06);">
<td style="padding: 10px;"><b>恒工精密</b></td>
<td style="padding: 10px; color: #94a3b8;">301261</td>
<td style="padding: 10px; text-align: right;">4,963</td>
<td style="padding: 10px; text-align: right;">56.46%</td>
<td style="padding: 10px; text-align: right;">132.25%</td>
<td style="padding: 10px; text-align: center;"><span style="background: rgba(239,68,68,0.15); color: #f87171; padding: 3px 10px; border-radius: 6px; font-size: 12px; font-weight: 500;">极高</span></td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.06);">
<td style="padding: 10px;"><b>同宇新材</b></td>
<td style="padding: 10px; color: #94a3b8;">301630</td>
<td style="padding: 10px; text-align: right;">698</td>
<td style="padding: 10px; text-align: right;">12.46%</td>
<td style="padding: 10px; text-align: right;">49.86%</td>
<td style="padding: 10px; text-align: center;"><span style="background: rgba(245,158,11,0.15); color: #fbbf24; padding: 3px 10px; border-radius: 6px; font-size: 12px; font-weight: 500;">中</span></td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.06);">
<td style="padding: 10px;"><b>特锐德</b></td>
<td style="padding: 10px; color: #94a3b8;">300001</td>
<td style="padding: 10px; text-align: right;">445</td>
<td style="padding: 10px; text-align: right;">0.42%</td>
<td style="padding: 10px; text-align: right;">0.43%</td>
<td style="padding: 10px; text-align: center;"><span style="background: rgba(34,197,94,0.15); color: #4ade80; padding: 3px 10px; border-radius: 6px; font-size: 12px; font-weight: 500;">低</span></td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.06);">
<td style="padding: 10px;"><b>快克智能</b></td>
<td style="padding: 10px; color: #94a3b8;">603203</td>
<td style="padding: 10px; text-align: right;">234</td>
<td style="padding: 10px; text-align: right;">0.71%</td>
<td style="padding: 10px; text-align: right;">0.72%</td>
<td style="padding: 10px; text-align: center;"><span style="background: rgba(34,197,94,0.15); color: #4ade80; padding: 3px 10px; border-radius: 6px; font-size: 12px; font-weight: 500;">低</span></td>
</tr>
<tr>
<td style="padding: 10px;"><b>宁新新材</b></td>
<td style="padding: 10px; color: #94a3b8;">920719</td>
<td style="padding: 10px; text-align: right;">115</td>
<td style="padding: 10px; text-align: right;">1.23%</td>
<td style="padding: 10px; text-align: right;">1.57%</td>
<td style="padding: 10px; text-align: center;"><span style="background: rgba(34,197,94,0.15); color: #4ade80; padding: 3px 10px; border-radius: 6px; font-size: 12px; font-weight: 500;">低</span></td>
</tr>
</tbody>
</table>
</div>
<div style="margin-top: 16px; padding: 14px 16px; background: rgba(239,68,68,0.08); border-left: 3px solid #ef4444; border-radius: 8px; font-size: 13px; color: #fca5a5; line-height: 1.7;">
<b>⚠️ 解禁压力分析：</b>明日（7月10日）共有10只股票限售解禁，合计约11.3亿股。重点关注三个高压力标的：<br>
① <b>TCL科技（000100）</b>：9.86亿股定增限售股解禁，市值约55亿元，解禁主体含深圳国资产业基金。7月9日该股已出现反弹但未能封板，显示资金对解禁有顾虑。面板行业正处于周期底部回升阶段，叠加AI显示、钙钛矿等新业务布局，国资股东大幅减持概率较低，但短期抛压仍需消化，建议观望为主，等待解禁落地后再做布局。<br>
② <b>天承科技（688603）</b>：61.98%总股本解禁，占流通股比高达163%，是明日压力最大的标的。公司主营PCB专用电子化学品，受益于AI服务器PCB需求增长，但如此大规模解禁下短期承压明显，坚决回避。<br>
③ <b>恒工精密（301261）</b>：56.46%总股本首发限售解禁，流通盘扩容超1.3倍，小市值标的波动风险大，建议规避。
</div>
'''

unlock_section = Section(title="🔓 限售股解禁详情", content=unlock_html, icon="unlock")
gen._components.append(unlock_section)

# ==========================================
# 6. 新股申购
# ==========================================
ipo_html = '''
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 16px;">
<div style="background: linear-gradient(135deg, rgba(59,130,246,0.15) 0%, rgba(147,51,234,0.15) 100%);
     border: 1px solid rgba(59,130,246,0.25); border-radius: 16px; padding: 20px;">
<div style="display: flex; align-items: center; gap: 12px; margin-bottom: 14px;">
<div style="width: 48px; height: 48px; background: linear-gradient(135deg, #3b82f6, #8b5cf6);
     border-radius: 12px; display: flex; align-items: center; justify-content: center;
     font-size: 24px;">💉</div>
<div>
<div style="font-size: 18px; font-weight: 700; color: #f1f5f9;">泰诺麦博</div>
<div style="font-size: 12px; color: #94a3b8;">787806 · 科创板 · 创新药</div>
</div>
</div>
<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px; font-size: 13px;">
<div style="background: rgba(255,255,255,0.05); padding: 10px; border-radius: 8px;">
<div style="color: #94a3b8; font-size: 11px;">发行价</div>
<div style="color: #f1f5f9; font-weight: 600; font-size: 16px;">14.46元</div>
</div>
<div style="background: rgba(255,255,255,0.05); padding: 10px; border-radius: 8px;">
<div style="color: #94a3b8; font-size: 11px;">发行数量</div>
<div style="color: #f1f5f9; font-weight: 600; font-size: 16px;">6908万股</div>
</div>
<div style="background: rgba(255,255,255,0.05); padding: 10px; border-radius: 8px;">
<div style="color: #94a3b8; font-size: 11px;">网上发行</div>
<div style="color: #f1f5f9; font-weight: 600; font-size: 16px;">1174万股</div>
</div>
<div style="background: rgba(255,255,255,0.05); padding: 10px; border-radius: 8px;">
<div style="color: #94a3b8; font-size: 11px;">申购上限</div>
<div style="color: #f1f5f9; font-weight: 600; font-size: 16px;">1.15万股</div>
</div>
<div style="background: rgba(255,255,255,0.05); padding: 10px; border-radius: 8px;">
<div style="color: #94a3b8; font-size: 11px;">顶格市值</div>
<div style="color: #f1f5f9; font-weight: 600; font-size: 16px;">11.50万元</div>
</div>
<div style="background: rgba(255,255,255,0.05); padding: 10px; border-radius: 8px;">
<div style="color: #94a3b8; font-size: 11px;">预计募资</div>
<div style="color: #f1f5f9; font-weight: 600; font-size: 16px;">约10亿元</div>
</div>
</div>
<div style="margin-top: 14px; padding: 12px; background: rgba(34,197,94,0.08); border-radius: 8px; font-size: 13px; color: #86efac; line-height: 1.6;">
<b>📋 申购建议：积极申购</b><br>
公司专注于医学研究和试验发展，所属创新药赛道，发行价14.46元偏低，科创板新股破发风险可控。虽然2024-2025年连续亏损，但创新药研发型企业亏损为行业常态，建议顶格申购。
</div>
</div>

<div style="background: linear-gradient(135deg, rgba(245,158,11,0.15) 0%, rgba(239,68,68,0.15) 100%);
     border: 1px solid rgba(245,158,11,0.25); border-radius: 16px; padding: 20px;">
<div style="display: flex; align-items: center; gap: 12px; margin-bottom: 14px;">
<div style="width: 48px; height: 48px; background: linear-gradient(135deg, #f59e0b, #ef4444);
     border-radius: 12px; display: flex; align-items: center; justify-content: center;
     font-size: 24px;">💾</div>
<div>
<div style="font-size: 18px; font-weight: 700; color: #f1f5f9;">长鑫科技（待申购）</div>
<div style="font-size: 12px; color: #94a3b8;">787825 · 7月16日 · 存储芯片龙头</div>
</div>
</div>
<div style="font-size: 13px; color: #e2e8f0; line-height: 1.7; margin-bottom: 14px;">
国产DRAM龙头长鑫科技将于7月16日网上申购，发行66.88亿股，预计募资312亿元，将成A股史上最大科技IPO之一。
公司是全球第四大DRAM厂商，2025年净利润18.75亿元（扭亏为盈）。长鑫上市将重塑半导体板块估值体系，是7月最重磅的资本市场事件。
</div>
<div style="padding: 12px; background: rgba(245,158,11,0.08); border-radius: 8px; font-size: 13px; color: #fcd34d; line-height: 1.6;">
<b>📌 关注要点：</b>长鑫上市带来的不仅是打新机会，更重要的是对整个存储产业链的估值锚定效应。建议提前布局受益标的：雅克科技（前驱体材料）、铜冠铜箔（锂电铜箔+电子铜箔）、北方华创（设备）等。
</div>
</div>
</div>
'''

ipo_section = Section(title="💰 新股申购与IPO动态", content=ipo_html, icon="trending-up")
gen._components.append(ipo_section)

# ==========================================
# 7. 市场影响深度分析
# ==========================================
impact_html = '''
<div style="line-height: 2; color: #e2e8f0; font-size: 14px;">

<h3 style="color: #f1f5f9; font-size: 18px; margin-bottom: 16px; border-left: 4px solid #f59e0b; padding-left: 12px;">
一、科创50暴涨后的市场走向：放量上攻还是缩量整固？
</h3>

<p style="margin-bottom: 14px; text-indent: 2em;">
7月9日A股上演了足以载入史册的暴涨行情——科创50单日暴涨8.41%，创下历史最大单日涨幅，成交额2245亿元天量，沪指放量上涨1.65%收复4000点，创业板指大涨4.49%收复4000点。沪深两市全天成交2.91万亿元，较前一日放量3502亿元，全市场超4100只个股上涨，逾200只个股涨停。这是一场由存储芯片、半导体全线爆发引领的科技盛宴。
</p>

<p style="margin-bottom: 14px; text-indent: 2em;">
<b>三重催化共振引爆行情：</b>第一，长鑫科技IPO正式启动（7月16日申购），作为国产DRAM第一股，312亿元募资规模点燃了整个半导体板块的热情，市场开始重新审视A股半导体企业的估值天花板；第二，全球存储涨价周期确认，三星Q3 DRAM涨价20%-30%、NAND涨价35%-40%的消息持续发酵，江波龙中报预增744倍成为业绩标杆；第三，多部委同日表态支持新质生产力，中证协、发改委、工信部密集发声，政策合力形成。
</p>

<p style="margin-bottom: 14px; text-indent: 2em;">
<b>明日（7月10日）是行情成色的关键检验日。</b>核心观察三个指标：一是成交额能否维持在2.5万亿以上，2.91万亿的天量如果快速萎缩至2万亿以下，说明增量资金入场不持续，大概率进入缩量整固阶段；二是科创50能否在2100点上方企稳，今日从最低2023点拉到2186点，涨幅巨大，回踩不破2100点才算多头趋势确认；三是中芯国际、兆易创新等标杆股的高位承接力度，这些龙头股的走势决定了半导体主线的持续性。
</p>

<p style="margin-bottom: 20px; text-indent: 2em;">
<b>操作建议：</b>今日暴涨后不建议追高，可等待回踩确认后再布局。科创50回踩2100点或5日线附近是更优买点。重点方向不变：存储芯片/半导体设备（长鑫IPO+涨价周期）、新能源（创业板反弹主力）、券商（市场活跃度提升受益者）。仓位建议6-7成，设好止盈止损。
</p>

<h3 style="color: #f1f5f9; font-size: 18px; margin-bottom: 16px; border-left: 4px solid #3b82f6; padding-left: 12px;">
二、长鑫科技IPO：存储产业链的估值重估机遇
</h3>

<p style="margin-bottom: 14px; text-indent: 2em;">
长鑫科技科创板IPO是7月A股最重要的资本市场事件，没有之一。作为国内唯一规模量产DRAM的企业、全球第四大DRAM厂商，长鑫科技的上市标志着中国存储芯片产业进入新纪元。但斌最新表态认为，长鑫与SK海力士上市并非资金分流利空，反而有望撬开A股硬科技的市值天花板——如果长鑫上市后能达到3-5万亿市值，整个半导体板块的估值空间都将被打开。
</p>

<p style="margin-bottom: 14px; text-indent: 2em;">
从产业链受益逻辑来看，长鑫上市将带动三条投资主线：<b>① 材料端</b>：半导体材料是长鑫供应链中确定性最高的环节，雅克科技（前驱体，已切入长鑫供应链）、上海新阳（光刻胶/电子化学品）、安集科技（CMP抛光液）等直接受益；<b>② 设备端</b>：长鑫扩产带动国产设备采购需求，北方华创、中微公司、精测电子等设备龙头优先受益；<b>③ 封测端</b>：长鑫出货量增长带动先进封装需求，长电科技、华天科技、通富微电等封测龙头间接受益。
</p>

<p style="margin-bottom: 20px; text-indent: 2em;">
<b>核心关注持仓标的：雅克科技（002409）</b>是存储产业链上游电子特气/前驱体龙头，深度绑定长鑫、三星、SK海力士等存储大厂，在S级催化中多次推荐。当前股价约210元，中报业绩有望超预期。但短期涨幅较大，建议在200-210区间分批布局，跌破200元减仓控制风险。<b>铜冠铜箔（301217）</b>：锂电铜箔龙头，电子电路铜箔已切入半导体产业链，受益存储芯片封装需求增长，当前股价约16元，估值处于合理区间。
</p>

<h3 style="color: #f1f5f9; font-size: 18px; margin-bottom: 16px; border-left: 4px solid #10b981; padding-left: 12px;">
三、中报业绩主线：从"炒预期"到"验真假"的关键窗口
</h3>

<p style="margin-bottom: 14px; text-indent: 2em;">
进入7月中旬，A股正式进入中报业绩验证期。截至7月9日，已有171家公司披露半年报预告，预喜率高达87.7%，64家公司净利润翻倍，10余家公司增幅超10倍。存储芯片（江波龙预增744倍）、化工炼化（恒逸石化预增25倍）、创新药（海思科预增5倍+）、券商（天风证券预增7倍）成为高增赛道的代表。
</p>

<p style="margin-bottom: 14px; text-indent: 2em;">
<b>但需要警惕的是，高增速不等于高回报。</b>很多公司的超高增速源于去年同期极低的利润基数，而非基本面发生质变。以江波龙为例，2025年上半年净利润仅1477万元，今年百亿级利润确实震撼，但这更多是行业周期反转+库存重估的结果，不能简单线性外推。投资者需要区分"基数效应型高增长"和"持续成长型高增长"，前者涨一波就会结束，后者才能走出长牛。
</p>

<p style="margin-bottom: 20px; text-indent: 2em;">
<b>业绩线操作策略：</b>优先选择"行业景气度持续向上+公司核心竞争力强+估值合理"的标的，回避"纯基数效应+纯题材炒作+估值已透支"的标的。具体到四大持仓：<b>英维克</b>液冷龙头中报业绩需验证，当前股价仍处深度调整，建议观望等待企稳信号；<b>雅克科技</b>半导体材料龙头，中报预增确定性高，可逢低加仓；<b>铜冠铜箔</b>锂电+电子铜箔双轮驱动，中报有望超预期，持有为主；<b>*ST建艺</b>已确认清仓（7/3最后交易日），不再纳入持仓跟踪。
</p>

<h3 style="color: #f1f5f9; font-size: 18px; margin-bottom: 16px; border-left: 4px solid #8b5cf6; padding-left: 12px;">
四、海外变量：美国CPI数据与全球科技股走向
</h3>

<p style="margin-bottom: 14px; text-indent: 2em;">
7月10日晚间公布的美国6月CPI数据是本周全球市场最重要的经济数据。在美联储6月FOMC会议点阵图显示半数委员预计年内至少加息一次的背景下，CPI走向直接决定7月议息会议的政策基调。如果通胀超预期回落，美联储可能释放降息信号，全球科技股估值将获得进一步支撑；反之，如果通胀粘性超预期，加息预期升温将对全球风险资产形成压制。
</p>

<p style="margin-bottom: 14px; text-indent: 2em;">
<b>海外科技产业方面，两条消息值得重点关注：</b>一是美光科技宣布2500亿美元美国本土投资计划，到2035年在美总投资超2500亿美元，全球存储资本开支持续扩张，设备和材料产业链需求确定性增强；二是Meta计划9月量产自研AI芯片IRIS，2027年算力翻倍至14吉瓦，科技巨头加速芯片自主化，一方面加剧行业竞争，另一方面也印证了AI算力需求的长期增长趋势。
</p>

<p style="margin-bottom: 14px; text-indent: 2em;">
这两条消息对A股的启示是：<b>全球科技产业的资本开支周期远未结束</b>，AI和存储是双轮驱动的确定性主线。国产替代逻辑在巨头自研芯片的背景下反而更加紧迫——只有实现核心技术自主可控，才能在全球科技竞争中立于不败之地。A股半导体设备、材料、EDA等"卡脖子"环节的国产替代空间巨大，是长期配置的优质赛道。
</p>

<h3 style="color: #f1f5f9; font-size: 18px; margin-bottom: 16px; border-left: 4px solid #ef4444; padding-left: 12px;">
五、央行货政例会解读：宽松基调延续，结构性政策倾斜
</h3>

<p style="margin-bottom: 14px; text-indent: 2em;">
7月8日晚间发布的央行二季度货币政策委员会例会纪要，是理解下半年A股流动性环境的顶层文件。核心信号有三个：一是<b>宽松基调锁定</b>，"继续实施适度宽松的货币政策，加大逆周期和跨周期调节力度"，打消市场对流动性收紧的担忧；二是<b>结构性支持顺序调整</b>，扩大内需首次排在第一位，其次是科技创新、中小微企业，意味着消费信贷和内需刺激政策有望加码；三是<b>汇率稳定优先</b>，"增强外汇市场韧性，稳定市场预期"，为北向资金持续流入创造条件。
</p>

<p style="margin-bottom: 14px; text-indent: 2em;">
对A股的影响：流动性宽松环境下，科技成长赛道估值有支撑，不会出现系统性杀估值；内需消费板块有望迎来政策催化，可作为科技主线的均衡配置；北向资金回流环境改善，外资重仓的存储龙头、头部半导体、优质消费龙头有望持续获得资金加持。
</p>

</div>
'''

impact_section = Section(title="🔍 深度影响分析与操作策略", content=impact_html, icon="search", variant="highlight")
gen._components.append(impact_section)

# ==========================================
# 8. 催化深度分析（Skill增强 - 前3大事件）
# ==========================================
deep_events = [
    {
        'title': '长鑫科技IPO开启存储新时代',
        'type': 'meeting',
        'description': '国产DRAM龙头长鑫科技7月16日科创板申购，预计募资312亿元，将重塑A股半导体估值体系',
        'category': 'IPO里程碑'
    },
    {
        'title': '科创50暴涨后行情延续性',
        'type': 'general',
        'description': '科创50单日暴涨8.41%创历史纪录，2.91万亿天量成交，明日是行情关键检验日',
        'category': '市场走势'
    },
    {
        'title': '美国6月CPI数据公布',
        'type': 'data',
        'description': '7月10日晚间公布美国6月CPI，通胀走向决定美联储7月议息会议基调，影响全球流动性',
        'category': '海外数据'
    },
]

gen.add_catalyst_deep_analysis(deep_events)

# ==========================================
# 9. 本周事件日历表格
# ==========================================
calendar_html = '''
<div style="overflow-x: auto;">
<table style="width: 100%; border-collapse: collapse; font-size: 13px; color: #e2e8f0;">
<thead>
<tr style="border-bottom: 2px solid rgba(255,255,255,0.15); background: rgba(255,255,255,0.03);">
<th style="text-align: center; padding: 12px 8px; font-weight: 600; color: #f1f5f9; width: 90px;">日期</th>
<th style="text-align: left; padding: 12px 10px; font-weight: 600; color: #f1f5f9;">事件</th>
<th style="text-align: center; padding: 12px 10px; font-weight: 600; color: #f1f5f9; width: 80px;">类型</th>
<th style="text-align: center; padding: 12px 10px; font-weight: 600; color: #f1f5f9; width: 80px;">影响等级</th>
</tr>
</thead>
<tbody>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.06);">
<td style="padding: 10px; text-align: center; font-weight: 600; color: #fbbf24;">7月10日 周五</td>
<td style="padding: 10px;">泰诺麦博科创板申购（787806）</td>
<td style="padding: 10px; text-align: center;"><span style="background: rgba(59,130,246,0.15); color: #60a5fa; padding: 2px 8px; border-radius: 4px; font-size: 11px;">新股</span></td>
<td style="padding: 10px; text-align: center;">⭐⭐</td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.06); background: rgba(251,191,36,0.03);">
<td style="padding: 10px; text-align: center; font-weight: 600; color: #fbbf24;">7月10日 周五</td>
<td style="padding: 10px;">TCL科技9.86亿股定增限售股解禁（约55亿市值）</td>
<td style="padding: 10px; text-align: center;"><span style="background: rgba(239,68,68,0.15); color: #f87171; padding: 2px 8px; border-radius: 4px; font-size: 11px;">解禁</span></td>
<td style="padding: 10px; text-align: center;">⭐⭐⭐</td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.06); background: rgba(251,191,36,0.03);">
<td style="padding: 10px; text-align: center; font-weight: 600; color: #fbbf24;">7月10日 周五</td>
<td style="padding: 10px;">美国6月CPI数据公布（北京时间晚间）</td>
<td style="padding: 10px; text-align: center;"><span style="background: rgba(139,92,246,0.15); color: #a78bfa; padding: 2px 8px; border-radius: 4px; font-size: 11px;">数据</span></td>
<td style="padding: 10px; text-align: center;">⭐⭐⭐⭐</td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.06);">
<td style="padding: 10px; text-align: center; font-weight: 600; color: #94a3b8;">7月11日 周六</td>
<td style="padding: 10px;">WAIC 2026 倒计时6天，参展商/议程持续披露</td>
<td style="padding: 10px; text-align: center;"><span style="background: rgba(16,185,129,0.15); color: #34d399; padding: 2px 8px; border-radius: 4px; font-size: 11px;">会议</span></td>
<td style="padding: 10px; text-align: center;">⭐⭐</td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.06);">
<td style="padding: 10px; text-align: center; font-weight: 600; color: #94a3b8;">7月12日 周日</td>
<td style="padding: 10px;">中报预告密集披露（7/15前主板强制披露）</td>
<td style="padding: 10px; text-align: center;"><span style="background: rgba(245,158,11,0.15); color: #fbbf24; padding: 2px 8px; border-radius: 4px; font-size: 11px;">业绩</span></td>
<td style="padding: 10px; text-align: center;">⭐⭐⭐</td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.06); background: rgba(16,185,129,0.03);">
<td style="padding: 10px; text-align: center; font-weight: 600; color: #34d399;">7月13日 周一</td>
<td style="padding: 10px;">英华特38.28%限售股解禁</td>
<td style="padding: 10px; text-align: center;"><span style="background: rgba(239,68,68,0.15); color: #f87171; padding: 2px 8px; border-radius: 4px; font-size: 11px;">解禁</span></td>
<td style="padding: 10px; text-align: center;">⭐⭐</td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.06); background: rgba(16,185,129,0.03);">
<td style="padding: 10px; text-align: center; font-weight: 600; color: #34d399;">7月14日 周二</td>
<td style="padding: 10px;">中国6月社融/M2/信贷数据公布（预期）</td>
<td style="padding: 10px; text-align: center;"><span style="background: rgba(59,130,246,0.15); color: #60a5fa; padding: 2px 8px; border-radius: 4px; font-size: 11px;">数据</span></td>
<td style="padding: 10px; text-align: center;">⭐⭐⭐</td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.06); background: rgba(16,185,129,0.03);">
<td style="padding: 10px; text-align: center; font-weight: 600; color: #34d399;">7月15日 周三</td>
<td style="padding: 10px;">主板中报强制披露截止日；国家统计局二季度GDP/工业/消费数据</td>
<td style="padding: 10px; text-align: center;"><span style="background: rgba(245,158,11,0.15); color: #fbbf24; padding: 2px 8px; border-radius: 4px; font-size: 11px;">数据</span></td>
<td style="padding: 10px; text-align: center;">⭐⭐⭐⭐⭐</td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.06); background: rgba(239,68,68,0.03);">
<td style="padding: 10px; text-align: center; font-weight: 600; color: #f87171;">7月16日 周四</td>
<td style="padding: 10px;"><b>长鑫科技科创板网上申购（688825）</b> · WAIC 2026倒计时1天</td>
<td style="padding: 10px; text-align: center;"><span style="background: rgba(245,158,11,0.15); color: #fbbf24; padding: 2px 8px; border-radius: 4px; font-size: 11px;">IPO</span></td>
<td style="padding: 10px; text-align: center;">⭐⭐⭐⭐⭐</td>
</tr>
<tr style="background: rgba(139,92,246,0.03);">
<td style="padding: 10px; text-align: center; font-weight: 600; color: #a78bfa;">7月17日 周五</td>
<td style="padding: 10px;"><b>2026世界人工智能大会开幕（WAIC 2026）</b> · 华为Atlas 950首秀</td>
<td style="padding: 10px; text-align: center;"><span style="background: rgba(139,92,246,0.15); color: #a78bfa; padding: 2px 8px; border-radius: 4px; font-size: 11px;">盛会</span></td>
<td style="padding: 10px; text-align: center;">⭐⭐⭐⭐⭐</td>
</tr>
</tbody>
</table>
</div>
'''

calendar_section = Section(title="📅 本周重要事件日历（7/10 - 7/17）", content=calendar_html, icon="calendar")
gen._components.append(calendar_section)

# ==========================================
# 10. 风险提示
# ==========================================
gen.add_risk_warning([
    "科创50暴涨后短期乖离率过大，存在回踩调整风险，若量能快速萎缩则行情持续性存疑",
    "美国6月CPI数据若超预期上行，可能引发美联储加息预期升温，压制全球科技股估值",
    "中报预告密集披露期，业绩不及预期的高位科技股面临大幅回调风险",
    "长鑫科技IPO临近，若发行定价过高或上市后表现不佳，可能拖累半导体板块情绪",
    "7月下旬解禁压力集中释放，天承科技、恒工精密等大规模解禁标的短期抛压显著",
    "外围地缘政治不确定性（中东局势、中美关系、台海局势）可能引发市场波动",
    "TCL科技等大额解禁标的若出现超预期减持，可能对面板板块形成短期压制",
    "本报告基于公开信息整理分析，不构成投资建议，投资有风险入市需谨慎"
])

# ==========================================
# 发布报告
# ==========================================
print("=" * 60)
print("🚀 开始生成明日催化剂报告（2026-07-10）")
print("=" * 60)

result = gen.publish(
    title="20260710_明日催化剂",
    report_type="tomorrow_catalyst",
    excerpt="科创50暴涨8.41%后行情检验日 · 长鑫IPO倒计时6天 · 美国CPI今晚公布 · TCL科技55亿解禁 · 中报业绩主线确立",
    auto_deploy=False  # 手动控制git部署
)

print("\n" + "=" * 60)
print("📊 发布结果")
print("=" * 60)
for k, v in result.items():
    if k != 'errors':
        print(f"  {k}: {v}")
if result.get('errors'):
    print("  errors:")
    for e in result['errors']:
        print(f"    - {e}")

# 检查文件大小
import os
if result.get('filepath') and os.path.exists(result['filepath']):
    size = os.path.getsize(result['filepath'])
    print(f"\n📁 文件大小: {size/1024:.1f} KB")
