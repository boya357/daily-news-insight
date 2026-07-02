#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""盘后速递生成脚本 - 2026-07-02（补跑）"""
import sys, os, json
sys.path.insert(0, '/root/daily-news-insight')
os.chdir('/root/daily-news-insight')

from v3.generators.aftermarket import AftermarketGenerator
from v3.components.layout import Section

with open('data/market.json', 'r', encoding='utf-8') as f:
    market = json.load(f)
with open('data/portfolio.json', 'r', encoding='utf-8') as f:
    portfolio = json.load(f)
with open('data/longhubang_market.json', 'r', encoding='utf-8') as f:
    lhb = json.load(f)

DATE = "20260702"
subtitle = "2026年7月2日 · 费半暴跌传导A股血洗科技，沪指-2.03%、创业板-5.71%、科创50-7.70%创年内最大跌幅"

gen = AftermarketGenerator(date_str=DATE, subtitle=subtitle)

gen.add_today_highlight(
    "💥 费半暴跌-6.27%（年内最大单日跌幅之一）的黑天鹅在A股全面传导！沪指-2.03%报4028.9点跌破20日线，"
    "创业板-5.71%创15个月最大单日跌幅、科创50-7.70%创年内最大跌幅报1987.29点。"
    "两市成交3.45万亿缩量2095亿，半导体/CPO/算力硬件遭史诗级抛售：北方华创、兆易创新、雅克科技等多只龙头跌停，"
    "芯片板块单日主力净流出超800亿。资金大逃亡避险资产：贵金属涨停潮（赤峰黄金、招金黄金）、人形机器人逆势走强（31家涨停）、"
    "银行/医药/中报预增抱团。🚨持仓两大核心铜冠铜箔-4.20%、雅克科技-10%跌停（公司澄清无六氟化钨+含氟特气仅5.79%），"
    "英维克-4.46%续创新低，*ST建艺-1.75%逼近11.79元。晚20:30美国6月非农仅增5.7万人远低于预期11.3万，"
    "黄金暴力拉涨破4140美元、美股期指反弹降息预期重燃，明日A股有望迎来喘息修复。"
)

indices_data = []
for idx in market['indices']:
    change_pct = idx['change_pct'] * 100
    sign = '+' if change_pct >= 0 else ''
    indices_data.append({
        'name': idx['name'],
        'value': f"{idx['price']:.2f}",
        'change': f"{sign}{change_pct:.2f}%",
        'up': idx['up'],
        'icon': 'trending_up' if idx['up'] else 'trending_down'
    })
gen.add_market_summary(
    indices=indices_data,
    volume="3.45万亿（缩量2095亿）",
    northbound="净流出约120亿（科技卖压）"
)

gen.add_sentiment_thermometer(
    temperature=22,
    volume="3.45万亿",
    up_count="2219只↑",
    down_count="3162只↓",
    limit_up_count=156
)

up_sectors = [
    {"name": "贵金属/黄金", "change": "+5.87%"},
    {"name": "人形机器人/具身智能", "change": "+2.14%"},
    {"name": "银行", "change": "+1.23%"},
    {"name": "医药/创新药", "change": "+0.21%"},
    {"name": "煤炭", "change": "+1.60%"},
    {"name": "纺织服饰", "change": "+1.58%"},
    {"name": "中报预增", "change": "+3.74%"},
]
down_sectors = [
    {"name": "通信/CPO/光模块", "change": "-7.36%"},
    {"name": "电子/半导体", "change": "-7.15%"},
    {"name": "半导体设备", "change": "-9.93%"},
    {"name": "光刻机", "change": "-5.69%"},
    {"name": "存储芯片", "change": "-5.67%"},
    {"name": "算力租赁/PCB", "change": "-5%~-6%"},
    {"name": "玻璃基板", "change": "-9.93%"},
]
gen.add_sector_performance(up_sectors=up_sectors, down_sectors=down_sectors)

