# coding: utf-8
"""
盘后速递生成脚本 - 2026年07月09日
使用 V3.0 AftermarketGenerator
"""
import sys
import os

WORK_DIR = '/root/daily-news-insight'
sys.path.insert(0, os.path.join(WORK_DIR, 'v3'))
os.chdir(WORK_DIR)

from v3.generators.aftermarket import AftermarketGenerator
from v3.components.layout import Section

gen = AftermarketGenerator(date_str="20260709", subtitle="2026.07.09 · 盘后速递")

# 1. 今日核心亮点
gen.add_today_highlight(
    "半导体产业链大爆发！科创50暴涨8.41%创历史第四大单日涨幅，"
    "长鑫科技IPO启动引爆存储板块，雅克科技涨停创历史新高。"
    "两市成交2.93万亿放量反弹，近5000股飘红，情绪由冰点快速回升至极度贪婪区间。"
)

# 2. 市场收盘总结
indices = [
    {"name": "上证指数", "value": "4036.59", "change": "+1.65%", "up": True, "icon": "trending_up"},
    {"name": "深证成指", "value": "15398.73", "change": "+3.07%", "up": True, "icon": "trending_up"},
    {"name": "创业板指", "value": "4018.17", "change": "+4.49%", "up": True, "icon": "trending_up"},
    {"name": "科创50", "value": "2185.83", "change": "+8.41%", "up": True, "icon": "rocket_launch"},
]
gen.add_market_summary(indices=indices, volume="2.93万亿", northbound="成交4007.68亿")

# 3. 情绪温度计
gen.add_sentiment_thermometer(
    temperature=82,
    volume="2.93万亿",
    up_count="4950↑",
    down_count="550↓",
    limit_up_count=148
)

# 4. 晚间重要新闻
gen.add_evening_news([
    {
        "title": "国家超算互联网核心节点正式上线，十万卡国产AI算力投入运营",
        "content": "7月9日，国家超算互联网核心节点在郑州正式上线运行。该节点是接入国家超算互联网的单体十万卡全精度算力资源池，可同时支撑十万卡、十万亿级参数大模型全量训练。目前国家超算互联网已建成汇聚超350万CPU核、25万GPU卡的全国规模最大一体化算力网络，注册用户超140万。",
        "time": "2026-07-09 16:34",
        "source": "央视新闻",
        "tag": "算力利好",
        "tag_variant": "primary"
    },
    {
        "title": "兆易创新半年预增超10倍，存储芯片龙头业绩大爆发",
        "content": "兆易创新(603986)发布2026年半年度业绩预增公告，上半年营收预计115亿元，同比增长约177%；归母净利润约69亿元，同比暴涨1099%。业绩增长主要系存储芯片行业供需紧张，公司存储产品量价齐升。",
        "time": "2026-07-09 18:38",
        "source": "财联社",
        "tag": "业绩超预期",
        "tag_variant": "success"
    },
    {
        "title": "长鑫科技启动科创板IPO，295亿募资刷新年内纪录",
        "content": "7月8日晚，长鑫科技在上交所披露上市招股意向书，7月13日启动初步询价，7月16日新股申购，预计7月底前挂牌。公司上半年预计营收1100-1200亿元，归母净利润500-570亿元。作为国内DRAM绝对龙头，上市将填补科创板存储高端标的稀缺性。",
        "time": "2026-07-09 08:00",
        "source": "每日经济新闻",
        "tag": "重磅IPO",
        "tag_variant": "warning"
    },
    {
        "title": "天赐材料上半年净利预增908%-1020%，电解液量价齐升",
        "content": "天赐材料(002709)公告，预计2026年上半年净利润27-30亿元，同比增长908%-1020%。电解液及六氟磷酸锂需求旺盛，销量显著增长，行业供需格局优化带动产品价格上行。",
        "time": "2026-07-09 17:12",
        "source": "证券时报",
        "tag": "业绩预增",
        "tag_variant": "success"
    },
    {
        "title": "三星晶圆代工新客户涨价15%，先进制程供需紧张加剧",
        "content": "三星电子已将晶圆代工新客户供货价格提高约15%，主要针对4nm和5nm等需求量大的先进制程节点，以及部分车用8nm节点。此前台积电已通知主要客户计划涨价5%-10%。AI算力驱动下，先进制程产能紧张格局持续。",
        "time": "2026-07-09 14:00",
        "source": "上海证券报",
        "tag": "行业涨价",
        "tag_variant": "danger"
    },
])

