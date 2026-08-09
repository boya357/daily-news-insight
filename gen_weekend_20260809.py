"""
周末速递 2026-08-09 生成脚本
"""
import sys, os
sys.path.insert(0, '/root/daily-news-insight/v3')
os.chdir('/root/daily-news-insight')

from v3.generators.weekend_express import WeekendExpressGenerator

gen = WeekendExpressGenerator(
    date_str='20260809', 
    subtitle='2026.08.09 · 周末速递 · 北京楼市新政+宇树科技IPO+存储超级周期延续'
)

# ============ 1. 周末要闻速览 ============
highlights = [
    {
        'icon': '🏛️',
        'title': '北京出台重磅楼市新政：限购松绑+公积金贷款翻倍',
        'content': '8月7日晚北京市住建委等三部门联合发文，非京籍家庭购五环内商品房社保/个税年限由2年降至1年，全市统一1年门槛。公积金贷款额度大幅提升：夫妻双缴存首套最高240万元（原120万翻倍），叠加多子女/绿色建筑/城六区外购房等上浮条件，最高可达340万元。同时取消公积金贷款两次上限、支持装修提取公积金（最高25万）、扩大带押过户范围。政策自8月8日起施行，北京限购政策来到2011年以来最宽松阶段。上海已于年初将社保年限全面降至1年，一线城市限购核心维度已基本实现实质性松绑。',
        'tag': '重磅政策',
        'importance': 'high',
        'source': '新华网/北京市住建委',
        'time': '8月7日晚'
    },
    {
        'icon': '🤖',
        'title': '宇树科技8月10日科创板申购 发行价150.80元',
        'content': 'A股"人形机器人第一股"宇树科技将于8月10日开启网上申购，发行价150.80元/股，对应发行市值609.9亿元，预计募资约60.99亿元。网上申购代码"787836"，顶格申购需1万沪市市值，中一签（500股）需缴款7.54万元。公司2025年营收16.99亿元，净利润2.88亿元，毛利率60%，是少数实现盈利的人形机器人企业。本次IPO拟募资中智能机器人模型研发投入20.22亿元首次超过本体研发（11.1亿元），行业从"卷身体"转向"卷大脑"。',
        'tag': 'IPO/打新',
        'importance': 'high',
        'source': '每日经济新闻/财联社',
        'time': '8月9日'
    },
    {
        'icon': '💰',
        'title': '央行下半年工作会议定调：继续实施适度宽松货币政策',
        'content': '中国人民银行8月1日召开2026年下半年工作会议，明确继续实施好适度宽松的货币政策，综合运用并适时调整货币政策工具，保持流动性充裕。促进降低融资中间费用，保持社会综合融资成本低位运行。聚焦扩大内需、科技创新和中小微企业等重点领域，下调结构性货币政策工具利率，增加科技创新和技术改造再贷款等额度。招联首席经济学家董希淼解读：下半年政策重心或将从"精准滴灌"转向"适时加力、提质增效"，降准降息均有可能适时启用。',
        'tag': '货币政策',
        'importance': 'high',
        'source': '新华网/中国人民银行',
        'time': '8月1日'
    },
    {
        'icon': '💾',
        'title': 'SK海力士390亿美元新建两座晶圆厂 存储紧缺或延续至2027',
        'content': 'SK海力士批准约54万亿韩元（约390亿美元）新建两座晶圆厂：龙仁第二工厂35.2万亿韩元、清州NAND新工厂19.1万亿韩元，定位为"保障供应能力而非追逐周期"。Transcend警告全球存储紧缺可能延续至2027年，2027年供应或比2026年更紧张。英伟达测试低内存版本Rubin Ultra GPU，HBM短缺已开始重塑AI芯片规格设计。三星管理层预计存储供应短缺将持续至2028年。',
        'tag': '存储芯片',
        'importance': 'normal',
        'source': 'DIGITIMES/中国电子报',
        'time': '8月7日'
    },
    {
        'icon': '⚛️',
        'title': '国常会核准4个核电项目8台机组 总投资超1700亿',
        'content': '7月31日国务院常务会议决定核准辽宁庄河一期、浙江金七门二期、广东太平岭三期、山东莱阳一期共4个核电项目8台百万千瓦机组，总投资超1700亿元。这是今年核电审批常态化的延续，2022-2025年我国连续四年每年核准10台及以上核电机组。会议同时部署高质量建设新型电网、加快推进物流网建设，以及推动医药科技创新。',
        'tag': '国常会/能源',
        'importance': 'normal',
        'source': '央视新闻/澎湃新闻',
        'time': '7月31日'
    },
    {
        'icon': '🏭',
        'title': '马斯克Terafab超级芯片工厂动工 初期投资168亿美元',
        'content': 'SpaceX官网确认超级芯片工厂Terafab选址得州格莱姆斯县破土动工，SpaceX和特斯拉初期投资168亿美元，未来扩建阶段投资额可能"大幅增加"。工厂旨在为特斯拉、SpaceX和xAI保障AI芯片供应。英伟达测试低内存版本Rubin Ultra GPU，反映HBM供应紧张已开始重塑AI芯片领袖的产品规格，云厂商可能需要重新评估大模型所需GPU数量。',
        'tag': '海外科技',
        'importance': 'normal',
        'source': 'SpaceX官网/界面新闻',
        'time': '8月7日'
    }
]
gen.add_weekend_highlights(highlights)

