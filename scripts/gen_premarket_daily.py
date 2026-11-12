#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""盘前每日新闻洞察一键生成脚本（每天8:00执行）
流程：
1. 采集隔夜美股数据
2. 采集A股盘前数据（持仓/行情）
3. 生成DailyReportPro带作战计划
4. 更新列表页 + latest.html
5. 自动git提交 + 企业微信推送
"""
import sys, os, shutil, subprocess
from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
os.chdir(BASE_DIR)
sys.path.insert(0, str(BASE_DIR / 'v3'))

def run(cmd, desc, timeout=180):
    print(f"\n{'='*60}\n▶ {desc}\n{'='*60}")
    r = subprocess.run(cmd, shell=True, cwd=BASE_DIR, capture_output=True, text=True, timeout=timeout)
    if r.stdout: print(r.stdout[-2000:])
    if r.returncode != 0:
        print(f"❌ {desc} 失败 (exit={r.returncode}): {r.stderr[-500:]}")
        return False
    return True

def main():
    today = datetime.now()
    # 周末跳过
    if today.weekday() >= 5:
        print(f"今天是{today.strftime('%A')}，非交易日，跳过")
        return 0
    date_str = today.strftime('%Y-%m-%d')
    date_compact = today.strftime('%Y%m%d')
    weekday_names = ['周一','周二','周三','周四','周五','周六','周日']
    weekday = weekday_names[today.weekday()]
    output_file = f"docs/daily/{date_compact}_每日新闻洞察.html"
    
    print(f"🚀 盘前日报生成 {date_str} {weekday}")
    
    # Step 1: 采集全球市场（隔夜美股）
    run("python3 scripts/fetch_global_market.py", "采集隔夜美股数据", 60)
    
    # Step 2: 采集A股盘前数据（持仓行情）
    run("python3 scripts/fetch_market_data.py", "采集A股盘前数据", 120)
    
    # Step 3: 生成日报
    print(f"\n{'='*60}\n▶ 生成每日新闻洞察（含作战计划）\n{'='*60}")
    from generators.daily_pro import DailyReportProGenerator
    subtitle = f"{today.strftime('%Y.%m.%d')} · {weekday} · 每日新闻洞察（盘前作战计划）"
    gen = DailyReportProGenerator(date_str, subtitle, data_dir=str(BASE_DIR/'data'))
    gen.build_standard_report()
    result = gen.publish(output_file)
    if not result.get('success'):
        print(f"❌ 生成失败: {result}")
        return 1
    size = result.get('file_size', 0)
    print(f"✅ 生成完成: {output_file} ({size} bytes)")
    
    # Step 4: 更新latest.html
    shutil.copy(output_file, "docs/daily/latest.html")
    print("✅ latest.html 已更新")
    
    # Step 5: 更新列表页
    try:
        from generators.list_page_pro import ListPageProGenerator
        lg = ListPageProGenerator('daily', docs_dir=str(BASE_DIR/'docs'))
        lg.load_data()
        lr = lg.publish()
        print(f"✅ daily列表页已更新（{lr.get('file_count')}份）")
    except Exception as e:
        print(f"⚠️  列表页更新失败: {e}")
    
    # Step 6: 校验
    ok = run("bash validate_system.sh 2>&1 | tail -5", "系统校验", 120)
    
    # Step 7: Git提交
    print(f"\n{'='*60}\n▶ Git提交\n{'='*60}")
    subprocess.run("git add -A", shell=True, cwd=BASE_DIR, capture_output=True)
    # 检查是否有变更
    diff = subprocess.run("git status --porcelain", shell=True, cwd=BASE_DIR, capture_output=True, text=True)
    if diff.stdout.strip():
        commit_msg = f"daily: 盘前日报 {date_str}（含今日作战计划）"
        subprocess.run(f'git commit -m "{commit_msg}"', shell=True, cwd=BASE_DIR, capture_output=True, timeout=30)
        subprocess.run("git push origin main", shell=True, cwd=BASE_DIR, capture_output=True, timeout=60)
        print("✅ 已提交并推送到GitHub")
    else:
        print("ℹ️  无变更需要提交")
    
    # Step 8: 企业微信推送
    url = "https://boya357.github.io/daily-news-insight/daily/latest.html"
    title = f"📰 {today.strftime('%m/%d')} {weekday} 每日新闻洞察·盘前作战计划"
    run(f'python3 simple_push.py "{url}" "{title}"', "企业微信推送", 30)
    
    print(f"\n🎉 盘前日报完成: {url}")
    return 0

if __name__ == '__main__':
    sys.exit(main())
