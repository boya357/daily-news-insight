#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
盘后速递生成脚本 - 2026年8月17日
使用V3.0 AftermarketGenerator生成
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'v3'))
os.chdir('/root/daily-news-insight')

from v3.generators.aftermarket import AftermarketGenerator

gen = AftermarketGenerator(
    date_str="20260817",
    subtitle="2026.08.17 · 盘后速递"
)

# ========== 1. 今日核心亮点 ==========
gen.add_today_highlight(
    "科创50暴涨4.14%领跑全场，半导体板块全线爆发，存储芯片+先进封装双主线共振。"
    "长鑫科技尾盘拉升涨12%市值破4万亿，通富微电涨停获10亿资金抢筹。"
    "沪指重返3982点逼近4000关口，两市成交2.39万亿放量普涨，赚钱效应约80%。"
)

# ========== 2. 市场收盘总结 ==========
gen.add_market_summary(
    indices=[
        {"name": "上证指数", "value": "3982.65", "change": "+1.41%", "up": True, "icon": "trending_up"},
        {"name": "深证成指", "value": "14704.27", "change": "+2.44%", "up": True, "icon": "trending_up"},
        {"name": "创业板指", "value": "3740.16", "change": "+3.14%", "up": True, "icon": "trending_up"},
        {"name": "科创50", "value": "1788.85", "change": "+4.14%", "up": True, "icon": "trending_up"},
    ],
    volume="2.39万亿",
    northbound="成交2997亿 / 净流出约36亿"
)

# ========== 3. 情绪温度计 ==========
gen.add_sentiment_thermometer(
    temperature=78,
    volume="2.39万亿",
    up_count="4335",
    down_count="1064",
    limit_up_count="110"
)

# ========== 4. 板块涨幅/跌幅榜 ==========
gen.add_sector_performance(
    up_sectors=[
        {"name": "国家大基金持股", "change": "+5.60%", "leader": "长鑫科技/中微公司", "reason": "大基金三期投资加速落地，半导体设备材料国产化率提升预期强化，叠加长江存储市占率跻身全球第三，国产替代逻辑持续兑现。"},
        {"name": "存储芯片", "change": "+4.67%", "leader": "长鑫科技+12%/通富微电涨停", "reason": "SK海力士董事长警告明年出现最严重'存储荒'，闪迪投资者日上修长期财务目标至中高双位数增长，存储超级周期再获产业端强验证。板块主力净流入231亿，45股净流入超亿元。"},
        {"name": "先进封装", "change": "+4.54%", "leader": "通富微电涨停/长电科技+9%", "reason": "ABF材料供应紧张催化国产替代，味之素削减中国大陆30%供货量，华正新材、宏昌电子涨停。台积电CoWoS产能持续满载，先进封装供需缺口延续至2027年。"},
        {"name": "CPO/光模块", "change": "+4.22%", "leader": "太辰光20cm涨停", "reason": "英伟达Spectrum-X以太网硅光交换机进入全面量产阶段，200G/lane CPO商业化落地提速，激光器数量减至1/4、功耗降至1/5，光模块产业链价值重估。"},
        {"name": "光刻胶/半导体材料", "change": "+4.19%", "leader": "雅克科技+5.15%/有研新材涨停", "reason": "半导体涨价效应从存储向设备材料扩散，摩根大通研报指出设备材料供应商正通过提价稳步提升毛利率。雅克科技主力净流入3.71亿，HBM前驱体材料龙头地位稳固。"},
        {"name": "电子(申万)", "change": "+4.61%", "leader": "半导体全产业链", "reason": "申万一级行业涨幅第一，科创板半导体成分股集体爆发，长鑫科技4万亿市值引领，半导体设备、材料、封测、设计全产业链共振上行。"},
        {"name": "通信(申万)", "change": "+4.19%", "leader": "太辰光/中际旭创", "reason": "光模块CPO产业链领涨，叠加AI算力基础设施建设持续加速，800G/1.6T光模块需求旺盛，上游光芯片、光器件同步受益。"},
        {"name": "有色金属", "change": "+2.86%", "leader": "铜/黄金板块", "reason": "全球半导体扩产带动铜箔等电子材料需求，叠加贵金属避险属性，铜冠铜箔涨7.45%创新高，中金黄金涨超4%。"},
    ],
    down_sectors=[
        {"name": "白酒/食品饮料", "change": "-1.87%", "leader": "贵州茅台-3.64%", "reason": "茅台上半年归母净利润同比下滑1.95%，出现上市以来罕见'增收不增利'，白酒板块集体重挫，资金从消费向科技切换。"},
        {"name": "传媒/游戏", "change": "-0.84%", "leader": "恺英网络-4%/中国电影-2%", "reason": "暑期档票房不及预期，游戏板块受政策监管担忧影响，资金从传媒板块流向科技成长主线。"},
        {"name": "煤炭", "change": "-0.5%", "leader": "煤炭板块整体走弱", "reason": "传统能源板块在科技股行情中相对滞涨，市场风险偏好提升下资金从防御板块流出，转向高弹性科技成长。"},
    ]
)

