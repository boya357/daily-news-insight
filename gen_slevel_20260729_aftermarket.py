#!/usr/bin/env python3
"""
20260729 盘后S级催化扫描生成脚本
事件：全球半导体暴跌第三日：通富微电/紫光股份跌停 机构24亿出逃 + 风格极致切换消费崛起
"""
import sys, os
sys.path.insert(0, 'v3')
os.chdir('/app/data/所有对话/主对话')

from v3.generators.s_level_catalyst import SLevelCatalystGenerator

# 初始化生成器
gen = SLevelCatalystGenerator(
    date_str="20260729",
    catalyst_title="半导体暴跌第三日：通富/紫光双跌停机构24亿出逃 + 消费崛起风格极致切换",
    subtitle="2026.07.29 · 盘后S级催化"
)

# ===== 1. 催化事件概述 =====
gen.add_catalyst_overview(
    overview="""
    <p><strong>【S级重大催化】</strong>2026年7月29日，全球半导体暴跌进入第三日，A股科技板块延续调整但大盘深V回升。费城半导体指数隔夜再跌4.49%、SMH本月跌幅扩大至19%接近2008年以来最差单月；SK海力士Q2营业利润60.54万亿韩元创历史新高但不及预期，美光跌8.85%、闪迪再跌14.25%、AMD跌8.15%。</p>
    <p style="margin-top:8px;">传导至A股，<strong>算力封测双雄通富微电、紫光股份双双封死跌停</strong>，龙虎榜显示机构合计净卖出超14亿元（通富9.79亿+紫光4.83亿），31只机构现身个股合计净卖出19.26亿元——机构系统性减仓科技高位股信号明确。但与此同时，<strong>A股三大指数探底回升集体收涨（沪指+0.40%、深成指+1.10%、创业板+1.55%），超4200只个股飘红，大消费板块全线爆发</strong>，食品饮料、乳业、零售多股涨停，市场呈现极端的"高低切换"风格切换。</p>
    <p style="margin-top:8px;"><strong>核心矛盾</strong>：全球AI硬件估值体系重估（SK海力士业绩miss+英伟达循环融资质疑）→ 半导体高位筹码松动 → 机构获利了结转向低位消费 → 风格切换是短期轮动还是中期主线切换？美联储今夜议息决议（北京时间30日凌晨2点）将成为关键变量。</p>
    <p style="margin-top:8px;"><strong>政策催化</strong>：工信部等七部门今日印发《2026年工业和信息化领域创新任务揭榜挂帅工作通知》，人形机器人与具身智能技术、类脑智能、算力高质量发展等24个专题入选，为硬科技长期逻辑提供政策支撑。</p>
    """,
    importance="S级"
)

