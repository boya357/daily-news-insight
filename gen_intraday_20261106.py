#!/usr/bin/env python3
# 20261106 盘中快报生成脚本

import sys
import os

WORK_DIR = '/root/daily-news-insight'
sys.path.insert(0, os.path.join(WORK_DIR, 'v3'))
os.chdir(WORK_DIR)

from generators.intraday import IntradayGenerator
from generators.list_page import ListPageGenerator

date_str = '2026年11月6日'

indices = [
    {'name': '上证指数', 'value': '3,647.90', 'change': '-1.14%', 'up': False, 'icon': 'trending_down'},
    {'name': '深证成指', 'value': '11,216.95', 'change': '-2.22%', 'up': False, 'icon': 'trending_down'},
    {'name': '创业板指', 'value': '2,477.07', 'change': '-3.50%', 'up': False, 'icon': 'trending_down'},
    {'name': '科创50', 'value': '1,259.84', 'change': '-2.09%', 'up': False, 'icon': 'trending_down'},
]
market_status = '震荡调整'

focus_point = 'A股今日受外围市场扰动大幅低开，截至午间收盘沪指跌1.14%报3647.90点，深成指跌2.22%报11216.95点，创业板指跌3.50%报2477.07点，科创50跌2.09%报1259.84点。半日成交约1.13万亿元，较上日同期缩量约3400亿元，全市场超4500只个股下跌仅约500只上涨，涨停26家跌停数量激增，市场情绪极度低迷。核心催化：（1）隔夜美股暴跌，纳指跌5.52%标普跌4.36%道指跌3.44%，费城半导体指数重挫12.25%创2020年3月以来最大单日跌幅，民主党中期选举大胜引发市场担忧AI数据中心监管收紧；（2）日韩股市同步大跌，日经225跌5.27%，韩国KOSPI一度暴跌8%触发熔断机制，三星电子SK海力士跌超9%；（3）A股低开后展现韧性，科创50盘中一度翻红，抄底资金逢低布局，但整体仍处于弱势震荡；（4）农业板块逆势领涨（种植业+1.8%），电力、光伏赛道反复活跃，算力硬件方向再度领跌（中际旭创东山精密等跌超8%）。盘面特征：普跌格局，仅农业/电力/银行等防御品种上涨，科技成长全线受挫，算力硬件链成为重灾区。'

print('Step 1: 生成报告...')
gen = IntradayGenerator(date_str=date_str, subtitle=f'{date_str} 星期五 · 午盘速递')
gen.add_focus_point(focus_point)
gen.add_market_overview(indices=indices, market_status=market_status)
print('  - 焦点和概览已添加')