strong_sectors = [
    {"name": "贵金属/黄金（避险主线）", "reason": "费半暴跌+非农爆冷+降息预期重燃三重催化，黄金直线拉升破4140美元涨超2.37%，赤峰黄金、招金黄金涨停，山金国际、东方锆业、翔鹭钨业涨超7%。资金系统性避险配置，小金属锆/钨/稀土跟涨，黄河旋风金刚石概念首板获主力净流入10.48亿居全市场第一。"},
    {"name": "人形机器人/具身智能（逆势独立主线）", "reason": "上海国际具身智能博览会开幕日（7/2-4）逆势爆发31家涨停！板块指数虽跌但梯队完整：锋龙股份3天2板、富春染织2连板、宏昌科技20cm首板、宏德股份/雷利电机/柯力传感批量涨停；汇川技术主力净流入4.16亿为机械板块第一，绿的谐波/双环传动/三花智控/拓斯达核心零部件全线活跃。产业逻辑从题材进入订单兑现，是今日唯一抗跌科技方向。"},
    {"name": "中报预增+低位价值（业绩防御主线）", "reason": "中报预增概念+3.74%居概念板块前列，海南海药8天6板领涨；银行板块+1.23%（成都银行/南京银行/江苏银行涨超2%），煤炭+1.6%，纺织服饰+1.58%（欣龙控股/华升股份涨停）。市场从「炒预期」彻底转向「看兑现」，低位低估值+业绩确定性成为资金避风港。"},
    {"name": "ST板块（新规博弈）", "reason": "7/6 ST涨跌幅扩至10%倒计时3天，ST板块整体+2.23%，59家ST涨停，*ST瑞茂、ST海龙、ST际华涨停，ST银江+13.26%。典型的新规前「末日博弈」，但*ST建艺逆市下跌-1.75%警示风险。"},
]
weak_sectors = [
    {"name": "半导体/存储/设备（费半暴跌直接传导）", "reason": "费半-6.27%年内最大单日跌幅在A股全面兑现：①半导体设备龙头北方华创、华海清科、中科飞测、富创精密、华峰测控、金海通批量跌停，长川科技/中微公司跌超11%；②存储芯片兆易创新跌停，佰维存储、江波龙、澜起科技跌超7%，板块单日主力净流出超800亿；③持仓雅克科技跌停-10%报212.48元（龙虎榜主力净卖5.25亿+机构兑现+澄清无六氟化钨三重打击）；④铜冠铜箔-4.20%报157.92元（主力净卖5.84亿），HVLP铜箔逻辑短期遭抛售。"},
    {"name": "CPO/光通信/算力硬件", "reason": "通信板块-7.36%居跌幅榜首：光迅科技、长芯博创、新易盛、剑桥科技、天孚通信跌停或跌超10%，华工科技主力净流出21.65亿居两市第一，中际旭创-5%以上。费半暴跌+Meta拟出售过剩AI算力被解读为CAPEX见顶，光模块/算力硬件上半年涨幅80-250%机构集中兑现。"},
    {"name": "PCB/电子化学品/玻璃基板", "reason": "东山精密跌停-10%，玻璃基板板块-9.93%接近全板块跌停，电子化学品板块跌幅居前。科技硬件产业链从上游材料到下游应用全线遭抛售，神工股份/江丰电子/新莱应材/赛腾股份等跌停或跌超9%。"},
    {"name": "高位AI算力/液冷（持仓英维克）", "reason": "英维克-4.46%续创新低71.4元（最低69.80元），成交37.9亿放量下跌，主力净流出2.1亿，连续5日主力净流出累计21.25亿、5日跌幅-17.92%，深度破止损-31.5%；同类申菱环境-2.15%、高澜股份、冰轮环境（-7.30%）等液冷温控链全线走弱，AI算力硬件需求放缓预期直接冲击。"},
]
core_view = (
    "7月2日是A股7月「验牌月」的第一次大考，市场给出了极为惨烈的答卷。暴跌的本质是三重利空共振："
    "①隔夜费半-6.27%（年内最大单日跌幅之一），导火索是Meta拟出售过剩AI算力被市场解读为AI CAPEX见顶信号，美光/闪迪-10%以上、科磊-11.77%、拉姆研究-9.71%，"
    "上半年涨幅80-250%的海外半导体龙头集中兑现；"
    "②国内科技股经历7/1的高低切换第一天后，7/2进入「多杀多」踩踏——北方华创、兆易创新等高位科技龙头跌停，"
    "芯片板块单日主力净流出超800亿，融资盘被动平仓+量化止损形成负反馈；"
    "③今晚20:30公布的美国6月非农仅增5.7万人（预期11.3万、前值17.2万），爆冷数据在A股收盘后公布，"
    "市场白天处于「等待数据避险」状态，资金提前撤离风险资产。"
    "关键信号：①人形机器人/具身智能31家涨停独立于科技暴跌，说明市场并非没有主线，而是从「算力硬件」切到「具身智能/AI应用」；"
    "②黄金/银行/中报预增等防御方向全线走强，避险情绪升温；③龙虎榜显示顶级游资并未大幅出逃科技，"
    "今日是机构集中兑现+融资盘强平，散户筹码松动。"
    "持仓方面：雅克科技跌停-10%为最大打击，需重新评估HBM材料逻辑在CAPEX见顶担忧下的持续性；"
    "铜冠铜箔-4.20%相对抗跌，HVLP铜箔长期逻辑未破但短期需观察存储板块企稳信号；"
    "英维克-4.46%继续破位，必须执行减仓纪律；*ST建艺-1.75%在ST板块集体涨停日逆市走弱，7/6前必须清仓。"
    "非农爆冷后黄金暴涨4140+、美股期指拉升0.7%、降息预期重燃，明日（7/3周五）A股有望迎来超跌反弹修复，但反弹是逃命波而非反转——"
    "科技股需等费半企稳+中报业绩验证后才能重新介入。"
)
gen.add_market_deep_analysis(
    strong_sectors=strong_sectors,
    weak_sectors=weak_sectors,
    core_view=core_view
)

