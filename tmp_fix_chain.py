#!/usr/bin/env python3
"""修复产业链分析并重新生成"""
import sys, os
sys.path.insert(0, 'v3')
os.chdir('/root/daily-news-insight')

from v3.generators.s_level_catalyst import SLevelCatalystGenerator
from components.data import StockTags
from components.layout import Section as LayoutSection

gen = SLevelCatalystGenerator(
    date_str="20260911",
    catalyst_title="CPI前夜全球风险重估 + 甲骨文财报验证AI算力超预期",
    subtitle="2026.09.11 · 盘后S级催化扫描"
)

# 1. 催化事件概述
gen.add_catalyst_overview(
    overview="9月11日盘后全球资本市场呈现\"风险重估+AI算力独立走强\"双重格局：A股三大指数集体收跌（沪指-1.18%/深成指-1.08%/创业板-0.49%），成交额1.97万亿放量，全市场超4800只个股下跌，军工/光通信逆市走强。盘后核心催化密集：①甲骨文Q1财报炸裂（营收同比+30%、AI云收入+121%、RPO飙至6640亿美元），AI算力需求再获验证；②美国8月CPI今晚20:30公布，市场预期核心CPI环比+0.2%同比+2.4%，整体CPI环比+0.3%同比+3.4%，美联储9月加息概率71.3%；③中东局势出现降温信号（胡塞宣布红海停火、特朗普称中期选举后结束战事），油价从109美元大幅回落至99美元；④FCC光通信新规靴子落地，中际旭创等未被纳入限制名单；⑤燧原科技科创板上市首日+179%，国产AI芯片情绪高燃。<br><br><b>评级：S级</b>。AI算力链获得双重验证（甲骨文财报+FCC靴子落地），CPI+中东局势构成周末关键变量，持仓4只标的全部跟随调整，无个股性利空。",
    importance="极高"
)

# 2. 催化事件详解
gen.add_catalyst_details(
    background="<b>【宏观背景】</b>2026年9月全球资本市场处于\"高通胀+高利率+地缘冲突\"三重压力下：10年期美债收益率逼近5%关口、WTI油价一度突破103美元/桶、美联储9月加息概率从35%飙升至71.3%。A股本周呈现\"科技强周期弱\"结构性分化，光模块/PCB主力大幅净流入（中际旭创本周+105亿），有色金属/能源金属领跌。<br><br><b>【事件时间线】</b><br>· 9月10日美股四连跌，费城半导体-2.66%，SK海力士-5.2%，美光-4.9%<br>· 9月11日早间：亚太股市集体跳水，日经225大跌2.7%<br>· 9月11日午盘：A股放量下跌，沪指最低探至3852点<br>· 9月11日盘后：甲骨文财报炸裂，盘前大涨超5%，带动半导体板块反弹<br>· 9月11日20:30（北京时间）：美国8月CPI公布",
    trigger="<b>【核心催化1：甲骨文财报验证AI算力爆发】</b><br>甲骨文Q1营收193.5亿美元（+30%），云基础设施收入73.9亿美元（+121%），单季新增300亿美元AI云合同，RPO达6640亿美元。Q1交付850兆瓦AI算力（约30万+GPU），几乎相当于上一财年总量的73%，GPU续约溢价20%。AI算力需求正从\"预期\"加速进入\"兑现期\"。<br><br><b>【核心催化2：FCC靴子落地，光通信利空出尽】</b><br>美国FCC最终规则未将中际旭创、新易盛、东山精密等中国光通信企业纳入限制名单，此前市场担忧的\"出口管制升级\"风险解除。高盛上调2026-2028年全球光模块市场规模预测33%/81%/115%，2028年达1485亿美元。<br><br><b>【核心催化3：油价跳水+中东降温，CPI博弈加剧】</b><br>胡塞武装宣布红海西海岸停火+特朗普称中期选举后结束伊朗战事，布油从109美元跳水至99美元。油价回落若持续，将显著缓解通胀压力，但今晚CPI数据仍是决定性变量。"
)

