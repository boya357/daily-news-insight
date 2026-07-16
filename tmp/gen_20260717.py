#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
明日催化剂 - 2026年7月17日（星期五）
"""
import sys, os
sys.path.insert(0, '/root/daily-news-insight')
os.chdir('/root/daily-news-insight')

from v3.generators.tomorrow_catalyst import TomorrowCatalystGenerator
from components.layout import Section

gen = TomorrowCatalystGenerator(
    date_str="20260717",
    subtitle="2026.07.17 · 明日催化剂 · WAIC2026开幕日"
)

# 1. 核心催化
gen.add_key_catalyst("""
<b>核心催化一</b>：2026世界人工智能大会（WAIC 2026）7月17日上午在上海开幕，国家主席习近平出席开幕式并发表主旨讲话，系统阐述中国AI发展与治理主张。1100余家企业参展，300余款产品全球首发，智算与具身智能两大赛道各汇聚超200家企业，AI算力与人形机器人产业链迎来最高级别政策催化。
<br><br>
<b>核心催化二</b>：长鑫科技（688825）IPO配号与中签率公布（T+1日），579亿元募资成科创板史上第二大IPO，DRAM国产替代独苗正式登陆资本市场，存储板块情绪有望共振。
<br><br>
<b>核心催化三</b>：国家外汇管理局上午10时举行新闻发布会，介绍2026年上半年外汇收支数据情况，人民币汇率与跨境资本流动走向是市场关注焦点。
""")

# 2. 事件日历
events = [
    {'type': 'meeting', 'title': 'WAIC 2026世界人工智能大会开幕 · 习近平出席并讲话',
     'description': '7月17-20日上海举行，主题"智能伙伴、共创未来"。习主席出席开幕式发表主旨讲话，系统阐述中国AI发展政策与治理主张。1100+企业参展，300余款全球首发。',
     'category': 'AI大会·S级'},
    {'type': 'meeting', 'title': '成都先进制造业新产品新技术发布会',
     'description': '7月17日"智造蓉城·焕新突破"主题活动，20家企业发布38项前沿新技术新产品，首创大模型平台系统数字化评估机制。APEC数字周配套活动。',
     'category': '产业发布'},
    {'type': 'data', 'title': '国新办：上半年外汇收支数据发布会',
     'description': '7月17日上午10时，外汇局副局长李斌介绍2026年上半年外汇收支数据并答记者问。关注人民币汇率走势与跨境资本流动。',
     'category': '宏观数据'},
    {'type': 'data', 'title': '美国7月密歇根大学消费者信心初值',
     'description': '7月17日21:00公布，前值49.5，预期51.0；通胀预期前值4.6%。消费者信心与通胀预期直接影响美联储降息节奏判断。',
     'category': '海外数据'},
    {'type': 'earnings', 'title': '长鑫科技IPO配号及中签率公布',
     'description': '长鑫科技（688825）T+1日公布配号结果与中签率。发行价8.66元，募资579亿元，科创板史上第二大IPO。国内唯一DRAM规模化量产IDM龙头。',
     'category': 'IPO里程碑'},
    {'type': 'policy', 'title': '安徽省上半年外贸情况新闻发布会',
     'description': '7月17日上午10:30，合肥海关发布安徽省2026年上半年外贸进出口数据。',
     'category': '区域经济'},
    {'type': 'general', 'title': '青岛食品/印象股份/银龙股份限售股解禁',
     'description': '青岛食品(001219)解禁9.48万股占比0.049%；印象股份解禁43.42万股占比0.40%；银龙股份(603969)解禁194.7万股占比0.22%（股权激励）。',
     'category': '限售解禁'},
    {'type': 'meeting', 'title': 'APEC数字周·成都人工智能+行动方案发布会',
     'description': '7月22日，成都市多部门联合发布《深入实施"人工智能+"行动方案》，解读算力数据支撑、AI+医疗、AI+消费等细分领域政策。',
     'category': '地方政策'},
    {'type': 'meeting', 'title': '三星第八代折叠屏手机全球发布会',
     'description': '7月22日伦敦发布，首发Flex Titanium钛金属折叠屏技术，第八代Galaxy折叠设备亮相。',
     'category': '消费电子'},
    {'type': 'earnings', 'title': '长鑫科技中签结果公布（T+2）',
     'description': '7月20日（下周一）公布中签结果并完成缴款。中一签需缴款4330元。',
     'category': 'IPO里程碑'},
]
gen.add_events_calendar(events)

# 3. 业绩公告
gen.add_earnings_announcements([
    {'name': '海光信息', 'code': '688041', 'type': '半年报预告', 'growth': '+41.5%~+52.3%'},
    {'name': '摩尔线程', 'code': '688795', 'type': '半年报预告', 'growth': '营收+135%~+149%'},
    {'name': '佰维存储', 'code': '688525', 'type': '半年报预告', 'growth': '扭亏·净利7-7.5亿'},
    {'name': '生益电子', 'code': '688183', 'type': '半年报预告', 'growth': '+104%~+114%'},
    {'name': '南亚新材', 'code': '688519', 'type': '半年报预告', 'growth': '+382%~+473%'},
    {'name': '复旦微电', 'code': '688385', 'type': '半年报预告', 'growth': '扣非+92%~+147%'},
])

# 4. 数据发布
gen.add_data_release([
    {'name': '中国6月外汇收支', 'prev': 'Q1顺差1260亿', 'expect': '上半年顺差扩大', 'actual': '待公布'},
    {'name': '美国密歇根消费者信心', 'prev': '49.5', 'expect': '51.0', 'actual': '待公布'},
    {'name': '美国工业产出月率', 'prev': '0.1%', 'expect': '0.2%', 'actual': '待公布'},
    {'name': '美国进口物价月率', 'prev': '1.9%', 'expect': '-0.7%', 'actual': '待公布'},
    {'name': '欧元区6月核心CPI终值', 'prev': '2.4%', 'expect': '2.4%', 'actual': '待公布'},
    {'name': '美国房屋开工/营建许可', 'prev': '131万/140万', 'expect': '118万/141万', 'actual': '待公布'},
])

# 5. 限售解禁详情
ban_html = """
<div style="overflow-x: auto;">
<table style="width: 100%; border-collapse: collapse; font-size: 13px;">
<thead><tr style="background: rgba(239, 68, 68, 0.1);">
<th style="padding: 10px 12px; text-align: left; border-bottom: 1px solid rgba(255,255,255,0.1); color: #fca5a5;">股票名称</th>
<th style="padding: 10px 12px; text-align: center; border-bottom: 1px solid rgba(255,255,255,0.1); color: #fca5a5;">代码</th>
<th style="padding: 10px 12px; text-align: right; border-bottom: 1px solid rgba(255,255,255,0.1); color: #fca5a5;">解禁数量</th>
<th style="padding: 10px 12px; text-align: right; border-bottom: 1px solid rgba(255,255,255,0.1); color: #fca5a5;">占总股本</th>
<th style="padding: 10px 12px; text-align: center; border-bottom: 1px solid rgba(255,255,255,0.1); color: #fca5a5;">解禁类型</th>
<th style="padding: 10px 12px; text-align: left; border-bottom: 1px solid rgba(255,255,255,0.1); color: #fca5a5;">影响评估</th>
</tr></thead>
<tbody>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.05);">
<td style="padding: 10px 12px; color: #e2e8f0;">银龙股份</td>
<td style="padding: 10px 12px; text-align: center; color: #94a3b8;">603969</td>
<td style="padding: 10px 12px; text-align: right; color: #e2e8f0;">194.7万股</td>
<td style="padding: 10px 12px; text-align: right; color: #fbbf24;">0.223%</td>
<td style="padding: 10px 12px; text-align: center; color: #94a3b8;">股权激励</td>
<td style="padding: 10px 12px; color: #86efac;">🟢 低风险</td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.05);">
<td style="padding: 10px 12px; color: #e2e8f0;">印象股份</td>
<td style="padding: 10px 12px; text-align: center; color: #94a3b8;">—</td>
<td style="padding: 10px 12px; text-align: right; color: #e2e8f0;">43.42万股</td>
<td style="padding: 10px 12px; text-align: right; color: #fbbf24;">0.402%</td>
<td style="padding: 10px 12px; text-align: center; color: #94a3b8;">离职高管</td>
<td style="padding: 10px 12px; color: #86efac;">🟢 低风险</td>
</tr>
<tr>
<td style="padding: 10px 12px; color: #e2e8f0;">青岛食品</td>
<td style="padding: 10px 12px; text-align: center; color: #94a3b8;">001219</td>
<td style="padding: 10px 12px; text-align: right; color: #e2e8f0;">9.48万股</td>
<td style="padding: 10px 12px; text-align: right; color: #86efac;">0.049%</td>
<td style="padding: 10px 12px; text-align: center; color: #94a3b8;">首发前股份</td>
<td style="padding: 10px 12px; color: #86efac;">🟢 极低风险</td>
</tr>
</tbody>
</table>
</div>
<div style="margin-top: 14px; padding: 12px 16px; background: rgba(16, 185, 129, 0.08); border: 1px solid rgba(16, 185, 129, 0.2); border-radius: 10px; font-size: 13px; color: #86efac; line-height: 1.7;">
<b>解禁日总体评估</b>：7月17日仅3家公司有限售股解禁，合计规模极小（约250万股量级），均不足总股本0.5%，对市场整体流动性几乎无冲击。需注意下周一（7月20日）<b>节能环境（300140）约21亿股解禁</b>，虽控股股东承诺6个月不减持，但仍需关注情绪面影响。
</div>
"""
gen._components.append(Section(title="🔒 限售股解禁详情", content=ban_html, icon="lock"))

# 6. 新股申购
ipo_html = """
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 14px;">
    <div style="background: rgba(30,30,50,0.5); border: 1px solid rgba(255,255,255,0.08); border-radius: 12px; padding: 18px;">
        <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 12px;">
            <div style="width: 40px; height: 40px; background: linear-gradient(135deg, #3b82f6, #1d4ed8); border-radius: 10px; display: flex; align-items: center; justify-content: center; font-size: 20px;">🔬</div>
            <div>
                <div style="font-size: 15px; font-weight: 700; color: #f1f5f9;">长鑫科技</div>
                <div style="font-size: 12px; color: #94a3b8;">688825 · 科创板 · DRAM存储芯片</div>
            </div>
        </div>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px; font-size: 12px;">
            <div style="color: #94a3b8;">发行价</div><div style="color: #fbbf24; text-align: right;">8.66元/股</div>
            <div style="color: #94a3b8;">发行规模</div><div style="color: #e2e8f0; text-align: right;">66.88亿股</div>
            <div style="color: #94a3b8;">募资总额</div><div style="color: #e2e8f0; text-align: right;">579亿元</div>
            <div style="color: #94a3b8;">动态PE</div><div style="color: #86efac; text-align: right;">约10.8倍</div>
            <div style="color: #94a3b8;">申购状态</div><div style="color: #fbbf24; text-align: right;">✅ 7/16已申购</div>
            <div style="color: #94a3b8;">配号中签率</div><div style="color: #fbbf24; text-align: right;">📅 明日公布</div>
        </div>
        <div style="margin-top: 12px; padding: 10px; background: rgba(34, 197, 94, 0.1); border-radius: 8px; font-size: 12px; color: #86efac; line-height: 1.6;">
        <b>申购建议</b>：⭐⭐⭐⭐⭐ 积极参与。国内唯一DRAM规模化量产IDM龙头，全球第四，绿鞋机制托底，国家大基金战略配售50%。行业超级周期上行，动态PE仅10.8倍显著低于同业。
        </div>
    </div>
    <div style="background: rgba(30,30,50,0.5); border: 1px solid rgba(255,255,255,0.08); border-radius: 12px; padding: 18px;">
        <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 12px;">
            <div style="width: 40px; height: 40px; background: linear-gradient(135deg, #6b7280, #374151); border-radius: 10px; display: flex; align-items: center; justify-content: center; font-size: 20px;">📋</div>
            <div>
                <div style="font-size: 15px; font-weight: 700; color: #f1f5f9;">明日无新股申购</div>
                <div style="font-size: 12px; color: #94a3b8;">7月17日无可申购新股</div>
            </div>
        </div>
        <div style="font-size: 12px; color: #94a3b8; line-height: 1.8;">
        近期重点新股进度：<br>
        • 长鑫科技：T+1（明日配号）<br>
        • 7月20日：长鑫T+2中签缴款
        </div>
        <div style="margin-top: 12px; padding: 10px; background: rgba(251, 191, 36, 0.1); border-radius: 8px; font-size: 12px; color: #fcd34d; line-height: 1.6;">
        <b>打新提醒</b>：7月20日（周一）长鑫科技T+2日，中签投资者需当日16:00前确保账户资金充足。连续12个月3次放弃将被暂停打新资格6个月。
        </div>
    </div>
