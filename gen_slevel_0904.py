#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-09-04 盘前S级催化扫描 - GPT-6+英伟达HF收购+沃勒鸽派"""
import sys, os
sys.path.insert(0, 'v3')
os.chdir('/root/daily-news-insight')

from v3.generators.s_level_catalyst import SLevelCatalystGenerator
from components.layout import Section

gen = SLevelCatalystGenerator(
    date_str="20260904",
    catalyst_title="GPT-6 AGI时代开启+英伟达129亿美元收购Hugging Face+沃勒鸽派美股大涨",
    subtitle="2026.09.04 · 盘前S级催化 · 双S级AI产业核弹"
)

# ============ 1. 催化总览 ============
gen.add_catalyst_overview(
    overview="""
    <div style="font-size:14px;line-height:2;">
        <strong style="color:#fbbf24;font-size:16px;">【双S级AI产业核弹落地】</strong><br>
        ① <strong style="color:#60a5fa;">OpenAI发布GPT-6 Astra</strong>，宣告"欢迎来到AGI时代"！ARC-AGI-3得分99.9%（GPT-5.6仅7.8%），ExploitBench漏洞利用100%，越界率0%，具备直接操作电脑完成跨软件工作流能力，定价每百万输入$10/输出$50；<br>
        ② <strong style="color:#34d399;">英伟达129.3亿美元收购Hugging Face</strong>，史上最大单笔收购，掌控300万模型/1800万开发者开源AI生态入口，黄仁勋承诺平台开放不强制英伟达硬件；<br>
        ③ <strong style="color:#a78bfa;">美联储沃勒鸽派表态</strong>，9月加息概率从63%降至50%，美股三大指数全线大涨（道指+1.18%、纳指+1.40%、标普+1.06%）创近1月最大涨幅，10Y美债收益率降至4.74%；<br>
        ④ <strong style="color:#fb923c;">英伟达RTX Spark（N1X芯片）10月上市</strong>，支持128GB统一内存，端侧AI推理能力达千万亿次浮点运算；<br>
        ⑤ <strong style="color:#f87171;">风险面：博通Q4指引不及预期收跌2.74%</strong>，Ciena跌10.36%，光通信高预期标的承压；SK海力士跌0.79%，存储板块盘初杀跌后修复。
    </div>
    """,
    importance="极高"
)

