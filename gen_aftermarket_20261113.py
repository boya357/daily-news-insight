#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, 'v3')
os.chdir('/root/daily-news-insight')

from v3.generators.aftermarket import AftermarketGenerator
from v3.components.layout import Section

DATE = "20261113"
SUBTITLE = "2026.11.13 · 盘后速递 · 科技股午后崩盘 CPO/PCB/MLCC全线重挫 银行股集体创新高避险"

gen = AftermarketGenerator(date_str=DATE, subtitle=SUBTITLE)

# ============ 1. 今日核心亮点 ============
gen.add_today_highlight("""
<strong style="color:#f87171;">⚠️ 科技股高开低走放量杀跌，三大指数集体收跌，全市场超4700只个股下跌</strong>。
今日A股呈现教科书级别的“利好出货”走势：早盘受隔夜美股AI板块大涨刺激（英伟达再创历史新高），半导体、CPO、存储芯片集体高开超1%，
科创50指数盘中一度涨超2%，市场情绪极度亢奋；但10:30之后抛压开始持续涌现，午后13:30科技板块更是遭遇恐慌性抛售，
CPO板块暴跌4.40%、PCB跌4.32%、MLCC被动元件跌4.34%、通信设备跌4.97%居申万一级行业跌幅榜首，
景旺电子跌停、生益科技跌停、兆易创新跌停、东山精密逼近跌停（-9.95%成交153亿天量），
中际旭创主力净流出29.42亿、新易盛21.15亿、东山精密17.71亿、天孚通信16.90亿，光模块整体净流出227.6亿。
尾盘资金疯狂涌入银行股避险，江苏银行、南京银行、青岛银行、成都银行、杭州银行5只银行股齐创历史新高，险资年末“哑铃型”配置效应显现。
全市场成交额1.66万亿元，较昨日缩量2764亿；内资主力资金净卖出600.2亿元；上涨家数仅765家，下跌4748家，涨停38家，市场情绪骤降至冰点。
""")

# ============ 2. 市场收盘总结 ============
indices = [
    {"name": "上证指数", "value": "3634.35", "change": "-0.59%", "up": False, "icon": "trending_down"},
    {"name": "深证成指", "value": "10968.79", "change": "-2.05%", "up": False, "icon": "trending_down"},
    {"name": "创业板指", "value": "2426.08", "change": "-3.32%", "up": False, "icon": "trending_down"},
    {"name": "科创50", "value": "1279.66", "change": "-2.30%", "up": False, "icon": "trending_down"},
]
gen.add_market_summary(indices=indices, volume="1.66万亿（缩量2764亿）", northbound="成交2300亿（净卖出为主）")

# ============ 3. 情绪温度计 ============
gen.add_sentiment_thermometer(temperature=22, volume="1.66万亿", up_count="765只", down_count="4748只", limit_up_count="38只")

# ============ 4. 板块涨跌幅排行 ============
up_sectors = [
    {"name": "🐷 猪肉/养殖", "change": "+2.15%", "up": True, "leader": "金新农、天邦食品双双涨停，板块涨幅居首"},
    {"name": "🏦 银行", "change": "+1.46%", "up": True, "leader": "江苏银行等5只银行股齐创历史新高"},
    {"name": "🏠 家用电器", "change": "+1.47%", "up": True, "leader": "防御性消费板块受避险资金追捧"},
    {"name": "🍶 白酒/食品饮料", "change": "+1.18%", "up": True, "leader": "古井贡酒涨4.27%，茅台逆势翻红"},
    {"name": "🎬 AI漫剧/影视", "change": "+2.40%", "up": True, "leader": "文投控股5天4板，幸福蓝海20CM涨停"},
    {"name": "⚡ 算力芯片", "change": "+0.5%", "up": True, "leader": "天普股份4连板，华东重机涨停"},
]
down_sectors = [
    {"name": "📡 CPO/光模块", "change": "-4.40%", "up": False, "leader": "景旺电子跌停，中际旭创-7%净流出29亿"},
    {"name": "🔌 PCB/覆铜板", "change": "-4.32%", "up": False, "leader": "东山精密-9.95%成交153亿，生益科技跌停"},
    {"name": "🔋 MLCC/被动元件", "change": "-4.34%", "up": False, "leader": "三环集团-8.89%，风华高科-6.84%"},
    {"name": "💻 通信设备", "change": "-4.97%", "up": False, "leader": "申万一级行业跌幅第一，新易盛跌停"},
    {"name": "🔬 电子半导体", "change": "-3.75%", "up": False, "leader": "兆易创新跌停，长电科技-3.21%"},
    {"name": "🧱 建筑材料", "change": "-3.25%", "up": False, "leader": "地产链持续走弱，消费建材普跌"},
]
gen.add_sector_performance(up_sectors=up_sectors, down_sectors=down_sectors)

