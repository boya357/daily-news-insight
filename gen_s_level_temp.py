import sys, os
sys.path.insert(0, 'v3')
os.chdir('/root/daily-news-insight')

from v3.generators.s_level_catalyst import SLevelCatalystGenerator
from components.layout import Section

gen = SLevelCatalystGenerator(
    date_str="20260817",
    catalyst_title="英伟达CPO交换机全面量产 + 存储超级周期 + 中芯国际超预期",
    subtitle="2026.08.17 · 盘前S级催化"
)

# ===== Step 1: 催化事件概述 =====
overview = """
<b>三重S级催化共振来袭！</b>周末海外传来三大重磅消息，共同指向AI算力产业链景气度再上台阶：<br><br>
<b>① 英伟达CPO交换机全面量产（最强催化）：</b>8月14日凌晨英伟达官宣Spectrum-X以太网硅光交换机进入全面量产，全球首款200G/lane CPO交换机，激光器减少75%、功耗降80%、MTBF提升10倍。首批客户CoreWeave、Lambda Labs、甲骨文。A股天孚通信为唯一官方点名供应链厂商。<br><br>
<b>② SK海力士预警2027年史上最严重存储荒：</b>SK集团会长崔泰源称2027年将是存储行业有史以来供应缺口最大的一年，三大原厂2027年DRAM和HBM产能已全部售罄，客户只拿到60%-70%配额。长协改为3-5年，需预付10%-30%订金。<br><br>
<b>③ 中芯国际Q2营收首破30亿美元：</b>AI配套芯片需求激增，出货量环比+14.4%，ASP环比+5.7%，毛利率25.3%超指引上限。Q3指引毛利率26%-28%，涨价效应持续释放，AI产能挤压带来成熟制程订单回流。
"""
gen.add_catalyst_overview(overview)

# ===== Step 2: 催化事件详解 =====
bg = """
AI算力竞争进入下半场——从单卡性能转向集群互联效率。随着大模型训练规模突破万卡级别，GPU之间的数据传输瓶颈日益凸显。<br><br>
存储方面，AI大模型对HBM、高带宽内存的需求呈指数级增长，传统存储周期规律被彻底打破，行业从年度短期合约转向3-5年长协+预付订金模式。<br><br>
晶圆代工方面，海外大厂产能向HBM/先进逻辑倾斜，成熟制程产能被挤压，国内晶圆代工龙头迎来订单回流+量价齐升的黄金窗口期。
"""
trigger = """
🔥 <b>直接导火索1：</b>英伟达Spectrum-X CPO交换机全面量产，黄仁勋亲自定调算力竞争重心从单卡转向集群互联，光互联成为AI工厂新命门<br><br>
🔥 <b>直接导火索2：</b>SK海力士董事长崔泰源罕见表态价格涨太快我很抱歉，2027年供应缺口将是史上最大，存储行业规则被彻底改写<br><br>
🔥 <b>直接导火索3：</b>中芯国际Q2营收30.06亿美元超预期，AI配套芯片需求激增，电源管理/BCD/光模块相关芯片供不应求，Q3涨价效应将更显著
"""
gen.add_catalyst_details(bg, trigger)

