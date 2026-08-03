"""
S级催化扫描 - 盘后 - 20260803
核心催化：日本出口管制升级落地+全球半导体巨震+科技股深V分化
"""
import sys
import os

os.chdir('/app/data/所有对话/主对话')
sys.path.insert(0, 'v3')

from v3.generators.s_level_catalyst import SLevelCatalystGenerator

# ============================================================
# 初始化生成器
# ============================================================
gen = SLevelCatalystGenerator(
    date_str="20260803",
    catalyst_title="日本管制升级+韩股暴跌+科技股深V巨震",
    subtitle="2026.08.03 · 盘后S级催化"
)

# ============================================================
# 1. 催化事件概述
# ============================================================
overview = """
<b>【核心事件】</b>8月首个交易日，全球半导体产业链迎来三重冲击：
① <b>日本第三轮对华半导体出口管制8月1日正式落地</b>，先进封装核心设备（固晶机/减薄机/TSV设备等20大类）纳入100%逐案审批，AI算力配套设备驳回率近80%；
② <b>韩国KOSPI暴跌5.12%</b>，三星电子、SK海力士双双大跌8.7%+，外资单日净卖出超2.6万亿韩元，存储板块获利盘集中兑现；
③ <b>A股科创50暴跌5.08%</b>创年内最大单日跌幅，但全市场4005只个股上涨（占比72%），极致分化上演"指数跌、个股嗨"。

<b>【盘后重磅】</b>中微公司发布中报业绩预告，上半年净利润27-29亿元，同比暴增282%-311%，设备龙头业绩超预期验证，为半导体板块提供基本面锚点。雅克科技龙虎榜显示机构+北向合计净买入4.9亿元，逆势抄底信号明确。

<b>【隔夜外盘前瞻】</b>美股盘前三大指数分化，道指期货涨1%、纳指期货涨0.35%；美光跌3%+、英伟达微跌、亚马逊涨2%；特朗普暂停对伊军事行动，原油暴跌6%+跌破80美元；10年期美债收益率回落至4.68%。
"""
gen.add_catalyst_overview(overview, importance="极高")

# ============================================================
# 2. 催化事件详解
# ============================================================
background = """
<b>日本出口管制升级落地（8月1日生效）</b>
本轮管制是日本对华半导体限制的第三轮升级，首次将<b>先进封装核心设备</b>纳入严格管控：
· 覆盖设备：高端固晶机、超薄晶圆减薄机、高精度分选机、激光隐切机、TSV硅通孔设备等20大类
· 审批规则：取消通用许可，强制执行100%逐案单独审批，常规周期3-6个月
· AI算力配套设备出口申请驳回率接近80%
· 过渡期：8月底前完成存量订单交付，9月起新订单全面适用新规

<b>韩国存储板块获利回吐</b>
7月最后一个交易日（7/31）韩国KOSPI单日暴涨18%，SK海力士涨停（+30%）、三星涨25%+，短期积累巨量获利盘。8月3日外资集中兑现，三星跌8.76%、SK海力士跌8.79%，外资分别净卖出9521亿韩元和1.72万亿韩元。

<b>A股半导体深度回调</b>
科创50暴跌5.08%，半导体设备ETF近乎跌停（-9.64%）。中科飞测、长川科技跌超12%，华海清科、富创精密跌超11%，中微公司跌9.93%。但同期全市场超4000只个股上涨，资金从高位科技龙头向低位题材（核电、电网、环保）快速切换。
"""

trigger = """
<b>直接触发因素（三重共振）</b>

1️⃣ <b>政策面：日本管制升级靴子落地</b>
先进封装设备纳入管制直接冲击HBM/Chiplet产业链，市场担忧国产替代进度。但需注意：管制是预期内事件，且国产替代逻辑反而强化。

2️⃣ <b>资金面：全球科技去杠杆传导</b>
· 韩国杠杆ETF规模较峰值缩水70%，去杠杆进程仍在演绎
· A股半导体ETF遭遇赎回压力，短线获利盘集中兑现
· 两融余额下降，杠杆资金回吐二季度全部增量
· 北向资金全天净卖出32.6亿元

3️⃣ <b>情绪面：风格切换加速</b>
国常会核准4个核电项目（1700亿投资）引爆核电板块，资金从高位科技向低位政策驱动板块快速迁移。可控核聚变、电网设备、环保等板块逆势走强。

<b>【反向支撑信号】</b>
· 雅克科技龙虎榜：机构净买入2.73亿+北向净买入2.17亿=合计4.9亿，机构逆势抄底
· 中微公司盘后业绩：上半年净利增282%-311%，设备龙头基本面验证
· 长鑫科技逆势V型反转收涨1.9%，成交超300亿，机构配置盘承接
· 两市成交额缩量至1.997万亿（-5446亿），缩量下跌=抛压衰竭迹象
"""
gen.add_catalyst_details(background, trigger)