</div>
"""
gen._components.append(Section(title="📝 新股申购", content=ipo_html, icon="file-text"))

# 7. 海外大事
overseas_html = """
<div style="display: flex; flex-direction: column; gap: 12px;">
    <div style="background: rgba(30,30,50,0.5); border: 1px solid rgba(255,255,255,0.08); border-radius: 12px; padding: 14px 16px;">
        <div style="font-size: 14px; font-weight: 600; color: #f87171; margin-bottom: 6px;">🇺🇸 美国：特朗普讲话 + 经济数据密集</div>
        <div style="font-size: 12px; color: #94a3b8; line-height: 1.7;">
        北京时间7月17日20:00特朗普就经济议题发表讲话（关注关税与货币政策表态）；20:30进口物价指数、21:15工业产出与产能利用率、22:00密歇根大学消费者信心初值与通胀预期。FOMC委员Schmid和Jefferson先后发表讲话，美联储政策信号密集。
        </div>
    </div>
    <div style="background: rgba(30,30,50,0.5); border: 1px solid rgba(255,255,255,0.08); border-radius: 12px; padding: 14px 16px;">
        <div style="font-size: 14px; font-weight: 600; color: #60a5fa; margin-bottom: 6px;">🇪🇺 欧元区：6月核心CPI终值</div>
        <div style="font-size: 12px; color: #94a3b8; line-height: 1.7;">
        北京时间7月17日17:00公布欧元区6月CPI终值与核心CPI终值，预期核心CPI同比2.4%与初值持平。若核心通胀超预期回落，欧洲央行降息预期将升温。同时公布欧元区经常账户，前值181亿欧元。
        </div>
    </div>
    <div style="background: rgba(30,30,50,0.5); border: 1px solid rgba(255,255,255,0.08); border-radius: 12px; padding: 14px 16px;">
        <div style="font-size: 14px; font-weight: 600; color: #fbbf24; margin-bottom: 6px;">🛢️ 能源：贝克休斯钻井数 + 中东局势</div>
        <div style="font-size: 12px; color: #94a3b8; line-height: 1.7;">
        凌晨1:00公布美国石油钻井总数（前值448座，预期445座）。中东局势仍是原油市场核心变量，特朗普称"伊朗局势稳定后油价将跌至55美元/桶"，市场观望情绪浓厚。
        </div>
    </div>
    <div style="background: rgba(30,30,50,0.5); border: 1px solid rgba(255,255,255,0.08); border-radius: 12px; padding: 14px 16px;">
        <div style="font-size: 14px; font-weight: 600; color: #c084fc; margin-bottom: 6px;">🇹🇭 外交：泰国总理访华</div>
        <div style="font-size: 12px; color: #94a3b8; line-height: 1.7;">
        泰国总理佩通坦7月16-20日对中国进行正式访问并出席WAIC 2026。习近平主席同其会见，李强、赵乐际分别会谈。中泰数字经济、AI合作、铁路等议题值得关注。
        </div>
    </div>
