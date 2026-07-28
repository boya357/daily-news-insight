#!/usr/bin/env python3
"""
明日催化剂报告生成脚本 - 2026年7月29日 周三
"""
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'v3'))

from generators.tomorrow_catalyst import TomorrowCatalystGenerator

# ========== 1. 创建生成器 ==========
gen = TomorrowCatalystGenerator(
    date_str="2026-07-29",
    subtitle="2026年7月29日 周三 · 超级央行周前夜 · 科技财报密集披露"
)

# ========== 2. 核心催化剂 ==========
key_catalyst = """
<b>五大核心催化</b>：① SK海力士Q2财报（存储超级周期验证）② 微软+Meta盘后财报（AI资本开支拷问）③ 美联储议息会议召开（7/28-29，决议周四凌晨）④ 第三届氟产业绿色发展创新大会开幕（半导体材料链）⑤ 上海机场百亿级限售解禁（全周最大单笔）
"""
gen.add_key_catalyst(key_catalyst.strip())

# ========== 3. 事件日历 ==========
events = [
    {
        'type': 'earnings',
        'title': 'SK海力士Q2财报发布',
        'description': '北京时间7月29日上午8:00发布二季度财报，市场预期营收84.1万亿韩元、营业利润64.1万亿韩元（同比+596%），HBM业务是核心看点。与英伟达7500亿美元长期协议后续进展受关注。',
        'category': '存储芯片 · AI算力'
    },
    {
        'type': 'earnings',
        'title': '微软FY26 Q4财报（盘后）',
        'description': '美股7月29日盘后发布（北京时间30日凌晨），市场一致预期营收约876-877亿美元、调整后EPS约4.21-4.24美元。Azure云增速、Copilot商业化进展、AI资本开支指引为三大核心关注点。',
        'category': 'AI算力 · 云服务'
    },
    {
        'type': 'earnings',
        'title': 'Meta Q2财报（盘后）',
        'description': '美股7月29日盘后发布，公司指引营收580-610亿美元。广告业务复苏与AI投入平衡是市场焦点，资本开支是否进一步上调将直接影响AI算力产业链情绪。',
        'category': 'AI应用 · 广告传媒'
    },
    {
        'type': 'earnings',
        'title': '高通FY26 Q3财报（盘后）',
        'description': '美股7月29日盘后发布，公司指引营收92-100亿美元、调整后EPS 2.10-2.30美元。手机业务底部确认、汽车业务50%增长、数据中心AI芯片进度三大看点。',
        'category': '半导体 · 汽车电子'
    },
    {
        'type': 'earnings',
        'title': '希捷科技FY26 Q4财报',
        'description': '7月28日盘后（北京时间29日清晨）发布全年及Q4财报，HDD需求复苏、AI数据中心存储订单是观察重点。',
        'category': '数据存储 · AI基础设施'
    },
    {
        'type': 'meeting',
        'title': '第三届氟产业绿色发展创新大会',
        'description': '7月29日至31日在内蒙古包头举办，聚焦氟化工产业链绿色转型与高端化发展。电子级氢氟酸、含氟电子特气等半导体材料相关议题受关注，影响半导体材料板块情绪。',
        'category': '半导体材料 · 氟化工'
    },
    {
        'type': 'meeting',
        'title': '美联储FOMC议息会议（第一日）',
        'description': '美东时间7月28-29日召开（对应北京时间29-30日），利率决议将于7月30日凌晨2:00公布。市场预期维持利率3.50%-3.75%不变，但加息概率约36%。会议首日无重大声明。',
        'category': '宏观政策 · 全球流动性'
    },
    {
        'type': 'meeting',
        'title': '2026中国国际游戏开发者大会（CIGDC）',
        'description': '7月28日至30日在上海举办，聚焦AI游戏开发、AIGC内容创作、虚拟人等前沿方向。为ChinaJoy预热，持续催化游戏、传媒、AI应用板块。',
        'category': '游戏传媒 · AIGC'
    },
    {
        'type': 'data',
        'title': '美国EIA原油库存数据',
        'description': '7月29日公布美国至7月24日当周EIA原油库存及战略石油储备库存。中东局势缓和后油价大幅回落，库存数据将影响能源板块短期情绪。',
        'category': '大宗商品 · 能源'
    },
    {
        'type': 'data',
        'title': '央行隔夜逆回购操作（首日）',
        'description': '7月29日至31日每日开展6000亿元隔夜逆回购，8月3日开展3000亿元，合计投放2.1万亿元，意在匹配月末资金需求，维护流动性平稳。',
        'category': '国内流动性 · 货币政策'
    },
    {
        'type': 'policy',
        'title': '千岸科技北交所上市',
        'description': '千岸科技（920065）7月29日在北交所上市，发行价24.30元/股，发行市盈率10.28倍，主营跨境电商自有品牌，提示Amazon平台集中度风险与美国关税政策影响。',
        'category': '新股上市 · 跨境电商'
    },
    {
        'type': 'policy',
        'title': '珈凯生物北交所网上申购',
        'description': '珈凯生物（920165）7月29日网上申购，发行价19.26元/股，发行市盈率14.98倍。主营生物活性原料，应用于功能性护肤等领域。',
        'category': '新股申购 · 生物科技'
    },
]
gen.add_events_calendar(events)