# ============================================================
# 3. 产业链梳理
# ============================================================
upstream = [
    {
        "name": "半导体设备（国产替代核心）",
        "desc": "日本管制升级加速国产替代进程，刻蚀/薄膜/量检测设备龙头受益于自主可控逻辑强化。中微公司中报净利增282%-311%验证设备高景气。",
        "stocks": [
            {"code": "688012", "name": "中微公司", "impact": "核心受益"},
            {"code": "002371", "name": "北方华创", "impact": "核心受益"},
            {"code": "688361", "name": "中科飞测", "impact": "高弹性"},
            {"code": "688072", "name": "拓荆科技", "impact": "薄膜设备"},
        ]
    },
    {
        "name": "半导体材料（供应链安全）",
        "desc": "光刻胶、电子特气、CMP抛光液等材料国产替代加速。雅克科技机构+北向逆势净买入4.9亿，显示长线资金对半导体材料龙头的信心。",
        "stocks": [
            {"code": "002409", "name": "雅克科技", "impact": "机构抄底"},
            {"code": "688535", "name": "华海诚科", "impact": "先进封装材料"},
            {"code": "300655", "name": "晶瑞电材", "impact": "光刻胶"},
        ]
    },
]

midstream = [
    {
        "name": "存储芯片（周期+国产替代双击）",
        "desc": "全球存储周期上行趋势未变，AI服务器HBM/DDR5需求持续拉动。短期韩国暴跌带来的情绪冲击是交易性调整，不改产业趋势。江波龙/佰维存储中报业绩暴增验证。",
        "stocks": [
            {"code": "688525", "name": "佰维存储", "impact": "存储模组"},
            {"code": "301308", "name": "江波龙", "impact": "存储龙头"},
            {"code": "603986", "name": "兆易创新", "impact": "利基存储"},
        ]
    },
    {
        "name": "先进封装（Chiplet核心环节）",
        "desc": "日本管制重点影响先进封装设备，但Chiplet是AI算力提升的必经之路，国产封装设备和材料厂商迎替代机遇。通富微电龙虎榜机构净买入2543万。",
        "stocks": [
            {"code": "002156", "name": "通富微电", "impact": "封测龙头"},
            {"code": "600584", "name": "长电科技", "impact": "封测龙头"},
            {"code": "002185", "name": "华天科技", "impact": "封测"},
        ]
    },
    {
        "name": "PCB铜箔（AI算力上游）",
        "desc": "AI服务器高阶PCB/HVLP铜箔需求持续增长，铜冠铜箔为国产HVLP铜箔龙头，随AI服务器升级持续受益。短期随板块调整，不改中期成长逻辑。",
        "stocks": [
            {"code": "301217", "name": "铜冠铜箔", "impact": "HVLP铜箔龙头"},
        ]
    },
]

downstream = [
    {
        "name": "核电（新主线崛起）",
        "desc": "国常会核准4个核电项目共8台机组，总投资超1700亿。\"十五五\"首批核准，华龙一号2.0版示范工程落地，核电量价共振（核准常态化+机制电价推广）。",
        "stocks": [
            {"code": "601611", "name": "中国核建", "impact": "核电建设"},
            {"code": "002438", "name": "江苏神通", "impact": "核电阀门"},
            {"code": "600875", "name": "东方电气", "impact": "核电设备"},
            {"code": "605167", "name": "利柏特", "impact": "核电模块"},
        ]
    },
    {
        "name": "AI应用端（低位补涨）",
        "desc": "算力硬件调整后，资金向AI应用端扩散。AI教育、数字营销、传媒游戏等板块活跃。传智教育6连板，AI应用端景气度验证。",
        "stocks": [
            {"code": "003032", "name": "传智教育", "impact": "AI教育龙头"},
            {"code": "002131", "name": "利欧股份", "impact": "AI营销"},
        ]
    },
]

gen.add_industry_chain_analysis(upstream, midstream, downstream)

# ============================================================
# 4. 持仓股分析
# ============================================================
from components.layout import Section

