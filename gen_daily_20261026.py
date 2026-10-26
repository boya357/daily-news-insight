#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-26 每日新闻洞察 - V3 Pro生成器"""
import sys, os
sys.path.insert(0, 'v3')
os.chdir('/root/daily-news-insight')
from generators.daily_pro import DailyReportProGenerator

gen = DailyReportProGenerator(
    date_str="2026-10-26",
    weekday="周一",
    subtitle="二十届五中全会今召开|存储芯片Q3业绩爆发德明利增29倍|油价暴涨创5月新高通胀担忧升温|A股指数编制新规今起实施|AWS容量2027年底前售罄",
    data_dir='/root/daily-news-insight/data'
)

# TL;DR
gen.set_tldr([
    ("二十届五中全会今召开 政策窗口期开启", "中国共产党第二十届中央委员会第五次全体会议今日至29日在北京召开，聚焦'十五五'规划与经济高质量发展，市场预期政策利好持续释放", "green"),
    ("存储芯片Q3业绩爆发 德明利净利增29倍", "德明利Q3净利同比增2903%，天齐锂业增1324%，寒武纪增148%，光迅科技增103%，科技成长股业绩端持续兑现支撑估值", "green"),
    ("油价暴涨创5月新高 通胀担忧压制美股", "布油涨至117美元创五个多月新高，全周涨超6%，美债收益率回升至4.99%，三大指数集体收跌，道指跌1.23%纳指跌0.21%", "red"),
    ("AWS容量2027年底前基本售罄 AI需求仍强", "亚马逊CEO贾西宣布AWS云计算容量2027年底前已基本售罄，大量订单排至2028年，AI基础设施需求远超市场预期", "green"),
], operation_advice="二十届五中全会召开+科技股业绩爆发双利好对冲外围压力，今日建议：仓位5-6成，重点关注存储/光通信/算力方向业绩兑现标的，持仓逢低加仓核心底仓，严格执行止损纪律", risk_level="中高", suggested_position="5-6成")

gen.set_holdings([
    {"name": "英维克", "code": "002837"},
    {"name": "铜冠铜箔", "code": "301217"},
    {"name": "雅克科技", "code": "002409"},
    {"name": "*ST建艺", "code": "002789"},
])

gen.set_og(
    description="10月26日盘前必读：二十届五中全会今日召开政策窗口开启；存储芯片Q3业绩大爆发德明利增29倍；油价暴涨创5月新高通胀担忧升温；AWS容量2027年底前售罄AI需求仍强",
    image=""
)

# 1. 隔夜全球市场
gen.add_global_market()

# 2. 市场总览
gen.add_market_overview()

print("Step 1-2 done")