# ========== 4. 业绩公告板块 ==========
earnings_stocks = [
    {'name': 'SK海力士', 'code': '000660.KS', 'type': 'Q2财报', 'growth': '+596%'},
    {'name': '微软', 'code': 'MSFT', 'type': 'FY26 Q4财报', 'growth': 'Azure +40%'},
    {'name': 'Meta', 'code': 'META', 'type': 'Q2财报', 'growth': '营收+22%'},
    {'name': '高通', 'code': 'QCOM', 'type': 'FY26 Q3财报', 'growth': '汽车+50%'},
    {'name': '希捷科技', 'code': 'STX', 'type': 'FY26 Q4财报', 'growth': 'HDD复苏'},
    {'name': '德明利', 'code': '001309', 'type': '限售解禁', 'growth': '中报+4943%'},
]
gen.add_earnings_announcements(earnings_stocks)

# ========== 5. 重要数据发布 ==========
data_list = [
    {'name': '美国EIA原油库存', 'prev': '待更新', 'expect': '关注去化速度', 'actual': '7月29日公布'},
    {'name': '央行6000亿逆回购', 'prev': 'MLF已续做', 'expect': '月末资金面平稳', 'actual': '7月29日操作'},
    {'name': '美联储会议首日', 'prev': '3.50%-3.75%', 'expect': '不变概率63.7%', 'actual': '决议30日凌晨'},
]
gen.add_data_release(data_list)

# ========== 6. 限售股解禁详情 ==========
unlock_analysis = """
<h3 style="color: #f87171; margin-bottom: 12px; font-size: 16px;">&#x1f513; 限售股解禁详情（7月29日）</h3>
<p style="margin-bottom: 10px;">本周（7.27-7.31）全市场42家公司限售股解禁，合计约22.84亿股，解禁市值约336亿元。<b style="color: #fbbf24;">7月29日为本周解禁高峰，单日约106.6亿元</b>。</p>

<table style="width: 100%; border-collapse: collapse; margin-bottom: 16px; font-size: 13px;">
  <thead>
    <tr style="background: rgba(248, 113, 113, 0.1);">
      <th style="padding: 10px 12px; text-align: left; border-bottom: 1px solid rgba(255,255,255,0.1); color: #f87171;">股票名称</th>
      <th style="padding: 10px 12px; text-align: center; border-bottom: 1px solid rgba(255,255,255,0.1); color: #f87171;">代码</th>
      <th style="padding: 10px 12px; text-align: right; border-bottom: 1px solid rgba(255,255,255,0.1); color: #f87171;">解禁市值</th>
      <th style="padding: 10px 12px; text-align: center; border-bottom: 1px solid rgba(255,255,255,0.1); color: #f87171;">占总股本</th>
      <th style="padding: 10px 12px; text-align: left; border-bottom: 1px solid rgba(255,255,255,0.1); color: #f87171;">解禁类型</th>
    </tr>
  </thead>
  <tbody>
    <tr style="border-bottom: 1px solid rgba(255,255,255,0.05);">
      <td style="padding: 10px 12px; color: #e2e8f0;"><b>上海机场</b> &#x26a0;&#xfe0f;</td>
      <td style="padding: 10px 12px; text-align: center; color: #94a3b8;">600009</td>
      <td style="padding: 10px 12px; text-align: right; color: #fbbf24;"><b>102.84亿</b></td>
      <td style="padding: 10px 12px; text-align: center; color: #94a3b8;">17.44%</td>
      <td style="padding: 10px 12px; color: #94a3b8;">定增机构配售</td>
    </tr>
    <tr style="border-bottom: 1px solid rgba(255,255,255,0.05);">
      <td style="padding: 10px 12px; color: #e2e8f0;">正元地信</td>
      <td style="padding: 10px 12px; text-align: center; color: #94a3b8;">688509</td>
      <td style="padding: 10px 12px; text-align: right; color: #f87171;">约12.7亿</td>
      <td style="padding: 10px 12px; text-align: center; color: #f87171;">50.03%</td>
      <td style="padding: 10px 12px; color: #94a3b8;">定增+首发限售</td>
    </tr>
    <tr style="border-bottom: 1px solid rgba(255,255,255,0.05);">
      <td style="padding: 10px 12px; color: #e2e8f0;">申达股份</td>
      <td style="padding: 10px 12px; text-align: center; color: #94a3b8;">600626</td>
      <td style="padding: 10px 12px; text-align: right; color: #94a3b8;">约2.84亿</td>
      <td style="padding: 10px 12px; text-align: center; color: #94a3b8;">7.25%</td>
      <td style="padding: 10px 12px; color: #94a3b8;">定向增发</td>
    </tr>
    <tr style="border-bottom: 1px solid rgba(255,255,255,0.05);">
      <td style="padding: 10px 12px; color: #e2e8f0;">岱勒新材</td>
      <td style="padding: 10px 12px; text-align: center; color: #94a3b8;">300700</td>
      <td style="padding: 10px 12px; text-align: right; color: #94a3b8;">约4.65亿</td>
      <td style="padding: 10px 12px; text-align: center; color: #94a3b8;">19.13%</td>
      <td style="padding: 10px 12px; color: #94a3b8;">定向增发</td>
    </tr>
    <tr>
      <td style="padding: 10px 12px; color: #e2e8f0;">德明利</td>
      <td style="padding: 10px 12px; text-align: center; color: #94a3b8;">001309</td>
      <td style="padding: 10px 12px; text-align: right; color: #22c55e;">约0.93亿</td>
      <td style="padding: 10px 12px; text-align: center; color: #22c55e;">0.80%</td>
      <td style="padding: 10px 12px; color: #94a3b8;">定增（董事长不减持）</td>
    </tr>
  </tbody>
</table>

<p style="font-size: 13px; color: #94a3b8; line-height: 1.7;">
<b style="color: #f87171;">&#x26a0;&#xfe0f; 重点风险提示：</b>上海机场102.84亿解禁为本周最大单笔，解禁主体为定增机构，短期减持不确定性高；正元地信解禁比例达50.03%，流通筹码翻倍，需警惕抛压。德明利虽有解禁，但董事长李虎已自愿承诺12个月内不减持，实际影响有限。
</p>
"""
gen.add_impact_analysis(unlock_analysis)

