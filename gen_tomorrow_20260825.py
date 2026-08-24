#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
明日催化剂 - 2026年8月25日
"""
import sys
import os

os.chdir('/root/daily-news-insight')
sys.path.insert(0, 'v3')

from v3.generators.tomorrow_catalyst import TomorrowCatalystGenerator

# 创建生成器
gen = TomorrowCatalystGenerator(
    date_str="20260825",
    subtitle="2026.08.25 · 明日催化剂"
)

# ========== 1. 明日核心催化 ==========
core_catalyst = """
<b>三大核心催化事件：</b>
<br><br>
① <b>十四届全国人大常委会第二十四次会议开幕</b>（8月25-28日）——审议医保法、耕地保护法、银行业监督管理法修订等10部法律草案，同时审议国务院关于今年以来国民经济和社会发展计划执行情况报告、预算执行情况报告、政府债务管理报告。会议释放的政策信号将对A股市场情绪产生重要影响，重点关注医保改革、银行监管、粮食安全三大方向。
<br><br>
② <b>苏盐井神1.64亿股定增限售解禁</b>（市值14.7亿元，占总股本17.14%）——本次解禁为2023年8月定增配售股份上市，发行价约6.78元/股，当前股价8.98元，定增股东浮盈约32%。作为盐化工+储能概念标的，大额解禁可能引发短期抛压，需警惕股价波动风险。
<br><br>
③ <b>第二十六届中国国际投资贸易洽谈会新闻发布会</b>（15:00国新办）——商务部副部长凌激介绍投洽会有关情况。作为年度投资盛会的预热发布会，可能释放吸引外资、对外开放新信号，利好跨境电商、外贸、自贸区概念板块。
"""
gen.add_key_catalyst(core_catalyst)

# ========== 2. 明日事件日历 ==========
events = [
    {
        'type': 'meeting',
        'title': '十四届全国人大常委会第二十四次会议',
        'description': '8月25日至28日在北京举行，审议医保法、耕地保护法、银行监管法等10部法律草案，以及经济社会发展计划执行、预算执行、政府债务管理等报告。',
        'category': '国家级会议'
    },
    {
        'type': 'policy',
        'title': '国新办：第二十六届投洽会新闻发布会',
        'description': '8月25日下午3时，商务部副部长凌激、福建省副省长赵增连介绍第二十六届中国国际投资贸易洽谈会有关情况并答记者问。',
        'category': '政策发布会'
    },
    {
        'type': 'data',
        'title': '6000亿元1年期MLF到期',
        'description': '8月25日有6000亿元1年期中期借贷便利（MLF）到期，央行续做操作及利率变化备受市场关注，是观察货币政策走向的重要窗口。',
        'category': '流动性'
    },
    {
        'type': 'meeting',
        'title': '文昌国际航空航天论坛·金融赋能分论坛',
        'description': '8月25日举行"金融赋能商业航天产业发展论坛"，打通技术创新、产业发展与资本市场连接，商业航天概念股或受催化。',
        'category': '产业论坛'
    },
    {
        'type': 'meeting',
        'title': '德国政府年度内阁闭门会议',
        'description': '8月25-26日，德国总理默茨与内阁部长及企业界代表举行闭门磋商，讨论德国工业竞争力、国家主权和关键技术等议题。',
        'category': '海外会议'
    },
    {
        'type': 'earnings',
        'title': 'A股半年报密集披露期',
        'description': '8月25日约200家A股公司披露半年报，包括中矿资源(净利+1147%)、士兰微(净利+95%)、华润微(净利+113%)、长飞光纤(净利+889%)等重磅标的。',
        'category': '业绩公告'
    },
    {
        'type': 'general',
        'title': '马矿股份中签缴款日',
        'description': '上交所主板新股马矿股份(780123)中签号公布及缴款日，发行价6.65元，发行市盈率13.81倍，主营铁矿石采选。',
        'category': '新股申购'
    },
    {
        'type': 'meeting',
        'title': '欧洲理事会主席巡访欧盟多国',
        'description': '8月25日起，欧洲理事会主席科斯塔巡访欧盟多国，力争在2026年底前达成下一期多年度财政框架(MFF)协议。',
        'category': '海外政治'
    },
]
gen.add_events_calendar(events)

# ========== 3. 限售股解禁详情 ==========
from v3.components.layout import Section

restriction_html = '''
<div style="overflow-x: auto;">
<table style="width: 100%; border-collapse: collapse; font-size: 13px;">
<thead>
<tr style="background: linear-gradient(135deg, rgba(139,92,246,0.2), rgba(59,130,246,0.2)); 
    border-bottom: 1px solid rgba(255,255,255,0.1);">
<th style="padding: 10px 12px; text-align: left; color: #e2e8f0; font-weight: 600;">股票名称</th>
<th style="padding: 10px 12px; text-align: right; color: #e2e8f0; font-weight: 600;">解禁数量</th>
<th style="padding: 10px 12px; text-align: right; color: #e2e8f0; font-weight: 600;">解禁市值</th>
<th style="padding: 10px 12px; text-align: right; color: #e2e8f0; font-weight: 600;">占总股本</th>
<th style="padding: 10px 12px; text-align: center; color: #e2e8f0; font-weight: 600;">解禁类型</th>
<th style="padding: 10px 12px; text-align: center; color: #e2e8f0; font-weight: 600;">风险等级</th>
</tr>
</thead>
<tbody>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.05);">
<td style="padding: 10px 12px; color: #f1f5f9;"><b>苏盐井神</b><br><span style="color:#94a3b8; font-size:11px;">603299</span></td>
<td style="padding: 10px 12px; text-align: right; color: #f87171;">1.64亿股</td>
<td style="padding: 10px 12px; text-align: right; color: #f87171;">14.70亿元</td>
<td style="padding: 10px 12px; text-align: right; color: #fbbf24;">17.14%</td>
<td style="padding: 10px 12px; text-align: center; color: #94a3b8;">增发法人配售</td>
<td style="padding: 10px 12px; text-align: center;"><span style="background:#fef3c7; color:#92400e; padding:2px 8px; border-radius:4px; font-size:11px; font-weight:500;">高风险</span></td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.05);">
<td style="padding: 10px 12px; color: #f1f5f9;"><b>泰凌微</b><br><span style="color:#94a3b8; font-size:11px;">688591</span></td>
<td style="padding: 10px 12px; text-align: right; color: #fbbf24;">2709万股</td>
<td style="padding: 10px 12px; text-align: right; color: #fbbf24;">7.30亿元</td>
<td style="padding: 10px 12px; text-align: right; color: #fbbf24;">11.21%</td>
<td style="padding: 10px 12px; text-align: center; color: #94a3b8;">发行前股份</td>
<td style="padding: 10px 12px; text-align: center;"><span style="background:#fef3c7; color:#92400e; padding:2px 8px; border-radius:4px; font-size:11px; font-weight:500;">中高</span></td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.05);">
<td style="padding: 10px 12px; color: #f1f5f9;"><b>奥来德</b><br><span style="color:#94a3b8; font-size:11px;">688378</span></td>
<td style="padding: 10px 12px; text-align: right; color: #22c55e;">832万股</td>
<td style="padding: 10px 12px; text-align: right; color: #22c55e;">3.81亿元</td>
<td style="padding: 10px 12px; text-align: right; color: #22c55e;">3.18%</td>
<td style="padding: 10px 12px; text-align: center; color: #94a3b8;">增发原股东配售</td>
<td style="padding: 10px 12px; text-align: center;"><span style="background:#dcfce7; color:#166534; padding:2px 8px; border-radius:4px; font-size:11px; font-weight:500;">低风险</span></td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.05);">
<td style="padding: 10px 12px; color: #f1f5f9;"><b>蓝丰生化</b><br><span style="color:#94a3b8; font-size:11px;">002513</span></td>
<td style="padding: 10px 12px; text-align: right; color: #22c55e;">604万股</td>
<td style="padding: 10px 12px; text-align: right; color: #22c55e;">0.32亿元</td>
<td style="padding: 10px 12px; text-align: right; color: #22c55e;">1.61%</td>
<td style="padding: 10px 12px; text-align: center; color: #94a3b8;">股权激励</td>
<td style="padding: 10px 12px; text-align: center;"><span style="background:#dcfce7; color:#166534; padding:2px 8px; border-radius:4px; font-size:11px; font-weight:500;">低风险</span></td>
</tr>
<tr>
<td style="padding: 10px 12px; color: #f1f5f9;"><b>赛福天/纳尔股份</b><br><span style="color:#94a3b8; font-size:11px;">603028/002825</span></td>
<td style="padding: 10px 12px; text-align: right; color: #22c55e;">261万股</td>
<td style="padding: 10px 12px; text-align: right; color: #22c55e;">0.21亿元</td>
<td style="padding: 10px 12px; text-align: right; color: #22c55e;">＜1%</td>
<td style="padding: 10px 12px; text-align: center; color: #94a3b8;">股权激励</td>
<td style="padding: 10px 12px; text-align: center;"><span style="background:#dcfce7; color:#166534; padding:2px 8px; border-radius:4px; font-size:11px; font-weight:500;">低风险</span></td>
</tr>
</tbody>
</table>
</div>
<div style="margin-top: 12px; padding: 10px 14px; background: rgba(251,191,36,0.08); 
    border: 1px solid rgba(251,191,36,0.2); border-radius: 8px; font-size: 12px; color: #fcd34d; line-height: 1.6;">
<b>解禁影响研判：</b>明日6股解禁合计约2.08亿股、市值26.6亿元，整体压力不大。核心风险标的是<b>苏盐井神</b>（14.7亿/17.14%占比），定增股东浮盈约32%可能触发获利了结；<b>泰凌微</b>为IPO原股东解禁，首发价与当前价接近（26.7元），抛压相对可控。其余股权激励类解禁影响极小。
</div>
'''

restriction_section = Section(title="限售股解禁详情", content=restriction_html, icon="lock")
gen._components.append(restriction_section)

# ========== 4. 新股申购与上市 ==========
ipo_html = '''
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 14px;">

<div style="background: rgba(30,41,59,0.6); border: 1px solid rgba(255,255,255,0.08); border-radius: 12px; padding: 16px;">
<div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 10px;">
<span style="font-size: 15px; font-weight: 600; color: #f1f5f9;">马矿股份 (601123)</span>
<span style="background: rgba(245,158,11,0.15); color: #fbbf24; padding: 3px 8px; border-radius: 6px; font-size: 11px;">中签缴款</span>
</div>
<div style="font-size: 12px; color: #94a3b8; line-height: 1.8;">
<b>申购代码：</b>780123<br>
<b>发行价格：</b>6.65元/股<br>
<b>发行市盈率：</b>13.81倍（行业均值36.09倍）<br>
<b>主营业务：</b>铁矿石采选、铁精粉/钼精矿销售<br>
<b>募集资金：</b>约8.21亿元（马坑铁矿采选扩能）<br>
<b>申购建议：</b>积极申购，发行价低、市盈率显著低于行业，破发风险极小
</div>
</div>

<div style="background: rgba(30,41,59,0.6); border: 1px solid rgba(255,255,255,0.08); border-radius: 12px; padding: 16px;">
<div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 10px;">
<span style="font-size: 15px; font-weight: 600; color: #f1f5f9;">近期申购预告</span>
<span style="background: rgba(59,130,246,0.15); color: #60a5fa; padding: 3px 8px; border-radius: 6px; font-size: 11px;">本周</span>
</div>
<div style="font-size: 12px; color: #94a3b8; line-height: 1.8;">
<b>8月26日（周三）：</b>洛轴股份(301699)、天博智能(732448)<br>
&nbsp;&nbsp;- 洛轴股份：创业板，发行约1.24亿股，高中签率预期<br>
&nbsp;&nbsp;- 天博智能：沪市主板，发行价62.65元，募资18.8亿<br>
<b>8月28日（周五）：</b>电科思仪(301689)<br>
&nbsp;&nbsp;- 创业板，发行约1.02亿股，高中签率预期<br>
<b>港股招股中：</b>希音(00625.HK)、梅卡曼德(09615.HK)<br>
&nbsp;&nbsp;- 8月27日截止招股，关注跨境电商/机器人赛道
</div>
</div>

</div>
'''
ipo_section = Section(title="新股申购与上市", content=ipo_html, icon="trending-up")
gen._components.append(ipo_section)

# ========== 5. 重要数据发布 ==========
data_list = [
    {'name': '中国1年期MLF到期', 'prev': '6000亿元', 'expect': '等量续做概率大', 'actual': '待公布'},
    {'name': '澳洲联储8月会议纪要', 'prev': '4.35%', 'expect': '维持不变', 'actual': '待公布'},
    {'name': '美国7月PCE物价指数', 'prev': '同比3.7%', 'expect': '同比放缓', 'actual': '8月27日公布'},
    {'name': '美国Q2 GDP修正值', 'prev': '初值1.5%', 'expect': '小幅上修', 'actual': '8月27日公布'},
]
gen.add_data_release(data_list)

# ========== 6. 海外大事与全球市场 ==========
overseas_html = '''
<div style="display: flex; flex-direction: column; gap: 12px;">

<div style="background: linear-gradient(135deg, rgba(239,68,68,0.08), rgba(249,115,22,0.08)); 
    border: 1px solid rgba(239,68,68,0.15); border-radius: 10px; padding: 14px;">
<div style="display: flex; align-items: center; gap: 8px; margin-bottom: 6px;">
<span style="font-size: 16px;">🇺🇸</span>
<span style="font-weight: 600; color: #fca5a5; font-size: 14px;">英伟达Q2财报（8月26日盘后）</span>
<span style="background: rgba(239,68,68,0.2); color: #f87171; padding: 2px 6px; border-radius: 4px; font-size: 10px;">⭐ 重磅</span>
</div>
<div style="font-size: 12px; color: #cbd5e1; line-height: 1.6;">
市场预期营收920亿美元（同比+96%），EPS 2.09美元。数据中心业务预计突破854亿美元（+107%）。
<b style="color:#fbbf24;">核心看点：</b>Q3营收指引、Blackwell Ultra进度、毛利率走势、AI资本开支可持续性。
过去四季度均超预期但次日平均跌超5%，本次市场预期极高，"好"已不够，必须"超预期好"。
<b style="color:#60a5fa;">影响A股：</b>算力/光模块/服务器/液冷全产业链，英维克、中际旭创等核心标的将受直接影响。
</div>
</div>

<div style="background: linear-gradient(135deg, rgba(139,92,246,0.08), rgba(59,130,246,0.08)); 
    border: 1px solid rgba(139,92,246,0.15); border-radius: 10px; padding: 14px;">
<div style="display: flex; align-items: center; gap: 8px; margin-bottom: 6px;">
<span style="font-size: 16px;">🏛️</span>
<span style="font-weight: 600; color: #c4b5fd; font-size: 14px;">杰克逊霍尔全球央行年会（8月27-29日）</span>
<span style="background: rgba(139,92,246,0.2); color: #a78bfa; padding: 2px 6px; border-radius: 4px; font-size: 10px;">重磅</span>
</div>
<div style="font-size: 12px; color: #cbd5e1; line-height: 1.6;">
美联储主席沃什将于8月28日发表主旨演讲（上任后首次），主题为"大局观"。
<b style="color:#fbbf24;">核心看点：</b>美国经济前景评估、通胀走向、利率路径信号。
当前市场已price-in 9月不加息预期，若沃什释放偏鹰信号可能推高美元美债、压制风险资产。
</div>
</div>

<div style="background: linear-gradient(135deg, rgba(245,158,11,0.08), rgba(239,68,68,0.08)); 
    border: 1px solid rgba(245,158,11,0.15); border-radius: 10px; padding: 14px;">
<div style="display: flex; align-items: center; gap: 8px; margin-bottom: 6px;">
<span style="font-size: 16px;">⚔️</span>
<span style="font-weight: 600; color: #fcd34d; font-size: 14px;">美伊对峙升级·霍尔木兹海峡风险</span>
<span style="background: rgba(245,158,11,0.2); color: #fbbf24; padding: 2px 6px; border-radius: 4px; font-size: 10px;">持续发酵</span>
</div>
<div style="font-size: 12px; color: #cbd5e1; line-height: 1.6;">
美财长贝森特8月24日宣布对伊朗"史上最严"制裁，伊朗石油出口骤降至28.7万桶/日。
伊朗威胁封锁霍尔木兹海峡反击，全球约20%石油运输受影响。国际油价已升至93美元以上，
柴油价格创历史新高，欧洲能源危机担忧重燃。关注后续事态升级对A股能源、军工板块催化。
</div>
</div>

<div style="background: linear-gradient(135deg, rgba(16,185,129,0.08), rgba(59,130,246,0.08)); 
    border: 1px solid rgba(16,185,129,0.15); border-radius: 10px; padding: 14px;">
<div style="display: flex; align-items: center; gap: 8px; margin-bottom: 6px;">
<span style="font-size: 16px;">🇰🇷</span>
<span style="font-weight: 600; color: #6ee7b7; font-size: 14px;">半导体全球高管峰会（8月26-27日·韩国）</span>
<span style="background: rgba(16,185,129,0.2); color: #34d399; padding: 2px 6px; border-radius: 4px; font-size: 10px;">产业</span>
</div>
<div style="font-size: 12px; color: #cbd5e1; line-height: 1.6;">
国际半导体产业集团(ISIG)在韩国水原举办全球高管峰会，同步举办芯粒及先进封装技术展。
英伟达、SK海力士、三星等头部企业高管出席，讨论AI时代半导体硬件创新与基础设施重构。
先进封装、HBM、Chiplet概念板块或受技术进展催化。
</div>
</div>

</div>
'''
overseas_section = Section(title="海外大事与全球市场", content=overseas_html, icon="globe")
gen._components.append(overseas_section)

# ========== 7. 市场影响深度分析 ==========
deep_analysis = """
<h3 style="color: #f1f5f9; font-size: 16px; margin-bottom: 14px; border-left: 3px solid #f59e0b; padding-left: 10px;">
事件一：十四届全国人大常委会第二十四次会议开幕 —— 多重政策信号密集释放
</h3>
<div style="font-size: 13px; color: #cbd5e1; line-height: 1.8;">
<p><b>【事件概述】</b>8月25日至28日，十四届全国人大常委会第二十四次会议在北京举行。会议议程涵盖<b>10部法律草案审议</b>和<b>6项重要报告</b>审议，是下半年最重要的立法与政策观察窗口之一。</p>