# ============ 5. 盘面深度解读（加字） ============
strong_sectors = [
    {"name": "银行/高股息", "reason": "科技股崩盘引发资金大规模避险，江苏银行、南京银行、青岛银行、成都银行、杭州银行5只城商行齐创历史新高，主力资金净流入银行板块8.63亿元，保险板块亦逆势收涨。高股息防御逻辑在年末险资“哑铃型”配置窗口下被持续强化：一端配置高股息资产做底仓防守，一端择机参与景气成长，银行板块作为底仓首选持续获得增量资金。江苏银行近期已连续8日阳线，资金入场意愿坚决，预计短期仍将是资金避风港。"},
    {"name": "AI影视/短剧", "reason": "文投控股5天4板成为短线情绪龙头，幸福蓝海20CM涨停，金逸影视4天2板，横店影视、湖北广电涨停，儒意电影涨停。《流浪地球3》正式定档2027年大年初一成为影视院线板块明确催化，呼家楼1.14亿独买儒意电影，游资主导的题材情绪行情仍在演绎。但需要注意的是，该板块更多是事件驱动+游资炒作，业绩兑现周期较长，中长线配置价值有限。"},
    {"name": "猪肉/养殖", "reason": "金新农、天邦食品双双涨停，板块整体涨幅2.15%位居概念板块榜首，牧原股份、温氏股份等龙头股逆势收红。核心逻辑是三重共振：一是猪周期底部上行预期增强，能繁母猪存栏连续多月去化；二是年末腌腊旺季+春节消费旺季来临，猪肉价格有望季节性反弹；三是农业板块本身具有防御属性，在科技股杀跌时成为避险资金新方向。但持续性还需观察生猪现货价格是否持续上涨。"},
]
weak_sectors = [
    {"name": "CPO/光模块", "reason": "景旺电子跌停封板，科翔股份、联讯仪器、炬光科技跌超10%，天孚通信-7.89%，新易盛跌停。主力资金层面更是惨烈：中际旭创主力净流出29.42亿元、新易盛21.15亿、东山精密17.71亿、天孚通信16.90亿、生益电子6.67亿、沪电股份6.19亿、兆龙互连5.44亿，光模块整体净流出227.6亿元。高位光模块在隔夜美股科技股大涨利好兑现后遭遇获利盘集中砸盘，属于典型的“利好出货”走势，前期抱团资金开始大规模撤退。"},
    {"name": "PCB/覆铜板", "reason": "生益科技跌停-9.99%，东山精密-9.95%逼近跌停成交153亿天量，崇达技术-8.09%，金安国纪-8.32%，鹏鼎控股、深南电路等龙头股均跌超5%。PCB板块前期受AI服务器需求爆发（英伟达GB200/GB300拉动HDI/高速PCB需求）催化涨幅过大，多数个股3季度以来涨幅超50%，当前属于典型的高位补跌+获利了结。机构龙虎榜显示沪电股份遭机构净卖出1.21亿元，为今日龙虎榜机构净卖出第一位。"},
    {"name": "算力硬件/液冷", "reason": "英维克-6.39%放量杀跌，主力净流出2.87亿元；高澜股份、申菱环境等液冷龙头均跌超7%。液冷板块在11月11日涨停后连续两个交易日大跌（12日-5.40%、13日-6.39%），呈现典型的“涨停出货”走势。算力硬件整体主力净流出137亿元，资金出逃态度坚决。这与前期我们反复提示的"高位算力硬件不追高"判断一致，液冷/光模块/PCB等AI硬件方向短期进入调整期。"},
]
core_view = """今日A股"高开低走"的杀伤力比直接低开更甚：早盘借隔夜美股AI板块大涨的利好（英伟达创历史新高）大幅高开，给了前期埋伏的短线资金和机构绝佳的离场机会；午后CPO/PCB/MLCC等高位科技股集体闪崩跌停，说明前期抱团资金已经开始大规模调仓换股，从高位科技股向银行/白酒/农业等低位防御方向切换。
<strong style="color:#f87171;">核心矛盾：高位科技股估值与业绩增速的匹配度问题</strong>。中际旭创、新易盛等光模块龙头2026年动态PE已超过40倍，透支了明年业绩增长预期；而银行板块2026年PE普遍在5-7倍，股息率5%以上，性价比差距悬殊，险资年末配置压力下高股息板块持续获得资金青睐。
<strong style="color:#fbbf24;">操作策略上，严格控制科技板块仓位≤50%，高位CPO/PCB/光模块方向坚决逢反弹减仓</strong>，
不要急于抄底，等待下一个明确的催化点（如英伟达Q3财报、国内大模型采购订单落地、三季报业绩超预期）再考虑加仓。下周一重点关注三大信号：①银行股能否延续强势继续创新高；②CPO/PCB是否惯性下探后出现缩量企稳信号；③上证指数3600点整数关口支撑力度。"""
gen.add_market_deep_analysis(strong_sectors=strong_sectors, weak_sectors=weak_sectors, core_view=core_view)

