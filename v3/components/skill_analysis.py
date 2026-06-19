"""
Skill分析渲染组件
整合多个Skill的核心分析能力，提供统一的HTML渲染接口

支持的分析类型：
1. 三维热度分析（政策-产业-资金）
2. SWOT分析
3. 情景推演（乐观/中性/悲观）
4. 产业链传导分析
5. 5Why深度追问
"""
from typing import Dict, List, Optional


def render_three_d_heat(heat_data: Dict, title: str = "三维热度评估") -> str:
    """渲染三维热度分析卡片"""
    policy_score = heat_data.get('policy_score', 50)
    industry_score = heat_data.get('industry_score', 50)
    capital_score = heat_data.get('capital_score', 50)
    overall_score = heat_data.get('overall_score', 50)
    conclusion = heat_data.get('conclusion', '中性热度')
    
    # 分数对应的颜色
    def get_color(score):
        if score >= 80:
            return 'from-green-500 to-emerald-500'
        elif score >= 60:
            return 'from-yellow-500 to-orange-500'
        elif score >= 40:
            return 'from-orange-500 to-red-500'
        else:
            return 'from-red-500 to-rose-500'
    
    def get_bar_color(score):
        if score >= 80:
            return 'bg-green-500'
        elif score >= 60:
            return 'bg-yellow-500'
        elif score >= 40:
            return 'bg-orange-500'
        else:
            return 'bg-red-500'
    
    # 热度等级
    if overall_score >= 80:
        level = '🔥 超高热度'
        level_color = 'text-red-400'
    elif overall_score >= 60:
        level = '☀️ 较高热度'
        level_color = 'text-orange-400'
    elif overall_score >= 40:
        level = '⛅ 中等热度'
        level_color = 'text-yellow-400'
    else:
        level = '❄️ 较低热度'
        level_color = 'text-blue-400'
    
    return f'''
    <div class="bg-white/5 backdrop-blur-sm rounded-xl p-4 border border-white/10">
        <div class="flex items-center justify-between mb-4">
            <h4 class="font-bold text-white flex items-center gap-2">
                <span>🌡️</span> {title}
            </h4>
            <span class="text-xs bg-white/10 px-2 py-1 rounded-full text-white/70">
                Skill增强
            </span>
        </div>
        
        <!-- 综合热度 -->
        <div class="text-center mb-4">
            <div class="text-4xl font-black bg-gradient-to-r {get_color(overall_score)} bg-clip-text text-transparent">
                {overall_score:.0f}
            </div>
            <div class="text-sm {level_color} font-semibold mt-1">{level}</div>
            <div class="text-xs text-white/50 mt-1">{conclusion}</div>
        </div>
        
        <!-- 三个维度 -->
        <div class="space-y-3">
            <div>
                <div class="flex justify-between text-xs mb-1">
                    <span class="text-white/70">📋 政策维度</span>
                    <span class="text-white font-semibold">{policy_score:.0f}分</span>
                </div>
                <div class="w-full h-2 bg-white/10 rounded-full overflow-hidden">
                    <div class="h-full {get_bar_color(policy_score)} rounded-full transition-all duration-500" 
                         style="width: {policy_score}%"></div>
                </div>
            </div>
            <div>
                <div class="flex justify-between text-xs mb-1">
                    <span class="text-white/70">🏭 产业维度</span>
                    <span class="text-white font-semibold">{industry_score:.0f}分</span>
                </div>
                <div class="w-full h-2 bg-white/10 rounded-full overflow-hidden">
                    <div class="h-full {get_bar_color(industry_score)} rounded-full transition-all duration-500" 
                         style="width: {industry_score}%"></div>
                </div>
            </div>
            <div>
                <div class="flex justify-between text-xs mb-1">
                    <span class="text-white/70">💰 资金维度</span>
                    <span class="text-white font-semibold">{capital_score:.0f}分</span>
                </div>
                <div class="w-full h-2 bg-white/10 rounded-full overflow-hidden">
                    <div class="h-full {get_bar_color(capital_score)} rounded-full transition-all duration-500" 
                         style="width: {capital_score}%"></div>
                </div>
            </div>
        </div>
    </div>
    '''


