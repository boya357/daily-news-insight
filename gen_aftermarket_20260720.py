#!/usr/bin/env python3
"""生成 2026-07-20（周一）盘后速递 - V3.0统一标准"""
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'v3'))
os.chdir(os.path.dirname(os.path.abspath(__file__)))

from generators.aftermarket import AftermarketGenerator
from components.layout import Section

DATE = "20260720"
SUBTITLE = "2026.07.20 · 盘后速递 · 周一"

gen = AftermarketGenerator(date_str=DATE, subtitle=SUBTITLE)

# ============================================================
# 1. 今日核心亮点
# ============================================================
highlight = '''<div style="font-size: 14px; line-height: 1.7; color: var(--text-secondary);">
<p style="margin: 0 0 10px 0;"><strong style="color: #f87171;">📉 今日定性：指数红个股崩，科技成长股遭遇黑色星期一</strong>。上证指数收3796.28点(+0.85%)，深成指跌0.71%报13610.23，创业板指+0.42%，科创50+0.19%。但指数红盘完全是权重护盘假象——全市场超3700只个股下跌，502只跌停，1399只跌幅超5%，中位数下跌1.87%，平均股价暴跌3.84%，亏钱效应爆表。</p>
<p style="margin: 0 0 10px 0;"><strong style="color: #c084fc;">🔥 核心矛盾：极致高低切换，科技→防御的中期级再平衡</strong>。资金从高位科技赛道（半导体/存储/PCB/光模块/液冷）全面出逃，电子板块主力净流出118.45亿，半导体全产业链净流出114亿；与此同时，电力(+31亿)、煤炭、油气、白酒、银行保险等防御板块全线大涨，中国海油、茅台、兖矿能源等权重领涨。这不是短期轮动，而是中期级别的资金再平衡。</p>
<p style="margin: 0 0 10px 0;"><strong style="color: #60a5fa;">🐲 龙虎榜看点：机构跌停板抄底光模块</strong>。今日龙虎榜102只个股出现机构席位，机构合计净买入50.92亿，但分化剧烈——光迅科技跌停板获机构净买3.58亿+北向2.4亿，德明利跌停机构净买2.69亿，九安医疗机构净买2.29亿；而中国巨石被机构狂卖15.42亿，东山精密机构净卖5.13亿。游资方面，交易猿3.188亿抄底东山精密，宁波桑田路接力中船特气。</p>
<p style="margin: 0;"><strong style="color: #fb923c;">⚠️ 持仓预警：四只持仓全部跌停，组合单日暴击</strong>。英维克-9.92%跌停收55.46元（年内新低）、铜冠铜箔-20%20cm跌停收103.24元、雅克科技-10%四连跌收130.50元、*ST建艺-10%一字跌停收8.55元。组合从高位回撤幅度惊人，进入极高风险区间，必须严格执行止损纪律。</p>
</div>'''
gen.add_today_highlight(highlight)

# ============================================================
# 2. 市场收盘总结
# ============================================================
indices = [
    {"name": "上证指数", "value": "3796.28", "change": "+0.85%", "icon": "trending_up", "up": True},
    {"name": "深证成指", "value": "13610.23", "change": "-0.71%", "icon": "trending_down", "up": False},
    {"name": "创业板指", "value": "3443.10", "change": "+0.42%", "icon": "trending_up", "up": True},
    {"name": "科创50", "value": "1718.69", "change": "+0.19%", "icon": "trending_up", "up": True},
]
gen.add_market_summary(indices, volume="2.70万亿(放量470亿)", northbound="小幅净流入(结构性调仓)")

# ============================================================
# 3. 市场深度分析
# ============================================================
market_deep_html = '''
<div style="display: flex; flex-direction: column; gap: 16px;">
    <div style="background: var(--glass-bg); border: 1px solid var(--glass-border); border-radius: 12px; padding: 16px;">
        <div style="font-weight: 600; color: var(--text-primary); margin-bottom: 10px; display: flex; align-items: center; gap: 8px;">
            <span>🌡️</span><span>情绪温度计：极度恐慌，跌停潮再现</span>
        </div>
        <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 10px; font-size: 13px;">
            <div style="background: rgba(239, 68, 68, 0.1); border-radius: 8px; padding: 10px; text-align: center;">
                <div style="color: #fca5a5; font-size: 11px; margin-bottom: 4px;">上涨/下跌</div>
                <div style="color: var(--text-primary); font-size: 16px; font-weight: 700;">1700 / 3700+</div>
                <div style="color: var(--text-muted); font-size: 11px;">涨跌比0.46:1</div>
            </div>
            <div style="background: rgba(245, 158, 11, 0.1); border-radius: 8px; padding: 10px; text-align: center;">
                <div style="color: #fcd34d; font-size: 11px; margin-bottom: 4px;">涨停/跌停</div>
                <div style="color: var(--text-primary); font-size: 16px; font-weight: 700;">67 / 502</div>
                <div style="color: var(--text-muted); font-size: 11px;">跌停潮再现</div>
            </div>
            <div style="background: rgba(59, 130, 246, 0.1); border-radius: 8px; padding: 10px; text-align: center;">
                <div style="color: #93c5fd; font-size: 11px; margin-bottom: 4px;">主力资金</div>
                <div style="color: #f87171; font-size: 16px; font-weight: 700;">-609亿</div>
                <div style="color: var(--text-muted); font-size: 11px;">全市场净流出</div>
            </div>
            <div style="background: rgba(168, 85, 247, 0.1); border-radius: 8px; padding: 10px; text-align: center;">
                <div style="color: #d8b4fe; font-size: 11px; margin-bottom: 4px;">北向资金</div>
                <div style="color: #4ade80; font-size: 16px; font-weight: 700;">+370亿(成分股)</div>
                <div style="color: var(--text-muted); font-size: 11px;">买防御卖科技</div>
            </div>
        </div>
    </div>
    
    <div style="background: var(--glass-bg); border: 1px solid var(--glass-border); border-radius: 12px; padding: 16px;">
        <div style="font-weight: 600; color: var(--text-primary); margin-bottom: 10px; display: flex; align-items: center; gap: 8px;">
            <span>🧭</span><span>今日走势深度复盘</span>
        </div>
        <div style="color: var(--text-secondary); font-size: 13px; line-height: 1.8;">
            <p style="margin: 0 0 8px 0;"><strong style="color: #fbbf24;">【早盘】国家队增持利好，指数高开科技冲高</strong>：受周末国家队机构增持消息刺激，沪指高开0.8%，科技股一度集体冲高——半导体、存储、PCB开盘拉升，铜冠铜箔、德明利等早盘翻红。但高开即引发获利盘兑现，科技股冲高后快速回落。</p>
            <p style="margin: 0 0 8px 0;"><strong style="color: #4ade80;">【午前】风格切换加剧，防御板块全线走强</strong>：电力、煤炭、油气、白酒等防御板块持续拉升，中国海油涨停封板，贵州茅台涨超5%，立新能源3连板。资金从科技成长加速流向红利防御，跷跷板效应明显。</p>
            <p style="margin: 0 0 8px 0;"><strong style="color: #f87171;">【午后】科技股崩盘式下跌，跌停潮蔓延</strong>：午后科技板块加速跳水，德明利、铜冠铜箔、中船特气等20cm跌停，PCB、光刻机、存储芯片板块集体暴跌，全市场跌停家数突破500只。权重股尾盘发力护盘，三大指数先后翻红，但个股普跌格局未改。</p>
            <p style="margin: 0;"><strong style="color: #c084fc;">【收盘】指数红个股崩的极端割裂</strong>：沪指+0.85%、创业板+0.42%、科创50+0.19%，但3700+个股下跌、502只跌停，中位数下跌1.87%。典型的"权重掩护小票出货"行情，科技成长股遭遇系统性估值杀跌。</p>
        </div>
    </div>
    
    <div style="background: var(--glass-bg); border: 1px solid var(--glass-border); border-radius: 12px; padding: 16px;">
        <div style="font-weight: 600; color: var(--text-primary); margin-bottom: 10px; display: flex; align-items: center; gap: 8px;">
            <span>⚡</span><span>科技股集体崩盘的六大核心原因</span>
        </div>
        <div style="color: var(--text-secondary); font-size: 13px; line-height: 1.8;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #f87171;">1. 外围科技熊市传导：费城半导体进入技术性熊市</strong>：上周五费城半导体指数自高点回落超20%，英伟达、美光、台积电全线大跌。韩国股市今日暴跌4.4%，SK海力士较年内高点暴跌40%，三星跌34%，韩股超35万杠杆账户爆仓，负面情绪直接传导至A股科技板块。</p>
            <p style="margin: 0 0 6px 0;"><strong style="color: #f87171;">2. 融资盘爆仓负反馈：连续13日缩水2231亿</strong>：7月以来A股融资余额已连续13个交易日缩水，较6月末高点累计减少约2231亿元，电子、半导体等科技板块是融资净卖出重灾区，单板块融资净流出超500亿元。连续下跌触发平仓线，被动卖盘砸低股价形成恶性循环。</p>
            <p style="margin: 0 0 6px 0;"><strong style="color: #f87171;">3. 赛道筹码极度拥挤：机构持仓创2019年以来新高</strong>：2026年二季度主动权益基金中半导体产业链持仓占比达18.7%，创2019年科技牛市后新高。申万半导体指数累计涨幅112%，光刻机龙头超340%，获利盘体量巨大，集中兑现引发踩踏。</p>
            <p style="margin: 0 0 6px 0;"><strong style="color: #f87171;">4. 长鑫巨型IPO抽血：科创板史上最大IPO</strong>：长鑫科技IPO发行价8.66元，首发募资579亿超募至666亿，超过中芯国际成为科创板开板以来最大IPO。机构被动抛售流动性最好的半导体龙头腾挪打新资金，持续压制板块买盘。</p>
            <p style="margin: 0 0 6px 0;"><strong style="color: #f87171;">5. AI资本开支预期降温：Meta抛售算力冲击长期逻辑</strong>：Meta宣布对外出售闲置算力，大型数据中心项目搁置，市场担忧全球云厂商削减芯片采购。叠加Kimi K3大模型证明低算力可实现顶尖效果，"无限堆高端芯片"的算力涨价逻辑被动摇。</p>
            <p style="margin: 0;"><strong style="color: #f87171;">6. 中报业绩"利好出尽"：7家不及预期</strong>：中报预告密集披露期，17家半导体公司已有7家净利润增速低于市场一致预期，3家预告亏损。高估值没有业绩跟上成了砸盘由头，市场奉行"买预期、卖事实"。</p>
        </div>
    </div>
</div>
'''
gen._components.append(Section(title="🧭 市场深度分析", content=market_deep_html, icon="analytics"))

