#!/usr/bin/env python3
"""
20260826 盘后S级催化扫描生成脚本
事件：英维克中报业绩拐点+液冷产业趋势确认 + 铜冠铜箔净利增514% + 英伟达财报前夜
"""
import sys, os
sys.path.insert(0, 'v3')
os.chdir('/root/daily-news-insight')

from v3.generators.s_level_catalyst import SLevelCatalystGenerator
from v3.components.layout import Section

gen = SLevelCatalystGenerator(
    date_str="20260826",
    catalyst_title="液冷业绩拐点确认：英维克Q2利润暴增1934%+铜冠铜箔增514%+英伟达财报前夜",
    subtitle="2026.08.26 · 盘后S级催化"
)

gen.add_catalyst_overview(
    overview='    <p><strong>【S级重大催化】</strong>2026年8月26日盘后，科技板块迎来多重催化共振。第一，持仓股<strong>英维克</strong>昨日涨停，龙虎榜机构净买入1.37亿元，中报显示Q2单季归母净利润环比暴增1934%，液冷散热从"可选"迈向"必选"的产业拐点得到业绩验证。第二，持仓股<strong>铜冠铜箔</strong>盘后发布半年报，上半年归母净利润2.15亿元，同比大增514.75%，存储铜箔+锂电铜箔双轮驱动。第三，<strong>英伟达Q2财报</strong>将于北京时间8月27日凌晨发布，市场预期营收917亿美元同比增96%，Rubin平台量产进展成为最大看点。第四，隔夜美股半导体全线反弹，费城半导体指数+1.44%，AMD+4.91%，存储/光通信板块领涨。</p>\n    <p style="margin-top:8px;">今日A股表现：沪指涨0.59%，科创50走强，半导体设备板块上涨1.51%。中韩半导体ETF成交额达61亿元，资金持续涌入科技赛道。龙虎榜机构现身28只个股，净买入11只。</p>\n    <p style="margin-top:8px;"><strong>核心逻辑</strong>：英维克Q2业绩拐点→液冷行业进入业绩兑现期（产业验证）；铜冠铜箔净利增514%→存储产业链复苏超预期（业绩验证）；英伟达财报前夜→全球AI算力资本开支周期锚定（情绪催化）。三重共振，科技板块或迎来业绩驱动的新一轮上行。</p>',
    importance="S级"
)

