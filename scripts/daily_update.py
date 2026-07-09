#!/usr/bin/env python3
"""
每日数据更新与页面生成脚本
- 更新市场数据
- 更新持仓数据
- 更新龙虎榜数据
- 生成所有数据驱动页面
- 同步数据到docs/data
- 自动Git提交部署
"""

import sys
import os
import json
import shutil
from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
V3_DIR = BASE_DIR / 'v3'
sys.path.insert(0, str(V3_DIR))

from utils.stable_market_fetcher import (
    safe_update_market_data,
    safe_update_portfolio,
    update_longhubang,
)


def update_all_data():
    """更新所有数据"""
    print("=" * 60)
    print("📊 开始更新所有数据")
    print("=" * 60)
    print()
    
    # 1. 更新市场数据
    print("1️⃣  更新市场数据...")
    market_data = safe_update_market_data()
    if market_data:
        print(f"   ✅ 市场数据更新完成")
    else:
        print(f"   ❌ 市场数据更新失败")
    print()
    
    # 2. 更新持仓数据
    print("2️⃣  更新持仓数据...")
    portfolio_data = safe_update_portfolio()
    if portfolio_data:
        print(f"   ✅ 持仓数据更新完成")
    else:
        print(f"   ❌ 持仓数据更新失败")
    print()
    
    # 3. 更新龙虎榜数据
    print("3️⃣  更新龙虎榜数据...")
    longhubang_data = update_longhubang()
    if longhubang_data:
        print(f"   ✅ 龙虎榜数据更新完成")
    else:
        print(f"   ❌ 龙虎榜数据更新失败")
    print()
    
    # 4. 更新全球市场数据
    print("4️⃣  更新全球市场数据...")
    try:
        from fetch_global_market import main as fetch_global
        global_data = fetch_global()
        print(f"   ✅ 全球市场数据更新完成")
    except Exception as e:
        print(f"   ⚠️  全球市场数据更新失败: {e}")
        global_data = None
    print()
    
    return market_data, portfolio_data, longhubang_data


def generate_all_pages():
    """生成所有数据驱动页面"""
    print("=" * 60)
    print("📄 开始生成所有数据驱动页面")
    print("=" * 60)
    print()
    
    generated_pages = []
    
    # 需要生成的页面列表（数据驱动型）
    pages = [
        # 首页
        ('home_page_pro', 'HomePageProGenerator', 'docs/index.html', {}),
        # 持仓仪表盘（特殊：参数是data_path）
        ('portfolio_dashboard_pro', 'PortfolioDashboardProGenerator', 'docs/portfolio/index.html', {'param_name': 'data_path', 'param_value': 'data/portfolio.json'}),
        # 龙虎榜
        ('longhubang_pro', 'LonghuBangProGenerator', 'docs/longhubang/index.html', {}),
        # 板块热力图
        ('sector_heatmap_pro', 'SectorHeatmapProGenerator', 'docs/sector-heatmap/index.html', {}),
        # 题材健康度
        ('topic_health_pro', 'TopicHealthProGenerator', 'docs/topic-health/index.html', {}),
        # 智能选题
        ('topic_picker_pro', 'TopicPickerProGenerator', 'docs/topic-picker/index.html', {}),
        # 预判验证中心
        ('prediction_center_pro', 'PredictionCenterProGenerator', 'docs/prediction-center/index.html', {}),
        # 智能预警系统
        ('alert_system_pro', 'AlertSystemProGenerator', 'docs/alert-system/index.html', {}),
        # 周度进化
        ('weekly_evolution_pro', 'WeeklyEvolutionProGenerator', 'docs/weekly-evolution/index.html', {}),
        # 数据时光机（特殊：类名不同）
        ('time_machine_pro', 'TimeMachinePage', 'docs/time-machine/index.html', {}),
    ]
    
    for i, (module_name, class_name, output_path, kwargs) in enumerate(pages, 1):
        try:
            module = __import__(f'generators.{module_name}', fromlist=[class_name])
            generator_class = getattr(module, class_name)
            
            # 处理特殊参数
            if kwargs:
                param_name = kwargs.get('param_name', 'data_dir')
                param_value = kwargs.get('param_value', 'data')
                generator = generator_class(**{param_name: param_value})
            else:
                generator = generator_class(data_dir='data')
            
            result = generator.publish(output_path)
            
            if isinstance(result, dict) and result.get('success'):
                print(f"{i:2d}. ✅ {class_name}: {result.get('file_size', 0)} 字节")
                generated_pages.append(output_path)
            else:
                print(f"{i:2d}. ⚠️  {class_name}: 生成结果异常")
        except Exception as e:
            print(f"{i:2d}. ❌ {class_name}: {e}")
    
    print()
    print(f"✅ 成功生成 {len(generated_pages)}/{len(pages)} 个页面")
    return generated_pages


def sync_data_to_docs():
    """同步数据文件到docs/data目录"""
    print()
    print("🔄 同步数据到 docs/data/ ...")
    
    source_dir = BASE_DIR / 'data'
    target_dir = BASE_DIR / 'docs' / 'data'
    
    os.makedirs(target_dir, exist_ok=True)
    
    # 需要同步的数据文件
    data_files = [
        'market.json',
        'portfolio.json',
        'longhubang_market.json',
    ]
    
    synced = 0
    for filename in data_files:
        source = source_dir / filename
        target = target_dir / filename
        if source.exists():
            shutil.copy2(source, target)
            synced += 1
            print(f"   ✅ {filename}")
        else:
            print(f"   ⚠️  {filename} 不存在，跳过")
    
    print(f"✅ 同步完成 {synced}/{len(data_files)} 个文件")
    return synced


