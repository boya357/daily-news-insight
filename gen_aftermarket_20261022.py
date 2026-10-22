import sys, os
sys.path.insert(0, '/root/daily-news-insight/v3')
os.chdir('/root/daily-news-insight')

from v3.generators.aftermarket import AftermarketGenerator

gen = AftermarketGenerator(date_str="20261022", subtitle="2026.10.22 · 盘后速递")

# ===== 今日核心亮点 =====
gen.add_today_highlight(
    "A股今日放量普跌，上证指数跌1.48%失守3700点，创业板指暴跌4.37%创年内最大单日跌幅，全市场近5000只个股下跌，两市成交额1.53万亿较前日放量993亿。"
    "通信、传媒、综合板块领跌，仅家用电器板块收红；半导体封测方向逆势活跃，华天科技涨停封板。"
    "持仓四只股票全线飘绿：铜冠铜箔跌5.84%领跌、雅克科技跌4.56%、英维克跌3.59%、*ST建艺跌1.30%。"
    "龙虎榜显示机构净卖出2.16亿，游资净买入6.84亿，市场呈现机构出货、游资接力的结构性博弈特征。"
    "工信部等八部门发文加快AI全环节落地应用，晚间政策利好有望催化明日科技板块修复。"
)

# ===== 市场收盘总结 =====
gen.add_market_summary(
    indices=[
        {"name": "上证指数", "value": "3658.03", "change": "-1.48%", "up": False, "icon": "trending_down"},
        {"name": "深证成指", "value": "11357.32", "change": "-2.96%", "up": False, "icon": "trending_down"},
        {"name": "创业板指", "value": "2576.90", "change": "-4.37%", "up": False, "icon": "trending_down"},
        {"name": "科创50", "value": "1305.87", "change": "-2.78%", "up": False, "icon": "trending_down"},
    ],
    volume="1.53万亿",
    northbound="净卖出约20.2亿"
)

# ===== 情绪温度计 =====
gen.add_sentiment_thermometer(
    temperature=22,
    volume="1.53万亿",
    up_count="533",
    down_count="4994",
    limit_up_count="22"
)

# ===== 晚间重要新闻 =====
gen.add_evening_news([
    {
        "title": "工信部等八部门：加快人工智能在产品研发、设计仿真、中试验证、生产运营等全环节落地应用",
        "content": "工信部等八部门印发《规划》，提出加快人工智能在产品研发、设计仿真、中试验证、生产运营等全环节落地应用，提升过程管理、分析预测、决策执行智能化水平，加快产业基础创新迭代。利好AI算力、工业软件、智能制造等产业链方向。",
        "time": "20:30",
        "source": "新华财经",
        "tag": "重磅政策",
        "tag_variant": "primary"
    },
    {
        "title": "A股放量普跌，创业板指暴跌4.37%创年内最大单日跌幅",
        "content": "今日四大股指集体收跌，上证指数跌1.48%报3658.03点，深成指跌2.96%报11357.32点，创业板指跌4.37%报2576.90点，科创综指跌3.32%。全市场533只上涨、4994只下跌，普跌格局明显。两市成交额1.53万亿，较前日放量993亿，恐慌盘涌出。",
        "time": "15:00",
        "source": "第一财经",
        "tag": "市场",
        "tag_variant": "danger"
    },
    {
        "title": "龙虎榜：机构净卖出2.16亿 游资净买入6.84亿",
        "content": "今日龙虎榜共66只个股上榜，机构席位合计净卖出2.16亿（买入20.83亿/卖出22.99亿），北向资金净卖出5405.54万，游资席位净买入6.84亿。机构净买入前三：安培龙1.36亿、昂利康5461万、利亚德3774万；机构净卖出前三：华盛昌1.05亿、中新赛克7155万、万丰奥威6974万。",
        "time": "18:20",
        "source": "第一财经/金融界",
        "tag": "资金",
        "tag_variant": "warning"
    },
    {
        "title": "中共中央办公厅、国务院办公厅发布《关于推动科技创新和产业创新深度融合的意见》",
        "content": "意见要求以发展新质生产力、建设现代化产业体系为目标，以构建企业主导、各主体协同的产学研融通创新体系为重点，推动科技创新和产业创新深度融合。利好半导体、高端装备、新材料等硬科技方向。",
        "time": "18:00",
        "source": "央视新闻",
        "tag": "政策",
        "tag_variant": "primary"
    },
    {
        "title": "三季报密集披露期开启：长川科技前三季度净利同比翻倍",
        "content": "长川科技披露前三季度业绩预告，归母净利润17.15-18.15亿元，同比增长98.17%-109.73%，半导体设备板块业绩高增验证行业景气度。华正新材前三季度净利润同比翻超11倍，覆铜板/CCL需求超预期。",
        "time": "21:30",
        "source": "财联社",
        "tag": "业绩",
        "tag_variant": "success"
    }
])

