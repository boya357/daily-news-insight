import sys, os
sys.path.insert(0, '/root/daily-news-insight/v3')
os.chdir('/root/daily-news-insight')

from v3.generators.aftermarket import AftermarketGenerator

gen = AftermarketGenerator(date_str="20261021", subtitle="2026.10.21 · 盘后速递")

# ===== 今日核心亮点 =====
gen.add_today_highlight(
    "大盘震荡回调，创业板指跌1.62%领跌，宁德时代单日暴跌超12%重挫新能源板块；"
    "题材股分化加剧，消费电子、出版、养殖业逆势走强，AI算力与半导体止跌企稳迹象初现。"
    "持仓股英维克涨0.69%、铜冠铜箔涨0.29%双双微红，雅克科技、*ST建艺小幅回调。"
    "英维克登上龙虎榜，机构与深股通博弈激烈，净买入3.69亿元需警惕分歧。"
)

# ===== 市场收盘总结 =====
gen.add_market_summary(
    indices=[
        {"name": "上证指数", "value": "3713.03", "change": "-0.60%", "up": False, "icon": "trending_down"},
        {"name": "深证成指", "value": "11704.35", "change": "-0.82%", "up": False, "icon": "trending_down"},
        {"name": "创业板指", "value": "2694.71", "change": "-1.62%", "up": False, "icon": "trending_down"},
    ],
    volume="1.43万亿",
    northbound="净卖出 68.5亿"
)

# ===== 情绪温度计 =====
gen.add_sentiment_thermometer(
    temperature=38,
    volume="1.43万亿",
    up_count="1986",
    down_count="3124",
    limit_up_count="57"
)

# ===== 晚间重要新闻 =====
gen.add_evening_news([
    {
        "title": "宁德时代Q3业绩不及预期，单日暴跌12.03%创历史最大跌幅",
        "content": "宁德时代今日收跌12.03%报227.90元，成交超400亿元创历史天量。市场传闻公司Q3毛利率环比下滑，且海外订单增速放缓，引发机构资金集体出逃。创业板指受其拖累大跌1.62%，新能源板块全线重挫。",
        "time": "20:15",
        "source": "财联社",
        "tag": "重磅",
        "tag_variant": "danger"
    },
    {
        "title": "工信部：加快推进人形机器人、算力等新基建项目落地",
        "content": "工信部新闻发言人表示，将加快推动人形机器人、先进计算、人工智能等新兴基础设施建设，预计四季度相关投资增速将进一步提升。利好AI算力、液冷散热、机器人等产业链。",
        "time": "19:30",
        "source": "科创板日报",
        "tag": "政策",
        "tag_variant": "primary"
    },
    {
        "title": "存储芯片产业链：长鑫科技上市第四日涨1.61%，半导体板块资金回流",
        "content": "长鑫科技今日收涨1.61%报40.97元，上市四日累计涨幅收窄至约140%。半导体板块今日获主力资金净流入13.4亿元，居行业首位，前期超跌后存在技术性反弹需求。",
        "time": "18:45",
        "source": "TheElec",
        "tag": "产业",
        "tag_variant": "success"
    },
    {
        "title": "北向资金今日净卖出68.5亿元，连续第3日净流出",
        "content": "北向资金今日净卖出68.5亿元，其中沪股通净卖出42.3亿，深股通净卖出26.2亿。近3日累计净卖出超200亿元，外资避险情绪升温。",
        "time": "17:00",
        "source": "东方财富",
        "tag": "资金",
        "tag_variant": "warning"
    },
    {
        "title": "10月LPR维持不变，1年期3.45%、5年期以上3.95%",
        "content": "10月21日LPR报价：1年期LPR为3.45%，5年期以上LPR为3.95%，均与上月持平。市场预期年底前仍有降准降息空间。",
        "time": "09:15",
        "source": "央行",
        "tag": "宏观",
        "tag_variant": "default"
    }
])

