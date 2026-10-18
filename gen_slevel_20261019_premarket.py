"""
S级催化盘前扫描 - 20261019
核心催化：美股半导体历史性暴跌，SOX连跌8日累计超15%，存储股单周重挫14-18%
类型：风险警示型S级催化
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'v3'))
os.chdir('/root/daily-news-insight')

from v3.generators.s_level_catalyst import SLevelCatalystGenerator

# ====== 初始化生成器 ======
gen = SLevelCatalystGenerator(
    date_str="20261019",
    catalyst_title="美股半导体历史性暴跌：SOX连跌8日蒸发2.3万亿，存储股单周重挫14-18%",
    subtitle="2026.10.19 · 盘前S级风险催化"
)

# ====== 1. 催化事件概述 ======
gen.add_catalyst_overview(
    overview="""
    <b>【S级风险预警】</b>美股半导体板块遭遇2008年以来最猛烈的连续抛售潮。截至美东时间10月16日，
    费城半导体指数(SOX)连续第8个交易日下跌，创2006年以来最长连跌纪录，单日大跌<b>-3.83%</b>，
    自10月7日高点累计跌幅超<b>15%</b>，整个板块市值蒸发近<b>2.3万亿美元</b>。
    <br><br>
    <b>核心导火索</b>：①AI算力租赁公司CoreWeave债务超510亿美元，债券收益率飙升至15%进入垃圾债区间，
    引发市场对AI资本开支可持续性的担忧；②美债收益率持续走高，高估值科技股承压；
    ③油价攀升推升通胀预期，美联储加息预期升温。
    <br><br>
    <b>存储板块重灾区</b>：闪迪单周跌<b>-17.86%</b>、西部数据<b>-16.43%</b>、美光科技<b>-14.59%</b>、
    SK海力士<b>-9.25%</b>，存储成为跌幅最大的子板块。
    <br><br>
    <b>对冲因素</b>：国内政策面持续释放利好（习近平考察算力、国常会深化"人工智能+"、科创板龙头密集回购），
    存储基本面依然坚挺（SK海力士Q3营业利润率78.4%，韩副总理称繁荣至少持续到2027年），
    A股半导体板块具备一定内生韧性，但短期情绪面冲击不可避免。
    """,
    importance="极高"
)

# ====== 2. 催化事件详解 ======
gen.add_catalyst_details(
    background="""
    <b>美股半导体此轮上涨基础</b>：2026年3月底至6月，费城半导体指数上涨逾一倍，新增市值约6.5万亿美元，
    核心驱动力为AI算力需求爆发带动的存储涨价+设备订单超预期。
    <br><br>
    <b>近期抛售背景</b>：
    <ul>
        <li><b>估值高位</b>：SOX指数6月创出历史新高后，半导体板块整体估值处于历史高位区间</li>
        <li><b>利率上行</b>：美国通胀数据反弹，加息预期升温，10年期美债收益率走高压制成长股估值</li>
        <li><b>AI债务担忧</b>：CoreWeave总债务超510亿美元，债券收益率达15%，市场开始质疑AI资本开支的回报率</li>
        <li><b>中期选举临近</b>：美国银行策略师哈特尼特警告未来一个月避险情绪可能升温</li>
        <li><b>获利了结</b>：前期涨幅巨大，做空者7天暴赚320亿美元（约2140亿元人民币）</li>
    </ul>
    <b>VIX波动率指数</b>单周累涨34.7%至19.99，接近担忧情绪上升临界点。
    """,
    trigger="""
    <b>直接触发因素</b>：
    <ol>
        <li><b>CoreWeave债务危机</b>：AI算力租赁龙头总债务超510亿美元（一年前仅150亿），
        公司债券价格大幅下挫，二级市场收益率升至15%进入垃圾债区间，单周股价重挫25.21%</li>
        <li><b>存储股领跌</b>：闪迪、西部数据、美光等存储巨头单周跌14-18%，
        市场担忧存储涨价周期见顶、AI需求不及预期</li>
        <li><b>半导体设备同步下挫</b>：应用材料-4.82%、泛林-4.87%、科磊同步走弱，
        设备板块作为周期先行指标承压明显</li>
        <li><b>纳指重挫</b>：纳指单周跌4.48%，为6月以来最差单周表现</li>
    </ol>
    <b>关键数据</b>：10月7日至15日7个交易日，半导体做空者账面收益约320亿美元。
    美银基金经理调查显示45%受访者认为"AI泡沫将在明年出现"。
    """
)

# ====== 3. 隔夜全球扫描 ======
overnight_html = """
<div style="display: flex; flex-direction: column; gap: 16px;">
    <!-- 指数概览 -->
    <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 12px;">
        <div style="background: rgba(239,68,68,0.1); border-radius: 12px; padding: 16px; text-align: center; border: 1px solid rgba(239,68,68,0.2);">
            <div style="font-size: 11px; color: #fca5a5; margin-bottom: 6px;">SOX费城半导体</div>
            <div style="font-size: 22px; font-weight: 800; color: #ef4444;">-3.83%</div>
            <div style="font-size: 10px; color: #f87171; margin-top: 4px;">11137.29 · 连跌8日</div>
        </div>
        <div style="background: rgba(239,68,68,0.08); border-radius: 12px; padding: 16px; text-align: center; border: 1px solid rgba(239,68,68,0.15);">
            <div style="font-size: 11px; color: #fca5a5; margin-bottom: 6px;">纳斯达克</div>
            <div style="font-size: 22px; font-weight: 800; color: #ef4444;">-2.15%</div>
            <div style="font-size: 10px; color: #f87171; margin-top: 4px;">26140.03 · 单周-4.48%</div>
        </div>
        <div style="background: rgba(245,158,11,0.08); border-radius: 12px; padding: 16px; text-align: center; border: 1px solid rgba(245,158,11,0.15);">
            <div style="font-size: 11px; color: #fcd34d; margin-bottom: 6px;">VIX波动率</div>
            <div style="font-size: 22px; font-weight: 800; color: #f59e0b;">+34.7%</div>
            <div style="font-size: 10px; color: #fbbf24; margin-top: 4px;">19.99 · 接近预警线</div>
        </div>
        <div style="background: rgba(168,85,247,0.08); border-radius: 12px; padding: 16px; text-align: center; border: 1px solid rgba(168,85,247,0.15);">
            <div style="font-size: 11px; color: #c4b5fd; margin-bottom: 6px;">标普500</div>
            <div style="font-size: 22px; font-weight: 800; color: #a855f7;">-1.09%</div>
            <div style="font-size: 10px; color: #c084fc; margin-top: 4px;">7659.44 · 单周-1.95%</div>
        </div>
    </div>
    
    <!-- 半导体个股跌幅 -->
    <div style="background: rgba(255,255,255,0.03); border-radius: 14px; padding: 18px; border: 1px solid rgba(255,255,255,0.06);">
        <div style="font-size: 14px; font-weight: 700; color: #f1f5f9; margin-bottom: 14px; display: flex; align-items: center;">
            <span style="margin-right: 8px;">📉</span> 核心半导体个股表现（周五单日 / 本周累计）
        </div>
        <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 10px;">
            <div style="background: rgba(239,68,68,0.08); padding: 10px 12px; border-radius: 8px; border-left: 3px solid #ef4444;">
                <div style="font-size: 11px; color: #94a3b8;">英伟达 NVDA</div>
                <div style="font-size: 15px; font-weight: 700; color: #ef4444;">-1.43%</div>
                <div style="font-size: 10px; color: #f87171;">单周 -6.61%</div>
            </div>
            <div style="background: rgba(239,68,68,0.1); padding: 10px 12px; border-radius: 8px; border-left: 3px solid #dc2626;">
                <div style="font-size: 11px; color: #94a3b8;">AMD</div>
                <div style="font-size: 15px; font-weight: 700; color: #dc2626;">-5.95%</div>
                <div style="font-size: 10px; color: #f87171;">单周 -13.05%</div>
            </div>
            <div style="background: rgba(239,68,68,0.08); padding: 10px 12px; border-radius: 8px; border-left: 3px solid #ef4444;">
                <div style="font-size: 11px; color: #94a3b8;">美光 MU</div>
                <div style="font-size: 15px; font-weight: 700; color: #ef4444;">-5.63%</div>
                <div style="font-size: 10px; color: #f87171;">单周 -14.59%</div>
            </div>
            <div style="background: rgba(220,38,38,0.12); padding: 10px 12px; border-radius: 8px; border-left: 3px solid #b91c1c;">
                <div style="font-size: 11px; color: #94a3b8;">闪迪 SNDK</div>
                <div style="font-size: 15px; font-weight: 700; color: #b91c1c;">-6%+</div>
                <div style="font-size: 10px; color: #dc2626;">单周 -17.86%</div>
            </div>
            <div style="background: rgba(239,68,68,0.1); padding: 10px 12px; border-radius: 8px; border-left: 3px solid #dc2626;">
                <div style="font-size: 11px; color: #94a3b8;">英特尔 INTC</div>
                <div style="font-size: 15px; font-weight: 700; color: #dc2626;">-5.79%</div>
                <div style="font-size: 10px; color: #f87171;">单周 -14.18%</div>
            </div>
            <div style="background: rgba(239,68,68,0.08); padding: 10px 12px; border-radius: 8px; border-left: 3px solid #ef4444;">
                <div style="font-size: 11px; color: #94a3b8;">应用材料 AMAT</div>
                <div style="font-size: 15px; font-weight: 700; color: #ef4444;">-4.82%</div>
                <div style="font-size: 10px; color: #f87171;">设备板块承压</div>
            </div>
            <div style="background: rgba(239,68,68,0.08); padding: 10px 12px; border-radius: 8px; border-left: 3px solid #ef4444;">
                <div style="font-size: 11px; color: #94a3b8;">泛林 LRCX</div>
                <div style="font-size: 15px; font-weight: 700; color: #ef4444;">-4.87%</div>
                <div style="font-size: 10px; color: #f87171;">设备板块承压</div>
            </div>
            <div style="background: rgba(239,68,68,0.06); padding: 10px 12px; border-radius: 8px; border-left: 3px solid #f87171;">
                <div style="font-size: 11px; color: #94a3b8;">阿斯麦 ASML</div>
                <div style="font-size: 15px; font-weight: 700; color: #f87171;">-0.96%</div>
                <div style="font-size: 10px; color: #fca5a5;">相对抗跌</div>
            </div>
        </div>
    </div>
    
    <!-- 国内政策利好对冲 -->
    <div style="background: rgba(16,185,129,0.06); border-radius: 14px; padding: 18px; border: 1px solid rgba(16,185,129,0.15);">
        <div style="font-size: 14px; font-weight: 700; color: #34d399; margin-bottom: 12px; display: flex; align-items: center;">
            <span style="margin-right: 8px;">🛡️</span> 国内对冲因素：政策+基本面双支撑
        </div>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px;">
            <div>
                <div style="font-size: 12px; font-weight: 600; color: #6ee7b7; margin-bottom: 6px;">📋 政策面</div>
                <ul style="font-size: 12px; color: #94a3b8; line-height: 1.8; margin: 0; padding-left: 16px;">
                    <li>习近平考察乌兰察布算力枢纽，强调算力网是"六张网"之一</li>
                    <li>国常会：深化拓展"人工智能+"行动，促进算电协同</li>
                    <li>央行将算力网纳入PSL抵押补充贷款支持领域</li>
                    <li>《电子信息制造业发展"十五五"规划》发布</li>
                </ul>
            </div>
            <div>
                <div style="font-size: 12px; font-weight: 600; color: #6ee7b7; margin-bottom: 6px;">💰 产业面</div>
                <ul style="font-size: 12px; color: #94a3b8; line-height: 1.8; margin: 0; padding-left: 16px;">
                    <li>长鑫科技前三季度预盈1310-1325亿元，同比扭亏</li>
                    <li>SK海力士Q3营业利润率预计78.4%，机构上修业绩</li>
                    <li>韩副总理：半导体繁荣至少持续到2027年</li>
                    <li>海光/澜起/格科微等科创板龙头密集回购（合计最高16亿）</li>
                </ul>
            </div>
        </div>
    </div>
