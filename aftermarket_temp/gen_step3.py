
# 10. 明日预判
gen.add_tomorrow_prediction([
    {
        "name": "大盘指数（7/9周四）", "direction": "震荡偏空", "confidence": 60,
        "reason": "沪指连续两日失守4000点，量能萎缩至2.56万亿，观望情绪浓厚。3970附近是60日线+前期平台支撑，若能守住可能横盘震荡；若放量跌破则下探3930-3950区间。关注量能能否回到2.7万亿以上。"
    },
    {
        "name": "算力/网络安全/云计算", "direction": "看涨（分化）", "confidence": 65,
        "reason": "今日最强主线，计算机板块单日净流入76亿，资金态度坚决。但浪潮信息龙虎榜显示机构和北向大举卖出，游资接力，短期高位股可能分化。关注低位补涨标的（信创/数据安全/AI应用），不追高龙头。"
    },
    {
        "name": "半导体设备", "direction": "震荡偏强", "confidence": 58,
        "reason": "科创50唯一收红，设备端获资金抄底（中科飞测/灿芯股份/华虹宏力大涨），国产替代逻辑强化。但存储/封测/材料端仍弱，板块内部分化。精测电子停牌收购上海精测半导体，明日半导体设备情绪可能受催化。"
    },
    {
        "name": "锂电/能源金属", "direction": "看跌（超跌反弹）", "confidence": 55,
        "reason": "今日跌停潮，天齐锂业/恩捷股份/天赐材料等多股跌停，板块情绪崩塌。但龙虎榜显示恩捷股份机构净买入（分歧），说明有资金在跌停板抄底。短期可能有技术性反弹，但中期趋势已走坏，反弹是减仓机会。"
    },
    {
        "name": "人形机器人", "direction": "看跌", "confidence": 62,
        "reason": "绿的谐波-15%、埃斯顿跌停，前期热门赛道资金获利了结明显。板块高位筹码松动，短期进入调整期。关注核心标的回调至30日线附近的支撑情况，调整充分后或有二波机会。"
    },
])

# 11. 操作计划
plan_html = """
<div style="background: linear-gradient(135deg, #fee2e2 0%, #fecaca 100%); border-radius: 16px; padding: 20px; margin-bottom: 16px; border-left: 4px solid #ef4444;">
    <div style="font-size: 15px; font-weight: 700; color: #991b1b; margin-bottom: 10px;">🔴 持仓风控优先级</div>
    <ul style="margin: 0; padding-left: 20px; font-size: 14px; color: #7f1d1d; line-height: 2;">
        <li><strong>铜冠铜箔(301217)</strong>：今日放量大跌7.47%，短期趋势走坏。<strong>反弹至145-150区间减仓1/3锁利</strong>，若明日继续跌破130则进一步减仓至底仓。存储中期逻辑未破但短期调整未结束，不抄底</li>
        <li><strong>雅克科技(002409)</strong>：今日深V反弹+2.25%，但电子板块整体资金流出188亿。<strong>反弹至195-200区间减仓1/3</strong>，破180警惕二次探底。半导体设备强但材料弱，板块内部分化需谨慎</li>
        <li><strong>英维克(002837)</strong>：震荡区间70-75，今日最高74.79触及减仓区。<strong>反弹74-75继续减仓</strong>，破70无条件离场。液冷板块跟随算力但弹性不如软件/安全，降仓换方向</li>
        <li><strong>*ST建艺(002789)</strong>：ST股严格控制仓位，不新增，逢高逐步清仓。10%涨跌幅下波动剧烈，退市风险不可忽视</li>
    </ul>
</div>

<div style="background: linear-gradient(135deg, #dbeafe 0%, #bfdbfe 100%); border-radius: 16px; padding: 20px; margin-bottom: 16px; border-left: 4px solid #3b82f6;">
    <div style="font-size: 15px; font-weight: 700; color: #1e40af; margin-bottom: 10px;">🎯 明日关注方向（控仓前提下）</div>
    <ul style="margin: 0; padding-left: 20px; font-size: 14px; color: #1e3a8a; line-height: 2;">
        <li><strong>算力应用端（AI安全/云计算/信创）</strong>：今日最强主线，资金大规模流入计算机板块。关注低位补涨标的，不追高位20cm涨停股，可关注有业绩支撑的细分龙头</li>
        <li><strong>半导体设备国产替代</strong>：科创50逆势收红，设备端获资金抄底，精测电子停牌重组可能带动板块情绪，关注低位设备股</li>
        <li><strong>油气/黄金（防御）</strong>：避险资金扎堆，油价上涨催化，适合防守仓位配置</li>
        <li><strong>总仓位控制</strong>：4-5成，沪指4000点下方谨慎为主，等企稳信号再加仓</li>
    </ul>
</div>

<div style="background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%); border-radius: 16px; padding: 20px; margin-bottom: 16px; border-left: 4px solid #f59e0b;">
    <div style="font-size: 15px; font-weight: 700; color: #92400e; margin-bottom: 10px;">⚡ 短线机会观察</div>
    <ul style="margin: 0; padding-left: 20px; font-size: 14px; color: #78350f; line-height: 2;">
        <li><strong>精测电子产业链</strong>：停牌收购上海精测半导体，明日半导体检测设备板块可能联动（中科飞测、华峰测控、长川科技）</li>
        <li><strong>中报超预期</strong>：每日晚间筛选业绩大增标的，华昌化工(+1026%)、特发信息(+881%-1167%)、高德红外(+602%-701%)等明日关注</li>
        <li><strong>连板梯队</strong>：恒尚节能7连板、ST海王6连板、大恒科技3连板，高位连板股亏钱效应明显（77只跌停），不建议追</li>
    </ul>
</div>

<div style="background: linear-gradient(135deg, #f3e8ff 0%, #e9d5ff 100%); border-radius: 16px; padding: 20px; border-left: 4px solid #a855f7;">
    <div style="font-size: 15px; font-weight: 700; color: #6b21a8; margin-bottom: 10px;">⚠️ 关键风险点</div>
    <ul style="margin: 0; padding-left: 20px; font-size: 14px; color: #581c87; line-height: 2;">
        <li>沪指连续失守4000点，若放量跌破3970支撑需防范加速探底</li>
        <li>半年报季开启，高位无业绩支撑的题材股注意业绩雷</li>
        <li>半导体产业链解禁压力大（屹唐股份559亿/沪硅产业大基金减持）</li>
        <li>锂电板块跌停潮后可能拖累新能源整体情绪</li>
    </ul>
</div>
"""
gen.add_trading_plan(plan_html)

# 12. 风险提示
gen.add_risk_warning([
    "沪指连续两天失守4000点，市场情绪偏弱，若跌破3970支撑需警惕加速调整风险",
    "半年报业绩窗口开启，高位纯题材股面临业绩验证压力，注意业绩雷风险",
    "半导体产业链大额解禁+产业资本减持（屹唐股份559亿/大基金减持），供给端压力不容忽视",
    "锂电板块跌停潮可能引发新能源整体情绪恶化，持仓需注意板块联动风险",
    "以上分析仅供参考，不构成投资建议，股市有风险，投资需谨慎"
])

# 生成并保存
output_path = "/root/daily-news-insight/docs/aftermarket/20260708_盘后速递.html"
html = gen.generate()
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(html)
print(f"✅ 报告已生成: {output_path}")
print(f"📄 文件大小: {os.path.getsize(output_path)} bytes")