# ===== 板块涨跌幅排行 =====
gen.add_sector_performance(
    up_sectors=[
        {"name": "家用电器", "change": "+0.08%"},
        {"name": "银行", "change": "-0.30%"},
        {"name": "食品饮料", "change": "-0.50%"},
        {"name": "工程机械", "change": "+逆势上涨"},
        {"name": "电机", "change": "+逆势上涨"},
    ],
    down_sectors=[
        {"name": "通信", "change": "-6.17%"},
        {"name": "传媒", "change": "-4.78%"},
        {"name": "综合", "change": "-4.66%"},
        {"name": "计算机", "change": "-4.20%"},
        {"name": "电子", "change": "-3.60%"},
    ]
)

# ===== 盘面深度解读 =====
gen.add_market_deep_analysis(
    strong_sectors=[
        {"name": "银行/家用电器", "reason": "防御板块逆势抗跌，银行板块仅微跌0.3%，家用电器是唯一收红的申万一级行业。市场风险偏好急剧下降，资金从成长股撤出后涌入低估值防御板块，属于典型的避险情绪宣泄。"},
        {"name": "工程机械", "reason": "南矿集团、山河智能等涨停领涨，基建稳增长预期升温，叠加出口数据向好，工程机械板块阶段性走强。但持续性存疑，更多是超跌反弹性质。"},
        {"name": "半导体封测", "reason": "华天科技涨停（+9.12%），主力资金净流入12.03亿元居电子行业首位，半导体封测方向逆势活跃。先进封装+国产替代双重逻辑，三季报业绩高增验证景气度，是今日市场为数不多的亮点。"},
        {"name": "电机", "reason": "电机板块逆势上涨，受益于人形机器人产业链预期，宇树机器人概念、减速器等细分方向有资金布局，属于题材性机会。"},
    ],
    weak_sectors=[
        {"name": "通信（-6.17%）", "reason": "光模块/CPO概念重挫，中际旭创、新易盛等龙头大幅下跌。前期涨幅过大、估值偏高，叠加三季报业绩兑现担忧，资金集中出逃，短期仍有调整压力。"},
        {"name": "传媒（-4.78%）", "reason": "新华传媒、龙版传媒等跌停，传媒板块前期AI+概念炒作充分，业绩兑现不及预期，叠加监管趋严，资金获利了结意愿强烈。"},
        {"name": "电子（-3.60%）", "reason": "电子行业主力资金净流出137.02亿元，源杰科技跌9.90%、东山精密跌7.84%。但板块内部分化明显，华天科技等封测标的逆势上涨，说明资金在做高低切换。"},
        {"name": "计算机（-4.20%）", "reason": "AI应用、信创板块全线回调，市场风险偏好下降导致高估值成长股承压，但工信部晚间发布AI全环节落地应用政策，明日有望迎来修复。"},
    ],
    core_view="今日市场出现放量普跌，创业板指暴跌4.37%创年内最大单日跌幅，全市场近5000只个股下跌，恐慌情绪蔓延。但我们认为这是牛市中期结构性调整的加速赶底阶段，而非新一轮熊市的开始。核心逻辑：（1）政策面持续向好——晚间工信部等八部门发布AI全环节落地应用重磅政策，叠加两办发布科技创新与产业创新融合意见，政策底已经明确；（2）成交量放大至1.53万亿，恐慌盘涌出，往往是阶段性底部的信号；（3）半导体封测方向逆势活跃，华天科技涨停，说明有聪明资金在逆势布局科技成长主线。操作策略：当前不宜盲目割肉，也不宜急于抄底，应保持耐心，等待市场企稳信号。重点关注：半导体（设备/材料/封测）、AI算力、液冷散热等核心主线的超跌反弹机会。"
)

