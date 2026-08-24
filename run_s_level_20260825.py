import sys, os
sys.path.insert(0, os.path.join(os.getcwd(), 'v3'))

from v3.generators.s_level_catalyst import SLevelCatalystGenerator
from components.layout import Section

gen = SLevelCatalystGenerator(
    date_str='20260825',
    catalyst_title='美股半导体暴跌：存储股崩盘+英伟达财报前避险',
    subtitle='2026.08.25 · 盘前S级催化预警'
)

# 1. 催化事件概述
gen.add_catalyst_overview(
    overview='''
    <strong>隔夜美股半导体板块遭遇重挫</strong>，费城半导体指数（SOX）收跌约2.7%，盘中一度跌超4%，报11265.94点。存储板块领跌，美光科技（MU）跌近6%，闪迪（SNDK）跌超6%，西部数据（WDC）跌超5%，SK海力士（SKHY）跌近5%。英伟达连续第7个交易日下跌，创2022年以来最长连跌纪录，市值跌破5.1万亿美元。
    <br><br>
    <strong>三大核心诱因：</strong>①传言特朗普政府或允许苹果向中国存储厂商（长鑫/长江存储）采购芯片，引发存储股恐慌性抛售；②三星电子公布90-110万亿韩元股东回报方案低于预期，股价暴跌超6%拖累板块情绪；③英伟达周三盘后财报前市场普遍减仓避险，叠加美联储主席沃什Jackson Hole讲话不确定性。
    <br><br>
    <strong>对A股影响判断：</strong>今日科技板块（半导体、存储、AI算力）面临显著低开压力，需警惕情绪传导。但国产替代逻辑（特别是存储国产替代）反而可能因"苹果采购中国存储"传闻获得短期情绪催化——长鑫/长江存储供应链存在结构性机会。
    ''',
    importance='高'
)