# ===== Step 3: 隔夜全球市场扫描 =====
overnight_html = """
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 12px;">
    <div style="background: linear-gradient(135deg, rgba(239,68,68,0.1) 0%, rgba(185,28,28,0.05) 100%);
                border-radius: 12px; padding: 16px; border: 1px solid rgba(239,68,68,0.2);">
        <div style="font-size: 12px; color: #fca5a5; margin-bottom: 6px;">费城半导体指数 (SOX)</div>
        <div style="font-size: 22px; font-weight: 700; color: #fef2f2;">12,417</div>
        <div style="font-size: 13px; color: #f87171; margin-top: 4px;">-0.08%（上周五）</div>
    </div>
    <div style="background: linear-gradient(135deg, rgba(34,197,94,0.1) 0%, rgba(21,128,61,0.05) 100%);
                border-radius: 12px; padding: 16px; border: 1px solid rgba(34,197,94,0.2);">
        <div style="font-size: 12px; color: #86efac; margin-bottom: 6px;">AMD</div>
        <div style="font-size: 22px; font-weight: 700; color: #f0fdf4;">$514.39</div>
        <div style="font-size: 13px; color: #4ade80; margin-top: 4px;">+6.5%</div>
    </div>
    <div style="background: linear-gradient(135deg, rgba(34,197,94,0.1) 0%, rgba(21,128,61,0.05) 100%);
                border-radius: 12px; padding: 16px; border: 1px solid rgba(34,197,94,0.2);">
        <div style="font-size: 12px; color: #86efac; margin-bottom: 6px;">美光科技 (MU)</div>
        <div style="font-size: 22px; font-weight: 700; color: #f0fdf4;">$971.66</div>
        <div style="font-size: 13px; color: #4ade80; margin-top: 4px;">+2.3%</div>
    </div>
    <div style="background: linear-gradient(135deg, rgba(34,197,94,0.1) 0%, rgba(21,128,61,0.05) 100%);
                border-radius: 12px; padding: 16px; border: 1px solid rgba(34,197,94,0.2);">
        <div style="font-size: 12px; color: #86efac; margin-bottom: 6px;">闪迪 (SNDK)</div>
        <div style="font-size: 22px; font-weight: 700; color: #f0fdf4;">大涨7%+</div>
        <div style="font-size: 13px; color: #4ade80; margin-top: 4px;">半月累涨近50%</div>
    </div>
</div>
<div style="margin-top: 14px; display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 12px;">
    <div style="background: linear-gradient(135deg, rgba(239,68,68,0.08) 0%, rgba(185,28,28,0.04) 100%);
                border-radius: 12px; padding: 14px; border: 1px solid rgba(239,68,68,0.15);">
        <div style="font-size: 12px; color: #fca5a5; margin-bottom: 4px;">应用材料 (AMAT)</div>
        <div style="font-size: 18px; font-weight: 700; color: #fef2f2;">$507.18 <span style="font-size: 13px; color: #f87171;">-5.1%</span></div>
    </div>
    <div style="background: linear-gradient(135deg, rgba(239,68,68,0.08) 0%, rgba(185,28,28,0.04) 100%);
                border-radius: 12px; padding: 14px; border: 1px solid rgba(239,68,68,0.15);">
        <div style="font-size: 12px; color: #fca5a5; margin-bottom: 4px;">博通 (AVGO)</div>
        <div style="font-size: 18px; font-weight: 700; color: #fef2f2;">$393.05 <span style="font-size: 13px; color: #f87171;">-5.9%</span></div>
    </div>
    <div style="background: linear-gradient(135deg, rgba(239,68,68,0.08) 0%, rgba(185,28,28,0.04) 100%);
                border-radius: 12px; padding: 14px; border: 1px solid rgba(239,68,68,0.15);">
        <div style="font-size: 12px; color: #fca5a5; margin-bottom: 4px;">英伟达 (NVDA)</div>
        <div style="font-size: 18px; font-weight: 700; color: #fef2f2;">$225.16 <span style="font-size: 13px; color: #fca5a5;">-0.1%</span></div>
    </div>
    <div style="background: linear-gradient(135deg, rgba(234,179,8,0.08) 0%, rgba(161,98,7,0.04) 100%);
                border-radius: 12px; padding: 14px; border: 1px solid rgba(234,179,8,0.15);">
        <div style="font-size: 12px; color: #fde047; margin-bottom: 4px;">台积电 (TSM)</div>
        <div style="font-size: 18px; font-weight: 700; color: #fefce8;">$426.67 <span style="font-size: 13px; color: #fca5a5;">-0.9%</span></div>
    </div>
</div>
<div style="margin-top: 14px; padding: 14px 16px; background: rgba(16,185,129,0.08); 
            border-radius: 12px; border: 1px solid rgba(16,185,129,0.25);">
    <div style="font-size: 13px; font-weight: 600; color: #6ee7b7; margin-bottom: 8px;">隔夜要闻速览</div>
    <div style="font-size: 12px; color: #cbd5e1; line-height: 1.8;">
        • <b>存储板块领涨</b>：闪迪+7%、西部数据+4%、希捷+5%，半月闪迪反弹近50%<br>
        • <b>设备股承压</b>：应用材料-5.1%、科磊-2.7%、泛林-1.4%，设备板块短期获利回吐<br>
        • <b>AMD暴涨6.5%</b>：47.5亿美元创纪录发债用于AI扩张，市场解读为AI弹药到位<br>
        • <b>韩国半导体散户狂潮</b>：三星散户股东逼近800万，每5个韩国成年人就有1人持股<br>
        • <b>高毅/景林/东方港湾Q2持仓</b>：加仓存储（美光+闪迪），减仓英伟达
    </div>
</div>
"""
overnight_section = Section(title="隔夜全球市场扫描", content=overnight_html, icon="globe")
gen._components.append(overnight_section)

