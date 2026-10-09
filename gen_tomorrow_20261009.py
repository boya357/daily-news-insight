#!/usr/bin/env python3
"""
明日催化剂 - 2026年10月10日/下周催化事件报告
生成日期: 2026-10-09
聚焦: 10月12日(周一)及本周重点催化事件
"""

import sys, os
sys.path.insert(0, '/root/daily-news-insight/v3')
os.chdir('/root/daily-news-insight')

from v3.generators.tomorrow_catalyst import TomorrowCatalystGenerator

gen = TomorrowCatalystGenerator(
    date_str="20261010",
    subtitle="2026.10.10 · 下周催化剂前瞻（10.12-10.16）"
)

# 1. 明日核心催化
core_catalyst_html = """
<div style="line-height: 1.8; color: #f1f5f9;">
    <p style="margin-bottom: 12px;"><strong style="color: #fbbf24;">【周一开盘核心关注】</strong>10月10日-12日周末期间三件大事将直接影响周一A股开盘方向：</p>
    <ul style="padding-left: 20px; color: #e2e8f0;">
        <li style="margin-bottom: 8px;"><span style="color: #f97316;">🔥 安森美涨价10月10日正式生效</span> — 全球功率半导体大厂ON Semiconductor全产品系列调价落地，英飞凌、TI、意法半导体已先后涨价，AI驱动功率半导体供需紧张格局确认，关注立昂微(605358)、东微半导(688261)、华虹宏力、芯联集成-U</li>
        <li style="margin-bottom: 8px;"><span style="color: #3b82f6;">🏭 第26届上海工博会10月12日开幕</span> — 首次设立集成电路展（国芯展），3000家展商、30万平米展区，覆盖数控机床、机器人、新能源汽车、AI+制造等十大专业展，工业母机+人形机器人+半导体设备多条主线共振</li>
        <li style="margin-bottom: 8px;"><span style="color: #ef4444;">⚠️ 周一解禁压力骤增</span> — 陕西能源(001286)24亿股解禁占总股本64%（约226亿市值）、金科股份(000656)18亿股解禁占17%、首药控股(688197)解禁比例56.96%，15股合计45.4亿股解禁</li>
    </ul>
    <p style="margin-top: 12px; color: #94a3b8; font-size: 13px;">本周看点：阶跃Step 5 Preview开源(10/15)、千问AI眼镜发售(10/13)、湾芯展(10/14-16)、中国9月CPI(10/14)、美国9月CPI(10/14)、广交会(10/15开幕)</p>
</div>
"""
gen.add_key_catalyst(core_catalyst_html)

# 2. 事件日历
events = [
    {'type': 'meeting', 'title': '第26届中国国际工业博览会（上海工博会）',
     'description': '10月12日-16日在国家会展中心（上海）举行，首次设立集成电路展（国芯展），设10大专业展，3000家展商参展，展区面积30万平米。聚焦工业母机、机器人、新能源汽车、AI+制造、半导体全产业链。',
     'category': '产业盛会 · S级'},
    {'type': 'policy', 'title': '安森美(ON Semiconductor)产品涨价正式生效',
     'description': '10月10日起对广泛产品系列实施价格调整，原材料、制造成本上涨是主因。AI驱动功率半导体高景气，海外IDM库存策略结构性转变，英飞凌、TI、意法半导体均已涨价。',
     'category': '半导体涨价 · A级'},
    {'type': 'meeting', 'title': '2026湾区半导体产业生态博览会（湾芯展）',
     'description': '10月14日-16日举办，聚焦半导体产业链生态，覆盖设计、制造、封测、设备、材料全链条，湾区半导体企业集中亮相。',
     'category': '半导体 · A级'},
    {'type': 'meeting', 'title': '2026人工智能产业大会（济南）',
     'description': '10月14日-16日在山东济南举办，聚焦人工智能产业落地与应用，预计发布多项AI产业政策与合作项目。',
     'category': 'AI产业 · B级'},
    {'type': 'general', 'title': '小鹏汽车新车巴黎全球上市发布会',
     'description': '小鹏集团董事长何小鹏宣布，新车将于10月12日在法国巴黎举办全球上市发布会，小鹏国际化战略加速推进。',
     'category': '新能源汽车 · B级'},
    {'type': 'general', 'title': '千问新一代AI眼镜10月13日现货发售',
     'description': '阿里达摩院旗下千问品牌新一代AI智能眼镜正式开售，AI硬件消费电子新赛道重要里程碑。',
     'category': 'AI硬件 · A级'},
    {'type': 'general', 'title': '京东"双11"活动10月12日全面开启',
     'description': '京东2026年双11大促10月12日启动预售，预计消费电子、家电、美妆等品类将迎来全年最大力度促销。',
     'category': '消费 · B级'},
    {'type': 'general', 'title': '阶跃星辰Step 5 Preview 10月15日正式开源',
     'description': '阶跃星辰(StepFun)将于10月15日开源Step 5 Preview版本，国产大模型开源生态再添重要玩家，有望推动AI应用成本进一步下降。',
     'category': '大模型 · A级'},
    {'type': 'data', 'title': '中国9月CPI/PPI数据公布',
     'description': '10月14日公布9月CPI年率，前值0.8%。通胀数据是判断货币政策走向的重要参考。',
     'category': '宏观数据 · A级'},
    {'type': 'data', 'title': '美国9月核心CPI年率公布',
     'description': '10月14日公布美国9月核心CPI，前值2.4%。美联储9月已加息25bp至3.75%-4%，12月再加息概率约68%。',
     'category': '海外数据 · A级'},
    {'type': 'data', 'title': '沪市首份三季报：有研新材',
     'description': '10月13日有研新材(600206)发布沪市首份三季报，三季报披露季正式拉开帷幕。截至10月8日已有27家公司预告前三季业绩，预增比例约81%。',
     'category': '业绩披露 · B级'},
    {'type': 'general', 'title': '陕西能源24亿股限售股解禁',
     'description': '10月12日解禁，占总股本64%，解禁市值约226亿元，为周一最大解禁规模。公用事业板块解禁压力集中释放。',
     'category': '解禁风险 · S级'},
    {'type': 'general', 'title': '金科股份18亿股重整限售股解禁',
     'description': '10月12日解禁，25家重整财务投资人合计18亿股，占总股本16.9992%。房地产板块流动性承压。',
     'category': '解禁风险 · A级'},
    {'type': 'general', 'title': '首药控股56.96%比例解禁',
     'description': '10月12日8471万股解禁，占总股本56.96%，占现流通股本132.36%。创新药板块高比例解禁标的。',
     'category': '解禁风险 · A级'},
    {'type': 'general', 'title': '三星电子Q3业绩暴增782.5%',
     'description': '三星电子Q3营业利润107.4万亿韩元(约801.7亿美元)，同比+782.5%，环比+20%，HBM出货量环比+50%。存储超级周期确认。',
     'category': '海外业绩 · S级'},
    {'type': 'general', 'title': '第140届广交会10月15日开幕',
     'description': '10月15日-11月4日在广州举办，中国外贸"晴雨表"，预计超200个国家和地区的采购商参会。出口链景气度观察窗口。',
     'category': '外贸 · B级'},
]

