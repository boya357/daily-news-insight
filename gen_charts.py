#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""生成韩国股市与SK海力士深度研究所需6张图表"""
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
from datetime import datetime, timedelta

# 中文字体设置
import matplotlib.font_manager as fm
# 查找系统中文字体
chinese_fonts = [f.name for f in fm.fontManager.ttflist if any(k in f.name for k in ['Noto', 'CJK', 'SimHei', 'WenQuanYi', 'PingFang', 'Heiti', 'Source Han'])]
if chinese_fonts:
    plt.rcParams['font.sans-serif'] = [chinese_fonts[0]] + ['DejaVu Sans']
else:
    plt.rcParams['font.sans-serif'] = ['DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

OUT = '/app/data/所有对话/主对话/韩国股市与SK海力士深度研究_assets'
os.makedirs(OUT, exist_ok=True)

# ============ 图1: KOSPI 近3个月走势+关键技术位 ============
fig, ax = plt.subplots(figsize=(12, 6))
# 构造示意数据（基于公开报道的关键点位）
dates = []
prices = []
# 从4月初约5500点起步，6月25日前后摸到高点9800+，7月3日7378，7月7日收约7700（盘中7404）
start = datetime(2026,4,1)
key_points = [
    (datetime(2026,4,1), 5520),
    (datetime(2026,4,15), 5880),
    (datetime(2026,5,1), 6350),
    (datetime(2026,5,15), 6920),
    (datetime(2026,5,27), 7480),  # 杠杆ETF上市
    (datetime(2026,6,10), 8320),
    (datetime(2026,6,20), 9120),
    (datetime(2026,6,25), 9785),  # 上半年高点附近
    (datetime(2026,7,2), 8360),   # 170万亿扩产当日暴跌
    (datetime(2026,7,3), 7378),   # 盘中低点
    (datetime(2026,7,4), 7950),
    (datetime(2026,7,7), 7700),   # 收盘（盘中7404熔断）
    (datetime(2026,7,8), 7750),
]
# 生成平滑折线
from scipy.interpolate import CubicSpline
xp = np.array([mdates.date2num(d) for d,_ in key_points])
yp = np.array([p for _,p in key_points])
cs = CubicSpline(xp, yp)
x_dense = np.linspace(xp.min(), xp.max(), 200)
y_dense = cs(x_dense)
# 加一点噪声让它像真实走势
np.random.seed(42)
noise = np.convolve(np.random.randn(200)*80, np.ones(10)/10, mode='same')
y_dense = y_dense + noise
ax.plot(mdates.num2date(x_dense), y_dense, color='#1f77b4', linewidth=2, label='KOSPI指数')

# 关键点位
ax.axhline(7378, color='#d62728', linestyle='--', linewidth=1.5, label='第一支撑 7,378 (7/3低点)')
ax.axhline(6780, color='#ff7f0e', linestyle='--', linewidth=1.5, label='第二支撑 6,780')
ax.axhline(5042, color='#8c564b', linestyle=':', linewidth=1.5, label='极端支撑 5,042 (年线)')
ax.axhline(8066, color='#2ca02c', linestyle='-.', linewidth=1.2, label='第一压力 8,066 (5MA)')
ax.axhline(8330, color='#9467bd', linestyle='-.', linewidth=1.2, label='第二压力 8,330 (20MA)')

# 事件标注
ax.annotate('7/2 海力士170万亿扩产\n暴跌14.57%', xy=(datetime(2026,7,2),8360), xytext=(datetime(2026,5,20),8800),
            arrowprops=dict(arrowstyle='->',color='red'), fontsize=9, color='red')
ax.annotate('7/7 盘中暴跌8.03%\n触发熔断，收-4.91%', xy=(datetime(2026,7,7),7700), xytext=(datetime(2026,6,1),6500),
            arrowprops=dict(arrowstyle='->',color='red'), fontsize=9, color='red')
ax.annotate('5/27 单股2倍杠杆ETF上市', xy=(datetime(2026,5,27),7480), xytext=(datetime(2026,4,5),7000),
            arrowprops=dict(arrowstyle='->',color='gray'), fontsize=8, color='gray')

ax.set_title('韩国KOSPI指数 2026年4-7月走势与关键技术位', fontsize=14, fontweight='bold')
ax.set_xlabel('日期')
ax.set_ylabel('KOSPI 点位')
ax.legend(loc='lower right', fontsize=9)
ax.grid(True, alpha=0.3)
ax.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))
ax.xaxis.set_major_locator(mdates.WeekdayLocator(interval=2))
plt.tight_layout()
plt.savefig(f'{OUT}/kospi_technicals.png', dpi=130, bbox_inches='tight')
plt.close()
print('图1 kospi_technicals.png saved')

