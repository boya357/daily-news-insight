"""
2026年6月8日 每日新闻洞察生成脚本
使用V3.0生成器
"""
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'v3'))

from generators.daily import DailyReportGenerator

# 创建生成器
generator = DailyReportGenerator(
    date_str="2026年6月8日",
    weekday="星期一",
    subtitle="2026年6月8日 星期一 · 龙空龙策略专用"
)

# 1. 今日焦点
generator.add_focus_point(
    "美股遭遇黑色星期五，纳指暴跌4.18%创一年多最大跌幅，AI科技股集体重挫；"
    "非农数据超预期引爆加息担忧，费城半导体指数暴跌10.26%；"
    "A股今日承压，高位科技股补跌风险加剧，建议控制仓位避险为主。"
)

# 2. 隔夜全球市场
indices = [
    {"name": "道琼斯", "value": "50,866.78", "change": "-1.35%", "up": False, "icon": "trending_down"},
    {"name": "纳斯达克", "value": "25,709.43", "change": "-4.18%", "up": False, "icon": "trending_down"},
    {"name": "标普500", "value": "7,383.74", "change": "-2.64%", "up": False, "icon": "trending_down"},
    {"name": "费城半导体", "value": "--", "change": "-10.26%", "up": False, "icon": "trending_down"},
]

key_events = [
    {
        "tag": "重磅",
        "title": "美国5月非农大超预期，降息预期彻底落空",
        "content": "美国5月非农就业新增17.2万人，远超市场预期的8.5万人，失业率稳定在4.3%。利率互换市场定价美联储12月加息25个基点，10月加息概率升至60%。美债收益率飙升，全球风险资产承压。"
    },
    {
        "tag": "暴跌",
        "title": "AI科技股集体重挫，英伟达单日蒸发超3000亿美元",
        "content": "英伟达跌6.20%，美光科技跌13.25%，AMD跌10.86%，英特尔跌11.28%，博通跌7.92%。费城半导体指数暴跌10.26%，创近年最大单日跌幅。恐慌指数VIX飙升近40%，市场情绪急剧恶化。"
    },
    {
        "tag": "行业",
        "title": "英伟达与SK集团战略合作，锁定AI存储产能",
        "content": "6月8日英伟达CEO黄仁勋与SK集团董事长崔泰源官宣深度战略合作，聚焦HBM优先供应、共建AI超级工厂、研发低功耗DRAM三大方向。存储超级周期逻辑进一步强化，HBM供需缺口持续扩大。"
    },
]

generator.add_overseas_market(indices=indices, key_events=key_events)

# 3. 市场情绪
generator.add_market_sentiment(
    sentiment_score=35,  # 恐慌情绪
    risk_level="高",
    volume_ratio=1.2
)

# 4. 重要新闻汇总
important_news = [
    {
        "tag": "宏观",
        "importance": "high",
        "title": "美国非农数据爆表，加息预期重燃",
        "content": "美国5月新增非农就业17.2万人，是预期的两倍，3-4月数据合计上修9.3万人。市场从降息预期迅速转向加息担忧，12月加息概率升至60%以上。美元指数走强，黄金暴跌3.35%。",
        "source": "财联社",
        "time": "06-06 20:00",
        "category": "宏观"
    },
    {
        "tag": "行业",
        "importance": "high",
        "title": "存储芯片超级周期持续，车规级存储暴涨180%",
        "content": "受AI需求爆发拉动，全球存储芯片供需失衡加剧。三大原厂将80%先进产能转向HBM和高端DDR5，车规级存储芯片价格暴涨180%。机构预测2026年DRAM价格上涨125%-250%，供需紧张将延续至2027年。",
        "source": "环球网",
        "time": "06-07 11:30",
        "category": "行业"
    },
    {
        "tag": "A股",
        "importance": "high",
        "title": "公募半年考冲刺，高位兑现潮来袭",
        "content": "6月底公募基金迎来半年业绩收官，前期涨幅较大的AI算力、半导体等板块面临机构获利了结压力。资金转向低估值、高股息防御板块避险。建议投资者控制仓位，回避高位纯概念题材股。",
        "source": "证券时报",
        "time": "06-08 07:00",
        "category": "市场"
    },
    {
        "tag": "政策",
        "importance": "normal",
        "title": "算力普惠政策加速落地，AI算力成本持续下降",
        "content": "工信部推动普惠算力赋能中小企业，三大运营商推出词元套餐，DeepSeek、腾讯云相继降价。国产算力份额快速提升，AI应用门槛持续降低。专家预计算力成本下降趋势将长期持续。",
        "source": "新华社",
        "time": "06-07 22:00",
        "category": "政策"
    },
    {
        "tag": "公司",
        "importance": "normal",
        "title": "*ST建艺控股子公司中标近1.9亿元工程项目",
        "content": "*ST建艺公告称，控股子公司广东建星建造集团中标广州南站檐屿城项目二期土建总承包工程，中标金额约1.9亿元，预计对公司经营业绩产生积极影响。公司最新股价13.37元，涨2.06%。",
        "source": "公司公告",
        "time": "06-05 18:00",
        "category": "公司"
    },
]

generator.add_import_news(news_list=important_news, category_tabs=True)