<p><b>【法律审议亮点及板块影响】</b></p>
<ul style="margin: 8px 0; padding-left: 20px;">
<li><b>医疗保障法草案三审：</b>加强医保基金管理、完善集中采购制度、细化异地就医结算、增加长期护理保险规定。对<b>医药商业、医疗器械、创新药</b>板块影响中性偏正面，医保支付范围扩大有利创新药放量，但集采常态化仍对价格形成压制。重点关注：<b>恒瑞医药、药明康德、迈瑞医疗</b>。</li>
<li><b>银行业监督管理法修订：</b>压实监管职责、加强消费者权益保护、强化金融风险防控。对<b>银行板块</b>整体中性，强化监管长期有利于行业健康发展，但短期合规成本可能上升。</li>
<li><b>耕地保护和质量提升法三审：</b>强化高标准农田建设、黑土地保护、粮食主产区利益补偿。利好<b>种业、农机、农田水利</b>板块，粮食安全主线持续强化。重点关注：<b>隆平高科、一拖股份、大禹节水</b>。</li>
<li><b>企业破产法修订：</b>完善市场退出机制，对<b>困境反转、ST板块</b>影响需关注破产重整相关条款变化。</li>
</ul>

<p><b>【报告审议亮点】</b></p>
<ul style="margin: 8px 0; padding-left: 20px;">
<li><b>国民经济和社会发展计划执行情况报告：</b>将梳理上半年经济运行情况，可能释放下半年稳增长政策加码信号。</li>
<li><b>预算执行情况报告：</b>关注财政支出进度、专项债发行使用情况，判断基建投资力度。</li>
<li><b>2025年度政府债务管理情况报告：</b>关注地方债风险化解进展，城投、基建板块或受影响。</li>
</ul>