# ============ 2. 政策解读 ============
policies = [
    {
        'title': '北京楼市新政：限购松绑+公积金翻倍 一线城市调控实质性转向',
        'content': '8月7日晚北京市住建委、规自委、公积金中心三部门联合印发《关于进一步优化调整本市房地产政策的通知》，推出7项政策措施：①非京籍家庭购五环内商品房社保/个税年限由2年降至1年，全市统一1年门槛；②公积金贷款额度大幅提升，夫妻双缴存首套最高240万元（原120万翻倍），叠加上浮条件最高可达340万元；③优化缴存年限挂钩机制，单人每年可贷20万、夫妻每年40万；④取消公积金贷款两次上限，结清后可再次申请；⑤扩大带押过户范围支持公积金贷款房屋；⑥支持装修提取公积金（最高25万）；⑦完善房屋赠与政策，父母赠与成年子女不再核验购房资格。政策自8月8日起施行。',
        'impact': '北京作为一线城市政策风向标，此次政策力度超预期，释放清晰的"稳楼市"信号。北京限购政策来到2011年以来最宽松阶段。短期直接利好北京本地地产、家居建材板块；中期看，上海、广州、深圳等其他一线城市大概率跟进优化，全国房地产政策空间正在打开。但行业真正复苏仍需经济基本面和市场信心配合，政策可以托底但反转需要时间。',
        'sector': '房地产, 家居建材, 家电消费',
        'level': '地方重磅'
    },
    {
        'title': '央行下半年工作会议：适度宽松+适时调整 降准降息可期',
        'content': '央行8月1日召开2026年下半年工作会议，核心要点：①继续实施好适度宽松的货币政策，综合运用并适时调整货币政策工具，保持流动性充裕；②保持社会综合融资成本低位运行，促进降低融资中间费用；③聚焦扩大内需、科技创新和中小微企业，下调结构性货币政策工具利率，增加科技创新和技术改造再贷款等额度；④高质量建设债券市场"科技板"，累计发行科技创新债券超2.8万亿元；⑤发挥两项支持资本市场货币政策工具的作用，稳定和增强资本市场信心；⑥稳妥化解重点领域风险，推进融资平台市场化转型；⑦稳步扩大外汇领域制度型开放，推出一揽子跨境投融资便利化政策。',
        'impact': '货币政策总基调延续"适度宽松"，但新增"适时调整"的弹性表述，释放出下半年政策主动性、前瞻性将进一步增强的信号。降准降息仍是储备工具，7月政治局会议明确"加大逆周期调节力度"。流动性环境维持友好，有助于提升资本市场整体风险偏好，成长赛道、顺周期板块有望迎来估值修复环境。科技金融"五篇大文章"持续加力，科创企业融资环境继续改善。',
        'sector': '全市场, 科技成长, 券商',
        'level': '国家'
    },
    {
        'title': '国常会核准8台核电机组+新型电网+物流网三箭齐发',
        'content': '7月31日国常会重点部署四大方向：①核准辽宁庄河一期、浙江金七门二期、广东太平岭三期、山东莱阳一期共4个核电项目8台机组，总投资超1700亿元，要求按全球最高安全标准建设运营；②高质量建设新型电网，加强统筹协调和政策支持，满足日益增长的用电需求，促进绿色低碳转型；③加快推进物流网建设，增强枢纽节点、骨干通道功能，完善城乡末端配送体系；④审议通过《住房公积金管理条例》修改草案，拓宽提取和使用范围；⑤推动医药科技创新，深化医药卫生体制改革。',
        'impact': '核电项目集中获批标志国内核电建设节奏进一步提速，核电作为新型电力系统重要基荷电源，全产业链中长期催化明确。新型电网建设直接受益于AI算力扩张带来的用电需求增长，特高压、智能电网、储能板块景气具备持续性。物流网建设对供应链、快递物流、冷链等形成长期利好。',
        'sector': '核电, 特高压, 智能电网, 储能',
        'level': '国家'
    },
    {
        'title': '人形机器人8月超级催化月 产业化进程加速',
        'content': '多重催化共振推动人形机器人进入产业化加速期：①宇树科技8月10日科创板申购，A股"人形机器人第一股"正式登场，发行价150.80元，市值609.9亿；②工信部联合国资委印发专项行动文件，推动人形机器人脱离演示展厅、进入真实生产场景常态化作业；③上半年具身智能赛道融资总额1217亿元，已超2025年全年67%，其中近一半投向"大脑派"企业；④市场监管总局数据显示上半年人形机器人领域新设企业11.6万户，同比增长9.5%；⑤2026年全年人形机器人整机产量有望突破10万台，较2025年2万台实现一年五倍跃升。',
        'impact': '宇树科技上市将带动人形机器人产业链价值重估，核心零部件供应商（减速器、电机、传感器）最直接受益。但行业仍处于早期阶段，70%以上销量来自科研教育领域，工业应用仅占9%，商业化落地能力是核心分化变量。资本正从"硬件身体"转向"AI大脑"，具备自研大模型能力的企业将享有估值溢价。操作上建议关注有真实订单的核心零部件龙头，规避纯概念标的。',
        'sector': '人形机器人, 减速器, 伺服电机, 传感器',
        'level': '行业'
    }
]
gen.add_policy_interpretation(policies, view_mode='card')

