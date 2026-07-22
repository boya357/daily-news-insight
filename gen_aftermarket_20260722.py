#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
2026年7月22日 盘后速递报告生成脚本
使用 V3.0 AftermarketGenerator 生成
"""
import sys
import os

sys.path.insert(0, '/root/daily-news-insight/v3')
os.chdir('/root/daily-news-insight')

from v3.generators.aftermarket import AftermarketGenerator
from components.layout import Section, HighlightBox, CardGrid, SubCard
from components.data import DataCard, Badge

# ==================== 初始化生成器 ====================
gen = AftermarketGenerator(
    date_str="20260722",
    subtitle="2026.07.22 · 盘后速递"
)

# ==================== 1. 今日核心亮点 ====================
gen.add_today_highlight(
    "市场分化加剧，沪指微涨0.07%守住3867点，深成指跌1.42%、创业板跌3.23%。"
    "高低切换极致演绎：贵金属/油气/煤炭领涨，PCB/存储芯片/机器人领跌。"
    "成交缩量至2.65万亿，较昨日萎缩3000亿。北向资金净流出约292亿，主力资金净流出196亿。"
    "雅克科技+4.4%延续反弹，铜冠铜箔-11.33%重创，英维克+0.87%窄幅震荡，*ST建艺-3.92%续创新低。"
)

# ==================== 2. 市场收盘总结 ====================
indices = [
    {"name": "上证指数", "value": "3867.03", "change": "+0.07%", "up": True, "icon": "trending_up"},
    {"name": "深证成指", "value": "14061.44", "change": "-1.42%", "up": False, "icon": "trending_down"},
    {"name": "创业板指", "value": "3566.73", "change": "-3.23%", "up": False, "icon": "trending_down"},
    {"name": "科创50", "value": "2014.10", "change": "-2.25%", "up": False, "icon": "trending_down"},
]
gen.add_market_summary(
    indices=indices,
    volume="2.65万亿（缩量3000亿）",
    northbound="净流出约292亿"
)

# ==================== 3. 情绪温度计 ====================
gen.add_sentiment_thermometer(
    temperature=35,
    volume="2.65万亿",
    up_count="1530↑",
    down_count="3876↓",
    limit_up_count=72
)

# ==================== 4. 板块涨跌幅排行 ====================
up_sectors = [
    {"name": "贵金属", "change": "+3.15%", "up": True, "leader": "山金国际/招金黄金涨停"},
    {"name": "石油石化", "change": "+2.87%", "up": True, "leader": "中曼石油两连板"},
    {"name": "煤炭采选", "change": "+2.54%", "up": True, "leader": "华电辽能/大有能源涨停"},
    {"name": "有色金属", "change": "+2.12%", "up": True, "leader": "盛达资源/兴业银锡领涨"},
    {"name": "电力板块", "change": "+1.96%", "up": True, "leader": "乐山电力/华银电力领涨"},
]

down_sectors = [
    {"name": "PCB/铜箔", "change": "-4.85%", "up": False, "leader": "铜冠铜箔-11.33%/中国巨石跌停"},
    {"name": "存储芯片", "change": "-3.97%", "up": False, "leader": "德明利跌停/佰维存储-8%"},
    {"name": "机器人", "change": "-3.72%", "up": False, "leader": "减速器/电机全线下挫"},
    {"name": "通信设备", "change": "-3.54%", "up": False, "leader": "光通信/PCB设备领跌"},
    {"name": "军工航天", "change": "-3.28%", "up": False, "leader": "商业航天板块重挫"},
]

gen.add_sector_performance(up_sectors=up_sectors, down_sectors=down_sectors)

# ==================== 5. 盘面深度解读 ====================
strong_sectors = [
    {"name": "贵金属板块", "reason": "国际金价突破4100美元/盎司创历史新高，地缘政治风险+美联储降息预期双重催化，山金国际三连板、招金黄金涨停，板块主力净流入28.98亿居全市场第一。持续性评级：B级（1-2周），取决于金价走势。"},
    {"name": "石油石化板块", "reason": "WTI原油突破85美元/桶涨3.06%，中东局势紧张加剧供应担忧，中曼石油两连板、中国海油涨超5%。防御属性+涨价逻辑共振，机构资金从科技成长转向资源价值。"},
    {"name": "电力/煤炭板块", "reason": "夏季用电高峰叠加高温天气，华电辽能四连板、华银电力四连板，煤电联动逻辑重获关注。资金从高估值科技股流向低估值公用事业，防御属性突出。"},
]

weak_sectors = [
    {"name": "PCB/铜箔板块", "reason": "昨日暴涨后获利盘集中兑现，铜冠铜箔暴跌11.33%、中国巨石跌停、南亚新材-8.94%。二季度业绩验证期来临，市场担忧涨价逻辑的可持续性，机构逢高减持。"},
    {"name": "存储芯片板块", "reason": "德明利连续跌停打开后继续下挫，佰维存储-8%、兆易创新-5%。昨日地天板反弹后今日再度走弱，说明下跌趋势未扭转，抄底资金信心不足。"},
    {"name": "机器人/军工板块", "reason": "前期热门题材全面退潮，减速器、电机、商业航天全线下挫。高位股补跌特征明显，资金从题材股全面撤出，转向防御性板块。"},
]

core_view = (
    "今日市场呈现典型的「高切低」风格切换：昨日暴涨的科技成长赛道（PCB、存储、机器人）今日集体回调，"
    "而贵金属、油气、煤炭等低估值资源防御板块逆势走强。核心原因有三：一是昨日科创50暴涨10.73%后"
    "获利盘集中兑现；二是国际金价突破4100美元、原油突破85美元，资源品涨价催化避险资金涌入；"
    "三是成交缩量3000亿至2.65万亿，增量资金未能持续进场，存量博弈下高低切换加速。"
    "操作上建议控制仓位在3-4成，防守反击为主，避免追高资源股，等待科技股缩量企稳后的二次机会。"
)

gen.add_market_deep_analysis(
    strong_sectors=strong_sectors,
    weak_sectors=weak_sectors,
    core_view=core_view
)

# ==================== 6. 持仓股深度诊断（自定义HTML，确保详细） ====================
holdings_html = """
<div style="display: flex; flex-direction: column; gap: 16px;">

    <!-- 英维克 -->
    <div style="background: rgba(30,30,50,0.6); border: 1px solid rgba(255,255,255,0.08); border-radius: 16px; padding: 20px 22px;">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px;">
            <div>
                <span style="font-size: 17px; font-weight: 700; color: #f1f5f9;">英维克</span>
                <span style="font-size: 13px; color: #9ca3af; margin-left: 8px;">002837 · 液冷散热龙头</span>
            </div>
            <div style="text-align: right;">
                <div style="font-size: 20px; font-weight: 700; color: #10b981;">60.51元</div>
                <div style="font-size: 14px; font-weight: 600; color: #10b981;">+0.52 (+0.87%)</div>
            </div>
        </div>
        <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 10px; margin-bottom: 14px; padding-bottom: 14px; border-bottom: 1px solid rgba(255,255,255,0.06);">
            <div><div style="font-size: 11px; color: #94a3b8;">成交额</div><div style="font-size: 14px; font-weight: 600; color: #e2e8f0;">37.76亿</div></div>
            <div><div style="font-size: 11px; color: #94a3b8;">换手率</div><div style="font-size: 14px; font-weight: 600; color: #e2e8f0;">5.42%</div></div>
            <div><div style="font-size: 11px; color: #94a3b8;">振幅</div><div style="font-size: 14px; font-weight: 600; color: #e2e8f0;">9.25%</div></div>
            <div><div style="font-size: 11px; color: #94a3b8;">主力净流入</div><div style="font-size: 14px; font-weight: 600; color: #10b981;">+0.41亿</div></div>
        </div>
        <div style="font-size: 13.5px; color: #cbd5e1; line-height: 1.8;">
            <p style="margin: 0 0 10px 0;"><strong style="color: #f59e0b;">📊 今日表现：</strong>英维克今日平开低走后探底回升，最低58.69元、最高64.24元，振幅9.25%，收盘60.51元微涨0.87%。成交额37.76亿较昨日55亿缩量，换手率5.42%。主力资金小幅净流入0.41亿，特大单+大单整体流入，显示有资金在低位承接。液冷板块今日整体偏弱，英维克相对抗跌。</p>
            <p style="margin: 0 0 10px 0;"><strong style="color: #f59e0b;">📈 技术面判断：</strong>股价仍处于下降通道，今日冲高64.24元后回落，确认65元附近压力明显。5日均线约59.5元形成短期支撑，10日均线65元为强压力位。MACD绿柱缩短，KDJ低位金叉，短期有超跌反弹需求，但中期下降趋势未改。70元下方均定义为弱势反弹区域，反弹量能不足是最大隐患。</p>
            <p style="margin: 0 0 10px 0;"><strong style="color: #f59e0b;">💰 资金面：</strong>主力净流入0.41亿（特大单+2.73亿，大单-2.51亿），呈现分歧状态。近5日主力累计净流出仍超10亿，中期流出趋势未改。液冷板块整体调整，行业β压制个股表现。北向资金今日净流出292亿，对科技成长股形成压制。</p>
            <p style="margin: 0 0 10px 0;"><strong style="color: #f59e0b;">📋 基本面：</strong>公司是国内液冷散热龙头，数据中心/智算中心温控解决方案提供商。AI算力浪潮下液冷需求爆发，公司在手订单充足。但短期估值偏高（PE TTM约160倍），需要业绩持续高增长来消化估值。中报业绩预计8月中下旬披露，是重要催化节点。</p>
            <p style="margin: 0;"><strong style="color: #ef4444;">🎯 操作建议：</strong>
                <br>• <strong>减仓位：</strong>反弹至 <strong>63-65元</strong> 区间减仓1/2
                <br>• <strong>清仓位：</strong>跌破 <strong>58元</strong> 无条件清仓止损
                <br>• <strong>观察位：</strong>若放量突破65元可持有观察，但70元以下不加仓
                <br>• <strong>核心逻辑：</strong>液冷赛道长期逻辑不变，但短期超跌反弹性质，反弹减仓为主
            </p>
        </div>
    </div>

    <!-- 铜冠铜箔 -->
    <div style="background: rgba(30,30,50,0.6); border: 1px solid rgba(255,255,255,0.08); border-radius: 16px; padding: 20px 22px;">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px;">
            <div>
                <span style="font-size: 17px; font-weight: 700; color: #f1f5f9;">铜冠铜箔</span>
                <span style="font-size: 13px; color: #9ca3af; margin-left: 8px;">301217 · HVLP铜箔龙头</span>
            </div>
            <div style="text-align: right;">
                <div style="font-size: 20px; font-weight: 700; color: #ef4444;">95.36元</div>
                <div style="font-size: 14px; font-weight: 600; color: #ef4444;">-12.18 (-11.33%)</div>
            </div>
        </div>
        <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 10px; margin-bottom: 14px; padding-bottom: 14px; border-bottom: 1px solid rgba(255,255,255,0.06);">
            <div><div style="font-size: 11px; color: #94a3b8;">成交额</div><div style="font-size: 14px; font-weight: 600; color: #e2e8f0;">61.80亿</div></div>
            <div><div style="font-size: 11px; color: #94a3b8;">换手率</div><div style="font-size: 14px; font-weight: 600; color: #e2e8f0;">7.52%</div></div>
            <div><div style="font-size: 11px; color: #94a3b8;">振幅</div><div style="font-size: 14px; font-weight: 600; color: #e2e8f0;">10.06%</div></div>
            <div><div style="font-size: 11px; color: #94a3b8;">主力净流出</div><div style="font-size: 14px; font-weight: 600; color: #ef4444;">-3.82亿</div></div>
        </div>
        <div style="font-size: 13.5px; color: #cbd5e1; line-height: 1.8;">
            <p style="margin: 0 0 10px 0;"><strong style="color: #f59e0b;">📊 今日表现：</strong>铜冠铜箔今日大幅低开100元（-7%）后震荡走低，最低探至94元，收盘95.36元暴跌11.33%，创调整以来新低。成交额61.8亿放量，换手率7.52%。主力资金净流出3.82亿，特大单+大单净卖出超5亿，机构加速出货特征明显。PET铜箔概念板块今日净流出16.13亿，铜冠铜箔净流出2.9亿居板块第二。</p>
            <p style="margin: 0 0 10px 0;"><strong style="color: #f59e0b;">📈 技术面判断：</strong>今日放量大阴线跌破100元整数关口，一阴破多线，技术形态极度恶化。从高点129元下跌至95元，短短3个交易日累计跌幅达26%，属于断崖式下跌。5日/10日/20日均线全部空头排列，下方支撑需看85-90元区间（前期平台）。MACD死叉向下发散，KDJ超卖区域但未见底背离信号。短期严重超卖可能有技术性反弹，但反弹高度有限。</p>
            <p style="margin: 0 0 10px 0;"><strong style="color: #f59e0b;">💰 资金面：</strong>主力净流出3.82亿（特大单差-5%，大单差-3.1%），BBD-3.09亿。近5日融资净流出2.83亿，融资余额持续下降。机构集中兑现离场，散户接盘（小单差+8.1%），典型的机构出货形态。中报业绩虽然大增486%-544%，但二季度环比下滑约7%戳破高增长预期，"利好出尽"剧本正在上演。</p>
            <p style="margin: 0 0 10px 0;"><strong style="color: #f59e0b;">📋 基本面：</strong>公司是国内HVLP铜箔龙头，AI服务器/PCB高端铜箔需求爆发。中报预告净利润同比增486%-544%，但二季度环比下滑约7%引发市场对业绩持续性的担忧。当前PE TTM约186倍，估值仍偏高，需要持续高增长消化。</p>
            <p style="margin: 0;"><strong style="color: #ef4444;">🎯 操作建议：</strong>
                <br>• <strong>止盈位：</strong>反弹至 <strong>100-105元</strong> 区间减仓至底仓（剩余1/4）
                <br>• <strong>清仓位：</strong>跌破 <strong>90元</strong> 止盈全部离场，保住剩余利润
                <br>• <strong>补仓位：</strong>85元以下可考虑小仓位博反弹，但需严格止损
                <br>• <strong>核心逻辑：</strong>存储铜箔长期需求逻辑仍在，但短期估值过高+机构出货+板块系统性调整，先落袋为安
            </p>
        </div>
    </div>

    <!-- 雅克科技 -->
    <div style="background: rgba(30,30,50,0.6); border: 1px solid rgba(255,255,255,0.08); border-radius: 16px; padding: 20px 22px;">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px;">
            <div>
                <span style="font-size: 17px; font-weight: 700; color: #f1f5f9;">雅克科技</span>
                <span style="font-size: 13px; color: #9ca3af; margin-left: 8px;">002409 · HBM前驱体龙头</span>
            </div>
            <div style="text-align: right;">
                <div style="font-size: 20px; font-weight: 700; color: #10b981;">149.86元</div>
                <div style="font-size: 14px; font-weight: 600; color: #10b981;">+6.31 (+4.40%)</div>
            </div>
        </div>
        <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 10px; margin-bottom: 14px; padding-bottom: 14px; border-bottom: 1px solid rgba(255,255,255,0.06);">
            <div><div style="font-size: 11px; color: #94a3b8;">成交额</div><div style="font-size: 14px; font-weight: 600; color: #e2e8f0;">74.92亿</div></div>
            <div><div style="font-size: 11px; color: #94a3b8;">换手率</div><div style="font-size: 14px; font-weight: 600; color: #e2e8f0;">15.45%</div></div>
            <div><div style="font-size: 11px; color: #94a3b8;">振幅</div><div style="font-size: 14px; font-weight: 600; color: #e2e8f0;">8.02%</div></div>
            <div><div style="font-size: 11px; color: #94a3b8;">主力净流入</div><div style="font-size: 14px; font-weight: 600; color: #10b981;">+3.84亿</div></div>
        </div>
        <div style="font-size: 13.5px; color: #cbd5e1; line-height: 1.8;">
            <p style="margin: 0 0 10px 0;"><strong style="color: #f59e0b;">📊 今日表现：</strong>雅克科技今日高开146.42元后冲高至157.91元（涨停价），午后受大盘拖累回落，收盘149.86元涨4.40%。成交额74.92亿放量，换手率15.45%。主力净流入3.84亿，特大单持续买入显示机构资金仍在布局。盘中一度冲板但未能封住，反映上方抛压较重。昨日龙虎榜显示机构净卖出1.33亿、北向净买入8553万，多空博弈激烈。</p>
            <p style="margin: 0 0 10px 0;"><strong style="color: #f59e0b;">📈 技术面判断：</strong>股价在140-160元区间震荡整理，5日均线上穿10日均线形成短期金叉，140元附近支撑较强。从7月高点246元回落至130元后反弹，目前处于第一波反弹后的震荡阶段。MACD绿柱持续缩短，KDJ金叉向上至60附近，反弹动能仍在但需突破160元压力才能打开上行空间。150元为短期多空分水岭。</p>
            <p style="margin: 0 0 10px 0;"><strong style="color: #f59e0b;">💰 资金面：</strong>主力净流入3.84亿（特大单买入积极），游资净流出4123万，散户净流出3.43亿。融资余额24.25亿，昨日融资净偿还2.26亿，杠杆资金在减仓。北向资金昨日净买入8553万，外资继续加仓。综合来看，机构与外资是主要买盘，游资和散户在逢高减仓。HBM需求爆发逻辑未变，台积电计划2027年上调代工价格进一步催化。</p>
            <p style="margin: 0 0 10px 0;"><strong style="color: #f59e0b;">📋 基本面：</strong>公司是国内半导体前驱体材料龙头，HBM相关材料营收约21亿元，深度绑定SK海力士、三星、美光三大存储巨头。2025年营收68.16亿增42.36%，归母净利10.42亿增83.74%。当前PE TTM约71倍，在半导体材料板块中估值相对合理。HBM需求爆发+国产替代双逻辑支撑中长期成长。</p>
            <p style="margin: 0;"><strong style="color: #10b981;">🎯 操作建议：</strong>
                <br>• <strong>减仓位：</strong>155-160元 减仓1/3锁定利润
                <br>• <strong>持有位：</strong>站稳 <strong>160元</strong> 可持半仓继续观察，目标看180元
                <br>• <strong>止盈位：</strong>跌破 <strong>140元</strong> 止盈离场，保住反弹利润
                <br>• <strong>加仓位：</strong>140-145元区间可小仓位加仓，跌破135止损
                <br>• <strong>核心逻辑：</strong>HBM前驱体龙头地位稳固，全球三大存储巨头均为客户，中期成长确定性高，但短期震荡整理需耐心
            </p>
        </div>
    </div>

    <!-- *ST建艺 -->
    <div style="background: rgba(30,30,50,0.6); border: 1px solid rgba(239,68,68,0.2); border-radius: 16px; padding: 20px 22px;">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px;">
            <div>
                <span style="font-size: 17px; font-weight: 700; color: #f1f5f9;">*ST建艺</span>
                <span style="font-size: 13px; color: #ef4444; margin-left: 8px;">002789 · 退市风险警示</span>
            </div>
            <div style="text-align: right;">
                <div style="font-size: 20px; font-weight: 700; color: #ef4444;">8.08元</div>
                <div style="font-size: 14px; font-weight: 600; color: #ef4444;">-0.33 (-3.92%)</div>
            </div>
        </div>
        <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 10px; margin-bottom: 14px; padding-bottom: 14px; border-bottom: 1px solid rgba(255,255,255,0.06);">
            <div><div style="font-size: 11px; color: #94a3b8;">成交额</div><div style="font-size: 14px; font-weight: 600; color: #e2e8f0;">2603万</div></div>
            <div><div style="font-size: 11px; color: #94a3b8;">换手率</div><div style="font-size: 14px; font-weight: 600; color: #e2e8f0;">2.02%</div></div>
            <div><div style="font-size: 11px; color: #94a3b8;">振幅</div><div style="font-size: 14px; font-weight: 600; color: #e2e8f0;">7.85%</div></div>
            <div><div style="font-size: 11px; color: #94a3b8;">主力净流出</div><div style="font-size: 14px; font-weight: 600; color: #ef4444;">-223万</div></div>
        </div>
        <div style="font-size: 13.5px; color: #cbd5e1; line-height: 1.8;">
            <p style="margin: 0 0 10px 0;"><strong style="color: #f59e0b;">📊 今日表现：</strong>*ST建艺今日低开低走，最低探至7.97元续创新低，收盘8.08元跌3.92%。成交额仅2603万，换手率2.02%，流动性濒临枯竭。主力资金净流出223万，游资净流入126万，散户净流入97万，基本是散户在交易。装修装饰板块今日跌2%，板块拖累+自身退市风险双重压制。</p>
            <p style="margin: 0 0 10px 0;"><strong style="color: #f59e0b;">📈 技术面判断：</strong>股价持续阴跌创历史新低，完全没有止跌信号。5日/10日/20日均线全部空头排列，下降斜率陡峭。成交量极度萎缩，地量见地价但在退市风险股中不适用。从13.45元成本到8.08元，浮亏已达-39.9%，且看不到底部。</p>
            <p style="margin: 0 0 10px 0;"><strong style="color: #f59e0b;">⚠️ 基本面风险：</strong>一季度亏损5311万，中报预亏1.1-1.6亿，负债率高达94.38%，毛利率仅2.55%。虽然2025年末净资产转正并申请摘帽，但目前仍在*ST状态，退市风险未完全解除。珠海正方集团入主后虽有债务豁免和资产注入预期，但业绩改善需要时间，短期股价缺乏支撑。</p>
            <p style="margin: 0 0 10px 0;"><strong style="color: #f59e0b;">📋 持仓心态：</strong>这只票已经严重拖累组合表现，浮亏近40%且仍在恶化。退市风险股的特点是下跌没有底，越拖越亏。虽然珠海正方国资背景提供了一定安全垫，但时间成本和机会成本太高。长痛不如短痛，坚决执行纪律。</p>
            <p style="margin: 0;"><strong style="color: #ef4444;">🎯 操作建议：</strong>
                <br>• <strong>最高优先级：</strong>任何价格立即清仓止损，关闭退市风险敞口
                <br>• <strong>反弹减仓：</strong>若有反弹至8.5-9元，必须坚决离场
                <br>• <strong>绝不加仓：</strong>退市风险股严禁补仓摊低成本，越补越亏
                <br>• <strong>核心逻辑：</strong>退市风险+业绩亏损+流动性枯竭，时间成本和机会成本太高，早割早解脱
            </p>
        </div>
    </div>