# 2. 隔夜外盘扫描模块
overnight_html = '''
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 12px; margin-bottom: 16px;">
    <div style="background: linear-gradient(135deg, rgba(239,68,68,0.15) 0%, rgba(185,28,28,0.08) 100%); border-radius: 12px; padding: 16px; border: 1px solid rgba(239,68,68,0.25); text-align: center;">
        <div style="font-size: 12px; color: #fca5a5; margin-bottom: 4px;">费城半导体指数</div>
        <div style="font-size: 22px; font-weight: 800; color: #f87171;">-2.7%</div>
        <div style="font-size: 11px; color: #94a3b8; margin-top: 2px;">报11,265.94点</div>
    </div>
    <div style="background: linear-gradient(135deg, rgba(239,68,68,0.15) 0%, rgba(185,28,28,0.08) 100%); border-radius: 12px; padding: 16px; border: 1px solid rgba(239,68,68,0.25); text-align: center;">
        <div style="font-size: 12px; color: #fca5a5; margin-bottom: 4px;">纳斯达克综合</div>
        <div style="font-size: 22px; font-weight: 800; color: #f87171;">-0.76%</div>
        <div style="font-size: 11px; color: #94a3b8; margin-top: 2px;">日线7连阴</div>
    </div>
    <div style="background: linear-gradient(135deg, rgba(239,68,68,0.15) 0%, rgba(185,28,28,0.08) 100%); border-radius: 12px; padding: 16px; border: 1px solid rgba(239,68,68,0.25); text-align: center;">
        <div style="font-size: 12px; color: #fca5a5; margin-bottom: 4px;">美光科技 (MU)</div>
        <div style="font-size: 22px; font-weight: 800; color: #f87171;">-5.83%</div>
        <div style="font-size: 11px; color: #94a3b8; margin-top: 2px;">存储龙头领跌</div>
    </div>
    <div style="background: linear-gradient(135deg, rgba(239,68,68,0.15) 0%, rgba(185,28,28,0.08) 100%); border-radius: 12px; padding: 16px; border: 1px solid rgba(239,68,68,0.25); text-align: center;">
        <div style="font-size: 12px; color: #fca5a5; margin-bottom: 4px;">英伟达 (NVDA)</div>
        <div style="font-size: 22px; font-weight: 800; color: #f87171;">-2.91%</div>
        <div style="font-size: 11px; color: #94a3b8; margin-top: 2px;">7连跌创纪录</div>
    </div>
</div>

<div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 12px;">
    <div style="background: rgba(255,255,255,0.04); border-radius: 12px; padding: 14px; border: 1px solid rgba(255,255,255,0.08);">
        <div style="font-size: 14px; font-weight: 700; color: #f1f5f9; margin-bottom: 10px; display: flex; align-items: center;">
            <span style="margin-right: 6px;">🇺🇸</span>美股核心半导体个股表现
        </div>
        <div style="display: flex; flex-direction: column; gap: 6px; font-size: 13px;">
            <div style="display: flex; justify-content: space-between;"><span style="color: #94a3b8;">闪迪 (SNDK)</span><span style="color: #f87171; font-weight: 600;">-6.45%</span></div>
            <div style="display: flex; justify-content: space-between;"><span style="color: #94a3b8;">美光科技 (MU)</span><span style="color: #f87171; font-weight: 600;">-5.83%</span></div>
            <div style="display: flex; justify-content: space-between;"><span style="color: #94a3b8;">西部数据 (WDC)</span><span style="color: #f87171; font-weight: 600;">-5.24%</span></div>
            <div style="display: flex; justify-content: space-between;"><span style="color: #94a3b8;">英特尔 (INTC)</span><span style="color: #f87171; font-weight: 600;">-3.12%</span></div>
            <div style="display: flex; justify-content: space-between;"><span style="color: #94a3b8;">超威半导体 (AMD)</span><span style="color: #f87171; font-weight: 600;">-3.49%</span></div>
            <div style="display: flex; justify-content: space-between;"><span style="color: #94a3b8;">台积电 (TSM)</span><span style="color: #f87171; font-weight: 600;">-2.11%</span></div>
            <div style="display: flex; justify-content: space-between;"><span style="color: #94a3b8;">博通 (AVGO)</span><span style="color: #f87171; font-weight: 600;">-2.63%</span></div>
            <div style="display: flex; justify-content: space-between;"><span style="color: #94a3b8;">应用材料 (AMAT)</span><span style="color: #f87171; font-weight: 600;">-1.65%</span></div>
            <div style="display: flex; justify-content: space-between;"><span style="color: #94a3b8;">泛林集团 (LRCX)</span><span style="color: #f87171; font-weight: 600;">-1.22%</span></div>
            <div style="display: flex; justify-content: space-between;"><span style="color: #94a3b8;">科磊 (KLAC)</span><span style="color: #f87171; font-weight: 600;">-1.32%</span></div>
        </div>
    </div>
    
    <div style="background: rgba(255,255,255,0.04); border-radius: 12px; padding: 14px; border: 1px solid rgba(255,255,255,0.08);">
        <div style="font-size: 14px; font-weight: 700; color: #f1f5f9; margin-bottom: 10px; display: flex; align-items: center;">
            <span style="margin-right: 6px;">🌏</span>亚洲市场与产业动态
        </div>
        <div style="display: flex; flex-direction: column; gap: 8px; font-size: 13px; color: #cbd5e1; line-height: 1.6;">
            <div>
                <span style="color: #fbbf24; font-weight: 600;">🇰🇷 三星暴跌6%+：</span>
                公布90-110万亿韩元史上最大股东回报方案，但市场认为缺乏明确回购承诺，回购/分红比例未明确，引发"利好出尽"抛售。SK海力士逆势微涨，40万亿韩元回购+50%自由现金流返还更显诚意。
            </div>
            <div>
                <span style="color: #60a5fa; font-weight: 600;">🇰🇷 韩系存储扩产中国：</span>
                三星西安X2产线启动V9型NAND转型投资（280层，月产4-5万片），SK海力士大连二厂推进NAND升级，核心刻蚀设备下月进场，目标明上半年月产3万片。
            </div>
            <div>
                <span style="color: #a78bfa; font-weight: 600;">🇹🇼 台积电：</span>
                A16（1.6nm级）工艺完成开发验证，Q4量产；先进封装CoWoS产能供不应求，部分订单外溢至英特尔马来西亚厂。小米玄戒O3 AI芯片采用台积电3nm制程。
            </div>
            <div>
                <span style="color: #34d399; font-weight: 600;">🇨🇳 国内政策：</span>
                上海发布"十五五"新型工业化规划，强化集成电路/生物医药/AI三大先导产业，推进高性能算力芯片、存储芯片达国际先进水平。
            </div>
        </div>
    </div>
</div>
'''

overnight_section = Section(title='🌍 隔夜全球扫描（强制核查）', content=overnight_html, icon='globe', variant='highlight')
gen._components.append(overnight_section)

