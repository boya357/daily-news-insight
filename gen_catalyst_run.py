import sys, os
os.chdir('/root/daily-news-insight')
sys.path.insert(0, '/root/daily-news-insight/v3')

from v3.generators.tomorrow_catalyst import TomorrowCatalystGenerator

gen = TomorrowCatalystGenerator(
    date_str="20260923",
    subtitle="2026.09.23 · 明日催化剂"
)

# ============ 1. 核心催化剂 ============
gen.add_key_catalyst("""
<b>【S级·习近平主席访美】</b>9月23日至25日，应美国总统特朗普邀请，国家主席习近平对美国进行国事访问。两国元首时隔4个月再度会晤，将为中美建设性战略稳定关系行稳致远提供战略引领。此访是2026年中美关系最重要的外交事件，经贸合作、AI治理、半导体、气候变化等议题料成焦点，中美贸易指数9月以来已累计上涨超3.4%。<br><br>
<b>【A级·中金公司复牌】</b>中金公司(601995)A股股票9月23日开市起复牌，换股吸收合并东兴证券、信达证券的"三合一"重组迈出关键一步。交易规模高达1139亿元，合并后总资产将超万亿、净利润超百亿、营收升至行业第三，有望重塑券商行业格局。<br><br>
<b>【A级·双场国新办发布会】</b>上午10时教育部发布会介绍"加快推进教育强国建设"；下午3时民政部发布会介绍"十五五"时期民政事业高质量发展。教育+养老双主题同日发声，教育信息化、养老服务板块迎政策催化。
""")

# ============ 2. 明日事件日历 ============
events = [
    {
        'type': 'meeting',
        'title': '习近平主席对美国进行国事访问',
        'description': '应美国总统特朗普邀请，国家主席习近平9月23日至25日对美国进行国事访问。两国元首将为中美建设性战略稳定关系提供战略引领。经贸合作、AI治理、半导体合作、气候变化等议题料成焦点。',
        'category': '元首外交 · S级'
    },
    {
        'type': 'general',
        'title': '中金公司A股复牌 千亿级券商重组落地',
        'description': '中金公司(601995)9月23日开市起复牌。换股吸收合并东兴证券、信达证券获证监会核准，新增发行A股约31.04亿股，交易规模1139亿元。合并后总资产将超万亿、营收升至行业第三。',
        'category': '证券市场 · A级'
    },
    {
        'type': 'policy',
        'title': '国新办：加快推进教育强国建设发布会',
        'description': '9月23日上午10时，教育部副部长杜江峰、王光彦介绍贯彻落实"十五五"规划，加快推进教育强国建设有关情况并答记者问。关注教育信息化、AI+教育、职业教育方向。',
        'category': '政策发布 · A级'
    },
    {
        'type': 'policy',
        'title': '国新办：民政事业高质量发展发布会',
        'description': '9月23日下午3时，民政部部长李常官介绍"十五五"时期推进民政事业高质量发展有关情况。养老服务、社区治理、社会救助等领域政策有望明确，养老产业迎催化。',
        'category': '政策发布 · B级'
    },
    {
        'type': 'meeting',
        'title': '2026云栖大会（持续）',
        'description': '9月22日开幕的云栖大会以"智以致用"为主题，Agentic AI为核心锚点。阿里云发布灵骏真武M890超节点、AgentCore智能体构建平台、Wan 3.0视频大模型等重磅产品，AI智能体产业链持续催化。',
        'category': '科技盛会 · A级'
    },
    {
        'type': 'meeting',
        'title': '第五届全球数字贸易博览会',
        'description': '第五届数贸会于9月23日举办，聚焦数字贸易、跨境电商、数据要素等议题。数字贸易、跨境支付、数据安全相关板块有望受关注。',
        'category': '行业展会 · B级'
    },
    {
        'type': 'data',
        'title': '周三11股限售股解禁 合计1.6亿股',
        'description': '9月23日共有11只A股面临解禁，合计约1.6亿股。首药控股解禁比例最高达56.96%（8471万股），友升股份解禁比例24.18%（4668万股），其余个股解禁比例均低于1%，整体压力可控。',
        'category': '解禁事件 · B级'
    },
    {
        'type': 'data',
        'title': '莫森泰克(920162)北交所新股申购',
        'description': '莫森泰克9月23日开启申购，发行价17.37元，发行市盈率10.00倍（行业均值22.47倍），申购上限76.5万股。公司主营汽车天窗、玻璃升降器等汽车开闭器件，国家级专精特新"小巨人"。',
        'category': '新股申购 · B级'
    },
    {
        'type': 'data',
        'title': '凯达重工(920025)北交所上市',
        'description': '凯达重工9月23日在北交所上市，发行价4.26元，网上中签率0.0182%。',
        'category': '新股上市 · B级'
    },
    {
        'type': 'data',
        'title': '国科转债、奥士转债申购',
        'description': '9月23日两只可转债申购：国科转债(123286，正股国科天成)、奥士转债(127117，正股奥士康)。',
        'category': '转债申购 · C级'
    },
    {
        'type': 'meeting',
        'title': '第三届储能安全大会/冶金展闭幕',
        'description': '2026第三届储能安全大会、第二十四届中国国际冶金工业展览会均于9月21-23日举办，23日为最后一日。储能安全、钢铁冶金板块前期已获事件驱动，关注闭幕成果发布。',
        'category': '行业展会 · C级'
    },
]