# ========== 7. 新股申购与上市 ==========
ipo_analysis = """
<h3 style="color: #a78bfa; margin-bottom: 12px; font-size: 16px;">&#x1f4c8; 新股申购与上市（7月29日）</h3>
<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-bottom: 16px;">
  <div style="background: rgba(167, 139, 250, 0.08); border: 1px solid rgba(167, 139, 250, 0.2); border-radius: 12px; padding: 14px;">
    <div style="font-weight: bold; color: #e2e8f0; font-size: 14px; margin-bottom: 6px;">千岸科技（920065）&#xb7; 上市</div>
    <div style="font-size: 12px; color: #94a3b8; line-height: 1.6;">
      &#x1f3f7;&#xfe0f; 发行价：<b style="color: #c4b5fd;">24.30元/股</b><br>
      &#x1f4ca; 发行市盈率：10.28倍<br>
      &#x1f3ed; 行业：跨境电商/自有品牌<br>
      &#x1f4b0; 募资总额：4.25亿元<br>
      &#x26a0;&#xfe0f; 风险：Amazon平台集中度85.55%、美国关税政策影响
    </div>
  </div>
  <div style="background: rgba(167, 139, 250, 0.08); border: 1px solid rgba(167, 139, 250, 0.2); border-radius: 12px; padding: 14px;">
    <div style="font-weight: bold; color: #e2e8f0; font-size: 14px; margin-bottom: 6px;">珈凯生物（920165）&#xb7; 申购</div>
    <div style="font-size: 12px; color: #94a3b8; line-height: 1.6;">
      &#x1f3f7;&#xfe0f; 发行价：<b style="color: #c4b5fd;">19.26元/股</b><br>
      &#x1f4ca; 发行市盈率：14.98倍<br>
      &#x1f3ed; 行业：生物活性原料/功能性护肤<br>
      &#x1f4b0; 募资总额：约1.40亿元<br>
      &#x1f3af; 申购建议：行业景气度尚可，可参与
    </div>
  </div>
</div>
<p style="font-size: 13px; color: #94a3b8; line-height: 1.6;">
本周其他新股：超纯应材、国仪公司将于7月31日申购。长鑫科技（688825）已于7月27日科创板上市，为年内最大IPO。
</p>
"""
gen.add_impact_analysis(ipo_analysis)