# 3. 重大新闻（自定义tab切换）
news_tabs = [
    {
        "label": "海外市场",
        "content": gen.create_card_group([
            {
                "title": "🛢️ 油价暴涨布油突破117美元 创五个多月新高 通胀担忧重燃",
                "content": """中东地缘风险持续叠加供应担忧，国际油价周五大幅飙升：
<br><strong>油价数据：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>WTI 12月原油期货收涨 <strong style="color:#ef4444;">3.82%</strong> 报103.27美元/桶，全周累涨4.29%</li>
<li>布伦特12月原油期货收涨 <strong style="color:#ef4444;">3.14%</strong> 报116.72美元/桶，全周累涨6.24%</li>
<li>布油盘中一度冲向117美元，创五个多月新高，单周涨幅创六周最佳</li>
<li>石油巨头股价集体刷新历史新高：埃克森美孚+1.39%、雪佛龙+1.46%、壳牌+1.63%</li>
</ul>
<strong>通胀担忧升温：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>美国10月综合PMI初值57.6，企业售价涨幅创四年高位（2022年8月以来最高）</li>
<li>10年期美债收益率回升至4.99%，日内升约4个基点，脱离近一个月低位</li>
<li>制造业PMI升至56.0创53个月新高，油价、原材料及运输成本上涨加剧通胀压力</li>
<li>美联储10月27-28日议息会议在即，市场定价维持利率不变，但降息预期延后</li>
</ul>
<strong>对A股影响：</strong>油价上涨推升通胀预期，可能压制全球科技股估值，但利好能源板块。A股能源链（石油、煤炭、油服）有望受益。
<br><br>
<em style="opacity:0.6">来源：财联社、华尔街见闻、Trading Economics</em>""",
            },
            {
                "title": "📉 美股三大指数集体收跌 道指跌653点 全周涨跌分化",
                "content": """油价上涨引发通胀担忧叠加AI融资疑虑，美股周五全线收低：
<br><strong>收盘数据：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>道琼斯 <strong style="color:#ef4444;">-1.23%</strong> 报52215.16点（跌653点）</li>
<li>标普500 <strong style="color:#ef4444;">-0.52%</strong> 报7623.68点</li>
<li>纳斯达克 <strong style="color:#ef4444;">-0.21%</strong> 报25955.34点</li>
<li>VIX波动率指数涨2.21%至19.45</li>
<li>费城半导体指数 <strong style="color:#22c55e;">+0.44%</strong> 报10779.46点（小幅反弹）</li>
</ul>
<strong>全周表现：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>标普500全周跌0.47%，纳指全周跌0.71%，道指全周涨0.41%</li>
<li>科技股震荡加剧，AI融资担忧主导市场情绪</li>
<li>Meta全周跌逾9%，CoreWeave全周跌超10%</li>
<li>苹果一度创盘中新高，市值短暂超越英伟达升至第一后转跌</li>
</ul>
<strong>核心科技股表现：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>美光科技 <strong style="color:#22c55e;">+2.46%</strong>、AMD <strong style="color:#22c55e;">+1.74%</strong>、英特尔 <strong style="color:#22c55e;">+1.72%</strong></li>
<li>微软 <strong style="color:#22c55e;">+0.66%</strong>、台积电ADR <strong style="color:#22c55e;">+1.49%</strong></li>
<li>英伟达 -0.59%、苹果 -0.14%、博通 -0.48%</li>
<li>美国运通 -3.62%（超预期财报但裁员5%）</li>
</ul>
<em style="opacity:0.6">来源：财联社、AA新闻、华尔街见闻</em>""",
            },
            {
                "title": "☁️ AWS容量2027年底前基本售罄 AI基础设施需求远超预期",
                "content": """亚马逊CEO安迪·贾西周五释放重磅信号，云计算需求持续爆发：
<br><strong>核心信息：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>AWS的云计算容量在<strong>2027年底前已基本售罄</strong>，大量订单已排至2028年</li>
<li>受人工智能基础设施需求不断增长的影响，需求远超市场预期</li>
<li>亚马逊正在努力快速扩展基础设施，以满足AI实验室和企业源源不断的需求</li>
</ul>
<strong>市场意义：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li><strong>直接驳斥AI泡沫论：</strong>云厂商容量售罄说明AI需求真实存在且持续增长</li>
<li><strong>上游全产业链受益：</strong>芯片、存储、光模块、液冷、电力等基础设施需求确定性极高</li>
<li><strong>供给约束成瓶颈：</strong>算力供给无法满足需求，算力价格有支撑，相关企业业绩有保障</li>
</ul>
<strong>对A股的映射：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>英维克（液冷）：算力扩张直接受益，液冷是高密度算力中心刚需</li>
<li>铜冠铜箔：AI服务器PCB铜箔需求随算力扩张持续增长</li>
<li>雅克科技：半导体材料需求随晶圆厂扩产而增长</li>
<li>光通信/光模块：算力互联需求持续爆发</li>
</ul>
<em style="opacity:0.6">来源：中证报、华尔街见闻</em>""",
            },
            {
                "title": "📡 SpaceX进军电信市场 美国三大运营商股价集体暴跌",
                "content": """SpaceX计划在美国各地获取至少8万个通信基站，引发电信板块地震：
<br><strong>电信股暴跌：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>AT&T 暴跌 <strong style="color:#ef4444;">7.96%</strong></li>
<li>T-Mobile 暴跌 <strong style="color:#ef4444;">7.71%</strong></li>
<li>Verizon 下跌 1.18%</li>
<li>SpaceX 上涨 1.89%（逆势上涨）</li>
<li>铁塔运营商反而受益：Crown Castle涨8.6%、American Tower涨6.1%</li>
</ul>
<strong>事件背景：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>消息称SpaceX正与蜂窝基础设施公司谈判，计划在美国建立全国性无线网络</li>
<li>SpaceX旗下星链已拥有超千万用户，正在从卫星通信向地面通信延伸</li>
<li>传统电信运营商面临颠覆性竞争压力，估值逻辑被重估</li>
</ul>
<em style="opacity:0.6">来源：财联社、AA新闻</em>""",
            },
        ], cols=1)
    },
]

news_html = gen.create_tab_pane(news_tabs, tab_id="daily-news")
gen.add_section("重大新闻", news_html, icon="📰")
print("Step 3 news tab 1 done")