gen.add_catalyst_details(
    background='    <p><strong>1. 背景一：液冷从"概念炒作"进入"业绩兑现"阶段</strong></p>\n    <p>2026年以来，AI算力集群功耗持续攀升，单柜功率从20kW快速跃升至50-100kW级别，传统风冷已无法满足散热需求，液冷逐步成为高密度智算中心的标配。东吴证券研报指出，国产液冷已由送样验证进入批量交付阶段，2026-2028年份额提升有望快于行业增长。英维克SoluKing长效液冷工质系列两款产品通过英特尔认证，产品矩阵持续完善。</p>\n    <p style="margin-top:8px;"><strong>2. 背景二：存储产业链复苏超预期，铜箔环节量价齐升</strong></p>\n    <p>全球存储芯片进入超级周期，DRAM和NAND Flash合约价持续上涨。集邦咨询预估，存储器合约价将持续飙升，DRAM、NAND Flash到2027年占主要云厂商资本支出比重将达68%。铜冠铜箔作为国内电子铜箔龙头，HVM铜箔适配高端存储芯片封装，HTE铜箔用于锂电领域，双轮驱动业绩爆发。上半年营收40.21亿元同比增34.16%，归母净利润2.15亿元同比增514.75%。</p>\n    <p style="margin-top:8px;"><strong>3. 背景三：英伟达财报前夜，全球科技股屏息以待</strong></p>\n    <p>英伟达将于8月26日美股盘后（北京时间27日凌晨）发布2027财年Q2财报。彭博一致预期营收917.5亿美元同比增96%，数据中心收入突破854亿美元同比增107%。市场关注三大焦点：①Rubin平台量产进度与收入贡献；②75%毛利率防线能否守住（存储涨价侵蚀成本）；③Q3指引是否继续超预期。此前英伟达已连续四个季度财报次日下跌，"财报后必跌"魔咒能否打破成为最大悬念。</p>',
    trigger='    <p><strong>🔥 触发因素一：英维克Q2利润暴增1934%，液冷业绩拐点确立</strong></p>\n    <p>英维克2026年半年报：上半年营收30.17亿元（+17.24%），归母净利润1.85亿元（-14.32%）。但拆解来看，Q2单季营收18.41亿元环比大增56.67%，归母净利润1.76亿元环比暴增近20倍，经营现金流同比增长126%。业绩拐点信号强烈：Q2利润占上半年95%，数据中心与储能温控业务放量+海外订单加速交付。8月25日涨停，成交额56.47亿元，龙虎榜机构净买入1.37亿元，主力资金净流入超16亿元。</p>\n    <p style="margin-top:8px;"><strong>🔥 触发因素二：铜冠铜箔中报净利增514.75%，存储+锂电双轮驱动</strong></p>\n    <p>铜冠铜箔8月26日盘后公告：2026年上半年营收40.21亿元同比增34.16%，归母净利润2.15亿元同比增514.75%。公司拟每10股派发现金红利0.6元。业绩大幅增长主要受益于：①存储芯片需求爆发带动HVM/HTE高端铜箔量价齐升；②锂电铜箔出货量增长；③铜价上涨带动产品价格提升。存储产业链复苏从上游设备、材料传导至铜箔环节，全面验证行业景气度。</p>\n    <p style="margin-top:8px;"><strong>🔥 触发因素三：隔夜美股半导体全线反弹，费半+1.44%AMD+4.91%</strong></p>\n    <p>8月25日美股收盘：费城半导体指数涨1.44%，结束前期连续调整。AMD涨4.91%（Raymond James上调至"强力买入"），迈威尔科技涨4.84%，希捷科技、西部数据涨超3%，SK海力士涨2.68%，美光科技涨超2%，台积电涨超1%。光通信板块大涨：Lumentum涨超6%，Applied Optoelectronics涨超5%，Coherent涨超4%。英伟达涨超2%，结束七连跌。反弹动力来自美债收益率回落+油价下跌+AI产业催化（SpaceX AI卫星明年发射）。</p>\n    <p style="margin-top:8px;"><strong>🔥 触发因素四：SK海力士公布HBM 20层以上封装路线，先进封装再添催化</strong></p>\n    <p>SK海力士在Hot Chips 2026大会上公布下一代HBM封装路线：短期内继续改进MR-MUF工艺支撑16层堆叠，中长期为20层以上结构研究混合键合技术。HBM封装从"量的堆叠"进入"质的飞跃"阶段，混合键合可使核心裸片增厚最多24%，同时改善散热与信号完整性。先进封装产业链持续向纵深发展，国内封装材料/设备厂商迎来长期成长空间。</p>'
)