portfolio_html = """
<div style="display: flex; flex-direction: column; gap: 14px;">
    <!-- 雅克科技 -->
    <div style="border-left: 4px solid #ef4444; border-radius: 0 12px 12px 0;">
        <div style="background: rgba(255,255,255,0.04); border-radius: 0 12px 12px 0; padding: 16px 20px; backdrop-filter: blur(10px); border: 1px solid rgba(255,255,255,0.06); border-left: none;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
                <div>
                    <span style="font-size: 18px; font-weight: 700; color: #f1f5f9;">雅克科技 (002409)</span>
                    <span style="margin-left: 12px; padding: 3px 10px; background: linear-gradient(135deg, #ef4444, #dc2626); color: white; border-radius: 20px; font-size: 12px; font-weight: 700;">-9.63%</span>
                </div>
                <span style="font-size: 22px; font-weight: 800; color: #f87171;">120.91元</span>
            </div>
            <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 12px; margin-bottom: 12px;">
                <div style="background: rgba(0,0,0,0.2); border-radius: 8px; padding: 10px; text-align: center;">
                    <div style="font-size: 11px; color: #94a3b8; margin-bottom: 4px;">换手率</div>
                    <div style="font-size: 15px; font-weight: 700; color: #fbbf24;">12.07%</div>
                </div>
                <div style="background: rgba(0,0,0,0.2); border-radius: 8px; padding: 10px; text-align: center;">
                    <div style="font-size: 11px; color: #94a3b8; margin-bottom: 4px;">成交额</div>
                    <div style="font-size: 15px; font-weight: 700; color: #60a5fa;">47.64亿</div>
                </div>
                <div style="background: rgba(0,0,0,0.2); border-radius: 8px; padding: 10px; text-align: center;">
                    <div style="font-size: 11px; color: #94a3b8; margin-bottom: 4px;">机构净买入</div>
                    <div style="font-size: 15px; font-weight: 700; color: #34d399;">+2.73亿</div>
                </div>
                <div style="background: rgba(0,0,0,0.2); border-radius: 8px; padding: 10px; text-align: center;">
                    <div style="font-size: 11px; color: #94a3b8; margin-bottom: 4px;">北向净买入</div>
                    <div style="font-size: 15px; font-weight: 700; color: #34d399;">+2.17亿</div>
                </div>
            </div>
            <div style="font-size: 13px; color: #cbd5e1; line-height: 1.8;">
                <b>【双重验证结论】</b>今日暴跌9.63%但龙虎榜显示<b>机构+北向合计净买入4.9亿元</b>（龙虎榜净买额全市场第一），属于典型的"多杀多"式恐慌抛售，而非基本面恶化导致的机构出逃。5家机构席位现身买入端，合计买入5.84亿、卖出3.11亿，净买入2.73亿（占成交额5.74%）。
                <br>✅ 利空性质：<b>情绪面杀跌，非实质性利空</b>。公司基本面未发生变化（Q1净利增2.47%），半导体材料国产替代逻辑强化。
                <br>✅ 估值锚：当前TTM市盈率约47倍，处于半导体材料板块中等水平，近5日累计跌幅已达28.6%，短期超跌。
                <br>✅ 操作建议：<b>底仓30%持有不动</b>，若明日继续下探至115-110元区间可考虑小仓位加仓做T。上方第一压力位130元（5日线），强压力位150元（前期平台）。
            </div>
        </div>
    </div>

    <!-- 铜冠铜箔 -->
    <div style="border-left: 4px solid #f59e0b; border-radius: 0 12px 12px 0;">
        <div style="background: rgba(255,255,255,0.04); border-radius: 0 12px 12px 0; padding: 16px 20px; backdrop-filter: blur(10px); border: 1px solid rgba(255,255,255,0.06); border-left: none;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
                <div>
                    <span style="font-size: 18px; font-weight: 700; color: #f1f5f9;">铜冠铜箔 (301217)</span>
                    <span style="margin-left: 12px; padding: 3px 10px; background: linear-gradient(135deg, #f59e0b, #d97706); color: white; border-radius: 20px; font-size: 12px; font-weight: 700;">-6.00%</span>
                </div>
                <span style="font-size: 22px; font-weight: 800; color: #fbbf24;">77.66元</span>
            </div>
            <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 12px; margin-bottom: 12px;">
                <div style="background: rgba(0,0,0,0.2); border-radius: 8px; padding: 10px; text-align: center;">
                    <div style="font-size: 11px; color: #94a3b8; margin-bottom: 4px;">换手率</div>
                    <div style="font-size: 15px; font-weight: 700; color: #fbbf24;">3.27%</div>
                </div>
                <div style="background: rgba(0,0,0,0.2); border-radius: 8px; padding: 10px; text-align: center;">
                    <div style="font-size: 11px; color: #94a3b8; margin-bottom: 4px;">成交额</div>
                    <div style="font-size: 15px; font-weight: 700; color: #60a5fa;">21.52亿</div>
                </div>
                <div style="background: rgba(0,0,0,0.2); border-radius: 8px; padding: 10px; text-align: center;">
                    <div style="font-size: 11px; color: #94a3b8; margin-bottom: 4px;">主力净流出</div>
                    <div style="font-size: 15px; font-weight: 700; color: #f87171;">-2.34亿</div>
                </div>
                <div style="background: rgba(0,0,0,0.2); border-radius: 8px; padding: 10px; text-align: center;">
                    <div style="font-size: 11px; color: #94a3b8; margin-bottom: 4px;">5日跌幅</div>
                    <div style="font-size: 15px; font-weight: 700; color: #f87171;">~25%</div>
                </div>
            </div>
            <div style="font-size: 13px; color: #cbd5e1; line-height: 1.8;">
                <b>【分析】</b>随PCB/覆铜板板块集体调整，短期跌幅较大但成交量未显著放大（换手率3.27%），说明恐慌性抛盘有限。主力资金净流出2.34亿（占比10.87%），但散户资金净流入2.69亿形成对冲。
                <br>✅ 基本面：AI服务器HVLP铜箔需求持续增长，公司为国产HVLP铜箔龙头，Q1业绩超预期。
                <br>✅ 估值锚：PB 11.7倍，处于历史中高位，但考虑到AI铜箔的高成长属性，估值可接受。
                <br>✅ 技术面：今日最低77.37元，已接近前期调整低点区域。下方支撑75-77元区间。
                <br>✅ 操作建议：<b>继续持有</b>，75-77元区间可考虑小幅加仓。上方压力位85元（10日线）。中期目标维持不变。
            </div>
        </div>
    </div>

    <!-- 英维克 -->
    <div style="border-left: 4px solid #3b82f6; border-radius: 0 12px 12px 0;">
        <div style="background: rgba(255,255,255,0.04); border-radius: 0 12px 12px 0; padding: 16px 20px; backdrop-filter: blur(10px); border: 1px solid rgba(255,255,255,0.06); border-left: none;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
                <div>
                    <span style="font-size: 18px; font-weight: 700; color: #f1f5f9;">英维克 (002837)</span>
                    <span style="margin-left: 12px; padding: 3px 10px; background: linear-gradient(135deg, #3b82f6, #2563eb); color: white; border-radius: 20px; font-size: 12px; font-weight: 700;">-2.11%</span>
                </div>
                <span style="font-size: 22px; font-weight: 800; color: #60a5fa;">46.45元</span>
            </div>
            <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 12px; margin-bottom: 12px;">
                <div style="background: rgba(0,0,0,0.2); border-radius: 8px; padding: 10px; text-align: center;">
                    <div style="font-size: 11px; color: #94a3b8; margin-bottom: 4px;">换手率</div>
                    <div style="font-size: 15px; font-weight: 700; color: #fbbf24;">3.37%</div>
                </div>
                <div style="background: rgba(0,0,0,0.2); border-radius: 8px; padding: 10px; text-align: center;">
                    <div style="font-size: 11px; color: #94a3b8; margin-bottom: 4px;">成交额</div>
                    <div style="font-size: 15px; font-weight: 700; color: #60a5fa;">17.86亿</div>
                </div>
                <div style="background: rgba(0,0,0,0.2); border-radius: 8px; padding: 10px; text-align: center;">
                    <div style="font-size: 11px; color: #94a3b8; margin-bottom: 4px;">市盈率(TTM)</div>
                    <div style="font-size: 15px; font-weight: 700; color: #a78bfa;">122.7倍</div>
                </div>
                <div style="background: rgba(0,0,0,0.2); border-radius: 8px; padding: 10px; text-align: center;">
                    <div style="font-size: 11px; color: #94a3b8; margin-bottom: 4px;">日内振幅</div>
                    <div style="font-size: 15px; font-weight: 700; color: #fbbf24;">5.02%</div>
                </div>
            </div>
            <div style="font-size: 13px; color: #cbd5e1; line-height: 1.8;">
                <b>【分析】</b>今日相对抗跌（仅跌2.11%），明显强于半导体设备和存储板块，液冷板块韧性显现。成交额缩量至17.86亿，抛压有所减轻。
                <br>✅ 基本面：AI算力液冷需求确定性高，公司为液冷龙头，数据中心液冷业务持续高增。
                <br>✅ 技术面：45-46元区间有一定支撑，今日最低45.82元后反弹，显示低位承接力。
                <br>✅ 操作建议：<b>持有观望</b>，关注45元支撑有效性，若跌破43元需止损。上方压力位50元。
            </div>
        </div>
    </div>

    <!-- *ST建艺 -->
    <div style="border-left: 4px solid #10b981; border-radius: 0 12px 12px 0;">
        <div style="background: rgba(255,255,255,0.04); border-radius: 0 12px 12px 0; padding: 16px 20px; backdrop-filter: blur(10px); border: 1px solid rgba(255,255,255,0.06); border-left: none;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
                <div>
                    <span style="font-size: 18px; font-weight: 700; color: #f1f5f9;">*ST建艺 (002789)</span>
                    <span style="margin-left: 12px; padding: 3px 10px; background: linear-gradient(135deg, #10b981, #059669); color: white; border-radius: 20px; font-size: 12px; font-weight: 700;">+4.91%</span>
                </div>
                <span style="font-size: 22px; font-weight: 800; color: #34d399;">10.04元</span>
            </div>
            <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 12px; margin-bottom: 12px;">
                <div style="background: rgba(0,0,0,0.2); border-radius: 8px; padding: 10px; text-align: center;">
                    <div style="font-size: 11px; color: #94a3b8; margin-bottom: 4px;">换手率</div>
                    <div style="font-size: 15px; font-weight: 700; color: #fbbf24;">1.85%</div>
                </div>
                <div style="background: rgba(0,0,0,0.2); border-radius: 8px; padding: 10px; text-align: center;">
                    <div style="font-size: 11px; color: #94a3b8; margin-bottom: 4px;">成交额</div>
                    <div style="font-size: 15px; font-weight: 700; color: #60a5fa;">2830万</div>
                </div>
                <div style="background: rgba(0,0,0,0.2); border-radius: 8px; padding: 10px; text-align: center;">
                    <div style="font-size: 11px; color: #94a3b8; margin-bottom: 4px;">市净率</div>
                    <div style="font-size: 15px; font-weight: 700; color: #a78bfa;">~4倍</div>
                </div>
                <div style="background: rgba(0,0,0,0.2); border-radius: 8px; padding: 10px; text-align: center;">
                    <div style="font-size: 11px; color: #94a3b8; margin-bottom: 4px;">今日表现</div>
                    <div style="font-size: 15px; font-weight: 700; color: #34d399;">尾盘拉升</div>
                </div>
            </div>
            <div style="font-size: 13px; color: #cbd5e1; line-height: 1.8;">
                <b>【分析】</b>今日收涨4.91%报10.04元，尾盘出现明显拉升。ST板块整体活跃度提升，市场风险偏好回暖下小盘ST股有资金博弈。
                <br>⚠️ 风险提示：Q1亏损5311万，负债率94.38%，退市风险仍存，属于高风险投机品种。
                <br>✅ 操作建议：<b>小仓位博弈为主</b>，严格控制仓位（不超过总仓位5%），止损位9元。
            </div>
        </div>
    </div>
</div>
"""