# ========== 8. 核心催化深度分析（Top 5）==========
deep_analysis = """
<h3 style="color: #fbbf24; margin-bottom: 16px; font-size: 18px;">&#x1f525; 五大核心催化深度分析</h3>

<!-- 催化1 -->
<div style="background: linear-gradient(135deg, rgba(251, 191, 36, 0.1) 0%, rgba(245, 158, 11, 0.05) 100%); 
            border: 1px solid rgba(251, 191, 36, 0.25); border-radius: 14px; padding: 18px; margin-bottom: 16px;">
  <div style="display: flex; align-items: center; margin-bottom: 12px;">
    <span style="background: linear-gradient(135deg, #f59e0b, #d97706); color: white; padding: 3px 10px; border-radius: 6px; font-size: 12px; font-weight: bold; margin-right: 10px;">催化一</span>
    <span style="font-size: 16px; font-weight: bold; color: #fef3c7;">SK海力士Q2财报：存储超级周期的验证时刻</span>
  </div>
  <div style="font-size: 13px; color: #e2e8f0; line-height: 1.8;">
    <p style="margin-bottom: 10px;"><b style="color: #fbbf24;">事件时间：</b>7月29日上午8:00（北京时间）发布财报，随后召开双语电话会议</p>
    <p style="margin-bottom: 10px;"><b style="color: #fbbf24;">市场预期：</b>营收84.1万亿韩元（约437亿美元），营业利润64.1万亿韩元，同比增长<b>+596%</b>，营业利润率75%-77%。这一数字将超越该公司2025年全年47.2万亿韩元的营业利润纪录。上半年营利即突破100万亿韩元，超越去年全年利润。</p>
    <p style="margin-bottom: 10px;"><b style="color: #fbbf24;">核心看点：</b>① HBM出货量与ASP走势，AI数据中心收入占比是否达到70%；② 第三季度业绩指引，DRAM/NAND涨价趋势能否延续至2027年；③ 与英伟达7500亿美元五年长期供应协议的后续细节；④ 海力士股价从高点腰斩后（下跌约45%），财报能否成为股价拐点。市场分歧在于：一方认为涨价周期已近峰值，另一方认为LTA长期协议让盈利可见性大幅提升。</p>
    <p style="margin-bottom: 10px;"><b style="color: #fbbf24;">影响标的：</b>
      <span style="background: rgba(251, 191, 36, 0.15); padding: 2px 8px; border-radius: 4px; margin-right: 6px; font-size: 12px;">长鑫科技 688825</span>
      <span style="background: rgba(251, 191, 36, 0.15); padding: 2px 8px; border-radius: 4px; margin-right: 6px; font-size: 12px;">兆易创新 603986</span>
      <span style="background: rgba(251, 191, 36, 0.15); padding: 2px 8px; border-radius: 4px; margin-right: 6px; font-size: 12px;">北京君正 300223</span>
      <span style="background: rgba(251, 191, 36, 0.15); padding: 2px 8px; border-radius: 4px; margin-right: 6px; font-size: 12px;">德明利 001309</span>
      <span style="background: rgba(251, 191, 36, 0.15); padding: 2px 8px; border-radius: 4px; margin-right: 6px; font-size: 12px;">江波龙 301308</span>
      <span style="background: rgba(251, 191, 36, 0.15); padding: 2px 8px; border-radius: 4px; margin-right: 6px; font-size: 12px;">佰维存储 688525</span>
    </p>
    <p style="margin-bottom: 0;"><b style="color: #fbbf24;">操作建议：</b>存储板块近期经历深度调整（SK海力士ADR跌超40%），SK海力士业绩若超预期并给出乐观指引，有望成为板块修复催化剂。建议关注HBM产业链、国产存储替代主线，但需警惕"利好兑现"风险——如果财报符合预期但指引偏保守，可能进一步压制情绪。短线交易者宜等待财报落地后再做方向判断。中长线投资者可逢低布局有真实业绩支撑的国产存储龙头。</p>
  </div>
</div>

<!-- 催化2 -->
<div style="background: linear-gradient(135deg, rgba(59, 130, 246, 0.1) 0%, rgba(139, 92, 246, 0.05) 100%); 
            border: 1px solid rgba(59, 130, 246, 0.25); border-radius: 14px; padding: 18px; margin-bottom: 16px;">
  <div style="display: flex; align-items: center; margin-bottom: 12px;">
    <span style="background: linear-gradient(135deg, #3b82f6, #8b5cf6); color: white; padding: 3px 10px; border-radius: 6px; font-size: 12px; font-weight: bold; margin-right: 10px;">催化二</span>
    <span style="font-size: 16px; font-weight: bold; color: #bfdbfe;">微软+Meta盘后财报：AI资本开支的压力测试</span>
  </div>
  <div style="font-size: 13px; color: #e2e8f0; line-height: 1.8;">
    <p style="margin-bottom: 10px;"><b style="color: #60a5fa;">事件时间：</b>7月29日美股盘后（北京时间30日凌晨4:30-5:30）</p>
    <p style="margin-bottom: 10px;"><b style="color: #60a5fa;">微软看点：</b>市场一致预期营收876-877亿美元、调整后EPS 4.21-4.24美元。法国巴黎银行预计Azure增速约41%（高于市场共识的40%）。市场重点关注：① Copilot商业化进展与付费用户渗透率；② FY27资本开支指引是否继续上调；③ AI服务的利润率变化趋势；④ 与英伟达的AI合作细节。</p>
    <p style="margin-bottom: 10px;"><b style="color: #60a5fa;">Meta看点：</b>公司指引Q2营收580-610亿美元，广告业务复苏动能与Reels增长是基本盘。核心拷问在于AI资本开支——Meta此前已大幅上调全年capex，若进一步上调可能引发市场对"投入大于产出"的担忧，重演Alphabet财报后的回调。Llama系列开源大模型的商业化进展也值得关注。</p>
    <p style="margin-bottom: 10px;"><b style="color: #60a5fa;">产业传导：</b>两家科技巨头的财报合起来堪称AI产业链的"期中考试"。如果云厂商继续扩大资本开支并确认AI需求持续性，则CPO光模块、AI服务器、PCB、液冷、高速连接器、存储芯片、半导体设备等上游链条将获得支撑。反之，若出现"增收不增利"或资本开支放缓信号，则整个AI算力链可能面临估值回调。</p>
    <p style="margin-bottom: 10px;"><b style="color: #60a5fa;">影响标的：</b>
      <span style="background: rgba(59, 130, 246, 0.15); padding: 2px 8px; border-radius: 4px; margin-right: 6px; font-size: 12px;">中际旭创 300308</span>
      <span style="background: rgba(59, 130, 246, 0.15); padding: 2px 8px; border-radius: 4px; margin-right: 6px; font-size: 12px;">新易盛 300502</span>
      <span style="background: rgba(59, 130, 246, 0.15); padding: 2px 8px; border-radius: 4px; margin-right: 6px; font-size: 12px;">工业富联 601138</span>
      <span style="background: rgba(59, 130, 246, 0.15); padding: 2px 8px; border-radius: 4px; margin-right: 6px; font-size: 12px;">浪潮信息 000977</span>
      <span style="background: rgba(59, 130, 246, 0.15); padding: 2px 8px; border-radius: 4px; margin-right: 6px; font-size: 12px;">寒武纪 688256</span>
      <span style="background: rgba(59, 130, 246, 0.15); padding: 2px 8px; border-radius: 4px; margin-right: 6px; font-size: 12px;">沪电股份 002463</span>
    </p>
    <p style="margin-bottom: 0;"><b style="color: #60a5fa;">操作建议：</b>科技财报集中在周三盘后公布，A股周四开盘将直面业绩影响。建议周三适度降低算力链仓位的敞口，等待财报靴子落地。若云厂商资本开支指引稳健、AI收入增长匹配投入，则光模块、AI服务器方向有望迎来修复；反之则需警惕进一步下探风险。仓位较重的投资者可考虑利用期权或对冲工具保护持仓。</p>
  </div>
</div>

<!-- 催化3 -->
<div style="background: linear-gradient(135deg, rgba(239, 68, 68, 0.1) 0%, rgba(249, 115, 22, 0.05) 100%); 
            border: 1px solid rgba(239, 68, 68, 0.25); border-radius: 14px; padding: 18px; margin-bottom: 16px;">
  <div style="display: flex; align-items: center; margin-bottom: 12px;">
    <span style="background: linear-gradient(135deg, #ef4444, #f97316); color: white; padding: 3px 10px; border-radius: 6px; font-size: 12px; font-weight: bold; margin-right: 10px;">催化三</span>
    <span style="font-size: 16px; font-weight: bold; color: #fecaca;">美联储议息会议：沃什时代的"猜谜大会"</span>
  </div>
  <div style="font-size: 13px; color: #e2e8f0; line-height: 1.8;">
    <p style="margin-bottom: 10px;"><b style="color: #f87171;">事件时间：</b>美东7.28-29日会议，决议北京时间7月30日（周四）凌晨2:00公布，2:30主席沃什新闻发布会</p>
    <p style="margin-bottom: 10px;"><b style="color: #f87171;">市场预期：</b>CME FedWatch显示维持利率3.50%-3.75%不变概率<b>63.7%</b>，加息25bp概率<b>36.3%</b>。本次会议不发布点阵图和季度经济预测（SEP），仅靠声明和讲话解读，波动性可能更大。9月加息预期更为强烈，市场定价9月加息概率超55%。</p>
    <p style="margin-bottom: 10px;"><b style="color: #f87171;">核心变量：</b>① 新任主席沃什的沟通风格——已抛弃前瞻指引，强调"逐次会议决定"；② 油价暴跌（7月27日跌逾8%）是否缓和通胀担忧；③ 特朗普"全球最低利率"喊话的政治干扰；④ 内部鹰鸽分歧——若反对票超2张将被视为强烈鹰派信号；⑤ 关税政策对通胀的长期影响评估。</p>
    <p style="margin-bottom: 10px;"><b style="color: #f87171;">A股传导路径：</b>美联储政策直接影响美债收益率和美元指数，进而左右北向资金流向和人民币汇率。若表态偏鸽，美债收益率回落，科技成长估值压力减轻，恒生科技和科创50有望修复；若偏鹰甚至意外加息，银行、保险、央企红利和资源板块相对占优，高估值成长股承压。</p>
    <p style="margin-bottom: 10px;"><b style="color: #f87171;">影响标的：</b>
      <span style="background: rgba(239, 68, 68, 0.15); padding: 2px 8px; border-radius: 4px; margin-right: 6px; font-size: 12px;">山东黄金 600547</span>
      <span style="background: rgba(239, 68, 68, 0.15); padding: 2px 8px; border-radius: 4px; margin-right: 6px; font-size: 12px;">中金黄金 600489</span>
      <span style="background: rgba(239, 68, 68, 0.15); padding: 2px 8px; border-radius: 4px; margin-right: 6px; font-size: 12px;">招商银行 600036</span>
      <span style="background: rgba(239, 68, 68, 0.15); padding: 2px 8px; border-radius: 4px; margin-right: 6px; font-size: 12px;">中国平安 601318</span>
      <span style="background: rgba(239, 68, 68, 0.15); padding: 2px 8px; border-radius: 4px; margin-right: 6px; font-size: 12px;">恒生科技ETF 513130</span>
    </p>
    <p style="margin-bottom: 0;"><b style="color: #f87171;">操作建议：</b>周三为议息会议首日，无重大声明，但市场情绪将偏向谨慎观望。真正的方向选择在周四凌晨决议公布后。建议周三降低高成长、高估值仓位的杠杆，控制整体仓位在中性水平。若决议偏鸽（维持+温和措辞），科技成长有望反弹，可关注科创50和恒生科技的修复机会；若偏鹰甚至意外加息，红利防御、银行保险相对占优，黄金可能短期承压但中长期逻辑不变。</p>
  </div>
</div>

<!-- 催化4 -->
<div style="background: linear-gradient(135deg, rgba(16, 185, 129, 0.1) 0%, rgba(6, 182, 212, 0.05) 100%); 
            border: 1px solid rgba(16, 185, 129, 0.25); border-radius: 14px; padding: 18px; margin-bottom: 16px;">
  <div style="display: flex; align-items: center; margin-bottom: 12px;">
    <span style="background: linear-gradient(135deg, #10b981, #06b6d4); color: white; padding: 3px 10px; border-radius: 6px; font-size: 12px; font-weight: bold; margin-right: 10px;">催化四</span>
    <span style="font-size: 16px; font-weight: bold; color: #a7f3d0;">第三届氟产业绿色发展创新大会：半导体材料链的催化窗口</span>
  </div>
  <div style="font-size: 13px; color: #e2e8f0; line-height: 1.8;">
    <p style="margin-bottom: 10px;"><b style="color: #34d399;">事件时间：</b>7月29日至31日在内蒙古包头市举办</p>
    <p style="margin-bottom: 10px;"><b style="color: #34d399;">会议看点：</b>① 氟化工产业绿色转型与高端化发展路线图；② 电子级氢氟酸、含氟电子特气等半导体材料的国产替代进展；③ 新能源（锂电电解液、PVDF）用氟材料需求展望；④ 环保政策趋严下的行业供给收缩预期；⑤ 第三代半导体（碳化硅）用含氟材料发展。</p>
    <p style="margin-bottom: 10px;"><b style="color: #34d399;">产业背景：</b>半导体材料是国产替代攻坚的核心领域，电子级氢氟酸（UPSS级）、三氟化氮、六氟化钨等含氟电子特气在芯片制造的刻蚀、清洗等关键工艺中不可或缺。随着国内晶圆厂扩产持续（2026年国内12英寸晶圆产能预计增长超20%），半导体材料的"卡脖子"环节替代加速。叠加存储芯片超级周期，上游氟化工电子材料需求有望持续高增。</p>
    <p style="margin-bottom: 10px;"><b style="color: #34d399;">制冷剂景气度：</b>除了半导体材料，氟化工另一支柱——制冷剂同样处于景气上行通道。三代制冷剂配额管理实施后，行业供给刚性增强，下游需求复苏带动价格持续上涨。这是氟化工企业业绩的重要支撑。</p>
    <p style="margin-bottom: 10px;"><b style="color: #34d399;">影响标的：</b>
      <span style="background: rgba(16, 185, 129, 0.15); padding: 2px 8px; border-radius: 4px; margin-right: 6px; font-size: 12px;">巨化股份 600160</span>
      <span style="background: rgba(16, 185, 129, 0.15); padding: 2px 8px; border-radius: 4px; margin-right: 6px; font-size: 12px;">多氟多 002407</span>
      <span style="background: rgba(16, 185, 129, 0.15); padding: 2px 8px; border-radius: 4px; margin-right: 6px; font-size: 12px;">永太科技 002326</span>
      <span style="background: rgba(16, 185, 129, 0.15); padding: 2px 8px; border-radius: 4px; margin-right: 6px; font-size: 12px;">昊华科技 600378</span>
      <span style="background: rgba(16, 185, 129, 0.15); padding: 2px 8px; border-radius: 4px; margin-right: 6px; font-size: 12px;">雅克科技 002409</span>
      <span style="background: rgba(16, 185, 129, 0.15); padding: 2px 8px; border-radius: 4px; margin-right: 6px; font-size: 12px;">三美股份 603379</span>
    </p>
    <p style="margin-bottom: 0;"><b style="color: #34d399;">操作建议：</b>氟化工板块兼具半导体材料国产替代（成长逻辑）+制冷剂配额（供给收缩逻辑）+新能源材料（需求增长逻辑）三重催化。会议期间可关注电子特气、电子级氢氟酸相关标的的异动，重点跟踪有实际半导体客户验证进展的公司。建议关注行业龙头巨化股份（制冷剂+电子特气双轮驱动）和有明确半导体材料业务的昊华科技、雅克科技。</p>
  </div>
</div>

<!-- 催化5 -->
<div style="background: linear-gradient(135deg, rgba(249, 115, 22, 0.1) 0%, rgba(234, 88, 12, 0.05) 100%); 
            border: 1px solid rgba(249, 115, 22, 0.25); border-radius: 14px; padding: 18px;">
  <div style="display: flex; align-items: center; margin-bottom: 12px;">
    <span style="background: linear-gradient(135deg, #f97316, #ea580c); color: white; padding: 3px 10px; border-radius: 6px; font-size: 12px; font-weight: bold; margin-right: 10px;">催化五</span>
    <span style="font-size: 16px; font-weight: bold; color: #fed7aa;">上海机场百亿解禁：本周最大风险点与航空复苏的博弈</span>
  </div>
  <div style="font-size: 13px; color: #e2e8f0; line-height: 1.8;">
    <p style="margin-bottom: 10px;"><b style="color: #fb923c;">事件概况：</b>上海机场（600009）7月29日将有4.34亿股定增机构配售股份解禁，解禁市值约102.84亿元，占总股本17.44%，为本周A股最大单笔解禁，也是唯一超百亿的解禁个股。</p>
    <p style="margin-bottom: 10px;"><b style="color: #fb923c;">解禁背景：</b>本次解禁来源于2023年的定增发行，参与机构包括多家公募基金、保险资管和产业资本。由于发行价格远低于当前市价，机构持仓浮盈丰厚，存在一定的减持动力。在当前市场环境偏弱、量能萎缩（两市成交跌破2万亿）的背景下，百亿级解禁对个股短期承压明显。</p>
    <p style="margin-bottom: 10px;"><b style="color: #fb923c;">航空业基本面：</b>暑期出行旺季持续，国际航线恢复进度加快，航空需求景气度较高。国际客流恢复至2019年同期约85%-90%水平，免税消费回流趋势明显。但油价波动（中东局势反复）、汇率因素仍对航企盈利构成扰动。机场作为航空产业链的"收租者"，受益于客流复苏确定性更高，且免税业务弹性大。</p>
    <p style="margin-bottom: 10px;"><b style="color: #fb923c;">同类对比：</b>本周其他大额解禁包括富乐德（约48亿，7月27日）、西安奕材-U（约26亿，7月28日）等，但上海机场所属的机场航运板块更具板块效应，其解禁可能影响整个交运板块的情绪。正元地信（解禁比例50.03%）则需警惕高比例原始股解禁的抛压风险。</p>
    <p style="margin-bottom: 10px;"><b style="color: #fb923c;">影响标的：</b>
      <span style="background: rgba(249, 115, 22, 0.15); padding: 2px 8px; border-radius: 4px; margin-right: 6px; font-size: 12px;">上海机场 600009</span>
      <span style="background: rgba(249, 115, 22, 0.15); padding: 2px 8px; border-radius: 4px; margin-right: 6px; font-size: 12px;">白云机场 600004</span>
      <span style="background: rgba(249, 115, 22, 0.15); padding: 2px 8px; border-radius: 4px; margin-right: 6px; font-size: 12px;">中国国航 601111</span>
      <span style="background: rgba(249, 115, 22, 0.15); padding: 2px 8px; border-radius: 4px; margin-right: 6px; font-size: 12px;">南方航空 600029</span>
      <span style="background: rgba(249, 115, 22, 0.15); padding: 2px 8px; border-radius: 4px; margin-right: 6px; font-size: 12px;">中国中免 601888</span>
    </p>
    <p style="margin-bottom: 0;"><b style="color: #fb923c;">操作建议：</b>短期回避上海机场解禁窗口期的不确定性，不建议在解禁前追高。若解禁后出现非理性下跌、基本面未变，则可能提供中期布局机会——机场板块受益于国际客流持续复苏和免税消费回流的逻辑仍然成立。对已持有投资者而言，建议关注解禁后量价关系，若缩量企稳可继续持有；若放量大跌则需减仓避险。同时可关注相对不受解禁影响、但同样受益于出行复苏的白云机场和中国中免。</p>
  </div>
</div>
"""
gen.add_impact_analysis(deep_analysis)