# ============ 2. 隔夜外盘扫描 ============
overnight_html = """
<div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;">
    <div style="background:linear-gradient(135deg,rgba(16,185,129,0.12) 0%,rgba(5,150,105,0.08) 100%);border-radius:14px;padding:18px;border:1px solid rgba(16,185,129,0.25);">
        <div style="display:flex;align-items:center;margin-bottom:12px;">
            <div style="width:36px;height:36px;background:linear-gradient(135deg,#10b981 0%,#059669 100%);border-radius:10px;display:flex;align-items:center;justify-content:center;margin-right:12px;">🇺🇸</div>
            <span style="font-size:16px;font-weight:700;color:#34d399;">美股三大指数全线大涨</span>
        </div>
        <div style="font-size:13px;color:#d1fae5;line-height:2;">
            道琼斯：53686.11 <span style="color:#34d399;font-weight:700;">+1.18%</span><br>
            标普500：7747.71 <span style="color:#34d399;font-weight:700;">+1.06%</span>（近1月最大涨幅）<br>
            纳斯达克：26584.06 <span style="color:#34d399;font-weight:700;">+1.40%</span><br>
            费城半导体：盘初跌2%后V转修复<br>
            纳斯达克中国金龙指数：<span style="color:#f87171;">-0.81%</span>（中概小幅承压）
        </div>
    </div>
    <div style="background:linear-gradient(135deg,rgba(59,130,246,0.12) 0%,rgba(37,99,235,0.08) 100%);border-radius:14px;padding:18px;border:1px solid rgba(96,165,250,0.25);">
        <div style="display:flex;align-items:center;margin-bottom:12px;">
            <div style="width:36px;height:36px;background:linear-gradient(135deg,#3b82f6 0%,#1d4ed8 100%);border-radius:10px;display:flex;align-items:center;justify-content:center;margin-right:12px;">🔧</div>
            <span style="font-size:16px;font-weight:700;color:#60a5fa;">核心科技股表现</span>
        </div>
        <div style="font-size:13px;color:#bfdbfe;line-height:2;">
            英伟达NVDA：<span style="color:#34d399;font-weight:700;">+1.80%</span>（129亿收购HF+N1X双催化）<br>
            微软MSFT：<span style="color:#34d399;font-weight:700;">+2.68%</span>  Meta：<span style="color:#34d399;font-weight:700;">+3.01%</span><br>
            特斯拉TSLA：<span style="color:#34d399;font-weight:700;">+5.42%</span>（Cybercab发布）<br>
            博通AVGO：<span style="color:#f87171;font-weight:700;">-2.74%</span>（Q4指引不及高预期）<br>
            SK海力士：<span style="color:#f87171;">-0.79%</span>  美光MU：<span style="color:#f87171;">-2.43%</span>（盘中）<br>
            台积电TSM：<span style="color:#34d399;">+0.36%</span>  阿斯麦ASML：<span style="color:#f87171;">-2.15%</span><br>
            AMD：<span style="color:#f87171;">-1.30%</span>（盘中一度跌2.45%后修复）<br>
            Snowflake：<span style="color:#34d399;font-weight:700;">+16.55%</span>（AI云数据业绩超预期）
        </div>
    </div>
    <div style="background:linear-gradient(135deg,rgba(245,158,11,0.12) 0%,rgba(217,119,6,0.08) 100%);border-radius:14px;padding:18px;border:1px solid rgba(251,191,36,0.25);">
        <div style="display:flex;align-items:center;margin-bottom:12px;">
            <div style="width:36px;height:36px;background:linear-gradient(135deg,#f59e0b 0%,#d97706 100%);border-radius:10px;display:flex;align-items:center;justify-content:center;margin-right:12px;">🏦</div>
            <span style="font-size:16px;font-weight:700;color:#fbbf24;">美联储+宏观流动性</span>
        </div>
        <div style="font-size:13px;color:#fde68a;line-height:2;">
            沃勒表态：通胀显示降温迹象，倾向维持利率不变<br>
            9月加息概率：63%→<span style="color:#34d399;font-weight:700;">50%</span>（CME FedWatch）<br>
            10Y美债收益率：<span style="color:#34d399;">-5bp至4.74%</span><br>
            2Y美债收益率：-7bp至4.307%<br>
            美元指数：99.60，-0.08%，延续弱势<br>
            周五（今晚）：美国8月非农数据（预期+5.5万人）<br>
            下周关键：8月CPI数据（决定9月议息走向）
        </div>
    </div>
    <div style="background:linear-gradient(135deg,rgba(168,85,247,0.12) 0%,rgba(126,34,206,0.08) 100%);border-radius:14px;padding:18px;border:1px solid rgba(168,85,247,0.25);">
        <div style="display:flex;align-items:center;margin-bottom:12px;">
            <div style="width:36px;height:36px;background:linear-gradient(135deg,#a855f7 0%,#7e22ce 100%);border-radius:10px;display:flex;align-items:center;justify-content:center;margin-right:12px;">🥇</div>
            <span style="font-size:16px;font-weight:700;color:#c084fc;">大宗商品+避险资产</span>
        </div>
        <div style="font-size:13px;color:#e9d5ff;line-height:2;">
            现货黄金：<span style="color:#34d399;font-weight:700;">+2.07%报4472.28美元/盎司</span>（逼近4500）<br>
            现货白银：<span style="color:#34d399;font-weight:700;">+2.56%报66.98美元/盎司</span><br>
            WTI原油：+0.32%报91.30美元/桶<br>
            布伦特原油：-0.12%报95.52美元/桶<br>
            比特币：<span style="color:#34d399;font-weight:700;">突破81000美元</span>（5月以来新高）<br>
            花旗预测Q4布油回落至70美元/桶（霍尔木兹重开预期）<br>
            荷兰央行转移86吨黄金至英国（地缘避险）
        </div>
    </div>
</div>
"""
gen._components.append(Section(title="🌍 隔夜全球扫描（22:00-08:00）", content=overnight_html, icon="globe"))

