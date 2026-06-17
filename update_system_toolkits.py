#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
系统工具箱统一更新脚本 - Pro版
基于V3架构生成器，一键更新所有工具页面

支持的工具：
- 智能预警系统 (alert_system_pro)
- 智能选题助手 (topic_picker_pro)
- 持仓智能预警仪表盘 (portfolio_dashboard_pro)
- 预判验证中心 (prediction_center_pro)
- 周度进化报告 (weekly_evolution_pro)
- 题材健康度报告 (topic_health_pro)
- 板块热力图 (sector_heatmap_pro)
- 龙虎榜透视 (longhubang_pro)
- 首页 (home_page_pro)
- 工作流监控中心 (workflow_status_pro)
- 周三前瞻 (weekly_outlook_pro)
"""

import os
import sys
from datetime import datetime

# 基础路径
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
V3_DIR = os.path.join(BASE_DIR, 'v3')
DATA_DIR = os.path.join(BASE_DIR, 'data')
DOCS_DIR = os.path.join(BASE_DIR, 'docs')
CONFIG_DIR = os.path.join(BASE_DIR, 'config')

# 添加v3目录到路径
sys.path.insert(0, V3_DIR)

# ============================================================
# 工具函数
# ============================================================

def get_update_time():
    """获取当前更新时间字符串"""
    now = datetime.now()
    return now.strftime('%Y年%-m月%-d日 %H:%M')

# ============================================================
# 各工具更新函数
# ============================================================

def update_alert_system():
    """更新智能预警系统 - Pro版"""
    from generators.alert_system_pro import AlertSystemProGenerator
    
    print("📊 更新智能预警系统...")
    try:
        generator = AlertSystemProGenerator(data_dir=DATA_DIR)
        output_path = os.path.join(DOCS_DIR, '智能预警系统', 'index.html')
        result = generator.publish(output_path)
        print(f"   ✅ 更新完成")
        print(f"   输出路径: {output_path}")
        return True
    except Exception as e:
        print(f"   ❌ 更新失败: {e}")
        return False

def update_topic_picker():
    """更新智能选题助手 - Pro版"""
    from generators.topic_picker_pro import TopicPickerProGenerator
    
    print("🎯 更新智能选题助手...")
    try:
        generator = TopicPickerProGenerator(data_dir=DATA_DIR)
        output_path = os.path.join(DOCS_DIR, '智能选题助手', 'index.html')
        result = generator.publish(output_path)
        print(f"   ✅ 更新完成")
        print(f"   输出路径: {output_path}")
        return True
    except Exception as e:
        print(f"   ❌ 更新失败: {e}")
        return False

def update_portfolio_dashboard():
    """更新持仓智能预警仪表盘 - Pro版"""
    from generators.portfolio_dashboard_pro import PortfolioDashboardProGenerator
    
    print("💼 更新持仓智能预警仪表盘...")
    try:
        data_path = os.path.join(DATA_DIR, 'portfolio.json')
        generator = PortfolioDashboardProGenerator(data_path=data_path)
        output_path = os.path.join(DOCS_DIR, '持仓智能预警仪表盘', 'index.html')
        result = generator.publish(output_path)
        print(f"   ✅ 更新完成")
        print(f"   输出路径: {output_path}")
        return True
    except Exception as e:
        print(f"   ❌ 更新失败: {e}")
        return False

def update_prediction_center():
    """更新预判验证中心 - Pro版"""
    from generators.prediction_center_pro import PredictionCenterProGenerator
    
    print("🔮 更新预判验证中心...")
    try:
        generator = PredictionCenterProGenerator(data_dir=DATA_DIR)
        output_path = os.path.join(DOCS_DIR, '预判验证中心', 'index.html')
        result = generator.publish(output_path)
        print(f"   ✅ 更新完成")
        print(f"   输出路径: {output_path}")
        return True
    except Exception as e:
        print(f"   ❌ 更新失败: {e}")
        return False

def update_weekly_evolution():
    """更新周度进化报告 - Pro版"""
    from generators.weekly_evolution_pro import WeeklyEvolutionProGenerator
    
    print("📈 更新周度进化报告...")
    try:
        generator = WeeklyEvolutionProGenerator(data_dir=DATA_DIR)
        output_path = os.path.join(DOCS_DIR, '周度进化报告', 'index.html')
        result = generator.publish(output_path)
        print(f"   ✅ 更新完成")
        print(f"   输出路径: {output_path}")
        return True
    except Exception as e:
        print(f"   ❌ 更新失败: {e}")
        return False

def update_topic_health():
    """更新题材健康度报告 - Pro版"""
    from generators.topic_health_pro import TopicHealthProGenerator
    
    print("💚 更新题材健康度报告...")
    try:
        generator = TopicHealthProGenerator(data_dir=DATA_DIR)
        output_path = os.path.join(DOCS_DIR, '题材健康度报告', 'index.html')
        result = generator.publish(output_path)
        print(f"   ✅ 更新完成")
        print(f"   输出路径: {output_path}")
        return True
    except Exception as e:
        print(f"   ❌ 更新失败: {e}")
        return False

def update_sector_heatmap():
    """更新板块热力图 - Pro版"""
    from generators.sector_heatmap_pro import SectorHeatmapProGenerator
    
    print("🔥 更新板块热力图...")
    try:
        generator = SectorHeatmapProGenerator(data_dir=DATA_DIR)
        output_path = os.path.join(DOCS_DIR, '板块热力图', 'index.html')
        result = generator.publish(output_path)
        print(f"   ✅ 更新完成")
        print(f"   输出路径: {output_path}")
        return True
    except Exception as e:
        print(f"   ❌ 更新失败: {e}")
        return False

def update_longhubang():
    """更新龙虎榜透视 - Pro版"""
    from generators.longhubang_pro import LonghuBangProGenerator
    
    print("🐉 更新龙虎榜透视...")
    try:
        generator = LonghuBangProGenerator(data_dir=DATA_DIR)
        output_path = os.path.join(DOCS_DIR, '龙虎榜', 'index.html')
        result = generator.publish(output_path)
        print(f"   ✅ 更新完成")
        print(f"   输出路径: {output_path}")
        return True
    except Exception as e:
        print(f"   ❌ 更新失败: {e}")
        return False

def update_home_page():
    """更新首页 - Pro版"""
    from generators.home_page_pro import HomePageProGenerator
    
    print("🏠 更新首页...")
    try:
        generator = HomePageProGenerator(data_dir=DATA_DIR, config_dir=CONFIG_DIR)
        output_path = os.path.join(DOCS_DIR, 'index.html')
        result = generator.publish(output_path)
        print(f"   ✅ 更新完成")
        print(f"   输出路径: {output_path}")
        return True
    except Exception as e:
        print(f"   ❌ 更新失败: {e}")
        return False

def update_workflow_status():
    """更新工作流监控中心 - Pro版"""
    from generators.workflow_status_pro import WorkflowStatusProGenerator
    
    print("⚙️ 更新工作流监控中心...")
    try:
        generator = WorkflowStatusProGenerator(data_dir=DATA_DIR, config_dir=CONFIG_DIR)
        output_path = os.path.join(DOCS_DIR, 'workflow_status.html')
        result = generator.publish(output_path)
        print(f"   ✅ 更新完成")
        print(f"   输出路径: {output_path}")
        return True
    except Exception as e:
        print(f"   ❌ 更新失败: {e}")
        return False

def update_weekly_outlook():
    """更新周三前瞻 - Pro版"""
    from generators.weekly_outlook_pro import WeeklyOutlookProGenerator
    
    print("🔭 更新周三前瞻...")
    try:
        generator = WeeklyOutlookProGenerator(data_dir=DATA_DIR)
        output_path = os.path.join(DOCS_DIR, 'weekly_outlook', 'latest.html')
        result = generator.publish(output_path)
        print(f"   ✅ 更新完成")
        print(f"   输出路径: {output_path}")
        return True
    except Exception as e:
        print(f"   ❌ 更新失败: {e}")
        return False


def update_time_machine():
    """更新数据时光机 - Pro版"""
    from generators.time_machine_pro import TimeMachinePage
    
    print("⏰ 更新数据时光机...")
    try:
        generator = TimeMachinePage(data_dir=DATA_DIR)
        output_path = os.path.join(DOCS_DIR, '数据时光机', 'index.html')
        result = generator.publish(output_path)
        print(f"   ✅ 更新完成")
        print(f"   输出路径: {output_path}")
        return True
    except Exception as e:
        print(f"   ❌ 更新失败: {e}")
        return False

def update_industry_chain_clock():
    """更新产业链时钟 - Pro版"""
    from generators.industry_chain_pro import IndustryChainClockProGenerator
    
    print("🔗 更新产业链时钟...")
    try:
        generator = IndustryChainClockProGenerator(data_dir=DATA_DIR)
        generator.load_data()
        output_path = os.path.join(DOCS_DIR, '产业链时钟', 'index.html')
        result = generator.publish(output_path)
        print(f"   ✅ 更新完成")
        print(f"   输出路径: {output_path}")
        return True
    except Exception as e:
        print(f"   ❌ 更新失败: {e}")
        import traceback
        traceback.print_exc()
        return False

# ============================================================
# 工具映射表
# ============================================================

TOOL_MAP = {
    'alert': ('智能预警系统', update_alert_system),
    'topic': ('智能选题助手', update_topic_picker),
    'portfolio': ('持仓智能预警仪表盘', update_portfolio_dashboard),
    'prediction': ('预判验证中心', update_prediction_center),
    'evolution': ('周度进化报告', update_weekly_evolution),
    'health': ('题材健康度报告', update_topic_health),
    'heatmap': ('板块热力图', update_sector_heatmap),
    'longhubang': ('龙虎榜透视', update_longhubang),
    'home': ('首页', update_home_page),
    'workflow': ('工作流监控中心', update_workflow_status),
    'weekly_outlook': ('周三前瞻', update_weekly_outlook),
    'time_machine': ('数据时光机', update_time_machine),
    'industry_chain': ('产业链时钟', update_industry_chain_clock),
}

# ============================================================
# 主函数
# ============================================================

def main():
    if len(sys.argv) > 1:
        mode = sys.argv[1]
    else:
        mode = 'all'
    
    update_time = get_update_time()
    
    print("=" * 60)
    print("📊 系统工具箱更新脚本 v2.0 (Pro版)")
    print(f"⏰ 更新时间: {update_time}")
    print("=" * 60)
    print()
    
    success_count = 0
    total_count = 0
    
    if mode == 'all':
        # 更新所有工具
        for tool_key, (tool_name, update_func) in TOOL_MAP.items():
            total_count += 1
            if update_func():
                success_count += 1
            print()
    else:
        # 更新指定工具
        if mode in TOOL_MAP:
            total_count = 1
            tool_name, update_func = TOOL_MAP[mode]
            if update_func():
                success_count = 1
        else:
            print(f"❌ 未知的工具类型: {mode}")
            print(f"   支持的类型: {', '.join(TOOL_MAP.keys())}")
            print(f"   传入 'all' 更新全部")
            return 0
    
    print("=" * 60)
    print(f"✅ 更新完成，成功 {success_count}/{total_count} 个工具")
    print("=" * 60)
    
    return success_count

if __name__ == '__main__':
    main()