# 3. 催化事件详解
gen.add_catalyst_details(
    background='''
    美股半导体板块经历今年以来最剧烈的调整之一。费城半导体指数从7月高点累计回调已超15%，英伟达连续7个交易日下跌，累计跌幅超15%，市值从5.9万亿美元蒸发至5.05万亿美元。
    <br><br>
    存储板块是本轮调整的重灾区。美光科技从历史高点回调超20%，闪迪、西部数据、SK海力士等存储股同步走弱。
    此前存储板块因AI算力需求爆发，股价已累计上涨100%-200%，估值处于历史高位，获利盘丰厚，任何利空都可能引发剧烈的获利回吐。
    ''',
    trigger='''
    <strong>直接导火索：</strong>周末传言特朗普政府可能允许苹果从中国存储厂商（长鑫CXMT采购DRAM、长江存储YMTC采购NAND）采购芯片，作为习9月访美前的"善意"姿态。市场担忧美光等美国存储厂商丢失苹果订单。
    <br><br>
    <strong>催化放大器：</strong>
    ① 三星电子股东回报方案低于预期，韩股三星暴跌超6%，拖累存储板块情绪
    ② 英伟达周三盘后财报前，全板块减仓避险（历史规律：财报日即使超预期也常下跌2%）
    ③ 特朗普宣布对加拿大汽车、钢铁征收50%关税，贸易紧张情绪升温
    ④ 美联储主席沃什Jackson Hole讲话不确定性，市场担忧鹰派表态
    ⑤ 10年期美债收益率维持在4.7%高位，压制科技股估值
    '''
)

# 4. 产业链梳理
gen.add_industry_chain_analysis(
    upstream=[
        {
            'name': '半导体设备',
            'desc': '海外设备商交期延长至1.5-2倍，国产设备替代窗口加速打开。韩国设备商订单积压翻番。',
            'stocks': [
                {'code': '002371', 'name': '北方华创', 'impact': '设备龙头'},
                {'code': '688012', 'name': '中微公司', 'impact': '刻蚀设备'},
                {'code': '688072', 'name': '拓荆科技', 'impact': '薄膜沉积'},
            ]
        },
        {
            'name': '半导体材料',
            'desc': '存储扩产带动前驱体、光刻胶、特气等材料需求，国产替代持续推进。',
            'stocks': [
                {'code': '002409', 'name': '雅克科技', 'impact': '前驱体+光刻胶'},
                {'code': '688519', 'name': '南大光电', 'impact': '光刻胶'},
            ]
        }
    ],
    midstream=[
        {
            'name': '存储芯片（DRAM/NAND/HBM）',
            'desc': 'AI驱动HBM需求持续紧张，国产存储替代加速。长江存储NAND全球市占率第三，长鑫科技DRAM份额紧追。美光暴跌事件反向强化国产替代逻辑。',
            'stocks': [
                {'code': '688825', 'name': '长鑫科技', 'impact': '国产DRAM龙头'},
                {'code': '603986', 'name': '兆易创新', 'impact': 'NOR Flash+DRAM'},
                {'code': '301308', 'name': '江波龙', 'impact': '存储模组'},
                {'code': '688525', 'name': '佰维存储', 'impact': '存储模组+H1净利71亿'},
            ]
        },
        {
            'name': 'AI芯片/算力',
            'desc': '英伟达财报前市场谨慎，关注数据中心业务指引及新一代芯片路线图。AI硬件仍是全年最强主线，但短期估值消化压力较大。',
            'stocks': [
                {'code': '688256', 'name': '寒武纪', 'impact': '国产AI芯片'},
                {'code': '688396', 'name': '华海诚科', 'impact': '先进封装材料'},
            ]
        },
        {
            'name': '液冷散热',
            'desc': 'AI算力密度提升带动液冷刚需，国产液冷进入批量交付阶段。英维克Q2业绩环比大幅改善，CDU开始出货。',
            'stocks': [
                {'code': '002837', 'name': '英维克', 'impact': '液冷全链条龙头'},
                {'code': '300499', 'name': '高澜股份', 'impact': '液冷散热'},
            ]
        }
    ],
    downstream=[
        {
            'name': '光模块/光通信',
            'desc': '新易盛H1净利75亿同比+91%，二季度环比+70%。光模块业绩持续超预期，但板块情绪受半导体整体拖累。',
            'stocks': [
                {'code': '300502', 'name': '新易盛', 'impact': '光模块龙头'},
                {'code': '300308', 'name': '中际旭创', 'impact': '光模块龙头'},
            ]
        },
        {
            'name': '铜箔/PCB',
            'desc': 'AI服务器带动高端HVLP铜箔供不应求，头部公司酝酿新一轮涨价。嘉元科技H1净利同比+940%。',
            'stocks': [
                {'code': '301217', 'name': '铜冠铜箔', 'impact': '锂电+PCB铜箔'},
                {'code': '688388', 'name': '嘉元科技', 'impact': '锂电铜箔龙头'},
            ]
        }
    ]
)