gen.add_industry_chain_analysis(
    upstream=[
        {
            'name': '电子铜箔（存储+锂电）',
            'desc': '存储芯片超级周期带动高端铜箔需求爆发，锂电铜箔同步复苏。铜冠铜箔作为国内龙头，HVM铜箔适配高端存储封装，量价齐升逻辑清晰。',
            'stocks': [
                {'code': '301217', 'name': '铜冠铜箔', 'impact': '强正面（净利增514%+双轮驱动）'},
                {'code': '600110', 'name': '诺德股份', 'impact': '正面（锂电铜箔龙头）'},
            ]
        },
        {
            'name': '半导体材料（HBM/前驱体）',
            'desc': 'HBM向20层以上迈进，封装材料需求持续增长。雅克科技HBM前驱体+电子特气双主线，受益于存储涨价与先进封装扩产。',
            'stocks': [
                {'code': '002409', 'name': '雅克科技', 'impact': '正面（HBM前驱体龙头）'},
                {'code': '688120', 'name': '华海诚科', 'impact': '正面（环氧塑封料GPM）'},
            ]
        },
        {
            'name': '液冷散热部件/工质',
            'desc': 'AI算力集群功耗飙升，液冷从可选变为必选。英维克Q2业绩拐点验证行业进入兑现期，液冷工质、CDU、冷板等核心部件需求快速增长。',
            'stocks': [
                {'code': '002837', 'name': '英维克', 'impact': '强正面（Q2利润增1934%+液冷龙头）'},
                {'code': '300648', 'name': '申菱环境', 'impact': '正面（液冷+温控）'},
            ]
        }
    ],
    midstream=[
        {
            'name': '液冷散热系统集成',
            'desc': '液冷渗透率快速提升，从互联网大厂向运营商、政企客户扩散。英维克、申菱环境等厂商在手订单充足，Q2开始进入业绩兑现阶段。',
            'stocks': [
                {'code': '002837', 'name': '英维克', 'impact': '强正面（液冷龙头+业绩拐点）'},
                {'code': '300648', 'name': '申菱环境', 'impact': '正面'},
                {'code': '603912', 'name': '佳力图', 'impact': '中性偏正面'},
            ]
        },
        {
            'name': '先进封装/HBM',
            'desc': 'SK海力士公布20层以上HBM路线，先进封装技术持续突破。日本封测设备管制倒逼国产替代，国内封测三巨头产能快速扩张。',
            'stocks': [
                {'code': '600584', 'name': '长电科技', 'impact': '正面（封测龙头）'},
                {'code': '002156', 'name': '通富微电', 'impact': '正面（AMD供应链）'},
                {'code': '002185', 'name': '华天科技', 'impact': '正面'},
            ]
        },
        {
            'name': '存储芯片',
            'desc': '隔夜美股存储板块全线回暖，集邦咨询预估存储器合约价持续飙升。HBM需求紧平衡，服务器DRAM涨价通道延续。',
            'stocks': [
                {'code': '688003', 'name': '长鑫科技', 'impact': '正面（DRAM国产替代龙头）'},
                {'code': '301217', 'name': '铜冠铜箔', 'impact': '正面（存储铜箔）'},
                {'code': '002409', 'name': '雅克科技', 'impact': '正面（HBM材料）'},
            ]
        },
        {
            'name': '半导体设备',
            'desc': '盛美上海上半年新签订单同比增105%，国产设备验证放量。半导体设备ETF走强，设备国产替代持续推进。',
            'stocks': [
                {'code': '688082', 'name': '盛美上海', 'impact': '正面（订单增105%）'},
                {'code': '688012', 'name': '中微公司', 'impact': '正面（刻蚀设备龙头）'},
                {'code': '688037', 'name': '芯源微', 'impact': '正面（涂胶显影）'},
            ]
        }
    ],
    downstream=[
        {
            'name': 'AI算力/数据中心',
            'desc': '英伟达财报前夜，市场预期数据中心收入突破854亿美元同比增107%。Rubin平台量产进度将决定下一阶段算力资本开支节奏。',
            'stocks': [
                {'code': 'NVDA', 'name': '英伟达（美股）', 'impact': '核心风向标'},
                {'code': '000977', 'name': '浪潮信息', 'impact': '正面（AI服务器龙头）'},
                {'code': '603019', 'name': '中科曙光', 'impact': '正面'},
            ]
        },
        {
            'name': '光模块/光通信',
            'desc': '隔夜美股光通信板块大涨，SpaceX AI卫星合作点燃光互连想象。1.6T/3.2T光模块升级周期持续推进。',
            'stocks': [
                {'code': '300308', 'name': '中际旭创', 'impact': '正面（光模块龙头）'},
                {'code': '300502', 'name': '新易盛', 'impact': '正面'},
                {'code': '600487', 'name': '亨通光电', 'impact': '正面（机构净买入18亿）'},
            ]
        }
    ]
)

