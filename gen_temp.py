import sys, os
sys.path.insert(0, 'v3')
os.chdir('/root/daily-news-insight')
from v3.generators.s_level_catalyst import SLevelCatalystGenerator

gen = SLevelCatalystGenerator(
    date_str="20261007",
    catalyst_title="南亚科DRAM再涨20% + 存储超级周期确认 + 国产算力里程碑",
    subtitle="2026.10.07 · 盘后S级催化【国庆特刊】"
)

# 1. 催化事件概述
gen.add_catalyst_overview(
    "国庆假期最后一天，全球半导体市场迎来三重重磅催化：①南亚科再度上调DRAM合约价最高20%，确认存储超级涨价周期延续；②DeepSeek融资近千亿，计划部署16万颗华为昇腾950DT，国产算力首次进入前沿大模型预训练赛道；③AMD CEO苏姿丰访韩争夺HBM4供应，HBM2027年产能已售罄。叠加纳指/标普再创历史新高，A股节后科技股迎来多重催化。",
    importance="极高"
)

# 2. 催化事件详解
gen.add_catalyst_details(
    background=
    "2026年存储芯片行业正处于AI驱动的超级景气周期中。DRAM/NAND价格自2025年Q3起持续上涨，"
    "已累计涨幅超过150%。HBM（高带宽内存）由于AI算力需求爆发，产能极度紧张，"
    "三星/SK海力士/美光三大厂HBM产能已排至2027年全年，客户开始锁定2028年供应。<br><br>"
    "国产算力方面，华为昇腾在中国AI芯片市场份额已超越英伟达，从2022年的不足5%提升至2026年预计的50%+，"
    "英伟达份额从95%暴跌至8%。DeepSeek V4已完成昇腾适配，并开源全套底层基础设施组件，"
    "国产算力正从推理端向训练端突破。<br><br>"
    "国庆假期期间（10月1-7日），A股休市，但海外市场持续交易。"
    "美股纳指、标普500连续创历史新高，费城半导体指数涨0.34%，"
    "存储板块出现分化（希捷-9%、SK海力士-6%、美光-1.7%），但这更多是短期获利回吐，"
    "存储涨价的产业逻辑并未改变。",
    trigger=
    "<b>催化一：南亚科DRAM合约价再涨20%</b><br>"
    "据台湾经济日报10月7日报道，南亚科近期陆续通知客户再度上调DRAM合约价格，最高涨幅达20%。"
    "南亚科9月合并营收450.91亿新台币，连续11个月创单月历史新高，同比大增576.62%。"
    "这是继三星、SK海力士之后又一存储大厂确认涨价，标志着DRAM超级涨价周期全面确认。<br><br>"
    "<b>催化二：DeepSeek融资近千亿 豪赌国产算力</b><br>"
    "DeepSeek新一轮融资估值逼近1000亿，计划在内蒙古建设大型数据中心，"
    "部署至少16万颗华为昇腾950DT超节点加速器。这将是已知最大规模的华为AI芯片集群，"
    "也是国产算力首次进入前沿大模型预训练赛道，梁文锋称之为\"DeepSeek最大的一场豪赌\"。<br><br>"
    "<b>催化三：AMD CEO苏姿丰访韩 争夺HBM4供应</b><br>"
    "AMD CEO苏姿丰10月7日访问三星电子，与存储部门负责人会谈HBM4供应事宜。"
    "HBM4已开始向MI455和Helios系统出货，HBM3E/HBM4产能已售罄至2027年。"
    "集邦咨询上修明年HBM价格展望，预估综合平均售价年增幅达121%。"
)

# 3. 隔夜外盘跟踪（V4.0强制）
from components.layout import Section, CardGrid, Card
from components.data import StatCard, DataGrid, Badge