# 3. 隔夜外盘跟踪
global_market_html = '''
<div class="grid md:grid-cols-2 lg:grid-cols-4 gap-3 mb-4">
    <div style="background: linear-gradient(135deg, rgba(239,68,68,0.15), rgba(239,68,68,0.05)); border-radius: 12px; padding: 16px; border: 1px solid rgba(239,68,68,0.25);">
        <div style="font-size: 12px; color: #fca5a5; margin-bottom: 4px;">纳斯达克综合</div>
        <div style="font-size: 20px; font-weight: 700; color: #f87171;">26,081.72</div>
        <div style="font-size: 13px; color: #f87171;">-0.65% / -171.62点</div>
        <div style="font-size: 11px; color: #94a3b8; margin-top: 4px;">9月10日收盘 连跌4日</div>
    </div>
    <div style="background: linear-gradient(135deg, rgba(239,68,68,0.15), rgba(239,68,68,0.05)); border-radius: 12px; padding: 16px; border: 1px solid rgba(239,68,68,0.25);">
        <div style="font-size: 12px; color: #fca5a5; margin-bottom: 4px;">费城半导体指数</div>
        <div style="font-size: 20px; font-weight: 700; color: #f87171;">-2.66%</div>
        <div style="font-size: 13px; color: #f87171;">存储芯片领跌</div>
        <div style="font-size: 11px; color: #94a3b8; margin-top: 4px;">SK海力士-5.2% 美光-4.9%</div>
    </div>
    <div style="background: linear-gradient(135deg, rgba(34,197,94,0.15), rgba(34,197,94,0.05)); border-radius: 12px; padding: 16px; border: 1px solid rgba(34,197,94,0.25);">
        <div style="font-size: 12px; color: #86efac; margin-bottom: 4px;">纳指100期货（盘前）</div>
        <div style="font-size: 20px; font-weight: 700; color: #4ade80;">+0.65%</div>
        <div style="font-size: 13px; color: #4ade80;">甲骨文财报带动反弹</div>
        <div style="font-size: 11px; color: #94a3b8; margin-top: 4px;">等待20:30 CPI数据</div>
    </div>
    <div style="background: linear-gradient(135deg, rgba(245,158,11,0.15), rgba(245,158,11,0.05)); border-radius: 12px; padding: 16px; border: 1px solid rgba(245,158,11,0.25);">
        <div style="font-size: 12px; color: #fcd34d; margin-bottom: 4px;">布伦特原油</div>
        <div style="font-size: 20px; font-weight: 700; color: #fbbf24;">103.99美元</div>
        <div style="font-size: 13px; color: #fbbf24;">-3.38% 大幅回落</div>
        <div style="font-size: 11px; color: #94a3b8; margin-top: 4px;">中东局势降温信号</div>
    </div>
</div>

<div class="grid md:grid-cols-3 gap-3 mb-4">
    <div style="background: rgba(255,255,255,0.03); border-radius: 12px; padding: 16px; border: 1px solid rgba(255,255,255,0.08);">
        <div style="font-size: 14px; font-weight: 700; color: #e2e8f0; margin-bottom: 10px;">🇺🇸 核心半导体标的（隔夜收盘）</div>
        <div style="font-size: 13px; color: #cbd5e1; line-height: 2;">
            英伟达 <span style="color:#f87171;">-2.37%</span> · 
            AMD <span style="color:#f87171;">-3.36%</span> · 
            美光 <span style="color:#f87171;">-4.90%</span><br>
            SK海力士ADR <span style="color:#f87171;">-5.20%</span> · 
            西部数据 <span style="color:#f87171;">-4.43%</span> · 
            阿斯麦 <span style="color:#f87171;">-2.43%</span><br>
            台积电ADR <span style="color:#94a3b8;">盘前小幅上涨</span> · 
            博通 <span style="color:#94a3b8;">盘前微涨</span>
        </div>
    </div>
    <div style="background: rgba(255,255,255,0.03); border-radius: 12px; padding: 16px; border: 1px solid rgba(255,255,255,0.08);">
        <div style="font-size: 14px; font-weight: 700; color: #e2e8f0; margin-bottom: 10px;">📈 盘前动态（截至20:20）</div>
        <div style="font-size: 13px; color: #cbd5e1; line-height: 2;">
            甲骨文 <span style="color:#4ade80;">+5~7%</span> 财报炸裂<br>
            英伟达 <span style="color:#4ade80;">+0.6%</span> 修复性反弹<br>
            美光 <span style="color:#4ade80;">+0.8~1%</span> 超跌反弹<br>
            SK海力士 <span style="color:#4ade80;">+1%</span> 技术性修复<br>
            Adobe <span style="color:#f87171;">-4%</span> 指引偏弱
        </div>
    </div>
    <div style="background: rgba(255,255,255,0.03); border-radius: 12px; padding: 16px; border: 1px solid rgba(255,255,255,0.08);">
        <div style="font-size: 14px; font-weight: 700; color: #e2e8f0; margin-bottom: 10px;">🌏 亚太/欧洲动态</div>
        <div style="font-size: 13px; color: #cbd5e1; line-height: 2;">
            日经225 <span style="color:#f87171;">-2.7%（约1800点）</span><br>
            韩国KOSPI <span style="color:#f87171;">大幅下跌</span><br>
            台积电8月营收 <span style="color:#4ade80;">+53.3%（5148亿新台币）</span><br>
            欧洲主要指数 <span style="color:#4ade80;">普遍上涨</span><br>
            韩国KB证券：存储库存不到10天
        </div>
    </div>
</div>

<div style="background: linear-gradient(135deg, rgba(168,85,247,0.1), rgba(139,92,246,0.05)); border-radius: 12px; padding: 16px; border: 1px solid rgba(168,85,247,0.3);">
    <div style="font-size: 14px; font-weight: 700; color: #c4b5fd; margin-bottom: 8px;">🔑 隔夜外盘核心结论</div>
    <div style="font-size: 13px; color: #cbd5e1; line-height: 1.9;">
        ① <b>情绪拐点：</b>美股连跌4日后盘前反弹，甲骨文财报是核心催化剂，验证AI算力需求依然旺盛，存储/半导体链获支撑；<br>
        ② <b>通胀博弈：</b>8月CPI数据今晚8:30公布，核心CPI环比+0.2%符合预期则加息概率回落，超预期则10年期美债或破5%；<br>
        ③ <b>油价风险释放：</b>中东局势出现降温信号，油价单日跳水超3%，短期缓解通胀压力但不确定性极高（停火真伪待确认）；<br>
        ④ <b>下周A股映射：</b>若CPI符合预期+甲骨文带动纳指反弹，则科技成长（光模块/AI算力/存储）有望率先修复；若CPI超预期，则全球风险资产继续承压。
    </div>
</div>
'''