# ===== 2. 催化事件详解 =====
gen.add_catalyst_details(
    background="""
    <p><strong>1. 全球背景：半导体板块技术性熊市确认</strong></p>
    <p>费城半导体指数（SOX）较6月高点回撤超23%，已进入技术性熊市。VanEck半导体ETF（SMH）本月累计跌幅19%，大概率创下2008年以来最差单月表现。导火索从英伟达"循环融资"质疑（7月27日）→ 韩国股市熔断+SK海力士暴跌（7月28日）→ 美股存储/光通信集体崩盘（7月29日），恐慌情绪呈链式传导。</p>
    <p style="margin-top:8px;"><strong>2. SK海力士财报：历史新高但"不及预期"</strong></p>
    <p>SK海力士Q2营业利润60.54万亿韩元（约416亿美元），同比+557%创历史新高，但低于分析师预期的64.22万亿。核心原因是公司在AI高端存储（HBM）领域投入过大，在传统DRAM涨价周期中获益相对较少。公司宣布HBM4已Q2量产出货，下半年扩大产能，与10家大客户签长期供货协议。盘后股价从跌8%快速拉回至涨1.7%，市场情绪反复。</p>
    <p style="margin-top:8px;"><strong>3. A股内部：科技高位获利盘集中兑现</strong></p>
    <p>通富微电连续两日跌停，年内最大涨幅130%+，中报预增288%-337%的利好已充分price-in；紫光股份月内涨幅超33%后跌停，机构+北向集体出逃。半导体、算力硬件、存储芯片等前期强势板块早盘遭集中抛压，科创50盘中一度大幅下挫。但<strong>与28日创业板单日暴跌7.35%不同</strong>，今日市场展现出明显的结构性分化——资金并未离场，而是进行大规模高低切换。</p>
    <p style="margin-top:8px;"><strong>4. 宏观变量：美联储议息会议今夜落地</strong></p>
    <p>美联储FOMC会议结果将于北京时间7月30日凌晨2点公布，市场普遍预期维持利率3.50%-3.75%不变（连续第五次按兵不动）。核心看点在声明语气和主席沃什的表态——中东局势推升油价、6月CPI降温但通胀风险未消，9月加息概率已升至76%-80%。</p>
    """,
    trigger="""
    <p><strong>🔥 触发因素一：机构系统性出货半导体（空方信号）</strong></p>
    <p>龙虎榜数据触目惊心：31只现身机构席位的个股中，20只净卖出，机构合计净卖出19.26亿元。通富微电机构净卖出9.79亿元（5家机构集体砸盘，其中1家零买入狂卖4.48亿），紫光股份机构净卖出4.83亿元，两大算力龙头双双跌停。这不是个股洗盘，而是机构对高位科技赛道的系统性减仓行为。</p>
    <p style="margin-top:8px;"><strong>🔥 触发因素二：消费板块全线爆发（多方信号）</strong></p>
    <p>食品饮料板块领涨两市，一鸣食品2连板、均瑶健康/良品铺子/欢乐家/李子园涨停，乳业、休闲食品、商超零售集体冲高。大金融板块午后异动，证券ETF涨2.03%，华林证券涨停。两市成交2.31万亿元，较前一日放量2708亿元，增量资金入场迹象明显，但增量资金选择的是低位消费而非高位科技。</p>
    <p style="margin-top:8px;"><strong>🔥 触发因素三：七部门揭榜挂帅人形机器人（政策催化）</strong></p>
    <p>工信部、应急管理部、央行、金融监管总局、证监会、中科院、国家文物局等七部门联合印发通知，启动2026年工信领域创新任务揭榜挂帅工作，围绕6大方向24个专题。其中<strong>人形机器人与具身智能技术专题由工信部+应急管理部联合推进</strong>，目标到2028年具身智能多模态大模型实现四类模态协同融合，多场景识别准确率96%以上。政策为科技成长提供长期支撑，有助于缓解短期恐慌情绪。</p>
    <p style="margin-top:8px;"><strong>🔥 触发因素四：美股盘后存储股反弹（外围企稳信号）</strong></p>
    <p>美股盘后存储芯片股普遍大涨：希捷科技涨6.60%、西部数据涨3.20%、闪迪涨2.07%、美光涨1.26%、SK海力士ADR转涨1.7%。科技七巨头盘后多数上涨，纳指期货涨0.57%。这意味着经过连续三日暴跌后，海外半导体板块出现初步企稳迹象，可能为明日A股科技股提供喘息窗口。</p>
    """
)

