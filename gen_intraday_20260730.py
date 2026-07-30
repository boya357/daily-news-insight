#!/usr/bin/env python3
"""
2026年7月30日 盘中快报生成脚本
使用V3.0 IntradayGenerator生成
"""
import sys
import os

# 设置工作目录
WORK_DIR = "/root/daily-news-insight"
sys.path.insert(0, os.path.join(WORK_DIR, "v3"))
os.chdir(WORK_DIR)

from generators.intraday import IntradayGenerator
from generators.list_page import ListPageGenerator

# ========== 数据准备 ==========
date_str = "2026年7月30日"

# 市场概览数据（午盘）
indices = [
    {"name": "上证指数", "value": "3,784.55", "change": "-1.15%", "up": False, "icon": "trending_down"},
    {"name": "深证成指", "value": "13,141.22", "change": "-3.79%", "up": False, "icon": "trending_down"},
    {"name": "创业板指", "value": "3,179.58", "change": "-5.89%", "up": False, "icon": "trending_down"},
    {"name": "科创50", "value": "1,572.25", "change": "-6.34%", "up": False, "icon": "alert-triangle"},
]
market_status = "暴跌"

# 午盘焦点
focus_point = "A股早盘低开低走，四大指数集体暴跌，科创50重挫超6%创阶段新低，创业板指跌近6%跌破3200点，两市超3400只个股下跌。半日成交1.45万亿，较昨日缩量264亿，但仍处历史高位。科技成长赛道遭遇全面抛售：CPO光模块三剑客集体暴跌13-16%，半导体/存储/HBM全线崩塌，PCB/算力硬件深度回调。防御板块逆势走强：白酒/食品饮料领涨，银行护盘，贵金属反弹。道指隔夜暴跌1100点创年内最大跌幅，全球AI链估值消化进入加速阶段。"

# 市场热点
hot_topics = [
    {
        "tag": "白酒消费",
        "title": "大消费逆势爆发，白酒板块领涨全市场",
        "content": "白酒/食品饮料成为今日唯一亮色，舍得酒业、金徽酒涨停，贵州茅台涨2.85%，酒ETF涨3.9%。催化逻辑：①科技股暴跌引发资金避险需求，消费板块估值处于历史低位；②美联储议息落地后市场风格切换，资金从高位成长向低位防御迁徙；③暑期消费旺季+中秋国庆备货预期催化；④中报业绩确定性强，白酒龙头业绩稳健。",
        "hot": True,
        "stocks": ["舍得酒业", "金徽酒", "贵州茅台", "一鸣食品"]
    },
    {
        "tag": "银行护盘",
        "title": "银行板块逆势走强，大行获资金避险流入",
        "content": "银行板块涨1.58%，工商银行涨超2%，银行ETF涨1.83%。催化：①市场暴跌背景下银行板块防御属性凸显，高股息低估值吸引避险资金；②美联储按兵不动，国内货币政策宽松预期支撑；③中报季银行业绩稳健，坏账风险可控。",
        "hot": True,
        "stocks": ["工商银行", "招商银行", "建设银行"]
    },
    {
        "tag": "贵金属",
        "title": "贵金属震荡反弹，避险情绪升温",
        "content": "贵金属板块逆势上涨，招金黄金涨停，赤峰黄金、西部黄金跟涨。催化：①全球股市暴跌引发避险情绪升温；②美元指数走弱+地缘政治风险支撑金价；③美联储降息预期下贵金属中长期配置价值凸显。",
        "hot": False,
        "stocks": ["招金黄金", "赤峰黄金", "西部黄金"]
    },
    {
        "tag": "AI应用/教育",
        "title": "AI应用端反复活跃，传智教育4连板",
        "content": "AI应用方向相对抗跌，传智教育走出4连板，普联软件、恒锋信息20CM涨停。催化：①字节跳动组织调整，飞书并入豆包+火山引擎，AI资源集中化；②AI应用端中报业绩预喜，教育+AI赛道景气度高；③应用端估值相对硬件更合理，资金从硬件向应用轮动。",
        "hot": False,
        "stocks": ["传智教育", "普联软件", "恒锋信息"]
    },
]