</div>
"""
gen._components.append(Section(title="🌍 海外大事提醒", content=overseas_html, icon="globe"))

# 8. 深度影响分析
deep_analysis = """
<div style="line-height: 1.9; color: #e2e8f0; font-size: 14px;">

<h3 style="color: #fbbf24; font-size: 16px; margin-top: 0; margin-bottom: 12px;">一、WAIC 2026开幕：AI政策最高级别催化，算力与人形机器人双线共振</h3>

<p style="margin: 10px 0;"><b>事件定位</b>：2026世界人工智能大会是今年中国最高规格的AI产业盛会，习近平主席亲自出席开幕式并发表主旨讲话，规格远超往届。1100余家企业参展、300余款全球首发产品，体量为历届之最。智算与人形机器人两大赛道各汇聚超200家企业，是产业趋势的"风向标"。</p>

<p style="margin: 10px 0;"><b>影响路径</b>：第一，最高领导人定调中国AI发展方向，政策确定性极强。预计将围绕"AI+行动"、算力基础设施、AI治理三大维度释放政策信号，直接利好AI算力板块（服务器、液冷、光模块、芯片）。第二，具身智能/人形机器人作为大会重点赛道，绿的谐波、步科股份等核心零部件企业登台展示，板块情绪有望被点燃。第三，海光信息、摩尔线程、沐曦股份等国产算力芯片企业携最新产品亮相，国产替代逻辑进一步强化。</p>