gen.add_events_calendar(events)

# 3. 限售股解禁详情
from components.layout import Section

jiejin_html = """
<div style="overflow-x: auto;">
    <table style="width: 100%; border-collapse: collapse; font-size: 13px; color: #e2e8f0;">
        <thead>
            <tr style="border-bottom: 2px solid rgba(255,255,255,0.1);">
                <th style="padding: 10px 12px; text-align: left; color: #94a3b8; font-weight: 500;">股票名称</th>
                <th style="padding: 10px 12px; text-align: center; color: #94a3b8; font-weight: 500;">代码</th>
                <th style="padding: 10px 12px; text-align: right; color: #94a3b8; font-weight: 500;">解禁数量(亿股)</th>
                <th style="padding: 10px 12px; text-align: right; color: #94a3b8; font-weight: 500;">占总股本%</th>
                <th style="padding: 10px 12px; text-align: right; color: #94a3b8; font-weight: 500;">占流通股%</th>
                <th style="padding: 10px 12px; text-align: center; color: #94a3b8; font-weight: 500;">风险等级</th>
            </tr>
        </thead>
        <tbody>
            <tr style="border-bottom: 1px solid rgba(255,255,255,0.05); background: rgba(239,68,68,0.08);">
                <td style="padding: 10px 12px; font-weight: 600;">陕西能源</td>
                <td style="padding: 10px 12px; text-align: center; color: #94a3b8;">001286</td>
                <td style="padding: 10px 12px; text-align: right; color: #fca5a5; font-weight: 600;">24.00</td>
                <td style="padding: 10px 12px; text-align: right; color: #fca5a5;">64.00%</td>
                <td style="padding: 10px 12px; text-align: right; color: #fca5a5;">228.57%</td>
                <td style="padding: 10px 12px; text-align: center;"><span style="background: rgba(239,68,68,0.2); color: #fca5a5; padding: 2px 10px; border-radius: 12px; font-size: 11px;">极高风险</span></td>
            </tr>
            <tr style="border-bottom: 1px solid rgba(255,255,255,0.05);">
                <td style="padding: 10px 12px; font-weight: 600;">金科股份</td>
                <td style="padding: 10px 12px; text-align: center; color: #94a3b8;">000656</td>
                <td style="padding: 10px 12px; text-align: right; color: #f97316; font-weight: 600;">18.00</td>
                <td style="padding: 10px 12px; text-align: right; color: #f97316;">17.00%</td>
                <td style="padding: 10px 12px; text-align: right; color: #f97316;">23.73%</td>
                <td style="padding: 10px 12px; text-align: center;"><span style="background: rgba(249,115,22,0.2); color: #fdba74; padding: 2px 10px; border-radius: 12px; font-size: 11px;">高风险</span></td>
            </tr>
            <tr style="border-bottom: 1px solid rgba(255,255,255,0.05);">
                <td style="padding: 10px 12px; font-weight: 600;">首药控股</td>
                <td style="padding: 10px 12px; text-align: center; color: #94a3b8;">688197</td>
                <td style="padding: 10px 12px; text-align: right; color: #f97316; font-weight: 600;">0.85</td>
                <td style="padding: 10px 12px; text-align: right; color: #f97316;">56.96%</td>
                <td style="padding: 10px 12px; text-align: right; color: #f97316;">132.36%</td>
                <td style="padding: 10px 12px; text-align: center;"><span style="background: rgba(249,115,22,0.2); color: #fdba74; padding: 2px 10px; border-radius: 12px; font-size: 11px;">高风险</span></td>
            </tr>
            <tr style="border-bottom: 1px solid rgba(255,255,255,0.05);">
                <td style="padding: 10px 12px; font-weight: 600;">奥美森</td>
                <td style="padding: 10px 12px; text-align: center; color: #94a3b8;">920080</td>
                <td style="padding: 10px 12px; text-align: right; color: #f97316; font-weight: 600;">0.58</td>
                <td style="padding: 10px 12px; text-align: right; color: #f97316;">69.51%</td>
                <td style="padding: 10px 12px; text-align: right; color: #f97316;">254.60%</td>
                <td style="padding: 10px 12px; text-align: center;"><span style="background: rgba(249,115,22,0.2); color: #fdba74; padding: 2px 10px; border-radius: 12px; font-size: 11px;">高风险</span></td>
            </tr>
            <tr style="border-bottom: 1px solid rgba(255,255,255,0.05);">
                <td style="padding: 10px 12px; font-weight: 600;">星徽股份</td>
                <td style="padding: 10px 12px; text-align: center; color: #94a3b8;">300464</td>
                <td style="padding: 10px 12px; text-align: right; color: #eab308; font-weight: 600;">1.02</td>
                <td style="padding: 10px 12px; text-align: right; color: #eab308;">21.88%</td>
                <td style="padding: 10px 12px; text-align: right; color: #eab308;">28.79%</td>
                <td style="padding: 10px 12px; text-align: center;"><span style="background: rgba(234,179,8,0.2); color: #fde047; padding: 2px 10px; border-radius: 12px; font-size: 11px;">中风险</span></td>
            </tr>
            <tr style="border-bottom: 1px solid rgba(255,255,255,0.05);">
                <td style="padding: 10px 12px; font-weight: 600;">中集环科</td>
                <td style="padding: 10px 12px; text-align: center; color: #94a3b8;">301559</td>
                <td style="padding: 10px 12px; text-align: right; color: #eab308; font-weight: 600;">0.51</td>
                <td style="padding: 10px 12px; text-align: right; color: #eab308;">8.50%</td>
                <td style="padding: 10px 12px; text-align: right; color: #eab308;">56.67%</td>
                <td style="padding: 10px 12px; text-align: center;"><span style="background: rgba(234,179,8,0.2); color: #fde047; padding: 2px 10px; border-radius: 12px; font-size: 11px;">中风险</span></td>
            </tr>
            <tr style="border-bottom: 1px solid rgba(255,255,255,0.05);">
                <td style="padding: 10px 12px; font-weight: 600;">珈凯生物</td>
                <td style="padding: 10px 12px; text-align: center; color: #94a3b8;">920165</td>
                <td style="padding: 10px 12px; text-align: right; color: #eab308; font-weight: 600;">0.07</td>
                <td style="padding: 10px 12px; text-align: right; color: #eab308;">14.73%</td>
                <td style="padding: 10px 12px; text-align: right; color: #eab308;">74.01%</td>
                <td style="padding: 10px 12px; text-align: center;"><span style="background: rgba(234,179,8,0.2); color: #fde047; padding: 2px 10px; border-radius: 12px; font-size: 11px;">中风险</span></td>
            </tr>
            <tr style="border-bottom: 1px solid rgba(255,255,255,0.05);">
                <td style="padding: 10px 12px; font-weight: 600;">惠城环保</td>
                <td style="padding: 10px 12px; text-align: center; color: #94a3b8;">300779</td>
                <td style="padding: 10px 12px; text-align: right; color: #10b981; font-weight: 600;">0.14</td>
                <td style="padding: 10px 12px; text-align: right; color: #10b981;">4.87%</td>
                <td style="padding: 10px 12px; text-align: right; color: #10b981;">6.37%</td>
                <td style="padding: 10px 12px; text-align: center;"><span style="background: rgba(16,185,129,0.2); color: #6ee7b7; padding: 2px 10px; border-radius: 12px; font-size: 11px;">低风险</span></td>
            </tr>
        </tbody>
    </table>
</div>
<div style="margin-top: 12px; padding: 10px 14px; background: rgba(239,68,68,0.1); border-left: 3px solid #ef4444; border-radius: 0 8px 8px 0; font-size: 13px; color: #fca5a5; line-height: 1.6;">
    <strong>⚠️ 解禁提示：</strong>10月12日（周一）共有15只股票解禁，合计45.4亿股，为节后首个交易日最大解禁日。
    陕西能源24亿股占总股本64%，解禁后流通盘暴增2.28倍，为全市场最大压力源；
    首药控股、奥美森解禁占流通盘比例均超100%，小市值标的需特别警惕流动性冲击。
    10月全月解禁总市值约3000亿元，环比+62.8%，主要压力集中在下旬（10/23、10/26、10/28、10/29）。
</div>
"""
jiejin_section = Section(title="🔓 限售股解禁详情（10月12日）", content=jiejin_html, icon="unlock")
gen._components.append(jiejin_section)