# ============ 3. 催化事件详解 ============
gen.add_catalyst_details(
    background="""
    <strong style="color:#60a5fa;">【GPT-6 Astra - AGI宣言级产品】</strong><br>
    北京时间9月4日凌晨OpenAI正式发布GPT-6 Astra，旗舰级模型跨越。核心突破：<br>
    • ARC-AGI-3抽象推理从GPT-5.6的7.8%飙升至<span style="color:#fbbf24;font-weight:700;">99.9%接近满分</span>，Claude Opus 5仅30%；<br>
    • FrontierMath Tier 4高阶数学97.6%、GPQA Diamond研究生级问答96%；<br>
    • ExploitBench漏洞利用<span style="color:#f87171;font-weight:700;">100%</span>（5.6为78.5%），新漏洞测试成功率39%（5.6仅5.5%）；<br>
    • 计算机操作能力突破：直接"看屏幕"操作KiCad完成PCB布局走线（2分54秒）、Blender建模+虚幻5场景漫游、eBay上架等跨软件工作流；OSWorld 2.0得分72.6%（5.6为65.7%），速度快近50%；<br>
    • 越界率从5.6的48%降至<span style="color:#34d399;font-weight:700;">0%</span>，安全对齐大幅提升；<br>
    • API定价：输入$10/百万token、输出$50/百万token（5.6促销价2.5倍），快速模式翻倍；<br>
    • OpenAI总裁Brockman："我认为我们已经到了AGI阶段，欢迎来到AGI时代。"<br><br>
    <strong style="color:#34d399;">【英伟达129.3亿美元收购Hugging Face】</strong><br>
    英伟达史上最大单笔收购，80倍PS。HF托管300万+模型、50万数据集、100万应用，1800万开发者、20万+企业用户，年化收入从1亿快速增至1.5亿美元。<br>
    战略意图：①防御OpenAI/Anthropic自研芯片（OpenAI本周Jalapeño芯片宣称超Blackwell）；②掌控开源AI生态分发入口；③为DGX Cloud过剩算力找出口；④与Stripe 80亿收购OpenRouter形成AI"中间层"并购浪潮。黄仁勋承诺平台开放不强制英伟达硬件。
    """,
    trigger="""
    <strong style="color:#fbbf24;">1. AI产业三重共振（S级）：</strong><br>
    • GPT-6能力跨越式升级，AI Agent从概念走向可执行工作流，直接利好AI算力/推理芯片/先进封装/液冷/AI应用全产业链；<br>
    • API定价2.5倍提升=推理算力需求爆发，推理侧投资逻辑强化（区别于训练侧）；<br>
    • 英伟达收购HF+N1X端侧芯片10月上市，构建"云-端-开源生态"三位一体护城河。<br><br>
    <strong style="color:#a78bfa;">2. 流动性边际转松（A级）：</strong><br>
    • 沃勒鸽派是关键转折，9月加息预期大幅降温；<br>
    • 美债收益率全线回落（10Y-5bp），成长股估值压制缓解；<br>
    • 但周五非农+下周CPI仍是关键变量。<br><br>
    <strong style="color:#fb923c;">3. 国内产业催化密集（A/B级）：</strong><br>
    • 深交所9月4日发布<span style="color:#f87171;font-weight:700;">创业板芯片指数（970096）</span>，半导体被动资金流入预期；<br>
    • 长电科技拟定增65亿扩产高性能计算高端先进封装；<br>
    • 澜起科技CXL 3.2 MXC芯片率先导入三星/SK海力士下一代产品；<br>
    • 精智达签15.76亿半导体测试设备大单；<br>
    • 亚康股份/行云科技各签9.22亿算力租赁协议；<br>
    • 中际旭创连续三日回购累计8.03亿；<br>
    • 工信部等十部门印发中小企业"十五五"规划，投早投小投硬科技；<br>
    • <span style="color:#f87171;">风险：金帝股份液冷澄清"尚未形成批量订单"</span>，四天三板后PE 55倍高于行业41倍，液冷分化预警。
    """
)