gen.add_events_calendar(events)

# ============ 3. 限售股解禁详情 ============
from components.layout import Section, SubCard
from components.data import StatCard

restriction_content = """
<div style="overflow-x: auto;">
<table style="width: 100%; border-collapse: collapse; font-size: 13px; color: #e2e8f0;">
<thead>
<tr style="border-bottom: 2px solid rgba(139, 92, 246, 0.3);">
<th style="text-align: left; padding: 10px 8px; color: #a78bfa;">股票代码</th>
<th style="text-align: left; padding: 10px 8px; color: #a78bfa;">股票简称</th>
<th style="text-align: right; padding: 10px 8px; color: #a78bfa;">解禁数量(万股)</th>
<th style="text-align: right; padding: 10px 8px; color: #a78bfa;">占总股本%</th>
<th style="text-align: right; padding: 10px 8px; color: #a78bfa;">占流通股本%</th>
<th style="text-align: left; padding: 10px 8px; color: #a78bfa;">影响评估</th>
</tr>
</thead>
<tbody>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.05);">
<td style="padding: 10px 8px;">688197</td>
<td style="padding: 10px 8px;"><b>首药控股-U</b></td>
<td style="text-align: right; padding: 10px 8px; color: #f87171;">8471.45</td>
<td style="text-align: right; padding: 10px 8px; color: #f87171;">56.96%</td>
<td style="text-align: right; padding: 10px 8px; color: #f87171;">132.36%</td>
<td style="padding: 10px 8px;"><span style="color: #ef4444; font-weight: 600;">高风险</span> 首发原股东限售，解禁比例超50%，实控人股份解禁，抛压大</td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.05);">
<td style="padding: 10px 8px;">603418</td>
<td style="padding: 10px 8px;"><b>友升股份</b></td>
<td style="text-align: right; padding: 10px 8px; color: #fbbf24;">4668.40</td>
<td style="text-align: right; padding: 10px 8px; color: #fbbf24;">24.18%</td>
<td style="text-align: right; padding: 10px 8px; color: #fbbf24;">112.86%</td>
<td style="padding: 10px 8px;"><span style="color: #f59e0b; font-weight: 600;">中风险</span> 解禁后流通盘翻倍，需警惕短期抛压</td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.05);">
<td style="padding: 10px 8px;">002239</td>
<td style="padding: 10px 8px;">奥特佳</td>
<td style="text-align: right; padding: 10px 8px;">2000.27</td>
<td style="text-align: right; padding: 10px 8px;">0.57%</td>
<td style="text-align: right; padding: 10px 8px;">0.75%</td>
<td style="padding: 10px 8px;"><span style="color: #10b981;">低风险</span> 占比小，影响有限</td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.05);">
<td style="padding: 10px 8px;">000886</td>
<td style="padding: 10px 8px;">海南高速</td>
<td style="text-align: right; padding: 10px 8px;">180.00</td>
<td style="text-align: right; padding: 10px 8px;">0.18%</td>
<td style="text-align: right; padding: 10px 8px;">0.18%</td>
<td style="padding: 10px 8px;"><span style="color: #10b981;">低风险</span> 占比极小</td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.05);">
<td style="padding: 10px 8px;">601126</td>
<td style="padding: 10px 8px;">四方股份</td>
<td style="text-align: right; padding: 10px 8px;">64.25</td>
<td style="text-align: right; padding: 10px 8px;">0.08%</td>
<td style="text-align: right; padding: 10px 8px;">0.08%</td>
<td style="padding: 10px 8px;"><span style="color: #10b981;">低风险</span> 股权激励解禁，数量极少</td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.05);">
<td style="padding: 10px 8px;">300124</td>
<td style="padding: 10px 8px;">汇川技术</td>
<td style="text-align: right; padding: 10px 8px;">31.00</td>
<td style="text-align: right; padding: 10px 8px;">0.01%</td>
<td style="text-align: right; padding: 10px 8px;">0.01%</td>
<td style="padding: 10px 8px;"><span style="color: #10b981;">低风险</span> 可忽略不计</td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.05);">
<td style="padding: 10px 8px;">600426</td>
<td style="padding: 10px 8px;">华鲁恒升</td>
<td style="text-align: right; padding: 10px 8px;">36.40</td>
<td style="text-align: right; padding: 10px 8px;">0.01%</td>
<td style="text-align: right; padding: 10px 8px;">0.01%</td>
<td style="padding: 10px 8px;"><span style="color: #10b981;">低风险</span> 可忽略不计</td>
</tr>
<tr>
<td style="padding: 10px 8px;">603726</td>
<td style="padding: 10px 8px;">朗迪集团</td>
<td style="text-align: right; padding: 10px 8px;">88.50</td>
<td style="text-align: right; padding: 10px 8px;">0.48%</td>
<td style="text-align: right; padding: 10px 8px;">0.48%</td>
<td style="padding: 10px 8px;"><span style="color: #10b981;">低风险</span> 影响有限</td>
</tr>
</tbody>
</table>
</div>
<div style="margin-top: 12px; padding: 10px 14px; background: rgba(248, 113, 113, 0.08); border-radius: 8px; border: 1px solid rgba(248, 113, 113, 0.2); font-size: 12px; color: #fca5a5; line-height: 1.6;">
<b>整体评估：</b>周三11股解禁合计约1.6亿股，整体压力可控。但<b>首药控股-U</b>解禁比例高达56.96%（实控人股份），<b>友升股份</b>解禁后流通盘翻倍，两只个股需重点警惕短期抛压。其余9只个股解禁占比均低于1%，对股价影响甚微。
</div>
"""
section = Section(title="🔓 限售股解禁详情", content=restriction_content, icon="unlock")
gen._components.append(section)

