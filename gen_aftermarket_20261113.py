#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, 'v3')
os.chdir('/root/daily-news-insight')

from v3.generators.aftermarket import AftermarketGenerator
from v3.components.layout import Section

DATE = "20261113"
SUBTITLE = "2026.11.13 · 盘后速递 · 科技股午后杀跌 CPO/PCB/MLCC全线重挫"

gen = AftermarketGenerator(date_str=DATE, subtitle=SUBTITLE)

gen.add_today_highlight("""
<strong style="color:#f87171;">⚠️ 科技股高开低走放量杀跌，三大指数集体收跌，全市场超4700只个股下跌</strong>。
今日A股呈现典型"高开低走"崩盘走势：早盘受隔夜美股AI大涨刺激，半导体、CPO、存储集体高开超1%，
科创50盘中一度涨超2%；但10:30后抛压持续涌现，午后科技板块遭遇恐慌性抛售，CPO跌4.4%、PCB跌4.32%、
MLCC跌4.34%，景旺电子跌停，东山精密逼近跌停，中际旭创主力净流出29.42亿。
尾盘资金涌入银行股避险，江苏银行、南京银行等5只银行股齐创历史新高。
成交额1.66万亿缩量2764亿，内资主力净卖出600.2亿，市场情绪骤降至冰点。
""")

indices = [
    {"name": "上证指数", "value": "3634.35", "change": "-0.59%", "up": False, "icon": "trending_down"},
    {"name": "深证成指", "value": "10968.79", "change": "-2.05%", "up": False, "icon": "trending_down"},
    {"name": "创业板指", "value": "2426.08", "change": "-3.32%", "up": False, "icon": "trending_down"},
    {"name": "科创50", "value": "1279.66", "change": "-2.30%", "up": False, "icon": "trending_down"},
]
gen.add_market_summary(indices=indices, volume="1.66万亿（缩量2764亿）", northbound="成交2300亿（净卖出）")

gen.add_sentiment_thermometer(temperature=22, volume="1.66万亿", up_count="765只", down_count="4748只", limit_up_count="38只")

up_sectors = [
    {"name": "🐷 猪肉/养殖", "change": "+2.15%", "up": True, "leader": "金新农、天邦食品双双涨停"},
    {"name": "🏦 银行", "change": "+1.46%", "up": True, "leader": "5只银行股齐创历史新高"},
    {"name": "🏠 家用电器", "change": "+1.47%", "up": True, "leader": "防御性板块受追捧"},
    {"name": "🍶 白酒/食品饮料", "change": "+1.18%", "up": True, "leader": "古井贡酒涨4.27%"},
    {"name": "🎬 AI漫剧/影视", "change": "+2.40%", "up": True, "leader": "文投控股5天4板"},
    {"name": "⚡ 算力芯片", "change": "+0.5%", "up": True, "leader": "天普股份4连板"},
]
down_sectors = [
    {"name": "📡 CPO/光模块", "change": "-4.40%", "up": False, "leader": "景旺电子跌停，中际旭创-7%"},
    {"name": "🔌 PCB/覆铜板", "change": "-4.32%", "up": False, "leader": "东山精密-9.95%逼近跌停"},
    {"name": "🔋 MLCC/被动元件", "change": "-4.34%", "up": False, "leader": "三环集团-8.89%，风华高科-6.84%"},
    {"name": "💻 通信设备", "change": "-4.97%", "up": False, "leader": "申万一级行业跌幅第一"},
    {"name": "🔬 电子半导体", "change": "-3.75%", "up": False, "leader": "兆易创新跌停"},
    {"name": "🧱 建筑材料", "change": "-3.25%", "up": False, "leader": "地产链持续走弱"},
]
gen.add_sector_performance(up_sectors=up_sectors, down_sectors=down_sectors)