# ============ 6. 持仓股深度诊断（7只，每只更详细） ============
holdings = [
    {
        "name": "英维克", "code": "002837", "price": "38.36", "change": "-6.39%", "up": False,
        "comment": "今日开盘41.04元高开放量杀跌，最高冲至41.57元后逐级回落，午后最低探至38.15元，距跌停价36.88元仅一步之遥，全天成交15.79亿元，换手率3.52%，主力资金净流出2.87亿元。走势上呈现典型的涨停板出货：11月11日涨停→12日-5.40%→13日-6.39%，三个交易日从高点45.99元跌至38.36元，跌幅达16.6%，技术面上5日、10日、20日均线已全部形成空头排列，MACD死叉向下，KDJ进入超卖区但尚未见底。🔴操作建议：<strong>38元为短期关键心理支撑位，若跌破36.88元（11日涨停开盘价即跌停价）必须立即清仓；反弹至40-41元区间（即今日开盘价附近）减仓1/2仓位</strong>，坚决不补仓、不抄底，等待液冷板块出现明确的缩量止跌+龙头反包信号后再考虑回补。机构一致目标均价56.84元需要等待右侧确认。"
    },
    {
        "name": "铜冠铜箔", "code": "301217", "price": "67.54", "change": "-5.72%", "up": False,
        "comment": "今日开盘73.08元高开0.3%后单边下挫，最高73.60元，最低66.89元，全天振幅9.37%，成交13.46亿元，换手率2.34%（流通盘8.29亿），主力资金小幅净流出。从11月4日高点77.50元回落至67.54元，10个交易日累计跌幅约13%，但公司前三季度净利润同比增长439.75%的业绩基本面非常扎实，HVLP铜箔国产替代逻辑清晰，主要受PCB板块整体暴跌拖累被动下跌。技术面看，67元附近正好是60日均线位置，有较强的技术支撑。🟡操作建议：<strong>66-67元区间可小幅加仓1成（建底仓），若有效跌破65元（前期平台支撑）立即止损出局；反弹至73-75元区间减仓1/3机动仓位</strong>。HVLP铜箔长期逻辑未变，但短期受PCB板块情绪拖累，控制总仓位不超过2成。"
    },
    {
        "name": "雅克科技", "code": "002409", "price": "86.34", "change": "-4.46%", "up": False,
        "comment": "今日开盘91.80元高开2%后单边下杀，最高冲至93.40元后迅速回落，午后最低85.51元，全天振幅8.73%，成交17.76亿元，换手率6.25%，主力资金净流出3435万元，抛压相对可控。作为HBM前驱体材料龙头，雅克科技受半导体板块整体拖累，但跌势相对克制——全天未触及跌停（跌停价81.33元），85.51元附近有明显承接盘。12位分析师一致目标均价97.70元，仍有13%的上行空间。🟡操作建议：<strong>85元为重要支撑位，若有效跌破82元减仓1/3；85-88元区间持有观望为主，反弹至92元以上减仓1/3机动仓位</strong>，底仓继续保留。HBM存储产业链长期景气逻辑未被破坏，但需要等待半导体板块情绪企稳。"
    },
    {
        "name": "*ST建艺", "code": "002789", "price": "8.00", "change": "-10.01%", "up": False,
        "comment": "今日一字跌停开盘，开盘价8.91元即为全天最高价，随后快速封死跌停至8.00元，买一封单挂单为零（完全没有承接盘），全天仅成交6410万元，换手率4.95%，主力资金净流出1082万元。公司被ST后持续走弱，庭外重组进展远水难解近渴，退市风险高悬，ST板块今日集体调整，封单坚决。🚨操作建议：<strong>下周一（11月17日）集合竞价直接挂8元跌停价排队清仓，必须无条件全部离场</strong>，退市风险股不宜有任何侥幸心理，任何盘中打开跌停的反弹都是逃命机会，不要恋战。"
    },
    {
        "name": "华海诚科", "code": "688535", "price": "73.08", "change": "-3.68%", "up": False,
        "comment": "今日开盘77.12元高开1.6%后震荡回落，最高79.71元，午后最低72.35元，成交5.47亿元，换手率5.08%，在科技股暴跌的背景下跌幅相对温和。11月12日有843万股限售股解禁（占总股本5.89%），短期面临解禁抛压释放，但公司Q3单季净利润同比增长515%的基本面非常强劲，先进封装GMC塑封料国产替代龙头地位稳固，72元附近获得明显支撑。🟢操作建议：<strong>70-73元区间可分批建仓2成仓位，若有效跌破68元（前期低点）立即止损；反弹至80元以上减仓机动仓位</strong>。解禁压力消化后有望迎来反弹行情，先进封装长期景气度明确。"
    },
    {
        "name": "长电科技", "code": "600584", "price": "52.70", "change": "-3.21%", "up": False,
        "comment": "今日开盘54.92元高开低走，最高55.50元，最低下探至52.20元跌破前期低点，全天成交超30亿元，换手率约3%，主力资金净流出2.96亿元（近3日累计净流出1.46亿元）。作为全球封测龙头，长电科技今日属于典型的错杀品种：Q3业绩高增长+2026年资本开支从上一年100亿上修至182亿元（同比+82%），基本面质地优异，主要受半导体板块整体拖累。🟢操作建议：<strong>52元以下可分批建仓2成仓位，50元整数关口加仓1成；若有效跌破49元（跌停价位置）止损出局；反弹至57元以上减仓获利了结</strong>。先进封装长期景气趋势明确，当前位置是较好的左侧布局窗口。"
    },
    {
        "name": "风华高科", "code": "000636", "price": "30.36", "change": "-6.84%", "up": False,
        "comment": "今日开盘33.01元高开0.3%后遭遇放量暴跌，最高33.17元即为全天高点，午后最低30.18元逼近跌停价29.33元，全天振幅9.17%，成交22.59亿元，换手率6.29%，主力资金净流出2.53亿元。公司Q3单季净利润同比增长470%，业绩大超预期，但今日遭遇典型的“利好出尽”式砸盘——前期埋伏业绩的资金在业绩兑现后集中获利了结，MLCC被动元件板块整体暴跌4.34%。30元为关键心理关口。🔴操作建议：<strong>30元为止损底线，若有效跌破29.33元跌停价立即清仓1/2仓位；29-30元区间观察承接力度，不急于抄底；反弹至33元以上减仓1/3仓位</strong>。MLCC行业周期反转长期逻辑未变，但短线获利盘抛压较大，需等待情绪企稳。"
    },
]
gen.add_holdings_tracking(holdings=holdings)