# ===== Step 4: 产业链梳理 =====
upstream = [
    {
        "name": "光芯片 / 激光器",
        "desc": "CPO外置CW激光器核心，磷化铟衬底+高纯铟+电子级红磷，是CPO架构的地基材料",
        "stocks": [
            {"code": "688498", "name": "源杰科技", "impact": "CW激光芯片国产龙头"},
            {"code": "688313", "name": "仕佳光子", "impact": "AWG+CW激光器扩产"},
            {"code": "002428", "name": "云南锗业", "impact": "磷化铟衬底国产龙头"},
            {"code": "600206", "name": "有研新材", "impact": "7N级超高纯铟"},
        ]
    },
    {
        "name": "存储材料 / 设备",
        "desc": "存储超级周期上游卖铲人，HBM材料、前道设备、测试设备",
        "stocks": [
            {"code": "002409", "name": "雅克科技", "impact": "HBM前驱体+光刻胶"},
            {"code": "688535", "name": "华海诚科", "impact": "HBM环氧塑封料"},
            {"code": "603690", "name": "至纯科技", "impact": "湿法设备"},
        ]
    },
    {
        "name": "铜箔 / 高端基材",
        "desc": "AI服务器PCB/HDI高附加值铜箔，MSCI纳入催化",
        "stocks": [
            {"code": "301217", "name": "铜冠铜箔", "impact": "MSCI纳入+AI铜箔放量"},
        ]
    },
]
midstream = [
    {
        "name": "CPO光模块 / 光引擎",
        "desc": "英伟达CPO交换机核心供应链，无源器件+光引擎+整机组装",
        "stocks": [
            {"code": "300394", "name": "天孚通信", "impact": "英伟达官方唯一A股点名"},
            {"code": "601138", "name": "工业富联", "impact": "CPO交换机整机ODM代工"},
            {"code": "300308", "name": "中际旭创", "impact": "1.6T硅光模块配套"},
            {"code": "300502", "name": "新易盛", "impact": "1.6T硅光批量供货"},
        ]
    },
    {
        "name": "晶圆代工 / 半导体制造",
        "desc": "AI产能挤压+成熟制程订单回流+量价齐升",
        "stocks": [
            {"code": "688981", "name": "中芯国际", "impact": "Q2营收首破30亿美刀"},
            {"code": "688347", "name": "华虹宏力", "impact": "产能扩张黄金期"},
        ]
    },
    {
        "name": "半导体设备 / 零部件",
        "desc": "晶圆厂扩产+国产替代双逻辑",
        "stocks": [
            {"code": "002371", "name": "北方华创", "impact": "设备平台龙头"},
            {"code": "688012", "name": "中微公司", "impact": "刻蚀设备+净利+98%"},
        ]
    },
]
downstream = [
    {
        "name": "液冷散热 / 温控",
        "desc": "AI算力密度提升驱动液冷需求，CPO交换机本身也是液冷机箱",
        "stocks": [
            {"code": "002837", "name": "英维克", "impact": "液冷龙头+AI温控"},
        ]
    },
    {
        "name": "AI服务器 / 算力基础设施",
        "desc": "CPO交换机带动AI集群建设加速",
        "stocks": [
            {"code": "603019", "name": "中科曙光", "impact": "国产算力龙头"},
            {"code": "000977", "name": "浪潮信息", "impact": "服务器龙头"},
        ]
    },
    {
        "name": "国产CPO交换机系统",
        "desc": "国内智算中心建设+自主可控需求",
        "stocks": [
            {"code": "000938", "name": "紫光股份", "impact": "新华三51.2T CPO商用"},
            {"code": "301165", "name": "锐捷网络", "impact": "51.2T CPO样机"},
        ]
    },
]
gen.add_industry_chain_analysis(upstream, midstream, downstream)