</div>
"""
from v3.components.layout import Section
gen._components.append(Section(title="🌍 隔夜全球扫描（强制模块）", content=overnight_html, icon="globe"))

# ====== 4. 产业链影响分析 ======
gen.add_industry_chain_analysis(
    upstream=[
        {
            "name": "半导体设备",
            "desc": "应用材料、泛林单日均跌近5%，设备作为周期先行指标承压明显。但国产设备替代逻辑不受海外波动影响，长鑫扩产+中芯扩产持续推进。",
            "stocks": [
                {"code": "688082", "name": "盛美上海", "impact": "中性偏强（在手订单170亿+，国内替代不受影响）"},
                {"code": "002371", "name": "北方华创", "impact": "中性（估值高但订单饱满，短期情绪承压）"},
                {"code": "688300", "name": "拓荆科技", "impact": "中性偏空（薄膜设备估值高，海外情绪传导）"},
            ]
        },
        {
            "name": "半导体材料",
            "desc": "存储景气度短期受情绪冲击，但供需缺口基本面未变。前驱体、光刻胶、电子特气等国产替代逻辑持续。",
            "stocks": [
                {"code": "002409", "name": "雅克科技", "impact": "短期承压（周跌12.55%，持仓股注意风险）"},
                {"code": "688126", "name": "沪硅产业", "impact": "中性偏强（大硅片国产替代刚需）"},
            ]
        },
    ],
    midstream=[
        {
            "name": "存储芯片（核心）",
            "desc": "海外存储股单周暴跌14-18%，但基本面未变：SK海力士Q3营业利润率78.4%，韩副总理称繁荣至少到2027年，2027年供需缺口将比2026年更严重。A股存储龙头长鑫科技业绩强劲。",
            "stocks": [
                {"code": "688825", "name": "长鑫科技", "impact": "强支撑（前三季预盈1310亿+，国产存储旗舰）"},
                {"code": "301217", "name": "铜冠铜箔", "impact": "短期承压（周跌5%，持仓股铜箔属中游材料）"},
            ]
        },
        {
            "name": "先进封装/HBM",
            "desc": "HBM是存储涨价核心驱动力，但短期受整体半导体情绪拖累。三星宣布采用台积电3nm为英伟达生产NVHBM基底裸片，产业格局持续演进。",
            "stocks": [
                {"code": "002156", "name": "通富微电", "impact": "中性偏空（AMD链+封测，海外下跌传导）"},
                {"code": "600584", "name": "长电科技", "impact": "中性（封测龙头，估值相对合理）"},
            ]
        },
        {
            "name": "AI算力芯片",
            "desc": "英伟达相对抗跌（单日-1.43%），但CoreWeave债务危机引发市场对AI资本开支可持续性的担忧。国产算力芯片有独立政策和内需支撑。",
            "stocks": [
                {"code": "688041", "name": "海光信息", "impact": "中性偏强（回购5-8亿+三季报预增38-52%）"},
                {"code": "688256", "name": "寒武纪", "impact": "中性（估值高但国产替代逻辑硬）"},
            ]
        },
    ],
    downstream=[
        {
            "name": "液冷/数据中心",
            "desc": "英维克本周跌12.16%，主力资金净流出3.17亿。短期受AI情绪整体拖累，但液冷行业需求基本面未变，仍是算力基础设施刚需。",
            "stocks": [
                {"code": "002837", "name": "英维克", "impact": "短期承压（持仓股，周跌12.16%，创60日新低）"},
            ]
        },
        {
            "name": "PCB/CCL",
            "desc": "AI服务器PCB需求仍在增长，但短期情绪面受科技股整体下跌影响。生益科技前三季度预增164%-181%。",
            "stocks": [
                {"code": "600183", "name": "生益科技", "impact": "中性偏强（业绩预增164-181%）"},
                {"code": "002463", "name": "沪电股份", "impact": "中性（AI服务器PCB龙头）"},
            ]
        },
    ]
)

# ====== 5. 持仓个股专项分析 ======
portfolio_html = """
<div style="display: flex; flex-direction: column; gap: 14px;">
    <!-- 英维克 -->
    <div style="background: rgba(239,68,68,0.06); border-radius: 14px; padding: 18px; border: 1px solid rgba(239,68,68,0.15); border-left: 4px solid #ef4444;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
            <span style="font-size: 16px; font-weight: 700; color: #f1f5f9;">英维克（002837）· 液冷龙头</span>
            <span style="padding: 3px 10px; background: rgba(239,68,68,0.2); color: #fca5a5; border-radius: 12px; font-size: 11px; font-weight: 700;">
                ⚠️ 短期承压
            </span>
        </div>
        <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 10px; margin-bottom: 12px;">
            <div style="text-align: center;">
                <div style="font-size: 10px; color: #64748b;">最新价</div>
                <div style="font-size: 16px; font-weight: 700; color: #f1f5f9;">44.70</div>
            </div>
            <div style="text-align: center;">
                <div style="font-size: 10px; color: #64748b;">周跌幅</div>
                <div style="font-size: 16px; font-weight: 700; color: #ef4444;">-12.16%</div>
            </div>
            <div style="text-align: center;">
                <div style="font-size: 10px; color: #64748b;">周主力净流出</div>
                <div style="font-size: 16px; font-weight: 700; color: #ef4444;">-3.17亿</div>
            </div>
            <div style="text-align: center;">
                <div style="font-size: 10px; color: #64748b;">动态PE</div>
                <div style="font-size: 16px; font-weight: 700; color: #fbbf24;">154.69</div>
            </div>
        </div>
        <div style="font-size: 12px; color: #94a3b8; line-height: 1.8;">
            <b>判断</b>：本周大跌12.16%，创60日新低，北向资金Q3大幅减仓28.44%。
            短期受美股科技股+AI情绪双重压制，估值154倍PE偏高。
            但液冷行业基本面未变，仍是算力基础设施刚需。股权激励已完成授予，管理层信心仍在。
            <br><b>操作建议</b>：<span style="color: #fbbf24;">底仓持有，不加仓，反弹至50元上方考虑减仓机动仓位。</span>
            关键支撑位40元（前低），跌破则需重新评估。三季报10月27日披露，需关注业绩兑现情况。
        </div>
    </div>
    
    <!-- 铜冠铜箔 -->
    <div style="background: rgba(245,158,11,0.06); border-radius: 14px; padding: 18px; border: 1px solid rgba(245,158,11,0.15); border-left: 4px solid #f59e0b;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
            <span style="font-size: 16px; font-weight: 700; color: #f1f5f9;">铜冠铜箔（301217）· PCB+锂电铜箔</span>
            <span style="padding: 3px 10px; background: rgba(245,158,11,0.2); color: #fcd34d; border-radius: 12px; font-size: 11px; font-weight: 700;">
                ⚠️ 中性偏弱
            </span>
        </div>
        <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 10px; margin-bottom: 12px;">
            <div style="text-align: center;">
                <div style="font-size: 10px; color: #64748b;">最新价</div>
                <div style="font-size: 16px; font-weight: 700; color: #f1f5f9;">85.42</div>
            </div>
            <div style="text-align: center;">
                <div style="font-size: 10px; color: #64748b;">周跌幅</div>
                <div style="font-size: 16px; font-weight: 700; color: #ef4444;">-4.97%</div>
            </div>
            <div style="text-align: center;">
                <div style="font-size: 10px; color: #64748b;">10日主力净流出</div>
                <div style="font-size: 16px; font-weight: 700; color: #ef4444;">-13.08亿</div>
            </div>
            <div style="text-align: center;">
                <div style="font-size: 10px; color: #64748b;">动态PE</div>
                <div style="font-size: 16px; font-weight: 700; color: #fbbf24;">164.78</div>
            </div>
        </div>
        <div style="font-size: 12px; color: #94a3b8; line-height: 1.8;">
            <b>判断</b>：本周跌4.97%，相对抗跌但主力资金持续流出（10日净流出13亿）。
            估值164倍PE偏高，H1业绩同比+514%但基数低。高端HVLP铜箔进展顺利是亮点。
            存储周期下行担忧对PCB铜箔需求预期有压制。
            <br><b>操作建议</b>：<span style="color: #fbbf24;">底仓持有，不追高，80元以下可考虑小幅加仓。</span>
            三季报10月28日披露，是关键验证窗口。若业绩超预期则可能逆势反弹。
        </div>
    </div>
    
    <!-- 雅克科技 -->
    <div style="background: rgba(239,68,68,0.06); border-radius: 14px; padding: 18px; border: 1px solid rgba(239,68,68,0.15); border-left: 4px solid #ef4444;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
            <span style="font-size: 16px; font-weight: 700; color: #f1f5f9;">雅克科技（002409）· 半导体材料</span>
            <span style="padding: 3px 10px; background: rgba(239,68,68,0.2); color: #fca5a5; border-radius: 12px; font-size: 11px; font-weight: 700;">
                ⚠️ 短期承压
            </span>
        </div>
        <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 10px; margin-bottom: 12px;">
            <div style="text-align: center;">
                <div style="font-size: 10px; color: #64748b;">最新价</div>
                <div style="font-size: 16px; font-weight: 700; color: #f1f5f9;">98.01</div>
            </div>
            <div style="text-align: center;">
                <div style="font-size: 10px; color: #64748b;">周跌幅</div>
                <div style="font-size: 16px; font-weight: 700; color: #ef4444;">-12.55%</div>
            </div>
            <div style="text-align: center;">
                <div style="font-size: 10px; color: #64748b;">周主力净流出</div>
                <div style="font-size: 16px; font-weight: 700; color: #ef4444;">-2.36亿</div>
            </div>
            <div style="text-align: center;">
                <div style="font-size: 10px; color: #64748b;">动态PE</div>
                <div style="font-size: 16px; font-weight: 700; color: #34d399;">41.58</div>
            </div>
        </div>
        <div style="font-size: 12px; color: #94a3b8; line-height: 1.8;">
            <b>判断</b>：本周跌12.55%，跌幅较大。PE 41.58倍在半导体材料中相对合理。
            子公司雅睿半导体增资扩股至19亿，电子材料业务持续放量。
            中期分红已实施（10派3.5元），股东户数持续减少（筹码集中）。
            存储跌价担忧对前驱体/光刻胶需求有传导影响，但国产替代逻辑未变。
            <br><b>操作建议</b>：<span style="color: #fbbf24;">底仓持有，90元以下可考虑小幅加仓（PE约38倍）。</span>
            三季报10月28日披露，关注电子材料业务增速是否持续超预期。
            关键支撑位90元，压力位110元。
        </div>
    </div>
    
    <!-- *ST建艺 -->
    <div style="background: rgba(148,163,184,0.06); border-radius: 14px; padding: 18px; border: 1px solid rgba(148,163,184,0.15); border-left: 4px solid #64748b;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
            <span style="font-size: 16px; font-weight: 700; color: #f1f5f9;">*ST建艺（002789）· 装饰工程</span>
            <span style="padding: 3px 10px; background: rgba(148,163,184,0.2); color: #94a3b8; border-radius: 12px; font-size: 11px; font-weight: 700;">
                🟰 无直接关联
            </span>
        </div>
        <div style="font-size: 12px; color: #94a3b8; line-height: 1.8;">
            <b>判断</b>：建筑装饰板块，与半导体/AI无直接关联，受美股科技股暴跌影响极小。
            核心逻辑仍为摘帽预期+基建政策。关注10月27日三季报。
        </div>
    </div>
