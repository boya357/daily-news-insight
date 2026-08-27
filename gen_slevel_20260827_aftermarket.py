#!/usr/bin/env python3
"""
20260827 盘后S级催化扫描生成脚本
"""
import sys, os
sys.path.insert(0, 'v3')
os.chdir('/root/daily-news-insight')

from v3.generators.s_level_catalyst import SLevelCatalystGenerator
from v3.components.layout import Section

gen = SLevelCatalystGenerator(
    date_str="20260827",
    catalyst_title="英伟达核弹财报引爆科技全面反攻：科创50暴涨3.77%+铠侠闪迪5万亿扩产+持仓全线大涨",
    subtitle="2026.08.27 · 盘后S级催化"
)

# 1. 催化事件概述
gen.add_catalyst_overview(
    overview='''<p><strong>【S级重大催化 - AI算力超级周期全面确认】</strong>北京时间8月27日凌晨，英伟达发布2027财年Q2财报，交出"核弹级"成绩单：单季营收<strong>962亿美元同比+106%</strong>，数据中心收入890亿美元同比+117%，Q3指引1080亿美元大超预期，2028财年营收指引同比+70%（此前市场预期仅44-45%），客户承诺订单从1190亿飙升至2790亿美元。黄仁勋定调"AI已到拐点，Token是有生产力的，算力直接等同于企业营收"。盘后英伟达从跌3%暴力拉升至涨7%报222美元。</p>
    <p style="margin-top:8px;"><strong>【A股放量反攻】</strong>受英伟达财报提振，A股科技板块全面爆发：上证+1.13%、深成指+1.50%、创业板+1.71%、<strong>科创50暴涨3.77%领涨</strong>，两市成交2.13万亿放量3172亿，主力资金净流入589亿连续3日，北向净买入62.36亿。半导体+5.04%、HBM/存储/CPO/PCB/覆铜板全线爆发。</p>
    <p style="margin-top:8px;"><strong>【多重共振】</strong>①铠侠+闪迪宣布6年5万亿日元(314亿美元)扩产NAND；②高通联手三星/SK海力士推进HBC芯片2027年商业化；③中报业绩爆发（铜冠铜箔+514%、香农芯创+2207%、金安国纪+987%）；④1-7月规上工企利润+17.6%。</p>
    <p style="margin-top:8px;"><strong>【持仓全线大涨】</strong>英维克+6.28%收65.97元（3日累涨约20%）、铜冠铜箔+6.22%收114.53元（主力净流入3.06亿）、雅克科技+6.42%收143.91元（主力净流入2.29亿）。</p>''',
    importance="S级"
)