# ============================================================
# 4. 板块涨跌幅排行
# ============================================================
up_sectors = [
    {"name": "石油石化", "change": "+5.82%"},
    {"name": "煤炭开采", "change": "+4.96%"},
    {"name": "电力", "change": "+4.35%"},
    {"name": "白酒", "change": "+3.78%"},
    {"name": "银行", "change": "+2.64%"},
    {"name": "保险", "change": "+2.41%"},
    {"name": "油气开采", "change": "+5.12%"},
    {"name": "船舶制造", "change": "+3.26%"},
    {"name": "电信运营", "change": "+2.18%"},
    {"name": "创新药", "change": "+2.05%"},
]

down_sectors = [
    {"name": "PCB", "change": "-8.72%"},
    {"name": "铜箔", "change": "-9.35%"},
    {"name": "存储芯片", "change": "-7.56%"},
    {"name": "光刻机", "change": "-8.13%"},
    {"name": "CPO/光模块", "change": "-6.89%"},
]

gen.add_sector_performance(up_sectors, down_sectors)

# ============================================================
# 5. 板块深度分析
# ============================================================
sector_deep_html = '''
<div style="display: flex; flex-direction: column; gap: 16px;">
    
    <div style="background: linear-gradient(135deg, rgba(16,185,129,0.12) 0%, rgba(5,150,105,0.08) 100%); border: 1px solid rgba(16,185,129,0.3); border-radius: 16px; padding: 20px;">
        <div style="font-size: 15px; font-weight: 700; color: #10b981; margin-bottom: 14px;">📈 领涨板块深度解析</div>
        
        <div style="background: var(--glass-bg); border-radius: 12px; padding: 14px; margin-bottom: 12px;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                <span style="font-weight: 600; color: var(--text-primary);">⚡ 电力板块 +4.35%</span>
                <span style="color: #10b981; font-weight: 700;">主力+31亿</span>
            </div>
            <div style="font-size: 13px; color: var(--text-secondary); line-height: 1.7;">
                <p style="margin: 0 0 4px 0;"><strong>龙头：</strong>立新能源(3连板)、华银电力(2连板)、乐山电力(2连板)、桂冠电力(2连板)、大唐发电涨停</p>
                <p style="margin: 0 0 4px 0;"><strong>逻辑：</strong>江苏等地用电负荷刷新历史纪录，夏季用电高峰需求确定；电力改革深化+超超临界发电概念催化；高股息防御属性获避险资金青睐</p>
                <p style="margin: 0;"><strong>持续性判断：★★★★☆</strong> 高温天气持续+业绩确定性强+资金流入明确，短期有望延续，但连板股需警惕追高风险</p>
            </div>
        </div>
        
        <div style="background: var(--glass-bg); border-radius: 12px; padding: 14px; margin-bottom: 12px;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                <span style="font-weight: 600; color: var(--text-primary);">🛢️ 石油石化 +5.82%</span>
                <span style="color: #10b981; font-weight: 700;">领涨全市场</span>
            </div>
            <div style="font-size: 13px; color: var(--text-secondary); line-height: 1.7;">
                <p style="margin: 0 0 4px 0;"><strong>龙头：</strong>中国海油涨停、中国石油+7%、中曼石油涨停、博迈科涨停</p>
                <p style="margin: 0 0 4px 0;"><strong>逻辑：</strong>霍尔木兹海峡局势紧张引发原油供应恐慌，国际油价飙升；高股息+中特估估值修复双轮驱动；地缘冲突加剧下的避险配置</p>
                <p style="margin: 0;"><strong>持续性判断：★★★★☆</strong> 地缘风险未解除+油价上行周期确认，趋势性行情，回调即是低吸机会</p>
            </div>
        </div>
        
        <div style="background: var(--glass-bg); border-radius: 12px; padding: 14px; margin-bottom: 12px;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                <span style="font-weight: 600; color: var(--text-primary);">⛏️ 煤炭开采 +4.96%</span>
                <span style="color: #10b981; font-weight: 700;">多股涨停</span>
            </div>
            <div style="font-size: 13px; color: var(--text-secondary); line-height: 1.7;">
                <p style="margin: 0 0 4px 0;"><strong>龙头：</strong>淮北矿业、大有能源、兖矿能源、中煤能源涨停</p>
                <p style="margin: 0 0 4px 0;"><strong>逻辑：</strong>迎峰度夏推高火电需求；国内安监高压致供给收缩；油价上涨带动煤炭替代价值；高股息防御属性</p>
                <p style="margin: 0;"><strong>持续性判断：★★★★☆</strong> 夏季用电高峰+供给收缩+高股息三重逻辑，中期趋势向好</p>
            </div>
        </div>
        
        <div style="background: var(--glass-bg); border-radius: 12px; padding: 14px;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                <span style="font-weight: 600; color: var(--text-primary);">🍷 白酒 +3.78%</span>
                <span style="color: #10b981; font-weight: 700;">茅台领涨</span>
            </div>
            <div style="font-size: 13px; color: var(--text-secondary); line-height: 1.7;">
                <p style="margin: 0 0 4px 0;"><strong>龙头：</strong>贵州茅台+5.6%(获32亿净流入)、古井贡酒涨停(4天2板)</p>
                <p style="margin: 0 0 4px 0;"><strong>逻辑：</strong>茅台提价预期催化消费复苏；避险资金抱团核心资产；消费板块估值处于历史低位</p>
                <p style="margin: 0;"><strong>持续性判断：★★★☆☆</strong> 超跌反弹+避险需求，中期持续性需观察消费数据验证</p>
            </div>
        </div>
    </div>
    
    <div style="background: linear-gradient(135deg, rgba(239,68,68,0.12) 0%, rgba(220,38,38,0.08) 100%); border: 1px solid rgba(239,68,68,0.3); border-radius: 16px; padding: 20px;">
        <div style="font-size: 15px; font-weight: 700; color: #ef4444; margin-bottom: 14px;">📉 领跌板块深度解析</div>
        
        <div style="background: var(--glass-bg); border-radius: 12px; padding: 14px; margin-bottom: 12px;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                <span style="font-weight: 600; color: var(--text-primary);">🟢 PCB板块 -8.72%</span>
                <span style="color: #ef4444; font-weight: 700;">批量跌停</span>
            </div>
            <div style="font-size: 13px; color: var(--text-secondary); line-height: 1.7;">
                <p style="margin: 0 0 4px 0;"><strong>领跌：</strong>东山精密跌停、金安国纪跌停、沪电股份跌停、深南电路跌停</p>
                <p style="margin: 0 0 4px 0;"><strong>原因：</strong>AI服务器PCB需求预期下修；前期涨幅过大获利盘集中兑现；PCB板块估值处于历史高位，业绩增速跟不上股价</p>
                <p style="margin: 0;"><strong>持续性判断：★★★☆☆</strong> 短期杀跌动能仍强，但机构跌停板抄底光迅科技显示部分机构开始布局，关注企稳信号</p>
            </div>
        </div>
        
        <div style="background: var(--glass-bg); border-radius: 12px; padding: 14px; margin-bottom: 12px;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                <span style="font-weight: 600; color: var(--text-primary);">💾 存储芯片 -7.56%</span>
                <span style="color: #ef4444; font-weight: 700;">板块重挫</span>
            </div>
            <div style="font-size: 13px; color: var(--text-secondary); line-height: 1.7;">
                <p style="margin: 0 0 4px 0;"><strong>领跌：</strong>德明利(4连板跌停)、铜冠铜箔20cm跌停、兆易创新-6.66%</p>
                <p style="margin: 0 0 4px 0;"><strong>原因：</strong>SK海力士暴跌40%引发全球存储链恐慌；长鑫IPO抽血效应；中报"利好出尽"；融资盘爆仓负反馈</p>
                <p style="margin: 0;"><strong>持续性判断：★★★★☆</strong> 外围下跌未止+融资盘平仓未完+获利盘仍在兑现，短期继续下行概率大，不宜抄底</p>
            </div>
        </div>
        
        <div style="background: var(--glass-bg); border-radius: 12px; padding: 14px;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                <span style="font-weight: 600; color: var(--text-primary);">🔬 光刻机 -8.13%</span>
                <span style="color: #ef4444; font-weight: 700;">板块暴跌</span>
            </div>
            <div style="font-size: 13px; color: var(--text-secondary); line-height: 1.7;">
                <p style="margin: 0 0 4px 0;"><strong>领跌：</strong>中船特气20cm跌停、茂莱光学20cm跌停、博迁新材跌停</p>
                <p style="margin: 0 0 4px 0;"><strong>原因：</strong>光刻机部件价格骤降引发产业链担忧；前期涨幅最大(龙头+340%)回撤也最猛；监管重点监控高位次新股</p>
                <p style="margin: 0;"><strong>持续性判断：★★★★☆</strong> 高位题材股泡沫破裂，估值回归之路漫长，坚决回避</p>
            </div>
        </div>
    </div>
    
</div>
'''
gen._components.append(Section(title="🏢 板块深度分析", content=sector_deep_html, icon="building"))

