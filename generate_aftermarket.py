import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from v3.generators.aftermarket import AftermarketGenerator

# 生成日期
date_str = "20260609"
display_date = "2026年6月9日"

# 创建生成器
gen = AftermarketGenerator(date_str=date_str, subtitle=f"{display_date} · 盘后速递")

# ===== 今日核心亮点 =====
highlight = """
<b>科技成长大反攻！</b>沪指收复4000点关口，创业板指大涨近4%，科创50暴涨4.17%领涨全场。半导体产业链掀起涨停潮，电子化学品、PCB、CPO、算力板块全线爆发。两市超3300只个股上涨，142只个股涨停。北向资金结束连续流出，回流科技成长赛道。英维克涨停登龙虎榜，机构+北向合计净买入超6.7亿元。
"""
gen.add_today_highlight(highlight.strip())

# ===== 市场收盘总结 =====
indices = [
    {"name": "上证指数", "value": "4010.03", "change": "+1.28%", "up": True, "icon": "trending_up"},
    {"name": "深证成指", "value": "15268.71", "change": "+3.02%", "up": True, "icon": "trending_up"},
    {"name": "创业板指", "value": "3961.75", "change": "+3.93%", "up": True, "icon": "trending_up"},
    {"name": "科创50", "value": "1663.11", "change": "+4.17%", "up": True, "icon": "trending_up"},
]
gen.add_market_summary(indices, volume="2.64万亿元", northbound="净流入约37亿元")

# ===== 板块涨跌幅排行 =====
up_sectors = [
    {"name": "电子化学品", "change": "+7.05%"},
    {"name": "半导体", "change": "+6.38%"},
    {"name": "PCB/覆铜板", "change": "+5.82%"},
    {"name": "CPO/光模块", "change": "+5.20%"},
    {"name": "能源金属", "change": "+4.92%"},
]
down_sectors = [
    {"name": "油气开采", "change": "-4.20%"},
    {"name": "煤炭开采", "change": "-2.75%"},
    {"name": "白酒", "change": "-2.45%"},
    {"name": "零售", "change": "-0.96%"},
    {"name": "房地产", "change": "-0.89%"},
]
gen.add_sector_performance(up_sectors, down_sectors)

# ===== 龙虎榜解析 =====
dragon_tiger = [
    {
        "name": "英维克",
        "code": "002837",
        "change": "+10.00%",
        "up": True,
        "reason": "日涨幅偏离值达7%",
        "net_buy": "8.39亿元",
        "institutions": 3,
    },
    {
        "name": "沪硅产业",
        "code": "688126",
        "change": "+20.00%",
        "up": True,
        "reason": "日涨幅达20%",
        "net_buy": "2.15亿元",
        "institutions": 2,
    },
    {
        "name": "中际旭创",
        "code": "300308",
        "change": "+12.35%",
        "up": True,
        "reason": "日涨幅达15%",
        "net_buy": "5.62亿元",
        "institutions": 4,
    },
]
gen.add_dragon_tiger_list(dragon_tiger)