# ========== 5. 盘面深度解读 ==========
gen.add_market_deep_analysis(
    strong_sectors=[
        {"name": "存储芯片", "reason": "SK海力士警告'存储荒'+闪迪上修指引双重催化，长鑫科技市值破4万亿引爆板块情绪，主力净流入231亿，40余股涨停或涨超10%。"},
        {"name": "先进封装", "reason": "ABF材料减供+国产替代逻辑共振，通富微电涨停获10亿抢筹，CoWoS产能紧缺持续，封测龙头价值重估进行中。"},
        {"name": "半导体设备", "reason": "全球存储大厂扩产+国内厂商业绩超预期，长江存储市占率跻身全球第三，设备国产化率提升空间大，中科飞测、长川科技领涨。"},
    ],
    weak_sectors=[
        {"name": "白酒消费", "reason": "茅台中报增收不增利打击信心，消费复苏节奏放缓，机构资金持续从消费白马向科技成长调仓。"},
        {"name": "传媒游戏", "reason": "暑期档票房平淡+游戏版号节奏担忧，板块缺乏催化，在科技主线虹吸效应下资金流出。"},
    ],
    core_view="今日市场呈现典型的'科技主攻、消费领跌'结构，科创50暴涨4.14%领跑全场，沪深两市成交2.39万亿放量普涨。核心驱动来自三条主线：一是存储芯片超级周期再获产业端强验证（SK海力士+闪迪），二是先进封装ABF材料紧张催化国产替代加速，三是CPO硅光交换机量产落地打开新成长空间。北向资金日内净流出约36亿但不影响内资主导的科技行情。技术面上沪指重返3982点逼近4000关口，创业板指站稳3700点，科创50突破前高，中期趋势仍向上。操作上建议聚焦半导体+AI算力主线，逢低布局存储、先进封装、设备材料三大方向，同时警惕高位股波动加剧风险。"
)

