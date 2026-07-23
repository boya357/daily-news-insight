#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
2026年7月23日（周四）明日催化剂报告生成脚本
V3.0 生成器 - TomorrowCatalystGenerator
"""
import sys
import os

os.chdir('/root/daily-news-insight')
sys.path.insert(0, 'v3')

from v3.generators.tomorrow_catalyst import TomorrowCatalystGenerator

# ==================== 初始化生成器 ====================
gen = TomorrowCatalystGenerator(
    date_str="20260723",
    subtitle="2026.07.23 · 周四明日催化剂"
)

# ==================== 1. 明日核心催化 ====================
core_catalyst_html = """
<div style="line-height: 1.9; color: #e2e8f0; font-size: 14px;">
    <p style="margin: 0 0 12px 0;">
        <strong style="color: #fbbf24;">【核心看点】</strong>
        明日（7月23日周四）市场将迎来多重重磅事件交织：
        <strong>AMD Advancing AI大会进入第二天</strong>，苏姿丰主题演讲定于北京时间7月24日凌晨揭幕，市场高度关注MI455X GPU与Helios机架系统路线图；
        <strong>欧洲央行利率决议</strong>将于晚间20:15公布，全球流动性预期面临考验；
        <strong>英特尔Q2财报</strong>盘后发布，数据中心CPU与代工业务进展是核心变量。
        国内方面，<strong>低空经济博览会进入专业观众日第二天</strong>，多场重磅论坛与签约活动集中上演；
        <strong>中报业绩预告进入密集披露窗口</strong>，源杰科技、协创数据等算力产业链标的业绩大幅预增。
    </p>
    <p style="margin: 0 0 12px 0;">
        <strong style="color: #34d399;">【机会主线】</strong>
        优先关注三条确定性较高的主线：① <strong>AI算力硬件</strong>（光模块/PCB/先进封装）——AMD大会超预期+英特尔财报验证需求复苏双重催化；
        ② <strong>低空经济</strong>（eVTOL整机/核心配套/低空基建）——博览会持续发酵+订单签约催化；
        ③ <strong>中报高增长标的</strong>（存储/半导体设备/算力链）——业绩确定性溢价阶段。
    </p>
    <p style="margin: 0;">
        <strong style="color: #f87171;">【风险预警】</strong>
        明日解禁总市值约百亿元，其中<strong>山大电力解禁占比达47.39%</strong>需重点警惕；
        欧洲央行若释放鹰派信号可能压制全球风险偏好；
        中报季业绩雷风险集中释放，规避高位纯题材标的。
    </p>
