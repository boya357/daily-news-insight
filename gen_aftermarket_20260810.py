#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
盘后速递 - 2026年8月10日
使用 V3.0 AftermarketGenerator 生成
"""

import sys
import os

sys.path.insert(0, '/root/daily-news-insight/v3')
os.chdir('/root/daily-news-insight')

from v3.generators.aftermarket import AftermarketGenerator
from v3.core.report import Section

# ============================================================
# 初始化生成器
# ============================================================
gen = AftermarketGenerator(
    date_str="20260810",
    subtitle="2026.08.10 · 盘后速递"
)

# ============================================================
# 1. 今日核心亮点
# ============================================================
gen.add_today_highlight(
    "沪指5连阳逼近4000点关口，两市成交2.52万亿维持历史高位；"
    "科技股早盘杀跌尾盘回补，消费医药军工黄金轮番走强，市场高低切换特征明显；"
    "铜冠铜箔+4.47%、雅克科技+4.34%领涨持仓，英维克续跌-1.18%创调整新低。"
)

# ============================================================
# 2. 市场收盘总结
# ============================================================
indices = [
    {'name': '上证指数', 'value': '3966.59', 'change': '+0.67%', 'up': True, 'icon': 'trending_up'},
    {'name': '深证成指', 'value': '14316.96', 'change': '+0.04%', 'up': True, 'icon': 'trending_up'},
    {'name': '创业板指', 'value': '3537.21', 'change': '-0.73%', 'up': False, 'icon': 'trending_down'},
    {'name': '科创50', 'value': '1737.77', 'change': '-0.36%', 'up': False, 'icon': 'trending_down'},
]
gen.add_market_summary(indices, volume="2.52万亿", northbound="小幅净流入")

# ============================================================
# 3. 盘面深度解读
# ============================================================
strong_sectors = [
    {'name': '地面兵装/军工', 'reason': '"十五五"规划军工方向持续发酵，兵装重组概念涨超7%，北方长龙20CM涨停，长城军工、洪都航空涨停，国企改革+重组预期双重催化，板块持续性较强。'},
    {'name': '医疗服务/CXO', 'reason': 'CXO超跌反弹，百花医药5连板，百普赛斯20CM涨停，毕得医药、药康生物等跟涨。药明康德美国法院初步禁令胜诉构成直接催化，叠加板块前期调整充分，机构资金回补明显。'},
    {'name': '贵金属/有色', 'reason': '金价站上4416美元/盎司创历史新高，美元指数跌破100，招金黄金涨停、翔鹭钨业4天2板。通胀预期+地缘风险+美元走弱三重逻辑支撑，黄金上行趋势未变。'},
    {'name': '大消费/食品饮料', 'reason': '白酒板块涨2.7%，迎驾贡酒涨超6%，养殖、酒店餐饮、预制菜等方向集体走强。暑期消费旺季+低位补涨逻辑，资金从高位科技流向低位消费防御。'},
    {'name': '电网设备', 'reason': '中电鑫龙、京泉华、三变科技涨停，电网投资加速+新型电力系统建设催化，叠加特高压、储能产业链联动，板块处于景气上行期。'},
]

weak_sectors = [
    {'name': 'CPO/光模块', 'reason': '光迅科技触及跌停，中际旭创、新易盛跌超5%，通宇通讯跌8.31%。前期涨幅过大，获利盘集中兑现，机构高位派发迹象明显，短期调整压力仍存。'},
    {'name': '通信设备/6G', 'reason': '板块早盘跌超5%，收盘跌3.67%，武汉凡谷跌9.64%，通宇通讯跌8.31%。游资主导的热门股大幅回调，机构资金流出规模较大。'},
    {'name': '保险/大金融', 'reason': '保险板块走弱，拖累沪指上方空间。利率下行预期压制保险板块估值，中报季临近资金趋于谨慎。'},
    {'name': 'PCB/元件', 'reason': '板块跌1.25%，生益科技、沪电股份等调整。科技板块整体分化，PCB作为中游环节面临估值压力。'},
    {'name': 'AI手机/消费电子', 'reason': '板块回调，高位科技股获利回吐，资金高低切换明显，消费电子链跟随调整。'},
]

core_view = (
    "今日A股呈现典型的\"沪强深弱、黄白分化\"格局，沪指5连阳逼近4000点关口，"
    "而创业板指盘中一度跌超2.5%后尾盘收窄至-0.73%，留下长下影线。市场核心特征是"
    "\"高低切换+防御占优\"：高位的CPO、光模块、通信设备等科技赛道集体调整，"
    "低位的医药、军工、消费、贵金属等板块轮番走强。"
    "从资金面看，两市成交2.52万亿较上周五缩量1413亿，但仍处于历史高位，"
    "说明市场流动性依然充裕。上涨家数超4000家、涨跌比约3:1，赚钱效应扩散至中小盘股。"
    "北向资金小幅净流入，8月以来累计净流入已突破600亿。"
    "持仓方面，铜冠铜箔+4.47%、雅克科技+4.34%表现亮眼，科技股尾盘回补力度较强；"
    "英维克续跌-1.18%创调整新低，液冷板块仍处弱势；*ST建艺-0.81%相对抗跌。"
    "整体来看，科技主线进入震荡整固期，高低切换节奏加快，操作上宜控制仓位、波段应对。"
)

gen.add_market_deep_analysis(strong_sectors, weak_sectors, core_view)

# ============================================================
# 4. 情绪温度计
# ============================================================
gen.add_sentiment_thermometer(
    temperature=68,
    volume="2.52万亿",
    up_count="4068↑",
    down_count="1391↓",
    limit_up_count=103
)

# ============================================================
# 5. 持仓股深度诊断
# ============================================================
holdings = [
    {
        "name": "铜冠铜箔",
        "code": "301217",
        "price": "120.99",
        "change": "+4.47%",
        "up": True,
        "comment": (
            "<strong>【当日表现】</strong>今日收120.99元，大涨4.47%，成交额93.42亿，换手率大幅放大。"
            "早盘开118.81元，最高123.00元，最低113.21元，振幅达8.5%，呈现探底回升的强势格局。"
            "铜箔板块今日跟随科技股尾盘回补，作为PCB上游核心材料，受益于AI服务器和HBM需求增长。<br><br>"
            "<strong>【技术面】</strong>今日收放量长阳，收复5日和10日均线，MACD绿柱缩短，"
            "KDJ低位金叉向上，短期反弹趋势确立。压力位125-128元（前期平台），支撑位113-115元（今日低点附近）。"
            "从形态看，110-130元区间为前期筹码密集区，需要放量突破才能打开上行空间。<br><br>"
            "<strong>【资金面】</strong>成交93.42亿创近期新高，量价配合良好，主力资金净流入明显。"
            "尾盘拉升坚决，说明有机构资金在低位回补。<br><br>"
            "<strong>【操作建议】</strong>持仓者继续持有，已反弹至前期平台附近，注意125元以上压力。"
            "建议：底仓70%继续持有；反弹至125-128元区间减仓20%锁定利润；若回踩115元附近不破可加仓20%；"
            "跌破110元止损离场。核心逻辑：HBM+AI服务器铜箔需求增长确定性高，短期反弹后注意波段操作。"
        )
    },
    {
        "name": "雅克科技",
        "code": "002409",
        "price": "155.24",
        "change": "+4.34%",
        "up": True,
        "comment": (
            "<strong>【当日表现】</strong>今日收155.24元，上涨4.34%，成交额53.13亿，量能明显放大。"
            "早盘开152.00元探低至146.30元后强势回升，最高155.55元接近涨停板，"
            "尾盘维持高位震荡，全天振幅6.27%。半导体材料板块今日尾盘集体拉升，雅克作为前驱体龙头领涨。<br><br>"
            "<strong>【技术面】</strong>今日收中阳线，收复5日均线，MACD金叉雏形显现，"
            "KDJ从超卖区快速回升至中位。压力位160-165元（前期震荡平台上沿），支撑位145-148元（今日低点+20日线）。"
            "从周线看，140-170元大箱体震荡格局，目前处于箱体中下部，反弹空间较大。<br><br>"
            "<strong>【资金面】</strong>成交53.13亿较前几日明显放大，主力资金净流入约3-4亿，"
            "机构回补迹象明显。半导体材料板块整体资金回流，HBM产业链逻辑持续强化。<br><br>"
            "<strong>【操作建议】</strong>持仓者继续持有，今日反弹力度超预期。建议：底仓60%持有；"
            "反弹至160-165元区间减仓30%；回踩148-150元区间不破可加仓20%；跌破140元止损。"
            "核心逻辑：半导体材料国产替代+HBM前驱体需求爆发，短期跟随板块反弹，中期看业绩兑现。"
        )
    },
    {
        "name": "英维克",
        "code": "002837",
        "price": "55.24",
        "change": "-1.18%",
        "up": False,
        "comment": (
            "<strong>【当日表现】</strong>今日收55.24元，下跌1.18%，成交额19.15亿，换手率继续维持高位。"
            "早盘开56.00元冲高57.10元后回落，最低54.30元，尾盘小幅回升，全天振幅5.0%。"
            "液冷板块今日整体偏弱，AI算力板块分化明显，英维克作为液冷龙头继续承压。<br><br>"
            "<strong>【技术面】</strong>今日收小阴线，再创调整新低54.30元，股价已跌破所有均线系统，"
            "处于典型的下跌趋势中。MACD绿柱仍在扩大，KDJ低位钝化，短期难言见底。"
            "压力位58-60元（5日线+前期低点），支撑位50-52元（心理关口+2025年平台）。"
            "从跌幅看，从高点76元已回调约27%，接近30%的中级调整幅度。<br><br>"
            "<strong>【资金面】</strong>成交19.15亿维持高位，资金持续流出，恐慌抛售仍在延续。"
            "机构出逃迹象明显，短期承接盘不足。北向资金亦在减持。<br><br>"
            "<strong>【操作建议】</strong>谨慎持有，严控仓位。建议：当前仓位控制在20%以内，不再加仓；"
            "反弹至58-60元区间减仓10%；跌破52元止损清仓；若企稳并放量收复60元，可考虑小幅回补。"
            "核心风险：液冷板块短期估值泡沫消化中，AI算力投资节奏可能放缓，需等待板块企稳信号。"
        )
    },
    {
        "name": "*ST建艺",
        "code": "002789",
        "price": "9.75",
        "change": "-0.81%",
        "up": False,
        "comment": (
            "<strong>【当日表现】</strong>今日收9.75元，下跌0.81%，成交额0.28亿，换手率较低。"
            "早盘开9.96元（涨停价附近）后冲高回落，最低9.61元，全天波动不大。"
            "ST板块今日整体偏弱，个股分化严重，*ST建艺作为重组预期标的，走势相对独立。<br><br>"
            "<strong>【技术面】</strong>今日收小阴线，未能延续上周五涨势，在10元整数关前遇阻。"
            "MACD红柱缩短，KDJ高位有死叉迹象，短期面临调整压力。支撑位9.3-9.5元（5日线+前期平台），"
            "压力位10.0-10.2元（整数关口+前期高点）。整体处于上升通道中，回调属于正常调整。<br><br>"
            "<strong>【资金面】</strong>成交0.28亿缩量明显，说明抛压不大，筹码锁定良好。"
            "ST股受限于50万股/日的买入限制，走势相对独立，主要受重组进展消息驱动。<br><br>"
            "<strong>【操作建议】</strong>继续持有，作为组合防御端配置。建议：底仓维持不变，仓位控制在10-15%；"
            "若跌至9.3-9.5元区间可小幅加仓5%；突破10.5元可加仓5%；跌破9元止损（重组预期可能生变）。"
            "核心逻辑：重组预期+摘帽预期，属于事件驱动型机会，需密切关注公告进展。"
        )
    },
]

# 自定义持仓股深度诊断渲染
def render_holdings_detail(holdings_list):
    html = '<div style="display: flex; flex-direction: column; gap: 16px;">'
    for h in holdings_list:
        change_color = "#10b981" if h.get('up', True) else "#ef4444"
        html += f'''
        <div style="background: rgba(30,30,50,0.5); border: 1px solid rgba(255,255,255,0.08);
                   border-radius: 16px; padding: 20px 22px;
                   box-shadow: 0 4px 12px rgba(0,0,0,0.2);">
            <div style="display: flex; align-items: center; margin-bottom: 12px; padding-bottom: 12px; border-bottom: 1px solid rgba(255,255,255,0.06);">
                <div style="flex: 1;">
                    <span style="font-size: 17px; font-weight: 700; color: #f1f5f9;">{h["name"]}</span>
                    <span style="font-size: 13px; color: #9ca3af; margin-left: 10px;">{h.get("code", "")}</span>
                </div>
                <div style="text-align: right;">
                    <div style="font-size: 20px; font-weight: 700; color: {change_color};">{h["price"]}</div>
                    <div style="font-size: 14px; font-weight: 600; color: {change_color};">{h["change"]}</div>
                </div>
            </div>
            <div style="font-size: 13px; color: #cbd5e1; line-height: 1.8;">
                {h["comment"]}
            </div>
        </div>
        '''
    html += '</div>'
    return html

holdings_html = render_holdings_detail(holdings)
holdings_section = Section(title="💼 持仓股深度诊断", content=holdings_html, icon="briefcase")
gen._components.append(holdings_section)

# ============================================================
# 6. 板块涨跌幅排行
# ============================================================
up_sectors = [
    {"name": "兵装重组", "change": "+7.17%"},
    {"name": "地面兵装", "change": "+5.41%"},
    {"name": "医疗服务", "change": "+4.59%"},
    {"name": "贵金属", "change": "+4.54%"},
    {"name": "养殖业", "change": "+4.19%"},
    {"name": "酒店餐饮", "change": "+4.22%"},
    {"name": "有色·钨", "change": "+3.89%"},
    {"name": "CXO概念", "change": "+3.92%"},
    {"name": "白酒", "change": "+2.70%"},
    {"name": "电网设备", "change": "+2.50%"},
]

down_sectors = [
    {"name": "CPO概念", "change": "-5.44%"},
    {"name": "通信设备", "change": "-3.67%"},
    {"name": "保险", "change": "-1.80%"},
    {"name": "PCB/元件", "change": "-1.25%"},
    {"name": "AI手机PC", "change": "-0.96%"},
]

gen.add_sector_performance(up_sectors, down_sectors)

# ============================================================
# 7. 龙虎榜深度解读
# ============================================================
dragon_stocks = [
    {
        "name": "通宇通讯",
        "code": "002792",
        "change": "-8.31%",
        "up": False,
        "institutions": 4,
        "reason": "日跌幅偏离值",
        "net_buy": "机构净买1.70亿",
        "detail": (
            "<strong>核心看点：机构抄底 vs 游资撤退</strong><br>"
            "收盘价34.10元，跌8.31%，成交31.65亿，换手27.16%。4家机构专用席位合计净买入1.70亿元，"
            "深股通净买入6847万元，机构+北向合计净买2.38亿；而营业部游资席位合计净卖出1.62亿。"
            "这是今日龙虎榜机构/外资与短线游资对立最极致的一笔交易，长线资金在深跌中坚定承接，"
            "上海超短和西安量化在坚决撤退。<br><br>"
            "<strong>持续性判断：</strong>机构大幅净买入+暴跌的结构，历史上往往意味着机构认为当前价位已进入价值区间，"
            "但短线情绪修复需要时间。后续关注34元能否企稳，若企稳则可能形成阶段性底部，"
            "目标反弹位38-40元；若继续破位下行则需警惕机构止损。"
        )
    },
    {
        "name": "百普赛斯",
        "code": "301080",
        "change": "+20.00%",
        "up": True,
        "institutions": 4,
        "reason": "日涨幅达20%",
        "net_buy": "机构净卖4430万",
        "detail": (
            "<strong>核心看点：机构涨停兑现，游资北向接力</strong><br>"
            "收盘价77.70元，20CM涨停，成交22.65亿，换手23.31%。4家机构专用席位合计净卖出4430.74万元，"
            "深股通净买入3910万元，国新证券北京分公司净买9315万，招商证券深圳益田路净买4482万。"
            "卖一席位中金上海分公司净卖1.22亿元。典型的机构逢高兑现、游资和北向接力的结构。<br><br>"
            "<strong>持续性判断：</strong>CXO板块整体超跌反弹，百普赛斯作为弹性标的领涨。"
            "但机构在涨停板上果断减仓，意味着筹码在高位完成交换。后续走势关键看游资接力能否持续，"
            "机构抛压能否消化。短期关注75-80元区间能否站稳，若能站稳则看高至90元；"
            "若明日大幅低开则可能形成短期高点。"
        )
    },
    {
        "name": "翔鹭钨业",
        "code": "002842",
        "change": "+10.01%",
        "up": True,
        "institutions": 4,
        "reason": "日涨幅偏离值",
        "net_buy": "游资净买2.24亿",
        "detail": (
            "<strong>核心看点：游资共识最强，知春路主导涨停</strong><br>"
            "收盘价42.22元，涨停，成交25.35亿，换手24.15%，振幅12.17%。国泰海通北京知春路净买1.19亿元，"
            "开源证券西安太华路净买1.05亿元，两家活跃游资合计净买2.24亿。深股通几乎平手（净卖671万），"
            "4家机构席位合计净卖出150.49万元，分歧较小。4天2板，成为有色·钨板块的情绪龙头。<br><br>"
            "<strong>持续性判断：</strong>游资主导的品种，情绪驱动为主。钨价上涨+小金属板块轮动+有色行情扩散，"
            "多重逻辑叠加。知春路席位以短线打板著称，次日溢价概率较高，但连板难度较大。"
            "关注明日能否突破45元压力位，若放量突破则有望挑战50元；若高开低走则注意游资出货风险。"
        )
    },
]

# 自定义龙虎榜渲染
def render_dragon_tiger_detail(stocks_list):
    html = '<div style="display: flex; flex-direction: column; gap: 16px;">'
    for s in stocks_list:
        change_color = "#10b981" if s.get('up', True) else "#ef4444"
        inst_html = f'<span style="font-size: 12px; color: #f59e0b; margin-left: 10px;">🏛️ {s.get("institutions", 0)}家机构</span>' if s.get('institutions', 0) > 0 else ''
        html += f'''
        <div style="background: rgba(30,30,50,0.5); border: 1px solid rgba(255,255,255,0.08);
                   border-radius: 16px; padding: 18px 20px;">
            <div style="display: flex; align-items: center; margin-bottom: 10px; padding-bottom: 10px; border-bottom: 1px solid rgba(255,255,255,0.06);">
                <div style="flex: 1;">
                    <span style="font-size: 16px; font-weight: 700; color: #f1f5f9;">{s["name"]}</span>
                    <span style="font-size: 12px; color: #9ca3af; margin-left: 8px;">{s.get("code", "")}</span>
                    {inst_html}
                </div>
                <span style="font-size: 18px; font-weight: 700; color: {change_color};">{s.get("change", "")}</span>
            </div>
            <div style="display: flex; gap: 20px; font-size: 12px; color: #94a3b8; margin-bottom: 12px;">
                <span>上榜原因：{s.get("reason", "")}</span>
                <span>净买卖：{s.get("net_buy", "")}</span>
            </div>
            <div style="font-size: 13px; color: #cbd5e1; line-height: 1.8;">
                {s["detail"]}
            </div>
        </div>
        '''
    html += '</div>'
    return html

dragon_html = render_dragon_tiger_detail(dragon_stocks)
dragon_section = Section(title="🐉 龙虎榜深度解读", content=dragon_html, icon="award")
gen._components.append(dragon_section)

# ============================================================
# 8. 重点关注标的
# ============================================================
watch_stocks_html = '''
<div style="display: flex; flex-direction: column; gap: 16px;">
    <div style="background: linear-gradient(135deg, rgba(16,185,129,0.1) 0%, rgba(6,182,212,0.05) 100%); 
                border: 1px solid rgba(16,185,129,0.3); border-radius: 16px; padding: 18px 20px;">
        <div style="display: flex; align-items: center; margin-bottom: 10px;">
            <span style="font-size: 16px; font-weight: 700; color: #10b981;">风华高科 000636</span>
            <span style="margin-left: auto; font-size: 13px; font-weight: 600; color: #10b981;">+5.85%</span>
        </div>
        <div style="font-size: 13px; color: #cbd5e1; line-height: 1.8;">
            <strong>关注逻辑：</strong>今日龙虎榜净买入4.20亿居首，机构净买入1216.55万。
            国内MLCC龙头，受益于消费电子复苏+汽车电子高增长+国产替代三重逻辑。
            前期调整充分，估值处于历史低位，机构资金开始左侧布局。<br>
            <strong>目标价：</strong>第一目标70元，第二目标78元<br>
            <strong>止损位：</strong>跌破56元止损（今日收盘61.70元）<br>
            <strong>建议仓位：</strong>5-8%，分批建仓
        </div>
    </div>
    
    <div style="background: linear-gradient(135deg, rgba(251,146,60,0.1) 0%, rgba(239,68,68,0.05) 100%); 
                border: 1px solid rgba(251,146,60,0.3); border-radius: 16px; padding: 18px 20px;">
        <div style="display: flex; align-items: center; margin-bottom: 10px;">
            <span style="font-size: 16px; font-weight: 700; color: #fb923c;">立新能源 001258</span>
            <span style="margin-left: auto; font-size: 13px; font-weight: 600; color: #ef4444;">+10.03% 涨停</span>
        </div>
        <div style="font-size: 13px; color: #cbd5e1; line-height: 1.8;">
            <strong>关注逻辑：</strong>今日涨停，龙虎榜机构净买入3716.93万，深股通净买入2468.84万，
            机构+北向共同做多。上半年净利润同比增长715.75%，业绩爆发式增长。
            新能源+储能+风电多重概念叠加，小盘股弹性大。近半年上榜11次，上榜次日平均涨4.38%，
            上榜后5日平均涨7.42%，历史胜率较高。<br>
            <strong>目标价：</strong>第一目标16.5元，第二目标18元<br>
            <strong>止损位：</strong>跌破13元止损<br>
            <strong>建议仓位：</strong>3-5%，追高需谨慎，建议回踩5日线介入
        </div>
    </div>
    
    <div style="background: linear-gradient(135deg, rgba(168,85,247,0.1) 0%, rgba(139,92,246,0.05) 100%); 
                border: 1px solid rgba(168,85,247,0.3); border-radius: 16px; padding: 18px 20px;">
        <div style="display: flex; align-items: center; margin-bottom: 10px;">
            <span style="font-size: 16px; font-weight: 700; color: #a855f7;">毕得医药 688073</span>
            <span style="margin-left: auto; font-size: 13px; font-weight: 600; color: #ef4444;">+20% 涨停</span>
        </div>
        <div style="font-size: 13px; color: #cbd5e1; line-height: 1.8;">
            <strong>关注逻辑：</strong>今日20CM涨停，龙虎榜机构净买入1988.25万，北向资金净买入2652.5万，
            机构+北向双双加仓。CXO板块超跌反弹龙头之一，分子砌块/试剂CDMO细分领域龙头，
            业绩持续高增长。药明康德美国诉讼胜诉提振CXO板块情绪，板块整体估值修复空间大。<br>
            <strong>目标价：</strong>第一目标130元，第二目标150元<br>
            <strong>止损位：</strong>跌破100元止损<br>
            <strong>建议仓位：</strong>3-5%，CXO板块超跌反弹逻辑，注意控制节奏
        </div>
    </div>
</div>
'''

watch_section = Section(title="🎯 重点关注标的", content=watch_stocks_html, icon="target")
gen._components.append(watch_section)

# ============================================================
# 9. 晚间重要新闻
# ============================================================
evening_news = [
    {
        "title": "央行：持续实施适度宽松的货币政策，7月CPI同比+0.5%",
        "content": "央行强调若经济需要，随时出台增量流动性工具。7月CPI同比上涨0.5%，PPI涨价放缓，市场无收紧担忧。宽松货币环境为A股提供流动性支撑。",
        "time": "2026-08-10 18:30",
        "source": "央行官网",
        "tag": "政策",
        "tag_variant": "primary"
    },
    {
        "title": "甘李药业：与Menarini签署6.64亿欧元GLP-1授权协议",
        "content": "甘李药业授予Menarini博凡格鲁肽超重/肥胖适应症独家许可，首付款6200万欧元，里程碑累计最高6.64亿欧元。创新药出海再添重磅案例。",
        "time": "2026-08-10 19:15",
        "source": "公司公告",
        "tag": "医药",
        "tag_variant": "success"
    },
    {
        "title": "药明康德：美国法院批准初步禁令，挑战1260H认定胜诉",
        "content": "美国哥伦比亚特区联邦地区法院批准药明康德所申请的初步禁令，使公司在挑战1260H认定的司法程序期间免受该认定带来的即时不利影响。CXO板块情绪重大利好。",
        "time": "2026-08-10 07:00",
        "source": "公司公告",
        "tag": "医药",
        "tag_variant": "success"
    },
    {
        "title": "证监会发布内地与香港资本市场10项合作举措",
        "content": "拓宽港股通、ETF互联互通渠道，利好港股科技、AH溢价偏低龙头。南向资金持续活跃，港股通指数今日涨1.12%。",
        "time": "2026-08-10 16:00",
        "source": "证监会",
        "tag": "政策",
        "tag_variant": "primary"
    },
    {
        "title": "金价站上4416美元创历史新高，美元指数跌破100",
        "content": "国际金价突破4416美元/盎司创历史新高，上海金报944.67元/克涨1.53%。美元指数跌破100至99.64，20日跌1.64%。通胀预期+地缘风险+美元走弱三重支撑。",
        "time": "2026-08-10 15:30",
        "source": "财联社",
        "tag": "贵金属",
        "tag_variant": "warning"
    },
]

gen.add_evening_news(evening_news)

# ============================================================
# 10. 业绩预增追踪
# ============================================================
gen.add_earnings_forecast()

# ============================================================
# 11. 明日关键预判
# ============================================================
predictions = [
    {
        "name": "上证指数",
        "direction": "震荡",
        "confidence": 65,
        "reason": "沪指5连阳后逼近4000点关口，短期有震荡整固需求。关注3950点支撑，上方压力位4000点整数关口。量能若继续萎缩需警惕调整风险，若放量则有望挑战4000点。"
    },
    {
        "name": "创业板指",
        "direction": "看涨",
        "confidence": 55,
        "reason": "创业板今日盘中跌超2.5%后尾盘大幅收窄，留下长下影线，3470点支撑经受住考验。科技股尾盘回补力度较强，明日有望延续超跌反弹，但趋势性反转尚需观察。关注3500点支撑和3600点压力。"
    },
    {
        "name": "半导体/先进封装",
        "direction": "看涨",
        "confidence": 70,
        "reason": "今日半导体尾盘大幅拉升，雅克科技+4.34%领涨。长鑫科技纳入MSCI、中芯国际明日盘后发财报两大事件催化。板块前期调整充分，机构资金回补明显，明日有望延续反弹。"
    },
    {
        "name": "CPO/光模块",
        "direction": "看跌",
        "confidence": 65,
        "reason": "今日CPO板块领跌，光迅科技触及跌停，中际旭创、新易盛跌超5%，通宇通讯跌8.31%。机构高位派发迹象明显，获利盘兑现压力仍大，短期调整尚未结束，暂不建议抄底。"
    },
    {
        "name": "医药/CXO",
        "direction": "看涨",
        "confidence": 75,
        "reason": "药明康德美国诉讼胜诉+板块超跌反弹双重催化，百花医药5连板、百普赛斯20CM涨停，机构资金回补明显。CXO板块估值处于历史低位，业绩确定性强，反弹趋势有望延续。"
    },
]

gen.add_tomorrow_prediction(predictions)

# ============================================================
# 12. 风险提示
# ============================================================
risks = [
    "科技股高位回调风险：CPO、光模块等前期热门赛道机构高位派发，短期调整压力仍存，可能带动科技板块进一步分化",
    "沪指4000点关口压力：沪指5连阳后逼近4000点整数关口，量能有所萎缩，若不能放量突破可能面临阶段性回调",
    "海外市场波动风险：本周美国7月CPI数据公布在即，若通胀超预期可能引发美联储加息预期升温，影响全球风险资产",
    "北向资金转向风险：8月以来北向资金累计净流入超600亿，外资在当前高位区域趋于谨慎，若转为净流出可能加剧市场波动",
    "中报业绩不及预期风险：中报季进入密集披露期，部分高位成长股若业绩不及预期，可能引发估值下杀",
]

gen.add_risk_warning(risks)

# ============================================================
# 13. 明日操作计划
# ============================================================
trading_plan = """
<h3 style="color: #f1f5f9; margin-bottom: 12px;">📊 大盘判断</h3>
<p>明日A股预计震荡整固，结构性行情延续。沪指关注3950-4000点区间，创业板关注3500-3600点区间。
量能若维持在2.3万亿以上则市场活跃度尚可，若跌破2.2万亿需警惕调整风险。
整体仓位建议控制在6-7成，高低切换背景下不宜过度追高。</p>