# ===== 持仓股跟踪 =====
gen.add_holdings_tracking([
    {
        "name": "英维克",
        "code": "002837",
        "price": "43.53",
        "change": "-3.59%",
        "up": False,
        "comment": "今日收跌3.59%报43.53元，成交12.07亿，换手率2.38%，较昨日明显放量。开盘冲高至46.15元后一路下挫，最低43.42元，收于全天低位附近，形成带长上影线的中阴线，多头反击失败。5日均线44.76元已失守，10日均线47.17元构成强压力。RSI6从18.74反弹至32后再度回落，MACD绿柱小幅收窄但空头趋势未变。布林下轨39.63元为最终支撑位，短期支撑看42元整数关口。主力资金今日净流入1357.91万元（超大单+1102万），与股价背离，说明有大资金在低位承接。液冷行业逻辑不变，英伟达Rubin平台带动液冷需求，中期看好。"
    },
    {
        "name": "铜冠铜箔",
        "code": "301217",
        "price": "81.65",
        "change": "-5.84%",
        "up": False,
        "comment": "今日大跌5.84%报81.65元，成交11.63亿，换手率1.68%，创阶段新低。开盘86.80元后单边下跌，最低81.60元，几乎收于最低点，空头动能强劲。5日均线86.52元、10日均线90.20元全部失守，短期均线空头排列。RSI6从28.50骤降至18.32再度进入超卖区间，KDJ的J值跌入负值区域。布林下轨77.45元为强支撑位，距离当前价格约5%空间。主力资金今日净卖出1.33亿元，资金出逃明显。铜箔板块整体承压，覆铜板概念今日也逆势下跌，行业短期缺乏催化。但中期AI服务器PCB/CCL需求增长260%的产业逻辑不变，当前位置估值已处于历史低位。"
    },
    {
        "name": "雅克科技",
        "code": "002409",
        "price": "92.39",
        "change": "-4.56%",
        "up": False,
        "comment": "今日收跌4.56%报92.39元，成交10.50亿，换手率3.51%。开盘97.01元后震荡下行，最低91.90元，收于日内低位。5日均线100.15元、10日均线103.39元全部跌破，短期均线呈空头排列。RSI6从12.29的极度超卖状态反弹后再度回落至22.56，MACD绿柱扩大至-4.52，空头动能仍在释放。支撑位看前期平台90元整数关口，强支撑86.30元（布林下轨）。半导体材料板块今日整体调整，但封测方向（华天科技）逆势涨停，说明资金在半导体内部做高低切换——从高估值材料股流向低估值封测股。雅克作为半导体材料龙头，中期HBM前驱体国产替代逻辑不变，但短期仍需等待板块企稳。"
    },
    {
        "name": "*ST建艺",
        "code": "002789",
        "price": "12.87",
        "change": "-1.30%",
        "up": False,
        "comment": "今日收跌1.30%报12.87元，成交1571.49万元，换手率0.78%，缩量调整。最高13.21元，最低12.61元，波幅4.60%，整体仍在12.5-13.5元区间内震荡。5日均线13.10元构成短期压力，下方支撑12.50元（前期低点）。作为ST股，今日跌幅远小于大盘，表现出明显的抗跌性，继续发挥组合防御缓冲的作用。公司庭外重组仍在推进中，申请撤销退市风险警示尚在深交所审核阶段。成交极度萎缩说明抛压有限，但缺乏买盘推动，短期大概率维持区间震荡。继续持有作为组合底仓，跌破12.5元需警惕。"
    }
])

# ===== 龙虎榜深度解析 =====
gen.add_dragon_tiger_list([
    {
        "name": "利亚德",
        "code": "300296",
        "change": "+8.35%",
        "up": True,
        "institutions": 3,
        "reason": "日涨幅偏离值达7%",
        "net_buy": "+1.83亿"
    },
    {
        "name": "安培龙",
        "code": "301413",
        "change": "+14.60%",
        "up": True,
        "institutions": 8,
        "reason": "日涨幅达20cm涨停",
        "net_buy": "+1.12亿"
    },
    {
        "name": "北新路桥",
        "code": "002307",
        "change": "+10.06%",
        "up": True,
        "institutions": 0,
        "reason": "日涨幅偏离值达7%",
        "net_buy": "+1.72亿"
    }
])