# ============================================================
# 6. 持仓股深度诊断
# ============================================================
holdings_html = '''
<div style="display: flex; flex-direction: column; gap: 16px;">
    
    <!-- 英维克 -->
    <div style="background: var(--glass-bg); border: 1px solid var(--glass-border); border-radius: 16px; padding: 20px; backdrop-filter: blur(10px);">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 14px;">
            <div>
                <span style="font-size: 18px; font-weight: 700; color: var(--text-primary);">英维克 002837</span>
                <span style="margin-left: 8px; padding: 2px 10px; background: rgba(239,68,68,0.2); color: #f87171; border-radius: 12px; font-size: 12px; font-weight: 600;">🔴 跌停</span>
            </div>
            <div style="text-align: right;">
                <div style="font-size: 22px; font-weight: 800; color: #ef4444;">55.46元</div>
                <div style="font-size: 14px; color: #ef4444; font-weight: 600;">-9.92%</div>
            </div>
        </div>
        
        <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 8px; margin-bottom: 14px;">
            <div style="background: rgba(0,0,0,0.2); border-radius: 8px; padding: 8px; text-align: center;">
                <div style="font-size: 11px; color: var(--text-muted);">成交额</div>
                <div style="font-size: 14px; font-weight: 600; color: var(--text-primary);">31.37亿</div>
            </div>
            <div style="background: rgba(0,0,0,0.2); border-radius: 8px; padding: 8px; text-align: center;">
                <div style="font-size: 11px; color: var(--text-muted);">换手率</div>
                <div style="font-size: 14px; font-weight: 600; color: var(--text-primary);">4.74%</div>
            </div>
            <div style="background: rgba(0,0,0,0.2); border-radius: 8px; padding: 8px; text-align: center;">
                <div style="font-size: 11px; color: var(--text-muted);">最高/最低</div>
                <div style="font-size: 14px; font-weight: 600; color: var(--text-primary);">63.61/55.41</div>
            </div>
            <div style="background: rgba(0,0,0,0.2); border-radius: 8px; padding: 8px; text-align: center;">
                <div style="font-size: 11px; color: var(--text-muted);">主力资金</div>
                <div style="font-size: 14px; font-weight: 600; color: #f87171;">-3.82亿</div>
            </div>
        </div>
        
        <div style="font-size: 13px; color: var(--text-secondary); line-height: 1.8;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #fbbf24;">【技术面判断】放量跌停，年内新低，下降趋势完全失控</strong>：今日开盘62.80元，最高63.61元，最低55.41元，收盘55.46元跌停，再创年内新低。从年内高点118.80元计算，累计跌幅已达53.3%，腰斩有余。所有均线呈完全空头排列，5日、10日、20日、60日均线全部向下发散。今日跌停封单超10万手，封板力度强，短期下方已无明显支撑。</p>
            <p style="margin: 0 0 6px 0;"><strong style="color: #60a5fa;">【资金面分析】机构加速出逃，散户接盘</strong>：今日主力净流出3.82亿元，近5日净流出8.71亿，近20日净流出29.56亿。超大单净流出3.13亿，显示机构仍在加速出货。北向资金今日继续减持液冷板块，英维克作为前期抱团标的，筹码松动严重。融资余额较上月下降8.3%，融资盘平仓加速了下跌。</p>
            <p style="margin: 0 0 6px 0;"><strong style="color: #c084fc;">【产业面评估】长期逻辑仍在，短期情绪崩溃</strong>：AI液冷长期需求逻辑并未改变——数据中心建设仍在加速，液冷渗透率持续提升。但短期市场风格剧烈切换，科技成长股遭遇系统性估值杀跌，液冷板块整体跌幅超25%。公司基本面没有出现重大恶化，但估值压缩过程可能持续。</p>
            <p style="margin: 0 0 6px 0;"><strong style="color: #f87171;">【操作建议：无条件清仓止损】</strong>：<strong>成本104.23元，当前55.46元，亏损46.8%，已深度跌破止损位98元</strong>。虽然亏损巨大，但纪律就是纪律——下降趋势完全确立，继续持有可能面临更大亏损。明日开盘第一时间无条件清仓止损离场，不要抱有任何反弹幻想。现金为王，等待市场真正企稳后再考虑重新布局。</p>
            <p style="margin: 0;">
                <span style="background: rgba(239,68,68,0.15); color: #f87171; padding: 4px 10px; border-radius: 8px; font-weight: 600;">🔴 止损位：98元(已跌破-46.8%)</span>
                <span style="margin-left: 8px; background: rgba(245,158,11,0.15); color: #fbbf24; padding: 4px 10px; border-radius: 8px; font-weight: 600;">📉 压力位：60元</span>
                <span style="margin-left: 8px; background: rgba(16,185,129,0.15); color: #10b981; padding: 4px 10px; border-radius: 8px; font-weight: 600;">⚠️ 操作：明日开盘清仓</span>
            </p>
        </div>
    </div>
    
    <!-- 铜冠铜箔 -->
    <div style="background: var(--glass-bg); border: 1px solid var(--glass-border); border-radius: 16px; padding: 20px; backdrop-filter: blur(10px);">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 14px;">
            <div>
                <span style="font-size: 18px; font-weight: 700; color: var(--text-primary);">铜冠铜箔 301217</span>
                <span style="margin-left: 8px; padding: 2px 10px; background: rgba(239,68,68,0.2); color: #f87171; border-radius: 12px; font-size: 12px; font-weight: 600;">🔴 20cm跌停</span>
            </div>
            <div style="text-align: right;">
                <div style="font-size: 22px; font-weight: 800; color: #ef4444;">103.24元</div>
                <div style="font-size: 14px; color: #ef4444; font-weight: 600;">-20.00%</div>
            </div>
        </div>
        
        <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 8px; margin-bottom: 14px;">
            <div style="background: rgba(0,0,0,0.2); border-radius: 8px; padding: 8px; text-align: center;">
                <div style="font-size: 11px; color: var(--text-muted);">成交额</div>
                <div style="font-size: 14px; font-weight: 600; color: var(--text-primary);">26.66亿</div>
            </div>
            <div style="background: rgba(0,0,0,0.2); border-radius: 8px; padding: 8px; text-align: center;">
                <div style="font-size: 11px; color: var(--text-muted);">换手率</div>
                <div style="font-size: 14px; font-weight: 600; color: var(--text-primary);">3.02%</div>
            </div>
            <div style="background: rgba(0,0,0,0.2); border-radius: 8px; padding: 8px; text-align: center;">
                <div style="font-size: 11px; color: var(--text-muted);">最高/最低</div>
                <div style="font-size: 14px; font-weight: 600; color: var(--text-primary);">119.00/103.24</div>
            </div>
            <div style="background: rgba(0,0,0,0.2); border-radius: 8px; padding: 8px; text-align: center;">
                <div style="font-size: 11px; color: var(--text-muted);">主力资金</div>
                <div style="font-size: 14px; font-weight: 600; color: #f87171;">-2.69亿</div>
            </div>
        </div>
        
        <div style="font-size: 13px; color: var(--text-secondary); line-height: 1.8;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #fbbf24;">【技术面判断】20cm一字闷杀，从逆势翻红到直接崩盘</strong>：今日开盘112.63元，最高119.00元（一度翻红），但随后快速跳水，午后封死20cm跌停板，最低103.24元。从周五逆势翻红到今日一字闷杀，走势极为极端。从年内高点176.80元计算，累计跌幅已达41.6%。今日跌停封单超3万手，成交额26.66亿显示有资金翘板但失败，短期动能极强。</p>
            <p style="margin: 0 0 6px 0;"><strong style="color: #60a5fa;">【资金面分析】机构持续兑现，浮盈大幅缩水</strong>：今日主力净流出2.69亿元，近5日净流出3.46亿，近10日净流出23.40亿，近20日净流出95.95亿。超大单净流出2.22亿，机构持续加速兑现获利筹码。成本87.16元，当前浮盈从最高+103%骤缩至仅+18%，利润回吐严重。</p>
            <p style="margin: 0 0 6px 0;"><strong style="color: #c084fc;">【产业面评估】HBM铜箔长期逻辑仍在，但板块情绪极差</strong>：存储HBM铜箔需求长期逻辑仍然成立——HBM3/HBM4加速渗透带动高端铜箔需求爆发，公司作为国内铜箔龙头直接受益。但短期存储板块全线重挫，SK海力士暴跌40%引发全球存储链恐慌，铜箔/PCB/存储产业链全线下杀，获利盘集中兑现压力巨大。</p>
            <p style="margin: 0 0 6px 0;"><strong style="color: #f87171;">【操作建议：开板即减仓，守住利润底线】</strong>：<strong>成本87.16元，当前103.24元，浮盈+18%（从+48%大幅回撤）</strong>。20cm跌停显示杀跌动能极强，明日若开板立即减仓2/3，只留底仓观察。若跌破90元则止盈清仓离场，确保至少守住+3%的底线利润。HBM铜箔长期逻辑不变，但短期板块调整远未结束，先保命再谈收益。</p>
            <p style="margin: 0;">
                <span style="background: rgba(239,68,68,0.15); color: #f87171; padding: 4px 10px; border-radius: 8px; font-weight: 600;">🔴 止盈位：90元</span>
                <span style="margin-left: 8px; background: rgba(245,158,11,0.15); color: #fbbf24; padding: 4px 10px; border-radius: 8px; font-weight: 600;">📉 减仓位：110元以上减2/3</span>
                <span style="margin-left: 8px; background: rgba(16,185,129,0.15); color: #10b981; padding: 4px 10px; border-radius: 8px; font-weight: 600;">⚠️ 操作：开板即减仓</span>
            </p>
        </div>
    </div>
    
    <!-- 雅克科技 -->
    <div style="background: var(--glass-bg); border: 1px solid var(--glass-border); border-radius: 16px; padding: 20px; backdrop-filter: blur(10px);">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 14px;">
            <div>
                <span style="font-size: 18px; font-weight: 700; color: var(--text-primary);">雅克科技 002409</span>
                <span style="margin-left: 8px; padding: 2px 10px; background: rgba(239,68,68,0.2); color: #f87171; border-radius: 12px; font-size: 12px; font-weight: 600;">🔴 四连跌跌停</span>
            </div>
            <div style="text-align: right;">
                <div style="font-size: 22px; font-weight: 800; color: #ef4444;">130.50元</div>
                <div style="font-size: 14px; color: #ef4444; font-weight: 600;">-10.00%</div>
            </div>
        </div>
        
        <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 8px; margin-bottom: 14px;">
            <div style="background: rgba(0,0,0,0.2); border-radius: 8px; padding: 8px; text-align: center;">
                <div style="font-size: 11px; color: var(--text-muted);">成交额</div>
                <div style="font-size: 14px; font-weight: 600; color: var(--text-primary);">36.54亿</div>
            </div>
            <div style="background: rgba(0,0,0,0.2); border-radius: 8px; padding: 8px; text-align: center;">
                <div style="font-size: 11px; color: var(--text-muted);">换手率</div>
                <div style="font-size: 14px; font-weight: 600; color: var(--text-primary);">8.21%</div>
            </div>
            <div style="background: rgba(0,0,0,0.2); border-radius: 8px; padding: 8px; text-align: center;">
                <div style="font-size: 11px; color: var(--text-muted);">最高/最低</div>
                <div style="font-size: 14px; font-weight: 600; color: var(--text-primary);">150.00/130.50</div>
            </div>
            <div style="background: rgba(0,0,0,0.2); border-radius: 8px; padding: 8px; text-align: center;">
                <div style="font-size: 11px; color: var(--text-muted);">主力资金</div>
                <div style="font-size: 14px; font-weight: 600; color: #f87171;">-0.96亿</div>
            </div>
        </div>
        
        <div style="font-size: 13px; color: var(--text-secondary); line-height: 1.8;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #fbbf24;">【技术面判断】四连跌跌停，从209元高位回撤37.6%</strong>：今日开盘149.11元，最高150.00元，最低130.50元，收盘130.50元跌停。连续四个交易日下跌，从7月15日最高点209.00元计算，短短4个交易日累计跌幅达37.6%，回撤速度极快。成交额36.54亿创近期天量，换手率8.21%显示筹码大规模交换。短期均线全部拐头向下，MACD死叉放量，下降动能强劲。</p>
            <p style="margin: 0 0 6px 0;"><strong style="color: #60a5fa;">【资金面分析】机构连续出货，融资盘减仓</strong>：今日主力净流出0.96亿元，近5日净流出27.73亿，近10日净流出30.23亿，近20日净流出57.63亿。机构连续多日出货，融资余额下降2.56%。但值得注意的是，今日龙虎榜显示部分机构在跌停板上开始抄底半导体材料标的，雅克科技作为HBM前驱体龙头可能获得长线资金关注。</p>
            <p style="margin: 0 0 6px 0;"><strong style="color: #c084fc;">【产业面评估】HBM前驱体国产替代逻辑仍然坚硬</strong>：公司是国内HBM前驱体绝对龙头，行业地位稳固，国产替代逻辑长期不变。HBM3/HBM4加速渗透带动前驱体需求持续增长，公司业绩确定性强。但短期科技成长股遭遇系统性估值重估，HBM/先进封装/半导体材料全线杀跌，板块情绪崩溃。</p>
            <p style="margin: 0 0 6px 0;"><strong style="color: #f87171;">【操作建议：反弹减仓至底仓，破位止盈离场】</strong>：<strong>成本108.80元，当前130.50元，浮盈+20%（从+92%大幅回撤）</strong>。四连跌停后短期可能有技术性反弹，反弹至135-140元区间坚决减仓2/3，只留底仓观察。若跌破120元整数关口则止盈清仓，确保至少守住+10%利润。HBM前驱体龙头长期价值仍在，但需等待板块情绪企稳后再考虑回补。</p>
            <p style="margin: 0;">
                <span style="background: rgba(239,68,68,0.15); color: #f87171; padding: 4px 10px; border-radius: 8px; font-weight: 600;">🔴 止盈位：120元</span>
                <span style="margin-left: 8px; background: rgba(245,158,11,0.15); color: #fbbf24; padding: 4px 10px; border-radius: 8px; font-weight: 600;">📉 减仓位：135-140元减2/3</span>
                <span style="margin-left: 8px; background: rgba(16,185,129,0.15); color: #10b981; padding: 4px 10px; border-radius: 8px; font-weight: 600;">⚠️ 操作：反弹减仓</span>
            </p>
        </div>
    </div>
    
    <!-- *ST建艺 -->
    <div style="background: var(--glass-bg); border: 1px solid var(--glass-border); border-radius: 16px; padding: 20px; backdrop-filter: blur(10px);">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 14px;">
            <div>
                <span style="font-size: 18px; font-weight: 700; color: var(--text-primary);">*ST建艺 002789</span>
                <span style="margin-left: 8px; padding: 2px 10px; background: rgba(239,68,68,0.2); color: #f87171; border-radius: 12px; font-size: 12px; font-weight: 600;">🔴 一字跌停</span>
            </div>
            <div style="text-align: right;">
                <div style="font-size: 22px; font-weight: 800; color: #ef4444;">8.55元</div>
                <div style="font-size: 14px; color: #ef4444; font-weight: 600;">-10.00%</div>
            </div>
        </div>
        
        <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 8px; margin-bottom: 14px;">
            <div style="background: rgba(0,0,0,0.2); border-radius: 8px; padding: 8px; text-align: center;">
                <div style="font-size: 11px; color: var(--text-muted);">成交额</div>
                <div style="font-size: 14px; font-weight: 600; color: var(--text-primary);">4105万</div>
            </div>
            <div style="background: rgba(0,0,0,0.2); border-radius: 8px; padding: 8px; text-align: center;">
                <div style="font-size: 11px; color: var(--text-muted);">换手率</div>
                <div style="font-size: 14px; font-weight: 600; color: var(--text-primary);">2.87%</div>
            </div>
            <div style="background: rgba(0,0,0,0.2); border-radius: 8px; padding: 8px; text-align: center;">
                <div style="font-size: 11px; color: var(--text-muted);">最高/最低</div>
                <div style="font-size: 14px; font-weight: 600; color: var(--text-primary);">9.83/8.55</div>
            </div>
            <div style="background: rgba(0,0,0,0.2); border-radius: 8px; padding: 8px; text-align: center;">
                <div style="font-size: 11px; color: var(--text-muted);">主力资金</div>
                <div style="font-size: 14px; font-weight: 600; color: #f87171;">-802万</div>
            </div>
        </div>
        
        <div style="font-size: 13px; color: var(--text-secondary); line-height: 1.8;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #fbbf24;">【技术面判断】连续跌停，退市风险下流动性濒临枯竭</strong>：今日开盘9.50元，最高9.83元，最低8.55元，收盘8.55元一字跌停。成交额仅4105万，换手率2.87%，显示买盘极度匮乏。从年内高点16.80元计算，累计跌幅已达49.1%，接近腰斩。下降通道完整，连续跌停模式，短期看不到止跌迹象。</p>
            <p style="margin: 0 0 6px 0;"><strong style="color: #60a5fa;">【资金面分析】大资金持续出逃，散户抄底接盘</strong>：今日主力净流出802万元，近5日净流出869万，近20日净流出1.05亿。大资金持续出逃，散户还在抄底接盘。ST板块整体低迷，退市风险股遭到资金抛弃。</p>
            <p style="margin: 0 0 6px 0;"><strong style="color: #c084fc;">【产业面评估】建筑装饰行业低迷，公司基本面持续恶化</strong>：建筑装饰行业整体低迷，地产链风险持续传导。公司债务问题+诉讼缠身+业绩亏损，多重利空叠加，退市风险持续发酵。基本面没有任何改善迹象，反而在持续恶化。</p>
            <p style="margin: 0 0 6px 0;"><strong style="color: #f87171;">【操作建议：坚决清仓，关闭退市风险敞口】</strong>：<strong>成本13.45元，当前8.55元，亏损-36.4%，已深度跌破止损位12.5元</strong>。*ST股票退市风险极高，继续持有可能面临更大亏损乃至退市归零。明日若开板坚决清仓离场，不要有任何侥幸心理。退市风险敞口必须立即关闭，这是投资纪律的底线。</p>
            <p style="margin: 0;">
                <span style="background: rgba(239,68,68,0.15); color: #f87171; padding: 4px 10px; border-radius: 8px; font-weight: 600;">🔴 止损位：12.5元(已跌破-36.4%)</span>
                <span style="margin-left: 8px; background: rgba(245,158,11,0.15); color: #fbbf24; padding: 4px 10px; border-radius: 8px; font-weight: 600;">📉 压力位：9.5元</span>
                <span style="margin-left: 8px; background: rgba(16,185,129,0.15); color: #10b981; padding: 4px 10px; border-radius: 8px; font-weight: 600;">⚠️ 操作：开板即清仓</span>
            </p>
        </div>
    </div>
    
</div>
'''
gen._components.append(Section(title="💼 持仓股深度诊断", content=holdings_html, icon="briefcase"))