# 5. 持仓股深度诊断
holdings_detail_html = '''
<div style="display: flex; flex-direction: column; gap: 18px;">
    <!-- 英维克 -->
    <div style="background: rgba(30,30,50,0.5); border: 1px solid rgba(255,255,255,0.08); border-radius: 16px; padding: 20px; box-shadow: 0 2px 8px rgba(0,0,0,0.2);">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px;">
            <div>
                <span style="font-size: 17px; font-weight: 700; color: #f1f5f9;">英维克 (002837)</span>
                <span style="font-size: 12px; color: #9ca3af; margin-left: 8px;">液冷散热 · AI算力基础设施</span>
            </div>
            <div style="text-align: right;">
                <div style="font-size: 20px; font-weight: 800; color: #10b981;">75.87元</div>
                <div style="font-size: 13px; font-weight: 600; color: #10b981;">+5.20%</div>
            </div>
        </div>
        <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 10px; margin-bottom: 14px;">
            <div style="background: rgba(255,255,255,0.04); padding: 10px; border-radius: 8px; text-align: center;">
                <div style="font-size: 11px; color: #94a3b8;">成交额</div>
                <div style="font-size: 14px; font-weight: 700; color: #e2e8f0;">55.0亿</div>
            </div>
            <div style="background: rgba(255,255,255,0.04); padding: 10px; border-radius: 8px; text-align: center;">
                <div style="font-size: 11px; color: #94a3b8;">换手率</div>
                <div style="font-size: 14px; font-weight: 700; color: #e2e8f0;">6.59%</div>
            </div>
            <div style="background: rgba(255,255,255,0.04); padding: 10px; border-radius: 8px; text-align: center;">
                <div style="font-size: 11px; color: #94a3b8;">今日最高</div>
                <div style="font-size: 14px; font-weight: 700; color: #f1f5f9;">76.55</div>
            </div>
            <div style="background: rgba(255,255,255,0.04); padding: 10px; border-radius: 8px; text-align: center;">
                <div style="font-size: 11px; color: #94a3b8;">今日最低</div>
                <div style="font-size: 14px; font-weight: 700; color: #f1f5f9;">68.24</div>
            </div>
        </div>
        <div style="font-size: 13.5px; color: #cbd5e1; line-height: 1.8;">
            <p style="margin: 0 0 8px 0;"><strong style="color: #fbbf24;">📊 技术面诊断：</strong>今日探底68.24元后强势V型反弹收75.87元，振幅8.39%，收盘接近全天最高点。MA5(72.95)与MA60(75.82)形成双重支撑，价格站稳MA60线上方。MA10(74.97)、MA20(75.21)已被收复，短期均线系统有拐头向上迹象。MACD仍处死叉状态但绿柱有收敛迹象，RSI回升至51.71进入中性偏强区间。上方第一压力位在80元整数关口，强压力位在89-90元区间(前期密集成交区)。下方支撑72-73元(MA5)、68元(今日低点)。</p>
            <p style="margin: 0 0 8px 0;"><strong style="color: #fbbf24;">💸 资金面分析：</strong>今日主力资金净流入约+2.15亿元，结束连续多日净流出态势，反弹中资金有明显回补迹象。但近5日累计仍净流出约-6.54亿元，中期资金流出趋势尚未根本扭转。北向资金持仓比例未见明显变化。成交额从前几日40亿左右放大至55亿，放量反弹显示有增量资金参与博弈。</p>
            <p style="margin: 0 0 8px 0;"><strong style="color: #fbbf24;">📰 消息面催化：</strong>AI算力+液冷板块今日整体大反弹，国家超算互联网核心节点上线(十万卡国产算力)强化算力基础设施逻辑，市场情绪全面回暖带动超跌股修复。但公司层面暂无实质性利好公告。</p>
            <p style="margin: 0;"><strong style="color: #ef4444;">🎯 操作建议：</strong>当前价格75.87元，距成本价104.23元仍有-27.2%的深度套牢，本次反弹性质为超跌修复而非反转。<br/>
            <strong>减仓计划：</strong>75-78元区间坚决减仓至1/3底仓以下；若继续反弹至80元以上，可再减1/3；85元以上考虑全部清仓。<br/>
            <strong>止损纪律：</strong>若回落跌破72元(MA5)减仓一半，跌破68元(今日低点)无条件清仓止损。<br/>
            <strong>严禁补仓摊薄成本</strong>，中期均线系统仍处于空头排列，反弹结束后大概率继续探底。</p>
        </div>
    </div>

    <!-- 铜冠铜箔 -->
    <div style="background: rgba(30,30,50,0.5); border: 1px solid rgba(255,255,255,0.08); border-radius: 16px; padding: 20px; box-shadow: 0 2px 8px rgba(0,0,0,0.2);">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px;">
            <div>
                <span style="font-size: 17px; font-weight: 700; color: #f1f5f9;">铜冠铜箔 (301217)</span>
                <span style="font-size: 12px; color: #9ca3af; margin-left: 8px;">锂电铜箔 · PCB铜箔 · HBM上游材料</span>
            </div>
            <div style="text-align: right;">
                <div style="font-size: 20px; font-weight: 800; color: #10b981;">139.68元</div>
                <div style="font-size: 13px; font-weight: 600; color: #10b981;">+4.24%</div>
            </div>
        </div>
        <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 10px; margin-bottom: 14px;">
            <div style="background: rgba(255,255,255,0.04); padding: 10px; border-radius: 8px; text-align: center;">
                <div style="font-size: 11px; color: #94a3b8;">成交额</div>
                <div style="font-size: 14px; font-weight: 700; color: #e2e8f0;">48.6亿</div>
            </div>
            <div style="background: rgba(255,255,255,0.04); padding: 10px; border-radius: 8px; text-align: center;">
                <div style="font-size: 11px; color: #94a3b8;">换手率</div>
                <div style="font-size: 14px; font-weight: 700; color: #e2e8f0;">4.32%</div>
            </div>
            <div style="background: rgba(255,255,255,0.04); padding: 10px; border-radius: 8px; text-align: center;">
                <div style="font-size: 11px; color: #94a3b8;">浮动盈亏</div>
                <div style="font-size: 14px; font-weight: 700; color: #10b981;">+60.3%</div>
            </div>
            <div style="background: rgba(255,255,255,0.04); padding: 10px; border-radius: 8px; text-align: center;">
                <div style="font-size: 11px; color: #94a3b8;">今日振幅</div>
                <div style="font-size: 14px; font-weight: 700; color: #f1f5f9;">7.21%</div>
            </div>
        </div>
        <div style="font-size: 13.5px; color: #cbd5e1; line-height: 1.8;">
            <p style="margin: 0 0 8px 0;"><strong style="color: #fbbf24;">📊 技术面诊断：</strong>今日探底130.40元后V型反弹收139.68元，基本收复昨日(7月8日)大跌失地，收盘接近全天最高点。MA5(143.46)构成短期第一压力位，MA10(153.61)、MA20(163.71)仍在上方形成压制，短期均线系统空头排列未改。MACD死叉绿柱放大，RSI仅22.96处于超卖区间，显示反弹动能虽强但趋势性反转仍需时间。支撑位：130元(今日低点)、129.5元(技术支撑位)、109.76元(MA60)。压力位：143.46元(MA5)、150元(整数关口)、153.61元(MA10)。</p>
            <p style="margin: 0 0 8px 0;"><strong style="color: #fbbf24;">💸 资金面分析：</strong>今日主力资金净流入约+3.26亿元，超跌后抄底资金明显介入。但近5日累计净流出约-15.27亿元，流出幅度仍然巨大，短期反弹后大概率仍有抛压。北向资金持仓稳定，未见大幅进出。成交额从前几日30亿左右放大至48.6亿，放量反弹显示多空分歧加大。</p>
            <p style="margin: 0 0 8px 0;"><strong style="color: #fbbf24;">📰 消息面催化：</strong>存储产业链今日集体爆发(HBM概念持续升温)，铜箔作为上游关键材料同步受益。三星晶圆代工涨价15%、长鑫科技IPO启动，整体半导体板块情绪高涨。但铜冠铜箔主业以锂电铜箔为主，HBM高端铜箔占比有限，需警惕题材炒作后的回落风险。</p>
            <p style="margin: 0;"><strong style="color: #ef4444;">🎯 操作建议：</strong>成本价87.16元，浮盈约+60.3%，利润已较丰厚，但近几日从180元高点回撤幅度超过22%，趋势走坏。<br/>
            <strong>减仓计划：</strong>140-145元区间继续减仓至1/3底仓以下锁定利润；若放量突破145元(MA5上方)可再持有观察1-2日，目标位150-155元；155元以上减至底仓。<br/>
            <strong>止损纪律：</strong>若回落跌破135元(今日反弹中位)减仓一半，跌破130元(今日低点)无条件清仓止盈。<br/>
            <strong>中期逻辑：</strong>锂电铜箔产能过剩担忧仍在，HBM铜箔贡献有限，建议趁反弹降低仓位，保留底仓观察中报业绩。</p>
        </div>
    </div>

    <!-- 雅克科技 -->
    <div style="background: rgba(30,30,50,0.5); border: 1px solid rgba(16,185,129,0.3); border-radius: 16px; padding: 20px; box-shadow: 0 2px 16px rgba(16,185,129,0.1);">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px;">
            <div>
                <span style="font-size: 17px; font-weight: 700; color: #f1f5f9;">雅克科技 (002409)</span>
                <span style="font-size: 12px; color: #9ca3af; margin-left: 8px;">半导体材料 · 光刻胶前驱体 · HBM材料</span>
                <span style="display: inline-block; background: linear-gradient(135deg, #10b981 0%, #059669 100%); color: white; font-size: 11px; font-weight: 700; padding: 2px 8px; border-radius: 10px; margin-left: 8px;">历史新高 ⭐</span>
            </div>
            <div style="text-align: right;">
                <div style="font-size: 20px; font-weight: 800; color: #10b981;">209.00元</div>
                <div style="font-size: 13px; font-weight: 600; color: #10b981;">+10.00% 涨停</div>
            </div>
        </div>
        <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 10px; margin-bottom: 14px;">
            <div style="background: rgba(255,255,255,0.04); padding: 10px; border-radius: 8px; text-align: center;">
                <div style="font-size: 11px; color: #94a3b8;">成交额</div>
                <div style="font-size: 14px; font-weight: 700; color: #e2e8f0;">64.5亿</div>
            </div>
            <div style="background: rgba(255,255,255,0.04); padding: 10px; border-radius: 8px; text-align: center;">
                <div style="font-size: 11px; color: #94a3b8;">换手率</div>
                <div style="font-size: 14px; font-weight: 700; color: #e2e8f0;">10.08%</div>
            </div>
            <div style="background: rgba(255,255,255,0.04); padding: 10px; border-radius: 8px; text-align: center;">
                <div style="font-size: 11px; color: #94a3b8;">浮动盈亏</div>
                <div style="font-size: 14px; font-weight: 700; color: #10b981;">+92.1%</div>
            </div>
            <div style="background: rgba(255,255,255,0.04); padding: 10px; border-radius: 8px; text-align: center;">
                <div style="font-size: 11px; color: #94a3b8;">封单金额</div>
                <div style="font-size: 14px; font-weight: 700; color: #f1f5f9;">9.73亿</div>
            </div>
        </div>
        <div style="font-size: 13.5px; color: #cbd5e1; line-height: 1.8;">
            <p style="margin: 0 0 8px 0;"><strong style="color: #fbbf24;">📊 技术面诊断：</strong>今日一字板未遂后深V反转，最低探175.11元，最终13:40封死涨停209元，创历史新高！全天振幅巨大，显示多空博弈激烈。MA5(194.15)、MA10(203.99)、MA20(177.95)呈多头排列，价格突破所有短期均线压制。MACD虽处死叉但今日大阳线后大概率将形成金叉，RSI回升至66.8进入偏强区间。上方第一目标位212-215元(技术压力位)，中期目标看240-250元(20日线高点)。下方支撑：204元(MA10)、194元(MA5)、178元(MA20/今日低点附近)。</p>
            <p style="margin: 0 0 8px 0;"><strong style="color: #fbbf24;">💸 资金面分析：</strong>今日主力资金净流入约+5.87亿元，涨停封单约9.73亿元，资金认可度非常高。但近5日累计净流出约-19.43亿元，说明前期调整过程中资金大幅撤离，今日属于集中回补。龙虎榜数据待进一步确认。北向资金今日大概率增仓。成交额64.46亿元创近期新高，放量涨停说明增量资金入场。</p>
            <p style="margin: 0 0 8px 0;"><strong style="color: #fbbf24;">📰 消息面催化：</strong><strong>三重催化共振：</strong>①长鑫科技IPO启动，存储产业链整体估值抬升，雅克作为前驱体材料龙头直接受益；②三星晶圆代工涨价15%，上游材料国产替代逻辑强化；③国家超算互联网核心节点上线，AI算力建设拉动半导体材料需求。公司中报业绩预期向好，半导体材料量价齐升逻辑持续兑现。</p>
            <p style="margin: 0;"><strong style="color: #ef4444;">🎯 操作建议：</strong>成本价108.80元，浮盈+92.1%，持仓中盈利最丰厚的标的，也是半导体材料核心龙头。<br/>
            <strong>减仓计划：</strong>明日若高开在215-220元区间，减仓1/3锁定利润；若继续冲高至230-240元，再减1/3；保留1/3底仓博弈中报行情和存储产业趋势。<br/>
            <strong>持有底线：</strong>收盘不破200元(MA10/涨停板中位)可继续持有；跌破200元减仓一半；跌破180元(MA20)止盈离场。<br/>
            <strong>中期策略：</strong>半导体材料国产替代+存储超级周期是全年主线，雅克科技作为前驱体+光刻胶双龙头，长期看好。但短期涨幅过大且创出历史新高，波动会加剧，建议分批止盈降低仓位，保留底仓参与趋势。</p>
        </div>
    </div>

    <!-- *ST建艺 -->
    <div style="background: rgba(30,30,50,0.5); border: 1px solid rgba(239,68,68,0.3); border-radius: 16px; padding: 20px; box-shadow: 0 2px 8px rgba(0,0,0,0.2);">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px;">
            <div>
                <span style="font-size: 17px; font-weight: 700; color: #f1f5f9;">*ST建艺 (002789)</span>
                <span style="font-size: 12px; color: #9ca3af; margin-left: 8px;">建筑装饰 · ST股</span>
                <span style="display: inline-block; background: linear-gradient(135deg, #dc2626 0%, #991b1b 100%); color: white; font-size: 11px; font-weight: 700; padding: 2px 8px; border-radius: 10px; margin-left: 8px;">退市预警 🚨</span>
            </div>
            <div style="text-align: right;">
                <div style="font-size: 20px; font-weight: 800; color: #ef4444;">10.38元</div>
                <div style="font-size: 13px; font-weight: 600; color: #ef4444;">-1.61%</div>
            </div>
        </div>
        <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 10px; margin-bottom: 14px;">
            <div style="background: rgba(255,255,255,0.04); padding: 10px; border-radius: 8px; text-align: center;">
                <div style="font-size: 11px; color: #94a3b8;">成交额</div>
                <div style="font-size: 14px; font-weight: 700; color: #e2e8f0;">2114万</div>
            </div>
            <div style="background: rgba(255,255,255,0.04); padding: 10px; border-radius: 8px; text-align: center;">
                <div style="font-size: 11px; color: #94a3b8;">换手率</div>
                <div style="font-size: 14px; font-weight: 700; color: #e2e8f0;">1.30%</div>
            </div>
            <div style="background: rgba(255,255,255,0.04); padding: 10px; border-radius: 8px; text-align: center;">
                <div style="font-size: 11px; color: #94a3b8;">浮动盈亏</div>
                <div style="font-size: 14px; font-weight: 700; color: #ef4444;">-22.8%</div>
            </div>
            <div style="background: rgba(255,255,255,0.04); padding: 10px; border-radius: 8px; text-align: center;">
                <div style="font-size: 11px; color: #94a3b8;">风险等级</div>
                <div style="font-size: 14px; font-weight: 700; color: #ef4444;">极高危</div>
            </div>
        </div>
        <div style="font-size: 13.5px; color: #cbd5e1; line-height: 1.8;">
            <p style="margin: 0 0 8px 0;"><strong style="color: #fbbf24;">📊 技术面诊断：</strong>今日延续弱势，开盘10.54元最高10.66元最低10.09元，收盘10.38元下跌1.61%。昨日开板反弹后今日再度走弱，显示反弹力度极弱。MA5(10.84)、MA10(11.28)、MA20(12.38)、MA60(12.96)全线空头排列，价格处于所有均线下方。MACD死叉绿柱持续放大，RSI仅16.44处于深度超卖区间，但超卖不代表见底，ST股可能持续阴跌。支撑位：9.98元(技术支撑)、10元整数关口。压力位：10.84元(MA5)、11.28元(MA10)。</p>
            <p style="margin: 0 0 8px 0;"><strong style="color: #fbbf24;">💸 资金面分析：</strong>今日主力资金净流出约-300万元，虽然金额不大但持续流出。成交额仅2114万元，换手率1.30%，成交极度萎缩，说明买盘匮乏，缺乏主力资金介入。北向资金无持仓。在退市风险明确的背景下，机构资金大概率已全部撤离，仅剩散户博弈。</p>
            <p style="margin: 0 0 8px 0;"><strong style="color: #fbbf24;">📰 消息面催化：</strong>退市风险未消除，公司债务违约、诉讼缠身、经营困难三大问题没有任何改善迹象。装饰行业整体低迷，公司无任何产业升级或转型计划。ST板块今日整体表现一般，未出现板块性反弹行情。</p>
            <p style="margin: 0;"><strong style="color: #ef4444;">🎯 操作建议：</strong>成本价13.45元，浮亏-22.8%，<strong>必须立即执行止损纪律，绝不抱有任何幻想！</strong><br/>
            <strong>清仓计划：</strong>明日集合竞价直接挂单清仓，或开盘后在10.3-10.5元区间全部卖出，不再犹豫。<br/>
            <strong>若反弹：</strong>若明日有反弹至10.8-11元(MA5附近)机会，更是绝佳离场窗口，必须全部清仓。<br/>
            <strong>极端情况：</strong>若跌破10元整数关口，不计成本立即止损，避免退市归零风险。<br/>
            <strong>核心警示：</strong>ST股一旦退市，股价可能跌至1元以下甚至归零，损失将是90%+。当前-22.8%的亏损是可承受范围，及时止损保留资金才是正确选择。投资的核心是<strong>先活下去，再谈赚钱</strong>。</p>
        </div>
    </div>
</div>
'''