gen._components.append(LayoutSection(title="🌍 隔夜外盘跟踪（V4.0强制）", content=global_market_html, icon="globe"))

# 4. 持仓个股分析
stocks_data = [
    {"code": "002837", "name": "英维克", "impact": "中性偏空"},
    {"code": "301217", "name": "铜冠铜箔", "impact": "中性"},
    {"code": "002409", "name": "雅克科技", "impact": "中性"},
    {"code": "002789", "name": "*ST建艺", "impact": "防御性"},
]

stock_tags_html = StockTags(stocks_data).render()

portfolio_html = f'''
<div style="margin-bottom: 16px;">
    <div style="font-size: 13px; color: #94a3b8; margin-bottom: 8px;">持仓标的影响评级</div>
    {stock_tags_html}
</div>

<div class="grid md:grid-cols-2 gap-3">
    <div style="background: rgba(255,255,255,0.03); border-radius: 12px; padding: 16px; border: 1px solid rgba(255,255,255,0.08);">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
            <span style="font-size: 15px; font-weight: 700; color: #e2e8f0;">英维克（002837）</span>
            <span style="font-size: 13px; color: #f87171;">-1.78% / 60.55元</span>
        </div>
        <div style="font-size: 12px; color: #94a3b8; margin-bottom: 6px;">成本：104.23元 | 深度套牢</div>
        <div style="font-size: 13px; color: #cbd5e1; line-height: 1.8;">
            <b>今日表现：</b>开61.08，最高61.81，最低59.80，收60.55，缩量调整。<br>
            <b>催化关联：</b>液冷板块跟随大盘调整，无个股性利空。甲骨文财报验证AI算力需求，液冷作为算力基础设施中长期逻辑不变。<br>
            <b>技术面：</b>60元整数关口附近震荡，50元为前期低点支撑。成交额13.27亿缩量，恐慌情绪有所缓解。<br>
            <b>双重验证：</b>✅ 无利空公告，无减持计划，9月10日推出股票期权激励计划（行权价46.73元），管理层对长期有信心。
        </div>
    </div>
    
    <div style="background: rgba(255,255,255,0.03); border-radius: 12px; padding: 16px; border: 1px solid rgba(255,255,255,0.08);">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
            <span style="font-size: 15px; font-weight: 700; color: #e2e8f0;">铜冠铜箔（301217）</span>
            <span style="font-size: 13px; color: #f87171;">-1.11% / 107.25元</span>
        </div>
        <div style="font-size: 12px; color: #94a3b8; margin-bottom: 6px;">AI铜箔+高速铜连接核心标的</div>
        <div style="font-size: 13px; color: #cbd5e1; line-height: 1.8;">
            <b>今日表现：</b>开105.52，最高108.72，最低101.55，收107.25，振幅7.07%。<br>
            <b>催化关联：</b>高速铜连接板块今日逆市活跃，铜冠铜箔盘中冲高后回落。调入深证成指+创业板指，指数型配置需求增加。<br>
            <b>技术面：</b>100元为近期支撑，110元为短期压力位。成交额31.73亿，换手率3.64%，筹码稳定。<br>
            <b>双重验证：</b>✅ 无利空公告，基本面正常。铜价短期波动影响有限，AI铜箔需求逻辑不变。
        </div>
    </div>
    
    <div style="background: rgba(255,255,255,0.03); border-radius: 12px; padding: 16px; border: 1px solid rgba(255,255,255,0.08);">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
            <span style="font-size: 15px; font-weight: 700; color: #e2e8f0;">雅克科技（002409）</span>
            <span style="font-size: 13px; color: #f87171;">-2.61% / 129.99元</span>
        </div>
        <div style="font-size: 12px; color: #94a3b8; margin-bottom: 6px;">半导体材料+HBM前驱体龙头</div>
        <div style="font-size: 13px; color: #cbd5e1; line-height: 1.8;">
            <b>今日表现：</b>开130.00，最高131.33，最低125.30，收129.99，振幅4.52%。<br>
            <b>催化关联：</b>半导体板块整体调整，雅克科技跟随下跌。但甲骨文财报+FCC落地对AI算力链是利好，HBM材料需求逻辑强化。<br>
            <b>技术面：</b>125元为短期支撑，135元为压力位。PE 55x（2026E），PB 7.73x，处于历史合理区间。<br>
            <b>双重验证：</b>✅ 无利空公告，无非正常减持。机构净卖出<成交额5%（未上龙虎榜），不构成看空信号。
        </div>
    </div>
    
    <div style="background: rgba(255,255,255,0.03); border-radius: 12px; padding: 16px; border: 1px solid rgba(255,255,255,0.08);">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
            <span style="font-size: 15px; font-weight: 700; color: #e2e8f0;">*ST建艺（002789）</span>
            <span style="font-size: 13px; color: #fbbf24;">防御性标的</span>
        </div>
        <div style="font-size: 12px; color: #94a3b8; margin-bottom: 6px;">组合对冲/防御仓</div>
        <div style="font-size: 13px; color: #cbd5e1; line-height: 1.8;">
            <b>今日表现：</b>ST板块整体波动，*ST建艺作为防御仓相对抗跌。<br>
            <b>催化关联：</b>与科技主线关联度低，作为组合对冲工具发挥作用。<br>
            <b>操作建议：</b>维持现有仓位，科技板块企稳前保留防御配置。<br>
            <b>双重验证：</b>✅ 无新增风险公告，ST状态为既知风险，无新增利空。
        </div>
    </div>
</div>
'''