# ============ 4. 新股申购 ============
ipo_content = """
<div style="display: flex; flex-direction: column; gap: 14px;">
<div style="background: rgba(30, 41, 59, 0.6); border: 1px solid rgba(99, 102, 241, 0.2); border-radius: 12px; padding: 16px;">
<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
<span style="font-size: 16px; font-weight: 700; color: #f1f5f9;">莫森泰克 (920162)</span>
<span style="padding: 3px 10px; background: linear-gradient(135deg, #3b82f6, #8b5cf6); color: white; border-radius: 6px; font-size: 12px; font-weight: 600;">9月23日申购</span>
</div>
<div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; font-size: 13px;">
<div><span style="color: #94a3b8;">发行价</span><br><span style="color: #f1f5f9; font-weight: 600;">17.37元</span></div>
<div><span style="color: #94a3b8;">发行市盈率</span><br><span style="color: #f1f5f9; font-weight: 600;">10.00倍</span></div>
<div><span style="color: #94a3b8;">行业市盈率</span><br><span style="color: #f1f5f9; font-weight: 600;">22.47倍</span></div>
<div><span style="color: #94a3b8;">申购上限</span><br><span style="color: #f1f5f9; font-weight: 600;">76.5万股</span></div>
<div><span style="color: #94a3b8;">发行规模</span><br><span style="color: #f1f5f9; font-weight: 600;">1700万股</span></div>
<div><span style="color: #94a3b8;">预计募资</span><br><span style="color: #f1f5f9; font-weight: 600;">2.95亿元</span></div>
</div>
<div style="margin-top: 12px; font-size: 12px; color: #94a3b8; line-height: 1.6;">
<b>主营业务：</b>汽车天窗、玻璃升降器等汽车开闭器件及电子控制单元研发制造，粉末冶金零部件。国家级专精特新"小巨人"。<br>
<b>业绩情况：</b>2025年营收19.24亿元，净利润2.25亿元（-14.97%）；2024年净利润2.64亿元（+36.84%）。<br>
<b>申购建议：</b><span style="color: #10b981; font-weight: 600;">★★★☆☆ 建议申购</span> 发行市盈率仅为行业均值的44%，安全边际较高；汽车零部件赛道稳定，但近年净利润增速放缓。
</div>
</div>

<div style="background: rgba(30, 41, 59, 0.6); border: 1px solid rgba(99, 102, 241, 0.2); border-radius: 12px; padding: 16px;">
<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
<span style="font-size: 16px; font-weight: 700; color: #f1f5f9;">粤芯半导体 (301660)</span>
<span style="padding: 3px 10px; background: linear-gradient(135deg, #f59e0b, #ef4444); color: white; border-radius: 6px; font-size: 12px; font-weight: 600;">9月24日申购</span>
</div>
<div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; font-size: 13px;">
<div><span style="color: #94a3b8;">申购代码</span><br><span style="color: #f1f5f9; font-weight: 600;">301660</span></div>
<div><span style="color: #94a3b8;">申购上限</span><br><span style="color: #f1f5f9; font-weight: 600;">12.8万股</span></div>
<div><span style="color: #94a3b8;">发行规模</span><br><span style="color: #f1f5f9; font-weight: 600;">5.13亿股</span></div>
<div><span style="color: #94a3b8;">预计募资</span><br><span style="color: #f1f5f9; font-weight: 600;">约77亿元</span></div>
<div><span style="color: #94a3b8;">行业</span><br><span style="color: #f1f5f9; font-weight: 600;">半导体</span></div>
<div><span style="color: #94a3b8;">创业板排名</span><br><span style="color: #f1f5f9; font-weight: 600;">今年第1大</span></div>
</div>
<div style="margin-top: 12px; font-size: 12px; color: #94a3b8; line-height: 1.6;">
<b>公司亮点：</b>广东首家12英寸晶圆制造企业，全球少数专注模拟芯片的特色工艺代工厂。中国大陆唯一具备12英寸硅光晶圆大规模量产能力的企业。2023-2025年营收CAGR达57.3%。<br>
<b>关注要点：</b>公司尚未盈利，2023-2025年累计亏损超65亿，预计最早2029年扭亏。发行规模巨大（今年创业板最大），中签率预计较高。<br>
<b>申购建议：</b><span style="color: #f59e0b; font-weight: 600;">★★★★☆ 重点关注</span> 半导体国产替代核心标的，赛道稀缺性强，但需注意未盈利风险，建议结合风险承受能力申购。
</div>
</div>

<div style="background: rgba(30, 41, 59, 0.6); border: 1px solid rgba(16, 185, 129, 0.2); border-radius: 12px; padding: 16px;">
<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
<span style="font-size: 16px; font-weight: 700; color: #f1f5f9;">凯达重工 (920025) 上市</span>
<span style="padding: 3px 10px; background: linear-gradient(135deg, #10b981, #059669); color: white; border-radius: 6px; font-size: 12px; font-weight: 600;">9月23日上市</span>
</div>
<div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; font-size: 13px;">
<div><span style="color: #94a3b8;">发行价</span><br><span style="color: #f1f5f9; font-weight: 600;">4.26元</span></div>
<div><span style="color: #94a3b8;">网上中签率</span><br><span style="color: #f1f5f9; font-weight: 600;">0.0182%</span></div>
<div><span style="color: #94a3b8;">上市地点</span><br><span style="color: #f1f5f9; font-weight: 600;">北交所</span></div>
</div>
</div>
</div>
"""
section = Section(title="📈 新股申购与上市", content=ipo_content, icon="trending-up")
gen._components.append(section)

