"""
V4 组件库测试页面生成器
用于验证所有V4组件的渲染效果
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from components.v4_components import (
    V4Card, V4Tag, V4Button,
    V4RadarChart, V4ProgressBar, V4DataGrid, V4HorizontalBarChart,
    V4Tabs, V4Breadcrumb,
    V4StockCard, V4TopicCard,
    V4Section, V4PageHeader, V4MarketOverview,
    get_all_component_styles,
)


def generate_test_page():
    """生成V4组件测试页面"""
    
    # 面包屑
    breadcrumb = V4Breadcrumb([
        {'label': '首页', 'href': 'index_v4.html'},
        {'label': '组件库', 'href': '#'},
        {'label': '全部组件', 'href': ''},
    ])
    
    # 页面头部
    page_header = V4PageHeader(
        title="V4 组件库",
        subtitle="V4设计系统核心组件集合 · 统一视觉风格与交互体验",
    )
    
    # 1. 基础组件 - 标签
    tags_html = ''
    variants = ['primary', 'success', 'warning', 'danger', 'info', 'gray', 'green', 'red', 'blue', 'orange', 'purple']
    sizes = ['sm', 'md', 'lg']
    
    for variant in variants:
        tags_html += V4Tag(f"{variant} 标签", variant=variant).render() + ' '
    
    tags_section = V4Section(
        title="标签组件 (V4Tag)",
        icon="🏷️",
        content=tags_html,
        tag_text="基础组件"
    )
    
    # 2. 基础组件 - 按钮
    buttons_html = ''
    button_variants = ['primary', 'secondary', 'success', 'danger', 'outline']
    for variant in button_variants:
        buttons_html += V4Button(f"{variant} 按钮", variant=variant).render() + ' '
    
    buttons_html += '<br><br>'
    for size in ['sm', 'md', 'lg']:
        buttons_html += V4Button(f"{size} 尺寸", variant="primary", size=size).render() + ' '
    
    buttons_html += '<br><br>'
    buttons_html += V4Button("带图标按钮", variant="primary", icon="✨").render()
    buttons_html += V4Button("链接按钮", variant="outline", href="#").render()
    
    buttons_section = V4Section(
        title="按钮组件 (V4Button)",
        icon="🔘",
        content=buttons_html,
        tag_text="基础组件"
    )
    
    # 3. 数据可视化 - 雷达图
    radar = V4RadarChart(
        labels=['政策', '产业', '资金', '情绪', '估值', '催化'],
        values=[92, 95, 88, 90, 85, 96],
        size=250,
        color="#8B5CF6",
    )
    
    radar_section = V4Section(
        title="雷达图组件 (V4RadarChart)",
        icon="📊",
        content=f'<div style="text-align: center;">{radar.render()}</div>',
        tag_text="数据可视化"
    )
    
    # 4. 数据可视化 - 进度条
    progress_html = ''
    progress_data = [
        ('政策支持度', 92, '#8B5CF6'),
        ('产业成熟度', 78, '#10B981'),
        ('资金关注度', 85, '#EF4444'),
        ('市场情绪', 65, '#F59E0B'),
        ('估值水平', 55, '#3B82F6'),
    ]
    for label, value, color in progress_data:
        progress_html += V4ProgressBar(
            value=value, label=label, color=color
        ).render()
    
    progress_section = V4Section(
        title="进度条组件 (V4ProgressBar)",
        icon="📈",
        content=progress_html,
        tag_text="数据可视化"
    )
    
    # 5. 数据可视化 - 数据网格
    grid_data = [
        {'value': '12,345', 'label': '今日成交额（亿）', 'color': '#8B5CF6'},
        {'value': '2,856', 'label': '上涨家数', 'color': '#EF4444'},
        {'value': '1,987', 'label': '下跌家数', 'color': '#10B981'},
        {'value': '贪婪', 'label': '市场情绪', 'color': '#F59E0B'},
        {'value': '4.2%', 'label': '平均涨幅', 'color': '#EF4444'},
        {'value': '32', 'label': '涨停数量', 'color': '#EF4444'},
    ]
    data_grid = V4DataGrid(grid_data, columns=3)
    
    grid_section = V4Section(
        title="数据网格组件 (V4DataGrid)",
        icon="📋",
        content=data_grid.render(),
        tag_text="数据可视化"
    )
    
    # 6. 数据可视化 - 横向柱状图
    bar_data = [
        {'label': 'AI算力', 'value': 9.5, 'color': '#EF4444'},
        {'label': '存储芯片', 'value': 8.2, 'color': '#EF4444'},
        {'label': '人形机器人', 'value': 7.8, 'color': '#EF4444'},
        {'label': '先进封装', 'value': 6.5, 'color': '#EF4444'},
        {'label': '消费电子', 'value': 2.1, 'color': '#10B981'},
    ]
    bar_chart = V4HorizontalBarChart(bar_data)
    
    bar_section = V4Section(
        title="横向柱状图组件 (V4HorizontalBarChart)",
        icon="📊",
        content=bar_chart.render(),
        tag_text="数据可视化"
    )
    
    # 7. Tab切换组件
    tabs_content = [
        {
            'label': '📰 新闻分类',
            'content': '<p>这里是新闻分类的内容区域。Tab组件支持卡片、线条、胶囊三种样式。</p>'
        },
        {
            'label': '📈 市场数据',
            'content': '<p>这里是市场数据的内容区域。点击不同的Tab可以切换不同的内容。</p>'
        },
        {
            'label': '💡 题材分析',
            'content': '<p>这里是题材分析的内容区域。所有Tab内容都支持淡入动画效果。</p>'
        },
    ]
    
    tabs_styles = ['card', 'line', 'pill']
    tabs_html = ''
    for style in tabs_styles:
        tabs_html += f'<h3 style="margin: 20px 0 12px 0; color: #374151;">{style} 样式</h3>'
        tabs = V4Tabs(tabs_content, tab_style=style)
        tabs_html += tabs.render()
    
    tabs_section = V4Section(
        title="Tab切换组件 (V4Tabs)",
        icon="📑",
        content=tabs_html,
        tag_text="导航组件"
    )
    
    # 8. 股票卡片
    stock_data = {
        'name': '铜冠铜箔',
        'code': '301217',
        'price': 185.68,
        'change_pct': 10.02,
        'change': 16.90,
        'metrics': [
            {'value': '158.2亿', 'label': '总市值'},
            {'value': '85.3倍', 'label': '市盈率'},
            {'value': '23.5%', 'label': '换手率'},
        ]
    }
    stock_card = V4StockCard(stock_data)
    
    stock_section = V4Section(
        title="股票卡片组件 (V4StockCard)",
        icon="📈",
        content=stock_card.render(),
        tag_text="业务组件"
    )
    
    # 9. 题材卡片
    topic_data = {
        'level': 'S',
        'level_name': '最强主线',
        'name': 'AI PC/智能体PC',
        'icon': '💻',
        'score': 94.7,
        'description': 'AI终端革命，Arm架构PC芯片生态快速成熟，Windows on Arm转型大趋势，AI PC渗透率快速提升。',
        'core_stocks': ['华勤技术', '龙芯中科', '寒武纪', '瑞芯微', '全志科技'],
        'catalyst': '微软Windows on Arm生态成熟，AI PC渗透率快速提升',
        'radar': {'政策': 92, '产业': 99, '资金': 92, '情绪': 94, '估值': 92, '催化': 99},
        'deep_dive_url': '#',
    }
    topic_card = V4TopicCard(topic_data)
    
    topic_section = V4Section(
        title="题材卡片组件 (V4TopicCard)",
        icon="🚀",
        content=topic_card.render(),
        tag_text="业务组件"
    )
    
    # 10. 市场概览模块
    market_data = {
        'indices': [
            {'name': '上证指数', 'value': 3245.68, 'change_pct': 1.25},
            {'name': '深证成指', 'value': 10876.32, 'change_pct': 1.85},
            {'name': '创业板指', 'value': 2156.78, 'change_pct': 2.34},
            {'name': '科创50', 'value': 956.43, 'change_pct': 3.12},
        ],
        'up_count': 2856,
        'down_count': 1987,
        'flat_count': 234,
        'sentiment': '贪婪',
        'volume': '1.2万亿',
        'hot_sectors': [
            {'name': 'AI算力', 'change_pct': 9.5},
            {'name': '存储芯片', 'change_pct': 8.2},
            {'name': '人形机器人', 'change_pct': 7.8},
            {'name': '先进封装', 'change_pct': 6.5},
            {'name': '消费电子', 'change_pct': -2.1},
        ],
    }
    market_overview = V4MarketOverview(market_data)
    
    market_section = V4Section(
        title="市场概览模块 (V4MarketOverview)",
        icon="🌐",
        content=market_overview.render(),
        tag_text="复合组件"
    )
    
    # 组合所有内容
    all_sections = [
        tags_section.render(),
        buttons_section.render(),
        radar_section.render(),
        progress_section.render(),
        grid_section.render(),
        bar_section.render(),
        tabs_section.render(),
        stock_section.render(),
        topic_section.render(),
        market_section.render(),
    ]
    
    # 获取所有组件样式
    component_styles = get_all_component_styles()
    
    # 完整HTML
    html = f'''
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>V4 组件库 - 投资洞察系统</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", sans-serif;
            background: linear-gradient(135deg, #F8FAFC 0%, #F1F5F9 100%);
            color: #1F2937;
            line-height: 1.6;
            min-height: 100vh;
        }}
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            padding: 32px 24px;
        }}
        {component_styles}
    </style>
</head>
<body>
    <div class="container">
        {breadcrumb.render()}
        {page_header.render()}
        {''.join(all_sections)}
    </div>
</body>
</html>
    '''
    
    return html


if __name__ == '__main__':
    html = generate_test_page()
    
    output_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        '..', 'docs', 'v4_components_test.html'
    )
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"✅ V4组件测试页面已生成: {output_path}")
    print(f"   文件大小: {os.path.getsize(output_path)} 字节")