# ============================================================
# 7. 龙虎榜深度解读
# ============================================================
longhubang_html = '''
<div style="display: flex; flex-direction: column; gap: 16px;">
    
    <div style="background: var(--glass-bg); border: 1px solid var(--glass-border); border-radius: 16px; padding: 18px;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
            <span style="font-size: 16px; font-weight: 700; color: var(--text-primary);">📊 龙虎榜全景数据</span>
            <span style="font-size: 12px; color: var(--text-muted);">2026-07-20</span>
        </div>
        <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 10px; font-size: 12px;">
            <div style="background: rgba(0,0,0,0.2); border-radius: 8px; padding: 10px; text-align: center;">
                <div style="color: var(--text-muted); margin-bottom: 4px;">上榜个股</div>
                <div style="font-size: 18px; font-weight: 700; color: var(--text-primary);">102只</div>
            </div>
            <div style="background: rgba(0,0,0,0.2); border-radius: 8px; padding: 10px; text-align: center;">
                <div style="color: var(--text-muted); margin-bottom: 4px;">机构净买入</div>
                <div style="font-size: 18px; font-weight: 700; color: #4ade80;">+50.92亿</div>
            </div>
            <div style="background: rgba(0,0,0,0.2); border-radius: 8px; padding: 10px; text-align: center;">
                <div style="color: var(--text-muted); margin-bottom: 4px;">机构净买/净卖</div>
                <div style="font-size: 14px; font-weight: 600; color: var(--text-primary);">59只 / 43只</div>
            </div>
            <div style="background: rgba(0,0,0,0.2); border-radius: 8px; padding: 10px; text-align: center;">
                <div style="color: var(--text-muted); margin-bottom: 4px;">市场情绪</div>
                <div style="font-size: 14px; font-weight: 600; color: #f87171;">恐慌(20分)</div>
            </div>
        </div>
    </div>
    
    <!-- 光迅科技 -->
    <div style="background: linear-gradient(135deg, rgba(59,130,246,0.12) 0%, rgba(147,51,234,0.08) 100%); border: 1px solid rgba(59,130,246,0.3); border-radius: 16px; padding: 18px;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
            <div>
                <span style="font-size: 16px; font-weight: 700; color: var(--text-primary);">光迅科技 002281</span>
                <span style="margin-left: 8px; padding: 2px 8px; background: rgba(239,68,68,0.2); color: #f87171; border-radius: 10px; font-size: 11px; font-weight: 600;">跌停</span>
            </div>
            <div style="text-align: right;">
                <span style="color: #4ade80; font-weight: 700;">机构净买 +3.58亿</span>
            </div>
        </div>
        <div style="font-size: 13px; color: var(--text-secondary); line-height: 1.7;">
            <p style="margin: 0 0 5px 0;"><strong>席位分析：</strong>机构专用席位净买入3.58亿元（机构买入第一名），北向资金（深股通）净买入2.40亿元。全天换手率5.87%，成交额80.72亿元。跌停板上获得机构+北向合计近6亿资金抄底，显示长线资金对光模块龙头的认可。</p>
            <p style="margin: 0 0 5px 0;"><strong>题材属性：</strong>光模块/CPO龙头，AI算力核心标的。今日光模块板块集体大跌，但光迅科技作为行业龙头获得机构逆势加仓。</p>
            <p style="margin: 0;"><strong>持续性判断：★★★☆☆</strong> 机构跌停板抄底是积极信号，但板块整体调整趋势未改，短期可能继续探底。长线资金建仓不代表股价马上反弹，需观察后续量价配合。关注10日均线压力。</p>
        </div>
    </div>
    
    <!-- 德明利 -->
    <div style="background: linear-gradient(135deg, rgba(245,158,11,0.12) 0%, rgba(239,68,68,0.08) 100%); border: 1px solid rgba(245,158,11,0.3); border-radius: 16px; padding: 18px;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
            <div>
                <span style="font-size: 16px; font-weight: 700; color: var(--text-primary);">德明利 001309</span>
                <span style="margin-left: 8px; padding: 2px 8px; background: rgba(239,68,68,0.2); color: #f87171; border-radius: 10px; font-size: 11px; font-weight: 600;">4连跌停</span>
            </div>
            <div style="text-align: right;">
                <span style="color: #4ade80; font-weight: 700;">机构净买 +2.69亿</span>
            </div>
        </div>
        <div style="font-size: 13px; color: var(--text-secondary); line-height: 1.7;">
            <p style="margin: 0 0 5px 0;"><strong>席位分析：</strong>机构专用席位净买入2.69亿元（机构买入第二名），北向资金净买入2.19亿元。但龙虎榜净卖出额排名第一(-8.44亿)，游资席位大举出逃——欢乐海岸净买入6182万试图翘板但失败。全天换手率10.76%，成交额85.97亿元。</p>
            <p style="margin: 0 0 5px 0;"><strong>题材属性：</strong>存储芯片主控芯片龙头，前期暴涨5倍的大牛股，存储板块人气标的。连续4个跌停，从高点回撤超过40%。</p>
            <p style="margin: 0;"><strong>持续性判断：★★☆☆☆</strong> 虽然机构逆势抄底，但连续跌停后抛压仍然沉重，游资出逃坚决。存储板块整体仍在下行通道，短期难以快速反转。激进投资者可在开板后观察换手率和承接力度，稳健投资者继续观望。</p>
        </div>
    </div>
    
    <!-- 东山精密 -->
    <div style="background: linear-gradient(135deg, rgba(168,85,247,0.12) 0%, rgba(236,72,153,0.08) 100%); border: 1px solid rgba(168,85,247,0.3); border-radius: 16px; padding: 18px;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
            <div>
                <span style="font-size: 16px; font-weight: 700; color: var(--text-primary);">东山精密 002384</span>
                <span style="margin-left: 8px; padding: 2px 8px; background: rgba(239,68,68,0.2); color: #f87171; border-radius: 10px; font-size: 11px; font-weight: 600;">跌停</span>
            </div>
            <div style="text-align: right;">
                <span style="color: #f87171; font-weight: 700;">机构净卖 -5.13亿</span>
            </div>
        </div>
        <div style="font-size: 13px; color: var(--text-secondary); line-height: 1.7;">
            <p style="margin: 0 0 5px 0;"><strong>席位分析：</strong>龙虎榜净买入额排名第三(+7.27亿)，但机构专用席位净卖出5.13亿元（机构卖出第二名）。北向资金（深股通）净买入6.48亿元（深股通净买入第一名），交易猿席位净买入3.188亿抄底。机构卖出、北向+游资买入，多空分歧巨大。</p>
            <p style="margin: 0 0 5px 0;"><strong>题材属性：</strong>PCB/FPC龙头，AI服务器核心供应链标的。今日PCB板块集体跌停，东山精密作为行业龙头首当其冲。</p>
            <p style="margin: 0;"><strong>持续性判断：★★☆☆☆</strong> 机构大幅卖出是负面信号，但北向资金和顶级游资同时抄底说明底部有承接力。多空分歧巨大意味着短期波动率会很高。关注200元整数关口的支撑力度，若能守住可能迎来技术性反弹。</p>
        </div>
    </div>
    
    <!-- 九安医疗 -->
    <div style="background: linear-gradient(135deg, rgba(16,185,129,0.12) 0%, rgba(52,211,153,0.08) 100%); border: 1px solid rgba(16,185,129,0.3); border-radius: 16px; padding: 18px;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
            <div>
                <span style="font-size: 16px; font-weight: 700; color: var(--text-primary);">九安医疗 002432</span>
                <span style="margin-left: 8px; padding: 2px 8px; background: rgba(239,68,68,0.2); color: #f87171; border-radius: 10px; font-size: 11px; font-weight: 600;">-8.46%</span>
            </div>
            <div style="text-align: right;">
                <span style="color: #4ade80; font-weight: 700;">机构净买 +2.29亿</span>
            </div>
        </div>
        <div style="font-size: 13px; color: var(--text-secondary); line-height: 1.7;">
            <p style="margin: 0 0 5px 0;"><strong>席位分析：</strong>龙虎榜净买入额排名第四(+6.14亿)，机构专用席位净买入2.29亿元。医药生物板块今日获机构青睐，九安医疗是机构重点加仓的医药标的。</p>
            <p style="margin: 0 0 5px 0;"><strong>题材属性：</strong>医疗器械/家用检测龙头，医药板块防御属性标的。在科技股崩盘的背景下，医药板块作为防御性板块获得资金流入。</p>
            <p style="margin: 0;"><strong>持续性判断：★★★☆☆</strong> 机构逆势加仓+防御板块属性，在市场风格切换背景下有一定持续性。但今日大跌8.46%说明抛压也不轻，关注68元支撑位。</p>
        </div>
    </div>
    
</div>
'''
gen._components.append(Section(title="🐉 龙虎榜深度解读", content=longhubang_html, icon="award"))

