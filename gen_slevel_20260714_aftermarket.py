import sys, os
sys.path.insert(0, 'v3')
os.chdir('/app/data/所有对话/主对话')
from v3.generators.s_level_catalyst import SLevelCatalystGenerator

gen = SLevelCatalystGenerator(
    date_str="20260714",
    catalyst_title="PCB业绩爆发潮+央行5000亿放水+外盘半导体反弹",
    subtitle="2026.07.14 · 盘后S级催化"
)

# 1. 催化事件概述
gen.add_catalyst_overview(
    "三大重磅催化共振：①PCB/算力产业链半年报业绩炸裂，生益科技、沪电股份、东山精密批量涨停，长飞光纤净利增9倍；②央行盘后宣布7月15日开展1.4万亿6个月买断式逆回购，净投放5000亿，流动性超预期宽松；③美股盘前半导体集体反弹，SK海力士涨超6%，美光涨3.4%，存储板块修复性反弹。SemiAnalysis力挺海力士HBM4量产，存储中期逻辑未破。"
)

# 2. 催化事件详解
gen.add_catalyst_details(
    background="7月14日A股早盘延续恐慌调整，午后走出深V反转，沪指收涨1.36%收复3900点，创业板指涨超3%。市场核心矛盾由前期地缘冲突引发的避险抛售，逐步转向中报业绩验证+流动性预期修复的双重支撑。PCB板块掀起涨停潮成为今日最强主线，生益科技、沪电股份、东山精密、广合科技等多股涨停，验证AI算力产业链从光模块向PCB/CCL等上游环节传导的业绩兑现逻辑。",
    trigger="三大触发因素共振：①业绩端——生益电子上半年净利增104%-114%，长飞光纤净利增711%-914%，东山精密增283%-296%，利通电子增1173%-1368%，算力产业链业绩全面超预期；②流动性——央行7月15日开展1.4万亿6个月买断式逆回购，净投放5000亿，跨越至2027年初，对冲税期+政府债缴款超2.2万亿缺口；③外盘修复——SemiAnalysis维持海力士乐观判断，HBM4量产进入爬坡期，SK海力士ADR涨超6%，存储板块集体反弹。"
)

# 3. 产业链分析
gen.add_industry_chain_analysis(
    upstream=[
        {
            "name": "覆铜板（CCL）/铜箔",
            "desc": "PCB产业链最上游，受益AI服务器高多层板需求爆发，铜箔加工费持续上行",
            "stocks": [
                {"code": "600183", "name": "生益科技", "impact": "涨停+10%"},
                {"code": "301217", "name": "铜冠铜箔", "impact": "持仓"},
                {"code": "688519", "name": "南亚新材", "impact": "机构净卖1.46亿"},
            ]
        },
        {
            "name": "电子玻纤",
            "desc": "覆铜板核心原材料，供给端集中度高，需求随AI服务器升级",
            "stocks": [
                {"code": "600176", "name": "中国巨石", "impact": "跟涨"},
            ]
        },
    ],
    midstream=[
        {
            "name": "PCB（印制电路板）",
            "desc": "AI算力产业链核心环节，高多层/HDI/载板需求爆发，业绩弹性最大",
            "stocks": [
                {"code": "002463", "name": "沪电股份", "impact": "涨停+10% 机构净买5.97亿"},
                {"code": "002384", "name": "东山精密", "impact": "涨停+10% 机构净买4.37亿"},
                {"code": "002916", "name": "深南电路", "impact": "跟涨"},
            ]
        },
        {
            "name": "光模块/光纤",
            "desc": "AI算力传输核心，800G/1.6T持续放量，长飞光纤Q2环比增284%-405%",
            "stocks": [
                {"code": "601869", "name": "长飞光纤", "impact": "净利增711%-914%"},
                {"code": "300308", "name": "中际旭创", "impact": "主力净流入59亿"},
                {"code": "300502", "name": "新易盛", "impact": "主力净流入54亿"},
            ]
        },
    ],
    downstream=[
        {
            "name": "AI服务器/数据中心",
            "desc": "算力需求终极载体，英伟达Vera Rubin平台推进，HBM4量产在即",
            "stocks": [
                {"code": "002837", "name": "英维克", "impact": "持仓-液冷散热"},
                {"code": "603019", "name": "中科曙光", "impact": "国产算力"},
            ]
        },
        {
            "name": "先进封装",
            "desc": "Chiplet/CoWoS需求持续紧张，台积电涨价传导",
            "stocks": [
                {"code": "002156", "name": "通富微电", "impact": "跟涨"},
                {"code": "002409", "name": "雅克科技", "impact": "持仓-光刻胶/前驱体"},
            ]
        },
    ]
)

