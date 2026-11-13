"""2026-11-12 盘后速递 V3.0生成脚本"""
import sys, os
sys.path.insert(0, 'v3')
os.chdir('/root/daily-news-insight')

from v3.generators.aftermarket import AftermarketGenerator
from v3.components.layout import Section

DATE = "20261112"
SUBTITLE = "2026.11.12 · 盘后速递 · 科技冲高回落"

gen = AftermarketGenerator(date_str=DATE, subtitle=SUBTITLE)

gen.add_today_highlight(
    "11月12日A股早盘科技股一度强势上攻，科创50盘中涨超4%，但午后风云突变，AI硬件、光通信、机器人、游戏等热门方向集体跳水，中际旭创从+5%跌至-6.11%，日内振幅近11%。截至收盘，沪指跌0.67%报3655.83点，深成指跌1.68%，创业板指跌2.44%，两市成交额1.95万亿放量2571亿，超4600只个股下跌。半导体板块净流入23.53亿成为唯一亮点，通信设备净流出68.14亿居首，资金高低切换明显。"
)

gen.add_market_summary(
    indices=[
        {"name": "上证指数", "value": "3655.83", "change": "-0.67%", "up": False, "icon": "trending_down"},
        {"name": "深证成指", "value": "11197.98", "change": "-1.68%", "up": False, "icon": "trending_down"},
        {"name": "创业板指", "value": "2509.43", "change": "-2.44%", "up": False, "icon": "trending_down"},
        {"name": "科创50", "value": "1309.84", "change": "+0.73%", "up": True, "icon": "trending_up"},
    ],
    volume="1.95万亿（放量2571亿）",
    northbound="成交2497.56亿，占比12.93%"
)

gen.add_sentiment_thermometer(
    temperature=32,
    volume="1.95万亿",
    up_count="875↑",
    down_count="4635↓",
    limit_up_count="37"
)

gen.add_market_deep_analysis(
    strong_sectors=[
        {"name": "兵装重组/军工", "reason": "板块逆势上涨2.07%，地面兵装全天强势，中国兵器装备集团资产整合预期发酵，北方长龙涨11.45%，航天南湖涨10.23%，中船系同步走强+1.09%，军工成为午后资金避险首选方向。"},
        {"name": "燃气/油气", "reason": "燃气板块涨0.95%，东方环宇4连板，洪通燃气涨停，新疆火炬、水发燃气跟涨。油价高位运行+冬季用气旺季+油气体制改革预期三重催化，成为防御性资金抱团方向。"},
        {"name": "半导体", "reason": "板块全天获得资金净流入约23.53亿元，是当日唯一大幅净流入行业。寒武纪涨8.11%成交201.72亿，燧原科技涨13.13%创上市新高，盛科通信涨11.34%。国产算力芯片自主可控逻辑强化，承接光模块流出资金。"},
        {"name": "白酒/消费", "reason": "白酒板块涨0.79%，银行涨约0.3%，红利资产午后发力，资金防守偏好抬升，形成典型的跷跷板效应，贵州茅台获北向资金持续买入。"},
    ],
    weak_sectors=[
        {"name": "贵金属", "reason": "贵金属板块暴跌5.77%领跌两市，山金国际跌超9%，赤峰黄金、招金黄金、山东黄金集体重挫。美国通胀数据超预期，美元走强，加息预期升温，国际金价大幅回落是主因。"},
        {"name": "游戏/影视/传媒", "reason": "游戏板块跌4.79%，影视院线跌4.19%，AI语料跌3.17%，AI视频跌3.38%。芒果超媒结束8连阳跌9.54%，华策影视跌13.97%，上海电影跌停，前期强势传媒AI应用方向集体兑现。"},
        {"name": "光模块/CPO/通信设备", "reason": "通信设备全天净流出68.14亿元居首，中际旭创从+5%跌至-6.11%振幅达11%成交336亿，新易盛跌4.38%成交256亿，天孚通信从+6%回落至-2.58%。昨日最吸金的方向次日即成为最大砸盘主力，典型的资金兑现。"},
        {"name": "人形机器人/自动化", "reason": "电机跌3.34%，自动化设备跌超3%，机器人板块从早盘涨超2%到午后翻绿大跌，三花智控、拓普集团等龙头由涨转跌，前期涨幅过大后的获利盘集中出逃。"},
    ],
    core_view=(
        "<b>核心判断：反弹进入震荡消化阶段，科技股冲高回落暴露三大警示信号。</b><br><br>"
        "今日盘面最值得警惕的特征有三：<br>"
        "<b>第一，放量滞涨+冲高跳水</b>。1.95万亿成交额较昨日放量2571亿，但上涨家数仅875只，下跌高达4635只，意味着大量资金在借反弹出货，而非进场抄底。半天成交1.23万亿时下跌股票就已接近3000只，指数上涨全靠少数权重撑场面，赚钱效应极差。<br>"
        "<b>第二，热门股日内从大涨到大跌，杀伤力极强</b>。中际旭创早盘+5%到收盘-6.11%，日内追高者亏损超10%；新易盛、天孚通信、铜冠铜箔盘中最高涨超5%，收盘均翻绿下跌。这种走势说明追涨资金已被埋，短期情绪会迅速降温。<br>"
        "<b>第三，资金跷跷板效应显现</b>。半导体净流入23.53亿的同时，通信设备净流出68.14亿，资金从光模块切向算力芯片是结构性选择而非全面撤退，叠加白酒/银行/军工等防御板块逆势走强，说明风险偏好正在快速收缩。<br><br>"
        "<b>外因方面</b>：美国通胀数据高于预期，市场上调12月加息预期，美元指数走强，长端美债收益率再创新高，对成长股估值形成压制；海外AI龙头晚间大跌直接拖累早盘情绪。<br><br>"
        "<b>策略上</b>：大的反弹结构没有破坏，但短期（2-3个交易日）将进入震荡消化期，操作上切忌追高，逢反弹对高位筹码进行减仓，等待回踩3600点附近的二次确认机会。科技方向重点关注半导体设备、算力芯片等相对强势分支的回踩低吸机会，光模块等高位兑现板块短期规避。"
    )
)