def git_commit_and_push():
    """Git提交并推送"""
    print()
    print("📝 Git 提交部署...")
    
    try:
        os.chdir(BASE_DIR)
        
        # 添加所有变更
        os.system('git add -A')
        
        # 提交
        commit_msg = f"自动更新: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} 数据与页面更新"
        result = os.system(f'git commit -m "{commit_msg}" --allow-empty')
        
        if result == 0:
            # 推送
            push_result = os.system('git push')
            if push_result == 0:
                print("✅ Git 推送成功")
                return True
            else:
                print("❌ Git 推送失败")
        else:
            print("⚠️  Git 提交失败或无变更")
    except Exception as e:
        print(f"❌ Git 操作异常: {e}")
    
    return False



def generate_all_reports():
    """生成所有报告类页面（Pro版）"""
    print()
    print("=" * 60)
    print("📄 生成所有报告类页面（Pro版）")
    print("=" * 60)
    print()
    
    import sys
    sys.path.insert(0, os.path.join(BASE_DIR, 'v3'))
    
    reports = [
        ('daily_pro', 'DailyReportProGenerator', '每日新闻洞察', 'daily'),
        ('aftermarket_pro', 'AftermarketProGenerator', '盘后速递', 'aftermarket'),
        ('s_level_catalyst_pro', 'SLevelCatalystProGenerator', 'S级催化扫描', 's_level_catalyst'),
        ('tomorrow_catalyst_pro', 'TomorrowCatalystProGenerator', '明日催化剂', 'tomorrow_catalyst'),
        ('weekly_review_pro', 'WeeklyReviewProGenerator', '周复盘', 'weekly_review'),
        ('weekend_express_pro', 'WeekendExpressProGenerator', '周末速递', 'weekend_express'),
    ]
    
    generated = 0
    for module_name, class_name, desc, dir_name in reports:
        try:
            module = __import__(f'generators.{module_name}', fromlist=[class_name])
            gen_class = getattr(module, class_name)
            gen = gen_class(data_dir='data')
            
            if hasattr(gen, 'build_standard_report'):
                gen.build_standard_report()
            
            html = gen.render()
            
            # 保存 - 生成带日期的文件（latest.html 统一为列表页，由列表页生成器维护）
            output_dir = os.path.join(BASE_DIR, 'docs', dir_name)
            os.makedirs(output_dir, exist_ok=True)
            
            today = datetime.now().strftime('%Y%m%d')
            date_file = os.path.join(output_dir, f'{today}_{desc}.html')
            with open(date_file, 'w', encoding='utf-8') as f:
                f.write(html)
            
            print(f"✅ {desc}: {len(html):,} 字节 → {os.path.basename(date_file)}")
            generated += 1
            
        except Exception as e:
            print(f"❌ {desc}: {e}")
    
    print()
    print(f"✅ 成功生成 {generated}/{len(reports)} 个报告页面")
    return generated

def main():
    """主函数"""
    start_time = datetime.now()
    
    print()
    print("🚀 每日数据更新与页面生成脚本")
    print(f"🕐 开始时间: {start_time.strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    # 1. 更新所有数据
    market_data, portfolio_data, longhubang_data = update_all_data()
    
    # 2. 生成所有页面
    generated_pages = generate_all_pages()
    
    # 3. 同步数据
    sync_data_to_docs()
    
    # 4. 生成所有报告页面
    report_count = generate_all_reports()
    
    # 5. 生成所有列表页
    print()
    print("=" * 60)
    print("📋 生成所有列表页")
    print("=" * 60)
    print()
    
    from generators.list_page_pro import ListPageProGenerator, CHANNEL_CONFIGS
    
    list_count = 0
    list_channels = [
        'industry_chain', 'weekly_review', 'weekly_outlook',
        'weekend_express', 'tomorrow_catalyst', 's_level_catalyst',
        'monthly', 'daily', 'intraday', 'aftermarket'
    ]
    
    for ch in list_channels:
        try:
            if ch in CHANNEL_CONFIGS:
                gen = ListPageProGenerator(ch, docs_dir=os.path.join(BASE_DIR, 'docs'))
                gen.load_data()
                result = gen.publish()
                print(f"✅ {ch}: {result.get('file_count', 0)} 份报告")
                list_count += 1
        except Exception as e:
            print(f"❌ {ch}: {e}")
    
    print()
    print(f"✅ 成功生成 {list_count} 个列表页")
    
    # 6. Git提交部署
    git_success = git_commit_and_push()
    
    # 总结
    end_time = datetime.now()
    duration = (end_time - start_time).total_seconds()
    
    print()
    print("=" * 60)
    print("📋 更新完成总结")
    print("=" * 60)
    print(f"🕐 完成时间: {end_time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"⏱️  耗时: {duration:.1f} 秒")
    print(f"📊 市场数据: {'✅' if market_data else '❌'}")
    print(f"💼 持仓数据: {'✅' if portfolio_data else '❌'}")
    print(f"🐉 龙虎榜数据: {'✅' if longhubang_data else '❌'}")
    print(f"📄 数据页面: {len(generated_pages)} 个")
    print(f"📰 报告页面: {report_count} 个")
    print(f"📤 Git部署: {'✅' if git_success else '❌'}")
    print()
    
    return 0


if __name__ == '__main__':
    sys.exit(main())


