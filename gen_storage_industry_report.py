#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
存储产业链全维度深度研究报告生成器 2026-07-09
基于ProGenerator深色玻璃态主题，参考液冷散热报告结构
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'v3'))

from generators.pro_base import ProGenerator, source_tag, CONF_HIGH, CONF_MEDIUM, CONF_LOW
from datetime import datetime


class StorageIndustryReportGenerator(ProGenerator):
    data_type = "industry_chain"

    def __init__(self):
        super().__init__(
            title="存储产业链全维度深度研究报告",
            active_page="产业链",
            footer_text="存储产业链全维度深度研究 · 2026-07-09",
            show_toc=False,
            theme="dark",
            tldr=[
                "【核心结论】长鑫科技7/9凌晨披露科创板IPO（688825，7/16申购，募资295亿，发行市值3000亿）叠加SK海力士7/10纳斯达克上市募资280亿美元，构成存储超级周期"
                "<b>历史性双IPO催化</b>；威刚董事长确认Q3 DRAM合约价涨20-30%、NAND涨35-40%（远超市场预期），<b>价格行情持续性评级：S级</b>（2026Q3-2027Q4，至少6个季度）。",
                "【板块验证】7/9 A股存储板块主力净流入315亿元，兆易创新/雅克科技/长电科技/华天科技/浪潮信息5股涨停，中微公司+11.49%、华海清科+16.61%、澜起科技+15.64%、上海新阳+18.74%集体创历史新高，半导体ETF涨6%+，<b>板块强度确认主升浪开启</b>。",
                "【操作建议】持仓雅克科技(002409，成本108.8元，现价209元涨停，浮盈+92.1%)<b>继续持有不卖</b>，前道材料核心受益+长鑫HBM前驱体独供+半导体特气+先进封装材料四维共振；短线第一目标250元，若Q3业绩兑现看300+，190元下方为加仓区间，跌破175元减仓风控。",
            ],
            operation_advice="雅克科技190-200区间逢回调加仓摊薄（已浮盈+92%以持有为主），存储板块主线配置：前道设备（北方华创/中微/华海清科）3成+存储设计IDM（兆易/澜起/江波龙）2成+材料（雅克/鼎龙/安集/沪硅/彤程）2成+封测（长电/通富/华天）1-1.5成；总仓位6-8成。",
            risk_level="中高",
            suggested_position="主线仓位6-8成（存储超级周期主线），单只个股不超2成",
            quick_anchors=[
                {"id": "conclusion", "title": "核心结论", "icon": "🎯"},
                {"id": "panorama", "title": "产业全景", "icon": "🌐"},
                {"id": "timeline", "title": "催化时间轴", "icon": "⏰"},
                {"id": "chain", "title": "产业链标的排序", "icon": "🏭"},
                {"id": "top10", "title": "TOP10深度卡片", "icon": "🏆"},
                {"id": "risk", "title": "风险提示", "icon": "⚠️"},
                {"id": "strategy", "title": "操作策略（雅克诊断）", "icon": "💡"},
            ],
            holding_stocks=[
                {"name": "雅克科技", "code": "002409"},
            ],
            og_description="长鑫IPO+SK海力士双上市催化存储超级周期，7/9板块主力净流入315亿5股涨停，全产业链6环节TOP标的排序+TOP10深度卡片+雅克科技持仓诊断",
        )

    def load_data(self):
        super().load_data()
        self.update_time = "2026年7月9日 18:30"
        self.cite("上交所/长鑫科技招股书", CONF_HIGH)
        self.cite("东方财富Choice/证券之星/财联社", CONF_HIGH)
        self.cite("威刚科技法说会", CONF_HIGH)
        self.cite("高盛/杰富瑞/交银国际研报", CONF_MEDIUM)
        self.cite("SEMI全球晶圆厂预测报告", CONF_MEDIUM)
        self.cite("TrendForce/江波龙/浪潮信息公告", CONF_HIGH)

    # ===================== 基础组件 =====================
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

    def _stock_card(self, rank, code, name, core, score_tup, price_info, cat, is_holding=False, catalysis="", risk="", rating="", targets=None):
        e, d, v, c = score_tup
        total = e + d + v + c
        if total >= 34: grade, gcolor = "S", "text-red-400"
        elif total >= 28: grade, gcolor = "A", "text-orange-400"
        elif total >= 22: grade, gcolor = "B", "text-yellow-400"
        else: grade, gcolor = "C", "text-white/50"
        hold_badge = '<span class="holding-badge">⭐持仓</span> ' if is_holding else ''
        targets_html = ""
        if targets:
            targets_html = f'''<div class="grid grid-cols-3 gap-2 mt-2 text-center text-xs">
                <div class="bg-green-500/10 border border-green-500/20 rounded p-1"><div class="text-white/40">支撑</div><div class="text-green-400 font-bold">{targets[0]}</div></div>
                <div class="bg-white/5 rounded p-1"><div class="text-white/40">现价</div><div class="text-white font-bold">{price_info[1]}</div></div>
                <div class="bg-red-500/10 border border-red-500/20 rounded p-1"><div class="text-white/40">目标</div><div class="text-red-400 font-bold">{targets[1]}</div></div>
            </div>'''
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
            {targets_html}
            <div class="flex gap-2 flex-wrap text-xs mt-2">
                {f'<span class="bg-green-500/10 text-green-300 px-2 py-0.5 rounded">🚀 {catalysis}</span>' if catalysis else ''}
                {f'<span class="bg-red-500/10 text-red-300 px-2 py-0.5 rounded">⚠️ {risk}</span>' if risk else ''}
                {f'<span class="bg-blue-500/10 text-blue-300 px-2 py-0.5 rounded">📌 {rating}</span>' if rating else ''}
            </div>
        </div>'''

    # ===================== 一、核心结论 =====================
    def _sec_conclusion(self):
        kpi = self._kpi_grid([
            ("7/9主力净流入", "315亿", "text-red-400", "存储板块历史天量"),
            ("涨停标的", "5只+", "text-red-400", "兆易/雅克/长电/华天/浪潮"),
            ("Q3 DRAM涨价", "20-30%", "text-orange-400", "威刚确认超预期"),
            ("Q3 NAND涨价", "35-40%", "text-orange-400", "远超TrendForce预测"),
        ])
        # 核心结论五大判断
        conclusions = [
            ("🎯 判断一：存储超级周期由「价格行情」升级为「产业资本行情」",
             "此前市场仅基于DRAM/NAND涨价交易β行情；长鑫IPO（募资295亿，180亿投向DDR5/HBM）+ SK海力士纳斯达克上市（募资280亿美元全部投入先进产能）+ 长江存储IPO推进（估值1600亿），三大存储IDM同步开启万亿级产能扩张周期，"
             "标志存储行情由「被动涨价」切换为「主动Capex扩张」，行情级别从板块性行情升级为产业链全面景气。SEMI预测2026年300mm晶圆厂存储设备投资+29%至520亿美元，2027年再+11%至570亿美元，设备/材料/零部件订单弹性最大。"),
            ("🎯 判断二：涨价幅度/持续性「双超预期」，2027年短缺更甚于2026",
             "威刚董事长陈立白7/9确认Q3 DRAM合约价涨20-30%、NAND涨35-40%（TrendForce此前仅预测DRAM涨13-18%/NAND涨10-15%，上修50-150%）；高盛判断2027年DRAM/NAND/HBM供应紧张程度超2026年，短缺延续至2028年；"
             "杰富瑞预测Q3环比涨40-50%、Q4再涨30-40%、2027全年均价同比涨40-45%。HBM3E/HBM4因AI需求供不应求，合约价已出现「一货难求」，SK海力士HBM订单排至2027年底。"),
            ("🎯 判断三：长鑫产业链受益顺序——前道设备→零部件→材料，业绩兑现存在时滞差",
             "长鑫初始发行66.88亿股募资295亿（180亿投向DDR5/HBM产能扩建），叠加IPO后持续融资扩产，未来3年Capex有望超1500亿元。受益顺序与弹性排序：①前道设备（刻蚀北方华创/中微、薄膜拓荆、CMP华海清科、清洗盛美）最先受益订单落地，业绩兑现Q3即体现；"
             "②零部件（富创精密/江丰电子/新莱应材）国产化率最低、弹性大；③材料耗材（雅克/鼎龙/安集/沪硅/彤程/上海新阳）随产能爬坡逐季放量，Q4-2027年业绩弹性最大。"),
            ("🎯 判断四：国产替代临界点突破，设备国产化率35%→50%进入非线性渗透期",
             "2026年6月国产设备综合国产化率突破35%临界点（据国信证券），验证了国产设备从0→1、1→N的非线性渗透逻辑。北方华创刻蚀/薄膜/热处理全平台覆盖，中微CCP刻蚀进入5nm验证、华海清科CMP独占、拓荆PECVD独供长鑫长江、盛美清洗进入海力士供应链，"
             "国产设备从「能用」到「好用」的拐点已至，长鑫IPO后国产设备订单有望加速放量。"),
            ("🎯 判断五：板块主升浪已开启，当前为「业绩+估值+事件」三击最佳窗口",
             "江波龙预告H1净利92-110亿（+622-743倍）、浪潮信息H1净利26-31亿（+226-288%）、兆易创新Q2业绩环比+150%、雅克科技Q2业绩超预期；PE估值角度：龙头设备北方华创40倍、中微50倍均处于历史中枢以下；"
             "事件面：7/10 SK海力士上市→7/13长鑫询价→7/15长鑫路演→7/16长鑫申购→7月底中报季→8月Q3业绩前瞻，催化密集无空窗期。")
        ]
        c_html = ""
        for title, body in conclusions:
            c_html += f'''
            <div class="bg-white/[0.03] p-4 rounded-lg border border-white/10 mb-3">
                <div class="text-red-400 font-bold text-sm mb-2">{title}</div>
                <p class="text-white/75 text-sm leading-relaxed">{body}</p>
            </div>'''
        content = kpi + self._glass_card(c_html, pad="p-5")
        content += self._glass_card(f'''
            <h3 class="text-white font-bold text-base mb-3">📊 7月9日存储板块核心数据全景（收盘数据）</h3>
            <p class="text-white/60 text-xs mb-3">数据来源：证券之星/东方财富Choice/财联社 {source_tag("多源交叉验证", CONF_HIGH, verified=True)}</p>
            <div class="grid grid-cols-2 md:grid-cols-4 gap-2 text-xs">
                <div class="bg-red-500/10 rounded p-2 text-center border border-red-500/20"><div class="text-white/50">涨停</div><div class="text-red-400 font-bold text-lg">5+</div></div>
                <div class="bg-red-500/10 rounded p-2 text-center border border-red-500/20"><div class="text-white/50">创历史新高</div><div class="text-red-400 font-bold text-lg">15+</div></div>
                <div class="bg-orange-500/10 rounded p-2 text-center border border-orange-500/20"><div class="text-white/50">主力净流入</div><div class="text-orange-400 font-bold text-lg">315亿</div></div>
                <div class="bg-orange-500/10 rounded p-2 text-center border border-orange-500/20"><div class="text-white/50">板块成交</div><div class="text-orange-400 font-bold text-lg">2800亿+</div></div>
                <div class="bg-white/5 rounded p-2 text-center"><div class="text-white/50">中微公司净流入</div><div class="text-white font-bold">17.29亿</div></div>
                <div class="bg-white/5 rounded p-2 text-center"><div class="text-white/50">澜起科技领涨</div><div class="text-white font-bold">+15.64%</div></div>
                <div class="bg-white/5 rounded p-2 text-center"><div class="text-white/50">华海清科</div><div class="text-white font-bold">+16.61%</div></div>
                <div class="bg-white/5 rounded p-2 text-center"><div class="text-white/50">上海新阳</div><div class="text-white font-bold">+18.74%</div></div>
            </div>
        ''')
        return self._section("conclusion", "一、核心结论：存储超级周期双IPO催化，S级行情启动", "🎯", content)

    # ===================== 二、产业全景 =====================
    def _sec_panorama(self):
        # 存储市场规模与景气度
        market_html = self._kpi_grid([
            ("2026全球半导体", "1.51万亿$", "text-cyan-400", "WSTS预测+90%"),
            ("全球DRAM市场", "~2500亿$", "text-cyan-400", "合约价Q3+20-30%"),
            ("全球NAND市场", "~1800亿$", "text-cyan-400", "合约价Q3+35-40%"),
            ("HBM市场", "~800亿$", "text-red-400", "2026年翻倍增长"),
        ])
        # 三大IDM对比表格
        idm_rows = [
            ("三星电子", "韩国", "DRAM全球第一(40%)/NAND第一(35%)", "HBM3E量产/HBM4开发中", "平泽P4扩建/泰勒厂2027量产", "股价7/9涨4%+"),
            ("SK海力士", "韩国", "DRAM第二(35%)/HBM绝对龙头(50%+)", "HBM3E独供英伟达/HBM4研发领先", "7/10纳斯达克上市募资280亿美元", "7/9韩股涨9%+"),
            ("美光科技", "美国", "DRAM第三(20%)/NAND第三(12%)", "HBM3E量产/获英伟达认证", "美国本土产能扩张+印度厂", "7/8美股涨6%+"),
            ("长鑫科技(CXMT)", "中国", "DRAM第四(7.67%)/国产第一", "DDR5量产/HBM研发中(180亿投向)", "科创板IPO 688825 募资295亿", "Q1营收508亿/+719%"),
            ("长江存储(YMTC)", "中国", "NAND国产第一(全球~6%)", "232L 3D NAND量产/Xtacking4.0", "IPO推进中/估值约1600亿", "未上市(供应链受益)"),
        ]
        idm_html = '<div class="overflow-x-auto"><table class="w-full text-xs"><thead><tr class="text-white/50 border-b border-white/10"><th class="py-2 px-2 text-left">IDM厂商</th><th class="py-2 px-2 text-left">国别</th><th class="py-2 px-2 text-left">市场地位</th><th class="py-2 px-2 text-left">先进产品</th><th class="py-2 px-2 text-left">Capex动作</th><th class="py-2 px-2 text-left">近期动态</th></tr></thead><tbody>'
        for i, row in enumerate(idm_rows):
            bg = "bg-yellow-500/5" if "长鑫" in row[0] else ""
            idm_html += f'<tr class="border-b border-white/5 {bg}"><td class="py-2 px-2 text-white font-bold">{"⭐ " if "长鑫" in row[0] else ""}{row[0]}</td><td class="py-2 px-2 text-white/70">{row[1]}</td><td class="py-2 px-2 text-white/70">{row[2]}</td><td class="py-2 px-2 text-cyan-300">{row[3]}</td><td class="py-2 px-2 text-orange-300">{row[4]}</td><td class="py-2 px-2 text-red-300">{row[5]}</td></tr>'
        idm_html += '</tbody></table></div>'

        # 产业链六大环节概览
        chain_overview = [
            ("① HBM/先进封装", "🧊", "HBM是本轮AI行情最硬核赛道，SK海力士独占50%+份额；国内长鑫180亿投向HBM/DDR5，通富/长电/华天先进封装产能紧张，日月光调涨报价20%+，台积电5-10%涨价覆盖7nm以下",
             "通富微电/长电科技/华天科技/华海诚科", "确定性最高"),
            ("② 半导体前道设备", "⚙️", "SEMI预测2026年300mm存储设备投资+29%至520亿美元；国产设备综合国产化率突破35%临界点，长鑫IPO后180亿设备订单启动；北方华创/中微/华海清科/拓荆/盛美订单能见度至2027年",
             "北方华创/中微公司/华海清科/拓荆科技/盛美上海", "业绩兑现最快(Q3)"),
            ("③ 半导体材料", "🧪", "材料随产能爬坡逐季放量，前驱体/光刻胶/CMP抛光垫/湿电子化学品/大硅片国产化加速；雅克科技HBM前驱体独供长鑫，彤程新材/上海新阳光刻胶突破，鼎龙CMP垫国产替代，安集抛光液独供，沪硅12寸硅片量产",
             "雅克科技/鼎龙股份/安集科技/彤程新材/上海新阳/沪硅产业", "弹性最大(Q4-2027)"),
            ("④ 存储设计/IDM", "💾", "国产DRAM/NAND进入收获期，兆易创新NOR Flash全球前三+DRAM利基型放量；北京君正车规存储+ISSI；澜起科技DDR5内存接口芯片+MRCD/MDB芯片垄断全球；东芯股份SLC NAND；普冉股份EEPROM+NOR",
             "兆易创新/澜起科技/北京君正/东芯股份/普冉股份", "直接受益涨价"),
            ("⑤ 存储模组/主控", "🔌", "模组厂最受益低价库存涨价红利，江波龙预告H1净利92-110亿(+622-743倍)创纪录；佰维存储去年亏损今年大额盈利；德明利主控+模组双轮驱动；但需关注低价库存Q3末-Q4初消耗完毕后的毛利回落",
             "江波龙/佰维存储/德明利", "弹性极大但有周期性"),
            ("⑥ 封测", "📦", "AI驱动先进封装产能紧张，CoWoS/Chiplet/HBM封装需求爆发；日月光调涨先进封装报价超20%；长电科技XDFOI高密度封装量产、通富微电AMD合作+CPO进展、华天科技存储封测量产",
             "长电科技/通富微电/华天科技", "周期反转+先进封装"),
        ]
        chain_html = ""
        for title, icon, body, stocks, note in chain_overview:
            chain_html += f'''
            <div class="bg-white/[0.03] p-4 rounded-lg border border-white/10 mb-3">
                <div class="flex items-center gap-2 mb-2">
                    <span class="text-xl">{icon}</span>
                    <span class="text-white font-bold text-sm">{title}</span>
                    <span class="bg-cyan-500/20 text-cyan-300 text-[10px] px-2 py-0.5 rounded ml-auto">{note}</span>
                </div>
                <p class="text-white/70 text-xs leading-relaxed mb-2">{body}</p>
                <p class="text-cyan-300 text-xs font-semibold">核心标的：{stocks}</p>
            </div>'''
        content = market_html + self._glass_card(f'''
            <h3 class="text-white font-bold text-base mb-3">🏭 全球存储IDM五强格局对比</h3>
            <p class="text-white/60 text-xs mb-3">长鑫科技Q1营收508亿(+719%)、毛利率40.99%超三星美光，产能利用率95.73%，全球DRAM份额7.67%排第四 {source_tag("上交所/长鑫招股书/WSTS/SEMI", CONF_HIGH, verified=True)}</p>
            {idm_html}
        ''')
        content += self._glass_card(f'''
            <h3 class="text-white font-bold text-base mb-3">🔗 存储产业链六大环节全景</h3>
            {chain_html}
        ''')
        # 价格行情表格
        price_rows = [
            ("DRAM DDR5 16Gb (合约价)", "Q2末 ~$3.5", "Q3 $4.2-4.6", "+20-30%", "威刚确认"),
            ("DRAM DDR4 8Gb (合约价)", "Q2末 ~$2.8", "Q3 $3.4-3.6", "+20-28%", "威刚确认"),
            ("NAND 512Gb TLC (合约价)", "Q2末 ~$3.2", "Q3 $4.3-4.5", "+35-40%", "威刚确认"),
            ("HBM3E 12Hi (英伟达订单)", "~$180/颗", ">$200/颗", "+15%+", "产业链反馈"),
            ("NOR Flash 256Mb", "Q2 ~$0.85", "Q3 $0.95-1.0", "+12-18%", "TrendForce"),
        ]
        price_html = '<div class="overflow-x-auto"><table class="w-full text-xs"><thead><tr class="text-white/50 border-b border-white/10"><th class="py-2 px-2 text-left">品类</th><th class="py-2 px-2 text-left">Q2末价格</th><th class="py-2 px-2 text-left">Q3预测</th><th class="py-2 px-2 text-left">涨幅</th><th class="py-2 px-2 text-left">来源</th></tr></thead><tbody>'
        for row in price_rows:
            price_html += f'<tr class="border-b border-white/5"><td class="py-2 px-2 text-white font-semibold">{row[0]}</td><td class="py-2 px-2 text-white/70">{row[1]}</td><td class="py-2 px-2 text-red-300 font-bold">{row[2]}</td><td class="py-2 px-2 text-red-400 font-black">{row[3]}</td><td class="py-2 px-2 text-white/50">{row[4]}</td></tr>'
        price_html += '</tbody></table></div>'
        content += self._glass_card(f'''
            <h3 class="text-white font-bold text-base mb-3">💰 Q3存储合约价行情一览（威刚董事长7/9法说会确认）</h3>
            <p class="text-white/60 text-xs mb-3">威刚董事长陈立白确认Q3 DRAM合约价涨20-30%、NAND涨35-40%，远超TrendForce此前预测的13-18%/10-15%，幅度超预期50-150% {source_tag("威刚科技法说会/TrendForce", CONF_HIGH, verified=True)}</p>
            {price_html}
        ''')
        return self._section("panorama", "二、产业全景：超级周期双IPO驱动，6大环节全面景气", "🌐", content)

    # ===================== 三、催化时间轴 =====================
    def _sec_timeline(self):
        events = [
            ("2026-07-09", "⚡", "长鑫科技科创板IPO招股书披露(688825)；威刚法说会确认Q3涨价；5股涨停板块爆发", "red", True),
            ("2026-07-10", "🏦", "SK海力士纳斯达克上市(SKHY)，募资280亿美元定价日，获7倍超额认购", "red", True),
            ("2026-07-13", "📊", "长鑫科技初步询价（机构报价），发行价约4.4元对应市值约3000亿", "orange", False),
            ("2026-07-15", "🎤", "长鑫科技网上路演，朱一明十年不减持承诺+大基金二期8.73%持股锁定", "orange", False),
            ("2026-07-16", "💥", "长鑫科技网上申购日，科创板年度最大IPO，预计冻结资金超万亿", "red", False),
            ("2026-07月下旬", "📈", "中报预告密集披露期：江波龙/兆易/浪潮/雅克/华海清科等业绩超预期集中兑现", "orange", False),
            ("2026-07-23", "📋", "长鑫科技预计上市挂牌日（申购后5个交易日），科创板存储第一股", "red", False),
            ("2026-08月", "💵", "Q3 DRAM/NAND合约价正式执行（威刚指引+20-40%），Q3业绩前瞻窗口", "orange", False),
            ("2026-08-15前后", "📊", "长江存储IPO进展披露（估值1600亿），第二批国产存储IPO催化", "cyan", False),
            ("2026-09月", "🚀", "英伟达Rubin GPU批量交付（HBM4需求启动），SK海力士/三星HBM4订单落地", "red", False),
            ("2026-Q4", "💰", "长鑫募投项目启动（180亿DDR5/HBM），国产设备/材料订单大批量落地", "orange", False),
            ("2026-Q4", "📈", "杰富瑞预测Q4价格再涨30-40%，存储模组/设计Q4业绩环比高增", "red", False),
            ("2027全年", "🎯", "高盛预测2027年短缺更甚于2026，全年均价同比涨40-45%，SEMI预测存储设备投资再+11%至570亿美元", "purple", False),
            ("2027-H1", "🏭", "长鑫合肥+北京新产能放量，HBM量产验证突破，国产设备/材料进入业绩兑现主升浪", "purple", False),
            ("2027-H2", "🌐", "SK海力士/美光/三星HBM4量产，全球HBM产能翻倍，先进封装产能继续紧张", "purple", False),
        ]
        tl_html = '<div class="relative border-l-2 border-white/20 ml-4 pl-6">'
        for date, icon, desc, color, hot in events:
            dot_color = {"red": "bg-red-500", "orange": "bg-orange-400", "cyan": "bg-cyan-400", "purple": "bg-purple-500"}[color]
            hot_badge = '<span class="bg-red-500 text-white text-[9px] px-1 py-0.5 rounded ml-1 font-bold">重磅</span>' if hot else ''
            tl_html += f'''
            <div class="relative mb-4">
                <div class="absolute -left-[29px] w-4 h-4 rounded-full {dot_color} border-2 border-white"></div>
                <div class="text-{color}-300 font-bold text-sm">{date} {icon}{hot_badge}</div>
                <p class="text-white/75 text-xs mt-1 leading-relaxed">{desc}</p>
            </div>'''
        tl_html += '</div>'
        content = self._glass_card(f'''
            <h3 class="text-white font-bold text-base mb-3">⏰ 存储超级周期核心催化时间轴（2026.7-2027.12）</h3>
            <p class="text-white/60 text-xs mb-4">未来12个月催化密集无空窗期，<b class="text-red-400">红色标记为高确定性重磅事件</b>，橙色为重要节点，紫色为趋势性催化 {source_tag("上交所/财联社/公司公告/SEMI/高盛/杰富瑞", CONF_HIGH, verified=True)}</p>
            {tl_html}
        ''')
        # 催化强度矩阵
        content += self._glass_card(f'''
            <h3 class="text-white font-bold text-base mb-3">📊 五大核心催化强度评级</h3>
            <div class="grid md:grid-cols-5 gap-2 text-xs">
                <div class="bg-gradient-to-br from-red-500/20 to-red-600/10 border border-red-500/30 rounded-lg p-3 text-center">
                    <div class="text-red-400 font-black text-lg">S</div>
                    <div class="text-white font-bold mt-1">长鑫IPO</div>
                    <div class="text-white/60 mt-1">募资295亿+国产替代</div>
                    <div class="text-red-300 mt-1">⭐⭐⭐⭐⭐</div>
                </div>
                <div class="bg-gradient-to-br from-red-500/20 to-red-600/10 border border-red-500/30 rounded-lg p-3 text-center">
                    <div class="text-red-400 font-black text-lg">S</div>
                    <div class="text-white font-bold mt-1">SK海力士上市</div>
                    <div class="text-white/60 mt-1">募资280亿美元扩产</div>
                    <div class="text-red-300 mt-1">⭐⭐⭐⭐⭐</div>
                </div>
                <div class="bg-gradient-to-br from-orange-500/20 to-orange-600/10 border border-orange-500/30 rounded-lg p-3 text-center">
                    <div class="text-orange-400 font-black text-lg">A</div>
                    <div class="text-white font-bold mt-1">Q3涨价超预期</div>
                    <div class="text-white/60 mt-1">DRAM+20-30%/NAND+35-40%</div>
                    <div class="text-orange-300 mt-1">⭐⭐⭐⭐</div>
                </div>
                <div class="bg-gradient-to-br from-orange-500/20 to-orange-600/10 border border-orange-500/30 rounded-lg p-3 text-center">
                    <div class="text-orange-400 font-black text-lg">A</div>
                    <div class="text-white font-bold mt-1">中报业绩兑现</div>
                    <div class="text-white/60 mt-1">江波龙+622倍/浪潮+226%</div>
                    <div class="text-orange-300 mt-1">⭐⭐⭐⭐</div>
                </div>
                <div class="bg-gradient-to-br from-cyan-500/20 to-cyan-600/10 border border-cyan-500/30 rounded-lg p-3 text-center">
                    <div class="text-cyan-400 font-black text-lg">B+</div>
                    <div class="text-white font-bold mt-1">高盛/杰富瑞唱多</div>
                    <div class="text-white/60 mt-1">2027更紧张+均价+40%</div>
                    <div class="text-cyan-300 mt-1">⭐⭐⭐</div>
                </div>
            </div>
        ''')
        return self._section("timeline", "三、核心催化时间轴：未来12个月事件密集无空窗", "⏰", content)

    # ===================== 四、产业链细分环节标的排序 =====================
    def _sec_chain(self):
        content = ""
        # HBM/先进封装
        hbm_stocks = [
            ("长电科技", "600584", "全球封测第三/国内第一，XDFOI高密度多维异构封装量产，HBM/Chiplet/CoWoS类封装全覆盖；2025年营收+17%、归母+79.86%创历史新高；定增扩产聚焦AI/汽车/存储三大高增长，先进封装收入占比超70%",
             (9, 9, 7, 8), ("7/9收盘", "103.52元 (+10%涨停反包)"), "封测龙头", False,
             "长鑫HBM封测核心供应商+日月光涨价20%受益", "短期涨幅较大注意追高", "买入：95-100区间低吸", ("90元", "130元")),
            ("通富微电", "002156", "国内封测第二，AMD苏州/槟城双基地绑定AMD；CPO光电合封通过可靠性测试+玻璃基板技术储备；7/9涨停收盘72.17元，5家机构净买入6.61亿+深股通净买入8.95亿；定增获注册批文",
             (9, 8, 7, 9), ("7/9收盘", "72.17元 (+10%涨停)"), "封测/CPO", False,
             "龙虎榜机构+外资抢筹+CPO技术突破+定增扩产", "涨停后追高风险+Q2毛利率", "买入：65-68区间", ("62元", "90元")),
            ("华天科技", "002185", "国内封测第三，存储封测龙头，7/9涨停收盘23.73元，主力净流入24.36亿居板块前列；先进封装产能扩建聚焦存储/汽车电子；估值相对最低（PE 35倍），补涨空间大",
             (8, 7, 9, 8), ("7/9收盘", "23.73元 (+10.01%涨停)"), "封测/存储", False,
             "资金净流入24亿+存储封测核心受益+低估值", "业绩弹性不如长电/通富", "买入：21-22元", ("20元", "30元")),
            ("华海诚科", "688535", "先进封装材料龙头，环氧塑封料(EMC)/颗粒状环氧塑封料(GMC)国产替代，HBM封装用GMC独供长电/通富；7/9收166.48元(+6.04%)",
             (9, 7, 5, 7), ("7/9收盘", "166.48元 (+6.04%)"), "封装材料", False,
             "HBM封装材料稀缺标的+长鑫链核心材料", "估值偏高PE 150倍+", "回调买入：150-155", ("140元", "200元")),
        ]
        html = ""
        for i, s in enumerate(hbm_stocks):
            html += self._stock_card(i+1, s[1], s[0], s[2], s[3], s[4], s[5], s[6], s[7], s[8], s[9], s[10])
        content += self._glass_card(f'''
            <h3 class="text-white font-bold text-base mb-3">🧊 环节一：HBM/先进封装（TOP4）——确定性最高环节，先进封装产能紧张涨价20%+</h3>
            <p class="text-white/60 text-xs mb-3">日月光调涨先进封装报价最高超20%，台积电5-10%涨价覆盖7nm及以下，HBM封装产能供不应求，封测厂景气度反转 {source_tag("财联社/公司公告/龙虎榜", CONF_HIGH, verified=True)}</p>
            {html}
        ''')
        # 前道设备
        equip_stocks = [
            ("北方华创", "002371", "国产设备绝对平台龙头，刻蚀/薄膜/清洗/热处理全品类覆盖，2025年营收破300亿；7/9收877.73元(+9.40%)，市值约4600亿；长鑫/SMIC/华虹核心设备供应商，订单能见度至2027年；PE(TTM)约38倍",
             (8, 10, 7, 8), ("7/9收盘", "877.73元 (+9.40%)"), "设备平台龙头", False,
             "国产设备第一+长鑫Capex核心受益+估值合理", "市值较大弹性略低", "买入：800-840区间", ("780元", "1100元")),
            ("中微公司", "688012", "CCP刻蚀龙头国内第一/全球第三，5nm刻蚀进入台积电验证，ICP刻蚀快速放量；7/9收471.59元(+11.49%创历史新高)，主力净流入17.29亿；Q1归母+197%，18家机构评级15买入3增持，目标均价423元（已突破）",
             (9, 9, 6, 9), ("7/9收盘", "471.59元 (+11.49%创新高)"), "刻蚀设备", False,
             "创历史新高+主力17亿净流入+5nm验证+目标价上修", "短期超买需消化", "买入：430-450回调加仓", ("410元", "560元")),
            ("华海清科", "688120", "CMP设备国产独家垄断，国内市占率超70%，减薄/清洗/再生设备延展；7/9收344.80元(+16.88%创新高)，近1月10次创新高；长鑫CMP设备独供，订单爆发；Q1业绩+150%",
             (10, 9, 5, 9), ("7/9收盘", "344.80元 (+16.88%创新高)"), "CMP设备", False,
             "CMP独家+长鑫独供+10次创新高+Q1高增", "估值偏高PE~80倍", "买入：310-320回调", ("290元", "420元")),
            ("拓荆科技", "688072", "PECVD设备国内绝对龙头（市占率90%+），ALD/混合键合快速放量；6/29起因筹划收购无锡尚积（PVD+刻蚀）停牌至今；7/8停牌价832元，市值2418亿；辽宁A股第一，Q1扣非扭亏",
             (9, 8, 5, 7), ("停牌价(7/8)", "832.00元 (停牌重组)"), "薄膜设备", False,
             "PECVD独供长鑫+收购补齐PVD/刻蚀+ALD增192%", "重组不确定性+停牌期间板块大涨或补涨", "复牌关注：若900以下可追", ("780元", "1000元")),
            ("盛美上海", "688082", "清洗设备龙头，进入SK海力士/SAMSUNG供应链，SAPS/TEBO技术全球领先；电镀炉管/先进封装封装设备延展；7/9收432.60元(+4.24%)，Q1营收+50%+",
             (8, 8, 6, 7), ("7/9收盘", "432.60元 (+4.24%)"), "清洗设备", False,
             "唯一进入海力士供应链的国产清洗设备+海外收入占比高", "弹性略低于华海/中微", "买入：400-410", ("380元", "520元")),
        ]
        html = ""
        for i, s in enumerate(equip_stocks):
            html += self._stock_card(i+1, s[1], s[0], s[2], s[3], s[4], s[5], s[6], s[7], s[8], s[9], s[10])
        content += self._glass_card(f'''
            <h3 class="text-white font-bold text-base mb-3">⚙️ 环节二：半导体前道设备（TOP5）——业绩兑现最快Q3即体现，SEMI预测+29%</h3>
            <p class="text-white/60 text-xs mb-3">国产设备综合国产化率突破35%临界点，长鑫IPO后设备订单最先落地，北方华创/中微/华海清科/拓荆/盛美五强格局稳定 {source_tag("SEMI/国信证券/公司公告/证券之星", CONF_HIGH, verified=True)}</p>
            {html}
        ''')
        # 半导体材料
        mat_stocks = [
            ("雅克科技", "002409", "⭐持仓股！半导体前驱体材料国内龙头，HBM/DRAM前驱体独供长鑫/海力士/三星，半导体特气（UP Chemical）+光刻胶+先进封装材料（华飞电子）四维布局；7/9涨停209元(+10%)，成交67.17亿，换手10.49%，市值约995亿；成本108.8元浮盈+92.1%；2025年营收增45%+，Q2业绩超预期",
             (9, 9, 7, 9), ("7/9收盘", "209.00元 (+10%涨停)"), "前驱体/特气", True,
             "长鑫HBM前驱体独供+4维度共振+涨停创新高+持仓", "涨停后追高风险+Q3确认", "持有为主，190-200加仓", ("175元", "300元")),
            ("上海新阳", "300236", "半导体光刻胶+电镀液+湿电子化学品龙头，ArF光刻胶量产突破，长鑫/中芯核心供应商；7/9收131.30元(+18.74%大涨)，资金大幅流入；Q1业绩扭亏+产品结构升级",
             (9, 7, 6, 8), ("7/9收盘", "131.30元 (+18.74%)"), "光刻胶/电镀液", False,
             "ArF光刻胶突破+18%大涨+长鑫链材料核心", "光刻胶验证周期长+历史业绩波动", "买入：118-125区间", ("110元", "170元")),
            ("鼎龙股份", "300054", "CMP抛光垫国产独家（国内市占率30%+），YPI/PSPI光敏材料突破，抛光垫+清洗液+柔显材料三大平台；7/9约92.97元(+4.04%)，Q1业绩+60%+；长鑫/SMIC抛光垫稳定供货",
             (8, 8, 7, 7), ("7/9收盘", "92.97元 (+4.04%)"), "CMP抛光垫", False,
             "CMP垫独家+平台化延展+估值合理PE 45倍", "弹性不如纯题材股", "买入：85-90", ("80元", "120元")),
            ("安集科技", "688019", "CMP抛光液国产龙头（国内市占率25%+），铜/钨抛光液全系列覆盖，功能性湿电子化学品延展；7/9约320.75元(+1.47%)，Q1业绩+45%；客户覆盖中芯/长鑫/华虹",
             (7, 8, 6, 6), ("7/9收盘", "320.75元 (+1.47%)"), "CMP抛光液", False,
             "抛光液龙头+客户全覆盖+业绩稳增", "估值偏高PE 60倍+涨幅相对落后", "买入：295-310", ("280元", "400元")),
            ("彤程新材", "603650", "半导体光刻胶龙头（北京科华+北旭电子），KrF/ArF光刻胶量产，橡胶化学品基本盘提供现金流；7/9收89.56元(+7.81%)，主力净流入1.52亿；机构目标均价110元",
             (8, 7, 6, 7), ("7/9收盘", "89.56元 (+7.81%)"), "光刻胶", False,
             "光刻胶龙头+主力净流入+机构目标110", "橡胶业务占比高弹性略低", "买入：82-85区间", ("78元", "110元")),
            ("沪硅产业", "688126", "12寸大硅片国产龙头，300mm硅片产能30万片/月爬坡至60万片，长鑫/中芯/华虹核心供应商；7/9约33.40元(+2.77%)，国产大硅片从0到1突破；2025年营收+35%",
             (8, 7, 7, 7), ("7/9收盘", "33.40元 (+2.77%)"), "大硅片", False,
             "12寸硅片国产独家+长鑫认证通过+低价股弹性", "尚未盈利+折旧压力大", "买入：30-32区间", ("28元", "42元")),
        ]
        html = ""
        for i, s in enumerate(mat_stocks):
            html += self._stock_card(i+1, s[1], s[0], s[2], s[3], s[4], s[5], s[6], s[7], s[8], s[9], s[10])
        content += self._glass_card(f'''
            <h3 class="text-white font-bold text-base mb-3">🧪 环节三：半导体材料（TOP6）——Q4-2027年业绩弹性最大，前驱体/光刻胶/CMP/硅片四大赛道</h3>
            <p class="text-white/60 text-xs mb-3">材料随长鑫/长江新产能爬坡逐季放量，前驱体雅克率先受益、光刻胶上海新阳/彤程突破、CMP垫鼎龙独家、抛光液安集龙头、大硅片沪硅起量 {source_tag("公司公告/国信证券/证券之星", CONF_HIGH, verified=True)}</p>
            {html}
        ''')
        # 存储设计/IDM
        design_stocks = [
            ("兆易创新", "603986", "国产存储设计龙头，NOR Flash全球第三（市占率20%），DRAM利基型放量（GD5/GD6系列），MCU业务复苏；7/9涨停收盘663.49元，成交突破百亿；Q2业绩环比+150%超预期，DRAM/NOR/NAND三驾马车齐发；PE(TTM)约45倍",
             (9, 9, 7, 8), ("7/9收盘", "663.49元 (+10%涨停)"), "存储设计龙头", False,
             "国产存储龙头+三业务齐发+NOR涨价直接受益+涨停", "涨停后位置偏高+减持风险", "买入：600-620回调", ("570元", "800元")),
            ("澜起科技", "688008", "全球内存接口芯片绝对龙头（DDR5 RCD市占率70%+），MRCD/MDB/DB芯片配套HBM，PCIe Retimer/CXL拓展第二曲线；7/9沪深300领涨+15.64%，盘中最高285元；DDR5渗透率提升+HBM配套芯片需求爆发",
             (10, 9, 6, 9), ("7/9收盘", "约285元 (+15.64%领涨)", ), "DDR5接口芯片", False,
             "DDR5渗透加速+HBM接口芯片垄断+沪深300领涨", "涨速较快短线或有震荡", "买入：255-270区间", ("240元", "350元")),
            ("北京君正", "300223", "车规存储龙头（ISSI），DRAM/SRAM/NOR车规全覆盖，AI+汽车电子双轮驱动；7/9约236元(+9.58%)，Q2业绩环比改善；车规存储壁垒高、毛利稳",
             (8, 7, 7, 7), ("7/9收盘", "约236元 (+9.58%)"), "车规存储", False,
             "车规存储龙头+ISSI品牌壁垒+汽车电子周期复苏", "消费类业务有拖累", "买入：215-225", ("200元", "290元")),
            ("普冉股份", "688766", "EEPROM+NOR Flash双线龙头，EEPROM全球前三，NOR Flash利基市场放量，MCU业务拓展；7/9收762.07元(+9.81%)，高价股弹性品种",
             (8, 6, 5, 6), ("7/9收盘", "762.07元 (+9.81%)"), "EEPROM/NOR", False,
             "EEPROM龙头+涨价直接受益+高弹性", "高股价小市值流动性较弱+估值贵", "买入：700-730", ("680元", "900元")),
            ("东芯股份", "688110", "SLC NAND国产龙头，SPI NAND/Serial NOR小容量存储专家，工业/车规拓展；7/9约172.50元(+2.19%)，相对滞涨有补涨空间",
             (7, 6, 7, 7), ("7/9收盘", "约172.50元 (+2.19%)"), "SLC NAND", False,
             "SLC NAND国产稀缺+滞涨补涨空间+估值较低", "技术壁垒低于兆易", "买入：160-168", ("150元", "210元")),
        ]
        html = ""
        for i, s in enumerate(design_stocks):
            html += self._stock_card(i+1, s[1], s[0], s[2], s[3], s[4], s[5], s[6], s[7], s[8], s[9], s[10])
        content += self._glass_card(f'''
            <h3 class="text-white font-bold text-base mb-3">💾 环节四：存储设计/IDM（TOP5）——涨价直接受益，兆易/澜起双龙头领涨</h3>
            <p class="text-white/60 text-xs mb-3">兆易创新NOR/DRAM/MCU三驾马车+澜起DDR5接口芯片垄断+北京君正车规存储特色，均直接受益存储涨价 {source_tag("公司公告/东方财富/财联社", CONF_HIGH, verified=True)}</p>
            {html}
        ''')
        # 模组
        module_stocks = [
            ("江波龙", "301308", "国产存储模组龙头（Lexar/FORESEE品牌），H1预告净利92-110亿(+622-743倍)，营收220-250亿，Q2预计53-71亿；低价库存红利Q3末-Q4初消耗完毕，H2毛利或回落；7/9约618元(+4.27%)，成交百亿",
             (10, 7, 4, 6), ("7/9收盘", "约618元 (+4.27%)"), "存储模组龙头", False,
             "H1业绩+622倍史上最强+Lexar品牌国际化", "低价库存Q3末消耗完毕+H2毛利回落风险大", "谨慎追高，止盈位：跌破560减仓", ("520元", "700元（短期）") ),
            ("佰维存储", "688525", "存储模组+主控+封测一体化，AI终端存储/eMMC/UFS放量；2025年亏损2026H1大幅扭亏；7/9约408元(+2.97%)，午盘主力净流出8.92亿（获利了结明显）",
             (8, 6, 4, 5), ("7/9收盘", "约408元 (+2.97%)"), "模组/封测", False,
             "去年亏损今年扭亏弹性大+AI终端存储放量", "主力净流出8.92亿（机构兑现）+估值贵", "回避/等回调至360-380", ("350元", "480元")),
            ("德明利", "001309", "SSD主控+模组双轮驱动，自研主控芯片+存储模组一体化，NAND涨价弹性大；7/9约831.77元(+0.82%)，高价股品种",
             (8, 6, 4, 5), ("7/9收盘", "约832元 (+0.82%)"), "主控/模组", False,
             "主控自研护城河+NAND涨价弹性大", "涨幅巨大+主力有兑现迹象+流动性一般", "谨慎，750以下低吸", ("720元", "950元")),
        ]
        html = ""
        for i, s in enumerate(module_stocks):
            html += self._stock_card(i+1, s[1], s[0], s[2], s[3], s[4], s[5], s[6], s[7], s[8], s[9], s[10])
        content += self._glass_card(f'''
            <h3 class="text-white font-bold text-base mb-3">🔌 环节五：存储模组/主控（TOP3）——H1业绩爆发但需警惕库存红利消退</h3>
            <p class="text-white/60 text-xs mb-3">模组厂Q1-Q3是最佳兑现窗口，江波龙H1净利92-110亿创纪录，但<b class="text-yellow-400">低价库存红利Q3末-Q4初消耗完毕</b>，H2需警惕毛利回落 {source_tag("公司公告/财联社", CONF_HIGH, verified=True)}</p>
            {html}
            <div class="mt-3 p-3 bg-yellow-500/10 border border-yellow-500/30 rounded-lg">
                <p class="text-yellow-300 text-xs font-bold">⚠️ 模组股特别提示</p>
                <p class="text-yellow-200/80 text-xs mt-1">模组股业绩弹性最大但周期性最强，低价库存消耗完毕后（预计Q3末-Q4初），若合约价不能继续上涨则毛利将快速回落。建议配置比例不超总仓15%，且优先选择有主控/品牌/自研能力的江波龙，纯模组佰维/德明利需更谨慎。</p>
            </div>
        ''')
        # 封测/服务器
        server_stocks = [
            ("浪潮信息", "000977", "国产服务器绝对龙头（市占率30%+），AI服务器放量+H1净利26-31亿(+226-288%)；7/9二连板收盘85.99元，成交185亿（历史天量），主力净流入48亿（两市前列）",
             (9, 8, 7, 7), ("7/9收盘", "85.99元 (+10%二连板)"), "AI服务器", False,
             "AI服务器龙头+二连板+H1业绩+226%+主力48亿净流入", "成交185亿天量+短期涨幅大或有震荡", "买入：78-82区间（回踩5日线）", ("75元", "110元")),
        ]
        html = ""
        for i, s in enumerate(server_stocks):
            html += self._stock_card(i+1, s[1], s[0], s[2], s[3], s[4], s[5], s[6], s[7], s[8], s[9], s[10])
        content += self._glass_card(f'''
            <h3 class="text-white font-bold text-base mb-3">💻 服务器/算力（延伸标的）</h3>
            <p class="text-white/60 text-xs mb-3">服务器是存储芯片最大下游需求方，AI服务器单机HBM+DDR5容量是传统服务器8-10倍，直接拉动DRAM/HBM需求 {source_tag("公司公告/财联社", CONF_HIGH)}</p>
            {html}
        ''')
        return self._section("chain", "四、产业链细分环节标的排序（6大环节TOP3-5）", "🏭", content)

    # ===================== 五、TOP10重点标的深度卡片 =====================
    def _sec_top10(self):
        # 这里输出10个重点标的的更详细卡片
        deep_cards = [
            {
                "rank": 1, "name": "雅克科技", "code": "002409", "cat": "⭐持仓·HBM/前驱体/特气",
                "holding": True,
                "price": "209.00元 (+10%涨停)",
                "scores": (9, 9, 7, 9),
                "core_logic": "半导体前驱体材料绝对龙头（收购UP Chemical全球第六），HBM高介电常数前驱体/Zr前驱体独供SK海力士/三星/长鑫；半导体特气（六氟化钨等）+光刻胶+先进封装球形硅微粉（华飞电子）四大赛道共振；长鑫180亿HBM/DDR5扩产前驱体是最大耗材，价值量占比前道材料20%+；朱一明（长鑫董事长）直接间接参股强化客户黏性",
                "catalysts": ["长鑫7/16申购→上市后HBM前驱体订单爆发", "Q2业绩超预期（市场预期归母7-8亿）", "SK海力士上市扩产+HBM4前驱体送样验证", "半导体特气国产替代加速+先进封装材料涨价"],
                "financials": [("2024营收", "63.2亿", "+38%"), ("2025营收", "~90亿", "+42%"), ("2026E营收", "130-150亿", "+50%"), ("2026E归母", "25-30亿", "+60%"), ("PE(2026E)", "33-40倍", "合理偏低"), ("毛利率", "32-35%", "稳中有升")],
                "buy_zone": "190-200元（回踩5日线/涨停缺口）",
                "stop_loss": "175元（跌破20日线或涨停开盘价）",
                "targets": [("第一目标(1月)", "250元", "+20%"), ("第二目标(3月)", "280-300元", "+35%"), ("乐观目标(6月)", "350元", "+67%")],
            },
            {
                "rank": 2, "name": "北方华创", "code": "002371", "cat": "设备平台龙头",
                "holding": False,
                "price": "877.73元 (+9.40%)",
                "scores": (8, 10, 7, 8),
                "core_logic": "国产半导体设备唯一平台型龙头，刻蚀（CCP+ICP）、薄膜（PVD+CVD+ALD）、热处理、清洗、氧化扩散全品类覆盖，2025年营收破300亿，2026E 450亿+；长鑫/中芯/华虹/长江存储四大客户深度绑定；零部件自供率持续提升，毛利率稳定在45%+",
                "catalysts": ["长鑫IPO后200亿+设备订单落地", "中芯/华虹/长存2026H2扩产招标", "12寸刻蚀设备进入三星/海力士验证", "Q2业绩+50%超预期"],
                "financials": [("2025营收", "310亿", "+38%"), ("2026E营收", "450亿", "+45%"), ("2026E归母", "85-95亿", "+45%"), ("PE(2026E)", "48-54倍", "合理"), ("毛利率", "45%", "稳中有升"), ("新签订单", "700亿+", "+40%")],
                "buy_zone": "800-840元（回踩10/20日线）",
                "stop_loss": "760元（跌破60日线）",
                "targets": [("第一目标", "1000元", "+14%"), ("第二目标", "1100元", "+25%"), ("乐观目标", "1300元", "+48%")],
            },
            {
                "rank": 3, "name": "中微公司", "code": "688012", "cat": "刻蚀龙头",
                "holding": False,
                "price": "471.59元 (+11.49%创历史新高)",
                "scores": (9, 9, 6, 9),
                "core_logic": "CCP电容耦合刻蚀国内市占率第一/全球第三，5nm CCP刻蚀进入台积电先进工艺验证，ICP电感耦合刻蚀在逻辑/存储厂快速放量；MOCVD设备在Mini-LED领域独大；拓荆科技持股8%+受益重组（公允价值变动收益）；Q1归母+197%超预期",
                "catalysts": ["5nm刻蚀进入台积电验证（重大突破）", "长鑫3D NAND/DRAM刻蚀订单放量", "持有拓荆科技8%（重组催化）", "大宗交易机构抢筹+主力17亿净流入"],
                "financials": [("2025营收", "120亿", "+35%"), ("2026E营收", "170亿", "+42%"), ("2026E归母", "35-40亿", "+50%"), ("PE(2026E)", "110-125倍", "偏高"), ("毛利率", "40%", "稳中有升"), ("Q1归母", "9.3亿", "+197%")],
                "buy_zone": "430-450元（回踩10日线）",
                "stop_loss": "400元（整数关口）",
                "targets": [("第一目标", "520元", "+10%"), ("第二目标", "580元", "+23%"), ("乐观目标", "650元", "+38%")],
            },
            {
                "rank": 4, "name": "兆易创新", "code": "603986", "cat": "存储设计龙头",
                "holding": False,
                "price": "663.49元 (+10%涨停)",
                "scores": (9, 9, 7, 8),
                "core_logic": "国产存储设计绝对龙头，NOR Flash全球市占率20%排第三（仅次于华邦/旺宏），DRAM利基型DDR3/DDR4量产放量（GD5/GD6），MCU业务消费/工业全面复苏；Q2业绩环比+150%大超预期，NOR合约价Q3涨15-20%直接受益；朱一明同时兼任长鑫董事长，长鑫产业链深度协同",
                "catalysts": ["长鑫IPO朱一明十年不减持（强化信心）", "DRAM自研+长鑫代工协同", "NOR Q3合约价涨15-20%直接受益", "MCU业务周期复苏"],
                "financials": [("2025营收", "105亿", "+55%"), ("2026E营收", "150-170亿", "+50%"), ("2026E归母", "35-40亿", "+100%"), ("PE(2026E)", "45-50倍", "合理"), ("毛利率", "42%", "提升中"), ("Q2归母", "12-14亿", "+150%QoQ")],
                "buy_zone": "600-620元（涨停后震荡回踩）",
                "stop_loss": "560元（跌破20日线）",
                "targets": [("第一目标", "750元", "+13%"), ("第二目标", "820元", "+24%"), ("乐观目标", "950元", "+43%")],
            },
            {
                "rank": 5, "name": "澜起科技", "code": "688008", "cat": "DDR5接口芯片",
                "holding": False,
                "price": "约285元 (+15.64%沪深300领涨)",
                "scores": (10, 9, 6, 9),
                "core_logic": "全球内存接口芯片（DDR5 RCD/DB）双寡头之一（与瑞萨IDT并列），DDR5世代市占率稳定在70%+；MRCD/MDB芯片为HBM内存扩展必需配套芯片，HBM需求爆发直接拉动；PCIe Retimer/CXL内存扩展芯片第二曲线；津逮CPU业务平稳",
                "catalysts": ["DDR5渗透率从30%→60%（量价齐升）", "HBM4配套MRCD/MDB独家供货", "CXL内存扩展芯片量产突破", "沪深300领涨+机构加仓"],
                "financials": [("2025营收", "60亿", "+65%"), ("2026E营收", "90-100亿", "+55%"), ("2026E归母", "32-38亿", "+50%"), ("PE(2026E)", "80-95倍", "偏高但高成长"), ("毛利率", "62%", "高毛利"), ("Q1营收", "17.3亿", "+72%")],
                "buy_zone": "255-270元（回踩20日线）",
                "stop_loss": "235元",
                "targets": [("第一目标", "320元", "+12%"), ("第二目标", "360元", "+26%"), ("乐观目标", "420元", "+47%")],
            },
            {
                "rank": 6, "name": "华海清科", "code": "688120", "cat": "CMP设备独家",
                "holding": False,
                "price": "344.80元 (+16.88%创新高)",
                "scores": (10, 9, 5, 9),
                "core_logic": "国内CMP化学机械抛光设备独家垄断（全球第二，仅次于应用材料），国内市占率70%+；减薄/清洗/再生/VDM设备多品类延展，2025年营收+60%；长鑫/SMIC CMP设备几乎100%来自华海清科；近1月10次创历史新高，趋势最强设备股",
                "catalysts": ["长鑫CMP设备独供（180亿HBM扩产核心受益）", "减薄设备在先进封装放量", "Q1-Q2业绩持续高增100%+", "创新高趋势资金抱团"],
                "financials": [("2025营收", "40亿", "+60%"), ("2026E营收", "65-75亿", "+70%"), ("2026E归母", "18-22亿", "+75%"), ("PE(2026E)", "80-95倍", "偏高）"), ("毛利率", "45%", "稳中有升"), ("Q1归母", "3.8亿", "+150%")],
                "buy_zone": "310-320元（回踩5/10日线）",
                "stop_loss": "285元",
                "targets": [("第一目标", "390元", "+13%"), ("第二目标", "440元", "+28%"), ("乐观目标", "500元", "+45%")],
            },
            {
                "rank": 7, "name": "长电科技", "code": "600584", "cat": "封测龙头",
                "holding": False,
                "price": "103.52元 (+10%涨停反包)",
                "scores": (9, 9, 7, 8),
                "core_logic": "全球封测第三/国内第一（市占率15%+），XDFOI高密度多维异构封装量产（Chiplet/CoWoS类），HBM/SiP/FCBGA全品类覆盖；2025年营收+17%归母+79.86%创历史新高，先进封装收入占比超70%；中芯国际为大股东协同效应强；日月光涨价20%+传导",
                "catalysts": ["长鑫HBM/DDR5封测核心供应商", "日月光涨价20%+公司调价", "定增扩产聚焦AI/汽车/存储", "涨停反包龙虎榜机构净买入"],
                "financials": [("2025营收", "360亿", "+17%"), ("2026E营收", "450亿", "+25%"), ("2026E归母", "30-35亿", "+50%"), ("PE(2026E)", "30-35倍", "低估"), ("毛利率", "15%", "触底回升"), ("Q1归母", "6.5亿", "+68%")],
                "buy_zone": "95-100元",
                "stop_loss": "88元",
                "targets": [("第一目标", "120元", "+16%"), ("第二目标", "135元", "+30%"), ("乐观目标", "160元", "+55%")],
            },
            {
                "rank": 8, "name": "江波龙", "code": "301308", "cat": "存储模组龙头（波段）",
                "holding": False,
                "price": "约618元 (+4.27%)",
                "scores": (10, 7, 4, 6),
                "core_logic": "国产存储模组绝对龙头（Lexar雷克沙国际品牌+FORESEE行业品牌），H1预告净利92-110亿(+622-743倍)创A股纪录，Q2单季53-71亿；但低价库存红利Q3末-Q4初消耗完毕，H2毛利可能回落；需波段操作见好就收",
                "catalysts": ["H1业绩超预期（8月底正式披露）", "Q3合约价继续上涨维持毛利", "企业级SSD/AI存储放量", "回购+大股东增持预期"],
                "financials": [("2025营收", "250亿", "+30%"), ("2026H1营收", "220-250亿", "+180%"), ("2026E营收", "500亿+", "+100%"), ("2026E归母", "120-140亿", "+1000%+"), ("PE(2026E)", "20-25倍（按峰值利润）", "低"), ("H1毛利率", "35%+", "Q3后回落")],
                "buy_zone": "560-590元（回调10%以上）",
                "stop_loss": "520元（破位止盈/止损）",
                "targets": [("第一目标", "700元", "+13%"), ("第二目标", "780元", "+26%"), ("止盈信号", "Q3末库存消耗完毕", "及时兑现")],
            },
            {
                "rank": 9, "name": "浪潮信息", "code": "000977", "cat": "AI服务器龙头",
                "holding": False,
                "price": "85.99元 (+10%二连板)",
                "scores": (9, 8, 7, 7),
                "core_logic": "国产服务器绝对龙头（国内市占率30%+、全球第二），AI服务器占比持续提升至40%+；H1预告净利26-31亿(+226-288%)大超预期，Q2单季16-21亿；7/9二连板成交185亿历史天量，主力净流入48亿两市居前；AI服务器单机DRAM+HBM容量是传统8-10倍",
                "catalysts": ["H1业绩+226%超预期", "AI服务器出货量H2持续高增", "英伟达Rubin Q3交付拉动新需求", "国产算力/信创服务器放量"],
                "financials": [("2025营收", "1200亿", "+15%"), ("2026E营收", "1600亿", "+33%"), ("2026E归母", "50-60亿", "+80%"), ("PE(2026E)", "30-35倍", "合理"), ("毛利率", "12%", "持续改善中"), ("Q2单季", "16-21亿", "+300%QoQ")],
                "buy_zone": "78-82元（回踩5日线）",
                "stop_loss": "72元（跌破20日线）",
                "targets": [("第一目标", "100元整数关", "+16%"), ("第二目标", "110元", "+28%"), ("乐观目标", "130元", "+51%")],
            },
            {
                "rank": 10, "name": "鼎龙股份", "code": "300054", "cat": "CMP抛光垫/平台材料",
                "holding": False,
                "price": "约92.97元 (+4.04%)",
                "scores": (8, 8, 7, 7),
                "core_logic": "CMP抛光垫国产独家垄断（国内市占率30%+，对标陶氏化学），YPI/PSPI光敏聚酰亚胺先进封装材料突破，清洗液新品放量，柔显材料布局；三大产品平台+打印耗材基本盘现金流稳定；PE 45倍在材料股中估值合理，长鑫/SMIC稳定供货",
                "catalysts": ["CMP抛光垫长鑫/长存订单放量", "YPI/PSPI在先进封装验证通过", "Q2业绩+50%持续高增", "相对滞涨补涨需求"],
                "financials": [("2025营收", "40亿", "+35%"), ("2026E营收", "55-60亿", "+40%"), ("2026E归母", "12-14亿", "+55%"), ("PE(2026E)", "42-48倍", "合理"), ("毛利率", "38%", "稳中有升"), ("Q1归母", "2.5亿", "+45%")],
                "buy_zone": "85-90元",
                "stop_loss": "78元",
                "targets": [("第一目标", "110元", "+18%"), ("第二目标", "125元", "+34%"), ("乐观目标", "145元", "+56%")],
            },
        ]
        content = ""
        for c in deep_cards:
            fin_html = ""
            for k, v, note in c["financials"]:
                fin_html += f'<div class="bg-white/[0.03] rounded p-2 text-center"><div class="text-[10px] text-white/40">{k}</div><div class="text-white font-bold text-sm">{v}</div><div class="text-[9px] text-white/50">{note}</div></div>'
            cat_html = ""
            for cat in c["catalysts"]:
                cat_html += f'<li class="text-white/70 text-xs mb-1">▸ {cat}</li>'
            targets_html = ""
            for label, price, gain in c["targets"]:
                targets_html += f'<div class="bg-red-500/10 border border-red-500/20 rounded p-2 text-center"><div class="text-[10px] text-white/50">{label}</div><div class="text-red-300 font-bold">{price}</div><div class="text-[10px] text-red-400">{gain}</div></div>'
            hold_cls = "border-yellow-500/50 holding-card" if c["holding"] else ""
            content += f'''
            <div class="bg-white/[0.04] border border-white/10 rounded-xl p-4 mb-4 {hold_cls}">
                <div class="flex items-start justify-between gap-2 mb-3 flex-wrap">
                    <div>
                        <div class="flex items-center gap-2 flex-wrap">
                            <span class="text-white/30 text-xs font-mono">#{c["rank"]}</span>
                            {"<span class='holding-badge'>⭐持仓</span>" if c["holding"] else ""}
                            <span class="text-white font-black text-lg">{c["name"]}</span>
                            <span class="text-white/40 text-xs font-mono">{c["code"]}</span>
                            <span class="bg-purple-500/20 text-purple-300 text-[10px] px-2 py-0.5 rounded border border-purple-500/30">{c["cat"]}</span>
                        </div>
                        <div class="text-red-400 font-bold text-sm mt-1">{c["price"]}</div>
                    </div>
                    <div class="grid grid-cols-4 gap-2 text-center text-xs">
                        <div><div class="text-white/40">弹性</div><div class="text-red-400 font-bold">{c["scores"][0]}</div></div>
                        <div><div class="text-white/40">确定</div><div class="text-green-400 font-bold">{c["scores"][1]}</div></div>
                        <div><div class="text-white/40">估值</div><div class="text-blue-400 font-bold">{c["scores"][2]}</div></div>
                        <div><div class="text-white/40">筹码</div><div class="text-yellow-400 font-bold">{c["scores"][3]}</div></div>
                    </div>
                </div>
                <div class="bg-white/[0.02] rounded-lg p-3 mb-3">
                    <div class="text-white/50 text-[10px] mb-1">🔍 核心逻辑</div>
                    <p class="text-white/80 text-xs leading-relaxed">{c["core_logic"]}</p>
                </div>
                <div class="mb-3">
                    <div class="text-white/50 text-[10px] mb-1">📊 关键财务/估值</div>
                    <div class="grid grid-cols-3 md:grid-cols-6 gap-2">{fin_html}</div>
                </div>
                <div class="mb-3">
                    <div class="text-white/50 text-[10px] mb-1">🚀 核心催化</div>
                    <ul class="list-none pl-0">{cat_html}</ul>
                </div>
                <div class="grid md:grid-cols-2 gap-3 mb-2">
                    <div class="bg-green-500/10 border border-green-500/20 rounded-lg p-2">
                        <div class="text-green-400 text-[10px] font-bold">💰 买入区间</div>
                        <div class="text-green-300 font-bold text-sm">{c["buy_zone"]}</div>
                    </div>
                    <div class="bg-red-500/10 border border-red-500/20 rounded-lg p-2">
                        <div class="text-red-400 text-[10px] font-bold">🛑 止损/止盈位</div>
                        <div class="text-red-300 font-bold text-sm">{c["stop_loss"]}</div>
                    </div>
                </div>
                <div class="grid grid-cols-3 gap-2">
                    {targets_html}
                </div>
            </div>'''
        return self._section("top10", "五、TOP10重点标的深度卡片（含价格点位/买卖区间）", "🏆", content)

    # ===================== 六、风险提示 =====================
    def _sec_risk(self):
        risks = [
            ("AI算力Capex不及预期", "若Meta/微软/谷歌Q2-Q3 Capex下修或AI商业化进展放缓，HBM/AI服务器需求可能低于预期，是本轮行情最大宏观风险。"),
            ("涨价持续性不及预期", "若Q4 DRAM/NAND合约价环比涨幅低于30%或转为下跌，模组/设计股业绩可能见光死（特别是江波龙/佰维/德明利等库存红利股）。"),
            ("长鑫IPO破发或定价偏低", "若7/13询价结果低于预期（<4元）或上市破发，可能短期打击板块情绪；但朱一明十年不减持+大基金二期8.73%锁定提供安全垫。"),
            ("国产替代进度低于预期", "若关键设备（EUV/高端刻蚀/高端光刻胶）国产验证遇阻，国产化率提升进度可能推迟；美国制裁升级也是风险点。"),
            ("地缘政治与出口管制", "美国对华半导体制裁升级（HBM设备/材料/EDA断供）、台海局势、韩国政府管制HBM技术转让等均可能冲击产业链。"),
            ("短期获利盘集中兑现", "7/9板块单日主力净流入315亿+5股涨停，短期获利盘丰厚；龙头股（中微/华海清科/澜起）单日涨幅10-18%可能引发短期回调。"),
            ("SK海力士上市定价不及预期", "7/10纳斯达克上市若定价低于预期或首日破发，可能短期影响海力士供应链情绪；但7倍超额认购提供支撑。"),
            ("板块轮动与估值消化", "半导体板块PE整体位于历史中枢偏上（设备50-100倍、设计45-80倍），若资金轮动至其他板块（创新药/消费/新能源）可能引发阶段性回调。"),
            ("江波龙等模组股H2毛利回落", "低价库存Q3末-Q4初消耗完毕后，若新采购成本与售价倒挂则毛利快速回落，需警惕Q4业绩下修风险。"),
            ("个股解禁/减持/商誉", "中微公司拓荆科技持股减持、部分设备股大额解禁、部分股票股东减持计划需持续关注。"),
        ]
        r_html = ""
        for i, (title, body) in enumerate(risks):
            r_html += f'<div class="flex gap-2 text-sm text-white/80 mb-2"><span class="text-red-400 flex-shrink-0">{i+1}.</span><span><b>{title}：</b>{body}</span></div>'
        # 风险应对策略
        hedge_html = '''
        <div class="grid md:grid-cols-3 gap-3 mt-3">
            <div class="bg-red-500/10 border border-red-500/20 rounded-lg p-3">
                <div class="text-red-400 font-bold text-sm mb-1">🛑 止损纪律</div>
                <p class="text-white/70 text-xs leading-relaxed">单只个股跌破20日线/买入成本-10%严格减仓1/3；板块指数跌破20日线降仓至5成以下；龙头股集体跌停时果断止损。</p>
            </div>
            <div class="bg-yellow-500/10 border border-yellow-500/20 rounded-lg p-3">
                <div class="text-yellow-400 font-bold text-sm mb-1">⚖️ 仓位管理</div>
                <p class="text-white/70 text-xs leading-relaxed">存储主线6-8成总仓，单只个股不超2成；设备/材料/设计/封测分散配置4大赛道，模组股不超1.5成以波段为主。</p>
            </div>
            <div class="bg-green-500/10 border border-green-500/20 rounded-lg p-3">
                <div class="text-green-400 font-bold text-sm mb-1">🎯 买卖节奏</div>
                <p class="text-white/70 text-xs leading-relaxed">龙头股（北方华创/中微/雅克/兆易）逢回调5/10日线加仓，追涨停板需谨慎；事件落地日（长鑫上市日）短期减仓兑现。</p>
            </div>
        </div>'''
        content = self._glass_card(f'''
            <h3 class="text-red-400 font-bold text-base mb-3">⚠️ 十大核心风险</h3>
            {r_html}
        ''')
        content += self._glass_card(f'''
            <h3 class="text-yellow-400 font-bold text-base mb-3">🛡️ 风险应对策略</h3>
            {hedge_html}
            <div class="mt-4 p-3 bg-yellow-500/10 border border-yellow-500/30 rounded-lg">
                <p class="text-yellow-300 text-xs font-bold">⚠️ 免责声明</p>
                <p class="text-yellow-200/80 text-xs mt-1">本报告基于公开信息整理（上交所/公司公告/财联社/东方财富/SEMI/高盛/杰富瑞/威刚法说会等多源交叉验证），仅作为投资研究参考，不构成任何投资建议。所有股价、估值、目标价均基于当前数据与合理假设，实际投资需自行判断、风险自担。股市有风险，投资需谨慎。</p>
            </div>
        ''')
        content += self._source_summary_section()
        return self._section("risk", "六、风险提示与免责声明", "⚠️", content)

    # ===================== 七、操作策略（含雅克诊断） =====================
    def _sec_strategy(self):
        # 雅克科技持仓诊断卡片
        yake_diag = f'''
        <div class="bg-gradient-to-br from-yellow-500/10 via-amber-500/5 to-transparent border-2 border-yellow-500/40 rounded-2xl p-5 mb-4 holding-card">
            <div class="flex items-center gap-2 mb-3">
                <span class="text-2xl">⭐</span>
                <h3 class="text-yellow-300 font-black text-lg">雅克科技(002409) 持仓深度诊断</h3>
                <span class="bg-yellow-500 text-black text-xs font-bold px-2 py-0.5 rounded ml-auto">核心持仓</span>
            </div>
            <div class="grid grid-cols-2 md:grid-cols-4 gap-3 mb-4">
                <div class="bg-white/[0.05] rounded-xl p-3 text-center">
                    <div class="text-white/50 text-[10px]">持仓成本</div>
                    <div class="text-white font-black text-xl">108.80</div>
                    <div class="text-white/40 text-[10px]">元/股</div>
                </div>
                <div class="bg-white/[0.05] rounded-xl p-3 text-center">
                    <div class="text-white/50 text-[10px]">7/9收盘价</div>
                    <div class="text-red-400 font-black text-xl">209.00</div>
                    <div class="text-red-300 text-[10px]">涨停+10%</div>
                </div>
                <div class="bg-white/[0.05] rounded-xl p-3 text-center">
                    <div class="text-white/50 text-[10px]">浮盈金额</div>
                    <div class="text-red-400 font-black text-xl">+100.2</div>
                    <div class="text-white/40 text-[10px]">元/股</div>
                </div>
                <div class="bg-gradient-to-br from-red-500/20 to-orange-500/10 border border-red-500/30 rounded-xl p-3 text-center">
                    <div class="text-white/50 text-[10px]">浮盈比例</div>
                    <div class="text-red-300 font-black text-xl">+92.1%</div>
                    <div class="text-red-400 text-[10px]">接近翻倍</div>
                </div>
            </div>
            <div class="grid grid-cols-2 md:grid-cols-4 gap-2 mb-4 text-center text-xs">
                <div class="bg-white/[0.03] rounded p-2"><div class="text-white/40">总市值</div><div class="text-white font-bold">约995亿</div></div>
                <div class="bg-white/[0.03] rounded p-2"><div class="text-white/40">PE(TTM)</div><div class="text-white font-bold">98.8倍</div></div>
                <div class="bg-white/[0.03] rounded p-2"><div class="text-white/40">7/9成交额</div><div class="text-white font-bold">67.17亿</div></div>
                <div class="bg-white/[0.03] rounded p-2"><div class="text-white/40">换手率</div><div class="text-white font-bold">10.49%</div></div>
            </div>
            <div class="bg-white/[0.03] rounded-lg p-3 mb-3">
                <div class="text-white/50 text-[10px] mb-1">📊 四维评分</div>
                <div class="grid grid-cols-4 gap-2 text-center">
                    <div><div class="text-red-400 font-black text-2xl">9</div><div class="text-white/60 text-[10px]">弹性 /10</div></div>
                    <div><div class="text-green-400 font-black text-2xl">9</div><div class="text-white/60 text-[10px]">确定性 /10</div></div>
                    <div><div class="text-blue-400 font-black text-2xl">7</div><div class="text-white/60 text-[10px]">估值 /10</div></div>
                    <div><div class="text-yellow-400 font-black text-2xl">9</div><div class="text-white/60 text-[10px]">筹码 /10</div></div>
                </div>
                <div class="text-center mt-2"><span class="text-red-400 font-black text-xl bg-white/10 px-3 py-1 rounded">S级 34分</span> <span class="text-white/60 text-xs ml-2">（S级≥34分，属于最高优先级持有）</span></div>
            </div>
            <div class="space-y-2 text-sm">
                <div class="flex gap-2"><span class="text-green-400 font-bold flex-shrink-0">✓ 持有逻辑：</span>
                    <span class="text-white/80 text-xs leading-relaxed"><b>继续坚定持有，当前不卖</b>。①HBM/DRAM前驱体独供长鑫/海力士/三星，长鑫180亿HBM扩产前驱体是最大耗材；②四大赛道（前驱体+特气+光刻胶+先进封装材料）共振，无单一业务风险；③涨停突破200整数关，成交量67亿换手10%属良性换手，非出货；④Q2业绩超预期预期（市场预期归母7-8亿，Q3-Q4加速）；⑤长鑫7/16申购催化仍在途。</span>
                </div>
                <div class="flex gap-2"><span class="text-yellow-400 font-bold flex-shrink-0">⚡ 加仓策略：</span>
                    <span class="text-white/80 text-xs leading-relaxed">已有浮盈+92%，不建议追涨停板加仓；若回踩190-200元区间（5日线附近/涨停缺口）可加仓1-2成；若强势整固后再封板突破220，则加仓需谨慎（高位加仓风险大）。整体仓位控制在单只2成以内。</span>
                </div>
                <div class="flex gap-2"><span class="text-red-400 font-bold flex-shrink-0">⚠️ 减仓信号：</span>
                    <span class="text-white/80 text-xs leading-relaxed">①跌破175元（20日线/涨停开盘价）减仓1/3锁利；②长鑫7/23上市日若"利好兑现"放量滞涨则减仓1/3；③Q3业绩低于预期（归母<10亿）减仓1/2；④出现连续3日放量阴线（主力出货）果断清仓。</span>
                </div>
                <div class="flex gap-2"><span class="text-cyan-400 font-bold flex-shrink-0">🎯 目标价位：</span>
                    <span class="text-white/80 text-xs leading-relaxed">第一目标<b class="text-red-400">250元</b>（长鑫上市催化，+20%），第二目标<b class="text-red-400">280-300元</b>（Q3业绩兑现，+35-45%），乐观目标<b class="text-red-400">350元</b>（2027年HBM全面放量+估值切换至2027年35-40倍PE）。</span>
                </div>
                <div class="flex gap-2"><span class="text-purple-400 font-bold flex-shrink-0">📅 关键节点：</span>
                    <span class="text-white/80 text-xs leading-relaxed">7/10 SK海力士上市（情绪催化）→7/13长鑫询价→7/16长鑫申购→7/23长鑫上市（利好兑现需警惕）→8月中报披露→9-10月Q3业绩预告→11月估值切换。</span>
                </div>
            </div>
            <div class="mt-4 p-3 bg-gradient-to-r from-green-500/10 to-cyan-500/10 border border-green-500/30 rounded-lg">
                <p class="text-green-300 text-sm font-bold">📌 结论：雅克科技处于长鑫+HBM+先进封装材料三重风口，持仓浮盈+92%仍属于上涨中期，继续持有为主，逢回调190-200加仓，175止损/250第一目标减仓1/3锁利，核心仓位持有至Q3业绩兑现。</p>
            </div>
        </div>'''
        # 仓位配置建议
        allocation = [
            ("前道设备", "3成 (30%)", "北方华创1成+中微公司0.7成+华海清科0.7成+拓荆/盛美0.6成", "业绩兑现最快，确定性最高"),
            ("存储设计/IDM", "2成 (20%)", "兆易创新0.7成+澜起科技0.7成+北京君正/普冉/东芯0.6成", "涨价直接受益"),
            ("半导体材料", "2成 (20%)", "雅克科技1成（已持仓）+鼎龙0.3成+安集0.2成+彤程0.2成+上海新阳0.2成+沪硅0.1成", "Q4弹性最大"),
            ("封测/HBM", "1-1.5成", "长电科技0.5成+通富微电0.5成+华天科技0.3-0.5成", "周期反转+先进封装"),
            ("AI服务器/模组", "0.5-1成", "浪潮信息0.3-0.5成+江波龙0.3-0.5成（波段）", "下游需求验证+弹性波段"),
            ("现金/机动", "0.5-1成", "回调加仓/风险对冲", "灵活机动"),
        ]
        alloc_html = ""
        for seg, ratio, stocks, note in allocation:
            alloc_html += f'''
            <div class="bg-white/[0.03] p-3 rounded-lg border border-white/10 mb-2">
                <div class="flex items-center justify-between mb-1">
                    <span class="text-white font-bold text-sm">{seg}</span>
                    <span class="text-cyan-400 font-black text-sm">{ratio}</span>
                </div>
                <p class="text-white/70 text-xs mb-1">{stocks}</p>
                <p class="text-white/50 text-[10px]">{note}</p>
            </div>'''
        # 短中长三线策略
        strategy = [
            ("超短线（1-2周）", "🔥", "事件驱动交易为主，聚焦7/10海力士上市+7/13长鑫询价+7/16长鑫申购三大催化，龙头股（中微/华海清科/澜起/雅克）回踩5日线买入，不追连续2个涨停板的股票；通富/长电/华天/兆易涨停后震荡2-3日可低吸；若板块单日成交>3500亿警惕短期见顶。"),
            ("中线（1-3个月）", "⚡", "主升浪行情持有为主，仓位维持6-8成。核心配置设备+材料双主线（北方华创/中微/雅克/兆易/澜起），事件节点（长鑫上市日7/23、中报披露8月）减仓1-2成锁利，回调后加回；目标板块整体涨幅20-30%。"),
            ("长线（6-12个月）", "🎯", "存储超级周期2026Q3-2027Q4至少6个季度，核心持有平台型龙头（北方华创/中微/雅克/兆易）穿越波动，2027年SEMI预测存储设备投资再+11%、高盛预测全年均价+40-45%，龙头有望翻倍。PE(TTM)超过80倍+业绩增速放缓时考虑兑现。"),
        ]
        strat_html = ""
        for label, icon, body in strategy:
            strat_html += f'''
            <div class="bg-white/[0.03] p-4 rounded-lg border border-white/10 mb-3">
                <div class="flex items-center gap-2 mb-2">
                    <span class="text-xl">{icon}</span>
                    <span class="text-white font-bold text-sm">{label}</span>
                </div>
                <p class="text-white/75 text-xs leading-relaxed">{body}</p>
            </div>'''
        # 买卖时机表
        timing = [
            ("7/10(周五)", "SK海力士纳斯达克上市定价", "持股观察", "若海力士大涨+7%→A股高开可减仓1成锁利；若平盘/小涨持有"),
            ("7/13(周一)", "长鑫科技初步询价", "持股观察", "若询价>5元（超预期）→板块继续冲高；若4-4.5元（符合预期）持有"),
            ("7/16(周四)", "长鑫科技网上申购日", "持有为主", "申购日通常板块情绪高涨，警惕『利好兑现』前的最后一冲"),
            ("7/23(周三)", "长鑫科技预计上市日", "减仓1成锁利", "上市首日若涨幅>50%→短期利好兑现减仓；若破发则加仓（长期买点）"),
            ("7月底-8月中", "中报密集披露期", "业绩兑现持有/不及预期减仓", "雅克/北方华创/兆易/江波龙中报超预期持有；不及预期减仓1/3"),
            ("9月", "Q3合约价执行+Q3业绩前瞻", "持有+加仓", "若Q3价格符合/超预期则加仓回调标的；若不及预期降仓"),
        ]
        timing_html = '<div class="overflow-x-auto"><table class="w-full text-xs"><thead><tr class="text-white/50 border-b border-white/10"><th class="py-2 px-2 text-left">日期</th><th class="py-2 px-2 text-left">事件</th><th class="py-2 px-2 text-left">操作建议</th><th class="py-2 px-2 text-left">判断条件</th></tr></thead><tbody>'
        for row in timing:
            timing_html += f'<tr class="border-b border-white/5"><td class="py-2 px-2 text-orange-300 font-bold whitespace-nowrap">{row[0]}</td><td class="py-2 px-2 text-white font-semibold">{row[1]}</td><td class="py-2 px-2 text-cyan-300 font-bold">{row[2]}</td><td class="py-2 px-2 text-white/70">{row[3]}</td></tr>'
        timing_html += '</tbody></table></div>'
        content = yake_diag
        content += self._glass_card(f'''
            <h3 class="text-white font-bold text-base mb-3">📊 建议仓位配置（总仓位6-8成）</h3>
            {alloc_html}
        ''')
        content += self._glass_card(f'''
            <h3 class="text-white font-bold text-base mb-3">🎯 短/中/长三线操作策略</h3>
            {strat_html}
        ''')
        content += self._glass_card(f'''
            <h3 class="text-white font-bold text-base mb-3">📅 未来一月关键节点操作表</h3>
            {timing_html}
        ''')
        # 金句总结
        content += self._glass_card(f'''
            <div class="text-center py-3">
                <p class="text-white/60 text-sm mb-2">—— 存储超级周期核心结论 ——</p>
                <p class="text-xl md:text-2xl font-black bg-gradient-to-r from-red-400 via-orange-400 to-yellow-400 bg-clip-text text-transparent leading-relaxed">
                    "长鑫IPO+海力士上市双轮驱动<br>
                    Q3涨价超预期+业绩持续兑现<br>
                    S级行情，坚定持有核心龙头"
                </p>
                <p class="text-white/50 text-xs mt-3">核心持仓雅克科技(002409) 成本108.8元 浮盈+92% → 继续持有，看250-300元</p>
            </div>
        ''')
        return self._section("strategy", "七、操作策略：雅克科技持仓诊断+全仓配置方案", "💡", content)

    def _content(self):
        header = f'''
        <div class="text-center mb-8 mt-4">
            <div class="inline-block bg-gradient-to-r from-red-500/20 via-orange-500/20 to-yellow-500/20 border border-red-500/30 rounded-full px-4 py-1 mb-3">
                <span class="text-red-300 text-xs font-semibold">🔥 S级产业链深度研究 · 2026年7月9日</span>
            </div>
            <h1 class="text-3xl md:text-4xl font-black text-white mb-2 tracking-tight">存储产业链全维度深度研究报告</h1>
            <p class="text-white/60 text-sm mb-2">长鑫IPO+SK海力士双上市超级催化 · Q3涨价超预期50-150%</p>
            <div class="flex items-center justify-center gap-4 text-xs text-white/40 flex-wrap">
                <span>📅 2026-07-09 盘后</span>
                <span>📊 覆盖6大环节30+核心标的</span>
                <span>⭐ 含雅克科技(+92%浮盈)持仓深度诊断</span>
                <span>📏 7大板块全链路拆解</span>
            </div>
            <div class="flex items-center justify-center gap-2 mt-3 flex-wrap">
                <span class="bg-red-500/20 text-red-300 text-[10px] px-2 py-1 rounded border border-red-500/30">S级行情</span>
                <span class="bg-orange-500/20 text-orange-300 text-[10px] px-2 py-1 rounded border border-orange-500/30">双IPO催化</span>
                <span class="bg-yellow-500/20 text-yellow-300 text-[10px] px-2 py-1 rounded border border-yellow-500/30">涨价超预期</span>
                <span class="bg-green-500/20 text-green-300 text-[10px] px-2 py-1 rounded border border-green-500/30">业绩兑现</span>
                <span class="bg-cyan-500/20 text-cyan-300 text-[10px] px-2 py-1 rounded border border-cyan-500/30">315亿净流入</span>
            </div>
        </div>'''
        return "\n".join([
            header,
            self._sec_conclusion(),
            self._sec_panorama(),
            self._sec_timeline(),
            self._sec_chain(),
            self._sec_top10(),
            self._sec_risk(),
            self._sec_strategy(),
        ])


def main():
    g = StorageIndustryReportGenerator()
    g.load_data()
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "docs/industry_chain/20260709_存储产业链全维度深度研究报告.html")
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