# ===== Step 5: 投资机会分析 =====
opps = [
    {
        "name": "CPO/光互联：最强主线，英伟达量产定调路线",
        "priority": "高",
        "logic": """英伟达Spectrum-X CPO交换机全面量产是AI光互联的里程碑事件。核心逻辑：算力竞争从单卡转向集群互联，CPO将光引擎直接封装在交换芯片旁，光损耗从22dB降到4dB（提升64倍），激光器减少75%、功耗降80%、MTBF提升10倍。<br><br>
<b>供应链确定性排序：</b>天孚通信（唯一A股官方点名）> 工业富联（整机组装65-70%价值量）> 中际旭创（1.6T外联模块）> 新易盛（1.6T硅光批量）> 华工科技（板载CPO光引擎）。<br><br>
<b>上游材料弹性：</b>源杰科技（CW激光芯片）、仕佳光子（AWG+CW激光器）、云南锗业（磷化铟衬底）。
<b>设备卖铲人：</b>罗博特科（硅光/CPO耦合设备）。<br><br>
<b>注意：</b>CPO尚处大规模商用早期，2026年小批量、2027年才规模化。短期光模块龙头业绩确定性更高。
        """,
        "stocks": [
            {"code": "300394", "name": "天孚通信", "impact": "英伟达官方供应链"},
            {"code": "601138", "name": "工业富联", "impact": "整机ODM代工"},
            {"code": "300308", "name": "中际旭创", "impact": "1.6T硅光模块"},
            {"code": "688498", "name": "源杰科技", "impact": "CW激光芯片国产替代"},
        ]
    },
    {
        "name": "存储超级周期：SK海力士预警史上最严重缺口",
        "priority": "高",
        "logic": """SK集团会长崔泰源8月13日表态：2027年将是存储行业有史以来供应缺口最大的一年，客户需求量接近原需求的两倍。<b>三大核心变化：</b><br>
① 需求端质变：AI智能体时代，存储需求与智能体数量挂钩，需求呈指数级增长<br>
② 供给端刚性：新建存储晶圆厂需4-5年，三大原厂2027年DRAM+HBM产能已全部售罄<br>
③ 商业模式重塑：35年短期合约改为3-5年长协，需预付10%-30%订金<br><br>
<b>A股受益方向：</b>存储芯片设计、HBM材料、存储设备、国产替代。
<b>关注：</b>2026年下半年到2027年国产存储产能释放将成为关键变量。
        """,
        "stocks": [
            {"code": "002409", "name": "雅克科技", "impact": "HBM前驱体龙头"},
            {"code": "688535", "name": "华海诚科", "impact": "HBM环氧塑封料"},
            {"code": "301217", "name": "铜冠铜箔", "impact": "存储PCB铜箔+MSCI"},
        ]
    },
    {
        "name": "晶圆代工：中芯国际超预期，量价齐升周期开启",
        "priority": "高",
        "logic": """中芯国际Q2营收30.06亿美元（环比+20%），毛利率25.3%（超指引上限3.3pct），归母净利润同比+261.7%。<b>核心看点：</b><br>
① AI配套需求激增：出货量环比+14.4%，AI配套芯片（电源管理、BCD、光模块收发）供不应求<br>
② 涨价效应Q3更显著：ASP环比+5.7%，Q3新价格晶圆占比提升，毛利率指引26%-28%<br>
③ 产能接近上限：产能利用率93.7%，Q3预计95%接近满产<br>
④ 合资厂进入收获期：非控股权益2.54亿美元（环比+659%）<br><br>
<b>投资逻辑：</b>全球晶圆代工进入量价齐升上行周期，国内龙头受益AI需求外溢+成熟制程订单回流。
        """,
        "stocks": [
            {"code": "688981", "name": "中芯国际", "impact": "Q2超预期+Q3涨价"},
            {"code": "688347", "name": "华虹宏力", "impact": "产能扩张黄金期"},
            {"code": "002371", "name": "北方华创", "impact": "设备龙头+扩产受益"},
        ]
    },
]
gen.add_investment_opportunities(opps, view_mode="tab")