<p><b>【投资建议】</b>会议为期4天，期间政策预期可能反复波动。操作上，<b>不建议追高政策概念股</b>，
应等待具体条款落地后再做决策。重点关注医保谈判受益的创新药龙头、粮食安全主题的种业标的，
以及银行板块中报业绩验证后的配置机会。整体偏中长期利好，短期对市场情绪有一定支撑作用。
<span style="color:#22c55e;">【评级：中性偏多】</span></p>
</div>

<div style="height: 20px;"></div>

<h3 style="color: #f1f5f9; font-size: 16px; margin-bottom: 14px; border-left: 3px solid #ef4444; padding-left: 10px;">
事件二：苏盐井神大额定增解禁 —— 盐化工龙头短期承压
</h3>
<div style="font-size: 13px; color: #cbd5e1; line-height: 1.8;">
<p><b>【解禁详情】</b>苏盐井神（603299）明日解禁<b>1.64亿股</b>，占总股本比例<b>17.14%</b>，
按最新收盘价8.98元计算，解禁市值约<b>14.7亿元</b>。本次解禁股份来自2023年8月的定向增发，
发行价约为6.78元/股，定增股东当前浮盈约<b>32%</b>。</p>

<p><b>【解禁性质分析】</b>本次解禁为<b>增发A股法人配售上市</b>，股东以机构投资者为主。
定增浮盈32%在当前市场环境下属于中等水平，部分财务投资者存在获利了结动力。
但考虑到苏盐井神当前估值（PE约15倍）处于历史中低位，且公司盐化工+储能双主业增长稳健，
产业资本大幅减持的概率较低。</p>

