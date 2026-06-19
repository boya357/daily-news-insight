"""
修复版：个股分析列表页生成
"""
import sys
import os
import json
import glob

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'v3'))

from components.pro import GlassCard, SectionTitle
from generators.pro_base import ProGenerator


class StockAnalysisListGenerator(ProGenerator):
    """个股分析列表页生成器"""
    
    data_type = "stock_list"
    
    def __init__(self, data_dir: str = "data", docs_dir: str = "docs"):
        super().__init__(
            title="个股分析中心",
            active_page="工具",
            footer_text="投资研究中心 · 数据驱动决策",
            data_dir=data_dir,
            show_toc=False,
        )
        self.docs_dir = docs_dir
        self.stock_data = []
    
    def load_data(self):
        super().load_data()
        
        stock_list_path = os.path.join(self.docs_dir, 'data', 'stock_analysis', 'stock_list.json')
        if os.path.exists(stock_list_path):
            with open(stock_list_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                stocks_dict = data.get('stocks', {})
                for name, info in stocks_dict.items():
                    if isinstance(info, dict):
                        self.stock_data.append({
                            'name': name,
                            'code': info.get('code', ''),
                            'sector': info.get('sector', ''),
                            'rating': info.get('rating', ''),
                        })
                    else:
                        self.stock_data.append({
                            'name': name,
                            'code': info if isinstance(info, str) else '',
                            'sector': '',
                            'rating': '',
                        })
        
        # 补充已生成详情页的股票
        detail_pages = glob.glob(os.path.join(self.docs_dir, '个股分析', '*.html'))
        existing_names = [s['name'] for s in self.stock_data]
        
        for page in detail_pages:
            name = os.path.basename(page).replace('.html', '')
            if name not in existing_names and name != 'index':
                self.stock_data.append({
                    'name': name,
                    'code': self._get_stock_code(name),
                    'sector': '',
                    'rating': '已分析',
                })
        
        self.stock_data.sort(key=lambda x: x['name'])
    
    def _get_stock_code(self, name: str) -> str:
        json_files = glob.glob(os.path.join(self.docs_dir, 'data', 'stock_analysis', '*.json'))
        for f in json_files:
            try:
                with open(f, 'r', encoding='utf-8') as fp:
                    data = json.load(fp)
                    if data.get('name') == name:
                        return data.get('code', '')
            except:
                continue
        return ''
    
    def _content(self) -> str:
        stats_html = f'''
        <div class="grid grid-cols-3 gap-4 mb-8">
            <div class="glass-card rounded-xl p-6 text-center">
                <div class="text-4xl font-bold text-blue-400 mb-2">{len(self.stock_data)}</div>
                <div class="text-white/60">覆盖股票</div>
            </div>
            <div class="glass-card rounded-xl p-6 text-center">
                <div class="text-4xl font-bold text-green-400 mb-2">{sum(1 for s in self.stock_data if s.get('rating') in ['买入', '增持', '已分析'])}</div>
                <div class="text-white/60">已分析</div>
            </div>
            <div class="glass-card rounded-xl p-6 text-center">
                <div class="text-4xl font-bold text-purple-400 mb-2">5</div>
                <div class="text-white/60">分析维度</div>
            </div>
        </div>
        '''
        
        cards_html = ''
        for stock in self.stock_data:
            name = stock['name']
            code = stock.get('code', '')
            sector = stock.get('sector', '')
            rating = stock.get('rating', '')
            
            detail_page = os.path.join(self.docs_dir, '个股分析', f'{name}.html')
            has_detail = os.path.exists(detail_page)
            
            link = f'{name}.html' if has_detail else '#'
            opacity = '' if has_detail else 'opacity-50'
            
            rating_color = {
                '买入': 'bg-green-500/20 text-green-400',
                '增持': 'bg-emerald-500/20 text-emerald-400',
                '持有': 'bg-yellow-500/20 text-yellow-400',
                '减持': 'bg-orange-500/20 text-orange-400',
                '卖出': 'bg-red-500/20 text-red-400',
                '已分析': 'bg-blue-500/20 text-blue-400',
            }.get(rating, 'bg-white/10 text-white/60')
            
            cards_html += f'''
            <a href="{link}" class="glass-card rounded-xl p-5 {opacity} hover:border-blue-400/50 transition-all duration-300 group block">
                <div class="flex items-start justify-between mb-3">
                    <div>
                        <h3 class="text-white font-bold text-lg group-hover:text-blue-400 transition-colors">{name}</h3>
                        <p class="text-white/50 text-sm">{code}</p>
                    </div>
                    {f'<span class="text-xs px-2.5 py-1 rounded-full {rating_color} font-medium">{rating}</span>' if rating else ''}
                </div>
                {f'<p class="text-white/40 text-sm mt-1">{sector}</p>' if sector else ''}
                <div class="mt-4 flex items-center text-blue-400/70 text-sm group-hover:text-blue-400 font-medium">
                    <span>查看深度分析</span>
                    <svg class="w-4 h-4 ml-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path>
                    </svg>
                </div>
            </a>
            '''
        
        grid_html = f'''
        <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-5 gap-4">
            {cards_html}
        </div>
        '''
        
        return f'''
        <div class="mb-8">
            <h1 class="text-3xl font-bold text-white mb-2">个股分析中心</h1>
            <p class="text-white/60">基于技术面、资金面、基本面的三维立体分析，助您把握投资机会</p>
        </div>
        
        {stats_html}
        
        {SectionTitle("全部股票", "📈", "点击股票名称查看完整深度分析报告").render()}
        {grid_html}
        '''


def main():
    docs_dir = 'docs'
    
    print("📋 生成个股分析列表页...")
    gen = StockAnalysisListGenerator(docs_dir=docs_dir)
    
    output = os.path.join(docs_dir, '个股分析', 'index.html')
    result = gen.publish(output)
    
    if result['success']:
        print(f"✅ 列表页生成成功: {output}")
        print(f"   文件大小: {result['file_size']} bytes")
    else:
        print(f"❌ 生成失败: {result.get('errors', result.get('error'))}")


if __name__ == '__main__':
    main()