gen._components.append(LayoutSection(title="💼 持仓个股分析（双重验证）", content=portfolio_html, icon="briefcase"))

# 5. 龙虎榜与资金面
longhubang_html = '''
<div class="grid md:grid-cols-2 gap-3 mb-4">
    <div style="background: linear-gradient(135deg, rgba(34,197,94,0.1), rgba(34,197,94,0.03)); border-radius: 12px; padding: 16px; border: 1px solid rgba(34,197,94,0.2);">
        <div style="font-size: 14px; font-weight: 700; color: #4ade80; margin-bottom: 10px;">📈 机构净买入TOP5（亿元）</div>
        <div style="font-size: 13px; color: #cbd5e1; line-height: 2;">
            1. 金安国纪 <span style="color:#4ade80;">+13.79亿</span> （+7.86%，电子布/PCB）<br>
            2. 博云新材 <span style="color:#4ade80;">+4.66亿</span> （+7.44%，军工/碳材料）<br>
            3. 长盈通 <span style="color:#4ade80;">+2.91亿</span> （+15.49%，光纤环/光通信）<br>
            4. 风华高科 <span style="color:#4ade80;">+1.83亿</span> （+10.00%，被动元件）<br>
            5. 嘉立创 <span style="color:#4ade80;">+1.14亿</span> （+10.00%，PCB/电子元器件）
        </div>
    </div>
    <div style="background: linear-gradient(135deg, rgba(239,68,68,0.1), rgba(239,68,68,0.03)); border-radius: 12px; padding: 16px; border: 1px solid rgba(239,68,68,0.2);">
        <div style="font-size: 14px; font-weight: 700; color: #f87171; margin-bottom: 10px;">📉 机构净卖出TOP5（亿元）</div>
        <div style="font-size: 13px; color: #cbd5e1; line-height: 2;">
            1. 逸豪新材 <span style="color:#f87171;">-2.30亿</span> （+7.28%，PCB，高位兑现）<br>
            2. 超声电子 <span style="color:#f87171;">-2.21亿</span> （+10.00%，PCB，高位兑现）<br>
            3. 北方铜业 <span style="color:#f87171;">-1.86亿</span> （-10.01%，铜/周期，获利盘出逃）<br>
            4. 法尔胜 <span style="color:#f87171;">-1.04亿</span> （-0.59%，高位题材）<br>
            5. 红棉股份 <span style="color:#f87171;">-0.90亿</span> （-10.09%，题材股）
        </div>
    </div>
</div>

<div style="background: rgba(255,255,255,0.03); border-radius: 12px; padding: 16px; border: 1px solid rgba(255,255,255,0.08);">
    <div style="font-size: 14px; font-weight: 700; color: #e2e8f0; margin-bottom: 8px;">🔍 龙虎榜核心解读</div>
    <div style="font-size: 13px; color: #cbd5e1; line-height: 1.9;">
        ① <b>机构态度：</b>45只个股现机构席位，22只净买入/23只净卖出，整体净买入16.87亿，机构分歧加大但偏积极；<br>
        ② <b>主线清晰：</b>机构抢筹方向集中在<span style="color:#4ade80;">电子布/PCB（金安国纪+13.79亿）、军工（博云新材+4.66亿）、光通信（长盈通+2.91亿）</span>，AI算力硬件链获机构持续加仓；<br>
        ③ <b>兑现方向：</b>机构卖出集中在周期股（北方铜业跌停）和高位PCB（逸豪新材/超声电子），属于正常获利了结，不是板块性看空；<br>
        ④ <b>持仓影响：</b>4只持仓股均未上龙虎榜，机构买卖占比<成交额5%，不构成异动信号。
    </div>
</div>
'''