# ============ 4. 产业链分析 ============
gen.add_industry_chain_analysis(
    upstream=[
        {"name": "AI算力芯片/GPU", "desc": "GPT-6推理算力爆发+N1X端侧芯片落地，算力最大受益方向", "stocks": [{"code": "300474", "name": "景嘉微", "impact": "GPU国产替代"}, {"code": "688256", "name": "寒武纪", "impact": "AI芯片龙头"}]},
        {"name": "半导体设备/先进封装", "desc": "长电65亿定增扩产+GPT-6驱动HBM/CoWoS需求持续", "stocks": [{"code": "600584", "name": "长电科技", "impact": "封测龙头定增"}, {"code": "002371", "name": "北方华创", "impact": "设备龙头"}]},
        {"name": "半导体材料", "desc": "HBM/先进封装扩产拉动前驱体/靶材/电子特气需求", "stocks": [{"code": "002409", "name": "雅克科技", "impact": "HBM前驱体"}, {"code": "688019", "name": "安集科技", "impact": "CMP抛光液"}]},
        {"name": "液冷散热", "desc": "AI芯片功耗3年翻3倍，金刚石散热是物理最优解；金帝澄清无订单板块分化", "stocks": [{"code": "002837", "name": "英维克", "impact": "液冷龙头"}, {"code": "002536", "name": "飞龙股份", "impact": "液冷泵"}]},
    ],
    midstream=[
        {"name": "CXL/内存接口芯片", "desc": "澜起CXL3.2导入三星/SK海力士，2027年CXL规模商用元年", "stocks": [{"code": "688008", "name": "澜起科技", "impact": "CXL首发量产"}]},
        {"name": "光模块/光通信", "desc": "博通Q4指引不及预期+Ciena跌10%，高预期标的短期承压，旭创8亿回购托底", "stocks": [{"code": "300308", "name": "中际旭创", "impact": "回购8亿托底"}, {"code": "300394", "name": "天孚通信", "impact": "光器件"}]},
        {"name": "PCB/铜箔", "desc": "GPT-6可自主PCB布局验证AI服务器PCB需求；铜价近历史新高支撑铜箔", "stocks": [{"code": "301217", "name": "铜冠铜箔", "impact": "PCB铜箔"}, {"code": "002463", "name": "沪电股份", "impact": "AI服务器PCB"}]},
        {"name": "AI Agent/软件应用", "desc": "GPT-6操作电脑能力飞跃，Agent SaaS落地加速，有真实付费的软件公司受益", "stocks": [{"code": "300624", "name": "万兴科技", "impact": "AI应用"}, {"code": "688111", "name": "金山办公", "impact": "AI办公"}]},
    ],
    downstream=[
        {"name": "算力租赁/IDC", "desc": "推理算力爆发+两单9.22亿算力租赁协议验证景气度", "stocks": [{"code": "301085", "name": "亚康股份", "impact": "9.22亿订单"}, {"code": "000977", "name": "浪潮信息", "impact": "AI服务器"}]},
        {"name": "黄金/贵金属", "desc": "金价突破4470逼近4500，地缘+降息双驱动，基金减持需注意分化", "stocks": [{"code": "600547", "name": "山东黄金", "impact": "黄金龙头"}, {"code": "600489", "name": "中金黄金", "impact": "黄金"}]},
        {"name": "创业板芯片指数", "desc": "9/4深交所发布创业板芯片指数（970096），被动配置+ETF预期", "stocks": []},
        {"name": "半导体测试设备", "desc": "精智达15.76亿大单验证国产化加速", "stocks": [{"code": "688627", "name": "精智达", "impact": "15.76亿订单"}, {"code": "688200", "name": "华峰测控", "impact": "测试设备"}]},
    ]
)