# ===== 板块涨跌幅排行 =====
gen.add_sector_performance(
    up_sectors=[
        {"name": "养殖业", "change": "+2.97%"},
        {"name": "出版", "change": "+1.81%"},
        {"name": "IT服务", "change": "+1.69%"},
        {"name": "元件", "change": "+1.50%"},
        {"name": "通信设备", "change": "+0.95%"},
    ],
    down_sectors=[
        {"name": "电池", "change": "-4.25%"},
        {"name": "光伏设备", "change": "-3.18%"},
        {"name": "风电设备", "change": "-2.87%"},
        {"name": "能源金属", "change": "-2.65%"},
        {"name": "医疗服务", "change": "-2.31%"},
    ]
)

# ===== 盘面深度解读 =====
gen.add_market_deep_analysis(
    strong_sectors=[
        {"name": "养殖业", "reason": "猪价持续反弹叠加消费旺季预期，东瑞股份涨停领涨，养殖板块迎来估值修复行情，持续性待观察Q4猪价走势。"},
        {"name": "出版传媒", "reason": "AI+出版概念反复活跃，出版传媒涨停带动板块，传媒板块具备政策催化和AI应用双重逻辑，关注三季报业绩兑现情况。"},
        {"name": "元件/半导体", "reason": "顺络电子大涨7.4%领涨元件板块，半导体板块获主力资金净流入13.4亿居首，前期超跌后技术反弹迹象明显，关注存储与先进封装主线。"},
        {"name": "IT服务", "reason": "慧辰股份20cm涨停，AI应用端情绪回暖，国产软件与信创板块受益于政策加码预期，四季度业绩释放可期。"},
    ],
    weak_sectors=[
        {"name": "新能源（电池/光伏/风电）", "reason": "宁德时代暴跌12%引发板块雪崩，新能源赛道机构持仓过重，业绩增速放缓担忧加剧，短期难言见底，规避为主。"},
        {"name": "医疗服务", "reason": "集采预期升温叠加估值偏高，医疗服务板块持续调整，CXO龙头承压，建议等待政策明朗后再布局。"},
        {"name": "能源金属", "reason": "锂价延续下行趋势，天齐锂业等龙头走弱，新能源上游周期性下行压力仍存，左侧抄底为时过早。"},
    ],
    core_view="今日市场呈现典型的结构分化行情，新能源赛道崩塌与科技股企稳形成鲜明对比。创业板指受宁德时代拖累大跌1.62%，但以半导体、AI应用、出版传媒为代表的科技成长股明显抗跌，主力资金开始回流前期超跌的科技板块。我们判断：当前处于牛市中期结构性调整的尾声阶段，新能源权重的下跌是最后一轮恐慌释放，科技主线（AI算力/半导体/存储）有望率先走出独立行情。操作上建议继续规避新能源权重，逢低布局科技成长方向。"
)

# ===== 持仓股跟踪 =====
gen.add_holdings_tracking([
    {
        "name": "英维克",
        "code": "002837",
        "price": "45.15",
        "change": "+0.69%",
        "up": True,
        "comment": "今日微涨0.69%收45.15元，成交8.67亿，换手率1.68%。最低价44.91元接近布林下轨39.63元支撑，RSI6为18.74处于超卖区域，KDJ低位金叉迹象初现。今日登上龙虎榜，机构席位分歧巨大（买入1.76亿 vs 卖出2.47亿），深股通净卖出10.81亿但买盘也有2.12亿。短期45元附近有支撑，反弹压力位在5日均线44.76元和10日均线47.17元。"
    },
    {
        "name": "铜冠铜箔",
        "code": "301217",
        "price": "86.71",
        "change": "+0.29%",
        "up": True,
        "comment": "今日微涨0.29%收86.71元，成交10.41亿，换手率1.43%。最低价86.31元再创阶段新低后收回，RSI6为28.50处于超卖边缘，KDJ的J值30.45低位走平。5日均线86.52元走平，短期有止跌企稳迹象。布林下轨77.45元为强支撑，上方压力位10日均线90.20元。主力资金今日净流出943万元，较前期明显收窄，抛压减轻。"
    },
    {
        "name": "雅克科技",
        "code": "002409",
        "price": "96.80",
        "change": "-0.46%",
        "up": False,
        "comment": "今日微跌0.46%收96.80元，成交9.49亿，换手率3.05%。最低价96.05元接近布林下轨86.30元上方，RSI6为12.29极度超卖，KDJ的K值13.36处于历史低位区间，技术上存在反弹需求。但MACD绿柱继续放大（-3.85），空头趋势尚未扭转。支撑位95元（前期平台），压力位10日均线103.39元。半导体材料板块整体止跌，关注能否跟随板块反弹。"
    },
    {
        "name": "*ST建艺",
        "code": "002789",
        "price": "13.04",
        "change": "-0.61%",
        "up": False,
        "comment": "今日微跌0.61%收13.04元，成交0.23亿，换手率1.12%。最低价12.50元探底后回升，形成长下影线。5日均线13.70元构成压力，下方支撑位12.50元。作为ST股，今日表现明显抗跌，属于组合中的防御品种。主力资金今日净流入90万元，波动较小。继续作为组合缓冲持有，若跌破12.5元需警惕。"
    }
])

