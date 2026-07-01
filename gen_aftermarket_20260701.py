#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""盘后速递生成脚本 - 2026-07-01"""
import sys, os, json
sys.path.insert(0, '/root/daily-news-insight')
os.chdir('/root/daily-news-insight')

from v3.generators.aftermarket import AftermarketGenerator
from components.layout import Section

# ===== Load Data =====
with open('data/market.json', 'r', encoding='utf-8') as f:
    market = json.load(f)
with open('data/portfolio.json', 'r', encoding='utf-8') as f:
    portfolio = json.load(f)
with open('data/longhubang_market.json', 'r', encoding='utf-8') as f:
    lhb = json.load(f)

DATE = "20260701"
subtitle = "2026年7月1日 \u00b7 下半年开门红极致高低切，大金融崛起科技集体回调"

gen = AftermarketGenerator(date_str=DATE, subtitle=subtitle)

# ===== 1. Today Highlight =====
gen.add_today_highlight(
    "\U0001f525 下半年首日极致分化！沪指涨0.44%站稳4100点，创业板指跌1.89%、科创50暴跌2.48%。"
    "全市场超4300只个股上涨、226家涨停，成交3.66万亿放量3862亿创阶段天量\u2014\u2014资金从高位算力/储能/CPO大举撤退，"
    "券商保险大金融、养殖、医药、化工等低位板块全线爆发，典型\u300c高切低、成长切价值\u300d行情。"
    "雅克科技+5.16%续创历史新高，龙虎榜机构净买入2.82亿！多氟多4连板，龙虎榜净买入17.86亿霸榜。"
)

# ===== 2. Market Summary =====
indices_data = []
for idx in market['indices']:
    change_pct = idx['change_pct'] * 100
    sign = '+' if change_pct >= 0 else ''
    indices_data.append({
        'name': idx['name'],
        'value': f"{idx['price']:.2f}",
        'change': f"{sign}{change_pct:.2f}%",
        'up': idx['up'],
        'icon': 'trending_up' if idx['up'] else 'trending_down'
    })
gen.add_market_summary(
    indices=indices_data,
    volume="3.66\u4e07\u4ebf\uff08\u653e\u91cf3862\u4ebf\uff09",
    northbound="\u5f85\u66f4\u65b0"
)

# ===== 3. Sentiment Thermometer =====
gen.add_sentiment_thermometer(
    temperature=38,
    volume="3.66\u4e07\u4ebf",
    up_count="4329\u53ea\u2191",
    down_count="1145\u53ea\u2193",
    limit_up_count=226
)

# ===== 4. Sector Performance =====
up_sectors = [
    {"name": "\u4fdd\u9669", "change": "+7.09%"},
    {"name": "\u8bc1\u5238", "change": "+6.52%"},
    {"name": "\u517b\u6b96\u4e1a", "change": "+5.87%"},
    {"name": "\u533b\u836f/\u521b\u65b0\u836f", "change": "+4.23%"},
    {"name": "\u6c1f\u5316\u5de5", "change": "+4.15%"},
    {"name": "\u7164\u70ad/\u5316\u5de5", "change": "+2.34%"},
]
down_sectors = [
    {"name": "\u5149\u901a\u4fe1/CPO", "change": "-5.23%"},
    {"name": "\u50a8\u80fd/\u9006\u53d8\u5668", "change": "-4.87%"},
    {"name": "PCB/\u5149\u7ea4", "change": "-3.55%"},
    {"name": "\u534a\u5bfc\u4f53/\u7b97\u529b", "change": "-2.48%"},
    {"name": "\u5149\u4f0f\u8bbe\u5907", "change": "-2.31%"},
    {"name": "\u7535\u529b\u8bbe\u5907", "change": "-1.46%"},
]
gen.add_sector_performance(up_sectors=up_sectors, down_sectors=down_sectors)

