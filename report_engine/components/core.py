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
    
    html = '''
    <div class="bg-gradient-to-r from-indigo-600 via-purple-600 to-pink-600 rounded-3xl p-8 md:p-12 text-white relative overflow-hidden">
        <div class="absolute top-0 right-0 w-96 h-96 bg-white/10 rounded-full -translate-y-1/2 translate-x-1/2"></div>
        <div class="absolute bottom-0 left-0 w-64 h-64 bg-white/10 rounded-full translate-y-1/2 -translate-x-1/2"></div>
        <div class="relative z-10">
            <h1 class="text-3xl md:text-4xl font-bold mb-4">TITLE_PLACEHOLDER</h1>
            <p class="text-xl md:text-2xl opacity-90 mb-6">SUBTITLE_PLACEHOLDER</p>METRICS_PLACEHOLDER
        </div>
    </div>
    '''
    html = html.replace('TITLE_PLACEHOLDER', title)
    html = html.replace('SUBTITLE_PLACEHOLDER', subtitle)
    html = html.replace('METRICS_PLACEHOLDER', metrics_html)
    return html


def data_card_grid(title, cards, cols=3):
    cols_class = {2: 'md:grid-cols-2', 3: 'md:grid-cols-3', 4: 'md:grid-cols-4'}.get(cols, 'md:grid-cols-3')
    card_items = []
    for card in cards:
        color = card.get('color', 'blue')
        item = '''
            <div class="bg-white rounded-2xl p-6 shadow-lg hover:shadow-xl transition-shadow">
                <div class="flex items-center justify-between mb-4">
                    <div class="w-12 h-12 bg-{color}-100 rounded-xl flex items-center justify-center">
                        <i class="fa {icon} text-{color}-600 text-xl"></i>
                    </div>
                    <span class="text-{color}-500 text-sm ml-2">{trend}</span>
                </div>
                <div class="text-3xl font-bold text-gray-800 mb-1">{value}</div>
                <div class="text-sm text-gray-500">{title}</div>
            </div>
        '''.format(color=color, icon=card.get('icon', 'fa-star'), trend=card.get('trend', ''), value=card.get('value', ''), title=card.get('title', ''))
        card_items.append(item)
    
    return '''
    <section class="mb-12">
        <h2 class="text-2xl font-bold text-gray-800 mb-6 flex items-center">
            <span class="w-1 h-8 bg-gradient-to-b from-indigo-500 to-purple-500 rounded-full mr-3"></span>
            ''' + title + '''
        </h2>
        <div class="grid grid-cols-1 ''' + cols_class + ''' gap-6">''' + ''.join(card_items) + '''
        </div>
    </section>
    '''


def comparison_table(title, headers, rows):
    header_html = ''.join([f'<th class="px-4 py-3 text-left text-sm font-semibold text-gray-700">{h}</th>' for h in headers])
    rows_html = ''
    for row in rows:
        cells = ''.join([f'<td class="px-4 py-3 text-sm text-gray-600">{c}</td>' for c in row])
        rows_html += f'<tr class="border-b border-gray-100 hover:bg-gray-50">{cells}</tr>'
    
    return '''
    <section class="mb-12">
        <h2 class="text-2xl font-bold text-gray-800 mb-6 flex items-center">
            <span class="w-1 h-8 bg-gradient-to-b from-indigo-500 to-purple-500 rounded-full mr-3"></span>
            ''' + title + '''
        </h2>
        <div class="bg-white rounded-2xl shadow-lg overflow-hidden">
            <table class="w-full">
                <thead class="bg-gray-50">
                    <tr>''' + header_html + '''</tr>
                </thead>
                <tbody>''' + rows_html + '''</tbody>
            </table>
        </div>
    </section>
    '''


def quote_block(content, source=""):
    source_html = f'<p class="text-right text-sm text-gray-400 mt-4">— {source}</p>' if source else ''
    return '''
    <section class="mb-12">
        <div class="bg-gradient-to-r from-indigo-50 via-purple-50 to-pink-50 rounded-2xl p-8 border-l-4 border-indigo-500">
            <p class="text-lg text-gray-700 italic leading-relaxed">"''' + content + '''"</p>''' + source_html + '''
        </div>
    </section>
    '''


def risk_opportunity(title, risks, opportunities):
    risks_html = ''.join([f'<li class="flex items-start mb-2"><span class="w-2 h-2 bg-red-500 rounded-full mr-3 mt-2"></span><span class="text-gray-700">{r}</span></li>' for r in risks])
    ops_html = ''.join([f'<li class="flex items-start mb-2"><span class="w-2 h-2 bg-green-500 rounded-full mr-3 mt-2"></span><span class="text-gray-700">{o}</span></li>' for o in opportunities])
    
    return '''
    <section class="mb-12">
        <h2 class="text-2xl font-bold text-gray-800 mb-6 flex items-center">
            <span class="w-1 h-8 bg-gradient-to-b from-indigo-500 to-purple-500 rounded-full mr-3"></span>
            ''' + title + '''
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
                <ul class="space-y-2">''' + ops_html + '''</ul>
            </div>
        </div>
    </section>
    '''


def industry_chain_diagram(title, layers):
    layers_html = ''.join([f'<div class="py-3 px-4 text-center font-medium text-gray-700" style="width: {layer.get("width", 100)}%">{layer["name"]}</div>' for layer in layers])
    
    return '''
    <section class="mb-12">
        <h2 class="text-2xl font-bold text-gray-800 mb-6 flex items-center">
            <span class="w-1 h-8 bg-gradient-to-b from-indigo-500 to-purple-500 rounded-full mr-3"></span>
            ''' + title + '''
        </h2>
        <div class="bg-white rounded-2xl p-6 shadow-lg">
            <div class="flex flex-col items-center space-y-3">''' + layers_html + '''
            </div>
        </div>
    </section>
    '''


def conclusion_block(title, points):
    points_html = ''.join([f'''
        <div class="flex items-start mb-4">
            <div class="w-8 h-8 bg-gradient-to-br from-indigo-500 to-purple-500 rounded-lg flex items-center justify-center text-white font-bold mr-4 flex-shrink-0">{i+1}</div>
            <div class="text-gray-700 pt-1">{p}</div>
        </div>''' for i, p in enumerate(points)])
    
    return '''
    <section class="mb-12">
        <h2 class="text-2xl font-bold text-gray-800 mb-6 flex items-center">
            <span class="w-1 h-8 bg-gradient-to-b from-indigo-500 to-purple-500 rounded-full mr-3"></span>
            ''' + title + '''
        </h2>
        <div class="bg-gradient-to-br from-indigo-50 via-purple-50 to-pink-50 rounded-2xl p-6">''' + points_html + '''
        </div>
    </section>
    '''