# ===== 3. 产业链梳理 =====
gen.add_industry_chain_analysis(
    upstream=[
        {
            "name": "半导体设备与材料（国产替代）",
            "desc": "短期受板块情绪拖累，但国产替代逻辑最硬。SEMI预测2026全球半导体设备销售额1659亿美元同比+23%，大基金三期3440亿七成指向设备与材料，设备零部件全链条涨价。",
            "stocks": [
                {"code": "002371", "name": "北方华创", "impact": "中性（短期情绪拖累+长期国产替代）"},
                {"code": "688072", "name": "拓荆科技", "impact": "中性偏负面（板块情绪压制）"},
                {"code": "002409", "name": "雅克科技", "impact": "负面（短期情绪杀跌，HBM前驱体逻辑未破）"},
                {"code": "688535", "name": "华海诚科", "impact": "中性（位置相对较低）"},
            ]
        },
        {
            "name": "电子铜箔与PCB材料",
            "desc": "AI算力上游核心材料，HBM和先进封装扩产带来需求增长，但短期受科技板块情绪压制明显，估值已回落至合理区间。",
            "stocks": [
                {"code": "301217", "name": "铜冠铜箔", "impact": "中性（跟随板块调整，基本面无变化）"},
            ]
        },
    ],
    midstream=[
        {
            "name": "算力封测与先进封装",
            "desc": "本次重灾区，通富微电连续两日跌停，机构出货坚决。AMD算力封测、HBM先进封装的产业逻辑未变，但短期估值回调压力大。长鑫上市利好兑现后，资金从封测老股抽离。",
            "stocks": [
                {"code": "002156", "name": "通富微电", "impact": "强负面（连续跌停+机构10亿出逃）"},
                {"code": "000938", "name": "紫光股份", "impact": "强负面（跌停+机构4.8亿出逃）"},
                {"code": "002185", "name": "华天科技", "impact": "负面（板块拖累，跌5.15%）"},
                {"code": "600584", "name": "长电科技", "impact": "负面（板块跟随调整）"},
            ]
        },
        {
            "name": "存储芯片",
            "desc": "全球存储板块经历史诗级波动。SK海力士Q2利润创新高但不及预期，HBM4量产兑现。美股存储盘后反弹，A股存储板块短期承压但产业基本面未变。",
            "stocks": [
                {"code": "688003", "name": "长鑫科技", "impact": "正面（产业地位确认，估值锚定作用）"},
                {"code": "603986", "name": "兆易创新", "impact": "负面（跌停+板块情绪）"},
            ]
        },
        {
            "name": "温控/液冷散热",
            "desc": "AI算力基础设施必备环节，英维克等液冷龙头从高点回撤超40%，短期受板块情绪拖累，但AI算力需求增长逻辑未破，估值逐步进入合理区间。",
            "stocks": [
                {"code": "002837", "name": "英维克", "impact": "负面（板块情绪+高位回撤，今日跌4.97%）"},
            ]
        },
    ],
    downstream=[
        {
            "name": "大消费（食品饮料/零售）",
            "desc": "今日资金流入主方向，高低切换首选。估值处于历史低位，中报业绩分化但龙头稳健，原奶周期改善+内需预期催化。短期情绪驱动，持续性需观察。",
            "stocks": [
                {"code": "605179", "name": "一鸣食品", "impact": "正面（2连板，消费情绪龙头）"},
                {"code": "605388", "name": "均瑶健康", "impact": "正面（涨停）"},
                {"code": "603719", "name": "良品铺子", "impact": "正面（涨停）"},
            ]
        },
        {
            "name": "人形机器人与具身智能",
            "desc": "七部门揭榜挂帅政策催化，人形机器人与具身智能技术专项由工信部+应急管理部联合推进。美国同日宣布限制中国机器人进口，国产替代紧迫性提升。长期赛道空间大，短期受科技板块情绪压制。",
            "stocks": [
                {"code": "300024", "name": "机器人", "impact": "正面（政策催化）"},
                {"code": "688169", "name": "石头科技", "impact": "中性（政策受益+板块情绪）"},
            ]
        },
    ],
)

# ===== 4. 关键数据统计 =====
gen.add_catalyst_deep_analysis(
    events=[
        {
            "title": "半导体板块机构系统性出货",
            "type": "market_structure",
            "description": "31只龙虎榜机构现身个股合计净卖出19.26亿元，通富微电/紫光股份双双跌停，机构获利了结高位科技股",
            "category": "risk_event",
        },
        {
            "title": "风格极致切换：消费崛起",
            "type": "sector_rotation",
            "description": "超4200只个股上涨，食品饮料/零售/券商领涨，两市放量2708亿，增量资金选择低位消费而非高位科技",
            "category": "market_structure",
        },
        {
            "title": "七部门人形机器人揭榜挂帅",
            "type": "policy",
            "description": "工信部等七部门启动2026年工信领域创新任务揭榜挂帅，人形机器人/类脑智能/算力等24个专题入选",
            "category": "policy_catalyst",
        },
    ]
)