global_market_html = '''
<div style="display: flex; flex-direction: column; gap: 16px;">
    <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 12px;">
        <div style="background: linear-gradient(135deg, rgba(34,197,94,0.12) 0%, rgba(22,163,74,0.06) 100%); border-radius: 12px; padding: 16px; border: 1px solid rgba(34,197,94,0.25); text-align: center;">
            <div style="font-size: 12px; color: #86efac; margin-bottom: 4px;">纳斯达克</div>
            <div style="font-size: 20px; font-weight: 800; color: #4ade80;">+0.45%</div>
            <div style="font-size: 11px; color: #64748b;">27,599点 历史新高</div>
        </div>
        <div style="background: linear-gradient(135deg, rgba(34,197,94,0.12) 0%, rgba(22,163,74,0.06) 100%); border-radius: 12px; padding: 16px; border: 1px solid rgba(34,197,94,0.25); text-align: center;">
            <div style="font-size: 12px; color: #86efac; margin-bottom: 4px;">标普500</div>
            <div style="font-size: 20px; font-weight: 800; color: #4ade80;">+0.58%</div>
            <div style="font-size: 11px; color: #64748b;">7,818点 历史新高</div>
        </div>
        <div style="background: linear-gradient(135deg, rgba(34,197,94,0.12) 0%, rgba(22,163,74,0.06) 100%); border-radius: 12px; padding: 16px; border: 1px solid rgba(34,197,94,0.25); text-align: center;">
            <div style="font-size: 12px; color: #86efac; margin-bottom: 4px;">费城半导体</div>
            <div style="font-size: 20px; font-weight: 800; color: #4ade80;">+0.34%</div>
            <div style="font-size: 11px; color: #64748b;">冲高回落 分化加剧</div>
        </div>
        <div style="background: linear-gradient(135deg, rgba(239,68,68,0.12) 0%, rgba(220,38,38,0.06) 100%); border-radius: 12px; padding: 16px; border: 1px solid rgba(239,68,68,0.25); text-align: center;">
            <div style="font-size: 12px; color: #fca5a5; margin-bottom: 4px;">台积电ADR</div>
            <div style="font-size: 20px; font-weight: 800; color: #f87171;">-0.72%</div>
            <div style="font-size: 11px; color: #64748b;">盘前再跌超2%</div>
        </div>
    </div>
    
    <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px;">
        <div style="background: rgba(255,255,255,0.03); border-radius: 12px; padding: 14px; border: 1px solid rgba(255,255,255,0.08);">
            <div style="font-size: 13px; font-weight: 700; color: #f1f5f9; margin-bottom: 10px;">🔴 存储板块（短期回调）</div>
            <div style="font-size: 12px; color: #94a3b8; line-height: 1.8;">
                希捷科技 <span style="color:#f87171;">-9.18%</span><br>
                西部数据 <span style="color:#f87171;">-6.93%</span><br>
                SK海力士 <span style="color:#f87171;">-6.39%</span><br>
                美光科技 <span style="color:#f87171;">-1.73%</span><br>
                <span style="color:#fbbf24; font-size: 11px;">⚠ 短期获利回吐，涨价逻辑未变</span>
            </div>
        </div>
        <div style="background: rgba(255,255,255,0.03); border-radius: 12px; padding: 14px; border: 1px solid rgba(255,255,255,0.08);">
            <div style="font-size: 13px; font-weight: 700; color: #f1f5f9; margin-bottom: 10px;">🟢 AI算力（强者恒强）</div>
            <div style="font-size: 12px; color: #94a3b8; line-height: 1.8;">
                Astera Labs <span style="color:#4ade80;">+7.58%</span><br>
                迈威尔科技 <span style="color:#4ade80;">+5.81%</span><br>
                博通 <span style="color:#4ade80;">+3.67%</span><br>
                AMD <span style="color:#4ade80;">+2.80%</span><br>
                英伟达 <span style="color:#4ade80;">+0.14%</span>
            </div>
        </div>
        <div style="background: rgba(255,255,255,0.03); border-radius: 12px; padding: 14px; border: 1px solid rgba(255,255,255,0.08);">
            <div style="font-size: 13px; font-weight: 700; color: #f1f5f9; margin-bottom: 10px;">📰 隔夜要闻</div>
            <div style="font-size: 12px; color: #94a3b8; line-height: 1.8;">
                ① Constellation Energy <span style="color:#4ade80;">+12.3%</span>（谷歌3.59GW核电合作）<br>
                ② 美光Q4营收542.3亿美元，HBM售罄至2027年<br>
                ③ AMD苏姿丰访韩 争夺HBM4供应<br>
                ④ 台积电ADR盘前跌超2%
            </div>
        </div>
    </div>
    
    <div style="background: linear-gradient(135deg, rgba(59,130,246,0.08) 0%, rgba(139,92,246,0.06) 100%); border-radius: 12px; padding: 14px 18px; border: 1px solid rgba(96,165,250,0.2);">
        <div style="font-size: 13px; font-weight: 700; color: #93c5fd; margin-bottom: 8px;">📊 外盘对A股映射判断</div>
        <div style="font-size: 12px; color: #cbd5e1; line-height: 1.8;">
            <b>正面映射：</b>纳指/标普创新高 → 科技股风险偏好提升；AI算力股普涨 → 算力链情绪提振；Constellation大涨 → AI核电/液冷散热关注度上升<br>
            <b>负面映射：</b>存储板块短期回调 → 国内存储股开盘可能承压；台积电ADR走弱 → 半导体代工链情绪谨慎<br>
            <b>综合判断：</b>整体偏正面，节后A股科技板块有望迎来修复行情，但存储板块需注意短期获利回吐压力
        </div>
    </div>
</div>
'''

