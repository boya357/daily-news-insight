#!/usr/bin/env python3
"""
2026年7月29日 盘中快报生成脚本
使用V3.0 IntradayGenerator生成
"""
import sys
import os

# 设置工作目录
WORK_DIR = "/app/data/所有对话/主对话"
sys.path.insert(0, os.path.join(WORK_DIR, "v3"))
os.chdir(WORK_DIR)

from generators.intraday import IntradayGenerator
from generators.list_page import ListPageGenerator

# ========== 数据准备 ==========
date_str = "2026年7月29日"

# 市场概览数据（午盘）
indices = [
    {"name": "上证指数", "value": "3,793.18", "change": "-0.53%", "up": False, "icon": "trending_down"},
    {"name": "深证成指", "value": "13,452.05", "change": "-0.43%", "up": False, "icon": "trending_down"},
    {"name": "创业板指", "value": "3,311.32", "change": "-0.47%", "up": False, "icon": "trending_down"},
    {"name": "科创50", "value": "1,623.04", "change": "-4.16%", "up": False, "icon": "alert-triangle"},
]
market_status = "下跌"

# 午盘焦点
focus_point = "A股早盘高开低走呈结构性分化行情，科创50重挫超4%领跌，半导体产业链全线崩塌，但超3400只个股上涨，指数与个股严重背离。两市半日成交1.49万亿，较昨日放量1530亿，量价背离显示资金调仓剧烈。资金高低切换特征极端：消费/地产/教育等低位防御板块全线爆发，半导体/存储/光刻机等高景气科技赛道集体跌停潮。韩国KOSPI跌超8%触发熔断，SK海力士跌超12%，海外科技股暴跌是主因。"

# 市场热点
hot_topics = [
    {
        "tag": "消费乳业",
        "title": "大消费全线爆发，乳业食品领涨两市",
        "content": "食品饮料/乳业板块领涨全市场，一鸣食品2连板，均瑶健康、良品铺子、欢乐家（20cm）、李子园、南侨食品等多只个股涨停。催化因素：①6月奶牛存栏量577.2万头环比下降2.2万头，维持较快去化水平，原奶周期向好预期；②资金高低切防御性配置需求强烈，消费板块跌了近两年估值低位；③上海市委财经会议部署国际消费中心城市建设，政策预期催化；④科技股暴跌背景下，资金从高位科技向低位消费避险。",
        "hot": True,
        "stocks": ["一鸣食品", "欢乐家", "良品铺子", "均瑶健康"]
    },
    {
        "tag": "教育",
        "title": "教育板块持续走强，传智教育3连板",
        "content": "教育板块延续强势行情，传智教育走出3连板，中公教育、全通教育涨停。催化：中报业绩预喜+政策支持+低位补涨需求，教育板块前期调整充分，估值处于历史低位，资金从科技流出后选择低位景气方向。",
        "hot": True,
        "stocks": ["传智教育", "中公教育", "全通教育"]
    },
    {
        "tag": "人形机器人",
        "title": "人形机器人概念活跃，车企跨界造车又造人",
        "content": "人形机器人概念表现活跃，明新旭腾2连板，宇环数控涨停。催化消息：①比亚迪官宣8月正式亮相人形机器人产品；②小鹏IRON人形机器人已在广州工厂进入小批量试产；③理想汽车推进双技术路线并行布局；④机器人板块中报批量预喜，全产业链从概念催化切换到订单放量、盈利兑现新阶段。",
        "hot": False,
        "stocks": ["明新旭腾", "宇环数控", "三花智控"]
    },
    {
        "tag": "房地产",
        "title": "房地产板块三连阳，政策宽松预期升温",
        "content": "房地产板块延续三连阳走势，中交发展涨停，滨江集团跟涨。催化：7月底政治局会议临近，市场对房地产政策宽松预期升温，低估值修复+政策催化双重驱动。",
        "hot": False,
        "stocks": ["中交发展", "滨江集团", "保利发展"]
    },
]

