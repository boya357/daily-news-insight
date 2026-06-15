"""
个股深度分析页面生成器
技术面 + 资金面 + 基本面 三维立体分析
"""
import sys
import os
import json
from pathlib import Path
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from components.pro import GlassCard, SectionTitle, get_pro_theme_css
from generators.pro_base import ProGenerator
from analyzers.stock_analyzer import StockAnalyzer, StockTechnicalAnalyzer


class StockAnalysisPageGenerator(ProGenerator):
    """个股深度分析页面生成器"""
    
    def __init__(self, stock_code, stock_name, data_dir: str = "data"):
        super().__init__(
            title=f"{stock_name} 深度分析",
            active_page="工具",
            footer_text="投资研究中心 · 数据驱动决策",
            data_dir=data_dir,
            show_toc=True,
        )
        self.stock_code = stock_code
        self.stock_name = stock_name
        self.analysis = None
    
    def load_data(self):
        """加载数据并进行分析"""
        super().load_data()
        
        # 获取K线数据（优先从文件加载，没有则生成模拟数据）
        prices = self._load_kline_data()
        
        # 进行分析
        analyzer = StockAnalyzer(self.stock_code, self.stock_name)
        analyzer.load_historical_data(prices)
        self.analysis = analyzer.analyze_all()
    
    def _load_kline_data(self):
        """加载K线数据"""
        # 尝试从数据文件加载
        kline_file = Path("data") / f"kline_{self.stock_code}.json"
        
        if kline_file.exists():
            with open(kline_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        
        # 没有数据文件则生成模拟数据
        return self._generate_mock_kline()
    
    def _generate_mock_kline(self):
        """生成模拟K线数据"""
        import random
        random.seed(hash(self.stock_code) % 10000)
        
        base_price = 50
        prices = []
        
        current = base_price
        for i in range(60):
            change = random.gauss(0, 0.025)
            open_price = current * (1 + random.uniform(-0.008, 0.008))
            high = max(open_price, current) * (1 + random.uniform(0, 0.04))
            low = min(open_price, current) * (1 - random.uniform(0, 0.04))
            close = current * (1 + change)
            volume = random.randint(800000, 8000000)
            
            prices.append({
                'date': f'2026-01-{i+1:02d}',
                'open': round(open_price, 2),
                'high': round(high, 2),
                'low': round(low, 2),
                'close': round(close, 2),
                'volume': volume,
            })
            
            current = close
        
        return prices
    
    def _render_stock_header(self) -> str:
        """渲染股票头部信息"""
        if not self.analysis or not self.analysis.get('technical'):
            return ''
        
        tech = self.analysis['technical']
        current_price = tech['support_resistance']['high_20']  # 临时用
        current_price = self.analysis['technical']['ma']['ma20'] or 50
        change = self.analysis.get('today_change', 0)
        change_pct = self.analysis.get('today_change_pct', 0)
        
        return f'''
        <div class="glass-card rounded-2xl p-6 mb-6">
            <div class="flex items-center justify-between mb-4">
                <div>
                    <h1 class="text-2xl font-bold text-white mb-1">{self.stock_name}</h1>
                    <span class="text-white/60 text-sm">{self.stock_code}</span>
                </div>
                <div class="text-right">
                    <div class="text-3xl font-bold text-white mb-1">{current_price:.2f}</div>
                    <div class="text-{'green-400' if change >= 0 else 'red-400'} text-sm">
                        {'+' if change >= 0 else ''}{change:.2f} ({'+' if change_pct >= 0 else ''}{change_pct:.2f}%)
                    </div>
                </div>
            </div>
            
            <div class="grid grid-cols-4 gap-4">
                <div class="text-center">
                    <div class="text-white/60 text-xs mb-1">综合评级</div>
                    <div class="text-lg font-bold text-{self._get_rating_color(self.analysis['overall']['score'])}">
                        {self.analysis['overall']['rating']}
                    </div>
                </div>
                <div class="text-center">
                    <div class="text-white/60 text-xs mb-1">综合评分</div>
                    <div class="text-lg font-bold text-white">{self.analysis['overall']['score']:.1f}</div>
                </div>
                <div class="text-center">
                    <div class="text-white/60 text-xs mb-1">技术面</div>
                    <div class="text-lg font-bold text-white">{tech['summary']['total_score']:.1f}</div>
                </div>
                <div class="text-center">
                    <div class="text-white/60 text-xs mb-1">基本面</div>
                    <div class="text-lg font-bold text-white">{self.analysis['fundamental']['score']:.1f}</div>
                </div>
            </div>
        </div>
        '''
    
    def _get_rating_color(self, score):
        if score >= 70:
            return 'green-400'
        elif score >= 55:
            return 'yellow-400'
        elif score >= 40:
            return 'orange-400'
        else:
            return 'red-400'
    
    def _render_technical_analysis(self) -> str:
        """渲染技术面分析"""
        if not self.analysis or not self.analysis.get('technical'):
            return ''
        
        tech = self.analysis['technical']
        summary = tech['summary']
        
        indicators = [
            ('均线系统', tech['ma']['trend'], tech['ma']['score'], f"MA5:{tech['ma']['ma5']:.2f} MA20:{tech['ma']['ma20']:.2f}" if tech['ma']['ma5'] else ''),
            ('MACD', tech['macd']['signal'], tech['macd']['score'], f"DIF:{tech['macd']['dif']:.2f} DEA:{tech['macd']['dea']:.2f}" if tech['macd']['dif'] else ''),
            ('RSI', tech['rsi']['signal'], tech['rsi']['score'], f"RSI(14):{tech['rsi']['rsi']:.1f}" if tech['rsi']['rsi'] else ''),
            ('KDJ', tech['kdj']['signal'], tech['kdj']['score'], f"K:{tech['kdj']['k']:.1f} D:{tech['kdj']['d']:.1f} J:{tech['kdj']['j']:.1f}" if tech['kdj']['k'] else ''),
            ('布林带', tech['boll']['signal'], tech['boll']['score'], f"位置:{tech['boll']['position']:.1f}%" if tech['boll']['position'] else ''),
            ('成交量', tech['volume']['signal'], tech['volume']['score'], f"量比:{tech['volume']['vol_ratio']:.2f}" if tech['volume']['vol_ratio'] else ''),
        ]
        
        indicators_html = ''
        for name, signal, score, detail in indicators:
            color = self._get_score_color(score)
            indicators_html += f'''
            <div class="glass-card rounded-xl p-4">
                <div class="flex items-center justify-between mb-2">
                    <span class="text-white font-medium">{name}</span>
                    <span class="text-{color} text-sm font-bold">{score:.0f}分</span>
                </div>
                <div class="text-white/70 text-sm mb-2">{signal}</div>
                <div class="w-full bg-white/10 rounded-full h-2">
                    <div class="bg-gradient-to-r from-{color}/50 to-{color} h-2 rounded-full transition-all duration-500" 
                         style="width: {min(100, max(0, score))}%"></div>
                </div>
                <div class="text-white/50 text-xs mt-2">{detail}</div>
            </div>
            '''
        
        return f'''
        <div class="mb-8">
            <h2 class="section-title">
                <span class="title-icon">📊</span>
                技术面分析
                <span class="text-sm font-normal text-white/60 ml-2">综合 {summary['total_score']:.1f}分 · {summary['rating']}</span>
            </h2>
            
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
                {indicators_html}
            </div>
        </div>
        '''
    
    def _get_score_color(self, score):
        if score >= 65:
            return 'green-400'
        elif score >= 50:
            return 'yellow-400'
        elif score >= 35:
            return 'orange-400'
        else:
            return 'red-400'
    
    def _render_support_resistance(self) -> str:
        """渲染支撑压力位分析"""
        if not self.analysis or not self.analysis.get('technical'):
            return ''
        
        sr = self.analysis['technical']['support_resistance']
        
        if not sr.get('support') or not sr.get('resistance'):
            return ''
        
        return f'''
        <div class="glass-card rounded-xl p-6 mb-6">
            <h3 class="text-lg font-bold text-white mb-4 flex items-center">
                <span class="text-xl mr-2">🎯</span>
                支撑压力位分析
            </h3>
            
            <div class="grid grid-cols-2 gap-6">
                <div class="text-center">
                    <div class="text-white/60 text-sm mb-1">压力位</div>
                    <div class="text-2xl font-bold text-red-400">{sr['resistance']:.2f}</div>
                    <div class="text-white/50 text-xs mt-1">距当前 +{sr['dist_to_resistance']:.2f}%</div>
                </div>
                <div class="text-center">
                    <div class="text-white/60 text-sm mb-1">支撑位</div>
                    <div class="text-2xl font-bold text-green-400">{sr['support']:.2f}</div>
                    <div class="text-white/50 text-xs mt-1">距当前 {sr['dist_to_support']:.2f}%</div>
                </div>
            </div>
            
            <div class="mt-4 p-3 bg-white/5 rounded-xl">
                <div class="text-white/60 text-xs mb-2">20日波动区间</div>
                <div class="flex justify-between text-sm">
                    <span class="text-red-400">最高 {sr['high_20']:.2f}</span>
                    <span class="text-green-400">最低 {sr['low_20']:.2f}</span>
                </div>
            </div>
        </div>
        '''
    
    def _render_overall_score(self) -> str:
        """渲染综合评分"""
        if not self.analysis:
            return ''
        
        overall = self.analysis['overall']
        score = overall['score']
        
        # 计算圆环角度
        angle = (score / 100) * 360
        
        return f'''
        <div class="glass-card rounded-xl p-6 mb-6">
            <h3 class="text-lg font-bold text-white mb-4 flex items-center">
                <span class="text-xl mr-2">🏆</span>
                综合评级
            </h3>
            
            <div class="flex items-center justify-center mb-4">
                <div class="relative w-32 h-32">
                    <svg class="w-full h-full transform -rotate-90">
                        <circle cx="64" cy="64" r="56" stroke="rgba(255,255,255,0.1)" stroke-width="8" fill="none"/>
                        <circle cx="64" cy="64" r="56" stroke="url(#gradient)" stroke-width="8" fill="none"
                                stroke-dasharray="{angle * 3.9} 360" stroke-linecap="round"
                                class="transition-all duration-1000"/>
                        <defs>
                            <linearGradient id="gradient" x1="0%" y1="0%" x2="100%" y2="0%">
                                <stop offset="0%" stop-color="#667eea"/>
                                <stop offset="100%" stop-color="#f093fb"/>
                            </linearGradient>
                        </defs>
                    </svg>
                    <div class="absolute inset-0 flex flex-col items-center justify-center">
                        <span class="text-3xl font-bold text-white">{score:.1f}</span>
                        <span class="text-xs text-white/60">综合评分</span>
                    </div>
                </div>
            </div>
            
            <div class="text-center">
                <span class="inline-block px-4 py-2 rounded-full bg-gradient-to-r from-purple-500/30 to-pink-500/30 text-white font-bold">
                    {overall['rating']}
                </span>
            </div>
            
            <div class="mt-6 space-y-3">
                <div class="flex items-center justify-between text-sm">
                    <span class="text-white/60">技术面权重</span>
                    <span class="text-white">{overall['weights']['technical']}%</span>
                </div>
                <div class="flex items-center justify-between text-sm">
                    <span class="text-white/60">基本面权重</span>
                    <span class="text-white">{overall['weights']['fundamental']}%</span>
                </div>
            </div>
        </div>
        '''
    
    def _content(self) -> str:
        """页面主内容"""
        try:
            self.load_data()
        except Exception as e:
            return f'<div class="glass-card p-6 text-white">数据加载失败: {e}</div>'
        
        return f'''
        <div class="max-w-6xl mx-auto px-4 py-8">
            {self._render_stock_header()}
            
            <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
                <div class="lg:col-span-2">
                    {self._render_technical_analysis()}
                </div>
                <div class="lg:col-span-1">
                    {self._render_overall_score()}
                    {self._render_support_resistance()}
                </div>
            </div>
        </div>
        '''
    
    def generate(self) -> str:
        """生成完整页面"""
        return self.render()
    
    def save(self, filepath: str) -> str:
        """保存到文件"""
        html = self.generate()
        Path(filepath).parent.mkdir(parents=True, exist_ok=True)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
        return filepath


def generate_stock_analysis_page(code, name, output_path, data_dir="data"):
    """生成个股分析页面"""
    gen = StockAnalysisPageGenerator(code, name, data_dir)
    return gen.save(output_path)


if __name__ == '__main__':
    output = generate_stock_analysis_page('002837', '英维克', 'docs/个股分析/英维克.html')
    print(f"页面已生成: {output}")