</div>
"""
gen._components.append(Section(title="📊 持仓个股专项分析（4只）", content=portfolio_html, icon="briefcase", variant="highlight"))

# ====== 6. 投资机会分析 ======
gen.add_investment_opportunities([
    {
        "name": "短期防御：控制仓位，规避高估值弹性品种",
        "priority": "高",
        "logic": "美股半导体8连跌+VIX飙升，短期A股科技板块情绪面冲击不可避免。建议：①整体科技仓位控制在50%以内；②对近一个月涨幅超50%的高弹性品种考虑减仓锁定利润；③现金仓位提升至20%以上，等待恐慌释放后的击球点。",
        "stocks": []
    },
    {
        "name": "中期布局：错杀机会在国产替代+业绩确定性",
        "priority": "中",
        "logic": "此次暴跌主要是海外估值回调+情绪宣泄，国内半导体产业的国产替代逻辑、AI算力的内生增长逻辑并未改变。待情绪稳定后，重点布局：①业绩确定性高的存储产业链（长鑫产业链）；②政策强支持的国产算力芯片（海光信息等回购标的）；③估值合理的设备材料龙头。",
        "stocks": [
            {"code": "688825", "name": "长鑫科技", "impact": "业绩硬支撑，国产存储旗舰"},
            {"code": "688041", "name": "海光信息", "impact": "回购5-8亿+三季报预增38-52%"},
            {"code": "600183", "name": "生益科技", "impact": "业绩预增164-181%，估值合理"},
        ]
    },
    {
        "name": "事件驱动：金融街论坛+LPR公布+三季报窗口",
        "priority": "中",
        "logic": "本周关键事件：①10月19日金融街论坛年会开幕（潘功胜、吴清发声）；②10月20日LPR公布（关注是否降息）；③三季报密集披露期。若有超预期政策或业绩，可能成为反弹催化剂。",
        "stocks": []
    },
    {
        "name": "风险对冲：关注防御性板块",
        "priority": "低",
        "logic": "若科技板块持续调整，资金可能流向防御性板块：医药（创新药+医疗器械）、消费（白酒+食品）、公用事业。但本轮调整大概率是短期情绪宣泄，不建议大规模切换风格。",
        "stocks": []
    },
], view_mode="tab")

# ====== 7. 催化深度分析 ======
gen.add_catalyst_deep_analysis([
    {
        "title": "美股半导体暴跌：情绪宣泄还是周期见顶？",
        "type": "data",
        "description": "SOX指数连续8日下跌，累计跌幅超15%，存储股单周跌14-18%，是短期情绪面回调还是存储周期见顶信号？",
        "category": "存储芯片/半导体"
    },
    {
        "title": "CoreWeave债务危机对AI资本开支的传导影响",
        "type": "policy",
        "description": "CoreWeave总债务超510亿美元，债券收益率升至15%，是否预示AI算力投资的债务驱动模式不可持续？对英伟达、AMD等上游芯片厂的订单影响几何？",
        "category": "AI算力"
    },
    {
        "title": "国内政策+基本面能否独立对冲海外冲击？",
        "type": "meeting",
        "description": "习近平考察算力、国常会深化AI+、科创板龙头密集回购、存储基本面坚挺，国内多重利好能否支撑A股半导体走出独立行情？",
        "category": "A股策略"
    },
])

# ====== 8. 风险提示 ======
gen.add_risk_warning([
    "美股半导体暴跌引发A股科技股情绪面冲击，开盘可能低开",
    "存储板块短期跌幅大，若恐慌情绪蔓延可能进一步下探",
    "美债收益率持续走高+美联储加息预期升温，全球流动性收紧风险",
    "AI资本开支可持续性遭质疑，高估值科技股估值压缩风险",
    "中期选举临近+地缘政治不确定性加剧，避险情绪升温风险"
])

# ====== 9. 投资策略建议 ======
gen.add_investment_strategy("""
<b>【整体策略】防守反击，控制仓位，等待恐慌释放后的击球点</b>
<br><br>
<b>一、仓位管理（优先级最高）</b><br>
• 科技股整体仓位建议控制在50%以内，现金仓位提升至20%+<br>
• 高弹性品种（先进封装设备、HBM材料、AI应用）仓位降至30%以下<br>
• 不建议恐慌性割肉，但也不建议抄底接飞刀，等待明确企稳信号<br><br>