# 国内要闻tab
domestic_tab = {
    "label": "国内要闻",
    "content": gen.create_card_group([
        {
            "title": "🏛️ 二十届五中全会今日召开 聚焦'十五五'规划与高质量发展",
            "content": """中国共产党第二十届中央委员会第五次全体会议今日至29日在北京召开：
<br><strong>会议核心议题：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>审议《中共中央关于制定国民经济和社会发展第十五个五年规划的建议》</li>
<li>研究部署'十五五'时期经济社会发展目标任务</li>
<li>聚焦高质量发展、新质生产力、科技创新等核心方向</li>
<li>深化改革扩大开放，推进中国式现代化建设</li>
</ul>
<strong>市场预期：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li><strong>科技自立自强：</strong>半导体、人工智能、先进制造等战略新兴产业有望获得更多政策支持</li>
<li><strong>扩大内需：</strong>消费、基建投资等稳增长措施预期加强</li>
<li><strong>绿色转型：</strong>新能源、碳中和相关产业持续受益</li>
<li>会议期间通常政策面偏暖，对市场情绪有正面支撑作用</li>
</ul>
<strong>对持仓的意义：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>英维克：绿色算力、算电协同是政策重点支持方向</li>
<li>雅克科技：半导体材料国产化属于科技自立自强核心领域</li>
<li>铜冠铜箔：高端铜箔进口替代符合产业升级方向</li>
</ul>
<em style="opacity:0.6">来源：新华社、第一财经</em>""",
        },
        {
            "title": "📊 存储芯片Q3业绩大爆发 德明利净利同比增2903%",
            "content": """多家科技公司发布三季度业绩，存储芯片板块业绩炸裂：
<br><strong>核心公司业绩：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li><strong>德明利(001309)：</strong>Q3净利润同比增长<strong style="color:#22c55e;">2903%</strong>，环比增长2%，存储超级周期持续兑现</li>
<li><strong>天齐锂业(002466)：</strong>Q3净利润同比增长<strong style="color:#22c55e;">1324%</strong>，环比下降42%</li>
<li><strong>寒武纪(688256)：</strong>Q3净利润同比增长<strong style="color:#22c55e;">148%</strong>，环比增长8%</li>
<li><strong>光迅科技(002281)：</strong>Q3净利润同比增长<strong style="color:#22c55e;">103%</strong>，光通信景气度高</li>
<li><strong>华盛锂电：</strong>Q3净利润同比增长801%，环比增长148%</li>
<li><strong>紫金矿业：</strong>Q3净利润同比增长25.97%</li>
</ul>
<strong>行业趋势：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>存储芯片从价格上涨阶段进入业绩全面兑现阶段</li>
<li>AI算力、光通信、半导体设备等赛道业绩普遍超预期</li>
<li>上游材料和设备企业业绩弹性最大</li>
<li>野村证券：存储芯片短缺局面将持续至2028年，板块估值被严重低估</li>
</ul>
<strong>对持仓的意义：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>雅克科技：存储材料需求爆发，HBM前驱体+光刻胶双轮驱动</li>
<li>铜冠铜箔：AI服务器+存储扩产带动高端铜箔需求</li>
<li>英维克：算力中心建设加速，液冷散热需求持续增长</li>
</ul>
<em style="opacity:0.6">来源：公司公告、财联社、中国证券报</em>""",
        },
        {
            "title": "📈 A股指数编制方案修订今日实施 单一个股权重上限15%",
            "content": """上交所修订上证系列综合指数编制方案，今日起正式实施：
<br><strong>修订内容：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>增加<strong>单个样本权重不超过15%</strong>的权重上限规则</li>
<li>将风险警示证券剔除时间从"实施日次月第二个星期五的下一交易日"调整为"公告日次月第二个星期五的下一交易日"</li>
<li>涉及指数：上证指数、上证A股指数、上证流通指数、科创综指及衍生指数</li>
</ul>
<strong>市场影响：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li><strong>权重股影响：</strong>权重超过15%的大市值个股可能面临被动调仓减仓压力</li>
<li><strong>指数更均衡：</strong>降低单一个股对指数的影响，提升指数代表性和稳定性</li>
<li><strong>ST股风险：</strong>风险警示股剔除提前，减少ST股对指数的拖累</li>
</ul>
<strong>今日其他重要事件：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>央行开展7000亿元1年期MLF操作，保持银行体系流动性充裕</li>
<li>北交所无价格涨跌幅限制股票大宗交易价格新规实施</li>
<li>百度被纳入恒生港股通新经济指数等3只指数生效</li>
<li>CPE 2026国际算电展在上海举办（10/26-28）</li>
</ul>
<em style="opacity:0.6">来源：上交所、财联社、第一财经</em>""",
        },
        {
            "title": "🤖 国务院印发AI就业意见 国家信息化'十五五'规划发布",
            "content": """政策层面持续加码人工智能与数字经济：
<br><strong>国务院AI就业意见：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>印发《关于适应人工智能技术发展助力构建就业友好型发展方式的意见》</li>
<li>部署6个方面18项主要任务，强化AI就业创造效应</li>
<li>拓展新兴领域AI就业新空间，加快开发AI领域新职业</li>
<li>减缓AI应用就业替代影响，建立AI应用就业风险评估机制</li>
</ul>
<strong>国家信息化"十五五"规划：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>中央网信委印发《国家信息化"十五五"规划》</li>
<li>突破关键核心技术：做精做细芯片成熟制程，提高先进制程制造能力</li>
<li>推进存算一体、三维集成、光电融合等技术突破应用</li>
</ul>
<strong>国常会部署：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>李强主持召开国务院常务会议，部署人口高质量发展</li>
<li>加快建设生育友好型社会，完善婚嫁生育养育教育政策</li>
<li>稳定新出生人口规模，释放人口综合红利</li>
</ul>
<em style="opacity:0.6">来源：新华社、国务院办公厅、财联社</em>""",
        },
    ], cols=1)
}
news_tabs.append(domestic_tab)