# ============ 7. 龙虎榜深度解析（5只详细） ============
longhubang = [
    {"name": "文投控股", "code": "600715", "up": True, "change": "+10.04%（5天4板）", "institutions": 0,
     "reason": "日涨幅偏离值7%的证券", "net_buy": "+4.68亿（呼家楼主买+游资合力封板）"},
    {"name": "旋极信息", "code": "300324", "up": True, "change": "+17.58%（20CM涨停）", "institutions": 0,
     "reason": "GPU/算力芯片概念", "net_buy": "+2.40亿（东财拉萨天团主导）"},
    {"name": "儒意电影", "code": "0136.HK", "up": True, "change": "+9.96%（港股涨停）", "institutions": 0,
     "reason": "流浪地球3定档2027春节催化", "net_buy": "+1.14亿（呼家楼独买）"},
    {"name": "沪电股份", "code": "002463", "up": False, "change": "-10.00%（跌停）", "institutions": 0,
     "reason": "机构净卖出第一位", "net_buy": "-1.21亿（机构大幅抛售）"},
    {"name": "通化金马", "code": "000766", "up": True, "change": "+10.00%（涨停）", "institutions": 0,
     "reason": "日涨幅偏离值7%", "net_buy": "机构净卖1613万+北向净卖2147万"},
]
gen.add_dragon_tiger_list(stocks=longhubang)