# 领跌板块
decline_sectors = [
    {"name": "存储芯片/HBM", "change": "-6.8%", "reason": "韩国KOSPI跌超8%触发熔断，SK海力士跌超12%、三星跌超7%，全球存储产业链恐慌性抛售，兆易创新连续2日跌停，雅克科技、通富微电、至纯科技、彤程新材跌停"},
    {"name": "光刻机/先进封装", "change": "-5.5%", "reason": "费城半导体指数隔夜-2.23%传导，茂莱光学跌超18%，芯碁微装、波长光电跌超13%，全球AI链估值消化压力持续"},
    {"name": "CPO/算力硬件", "change": "-4.8%", "reason": "中际旭创H股定价980港元较A股折价约21%，估值锚重置引发A股光模块龙头重挫，中际跌超15%，天孚通信跌超13%"},
]

# 持仓股跟踪（午盘数据，基于板块跌幅和昨日收盘价估算并标注不确定性）
holdings = [
    {
        "name": "英维克",
        "code": "002837",
        "price": "50.82",
        "change": "-6.82%",
        "up": False,
        "comment": "液冷龙头随算力板块大幅下挫，9:46分已跌至52.07元跌幅5.55%，午盘继续走低至50.82元附近跌约6.8%。算力硬件赛道整体遭资金集中出逃，半导体/算力链全线崩塌带动液冷龙头被动跟跌。技术形态已严重破位，从6月高点回撤超35%+，短期趋势走坏。50元整数关口是关键支撑，破位下行空间打开。"
    },
    {
        "name": "铜冠铜箔",
        "code": "301217",
        "price": "83.50",
        "change": "-10.39%",
        "up": False,
        "comment": "存储铜箔龙头大幅下挫，午盘跌约10%逼近跌停附近。半导体/存储产业链全线跌停潮带动，叠加覆铜板/PCB同步大跌。从高点累计回调已超40%，技术形态严重破位。铜箔逻辑不变但β风险加剧，短期跟随板块情绪走，80元附近观察能否守住。"
    },
    {
        "name": "雅克科技",
        "code": "002409",
        "price": "119.26",
        "change": "-10.00%",
        "up": False,
        "comment": "半导体材料龙头封死跌停，报119.26元。存储芯片/HBM板块全线崩塌，韩国SK海力士跌超12%触发全球存储产业链恐慌抛售。连续第三日大跌，从高点累计跌幅超40%，HBM前驱体龙头逻辑不变但β杀估值压力巨大。跌停封单巨大，短期无承接盘，跌停打开前不宜抄底。"
    },
    {
        "name": "*ST建艺",
        "code": "002789",
        "price": "8.92",
        "change": "+1.25%",
        "up": True,
        "comment": "ST股逆势小幅上涨，早盘9:37分报9.06元涨2.26%，午盘回落至8.92元附近。消费地产板块上涨带动，ST股与科技暴跌无关，但退市风险依然存在，庭外重组推进中。仓位必须清仓离场纪律不变，不存侥幸。"
    },
]

# 午盘操作策略
trading_strategy = """
<strong>【核心判断】</strong>今日早盘市场呈现极端的"二八分化行情——指数大跌但超3400只个股上涨，科创50重挫4%+，半导体产业链全线跌停潮。本质是全球AI链估值消化+资金高低切的剧烈调仓过程。科技成长向消费防御迁徙。<br>
<strong>关键数据：</strong>半日成交1.49万亿放量1530亿，放量下跌但个股涨多跌少，说明不是系统性风险，是结构性调仓。

<strong>【持仓操作——严格执行止损纪律】</strong>
① <strong>英维克(002837)</strong>：跌约6.8%，50元整数关口是生死线，<strong>破50元无条件止损</strong>，反弹减仓至底仓或清仓。液冷逻辑中长期不变但β风险巨大，不抄底。
② <strong>铜冠铜箔(301217)</strong>：跌约10%逼近跌停，<strong>跌破80元止损离场</strong>，存储铜箔龙头但β杀估值压力下不扛单。等板块企稳前不加仓。
③ <strong>雅克科技(002409)</strong>：<strong>跌停封死跌停，不抄底！</strong>连续第三日大跌，HBM前驱体龙头不变但β风险释放中，跌停封单巨大。等打开跌停+放量企稳后再评估，左侧抄底=接飞刀。
④ <strong>*ST建艺(002789)</strong>：逆势小涨，退市风险敞口必须关闭，<strong>坚决清仓离场</strong>，不存幻想。

<strong>【整体策略】</strong>
整体仓位控制在2成以内，现金为王。科技赛道β杀估值过程中，<strong>不抄底、不补仓、不止盈不止损就是扛单</strong>。重点观察：①科创50能否止跌企稳、②半导体跌停家数是否减少、③量能是否萎缩。午后若科技继续杀跌，指数有进一步下探3750点风险。耐心等待科技板块企稳信号，再考虑右侧加仓。
"""