holdings_section = Section(title="💼 持仓股深度诊断", content=holdings_detail_html, icon="briefcase")
gen._components.append(holdings_section)

# 6. 板块涨跌幅排行
up_sectors = [
    {"name": "半导体设备", "change": "+10.0%", "up": True},
    {"name": "存储芯片", "change": "+8.5%", "up": True},
    {"name": "AI芯片", "change": "+7.2%", "up": True},
    {"name": "先进封装", "change": "+6.8%", "up": True},
    {"name": "CPO/光模块", "change": "+5.5%", "up": True},
    {"name": "科创50", "change": "+8.41%", "up": True},
    {"name": "半导体材料", "change": "+6.2%", "up": True},
    {"name": "PCB", "change": "+4.8%", "up": True},
    {"name": "券商", "change": "+3.2%", "up": True},
    {"name": "算力基础设施", "change": "+4.2%", "up": True},
]
down_sectors = [
    {"name": "煤炭", "change": "-1.2%", "up": False},
    {"name": "石油石化", "change": "-0.8%", "up": False},
    {"name": "锂矿/锂电", "change": "-3.5%", "up": False},
    {"name": "银行", "change": "+0.3%", "up": True},
    {"name": "食品饮料", "change": "-0.5%", "up": False},
]
gen.add_sector_performance(up_sectors=up_sectors, down_sectors=down_sectors)