# 2. 催化事件详解
gen.add_catalyst_details(
    background='''
    <p><strong>1. 英伟达Q2财报：AI算力拐点的历史性确认</strong></p>
    <p>英伟达2027财年Q2核心数据：营收962亿美元（预期920亿，同比+106%环比+18%），净利润596.9亿美元（+126%），数据中心890亿美元（+117%占比92%），毛利率75%，EPS 2.22美元（预期2.09）。Q3指引1080亿美元±2%（不含中国数据中心），FY2028营收+70%大超预期的44-45%。客户承诺订单从1190亿暴增至2790亿美元，单季返还股东260亿美元，剩余回购授权990亿。Vera Rubin全面投产，撬动超5000亿美元第三方AI基建。</p>
    <p>CFO透露：客户预测明年需求翻一番但受供应（尤其内存）限制，能把握+70%；受内存价格极端高企影响Q4毛利率降至71-72%，FY2028稳定在72-73%；对华H200已交付但占比&lt;1%。黄仁勋："AI已到拐点，算力直接等同于企业营收"。</p>
    <p style="margin-top:12px;"><strong>2. A股科技全面爆发：从缩量修复到放量上攻</strong></p>
    <p>8月27日成交2.13万亿放量3172亿，全市场3394涨1944跌，78涨停4跌停，恐贪指数从8天前冰点27.3升至61.5。电子特大单净流入347.8亿居首，通信+92.4亿，资金从银行(-1.04%)、电力设备(-0.71%，阳光电源-12.24%)撤出加仓科技。</p>
    <p style="margin-top:12px;"><strong>3. 存储超级周期再强化：铠侠+闪迪5万亿扩产</strong></p>
    <p>铠侠与闪迪联合宣布：到2032年在日本合计投入5万亿日元（314亿美元），北上工厂投入1.8万亿日元生产面向AI数据中心的高密度3D NAND，希望日本政府承担1/3成本。铠侠东京收涨5%，美股盘前闪迪+5%。全球存储原厂All-in扩产，"higher for longer"逻辑再获验证。</p>
    <p style="margin-top:12px;"><strong>4. 高通HBC芯片2027商业化：新存储架构破局</strong></p>
    <p>高通在"德意志银行2026科技大会"透露已与三星、SK海力士推进高带宽计算(HBC)芯片合作，对方反应积极主动提方案，计划2027年商业化。HBC有望成为继HBM之后下一代AI存储架构。</p>
    ''',
    trigger='''
    <p><strong>🔥 触发一：英伟达财报+盘后暴力反转</strong></p>
    <p>财报刚出盘后一度跌超3%（Q3指引1080亿未到部分机构喊的1100亿+），但电话会FY2028+70%+订单2790亿后暴力拉升，最大涨幅突破7%报222美元。TTM科技(PCB)+8.37%、Lumentum(光通信)+6.04%等英伟达链逆势大涨。</p>
    <p style="margin-top:8px;"><strong>🔥 触发二：A股主力589亿净流入，电子/通信天量涌入</strong></p>
    <p>主力连续3日净流入589亿；电子+297.8亿（+4.31%），半导体+173.7亿（+5.04%），元件+125.2亿（+5.09%），通信+101.28亿（+3.39%）。生益科技主力净买24-27亿居首，亨通光电超31亿，德明利/长飞/胜宏/工业富联/澜起均超10亿。龙虎榜机构合计净买24.38亿，德明利机构净买13.57亿居首。</p>
    <p style="margin-top:8px;"><strong>🔥 触发三：中报业绩爆发潮</strong></p>
    <p>铜冠铜箔+514.75%（HVM铜箔量价齐升）、香农芯创+2207%（海普存储+996%）、富瀚微+1419%、金安国纪+987%（CCL订单饱满供不应求）、亨通光电+93%、中国人寿+228.6%。1-7月规上工企利润+17.6%（制造业+18.8%）。</p>
    <p style="margin-top:8px;"><strong>🔥 触发四：持仓全线大涨</strong></p>
    <p>英维克+6.28%收65.97元（成交68.45亿换手9.41%），3日累涨约20%；铜冠铜箔+6.22%收114.53元（成交42.07亿换手4.53%，主力净流入3.06亿）；雅克科技+6.42%收143.91元（成交28.07亿换手6.24%，主力净流入2.29亿）。</p>
    '''
)

