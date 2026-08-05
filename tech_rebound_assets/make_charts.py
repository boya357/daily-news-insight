
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

def _ensure_cjk_font():
    import matplotlib
    if not any("CJK" in f or "WenQuanYi" in f for f in matplotlib.rcParams.get("font.sans-serif", [])):
        import subprocess
        subprocess.run(["sed", "-i",
            "s|^#*[[:space:]]*font\\.family[[:space:]]*:.*|font.family: sans-serif|;"
            "s|^#*[[:space:]]*font\\.sans-serif[[:space:]]*:.*|font.sans-serif: Noto Sans CJK SC, WenQuanYi Micro Hei, DejaVu Sans, sans-serif|;"
            "s|^#*[[:space:]]*axes\\.unicode_minus[[:space:]]*:.*|axes.unicode_minus: False|",
            matplotlib.matplotlib_fname()])
        matplotlib.font_manager._load_fontmanager(try_read_cache=False)
        plt.rcParams["font.family"] = "sans-serif"
        plt.rcParams["font.sans-serif"] = ["Noto Sans CJK SC", "WenQuanYi Micro Hei", "DejaVu Sans"]
    plt.rcParams["axes.unicode_minus"] = False

_ensure_cjk_font()

out_dir = "/app/data/所有对话/主对话/tech_rebound_assets"
os.makedirs(out_dir, exist_ok=True)

# =========== Chart 1: 科技细分板块8月5日涨幅对比 ===========
sectors = [
    ("靶材", 9.72),
    ("电子化学品", 7.83),
    ("电子特气", 6.88),
    ("大硅片", 7.35),
    ("元件(PCB/MLCC)", 6.56),
    ("半导体(整体)", 5.80),
    ("CPO概念", 4.33),
    ("消费电子", 4.33),
    ("通信设备", -1.83),
    ("小金属(锗/钨)", 6.40),
    ("贵金属", 7.70),
    ("玻璃玻纤", 7.78),
]
sectors_sorted = sorted(sectors, key=lambda x: x[1])
names = [s[0] for s in sectors_sorted]
vals = [s[1] for s in sectors_sorted]
colors = ["#C62828" if v < 0 else ("#2E7D32" if "半导体" in n or "元件" in n or "CPO" in n or "靶材" in n or "电子" in n or "大硅片" in n else "#1F4E79") for n, v in sectors_sorted]
fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.barh(names, vals, color=colors, edgecolor='white')
ax.axvline(0, color='black', lw=0.8)
ax.set_title("8月5日科技相关板块涨跌幅（%）", fontsize=14, fontweight='bold')
ax.set_xlabel("涨跌幅（%）")
for bar, v in zip(bars, vals):
    ax.text(v + (0.15 if v>=0 else -0.15), bar.get_y()+bar.get_height()/2,
            f"{v:+.2f}%", va='center', ha='left' if v>=0 else 'right', fontsize=10)
ax.set_xlim(-3, 11)
ax.grid(axis='x', alpha=0.3)
plt.tight_layout()
plt.savefig(f"{out_dir}/sector_performance_0805.png", dpi=140, bbox_inches='tight')
plt.close()
print("chart1 done")

# =========== Chart 2: 候选主线五维评分雷达图 ===========
categories = ["政策催化", "业绩兑现", "资金共识", "板块容量", "历史股性"]
# 1-10分
scores = {
    "半导体设备": [9, 8, 9, 9, 7],
    "存储/HBM":   [8, 10, 8, 9, 8],
    "PCB/AI服务器板": [7, 9, 8, 8, 7],
    "CPO/光模块": [6, 9, 5, 9, 9],   # FCC利空导致资金共识降分
    "MLCC被动元件": [7, 8, 7, 6, 6],
    "先进封装":     [8, 7, 7, 7, 7],
    "半导体材料":   [9, 6, 7, 6, 6],
    "AI算力芯片": [8, 7, 7, 8, 8],
}
N = len(categories)
angles = [n/float(N)*2*np.pi for n in range(N)]
angles += angles[:1]
fig, ax = plt.subplots(figsize=(9, 8), subplot_kw=dict(polar=True))
colors_list = ["#C62828", "#1F4E79", "#2E7D32", "#6B7280", "#D9822B", "#7B1FA2", "#00838F", "#EF6C00"]
for (name, score), color in zip(scores.items(), colors_list):
    values = score + score[:1]
    lw = 2.8 if name in ("半导体设备", "存储/HBM") else 1.5
    alpha_fill = 0.20 if name in ("半导体设备", "存储/HBM") else 0.07
    ax.plot(angles, values, color=color, linewidth=lw, label=name)
    ax.fill(angles, values, color=color, alpha=alpha_fill)
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=12)
ax.set_ylim(0, 10)
ax.set_yticks([2,4,6,8,10])
ax.set_yticklabels(["2","4","6","8","10"], fontsize=9, color='gray')
ax.set_title("候选主线题材五维评分对比", fontsize=14, fontweight='bold', pad=22)
ax.legend(loc='upper right', bbox_to_anchor=(1.32, 1.08), fontsize=10)
plt.tight_layout()
plt.savefig(f"{out_dir}/mainline_radar.png", dpi=140, bbox_inches='tight')
plt.close()
print("chart2 done")