# ============ 3. 下周题材预判 ============
topics = [
    {
        'name': '存储芯片/HBM超级周期延续',
        'probability': '高确定性',
        'logic': 'SK海力士批准390亿美元新建两座晶圆厂，定位保障供应而非追周期；Transcend警告存储紧缺延续至2027年；英伟达测试低内存版Rubin Ultra GPU，HBM短缺重塑芯片规格。产业端三大存储厂商业绩集体爆发：SK海力士DRAM均价环比涨30%、NAND涨50%；三星存储营收同比飙升471%；铠侠净利润一年翻45倍。AI驱动存储需求结构性增长，HBM/服务器DDR5/企业级SSD三大高景气赛道供需紧张格局中长期不变。但需注意板块前期涨幅大，高位波动加剧。',
        'stocks': ['雅克科技', '铜冠铜箔', '佰维存储', '澜起科技', '德明利', '东芯股份'],
        'category': '科技成长',
        'rating': '强烈推荐'
    },
    {
        'name': 'PCB/铜箔产业链景气上行',
        'probability': '高确定性',
        'logic': '高盛上调AI服务器PCB市场空间38%至2028年840亿美元；AI服务器PCB价值量是普通服务器的3-5倍；铜箔板块周五掀涨停潮，方邦股份20cm涨停，铜冠铜箔盘中涨停收涨16.98%。高频高速铜箔供不应求，铜冠铜箔上半年净利润预增486%-543%。刚果金禁运铜钴精矿导致LME铜创年内新高，成本端支撑铜箔价格。AI算力+新能源汽车双轮驱动，高端铜箔缺口持续扩大。周五板块放量大涨，资金介入明显，下周有望延续强势。',
        'stocks': ['铜冠铜箔', '方邦股份', '诺德股份', '胜宏科技', '沪电股份', '深南电路'],
        'category': '科技成长',
        'rating': '强烈推荐'
    },
    {
        'name': '液冷散热：AI算力刚需 订单加速兑现',
        'probability': '高确定性',
        'logic': '英伟达GB300/Rubin系列强制全液冷，谷歌TPU V8单芯片功耗高达1300W，传统风冷彻底退出高端AI算力场景。液冷渗透率从2024年14%快速提升至2026年40%，中金预计2026年全球AI液冷市场规模达86亿美元，IDC预计中国液冷服务器市场2024-2029年CAGR达46.8%。英维克在手订单超85亿元，谷歌+英伟达7月新增CDU订单约10亿元；浪潮信息液冷服务器占比从40%跃升至85%。行业处于订单加速兑现期，但板块前期调整幅度大，股价与基本面背离。',
        'stocks': ['英维克', '高澜股份', '申菱环境', '飞龙股份', '中石科技', '同飞股份'],
        'category': '科技成长',
        'rating': '推荐'
    },
    {
        'name': '人形机器人产业化加速 宇树上市催化',
        'probability': '中确定性',
        'logic': '宇树科技8月10日科创板申购，人形机器人第一股上市将带动板块情绪；上半年具身智能融资1217亿超去年全年67%；工信部推动机器人进入真实生产场景；2026年整机产量有望突破10万台（2025年2万台）。但商业化仍处早期，70%收入来自科研教育，工业应用仅9%，硬件跑得快但智能跟不上是核心瓶颈。资本从"身体"转向"大脑"，具身智能大模型成新方向。宇树上市后板块情绪有望冲高，但需警惕利好兑现回调。',
        'stocks': ['绿的谐波', '双环传动', '拓普集团', '三花智控', '鸣志电器', '贝斯特'],
        'category': '科技成长',
        'rating': '推荐'
    },
    {
        'name': '北京楼市新政+地产链修复预期',
        'probability': '中确定性',
        'logic': '北京出台重磅楼市新政，限购松绑+公积金贷款翻倍，一线城市调控实质性转向。政策力度超预期，信号意义重大，其他一线城市大概率跟进。短期利好北京本地地产股和家居建材，中期关注政策传导效果和销量修复。但行业基本面反转仍需经济和信心配合，不宜过度乐观。从投资角度，政策底已现但市场底尚需确认，更适合左侧分批布局而非追高。',
        'stocks': ['京能置业', '首开股份', '北辰实业', '东方雨虹', '伟星新材', '兔宝宝'],
        'category': '顺周期',
        'rating': '关注'
    },
    {
        'name': '核电+新型电网建设提速',
        'probability': '高确定性',
        'logic': '国常会一次性核准4个核电项目8台机组，总投资超1700亿元，核电审批常态化。新型电网建设纳入国家战略，AI算力扩张带来用电需求持续增长。核电作为基荷电源，兼具稳定供电和降碳双重价值，全产业链从设备到材料到运营持续受益。板块估值低、业绩稳，是稳健资金的优选方向。AI数据中心的电力需求增长也为电网建设带来新增量。',
        'stocks': ['中国核电', '中国广核', '东方电气', '上海电气', '沃尔核材', '江苏神通'],
        'category': '稳增长',
        'rating': '推荐'
    }
]
gen.add_next_week_topics(topics, view_mode='tab')

# ============ 4. 下周事件日历 ============
from v3.components.layout import Section

