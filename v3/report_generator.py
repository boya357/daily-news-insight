"""
报告生成调度器
- 统一管理所有报告的生成
- 生成前自动更新实时行情数据
- 确保所有报告使用同源数据
- 支持各种报告类型：盘中快报、日报、S级催化扫描等
"""

import os
import sys
from pathlib import Path
from datetime import datetime

# 确保路径正确
_current_dir = Path(__file__).resolve().parent
sys.path.insert(0, str(_current_dir))

from utils.market_data_manager import get_market_manager
from utils.data_quality_checker import DataQualityChecker


class ReportGenerator:
    """报告生成调度器
    
    负责：
    1. 生成前自动更新行情数据
    2. 调用对应生成器生成报告
    3. 保存报告到正确位置
    4. 更新列表页
    """
    
    def __init__(self, data_dir: str = None, docs_dir: str = None):
        self.data_dir = Path(data_dir) if data_dir else _current_dir.parent / 'data'
        self.docs_dir = Path(docs_dir) if docs_dir else _current_dir.parent / 'docs'
        
        self.market_manager = get_market_manager(str(self.data_dir))
        self.quality_checker = DataQualityChecker(str(self.data_dir))
    
    def _ensure_data_updated(self, force: bool = False) -> bool:
        """确保数据已更新
        
        Args:
            force: 是否强制更新
            
        Returns:
            bool: 数据是否可用
        """
        # 检查数据文件是否存在
        market_file = self.data_dir / 'market.json'
        portfolio_file = self.data_dir / 'portfolio.json'
        
        if not market_file.exists() or not portfolio_file.exists() or force:
            # 需要更新数据
            results = self.market_manager.update_all(force_update=force)
            # 至少指数和持仓要成功
            return results.get('indices', False) and results.get('portfolio', False)
        
        return True
    
    def _check_data_quality(self) -> dict:
        """检查数据质量
        
        Returns:
            dict: 质量检查结果
        """
        return self.quality_checker.check_all()
    
    def _validate_before_generate(self, force_update: bool = True) -> bool:
        """生成前验证
        
        1. 更新数据
        2. 检查数据质量
        
        Returns:
            bool: 是否可以继续生成
        """
        # 1. 更新数据
        data_ok = self._ensure_data_updated(force=force_update)
        
        if not data_ok:
            print("❌ 数据更新失败，无法生成报告")
            return False
        
        # 2. 检查数据质量
        quality = self._check_data_quality()
        
        if not quality['is_valid']:
            print("⚠️  数据质量存在问题，请检查:")
            for issue in quality['all_issues']:
                if '❌' in issue:
                    print(f"   {issue}")
            # 有严重错误时不生成报告
            return False
        
        return True
    
    def generate_intraday(self, date_str: str = None, subtitle: str = None, 
                          force_data_update: bool = True) -> str:
        """生成盘中快报
        
        Args:
            date_str: 日期字符串，如 '2026-06-18'，默认为今天
            subtitle: 副标题
            force_data_update: 是否强制更新数据
            
        Returns:
            str: 生成的HTML内容
        """
        # 1. 确保数据最新且质量合格
        if force_data_update:
            if not self._validate_before_generate(force_update=True):
                raise RuntimeError("数据验证失败，无法生成报告")
        
        # 2. 导入生成器
        from generators.intraday_pro import IntradayProGenerator
        
        # 3. 生成报告
        if date_str is None:
            date_str = datetime.now().strftime('%Y-%m-%d')
        
        gen = IntradayProGenerator(date_str=date_str, subtitle=subtitle, 
                                   data_dir=str(self.data_dir))
        gen.build_standard_report()
        html = gen.render()
        
        # 4. 保存报告
        output_dir = self.docs_dir / 'intraday'
        output_dir.mkdir(parents=True, exist_ok=True)
        
        date_for_file = date_str.replace('-', '')
        output_file = output_dir / f'{date_for_file}_盘中快报.html'
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html)
        
        print(f"✅ 盘中快报已保存: {output_file}")
        
        # 5. 更新列表页
        try:
            self._update_intraday_list()
        except Exception as e:
            print(f"⚠️  更新列表页失败: {e}")
        
        return html
    
    def generate_s_level_catalyst(self, date_str: str = None, 
                                  force_data_update: bool = True,
                                  time_prefix: str = '盘前') -> str:
        """生成S级催化扫描报告
        
        Args:
            date_str: 日期字符串
            force_data_update: 是否强制更新数据
            time_prefix: 时间前缀，如 '盘前'、'盘中'、'盘后'
            
        Returns:
            str: 生成的HTML内容
        """
        # 1. 确保数据最新且质量合格
        if force_data_update:
            if not self._validate_before_generate(force_update=True):
                raise RuntimeError("数据验证失败，无法生成报告")
        
        # 2. 导入生成器
        from generators.s_level_catalyst_pro import SLevelCatalystProGenerator
        
        # 3. 生成报告
        if date_str is None:
            date_str = datetime.now().strftime('%Y-%m-%d')
        
        gen = SLevelCatalystProGenerator(
            date_str=date_str, 
            data_dir=str(self.data_dir)
        )
        gen.build_standard_report()
        html = gen.render()
        
        # 4. 保存报告
        output_dir = self.docs_dir / 's级催化扫描'
        output_dir.mkdir(parents=True, exist_ok=True)
        
        date_for_file = date_str.replace('-', '')
        output_file = output_dir / f'{date_for_file}_{time_prefix}_S级催化扫描.html'
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html)
        
        print(f"✅ S级催化扫描报告已保存: {output_file}")
        
        return html
    
    def generate_daily(self, date_str: str = None, 
                       force_data_update: bool = True) -> str:
        """生成每日投资日报
        
        Args:
            date_str: 日期字符串
            force_data_update: 是否强制更新数据
            
        Returns:
            str: 生成的HTML内容
        """
        # 1. 确保数据最新且质量合格
        if force_data_update:
            if not self._validate_before_generate(force_update=True):
                raise RuntimeError("数据验证失败，无法生成报告")
        
        # 2. 导入生成器
        from generators.daily_pro import DailyProGenerator
        
        # 3. 生成报告
        if date_str is None:
            date_str = datetime.now().strftime('%Y-%m-%d')
        
        gen = DailyProGenerator(date_str=date_str, 
                                data_dir=str(self.data_dir))
        gen.build_standard_report()
        html = gen.render()
        
        # 4. 保存报告
        output_dir = self.docs_dir / 'daily'
        output_dir.mkdir(parents=True, exist_ok=True)
        
        date_for_file = date_str.replace('-', '')
        output_file = output_dir / f'{date_for_file}_每日投资日报.html'
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html)
        
        print(f"✅ 每日投资日报已保存: {output_file}")
        
        return html
    
    def _update_intraday_list(self):
        """更新盘中快报列表页"""
        try:
            from generators.list_page_pro import ListPageProGenerator
            
            list_gen = ListPageProGenerator(
                channel_key='intraday',
                docs_dir=str(self.docs_dir),
                data_dir=str(self.data_dir),
            )
            list_gen.publish()
            print("✅ 盘中快报列表页已更新")
        except Exception as e:
            print(f"⚠️  更新列表页失败: {e}")
            import traceback
            traceback.print_exc()
    
    def update_all_list_pages(self):
        """更新所有列表页"""
        # TODO: 实现所有类型报告的列表页更新
        pass