# ============ 龙虎榜深度解读补充区 ============
lhb_deep_html = '''
<div style="display: flex; flex-direction: column; gap: 14px; margin-top: 8px;">
<div style="background: rgba(30,30,50,0.5); border: 1px solid rgba(255,255,255,0.08); border-radius: 14px; padding: 18px;">
    <h4 style="margin:0 0 10px; color:#f87171; font-size:14px;">🔍 龙虎榜深度解读</h4>
    <div style="font-size:13px; color:#cbd5e1; line-height:1.8;">
    <p style="margin:0 0 10px;"><strong style="color:#f1f5f9;">① 文投控股（5天4板·AI影视龙头）：</strong>
    今日龙虎榜净买入4.68亿元高居全市场第一，呼家楼等一线游资主导封板，叠加散户席位合力助攻。但5天4板后位置已高，累计涨幅超60%，
    属于典型的游资接力情绪票，普通投资者追高风险极大。若下周一继续一字板可观察，但开板后谨防天地板。</p>
    
    <p style="margin:0 0 10px;"><strong style="color:#f1f5f9;">② 旋极信息（20CM涨停·GPU概念）：</strong>
    龙虎榜净买入2.40亿元，但买入席位以东财拉萨天团（散户大本营）为主，缺乏机构和知名游资参与，
    换手率高达20.86%，振幅11.21%，属于典型的散户情绪套利标的，持续性较差，不建议追高接力。</p>
    
    <p style="margin:0 0 10px;"><strong style="color:#f1f5f9;">③ 儒意电影（《流浪地球3》定档催化）：</strong>
    港股儒意电影涨停，知名游资呼家楼席位独买1.14亿元，成为今日最受关注的游资动向之一。《流浪地球3》定档2027年大年初一，
    作为重要出品方将直接受益，但影视院线项目兑现周期长达一年多，短期纯情绪炒作，注意追高风险。</p>
    
    <p style="margin:0 0 10px;"><strong style="color:#ef4444;">④ 沪电股份（机构净卖第一·风险信号）：</strong>
    PCB龙头沪电股份今日跌停，龙虎榜显示机构净卖出1.21亿元，为今日全市场机构净卖出金额最大的个股。
    <strong style="color:#f87171;">这是一个非常重要的信号——机构对高位PCB/AI硬件方向的态度已从加仓转为坚决减仓</strong>，
    意味着AI算力硬件板块的中期调整可能刚刚开始，持有相关标的务必高度警惕，反弹就是减仓机会。</p>
    
    <p style="margin:0;"><strong style="color:#f1f5f9;">⑤ 通化金马（涨停但内外资双卖）：</strong>
    今日涨停看似强势，但龙虎榜显示机构净卖出1613万元、北向资金净卖出2147万元，典型的游资短炒行为，
    内外资主力都在借涨停出货，这种涨停板的持续性极差，追高被套概率很高。</p>
    </div>
</div>
</div>'''
gen._components.append(Section(title="🐉 龙虎榜深度解读", content=lhb_deep_html, icon="award"))