# ============ 5. 投资机会 ============
gen.add_investment_opportunities([
    {
        "name": "🔥 S级：AI推理算力/先进封装全产业链（GPT-6 AGI时代核心受益）",
        "priority": "高",
        "logic": "GPT-6能力飞跃+API定价2.5倍+英伟达收购HF，AI推理算力进入新一轮爆发周期。Agent从Chat走向Action（操作电脑/工作流），推理调用量指数级增长。算力芯片→先进封装→HBM→液冷全链条受益。但博通/Ciena指引不及预期显示光通信高预期环节短期有回吐压力，优先业绩兑现度高+订单验证方向。",
        "stocks": [
            {"code": "688256", "name": "寒武纪", "impact": "AI推理芯片核心标的"},
            {"code": "600584", "name": "长电科技", "impact": "65亿定增加码先进封装"},
            {"code": "002409", "name": "雅克科技", "impact": "HBM前驱体龙头"},
            {"code": "688008", "name": "澜起科技", "impact": "CXL3.2首发导入三星/SK"},
        ]
    },
    {
        "name": "🔥 S级：英伟达产业链（N1X端侧AI+HF生态整合）",
        "priority": "高",
        "logic": "英伟达129亿收购HF+N1X芯片10月上市+300亿投资OpenAI+1080亿信用支持，构建芯片-云-生态全栈护城河。端侧AI推理设备（RTX Spark 128GB统一内存）打开AI PC/边缘计算新市场，利好PCB/散热/先进封装国产供应链。",
        "stocks": [
            {"code": "300308", "name": "中际旭创", "impact": "连续3日回购8亿托底"},
            {"code": "002837", "name": "英维克", "impact": "液冷散热（注意深跌后反弹）"},
            {"code": "301217", "name": "铜冠铜箔", "impact": "AI服务器PCB铜箔"},
        ]
    },
    {
        "name": "⚡ A级：半导体设备/材料国产替代（多重共振）",
        "priority": "高",
        "logic": "①创业板芯片指数9/4发布带来被动资金；②长电65亿定增+精智达15.76亿测试设备大单验证国产化加速；③澜起CXL3.2导入三星/SK是国产互连芯片里程碑；④中际旭创/安集科技回购+H股上市催化。",
        "stocks": [
            {"code": "688627", "name": "精智达", "impact": "15.76亿半导体测试大单"},
            {"code": "002371", "name": "北方华创", "impact": "半导体设备平台龙头"},
            {"code": "688019", "name": "安集科技", "impact": "CMP抛光液+H股上市"},
        ]
    },
    {
        "name": "⚡ A级：黄金/贵金属（地缘+流动性双驱动）",
        "priority": "中",
        "logic": "金价逼近4500美元创历史新高，中东地缘+沃勒鸽派+荷兰/法国央行黄金迁移多重催化。但基金上半年减持黄金股24%，板块内部分化，优选业绩增速靠前标的。",
        "stocks": [
            {"code": "600547", "name": "山东黄金", "impact": "黄金龙头"},
            {"code": "601069", "name": "西部黄金", "impact": "基金增持标的"},
        ]
    },
    {
        "name": "⚠️ 风险预警：液冷纯概念标的（金帝股份澄清无订单）",
        "priority": "低",
        "logic": "金帝股份四天三板后发异动公告明确液冷项目尚未形成批量生产能力/收入/正式订单，PE 55倍高于行业41倍，两日换手35%。液冷板块短期涨幅大后分化不可避免，飞龙股份已有批量订单/金富科技液冷已并表的真标的相对安全，无订单纯概念股注意回调。",
        "stocks": [
            {"code": "603270", "name": "金帝股份", "impact": "⚠️四天三板后澄清无订单"},
            {"code": "002536", "name": "飞龙股份", "impact": "已有批量订单趋势较强"},
        ]
    }
], view_mode="tab")