# ===== 龙虎榜深度解析 =====
gen.add_dragon_tiger_list([
    {
        "name": "英维克",
        "code": "002837",
        "change": "+0.69%",
        "up": True,
        "institutions": 3,
        "reason": "日涨幅偏离值达7%",
        "net_buy": "+3.69亿"
    },
    {
        "name": "南威软件",
        "code": "603636",
        "change": "+10.01%",
        "up": True,
        "institutions": 0,
        "reason": "日涨幅偏离值达7%",
        "net_buy": "-1.79亿"
    },
    {
        "name": "大业股份",
        "code": "603278",
        "change": "+10.01%",
        "up": True,
        "institutions": 0,
        "reason": "三日涨幅偏离值20%",
        "net_buy": "+3512万"
    }
])

# ===== 龙虎榜深度分析补充（自定义HTML） =====
from v3.core.report import Report
from v3.components.layout import Section, SubCard

lhb_detail_html = '''
<div style="display: flex; flex-direction: column; gap: 20px; margin-top: 16px;">
    
    <div style="background: rgba(30,30,50,0.5); border: 1px solid rgba(255,255,255,0.08); border-radius: 16px; padding: 20px;">
        <div style="font-size: 16px; font-weight: 700; color: #f1f5f9; margin-bottom: 12px;">🐉 英维克（002837）龙虎榜深度解读</div>
        <div style="font-size: 13px; color: #94a3b8; line-height: 1.8;">
            <p><strong style="color: #f59e0b;">上榜原因：</strong>日涨幅偏离值达7%，总买入10.11亿，总卖出6.43亿，净买入3.69亿</p>
            <p><strong style="color: #10b981;">买方分析：</strong>买方前五中机构专用占据2席（买二1.76亿+买五未上榜），开源证券西安西大街买入1.22亿（知名游资席位），国泰海通上海长宁江苏路买入1.35亿（量化席位），国泰海通北京知春路买入1.56亿（知春路游资）。</p>
            <p><strong style="color: #ef4444;">卖方分析：</strong>卖方前五中机构专用占据3席（合计卖出约2.47亿），深股通专用卖出3.20亿（同时买入2.12亿，净卖出1.08亿），招商证券深圳科技园卖出5713万。</p>
            <p><strong style="color: #fbbf24;">持续性判断：</strong>⭐⭐⭐ 中等偏强。机构席位多空分歧巨大（买1.76亿 vs 卖2.47亿），说明机构内部对当前位置看法不一。游资积极介入（知春路+开源西大街），短期有反弹动力，但机构整体净卖出需警惕反弹高度。压力位48-50元区间。</p>
        </div>
    </div>
    
    <div style="background: rgba(30,30,50,0.5); border: 1px solid rgba(255,255,255,0.08); border-radius: 16px; padding: 20px;">
        <div style="font-size: 16px; font-weight: 700; color: #f1f5f9; margin-bottom: 12px;">🐉 南威软件（603636）龙虎榜深度解读</div>
        <div style="font-size: 13px; color: #94a3b8; line-height: 1.8;">
            <p><strong style="color: #f59e0b;">上榜原因：</strong>日涨幅偏离值达7%，总买入6382万，总卖出8174万，净卖出1793万</p>
            <p><strong style="color: #10b981;">买方分析：</strong>沪股通专用买入2300万（买一），国泰海通南京金融城买入1070万，瑞银证券上海花园石桥路买入1061万（外资席位），摩根大通上海银城中路未进入买方前五。</p>
            <p><strong style="color: #ef4444;">卖方分析：</strong>沪股通专用卖出3217万（卖一，同时买入2300万，净卖出917万），国泰海通总部卖出1570万，摩根大通上海银城中路卖出1214万，瑞银证券卖出1177万。外资席位集体出逃。</p>
            <p><strong style="color: #fbbf24;">持续性判断：</strong>⭐⭐ 偏弱。今日虽涨停但龙虎榜净卖出，且外资席位（沪股通+瑞银+摩根大通）集体做T减仓，游资参与度较低。三日累计净卖出2760万，主力资金有兑现迹象。建议观望为主，不追高。</p>
        </div>
    </div>
    
    <div style="background: rgba(30,30,50,0.5); border: 1px solid rgba(255,255,255,0.08); border-radius: 16px; padding: 20px;">
        <div style="font-size: 16px; font-weight: 700; color: #f1f5f9; margin-bottom: 12px;">🐉 大业股份（603278）龙虎榜深度解读</div>
        <div style="font-size: 13px; color: #94a3b8; line-height: 1.8;">
            <p><strong style="color: #f59e0b;">上榜原因：</strong>三日涨幅偏离值累计达20%，总买入5951万，总卖出2438万，净买入3513万</p>
            <p><strong style="color: #10b981;">买方分析：</strong>中信证券安徽分公司买入1550万（买一），五矿证券江苏分公司买入1478万，国泰海通重庆民生路买入1093万，华鑫证券上海陆家嘴买入879万（量化席位）。买方阵容以地方游资为主。</p>
            <p><strong style="color: #ef4444;">卖方分析：</strong>中泰证券诸城人民东路卖出1020万（卖一，本地席位可能为原始股东减持），银河证券如皋健康路卖出468万。卖出压力较小，筹码相对稳定。</p>
            <p><strong style="color: #fbbf24;">持续性判断：</strong>⭐⭐⭐ 中等。净买入3513万力度尚可，卖方抛压不大，但买方均为地方游资而非一线顶级游资，持续性存疑。叠加个股属于轮胎制造传统行业，缺乏题材想象力。明日若不能强势连板，追高风险较大。</p>
        </div>
    </div>
    
</div>
'''