# 领跌板块
decline_sectors = [
    {"name": "CPO/光模块", "change": "-12%+", "reason": "中际旭创港股IPO首日破发（定价980港元较A股折价约21%）+1.6T光模块降价传闻，'易中天'三剑客集体暴跌：新易盛-16.43%、中际旭创-15.77%、天孚通信-13.5%"},
    {"name": "半导体/存储芯片", "change": "-8%+", "reason": "道指隔夜暴跌1100点创年内最大跌幅，全球科技股估值消化加速，科创半导体ETF跌8.88%，雅克科技跌停、长鑫科技大跌、中科飞测/华虹宏力重挫"},
    {"name": "算力硬件/PCB", "change": "-7%+", "reason": "AI硬件链估值泡沫破裂，从光模块向PCB/服务器/液冷传导，生益电子、沪电股份等大幅下挫，通信ETF跌近10%"},
]

# 持仓股跟踪（午盘数据）
holdings = [
    {
        "name": "英维克",
        "code": "002837",
        "price": "47.15",
        "change": "-7.52%",
        "up": False,
        "comment": "液冷龙头随算力硬件板块大幅下挫，午盘报47.15元跌约7.5%，主力资金净流出3.2亿。AI算力硬件链整体遭遇抛售潮，CPO/光模块暴跌传导至液冷/服务器等算力基础设施。技术形态已严重破位，从6月高点回撤超40%，50元整数关口已失守，短期趋势走坏。下方支撑看45元附近，破位则下行空间进一步打开。"
    },
    {
        "name": "铜冠铜箔",
        "code": "301217",
        "price": "78.50",
        "change": "-12.23%",
        "up": False,
        "comment": "存储铜箔龙头深度下挫，10:34分创60日新低报80.14元，午盘继续下探至78.5元附近跌超12%。半导体/存储产业链全线暴跌，PCB/覆铜板同步大跌拖累铜箔板块。从高点累计回调已超50%，技术形态完全破位。铜箔逻辑不变但β风险极度放大，76元跌停价是关键支撑，跌破后短期无底部可言。"
    },
    {
        "name": "雅克科技",
        "code": "002409",
        "price": "136.97",
        "change": "-9.99%",
        "up": False,
        "comment": "半导体材料龙头盘中跌停，10:41分打开跌停报136.97元，成交39.19亿换手率8.64%。存储芯片/HBM板块全线崩塌，全球科技股估值消化加速。HBM前驱体龙头逻辑不变但β杀估值压力巨大，跌停打开说明有资金尝试抄底，但抛压依然沉重。连续第四日大跌，从高点累计跌幅超45%，短期不宜盲目抄底。"
    },
    {
        "name": "*ST建艺",
        "code": "002789",
        "price": "8.50",
        "change": "-5.24%",
        "up": False,
        "comment": "ST股今日随大盘下跌，午盘报8.5元附近跌约5%，逼近前期低点。ST板块整体受市场情绪拖累，但个股逻辑独立。退市风险敞口必须关闭，坚决清仓离场纪律不变，不存侥幸。新增诉讼仲裁2419万元占净资产11.75%，基本面持续恶化。"
    },
]