# 3. 产业链分析
gen.add_industry_chain_analysis(
    upstream=[
        {'name': '半导体材料（HBM前驱体/电子特气/封装材料）', 'desc': '英伟达CFO定调内存是最大瓶颈，高通HBC 2027商业化打开空间。雅克科技HBM前驱体+电子特气双主线受益。', 'stocks': [
            {'code': '002409', 'name': '雅克科技', 'impact': '【持仓】HBM前驱体龙头+6.42%'},
            {'code': '688535', 'name': '华海诚科', 'impact': '环氧塑封料GPM'},
            {'code': '688300', 'name': '联瑞新材', 'impact': '球硅填料+20cm涨停，机构净买1.2亿'},
        ]},
        {'name': '覆铜板/电子铜箔（CCL/HVM铜箔）', 'desc': '金安国纪+987%验证CCL订单饱满供不应求，高盛上调AI服务器PCB市场38%至2028年840亿美元。', 'stocks': [
            {'code': '301217', 'name': '铜冠铜箔', 'impact': '【持仓】HVM铜箔+514%业绩，+6.22%'},
            {'code': '600183', 'name': '生益科技', 'impact': 'CCL龙头，主力净买24-27亿全市场第一'},
            {'code': '002636', 'name': '金安国纪', 'impact': '涨停+净利+987%'},
        ]},
        {'name': '半导体设备', 'desc': '布图设计保护条例10/15实施（惩罚性赔偿+光子/量子芯片），拓荆科技5亿设产业基金，盛美订单+105%。', 'stocks': [
            {'code': '688082', 'name': '盛美上海', 'impact': '新签订单+105%'},
            {'code': '688072', 'name': '拓荆科技', 'impact': '5亿设产业基金'},
        ]},
    ],
    midstream=[
        {'name': '液冷散热', 'desc': 'Rubin全面投产推升服务器功耗，英维克Q2利润环比+1934%确立业绩拐点，SoluKing获英特尔认证。', 'stocks': [
            {'code': '002837', 'name': '英维克', 'impact': '【持仓】液冷龙头Q2拐点，3日累涨约20%'},
            {'code': '300648', 'name': '申菱环境', 'impact': '液冷+储能温控'},
        ]},
        {'name': '存储芯片/HBM', 'desc': '铠侠闪迪5万亿扩产+英伟达CFO定调瓶颈+HBC新架构。德明利涨停机构净买13.57亿。', 'stocks': [
            {'code': '001309', 'name': '德明利', 'impact': '涨停+机构净买13.57亿'},
            {'code': '301217', 'name': '铜冠铜箔', 'impact': '【持仓】存储铜箔+514%'},
            {'code': '300475', 'name': '香农芯创', 'impact': '净利+2207%（海普存储+996%）'},
        ]},
        {'name': 'PCB/AI服务器板', 'desc': '板块26股涨停，AI服务器PCB价值量是传统5-8倍，高层数HDI/高速板需求爆发。', 'stocks': [
            {'code': '600183', 'name': '生益科技', 'impact': '主力净买27亿'},
            {'code': '300476', 'name': '胜宏科技', 'impact': 'AI服务器PCB龙头'},
            {'code': '301400', 'name': '嘉立创', 'impact': 'PCB涨停'},
        ]},
        {'name': 'AI芯片/算力', 'desc': '英伟达FY2028+70%+2790亿订单，九大CSP CapEx 2026破8300亿(+79%)。', 'stocks': [
            {'code': 'NVDA', 'name': '英伟达(美股)', 'impact': '盘后+5-7%至222美元'},
            {'code': '601138', 'name': '工业富联', 'impact': 'AI服务器代工'},
        ]},
    ],
    downstream=[
        {'name': '光模块/CPO/光通信', 'desc': 'TTM+8.37%/Lumentum+6.04%隔夜大涨；A股长飞光纤涨停、赛微电子20cm、亨通光电涨停主力净买31亿。', 'stocks': [
            {'code': '600487', 'name': '亨通光电', 'impact': '涨停+主力净买31亿+中报+93%'},
            {'code': '601869', 'name': '长飞光纤', 'impact': '涨停'},
            {'code': '300308', 'name': '中际旭创', 'impact': '光模块龙头'},
        ]},
        {'name': 'AI服务器/IDC', 'desc': '2790亿订单+5000亿第三方AI基建撬动，云厂商CSP资本开支持续超预期。', 'stocks': [
            {'code': '000977', 'name': '浪潮信息', 'impact': 'AI服务器龙头'},
            {'code': '601138', 'name': '工业富联', 'impact': '主力净买居前'},
        ]},
    ]
)

# 4. 投资机会
gen.add_investment_opportunities(
    opportunities=[
        {'name': 'AI算力全产业链（S级）', 'priority': '高',
         'logic': '英伟达Q2核弹财报+FY2028+70%+2790亿订单是AI算力超级周期最权威产业验证。A股科创50+3.77%放量上攻，主力589亿净流入，内外资共振做多，是业绩驱动主升浪起点。',
         'stocks': [
             {'code': '002837', 'name': '英维克', 'impact': '【持仓】液冷Q2拐点+3日涨约20%'},
             {'code': '300308', 'name': '中际旭创', 'impact': '光模块龙头'},
             {'code': '601138', 'name': '工业富联', 'impact': 'AI服务器代工'},
         ]},
        {'name': '存储芯片/HBM（S级）', 'priority': '高',
         'logic': '铠侠闪迪5万亿扩产+CFO定调内存瓶颈至2028+HBC新架构2027，存储超级周期持续验证。铜冠+514%/香农+2207%中报验证景气传导。',
         'stocks': [
             {'code': '301217', 'name': '铜冠铜箔', 'impact': '【持仓】+514%业绩+主力净买3亿'},
             {'code': '001309', 'name': '德明利', 'impact': '涨停+机构净买13.57亿'},
             {'code': '002409', 'name': '雅克科技', 'impact': '【持仓】HBM前驱体+6.42%'},
         ]},
        {'name': 'PCB/CCL覆铜板（S级）', 'priority': '高',
         'logic': '金安国纪+987%验证CCL供不应求，26股涨停，生益科技主力净买27亿全市场第一。高盛上调AI服务器PCB市场38%。',
         'stocks': [
             {'code': '600183', 'name': '生益科技', 'impact': '主力净买27亿全市场第一'},
             {'code': '002636', 'name': '金安国纪', 'impact': '涨停+987%'},
             {'code': '301217', 'name': '铜冠铜箔', 'impact': '【持仓】电子铜箔'},
         ]},
        {'name': '液冷散热（A级）', 'priority': '高',
         'logic': '英维克Q2+1934%确立业绩拐点，Rubin投产推动液冷渗透率从15%向50%加速。短期3日涨约20%注意超买，中期确定。',
         'stocks': [
             {'code': '002837', 'name': '英维克', 'impact': '【持仓】液冷龙头，3日涨约20%成交68亿'},
             {'code': '300648', 'name': '申菱环境', 'impact': '液冷+储能'},
         ]},
        {'name': '半导体材料/设备（A级）', 'priority': '中',
         'logic': '布图设计保护条例+拓荆5亿基金+盛美订单+105%，制度+资本+业绩三重驱动。联瑞新材20cm涨停验证资金认可。',
         'stocks': [
             {'code': '002409', 'name': '雅克科技', 'impact': '【持仓】HBM+特气双主线'},
             {'code': '688300', 'name': '联瑞新材', 'impact': '20cm+机构净买1.2亿'},
         ]},
    ],
    view_mode="tab"
)