gen.add_sector_performance(
    up_sectors=[
        {"name": "兵装重组概念", "change": "+2.07%", "up": True, "leader": "北方长龙+11.45%"},
        {"name": "中船系", "change": "+1.09%", "up": True, "leader": "中船防务"},
        {"name": "科创次新股", "change": "+0.98%", "up": True, "leader": "燧原科技+13.13%"},
        {"name": "燃气", "change": "+0.95%", "up": True, "leader": "东方环宇4连板"},
        {"name": "白酒", "change": "+0.79%", "up": True, "leader": "贵州茅台"},
        {"name": "半导体", "change": "+0.5%+", "up": True, "leader": "寒武纪+8.11%"},
    ],
    down_sectors=[
        {"name": "贵金属", "change": "-5.77%", "up": False, "leader": "山金国际-9%+"},
        {"name": "游戏", "change": "-4.79%", "up": False, "leader": "凯撒文化"},
        {"name": "影视院线", "change": "-4.19%", "up": False, "leader": "上海电影跌停"},
        {"name": "AI语料/AI视频", "change": "-3.17%/-3.38%", "up": False, "leader": "华策影视-13.97%"},
        {"name": "电机/自动化", "change": "-3.34%", "up": False, "leader": "雷赛智能-7.6%"},
        {"name": "通信设备/CPO", "change": "-3%+", "up": False, "leader": "中际旭创-6.11%"},
    ]
)