gen._components.append(LayoutSection(title="📊 龙虎榜与资金流向", content=longhubang_html, icon="chart-bar"))

# 6. 盘后重要公告梳理
announcements_html = '''
<div class="grid md:grid-cols-2 gap-3">
    <div style="background: rgba(255,255,255,0.03); border-radius: 12px; padding: 16px; border: 1px solid rgba(255,255,255,0.08);">
        <div style="font-size: 14px; font-weight: 700; color: #4ade80; margin-bottom: 10px;">✅ 利好公告</div>
        <div style="font-size: 13px; color: #cbd5e1; line-height: 2;">
            · <b>华锡有色</b>：筹划控制权变更，下周一停牌不超2日，中国五矿或入主<br>
            · <b>新华传媒</b>：筹划发行股份购买界面财联社控股权，继续停牌<br>
            · <b>东阳光</b>：控股股东首次增持737万股，金额2.32亿元<br>
            · <b>先惠技术</b>：实控人+高管拟增持4000万~8000万元<br>
            · <b>沃森生物</b>：玉溪沃森mRNA疫苗获批上市许可（18岁以上）<br>
            · <b>华虹宏力</b>：完成发行股份购资产+配募，1.91亿新增股份登记
        </div>
    </div>
    <div style="background: rgba(255,255,255,0.03); border-radius: 12px; padding: 16px; border: 1px solid rgba(255,255,255,0.08);">
        <div style="font-size: 14px; font-weight: 700; color: #f87171; margin-bottom: 10px;">⚠️ 利空/风险公告</div>
        <div style="font-size: 13px; color: #cbd5e1; line-height: 2;">
            · <b>*ST清越</b>：连续20日收盘价低于1元，触及交易类退市，今日停牌<br>
            · <b>亚邦股份</b>：控股股东34.02%股份将司法拍卖，实控权存重大不确定性<br>
            · <b>上海合晶</b>：持股5%以上股东拟减持不超1%<br>
            · <b>皮阿诺/欧普康视/国科恒泰</b>：持股5%以上股东拟减持不超3%<br>
            · <b>桂林旅游</b>：4连板后澄清未参与平陆运河业务（炒作降温）<br>
            · <b>捷荣技术</b>：澄清折叠屏精密结构件收入占比极低
        </div>
    </div>
</div>
'''