strong_sectors = [
    {"name": "银行/高股息", "reason": "科技股崩盘引发资金避险，江苏银行等5只银行股创历史新高，主力净流入银行8.63亿，保险板块逆势收涨。高股息防御逻辑在年末调仓窗口被强化，预计短期仍是资金避风港。"},
    {"name": "AI影视/短剧", "reason": "文投控股5天4板，幸福蓝海20CM涨停，金逸影视4天2板，横店影视、湖北广电涨停。《流浪地球3》定档2027春节催化影视院线板块，呼家楼1.14亿抢筹儒意电影。"},
    {"name": "猪肉/养殖", "reason": "金新农、天邦食品双双涨停，猪周期预期+年末消费旺季+防御属性三重逻辑，板块涨幅2.15%居概念榜首，持续性需观察生猪价格。"},
]
weak_sectors = [
    {"name": "CPO/光模块", "reason": "景旺电子跌停，科翔股份、炬光科技跌超10%，中际旭创主力净流出29.42亿、新易盛21.15亿、东山精密17.71亿、天孚通信16.9亿。高位光模块在美股利好兑现后遭获利盘集中砸盘，光模块整体净流出227.6亿。"},
    {"name": "PCB/覆铜板", "reason": "生益科技跌停-9.99%，东山精密-9.95%成交153亿，崇达技术-8.09%，金安国纪-8.32%。PCB前期受AI服务器需求催化涨幅过大，属高位补跌，资金获利了结坚决。"},
    {"name": "算力硬件/液冷", "reason": "英维克-6.39%放量杀跌，主力净流出2.87亿；液冷板块在11日涨停后连续两日大跌（12日-5.4%、13日-6.39%），典型拉高出货走势，算力硬件整体主力净流出137亿。"},
]
core_view = """今日A股"高开低走"杀伤力比直接低开更甚：早盘借隔夜美股AI大涨利好高开给了短线资金绝佳离场机会；午后CPO/PCB/MLCC等高位科技股集体闪崩，说明前期抱团资金开始大规模调仓。<strong style="color:#f87171;">核心矛盾：高位科技股估值与业绩增速匹配度问题</strong>，中际旭创、新易盛等光模块龙头估值已透支明年业绩，而银行/白酒低估值高股息板块在险资年末"哑铃型"配置下持续获资金青睐。<strong style="color:#fbbf24;">操作上严格控制科技仓位≤50%，高位CPO/PCB方向坚决减仓</strong>，等待下一个明确催化点再加仓。下周一关注银行股能否延续强势、科技股能否在3600点附近企稳。"""
gen.add_market_deep_analysis(strong_sectors=strong_sectors, weak_sectors=weak_sectors, core_view=core_view)