holdings_html = '''
<div style="display: flex; flex-direction: column; gap: 16px;">

<div style="background: linear-gradient(135deg, rgba(239,68,68,0.12) 0%, rgba(234,88,12,0.06) 100%); border: 1px solid rgba(239,68,68,0.25); border-radius: 16px; padding: 20px; backdrop-filter: blur(10px);">
  <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
    <div>
      <span style="font-size: 17px; font-weight: 700; color: #f1f5f9;">🔄 英维克</span>
      <span style="font-size: 12px; color: #94a3b8; margin-left: 8px;">002837 · 液冷散热</span>
      <span style="font-size: 11px; padding: 2px 8px; border-radius: 10px; background: rgba(239,68,68,0.2); color: #f87171; margin-left: 8px;">大跌破位</span>
    </div>
    <div style="text-align: right;">
      <div style="font-size: 22px; font-weight: 800; color: #ef4444;">40.98</div>
      <div style="font-size: 13px; color: #ef4444; font-weight: 600;">-5.40%  成交28.45亿</div>
    </div>
  </div>
  <div style="display: grid; grid-template-columns: 1fr 1fr 1fr 1fr; gap: 8px; margin-bottom: 12px; font-size: 12px;">
    <div style="background: rgba(255,255,255,0.04); border-radius: 8px; padding: 8px; text-align: center;"><div style="color: #94a3b8;">今开</div><div style="color: #e2e8f0; font-weight: 600;">43.34</div></div>
    <div style="background: rgba(255,255,255,0.04); border-radius: 8px; padding: 8px; text-align: center;"><div style="color: #94a3b8;">最高</div><div style="color: #e2e8f0; font-weight: 600;">44.50</div></div>
    <div style="background: rgba(255,255,255,0.04); border-radius: 8px; padding: 8px; text-align: center;"><div style="color: #94a3b8;">最低</div><div style="color: #ef4444; font-weight: 600;">40.82</div></div>
    <div style="background: rgba(255,255,255,0.04); border-radius: 8px; padding: 8px; text-align: center;"><div style="color: #94a3b8;">换手率</div><div style="color: #e2e8f0; font-weight: 600;">5.87%</div></div>
  </div>
  <div style="font-size: 13px; color: #cbd5e1; line-height: 1.8;">
    <p style="margin: 0 0 8px 0;"><b style="color:#f87171">技术面：</b>今日开盘短暂冲高至44.50元后持续走弱，午后跟随AI硬件板块跳水，最低下探40.82元，跌破前期42元支撑位，收盘40.98元创本轮调整新低。5/10/20日均线呈空头排列向下发散，40元整数关口是下一道重要心理防线；MACD绿柱继续放大，KDJ进入超卖区但无拐头迹象。</p>
    <p style="margin: 0 0 8px 0;"><b style="color:#fbbf24">资金面：</b>全天成交28.45亿元，主力资金净流出2.03亿元。融资余额31.11亿昨日净买入3763万，融资盘仍在加仓，警惕后续被动平仓风险；北向资金三季度已减持1143万股，外资在高位开始兑现。</p>
    <p style="margin: 0;"><b style="color:#60a5fa">操作建议：</b>🔴 当前价40.98元深度浮亏约60%（成本104.23元），技术破位信号明确。操作策略：<b>①40元为止损最后防线</b>，若明日放量跌破40元（成交量较今日放大20%以上），果断减仓1/2至仅剩底仓；<b>②反弹减仓机会</b>：若明日反抽42.5-43.5元区间（5日线附近），是绝佳减仓窗口，减仓1/3，保留底仓观察；<b>③严禁补仓</b>：液冷板块整体处于下降通道，逆势加仓会越套越深；<b>④建仓观察点</b>：等待缩量企稳信号（连续2日成交额低于15亿且不创新低），再考虑在36-38元区间小仓位试探。90天机构目标均价56.84元为中长期反弹目标，需基本面催化配合。</p>
  </div>
</div>

<div style="background: linear-gradient(135deg, rgba(251,146,60,0.12) 0%, rgba(234,88,12,0.06) 100%); border: 1px solid rgba(251,146,60,0.25); border-radius: 16px; padding: 20px; backdrop-filter: blur(10px);">
  <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
    <div>
      <span style="font-size: 17px; font-weight: 700; color: #f1f5f9;">🥉 铜冠铜箔</span>
      <span style="font-size: 12px; color: #94a3b8; margin-left: 8px;">301217 · PCB铜箔/HVLP</span>
      <span style="font-size: 11px; padding: 2px 8px; border-radius: 10px; background: rgba(251,146,60,0.2); color: #fb923c; margin-left: 8px;">冲高回落</span>
    </div>
    <div style="text-align: right;">
      <div style="font-size: 22px; font-weight: 800; color: #f59e0b;">71.64</div>
      <div style="font-size: 13px; color: #ef4444; font-weight: 600;">-2.40%  成交21.43亿</div>
    </div>
  </div>
  <div style="display: grid; grid-template-columns: 1fr 1fr 1fr 1fr; gap: 8px; margin-bottom: 12px; font-size: 12px;">
    <div style="background: rgba(255,255,255,0.04); border-radius: 8px; padding: 8px; text-align: center;"><div style="color: #94a3b8;">今开</div><div style="color: #e2e8f0; font-weight: 600;">73.10</div></div>
    <div style="background: rgba(255,255,255,0.04); border-radius: 8px; padding: 8px; text-align: center;"><div style="color: #94a3b8;">最高</div><div style="color: #10b981; font-weight: 600;">77.50(+5.6%)</div></div>
    <div style="background: rgba(255,255,255,0.04); border-radius: 8px; padding: 8px; text-align: center;"><div style="color: #94a3b8;">最低</div><div style="color: #ef4444; font-weight: 600;">71.63</div></div>
    <div style="background: rgba(255,255,255,0.04); border-radius: 8px; padding: 8px; text-align: center;"><div style="color: #94a3b8;">换手率</div><div style="color: #e2e8f0; font-weight: 600;">3.46%</div></div>
  </div>
  <div style="font-size: 13px; color: #cbd5e1; line-height: 1.8;">
    <p style="margin: 0 0 8px 0;"><b style="color:#fbbf24">盘面特征：</b>典型的冲高回落洗盘走势，早盘一度冲高至77.50元（涨幅+5.6%），但午后跟随大盘跳水，最终以最低价71.64元收盘，日内振幅高达8%，从高点到收盘回落近8%，追高资金全部被套。上午11:30前还曾临时停牌显示交易异常，多空博弈激烈。</p>
    <p style="margin: 0 0 8px 0;"><b style="color:#10b981">基本面：</b>前三季度归母净利润3.39亿元同比+439.75%，Q3单季净利同比+345%，高端PCB铜箔技改项目1.54亿已获批，HVLP铜箔国产替代逻辑长期成立。但当前TTM市盈率175倍估值偏高，股价从28.27元低点已反弹超150%，短期获利盘丰厚。</p>
    <p style="margin: 0;"><b style="color:#60a5fa">操作建议：</b>🟡 今日走势显示75-78元区间抛压沉重，短期难以一蹴而就突破。操作策略：<b>①75元以上为减仓区</b>，若明日反抽至74-76元区间，持仓较重者减仓1/3锁定利润；<b>②支撑位70元</b>，若不破70元可继续持有底仓，放量跌破70元（成交额超25亿+阴线）需减仓至底仓；<b>③加仓点</b>：等待回调至65-68元区间（20日均线附近）缩量企稳后，可小仓位（10-15%）加仓做反弹；<b>④止损位65元</b>，跌破65元坚决止损离场。上方目标位先看80元，突破后看前高88元。</p>
  </div>
</div>

<div style="background: linear-gradient(135deg, rgba(96,165,250,0.12) 0%, rgba(139,92,246,0.06) 100%); border: 1px solid rgba(96,165,250,0.25); border-radius: 16px; padding: 20px; backdrop-filter: blur(10px);">
  <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
    <div>
      <span style="font-size: 17px; font-weight: 700; color: #f1f5f9;">🧪 雅克科技</span>
      <span style="font-size: 12px; color: #94a3b8; margin-left: 8px;">002409 · 半导体材料/HBM前驱体</span>
      <span style="font-size: 11px; padding: 2px 8px; border-radius: 10px; background: rgba(16,185,129,0.2); color: #34d399; margin-left: 8px;">相对抗跌</span>
    </div>
    <div style="text-align: right;">
      <div style="font-size: 22px; font-weight: 800; color: #10b981;">90.37</div>
      <div style="font-size: 13px; color: #10b981; font-weight: 600;">+1.19%  存储芯片龙头</div>
    </div>
  </div>
  <div style="font-size: 13px; color: #cbd5e1; line-height: 1.8;">
    <p style="margin: 0 0 8px 0;"><b style="color:#10b981">盘面特征：</b>在科技股普遍大跌背景下雅克科技逆势上涨1.19%，表现相当抗跌，验证了存储芯片/HBM材料龙头的韧性。今日召开2026年第三次临时股东大会，市场预期后续可能释放更多HBM订单和产能扩张利好。半导体材料板块净流入约23.53亿，雅克作为板块核心标的直接受益。</p>
    <p style="margin: 0 0 8px 0;"><b style="color:#60a5fa">技术面：</b>股价从前期115元高点回调至当前90元附近，跌幅约22%，在85-90元区间获得明显支撑。当前PE（TTM）约40倍，在半导体材料板块中估值合理偏低（ROE 10.19%行业排名前列）。MACD有底背离迹象，KDJ在超卖区有金叉预期。今日逆势收阳是转强信号。</p>
    <p style="margin: 0;"><b style="color:#60a5fa">操作建议：</b>🟢 持仓继续持有，雅克是当前组合中最具确定性的底仓品种。操作策略：<b>①底仓（30%仓位）继续持有</b>，HBM/存储芯片景气度向上逻辑未变，2027年全球HBM需求翻倍增长确定；<b>②加仓点</b>：85-88元区间是绝佳击球区，回踩时可加仓20%；<b>③减仓点</b>：反弹至100-105元区间（前期套牢盘密集区），机动仓部分（约1/3）可高抛减仓做波段；<b>④中线目标位</b>：115-120元（前期高点附近），需存储芯片涨价/HBM大客户订单落地催化；<b>⑤止损位</b>：有效跌破83元（20周均线）减仓一半，跌破78元清仓机动仓。今日逆势走强验证了之前"跌停日不抄底、90元以下分批建仓"的判断正确。</p>
  </div>
</div>

<div style="background: linear-gradient(135deg, rgba(148,163,184,0.12) 0%, rgba(100,116,139,0.06) 100%); border: 1px solid rgba(148,163,184,0.25); border-radius: 16px; padding: 20px; backdrop-filter: blur(10px);">
  <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
    <div>
      <span style="font-size: 17px; font-weight: 700; color: #f1f5f9;">🏗️ *ST建艺</span>
      <span style="font-size: 12px; color: #94a3b8; margin-left: 8px;">002789 · ST重组</span>
      <span style="font-size: 11px; padding: 2px 8px; border-radius: 10px; background: rgba(251,191,36,0.2); color: #fbbf24; margin-left: 8px;">小跌</span>
    </div>
    <div style="text-align: right;">
      <div style="font-size: 22px; font-weight: 800; color: #f59e0b;">8.89</div>
      <div style="font-size: 13px; color: #ef4444; font-weight: 600;">-2.84%  成交3488万</div>
    </div>
  </div>
  <div style="display: grid; grid-template-columns: 1fr 1fr 1fr 1fr; gap: 8px; margin-bottom: 12px; font-size: 12px;">
    <div style="background: rgba(255,255,255,0.04); border-radius: 8px; padding: 8px; text-align: center;"><div style="color: #94a3b8;">今开</div><div style="color: #e2e8f0; font-weight: 600;">9.05</div></div>
    <div style="background: rgba(255,255,255,0.04); border-radius: 8px; padding: 8px; text-align: center;"><div style="color: #94a3b8;">最高</div><div style="color: #10b981; font-weight: 600;">9.45</div></div>
    <div style="background: rgba(255,255,255,0.04); border-radius: 8px; padding: 8px; text-align: center;"><div style="color: #94a3b8;">最低</div><div style="color: #ef4444; font-weight: 600;">8.89(收盘)</div></div>
    <div style="background: rgba(255,255,255,0.04); border-radius: 8px; padding: 8px; text-align: center;"><div style="color: #94a3b8;">换手率</div><div style="color: #e2e8f0; font-weight: 600;">2.46%</div></div>
  </div>
  <div style="font-size: 13px; color: #cbd5e1; line-height: 1.8;">
    <p style="margin: 0 0 8px 0;"><b style="color:#fbbf24">盘面特征：</b>今日早盘冲高至9.45元后震荡回落，最低8.89元以最低价收盘，换手率2.46%，成交仅3488万元，属缩量调整。作为防御性ST重组标的，在4600+股下跌的市场环境下跌幅仅2.84%，相对抗跌属性明显。</p>
    <p style="margin: 0 0 8px 0;"><b style="color:#60a5fa">重组进展：</b>公司2025年末净资产转正至2.06亿元，已向深交所提交撤销退市风险警示申请；控股股东已豁免14亿元债务并捐赠现金4亿元；庭外重组正在推进，金杜+融关律所联合担任协调人；子公司近期连续中标1.59-1.9亿元工程项目，基本面持续改善。</p>
    <p style="margin: 0;"><b style="color:#60a5fa">操作建议：</b>🟡 作为组合的防御性配置继续保留小仓位（建议不超过总仓位10%）。操作策略：<b>①8.5元为关键支撑</b>，不跌破可继续持有博弈摘帽+重组预期；<b>②加仓点</b>：若缩量回调至8.5-8.7元区间企稳，可小仓位补1/3；<b>③减仓点</b>：反弹至9.5-10元区间（前期平台）减仓一半锁定收益；<b>④止损位8.3元</b>，跌破8.3元说明重组预期降温，果断止损出局；<b>⑤关键事件</b>：关注深交所摘帽批复进展，一旦摘帽成功可能出现连续涨停，届时逢高兑现。</p>
  </div>
</div>

<div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.06); border-radius: 14px; padding: 16px;">
  <div style="font-size: 14px; font-weight: 600; color: #94a3b8; margin-bottom: 12px;">📌 其他持仓简要诊断</div>
  <div style="font-size: 13px; color: #cbd5e1; line-height: 1.8;">
    <p style="margin: 0 0 8px 0;"><b style="color:#fb923c">风华高科(000636) 32.59元 -3.41%</b>：MLCC国产龙头，Q3单季净利+470%，今日从35.18元高点回落至32.59元，振幅7.6%。支撑位32元，压力位35元。<b>操作</b>：32元不破持有，跌破31元减仓；反弹34.5元以上减仓1/3；29-30元为加仓点。祥和工业园产能释放+MLCC涨价双重逻辑，中期看好。</p>
    <p style="margin: 0 0 8px 0;"><b style="color:#60a5fa">长电科技(600584) 54.45元 +0.09%</b>：先进封装龙头，今日在半导体板块中表现抗跌。54元为关键支撑，压力位58元。<b>操作</b>：持有为主，52元以下可加仓；反弹至58-60元减仓1/4。长鑫科技产业链核心封测标的，长线逻辑明确。</p>
    <p style="margin: 0;"><b style="color:#a78bfa">华海诚科(688535) 75.87元 +0.25%</b>：环氧塑封料龙头，今日相对抗跌。75元支撑，压力位82元。<b>操作</b>：当前75-78元区间可持有底仓，70元以下加仓至标准仓；反弹至85元以上减仓1/3。</p>
  </div>
</div>

</div>
'''
gen._components.append(Section(title="💼 持仓股深度诊断", content=holdings_html, icon="briefcase"))