</div>
"""

from components.layout import Section
holdings_section = Section(title="💼 持仓股深度诊断", content=holdings_html, icon="briefcase")
gen._components.append(holdings_section)

# ==================== 7. 龙虎榜深度解读 ====================
dragon_html = """
<div style="display: flex; flex-direction: column; gap: 14px;">

    <!-- 山金国际 -->
    <div style="background: rgba(30,30,50,0.6); border: 1px solid rgba(255,255,255,0.08); border-radius: 16px; padding: 18px 20px;">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 10px;">
            <div>
                <span style="font-size: 16px; font-weight: 700; color: #f1f5f9;">山金国际</span>
                <span style="font-size: 12px; color: #9ca3af; margin-left: 6px;">000975</span>
                <span style="font-size: 11px; background: linear-gradient(135deg, #f59e0b, #d97706); color: white; padding: 2px 8px; border-radius: 10px; margin-left: 8px;">三连板</span>
            </div>
            <span style="font-size: 18px; font-weight: 700; color: #10b981;">+10.01% · 22.52元</span>
        </div>
        <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; margin-bottom: 12px; font-size: 12px;">
            <div><div style="color: #94a3b8;">成交额</div><div style="color: #e2e8f0; font-weight: 600;">20.73亿</div></div>
            <div><div style="color: #94a3b8;">换手率</div><div style="color: #e2e8f0; font-weight: 600;">3.71%</div></div>
            <div><div style="color: #94a3b8;">龙虎榜净买</div><div style="color: #10b981; font-weight: 600;">+8550万</div></div>
        </div>
        <div style="font-size: 13px; color: #cbd5e1; line-height: 1.7;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #f59e0b;">席位分析：</strong>买一国泰海通成都北一环路（成都系）买入1.02亿，买四长江证券上海天钥桥路（炒股养家）买入5785万，买五华鑫上海宛平南路买入5204万。两大顶级游资联手做多，成都系+炒股养家合计买入超1.6亿。</p>
            <p style="margin: 0 0 6px 0;"><strong style="color: #f59e0b;">机构动向：</strong>5家机构席位现身，合计买入1.34亿、卖出2.06亿，机构净卖出7118万。深股通净卖出5374万。游资在买、机构和外资在卖，分歧明显。机构借涨停出货，游资接力炒作。</p>
            <p style="margin: 0 0 6px 0;"><strong style="color: #f59e0b;">题材逻辑：</strong>国际金价突破4100美元/盎司创历史新高，黄金股迎来业绩+估值双升。美联储降息预期升温+中东地缘风险+美元走弱三重催化，黄金中长期上涨趋势确立。山金国际作为黄金股龙头，资源储量大、业绩弹性高。</p>
            <p style="margin: 0;"><strong style="color: #f59e0b;">持续性判断：</strong>⭐⭐⭐ 中等偏强。金价突破4100美元是核心催化，游资合力封板，但机构和北向趁涨停出货，说明机构对持续性存疑。明日若高开过多需谨慎追高，关注23元压力位能否放量突破。回调至20-21元可关注。</p>
        </div>
    </div>

    <!-- 星网锐捷 -->
    <div style="background: rgba(30,30,50,0.6); border: 1px solid rgba(255,255,255,0.08); border-radius: 16px; padding: 18px 20px;">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 10px;">
            <div>
                <span style="font-size: 16px; font-weight: 700; color: #f1f5f9;">星网锐捷</span>
                <span style="font-size: 12px; color: #9ca3af; margin-left: 6px;">002396</span>
                <span style="font-size: 11px; background: linear-gradient(135deg, #8b5cf6, #6d28d9); color: white; padding: 2px 8px; border-radius: 10px; margin-left: 8px;">机构净买6亿</span>
            </div>
            <span style="font-size: 18px; font-weight: 700; color: #10b981;">+9.43% · 34.59元</span>
        </div>
        <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; margin-bottom: 12px; font-size: 12px;">
            <div><div style="color: #94a3b8;">成交额</div><div style="color: #e2e8f0; font-weight: 600;">73.5亿</div></div>
            <div><div style="color: #94a3b8;">换手率</div><div style="color: #e2e8f0; font-weight: 600;">3.5%</div></div>
            <div><div style="color: #94a3b8;">机构净买</div><div style="color: #10b981; font-weight: 600;">+6.00亿</div></div>
        </div>
        <div style="font-size: 13px; color: #cbd5e1; line-height: 1.7;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #f59e0b;">席位分析：</strong>4家机构专用席位合计净买入6亿元，占总成交额的8.16%，为今日机构净买额第一名。卖五席位中"小棉袄"卖出8391万（昨日介入，今日止盈），属于游资获利了结。机构大额买入，游资出货。</p>
            <p style="margin: 0 0 6px 0;"><strong style="color: #f59e0b;">机构动向：</strong>机构大幅抢筹，净买入6亿为今日全市场最高。说明机构看好网络设备/算力基础设施的长期逻辑，腾讯云大规模部署国产化算力是重要催化。AI算力需求从GPU向网络设备、交换机、NPO等方向扩散。</p>
            <p style="margin: 0 0 6px 0;"><strong style="color: #f59e0b;">题材逻辑：</strong>网络设备+云计算+信创概念，公司是国内企业级网络设备龙头，交换机、路由器市场份额领先。AI算力建设带动高端交换机需求爆发，公司受益于AI算力基础设施建设浪潮。腾讯云Q4部署NPO超级节点进一步催化。</p>
            <p style="margin: 0;"><strong style="color: #f59e0b;">持续性判断：</strong>⭐⭐⭐⭐ 较强。机构大额买入往往意味着中期行情，而非游资一日游。但今日近涨停位置机构接盘，短期可能震荡消化，36元附近有压力，回调至32-33元可关注。</p>
        </div>
    </div>

    <!-- 红板科技 -->
    <div style="background: rgba(30,30,50,0.6); border: 1px solid rgba(255,255,255,0.08); border-radius: 16px; padding: 18px 20px;">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 10px;">
            <div>
                <span style="font-size: 16px; font-weight: 700; color: #f1f5f9;">红板科技</span>
                <span style="font-size: 12px; color: #9ca3af; margin-left: 6px;">001322</span>
                <span style="font-size: 11px; background: linear-gradient(135deg, #06b6d4, #0891b2); color: white; padding: 2px 8px; border-radius: 10px; margin-left: 8px;">PCB+存储</span>
            </div>
            <span style="font-size: 18px; font-weight: 700; color: #10b981;">+8.86% · 83.82元</span>
        </div>
        <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; margin-bottom: 12px; font-size: 12px;">
            <div><div style="color: #94a3b8;">龙虎榜净买</div><div style="color: #10b981; font-weight: 600;">+3.51亿</div></div>
            <div><div style="color: #94a3b8;">机构净买</div><div style="color: #10b981; font-weight: 600;">+2.69亿</div></div>
            <div><div style="color: #94a3b8;">净买占比</div><div style="color: #10b981; font-weight: 600;">11.71%</div></div>
        </div>
        <div style="font-size: 13px; color: #cbd5e1; line-height: 1.7;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #f59e0b;">席位分析：</strong>华泰总部买入6842万，机构专用席位净买入2.69亿，合计净买入3.51亿。净买占比高达11.71%，资金介入程度深。存储+PCB双题材叠加，是科技股中相对低位的标的。</p>
            <p style="margin: 0 0 6px 0;"><strong style="color: #f59e0b;">机构动向：</strong>机构净买入2.69亿排名全市场第二，说明机构对存储产业链上游PCB材料的看好。在存储芯片整体调整的背景下，PCB方向获得机构逆势布局，可能是认为PCB板块调整更充分、估值更合理。</p>
            <p style="margin: 0 0 6px 0;"><strong style="color: #f59e0b;">题材逻辑：</strong>次新股+PCB+存储芯片概念，公司专业从事印制电路板的研发、生产和销售，产品广泛应用于消费电子、通信、工业控制等领域。存储芯片需求复苏带动上游PCB订单增长，次新股流通盘小弹性大。</p>
            <p style="margin: 0;"><strong style="color: #f59e0b;">持续性判断：</strong>⭐⭐⭐ 中等。机构买入提供中期支撑，但整个PCB板块今日大跌，红板科技属于相对抗跌的个股。明日若板块继续调整，可能会有补跌风险。关注75-78元支撑位，跌破则短期走弱。</p>
        </div>
    </div>

    <!-- 托伦斯 -->
    <div style="background: rgba(30,30,50,0.6); border: 1px solid rgba(255,255,255,0.08); border-radius: 16px; padding: 18px 20px;">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 10px;">
            <div>
                <span style="font-size: 16px; font-weight: 700; color: #f1f5f9;">托伦斯</span>
                <span style="font-size: 12px; color: #9ca3af; margin-left: 6px;">688629</span>
                <span style="font-size: 11px; background: linear-gradient(135deg, #ec4899, #be185d); color: white; padding: 2px 8px; border-radius: 10px; margin-left: 8px;">20CM两连板</span>
            </div>
            <span style="font-size: 18px; font-weight: 700; color: #10b981;">+20.00% · 158.71元</span>
        </div>
        <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; margin-bottom: 12px; font-size: 12px;">
            <div><div style="color: #94a3b8;">龙虎榜净买</div><div style="color: #10b981; font-weight: 600;">+1.93亿</div></div>
            <div><div style="color: #94a3b8;">半导体设备</div><div style="color: #e2e8f0; font-weight: 600;">国产替代</div></div>
            <div><div style="color: #94a3b8;">游资席位</div><div style="color: #e2e8f0; font-weight: 600;">溧阳路+苏南帮</div></div>
        </div>
        <div style="font-size: 13px; color: #cbd5e1; line-height: 1.7;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #f59e0b;">席位分析：</strong>上海溧阳路买入8457万，苏南帮买入5821万，两大游资联手封板。拉萨天团也出现在榜单中，散户跟风明显。两连板后筹码交换加剧，短期涨幅已大。</p>
            <p style="margin: 0 0 6px 0;"><strong style="color: #f59e0b;">题材逻辑：</strong>半导体精密零部件+设备国产替代概念，是科技股中少数能连板的标的。在存储芯片整体调整的背景下，半导体设备方向展现相对强度。设备国产替代是中长期确定性最高的赛道之一。</p>
            <p style="margin: 0 0 6px 0;"><strong style="color: #f59e0b;">资金性质：</strong>纯游资推动，机构参与度低。两连板后短期获利盘丰厚，一旦市场情绪转弱，可能出现大幅回调。科创板个股波动大，20CM涨跌幅风险收益比不对称。</p>
            <p style="margin: 0;"><strong style="color: #f59e0b;">持续性判断：</strong>⭐⭐ 偏弱。两连板后短期涨幅已大，且主要是游资推动，机构参与度低。明日冲高后回落概率大，不建议追高。关注160元压力位，若不能放量突破则短期见顶风险大。</p>
        </div>
    </div>