gen.report.add(Section(title="📊 持仓股盘后诊断", content=portfolio_html, icon="pie-chart", variant="highlight"))

# ============================================================
# 5. 隔夜外盘扫描
# ============================================================
overnight_html = """
<div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 14px;">
    <!-- 美股指数 -->
    <div style="background: linear-gradient(135deg, rgba(59,130,246,0.12) 0%, rgba(37,99,235,0.08) 100%); border-radius: 14px; padding: 18px; border: 1px solid rgba(96,165,250,0.25);">
        <div style="font-size: 15px; font-weight: 700; color: #60a5fa; margin-bottom: 12px;">🇺🇸 美股盘前（截至20:00 ET）</div>
        <div style="display: flex; flex-direction: column; gap: 8px;">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <span style="color: #cbd5e1; font-size: 13px;">道指期货</span>
                <span style="color: #34d399; font-weight: 700; font-size: 14px;">+1.02%</span>
            </div>
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <span style="color: #cbd5e1; font-size: 13px;">标普500期货</span>
                <span style="color: #34d399; font-weight: 700; font-size: 14px;">+0.65%</span>
            </div>
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <span style="color: #cbd5e1; font-size: 13px;">纳指100期货</span>
                <span style="color: #fbbf24; font-weight: 700; font-size: 14px;">+0.35%</span>
            </div>
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <span style="color: #cbd5e1; font-size: 13px;">10年期美债收益率</span>
                <span style="color: #34d399; font-weight: 700; font-size: 14px;">4.68% ↓</span>
            </div>
        </div>
    </div>

    <!-- 半导体个股 -->
    <div style="background: linear-gradient(135deg, rgba(168,85,247,0.12) 0%, rgba(139,92,246,0.08) 100%); border-radius: 14px; padding: 18px; border: 1px solid rgba(168,85,247,0.25);">
        <div style="font-size: 15px; font-weight: 700; color: #c084fc; margin-bottom: 12px;">🔬 核心半导体标的盘前</div>
        <div style="display: flex; flex-direction: column; gap: 8px;">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <span style="color: #cbd5e1; font-size: 13px;">美光 (MU)</span>
                <span style="color: #f87171; font-weight: 700; font-size: 14px;">-3.0%+</span>
            </div>
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <span style="color: #cbd5e1; font-size: 13px;">英伟达 (NVDA)</span>
                <span style="color: #f87171; font-weight: 700; font-size: 14px;">-1.18%</span>
            </div>
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <span style="color: #cbd5e1; font-size: 13px;">AMD</span>
                <span style="color: #f87171; font-weight: 700; font-size: 14px;">-1.3%</span>
            </div>
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <span style="color: #cbd5e1; font-size: 13px;">亚马逊 (AMZN)</span>
                <span style="color: #34d399; font-weight: 700; font-size: 14px;">+2.0%</span>
            </div>
        </div>
    </div>

    <!-- 亚太市场 -->
    <div style="background: linear-gradient(135deg, rgba(245,158,11,0.12) 0%, rgba(217,119,6,0.08) 100%); border-radius: 14px; padding: 18px; border: 1px solid rgba(251,191,36,0.25);">
        <div style="font-size: 15px; font-weight: 700; color: #fbbf24; margin-bottom: 12px;">🌏 亚太市场（今日收盘）</div>
        <div style="display: flex; flex-direction: column; gap: 8px;">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <span style="color: #cbd5e1; font-size: 13px;">韩国KOSPI</span>
                <span style="color: #f87171; font-weight: 700; font-size: 14px;">-5.12%</span>
            </div>
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <span style="color: #cbd5e1; font-size: 13px;">三星电子</span>
                <span style="color: #f87171; font-weight: 700; font-size: 14px;">-8.76%</span>
            </div>
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <span style="color: #cbd5e1; font-size: 13px;">SK海力士</span>
                <span style="color: #f87171; font-weight: 700; font-size: 14px;">-8.79%</span>
            </div>
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <span style="color: #cbd5e1; font-size: 13px;">日经225</span>
                <span style="color: #fbbf24; font-weight: 700; font-size: 14px;">约-1%</span>
            </div>
        </div>
    </div>

    <!-- 大宗商品 -->
    <div style="background: linear-gradient(135deg, rgba(16,185,129,0.12) 0%, rgba(5,150,105,0.08) 100%); border-radius: 14px; padding: 18px; border: 1px solid rgba(16,185,129,0.25);">
        <div style="font-size: 15px; font-weight: 700; color: #34d399; margin-bottom: 12px;">🛢️ 大宗商品 & 地缘</div>
        <div style="display: flex; flex-direction: column; gap: 8px;">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <span style="color: #cbd5e1; font-size: 13px;">WTI原油</span>
                <span style="color: #f87171; font-weight: 700; font-size: 14px;">-6.09% 79.52$</span>
            </div>
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <span style="color: #cbd5e1; font-size: 13px;">布伦特原油</span>
                <span style="color: #f87171; font-weight: 700; font-size: 14px;">-5.05% 83.44$</span>
            </div>
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <span style="color: #cbd5e1; font-size: 13px;">COMEX黄金</span>
                <span style="color: #34d399; font-weight: 700; font-size: 14px;">+0.28% 4118$</span>
            </div>
            <div style="font-size: 11px; color: #64748b; margin-top: 6px; line-height: 1.6;">
                特朗普暂停对伊军事行动+OPEC+9月增产18.8万桶/日，原油暴跌。地缘风险缓解利好风险资产。
            </div>
        </div>
    </div>
</div>
"""
gen.report.add(Section(title="🌍 隔夜外盘扫描", content=overnight_html, icon="globe"))