# 4. 新股申购
new_stock_html = """
<div style="line-height: 1.7; color: #e2e8f0; font-size: 14px;">
    <p style="margin-bottom: 12px;"><strong>下周新股申购安排（10月12日-10月16日）：</strong></p>
    <div style="padding: 14px 16px; background: rgba(59,130,246,0.1); border-radius: 12px; border: 1px solid rgba(59,130,246,0.2); margin-bottom: 14px;">
        <div style="font-weight: 600; color: #93c5fd; margin-bottom: 6px;">📢 重要提示：下周无新股申购</div>
        <div style="font-size: 13px; color: #94a3b8;">
            本周唯一申购标的通则康威(301718)已于10月9日完成申购，中签号将于10月13日(周二)公布。
            下一只新股申购为皇冠新材(001381)，申购日期为10月19日(周一)。
        </div>
    </div>
    
    <div style="font-weight: 600; color: #f1f5f9; margin-bottom: 8px;">📋 本周新股动态：</div>
    <div style="display: flex; flex-direction: column; gap: 8px;">
        <div style="padding: 10px 14px; background: rgba(255,255,255,0.05); border-radius: 8px; border: 1px solid rgba(255,255,255,0.08);">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <span style="font-weight: 600;">通则康威(301718)</span>
                <span style="font-size: 12px; background: rgba(59,130,246,0.3); color: #93c5fd; padding: 2px 8px; border-radius: 6px;">10/13 中签号</span>
            </div>
            <div style="font-size: 12px; color: #94a3b8; margin-top: 4px;">
                发行价26.88元/股 · 发行市盈率44.72倍(行业73.53倍) · 宽带连接终端设备 · 境外收入占比90.61%
            </div>
        </div>
        <div style="padding: 10px 14px; background: rgba(255,255,255,0.05); border-radius: 8px; border: 1px solid rgba(255,255,255,0.08);">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <span style="font-weight: 600;">宇特光电(920157)</span>
                <span style="font-size: 12px; background: rgba(16,185,129,0.3); color: #6ee7b7; padding: 2px 8px; border-radius: 6px;">10/9 已上市</span>
            </div>
            <div style="font-size: 12px; color: #94a3b8; margin-top: 4px;">
                北交所 · 发行价13.75元/股 · 发行市盈率14.99倍 · 光连接产品/数据中心光模块组件
            </div>
        </div>
    </div>
    
    <div style="margin-top: 14px; font-size: 13px; color: #94a3b8;">
        <strong>申购策略：</strong>下周打新空窗期，投资者可关注已上市新股的交易机会。
        通则康威作为全球5G FWA CPE第七大供应商，受益于全球宽带建设和AI算力基础设施需求，建议关注上市后表现。
        皇冠新材(10/19申购)为包装新材料企业，可提前做好申购准备。
    </div>
</div>
"""
new_stock_section = Section(title="📈 新股申购与上市", content=new_stock_html, icon="trending-up")
gen._components.append(new_stock_section)