event_calendar_html = '''
<div style="display: flex; flex-direction: column; gap: 12px;">
    <div style="border-left: 4px solid #3b82f6; border-radius: 0 12px 12px 0; background: rgba(30, 41, 59, 0.7); backdrop-filter: blur(12px); border: 1px solid rgba(148, 163, 184, 0.1); padding: 14px 18px;">
        <div style="display: flex; align-items: center; margin-bottom: 10px;">
            <span style="background: linear-gradient(135deg, #3b82f6, #1d4ed8); color: white; padding: 4px 12px; border-radius: 20px; font-size: 12px; font-weight: 600; margin-right: 10px;">8月10日 周一</span>
            <span style="color: #94a3b8; font-size: 12px;">5项重要事件</span>
        </div>
        <div style="font-size: 13px; color: #e2e8f0; line-height: 1.8;">
            <p style="margin: 4px 0;">📈 <strong>宇树科技科创板申购</strong>：发行价150.80元/股，申购代码787836，顶格申购6000股。人形机器人第一股上市，将带动机器人产业链情绪。影响板块：人形机器人、减速器、伺服电机。</p>
            <p style="margin: 4px 0;">🔓 <strong>陆家嘴7.79亿股限售股解禁</strong>：占总股本15.47%，但控股股东自愿承诺12个月内不转让，实际抛压有限。关注地产板块情绪。</p>
            <p style="margin: 4px 0;">🏠 <strong>北京楼市新政正式实施</strong>：限购松绑+公积金翻倍全面落地，观察地产链和家居建材板块反应。</p>
            <p style="margin: 4px 0;">📰 <strong>中报密集披露</strong>：伟星新材、天合光能等多家公司披露中报。</p>
            <p style="margin: 4px 0;">🔬 <strong>长鑫科技纳入MSCI中国指数生效</strong>：被动资金配置带来增量买盘，关注对科创50和半导体板块的带动效应。</p>
        </div>
    </div>
    
    <div style="border-left: 4px solid #10b981; border-radius: 0 12px 12px 0; background: rgba(30, 41, 59, 0.7); backdrop-filter: blur(12px); border: 1px solid rgba(148, 163, 184, 0.1); padding: 14px 18px;">
        <div style="display: flex; align-items: center; margin-bottom: 10px;">
            <span style="background: linear-gradient(135deg, #10b981, #059669); color: white; padding: 4px 12px; border-radius: 20px; font-size: 12px; font-weight: 600; margin-right: 10px;">8月11日 周二</span>
            <span style="color: #94a3b8; font-size: 12px;">3项重磅事件</span>
        </div>
        <div style="font-size: 13px; color: #e2e8f0; line-height: 1.8;">
            <p style="margin: 4px 0;">🇺🇸 <strong>美国7月CPI数据公布（重点关注）</strong>：此前6月CPI为3.5%低于预期3.8%，若7月继续回落，美联储降息预期将升温，直接影响全球科技股估值和北向资金流向。是下周最重要的数据。</p>
            <p style="margin: 4px 0;">💰 <strong>中国7月社融/M2数据</strong>：7月政治局会议后首份金融数据，观察信贷需求是否回暖，是判断经济复苏力度的重要风向标。</p>
            <p style="margin: 4px 0;">📱 <strong>腾讯控股中期业绩</strong>：微信生态+云业务+游戏三驾马车表现，关注AI相关业务进展和资本开支情况。</p>
        </div>
    </div>
    
    <div style="border-left: 4px solid #f59e0b; border-radius: 0 12px 12px 0; background: rgba(30, 41, 59, 0.7); backdrop-filter: blur(12px); border: 1px solid rgba(148, 163, 184, 0.1); padding: 14px 18px;">
        <div style="display: flex; align-items: center; margin-bottom: 10px;">
            <span style="background: linear-gradient(135deg, #f59e0b, #d97706); color: white; padding: 4px 12px; border-radius: 20px; font-size: 12px; font-weight: 600; margin-right: 10px;">8月12日 周三</span>
            <span style="color: #94a3b8; font-size: 12px;">4项重要事件</span>
        </div>
        <div style="font-size: 13px; color: #e2e8f0; line-height: 1.8;">
            <p style="margin: 4px 0;">🇺🇸 <strong>美国7月PPI数据</strong>：继CPI后的另一通胀数据，若低于预期将强化降息预期。</p>
            <p style="margin: 4px 0;">🔓 <strong>风神股份1.17亿股限售股解禁</strong>：占总股本13.12%，14名股东6个月限售期满，需警惕抛压。</p>
            <p style="margin: 4px 0;">💰 <strong>宇树科技中签结果+缴款</strong>：中签投资者需确保账户有足额资金。</p>
            <p style="margin: 4px 0;">🛒 <strong>京东集团中期业绩</strong>：关注消费复苏和AI零售进展。</p>
        </div>
    </div>
    
    <div style="border-left: 4px solid #8b5cf6; border-radius: 0 12px 12px 0; background: rgba(30, 41, 59, 0.7); backdrop-filter: blur(12px); border: 1px solid rgba(148, 163, 184, 0.1); padding: 14px 18px;">
        <div style="display: flex; align-items: center; margin-bottom: 10px;">
            <span style="background: linear-gradient(135deg, #8b5cf6, #7c3aed); color: white; padding: 4px 12px; border-radius: 20px; font-size: 12px; font-weight: 600; margin-right: 10px;">8月13日 周四</span>
            <span style="color: #94a3b8; font-size: 12px;">4项重要事件</span>
        </div>
        <div style="font-size: 13px; color: #e2e8f0; line-height: 1.8;">
            <p style="margin: 4px 0;">🇺🇸 <strong>美国初请失业金人数</strong>：劳动力市场数据，若走弱将强化降息预期。</p>
            <p style="margin: 4px 0;">🍶 <strong>贵州茅台中期业绩</strong>：消费龙头业绩，观察白酒消费复苏情况。</p>
            <p style="margin: 4px 0;">🔬 <strong>中芯国际中期业绩</strong>：半导体制造龙头业绩，观察国产替代进度和资本开支。</p>
            <p style="margin: 4px 0;">⛽ <strong>国内成品油调价窗口</strong>：本轮计价周期内国际油价波动，关注调价方向和幅度。</p>
        </div>
    </div>
    
    <div style="border-left: 4px solid #ef4444; border-radius: 0 12px 12px 0; background: rgba(30, 41, 59, 0.7); backdrop-filter: blur(12px); border: 1px solid rgba(148, 163, 184, 0.1); padding: 14px 18px;">
        <div style="display: flex; align-items: center; margin-bottom: 10px;">
            <span style="background: linear-gradient(135deg, #ef4444, #dc2626); color: white; padding: 4px 12px; border-radius: 20px; font-size: 12px; font-weight: 600; margin-right: 10px;">8月14日 周五</span>
            <span style="color: #94a3b8; font-size: 12px;">3项重磅事件</span>
        </div>
        <div style="font-size: 13px; color: #e2e8f0; line-height: 1.8;">
            <p style="margin: 4px 0;">🏭 <strong>中国7月工业增加值/社零/固投数据</strong>：月度经济数据集中公布，判断经济复苏力度的重要指标。工业增加值看制造业复苏，社零看消费回暖。</p>
            <p style="margin: 4px 0;">📊 <strong>美国密歇根大学消费者信心指数初值</strong>：美国消费信心数据，影响美联储政策判断。</p>
            <p style="margin: 4px 0;">🗓️ <strong>中报披露高峰</strong>：本周五将有大量公司披露中报，注意业绩雷风险，尤其是绩差股和高估值标的。</p>
        </div>
    </div>
</div>
'''

event_section = Section(title="📅 下周重大事件日历", content=event_calendar_html, icon="calendar")
gen._components.insert(2, event_section)