# 午盘操作策略
trading_strategy = """
<strong>【核心判断】</strong>今日早盘市场全线暴跌，科创50重挫6.34%创阶段新低，创业板指跌近6%，四大指数同步破位。本质是全球AI链估值消化进入加速阶段+国内科技股抱团瓦解的共振下跌，不是普通回调而是主跌浪。昨日反抽只活了一天即被"断头铡刀"否定。<br>
<strong>关键数据：</strong>半日成交1.45万亿（缩量264亿），3400+个股下跌，283只跌超9%，恐慌情绪蔓延。

<strong>【持仓操作——严格执行止损纪律】</strong>
① <strong>英维克(002837)</strong>：跌约7.5%跌破50元，<strong>50元已破位，无条件止损减仓</strong>，反弹至48-49元继续减。液冷逻辑中长期不变但β风险巨大，不抄底、不补仓。
② <strong>铜冠铜箔(301217)</strong>：跌超12%创60日新低，<strong>跌破80元已确认，止损离场</strong>。存储铜箔龙头但β杀估值压力下不扛单，76元跌停价附近若不能企稳则清仓。
③ <strong>雅克科技(002409)</strong>：盘中跌停后短暂打开，<strong>跌停打开≠见底，不抄底！</strong>连续第四日大跌，HBM前驱体龙头不变但β风险释放中，等放量企稳+板块止跌再评估。
④ <strong>*ST建艺(002789)</strong>：随大盘下跌，<strong>退市风险敞口必须关闭，坚决清仓离场</strong>，不存幻想。

<strong>【整体策略】</strong>
整体仓位控制在2成以内，现金为王。科技主跌浪中，<strong>不抄底、不补仓、扛单=找死</strong>。重点观察三个信号：①沪指能否守住3780点（昨日低点3782）；②科创50能否在1550点附近止跌；③跌停家数是否减少。午后若科技继续杀跌，沪指有下探3750点风险。耐心等待企稳信号，右侧加仓永远比左侧抄底安全。
"""

# 风险提示
risks = [
    "全球AI链估值消化进入加速阶段，道指隔夜暴跌1100点创年内最大跌幅，海外科技股继续暴跌传导风险",
    "半导体/光模块/算力硬件全线崩塌，科技股抱团瓦解过程中流动性风险加剧",
    "科创50创阶段新低，四大指数同步破位，技术形态恶化",
    "中报业绩暴雷风险，高位科技股补跌压力持续",
    "美联储7月议息虽落地但市场解读偏鹰，长端利率走高压制成长股估值"
]

# 市场逻辑总结
summary = """
今日市场全线暴跌，核心逻辑是"全球科技股估值消化加速+国内抱团瓦解"的双杀：
<strong>1. 海外暴跌传导</strong>：道指隔夜暴跌1153点（-2.19%）创年内最大跌幅，纳指进入技术性调整，全球AI链估值消化进入加速阶段；
<strong>2. CPO光模块领跌</strong>：中际旭创港股IPO首日破发（折价21%）+1.6T降价传闻，"易中天"三剑客集体暴跌13-16%，成为杀跌主力军；
<strong>3. 科技链全面崩塌</strong>：从光模块向半导体/存储/PCB/算力硬件/液冷全面传导，科技成长赛道无差别抛售；
<strong>4. 资金避险迁徙</strong>：白酒/食品饮料/银行/贵金属逆势走强，资金从高位成长向低位防御大幅迁徙；
<strong>5. 反抽一日游</strong>：昨日科创50反抽确认后今日即被"断头铡刀"否定，主跌浪特征明显。

<strong>操作纪律：</strong>主跌浪中严格执行止损，现金为王，不抄底不补仓，等待右侧企稳信号。
"""

# ========== 生成报告 ==========
gen = IntradayGenerator(date_str=date_str, subtitle=f"{date_str} 星期四 · 午盘速递")

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
output_path = os.path.join(WORK_DIR, "docs/intraday/20260730_盘中快报.html")
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
    title="20260730 盘中快报",
    date="2026-07-30",
    url="20260730_盘中快报.html",
    excerpt="科创50重挫6.34%创阶段新低，CPO光模块三剑客集体暴跌13-16%，科技链全面崩塌，白酒银行逆势护盘",
    tag="午盘速递"
)
print(f"列表页更新: {'成功' if success else '失败'}")

# ========== 更新latest.html（最新报告副本） ==========
import shutil
latest_path = os.path.join(WORK_DIR, "docs/intraday/latest.html")
shutil.copy(output_path, latest_path)
print(f"latest.html已更新: {os.path.getsize(latest_path)} bytes")