# 7. 盘面深度解读
gen.add_market_deep_analysis(
    strong_sectors=[
        {
            "name": "半导体设备",
            "reason": "长鑫科技IPO启动(拟募资295亿，上半年净利500-570亿)直接引爆存储扩产预期，从产业链传导看刻蚀、薄膜沉积、CMP等设备率先获益。半导体设备ETF涨停，板块涨幅超10%。结合三星晶圆代工涨价15%，国产替代逻辑进一步强化。"
        },
        {
            "name": "存储芯片",
            "reason": "长鑫科技招股书披露+兆易创新半年预增1099%+威刚董事长预计Q3 DRAM合约价续涨20-30%，三重利好叠加。板块涨幅超8%，雅克科技涨停创历史新高，兆易创新涨停成交382亿。AI驱动下存储供需紧张至少延续至2027年下半年。"
        },
        {
            "name": "先进封装/CPO",
            "reason": "AI算力建设带动先进封装需求爆发，通富微电涨停(机构净买6.61亿+北向净买8.95亿)。CPO概念午后飙升，东山精密、光迅科技、长电科技涨停，中际旭创成交416亿居A股首位。光模块龙头仍保持高景气低估值特征。"
        },
        {
            "name": "AI算力",
            "reason": "国家超算互联网核心节点今日正式上线，十万卡国产AI算力投入运营，强化算力基础设施自主可控逻辑。浪潮信息连续两日涨停，市值破千亿。算力产业链基本面具有强韧性，多家龙头Q2业绩积极预增。"
        },
    ],
    weak_sectors=[
        {
            "name": "锂矿/锂电池",
            "reason": "天华新能跌近15%，融捷股份连续两日跌停，天齐锂业、中矿资源跌超6%。虽然天赐材料、天华新能等发布亮眼业绩预告，但市场担忧锂价见顶回落+产能过剩，股价反而下跌，典型的利好出尽行情。"
        },
        {
            "name": "煤炭/石油石化",
            "reason": "市场风格切换至科技成长，传统能源板块承压。资金从低位价值板块大幅流出，转向半导体等成长赛道。煤炭板块-1.2%、石油石化-0.8%，中国神华、中国石油等龙头飘绿。"
        },
    ],
    core_view=(
        "今日A股上演深V大反转，科创50暴涨8.41%创历史第四大单日涨幅，半导体产业链全线爆发是核心驱动。"
        "长鑫科技IPO启动+三星代工涨价+国家超算节点上线三重催化共振，引发存储、设备、材料、封装全产业链行情。"
        "两市成交2.93万亿放量4800亿，近5000股飘红，情绪从周三的冰点快速回升至极度贪婪区间。"
        "但需注意：①放量大涨后短线获利盘丰厚，明日面临分化压力；②锂矿等板块大跌说明资金在调仓而非全面加仓；"
        "③科创50单日8%+的暴涨历史上多为脉冲行情，持续性需要观察。"
        "操作上建议：持仓股趁反弹减仓优化结构，聚焦半导体材料/设备/存储等核心主线，回避高位纯题材股。"
    )
)