<p style="margin: 10px 0;"><b>操作建议</b>：持仓股中，<b>英维克（002837）</b>作为液冷散热龙头直接受益于AI算力基建加速，建议持有并关注大会期间液冷板块的情绪催化。<b>雅克科技（002409）</b>作为半导体材料平台型公司，HBM封装材料需求与AI算力周期高度相关，大会催化有望带动存储产业链情绪。注意：大会开幕日往往是"利好兑现"节点，不宜追高，应以持仓持有或回调加仓为主。</p>

<h3 style="color: #fbbf24; font-size: 16px; margin-top: 24px; margin-bottom: 12px;">二、长鑫科技IPO里程碑：存储国产替代核心资产正式亮相</h3>

<p style="margin: 10px 0;"><b>事件定位</b>：长鑫科技作为国内唯一实现DRAM规模化量产的IDM龙头，全球市占率第四，579亿元募资是科创板史上第二大IPO。7月16日申购、7月17日配号中签率公布、7月20日中签结果，整个IPO进程贯穿本周，是存储板块最重要的催化剂之一。</p>

<p style="margin: 10px 0;"><b>影响路径</b>：一是"存储超级周期"逻辑获得资本市场最高级别验证——长鑫作为行业核心玩家，其上市本身就是行业景气度的确认。二是产业链映射效应显著：铜冠铜箔（锂电铜箔+电子铜箔双轮驱动，PCB/CCL上游）、雅克科技（半导体材料）、生益电子/南亚新材（覆铜板/PCB）等上游材料企业有望获得估值联动。三是科创板整体情绪提振：超级IPO的成功发行显示市场对科技成长方向的信心，利好科创板整体风险偏好。</p>

