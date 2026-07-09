"""
S级催化盘前扫描 - 2026-07-10
核心催化：美光2500亿扩产 + SK海力士ADR今晚上市 + 长鑫申购启动 + 台积电涨价
"""
import sys, os
sys.path.insert(0, 'v3')
os.chdir('/root/daily-news-insight')

from v3.generators.s_level_catalyst import SLevelCatalystGenerator
from v3.components.layout import Section
from v3.components.data import StockTags

gen = SLevelCatalystGenerator(
    date_str="20260710",
    catalyst_title="存储超级周期三重共振 + 台积电先进制程涨价",
    subtitle="2026.07.10 · 盘前S级催化"
)

# ========== 1. 催化概述 ==========
gen.add_catalyst_overview(
    "隔夜全球半导体迎来四大重磅催化共振：①美光宣布2035年前美国投资超2500亿美元新建存储产能，创行业史上最大单笔投资；②SK海力士纳斯达克ADR认购超7倍，今晚（7/10）正式挂牌，募资超280亿美元为半导体史上最大IPO；③长鑫科技确认7月16日科创板申购，上半年净利500-570亿同比增22倍，国产存储龙头正式登陆；④台积电通知客户Q3起7nm及以下制程涨价8-12%，AI/HPC芯片交期延长至26周。费半指数隔夜大涨3.06%收12960点，闪迪+7.6%、AMD+5.67%、应用材料+3.2%、美光+4.5%。存储超级周期从「预期博弈」进入「产能+订单+价格」三重验证阶段，A股存储产业链、半导体设备、先进封装方向迎来S级催化。",
    importance="S级"
)

