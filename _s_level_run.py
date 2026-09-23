import sys, os
sys.path.insert(0, '/root/daily-news-insight/v3')
os.chdir('/root/daily-news-insight')

from v3.generators.s_level_catalyst import SLevelCatalystGenerator

gen = SLevelCatalystGenerator(
    date_str="20260924",
    catalyst_title="台积电2027年涨价3-6%+6G十五五规划双催化",
    subtitle="2026.09.24 · 盘前S级催化扫描"
)

overview_text = (
    "隔夜两大催化同时落地：<strong>①台积电确定2027年1月上调晶圆代工价格3%-6%</strong>，先进制程涨幅更高，"
    "8寸厂产能利用率超100%，45nm以下满载，订单能见度延伸至2030年；"
    "<strong>②工信部发布《信息通信行业发展\"十五五\"规划》</strong>，明确适时启动6G商用、"
    "智能算力规模增至9800EFLOPS（增长5倍+）、新建算力设施PUE降至1.2以下。"
    "美股方面，费城半导体指数跌2.01%，存储板块领跌（闪迪-3.96%、SK海力士-3.61%、美光-2.69%），"
    "主因\"大空头\"Burry加码做空美光+美联储10月加息概率飙升至68.6%（PMI超预期）。"
    "综合评级：<strong>台积电涨价为产业层面S级利好</strong>，国产替代+先进封装+半导体材料直接受益；"
    "6G/算力规划为中长期政策催化；美股回调形成短期情绪扰动。"
)
gen.add_catalyst_overview(overview_text)

from components.layout import Section