<p style="margin: 10px 0;"><b>操作建议</b>：持仓股<b>铜冠铜箔（301217）</b>作为电子铜箔供应商，间接受益于存储芯片产业链高景气。铜冠铜箔当前处于相对低位，AI算力+存储周期双催化下具备修复空间，可继续持有等待催化。<b>雅克科技</b>作为半导体材料龙头，HBM前驱体/封装材料业务直接受益于存储扩产，中长期逻辑不变。</p>

<h3 style="color: #fbbf24; font-size: 16px; margin-top: 24px; margin-bottom: 12px;">三、半年报业绩预告密集披露：AI链业绩验证期到来</h3>

<p style="margin: 10px 0;"><b>事件定位</b>：截至7月16日，科创板已有32家公司披露半年报预告，其中30家预喜（占比超93%），AI产业链业绩集中爆发。海光信息净利增长41-52%、摩尔线程营收增长135-149%、佰维存储扭亏盈利7-7.5亿、生益电子增长104-114%、南亚新材大增382-473%，产业链从算力芯片→存储→PCB→覆铜板→材料全链条业绩兑现。</p>

<p style="margin: 10px 0;"><b>影响判断</b>：AI产业链业绩大爆发不是单家公司的孤例，而是从算力芯片到上游材料的全产业链共振，验证了"AI算力超级周期"的产业逻辑。这与2026年上半年出口高增（6月单月增27%）、工业增加值超预期形成宏观+中观双验证。业绩为王的市场环境下，有真实业绩支撑的AI链标的将获得持续资金青睐。</p>

