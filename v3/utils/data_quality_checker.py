"""
数据质量校验工具
- 验证市场数据的合理性
- 检测异常数据
- 确保报告数据质量
"""

import json
from pathlib import Path
from datetime import datetime, timedelta
from typing import List, Dict, Tuple


class DataQualityChecker:
    """数据质量校验器"""
    
    def __init__(self, data_dir: str = None):
        if data_dir:
            self.data_dir = Path(data_dir)
        else:
            self.data_dir = Path(__file__).resolve().parent.parent.parent / 'data'
    
    def check_portfolio_data(self) -> Tuple[bool, List[str]]:
        """检查持仓数据质量
        
        Returns:
            (is_valid, issues) - 是否有效和问题列表
        """
        issues = []
        
        try:
            portfolio_file = self.data_dir / 'portfolio.json'
            if not portfolio_file.exists():
                issues.append("❌ 持仓数据文件不存在")
                return False, issues
            
            with open(portfolio_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            stocks = data.get('stocks', [])
            if not stocks:
                issues.append("❌ 持仓股票列表为空")
                return False, issues
            
            for stock in stocks:
                name = stock.get('name', '未知')
                code = stock.get('code', stock.get('id', ''))
                current_price = stock.get('current_price', 0)
                today_change = stock.get('today_change', 0)
                cost_price = stock.get('cost_price', 0)
                
                # 检查价格合理性
                if current_price <= 0:
                    issues.append(f"❌ {name}({code}): 当前价格为 0 或负数")
                elif current_price < 1:
                    issues.append(f"⚠️  {name}({code}): 当前价格过低 ({current_price}元)")
                elif current_price > 10000:
                    issues.append(f"⚠️  {name}({code}): 当前价格过高 ({current_price}元)")
                
                # 检查涨跌幅合理性（单日涨跌幅通常在 ±20% 以内，ST股±5%）
                change_pct = abs(today_change) * 100
                is_st = 'ST' in name or 'st' in name.lower()
                max_change = 5 if is_st else 20
                
                if change_pct > max_change:
                    issues.append(f"⚠️  {name}({code}): 涨跌幅异常 ({today_change*100:+.2f}%)，超过 {max_change}%")
                
                # 检查成本价合理性
                if cost_price <= 0:
                    issues.append(f"⚠️  {name}({code}): 成本价为 0 或负数")
                
                # 检查涨跌幅与价格是否匹配（粗略校验）
                if current_price > 0 and cost_price > 0:
                    expected_change = (current_price - cost_price) / cost_price
                    # 这个校验不一定准确，因为 today_change 是当日涨跌幅，不是相对成本
                    # 只是简单检查是否数量级一致
                    if abs(today_change) > 1:
                        issues.append(f"⚠️  {name}({code}): 涨跌幅数值异常 ({today_change})，应该是小数形式")
            
            # 检查更新时间
            update_time = data.get('update_time', '')
            if update_time:
                try:
                    update_dt = datetime.strptime(update_time, '%Y年%m月%d日 %H:%M')
                    now = datetime.now()
                    time_diff = now - update_dt
                    
                    if time_diff > timedelta(hours=4):
                        issues.append(f"⚠️  数据更新时间较早 ({update_time})，可能不是最新的")
                    elif time_diff < timedelta(minutes=-1):
                        issues.append(f"⚠️  数据更新时间在未来 ({update_time})，可能有误")
                except:
                    pass
            
            if not issues:
                issues.append("✅ 持仓数据质量良好")
            
            return True, issues
            
        except Exception as e:
            issues.append(f"❌ 检查持仓数据时出错: {e}")
            return False, issues
    
    def check_market_data(self) -> Tuple[bool, List[str]]:
        """检查市场数据质量
        
        Returns:
            (is_valid, issues) - 是否有效和问题列表
        """
        issues = []
        
        try:
            market_file = self.data_dir / 'market.json'
            if not market_file.exists():
                issues.append("❌ 市场数据文件不存在")
                return False, issues
            
            with open(market_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            indices = data.get('indices', [])
            if not indices:
                issues.append("❌ 指数数据为空")
                return False, issues
            
            # 检查指数数据
            for idx in indices:
                name = idx.get('name', '未知')
                price = idx.get('price', 0)
                change_pct = idx.get('change_pct', 0)
                
                if price <= 0:
                    issues.append(f"❌ {name}: 指数点位为 0 或负数")
                
                if abs(change_pct) > 0.1:  # 10%
                    issues.append(f"⚠️  {name}: 涨跌幅异常 ({change_pct*100:+.2f}%)")
            
            # 检查市场统计
            market_data = data.get('market_data', {})
            up_count = market_data.get('up_count', 0)
            down_count = market_data.get('down_count', 0)
            turnover = market_data.get('turnover', '')
            
            if up_count + down_count > 10000:
                issues.append(f"⚠️  涨跌家数总和过大 ({up_count + down_count})")
            elif up_count + down_count < 100:
                issues.append(f"⚠️  涨跌家数总和过小 ({up_count + down_count})")
            
            if not turnover:
                issues.append("⚠️  成交额数据为空")
            
            # 检查情绪数据
            sentiment = data.get('sentiment', {})
            fear_greed = sentiment.get('fear_greed', 50)
            if fear_greed < 0 or fear_greed > 100:
                issues.append(f"⚠️  恐惧贪婪指数异常 ({fear_greed})")
            
            # 检查更新时间
            update_time = data.get('update_time', '')
            if update_time:
                try:
                    update_dt = datetime.strptime(update_time, '%Y年%m月%d日 %H:%M')
                    now = datetime.now()
                    time_diff = now - update_dt
                    
                    if time_diff > timedelta(hours=4):
                        issues.append(f"⚠️  数据更新时间较早 ({update_time})，可能不是最新的")
                except:
                    pass
            
            if not any('❌' in issue for issue in issues):
                issues.insert(0, "✅ 市场数据质量良好")
            
            return not any('❌' in issue for issue in issues), issues
            
        except Exception as e:
            issues.append(f"❌ 检查市场数据时出错: {e}")
            return False, issues
    
    def check_all(self) -> dict:
        """检查所有数据质量
        
        Returns:
            dict: 检查结果汇总
        """
        portfolio_valid, portfolio_issues = self.check_portfolio_data()
        market_valid, market_issues = self.check_market_data()
        
        all_issues = portfolio_issues + market_issues
        all_valid = portfolio_valid and market_valid
        
        return {
            'is_valid': all_valid,
            'portfolio': {
                'valid': portfolio_valid,
                'issues': portfolio_issues,
            },
            'market': {
                'valid': market_valid,
                'issues': market_issues,
            },
            'all_issues': all_issues,
            'summary': f"数据质量{'良好' if all_valid else '存在问题'}，共 {len(all_issues)} 项检查结果",
        }


def check_data_quality(data_dir: str = None) -> dict:
    """便捷函数：检查数据质量"""
    checker = DataQualityChecker(data_dir)
    return checker.check_all()


def print_data_quality_report(data_dir: str = None):
    """打印数据质量报告"""
    result = check_data_quality(data_dir)
    
    print("=" * 60)
    print("📊 数据质量检查报告")
    print("=" * 60)
    print()
    
    print("📈 市场数据:")
    for issue in result['market']['issues']:
        print(f"  {issue}")
    print()
    
    print("💼 持仓数据:")
    for issue in result['portfolio']['issues']:
        print(f"  {issue}")
    print()
    
    print("=" * 60)
    print(f"{'✅' if result['is_valid'] else '❌'} {result['summary']}")
    print("=" * 60)


if __name__ == '__main__':
    print_data_quality_report()