overnight_html = '''
<div style="display: flex; flex-direction: column; gap: 12px;">
    <div style="background: linear-gradient(135deg, rgba(239,68,68,0.12) 0%, rgba(185,28,28,0.06) 100%); 
                border-radius: 14px; padding: 18px; border: 1px solid rgba(248,113,113,0.25);">
        <div style="display: flex; align-items: center; margin-bottom: 14px;">
            <div style="width: 36px; height: 36px; background: linear-gradient(135deg, #ef4444 0%, #b91c1c 100%); 
                       border-radius: 10px; display: flex; align-items: center; justify-content: center; margin-right: 12px;">
                🇺🇸
            </div>
            <span style="font-size: 16px; font-weight: 700; color: #fca5a5;">美股半导体 · 全线回调</span>
            <span style="margin-left: auto; font-size: 12px; color: #fca5a5; background: rgba(239,68,68,0.15); 
                       padding: 4px 10px; border-radius: 20px; font-weight: 600;">9月23日收盘</span>
        </div>
        <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 10px;">
            <div style="background: rgba(255,255,255,0.04); border-radius: 10px; padding: 12px; text-align: center;">
                <div style="font-size: 11px; color: #94a3b8; margin-bottom: 4px;">费城半导体</div>
                <div style="font-size: 16px; font-weight: 700; color: #f87171;">-2.01%</div>
                <div style="font-size: 10px; color: #64748b;">12,434点</div>
            </div>
            <div style="background: rgba(255,255,255,0.04); border-radius: 10px; padding: 12px; text-align: center;">
                <div style="font-size: 11px; color: #94a3b8; margin-bottom: 4px;">英伟达 NVDA</div>
                <div style="font-size: 16px; font-weight: 700; color: #f87171;">-1.47%</div>
                <div style="font-size: 10px; color: #64748b;">$225.51</div>
            </div>
            <div style="background: rgba(255,255,255,0.04); border-radius: 10px; padding: 12px; text-align: center;">
                <div style="font-size: 11px; color: #94a3b8; margin-bottom: 4px;">AMD</div>
                <div style="font-size: 16px; font-weight: 700; color: #f87171;">-1.54%</div>
                <div style="font-size: 10px; color: #64748b;">$614.16</div>
            </div>
            <div style="background: rgba(255,255,255,0.04); border-radius: 10px; padding: 12px; text-align: center;">
                <div style="font-size: 11px; color: #94a3b8; margin-bottom: 4px;">博通 AVGO</div>
                <div style="font-size: 16px; font-weight: 700; color: #f87171;">-2.62%</div>
                <div style="font-size: 10px; color: #64748b;">设备领跌</div>
            </div>
        </div>
    </div>
    
    <div style="background: linear-gradient(135deg, rgba(245,158,11,0.12) 0%, rgba(180,83,9,0.06) 100%); 
                border-radius: 14px; padding: 18px; border: 1px solid rgba(251,191,36,0.25);">
        <div style="display: flex; align-items: center; margin-bottom: 14px;">
            <div style="width: 36px; height: 36px; background: linear-gradient(135deg, #f59e0b 0%, #b45309 100%); 
                       border-radius: 10px; display: flex; align-items: center; justify-content: center; margin-right: 12px;">
                💾
            </div>
            <span style="font-size: 16px; font-weight: 700; color: #fcd34d;">存储芯片 · 领跌大盘</span>
            <span style="margin-left: auto; font-size: 12px; color: #f87171; background: rgba(239,68,68,0.15); 
                       padding: 4px 10px; border-radius: 20px; font-weight: 600;">Burry加码做空</span>
        </div>
        <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 10px;">
            <div style="background: rgba(255,255,255,0.04); border-radius: 10px; padding: 12px; text-align: center;">
                <div style="font-size: 11px; color: #94a3b8; margin-bottom: 4px;">闪迪 SNDK</div>
                <div style="font-size: 16px; font-weight: 700; color: #f87171;">-3.96%</div>
                <div style="font-size: 10px; color: #64748b;">NAND龙头</div>
            </div>
            <div style="background: rgba(255,255,255,0.04); border-radius: 10px; padding: 12px; text-align: center;">
                <div style="font-size: 11px; color: #94a3b8; margin-bottom: 4px;">SK海力士</div>
                <div style="font-size: 16px; font-weight: 700; color: #f87171;">-3.61%</div>
                <div style="font-size: 10px; color: #64748b;">HBM龙头</div>
            </div>
            <div style="background: rgba(255,255,255,0.04); border-radius: 10px; padding: 12px; text-align: center;">
                <div style="font-size: 11px; color: #94a3b8; margin-bottom: 4px;">美光 MU</div>
                <div style="font-size: 16px; font-weight: 700; color: #f87171;">-2.69%</div>
                <div style="font-size: 10px; color: #64748b;">DRAM龙头</div>
            </div>
            <div style="background: rgba(255,255,255,0.04); border-radius: 10px; padding: 12px; text-align: center;">
                <div style="font-size: 11px; color: #94a3b8; margin-bottom: 4px;">泛林 LRCX</div>
                <div style="font-size: 16px; font-weight: 700; color: #f87171;">-3%+</div>
                <div style="font-size: 10px; color: #64748b;">设备龙头</div>
            </div>
        </div>
        <div style="margin-top: 10px; font-size: 12px; color: #94a3b8; line-height: 1.6;">
            ⚠️ 催化因素："大空头"Michael Burry加码做空美光+Nebius，押注内存供应增加价格承压；
            美国9月PMI初值58.4（62个月高位），美联储10月加息概率从53%飙升至68.6%
        </div>
    </div>
    
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px;">
        <div style="background: linear-gradient(135deg, rgba(59,130,246,0.12) 0%, rgba(37,99,235,0.06) 100%); 
                    border-radius: 14px; padding: 16px; border: 1px solid rgba(96,165,250,0.25);">
            <div style="display: flex; align-items: center; margin-bottom: 10px;">
                <span style="font-size: 14px; font-weight: 700; color: #60a5fa;">🇰🇷 韩国半导体</span>
            </div>
            <div style="font-size: 12px; color: #cbd5e1; line-height: 1.7;">
                • 高盛重申SK海力士买入评级，目标价350万韩元<br>
                • HBM价格下半年持续走高，HBM4占比Q4提升<br>
                • 产能接近满载，龙仁厂2027年2月开幕<br>
                • LTA长期协议覆盖率有望达50%+
            </div>
        </div>
        <div style="background: linear-gradient(135deg, rgba(16,185,129,0.12) 0%, rgba(5,150,105,0.06) 100%); 
                    border-radius: 14px; padding: 16px; border: 1px solid rgba(52,211,153,0.25);">
            <div style="display: flex; align-items: center; margin-bottom: 10px;">
                <span style="font-size: 14px; font-weight: 700; color: #34d399;">🇨🇳 国内政策</span>
            </div>
            <div style="font-size: 12px; color: #cbd5e1; line-height: 1.7;">
                • 工信部"十五五"规划：适时启动6G商用<br>
                • 智能算力规模从1590→9800 EFLOPS<br>
                • 新建算力设施PUE降至1.2以下<br>
                • 首提"智能体互联网络"概念
            </div>
        </div>
    </div>
</div>
'''