# ============ 5. 持仓股周末复盘 ============
portfolio_html = '''
<div style="display: flex; flex-direction: column; gap: 14px;">
    <div style="background: linear-gradient(135deg, rgba(16,185,129,0.10) 0%, rgba(5,150,105,0.06) 100%); border: 1px solid rgba(16,185,129,0.3); border-radius: 14px; padding: 16px 18px;">
        <div style="display: flex; align-items: center; margin-bottom: 12px;">
            <span style="font-size: 16px; font-weight: 700; color: #059669; flex: 1;">铜冠铜箔 (301217)</span>
            <span style="background: linear-gradient(135deg, #10b981, #059669); color: white; padding: 4px 10px; border-radius: 6px; font-size: 13px; font-weight: 600;">收115.81元 +16.98%</span>
        </div>
        <div style="font-size: 13px; color: #cbd5e1; line-height: 1.8;">
            <p><strong>📊 本周表现：</strong>周涨约+17%，周五放量大涨+16.98%收115.81元，盘中触及20cm涨停，成交额88.37亿，换手率9.57%。龙虎榜显示3日机构净卖出1.27亿元，北向资金净买入342万元。</p>
            <p><strong>🔥 关键催化：</strong>①高盛上调AI服务器PCB市场空间38%至2028年840亿美元；②刚果金禁运铜钴精矿，LME铜创年内新高；③高频高速铜箔供不应求，上半年净利润预增486%-543%；④铜箔板块掀涨停潮（方邦股份20cm涨停、诺德股份涨停）。</p>
            <p><strong>🎯 下周关键价位：</strong>压力位125-130元、强压力140元；支撑位105-100元、强支撑95元；止盈线100元（跌破止盈离场）。</p>
            <p><strong>📋 操作计划：</strong>目前浮盈约+33%，下周高开冲120-125元减仓至1/3底仓锁定利润（兑现约2/3仓位）；若冲高至130元以上继续减仓；回踩100-105元可接回底仓；跌破100元无条件止盈离场保住利润。仓位从当前降至底仓1/3，等待回调后再评估加仓机会。</p>
        </div>
    </div>
    
    <div style="background: linear-gradient(135deg, rgba(16,185,129,0.10) 0%, rgba(5,150,105,0.06) 100%); border: 1px solid rgba(16,185,129,0.3); border-radius: 14px; padding: 16px 18px;">
        <div style="display: flex; align-items: center; margin-bottom: 12px;">
            <span style="font-size: 16px; font-weight: 700; color: #059669; flex: 1;">雅克科技 (002409)</span>
            <span style="background: linear-gradient(135deg, #10b981, #059669); color: white; padding: 4px 10px; border-radius: 6px; font-size: 13px; font-weight: 600;">收148.78元 +2.60%</span>
        </div>
        <div style="font-size: 13px; color: #cbd5e1; line-height: 1.8;">
            <p><strong>📊 本周表现：</strong>周涨约+3%，周五+2.60%收148.78元，成交额46.77亿，换手率9.93%。大宗交易成交624.88万元，买方为机构专用。主力资金净流入3770万元。从高点回撤约30%后逐步企稳。</p>
            <p><strong>🔥 关键催化：</strong>①存储超级周期延续，HBM前驱体需求持续增长；②SK海力士390亿美元扩产，上游材料需求增加；③英伟达测试低内存版Rubin Ultra，HBM短缺重塑AI芯片格局；④电子特气+半导体材料双主线逻辑。</p>
            <p><strong>🎯 下周关键价位：</strong>压力位155-160元、强压力170元；支撑位140-142元、强支撑135元；止盈线140元（跌破减至底仓）。</p>
            <p><strong>📋 操作计划：</strong>目前浮盈约+37%，150-155元减仓1/3锁利；160元以上减仓至半仓持有；150元附近可维持现有仓位观察；跌破142元止盈至底仓（1/4）；跌破135元清仓止盈。核心底仓继续持有，HBM长期逻辑不变但短期需防板块轮动。</p>
        </div>
    </div>
    
    <div style="background: linear-gradient(135deg, rgba(245,158,11,0.10) 0%, rgba(217,119,6,0.06) 100%); border: 1px solid rgba(245,158,11,0.3); border-radius: 14px; padding: 16px 18px;">
        <div style="display: flex; align-items: center; margin-bottom: 12px;">
            <span style="font-size: 16px; font-weight: 700; color: #d97706; flex: 1;">英维克 (002837)</span>
            <span style="background: linear-gradient(135deg, #f59e0b, #d97706); color: white; padding: 4px 10px; border-radius: 6px; font-size: 13px; font-weight: 600;">收55.90元 +5.61%</span>
        </div>
        <div style="font-size: 13px; color: #cbd5e1; line-height: 1.8;">
            <p><strong>📊 本周表现：</strong>周涨约+6%，周五+5.61%收55.90元，成交额28.97亿，换手率4.66%。主力资金净流入3.42亿元（占总成交额11.81%）。从高点93.52元回撤约40%，深度破止损状态下超跌反弹。液冷板块跟随科技修复但弱于PCB/铜箔。</p>
            <p><strong>🔥 关键催化：</strong>①在手订单超85亿元，谷歌+英伟达7月新增CDU订单约10亿元；②液冷渗透率快速提升（2026年40%），AI算力刚需；③数据中心概念周五主力净流入34.21亿元，板块回暖。</p>
            <p><strong>🎯 下周关键价位：</strong>压力位60-65元、强压力70元；支撑位52-53元、强支撑50元；止损线52元（二次跌破清仓）。</p>
            <p><strong>📋 操作计划：</strong>目前深度浮亏约-46%，反弹60-65元区间坚决减仓≥1/2（降低持仓风险）；若反弹至70元以上继续减仓至1/3底仓；二次跌破52元无条件清仓离场，绝不补仓抄底。反弹减仓是第一要务，液冷板块中期趋势仍未反转，需控制仓位。</p>
        </div>
    </div>
    
    <div style="background: linear-gradient(135deg, rgba(239,68,68,0.10) 0%, rgba(220,38,38,0.06) 100%); border: 1px solid rgba(239,68,68,0.3); border-radius: 14px; padding: 16px 18px;">
        <div style="display: flex; align-items: center; margin-bottom: 12px;">
            <span style="font-size: 16px; font-weight: 700; color: #dc2626; flex: 1;">*ST建艺 (002789)</span>
            <span style="background: linear-gradient(135deg, #ef4444, #dc2626); color: white; padding: 4px 10px; border-radius: 6px; font-size: 13px; font-weight: 600;">收9.83元 -5.30%</span>
        </div>
        <div style="font-size: 13px; color: #cbd5e1; line-height: 1.8;">
            <p><strong>📊 本周表现：</strong>周跌约-5%，周五-5.30%收9.83元，成交额仅4280万，换手率2.74%。主力资金净流出532.88万元。披露重大诉讼事项（涉资2179.63万元）。退市风险+债务问题+诉讼三重压力，成交低迷流动性枯竭。</p>
            <p><strong>⚠️ 风险因素：</strong>①一季度亏损5311万，毛利率仅2.55%，负债率94.38%；②重大诉讼事项增加不确定性；③退市风险警示未解除，重组进展不明；④成交地量，流动性濒临枯竭，卖出困难。</p>
            <p><strong>🎯 下周关键价位：</strong>压力位10-10.5元；支撑位9元、强支撑8.5元。</p>
            <p><strong>📋 操作计划：</strong>🚨<strong>最高优先级：立即清仓止损</strong>！退市风险敞口必须关闭，任何价格都要离场。浮亏约-27%，虽然亏损较大但退市风险可能导致更大损失甚至归零。下周周一开盘无条件挂单卖出，不计成本清仓。退市风险股绝不恋战，绝不抄底补仓。</p>
        </div>
    </div>
</div>
'''