# ============================================================
# 6. 龙虎榜异动信号
# ============================================================
longhubang_html = """
<div style="display: flex; flex-direction: column; gap: 12px;">
    <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px;">
        <div style="background: rgba(16,185,129,0.1); border-radius: 12px; padding: 14px; border: 1px solid rgba(16,185,129,0.2);">
            <div style="font-size: 12px; color: #6ee7b7; margin-bottom: 6px;">机构净买入TOP1</div>
            <div style="font-size: 16px; font-weight: 700; color: #f1f5f9;">德明利</div>
            <div style="font-size: 20px; font-weight: 800; color: #34d399;">+5.13亿</div>
            <div style="font-size: 11px; color: #64748b; margin-top: 4px;">存储主控 | 占成交5.25%</div>
        </div>
        <div style="background: rgba(16,185,129,0.1); border-radius: 12px; padding: 14px; border: 1px solid rgba(16,185,129,0.2);">
            <div style="font-size: 12px; color: #6ee7b7; margin-bottom: 6px;">机构净买入TOP2</div>
            <div style="font-size: 16px; font-weight: 700; color: #f1f5f9;">雅克科技</div>
            <div style="font-size: 20px; font-weight: 800; color: #34d399;">+2.73亿</div>
            <div style="font-size: 11px; color: #64748b; margin-top: 4px;">半导体材料 | 占成交5.74%</div>
        </div>
        <div style="background: rgba(16,185,129,0.1); border-radius: 12px; padding: 14px; border: 1px solid rgba(16,185,129,0.2);">
            <div style="font-size: 12px; color: #6ee7b7; margin-bottom: 6px;">机构净买入TOP3</div>
            <div style="font-size: 16px; font-weight: 700; color: #f1f5f9;">利欧股份</div>
            <div style="font-size: 20px; font-weight: 800; color: #34d399;">+1.46亿</div>
            <div style="font-size: 11px; color: #64748b; margin-top: 4px;">AI营销 | 占成交2.09%</div>
        </div>
    </div>
    <div style="font-size: 13px; color: #94a3b8; line-height: 1.8; background: rgba(0,0,0,0.2); border-radius: 10px; padding: 12px 16px;">
        <b>📌 龙虎榜核心信号：</b>
        <br>① 雅克科技机构净买入2.73亿+北向2.17亿=合计4.9亿（全市场龙虎榜净买第一），暴跌日机构逆势抄底，信号积极
        <br>② 德明利机构净买入5.13亿居首，存储主控芯片获机构青睐
        <br>③ 通富微电机构净买入2543万，先进封装封测龙头获机构小幅加仓
        <br>④ 富瀚微20cm涨停（+20.01%），龙虎榜净买入3.75亿，AI视觉芯片龙头业绩爆发获资金追捧
    </div>
</div>
"""
gen.report.add(Section(title="🏆 龙虎榜异动信号", content=longhubang_html, icon="trophy"))