gen._components.append(Section(title="🌍 隔夜全球扫描", content=overnight_html, icon="globe"))

# 催化详解
background_text = (
    "<strong>台积电涨价背景：</strong>AI算力需求持续爆发，从GPU、ASIC扩散至PMIC、MCU、功率器件、驱动IC、光通信芯片等全品类，"
    "带动晶圆代工产能全面吃紧。台积电2nm/3nm先进制程供不应求，CoWoS先进封装产能持续紧张，订单能见度已延伸至2030年。"
    "同时海外建厂成本是本土的4-5倍，2nm量产爬坡将使2026H2毛利率承压3-4个百分点。<br><br>"
    "<strong>6G十五五规划背景：</strong>《信息通信行业发展\"十五五\"规划》正式发布，锚定2030年全面建成新一代通信网。"
    "核心指标：智能算力规模从1590 EFLOPS增至9800 EFLOPS（+516%），5G用户普及率95%，千兆宽带用户3.2亿户，"
    "新建大型超大型算力设施PUE降至1.2以下。首次提出\"智能体互联网络\"概念。"
)
trigger_text = (
    "<strong>台积电涨价触发（凌晨3:30）：</strong>供应链人士确认台积电2027年1月起上调Wafer Out报价3%-6%，"
    "2nm/3nm等先进制程涨幅更高。8寸厂产能利用率超100%，45nm以下制程满载。联电、力积电等同业已宣布跟进涨价策略。<br><br>"
    "<strong>政策催化触发（9月23日）：</strong>工信部副部长余晓晖在2026中国国际信息通信展览会开幕式上明确"
    "加快6G核心技术攻关、推动算力设施扩容提质、强化算网协同。ION-2030智能光网络推进组成立。<br><br>"
    "<strong>美股回调触发：</strong>美国9月综合PMI初值58.4（62个月高位），制造业PMI 57.0（52个月高点），"
    "CME美联储观察工具显示10月加息概率从53%飙升至68.6%。"
)
gen.add_catalyst_details(background_text, trigger_text)