# 4. 投资机会分析
gen.add_investment_opportunities([
    {
        "name": "PCB高弹性主线（S级）",
        "priority": "高",
        "logic": "AI算力PCB业绩爆发确认，生益/沪电/东山精密三驾马车齐涨停，机构龙虎榜净买入合计超10亿。从光模块→PCB→CCL→铜箔的产业链传导逻辑验证，叠加英伟达下一代平台催化，中期确定性高。关注回调后的加仓机会。",
        "stocks": [
            {"code": "002463", "name": "沪电股份", "impact": "机构净买5.97亿+北向6.39亿"},
            {"code": "002384", "name": "东山精密", "impact": "净利增283%-296%"},
            {"code": "600183", "name": "生益科技", "impact": "净利增117%-131%"},
        ]
    },
    {
        "name": "铜箔/CCL上游补涨（A级）",
        "priority": "高",
        "logic": "PCB涨停潮将向上游铜箔、覆铜板传导，铜冠铜箔作为电子铜箔标的，叠加锂电铜箔复苏预期，估值处于历史低位。生益科技已涨停验证CCL逻辑，铜箔环节弹性可能更大。",
        "stocks": [
            {"code": "301217", "name": "铜冠铜箔", "impact": "持仓，PCB上游补涨逻辑"},
            {"code": "688519", "name": "南亚新材", "impact": "CCL标的"},
        ]
    },
    {
        "name": "存储板块修复性反弹（A级）",
        "priority": "中",
        "logic": "SemiAnalysis力挺SK海力士，HBM4量产爬坡进行时，存储中期逻辑未破。美股盘前存储集体反弹（海力士+6%、美光+3.4%、闪迪+5.7%），A股存储板块经过连续调整后有望迎来修复。但需注意短期情绪仍脆弱，控制仓位。",
        "stocks": [
            {"code": "603986", "name": "兆易创新", "impact": "存储龙头"},
            {"code": "002409", "name": "雅克科技", "impact": "持仓-存储材料"},
            {"code": "300458", "name": "全志科技", "impact": "存储控制"},
        ]
    },
    {
        "name": "券商重组催化（B级）",
        "priority": "低",
        "logic": "中金+东兴+信达三家券商大重组获证监会受理，交易规模1139亿。券商板块受流动性宽松+资本市场改革双轮驱动，但整体弹性弱于科技主线，作为情绪指标观察。",
        "stocks": [
            {"code": "601995", "name": "中金公司", "impact": "重组主体"},
            {"code": "601198", "name": "东兴证券", "impact": "被合并方"},
        ]
    },
], view_mode="tab")