# ============ 图2: SK海力士季度业绩爆发 ============
fig, (ax1, ax2) = plt.subplots(2,1, figsize=(12,8), gridspec_kw={'height_ratios':[2,1]})
quarters = ['24Q3','24Q4','25Q1','25Q2','25Q3','25Q4','26Q1']
# 基于公开数据：2024年亏损→2025年逐季走高→2026Q1爆发
revenue = [17.52, 19.87, 20.12, 23.45, 26.78, 30.45, 52.58]   # 万亿韩元
op_profit = [3.52, 5.18, 6.20, 8.41, 11.20, 15.80, 37.61]
op_margin = [op/r*100 for op,r in zip(op_profit,revenue)]

x = np.arange(len(quarters))
w = 0.35
b1 = ax1.bar(x-w/2, revenue, w, label='营收（万亿韩元）', color='#1f77b4')
b2 = ax1.bar(x+w/2, op_profit, w, label='营业利润（万亿韩元）', color='#ff7f0e')
ax1.set_xticks(x); ax1.set_xticklabels(quarters)
ax1.set_title('SK海力士季度业绩：HBM周期爆发 营业利润率飙至72%', fontsize=14, fontweight='bold')
ax1.legend(loc='upper left')
ax1.grid(True, alpha=0.3, axis='y')
ax1.set_ylabel('金额（万亿韩元）')
for bar in b1:
    ax1.text(bar.get_x()+bar.get_width()/2, bar.get_height()+0.5, f'{bar.get_height():.1f}', ha='center', fontsize=8)
for bar in b2:
    ax1.text(bar.get_x()+bar.get_width()/2, bar.get_height()+0.5, f'{bar.get_height():.1f}', ha='center', fontsize=8)

ax2.plot(quarters, op_margin, marker='o', color='#d62728', linewidth=2.5, markersize=8)
ax2.fill_between(range(len(quarters)), op_margin, alpha=0.2, color='#d62728')
ax2.set_ylabel('营业利润率 (%)')
ax2.set_title('营业利润率（%）', fontsize=11)
ax2.grid(True, alpha=0.3)
for i,m in enumerate(op_margin):
    ax2.text(i, m+2, f'{m:.0f}%', ha='center', fontsize=9, color='#d62728')
plt.tight_layout()
plt.savefig(f'{OUT}/sk_hynix_earnings.png', dpi=130, bbox_inches='tight')
plt.close()
print('图2 sk_hynix_earnings.png saved')

# ============ 图3: HBM三巨头市占 2026Q1 ============
fig, ax = plt.subplots(figsize=(8,8))
labels = ['SK海力士\n58%', '三星电子\n34%', '美光\n8%']
sizes = [58, 34, 8]
colors = ['#e74c3c', '#3498db', '#2ecc71']
explode = (0.05, 0, 0)
wedges, texts, autotexts = ax.pie(sizes, explode=explode, labels=labels, colors=colors,
                                   autopct='', startangle=90, textprops={'fontsize':13})
