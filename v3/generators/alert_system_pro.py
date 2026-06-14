"""
智能预警系统生成器 - Pro版
基于Pro组件库重构，深色玻璃态风格
"""
import sys
import os
import json
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from components.pro import (
    GlassCard, SectionTitle, TagBadge, 
    RiskBar, AlertSection
)
from generators.pro_base import ProGenerator


class AlertSystemProGenerator(ProGenerator):
    """智能预警系统 - Pro版生成器"""
    
    data_type = "alerts"
    
    def __init__(self, data_dir: str = "data"):
        super().__init__(
            title="智能预警系统",
            active_page="首页",
            footer_text="智能预警系统 · 实时监控风险机会",
            data_dir=data_dir,
            show_toc=True,
        )
    def load_data(self):
        """加载预警数据"""
        super().load_data()
        self.data = self.data_loader.get_data("alerts")
        self.risk_index = self.data.get('risk_index', 0)
        self.risk_level = self.data.get('risk_level', '中风险')
        self.risk_color = self.data.get('risk_color', 'yellow')
        self.suggested_position = self.data.get('suggested_position', '--')
        self.monitor_cards = self.data.get('monitor_cards', [])
        self.critical_alerts = self.data.get('critical_alerts', [])
        self.warning_alerts = self.data.get('warning_alerts', [])
        self.info_alerts = self.data.get('info_alerts', [])
        self.strategy = self.data.get('strategy', {})
    
    def _generate_risk_overview(self) -> str:
        """生成风险总览区域"""
        # 风险指数圆环
        risk_colors = {
            'green': ('#10b981', '#059669'),
            'yellow': ('#f59e0b', '#d97706'),
            'orange': ('#f97316', '#ea580c'),
            'red': ('#ef4444', '#dc2626'),
        }
        color1, color2 = risk_colors.get(self.risk_color, risk_colors['yellow'])
        
        # 计算圆环进度
        circumference = 2 * 3.14159 * 60
        offset = circumference * (1 - self.risk_index / 100)
        
        content = f'''
            <div class="flex flex-col md:flex-row items-center gap-8">
                <!-- 风险指数圆环 -->
                <div class="relative w-40 h-40 flex-shrink-0">
                    <svg class="w-40 h-40 transform -rotate-90">
                        <circle cx="80" cy="80" r="60" stroke="rgba(255,255,255,0.1)" stroke-width="8" fill="none"/>
                        <circle cx="80" cy="80" r="60" 
                                stroke="url(#riskGradient)" 
                                stroke-width="8" 
                                fill="none"
                                stroke-linecap="round"
                                stroke-dasharray="{circumference}"
                                stroke-dashoffset="{offset}"/>
                        <defs>
                            <linearGradient id="riskGradient" x1="0%" y1="0%" x2="100%" y2="100%">
                                <stop offset="0%" stop-color="{color1}"/>
                                <stop offset="100%" stop-color="{color2}"/>
                            </linearGradient>
                        </defs>
                    </svg>
                    <div class="absolute inset-0 flex flex-col items-center justify-center">
                        <div class="text-4xl font-black text-white">{self.risk_index}</div>
                        <div class="text-sm text-white/60">风险指数</div>
                    </div>
                </div>
                
                <!-- 风险详情 -->
                <div class="flex-1 text-center md:text-left">
                    <div class="inline-block px-6 py-2 bg-gradient-to-r from-yellow-500/20 to-orange-500/20 border border-yellow-500/30 text-yellow-400 rounded-full text-lg font-bold mb-4">
                        ⚠️ {self.risk_level}
                    </div>
                    
                    <div class="grid grid-cols-2 gap-4 mb-4">
                        <div class="bg-white/5 rounded-xl p-4 text-center">
                            <div class="text-2xl font-bold text-white">{self.suggested_position}</div>
                            <div class="text-sm text-white/60 mt-1">建议仓位</div>
                        </div>
                        <div class="bg-white/5 rounded-xl p-4 text-center">
                            <div class="text-2xl font-bold text-white">{len(self.critical_alerts) + len(self.warning_alerts)}</div>
                            <div class="text-sm text-white/60 mt-1">预警数</div>
                        </div>
                    </div>
                </div>
            </div>
        '''
        
        return GlassCard(content=content, padding="p-8", extra_class="mb-6").render()
    
    def _generate_monitor_cards(self) -> str:
        """生成监控维度卡片"""
        if not self.monitor_cards:
            return ''
        
        cards_html = ''
        for card in self.monitor_cards:
            title = card.get('title', '')
            icon = card.get('icon', '📊')
            score = card.get('score', 0)
            level = card.get('level', '')
            level_color = card.get('level_color', 'yellow')
            items = card.get('items', [])
            
            # 分数条颜色
            score_colors = {
                'green': 'from-green-500 to-emerald-500',
                'yellow': 'from-yellow-500 to-orange-500',
                'red': 'from-red-500 to-rose-600',
            }
            gradient = score_colors.get(level_color, score_colors['yellow'])
            
            items_html = ''
            for item in items[:3]:
                items_html += f'<div class="text-sm text-white/70 mb-1">• {item}</div>'
            
            cards_html += f'''
            <div class="bg-white/5 border border-white/10 rounded-xl p-5">
                <div class="flex items-center justify-between mb-3">
                    <div class="flex items-center gap-2">
                        <span class="text-2xl">{icon}</span>
                        <h3 class="text-white font-bold">{title}</h3>
                    </div>
                    <span class="px-2 py-1 bg-{level_color}-500/20 text-{level_color}-400 text-xs font-bold rounded-full">
                        {level}
                    </span>
                </div>
                
                <div class="mb-3">
                    <div class="flex justify-between text-sm text-white/60 mb-1">
                        <span>风险评分</span>
                        <span>{score}/100</span>
                    </div>
                    <div class="w-full h-2 bg-white/10 rounded-full overflow-hidden">
                        <div class="h-full bg-gradient-to-r {gradient} rounded-full" style="width: {score}%"></div>
                    </div>
                </div>
                
                <div class="space-y-1">
                    {items_html}
                </div>
            </div>
            '''
        
        content = f'''
            {SectionTitle(text='📊 多维度监控', icon='📊').render()}
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
                {cards_html}
            </div>
        '''
        
        return GlassCard(content=content, padding="p-6", extra_class="mb-6").render()
    
    def _generate_alerts_section(self, title: str, icon: str, alerts: list, level: str = "warning") -> str:
        """生成预警列表区域"""
        if not alerts:
            return ''
        
        alerts_html = ''
        for alert in alerts:
            alert_title = alert.get('title', '')
            time = alert.get('time', '')
            description = alert.get('description', '')
            suggestion = alert.get('suggestion', '')
            tags = alert.get('tags', [])
            
            tags_html = ''
            for tag in tags:
                tags_html += f'<span class="px-2 py-0.5 bg-white/10 text-white/60 text-xs rounded-full">{tag}</span>'
            
            suggestion_html = ''
            if suggestion:
                suggestion_html = f'''
                <div class="mt-2 p-2 bg-white/5 rounded-lg border-l-2 border-yellow-400">
                    <span class="text-xs text-yellow-400 font-medium">💡 建议：</span>
                    <span class="text-xs text-white/70">{suggestion}</span>
                </div>
                '''
            
            alerts_html += f'''
            <div class="p-4 bg-white/5 rounded-xl border border-white/10 mb-3 last:mb-0 hover:bg-white/10 transition-colors">
                <div class="flex items-start justify-between gap-4">
                    <div class="flex-1 min-w-0">
                        <h4 class="text-white font-semibold mb-1">{alert_title}</h4>
                        <p class="text-sm text-white/60 mb-2">{description}</p>
                        <div class="flex items-center gap-2 flex-wrap">
                            <span class="text-xs text-white/40">⏰ {time}</span>
                            {tags_html}
                        </div>
                        {suggestion_html}
                    </div>
                </div>
            </div>
            '''
        
        content = f'''
            {SectionTitle(text=f'{icon} {title}', icon=icon).render()}
            {alerts_html}
        '''
        
        return GlassCard(content=content, padding="p-6", extra_class="mb-6").render()
    
    def _generate_strategy_section(self) -> str:
        """生成应对策略区域"""
        strategy = self.strategy
        if not strategy:
            return ''
        
        immediate = strategy.get('immediate', [])
        watch = strategy.get('watch', [])
        hold = strategy.get('hold', [])
        
        def strategy_items(items, color):
            if not items:
                return '<p class="text-white/40 text-sm">暂无</p>'
            html = ''
            for item in items:
                html += f'<div class="flex items-start gap-2 mb-2 last:mb-0"><span class="text-{color}-400 mt-0.5">•</span><span class="text-sm text-white/80">{item}</span></div>'
            return html
        
        content = f'''
            {SectionTitle(text='🎯 应对策略', icon='🎯').render()}
            
            <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
                <div class="bg-red-500/10 border border-red-500/20 rounded-xl p-4">
                    <h3 class="text-red-400 font-bold mb-3 flex items-center gap-2">
                        <span>🔴</span> 立即行动
                    </h3>
                    {strategy_items(immediate, 'red')}
                </div>
                
                <div class="bg-yellow-500/10 border border-yellow-500/20 rounded-xl p-4">
                    <h3 class="text-yellow-400 font-bold mb-3 flex items-center gap-2">
                        <span>🟡</span> 密切关注
                    </h3>
                    {strategy_items(watch, 'yellow')}
                </div>
                
                <div class="bg-green-500/10 border border-green-500/20 rounded-xl p-4">
                    <h3 class="text-green-400 font-bold mb-3 flex items-center gap-2">
                        <span>🟢</span> 持有观望
                    </h3>
                    {strategy_items(hold, 'green')}
                </div>
            </div>
        '''
        
        return GlassCard(content=content, padding="p-6", extra_class="mb-6").render()
    
    def _content(self) -> str:
        """页面主要内容"""
        risk_overview = self._generate_risk_overview()
        monitor_cards = self._generate_monitor_cards()
        critical_section = self._generate_alerts_section(
            '紧急预警', '🚨', self.critical_alerts, 'danger'
        )
        warning_section = self._generate_alerts_section(
            '风险警告', '⚠️', self.warning_alerts, 'warning'
        )
        info_section = self._generate_alerts_section(
            '信息提示', 'ℹ️', self.info_alerts, 'safe'
        )
        strategy_section = self._generate_strategy_section()
        
        return f'''
            {risk_overview}
            {monitor_cards}
            {critical_section}
            {warning_section}
            {info_section}
            {strategy_section}
        '''
    
    def publish(self, output_path: str = None):
        """发布到生产路径"""
        if output_path is None:
            output_path = "docs/alerts/index_pro.html"
        return super().publish(output_path)


if __name__ == '__main__':
    generator = AlertSystemProGenerator()
    html = generator.generate()
    
    output_path = '/tmp/test_alert_system_pro.html'
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"✅ 生成完成")
    print(f"   输出文件: {output_path}")
    print(f"   文件大小: {len(html)} 字节")
    print(f"   风险指数: {generator.risk_index}")
    print(f"   监控维度: {len(generator.monitor_cards)} 个")