</div>
"""

dragon_section = Section(title="🐉 龙虎榜深度解读", content=dragon_html, icon="award")
gen._components.append(dragon_section)

# ==================== 8. 重点关注标的 ====================
watch_html = """
<div style="display: flex; flex-direction: column; gap: 14px;">

    <!-- 1. 锐捷网络 -->
    <div style="background: linear-gradient(135deg, rgba(59,130,246,0.1) 0%, rgba(139,92,246,0.08) 100%); border: 1px solid rgba(59,130,246,0.2); border-radius: 16px; padding: 18px 20px;">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 10px;">
            <div>
                <span style="font-size: 16px; font-weight: 700; color: #f1f5f9;">锐捷网络</span>
                <span style="font-size: 12px; color: #9ca3af; margin-left: 6px;">301165</span>
                <span style="font-size: 11px; background: linear-gradient(135deg, #10b981, #059669); color: white; padding: 2px 8px; border-radius: 10px; margin-left: 8px;">买入评级</span>
            </div>
            <span style="font-size: 14px; color: #10b981;">今日 +20%（20CM涨停）</span>
        </div>
        <div style="font-size: 13px; color: #cbd5e1; line-height: 1.7;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #f59e0b;">📌 买入逻辑：</strong>① 网络设备+算力基础设施龙头，腾讯云大规模部署国产化算力直接受益；② 深股通净买入1.13亿，4家机构合计净买入1.8亿，机构+外资联手抢筹；③ 交换机/NPO赛道景气度高，AI算力需求持续增长驱动产品量价齐升；④ 相对高位的光模块/PCB，网络设备估值更具吸引力。</p>
            <p style="margin: 0 0 6px 0;"><strong style="color: #10b981;">🎯 目标价：</strong>短期目标 <strong>175-185元</strong>（+15%~20%），中期看200元以上</p>
            <p style="margin: 0;"><strong style="color: #ef4444;">🛑 止损位：</strong>跌破 <strong>140元</strong> 止损（约-10%）</p>
        </div>
    </div>

    <!-- 2. 招金黄金 -->
    <div style="background: linear-gradient(135deg, rgba(245,158,11,0.1) 0%, rgba(217,119,6,0.08) 100%); border: 1px solid rgba(245,158,11,0.2); border-radius: 16px; padding: 18px 20px;">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 10px;">
            <div>
                <span style="font-size: 16px; font-weight: 700; color: #f1f5f9;">招金黄金</span>
                <span style="font-size: 12px; color: #9ca3af; margin-left: 6px;">600489</span>
                <span style="font-size: 11px; background: linear-gradient(135deg, #f59e0b, #d97706); color: white; padding: 2px 8px; border-radius: 10px; margin-left: 8px;">关注评级</span>
            </div>
            <span style="font-size: 14px; color: #10b981;">今日 +9.97%</span>
        </div>
        <div style="font-size: 13px; color: #cbd5e1; line-height: 1.7;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #f59e0b;">📌 关注逻辑：</strong>① 国际金价突破4100美元/盎司创历史新高，黄金股业绩弹性最大；② 美联储降息预期升温+地缘政治风险双重催化，金价中长期上涨趋势明确；③ 章盟主买入1784万，游资开始关注黄金板块；④ 招金黄金是国内四大黄金集团之一，资源储量丰富，业绩弹性高于山金国际。</p>
            <p style="margin: 0 0 6px 0;"><strong style="color: #10b981;">🎯 目标价：</strong>短期目标 <strong>15-16元</strong>（+15%~23%）</p>
            <p style="margin: 0;"><strong style="color: #ef4444;">🛑 止损位：</strong>跌破 <strong>11.5元</strong> 止损（约-12%）</p>
        </div>
    </div>

    <!-- 3. 德明利 -->
    <div style="background: linear-gradient(135deg, rgba(239,68,68,0.1) 0%, rgba(220,38,38,0.08) 100%); border: 1px solid rgba(239,68,68,0.2); border-radius: 16px; padding: 18px 20px;">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 10px;">
            <div>
                <span style="font-size: 16px; font-weight: 700; color: #f1f5f9;">德明利</span>
                <span style="font-size: 12px; color: #9ca3af; margin-left: 6px;">001309</span>
                <span style="font-size: 11px; background: linear-gradient(135deg, #ef4444, #dc2626); color: white; padding: 2px 8px; border-radius: 10px; margin-left: 8px;">风险观察</span>
            </div>
            <span style="font-size: 14px; color: #ef4444;">今日跌停</span>
        </div>
        <div style="font-size: 13px; color: #cbd5e1; line-height: 1.7;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #f59e0b;">📌 关注逻辑（超跌反弹博弈）：</strong>① 存储芯片板块龙头之一，连续跌停后估值大幅压缩，二季度业绩环比下滑已被市场消化；② 屠文斌买入9201万逆势抄底，与炒新一族卖出9898万形成对手盘，多空博弈激烈；③ 若存储板块企稳，德明利作为人气龙头反弹力度可能最大；④ 但风险也极大，属于高风险高收益的博弈标的。</p>
            <p style="margin: 0 0 6px 0;"><strong style="color: #10b981;">🎯 目标价：</strong>超跌反弹目标 <strong>500-550元</strong>（+20%~30%）</p>
            <p style="margin: 0;"><strong style="color: #ef4444;">🛑 止损位：</strong>跌破 <strong>380元</strong> 止损（约-8%），若继续跌停则放弃</p>
            <p style="margin: 8px 0 0 0; color: #f59e0b; font-size: 12px;">⚠️ 高风险标的，仅适合小仓位博弈，严格止损</p>
        </div>
    </div>