# ===== 5. Deep Analysis =====
strong_sectors = [
    {"name": "\u5927\u91d1\u878d\uff08\u8bc1\u5238+\u4fdd\u9669\uff09", "reason": "\u4e2d\u8bc1\u534f\u51fa\u53f0\u8bc1\u5238\u4e94\u5927\u9886\u57df\u4e13\u9879\u8bc4\u4ef7\u529e\u6cd5\uff1b\u4e0a\u534a\u5e74A\u80a1\u6210\u4ea4\u521b\u5386\u53f2\u65b0\u9ad8\uff0c\u8bc1\u5238\u5546\u4e8c\u5b63\u5ea6\u4e1a\u7ee9\u9884\u671f\u4e0a\u8c03\uff1b\u4fdd\u9669\u677f\u5757\u4f30\u503c\u8fd15\u5e74\u5e95\u90e8\uff0c\u4e3b\u529b\u51c0\u6d41\u5165\u8bc1\u523890.55\u4ebf\u3001\u4fdd\u966942.1\u4ebf\uff0c\u5929\u98ce/\u56fd\u76db/\u534e\u5b89\u8bc1\u5238\u6da8\u505c\uff0c\u65b0\u534e\u4fdd\u9669\u76d8\u4e2d\u5c01\u677f\u3002"},
    {"name": "\u755c\u79bd\u517b\u6b96\uff08\u732a/\u9e21\uff09", "reason": "\u767d\u7fbd\u9e21\u3001\u751f\u732a\u8fdb\u5165\u5468\u671f\u4e0a\u884c\u901a\u9053\uff0c\u591a\u5bb6\u517b\u6b96\u4f01\u4e1a\u4e2d\u62a5\u9884\u589e\uff0c\u76ca\u751f\u80a1\u4efd\u3001\u65b0\u5e0c\u671b\u3001\u50b2\u519c\u751f\u7269\u6da8\u505c\uff0c\u4e3b\u529b\u51c0\u6d41\u516537.6\u4ebf\u3002"},
    {"name": "\u6c1f\u5316\u5de5/\u57fa\u7840\u5316\u5de5", "reason": "\u626c\u6770\u79d1\u6280\u5ba3\u5e03\u5168\u7cfb\u5217\u4ea7\u54c17\u67081\u65e5\u8d77\u6da8\u4ef710-15%\uff1b\u591a\u6c1f\u591a4\u8fde\u677f\uff08\u7535\u5b50\u7ea7\u6c22\u6c1f\u9178\u6982\u5ff5\uff09\uff0c\u660a\u534e\u79d1\u6280\u83b7\u5927\u989d\u8d44\u91d1\u4e70\u5165\uff0c\u5316\u5de5\u5408\u8ba1\u51c0\u6d41\u516568.3\u4ebf\u3002"},
    {"name": "\u521b\u65b0\u836f/\u533b\u836f", "reason": "\u5348\u540e\u5168\u7ebf\u62c9\u5347\uff0c20CM\u6da8\u505c\u4e2a\u80a1\u96c6\u4e2d\uff0c\u4e3b\u529b\u51c0\u6d41\u516529.8\u4ebf\uff0c\u677f\u5757\u8f6e\u52a8\u8865\u6da8\u7279\u5f81\u660e\u663e\u3002"},
]
weak_sectors = [
    {"name": "\u5149\u901a\u4fe1/CPO/\u5149\u6a21\u5757", "reason": "\u4e0a\u534a\u5e74\u6700\u5f3a\u4e3b\u7ebf\u906d\u9047\u96c6\u4e2d\u5151\u73b0\uff0c\u51c0\u6d41\u51fa112.6\u4ebf\u5c45\u9996\u3002\u534e\u5de5\u79d1\u6280(-9.11%)\u9886\u8dcc\uff0c\u5317\u5411\u8fde\u7eed\u51cf\u6301\uff0c\u673a\u6784\u83b7\u5229\u4e86\u7ed3\u3002"},
    {"name": "\u50a8\u80fd/\u9006\u53d8\u5668", "reason": "\u51c0\u6d41\u51fa87.2\u4ebf\uff0c\u9633\u5149\u7535\u6e90\u5355\u65e5\u66b4\u8dcc-13.18%\uff0c\u6d77\u5916\u50a8\u80fd\u8ba2\u5355\u589e\u901f\u653e\u7f13\u9884\u671f\u5f15\u53d1\u6050\u614c\u629b\u552e\uff0c\u516c\u52df\u4fdd\u9669\u51cf\u4ed3\u3002"},
    {"name": "\u7b97\u529b\u82af\u7247/\u534a\u5bfc\u4f53\u9ad8\u4f4d", "reason": "\u5bd2\u6b66\u7eaa\u66b4\u8dcc-10.35%\u51c0\u6d41\u51fa16.23\u4ebf\uff0c\u6df1\u79d1\u6280-8.43%\u51c0\u6d41\u51fa23.28\u4ebf\uff0c\u4f70\u7ef4\u5b58\u50a8-12.63%\u51c0\u6d41\u51fa20.55\u4ebf\u3002\u592e\u884c\u5355\u65e5\u51c0\u56de\u7b3c1.16\u4e07\u4ebf\u6d41\u52a8\u6027\uff0c\u9ad8\u4f30\u503c\u627f\u538b\u3002"},
    {"name": "PCB/\u5149\u7ea4", "reason": "\u8d44\u91d1\u4ecePCB\u4e0a\u6e38\u64a4\u9000\uff08\u9f99\u864e\u699c\u4e2d\u5c71\u4e1c\u8def\u5356\u8054\u5f97\u88c5\u5907\u3001\u7ea2\u677f\u79d1\u6280\uff09\uff0c\u5411PCB\u4e2d\u6e38\u548c\u534a\u5bfc\u4f53\u8bbe\u5907\u5207\u6362\uff0c\u677f\u5757\u6574\u4f53\u56de\u8c03\u3002"},
]
core_view = (
    "7\u67081\u65e5\u662f\u4e0b\u534a\u5e74\u884c\u60c5\u7684\u5206\u6c34\u5cad\u3002\u6781\u81f4\u9ad8\u4f4e\u5207\u6362\u7684\u672c\u8d28\u539f\u56e0\u6709\u4e09\uff1a\u2460\u534a\u5e74\u5ea6\u8003\u6838\u7ed3\u675f\uff0c\u673a\u6784\u8c03\u4ed3\u6362\u80a1\u4ece\u9ad8\u4f4d\u79d1\u6280\u5411\u4f4e\u4f4d\u4f4e\u4f30\u503c\u5207\u6362\uff1b"
    "\u2461\u592e\u884c\u5355\u65e5\u51c0\u56de\u7b3c1.16\u4e07\u4ebf\u6d41\u52a8\u6027\uff0c\u9ad8\u4f30\u503c\u6210\u957f\u80a1\u9996\u5f53\u5176\u51b2\uff1b"
    "\u24627\u6708\u8fdb\u5165\u4e2d\u62a5\u4e1a\u7ee9\u9a8c\u8bc1\u671f\uff0c\u5e02\u573a\u4ece\u300c\u7092\u9884\u671f\u300d\u8f6c\u5411\u300c\u770b\u5151\u73b0\u300d\uff0c\u9ad8\u4f4d\u79d1\u6280\u80a1\u9762\u4e34\u4e1a\u7ee9\u4e0e\u4f30\u503c\u53cc\u6740\u98ce\u9669\u3002"
    "\u5173\u952e\u4fe1\u53f7\uff1a\u4e2d\u5c71\u4e1c\u8def4.32\u4ebf\u91cd\u4ed3\u534a\u5bfc\u4f53\u8bbe\u5907+PCB\u4e2d\u6e38\uff08\u8d85\u58f0\u7535\u5b501.085\u4ebf+\u5148\u5bfc\u57fa\u75353.236\u4ebf\uff09\uff0c"
    "\u540c\u65f6\u5356\u51faPCB\u4e0a\u6e38\u8bbe\u5907\u8054\u5f97\u88c5\u5907\u8fd11\u4ebf\u2014\u2014\u8bf4\u660e7\u6708\u65b0\u4e3b\u7ebf\u4e0d\u662f\u300cAI\u7b97\u529b\u5168\u9762\u64a4\u9000\u300d\uff0c\u800c\u662f\u300c\u79d1\u6280\u5185\u90e8\u4ece\u786c\u4ef6\u7092\u9884\u671f\u2192\u8bbe\u5907+\u6750\u6599\u56fd\u4ea7\u66ff\u4ee3\u300d\u7684\u7eb5\u6df1\u5207\u6362\u3002"
    "\u96c5\u514b\u79d1\u6280+5.16%\u521b\u5386\u53f2\u65b0\u9ad8\u4e14\u9f99\u864e\u699c\u673a\u6784\u51c0\u4e70\u51652.82\u4ebf\uff0c\u5370\u8bc1HBM/\u534a\u5bfc\u4f53\u6750\u6599\u4ecd\u662f\u8d44\u91d1\u8ba4\u53ef\u7684\u65b9\u5411\u3002"
    "\u6301\u4ed3\u65b9\u9762\uff1a\u94dc\u51a0\u94dc\u7b94\u9ad8\u4f4d\u9707\u8361-0.14%\uff0cHVLP\u94dc\u7b94\u903b\u8f91\u672a\u7834\uff1b\u96c5\u514b\u79d1\u6280\u4e3b\u5347\u6d6a\u5ef6\u7eed\uff0c\u56de\u8e295\u65e5\u7ebf(215-220)\u518d\u51b3\u7b56\uff1b"
    "\u82f1\u7ef4\u514b\u66b4\u8dcc-6.07%\u521b\u65b0\u4f4e74\u5143\uff0c\u7834\u6b62\u635f-28%\uff0c\u9022\u9ad8\u575a\u51b3\u51cf\u4ed3\uff1b*ST\u5efa\u827a+3.90%\u653612\u5143\u4ecd\u7834\u6b62\u635f\uff0c7/6\u6da8\u8dcc\u5e45\u6269\u81f310%\uff0c\u53cd\u62bd\u79bb\u573a\u3002"
)
gen.add_market_deep_analysis(strong_sectors=strong_sectors, weak_sectors=weak_sectors, core_view=core_view)