# ============================================================
# 8. 重点关注标的
# ============================================================
watchlist_html = '''
<div style="display: flex; flex-direction: column; gap: 16px;">
    
    <div style="background: var(--glass-bg); border: 1px solid var(--glass-border); border-radius: 16px; padding: 18px;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
            <div>
                <span style="font-size: 16px; font-weight: 700; color: var(--text-primary);">中国海油 600938</span>
                <span style="margin-left: 8px; padding: 2px 8px; background: rgba(16,185,129,0.2); color: #4ade80; border-radius: 10px; font-size: 11px; font-weight: 600;">涨停</span>
            </div>
            <div style="text-align: right;">
                <span style="color: #4ade80; font-weight: 700;">关注等级：★★★★☆</span>
            </div>
        </div>
        <div style="font-size: 13px; color: var(--text-secondary); line-height: 1.7;">
            <p style="margin: 0 0 5px 0;"><strong>买入逻辑：</strong>①霍尔木兹海峡局势紧张，原油供应恐慌，国际油价进入上行周期；②高股息+中特估双轮驱动，防御属性极强；③上半年油气公司业绩普遍超预期；④资金从科技转向能源，中期趋势明确。</p>
            <p style="margin: 0 0 5px 0;"><strong>技术面：</strong>今日强势涨停突破，成交量放大，均线多头排列，上升趋势明确。</p>
            <p style="margin: 0;">
                <span style="background: rgba(16,185,129,0.15); color: #4ade80; padding: 3px 8px; border-radius: 6px; font-weight: 600;">🎯 目标价：32-35元</span>
                <span style="margin-left: 6px; background: rgba(239,68,68,0.15); color: #f87171; padding: 3px 8px; border-radius: 6px; font-weight: 600;">🛑 止损位：25元</span>
                <span style="margin-left: 6px; background: rgba(59,130,246,0.15); color: #60a5fa; padding: 3px 8px; border-radius: 6px; font-weight: 600;">💰 建议仓位：10-15%</span>
            </p>
        </div>
    </div>
    
    <div style="background: var(--glass-bg); border: 1px solid var(--glass-border); border-radius: 16px; padding: 18px;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
            <div>
                <span style="font-size: 16px; font-weight: 700; color: var(--text-primary);">立新能源 001258</span>
                <span style="margin-left: 8px; padding: 2px 8px; background: rgba(16,185,129,0.2); color: #4ade80; border-radius: 10px; font-size: 11px; font-weight: 600;">3连板</span>
            </div>
            <div style="text-align: right;">
                <span style="color: #4ade80; font-weight: 700;">关注等级：★★★☆☆</span>
            </div>
        </div>
        <div style="font-size: 13px; color: var(--text-secondary); line-height: 1.7;">
            <p style="margin: 0 0 5px 0;"><strong>买入逻辑：</strong>①夏季用电高峰，用电负荷屡创新高，电力需求确定；②绿电政策支撑+电力改革催化；③电力板块批量涨停，板块效应明显，立新能源是高度龙头；④小盘次新股，弹性大。</p>
            <p style="margin: 0 0 5px 0;"><strong>风险提示：</strong>3连板后追高风险大，需等待回调机会。次新股波动剧烈，仓位控制第一。</p>
            <p style="margin: 0;">
                <span style="background: rgba(16,185,129,0.15); color: #4ade80; padding: 3px 8px; border-radius: 6px; font-weight: 600;">🎯 目标价：25-28元</span>
                <span style="margin-left: 6px; background: rgba(239,68,68,0.15); color: #f87171; padding: 3px 8px; border-radius: 6px; font-weight: 600;">🛑 止损位：16元</span>
                <span style="margin-left: 6px; background: rgba(59,130,246,0.15); color: #60a5fa; padding: 3px 8px; border-radius: 6px; font-weight: 600;">💰 建议仓位：5-8%</span>
            </p>
        </div>
    </div>
    
    <div style="background: var(--glass-bg); border: 1px solid var(--glass-border); border-radius: 16px; padding: 18px;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
            <div>
                <span style="font-size: 16px; font-weight: 700; color: var(--text-primary);">贵州茅台 600519</span>
                <span style="margin-left: 8px; padding: 2px 8px; background: rgba(16,185,129,0.2); color: #4ade80; border-radius: 10px; font-size: 11px; font-weight: 600;">+5.60%</span>
            </div>
            <div style="text-align: right;">
                <span style="color: #4ade80; font-weight: 700;">关注等级：★★★★☆</span>
            </div>
        </div>
        <div style="font-size: 13px; color: var(--text-secondary); line-height: 1.7;">
            <p style="margin: 0 0 5px 0;"><strong>买入逻辑：</strong>①提价预期催化消费复苏，茅台作为消费龙头直接受益；②获32亿主力资金净流入，机构资金持续加仓；③消费板块估值处于历史低位，安全边际高；④避险属性强，市场风格切换背景下防御价值突出；⑤北向资金重点配置标的。</p>
            <p style="margin: 0 0 5px 0;"><strong>技术面：</strong>今日放量大涨突破1300元整数关口，结束长期下跌趋势，短期筑底反弹信号明确。</p>
            <p style="margin: 0;">
                <span style="background: rgba(16,185,129,0.15); color: #4ade80; padding: 3px 8px; border-radius: 6px; font-weight: 600;">🎯 目标价：1500-1600元</span>
                <span style="margin-left: 6px; background: rgba(239,68,68,0.15); color: #f87171; padding: 3px 8px; border-radius: 6px; font-weight: 600;">🛑 止损位：1200元</span>
                <span style="margin-left: 6px; background: rgba(59,130,246,0.15); color: #60a5fa; padding: 3px 8px; border-radius: 6px; font-weight: 600;">💰 建议仓位：15-20%</span>
            </p>
        </div>
    </div>
    
</div>
'''
gen._components.append(Section(title="🎯 重点关注标的", content=watchlist_html, icon="target"))