lhb_overview_html = '''
<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:14px;margin-bottom:14px;">
    <div style="background: linear-gradient(135deg, #fef2f2 0%, #fee2e2 100%); border-radius:12px;padding:16px;border:1px solid rgba(239,68,68,0.2);">
        <div style="font-size:14px;font-weight:700;color:#991b1b;margin-bottom:8px;">🔴 机构动向</div>
        <div style="font-size:13px;color:#7f1d1d;line-height:1.8;">
            <strong>科技板块机构集中出逃</strong>：半导体/CPO板块机构净卖出超百亿，雅克科技单日主力净卖5.25亿、铜冠铜箔主力净卖5.84亿、华工科技主力净流出21.65亿居两市第一。<br>
            <strong>逆势流入</strong>：黄河旋风（金刚石/超硬材料）主力净流入10.48亿居全市场第一，赤峰黄金净流入4.52亿，汇川技术（机器人）净流入4.16亿。
        </div>
    </div>
    <div style="background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%); border-radius:12px;padding:16px;border:1px solid rgba(245,158,11,0.2);">
        <div style="font-size:14px;font-weight:700;color:#92400e;margin-bottom:8px;">🎯 游资核心动向</div>
        <div style="font-size:13px;color:#78350f;line-height:1.8;">
            <strong>机器人抱团</strong>：锋龙股份3天2板、富春染织2连板，汇川技术/锋龙股份获顶级游资介入；<br>
            <strong>ST新规博弈</strong>：59家ST涨停系7/6涨跌幅扩至10%前末日博弈；<br>
            <strong>黄金/资源</strong>：赤峰黄金、招金黄金涨停，小金属锆/钨跟涨，避险资金入场。
        </div>
    </div>
</div>
'''
gen._components.append(Section(title="🐉 龙虎榜综述", content=lhb_overview_html, icon="award"))