holdings = [
    {"name": "英维克", "code": "002837", "price": "38.36", "change": "-6.39%", "up": False,
     "comment": "今开41.04高开放量杀跌，最高41.57，最低38.15逼近跌停36.88，成交15.79亿换手3.52%，主力净流出2.87亿。11日涨停→12日-5.4%→13日-6.39%，典型涨停后出货，5/10/20日均线全部空头排列。🔴操作建议：<strong>38元为关键支撑，跌破36.88跌停价立即清仓；反弹至40-41元减仓1/2</strong>，不补仓不抄底。"},
    {"name": "铜冠铜箔", "code": "301217", "price": "67.54", "change": "-5.72%", "up": False,
     "comment": "今开73.08高开低走，最高73.6，最低66.89，振幅9.37%，成交13.46亿换手2.34%。前三季度净利润+439.75%业绩扎实，技术面67元附近有60日线支撑。🟡操作建议：<strong>66-67元小幅加仓1成底仓，跌破65元止损；反弹至73-75元减仓1/3</strong>。HVLP铜箔逻辑未变但受PCB拖累，仓位控制在2成以内。"},
    {"name": "雅克科技", "code": "002409", "price": "86.34", "change": "-4.46%", "up": False,
     "comment": "今开91.80高开后单边下杀，最高93.40，最低85.51，振幅8.73%，成交17.76亿换手6.25%，主力净流出3435万。HBM前驱体龙头受半导体拖累但未跌停，12位分析师目标均价97.70。🟡操作建议：<strong>85元重要支撑，跌破82元减仓1/3；85-88元观望，反弹至92元以上减仓机动仓</strong>，底仓保留。"},
    {"name": "*ST建艺", "code": "002789", "price": "8.00", "change": "-10.01%", "up": False,
     "comment": "一字跌停，最高8.91即开盘价，最低8.00封死跌停，买一挂单为零无承接，成交6410万换手4.95%，主力净流出1082万。退市风险+ST板块集体调整，封单坚决。🚨操作建议：<strong>下周一挂8元跌停价排队清仓，无条件离场</strong>，退市风险股不恋战。"},
    {"name": "华海诚科", "code": "688535", "price": "73.08", "change": "-3.68%", "up": False,
     "comment": "今开77.12高开回落，最高79.71，最低72.35，成交5.47亿换手5.08%。11月12日843万股限售股解禁抛压释放中，但Q3单季净利+515%基本面强劲。🟢操作建议：<strong>70-73元分批建仓2成，跌破68元止损；反弹至80元以上减仓</strong>，GMC塑封料国产替代长期逻辑清晰。"},
    {"name": "长电科技", "code": "600584", "price": "52.70", "change": "-3.21%", "up": False,
     "comment": "今开54.92高开低走，最高55.50，最低52.20破前低，主力净流出2.96亿，封测龙头遭错杀。Q3业绩高增+资本开支上修至182亿，基本面优质。🟢操作建议：<strong>52元以下分批建仓2成，50元加仓1成，跌破49元止损；反弹至57元减仓</strong>，先进封装景气左侧布局。"},
    {"name": "风华高科", "code": "000636", "price": "30.36", "change": "-6.84%", "up": False,
     "comment": "今开33.01高开后放量暴跌，最高33.17，最低30.18逼近跌停29.33，振幅9.17%，成交22.59亿换手6.29%，主力净流出2.53亿。Q3净利+470%后遇利好出尽式砸盘。🔴操作建议：<strong>30元为底线，跌破29.33跌停价清仓1/2；29-30元观察承接，不急于抄底；反弹至33元以上减仓1/3</strong>。"},
]
gen.add_holdings_tracking(holdings=holdings)

longhubang = [
    {"name": "文投控股", "code": "600715", "up": True, "change": "+10.04%（5天4板）", "institutions": 0,
     "reason": "日涨幅偏离值7%", "net_buy": "+4.68亿（呼家楼+游资合力）"},
    {"name": "旋极信息", "code": "300324", "up": True, "change": "+17.58%（20CM涨停）", "institutions": 0,
     "reason": "GPU/算力概念", "net_buy": "+2.40亿（东财拉萨天团）"},
    {"name": "儒意电影", "code": "00136", "up": True, "change": "+9.96%", "institutions": 0,
     "reason": "流浪地球3定档", "net_buy": "+1.14亿（呼家楼独买）"},
    {"name": "沪电股份", "code": "002463", "up": False, "change": "-10.00%（跌停）", "institutions": 0,
     "reason": "机构净卖出第一", "net_buy": "-1.21亿（机构大幅抛售）"},
    {"name": "通化金马", "code": "000766", "up": True, "change": "+10.00%", "institutions": 0,
     "reason": "日涨幅偏离值7%", "net_buy": "机构净卖1613万+北向净卖2147万"},
]
gen.add_dragon_tiger_list(stocks=longhubang)

