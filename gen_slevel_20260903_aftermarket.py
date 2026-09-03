#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
20260903 盘后S级催化扫描生成脚本
核心催化：十部门"十五五"规划硬科技国家基金+长电科技65亿定增加码先进封装+精智达15.76亿半导体测试设备合同+隔夜美股半导体企稳
"""
import sys, os
sys.path.insert(0, 'v3')
os.chdir('/root/daily-news-insight')

from v3.generators.s_level_catalyst import SLevelCatalystGenerator
from v3.components.layout import Section
from v3.components.data import StockTags

gen = SLevelCatalystGenerator(
    date_str="20260903",
    catalyst_title="硬科技国家级催化：十部门十五五规划+长电科技65亿定增先进封装+精智达15亿设备合同",
    subtitle="2026.09.03 · 盘后S级催化"
)

# ====== 1. 催化事件概述 ======
gen.add_catalyst_overview(
    overview='<p><strong>【S级重大催化·盘后三响炮】</strong>2026年9月3日盘后，硬科技/半导体产业链迎来多重重磅催化共振，明日A股科技板块或迎来新一轮方向选择：</p>\n<p style="margin-top:8px;"><strong>第一炮（国家级·政策）</strong>：工信部、发改委、科技部、财政部、央行、证监会等<strong>十部门联合印发《促进中小企业发展"十五五"规划》</strong>，明确设立<strong>国家中小企业发展基金二期</strong>，带动社会资本"投早、投小、投长期、投硬科技"，重点投向芯片、半导体、AI、机器人、量子科技、具身智能等前沿领域；提出"推动普惠算力赋能中小企业""高质量建设债券市场科技板""千帆百舸上市培育专项行动"，构建从种子期到IPO的完整资本通道。</p>\n<p style="margin-top:8px;"><strong>第二炮（产业级·资本）</strong>：<strong>长电科技(600584)</strong>公告拟定增募资不超过<strong>65亿元</strong>，全部投向高性能计算先进封装、晶圆级封装、存储芯片封测等五大方向，<strong>控股股东磐石润企亲自认购22.53%</strong>，释放最强产业信心信号。上半年净利增79.41%，先进封装高附加值持续兑现。</p>\n<p style="margin-top:8px;"><strong>第三炮（订单级·业绩）</strong>：<strong>精智达</strong>公告与某客户签订<strong>15.76亿元半导体测试设备采购协议</strong>（预计2年内交付），叠加<strong>亚康股份</strong>下属公司签订<strong>9.22亿元算力租赁协议</strong>，AI算力设备/服务订单持续兑现。</p>\n<p style="margin-top:8px;"><strong>隔夜外盘</strong>：美股终结四连跌，道指+0.56%，纳指+0.45%，费城半导体+0.45%；英伟达+3.21%领涨（市值突破5.4万亿美元），美光+2.43%，SK海力士ADR+2.61%，英特尔+1.21%，阿斯麦+1.03%；AI应用股遭血洗，MongoDB-13%、Palantir-5.81%，"卖铲vs挖矿"分化极致。美国商务部长卢特尼克宣布半导体差异化关税政策（在美建厂免税/低税，海外生产高税）。韩国电力拟向三星/SK海力士预收25万亿韩元（约180亿美元）未来5年电费。</p>\n<p style="margin-top:8px;"><strong>今日A股表现</strong>：三大指数"躺平"微涨（沪指+0.02%，深成+0.10%，创业板+0.01%），但个股普跌（超3500只下跌），成交额缩至1.76万亿。板块分化：AI算力(+4.2%)、存储芯片(+3.5%)、人形机器人(+2.8%)领涨；煤炭、石油石化下跌。龙虎榜机构净卖出1.77亿，游资净流入13.07亿。</p>\n<p style="margin-top:8px;"><strong>核心逻辑</strong>：十部门规划=国家级硬科技长钱入场（政策+资本双轮驱动）；长电科技65亿定增=先进封装产能扩张+控股股东真金白银认购（产业资本信号极强）；精智达15.76亿设备订单=半导体设备国产替代订单兑现（业绩验证）；隔夜美股半导体企稳=外部风险缓解。<strong>四大催化共振，硬科技/先进封装/半导体设备方向明日重点关注。</strong></p>',
    importance="S级"
)

# ====== 2. 催化事件详解 ======
gen.add_catalyst_details(
    background='<p><strong>1. 政策背景：硬科技国家级顶层设计持续加码</strong></p>\n<p>"十五五"规划单独设立"强化生产要素供给"章节，围绕融资、人才、数据三大要素出台系统化政策。较"十四五"最大升级在于：从"政策驱动"转向"资本型培育"，通过国家中小企业发展基金二期+债券市场科技板+上市培育库+专精特新专板，构建覆盖企业全生命周期的直接融资体系。这是继7月政治局会议"硬科技国产替代"定调后，首个落地的万亿级配套政策。</p>\n<p style="margin-top:8px;">值得注意的是，新华社通稿特别提到"前7个月集成电路出口额达2160亿美元，同比增长99.5%，已超2025年全年"，存储器出口同比暴增221.7%占芯片出口总额70.1%。集成电路产业链上市公司上半年净利润同比增长99%，研发费用增长13.4%，行业基本面高景气已获数据验证。</p>\n<p style="margin-top:8px;"><strong>2. 产业背景：先进封装从"可选"变"必选"，HBM/AI算力驱动封测龙头扩产</strong></p>\n<p>全球AI算力需求持续爆发，博通Q3 AI半导体收入167亿美元同比+221%，戴尔AI服务器订单积压950亿美元。CoWoS/HBM等先进封装产能持续供不应求，台积电CoWoS产能2026年预计扩张至月产9万片仍无法满足需求。国内封测三巨头（长电、通富、华天）加速扩产承接订单转移，先进封装成为国产替代确定性最高的环节之一。</p>\n<p style="margin-top:8px;"><strong>3. 外盘背景：美股四连跌后企稳，AI硬件强应用弱格局加剧</strong></p>\n<p>美股9月2日终结此前四连跌，美债收益率盘中触及4.818%（2023年11月以来新高）后回落至4.78%，成为市场反弹触发因素。半导体板块领涨：英伟达+3.21%（35亿美元投资联发科深化AI合作）、美光+2.43%、SK海力士ADR+2.61%；但AI应用软件股集体暴跌（MongoDB-13%、Palantir-5.81%、Datadog-6%），"卖铲子"与"挖矿"分化极致，硬件需求被订单数据验证，应用端变现仍处早期。</p>\n<p style="margin-top:8px;"><strong>4. 国际博弈背景：美国半导体差异化关税+欧盟Chips Act 2.0+韩国电力预收电费</strong></p>\n<p>美国商务部长卢特尼克宣布半导体关税将按产地差异化：在美建厂企业免税/低税，海外生产面临高税率，相当于"市场准入费"。台积电、美光等已承诺约1.2万亿美元在美建厂投资。欧盟委员会同日提出Chips Act 2.0，重点从产能扩张转向需求端，连接芯片制造商与AI数据中心/云厂商。韩国电力拟向三星/SK海力士预收25万亿韩元（约180亿美元）未来5年电费，侧面反映两大存储巨头产能持续扩张、用电需求激增。</p>',

    trigger='<p><strong>🔥 触发一：十部门联合印发"十五五"规划，国家中小企业发展基金二期落地</strong></p>\n<p>规划七大重点任务+七大专项工程同步推出，核心增量政策包括：①设立<strong>国家中小企业发展基金二期</strong>，大力发展创业投资，投早投小投硬科技（芯片/半导体/AI/机器人/量子/具身智能）；②推动<strong>普惠算力赋能中小企业</strong>，降低用算成本，鼓励参与国家级AI开源社区；③<strong>高质量建设债券市场"科技板"</strong>，深化"专精特新"专板建设；④实施<strong>"千帆百舸"上市培育专项行动</strong>，建立优质中小企业上市培育库；⑤到2030年专精特新"小巨人"企业达2.2万家，国家级特色产业集群600个。</p>\n<p style="margin-top:6px;">政策信号明确：硬科技赛道从"炒概念"进入"国家级长线资本+制度性融资通道"双轮驱动阶段，对半导体设备、AI算力、机器人等硬科技方向构成中长期重大利好。</p>\n<p style="margin-top:10px;"><strong>🔥 触发二：长电科技65亿定增加码先进封装，控股股东认购22.53%</strong></p>\n<p>长电科技今晚公告拟定增募资不超过65亿元，五大投向精准卡位AI算力+存储超级周期：①<strong>高性能计算高端先进封装平台扩产</strong>（AI算力芯片封装需求爆发）；②<strong>高端电源模组先进封装测试产能升级</strong>（AI服务器电源管理芯片封装）；③<strong>晶圆级封装先进工艺平台升级扩能</strong>（AI芯片+存储芯片）；④<strong>高密度大容量存储芯片系统级封测能力升级</strong>（全球存储超级周期直接受益）；⑤补充流动资金及还贷。</p>\n<p style="margin-top:6px;">最关键信号：<strong>控股股东磐石润企亲自认购22.53%</strong>。最了解公司价值的内部人真金白银下场，这是产业资本对先进封装景气度最直接的投票。公司上半年归母净利8.45亿元同比+79.41%，先进封装高附加值业务持续释放利润弹性（利润增速是营收增速的16倍）。</p>\n<p style="margin-top:10px;"><strong>🔥 触发三：精智达15.76亿半导体测试设备合同+亚康股份9.22亿算力租赁</strong></p>\n<p>精智达与某客户签订半导体测试设备采购协议，合同总额<strong>15.76亿元（含税）</strong>，预计2年内完成交付。半导体测试设备是半导体设备国产化率最低的环节之一（当前国产化率不足10%），15亿大单验证国产测试设备进入批量放量阶段。亚康股份下属公司签订<strong>9.22亿元算力租赁协议</strong>，算力运营商业模式持续兑现。</p>\n<p style="margin-top:10px;"><strong>🔥 触发四：隔夜美股半导体企稳+英伟达反弹+存储板块全线回暖</strong></p>\n<p>费城半导体指数收涨0.45%报11339点，盘中V形反弹（最低下探11154点后回升）。英伟达+3.21%领涨（市值站上5.4万亿美元，单日增加超1万亿人民币市值），35亿美元投资联发科深化AI基础设施合作。美光+2.43%、SK海力士ADR+2.61%、闪迪+1.08%——存储板块全线回暖。博通盘后一度跌超6%随后转涨（财报电话会期间）。Snowflake盘后大涨22%（Q2业绩超预期）。AI应用股血洗与硬件强势形成极致分化。</p>\n<p style="margin-top:10px;"><strong>🔥 触发五：医保国谈9月5日启动（附带催化·非持仓相关）</strong></p>\n<p>2026年国家医保谈判将于9月5日（周六）正式启动，首次引入8年价格保护等新机制，1类新药连续纳入谈判目录满4年可享降幅减半。创新药板块短期情绪催化，但与持仓4只标的无直接关联，仅作市场情绪参考。</p>'
)

# ====== 3. 产业链分析 ======
gen.add_industry_chain_analysis(
    upstream=[
        {
            'name': '半导体材料（封装材料/前驱体/靶材）',
            'desc': '长电科技65亿扩产先进封装，直接拉动封装材料需求。存储超级周期带动HBM前驱体、环氧塑封料等需求持续高增。雅克科技HBM前驱体+电子特气双主线直接受益。',
            'stocks': [
                {'code': '002409', 'name': '雅克科技', 'impact': '强正面（HBM前驱体龙头+先进封装材料）'},
                {'code': '688535', 'name': '华海诚科', 'impact': '正面（GPM环氧塑封料）'},
                {'code': '688268', 'name': '华特气体', 'impact': '正面（电子特气）'},
            ]
        },
        {
            'name': '电子铜箔（HVM存储铜箔+锂电铜箔）',
            'desc': '前7月存储器出口暴增221.7%验证存储超级周期，HVM高端铜箔量价齐升。铜冠铜箔作为国内电子铜箔龙头，双轮驱动逻辑不变。',
            'stocks': [
                {'code': '301217', 'name': '铜冠铜箔', 'impact': '正面（存储铜箔+锂电铜箔双轮驱动）'},
                {'code': '600110', 'name': '诺德股份', 'impact': '中性偏正面'},
            ]
        },
        {
            'name': '半导体设备（测试设备/光刻/刻蚀/薄膜）',
            'desc': '精智达15.76亿测试设备大单验证国产半导体测试设备进入批量放量期。国家基金二期+十五五规划双重加持，设备国产替代加速。',
            'stocks': [
                {'code': '688627', 'name': '精智达', 'impact': '强正面（15.76亿半导体测试设备合同）'},
                {'code': '688012', 'name': '中微公司', 'impact': '正面（刻蚀设备龙头）'},
                {'code': '688082', 'name': '盛美上海', 'impact': '正面（清洗设备）'},
                {'code': '688037', 'name': '芯源微', 'impact': '正面（涂胶显影）'},
            ]
        },
    ],
    midstream=[
        {
            'name': '先进封装/封测（HPC/HBM/晶圆级）',
            'desc': '长电科技65亿定增加码五大先进封装方向，控股股东认购22.53%释放最强信号。CoWoS产能供不应求，国内封测龙头加速扩产承接订单转移，先进封装进入业绩兑现期。',
            'stocks': [
                {'code': '600584', 'name': '长电科技', 'impact': '强正面（65亿定增+控股股东认购22.53%）'},
                {'code': '002156', 'name': '通富微电', 'impact': '正面（AMD供应链+先进封装）'},
                {'code': '002185', 'name': '华天科技', 'impact': '正面（存储封测）'},
            ]
        },
        {
            'name': '液冷散热/AI温控',
            'desc': 'AI算力集群功耗持续攀升，普惠算力政策+算力租赁大单（亚康9.22亿）验证算力基础设施高景气，液冷散热从可选变必选。英维克今日+3.41%技术面企稳反弹。',
            'stocks': [
                {'code': '002837', 'name': '英维克', 'impact': '正面（液冷龙头+Q2业绩拐点确认）'},
                {'code': '300648', 'name': '申菱环境', 'impact': '正面'},
                {'code': '300449', 'name': '高澜股份', 'impact': '中性偏正面'},
            ]
        },
        {
            'name': '存储芯片（DRAM/NAND/HBM）',
            'desc': '前7月存储器出口+221.7%占芯片出口70.1%，全球存储超级周期数据验证。美光+2.43%、SK海力士ADR+2.61%隔夜回暖。韩国电力预收三星/SK海力士25万亿电费侧面印证产能扩张。',
            'stocks': [
                {'code': '688003', 'name': '长鑫科技', 'impact': '正面（DRAM国产替代龙头）'},
                {'code': '301217', 'name': '铜冠铜箔', 'impact': '正面（HVM存储铜箔）'},
                {'code': '002409', 'name': '雅克科技', 'impact': '正面（HBM前驱体）'},
                {'code': '301308', 'name': '江波龙', 'impact': '正面（存储模组）'},
            ]
        },
        {
            'name': 'AI服务器/算力租赁',
            'desc': '亚康股份9.22亿算力租赁协议验证算力运营商业模式。戴尔AI服务器积压订单950亿美元，博通AI收入+221%，AI算力需求持续爆发。国家普惠算力政策降低中小企业用算成本，扩大算力市场。',
            'stocks': [
                {'code': '000977', 'name': '浪潮信息', 'impact': '正面（AI服务器龙头）'},
                {'code': '603019', 'name': '中科曙光', 'impact': '正面'},
                {'code': '301085', 'name': '亚康股份', 'impact': '强正面（9.22亿算力租赁）'},
            ]
        },
    ],
    downstream=[
        {
            'name': 'AI数据中心/云厂商CSP',
            'desc': '普惠算力政策+国家级AI开源社区建设，直接利好CSP资本开支。博通AI收入+221%验证云厂商AI资本开支持续扩张。欧盟Chips Act 2.0也明确连接芯片厂与AI数据中心。',
            'stocks': [
                {'code': 'NVDA', 'name': '英伟达（美股）', 'impact': '核心风向标（+3.21%，35亿投联发科）'},
                {'code': 'AVGO', 'name': '博通（美股）', 'impact': '核心风向标（AI收入+221%）'},
            ]
        },
        {
            'name': '创投/硬科技母基金（间接受益）',
            'desc': '国家中小企业发展基金二期设立，直接利好创投、产业园区平台、硬科技孵化企业。鲁信创投、张江高科等平台类公司将受益于基金二期杠杆效应和退出通道拓宽（科技板+千帆百舸上市培育）。',
            'stocks': [
                {'code': '600783', 'name': '鲁信创投', 'impact': '正面（创投龙头）'},
                {'code': '600895', 'name': '张江高科', 'impact': '正面（园区+创投）'},
                {'code': '000931', 'name': '中关村', 'impact': '正面（科技园区）'},
            ]
        },
    ]
)

# ====== 4. 投资机会 ======
gen.add_investment_opportunities(
    opportunities=[
        {
            'name': '先进封装封测龙头（S级·产业资本信号最强）',
            'priority': '高',
            'logic': '长电科技65亿定增全部投向先进封装（HPC/晶圆级/存储封测），控股股东磐石润企亲自认购22.53%——这是产业资本用真金白银对先进封装景气度的最强投票。上半年净利+79.41%已验证先进封装高附加值，利润增速是营收16倍。明日先进封装板块有望成为市场最强主线。对标：台积电CoWoS产能供不应求持续扩张，国内封测三巨头加速扩产承接订单转移。',
            'stocks': [
                {'code': '600584', 'name': '长电科技', 'impact': '65亿定增+控股股东认购22.53%+净利+79.41%（直接催化）'},
                {'code': '002156', 'name': '通富微电', 'impact': 'AMD供应链+先进封装扩产（板块联动）'},
                {'code': '002185', 'name': '华天科技', 'impact': '存储封测受益'},
            ]
        },
        {
            'name': '半导体设备国产替代（S级·订单+政策双驱动）',
            'priority': '高',
            'logic': '精智达15.76亿元半导体测试设备大单（2年交付）直接验证国产半导体设备进入批量放量阶段。测试设备是国产化率最低的环节之一（不足10%），替代空间巨大。叠加十部门十五五规划"投硬科技"政策+国家基金二期，半导体设备板块同时获得订单兑现+政策加持+长线资本三重共振。',
            'stocks': [
                {'code': '688627', 'name': '精智达', 'impact': '15.76亿测试设备合同（直接催化）'},
                {'code': '688012', 'name': '中微公司', 'impact': '刻蚀设备龙头+国产替代核心标的'},
                {'code': '688082', 'name': '盛美上海', 'impact': '上半年新签订单+105%'},
                {'code': '688200', 'name': '华峰测控', 'impact': '半导体测试设备龙头'},
            ]
        },
        {
            'name': '国家级硬科技政策受益（A级·中长期）',
            'priority': '中高',
            'logic': '十部门十五五规划设立国家中小企业发展基金二期，直接撬动社会资本投早投小投硬科技，同时配套科技板+上市培育库+专精特新专板等制度性融资通道。中长期利好硬科技各细分赛道龙头，短期偏情绪催化，适合逢低布局有业绩支撑的真硬科技标的，回避纯概念蹭热点。',
            'stocks': [
                {'code': '688082', 'name': '盛美上海', 'impact': '专精特新小巨人+设备龙头'},
                {'code': '688627', 'name': '精智达', 'impact': '专精特新+订单兑现'},
                {'code': '600783', 'name': '鲁信创投', 'impact': '创投龙头间接受益基金二期'},
            ]
        },
        {
            'name': '算力基础设施/液冷散热（B级·持续景气）',
            'priority': '中',
            'logic': '亚康股份9.22亿算力租赁协议+普惠算力政策持续加码+英维克Q2业绩拐点确认，AI算力基础设施高景气持续。英伟达+3.21%隔夜反弹也给算力链提供情绪支撑。但需注意今日市场缩量至1.76万亿，存量博弈下需区分真订单与纯概念。',
            'stocks': [
                {'code': '002837', 'name': '英维克', 'impact': '液冷龙头+Q2业绩拐点（持仓股）'},
                {'code': '301085', 'name': '亚康股份', 'impact': '9.22亿算力租赁合同'},
                {'code': '300648', 'name': '申菱环境', 'impact': '液冷+温控'},
            ]
        },
        {
            'name': '存储芯片超级周期（B级·外盘+数据验证）',
            'priority': '中',
            'logic': '前7月存储器出口+221.7%占芯片出口70.1%的官方数据验证存储超级周期。美光+2.43%、SK海力士ADR+2.61%隔夜存储板块回暖。但板块前期涨幅较大，铜冠铜箔今日-3.72%有获利回吐迹象，需等待企稳信号。',
            'stocks': [
                {'code': '301217', 'name': '铜冠铜箔', 'impact': '存储铜箔+HVM铜箔（持仓股）'},
                {'code': '002409', 'name': '雅克科技', 'impact': 'HBM前驱体+电子特气（持仓股）'},
                {'code': '301308', 'name': '江波龙', 'impact': '存储模组龙头'},
            ]
        },
    ]
)

# ====== 5. 持仓股影响分析 ======
port_section = Section(title="📊 持仓股影响分析 & 操作建议", content='<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px;">\n    <div style="background: linear-gradient(135deg, rgba(34,197,94,0.12) 0%, rgba(22,163,74,0.06) 100%); border-radius: 14px; padding: 18px; border: 1px solid rgba(34,197,94,0.3);">\n        <div style="font-size: 14px; font-weight: 700; color: #4ade80; margin-bottom: 12px;">英维克 (002837) 液冷散热</div>\n        <div style="font-size: 13px; color: #cbd5e1; line-height: 1.9;">\n            <p><strong>收盘价：</strong>68.49元 <span style="color:#4ade80;">+3.41%</span></p>\n            <p><strong>催化影响：</strong><span style="color:#4ade80;"><strong>中性偏正面</strong></span></p>\n            <p>十五五规划"普惠算力"政策+亚康股份9.22亿算力租赁大单，对算力基础设施链形成正面支撑。今日+3.41%反弹，技术面从50元低点持续修复，成交额71.4亿量能充沛。</p>\n            <p><strong>双重验证</strong>：①Q2业绩环比暴增1934%已确认（公司公告）；②今日龙虎榜持仓股未上榜，资金面平稳。无重大利空。</p>\n            <p><strong>估值锚</strong>：成本104.23元（深度套牢-34.3%），当前PE(TTM)约42倍，技术压力位70元（整数关+前期平台），支撑位65元（5日线）。</p>\n            <p><strong>操作建议：</strong>持有为主。70元附近若遇阻可小幅减机动仓（不超过1/3），回踩65元以下可低吸。当前距离成本仍远，不割肉、不追高，波段操作摊低成本。止损维持50元最后防线。</p>\n        </div>\n    </div>\n    <div style="background: linear-gradient(135deg, rgba(245,158,11,0.12) 0%, rgba(217,119,6,0.06) 100%); border-radius: 14px; padding: 18px; border: 1px solid rgba(245,158,11,0.3);">\n        <div style="font-size: 14px; font-weight: 700; color: #fbbf24; margin-bottom: 12px;">铜冠铜箔 (301217) 电子铜箔</div>\n        <div style="font-size: 13px; color: #cbd5e1; line-height: 1.9;">\n            <p><strong>收盘价：</strong>104.84元 <span style="color:#f87171;">-3.72%</span></p>\n            <p><strong>催化影响：</strong><span style="color:#fbbf24;"><strong>中性（短期获利回吐+长期利好）</strong></span></p>\n            <p>今日高开低走（开111.11→收104.84，振幅8.5%），获利盘兑现压力明显。但盘后长电科技65亿定增存储封测+存储器出口+221.7%数据+美光/海力士隔夜上涨，对存储链形成正面支撑。</p>\n            <p><strong>双重验证</strong>：①半年报净利+514.75%已公告（8/26）；②今日下跌为正常技术调整，无利空公告。</p>\n            <p><strong>估值锚</strong>：成本87.16元（浮盈+20.3%），动态PE约48倍（中报摊薄后），技术支撑位100元（整数关）/103元（今日低点），压力位112元（今日高点）。</p>\n            <p><strong>操作建议：</strong>持有，成本有安全垫。若明日跌破100元且放量，减仓1/3锁定利润；若能企稳105元以上则继续持有，目标位115-120元。</p>\n        </div>\n    </div>\n    <div style="background: linear-gradient(135deg, rgba(34,197,94,0.12) 0%, rgba(22,163,74,0.06) 100%); border-radius: 14px; padding: 18px; border: 1px solid rgba(34,197,94,0.3);">\n        <div style="font-size: 14px; font-weight: 700; color: #4ade80; margin-bottom: 12px;">雅克科技 (002409) 半导体材料 ⭐长电定增直接受益</div>\n        <div style="font-size: 13px; color: #cbd5e1; line-height: 1.9;">\n            <p><strong>收盘价：</strong>131.60元 <span style="color:#4ade80;">+0.58%</span></p>\n            <p><strong>催化影响：</strong><span style="color:#4ade80;"><strong>正面（长电65亿扩产先进封装+HBM需求+存储回暖）</strong></span></p>\n            <p>长电科技65亿定增中有高密度大容量存储芯片封测+晶圆级封装项目，直接拉动封装材料需求；HBM前驱体+电子特气双主线受益于HBM扩产+存储超级周期。今日微涨0.58%站稳130元。</p>\n            <p><strong>双重验证</strong>：①H1净利5.61亿+7.3%已公告；②长电科技定增公告已核实（上交所披露）；③无减持/利空公告。</p>\n            <p><strong>估值锚</strong>：成本108.80元（浮盈+21.0%），PE(TTM)约55倍，技术压力位135元/140元（前高），支撑位125元（20日线）。</p>\n            <p><strong>操作建议：</strong>持有底仓，长电定增催化下明日有望联动上涨。135-140元区间减30%机动仓锁定利润，回踩125元附近接回。中期目标150元。</p>\n        </div>\n    </div>\n    <div style="background: linear-gradient(135deg, rgba(239,68,68,0.1) 0%, rgba(220,38,38,0.05) 100%); border-radius: 14px; padding: 18px; border: 1px solid rgba(239,68,68,0.25);">\n        <div style="font-size: 14px; font-weight: 700; color: #f87171; margin-bottom: 12px;">*ST建艺 (002789)</div>\n        <div style="font-size: 13px; color: #cbd5e1; line-height: 1.9;">\n            <p><strong>收盘价：</strong>11.77元 <span style="color:#4ade80;">+0.43%</span></p>\n            <p><strong>催化影响：</strong><span style="color:#f87171;"><strong>无关联</strong></span></p>\n            <p>今日盘后所有重磅催化均与ST建艺无直接关联。公司仍处于庭外重组阶段，退市风险未解除。</p>\n            <p><strong>风险提示：</strong>上半年预亏1.1-1.6亿元，新增诉讼仲裁4401万元，被列为失信被执行人。</p>\n            <p><strong>估值锚</strong>：成本13.45元（浮亏-12.5%），止损位12.5元（已跌破）。</p>\n            <p><strong>操作建议：</strong>坚决回避，逢反弹减仓/清仓，不浪费仓位在ST股上。科技主线行情明确，资金应配置到确定性更高的硬科技标的。</p>\n        </div>\n    </div>\n</div>\n<p style="margin-top: 10px; font-size: 12px; color: #94a3b8;">注：以上分析基于公开信息整理，不构成投资建议。双重验证：长电科技65亿定增来自上交所公告+界面新闻+财联社三源交叉验证；精智达15.76亿合同来自公司公告+界面新闻确认；十部门规划来自中国政府网+新华社+工信部官网确认；持仓股价/成交数据来自腾讯财经实时数据。</p>', icon="briefcase")
gen._components.append(port_section)

# ====== 6. 隔夜外盘扫描 ======
overnight_section = Section(title="🌍 隔夜外盘扫描（V4.0强制）", content='<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px;">\n    <div style="background: rgba(59,130,246,0.08); border-radius: 12px; padding: 16px; border: 1px solid rgba(59,130,246,0.2);">\n        <div style="font-size: 14px; font-weight: 700; color: #93c5fd; margin-bottom: 10px;">📈 美股主要指数（9/2收盘）</div>\n        <div style="font-size: 13px; color: #cbd5e1; line-height: 2;">\n            <p>道琼斯：53061.95 <span style="color:#4ade80;">+0.56%</span>（终结四连跌）</p>\n            <p>标普500：7666.60 <span style="color:#4ade80;">+0.46%</span></p>\n            <p>纳斯达克：26217.83 <span style="color:#4ade80;">+0.45%</span></p>\n            <p>费城半导体：11339.25 <span style="color:#4ade80;">+0.45%</span>（盘中V形反转）</p>\n            <p>VIX恐慌指数：15.29 <span style="color:#4ade80;">-6.43%</span></p>\n        </div>\n    </div>\n    <div style="background: rgba(168,85,247,0.08); border-radius: 12px; padding: 16px; border: 1px solid rgba(168,85,247,0.2);">\n        <div style="font-size: 14px; font-weight: 700; color: #c084fc; margin-bottom: 10px;">💴 亚太/欧洲市场</div>\n        <div style="font-size: 13px; color: #cbd5e1; line-height: 2;">\n            <p>日经225：44946.64 <span style="color:#f87171;">-0.90%</span>（日元加息预期）</p>\n            <p>韩国KOSPI：V型反转 <span style="color:#4ade80;">+1.07%</span>（三星/SK海力士涨近1%）</p>\n            <p>恒生指数：25213.31 <span style="color:#f87171;">-0.39%</span></p>\n            <p>富时100：9284.83 <span style="color:#4ade80;">+0.77%</span></p>\n        </div>\n    </div>\n    <div style="background: rgba(245,158,11,0.08); border-radius: 12px; padding: 16px; border: 1px solid rgba(245,158,11,0.2);">\n        <div style="font-size: 14px; font-weight: 700; color: #fcd34d; margin-bottom: 10px;">🔥 核心半导体标的</div>\n        <div style="font-size: 13px; color: #cbd5e1; line-height: 2;">\n            <p>英伟达 NVDA：224.41 <span style="color:#4ade80;">+3.21%</span>（35亿投联发科）</p>\n            <p>美光 MU：956.08 <span style="color:#4ade80;">+2.43%</span>（存储龙头回暖）</p>\n            <p>SK海力士 ADR：164.98 <span style="color:#4ade80;">+2.61%</span></p>\n            <p>英特尔 INTC：90.05 <span style="color:#4ade80;">+1.21%</span></p>\n            <p>阿斯麦 ASML：1682.30 <span style="color:#4ade80;">+1.03%</span></p>\n            <p>台积电 TSM：415.50 <span style="color:#4ade80;">+0.36%</span></p>\n            <p>AMD：457.06 <span style="color:#f87171;">-0.55%</span></p>\n            <p>博通 AVGO：367.24 <span style="color:#f87171;">-0.66%</span>（盘后波动）</p>\n        </div>\n    </div>\n    <div style="background: rgba(239,68,68,0.08); border-radius: 12px; padding: 16px; border: 1px solid rgba(239,68,68,0.2);">\n        <div style="font-size: 14px; font-weight: 700; color: #fca5a5; margin-bottom: 10px;">💀 AI应用股血洗</div>\n        <div style="font-size: 13px; color: #cbd5e1; line-height: 2;">\n            <p>MongoDB：<span style="color:#f87171;">-13%+</span></p>\n            <p>Palantir：169.46 <span style="color:#f87171;">-5.81%</span></p>\n            <p>Datadog：<span style="color:#f87171;">-6%+</span></p>\n            <p>Snowflake盘后：<span style="color:#4ade80;">+22%</span>（业绩超预期）</p>\n            <p>信号：市场区分"卖铲vs挖矿"，硬件订单强，应用变现早</p>\n        </div>\n    </div>\n    <div style="background: rgba(34,197,94,0.08); border-radius: 12px; padding: 16px; border: 1px solid rgba(34,197,94,0.2);">\n        <div style="font-size: 14px; font-weight: 700; color: #86efac; margin-bottom: 10px;">💰 大宗商品/债市</div>\n        <div style="font-size: 13px; color: #cbd5e1; line-height: 2;">\n            <p>COMEX黄金：4483.3 <span style="color:#4ade80;">+1.56%</span></p>\n            <p>COMEX白银：66.52 <span style="color:#4ade80;">+1.62%</span></p>\n            <p>WTI原油：91.54 <span style="color:#4ade80;">+0.59%</span></p>\n            <p>10Y美债：4.78%（盘中4.818%创2023/11来新高）</p>\n            <p>30Y美债：5.275%（2007年来高位）</p>\n            <p>8月ADP就业仅增3.7万（远低预期）</p>\n        </div>\n    </div>\n    <div style="background: rgba(99,102,241,0.08); border-radius: 12px; padding: 16px; border: 1px solid rgba(99,102,241,0.2);">\n        <div style="font-size: 14px; font-weight: 700; color: #a5b4fc; margin-bottom: 10px;">📰 关键国际事件</div>\n        <div style="font-size: 13px; color: #cbd5e1; line-height: 2;">\n            <p>🇺🇸 卢特尼克：半导体差异化关税</p>\n            <p>🇺🇸 台积电/美光等承诺在美投资1.2万亿美元</p>\n            <p>🇪🇺 欧盟Chips Act 2.0（连接芯片厂+AI数据中心）</p>\n            <p>🇰🇷 韩国电力拟向三星/SK海力士预收25万亿电费</p>\n            <p>🇺🇸 周五非农数据成关键（预期+5.5万）</p>\n        </div>\n    </div>\n</div>\n<p style="margin-top: 10px; font-size: 12px; color: #94a3b8;">数据来源：新浪财经、FX168、Financial News、财联社 | 2026.09.03 20:00盘后</p>', icon="globe")
gen._components.append(overnight_section)

# ====== 7. 龙虎榜分析 ======
dragon_section = Section(title="🐯 龙虎榜机构资金动向", content='<div style="background: rgba(245,158,11,0.06); border-radius: 14px; padding: 20px; border: 1px solid rgba(245,158,11,0.2);">\n    <div style="font-size: 15px; font-weight: 700; color: #fcd34d; margin-bottom: 16px;">\n        <span style="margin-right: 8px;">🐯</span>龙虎榜机构动向（9月3日）\n    </div>\n    <div style="font-size: 13px; color: #cbd5e1;">\n        <p style="margin-bottom: 12px;">9月3日两市缩量调整（成交1.76万亿，3500+个股下跌），龙虎榜共53只个股上榜。<strong>机构净卖出1.77亿元</strong>（买入17.43亿/卖出19.20亿），<strong>游资净买入13.07亿元</strong>，北向净卖出4437万。市场情绪偏谨慎，游资主导短线热点，机构态度偏防御。</p>\n        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-top: 12px;">\n            <div style="background: rgba(34,197,94,0.06); border-radius: 10px; padding: 12px; border: 1px solid rgba(34,197,94,0.15);">\n                <div style="font-weight: 600; color: #4ade80; margin-bottom: 8px;">游资净买入TOP5</div>\n                <div style="font-size: 12px; line-height: 1.9;">\n                    <p>1. 黄河旋风(600172)：<span style="color:#4ade80;">+2.82亿</span> | 涨7.93%</p>\n                    <p>2. 白银有色(601212)：<span style="color:#4ade80;">+2.43亿</span> | 涨停</p>\n                    <p>3. 飞龙股份(002536)：<span style="color:#4ade80;">+1.72亿</span> | 涨8.54%</p>\n                    <p>4. 思泉新材(301489)：<span style="color:#4ade80;">+1.69亿</span> | 20CM涨停</p>\n                    <p>5. 光洋股份(002708)：<span style="color:#4ade80;">+1.64亿</span> | 涨停</p>\n                </div>\n            </div>\n            <div style="background: rgba(239,68,68,0.06); border-radius: 10px; padding: 12px; border: 1px solid rgba(239,68,68,0.15);">\n                <div style="font-weight: 600; color: #f87171; margin-bottom: 8px;">板块资金动向</div>\n                <div style="font-size: 12px; line-height: 1.9;">\n                    <p>• 有色金属：净买3.49亿（机构+790万）</p>\n                    <p>• 成长股：净买7644万（机构-1343万）</p>\n                    <p>• 半导体/科技：净卖962万（机构0）</p>\n                    <p>• 医药生物：净卖1.19亿</p>\n                    <p>• 机构净买TOP：华盛昌+5366万</p>\n                </div>\n            </div>\n        </div>\n        <div style="margin-top: 14px; padding: 12px; background: rgba(59,130,246,0.06); border-radius: 10px; border: 1px solid rgba(59,130,246,0.15);">\n            <div style="font-weight: 600; color: #60a5fa; margin-bottom: 8px;">💡 龙虎榜核心解读</div>\n            <div style="font-size: 12px; line-height: 1.9; color: #cbd5e1;">\n                <p>• 持仓4股均未登上龙虎榜，资金面平稳无异常信号。</p>\n                <p>• 思泉新材（散热材料）20CM涨停获游资1.69亿净买入，与液冷散热方向形成题材联动，关注对英维克情绪传导。</p>\n                <p>• 飞龙股份连发异动公告提示"非车业务占比低"，纯题材炒作不追。</p>\n                <p>• 机构净卖出1.77亿幅度较小（<成交额5%），按V4.0铁规不构成看空信号，视为正常调仓。</p>\n            </div>\n        </div>\n        <p style="margin-top: 14px; font-size: 12px; color: #94a3b8;">数据来源：东方财富龙虎榜、证券时报·数据宝 | 2026.09.03</p>\n    </div>\n</div>', icon="activity")
gen._components.append(dragon_section)

# ====== 8. 风险提示 ======
gen.add_risk_warning([
    '美国半导体差异化关税政策风险：卢特尼克宣布海外生产面临高税率，可能冲击亚洲晶圆厂成本结构',
    '长电科技65亿定增稀释效应：定增发行价通常折价10-20%，短期可能对股价形成压制',
    '十部门十五五规划为中长期政策，短期偏情绪催化，可能出现"利好兑现高开低走"',
    '精智达15.76亿合同客户未具名，合同执行存在不确定性',
    '铜冠铜箔今日高开低走-3.72%，短期获利盘压力大',
    'AI应用股隔夜暴跌（MongoDB-13%），市场风格极致偏向硬件',
    '美10Y国债4.78%（30Y5.275%为2007年来高位），高利率压制风险资产估值，周五非农是关键',
    '韩国电力预收三星/SK海力士25万亿电费，可能增加存储巨头成本',
    '市场缩量至1.76万亿，存量博弈下板块轮动加快',
    '*ST建艺退市风险未解除，坚决回避',
    '本报告不构成投资建议，股市有风险，投资需谨慎'
])

# ====== 9. 投资策略 ======
gen.add_investment_strategy('''
<p><strong>【整体判断】</strong>9月3日盘后迎来S级多重催化共振：<strong>十部门"十五五"规划（国家级政策）+长电科技65亿定增（产业资本信号）+精智达15.76亿设备合同（订单兑现）+隔夜美股半导体企稳（外部风险缓解）</strong>，四大催化集中指向硬科技/先进封装/半导体设备方向。但需注意：今日市场缩量至1.76万亿、个股普跌、机构净卖出、美债收益率高位，整体情绪偏谨慎，明日大概率是<strong>结构性机会而非普涨</strong>，聚焦最确定的先进封装主线。</p>

<p style="margin-top:12px;"><strong>【明日关键观察点】</strong></p>
<ul style="margin-top:8px; padding-left: 20px; line-height: 2; color: #e2e8f0;">
    <li><strong>长电科技开盘表现</strong>：65亿定增+控股股东认购是今晚最强催化，若高开高走放量封板将带动整个先进封装板块；若高开低走则说明市场解读为稀释利空。</li>
    <li><strong>精智达开盘表现</strong>：15.76亿测试设备大单，若20CM涨停将引爆半导体设备板块。</li>
    <li><strong>两市成交额</strong>：若回到1.9万亿以上则反弹有量，若继续缩量至1.7万亿以下则反弹乏力。</li>
    <li><strong>周五（9/5）美国非农数据</strong>：预期新增5.5万，若不及预期强化9月降息预期。</li>
</ul>

<p style="margin-top:12px;"><strong>【仓位建议】</strong>整体仓位维持<strong>5-6成</strong>，核心持仓不追高、不割肉。盘后催化集中在先进封装/半导体设备，若明日高开过多（>5%）不追，等待回踩确认。预留资金应对周五非农波动。</p>

<p style="margin-top:12px;"><strong>【方向优先级排序】</strong></p>
<ol style="margin-top:8px; padding-left: 20px; line-height: 2; color: #e2e8f0;">
    <li><strong>🥇 第一优先级：先进封装/封测</strong> — 长电科技65亿定增+控股股东认购22.53%是今晚最强产业信号</li>
    <li><strong>🥈 第二优先级：半导体设备</strong> — 精智达15.76亿订单+国家基金二期+十五五规划三重共振</li>
    <li><strong>🥉 第三优先级：HBM/半导体材料</strong> — 长电扩产+HBM需求+存储超级周期，雅克科技直接受益</li>
    <li>第四优先级：液冷散热/算力基础设施 — 英维克持有为主</li>
    <li>第五优先级：创投/硬科技母基金 — 中长期受益基金二期</li>
</ol>

<p style="margin-top:12px;"><strong>【持仓股具体操作】</strong></p>
<ul style="margin-top:8px; padding-left: 20px; line-height: 2; color: #e2e8f0;">
    <li><strong>英维克(002837)</strong>：持有，70元遇阻减1/3机动仓，回踩65元低吸，止损50元</li>
    <li><strong>铜冠铜箔(301217)</strong>：持有，跌破100元放量减1/3锁利，企稳105元以上持有至115-120元</li>
    <li><strong>雅克科技(002409)</strong>：持有底仓，135-140元减30%机动仓，回踩125元接回，中期目标150元</li>
    <li><strong>*ST建艺(002789)</strong>：逢反弹减仓/清仓，坚决回避</li>
</ul>

<p style="margin-top:12px;"><strong>【核心风险提醒】</strong>十部门规划为中长期政策≠明天全涨，需精选有业绩+有订单的真龙头；长电定增存在折价稀释效应不追高；缩量+高位美债+周五非农三大压力仍在，控制仓位第一。</p>
''')

print("开始生成S级催化盘后报告...")
html = gen.generate()
print(f"报告生成完成，长度: {len(html)} 字符")

result = gen.publish(
    title="硬科技国家级催化：十部门十五五规划+长电科技65亿定增先进封装+精智达15亿设备合同",
    report_type="s_level_catalyst",
    filename="20260903_盘后_S级催化扫描_硬科技国家级催化+长电65亿定增.html",
    excerpt="S级催化：十部门联合印发十五五规划设立国家中小企业发展基金二期投硬科技+长电科技65亿定增加码先进封装控股股东认购22.53%+精智达15.76亿半导体测试设备合同+隔夜美股半导体企稳英伟达+3.21%。",
    auto_deploy=True,
    docs_root="docs"
)
print(f"发布结果: {result}")
print("任务完成！")