# 持仓相关tab
holding_tab = {
    "label": "持仓相关",
    "content": gen.create_card_group([
        {
            "title": "❄️ 英维克：五中全会+算电展双重催化 液冷龙头蓄势待发",
            "content": """英维克(002837)最新动态：
<br><strong>近期催化：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li><strong>二十届五中全会：</strong>绿色算力、算电协同是"十五五"重点方向，政策面持续利好</li>
<li><strong>CPE 2026国际算电展：</strong>今日在上海举办，液冷散热是核心议题</li>
<li><strong>AWS容量售罄：</strong>全球算力需求爆发，液冷散热需求确定性极高</li>
<li>总书记此前考察乌兰察布算力网，强调绿色算力与算电协同</li>
</ul>
<strong>业绩关注：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>三季报披露日期：10月27日（周二）</li>
<li>市场预期液冷业务持续高增长，AI算力相关收入占比提升</li>
<li>近期中标多个大型数据中心液冷项目</li>
</ul>
<strong>操作建议：</strong>政策催化密集+业绩期临近，底仓坚定持有。若回调至40元以下可加仓机动仓位，止损位38元，上方压力位50元。
<br><br>
<em style="opacity:0.6">来源：财联社、公司公告</em>""",
        },
        {
            "title": "🟫 铜冠铜箔：存储业绩爆发验证需求 高端铜箔景气持续",
            "content": """铜冠铜箔(301217)最新动态：
<br><strong>行业景气验证：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>德明利Q3净利增29倍，存储超级周期业绩端全面兑现</li>
<li>AWS容量2027年底前售罄，AI服务器需求持续爆发</li>
<li>存储+AI服务器双轮驱动高端PCB铜箔需求结构性向好</li>
<li>野村证券：存储芯片短缺局面将持续至2028年</li>
</ul>
<strong>公司基本面：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>中报净利2.15亿同比增514%，盈利能力大幅改善</li>
<li>锂电铜箔+电子电路铜箔双轮驱动，高端产品占比提升</li>
<li>三季报披露日期：10月28日</li>
</ul>
<strong>操作建议：</strong>行业高景气度+业绩验证，回调即是加仓机会。底仓持有，若回调至80元附近可加仓，止损位75元，目标位看100元以上。
<br><br>
<em style="opacity:0.6">来源：公司公告、证券时报</em>""",
        },
        {
            "title": "🔬 雅克科技：存储材料需求爆发 三季报临近关注业绩兑现",
            "content": """雅克科技(002409)最新动态：
<br><strong>行业催化：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>存储芯片Q3业绩大爆发，德明利增29倍验证行业景气度</li>
<li>HBM需求持续爆发，带动前驱体+光刻胶需求增长</li>
<li>野村证券：存储短缺将持续至2028年，板块估值被严重低估</li>
<li>国家信息化"十五五"规划强调先进制程与材料突破</li>
</ul>
<strong>公司动态：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>子公司江苏雅睿增资近18亿布局光刻胶，加码半导体材料</li>
<li>中韩双基地扩产建设推进，新增产能预计明年年底前建成</li>
<li>韩国UP Chemical生产基地基本满产</li>
<li>三季报披露日期：10月28日</li>
</ul>
<strong>操作建议：</strong>存储材料龙头地位稳固，三季报有望验证业绩增长。底仓30%持有，若回调至90元以下可加仓，真正击球区85-90元，止损位80元。
<br><br>
<em style="opacity:0.6">来源：公司公告、财联社</em>""",
        },
        {
            "title": "🏗️ *ST建艺：重组预期+摘帽逻辑 独立行情不受外围影响",
            "content": """*ST建艺(002789)最新动态：
<br><strong>核心逻辑：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>ST摘帽预期+重组转型预期，独立于科技板块行情</li>
<li>外围科技股波动对其影响极小，可作为组合避险配置</li>
<li>建筑装饰主业稳定，科技转型预期提供想象空间</li>
</ul>
<strong>关注要点：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>三季报业绩进展，是否持续改善</li>
<li>摘帽进度与相关公告</li>
<li>新业务拓展与转型进展</li>
</ul>
<strong>操作建议：</strong>底仓持有，作为组合防御品种。ST股严格控制仓位比例，不超过总仓位10%，严格执行止损纪律。
<br><br>
<em style="opacity:0.6">来源：公司公告</em>""",
        },
    ], cols=1)
}
news_tabs.append(holding_tab)