# ============ 8. 重点关注标的（4只） ============
focus_html = '''
<div style="display: flex; flex-direction: column; gap: 14px;">
<div style="background: linear-gradient(135deg, rgba(16,185,129,0.12), rgba(5,150,105,0.08)); border: 1px solid rgba(16,185,129,0.3); border-radius: 14px; padding: 16px;">
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
        <strong style="color:#34d399; font-size:15px;">🏦 江苏银行(600919) · 防御首选</strong>
        <span style="color:#34d399; font-weight:700;">创历史新高</span>
    </div>
    <p style="margin:0; font-size:13px; color:#cbd5e1; line-height:1.7;">
    <strong style="color:#f1f5f9;">关注逻辑：</strong>银行板块新龙头，连续8日阳线创历史新高，高股息（股息率约5.5%）+险资年末配置+资金避险三重逻辑共振，是当前市场最确定的方向之一。作为城商行标杆，资产质量优异，净息差企稳。
    <strong style="color:#fbbf24;">买入区间：</strong>回调至10日均线附近分批建仓，不追高；
    <strong style="color:#fbbf24;">目标价：</strong>突破历史新高后看10%上行空间；
    <strong style="color:#ef4444;">止损位：</strong>有效跌破20日均线止损。
    </p>
</div>

<div style="background: linear-gradient(135deg, rgba(59,130,246,0.12), rgba(99,102,241,0.08)); border: 1px solid rgba(96,165,250,0.3); border-radius: 14px; padding: 16px;">
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
        <strong style="color:#60a5fa; font-size:15px;">🐷 金新农(002548) · 猪周期龙头</strong>
        <span style="color:#10b981; font-weight:700;">首板涨停</span>
    </div>
    <p style="margin:0; font-size:13px; color:#cbd5e1; line-height:1.7;">
    <strong style="color:#f1f5f9;">关注逻辑：</strong>猪肉板块龙头之一，今日强势首板涨停突破年线。猪周期底部上行预期+年末腌腊消费旺季+农业防御属性三重催化，
    农业板块有望成为继银行之后又一个避险资金聚集方向。金新农作为生猪养殖弹性品种，猪价反弹时业绩弹性大。
    <strong style="color:#fbbf24;">买入区间：</strong>回踩涨停价（约8.5元附近）轻仓试探；
    <strong style="color:#fbbf24;">目标价：</strong>看板块持续性，第一目标前期高点10元；
    <strong style="color:#ef4444;">止损位：</strong>跌破涨停开盘价止损。
    </p>
</div>

<div style="background: linear-gradient(135deg, rgba(139,92,246,0.12), rgba(124,58,237,0.08)); border: 1px solid rgba(139,92,246,0.3); border-radius: 14px; padding: 16px;">
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
        <strong style="color:#a78bfa; font-size:15px;">💎 长电科技(600584) · 错杀机会</strong>
        <span style="color:#fbbf24; font-weight:700;">左侧布局</span>
    </div>
    <p style="margin:0; font-size:13px; color:#cbd5e1; line-height:1.7;">
    <strong style="color:#f1f5f9;">关注逻辑：</strong>全球第三大封测厂商，Q3业绩高增+资本开支上修至182亿，先进封装长期景气度确定，今日随板块暴跌属错杀。
    52元以下是较好的左侧布局区间，适合中线投资者分批建仓。
    <strong style="color:#fbbf24;">买入区间：</strong>50-52元分批建仓2-3成；
    <strong style="color:#fbbf24;">目标价：</strong>中期目标65-70元；
    <strong style="color:#ef4444;">止损位：</strong>有效跌破49元止损。
    </p>
</div>

<div style="background: linear-gradient(135deg, rgba(245,158,11,0.12), rgba(234,88,12,0.08)); border: 1px solid rgba(245,158,11,0.3); border-radius: 14px; padding: 16px;">
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
        <strong style="color:#fbbf24; font-size:15px;">⚠️ 风险警示：东山精密(002384)</strong>
        <span style="color:#ef4444; font-weight:700;">-9.95%天量暴跌</span>
    </div>
    <p style="margin:0; font-size:13px; color:#cbd5e1; line-height:1.7;">
    <strong style="color:#f1f5f9;">风险提示：</strong>今日成交153亿元天量暴跌逼近跌停，PCB龙头遭机构和游资联合抛售，主力净流出17.71亿元，技术形态彻底破位。
    若持有该股，<strong style="color:#ef4444;">反弹至90元以上坚决减仓离场</strong>，不要抱有反弹幻想。
    <strong style="color:#ef4444;">关键支撑：</strong>80元（60日线），跌破则打开进一步下跌空间；
    <strong style="color:#ef4444;">压力位：</strong>95元。
    </p>
</div>
</div>'''
gen._components.append(Section(title="⭐ 重点关注标的（机会+风险）", content=focus_html, icon="star"))

# ============ 9. 明日关键预判 ============
predictions = [
    {"name": "大盘指数", "direction": "震荡", "confidence": 70,
     "reason": "3600点整数关口有较强心理支撑，但科技股抛压尚未完全释放，预计下周一沪指在3600-3660点区间震荡整理，创业板指考验2400点支撑，科创50在1250-1300点区间震荡。银行股若继续强势可有效托住指数，但科技股盘中反抽大概率是减仓机会而非反转信号。"},
    {"name": "CPO/光模块", "direction": "看跌", "confidence": 65,
     "reason": "主力资金单日净流出227.6亿元，景旺电子跌停、机构净卖沪电股份1.21亿元，高位科技股筹码已明显松动，机构态度从加仓转为坚决减仓。下周一惯性下探概率较大，5日线已拐头向下形成强压力，不急于抄底，等待缩量企稳信号。"},
    {"name": "银行/高股息", "direction": "看涨", "confidence": 65,
     "reason": "5只银行股齐创历史新高，险资年末配置压力+资金避险需求+高股息吸引力三重逻辑，银行/保险/电力等高股息方向有望延续强势，但连续大涨后追高需谨慎，回调5日线是较好介入机会。"},
    {"name": "AI影视/短剧", "direction": "震荡", "confidence": 55,
     "reason": "文投控股5天4板、呼家楼买入儒意电影，板块情绪仍在但龙头位置已高，下周一分化加剧是大概率事件，后排跟风股可能率先掉队，只适合激进投资者快进快出，不做中长线配置。"},
]
gen.add_tomorrow_prediction(predictions=predictions)