<p><b>【公司基本面】</b>苏盐井神是国内盐化工龙头，主营盐矿开采、盐及盐化工产品生产。
公司积极布局盐穴储能业务，已建成多个压缩空气储能和储盐项目，受益于新型储能政策推动。
2026年上半年公司业绩表现稳健，盐化工产品价格稳中向好，储能业务贡献增量。</p>

<p><b>【操作建议】</b>
<span style="color:#f87171;">【短期：谨慎】</span>
明日解禁日可能出现短期抛压，不建议在开盘追高。若股价因解禁恐慌下跌至8.2-8.5元区间（接近定增成本线），
可考虑逢低吸纳。
<span style="color:#22c55e;">【中期：中性偏多】</span>
公司盐化工+储能双轮驱动逻辑清晰，盐穴储能赛道长坡厚雪，解禁压力消化后仍有配置价值。
建议关注持仓中盐化工相关标的的联动效应，如<b>雪天盐业、云南盐化</b>等。</p>
</div>

<div style="height: 20px;"></div>

<h3 style="color: #f1f5f9; font-size: 16px; margin-bottom: 14px; border-left: 3px solid #8b5cf6; padding-left: 10px;">
事件三：英伟达Q2财报前瞻 —— AI产业链的季度大考
</h3>
<div style="font-size: 13px; color: #cbd5e1; line-height: 1.8;">
<p><b>【事件时间】</b>8月26日（周三）美股盘后公布，约北京时间27日凌晨5点财报电话会。</p>