</div>
"""

watch_section = Section(title="🎯 重点关注标的", content=watch_html, icon="star")
gen._components.append(watch_section)

# ==================== 9. 明日关键预判 ====================
predictions = [
    {
        "name": "大盘走势",
        "direction": "震荡",
        "confidence": 65,
        "reason": "沪指3867点附近多空博弈，权重托底但成长股承压。明日大概率延续震荡格局，上证3830-3900点区间震荡。成交若继续缩量至2.5万亿以下，需警惕二次探底风险。关注3830点支撑能否守住。创业板指跌3.23%后有技术性反弹需求，但力度可能有限。"
    },
    {
        "name": "贵金属板块",
        "direction": "看涨",
        "confidence": 70,
        "reason": "国际金价突破4100美元创历史新高，美联储降息预期+地缘政治风险双重支撑。游资已开始布局（成都系+炒股养家买入山金国际），板块短期有望延续强势。但连续上涨后需警惕获利回吐，低吸为主不追高。黄金中长期上涨趋势确立，回调即是机会。"
    },
    {
        "name": "半导体/存储",
        "direction": "震荡",
        "confidence": 55,
        "reason": "昨日暴涨后今日大幅回调，属于正常的获利回吐。存储芯片中期逻辑未变（HBM需求爆发+涨价周期），但短期估值过高+机构出货需要时间消化。预计在当前位置震荡整固1-2周，关注德明利/佰维存储能否止跌。雅克科技作为HBM材料龙头相对抗跌。"
    },
    {
        "name": "电力/煤炭",
        "direction": "看涨",
        "confidence": 60,
        "reason": "夏季用电高峰+高温天气催化，华电辽能四连板、华银电力四连板打出高度。低估值+高股息+防御属性，在市场风格切换中持续受益。关注二三线电力股的补涨机会。但需注意煤价上涨可能侵蚀火电企业利润。"
    },
]

gen.add_tomorrow_prediction(predictions)

# ==================== 10. 明日操作计划 ====================
trading_plan = """
<div style="font-size: 14px; line-height: 1.9; color: #e2e8f0;">
    <h4 style="color: #f59e0b; margin: 0 0 12px 0; font-size: 15px;">📊 大盘判断</h4>
    <p style="margin: 0 0 14px 0;">明日大盘预计维持震荡格局，上证指数3830-3900点区间运行。成交继续缩量的可能性较大，市场情绪从昨日的极度贪婪回落至偏谨慎。操作上以防守反击为主，控制仓位3-4成，不追高、不抄底，等待明确信号。创业板指今日大跌3.23%后明日或有技术性反弹，但需观察量能配合。</p>

    <h4 style="color: #f59e0b; margin: 0 0 12px 0; font-size: 15px;">💼 持仓操作计划（具体到价位）</h4>
    <p style="margin: 0 0 10px 0;"><strong style="color: #ef4444;">① 英维克（002837）：</strong>
        <br>• 反弹至 <strong>63-65元</strong> 减仓1/2
        <br>• 跌破 <strong>58元</strong> 无条件清仓止损
        <br>• 65元以下均为弱势反弹区域，不加仓
    </p>
    <p style="margin: 0 0 10px 0;"><strong style="color: #ef4444;">② 铜冠铜箔（301217）：</strong>
        <br>• 反弹至 <strong>100-105元</strong> 减仓至底仓（1/4）
        <br>• 跌破 <strong>90元</strong> 止盈全部离场
        <br>• 短期趋势已走坏，保住剩余利润为首要任务
    </p>
    <p style="margin: 0 0 10px 0;"><strong style="color: #10b981;">③ 雅克科技（002409）：</strong>
        <br>• 155-160元 减仓1/3锁定利润
        <br>• 站稳 <strong>160元</strong> 可持半仓继续观察，目标看180元
        <br>• 跌破 <strong>140元</strong> 止盈离场
        <br>• 140-145元区间可小仓位加仓，跌破135止损
    </p>
    <p style="margin: 0 0 14px 0;"><strong style="color: #ef4444;">④ *ST建艺（002789）：</strong>
        <br>• <strong>最高优先级</strong>：任何价格立即清仓止损
        <br>• 若有反弹至8.5-9元，必须坚决离场
        <br>• 退市风险敞口必须关闭，绝不恋战
    </p>

    <h4 style="color: #f59e0b; margin: 0 0 12px 0; font-size: 15px;">🎯 新建仓计划</h4>
    <p style="margin: 0 0 10px 0;"><strong>锐捷网络（301165）：</strong>回调至 <strong>145-150元</strong> 区间可小仓位介入（1成以内），止损140元，目标175-185元。机构大买+算力基础设施逻辑，中期看好。</p>
    <p style="margin: 0 0 14px 0;"><strong>招金黄金（600489）：</strong>回调至 <strong>11.5-12元</strong> 可轻仓布局（0.5成），止损10.5元，目标15-16元。金价中长期上涨趋势明确，作为防御配置。</p>

    <h4 style="color: #f59e0b; margin: 0 0 12px 0; font-size: 15px;">⚠️ 仓位管理</h4>
    <p style="margin: 0;">整体仓位控制在 <strong>3-4成</strong>，其中雅克科技为核心底仓（1-1.5成），其余持仓逢高减仓。现金为王，等待市场真正企稳信号（缩量+止跌+政策催化）。不盲目抄底，不追高资源股，耐心等待确定性机会。</p>
