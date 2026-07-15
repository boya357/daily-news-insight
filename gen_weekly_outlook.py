#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import os
sys.path.insert(0, '/root/daily-news-insight/v3')
from generators.weekly_outlook_pro import WeeklyOutlookProGenerator

gen = WeeklyOutlookProGenerator(date_str="2026-07-15")

# ============ 周中核心观察 ============
gen.add_midweek_summary("""
本周三（7月15日）市场迎来多重重磅信号集中落地：<strong>二季度GDP+6月经济数据</strong>公布、<strong>主板中报预告强制收官</strong>（超600家企业爆雷）、<strong>美国6月CPI超预期回落</strong>（核心CPI年率2.6%，6年来首次环比负增长）、<strong>长鑫科技IPO发行价敲定</strong>（8.66元/股，对应市值约5792亿）。
<br><br>
盘面呈现典型<strong>「冰火两重天」</strong>格局：半导体存储链受长鑫IPO定价低于预期冲击出现大幅调整（德明利一字跌停、先进封装指数大跌7.59%），而创新药、AI算力、高股息防御板块逆势走强。
<br><br>
<strong>核心定调</strong>：7月中下旬将进入「业绩真空+政策催化+事件密集」三重叠加的黄金窗口期，中报雷潮出清后，资金将加速向有真实业绩支撑的科技成长主线集中，结构远重于指数。
""")

# ============ 周中市场概览 ============
gen.add_market_status([
    {'name': '上证指数', 'value': '3,985', 'change': '-0.29%', 'up': False},
    {'name': '创业板指', 'value': '2,456', 'change': '-1.21%', 'up': False},
    {'name': '科创50', 'value': '1,128', 'change': '-4.25%', 'up': False},
    {'name': '两市成交', 'value': '2.59万亿', 'change': '缩量', 'up': False},
])

# ============ 重点关注题材 ============
gen.add_focus_topics([
    {
        'name': '存储芯片/HBM',
        'logic': '长鑫科技7/16申购（295亿募资，科创板第二大IPO），短期资金分流但中长期带动国产存储估值重估；SK海力士美股上市走强+全球存储超级周期延续；江波龙等中报业绩暴增验证景气度。本周半导体大跌属于「长鑫定价低于预期+高位获利兑现」的短期冲击，不改产业上行趋势。',
        'attention': '重点关注',
        'stocks': ['江波龙', '德明利', '兆易创新', '铜冠铜箔', '雅克科技']
    },
    {
        'name': 'AI算力/液冷散热',
        'logic': 'WAIC 7/17开幕，300+款AI新品全球首发，华为Atlas 950超节点真机亮相；推理token量6月环比增70%、同比20倍；液冷板块持续性评级A级。算力需求曲线继续变陡，产业链从「讲故事」进入「兑业绩」阶段。',
        'attention': '重点关注',
        'stocks': ['英维克', '浪潮信息', '中际旭创', '寒武纪', '海光信息']
    },
    {
        'name': '人形机器人/具身智能',
        'logic': 'WAIC展出多款人形机器人及AI灵巧手，具身智能赛道独立成馆；机器人+创新发展大会刚闭幕；2026年人形机器人整机产量有望突破10万台。从「会走路」到「能干活」，产业落地加速。',
        'attention': '重点关注',
        'stocks': ['拓普集团', '三花智控', '绿的谐波', '鸣志电器']
    },
    {
        'name': '创新药/医药',
        'logic': '《国家基本药物目录(2026年版)》发布+BD出海爆发（上半年出海金额997亿美元，约为2024年全年2倍）+中报业绩预增三重催化；迪哲医药20CM两连板、哈药股份4连板。政策+出海+业绩三共振，板块持续性强于纯题材。',
        'attention': '持续跟踪',
        'stocks': ['迪哲医药', '昭衍新药', '恒瑞医药', '药明康德']
    },
    {
        'name': '半导体设备/材料',
        'logic': '长鑫IPO扩产直接拉动上游设备与材料需求；国产替代政策持续加码；中报预增确定性高。先进封装短期调整较多，但HBM驱动的CoWoS需求长期逻辑不变。',
        'attention': '持续跟踪',
        'stocks': ['拓荆科技', '中微公司', '雅克科技', '华海诚科']
    },
    {
        'name': '稀有金属/稀土',
        'logic': '工信部联合自然资源部发布《稀有金属产业高质量发展三年行动补充方案》，设立800亿国家级稀有金属新材料产业基金，完善战略收储机制。政策从资源端到制造端形成完整红利链条。',
        'attention': '事件驱动',
        'stocks': ['北方稀土', '中国稀土', '厦门钨业']
    },
    {
        'name': '商业航天/卫星',
        'logic': '工信部同步发布商业航天上下游配套材料扶持政策，开放低轨卫星轨道资源，航天特种材料企业获研发补贴。与稀有金属政策形成联动，打通上下游产业链。',
        'attention': '事件驱动',
        'stocks': ['中国卫星', '航天电子', '铖昌科技']
    },
])