# 5. 隔夜外盘
overnight_html = '''
<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px;">
<div style="background: rgba(34,197,94,0.08); border-radius: 12px; padding: 16px; border: 1px solid rgba(34,197,94,0.2);">
<div style="font-size:14px;font-weight:700;color:#4ade80;margin-bottom:10px;">📈 8月26日美股收盘</div>
<div style="font-size:13px;color:#cbd5e1;line-height:2;">
<p>道指：<span style="color:#f87171;">-0.21%</span> 53463</p>
<p>标普500：<span style="color:#f87171;">-0.02%</span> 7675</p>
<p>纳指：<span style="color:#f87171;">-0.08%</span> 26130</p>
<p>费半SOX：<span style="color:#4ade80;">+0.20%</span></p>
<p>英伟达正股：<span style="color:#f87171;">-1.59%</span> 209.66（盘后+5-7%至222）</p>
<p>TTM(PCB)：<span style="color:#4ade80;">+8.37%</span>；Lumentum：<span style="color:#4ade80;">+6.04%</span></p>
</div></div>
<div style="background: rgba(245,158,11,0.08); border-radius: 12px; padding: 16px; border: 1px solid rgba(245,158,11,0.2);">
<div style="font-size:14px;font-weight:700;color:#fcd34d;margin-bottom:10px;">🔥 英伟达Q2核心数据</div>
<div style="font-size:13px;color:#cbd5e1;line-height:2;">
<p>Q2营收：<span style="color:#4ade80;">962亿美元</span>（预期920，+106%）</p>
<p>数据中心：<span style="color:#4ade80;">890亿美元</span>（+117%）</p>
<p>Q3指引：<span style="color:#4ade80;">1080亿±2%</span>（不含中国）</p>
<p>FY2028：<span style="color:#4ade80;">+70%</span>（预期44-45%）</p>
<p>客户承诺订单：2790亿（Q1为1190亿）</p>
<p>毛利率预警：Q4降至71-72%（内存涨价）</p>
</div></div>
<div style="background: rgba(168,85,247,0.08); border-radius: 12px; padding: 16px; border: 1px solid rgba(168,85,247,0.2);">
<div style="font-size:14px;font-weight:700;color:#c084fc;margin-bottom:10px;">💎 8月27日美股盘前</div>
<div style="font-size:13px;color:#cbd5e1;line-height:2;">
<p>英伟达：<span style="color:#4ade80;">+7%</span> 222美元</p>
<p>闪迪SNDK：<span style="color:#4ade80;">+5%</span>（铠侠扩产）</p>
<p>迈威尔MRVL：<span style="color:#4ade80;">+5%</span>（今晚发财报）</p>
<p>ARM：<span style="color:#4ade80;">+4%</span>；英特尔：<span style="color:#4ade80;">+2%</span></p>
<p>纳指期货：<span style="color:#4ade80;">+1%以上</span></p>
</div></div>
<div style="background: rgba(59,130,246,0.08); border-radius: 12px; padding: 16px; border: 1px solid rgba(59,130,246,0.2);">
<div style="font-size:14px;font-weight:700;color:#93c5fd;margin-bottom:10px;">🌏 亚太 & 产业重磅</div>
<div style="font-size:13px;color:#cbd5e1;line-height:2;">
<p>🇯🇵 铠侠+闪迪：6年<span style="color:#fbbf24;">5万亿日元扩产NAND</span></p>
<p>🇰🇷 高通+三星+SK海力士：<span style="color:#fbbf24;">HBC芯片2027商业化</span></p>
<p>🇭🇰 恒指-0.34%，芯片股逆势（澜起+12%、兆易+7%）</p>
<p>🇨🇳 1-7月规上工企利润：<span style="color:#4ade80;">+17.6%</span></p>
<p>🇨🇳 上海发布"智算光网"研发专项</p>
<p>🇨🇳 四部门IC企业非货币性资产可分期缴税</p>
</div></div>
</div>
<p style="margin-top:10px;font-size:12px;color:#94a3b8;">数据来源：财联社、证券时报、新浪财经、第一财经 | 2026.08.27 盘后</p>
'''
gen._components.append(Section(title="🌍 隔夜外盘 & 全球半导体动态", content=overnight_html, icon="globe"))