# 5. 催化深度分析
gen.add_catalyst_deep_analysis([
    {
        'title': '美股半导体暴跌事件',
        'type': 'data',
        'description': '费城半导体指数跌2.7%，存储股领跌，英伟达7连跌创纪录，市场担忧存储竞争格局变化和财报前风险',
        'category': '全球市场'
    },
    {
        'title': '苹果采购中国存储芯片传闻',
        'type': 'policy',
        'description': '特朗普政府或允许苹果从长鑫/长江存储采购芯片，引发美光等美国存储厂商份额担忧，但分析认为短期影响有限（CXMT良率低、仅单一Mac产品）',
        'category': '产业政策'
    },
    {
        'title': '英伟达财报前避险',
        'type': 'earnings',
        'description': '英伟达周三盘后发布Q2财报，市场预期数据中心营收超854亿美元，同比+107%，但历史规律显示财报日常下跌2%',
        'category': '公司业绩'
    }
])

# 6. 投资机会分析
gen.add_investment_opportunities([
    {
        'name': '存储国产替代：反向催化机会',
        'priority': '高',
        'logic': '''美光暴跌的核心逻辑是"苹果可能采购中国存储"——虽然短期实际影响有限（CXMT良率低、仅单一产品），但这一事件方向上强化了中国存储厂商崛起的产业趋势。长江存储NAND已跻身全球第三，长鑫科技DRAM份额快速提升。如果美国政府真的放开限制，意味着中国存储产品品质已获得苹果级认可，对国产存储产业链是里程碑式的利好。
        <br><br>
        重点关注：<strong>长鑫科技（国产DRAM龙头）、佰维存储（H1净利71亿+企业级SSD）、江波龙、兆易创新</strong>，以及存储设备/材料供应链。''',
        'stocks': [
            {'code': '688825', 'name': '长鑫科技', 'impact': '核心受益'},
            {'code': '688525', 'name': '佰维存储', 'impact': '业绩高增'},
            {'code': '002371', 'name': '北方华创', 'impact': '设备受益'},
        ]
    },
    {
        'name': '半导体设备：海外交期延长=国产替代加速',
        'priority': '高',
        'logic': '''韩媒报道：应用材料、ASML、泛林、科磊五大设备商交付周期已延长至1.5-2倍（6个月→约1年）；韩国设备商订单积压较去年底翻番。中国存储扩产（长鑫5-6万片/年、长江存储武汉三期）叠加海外交期延长，国产设备采购比例将进一步提升。
        <br><br>
        长鑫科技新一代产线国产设备占比有望超40%，长江存储武汉三期核心工序国产化率已超60%。设备是半导体板块确定性最高的细分赛道之一。''',
        'stocks': [
            {'code': '002371', 'name': '北方华创', 'impact': '平台型龙头'},
            {'code': '688012', 'name': '中微公司', 'impact': '刻蚀龙头'},
            {'code': '688072', 'name': '拓荆科技', 'impact': '薄膜沉积'},
            {'code': '688082', 'name': '盛美上海', 'impact': '清洗设备'},
        ]
    },
    {
        'name': '液冷：Q3业绩兑现期临近',
        'priority': '中',
        'logic': '''英维克H1中报显示Q2营收18.41亿（环比+56.67%），归母净利1.76亿（环比+1934%），毛利率25.24%环比提升。飞龙股份已披露开始给英维克发货泵，CDU发货在即。Q3液冷初步业绩兑现窗口临近。
        <br><br>
        但需注意：板块整体受情绪拖累，英维克估值已较高（PE超2000倍），建议等待回调后低吸，不宜追高。''',
        'stocks': [
            {'code': '002837', 'name': '英维克', 'impact': '液冷龙头'},
            {'code': '300499', 'name': '高澜股份', 'impact': '液冷散热'},
        ]
    },
    {
        'name': '铜箔：业绩验证+涨价预期',
        'priority': '中',
        'logic': '''嘉元科技H1净利3.82亿同比+940%，扣非同比+1653%。高端HVLP铜箔供不应求，头部公司酝酿新一轮涨价。AI算力硬件迭代是核心驱动力。
        <br><br>
        铜冠铜箔近期回调较多（周跌6.7%），但基本面持续向好，短期有超跌反弹机会。估值相对科技板块其他赛道更有安全边际。''',
        'stocks': [
            {'code': '301217', 'name': '铜冠铜箔', 'impact': '铜箔龙头'},
            {'code': '688388', 'name': '嘉元科技', 'impact': '业绩高增'},
        ]
    }
], view_mode='tab')