# 5. 经济数据公布
gen.add_data_release([
    {'name': '中国9月CPI年率', 'prev': '0.8%', 'expect': '待公布', 'actual': '10/14公布'},
    {'name': '美国9月核心CPI年率', 'prev': '2.4%', 'expect': '待公布', 'actual': '10/14公布'},
    {'name': '美国10月密歇根大学消费者信心指数', 'prev': '48.1', 'expect': '47.8', 'actual': '10/9公布'},
    {'name': '中国9月PPI', 'prev': '待确认', 'expect': '待公布', 'actual': '10/14公布'},
    {'name': '日本9月PPI年率', 'prev': '7.6%', 'expect': '待公布', 'actual': '10/13公布'},
    {'name': '美国9月成屋销售年化总数', 'prev': '待确认', 'expect': '待公布', 'actual': '10/13公布'},
])

# 6. 海外大事提醒
overseas_html = """
<div style="display: flex; flex-direction: column; gap: 10px;">
    <div style="padding: 14px 16px; background: rgba(139,92,246,0.1); border-radius: 12px; border: 1px solid rgba(139,92,246,0.2);">
        <div style="font-weight: 600; color: #c4b5fd; margin-bottom: 6px;">🇺🇸 美联储12月加息概率升至68%</div>
        <div style="font-size: 13px; color: #cbd5e1; line-height: 1.6;">
            美联储9月FOMC会议纪要显示，与会成员一致同意加息25bp至3.75%-4%，多数认为年底前进一步上调利率可能合适。
            纽约联储调查显示9月消费者一年期通胀预期升至3.9%（2023年5月以来最高），强化加息预期。
            <strong style="color: #f87171;">关注10月14日美国9月CPI数据</strong>，若超预期将进一步推升加息概率。
        </div>
    </div>
    
    <div style="padding: 14px 16px; background: rgba(245,158,11,0.1); border-radius: 12px; border: 1px solid rgba(245,158,11,0.2);">
        <div style="font-weight: 600; color: #fcd34d; margin-bottom: 6px;">🇰🇷 三星Q3业绩暴增782.5%，存储超级周期确认</div>
        <div style="font-size: 13px; color: #cbd5e1; line-height: 1.6;">
            三星电子Q3营业利润107.4万亿韩元(约801.7亿美元)，同比+782.5%，环比+20%。
            HBM出货量环比增长近50%，AI芯片需求爆发带动内存业务盈利强劲增长。
            10月29日将公布完整财报。存储产业链HBM方向持续高景气，关注<strong style="color: #fbbf24;">HBM材料、存储封测、DDR5产业链</strong>。
        </div>
    </div>
    
    <div style="padding: 14px 16px; background: rgba(16,185,129,0.1); border-radius: 12px; border: 1px solid rgba(16,185,129,0.2);">
        <div style="font-weight: 600; color: #6ee7b7; margin-bottom: 6px;">🌏 安森美10月10日起全系列涨价，功率半导体共振</div>
        <div style="font-size: 13px; color: #cbd5e1; line-height: 1.6;">
            ON Semiconductor涨价正式生效，年内已完成两轮调价。英飞凌、TI、意法半导体、瑞萨电子均已落地涨价动作。
            台系厂商强茂、台半计划10月对现货再度提价10%-15%。
            AI驱动功率半导体需求爆发+8英寸成熟制程产能紧张，行业供需格局持续向好，原厂订单交期延长。
        </div>
    </div>
    
    <div style="padding: 14px 16px; background: rgba(236,72,153,0.1); border-radius: 12px; border: 1px solid rgba(236,72,153,0.2);">
        <div style="font-weight: 600; color: #f9a8d4; margin-bottom: 6px;">🚢 马士基紧急燃油附加费上调至20%（10月12日生效）</div>
        <div style="font-size: 13px; color: #cbd5e1; line-height: 1.6;">
            全球最大集装箱航运公司马士基将紧急燃油附加费(EFS)上调至20%，10月12日起生效。
            国际油价持续高位推升航运成本，集运运价有望获得支撑。关注航运、港口、物流板块情绪变化。
            同时国内航线燃油附加费10月10日起上调，航空板块成本端承压。
        </div>
    </div>
    
    <div style="padding: 14px 16px; background: rgba(59,130,246,0.1); border-radius: 12px; border: 1px solid rgba(59,130,246,0.2);">
        <div style="font-weight: 600; color: #93c5fd; margin-bottom: 6px;">🇫🇷 小鹏汽车巴黎全球发布会（10月12日）</div>
        <div style="font-size: 13px; color: #cbd5e1; line-height: 1.6;">
            何小鹏亲赴法国巴黎举办新车全球上市发布会，小鹏国际化战略进入新阶段。
            欧洲市场是中国新能源汽车出海的核心战场，小鹏、比亚迪、蔚来等加速布局。
            关注出海产业链：整车出口、汽车零部件、海外充电基础设施。
        </div>
    </div>
</div>
"""
overseas_section = Section(title="🌍 海外大事提醒", content=overseas_html, icon="globe")
gen._components.append(overseas_section)