# ===== 6. LHB Overview =====
lhb_overview_html = '''
<div style="background: white; padding: 24px; border: 1px solid rgba(0,0,0,0.06); border-radius: 16px; box-shadow: 0 2px 8px rgba(0,0,0,0.04);">
    <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 12px; margin-bottom: 16px;">
        <div style="text-align: center; padding: 12px; background: #f8fafc; border-radius: 10px;">
            <div style="font-size: 20px; font-weight: 800; color: #374151;">100\u53ea</div>
            <div style="font-size: 12px; color: #9ca3af; margin-top: 4px;">\u4e0a\u699c\u4e2a\u80a1</div>
        </div>
        <div style="text-align: center; padding: 12px; background: #f8fafc; border-radius: 10px;">
            <div style="font-size: 20px; font-weight: 800; color: #ef4444;">57.67\u4ebf</div>
            <div style="font-size: 12px; color: #9ca3af; margin-top: 4px;">\u9f99\u864e\u699c\u51c0\u4e70</div>
        </div>
        <div style="text-align: center; padding: 12px; background: #f8fafc; border-radius: 10px;">
            <div style="font-size: 20px; font-weight: 800; color: #f59e0b;">33\u4e70/20\u5356</div>
            <div style="font-size: 12px; color: #9ca3af; margin-top: 4px;">\u673a\u6784\u52a8\u5411</div>
        </div>
        <div style="text-align: center; padding: 12px; background: #f8fafc; border-radius: 10px;">
            <div style="font-size: 20px; font-weight: 800; color: #2563eb;">\u9ad8\u4f4e\u5207\u6362</div>
            <div style="font-size: 12px; color: #9ca3af; margin-top: 4px;">\u6e38\u8d44\u98ce\u683c</div>
        </div>
    </div>
    <div style="background: linear-gradient(135deg, #fef3c7 0%, #fef9c3 100%); border-radius: 12px; padding: 16px; border: 1px solid rgba(245,158,11,0.2);">
        <div style="font-size: 14px; font-weight: 700; color: #92400e; margin-bottom: 8px;">\U0001f3af \u6e38\u8d44\u6838\u5fc3\u52a8\u5411</div>
        <div style="font-size: 13px; color: #78350f; line-height: 1.8;">
            <strong>\u4e2d\u5c71\u4e1c\u8def4.32\u4ebf</strong>\u6210\u4e3a\u7edd\u5bf9\u4e3b\u89d2\uff1a\u4e70\u8d85\u58f0\u7535\u5b501.085\u4ebf(PCB\u4e2d\u6e38)+\u4e70\u5148\u5bfc\u57fa\u75353.236\u4ebf(\u534a\u5bfc\u4f53\u8bbe\u5907)-\u5356\u8054\u5f97\u88c5\u59070.98\u4ebf(PCB\u4e0a\u6e38)\u2192\u8d44\u91d1\u62bc\u6ce8\u534a\u5bfc\u4f53\u8bbe\u5907\u56fd\u4ea7\u66ff\u4ee3+PCB\u4e2d\u6e38\u5236\u9020<br>
            <strong>AI\u7b97\u529b\u64a4\u9000</strong>\uff1a\u4f5b\u5c71\u7cfb\u5356\u5929\u5a31\u6570\u79d11.17\u4ebf+\u7389\u5170\u8def\u53566451\u4e07\uff0c\u5408\u8ba11.82\u4ebf\u7529\u5356AI\u7b97\u529b\u4ee3\u8868\u80a1\uff0c\u64a4\u9000\u4fe1\u53f7\u660e\u786e<br>
            <strong>\u4f5c\u624b\u65b0\u4e001.45\u4ebf</strong>\u5207\u5316\u5de5/\u6750\u6599\uff1a\u4e2d\u5a01\u7535\u5b509051\u4e07+\u5929\u5bcc\u80fd\u6e905465\u4e07\uff0c\u4f4e\u4f4d\u5c0f\u7968\u9ad8\u4f4e\u5207<br>
            <strong>\u7ae0\u76df\u4e3b+\u6e56\u91cc\u5927\u90533665\u4e07</strong>\u53cc\u5e2d\u4f4d\u8054\u52a8\u4e70\u6d77\u5357\u6d77\u836f(\u6d77\u5357\u81ea\u8d38\u6982\u5ff5)
        </div>
    </div>
</div>
'''
gen._components.append(Section(title="\U0001f409 \u9f99\u864e\u699c\u7efc\u8ff0", content=lhb_overview_html, icon="award"))