lhb_stocks = [
    {"name": "黄河旋风", "code": "600172", "change": "+10.02%", "up": True, "reason": "金刚石/超硬材料/首板/主力净买10.48亿居全市第一", "net_buy": "10.48亿", "institutions": 1},
    {"name": "汇川技术", "code": "300124", "change": "+0.77%", "up": True, "reason": "人形机器人龙头/主力净买4.16亿/机构逆势加仓", "net_buy": "4.16亿", "institutions": 1},
    {"name": "赤峰黄金", "code": "600988", "change": "+10.01%", "up": True, "reason": "贵金属龙头/避险/主力净买4.52亿/黄金破4140", "net_buy": "4.52亿", "institutions": 1},
    {"name": "海南海药", "code": "000566", "change": "+10.03%", "up": True, "reason": "8天6板/创新药/医保商保谈判/主力净买2.17亿", "net_buy": "2.17亿", "institutions": 1},
    {"name": "雅克科技", "code": "002409", "change": "-10.00%", "up": False, "reason": "跌停/HBM前驱体/持仓股/澄清无六氟化钨/主力净卖5.25亿", "net_buy": "主力净卖5.25亿", "institutions": 0},
    {"name": "铜冠铜箔", "code": "301217", "change": "-4.20%", "up": False, "reason": "HVLP铜箔/持仓股/存储大跌拖累/主力净卖5.84亿", "net_buy": "主力净卖5.84亿", "institutions": 0},
]
gen.add_dragon_tiger_list(lhb_stocks)

portfolio_advice_update = {
    "002837": {"type": "reduce", "type_label": "🔴 坚决清仓", "color": "red",
        "text": "英维克-4.46%收71.4元，最低69.80元续创新低，连续5日主力净流出累计21.25亿、5日跌幅-17.92%。深度破止损-31.5%（成本104.23），AI算力CAPEX见顶担忧下液冷温控逻辑动摇。7月2日已出现大宗交易71.4元折价成交（机构卖机构），反弹即是逃命窗口。建议明日（7/3）任何反弹至73-75区间坚决清仓，下破70元无条件离场，禁止补仓摊低成本。"},
    "301217": {"type": "hold", "type_label": "🟡 减仓锁利", "color": "orange",
        "text": "铜冠铜箔-4.20%收157.92元，主力净卖5.84亿元，受存储板块暴跌（兆易创新跌停、费半-6.27%）拖累。但HVLP铜箔受益HBM封装长期逻辑未破（三星/SK海力士4万亿韩元扩产+SK海力士7/10美股上市），相对半导体设备/光模块-7%以上跌幅相对抗跌。建议：①160-165区间减仓1/3锁利（当前浮盈+81.2%）；②剩余底仓移动止盈上移至155元，跌破150元再减1/3；③等待存储板块企稳（费半止跌+中报验证）后再决策是否回补。"},
    "002409": {"type": "hold", "type_label": "🟠 紧急评估", "color": "orange",
        "text": "雅克科技-10%跌停收212.48元（成交91.87亿天量+主力净卖5.25亿），三重打击：①隔夜费半暴跌存储/半导体设备链全线崩盘传导；②公司连续两日发风险公告澄清「无六氟化钨业务、含氟特气仅占营收5.79%、市场对电子业务过度解读」；③机构从7/1净买2.82亿转为今日净卖5.25亿，筹码大幅松动。【双重验证】：公司澄清属于「股价异动标准监管模板」（近3日累计偏离20%+强制披露），并非实质性利空，但「过度解读」的措辞表明公司认为当前估值包含过多HBM预期。建议：①底仓保留1/2观察，等待210-220区间企稳信号；②反弹至225-230减仓1/3锁利（当前浮盈+103.8%）；③跌破200元必须减仓至1/4以下，防范中报业绩不及预期的戴维斯双杀。"},
    "002789": {"type": "sell", "type_label": "🔴 必须清仓", "color": "red",
        "text": "*ST建艺-1.75%收11.79元，在ST板块59家涨停的背景下逆市下跌（主力净流出275万），说明资金并不认可其投机价值。7/6（周一）ST涨跌幅正式扩至10%，剩余最后1个交易日（7/3周五），7/3是最后离场窗口！扩幅后：单日跌停-10%，两日最大亏19%；公司Q1营收同比-35%、归母净亏5311万、负债率94.38%，基本面无改善。纪律：7/3开盘任何价格必须清仓，不挂单等反弹，不留1股。"}
}