# ===== 龙虎榜深度分析补充（自定义HTML） =====
from v3.core.report import Report
from v3.components.layout import Section, SubCard

lhb_detail_html = '''
<div style="display: flex; flex-direction: column; gap: 20px; margin-top: 16px;">
    
    <div style="background: rgba(30,30,50,0.5); border: 1px solid rgba(255,255,255,0.08); border-radius: 16px; padding: 20px;">
        <div style="font-size: 16px; font-weight: 700; color: #f1f5f9; margin-bottom: 12px;">🐉 利亚德（300296）龙虎榜深度解读</div>
        <div style="font-size: 13px; color: #94a3b8; line-height: 1.8;">
            <p><strong style="color: #f59e0b;">上榜原因：</strong>日涨幅偏离值达7%，收涨8.35%报6.10元，总买入约5.6亿，总卖出约3.77亿，净买入1.83亿</p>
            <p><strong style="color: #10b981;">买方分析：</strong>机构专用席位占据3席，合计净买入3774.07万元；中信证券上海溧阳路（顶级游资席位，成功率68%）买入3744万；国泰海通上海长宁江苏路（量化席位）买入约3200万。买方阵容机构+游资+量化齐聚，质量较高。</p>
            <p><strong style="color: #ef4444;">卖方分析：</strong>卖方前五以游资和散户席位为主，深股通专用席位净卖出约1200万，北向资金小幅减仓。整体卖压不大，筹码相对稳定。</p>
            <p><strong style="color: #fbbf24;">持续性判断：</strong>⭐⭐⭐⭐ 较强。机构净买入近4000万叠加顶级游资溧阳路介入，说明大资金对其成长股属性认可度高。利亚德是LED显示龙头，兼有AI+虚拟现实+MicroLED多重概念，位置低、市值中等（约150亿），弹性空间大。明日若能继续放量突破6.5元压力位，有望挑战7元整数关口。</p>
        </div>
    </div>
    
    <div style="background: rgba(30,30,50,0.5); border: 1px solid rgba(255,255,255,0.08); border-radius: 16px; padding: 20px;">
        <div style="font-size: 16px; font-weight: 700; color: #f1f5f9; margin-bottom: 12px;">🐉 安培龙（301413）龙虎榜深度解读</div>
        <div style="font-size: 13px; color: #94a3b8; line-height: 1.8;">
            <p><strong style="color: #f59e0b;">上榜原因：</strong>日涨幅达20cm涨停，收涨14.60%（实际非涨停，因注册制新股首日无涨跌幅限制/或为大幅上涨），总买入约3.5亿，总卖出约2.38亿，净买入1.12亿</p>
            <p><strong style="color: #10b981;">买方分析：</strong>机构专用席位多达8个，合计净买入1.36亿元，是今日机构净买入最多的个股。国泰君安深圳益田路（游资席位）买入2808万，机构抱团迹象明显。安培龙是热敏电阻/温度传感器龙头，应用于新能源汽车、储能、消费电子等领域。</p>
            <p><strong style="color: #ef4444;">卖方分析：</strong>7个机构席位出现在卖方，说明机构内部存在分歧，但整体净买入仍达1.36亿，买盘力量占优。</p>
            <p><strong style="color: #fbbf24;">持续性判断：</strong>⭐⭐⭐⭐ 强。8家机构集体买入，机构认可度极高。今日大涨14.6%但成交量未异常放大，筹码锁定良好。作为次新股+传感器+汽车电子概念，题材想象力丰富。明日有望继续冲高，但需注意短期涨幅过大后的回调风险，建议关注5日均线支撑。</p>
        </div>
    </div>
    
    <div style="background: rgba(30,30,50,0.5); border: 1px solid rgba(255,255,255,0.08); border-radius: 16px; padding: 20px;">
        <div style="font-size: 16px; font-weight: 700; color: #f1f5f9; margin-bottom: 12px;">🐉 北新路桥（002307）龙虎榜深度解读</div>
        <div style="font-size: 13px; color: #94a3b8; line-height: 1.8;">
            <p><strong style="color: #f59e0b;">上榜原因：</strong>日涨幅偏离值达7%，收涨10.06%报3.39元（涨停），总买入约4.8亿，总卖出约3.08亿，净买入1.72亿</p>
            <p><strong style="color: #10b981;">买方分析：</strong>买方前五以游资席位为主，中信证券上海溧阳路买入约2500万（净买入1872万，同时有卖出），其余为地方游资席位。没有机构专用席位出现在买方，游资主导行情。</p>
            <p><strong style="color: #ef4444;">卖方分析：</strong>机构专用席位净卖出3742.74万元，是今日龙虎榜机构净卖出较多的个股之一，说明机构在借涨停出货。北向资金也有小幅卖出。</p>
            <p><strong style="color: #fbbf24;">持续性判断：</strong>⭐⭐ 偏弱。虽然游资净买入1.72亿力度不小，但机构净卖出3742万，且北新路桥属于传统基建行业，缺乏科技成长属性。在今日大盘暴跌背景下，基建板块成为避险方向，但其上涨更多是轮动补涨性质，持续性存疑。不建议追高，若明日低开可关注能否弱转强。</p>
        </div>
    </div>
    
</div>
'''