</div>
"""
gen.add_key_catalyst(core_catalyst_html)

# ==================== 2. 明日事件日历 ====================
events_list = [
    # AI算力
    {
        'type': 'meeting',
        'title': 'AMD Advancing AI大会·第二天（旧金山）',
        'description': '大会进入第二天，苏姿丰CEO主题演讲定于美西时间7月23日上午（北京时间7月24日凌晨00:30），重点披露MI455X GPU、Helios机架系统、Zen6架构路线图，以及与微软Azure的深度合作进展。A股光模块、PCB、先进封装产业链或受情绪带动。',
        'category': '海外科技会议'
    },
    {
        'type': 'earnings',
        'title': '英特尔发布2026年Q2财报（美股盘后）',
        'description': '市场预期营收144.5亿美元（同比+12.37%），EPS 0.08美元（同比扭亏）。核心看点：数据中心服务器CPU出货量与定价、18A制程良率进展、代工业务外部客户拓展、PC业务下滑幅度。期权市场隐含波动±15.21%。',
        'category': '海外财报'
    },
    # 央行政务
    {
        'type': 'policy',
        'title': '欧洲央行公布利率决议',
        'description': '公布时间7月23日20:15（北京时间），市场普遍预期存款利率维持2.25%不变。关注拉加德新闻发布会（20:45）的政策指引措辞——偏鸽将利好全球风险资产，偏鹰则压制成长股估值。',
        'category': '海外央行'
    },
    # 国内产业
    {
        'type': 'meeting',
        'title': '2026国际低空经济博览会·专业观众日第二天',
        'description': '展期7月22-25日，今日4场专题论坛集中举办，涵盖低空基础设施、安全保障、应用场景等主题，主办方将联合发布《智慧城市低空基础设施建设》主题报告。eVTOL整机、低空安防、无人机产业链持续受关注。',
        'category': '产业展会'
    },
    {
        'type': 'meeting',
        'title': '上海核能可持续发展大会·第二天',
        'description': '7月22-24日在上海国家会展中心举办，聚焦小型堆、四代核电、核能综合利用等议题。核电产业链（中国核电、中国核建、上海电气等）迎来事件性催化。',
        'category': '产业展会'
    },
    # 数据发布
    {
        'type': 'data',
        'title': '美国当周初请失业金人数',
        'description': '公布时间20:30（北京时间），市场预期21.1万人。作为劳动力市场高频指标，数据超预期上行将强化美联储降息预期，利好成长股；反之则可能引发紧缩担忧。',
        'category': '海外经济数据'
    },
    # 限售股解禁
    {
        'type': 'general',
        'title': '11家公司限售股解禁',
        'description': '山大电力（301609）解禁占比47.39%（市值约22.3亿元）居首，其他包括新睿电子、技源集团、富岭股份、新锦动力、银禧科技、宸展光电、德明利、生益科技、大洋生物、水晶光电。重点警惕高占比+高估值小票解禁抛压。',
        'category': '限售股解禁'
    },
    # 航天
    {
        'type': 'general',
        'title': '长征三号乙运载火箭西昌发射',
        'description': '预计7月23日20:00左右从西昌卫星发射中心发射，执行GTO轨道发射任务。商业航天板块（中国卫通、天银机电、航天电子等）或受事件情绪带动。',
        'category': '商业航天'
    },
]

gen.add_events_calendar(events_list)

# ==================== 3. 业绩公告 ====================
earnings_stocks = [
    {
        'name': '源杰科技',
        'code': '688498',
        'type': '半年报预增',
        'growth': '+1197% ~ +1305%',
    },
    {
        'name': '协创数据',
        'code': '300857',
        'type': '半年报预增',
        'growth': '+247% ~ +340%',
    },
    {
        'name': '兆易创新',
        'code': '603986',
        'type': '项目增资',
        'growth': 'DRAM+5亿元',
    },
    {
        'name': '佰维存储',
        'code': '688525',
        'type': '回购提议',
        'growth': '2~2.5亿注销',
    },
    {
        'name': '顺丰控股',
        'code': '002352',
        'type': '回购进展',
        'growth': '60亿元完成',
    },
    {
        'name': '阳光电源',
        'code': '300274',
        'type': '回购提议',
        'growth': '5~10亿元',
    },
]

gen.add_earnings_announcements(earnings_stocks)

# ==================== 4. 重要数据发布 ====================
data_list = [
    {
        'name': '欧洲央行利率决议',
        'prev': '2.25%',
        'expect': '2.25%（维持）',
        'actual': '待公布'
    },
    {
        'name': '美国初请失业金人数',
        'prev': '—',
        'expect': '21.1万人',
        'actual': '待公布'
    },
    {
        'name': '英特尔Q2财报',
        'prev': '营收136亿',
        'expect': '营收144.5亿',
        'actual': '盘后发布'
    },
]

gen.add_data_release(data_list)

# ==================== 5. 重点事件影响深度分析与操作建议 ====================
deep_analysis_html = """
<div style="line-height: 1.9; color: #e2e8f0; font-size: 14px;">
    
    <h3 style="color: #fbbf24; font-size: 16px; margin: 0 0 10px 0; border-left: 3px solid #fbbf24; padding-left: 10px;">
        一、AMD Advancing AI大会 & 英特尔财报：AI算力赛道的双重考验
    </h3>
    <p style="margin: 0 0 12px 0;">
        明日（准确说是7月24日凌晨）AI算力赛道将迎来"双重考验"：AMD大会苏姿丰主题演讲揭幕，以及英特尔Q2财报发布。
        <strong style="color: #34d399;">利好逻辑：</strong>
        若AMD披露MI455X GPU采用HBM4高带宽内存、FP8低精度算力参数超预期，或宣布Helios机架系统量产时间表提前，
        将直接带动A股光模块（中际旭创、新易盛、光迅科技）、AI服务器PCB（胜宏科技、沪电股份）、先进封装（长电科技、通富微电）情绪补涨。
        英特尔方面，若数据中心CPU营收增速与订单能见度超预期，将验证"AI推理时代CPU需求结构性增长"逻辑，利好国产CPU产业链。
    </p>
    <p style="margin: 0 0 14px 0;">
        <strong style="color: #f87171;">风险点：</strong>
        当前市场对AI板块预期已降至阶段低位，若AMD仅侧重路线图展望、缺少具体出货指引，或英特尔PC业务下滑超预期，
        可能引发"预期兑现"后的短期抛压。<strong>操作建议：</strong>
        持仓标的（英维克、雅克科技）设好止损位，不建议在大会前追高加仓；
        光模块/存储方向若盘中出现急跌5%以上可考虑低吸博弈超预期，但仓位控制在20%以内。
        重点关注<strong>英维克</strong>——液冷作为AI算力基础设施刚需，AMD/MI系列GPU功率密度提升直接利好液冷渗透率，若大会超预期有望带动估值修复。
    </p>
    
    <h3 style="color: #fbbf24; font-size: 16px; margin: 0 0 10px 0; border-left: 3px solid #fbbf24; padding-left: 10px;">
        二、低空经济博览会持续发酵：从概念展示到订单落地的关键观察窗口
    </h3>
    <p style="margin: 0 0 12px 0;">
        2026国际低空经济博览会已于7月22日开幕，展期至7月25日。本届博览会展出面积6万平方米、452家企业参展、65项首发成果（全球首发23项），
        规模和能级全面升级。<strong>7月23日作为专业观众日第二天，是产业签约与论坛集中爆发的节点</strong>，
        主办方将联合发布《智慧城市低空基础设施建设》主题报告，4场专题论坛覆盖基础支撑、安全保障、应用场景等核心议题。
    </p>
    <p style="margin: 0 0 14px 0;">
        <strong style="color: #34d399;">影响分析（偏利好）：</strong>
        低空经济已纳入"十五五"规划、新《民用航空法》已落地，本届展会是政策落地后的首场行业盛会，
        核心看点不在概念展示，而在<strong>适航证推进、物流/载人场景实质性订单签约</strong>。
        若展会期间出现重大订单签约或适航证进展公告，相关标的有望迎来情绪驱动行情。
        关注标的：<strong>铜冠铜箔</strong>（储能+低空轻量化材料双逻辑）、
        中信海直（低空运营）、万丰奥威（通航飞机）、华测导航（低空导航）、宗申动力（航空发动机）。
        持仓标的<strong>铜冠铜箔</strong>需关注HVLP超薄铜箔在低空飞行器线束、PCB中的应用增量。
    </p>
    <p style="margin: 0 0 14px 0;">
        <strong style="color: #f87171;">风险提示：</strong>
        7月22日开幕日已是情绪高点，明日需警惕"利好兑现高开低走"风险，尤其是纯概念、无业绩支撑的小票。
        操作上建议优先选择有基本面支撑、估值合理的产业链中游标的，规避高位连板情绪股。
    </p>
    
    <h3 style="color: #fbbf24; font-size: 16px; margin: 0 0 10px 0; border-left: 3px solid #fbbf24; padding-left: 10px;">
        三、欧洲央行利率决议：全球流动性的关键信号
    </h3>
    <p style="margin: 0 0 12px 0;">
        欧洲央行将于北京时间7月23日20:15公布最新利率决议，市场普遍预期存款利率维持2.25%不变。
        这是6月加息25个基点后的首次会议，政策声明措辞和拉加德新闻发布会的指引更为关键。
    </p>
    <p style="margin: 0 0 14px 0;">
        <strong>三种情景推演：</strong>
        <br>
        ① <strong style="color: #34d399;">中性偏鸽（基准情景，概率约60%）：</strong>
        维持利率不变，声明保留"数据依赖"和"逐次会议决策"措辞，拉加德强调通胀回落但经济下行风险加大。
        影响：欧元小幅走弱，全球风险资产情绪平稳，A股北向资金维持小幅净流入。
        <br>
        ② <strong style="color: #fbbf24;">鹰派信号（概率约30%）：</strong>
        维持利率不变但声明增加"通胀仍面临上行风险"，拉加德强调不排除进一步加息。
        影响：欧元走强，美元指数走弱但全球股债承压，北向资金可能阶段性流出，成长股估值面临压制。
        <br>
        ③ <strong style="color: #34d399;">鸽派转向（小概率，约10%）：</strong>
        删除"限制性利率"相关表述，暗示降息窗口临近。
        影响：全球风险资产普涨，成长股弹性最大，北向资金大幅流入。
    </p>
    <p style="margin: 0 0 14px 0;">
        <strong>操作建议：</strong>
        晚间决议前降低杠杆仓位，观望为主；若决议偏鸽，可适度加仓高弹性的科技成长方向；
        若偏鹰，短期转向防御（电力、高股息、贵金属）。整体上决议对A股的影响属于情绪层面，不改变中期趋势。
    </p>
    
    <h3 style="color: #fbbf24; font-size: 16px; margin: 0 0 10px 0; border-left: 3px solid #fbbf24; padding-left: 10px;">
        四、中报业绩预告密集期：业绩为王，分化加剧
    </h3>
    <p style="margin: 0 0 12px 0;">
        当前处于中报业绩预告的密集披露窗口（深市创业板/科创板强制披露截止日前），
        盘后已披露的多家算力产业链公司业绩大幅超预期：
        <strong>源杰科技</strong>上半年净利预增1197%-1305%（光芯片量价齐升），
        <strong>协创数据</strong>上半年净利预增247%-340%（AI服务器+存储设备放量）。
        同时，一批公司披露回购/增持计划：佰维存储（2-2.5亿回购注销）、阳光电源（5-10亿回购）、三环集团（9亿回购）、顺丰控股（60亿回购完成）。
    </p>
    <p style="margin: 0 0 14px 0;">
        <strong style="color: #34d399;">影响判断（结构性利好）：</strong>
        回购增持潮+业绩预增集中释放，说明产业资本对当前估值认可度提升，科技成长赛道的基本面底正在夯实。
        持仓标的<strong>雅克科技</strong>（半导体材料）和<strong>铜冠铜箔</strong>（锂电铜箔+电子铜箔）
        需重点关注中报业绩预告披露节奏，若业绩超预期有望触发估值修复。
        <strong>*ST建艺</strong>需警惕中报业绩风险，严格执行止损纪律。
    </p>
    
    <h3 style="color: #fbbf24; font-size: 16px; margin: 0 0 10px 0; border-left: 3px solid #fbbf24; padding-left: 10px;">
        五、限售股解禁风险提示：山大电力占比近五成需重点警惕
    </h3>
    <p style="margin: 0 0 14px 0;">
        明日共11家公司限售股解禁，其中<strong>山大电力（301609.SZ）</strong>解禁数量最大、风险最高：
        解禁7718.72万股，占总股本<strong style="color: #f87171;">47.39%</strong>，
        解禁市值约22.3亿元（按7月21日收盘价34.89元计算）。
        解禁性质为首发原股东限售股份，涉及21名股东（含多位核心技术人员、董事长等），实际可流通股份约6151.77万股。
        公司一季度净利润同比下降16.16%，市盈率TTM 42倍高于行业均值28倍，估值偏高+高解禁比例叠加，
        <strong style="color: #f87171;">短期抛压风险较大，建议规避</strong>。
        其他解禁标的中，生益科技、水晶光电等大盘股解禁比例较低，影响相对有限。
    </p>
    
    <h3 style="color: #fbbf24; font-size: 16px; margin: 0 0 10px 0; border-left: 3px solid #fbbf24; padding-left: 10px;">
        六、持仓个股操作建议（针对boya持仓4股）
    </h3>
    <p style="margin: 0 0 8px 0;">
        <strong style="color: #93c5fd;">1. 英维克（002837）</strong>：
        液冷+AI算力基础设施核心标的。明日AMD大会若披露高功率GPU路线图，液冷需求逻辑进一步强化。
        操作建议：持有为主，若盘中回踩20日线可适当加仓；止损位设在前期低点下方5%。
    </p>
    <p style="margin: 0 0 8px 0;">
        <strong style="color: #93c5fd;">2. 铜冠铜箔（301217）</strong>：
        锂电铜箔+HVLP电子铜箔双赛道，低空经济+AI服务器PCB双重催化。
        操作建议：低空博览会持续发酵有望带动情绪，中报业绩预告是下一个关键催化，持有观察。
    </p>
    <p style="margin: 0 0 8px 0;">
        <strong style="color: #93c5fd;">3. 雅克科技（002409）</strong>：
        半导体材料平台型公司，存储产业链上游核心标的。英特尔/AMD消息面持续催化，
        中报业绩预告若超预期有望加速估值修复。操作建议：持有，关注中报披露节奏。
    </p>
    <p style="margin: 0 0 14px 0;">
        <strong style="color: #f87171;">4. *ST建艺（002789）</strong>：
        中报季ST股业绩风险集中，需高度警惕。操作建议：严格执行止损纪律，
        若跌破支撑位果断减仓，不做博弈。
    </p>