gen.add_dragon_tiger_list([
    {"name": "粤芯半导(301660)", "code": "301660", "change": "+7.28% 30.80元", "up": True, "reason": "换手38.27%", "net_buy": "+2.89亿元（5机构全买）", "institutions": 5},
    {"name": "赛腾股份(603283)", "code": "603283", "change": "涨停", "up": True, "reason": "日涨幅偏离7%", "net_buy": "+2.51亿元"},
    {"name": "风语筑(603466)", "code": "603466", "change": "涨停", "up": True, "reason": "AI应用/短剧", "net_buy": "+2.40亿元"},
    {"name": "大东方(600327)", "code": "600327", "change": "+9.95%涨停 7.18元", "up": True, "reason": "振幅17.71%+换手38.62%", "net_buy": "+1509万元（江苏路+拉萨天团）"},
    {"name": "福莱新材(605488)", "code": "605488", "change": "跌停 -9.32%", "up": False, "reason": "日跌幅偏离", "net_buy": "-1.98亿元（机构净卖2.23亿）"},
    {"name": "山金国际(000975)", "code": "000975", "change": "-9%+", "up": False, "reason": "贵金属暴跌", "net_buy": "机构净卖1.34亿"},
])

lhb_html = '''
<div style="background: rgba(30,30,50,0.5); padding: 20px; border: 1px solid rgba(255,255,255,0.08); border-radius: 16px; font-size: 13px; color: #cbd5e1; line-height: 1.8;">
<p style="margin: 0 0 10px 0;"><b style="color:#10b981">🔥 粤芯半导(301660)——机构资金5席抢筹，半导体新贵重点跟踪：</b>
今日收涨7.28%报30.80元，换手率高达38.27%，龙虎榜买入前五席位<b>全部为机构专用席位</b>，合计净买入2.89亿元，是今日龙虎榜机构净买入最多的个股。作为广州本土12寸晶圆厂，粤芯半导是国内模拟芯片代工龙头，近期半导体国产化+成熟制程产能紧张催化明显。5家机构集体抢筹说明机构资金对半导体国产替代主线高度认可。
<b>持续性：★★★★☆</b> 机构大额净买入+高换手，明日高开概率大但30元上方抛压存在；回踩28-29元可关注低吸，止损26元。</p>

<p style="margin: 0 0 10px 0;"><b style="color:#f59e0b">⚡ 赛腾股份(603283)——消费电子+半导体设备双概念，净买入2.51亿：</b>
主营智能装备，覆盖苹果产业链+半导体检测设备，今日涨停登榜，净买入2.51亿元。作为苹果AI手机+半导体设备双重受益标的，近期机构关注度提升。<b>持续性：★★★☆☆</b> 关注明日封单，继续放量则冲击前高，炸板则短线兑现。</p>

<p style="margin: 0 0 10px 0;"><b style="color:#a78bfa">🎬 风语筑+凯撒文化——AI短剧/游戏概念多空博弈：</b>
风语筑涨停获净买入2.40亿元，凯撒文化虽上榜净买入1891万但4机构买+4机构卖分歧明显。AI应用板块整体大跌4%+，上海电影跌停、华策影视跌13.97%，AI应用方向资金分歧极大，机构多空博弈激烈。<b>持续性：★★☆☆☆</b> 板块退潮期高位追涨风险极高，建议观望。</p>

<p style="margin: 0 0 10px 0;"><b style="color:#ef4444">⚠️ 福莱新材+山金国际——机构大幅出逃，警惕继续杀跌：</b>
福莱新材跌停，机构席位净卖出2.23亿元；山金国际跌超9%，机构净卖1.34亿+北向同步卖出。贵金属板块在美元走强+加息预期下进入调整周期，短期规避。<b>持续性：★☆☆☆☆</b> 机构大卖+板块逻辑破坏，反弹即减仓点。</p>

<p style="margin: 0;"><b style="color:#60a5fa">🎯 知名游资动向：</b>北京知春路（国泰海通）买入吉视传媒0.55亿（AI短剧6连板）；作手新一买入东方海洋0.60亿（预制菜）；大东方(600327)获国泰君安江苏路买入6156万+高盛上海买入2394万，游资抱团预制菜/零售防御方向。</p>
</div>
'''
gen._components.append(Section(title="🐉 龙虎榜深度解读", content=lhb_html, icon="award"))