def render_swot(swot_data: Dict, title: str = "SWOT分析") -> str:
    """渲染SWOT分析卡片"""
    strengths = swot_data.get('strengths', [])
    weaknesses = swot_data.get('weaknesses', [])
    opportunities = swot_data.get('opportunities', [])
    threats = swot_data.get('threats', [])
    
    def render_list(items, icon, color_class):
        if not items:
            return f'<div class="text-white/30 text-xs">暂无数据</div>'
        lis = ''.join([f'<li class="text-xs text-white/70 mb-1.5 flex items-start gap-1.5"><span class="{color_class} mt-0.5">•</span><span>{item}</span></li>' for item in items])
        return f'<ul class="space-y-1">{lis}</ul>'
    
    return f'''
    <div class="bg-white/5 backdrop-blur-sm rounded-xl p-4 border border-white/10">
        <div class="flex items-center justify-between mb-4">
            <h4 class="font-bold text-white flex items-center gap-2">
                <span>📊</span> {title}
            </h4>
            <span class="text-xs bg-purple-500/20 text-purple-400 px-2 py-1 rounded-full border border-purple-500/30">
                超级分析师框架
            </span>
        </div>
        
        <div class="grid grid-cols-2 gap-3">
            <!-- 优势 -->
            <div class="bg-green-500/10 rounded-lg p-3 border border-green-500/20">
                <div class="text-green-400 font-bold text-sm mb-2 flex items-center gap-1">
                    <span>💪</span> 优势 (S)
                </div>
                {render_list(strengths, '•', 'text-green-400')}
            </div>
            
            <!-- 劣势 -->
            <div class="bg-red-500/10 rounded-lg p-3 border border-red-500/20">
                <div class="text-red-400 font-bold text-sm mb-2 flex items-center gap-1">
                    <span>⚠️</span> 劣势 (W)
                </div>
                {render_list(weaknesses, '•', 'text-red-400')}
            </div>
            
            <!-- 机会 -->
            <div class="bg-blue-500/10 rounded-lg p-3 border border-blue-500/20">
                <div class="text-blue-400 font-bold text-sm mb-2 flex items-center gap-1">
                    <span>✨</span> 机会 (O)
                </div>
                {render_list(opportunities, '•', 'text-blue-400')}
            </div>
            
            <!-- 威胁 -->
            <div class="bg-orange-500/10 rounded-lg p-3 border border-orange-500/20">
                <div class="text-orange-400 font-bold text-sm mb-2 flex items-center gap-1">
                    <span>🔥</span> 威胁 (T)
                </div>
                {render_list(threats, '•', 'text-orange-400')}
            </div>
        </div>
    </div>
    '''


def render_scenarios(scenarios: List[Dict], title: str = "情景推演") -> str:
    """渲染情景推演卡片"""
    if not scenarios:
        return '<div class="text-white/50 text-sm">暂无情景分析数据</div>'
    
    scenario_cards = ''
    for s in scenarios:
        name = s.get('scenario_name', '未知情景')
        prob = s.get('probability', 0) * 100
        impact = s.get('impact_score', 0)
        ret = s.get('expected_return', 0) * 100
        desc = s.get('description', '')
        assumptions = s.get('key_assumptions', [])
        
        # 根据情景类型设置颜色
        if '乐观' in name:
            color = 'green'
            icon = '📈'
        elif '悲观' in name:
            color = 'red'
            icon = '📉'
        else:
            color = 'yellow'
            icon = '➡️'
        
        assumption_text = '、'.join(assumptions[:2]) if assumptions else '无'
        
        scenario_cards += f'''
        <div class="bg-{color}-500/10 rounded-lg p-3 border border-{color}-500/20">
            <div class="flex items-center justify-between mb-2">
                <span class="text-{color}-400 font-bold text-sm flex items-center gap-1">
                    {icon} {name}
                </span>
                <span class="text-xs bg-white/10 px-2 py-0.5 rounded-full text-white/70">
                    概率 {prob:.0f}%
                </span>
            </div>
            <div class="text-xs text-white/70 mb-2">{desc}</div>
            <div class="flex justify-between text-xs">
                <span class="text-white/50">影响程度: <span class="text-white font-semibold">{impact:.0f}</span></span>
                <span class="text-white/50">预期收益: <span class="text-{color}-400 font-semibold">{ret:+.1f}%</span></span>
            </div>
            <div class="mt-2 text-xs text-white/40">
                核心假设: {assumption_text}
            </div>
        </div>
        '''
    
    return f'''
    <div class="bg-white/5 backdrop-blur-sm rounded-xl p-4 border border-white/10">
        <div class="flex items-center justify-between mb-4">
            <h4 class="font-bold text-white flex items-center gap-2">
                <span>🎯</span> {title}
            </h4>
            <span class="text-xs bg-blue-500/20 text-blue-400 px-2 py-1 rounded-full border border-blue-500/30">
                情景规划框架
            </span>
        </div>
        <div class="space-y-2">
            {scenario_cards}
        </div>
    </div>
    '''