gen.add_investment_opportunities(
    opportunities=[
        {
            'name': '液冷业绩兑现主线（S级机会）',
            'priority': '高',
            'logic': '英维克Q2利润环比暴增1934%，标志着液冷行业从概念炒作进入业绩兑现阶段。AI算力集群功耗持续攀升，液冷从"可选"变为"必选"，行业渗透率有望从当前15%快速提升至50%以上。机构资金已大规模进场（英维克机构净买1.37亿），业绩+资金+产业三重共振。',
            'stocks': [
                {'code': '002837', 'name': '英维克', 'impact': '液冷龙头+业绩拐点+机构加持'},
                {'code': '300648', 'name': '申菱环境', 'impact': '液冷+储能温控'},
            ]
        },
        {
            'name': '存储铜箔量价齐升（S级机会）',
            'priority': '高',
            'logic': '铜冠铜箔上半年净利增514.75%，大超市场预期。存储芯片超级周期带动高端HVM铜箔需求爆发，叠加锂电铜箔复苏，双轮驱动业绩高增长。存储产业链从设备、材料到铜箔全链条验证景气度，铜箔环节弹性最大。',
            'stocks': [
                {'code': '301217', 'name': '铜冠铜箔', 'impact': '净利增514%+存储+锂电双轮驱动'},
            ]
        },
        {
            'name': '英伟达财报催化的算力产业链',
            'priority': '中高',
            'logic': '英伟达Q2财报将于27日凌晨发布，市场预期营收917亿美元同比增96%。若财报超预期且Rubin平台进展顺利，将直接催化A股算力产业链（光模块、PCB、液冷、AI服务器）。若不及预期则可能引发短期调整。当前期权隐含波动5.4%，低于历史均值，市场情绪偏谨慎。',
            'stocks': [
                {'code': '300308', 'name': '中际旭创', 'impact': '光模块龙头+英伟达供应链'},
                {'code': '002463', 'name': '沪电股份', 'impact': 'AI服务器PCB龙头'},
                {'code': '002837', 'name': '英维克', 'impact': '液冷配套'},
            ]
        },
        {
            'name': 'HBM/先进封装材料',
            'priority': '中高',
            'logic': 'SK海力士公布HBM 20层以上封装路线，混合键合技术突破，HBM向更高密度、更高带宽演进。先进封装扩产持续带动材料需求，HBM封装材料量价齐升逻辑清晰。',
            'stocks': [
                {'code': '002409', 'name': '雅克科技', 'impact': 'HBM前驱体+电子特气'},
                {'code': '688120', 'name': '华海诚科', 'impact': '环氧塑封料GPM国产替代'},
            ]
        }
    ]
)

# 隔夜外盘板块
overnight_section = Section(title="🌍 隔夜外盘 & 全球市场全景跟踪", content='<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px;">\n    <div style="background: rgba(34,197,94,0.08); border-radius: 12px; padding: 16px; border: 1px solid rgba(34,197,94,0.2);">\n        <div style="font-size: 14px; font-weight: 700; color: #4ade80; margin-bottom: 10px;">📈 美股主要指数（8/25收盘）</div>\n        <div style="font-size: 13px; color: #cbd5e1; line-height: 2;">\n            <p>纳斯达克指数：<span style="color:#4ade80;">+0.66%</span> 报26151.30点</p>\n            <p>标普500指数：<span style="color:#4ade80;">+0.32%</span> 报7677.28点</p>\n            <p>道琼斯指数：<span style="color:#4ade80;">+0.30%</span> 报53577.40点</p>\n            <p>费城半导体指数：<span style="color:#4ade80;">+1.44%</span>（反弹延续）</p>\n            <p>纳斯达克金龙指数：<span style="color:#4ade80;">+1.11%</span> 报6268.26点</p>\n        </div>\n    </div>\n    <div style="background: rgba(245,158,11,0.08); border-radius: 12px; padding: 16px; border: 1px solid rgba(245,158,11,0.2);">\n        <div style="font-size: 14px; font-weight: 700; color: #fcd34d; margin-bottom: 10px;">🔥 核心半导体标的（收盘）</div>\n        <div style="font-size: 13px; color: #cbd5e1; line-height: 2;">\n            <p>英伟达 NVDA：<span style="color:#4ade80;">+2%+</span>（结束七连跌）</p>\n            <p>台积电 TSM：<span style="color:#4ade80;">+1%+</span></p>\n            <p>美光科技 MU：<span style="color:#4ade80;">+2%+</span></p>\n            <p>AMD：<span style="color:#4ade80;">+4.91%</span>（上调评级催化）</p>\n            <p>博通 AVGO：小幅上涨</p>\n            <p>SK海力士 ADR：<span style="color:#4ade80;">+2.68%</span></p>\n            <p>迈威尔科技 MRVL：<span style="color:#4ade80;">+4.84%</span></p>\n        </div>\n    </div>\n    <div style="background: rgba(168,85,247,0.08); border-radius: 12px; padding: 16px; border: 1px solid rgba(168,85,247,0.2);">\n        <div style="font-size: 14px; font-weight: 700; color: #c084fc; margin-bottom: 10px;">💡 光通信/存储板块（涨幅榜）</div>\n        <div style="font-size: 13px; color: #cbd5e1; line-height: 2;">\n            <p>Lumentum：<span style="color:#4ade80;">+6%+</span>（光器件）</p>\n            <p>Applied Optoelectronics：<span style="color:#4ade80;">+5%+</span>（光器件）</p>\n            <p>Coherent：<span style="color:#4ade80;">+4%+</span>（光器件）</p>\n            <p>希捷科技 STX：<span style="color:#4ade80;">+3%+</span>（存储）</p>\n            <p>西部数据 WDC：<span style="color:#4ade80;">+3%+</span>（存储）</p>\n            <p>闪迪 SNDK：上涨（存储）</p>\n        </div>\n    </div>\n    <div style="background: rgba(59,130,246,0.08); border-radius: 12px; padding: 16px; border: 1px solid rgba(59,130,246,0.2);">\n        <div style="font-size: 14px; font-weight: 700; color: #93c5fd; margin-bottom: 10px;">📰 关键政策/事件</div>\n        <div style="font-size: 13px; color: #cbd5e1; line-height: 2;">\n            <p>🇺🇸 英伟达Q2财报：8/26盘后发布，预期营收917亿</p>\n            <p>🇰🇷 SK海力士公布HBM 20层以上封装路线</p>\n            <p>🇯🇵 日本第三轮对华半导体管制8月1日生效</p>\n            <p>🇨🇳 盛美上海上半年新签订单同比增105%</p>\n            <p>🛢️ WTI原油：-3.12%报82.36美元/桶</p>\n            <p>💰 美10年期国债收益率：约4.66%（回落）</p>\n            <p>🌏 SpaceX AI卫星搭载英伟达芯片明年Q4发射</p>\n        </div>\n    </div>\n</div>\n<p style="margin-top: 10px; font-size: 12px; color: #94a3b8;">数据来源：财联社、中新经纬、新浪财经、证券时报 | 2026.08.26 盘后</p>', icon="globe")
gen._components.append(overnight_section)