# 5. 隔夜外盘扫描（强制模块）
global_market_html = '''
<div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 12px; margin-bottom: 16px;">
    <div style="background: linear-gradient(135deg, rgba(34,197,94,0.15) 0%, rgba(22,163,74,0.08) 100%); border-radius: 12px; padding: 16px; border: 1px solid rgba(34,197,94,0.25);">
        <div style="font-size: 12px; color: #86efac; margin-bottom: 6px;">纳指期货</div>
        <div style="font-size: 22px; font-weight: 700; color: #4ade80;">+0.44%</div>
        <div style="font-size: 11px; color: #64748b; margin-top: 4px;">盘前 19:00</div>
    </div>
    <div style="background: linear-gradient(135deg, rgba(239,68,68,0.15) 0%, rgba(185,28,28,0.08) 100%); border-radius: 12px; padding: 16px; border: 1px solid rgba(239,68,68,0.25);">
        <div style="font-size: 12px; color: #fca5a5; margin-bottom: 6px;">道指期货</div>
        <div style="font-size: 22px; font-weight: 700; color: #f87171;">-0.20%</div>
        <div style="font-size: 11px; color: #64748b; margin-top: 4px;">盘前 19:00</div>
    </div>
    <div style="background: linear-gradient(135deg, rgba(34,197,94,0.15) 0%, rgba(22,163,74,0.08) 100%); border-radius: 12px; padding: 16px; border: 1px solid rgba(34,197,94,0.25);">
        <div style="font-size: 12px; color: #86efac; margin-bottom: 6px;">SK海力士ADR</div>
        <div style="font-size: 22px; font-weight: 700; color: #4ade80;">+6.56%</div>
        <div style="font-size: 11px; color: #64748b; margin-top: 4px;">盘前反弹</div>
    </div>
    <div style="background: linear-gradient(135deg, rgba(251,146,60,0.15) 0%, rgba(234,88,12,0.08) 100%); border-radius: 12px; padding: 16px; border: 1px solid rgba(251,146,60,0.25);">
        <div style="font-size: 12px; color: #fdba74; margin-bottom: 6px;">WTI原油</div>
        <div style="font-size: 22px; font-weight: 700; color: #fb923c;">+约10%</div>
        <div style="font-size: 11px; color: #64748b; margin-top: 4px;">地缘冲突</div>
    </div>
</div>
<div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px; margin-bottom: 16px;">
    <div style="background: rgba(255,255,255,0.04); border-radius: 12px; padding: 14px; border: 1px solid rgba(255,255,255,0.08);">
        <div style="font-size: 13px; font-weight: 600; color: #e2e8f0; margin-bottom: 8px;">📊 昨夜美股收盘回顾</div>
        <div style="font-size: 12px; color: #94a3b8; line-height: 1.8;">
            • 纳指 -1.55%（收于25873点）<br>
            • 费半指数 -4.78%（12347点）<br>
            • 英伟达 -3.52% / AMD -4.21%<br>
            • 美光 -4.32% / 台积电ADR -2.89%<br>
            • SK海力士ADR -9.32%（首尔跌15.37%）
        </div>
    </div>
    <div style="background: rgba(255,255,255,0.04); border-radius: 12px; padding: 14px; border: 1px solid rgba(255,255,255,0.08);">
        <div style="font-size: 13px; font-weight: 600; color: #e2e8f0; margin-bottom: 8px;">🔄 盘前修复情况</div>
        <div style="font-size: 12px; color: #94a3b8; line-height: 1.8;">
            • SK海力士 +6.56%（SemiAnalysis力挺）<br>
            • 美光 +3.44% / 闪迪 +5.68%<br>
            • 英伟达 +0.45% / 西部数据 +2.78%<br>
            • Tower半导体 +18.84%（日本扩产）<br>
            • 整体存储板块集体反弹
        </div>
    </div>
    <div style="background: rgba(255,255,255,0.04); border-radius: 12px; padding: 14px; border: 1px solid rgba(255,255,255,0.08);">
        <div style="font-size: 13px; font-weight: 600; color: #e2e8f0; margin-bottom: 8px;">🌏 亚太/产业动态</div>
        <div style="font-size: 12px; color: #94a3b8; line-height: 1.8;">
            • 海力士HBM4量产爬坡，9月起供英伟达Vera Rubin<br>
            • 博世美国加州碳化硅工厂试生产<br>
            • Tower半导体日本双线扩产硅光子/先进封装<br>
            • 台积电成熟制程2027年涨价（个位数）<br>
            • 三星S26 Ultra屏幕泛红问题发酵
        </div>
    </div>
</div>
<div style="background: linear-gradient(135deg, rgba(59,130,246,0.1) 0%, rgba(139,92,246,0.06) 100%); border-radius: 12px; padding: 14px; border: 1px solid rgba(96,165,250,0.2);">
    <div style="font-size: 13px; font-weight: 600; color: #60a5fa; margin-bottom: 8px;">💡 外盘对A股映射判断</div>
    <div style="font-size: 12px; color: #cbd5e1; line-height: 1.8;">
        昨夜美股半导体暴跌的恐慌情绪已在今日A股早盘充分释放（科创板最低跌超4%），午后深V反弹说明抄底资金已入场。盘前存储板块的修复性反弹（海力士+6.5%、美光+3.4%）将进一步强化明日A股半导体板块的修复预期。但需注意：①地缘冲突仍在升级，油价暴涨可能推升通胀预期压制美联储降息；②22:00美联储主席沃什国会听证会可能释放鹰派信号，是今晚最大变量。
    </div>
</div>
'''