# 6. 龙虎榜
dragon_html = '''
<div style="background:rgba(245,158,11,0.06);border-radius:14px;padding:20px;border:1px solid rgba(245,158,11,0.2);">
<div style="font-size:15px;font-weight:700;color:#fcd34d;margin-bottom:16px;">🐯 龙虎榜机构动向（8月27日）</div>
<div style="font-size:13px;color:#cbd5e1;">
<p style="margin-bottom:12px;">今日44只个股现身龙虎榜机构席位，<strong>27只净买入、17只净卖出</strong>，机构合计<strong>净买入24.38亿元</strong>（买入122.72亿/卖出98.35亿），全面做多科技。</p>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:12px;">
<div style="background:rgba(34,197,94,0.06);border-radius:10px;padding:12px;border:1px solid rgba(34,197,94,0.15);">
<div style="font-weight:600;color:#4ade80;margin-bottom:8px;">🏆 机构净买入TOP5</div>
<div style="font-size:12px;line-height:1.9;">
<p>1.德明利(001309)：<span style="color:#4ade80;">+13.57亿</span> | 涨停+存储龙头</p>
<p>2.东方钽业(000962)：<span style="color:#4ade80;">+4.43亿</span> | 涨停</p>
<p>3.汉森制药(002412)：<span style="color:#4ade80;">+2.29亿</span> | +7.10%</p>
<p>4.神农种业(301119)：<span style="color:#4ade80;">+2.13亿</span> | +9.05%</p>
<p>5.恒铭达(002947)：<span style="color:#4ade80;">+1.99亿</span> | +4.74%</p>
</div></div>
<div style="background:rgba(239,68,68,0.06);border-radius:10px;padding:12px;border:1px solid rgba(239,68,68,0.15);">
<div style="font-weight:600;color:#f87171;margin-bottom:8px;">⚠️ 机构净卖出TOP3</div>
<div style="font-size:12px;line-height:1.9;">
<p>1.通鼎互联(002491)：<span style="color:#f87171;">-4.21亿</span> | +5.05%</p>
<p>2.千金药业(600479)：<span style="color:#f87171;">-1.24亿</span> | +0.38%</p>
<p>3.思源电气(002028)：<span style="color:#f87171;">-1.08亿</span> | 跌停（电力设备）</p>
</div></div>
</div>
<div style="margin-top:14px;padding:12px;background:rgba(59,130,246,0.06);border-radius:10px;border:1px solid rgba(59,130,246,0.15);">
<div style="font-weight:600;color:#60a5fa;margin-bottom:8px;">💡 特大单资金动向</div>
<div style="font-size:12px;line-height:1.9;color:#cbd5e1;">
<p>• 电子行业特大单<span style="color:#4ade80;">净流入347.8亿</span>居首，通信+92.4亿</p>
<p>• 生益科技+24.4亿、亨通光电超31亿、长飞光纤+19.4亿居前</p>
<p>• 电力设备净流出24.2亿（<strong>阳光电源-12.24%</strong>），宁德-10.2亿，资金弃防御加仓科技</p>
<p>• 北向资金净买入<span style="color:#4ade80;">62.36亿</span>，内外资共振</p>
</div></div>
<div style="margin-top:14px;padding:12px;background:rgba(245,158,11,0.06);border-radius:10px;border:1px solid rgba(245,158,11,0.15);">
<div style="font-weight:600;color:#fbbf24;margin-bottom:8px;">📊 持仓股验证</div>
<div style="font-size:12px;line-height:1.9;color:#cbd5e1;">
<p>• <strong>铜冠铜箔</strong>：主力净流入<span style="color:#4ade80;">3.06亿</span>（电力设备流入第2），换手4.53%良性</p>
<p>• <strong>英维克</strong>：3日主力净流入<span style="color:#4ade80;">18.58亿</span>，8/25机构净买1.76亿+深股通净买2.12亿</p>
<p>• <strong>雅克科技</strong>：主力净流入<span style="color:#4ade80;">2.29亿</span>（先进封装流入第1）</p>
<p>• <strong>*ST建艺</strong>：主力净流出75万，地量1590万，继续回避</p>
</div></div>
<p style="margin-top:14px;font-size:12px;color:#94a3b8;">数据来源：证券时报、东方财富Choice、金融界 | 2026.08.27</p>
</div></div>
'''
gen._components.append(Section(title="🐯 龙虎榜机构资金动向", content=dragon_html, icon="activity"))