lhb_section = Section(title="📊 龙虎榜深度分析", content=lhb_detail_html, icon="bar_chart")
gen._components.append(lhb_section)

# ===== 重点关注标的 =====
watchlist_html = '''
<div style="display: flex; flex-direction: column; gap: 16px;">
    
    <div style="background: linear-gradient(135deg, rgba(245,158,11,0.1) 0%, rgba(239,68,68,0.08) 100%); 
                border: 1px solid rgba(245,158,11,0.3); border-radius: 16px; padding: 20px;">
        <div style="display: flex; align-items: center; margin-bottom: 12px;">
            <span style="font-size: 18px; font-weight: 700; color: #f59e0b;">🔥 华海诚科（688535）</span>
            <span style="margin-left: 12px; background: rgba(245,158,11,0.2); color: #f59e0b; 
                         font-size: 12px; padding: 4px 10px; border-radius: 12px;">关注评级：A+</span>
        </div>
        <div style="font-size: 13px; color: #e2e8f0; line-height: 1.8;">
            <p><strong>当前价格：</strong>78.67元 · 今日-0.16% · 成交2.81亿 · 换手2.65%</p>
            <p><strong>关注逻辑：</strong>先进封装材料龙头，环氧塑封料（EMC）国产替代核心标的。HBM产业链爆发带动EMC需求快速增长，公司是国内少数能量产高端EMC的企业。前期从120元高点回调超30%，当前78元附近估值已回到合理区间，RSI6为24.7处于超卖区域，技术面反弹需求强烈。</p>
            <p><strong>目标价：</strong>第一目标位90元（5日均线+10日均线附近），第二目标位105元（20日均线附近）</p>
            <p><strong>止损位：</strong>75元（跌破布林下轨67.86元前的第一道防线，若有效跌破则看至70元）</p>
            <p><strong>操作建议：</strong>78元以下可分批建仓，首仓20%，若跌至75元再加仓20%，总仓位≤40%。反弹至90元减仓1/3，100元以上减仓至底仓。</p>
        </div>
    </div>
    
    <div style="background: linear-gradient(135deg, rgba(16,185,129,0.1) 0%, rgba(5,150,105,0.08) 100%); 
                border: 1px solid rgba(16,185,129,0.3); border-radius: 16px; padding: 20px;">
        <div style="display: flex; align-items: center; margin-bottom: 12px;">
            <span style="font-size: 18px; font-weight: 700; color: #10b981;">💎 长电科技（600584）</span>
            <span style="margin-left: 12px; background: rgba(16,185,129,0.2); color: #10b981; 
                         font-size: 12px; padding: 4px 10px; border-radius: 12px;">关注评级：A</span>
        </div>
        <div style="font-size: 13px; color: #e2e8f0; line-height: 1.8;">
            <p><strong>当前价格：</strong>57.23元 · 今日-0.03% · 成交21.34亿 · 换手2.07%</p>
            <p><strong>关注逻辑：</strong>国内封测龙头，先进封装（CoWoS/2.5D/3D）核心受益标的。AI芯片爆发带动先进封装需求激增，长电科技是国内技术最领先、产能最大的封测企业。今日成交21亿明显放量，主力资金有回流迹象，股价在57元附近获得支撑（接近前期平台）。MACD绿柱收窄至-0.94，下跌动能衰减。</p>
            <p><strong>目标价：</strong>第一目标位64元（20日均线+布林中轨），第二目标位70元（60日均线附近）</p>
            <p><strong>止损位：</strong>54元（跌破前期低点52.58元前的支撑位）</p>
            <p><strong>操作建议：</strong>57-58元区间可建底仓30%，若回调至55元加仓20%。反弹至64元减仓1/2，剩余仓位看70元。</p>
        </div>
    </div>
    
    <div style="background: linear-gradient(135deg, rgba(139,92,246,0.1) 0%, rgba(79,70,229,0.08) 100%); 
                border: 1px solid rgba(139,92,246,0.3); border-radius: 16px; padding: 20px;">
        <div style="display: flex; align-items: center; margin-bottom: 12px;">
            <span style="font-size: 18px; font-weight: 700; color: #8b5cf6;">⚡ 顺络电子（002138）</span>
            <span style="margin-left: 12px; background: rgba(139,92,246,0.2); color: #8b5cf6; 
                         font-size: 12px; padding: 4px 10px; border-radius: 12px;">关注评级：B+</span>
        </div>
        <div style="font-size: 13px; color: #e2e8f0; line-height: 1.8;">
            <p><strong>当前价格：</strong>约28元 · 今日+7.40%（板块领涨）· 元件板块涨幅第一</p>
            <p><strong>关注逻辑：</strong>国内电感龙头，AI服务器/汽车电子/消费电子多轮驱动。今日元件板块大涨1.5%，顺络电子领涨7.4%，资金开始布局消费电子产业链的复苏预期。消费电子处于库存周期底部，Q4有望迎来环比改善。顺络电子作为被动元件龙头，业绩弹性大。</p>
            <p><strong>目标价：</strong>第一目标位32元（前期平台），第二目标位36元（年线附近）</p>
            <p><strong>止损位：</strong>26元（今日实体阳线的2/3位置）</p>
            <p><strong>操作建议：</strong>今日涨幅较大，不建议追高，等待回调至27-28元区间再考虑建仓。仓位≤20%，快进快出为主。</p>
        </div>
    </div>
    
</div>
'''