focus_html = '''
<div style="display: flex; flex-direction: column; gap: 14px;">
<div style="background: linear-gradient(135deg, rgba(16,185,129,0.12), rgba(5,150,105,0.08)); border: 1px solid rgba(16,185,129,0.3); border-radius: 14px; padding: 16px;">
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
        <strong style="color:#34d399; font-size:15px;">🏦 江苏银行(600919)</strong>
        <span style="color:#34d399; font-weight:700;">创历史新高</span>
    </div>
    <p style="margin:0; font-size:13px; color:#cbd5e1; line-height:1.7;">
    <strong style="color:#f1f5f9;">逻辑：</strong>银行股龙头，高股息+险资配置+年末防御三重逻辑，板块风向标。<strong style="color:#fbbf24;">买点：</strong>回调10日线分批建仓；<strong style="color:#fbbf24;">目标：</strong>突破新高+10%；<strong style="color:#ef4444;">止损：</strong>跌破20日线。
    </p>
</div>
<div style="background: linear-gradient(135deg, rgba(59,130,246,0.12), rgba(99,102,241,0.08)); border: 1px solid rgba(96,165,250,0.3); border-radius: 14px; padding: 16px;">
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
        <strong style="color:#60a5fa; font-size:15px;">🐷 金新农(002548)</strong>
        <span style="color:#10b981; font-weight:700;">首板涨停</span>
    </div>
    <p style="margin:0; font-size:13px; color:#cbd5e1; line-height:1.7;">
    <strong style="color:#f1f5f9;">逻辑：</strong>猪肉板块龙头，猪周期+消费旺季+防御属性，农业有望成避险新方向。<strong style="color:#fbbf24;">买点：</strong>回踩涨停价轻仓；<strong style="color:#ef4444;">止损：</strong>跌破涨停开盘价。
    </p>
</div>
<div style="background: linear-gradient(135deg, rgba(245,158,11,0.12), rgba(234,88,12,0.08)); border: 1px solid rgba(245,158,11,0.3); border-radius: 14px; padding: 16px;">
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
        <strong style="color:#fbbf24; font-size:15px;">⚠️ 风险警示：东山精密(002384)</strong>
        <span style="color:#ef4444; font-weight:700;">-9.95%天量</span>
    </div>
    <p style="margin:0; font-size:13px; color:#cbd5e1; line-height:1.7;">
    <strong style="color:#f1f5f9;">风险：</strong>成交153亿天量暴跌逼近跌停，PCB龙头遭资金大规模出逃，持有者反弹至90元以上坚决减仓。<strong style="color:#ef4444;">支撑：</strong>80元；<strong style="color:#ef4444;">压力：</strong>95元。
    </p>
</div>
</div>'''
gen._components.append(Section(title="⭐ 重点关注标的", content=focus_html, icon="star"))

predictions = [
    {"name": "大盘指数", "direction": "震荡", "confidence": 70,
     "reason": "3600点整数关口有支撑，但科技股抛压未完全释放，预计下周一沪指在3600-3660区间震荡，创业板指考验2400点支撑。银行股强势可托住指数，但科技股反抽是减仓机会。"},
    {"name": "CPO/光模块", "direction": "看跌", "confidence": 65,
     "reason": "主力净流出227.6亿，景旺电子跌停、机构净卖沪电1.21亿，高位科技股筹码松动，下周一惯性下探概率大，不急于抄底。"},
    {"name": "银行/高股息", "direction": "看涨", "confidence": 65,
     "reason": "5只银行股创历史新高，险资年末配置压力+资金避险需求，银行/保险/高股息方向有望延续，但追高需谨慎。"},
    {"name": "AI影视/短剧", "direction": "震荡", "confidence": 55,
     "reason": "文投控股5天4板、呼家楼买入儒意电影，情绪仍在但位置已高，分化加剧，只适合快进快出。"},
]
gen.add_tomorrow_prediction(predictions=predictions)

