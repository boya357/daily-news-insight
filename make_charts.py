#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""雅克科技深度研究报告可视化：K线+均线、财务趋势、业务结构、估值对比、HBM敏感性"""
import os, pickle, math
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.patches import Rectangle
from datetime import datetime
import numpy as np

# 中文字体
plt.rcParams["font.sans-serif"] = ["Noto Sans CJK SC", "Noto Sans CJK JP", "WenQuanYi Zen Hei", "DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False

OUT = "/app/data/所有对话/主对话/雅克科技深度研究_assets"
os.makedirs(OUT, exist_ok=True)

with open("/tmp/kline.pkl","rb") as f:
    krows = pickle.load(f)  # (date, open, close, high, low, vol, amt)

# ========== 图1: K线+均线+成交量 ==========
def chart_kline():
    dates = [datetime.strptime(r[0],"%Y-%m-%d") for r in krows]
    opens = np.array([r[1] for r in krows])
    closes = np.array([r[2] for r in krows])
    highs = np.array([r[3] for r in krows])
    lows = np.array([r[4] for r in krows])
    vols = np.array([r[5] for r in krows])/10000  # 万手
    n=len(dates)

    # 计算均线
    def ma(arr,p):
        out=np.full_like(arr,np.nan,dtype=float)
        for i in range(p-1,len(arr)): out[i]=arr[i-p+1:i+1].mean()
        return out
    ma5=ma(closes,5); ma10=ma(closes,10); ma20=ma(closes,20); ma60=ma(closes,60)

    fig,(ax1,ax2)=plt.subplots(2,1,figsize=(13,7),gridspec_kw={"height_ratios":[3,1]},sharex=True)
    fig.patch.set_facecolor("#0f0c29")
    for ax in (ax1,ax2):
        ax.set_facecolor("#0f0c29")
        ax.tick_params(colors="#ddd")
        for s in ax.spines.values(): s.set_color("#444")

    # K线
    for i,d in enumerate(dates):
        color = "#ef4444" if closes[i]<opens[i] else "#22c55e"
        # 影线
        ax1.plot([i,i],[lows[i],highs[i]],color=color,lw=0.8)
        # 实体
        body_b=min(opens[i],closes[i]); body_h=abs(closes[i]-opens[i])
        ax1.add_patch(Rectangle((i-0.3,body_b),0.6,max(body_h,0.3),facecolor=color,edgecolor=color))

    ax1.plot(range(n),ma5,color="#fbbf24",lw=1.2,label="MA5")
    ax1.plot(range(n),ma10,color="#60a5fa",lw=1.2,label="MA10")
    ax1.plot(range(n),ma20,color="#a78bfa",lw=1.2,label="MA20")
    if n>=60: ax1.plot(range(n),ma60,color="#f472b6",lw=1.3,label="MA60")
    # 标记关键事件
    marks = {
        "7/1高点246.44": datetime(2026,7,1),
        "7/17-7%": datetime(2026,7,17),
        "7/20跌停130.5": datetime(2026,7,20),
        "3/中旬80元": datetime(2026,3,20),
    }
    for lab,dm in marks.items():
        if dm in dates:
            idx=dates.index(dm)
            ax1.annotate(lab,xy=(idx,highs[idx] if "跌停" not in lab else closes[idx]),
                         xytext=(idx,highs[idx]*1.05),color="#fff",fontsize=9,ha="center",
                         arrowprops=dict(arrowstyle="->",color="#fbbf24",lw=0.8))

    ax1.set_title("雅克科技(002409) 日K线 + 关键均线 (2026.02-2026.07)",color="#fff",fontsize=14,pad=12)
    ax1.legend(loc="upper left",facecolor="#1e1b4b",edgecolor="#444",labelcolor="#fff",fontsize=9)
    ax1.set_ylabel("价格(元)",color="#ddd")
    ax1.grid(True,color="#2a2750",alpha=0.4)

    # 成交量
    colors = ["#ef4444" if closes[i]<opens[i] else "#22c55e" for i in range(n)]
    ax2.bar(range(n),vols,color=colors,width=0.6)
    ax2.set_ylabel("成交量(万手)",color="#ddd")
    ax2.grid(True,color="#2a2750",alpha=0.4)
    # x轴
    tick_idx = list(range(0,n,max(1,n//12)))
    ax2.set_xticks(tick_idx)
    ax2.set_xticklabels([dates[i].strftime("%m-%d") for i in tick_idx],rotation=30,color="#ddd",fontsize=8)

    plt.tight_layout()
    p=f"{OUT}/01_kline.png"
    plt.savefig(p,dpi=130,facecolor=fig.get_facecolor());plt.close()
    print("saved",p)

# ========== 图2: 营收&净利趋势(近6年+2026Q1年化) ==========
def chart_finance():
    # 数据来源：westockdata lrb + 2025年报+2026Q1
    years=["2020","2021","2022","2023","2024","2025","2026E"]
    # 雅克历年营收(亿元)
    rev=[22.73,37.20,42.09,49.33,68.62,86.11, 88.0]
    # 归母净利(亿元)
    npf=[4.00,3.36,5.04,6.43,8.72,10.00,11.2]
    # 2026E基于2026Q1营收19.73亿、归母2.67亿，简单年化*4做参考(实际非均匀)
    # 调整：采用机构中性预期13亿净利为2026E中位
    rev_e= 19.73*4 if False else 92.0  # 机构一致约90-95亿；取92
    npf_e=13.0
    rev[-1]=rev_e; npf[-1]=npf_e

    fig,ax1=plt.subplots(figsize=(11,5.5))
    fig.patch.set_facecolor("#0f0c29")
    ax1.set_facecolor("#0f0c29")
    ax1.tick_params(colors="#ddd")
    for s in ax1.spines.values(): s.set_color("#444")

    x=np.arange(len(years))
    w=0.35
    b1=ax1.bar(x-w/2,rev,w,color="#6366f1",label="营业收入(亿元)")
    ax2=ax1.twinx(); ax2.set_facecolor("#0f0c29"); ax2.tick_params(colors="#ddd")
    b2=ax2.bar(x+w/2,npf,w,color="#f59e0b",label="归母净利(亿元)")
    # 增长率折线
    rev_yoy=[np.nan]+[round((rev[i]/rev[i-1]-1)*100,1) for i in range(1,len(rev)-1)]+[np.nan]
    npf_yoy=[np.nan]+[round((npf[i]/npf[i-1]-1)*100,1) for i in range(1,len(npf)-1)]+[np.nan]
    ax2.plot(x[:-1],[npf[i] for i in range(len(years)-1)],"-o",color="#22c55e",lw=2,label="归母净利趋势")

    for i,v in enumerate(rev):
        ax1.text(i-w/2,v+1,f"{v:.1f}",ha="center",color="#c7d2fe",fontsize=9)
    for i,v in enumerate(npf):
        ax2.text(i+w/2,v+0.2,f"{v:.2f}",ha="center",color="#fcd34d",fontsize=9)
    ax1.set_xticks(x);ax1.set_xticklabels(years,color="#ddd")
    ax1.set_ylabel("营收(亿元)",color="#c7d2fe"); ax2.set_ylabel("归母净利(亿元)",color="#fcd34d")
    ax1.set_title("雅克科技 2020-2026E 营收与归母净利趋势",color="#fff",fontsize=14,pad=12)
    ax1.set_ylim(0,110); ax2.set_ylim(0,16)
    # 合并图例
    lines1,labels1=ax1.get_legend_handles_labels()
    lines2,labels2=ax2.get_legend_handles_labels()
    ax1.legend(lines1+lines2,labels1+labels2,loc="upper left",facecolor="#1e1b4b",edgecolor="#444",labelcolor="#fff",fontsize=9)
    ax1.grid(True,color="#2a2750",alpha=0.4)
    plt.tight_layout()
    p=f"{OUT}/02_finance_trend.png"
    plt.savefig(p,dpi=130,facecolor=fig.get_facecolor());plt.close()
    print("saved",p)

# ========== 图3: 2025年业务结构饼图 ==========
def chart_biz():
    labels=["LNG保温绝热材料","半导体前驱体(化学材料)","光刻胶及配套试剂","电子特气","LDS输送设备","硅微粉","阻燃剂","租赁工程/其他"]
    sizes=[27.53,24.51,22.76,4.85,3.53,3.35,3.34,10.13]
    colors=["#6366f1","#a855f7","#ec4899","#f59e0b","#22c55e","#06b6d4","#84cc16","#64748b"]
    fig,ax=plt.subplots(figsize=(10,7))
    fig.patch.set_facecolor("#0f0c29");ax.set_facecolor("#0f0c29")
    wedges,texts,autotexts=ax.pie(sizes,labels=labels,autopct="%1.2f%%",colors=colors,startangle=90,
        wedgeprops=dict(width=0.42,edgecolor="#0f0c29",linewidth=2),
        textprops=dict(color="#fff",fontsize=11))
    for at in autotexts: at.set_color("#fff");at.set_fontsize(9);at.set_weight("bold")
    ax.set_title("雅克科技 2025年营收结构（按业务板块）",color="#fff",fontsize=14,pad=20)
    plt.tight_layout()
    p=f"{OUT}/03_biz_mix.png"
    plt.savefig(p,dpi=130,facecolor=fig.get_facecolor());plt.close()
    print("saved",p)

# ========== 图4: 可比公司PE估值对比 ==========
def chart_valuation():
    companies=["雅克科技(002409)","Soulbrain(韩,前驱体)","Hansol Chemical(韩,前驱体)","默克EMD(德,前驱体)","信越化学(日)","华海诚科(环氧塑封)","安集科技(抛光液)","江丰电子(靶材)","沪硅产业(硅片)","中微公司(设备)","北方华创(设备)"]
    pe_ttm=[62.0, 18.0, 16.0, 22.0, 18.5, 260.0, 78.0, 95.0, 400.0, 55.0, 42.0]
    # 雅克当前按跌停130.5/EPS2.10算 = 62.1x
    colors=["#ef4444" if c.startswith("雅克") else ("#22c55e" if "韩" in c or "德" in c or "日" in c else "#6366f1") for c in companies]
    fig,ax=plt.subplots(figsize=(11,6))
    fig.patch.set_facecolor("#0f0c29");ax.set_facecolor("#0f0c29")
    ax.tick_params(colors="#ddd")
    for s in ax.spines.values(): s.set_color("#444")
    bars=ax.barh(companies[::-1],pe_ttm[::-1],color=colors[::-1])
    for bar,v in zip(bars,pe_ttm[::-1]):
        ax.text(v+5,bar.get_y()+bar.get_height()/2,f"{v}x",va="center",color="#fff",fontsize=10)
    ax.set_xlabel("PE(TTM) 倍",color="#ddd")
    ax.set_title("半导体材料/设备可比公司 PE(TTM) 横向对比 (2026-07-20)",color="#fff",fontsize=14,pad=12)
    ax.grid(True,axis="x",color="#2a2750",alpha=0.4)
    ax.set_xlim(0,max(pe_ttm)*1.18)
    plt.tight_layout()
    p=f"{OUT}/04_valuation.png"
    plt.savefig(p,dpi=130,facecolor=fig.get_facecolor());plt.close()
    print("saved",p)

# ========== 图5: 股价暴跌复盘时间轴 (文字+箭头) ==========
def chart_timeline():
    events=[
        ("7/1", "历史高点246.44元\n公司发异动公告:\n\"过度解读和过高预期\"\n无六氟化钨业务","#ef4444"),
        ("7/2-7/10", "高位震荡200-229\nHBM概念资金博弈\n龙虎榜机构分化","#f59e0b"),
        ("7/13", "周-跳空低开189\n获利盘集中出逃\n跌破200关口","#f59e0b"),
        ("7/15", "337-TA-1511立案\n(被告不含SK海力士/雅克)\n韩国反垄断搜查澜起韩国办\nSK海力士HBM4量产交付英伟达","#8b5cf6"),
        ("7/17", "\"黑色星期五\"\n雅克-7.05% (158→145)\n上证-3.05% 系统性风险\n两市4500+下跌","#ef4444"),
        ("7/20", "跌停封板130.50\n跌穿BOLL下轨135.5\n距高点-47%\n融资盘被动平仓风险","#dc2626"),
    ]
    fig,ax=plt.subplots(figsize=(13,5.5))
    fig.patch.set_facecolor("#0f0c29");ax.set_facecolor("#0f0c29")
    ax.set_xlim(0,10);ax.set_ylim(0,6)
    ax.axis("off")
    # 主轴
    ax.plot([0.5,9.5],[3,3],color="#6366f1",lw=3)
    for i,(d,t,c) in enumerate(events):
        x=0.5+i*1.6
        y=4.2 if i%2==0 else 1.8
        ax.plot([x,x],[3,y-0.15 if y>3 else y+0.15],color=c,lw=1.5)
        ax.scatter([x],[3],s=120,color=c,zorder=5,edgecolors="#fff",linewidths=1.2)
        ax.text(x,y,d,ha="center",color=c,fontsize=12,weight="bold")
        ax.text(x,y-0.45 if y>3 else y+0.45,t,ha="center",va="top" if y>3 else "bottom",
                color="#e5e7eb",fontsize=8.5,bbox=dict(boxstyle="round,pad=0.4",facecolor="#1e1b4b",edgecolor=c,alpha=0.85))
    ax.text(5,5.5,"雅克科技 2026年7月暴跌路径复盘时间轴 (246.44→130.50, -47%)",ha="center",color="#fff",fontsize=15,weight="bold")
    plt.tight_layout()
    p=f"{OUT}/05_timeline.png"
    plt.savefig(p,dpi=130,facecolor=fig.get_facecolor());plt.close()
    print("saved",p)

# ========== 图6: 毛利率&净利率变化 ==========
def chart_margin():
    years=["2020","2021","2022","2023","2024","2025","2026Q1"]
    gross=[30.5,26.5,28.8,29.7,30.2,30.96,31.25]
    net=[18.0,9.2,12.2,13.2,12.9,11.6,13.5]
    roe=[11.5,8.0,10.5,12.0,14.2,14.1,3.5]  # Q1单季
    fig,ax=plt.subplots(figsize=(11,5.5))
    fig.patch.set_facecolor("#0f0c29");ax.set_facecolor("#0f0c29")
    ax.tick_params(colors="#ddd")
    for s in ax.spines.values(): s.set_color("#444")
    ax.plot(years,gross,"-o",color="#6366f1",lw=2,label="毛利率(%)")
    ax.plot(years,net,"-s",color="#f59e0b",lw=2,label="归母净利率(%)")
    ax.axhline(y=30,color="#22c55e",ls="--",alpha=0.4,lw=1)
    for i,v in enumerate(gross): ax.text(i,v+0.5,f"{v}%",ha="center",color="#c7d2fe",fontsize=9)
    for i,v in enumerate(net): ax.text(i,v-1.2,f"{v}%",ha="center",color="#fcd34d",fontsize=9)
    ax.set_title("雅克科技 盈利能力变化（毛利率/净利率）",color="#fff",fontsize=14,pad=12)
    ax.set_ylim(5,35)
    ax.legend(facecolor="#1e1b4b",edgecolor="#444",labelcolor="#fff",fontsize=10)
    ax.grid(True,color="#2a2750",alpha=0.4)
    plt.tight_layout()
    p=f"{OUT}/06_margin.png"
    plt.savefig(p,dpi=130,facecolor=fig.get_facecolor());plt.close()
    print("saved",p)

if __name__=="__main__":
    chart_kline()
    chart_finance()
    chart_biz()
    chart_valuation()
    chart_timeline()
    chart_margin()
    print("ALL DONE")