# ========== 6. 持仓股深度诊断 ==========
gen.add_holdings_tracking(
    holdings=[
        {
            "name": "英维克",
            "code": "002837",
            "price": "58.69",
            "change": "+2.80%",
            "up": True,
            "comment": """<strong>【当日表现】</strong>收盘58.69元，涨2.80%，成交23.81亿，换手率3.64%，最高58.69元，最低56.45元。今日跟随液冷板块温和反弹，成交额较上周五放量约15%，外盘大于内盘显示买盘稍强。
<strong>【技术面判断】</strong>股价连续两日反弹站上58元，但仍处于60-65元密集套牢区下方。5日均线约56.5元构成短期支撑，上方压力位60元整数关口、62元20日均线。MACD绿柱缩短但尚未金叉，KDJ低位金叉向上，短期反弹动能尚存，但60元上方压力沉重。
<strong>【资金面分析】</strong>主力资金小幅净流入约5000万，北向资金今日整体净流出但对液冷龙头配置意愿仍存。融资余额近期维持稳定，多空博弈激烈。
<strong>【操作建议】</strong>成本价104.23元，当前深度浮亏43.7%。建议：①反弹至60-62元区间减仓1/3，降低仓位至底仓水平；②若跌破55元则减仓至仅保留观察仓；③55-60元区间持有观望，不建议补仓；④真正企稳信号需站上65元且放量突破才考虑加仓。止损位52元，跌破清仓止损。
<strong>【关键点位】</strong>压力位：60元(首压)、62元(20日线)、65元(强压)；支撑位：56元(5日线)、55元(近期低点)、52元(止损位)。"""
        },
        {
            "name": "铜冠铜箔",
            "code": "301217",
            "price": "132.22",
            "change": "+7.45%",
            "up": True,
            "comment": """<strong>【当日表现】</strong>收盘132.22元，大涨7.45%，成交71.39亿，换手率6.78%，最高133.88元，最低121.40元，振幅10.28%。今日放量大阳线突破130元整数关口，主力资金净流入2.76亿元，特大单净流入1.93亿，机构主导特征明显。
<strong>【技术面判断】</strong>今日放量突破130元关键阻力位，创出近期反弹新高。5日、10日、20日均线呈多头排列，MACD红柱放大，KDJ进入超买区但强势行情中可能延续。布林带上轨开口向上，上升通道完好。下一目标位140元，强压力位148元前高附近。
<strong>【资金面分析】</strong>主力资金净流入2.76亿，特大单差2.7%，通吃率3.8%，机构买盘强劲。近5日融资净流入5.44亿，杠杆资金持续加仓。MSCI中国指数新纳入铜冠铜箔，被动资金配置需求支撑。
<strong>【操作建议】</strong>今日强势突破130元，确认反弹趋势延续。建议：①持有底仓不动，135-140元区间可考虑减仓1/4锁定利润；②若回落至125元附近可加仓1/4；③止损位上移至118元，跌破则减仓至底仓；④若放量突破140元可看高至150元。
<strong>【关键点位】</strong>压力位：135元、140元、148元(前高)；支撑位：128元、125元(5日线)、118元(止损位)。"""
        },
        {
            "name": "雅克科技",
            "code": "002409",
            "price": "159.01",
            "change": "+5.15%",
            "up": True,
            "comment": """<strong>【当日表现】</strong>收盘159.01元，涨5.15%，成交45.21亿，换手率9.11%，最高159.44元，最低149.88元，振幅6.32%。今日在HBM+存储芯片行情带动下放量上涨，主力资金净流入3.71亿元，游资净流出0.98亿，散户净流出2.72亿，典型机构吸筹格局。
<strong>【技术面判断】</strong>股价重返160元关口附近，收复前期下跌失地。5日线上穿10日线形成金叉，MACD金叉红柱放大，KDJ中高位向上。上方压力位160元(整数关口)、166元(涨停价)、180元(前期平台)。下方支撑150元、145元(20日线)。
<strong>【资金面分析】</strong>主力净流入3.71亿占总成交8.2%，机构买盘强劲。近5日融资净流入2.9亿，融资余额持续攀升。HBM前驱体材料龙头受益于存储超级周期，机构评级全为买入。
<strong>【操作建议】</strong>HBM材料龙头，存储超级周期核心受益标的。建议：①底仓30%持有不动；②若回踩150-152元区间可加仓至40%；③165-170元区间可减仓机动仓10%；④止损位140元，跌破则减仓至底仓；⑤若放量突破170元可看高至200元。
<strong>【关键点位】</strong>压力位：160元、166元、170元、200元；支撑位：152元、148元、140元(止损位)。"""
        },
        {
            "name": "*ST建艺",
            "code": "002789",
            "price": "10.22",
            "change": "+0.69%",
            "up": True,
            "comment": """<strong>【当日表现】</strong>收盘10.22元，微涨0.69%，成交1221.89万元，换手率0.77%，最高10.29元，最低10.06元。今日缩量整理，成交极度清淡，主力资金小幅净流出约80万，散户主导交易。
<strong>【技术面判断】</strong>股价在10元附近窄幅震荡，处于底部整理阶段。5日、10日、20日均线粘合，方向不明。MACD零轴下方走平，KDJ低位钝化。上方压力位10.5元、11元(前期平台)，下方支撑9.5元、9.14元(跌停价)。
<strong>【资金面与消息面】</strong>庭外重组推进中，重整投资人招募审慎评估。董事长辞职，公司治理存在不确定性。持有广东建艺矿业77%股权，矿业资产有一定价值。8月28日拟披露中报，业绩或持续亏损。
<strong>【操作建议】</strong>ST重组股，风险极高，仅适合小仓位博弈。建议：①现有仓位持有观望，控制在总仓位5%以内；②若跌破9.5元止损出局；③若放量突破11元可加仓博弈重组预期；④中报前建议谨慎，避免业绩雷；⑤10-10.5元区间高抛低吸做T降低成本。
<strong>【关键点位】</strong>压力位：10.5元、11元、11.17元(涨停价)；支撑位：10元、9.5元、9.14元(止损位)。"""
        },
    ]
)

