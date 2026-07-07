#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
液冷散热产业链深度研究报告生成器 2026-07-07
使用ProPage深色玻璃态主题
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'v3'))

from generators.pro_base import ProGenerator, source_tag, CONF_HIGH, CONF_MEDIUM, CONF_LOW
from datetime import datetime


class LiquidCoolingReportGenerator(ProGenerator):
    data_type = "industry_chain"

    def __init__(self):
        super().__init__(
            title="液冷散热产业链深度研究报告",
            active_page="产业链",
            footer_text="液冷散热产业链深度研究 · 2026-07-07",
            show_toc=False,
            theme="dark",
            tldr=[
                "【核心结论】液冷散热7/6逆势走强，主力资金结构性抢筹（英维克4.12亿净流入），是物理天花板+政策强制+英伟达Rubin全液冷+中报业绩四重共振，<b>持续性评级：A级（2-4周阶段性主线，中报超预期可升级S级）</b>。",
                "【板块验证】7/6沪指-0.06%、通信-3.05%背景下液冷概念涨2%+，中石科技+18%/高澜+14%/申菱+11%/4只涨停，英维克+3.68%且主力净流入居板块前列，独立走强事实成立。",
                "【操作建议】持仓英维克（成本104.23，现价74.06，浮亏-28.9%）<b>不割肉</b>，冷板龙头85亿在手订单+英伟达Tier1+英特尔全链条认证，中报是关键拐点；72-75区间补仓摊薄，反弹95减仓。",
            ],
            operation_advice="英维克74附近逢低补仓摊薄成本至90元下方，目标88-95；短线弹性关注高澜/中石/飞龙/大元，严格止损-8%。",
            risk_level="中高",
            suggested_position="主线仓位3-4成（冷板集成龙头2成+上游零部件1-1.5成）",
            quick_anchors=[
                {"id": "verify", "title": "板块验证", "icon": "📈"},
                {"id": "logic", "title": "催化逻辑", "icon": "🔥"},
                {"id": "sustain", "title": "持续性", "icon": "⏱️"},
                {"id": "chain", "title": "产业链拆解", "icon": "🔗"},
                {"id": "stocks", "title": "TOP15标的", "icon": "🏆"},
                {"id": "yingweike", "title": "英维克诊断", "icon": "⭐"},
                {"id": "strategy", "title": "投资策略", "icon": "💡"},
                {"id": "risk", "title": "风险提示", "icon": "⚠️"},
            ],
            holding_stocks=[
                {"name": "英维克", "code": "002837"},
                {"name": "铜冠铜箔", "code": "301217"},
                {"name": "雅克科技", "code": "002409"},
                {"name": "*ST建艺", "code": "002789"},
            ],
            og_description="液冷散热7/6逆势走强独立行情验证，四重催化共振持续性分析，产业链全链路拆解+TOP15标的四维打分+英维克持仓诊断",
        )

    def load_data(self):
        super().load_data()
        self.update_time = "2026年7月7日 09:50"
        self.cite("东方财富Choice数据", CONF_HIGH)
        self.cite("财联社", CONF_HIGH)
        self.cite("证券时报数据宝", CONF_HIGH)
        self.cite("中信证券研报", CONF_MEDIUM)
        self.cite("光大证券研报", CONF_MEDIUM)
        self.cite("赛迪顾问", CONF_MEDIUM)
        self.cite("TrendForce", CONF_MEDIUM)

    def _section(self, sid, title, icon, content):
        return f'''
        <section id="{sid}" class="mb-8 scroll-mt-24">
            <div class="flex items-center gap-3 mb-4 pb-3 border-b border-white/10">
                <span class="text-2xl">{icon}</span>
                <h2 class="text-xl md:text-2xl font-black text-white tracking-tight">{title}</h2>
            </div>
            {content}
        </section>'''

    def _glass_card(self, content, pad="p-5", extra=""):
        return f'<div class="card-glass {pad} mb-4 {extra}">{content}</div>'

    def _kpi_grid(self, items):
        html = '<div class="grid grid-cols-2 md:grid-cols-4 gap-3 mb-4">'
        for label, value, color, sub in items:
            html += f'''
            <div class="bg-white/[0.04] border border-white/10 rounded-xl p-3 text-center">
                <div class="text-xs text-white/50 mb-1">{label}</div>
                <div class="text-{color} text-2xl font-black tracking-tight">{value}</div>
                <div class="text-[10px] text-white/40 mt-1">{sub}</div>
            </div>'''
        html += '</div>'
        return html

    def _stock_row(self, rank, code, name, core, score_tup, price_info, cat, is_holding=False, catalysis="", risk="", rating=""):
        e, d, v, c = score_tup
        total = e + d + v + c
        if total >= 34: grade, gcolor = "S", "text-red-400"
        elif total >= 28: grade, gcolor = "A", "text-orange-400"
        elif total >= 22: grade, gcolor = "B", "text-yellow-400"
        else: grade, gcolor = "C", "text-white/50"
        hold_badge = '<span class="holding-badge">⭐持仓</span> ' if is_holding else ''
        return f'''
        <div class="bg-white/[0.04] border border-white/10 rounded-xl p-4 mb-3 stock-card {'holding-card' if is_holding else ''}">
            <div class="flex items-start justify-between gap-3 mb-2 flex-wrap">
                <div class="flex items-center gap-2 flex-wrap">
                    <span class="text-white/30 text-xs font-mono w-6">#{rank}</span>
                    {hold_badge}<span class="text-white font-bold text-base">{name}</span>
                    <span class="text-white/40 text-xs font-mono">{code}</span>
                    <span class="bg-purple-500/20 text-purple-300 text-[10px] px-2 py-0.5 rounded border border-purple-500/30">{cat}</span>
                    <span class="{gcolor} font-black text-sm bg-white/5 px-2 py-0.5 rounded">{grade}级 {total}分</span>
                </div>
                <div class="text-right">
                    <div class="text-white/50 text-[10px]">{price_info[0]}</div>
                    <div class="text-white font-bold text-sm">{price_info[1]}</div>
                </div>
            </div>
            <div class="text-white/75 text-sm leading-relaxed mb-2">{core}</div>
            <div class="grid grid-cols-4 gap-2 mb-2">
                <div class="text-center"><div class="text-[10px] text-white/40">弹性</div><div class="text-red-400 font-bold">{e}/10</div></div>
                <div class="text-center"><div class="text-[10px] text-white/40">确定性</div><div class="text-green-400 font-bold">{d}/10</div></div>
                <div class="text-center"><div class="text-[10px] text-white/40">估值</div><div class="text-blue-400 font-bold">{v}/10</div></div>
                <div class="text-center"><div class="text-[10px] text-white/40">筹码</div><div class="text-yellow-400 font-bold">{c}/10</div></div>
            </div>
            <div class="flex gap-2 flex-wrap text-xs">
                {f'<span class="bg-green-500/10 text-green-300 px-2 py-0.5 rounded">🚀 {catalysis}</span>' if catalysis else ''}
                {f'<span class="bg-red-500/10 text-red-300 px-2 py-0.5 rounded">⚠️ {risk}</span>' if risk else ''}
                {f'<span class="bg-blue-500/10 text-blue-300 px-2 py-0.5 rounded">📌 {rating}</span>' if rating else ''}
            </div>
        </div>'''

    def _sec_verify(self):
        kpi = self._kpi_grid([
            ("7/6沪指", "-0.06%", "white", "大盘弱势"),
            ("通信板块", "-3.05%", "text-green-400", "AI硬件普跌"),
            ("液冷概念", "+2%↑", "text-red-400", "逆势大涨"),
            ("成交", "658亿", "text-yellow-400", "量能放大50%"),
        ])
        table_rows = [
            ("中石科技", "300684", "+18.19%", "73.29", "导热材料/冷板部件", "领涨龙头"),
            ("高澜股份", "300499", "+10.11%", "41.94", "冷板+浸没双线", "主力净流入1.75亿"),
            ("申菱环境", "301018", "+6.13%", "130.73", "CDU+液冷总包", "主力净流入1.39亿"),
            ("大元泵业", "603757", "+10.00%", "79.19", "液冷屏蔽泵", "涨停+主力2.35亿"),
            ("海鸥股份", "603269", "+9.97%", "—", "冷却塔/冷源", "涨停+主力1.56亿"),
            ("联德股份", "605060", "+10.00%", "—", "液冷精密结构件", "涨停"),
            ("宏盛股份", "603090", "+10.00%", "—", "CDU/广达Meta链", "涨停+主力1.05亿"),
            ("快克智能", "603203", "涨停", "—", "液冷焊接设备", "涨停"),
            ("南方泵业", "300145", "+8.65%", "—", "液冷泵", "主力1.80亿"),
            ("冰轮环境", "000811", "+1.86%(收)", "53.63", "园区冷源/冷水机组", "盘初+7.86%"),
            ("飞龙股份", "002536", "+6.58%(盘)", "—", "液冷电子水泵", "三巨头认证"),
            ("同飞股份", "300990", "+6.73%(盘)", "—", "工业温控/液冷", "订单排到2027"),
            ("银轮股份", "002126", "跟涨+5%", "—", "汽零跨界液冷", "墨西哥基地出海"),
            ("腾龙股份", "603158", "+5.32%(盘)", "—", "液冷管路", "汽零跨界"),
            ("英维克(持仓)", "002837", "+3.68%", "74.06", "冷板全链条龙头", "主力净流入4.12亿🏆"),
        ]
        rows_html = ""
        for i, (n, c, chg, pr, biz, note) in enumerate(table_rows):
            chg_color = "text-red-400" if ("+" in chg or "涨" in chg or "涨停" in chg) else "text-green-400"
            is_hold = "持仓" in n
            rows_html += f'''
            <tr class="border-b border-white/5 {'bg-yellow-500/5' if is_hold else ''}">
                <td class="py-2 px-2 text-white/40 text-xs">{i+1}</td>
                <td class="py-2 px-2 text-white font-semibold text-sm">{"⭐ " if is_hold else ""}{n}</td>
                <td class="py-2 px-2 text-white/40 text-xs font-mono">{c}</td>
                <td class="py-2 px-2 {chg_color} font-bold text-sm">{chg}</td>
                <td class="py-2 px-2 text-white/50 text-xs hidden md:table-cell">{pr}</td>
                <td class="py-2 px-2 text-white/70 text-xs">{biz}</td>
                <td class="py-2 px-2 text-white/60 text-xs hidden md:table-cell">{note}</td>
            </tr>'''
        table = f'''
        <div class="overflow-x-auto">
        <table class="w-full text-sm">
            <thead><tr class="text-white/50 text-xs border-b border-white/10">
                <th class="py-2 px-2 text-left">#</th><th class="py-2 px-2 text-left">标的</th><th class="py-2 px-2 text-left">代码</th>
                <th class="py-2 px-2 text-left">7/6涨跌</th><th class="py-2 px-2 text-left hidden md:table-cell">收盘</th>
                <th class="py-2 px-2 text-left">液冷业务</th><th class="py-2 px-2 text-left hidden md:table-cell">备注</th>
            </tr></thead>
            <tbody>{rows_html}</tbody>
        </table></div>'''
        content = kpi + self._glass_card(f'''
            <h3 class="text-white font-bold text-base mb-2">📊 7月6日液冷板块核心标的涨跌全览（盘初+收盘双验证）</h3>
            <p class="text-white/60 text-xs mb-3">数据来源：东方财富Choice/财联社/证券时报数据宝 {source_tag("多源交叉", CONF_HIGH, verified=True)}</p>
            {table}
        ''')
        content += self._glass_card(f'''
            <h3 class="text-white font-bold text-base mb-2">🔍 "独立走强"判断三重验证</h3>
            <div class="grid md:grid-cols-3 gap-3">
                <div class="bg-white/[0.03] p-3 rounded-lg border border-white/10">
                    <div class="text-red-400 font-bold text-sm mb-1">✓ 逆势验证</div>
                    <p class="text-white/70 text-xs leading-relaxed">7/6沪指-0.06%、通信板块-3.05%、建筑材料-5.75%、华工科技/罗博特科/绿的谐波批量跌6-7%；同日液冷概念板块涨2%，9只涨停/涨超10%，典型"指数跌、板块涨"独立行情。</p>
                </div>
                <div class="bg-white/[0.03] p-3 rounded-lg border border-white/10">
                    <div class="text-red-400 font-bold text-sm mb-1">✓ 资金验证</div>
                    <p class="text-white/70 text-xs leading-relaxed">机械设备行业当日主力净流出48.81亿，但液冷子板块批量净流入：英维克4.12亿、大元泵业2.35亿、南方泵业1.80亿、高澜1.75亿、海鸥1.56亿、申菱1.39亿，资金结构性抢筹，量能放大50%。</p>
                </div>
                <div class="bg-white/[0.03] p-3 rounded-lg border border-white/10">
                    <div class="text-red-400 font-bold text-sm mb-1">✓ 催化验证</div>
                    <p class="text-white/70 text-xs leading-relaxed">非单一突发利好，是7/2大跌后资金回流高确定性业绩赛道+光大早盘液冷研报+Rubin全液冷/昇腾Atlas950/CDU金标准/欧盟PUE新规多重共振，非纯情绪炒作。</p>
                </div>
            </div>
            <p class="text-white/80 text-sm mt-3 font-semibold">结论："液冷散热独立走强"判断<b class="text-red-400">事实成立</b>，有资金面、基本面、催化面三重支撑。</p>
        ''')
        return self._section("verify", "一、板块走强验证：7/6液冷逆势上涨是否真实？", "📈", content)

    def _sec_logic(self):
        catalysts = [
            ("🔥 英伟达Rubin全液冷强制标准（产业最强催化）",
             "英伟达Rubin平台彻底取消风冷兼容，单GPU功耗突破1500W，单机柜功率从传统4-8kW飙升至100kW+（NVL144达130kW），空气导热系数仅为液体1/25，30kW以上风冷物理失效；Rubin Q3批量交付强制配套液冷。单柜液冷价值从GB200的4.15万→Rubin NVL144的5.57万美元(+34%)。谷歌TPUv7/ Meta/微软跟进。",
             "高"),
            ("📜 政策端：PUE红线强制液冷（政策硬约束）",
             "工信部《人工智能与能源双向赋能行动方案》硬性要求：新建大型AI智算中心必须配套液冷；东数西算枢纽PUE≤1.2（风冷1.4-1.5无法达标），无液冷项目不予审批；2028年前完成存量高功耗风冷机房改造，千亿存量改造市场开启。7月欧盟数据中心PUE新规生效，北京上海已禁新建纯风冷。",
             "高"),
            ("💰 订单端：7月万级机柜集采周期开启",
             "三大运营商、字节/腾讯/阿里、算力租赁公司集中开启大规模液冷集采，告别往年小批量试点。头部企业在手订单覆盖至2027：英维克85亿+、申菱30亿+、高澜/同飞/曙光排到2027。CDU获CRAA金标准认证（6家首批），降低客户试错门槛，大规模集采条件成熟。",
             "高"),
            ("📈 渗透率J型拐点：12%→50%临界点（产业β）",
             "2025年末国内液冷渗透率约12-20%，2026Q1 AI训练服务器液冷渗透率已达74%，新建40+智算中心100%液冷；机构预测2026全年渗透率突破50%（可选→标配临界点），2027>50%、2030年82%。渗透率30-50%是产业爆发典型J曲线拐点，参考2019-2020新能源车行情。",
             "高"),
            ("🏆 英特尔液冷工质认证：标准化里程碑",
             "6/24英特尔联合英维克、嘉实多发布单相冷板液冷工质验证成果，英维克SK-P25-C/SK-WT-C通过225天严苛双回路测试，Coolinside全链条实现100%英特尔认证覆盖，国内唯一、全球稀缺。标志液冷从「可选」走向「标配」，标准化加速产业化。",
             "中高"),
            ("🇨🇳 华为昇腾Atlas950全液冷千卡集群",
             "华为Atlas 950全液冷千卡集群交付排期至Q4，申菱、英维克作为华为CDU一级供应商，半年报液冷营收大幅增长；冰轮环境等园区冷源同步受益。国产算力链液冷需求爆发，与海外英伟达链双轮驱动。",
             "中高"),
            ("📊 业绩端：中报预告催化+Q2订单交付",
             "中信证券指出液冷从题材预期进入业绩兑现期，冷板/CDU/氟化液龙头H1净利同比普遍70%+；英维克Q1液冷收入+250-290%、高澜+180-210%、申菱+220-250%、曙光数创液冷+780%。中报预告窗口（7月中-8月中）是业绩验证关键期。部分企业上调售价8-35%。",
             "中高"),
        ]
        cat_html = ""
        for title, body, level in catalysts:
            lcolor = {"高": "text-red-400", "中高": "text-orange-400", "中": "text-yellow-400"}.get(level, "text-white/60")
            cat_html += f'''
            <div class="bg-white/[0.03] border-l-2 border-purple-500/60 pl-4 py-2 mb-3">
                <div class="flex items-center gap-2 mb-1 flex-wrap">
                    <span class="text-white font-bold text-sm">{title}</span>
                    <span class="{lcolor} text-[10px] bg-white/5 px-1.5 rounded">催化级别：{level}</span>
                </div>
                <p class="text-white/70 text-sm leading-relaxed">{body}</p>
            </div>'''
        content = self._glass_card(f'''
            <h3 class="text-white font-bold text-base mb-3">七大核心催化逻辑（政策+产业+订单+业绩+标准化五重共振）</h3>
            {cat_html}
        ''')
        content += self._glass_card(f'''
            <h3 class="text-white font-bold text-base mb-3">🌡️ 核心底层逻辑：AI芯片功耗暴涨突破风冷物理极限</h3>
            <div class="grid grid-cols-2 md:grid-cols-5 gap-2 text-center text-xs">
                <div class="bg-white/[0.03] p-2 rounded"><div class="text-white/40">H100</div><div class="text-white font-bold">700W</div><div class="text-white/40">风冷可解</div></div>
                <div class="bg-white/[0.03] p-2 rounded"><div class="text-white/40">B200</div><div class="text-yellow-400 font-bold">1000W</div><div class="text-white/40">临界</div></div>
                <div class="bg-white/[0.03] p-2 rounded border border-orange-500/30"><div class="text-white/40">GB300</div><div class="text-orange-400 font-bold">1400W</div><div class="text-orange-300">液冷必须</div></div>
                <div class="bg-red-500/20 p-2 rounded border border-red-500/50"><div class="text-red-300 font-bold">Rubin</div><div class="text-red-400 font-black text-lg">1500W+</div><div class="text-red-300">强制全液冷</div></div>
                <div class="bg-white/[0.03] p-2 rounded"><div class="text-white/40">单机柜</div><div class="text-red-400 font-bold">100kW+</div><div class="text-white/40">风冷失效</div></div>
            </div>
            <p class="text-white/70 text-xs mt-3 leading-relaxed">
                物理定律层面：空气导热系数仅为液体的<b class="text-red-400">1/25</b>，30kW/柜以上风冷彻底失效，强行风冷导致芯片降频、算力缩水、设备老化。<b>液冷不是企业主动选择，是物理定律卡死的必选项</b>。这是产业逻辑最强硬的底层支撑——不可逆、不依赖政策、不依赖情绪。
            </p>
            <p class="text-white/60 text-[11px] mt-2">数据来源：英伟达技术白皮书/TrendForce/光大证券 {source_tag("多源交叉", CONF_HIGH, verified=True)}</p>
        ''')
        return self._section("logic", "二、核心催化逻辑：为什么是现在？为什么是液冷？", "🔥", content)

    def _sec_sustain(self):
        content = self._glass_card(f'''
            <div class="text-center mb-4">
                <div class="text-white/60 text-sm mb-2">液冷散热板块持续性评级</div>
                <div class="inline-block bg-gradient-to-r from-orange-500/20 to-red-500/20 border border-orange-500/50 rounded-2xl px-8 py-4">
                    <div class="text-5xl font-black text-orange-400">A级</div>
                    <div class="text-white/80 text-sm mt-1">阶段性主线（2-4周）</div>
                    <div class="text-white/50 text-xs mt-1">中报超预期可升级S级（1月+主线）</div>
                </div>
            </div>
            <p class="text-white/80 text-sm leading-relaxed mb-3">
                <b class="text-orange-400">评级理由：</b>液冷具备"产业不可逆逻辑+中报业绩兑现+主力资金结构性流入+政策刚性约束"四大主线基因，
                但当前并非市场唯一主线（存储/HBM/机器人/创新药/煤炭均有结构性机会），且Q1龙头业绩受汇兑/减值拖累利润端尚未完全兑现，
                短期估值不低，需要中报数据持续验证。
            </p>
        ''', extra="border-2 border-orange-500/30")
        cond_items = [
            ("政策催化", "✅ 已落地", "PUE≤1.2强制、欧盟新规、北京/上海禁纯风冷", 10),
            ("产业β", "✅ 渗透率J曲线", "2026Q1训练服务器液冷渗透率74%，全年冲击50%", 10),
            ("龙头催化", "✅ 英伟达+华为双轮", "Rubin Q3全液冷/昇腾Atlas950交付排至Q4", 9),
            ("订单兑现", "✅ 在手订单明确", "英维克85亿/申菱30亿/头部排到2027", 9),
            ("业绩弹性", "⚠️ H1验证中", "Q1汇兑减值承压，H2加速，中报预告为关键", 7),
            ("资金共识", "🔄 正在形成", "7/6单日抢筹，但尚未形成跨板块持续抱团", 7),
            ("估值空间", "⚠️ 龙头偏高", "英维克PE偏高/二线PE 30-50倍", 6),
            ("筹码结构", "🔄 机构+游资共振", "冰轮连续12日净买/英维克机构高/大元高澜换手20%+", 6),
            ("产业周期", "✅ 成长期初段", "渗透率37%→50%拐点，类似2019-2020新能源车阶段", 9),
        ]
        ch = ""
        for name, status, desc, score in cond_items:
            color = "text-green-400" if "✅" in status else ("text-yellow-400" if "⚠️" in status else "text-orange-400")
            ch += f'''
            <div class="mb-2">
                <div class="flex justify-between items-center mb-1">
                    <span class="text-white text-sm font-semibold">{name}</span>
                    <span class="{color} text-xs font-bold">{status}</span>
                </div>
                <div class="risk-bar"><div class="risk-bar-fill" style="width:{score*10}%; background: linear-gradient(90deg, #f59e0b, #ef4444);"></div></div>
                <div class="text-white/50 text-xs mt-1">{desc}</div>
            </div>'''
        content += self._glass_card(f'''
            <h3 class="text-white font-bold text-base mb-3">📋 成为主线的9大必要条件逐条评估（满分90分）</h3>
            {ch}
            <p class="text-white/80 text-sm mt-3">
                <b>综合打分：73/90（81分）</b>，政策/产业/龙头/订单/周期5项高分，业绩/资金/估值/筹码4项仍需验证。
                <b class="text-orange-400">若7月中报预告普遍超预期+两市成交维持2.8万亿+每周有亿级液冷中标，升级S级主线；若中报不及预期或Rubin延期，回落B级脉冲。</b>
            </p>
        ''')
        content += self._glass_card(f'''
            <h3 class="text-white font-bold text-base mb-3">🆚 与其他主线横向对比</h3>
            <div class="overflow-x-auto">
            <table class="w-full text-xs">
                <thead><tr class="text-white/50 border-b border-white/10">
                    <th class="py-2 px-2 text-left">板块</th><th class="py-2 px-2 text-left">阶段</th><th class="py-2 px-2 text-left">核心驱动</th>
                    <th class="py-2 px-2 text-left">业绩</th><th class="py-2 px-2 text-left">持续性</th><th class="py-2 px-2 text-left">评级</th>
                </tr></thead>
                <tbody>
                    <tr class="border-b border-white/5 bg-red-500/5"><td class="py-2 font-bold text-red-400">液冷散热</td><td class="py-2">刚启动</td><td class="py-2">物理强制+政策+Rubin</td><td class="py-2">H1验证/H2爆发</td><td class="py-2">2-4周→S可能</td><td class="py-2 text-orange-400 font-bold">A（重点）</td></tr>
                    <tr class="border-b border-white/5"><td class="py-2">HBM/存储</td><td class="py-2">主升中段</td><td class="py-2">SK海力士涨价/Meta需求</td><td class="py-2">已连续兑现</td><td class="py-2">1-2月</td><td class="py-2 text-red-400">S</td></tr>
                    <tr class="border-b border-white/5"><td class="py-2">人形机器人</td><td class="py-2">分化期</td><td class="py-2">Optimus量产</td><td class="py-2">远期</td><td class="py-2">反复轮动</td><td class="py-2 text-yellow-400">B+</td></tr>
                    <tr class="border-b border-white/5"><td class="py-2">黄金/有色</td><td class="py-2">趋势中段</td><td class="py-2">降息+避险</td><td class="py-2">价格驱动</td><td class="py-2">中线</td><td class="py-2 text-yellow-400">B+</td></tr>
                    <tr class="border-b border-white/5"><td class="py-2">创新药</td><td class="py-2">刚启动</td><td class="py-2">BD出海+医保</td><td class="py-2">H2兑现</td><td class="py-2">2-4周</td><td class="py-2 text-orange-400">A-</td></tr>
                    <tr class="border-b border-white/5"><td class="py-2">煤炭/红利</td><td class="py-2">防御阶段</td><td class="py-2">高股息+迎峰度夏</td><td class="py-2">稳定</td><td class="py-2">防守配置</td><td class="py-2 text-white/50">B</td></tr>
                    <tr><td class="py-2">CPO/光模块</td><td class="py-2">调整期</td><td class="py-2">1.6T放量</td><td class="py-2">已兑现</td><td class="py-2">等待Q3</td><td class="py-2 text-white/50">B-</td></tr>
                </tbody>
            </table></div>
            <p class="text-white/70 text-xs mt-3">液冷是<b>AI硬件调整后最先企稳反弹的细分</b>，相对存储位置低、相对机器人业绩确定、相对创新药产业β更硬，是AI算力链的"避险型进攻品种"。</p>
        ''')
        content += self._risk_section(
            title="🔴 证伪条件/空方逻辑",
            falsify_signals=[
                "英伟达Rubin量产/交付延期（最核心证伪信号）",
                "龙头中报液冷营收增速<150%或毛利率下滑",
                "两市成交持续低于2.2万亿，题材资金退潮",
                "液冷集采价格战爆发，单价下降超20%",
                "Meta/MSFT/谷歌Q2 Capex下修",
                "英维克放量跌破68元/申菱跌破115元关键均线",
            ],
            stop_loss="板块指数跌破20日均线（约2200点）或英维克跌破68元（-8%止损）",
            bear_logic=[
                "Q1英维克净利润-82%（汇兑+减值），利润兑现滞后，市场对'光打雷不下雨'有警惕",
                "动态估值偏高：英维克TTM PE 100倍+，透支2027预期",
                "中低端竞争恶化：大量汽零/家电/机械企业跨界液冷，毛利率下行压力",
                "7月以来主线切换快（存储/创新药/煤炭/机器人轮番表现），资金抱团持续性差",
                "AI硬件整体调整期（华工/绿的/欧科亿批量跌6-13%），液冷独木难支有补跌风险",
                "机构持仓已不低，龙头增量资金空间有限",
            ],
            contrarian_view="反方认为：液冷'故事'讲了2年，2024-2025多次脉冲均回落；真正大规模业绩兑现要到2026Q4-2027Q1，当前仍是预期博弈阶段，容易'利好兑现即出局'。若7-8月中报不能强力验证，可能重演4-5月AI硬件'利好出尽'走势。"
        )
        content += self._glass_card(f'''
            <h3 class="text-white font-bold text-base mb-2">👀 持续性关键观察指标（每周跟踪）</h3>
            <div class="grid md:grid-cols-2 gap-2 text-sm">
                <div class="bg-green-500/5 border border-green-500/20 rounded p-2">
                    <div class="text-green-400 font-bold text-xs mb-1">升级S级信号（出现2项以上加仓）</div>
                    <ul class="text-white/70 text-xs space-y-1">
                        <li>• 两市成交额连续3日维持2.8万亿+</li>
                        <li>• 每周持续披露亿级液冷中标公告（≥2个）</li>
                        <li>• 英维克/申菱/高澜中报液冷净利+100%以上</li>
                        <li>• 英伟达Q2 Capex超预期+Rubin时间表确认</li>
                        <li>• 液冷ETF连续3日净流入+板块连板≥3</li>
                    </ul>
                </div>
                <div class="bg-red-500/5 border border-red-500/20 rounded p-2">
                    <div class="text-red-400 font-bold text-xs mb-1">降级B级信号（出现2项即减仓）</div>
                    <ul class="text-white/70 text-xs space-y-1">
                        <li>• 成交额跌破2.2万亿+题材批量跌停</li>
                        <li>• 龙头中报低于预期或毛利率下滑</li>
                        <li>• 英维克跌破68元、申菱跌破115元</li>
                        <li>• 英伟达/谷歌Capex下修或Rubin延期</li>
                        <li>• 液冷集采报价比去年降价超25%</li>
                    </ul>
                </div>
            </div>
        ''')
        return self._section("sustain", "三、主线持续性判断：A级（2-4周），中报决定能否升级S级", "⏱️", content)

    def _sec_chain(self):
        content = self._glass_card(f'''
            <h3 class="text-white font-bold text-base mb-3">🌐 液冷散热产业链全景图</h3>
            <div class="text-center mb-4">
                <div class="inline-block w-full max-w-2xl">
                    <div class="bg-gradient-to-r from-blue-500/20 to-cyan-500/20 border border-blue-500/30 rounded-xl p-3 mb-2">
                        <div class="text-blue-300 font-bold text-sm">⬆ 上游：核心材料 & 零部件</div>
                        <div class="text-white/70 text-xs mt-1">冷却液（氟化液/水乙二醇）·冷板材料（铝/铜/微通道）·连接件（快接头/管路/密封）·液冷泵/阀·换热器</div>
                    </div>
                    <div class="text-purple-400 text-xl">⬇</div>
                    <div class="bg-gradient-to-r from-purple-500/20 to-pink-500/20 border border-purple-500/30 rounded-xl p-3 mb-2">
                        <div class="text-purple-300 font-bold text-sm">⬛ 中游：液冷系统集成（价值核心，占85%）</div>
                        <div class="text-white/70 text-xs mt-1">冷板式（CDU+冷板+Manifold，占85%）·浸没式（单相/两相，6-10%）·喷淋式（小众）·温控整机</div>
                    </div>
                    <div class="text-pink-400 text-xl">⬇</div>
                    <div class="bg-gradient-to-r from-pink-500/20 to-orange-500/20 border border-pink-500/30 rounded-xl p-3">
                        <div class="text-pink-300 font-bold text-sm">⬇ 下游：应用场景</div>
                        <div class="text-white/70 text-xs mt-1">AI数据中心·AI服务器（GB200/Rubin/昇腾）·储能温控·动力电池·超算·CPO光模块·电源液冷一体化</div>
                    </div>
                </div>
            </div>
        ''')
        content += self._glass_card(f'''
            <h3 class="text-white font-bold text-base mb-3">📏 市场空间测算：2025-2030 CAGR 40%+</h3>
            <div class="overflow-x-auto">
            <table class="w-full text-xs">
                <thead><tr class="text-white/50 border-b border-white/10">
                    <th class="py-1 px-2 text-left">年份</th><th class="py-1 px-2 text-right">国内液冷(亿)</th><th class="py-1 px-2 text-right">同比</th>
                    <th class="py-1 px-2 text-right">冷板式</th><th class="py-1 px-2 text-right">浸没式</th><th class="py-1 px-2 text-right">渗透率</th>
                </tr></thead>
                <tbody>
                    <tr class="border-b border-white/5"><td class="py-1">2024</td><td class="py-1 text-right text-white/70">110</td><td class="py-1 text-right">—</td><td class="py-1 text-right">~100</td><td class="py-1 text-right">~10</td><td class="py-1 text-right text-white/60">14%</td></tr>
                    <tr class="border-b border-white/5"><td class="py-1">2025</td><td class="py-1 text-right">160</td><td class="py-1 text-right text-yellow-400">+45%</td><td class="py-1 text-right">147</td><td class="py-1 text-right">13</td><td class="py-1 text-right text-white/60">20-33%</td></tr>
                    <tr class="border-b border-white/5 bg-orange-500/10"><td class="py-1 font-bold text-orange-400">2026E</td><td class="py-1 text-right font-bold text-orange-400">233-942</td><td class="py-1 text-right text-red-400 font-bold">+46-80%</td><td class="py-1 text-right">216</td><td class="py-1 text-right">16</td><td class="py-1 text-right text-orange-400 font-bold">37-50%</td></tr>
                    <tr class="border-b border-white/5"><td class="py-1">2027E</td><td class="py-1 text-right">314-1478</td><td class="py-1 text-right text-yellow-400">+35-57%</td><td class="py-1 text-right">280</td><td class="py-1 text-right">34</td><td class="py-1 text-right">>50%</td></tr>
                    <tr class="border-b border-white/5"><td class="py-1">2028E</td><td class="py-1 text-right">470-2000</td><td class="py-1 text-right text-yellow-400">+50%</td><td class="py-1 text-right">438</td><td class="py-1 text-right">33</td><td class="py-1 text-right">~65%</td></tr>
                    <tr><td class="py-1">2030E</td><td class="py-1 text-right">全球535亿美元</td><td class="py-1 text-right">—</td><td class="py-1 text-right">60%</td><td class="py-1 text-right">40%</td><td class="py-1 text-right text-green-400">82%</td></tr>
                </tbody>
            </table></div>
            <p class="text-white/60 text-[11px] mt-2">口径：233-470亿为赛迪数据中心液冷设备口径；942-1478亿为全产业链口径（含服务器+IDC+储能+动力）；全球数据为中信/国信。CAGR(2025-28E) 43-55%。{source_tag("赛迪/中信/IDC", CONF_MEDIUM)}</p>
        ''')
        content += self._glass_card(f'''
            <h3 class="text-white font-bold text-base mb-3">⚔️ 技术路线对比：冷板式vs浸没式vs喷淋式</h3>
            <div class="overflow-x-auto">
            <table class="w-full text-xs">
                <thead><tr class="text-white/50 border-b border-white/10">
                    <th class="py-1 px-2 text-left">维度</th><th class="py-1 px-2 text-left">冷板式（主流）</th><th class="py-1 px-2 text-left">浸没式（远期）</th><th class="py-1 px-2 text-left">喷淋式</th>
                </tr></thead>
                <tbody>
                    <tr class="border-b border-white/5"><td class="py-1 font-semibold">散热能力</td><td class="py-1">100-300W/cm²</td><td class="py-1">单相300-800/两相500-1500W/cm²</td><td class="py-1">中等</td></tr>
                    <tr class="border-b border-white/5"><td class="py-1 font-semibold">PUE</td><td class="py-1">1.15-1.25</td><td class="py-1">1.02-1.15</td><td class="py-1">1.10-1.20</td></tr>
                    <tr class="border-b border-white/5"><td class="py-1 font-semibold">场景</td><td class="py-1 text-green-400">20-100kW中高密度</td><td class="py-1 text-blue-400">>50kW超算/万卡</td><td class="py-1">边缘</td></tr>
                    <tr class="border-b border-white/5"><td class="py-1 font-semibold">2026市占率</td><td class="py-1 text-red-400 font-bold">85-93%</td><td class="py-1">6-10%</td><td class="py-1"><1%</td></tr>
                    <tr class="border-b border-white/5"><td class="py-1 font-semibold">改造成本</td><td class="py-1">低</td><td class="py-1">高（专用服务器/冷却液）</td><td class="py-1">中</td></tr>
                    <tr class="border-b border-white/5"><td class="py-1 font-semibold">认证周期</td><td class="py-1">6-12个月</td><td class="py-1">18-36个月</td><td class="py-1">中</td></tr>
                    <tr class="border-b border-white/5"><td class="py-1 font-semibold">单柜价值</td><td class="py-1">3-5万美元</td><td class="py-1">5-8万美元</td><td class="py-1">3-5万</td></tr>
                    <tr class="border-b border-white/5"><td class="py-1 font-semibold">核心部件</td><td class="py-1">冷板(32%)+快接(28%)+CDU(25%)</td><td class="py-1">腔体+氟化液+CDU</td><td class="py-1">喷淋头+管路</td></tr>
                    <tr><td class="py-1 font-semibold">代表标的</td><td class="py-1 text-red-400">英维克/申菱/高澜/银轮/飞龙</td><td class="py-1 text-blue-400">曙光数创/巨化/高澜</td><td class="py-1">少量</td></tr>
                </tbody>
            </table></div>
            <div class="mt-3 p-3 bg-white/[0.03] rounded-lg border border-white/10">
                <div class="text-yellow-400 font-bold text-sm mb-1">💡 判断结论</div>
                <p class="text-white/70 text-xs leading-relaxed">
                    <b class="text-red-400">短期6-18月（2026-2027H1）冷板式绝对主流</b>，占85%+份额，订单兑现最快；
                    <b class="text-blue-400">中长期（2027H2-2030）浸没式6%→40%</b>，超高功耗场景放量；
                    <b>氟化液耗材（巨化）具备复购属性</b>，是最佳"卖铲人"。两条路线<b>互补而非替代</b>。
                </p>
            </div>
        ''')
        content += self._glass_card(f'''
            <h3 class="text-white font-bold text-base mb-2">💰 冷板式BOM价值拆分</h3>
            <div class="space-y-2">
                <div><div class="flex justify-between text-xs mb-1"><span class="text-white">微通道冷板（最大单一零部件）</span><span class="text-red-400 font-bold">32%</span></div><div class="risk-bar"><div class="risk-bar-fill" style="width:64%;background:linear-gradient(90deg,#ef4444,#f97316);"></div></div></div>
                <div><div class="flex justify-between text-xs mb-1"><span class="text-white">UQD快接头/盲插连接器</span><span class="text-orange-400 font-bold">28%</span></div><div class="risk-bar"><div class="risk-bar-fill" style="width:56%;background:linear-gradient(90deg,#f97316,#f59e0b);"></div></div></div>
                <div><div class="flex justify-between text-xs mb-1"><span class="text-white">CDU冷却液分配单元（心脏）</span><span class="text-yellow-400 font-bold">25%</span></div><div class="risk-bar"><div class="risk-bar-fill" style="width:50%;background:linear-gradient(90deg,#f59e0b,#eab308);"></div></div></div>
                <div><div class="flex justify-between text-xs mb-1"><span class="text-white">Manifold/管路/冷却液</span><span class="text-blue-400 font-bold">10%</span></div><div class="risk-bar"><div class="risk-bar-fill" style="width:20%;background:linear-gradient(90deg,#3b82f6,#6366f1);"></div></div></div>
                <div><div class="flex justify-between text-xs mb-1"><span class="text-white">冷却塔/冷源/施工</span><span class="text-purple-400 font-bold">5%</span></div><div class="risk-bar"><div class="risk-bar-fill" style="width:10%;background:linear-gradient(90deg,#8b5cf6,#a855f7);"></div></div></div>
            </div>
            <p class="text-white/60 text-[11px] mt-2">冷板+快接+CDU占85%是利润核心；Rubin 45℃高温液冷对密封/冷却液耐温耐腐蚀提出新要求，催生材料升级红利。</p>
        ''')
        upstream = [
            ("冷却液(氟化液/PG)", "巨化股份·统一股份·康普顿·英维克(SoluKing)", "耗材复购/浸没放量", "99.99%纯度壁垒/3M退国产替代"),
            ("微通道冷板", "高澜股份·飞荣达·鸿富瀚·银轮股份·祥鑫科技·精研科技", "单机柜冷板数量翻倍", "微通道+散热盖一体化/英伟达认证"),
            ("快接头/UQD", "中航光电·奕东电子·鼎通科技·意华股份·硕贝德", "密封壁垒/耗材属性", "Rubin全液冷刚需"),
            ("液冷泵/阀", "飞龙股份·大元泵业·南方泵业·利欧股份", "CDU心脏/三客户认证", "22/37kW批量交付"),
            ("管路/密封件", "川环科技·腾龙股份·中石科技·联德股份", "45℃高温催生材料升级", "EPDM耐温耐腐升级"),
            ("冷源/冷却塔", "海鸥股份·冰轮环境·汉钟精机·佳力图", "园区一次侧/海外订单", "磁悬浮/闭式塔"),
        ]
        midstream = [
            ("冷板式集成(主线)", "英维克⭐·申菱环境·高澜股份·依米康·网宿科技", "全链条+Tier1认证/85亿订单", "毛利20-30%规模效应"),
            ("浸没式集成", "曙光数创·高澜股份·英维克", "国内浸没60%+市占/MW级相变", "高壁垒/超算万卡"),
            ("CDU专业厂", "申菱环境·宏盛股份·佳力图", "广达Meta/金标准认证", "系统心脏/认证最长"),
            ("精密温控", "英维克·申菱·同飞股份·朗进科技", "风冷+液冷/液冷占比提升", "跨界切入AIDC"),
        ]
        downstream = [
            ("AI服务器/OEM", "浪潮信息·工业富联·超聚变·宁畅·中科曙光", "整机预装液冷", "OEM升级液冷"),
            ("IDC/智算中心", "润泽科技·数据港·奥飞数据·光环新网·科华数据", "PUE<1.2合规必配", "capex增但OPEX降"),
            ("云厂商(客户)", "字节·腾讯·阿里·百度·美团·三大运营商", "7月万柜集采期", "采购方"),
            ("储能温控", "英维克·高澜·同飞·银轮·申菱", "第二曲线/5%→30%渗透", "技术同源"),
            ("动力电池/汽零跨界", "银轮·飞龙·三花·拓普·川环", "车规跨界AIDC/外溢订单", "产能/精密加工优势"),
            ("CPO/光模块液冷", "中石科技·鼎通·奕东·硕贝德·意华", "1.6T/3.2T液冷可插拔", "新增量2027放量"),
            ("电源液冷一体化", "英维克(方案)·欧陆通·麦格米特·中恒电气", "96%转换效率", "机构低估增量"),
        ]
        def render_chain(groups, color):
            h = ""
            for seg, stocks, logic, key in groups:
                h += f'''
                <div class="bg-white/[0.03] border border-{color}-500/20 rounded-lg p-2 mb-2">
                    <div class="text-{color}-400 font-bold text-xs mb-1">{seg}</div>
                    <div class="text-white/80 text-[11px] mb-1">{stocks}</div>
                    <div class="text-white/50 text-[10px]">🔑{key} | 💡{logic}</div>
                </div>'''
            return h
        content += f'''
        <div class="grid md:grid-cols-3 gap-3">
            <div>{self._glass_card(f'<h4 class="text-blue-400 font-bold mb-2 text-sm">🔷 上游材料/零部件</h4>' + render_chain(upstream, "blue"), pad="p-3")}</div>
            <div>{self._glass_card(f'<h4 class="text-purple-400 font-bold mb-2 text-sm">🔮 中游系统集成(核心)</h4>' + render_chain(midstream, "purple"), pad="p-3")}</div>
            <div>{self._glass_card(f'<h4 class="text-pink-400 font-bold mb-2 text-sm">🌸 下游应用场景</h4>' + render_chain(downstream, "pink"), pad="p-3")}</div>
        </div>'''
        return self._section("chain", "四、产业链全链路拆解：冷板主线+浸没成长+耗材复购", "🔗", content)

    def _sec_stocks(self):
        stocks = [
            (1, "002837", "英维克", "冷板式液冷绝对龙头，国内唯一英伟达PN Tier1+英特尔100%全链条双认证；Coolinside全自研覆盖冷板/快接/CDU/Manifold/工质/管路/冷源；冷板市占率42%+；在手液冷订单85亿+，Q1液冷+250-290%；客户覆盖谷歌/英伟达/字节/腾讯/阿里，泰国/美国基地出海。",
             (8, 10, 5, 7), ("7/6收盘", "74.06(+3.68%)"), "⭐持仓·冷板全链条龙头", True,
             "Rubin Q3+中报拐点+出海", "Q1净利-82%+动态PE高+铜铝成本", "核心压舱石·中长线"),
            (2, "301018", "申菱环境", "CDU液冷分配单元龙头，算力园区总包核心；东数西算多枢纽中标；运营商核心供货；45℃高温液冷适配Rubin；Q1液冷5.1-5.8亿+220-250%；华为Atlas950 CDU一级供应商，海外占比25%。",
             (8, 9, 6, 7), ("7/6收盘", "130.73(+6.13%)"), "CDU龙头·华为链", False,
             "昇腾Atlas950+1.31亿美元海外", "流通市值小波动大", "中线核心"),
            (3, "300499", "高澜股份", "冷板+浸没+喷淋三线全覆盖；数据中心+储能双线；Q1液冷4.2-4.8亿+180-210%，毛利率32%+8pct；通过英伟达/AMD认证订单排至2027；7/6+10.11%主力1.75亿。",
             (9, 8, 7, 8), ("7/6收盘", "41.94(+10.11%)"), "冷板+浸没双线", False,
             "冷板放量+储能液冷+弹性大", "储能周期+浸没待时", "短中线"),
            (4, "002536", "飞龙股份", "液冷电子水泵龙头（CDU心脏），8-37kW全覆盖；22kW批量，37kW新订单落地；绑定英伟达/华为/谷歌三巨头；2025民用液冷6.73亿+28%；机构预计2026液冷20-30亿、净利率20-22%。",
             (9, 8, 7, 8), ("7/6盘初", "+6.58%"), "液冷泵·三巨头认证", False,
             "37kW放量+三客户认证", "当前液冷占比15%", "短线高弹性"),
            (5, "872808", "曙光数创", "北交所浸没式龙头，背靠中科曙光；国内浸没市占率60%+；2026/4发布MW级相变浸没整机柜C8000(单机柜900kW，PUE<1.04)，提前实现英伟达2028指标；Q1液冷+780%；国家级超算供应商。",
             (9, 7, 6, 6), ("北交所", "浸没龙头"), "浸没式·超算", False,
             "MW相变+超算订单+780%增长", "北交所流动性+浸没体量小", "中长期浸没"),
            (6, "603757", "大元泵业", "液冷屏蔽泵核心供应商，长期配套英维克/申菱；7/6涨停+主力2.35亿；液冷泵批量交付，技术壁垒高。",
             (9, 7, 6, 8), ("7/6涨停", "79.19(+10.00%)"), "液冷泵·英维克/申菱配套", False,
             "泵类国产替代+情绪龙头", "市值小票波动大", "短线情绪龙头"),
            (7, "300602", "飞荣达", "导热/EMI/热管理龙头，AI服务器液冷散热模组+冷板核心供应商；华为/英伟达/苹果客户；导热器件+液冷板双线放量。",
             (8, 7, 7, 7), ("导热+液冷", "热管理全链条"), "导热+冷板", False,
             "华为链+多业务协同", "消费电子占比高", "中线"),
            (8, "600160", "巨化股份", "国内电子氟化液断层龙头，唯一量产高纯度电子氟化液；12万吨新产能2026投产；供货曙光/英维克/字节/阿里；打破3M垄断；耗材复购毛利率50%+穿越周期。",
             (7, 9, 8, 7), ("氟化液龙头", "耗材复购"), "氟化液·浸没耗材", False,
             "3M退+国产替代+耗材", "化工周期+浸没放量慢", "中长期价值"),
            (9, "300990", "同飞股份", "工业温控/液冷专业厂；冷板+浸没双线；订单排至2027；储能温控同步发力；7/6盘初+6.73%。",
             (8, 7, 7, 6), ("7/6盘初", "+6.73%"), "工业温控·浸没", False,
             "浸没订单排2027+储能", "市值小机构覆盖少", "中短线"),
            (10, "002126", "银轮股份", "汽车热管理龙头跨界AIDC；增资2.69亿墨西哥基地服务北美；液冷板/换热器技术同源；客户覆盖北美算力厂；7/6跟涨5%。",
             (7, 8, 8, 7), ("汽零+出海", "跟涨+5%"), "汽零跨界+出海", False,
             "墨西哥出海+北美订单", "车业务占比高", "中线价值"),
            (11, "603269", "海鸥股份", "冷却塔/冷源龙头；7/6涨停+主力1.56亿；液冷终端散热；多项国际认证；园区冷源配套。",
             (8, 6, 6, 8), ("7/6涨停", "+9.97%"), "冷却塔·冷源", False,
             "涨停情绪+冷源配套", "传统业务/壁垒低", "短线情绪"),
            (12, "000811", "冰轮环境", "园区冷源/磁悬浮冷水机组龙头；7/6盘初+7.86%；连续12日主力净买；配套华为/英伟达智算园区；海外英伟达改造大单。",
             (7, 8, 7, 8), ("7/6收盘", "53.63(+1.86%)"), "冷源·磁悬浮", False,
             "12日净买+海外订单", "PE 113偏高+传统业务", "中线趋势"),
            (13, "300684", "中石科技", "导热材料/EMI龙头；7/6+18.19%领涨板块；液冷散热+导热+CPO液冷；AI高导热材料爆发；短期弹性最强。",
             (10, 6, 5, 9), ("7/6领涨", "73.29(+18.19%)"), "导热+CPO液冷", False,
             "领涨+CPO新业务+情绪", "纯题材/估值高/业绩待验", "短线弹性"),
            (14, "603090", "宏盛股份", "CDU专业厂商，切入广达/Meta/英伟达供应链；7/6涨停+主力1.05亿；CDU金标准认证首批。",
             (9, 6, 6, 7), ("7/6涨停", "+10.00%"), "CDU·广达/Meta", False,
             "涨停+海外客户+CDU认证", "市值小/订单待验", "短线观察"),
            (15, "300547", "川环科技", "液冷管路/胶管龙头；汽零胶管跨界AIDC；Rubin 45℃高温液冷管路升级受益；客户覆盖多家液冷集成商。",
             (8, 6, 7, 6), ("管路", "胶管跨界"), "液冷管路", False,
             "高温管路升级+汽零产能", "液冷占比待提升", "补涨观察"),
        ]
        top_html = ""
        for s in stocks:
            top_html += self._stock_row(*s)
        extended = [
            ("300249", "依米康", "数据中心温控老牌，液冷布局中"),
            ("300017", "网宿科技", "CDN+边缘+液冷IDC"),
            ("300709", "精研科技", "MIM/散热/液冷结构件"),
            ("300594", "朗进科技", "轨交温控+数据中心液冷"),
            ("301128", "强瑞技术", "散热模组/液冷检测/华为供应商"),
            ("300145", "南方泵业", "水泵龙头+液冷泵，7/6+8.65%"),
            ("605060", "联德股份", "精密机械+液冷结构件，7/6涨停"),
            ("603203", "快克智能", "液冷焊接设备，7/6涨停"),
            ("002897", "意华股份", "高速连接器+液冷快接"),
            ("002518", "科士达", "UPS+液冷数据中心"),
            ("002335", "科华数据", "IDC+液冷温控"),
            ("300738", "奥飞数据", "IDC液冷改造"),
            ("603881", "数据港", "IDC液冷新建"),
            ("300442", "润泽科技", "3.6GW算力+液冷智算"),
            ("000977", "浪潮信息", "AI服务器整机液冷预装"),
            ("601138", "工业富联", "AI服务器OEM+液冷整机"),
            ("603019", "中科曙光", "超算+液冷服务器"),
            ("002050", "三花智控", "汽车热管理+液冷阀"),
            ("603305", "旭升集团", "铝压铸+液冷板"),
            ("002475", "立讯精密", "连接器+液冷整机"),
            ("603920", "世运电路", "PCB+液冷板配套"),
            ("002384", "东山精密", "PCB+散热模组"),
            ("002463", "沪电股份", "AI服务器PCB+液冷"),
            ("300679", "电连技术", "连接器+液冷快接"),
            ("002600", "领益智造", "散热/结构件+液冷"),
        ]
        ext_rows = ""
        for i, (code, name, biz) in enumerate(extended):
            is_hold = any(name == s.get("name") for s in self.holding_stocks)
            ext_rows += f'''
            <tr class="border-b border-white/5 text-xs {'bg-yellow-500/5' if is_hold else ''}">
                <td class="py-1 px-1 text-white/40">{i+16}</td>
                <td class="py-1 px-1 text-white">{"⭐" if is_hold else ""}{name}</td>
                <td class="py-1 px-1 text-white/40 font-mono">{code}</td>
                <td class="py-1 px-1 text-white/60">{biz}</td>
            </tr>'''
        content = self._glass_card(f'''
            <h3 class="text-white font-bold text-base mb-2">🏆 TOP15核心标的四维打分（弹性/确定性/估值/筹码 各10分，满分40）</h3>
            <p class="text-white/50 text-xs mb-3">弹性(市值/纯度/订单)、确定性(业绩/客户/壁垒)、估值(PE/PB/2026E匹配)、筹码(机构/龙虎榜/换手/融资)</p>
            {top_html}
        ''')
        content += self._glass_card(f'''
            <h3 class="text-white font-bold text-base mb-2">📚 产业链扩展标的池（25只，合计覆盖40只+）</h3>
            <p class="text-white/50 text-xs mb-2">含直接液冷+间接受益（IDC/服务器/汽零/电源/CPO/储能）</p>
            <div class="overflow-x-auto">
            <table class="w-full text-xs">
                <thead class="sticky top-0 bg-[#1a1735]"><tr class="text-white/50 border-b border-white/10">
                    <th class="py-1 px-1 text-left">#</th><th class="py-1 px-1 text-left">名称</th><th class="py-1 px-1 text-left">代码</th><th class="py-1 px-1 text-left">液冷业务</th>
                </tr></thead>
                <tbody>{ext_rows}</tbody>
            </table></div>
        ''')
        return self._section("stocks", "五、TOP15标的排名+扩展标的池", "🏆", content)

    def _sec_yingweike(self):
        content = self._glass_card(f'''
            <div class="flex items-center gap-3 mb-3 flex-wrap">
                <span class="holding-badge">⭐持仓股</span>
                <h3 class="text-white font-bold text-xl">英维克（002837）深度诊断</h3>
            </div>
            <div class="grid grid-cols-2 md:grid-cols-4 gap-3 mb-4">
                <div class="bg-white/[0.04] p-3 rounded-lg text-center border border-yellow-500/30">
                    <div class="text-xs text-white/50">持仓成本</div>
                    <div class="text-yellow-400 text-2xl font-black">104.23</div>
                </div>
                <div class="bg-white/[0.04] p-3 rounded-lg text-center border border-white/10">
                    <div class="text-xs text-white/50">最新价(7/6)</div>
                    <div class="text-white text-2xl font-black">74.06</div>
                </div>
                <div class="bg-white/[0.04] p-3 rounded-lg text-center border border-green-500/30">
                    <div class="text-xs text-white/50">浮亏</div>
                    <div class="text-green-400 text-2xl font-black">-28.9%</div>
                </div>
                <div class="bg-white/[0.04] p-3 rounded-lg text-center border border-white/10">
                    <div class="text-xs text-white/50">总市值</div>
                    <div class="text-white text-2xl font-black">944亿</div>
                </div>
            </div>
        ''', extra="border-2 border-yellow-500/30 holding-card")
        content += self._glass_card(f'''
            <h4 class="text-white font-bold text-sm mb-2">🎯 为什么不割肉（核心逻辑未变）</h4>
            <ul class="space-y-2 text-sm text-white/80">
                <li>✅ <b>产业地位无可替代</b>：国内唯一英伟达PN Tier1+英特尔100%全链条双认证液冷厂商，冷板市占率42%+，Coolinside全自研。</li>
                <li>✅ <b>客户矩阵豪华</b>：海外英伟达MGX/Blackwell+谷歌2MW CDU+Meta；国内字节/腾讯/阿里/百度/三大运营商。</li>
                <li>✅ <b>在手订单充足</b>：截至4月在手液冷订单85亿+，Q1液冷+250-290%，全年液冷冲击40-50亿。</li>
                <li>✅ <b>技术壁垒巩固</b>：6/24英特尔工质认证里程碑+SoluKing品牌+七大国内基地+泰国/美国海外基地，2GW+零漏液。</li>
                <li>✅ <b>双赛道</b>：数据中心液冷+储能温控（中东项目落地），平滑周期。</li>
            </ul>
        ''')
        content += self._glass_card(f'''
            <h4 class="text-red-400 font-bold text-sm mb-2">⚠️ 为什么跌（压力点）</h4>
            <ul class="space-y-2 text-sm text-white/70">
                <li>❌ <b>Q1利润暴雷</b>：Q1净利-82%，主因IDC项目延期减值+扩产财务费用+汇兑损失。</li>
                <li>❌ <b>估值贵</b>：TTM PE 100倍+，按2026E 10.69亿算PE 88倍，2027E 14.63亿算PE 64倍，已透支较多。</li>
                <li>❌ <b>竞争加剧</b>：申菱/高澜/银轮/飞龙/冰轮等跨界液冷，中低端价格战风险。</li>
                <li>❌ <b>海外不确定</b>：地缘/汇率/英伟达供应链调整。</li>
                <li>❌ <b>原材料波动</b>：铜/铝成本。</li>
                <li>❌ <b>账期问题</b>：数据中心项目账期长，现金流承压。</li>
            </ul>
        ''')
        content += self._glass_card(f'''
            <h4 class="text-yellow-400 font-bold text-sm mb-2">📊 机构盈利预测与估值</h4>
            <div class="overflow-x-auto">
            <table class="w-full text-xs">
                <thead><tr class="text-white/50 border-b border-white/10">
                    <th class="py-1 px-2 text-left">年份</th><th class="py-1 px-2 text-right">营收(亿)</th><th class="py-1 px-2 text-right">归母(亿)</th>
                    <th class="py-1 px-2 text-right">同比</th><th class="py-1 px-2 text-right">EPS</th><th class="py-1 px-2 text-right">PE@74元</th>
                </tr></thead>
                <tbody>
                    <tr class="border-b border-white/5"><td class="py-1">2024A</td><td class="py-1 text-right">42.4</td><td class="py-1 text-right">4.2</td><td class="py-1 text-right">—</td><td class="py-1 text-right">0.33</td><td class="py-1 text-right">224×</td></tr>
                    <tr class="border-b border-white/5"><td class="py-1">2025A</td><td class="py-1 text-right">~65</td><td class="py-1 text-right">~6.5</td><td class="py-1 text-right text-yellow-400">+55%</td><td class="py-1 text-right">0.51</td><td class="py-1 text-right">145×</td></tr>
                    <tr class="border-b border-white/5 bg-yellow-500/5"><td class="py-1 font-bold text-yellow-400">2026E</td><td class="py-1 text-right font-bold">~110</td><td class="py-1 text-right font-bold text-yellow-400">10.7</td><td class="py-1 text-right text-red-400 font-bold">+64%</td><td class="py-1 text-right">0.84</td><td class="py-1 text-right font-bold">88×</td></tr>
                    <tr class="border-b border-white/5"><td class="py-1">2027E</td><td class="py-1 text-right">~155</td><td class="py-1 text-right">14.6</td><td class="py-1 text-right text-yellow-400">+37%</td><td class="py-1 text-right">1.15</td><td class="py-1 text-right">64×</td></tr>
                    <tr><td class="py-1">2028E</td><td class="py-1 text-right">~200</td><td class="py-1 text-right">20+</td><td class="py-1 text-right">+35%</td><td class="py-1 text-right">1.57</td><td class="py-1 text-right text-green-400">47×</td></tr>
                </tbody>
            </table></div>
            <p class="text-white/60 text-[11px] mt-2">注：综合中信/高盛/长江一致预期；高盛12个月目标价118.6元。</p>
        ''')
        content += self._glass_card(f'''
            <h4 class="text-green-400 font-bold text-sm mb-2">💡 操作建议（成本104.23/现价74.06/浮亏-28.9%）</h4>
            <div class="grid md:grid-cols-2 gap-3">
                <div class="bg-green-500/10 border border-green-500/30 rounded-lg p-3">
                    <div class="text-green-400 font-bold text-sm mb-1">✅ 不割肉，逢低补仓摊薄</div>
                    <ul class="text-white/80 text-xs space-y-1">
                        <li>1. <b>核心逻辑未变</b>：J型拐点+龙头地位+85亿订单+双认证</li>
                        <li>2. <b>下跌是短期</b>：Q1汇兑/减值+板块调整+估值消化</li>
                        <li>3. <b>催化临近</b>：中报预告（7月中）/Rubin Q3/谷歌大单</li>
                        <li>4. <b>补仓策略</b>：72-75补1/3摊至~95；68-70补1/3至~88</li>
                        <li>5. <b>目标位</b>：第一88-95（减仓），第二105-118</li>
                    </ul>
                </div>
                <div class="bg-red-500/10 border border-red-500/30 rounded-lg p-3">
                    <div class="text-red-400 font-bold text-sm mb-1">⛔ 止损纪律（严格执行）</div>
                    <ul class="text-white/80 text-xs space-y-1">
                        <li>• <b>硬止损68元</b>（跌破离场，总亏-35%）</li>
                        <li>• 中报液冷增速<150%或毛利率下滑，减仓1/2</li>
                        <li>• Rubin明确延期2027，清仓</li>
                        <li>• 两市成交连续5日<2.2万亿+连跌，减仓观望</li>
                        <li>• 反弹至95-100先减1/3锁定</li>
                    </ul>
                </div>
            </div>
            <p class="text-white/70 text-sm mt-3">
                <b>核心判断：</b>英维克74元对应2027E PE 64倍，作为液冷绝对龙头估值合理偏低（2027E PEG≈1.7）；
                104元成本对应2027E PE 90倍，确实买入偏贵。<b class="text-yellow-400">通过补仓摊薄+反弹做T，有望Q4前回到90元区间，浮亏收窄至-15%内</b>。
                中报若超预期（净利+100%以上），年底有望重回100+。
            </p>
        ''')
        return self._section("yingweike", "六、⭐持仓诊断：英维克(002837) 不割肉逢低补仓", "⭐", content)

    def _sec_strategy(self):
        content = self._glass_card(f'''
            <h3 class="text-white font-bold text-base mb-3">🎯 三类投资者配置方案</h3>
            <div class="grid md:grid-cols-3 gap-3">
                <div class="bg-red-500/10 border border-red-500/30 rounded-lg p-3">
                    <div class="flex items-center gap-2 mb-2"><span class="text-2xl">⚡</span><span class="text-red-400 font-bold">短线（1-2周）</span></div>
                    <div class="text-white/60 text-[11px] mb-2">博弈板块脉冲/连板/情绪溢价</div>
                    <div class="text-white/80 text-xs space-y-1">
                        <div>🔥 弹性首选：<b class="text-red-400">高澜股份、中石科技、飞龙股份</b></div>
                        <div>🎰 情绪龙头：<b>大元泵业、海鸥股份、宏盛股份</b></div>
                        <div>🛡️ 止损：-8%严格止盈止损</div>
                        <div>⏰ 周期：3-10天</div>
                        <div>📌 仓位：≤15%，单票≤5%</div>
                    </div>
                </div>
                <div class="bg-purple-500/10 border border-purple-500/30 rounded-lg p-3">
                    <div class="flex items-center gap-2 mb-2"><span class="text-2xl">🎯</span><span class="text-purple-400 font-bold">中线（1-3月）</span></div>
                    <div class="text-white/60 text-[11px] mb-2">中报业绩验证+渗透率拐点</div>
                    <div class="text-white/80 text-xs space-y-1">
                        <div>🏆 核心配置：<b class="text-purple-400">英维克⭐、申菱环境、高澜股份</b></div>
                        <div>💎 价值辅助：<b>巨化股份(耗材)、银轮股份(出海)</b></div>
                        <div>🛡️ 止损：跌破20日线/中报不及预期减仓</div>
                        <div>⏰ 周期：1-3个月</div>
                        <div>📌 仓位：3-4成</div>
                    </div>
                </div>
                <div class="bg-blue-500/10 border border-blue-500/30 rounded-lg p-3">
                    <div class="flex items-center gap-2 mb-2"><span class="text-2xl">🏦</span><span class="text-blue-400 font-bold">长线（6-18月）</span></div>
                    <div class="text-white/60 text-[11px] mb-2">液冷渗透率12%→80%长期成长</div>
                    <div class="text-white/80 text-xs space-y-1">
                        <div>👑 龙头长期：<b class="text-blue-400">英维克⭐</b>（全链条壁垒）</div>
                        <div>💧 卖铲人：<b>巨化股份(氟化液耗材复购)</b></div>
                        <div>🔮 远期弹性：<b>曙光数创(浸没)</b></div>
                        <div>🌐 出海：<b>银轮股份、申菱环境</b></div>
                        <div>📌 仓位：核心2-3成，回调加仓</div>
                    </div>
                </div>
            </div>
        ''')
        content += self._glass_card(f'''
            <h3 class="text-white font-bold text-base mb-2">📅 行情节奏推演（2026H2）</h3>
            <div class="relative pl-6 border-l-2 border-purple-500/40">
                <div class="mb-4 relative">
                    <div class="absolute -left-[29px] w-4 h-4 rounded-full bg-red-500 border-2 border-white"></div>
                    <div class="text-red-400 font-bold text-sm">7月上中（当前）：预期启动期</div>
                    <p class="text-white/70 text-xs">7/6独立走强启动，研报密集催化，资金抢筹；重点关注7月15日前中报预告窗口。操作：<b>逢低布局冷板龙头+零部件弹性</b>。</p>
                </div>
                <div class="mb-4 relative">
                    <div class="absolute -left-[29px] w-4 h-4 rounded-full bg-orange-500 border-2 border-white"></div>
                    <div class="text-orange-400 font-bold text-sm">7月下-8月：业绩验证期（最关键）</div>
                    <p class="text-white/70 text-xs">中报密集披露，液冷龙头业绩兑现则板块升级S级主线，目标突破3000点；若不及预期则回踩。重点跟踪：英维克/申菱/高澜液冷收入增速、毛利率、订单指引。</p>
                </div>
                <div class="mb-4 relative">
                    <div class="absolute -left-[29px] w-4 h-4 rounded-full bg-yellow-500 border-2 border-white"></div>
                    <div class="text-yellow-400 font-bold text-sm">9-10月：Rubin交付+三季报</div>
                    <p class="text-white/70 text-xs">英伟达Rubin Q3批量交付，海外订单兑现；三季报验证持续增长；运营商万柜集采交付。Q2业绩验证后或主升。</p>
                </div>
                <div class="relative">
                    <div class="absolute -left-[29px] w-4 h-4 rounded-full bg-green-500 border-2 border-white"></div>
                    <div class="text-green-400 font-bold text-sm">11-12月：估值切换+2027预期</div>
                    <p class="text-white/70 text-xs">估值切换至2027E，业绩持续兑现则龙头PE修复至70-90倍；展望Rubin放量年+浸没起量。</p>
                </div>
            </div>
        ''')
        return self._section("strategy", "七、投资策略：短中长三线配置方案", "💡", content)

    def _sec_risk(self):
        risks = [
            ("AI算力Capex下修", "Meta/微软/谷歌Q2 Capex不及预期或AI商业化放缓导致订单后移"),
            ("英伟达Rubin延期", "Rubin延期至2027量产是最核心证伪信号"),
            ("行业价格战", "汽零/家电/机械企业跨界液冷导致中低端毛利率下行"),
            ("中报不及预期", "Q1英维克-82%，若H1毛利率下滑/汇兑损失继续则打击信心"),
            ("估值消化", "龙头TTM PE 80-150倍透支预期，业绩不匹配即回调"),
            ("地缘政治", "中美科技战/关税/供应链调整影响出海"),
            ("板块轮动", "资金快速切换至创新药/机器人/存储等主线导致补跌"),
            ("原材料波动", "铜/铝涨价压缩冷板/管路/换热器毛利"),
            ("技术路线变迁", "芯片级微流体/金刚石散热等颠覆性技术可能冲击现有产业链"),
        ]
        r_html = ""
        for i, (title, body) in enumerate(risks):
            r_html += f'<div class="flex gap-2 text-sm text-white/80 mb-2"><span class="text-red-400 flex-shrink-0">{i+1}.</span><span><b>{title}：</b>{body}</span></div>'
        content = self._glass_card(f'''
            <h3 class="text-red-400 font-bold text-base mb-3">⚠️ 核心风险提示</h3>
            {r_html}
            <div class="mt-4 p-3 bg-yellow-500/10 border border-yellow-500/30 rounded-lg">
                <p class="text-yellow-300 text-xs font-bold">⚠️ 免责声明：本报告基于公开信息整理，仅作为投资研究参考，不构成任何投资建议。股市有风险，投资需谨慎。</p>
            </div>
        ''')
        content += self._source_summary_section()
        return self._section("risk", "八、风险提示与免责声明", "⚠️", content)

    def _content(self):
        header = f'''
        <div class="text-center mb-8 mt-4">
            <div class="inline-block bg-gradient-to-r from-cyan-500/20 via-blue-500/20 to-purple-500/20 border border-cyan-500/30 rounded-full px-4 py-1 mb-3">
                <span class="text-cyan-300 text-xs font-semibold">🔥 产业链深度研究 · 2026年7月7日</span>
            </div>
            <h1 class="text-3xl md:text-4xl font-black text-white mb-2 tracking-tight">液冷散热产业链深度研究报告</h1>
            <p class="text-white/60 text-sm mb-2">物理定律强制下的AI算力散热刚需 · 能否成为下一个主线？</p>
            <div class="flex items-center justify-center gap-4 text-xs text-white/40 flex-wrap">
                <span>📅 2026-07-07 盘前</span>
                <span>📊 覆盖40+核心标的</span>
                <span>⭐ 含英维克持仓诊断</span>
                <span>📏 8大章节全链路拆解</span>
            </div>
        </div>'''
        return "\n".join([
            header,
            self._sec_verify(),
            self._sec_logic(),
            self._sec_sustain(),
            self._sec_chain(),
            self._sec_stocks(),
            self._sec_yingweike(),
            self._sec_strategy(),
            self._sec_risk(),
        ])


def main():
    g = LiquidCoolingReportGenerator()
    g.load_data()
    out = "/root/daily-news-insight/docs/industry_chain/20260707_液冷散热产业链深度研究报告.html"
    res = g.publish(out)
    print(f"结果: {res}")
    if not res.get('success'):
        print("ERRORS:", res.get('errors'))
        return 1
    print(f"✅ 报告已生成: {out}")
    print(f"   文件大小: {res['file_size']/1024:.1f} KB")
    return 0


if __name__ == "__main__":
    sys.exit(main())