</div>
"""

gen.add_trading_plan(trading_plan)

# ==================== 11. 晚间重要新闻 ====================
evening_news = [
    {
        "title": "佰维存储董事长提议2亿-2.5亿元回购股份，全部用于注销减资",
        "content": "佰维存储控股股东、实际控制人兼董事长孙成思提议公司以集中竞价交易方式回购A股股份，资金规模2.00亿至2.50亿元，所回购股份全部用于注销以缩减注册资本。回购价格不超过董事会审议通过前...",
        "time": "19:43",
        "source": "公司公告",
        "tag": "利好",
        "tag_variant": "success"
    },
    {
        "title": "国际金价突破4100美元/盎司 创历史新高",
        "content": "受美联储降息预期升温、地缘政治风险加剧、美元走弱多重因素影响，现货黄金突破4100美元/盎司关键关口，创历史新高。黄金股今日集体大涨，山金国际三连板、招金黄金涨停。",
        "time": "18:30",
        "source": "东方财富",
        "tag": "行业催化",
        "tag_variant": "warning"
    },
    {
        "title": "央行今日开展760亿元7天期逆回购，净回笼3505亿元",
        "content": "7月22日央行公告完成760亿元7天期逆回购操作，操作利率1.40%。同日有4265亿元逆回购到期，实现净回笼3505亿元。资金面整体平稳，Shibor隔夜品种下行3.0个基点至1.38%。",
        "time": "11:27",
        "source": "央行公告",
        "tag": "宏观",
        "tag_variant": "default"
    },
    {
        "title": "二季度公募基金规模达39.66万亿，主动权益基金增超万亿",
        "content": "截至2026年二季度末，全市场公募基金合计规模达39.66万亿元，较一季度末增加约2.14万亿元，环比增幅5.7%。主动管理股票型+混合型基金规模新增超1万亿元，科技行情推动权益基金扩容。",
        "time": "07:00",
        "source": "财联社",
        "tag": "行业数据",
        "tag_variant": "info"
    },
    {
        "title": "星辉环材拟斥1亿至2亿元回购A股股份",
        "content": "星辉环材公告拟使用自有资金以集中竞价交易方式回购公司已发行的人民币普通股，回购资金总额不低于1亿元且不超过2亿元，回购价格不超过65.54元/股。回购股份用于维护公司价值及股东权益。",
        "time": "10:19",
        "source": "公司公告",
        "tag": "利好",
        "tag_variant": "success"
    },
]

gen.add_evening_news(evening_news)

# ==================== 12. 风险提示 ====================
risks = [
    "科技成长股获利回吐风险：昨日暴涨后今日大幅回调，若明日继续放量下跌可能形成二次探底",
    "北向资金持续流出：今日净流出约292亿，若外资持续撤离将进一步压制成长股表现",
    "中报业绩雷风险：中报披露进入尾声，警惕业绩不及预期的个股爆雷",
    "地缘政治风险：中东局势紧张加剧，可能引发全球市场波动",
    "成交缩量信号：今日缩量3000亿至2.65万亿，增量资金不足可能导致反弹夭折",
    "持仓股风险：铜冠铜箔技术形态破位、*ST建艺退市风险未解除，需严格执行纪律"
]

gen.add_risk_warning(risks)

# ==================== 发布报告 ====================
print("正在生成并发布报告...")
result = gen.publish(
    title="盘后速递",
    report_type="aftermarket",
    filename="20260722_盘后速递.html",
    excerpt="市场分化加剧，高低切换极致演绎。贵金属领涨，PCB/存储芯片领跌。成交缩量至2.65万亿，北向资金净流出292亿。持仓股雅克科技+4.4%延续反弹，铜冠铜箔-11.33%重创。",
    auto_deploy=True
)

print(f"发布结果: {result}")
print("✅ 盘后速递报告生成完成！")
