#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""生成英伟达800VDC研究报告所需图表"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import os

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['Noto Sans CJK SC', 'WenQuanYi Micro Hei', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False
print("Using font:", plt.rcParams['font.sans-serif'])

OUT = "/app/data/所有对话/主对话/英伟达800VDC智算中心供电_assets"
os.makedirs(OUT, exist_ok=True)

# ============ 图1: 全球AI数据中心800V/HVDC/SST市场规模预测(2025-2030) ============
years = [2025, 2026, 2027, 2028, 2029, 2030]
# 单位：亿元人民币。基于兴业证券/花旗/SemiAnalysis综合测算（中性情景）
# 传统UPS向HVDC/SST演进
ups_market =     [340, 380, 320, 240, 160, 92]      # 传统UPS逐步萎缩
hvdc_market =    [ 50, 150, 400, 680, 800, 858]     # 800V HVDC/Power Shelf/Sidecar
sst_market =     [  5,  20,  80, 280, 800, 1760]    # SST固态变压器2028后加速
psu_highpower =  [120, 220, 380, 520, 620, 700]     # 高功率PSU/电源组件（800V相关）
total = [a+b+c+d for a,b,c,d in zip(ups_market, hvdc_market, sst_market, psu_highpower)]

fig, ax = plt.subplots(figsize=(11, 6.5))
x = np.arange(len(years))
w = 0.55
ax.bar(x, ups_market, w, label='Traditional UPS (shrinking)', color='#95a5a6')
ax.bar(x, hvdc_market, w, bottom=ups_market, label='800V HVDC / Power Shelf', color='#3498db')
bot2 = [a+b for a,b in zip(ups_market, hvdc_market)]
ax.bar(x, sst_market, w, bottom=bot2, label='SST (Solid State Transformer)', color='#e74c3c')
bot3 = [a+b for a,b in zip(bot2, sst_market)]
ax.bar(x, psu_highpower, w, bottom=bot3, label='High-power PSU / Components', color='#f39c12')
for i, t in enumerate(total):
    ax.text(i, t+50, f'{t}', ha='center', fontsize=10, fontweight='bold')
ax.set_xticks(x); ax.set_xticklabels(years)
ax.set_ylabel('Market Size (RMB 100M)')
ax.set_title('Global AI Datacenter Power Delivery Market Forecast 2025-2030\n(Neutral Scenario, Unit: RMB 100M)')
ax.legend(loc='upper left', fontsize=9)
ax.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig(f"{OUT}/market_size.png", dpi=140, bbox_inches='tight')
plt.close()
print("Saved market_size.png")

# ============ 图2: 800V HVDC渗透率曲线（三档情景） ============
years2 = [2025, 2026, 2027, 2028, 2029, 2030]
bear =   [0,  3, 10, 22, 28, 30]    # 大摩专家30%
base =   [0,  8, 25, 50, 65, 70]    # 中性（折中花旗/ABB）
bull =   [0, 12, 35, 65, 78, 80]    # 乐观（接近花旗79%）

fig, ax = plt.subplots(figsize=(10, 5.5))
ax.plot(years2, bear, 'o--', color='#7f8c8d', label='Bear (Morgan Stanley expert survey, 30% by 2030)', linewidth=2)
ax.plot(years2, base, 's-',  color='#2980b9', label='Base (Synthesis, ~70% by 2030)', linewidth=2.5)
ax.plot(years2, bull, '^-',  color='#c0392b', label='Bull (Citi 79% by 2030)', linewidth=2)
ax.fill_between(years2, bear, bull, alpha=0.12, color='#3498db')
ax.axvline(2027, color='orange', linestyle=':', alpha=0.7)
ax.text(2027.05, 5, 'Rubin Ultra\nNVL576 ramp', fontsize=9, color='orange')
ax.set_xticks(years2)
ax.set_ylabel('800V HVDC Penetration in New AI Datacenters (%)')
ax.set_xlabel('Year')
ax.set_title('800V HVDC Penetration Forecast (3 Scenarios)')
ax.set_ylim(0, 90)
ax.legend(loc='upper left', fontsize=9)
ax.grid(alpha=0.3)
plt.tight_layout()
plt.savefig(f"{OUT}/penetration.png", dpi=140, bbox_inches='tight')
plt.close()
print("Saved penetration.png")

# ============ 图3: 产业链价值量分布（800V整机柜1MW供电侧BOM） ============
labels = ['Power Shelf/\nSidecar PSU', 'Busway/\nCopper', 'SST / HVDC\nRectifier', 'Magnetics\n(transformer/inductor)',
         'Power\nSemiconductor', 'Capacitors\n(film/Al/Supercap)', 'Connectors/\nBreakers/Relays', 'BBU /\nEnergy Storage', 'Others']
# 基于SemiAnalysis/券商研报拆分（约25-30万/柜供电侧BOM，按占比）
sizes = [22, 14, 20, 10, 12, 8, 7, 4, 3]
colors = ['#3498db', '#e67e22', '#e74c3c', '#9b59b6', '#1abc9c', '#f1c40f', '#34495e', '#2ecc71', '#95a5a6']
explode = [0.06, 0, 0.08, 0, 0.02, 0, 0.02, 0, 0]

fig, ax = plt.subplots(figsize=(10, 7))
wedges, texts, autotexts = ax.pie(sizes, labels=labels, autopct='%1.0f%%', startangle=90,
                                   colors=colors, explode=explode, textprops={'fontsize':10})
ax.set_title('800V HVDC 1MW Rack Power-Delivery BOM Value Split\n(Basis: ~RMB 250-300k power-side BOM per MW rack)')
plt.tight_layout()
plt.savefig(f"{OUT}/value_chain_pie.png", dpi=140, bbox_inches='tight')
plt.close()
print("Saved value_chain_pie.png")

# ============ 图4: A股核心标的综合评分条形图 ============
# 评分体系：业务纯度30 + 技术壁垒25 + 客户质量20 + 业绩弹性25 = 100
# 基于公开信息的分析师视角评分（说明：此为研究判断，非投资建议）
stocks = [
    ('Megmeet 麦格米特 (002851)',   9.0, 8.5, 9.5, 8.0, 'S'),
    ('Inwin 欧陆通 (300870)',        8.0, 7.0, 8.5, 9.0, 'A'),
    ('Zhongheng 中恒电气 (002364)',  8.5, 7.5, 8.5, 7.5, 'A'),
    ('Kehua 科华数据 (002335)',      7.0, 7.5, 8.0, 6.5, 'A'),
    ('Xinleinen 新雷能 (300593)',    8.5, 8.0, 7.5, 9.5, 'A'),
    ('Star Power 斯达半导 (603290)', 7.0, 9.0, 7.5, 7.5, 'A'),
    ('Macmic 宏微科技 (688711)',     7.5, 8.5, 7.0, 8.5, 'A'),
    ('Times Elec 时代电气 (688187)', 6.5, 9.0, 8.0, 6.0, 'B'),
    ('Farah 法拉电子 (600563)',      7.5, 8.5, 8.0, 6.5, 'A'),
    ('Jianghai 江海股份 (002484)',   7.5, 8.0, 7.0, 7.5, 'B'),
    ('Tongfeng 铜峰电子 (600237)',   7.0, 7.0, 6.5, 8.0, 'B'),
    ('Keli 可立克 (002782)',         8.0, 7.0, 7.0, 8.5, 'B'),
    ('Mentech 铭普光磁 (002902)',    7.5, 7.0, 7.0, 8.0, 'B'),
    ('Jingquanhu 京泉华 (002885)',   7.0, 6.5, 6.5, 8.0, 'B'),
    ('Eaglerise 伊戈尔 (002922)',    7.5, 7.5, 8.0, 7.0, 'B'),
    ('Takechannel 铂科新材 (300811)',8.0, 8.5, 8.5, 8.5, 'S'),
    ('Sunlord 顺络电子 (002138)',    7.0, 8.0, 7.5, 7.0, 'B'),
    ('Sifang 四方股份 (601126)',     6.5, 8.5, 7.0, 6.0, 'B'),
    ('Jinpan 金盘科技 (688676)',     6.5, 7.5, 7.5, 6.5, 'B'),
    ('TYT 泰永长征 (002927)',        8.5, 9.0, 8.0, 9.0, 'S'),
    ('Hongfa 宏发股份 (600885)',     5.5, 8.5, 8.5, 6.0, 'B'),
    ('Zhongrong 中熔电气 (301031)',  7.5, 8.0, 8.0, 8.0, 'B'),
    ('Yonggui 永贵电器 (300351)',    7.0, 7.0, 7.5, 8.0, 'B'),
    ('Envicool 英维克 (002837)',     7.5, 8.0, 9.0, 7.0, 'A'),
    ('Walsin 沃尔核材 (002130)',     6.5, 6.5, 7.5, 7.0, 'B'),
    ('Baosheng 宝胜股份 (600973)',   6.0, 6.0, 7.0, 7.0, 'C'),
    ('Kstar 科士达 (002518)',        6.0, 6.5, 7.0, 6.0, 'C'),
    ('Huafeng 华丰科技 (688629)',    6.5, 7.0, 7.5, 6.5, 'C'),
    ('Great Wall 中国长城 (000066)', 5.5, 7.0, 6.5, 5.5, 'C'),
    ('Peri 派瑞股份 (300831)',       4.0, 8.0, 6.0, 4.0, 'C'),
]
# 加权综合
scored = []
for name, pur, bar, cus, ela, tier in stocks:
    total = pur*3 + bar*2.5 + cus*2 + ela*2.5   # max 10*10=100 其实是10* (3+2.5+2+2.5) = 100
    scored.append((name, total, tier))
scored.sort(key=lambda x: -x[1])

names = [s[0] for s in scored]
vals = [s[1] for s in scored]
tiers = [s[2] for s in scored]
tier_color = {'S':'#c0392b', 'A':'#e67e22', 'B':'#3498db', 'C':'#95a5a6'}
bar_colors = [tier_color[t] for t in tiers]

fig, ax = plt.subplots(figsize=(12, 12))
y_pos = np.arange(len(names))
bars = ax.barh(y_pos, vals, color=bar_colors, edgecolor='white')
ax.set_yticks(y_pos); ax.set_yticklabels(names, fontsize=10)
ax.invert_yaxis()
ax.set_xlim(55, 95)
ax.set_xlabel('Composite Score (Purity 30% + Tech Barrier 25% + Customer 20% + Elasticity 25%)')
ax.set_title('A-Share 800V HVDC Value Chain - Composite Score Ranking')
for bar, v, t in zip(bars, vals, tiers):
    ax.text(v+0.3, bar.get_y()+bar.get_height()/2, f'{v:.1f} ({t})', va='center', fontsize=9, fontweight='bold')
# Legend
import matplotlib.patches as mpatches
legend_handles = [mpatches.Patch(color=v, label=f'Tier {k}') for k,v in tier_color.items()]
ax.legend(handles=legend_handles, loc='lower right', fontsize=10)
ax.grid(axis='x', alpha=0.3)
plt.tight_layout()
plt.savefig(f"{OUT}/stock_ranking.png", dpi=140, bbox_inches='tight')
plt.close()
print("Saved stock_ranking.png")

print("All charts saved to:", OUT)