gen._components.append(Section(title="🌍 隔夜外盘扫描（强制）", content=global_market_html, icon="globe"))

# 4. 产业链分析
gen.add_industry_chain_analysis(
    upstream=[
        {
            "name": "半导体设备",
            "desc": "光刻机、刻蚀机、薄膜沉积设备等核心设备，存储扩产周期设备需求持续增长",
            "stocks": [
                {"code": "688072", "name": "拓荆科技", "impact": "高"},
                {"code": "688300", "name": "联影医疗", "impact": "中"},
                {"code": "688525", "name": "佰维存储", "impact": "中"}
            ]
        },
        {
            "name": "电子特气/材料",
            "desc": "半导体制程必需的电子特气、光刻胶、CMP材料等，新亚制程拟收购启元气体切入赛道",
            "stocks": [
                {"code": "002388", "name": "新亚制程", "impact": "高(停牌)"},
                {"code": "688268", "name": "华特气体", "impact": "高"},
                {"code": "300054", "name": "鼎龙股份", "impact": "中"}
            ]
        },
    ],
    midstream=[
        {
            "name": "存储芯片设计/制造",
            "desc": "DRAM/NAND/HBM存储芯片，AI驱动量价齐升超级周期，南亚科再涨20%确认涨价延续",
            "stocks": [
                {"code": "603986", "name": "兆易创新", "impact": "极高"},
                {"code": "688525", "name": "佰维存储", "impact": "极高"},
                {"code": "688110", "name": "东芯股份", "impact": "高"},
                {"code": "301308", "name": "江波龙", "impact": "高"}
            ]
        },
        {
            "name": "国产AI算力芯片",
            "desc": "DeepSeek 16万颗昇腾950DT + 华为昇腾份额超50%，国产算力从推理走向训练",
            "stocks": [
                {"code": "688256", "name": "寒武纪", "impact": "极高"},
                {"code": "688041", "name": "海光信息", "impact": "高"},
                {"code": "600410", "name": "华胜天成", "impact": "中"}
            ]
        },
        {
            "name": "HBM/先进封装",
            "desc": "HBM4已出货，产能售罄至2027年，价格年增幅121%，先进封装是关键瓶颈",
            "stocks": [
                {"code": "002156", "name": "通富微电", "impact": "高"},
                {"code": "600584", "name": "长电科技", "impact": "高"},
                {"code": "002409", "name": "雅克科技", "impact": "高"}
            ]
        },
    ],
    downstream=[
        {
            "name": "AI服务器/液冷散热",
            "desc": "AI算力基建加速，液冷散热是刚需，Constellation大涨印证AI能源需求爆发",
            "stocks": [
                {"code": "002837", "name": "英维克", "impact": "极高"},
                {"code": "300896", "name": "爱美客", "impact": "中"},
                {"code": "603019", "name": "中科曙光", "impact": "高"}
            ]
        },
        {
            "name": "PCB/CCL/铜箔",
            "desc": "AI服务器PCB量价齐升，高端HDI/载板需求爆发，铜箔是核心上游材料",
            "stocks": [
                {"code": "301217", "name": "铜冠铜箔", "impact": "高"},
                {"code": "603186", "name": "华正新材", "impact": "中"},
                {"code": "002938", "name": "鹏鼎控股", "impact": "中"}
            ]
        },
    ]
)