# 便捷函数
def generate_intraday_report(date_str: str = None, force_update: bool = True) -> str:
    """便捷函数：生成盘中快报"""
    generator = ReportGenerator()
    return generator.generate_intraday(date_str=date_str, force_data_update=force_update)


def generate_s_level_report(date_str: str = None, force_update: bool = True) -> str:
    """便捷函数：生成S级催化扫描报告"""
    generator = ReportGenerator()
    return generator.generate_s_level_catalyst(date_str=date_str, force_data_update=force_update)


def generate_daily_report(date_str: str = None, force_update: bool = True) -> str:
    """便捷函数：生成每日投资日报"""
    generator = ReportGenerator()
    return generator.generate_daily(date_str=date_str, force_data_update=force_update)


def update_all_market_data(force: bool = False) -> dict:
    """便捷函数：更新所有市场数据"""
    generator = ReportGenerator()
    generator._ensure_data_updated(force=force)
    return {'status': 'success'}


if __name__ == '__main__':
    import argparse
    
    parser = argparse.ArgumentParser(description='报告生成调度器')
    parser.add_argument('--type', '-t', type=str, default='intraday',
                        help='报告类型: intraday/daily/s_level')
    parser.add_argument('--date', '-d', type=str, default=None,
                        help='日期: YYYY-MM-DD')
    parser.add_argument('--no-data-update', action='store_true',
                        help='不更新数据，直接使用现有数据')
    
    args = parser.parse_args()
    
    generator = ReportGenerator()
    
    if args.type == 'intraday':
        html = generator.generate_intraday(
            date_str=args.date,
            force_data_update=not args.no_data_update
        )
        print(f"\n✅ 盘中快报生成完成，长度: {len(html)} 字符")
    elif args.type == 'daily':
        html = generator.generate_daily(
            date_str=args.date,
            force_data_update=not args.no_data_update
        )
        print(f"\n✅ 每日投资日报生成完成，长度: {len(html)} 字符")
    elif args.type == 's_level':
        html = generator.generate_s_level_catalyst(
            date_str=args.date,
            force_data_update=not args.no_data_update
        )
        print(f"\n✅ S级催化扫描报告生成完成，长度: {len(html)} 字符")
    else:
        print(f"❌ 不支持的报告类型: {args.type}")