# ========== 7. 龙虎榜深度解析 ==========
gen.add_dragon_tiger_list(
    stocks=[
        {
            "name": "通富微电",
            "code": "002156",
            "change": "+10.01%",
            "up": True,
            "institutions": 1,
            "reason": "日涨幅偏离值达7%",
            "net_buy": "+10.21亿元",
        },
        {
            "name": "兴森科技",
            "code": "002436",
            "change": "+9.99%",
            "up": True,
            "institutions": 1,
            "reason": "日涨幅偏离值达7%",
            "net_buy": "机构净买最多",
        },
        {
            "name": "太辰光",
            "code": "300570",
            "change": "+20.00%",
            "up": True,
            "institutions": 1,
            "reason": "日涨幅达15%前5只证券",
            "net_buy": "机构+北向共同净买",
        },
        {
            "name": "有研新材",
            "code": "600206",
            "change": "+10.00%",
            "up": True,
            "institutions": 0,
            "reason": "日涨幅偏离值达7%",
            "net_buy": "主力净流入11.62亿",
        },
    ]
)

# ========== 7.5 龙虎榜深度分析补充（用自定义section） ==========
lhb_analysis_html = '''
<div style="background: rgba(30,30,50,0.5); border: 1px solid rgba(255,255,255,0.08); border-radius: 16px; padding: 20px;">
    <div style="font-size: 14px; font-weight: 700; color: #f1f5f9; margin-bottom: 14px;">🐉 龙虎榜深度分析</div>
    <div style="display: flex; flex-direction: column; gap: 16px;">
        <div style="padding: 14px; background: rgba(16,185,129,0.08); border-radius: 12px; border-left: 3px solid #10b981;">
            <div style="font-weight: 600; color: #10b981; margin-bottom: 6px;">通富微电 (002156) · 净买入10.21亿</div>
            <div style="font-size: 13px; color: #94a3b8; line-height: 1.7;">
                龙虎榜净买入金额全市场第一，北向资金净买入5.39亿，机构席位同步净买入，形成"机构+北向"双认可格局。封测龙头地位稳固，先进封装高景气度持续，ABF材料国产替代+CoWoS产能紧缺双重逻辑共振。
                涨停板封单坚决，换手率9.73%量价配合良好。明日大概率高开3-5%，若高开3%以内可考虑低吸。目标价75-80元，止损位63元。
                <strong>持续性判断：强</strong>，先进封装主线核心标的，机构资金介入深，有望延续涨势。
            </div>
        </div>
        <div style="padding: 14px; background: rgba(59,130,246,0.08); border-radius: 12px; border-left: 3px solid #3b82f6;">
            <div style="font-weight: 600; color: #3b82f6; margin-bottom: 6px;">兴森科技 (002436) · 机构净买第一</div>
            <div style="font-size: 13px; color: #94a3b8; line-height: 1.7;">
                机构净买入金额最多的个股，换手率10.17%。ABF载板+IC载板核心标的，味之素削减ABF供货量直接催化国产替代预期。机构+北向资金共同净买入，资金认可度极高。
                ABF材料是先进封装关键材料，全球95%以上由日本味之素垄断，国产替代空间巨大。明日关注能否突破前高，若放量站上15元可看高至18元，止损位12.5元。
                <strong>持续性判断：较强</strong>，ABF国产替代是新催化主题，短期热度有望延续。
            </div>
        </div>
        <div style="padding: 14px; background: rgba(168,85,247,0.08); border-radius: 12px; border-left: 3px solid #a855f7;">
            <div style="font-weight: 600; color: #a855f7; margin-bottom: 6px;">太辰光 (300570) · 20cm涨停</div>
            <div style="font-size: 13px; color: #94a3b8; line-height: 1.7;">
                20cm涨停，成交45.08亿，换手率12.70%。CPO/光连接器龙头，英伟达Spectrum-X硅光交换机量产催化。机构和北向资金共同净买入。
                股价创历史新高，上方无套牢盘，空间打开。但20cm涨停后波动加大，需警惕追高风险。明日若高开5%以内可考虑低吸，目标价230-250元，止损位180元。
                <strong>持续性判断：强</strong>，CPO赛道景气度高，但短期涨幅大，建议回调后介入更安全。
            </div>
        </div>
    </div>
</div>
'''

