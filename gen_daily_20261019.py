#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-19 每日新闻洞察 - V3 Pro生成器"""
import sys, os
sys.path.insert(0, 'v3')
os.chdir('/root/daily-news-insight')
from generators.daily_pro import DailyReportProGenerator

gen = DailyReportProGenerator(
    date_str="2026-10-19",
    weekday="周一",
    subtitle="SOX八连跌创2006年以来最长纪录存储单周重挫14-18% | CoreWeave股债双杀AI债务恐慌蔓延 | 总书记考察乌兰察布算力网前景广阔 | 德明利前三季净利暴增320倍",
    data_dir='/root/daily-news-insight/data'
)

# TL;DR
gen.set_tldr([
    ("美股半导体八连跌 存储板块重灾区", "SOX连续8日下跌创2006年以来最长连跌纪录，累计跌幅超15%市值蒸发2.3万亿美元，存储股单周重挫14-18%，CoreWeave债务危机引爆AI融资链条恐慌", "red"),
    ("总书记考察乌兰察布 算力网前景广阔", "习近平总书记10月16日考察内蒙古乌兰察布，强调算力网是国家六张网之一，算力产业正处在加速发展阶段，提出算电协同、算水协同两大要求", "green"),
    ("德明利前三季净利暴增320倍 存储业绩炸裂", "德明利前三季度归母净利润86.5-89.5亿元同比增32046%-33154%，企业级存储业务收入82.37亿元，存储超级周期业绩端持续兑现", "green"),
], operation_advice="外围半导体暴跌冲击不可避免，A股有政策底支撑，今日建议：仓位控制在4-5成，持仓标的逢高减仓机动仓位，核心底仓不动，等待情绪宣泄后的低吸机会", risk_level="高", suggested_position="4-5成")

gen.set_holdings([
    {"name": "英维克", "code": "002837"},
    {"name": "铜冠铜箔", "code": "301217"},
    {"name": "雅克科技", "code": "002409"},
    {"name": "*ST建艺", "code": "002789"},
])

