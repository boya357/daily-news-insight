#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""S级催化盘后扫描 - 2026-07-07（周二）
核心主题：存储超级周期"利好出尽"第一击+韩国3.5万亿芯片举国投资+大基金密集减持
"""
import sys, os
sys.path.insert(0, '/root/daily-news-insight')
os.chdir('/root/daily-news-insight')

from v3.generators.s_level_catalyst import SLevelCatalystGenerator
from v3.components.data import StockTags
from v3.components.layout import Section

DATE = "20260707"
TITLE = "存储利好出尽第一击+韩国举国芯片投资+大基金密集减持·7/7盘后S级催化"
SUBTITLE = "2026.07.07 · 盘后S级催化深度分析（周二·三星业绩炸表股价却暴跌）"

gen = SLevelCatalystGenerator(date_str=DATE, catalyst_title=TITLE, subtitle=SUBTITLE)

# === 1. 总览 ===
overview = (
    "7月7日（周二）盘后，全球半导体市场上演<b class='text-red-400'>「业绩最炸日=股价见顶日」</b>的经典剧本——"
    "三星电子Q2营业利润同比+1810%（89.4万亿韩元，超预期），但股价却暴跌近7%引发全球存储板块连环杀跌。"
    "A股半导体逆势分化，设备/硅片/封测走强（华天科技涨停封测120亿成交），存储芯片高开低走收跌。"
    "盘后重磅事件密集：韩国宣布3.5万亿人民币史上最大芯片投资计划、大基金一日三度减持半导体（沪硅产业拟减2%）。"
    "市场进入「业绩兑现期+高低切换」关键窗口，<b>中报是唯一试金石，无业绩高位票坚决规避</b>。\n\n"
    "①【S+·存储超级周期利好出尽第一击·三星炸表却暴跌】三星电子Q2营业利润89.4万亿韩元（约580亿美元）同比暴增1810%，"
    "营收171万亿韩元同比+129%，双双超预期——但韩股却暴跌-6.97%、SK海力士-6.5%、日股铠侠-11%。"
    "美股盘前连环杀跌：美光-6%、闪迪-6%、西部数据-7%、AMD-4%、英特尔-3.4%，纳指100期货-0.85%。"
    "核心逻辑：<b>股价已提前price-in（三星年涨158%、海力士年涨273%），市场从「看利润增速」转向「看现金流与股东回报」</b>，"
    "摩根士丹利等机构提示「存储涨价周期已进入下半场」。对A股传导：存储高位票（兆易创新/江波龙/北京君正等）短期承压，"
    "但设备/材料/封测等「卖铲人」因韩国3.5万亿扩产计划反而获得新增长逻辑。\n\n"
    "②【S+·韩国3.5万亿人民币举国芯片投资·设备材料大时代】韩国政府官宣史上最大半导体产业规划："
    "在西南部光州、全罗地区布局4座高端存储晶圆厂，总投资800万亿韩元（约3.5万亿人民币），"
    "三星+SK海力士各2座，聚焦DRAM/3D NAND及中端HBM，目标5年内全国DRAM产能翻倍。"
    "叠加此前三星4755万亿韩元（约3万亿美元）15年本土投资+SK海力士1100万亿韩元计划，"
    "韩国存储扩产进入「举国体制」阶段。SEMI预测2026全球300mm存储设备投资首破500亿美元（+29%），"
    "中国大陆设备支出940亿美元全球第一（25%占比）。<b>设备/零部件/材料是本轮扩产最确定受益链条</b>。\n\n"
    "③【S·大基金一日三减·半导体国家队高位兑现】7月7日盘后/盘前，大基金三度出手减持："
    "(a) 沪硅产业盘后公告：大基金拟减持不超2%（约22.88亿元）；"
    "(b) 德邦科技：大基金5/14-7/6累计减持3%（约3.64亿元），减持完毕；"
    "(c) 兴福电子：大基金二期6/17-7/6减持1%（360万股），持股降至5.94%。"
    "大基金在半导体板块反弹之际密集减持，信号意义强：<b>国家队在「国产替代核心标的」上有序兑现，"
    "不改变长期产业方向，但短期对情绪有压制</b>。历史规律：大基金减持后相关标的短期承压1-2周，但中期仍看基本面。\n\n"
    "④【S·龙虎榜资金高低切换·机构狂买封测/设备】今日龙虎榜55只个股现机构席位，机构合计净买入29.01亿元，"
    "但结构极端分化——华天科技（封测龙头）机构净买1.91亿+深股通6.45亿+游资7.41亿，合计净买15.77亿元涨停，"
    "成交119.99亿创历史天量；东方钽业机构净买8.44亿；惠科股份机构净买7.64亿；TCL中环机构净买0.58亿。"
    "另一边：埃斯顿机构净卖5.28亿、美诺华-1.27亿、黄河旋风-1.25亿。"
    "北向资金今日净买66亿，52亿集中在半导体设备32.7亿+存储芯片11.4亿+高端装备7.9亿。"
    "<b>资金从高位AI题材/纯概念向「有业绩+低估值+硬科技」切换</b>，半导体设备PE 28倍（27%分位）+中报预增50%-120%是核心吸引力。\n\n"
    "⑤【A+·持仓复盘·三只持仓守住关键支撑】英维克收71.29（-3.74%）冲高76.88回落，长上影线再逼近70生死线；"
    "铜冠铜箔收144.82（+0.45%）小阳十字星企稳，143-145区间有承接；"
    "雅克科技收185.82（-0.34%）小阴企稳，最低181接近180关键支撑；"
    "*ST建艺收10.20（-9.97%）首日10%跌幅即跌停封板，开板即清仓。"
    "整体：四只持仓中三只科技股均在关键支撑位，明日若美股半导体继续大跌需警惕破位风险。\n\n"
    "⚡ 明日核心判断：存储板块在三星「业绩顶」信号下进入分化调整期，设备/材料/封测因扩产逻辑相对抗跌；"
    "大盘缩量5100亿至2.58万亿+超4700只下跌，市场情绪极弱，<b>仓位严格3成以内</b>，"
    "半导体方向只做「设备+封测+材料」三低方向（低估值+低位+低涨幅），高位存储票反抽减仓。"
)
gen.add_catalyst_overview(overview=overview, importance="极高")

# === 2. 背景与触发 ===
background = (
    "一、全球半导体周期大背景：从「涨价预期」进入「业绩兑现+扩产能」阶段\n"
    "2026年上半年，全球半导体特别是存储板块经历史诗级上涨——三星电子累计+158%、SK海力士+273%、"
    "美光+超200%、闪迪+300%+，核心驱动是AI服务器+HBM带来的存储超级周期，DRAM/NAND价格连续6个季度上涨。"
    "但进入7月，市场开始定价「涨价周期下半场」：DRAM Q3预计涨10-20%（原预期5-10%），"
    "但Q4涨幅可能收窄至5-10%，2027年供需格局因韩美大厂大规模扩产可能趋于平衡。\n\n"
    "二、三星Q2业绩超预期但未「炸裂到震撼」\n"
    "三星Q2营业利润89.4万亿韩元（超预期84.2万亿），同比+1810%，营收171万亿韩元（超预期169.2万亿）。"
    "按业务拆分估算：半导体部门约65-70万亿（存储约55-60万亿）、手机约10-12万亿、显示约5-7万亿。"
    "市场「利好出尽」逻辑：(1) 股价已提前涨了一年多，估值已反映大部分预期；"
    "(2) 投资者关注焦点从「利润增速」转向「自由现金流+股东回报」，市场期待更大规模回购/分红未兑现；"
    "(3) 摩根士丹利等机构提示「存储涨价最快的阶段已过去」，Q4及2027年增速可能放缓。\n\n"
    "三、A股半导体分化的底层逻辑：高低切换+中报验证\n"
    "今日A股半导体内部严重分化——半导体设备（+3.2%）、半导体硅片（+4.5%）、封测（+2.8%）走强，"
    "但存储芯片（-2.1%）、PCB（-3.5%）、光模块（-2.8%）走弱。背后核心是「资金从高位兑现转向低位布局」："
    "(1) 设备板块PE 28倍（近三年27%分位），中报预增50%-120%，估值业绩匹配度高；"
    "(2) 存储板块PE普遍已60-80倍，部分标的PE超100倍，需要中报验证才能消化估值；"
    "(3) 北向+机构+游资三方合力向设备/硅片/封测流动，华天科技120亿成交是标志性事件。"
)

trigger = (
    "触发事件一（15:00收盘后）：三星电子Q2业绩炸表+韩国宣布800万亿韩元新晶圆厂投资\n"
    "· 三星发布Q2初步财报：营业利润89.4万亿韩元（+1810%），营收171万亿韩元（+129%），双双超预期\n"
    "· 韩国政府官宣：在西南部光州、全罗布局4座高端存储晶圆厂，总投资800万亿韩元（约3.5万亿人民币）\n"
    "· 韩股反应：三星电子-6.97%、SK海力士-6.5%、KOSPI两度触发熔断\n\n"
    "触发事件二（16:00-18:00）：大基金密集减持半导体+龙虎榜数据出炉\n"
    "· 沪硅产业盘后公告：大基金拟减持不超2%（约22.88亿元）\n"
    "· 德邦科技、兴福电子大基金减持进展公告\n"
    "· 龙虎榜：华天科技机构+深股通+游资合计净买15.77亿涨停，机构合计净买入29亿\n"
    "· 北向资金净买66亿，52亿集中在半导体设备+存储+高端装备\n\n"
    "触发事件三（20:00前）：美股盘前存储板块连环杀跌\n"
    "· 美光科技盘前-6%、闪迪-6%、西部数据-7%、AMD-4%、博通-2%\n"
    "· 纳指100期货-0.85%、标普500期货-0.14%、道指期货+0.23%\n"
    "· SOXS三倍做空半导体ETF盘前+9%\n"
    "· 港股存储板块同步大跌：兆易创新-12%、澜起科技-10%"
)
gen.add_catalyst_details(background=background, trigger=trigger)

# === 3. 产业链分析 ===
gen.add_industry_chain_analysis(
    upstream=[
        {"name": "半导体设备", "leader": "北方华创、中微公司、盛美上海、拓荆科技", "logic": "韩国3.5万亿扩产+长江存储三期国产设备占比破50%，设备订单排到2027年末，SEMI上调2026全球存储设备投资至520亿美元（+29%）"},
        {"name": "半导体材料", "leader": "沪硅产业、有研硅、雅克科技、安集科技", "logic": "硅片/前驱体/光刻胶/电子特气等上游材料随晶圆厂扩产持续放量，国产替代加速，沪硅产业大基金减持不改长期逻辑"},
        {"name": "半导体零部件", "leader": "富创精密、新莱应材、英杰电气", "logic": "设备扩产最先受益的是零部件，国产替代率从10%向30%提升，弹性最大"},
    ],
    midstream=[
        {"name": "晶圆制造/封测", "leader": "中芯国际、华天科技、长电科技、通富微电", "logic": "封测三巨头合计220亿扩产，华天科技今日120亿天量涨停+机构深股通游资三方抢筹，2.5D/3D先进封装需求持续爆发"},
        {"name": "存储芯片", "leader": "兆易创新、江波龙、北京君正、佰维存储", "logic": "涨价周期进入下半场，业绩兑现但估值已高，三星「业绩顶」信号下短期承压，分化加剧——有产能有客户的龙头相对抗跌"},
        {"name": "AI芯片/GPU", "leader": "寒武纪、海光信息、龙芯中科", "logic": "国内AI芯片自主可控逻辑不变，但短期受美股半导体情绪影响较大，寒武纪今日+4.5%相对强势"},
    ],
    downstream=[
        {"name": "AI服务器/算力", "leader": "工业富联、浪潮信息、中科曙光", "logic": "AI服务器需求仍在增长，但市场担忧CAPEX见顶，PCB/光模块等配套环节前期涨幅大调整压力大"},
        {"name": "消费电子/手机", "leader": "立讯精密、歌尔股份、蓝思科技", "logic": "消费电子复苏缓慢，苹果链相对确定，安卓链仍在去库存，整体弹性弱于AI链"},
        {"name": "汽车电子", "leader": "德赛西威、均胜电子、华阳集团", "logic": "智能驾驶+车规半导体需求增长确定，但车规认证周期长，短期弹性不如AI链"},
    ]
)

# === 4. 投资机会 ===
opportunities = [
    {
        "name": "S+：半导体设备——全球扩产周期最确定受益链",
        "priority": "高",
        "logic": (
            "韩国3.5万亿举国投资+长江存储三期+合肥长鑫扩产+美光日本扩厂，全球存储扩产进入超级周期。"
            "SEMI预测2026全球300mm存储设备投资首破500亿美元（+29%），中国大陆设备支出940亿美元全球第一。"
            "设备板块PE仅28倍（近三年27%分位），中报预增50%-120%，估值业绩匹配度高。"
            "今日北向资金净买半导体设备32.7亿，是资金高低切换的核心方向。"
            "核心逻辑：<b>卖铲人永远比挖金人先赚钱</b>，扩产周期中设备订单先于晶圆厂盈利兑现。"
        ),
        "stocks": [
            {"code": "002371", "name": "北方华创", "impact": "设备龙头全覆盖"},
            {"code": "688012", "name": "中微公司", "impact": "刻蚀设备龙头"},
            {"code": "688082", "name": "盛美上海", "impact": "清洗设备+电镀设备"},
            {"code": "688072", "name": "拓荆科技", "impact": "薄膜沉积设备"},
        ],
    },
    {
        "name": "S：先进封装/封测——AI算力的「最后一公里」",
        "priority": "高",
        "logic": (
            "AI芯片性能提升越来越依赖先进封装（CoWoS/2.5D/3D），日月光CoWoS已涨价55%排到2027Q4。"
            "今日华天科技涨停+119.99亿成交创历史天量，机构+深股通+游资三方合计净买入15.77亿，是资金认可度最高的方向。"
            "封测三巨头近期集中披露百亿扩产计划（合计超220亿），产业资本用真金白银投票。"
            "核心逻辑：<b>HBM需求爆发→先进封装产能紧缺→封测厂量价齐升</b>，"
            "A股封测估值显著低于海外（日月光/安靠），仍有提升空间。"
        ),
        "stocks": [
            {"code": "002185", "name": "华天科技", "impact": "今日涨停龙一，封测+存储封测"},
            {"code": "600584", "name": "长电科技", "impact": "封测龙头，先进封装领先"},
            {"code": "002156", "name": "通富微电", "impact": "AMD核心封测伙伴"},
        ],
    },
    {
        "name": "S：半导体硅片/材料——扩产直接受益者",
        "priority": "高",
        "logic": (
            "全球晶圆厂扩产→硅片需求增长，国产替代加速。今日有研硅20cm涨停、有研新材10cm涨停、"
            "沪硅产业涨超8%、上海合晶+12.85%，硅片板块集体走强。"
            "逻辑：存储扩产需要大量12寸硅片，国内硅片厂商从追赶走向替代，沪硅产业/立昂微/有研硅等受益。"
            "大基金减持沪硅产业是短期情绪扰动，不改产业趋势。"
            "材料方向：雅克科技（前驱体+电子特气）、安集科技（CMP抛光液）、鼎龙股份（CMP抛光垫）等持续受益。"
        ),
        "stocks": [
            {"code": "688432", "name": "有研硅", "impact": "硅片+半导体材料"},
            {"code": "688126", "name": "沪硅产业", "impact": "12寸硅片龙头（注意大基金减持）"},
            {"code": "002409", "name": "雅克科技", "impact": "HBM前驱体+电子特气（持仓）"},
        ],
    },
    {
        "name": "A：存储芯片——分化加剧，只做真龙头",
        "priority": "中",
        "logic": (
            "三星「业绩顶」信号下，存储板块短期进入调整期，但产业基本面未变——"
            "Counterpoint预测Q3 DRAM价格仍涨10-20%，高于原预期5-10%。"
            "关键是<b>分化</b>：有产能有客户的龙头（如兆易创新/江波龙）可能高位震荡，"
            "而纯概念/无业绩/估值过高的小票可能大幅回调。"
            "操作策略：高位存储票反抽减仓，等待中报验证后再决定是否接回；"
            "若回调20-30%且中报业绩超预期，反而是布局Q4行情的机会。"
        ),
        "stocks": [
            {"code": "603986", "name": "兆易创新", "impact": "存储设计龙头，NOR Flash+DRAM"},
            {"code": "301308", "name": "江波龙", "impact": "存储模组龙头，中报暴增744倍"},
            {"code": "300223", "name": "北京君正", "impact": "车载存储+SRAM"},
        ],
    },
]
gen.add_investment_opportunities(opportunities=opportunities, view_mode="tab")

# === 5. 持仓分析 + 投资策略 合并 ===
strategy_full = f'''
<div style="padding: 4px;">
<h3 style="color: #f87171; margin: 0 0 14px; font-size: 16px; display: flex; align-items: center; gap: 8px;">
    📊 持仓四剑客盘后深度复盘
</h3>

<div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 12px; margin-bottom: 16px;">
    <div style="background: rgba(239,68,68,0.08); border: 1px solid rgba(239,68,68,0.2); border-radius: 10px; padding: 14px; border-left: 3px solid #ef4444;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
            <span style="font-weight: 700; color: #f1f5f9;">英维克 002837</span>
            <span style="color: #f87171; font-weight: 700;">-3.74%</span>
        </div>
        <div style="color: #cbd5e1; font-size: 12px; line-height: 1.8;">
            收71.29元｜最高76.88｜最低71.05｜成交37.05亿<br>
            <b style="color: #fbbf24;">技术面：</b>长上影线冲高回落，反弹失败信号，70元生死线岌岌可危<br>
            <b style="color: #fbbf24;">估值面：</b>PE(TTM) 188倍、PB 26倍，估值仍处历史90%+分位<br>
            <b style="color: #fbbf24;">资金面：</b>5日主力净流出14.86亿，机构持续兑现<br>
            <b style="color: #f87171;">明日操作：</b>73-75区间是最后减仓窗口，<b>破70元无条件清仓</b>
        </div>
    </div>
    
    <div style="background: rgba(245,158,11,0.08); border: 1px solid rgba(245,158,11,0.2); border-radius: 10px; padding: 14px; border-left: 3px solid #f59e0b;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
            <span style="font-weight: 700; color: #f1f5f9;">铜冠铜箔 301217</span>
            <span style="color: #22c55e; font-weight: 700;">+0.45%</span>
        </div>
        <div style="color: #cbd5e1; font-size: 12px; line-height: 1.8;">
            收144.82元｜最高149.23｜最低140.61｜成交44.38亿<br>
            <b style="color: #fbbf24;">技术面：</b>小阳十字星企稳，143-145区间有承接，5日线向下压制<br>
            <b style="color: #fbbf24;">估值面：</b>PE(TTM) 731倍、PB 21.8倍，估值极高，靠AI/CCL预期支撑<br>
            <b style="color: #fbbf24;">资金面：</b>主力近5日净流出，国轩高科前期减持已兑现<br>
            <b style="color: #22c55e;">明日操作：</b>140-145震荡，<b>不破140可持有底仓1/3</b>，反弹150+减仓
        </div>
    </div>
    
    <div style="background: rgba(245,158,11,0.08); border: 1px solid rgba(245,158,11,0.2); border-radius: 10px; padding: 14px; border-left: 3px solid #f59e0b;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
            <span style="font-weight: 700; color: #f1f5f9;">雅克科技 002409</span>
            <span style="color: #f87171; font-weight: 700;">-0.34%</span>
        </div>
        <div style="color: #cbd5e1; font-size: 12px; line-height: 1.8;">
            收185.82元｜最高193.33｜最低181.00｜成交54.49亿<br>
            <b style="color: #fbbf24;">技术面：</b>三连跌后小阴企稳，180元是关键支撑位（前期平台+60日线）<br>
            <b style="color: #fbbf24;">估值面：</b>PE(TTM) 88倍、PB 7.8倍，处于历史60%分位，估值尚可<br>
            <b style="color: #fbbf24;">资金面：</b>7/2-7/6三日主力净流出超16亿，今日有企稳迹象<br>
            <b style="color: #22c55e;">明日操作：</b>180元多空分水岭，<b>守住保留底仓1/2</b>，破180减至1/4
        </div>
    </div>
    
    <div style="background: rgba(220,38,38,0.1); border: 1px solid rgba(220,38,38,0.3); border-radius: 10px; padding: 14px; border-left: 3px solid #dc2626;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
            <span style="font-weight: 700; color: #f1f5f9;">*ST建艺 002789</span>
            <span style="color: #dc2626; font-weight: 700;">-9.97% 跌停</span>
        </div>
        <div style="color: #cbd5e1; font-size: 12px; line-height: 1.8;">
            收10.20元｜跌停封板｜成交5372万｜换手率3.28%<br>
            <b style="color: #fbbf24;">基本面：</b>Q1净亏5311万（-69%），未分配亏损超27亿<br>
            <b style="color: #fbbf24;">资金面：</b>主力净流出1501万（占成交28%），封单坚决<br>
            <b style="color: #fbbf24;">估值面：</b>PB 11.89倍（亏损股无PE），估值极高<br>
            <b style="color: #dc2626;">明日操作：</b><b>任何开板机会立即清仓</b>，预计还有2-3个跌停
        </div>
    </div>
</div>

<div style="background: linear-gradient(90deg, rgba(59,130,246,0.15), transparent); border-radius: 8px; border-left: 3px solid #3b82f6; padding: 12px; margin-bottom: 16px;">
    <div style="color: #93c5fd; font-weight: 700; margin-bottom: 6px;">📌 明日持仓优先级排序（7/8周三）</div>
    <div style="color: #e2e8f0; font-size: 13px; line-height: 2;">
        <b style="color: #f87171;">🚨 第一优先级：</b>*ST建艺开板即清仓，不计成本，绝不犹豫<br>
        <b style="color: #f87171;">🚨 第二优先级：</b>英维克73-75减仓窗口，破70无条件清仓，纪律第一<br>
        <b style="color: #fbbf24;">⚡ 第三优先级：</b>雅克科技守180 / 铜冠铜箔守140，不破位持有底仓，破位减仓<br>
        <b style="color: #22c55e;">💡 仓位控制：</b>整体仓位严格控制在3成以内，现金为王应对极端行情
    </div>
</div>

<h3 style="color: #fbbf24; margin: 18px 0 14px; font-size: 16px; display: flex; align-items: center; gap: 8px;">
    🎯 明日操作全攻略
</h3>

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px; margin-bottom: 16px;">
    <div style="background: linear-gradient(135deg, rgba(34,197,94,0.1), rgba(22,163,74,0.05)); border: 1px solid rgba(34,197,94,0.3); border-radius: 12px; padding: 16px;">
        <h4 style="color: #4ade80; margin: 0 0 10px; font-size: 14px;">✅ 进攻方向（轻仓参与）</h4>
        <ul style="color: #bbf7d0; margin: 0; padding-left: 18px; font-size: 12px; line-height: 2;">
            <li><b>半导体设备</b>：北方华创/中微公司/盛美上海，回调5-10%低吸，仓位5-8%</li>
            <li><b>先进封装/封测</b>：华天科技/长电科技/通富微电，关注华天能否连板定情绪</li>
            <li><b>半导体材料</b>：雅克科技守180可持底仓，沪硅产业需消化减持压力</li>
            <li><b>核心逻辑</b>：韩国3.5万亿扩产+国内存储扩产+国产替代三重共振</li>
        </ul>
    </div>

    <div style="background: linear-gradient(135deg, rgba(239,68,68,0.1), rgba(220,38,38,0.05)); border: 1px solid rgba(239,68,68,0.3); border-radius: 12px; padding: 16px;">
        <h4 style="color: #fca5a5; margin: 0 0 10px; font-size: 14px;">❌ 规避方向</h4>
        <ul style="color: #fecaca; margin: 0; padding-left: 18px; font-size: 12px; line-height: 2;">
            <li>高位存储纯概念股（无业绩+PE超100倍+上半年涨3倍+）</li>
            <li>ST板块全部规避（除清仓*ST建艺外不碰任何ST）</li>
            <li>高位AI题材小票（光模块/PCB/液冷等前期大牛股，反抽减仓）</li>
            <li>贵金属短期规避（COMEX黄金回调压力），等待回调后再布局</li>
            <li>大基金减持标的短期规避（沪硅产业等需消化1-2周）</li>
        </ul>
    </div>
</div>

<div style="background: linear-gradient(135deg, rgba(168,85,247,0.12), rgba(139,92,246,0.06)); border: 1px solid rgba(168,85,247,0.3); border-radius: 12px; padding: 16px;">
    <h4 style="color: #d8b4fe; margin: 0 0 10px; font-size: 14px;">🌙 隔夜外盘重点关注（7/7晚-7/8晨）</h4>
    <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px;">
        <div style="background: rgba(0,0,0,0.2); border-radius: 8px; padding: 10px;">
            <div style="color: #a78bfa; font-weight: 700; font-size: 12px; margin-bottom: 4px;">📈 指数层面</div>
            <div style="color: #e2e8f0; font-size: 11px; line-height: 1.7;">
                纳指/标普/道指收盘表现<br>
                费半指数涨跌幅<br>
                VIX恐慌指数变化
            </div>
        </div>
        <div style="background: rgba(0,0,0,0.2); border-radius: 8px; padding: 10px;">
            <div style="color: #a78bfa; font-weight: 700; font-size: 12px; margin-bottom: 4px;">🔬 核心半导体</div>
            <div style="color: #e2e8f0; font-size: 11px; line-height: 1.7;">
                美光/英伟达/AMD走势<br>
                台积电ADR/博通/ASML<br>
                西部数据/闪迪表现
            </div>
        </div>
        <div style="background: rgba(0,0,0,0.2); border-radius: 8px; padding: 10px;">
            <div style="color: #a78bfa; font-weight: 700; font-size: 12px; margin-bottom: 4px;">📰 关键事件</div>
            <div style="color: #e2e8f0; font-size: 11px; line-height: 1.7;">
                美联储6月会议纪要（明晨）<br>
                SK海力士ADR上市前动态<br>
                美光/英特尔财报指引
            </div>
        </div>
    </div>
</div>

<div style="margin-top: 14px; padding: 14px; background: rgba(251,191,36,0.1); border: 1px solid rgba(251,191,36,0.3); border-radius: 12px;">
    <div style="color: #fde047; font-weight: 700; margin-bottom: 8px; font-size: 14px;">⚡ 核心口诀</div>
    <div style="color: #fef3c7; font-size: 13px; line-height: 1.9;">
        <b style="font-size: 15px;">存储顶、设备起，封测涨停是信号；大基金、有序退，高低切换要记牢。</b><br>
        三星业绩炸表股价跌，利好出尽第一条；韩国投资三万亿，设备材料最受益。<br>
        英维克逼近七十线，破位清仓莫犹豫；建艺跌停开板走，纪律执行保本金。<br>
        仓位三成现金多，中报季里求真龙；缩量阴跌不言底，等待放量再进场。
    </div>
</div>

</div>
'''
gen.add_investment_strategy(strategy_full)

# === 6. 风险警示 ===
risks = [
    "美股半导体崩盘风险：三星业绩顶信号下，若美光/英伟达/AMD等持续大跌，A股半导体将二次探底，需警惕情绪传导",
    "大基金减持扩散风险：若大基金减持从沪硅产业/德邦科技/兴福电子扩散到更多核心标的，将对半导体板块情绪形成持续压制",
    "存储涨价周期见顶风险：若Q4 DRAM/NAND涨价幅度不及预期或2027年供需反转，存储板块估值将大幅下修",
    "宏观流动性风险：美联储若因通胀粘性推迟降息，全球风险资产承压，A股科技股估值面临压力",
    "中报业绩雷风险：7-8月中报密集披露期，高位高估值个股若业绩不及预期将面临戴维斯双杀",
    "持仓个股破位风险：英维克逼近70元生死线，雅克科技180元/铜冠铜箔140元若有效跌破将触发新一轮下跌",
]
gen.add_risk_warning(risks=risks)

# === 7. 发布 ===
output_filename = f"{DATE}_盘后_S级催化扫描_存储利好出尽第一击+韩国举国芯片投资.html"
result = gen.publish(
    title=f"S级催化盘后 {DATE} - 存储利好出尽+韩国3.5万亿芯片投资+大基金减持",
    report_type="s_level_catalyst",
    filename=output_filename,
    excerpt="7/7盘后：三星Q2利润+1810%但股价暴跌-7%（利好出尽第一击），韩国宣布800万亿韩元（3.5万亿人民币）4座晶圆厂举国投资计划，大基金一日三减（沪硅产业拟减2%），龙虎榜机构狂买华天科技15.77亿；持仓英维克逼近70生死线、*ST建艺跌停、雅克/铜冠守支撑。",
    auto_deploy=True,
)
print(f"=== PUBLISH RESULT ===")
print(result)