</div>
"""

# 自定义Section来放深度分析
from v3.components.layout import Section
deep_analysis_section = Section(
    title="🎯 重点事件深度分析与操作建议",
    content=deep_analysis_html,
    icon="target",
    variant="highlight"
)
gen._components.append(deep_analysis_section)

# ==================== 6. 催化深度分析（Skill增强：三维热度+SWOT+情景推演） ====================
skill_events = [
    {
        'title': 'AMD Advancing AI大会·苏姿丰主题演讲',
        'type': 'meeting',
        'description': '7月24日凌晨00:30，苏姿丰CEO发表主题演讲，披露MI455X GPU、Helios机架、Zen6架构及与微软Azure合作进展，AI算力产业链核心催化事件。',
        'category': '海外科技会议 | AI算力'
    },
    {
        'title': '欧洲央行7月利率决议',
        'type': 'policy',
        'description': '7月23日20:15公布利率决议，市场预期维持2.25%不变，拉加德新闻发布会指引将影响全球流动性预期与风险偏好。',
        'category': '海外央行 | 宏观政策'
    },
    {
        'title': '英特尔Q2财报·数据中心与代工业务验证',
        'type': 'earnings',
        'description': '7月23日美股盘后发布Q2财报，数据中心CPU需求复苏、18A制程良率、代工业务亏损收窄是核心看点，期权隐含波动±15%。',
        'category': '海外财报 | 半导体'
    },
]

gen.add_catalyst_deep_analysis(skill_events)

# ==================== 7. 本周事件日历表格 ====================
week_calendar_html = """
<div style="overflow-x: auto;">
    <table style="width: 100%; border-collapse: collapse; font-size: 13px; color: #e2e8f0;">
        <thead>
            <tr style="background: linear-gradient(135deg, rgba(251,191,36,0.15), rgba(239,68,68,0.1)); border-bottom: 1px solid rgba(255,255,255,0.1);">
                <th style="padding: 10px 12px; text-align: left; font-weight: 600; color: #fbbf24;">日期</th>
                <th style="padding: 10px 12px; text-align: left; font-weight: 600; color: #fbbf24;">事件名称</th>
                <th style="padding: 10px 12px; text-align: left; font-weight: 600; color: #fbbf24;">类型</th>
                <th style="padding: 10px 12px; text-align: left; font-weight: 600; color: #fbbf24;">影响板块/标的</th>
                <th style="padding: 10px 12px; text-align: center; font-weight: 600; color: #fbbf24;">重要性</th>
            </tr>
        </thead>
        <tbody>
            <tr style="border-bottom: 1px solid rgba(255,255,255,0.05);">
                <td style="padding: 10px 12px; white-space: nowrap;">7月22日（周三）</td>
                <td style="padding: 10px 12px;">低空经济博览会开幕 / AMD大会第一天 / 核能大会开幕</td>
                <td style="padding: 10px 12px;"><span style="background: rgba(139,92,246,0.2); color: #c4b5fd; padding: 2px 8px; border-radius: 4px; font-size: 11px;">产业展会</span></td>
                <td style="padding: 10px 12px;">低空经济、AI算力、核电</td>
                <td style="padding: 10px 12px; text-align: center;"><span style="color: #f87171;">★★★★★</span></td>
            </tr>
            <tr style="border-bottom: 1px solid rgba(255,255,255,0.05); background: rgba(251,191,36,0.03);">
                <td style="padding: 10px 12px; white-space: nowrap; font-weight: 600; color: #fbbf24;">7月23日（周四）·明日</td>
                <td style="padding: 10px 12px;">欧洲央行利率决议 / 英特尔Q2财报 / AMD大会第二天 / 长三乙发射 / 11股解禁</td>
                <td style="padding: 10px 12px;"><span style="background: rgba(239,68,68,0.2); color: #fca5a5; padding: 2px 8px; border-radius: 4px; font-size: 11px;">重磅</span></td>
                <td style="padding: 10px 12px;">AI算力、半导体、全球流动性、商业航天</td>
                <td style="padding: 10px 12px; text-align: center;"><span style="color: #f87171;">★★★★★</span></td>
            </tr>
            <tr style="border-bottom: 1px solid rgba(255,255,255,0.05);">
                <td style="padding: 10px 12px; white-space: nowrap;">7月24日（周五）</td>
                <td style="padding: 10px 12px;">AMD大会苏姿丰演讲落地 / 欧元区7月PMI初值 / 美国7月PMI初值 / 日本6月CPI</td>
                <td style="padding: 10px 12px;"><span style="background: rgba(59,130,246,0.2); color: #93c5fd; padding: 2px 8px; border-radius: 4px; font-size: 11px;">数据发布</span></td>
                <td style="padding: 10px 12px;">AI算力、全球宏观、新能源</td>
                <td style="padding: 10px 12px; text-align: center;"><span style="color: #fbbf24;">★★★★☆</span></td>
            </tr>
            <tr style="border-bottom: 1px solid rgba(255,255,255,0.05);">
                <td style="padding: 10px 12px; white-space: nowrap;">7月24日（周五）</td>
                <td style="padding: 10px 12px;">新股申购：津富士达、嘉立创</td>
                <td style="padding: 10px 12px;"><span style="background: rgba(16,185,129,0.2); color: #6ee7b7; padding: 2px 8px; border-radius: 4px; font-size: 11px;">新股申购</span></td>
                <td style="padding: 10px 12px;">新股</td>
                <td style="padding: 10px 12px; text-align: center;"><span style="color: #6ee7b7;">★★☆☆☆</span></td>
            </tr>
            <tr style="border-bottom: 1px solid rgba(255,255,255,0.05);">
                <td style="padding: 10px 12px; white-space: nowrap;">7月25日（周六）</td>
                <td style="padding: 10px 12px;">低空经济博览会闭幕（公众日第二天）</td>
                <td style="padding: 10px 12px;"><span style="background: rgba(107,114,128,0.2); color: #9ca3af; padding: 2px 8px; border-radius: 4px; font-size: 11px;">展会闭幕</span></td>
                <td style="padding: 10px 12px;">低空经济</td>
                <td style="padding: 10px 12px; text-align: center;"><span style="color: #9ca3af;">★★☆☆☆</span></td>
            </tr>
            <tr>
                <td style="padding: 10px 12px; white-space: nowrap;">7月28日（周二）</td>
                <td style="padding: 10px 12px;">纳米材料器件创新大会 / 美联储FOMC会议前静默期</td>
                <td style="padding: 10px 12px;"><span style="background: rgba(139,92,246,0.2); color: #c4b5fd; padding: 2px 8px; border-radius: 4px; font-size: 11px;">产业会议</span></td>
                <td style="padding: 10px 12px;">半导体材料、科技</td>
                <td style="padding: 10px 12px; text-align: center;"><span style="color: #fbbf24;">★★★☆☆</span></td>
            </tr>
        </tbody>
    </table>