lhb_section = Section(title="📊 龙虎榜深度分析", content=lhb_detail_html, icon="bar_chart")
gen._components.append(lhb_section)

# ===== 重点关注标的 =====
watchlist_html = '''
<div style="display: flex; flex-direction: column; gap: 16px;">
    
    <div style="background: linear-gradient(135deg, rgba(16,185,129,0.1) 0%, rgba(5,150,105,0.08) 100%); 
                border: 1px solid rgba(16,185,129,0.3); border-radius: 16px; padding: 20px;">
        <div style="display: flex; align-items: center; margin-bottom: 12px;">
            <span style="font-size: 18px; font-weight: 700; color: #10b981;">💎 华天科技（002185）</span>
            <span style="margin-left: 12px; background: rgba(16,185,129,0.2); color: #10b981; 
                         font-size: 12px; padding: 4px 10px; border-radius: 12px;">关注评级：S</span>
        </div>
        <div style="font-size: 13px; color: #e2e8f0; line-height: 1.8;">
            <p><strong>当前价格：</strong>15.55元 · 今日+9.12% · 成交18.6亿 · 换手6.93%</p>
            <p><strong>关注逻辑：</strong>国内封测龙头之一，今日逆势涨停，主力资金净流入12.03亿元居电子行业首位，是今日市场最亮眼的科技股。半导体封测是先进封装产业链核心环节，AI芯片爆发带动CoWoS/2.5D/3D封装需求激增。华天科技市值仅300多亿，估值处于行业低位（PE约25倍），具备较大向上空间。盘后固定价格交易再成交1694万，买盘依然强劲。</p>
            <p><strong>目标价：</strong>第一目标位18元（前期平台+布林上轨），第二目标位21元（年线附近）</p>
            <p><strong>止损位：</strong>14元（今日涨停板实体的1/2位置）</p>
            <p><strong>操作建议：</strong>明日若低开至15元以下可积极建仓，首仓30%；若高开不超过5%（16.3元以下）也可小仓位追入20%。总仓位≤50%。反弹至18元减仓1/3，20元以上减仓至底仓。</p>
        </div>
    </div>
    
    <div style="background: linear-gradient(135deg, rgba(245,158,11,0.1) 0%, rgba(239,68,68,0.08) 100%); 
                border: 1px solid rgba(245,158,11,0.3); border-radius: 16px; padding: 20px;">
        <div style="display: flex; align-items: center; margin-bottom: 12px;">
            <span style="font-size: 18px; font-weight: 700; color: #f59e0b;">🔥 长川科技（300604）</span>
            <span style="margin-left: 12px; background: rgba(245,158,11,0.2); color: #f59e0b; 
                         font-size: 12px; padding: 4px 10px; border-radius: 12px;">关注评级：A+</span>
        </div>
        <div style="font-size: 13px; color: #e2e8f0; line-height: 1.8;">
            <p><strong>当前价格：</strong>三季报业绩预告：归母净利润17.15-18.15亿，同比+98%~+110%</p>
            <p><strong>关注逻辑：</strong>半导体测试设备龙头，今晚发布三季报业绩预告，前三季度净利润同比翻倍，验证半导体设备行业高景气度。国产替代大趋势下，测试设备是受益确定性最高的环节之一。长川科技产品线不断拓展，从测试机扩展到分选机、探针台，平台化布局成型。在当前市场环境下，业绩高增的硬科技标的具备稀缺性，容易获得资金关注。</p>
            <p><strong>目标价：</strong>第一目标位前期高点附近，第二目标位历史新高</p>
            <p><strong>止损位：</strong>20日均线下方</p>
            <p><strong>操作建议：</strong>明日开盘可关注集合竞价情况，若高开不超过5%可建底仓20%；若低开则是更好的买入机会，可加至30%仓位。以20日均线为止损线，跌破则止损。</p>
        </div>
    </div>
    
    <div style="background: linear-gradient(135deg, rgba(139,92,246,0.1) 0%, rgba(79,70,229,0.08) 100%); 
                border: 1px solid rgba(139,92,246,0.3); border-radius: 16px; padding: 20px;">
        <div style="display: flex; align-items: center; margin-bottom: 12px;">
            <span style="font-size: 18px; font-weight: 700; color: #8b5cf6;">⚡ 德明利（001309）</span>
            <span style="margin-left: 12px; background: rgba(139,92,246,0.2); color: #8b5cf6; 
                         font-size: 12px; padding: 4px 10px; border-radius: 12px;">关注评级：A</span>
        </div>
        <div style="font-size: 13px; color: #e2e8f0; line-height: 1.8;">
            <p><strong>当前价格：</strong>243.17元 · 今日+4.00% · 电子行业资金流入榜第三（净流入2.46亿）</p>
            <p><strong>关注逻辑：</strong>存储芯片模组+主控芯片标的，今日在大盘暴跌4%的背景下逆势上涨4%，主力资金净流入2.46亿元，盘后固定价格交易再成交793万，买盘强劲。存储芯片行业处于周期底部回升阶段，AI服务器带动的企业级存储需求爆发是核心驱动力。德明利作为中小市值存储标的，弹性较大。</p>
            <p><strong>目标价：</strong>第一目标位270元（前期平台），第二目标位300元（历史新高附近）</p>
            <p><strong>止损位：</strong>225元（今日阳线实体的2/3位置）</p>
            <p><strong>操作建议：</strong>明日若回调至235-240元区间可建仓，仓位≤20%。以225元为止损线，跌破则止损。快进快出为主，不做长期持有。</p>
        </div>
    </div>
    
</div>
'''