# 8. 龙虎榜
dragon_stocks = [
    {
        "name": "通富微电 (002156)",
        "code": "先进封装龙头",
        "change": "+10.00% 涨停",
        "up": True,
        "reason": "日涨幅偏离值7.78%",
        "net_buy": "机构净买6.61亿 + 北向净买8.95亿",
        "institutions": 5,
    },
    {
        "name": "瑞华泰 (688323)",
        "code": "PI膜 · 半导体材料",
        "change": "+20.00% 涨停",
        "up": True,
        "reason": "日换手率达30%+",
        "net_buy": "机构净买13.37亿(今日机构净买王)",
        "institutions": 4,
    },
    {
        "name": "华天科技 (002185)",
        "code": "集成电路封测",
        "change": "+10.00% 涨停",
        "up": True,
        "reason": "日涨幅偏离值7%+",
        "net_buy": "机构净买3.07亿 + 北向净买4.31亿",
        "institutions": 3,
    },
    {
        "name": "上海新阳 (300236)",
        "code": "半导体材料 · 电子化学品",
        "change": "+20.00% 涨停",
        "up": True,
        "reason": "日涨幅达20%",
        "net_buy": "机构净买1.88亿 + 北向净买1.97亿",
        "institutions": 2,
    },
]
gen.add_dragon_tiger_list(stocks=dragon_stocks)