portfolio_section = Section(title="💼 持仓股周末复盘", content=portfolio_html, icon="briefcase")
gen._components.append(portfolio_section)

# ============ 6. 下周操作策略 ============
trading_plan_html = '''
<div style="font-size: 14px; color: #e2e8f0; line-height: 1.9;">
    <h4 style="color: #60a5fa; margin: 16px 0 8px 0; font-size: 15px;">一、大盘判断</h4>
    <p style="margin: 6px 0;">本周科技股强势反弹，科创50涨超5%，存储/PCB/铜箔板块领涨。周末政策面暖风频吹（北京楼市新政+央行适度宽松+核电+电网），流动性环境友好，市场情绪从恐惧转向中性偏乐观。</p>
    <p style="margin: 6px 0;">下周大盘判断：<strong>震荡上行，结构性行情为主</strong>。上证指数有望挑战4100点，科创50继续领跑。核心支撑来自政策面持续发力+中报业绩验证+外资回流。但需注意美国CPI数据的外部扰动，以及中报业绩雷的尾部风险。</p>
    <p style="margin: 6px 0;">成交量：若能维持2.5万亿以上，反弹持续性较强；若缩量至2万亿以下，需警惕二次探底。</p>
    
    <h4 style="color: #60a5fa; margin: 16px 0 8px 0; font-size: 15px;">二、仓位建议</h4>
    <p style="margin: 6px 0;"><strong>整体仓位：5-6成</strong>（当前约4成，可适度加仓）。具体分配：</p>
    <ul style="margin: 6px 0; padding-left: 20px; color: #cbd5e1;">
        <li style="margin: 4px 0;"><strong>核心底仓（3成）：</strong>雅克科技（HBM前驱体+存储材料龙头）+ 铜冠铜箔底仓（PCB铜箔高景气）</li>
        <li style="margin: 4px 0;"><strong>机动仓位（2成）：</strong>PCB产业链（胜宏科技、沪电股份）+ 液冷散热（英维克减仓后保留底仓）+ 人形机器人（宇树上市催化）</li>
        <li style="margin: 4px 0;"><strong>现金（4成）：</strong>保持充足现金，等待回调加仓机会和中报后的优质标的布局</li>
    </ul>
    
    <h4 style="color: #60a5fa; margin: 16px 0 8px 0; font-size: 15px;">三、重点关注方向</h4>
    <p style="margin: 6px 0;"><strong>第一主线：PCB/铜箔产业链（最高优先级）</strong></p>
    <ul style="margin: 6px 0; padding-left: 20px; color: #cbd5e1;">
        <li style="margin: 4px 0;">核心逻辑：AI服务器PCB价值量3-5倍提升+高盛上调市场空间38%+铜箔供需缺口扩大+铜价上涨</li>
        <li style="margin: 4px 0;">关注标的：铜冠铜箔（持仓）、方邦股份、胜宏科技、沪电股份、深南电路</li>
        <li style="margin: 4px 0;">操作：铜冠铜箔冲高减仓锁定利润，回调后再接回；可小仓位加仓胜宏科技或沪电股份</li>
    </ul>
    
    <p style="margin: 6px 0;"><strong>第二主线：存储/HBM（中长期确定性最高）</strong></p>
    <ul style="margin: 6px 0; padding-left: 20px; color: #cbd5e1;">
        <li style="margin: 4px 0;">核心逻辑：SK海力士390亿扩产+存储紧缺延续至2027年+HBM供需缺口长期存在+AI驱动结构性需求</li>
        <li style="margin: 4px 0;">关注标的：雅克科技（持仓）、佰维存储、澜起科技、德明利、东芯股份</li>
        <li style="margin: 4px 0;">操作：雅克科技底仓持有，150-155元减仓锁利，回调至140附近可加仓</li>
    </ul>
    
    <p style="margin: 6px 0;"><strong>第三主线：人形机器人（事件驱动型）</strong></p>
    <ul style="margin: 6px 0; padding-left: 20px; color: #cbd5e1;">
        <li style="margin: 4px 0;">核心逻辑：宇树科技8/10申购+产业化加速+政策支持+融资爆发</li>
        <li style="margin: 4px 0;">关注标的：绿的谐波、双环传动、三花智控、拓普集团</li>
        <li style="margin: 4px 0;">操作：小仓位参与（≤1成），宇树上市前情绪冲高时减仓，警惕利好兑现回调</li>
    </ul>
    
    <h4 style="color: #60a5fa; margin: 16px 0 8px 0; font-size: 15px;">四、具体买卖计划</h4>
    <table style="width: 100%; border-collapse: collapse; margin: 10px 0; font-size: 13px;">
        <thead>
            <tr style="border-bottom: 2px solid #334155;">
                <th style="padding: 8px 6px; text-align: left; color: #94a3b8;">标的</th>
                <th style="padding: 8px 6px; text-align: center; color: #94a3b8;">当前价</th>
                <th style="padding: 8px 6px; text-align: center; color: #94a3b8;">买入/加仓</th>
                <th style="padding: 8px 6px; text-align: center; color: #94a3b8;">减仓/止盈</th>
                <th style="padding: 8px 6px; text-align: center; color: #94a3b8;">止损</th>
                <th style="padding: 8px 6px; text-align: center; color: #94a3b8;">目标仓位</th>
            </tr>
        </thead>
        <tbody>
            <tr style="border-bottom: 1px solid #1e293b;">
                <td style="padding: 8px 6px; color: #e2e8f0;">铜冠铜箔</td>
                <td style="padding: 8px 6px; text-align: center; color: #10b981;">115.81</td>
                <td style="padding: 8px 6px; text-align: center; color: #60a5fa;">100-105接回</td>
                <td style="padding: 8px 6px; text-align: center; color: #f59e0b;">120-125减至1/3</td>
                <td style="padding: 8px 6px; text-align: center; color: #ef4444;">跌破100止盈</td>
                <td style="padding: 8px 6px; text-align: center; color: #e2e8f0;">1.5成</td>
            </tr>
            <tr style="border-bottom: 1px solid #1e293b;">
                <td style="padding: 8px 6px; color: #e2e8f0;">雅克科技</td>
                <td style="padding: 8px 6px; text-align: center; color: #10b981;">148.78</td>
                <td style="padding: 8px 6px; text-align: center; color: #60a5fa;">140-142加仓</td>
                <td style="padding: 8px 6px; text-align: center; color: #f59e0b;">150-155减1/3</td>
                <td style="padding: 8px 6px; text-align: center; color: #ef4444;">跌破135止盈</td>
                <td style="padding: 8px 6px; text-align: center; color: #e2e8f0;">1.5-2成</td>
            </tr>
            <tr style="border-bottom: 1px solid #1e293b;">
                <td style="padding: 8px 6px; color: #e2e8f0;">英维克</td>
                <td style="padding: 8px 6px; text-align: center; color: #f59e0b;">55.90</td>
                <td style="padding: 8px 6px; text-align: center; color: #94a3b8;">不建议加仓</td>
                <td style="padding: 8px 6px; text-align: center; color: #f59e0b;">60-65减≥1/2</td>
                <td style="padding: 8px 6px; text-align: center; color: #ef4444;">跌破52清仓</td>
                <td style="padding: 8px 6px; text-align: center; color: #e2e8f0;">0.5成底仓</td>
            </tr>
            <tr style="border-bottom: 1px solid #1e293b;">
                <td style="padding: 8px 6px; color: #e2e8f0;">*ST建艺</td>
                <td style="padding: 8px 6px; text-align: center; color: #ef4444;">9.83</td>
                <td style="padding: 8px 6px; text-align: center; color: #94a3b8;">严禁买入</td>
                <td style="padding: 8px 6px; text-align: center; color: #ef4444;">周一立即全部清仓</td>
                <td style="padding: 8px 6px; text-align: center; color: #ef4444;">退市风险</td>
                <td style="padding: 8px 6px; text-align: center; color: #e2e8f0;">清零</td>
            </tr>
            <tr style="border-bottom: 1px solid #1e293b;">
                <td style="padding: 8px 6px; color: #e2e8f0;">胜宏科技/沪电</td>
                <td style="padding: 8px 6px; text-align: center; color: #60a5fa;">观察</td>
                <td style="padding: 8px 6px; text-align: center; color: #10b981;">回调5%介入</td>
                <td style="padding: 8px 6px; text-align: center; color: #f59e0b;">涨15-20%止盈</td>
                <td style="padding: 8px 6px; text-align: center; color: #ef4444;">跌破20日线止损</td>
                <td style="padding: 8px 6px; text-align: center; color: #e2e8f0;">新增0.5-1成</td>
            </tr>
        </tbody>
    </table>
    
    <h4 style="color: #60a5fa; margin: 16px 0 8px 0; font-size: 15px;">五、下周操作节奏</h4>
    <ul style="margin: 6px 0; padding-left: 20px; color: #cbd5e1;">
        <li style="margin: 4px 0;"><strong>周一（8/10）：</strong>重点关注宇树科技申购对机器人板块的带动，以及北京楼市新政对地产链的刺激。科技股若高开过多不追涨，等待回踩。*ST建艺开盘立即清仓。</li>
        <li style="margin: 4px 0;"><strong>周二（8/11）：</strong>美国CPI+中国社融双重数据，是下周最重要的时间窗口。数据利好则加仓，数据不及预期则继续减仓防御。铜冠铜箔若冲高120+减仓。</li>
        <li style="margin: 4px 0;"><strong>周三（8/12）：</strong>美国PPI数据，关注美股反应。风神股份解禁需警惕。宇树科技中签结果公布。</li>
        <li style="margin: 4px 0;"><strong>周四（8/13）：</strong>中报披露高峰，注意持仓股和关注标的的业绩情况。茅台/中芯国际业绩对消费和半导体板块有指引意义。</li>
        <li style="margin: 4px 0;"><strong>周五（8/14）：</strong>中国宏观经济数据（工业增加值/社零/固投），判断经济复苏力度。周末效应下仓位控制。</li>
    </ul>
</div>
'''