gen.set_og(
    description="10月19日盘前必读：美股半导体八连跌创20年最长纪录，CoreWeave债务危机引爆AI恐慌；总书记考察算力网强调算电协同；德明利前三季净利暴增320倍存储业绩炸裂",
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
                "title": "📉 费城半导体八连跌创2006年以来最长纪录 累计跌超15%蒸发2.3万亿",
                "content": """美股半导体板块遭遇历史性抛售，费城半导体指数(SOX)连续第8个交易日收跌：
<br><strong>收盘数据：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>费城半导体指数 <strong style="color:#ef4444;">-3.83%</strong> 报11137.29点</li>
<li>创2006年5月以来最长连跌纪录（SOXX ETF九连跌）</li>
<li>10月7日高点以来累计跌幅超<strong style="color:#ef4444;">15%</strong>，市值蒸发近2.3万亿美元</li>
<li>做空者7个交易日账面获利约320亿美元（约2140亿元人民币）</li>
</ul>
<strong>成分股全线下跌：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>COHERENT -7.04%、ARM -6.94%、TOWER半导体 -6.78%</li>
<li>AMD -5.95%、英特尔 -5.79%、美光 -5.63%、迈威尔 -5%+</li>
<li>应用材料 -4.82%、博通 -4.52%、格芯 -4%+、拉姆研究 -4%+</li>
<li>英伟达 -1.43%、阿斯麦 -0.96%、台积电ADR -2.28%</li>
</ul>
<strong>下跌三重导火索：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li><strong>通胀超预期：</strong>9月CPI反弹推升加息预期，10年期美债收益率走高</li>
<li><strong>AI债务危机：</strong>CoreWeave股债双杀，520亿美元债务规模引发市场对AI资本开支可持续性的深度质疑</li>
<li><strong>获利回吐：</strong>3月底至6月SOX翻倍涨6.5万亿，高位获利盘集中出逃</li>
</ul>
<strong>估值视角：</strong>摩根士丹利数据显示SOX远期市盈率从高点回调约40%至20.2倍，距上一轮周期低点仅剩约8%空间。
<br><br>
<em style="opacity:0.6">来源：彭博社、S3 Partners、证券时报、新浪财经</em>""",
            },
            {
                "title": "💥 CoreWeave股债双杀 520亿债务引爆AI融资链条恐慌",
                "content": """AI算力租赁公司CoreWeave成为本轮科技股抛售的风暴眼：
<br><strong>市场表现：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>单周重挫<strong style="color:#ef4444;">25.21%</strong>，较年内高点累计跌超60%</li>
<li>无担保债券收益率飙升至<strong style="color:#ef4444;">15%</strong>，落入高风险垃圾债区间</li>
<li>五年期CDS利差突破1000个基点，市场预测五年内违约概率超60%</li>
<li>做空者按市值计价账面利润超10亿美元</li>
</ul>
<strong>债务规模惊人：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>截至6月30日总债务超<strong>510-520亿美元</strong>，一年前仅约150亿美元</li>
<li>年度资本支出预测上调至最高390亿美元，现金消耗速度远超市场容忍度</li>
<li>2025年营收51亿美元、净亏损12亿美元，烧钱模式不可持续</li>
<li>创始人已减持套现约33亿美元，市场信心进一步受挫</li>
</ul>
<strong>传导链条：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li><strong>芯片股：</strong>英伟达最直接客户之一，AI资本开支预期被重新定价</li>
<li><strong>云厂商：</strong>Nebius跌10%、甲骨文跌8.8%，云算力板块集体承压</li>
<li><strong>韩股联动：</strong>韩国KOSPI上周暴跌7.6%，三星跌9.5%SK海力士跌11%</li>
<li><strong>信贷市场：</strong>高收益债平均收益率升至8.41%，为近18个月高位</li>
</ul>
<strong>机构观点：</strong>9fin称CoreWeave是AI信贷市场的矿井里的金丝雀，将成为AI热潮融资定价的转折点。
<br><br>
<em style="opacity:0.6">来源：36氪、华尔街见闻、新浪财经</em>""",
            },
            {
                "title": "💾 存储板块单周重挫14-18% 成为本轮暴跌重灾区",
                "content": """存储芯片板块跌幅居半导体各子板块之首，闪迪/西数/美光集体暴跌：
<br><strong>单周跌幅榜：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>闪迪(SNDK) <strong style="color:#ef4444;">-17.86%</strong></li>
<li>西部数据(WDC) <strong style="color:#ef4444;">-16.43%</strong></li>
<li>美光科技(MU) <strong style="color:#ef4444;">-14.59%</strong>（周五单跌5.63%）</li>
<li>希捷科技(STX) 周五跌7.50%</li>
<li>SK海力士 单周跌9.25%（周五反弹0.79%）</li>
</ul>
<strong>存储基本面对冲因素：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li><strong>业绩端强韧：</strong>SK海力士Q3营业利润率78.4%创历史新高，韩副总理称存储繁荣至少持续到2027年</li>
<li><strong>A股存储爆发：</strong>德明利前三季净利86.5-89.5亿增320倍，长鑫科技前三季营收2650-2700亿</li>
<li><strong>供需格局：</strong>HBM3E/HBM4供不应求格局未变，AI服务器渗透率持续提升</li>
</ul>
<strong>关键判断：</strong>本轮存储股下跌是估值回调而非基本面反转，存储超级周期的产业逻辑（AI驱动+HBM供需缺口）依然成立，但短期情绪面宣泄可能持续1-2周。
<br><strong>对A股影响：</strong>存储板块开盘承压在所难免，但国内存储公司业绩已进入爆发期，国产替代+业绩双重支撑下回调空间有限，关注错杀机会。
<br><br>
<em style="opacity:0.6">来源：彭博社、东方财富、公司公告</em>""",
            },
            {
                "title": "🌍 美股三大指数集体收跌 纳指重挫2.15% VIX飙升34.7%",
                "content": """多重利空共振下美股全线收跌，纳指创7月以来最大单周跌幅：
<br><strong>收盘数据：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>道琼斯 <strong style="color:#ef4444;">-0.34%</strong> 报52002.41点</li>
<li>标普500 <strong style="color:#ef4444;">-1.09%</strong> 报7659.44点</li>
<li>纳斯达克 <strong style="color:#ef4444;">-2.15%</strong> 报26140.03点（跌573点）</li>
<li>费城半导体 <strong style="color:#ef4444;">-3.83%</strong></li>
</ul>
<strong>科技七巨头分化：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>苹果 <strong style="color:#22c55e;">+0.43%</strong>（逆势上涨，防御属性凸显）</li>
<li>英伟达 -1.43%、微软 -1.93%、亚马逊 -1.87%</li>
<li>Meta -3.72%、谷歌 -2.32%、特斯拉 -2.13%</li>
</ul>
<strong>市场情绪指标：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>VIX波动率指数单周累涨<strong style="color:#ef4444;">34.7%</strong>至19.99，接近担忧临界点</li>
<li>纳指100录得2025年4月以来最差单周表现，跌幅5.5%</li>
<li>苹果市值首次突破5万亿美元，成为继英伟达后第二家5万亿公司</li>
</ul>
<strong>大宗商品：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>WTI原油 -1.50% 报97.53美元，布伦特 -1.70% 报108.00美元</li>
<li>COMEX黄金 <strong style="color:#22c55e;">+0.49%</strong> 报4201.68美元（避险需求支撑）</li>
<li>COMEX白银 +0.29% 报57.47美元</li>
</ul>
<em style="opacity:0.6">来源：新浪财经、财联社、东方财富</em>""",
            },
            {
                "title": "🇰🇷 韩国市场反弹 三星+2.62%SK海力士+0.79% 现代汽车+5.58%",
                "content": """经历上周黑色星期四后，韩国市场周五迎来反弹修复：
<br><strong>KOSPI反弹：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>周四KOSPI暴跌7.57%，创2008年金融危机以来最大单日跌幅</li>
<li>交易所启动SIDECAR机制暂停程序化卖盘</li>
<li>周五震荡反弹，半导体板块分化，汽车股领涨</li>
</ul>
<strong>核心标的表现：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>三星电子 <strong style="color:#22c55e;">+2.62%</strong> 报215500韩元</li>
<li>SK海力士 <strong style="color:#22c55e;">+0.79%</strong> 报1272000韩元（单周仍跌9.25%）</li>
<li>现代汽车 <strong style="color:#22c55e;">+5.58%</strong>、起亚 +4.06%（汽车出口强劲）</li>
<li>NAVER +3.69%、Kakao +2.74%（互联网板块反弹）</li>
<li>三星SDI -1.85%、SK Innovation -1.94%（电池板块继续承压）</li>
</ul>
<strong>政策回应：</strong>韩国政府紧急召开宏观经济金融会议，副总理称将采取一切必要措施稳定市场，韩国央行也表示准备好注入流动性。
<br><br>
<em style="opacity:0.6">来源：财联社、韩联社</em>""",
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
            "title": "🎯 总书记考察乌兰察布 算力网是国家六张网之一前景广阔",
            "content": """习近平总书记10月16日在内蒙古自治区乌兰察布市考察，重点调研绿色算力产业：
<br><strong>核心讲话：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>算力网是国家规划建设的六张网之一，算力产业正处在加速发展阶段，<strong style="color:#22c55e;">前景广阔</strong></li>
<li>认真落实<strong>高效、绿色、安全</strong>的要求</li>
<li>注重算电协同、算水协同两条绿色底线</li>
<li>不断把算力优势转化为发展优势</li>
<li>积极推动绿色算力产业发展，为推进数字中国建设、促进新质生产力发展多作贡献</li>
</ul>
<strong>乌兰察布算力现状：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>国家八大算力枢纽节点、十大数据中心集群之一</li>
<li>已签约数据中心项目超百个，投运算力<strong>17.2万P</strong>，同比增长112%</li>
<li>智能算力占比超95%，被称为一座因凉而热的城市</li>
<li>依托冷凉气候、稳定地质、绿电占比高、近京低时延等优势</li>
</ul>
<strong>战略背景：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>今年4月中央政治局会议提出加强六张网规划建设，算力网纳入国家顶层设计</li>
<li>中共中央、国务院印发《关于发展新质生产力的意见》，部署建设全国一体化算力网</li>
<li>十五五开局起步的重要落子，从东数西算工程到全国一体化算力网升级</li>
</ul>
<strong>对持仓的意义：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>英维克（液冷散热）：直接受益于算力中心建设+绿色算力要求，算电协同和液冷是核心方向</li>
<li>雅克科技（半导体材料）：算力芯片需求增长带动上游材料景气度</li>
<li>铜冠铜箔（PCB/锂电铜箔）：算力基础设施建设带动PCB铜箔需求</li>
</ul>
<em style="opacity:0.6">来源：人民网、央视网、中国经济网</em>""",
        },
        {
            "title": "💰 德明利前三季净利暴增320倍 存储超级周期业绩端持续兑现",
            "content": """德明利(001309)发布2026年前三季度业绩预告，存储板块业绩持续爆发：
<br><strong>核心数据：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>营业收入 <strong>275-295亿元</strong>，同比增长<strong style="color:#22c55e;">312.97%-343.00%</strong>（约3倍）</li>
<li>归母净利润 <strong style="color:#22c55e;">86.5-89.5亿元</strong>，同比增长<strong style="color:#22c55e;">32046.52%-33154.49%</strong>（约320倍）</li>
<li>上年同期亏损2707.65万元，成功扭亏为盈</li>
<li>扣非净利润85.96-88.96亿元，同比增长约17128%-17722%</li>
<li>Q3单季净利润26.33-29.33亿元，环比持续增长</li>
</ul>
<strong>业绩驱动：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li><strong>企业级存储爆发：</strong>前三季企业级存储业务收入82.37亿元，收入规模及占比提升</li>
<li>企业级自研主控芯片+全谱系产品矩阵，已进入国内头部云服务商供应链</li>
<li>越南生产基地量产交付，全球化业务拓展加速</li>
<li>股份支付费用约2.81亿元（上年同期3941万元），剔除后利润更高</li>
</ul>
<strong>行业全景：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>长鑫科技：前三季营收2650-2700亿（+727%-743%），净利1310-1325亿</li>
<li>江波龙、佰维存储等存储公司前三季业绩普遍大幅预喜</li>
<li>存储超级周期从价格上涨阶段进入业绩兑现阶段</li>
</ul>
<strong>对持仓的意义：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>雅克科技：存储材料直接受益于存储晶圆厂扩产和HBM需求爆发</li>
<li>铜冠铜箔：PCB铜箔需求随AI服务器和存储产业链扩张而增长</li>
</ul>
<em style="opacity:0.6">来源：公司公告、中国证券报、证券时报</em>""",
        },
        {
            "title": "📢 国常会深化人工智能+行动 夯实算力底座",
            "content": """国务院总理李强10月16日主持召开国务院常务会议，聚焦人工智能发展：
<br><strong>核心部署：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>人工智能是影响未来发展的关键变量，要深化拓展人工智能+行动</li>
<li><strong>夯实发展底座：</strong>加强技术攻关和算法创新，促进算电协同，增加高质量数据供给</li>
<li><strong>突出赋能应用：</strong>以实体经济为重点强化供需衔接，鼓励联合研发，推进中试验证</li>
<li><strong>统筹发展和安全：</strong>因业分级分类施策，加强风险研判评估，守牢安全底线</li>
</ul>
<strong>商务部+科技部：AI技术出口管制</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>拟修订《中国禁止出口限制出口技术目录》</li>
<li>增列人工智能、生物医药、光伏三个领域共40项技术</li>
<li>AI领域包括大模型、智能体、算力集群、信息处理相关23项技术</li>
<li>已开源/公开发表的技术不纳入管理范围</li>
</ul>
<strong>今日重点事件：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li><strong>10:00</strong> 国新办举行2026年前三季度国民经济运行情况新闻发布会</li>
<li><strong>金融街论坛年会</strong>：10/19-22在北京举办，央行行长潘功胜、证监会主席吴清将出席演讲</li>
<li><strong>港股休市</strong>：重阳节假期，南北向交易关闭</li>
<li><strong>国家统计局</strong>：公布70个大中城市住宅销售价格月度报告</li>
</ul>
<em style="opacity:0.6">来源：新华社、财联社、第一财经</em>""",
        },
        {
            "title": "📈 A股分红回购增持热潮 年内现金分红超2万亿",
            "content": """上市公司投资者回报持续增强，监管引导提高上市公司质量：
<br><strong>分红回购数据：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>已有<strong>3734家</strong>A股上市公司实施分红</li>
<li>现金分红总额超<strong>2万亿元</strong></li>
<li>回购增持动作密集，回馈投资者意识显著增强</li>
</ul>
<strong>监管导向：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>监管部门明确将引导上市公司通过股权激励、分红回购等提高自身价值</li>
<li>大力督促引导上市公司强化投资者回报意识</li>
<li>增强投资者回报的持续性、及时性和可预期性</li>
</ul>
<strong>其他公司动态：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>博盈特焊：筹划重大资产重组，10月19日起停牌</li>
<li>盛和资源：拟向中稀发展转让4家稀土冶炼分离子公司51%股权</li>
<li>ST绝味：10月20日起撤销其他风险警示，简称变更为绝味食品</li>
<li>恒力石化：前三季净利预增104.2%至102.56亿元</li>
<li>国投中鲁：证券简称变更为国投电子</li>
</ul>
<em style="opacity:0.6">来源：财联社、中国证券报</em>""",
        },
    ], cols=1)
}
news_tabs.append(domestic_tab)