# 5. 投资机会分析
gen.add_investment_opportunities([
    {
        "name": "存储芯片涨价主线（最高优先级）",
        "priority": "高",
        "logic": "南亚科DRAM合约价再涨20%，确认存储超级涨价周期延续。集邦咨询上修HBM价格展望至年增121%。"
                 "三大厂HBM产能已售罄至2027年。供给端：美光工会取得罢工权、大厂产能向HBM倾斜挤压传统DRAM供给。"
                 "需求端：AI服务器+消费电子复苏双轮驱动。A股存储标的：兆易创新（NOR+DRAM龙头）、佰维存储（HBM+存储模组）、"
                 "江波龙（企业级存储）、东芯股份（NAND+NOR）。",
        "stocks": [
            {"code": "603986", "name": "兆易创新", "impact": "极高"},
            {"code": "688525", "name": "佰维存储", "impact": "极高"},
            {"code": "301308", "name": "江波龙", "impact": "高"},
            {"code": "688110", "name": "东芯股份", "impact": "高"}
        ]
    },
    {
        "name": "国产算力突破线",
        "priority": "高",
        "logic": "DeepSeek融资近千亿，计划部署16万颗华为昇腾950DT，国产算力首次进入前沿大模型预训练赛道。"
                 "华为昇腾国内份额已超50%，英伟达跌至8%。DeepSeek开源昇腾全套底层基础设施组件，"
                 "国产算力软件栈成熟度快速提升。关注寒武纪（思元系列AI芯片）、海光信息（CPU+DCU双轮驱动）、"
                 "华胜天成（昇腾生态合作伙伴）。",
        "stocks": [
            {"code": "688256", "name": "寒武纪", "impact": "极高"},
            {"code": "688041", "name": "海光信息", "impact": "高"},
            {"code": "600410", "name": "华胜天成", "impact": "中"}
        ]
    },
    {
        "name": "HBM/先进封装产业链",
        "priority": "高",
        "logic": "AMD CEO苏姿丰访韩争夺HBM4供应，HBM3E/HBM4产能售罄至2027年，价格年增121%。"
                 "英伟达要求HBM减薄以加速混合键合技术落地。"
                 "先进封装是HBM产能释放的关键瓶颈。关注通富微电（AMD核心封测伙伴）、"
                 "长电科技（封测龙头）、雅克科技（前驱体+光刻胶）。",
        "stocks": [
            {"code": "002156", "name": "通富微电", "impact": "高"},
            {"code": "600584", "name": "长电科技", "impact": "高"},
            {"code": "002409", "name": "雅克科技", "impact": "高"}
        ]
    },
    {
        "name": "液冷散热（AI能源催化）",
        "priority": "中",
        "logic": "谷歌3.59GW核电合作推动AI能源板块大涨（Constellation +12.3%）。"
                 "AI算力集群热密度持续提升，液冷散热渗透率加速。英维克作为液冷龙头深度受益。"
                 "英伟达Blackwell/ Rubin平台液冷渗透率大幅提升。",
        "stocks": [
            {"code": "002837", "name": "英维克", "impact": "高"},
            {"code": "300896", "name": "申菱环境", "impact": "中"}
        ]
    },
], view_mode="tab")

