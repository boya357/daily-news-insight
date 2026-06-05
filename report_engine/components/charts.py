"""
图表组件库 - 数据可视化组件
"""

def pie_chart(title, data, colors=None):
    """
    饼图/环形图组件 (纯CSS实现)
    
    Args:
        title: 图表标题
        data: 数据列表，每个元素为{name, value}
        colors: 颜色列表
    """
    default_colors = ['#6366f1', '#8b5cf6', '#a855f7', '#d946ef', '#ec4899', '#f43f5e']
    if not colors:
        colors = default_colors[:len(data)]
    
    total = sum([d['value'] for d in data])
    
    legend_html = []
    for i, d in enumerate(data):
        pct = round(d['value'] / total * 100, 1)
        legend_html.append(f'''
            <div class="flex items-center mb-2">
                <div class="w-3 h-3 rounded-full mr-3" style="background-color: {colors[i]}"></div>
                <span class="text-sm text-gray-600 flex-1">{d["name"]}</span>
                <span class="text-sm font-semibold text-gray-800">{pct}%</span>
            </div>
        ''')
    
    return f'''
    <!-- ========== 市场份额饼图 ========== -->
    <div class="bg-white rounded-2xl p-6 shadow-lg">
        <h3 class="text-lg font-semibold text-gray-800 mb-6">{title}</h3>
        <div class="flex items-center">
            <div class="w-40 h-40 relative mr-8">
                <svg viewBox="0 0 36 36" class="w-full h-full transform -rotate-90">
                    <!-- CSS饼图由多个环形叠加实现 -->
                    <circle cx="18" cy="18" r="15.915" fill="transparent" stroke="{colors[0]}" stroke-width="3" stroke-dasharray="100 100" stroke-dashoffset="0"></circle>
                </svg>
                <div class="absolute inset-0 flex items-center justify-center">
                    <span class="text-xl font-bold text-gray-800">100%</span>
                </div>
            </div>
            <div class="flex-1">
                {''.join(legend_html)}
            </div>
        </div>
    </div>
    '''


def value_chain(title, layers):
    """
    产业链价值分布组件
    
    Args:
        title: 标题
        layers: 价值层级，每个元素为{name, value, color}
    """
    max_value = max([l['value'] for l in layers])
    
    bars_html = []
    for layer in layers:
        width = (layer['value'] / max_value) * 100
        color = layer.get('color', 'indigo')
        
        bars_html.append(f'''
            <div class="mb-4">
                <div class="flex justify-between mb-1">
                    <span class="text-sm text-gray-600">{layer["name"]}</span>
                    <span class="text-sm font-semibold text-gray-800">{layer["value"]}%</span>
                </div>
                <div class="h-4 bg-gray-100 rounded-full overflow-hidden">
                    <div class="h-full bg-gradient-to-r from-{color}-500 to-{color}-400 rounded-full transition-all duration-500" style="width: {width}%"></div>
                </div>
            </div>
        ''')
    
    return f'''
    <!-- ========== 产业链价值分布 ========== -->
    <div class="bg-white rounded-2xl p-6 shadow-lg">
        <h3 class="text-lg font-semibold text-gray-800 mb-6">{title}</h3>
        {''.join(bars_html)}
    </div>
    '''


def market_share_horizontal(title, companies):
    """
    横向市场份额对比图
    
    Args:
        title: 标题
        companies: 公司列表，每个元素为{name, share, highlight}
    """
    max_share = max([c['share'] for c in companies])
    
    bars_html = []
    for c in companies:
        width = (c['share'] / max_share) * 100
        highlight_class = 'ring-2 ring-indigo-500 ring-offset-2' if c.get('highlight', False) else ''
        color = 'indigo' if c.get('highlight', False) else 'gray'
        
        bars_html.append(f'''
            <div class="mb-5">
                <div class="flex justify-between mb-2">
                    <span class="text-sm font-medium text-gray-700">{c["name"]}</span>
                    <span class="text-sm font-bold text-gray-800">{c["share"]}%</span>
                </div>
                <div class="h-6 bg-gray-100 rounded-full overflow-hidden {highlight_class}">
                    <div class="h-full bg-gradient-to-r from-{color}-500 to-{color}-400 rounded-full transition-all duration-700" style="width: {width}%"></div>
                </div>
            </div>
        ''')
    
    return f'''
    <!-- ========== 市场份额横向对比 ========== -->
    <div class="bg-white rounded-2xl p-6 shadow-lg">
        <h3 class="text-lg font-semibold text-gray-800 mb-6">{title}</h3>
        {''.join(bars_html)}
    </div>
    '''