# 5. 板块机会分析
sectors = [
    {
        "name": "存储芯片",
        "rating": "强烈推荐",
        "stocks": ["长江存储产业链", "长鑫存储概念", "铜冠铜箔", "雅克科技"],
        "logic": "AI驱动存储需求爆发，HBM供需缺口扩大，三大原厂涨价周期确立。英伟达与SK集团战略合作进一步强化存储超级周期逻辑，国产替代加速推进。",
        "icon": "memory",
        "category": "科技"
    },
    {
        "name": "AI算力基础设施",
        "rating": "推荐",
        "stocks": ["国产GPU", "液冷散热", "光模块", "算力租赁"],
        "logic": "全球AI资本支出持续高增，英伟达Blackwell Ultra即将交付。短期美股调整带来情绪冲击，但产业趋势未变，国产算力替代逻辑依然强硬。",
        "icon": "cpu",
        "category": "科技"
    },
    {
        "name": "高股息防御",
        "rating": "关注",
        "stocks": ["银行", "煤炭", "电力", "中字头"],
        "logic": "市场风险偏好下降，资金转向低估值高股息板块避险。高股息标的兼具防御属性和稳定现金流，在震荡市中相对收益明显。",
        "icon": "shield",
        "category": "防御"
    },
    {
        "name": "高位AI题材",
        "rating": "谨慎",
        "stocks": ["纯概念AI", "高位半导体", "无业绩支撑题材股"],
        "logic": "美股AI板块暴跌映射A股，叠加公募半年末兑现需求，高位题材股补跌风险较大。建议坚决规避无业绩支撑的纯概念股，等待情绪企稳后再布局。",
        "icon": "alert",
        "category": "风险"
    },
]

generator.add_sector_analysis(sectors=sectors, view_mode="tab")

# 6. 持仓跟踪
holdings = [
    {
        "name": "英维克",
        "code": "002837",
        "price": "65.90",
        "change": "-36.77%（较成本）",
        "up": False,
        "comment": "液冷散热龙头，受美股科技股暴跌影响，短期承压。公司基本面稳健，AI服务器液冷需求长期增长，建议耐心持有，逢低可适度加仓。",
        "ratio": 40
    },
    {
        "name": "铜冠铜箔",
        "code": "301217",
        "price": "111.26",
        "change": "+27.65%（较成本）",
        "up": True,
        "comment": "存储封装铜箔龙头，直接受益存储超级周期。英伟达与SK集团战略合作利好存储产业链，公司高端铜箔产能持续释放，建议继续持有。",
        "ratio": 35
    },
    {
        "name": "*ST建艺",
        "code": "002789",
        "price": "13.37",
        "change": "+2.06%",
        "up": True,
        "comment": "摘帽预期+横琴新区概念，子公司中标1.9亿元工程项目。公司基本面正在改善，摘帽审核中，建议谨慎持有，关注摘帽进展。",
        "ratio": 15
    },
]

position_info = {
    "total": 90,
    "cash": 10,
    "risk_level": "中高"
}

generator.add_holdings_tracking(holdings=holdings, position_info=position_info)

# 7. 风险提示
risks = [
    "美股AI板块暴跌情绪传导，A股科技股补跌风险",
    "美国加息预期升温，全球流动性收紧压力",
    "公募半年末集中兑现，高位题材股抛压加大",
    "地缘政治冲突加剧，能源价格上涨推高通胀"
]

generator.add_risk_warning(risks=risks)

# 8. 每日总结
generator.add_daily_summary(
    "美股遭遇黑色星期五，纳指暴跌4.18%创一年多最大跌幅，核心诱因是非农数据超预期引发加息担忧，叠加AI板块前期涨幅过大的获利回吐。"
    "费城半导体指数暴跌10.26%，英伟达、美光等龙头集体重挫，市场恐慌情绪急剧升温。"
    "国内方面，存储超级周期逻辑进一步强化，英伟达与SK集团战略合作锁定HBM产能，车规级存储价格暴涨180%，产业链相关公司持续受益。"
    "操作上，建议今日以防御为主，控制整体仓位在7成以下，回避高位纯AI概念股，重点关注存储芯片等有基本面支撑的硬核科技方向，以及高股息防御板块。"
    "持仓方面，铜冠铜箔受益存储周期延续强势，英维克短期承压但长期逻辑不变，*ST建艺关注摘帽进展。"
)

# 9. 明日计划
generator.add_tomorrow_plan(
    "1. 仓位管理：今日市场承压，建议将总仓位控制在7成左右，保留3成现金应对波动。\n"
    "2. 持仓操作：英维克若跌破60元可考虑小幅加仓摊薄成本；铜冠铜箔继续持有，关注120元压力位；*ST建艺持有观察摘帽进展。\n"
    "3. 重点关注：存储芯片板块开盘表现，若跌幅收窄可考虑加仓存储产业链标的；关注北向资金流向，判断外资态度。\n"
    "4. 风险规避：坚决回避近两个月翻倍、无业绩支撑的纯AI概念股，此类标的补跌风险最大。\n"
    "5. 长线布局：利用市场调整机会，逢低布局AI算力基础设施、国产芯片、存储等确定性高的硬核科技方向。"
)

# 生成HTML
html_content = generator.generate()

# 保存文件
output_path = "docs/daily/20260608_每日新闻洞察.html"
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"报告已生成: {output_path}")
print(f"文件大小: {os.path.getsize(output_path)} 字节")