def render_industry_chain(chain_data: Dict, title: str = "产业链传导分析") -> str:
    """渲染产业链传导分析"""
    upstream = chain_data.get('upstream', [])
    midstream = chain_data.get('midstream', [])
    downstream = chain_data.get('downstream', [])
    impact_level = chain_data.get('impact_level', '中等')
    key_beneficiary = chain_data.get('key_beneficiary', '')
    
    def render_chain_items(items, label, icon, color):
        if not items:
            return f'<div class="text-white/30 text-xs">暂无{label}数据</div>'
        items_html = ''.join([
            f'<span class="inline-block bg-white/10 text-white/80 text-xs px-2 py-1 rounded-md mr-1 mb-1">{item}</span>' 
            for item in items
        ])
        return f'''
        <div class="mb-3 last:mb-0">
            <div class="text-xs font-semibold {color} mb-1.5 flex items-center gap-1">
                {icon} {label}
            </div>
            <div class="flex flex-wrap gap-1">
                {items_html}
            </div>
        </div>
        '''
    
    return f'''
    <div class="bg-white/5 backdrop-blur-sm rounded-xl p-4 border border-white/10">
        <div class="flex items-center justify-between mb-4">
            <h4 class="font-bold text-white flex items-center gap-2">
                <span>🔗</span> {title}
            </h4>
            <span class="text-xs bg-emerald-500/20 text-emerald-400 px-2 py-1 rounded-full border border-emerald-500/30">
                产业链分析
            </span>
        </div>
        
        {render_chain_items(upstream, '上游受益', '⬆️', 'text-emerald-400')}
        {render_chain_items(midstream, '中游传导', '➡️', 'text-blue-400')}
        {render_chain_items(downstream, '下游需求', '⬇️', 'text-purple-400')}
        
        {key_beneficiary and f'''
        <div class="mt-3 pt-3 border-t border-white/10">
            <div class="text-xs text-white/50 mb-1">核心受益环节</div>
            <div class="text-sm font-semibold text-yellow-400">{key_beneficiary}</div>
        </div>
        '''}
    </div>
    '''


def render_five_why(five_why_data: Dict, title: str = "5Why深度追问") -> str:
    """渲染5Why深度分析"""
    whys = five_why_data.get('whys', [])
    root_cause = five_why_data.get('root_cause', '')
    insight = five_why_data.get('insight', '')
    
    if not whys:
        return '<div class="text-white/50 text-sm">暂无5Why分析数据</div>'
    
    why_items = ''
    for i, why in enumerate(whys):
        why_text = why.get('question', '')
        answer_text = why.get('answer', '')
        depth = why.get('depth', i+1)
        
        colors = ['text-blue-400', 'text-cyan-400', 'text-teal-400', 'text-emerald-400', 'text-green-400']
        color = colors[min(i, len(colors)-1)]
        
        why_items += f'''
        <div class="relative pl-6 pb-4 last:pb-0">
            <div class="absolute left-0 top-0 w-5 h-5 rounded-full bg-white/10 flex items-center justify-center text-xs font-bold {color}">
                {depth}
            </div>
            {i < len(whys)-1 and '<div class="absolute left-2.5 top-5 w-0.5 h-full bg-white/10"></div>' or ''}
            <div class="text-xs text-white/60 mb-1">为什么？</div>
            <div class="text-sm text-white/90">{why_text}</div>
            <div class="text-xs text-white/50 mt-1">→ {answer_text}</div>
        </div>
        '''
    
    return f'''
    <div class="bg-white/5 backdrop-blur-sm rounded-xl p-4 border border-white/10">
        <div class="flex items-center justify-between mb-4">
            <h4 class="font-bold text-white flex items-center gap-2">
                <span>❓</span> {title}
            </h4>
            <span class="text-xs bg-indigo-500/20 text-indigo-400 px-2 py-1 rounded-full border border-indigo-500/30">
                5Why深度法
            </span>
        </div>
        
        <div class="space-y-0">
            {why_items}
        </div>
        
        {root_cause and f'''
        <div class="mt-4 pt-3 border-t border-white/10">
            <div class="text-xs text-white/50 mb-1">根本原因</div>
            <div class="text-sm font-semibold text-yellow-400">{root_cause}</div>
        </div>
        '''}
        
        {insight and f'''
        <div class="mt-2">
            <div class="text-xs text-white/50 mb-1">核心洞察</div>
            <div class="text-sm text-white/80">{insight}</div>
        </div>
        '''}
    </div>
    '''


def render_skill_analysis_summary(
    three_d_heat: Optional[Dict] = None,
    swot: Optional[Dict] = None,
    scenarios: Optional[List[Dict]] = None,
    industry_chain: Optional[Dict] = None,
    five_why: Optional[Dict] = None,
    compact: bool = False
) -> str:
    """综合渲染Skill分析结果（可选择需要的模块）
    
    Args:
        three_d_heat: 三维热度数据
        swot: SWOT分析数据
        scenarios: 情景推演数据
        industry_chain: 产业链分析数据
        five_why: 5Why分析数据
        compact: 是否为紧凑模式（用于在现有卡片中嵌入）
    """
    parts = []
    
    if three_d_heat:
        parts.append(render_three_d_heat(three_d_heat))
    
    if swot:
        parts.append(render_swot(swot))
    
    if scenarios:
        parts.append(render_scenarios(scenarios))
    
    if industry_chain:
        parts.append(render_industry_chain(industry_chain))
    
    if five_why:
        parts.append(render_five_why(five_why))
    
    if not parts:
        return ''
    
    if compact:
        return f'<div class="space-y-3 mt-3 pt-3 border-t border-white/10">{"".join(parts)}</div>'
    
    return f'<div class="space-y-4">{"".join(parts)}</div>'