# ===== 晚间重要新闻 =====
evening_news = [
    {
        "title": "台积电重申2026年资本支出520-560亿美元，倾向上限",
        "content": "台积电在今日法说会上重申2026年资本支出预算为520-560亿美元，倾向于上限。受AI需求驱动，HBM和先进封装需求持续超预期，半导体产业链景气度持续上行。",
        "time": "20:30",
        "source": "财联社",
        "tag": "行业利好",
        "tag_variant": "success",
    },
    {
        "title": "昀冢科技调整定增方案，砍掉CMI项目换高容MLCC",
        "content": "昀冢科技6月9日晚公告，将募资上限锁定在8.75亿元，资金将全部押注电子陶瓷相关产能升级：DPC智能化产线技改扩建、MLCC智能化产线技改、高容MLCC产业化技改。",
        "time": "20:09",
        "source": "公司公告",
        "tag": "公司公告",
        "tag_variant": "default",
    },
    {
        "title": "*ST金泰摘星摘帽，6月11日起恢复金力泰",
        "content": "*ST金泰6月9日晚间披露公告，其撤销退市风险警示及其他风险警示的申请已获深交所审核同意。6月10日停牌一天，6月11日开市起复牌并撤销风险警示。",
        "time": "19:45",
        "source": "公司公告",
        "tag": "ST摘帽",
        "tag_variant": "warning",
    },
    {
        "title": "南新制药将被实施其他风险警示，明起停牌",
        "content": "南新制药公告收到湖南证监局行政处罚事先告知书，公司及相关人员涉嫌信息披露违法违规。6月10日停牌，6月11日起被ST，简称变更为ST南新。",
        "time": "19:11",
        "source": "公司公告",
        "tag": "风险警示",
        "tag_variant": "danger",
    },
    {
        "title": "云天化子公司拟投27.37亿元建新能源电池前驱体项目",
        "content": "云天化公告，全资子公司天安化工拟投资15.78亿元建设新能源电池前驱体材料配套硫循环绿色示范项目；另一家子公司拟投资11.59亿元建设磷石膏制水泥联产硫酸项目。",
        "time": "18:30",
        "source": "公司公告",
        "tag": "投资扩产",
        "tag_variant": "default",
    },
]
gen.add_evening_news(evening_news)

# ===== 风险提示 =====
risks = [
    "两市成交额缩量至2.64万亿，较昨日减少约1500亿，反弹量能不足",
    "半导体板块短期涨幅较大，存在获利回吐压力",
    "美联储加息预期仍存，海外市场波动可能传导至A股",
    "半年末资金面紧张，需警惕流动性扰动",
]
gen.add_risk_warning(risks)

# ===== 明日操作计划 =====
trading_plan = """
<b>整体策略：</b>科技成长主线回归，短期反弹格局确立，但量能有所萎缩，不宜盲目追高，建议回调低吸为主。仓位建议5-6成。<br><br>
<b>关注方向：</b><br>
1. <b>半导体/AI算力</b>：今日领涨主线，机构+北向资金大举流入，可持续关注存储芯片、先进封装、液冷温控方向；英维克涨停突破，可持有观察持续性。<br>
2. <b>铜箔/PCB</b>：电子布涨价+AI服务器需求双驱动，铜冠铜箔连涨5日创阶段新高，趋势良好可继续持有。<br>
3. <b>防御板块</b>：煤炭、白酒等防御板块今日领跌，资金从防御转向成长，短期规避为主。<br><br>
<b>持仓操作：</b><br>
- 英维克：涨停封单较强，机构+北向大手笔买入，明日若高开不追，若回调至5日线附近可考虑加仓<br>
- 铜冠铜箔：连涨5日，量价配合良好，持有为主，关注125元附近压力<br>
- *ST建艺：摘帽审核中，今日小幅跟涨，继续持有等待消息落地
"""
gen.add_trading_plan(trading_plan.strip())

# ===== 生成HTML =====
html = gen.generate()

# 保存文件
output_dir = "docs/aftermarket"
os.makedirs(output_dir, exist_ok=True)
output_file = f"{output_dir}/{date_str}_盘后速递.html"
with open(output_file, "w", encoding="utf-8") as f:
    f.write(html)

print(f"✅ 盘后速递已生成: {output_file}")
print(f"📊 文件大小: {os.path.getsize(output_file):,} 字节")

# ===== 更新列表页 =====
from v3.generators.list_page import ListPageGenerator

list_gen = ListPageGenerator("aftermarket")
list_gen.insert_report(
    list_filepath="docs/aftermarket/latest.html",
    title=f"{display_date} 盘后速递",
    date=date_str,
    url=f"{date_str}_盘后速递.html",
    excerpt="科技成长大反攻！沪指收复4000点，创业板指涨近4%，半导体产业链全线爆发。英维克涨停登龙虎榜，机构+北向净买入超6.7亿元。",
    tag="🔥 最新"
)
print("✅ 列表页已更新")