from v3.components.layout import Section
gen._components.append(Section(
    title="🌍 隔夜外盘扫描",
    content=global_market_html,
    icon="globe",
    variant="highlight"
))

# 6. 龙虎榜异常信号
longhubang_html = '''
<div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 14px;">
    <div style="background: linear-gradient(135deg, rgba(34,197,94,0.1) 0%, rgba(22,163,74,0.05) 100%); border-radius: 12px; padding: 16px; border: 1px solid rgba(34,197,94,0.2);">
        <div style="font-size: 15px; font-weight: 700; color: #4ade80; margin-bottom: 12px;">📈 机构净买入TOP5</div>
        <div style="font-size: 12px; color: #cbd5e1; line-height: 2;">
            1. <span style="color: #f1f5f9; font-weight: 600;">沪电股份</span> +5.97亿（涨停，北向+6.39亿）<br>
            2. <span style="color: #f1f5f9; font-weight: 600;">东山精密</span> +4.37亿（涨停，净利增283%）<br>
            3. <span style="color: #f1f5f9; font-weight: 600;">宿迁联盛</span> +3.99亿<br>
            4. <span style="color: #f1f5f9; font-weight: 600;">风华高科</span> +2.06亿（涨停）<br>
            5. 其他机构净买入个股共19只
        </div>
    </div>
    <div style="background: linear-gradient(135deg, rgba(239,68,68,0.1) 0%, rgba(185,28,28,0.05) 100%); border-radius: 12px; padding: 16px; border: 1px solid rgba(239,68,68,0.2);">
        <div style="font-size: 15px; font-weight: 700; color: #f87171; margin-bottom: 12px;">📉 机构净卖出TOP5</div>
        <div style="font-size: 12px; color: #cbd5e1; line-height: 2;">
            1. <span style="color: #f1f5f9; font-weight: 600;">华天科技</span> -14.03亿（成交额210亿，占比6.7%）<br>
            2. <span style="color: #f1f5f9; font-weight: 600;">南亚新材</span> -1.46亿<br>
            3. <span style="color: #f1f5f9; font-weight: 600;">翔鹭钨业</span> -0.74亿<br>
            4. <span style="color: #f1f5f9; font-weight: 600;">凯美特气</span> -0.18亿（跌停）<br>
            5. 其他机构净卖出个股共20只
        </div>
    </div>
</div>
<div style="background: rgba(251,191,36,0.08); border-radius: 12px; padding: 14px; border: 1px solid rgba(251,191,36,0.2); margin-top: 14px;">
    <div style="font-size: 13px; font-weight: 600; color: #fbbf24; margin-bottom: 8px;">⚠️ 龙虎榜关键解读</div>
    <div style="font-size: 12px; color: #fef3c7; line-height: 1.8;">
        • 华天科技机构净卖14.03亿，占当日成交额210亿的6.7%，超过5%阈值，需警惕短期回调风险。封测板块前期涨幅较大，机构获利了结迹象明显。<br>
        • PCB三剑客（沪电+东山+风华）获机构+北向合计净买入超20亿，主线地位确认。<br>
        • 苏州固锝跌停但机构净卖出仅约1700万（占比2%），属于情绪性杀跌，不构成看空信号。
    </div>
</div>
'''

gen._components.append(Section(
    title="🐉 龙虎榜异常信号",
    content=longhubang_html,
    icon="trending-up"
))