plan = '''
<div style="background: rgba(30,30,50,0.5); border-radius: 16px; padding: 20px; border: 1px solid rgba(255,255,255,0.08);">
<p style="margin:0 0 12px;"><strong style="color:#fbbf24; font-size:16px;">📊 仓位建议：总仓位由7成降至5成，现金留5成应对下周波动</strong></p>
<p style="margin:0 0 10px;"><strong style="color:#ef4444;">🔴 减仓/止损（优先级最高）：</strong></p>
<ul style="margin:0 0 14px; padding-left:20px; font-size:13px; color:#cbd5e1; line-height:2;">
<li><strong style="color:#ef4444;">*ST建艺</strong>：下周一挂8元跌停价<strong>无条件清仓</strong></li>
<li><strong style="color:#ef4444;">英维克</strong>：<strong>跌破36.88元清仓</strong>；反弹40-41元减仓1/2，不补仓</li>
<li><strong style="color:#ef4444;">风华高科</strong>：<strong>跌破29.33元减仓1/2</strong>；反弹33元以上减仓1/3</li>
<li><strong style="color:#ef4444;">雅克科技</strong>：跌破82元减仓1/3；反弹92元以上减仓机动仓</li>
</ul>
<p style="margin:0 0 10px;"><strong style="color:#10b981;">🟢 加仓/建仓观察（左侧轻仓）：</strong></p>
<ul style="margin:0 0 14px; padding-left:20px; font-size:13px; color:#cbd5e1; line-height:2;">
<li><strong style="color:#10b981;">长电科技</strong>：52元以下建仓2成，50元加仓1成，跌破49元止损</li>
<li><strong style="color:#10b981;">铜冠铜箔</strong>：66-67元加仓1成，跌破65元止损</li>
<li><strong style="color:#10b981;">华海诚科</strong>：70-73元建仓2成，跌破68元止损</li>
<li><strong style="color:#60a5fa;">银行/高股息ETF</strong>：10%仓位防御对冲</li>
</ul>
<p style="margin:0;"><strong style="color:#fbbf24;">⚠️ 纪律：</strong>今日高位科技股集体杀跌是明确风险信号，<strong style="color:#f87171;">不抄底、不补仓、不抢反弹</strong>，严格止损，空出资金等待科技股企稳信号。下周一重点关注银行股延续性、CPO/PCB是否继续暴跌、沪指3600点支撑。</p>
</div>'''
gen.add_trading_plan(plan=plan)

evening_news = [
    {"title": "央行：坚持适度宽松货币政策", "content": "保持流动性合理充裕，支持实体经济发展。", "time": "11/13", "source": "央行", "tag": "宏观", "tag_variant": "primary"},
    {"title": "流浪地球3定档2027春节，儒意电影涨停", "content": "呼家楼1.14亿抢筹，影视院线板块受催化。", "time": "11/13", "source": "证券时报", "tag": "题材", "tag_variant": "warning"},
    {"title": "5只银行股创历史新高", "content": "江苏银行/南京银行/青岛银行/成都银行/杭州银行齐创新高，险资年末加仓高股息。", "time": "11/13", "source": "财联社", "tag": "资金", "tag_variant": "success"},
    {"title": "CPO/PCB主力净流出超400亿", "content": "中际旭创净流出29亿、新易盛21亿、东山精密18亿，机构抛售态度坚决。", "time": "11/13", "source": "数据宝", "tag": "资金", "tag_variant": "danger"},
    {"title": "美股英伟达创历史新高", "content": "隔夜美股科技股大涨，但A股高开低走说明利好已被提前消化。", "time": "11/13", "source": "新浪财经", "tag": "海外", "tag_variant": "default"},
]
gen.add_evening_news(news_list=evening_news)

risks = [
    "高位科技股获利回吐风险：CPO/PCB/MLCC/液冷主力资金大幅流出，短期调整压力大，切勿盲目抄底",
    "仓位集中风险：若科技仓位过重，下周一继续杀跌将面临较大回撤，建议降至5成以下",
    "ST退市风险：*ST建艺跌停封单坚决，必须无条件离场",
    "北向资金流向风险：北向对科技股态度分化，持续跟踪外资动向",
    "周末消息面不确定性：关注中美关系、国内政策、美股走势，控制仓位过节",
]
gen.add_risk_warning(risks=risks)

print("Publishing...")
result = gen.publish(filename=f"{DATE}_盘后速递.html")
print(f"Result: {result}")
print("Done!")