# ============ 10. 明日操作计划 ============
plan = '''
<div style="background: rgba(30,30,50,0.5); border-radius: 16px; padding: 20px; border: 1px solid rgba(255,255,255,0.08);">
<p style="margin:0 0 12px;"><strong style="color:#fbbf24; font-size:16px;">📊 总仓位建议：由7成降至5成，现金留5成应对下周波动，科技仓位控制在4成以内</strong></p>

<p style="margin:0 0 10px;"><strong style="color:#ef4444;">🔴 第一优先级：减仓/止损操作（下周一开盘即执行）：</strong></p>
<ul style="margin:0 0 14px; padding-left:20px; font-size:13px; color:#cbd5e1; line-height:2;">
<li><strong style="color:#ef4444;">*ST建艺(002789)</strong>：下周一集合竞价<strong>挂8元跌停价无条件全仓清仓</strong>，退市风险股必须第一时间离场，不要抱有任何侥幸心理</li>
<li><strong style="color:#ef4444;">英维克(002837)</strong>：<strong>若跌破36.88元（跌停价）立即清仓出局</strong>；反弹至40-41元区间（今日开盘价附近）减仓1/2，<strong>坚决不补仓、不抄底</strong></li>
<li><strong style="color:#ef4444;">风华高科(000636)</strong>：<strong>若跌破29.33元（跌停价）减仓1/2</strong>；29-30元区间观察承接力度不急于抄底；反弹至33元以上减仓1/3</li>
<li><strong style="color:#ef4444;">雅克科技(002409)</strong>：若有效跌破82元减仓1/3；85-88元区间持有观望；反弹至92元以上减仓机动仓位</li>
<li><strong style="color:#ef4444;">东山精密/沪电股份等高位PCB</strong>：如持有，反弹至5日线附近坚决减仓，不格局</li>
</ul>

<p style="margin:0 0 10px;"><strong style="color:#10b981;">🟢 第二优先级：加仓/建仓观察（严格控制仓位，左侧轻仓试探）：</strong></p>
<ul style="margin:0 0 14px; padding-left:20px; font-size:13px; color:#cbd5e1; line-height:2;">
<li><strong style="color:#10b981;">长电科技(600584)</strong>：52元以下分批建仓2成仓位，50元整数关口加仓1成，总仓位不超过3成；若有效跌破49元立即止损出局；反弹至57元以上减仓获利了结</li>
<li><strong style="color:#10b981;">铜冠铜箔(301217)</strong>：66-67元区间小幅加仓1成底仓，若有效跌破65元（前期平台支撑）止损；反弹至73-75元区间减仓1/3机动仓</li>
<li><strong style="color:#10b981;">华海诚科(688535)</strong>：70-73元区间分批建仓2成仓位，若有效跌破68元（前期低点）止损；反弹至80元以上减仓</li>
<li><strong style="color:#60a5fa;">银行/高股息ETF（512800/515180）</strong>：拿出10%仓位配置高股息ETF对冲科技波动，作为底仓防御</li>
</ul>

<p style="margin:0 0 10px;"><strong style="color:#fbbf24;">🟡 第三优先级：观察等待（不加仓、不操作，等待信号）：</strong></p>
<ul style="margin:0 0 14px; padding-left:20px; font-size:13px; color:#cbd5e1; line-height:2;">
<li>CPO/光模块/液冷方向：等待出现连续2日缩量止跌+龙头反包阳线，再考虑回补，至少观望到下周二之后</li>
<li>猪肉/农业方向：观察金新农、天邦食品周一能否连板，若断板则放弃，不做后排接力</li>
<li>AI影视方向：文投控股若开板放量则止盈离场，不追高不接力</li>
</ul>

<p style="margin:0;"><strong style="color:#fbbf24;">⚠️ 交易纪律提醒：</strong>
今日高位科技股集体杀跌是非常明确的中期调整信号，不是简单的单日波动。<strong style="color:#f87171;">不抄底、不补仓、不抢反弹、不逆势加仓</strong>，
严格执行止损纪律是当前第一要务。空出来的资金耐心等待科技股出现明确企稳信号（连续2日缩量止跌+龙头股反包阳线）后再考虑进场。
下周一开盘后重点观察三大信号：①银行股能否延续强势继续创新高（高股息逻辑是否成立）；②CPO/PCB是否惯性下探后出现承接盘；③上证指数3600点整数关口支撑力度。
<strong>周末期间注意关注消息面变化，控制仓位安心度周末。</strong>
</p>
</div>'''
gen.add_trading_plan(plan=plan)