from v3.components.layout import Section
lhb_section = Section(title="📊 龙虎榜深度解读", content=lhb_analysis_html, icon="chart")
# 插入到龙虎榜列表之后（在index为7的位置之后是evening_news）
# 简单处理：追加到最后之前

# ========== 8. 晚间重要新闻 ==========
gen.add_evening_news(
    news_list=[
        {"title": "SK海力士董事长警告：明年将出现最严重的'存储荒'", "content": "SK海力士董事长崔泰源公开表示，2027年将出现最严重的存储芯片供应短缺，存储超级周期逻辑进一步强化。三星、SK海力士、闪迪等巨头纷纷签署5年期长期协议并收取大额预付款，锁定未来供应。", "time": "20:30"},
        {"title": "闪迪投资者日上调长期财务目标", "content": "闪迪公布长期财务目标：2028-2030财年实现中高双位数营收增长，非GAAP毛利率约80%，远超市场预期。三大美国云服务商已签署8项长期协议，平均期限4年。", "time": "19:45"},
        {"title": "英伟达Spectrum-X硅光交换机全面量产", "content": "8月14日英伟达宣布全球首款200G/lane CPO以太网交换机进入全面量产，激光器数量减至传统方案1/4、功耗降至1/5，光损耗从22dB降至4dB，CPO商业化正式提速。", "time": "18:20"},
        {"title": "长江存储NAND市占率首次跻身全球前三", "content": "Counterpoint数据显示，2026年Q2长江存储NAND闪存出货量市占率达14%，首次超越铠侠跻身全球第三。三星25%、SK海力士22%、长江存储14%，国产存储突破关键里程碑。", "time": "17:30"},
        {"title": "味之素削减中国大陆ABF供货量30%", "content": "掌握全球ABF逾95%市占率的日本味之素，8月中旬通知削减中国大陆市场30%供货量。大陆ABF自给率不足5%，减供冲击高阶算力芯片封装供应链，国产替代压力骤升。", "time": "16:50"},
        {"title": "央行万亿级买断式逆回购续做", "content": "8月14日央行开展10000亿元6个月期买断式逆回购等量续做，同日首次在月中税期开展3490亿元隔夜逆回购。10年期国债收益率降至1.68%，创2025年7月以来新低，流动性充裕支撑股市。", "time": "15:00"},
    ]
)

# 插入龙虎榜深度分析section到evening news之前
# 找到合适位置插入 - 先在watch section中一并处理