# ============================================================
# 7. 催化深度分析（Skill增强）
# ============================================================
gen.add_catalyst_deep_analysis([
    {
        "title": "日本出口管制升级",
        "type": "policy",
        "description": "日本第三轮对华半导体出口管制正式落地，先进封装设备纳入管控，国产替代加速",
        "category": "政策催化"
    },
    {
        "title": "半导体板块深调",
        "type": "data",
        "description": "科创50暴跌5.08%，半导体设备ETF近乎跌停，但机构逆势抄底雅克科技等龙头",
        "category": "市场异动"
    },
    {
        "title": "中微公司业绩爆发",
        "type": "earnings",
        "description": "中微公司中报预增282%-311%，半导体设备龙头业绩超预期验证基本面",
        "category": "业绩催化"
    },
])

# ============================================================
# 8. 投资机会分析
# ============================================================
opportunities = [
    {
        "name": "半导体设备国产替代（核心主线）",
        "priority": "高",
        "logic": "日本出口管制升级反而加速国产设备替代进程。中微公司中报净利增282%-311%验证设备高景气。当前板块深度调整提供优质布局窗口。重点关注刻蚀、薄膜、量检测设备龙头。",
        "stocks": [
            {"code": "688012", "name": "中微公司", "impact": "业绩验证"},
            {"code": "002371", "name": "北方华创", "impact": "设备平台"},
        ]
    },
    {
        "name": "半导体材料抄底机会",
        "priority": "高",
        "logic": "雅克科技龙虎榜机构+北向逆势净买入4.9亿，显示长线资金对半导体材料龙头的信心。半导体材料国产替代空间大，短期超跌后弹性足。",
        "stocks": [
            {"code": "002409", "name": "雅克科技", "impact": "机构抄底"},
            {"code": "688535", "name": "华海诚科", "impact": "先进封装材料"},
        ]
    },
    {
        "name": "核电新主线（事件驱动）",
        "priority": "中",
        "logic": "国常会核准4个核电项目1700亿投资，\"十五五\"首批核准落地。核准常态化+机制电价推广双轮驱动，核电运营商DCF价值重估。关注核电设备、阀门、建设龙头。",
        "stocks": [
            {"code": "601611", "name": "中国核建", "impact": "核电建设"},
            {"code": "002438", "name": "江苏神通", "impact": "核电阀门"},
            {"code": "600875", "name": "东方电气", "impact": "主设备"},
        ]
    },
    {
        "name": "存储芯片（中期布局）",
        "priority": "中",
        "logic": "全球存储周期上行趋势未变，AI服务器HBM需求持续拉动。韩国暴跌是短期获利盘兑现，不改产业趋势。江波龙中报预增600倍+验证行业景气。等待企稳信号后分批布局。",
        "stocks": [
            {"code": "301308", "name": "江波龙", "impact": "存储龙头"},
            {"code": "688525", "name": "佰维存储", "impact": "存储模组"},
        ]
    },
    {
        "name": "AI应用端（低位补涨）",
        "priority": "低",
        "logic": "算力硬件调整后资金向AI应用端扩散。AI教育、数字营销、传媒游戏等板块有补涨需求。属于题材性机会，快进快出为主。",
        "stocks": [
            {"code": "003032", "name": "传智教育", "impact": "AI教育"},
        ]
    },
]
gen.add_investment_opportunities(opportunities, view_mode="tab")