# ========== 2. 隔夜全球扫描 ==========
global_scan_html = '''
<div style="background: linear-gradient(135deg, rgba(99,102,241,0.1) 0%, rgba(139,92,246,0.08) 100%); 
            border-radius: 14px; padding: 20px; border: 1px solid rgba(139,92,246,0.25);">
    <div style="display: flex; align-items: center; margin-bottom: 16px;">
        <div style="width: 36px; height: 36px; 
                   background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%); 
                   border-radius: 10px; display: flex; align-items: center; justify-content: center; 
                   margin-right: 12px;">
            🌍
        </div>
        <span style="font-size: 16px; font-weight: 700; color: #a78bfa;">隔夜全球半导体扫描</span>
        <span style="margin-left: auto; font-size: 12px; color: #94a3b8;">2026-07-09 美股收盘</span>
    </div>
    
    <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px; margin-bottom: 16px;">
        <div style="background: rgba(34,197,94,0.1); border-radius: 10px; padding: 14px; text-align: center; border: 1px solid rgba(34,197,94,0.25);">
            <div style="font-size: 12px; color: #86efac; margin-bottom: 4px;">费城半导体 SOX</div>
            <div style="font-size: 20px; font-weight: 800; color: #4ade80;">+3.06%</div>
            <div style="font-size: 11px; color: #64748b;">12,960.00</div>
        </div>
        <div style="background: rgba(34,197,94,0.1); border-radius: 10px; padding: 14px; text-align: center; border: 1px solid rgba(34,197,94,0.25);">
            <div style="font-size: 12px; color: #86efac; margin-bottom: 4px;">纳斯达克</div>
            <div style="font-size: 20px; font-weight: 800; color: #4ade80;">+1.30%</div>
            <div style="font-size: 11px; color: #64748b;">26,206.89</div>
        </div>
        <div style="background: rgba(34,197,94,0.1); border-radius: 10px; padding: 14px; text-align: center; border: 1px solid rgba(34,197,94,0.25);">
            <div style="font-size: 12px; color: #86efac; margin-bottom: 4px;">标普500</div>
            <div style="font-size: 20px; font-weight: 800; color: #4ade80;">+0.81%</div>
            <div style="font-size: 11px; color: #64748b;">7,543.64</div>
        </div>
    </div>
    
    <div style="font-size: 13px; color: #cbd5e1; font-weight: 600; margin-bottom: 10px;">📈 核心半导体个股表现</div>
    <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 8px; margin-bottom: 16px;">
        <div style="background: rgba(30,41,59,0.6); border-radius: 8px; padding: 10px; text-align: center;">
            <div style="font-size: 11px; color: #94a3b8;">英伟达 NVDA</div>
            <div style="font-size: 15px; font-weight: 700; color: #4ade80;">+3.65%</div>
        </div>
        <div style="background: rgba(30,41,59,0.6); border-radius: 8px; padding: 10px; text-align: center;">
            <div style="font-size: 11px; color: #94a3b8;">AMD</div>
            <div style="font-size: 15px; font-weight: 700; color: #4ade80;">+5.67%</div>
        </div>
        <div style="background: rgba(30,41,59,0.6); border-radius: 8px; padding: 10px; text-align: center;">
            <div style="font-size: 11px; color: #94a3b8;">美光 MU</div>
            <div style="font-size: 15px; font-weight: 700; color: #4ade80;">+4.5%</div>
        </div>
        <div style="background: rgba(30,41,59,0.6); border-radius: 8px; padding: 10px; text-align: center;">
            <div style="font-size: 11px; color: #94a3b8;">应用材料 AMAT</div>
            <div style="font-size: 15px; font-weight: 700; color: #4ade80;">+3.2%</div>
        </div>
        <div style="background: rgba(30,41,59,0.6); border-radius: 8px; padding: 10px; text-align: center;">
            <div style="font-size: 11px; color: #94a3b8;">闪迪 SNDK</div>
            <div style="font-size: 15px; font-weight: 700; color: #4ade80;">+7.6%</div>
        </div>
        <div style="background: rgba(30,41,59,0.6); border-radius: 8px; padding: 10px; text-align: center;">
            <div style="font-size: 11px; color: #94a3b8;">西部数据 WDC</div>
            <div style="font-size: 15px; font-weight: 700; color: #4ade80;">+5%+</div>
        </div>
        <div style="background: rgba(30,41,59,0.6); border-radius: 8px; padding: 10px; text-align: center;">
            <div style="font-size: 11px; color: #94a3b8;">台积电 TSM</div>
            <div style="font-size: 15px; font-weight: 700; color: #94a3b8;">-0.03%</div>
        </div>
        <div style="background: rgba(30,41,59,0.6); border-radius: 8px; padding: 10px; text-align: center;">
            <div style="font-size: 11px; color: #94a3b8;">日月光 ASX</div>
            <div style="font-size: 15px; font-weight: 700; color: #4ade80;">+8.6%</div>
        </div>
    </div>
    
    <div style="font-size: 13px; color: #cbd5e1; font-weight: 600; margin-bottom: 10px;">🇰🇷 韩国半导体动态</div>
    <div style="background: rgba(30,41,59,0.6); border-radius: 10px; padding: 14px; margin-bottom: 12px;">
        <div style="display: flex; align-items: center; margin-bottom: 8px;">
            <span style="background: linear-gradient(135deg, #3b82f6, #8b5cf6); color: white; font-size: 11px; font-weight: 700; padding: 2px 8px; border-radius: 6px; margin-right: 8px;">重磅</span>
            <span style="color: #e2e8f0; font-size: 13px; font-weight: 600;">SK海力士ADR今晚纳斯达克挂牌，认购超7倍</span>
        </div>
        <div style="color: #94a3b8; font-size: 12px; line-height: 1.7;">
            SK集团会长赴美参加敲钟仪式，将与英伟达、特斯拉等洽谈AI存储合作扩大。募资约280-330亿美元，为半导体史上最大IPO。7/10以when-issued模式交易（代码SKHYV），7/13转为常规交易（SKHY）。韩股今日SK海力士+7%、三星+4%大幅反弹。
        </div>
    </div>
    <div style="background: rgba(30,41,59,0.6); border-radius: 10px; padding: 14px;">
        <div style="display: flex; align-items: center; margin-bottom: 8px;">
            <span style="background: rgba(245,158,11,0.2); color: #fbbf24; font-size: 11px; font-weight: 700; padding: 2px 8px; border-radius: 6px; margin-right: 8px;">关注</span>
            <span style="color: #e2e8f0; font-size: 13px; font-weight: 600;">三星Q2利润89.4万亿韩元创历史新高，超越英伟达同期</span>
        </div>
        <div style="color: #94a3b8; font-size: 12px; line-height: 1.7;">
            二季度营业利润同比增18.1倍达584亿美元，存储贡献七成以上盈利增量。但韩股出现"买预期卖事实"，7/8三星跌6.25%、SK海力士跌5.68%，7/9双双大幅反弹。外资从存储龙头转向AI半导体价值链标的。
        </div>
    </div>
</div>
'''