# 龙虎榜板块
dragon_section = Section(title="🐯 龙虎榜机构资金动向", content='<div style="background: rgba(245,158,11,0.06); border-radius: 14px; padding: 20px; border: 1px solid rgba(245,158,11,0.2);">\n    <div style="font-size: 15px; font-weight: 700; color: #fcd34d; margin-bottom: 16px; display: flex; align-items: center;">\n        <span style="margin-right: 8px;">🐯</span>龙虎榜机构动向（8月26日）\n    </div>\n    <div style="font-size: 13px; color: #cbd5e1;">\n        <p style="margin-bottom: 12px;">8月26日沪指上涨0.59%，机构现身28只个股龙虎榜，<strong>净买入11只，净卖出17只</strong>，合计净卖出3.89亿元。深沪股通席位出现在23只个股龙虎榜。</p>\n        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-top: 12px;">\n            <div style="background: rgba(34,197,94,0.06); border-radius: 10px; padding: 12px; border: 1px solid rgba(34,197,94,0.15);">\n                <div style="font-weight: 600; color: #4ade80; margin-bottom: 8px;">机构净买入TOP5</div>\n                <div style="font-size: 12px; line-height: 1.9;">\n                    <p>1. 国仪公司(688828)：<span style="color:#4ade80;">+6426万</span> | 换手率39.59%</p>\n                    <p>2. 兆日科技(300333)：<span style="color:#4ade80;">+5551万</span> | 净利增5639%</p>\n                    <p>3. 新大陆(000997)：<span style="color:#4ade80;">+5364万</span> | 涨停+深股通+1.41亿</p>\n                    <p>4. 汉森制药(002412)：<span style="color:#4ade80;">+3570万</span> | 涨幅6.16%</p>\n                    <p>5. 中南文化(002445)：<span style="color:#4ade80;">+3324万</span> | 跌2.96%</p>\n                </div>\n            </div>\n            <div style="background: rgba(239,68,68,0.06); border-radius: 10px; padding: 12px; border: 1px solid rgba(239,68,68,0.15);">\n                <div style="font-weight: 600; color: #f87171; margin-bottom: 8px;">机构净卖出TOP3</div>\n                <div style="font-size: 12px; line-height: 1.9;">\n                    <p>1. 中际联合(605305)：<span style="color:#f87171;">-1.94亿</span> | 跌9.70%</p>\n                    <p>2. 华瑞股份(300626)：<span style="color:#f87171;">-8657万</span> | 跌17.24%</p>\n                    <p>3. 通鼎互联(002491)：<span style="color:#f87171;">-6564万</span> | 涨5.05%</p>\n                </div>\n            </div>\n        </div>\n        <div style="margin-top: 14px; padding: 12px; background: rgba(59,130,246,0.06); border-radius: 10px; border: 1px solid rgba(59,130,246,0.15);">\n            <div style="font-weight: 600; color: #60a5fa; margin-bottom: 8px;">💡 重点点评</div>\n            <div style="font-size: 12px; line-height: 1.9; color: #cbd5e1;">\n                <p>• <strong>英维克(002837)</strong>：昨日（8/25）龙虎榜机构净买入1.37亿，深股通净卖出1.08亿，机构资金与外资分歧，整体多方胜出。今日延续强势。</p>\n                <p>• 新大陆(000997)：机构+深股通合计净买入近2亿，涨停板资金合力较强。</p>\n                <p>• 兆日科技(300333)：上半年净利增5639%，4家机构现身，机构对业绩高增长标的认可度提升。</p>\n            </div>\n        </div>\n        <p style="margin-top: 14px; font-size: 12px; color: #94a3b8;">数据来源：证券时报·数据宝、东方财富 | 2026.08.26</p>\n    </div>\n</div>', icon="activity")
gen._components.append(dragon_section)