# 持仓相关tab
holding_tab = {
    "label": "持仓相关",
    "content": gen.create_card_group([
        {
            "title": "❄️ 英维克：液冷龙头受益算力网建设 融资余额持续回落",
            "content": """英维克(002837)最新动态：
<br><strong>股价与估值：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>10月16日收盘价 <strong>44.70元</strong>（+0.07%），总市值571.64亿元</li>
<li>动态市盈率154.69倍，市净率15.95倍</li>
<li>三季度北向资金持股下降28.44%，外资持续减仓</li>
</ul>
<strong>融资融券：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>融资余额持续回落：10月15日36.23亿，较前期高位显著下降</li>
<li>融资余额占流通市值比例7.15%，处于近一年70%分位水平</li>
<li>连续多日融资净偿还，杠杆资金撤退明显</li>
</ul>
<strong>近期利好：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>总书记考察算力网，强调算电协同、绿色算力，液冷是核心配套</li>
<li>参与湾区算电协同创新联合体</li>
<li>推出覆盖全链路的液冷解决方案及全场景撬块数据中心解决方案</li>
<li>股票期权激励计划首次授予完成，765名激励对象绑定利益</li>
<li>近期中标：中车株洲冷机项目、中国移动长三角科创中心液冷CDU项目等</li>
</ul>
<strong>关键日期：</strong>10月27日披露三季报
<br><strong>操作建议：</strong>外围半导体暴跌+融资盘撤离短期承压，但算力网政策利好提供支撑。底仓持有，机动仓位逢低可小幅加仓但控制节奏，止损位40元。
<br><br>
<em style="opacity:0.6">来源：财联社、东方财富、企查查</em>""",
        },
        {
            "title": "🟫 铜冠铜箔：铜箔赛道高景气验证 短期资金流出承压",
            "content": """铜冠铜箔(301217)最新动态：
<br><strong>股价与估值：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>10月16日收盘价 <strong>85.42元</strong>（-4.29%），总市值708.15亿元</li>
<li>动态市盈率164.78倍，市净率12.62倍</li>
<li>当日主力资金净卖出7525.53万元，10月15日净卖出1.18亿元</li>
<li>本周（10.12-10.16）累计跌4.97%，主力资金净流出4.31亿元</li>
</ul>
<strong>行业景气验证：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>嘉元科技前三季净利预增12倍（5.3-5.8亿），铜箔需求景气度持续验证</li>
<li>德明利存储业绩暴增320倍，AI存储需求带动PCB铜箔量价齐升</li>
<li>存储超级周期+AI服务器双轮驱动，高端铜箔需求结构性向好</li>
</ul>
<strong>公司基本面：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>中报净利2.15亿同比增514%，盈利能力大幅改善</li>
<li>锂电铜箔+电子电路铜箔双轮驱动</li>
<li>9月接待2家机构调研</li>
<li>股东户数15.86万户，较前期增加（筹码分散）</li>
</ul>
<strong>关键日期：</strong>10月28日披露三季报
<br><strong>操作建议：</strong>短期受外围情绪+资金流出双重承压，但铜箔行业高景气度逻辑不变。底仓持有，若跌破80元可考虑加仓，止损位75元。
<br><br>
<em style="opacity:0.6">来源：证券之星、东方财富、新浪财经</em>""",
        },
        {
            "title": "🔬 雅克科技：子公司增资近18亿布局光刻胶 本周跌12.55%",
            "content": """雅克科技(002409)最新动态：
<br><strong>股价与表现：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>10月16日收盘价 <strong>98.01元</strong>（-1.00%），总市值466.46亿元</li>
<li>本周（10.12-10.16）累计跌<strong style="color:#ef4444;">12.55%</strong></li>
<li>主力资金单周净流出2.36亿元</li>
<li>市盈率(TTM)44.92倍，市净率5.83倍</li>
</ul>
<strong>重大事项：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li><strong>子公司增资：</strong>拟与投资人共同对江苏雅睿增资不超17.89亿元，布局半导体光刻胶</li>
<li>大基金管理机构任职的董事投弃权票，认为定价低于估值</li>
<li>增资价格引发市场对估值的讨论，是近期下跌因素之一</li>
</ul>
<strong>产能进展：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>中韩双基地扩产建设推进，新增产能预计明年年底前建成</li>
<li>韩国UP Chemical生产基地基本满产，江苏先科暂未满产</li>
<li>部分前驱体业务已由韩国转移至江苏先科</li>
</ul>
<strong>存储材料逻辑：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>存储超级周期下，HBM需求爆发带动前驱体+光刻胶需求</li>
<li>德明利/长鑫科技业绩验证存储景气度，上游材料长期受益</li>
<li>外围存储股暴跌短期情绪冲击，但国内存储产业链独立景气</li>
</ul>
<strong>关键日期：</strong>10月28日披露三季报
<br><strong>操作建议：</strong>本周已跌12.55%，短期跌幅较大有反弹需求，但外围风险未解除。底仓30%持有，反弹至105-110元可减仓机动仓位，真正击球区85-90元。
<br><br>
<em style="opacity:0.6">来源：证券之星、东方财富、企查查</em>""",
        },
        {
            "title": "🏗️ *ST建艺：装修装饰+重组预期 独立行情不受外围影响",
            "content": """*ST建艺(002789)最新动态：
<br><strong>核心逻辑：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>ST摘帽预期+重组转型预期，独立于科技板块行情</li>
<li>外围科技股暴跌对其影响极小，甚至可能成为避险资金选择</li>
<li>建筑装饰主业+科技转型双轮驱动</li>
</ul>
<strong>关注要点：</strong>
<ul style="margin:8px 0;padding-left:20px;">
<li>三季报业绩进展，是否持续改善</li>
<li>摘帽进度与相关公告</li>
<li>新业务拓展与转型进展</li>
</ul>
<strong>操作建议：</strong>底仓持有，不受外围科技股波动影响。ST股严格控制仓位比例，不超过总仓位10%。
<br><br>
<em style="opacity:0.6">来源：公司公告</em>""",
        },
    ], cols=1)
}
news_tabs.append(holding_tab)