watch_section = Section(title="🎯 重点关注标的（3只）", content=watchlist_html, icon="star")
gen._components.append(watch_section)

# ===== 明日关键预判 =====
gen.add_tomorrow_prediction([
    {
        "name": "AI算力/液冷散热",
        "direction": "震荡",
        "confidence": 65,
        "reason": "英维克今日微涨并登上龙虎榜，机构与游资博弈激烈。短期超跌后有技术反弹需求，但上方套牢盘较重，5日和10日均线构成压力。预计明日震荡为主，波动区间44-48元。"
    },
    {
        "name": "半导体/先进封装",
        "direction": "看涨",
        "confidence": 70,
        "reason": "半导体板块今日获主力资金净流入13.4亿居行业首位，雅克科技、长电科技等龙头止跌企稳。前期超跌幅度大，估值已回落至合理区间，叠加产业催化不断，技术性反弹概率较大。"
    },
    {
        "name": "新能源（电池/光伏）",
        "direction": "看跌",
        "confidence": 75,
        "reason": "宁德时代今日暴跌12%创历史最大跌幅，成交超400亿天量，机构资金疯狂出逃。新能源赛道趋势性走坏，短期难言见底，预计明日继续下探寻找支撑。规避为主。"
    },
    {
        "name": "大盘走势",
        "direction": "震荡",
        "confidence": 60,
        "reason": "上证指数3700点附近有支撑，今日最低3703点后收回。但创业板受新能源拖累继续走弱，市场分化严重。预计明日大盘震荡整理，沪指3700-3750区间波动，关注量能变化。"
    }
])