<p><b>【市场预期】</b>华尔街一致预期Q2营收<b>920亿美元</b>（同比+96%，环比加速），
调整后EPS <b>2.09美元</b>。数据中心业务预计突破854亿美元（同比+107%），
其中超大规模云厂商板块435亿、ACIE板块417亿。毛利率预期维持在74.9%-75%区间。</p>

<p><b>【核心观察点】</b></p>
<ol style="margin: 8px 0; padding-left: 20px;">
<li><b>Q3营收指引：</b>大摩预计1023亿美元（环比+12%），关键看管理层指引是否超预期</li>
<li><b>毛利率走势：</b>受HBM成本上升影响，70%中段毛利率目标能否维持是核心关切</li>
<li><b>Blackwell Ultra交付进度：</b>下一代产品路线图，决定2027年增长确定性</li>
<li><b>ACIE业务增速：</b>AI企业/工业市场是否接棒超大规模云厂商成为新增长极</li>
<li><b>涨价影响解读：</b>彭博报道新一代AI服务器涨价15%+，管理层如何回应成本传导能力</li>
</ol>

<p><b>【A股影响分析】</b>
英伟达财报是全球AI产业链的"体检报告"，直接影响A股科技股风险偏好：</p>
<ul style="margin: 8px 0; padding-left: 20px;">
<li><b>光模块：</b>中际旭创、新易盛、天孚通信等，业绩与英伟达资本开支高度绑定</li>
<li><b>算力/液冷：</b>英维克、工业富联、浪潮信息等，AI服务器需求直接受益</li>
<li><b>半导体设备/先进封装：</b>雅克科技、北方华创、长川科技等，产业链景气度传导</li>
<li><b>存储/HBM：</b>铜冠铜箔、佰维存储、德明利等，AI存储需求验证</li>
</ul>

