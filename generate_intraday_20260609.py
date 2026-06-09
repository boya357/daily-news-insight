#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
2026年6月9日 盘中快报生成脚本
"""
import sys
import os

sys.path.insert(0, '/root/daily-news-insight')

from v3.generators.intraday import IntradayGenerator

def generate_intraday_report():
    # 初始化生成器
    gen = IntradayGenerator(
        date_str="2026年6月9日",
        subtitle="2026年6月9日 · 午盘速递"
    )
    
    # 1. 市场概览
    indices = [
        {"name": "上证指数", "value": "3,979.68", "change": "+0.51%", "up": True, "icon": "trending_up"},
        {"name": "深证成指", "value": "15,007.11", "change": "+1.25%", "up": True, "icon": "trending_up"},
        {"name": "创业板指", "value": "3,884.54", "change": "+1.91%", "up": True, "icon": "trending_up"},
        {"name": "科创综指", "value": "2,008.41", "change": "+2.72%", "up": True, "icon": "trending_up"},
    ]
    gen.add_market_overview(indices, market_status="震荡上涨")
    
    # 2. 热点板块解析
    hot_topics = [
        {
            "tag": "半导体",
            "title": "半导体产业链全线爆发，设备材料领涨",
            "content": "受海外芯片股反弹及国产替代加速双重催化，半导体产业链今日早盘全线走强。电子化学品、半导体设备、PCB、硅片等细分方向领涨市场。北方华创等龙头标的获主力资金大举流入，板块内多只个股涨幅超5%。内资晶圆厂资本开支持续扩张，长江存储与长鑫存储合计新增10-12万片每月产能，国产设备厂商进入量价齐升景气周期。",
            "hot": True,
            "stocks": ["北方华创", "中微公司", "沪硅产业", "铜冠铜箔"]
        },
        {
            "tag": "光通信",
            "title": "光纤光缆板块强势，AI算力基础设施需求强劲",
            "content": "光通信板块今日表现亮眼，光纤光缆方向尤为突出。运营商近期启动2026年至2027年5G-A基站设备集采，总规模超过60万站，预计投资金额超800亿元，对通信设备产业链构成实质性业绩支撑。AI算力需求持续爆发带动高速光模块、光纤光缆需求增长，行业景气度持续上行。",
            "hot": True,
            "stocks": ["太辰光", "中际旭创", "亨通光电", "长飞光纤"]
        },
        {
            "tag": "AI应用",
            "title": "AI应用端持续活跃，应用落地加速推进",
            "content": "AI应用板块早盘延续活跃态势，短剧、具身智能、AI金融等细分方向表现突出。市场风格正从硬件炒作为主向应用落地扩散，AI应用端公司业绩逐步兑现，估值具备性价比。随着大模型技术迭代加速，AI应用场景不断拓展，行业正从概念炒作迈向业绩验证期。",
            "hot": False,
            "stocks": ["昆仑万维", "万兴科技", "科大讯飞", "蓝色光标"]
        },
        {
            "tag": "储能",
            "title": "储能板块异动，宁德时代长单锁定需求",
            "content": "储能板块早盘异动走强，永太科技子公司与宁德时代签订长期电解液供货协议，约定2026年至2028年期间宁德时代预计合计采购电解液约47万吨。大规模长协订单直接锁定未来三年核心电池材料需求，强化市场对锂电池产业链需求确定性和行业景气度持续上行的预期。",
            "hot": False,
            "stocks": ["宁德时代", "亿纬锂能", "英维克", "科华数据"]
        }
    ]
    gen.add_hot_topics(hot_topics)
    
    # 3. 领跌板块警示
    decline_sectors = [
        {
            "name": "煤炭开采加工",
            "change": "-3.2%",
            "reason": "高位红利资产遭获利了结，资金转向成长赛道"
        },
        {
            "name": "油气开采及服务",
            "change": "-2.8%",
            "reason": "国际油价波动叠加市场风格切换，防御板块承压"
        },
        {
            "name": "白酒",
            "change": "-1.5%",
            "reason": "消费复苏节奏放缓，资金避高就低流出消费板块"
        }
    ]
    gen.add_decline_sectors(decline_sectors)
    
    # 4. 持仓股跟踪
    holdings = [
        {
            "name": "英维克",
            "code": "002837",
            "price": "66.46",
            "change": "+4.86%",
            "up": True,
            "comment": "液冷温控龙头，受益于AI算力需求爆发。今日随储能及算力硬件板块同步上涨，主力资金净流入超2亿元，技术形态企稳回升。"
        },
        {
            "name": "铜冠铜箔",
            "code": "301217",
            "price": "121.77",
            "change": "+7.67%",
            "up": True,
            "comment": "PCB铜箔龙头，深度受益于半导体产业链景气度回升及AI服务器需求增长。今日放量大涨，突破前期平台，主力资金流入明显。"
        },
        {
            "name": "*ST建艺",
            "code": "002789",
            "price": "13.33",
            "change": "+2.38%",
            "up": True,
            "comment": "横琴新区+建筑节能+创投概念，摘帽审核进行中。今日跟随市场反弹，股价位于支撑位上方，关注后续摘帽进展。"
        }
    ]
    gen.add_holdings_tracking(holdings)
    
    # 5. 午盘操作策略
    strategy = """
    <strong>一、市场判断</strong><br>
    今日A股三大指数集体高开高走，创业板指领涨，市场呈现普涨格局。科技成长方向全面回暖，半导体产业链成为最强主线，资金从防御板块向成长赛道切换迹象明显。半日成交额约1.68万亿元，量能维持活跃水平，市场情绪较昨日显著修复。<br><br>
    
    <strong>二、操作策略</strong><br>
    1. <strong>主线把握</strong>：聚焦科技成长主线，重点关注半导体设备材料、AI算力基础设施、光通信等高景气方向，逢低布局核心标的。<br>
    2. <strong>持仓策略</strong>：英维克、铜冠铜箔等持仓股跟随板块上涨，可继续持有，关注午后量能持续性；*ST建艺关注摘帽进展，谨慎操作。<br>
    3. <strong>风险控制</strong>：外围市场波动仍存，中东局势不确定性犹存，需警惕午后获利回吐压力，控制仓位避免追高。<br>
    4. <strong>关注方向</strong>：午后重点观察半导体板块持续性、成交额能否有效放大，以及北向资金流向变化。
    """
    gen.add_trading_strategy(strategy)
    
    # 6. 风险提示
    risks = [
        "外围市场波动风险：美股科技股波动可能传导至A股",
        "地缘政治风险：中东局势不确定性仍存，可能影响市场情绪",
        "板块轮动加速风险：市场风格切换较快，追高风险较大",
        "业绩不及预期风险：部分科技股估值偏高，需警惕业绩验证风险"
    ]
    gen.add_risk_warning(risks)
    
    # 7. 市场逻辑总结
    summary = """
    今日市场核心逻辑：<strong>科技成长主导，板块轮动扩散</strong>。经历昨日调整后，市场情绪快速修复，资金从高位红利板块流向超跌成长方向，半导体产业链成为市场最强主线。政策层面，5G-A集采落地、晶圆厂扩产加速等产业利好不断释放，支撑科技板块景气度。
    整体来看，市场仍处于结构性行情中，板块轮动特征明显。建议聚焦产业趋势明确的硬科技方向，把握高低切换节奏，避免追高，逢低布局具备业绩支撑的优质标的。
    """
    gen.add_summary(summary)
    
    # 生成并保存
    output_path = "/root/daily-news-insight/docs/intraday/20260609_盘中快报.html"
    html = gen.generate()
    gen.save(output_path)
    
    print(f"盘中快报已生成：{output_path}")
    print(f"文件大小：{os.path.getsize(output_path)} 字节")
    
    return output_path

if __name__ == "__main__":
    generate_intraday_report()