# 持仓股分析板块
port_section = Section(title="📊 持仓股影响分析 & 操作建议", content='<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px;">\n    <div style="background: linear-gradient(135deg, rgba(34,197,94,0.12) 0%, rgba(22,163,74,0.06) 100%); border-radius: 14px; padding: 18px; border: 1px solid rgba(34,197,94,0.3);">\n        <div style="font-size: 14px; font-weight: 700; color: #4ade80; margin-bottom: 12px;">英维克 (002837) 液冷散热 ⭐S级催化</div>\n        <div style="font-size: 13px; color: #cbd5e1; line-height: 1.9;">\n            <p><strong>当前价格：</strong>约60.23元（8/25涨停）</p>\n            <p><strong>催化影响：</strong><span style="color:#4ade80;"><strong>强正面</strong></span></p>\n            <p>Q2单季利润环比暴增1934%，业绩拐点确立。液冷行业从概念进入兑现阶段，机构净买入1.37亿验证资金共识。主力资金净流入超16亿元。</p>\n            <p><strong>技术面：</strong>突破前高，成交量放大至56.47亿，换手率8.51%。短期超买，注意回踩风险。</p>\n            <p><strong>操作建议：</strong>持有为主，不追高。若回踩55元附近（5日线支撑）可考虑加仓；若冲高至65-68元压力区间可减仓机动仓锁定利润。止损位上移至52元。</p>\n        </div>\n    </div>\n    <div style="background: linear-gradient(135deg, rgba(34,197,94,0.12) 0%, rgba(22,163,74,0.06) 100%); border-radius: 14px; padding: 18px; border: 1px solid rgba(34,197,94,0.3);">\n        <div style="font-size: 14px; font-weight: 700; color: #4ade80; margin-bottom: 12px;">铜冠铜箔 (301217) 电子铜箔 ⭐S级催化</div>\n        <div style="font-size: 13px; color: #cbd5e1; line-height: 1.9;">\n            <p><strong>催化影响：</strong><span style="color:#4ade80;"><strong>强正面</strong></span></p>\n            <p>盘后发布半年报：上半年归母净利润2.15亿元，同比大增514.75%，大超市场预期。存储铜箔+锂电铜箔双轮驱动，量价齐升。拟10派0.6元分红。</p>\n            <p><strong>估值锚：</strong>动态PE随业绩大幅下降，存储铜箔赛道高增长可期。HVM铜箔受益于存储芯片超级周期，需求确定性强。</p>\n            <p><strong>操作建议：</strong>持有，明日关注高开幅度。若高开后能放量上攻则继续持有；若高开低走（利好兑现）可适当减仓。中期看好存储周期复苏逻辑。</p>\n        </div>\n    </div>\n    <div style="background: linear-gradient(135deg, rgba(59,130,246,0.1) 0%, rgba(37,99,235,0.05) 100%); border-radius: 14px; padding: 18px; border: 1px solid rgba(59,130,246,0.25);">\n        <div style="font-size: 14px; font-weight: 700; color: #60a5fa; margin-bottom: 12px;">雅克科技 (002409) 半导体材料</div>\n        <div style="font-size: 13px; color: #cbd5e1; line-height: 1.9;">\n            <p><strong>催化影响：</strong><span style="color:#60a5fa;"><strong>中性偏正面</strong></span></p>\n            <p>SK海力士HBM 20层路线发布+存储板块反弹+铜冠铜箔业绩验证，对雅克科技HBM前驱体业务形成间接催化。上半年净利5.61亿元同比增7.3%，增速温和。</p>\n            <p><strong>机构动向：</strong>二季度机构持股减少超10家，前十大机构持股比例下跌2.27个百分点，需关注机构减仓压力。</p>\n            <p><strong>操作建议：</strong>持有底仓，关注明日板块联动效应。若反弹至130-135元区间可考虑减机动仓。支撑位120元，止损位115元。</p>\n        </div>\n    </div>\n    <div style="background: linear-gradient(135deg, rgba(239,68,68,0.1) 0%, rgba(220,38,38,0.05) 100%); border-radius: 14px; padding: 18px; border: 1px solid rgba(239,68,68,0.25);">\n        <div style="font-size: 14px; font-weight: 700; color: #f87171; margin-bottom: 12px;">*ST建艺 (002789)</div>\n        <div style="font-size: 13px; color: #cbd5e1; line-height: 1.9;">\n            <p><strong>催化影响：</strong><span style="color:#f87171;"><strong>无直接关联</strong></span></p>\n            <p>今日公告选举刘常青为董事长（正方集团副总经理空降），属于常规人事变动。公司仍处于庭外重组阶段，退市风险未解除。</p>\n            <p><strong>风险提示：</strong>公司上半年预亏1.1-1.6亿元，新增诉讼仲裁4401万元占净资产21%，被列为失信被执行人。ST股不参与任何题材炒作。</p>\n            <p><strong>操作建议：</strong>坚决回避，不参与任何反弹。退市风险股与科技主线无关联，不浪费仓位。</p>\n        </div>\n    </div>\n</div>\n<p style="margin-top: 10px; font-size: 12px; color: #94a3b8;">注：以上分析基于公开信息整理，不构成投资建议。双重验证：英维克龙虎榜数据来自深交所+东方财富+证券时报三源交叉验证；铜冠铜箔业绩来自公司公告+财联社双源确认。</p>', icon="briefcase")
gen._components.append(port_section)