# ============================================================
# 9. 明日操作策略
# ============================================================
plan_html = '''
<div style="font-size: 14px; line-height: 1.8; color: var(--text-secondary);">
    
    <div style="background: linear-gradient(135deg, rgba(59,130,246,0.15) 0%, rgba(147,51,234,0.1) 100%); border: 1px solid rgba(59,130,246,0.3); border-radius: 14px; padding: 16px; margin-bottom: 16px;">
        <div style="font-weight: 700; color: #60a5fa; margin-bottom: 10px; font-size: 15px;">📊 大盘判断：指数震荡，个股继续分化探底</div>
        <p style="margin: 0 0 6px 0;">明日大盘大概率延续震荡格局，沪指在3740-3820区间波动。权重护盘下指数跌幅有限，但科技成长股的调整远未结束，个股层面继续承压。关注两个信号：①成交额是否缩量至2.2万亿以下（地量见底信号）；②跌停家数是否明显减少（情绪企稳信号）。</p>
        <p style="margin: 0;">创业板指关注3400点支撑，科创50关注1650点支撑。若跌破则打开进一步下行空间。</p>
    </div>
    
    <div style="background: var(--glass-bg); border: 1px solid var(--glass-border); border-radius: 14px; padding: 16px; margin-bottom: 16px;">
        <div style="font-weight: 700; color: var(--text-primary); margin-bottom: 10px; font-size: 15px;">💰 仓位建议：0-2成仓位，现金为王</div>
        <p style="margin: 0;">科技成长股系统性风险释放中，防御板块虽有机会但追高风险大。当前阶段以防守为主，整体仓位控制在0-2成。等待市场真正企稳（地量+止跌形态）后再加仓不迟。</p>
    </div>
    
    <div style="background: var(--glass-bg); border: 1px solid var(--glass-border); border-radius: 14px; padding: 16px; margin-bottom: 16px;">
        <div style="font-weight: 700; color: #ef4444; margin-bottom: 10px; font-size: 15px;">🔴 持仓操作计划（严格执行纪律）</div>
        
        <p style="margin: 0 0 4px 0;"><strong style="color: #ef4444;">1. 英维克(002837)：明日开盘无条件清仓</strong><br>
        成本104.23元→现价55.46元，亏损-46.8%，已深度破止损。<strong>明日9:30开盘第一时间挂单卖出</strong>，不犹豫不等待，纪律就是纪律。哪怕卖在最低点也要执行，因为后面可能跌得更低。<strong>卖出价位：集合竞价或开盘价</strong>。</p>
        
        <p style="margin: 0 0 4px 0;"><strong style="color: #f97316;">2. 铜冠铜箔(301217)：开板即减仓2/3</strong><br>
        成本87.16元→现价103.24元，浮盈+18%。<strong>明日若开板立即减仓2/3</strong>，只留1/3底仓观察。<strong>若开板后反弹至110元以上，继续减仓至只剩底仓</strong>。<strong>若跌破90元整数关口，全部止盈清仓</strong>，确保至少守住+3%利润底线。</p>
        
        <p style="margin: 0 0 4px 0;"><strong style="color: #fbbf24;">3. 雅克科技(002409)：反弹减仓至底仓</strong><br>
        成本108.80元→现价130.50元，浮盈+20%。四连跌停后可能有技术性反弹，<strong>反弹至135-140元区间坚决减仓2/3</strong>，只留底仓。<strong>若跌破120元整数关口，全部止盈清仓</strong>，确保至少守住+10%利润。</p>
        
        <p style="margin: 0;"><strong style="color: #dc2626;">4. *ST建艺(002789)：开板坚决清仓</strong><br>
        成本13.45元→现价8.55元，亏损-36.4%，深度破止损+退市风险。<strong>明日若开板立即清仓，不留一股</strong>。退市风险敞口必须关闭，这是底线。哪怕亏损巨大也要接受现实，ST股没有什么好留恋的。</p>
    </div>
    
    <div style="background: var(--glass-bg); border: 1px solid var(--glass-border); border-radius: 14px; padding: 16px; margin-bottom: 16px;">
        <div style="font-weight: 700; color: #4ade80; margin-bottom: 10px; font-size: 15px;">🟢 新机会观察（小仓位试错）</div>
        
        <p style="margin: 0 0 4px 0;"><strong>1. 油气能源（中国海油/中国石油）：</strong>地缘风险+油价上涨+高股息三重逻辑，趋势性机会。<strong>中国海油回调至27-28元区间可小仓位(5-8%)低吸</strong>，止损位25元，目标价32-35元。</p>
        
        <p style="margin: 0 0 4px 0;"><strong>2. 白酒消费（贵州茅台）：</strong>提价预期+防御属性+估值低位。<strong>茅台回调至1280-1300元区间可布局(10-15%仓位)</strong>，止损位1200元，目标价1500-1600元。</p>
        
        <p style="margin: 0 0 4px 0;"><strong>3. 电力（立新能源/华银电力）：</strong>夏季用电高峰+电力改革。但连板股追高风险大，<strong>等待回调至5日均线附近再考虑</strong>，仓位控制在5%以内。</p>
        
        <p style="margin: 0;"><strong>4. 科技股超跌反弹机会：</strong>暂不参与。虽然机构跌停板抄底光迅科技、德明利，但板块调整趋势未改，抄底风险远大于收益。耐心等待明确的企稳信号再考虑。</p>
    </div>
    
    <div style="background: rgba(245,158,11,0.1); border: 1px solid rgba(245,158,11,0.3); border-radius: 14px; padding: 16px;">
        <div style="font-weight: 700; color: #fbbf24; margin-bottom: 10px; font-size: 15px;">⚠️ 明日关键观察点</div>
        <ol style="margin: 0; padding-left: 20px; color: var(--text-secondary);">
            <li>成交额是否缩量：若缩量至2.2万亿以下，可能接近短期底部</li>
            <li>跌停家数：若跌停家数降至100以内，情绪可能企稳</li>
            <li>科技板块是否止跌：半导体/存储/PCB板块能否出现抗跌标的</li>
            <li>防御板块持续性：电力/煤炭/油气能否连板扩散，还是一日游</li>
            <li>北向资金流向：继续流入还是转向流出</li>
        </ol>
    </div>
    
</div>
'''
gen.add_trading_plan(plan_html)