# ========== 9. 海外大事提醒 ==========
overseas_section = """
<h3 style="color: #60a5fa; margin-bottom: 12px; font-size: 16px;">&#x1f30d; 海外大事提醒（本周后续）</h3>
<div style="display: flex; flex-direction: column; gap: 10px;">
  
  <div style="background: rgba(96, 165, 250, 0.08); border-left: 3px solid #3b82f6; border-radius: 0 10px 10px 0; padding: 12px 14px;">
    <div style="font-weight: bold; color: #93c5fd; font-size: 13px; margin-bottom: 4px;">&#x1f4c5; 7月30日（周四）&#xb7; 超级星期四</div>
    <div style="font-size: 12px; color: #94a3b8; line-height: 1.6;">
      &#x2022; 美联储利率决议 + 沃什发布会（凌晨2:00）<br>
      &#x2022; 美国6月核心PCE物价指数 + Q2 GDP初值<br>
      &#x2022; 英国央行利率决议（预期维持3.75%）<br>
      &#x2022; 三星电子Q2完整版财报<br>
      &#x2022; 苹果、亚马逊财报（盘后）<br>
      &#x2022; 中际旭创H股港股挂牌（03308.HK）
    </div>
  </div>
  
  <div style="background: rgba(96, 165, 250, 0.08); border-left: 3px solid #8b5cf6; border-radius: 0 10px 10px 0; padding: 12px 14px;">
    <div style="font-weight: bold; color: #c4b5fd; font-size: 13px; margin-bottom: 4px;">&#x1f4c5; 7月31日（周五）&#xb7; 数据+财报双高峰</div>
    <div style="font-size: 12px; color: #94a3b8; line-height: 1.6;">
      &#x2022; 中国7月官方制造业PMI（09:30）<br>
      &#x2022; 日本央行利率决议（预期维持1.0%）<br>
      &#x2022; 美国7月密歇根大学消费者信心终值<br>
      &#x2022; 铠侠Q1财报（存储三雄收尾）<br>
      &#x2022; 第12批国家药品集采上海开标（65个品种）<br>
      &#x2022; ChinaJoy 2026上海开幕（7.31-8.3）<br>
      &#x2022; 国内成品油新一轮调价窗口
    </div>
  </div>
  
  <div style="background: rgba(96, 165, 250, 0.08); border-left: 3px solid #f59e0b; border-radius: 0 10px 10px 0; padding: 12px 14px;">
    <div style="font-weight: bold; color: #fcd34d; font-size: 13px; margin-bottom: 4px;">&#x1f4c5; 7月30日-8月1日 &#xb7; 产业会议密集</div>
    <div style="font-size: 12px; color: #94a3b8; line-height: 1.6;">
      &#x2022; 2026人工智能产品应用博览会（苏州国际博览中心）<br>
      &nbsp;&nbsp;近400家展商，华为昇腾950、零一万物、九识智能等亮相<br>
      &nbsp;&nbsp;9大核心板块 + 10+场主题交流会<br>
      &#x2022; 2026中国国际游戏开发者大会（上海，7.28-30）<br>
      &nbsp;&nbsp;聚焦AI游戏、AIGC、虚拟人等前沿方向
    </div>
  </div>
  
</div>
"""
gen.add_impact_analysis(overseas_section)