gen.add_risk_warning([
    '英伟达财报不及预期风险：若英伟达Q3指引低于市场预期，可能引发全球科技股调整，A股算力产业链将承压',
    '英维克短期超买风险：涨停后短期涨幅较大，主力资金获利了结可能导致回调，注意追高风险',
    '铜冠铜箔利好兑现风险：业绩大增514%已部分反映在股价中，若明日高开低走需警惕"利好出尽"',
    '存储周期复苏持续性存疑：全球经济不确定性可能影响存储需求复苏节奏，涨价能否持续有待验证',
    '机构减仓压力：雅克科技二季度机构持股减少，反弹过程中可能面临机构抛压',
    '地缘政治风险：中美科技博弈、日本半导体管制、中东局势等外部不确定性',
    '本报告不构成投资建议，股市有风险，投资需谨慎'
])

gen.add_investment_strategy('<p><strong>【整体判断】</strong>今日盘后科技板块迎来多重催化共振：英维克Q2利润暴增1934%验证液冷业绩拐点、铜冠铜箔净利增514%验证存储产业链复苏、隔夜美股半导体全线反弹提振情绪、英伟达财报前夜聚焦全球目光。整体判断为<strong>业绩驱动的结构性行情</strong>，而非普涨，选股比仓位更重要。</p>\n<p style="margin-top:12px;"><strong>【明日关键变量】</strong></p>\n<ul style="margin-top:8px; padding-left: 20px; line-height: 2; color: #e2e8f0;">\n    <li><strong>英伟达财报（8/27凌晨）</strong>：决定全球科技股短期方向。若超预期+Rubin指引乐观，则A股算力产业链继续上攻；若不及预期则可能引发调整。</li>\n    <li><strong>铜冠铜箔开盘表现</strong>：业绩大增514%能否带动存储板块整体走强，是验证存储周期复苏强度的关键。</li>\n    <li><strong>英维克能否延续强势</strong>：涨停后量价配合情况，决定液冷板块行情的持续性。</li>\n    <li><strong>量能变化</strong>：沪深两市成交额能否维持在万亿以上，决定反弹的广度和高度。</li>\n</ul>\n<p style="margin-top:12px;"><strong>【仓位建议】</strong>整体仓位维持<strong>5-6成</strong>，以液冷+存储铜箔为核心配置，半导体材料/设备为辅。不追高、逢低布局，预留资金应对英伟达财报后的波动。</p>\n<p style="margin-top:12px;"><strong>【分方向优先级】</strong></p>\n<ol style="margin-top:8px; padding-left: 20px; line-height: 2; color: #e2e8f0;">\n    <li><strong>🥇 第一优先级：液冷散热</strong> — 英维克Q2业绩拐点验证行业进入兑现期，机构资金进场确认。业绩+资金+产业三重共振，确定性最高。</li>\n    <li><strong>🥈 第二优先级：存储铜箔</strong> — 铜冠铜箔净利增514%验证存储产业链复苏，量价齐升弹性最大。存储超级周期逻辑持续强化。</li>\n    <li><strong>🥉 第三优先级：HBM/先进封装材料</strong> — SK海力士20层路线发布+日本管制催化国产替代，长期成长空间大，但短期催化剂强度稍弱。</li>\n    <li>第四优先级：光模块/PCB — 英伟达财报催化+1.6T升级周期，弹性较大但波动也大。</li>\n</ol>\n<p style="margin-top:12px;"><strong>【持仓操作建议】</strong></p>\n<ul style="margin-top:8px; padding-left: 20px; line-height: 2; color: #e2e8f0;">\n    <li><strong>英维克：</strong>核心持仓，持有为主。回踩5日线加仓，冲高至65-68元减机动仓。止损上移至52元。</li>\n    <li><strong>铜冠铜箔：</strong>核心持仓，明日重点关注。若高开高走则持有；若高开低走且放量则减仓。中期看好存储周期复苏。</li>\n    <li><strong>雅克科技：</strong>底仓持有，130-135元区间可减机动仓。机构减仓压力需警惕。</li>\n    <li><strong>*ST建艺：</strong>坚决回避，不参与任何反弹。</li>\n</ul>\n<p style="margin-top:12px;"><strong>【英伟达财报交易策略】</strong></p>\n<ul style="margin-top:8px; padding-left: 20px; line-height: 2; color: #e2e8f0;">\n    <li><strong>情景一：财报超预期+Rubin指引乐观</strong> → 加仓液冷/光模块/PCB，目标仓位7成</li>\n    <li><strong>情景二：财报符合预期+指引中性</strong> → 维持现有仓位，高抛低吸</li>\n    <li><strong>情景三：财报不及预期+指引下修</strong> → 减仓至4成，等待回调后再布局</li>\n</ul>\n<p style="margin-top:12px;"><strong>【中期展望】</strong>AI算力+存储+液冷+先进封装的产业大趋势未变，2026年是业绩兑现元年。英维克Q2拐点+铜冠铜箔高增长验证了从"故事"到"业绩"的转变。回调就是买入机会，但需注意节奏控制，不追高、不恋战，严格执行止损纪律。</p>')

print("开始生成S级催化报告...")
html = gen.generate()
print(f"报告生成完成，长度: {len(html)} 字符")

result = gen.publish(
    title="液冷业绩拐点确认：英维克Q2利润暴增1934%+铜冠铜箔增514%+英伟达财报前夜",
    report_type="s_level_catalyst",
    filename="20260826_盘后_S级催化扫描_液冷业绩拐点+存储复苏.html",
    excerpt="S级催化：英维克Q2利润环比暴增1934%液冷业绩拐点+铜冠铜箔净利增514.75%存储复苏验证+英伟达财报前夜全球聚焦+隔夜美股半导体反弹。",
    auto_deploy=True,
    docs_root="docs"
)
print(f"发布结果: {result}")
print("任务完成！")