gen._components.append(LayoutSection(title="📋 盘后重要公告梳理", content=announcements_html, icon="newspaper"))

# 7. 产业链分析（dict格式）
gen.add_industry_chain_analysis(
    upstream=[
        {
            "name": "AI芯片",
            "desc": "英伟达、AMD等国际巨头；燧原科技等国产替代加速",
            "stocks": [
                {"code": "NVDA", "name": "英伟达", "impact": "盘前+0.6%"},
                {"code": "688247", "name": "燧原科技", "impact": "首日+179%"},
            ]
        },
        {
            "name": "HBM/存储芯片",
            "desc": "SK海力士、美光、三星；韩国KB证券称存储库存不到10天",
            "stocks": [
                {"code": "MU", "name": "美光科技", "impact": "盘前+0.8%"},
            ]
        },
        {
            "name": "半导体设备/制造",
            "desc": "阿斯麦、台积电；台积电8月营收同比+53.3%，创历史新高",
            "stocks": [
                {"code": "TSM", "name": "台积电ADR", "impact": "盘前上涨"},
                {"code": "ASML", "name": "阿斯麦", "impact": "盘前+1.5%"},
            ]
        },
    ],
    midstream=[
        {
            "name": "光模块/光通信",
            "desc": "FCC靴子落地+高盛上调预测，三重利好共振",
            "stocks": [
                {"code": "300308", "name": "中际旭创", "impact": "成交299.7亿居首"},
                {"code": "300502", "name": "新易盛", "impact": "本周净流入52亿"},
                {"code": "300394", "name": "天孚通信", "impact": "CPO核心受益"},
            ]
        },
        {
            "name": "PCB/高速铜连接",
            "desc": "AI服务器PCB需求爆发，机构大举加仓",
            "stocks": [
                {"code": "002636", "name": "金安国纪", "impact": "机构+13.79亿"},
                {"code": "002384", "name": "东山精密", "impact": "本周净流入40亿"},
                {"code": "301217", "name": "铜冠铜箔", "impact": "AI铜箔龙头"},
            ]
        },
        {
            "name": "液冷散热/半导体材料",
            "desc": "液冷为算力基础设施，HBM材料需求随AI算力爆发",
            "stocks": [
                {"code": "002837", "name": "英维克", "impact": "液冷龙头"},
                {"code": "002409", "name": "雅克科技", "impact": "HBM前驱体"},
            ]
        },
    ],
    downstream=[
        {
            "name": "AI云服务/智算中心",
            "desc": "甲骨文Q1云收入+121%，AI算力需求加速兑现",
            "stocks": [
                {"code": "ORCL", "name": "甲骨文", "impact": "盘前+5~7%"},
            ]
        },
        {
            "name": "大模型/AI应用",
            "desc": "AI应用层随算力成本下降逐步放量",
            "stocks": []
        },
    ]
)

