import sys
sys.path.insert(0, '/root/daily-news-insight')

from v3.generators.s_level_catalyst import SLevelCatalystGenerator

DATE = "20260606"
gen = SLevelCatalystGenerator(title="S级催化：AI算力全面爆发")
gen.add_catalyst_overview(
    overview="英伟达正式发布H200 GPU，HBM容量提升至141GB，带宽提升2.3倍，将全面推动AI算力升级，带动整个产业链需求爆发。",
    event_date="2026年6月2日",
    impact_level="S级"
)
gen.add_impact_analysis(
    impact="H200芯片的发布标志着AI算力进入新阶段。HBM容量和带宽的大幅提升将支持更大规模的AI模型训练和推理，推动AI应用加速落地。",
    dimensions=[
        {"name": "市场空间", "level": 5, "desc": "全球AI芯片市场2026年预计达2500亿美元"},
        {"name": "产业成熟度", "level": 4, "desc": "大模型应用进入规模化落地期"},
        {"name": "业绩弹性", "level": 5, "desc": "头部算力公司业绩增速普遍超过100%"},
    ]
)
gen.add_beneficiary_stocks([
    {"name": "寒武纪", "code": "688256", "logic": "国内AI芯片龙头", "elasticity": "目标涨幅50-80%", "rating": "强烈推荐"},
    {"name": "中际旭创", "code": "300308", "logic": "全球光模块龙头", "elasticity": "目标涨幅30-50%", "rating": "推荐"},
    {"name": "雅克科技", "code": "002409", "logic": "HBM前驱体全球第二", "elasticity": "目标涨幅40-60%", "rating": "强烈推荐"},
])
gen.add_timeline_analysis([
    {"stage": "概念期", "time": "2023-2024", "feature": "ChatGPT引爆AI概念", "related_stocks": "寒武纪"},
    {"stage": "成长期", "time": "2025-2026", "feature": "大模型规模化落地", "related_stocks": "中际旭创"},
    {"stage": "爆发期", "time": "2026-2027", "feature": "H200量产，AI应用大规模落地", "related_stocks": "雅克科技"},
])
gen.add_risk_warning(["AI芯片需求不及预期", "行业竞争加剧", "海外技术封锁风险"])
gen.add_investment_strategy("逢低布局，长期持有。建议配置仓位20-25%，回调10-15%是加仓良机。")

output_path = f"/root/daily-news-insight/docs/s级催化扫描/{DATE}_V30测试_S级催化.html"
gen.save(output_path)
print("✅ S级催化测试报告已生成")