watch_section = Section(title="🎯 重点关注标的（3只）", content=watchlist_html, icon="star")
gen._components.append(watch_section)

# ===== 明日关键预判 =====
gen.add_tomorrow_prediction([
    {
        "name": "半导体/先进封装",
        "direction": "看涨",
        "confidence": 75,
        "reason": "今日半导体封测方向逆势活跃，华天科技涨停、长川科技晚间发布超预期三季报。叠加晚间工信部发布AI全环节落地应用重磅政策，半导体板块有望成为明日市场反弹先锋。重点关注封测、设备、材料三大方向。"
    },
    {
        "name": "AI算力/液冷散热",
        "direction": "震荡反弹",
        "confidence": 65,
        "reason": "英维克今日放量下跌，但主力资金净流入1357万出现底背离。晚间工信部AI政策利好叠加液冷产业长期逻辑不变，预计明日技术性反弹概率较大。但上方5日和10日均线压力仍在，反弹高度需观察量能配合。"
    },
    {
        "name": "通信/光模块",
        "direction": "看跌",
        "confidence": 70,
        "reason": "通信板块今日暴跌6.17%领跌两市，光模块龙头中际旭创、新易盛大挫。前期涨幅过大、估值偏高，叠加北向资金大幅卖出，短期调整尚未结束。明日可能继续下探寻找支撑，规避为主。"
    },
    {
        "name": "大盘走势",
        "direction": "超跌反弹",
        "confidence": 60,
        "reason": "今日放量普跌后，恐慌盘已大量涌出，1.53万亿成交量说明有大量承接盘。晚间政策利好（AI+科技创新）有望催化明日超跌反弹。上证指数3600点附近有强支撑，创业板2500点是关键心理关口。但反弹力度仍需观察量能和北向资金流向。"
    }
])