gen._components.append(Section(title="🌍 隔夜全球扫描", content=global_scan_html, icon="globe", variant="highlight"))

# ========== 3. 催化详解 ==========
gen.add_catalyst_details(
    background="""全球AI算力扩张推动存储芯片进入历史性超级周期。三大核心变量叠加：
    <br><br>
    <b>① 需求端爆发</b>：单台AI训练服务器DRAM容量为传统服务器的10倍，NAND用量达3倍以上。2026年AI相关DRAM需求占行业总需求比重突破53%，算力大模型存储读写需求每半年翻倍。
    <br><br>
    <b>② 供给端紧缺</b>：三大原厂（三星、SK海力士、美光）将80%以上先进制程产能倾斜给HBM、高端DDR5，消费级通用存储产能持续收缩。Jefferies预测2026Q3 DRAM合约价环比涨40-50%，Q4继续涨30-40%。
    <br><br>
    <b>③ 国产替代窗口</b>：长鑫科技、长江存储两大国产龙头加速推进IPO，国内存储产业链自主可控进程加快。长鑫上半年净利500-570亿同比增22倍，国产DRAM技术已达国际先进水平。
    <br><br>
    产业共识：海外新建芯片工厂建设周期普遍8-10年，当下宣布的万亿级扩产规划产能落地集中在2028年后，<b>短期市场紧缺格局不会改变，高端存储长期维持高景气</b>。""",
    trigger="""隔夜四大催化同步落地，形成共振效应：
    <br><br>
    <b>🔥 美光2500亿美元扩产</b>：2035年前在美国新建多座存储工厂，满足AI热潮带动的内存芯片需求。确认行业资本开支进入新一轮上行周期，<b>半导体设备产业链直接受益</b>。
    <br><br>
    <b>🔥 SK海力士ADR超7倍认购</b>：全球顶级AI基金疯抢，今晚（7/10）纳斯达克挂牌。验证AI存储龙头的全球资金认可度，<b>有望为A股存储板块打开估值天花板</b>。
    <br><br>
    <b>🔥 长鑫科技7/16科创板申购</b>：国产DRAM龙头正式登陆A股，募资295亿扩产+HBM前瞻研发。上半年营收1100-1200亿、净利500-570亿，<b>将成为A股存储产业链核心标的和估值锚</b>。
    <br><br>
    <b>🔥 台积电7nm以下涨价8-12%</b>：AI芯片交期延长至26周（较Q1延长7周），先进制程产能紧张持续升级。<b>国产替代逻辑进一步强化</b>。"""
)