<h3 style="color: #f1f5f9; margin: 20px 0 12px 0;">💼 持仓操作计划</h3>

<p><strong>1. 铜冠铜箔（301217）—— 持有，反弹减仓</strong><br>
今日+4.47%领涨，短期反弹趋势确立。操作计划：底仓70%继续持有，
明日若冲高至125-128元区间减仓20%锁定利润；若回踩115元附近不破可加仓20%做T；
跌破110元止损离场。核心逻辑：HBM铜箔需求增长确定性高，短期反弹至压力位注意兑现。</p>

<p><strong>2. 雅克科技（002409）—— 持有，分批减仓</strong><br>
今日+4.34%强势反弹，半导体材料板块尾盘回补力度大。操作计划：底仓60%持有，
明日若冲至160-165元区间减仓30%；回踩148-150元区间不破可加仓20%；
跌破140元止损。核心逻辑：HBM前驱体国产替代逻辑不变，短期跟随板块反弹，中期看业绩兑现。</p>

<p><strong>3. 英维克（002837）—— 谨慎，严控仓位</strong><br>
今日-1.18%续创新低，液冷板块仍处弱势。操作计划：当前仓位控制在20%以内，不再加仓；
反弹至58-60元区间减仓10%；跌破52元果断止损清仓；
若企稳并放量收复60元，可考虑小幅回补5-10%。核心风险：液冷估值泡沫消化中，需等待板块企稳信号。</p>