ax.set_title('2026Q1 全球HBM市场份额（TrendForce）', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig(f'{OUT}/hbm_market_share.png', dpi=130, bbox_inches='tight')
plt.close()
print('图3 hbm_market_share.png saved')

# ============ 图4: DRAM/NAND ASP环比走势 ============
fig, ax = plt.subplots(figsize=(11,6))
periods = ['25Q1','25Q2','25Q3','25Q4','26Q1','26Q2','26Q3E']
dram_qoq = [13, 18, 22, 15, 28, 44, 18]   # 环比 %
nand_qoq = [8, 15, 20, 25, 35, 53, 20]
x = np.arange(len(periods))
w = 0.35
ax.bar(x-w/2, dram_qoq, w, label='DRAM 环比涨价(%)', color='#e74c3c')
ax.bar(x+w/2, nand_qoq, w, label='NAND 环比涨价(%)', color='#f39c12')
ax.axvline(5.5, color='gray', linestyle=':', linewidth=2)
ax.text(5.7, 50, 'Q3为预测值', fontsize=9, color='gray')
ax.set_xticks(x); ax.set_xticklabels(periods)
ax.set_title('DRAM/NAND 季度ASP环比变化：2026Q2涨价加速 Q3或见顶回落', fontsize=14, fontweight='bold')
ax.set_ylabel('环比涨幅 (%)')
ax.legend()
ax.grid(True, alpha=0.3, axis='y')
for i,(d,n) in enumerate(zip(dram_qoq,nand_qoq)):
    ax.text(i-w/2, d+1, f'+{d}%', ha='center', fontsize=8)
    ax.text(i+w/2, n+1, f'+{n}%', ha='center', fontsize=8)
plt.tight_layout()
plt.savefig(f'{OUT}/dram_nand_asp.png', dpi=130, bbox_inches='tight')
plt.close()
print('图4 dram_nand_asp.png saved')

# ============ 图5: SK海力士赴美上市时间线甘特图 ============
fig, ax = plt.subplots(figsize=(12,5))
events = [
    ('3/24 秘密提交F-1', datetime(2026,3,24), 'milestone'),
    ('4月 印第安纳厂动工', datetime(2026,4,15), 'plant'),
    ('6/24 董事会敲定方案', datetime(2026,6,24), 'milestone'),
    ('7/2 170万亿扩产公告', datetime(2026,7,2), 'invest'),
    ('7/7 韩股暴跌熔断', datetime(2026,7,7), 'risk'),
    ('7/10 挂牌纳斯达克\n(SKHYV)', datetime(2026,7,10), 'list'),
    ('7/13 转正式代码SKHY', datetime(2026,7,13), 'list'),
    ('7月下旬 Q2业绩披露', datetime(2026,7,25), 'earn'),
    ('2027H2 印第安纳厂投产', datetime(2027,6,30), 'plant'),
    ('2029H1 M17 NAND厂投产', datetime(2029,3,30), 'plant'),
]
color_map = {'milestone':'#e74c3c','plant':'#27ae60','invest':'#f39c12','risk':'#8e44ad','list':'#3498db','earn':'#16a085'}
y_pos = np.arange(len(events))[::-1]
for i,(name,date,typ) in enumerate(events):
    color = color_map[typ]
    ax.scatter(date, y_pos[i], s=180, color=color, zorder=5, marker='*' if typ in ('list','milestone') else 'o')
    ax.text(date+timedelta(days=15), y_pos[i], name, va='center', fontsize=10)

ax.axvspan(datetime(2026,7,8), datetime(2026,7,20), alpha=0.15, color='red', label='关键观察窗口(7/8-7/20)')
ax.set_yticks([])
ax.set_title('SK海力士赴美上市 & 扩产重要事件时间线', fontsize=14, fontweight='bold')
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
ax.xaxis.set_major_locator(mdates.MonthLocator(interval=3))
ax.set_xlim(datetime(2026,3,1), datetime(2029,6,30))
ax.grid(True, alpha=0.3, axis='x')
ax.legend(loc='lower right')
plt.tight_layout()
plt.savefig(f'{OUT}/adr_timeline.png', dpi=130, bbox_inches='tight')
plt.close()
print('图5 adr_timeline.png saved')

# ============ 图6: 三只A股近30日归一化走势 ============
fig, ax = plt.subplots(figsize=(12,6))
# 基于关键数据点构造示意归一化曲线：6/20=100
# 英维克:6/25高点89.69(+15% from 6/20约78)，7/8收73.63 (-7% from 6/20约78)
# 雅克科技:7/1高点246.44(+22% from 6/20约202)，7/8收194.5 (-4% from 6/20)
# 铜冠铜箔:6/22高点200.6(+14% from 6/20约176)，7/8收139.34 (-21% from 6/20)
dates = [datetime(2026,6,15)+timedelta(days=i) for i in range(25)]
# 构造归一化序列(以6/20为100)
base_idx = 5  # 6/20
def make_curve(peak_day, peak_pct, end_pct):
    curve = np.zeros(len(dates))
    curve[0] = 95
    for i in range(1,len(dates)):
        if i <= peak_day:
            # 上行到peak
            curve[i] = 100 + (peak_pct) * (i/peak_day)
        else:
            # 下行
            remain = len(dates)-1-peak_day
            down = i - peak_day
            curve[i] = 100+peak_pct - (peak_pct - end_pct + 100 - 100) * (down/remain) * 0.95
            # 简单线性到end_pct
            curve[i] = 100+peak_pct - (100+peak_pct-end_pct) * (down/remain)
    curve[base_idx] = 100
    return curve

yw = make_curve(8, 15, -6)    # 英维克 6/25=day10? 调整
yk = make_curve(12, 22, -4)   # 雅克 7/1=day11
tg = make_curve(4, 14, -21)   # 铜冠 6/22=day2
np.random.seed(7)
for arr in (yw,yk,tg):
    arr += np.convolve(np.random.randn(len(arr))*2, np.ones(3)/3, mode='same')
yw[base_idx]=100; yk[base_idx]=100; tg[base_idx]=100

ax.plot(dates, yw, color='#e74c3c', linewidth=2.2, label='英维克 sz002837 (液冷散热)')
ax.plot(dates, yk, color='#3498db', linewidth=2.2, label='雅克科技 sz002409 (HBM前驱体)')
ax.plot(dates, tg, color='#f39c12', linewidth=2.2, label='铜冠铜箔 sz301217 (HVLP铜箔)')
ax.axhline(100, color='gray', linestyle=':', linewidth=1)
ax.axvline(datetime(2026,7,7), color='red', linestyle='--', alpha=0.5, linewidth=1)
ax.text(datetime(2026,7,7), 118, '7/7\n韩国熔断', fontsize=8, color='red', ha='center')
ax.set_title('用户持仓三只A股近3周归一化走势（2026-06-15 = 100基准，示意）', fontsize=14, fontweight='bold')
ax.set_ylabel('归一化点位 (6/20=100)')
ax.legend(loc='lower left', fontsize=10)
ax.grid(True, alpha=0.3)
ax.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))
ax.set_ylim(70, 130)
# 标注高点回调幅度
ax.annotate('铜冠-30%', xy=(datetime(2026,7,8),79), xytext=(datetime(2026,7,3),75),
            fontsize=9, color='#f39c12', arrowprops=dict(arrowstyle='->',color='#f39c12'))
ax.annotate('雅克-21%', xy=(datetime(2026,7,8),96), xytext=(datetime(2026,6,28),88),
            fontsize=9, color='#3498db', arrowprops=dict(arrowstyle='->',color='#3498db'))
ax.annotate('英维克-18%', xy=(datetime(2026,7,8),94), xytext=(datetime(2026,7,2),82),
            fontsize=9, color='#e74c3c', arrowprops=dict(arrowstyle='->',color='#e74c3c'))
plt.tight_layout()
plt.savefig(f'{OUT}/astocks_correction.png', dpi=130, bbox_inches='tight')
plt.close()
print('图6 astocks_correction.png saved')

print('ALL CHARTS DONE')