# 6. 催化深度分析
gen.add_catalyst_deep_analysis([
    {
        "title": "存储芯片超级涨价周期",
        "type": "data",
        "description": "南亚科DRAM合约价再涨20%，HBM年增121%，三大厂产能售罄至2027年，AI驱动量价齐升",
        "category": "存储芯片"
    },
    {
        "title": "国产算力里程碑",
        "type": "policy",
        "description": "DeepSeek 16万颗昇腾950DT+开源全栈，国产算力首次进入前沿大模型预训练赛道",
        "category": "AI算力"
    },
    {
        "title": "节后A股修复行情",
        "type": "meeting",
        "description": "纳指标普创新高+日历效应+科技股估值修复，节后开门红概率高",
        "category": "市场展望"
    },
])

# 7. 持仓相关分析（双重验证）
portfolio_analysis = '''
<div style="display: flex; flex-direction: column; gap: 14px;">
    <div style="background: linear-gradient(135deg, rgba(245,158,11,0.10) 0%, rgba(217,119,6,0.04) 100%); 
                border-radius: 12px; padding: 16px; border: 1px solid rgba(251,191,36,0.25);">
        <div style="font-size: 14px; font-weight: 700; color: #fbbf24; margin-bottom: 10px;">📋 持仓股催化影响评估【假期双重验证】</div>
        <div style="font-size: 12px; color: #cbd5e1; line-height: 1.9;">
            <b>① 英维克(002837) — 利好（液冷+AI能源催化）</b><br>
            · Google 3.59GW核电合作 → AI能耗需求增长 → 液冷散热渗透率加速提升<br>
            · 英伟达Blackwell/Rubin平台液冷渗透率提升 → 英维克作为液冷龙头直接受益<br>
            · 美股Constellation Energy +12.3%印证AI能源主题热度<br>
            <span style="color: #86efac;">✓ 双重验证：谷歌官方公告+多美股AI能源股普涨，逻辑成立</span><br><br>
            
            <b>② 铜冠铜箔(301217) — 偏利好（PCB铜箔+存储扩产）</b><br>
            · 存储芯片涨价周期确认 → 存储厂扩产预期升温 → 锂电铜箔+电子铜箔需求边际改善<br>
            · AI服务器PCB量价齐升 → 高端铜箔需求增长<br>
            · 注意：铜箔板块弹性弱于存储芯片设计/封测，属于间接受益<br>
            <span style="color: #86efac;">✓ 双重验证：南亚科涨价已确认+AI服务器需求景气延续</span><br><br>
            
            <b>③ 雅克科技(002409) — 利好（HBM前驱体+先进封装材料）</b><br>
            · HBM4出货+产能售罄至2027年 → HBM扩产加速 → 前驱体需求增长<br>
            · AMD苏姿丰访韩争夺HBM供应 → HBM扩产确定性进一步提升<br>
            · 存储涨价周期 → 存储厂资本开支扩张 → 半导体材料需求增长<br>
            <span style="color: #86efac;">✓ 双重验证：美光财报HBM售罄确认+AMD/三星HBM合作进展</span><br><br>
            
            <b>④ *ST建艺(002789) — 无直接催化（建筑装饰）</b><br>
            · 科技板块催化对ST建艺无直接影响<br>
            · 注意节后资金回流科技板块可能导致ST股资金分流<br>
            <span style="color: #fca5a5;">⚠ 建议：节后观察资金流向，如科技持续走强可考虑减仓ST换入主线</span>
        </div>
    </div>
    
    <div style="background: linear-gradient(135deg, rgba(239,68,68,0.08) 0%, rgba(220,38,38,0.04) 100%); 
                border-radius: 12px; padding: 16px; border: 1px solid rgba(239,68,68,0.2);">
        <div style="font-size: 14px; font-weight: 700; color: #f87171; margin-bottom: 10px;">⚠️ 空方视角 & 风险点（V4.0强制）</div>
        <div style="font-size: 12px; color: #cbd5e1; line-height: 1.9;">
            <b>1. 存储板块短期回调风险</b><br>
            · 美股存储板块10月6日大幅回调（希捷-9%、SK海力士-6%、美光-1.7%），可能对A股存储股开盘形成压力<br>
            · 市场担忧涨价节奏放缓、需求预期提前透支<br><br>
            
            <b>2. 美债收益率上行压制估值</b><br>
            · 10年期美债收益率突破5.3%，高估值成长股承压<br>
            · 科技股三季度已大幅调整，是否企稳仍需观察<br><br>
            
            <b>3. 国产算力产能瓶颈</b><br>
            · 华为昇腾950DT年底/明年初才规模供货，DeepSeek 16万颗部署周期较长<br>
            · 国产算力软件栈成熟度仍需时间验证，预训练稳定性是关键挑战<br><br>
            
            <b>4. 新亚制程重组不确定性</b><br>
            · 短期涨幅已达95.7%，公司提示情绪过热风险<br>
            · 重组方案尚未确定，审批存在不确定性
        </div>
    </div>
</div>
'''
gen._components.append(Section(title="📊 持仓影响评估 & 空方视角", content=portfolio_analysis, icon="shield-check", variant="highlight"))