trading_section = Section(title="🎯 下周操作策略", content=trading_plan_html, icon="target")
gen._components.append(trading_section)

# ============ 7. 风险提示 ============
risk_html = '''
<div style="display: flex; flex-direction: column; gap: 12px;">
    <div style="background: rgba(239,68,68,0.05); border: 1px solid #dc2626; border-radius: 12px; padding: 14px 16px;">
        <div style="display: flex; align-items: center; margin-bottom: 8px;">
            <span style="background: linear-gradient(135deg, #ef4444, #dc2626); color: white; padding: 3px 10px; border-radius: 6px; font-size: 11px; font-weight: 600; margin-right: 10px;">高风险</span>
            <span style="font-size: 14px; font-weight: 600; color: #f1f5f9;">美国CPI超预期+美联储政策转向风险</span>
        </div>
        <div style="font-size: 13px; color: #94a3b8; line-height: 1.7;">
            <p style="margin: 4px 0;"><strong>触发条件：</strong>8月12日公布的美国7月CPI同比超过3.6%，反弹超预期。</p>
            <p style="margin: 4px 0;"><strong>影响范围：</strong>美债收益率反弹→压制全球科技成长股估值→北向资金流出→A股成长板块回调。高估值科技股首当其冲。</p>
            <p style="margin: 4px 0;"><strong>应对措施：</strong>提前减仓高位科技股锁定利润（铜冠铜箔、雅克科技冲高减仓），增加现金仓位至5成以上，等待数据明朗后再决策。若CPI符合预期或低于预期，则是加仓良机。</p>
        </div>
    </div>
    
    <div style="background: rgba(245,158,11,0.05); border: 1px solid #d97706; border-radius: 12px; padding: 14px 16px;">
        <div style="display: flex; align-items: center; margin-bottom: 8px;">
            <span style="background: linear-gradient(135deg, #f59e0b, #d97706); color: white; padding: 3px 10px; border-radius: 6px; font-size: 11px; font-weight: 600; margin-right: 10px;">中风险</span>
            <span style="font-size: 14px; font-weight: 600; color: #f1f5f9;">科技板块获利回吐+高位震荡风险</span>
        </div>
        <div style="font-size: 13px; color: #94a3b8; line-height: 1.7;">
            <p style="margin: 4px 0;"><strong>触发条件：</strong>存储/PCB/铜箔等科技板块短期涨幅较大，铜冠铜箔周五单日涨17%，板块内获利盘丰厚，龙头股放量滞涨或量价背离。</p>
            <p style="margin: 4px 0;"><strong>影响范围：</strong>AI算力、存储芯片、人形机器人、PCB/铜箔等高位科技板块。宇树科技上市后人形机器人板块可能出现"利好兑现"回调。</p>
            <p style="margin: 4px 0;"><strong>应对措施：</strong>冲高减仓锁定利润，不追高，等待回调5-10%后再介入。保持仓位灵活，核心底仓持有不动，机动仓位高抛低吸。</p>
        </div>
    </div>
    
    <div style="background: rgba(245,158,11,0.05); border: 1px solid #d97706; border-radius: 12px; padding: 14px 16px;">
        <div style="display: flex; align-items: center; margin-bottom: 8px;">
            <span style="background: linear-gradient(135deg, #f59e0b, #d97706); color: white; padding: 3px 10px; border-radius: 6px; font-size: 11px; font-weight: 600; margin-right: 10px;">中风险</span>
            <span style="font-size: 14px; font-weight: 600; color: #f1f5f9;">中报业绩雷集中释放风险</span>
        </div>
        <div style="font-size: 13px; color: #94a3b8; line-height: 1.7;">
            <p style="margin: 4px 0;"><strong>触发条件：</strong>8月中旬为中报披露高峰期，持仓股或关注标的业绩大幅低于预期，或出现亏损/商誉减值等负面消息。</p>
            <p style="margin: 4px 0;"><strong>影响范围：</strong>业绩预亏股、高估值概念股、有财务违规前科个股。已有交大昂立等公司被ST，警示效应明显。</p>
            <p style="margin: 4px 0;"><strong>应对措施：</strong>提前排查持仓股业绩预告和历史财务情况，规避业绩不确定的中小盘标的，优先选择业绩确定性高的行业龙头。对有瑕疵的个股提前减仓。</p>
        </div>
    </div>
    
    <div style="background: rgba(107,114,128,0.05); border: 1px solid #4b5563; border-radius: 12px; padding: 14px 16px;">
        <div style="display: flex; align-items: center; margin-bottom: 8px;">
            <span style="background: linear-gradient(135deg, #6b7280, #4b5563); color: white; padding: 3px 10px; border-radius: 6px; font-size: 11px; font-weight: 600; margin-right: 10px;">低风险</span>
            <span style="font-size: 14px; font-weight: 600; color: #f1f5f9;">地缘政治冲突升级风险</span>
        </div>
        <div style="font-size: 13px; color: #94a3b8; line-height: 1.7;">
            <p style="margin: 4px 0;"><strong>触发条件：</strong>中东局势突然升级、美伊冲突加剧、重大贸易摩擦事件等。</p>
            <p style="margin: 4px 0;"><strong>影响范围：</strong>国际油价暴涨→推升通胀预期→美联储降息推迟→全球风险偏好下降。航空板块承压，油气/黄金避险属性凸显。</p>
            <p style="margin: 4px 0;"><strong>应对措施：</strong>保持少量黄金/油气配置作为对冲（≤5%仓位），控制整体仓位在6成以内，预留现金应对突发风险。</p>
        </div>
    </div>
</div>
'''

risk_section = Section(title="⚠️ 风险提示与应对", content=risk_html, icon="alert-triangle")
gen._components.append(risk_section)

# ============ 生成并发布 ============
print('开始生成并发布...')
result = gen.publish(
    title='周末速递 2026.08.09',
    excerpt='北京楼市重磅新政+宇树科技申购+存储超级周期延续+下周完整操作策略指南',
    auto_deploy=True,
    docs_root='docs'
)
print(f'发布结果: {result}')

# 验证字数
html = gen.generate()
import re
chinese_chars = re.findall(r'[\u4e00-\u9fff]', html)
print(f'中文字符数（含模板）: {len(chinese_chars)}')

print('完成！')