# ============ 操作要点 ============
gen.add_strategy_points([
    {
        'title': '仓位管理',
        'content': '建议总仓位5-6成。中报雷潮刚出清，短期情绪修复但上方仍有长鑫IPO分流、美联储7月底会议等不确定性，保持灵活仓位，进退自如。'
    },
    {
        'title': '板块配置',
        'content': '核心配置（60%）：AI算力+存储芯片；弹性配置（25%）：人形机器人+创新药；防御配置（15%）：稀有金属/高股息。科技成长仍是主战场。'
    },
    {
        'title': '操作节奏',
        'content': 'WAIC前（7/16-7/17）可适度布局算力与机器人；会议期间（7/18-7/20）分批兑现止盈；7/20 LPR前后观察政策信号；7/23起美股大厂财报季需警惕利好出尽。'
    },
    {
        'title': '风险纪律',
        'content': '单票止损严格执行8%；高位股不追涨，回踩支撑再低吸；中报无业绩支撑的纯题材小票坚决规避；长鑫申购日（7/16）注意资金分流冲击。'
    },
])

# ============ 下半周+下周操作策略 ============
gen.add_second_half_strategy("""
<strong>📅 时间轴：7/16(周四)→7/25(周六)</strong>
<br><br>
<strong>第一阶段（7/16-7/17）：事件密集窗口，高波动高机会</strong><br>
• 7/16周四：长鑫科技全网申购（短期资金分流，但落地后利空出尽）；首批中报披露（优彩资源、沃华医药）；亚太智能装备博览会开幕<br>
• 7/17周五：WAIC世界人工智能大会开幕，全月最强AI催化；股指期货/期权月度交割日（日内波动放大）；成品油调价窗口；第七届世界光子大会开幕<br>
• <strong>策略</strong>：周四早盘若因长鑫申购出现回调，是低吸算力、存储核心标的的机会；周五WAIC开幕后注意「买预期卖事实」，算力股冲高可分批减仓
<br><br>
<strong>第二阶段（7/20-7/22）：LPR+政策窗口，观察信号</strong><br>
• 7/20周一：LPR月度报价（市场预期7月LPR维持不变的概率较高，但若超预期下调则利好地产链和成长股）；APEC数字与人工智能部长会议持续<br>
• 7/21-22：中报正式披露进入加速期；工信部产业政策持续落地<br>
• <strong>策略</strong>：LPR若持平则符合预期，市场情绪由政策预期转向业绩驱动；若超预期下调则券商、地产链有脉冲机会
<br><br>
<strong>第三阶段（7/23-7/25）：美股财报季开启，外部扰动增加</strong><br>
• 7/23起：谷歌、Meta等美股AI大厂财报季开锣，关注资本开支指引与AI业务进展<br>
• 7/29-30美联储议息会议前的最后观察窗口（6月CPI已大幅低于预期，加息概率从42%降至8%）<br>
• <strong>策略</strong>：美股财报若超预期则A股算力链跟涨，若不及预期则需防范外围传导；月底前保持适度谨慎，不追高
<br><br>
<strong>🎯 核心策略一句话：雷潮出清后拥抱科技主线，WAIC前布局、会后兑现，月底前落袋为安。</strong>
""")

