"""
题材健康度报告生成器 - Pro版
基于Pro组件库重构，深色玻璃态风格
"""
import sys
import os
import json
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from components.pro import (
    GlassCard, SectionTitle, TagBadge, RiskBar
)
from generators.pro_base import ProGenerator


class TopicHealthProGenerator(ProGenerator):
    data_type = "topics"

    """题材健康度报告 - Pro版生成器"""
    
    def __init__(self, data_dir: str = "data"):
        super().__init__(
            title="题材健康度报告",
            active_page="日报",
            footer_text="题材健康度 · 多维度评估投资价值",
            data_dir=data_dir,
            show_toc=True,
        )

    def load_data(self):
        """加载题材数据"""
        super().load_data()
        self.data = self.data_loader.get_data("topics")
        
        self.s_topics = self.data.get('s_level_topics', [])
        self.a_topics = self.data.get('a_level_topics', [])
        self.b_topics = self.data.get('b_level_topics', [])
        self.all_topics = self.s_topics + self.a_topics + self.b_topics
        
        # 按健康度排序
        self.sorted_topics = sorted(
            self.all_topics,
            key=lambda x: x.get('health_score', 0),
            reverse=True
        )
        
        # 计算统计数据
        self.health_scores = [t.get('health_score', 0) for t in self.all_topics]
        self.avg_health = sum(self.health_scores) / len(self.health_scores) if self.health_scores else 0
        self.max_health = max(self.health_scores) if self.health_scores else 0
        self.min_health = min(self.health_scores) if self.health_scores else 0
        
        # 维度名称映射
        self.dim_names = {
            'policy': '政策支持',
            'industry': '产业景气',
            'capital': '资金热度',
            'sentiment': '市场情绪',
            'valuation': '估值水平',
            'catalyst': '催化强度'
        }
    
    def _get_health_level(self, score: float) -> tuple:
        """获取健康度等级和颜色"""
        if score >= 90:
            return '极佳', 'text-green-400', 'from-green-500/20 to-emerald-500/20', 'border-green-500/30'
        elif score >= 80:
            return '良好', 'text-blue-400', 'from-blue-500/20 to-cyan-500/20', 'border-blue-500/30'
        elif score >= 70:
            return '一般', 'text-yellow-400', 'from-yellow-500/20 to-orange-500/20', 'border-yellow-500/30'
        elif score >= 60:
            return '偏弱', 'text-orange-400', 'from-orange-500/20 to-red-500/20', 'border-orange-500/30'
        else:
            return '危险', 'text-red-400', 'from-red-500/20 to-rose-500/20', 'border-red-500/30'
    
    def _generate_overview(self) -> str:
        """生成健康度总览区域"""
        avg_level, avg_color, _, _ = self._get_health_level(self.avg_health)
        
        # 评级分布
        s_count = len(self.s_topics)
        a_count = len(self.a_topics)
        b_count = len(self.b_topics)
        
        content = f'''
            {SectionTitle(text='📊 健康度总览', icon='📊').render()}
            
            <!-- 核心指标 -->
            <div class="grid grid-cols-2 md:grid-cols-4 gap-4 mb-6">
                <div class="text-center p-4 bg-white/5 rounded-xl">
                    <div class="text-3xl font-black text-white">{len(self.all_topics)}</div>
                    <div class="text-sm text-white/50 mt-1">跟踪题材</div>
                </div>
                <div class="text-center p-4 bg-white/5 rounded-xl">
                    <div class="text-3xl font-black {avg_color}">{self.avg_health:.1f}</div>
                    <div class="text-sm text-white/50 mt-1">平均健康度</div>
                </div>
                <div class="text-center p-4 bg-white/5 rounded-xl">
                    <div class="text-3xl font-black text-green-400">{self.max_health}</div>
                    <div class="text-sm text-white/50 mt-1">最高健康度</div>
                </div>
                <div class="text-center p-4 bg-white/5 rounded-xl">
                    <div class="text-3xl font-black text-red-400">{self.min_health}</div>
                    <div class="text-sm text-white/50 mt-1">最低健康度</div>
                </div>
            </div>
            
            <!-- 评级分布 -->
            <div class="bg-white/5 rounded-xl p-5">
                <div class="text-white/70 text-sm mb-3">评级分布</div>
                <div class="flex items-center gap-4">
                    <div class="flex-1 h-3 bg-gray-700 rounded-full overflow-hidden flex">
                        <div class="bg-gradient-to-r from-purple-500 to-pink-500 h-full" style="width: {s_count/len(self.all_topics)*100}%"></div>
                        <div class="bg-gradient-to-r from-blue-500 to-cyan-500 h-full" style="width: {a_count/len(self.all_topics)*100}%"></div>
                        <div class="bg-gradient-to-r from-gray-500 to-gray-400 h-full" style="width: {b_count/len(self.all_topics)*100}%"></div>
                    </div>
                </div>
                <div class="flex justify-between mt-2 text-xs">
                    <span class="text-purple-400">S级 · {s_count}个</span>
                    <span class="text-blue-400">A级 · {a_count}个</span>
                    <span class="text-gray-400">B级 · {b_count}个</span>
                </div>
            </div>
        '''
        
        return GlassCard(content=content, padding="p-6", extra_class="mb-6").render()
    
    def _generate_health_ranking(self) -> str:
        """生成健康度排行榜"""
        items_html = ''
        
        for i, topic in enumerate(self.sorted_topics):
            name = topic.get('name', '')
            score = topic.get('health_score', 0)
            level = topic.get('level', '')
            level_text, color_class, bg_class, border_class = self._get_health_level(score)
            
            # 前三名特殊样式
            if i == 0:
                rank_icon = '🥇'
            elif i == 1:
                rank_icon = '🥈'
            elif i == 2:
                rank_icon = '🥉'
            else:
                rank_icon = f'<span class="text-white/40 font-bold">{i+1}</span>'
            
            # 趋势
            trend = topic.get('health_trend', 'stable')
            if trend == 'up':
                trend_icon = '<span class="text-green-400">↑</span>'
            elif trend == 'down':
                trend_icon = '<span class="text-red-400">↓</span>'
            else:
                trend_icon = '<span class="text-white/30">—</span>'
            
            items_html += f'''
            <div class="flex items-center gap-4 p-3 rounded-xl hover:bg-white/5 transition-colors">
                <div class="w-8 text-center text-lg">{rank_icon}</div>
                <div class="flex-1">
                    <div class="flex items-center gap-2">
                        <span class="text-white font-medium">{name}</span>
                        <span class="text-xs px-2 py-0.5 rounded-full {bg_class} {color_class} border {border_class}">
                            {level}级
                        </span>
                    </div>
                    <div class="flex items-center gap-2 mt-1">
                        <div class="flex-1 h-1.5 bg-white/10 rounded-full overflow-hidden">
                            <div class="h-full bg-gradient-to-r from-blue-500 to-purple-500 rounded-full" 
                                 style="width: {score}%;"></div>
                        </div>
                        <span class="text-xs text-white/50 w-10 text-right">{score}分</span>
                    </div>
                </div>
                <div class="text-lg">{trend_icon}</div>
            </div>
            '''
        
        content = f'''
            {SectionTitle(text='🏆 健康度排行榜', icon='🏆').render()}
            <div class="space-y-1">
                {items_html}
            </div>
        '''
        
        return GlassCard(content=content, padding="p-6", extra_class="mb-6").render()
    
    def _generate_topic_detail_card(self, topic: dict, rank: int) -> str:
        """生成单个题材的详细健康度卡片"""
        name = topic.get('name', '')
        score = topic.get('health_score', 0)
        level = topic.get('level', '')
        icon = topic.get('icon', '📈')
        last_eval = topic.get('last_evaluation', '')
        core_logic = topic.get('core_logic', '')
        
        level_text, color_class, bg_class, border_class = self._get_health_level(score)
        
        # 维度得分
        dim_scores = topic.get('dimension_scores', {})
        dim_bars = ''
        for dim_key, dim_name in self.dim_names.items():
            dim_score = dim_scores.get(dim_key, 0)
            dim_bars += f'''
            <div class="flex items-center gap-3 py-1.5">
                <span class="text-white/60 text-sm w-20">{dim_name}</span>
                <div class="flex-1 h-2 bg-white/10 rounded-full overflow-hidden">
                    <div class="h-full bg-gradient-to-r from-blue-500 to-purple-500 rounded-full transition-all" 
                         style="width: {dim_score}%;"></div>
                </div>
                <span class="text-white/80 text-sm font-medium w-12 text-right">{dim_score}</span>
            </div>
            '''
        
        # 其他指标
        prosperity = topic.get('prosperity_score', 0)
        prosperity_trend = topic.get('prosperity_trend', 'stable')
        fund_flow = topic.get('fund_flow', '')
        policy_support = topic.get('policy_support', '')
        
        trend_map = {'up': ('↑', 'text-green-400'), 'down': ('↓', 'text-red-400'), 'stable': ('—', 'text-white/40')}
        trend_icon, trend_color = trend_map.get(prosperity_trend, ('—', 'text-white/40'))
        
        content = f'''
            <div class="bg-gradient-to-br {bg_class} border {border_class} rounded-2xl p-6">
                <!-- 头部 -->
                <div class="flex items-start justify-between mb-4">
                    <div class="flex items-center gap-3">
                        <div class="w-12 h-12 rounded-xl bg-white/10 flex items-center justify-center text-2xl">
                            {icon}
                        </div>
                        <div>
                            <div class="flex items-center gap-2">
                                <h3 class="text-xl font-bold text-white">{name}</h3>
                                <span class="text-xs px-2 py-0.5 rounded-full bg-white/10 text-white/70">
                                    {level}级题材
                                </span>
                            </div>
                            <p class="text-white/50 text-sm mt-1 line-clamp-1">{core_logic}</p>
                        </div>
                    </div>
                    <div class="text-right">
                        <div class="text-3xl font-black {color_class}">{score}</div>
                        <div class="text-xs text-white/50">健康度评分</div>
                    </div>
                </div>
                
                <!-- 维度得分 -->
                <div class="mb-4">
                    <div class="text-white/70 text-sm mb-2">六维评估</div>
                    {dim_bars}
                </div>
                
                <!-- 辅助指标 -->
                <div class="grid grid-cols-3 gap-3 pt-4 border-t border-white/10">
                    <div class="text-center">
                        <div class="text-white font-bold">{prosperity} <span class="{trend_color} text-sm">{trend_icon}</span></div>
                        <div class="text-xs text-white/50 mt-0.5">景气度</div>
                    </div>
                    <div class="text-center">
                        <div class="text-white/80 font-medium text-sm">{fund_flow}</div>
                        <div class="text-xs text-white/50 mt-0.5">资金流向</div>
                    </div>
                    <div class="text-center">
                        <div class="text-white/80 font-medium text-sm">{policy_support}</div>
                        <div class="text-xs text-white/50 mt-0.5">政策支持</div>
                    </div>
                </div>
                
                <!-- 评估时间 -->
                <div class="mt-4 pt-3 border-t border-white/10 text-xs text-white/40 text-center">
                    上次评估: {last_eval}
                </div>
            </div>
        '''
        
        return content
    
    def _generate_detailed_analysis(self) -> str:
        """生成详细分析区域"""
        cards_html = ''
        for i, topic in enumerate(self.sorted_topics):
            cards_html += self._generate_topic_detail_card(topic, i+1)
        
        content = f'''
            {SectionTitle(text='📋 题材健康度详评', icon='📋').render()}
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                {cards_html}
            </div>
        '''
        
        return GlassCard(content=content, padding="p-6", extra_class="mb-6").render()
    
    def _generate_risk_opportunity(self) -> str:
        """生成风险与机会提示"""
        # 降级风险
        downgrade_candidates = [t for t in self.all_topics if t.get('downgrade_candidates') or t.get('health_trend') == 'down']
        
        # 升级机会
        upgrade_candidates = [t for t in self.all_topics if t.get('upgrade_candidates') or t.get('health_trend') == 'up']
        
        # 高风险（健康度低于60）
        high_risk = [t for t in self.all_topics if t.get('health_score', 100) < 60]
        
        risk_html = ''
        for topic in high_risk + downgrade_candidates[:3]:
            name = topic.get('name', '')
            score = topic.get('health_score', 0)
            reasons = topic.get('downgrade_candidates', [])
            reason_text = '、'.join(reasons[:2]) if reasons else '健康度持续走低'
            
            risk_html += f'''
            <div class="flex items-start gap-3 p-3 rounded-xl bg-red-500/10 border border-red-500/20">
                <span class="text-red-400 text-lg">⚠️</span>
                <div>
                    <div class="text-white font-medium">{name}</div>
                    <div class="text-red-300/70 text-sm mt-0.5">{reason_text}</div>
                    <div class="text-red-400/60 text-xs mt-1">健康度: {score}分</div>
                </div>
            </div>
            '''
        
        if not risk_html:
            risk_html = '<div class="text-center text-white/40 py-4">当前暂无高风险题材</div>'
        
        opp_html = ''
        for topic in upgrade_candidates[:5]:
            name = topic.get('name', '')
            score = topic.get('health_score', 0)
            reasons = topic.get('upgrade_candidates', [])
            reason_text = '、'.join(reasons[:2]) if reasons else '景气度持续上行'
            
            opp_html += f'''
            <div class="flex items-start gap-3 p-3 rounded-xl bg-green-500/10 border border-green-500/20">
                <span class="text-green-400 text-lg">✨</span>
                <div>
                    <div class="text-white font-medium">{name}</div>
                    <div class="text-green-300/70 text-sm mt-0.5">{reason_text}</div>
                    <div class="text-green-400/60 text-xs mt-1">健康度: {score}分</div>
                </div>
            </div>
            '''
        
        if not opp_html:
            opp_html = '<div class="text-center text-white/40 py-4">当前暂无明确升级机会</div>'
        
        content = f'''
            {SectionTitle(text='🎯 风险与机会提示', icon='🎯').render()}
            
            <div class="grid md:grid-cols-2 gap-6">
                <div>
                    <div class="flex items-center gap-2 mb-3">
                        <span class="text-red-400">⚠️</span>
                        <span class="text-white font-medium">风险提示</span>
                    </div>
                    <div class="space-y-2">
                        {risk_html}
                    </div>
                </div>
                
                <div>
                    <div class="flex items-center gap-2 mb-3">
                        <span class="text-green-400">✨</span>
                        <span class="text-white font-medium">机会提示</span>
                    </div>
                    <div class="space-y-2">
                        {opp_html}
                    </div>
                </div>
            </div>
        '''
        
        return GlassCard(content=content, padding="p-6", extra_class="mb-6").render()
    
    def _generate_dimension_analysis(self) -> str:
        """生成维度分析区域"""
        # 计算各维度平均分
        dim_avgs = {}
        for dim_key in self.dim_names:
            scores = [t.get('dimension_scores', {}).get(dim_key, 0) for t in self.all_topics]
            dim_avgs[dim_key] = sum(scores) / len(scores) if scores else 0
        
        # 按分数排序
        sorted_dims = sorted(dim_avgs.items(), key=lambda x: x[1], reverse=True)
        
        dim_items = ''
        for dim_key, avg_score in sorted_dims:
            dim_name = self.dim_names.get(dim_key, dim_key)
            level_text, color_class, _, _ = self._get_health_level(avg_score)
            
            dim_items += f'''
            <div class="flex items-center gap-4 p-3 rounded-xl bg-white/5">
                <span class="text-white/70 w-20">{dim_name}</span>
                <div class="flex-1 h-2 bg-white/10 rounded-full overflow-hidden">
                    <div class="h-full bg-gradient-to-r from-indigo-500 to-purple-500 rounded-full" 
                         style="width: {avg_score}%;"></div>
                </div>
                <span class="{color_class} font-bold w-16 text-right">{avg_score:.1f}</span>
            </div>
            '''
        
        # 找出最强和最弱维度
        strongest = sorted_dims[0] if sorted_dims else ('', 0)
        weakest = sorted_dims[-1] if sorted_dims else ('', 0)
        
        content = f'''
            {SectionTitle(text='📐 维度分析', icon='📐').render()}
            
            <div class="grid md:grid-cols-2 gap-4 mb-4">
                <div class="p-4 bg-green-500/10 border border-green-500/20 rounded-xl">
                    <div class="text-green-400 text-sm mb-1">最强维度</div>
                    <div class="text-white font-bold text-lg">{self.dim_names.get(strongest[0], strongest[0])}</div>
                    <div class="text-green-300/70 text-sm">平均 {strongest[1]:.1f} 分</div>
                </div>
                <div class="p-4 bg-red-500/10 border border-red-500/20 rounded-xl">
                    <div class="text-red-400 text-sm mb-1">最弱维度</div>
                    <div class="text-white font-bold text-lg">{self.dim_names.get(weakest[0], weakest[0])}</div>
                    <div class="text-red-300/70 text-sm">平均 {weakest[1]:.1f} 分</div>
                </div>
            </div>
            
            <div class="space-y-1">
                {dim_items}
            </div>
        '''
        
        return GlassCard(content=content, padding="p-6", extra_class="mb-6").render()
    
    def _content(self) -> str:
        """页面主要内容"""
        overview = self._generate_overview()
        ranking = self._generate_health_ranking()
        detailed = self._generate_detailed_analysis()
        dimension = self._generate_dimension_analysis()
        risk_opp = self._generate_risk_opportunity()
        
        return f'''
            {overview}
            {ranking}
            {detailed}
            {dimension}
            {risk_opp}
        '''
    
    def publish(self, output_path: str = "docs/题材健康度报告/index_pro.html"):
        """发布到生产路径"""
        return super().publish(output_path)


if __name__ == '__main__':
    generator = TopicHealthProGenerator()
    html = generator.render()
    
    output_path = '/tmp/test_topic_health_pro.html'
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"✅ 生成完成")
    print(f"   输出文件: {output_path}")
    print(f"   文件大小: {len(html)} 字节")
    print(f"   跟踪题材: {len(generator.all_topics)} 个")
    print(f"   平均健康度: {generator.avg_health:.1f}")
