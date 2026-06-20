"""
统一股票数据管理器
- 统一管理所有股票的分析数据
- 解决JSON数据与V2页面数据不一致的问题
- 提供股票发现、数据生成、页面生成的全链路能力
"""

import os
import sys
import json
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Optional, Set

_current_dir = Path(__file__).resolve().parent
sys.path.insert(0, str(_current_dir.parent))

from analyzers.stock_analyzer import StockAnalyzer
from generators.stock_detail_unified_v3 import generate_stock_detail


class UnifiedStockManager:
    """统一股票数据管理器"""
    
    def __init__(self, docs_dir: str = None):
        if docs_dir:
            self.docs_dir = Path(docs_dir)
        else:
            self.docs_dir = Path(__file__).resolve().parent.parent.parent / 'docs'
        
        self.data_dir = self.docs_dir / 'data' / 'stock_analysis'
        self.pages_dir = self.docs_dir / '个股分析'
        self.list_file = self.data_dir / 'stock_list.json'
        
        self.data_dir.mkdir(parents=True, exist_ok=True)
        self.pages_dir.mkdir(parents=True, exist_ok=True)
    
    def load_stock_list(self) -> Dict:
        """加载股票列表"""
        if self.list_file.exists():
            with open(self.list_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {'stocks': {}, 'total': 0, 'update_time': ''}
    
    def save_stock_list(self, data: Dict):
        """保存股票列表"""
        data['total'] = len(data.get('stocks', {}))
        data['update_time'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with open(self.list_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    
    def get_stock_info(self, stock_name: str) -> Optional[Dict]:
        """获取股票信息"""
        data = self.load_stock_list()
        return data['stocks'].get(stock_name)
    
    def has_stock(self, stock_name: str) -> bool:
        """检查股票是否在列表中"""
        data = self.load_stock_list()
        return stock_name in data['stocks']
    
    def has_detail_page(self, stock_name: str) -> bool:
        """检查是否有详情页"""
        return (self.pages_dir / f'{stock_name}.html').exists()
    
    def has_analysis_data(self, stock_code: str) -> bool:
        """检查是否有分析数据"""
        return (self.data_dir / f'{stock_code}.json').exists()
    
    def discover_stocks(self, stock_names: List[str], 
                       stock_codes: Dict[str, str] = None,
                       sectors: Dict[str, str] = None) -> int:
        """发现新股票并添加到列表（Level 1 覆盖）
        
        Args:
            stock_names: 股票名称列表
            stock_codes: 股票名称到代码的映射
            sectors: 股票名称到板块的映射
            
        Returns:
            新增的股票数量
        """
        data = self.load_stock_list()
        existing = set(data['stocks'].keys())
        new_stocks = set(stock_names) - existing
        
        for name in new_stocks:
            code = ''
            sector = ''
            if stock_codes and name in stock_codes:
                code = stock_codes[name]
            if sectors and name in sectors:
                sector = sectors[name]
            
            data['stocks'][name] = {
                'code': code,
                'sector': sector,
                'rating': '待分析',
                'data_level': 1  # 1=仅名称, 2=有基础数据, 3=有完整V2分析
            }
        
        if new_stocks:
            self.save_stock_list(data)
            print(f"✅ 发现 {len(new_stocks)} 只新股票，已添加到股票池")
        
        return len(new_stocks)
    
    def generate_analysis_data(self, stock_code: str, stock_name: str) -> Optional[Dict]:
        """生成股票分析数据（Level 2 覆盖）
        
        使用StockAnalyzer生成完整分析数据并保存为JSON
        """
        try:
            analyzer = StockAnalyzer(stock_code, stock_name)
            
            # 尝试加载K线数据
            kline_file = self.data_dir / f'kline_{stock_code}.json'
            if kline_file.exists():
                with open(kline_file, 'r', encoding='utf-8') as f:
                    prices = json.load(f)
                analyzer.load_historical_data(prices)
            else:
                # 没有K线时使用模拟数据（后续可接入真实行情）
                pass
            
            analysis = analyzer.analyze_all()
            
            # 保存分析数据
            output_file = self.data_dir / f'{stock_code}.json'
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(analysis, f, ensure_ascii=False, indent=2)
            
            # 更新股票列表
            data = self.load_stock_list()
            if stock_name in data['stocks']:
                data['stocks'][stock_name].update({
                    'rating': analysis.get('overall', {}).get('rating', ''),
                    'score': analysis.get('overall', {}).get('score', 0),
                    'data_level': 2,
                    'analyze_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                })
                self.save_stock_list(data)
            
            print(f"  ✅ {stock_name} ({stock_code}) 分析数据生成完成")
            return analysis
            
        except Exception as e:
            print(f"  ❌ {stock_name} 分析数据生成失败: {e}")
            return None
    
    def generate_detail_page(self, stock_code: str, stock_name: str) -> bool:
        """生成个股分析详情页（Level 3 覆盖）"""
        try:
            output_path = str(self.pages_dir / f'{stock_name}.html')
            html = generate_stock_detail(stock_code, stock_name, str(self.data_dir), str(self.pages_dir))
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(html)
            
            # 更新股票列表
            data = self.load_stock_list()
            if stock_name in data['stocks']:
                data['stocks'][stock_name]['data_level'] = 3
                self.save_stock_list(data)
            
            return True
        except Exception as e:
            print(f"  ❌ {stock_name} 详情页生成失败: {e}")
            return False
    
    def full_process_stock(self, stock_name: str, stock_code: str, 
                          sector: str = '') -> bool:
        """完整处理一只股票：发现→数据→页面
        
        Returns:
            是否成功生成详情页
        """
        # Level 1: 添加到列表
        self.discover_stocks([stock_name], {stock_name: stock_code}, {stock_name: sector})
        
        # Level 2: 生成分析数据
        analysis = self.generate_analysis_data(stock_code, stock_name)
        if not analysis:
            return False
        
        # Level 3: 生成详情页
        return self.generate_detail_page(stock_code, stock_name)
    
    def batch_process(self, stock_names: List[str] = None, 
                     level: int = 3) -> Dict:
        """批量处理股票
        
        Args:
            stock_names: 股票名称列表，None表示处理所有已发现的股票
            level: 处理级别 (1=仅发现, 2=生成数据, 3=生成页面)
            
        Returns:
            处理结果统计
        """
        data = self.load_stock_list()
        
        if stock_names is None:
            stock_names = list(data['stocks'].keys())
        
        stats = {
            'total': len(stock_names),
            'discovered': 0,
            'data_generated': 0,
            'page_generated': 0,
            'failed': 0
        }
        
        for i, name in enumerate(stock_names):
            info = data['stocks'].get(name, {})
            code = info.get('code', '')
            sector = info.get('sector', '')
            
            if not code:
                print(f"⚠️  {name} 没有股票代码，跳过")
                stats['failed'] += 1
                continue
            
            current_level = info.get('data_level', 1)
            
            try:
                if level >= 2 and current_level < 2:
                    self.generate_analysis_data(code, name)
                    stats['data_generated'] += 1
                
                if level >= 3 and current_level < 3:
                    self.generate_detail_page(code, name)
                    stats['page_generated'] += 1
                
            except Exception as e:
                print(f"❌ 处理 {name} 失败: {e}")
                stats['failed'] += 1
        
        print(f"\n📊 批量处理完成:")
        print(f"   总数: {stats['total']}")
        print(f"   新增数据: {stats['data_generated']}")
        print(f"   新增页面: {stats['page_generated']}")
        print(f"   失败: {stats['failed']}")
        
        return stats
    
    def get_coverage_stats(self) -> Dict:
        """获取覆盖统计"""
        data = self.load_stock_list()
        stocks = data['stocks']
        
        total = len(stocks)
        level1 = total  # 所有在列表里的都是Level 1
        level2 = sum(1 for s in stocks.values() if s.get('data_level', 1) >= 2)
        level3 = sum(1 for s in stocks.values() if s.get('data_level', 1) >= 3)
        
        return {
            'total': total,
            'level1': level1,
            'level2': level2,
            'level3': level3,
            'level1_pct': '100%',
            'level2_pct': f'{level2/total*100:.1f}%' if total else '0%',
            'level3_pct': f'{level3/total*100:.1f}%' if total else '0%',
        }


# 单例

    def generate_list_page(self, output_path: str = None) -> str:
        """生成个股分析列表页

        Args:
            output_path: 输出路径，默认为 docs/个股分析/index.html

        Returns:
            生成的HTML内容
        """
        data = self.load_stock_list()
        stocks = data.get('stocks', {})

        # 准备股票数据
        stock_data = []
        for name, info in stocks.items():
            if isinstance(info, dict):
                stock_data.append({
                    'name': name,
                    'code': info.get('code', ''),
                    'sector': info.get('sector', ''),
                    'rating': info.get('rating', ''),
                    'data_level': info.get('data_level', 1),
                })
            else:
                stock_data.append({
                    'name': name,
                    'code': info if isinstance(info, str) else '',
                    'sector': '',
                    'rating': '',
                    'data_level': 1,
                })

        # 按名称排序
        stock_data.sort(key=lambda x: x['name'])

        # 统计数据
        total = len(stock_data)
        buy_rated = sum(1 for s in stock_data if s.get('rating') in ['买入', '增持'])
        has_page = sum(1 for s in stock_data if s.get('data_level', 1) >= 3)

        # 生成股票卡片HTML
        cards_html = ''
        for stock in stock_data:
            name = stock['name']
            code = stock.get('code', '')
            sector = stock.get('sector', '')
            rating = stock.get('rating', '')
            has_detail = stock.get('data_level', 1) >= 3

            link = name + '.html' if has_detail else '#'
            cursor_class = 'cursor-pointer' if has_detail else 'cursor-not-allowed opacity-60'

            rating_colors = {
                '买入': 'text-green-400',
                '增持': 'text-emerald-400',
                '持有': 'text-yellow-400',
                '减持': 'text-orange-400',
                '卖出': 'text-red-400',
                '已分析': 'text-blue-400',
            }
            rating_color = rating_colors.get(rating, 'text-white/60')

            rating_bgs = {
                '买入': 'bg-green-500/20',
                '增持': 'bg-emerald-500/20',
                '持有': 'bg-yellow-500/20',
                '减持': 'bg-orange-500/20',
                '卖出': 'bg-red-500/20',
                '已分析': 'bg-blue-500/20',
            }
            rating_bg = rating_bgs.get(rating, 'bg-white/10')

            rating_span = ''
            if rating:
                rating_span = '<span class="text-xs px-2 py-1 rounded-full ' + rating_bg + ' ' + rating_color + '">' + rating + '</span>'

            sector_p = ''
            if sector:
                sector_p = '<p class="text-white/40 text-xs mt-2">' + sector + '</p>'

            card = '<a href="' + link + '" class="glass-card rounded-xl p-4 ' + cursor_class + ' hover:border-blue-400/50 transition-all duration-300 group block">'
            card += '<div class="flex items-start justify-between mb-2">'
            card += '<div>'
            card += '<h3 class="text-white font-bold text-lg group-hover:text-blue-400 transition-colors">' + name + '</h3>'
            card += '<p class="text-white/50 text-sm">' + code + '</p>'
            card += '</div>'
            card += rating_span
            card += '</div>'
            card += sector_p
            card += '<div class="mt-3 flex items-center text-blue-400/70 text-xs group-hover:text-blue-400">'
            card += '<span>查看深度分析</span>'
            card += '<svg class="w-3 h-3 ml-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">'
            card += '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path>'
            card += '</svg>'
            card += '</div>'
            card += '</a>'
            cards_html += card + '\n'

        html = '<!DOCTYPE html>\n'
        html += '<html lang="zh-CN">\n'
        html += '<head>\n'
        html += '    <meta charset="UTF-8">\n'
        html += '    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
        html += '    <title>个股分析中心 - 投资研究中心</title>\n'
        html += '    <script src="https://cdn.tailwindcss.com"></script>\n'
        html += '    <style>\n'
        html += "        @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@300;400;500;700;900&display=swap');\n"
        html += '        * { font-family: "Noto Sans SC", sans-serif; }\n'
        html += '        body {\n'
        html += '            background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 50%, #312e81 100%);\n'
        html += '            min-height: 100vh;\n'
        html += '            padding-top: 80px;\n'
        html += '            color: white;\n'
        html += '        }\n'
        html += '        .nav-bar {\n'
        html += '            position: fixed;\n'
        html += '            top: 0;\n'
        html += '            left: 0;\n'
        html += '            right: 0;\n'
        html += '            z-index: 100;\n'
        html += '            background: rgba(15, 23, 42, 0.9);\n'
        html += '            backdrop-filter: blur(20px);\n'
        html += '            border-bottom: 1px solid rgba(255, 255, 255, 0.1);\n'
        html += '        }\n'
        html += '        .nav-link {\n'
        html += '            color: rgba(255, 255, 255, 0.7);\n'
        html += '            padding: 0.75rem 1rem;\n'
        html += '            text-decoration: none;\n'
        html += '            transition: color 0.3s;\n'
        html += '        }\n'
        html += '        .nav-link:hover, .nav-link.active {\n'
        html += '            color: #60a5fa;\n'
        html += '        }\n'
        html += '        .glass-card {\n'
        html += '            background: rgba(255, 255, 255, 0.05);\n'
        html += '            backdrop-filter: blur(10px);\n'
        html += '            border: 1px solid rgba(255, 255, 255, 0.1);\n'
        html += '            border-radius: 1rem;\n'
        html += '        }\n'
        html += '        .section-title {\n'
        html += '            border-left: 4px solid #3b82f6;\n'
        html += '            padding-left: 1rem;\n'
        html += '            margin-bottom: 1.5rem;\n'
        html += '        }\n'
        html += '    </style>\n'
        html += '</head>\n'
        html += '<body>\n'
        html += '    <nav class="nav-bar">\n'
        html += '        <div class="max-w-7xl mx-auto px-4 flex items-center h-16">\n'
        html += '            <div class="text-xl font-bold text-white mr-8">📈 投资研究中心</div>\n'
        html += '            <a href="../index.html" class="nav-link">首页</a>\n'
        html += '            <a href="index.html" class="nav-link active">个股分析</a>\n'
        html += '            <a href="../industry_chain/index.html" class="nav-link">产业链</a>\n'
        html += '        </div>\n'
        html += '    </nav>\n'
        html += '\n'
        html += '    <div class="max-w-7xl mx-auto px-4 py-8">\n'
        html += '        <div class="text-center mb-12">\n'
        html += '            <h1 class="text-4xl font-black text-white mb-3">🔍 个股分析中心</h1>\n'
        html += '            <p class="text-white/60 text-lg">深度覆盖全市场核心标的，多维分析助力投资决策</p>\n'
        html += '        </div>\n'
        html += '\n'
        html += '        <!-- 统计卡片 -->\n'
        html += '        <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-12">\n'
        html += '            <div class="glass-card rounded-2xl p-6 text-center">\n'
        html += '                <div class="text-4xl font-black text-blue-400 mb-2">' + str(total) + '</div>\n'
        html += '                <div class="text-white/60">覆盖股票</div>\n'
        html += '            </div>\n'
        html += '            <div class="glass-card rounded-2xl p-6 text-center">\n'
        html += '                <div class="text-4xl font-black text-green-400 mb-2">' + str(buy_rated) + '</div>\n'
        html += '                <div class="text-white/60">推荐评级</div>\n'
        html += '            </div>\n'
        html += '            <div class="glass-card rounded-2xl p-6 text-center">\n'
        html += '                <div class="text-4xl font-black text-purple-400 mb-2">' + str(has_page) + '</div>\n'
        html += '                <div class="text-white/60">深度分析页</div>\n'
        html += '            </div>\n'
        html += '        </div>\n'
        html += '\n'
        html += '        <!-- 股票列表 -->\n'
        html += '        <div class="section-title">\n'
        html += '            <h2 class="text-2xl font-bold text-white">全部股票</h2>\n'
        html += '            <p class="text-white/50 text-sm mt-1">按名称排序，点击查看深度分析报告</p>\n'
        html += '        </div>\n'
        html += '\n'
        html += '        <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-5 gap-4">\n'
        html += cards_html
        html += '        </div>\n'
        html += '    </div>\n'
        html += '\n'
        html += '    <footer class="mt-20 py-8 border-t border-white/10 text-center text-white/40 text-sm">\n'
        html += '        <p>投资研究中心 · 数据驱动决策 · 股市有风险，投资需谨慎</p>\n'
        html += '    </footer>\n'
        html += '\n'
        html += '    <!-- 悬浮卡片JS -->\n'
        html += '    <script src="../js/stock-hover-card.js"></script>\n'
        html += '</body>\n'
        html += '</html>'

        # 保存文件
        if output_path is None:
            output_path = str(self.pages_dir / 'index.html')

        import os
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html)

        print(f"✅ 个股分析列表页已生成: {output_path}")
        return html




_manager = None

def get_stock_manager(docs_dir: str = None) -> UnifiedStockManager:
    global _manager
    if _manager is None:
        _manager = UnifiedStockManager(docs_dir)
    return _manager


if __name__ == '__main__':
    # 测试
    manager = UnifiedStockManager()
    stats = manager.get_coverage_stats()
    print("当前覆盖统计:")
    print(f"  股票总数: {stats['total']}")
    print(f"  Level 1 (已发现): {stats['level1']} ({stats['level1_pct']})")
    print(f"  Level 2 (有数据): {stats['level2']} ({stats['level2_pct']})")
    print(f"  Level 3 (有详情页): {stats['level3']} ({stats['level3_pct']})")