# 7. 投资策略建议
gen.add_investment_strategy(
    strategy='''
    <strong>一、今日操作总策略：先防御，再出击</strong>
    <br><br>
    <strong>1. 开盘策略：低开不恐慌，高开不追涨</strong><br>
    受美股半导体暴跌影响，今日A股科技板块大概率低开。持仓股如有大幅低开（-3%以上），<strong>禁止恐慌割肉</strong>。原因：本轮下跌核心驱动是美股情绪传导+英伟达财报前避险，而非基本面恶化。国产存储甚至有反向催化。
    <br><br>
    <strong>2. 仓位管理：整体维持中性偏谨慎</strong><br>
    建议总仓位控制在<strong>60%-70%</strong>，保留30%+现金应对波动。等待英伟达财报（周三晚）落地后再加仓。
    <br><br>
    <strong>3. 持仓股具体操作指引（双重验证原则）：</strong>
    <ul style="margin-top: 8px; padding-left: 20px; line-height: 2;">
        <li><strong>英维克（002837）：</strong>液冷基本面持续向好（Q2业绩环比大增+CDU出货在即），本次下跌属板块情绪带动，<strong>持有为主</strong>。若低开超5%可考虑小幅加仓（不超过总仓位5%）。估值锚：2026年一致预期PE超100倍，偏高，不追高。</li>
        <li><strong>铜冠铜箔（301217）：</strong>行业景气度高（涨价+业绩大增），近期已回调6.7%，继续大跌空间有限。<strong>持有+逢低加仓</strong>。估值锚：2026年PE约20倍，在科技板块中具安全边际。</li>
        <li><strong>雅克科技（002409）：</strong>半导体材料龙头，存储扩产受益。上周跌停后已反弹，本次美股半导体下跌可能带来二次探底压力。<strong>底仓持有，不加仓</strong>。等待站稳145元以上再考虑加仓。估值锚：动态PE 62.7倍，行业合理偏高。</li>
        <li><strong>*ST建艺：</strong>独立行情，与半导体板块关联度低，按原有策略持有。</li>
    </ul>
    <br>
    <strong>4. 出击方向（若低开企稳后）：</strong><br>
    优先级：<strong>存储国产替代 ＞ 半导体设备 ＞ 铜箔 ＞ 液冷</strong>
    <br>
    存储方向是本次事件中唯一有"反向催化"逻辑的板块，值得重点关注。设备是全年确定性最高赛道，回调即是加仓机会。
    <br><br>
    <strong>5. 风险控制：</strong><br>
    若英伟达财报不及预期（周三晚），可能引发第二轮下跌，届时需严格执行止损纪律。单只个股跌幅超10%必须减仓50%。
    '''
)

# 8. 风险提示
gen.add_risk_warning([
    '英伟达财报不及预期风险：若数据中心业务指引低于市场预期，可能引发科技板块第二轮深度调整',
    '美联储主席沃什Jackson Hole讲话鹰派风险：加息预期升温将压制科技股估值',
    '中美关系反复：苹果采购中国存储芯片传闻存在不确定性，政策方向可能快速变化',
    '半导体板块估值偏高：前期涨幅大，获利盘丰厚，任何利空都可能引发剧烈波动',
    '贸易摩擦升级：特朗普对加拿大加征关税，贸易保护主义抬头影响全球市场情绪'
])

# 生成并发布
result = gen.publish(
    title='S级催化预警：美股半导体暴跌',
    filename='20260825_盘前_S级催化扫描_美股半导体暴跌.html',
    excerpt='费城半导体指数跌2.7%，美光科技跌近6%，存储股集体崩盘。三大诱因：苹果采购中国存储传闻+三星股东回报不及预期+英伟达财报前避险。A股科技板块承压，但存储国产替代有反向催化机会。'
)
print('Publish result:', result)
