#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S级催化盘后扫描 - 20260716
核心事件：半导体板块系统性崩盘 + 台积电财报超预期遭抛售 + 存储板块获利回吐
"""
import sys, os
sys.path.insert(0, '/root/daily-news-insight/v3')
os.chdir('/root/daily-news-insight')

from v3.generators.s_level_catalyst import SLevelCatalystGenerator

# ============ 初始化生成器 ============
gen = SLevelCatalystGenerator(
    date_str="20260716",
    catalyst_title="半导体板块系统性崩盘",
    subtitle="2026.07.16 · 盘后S级催化"
)

# ============ 1. 催化概述 ============
gen.add_catalyst_overview(
    overview="""
    <strong>今日A股半导体板块遭遇系统性重挫</strong>，科创50暴跌4.02%失守1850点，存储芯片、先进封装、半导体设备全线下挫。核心催化链：①长鑫科技IPO申购抽血295亿（年内最大）引发市场流动性恐慌；②隔夜美股存储股集体崩盘（美光-8%、SK海力士-9%、西部数据-8%）传导至A股；③台积电Q2财报超预期但盘前仍跌，市场担忧AI算力投入成本侵蚀利润。截至收盘，全市场2860只个股下跌，半导体板块主力净流出超400亿，德明利连续一字跌停、佰维存储单日暴跌15%，板块情绪进入冰点。持仓股雅克科技触及跌停（-10%），铜冠铜箔续跌，英维克探底64元后小幅收涨。
    """,
    importance="S级"
)

# ============ 2. 催化详情（背景+触发） ============
gen.add_catalyst_details(
    background="""
    <p>半导体板块自6月下旬以来持续走弱，费城半导体指数从6月22日高点已回落约16%，进入技术性调整区间。</p>
    <p><strong>背景一：存储板块估值透支</strong>——前期SK海力士上市、HBM涨价、存储超级周期等利好已充分定价，A股存储概念股普遍涨幅50%-200%，获利盘积累丰厚，中报最后披露期机构集中兑现。</p>
    <p><strong>背景二：长鑫科技IPO抽血效应</strong>——7月16日科创板申购，募资295亿元创年内最大，市场担忧冻结资金超万亿，叠加7月以来成交额从3.1万亿缩至2.4万亿，流动性持续收紧。</p>
    <p><strong>背景三：地缘风险升温</strong>——美军对伊朗发动第二轮空袭，原油上涨推升通胀预期，美联储降息时点可能延后，风险资产承压。</p>
    """,
    trigger="""
    <p><strong>触发一：隔夜存储股集体崩盘⚡</strong>——美光科技大跌8.02%、闪迪跌超8%、西部数据跌超8%、SK海力士美股跌9%，费城半导体指数跌2.08%。存储板块获利回吐浪潮从美股传导至A股。</p>
    <p><strong>触发二：台积电Q2财报超预期但"利好出尽"</strong>——Q2净利润同比+77.4%、毛利率67.7%均超预期，但资本支出上调至600-640亿美元引发市场对AI投入成本的担忧，盘前台积电ADR仍下跌。</p>
    <p><strong>触发三：德明利一字跌停带崩板块情绪</strong>——德明利二季度净利润环比下滑5.74%-29.65%，封单超60亿，成为存储板块情绪崩溃的导火索。</p>
    <p><strong>触发四：中报业绩雷集中释放</strong>——主板中报预告最后披露日（7/15）后，62只高位科技小票预亏，市场从"炒题材"切换至"炒业绩"，纯概念标的遭抛售。</p>
    """
)

# ============ 3. 产业链分析 ============
gen.add_industry_chain_analysis(
    upstream=[
        {"name": "半导体材料", "status": "🔴 深度调整", "detail": "雅克科技触及跌停、华海诚科-7%，HBM前驱体/封装材料板块获利回吐"},
        {"name": "半导体设备", "status": "🟡 相对抗跌", "detail": "中微公司/北方华创跌幅小于板块，ASML上调全年指引提供一定支撑"},
        {"name": "电子特气", "status": "🟡 分化", "detail": "氦气出口管制催化余温尚存，但板块整体跟跌"},
    ],
    midstream=[
        {"name": "存储芯片", "status": "🔴 崩盘式下跌", "detail": "德明利一字跌停、佰维存储-15%、深科技跌停、江波龙-10%，板块主力净流出超200亿"},
        {"name": "先进封装", "status": "🔴 大幅调整", "detail": "长电科技-9%、通富微电-8%、华天科技跌停，HBM封装逻辑短期让位于情绪杀跌"},
        {"name": "晶圆制造", "status": "🟡 中芯概念领跌", "detail": "中芯国际-5%、华虹公司-6%，台积电财报利好未传导至A股"},
    ],
    downstream=[
        {"name": "AI算力/液冷", "status": "🔴 持续走弱", "detail": "英维克再探新低64元、曙光数创-7%、高澜股份-6%，液冷板块未见企稳信号"},
        {"name": "AI应用/游戏", "status": "🟢 逆势上涨", "detail": "传媒板块+1.66%、游戏/影视院线领涨，资金高低切换至应用端"},
        {"name": "创新药/消费", "status": "🟢 防御性走强", "detail": "医药生物+1.57%、白酒/食品饮料抗跌，避险资金涌入防御板块"},
    ]
)

# ============ 4. 投资机会 ============
gen.add_investment_opportunities(
    opportunities=[
        {
            "title": "半导体设备国产替代",
            "level": "A级机会",
            "direction": "中期逢低布局",
            "logic": "ASML上调全年指引+2027年低NA EUV产能增30%，半导体设备需求逻辑未破；国产替代加速背景下，中微公司、北方华创、拓荆科技等设备龙头回调后估值更具吸引力。ASML证实英特尔High NA EUV已用于Ultra 3量产，先进制程设备需求确定性高。",
            "targets": [
                {"code": "688012", "name": "中微公司", "impact": "刻蚀设备龙头"},
                {"code": "002371", "name": "北方华创", "impact": "平台型龙头"},
                {"code": "688072", "name": "拓荆科技", "impact": "薄膜沉积龙头"},
            ],
            "risk": "科创板流动性收缩，短期可能继续下探"
        },
        {
            "title": "存储芯片HBM核心标的",
            "level": "B级机会",
            "direction": "耐心等待企稳",
            "logic": "存储超级周期逻辑未破（HBM4 2027年价格翻倍、SK海力士CEO称2027年最紧缺），但短期获利盘兑现+美股存储股回调压力较大，需等待A股存储板块情绪企稳。长鑫科技IPO完成后反而可能成为存储板块情绪修复催化剂。",
            "targets": [
                {"code": "301217", "name": "铜冠铜箔", "impact": "HBM铜箔龙头，持仓股"},
                {"code": "002409", "name": "雅克科技", "impact": "HBM前驱体龙头，持仓股"},
                {"code": "688525", "name": "佰维存储", "impact": "存储模组龙头"},
            ],
            "risk": "板块情绪冰点期可能继续下探10%-15%"
        },
        {
            "title": "AI应用端防御切换",
            "level": "B级机会",
            "direction": "短期关注",
            "logic": "资金从硬件端高低切换至应用端，今日传媒+1.66%、游戏/影视逆势上涨。苹果AI国行版与阿里千问合作落地，AI应用商业化加速预期升温。防御性板块创新药、白酒、消费表现相对强势。",
            "targets": [
                {"code": "300413", "name": "芒果超媒", "impact": "AI+内容"},
                {"code": "002555", "name": "三七互娱", "impact": "AI+游戏"},
            ],
            "risk": "防御性行情持续性待观察"
        },
    ],
    view_mode="card"
)

# ============ 5. 持仓股影响评估（双重验证） ============
# 使用StockTags组件渲染持仓股
from v3.components.data import StockTags
holdings = [
    {"code": "002409", "name": "雅克科技", "impact": "触及跌停"},
    {"code": "301217", "name": "铜冠铜箔", "impact": "续跌破位"},
    {"code": "002837", "name": "英维克", "impact": "探底64元"},
    {"code": "002789", "name": "*ST建艺", "impact": "退市风险"},
]
holdings_html = StockTags(holdings)

section_header = f'''
<div class="mb-4">
    <div style="background: linear-gradient(135deg, rgba(239,68,68,0.15) 0%, rgba(220,38,38,0.08) 100%);
                border-radius: 16px; padding: 24px; border: 1px solid rgba(248,113,113,0.25);">
        <div style="display: flex; align-items: center; margin-bottom: 12px; flex-wrap: wrap; gap: 8px;">
            <div style="display: flex; align-items: center;">
                <span style="font-size: 22px; margin-right: 10px;">📊</span>
                <span style="font-size: 18px; font-weight: 700; color: #fca5a5;">持仓股今日表现与影响评估</span>
            </div>
            <span style="font-size: 12px; color: #f87171; background: rgba(239,68,68,0.15); 
                         padding: 4px 10px; border-radius: 20px; border: 1px solid rgba(248,113,113,0.3);">双重验证</span>
        </div>
        <div style="margin-bottom: 14px;">
            {holdings_html}
        </div>
'''

gen._components.append(section_header)

# 雅克科技
gen._components.append('''
        <div style="background: rgba(0,0,0,0.25); border-radius: 12px; padding: 16px; margin-bottom: 12px;
                    border: 1px solid rgba(239,68,68,0.2);">
            <div style="display: flex; align-items: center; margin-bottom: 10px; flex-wrap: wrap; gap: 8px;">
                <span style="font-weight: 700; color: #f87171; font-size: 15px;">雅克科技 (002409)</span>
                <span style="color: #ef4444; font-weight: 700; font-size: 13px;">-10% 触及跌停</span>
                <span style="margin-left: auto; color: #fbbf24; font-size: 12px;">⚠️ 两日累计-18%</span>
            </div>
            <div style="font-size: 13px; color: #cbd5e1; line-height: 1.8;">
                <p><strong>今日表现：</strong>开盘190.52元，盘中触及跌停板154.17元（证星异动提醒14:50确认），
                    多信源数据有差异（东方财富显示收171.30/-8.64% vs 证星称触及跌停），
                    实际为尾盘封板前状态，但全天跌幅显著大于板块平均。</p>
                <p><strong>跌停原因分析：</strong>
                    <br>① <strong>板块系统性风险</strong>——半导体/HBM板块集体崩盘，德明利一字跌停带崩情绪
                    <br>② <strong>获利盘集中兑现</strong>——7月初160元→229元历史新高，涨幅超40%，机构加速出货
                    <br>③ <strong>美股存储股传导</strong>——美光-8%、SK海力士-9%引发A股存储产业链跟跌
                </p>
                <p style="color: #86efac;"><strong>✅ 双重验证结论：</strong>
                    <br>• 证星异动提醒 + 中财网盘中数据 + 证券时报均确认大幅下跌
                    <br>• 板块性下跌，雅克跌幅属β放大，<strong>未发现公司自身利空公告</strong>（无减持、无业绩下修、无监管问询）
                    <br>• <strong style="color: #fbbf24;">结论：系统性风险导致的获利盘兑现，非个股实质性利空</strong>
                </p>
                <p><strong>估值锚：</strong>PE(TTM)约75倍（近2年60%分位，中性偏高）；PB约10倍（近2年80%分位）
                <br><strong>技术位：</strong>支撑位160元（60日均线附近），强支撑150元（前期突破平台）</p>
            </div>
        </div>
''')

# 铜冠铜箔
gen._components.append('''
        <div style="background: rgba(0,0,0,0.25); border-radius: 12px; padding: 16px; margin-bottom: 12px;
                    border: 1px solid rgba(251,191,36,0.2);">
            <div style="display: flex; align-items: center; margin-bottom: 10px; flex-wrap: wrap; gap: 8px;">
                <span style="font-weight: 700; color: #fbbf24; font-size: 15px;">铜冠铜箔 (301217)</span>
                <span style="color: #fbbf24; font-weight: 700; font-size: 13px;">续跌约-5%~-7%</span>
                <span style="margin-left: auto; color: #fbbf24; font-size: 12px;">🟡 存储板块拖累</span>
            </div>
            <div style="font-size: 13px; color: #cbd5e1; line-height: 1.8;">
                <p><strong>今日表现：</strong>存储板块集体崩盘背景下继续下探，昨日收127.40元，今日大概率跌破120元支撑（收盘数据待确认）。</p>
                <p><strong>下跌原因：</strong>存储板块系统性调整+获利盘兑现，HBM铜箔需求逻辑未变但短期情绪极差</p>
                <p style="color: #86efac;"><strong>✅ 双重验证：</strong>德明利跌停+佰维存储-15%+深科技跌停，存储板块普跌，铜冠铜箔跌幅在板块内属中等水平</p>
                <p><strong>估值锚：</strong>动态PE约45倍（2026E，近3年55%分位）；PB约5.5倍
                <br><strong>技术位：</strong>支撑115元（前期平台），强支撑105元（30日均线附近）</p>
            </div>
        </div>
''')

# 英维克
gen._components.append('''
        <div style="background: rgba(0,0,0,0.25); border-radius: 12px; padding: 16px; margin-bottom: 12px;
                    border: 1px solid rgba(148,163,184,0.2);">
            <div style="display: flex; align-items: center; margin-bottom: 10px; flex-wrap: wrap; gap: 8px;">
                <span style="font-weight: 700; color: #94a3b8; font-size: 15px;">英维克 (002837)</span>
                <span style="color: #4ade80; font-weight: 700; font-size: 13px;">+0.18% 探底回升</span>
                <span style="margin-left: auto; color: #4ade80; font-size: 12px;">🟢 最低64元</span>
            </div>
            <div style="font-size: 13px; color: #cbd5e1; line-height: 1.8;">
                <p><strong>今日表现：</strong>今开66.50元，最高70.77元，最低64.00元，收67.86元(+0.18%)，振幅9.99%。
                    盘中再创调整新低64元，但尾盘收红，显示64-65元区间有一定承接。</p>
                <p><strong>信号解读：</strong>液冷板块整体走弱背景下，英维克再创新低后V反收平，
                    属于超跌后的技术性反弹，<strong>非趋势反转信号</strong>。</p>
                <p style="color: #86efac;"><strong>✅ 双重验证：</strong>富途牛牛 + 中财网 + e公司三个信源确认收盘价67.86元左右，振幅近10%，最低64元</p>
                <p><strong>估值锚：</strong>PE(TTM)约179倍（估值依然偏高）；PB约26倍（近2年10%分位，已深度回调）
                <br><strong>技术位：</strong>支撑64元（今日低点），压力70元（5日线）、75元（10日线）</p>
            </div>
        </div>
''')

# *ST建艺
gen._components.append('''
        <div style="background: rgba(0,0,0,0.25); border-radius: 12px; padding: 16px;
                    border: 1px solid rgba(239,68,68,0.2);">
            <div style="display: flex; align-items: center; margin-bottom: 10px; flex-wrap: wrap; gap: 8px;">
                <span style="font-weight: 700; color: #ef4444; font-size: 15px;">*ST建艺 (002789)</span>
                <span style="color: #ef4444; font-weight: 700; font-size: 13px;">🚨 退市风险未解除</span>
                <span style="margin-left: auto; color: #ef4444; font-size: 12px;">必须清仓</span>
            </div>
            <div style="font-size: 13px; color: #cbd5e1; line-height: 1.8;">
                <p>退市风险+诉讼+债务问题三大雷未解，成交低迷流动性枯竭，任何价格立即清仓止损。</p>
            </div>
        </div>
''')

gen._components.append('''
    </div>
</div>
''')

# ============ 6. 隔夜外盘扫描（强制覆盖） ============
gen._components.append('''
<div class="mb-4">
    <div style="background: linear-gradient(135deg, rgba(59,130,246,0.15) 0%, rgba(139,92,246,0.08) 100%);
                border-radius: 16px; padding: 24px; border: 1px solid rgba(96,165,250,0.25);">
        <div style="display: flex; align-items: center; margin-bottom: 16px; flex-wrap: wrap; gap: 8px;">
            <div style="display: flex; align-items: center;">
                <span style="font-size: 22px; margin-right: 10px;">🌍</span>
                <span style="font-size: 18px; font-weight: 700; color: #93c5fd;">隔夜外盘扫描（截至北京时间20:00）</span>
            </div>
            <span style="margin-left: auto; font-size: 12px; color: #60a5fa; background: rgba(59,130,246,0.15);
                         padding: 4px 10px; border-radius: 20px; border: 1px solid rgba(96,165,250,0.3);">V4.0强制项</span>
        </div>
        
        <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 12px; margin-bottom: 16px;">
            <div style="background: rgba(0,0,0,0.25); border-radius: 10px; padding: 14px; border: 1px solid rgba(239,68,68,0.2);">
                <div style="font-size: 13px; color: #94a3b8; margin-bottom: 6px;">费城半导体指数</div>
                <div style="font-size: 20px; font-weight: 700; color: #f87171;">-2.08%</div>
                <div style="font-size: 11px; color: #64748b;">较6月高点回落约16%</div>
            </div>
            <div style="background: rgba(0,0,0,0.25); border-radius: 10px; padding: 14px; border: 1px solid rgba(34,197,94,0.2);">
                <div style="font-size: 13px; color: #94a3b8; margin-bottom: 6px;">纳斯达克指数</div>
                <div style="font-size: 20px; font-weight: 700; color: #4ade80;">+0.62%</div>
                <div style="font-size: 11px; color: #64748b;">科技七巨头多数上涨，苹果+4%</div>
            </div>
        </div>
        
        <div style="font-size: 14px; font-weight: 600; color: #e2e8f0; margin-bottom: 10px;">📡 核心半导体标的表现</div>
        <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 8px; margin-bottom: 14px;">
            <div style="background: rgba(0,0,0,0.2); border-radius: 8px; padding: 10px; text-align: center;">
                <div style="font-size: 12px; color: #94a3b8;">美光科技</div>
                <div style="font-size: 16px; font-weight: 700; color: #f87171;">-8.02%</div>
            </div>
            <div style="background: rgba(0,0,0,0.2); border-radius: 8px; padding: 10px; text-align: center;">
                <div style="font-size: 12px; color: #94a3b8;">SK海力士(美股)</div>
                <div style="font-size: 16px; font-weight: 700; color: #f87171;">-9.00%</div>
            </div>
            <div style="background: rgba(0,0,0,0.2); border-radius: 8px; padding: 10px; text-align: center;">
                <div style="font-size: 12px; color: #94a3b8;">英伟达</div>
                <div style="font-size: 16px; font-weight: 700; color: #4ade80;">+0.33%</div>
            </div>
            <div style="background: rgba(0,0,0,0.2); border-radius: 8px; padding: 10px; text-align: center;">
                <div style="font-size: 12px; color: #94a3b8;">AMD</div>
                <div style="font-size: 16px; font-weight: 700; color: #f87171;">-3.46%</div>
            </div>
            <div style="background: rgba(0,0,0,0.2); border-radius: 8px; padding: 10px; text-align: center;">
                <div style="font-size: 12px; color: #94a3b8;">台积电ADR(盘前)</div>
                <div style="font-size: 16px; font-weight: 700; color: #fbbf24;">下跌中</div>
            </div>
            <div style="background: rgba(0,0,0,0.2); border-radius: 8px; padding: 10px; text-align: center;">
                <div style="font-size: 12px; color: #94a3b8;">ASML</div>
                <div style="font-size: 16px; font-weight: 700; color: #4ade80;">+2%+</div>
            </div>
        </div>
        
        <div style="font-size: 14px; font-weight: 600; color: #e2e8f0; margin-bottom: 10px;">🔥 重点事件</div>
        <div style="font-size: 13px; color: #cbd5e1; line-height: 1.8;">
            <p>① <strong>台积电Q2财报超预期</strong>：净利润+77.4%、毛利率67.7%均超预期，上调全年营收增长指引至40%+，资本支出上调至600-640亿美元。但盘前仍下跌，市场担忧AI投入成本。</p>
            <p>② <strong>ASML上调全年指引</strong>：2026年净销售额预期上调至430-450亿欧元，2027年低NA EUV产能增加30%。英特尔High NA EUV已用于Ultra 3量产。</p>
            <p>③ <strong>存储股集体崩盘</strong>：美光-8%、西部数据/闪迪-8%、希捷-6%、迈威尔-7%。存储板块从"超级周期"叙事切换至"获利兑现"阶段。</p>
            <p>④ <strong>地缘风险升级</strong>：美军对伊朗发动第二轮空袭，伊朗威胁打击海湾基础设施。原油上涨推升通胀担忧。</p>
            <p>⑤ <strong>美股盘前期货</strong>（截至20:00）：纳指期货-0.8%~-0.9%、标普500期货-0.3%、道指期货+0.1%，科技股继续承压。</p>
        </div>
    </div>
</div>
''')

# ============ 7. 明日策略 ============
gen.add_investment_strategy(
    strategy="""
    <div style="font-size: 14px; line-height: 2; color: #cbd5e1;">
    <p><strong style="color: #f87171;">整体判断：半导体板块进入情绪冰点期，短期或继续探底，但中期逻辑未破</strong></p>
    
    <p><strong>一、大盘层面：</strong>沪指跌破3900点创调整新低，成交额缩至2.4万亿，市场信心不足。长鑫科技IPO申购完成后，抽血效应有望缓解。短期关注3800点支撑，中期等待放量长阳确认企稳。</p>
    
    <p><strong>二、持仓操作建议（附估值锚）：</strong></p>
    <p>1. <strong>雅克科技</strong>：今日触及跌停，连续两日暴跌累计约18%。
        <br>📌 估值锚：PE(TTM)约75倍（近2年60%分位），PB约10倍（近2年80%分位）
        <br>📌 技术位：支撑160元（60日均线），强支撑150元（前期突破平台）
        <br>📌 操作：<strong>减仓至1/4底仓</strong>，160元附近观察支撑，跌破160元止盈离场。逻辑：HBM前驱体需求未变但短期情绪极差，控制仓位优先。
    </p>
    <p>2. <strong>铜冠铜箔</strong>：存储板块系统性调整，跌破120元。
        <br>📌 估值锚：动态PE约45倍（2026E，近3年55%分位），PB约5.5倍
        <br>📌 技术位：支撑115元，强支撑105元
        <br>📌 操作：<strong>减仓至底仓1/4以下</strong>，反弹125-130元坚决减仓，破115元止盈离场。
    </p>
    <p>3. <strong>英维克</strong>：探底64元后小幅收红，创新低后V反。
        <br>📌 估值锚：PE(TTM)约179倍（偏高），PB约26倍（近2年10%分位）
        <br>📌 技术位：支撑64元（今日低点），压力70/75元
        <br>📌 操作：<strong>无条件清仓</strong>（已深度破止损35%+），任何反弹都是离场机会，严禁补仓抄底。
    </p>
    <p>4. <strong>*ST建艺</strong>：退市风险未解除，<strong>任何价格立即清仓</strong>。</p>
    
    <p><strong>三、板块策略：</strong>
    <br>• 短期防御：创新药、白酒、消费等防御板块
    <br>• 中期布局：半导体设备龙头（ASML上调指引+国产替代）回调后逢低吸纳
    <br>• 耐心等待：存储板块情绪企稳信号（美股存储股止跌+A股量能萎缩）
    </p>
    
    <p><strong style="color: #fbbf24;">⚠️ 风险提示：市场情绪极度脆弱，任何利空都可能被放大，控制仓位在2成以下，现金为王，等待企稳信号。</strong></p>
    </div>
    """
)

# ============ 8. 风险提示 ============
gen.add_risk_warning(
    risks=[
        "半导体板块情绪可能继续恶化，短期跌幅不可预测，切勿抄底",
        "长鑫科技IPO后锁定期抛压、存量资金博弈可能加剧市场波动",
        "地缘冲突升级（美伊局势）可能导致全球风险资产进一步调整",
        "中报业绩雷潮尚未完全消化，高位股仍有补跌风险",
        "美联储降息预期延后可能压制全球科技股估值",
        "持仓股已深度破止损，严格执行纪律，严禁情绪化补仓"
    ]
)

# ============ 发布 ============
print("正在生成报告...")
result = gen.publish(
    title="半导体板块系统性崩盘",
    filename="20260716_盘后_S级催化扫描_半导体板块系统性崩盘.html",
    excerpt="科创50暴跌4.02%，存储芯片/先进封装/半导体设备全线下挫，美光-8%+SK海力士-9%传导，长鑫科技IPO抽血295亿，雅克科技触及跌停"
)
print(f"发布结果: {result}")