# ========== 9. 重点关注标的 ==========
watch_html = '''
<div style="display: flex; flex-direction: column; gap: 16px;">
    <div style="background: rgba(30,30,50,0.5); border: 1px solid rgba(255,255,255,0.08); border-radius: 14px; padding: 18px;">
        <div style="display: flex; align-items: center; margin-bottom: 10px;">
            <span style="font-size: 16px; font-weight: 700; color: #f1f5f9;">长电科技 (600584)</span>
            <span style="margin-left: 10px; font-size: 12px; background: linear-gradient(135deg, #10b981, #059669); color: white; padding: 3px 10px; border-radius: 10px;">重点关注</span>
            <span style="margin-left: auto; font-size: 15px; font-weight: 700; color: #10b981;">+9.07%</span>
        </div>
        <div style="font-size: 13px; color: #94a3b8; line-height: 1.8;">
            <p><strong>买入逻辑：</strong>国内封测龙头，先进封装产能持续扩张，受益于CoWoS供需缺口。今日涨9.07%，成交放大至10.68%换手，主力净流入15.38亿。存储+AI芯片封装需求双驱动，业绩增长确定性高。</p>
            <p><strong>目标价：</strong>第一目标100元，第二目标115元</p>
            <p><strong>止损位：</strong>75元（跌破20日均线）</p>
            <p><strong>建议仓位：</strong>5-8%，80-82元区间可分批建仓</p>
        </div>
    </div>
    
    <div style="background: rgba(30,30,50,0.5); border: 1px solid rgba(255,255,255,0.08); border-radius: 14px; padding: 18px;">
        <div style="display: flex; align-items: center; margin-bottom: 10px;">
            <span style="font-size: 16px; font-weight: 700; color: #f1f5f9;">中微半导 (688380)</span>
            <span style="margin-left: 10px; font-size: 12px; background: linear-gradient(135deg, #f59e0b, #ef4444); color: white; padding: 3px 10px; border-radius: 10px;">强势关注</span>
            <span style="margin-left: auto; font-size: 15px; font-weight: 700; color: #10b981;">+16.81%</span>
        </div>
        <div style="font-size: 13px; color: #94a3b8; line-height: 1.8;">
            <p><strong>买入逻辑：</strong>MCU+模拟芯片设计公司，今日暴涨16.81%领涨半导体板块。存储超级周期带动周边芯片需求，公司产品矩阵丰富，切入汽车电子+工业控制等高增长赛道。量价齐升，资金关注度快速提升。</p>
            <p><strong>目标价：</strong>第一目标60元，第二目标70元</p>
            <p><strong>止损位：</strong>45元（跌破5日均线）</p>
            <p><strong>建议仓位：</strong>3-5%，回调至50元附近可低吸，追高需谨慎</p>
        </div>
    </div>
    
    <div style="background: rgba(30,30,50,0.5); border: 1px solid rgba(255,255,255,0.08); border-radius: 14px; padding: 18px;">
        <div style="display: flex; align-items: center; margin-bottom: 10px;">
            <span style="font-size: 16px; font-weight: 700; color: #f1f5f9;">普冉股份 (688766)</span>
            <span style="margin-left: 10px; font-size: 12px; background: linear-gradient(135deg, #8b5cf6, #6366f1); color: white; padding: 3px 10px; border-radius: 10px;">存储新秀</span>
            <span style="margin-left: auto; font-size: 15px; font-weight: 700; color: #10b981;">+13.38%</span>
        </div>
        <div style="font-size: 13px; color: #94a3b8; line-height: 1.8;">
            <p><strong>买入逻辑：</strong>NOR Flash龙头，存储芯片涨价周期直接受益。今日涨13.38%，换手率11.35%，主力净流入5.55亿。消费电子复苏+AI终端存储需求增长双驱动，公司NOR Flash产品向高附加值领域拓展。</p>
            <p><strong>目标价：</strong>第一目标320元，第二目标380元</p>
            <p><strong>止损位：</strong>250元（跌破10日均线）</p>
            <p><strong>建议仓位：</strong>3-5%，280-290元区间可分批建仓</p>
        </div>
    </div>
</div>
'''

watch_section = Section(title="🎯 重点关注标的", content=watch_html, icon="star")
gen._components.append(watch_section)

# 插入龙虎榜深度分析
gen._components.insert(gen._components.index(watch_section) - 1, lhb_section)

# ========== 10. 明日关键预判 ==========
gen.add_tomorrow_prediction(
    predictions=[
        {"name": "存储芯片", "direction": "看涨", "confidence": 85, "reason": "SK海力士+闪迪双重催化，长鑫科技4万亿市值打开空间，板块主力净流入231亿，资金认可度极高。预计明日延续强势，但需警惕高位股分化，龙头优先。"},
        {"name": "先进封装", "direction": "看涨", "confidence": 80, "reason": "ABF材料减供催化国产替代，通富微电10亿资金抢筹涨停，机构+北向共同买入。封测板块估值修复进行中，龙头有望连板。"},
        {"name": "CPO/光模块", "direction": "看涨", "confidence": 75, "reason": "英伟达硅光交换机量产落地，太辰光20cm涨停点燃情绪。光模块板块经历调整后再度启动，中期逻辑扎实。但短期涨幅较大，注意追高风险。"},
        {"name": "白酒/消费", "direction": "看跌", "confidence": 65, "reason": "茅台中报增收不增利打击信心，机构资金持续从消费调仓至科技。短期消费板块缺乏催化，继续跑输大盘概率大。"},
        {"name": "大盘整体", "direction": "看涨", "confidence": 70, "reason": "沪指逼近4000点关口，科创50领涨市场情绪高涨，成交放量至2.39万亿。但连续上涨后获利盘较多，明日或有震荡，4000点附近可能反复争夺。"},
    ]
)