# ========== 4. 产业链分析 ==========
gen.add_industry_chain_analysis(
    upstream=[
        {"name": "半导体设备", "impact": "美光2500亿+长鑫扩产+三星SK扩产，全球存储资本开支进入超级周期。单座存储晶圆厂超七成资本开支流向设备，刻蚀、薄膜、清洗设备率先受益。", "stocks": ["中微公司", "北方华创", "华海清科", "芯源微"]},
        {"name": "存储材料", "impact": "HBM前驱体、电子特气、抛光液、硅片等核心材料需求随产能扩张同步放量，国产替代加速。雅克科技（HBM前驱体全球龙头）直接受益。", "stocks": ["雅克科技", "安集科技", "鼎龙股份", "沪硅产业"]},
        {"name": "半导体零部件", "impact": "扩产周期下精密零部件需求激增，本土配套厂商导入验证节奏加快。", "stocks": ["富创精密", "新莱应材", "正帆科技"]},
    ],
    midstream=[
        {"name": "存储芯片设计/制造", "impact": "长鑫科技IPO启动，国产DRAM龙头登陆科创板，将成为A股存储板块核心锚。存储涨价周期中，具备产能的厂商盈利弹性最大。", "stocks": ["兆易创新", "北京君正", "澜起科技", "长鑫科技(待上市)"]},
        {"name": "先进封装", "impact": "HBM需要CoWoS/2.5D先进封装配套，台积电CoWoS产能持续紧张。日月光+8.6%领涨封测板块。", "stocks": ["长电科技", "通富微电", "华天科技", "甬矽电子"]},
        {"name": "存储封测/模组", "impact": "存储芯片封测需求随产能扩张同步增长，DDR5/HBM封测技术升级带来价值量提升。", "stocks": ["深科技", "江波龙", "佰维存储"]},
    ],
    downstream=[
        {"name": "AI服务器/算力", "impact": "存储涨价传导至AI服务器成本端，但供给紧张说明需求依然强劲。拥有供应链保障的头部厂商更具竞争优势。", "stocks": ["工业富联", "浪潮信息", "中科曙光"]},
        {"name": "液冷散热", "impact": "AI算力扩张+存储密度提升，单机柜热密度持续攀升，液冷成为刚需。英维克等液冷龙头间接受益。", "stocks": ["英维克", "申菱环境", "高澜股份"]},
        {"name": "半导体测试", "impact": "产能扩张带动测试设备和探针卡需求，CPO光电同步测试成为新增长点。", "stocks": ["华峰测控", "长川科技", "精测电子"]},
    ]
)

# ========== 5. 投资机会 ==========
gen.add_investment_opportunities([
    {
        "title": "🏆 S级：HBM前驱体 + 存储材料龙头",
        "confidence": "高",
        "target": "雅克科技 002409",
        "logic": "HBM前驱体全球龙头，深度绑定SK海力士、美光、长鑫三大客户。SK海力士ADR上市+美光扩产+长鑫IPO三重催化叠加。昨日已涨停创历史新高（209元），趋势明确。",
        "action": "趋势持有为主，215-220区间可减1/3锁利，200元以上维持半仓，跌破200止盈至底仓"
    },
    {
        "title": "🥇 A级：半导体设备国产替代",
        "confidence": "高",
        "target": "中微公司、北方华创、华海清科",
        "logic": "美光2500亿+长鑫扩产+台积电涨价确认全球半导体设备超级周期。国产替代+自主可控是中长期主线。昨日中微+11%、华海清科+16%已有表现，板块热度高。",
        "action": "回调即介入机会，关注中微公司（刻蚀龙头）、华海清科（CMP龙头）弹性品种"
    },
    {
        "title": "🥈 B级：铜箔/CCL - 存储产业链上游",
        "confidence": "中",
        "target": "铜冠铜箔 301217",
        "logic": "存储芯片封装载板用高端铜箔需求增长，国产替代空间大。前期涨幅较大+机构兑现，短期处于高位震荡。昨日探底130后V反收139.68，140-145为压力位。",
        "action": "140-145区间继续减仓至1/3底仓锁利，放量突破145可留仓博弈新高，破135止盈离场"
    },
    {
        "title": "⚠️ 观察级：液冷散热 - 间接受益",
        "confidence": "中",
        "target": "英维克 002837",
        "logic": "存储芯片功耗提升间接拉动液冷需求，但公司基本面仍在调整期。昨日探底68.24后V反收75.87，短期反弹但中期趋势未改。",
        "action": "75-78元坚决减仓≥1/2，80元以上清仓，破70无条件止损，严禁补仓"
    },
])

# ========== 6. 催化深度分析 ==========
gen.add_catalyst_deep_analysis([
    {
        "title": "美光2500亿扩产 + SK海力士ADR上市",
        "type": "industry",
        "description": "全球存储双雄同步释放重磅信号：美光创行业最大单笔投资，SK海力士登陆全球最大资本市场，共同确认存储超级周期延续性",
        "category": "产业催化",
    },
    {
        "title": "长鑫科技科创板IPO + 台积电先进制程涨价",
        "type": "policy",
        "description": "国产存储龙头上市强化自主可控主线，台积电涨价确认先进制程供需紧张格局，半导体设备材料全产业链受益",
        "category": "资本运作+产业",
    },
])