# 8. 投资机会
gen.add_investment_opportunities([
    {
        "title": "光模块/光通信",
        "level": "S级",
        "logic": "FCC靴子落地+高盛上调行业预测至2028年1485亿美元+甲骨文验证算力需求，三重利好共振。中际旭创本周主力净流入105亿，机构持续加仓。",
        "targets": [
            {"name": "中际旭创", "code": "300308", "comment": "全球光模块龙头，H股目标价3267港元"},
            {"name": "新易盛", "code": "300502", "comment": "高速光模块核心标的，本周+52亿净流入"},
            {"name": "天孚通信", "code": "300394", "comment": "光器件平台型公司，CPO核心受益"},
        ]
    },
    {
        "title": "PCB/高速铜连接",
        "level": "A级",
        "logic": "AI服务器PCB需求爆发，金安国纪机构单日净买入13.79亿信号强烈。高多层/HDI板供需紧张，铜箔、CCL全链受益。",
        "targets": [
            {"name": "铜冠铜箔", "code": "301217", "comment": "AI铜箔龙头，调入深证成指+创业板指"},
            {"name": "金安国纪", "code": "002636", "comment": "电子布/CCL龙头，机构大举加仓"},
            {"name": "东山精密", "code": "002384", "comment": "PCB龙头，本周主力净流入40亿"},
        ]
    },
    {
        "title": "国产AI芯片",
        "level": "A级",
        "logic": "燧原科技上市首日+179%，国产AI芯片情绪高涨。美国出口管制背景下，国产替代加速推进。工信部印发《人工智能+软件专项行动实施方案》。",
        "targets": [
            {"name": "海光信息", "code": "688041", "comment": "国产CPU/GPU龙头"},
            {"name": "寒武纪", "code": "688256", "comment": "AI芯片设计龙头"},
            {"name": "龙芯中科", "code": "688047", "comment": "国产CPU自主可控"},
        ]
    },
    {
        "title": "军工（防御+成长）",
        "level": "B级",
        "logic": "中东局势持续紧张，军工板块逆市走强（地面兵装今日领涨）。博云新材机构净买入4.66亿，军工+半导体材料双重逻辑。",
        "targets": [
            {"name": "博云新材", "code": "002297", "comment": "碳碳复合材料+军工，机构大举加仓"},
        ]
    },
], view_mode="card")

# 9. 风险提示
gen.add_risk_warning([
    "美国8月CPI数据超预期风险：若核心CPI环比>0.2%，美联储9月加息概率或飙升至80%+，10年期美债收益率可能突破5%，全球风险资产承压",
    "中东局势反复风险：胡塞停火声明真实性待确认，特朗普表态具有不确定性，油价可能再次冲高",
    "A股情绪面风险：全市场超4800只个股下跌，市场恐慌情绪蔓延，科技板块可能继续被错杀",
    "持仓股流动性风险：英维克深度套牢，止损纪律需严格执行；铜冠铜箔/雅克科技若跌破关键支撑位需减仓",
    "S级催化时效性风险：甲骨文财报利好可能被CPI数据压制，短期波动剧烈，不宜追高",
])

# 10. 投资策略
gen.add_investment_strategy(
    "<b>【总体判断】</b>当前处于\"AI算力基本面超预期\"与\"宏观流动性收紧\"的博弈期。甲骨文财报验证了AI算力需求的真实性和持续性，FCC靴子落地解除了光通信最大政策风险，但CPI数据和美联储加息仍是短期压制因素。<br><br>"
    "<b>【仓位管理】</b>总仓位控制在60-70%，保留30%+现金应对周末不确定性。左侧抄底不超过30%，等待CPI数据和下周一趋势确认后再加仓。<br><br>"
    "<b>【持仓操作】</b><br>"
    "· <b>英维克</b>：60元附近观察支撑，若跌破58元减仓20%；反弹至65元以上可考虑做T降低成本。长期逻辑不变（液冷渗透率提升），但短期受情绪影响大。<br>"
    "· <b>铜冠铜箔</b>：100-105元为击球区，可逢低加仓（不超过总仓10%）。AI铜箔需求逻辑强，调入指数带来被动配置增量。技术面：100元支撑、120元目标。<br>"
    "· <b>雅克科技</b>：125元支撑位可小幅加仓（底仓持有），反弹至140元以上减仓机动仓。PE 55x处于历史中位，估值合理。HBM材料需求随甲骨文验证进一步强化。<br>"
    "· <b>*ST建艺</b>：维持防御仓位，科技板块企稳前不急于减仓。<br><br>"
    "<b>【重点关注】</b><br>"
    "① 今晚20:30美国8月CPI数据（核心CPI环比是关键）<br>"
    "② 美股科技股今晚表现（甲骨文财报能否带动板块反弹）<br>"
    "③ 周末中东局势发展（停火是否属实、油价走势）<br>"
    "④ 下周一A股开盘：光模块/PCB板块能否延续强势<br><br>"
    "<b>【操作纪律】</b>严格执行止损，单只个股回撤>10%必须减仓，总仓位回撤>5%降低仓位至50%以下。不追高、不满仓、不加杠杆。"
)

# 发布
result = gen.publish(
    title="CPI前夜全球重估+甲骨文验证AI算力超预期",
    filename="20260911_盘后_S级催化扫描_CPI前夜+甲骨文AI算力验证.html"
)
print("发布结果：", result)