# ============ 持仓股专项分析 ============
holdings_html = """
<div class="space-y-3">
    <div class="bg-gradient-to-r from-blue-500/20 to-cyan-500/20 border border-blue-500/30 rounded-xl p-4">
        <div class="flex items-center justify-between mb-2">
            <span class="text-white font-bold">❄️ 英维克（液冷散热龙头）</span>
            <span class="text-yellow-400 text-sm">持有中</span>
        </div>
        <div class="text-white/80 text-sm leading-relaxed">
            <strong>催化因素：</strong>WAIC大会液冷散热为重点展出方向+AI算力需求持续爆发+中报业绩预增确定性高<br>
            <strong>技术面：</strong>液冷板块持续性评级A级（2-4周），英维克作为龙头受益最直接<br>
            <strong>操作建议：</strong>WAIC前（7/16-7/17）若冲高至78-80元区间减仓1/3锁定利润；回踩72-73元支撑位加仓；移动止盈上移至70元；底仓继续持有看产业趋势
        </div>
    </div>
    
    <div class="bg-gradient-to-r from-amber-500/20 to-orange-500/20 border border-amber-500/30 rounded-xl p-4">
        <div class="flex items-center justify-between mb-2">
            <span class="text-white font-bold">🟡 铜冠铜箔（锂电+PCB铜箔）</span>
            <span class="text-green-400 text-sm">持有中</span>
        </div>
        <div class="text-white/80 text-sm leading-relaxed">
            <strong>催化因素：</strong>存储/PCB铜箔需求回暖+稀有金属政策利好铜产业链+中报预增弹性大<br>
            <strong>技术面：</strong>前期涨幅较大，需警惕高位回调，但中长期产业逻辑不变<br>
            <strong>操作建议：</strong>170元上方减仓1/3锁定利润；移动止盈上移至160元；回踩155-160元区间可接回；底仓长线持有
        </div>
    </div>
    
    <div class="bg-gradient-to-r from-purple-500/20 to-pink-500/20 border border-purple-500/30 rounded-xl p-4">
        <div class="flex items-center justify-between mb-2">
            <span class="text-white font-bold">🔬 雅克科技（半导体材料/HBM前驱体）</span>
            <span class="text-green-400 text-sm">持有中</span>
        </div>
        <div class="text-white/80 text-sm leading-relaxed">
            <strong>催化因素：</strong>HBM需求爆发驱动前驱体量价齐升+长鑫扩产拉动国产替代+存储超级周期+中报预增<br>
            <strong>技术面：</strong>近期随半导体板块回调，中期上升趋势未破<br>
            <strong>操作建议：</strong>回踩215-220元区间加仓；冲高250元以上可T出加仓部分；底仓坚定持有，HBM产业链是全年最确定主线之一
        </div>
    </div>
    
    <div class="bg-gradient-to-r from-red-500/20 to-rose-500/20 border border-red-500/30 rounded-xl p-4">
        <div class="flex items-center justify-between mb-2">
            <span class="text-white font-bold">⚠️ *ST建艺</span>
            <span class="text-red-400 text-sm">高风险</span>
        </div>
        <div class="text-white/80 text-sm leading-relaxed">
            <strong>风险提示：</strong>7/6起ST涨跌幅扩至10%，波动率翻倍；中报季ST股是雷区集中地带<br>
            <strong>操作建议：</strong>任何反抽都是减仓机会，建议7月内完成清仓（最迟7月底前）；不补仓、不抄底、不抱幻想
        </div>
    </div>
</div>
"""
gen.add_section("持仓股下周操作指引", holdings_html, "💼")