<p><strong>4. *ST建艺（002789）—— 持有，防御配置</strong><br>
今日-0.81%缩量调整，筹码锁定良好。操作计划：底仓维持不变（10-15%）；
若跌至9.3-9.5元区间可小幅加仓5%；突破10.5元加仓5%；跌破9元止损（重组预期可能生变）。
核心逻辑：重组+摘帽预期，事件驱动型机会，密切关注公告进展。</p>

<h3 style="color: #f1f5f9; margin: 20px 0 12px 0;">🎯 新开仓计划</h3>
<p><strong>关注标的：风华高科（000636）</strong><br>
龙虎榜机构净买入居首，MLCC龙头+消费电子复苏+国产替代。
买入区间：60-62元（回踩5日线附近）；目标价：70元（第一目标）；止损位：56元；仓位：5-8%。</p>

<p><strong>关注标的：毕得医药（688073）</strong><br>
CXO超跌反弹，机构+北向双双加仓。买入区间：105-110元（回踩10日线附近）；
目标价：130元（第一目标）；止损位：100元；仓位：3-5%。</p>

<h3 style="color: #f1f5f9; margin: 20px 0 12px 0;">⚠️ 重点观察</h3>
<p>1. 沪指4000点关口能否放量突破<br>
2. 创业板3500点支撑是否有效<br>
3. CPO/光模块板块能否止跌企稳<br>
4. 中芯国际明日盘后财报对半导体板块的影响<br>
5. 美国7月CPI数据（周三晚间公布）</p>
"""

gen.add_trading_plan(trading_plan)

# ============================================================
# 发布报告
# ============================================================
print("正在生成盘后速递报告...")
result = gen.publish(
    title="2026.08.10 盘后速递",
    report_type="aftermarket",
    excerpt="沪指5连阳逼近4000点，科技股探底回升，铜冠铜箔+4.47%雅克科技+4.34%领涨持仓",
    auto_deploy=False
)
print(f"发布结果: {result}")
if isinstance(result, dict):
    print(f"文件路径: {result.get('filepath', 'N/A')}")