stocks_html = '<div style="display: flex; flex-direction: column; gap: 14px;">'
for s in portfolio.get('stocks', []):
    change = s.get('today_change', 0) * 100
    sign = '+' if change >= 0 else ''
    change_color = '#10b981' if change < 0 else '#ef4444'
    price = s.get('current_price', 0)
    cost = s.get('cost_price', 0)
    pnl = (price - cost) / cost * 100
    pnl_sign = '+' if pnl >= 0 else ''
    pnl_color = '#ef4444' if pnl >= 0 else '#10b981'
    code = s.get('code', '')
    advice = portfolio_advice_update.get(code, s.get('advice', {}))
    advice_color_map = {'red': '#ef4444', 'orange': '#f97316', 'green': '#10b981'}
    advice_color = advice_color_map.get(advice.get('color', 'red'), '#ef4444')
    if code == "002837":
        risk_level = "高危区 - 深度破止损-31.5%"; risk_color = '#ef4444'
    elif code == "002409":
        risk_level = "警示区 - 跌停破位"; risk_color = '#f97316'
    elif code == "301217":
        risk_level = "安全区 - 大幅浮盈+81%"; risk_color = '#10b981'
    else:
        risk_level = "高危区 - 必须清仓"; risk_color = '#ef4444'
    stocks_html += f'''
    <div style="background: rgba(255,255,255,0.7); backdrop-filter: blur(10px); border-radius: 14px; padding: 18px; border: 1px solid rgba(0,0,0,0.06);">
        <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 10px;">
            <div>
                <span style="font-size: 17px; font-weight: 700; color: #1f2937;">{s['name']}</span>
                <span style="font-size: 12px; color: #9ca3af; margin-left: 6px;">{s['code']}</span>
                <span style="font-size: 11px; padding: 2px 8px; border-radius: 10px; background: {risk_color}22; color: {risk_color}; margin-left: 8px;">{risk_level}</span>
            </div>
            <div style="text-align: right;">
                <div style="font-size: 20px; font-weight: 800; color: {change_color};">{sign}{change:.2f}%</div>
                <div style="font-size: 12px; color: #9ca3af;">{price:.2f}元</div>
            </div>
        </div>
        <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 8px; margin-bottom: 12px;">
            <div style="text-align: center; padding: 8px; background: #f8fafc; border-radius: 8px;">
                <div style="font-size: 11px; color: #9ca3af;">成本</div>
                <div style="font-size: 14px; font-weight: 600; color: #374151;">{cost:.2f}元</div>
            </div>
            <div style="text-align: center; padding: 8px; background: #f8fafc; border-radius: 8px;">
                <div style="font-size: 11px; color: #9ca3af;">浮动盈亏</div>
                <div style="font-size: 14px; font-weight: 600; color: {pnl_color};">{pnl_sign}{pnl:.2f}%</div>
            </div>
            <div style="text-align: center; padding: 8px; background: #f8fafc; border-radius: 8px;">
                <div style="font-size: 11px; color: #9ca3af;">止损位</div>
                <div style="font-size: 14px; font-weight: 600; color: #374151;">{s.get('stop_loss_price', 0):.2f}元</div>
            </div>
        </div>
        <div style="background: {advice_color}11; border-left: 3px solid {advice_color}; padding: 10px 14px; border-radius: 0 8px 8px 0; font-size: 13px; color: #374151; line-height: 1.6;">
            <strong style="color: {advice_color};">{advice.get('type_label', '')}：</strong>{advice.get('text', '')}
        </div>
    </div>'''
stocks_html += '</div>'
gen._components.append(Section(title="💼 持仓股追踪", content=stocks_html, icon="briefcase"))