watch_html = '''
<div style="display: flex; flex-direction: column; gap: 14px;">
<div style="background: linear-gradient(135deg, rgba(16,185,129,0.12) 0%, rgba(5,150,105,0.06) 100%); border: 1px solid rgba(16,185,129,0.3); border-radius: 14px; padding: 16px;">
  <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
    <div><span style="font-weight: 700; color: #f1f5f9; font-size: 15px;">🧠 寒武纪(688256)</span>
    <span style="font-size: 11px; padding: 2px 8px; border-radius: 10px; background: rgba(16,185,129,0.2); color: #34d399; margin-left: 8px;">AI算力芯片龙头</span></div>
    <div style="color: #10b981; font-weight: 700;">+8.11% 973.00元</div>
  </div>
  <div style="font-size: 13px; color: #cbd5e1; line-height: 1.7;">
    <b style="color:#34d399">买入逻辑：</b>国产AI算力芯片绝对龙头，今日在大盘大跌中逆势涨8.11%，成交201.72亿元，北向资金成交36.81亿元居沪股通首位。资金从光模块切向算力芯片趋势明确，寒武纪作为国产算力旗帜承接力最强。<br>
    <b style="color:#60a5fa">目标价：</b>第一目标1050元（突破后看1200元）；<b style="color:#ef4444">止损位：</b>跌破900元减仓，跌破850元止损。<br>
    <b style="color:#fbbf24">操作建议：</b>973元不追高，回踩920-940元区间缩量企稳可小仓位（10%）参与，突破1000元整数关后可加仓。
  </div>
</div>
<div style="background: linear-gradient(135deg, rgba(59,130,246,0.12) 0%, rgba(99,102,241,0.06) 100%); border: 1px solid rgba(96,165,250,0.25); border-radius: 14px; padding: 16px;">
  <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
    <div><span style="font-weight: 700; color: #f1f5f9; font-size: 15px;">🔥 燧原科技(688801)</span>
    <span style="font-size: 11px; padding: 2px 8px; border-radius: 10px; background: rgba(96,165,250,0.2); color: #60a5fa; margin-left: 8px;">科创次新+AI芯片</span></div>
    <div style="color: #10b981; font-weight: 700;">+13.13% 558.88元(历史新高)</div>
  </div>
  <div style="font-size: 13px; color: #cbd5e1; line-height: 1.7;">
    <b style="color:#34d399">买入逻辑：</b>今日大涨13.13%创上市新高，是AI算力芯片方向弹性最大标的。昨日龙虎榜机构净买入4.35亿元，今日继续放量大涨，主力做多意愿强烈。作为国内第二梯队AI训练芯片厂商，订单能见度高。<br>
    <b style="color:#60a5fa">目标价：</b>第一目标620元，突破后看700元；<b style="color:#ef4444">止损位：</b>跌破500元止损。<br>
    <b style="color:#fbbf24">操作建议：</b>已创新高不宜追高，等回踩520-540元区间再考虑，适合风险偏好高的投资者小仓位参与。
  </div>
</div>
<div style="background: linear-gradient(135deg, rgba(251,146,60,0.12) 0%, rgba(234,88,12,0.06) 100%); border: 1px solid rgba(251,146,60,0.25); border-radius: 14px; padding: 16px;">
  <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
    <div><span style="font-weight: 700; color: #f1f5f9; font-size: 15px;">🛢️ 东方环宇(603706)</span>
    <span style="font-size: 11px; padding: 2px 8px; border-radius: 10px; background: rgba(251,146,60,0.2); color: #fb923c; margin-left: 8px;">燃气4连板</span></div>
    <div style="color: #10b981; font-weight: 700;">涨停4连板</div>
  </div>
  <div style="font-size: 13px; color: #cbd5e1; line-height: 1.7;">
    <b style="color:#34d399">买入逻辑：</b>燃气板块龙头4连板，洪通燃气涨停助攻，新疆火炬跟涨。冬季用气旺季+油价高位+油气体制改革催化，是当前市场最强防御主线。<br>
    <b style="color:#60a5fa">目标价：</b>若5连板打开空间看至前高；<b style="color:#ef4444">止损位：</b>不板即走。<br>
    <b style="color:#fbbf24">操作建议：</b>4连板位置不建议追高，关注新疆火炬、水发燃气等补涨机会，回调5日线（约-5%）可轻仓参与补涨，严格止损。
  </div>
</div>
<div style="background: linear-gradient(135deg, rgba(239,68,68,0.12) 0%, rgba(220,38,38,0.06) 100%); border: 1px solid rgba(239,68,68,0.3); border-radius: 14px; padding: 16px;">
  <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
    <div><span style="font-weight: 700; color: #f1f5f9; font-size: 15px;">⚠️ 风险规避：中际旭创/新易盛/天孚通信</span>
    <span style="font-size: 11px; padding: 2px 8px; border-radius: 10px; background: rgba(239,68,68,0.2); color: #f87171; margin-left: 8px;">高位兑现</span></div>
    <div style="color: #ef4444; font-weight: 700;">-6.11%/-4.38%/-2.58%</div>
  </div>
  <div style="font-size: 13px; color: #cbd5e1; line-height: 1.7;">
    光模块"三剑客"今日从大涨到大跌，日内振幅均超10%，通信设备板块净流出68亿。<b>短期建议规避</b>，不要急于抄底，等待连续调整3-5日后缩量企稳再考虑。关键观察点：中际旭创能否守住480元支撑（今日最低485元），跌破看450元。
  </div>
</div>
</div>
'''
gen._components.append(Section(title="⭐ 重点关注标的", content=watch_html, icon="star"))

