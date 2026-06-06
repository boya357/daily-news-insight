#!/usr/bin/env python3
"""
V3.0 系统测试脚本
测试所有组件、生成器、校验器是否正常工作
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_basic_components():
    """测试基础组件"""
    print("🔧 测试基础组件...")
    
    from components.layout import Navbar, Footer, Section, Card
    
    # 测试Navbar
    nav = Navbar(active_key="industry_chain")
    nav_html = nav.render()
    assert "投资研究中心" in nav_html, "Navbar缺少站点名称"
    assert "产业链" in nav_html, "Navbar缺少产业链链接"
    assert "toggleMobileMenu" in nav_html, "Navbar缺少移动端菜单函数"
    assert "hamburger-btn" in nav_html, "Navbar缺少汉堡按钮"
    print("  ✅ Navbar 正常")
    
    # 测试Footer
    footer = Footer()
    footer_html = footer.render()
    assert "投资研究中心" in footer_html, "Footer缺少站点名称"
    print("  ✅ Footer 正常")
    
    # 测试Section
    section = Section("测试标题", "测试内容", subtitle="测试副标题", icon="📊")
    section_html = section.render()
    assert "测试标题" in section_html
    assert "测试内容" in section_html
    assert "测试副标题" in section_html
    assert "📊" in section_html
    print("  ✅ Section 正常")
    
    # 测试Card
    card = Card("卡片内容", title="卡片标题", variant="primary")
    card_html = card.render()
    assert "卡片标题" in card_html
    assert "卡片内容" in card_html
    print("  ✅ Card 正常")


def test_data_components():
    """测试数据组件"""
    print("📊 测试数据组件...")
    
    from components.data import DataCard, DataGrid, CompareTable, MetricsRow
    
    # 测试DataCard
    dc = DataCard("市值", "285亿", trend="+5.2%", trend_up=True, unit="元")
    dc_html = dc.render()
    assert "市值" in dc_html
    assert "285亿" in dc_html
    assert "+5.2%" in dc_html
    assert "text-red-500" in dc_html  # 上涨应该是红色
    print("  ✅ DataCard 正常")
    
    # 测试DataGrid
    grid = DataGrid([
        DataCard("营收", "100亿"),
        DataCard("利润", "20亿"),
        DataCard("毛利率", "35%"),
        DataCard("PE", "25x"),
    ], cols=4)
    grid_html = grid.render()
    assert grid_html.count("bg-white/80") == 4
    print("  ✅ DataGrid 正常")
    
    # 测试CompareTable
    table = CompareTable(
        headers=["公司", "市值", "PE", "评级"],
        rows=[
            ["公司A", "1000亿", "25x", "买入"],
            ["公司B", "500亿", "20x", "持有"],
            ["公司C", "200亿", "15x", "买入"],
        ],
        highlight_rows=[0],
        highlight_cols=[3],
    )
    table_html = table.render()
    assert "公司A" in table_html
    assert "bg-indigo-50/50" in table_html  # 高亮行
    assert "text-indigo-600" in table_html  # 高亮列
    print("  ✅ CompareTable 正常")
    
    # 测试MetricsRow
    metrics = MetricsRow([
        ("涨幅", "+5.2%", True),
        ("换手率", "3.5%", None),
        ("成交量", "100万手", True),
    ])
    metrics_html = metrics.render()
    assert "+5.2%" in metrics_html
    assert metrics_html.count("bg-red-500") == 2  # 两个上涨
    assert "bg-gray-400" in metrics_html  # 一个平
    print("  ✅ MetricsRow 正常")


def test_chart_components():
    """测试图表组件"""
    print("📈 测试图表组件...")
    
    from components.charts import LineChart, BarChart, PieChart
    
    # 测试折线图
    line = LineChart(
        labels=["1月", "2月", "3月", "4月"],
        datasets=[
            {"label": "营收", "data": [100, 120, 150, 180]},
            {"label": "利润", "data": [20, 25, 30, 35]},
        ],
        title="营收趋势"
    )
    line_html = line.render()
    assert "营收趋势" in line_html
    assert "type" in line_html and "line" in line_html
    assert "maintainAspectRatio" in line_html
    assert "true" in line_html  # 确保是true
    print("  ✅ LineChart 正常")
    
    # 测试柱状图
    bar = BarChart(
        labels=["A", "B", "C"],
        datasets=[{"label": "销量", "data": [10, 20, 15]}],
        title="销量对比"
    )
    bar_html = bar.render()
    assert "bar" in bar_html
    print("  ✅ BarChart 正常")
    
    # 测试饼图
    pie = PieChart(
        labels=["产品A", "产品B", "产品C"],
        data=[40, 35, 25],
        title="收入占比"
    )
    pie_html = pie.render()
    assert "doughnut" in pie_html  # 默认环形图
    print("  ✅ PieChart 正常")


def test_special_components():
    """测试特殊组件"""
    print("🎨 测试特殊组件...")
    
    from components.special import RiskAlert, QuoteBlock, Timeline, ButtonGroup, CatalystTag
    
    # 测试RiskAlert
    risk = RiskAlert("danger", "这是高风险提示", title="风险警告")
    risk_html = risk.render()
    assert "风险警告" in risk_html
    assert "bg-red-50" in risk_html
    print("  ✅ RiskAlert 正常")
    
    # 测试QuoteBlock
    quote = QuoteBlock("投资是认知的变现", author="巴菲特", source="致股东信")
    quote_html = quote.render()
    assert "投资是认知的变现" in quote_html
    assert "巴菲特" in quote_html
    print("  ✅ QuoteBlock 正常")
    
    # 测试Timeline
    timeline = Timeline([
        {"time": "2024-01", "title": "事件1", "content": "内容1", "type": "primary"},
        {"time": "2024-02", "title": "事件2", "content": "内容2", "type": "success"},
    ])
    timeline_html = timeline.render()
    assert "事件1" in timeline_html
    assert "事件2" in timeline_html
    print("  ✅ Timeline 正常")
    
    # 测试ButtonGroup
    btns = ButtonGroup([
        {"text": "查看详情", "link": "#", "variant": "primary"},
        {"text": "返回", "link": "#", "variant": "secondary"},
    ])
    btns_html = btns.render()
    assert "查看详情" in btns_html
    assert "bg-indigo-500" in btns_html
    print("  ✅ ButtonGroup 正常")
    
    # 测试CatalystTag
    tag = CatalystTag("S级催化", level="s")
    tag_html = tag.render()
    assert "S级催化" in tag_html
    assert "from-purple-500" in tag_html
    print("  ✅ CatalystTag 正常")


def test_report_class():
    """测试Report核心类"""
    print("📝 测试Report核心类...")
    
    from core.report import Report
    from components.layout import Section
    from components.data import DataCard
    
    # 创建报告
    report = Report(title="测试报告", report_type="industry_chain", subtitle="测试副标题")
    
    # 添加组件
    report.add(Section("第一节", "这是第一节的内容"))
    report.add_section("第二节", "这是第二节的内容", icon="📊")
    report.add_data_grid([
        DataCard("指标1", "100"),
        DataCard("指标2", "200"),
    ])
    report.add_risk_alert("warning", "注意投资风险")
    
    # 生成HTML
    html = report.generate()
    
    # 验证
    assert "<!DOCTYPE html>" in html
    assert "<html" in html
    assert "<head>" in html
    assert "<body>" in html
    assert "测试报告" in html
    assert "测试副标题" in html
    assert "第一节" in html
    assert "第二节" in html
    assert "glass-nav" in html
    assert "hamburger-btn" in html
    assert "toggleMobileMenu" in html
    assert "投资研究中心" in html
    
    print("  ✅ Report 类正常")
    return html


def test_validators(html: str):
    """测试校验器"""
    print("✅ 测试校验器...")
    
    from validators.structure import StructureValidator
    from validators.links import LinkValidator
    from validators.content import ContentValidator
    
    # 结构校验
    struct_errors = StructureValidator.validate(html)
    print(f"  结构校验: {len(struct_errors)} 个错误")
    for err in struct_errors:
        print(f"    ❌ {err}")
    
    # 链接校验
    link_errors = LinkValidator.validate(html)
    print(f"  链接校验: {len(link_errors)} 个错误")
    for err in link_errors:
        print(f"    ❌ {err}")
    
    # 内容校验
    content_errors = ContentValidator.validate(html)
    print(f"  内容校验: {len(content_errors)} 个错误")
    for err in content_errors:
        print(f"    ❌ {err}")
    
    all_errors = struct_errors + link_errors + content_errors
    if all_errors:
        print(f"  ⚠️  共发现 {len(all_errors)} 个问题")
    else:
        print("  ✅ 所有校验通过！")
    
    return all_errors


def test_deep_dive_generator():
    """测试深度研究报告生成器"""
    print("🚀 测试深度研究生成器...")
    
    from generators.deep_dive import DeepDiveGenerator
    from components.data import DataCard
    
    gen = DeepDiveGenerator(
        title="AI算力产业链深度研究",
        subtitle="2024年最具爆发力的赛道"
    )
    
    gen.add_summary(
        core_view="AI算力是未来3年确定性最高的赛道，全球AI芯片需求爆发式增长...",
        bull_points=[
            "大模型训练需求持续爆发",
            "算力基础设施建设加速",
            "国产替代空间广阔",
        ],
        bear_points=[
            "美国出口管制风险",
            "行业竞争加剧",
            "估值偏高",
        ]
    )
    
    gen.add_key_metrics([
        ("总市值", "5000亿", True),
        ("PE", "45x", None),
        ("毛利率", "65%", True),
        ("净利润增速", "+85%", True),
    ])
    
    gen.add_analysis_section(
        title="📈 行业趋势",
        content="<p>AI算力行业正处于高速发展期...</p><p>预计未来三年复合增速超过50%</p>",
        icon="📊"
    )
    
    gen.add_competitive_analysis(
        headers=["公司", "技术", "产能", "毛利率", "评级"],
        rows=[
            ["龙头A", "领先", "10万片/月", "70%", "买入"],
            ["公司B", "先进", "5万片/月", "60%", "增持"],
            ["公司C", "追赶", "2万片/月", "45%", "中性"],
        ],
        highlight_rows=[0],
    )
    
    gen.add_timeline([
        {"time": "2024-01", "title": "大模型发布", "content": "GPT-5发布，算力需求激增", "type": "primary"},
        {"time": "2024-03", "title": "政策支持", "content": "国家出台算力支持政策", "type": "success"},
    ])
    
    gen.add_catalyst_tags(["AI大模型", "算力基建", "国产替代", "数据中心"])
    
    gen.add_risk_section([
        "技术迭代不及预期",
        "行业竞争加剧导致毛利率下滑",
        "美国出口管制政策收紧",
    ])
    
    gen.add_conclusion(
        conclusion="AI算力赛道长期向好，建议关注具备核心技术优势的龙头企业...",
        rating="推荐"
    )
    
    html = gen.generate()
    
    # 保存测试
    test_file = "/tmp/test_deep_dive.html"
    gen.save(test_file)
    
    print(f"  ✅ 深度研究报告生成成功")
    print(f"  📄 已保存到: {test_file}")
    
    return html


def test_list_page():
    """测试列表页生成器"""
    print("📋 测试列表页生成器...")
    
    from generators.list_page import ListPageGenerator
    
    gen = ListPageGenerator("industry_chain")
    
    # 创建列表页
    list_file = "/tmp/test_list.html"
    gen.create_list_page(
        output_path=list_file,
        title="产业链深度研究",
        description="深度解析各产业链投资机会"
    )
    
    # 插入报告
    success = gen.insert_report(
        list_filepath=list_file,
        title="AI算力产业链深度研究",
        date="2024-06-06",
        url="20240606_ai_compute.html",
        excerpt="AI算力是未来3年确定性最高的赛道...",
        tag="深度"
    )
    
    assert success, "插入报告失败"
    
    # 再插入一篇
    success2 = gen.insert_report(
        list_filepath=list_file,
        title="存储芯片产业链研究",
        date="2024-06-05",
        url="20240605_memory.html",
        excerpt="存储芯片周期反转，AI带动需求爆发...",
        tag="深度"
    )
    
    assert success2, "插入第二篇报告失败"
    
    count = gen.get_report_count(list_file)
    assert count == 2, f"期望2篇报告，实际{count}篇"
    
    print(f"  ✅ 列表页生成器正常，共 {count} 篇报告")
    print(f"  📄 列表页已保存到: {list_file}")


def main():
    """主测试函数"""
    print("=" * 60)
    print("V3.0 报告生成系统 - 全面测试")
    print("=" * 60)
    print()
    
    all_passed = True
    
    try:
        test_basic_components()
    except Exception as e:
        print(f"  ❌ 基础组件测试失败: {e}")
        all_passed = False
    print()
    
    try:
        test_data_components()
    except Exception as e:
        print(f"  ❌ 数据组件测试失败: {e}")
        all_passed = False
    print()
    
    try:
        test_chart_components()
    except Exception as e:
        print(f"  ❌ 图表组件测试失败: {e}")
        all_passed = False
    print()
    
    try:
        test_special_components()
    except Exception as e:
        print(f"  ❌ 特殊组件测试失败: {e}")
        all_passed = False
    print()
    
    try:
        html = test_report_class()
    except Exception as e:
        print(f"  ❌ Report类测试失败: {e}")
        import traceback
        traceback.print_exc()
        all_passed = False
        html = ""
    print()
    
    try:
        errors = test_validators(html) if html else []
        if errors:
            all_passed = False
    except Exception as e:
        print(f"  ❌ 校验器测试失败: {e}")
        import traceback
        traceback.print_exc()
        all_passed = False
    print()
    
    try:
        test_deep_dive_generator()
    except Exception as e:
        print(f"  ❌ 深度研究生成器测试失败: {e}")
        import traceback
        traceback.print_exc()
        all_passed = False
    print()
    
    try:
        test_list_page()
    except Exception as e:
        print(f"  ❌ 列表页生成器测试失败: {e}")
        import traceback
        traceback.print_exc()
        all_passed = False
    print()
    
    print("=" * 60)
    if all_passed:
        print("🎉 所有测试通过！V3.0系统运行正常")
    else:
        print("⚠️  部分测试失败，请检查问题")
    print("=" * 60)
    
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