# ============ 5. 经济数据 ============
gen.add_data_release([
    {
        'name': '美国9月PMI初值',
        'prev': '51.2 (8月)',
        'expect': '50.8',
        'actual': '待公布'
    },
    {
        'name': '美国EIA原油库存',
        'prev': '-320万桶',
        'expect': '待预测',
        'actual': '待公布'
    },
    {
        'name': '流通领域生产资料价格',
        'prev': '9月中旬',
        'expect': '9月下旬',
        'actual': '9月24日公布'
    },
    {
        'name': '成品油调价窗口',
        'prev': '上轮上调',
        'expect': '9月24日24时',
        'actual': '9月24日开启'
    },
])

# ============ 6. 海外大事提醒 ============
overseas_content = """
<div style="display: flex; flex-direction: column; gap: 12px;">

<div style="background: linear-gradient(135deg, rgba(239, 68, 68, 0.1), rgba(249, 115, 22, 0.1)); border: 1px solid rgba(239, 68, 68, 0.2); border-radius: 12px; padding: 14px;">
<div style="font-size: 15px; font-weight: 700; color: #f87171; margin-bottom: 6px;">🇺🇸 美联储加息余波持续</div>
<div style="font-size: 13px; color: #cbd5e1; line-height: 1.7;">
美联储9月16日宣布加息25bp，联邦基金利率升至3.75%-4.00%，为时隔三年多重启加息。最新点阵图显示16位官员预计年底利率将高于当前水平，市场预计四季度至少再加息一次概率接近90%。10年期美债收益率已从4.969%高位回落至5%以下，但高利率环境持续压制风险资产估值。
</div>
</div>

<div style="background: linear-gradient(135deg, rgba(59, 130, 246, 0.1), rgba(139, 92, 246, 0.1)); border: 1px solid rgba(59, 130, 246, 0.2); border-radius: 12px; padding: 14px;">
<div style="font-size: 15px; font-weight: 700; color: #60a5fa; margin-bottom: 6px;">🌍 中美关系重大节点</div>
<div style="font-size: 13px; color: #cbd5e1; line-height: 1.7;">
习近平主席9月23日至25日访美，两国元首半年内实现国事互访，具有历史性里程碑意义。中美双方在经贸、AI治理、半导体合作、禁毒、气候变化等领域有望达成新共识。中美贸易指数9月以来已累计上涨超3.4%，市场已提前反映部分乐观预期。
</div>
</div>

<div style="background: linear-gradient(135deg, rgba(16, 185, 129, 0.1), rgba(6, 182, 212, 0.1)); border: 1px solid rgba(16, 185, 129, 0.2); border-radius: 12px; padding: 14px;">
<div style="font-size: 15px; font-weight: 700; color: #34d399; margin-bottom: 6px;">🤖 全球AI产业动态</div>
<div style="font-size: 13px; color: #cbd5e1; line-height: 1.7;">
1. Meta推出的AI智能体Muse超越ChatGPT和Claude登苹果应用商店榜首，AI Agent商业化加速；<br>
2. 阿里云栖大会发布AgentCore智能体构建平台、真武V900芯片等全栈AI产品；<br>
3. 工信部印发《"人工智能+软件"专项行动实施方案》，目标到2028年打造100个智能体软件标杆应用。
</div>
</div>

</div>
"""
section = Section(title="🌍 海外大事提醒", content=overseas_content, icon="globe")
gen._components.append(section)