# ========== 10. 本周事件日历表格 ==========
weekly_calendar = """
<h3 style="color: #fbbf24; margin-bottom: 12px; font-size: 16px;">&#x1f4c5; 本周事件日历（7.27-7.31）</h3>
<table style="width: 100%; border-collapse: collapse; font-size: 12.5px;">
  <thead>
    <tr style="background: rgba(251, 191, 36, 0.1);">
      <th style="padding: 8px 10px; text-align: center; border-bottom: 1px solid rgba(255,255,255,0.1); color: #fbbf24; width: 80px;">日期</th>
      <th style="padding: 8px 10px; text-align: left; border-bottom: 1px solid rgba(255,255,255,0.1); color: #fbbf24;">国内事件</th>
      <th style="padding: 8px 10px; text-align: left; border-bottom: 1px solid rgba(255,255,255,0.1); color: #fbbf24;">海外事件</th>
    </tr>
  </thead>
  <tbody>
    <tr style="border-bottom: 1px solid rgba(255,255,255,0.05);">
      <td style="padding: 8px 10px; text-align: center; color: #94a3b8; font-weight: bold;">周一<br>7.27</td>
      <td style="padding: 8px 10px; color: #e2e8f0;">工业企业利润数据 | 长鑫科技科创板上市 | 内幕交易新规施行 | APEC林业部长级会议</td>
      <td style="padding: 8px 10px; color: #94a3b8;">阿斯利康财报 | 油价暴跌逾8% | 特朗普喊话"全球最低利率"</td>
    </tr>
    <tr style="border-bottom: 1px solid rgba(255,255,255,0.05);">
      <td style="padding: 8px 10px; text-align: center; color: #94a3b8; font-weight: bold;">周二<br>7.28</td>
      <td style="padding: 8px 10px; color: #e2e8f0;">CIGDC游戏开发者大会开幕 | 荣耀影像技术发布会 | 格科微/北汽蓝谷解禁</td>
      <td style="padding: 8px 10px; color: #94a3b8;">美国ADP就业+消费者信心 | 康宁/波音财报 | 希捷财报</td>
    </tr>
    <tr style="border-bottom: 1px solid rgba(255,255,255,0.05); background: rgba(251, 191, 36, 0.06);">
      <td style="padding: 8px 10px; text-align: center; color: #fbbf24; font-weight: bold;">周三<br>7.29 &#x2b50;</td>
      <td style="padding: 8px 10px; color: #e2e8f0;"><b>氟产业创新大会开幕</b> | 上海机场百亿解禁 | 央行6000亿逆回购首日 | 千岸科技上市/珈凯生物申购 | 正元地信/岱勒新材解禁</td>
      <td style="padding: 8px 10px; color: #e2e8f0;"><b style="color: #fbbf24;">SK海力士Q2财报</b> | 微软/Meta/高通财报(盘后) | 美联储会议首日 | EIA原油库存</td>
    </tr>
    <tr style="border-bottom: 1px solid rgba(255,255,255,0.05);">
      <td style="padding: 8px 10px; text-align: center; color: #f87171; font-weight: bold;">周四<br>7.30 &#x1f525;</td>
      <td style="padding: 8px 10px; color: #e2e8f0;">苏州AI智博会开幕 | 中际旭创H股上市 | 文化产业数据 | 晶丰明源解禁</td>
      <td style="padding: 8px 10px; color: #e2e8f0;"><b style="color: #f87171;">美联储利率决议</b> | 美国Q2 GDP+PCE | 英国央行决议 | 三星/苹果/亚马逊财报</td>
    </tr>
    <tr>
      <td style="padding: 8px 10px; text-align: center; color: #a78bfa; font-weight: bold;">周五<br>7.31</td>
      <td style="padding: 8px 10px; color: #e2e8f0;">7月官方PMI | 第12批药品集采开标 | ChinaJoy开幕 | 外汇/贸易数据 | 成品油调价 | 超纯应材/国仪申购</td>
      <td style="padding: 8px 10px; color: #e2e8f0;">日本央行决议 | 美国密歇根信心指数 | 铠侠财报 | 埃克森美孚/雪佛龙财报</td>
    </tr>
  </tbody>
</table>
"""
gen.add_impact_analysis(weekly_calendar)