# ===== 5. 持仓影响分析（双重验证） =====
from v3.generators.s_level_catalyst import Section, DataCard, DataGrid, StockTags, Badge, SubCard

portfolio_content = """
<div style="background: rgba(255,255,255,0.04); border-radius: 14px; padding: 20px; border: 1px solid rgba(255,255,255,0.08);">
    <div style="font-size: 16px; font-weight: 700; color: #f1f5f9; margin-bottom: 16px;">
        📊 持仓四标的双重验证结果
    </div>
    <div style="display: flex; flex-direction: column; gap: 12px;">
"""

# 英维克
portfolio_content += """
        <div style="background: rgba(255,255,255,0.03); border-radius: 10px; padding: 14px 16px; border: 1px solid rgba(255,255,255,0.06);">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                <div style="display: flex; align-items: center; gap: 8px;">
                    <span style="font-weight: 600; color: #f87171;">英维克 002837</span>
                    <span style="font-size: 12px; background: rgba(239,68,68,0.2); color: #fca5a5; padding: 2px 8px; border-radius: 999px;">-4.97% 收52.39元</span>
                </div>
                <span style="font-size: 12px; background: rgba(34,197,94,0.2); color: #86efac; padding: 2px 8px; border-radius: 999px;">✅ 无实质利空</span>
            </div>
            <div style="font-size: 12px; color: #94a3b8; line-height: 1.6;">
                <strong>双重验证结论：</strong>① 今日无公司公告/监管函/业绩修正；② 下跌主因是半导体板块整体调整+液冷板块情绪拖累+高位筹码松动（从93.52元高点回撤44%）；
                ③ 中标南京电信IDC机房项目为正面但影响有限。<strong>判定：板块情绪性回调，非个股基本面恶化</strong>。
            </div>
        </div>
"""

# 铜冠铜箔
portfolio_content += """
        <div style="background: rgba(255,255,255,0.03); border-radius: 10px; padding: 14px 16px; border: 1px solid rgba(255,255,255,0.06);">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                <div style="display: flex; align-items: center; gap: 8px;">
                    <span style="font-weight: 600; color: #fbbf24;">铜冠铜箔 301217</span>
                    <span style="font-size: 12px; background: rgba(251,191,36,0.2); color: #fcd34d; padding: 2px 8px; border-radius: 999px;">-0.80% 收86.96元</span>
                </div>
                <span style="font-size: 12px; background: rgba(34,197,94,0.2); color: #86efac; padding: 2px 8px; border-radius: 999px;">✅ 无实质利空</span>
            </div>
            <div style="font-size: 12px; color: #94a3b8; line-height: 1.6;">
                <strong>双重验证结论：</strong>① 今日无新公告，最新公告为7月22日职工代表董事辞职（中性）；② 走势明显强于板块，今日仅微跌0.8%，抗跌性凸显；
                ③ 中报预告已于7月20日发布。<strong>判定：板块温和跟随，基本面稳定，抗跌性较强</strong>。
            </div>
        </div>
"""