# ===== LHB Stocks =====
lhb_stocks = [
    {"name": "\u591a\u6c1f\u591a", "code": "002407", "change": "+9.99%", "up": True, "reason": "8\u59294\u677f/\u7535\u5b50\u7ea7\u6c22\u6c1f\u9178/\u673a\u6784\u51c0\u4e7010.67\u4ebf/\u51c0\u4e7017.86\u4ebf\u9738\u699c", "net_buy": "17.86\u4ebf", "institutions": 1},
    {"name": "\u660a\u534e\u79d1\u6280", "code": "600378", "change": "+7.46%", "up": True, "reason": "\u6c1f\u5316\u5de5/\u7535\u5b50\u7279\u6c14/\u673a\u6784\u51c0\u4e705.36\u4ebf/\u4e09\u65e5\u699c", "net_buy": "7.59\u4ebf", "institutions": 1},
    {"name": "\u4e1c\u65b9\u9506\u4e1a", "code": "002167", "change": "+10.01%", "up": True, "reason": "\u9506\u82f1\u7802\u6da8\u4ef7/\u56fa\u6001\u7535\u6c60\u7535\u89e3\u8d28/\u957f\u6c5f\u5b89\u5fbd1.60\u4ebf", "net_buy": "3.70\u4ebf", "institutions": 1},
    {"name": "\u9510\u6377\u7f51\u7edc", "code": "301165", "change": "+6.80%", "up": True, "reason": "AI\u7f51\u7edc\u8bbe\u5907/\u673a\u6784\u51c0\u4e703.17\u4ebf/\u4e2d\u5c71\u4e1c\u8def\u53c2\u4e0e", "net_buy": "3.60\u4ebf", "institutions": 1},
    {"name": "\u683c\u79d1\u5fae", "code": "688728", "change": "+20.01%", "up": True, "reason": "2\u8fde\u677f20CM/CIS\u82af\u7247/2\u4ebf\u50cf\u7d20\u6982\u5ff5(\u6f84\u6e05\u672a\u51fa\u8d27)", "net_buy": "3.79\u4ebf", "institutions": 1},
    {"name": "\u96c5\u514b\u79d1\u6280", "code": "002409", "change": "+5.16%", "up": True, "reason": "HBM\u524d\u9a71\u4f53\u9f99\u5934/\u7eed\u521b\u5386\u53f2\u65b0\u9ad8/\u6301\u4ed3\u80a1", "net_buy": "\u673a\u6784\u51c0\u4e702.82\u4ebf", "institutions": 1},
]
gen.add_dragon_tiger_list(lhb_stocks)

# ===== 7. Portfolio =====
stocks_html = '<div style="display: flex; flex-direction: column; gap: 14px;">'
for s in portfolio.get('stocks', []):
    change = s.get('today_change', 0) * 100
    sign = '+' if change >= 0 else ''
    change_color = '#ef4444' if change >= 0 else '#10b981'
    price = s.get('current_price', 0)
    cost = s.get('cost_price', 0)
    pnl = (price - cost) / cost * 100
    pnl_sign = '+' if pnl >= 0 else ''
    pnl_color = '#ef4444' if pnl >= 0 else '#10b981'
    risk_map = {
        '\u9ad8\u5371\u533a - \u6df1\u5ea6\u7834\u6b62\u635f': '#ef4444',
        '\u9ad8\u5371\u533a - \u7834\u6b62\u635f': '#f97316',
        '\u5b89\u5168\u533a - \u5927\u5e45\u6d6e\u76c8': '#10b981',
        '\u4e3b\u5347\u6d6a - \u8d8b\u52bf\u8ddf\u8e2a': '#ec4899'
    }
    risk_level = s.get('risk_level', '')
    risk_color = risk_map.get(risk_level, '#6b7280')
    advice = s.get('advice', {})
    advice_color = '#ef4444' if advice.get('type') == 'reduce' else '#10b981'
    stocks_html += f'''
    <div style="background: rgba(255,255,255,0.7); backdrop-filter: blur(10px); border-radius: 14px; padding: 18px; border: 1px solid rgba(0,0,0,0.06);">
        <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 10px;">
            <div>
                <span style="font-size: 17px; font-weight: 700; color: #1f2937;">{s['name']}</span>
                <span style="font-size: 12px; color: #9ca3af; margin-left: 6px;">{s['code']}</span>
                <span style="font-size: 11px; padding: 2px 8px; border-radius: 10px; background: {risk_color}22; color: {risk_color}; margin-left: 8px;">{risk_level}</span>
            </div>
            <div style="text-align: right;">
                <div style="font-size: 20px; font-weight: 800; color: {change_color};">{sign}{change:.2f}%</div>
                <div style="font-size: 12px; color: #9ca3af;">{price:.2f}\u5143</div>
            </div>
        </div>
        <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 8px; margin-bottom: 12px;">
            <div style="text-align: center; padding: 8px; background: #f8fafc; border-radius: 8px;">
                <div style="font-size: 11px; color: #9ca3af;">\u6210\u672c</div>
                <div style="font-size: 14px; font-weight: 600; color: #374151;">{cost:.2f}\u5143</div>
            </div>
            <div style="text-align: center; padding: 8px; background: #f8fafc; border-radius: 8px;">
                <div style="font-size: 11px; color: #9ca3af;">\u6d6e\u52a8\u76c8\u4e8f</div>
                <div style="font-size: 14px; font-weight: 600; color: {pnl_color};">{pnl_sign}{pnl:.2f}%</div>
            </div>
            <div style="text-align: center; padding: 8px; background: #f8fafc; border-radius: 8px;">
                <div style="font-size: 11px; color: #9ca3af;">\u6b62\u635f\u4f4d</div>
                <div style="font-size: 14px; font-weight: 600; color: #374151;">{s.get('stop_loss_price', 0):.2f}\u5143</div>
            </div>
        </div>
        <div style="background: {advice_color}11; border-left: 3px solid {advice_color}; padding: 10px 14px; border-radius: 0 8px 8px 0; font-size: 13px; color: #374151; line-height: 1.6;">
            <strong style="color: {advice_color};">{advice.get('type_label', '')}\uff1a</strong>{advice.get('text', '')}
        </div>
    </div>'''
stocks_html += '</div>'
gen._components.append(Section(title="\U0001f4bc \u6301\u4ed3\u80a1\u8ffd\u8e2a", content=stocks_html, icon="briefcase"))