</div>
<p style="font-size: 12px; color: #64748b; margin-top: 10px; text-align: right;">数据来源：财联社、上证报、东方财富、公开信息整理</p>
"""

week_calendar_section = Section(
    title="📆 本周事件日历总览",
    content=week_calendar_html,
    icon="calendar",
    variant="dark"
)
# 插入到事件日历之后（第3个位置，索引2）
gen._components.insert(2, week_calendar_section)

# ==================== 8. 风险提示 ====================
risks = [
    "欧洲央行利率决议超预期鹰派，引发全球流动性收紧预期",
    "AMD大会低于预期，AI算力板块短期情绪退潮",
    "中报业绩雷集中释放，高位纯题材股大幅回调",
    "山大电力等高比例解禁标的抛压扩散，冲击次新情绪",
    "地缘政治局势升级，全球避险情绪升温",
    "低空经济博览会利好兑现，相关标的高开低走"
]

gen.add_risk_warning(risks)

# ==================== 发布 ====================
print("正在生成报告...")
html = gen.generate()
print(f"HTML总长度: {len(html)} 字符")

# 保存并发布
result = gen.publish(
    title="明日催化剂",
    report_type="tomorrow_catalyst",
    filename="20260723_明日催化剂.html",
    excerpt="7月23日周四多重重磅事件：AMD大会+英特尔财报双催化AI算力，欧洲央行利率决议考验全球流动性，低空经济博览会持续发酵，中报业绩密集披露。8大具体事件+深度分析+持仓操作建议全收录。",
    auto_deploy=False,
    docs_root="/root/daily-news-insight/docs"
)

print(f"发布结果: {result}")
print(f"文件路径: {result.get('filepath')}")
print(f"列表页更新: {result.get('list_updated')}")