# 8. 投资策略
gen.add_investment_strategy(
    "<b>整体判断：</b>国庆假期海外科技股整体偏强，纳指/标普创新高，存储涨价+国产算力+AI能源三重催化叠加，"
    "节后A股科技板块有望迎来修复行情。但需注意美股存储板块短期回调对A股的开盘压力。<br><br>"
    
    "<b>操作策略（节后首周）：</b><br>"
    "1. <b>主线方向：</b>存储芯片＞国产算力＞HBM/先进封装＞液冷散热，优先级从高到低<br>"
    "2. <b>仓位建议：</b>科技成长仓位可从节前防御位（30%）提升至50-60%，分两批建仓<br>"
    "3. <b>买入节奏：</b>首日高开不追高，等回踩确认后再介入；如低开则是较好的左侧买点<br>"
    "4. <b>持仓调整：</b>英维克/雅克科技持有为主，铜冠铜箔可考虑部分换入存储弹性标的，*ST建艺观察资金流向再决定<br><br>"
    
    "<b>重点关注标的：</b><br>"
    "· 存储弹性：兆易创新、佰维存储、江波龙（优先关注回调后低吸机会）<br>"
    "· 国产算力：寒武纪、海光信息（DeepSeek催化直接受益）<br>"
    "· 先进封装：通富微电、长电科技（HBM扩产+AMD合作催化）<br>"
    "· 液冷散热：英维克（AI能源主题+液冷渗透率提升）<br><br>"
    
    "<b>风险控制：</b><br>"
    "· 单一个股仓位不超过总仓位20%<br>"
    "· 如节后首日高开超3%，不追涨，等回踩5日线再考虑<br>"
    "· 设置止损线：跌破前期低点或亏损超8%严格止损"
)

# 9. 风险提示
gen.add_risk_warning([
    "美股存储板块短期回调可能传导至A股，存储股开盘承压",
    "美债收益率持续上行压制科技股估值",
    "国产算力产能释放不及预期，DeepSeek部署进度存不确定性",
    "存储涨价节奏可能低于市场预期，需求端存在波动",
    "新亚制程等重组股短期涨幅过大，警惕情绪退潮风险"
])

# 10. 发布
result = gen.publish(
    title="⚡ S级催化：南亚科DRAM再涨20%+国产算力里程碑+存储超级周期确认【国庆特刊】",
    filename="20261007_盘后_S级催化扫描_存储涨价国产算力.html"
)
print(result)
