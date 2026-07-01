#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
2026年7月1日周三前瞻报告生成
"""
import sys, os
sys.path.insert(0, '/root/daily-news-insight')
sys.path.insert(0, '/root/daily-news-insight/v3')

from datetime import datetime
from generators.weekly_outlook_pro import WeeklyOutlookProGenerator

OUTPUT_PATH = '/root/daily-news-insight/docs/weekly_outlook/20260701_周三前瞻.html'

gen = WeeklyOutlookProGenerator(date_str='2026-07-01', data_dir='/root/daily-news-insight/data')
gen.active_page = '周三前瞻'

# ========== 1. 周中核心观察 ==========
midweek_summary = '''
<p>7月首个交易日（7/1）A股呈现极端分化：<b class="text-green-400">沪指涨0.44%报4112点</b>，保险/券商大涨7%/4.8%领涨，全市场超4300股上涨、220股涨停；但<b class="text-red-400">创业板指跌1.89%、科创综指跌1.34%</b>，CPO/PCB/元件等前期高位科技股集体回调，寒武纪等高估值票发风险提示公告，<b>典型的"高低切换"首日</b>。成交3.66万亿，放量3862亿，资金从高位科技流向大金融+中报绩优方向。</p>
<p class="mt-2"><b>周中定调：</b>市场正经历"业绩定价"切换——7/15前中报预告密集披露+7/6交易新规+7/2-7/29海外央行超级周（非农→CPI→FOMC），<b>7月是全年最关键的"验牌月"（利率/AI/财报三张牌）</b>。操作上：<b class="text-yellow-400">高位无业绩科技股必须减仓兑现，半导体设备/存储/HBM等中报确定性高的方向回踩即加仓</b>。</p>
'''
gen.add_midweek_summary(midweek_summary)

# ========== 2. 周中市场概览 ==========
gen.add_market_status([
    {'name': '上证指数', 'value': '4112.45', 'change': '+0.44%', 'up': True},
    {'name': '深证成指', 'value': '16119.17', 'change': '-0.53%', 'up': False},
    {'name': '创业板指', 'value': '4260.72', 'change': '-1.89%', 'up': False},
    {'name': '科创综指', 'value': '—', 'change': '-1.34%', 'up': False},
    {'name': '北证50', 'value': '1264.94', 'change': '+1.10%', 'up': True},
    {'name': '两市成交', 'value': '3.66万亿', 'change': '+3862亿', 'up': True},
    {'name': '涨停/跌停', 'value': '220/—', 'change': '4300+上涨', 'up': True},
    {'name': '伦敦金', 'value': '~4000', 'change': '跌破4000后反弹', 'up': False},
])

# ========== 3. 下周重大事件日历 ==========
calendar_html = '<div style="display:flex;flex-direction:column;gap:10px;">'
events = [
    ('07/02 周四', '🔥 S级', '美国6月非农就业数据（20:30）', '因独立日提前到周四公布，预期新增11.3万、失业率4.3%。白宫官员暗示数据或强劲——超预期强化加息预期压制成长股；弱于预期则降息预期升温科技股反弹。<b class="text-yellow-400">今晚ADP+明晚非农是周内最大变量</b>。'),
    ('07/02-04', '🔥 S级', '上海国际具身智能产业博览会', '首届展会200+企业参展，宇树/加速进化/乐聚/中科新松等整机厂亮相，三大全国赛事+出海对接会。<b class="text-green-400">减速器/伺服/传感器/灵巧手方向催化</b>，关注绿的谐波、双环传动、汇川技术、埃斯顿、拓斯达。'),
    ('07/02-04', '⭐ A级', '全球数字经济大会（北京）', 'AI算力、数据要素、信创政策集中披露。'),
    ('07/01-03', '⭐ A级', '慕尼黑上海电子展', 'AI芯片、车载电子、先进封装、功率半导体主题，英飞凌/意法AI机柜MOS/隔离芯片新品集中展示。'),
    ('07/01-04', '⭐ A级', '达沃斯科技峰会（瑞士）', '聚焦"物理AI与机器人"，英伟达主讲，Robot City全城落地演示。'),
    ('07/03 周五', '⚡ B级', '成品油调价窗口+美国独立日（美股休市）', '油价调整+外围休市，北向通道波动加大。'),
    ('07/05-07', '⭐ A级', '第四届国际商业航天遥感卫星应用大会', '商业航天/卫星互联网催化。'),
    ('07/06 周一', '🔥 S级', 'A股交易新规正式实施', '三大改动：①<b>主板ST/*ST涨跌幅由5%扩至10%</b>；②<b>盘后固定价交易扩展至全A股+ETF</b>（15:05-15:30按收盘价）；③ETF尾盘3分钟改集合竞价。<b class="text-red-400">*ST建艺必须在反抽中果断离场！</b>'),
    ('07/08 周三', '🔥 S级', '美联储6月议息会议纪要公布', '定调7/29 FOMC预期，直接影响北向资金——偏鹰则科技承压，偏鸽则成长修复。'),
    ('07/08-10', '⭐ A级', '中国互联网大会（北京）', '政企AI算力、信创、数据要素集采政策披露，国产服务器/算力整机催化。'),
    ('07/02起', '🔥 S级', '三星+SK海力士韩国4万亿人民币投资计划+SK海力士7/10美股IPO', '三星300万亿韩元建芯片厂；SK海力士7/10美股ADR上市融资294亿美元（史上第三大IPO）。<b class="text-green-400">HBM/存储超级周期获资本端验证</b>，对标HBM材料（雅克科技）、铜箔（铜冠铜箔）。'),
    ('7月全月', '🔥 S级', '全球半导体全线调价+中报预告披露至7/15', 'AI芯片/HBM/DRAM/NAND/功率/模拟全链涨价，Q3 DRAM环比+40-50%；中报预增集中半导体设备（长川+110~134%）、存储、MLCC、锂电材料。<b class="text-yellow-400">7/15前是中报行情黄金窗口</b>。'),
]
for date, level, title, desc in events:
    if 'S级' in level:
        border='border-red-500/50'; bg='bg-red-500/5'; tag='bg-red-500/20 text-red-300 border-red-500/40'
    elif 'A级' in level:
        border='border-orange-500/40'; bg='bg-orange-500/5'; tag='bg-orange-500/20 text-orange-300 border-orange-500/40'
    else:
        border='border-blue-500/30'; bg='bg-blue-500/5'; tag='bg-blue-500/20 text-blue-300 border-blue-500/40'
    calendar_html += f'''
    <div style="border:1px solid {border.replace('border-','')};background:{bg.replace('bg-','')};border-radius:12px;padding:14px 16px;">
        <div style="display:flex;align-items:center;gap:10px;flex-wrap:wrap;margin-bottom:6px;">
            <span style="font-family:monospace;color:#94a3b8;font-size:13px;min-width:90px;">{date}</span>
            <span style="padding:2px 10px;border-radius:20px;font-size:11px;font-weight:700;border:1px solid;{tag}">{level}</span>
            <span style="color:white;font-weight:600;font-size:14px;">{title}</span>
        </div>
        <div style="color:#cbd5e1;font-size:13px;line-height:1.7;padding-left:100px;">{desc}</div>
    </div>'''
calendar_html += '</div>'
gen.add_section('📅 下周重大事件日历（7/2-7/11）', calendar_html, '📅')

# ========== 4. 重点关注题材 ==========
topics = [
    {'name': 'S级：存储芯片/HBM（超级周期最强主线）','attention':'🔥 核心仓位',
     'logic':'<b>逻辑最硬、业绩最确定</b>：①7/1起全球近20家半导体厂全线调价，Q3 DRAM环比+40~50%、Q4再+30%，HBM产能被云厂商3-5年长单锁死，新产能2028年才释放；②三星1000万亿韩元投资+300万亿建芯片厂，SK海力士7/10美股IPO融资294亿美元（HBM王者赴美估值重塑）；③美光Q3毛利率84%历史新高，高盛上调三星2027 HBM价增预测至+44%；④中报业绩弹性最大（佰维/德明利利润破40亿级别）。<b>持仓铜冠铜箔（HVLP铜箔受益HBM封装）+雅克科技（HBM封装材料）继续持有，170/220均线以上底仓锁利</b>。',
     'stocks':['铜冠铜箔(301217)','雅克科技(002409)','兆易创新','佰维存储','江波龙','澜起科技','长电科技','华海诚科']},
    {'name': 'S级：半导体设备/材料（中报预增+国产替代）','attention':'🔥 核心仓位',
     'logic':'<b>七月核心主线</b>：①二季度业绩爆炸，长川科技中报预增110-134%（Q2环比+55~83%加速），北方华创/盛美/华峰订单排到2027；②7/15-17成都全球半导体博览会+大基金三期配套政策落地；③8寸成熟产能紧缺+设备国产化率加速；④板块上半年仅涨35%，估值分位40%，安全边际充足，是机构高低切换首选。',
     'stocks':['北方华创','中微公司','长川科技','盛美上海','拓荆科技','华峰测控','芯源微']},
    {'name': 'A级：人形机器人/具身智能（展会强催化）','attention':'⭐ 短线博弈',
     'logic':'7/2-4上海具身智能博览会是七月高端制造核心催化：200+企业参展+三大赛事+出海对接会，叠加达沃斯"物理AI"主题、十五五未来产业吹风。板块脱离概念期进入订单兑现。<b class="text-yellow-400">题材弹性大波动大，快进快出不恋战，优先核心零部件（减速器/丝杠/灵巧手）</b>。',
     'stocks':['绿的谐波','双环传动','汇川技术','三花智控','拓普集团','埃斯顿','拓斯达']},
    {'name': 'A级：功率半导体/电子特气（全线涨价）','attention':'⭐ 重点跟踪',
     'logic':'英飞凌/意法年内第二轮涨价，车规IGBT、AI机柜MOS涨10-20%，800V隔离芯片涨25%；电子特气（日本六氟化钨收缩）7/1金宏气体20cm涨停验证。8寸产线稼动率85-90%满负荷，新产能2027H2才释放。',
     'stocks':['斯达半导','扬杰科技','时代电气','金宏气体','兴福电子']},
    {'name': 'B级：券商/大金融（交易新规+中报）','attention':'👀 轮动观察',
     'logic':'7/1券商暴涨4.84%（华安/天风/国盛涨停），保险涨7.09%，催化是7/6交易新规（盘后固定价交易扩容、ETF优化利好金融IT）+中报改善+市场放量。<b>持续性待观察，不追高</b>。',
     'stocks':['东方财富','同花顺','中信证券','华安证券','新华保险']},
    {'name': 'B级：MLCC/被动元件（AI服务器拉动）','attention':'👀 轮动观察',
     'logic':'AI服务器MLCC用量是普通服务器8-10倍，村田/松下涨价，国内龙头风华/三环开工率满负荷，中报预增确定，位置相对较低。',
     'stocks':['风华高科','三环集团','洁美科技','国瓷材料']},
]
gen.add_focus_topics(topics)

# ========== 5. 核心持仓前瞻策略 ==========
portfolio_html = '<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:14px;">'
portfolio = [
    {'name':'🔴 英维克 (002837)','price':'74.73','chg':'-6.07% 创新低','pnl':'-28.30% 深度破止损',
     'plan':'7/1继续暴跌创新低74元，液冷温控在高低切换中失血。<b class="text-red-400">纪律：逢高坚决减仓≥1/2</b>，反弹78-80是减仓窗口；下破72元无条件清仓。7/17 WAIC液冷环节或有脉冲，仅作逃命波。','color':'red'},
    {'name':'🟢 铜冠铜箔 (301217)','price':'164.84','chg':'-0.14% 高位震荡','pnl':'+89.12% 浮盈丰厚',
     'plan':'存储涨价+HBM封装铜箔是最确定主线之一，三星/SK 4万亿投资+SK海力士7/10美股上市是短期强催化。<b class="text-green-400">策略：170上方减1/3锁利，移动止盈上移至165</b>；回踩160-165不破可加回。Q3 DRAM涨价40-50%是下一波主升浪催化，底仓长线持有。','color':'green'},
    {'name':'🟢 雅克科技 (002409)','price':'236.09','chg':'+5.16% 续创历史新高','pnl':'+116.99% 主升浪',
     'plan':'HBM封装材料核心龙头，7/1大涨5.16%创历史新高。SK海力士赴美上市+HBM4批量交付是核心催化，7/15-17成都半导体博览会潜在催化。<b class="text-green-400">策略：底仓持有</b>，回踩5日线（215-220）是决策加仓点；冲高250+可小部分T出锁利，但底仓不丢。','color':'green'},
    {'name':'🔴 *ST建艺 (002789)','price':'12.00','chg':'破止损位','pnl':'-10.78%',
     'plan':'<b class="text-red-400">7/6起ST涨跌幅扩至10%是生死线！最后的离场窗口。</b>规则变化后：①利空单日-10%快速释放，两日最大亏19%；②投资者赔偿常态化+退市加速，垃圾ST出清。<b class="text-red-400">纪律：7/2-7/3盘中任何反抽（12.3-12.6）是最后离场机会，7/6前必须清仓！</b>','color':'red'},
]
for p in portfolio:
    border = 'border-red-500/40' if p['color']=='red' else 'border-green-500/40'
    bg = 'bg-red-500/5' if p['color']=='red' else 'bg-green-500/5'
    chg_cls = 'text-red-400' if p['color']=='red' else 'text-green-400'
    portfolio_html += f'''
    <div style="border:1px solid {border.replace('border-','')};background:{bg.replace('bg-','')};border-radius:12px;padding:14px 16px;">
        <div style="margin-bottom:8px;"><span style="color:white;font-weight:700;font-size:15px;">{p['name']}</span></div>
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:6px;font-size:12px;margin-bottom:10px;">
            <div style="color:#94a3b8;">最新价：<span class="{chg_cls} font-semibold">{p['price']}</span></div>
            <div style="color:#94a3b8;">今日：<span class="{chg_cls} font-semibold">{p['chg']}</span></div>
            <div style="grid-column:1/-1;color:#94a3b8;">浮盈/亏：<span class="{chg_cls} font-semibold">{p['pnl']}</span></div>
        </div>
        <div style="color:#cbd5e1;font-size:13px;line-height:1.7;border-top:1px solid rgba(255,255,255,0.08);padding-top:10px;">{p['plan']}</div>
    </div>'''
portfolio_html += '</div>'
gen.add_section('💼 核心持仓下周操作策略', portfolio_html, '💼')

# ========== 6. 下半周+下周操作策略 ==========
strategy = '''
<div style="line-height:1.9;">
<p><b>🎯 总仓位建议：5成（中性偏谨慎）</b>——7/2-7/29海外央行超级周（非农→CPI→ECB→BoJ→FOMC）+7/6交易新规+7/15中报截止，<b>波动显著放大</b>，不满仓。</p>
<p class="mt-3"><b>📌 三段式操作节奏：</b></p>
<p><b>① 7/2-7/4（本周三四五）：</b>今晚ADP+沃什讲话+明晚非农，<b class="text-yellow-400">数据前控仓不追高</b>。非农超强则科技再杀一波=设备/存储低吸机会；非农弱则科技反弹=减高位票窗口。关注具身智能博览会短线博弈。</p>
<p><b>② 7/6-7/10（下周一起）：</b>交易新规首周+美联储纪要+中报密集披露，<b class="text-green-400">7月最好调仓窗口</b>：<b>卖高买低</b>——卖无业绩CPO/PCB/纯题材小票，买半导体设备/存储/HBM材料/电子特气等中报预增确定方向。</p>
<p><b>③ 7/15后：</b>中报截止+成都半导体博览会(7/15-17)+WAIC(7/17-20)，业绩验证后科技主线有望主升，但警惕"利好兑现"。</p>
<p class="mt-3"><b>🚨 三条铁律：</b></p>
<ul style="padding-left:20px;margin:8px 0;">
<li><b class="text-red-400">*ST建艺7/6前必须清仓</b>，ST扩至10%后单日跌停风险翻倍</li>
<li><b class="text-yellow-400">英维克反弹减仓≥1/2</b>，下破72元无条件离场</li>
<li><b class="text-green-400">铜冠铜箔/雅克科技底仓保留</b>，但170/250上方分批锁利1/3</li>
</ul>
<p class="mt-3"><b>💡 方向优先级：</b><br>
<b>核心配置（3成）：</b>存储/HBM（铜冠+雅克+兆易+长电）+ 半导体设备（北方华创+长川+盛美）<br>
<b>短线博弈（1成）：</b>人形机器人/具身智能（绿的谐波+双环+埃斯顿），快进快出<br>
<b>规避：</b>高位无业绩CPO/光模块小票、ST垃圾股、纯题材无订单概念股
</p>
</div>
'''
gen.add_second_half_strategy(strategy)

# ========== 7. 操作要点 ==========
gen.add_strategy_points([
    {'title':'仓位管理','content':'总仓位5成，核心科技3成+短线1成+现金1成，7/29 FOMC前不加满'},
    {'title':'高低切换','content':'7月"业绩定价月"，从高位无业绩科技切换至中报预增确定的半导体设备/存储/电子特气'},
    {'title':'ST紧急处理','content':'7/6主板ST涨跌幅扩至10%，*ST建艺7/3前反抽必须清仓，不抱幻想'},
    {'title':'数据节点','content':'今晚ADP/沃什、明晚非农、7/8美联储纪要、7/10 SK海力士美股上市、7/14 CPI、7/15中报截止'},
    {'title':'不追高','content':'券商/保险7/1大涨是情绪脉冲不追；机器人题材只低吸不打板'},
])

# ========== 8. 风险提示 ==========
gen.add_risk_warning([
    '🔥 美国6月非农超预期→加息预期升温→美元/美债收益率上行→成长股估值承压',
    '🔥 美联储7/29 FOMC偏鹰（点阵图已转加息，近半数官员支持年内加息）',
    '⚠️ 7/6 ST涨跌幅扩至10%，ST板块可能踩踏式下跌，*ST建艺单日-10%风险',
    '⚠️ 中报预告期"业绩雷"，纯题材/无订单/高位小票集中杀估值',
    '⚠️ 7月欧美夏季度假，流动性萎缩，波幅或放大1.5-2倍',
    '⚡ 美伊谈判反复、中东局势、霍尔木兹海峡通航不确定性',
    '⚡ 金价跌破4000美元后剧烈震荡，黄金相关标的波动率放大',
])

os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
result = gen.save(OUTPUT_PATH)
print(f"OK saved: {result}, size={os.path.getsize(OUTPUT_PATH)}")
with open(OUTPUT_PATH,'r',encoding='utf-8') as f:
    html=f.read()
for c in ['周三前瞻','2026-07-01','glass-nav','7月6日','ST建艺','非农','具身智能','半导体设备','HBM','4112']:
    print(f"  {'✅' if c in html else '❌'} {c}")