# 雅克科技
portfolio_content += """
        <div style="background: rgba(255,255,255,0.03); border-radius: 10px; padding: 14px 16px; border: 1px solid rgba(255,255,255,0.06);">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                <div style="display: flex; align-items: center; gap: 8px;">
                    <span style="font-weight: 600; color: #f87171;">雅克科技 002409</span>
                    <span style="font-size: 12px; background: rgba(239,68,68,0.2); color: #fca5a5; padding: 2px 8px; border-radius: 999px;">-8.56% 收152.18元</span>
                </div>
                <span style="font-size: 12px; background: rgba(34,197,94,0.2); color: #86efac; padding: 2px 8px; border-radius: 999px;">✅ 无实质利空</span>
            </div>
            <div style="font-size: 12px; color: #94a3b8; line-height: 1.6;">
                <strong>双重验证结论：</strong>① 今日无公司公告/业绩修正/监管函，最近公告为7月1日交易异常波动公告（中性风险提示）；
                ② 下跌主因是半导体材料板块整体调整+HBM产业链情绪降温+高位获利盘兑现；③ 未上龙虎榜，机构减仓规模小于通富/紫光。
                <strong>判定：板块系统性回调，HBM前驱体产业逻辑未破</strong>。短期跌幅较大需警惕情绪惯性，但非个股利空驱动。
            </div>
        </div>
"""

# *ST建艺
portfolio_content += """
        <div style="background: rgba(255,255,255,0.03); border-radius: 10px; padding: 14px 16px; border: 1px solid rgba(255,255,255,0.06);">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                <div style="display: flex; align-items: center; gap: 8px;">
                    <span style="font-weight: 600; color: #86efac;">*ST建艺 002789</span>
                    <span style="font-size: 12px; background: rgba(34,197,94,0.2); color: #86efac; padding: 2px 8px; border-radius: 999px;">+1.24% 收8.97元</span>
                </div>
                <span style="font-size: 12px; background: rgba(34,197,94,0.2); color: #86efac; padding: 2px 8px; border-radius: 999px;">✅ 无利空</span>
            </div>
            <div style="font-size: 12px; color: #94a3b8; line-height: 1.6;">
                <strong>双重验证结论：</strong>① 今日无新公告，摘帽预期仍在；② ST板块整体表现平稳，个股与科技板块关联度低，呈现独立走势。
                <strong>判定：独立逻辑标的，不受科技板块调整影响</strong>。
            </div>
        </div>
"""

portfolio_content += """
    </div>
    <div style="margin-top: 14px; padding: 12px 14px; background: rgba(59,130,246,0.1); border-radius: 8px; border-left: 3px solid #3b82f6;">
        <div style="font-size: 13px; color: #93c5fd; font-weight: 600;">💡 双重验证总评</div>
        <div style="font-size: 12px; color: #cbd5e1; line-height: 1.7; margin-top: 6px;">
            四只持仓<strong>均无实质性利空公告</strong>，全部下跌（除*ST建艺）均为<strong>板块情绪性回调</strong>而非个股基本面恶化。
            机构今日重点抛售对象为通富微电/紫光股份等前期涨幅巨大的算力封测标的，持仓中<strong>铜冠铜箔抗跌性最强</strong>（-0.8% vs 创业板+1.55%），
            <strong>雅克科技跌幅最大</strong>（-8.56%）需关注短期情绪惯性。<strong>不构成减仓≥30%的条件</strong>，维持原持仓策略观察。
        </div>
    </div>
</div>
"""

section_portfolio = Section(title="💼 持仓影响与双重验证", content=portfolio_content, icon="briefcase")
gen._components.append(section_portfolio)