# ============ 7. 重点事件影响深度分析 ============
deep_analysis_content = """
<div style="line-height: 1.85; color: #e2e8f0; font-size: 14px;">

<h3 style="color: #fbbf24; font-size: 16px; margin: 0 0 10px 0;">🔥 核心事件一：习近平主席访美 — 中美关系新定位的战略落地</h3>

<p style="margin: 0 0 12px 0;"><b>事件背景：</b>应美国总统特朗普邀请，国家主席习近平将于9月23日至25日对美国进行国事访问。这是今年5月北京会晤后两国元首再度面对面会晤，也是"中美建设性战略稳定关系"新定位确立后的首次国事访问，具有历史性里程碑意义。</p>

<p style="margin: 0 0 12px 0;"><b>影响分析：</b>此次访问的核心意义在于将"四个稳定"（合作为主的积极稳定、竞争有度的良性稳定、分歧可控的常态稳定、和平可期的持久稳定）从战略共识转化为具体行动。从已释放的信号看，以下领域有望取得实质进展：</p>

<p style="margin: 0 0 12px 0;"><b>① 经贸合作层面：</b>中美贸易理事会数据显示95%受访美企认为在华业务有助全球竞争力，92%实现盈利。贸易理事会架构、职能、运行模式等机制化安排有望落地，经贸关系从危机应对转向制度管理。利好出海概念（纺织服饰、轻工制造、医疗耗材、通用设备）。重点标的：华利集团（境外收入占比近80%）、巨星科技、恒林股份、五洲医疗（年内涨幅超175%）、梦百合（机构预测2026年净利润增幅近1030%）。</p>

<p style="margin: 0 0 12px 0;"><b>② 科技与AI层面：</b>双方在AI治理、开源模型合作、半导体供应链等领域有望达成阶段性共识。此前美方在人工智能、生物医药等新兴领域交流热度已上升。关注半导体设备、AI算力相关标的，但需注意预期兑现风险。</p>

<p style="margin: 0 0 16px 0;"><b>操作建议：</b>此次访问级别高、意义重大，但市场已提前有所预期（中美贸易指数9月累计涨3.4%）。建议<b>利好兑现前不追高</b>，重点跟踪访问期间是否有超预期合作成果。若会谈释放超预期积极信号，出海产业链、半导体合作、农业采购等方向有望迎来脉冲行情；若成果低于预期，相关板块可能出现短期回调。整体定性为<b>中性偏多</b>，以事件驱动型机会看待。</p>

<h3 style="color: #fbbf24; font-size: 16px; margin: 20px 0 10px 0;">💎 核心事件二：中金公司复牌 — 券商行业整合加速信号</h3>

<p style="margin: 0 0 12px 0;"><b>事件背景：</b>中金公司A股股票9月23日开市起复牌。换股吸收合并东兴证券、信达证券获证监会核准，新增发行A股约31.04亿股，整体交易规模1139亿元。合并后总资产将超万亿，净利润超百亿，营收升至行业第三。</p>

<p style="margin: 0 0 12px 0;"><b>影响分析：</b>中金"三合一"重组是汇金系券商整合的关键一步，也是打造"国际一流投行"战略的重要落地。此次重组具有多重意义：</p>

<p style="margin: 0 0 12px 0;"><b>① 行业格局重塑：</b>合并后中金公司总资产突破万亿，营收跻身行业前三，形成与中信证券、国泰海通正面竞争的第一梯队格局。券商行业集中度提升趋势明确，头部券商竞争优势进一步强化。</p>

<p style="margin: 0 0 12px 0;"><b>② 整合效应待释放：</b>东方资产、信达资产将成为中金主要股东（分别持股8.03%、16.76%）。承接东兴基金100%及信达澳亚基金54%股权，东兴期货及信达期货纳入麾下。证监会要求一年内制定具体整合方案。短期需关注整合带来的协同效应与摩擦成本。</p>

<p style="margin: 0 0 12px 0;"><b>③ 估值影响：</b>停牌前中金股价31.80元，市值1535亿元，低于换股价格36.68元。有效申报的异议股份仅732.19万股，占比极低，说明股东普遍看好合并前景。复牌后股价表现将成为市场关注焦点。</p>

<p style="margin: 0 0 16px 0;"><b>操作建议：</b>中金复牌对券商板块构成情绪面催化，但需理性看待：① 换股价格36.68元对现价有一定安全垫，但停牌期间行业已有所变化；② 整合效应需要时间兑现，短期更多是事件驱动；③ 建议关注低估值头部券商的配置价值，但不建议盲目追涨复牌首日的中金公司。整体定性为<b>利好券商板块情绪</b>，持续性取决于后续整合进展。</p>

<h3 style="color: #fbbf24; font-size: 16px; margin: 20px 0 10px 0;">🤖 核心事件三：Agentic AI浪潮 — 云栖大会释放产业加速信号</h3>

<p style="margin: 0 0 12px 0;"><b>事件背景：</b>9月22日开幕的2026云栖大会以"智以致用"为主题，Agentic AI为核心锚点。阿里云发布了全栈Agentic Cloud战略，包括灵骏真武M890超节点、AgentCore智能体构建平台、Wan 3.0视频大模型、QwenNote AI硬件等重磅产品。工信部同期印发《"人工智能+软件"专项行动实施方案》。</p>

<p style="margin: 0 0 12px 0;"><b>影响分析：</b>AI产业正从"模型能力竞争"全面转向"智能体应用落地"的新阶段：</p>

<p style="margin: 0 0 12px 0;"><b>① 产业趋势明确：</b>中国信通院测算，到2030年国内AI Agent市场规模有望突破5万亿元，企业级Agent是增长最快的细分市场。工信部提出到2028年推广覆盖2万家规模以上软件企业，打造100个智能体软件标杆应用。政策+产业双轮驱动。</p>

<p style="margin: 0 0 12px 0;"><b>② 应用端先行爆发：</b>Meta的Muse智能体登顶苹果应用商店，国内金山办公（300余个教育智能体）、税友股份（犀友AI平台）、汉朔科技（门店智能执行平台）等公司已实现产品落地。9月22日A股AI应用方向（AI办公、虚拟人、智能体概念）涨幅均超2%，验证了市场对这一方向的认可。</p>

<p style="margin: 0 0 12px 0;"><b>③ 算力底座持续受益：</b>阿里云宣布到2032年全球数据中心运营规模将超20GW，平头哥真武V900芯片算力为上一代3倍。国产算力产业链（服务器、光模块、PCB、存储）需求确定性持续增强。</p>

<p style="margin: 0 0 16px 0;"><b>操作建议：</b>AI Agent是当前科技板块最确定的产业趋势之一，云栖大会进一步强化了这一共识。但板块已积累一定涨幅（计算机、传媒板块9月22日出现涨停潮），建议<b>避免追高，逢回调布局</b>。重点关注三条线：① 应用层（AI办公、智能体落地先驱）；② 算力层（服务器、光模块、PCB，有业绩支撑）；③ 国产算力链（存储、半导体，拥挤度仍处历史底部）。整体定性为<b>中长期产业趋势确认</b>，短期注意节奏。</p>

<h3 style="color: #fbbf24; font-size: 16px; margin: 20px 0 10px 0;">📚 核心事件四：教育强国发布会 — 政策+AI双催化教育板块</h3>

<p style="margin: 0 0 12px 0;"><b>事件背景：</b>9月23日上午10时，教育部副部长杜江峰将出席国新办发布会，介绍贯彻落实"十五五"规划，加快推进教育强国建设有关情况。近期中办国办印发《关于分类推进高校改革的意见》，教育领域政策密集出台。</p>

<p style="margin: 0 0 12px 0;"><b>影响分析：</b>教育行业正迎来政策环境、基本面与AI逻辑的三重积极变化：</p>

<p style="margin: 0 0 12px 0;"><b>① 政策常态化：</b>经历前期供给出清后，教育行业监管趋于常态化、数字化，政策环境边际改善。"十五五"规划将教育强国建设放在突出位置，职业教育、AI教育、科技教育获重点支持。</p>

<p style="margin: 0 0 12px 0;"><b>② AI+教育增量：</b>金山办公联合浙江省教育技术中心打造的"AI会学"平台入选全球最佳实践案例，300余个教育智能体帮助教师缩减40%以上备课时长。AI教育是AI Agent落地最成熟的场景之一。</p>

<p style="margin: 0 0 16px 0;"><b>关注标的：</b>读客文化（民营图书策划发行）、中文在线（在线教育+教育信息化）、金山办公（AI教育标杆应用）、科大讯飞（智慧教育龙头）。整体定性为<b>政策催化+产业趋势共振</b>，建议关注发布会是否释放超预期政策信号。</p>

</div>
"""
section = Section(title="🎯 重点事件影响深度分析与操作建议", content=deep_analysis_content, icon="target", variant="highlight")
gen._components.append(section)