# ============================================================
# 10. 风险提示
# ============================================================
risks = [
    "科技成长股系统性估值杀跌风险：半导体/存储/PCB等板块调整远未结束，抄底可能被套",
    "融资盘爆仓负反馈风险：融资余额连续13日缩水，被动平仓可能继续压制股价",
    "外围科技熊市传导风险：费城半导体进入技术性熊市，韩股暴跌，负面情绪持续传导",
    "长鑫IPO抽血效应：科创板史上最大IPO，机构腾挪资金持续压制科技板块",
    "地缘冲突加剧风险：霍尔木兹海峡局势紧张，全球资本市场波动率上升"
]
gen.add_risk_warning(risks)

# ============================================================
# 发布
# ============================================================
print("开始生成盘后速递报告...")
html = gen.generate()
print(f"HTML生成完成，长度: {len(html)} 字符")

# 保存并发布
result = gen.publish(
    title="2026.07.20 盘后速递",
    report_type="aftermarket",
    filename="20260720_盘后速递.html",
    excerpt="指数红个股崩，科技成长股遭遇黑色星期一。4只持仓全部跌停，组合单日暴击。电力/煤炭/油气/白酒防御板块全线大涨，极致高低切换。",
    auto_deploy=False
)
print(f"发布结果: {result}")

# 字数统计
import re
text_only = re.sub(r'<[^>]+>', '', html)
chinese_chars = len(re.findall(r'[\u4e00-\u9fff]', text_only))
print(f"正文中文字数: {chinese_chars}")