# ===== 6. 隔夜外盘扫描（强制要求） =====
overnight_content = """
<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px;">
    <!-- 左侧：指数表现 -->
    <div style="background: rgba(255,255,255,0.04); border-radius: 12px; padding: 16px; border: 1px solid rgba(255,255,255,0.08);">
        <div style="font-size: 14px; font-weight: 700; color: #f1f5f9; margin-bottom: 12px;">📊 隔夜外盘指数表现</div>
        <div style="display: flex; flex-direction: column; gap: 8px;">
            <div style="display: flex; justify-content: space-between; align-items: center; padding: 6px 0; border-bottom: 1px solid rgba(255,255,255,0.05);">
                <span style="font-size: 13px; color: #cbd5e1;">费城半导体 SOX</span>
                <span style="font-size: 13px; color: #f87171; font-weight: 600;">-4.49%</span>
            </div>
            <div style="display: flex; justify-content: space-between; align-items: center; padding: 6px 0; border-bottom: 1px solid rgba(255,255,255,0.05);">
                <span style="font-size: 13px; color: #cbd5e1;">纳斯达克</span>
                <span style="font-size: 13px; color: #f87171;">-0.22%</span>
            </div>
            <div style="display: flex; justify-content: space-between; align-items: center; padding: 6px 0; border-bottom: 1px solid rgba(255,255,255,0.05);">
                <span style="font-size: 13px; color: #cbd5e1;">标普500</span>
                <span style="font-size: 13px; color: #86efac;">+0.21%</span>
            </div>
            <div style="display: flex; justify-content: space-between; align-items: center; padding: 6px 0; border-bottom: 1px solid rgba(255,255,255,0.05);">
                <span style="font-size: 13px; color: #cbd5e1;">道琼斯</span>
                <span style="font-size: 13px; color: #86efac; font-weight: 600;">+1.03%</span>
            </div>
            <div style="display: flex; justify-content: space-between; align-items: center; padding: 6px 0; border-bottom: 1px solid rgba(255,255,255,0.05);">
                <span style="font-size: 13px; color: #cbd5e1;">恒生指数</span>
                <span style="font-size: 13px; color: #86efac;">+1.96%</span>
            </div>
            <div style="display: flex; justify-content: space-between; align-items: center; padding: 6px 0;">
                <span style="font-size: 13px; color: #cbd5e1;">WTI原油</span>
                <span style="font-size: 13px; color: #fbbf24; font-weight: 600;">+6.58%</span>
            </div>
        </div>
        <div style="margin-top: 10px; font-size: 11px; color: #64748b;">数据来源：环球市场 · 更新时间 2026-07-29 20:27</div>
    </div>
    
    <!-- 右侧：核心半导体标的 -->
    <div style="background: rgba(255,255,255,0.04); border-radius: 12px; padding: 16px; border: 1px solid rgba(255,255,255,0.08);">
        <div style="font-size: 14px; font-weight: 700; color: #f1f5f9; margin-bottom: 12px;">🔬 核心半导体标的表现</div>
        <div style="display: flex; flex-direction: column; gap: 8px;">
            <div style="display: flex; justify-content: space-between; align-items: center; padding: 6px 0; border-bottom: 1px solid rgba(255,255,255,0.05);">
                <span style="font-size: 13px; color: #cbd5e1;">英伟达 NVDA</span>
                <span style="font-size: 13px; color: #86efac;">+0.25%（盘后+0.32%）</span>
            </div>
            <div style="display: flex; justify-content: space-between; align-items: center; padding: 6px 0; border-bottom: 1px solid rgba(255,255,255,0.05);">
                <span style="font-size: 13px; color: #cbd5e1;">美光 MU</span>
                <span style="font-size: 13px; color: #f87171;">-8.85%（盘后+1.26%）</span>
            </div>
            <div style="display: flex; justify-content: space-between; align-items: center; padding: 6px 0; border-bottom: 1px solid rgba(255,255,255,0.05);">
                <span style="font-size: 13px; color: #cbd5e1;">AMD</span>
                <span style="font-size: 13px; color: #f87171;">-8.15%</span>
            </div>
            <div style="display: flex; justify-content: space-between; align-items: center; padding: 6px 0; border-bottom: 1px solid rgba(255,255,255,0.05);">
                <span style="font-size: 13px; color: #cbd5e1;">SK海力士 ADR</span>
                <span style="font-size: 13px; color: #f87171;">-8.98%（盘后转+1.7%）</span>
            </div>
            <div style="display: flex; justify-content: space-between; align-items: center; padding: 6px 0; border-bottom: 1px solid rgba(255,255,255,0.05);">
                <span style="font-size: 13px; color: #cbd5e1;">闪迪 SNDK</span>
                <span style="font-size: 13px; color: #f87171; font-weight: 600;">-14.25%（盘后+2.07%）</span>
            </div>
            <div style="display: flex; justify-content: space-between; align-items: center; padding: 6px 0;">
                <span style="font-size: 13px; color: #cbd5e1;">应用材料 AMAT</span>
                <span style="font-size: 13px; color: #f87171;">-7.82%</span>
            </div>
        </div>
        <div style="margin-top: 10px; padding: 8px 10px; background: rgba(34,197,94,0.1); border-radius: 6px; font-size: 11px; color: #86efac;">
            🟢 盘后关键信号：存储股集体反弹（希捷+6.6%、西数+3.2%），纳指期货+0.57%，初步企稳迹象
        </div>
    </div>
</div>

<!-- 下方：事件与政策 -->
<div style="margin-top: 16px; background: rgba(255,255,255,0.04); border-radius: 12px; padding: 16px; border: 1px solid rgba(255,255,255,0.08);">
    <div style="font-size: 14px; font-weight: 700; color: #f1f5f9; margin-bottom: 12px;">🌍 隔夜重大事件与政策</div>
    <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 12px;">
        <div style="padding: 12px; background: rgba(139,92,246,0.1); border-radius: 8px; border: 1px solid rgba(139,92,246,0.2);">
            <div style="font-size: 12px; color: #a78bfa; font-weight: 600; margin-bottom: 6px;">🏛️ 美联储议息</div>
            <div style="font-size: 12px; color: #cbd5e1; line-height: 1.6;">
                北京时间7月30日凌晨2点公布决议，市场预期维持3.50%-3.75%不变。核心看点：沃什表态语气、9月加息暗示（当前概率76-80%）。油价反弹+中东局势增添通胀不确定性。
            </div>
        </div>
        <div style="padding: 12px; background: rgba(245,158,11,0.1); border-radius: 8px; border: 1px solid rgba(245,158,11,0.2);">
            <div style="font-size: 12px; color: #fbbf24; font-weight: 600; margin-bottom: 6px;">💰 CHIPS法案补贴</div>
            <div style="font-size: 12px; color: #cbd5e1; line-height: 1.6;">
                美国商务部NIST宣布8.74亿美元AI半导体技术研发补贴，7家本土企业入选。格芯获3亿美元主攻CPO共封装光学，Kepler获2.45亿研发3D铁电AI存储替代HBM。
            </div>
        </div>
        <div style="padding: 12px; background: rgba(239,68,68,0.1); border-radius: 8px; border: 1px solid rgba(239,68,68,0.2);">
            <div style="font-size: 12px; color: #f87171; font-weight: 600; margin-bottom: 6px;">⚠️ 出口管制升级</div>
            <div style="font-size: 12px; color: #cbd5e1; line-height: 1.6;">
                美国FCC更新受管制清单，新增先进机器人设备和电力逆变器类别，涵盖人形/四足机器人。同日中国七部门启动人形机器人揭榜挂帅，国产替代紧迫性进一步提升。
            </div>
        </div>
    </div>
</div>
"""