# ============ 8. 催化深度分析（Skill增强） ============
gen.add_catalyst_deep_analysis([
    {'type': 'meeting', 'title': '习近平主席访美', 'description': '两国元首会晤，中美建设性战略稳定关系战略引领，经贸合作、AI治理等议题', 'category': '元首外交'},
    {'type': 'general', 'title': '中金公司复牌', 'description': '千亿级券商三合一重组落地，总资产超万亿，营收行业第三', 'category': '证券市场'},
    {'type': 'policy', 'title': '教育强国建设发布会', 'description': '十五五规划教育政策解读，AI+教育、职业教育催化', 'category': '政策发布'},
])

# ============ 9. 风险提示 ============
gen.add_risk_warning([
    "习近平主席访美成果存在不确定性，若低于预期可能引发相关板块回调",
    "首药控股-U、友升股份解禁比例较高，需警惕短期抛压对个股影响",
    "美联储加息周期持续，高利率环境压制全球风险资产估值，美债收益率波动可能传导至A股",
    "AI板块近期涨幅较大，存在短期获利回吐风险，注意追高风险",
    "中金公司复牌后股价波动可能放大，不建议盲目追涨",
    "以上分析基于公开信息整理，不构成投资建议，股市有风险，入市需谨慎"
])

# ============ 发布 ============
result = gen.publish()
print("发布结果：", result)
