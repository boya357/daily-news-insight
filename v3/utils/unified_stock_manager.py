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
from generators.stock_analysis_page_v2 import generate_stock_page


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
            generate_stock_page(stock_code, stock_name, output_path)
            
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
