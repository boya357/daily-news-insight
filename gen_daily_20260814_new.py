#!/usr/bin/env python3
"""2026年8月14日 每日新闻洞察生成 - 周五"""
import sys, os, shutil, json
WORK_DIR = '/root/daily-news-insight'
sys.path.insert(0, os.path.join(WORK_DIR, 'v3'))
from generators.daily_pro import DailyReportProGenerator

gen = DailyReportProGenerator(
    date_str='2026年8月14日', weekday='星期五',
    subtitle='2026年8月14日 周五 · 美股齐涨纳指+0.81%·闪迪+13.67%引爆存储·央行1万亿买断式逆回购·A股放量跌4300股·算力成唯一科技活口',
    data_dir=os.path.join(WORK_DIR, 'data')
)

def render_cards(items):
    out = ''
    for i in items:
        c = 'text-red-400' if i['up'] else 'text-green-400'
        bg = 'from-red-500/20 to-orange-500/10 border-red-500/20' if i['up'] else 'from-green-500/20 to-emerald-500/10 border-green-500/20'
        out += '<div class="bg-gradient-to-br %s border rounded-lg p-3 text-center transition-all duration-300 hover:scale-105"><div class="text-xs text-white/60 mb-1">%s</div><div class="text-sm font-bold %s">%s</div></div>' % (bg, i['name'], c, i['change'])
    return out

def render_list(items):
    out = ''
    for i in items:
        c = 'text-red-400' if i['up'] else 'text-green-400'
        out += '<div class="flex items-center justify-between py-2 border-b border-white/5 last:border-0"><span class="text-sm text-white/70">%s</span><span class="text-sm font-semibold %s">%s</span></div>' % (i['name'], c, i['change'])
    return out


gen.set_tldr(
    key_points=[
        '美股全线收涨：道指+0.13%、标普+0.65%、纳指+0.81%；费城半导体+0.46%进入技术性牛市；存储板块大爆发，闪迪+13.67%、海力士+9%、美光+4.23%',
        '闪迪投资者日炸裂：NAND市场2027年将达5000亿美元，2028-2030年营收中高双位数增长、毛利率约80%、FCF利润率约50%；AI推理驱动存储需求爆发',
        '央行大动作：8月14日开展10000亿元6个月期买断式逆回购（等量续作），叠加3个月期加量2000亿，8月合计净投放2000亿，配合2.77万亿政府债发行',
        'A股放量跳水：沪指-0.50%失守3940，深成指-0.87%，两市成交2.55万亿放量下跌，4300+个股下跌；机器人/有色/军工重挫，算力液冷成唯一科技活口',
        '持仓策略：雅克科技-3.67%放量大跌，铜冠铜箔-1.06%，英维克-1%，科技高位股集体回调；逢高减仓纪律不变，关注存储板块外溢机会'
    ],
    operation_advice='隔夜美股存储大爆发+央行万亿流动性呵护，今日A股或有修复但分化加剧；科技高位股继续减仓，存储材料/设备方向关注外溢机会，仓位4成防御为主',
    risk_level='中等偏高',
    suggested_position='3-4成'
)

gen.set_quick_anchors([
    {'id': 'section-隔夜全球市场深度解读', 'title': '全球市场', 'icon': '🌍'},
    {'id': 'section-A股昨日复盘与今日展望', 'title': 'A股复盘', 'icon': '📊'},
    {'id': 'section-核心题材与今日催化', 'title': '核心题材', 'icon': '🔥'},
    {'id': 'section-持仓诊断与操作建议', 'title': '持仓诊断', 'icon': '💼'},
    {'id': 'section-空方视角与多空博弈', 'title': '空方视角', 'icon': '⚖️'},
    {'id': 'section-预判验证闭环', 'title': '预判验证', 'icon': '🔮'},
    {'id': 'section-教训库引用', 'title': '教训库', 'icon': '📚'},
])

gen.set_holdings([
    {'name': '英维克', 'code': '002837'},
    {'name': '铜冠铜箔', 'code': '301217'},
    {'name': '雅克科技', 'code': '002409'},
    {'name': '*ST建艺', 'code': '002789'},
])

gen.set_og(
    description='每日新闻洞察 2026年8月14日：美股齐涨纳指+0.81%、闪迪+13.67%引爆存储、央行1万亿买断式逆回购、A股放量跌4300股',
)

gen.add_global_market()