section_overnight = Section(title="🌙 隔夜外盘扫描（强制覆盖）", content=overnight_content, icon="globe")
gen._components.append(section_overnight)

# ===== 7. 投资策略建议 =====
gen.add_investment_strategy(
    strategy="""
    <p><strong>一、当前定性：牛市中期调整第三日，风格切换进行时</strong></p>
    <p>本次调整的性质是<strong>"科技高位获利了结 + 资金高低切换"</strong>，而非系统性风险。核心证据：① 大盘放量回升（成交2.31万亿+2708亿），超4200股上涨，资金并未离场只是换仓；② 消费、券商等低位板块接力上涨，市场有明确的做多方向；③ 美股盘后存储股已出现反弹信号，海外最恐慌阶段可能已过。</p>
    
    <p style="margin-top:12px;"><strong>二、持仓操作建议</strong></p>
    <p><strong>1. 英维克（002837）：</strong>今日跌4.97%收52.39元，从高点回撤44%。基本面无实质利空，但技术面破位下行趋势明显。<strong>策略：</strong>底仓持有观望，不急于抄底，等待止跌信号（连续2日收阳+放量）。关键支撑位：50元（前期平台），若跌破可能下探45元。液冷逻辑未破，等待AI算力需求重新验证。</p>
    
    <p style="margin-top:8px;"><strong>2. 铜冠铜箔（301217）：</strong>今日仅跌0.8%收86.96元，<strong>抗跌性全持仓最强</strong>，明显跑赢半导体板块和创业板。基本面稳定，估值处于合理区间。<strong>策略：</strong>继续持有，85-90元区间为合理震荡区，若科技板块企稳反弹，铜冠有望率先修复。</p>
    
    <p style="margin-top:8px;"><strong>3. 雅克科技（002409）：</strong>今日跌8.56%收152.18元，跌幅较大但未上龙虎榜，机构抛压小于通富/紫光。HBM前驱体产业逻辑未变，SK海力士Q2财报证实HBM需求旺盛。<strong>策略：</strong>底仓持有，不建议加仓抄底，等待板块情绪企稳。关键支撑位：145元（60日均线附近），若跌破需重新评估。<strong>减仓条件未触发</strong>（无实质利空+机构净卖未到5%阈值）。</p>
    
    <p style="margin-top:8px;"><strong>4. *ST建艺（002789）：</strong>今日涨1.24%收8.97元，独立逻辑标的，不受科技板块影响。<strong>策略：</strong>继续持有，摘帽预期下维持原策略。</p>
    
    <p style="margin-top:12px;"><strong>三、重点关注信号（决定后续方向）</strong></p>
    <p><strong>右侧信号（加仓条件）：</strong>① 半导体板块连续2日放量上涨，机构净买入转正；② 英伟达/美光等核心标的企稳回升，费半指数收复5日均线；③ 中报业绩验证期存储/设备龙头超预期。</p>
    <p><strong>左侧风险（减仓条件）：</strong>① 美联储议息超预期鹰派（暗示9月加息概率升至90%+）；② 持仓股出现实质利空公告或机构单日净卖出超成交额5%；③ 沪指有效跌破3800点且成交量萎缩。</p>
    
    <p style="margin-top:12px;"><strong>四、估值锚参考</strong></p>
    <p>英维克：动态PE约30-35倍（2026E），处于近3年30%分位，估值已回落至合理偏低区间；</p>
    <p>铜冠铜箔：动态PE约20-25倍（2026E），处于近3年25%分位，估值低位；</p>
    <p>雅克科技：动态PE约35-40倍（2026E），处于近3年50%分位，估值中性偏高但考虑HBM增速可接受；</p>
    <p style="margin-top:8px;"><em>数据来源：券商一致预期 · 置信度中等（板块调整期盈利预测下修风险）</em></p>
    """
)

# ===== 8. 风险提示 =====
gen.add_risk_warning([
    "美联储议息会议今夜（30日凌晨2点）公布结果，若超预期鹰派可能引发全球市场进一步调整",
    "半导体板块机构出货趋势尚未结束，短期情绪惯性可能导致持仓股继续承压",
    "SK海力士HBM产能下半年大幅扩张，若供给释放快于需求，存储涨价周期可能提前见顶",
    "风格切换持续性存疑，消费板块上涨更多是情绪和估值修复，缺乏业绩持续爆发的催化剂",
    "中东局势反复推升油价，通胀反弹风险可能限制美联储货币政策空间",
])

# ===== 发布 =====
result = gen.publish(
    title="半导体暴跌第三日：通富/紫光双跌停机构24亿出逃 + 消费崛起风格切换",
    filename="20260729_盘后_S级催化扫描_半导体暴跌+风格切换.html",
)

print("发布结果:", result)