# ============ 下周大事日历 ============
calendar_html = """
<div class="overflow-x-auto">
    <table class="w-full text-sm text-left">
        <thead class="text-xs text-white/60 uppercase border-b border-white/10">
            <tr>
                <th class="py-3 px-2">日期</th>
                <th class="py-3 px-2">事件</th>
                <th class="py-3 px-2">影响板块</th>
                <th class="py-3 px-2">重要性</th>
            </tr>
        </thead>
        <tbody class="text-white/80">
            <tr class="border-b border-white/5">
                <td class="py-3 px-2 font-semibold">7/20 周一</td>
                <td class="py-3 px-2">LPR月度报价（1年期3.0%/5年期3.5%）</td>
                <td class="py-3 px-2">地产、银行、全市场</td>
                <td class="py-3 px-2"><span class="text-yellow-400">⭐⭐⭐</span></td>
            </tr>
            <tr class="border-b border-white/5">
                <td class="py-3 px-2 font-semibold">7/20 周一</td>
                <td class="py-3 px-2">WAIC世界人工智能大会持续（至7/20）</td>
                <td class="py-3 px-2">AI算力、机器人、大模型</td>
                <td class="py-3 px-2"><span class="text-red-400">⭐⭐⭐⭐⭐</span></td>
            </tr>
            <tr class="border-b border-white/5">
                <td class="py-3 px-2 font-semibold">7/21 周二</td>
                <td class="py-3 px-2">APEC数字与人工智能部长会议持续（至7/24）</td>
                <td class="py-3 px-2">数字经济、国产AI芯片</td>
                <td class="py-3 px-2"><span class="text-yellow-400">⭐⭐⭐</span></td>
            </tr>
            <tr class="border-b border-white/5">
                <td class="py-3 px-2 font-semibold">7/22 周三</td>
                <td class="py-3 px-2">中报正式披露加速期</td>
                <td class="py-3 px-2">全市场（业绩线）</td>
                <td class="py-3 px-2"><span class="text-orange-400">⭐⭐⭐⭐</span></td>
            </tr>
            <tr class="border-b border-white/5">
                <td class="py-3 px-2 font-semibold">7/23 周四</td>
                <td class="py-3 px-2">美股AI大厂财报季开启（谷歌打头）</td>
                <td class="py-3 px-2">AI算力、光模块、芯片</td>
                <td class="py-3 px-2"><span class="text-red-400">⭐⭐⭐⭐⭐</span></td>
            </tr>
            <tr class="border-b border-white/5">
                <td class="py-3 px-2 font-semibold">7/24 周五</td>
                <td class="py-3 px-2">欧美PMI初值、美国新屋销售</td>
                <td class="py-3 px-2">周期、全球市场情绪</td>
                <td class="py-3 px-2"><span class="text-yellow-400">⭐⭐⭐</span></td>
            </tr>
            <tr>
                <td class="py-3 px-2 font-semibold">7/25 周六</td>
                <td class="py-3 px-2">美联储7/29-30会议前缄默期开始</td>
                <td class="py-3 px-2">美债、北向资金</td>
                <td class="py-3 px-2"><span class="text-orange-400">⭐⭐⭐⭐</span></td>
            </tr>
        </tbody>
    </table>
</div>
"""
gen.add_section("下周（7/20-7/25）关键日历", calendar_html, "📅")

# ============ 风险提示 ============
gen.add_risk_warning([
    "长鑫科技IPO申购日（7/16）资金分流冲击，尤其是高位科技股可能承压",
    "美股AI大厂财报季（7/23起）：预期已打满，若资本开支指引不及预期可能引发回调",
    "WAIC大会期间买预期卖事实效应，AI算力股可能出现会议期间冲高回落",
    "美联储7/29-30议息会议前的不确定性，虽然6月CPI大幅低于预期但通胀粘性仍存",
    "中报正式披露期（7月下旬-8月底）：创业板/科创板无强制预告，存在8月底暴雷风险",
])

# ============ 生成并保存 ============
output_path = "/root/daily-news-insight/docs/weekly_outlook/20260715_周三前瞻.html"
result = gen.save(output_path)
size = os.path.getsize(output_path)
print(f"生成成功：{result}")
print(f"文件大小：{size} bytes")