global_cards1 = render_cards([
    {"name":"道琼斯","change":"+0.13%","up":True},
    {"name":"标普500","change":"+0.65%","up":True},
    {"name":"纳斯达克","change":"+0.81%","up":True},
    {"name":"费城半导体","change":"+0.46%","up":True},
    {"name":"日经225","change":"-0.90%","up":False},
    {"name":"恒生指数","change":"-0.17%","up":False},
])
global_list1 = render_list([
    {"name":"WTI原油","change":"-0.08%/$81.18","up":False},
    {"name":"布伦特原油","change":"-0.06%/$87.02","up":False},
    {"name":"COMEX黄金","change":"-0.37%/$4404","up":False},
    {"name":"COMEX白银","change":"-0.60%/$64.61","up":False},
])
global_list2 = render_list([
    {"name":"三星电子","change":"+4.89%","up":True},
    {"name":"SK海力士","change":"+5.92%","up":True},
    {"name":"美光科技","change":"+4.23%","up":True},
    {"name":"台积电ADR","change":"+0.31%","up":True},
])
global_list3 = render_list([
    {"name":"英伟达","change":"+0.54%/$225.30","up":True},
    {"name":"AMD","change":"+0.02%/$483.01","up":True},
    {"name":"微软","change":"+0.90%/$496.88","up":True},
    {"name":"苹果","change":"+1.00%/$305.26","up":True},
    {"name":"博通","change":"+0.43%/$417.82","up":True},
    {"name":"英特尔","change":"+3.58%/$104.56","up":True},
    {"name":"应用材料","change":"-2.48%/$534.54","up":False},
    {"name":"阿斯麦","change":"+2.09%/$1847.90","up":True},
])

global_html = \'\'\'
<div class="grid md:grid-cols-3 gap-4">
  <div class="md:col-span-2">
    <div class="text-white font-semibold mb-3 flex items-center gap-2"><span>🌍</span><span>隔夜全球市场 · 存储史诗级暴涨·闪迪+13.67%·NAND开启5000亿时代</span></div>
    <div class="grid grid-cols-3 md:grid-cols-6 gap-2">{0}</div>
    <p class="text-xs text-white/50 mt-3 leading-relaxed">
      ⚡ <b class="text-yellow-400">核心要点：美股三大指数全线收涨，纳指+0.81%；费城半导体指数+0.46%正式进入技术性牛市；存储板块史诗级爆发，闪迪+13.67%、SK海力士+5.92%、美光+4.23%；特斯拉+3.8%领涨七巨头；黄金微跌原油持平</b>——<br>
      ①<b>存储板块大爆发</b>：闪迪投资者日公布超级指引，NAND市场2027年将达5000亿美元，2028-2030年营收中高双位数增长、毛利率约80%、FCF利润率约50%。股价单日暴涨13.67%创数月最大涨幅。SK海力士+5.92%、美光科技+4.23%、西部数据+7%。AI推理驱动数据中心存储需求爆发，KV Cache重塑存储架构，企业级SSD供不应求。<br>
      ②<b>费半进入技术性牛市</b>：费城半导体指数+0.46%收12456点，较近期低点反弹超20%，正式宣告技术性牛市。CoreWeave、超微电脑等AI算力公司财报超预期，验证AI资本开支依然强劲。英特尔+3.58%、阿斯麦+2.09%。<br>
      ③<b>科技七巨头多数上涨</b>：特斯拉+3.80%（马斯克称AI收入9月首超其他业务）、Meta+2.74%、苹果+1.00%、微软+0.90%、英伟达+0.54%；仅亚马逊-0.80%下跌。整体风险偏好回升。<br>
      ④<b>经济数据温和</b>：美国7月PPI同比+4.7%低于预期4.9%，初请失业金20.9万人高于预期。美联储9月加息概率维持低位（约38%），市场预期通胀压力逐步缓解。<br>
      ⑤<b>原油黄金小幅回落</b>：WTI原油微跌0.08%收81.18美元，布伦特-0.06%收87.02美元。霍尔木兹海峡僵局仍存但市场逐步消化。COMEX黄金-0.37%收4404美元。<br>
      ⑥<b>中概股下跌</b>：纳斯达克中国金龙指数-1.84%，京东-7.31%、拼多多-5.46%、阿里巴巴-2.44%。
    </p>
  </div>
  <div class="space-y-4">
    <div>
    <div class="text-white font-semibold mb-3 flex items-center gap-2"><span>🛢️</span><span>大宗商品</span></div>
      <div class="bg-white/5 rounded-lg p-3">{1}</div></div>
    <div>
    <div class="text-white font-semibold mb-3 flex items-center gap-2"><span>🇰🇷</span><span>韩股存储双雄</span></div>
      <div class="bg-white/5 rounded-lg p-3">{2}</div></div>
    <div>
    <div class="text-white font-semibold mb-3 flex items-center gap-2"><span>💻</span><span>美股科技龙头</span></div>
      <div class="bg-white/5 rounded-lg p-3">{3}</div></div>
  </div>
</div>\'\'\'.format(global_cards1, global_list1, global_list2, global_list3)
gen.add_section("隔夜全球市场深度解读", global_html, "🌍")
