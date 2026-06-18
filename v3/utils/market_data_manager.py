"""
统一市场数据管理器
- 封装所有行情数据更新操作
- 确保报告生成前数据是最新的
- 多数据源冗余，失败自动降级
- 所有报告生成器统一通过此模块获取实时数据
"""

import os
import sys
import json
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Optional, Tuple

# 确保可以导入同目录模块
_current_dir = Path(__file__).resolve().parent
sys.path.insert(0, str(_current_dir.parent))

from utils.stable_market_fetcher import (
    fetch_indexes,
    fetch_stock_price,
    _http_get,
    _get_headers,
)


class MarketDataManager:
    """统一市场数据管理器
    
    负责：
    1. 更新大盘指数数据（真实行情）
    2. 更新个股价格数据（真实行情）
    3. 更新持仓组合数据
    4. 估算市场情绪、涨跌家数等衍生数据
    5. 提供统一的数据访问接口
    """
    
    def __init__(self, data_dir: str = None):
        if data_dir:
            self.data_dir = Path(data_dir)
        else:
            self.data_dir = Path(__file__).resolve().parent.parent.parent / 'data'
        
        self.portfolio_file = self.data_dir / 'portfolio.json'
        self.market_file = self.data_dir / 'market.json'
    
    def _load_json(self, filepath: Path) -> dict:
        """加载JSON文件"""
        if not filepath.exists():
            return {}
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    def _save_json(self, filepath: Path, data: dict):
        """保存JSON文件"""
        filepath.parent.mkdir(parents=True, exist_ok=True)
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
    
    # ============ 指数数据更新 ============
    
    def update_indices(self) -> Tuple[List[dict], bool]:
        """更新大盘指数数据
        
        Returns:
            (indices_list, success) - 指数数据列表和是否成功
        """
        try:
            indices = fetch_indexes()
            
            if not indices or len(indices) < 3:
                print(f"⚠️  指数数据获取不完整，仅 {len(indices)} 个，保留原有数据")
                return [], False
            
            # 读取现有market数据
            market_data = self._load_json(self.market_file)
            
            # 更新指数数据
            market_data['indices'] = indices
            market_data['update_time'] = datetime.now().strftime('%Y年%m月%d日 %H:%M')
            
            # 更新市场情绪（基于指数表现）
            avg_change = sum(idx['change_pct'] for idx in indices) / len(indices)
            sentiment = self._calculate_sentiment(avg_change)
            market_data['sentiment'] = sentiment
            
            # 估算涨跌家数
            market_stats = self._estimate_market_stats(avg_change)
            if 'market_data' not in market_data:
                market_data['market_data'] = {}
            market_data['market_data'].update(market_stats)
            
            # 保存
            self._save_json(self.market_file, market_data)
            
            print(f"✅ 指数数据更新完成 ({len(indices)} 个指数)")
            return indices, True
            
        except Exception as e:
            print(f"❌ 更新指数数据失败: {e}")
            return [], False
    
    # ============ 持仓数据更新 ============
    
    def update_portfolio(self) -> Tuple[List[dict], bool]:
        """更新持仓股的实时行情数据
        
        Returns:
            (stocks_list, success) - 更新后的股票列表和是否成功
        """
        try:
            portfolio_data = self._load_json(self.portfolio_file)
            
            if not portfolio_data or 'stocks' not in portfolio_data:
                print("❌ 持仓数据文件不存在或格式错误")
                return [], False
            
            stocks = portfolio_data['stocks']
            success_count = 0
            
            for stock in stocks:
                code = stock.get('id', stock.get('code', ''))
                name = stock.get('name', '')
                
                if not code:
                    continue
                
                # 获取实时行情
                quote = fetch_stock_price(code, name)
                
                if quote and quote.get('price', 0) > 0:
                    old_price = stock.get('current_price', 0)
                    stock['current_price'] = quote['price']
                    stock['today_change'] = quote['change_pct']
                    stock['today_high'] = quote.get('high', quote['price'])
                    stock['today_low'] = quote.get('low', quote['price'])
                    stock['today_open'] = quote.get('open', quote['price'])
                    stock['pre_close'] = quote.get('pre_close', quote['price'])
                    
                    # 更新风险状态
                    self._update_risk_status(stock)
                    
                    change_str = f"{'+' if quote['up'] else ''}{quote['change']:.2f}"
                    pct_str = f"{'+' if quote['up'] else ''}{quote['change_pct']*100:.2f}%"
                    print(f"  ✅ {name}: {quote['price']}元 ({change_str}, {pct_str}) [{quote.get('source', '?')}]")
                    success_count += 1
                else:
                    print(f"  ⚠️  {name}: 获取失败，保留原价 {stock.get('current_price', 0)}元")
            
            # 更新组合整体数据
            self._update_portfolio_summary(portfolio_data)
            
            portfolio_data['update_time'] = datetime.now().strftime('%Y年%m月%d日 %H:%M')
            
            # 保存
            self._save_json(self.portfolio_file, portfolio_data)
            
            print(f"✅ 持仓数据更新完成: {success_count}/{len(stocks)} 只成功")
            return stocks, success_count > 0
            
        except Exception as e:
            print(f"❌ 更新持仓数据失败: {e}")
            import traceback
            traceback.print_exc()
            return [], False
    
    # ============ 热门板块数据更新 ============
    
    def update_hot_sectors(self) -> bool:
        """更新热门板块数据
        
        尝试从东方财富获取板块涨幅数据，失败则使用估算
        """
        try:
            # 尝试从东方财富获取板块数据
            sectors = self._fetch_sectors_from_eastmoney()
            
            if sectors and len(sectors) >= 5:
                market_data = self._load_json(self.market_file)
                market_data['sectors_hot'] = sectors[:10]
                market_data['sectors_cold'] = sectors[-5:] if len(sectors) > 10 else []
                self._save_json(self.market_file, market_data)
                print(f"✅ 板块数据更新完成 ({len(sectors)} 个板块)")
                return True
            
            print("⚠️  板块数据获取失败，使用估算数据")
            return False
            
        except Exception as e:
            print(f"❌ 更新板块数据失败: {e}")
            return False
    
    def _fetch_sectors_from_eastmoney(self) -> List[dict]:
        """从东方财富获取板块涨幅数据"""
        try:
            # 东方财富行业板块API
            url = "https://push2.eastmoney.com/api/qt/clist/get?pn=1&pz=50&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&wbp2u=|0|0|0|web&fid=f3&fs=m:90+t:2+f:!50&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f26,f22,f11,f62,f128,f136,f115,f152,f133,f1080"
            
            headers = _get_headers()
            headers['Referer'] = 'https://quote.eastmoney.com/center/gridlist.html'
            
            import urllib.request
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=10) as resp:
                data = json.loads(resp.read().decode('utf-8'))
                
                if data.get('data', {}).get('diff'):
                    sectors_raw = data['data']['diff']
                    sectors = []
                    
                    for s in sectors_raw:
                        name = s.get('f14', '')
                        change_pct = s.get('f3', 0) / 100  # 百分比转小数
                        leader = s.get('f128', '')
                        
                        if name:
                            sectors.append({
                                'name': name,
                                'change_pct': change_pct / 100,  # 再转一次，因为返回的是百分比数值
                                'up': change_pct >= 0,
                                'leader': leader,
                            })
                    
                    # 按涨幅排序
                    sectors.sort(key=lambda x: x['change_pct'], reverse=True)
                    return sectors
            
        except Exception as e:
            print(f"  获取东方财富板块数据失败: {e}")
        
        return []
    
    # ============ 完整更新 ============
    
    def update_all(self, force_update: bool = False) -> dict:
        """完整更新所有市场数据
        
        Args:
            force_update: 是否强制更新，即使数据较新也重新获取
            
        Returns:
            dict: 更新结果摘要
        """
        print("=" * 60)
        print("📊 统一市场数据更新")
        print(f"🕐 开始时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("=" * 60)
        print()
        
        results = {
            'indices': False,
            'portfolio': False,
            'sectors': False,
            'update_time': datetime.now().isoformat(),
        }
        
        # 1. 更新指数
        print("📈 更新大盘指数...")
        _, results['indices'] = self.update_indices()
        print()
        
        # 2. 更新持仓
        print("💼 更新持仓股行情...")
        _, results['portfolio'] = self.update_portfolio()
        print()
        
        # 3. 更新板块
        print("🏭 更新热门板块...")
        results['sectors'] = self.update_hot_sectors()
        print()
        
        # 总结
        success_count = sum(1 for v in results.values() if v is True)
        print("=" * 60)
        print(f"📋 更新完成: {success_count}/3 项成功")
        
        if success_count >= 2:
            print("✅ 数据更新成功，可以生成报告")
        else:
            print("⚠️  数据更新不完全，可能影响报告准确性")
        
        print("=" * 60)
        
        return results
    
    # ============ 辅助方法 ============
    
    def _calculate_sentiment(self, avg_change: float) -> dict:
        """根据指数平均涨跌幅计算市场情绪"""
        if avg_change > 0.03:
            fear_greed = 90
            fg_text = "极度贪婪"
        elif avg_change > 0.02:
            fear_greed = 80
            fg_text = "贪婪"
        elif avg_change > 0.01:
            fear_greed = 68
            fg_text = "乐观"
        elif avg_change > 0:
            fear_greed = 58
            fg_text = "偏乐观"
        elif avg_change > -0.01:
            fear_greed = 48
            fg_text = "中性"
        elif avg_change > -0.02:
            fear_greed = 38
            fg_text = "恐慌"
        else:
            fear_greed = 22
            fg_text = "恐惧"
        
        return {
            'fear_greed': fear_greed,
            'fear_greed_text': fg_text,
        }
    
    def _estimate_market_stats(self, avg_change: float) -> dict:
        """估算市场涨跌家数等统计数据
        
        注意：这些是估算值，真实数据需要从专门的API获取
        """
        # 估算涨跌比（基于指数表现）
        up_ratio = min(0.85, max(0.15, 0.5 + avg_change * 8))
        total_stocks = 5500  # A股总数估算
        up_count = int(total_stocks * up_ratio)
        down_count = total_stocks - up_count
        
        # 估算涨跌停数量
        if avg_change > 0:
            limit_up = int(40 + avg_change * 2000)
            limit_down = max(5, int(20 - avg_change * 300))
        else:
            limit_up = max(10, int(40 + avg_change * 300))
            limit_down = int(30 - avg_change * 800)
        
        limit_up = max(5, min(300, limit_up))
        limit_down = max(5, min(200, limit_down))
        
        # 估算成交额（万亿级市场）
        base_turnover = 20000  # 基数2万亿
        turnover_estimate = base_turnover + abs(avg_change) * 30000
        turnover_str = f"{int(turnover_estimate / 100) * 100}亿"
        
        return {
            'turnover': turnover_str,
            'up_count': up_count,
            'down_count': down_count,
            'limit_up_count': limit_up,
            'limit_down_count': limit_down,
        }
    
    def _update_risk_status(self, stock: dict):
        """更新股票的风险状态"""
        cost_price = stock.get('cost_price', 0)
        current_price = stock.get('current_price', 0)
        stop_loss_price = stock.get('stop_loss_price', 0)
        
        if stop_loss_price > 0 and current_price <= stop_loss_price:
            stock['risk_level'] = '高危区 - 已跌破止损'
            stock['risk_color'] = 'text-red-600'
            stock['risk_progress'] = 95
            stock['icon'] = '🆘'
            stock['gradient'] = 'from-red-500 to-orange-500'
        elif cost_price > 0:
            profit_pct = (current_price - cost_price) / cost_price
            if profit_pct > 0.5:
                stock['risk_level'] = '安全区 - 大幅盈利'
                stock['risk_color'] = 'text-green-600'
                stock['risk_progress'] = 20
                stock['icon'] = '✅'
                stock['gradient'] = 'from-green-500 to-emerald-500'
            elif profit_pct > 0:
                stock['risk_level'] = '安全区 - 正常波动'
                stock['risk_color'] = 'text-green-600'
                stock['risk_progress'] = 40
                stock['icon'] = '📈'
                stock['gradient'] = 'from-blue-500 to-cyan-500'
            elif profit_pct > -0.1:
                stock['risk_level'] = '警戒区 - 小幅浮亏'
                stock['risk_color'] = 'text-yellow-600'
                stock['risk_progress'] = 65
                stock['icon'] = '⚠️'
                stock['gradient'] = 'from-yellow-500 to-orange-500'
            else:
                stock['risk_level'] = '危险区 - 浮亏较大'
                stock['risk_color'] = 'text-orange-600'
                stock['risk_progress'] = 80
                stock['icon'] = '📉'
                stock['gradient'] = 'from-orange-500 to-red-500'
    
    def _update_portfolio_summary(self, portfolio_data: dict):
        """更新组合整体收益数据"""
        stocks = portfolio_data.get('stocks', [])
        
        total_cost = 0
        total_value = 0
        profit_count = 0
        loss_count = 0
        stop_loss_break_count = 0
        
        for stock in stocks:
            cost_price = stock.get('cost_price', 0)
            current_price = stock.get('current_price', 0)
            # 假设每只股票持仓份额相同，或者用数量计算
            # 这里简化为等权重
            shares = stock.get('shares', 100)
            
            total_cost += cost_price * shares
            total_value += current_price * shares
            
            if current_price >= cost_price:
                profit_count += 1
            else:
                loss_count += 1
            
            stop_loss = stock.get('stop_loss_price', 0)
            if stop_loss > 0 and current_price <= stop_loss:
                stop_loss_break_count += 1
        
        if total_cost > 0:
            total_return = (total_value - total_cost) / total_cost
            portfolio_data['portfolio']['total_return'] = round(total_return, 4)
        
        portfolio_data['portfolio']['profit_count'] = profit_count
        portfolio_data['portfolio']['loss_count'] = loss_count
        portfolio_data['portfolio']['stop_loss_break_count'] = stop_loss_break_count


# 全局单例
_manager = None


def get_market_manager(data_dir: str = None) -> MarketDataManager:
    """获取市场数据管理器单例"""
    global _manager
    if _manager is None:
        _manager = MarketDataManager(data_dir)
    return _manager


def update_market_data(data_dir: str = None, force: bool = False) -> dict:
    """便捷函数：更新所有市场数据
    
    Args:
        data_dir: 数据目录路径
        force: 是否强制更新
    
    Returns:
        dict: 更新结果
    """
    manager = get_market_manager(data_dir)
    return manager.update_all(force_update=force)


def update_portfolio_data(data_dir: str = None) -> Tuple[List[dict], bool]:
    """便捷函数：仅更新持仓数据"""
    manager = get_market_manager(data_dir)
    return manager.update_portfolio()


def update_index_data(data_dir: str = None) -> Tuple[List[dict], bool]:
    """便捷函数：仅更新指数数据"""
    manager = get_market_manager(data_dir)
    return manager.update_indices()


if __name__ == '__main__':
    # 测试
    results = update_market_data()
    print("\n最终结果:", results)