gen.add_tomorrow_prediction([
    {"name": "大盘走势：震荡探底", "direction": "震荡", "confidence": 70,
     "reason": "今日放量冲高回落长上影线明显，短期进入2-3个交易日震荡消化期。下方支撑3620-3630点（10日线），强支撑3600点整数关；上方压力3680-3700点。预计明日低开后有技术性反抽，但反弹力度有限，收小阴小阳概率大。"},
    {"name": "半导体/算力芯片", "direction": "看涨", "confidence": 72,
     "reason": "今日半导体板块逆势净流入23.53亿，寒武纪、燧原科技获资金抢筹，粤芯半导5家机构净买入，资金从光模块切向半导体设备/芯片趋势确立。明日半导体有望继续相对强势，关注国产算力芯片、半导体设备、先进封装分支。"},
    {"name": "光模块/CPO", "direction": "看跌", "confidence": 68,
     "reason": "通信设备板块净流出68亿居首，中际旭创日内振幅11%套牢大量追涨资金，短期情绪降温明显。明日大概率继续调整或弱反弹，反抽就是减仓机会，不建议抄底。"},
    {"name": "军工/燃气/白酒（防御）", "direction": "看涨", "confidence": 65,
     "reason": "资金跷跷板效应下军工、燃气、白酒等防御板块有望继续获得避险资金青睐，但持续性需观察，适合小仓位快进快出，不建议追高连板股。"},
])