# 7. 持仓分析
port_html = '''
<div style="display:grid;grid-template-columns:1fr 1fr;gap:16px;">
<div style="background:linear-gradient(135deg,rgba(34,197,94,0.12) 0%,rgba(22,163,74,0.06) 100%);border-radius:14px;padding:18px;border:1px solid rgba(34,197,94,0.3);">
<div style="font-size:14px;font-weight:700;color:#4ade80;margin-bottom:12px;">英维克 (002837) 液冷 ⭐S级</div>
<div style="font-size:13px;color:#cbd5e1;line-height:1.9;">
<p><strong>今日：</strong><span style="color:#4ade80;">+6.28%</span> 收<strong>65.97元</strong>，成交68.45亿换手9.41%</p>
<p><strong>3日累涨：</strong><span style="color:#4ade80;">约+20.5%</span>（54.75→65.97）</p>
<p><strong>催化：</strong><span style="color:#4ade80;"><strong>强正面</strong></span> 英伟达Rubin投产推升液冷需求+Q2利润环比+1934%业绩拐点+开源买入评级</p>
<p><strong>资金：</strong>3日主力净流入18.58亿（占比9.74%），8/25机构净买1.76亿</p>
<p><strong>技术：</strong>突破60元压力冲66元，接近68元前高压力区，MACD金叉但9.41%换手显示分歧</p>
<p><strong>估值：</strong>动态PE约50-55倍（H2业绩线性推算），液冷渗透率加速期可接受</p>
<p><strong>操作：</strong>持有底仓，<span style="color:#fbbf24;">66-70元减机动仓1/3锁利</span>；回踩60-62元接回；<span style="color:#4ade80;">止损上移至55元</span>，不追高</p>
</div></div>
<div style="background:linear-gradient(135deg,rgba(34,197,94,0.12) 0%,rgba(22,163,74,0.06) 100%);border-radius:14px;padding:18px;border:1px solid rgba(34,197,94,0.3);">
<div style="font-size:14px;font-weight:700;color:#4ade80;margin-bottom:12px;">铜冠铜箔 (301217) 电子铜箔 ⭐S级</div>
<div style="font-size:13px;color:#cbd5e1;line-height:1.9;">
<p><strong>今日：</strong><span style="color:#4ade80;">+6.22%</span> 收<strong>114.53元</strong>，成交42.07亿换手4.53%，振幅7.94%</p>
<p><strong>浮盈：</strong>成本87.16元，浮盈约<span style="color:#4ade80;">+31.4%</span></p>
<p><strong>催化：</strong><span style="color:#4ade80;"><strong>强正面</strong></span> 中报+514.75%+PCB/CCL涨停潮+铠侠5万亿扩产+主力净买3.06亿</p>
<p><strong>资金：</strong>电力设备流入第2（3.06亿），游资+6482万，散户-3.96亿（机构吸筹形态）</p>
<p><strong>技术：</strong>从8/20低点52.93反弹116%，115元短期压力（今日高115.36未站稳）</p>
<p><strong>估值：</strong>动态PE约190-220倍偏高，需Q3-Q4业绩持续上修消化</p>
<p><strong>操作：</strong>持有底仓，<span style="color:#fbbf24;">115-120元减机动仓1/3锁利</span>（套牢区）；回踩105-108元接回；<span style="color:#4ade80;">止损上移至100元</span></p>
</div></div>
<div style="background:linear-gradient(135deg,rgba(34,197,94,0.1) 0%,rgba(22,163,74,0.05) 100%);border-radius:14px;padding:18px;border:1px solid rgba(34,197,94,0.25);">
<div style="font-size:14px;font-weight:700;color:#4ade80;margin-bottom:12px;">雅克科技 (002409) 半导体材料 ⭐A级</div>
<div style="font-size:13px;color:#cbd5e1;line-height:1.9;">
<p><strong>今日：</strong><span style="color:#4ade80;">+6.42%</span> 收<strong>143.91元</strong>，成交28.07亿换手6.24%</p>
<p><strong>浮盈：</strong>成本108.8元，浮盈约<span style="color:#4ade80;">+32.3%</span></p>
<p><strong>催化：</strong><span style="color:#4ade80;"><strong>正面</strong></span> HBM前驱体受益内存瓶颈+电子特气昊华涨停+H1净利+7.29%（Q2+12%）</p>
<p><strong>资金：</strong>主力净流入2.29亿（工业气体第2/先进封装第1），净流入率7.41%健康</p>
<p><strong>技术：</strong>8/20高点152.18→8/26低点135.23调整后放量反弹，145元短期压力，150元强阻</p>
<p><strong>估值：</strong>动态PE约90-100倍，HBM前驱体全球稀缺可接受，需Q3业绩加速</p>
<p><strong>双重验证：</strong>无利空公告，中报为正面业绩（Q2+12%），无减持/风险</p>
<p><strong>操作：</strong>持有底仓，<span style="color:#fbbf24;">148-152元减机动仓1/3</span>；回踩138-140元接回；<span style="color:#4ade80;">止损130元</span></p>
</div></div>
<div style="background:linear-gradient(135deg,rgba(239,68,68,0.1) 0%,rgba(220,38,38,0.05) 100%);border-radius:14px;padding:18px;border:1px solid rgba(239,68,68,0.25);">
<div style="font-size:14px;font-weight:700;color:#f87171;margin-bottom:12px;">*ST建艺 (002789) ST股</div>
<div style="font-size:13px;color:#cbd5e1;line-height:1.9;">
<p><strong>今日：</strong><span style="color:#f87171;">-1.46%</span> 收<strong>10.15元</strong>，成交1590万地量，换手1.0%</p>
<p><strong>浮亏：</strong>成本约13.45元，浮亏约<span style="color:#f87171;">-24.5%</span></p>
<p><strong>催化：</strong><span style="color:#f87171;"><strong>无关联</strong></span> 科技大牛市中依然下跌，退市风险+债务问题+庭外重组不确定</p>
<p><strong>双重验证：</strong>中报预亏1.1-1.6亿，新增诉讼4401万占净资产21%，被列失信被执行人</p>
<p><strong>操作：</strong><span style="color:#f87171;"><strong>明日开盘清仓（最高优先级）</strong></span>，科技大牛带不动的ST股必须止损，释放仓位给科技主线</p>
</div></div>
</div>
<p style="margin-top:10px;font-size:12px;color:#94a3b8;">注：以上分析不构成投资建议。双重验证：价格/资金来自东方财富+证券时报+证券之星三源交叉；中报来自公司公告+财联社双源确认；减仓建议均附带技术位+估值锚。</p>
'''
gen._components.append(Section(title="📊 持仓股影响分析 & 操作建议", content=port_html, icon="briefcase"))