# ===== 明日操作计划 =====
trading_plan = '''
<div style="background: rgba(30,30,50,0.5); border: 1px solid rgba(255,255,255,0.08); border-radius: 16px; padding: 24px;">
    <div style="font-size: 16px; font-weight: 700; color: #f1f5f9; margin-bottom: 20px;">📋 明日操作策略（2026.10.22）</div>
    
    <div style="margin-bottom: 20px;">
        <div style="font-size: 14px; font-weight: 600; color: #f59e0b; margin-bottom: 8px;">一、大盘判断</div>
        <div style="font-size: 13px; color: #cbd5e1; line-height: 1.8;">
            上证指数在3700点附近获得支撑，但创业板受新能源权重拖累继续走弱。市场呈现典型的结构性分化，科技股企稳、新能源崩盘的格局有望延续。
            预计明日沪指震荡整理，区间3700-3750点；创业板继续下探考验2650点支撑。操作上聚焦科技成长方向，坚决规避新能源权重。
        </div>
    </div>
    
    <div style="margin-bottom: 20px;">
        <div style="font-size: 14px; font-weight: 600; color: #f59e0b; margin-bottom: 8px;">二、仓位建议</div>
        <div style="font-size: 13px; color: #cbd5e1; line-height: 1.8;">
            整体仓位控制在50%-60%，其中科技成长方向40%、防御品种10%、现金储备40%-50%。
            当前处于底部磨底阶段，不宜满仓抄底，但也不宜过度悲观，保持分批建仓节奏。
        </div>
    </div>
    
    <div style="margin-bottom: 20px;">
        <div style="font-size: 14px; font-weight: 600; color: #f59e0b; margin-bottom: 8px;">三、持仓股操作计划</div>
        <div style="font-size: 13px; color: #cbd5e1; line-height: 2;">
            <p><strong style="color: #fb923c;">1. 英维克（002837）</strong>：当前价45.15元<br>
            &nbsp;&nbsp;• 反弹至<span style="color: #10b981; font-weight: 700;">48元以上</span>减仓1/3（降低持仓成本）<br>
            &nbsp;&nbsp;• 反弹至<span style="color: #10b981; font-weight: 700;">50元以上</span>再减仓1/3<br>
            &nbsp;&nbsp;• 跌破<span style="color: #ef4444; font-weight: 700;">44元</span>止损减仓至底仓（100股观察仓）<br>
            &nbsp;&nbsp;• 44-48元区间持有观望，不做操作</p>
            
            <p><strong style="color: #fb923c;">2. 铜冠铜箔（301217）</strong>：当前价86.71元<br>
            &nbsp;&nbsp;• 反弹至<span style="color: #10b981; font-weight: 700;">92元以上</span>减仓1/3<br>
            &nbsp;&nbsp;• 反弹至<span style="color: #10b981; font-weight: 700;">98元以上</span>再减仓1/3<br>
            &nbsp;&nbsp;• 跌破<span style="color: #ef4444; font-weight: 700;">84元</span>止损减仓<br>
            &nbsp;&nbsp;• 84-90元区间持有，等待铜箔产业催化</p>
            
            <p><strong style="color: #fb923c;">3. 雅克科技（002409）</strong>：当前价96.80元<br>
            &nbsp;&nbsp;• 反弹至<span style="color: #10b981; font-weight: 700;">105元以上</span>减仓1/3<br>
            &nbsp;&nbsp;• 反弹至<span style="color: #10b981; font-weight: 700;">115元以上</span>再减仓1/3<br>
            &nbsp;&nbsp;• 跌破<span style="color: #ef4444; font-weight: 700;">93元</span>止损减仓<br>
            &nbsp;&nbsp;• 93-100元区间持有，半导体材料是主线方向</p>
            
            <p><strong style="color: #fb923c;">4. *ST建艺（002789）</strong>：当前价13.04元<br>
            &nbsp;&nbsp;• 继续持有作为组合防御缓冲<br>
            &nbsp;&nbsp;• 跌破<span style="color: #ef4444; font-weight: 700;">12.5元</span>减仓50%<br>
            &nbsp;&nbsp;• 反弹至<span style="color: #10b981; font-weight: 700;">14.5元以上</span>考虑减仓</p>
        </div>
    </div>
    
    <div>
        <div style="font-size: 14px; font-weight: 600; color: #f59e0b; margin-bottom: 8px;">四、新建仓计划</div>
        <div style="font-size: 13px; color: #cbd5e1; line-height: 2;">
            <p><strong style="color: #10b981;">1. 华海诚科（688535）</strong>：先进封装材料龙头<br>
            &nbsp;&nbsp;• 建仓区间：<span style="font-weight: 700;">76-78元</span>，首仓20%<br>
            &nbsp;&nbsp;• 加仓条件：跌至75元以下加20%，总仓位≤40%<br>
            &nbsp;&nbsp;• 止损位：72元（有效跌破则止损）</p>
            
            <p><strong style="color: #10b981;">2. 长电科技（600584）</strong>：封测龙头<br>
            &nbsp;&nbsp;• 建仓区间：<span style="font-weight: 700;">56-58元</span>，底仓30%<br>
            &nbsp;&nbsp;• 加仓条件：回调至55元加20%<br>
            &nbsp;&nbsp;• 止损位：54元</p>
        </div>
    </div>
</div>
'''

plan_section = Section(title="🎯 明日操作策略", content=trading_plan, icon="target", variant="highlight")
gen._components.append(plan_section)

# ===== 风险提示 =====
gen.add_risk_warning([
    "宁德时代暴跌引发新能源赛道系统性风险，可能进一步拖累创业板指和市场情绪",
    "北向资金连续3日净卖出超200亿，外资持续流出可能加剧市场波动",
    "美股科技股今晚若大幅波动，可能影响明日A股科技板块开盘",
    "持仓股均处于下降趋势中，技术性反弹后可能继续下探，需严格执行止损纪律",
    "10月底为三季报密集披露期，业绩雷风险需警惕，尤其是高估值成长股"
])

# ===== 发布 =====
result = gen.publish(title="盘后速递 2026.10.21", auto_deploy=False)
print(f"发布结果: {result}")