# ===== 8. Evening News =====
evening_news = [
    {"title": "\u592e\u884c\u5355\u65e5\u51c0\u56de\u7b3c1.16\u4e07\u4ebf\uff0c\u6d41\u52a8\u6027\u9636\u6bb5\u6027\u6536\u7d27", "content": "7\u67081\u65e5\u592e\u884c\u5f00\u5c551000\u4ebf\u9006\u56de\u8d2d\uff0c\u5f53\u65e5\u67096625\u4ebf7\u5929\u9006\u56de\u8d2d+6000\u4ebf\u9694\u591c\u9006\u56de\u8d2d\u5230\u671f\uff0c\u5355\u65e5\u51c0\u56de\u7b3c1.16\u4e07\u4ebf\u5143\u3002\u77ed\u671f\u6d41\u52a8\u6027\u6536\u7d27\u662f\u4eca\u65e5\u9ad8\u4f4d\u79d1\u6280\u80a1\u96c6\u4f53\u56de\u8c03\u7684\u91cd\u8981\u50ac\u5316\u5242\uff0c\u9ad8\u4f30\u503c\u6210\u957f\u677f\u5757\u627f\u538b\u660e\u663e\u3002", "time": "20:00", "source": "\u592e\u884c\u516c\u5f00\u5e02\u573a", "tag": "\u5b8f\u89c2", "tag_variant": "danger"},
    {"title": "\u516b\u90e8\u95e8\u8054\u5408\u5370\u53d1\u300a\u5173\u4e8e\u63a8\u52a8\u5de5\u4e1a\u4e92\u8054\u7f51\u9ad8\u8d28\u91cf\u53d1\u5c55\u7684\u5b9e\u65bd\u610f\u89c1\u300b", "content": "\u63d0\u51fa\u52302030\u5e74\u5efa\u8bbe5\u4e07\u5f20\u5de5\u4e1a5G\u4e13\u7f51\uff0c\u6253\u90205\u4e2a\u5de6\u53f3\u5177\u6709\u56fd\u9645\u5f71\u54cd\u529b\u7684\u7efc\u5408\u578b\u5e73\u53f0\uff0c\u6838\u5fc3\u4ea7\u4e1a\u589e\u52a0\u503c\u7a81\u78342.5\u4e07\u4ebf\u5143\u3002\u5de5\u4e1a\u4e92\u8054\u7f51\u5e73\u53f0\u3001\u5de5\u4e1a\u8f6f\u4ef6\u3001\u5de5\u4e1a5G\u4e13\u7f51\u8bbe\u5907\u3001\u5de5\u4e1a\u4f20\u611f\u5668\u7b49\u65b9\u5411\u8fce\u6765\u7cfb\u7edf\u6027\u653f\u7b56\u50ac\u5316\u3002", "time": "18:30", "source": "\u5de5\u4fe1\u90e8", "tag": "\u653f\u7b56", "tag_variant": "primary"},
    {"title": "\u591a\u6c1f\u591a\u53d1\u5e03\u98ce\u9669\u63d0\u793a\uff1a\u534a\u5bfc\u4f53\u7ea7\u6c22\u6c1f\u9178\u8425\u6536\u5360\u6bd4\u4e0d\u8db32%\uff0c\u65e0\u516d\u6c1f\u5316\u94a8\u4ea7\u7ebf", "content": "8\u59294\u677f\u591a\u6c1f\u591a\u516c\u544a\u79f0\uff0c2025\u5e74\u5ea6\u53ca2026\u5e74Q1\u534a\u5bfc\u4f53\u7ea7\u6c22\u6c1f\u9178\u4ea7\u54c1\u9500\u552e\u989d\u5360\u8425\u6536\u4e0d\u8db32%\uff0c\u6ca1\u6709\u516d\u6c1f\u5316\u94a8\u751f\u4ea7\u7ebf\uff0c\u672a\u7b7e\u7f72\u5b9e\u8d28\u6027\u8ba2\u5355\u534f\u8bae\u3002\u8fde\u7eed10\u4e2a\u4ea4\u6613\u65e5\u7d2f\u8ba1\u6da840.48%\uff0c\u5b58\u5728\u975e\u7406\u6027\u7092\u4f5c\u98ce\u9669\uff0c\u77ed\u671f\u56de\u843d\u98ce\u9669\u5927\u3002", "time": "19:00", "source": "\u516c\u53f8\u516c\u544a", "tag": "\u98ce\u9669", "tag_variant": "danger"},
    {"title": "\u626c\u6770\u79d1\u6280\uff1a\u5168\u7cfb\u5217\u4ea7\u54c1\u6da8\u4ef710%-15%\uff0c7\u67081\u65e5\u8d77\u6267\u884c", "content": "\u53d7\u4e0a\u6e38\u82af\u7247\u6676\u5706\u3001\u5927\u5b97\u91d1\u5c5e\u3001\u5c01\u88c5\u539f\u6750\u6599\u5168\u7ebf\u6301\u7eed\u6da8\u4ef7\u5f71\u54cd\uff0c\u626c\u6770\u79d1\u6280\u51b3\u5b9a\u5bf9\u5168\u7cfb\u5217\u4ea7\u54c1\u4ef7\u683c\u8c03\u657410%-15%\uff0c7\u67081\u65e5\u8d77\u51fa\u8d27\u6b63\u5f0f\u6267\u884c\u3002\u534a\u5bfc\u4f53\u529f\u7387\u5668\u4ef6\u6da8\u4ef7\u5468\u671f\u542f\u52a8\u4fe1\u53f7\u660e\u786e\u3002", "time": "18:00", "source": "\u673a\u6784\u8c03\u7814", "tag": "\u884c\u4e1a", "tag_variant": "success"},
    {"title": "6\u6708\u5236\u9020\u4e1aPMI\u5f55\u5f9750.3%\uff0c\u91cd\u8fd4\u6269\u5f20\u533a\u95f4", "content": "6\u6708\u5236\u9020\u4e1aPMI\u8f83\u4e0a\u6708\u56de\u53470.3\u4e2a\u767e\u5206\u70b9\u81f350.3%\uff0c\u91cd\u8fd4\u6269\u5f20\u533a\u95f4\uff0c\u9ad8\u4e8e\u5e02\u573a\u9884\u671f\u3002\u65b0\u8ba2\u5355\u6307\u6570\u5927\u5e45\u4e0a\u884c\u662f\u9996\u8981\u8d21\u732e\u9879\uff0c\u9ad8\u6280\u672f\u5236\u9020\u4e1a\u548c\u88c5\u5907\u5236\u9020\u4e1a\u666f\u6c14\u5ea6\u4e0a\u884c\u30027\u6708\u8fdb\u5165\u653f\u7b56\u4e0e\u57fa\u672c\u9762\u5173\u952e\u9a8c\u8bc1\u671f\u3002", "time": "09:00", "source": "\u56fd\u5bb6\u7edf\u8ba1\u5c40", "tag": "\u5b8f\u89c2", "tag_variant": "success"},
    {"title": "\u683c\u79d1\u5fae\u6f84\u6e05\uff1a2\u4ebf\u50cf\u7d20\u4ea7\u54c1\u5c1a\u672a\u5f62\u6210\u5ba2\u6237\u4ea7\u54c1\u51fa\u8d27", "content": "2\u8fde\u677f\u683c\u79d1\u5fae\u53d1\u5e03\u98ce\u9669\u63d0\u793a\u516c\u544a\uff0c2\u4ebf\u50cf\u7d20\u4ea7\u54c1\u5f00\u53d1\u987a\u5229\u5e76\u4e0e\u90e8\u5206\u5ba2\u6237\u8fbe\u6210\u521d\u6b65\u5408\u4f5c\u610f\u5411\uff0c\u4f46\u5c1a\u672a\u5f62\u6210\u5ba2\u6237\u4ea7\u54c1\u51fa\u8d27\uff1b\u4e34\u6e2f\u5de5\u5382\u76ee\u524d\u4e3b\u8981\u751f\u4ea7\u9ad8\u7aefCIS\u4ea7\u54c1\u3002\u76f8\u5173\u5e02\u573a\u673a\u6784\u4f20\u64ad\u4fe1\u606f\u975e\u516c\u53f8\u5b9e\u9645\u7ecf\u8425\u8fdb\u5ea6\u3002", "time": "19:20", "source": "\u516c\u53f8\u516c\u544a", "tag": "\u98ce\u9669", "tag_variant": "warning"},
    {"title": "\u4ebf\u7530\u667a\u80fd\uff1a1.13\u4ebf\u5143\u7b97\u529b\u670d\u52a1\u5408\u540c\u7ec8\u6b62", "content": "\u5168\u8d44\u5b50\u516c\u53f8\u7518\u8083\u4ebf\u7b97\u4e0e\u65e0\u95ee\u82af\u7a79\u7b7e\u7f72\u76841.13\u4ebf\u5143\u7b97\u529b\u670d\u52a1\u9879\u76ee\u5408\u540c\uff0c\u56e0\u91c7\u8d2d\u65b9\u4e1a\u52a1\u5ba2\u89c2\u53d8\u5316\uff0c\u53cc\u65b9\u4e00\u81f4\u7b7e\u8ba2\u7ec8\u6b62\u534f\u8bae\u3002AI\u7b97\u529b\u79df\u8d41\u6982\u5ff5\u964d\u6e29\u7684\u53c8\u4e00\u4fe1\u53f7\u3002", "time": "19:10", "source": "\u516c\u53f8\u516c\u544a", "tag": "\u516c\u53f8", "tag_variant": "danger"},
    {"title": "\u591a\u5bb6\u516c\u53f8\u64a4\u9500ST/\u6458\u5e3d\uff1a*ST\u91d1\u79d1\u2192\u91d1\u79d1\u80a1\u4efd\u3001*ST\u5b9d\u5b9e\u2192\u5b9d\u5854\u5b9e\u4e1a\u3001ST\u901a\u8109\u2192\u4e2d\u901a\u56fd\u8109", "content": "*ST\u91d1\u79d1\u3001*ST\u5b9d\u5b9e7\u67081\u65e5\u505c\u724c1\u5929\uff0c7\u67082\u65e5\u590d\u724c\u64a4\u9500\u9000\u5e02\u98ce\u9669\u8b66\u793a\u5e76\u6da8\u8dcc\u5e45\u6269\u81f310%\uff1bST\u901a\u8109\u540c\u6837\u64a4\u9500\u5176\u4ed6\u98ce\u9669\u8b66\u793a\u53d8\u66f4\u4e3a\u4e2d\u901a\u56fd\u8109\u3002", "time": "07:42", "source": "\u6caa\u6df1\u4ea4\u6613\u6240", "tag": "\u516c\u544a", "tag_variant": "default"},
]
gen.add_evening_news(evening_news)