# =========== Chart 3: 核心标的成交额 & 涨幅 ===========
stocks = [
    ("中际旭创", -7.27, 671),
    ("工业富联", 10.0, 186),
    ("胜宏科技", 17.13, 295),
    ("寒武纪", 5.44, 206),
    ("兆易创新", 8.26, 262),  # 周口径估
    ("长鑫科技", 0.2, 314),
    ("中微公司", 12.68, 131),
    ("北方华创", 6.87, 99),
    ("佰维存储", 7.14, 96),
    ("澜起科技", 5.20, 122),
    ("海光信息", 4.90, 76),
    ("中芯国际", 3.59, 83),
    ("拓荆科技", 12.14, 73),
    ("雅克科技", 8.60, 59),
    ("铜冠铜箔", 10.14, 40),
    ("华海清科", 11.82, 48),
]
stocks_sorted = sorted(stocks, key=lambda x: x[2], reverse=True)
names = [s[0] for s in stocks_sorted]
amts = [s[2] for s in stocks_sorted]
chgs = [s[1] for s in stocks_sorted]
fig, ax1 = plt.subplots(figsize=(12, 6.5))
x = np.arange(len(names))
bars = ax1.bar(x, amts, color=["#C62828" if c < 0 else "#1F4E79" for c in chgs], alpha=0.85, label="成交额(亿元)")
ax1.set_ylabel("成交额（亿元）", fontsize=11)
ax1.set_xticks(x)
ax1.set_xticklabels(names, rotation=35, ha='right', fontsize=10)
ax2 = ax1.twinx()
ax2.plot(x, chgs, color="#D9822B", marker='o', linewidth=2, markersize=7, label="涨跌幅(%)")
ax2.axhline(0, color='gray', lw=0.6, ls='--')
ax2.set_ylabel("涨跌幅（%）", fontsize=11, color="#D9822B")
ax2.tick_params(axis='y', labelcolor="#D9822B")
ax1.set_title("8月5日科技核心个股成交额（柱）vs 涨跌幅（线）", fontsize=14, fontweight='bold')
for i, (a, c) in enumerate(zip(amts, chgs)):
    ax2.text(i, c + (0.7 if c>=0 else -1.2), f"{c:+.1f}%", ha='center', fontsize=8.5, color="#D9822B")
ax1.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig(f"{out_dir}/core_stocks_amount_chg.png", dpi=140, bbox_inches='tight')
plt.close()
print("chart3 done")

# =========== Chart 4: 存储超级周期价格走势示意（Q1-Q4 2026E DRAM/NAND 环比涨幅） ===========
quarters = ["2026Q1", "2026Q2", "2026Q3E\n(瑞银最新)", "2026Q4E"]
dram = [95, 60, 32, 18]   # % QoQ 区间中值/瑞银
nand = [50, 72, 30, 12]
x = np.arange(len(quarters))
w = 0.36
fig, ax = plt.subplots(figsize=(9, 5.5))
b1 = ax.bar(x-w/2, dram, w, label="DRAM合约价环比涨幅(%)", color="#1F4E79")
b2 = ax.bar(x+w/2, nand, w, label="NAND合约价环比涨幅(%)", color="#D9822B")
ax.set_xticks(x); ax.set_xticklabels(quarters, fontsize=11)
ax.set_ylabel("环比涨幅（%）")
ax.set_title("2026年存储合约价季度环比涨幅：超级周期前中段", fontsize=13, fontweight='bold')
ax.legend()
for bars in (b1, b2):
    for b in bars:
        ax.text(b.get_x()+b.get_width()/2, b.get_height()+1.5, f"{b.get_height():.0f}%", ha='center', fontsize=10)
ax.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig(f"{out_dir}/storage_price_cycle.png", dpi=140, bbox_inches='tight')
plt.close()
print("chart4 done")

print("ALL CHARTS DONE")