<p><b>【操作建议】</b>
<span style="color:#fbbf24;">【短期：谨慎乐观，提防"利好出尽"】</span>
过去4个季度英伟达均超预期但次日股价平均下跌超5%，市场已形成"财报日即顶"的惯性思维。
本次市场预期极高（920亿营收/2.09 EPS已是非常乐观的预期），如果只是"符合预期"可能引发获利回吐。
建议持仓科技股的投资者<b>在财报前适当降低仓位至60-70%</b>，待财报落地后根据指引再决定是否加仓。
若财报指引超预期（Q3指引＞1000亿+毛利率维持75%），则AI科技股有望开启新一轮上涨；
若指引不及预期，科技股可能面临10-15%的回调压力。
<span style="color:#60a5fa;">【持仓相关：英维克/铜冠铜箔/雅克科技均受影响】</span></p>
</div>

<div style="height: 20px;"></div>

<h3 style="color: #f1f5f9; font-size: 16px; margin-bottom: 14px; border-left: 3px solid #10b981; padding-left: 10px;">
事件四：半年报密集披露期 —— 半导体/光模块业绩验证
</h3>
<div style="font-size: 13px; color: #cbd5e1; line-height: 1.8;">
<p>8月下旬进入A股半年报披露高峰期，8月25日预计有约200家公司披露中报。
其中多个重磅标的值得重点关注：</p>