# 龙虎榜深度分析
dragon_analysis_html = '''
<div style="margin-top: 16px; background: rgba(30,30,50,0.5); border: 1px solid rgba(255,255,255,0.08); border-radius: 14px; padding: 18px;">
    <div style="font-size: 15px; font-weight: 700; color: #f1f5f9; margin-bottom: 12px;">📊 龙虎榜深度解读</div>
    <div style="font-size: 13.5px; color: #cbd5e1; line-height: 1.9;">
        <p style="margin: 0 0 10px 0;"><strong style="color: #10b981;">通富微电——机构+北向双轮驱动，封测龙头地位确认：</strong>
        今日通富微电涨停成交113.39亿元，龙虎榜显示5家机构专用席位合计净买入6.61亿元，深股通专用席位净买入8.95亿元，合计净买超15.5亿元。
        买入方以机构和北向为主，属于典型的机构定调行情。通富微电作为国内封测第二大企业，直接受益于AI算力带动的先进封装需求爆发。
        近半年该股累计上榜龙虎榜6次，上榜次日股价平均涨4.39%，短期持续性较好。但需注意近5日主力资金净流入仅9.70亿元，今日单日贡献了大部分，说明资金集中性爆发而非持续建仓。
        <strong>操作建议：</strong>明日若高开在76-78元区间可轻仓追入博弈趋势，止损位72元(今日涨停板中位)，目标位85-90元。</p>
        
        <p style="margin: 0 0 10px 0;"><strong style="color: #10b981;">瑞华泰——机构重金押注的半导体材料黑马：</strong>
        今日机构净买入冠军，13.37亿元的机构净买额远超第二名，显示机构对PI膜材料赛道的强烈看好。
        瑞华泰是国内聚酰亚胺薄膜龙头，产品广泛应用于柔性电路板、半导体封装等领域，在AI服务器、HBM等高端场景需求爆发下，高端PI膜供需紧张。
        20cm涨停后短期涨幅较大，建议<strong>观察次日承接力</strong>，若能维持高位震荡且量能不萎缩，可关注回踩5日线后的低吸机会。
        <strong>止损位：</strong>跌破今日涨停板开盘价(约30%涨幅位置)止损。</p>
        
        <p style="margin: 0 0 10px 0;"><strong style="color: #10b981;">华天科技——封测板块全面启动的验证信号：</strong>
        华天科技涨停，机构净买3.07亿+北向净买4.31亿，与通富微电形成封测双子星格局。
        这说明<strong>先进封装不是个股行情而是板块行情</strong>，背后的产业逻辑是AI算力带动Chiplet/2.5D/3D封装需求爆发。
        华天科技市值相对较小(约500亿级)，弹性可能更大。<strong>建议：</strong>封测板块可关注长电科技(市值最大最稳)、通富微电(AMD产业链)、华天科技(弹性最大)的三剑客组合。</p>
        
        <p style="margin: 0;"><strong style="color: #f59e0b;">整体判断：</strong>
        今日龙虎榜机构净买入集中在半导体产业链(封测、材料、设备)，与盘面主线高度一致，说明本轮反弹有机构资金参与而非单纯游资炒作。
        机构净买入30只、净卖出27只，多空基本平衡，但<strong>买入方向高度集中在半导体</strong>，卖出分散在各行业，说明机构正在进行结构性调仓。
        持续性判断：封测/半导体材料板块有机构+产业逻辑双重支撑，持续性评级<strong>A级(3-5天)</strong>，但短期暴涨后明日大概率分化，建议等回调再介入，不追高。</p>
    </div>
</div>
'''
dragon_analysis_section = Section(title="🐉 龙虎榜深度分析", content=dragon_analysis_html, icon="award")
gen._components.append(dragon_analysis_section)