plan_text = '''
<div style="display: flex; flex-direction: column; gap: 14px;">
<div style="background: rgba(239,68,68,0.08); border-left: 4px solid #ef4444; padding: 14px 18px; border-radius: 0 12px 12px 0;">
  <div style="font-weight: 700; color: #f87171; margin-bottom: 8px;">🚨 总体仓位建议：从6-7成降至5成</div>
  <div style="font-size: 13px; color: #cbd5e1; line-height: 1.7;">
    今日放量冲高回落+4600+股下跌是明确的短期风险信号，<b>总仓位建议从6-7成降至5成</b>，保留现金等待回踩3600点附近的二次低吸机会。反弹修复大格局未破，但短期节奏放缓，宁可错过不可做错。
  </div>
</div>
<div style="background: rgba(30,30,50,0.5); border: 1px solid rgba(255,255,255,0.08); border-radius: 14px; padding: 16px;">
<div style="font-weight: 700; color: #60a5fa; margin-bottom: 10px; font-size: 14px;">📋 明日具体买卖计划</div>
<table style="width:100%; font-size: 13px; color: #cbd5e1; border-collapse: collapse;">
<thead><tr style="border-bottom: 1px solid rgba(255,255,255,0.1);">
  <th style="text-align:left; padding: 6px; color: #94a3b8;">标的</th>
  <th style="text-align:center; padding: 6px; color: #94a3b8;">方向</th>
  <th style="text-align:center; padding: 6px; color: #94a3b8;">触发价格</th>
  <th style="text-align:center; padding: 6px; color: #94a3b8;">仓位</th>
</tr></thead>
<tbody>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.05);"><td style="padding:8px 6px">英维克002837</td><td style="text-align:center;padding:8px 6px;color:#f87171">反弹减仓</td><td style="text-align:center;padding:8px 6px">42.5-43.5元</td><td style="text-align:center;padding:8px 6px">减1/3</td></tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.05);"><td style="padding:8px 6px">英维克</td><td style="text-align:center;padding:8px 6px;color:#ef4444">止损减仓</td><td style="text-align:center;padding:8px 6px">跌破40元放量</td><td style="text-align:center;padding:8px 6px">减1/2</td></tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.05);"><td style="padding:8px 6px">铜冠铜箔301217</td><td style="text-align:center;padding:8px 6px;color:#fbbf24">高抛减仓</td><td style="text-align:center;padding:8px 6px">74-76元</td><td style="text-align:center;padding:8px 6px">减1/3</td></tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.05);"><td style="padding:8px 6px">铜冠铜箔</td><td style="text-align:center;padding:8px 6px;color:#10b981">低吸加仓</td><td style="text-align:center;padding:8px 6px">65-68元</td><td style="text-align:center;padding:8px 6px">加10-15%</td></tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.05);"><td style="padding:8px 6px">雅克科技002409</td><td style="text-align:center;padding:8px 6px;color:#10b981">加仓</td><td style="text-align:center;padding:8px 6px">85-88元</td><td style="text-align:center;padding:8px 6px">加20%</td></tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.05);"><td style="padding:8px 6px">雅克科技</td><td style="text-align:center;padding:8px 6px;color:#fbbf24">高抛</td><td style="text-align:center;padding:8px 6px">100-105元</td><td style="text-align:center;padding:8px 6px">减1/3机动仓</td></tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.05);"><td style="padding:8px 6px">风华高科000636</td><td style="text-align:center;padding:8px 6px;color:#fbbf24">减仓</td><td style="text-align:center;padding:8px 6px">34.5元以上</td><td style="text-align:center;padding:8px 6px">减1/3</td></tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.05);"><td style="padding:8px 6px">寒武纪(关注)</td><td style="text-align:center;padding:8px 6px;color:#10b981">小仓试错</td><td style="text-align:center;padding:8px 6px">920-940元企稳</td><td style="text-align:center;padding:8px 6px">10%仓位</td></tr>
<tr><td style="padding:8px 6px">粤芯半导(关注)</td><td style="text-align:center;padding:8px 6px;color:#10b981">低吸</td><td style="text-align:center;padding:8px 6px">28-29元</td><td style="text-align:center;padding:8px 6px">5-10%仓位</td></tr>
</tbody></table>
</div>
<div style="background: rgba(59,130,246,0.08); border-left: 4px solid #60a5fa; padding: 14px 18px; border-radius: 0 12px 12px 0;">
  <div style="font-weight: 700; color: #60a5fa; margin-bottom: 8px;">💡 操作纪律</div>
  <div style="font-size: 13px; color: #cbd5e1; line-height: 1.7;">
    ① <b>禁止追高</b>：今日冲高回落的教训深刻，明日所有高开超过2%的标的都不追；<br>
    ② <b>逢高减仓</b>：所有反弹到5日线附近的高位标的（光模块、机器人、游戏）都减仓；<br>
    ③ <b>小仓位试错</b>：新开仓严格控制在10%以内，止损位-5%严格执行；<br>
    ④ <b>现金为王</b>：保留50%现金，等待大盘回踩3600点+缩量企稳后再加仓；<br>
    ⑤ <b>关注夜盘</b>：今晚美股科技股表现是明日A股风向标，若英伟达/AMD大跌则明日继续防御，若反弹则科技股有望企稳。
  </div>
</div>
</div>
'''
gen.add_trading_plan(plan_text)

