"""
股票发现与注册管理器
- 自动从报告中提取股票名称
- 自动注册到股票池
- 自动生成分析数据和详情页
- 确保全站股票覆盖一致
"""

import os
import re
import json
from pathlib import Path
from typing import List, Dict, Set, Optional, Tuple


class StockDiscoveryManager:
    """股票发现管理器"""
    
    def __init__(self, docs_dir: str = None):
        if docs_dir:
            self.docs_dir = Path(docs_dir)
        else:
            self.docs_dir = Path(__file__).resolve().parent.parent.parent / 'docs'
        
        self.data_dir = self.docs_dir / 'data' / 'stock_analysis'
        self.pages_dir = self.docs_dir / '个股分析'
        self.list_file = self.data_dir / 'stock_list.json'
        
        self._known_stocks = None
        self._stock_code_map = None  # name -> code
    
    def load_stock_list(self) -> Dict:
        """加载股票列表"""
        if self.list_file.exists():
            with open(self.list_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {'stocks': {}, 'total': 0, 'update_time': ''}
    
    def save_stock_list(self, data: Dict):
        """保存股票列表"""
        data['total'] = len(data.get('stocks', {}))
        from datetime import datetime
        data['update_time'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.list_file.parent.mkdir(parents=True, exist_ok=True)
        with open(self.list_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    
    def get_known_stocks(self) -> Set[str]:
        """获取已知股票名称集合"""
        if self._known_stocks is None:
            data = self.load_stock_list()
            self._known_stocks = set(data.get('stocks', {}).keys())
        return self._known_stocks
    
    def get_stock_code_map(self) -> Dict[str, str]:
        """获取股票名称到代码的映射"""
        if self._stock_code_map is None:
            data = self.load_stock_list()
            self._stock_code_map = {
                name: info.get('code', '') 
                for name, info in data.get('stocks', {}).items()
            }
        return self._stock_code_map
    
    def _extract_html_text(self, html_content: str) -> str:
        """从HTML中提取纯文本"""
        # 移除script和style标签内容
        text = re.sub(r'<(script|style)[^>]*>.*?</\1>', '', html_content, flags=re.DOTALL)
        # 移除HTML标签
        text = re.sub(r'<[^>]+>', '', text)
        # 清理空白
        text = re.sub(r'\s+', ' ', text)
        return text.strip()
    
    def extract_stocks_from_text(self, text: str) -> List[Tuple[str, str]]:
        """从文本中提取股票名称和代码
        
        Returns:
            [(股票名, 股票代码), ...]
        """
        found = {}  # name -> code
        
        # 1. 匹配「名称(代码)」格式（最可靠）
        # 支持：中文名(6位数字)、中文名(5位数字港股)、中文名(4位数字.XX)
        pattern = r'([\u4e00-\u9fa5A-Za-z][\u4e00-\u9fa5A-Za-z0-9\*\-]{1,9})\s*[\(（](\d{4,6}[\.\w]*)[\)）]'
        matches = re.findall(pattern, text)
        for name, code in matches:
            name = name.strip()
            if len(name) >= 2:
                found[name] = code
        
        # 2. 匹配已知股票名称
        known = self.get_known_stocks()
        code_map = self.get_stock_code_map()
        
        # 为了避免部分匹配，按长度降序排序
        sorted_stocks = sorted(known, key=len, reverse=True)
        
        for stock_name in sorted_stocks:
            # 使用词边界匹配（中文没有空格，用前后非中文字符判断）
            # 简单处理：直接搜索，但避免子串匹配到更长的名称
            if stock_name in text and stock_name not in found:
                # 简单防误判：确保名称前后不是其他中文字符
                idx = 0
                while True:
                    idx = text.find(stock_name, idx)
                    if idx == -1:
                        break
                    # 检查前后字符
                    before = text[idx-1] if idx > 0 else ''
                    after = text[idx+len(stock_name)] if idx+len(stock_name) < len(text) else ''
                    
                    # 如果前后都是非中文字符或者边界，认为是独立的词
                    if not before or not re.match(r'[\u4e00-\u9fa5]', before) or \
                       not after or not re.match(r'[\u4e00-\u9fa5]', after):
                        found[stock_name] = code_map.get(stock_name, '')
                        break
                    idx += len(stock_name)
        
        # 转换为列表
        result = [(name, code) for name, code in found.items()]
        result.sort(key=lambda x: len(x[0]), reverse=True)
        return result
    
    def discover_from_html(self, html_path: str) -> List[Tuple[str, str]]:
        """从HTML文件中提取股票"""
        path = Path(html_path)
        if not path.exists():
            return []
        
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        text = self._extract_html_text(content)
        return self.extract_stocks_from_text(text)
    
    def discover_from_directory(self, dir_path: str, pattern: str = '*.html') -> Dict[str, List[str]]:
        """从目录下所有文件中发现股票"""
        results = {}
        dir_p = Path(dir_path)
        for f in dir_p.glob(pattern):
            stocks = self.discover_from_html(str(f))
            if stocks:
                results[f.name] = [s[0] for s in stocks]
        return results
    
    def register_stock(self, stock_name: str, stock_code: str = '', 
                      sector: str = '', rating: str = '待分析') -> bool:
        """注册一只新股票到股票池
        
        Returns:
            是否为新增
        """
        data = self.load_stock_list()
        stocks = data.get('stocks', {})
        
        if stock_name in stocks:
            # 已存在，更新信息
            info = stocks[stock_name]
            if stock_code and not info.get('code'):
                info['code'] = stock_code
            if sector and not info.get('sector'):
                info['sector'] = sector
            if rating and rating != '待分析':
                info['rating'] = rating
            self.save_stock_list(data)
            return False
        else:
            # 新增
            stocks[stock_name] = {
                'code': stock_code,
                'sector': sector,
                'rating': rating,
                'score': 0,
                'data_level': 1,  # 1=仅名称, 2=有分析数据, 3=有详情页
            }
            data['stocks'] = stocks
            self.save_stock_list(data)
            # 清除缓存
            self._known_stocks = None
            self._stock_code_map = None
            return True
    
    def batch_register(self, stock_names: List[str], sector: str = '') -> int:
        """批量注册股票
        
        Returns:
            新增数量
        """
        new_count = 0
        for name in stock_names:
            if self.register_stock(name, sector=sector):
                new_count += 1
        return new_count
    
    def generate_stock_page(self, stock_name: str) -> bool:
        """生成单只股票的详情页（如果有分析数据的话）"""
        data = self.load_stock_list()
        stock_info = data.get('stocks', {}).get(stock_name)
        if not stock_info:
            return False
        
        code = stock_info.get('code', '')
        if not code:
            return False
        
        # 检查是否有分析数据
        data_file = self.data_dir / f'{code}.json'
        if not data_file.exists():
            return False
        
        # 生成页面
        try:
            from generators.stock_detail_unified_v2 import StockDetailPageGenerator
            gen = StockDetailPageGenerator(str(self.data_dir), str(self.pages_dir))
            gen.save_page(stock_name, code)
            
            # 更新data_level
            stocks = data['stocks']
            if stock_name in stocks:
                stocks[stock_name]['data_level'] = 3
                self.save_stock_list(data)
            
            return True
        except Exception as e:
            print(f"  生成 {stock_name} 页面失败: {e}")
            return False
    
    def generate_all_missing_pages(self) -> int:
        """为所有有分析数据但没有详情页的股票生成页面"""
        data = self.load_stock_list()
        stocks = data.get('stocks', {})
        
        count = 0
        for name, info in stocks.items():
            code = info.get('code', '')
            if not code:
                continue
            
            data_file = self.data_dir / f'{code}.json'
            page_file = self.pages_dir / f'{name}.html'
            
            if data_file.exists() and not page_file.exists():
                if self.generate_stock_page(name):
                    count += 1
        
        return count
    
    def sync_stock_list_from_files(self):
        """根据实际文件同步更新股票列表元数据"""
        data = self.load_stock_list()
        stocks = data.get('stocks', {})
        
        for name, info in stocks.items():
            code = info.get('code', '')
            
            # 检查分析数据文件
            if code:
                data_file = self.data_dir / f'{code}.json'
                has_data = data_file.exists()
            else:
                has_data = False
            
            # 检查详情页
            page_file = self.pages_dir / f'{name}.html'
            has_page = page_file.exists()
            
            # 更新data_level
            if has_page:
                info['data_level'] = 3
            elif has_data:
                info['data_level'] = 2
            else:
                info['data_level'] = 1
        
        self.save_stock_list(data)
    
    def get_coverage_stats(self) -> Dict:
        """获取覆盖率统计"""
        # 先同步
        self.sync_stock_list_from_files()
        
        data = self.load_stock_list()
        stocks = data.get('stocks', {})
        total = len(stocks)
        
        has_code = sum(1 for s in stocks.values() if s.get('code'))
        has_data = sum(1 for s in stocks.values() if s.get('data_level', 1) >= 2)
        has_page = sum(1 for s in stocks.values() if s.get('data_level', 1) >= 3)
        
        return {
            'total': total,
            'has_code': has_code,
            'has_data': has_data,
            'has_page': has_page,
            'code_coverage': f'{has_code/total*100:.1f}%' if total else '0%',
            'data_coverage': f'{has_data/total*100:.1f}%' if total else '0%',
            'page_coverage': f'{has_page/total*100:.1f}%' if total else '0%',
        }


# 单例
_manager = None

def get_stock_discovery_manager(docs_dir: str = None) -> StockDiscoveryManager:
    global _manager
    if _manager is None:
        _manager = StockDiscoveryManager(docs_dir)
    return _manager


if __name__ == '__main__':
    manager = get_stock_discovery_manager()
    stats = manager.get_coverage_stats()
    print("📊 股票覆盖统计:")
    print(f"   总数: {stats['total']}")
    print(f"   有代码: {stats['has_code']} ({stats['code_coverage']})")
    print(f"   有数据: {stats['has_data']} ({stats['data_coverage']})")
    print(f"   有详情页: {stats['has_page']} ({stats['page_coverage']})")