# ============ 6. 持仓评估 ============
portfolio_html = """
<div style="display:flex;flex-direction:column;gap:14px;">
    <div style="background:linear-gradient(135deg,rgba(16,185,129,0.10) 0%,rgba(5,150,105,0.06) 100%);border-radius:14px;padding:20px;border:1px solid rgba(16,185,129,0.25);">
        <div style="display:flex;align-items:center;gap:10px;margin-bottom:10px;">
            <span style="font-size:18px;font-weight:800;color:#34d399;">铜冠铜箔 301217</span>
            <span style="background:linear-gradient(135deg,#10b981,#059669);color:white;padding:3px 10px;border-radius:20px;font-size:11px;font-weight:700;">🟢 GPT-6+PCB双催化利好</span>
        </div>
        <div style="font-size:13px;color:#d1fae5;line-height:1.9;">
            <strong>影响评估：正面</strong>。GPT-6具备直接完成PCB布局走线能力，验证AI服务器/端侧设备PCB需求爆发逻辑；高盛上调AI服务器PCB市场至2028年840亿美元；铜价近历史新高（澳新预测明年初创历史新高）支撑铜箔加工费。但前期涨幅较大，若高开过多注意减仓锁利。<br>
            <strong>操作建议：</strong>持有底仓为主，高开冲压力位可分批减仓1/3锁利，回踩支撑再接回。关注PCB板块开盘强度。
        </div>
    </div>
    <div style="background:linear-gradient(135deg,rgba(59,130,246,0.10) 0%,rgba(37,99,235,0.06) 100%);border-radius:14px;padding:20px;border:1px solid rgba(96,165,250,0.25);">
        <div style="display:flex;align-items:center;gap:10px;margin-bottom:10px;">
            <span style="font-size:18px;font-weight:800;color:#60a5fa;">雅克科技 002409</span>
            <span style="background:linear-gradient(135deg,#3b82f6,#1d4ed8);color:white;padding:3px 10px;border-radius:20px;font-size:11px;font-weight:700;">🟡 HBM逻辑强化+短期震荡</span>
        </div>
        <div style="font-size:13px;color:#bfdbfe;line-height:1.9;">
            <strong>影响评估：结构性正面</strong>。GPT-6推理算力爆发→AI服务器HBM需求维持高景气，前驱体长期逻辑不变；但隔夜美光/SK海力士盘中均跌，存储板块短期获利回吐压力。<br>
            <strong>操作建议：</strong>底仓持有，注意半导体板块整体情绪，不追高，150元以上逢高可分批减仓1/3锁利。
        </div>
    </div>
    <div style="background:linear-gradient(135deg,rgba(251,191,36,0.10) 0%,rgba(217,119,6,0.06) 100%);border-radius:14px;padding:20px;border:1px solid rgba(251,191,36,0.25);">
        <div style="display:flex;align-items:center;gap:10px;margin-bottom:10px;">
            <span style="font-size:18px;font-weight:800;color:#fbbf24;">英维克 002837</span>
            <span style="background:linear-gradient(135deg,#f59e0b,#d97706);color:white;padding:3px 10px;border-radius:20px;font-size:11px;font-weight:700;">⚠️ 液冷分化，金帝澄清拖累</span>
        </div>
        <div style="font-size:13px;color:#fde68a;line-height:1.9;">
            <strong>影响评估：分化</strong>。GPT-6+N1X验证AI散热长期逻辑（功耗3年翻3倍），但金帝盘后公告液冷"尚未形成批量订单/收入"将引发纯概念回调。英维克作为龙头有真实业绩，受影响小于纯概念，但板块情绪短期承压。前期深度破止损后反弹，反弹减仓纪律不变。<br>
            <strong>操作建议：</strong>反弹60-65元坚决减仓≥1/2，严格执行止损纪律，严禁补仓抄底。
        </div>
    </div>
    <div style="background:linear-gradient(135deg,rgba(239,68,68,0.10) 0%,rgba(185,28,28,0.06) 100%);border-radius:14px;padding:20px;border:1px solid rgba(239,68,68,0.25);">
        <div style="display:flex;align-items:center;gap:10px;margin-bottom:10px;">
            <span style="font-size:18px;font-weight:800;color:#f87171;">*ST建艺 002789</span>
            <span style="background:linear-gradient(135deg,#ef4444,#991b1b);color:white;padding:3px 10px;border-radius:20px;font-size:11px;font-weight:700;">🚨 立即清仓（最高优先级）</span>
        </div>
        <div style="font-size:13px;color:#fecaca;line-height:1.9;">
            <strong>影响评估：无影响，退市风险仍在</strong>。*ST康佳今日公告主动终止上市（停牌），ST板块风险偏好进一步承压，*ST建艺退市风险敞口未关闭，与AI催化完全无关。<br>
            <strong>操作建议：</strong>立即清仓止损，绝不恋战。任何价位都是离场机会。
        </div>
    </div>
</div>
"""
gen._components.append(Section(title="📊 持仓个股影响评估", content=portfolio_html, icon="briefcase"))

# ============ 7. 风险提示 ============
gen.add_risk_warning([
    "博通Q4指引不及预期收跌2.74%+Ciena跌10.36%，光通信/AI硬件高预期标的获利回吐风险，今日相关板块高开后可能冲高回落",
    "金帝股份四天三板后盘后澄清液冷项目无批量订单/收入/正式协议，PE 55倍高于行业41倍，两日换手35%，液冷纯概念标的今日面临回调",
    "今晚美国8月非农数据公布（预期+5.5万），若超预期强劲将重新点燃加息预期，外盘大幅波动",
    "GPT-6/AGI概念短期情绪过热，追高风险大，优先选有真实业绩/订单标的，规避纯题材炒作",
    "SK海力士-0.79%/美光盘中-2.43%/阿斯麦-2.15%，半导体设备/存储外盘走弱，A股相关标的开盘可能承压",
    "沃勒鸽派已被市场定价，9月加息概率仍有50%，降息预期未确立，流动性宽松预期不可过度线性外推",
    "*ST康佳主动终止上市，ST板块风险偏好下降，退市风险股坚决回避"
])

