"""
核心UI组件库 - 基础展示组件
"""

def gradient_banner(title, subtitle, metrics=None):
    metrics_html = ""
    if metrics:
        metrics_items = []
        for m in metrics:
            item = '<div class="bg-white/20 backdrop-blur-sm rounded-2xl px-8 py-4 text-white"><div class="text-3xl font-bold">' + m["value"] + '</div><div class="text-sm opacity-80">' + m["label"] + '</div></div>'
            metrics_items.append(item)
        metrics_html = '<div class="mt-8 grid grid-cols-2 md:grid-cols-4 gap-4">' + ''.join(metrics_items) + '</div>'
    
    return '''
    <div class="bg-gradient-to-r from-indigo-600 via-purple-600 to-pink-600 rounded-3xl p-8 md:p-12 text-white relative overflow-hidden">
        <div class="absolute top-0 right-0 w-96 h-96 bg-white/10 rounded-full -translate-y-1/2 translate-x-1/2"></div>
        <div class="absolute bottom-0 left-0 w-64 h-64 bg-white/10 rounded-full translate-y-1/2 -translate-x-1/2"></div>
        <div class="relative z-10">
            <h1 class="text-3xl md:text-4xl font-bold mb-4">' + title + '</h1>
            <p class="text-xl md:text-2xl opacity-90 mb-6">' + subtitle + '</p>' + metrics_html + '''
        </div>
    </div>
    '''


def data_card_grid(title, cards, cols=3):
    cols_class = {2: 'md:grid-cols-2', 3: 'md:grid-cols-3', 4: 'md:grid-cols-4'}.get(cols, 'md:grid-cols-3')
    card_items = []
    for card in cards:
        color = card.get('color', 'blue')
        trend = card.get('trend', '')
        trend_html = ''
        if trend:
            trend_color = 'text-green-500' if trend.startswith('+') else 'text-red-500'
            trend_html = '<span class="' + trend_color + ' text-sm ml-2">' + trend + '</span>'
        card_html = '''
            <div class="bg-white rounded-2xl p-6 shadow-lg hover:shadow-xl transition-shadow">
                <div class="flex items-center justify-between mb-4">
                    <div class="w-12 h-12 bg-''' + color + '''-100 rounded-xl flex items-center justify-center">
                        <i class="fa ''' + card["icon"] + ''' text-''' + color + '''-600 text-xl"></i>
                    </div>''' + trend_html + '''
                </div>
                <div class="text-3xl font-bold text-gray-800 mb-1">' + card["value"] + '</div>
                <div class="text-sm text-gray-500">' + card["title"] + '</div>
            </div>
        '''
        card_items.append(card_html)
    return '''
    <section class="mb-12">
        <h2 class="text-2xl font-bold text-gray-800 mb-6 flex items-center">
            <span class="w-1 h-8 bg-gradient-to-b from-indigo-500 to-purple-500 rounded-full mr-3"></span>''' + title + '''
        </h2>
        <div class="grid grid-cols-1 ''' + cols_class + ''' gap-6">''' + ''.join(card_items) + '''
        </div>
    </section>
    '''


def comparison_table(title, headers, rows, highlight_col=None):
    header_html = ''.join(['<th class="px-4 py-3 text-left text-sm font-semibold text-gray-700">' + h + '</th>' for h in headers])
    rows_html = []
    for row in rows:
        cells = []
        for i, cell in enumerate(row):
            highlight_class = 'text-gray-600'
            if highlight_col is not None:
                if (isinstance(highlight_col, int) and i == highlight_col) or (isinstance(highlight_col, str) and headers[i] == highlight_col):
                    highlight_class = 'bg-indigo-50 font-semibold text-indigo-700'
            cells.append('<td class="px-4 py-3 text-sm ' + highlight_class + '">' + cell + '</td>')
        rows_html.append('<tr class="border-b border-gray-100 hover:bg-gray-50">' + ''.join(cells) + '</tr>')
    return '''
    <section class="mb-12">
        <h2 class="text-2xl font-bold text-gray-800 mb-6 flex items-center">
            <span class="w-1 h-8 bg-gradient-to-b from-indigo-500 to-purple-500 rounded-full mr-3"></span>''' + title + '''
        </h2>
        <div class="bg-white rounded-2xl shadow-lg overflow-hidden">
            <div class="overflow-x-auto">
                <table class="w-full">
                    <thead class="bg-gray-50">
                        <tr class="border-b border-gray-200">''' + header_html + '''</tr>
                    </thead>
                    <tbody class="divide-y divide-gray-100">''' + ''.join(rows_html) + '''</tbody>
                </table>
            </div>
        </div>
    </section>
    '''


def quote_block(content, source=None):
    source_html = ''
    if source:
        source_html = '<div class="text-sm text-gray-500 mt-3">—— ' + source + '</div>'
    return '''
    <div class="bg-gradient-to-r from-indigo-50 to-purple-50 rounded-2xl p-6 mb-8 border-l-4 border-indigo-500">
        <div class="flex items-start">
            <i class="fa fa-quote-left text-indigo-400 text-2xl mr-4 mt-1"></i>
            <div>
                <p class="text-gray-700 leading-relaxed">' + content + '</p>' + source_html + '''
            </div>
        </div>
    </div>
    '''


def risk_opportunity(title, risks, opportunities):
    risks_items = []
    for r in risks:
        risks_items.append('<li class="flex items-start mb-2"><span class="w-2 h-2 bg-red-500 rounded-full mr-3 mt-2"></span><span class="text-gray-700">' + r + '</span></li>')
    risks_html = ''.join(risks_items)
    opps_items = []
    for o in opportunities:
        opps_items.append('<li class="flex items-start mb-2"><span class="w-2 h-2 bg-green-500 rounded-full mr-3 mt-2"></span><span class="text-gray-700">' + o + '</span></li>')
    opps_html = ''.join(opps_items)
    return '''
    <section class="mb-12">
        <h2 class="text-2xl font-bold text-gray-800 mb-6 flex items-center">
            <span class="w-1 h-8 bg-gradient-to-b from-indigo-500 to-purple-500 rounded-full mr-3"></span>''' + title + '''
        </h2>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div class="bg-red-50 rounded-2xl p-6">
                <h3 class="text-lg font-semibold text-red-700 mb-4 flex items-center">
                    <i class="fa fa-exclamation-triangle mr-2"></i>风险提示
                </h3>
                <ul class="space-y-2">''' + risks_html + '''</ul>
            </div>
            <div class="bg-green-50 rounded-2xl p-6">
                <h3 class="text-lg font-semibold text-green-700 mb-4 flex items-center">
                    <i class="fa fa-lightbulb-o mr-2"></i>投资机会
                </h3>
                <ul class="space-y-2">''' + opps_html + '''</ul>
            </div>
        </div>
    </section>
    '''


def industry_chain_diagram(title, layers):
    layers_html = []
    for idx, layer in enumerate(layers):
        color = layer.get('color', 'blue')
        companies = ', '.join(layer['companies'])
        arrow = '<i class="fa fa-chevron-right text-gray-300 mx-4"></i>' if idx < len(layers) - 1 else ''
        layers_html.append('<div class="flex items-center"><div class="w-32 flex-shrink-0"><div class="bg-' + color + '-100 text-' + color + '-700 px-4 py-2 rounded-lg text-center font-semibold text-sm">' + layer["name"] + '</div></div><div class="flex-1 ml-4"><div class="bg-white rounded-xl px-4 py-3 shadow-sm"><span class="text-gray-600 text-sm">' + companies + '</span></div></div>' + arrow + '</div>')
    return '''
    <section class="mb-12">
        <h2 class="text-2xl font-bold text-gray-800 mb-6 flex items-center">
            <span class="w-1 h-8 bg-gradient-to-b from-indigo-500 to-purple-500 rounded-full mr-3"></span>''' + title + '''
        </h2>
        <div class="bg-gradient-to-br from-gray-50 to-white rounded-2xl p-6 shadow-lg">
            <div class="space-y-4">''' + ''.join(layers_html) + '''</div>
        </div>
    </section>
    '''


def conclusion_block(title, points):
    points_items = []
    for i, p in enumerate(points):
        points_items.append('<div class="flex items-start mb-4"><div class="w-8 h-8 bg-gradient-to-br from-indigo-500 to-purple-500 rounded-lg flex items-center justify-center text-white font-bold mr-4 flex-shrink-0">' + str(i + 1) + '</div><div class="text-gray-700 pt-1">' + p + '</div></div>')
    points_html = ''.join(points_items)
    return '''
    <section class="mb-12">
        <h2 class="text-2xl font-bold text-gray-800 mb-6 flex items-center">
            <span class="w-1 h-8 bg-gradient-to-b from-indigo-500 to-purple-500 rounded-full mr-3"></span>''' + title + '''
        </h2>
        <div class="bg-gradient-to-br from-indigo-50 via-purple-50 to-pink-50 rounded-2xl p-6">''' + points_html + '''</div>
    </section>
    '''