<p style="margin: 10px 0;"><b>持仓影响评估</b>：<b>英维克</b>液冷业务上半年大概率保持高增长，行业需求端持续验证。<b>雅克科技</b>半导体材料业务受益于存储扩产+先进封装双驱动。<b>铜冠铜箔</b>电子铜箔业务有望在下半年体现量价齐升。三只持仓均处于AI算力产业链上游/材料端，业绩确定性较强，中报季可逢低布局。</p>

<h3 style="color: #fbbf24; font-size: 16px; margin-top: 24px; margin-bottom: 12px;">四、外汇局发布会：人民币汇率走势是宏观关键变量</h3>

<p style="margin: 10px 0;"><b>事件定位</b>：国新办上午10点的外汇局发布会，将披露上半年外汇收支全貌。近期人民币升值态势明显——离岸人民币盘中涨破6.77，创近四周新高。外汇储备规模、跨境资本流动、央行对汇率的态度是市场关注焦点。</p>

<p style="margin: 10px 0;"><b>影响判断</b>：若外汇局释放积极信号、确认外资持续流入，将进一步强化人民币升值预期，利好A股整体流动性，尤其利好外资重仓的消费、金融、新能源等板块。反之，若提及汇率波动风险或资本外流压力，则可能压制市场风险偏好。对AI/科技板块的间接影响主要通过风险偏好传导。</p>

</div>
"""
gen.add_impact_analysis(deep_analysis)

# 9. Skill增强深度分析
gen.add_catalyst_deep_analysis([
    {'title': 'WAIC 2026世界人工智能大会', 'type': 'meeting',
     'description': '习近平出席开幕式，1100+企业参展，300余款全球首发，AI算力与人形机器人两大核心赛道',
     'category': 'AI大会·S级催化'},
    {'title': '长鑫科技科创板IPO', 'type': 'general',
     'description': '579亿元募资，科创板史上第二大IPO，国内DRAM唯一量产龙头，国产替代核心资产',
     'category': 'IPO里程碑·存储'},
    {'title': '半年报业绩密集披露', 'type': 'earnings',
     'description': 'AI产业链业绩集中爆发，科创板预喜率超93%，算力芯片-存储-PCB-材料全链条增长',
     'category': '业绩验证·AI链'},
])

# 10. 风险提示
gen.add_risk_warning([
    "WAIC 2026开幕日可能出现\"利好兑现\"行情，AI板块短期冲高回落风险",
    "美国密歇根消费者信心及通胀预期若超预期上行，可能推迟美联储降息预期，压制全球风险资产",
    "特朗普讲话涉及关税或贸易政策，可能引发市场波动",
    "长鑫科技巨量IPO对市场流动性的抽血效应需观察",
    "半年报业绩预告进入密集期，部分不及预期个股可能出现大幅调整",
    "中东地缘局势反复，原油价格波动可能传导至通胀与货币政策预期",
    "持仓股*ST建艺存在退市风险警示，需严格执行止损纪律"
])

# 发布
print("开始生成明日催化剂报告...")
result = gen.publish(
    title="2026.07.17 明日催化剂",
    excerpt="WAIC 2026盛大开幕 · 长鑫科技IPO里程碑 · 外汇局上半年数据发布 · AI链业绩大爆发验证",
    auto_deploy=True
)
print(f"发布结果: {result}")