evening_news = [
    {"title": "💥 美国6月非农就业仅增5.7万人，远低于预期11.3万，爆冷数据降息预期重燃", "content": "美国劳工部7月2日20:30公布：6月非农新增就业5.7万人（预期11.3万、前值17.2万大幅下修），失业率4.2%（前值4.3%）。数据公布后：现货黄金直线拉升破4120-4140美元日内涨超2.37%、现货白银涨超4%；美股三大期指短线拉升0.3-0.7%（纳指期货+0.71%）；10年期美债收益率下行；市场重新定价美联储9月降息概率大幅提升。对A股：明日科技股有望迎来喘息修复，但中期需警惕美国经济硬着陆风险。", "time": "20:30", "source": "美国劳工部/财联社", "tag": "宏观S级", "tag_variant": "danger"},
    {"title": "🔥 费城半导体指数暴跌-6.27%，Meta拟出售过剩AI算力引发CAPEX见顶恐慌", "content": "隔夜（7/1晚）费城半导体指数暴跌-6.27%创年内最大单日跌幅：科磊-11.77%、应用材料-9.97%、拉姆研究-9.71%、美光-10.57%、闪迪-10.62%、英特尔-9.03%、AMD-6.89%、台积电ADR-7.01%、康宁-13.61%。导火索：Meta计划对外出售过剩AI算力资源，市场解读为北美云厂商CAPEX见顶信号；叠加美联储沃什鹰派讲话+半年报机构集中兑现+韩国监管拟限制三星/SK海力士杠杆ETF。中概金龙指数逆势+2.93%，拼多多大涨8%。", "time": "04:30", "source": "财联社/美股收盘", "tag": "海外S级", "tag_variant": "danger"},
    {"title": "⚠️ 雅克科技再度发风险公告：无六氟化钨业务，含氟类特种气体营收占比仅5.79%", "content": "公司7月1日晚发布股票交易异常波动公告：①公司既没有六氟化钨相关业务，也没有布局计划；②含氟类特种气体营收占比仅5.79%；③短期内部分市场观点对公司电子业务发展存在过度解读和过高预期。7月2日公司股价一字跌停-10%报212.48元，成交91.87亿天量。【双重验证】该公告属于《深交所股票交易异常波动》监管模板（连续3日偏离20%强制披露），并非主动释放利空，但措辞明确警示「过度解读」。", "time": "18:20", "source": "深交所公告", "tag": "持仓", "tag_variant": "warning"},
    {"title": "📈 日月光先进封装第三轮涨价20%（CoWoS/FoCoS）", "content": "继3月、5月两轮涨价后，日月光投控7月启动CoWoS、FoCoS等先进封装第三轮涨价20%，反映AI芯片先进封装产能持续紧张、HBM配套封装需求爆发。利好国内封测（长电科技/通富微电）及封装材料（华海诚科/雅克科技前驱体）。但今日板块随半导体大盘调整，长电科技-7%。", "time": "16:00", "source": "产业链", "tag": "产业", "tag_variant": "success"},
    {"title": "📈 国巨MLCC全系列涨价，高端现货涨10倍", "content": "被动元件龙头国巨通知7月起MLCC全系列涨价，工业级/车规级涨幅10-20%，AI服务器用高容MLCC现货价格暴涨10倍（从0.05元/颗→0.5元/颗），反映AI服务器MLCC用量是普通8-10倍、供需极度紧张。利好风华高科、三环集团、洁美科技。", "time": "盘中", "source": "产业链", "tag": "产业", "tag_variant": "success"},
    {"title": "📈 三星HBM4E良率破70%，2027年量产", "content": "三星电子宣布HBM4E（12-16层堆叠）良率突破70%，目标2027年量产，较TSMC/SK海力士路线差异化。HBM竞赛升级持续利好前驱体/TSV材料/HVLP铜箔等上游材料。", "time": "韩联社", "source": "三星电子", "tag": "产业", "tag_variant": "success"},
    {"title": "🤖 上海具身智能博览会开幕（7/2-4），200+企业参展，31股涨停", "content": "首届上海国际具身智能产业博览会开幕，宇树/加速进化/乐聚/中科新松等整机厂亮相，三大全国赛事+出海对接会。今日人形机器人板块逆势31家涨停，锋龙股份3天2板、宏昌科技20cm涨停，汇川技术主力净买4.16亿。", "time": "09:00", "source": "展会", "tag": "催化", "tag_variant": "success"},
    {"title": "📅 7/6（周一）ST涨跌幅扩至10%新规实施，剩余最后1个交易日", "content": "新规要点：①主板ST/*ST涨跌幅由5%扩至10%；②盘后固定价交易扩展至全A股+ETF（15:05-15:30按收盘价）；③ETF尾盘3分钟改集合竞价。ST板块今日59家涨停的末日博弈但*ST建艺逆市下跌，7/3是持仓最后离场窗口。", "time": "倒计时", "source": "沪深交易所", "tag": "规则", "tag_variant": "warning"},
    {"title": "🧪 电子级氢氟酸G5半年涨75%引爆氟化工板块", "content": "日本限制出口+国内晶圆厂扩产拉动，电子级氢氟酸G5（12英寸晶圆用）半年涨75%，从1.2万/吨涨至2.1万/吨；多氟多昨日4连板今日发风险公告（半导体级氢氟酸营收占比<2%）后炸板；昊华科技、巨化股份等跟涨。", "time": "盘中", "source": "百川资讯", "tag": "涨价", "tag_variant": "success"},
]
gen.add_evening_news(evening_news)