# ============================================================
# 9. 投资策略建议
# ============================================================
strategy = """
<b>【总体判断】</b>今日半导体暴跌是全球科技股去杠杆+日本管制落地+获利盘兑现的三重共振，但<b>基本面没有恶化</b>（中微公司业绩验证），属于交易性调整而非趋势性反转。科创50单日跌5%+属于"极端情绪日"，历史上此类极端日之后1-2周内出现技术性反弹的概率较高。

<b>【仓位管理】</b>
· 总仓位控制在<b>5-6成</b>，保留4成以上现金应对波动
· 科技仓位占比不超过4成，分3批建仓（首批2成、第二批探底后加1成、第三批趋势确认后加1成）
· 核电/电网等新主线仓位1-2成，作为防御配置

<b>【操作节奏】</b>
① <b>明日（8/4）关注</b>：若半导体继续下探，雅克科技跌至115元以下可小仓位加仓做T；铜冠铜箔75元以下可小幅加仓
② <b>本周观察</b>：科创50能否在1500点附近企稳，成交额是否继续缩量（缩量=见底信号）
③ <b>关键催化</b>：关注AMD、闪迪本周财报（存储周期持续性验证），以及国内半导体政策面是否有对冲利好
④ <b>止损纪律</b>：单只持仓跌破技术支撑位（如英维克43元、铜冠铜箔70元）坚决止损

<b>【主线判断】</b>
科技成长仍是中期主线，但短期进入震荡磨底阶段。8月大概率是"修复+分化"行情，不再是普涨格局。选股逻辑从"题材驱动"转向"业绩兑现"，重点关注中报超预期的细分龙头。
核电作为新崛起的政策驱动主线，可持续关注，但不宜追高，等待回调后低吸。
"""
gen.add_investment_strategy(strategy)

# ============================================================
# 10. 风险提示
# ============================================================
gen.add_risk_warning([
    "美联储9月加息风险：市场已定价64%概率9月加息25bp，若通胀数据超预期可能引发新一轮科技股抛售",
    "韩国去杠杆风险：韩股波动率极高，若外资持续流出可能传导至A股半导体板块",
    "日本出口管制实际影响待观察：先进封装设备国产替代需要时间，短期可能影响相关企业扩产进度",
    "中报业绩雷风险：8月中下旬进入中报密集披露期，部分高估值个股若业绩不及预期可能承压",
    "地缘政治风险：中东局势虽有缓和但仍存不确定性，原油价格波动可能影响通胀预期",
    "本文仅为信息分析，不构成投资建议，投资有风险，入市需谨慎"
])

# ============================================================
# 发布报告
# ============================================================
result = gen.publish(
    title="日本管制升级+韩股暴跌+科技股深V巨震",
    filename="20260803_盘后_S级催化扫描_日本管制升级+科技股深V巨震.html"
)

print("发布结果:", result)