<p><b>【半导体板块】</b></p>
<ul style="margin: 8px 0; padding-left: 20px;">
<li><b>士兰微（600460）：</b>上半年净利润5.16亿元，同比+94.84%，Q2环比+47%。IDM模式受益于半导体景气上行，功率半导体+特色工艺双线增长。</li>
<li><b>华润微（688396）：</b>上半年净利润7.22亿元，同比+113.23%，拟每10股派0.56元。产能利用率接近满载，产品价格上调。</li>
<li><b>道通科技（688208）：</b>上半年净利润4.34亿元，同比-9.73%，汽车诊断设备出口承压。</li>
</ul>

<p><b>【锂电/有色板块】</b></p>
<ul style="margin: 8px 0; padding-left: 20px;">
<li><b>中矿资源（002738）：</b>上半年净利润11.11亿元，同比+1146.81%！Q2环比+18%。锂盐价格大幅反弹驱动业绩暴增，锂电产业链景气度验证。</li>
</ul>

<p><b>【光通信板块】</b></p>
<ul style="margin: 8px 0; padding-left: 20px;">
<li><b>长飞光纤（600487）：</b>上半年净利润29.25亿元，同比+888.88%，拟每10股派10.6元。光纤光缆量价齐升，AI算力基础设施需求旺盛。</li>
</ul>

<p><b>【投资建议】</b>
半年报密集期是"验金石"，业绩超预期的标的将获得资金青睐，业绩不及预期的可能加速下跌。
建议重点关注持仓相关的<b>英维克（液冷）、铜冠铜箔（存储/锂电铜箔）、雅克科技（半导体材料）</b>
的半年报发布时间，提前做好仓位管理。从已披露数据看，半导体设备/材料、光通信、锂矿板块业绩亮眼，
可重点挖掘超预期个股机会。</p>
</div>

<div style="height: 20px;"></div>