# 重新构建完整tab（包含3个tab）
news_html_full = gen.create_tab_pane(news_tabs, tab_id="daily-news")
gen.add_section("重大新闻", news_html_full, icon="📰")

print("Step 3 tabs done")

# 4. 板块分析
gen.add_sector_analysis()

# 5. 今日催化剂
gen.add_today_catalysts()

# 6. 题材动态
gen.add_topic_dynamics()

# 7. 题材深度
gen.add_topic_deep_dive()

# 8. 韭研公社热点
gen.add_jiuyan_hot_topics()

# 9. 持仓跟踪
gen.add_holdings_tracking()

# 10. 明日预判
gen.add_tomorrow_prediction()

# 11. 风险预警
gen.add_risk_warning()

# 12. 空方视角
bear_case_html = '''
<div class="space-y-3">
    <div style="padding:12px 16px;background:rgba(239,68,68,0.1);border:1px solid rgba(239,68,68,0.3);border-radius:8px;">
        <strong style="color:#fca5a5;">⚠️ 空方核心论点：油价暴涨+美联储议息双重压力</strong>
        <p style="margin-top:6px;opacity:0.85;">布油突破117美元创5个月新高，通胀担忧重燃，美联储本周议息可能释放鹰派信号。美股科技股估值仍高，AI融资担忧尚未完全消化，外围风险继续压制A股科技板块。</p>
    </div>
    <div style="padding:12px 16px;background:rgba(251,191,36,0.1);border:1px solid rgba(251,191,36,0.3);border-radius:8px;">
        <strong style="color:#fcd34d;">⚡ 空方催化因素</strong>
        <ul style="margin-top:6px;padding-left:20px;opacity:0.85;">
            <li>油价暴涨推升通胀预期→美联储推迟降息→全球流动性收紧</li>
            <li>AI融资担忧持续，CoreWeave债务危机尚未解除</li>
            <li>高盛下调韩国Kospi目标25%，全球半导体估值下修</li>
            <li>A股指数权重新规实施，大权重股可能被动减仓</li>
            <li>中东地缘冲突持续升级，避险情绪升温</li>
        </ul>
    </div>
    <div style="padding:12px 16px;background:rgba(34,197,94,0.1);border:1px solid rgba(34,197,94,0.3);border-radius:8px;">
        <strong style="color:#86efac;">✅ 多方反驳论据</strong>
        <ul style="margin-top:6px;padding-left:20px;opacity:0.85;">
            <li>二十届五中全会召开，政策面偏暖，国内政策底明确</li>
            <li>AWS容量2027年底前售罄，AI需求真实性得到验证</li>
            <li>存储芯片Q3业绩大爆发，德明利增29倍，基本面强劲</li>
            <li>央行7000亿MLF操作，国内流动性充裕</li>
            <li>上周五A股探底回升大逆转，宽基ETF成交历史天量，资金进场明显</li>
        </ul>
    </div>
    <p style="opacity:0.7;font-size:0.9rem;">💡 结论：外围压力犹存但国内政策与业绩双重支撑，A股有望走出独立行情。重点关注业绩确定性高的科技成长股，控制仓位、分批布局。</p>
</div>
'''
gen.add_section("空方视角", bear_case_html, icon="🐻", extra_class="bear-case")

# 13. 每日总结
gen.add_daily_summary()

# 发布
output_path = '/root/daily-news-insight/docs/daily/20261026_每日新闻洞察.html'
result = gen.publish(output_path)
print("发布结果:", result)