# 7. 持仓个股影响分析
portfolio_html = '''
<div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 14px;">
    <div style="background: rgba(255,255,255,0.04); border-radius: 12px; padding: 16px; border: 1px solid rgba(255,255,255,0.08);">
        <div style="display: flex; align-items: center; margin-bottom: 10px;">
            <span style="font-size: 15px; font-weight: 700; color: #f1f5f9;">英维克 (002837)</span>
            <span style="margin-left: auto; padding: 3px 10px; border-radius: 20px; font-size: 11px; font-weight: 600; background: rgba(34,197,94,0.2); color: #4ade80;">液冷散热·利好</span>
        </div>
        <div style="font-size: 12px; color: #94a3b8; line-height: 1.8;">
            影响等级：<span style="color: #4ade80;">正面（偏强）</span><br>
            逻辑：PCB/算力产业链爆发，AI服务器需求持续景气，液冷散热作为配套环节同步受益。今日板块整体反弹，英维克跟随修复。<br>
            操作建议：持有，关注20日均线支撑。若反弹至前高附近可考虑分批减仓锁定利润。
        </div>
    </div>
    <div style="background: rgba(255,255,255,0.04); border-radius: 12px; padding: 16px; border: 1px solid rgba(255,255,255,0.08);">
        <div style="display: flex; align-items: center; margin-bottom: 10px;">
            <span style="font-size: 15px; font-weight: 700; color: #f1f5f9;">铜冠铜箔 (301217)</span>
            <span style="margin-left: auto; padding: 3px 10px; border-radius: 20px; font-size: 11px; font-weight: 600; background: rgba(34,197,94,0.2); color: #4ade80;">PCB上游·强催化</span>
        </div>
        <div style="font-size: 12px; color: #94a3b8; line-height: 1.8;">
            影响等级：<span style="color: #4ade80;">正面（强）</span><br>
            逻辑：PCB涨停潮向上游传导，电子铜箔是CCL/PCB核心原材料。生益科技涨停验证行业景气度，铜箔加工费有望上行。叠加锂电铜箔底部复苏预期，双击逻辑。<br>
            操作建议：持有，若明日PCB板块延续强势，铜冠铜箔有补涨需求。支撑位看60日均线。
        </div>
    </div>
    <div style="background: rgba(255,255,255,0.04); border-radius: 12px; padding: 16px; border: 1px solid rgba(255,255,255,0.08);">
        <div style="display: flex; align-items: center; margin-bottom: 10px;">
            <span style="font-size: 15px; font-weight: 700; color: #f1f5f9;">雅克科技 (002409)</span>
            <span style="margin-left: auto; padding: 3px 10px; border-radius: 20px; font-size: 11px; font-weight: 600; background: rgba(251,191,36,0.2); color: #fbbf24;">存储材料·修复</span>
        </div>
        <div style="font-size: 12px; color: #94a3b8; line-height: 1.8;">
            影响等级：<span style="color: #fbbf24;">中性偏正面</span><br>
            逻辑：SK海力士HBM4量产爬坡+美股存储盘前反弹，存储板块情绪修复。雅克作为半导体材料平台型公司（光刻胶+前驱体+LNG保温），受益存储产业链景气度回升。<br>
            操作建议：持有，华天科技机构大额净卖显示封测板块有获利了结压力，雅克需观察存储板块持续性。
        </div>
    </div>
    <div style="background: rgba(255,255,255,0.04); border-radius: 12px; padding: 16px; border: 1px solid rgba(255,255,255,0.08);">
        <div style="display: flex; align-items: center; margin-bottom: 10px;">
            <span style="font-size: 15px; font-weight: 700; color: #f1f5f9;">*ST建艺 (002789)</span>
            <span style="margin-left: auto; padding: 3px 10px; border-radius: 20px; font-size: 11px; font-weight: 600; background: rgba(148,163,184,0.2); color: #94a3b8;">ST摘帽·无直接影响</span>
        </div>
        <div style="font-size: 12px; color: #94a3b8; line-height: 1.8;">
            影响等级：<span style="color: #94a3b8;">中性</span><br>
            逻辑：央行放水利好基建/装饰板块流动性，但ST股主要看自身摘帽进度。今日无新增公告，继续等待中报及摘帽进展。<br>
            操作建议：持有，严格执行止损纪律。若跌破前期低点需果断减仓。
        </div>
    </div>
</div>
<div style="background: linear-gradient(135deg, rgba(249,115,22,0.1) 0%, rgba(234,88,12,0.05) 100%); border-radius: 12px; padding: 14px; border: 1px solid rgba(249,115,22,0.25); margin-top: 14px;">
    <div style="font-size: 13px; font-weight: 600; color: #fb923c; margin-bottom: 8px;">🏆 持仓股优先级排序（明日操作）</div>
    <div style="font-size: 12px; color: #fed7aa; line-height: 1.8;">
        铜冠铜箔（PCB上游补涨+电子铜箔景气）＞ 英维克（算力链跟涨+液冷）＞ 雅克科技（存储修复观察）＞ *ST建艺（无催化持有）
    </div>
</div>
'''