<h3 style="color: #f1f5f9; font-size: 16px; margin-bottom: 14px; border-left: 3px solid #3b82f6; padding-left: 10px;">
事件五：MLF到期6000亿 —— 观察货币政策走向的窗口
</h3>
<div style="font-size: 13px; color: #cbd5e1; line-height: 1.8;">
<p><b>【事件概况】</b>8月25日有<b>6000亿元</b>1年期MLF到期，央行续做操作是观察货币政策立场的重要窗口。</p>

<p><b>【背景分析】</b>
当前经济处于复苏进程中，7月经济数据整体稳中向好，但外需压力、地产修复斜率、消费后劲仍存不确定性。
8月LPR报价维持不变（1年期3.35%，5年期3.75%），央行政策处于观察期。
美国7月PCE即将公布+杰克逊霍尔年会在即，全球货币政策不确定性上升，中国央行大概率维持稳健基调。</p>

<p><b>【预期判断】</b>
<span style="color:#22c55e;">大概率：等量续做，利率不变</span>——6000亿全额续做，操作利率维持2.30%不变，符合市场预期，对市场影响中性。
<span style="color:#fbbf24;">小概率：小幅加量续做</span>——如续做7000-8000亿，释放宽松信号，利好银行、地产、成长股。
<span style="color:#f87171;">极小概率：缩量续做</span>——若缩量至5000亿以下，可能引发流动性收紧担忧。</p>

<p><b>【市场影响】</b>MLF操作影响银行中长期资金成本，进而影响LPR报价和市场流动性预期。
若维持中性操作，A股市场流动性环境保持平稳，对科技成长股友好；若超预期宽松，
银行、地产、券商等利率敏感板块可能获得短期脉冲。整体而言，当前货币政策对A股的影响偏正面。</p>
</div>
"""
gen.add_impact_analysis(deep_analysis)

# ========== 8. 催化深度分析Skill增强模块 ==========
deep_events = [
    {
        'title': '十四届全国人大常委会第二十四次会议',
        'type': 'policy',
        'description': '审议医保法、银行监管法等10部法律草案及经济运行报告，政策信号密集释放',
        'category': '国家级会议·政策催化'
    },
    {
        'title': '英伟达Q2财报',
        'type': 'earnings',
        'description': 'AI产业链季度大考，预计营收920亿+96%，指引决定科技股方向',
        'category': '海外重磅·AI产业链'
    },
    {
        'title': '杰克逊霍尔全球央行年会',
        'type': 'meeting',
        'description': '美联储主席沃什首次亮相，全球货币政策走向关键信号',
        'category': '全球央行·利率政策'
    },
]
gen.add_catalyst_deep_analysis(deep_events)

# ========== 9. 风险提示 ==========
risks = [
    "英伟达财报不及预期或指引偏弱，可能引发全球科技股回调，影响A股算力/半导体/存储板块",
    "美伊对峙持续升级，霍尔木兹海峡封锁风险加剧，油价暴涨推高通胀并压制风险偏好",
    "苏盐井神等大额解禁股抛压超预期，引发相关板块情绪传导",
    "全国人大常委会相关法律审议结果不及预期，政策催化落空",
    "MLF操作低于市场预期，流动性收紧担忧引发市场波动",
    "杰克逊霍尔年会上美联储释放超预期鹰派信号，美元走强压制人民币资产",
    "半年报密集披露期业绩雷风险，高位股业绩不及预期可能大幅回调"
]
gen.add_risk_warning(risks)

# ========== 发布 ==========
print("开始生成并发布明日催化剂报告...")
result = gen.publish(
    title="明日催化剂",
    excerpt="十四届全国人大常委会第二十四次会议开幕，审议10部法律草案及经济运行报告；苏盐井神1.64亿股解禁（市值14.7亿/占比17.14%）；第二十六届投洽会新闻发布会；6000亿MLF到期；英伟达Q2财报前瞻（8.26盘后）；杰克逊霍尔年会前瞻"
)

print(f"\n发布结果: {result['success']}")
print(f"文件路径: {result['filepath']}")
print(f"列表页更新: {result['list_updated']}")
print(f"校验: {result['validated']}")
print(f"部署: {result['deployed']}")
if result['errors']:
    print(f"错误: {result['errors']}")