# 7. 重点事件深度影响分析
deep_analysis_html = """
<div style="line-height: 1.8; color: #e2e8f0; font-size: 14px;">
    
    <div style="margin-bottom: 20px;">
        <h3 style="color: #fbbf24; font-size: 16px; font-weight: 700; margin-bottom: 10px; border-left: 3px solid #fbbf24; padding-left: 10px;">
            一、安森美涨价落地：功率半导体涨价周期确认，国产替代加速
        </h3>
        <div style="padding: 12px 16px; background: rgba(255,255,255,0.03); border-radius: 10px;">
            <p style="margin-bottom: 8px;"><strong>事件：</strong>安森美(ON Semiconductor)于10月10日起对广泛产品系列实施价格调整，这是其年内第二轮涨价。全球功率半导体大厂英飞凌、德州仪器、意法半导体、瑞萨电子均已先后落地涨价动作，台系厂商强茂、台半计划10月对现货再度提价10%-15%。</p>
            <p style="margin-bottom: 8px;"><strong>影响分析：</strong></p>
            <p style="margin-bottom: 6px; padding-left: 12px;"><strong>1. 涨价逻辑从"渠道补库"升级为"原厂主动扩库存"。</strong>瑞萨电子已将全链条库存目标从120天提升至150天，这是厂商基于真实供需短缺做出的主动经营调整，区别于2021年渠道投机性囤货，确认本轮景气的持续性与真实性。AI算力爆发是核心增量，数据中心电源、服务器功率器件需求持续超预期。</p>
            <p style="margin-bottom: 6px; padding-left: 12px;"><strong>2. 供给端8英寸成熟制程产能紧张。</strong>AI相关需求持续抬升对8英寸产能的占用，挤压传统应用领域可用产能。功率半导体公司过去两年受制于竞争激烈，未有大规模产能扩产计划和资金支持，供需缺口将持续扩大。</p>
            <p style="margin-bottom: 6px; padding-left: 12px;"><strong>3. 国产替代窗口期打开。</strong>海外大厂全线涨价+交期延长，为国内功率半导体厂商带来绝佳的客户导入和份额提升机会。国内厂商在IGBT、MOSFET、SiC等领域已具备技术竞争力，有望加速替代海外品牌。</p>
            <p style="margin-bottom: 8px;"><strong>受益标的：</strong></p>
            <p style="padding-left: 12px;">
                <span style="color: #fbbf24;">立昂微(605358)</span> — 硅片+功率双轮驱动，上半年扭亏为盈，12英寸硅片产能爬坡中<br>
                <span style="color: #fbbf24;">东微半导(688261)</span> — 高压超级结MOSFET龙头，机构一致预测今明两年净利增速均超40%<br>
                <span style="color: #fbbf24;">华虹宏力(688347)</span> — 8英寸晶圆代工龙头，功率器件产能紧张直接受益<br>
                <span style="color: #fbbf24;">芯联集成-U(688469)</span> — 功率半导体IDM，上半年归母净利同比增长超100%
            </p>
            <p style="margin-top: 8px;"><strong>操作建议：</strong>功率半导体本轮涨价周期的级别和持续性超出市场预期，AI驱动的需求增量是核心变量。
            建议逢低布局上游晶圆代工+设计龙头，重点关注12英寸产能扩张进度和SiC/GaN等宽禁带半导体布局进展。
            短期注意安森美涨价"靴子落地"后的情绪兑现风险，但中期趋势明确，回调即是加仓机会。</p>
        </div>
    </div>
    
    <div style="margin-bottom: 20px;">
        <h3 style="color: #3b82f6; font-size: 16px; font-weight: 700; margin-bottom: 10px; border-left: 3px solid #3b82f6; padding-left: 10px;">
            二、上海工博会开幕：十大专业展，首次设立集成电路展
        </h3>
        <div style="padding: 12px 16px; background: rgba(255,255,255,0.03); border-radius: 10px;">
            <p style="margin-bottom: 8px;"><strong>事件：</strong>第26届中国国际工业博览会（上海工博会）将于10月12日-16日在国家会展中心（上海）举行，展区面积30万平米，3000家展商参展，预计超20万专业观众。今年首次设立集成电路展（国芯展），十大专业展覆盖数控机床、工业自动化、机器人、智慧能源、信息与通信、智行未来、绿色低碳、新材料、科技创新、集成电路。</p>
            <p style="margin-bottom: 8px;"><strong>影响分析：</strong></p>
            <p style="margin-bottom: 6px; padding-left: 12px;"><strong>1. 半导体设备/材料国产化进展集中展示。</strong>首次设立的国芯展是最大看点，将集中展示国产光刻机、刻蚀机、薄膜沉积、清洗、CMP、量检测等全链条设备进展，以及靶材、抛光液、电子化学品等关键材料的最新突破。国产替代的"硬支撑"将从概念走向实锤。</p>
            <p style="margin-bottom: 6px; padding-left: 12px;"><strong>2. 人形机器人+工业机器人双线并行。</strong>机器人展将展示最新的人形机器人原型机、协作机器人、工业机器人解决方案。特斯拉Optimus、小米CyberOne、宇树、傅利叶等人形机器人进展是市场关注焦点，工博会是国内厂商集中秀肌肉的舞台。</p>
            <p style="margin-bottom: 6px; padding-left: 12px;"><strong>3. AI+制造深度融合场景集中呈现。</strong>信息与通信展更名为"新一代智能制造展(AIMS)"，聚焦从词元到算力的AI+制造融合场景。工业大模型、机器视觉、智能检测、数字孪生等应用将有大量实物演示。</p>
            <p style="margin-bottom: 6px; padding-left: 12px;"><strong>4. 新能源汽车全产业链展示。</strong>智行未来展聚焦智能网联新能源汽车全产业链，从整车到车规芯片、智能驾驶、下一代电池全覆盖。</p>
            <p style="margin-bottom: 8px;"><strong>受益方向：</strong></p>
            <p style="padding-left: 12px;">
                <span style="color: #60a5fa;">半导体设备/材料</span> — 北方华创、中微公司、拓荆科技、华海诚科、雅克科技<br>
                <span style="color: #60a5fa;">工业母机/数控机床</span> — 科德数控、华中数控、创世纪、海天精工<br>
                <span style="color: #60a5fa;">人形机器人</span> — 拓普集团、三花智控、鸣志电器、绿的谐波<br>
                <span style="color: #60a5fa;">AI+制造</span> — 中控技术、宝信软件、赛意信息、汉得信息
            </p>
            <p style="margin-top: 8px;"><strong>操作建议：</strong>工博会是事件驱动型行情的典型催化剂，开幕前一周相关板块通常会有预热行情。
            重点关注首次设立的集成电路展带来的半导体设备/材料方向催化，以及人形机器人的最新进展。
            建议在周一开盘前布局预期差较大的细分方向，开幕后根据实际展示内容调整仓位。
            注意"见光死"风险，若展会内容不及预期，需及时止盈。</p>
        </div>
    </div>
    
    <div style="margin-bottom: 20px;">
        <h3 style="color: #ef4444; font-size: 16px; font-weight: 700; margin-bottom: 10px; border-left: 3px solid #ef4444; padding-left: 10px;">
            三、周一解禁洪峰：45.4亿股集中释放，陕西能源压力最大
        </h3>
        <div style="padding: 12px 16px; background: rgba(255,255,255,0.03); border-radius: 10px;">
            <p style="margin-bottom: 8px;"><strong>事件：</strong>10月12日（周一）共有15只股票面临解禁，合计45.4亿股。其中陕西能源24亿股（占总股本64%）、金科股份18亿股（占17%）、首药控股8471万股（占56.96%）为三大压力源。</p>
            <p style="margin-bottom: 8px;"><strong>影响分析：</strong></p>
            <p style="margin-bottom: 6px; padding-left: 12px;"><strong>1. 陕西能源解禁规模最大，冲击最剧烈。</strong>24亿股占总股本64%，解禁后流通盘暴增2.28倍（从10.5亿股增至34.5亿股）。
            作为公用事业板块的次新股，解禁前流通盘较小导致估值偏高，解禁后估值回归压力大。
            参考历史上类似高比例解禁次新股的走势，解禁前后1-2周内普遍承压10%-20%。</p>
            <p style="margin-bottom: 6px; padding-left: 12px;"><strong>2. 金科股份重整投资人解禁，减持意愿强。</strong>18亿股来自25家重整财务投资人，持仓成本远低于当前股价，
            财务投资人通常有较强的变现诉求。公司基本面仍较弱，上半年扣非净利润为负，
            投资人缺乏长期持有的理由，解禁后可能形成持续抛压。</p>
            <p style="margin-bottom: 6px; padding-left: 12px;"><strong>3. 小市值高比例解禁标的流动性风险大。</strong>首药控股、奥美森等解禁占流通盘比例超100%，
            但绝对市值不大，主要风险在于短期供需失衡导致的股价剧烈波动。
            创新药板块整体处于估值修复期，若公司基本面有亮点，解禁后反而可能迎来机构建仓机会。</p>
            <p style="margin-bottom: 6px; padding-left: 12px;"><strong>4. 全月解禁压力前低后高。</strong>10月全月解禁总市值约3000亿元，
            主要压力集中在下旬（10/23、10/26、10/28、10/29），西安奕材(788亿)、中船特气(743亿)两大解禁均在下旬。
            周一解禁虽有45亿股，但因陕西能源、金科股份股价低，绝对市值约260亿元，全月来看属于中等水平。</p>
            <p style="margin-top: 8px;"><strong>操作建议：</strong>
            持有陕西能源的投资者建议在解禁前减仓规避短期冲击，等待解禁后抛压释放完毕再考虑是否回补。
            金科股份建议观望为主，等待重整后的基本面改善信号。
            对于首药控股等创新药标的，若看好公司管线价值，可在解禁后逢低布局。
            整体来看，周一解禁对市场的影响以结构性为主，不会改变大盘趋势，但会对相关个股造成显著压力。</p>
        </div>
    </div>
    
    <div style="margin-bottom: 20px;">
        <h3 style="color: #8b5cf6; font-size: 16px; font-weight: 700; margin-bottom: 10px; border-left: 3px solid #8b5cf6; padding-left: 10px;">
            四、阶跃Step 5 Preview开源 + 千问AI眼镜发售：AI软硬件双轮驱动
        </h3>
        <div style="padding: 12px 16px; background: rgba(255,255,255,0.03); border-radius: 10px;">
            <p style="margin-bottom: 8px;"><strong>事件：</strong>阶跃星辰(StepFun)将于10月15日正式开源Step 5 Preview版本；千问新一代AI眼镜将于10月13日现货发售。</p>
            <p style="margin-bottom: 8px;"><strong>影响分析：</strong></p>
            <p style="margin-bottom: 6px; padding-left: 12px;"><strong>1. 大模型开源生态加速成熟。</strong>阶跃Step 5 Preview开源是继DeepSeek、通义千问之后又一国产大模型重要进展。
            开源模型能力的持续提升将推动AI应用成本快速下降，加速各行业AI渗透。
            同时开源生态的繁荣也会倒逼闭源模型厂商加快迭代，整体推动行业进步。</p>
            <p style="margin-bottom: 6px; padding-left: 12px;"><strong>2. AI眼镜：消费电子新赛道的关键节点。</strong>千问AI眼镜现货发售标志着AI眼镜从概念走向量产。
            AI眼镜被认为是继智能手机之后的下一代计算平台，
            具备AI助理、实时翻译、导航、拍照/录像、健康监测等功能，市场空间巨大。
            目前行业处于早期阶段，谁能率先打造爆款产品，谁就能占据先发优势。</p>
            <p style="margin-bottom: 6px; padding-left: 12px;"><strong>3. 软硬件共振推动AI产业落地。</strong>大模型开源降低软件门槛，AI硬件提供新的交互入口，
            二者结合将催生大量创新应用场景。从AI手机到AI眼镜再到AI PC，
            消费电子的AI化是大趋势，将带动光学、显示、传感、电池等上游产业链需求增长。</p>
            <p style="margin-bottom: 8px;"><strong>受益标的：</strong></p>
            <p style="padding-left: 12px;">
                <span style="color: #c4b5fd;">AI眼镜/AR</span> — 舜宇光学、歌尔股份、立讯精密、水晶光电、蓝特光学<br>
                <span style="color: #c4b5fd;">大模型/AI应用</span> — 科大讯飞、三六零、昆仑万维、万兴科技<br>
                <span style="color: #c4b5fd;">AI算力</span> — 英伟达产业链、寒武纪、海光信息、英维克
            </p>
            <p style="margin-top: 8px;"><strong>操作建议：</strong>
            AI主题经历前期调整后，近期催化事件密集（工博会AI+制造、阶跃开源、AI眼镜发售），
            有望迎来新一轮行情。建议关注预期差较大的AI硬件方向（AI眼镜/AR产业链），
            以及大模型开源带来的AI应用端机会。算力方向作为AI基础设施，长期逻辑不变，
            可逢调整加仓核心标的。</p>
        </div>
    </div>
    
    <div>
        <h3 style="color: #ec4899; font-size: 16px; font-weight: 700; margin-bottom: 10px; border-left: 3px solid #ec4899; padding-left: 10px;">
            五、三星Q3业绩暴增782.5%：存储超级周期全面确认
        </h3>
        <div style="padding: 12px 16px; background: rgba(255,255,255,0.03); border-radius: 10px;">
            <p style="margin-bottom: 8px;"><strong>事件：</strong>三星电子Q3营业利润107.4万亿韩元(约801.7亿美元)，同比暴增782.5%，环比增长20%，主要得益于AI芯片需求激增带动内存业务盈利强劲增长。HBM出货量环比增长近50%。</p>
            <p style="margin-bottom: 8px;"><strong>影响分析：</strong></p>
            <p style="margin-bottom: 6px; padding-left: 12px;"><strong>1. 存储超级周期全面确认，景气度持续超预期。</strong>三星作为全球存储龙头，其业绩表现是行业景气度的最佳风向标。
            Q3营业利润超800亿美元，同比暴增近8倍，且环比仍增长20%，说明存储行业的复苏强度和持续性远超市场预期。
            HBM出货量环比+50%是最亮眼的数据，AI对HBM的需求处于爆发式增长阶段。</p>
            <p style="margin-bottom: 6px; padding-left: 12px;"><strong>2. HBM产业链是最确定的增长方向。</strong>从三星、SK海力士到美光，全球三大存储厂商均在大幅扩产HBM，
            HBM3E、HBM4迭代加速。HBM产业链包括：上游材料（封装基板、TSV、导电胶）、
            中游封装（CoWoS、2.5D/3D封装）、下游应用（AI GPU、AI加速器）。
            国内厂商在HBM封测、材料领域加速突破。</p>
            <p style="margin-bottom: 6px; padding-left: 12px;"><strong>3. 存储全链条涨价延续。</strong>DRAM和NAND Flash价格持续上涨，
            原厂议价权强，下游接受度高。AI服务器需求是核心增量，
            同时传统领域（PC、手机）也在复苏，形成"AI+消费"双轮驱动。
            预计涨价周期至少延续至2027年。</p>
            <p style="margin-bottom: 8px;"><strong>受益标的：</strong></p>
            <p style="padding-left: 12px;">
                <span style="color: #f9a8d4;">HBM材料/封装</span> — 雅克科技、华海诚科、长电科技、通富微电、晶方科技<br>
                <span style="color: #f9a8d4;">存储芯片</span> — 兆易创新、北京君正、东芯股份、澜起科技<br>
                <span style="color: #f9a8d4;">存储设备/检测</span> — 精测电子、长川科技、华峰测控
            </p>
            <p style="margin-top: 8px;"><strong>操作建议：</strong>
            存储是当前A股最强的产业趋势之一，超级周期的逻辑不断被验证。
            三星Q3业绩再超预期，将进一步强化市场对存储板块的信心。
            建议逢回调加仓存储产业链，优先布局HBM材料和先进封装方向。
            雅克科技(002409)作为HBM前驱材料龙头，受益确定性高，当前价位值得关注。
            短期注意美股半导体板块波动对A股的传导影响。</p>
        </div>
    </div>
</div>
"""
deep_analysis_section = Section(title="💡 重点事件深度影响分析与操作建议", content=deep_analysis_html, icon="zap", variant="highlight")
gen._components.append(deep_analysis_section)