gen._components.append(Section(
    title="📊 持仓影响与操作建议",
    content=portfolio_html,
    icon="briefcase",
    variant="highlight"
))

# 8. 催化深度分析（Skill增强）
gen.add_catalyst_deep_analysis([
    {
        "title": "PCB业绩爆发潮",
        "type": "产业催化",
        "description": "AI算力PCB产业链业绩全面超预期，多家公司净利翻倍甚至十倍增长，机构资金大举流入",
        "category": "technology",
    },
    {
        "title": "央行5000亿净投放",
        "type": "政策催化",
        "description": "1.4万亿买断式逆回购净投放5000亿，流动性超预期宽松，对冲税期+政府债缴款压力",
        "category": "macro",
    },
    {
        "title": "存储板块修复反弹",
        "type": "外盘映射",
        "description": "SemiAnalysis力挺海力士，HBM4量产爬坡，美股存储盘前集体反弹",
        "category": "technology",
    },
])

# 9. 风险提示
gen.add_risk_warning([
    "地缘冲突升级风险：美伊对峙持续，油价暴涨可能推升通胀预期，压制美联储降息空间",
    "美联储政策风险：今晚22:00沃什国会听证会可能释放鹰派信号，引发美股再次波动",
    "PCB板块追高风险：今日批量涨停后短期涨幅较大，明日可能分化，不宜追高",
    "华天科技机构大额出逃：机构净卖占比6.7%（超5%阈值），封测板块短期承压",
    "业绩预告≠最终业绩：中报预告数据未经审计，正式财报可能存在差异",
    "ST股退市风险：*ST建艺仍存不确定性，严格控制仓位和止损",
])

# 10. 投资策略
gen.add_investment_strategy(
    "【总体策略】三大催化共振，市场情绪底部修复，但仍处于震荡区间，控制仓位5-6成，以业绩为主线择优布局。<br><br>"
    "【主线进攻】PCB/算力产业链是当前最强主线，生益+沪电+东山精密三驾马车齐涨停+机构大额净买确认。操作上不追高，回调至5日均线附近可低吸。铜冠铜箔作为PCB上游补涨标的，可重点关注。<br><br>"
    "【修复观察】存储板块经历连续调整后迎来外盘反弹修复，中期逻辑（HBM4量产+AI需求）未破，但短期情绪仍脆弱。雅克科技持有观察，不急于加仓。<br><br>"
    "【防守配置】油价暴涨背景下，油气/贵金属板块有避险属性，但持续性存疑，不宜追高。消费板块受\"十五五\"规划催化，但弹性弱于科技。<br><br>"
    "【风险控制】严格执行止损纪律，单只个股亏损不超8%。今晚重点关注美联储主席沃什听证会，若释放超预期鹰派信号，需降低仓位应对。"
)

# 发布
result = gen.publish(
    title="⚡ PCB业绩爆发+央行放水+外盘反弹",
    filename="20260714_盘后_S级催化扫描_PCB业绩爆发_央行放水_外盘反弹.html"
)

print("发布结果:", result)