# ========== 7. 持仓操作建议 ==========
holding_tags = StockTags([
    {"code": "002409", "name": "雅克科技", "impact": "HBM前驱体龙头 · S级利好 · 趋势持有"},
    {"code": "301217", "name": "铜冠铜箔", "impact": "存储上游 · 高位减仓"},
    {"code": "002837", "name": "英维克", "impact": "液冷间接受益 · 反弹减仓"},
    {"code": "002789", "name": "*ST建艺", "impact": "退市风险 · 立即清仓"},
])

strategy_html = f'''
<div style="margin-bottom: 16px;">
    <div style="font-size: 13px; color: #94a3b8; margin-bottom: 10px;">持仓标的影响评估</div>
    {holding_tags.render()}
</div>

<div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 12px;">
    <div style="background: linear-gradient(135deg, rgba(34,197,94,0.12) 0%, rgba(22,163,74,0.08) 100%); 
                border-radius: 12px; padding: 16px; border: 1px solid rgba(34,197,94,0.3);">
        <div style="display: flex; align-items: center; margin-bottom: 10px;">
            <span style="font-size: 15px; font-weight: 800; color: #4ade80;">雅克科技 002409</span>
            <span style="margin-left: auto; background: rgba(34,197,94,0.2); color: #4ade80; font-size: 11px; font-weight: 700; padding: 3px 8px; border-radius: 6px;">S级利好</span>
        </div>
        <div style="color: #94a3b8; font-size: 12px; margin-bottom: 8px;">最新价：209.00元（涨停）｜浮盈：+92.1%｜成本：108.8元</div>
        <div style="color: #e2e8f0; font-size: 13px; line-height: 1.7;">
            <b>核心逻辑：</b>HBM前驱体全球龙头，美光+SK海力士+长鑫三重客户催化叠加。昨日涨停创历史新高，封单9.73亿，主力净流入+5.87亿，趋势明确。<br>
            <b>操作建议：</b>趋势牛股不轻易下车。215-220减1/3锁利，200元以上维持半仓，跌破200止盈至底仓。<b>估值锚：</b>2026年PE约35-40x（存储材料龙头溢价），目标价区间230-260元。
        </div>
    </div>
    
    <div style="background: linear-gradient(135deg, rgba(245,158,11,0.12) 0%, rgba(217,119,6,0.08) 100%); 
                border-radius: 12px; padding: 16px; border: 1px solid rgba(245,158,11,0.3);">
        <div style="display: flex; align-items: center; margin-bottom: 10px;">
            <span style="font-size: 15px; font-weight: 800; color: #fbbf24;">铜冠铜箔 301217</span>
            <span style="margin-left: auto; background: rgba(245,158,11,0.2); color: #fbbf24; font-size: 11px; font-weight: 700; padding: 3px 8px; border-radius: 6px;">谨慎乐观</span>
        </div>
        <div style="color: #94a3b8; font-size: 12px; margin-bottom: 8px;">最新价：139.68元｜浮盈：+60.3%｜成本：87.16元</div>
        <div style="color: #e2e8f0; font-size: 13px; line-height: 1.7;">
            <b>核心逻辑：</b>锂电铜箔+电子铜箔双主业，存储封装载板用高端铜箔间接受益。前期涨幅巨大+机构近5日净流出15.27亿，高位震荡格局。昨日探底V反说明有承接。<br>
            <b>操作建议：</b>140-145元减仓至1/3底仓锁定利润（已达-60%仓位建议）。放量突破145可留仓博弈新高，破135止盈离场。<b>估值锚：</b>2026年PE约25-30x，合理区间120-150元。
        </div>
    </div>
    
    <div style="background: linear-gradient(135deg, rgba(239,68,68,0.12) 0%, rgba(220,38,38,0.08) 100%); 
                border-radius: 12px; padding: 16px; border: 1px solid rgba(239,68,68,0.3);">
        <div style="display: flex; align-items: center; margin-bottom: 10px;">
            <span style="font-size: 15px; font-weight: 800; color: #f87171;">英维克 002837</span>
            <span style="margin-left: auto; background: rgba(239,68,68,0.2); color: #f87171; font-size: 11px; font-weight: 700; padding: 3px 8px; border-radius: 6px;">深度破止损</span>
        </div>
        <div style="color: #94a3b8; font-size: 12px; margin-bottom: 8px;">最新价：75.87元｜浮亏：-27.2%｜成本：104.23元</div>
        <div style="color: #e2e8f0; font-size: 13px; line-height: 1.7;">
            <b>核心逻辑：</b>液冷龙头但AI液冷订单兑现不及预期，业绩增速放缓+估值高。存储板块间接受益但非直接逻辑。昨日探底V反+5.2%，短期反弹但中期下降趋势未改。<br>
            <b>操作建议：</b>75-78元区间坚决减仓≥1/2（双重验证：深度破止损-27%+中期流出趋势未改+反弹至压力位），80元以上清仓，破70无条件止损，严禁补仓。
        </div>
    </div>
    
    <div style="background: linear-gradient(135deg, rgba(239,68,68,0.15) 0%, rgba(185,28,28,0.1) 100%); 
                border-radius: 12px; padding: 16px; border: 1px solid rgba(239,68,68,0.4);">
        <div style="display: flex; align-items: center; margin-bottom: 10px;">
            <span style="font-size: 15px; font-weight: 800; color: #ef4444;">*ST建艺 002789</span>
            <span style="margin-left: auto; background: rgba(239,68,68,0.3); color: #fca5a5; font-size: 11px; font-weight: 700; padding: 3px 8px; border-radius: 6px;">🚨 立即清仓</span>
        </div>
        <div style="color: #94a3b8; font-size: 12px; margin-bottom: 8px;">最新价：10.38元｜浮亏：-22.8%｜成本：~13.45元</div>
        <div style="color: #e2e8f0; font-size: 13px; line-height: 1.7;">
            <b>核心逻辑：</b>退市风险+诉讼+债务问题三大雷未解，与今日存储催化完全无关。成交萎缩至2114万，资金关注度极低。<br>
            <b>操作建议：</b><b>开盘任何价格立即清仓（最高优先级）</b>，退市风险股绝不恋战。任何反弹都是逃命机会，10元以下更难出手！
        </div>
    </div>
</div>

<div style="margin-top: 16px; background: rgba(30,41,59,0.6); border-radius: 10px; padding: 14px; border-left: 4px solid #3b82f6;">
    <div style="color: #60a5fa; font-size: 13px; font-weight: 700; margin-bottom: 6px;">📊 整体仓位建议</div>
    <div style="color: #cbd5e1; font-size: 13px; line-height: 1.8;">
        今日存储+半导体设备是最强主线，但考虑到前期涨幅巨大+半年报窗口临近，建议整体仓位维持<b>4-5成</b>，以雅克科技为主仓（趋势未破），其余逢高减仓降仓位。<b>严禁追高</b>，回调再介入。重点关注开盘后雅克科技能否高开高走确认趋势延续性。
    </div>
</div>
'''

gen._components.append(Section(title="💼 持仓操作指引", content=strategy_html, icon="briefcase", variant="highlight"))

# ========== 8. 风险提示 ==========
gen.add_risk_warning([
    "存储板块前期涨幅巨大，存在利好兑现后的获利回吐风险，尤其注意高位股追高风险",
    "美伊冲突升级可能导致全球市场风险偏好下降，原油暴涨推升通胀预期，美联储加息压力增大",
    "美国反垄断诉讼指控三星、SK海力士、美光协同限制产能，若进展超预期可能影响涨价逻辑",
    "半年报窗口临近，部分高位题材股可能面临业绩证伪风险，注意规避纯题材无业绩标的",
    "本报告仅供参考，不构成投资建议。投资有风险，入市需谨慎。"
])

# ========== 9. 发布 ==========
print("开始生成并发布报告...")
result = gen.publish(
    title="存储超级周期三重共振 + 台积电涨价",
    excerpt="美光2500亿扩产+SK海力士ADR超7倍认购+长鑫申购启动+台积电先进制程涨价，费半大涨3.06%，存储超级周期确认"
)
print(f"发布结果：{result}")