# 8. 催化深度分析（Skill增强）
gen.add_catalyst_deep_analysis([
    {'type': 'policy', 'title': '安森美涨价落地 · 功率半导体涨价周期',
     'description': 'ON Semiconductor全产品系列涨价10月10日生效，全球功率半导体大厂全线涨价，AI驱动供需紧张',
     'category': '半导体 · A级'},
    {'type': 'meeting', 'title': '上海工博会开幕 · 首次设立集成电路展',
     'description': '第26届中国国际工业博览会10月12日开幕，十大专业展，3000家展商，国芯展首次亮相',
     'category': '产业盛会 · S级'},
    {'type': 'general', 'title': '三星Q3业绩暴增 · 存储超级周期确认',
     'description': '三星电子Q3营业利润同比+782.5%，HBM出货量环比+50%，存储行业景气度全面确认',
     'category': '存储 · S级'},
])

# 9. 本周事件总览时间表
timeline_html = """
<div style="position: relative; padding-left: 20px;">
    <div style="position: absolute; left: 8px; top: 0; bottom: 0; width: 2px; background: linear-gradient(to bottom, #3b82f6, #8b5cf6, #ec4899); border-radius: 1px;"></div>
    
    <div style="position: relative; margin-bottom: 16px;">
        <div style="position: absolute; left: -20px; top: 4px; width: 14px; height: 14px; background: #f97316; border-radius: 50%; border: 2px solid #1e293b;"></div>
        <div style="font-weight: 600; color: #fdba74; font-size: 14px;">10月12日（周一）</div>
        <div style="font-size: 13px; color: #94a3b8; margin-top: 4px; line-height: 1.6;">
            • 第26届上海工博会开幕（国家会展中心）<br>
            • 陕西能源24亿股解禁（占总股本64%，约226亿）<br>
            • 金科股份18亿股解禁（重整财务投资人）<br>
            • 小鹏汽车巴黎全球新车发布会<br>
            • 京东"双11"活动全面开启<br>
            • 马士基紧急燃油附加费上调至20%生效
        </div>
    </div>
    
    <div style="position: relative; margin-bottom: 16px;">
        <div style="position: absolute; left: -20px; top: 4px; width: 14px; height: 14px; background: #3b82f6; border-radius: 50%; border: 2px solid #1e293b;"></div>
        <div style="font-weight: 600; color: #93c5fd; font-size: 14px;">10月13日（周二）</div>
        <div style="font-size: 13px; color: #94a3b8; margin-top: 4px; line-height: 1.6;">
            • 千问新一代AI眼镜现货发售<br>
            • 沪市首份三季报：有研新材发布<br>
            • 通则康威中签号公布(T+2)<br>
            • 第19届国际油脂油料大会开幕<br>
            • 日本9月PPI年率公布<br>
            • 美国9月成屋销售年化总数公布
        </div>
    </div>
    
    <div style="position: relative; margin-bottom: 16px;">
        <div style="position: absolute; left: -20px; top: 4px; width: 14px; height: 14px; background: #8b5cf6; border-radius: 50%; border: 2px solid #1e293b;"></div>
        <div style="font-weight: 600; color: #c4b5fd; font-size: 14px;">10月14日（周三）</div>
        <div style="font-size: 13px; color: #94a3b8; margin-top: 4px; line-height: 1.6;">
            • 中国9月CPI/PPI数据公布<br>
            • 美国9月核心CPI年率公布（关键！影响美联储加息预期）<br>
            • 2026人工智能产业大会开幕（济南）<br>
            • 2026湾区半导体产业生态博览会（湾芯展）开幕
        </div>
    </div>
    
    <div style="position: relative; margin-bottom: 16px;">
        <div style="position: absolute; left: -20px; top: 4px; width: 14px; height: 14px; background: #10b981; border-radius: 50%; border: 2px solid #1e293b;"></div>
        <div style="font-weight: 600; color: #6ee7b7; font-size: 14px;">10月15日（周四）</div>
        <div style="font-size: 13px; color: #94a3b8; margin-top: 4px; line-height: 1.6;">
            • 阶跃星辰Step 5 Preview正式开源<br>
            • 第140届广交会开幕（广州，持续至11月4日）<br>
            • 第23届中国国际住宅产业暨建筑工业化博览会
        </div>
    </div>
    
    <div style="position: relative;">
        <div style="position: absolute; left: -20px; top: 4px; width: 14px; height: 14px; background: #ec4899; border-radius: 50%; border: 2px solid #1e293b;"></div>
        <div style="font-weight: 600; color: #f9a8d4; font-size: 14px;">10月16日（周五）</div>
        <div style="font-size: 13px; color: #94a3b8; margin-top: 4px; line-height: 1.6;">
            • 上海工博会闭幕<br>
            • 湾芯展闭幕<br>
            • 人工智能产业大会闭幕<br>
            • 中国9月70城房价数据公布（预计）
        </div>
    </div>
</div>
"""
timeline_section = Section(title="📅 本周催化事件时间轴", content=timeline_html, icon="calendar")
gen._components.append(timeline_section)

# 10. 风险提示
gen.add_risk_warning([
    "陕西能源等大额解禁可能对相关个股及板块情绪造成短期冲击",
    "美国9月CPI数据若超预期，可能推升美联储加息预期，引发全球市场波动",
    "工博会、安森美涨价等事件存在预期兑现后获利回吐风险",
    "三星业绩虽超预期，但需警惕美股半导体板块波动向A股传导",
    "美联储12月加息概率已升至68%，全球流动性收紧压力持续",
    "三季报披露季开启，业绩不及预期的个股可能面临戴维斯双杀",
    "国内航线燃油附加费上调，航空板块成本端承压"
])

# 发布
print("开始生成并发布明日催化剂报告...")
result = gen.publish()
print(f"发布结果: {result}")
print("报告生成完成！")