gen.add_earnings_forecast()

predictions = [
    {"name": "超跌反弹（科技股修复）", "direction": "看涨", "confidence": 65, "reason": "非农爆冷5.7万远低预期→降息预期重燃→美股期指+0.7%、黄金暴涨4140+→外资风险偏好修复。A股半导体/CPO/算力连续两日暴跌累计跌幅大（科创50两日累计-10%），短期超跌反弹概率高，但反弹是逃命波而非反转。"},
    {"name": "黄金/贵金属/小金属", "direction": "看涨", "confidence": 75, "reason": "非农爆冷+降息预期+避险三重催化，现货黄金破4140美元涨2.37%创近期新高。赤峰黄金/招金黄金今日已涨停，明日有望延续强势，但需警惕美元反弹后的冲高回落。"},
    {"name": "人形机器人/具身智能", "direction": "看涨", "confidence": 68, "reason": "上海具身智能博览会第二日（7/3）+板块今日逆势31家涨停独立于科技暴跌+汇川技术等龙头机构逆势加仓。短期强催化仍在，但板块已连涨多日且涨幅集中在小票，注意高位股兑现风险。"},
    {"name": "半导体/CPO/算力", "direction": "震荡修复", "confidence": 50, "reason": "连续两天暴跌后（科50两日-10%+），短期技术性反弹可期，但中期CAPEX见顶担忧未消+中报业绩验证期+北方华创/兆易创新等龙头跌停套牢盘压力巨大，反弹高度有限，是减仓窗口而非加仓机会。"},
    {"name": "中报预增/低位价值", "direction": "看涨", "confidence": 62, "reason": "7月15日前中报预告密集披露期，市场从炒预期转向看兑现，中报大幅预增+低位低估值方向（医药/银行/煤炭/化工涨价）继续是资金避风港。"},
]
gen.add_tomorrow_prediction(predictions)

gen.add_risk_warning([
    "🔥 隔夜费半-6.27%暴跌只是开始，Meta出售AI算力引发CAPEX见顶担忧或持续发酵，若今晚美股科技股继续下挫将再度冲击A股",
    "🔥 美国6月非农爆冷5.7万表面利好降息，但经济硬着陆风险升温，若后续数据进一步恶化可能引发衰退交易",
    "⚠️ 雅克科技跌停-10%，风险公告「过度解读」措辞需警惕，HBM材料板块可能面临估值回调",
    "⚠️ 7/6 ST涨跌幅扩至10%，*ST建艺7/3必须清仓，否则面临单日-10%跌停、两日-19%的极端风险",
    "⚠️ 英维克深度破止损-31.5%连续下跌，AI算力链需求放缓预期下，液冷温控板块中期压力巨大",
    "⚠️ 两市融资余额可能面临平仓压力，若明日继续下跌可能触发杠杆资金强平负反馈",
    "⚡ 7/3美国独立日美股休市，北向通道关闭，外资缺席下A股流动性波动可能放大",
    "⚡ 中报预告期（7/15前）「业绩雷」密集释放，纯题材/无订单/高位小票继续杀估值",
])