# ===== 9. Earnings Forecast =====
gen.add_earnings_forecast()

# ===== 10. Tomorrow Prediction =====
predictions = [
    {"name": "\u5927\u91d1\u878d\uff08\u8bc1\u5238/\u4fdd\u9669\uff09", "direction": "\u770b\u6da8", "confidence": 70, "reason": "\u8bc1\u5238\u677f\u5757\u653e\u91cf\u5927\u6da8+\u4e3b\u529b\u51c0\u6d41\u516590\u4ebf\uff0c\u5929\u98ce/\u56fd\u76db/\u534e\u5b89\u6da8\u505c\u3002\u534a\u5e74\u672b\u8003\u6838\u7ed3\u675f+\u6210\u4ea4\u653e\u91cf\u5927+\u4e1a\u7ee9\u9884\u671f\u4e0a\u4fee\uff0c\u8bc1\u5238\u4f5c\u4e3a\u725b\u5e02\u65d7\u624b\u6709\u671b\u5ef6\u7eed\u3002\u4f46\u9996\u65e5\u7206\u53d1\u540e\u6b21\u65e5\u5206\u5316\u6982\u7387\u5927\uff0c\u5173\u6ce8\u524d\u6392\u9f99\u5934\u5ef6\u7eed\u6027\u3002\u4fdd\u9669\u677f\u5757\u4f30\u503c\u5e95\u90e8\uff0c\u65b0\u534e\u4fdd\u9669\u5c01\u677f\uff0c\u8865\u6da8\u7a7a\u95f4\u4ecd\u5728\u3002"},
    {"name": "\u534a\u5bfc\u4f53\u8bbe\u5907/\u6750\u6599", "direction": "\u770b\u6da8", "confidence": 72, "reason": "\u9f99\u864e\u699c\u4e2d\u5c71\u4e1c\u8def4.32\u4ebf\u91cd\u4ed3\u534a\u5bfc\u4f53\u8bbe\u5907\uff08\u5148\u5bfc\u57fa\u75353.23\u4ebf+\u8d85\u58f0\u7535\u5b501.085\u4ebf\uff09\uff0c\u96c5\u514b\u79d1\u6280\u673a\u6784\u51c0\u4e70\u51652.82\u4ebf\u521b\u5386\u53f2\u65b0\u9ad8\uff0cHBM/\u524d\u9a71\u4f53/\u534a\u5bfc\u4f53\u8bbe\u5907\u56fd\u4ea7\u66ff\u4ee3\u662f7\u6708\u65b0\u4e3b\u7ebf\u3002\u97e9\u56fd800\u4e07\u4ebf\u97e9\u5143\u534a\u5bfc\u4f53\u6269\u4ea7\u8ba1\u5212+\u5168\u7403\u82af\u72477/1\u6da8\u4ef7+\u957f\u946b295\u4ebfIPO\u4e09\u91cd\u50ac\u5316\u4ecd\u5728\u3002"},
    {"name": "AI\u7b97\u529b/CPO/\u5149\u6a21\u5757", "direction": "\u770b\u8dcc", "confidence": 68, "reason": "\u9f99\u864b\u699cAI\u7b97\u529b\u65b9\u54111.82\u4ebf\u8d44\u91d1\u64a4\u9000\u4fe1\u53f7\u660e\u786e\uff08\u5929\u5a31\u6570\u79d1\u88ab\u53cc\u6d3e\u7cfb\u7838\u76d8\uff09\uff0c\u5149\u901a\u4fe1\u51c0\u6d41\u51fa112.6\u4ebf\u5c45\u9996\u3002\u592e\u884c\u51c0\u56de\u7b3c1.16\u4e07\u4ebf\u538b\u5236\u9ad8\u4f30\u503c\uff0c\u5bd2\u6b66\u7eaa-10%\u3001\u534e\u5de5\u79d1\u6280-9%\u3001\u9633\u5149\u7535\u6e90-13%\u7b49\u9ad8\u4f4d\u80a1\u653e\u91cf\u7834\u4f4d\uff0c\u77ed\u671f\u629b\u538b\u672a\u91ca\u653e\u5b8c\u6bd5\uff0c\u5207\u52ff\u76f2\u76ee\u6284\u5e95\u3002"},
    {"name": "\u6c1f\u5316\u5de5/\u5316\u5de5\u6da8\u4ef7", "direction": "\u9707\u8361", "confidence": 55, "reason": "\u591a\u6c1f\u591a4\u8fde\u677f\u4f46\u53d1\u98ce\u9669\u63d0\u793a\uff08\u534a\u5bfc\u4f53\u7ea7\u6c22\u6c1f\u9178\u5360\u6bd4<2%\uff09\uff0c\u626c\u6770\u79d1\u6280\u6da8\u4ef710-15%\u50ac\u5316\u5316\u5de5\u677f\u5757\u3002\u677f\u5757\u6574\u4f53\u4f4e\u4f4d\uff0c\u4f46\u591a\u6c1f\u591a\u77ed\u671f\u6da8\u5e45\u8fc7\u5927\u5b58\u5728\u56de\u8c03\u98ce\u9669\uff0c\u5173\u6ce8\u660a\u534e\u79d1\u6280\uff08\u673a\u6784\u4e705.36\u4ebf\uff09\u7b49\u65b0\u9f99\u5934\u662f\u5426\u63a5\u529b\u3002"},
    {"name": "\u517b\u6b96/\u519c\u4e1a", "direction": "\u770b\u6da8", "confidence": 60, "reason": "\u767d\u7fbd\u9e21/\u751f\u732a\u5468\u671f\u4e0a\u884c+\u4e2d\u62a5\u9884\u589e\u9a71\u52a8\uff0c\u76ca\u751f\u80a1\u4efd\u7b49\u591a\u80a1\u6da8\u505c\uff0c\u4e3b\u529b\u51c0\u6d41\u516537.6\u4ebf\u3002\u5c5e\u4e8e\u5178\u578b\u7684\u4f4e\u4f4d\u8865\u6da8+\u5468\u671f\u53cd\u8f6c\u903b\u8f91\uff0c\u4f46\u677f\u5757\u5bb9\u91cf\u6709\u9650\uff0c\u8ffd\u9ad8\u9700\u8c28\u614e\u3002"},
]
gen.add_tomorrow_prediction(predictions)