# ============ 11. 晚间重要新闻 ============
evening_news = [
    {"title": "央行：坚持实施适度宽松货币政策，加大逆周期调节力度", "content": "央行表示将继续实施适度宽松的货币政策，保持流动性合理充裕，引导金融机构加大对实体经济支持力度，社会融资规模和货币信贷总量合理增长。", "time": "11/13 18:00", "source": "央行官网", "tag": "宏观", "tag_variant": "primary"},
    {"title": "《流浪地球3》正式定档2027年大年初一，儒意电影涨停", "content": "《流浪地球3》定档2027年春节，儒意影业作为重要出品方港股涨停，呼家楼1.14亿抢筹，A股影视院线板块集体走强，文投控股5天4板。", "time": "11/13 16:30", "source": "证券时报", "tag": "题材", "tag_variant": "warning"},
    {"title": "5只银行股创历史新高，险资年末“哑铃型”配置加速加仓高股息", "content": "江苏银行、南京银行、青岛银行、成都银行、杭州银行今日均创历史新高，险资年末配置压力下高股息资产持续受青睐，银行板块主力净流入8.63亿元。", "time": "11/13 16:00", "source": "财联社", "tag": "资金", "tag_variant": "success"},
    {"title": "CPO/PCB主力资金净流出超400亿，机构砸盘高位科技股", "content": "中际旭创主力净流出29.42亿、新易盛21.15亿、东山精密17.71亿、天孚通信16.90亿，光模块板块整体净流出227.6亿，机构抛售态度坚决。", "time": "11/13 16:45", "source": "东方财富数据中心", "tag": "资金", "tag_variant": "danger"},
    {"title": "美股英伟达再创历史新高，博通、AMD同步走强", "content": "隔夜美股AI产业链全线大涨，英伟达续创历史新高，但A股相关板块高开低走，说明美股利好已被提前消化，“利好出货”迹象明显。", "time": "11/13 05:00", "source": "新浪财经", "tag": "海外", "tag_variant": "default"},
    {"title": "MLCC被动元件板块暴跌4.34%，风华高科、三环集团领跌", "content": "MLCC板块今日重挫，三环集团-8.89%、风华高科-6.84%，市场担忧消费电子需求复苏不及预期，叠加前期涨幅过大获利盘了结。", "time": "11/13 15:30", "source": "东方财富", "tag": "板块", "tag_variant": "danger"},
]
gen.add_evening_news(news_list=evening_news)

# ============ 12. 风险提示 ============
risks = [
    "高位科技股获利回吐风险：CPO/光模块/PCB/MLCC/液冷等AI算力硬件板块单日主力资金净流出超400亿元，机构态度已从加仓转为减仓，短期调整压力较大，切勿盲目抄底",
    "仓位过度集中风险：若科技板块仓位过重（>60%），下周一若继续杀跌将面临较大回撤，建议周末前将总仓位降至5成以下，科技仓位控制在4成以内",
    "ST退市风险：*ST建艺已跌停封单且无承接，退市风险高悬，必须无条件全部离场，不要抱有任何侥幸心理",
    "北向资金流向风险：北向资金今日对科技股态度分化，需持续跟踪外资动向，若北向连续净流出需进一步降低仓位",
    "周末消息面不确定性风险：重点关注中美关系动向、国内政策变化、美股科技股周末走势、地缘政治风险等因素，控制仓位安心度周末",
]
gen.add_risk_warning(risks=risks)

# ============ 发布 ============
print("Publishing...")
result = gen.publish(filename=f"{DATE}_盘后速递.html")
print(f"Result: {result}")
print("Done!")
