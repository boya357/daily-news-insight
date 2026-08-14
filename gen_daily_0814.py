#!/usr/bin/env python3
import sys, os, shutil, json
WORK_DIR = "/root/daily-news-insight"
sys.path.insert(0, os.path.join(WORK_DIR, "v3"))
from generators.daily_pro import DailyReportProGenerator

gen = DailyReportProGenerator(
    date_str="2026年8月14日", weekday="星期五",
    subtitle="2026年8月14日 周五 · 美股齐涨纳指+0.81%·闪迪+13.67%引爆存储·央行1万亿买断式逆回购·A股放量跌4300股·算力成唯一科技活口",
    data_dir=os.path.join(WORK_DIR, "data")
)

def rc(items):
    out = ""
    for i in items:
        c = "text-red-400" if i["up"] else "text-green-400"
        bg = "from-red-500/20 to-orange-500/10 border-red-500/20" if i["up"] else "from-green-500/20 to-emerald-500/10 border-green-500/20"
        out += '<div class="bg-gradient-to-br %s border rounded-lg p-3 text-center transition-all duration-300 hover:scale-105"><div class="text-xs text-white/60 mb-1">%s</div><div class="text-sm font-bold %s">%s</div></div>' % (bg, i["name"], c, i["change"])
    return out

def rl(items):
    out = ""
    for i in items:
        c = "text-red-400" if i["up"] else "text-green-400"
        out += '<div class="flex items-center justify-between py-2 border-b border-white/5 last:border-0"><span class="text-sm text-white/70">%s</span><span class="text-sm font-semibold %s">%s</span></div>' % (i["name"], c, i["change"])
    return out

gen.set_tldr(
    key_points=[
        "美股全线收涨：道指+0.13%、标普+0.65%、纳指+0.81%；费城半导体+0.46%进入技术性牛市；存储板块大爆发，闪迪+13.67%、海力士+9%、美光+4.23%",
        "闪迪投资者日炸裂：NAND市场2027年将达5000亿美元，2028-2030年营收中高双位数增长、毛利率约80%、FCF利润率约50%；AI推理驱动存储需求爆发",
        "央行大动作：8月14日开展10000亿元6个月期买断式逆回购（等量续作），叠加3个月期加量2000亿，8月合计净投放2000亿，配合2.77万亿政府债发行",
        "A股放量跳水：沪指-0.50%失守3940，深成指-0.87%，两市成交2.55万亿放量下跌，4300+个股下跌；机器人/有色/军工重挫，算力液冷成唯一科技活口",
        "持仓策略：雅克科技-3.67%放量大跌，铜冠铜箔-1.06%，英维克-1%，科技高位股集体回调；逢高减仓纪律不变，关注存储板块外溢机会"
    ],
    operation_advice="隔夜美股存储大爆发+央行万亿流动性呵护，今日A股或有修复但分化加剧；科技高位股继续减仓，存储材料/设备方向关注外溢机会，仓位4成防御为主",
    risk_level="中等偏高",
    suggested_position="3-4成"
)

gen.set_quick_anchors([
    {"id": "section-隔夜全球市场深度解读", "title": "全球市场", "icon": "🌍"},
    {"id": "section-A股昨日复盘与今日展望", "title": "A股复盘", "icon": "📊"},
    {"id": "section-核心题材与今日催化", "title": "核心题材", "icon": "🔥"},
    {"id": "section-持仓诊断与操作建议", "title": "持仓诊断", "icon": "💼"},
    {"id": "section-空方视角与多空博弈", "title": "空方视角", "icon": "⚖️"},
    {"id": "section-预判验证闭环", "title": "预判验证", "icon": "🔮"},
    {"id": "section-教训库引用", "title": "教训库", "icon": "📚"},
])

gen.set_holdings([
    {"name": "英维克", "code": "002837"},
    {"name": "铜冠铜箔", "code": "301217"},
    {"name": "雅克科技", "code": "002409"},
    {"name": "*ST建艺", "code": "002789"},
])

gen.set_og(description="每日新闻洞察 2026年8月14日：美股齐涨纳指+0.81%、闪迪+13.67%引爆存储、央行1万亿买断式逆回购、A股放量跌4300股")

gen.add_global_market()