# 产业链
gen.add_industry_chain_analysis(
    upstream=[
        {
            "name": "半导体材料",
            "desc": "晶圆代工涨价传导至上游材料端，光刻胶、前驱体、电子特气、CMP抛光液等需求量价齐升，国产替代加速",
            "stocks": [
                {"code": "002409", "name": "雅克科技", "impact": "前驱体+光刻胶双龙头"},
                {"code": "688519", "name": "南大光电", "impact": "电子特气+光刻胶"},
                {"code": "300655", "name": "晶瑞电材", "impact": "光刻胶+电子化学品"},
            ]
        },
        {
            "name": "半导体设备",
            "desc": "产能紧张推动晶圆厂扩产，设备采购周期上行，国产替代是核心主线，刻蚀/薄膜/量测设备受益最直接",
            "stocks": [
                {"code": "688012", "name": "中微公司", "impact": "刻蚀设备龙头"},
                {"code": "002371", "name": "北方华创", "impact": "平台型设备龙头"},
                {"code": "688082", "name": "盛美上海", "impact": "清洗/电镀设备"},
            ]
        },
    ],
    midstream=[
        {
            "name": "晶圆代工（核心）",
            "desc": "台积电涨价确认行业景气度，中芯国际产能利用率93.7%接近满产，Q3预计维持95%高位，已协商上调定价",
            "stocks": [
                {"code": "688981", "name": "中芯国际", "impact": "国产晶圆代工龙头"},
                {"code": "688230", "name": "华虹公司", "impact": "特色工艺+功率器件"},
            ]
        },
        {
            "name": "先进封装",
            "desc": "2.5D/3D封装演进，CoWoS-L持续供不应求，预计至2028年仍为AI芯片主流封装方案",
            "stocks": [
                {"code": "600584", "name": "长电科技", "impact": "封测龙头 先进封装"},
                {"code": "002185", "name": "华天科技", "impact": "晶圆级封装"},
            ]
        },
    ],
    downstream=[
        {
            "name": "AI算力/液冷",
            "desc": "算力规模5倍增长+PUE≤1.2硬性要求，液冷从可选项变必选项，2026年液冷市场规模破千亿",
            "stocks": [
                {"code": "002837", "name": "英维克", "impact": "液冷全链条龙头"},
                {"code": "300475", "name": "聚隆科技", "impact": "液冷结构件"},
            ]
        },
        {
            "name": "PCB/高端铜箔",
            "desc": "AI服务器PCB升级带动高端铜箔需求激增260%，HVLP铜箔供不应求",
            "stocks": [
                {"code": "301217", "name": "铜冠铜箔", "impact": "高端PCB铜箔龙头"},
                {"code": "600183", "name": "生益科技", "impact": "覆铜板龙头"},
            ]
        },
        {
            "name": "6G/卫星互联网",
            "desc": "适时启动6G商用+低轨卫星互联网+智能体互联网络，通信板块新成长曲线",
            "stocks": [
                {"code": "002281", "name": "光迅科技", "impact": "光器件龙头"},
                {"code": "600498", "name": "烽火通信", "impact": "光通信设备"},
            ]
        },
    ]
)

# 投资机会
gen.add_investment_opportunities(
    [
        {
            "name": "半导体材料 - 台积电涨价传导链（最高优先级）",
            "priority": "高",
            "logic": (
                "台积电涨价3-6%确认行业景气度，上游材料直接受益于量价齐升+国产替代双重逻辑。"
                "雅克科技作为前驱体+光刻胶双龙头，韩国UP Chemical满产，2027年先进逻辑用前驱体业务规模持续增长。"
                "中芯国际产能利用率93.7%接近满产，Q3维持95%高位，已协商上调定价，上游材料端议价能力同步增强。"
                "估值锚：雅克科技当前PE(TTM) 62.92x，机构一致预期2026年业绩增速约30%，PEG约2x"
            ),
            "stocks": [
                {"code": "002409", "name": "雅克科技", "impact": "核心持仓"},
                {"code": "688519", "name": "南大光电", "impact": "弹性标的"},
            ]
        },
        {
            "name": "算力基础设施 - 液冷+高端铜箔（高优先级）",
            "priority": "高",
            "logic": (
                "十五五规划明确智能算力从1590→9800 EFLOPS（+516%），新建算力设施PUE≤1.2。"
                "液冷是PUE达标关键技术，中金预测2026年液冷市场规模破千亿，2028年达3000亿。"
                "铜冠铜箔HVLP4代量产、HVLP5代突破，AI服务器高端铜箔需求增260%。"
                "估值锚：铜冠铜箔PE(TTM) 230x但2026H1净利增514%，Q3环比持续改善，PEG<0.5"
            ),
            "stocks": [
                {"code": "002837", "name": "英维克", "impact": "核心持仓"},
                {"code": "301217", "name": "铜冠铜箔", "impact": "核心持仓"},
            ]
        },
        {
            "name": "先进封装/晶圆代工（中优先级）",
            "priority": "中",
            "logic": (
                "台积电涨价核心原因是先进制程+先进封装产能全面吃紧，CoWoS-L预计至2028年仍为AI芯片主流封装方案。"
                "国内先进封装企业有望承接溢出需求，中芯国际95%产能利用率下议价权提升。"
                "短期美股半导体回调+加息预期压制情绪，但产业趋势不受影响"
            ),
            "stocks": [
                {"code": "688981", "name": "中芯国际", "impact": "国产代工龙头"},
                {"code": "600584", "name": "长电科技", "impact": "封测龙头"},
            ]
        },
        {
            "name": "6G/卫星互联网（中优先级 主题催化）",
            "priority": "中",
            "logic": (
                "十五五规划首次明确适时启动6G商用，首提智能体互联网络概念，6G从万物互联升级为万物智联。"
                "但6G商用时点为2030年前后，当前仍处于技术攻关+标准制定阶段，以主题性机会为主，不宜过度追高"
            ),
            "stocks": [
                {"code": "002281", "name": "光迅科技", "impact": "光器件"},
                {"code": "600498", "name": "烽火通信", "impact": "通信设备"},
            ]
        },
    ],
    view_mode="tab"
)