# ========== 11. 明日操作计划 ==========
plan_text = '''
<p><strong>【大盘判断】</strong>沪指重返3982点逼近4000关口，科创50暴涨4.14%创阶段新高，两市成交2.39万亿放量普涨。中期趋势向上确认，但短期连续上涨后4000点整数关口或有震荡整固需求。明日预计高开后震荡，科技主线延续分化行情。</p>

<p><strong>【仓位建议】</strong>建议仓位70-80%，以科技成长为主线，聚焦半导体+AI算力两大方向。保留20%现金应对波动和调仓机会。</p>

<p><strong>【持仓操作计划】</strong></p>
<p><strong>1. 英维克(002837)：</strong>当前58.69元，浮亏43.7%。反弹至60-62元区间减仓1/3，将仓位降至底仓水平；55-60元持有观望，不补仓；跌破55元减仓至观察仓；止损位52元。</p>
<p><strong>2. 铜冠铜箔(301217)：</strong>当前132.22元，今日强势突破。持有底仓不动，135-140元区间减仓1/4锁定利润；回踩125元附近可加仓1/4；止损位上移至118元。</p>
<p><strong>3. 雅克科技(002409)：</strong>当前159.01元，HBM材料龙头。底仓30%持有，回踩150-152元加仓至40%；165-170元减仓机动仓10%；止损位140元。</p>
<p><strong>4. *ST建艺(002789)：</strong>当前10.22元，底部震荡。小仓位持有观望，控制在总仓位5%以内；跌破9.5元止损；放量突破11元可加仓博弈；中报前谨慎。</p>

<p><strong>【明日新开仓计划】</strong></p>
<p><strong>1. 长电科技(600584)：</strong>封测龙头，先进封装核心标的。80-82元区间建仓5%，目标价100元，止损位75元。</p>
<p><strong>2. 通富微电(002156)：</strong>龙虎榜10亿资金抢筹。若明日高开3%以内可轻仓试错3%，目标价75-80元，止损位63元；高开超5%则不追。</p>
<p><strong>3. 普冉股份(688766)：</strong>NOR Flash龙头，存储涨价受益。280-290元区间建仓3%，目标价320元，止损位250元。</p>

<p><strong>【风险控制】</strong>单只个股仓位不超过10%，单一板块不超过30%。严格执行止损纪律，破位标的果断减仓。科技股波动大，切忌追高，回调买入更安全。</p>
'''
gen.add_trading_plan(plan_text)

# ========== 12. 风险提示 ==========
gen.add_risk_warning(
    risks=[
        "科技股短期涨幅较大，获利盘丰厚，存在回调风险，尤其是高位20cm涨停个股波动加剧",
        "北向资金持续净流出，外资观望情绪浓厚，若外资加大流出可能影响市场情绪",
        "存储芯片涨价逻辑虽强，但需警惕美联储加息预期变化导致全球科技股估值承压",
        "4000点整数关口附近多空博弈激烈，沪指可能出现反复震荡",
        "ABF材料减供事件需核实真实性，若后续澄清可能导致相关概念股回调",
    ]
)

# ========== 发布 ==========
print("正在生成报告...")
html = gen.generate()
print(f"生成完成，HTML长度：{len(html)} 字符")

# 发布
result = gen.publish(
    title="盘后速递",
    report_type="aftermarket",
    filename="20260817_盘后速递.html",
    excerpt="科创50暴涨4.14%领跑，半导体全线爆发，存储芯片+先进封装双主线共振。通富微电涨停获10亿资金抢筹，长鑫科技市值破4万亿。",
    auto_deploy=True,
    docs_root="docs"
)

print(f"发布结果：{result}")
print("盘后速递生成完成！")