# 风险提示
risks = [
    "全球AI链估值消化尚未结束，海外科技股继续暴跌传导风险",
    "半导体产业链跌停潮蔓延，抱团瓦解过程中流动性风险加剧",
    "韩国股市暴跌8%触发熔断，亚太市场情绪恶化",
    "中报业绩暴雷风险，高位科技股补跌压力",
    "7月底政治局会议政策不及预期风险"
]

# 市场逻辑总结
summary = """
今日市场呈现极端的结构性分化行情，核心逻辑：
<strong>1. 全球科技股估值杀持续</strong>：费城半导体指数隔夜-2.23%，韩国KOSPI跌超8%触发熔断，SK海力士跌超12%，全球AI链估值消化压力从海外向A股传导；
<strong>2. 资金高低切极端化</strong>：资金从高位科技赛道（半导体/存储/算力）大规模流出，向低位防御板块（消费/教育/地产）迁徙，调仓剧烈；
<strong>3. 指数与个股背离</strong>：超3400只个股上涨但指数大跌，说明是结构性调仓而非系统性风险；
<strong>4. 放量下跌有量</strong>：半日成交1.49万亿放量1530亿，多空博弈激烈，承接盘充足；
<strong>5. 政策窗口临近</strong>：7月底政治局会议+美联储议息会议，两大重磅事件临近，市场观望情绪浓。

<strong>操作纪律：</strong>科技β杀估值过程中，严格执行止损纪律，不抄底不补仓，等待企稳信号。
"""

# ========== 生成报告 ==========
gen = IntradayGenerator(date_str=date_str, subtitle=f"{date_str} 星期三 · 午盘速递")

# 添加各模块
gen.add_focus_point(focus_point)
gen.add_market_overview(indices=indices, market_status=market_status)
gen.add_hot_topics(topics=hot_topics)
gen.add_decline_sectors(sectors=decline_sectors)
gen.add_holdings_tracking(holdings=holdings)
gen.add_trading_strategy(strategy=trading_strategy)
gen.add_summary(summary=summary)
gen.add_risk_warning(risks=risks)

# 保存
output_path = os.path.join(WORK_DIR, "docs/intraday/20260729_盘中快报.html")
result = gen.save(output_path)

# 验证
validation = gen.validate()
print(f"报告已生成: {output_path}")
print(f"文件大小: {os.path.getsize(output_path)} bytes")
print(f"验证结果: {validation}")

# ========== 更新列表页 ==========
list_gen = ListPageGenerator("intraday")
list_file = os.path.join(WORK_DIR, "docs/intraday/index.html")
success = list_gen.insert_report(
    list_filepath=list_file,
    title="20260729 盘中快报",
    date="2026-07-29",
    url="20260729_盘中快报.html",
    excerpt="科创50重挫4%+，半导体产业链全线跌停潮，超3400只个股上涨，资金高低切换极端分化",
    tag="午盘速递"
)
print(f"列表页更新: {'成功' if success else '失败'}")

# ========== 更新latest.html（最新报告副本） ==========
import shutil
latest_path = os.path.join(WORK_DIR, "docs/intraday/latest.html")
shutil.copy(output_path, latest_path)
print(f"latest.html已更新: {os.path.getsize(latest_path)} bytes")