# 重新构建tab pane（因为追加了新tab）
news_html = gen.create_tab_pane(news_tabs, tab_id="daily-news")
# 替换之前的重大新闻section（通过重新添加）
# 这里直接追加新的，之前那个保留也没关系
print("Step 3 additional tabs done")

# 重新构建完整tab（包含3个tab）
news_html_full = gen.create_tab_pane(news_tabs, tab_id="daily-news")
gen.add_section("重大新闻", news_html_full, icon="📰")

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
        <strong style="color:#fca5a5;">⚠️ 空方核心论点：AI泡沫破裂进行时</strong>
        <p style="margin-top:6px;opacity:0.85;">CoreWeave债务危机只是开始，AI资本开支建立在债务融资基础上，一旦融资成本上升，整个产业链都会受到冲击。存储股高位获利盘巨大，A股存储板块估值偏高，有补跌需求。</p>
    </div>
    <div style="padding:12px 16px;background:rgba(251,191,36,0.1);border:1px solid rgba(251,191,36,0.3);border-radius:8px;">
        <strong style="color:#fcd34d;">⚡ 空方催化因素</strong>
        <ul style="margin-top:6px;padding-left:20px;opacity:0.85;">
            <li>美国通胀反弹→加息预期升温→全球科技股估值杀</li>
            <li>CoreWeave违约风险上升→AI资本开支预期下修→芯片需求减少</li>
            <li>韩股暴跌引发全球半导体恐慌蔓延</li>
            <li>A股科技股估值偏高，有补跌空间</li>
            <li>融资盘高位撤离，流动性压力显现</li>
        </ul>
    </div>
    <div style="padding:12px 16px;background:rgba(34,197,94,0.1);border:1px solid rgba(34,197,94,0.3);border-radius:8px;">
        <strong style="color:#86efac;">✅ 多方反驳论据</strong>
        <ul style="margin-top:6px;padding-left:20px;opacity:0.85;">
            <li>总书记考察算力网，国内政策底明确，算力建设加速</li>
            <li>存储基本面强劲：德明利增320倍、长鑫科技增700%+</li>
            <li>SK海力士Q3利润率78.4%，韩副总理称繁荣至少到2027年</li>
            <li>A股半导体估值已部分回调，国产替代逻辑独立</li>
            <li>国内货币政策宽松，流动性充裕</li>
        </ul>
    </div>
    <p style="opacity:0.7;font-size:0.9rem;">💡 结论：短期情绪面冲击不可避免，但中长期产业逻辑未变。操作上控制仓位、分批建仓、严格止损是应对之道。</p>
</div>
'''
gen.add_section("空方视角", bear_case_html, icon="🐻", extra_class="bear-case")

# 13. 每日总结
gen.add_daily_summary()

# 发布
output_path = '/root/daily-news-insight/docs/daily/20261019_每日新闻洞察.html'
result = gen.publish(output_path)
print("发布结果:", result)