news_list = [
    {"title": "美国10月CPI超预期，市场上调12月加息概率，美元走强美债收益率飙升",
     "content": "美国通胀数据高于预期，市场上调美联储12月加息预期，美元指数走强，长端美债收益率再创新高，国际金价大跌，贵金属板块承压。对A股成长股估值形成短期压制，但国内货币政策独立性强，影响有限。",
     "time": "今晚", "source": "财联社", "tag": "宏观", "tag_variant": "danger"},
    {"title": "海外AI龙头昨夜大跌，全球AI产业情绪受冲击",
     "content": "海外AI龙头企业晚间大幅下挫，市场担忧相关事件对全球AI产业景气度带来冲击，直接传导至A股AI硬件板块午后跳水，光模块/CPO/PCB等算力上游从涨转跌。",
     "time": "昨夜", "source": "新浪财经", "tag": "外围", "tag_variant": "warning"},
    {"title": "粤芯半导5家机构席位净买入2.89亿，半导体国产替代逻辑获机构认可",
     "content": "今日龙虎榜数据显示，次新股粤芯半导买入前五席位全部为机构专用，合计净买入2.89亿元，机构资金对半导体国产替代主线认可度提升。",
     "time": "盘后", "source": "东方财富", "tag": "资金", "tag_variant": "success"},
    {"title": "中际旭创成交336亿全市场第一，光模块资金高位激烈换手",
     "content": "中际旭创全天成交336.22亿元居A股首位，日内振幅达11%，新易盛256亿、天孚通信98亿。光模块板块全天净流出68亿，高位筹码兑现意愿强烈。",
     "time": "盘后", "source": "同花顺", "tag": "提示", "tag_variant": "warning"},
    {"title": "铜冠铜箔拟投1.54亿元实施高端铜箔技改项目，HVLP铜箔加速国产替代",
     "content": "公司董事会已审议通过部分生产线技术改造项目，加码高端PCB铜箔产能。前三季度净利润3.39亿元同比+439.75%，Q3单季+345%，高端铜箔加工费上行周期确立。",
     "time": "近期", "source": "公司公告", "tag": "持仓", "tag_variant": "primary"},
]
gen.add_evening_news(news_list)

gen.add_risk_warning([
    "美国通胀超预期+加息预期升温，海外流动性收紧可能继续压制A股成长股估值",
    "今日放量冲高回落显示获利盘兑现压力大，短期2-3个交易日可能继续震荡调整",
    "光模块/CPO等高位赛道资金流出明显，反抽就是减仓机会，切忌盲目抄底",
    "贵金属板块受美元走强+金价大跌冲击，短期规避为上",
    "海外AI龙头波动可能继续影响A股科技股情绪，注意控制仓位在5成以内",
    "ST股、小市值题材股流动性风险加大，避免追高连板妖股",
])

print("=" * 60)
print("正在发布盘后速递...")
result = gen.publish(
    title="盘后速递",
    filename="20261112_盘后速递.html",
    excerpt="11月12日A股冲高回落，沪指跌0.67%，成交1.95万亿放量2571亿，4635只个股下跌；半导体逆势净流入23.53亿，光模块净流出68亿，英维克-5.4%/铜冠铜箔-2.4%/雅克科技+1.19%抗跌，明日关注3600点支撑。",
    auto_deploy=False,
)
print("发布结果:", result)
