"""
报告生成引擎 - 内容驱动的智能报告生成器
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from components.core import (
    data_card_grid, 
    comparison_table, 
    quote_block, 
    risk_opportunity, 
    industry_chain_diagram,
    conclusion_block
)
from components.charts import (
    market_share_horizontal,
    value_chain
)
from components.layouts import report_page


def generate_yake_report():
    """
    生成雅克科技HBM产业链深度研究报告
    内容驱动，自动选择最佳UI组件
    """
    
    # ========== 第1部分：核心指标卡片 ==========
    metrics_cards = data_card_grid(
        title="核心指标总览",
        cards=[
            {"icon": "fa-trophy", "title": "全球排名", "value": "第3", "trend": "+国内第1", "color": "yellow"},
            {"icon": "fa-shield", "title": "技术壁垒", "value": "7N级", "trend": "全球仅3家", "color": "blue"},
            {"icon": "fa-handshake-o", "title": "独家供应", "value": "SK海力士", "trend": "至2031年", "color": "green"},
            {"icon": "fa-line-chart", "title": "2026年营收", "value": "~90亿", "trend": "+4~16%", "color": "purple"},
            {"icon": "fa-percent", "title": "HBM业务占比", "value": "~15%", "trend": "快速提升", "color": "indigo"},
            {"icon": "fa-users", "title": "覆盖客户", "value": "6+", "trend": "全球存储巨头", "color": "pink"},
        ],
        cols=3
    )
    
    # ========== 第2部分：核心结论引用 ==========
    core_quote = quote_block(
        content="雅克科技是目前A股唯一同时进入SK海力士、三星、美光三大全球存储巨头HBM供应链的半导体材料企业，其7N级超高纯前驱体技术壁垒全球领先。如果全球瞬间失去雅克科技的产能，HBM与先进DRAM将出现2-3年的供给真空期。",
        source="多家机构联合研究报告 · 2026年6月"
    )
    
    # ========== 第3部分：全球竞争格局 ==========
    competition_chart = market_share_horizontal(
        title="全球HBM前驱体市场份额（2026年预测）",
        companies=[
            {"name": "默克 (Merck)", "share": 42},
            {"name": "信越化学 (Shin-Etsu)", "share": 35},
            {"name": "雅克科技 (via UP Chemical)", "share": 18, "highlight": True},
            {"name": "其他厂商", "share": 5},
        ]
    )
    
    # ========== 第4部分：产业链价值分布 ==========
    value_chain_chart = value_chain(
        title="HBM产业链价值分布",
        layers=[
            {"name": "HBM芯片制造", "value": 60, "color": "purple"},
            {"name": "先进封装", "value": 15, "color": "indigo"},
            {"name": "关键材料（前驱体等）", "value": 10, "color": "blue"},
            {"name": "封装基板", "value": 8, "color": "cyan"},
            {"name": "GMC塑封材料", "value": 4, "color": "teal"},
            {"name": "其他配套", "value": 3, "color": "gray"},
        ]
    )
    
    # 竞争格局+价值分布双列布局
    competition_section = f'''
    <section class="mb-12">
        <h2 class="text-2xl font-bold text-gray-800 mb-6 flex items-center">
            <span class="w-1 h-8 bg-gradient-to-b from-indigo-500 to-purple-500 rounded-full mr-3"></span>
            全球竞争格局与产业链价值
        </h2>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            {competition_chart}
            {value_chain_chart}
        </div>
    </section>
    '''
    
    # ========== 第5部分：存储产业链核心标的对比 ==========
    comparison = comparison_table(
        title="存储产业链核心标的深度对比",
        headers=["标的", "代码", "核心产品", "2026E营收", "毛利率", "HBM相关占比", "核心竞争力"],
        rows=[
            ["雅克科技", "002409", "HBM前驱体", "~90亿", "31%", "~15%", "🇨🇳 SK海力士独家，7N级纯度，全球三强"],
            ["华海诚科", "688535", "HBM专用GMC", "~11亿", "27%", "~20%", "🇨🇳 国内唯一GMC量产，SK海力士认证中"],
            ["铜冠铜箔", "301217", "HVLP铜箔", "~48亿", "14%", "~25%", "🇨🇳 存储芯片封装铜箔，国内市占率第一"],
            ["菲利华", "300395", "石英材料", "~20亿", "50%", "~30%", "🇨🇳 英伟达独家绑定，全球半导体石英龙头"],
            ["安集科技", "688019", "CMP抛光液", "~16亿", "52%", "~10%", "🇨🇳 国内CMP抛光液龙头"],
            ["南大光电", "300346", "前驱体/光刻胶", "~15亿", "35%", "~5%", "🇨🇳 ArF光刻胶突破，前驱体追赶中"],
        ],
        highlight_col="雅克科技"
    )
    
    # ========== 第6部分：客户结构图谱 ==========
    chain_diagram = industry_chain_diagram(
        title="雅克科技全球客户覆盖图谱",
        layers=[
            {"name": "韩国客户", "companies": ["SK海力士（HBM独家）", "三星电子（验证通过）"], "color": "blue"},
            {"name": "美国客户", "companies": ["美光（批量供货）", "英特尔（验证中）"], "color": "indigo"},
            {"name": "国内存储", "companies": ["长江存储", "长鑫存储"], "color": "red"},
            {"name": "逻辑代工", "companies": ["台积电（3nm验证）", "中芯国际"], "color": "purple"},
        ]
    )
    
    # ========== 第7部分：风险与机会 ==========
    risk_opp = risk_opportunity(
        title="风险提示与投资机会",
        risks=[
            "客户集中度风险：SK海力士占HBM业务比例较高，单一客户依赖",
            "技术迭代风险：HBM技术路线快速演进，下一代材料需持续研发投入",
            "地缘政治风险：中美科技博弈可能影响全球供应链稳定性",
            "产能爬坡风险：7N级超高纯量产线良率提升需要时间",
            "行业周期风险：存储行业周期性波动可能影响订单需求",
        ],
        opportunities=[
            "AI算力爆发带动HBM需求指数级增长，前驱体作为耗材持续受益",
            "国产替代加速：国内存储厂商扩产，材料自给率提升空间巨大",
            "三星、美光订单放量：2026年下半年开始批量供货，业绩弹性大",
            "平台化协同：光刻胶、电子特气多品类增长，客户粘性持续增强",
            "HBM4/HBM5技术迭代：公司深度参与下一代材料研发，先发优势显著",
        ]
    )
    
    # ========== 第8部分：核心结论 ==========
    conclusion = conclusion_block(
        title="投资结论与核心观点",
        points=[
            "雅克科技 = HBM浪潮中的「卖铲人」：不直接生产HBM芯片，但向全球巨头提供制造HBM必需的关键材料，受益确定性高于芯片厂商。",
            "技术壁垒全球领先：7N级超高纯前驱体全球仅3家能量产，国内尚无竞争对手，技术代差至少3-5年。",
            "业绩增长路径清晰：2026年SK海力士独家订单放量，2027年三星、美光订单接棒，未来3年复合增速有望保持30%+。",
            "平台化价值重估：公司已从前驱体单一材料商转型为一站式半导体材料平台，光刻胶、电子特气、CMP材料多轮驱动增长。",
            "国产替代空间巨大：HBM用前驱体国内自给率不足5%，长江存储、长鑫存储扩产为公司提供第二增长曲线。",
        ]
    )
    
    # ========== 组装完整报告 ==========
    report_html = report_page(
        title="雅克科技HBM产业链深度研究报告",
        subtitle="全球HBM前驱体核心供应商 · AI算力浪潮的确定性受益者",
        metrics=[
            {"value": "7N级", "label": "超高纯度"},
            {"value": "18%", "label": "全球市占率"},
            {"value": "65%", "label": "HBM4毛利率"},
            {"value": "1052吨", "label": "远期总产能"},
        ],
        content_sections=[
            metrics_cards,
            core_quote,
            competition_section,
            comparison,
            chain_diagram,
            risk_opp,
            conclusion,
        ]
    )
    
    return report_html


if __name__ == "__main__":
    report = generate_yake_report()
    with open("../docs/industry_chain/20260605_雅克科技_HBM产业链深度研究报告_v2.html", "w", encoding="utf-8") as f:
        f.write(report)
    print("✅ 新版雅克科技HBM产业链深度研究报告生成完成！")