# 8. 风险提示
gen.add_risk_warning([
    '英伟达利好兑现风险：盘后+7%已部分price in，今晚美股若冲高回落可能引发A股高开低走',
    '内存涨价侵蚀毛利率风险：英伟达CFO预警Q4毛利率降至71-72%，对存储成本敏感标的承压',
    '短期超买回调：科创50单日+3.77%、英维克3日+20%、铜冠累计反弹116%，A50交割日+杰克逊霍尔年会扰动',
    '铜冠铜箔估值偏高：动态PE约190-220倍，需Q3-Q4持续超预期消化',
    '铠侠扩产过剩隐忧：花旗提示扩产时机可能恰逢2028年后周期拐点，铠侠自6月高点腰斩',
    '风格切换反复风险：资金从防御撤出加仓科技，若市场避险可能反向流动',
    '中美科技博弈：英伟达Q3不含中国数据中心收入，对华H200占比<1%，出口管制不确定性持续',
    '本报告不构成投资建议，股市有风险，投资需谨慎'
])

# 9. 投资策略
gen.add_investment_strategy('''
<p><strong>【整体判断】</strong>英伟达Q2核弹财报是AI算力产业趋势的"历史性确认"：962亿营收+106%、Q3指引1080亿、FY2028+70%（大超预期44-45%）、客户订单从1190亿暴增至2790亿，黄仁勋定调"AI已到拐点，算力=营收"。叠加铠侠闪迪5万亿扩产、高通HBC、中报爆发潮、工企利润+17.6%，<strong>科技主线从"缩量修复"切换为"放量上攻"</strong>，科创50+3.77%+成交2.13万亿+主力589亿净流入是明确信号。但短期3日急涨后获利盘堆积+A50交割日+杰克逊霍尔年会，<strong>明日大概率高开冲高后分化</strong>，忌追高后排。</p>
<p style="margin-top:12px;"><strong>【8/28周五关键变量】</strong></p>
<ul style="margin-top:8px;padding-left:20px;line-height:2;color:#e2e8f0;">
<li><strong>英伟达今晚走势</strong>：盘前+7%报222，正式开盘站稳则A股冲高；回落至+2%以下则高开低走</li>
<li><strong>迈威尔MRVL财报（今晚盘后）</strong>：定制AI芯片+高速互联核心供应商，超预期将催化光通信/CPO</li>
<li><strong>量能</strong>：守住2万亿以上则上攻有效；缩量至1.8万亿以下警惕假突破</li>
<li><strong>A50交割日+杰克逊霍尔年会</strong>：到期日波动放大+鲍威尔讲话影响流动性预期</li>
</ul>
<p style="margin-top:12px;"><strong>【仓位建议】</strong><span style="color:#4ade80;">6-7成</span>（较昨日上调1成），核心持有液冷+存储铜箔+半导体材料三主线，预留3成应对分化回踩。不追高，分歧回踩比追大阳更优。</p>
<p style="margin-top:12px;"><strong>【方向优先级】</strong></p>
<ol style="margin-top:8px;padding-left:20px;line-height:2;color:#e2e8f0;">
<li><strong>🥇 AI算力全链</strong> — 英伟达+2790亿订单确定性最强，液冷(英维克)+光模块+PCB+AI服务器核心持有</li>
<li><strong>🥈 存储/HBM</strong> — 铠侠扩产+CFO定调瓶颈+HBC新架构，铜冠+德明利+雅克受益</li>
<li><strong>🥉 PCB/CCL</strong> — 金安国纪+987%+生益主力净买27亿+高盛上调空间，业绩兑现最强</li>
<li>第四：半导体设备/材料 — 布图条例10月实施+国产替代长期逻辑，短期弹性弱于前三</li>
</ol>
<p style="margin-top:12px;"><strong>【持仓操作】</strong></p>
<ul style="margin-top:8px;padding-left:20px;line-height:2;color:#e2e8f0;">
<li><strong>英维克</strong>：66-70元减机动仓1/3，回踩60-62元接回，止损上移至55元</li>
<li><strong>铜冠铜箔</strong>：115-120元减机动仓1/3（套牢区），回踩105-108元接回，止损上移至100元</li>
<li><strong>雅克科技</strong>：148-152元减机动仓1/3，回踩138-140元接回，止损130元</li>
<li><strong>*ST建艺</strong>：<span style="color:#f87171;"><strong>明日开盘清仓（最高优先级）</strong></span>，释放仓位给科技主线</li>
</ul>
<p style="margin-top:12px;"><strong>【英伟达情景推演】</strong></p>
<ul style="margin-top:8px;padding-left:20px;line-height:2;color:#e2e8f0;">
<li><strong>情景一（45%）</strong>：英伟达收涨3-5%+MRVL超预期 → A股分化前排强者恒强，加仓至7成</li>
<li><strong>情景二（35%）</strong>：英伟达+0-3%+MRVL符合 → 震荡消化，维持6成</li>
<li><strong>情景三（20%）</strong>：英伟达冲高回落收跌 → 回踩3920-3930支撑，减仓至5成</li>
</ul>
<p style="margin-top:12px;"><strong>【中期展望】</strong>FY2028+70%+2790亿订单是AI算力"信仰充值"，2026Q3-2028资本开支周期确定性极高。这是<strong>业绩驱动主升浪的起点</strong>，不是题材尾声。英维克Q2拐点+铜冠+514%+金安国纪+987%验证"从故事到业绩"的转变。节奏上牢记：<strong>主升浪最大敌人是追高</strong>，分歧回踩是买点，一致高潮是卖点。*ST建艺果断清仓。</p>
''')

print("开始生成S级催化报告...")
html = gen.generate()
print(f"报告长度: {len(html)} 字符")
result = gen.publish(
    title="英伟达核弹财报引爆科技全面反攻：科创50暴涨3.77%+铠侠闪迪5万亿扩产+持仓全线大涨",
    report_type="s_level_catalyst",
    filename="20260827_盘后_S级催化扫描_英伟达核弹财报+科技全面反攻.html",
    excerpt="S级催化：英伟达Q2营收962亿+106%大超预期、FY2028+70%、客户订单2790亿翻倍；A股科创50暴涨3.77%成交2.13万亿放量上攻，主力净流入589亿；铠侠闪迪5万亿扩产NAND；持仓全线大涨。",
    auto_deploy=True, docs_root="docs"
)
print(f"发布结果: {result}")
print("任务完成！")