<b>二、持仓操作（4只持仓股逐一说明）</b><br>
• <b>英维克</b>：底仓持有，不补仓。反弹至50元上方考虑减仓机动仓。关键支撑40元，跌破需止损。三季报10/27是关键验证窗口。<br>
• <b>铜冠铜箔</b>：底仓持有，80元以下可考虑小幅加仓（不超过总仓位5%）。三季报10/28若超预期可能逆势反弹。<br>
• <b>雅克科技</b>：底仓持有，90元以下可加仓（PE约38倍，相对合理）。三季报10/28关注电子材料增速。<br>
• <b>*ST建艺</b>：持有观望，与科技板块关联度低，受影响有限。<br><br>

<b>三、关注信号（决定后续操作方向）</b><br>
• 🔴 警惕信号：SOX指数继续下跌破10000点、纳指跌破25000点、VIX突破25<br>
• 🟢 企稳信号：SOX单日反弹超3%且放量、存储股止跌、国内出台超预期刺激政策<br>
• 📅 关键时间：10/20 LPR公布（是否降息）、10/21泛林财报（设备周期验证）、10/28 SK海力士正式财报<br><br>

<b>四、中长期观点（核心逻辑未变）</b><br>
本次暴跌更像是高估值下的获利了结+情绪宣泄，而非产业周期见顶。
存储基本面依然坚挺（SK海力士Q3利润率78.4%，2027年供需缺口更大），
AI算力的中长期增长趋势未变（国内有独立政策和内需支撑）。
待估值消化后，优质龙头将迎来更好的布局机会。
""")

# ====== 发布 ======
print("开始生成S级催化报告...")
result = gen.publish(
    title="S级风险催化：美股半导体历史性暴跌",
    excerpt="SOX连跌8日累计跌超15%，存储股单周重挫14-18%，持仓个股影响分析与操作建议"
)
print(f"发布结果：{result}")
print("报告生成完成！")