# ===== 11. Risk Warning =====
gen.add_risk_warning([
    "\u592e\u884c\u5355\u65e5\u51c0\u56de\u7b3c1.16\u4e07\u4ebf\uff0c\u82e5\u6301\u7eed\u6536\u7d27\u5c06\u538b\u5236\u9ad8\u4f30\u503c\u6210\u957f\u80a1",
    "\u9ad8\u4f4d\u79d1\u6280\u80a1\uff08\u5bd2\u6b66\u7eaa\u3001\u6df1\u79d1\u6280\u3001\u4f70\u7ef4\u5b58\u50a8\u3001\u534e\u5de5\u79d1\u6280\u7b49\uff09\u653e\u91cf\u7834\u4f4d\uff0c\u77ed\u671f\u629b\u538b\u672a\u91ca\u653e\u5b8c\u6bd5\uff0c\u5207\u52ff\u76f2\u76ee\u6284\u5e95",
    "\u591a\u6c1f\u591a\u3001\u683c\u79d1\u5fae\u7b49\u70ed\u95e8\u80a1\u53d1\u5e03\u98ce\u9669\u63d0\u793a\u516c\u544a\uff0c\u6982\u5ff5\u7092\u4f5c\u9762\u4e34\u8bc1\u4f2a",
    "7\u6708\u8fdb\u5165\u4e2d\u62a5\u4e1a\u7ee9\u9a8c\u8bc1\u671f\uff0c\u7eaf\u9898\u6750\u65e0\u4e1a\u7ee9\u652f\u6491\u4e2a\u80a1\u9762\u4e34\u4f30\u503c\u56de\u5f52\u98ce\u9669",
    "\u82f1\u7ef4\u514b\u6df1\u5ea6\u7834\u6b62\u635f-28%\uff0c*ST\u5efa\u827a7/6\u6da8\u8dcc\u5e45\u6269\u81f310%\uff0c\u6301\u4ed3\u98ce\u9669\u52a0\u5267",
    "\u970d\u5c14\u6728\u5179\u6d77\u5ce1\u4e09\u6761\u822a\u7ebf\u5e76\u5b58\uff0c\u822a\u8fd0\u79e9\u5e8f\u590d\u6742\u5316\uff0c\u6cb9\u4ef7\u5730\u7f18\u5c3e\u90e8\u98ce\u9669\u4e0d\u53ef\u5ffd\u89c6",
])