# ===== Step 6: 持仓股影响分析 =====
portfolio_html = """
<div style="display: flex; flex-direction: column; gap: 14px;">
    <div style="border-left: 4px solid #22c55e; border-radius: 0 12px 12px 0;">
        <div style="background: rgba(255,255,255,0.05); border-radius: 0 12px 12px 0; padding: 16px 18px; 
                    border: 1px solid rgba(255,255,255,0.08); border-left: none;">
            <div style="display: flex; align-items: center; margin-bottom: 10px;">
                <span style="font-size: 16px; font-weight: 700; color: #f1f5f9;">英维克 (002837) - 液冷龙头</span>
                <span style="margin-left: auto; padding: 3px 10px; border-radius: 20px; font-size: 11px; font-weight: 700;
                           background: linear-gradient(135deg, #22c55e 0%, #15803d 100%); color: white;">
                    利好
                </span>
            </div>
            <div style="font-size: 13px; color: #cbd5e1; line-height: 1.8;">
                <b>催化逻辑：</b>CPO交换机+AI集群建设加速→液冷需求增长。英伟达Spectrum-X SN6810采用2U液冷机箱，印证高密度算力下液冷刚需。
                存储超级周期下HBM/AI服务器的功耗密度持续提升，液冷渗透率加速。
                <br><b>操作建议：</b>液冷主线逻辑强化，继续持有，关注中报业绩验证。若科技板块整体反弹，英维克有望跟随液冷板块修复。
            </div>
        </div>
    </div>
    <div style="border-left: 4px solid #22c55e; border-radius: 0 12px 12px 0;">
        <div style="background: rgba(255,255,255,0.05); border-radius: 0 12px 12px 0; padding: 16px 18px;
                    border: 1px solid rgba(255,255,255,0.08); border-left: none;">
            <div style="display: flex; align-items: center; margin-bottom: 10px;">
                <span style="font-size: 16px; font-weight: 700; color: #f1f5f9;">铜冠铜箔 (301217) - AI铜箔+MSCI</span>
                <span style="margin-left: auto; padding: 3px 10px; border-radius: 20px; font-size: 11px; font-weight: 700;
                           background: linear-gradient(135deg, #22c55e 0%, #15803d 100%); color: white;">
                    双重利好
                </span>
            </div>
            <div style="font-size: 13px; color: #cbd5e1; line-height: 1.8;">
                <b>催化逻辑：</b>① MSCI中国指数8月31日纳入，被动资金配置预期；② 存储超级周期+HBM需求带动PCB/铜箔高附加值产品放量；
                ③ 三孚新科考察交流，高端铜箔产业协同可期；④ 上半年预盈2.05-2.25亿元，同比+486%以上。
                <br><b>操作建议：</b>基本面+事件催化双重利好，继续持有，关注MSCI生效前的被动资金流入效应。
            </div>
        </div>
    </div>
    <div style="border-left: 4px solid #22c55e; border-radius: 0 12px 12px 0;">
        <div style="background: rgba(255,255,255,0.05); border-radius: 0 12px 12px 0; padding: 16px 18px;
                    border: 1px solid rgba(255,255,255,0.08); border-left: none;">
            <div style="display: flex; align-items: center; margin-bottom: 10px;">
                <span style="font-size: 16px; font-weight: 700; color: #f1f5f9;">雅克科技 (002409) - HBM材料龙头</span>
                <span style="margin-left: auto; padding: 3px 10px; border-radius: 20px; font-size: 11px; font-weight: 700;
                           background: linear-gradient(135deg, #22c55e 0%, #15803d 100%); color: white;">
                    利好
                </span>
            </div>
            <div style="font-size: 13px; color: #cbd5e1; line-height: 1.8;">
                <b>催化逻辑：</b>SK海力士预警存储史上最大缺口，HBM需求持续爆发。雅克科技是国内前驱体龙头，深度受益HBM扩产。
                存储超级周期拉长至2030年后，材料端景气度确定性高。
                <br><b>操作建议：</b>底仓30%持有策略不变，存储超级周期逻辑进一步强化。反弹后机动仓可考虑减仓，115-120元区间再评估。
                注意短期科技板块情绪波动带来的回调风险。
            </div>
        </div>
    </div>
    <div style="border-left: 4px solid #f59e0b; border-radius: 0 12px 12px 0;">
        <div style="background: rgba(255,255,255,0.05); border-radius: 0 12px 12px 0; padding: 16px 18px;
                    border: 1px solid rgba(255,255,255,0.08); border-left: none;">
            <div style="display: flex; align-items: center; margin-bottom: 10px;">
                <span style="font-size: 16px; font-weight: 700; color: #f1f5f9;">*ST建艺 (002789) - 重组预期</span>
                <span style="margin-left: auto; padding: 3px 10px; border-radius: 20px; font-size: 11px; font-weight: 700;
                           background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%); color: white;">
                    中性
                </span>
            </div>
            <div style="font-size: 13px; color: #cbd5e1; line-height: 1.8;">
                <b>催化逻辑：</b>与本次科技三重催化无直接关联，独立重组逻辑。
                <br><b>操作建议：</b>按原计划持有，关注重组进展。严格执行止损纪律。
            </div>
        </div>
    </div>
</div>
"""
portfolio_section = Section(title="持仓股影响评估", content=portfolio_html, icon="briefcase", variant="highlight")
gen._components.append(portfolio_section)