# 催化深度分析
gen.add_catalyst_deep_analysis([
    {
        "title": "台积电2027年涨价",
        "type": "policy",
        "description": "台积电确定2027年1月上调晶圆代工价格3%-6%，先进制程涨幅更高，产能全面吃紧，订单能见度至2030年",
        "category": "半导体"
    },
    {
        "title": "十五五6G算力规划",
        "type": "policy",
        "description": "工信部发布信息通信十五五规划，智能算力增5倍+、6G适时商用、PUE≤1.2",
        "category": "通信算力"
    },
    {
        "title": "美联储加息预期升温",
        "type": "data",
        "description": "美国9月PMI超预期创62个月新高，10月加息概率飙升至68.6%，科技股估值承压",
        "category": "宏观"
    },
])

# 投资策略
strategy_html = '''
<div style="line-height: 1.9; color: #e2e8f0; font-size: 14px;">
    <div style="background: linear-gradient(135deg, rgba(34,197,94,0.1) 0%, rgba(22,163,74,0.05) 100%); 
                border-radius: 12px; padding: 16px; margin-bottom: 14px; border-left: 4px solid #22c55e;">
        <div style="font-weight: 700; color: #4ade80; margin-bottom: 8px;">📌 总体策略：结构性看多，回调加仓核心标的</div>
        <div style="font-size: 13px; color: #cbd5e1; line-height: 1.8;">
            台积电涨价从产业层面确认半导体景气度延续，6G/算力规划提供中长期政策支撑。
            隔夜美股回调+加息预期升温为短期情绪扰动，不改变产业趋势。
            建议利用低开机会加仓确定性最高的材料+液冷+铜箔三条主线。
        </div>
    </div>
    
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px;">
        <div style="background: rgba(255,255,255,0.04); border-radius: 12px; padding: 14px; border: 1px solid rgba(255,255,255,0.08);">
            <div style="display: flex; align-items: center; margin-bottom: 8px;">
                <span style="font-weight: 700; color: #f1f5f9;">英维克（002837）</span>
                <span style="margin-left: auto; background: rgba(34,197,94,0.2); color: #4ade80; 
                           padding: 3px 10px; border-radius: 20px; font-size: 11px; font-weight: 600;">持有+逢低加仓</span>
            </div>
            <div style="font-size: 12px; color: #94a3b8; line-height: 1.7;">
                现价61.25元。PUE≤1.2硬性要求直接利好液冷，Q3订单加速兑现在即。
                机构目标价86.51元，上行空间41%。回调至58-60元区间可加仓。
                <br><strong>估值锚：</strong>2026年一致预期PE约40x，2027年约25x
            </div>
        </div>
        <div style="background: rgba(255,255,255,0.04); border-radius: 12px; padding: 14px; border: 1px solid rgba(255,255,255,0.08);">
            <div style="display: flex; align-items: center; margin-bottom: 8px;">
                <span style="font-weight: 700; color: #f1f5f9;">铜冠铜箔（301217）</span>
                <span style="margin-left: auto; background: rgba(245,158,11,0.2); color: #fbbf24; 
                           padding: 3px 10px; border-radius: 20px; font-size: 11px; font-weight: 600;">持有 不追高</span>
            </div>
            <div style="font-size: 12px; color: #94a3b8; line-height: 1.7;">
                现价119.23元（昨日+4.09%），需警惕追高风险。
                HVLP4代量产+HVLP5突破，高端铜箔需求增260%，但PE(TTM)230x偏高。
                <br><strong>估值锚：</strong>2026年净利预期约8-10亿，PE约100-120x，回调至100-110元再加仓
            </div>
        </div>
        <div style="background: rgba(255,255,255,0.04); border-radius: 12px; padding: 14px; border: 1px solid rgba(255,255,255,0.08);">
            <div style="display: flex; align-items: center; margin-bottom: 8px;">
                <span style="font-weight: 700; color: #f1f5f9;">雅克科技（002409）</span>
                <span style="margin-left: auto; background: rgba(34,197,94,0.2); color: #4ade80; 
                           padding: 3px 10px; border-radius: 20px; font-size: 11px; font-weight: 600;">持有+逢低加仓</span>
            </div>
            <div style="font-size: 12px; color: #94a3b8; line-height: 1.7;">
                现价137.28元（+1.31%），主力资金净流入8905万（5.59%成交额）。
                台积电涨价直接利好上游材料，前驱体+光刻胶双赛道共振。
                <br><strong>估值锚：</strong>PE(TTM) 62.92x，机构一致预期2026年增速30%+，PEG约2x
            </div>
        </div>
        <div style="background: rgba(255,255,255,0.04); border-radius: 12px; padding: 14px; border: 1px solid rgba(255,255,255,0.08);">
            <div style="display: flex; align-items: center; margin-bottom: 8px;">
                <span style="font-weight: 700; color: #f1f5f9;">*ST建艺（002789）</span>
                <span style="margin-left: auto; background: rgba(245,158,11,0.2); color: #fbbf24; 
                           padding: 3px 10px; border-radius: 20px; font-size: 11px; font-weight: 600;">持有 观察</span>
            </div>
            <div style="font-size: 12px; color: #94a3b8; line-height: 1.7;">
                ST重组博弈标的，与本次半导体/6G催化关联度低。
                独立逻辑运行，建议维持原有仓位策略，不增不减。
                <br><strong>风险提示：</strong>ST股退市风险，仓位控制在5%以内
            </div>
        </div>
    </div>
    
    <div style="margin-top: 14px; background: rgba(245,158,11,0.08); border-radius: 12px; padding: 14px; 
                border: 1px solid rgba(245,158,11,0.2);">
        <div style="font-weight: 700; color: #fbbf24; margin-bottom: 8px;">⚠️ 减仓规则双重验证说明</div>
        <div style="font-size: 12px; color: #94a3b8; line-height: 1.7;">
            本次扫描未发出任何≥30%的减仓指令。所有持仓建议均为持有/逢低加仓。
            隔夜美股半导体回调为加息预期+做空消息扰动，产业逻辑（台积电涨价）未被破坏，
            不构成产业逻辑破坏+估值透支+技术破位三重信号，因此不触发减仓铁律。
        </div>
    </div>
</div>
'''

gen.add_investment_strategy(strategy_html)

# 风险提示
gen.add_risk_warning([
    "美联储10月加息概率升至68.6%，若加息落地可能进一步压制科技股估值",
    "Burry做空美光引发存储板块情绪波动，需警惕短期获利回吐压力",
    "台积电涨价属2027年事件，短期对业绩无直接影响，谨防情绪透支",
    "6G商用时点较远（2030年前后），主题性机会需把握节奏，不宜长期持有",
    "ST建艺退市风险，仓位需严格控制"
])

# 发布
result = gen.publish(
    title="S级催化｜台积电涨价3-6%+6G十五五规划双催化",
    filename="20260924_盘前_S级催化扫描_台积电涨价+6G规划"
)
print("发布结果:", result)