# ============ 8. 投资策略 ============
gen.add_investment_strategy("""
<div style="line-height:2;font-size:14px;">
    <div style="background:linear-gradient(135deg,rgba(239,68,68,0.15),rgba(239,68,68,0.05));border-radius:12px;padding:16px;margin-bottom:16px;border-left:4px solid #ef4444;">
        <strong style="color:#f87171;font-size:15px;">🎯 今日核心策略：AI算力主线积极做多，但警惕高开分化，结构重于仓位</strong>
    </div>
    <p><strong style="color:#fbbf24;">一、整体仓位建议：5-6成</strong></p>
    <p>隔夜双S级AI催化+沃勒鸽派是实质性利好组合，GPT-6 AGI时代开启是产业级事件（类比GPT-3/4发布时刻），风险偏好有望大幅提升。但需警惕：①博通/Ciena指引不及预期显示AI硬件高预期环节有分歧；②光通信/液冷等前期热炒板块有回调压力；③今晚非农不确定性。建议仓位5-6成，不宜满仓追高。</p>
    <p><strong style="color:#60a5fa;">二、进攻方向（优先级排序）：</strong></p>
    <ol style="padding-left:20px;">
        <li><strong style="color:#34d399;">AI推理算力/先进封装（S级）</strong>：GPT-6 API涨价2.5倍=推理算力爆发，长电65亿定增+澜起CXL3.2验证产业链景气。关注长电科技、澜起科技、寒武纪、雅克科技。</li>
        <li><strong style="color:#34d399;">半导体设备/材料（A级）</strong>：创业板芯片指数今日发布+精智达15.76亿大单+中际旭创回购，国产替代+被动资金流入双驱动。关注精智达、北方华创、安集科技。</li>
        <li><strong style="color:#a78bfa;">英伟达产业链（A级）</strong>：N1X端侧AI 10月上市+HF生态整合，关注有真实业绩的PCB/铜箔/光模块龙头。铜冠铜箔持有底仓，中际旭创回购托底。</li>
        <li><strong style="color:#fbbf24;">黄金（B级防御）</strong>：金价4470+地缘+鸽派，板块内部分化，短线事件驱动。</li>
    </ol>
    <p><strong style="color:#f87171;">三、回避方向：</strong></p>
    <ul style="padding-left:20px;">
        <li>液冷纯概念标的（金帝澄清无订单引发板块分化），英维克逢反弹减仓</li>
        <li>光通信高估值小票（博通/Ciena指引不及预期传导）</li>
        <li>*ST/退市风险股（*ST康佳终止上市引发ST恐慌），*ST建艺立即清仓</li>
        <li>无业绩支撑的纯AI概念炒作标的（GPT-6概念高开低走杀伤力大）</li>
    </ul>
    <p><strong style="color:#fb923c;">四、今日关键观察点：</strong></p>
    <ol style="padding-left:20px;">
        <li>开盘竞价：半导体/AI算力竞价强度，核心标的高开3%以上且封单坚决可适度参与；集体高开5%以上警惕高开低走</li>
        <li>创业板芯片指数（970096）今日首发，半导体资金流向是风向标</li>
        <li>北向资金开盘态度，大幅净流入则确认行情级别</li>
        <li>液冷板块开盘：金帝股份是否跌停/低开，决定液冷板块整体情绪</li>
        <li>两市成交量能否放大至2万亿以上（昨日1.76万亿缩量），量能是持续性关键</li>
    </ol>
    <p><strong style="color:#a78bfa;">五、持仓操作纪律：</strong></p>
    <ul style="padding-left:20px;">
        <li>🟢 铜冠铜箔：持有底仓，高开冲压力位减1/3锁利</li>
        <li>🟡 雅克科技：底仓持有，不追高，逢高减仓</li>
        <li>⚠️ 英维克：反弹60-65元坚决减仓≥1/2，严禁补仓</li>
        <li>🚨 *ST建艺：任何价格立即清仓（最高优先级）</li>
    </ul>
</div>
""")

# ============ 发布 ============
result = gen.publish(
    filename="20260904_盘前_S级催化扫描_GPT6_AGI时代+英伟达129亿收购HF+沃勒鸽派.html",
    excerpt="9月4日盘前S级催化：GPT-6 Astra发布宣告AGI时代+英伟达129亿美元收购Hugging Face+沃勒鸽派言论推动美股创近1月最大涨幅，AI算力/先进封装/半导体设备全线受益，警惕液冷概念分化与博通指引风险。"
)
print("="*60)
print(f"PUBLISH RESULT: {result}")
print("="*60)