# 9. 重点关注标的
watchlist_html = '''
<div style="display: flex; flex-direction: column; gap: 14px;">
    <div style="background: rgba(30,30,50,0.5); border: 1px solid rgba(139,92,246,0.2); border-radius: 14px; padding: 16px;">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 10px;">
            <div>
                <span style="font-size: 16px; font-weight: 700; color: #f1f5f9;">中芯国际 (688981)</span>
                <span style="font-size: 12px; background: rgba(139,92,246,0.2); color: #a78bfa; padding: 2px 8px; border-radius: 10px; margin-left: 8px;">晶圆代工龙头</span>
            </div>
            <span style="font-size: 14px; font-weight: 700; color: #10b981;">+13.87%</span>
        </div>
        <div style="font-size: 13px; color: #cbd5e1; line-height: 1.75;">
            <p style="margin: 0 0 6px 0;"><strong>逻辑：</strong>国内晶圆代工绝对龙头，直接受益于三星/台积电涨价潮+国产替代加速。今日涨近14%创上市新高，成交超300亿。长鑫科技/长江存储陆续上市，整个国产半导体产业链估值体系重估，中芯国际作为产业链总龙头估值锚定会持续上移。2026Q2业绩有望超预期。</p>
            <p style="margin: 0 0 6px 0;"><strong>买入区间：</strong>回调至95-100元区间(5日线附近)可分批建仓</p>
            <p style="margin: 0 0 6px 0;"><strong>目标价：</strong>短期目标120元，中期目标140元(对应2026年4倍PS)</p>
            <p style="margin: 0;"><strong style="color: #ef4444;">止损位：</strong>跌破90元(10日线)止损</p>
        </div>
    </div>
    
    <div style="background: rgba(30,30,50,0.5); border: 1px solid rgba(139,92,246,0.2); border-radius: 14px; padding: 16px;">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 10px;">
            <div>
                <span style="font-size: 16px; font-weight: 700; color: #f1f5f9;">上海新阳 (300236)</span>
                <span style="font-size: 12px; background: rgba(139,92,246,0.2); color: #a78bfa; padding: 2px 8px; border-radius: 10px; margin-left: 8px;">半导体材料 · 电子化学品</span>
            </div>
            <span style="font-size: 14px; font-weight: 700; color: #10b981;">+20.00% 20cm涨停</span>
        </div>
        <div style="font-size: 13px; color: #cbd5e1; line-height: 1.75;">
            <p style="margin: 0 0 6px 0;"><strong>逻辑：</strong>国内半导体电子化学品龙头，电镀液/清洗液/光刻胶产品布局全面。今日20cm涨停，龙虎榜显示机构净买1.88亿+北向净买1.97亿，机构+外资双双看好。存储扩产周期下，上游材料国产替代加速，公司核心产品验证导入向批量供货拐点临近。</p>
            <p style="margin: 0 0 6px 0;"><strong>买入区间：</strong>明日若开在60-65元(涨停板中位下方)可轻仓试错</p>
            <p style="margin: 0 0 6px 0;"><strong>目标价：</strong>短期目标75-80元，中期看100元(业绩兑现+估值提升)</p>
            <p style="margin: 0;"><strong style="color: #ef4444;">止损位：</strong>跌破55元(涨停板1/3位)止损</p>
        </div>
    </div>
    
    <div style="background: rgba(30,30,50,0.5); border: 1px solid rgba(139,92,246,0.2); border-radius: 14px; padding: 16px;">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 10px;">
            <div>
                <span style="font-size: 16px; font-weight: 700; color: #f1f5f9;">浪潮信息 (000977)</span>
                <span style="font-size: 12px; background: rgba(139,92,246,0.2); color: #a78bfa; padding: 2px 8px; border-radius: 10px; margin-left: 8px;">AI服务器龙头</span>
            </div>
            <span style="font-size: 14px; font-weight: 700; color: #10b981;">+10.00% 两连板</span>
        </div>
        <div style="font-size: 13px; color: #cbd5e1; line-height: 1.75;">
            <p style="margin: 0 0 6px 0;"><strong>逻辑：</strong>国内AI服务器市占率第一，上半年净利润预增226%-288%(26-31亿元)，业绩高增长确认。今日连续第二个涨停，市值突破千亿。国家超算互联网核心节点上线强化算力基础设施逻辑，AI算力建设高峰期远未结束。龙虎榜数据显示23.54亿主力资金抢筹。</p>
            <p style="margin: 0 0 6px 0;"><strong>买入区间：</strong>回调至75-78元区间(5日线附近)可建仓</p>
            <p style="margin: 0 0 6px 0;"><strong>目标价：</strong>短期目标95-100元，中期目标120元(对应2026年30倍PE)</p>
            <p style="margin: 0;"><strong style="color: #ef4444;">止损位：</strong>跌破70元(10日线)止损</p>
        </div>
    </div>

    <div style="background: rgba(239,68,68,0.05); border: 1px solid rgba(239,68,68,0.2); border-radius: 14px; padding: 16px;">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 10px;">
            <div>
                <span style="font-size: 16px; font-weight: 700; color: #f1f5f9;">⚠️ 风险警示：固德威 (688390)</span>
                <span style="font-size: 12px; background: rgba(239,68,68,0.2); color: #f87171; padding: 2px 8px; border-radius: 10px; margin-left: 8px;">机构大举出逃</span>
            </div>
            <span style="font-size: 14px; font-weight: 700; color: #ef4444;">机构净卖10.56亿</span>
        </div>
        <div style="font-size: 13px; color: #cbd5e1; line-height: 1.75;">
            <p style="margin: 0;">今日龙虎榜机构净卖出冠军，10.56亿机构资金砸盘出逃。光伏/储能板块今日虽有反弹但机构持续减仓，建议<strong>坚决回避</strong>所有光伏储能标的，机构出货周期远未结束。同类风险股：东山精密(机构净卖8.7亿)、锋龙股份(机构净卖7420万)。</p>
        </div>
    </div>
</div>
'''
watchlist_section = Section(title="🎯 重点关注标的", content=watchlist_html, icon="flag")
gen._components.append(watchlist_section)

# 10. 明日关键预判
gen.add_tomorrow_prediction([
    {
        "name": "半导体/存储产业链",
        "direction": "看涨",
        "confidence": 78,
        "reason": "长鑫科技IPO+三星涨价+机构重仓买入三重驱动，板块行情刚启动2天，资金介入深。但今日单日涨幅过大(科创50+8.4%)，明日大概率出现分化，前排龙头继续强势，后排跟风股回落。建议聚焦设备、材料、封测三大核心环节龙头。"
    },
    {
        "name": "大盘指数(上证指数)",
        "direction": "震荡",
        "confidence": 65,
        "reason": "今日放量大涨后4036点已站上4000点整数关口，但上方4050-4100点区间有前期套牢盘压力。连续放量拉升后多头能量消耗较大，明日大概率进入震荡整固。支撑位：4000点(整数关口)、3970点(5日线)。压力位：4050点、4100点。"
    },
    {
        "name": "CPO/光模块",
        "direction": "看涨",
        "confidence": 70,
        "reason": "今日午后集体爆发，光迅科技、东山精密、长电科技涨停，中际旭创成交416亿居A股首位。CPO量产节奏虽有分歧(2026下半年vs 2028年)，但高速光模块需求增长确定性强，龙头估值仍有优势。关注天孚通信、中际旭创、新易盛等龙头的持续性。"
    },
    {
        "name": "券商板块",
        "direction": "震荡偏强",
        "confidence": 60,
        "reason": "华安证券涨停、招商证券涨约7%，券商板块今日表现活跃。成交量放大至2.93万亿对券商经纪业务是直接利好。但券商板块历来持续性较差，更多是情绪催化剂角色。若明日两市成交维持在2.5万亿以上，券商仍有脉冲机会，但不建议追高。"
    },
    {
        "name": "锂电/光伏新能源",
        "direction": "看跌",
        "confidence": 72,
        "reason": "今日市场风格极端切换，资金从新能源大幅流出转向半导体。天华新能跌近15%、融捷股份连跌2个跌停，固德威机构净卖10.56亿。虽然部分公司业绩亮眼，但股价反而下跌(利好出尽)，说明机构在系统性减仓新能源板块。建议坚决回避，不要抄底。"
    },
])

