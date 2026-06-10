#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
六氟化钨（WF6）产业链深度研究报告生成器
"""

import sys
import os
sys.path.insert(0, '/root/daily-news-insight/v3')

from generators.deep_dive import DeepDiveGenerator
from components.data import StatCard, CompareTable, GaugeChart, Tabs
from components.special import Timeline

def generate_report():
    gen = DeepDiveGenerator(
        title="六氟化钨（WF6）产业链深度研究",
        subtitle="AI算力革命驱动的半导体核心材料，国产替代黄金窗口期已至"
    )
    
    # 1. 核心观点摘要
    gen.add_summary(
        core_view="六氟化钨作为半导体钨沉积工艺的唯一前驱体材料，正迎来AI算力革命驱动的超级景气周期。日本产能断供导致全球供需缺口急剧扩大，国内龙头企业凭借资源优势+技术突破+客户认证三重壁垒，迎来量价齐升的历史性机遇。",
        bull_points=[
            "供需缺口持续扩大：日本2000吨产能断供，2026年缺口约11%，2027年扩大至34%，产品价格2个月暴涨190%",
            "需求爆发式增长：AI+HBM+3D NAND三重驱动，单片晶圆用量从0.8kg增至2.5kg+，行业年增速15%-20%",
            "国产替代加速：中国掌控全球80%钨资源，国内企业技术突破6N/7N级产品，切入全球头部晶圆厂供应链",
            "盈利弹性巨大：钨粉成本占比60-70%，国内企业具备资源自给优势，价格上涨直接转化为利润增厚",
            "政策强力支持：钨出口管制+电子特气国产化政策双轮驱动，行业进入高景气长周期"
        ],
        bear_points=[
            "估值泡沫风险：板块短期涨幅巨大，中船特气PE超380倍，存在情绪过热回调风险",
            "订单落地不及预期：日本断供后客户洽谈增多，但实质性长单签署仍需时间验证",
            "技术替代隐忧：钼金属、WOF4等替代技术长期存在，虽距量产仍需5-8年但需持续跟踪",
            "产能扩张超预期：多氟多等新玩家加速入局，2027年行业新增产能可能超预期",
            "半导体周期波动：若AI需求降温或存储扩产放缓，行业景气度可能快速回落"
        ]
    )
    
    # 2. 行业景气度仪表盘
    gen.add_gauge_chart(
        title="行业景气度指数",
        value=92,
        max_value=100,
        label="极度景气",
        color="#f97316"
    )
    
    stat_cards = [
        StatCard(title="价格涨幅(2月)", value="190%", subtitle="6N级产品均价", trend="+190%", trend_up=True),
        StatCard(title="2026年供需缺口", value="11%", subtitle="下半年扩大至20%+", trend="扩大", trend_up=True),
        StatCard(title="产能利用率", value="90%+", subtitle="头部企业满产状态", trend="高位", trend_up=True),
        StatCard(title="出口均价涨幅", value="117.9%", subtitle="2026年1-4月累计", trend="+117.9%", trend_up=True),
    ]
    gen.add_stat_cards(stat_cards, cols=4)
    
    # 3. 产业链全景
    upstream = """
    <div style="padding:10px 0;">
        <h4 style="color:#1a73e8;margin-bottom:15px;">🔬 上游：原材料供应</h4>
        <div style="display:flex;flex-wrap:wrap;gap:15px;">
            <div style="flex:1;min-width:200px;background:#f0f7ff;padding:15px;border-radius:8px;">
                <h5 style="margin:0 0 10px 0;color:#1a73e8;">钨矿 / 钨粉</h5>
                <p style="margin:5px 0;font-size:14px;">• 占生产成本60%-70%</p>
                <p style="margin:5px 0;font-size:14px;">• 中国占全球储量80%+</p>
                <p style="margin:5px 0;font-size:14px;">• 6N级高纯钨粉已国产化</p>
                <p style="margin:5px 0;font-size:14px;color:#e74c3c;">• 出口管制持续收紧</p>
            </div>
            <div style="flex:1;min-width:200px;background:#f0fff4;padding:15px;border-radius:8px;">
                <h5 style="margin:0 0 10px 0;color:#34a853;">氟气 / 氢氟酸</h5>
                <p style="margin:5px 0;font-size:14px;">• 合成反应核心原料</p>
                <p style="margin:5px 0;font-size:14px;">• 国内氟化工产能充足</p>
                <p style="margin:5px 0;font-size:14px;">• 中船特气等实现自给</p>
                <p style="margin:5px 0;font-size:14px;color:#e74c3c;">• 环保要求趋严</p>
            </div>
        </div>
        <div style="margin-top:15px;font-size:13px;color:#666;">
            <strong>代表企业：</strong>厦门钨业、中钨高新、章源钨业、巨化股份
        </div>
    </div>
    """
    
    midstream = """
    <div style="padding:10px 0;">
        <h4 style="color:#f39c12;margin-bottom:15px;">⚗️ 中游：制备与纯化</h4>
        <div style="display:flex;flex-wrap:wrap;gap:15px;">
            <div style="flex:1;min-width:200px;background:#fff8f0;padding:15px;border-radius:8px;">
                <h5 style="margin:0 0 10px 0;color:#f39c12;">合成工艺</h5>
                <p style="margin:5px 0;font-size:14px;">• 钨粉直接氟化法（主流）</p>
                <p style="margin:5px 0;font-size:14px;">• 三氟化氮间接合成法</p>
                <p style="margin:5px 0;font-size:14px;">• 反应温度300-400℃</p>
                <p style="margin:5px 0;font-size:14px;">• 流化床反应器为主</p>
            </div>
            <div style="flex:1;min-width:200px;background:#f5f0ff;padding:15px;border-radius:8px;">
                <h5 style="margin:0 0 10px 0;color:#9c27b0;">纯化技术</h5>
                <p style="margin:5px 0;font-size:14px;">• 精馏提纯（去除重组分）</p>
                <p style="margin:5px 0;font-size:14px;">• 吸附除杂（去除轻组分）</p>
                <p style="margin:5px 0;font-size:14px;">• 金属杂质控制ppb级</p>
                <p style="margin:5px 0;font-size:14px;">• 7N级为全球最高水平</p>
            </div>
        </div>
        <div style="margin-top:15px;font-size:13px;color:#666;">
            <strong>代表企业：</strong>中船特气、昊华科技、中巨芯、华特气体、南大光电
        </div>
    </div>
    """
    
    downstream = """
    <div style="padding:10px 0;">
        <h4 style="color:#2e7d32;margin-bottom:15px;">💡 下游：应用领域</h4>
        <div style="display:flex;flex-wrap:wrap;gap:15px;">
            <div style="flex:1.4;min-width:200px;background:#e8f5e9;padding:15px;border-radius:8px;">
                <h5 style="margin:0 0 10px 0;color:#2e7d32;">半导体 (70%)</h5>
                <p style="margin:5px 0;font-size:14px;">• 3D NAND闪存：钨塞/互连层</p>
                <p style="margin:5px 0;font-size:14px;">• HBM高带宽存储：TSV填充</p>
                <p style="margin:5px 0;font-size:14px;">• 先进逻辑芯片：接触孔/通孔</p>
                <p style="margin:5px 0;font-size:14px;">• 要求纯度6N以上，先进制程需7N</p>
            </div>
            <div style="flex:1;min-width:150px;background:#fff3e0;padding:15px;border-radius:8px;">
                <h5 style="margin:0 0 10px 0;color:#e65100;">光伏 (10%)</h5>
                <p style="margin:5px 0;font-size:14px;">• 薄膜太阳能电池</p>
                <p style="margin:5px 0;font-size:14px;">• 电极材料沉积</p>
                <p style="margin:5px 0;font-size:14px;">• 纯度要求5N级</p>
            </div>
            <div style="flex:1;min-width:150px;background:#e3f2fd;padding:15px;border-radius:8px;">
                <h5 style="margin:0 0 10px 0;color:#1565c0;">显示面板 (8%)</h5>
                <p style="margin:5px 0;font-size:14px;">• OLED/TFT导电层</p>
                <p style="margin:5px 0;font-size:14px;">• 金属布线沉积</p>
                <p style="margin:5px 0;font-size:14px;">• 纯度要求5N-6N</p>
            </div>
        </div>
        <div style="margin-top:15px;font-size:13px;color:#666;">
            <strong>代表客户：</strong>台积电、三星、SK海力士、美光、中芯国际、长江存储
        </div>
    </div>
    """
    
    chain_html = f"""
    <div style="display:flex;flex-direction:column;gap:10px;">
        {upstream}
        <div style="text-align:center;font-size:28px;color:#666;">⬇️</div>
        {midstream}
        <div style="text-align:center;font-size:28px;color:#666;">⬇️</div>
        {downstream}
    </div>
    """
    
    gen.add_analysis_section(title="产业链全景梳理", content=chain_html, icon="chain")
    
    # 4. 市场空间与竞争格局
    market_cards = [
        StatCard(title="2026全球市场规模", value="7.4亿美元", subtitle="约53亿人民币", trend="+19% YoY", trend_up=True),
        StatCard(title="2035年市场规模", value="34.5亿美元", subtitle="CAGR约19%", trend="快速增长", trend_up=True),
        StatCard(title="2026全球需求量", value="~11000吨", subtitle="同比+22%", trend="加速增长", trend_up=True),
        StatCard(title="中国产能占比", value="50%+", subtitle="全球第一", trend="持续提升", trend_up=True),
    ]
    gen.add_stat_cards(market_cards, cols=4)
    
    comp_headers = ["企业名称", "国家/地区", "产能(吨/年)", "技术水平", "主要客户", "市场地位"]
    comp_rows = [
        ["SK Specialty", "韩国", "约2500", "6N级主流", "三星、SK海力士", "全球前二"],
        ["中船特气", "中国", "2000-2230", "6N为主，7N量产", "台积电、中芯、长江存储", "全球第一阵营"],
        ["关东电化", "日本", "1400", "6N级", "台积电、日本芯片厂", "产能受限（断供）"],
        ["中央硝子", "日本", "600", "6N级", "日本、韩国芯片厂", "产能受限（断供）"],
        ["昊华科技", "中国", "600-700", "6N级", "国内外存储厂", "国内第二"],
        ["中巨芯", "中国", "600", "5N5", "中芯、华虹", "国内第三阵营"],
        ["南大光电", "中国", "500", "5N-6N", "国内晶圆厂", "国内第三阵营"],
    ]
    gen.add_competitive_analysis(headers=comp_headers, rows=comp_rows, highlight_rows=[1, 4])
    
    # 5. 技术壁垒分析
    tech_tab1 = """
    <div style="padding:15px 0;">
        <p>六氟化钨纯度直接影响芯片良率，是核心技术壁垒：</p>
        <ul style="line-height:2;">
            <li><strong>6N级（99.9999%）</strong>：主流先进制程要求，金属杂质总含量≤100ppb</li>
            <li><strong>7N级（99.99999%）</strong>：3nm及以下制程要求，金属杂质总含量≤10ppb</li>
            <li>需控制Fe、Ni、Cr、Na、K等20余种金属杂质含量</li>
            <li>水分、氧含量需控制在ppm级甚至ppb级</li>
            <li>颗粒度控制要求严格，避免划伤晶圆表面</li>
        </ul>
        <p style="color:#e74c3c;font-weight:bold;margin-top:15px;">
            目前仅中船特气等极少数国内企业实现7N级产品量产，技术差距5-8年。
        </p>
    </div>
    """
    
    tech_tab2 = """
    <div style="padding:15px 0;">
        <p>半导体材料客户认证周期长、门槛高：</p>
        <ul style="line-height:2;">
            <li><strong>认证周期：</strong>通常需1-3年，含样品测试、小批量验证、批量供货等阶段</li>
            <li><strong>认证标准：</strong>需通过SEMI国际标准、客户工厂审核、质量体系认证</li>
            <li><strong>替换成本：</strong>一旦验证通过并稳定供货，晶圆厂不会轻易更换供应商</li>
            <li><strong>资质要求：</strong>需具备ISO9001、ISO14001、ISO45001等多重认证</li>
        </ul>
        <p style="color:#2e7d32;font-weight:bold;margin-top:15px;">
            头部企业已完成全球主要晶圆厂认证，新进入者难以短期突破。
        </p>
    </div>
    """
    
    tech_tab3 = """
    <div style="padding:15px 0;">
        <p>生产工艺复杂，环保安全要求极高：</p>
        <ul style="line-height:2;">
            <li><strong>工艺复杂：</strong>氟化反应需高温高压，对反应器材质、控制系统要求极高</li>
            <li><strong>安全风险：</strong>WF6具强腐蚀性、剧毒性，遇水剧烈反应生成HF</li>
            <li><strong>设备要求：</strong>需使用蒙乃尔合金、哈氏合金等特种材质设备</li>
            <li><strong>环保审批：</strong>环评、安评审批严格，新建产线周期长达18个月以上</li>
            <li><strong>三废处理：</strong>含氟废气、废水处理成本高，技术难度大</li>
        </ul>
        <p style="color:#f39c12;font-weight:bold;margin-top:15px;">
            高安全环保要求抬高行业准入门槛，小企业难以合规生产。
        </p>
    </div>
    """
    
    tech_tab4 = """
    <div style="padding:15px 0;">
        <p>钨资源战略属性凸显，原料供应决定产能上限：</p>
        <ul style="line-height:2;">
            <li><strong>资源垄断：</strong>中国占全球钨储量80%以上，产量占比更高</li>
            <li><strong>成本占比：</strong>高纯钨粉占六氟化钨生产成本的60%-70%</li>
            <li><strong>出口管制：</strong>中国逐步收紧钨产品出口，海外厂商原料获取困难</li>
            <li><strong>一体化优势：</strong>具备钨矿-钨粉-WF6全产业链的企业成本优势显著</li>
        </ul>
        <p style="color:#9c27b0;font-weight:bold;margin-top:15px;">
            中国企业凭借资源禀赋建立天然竞争优势，日本企业已受制于人。
        </p>
    </div>
    """
    
    gen.add_tabs_section(
        title="技术壁垒分析",
        tabs=[("纯度控制壁垒", tech_tab1), ("客户认证壁垒", tech_tab2), 
              ("工艺与环保壁垒", tech_tab3), ("原料资源壁垒", tech_tab4)],
        icon="shield"
    )
    
    # 6. 核心标的对比
    targets_headers = ["公司", "代码", "WF6产能", "纯度等级", "营收占比", "毛利率", "2026Q1增速", "核心优势"]
    targets_rows = [
        ["中船特气", "688146", "2000-2230吨", "6N/7N量产", "估算~25%", "30.2%", "+16.86%", "全球产能第一，技术领先，客户最全"],
        ["昊华科技", "600378", "600-700吨", "6N级", "约7%", "~25%", "+66.73%", "央企背景，氟化工全产业链，成本优势"],
        ["中巨芯", "688549", "600吨", "5N5", "约15%", "15.71%", "扭亏", "巨化+大基金背景，湿电子化学品协同"],
        ["华特气体", "688268", "200吨", "6N(少量7N)", "约10%", "32%", "+30%", "光刻气龙头，ASML认证，客户优质"],
        ["南大光电", "300346", "500吨", "5N-6N", "特气整体59%", "-", "+30%+", "前驱体+特气双轮，乌兰察布基地放量"],
        ["和远气体", "002971", "试生产", "-", "0%", "-", "-", "潜江产业园布局，潜在弹性大"],
    ]
    table_html = CompareTable(headers=targets_headers, rows=targets_rows, highlight_rows=[0, 1]).render()
    gen.add_analysis_section(title="核心标的对比分析", content=table_html, icon="chart")
    
    # 7. 三梯队标的分类
    tiers_html = """
    <div style="padding:10px 0;">
        <h4 style="color:#667eea;margin-bottom:15px;">🥇 第一梯队：核心龙头（确定性最强）</h4>
        <div style="display:flex;flex-wrap:wrap;gap:15px;margin-bottom:25px;">
            <div style="flex:1;min-width:250px;background:linear-gradient(135deg,#667eea 0%,#764ba2 100%);color:white;padding:20px;border-radius:12px;">
                <h3 style="margin:0 0 10px 0;">中船特气 (688146)</h3>
                <p style="margin:5px 0;font-size:14px;">🏆 全球六氟化钨龙头，产能2000-2230吨/年</p>
                <p style="margin:5px 0;font-size:14px;">🔬 国内唯一7N级量产企业，技术壁垒最高</p>
                <p style="margin:5px 0;font-size:14px;">🌍 客户覆盖台积电、三星、SK海力士等全球头部</p>
                <p style="margin:5px 0;font-size:14px;">📈 2027年扩至3000吨，量价齐升弹性最大</p>
                <p style="margin:5px 0;font-size:14px;">⚠️ 估值偏高，PE超380倍</p>
                <div style="margin-top:10px;padding-top:10px;border-top:1px solid rgba(255,255,255,0.3);">
                    <span style="font-weight:bold;">综合评分：95分</span>
                </div>
            </div>
            <div style="flex:1;min-width:250px;background:linear-gradient(135deg,#f093fb 0%,#f5576c 100%);color:white;padding:20px;border-radius:12px;">
                <h3 style="margin:0 0 10px 0;">昊华科技 (600378)</h3>
                <p style="margin:5px 0;font-size:14px;">🏛️ 央企背景（中国中化），资源整合能力强</p>
                <p style="margin:5px 0;font-size:14px;">⚗️ 产能600-700吨/年，国内第二</p>
                <p style="margin:5px 0;font-size:14px;">🔗 氟化工全产业链，成本控制能力突出</p>
                <p style="margin:5px 0;font-size:14px;">💰 估值相对合理，安全边际较高</p>
                <p style="margin:5px 0;font-size:14px;">⚠️ WF6业务占比不高，弹性略弱</p>
                <div style="margin-top:10px;padding-top:10px;border-top:1px solid rgba(255,255,255,0.3);">
                    <span style="font-weight:bold;">综合评分：82分</span>
                </div>
            </div>
        </div>
        
        <h4 style="color:#f39c12;margin-bottom:15px;">🥈 第二梯队：弹性标的（成长空间大）</h4>
        <div style="display:flex;flex-wrap:wrap;gap:15px;margin-bottom:25px;">
            <div style="flex:1;min-width:200px;background:#fff3e0;padding:15px;border-radius:8px;">
                <h5 style="margin:0 0 8px 0;color:#e65100;">中巨芯 (688549)</h5>
                <p style="margin:3px 0;font-size:13px;">• 产能600吨/年，5N5级</p>
                <p style="margin:3px 0;font-size:13px;">• 巨化股份+大基金合资</p>
                <p style="margin:3px 0;font-size:13px;">• 湿电子化学品协同效应</p>
                <p style="margin:3px 0;font-size:13px;">• 2026Q1扭亏，拐点显现</p>
                <p style="margin-top:8px;font-weight:bold;color:#e65100;">评分：72分</p>
            </div>
            <div style="flex:1;min-width:200px;background:#e8f5e9;padding:15px;border-radius:8px;">
                <h5 style="margin:0 0 8px 0;color:#2e7d32;">华特气体 (688268)</h5>
                <p style="margin:3px 0;font-size:13px;">• 产能200吨/年，6N级</p>
                <p style="margin:3px 0;font-size:13px;">• 国内唯一ASML认证</p>
                <p style="margin:3px 0;font-size:13px;">• 光刻气龙头，品类协同</p>
                <p style="margin:3px 0;font-size:13px;">• 毛利率32%，盈利能力强</p>
                <p style="margin-top:8px;font-weight:bold;color:#2e7d32;">评分：70分</p>
            </div>
            <div style="flex:1;min-width:200px;background:#e3f2fd;padding:15px;border-radius:8px;">
                <h5 style="margin:0 0 8px 0;color:#1565c0;">南大光电 (300346)</h5>
                <p style="margin:3px 0;font-size:13px;">• 产能500吨/年，5N-6N</p>
                <p style="margin:3px 0;font-size:13px;">• 前驱体+特气双主线</p>
                <p style="margin:3px 0;font-size:13px;">• 乌兰察布基地产能释放</p>
                <p style="margin:3px 0;font-size:13px;">• 7N级产品研发中</p>
                <p style="margin-top:8px;font-weight:bold;color:#1565c0;">评分：68分</p>
            </div>
        </div>
        
        <h4 style="color:#9e9e9e;margin-bottom:15px;">🥉 第三梯队：概念股（上游原料/布局中）</h4>
        <div style="display:flex;flex-wrap:wrap;gap:15px;">
            <div style="flex:1;min-width:180px;background:#fce4ec;padding:15px;border-radius:8px;">
                <h5 style="margin:0 0 8px 0;color:#c2185b;">厦门钨业 (600549)</h5>
                <p style="margin:3px 0;font-size:13px;">• 全球钨资源龙头</p>
                <p style="margin:3px 0;font-size:13px;">• 年产能1.2万吨钨精矿</p>
                <p style="margin:3px 0;font-size:13px;">• 6N高纯钨粉已验证</p>
                <p style="margin:3px 0;font-size:13px;">• 上游原料核心受益</p>
            </div>
            <div style="flex:1;min-width:180px;background:#f3e5f5;padding:15px;border-radius:8px;">
                <h5 style="margin:0 0 8px 0;color:#7b1fa2;">中钨高新 (000657)</h5>
                <p style="margin:3px 0;font-size:13px;">• 五矿集团钨业平台</p>
                <p style="margin:3px 0;font-size:13px;">• 柿竹园世界级钨矿</p>
                <p style="margin:3px 0;font-size:13px;">• 资源自给率70%</p>
                <p style="margin:3px 0;font-size:13px;">• 钨粉产能全球领先</p>
            </div>
            <div style="flex:1;min-width:180px;background:#fffde7;padding:15px;border-radius:8px;">
                <h5 style="margin:0 0 8px 0;color:#f57f17;">和远气体 (002971)</h5>
                <p style="margin:3px 0;font-size:13px;">• 500吨产能建设中</p>
                <p style="margin:3px 0;font-size:13px;">• 潜江产业园布局</p>
                <p style="margin:3px 0;font-size:13px;">• 客户认证推进中</p>
                <p style="margin:3px 0;font-size:13px;">• 量产时间不确定</p>
            </div>
            <div style="flex:1;min-width:180px;background:#e0f7fa;padding:15px;border-radius:8px;">
                <h5 style="margin:0 0 8px 0;color:#00838f;">巨化股份 (600160)</h5>
                <p style="margin:3px 0;font-size:13px;">• 氟化工绝对龙头</p>
                <p style="margin:3px 0;font-size:13px;">• 中巨芯第一大股东</p>
                <p style="margin:3px 0;font-size:13px;">• 原料自给能力强</p>
                <p style="margin:3px 0;font-size:13px;">• 间接受益WF6景气</p>
            </div>
        </div>
    </div>
    """
    gen.add_analysis_section(title="投资标的三梯队划分", content=tiers_html, icon="trophy")
    
    # 8. 催化因素时间轴
    timeline_items = [
        {"time": "2025年2月", "title": "出口管制政策出台", "content": "中国将钨相关物项纳入出口管制，全年钨出口量同比下降27.5%，行业供给格局开始重塑。", "type": "warning"},
        {"time": "2025年10月", "title": "日韩涨价通知", "content": "韩国SK Specialty、日本关东电化等通知客户2026年六氟化钨价格上调70%-90%，开启涨价周期。", "type": "warning"},
        {"time": "2026年1月", "title": "对日出口管制升级", "content": "商务部加强对日本两用物项出口管制，碳化钨、高纯钨粉、六氟化钨等核心材料列入严管清单。", "type": "danger"},
        {"time": "2026年4月", "title": "日本厂商断供预警", "content": "日本关东电化、中央硝子通知三星等客户，钨原料库存仅可维持至5-6月，下半年供应无法保障。", "type": "danger"},
        {"time": "2026年5月", "title": "矿产资源法修订", "content": "《中华人民共和国矿产资源法实施条例》明确对钨实行刚性年度开采总量控制，战略资源属性强化。", "type": "primary"},
        {"time": "2026年6月", "title": "价格暴涨190%", "content": "6N级六氟化钨报价达220-300万元/吨，较4月初涨幅超190%，出口均价翻倍，行业进入高景气。", "type": "success"},
        {"time": "2026年H2", "title": "国产替代加速", "content": "预计海外晶圆厂加速导入国内供应商，中船特气、昊华科技等有望获得更多海外订单，出口占比提升。", "type": "info"},
        {"time": "2027年", "title": "产能集中释放", "content": "中船特气新增1000吨产能投产，多氟多等新玩家产能释放，总产能预计增长30%+。", "type": "info"},
        {"time": "2028年+", "title": "长周期成长", "content": "AI算力持续增长、3D NAND层数突破、HBM需求爆发，驱动六氟化钨需求持续增长，国产替代深化。", "type": "success"},
    ]
    gen.add_timeline(items=timeline_items, title="行业催化因素时间线")
    
    # 9. 投资逻辑
    logic_html = """
    <div style="padding:10px 0;">
        <div style="display:flex;flex-wrap:wrap;gap:15px;">
            <div style="flex:1;min-width:200px;">
                <h4 style="color:#e74c3c;margin-bottom:10px;">📈 需求端：AI革命驱动超级周期</h4>
                <ul style="font-size:14px;line-height:1.8;">
                    <li>AI大模型训练推动HBM需求爆发，单颗芯片WF6用量翻倍</li>
                    <li>3D NAND向300层+演进，单片晶圆用量从0.8kg增至2.5kg</li>
                    <li>全球晶圆厂扩产持续，成熟制程+先进制程双轮驱动</li>
                    <li>行业年增速15%-20%，是半导体材料中增速最快赛道之一</li>
                </ul>
            </div>
            <div style="flex:1;min-width:200px;">
                <h4 style="color:#e67e22;margin-bottom:10px;">⚖️ 供给端：缺口扩大支撑价格上涨</h4>
                <ul style="font-size:14px;line-height:1.8;">
                    <li>日本2000吨产能因钨原料断供面临停产，占全球约20%</li>
                    <li>新建产能环评安评周期长，18个月内无大规模新增</li>
                    <li>中国钨开采总量控制，原料端持续收紧</li>
                    <li>供需缺口2026年约11%，2027年扩大至34%，紧平衡持续</li>
                </ul>
            </div>
            <div style="flex:1;min-width:200px;">
                <h4 style="color:#27ae60;margin-bottom:10px;">🇨🇳 国产替代：从跟随到主导</h4>
                <ul style="font-size:14px;line-height:1.8;">
                    <li>国内企业技术突破，6N/7N产品达到国际先进水平</li>
                    <li>中国掌握钨资源话语权，产业链自主可控能力强</li>
                    <li>海外供应链不稳定，晶圆厂加速导入国内供应商</li>
                    <li>国产化率从30%向60%+提升，空间广阔</li>
                </ul>
            </div>
        </div>
    </div>
    """
    gen.add_analysis_section(title="核心投资逻辑", content=logic_html, icon="diamond")
    
    # 10. 风险提示
    risks = [
        "估值泡沫风险：板块短期涨幅巨大，中船特气PE超380倍，PB超22倍，均处于历史100%分位。市场情绪过热背景下，若业绩兑现不及预期，可能出现较大幅度回调。",
        "订单落地不及预期风险：日本断供后客户咨询洽谈增多，但尚未签署实质性长单。晶圆厂供应商认证周期长，订单落地节奏存在不确定性，短期业绩弹性可能低于市场预期。",
        "技术替代风险：三星在第九代V-NAND中用钼替代钨，层高降低30-40%；WOF4低温沉积技术已列入台积电2027年路线图。虽距大规模量产仍需5-8年，但长期需警惕技术路线变迁风险。",
        "产能扩张超预期风险：多氟多1200吨产能预计2026Q3量产，规划总产能3000吨；和远气体等多家企业布局六氟化钨。若新玩家加速进入，可能导致行业竞争格局恶化。",
        "下游需求不及预期风险：半导体行业具有强周期性，若AI需求降温、存储扩产放缓或全球经济下行，六氟化钨需求增速可能低于预期，行业景气度快速回落。",
        "政策变动风险：钨出口管制政策、环保政策、半导体扶持政策等均存在不确定性，政策变化可能对行业供需格局和企业盈利产生重大影响。",
    ]
    gen.add_risk_section(risks=risks)
    
    # 11. 投资评级
    rating_left = """
    <div style="background:linear-gradient(135deg,#667eea 0%,#764ba2 100%);color:white;padding:30px;border-radius:12px;height:100%;">
        <h3 style="margin-top:0;">行业投资评级</h3>
        <div style="font-size:48px;font-weight:bold;margin:20px 0;">推荐</div>
        <p style="opacity:0.9;">六氟化钨行业正处于需求爆发+供给收缩+国产替代三重共振的历史性窗口期，行业高景气度至少维持2-3年。</p>
        <div style="margin-top:20px;padding-top:20px;border-top:1px solid rgba(255,255,255,0.3);">
            <p style="margin:5px 0;">评级时间：2026年6月10日</p>
            <p style="margin:5px 0;">分析师：产业链研究团队</p>
        </div>
    </div>
    """
    
    rating_right = """
    <div style="background:#f8f9fa;padding:25px;border-radius:12px;height:100%;">
        <h3 style="margin-top:0;color:#333;">核心跟踪指标</h3>
        <ul style="line-height:2;font-size:14px;list-style:none;padding-left:0;">
            <li style="margin:8px 0;">📊 <strong>六氟化钨价格走势</strong>：6N级、7N级产品周度报价</li>
            <li style="margin:8px 0;">📦 <strong>出口数据</strong>：每月海关出口量、均价变化</li>
            <li style="margin:8px 0;">🏭 <strong>产能利用率</strong>：头部企业开工率、订单排期</li>
            <li style="margin:8px 0;">📝 <strong>客户认证进展</strong>：新客户导入、长单签署情况</li>
            <li style="margin:8px 0;">🔬 <strong>技术突破</strong>：7N级产品良率提升、新工艺应用</li>
            <li style="margin:8px 0;">📜 <strong>政策变动</strong>：钨出口管制、环保政策变化</li>
            <li style="margin:8px 0;">🔄 <strong>替代技术进展</strong>：钼、WOF4等替代技术研发进度</li>
            <li style="margin:8px 0;">📈 <strong>下游需求</strong>：HBM出货量、3D NAND产能扩张节奏</li>
        </ul>
    </div>
    """
    
    gen.add_split_layout(
        title="投资评级与跟踪指标",
        left_content=rating_left,
        right_content=rating_right,
        icon="star"
    )
    
    # 生成报告
    html_content = gen.generate()
    
    output_path = '/root/daily-news-insight/docs/industry_chain/20260610_六氟化钨产业链深度研究.html'
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"报告已生成: {output_path}")
    print(f"文件大小: {len(html_content)} 字节")
    return output_path

if __name__ == '__main__':
    generate_report()