trading_plan = '''
<div style="display: flex; flex-direction: column; gap: 16px;">
    <div style="background: rgba(239,68,68,0.08); border-radius: 12px; padding: 16px; border-left: 4px solid #ef4444;">
        <div style="font-weight: 700; color: #ef4444; margin-bottom: 8px;">🔴 紧急清仓/减仓（7/3开盘第一优先级）</div>
        <div style="font-size: 13px; color: #4b5563; line-height: 1.8;">
            <strong>*ST建艺(002789)</strong>：7/6涨跌幅扩至10%，<strong>7/3开盘任何价格必须清仓不留1股</strong>，不挂单等反弹、不抱幻想。公司基本面持续恶化，扩幅后单日跌停-10%相当于原规则下两日跌停，绝对不能等到7/6。<br>
            <strong>英维克(002837)</strong>：深度破止损-31.5%+连续5日净流出21亿+大宗折价71.4元成交，AI算力CAPEX见顶逻辑动摇。<strong>7/3任何反弹至73-75区间坚决清仓，下破70元无条件离场</strong>，禁止补仓摊低成本。
        </div>
    </div>
    <div style="background: rgba(249,115,22,0.08); border-radius: 12px; padding: 16px; border-left: 4px solid #f97316;">
        <div style="font-weight: 700; color: #f97316; margin-bottom: 8px;">🟠 减仓锁利（控制仓位）</div>
        <div style="font-size: 13px; color: #4b5563; line-height: 1.8;">
            <strong>铜冠铜箔(301217)</strong>：相对抗跌但主力净卖5.84亿，存储板块整体暴跌拖累。<strong>160-165减仓1/3锁利（浮盈81%落袋）</strong>，剩余底仓移动止盈上移至155元，跌破150再减1/3。等费半企稳+中报验证后再决策。<br>
            <strong>雅克科技(002409)</strong>：跌停-10%+公司澄清过度解读+机构从买2.8亿转卖5.25亿，<strong>底仓保留1/2观察200-210支撑</strong>，反弹225-230减仓1/3锁利（浮盈103%部分落袋），<strong>跌破200元必须减仓至1/4以下</strong>。
        </div>
    </div>
    <div style="background: rgba(16,185,129,0.08); border-radius: 12px; padding: 16px; border-left: 4px solid #10b981;">
        <div style="font-weight: 700; color: #10b981; margin-bottom: 8px;">🟢 明日可轻仓关注（超跌反弹+独立主线）</div>
        <div style="font-size: 13px; color: #4b5563; line-height: 1.8;">
            ①<strong>人形机器人/具身智能</strong>：博览会第二日催化，但板块已31家涨停只做核心龙头低吸（汇川技术/绿的谐波/双环传动/埃斯顿），不追2板以上小票；<br>
            ②<strong>黄金/贵金属</strong>：非农爆冷+降息预期+避险（赤峰黄金/山金国际/招金黄金），但今日已涨停等回踩5日线；<br>
            ③<strong>半导体设备/存储超跌反弹</strong>：北方华创/兆易创新跌停后或有反弹，<strong>仅做T+0日内，不留隔夜仓</strong>，反弹是减仓科技股的窗口而非加仓窗口。
        </div>
    </div>
    <div style="background: rgba(245,158,11,0.08); border-radius: 12px; padding: 16px; border-left: 4px solid #f59e0b;">
        <div style="font-weight: 700; color: #f59e0b; margin-bottom: 8px;">🟡 仓位建议</div>
        <div style="font-size: 13px; color: #4b5563; line-height: 1.8;">
            处理完*ST建艺+英维克清仓、铜冠/雅克减仓锁利后，<strong>总仓位从当前约7成降至3成以下</strong>。7月是验牌月（非农→CPI→FOMC→中报→ST新规），波动剧烈不满仓。保留现金等待：①费半企稳信号（连续2日收阳+龙头止跌）；②中报业绩验证（7/15前后）；③7/29 FOMC靴子落地后再重新加仓。
        </div>
    </div>
</div>
'''
gen.add_trading_plan(trading_plan)

output_path = f"docs/aftermarket/{DATE}_盘后速递.html"
html = gen.generate()
os.makedirs(os.path.dirname(output_path), exist_ok=True)
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(html)
print(f"OK: {output_path}")
print(f"Size: {os.path.getsize(output_path)} bytes")