# 11. 明日操作策略
trading_plan = '''
<div style="font-size: 14px; color: #e2e8f0; line-height: 1.9;">
    <p style="margin: 0 0 12px 0;"><strong style="color: #f59e0b;">📈 大盘判断：</strong>
    今日深V反转放量大涨，科创50创历史第四大单日涨幅，市场情绪快速回暖。但单日8%级别的暴涨历史上多为脉冲行情，持续性存疑。
    明日大概率进入<strong>分化震荡</strong>格局：前排半导体龙头继续强势，后排跟风股回落，指数在4000-4080点区间震荡。
    操作上<strong>不宜追高</strong>，应利用反弹优化持仓结构，聚焦核心主线龙头。</p>
    
    <p style="margin: 0 0 12px 0;"><strong style="color: #f59e0b;">💰 仓位建议：</strong>
    总体仓位<strong>从3成提升至5-6成</strong>，加仓方向为半导体设备/材料/封测龙头。
    但不建议满仓，保留3-4成现金应对波动。
    持仓结构：<strong>60%半导体核心主线 + 20%液冷/算力 + 20%现金</strong></p>
    
    <p style="margin: 0 0 12px 0;"><strong style="color: #ef4444;">🔴 持仓操作计划(按优先级排序)：</strong></p>
    
    <p style="margin: 0 0 8px 0;"><strong>1. *ST建艺(002789)：明日集合竞价清仓</strong><br/>
    当前价10.38元，浮亏-22.8%。退市风险高悬，任何反弹都是离场机会。<br/>
    操作：明日9:25集合竞价直接挂单卖出全部仓位；若开盘后有反弹至10.8-11元机会更是绝佳窗口，必须全部清仓。<br/>
    <strong>核心原则：留得青山在，不怕没柴烧。</strong></p>
    
    <p style="margin: 0 0 8px 0;"><strong>2. 雅克科技(002409)：涨停后分批止盈</strong><br/>
    当前价209元(涨停)，浮盈+92.1%，创历史新高。<br/>
    操作：明日若高开215-220元区间，<strong>减仓1/3</strong>锁定利润；若继续冲高至230-240元，<strong>再减1/3</strong>；保留1/3底仓博弈中报行情。<br/>
    止损线：收盘跌破200元减仓一半，跌破180元止盈离场。</p>
    
    <p style="margin: 0 0 8px 0;"><strong>3. 铜冠铜箔(301217)：反弹减仓锁定利润</strong><br/>
    当前价139.68元，浮盈+60.3%。短期均线仍处空头排列，反弹性质待确认。<br/>
    操作：140-145元区间<strong>减仓至1/3底仓</strong>以下(卖出约2/3)锁定利润；若放量突破145元可再持有1-2日观察。<br/>
    止损线：回落跌破135元减仓一半，跌破130元清仓止盈。</p>
    
    <p style="margin: 0 0 12px 0;"><strong>4. 英维克(002837)：趁反弹坚决减仓</strong><br/>
    当前价75.87元，浮亏-27.2%，深度套牢。今日反弹属于板块带动，非个股基本面改善。<br/>
    操作：75-78元区间<strong>减仓至1/3底仓</strong>以下；反弹至80元以上考虑全部清仓。<br/>
    <strong>严禁补仓</strong>，中期下跌趋势未改，反弹结束大概率继续探底。<br/>
    止损线：跌破72元减仓一半，跌破68元无条件清仓。</p>
    
    <p style="margin: 0 0 12px 0;"><strong style="color: #10b981;">🟢 新开仓方向(低吸不追高)：</strong></p>
    <p style="margin: 0 0 8px 0;"><strong>首选：中芯国际(688981)——晶圆代工总龙头</strong><br/>
    买入区间：回调至95-100元(5日线附近)分批建仓，建议仓位15%<br/>
    目标价：120元(短期)、140元(中期) | 止损：跌破90元</p>
    
    <p style="margin: 0 0 8px 0;"><strong>次选：通富微电(002156)——先进封装龙头</strong><br/>
    买入区间：回调至68-70元(涨停板中位附近)轻仓试错，建议仓位10%<br/>
    目标价：85-90元 | 止损：跌破65元</p>
    
    <p style="margin: 0;"><strong>备选：浪潮信息(000977)——AI服务器龙头</strong><br/>
    买入区间：回调至75-78元(5日线)建仓，建议仓位10%<br/>
    目标价：95-100元 | 止损：跌破70元</p>
</div>
'''
gen.add_trading_plan(plan=trading_plan)

# 12. 风险提示
gen.add_risk_warning(risks=[
    "半导体板块单日暴涨后获利盘丰厚，明日可能出现大幅分化和回调，追高风险大",
    "市场风格极端切换，新能源等板块持续承压，持仓结构不合理可能赚指数不赚钱",
    "长鑫科技上市后存在利好兑现风险，参考2020年中芯国际上市后半导体板块走势",
    "量能放大至2.93万亿若不可持续(跌破2.5万亿)，则反弹高度受限",
    "外部不确定性：美联储政策、地缘政治、海外市场波动可能影响A股情绪",
])

# 生成并发布
result = gen.publish(
    title="盘后速递",
    report_type="aftermarket",
    excerpt="科创50暴涨8.41%创历史第四大涨幅，半导体产业链全线爆发。雅克科技涨停创历史新高，4只持仓股深度诊断+具体买卖点位。龙虎榜机构重仓封测龙头，明日操作策略已更新。",
    auto_deploy=True
)

print("发布结果：", result)
print("报告生成完成！")
