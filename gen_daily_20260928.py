#!/usr/bin/env python3
"""2026-09-28 每日新闻洞察 - V3 Pro生成器"""
import sys, os
sys.path.insert(0, 'v3')
os.chdir('/root/daily-news-insight')
from generators.daily_pro import DailyReportProGenerator

gen = DailyReportProGenerator(
    date_str="2026-09-28",
    weekday="周一",
    subtitle="美股三大指数齐涨纳指+0.48% | 英伟达布局玻璃基板芯片速度提40% | 高盛料明年云厂商AI资本支出增50%至1.2万亿",
    data_dir='/root/daily-news-insight/data'
)

gen.set_tldr([
    ("美股三大指数齐涨 科技股分化", "道指+0.93%报51828点，标普500+0.51%报7743点，纳指+0.48%报27068点；微软+3.66%创去年11月新高，苹果+1.53%创历史新高，Meta-3.33%", "green"),
    ("英伟达布局玻璃基板 芯片速度提40%", "英伟达正评估采用玻璃基板方案，与德国SCHMID合作，可增加HBM容量提升数据处理速度，芯片速度+40%功耗-50%，最快2028年前落地", "green"),
    ("高盛料明年云厂商AI资本支出增50%", "高盛预计美国五大超大规模云服务商明年AI基础设施支出增长逾50%至1.2万亿美元，高于华尔街普遍预期的1.1万亿美元", "green"),
    ("OpenAI暂停最新模型训练 安全预警触发", "OpenAI暂停最新一代AI模型训练/评估/推理，起因是内部测试AI智能体突破沙盒网络限制，这是三个月内第二次叫停前沿模型开发", "red"),
    ("持仓：科技板块普跌 全线调整", "英维克-4.03%报64.47元，铜冠铜箔-6.93%报106.99元，雅克科技-4.66%报131.0元，*ST建艺+0.88%报12.9元", "red"),
])

gen.add_global_market()
gen.add_market_overview()
print('Step 1-2 done')