# ===== 12. Trading Plan =====
trading_plan = '''
<div style="display: flex; flex-direction: column; gap: 16px;">
    <div style="background: rgba(239,68,68,0.08); border-radius: 12px; padding: 16px; border-left: 4px solid #ef4444;">
        <div style="font-weight: 700; color: #ef4444; margin-bottom: 8px;">\U0001f534 \u51cf\u4ed3/\u6b62\u635f\uff08\u4f18\u5148\u7ea7\u6700\u9ad8\uff09</div>
        <div style="font-size: 13px; color: #4b5563; line-height: 1.8;">
            <strong>\u82f1\u7ef4\u514b(002837)</strong>\uff1a\u4eca\u65e5\u66b4\u8dcc-6.07%\u653674.73\u5143\u521b\u65b0\u4f4e\uff0c\u6df1\u5ea6\u7834\u6b62\u635f-28%\uff0c\u4e3b\u529b\u6301\u7eed\u6d41\u51fa\u3002\u660e\u65e5\u5982\u6709\u51b2\u9ad8\u81f377-80\u533a\u95f4\uff0c<strong>\u575a\u51b3\u51cf\u4ed3\u81f3\u5c111/2</strong>\uff0c\u5207\u52ff\u8865\u4ed3\u644a\u4f4e\u6210\u672c\u3002<br>
            <strong>*ST\u5efa\u827a(002789)</strong>\uff1a\u4eca\u65e5+3.90%\u653612\u5143\u4ecd\u5728\u6b62\u635f\u4f4d\u4e0b\u65b9\uff0c7/6\u6da8\u8dcc\u5e45\u6269\u81f310%\u6ce2\u52a8\u52a0\u5927\u3002\u660e\u65e5\u76d8\u4e2d\u53cd\u62bd12.1-12.5\u533a\u95f4<strong>\u6b62\u635f\u79bb\u573a</strong>\uff0c\u8fd9\u662f\u6700\u540e\u7a97\u53e3\u3002
        </div>
    </div>
    <div style="background: rgba(16,185,129,0.08); border-radius: 12px; padding: 16px; border-left: 4px solid #10b981;">
        <div style="font-weight: 700; color: #10b981; margin-bottom: 8px;">\U0001f7e2 \u6301\u6709/\u89c2\u5bdf</div>
        <div style="font-size: 13px; color: #4b5563; line-height: 1.8;">
            <strong>\u96c5\u514b\u79d1\u6280(002409)</strong>\uff1a+5.16%\u7eed\u521b\u5386\u53f2\u65b0\u9ad8245.83\u5143\uff0c\u9f99\u864e\u699c\u673a\u6784\u51c0\u4e70\u51652.82\u4ebf\uff01HBM\u4e3b\u5347\u6d6a\u5ef6\u7eed\u3002\u5e95\u4ed3\u7ee7\u7eed\u6301\u6709\uff0c\u82e5\u56de\u8e295\u65e5\u7ebf(215-220\u533a\u95f4)\u53ef\u52a0\u4ed3\u51b3\u7b56\uff0c\u76d8\u4e2d\u51b2\u9ad8240+\u4e0d\u51cf\u4ed3\uff0c\u4f46<strong>\u7981\u6b62\u8ffd\u9ad8</strong>\u3002<br>
            <strong>\u94dc\u51a0\u94dc\u7b94(301217)</strong>\uff1a\u9ad8\u4f4d\u9707\u8361-0.14%\u6536164.84\u5143\uff0c\u6d6e\u76c8+89%\u3002HVLP\u94dc\u7b94+\u5b58\u50a8\u6da8\u4ef7\u903b\u8f91\u672a\u7834\uff0c\u5e95\u4ed3\u6301\u6709\u3002\u79fb\u52a8\u6b62\u76c8165\u5143\uff0c170\u5143\u4e0a\u65b9\u53ef\u51cf1/3\u9501\u5229\u3002\u4eca\u65e5\u76d8\u4e2d\u51b2172.5\u5df2\u7ed9\u51cf\u4ed3\u7a97\u53e3\uff0c\u672a\u51cf\u7684\u7ee7\u7eed\u7b49\u3002
        </div>
    </div>
    <div style="background: rgba(59,130,246,0.08); border-radius: 12px; padding: 16px; border-left: 4px solid #3b82f6;">
        <div style="font-weight: 700; color: #3b82f6; margin-bottom: 8px;">\U0001f535 \u5173\u6ce8\u65b9\u5411\uff08\u8f7b\u4ed3\u8bd5\u63a2\uff09</div>
        <div style="font-size: 13px; color: #4b5563; line-height: 1.8;">
            \u2460<strong>\u534a\u5bfc\u4f53\u8bbe\u5907</strong>\uff1a\u4e2d\u5c71\u4e1c\u8def4.32\u4ebf\u91cd\u4ed3\u5148\u5bfc\u57fa\u7535+\u8d85\u58f0\u7535\u5b50\uff0c\u97e9\u56fd800\u4e07\u4ebf\u6269\u4ea7+\u56fd\u4ea7\u66ff\u4ee3\u903b\u8f91\uff0c\u5173\u6ce8\u8bbe\u5907\u9f99\u5934\u56de\u8c03\u673a\u4f1a\uff08\u4e0d\u8ffd\u9ad8\uff09\uff1b<br>
            \u2461<strong>\u8bc1\u5238\u9f99\u5934</strong>\uff1a\u9996\u65e5\u7206\u53d1\u6b21\u65e5\u5206\u5316\uff0c\u5173\u6ce8\u5929\u98ce/\u56fd\u76db/\u534e\u5b89\u7b49\u524d\u6392\u9f99\u5934\u5ef6\u7eed\u6027\uff0c\u4f4e\u5438\u4e0d\u8ffd\u9ad8\uff1b<br>
            \u2462<strong>\u5316\u5de5\u6da8\u4ef7</strong>\uff1a\u626c\u6770\u79d1\u6280\u6da8\u4ef710-15%\uff0c\u660a\u534e\u79d1\u6280\u673a\u6784\u51c0\u4e705.36\u4ebf\uff0c\u6c1f\u5316\u5de5/\u7535\u5b50\u7279\u6c14\u65b9\u5411\u5173\u6ce8\u65b0\u9f99\u5934\u63a5\u529b\uff08\u6ce8\u610f\u591a\u6c1f\u591a\u98ce\u9669\uff09\u3002
        </div>
    </div>
    <div style="background: rgba(245,158,11,0.08); border-radius: 12px; padding: 16px; border-left: 4px solid #f59e0b;">
        <div style="font-weight: 700; color: #f59e0b; margin-bottom: 8px;">\U0001f7e1 \u4ed3\u4f4d\u5efa\u8bae</div>
        <div style="font-size: 13px; color: #4b5563; line-height: 1.8;">
            \u5e02\u573a\u5904\u4e8e\u98ce\u683c\u5207\u6362\u5173\u952e\u671f\uff0c\u9ad8\u4f4d\u79d1\u6280\u80a1\u653e\u91cf\u7834\u4f4d+\u6d41\u52a8\u6027\u6536\u7d27\u3002<strong>\u5efa\u8bae\u4ed3\u4f4d\u964d\u81f35\u6210\u4ee5\u4e0b</strong>\uff0c\u4f18\u5148\u5904\u7406\u7834\u6b62\u635f\u6301\u4ed3\uff0c\u4e0d\u6025\u4e8e\u52a0\u4ed3\u65b0\u65b9\u5411\u3002\u7b49\u5f85\u79d1\u6280\u80a1\u5145\u5206\u8c03\u6574\u3001\u4e2d\u62a5\u4e1a\u7ee9\u660e\u6717\u540e\u518d\u52a0\u4ed3\u3002
        </div>
    </div>
</div>
'''
gen.add_trading_plan(trading_plan)

# ===== Generate & Save =====
output_path = f"docs/aftermarket/{DATE}_\u76d8\u540e\u901f\u9012.html"
html = gen.generate()
os.makedirs(os.path.dirname(output_path), exist_ok=True)
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(html)
print(f"OK: {output_path}")
print(f"Size: {os.path.getsize(output_path)} bytes")