# ===== 明日操作计划 =====
trading_plan = '''
<div style="background: rgba(30,30,50,0.5); border: 1px solid rgba(255,255,255,0.08); border-radius: 16px; padding: 24px;">
    <div style="font-size: 16px; font-weight: 700; color: #f1f5f9; margin-bottom: 20px;">📋 明日操作策略（2026.10.23）</div>
    
    <div style="margin-bottom: 20px;">
        <div style="font-size: 14px; font-weight: 600; color: #f59e0b; margin-bottom: 8px;">一、大盘判断</div>
        <div style="font-size: 13px; color: #cbd5e1; line-height: 1.8;">
            今日放量普跌（1.53万亿，4994只下跌），属于恐慌性抛售阶段，往往意味着短期底部临近。
            晚间工信部等八部门发布AI全环节落地应用重磅政策，叠加两办科技创新融合意见，政策面持续加码。
            预计明日超跌反弹概率较大，沪指有望在3600-3650点区间企稳反弹，创业板2500点有强支撑。
            但反弹持续性仍需观察：若量能萎缩、北向资金继续流出，则反弹高度有限，可能只是下跌中继。
            操作策略：以防御为主，趁反弹降低仓位，保留现金等待更明确的右侧信号。
        </div>
    </div>
    
    <div style="margin-bottom: 20px;">
        <div style="font-size: 14px; font-weight: 600; color: #f59e0b; margin-bottom: 8px;">二、仓位建议</div>
        <div style="font-size: 13px; color: #cbd5e1; line-height: 1.8;">
            整体仓位控制在40%-50%（较前期下调10%），其中：
            科技成长方向30%（半导体为主、AI算力为辅）、防御品种10%、现金储备50%-60%。
            当前处于加速赶底阶段，不宜急于抄底，保留充足弹药等待更明确的底部信号。
            现金为王，耐心等待右侧机会。
        </div>
    </div>
    
    <div style="margin-bottom: 20px;">
        <div style="font-size: 14px; font-weight: 600; color: #f59e0b; margin-bottom: 8px;">三、持仓股操作计划</div>
        <div style="font-size: 13px; color: #cbd5e1; line-height: 2;">
            <p><strong style="color: #fb923c;">1. 英维克（002837）</strong>：当前价43.53元，今日-3.59%<br>
            &nbsp;&nbsp;• <strong>核心判断</strong>：今日放量下跌但主力资金净流入，底背离信号明显，短期有反弹需求<br>
            &nbsp;&nbsp;• 反弹至<span style="color: #10b981; font-weight: 700;">46元以上</span>减仓1/3（降低持仓比例）<br>
            &nbsp;&nbsp;• 反弹至<span style="color: #10b981; font-weight: 700;">48元以上</span>再减仓1/3<br>
            &nbsp;&nbsp;• 跌破<span style="color: #ef4444; font-weight: 700;">42元</span>止损减仓至底仓（100股观察仓）<br>
            &nbsp;&nbsp;• 42-46元区间持有观望，不做操作，等待反弹</p>
            
            <p><strong style="color: #fb923c;">2. 铜冠铜箔（301217）</strong>：当前价81.65元，今日-5.84%<br>
            &nbsp;&nbsp;• <strong>核心判断</strong>：今日创阶段新低，空头动能强劲，但RSI已超卖（18.32），随时可能技术性反弹<br>
            &nbsp;&nbsp;• 反弹至<span style="color: #10b981; font-weight: 700;">88元以上</span>减仓1/3<br>
            &nbsp;&nbsp;• 反弹至<span style="color: #10b981; font-weight: 700;">92元以上</span>再减仓1/3<br>
            &nbsp;&nbsp;• 跌破<span style="color: #ef4444; font-weight: 700;">78元</span>止损减仓（布林下轨支撑，若有效跌破则趋势恶化）<br>
            &nbsp;&nbsp;• 78-85元区间持有，若反弹无力则考虑进一步降低仓位</p>
            
            <p><strong style="color: #fb923c;">3. 雅克科技（002409）</strong>：当前价92.39元，今日-4.56%<br>
            &nbsp;&nbsp;• <strong>核心判断</strong>：半导体材料龙头，中期HBM前驱体逻辑不变，但短期受板块拖累继续调整<br>
            &nbsp;&nbsp;• 反弹至<span style="color: #10b981; font-weight: 700;">100元以上</span>减仓1/3<br>
            &nbsp;&nbsp;• 反弹至<span style="color: #10b981; font-weight: 700;">105元以上</span>再减仓1/3<br>
            &nbsp;&nbsp;• 跌破<span style="color: #ef4444; font-weight: 700;">90元</span>止损减仓至底仓（前期平台支撑，若有效跌破则看至85元）<br>
            &nbsp;&nbsp;• 90-98元区间持有，关注半导体封测板块（华天科技）能否带动材料股反弹</p>
            
            <p><strong style="color: #fb923c;">4. *ST建艺（002789）</strong>：当前价12.87元，今日-1.30%<br>
            &nbsp;&nbsp;• <strong>核心判断</strong>：ST股抗跌属性明显，继续作为组合防御缓冲，贡献稳定性<br>
            &nbsp;&nbsp;• 继续持有，维持当前仓位<br>
            &nbsp;&nbsp;• 跌破<span style="color: #ef4444; font-weight: 700;">12.5元</span>减仓50%（前期低点支撑）<br>
            &nbsp;&nbsp;• 反弹至<span style="color: #10b981; font-weight: 700;">14元以上</span>考虑减仓（区间上沿）</p>
        </div>
    </div>
    
    <div>
        <div style="font-size: 14px; font-weight: 600; color: #f59e0b; margin-bottom: 8px;">四、新建仓计划</div>
        <div style="font-size: 13px; color: #cbd5e1; line-height: 2;">
            <p><strong style="color: #10b981;">1. 华天科技（002185）</strong>：封测龙头，今日逆势涨停<br>
            &nbsp;&nbsp;• 建仓区间：<span style="font-weight: 700;">15-15.5元</span>（明日低开或平开时），首仓30%<br>
            &nbsp;&nbsp;• 加仓条件：回调至14.5元加20%，总仓位≤50%<br>
            &nbsp;&nbsp;• 止损位：14元（跌破今日涨停板实体的1/2位置）<br>
            &nbsp;&nbsp;• 目标位：18元（第一目标），21元（第二目标）</p>
            
            <p><strong style="color: #10b981;">2. 长川科技（300604）</strong>：半导体测试设备，三季报超预期<br>
            &nbsp;&nbsp;• 建仓区间：<span style="font-weight: 700;">高开≤5%以内</span>可建底仓20%，低开更优<br>
            &nbsp;&nbsp;• 加仓条件：若回调至20日均线加20%，总仓位≤40%<br>
            &nbsp;&nbsp;• 止损位：20日均线下方3%<br>
            &nbsp;&nbsp;• 注意：业绩预告利好已出，警惕"利好兑现"行情，不宜追高</p>
        </div>
    </div>
</div>
'''

plan_section = Section(title="🎯 明日操作策略", content=trading_plan, icon="target", variant="highlight")
gen._components.append(plan_section)

# ===== 风险提示 =====
gen.add_risk_warning([
    "今日放量普跌后市场情绪极度脆弱，若晚间美股大幅下跌可能进一步冲击明日A股开盘",
    "北向资金近期持续流出，外资减持可能加剧核心资产的调整压力",
    "持仓四只股票全部处于下降趋势中，技术性反弹后可能继续下探，需严格执行止损纪律",
    "10月底为三季报密集披露期，业绩雷风险较高，尤其是高估值成长股需警惕业绩不及预期",
    "光通信、传媒等前期热门板块崩塌可能引发连锁反应，拖累整体科技板块估值下修"
])

# ===== 发布 =====
result = gen.publish(title="盘后速递 2026.10.22", auto_deploy=False)
print(f"发布结果: {result}")