# ========== 11. 催化深度分析（Skill增强）==========
catalyst_deep_events = [
    {
        'type': 'earnings',
        'title': 'SK海力士Q2财报',
        'description': 'AI存储超级周期验证，HBM龙头业绩历史新高',
        'category': '存储芯片'
    },
    {
        'type': 'policy',
        'title': '美联储议息会议',
        'description': '沃什时代首次议息，加息与否悬而未决',
        'category': '宏观政策'
    },
    {
        'type': 'earnings',
        'title': '微软+Meta科技财报',
        'description': 'AI资本开支与商业化的压力测试',
        'category': 'AI算力'
    },
]
gen.add_catalyst_deep_analysis(catalyst_deep_events)

# ========== 12. 风险提示 ==========
risks = [
    "美联储议息会议结果超预期偏鹰，美债收益率上行压制全球成长股估值",
    "科技巨头财报不及预期或AI资本开支指引下调，引发算力产业链情绪杀跌",
    "SK海力士财报符合预期但指引偏保守，存储板块利好兑现后继续调整",
    "上海机场百亿解禁引发航空机场板块短期抛压，拖累大消费情绪",
    "中东地缘局势反复，油价大幅波动影响通胀预期与全球市场风险偏好",
    "月末资金面波动叠加长鑫科技上市虹吸效应，A股流动性阶段性收紧",
    "半年报密集披露期部分公司业绩暴雷，引发个股及板块情绪杀跌",
    "中美关税摩擦升级，出口链及科技板块承压"
]
gen.add_risk_warning(risks)

# ========== 13. 生成并发布 ==========
print("正在生成报告...")
html = gen.generate()
print(f"报告生成完成，长度: {len(html)} 字符")

# 验证
errors = gen.validate()
if errors:
    print(f"验证问题: {errors}")
else:
    print("验证通过 ✓")

# 发布
print("正在发布...")
result = gen.publish(
    title="明日催化剂 | 2026年7月29日",
    excerpt="超级央行周前夜 · SK海力士Q2财报+微软Meta财报双响 · 百亿解禁来袭 · 氟产业大会催化半导体材料",
    auto_deploy=True
)
print(f"发布结果: {result}")