# ===== Step 7: 风险提示 =====
gen.add_risk_warning([
    "CPO交换机尚处量产初期，2026年出货量有限，业绩兑现需要时间，警惕纯概念炒作风险",
    "存储超级周期下，消费级NAND可能率先见顶，四季度消费级合约价上涨动能或已枯竭",
    "中芯国际Q3指引环比增速放缓至2%-4%，产能接近上限，短期增长更多靠涨价而非放量",
    "美股半导体设备股上周五大跌（AMAT-5.1%、AVGO-5.9%），或传导至A股设备板块情绪",
    "科技板块整体仍处震荡格局，单日大涨后注意追高风险，建议分批布局而非追涨"
])

# ===== Step 8: 投资策略建议 =====
strategy = """
<b>整体判断：三重S级催化共振，AI算力产业链景气度确认上行，今日科技板块有望高开。</b><br><br>
<b>优先级排序：</b>CPO/光互联（最强催化，英伟达量产定调） > 存储超级周期（SK海力士预警，持续时间长） > 晶圆代工（中芯超预期，基本面扎实）<br><br>
<b>操作策略：</b><br>
• <b>持仓策略</b>：4只持仓股全部受益于本次催化（铜冠铜箔双重利好最强），继续持有为主，不追高加仓<br>
• <b>新开仓方向</b>：CPO方向优先关注天孚通信（供应链确定性最高）、工业富联（价值量最大）、中际旭创（基本盘稳+新业务）<br>
• <b>存储方向</b>：HBM材料（雅克科技、华海诚科）逻辑最硬，设备（北方华创、中微公司）跟随<br>
• <b>仓位管理</b>：左侧仓位控制在30-50%，科技板块整体仍处震荡格局，分批介入更稳妥<br>
• <b>止损纪律</b>：单只个股回撤超过8%严格止损，不补仓、不摊平成本<br><br>
<b>空方视角（必须考虑）：</b><br>
• CPO量产不等于业绩爆发，目前出货量有限，概念兑现需要1-2个季度验证<br>
• 美股半导体设备股大跌可能传导，A股设备板块有回调压力<br>
• 存储超级周期的超级部分主要在HBM，消费级NAND已现疲态<br>
• 中芯国际Q3增速指引放缓，市场可能解读为景气度见顶信号
"""
gen.add_investment_strategy(strategy)

# ===== 发布 =====
result = gen.publish()
print("Publish result:", result)
