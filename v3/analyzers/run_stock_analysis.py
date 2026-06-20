#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
个股分析Skill集成脚本
调用 stock-analysis Skill 进行完整的个股技术分析
支持批量分析、数据格式转换、结果存储

用法: python3 scripts/run_stock_analysis.py --stocks 002837,301217,002409,002789
"""

import os
import sys
import json
import time
import argparse
import subprocess
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Optional

# Skill脚本路径
SKILL_DIR = Path("/app/data/所有对话/主对话/.skills/skill_stock-analysis")
FETCH_SCRIPT = SKILL_DIR / "scripts/fetch_stock_data.py"
ANALYZE_SCRIPT = SKILL_DIR / "scripts/analyze_stock.py"

# 项目数据目录
PROJECT_DIR = Path("/root/daily-news-insight")
DATA_DIR = PROJECT_DIR / "data" / "stock_analysis"
DOCS_DATA_DIR = PROJECT_DIR / "docs" / "data" / "stock_analysis"


def run_command(cmd: List[str], cwd: str = None) -> Dict:
    """执行命令并返回结果"""
    try:
        result = subprocess.run(
            cmd,
            cwd=cwd,
            capture_output=True,
            text=True,
            timeout=60
        )
        return {
            "success": result.returncode == 0,
            "stdout": result.stdout,
            "stderr": result.stderr,
            "returncode": result.returncode
        }
    except subprocess.TimeoutExpired:
        return {"success": False, "error": "timeout", "stdout": "", "stderr": "Command timed out"}
    except Exception as e:
        return {"success": False, "error": str(e), "stdout": "", "stderr": str(e)}


def fetch_stock_data(stock_code: str, days: int = 60) -> Optional[Dict]:
    """获取股票行情数据"""
    cmd = [
        sys.executable, str(FETCH_SCRIPT),
        "--stock_code", stock_code,
        "--days", str(days)
    ]
    result = run_command(cmd, cwd=str(SKILL_DIR))
    
    if not result["success"]:
        print(f"  ❌ 获取行情失败: {result.get('error', result['stderr'])}")
        return None
    
    # 从输出中提取数据文件路径
    output = result["stdout"]
    data_file = None
    for line in output.split("\n"):
        if "数据已保存到" in line or "数据文件" in line:
            parts = line.split(":")
            if len(parts) >= 2:
                potential_path = parts[-1].strip()
                if os.path.exists(potential_path):
                    data_file = potential_path
                elif os.path.exists(str(SKILL_DIR / potential_path)):
                    data_file = str(SKILL_DIR / potential_path)
    
    # 如果没找到路径，尝试默认位置
    if not data_file:
        default_path = SKILL_DIR / f"stock_data_{stock_code}.json"
        if default_path.exists():
            data_file = str(default_path)
    
    if data_file and os.path.exists(data_file):
        with open(data_file, "r", encoding="utf-8") as f:
            return json.load(f)
    
    print(f"  ⚠️  无法找到数据文件")
    return None


def analyze_stock(stock_code: str) -> Optional[Dict]:
    """执行技术分析"""
    data_file = SKILL_DIR / f"stock_data_{stock_code}.json"
    if not data_file.exists():
        print(f"  ❌ 数据文件不存在: {data_file}")
        return None
    
    cmd = [
        sys.executable, str(ANALYZE_SCRIPT),
        "--data_file", str(data_file),
        "--output", str(SKILL_DIR / f"analysis_{stock_code}.json")
    ]
    result = run_command(cmd, cwd=str(SKILL_DIR))
    
    if not result["success"]:
        print(f"  ❌ 技术分析失败: {result.get('error', result['stderr'])}")
        return None
    
    output_file = SKILL_DIR / f"analysis_{stock_code}.json"
    if output_file.exists():
        with open(output_file, "r", encoding="utf-8") as f:
            return json.load(f)
    
    print(f"  ⚠️  无法找到分析结果文件")
    return None


def convert_to_system_format(skill_data: Dict, stock_code: str, stock_name: str) -> Dict:
    """将Skill输出格式转换为系统标准格式"""
    
    result = {
        "code": stock_code,
        "name": stock_name,
        "sector": "",
        "business": "",
        "analyze_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "data_source": "stock-analysis Skill v2.1 (新浪财经)",
        "update_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    
    tech = skill_data.get("technical_indicators", {})
    current_price = skill_data.get("current_price", 0)
    
    result["market"] = {
        "current_price": current_price,
        "change_pct": 0,
        "change_amount": 0,
        "volume": skill_data.get("volume_analysis", {}).get("volume_hands", 0),
        "turnover_rate": 0,
        "amount": 0,
        "high": 0,
        "low": 0,
        "open": 0,
        "prev_close": 0
    }
    
    support = skill_data.get("support_resistance", {})
    support_levels = support.get("support_levels", [])
    resistance_levels = support.get("resistance_levels", [])
    
    gap = skill_data.get("gap_analysis", {})
    down_gaps = gap.get("down_gaps", [])
    up_gaps = gap.get("up_gaps", [])
    
    trend = skill_data.get("trend_analysis", {})
    volume = skill_data.get("volume_analysis", {})
    
    macd = tech.get("macd", {})
    rsi = tech.get("rsi", {})
    
    tech_score = calc_technical_score(tech, current_price, trend, volume, support_levels, resistance_levels)
    
    result["technical"] = {
        "score": tech_score,
        "rating": get_rating(tech_score),
        "ma5": tech.get("ma5", 0),
        "ma10": tech.get("ma10", 0),
        "ma20": tech.get("ma20", 0),
        "ma60": tech.get("ma60", 0),
        "macd": {
            "dif": macd.get("dif", 0),
            "dea": macd.get("dea", 0),
            "macd": macd.get("macd", 0),
            "signal": macd.get("signal", "")
        },
        "rsi": {
            "value": rsi.get("value", 0),
            "signal": rsi.get("signal", "")
        },
        "support_levels": support_levels,
        "resistance_levels": resistance_levels,
        "gaps": {
            "up_gaps": up_gaps,
            "down_gaps": down_gaps
        },
        "trend": {
            "direction": trend.get("trend", ""),
            "strength": trend.get("strength", ""),
            "description": trend.get("description", "")
        },
        "volume": {
            "volume_hands": volume.get("volume_hands", 0),
            "volume_ratio": volume.get("volume_ratio", 0),
            "signal": volume.get("signal", ""),
            "description": volume.get("description", "")
        }
    }
    
    result["overall"] = {
        "score": tech_score,
        "rating": get_rating(tech_score),
        "price": current_price,
        "change_pct": 0
    }
    
    result["fundamental"] = {}
    result["themes"] = []
    result["news"] = []
    result["trader"] = {}
    
    return result


def calc_technical_score(tech: Dict, current_price: float, trend: Dict, volume: Dict,
                         supports: List, resistances: List) -> float:
    """计算技术面得分 (0-100)"""
    score = 50
    
    ma5 = tech.get("ma5", 0)
    ma10 = tech.get("ma10", 0)
    ma20 = tech.get("ma20", 0)
    ma60 = tech.get("ma60", 0)
    
    if ma5 and ma10 and ma20:
        if ma5 > ma10 > ma20:
            score += 15
        elif ma5 > ma10:
            score += 8
        elif ma5 < ma10 < ma20:
            score -= 15
        elif ma5 < ma10:
            score -= 8
    
    macd = tech.get("macd", {})
    if macd:
        macd_val = macd.get("macd", 0)
        signal = macd.get("signal", "")
        if macd_val > 0 and "红柱放大" in signal:
            score += 15
        elif macd_val > 0:
            score += 8
        elif macd_val < 0 and "绿柱放大" in signal:
            score -= 15
        elif macd_val < 0:
            score -= 8
    
    rsi = tech.get("rsi", {})
    if rsi:
        rsi_val = rsi.get("value", 50)
        if rsi_val > 70:
            score -= 5
        elif rsi_val < 30:
            score += 10
        elif 40 <= rsi_val <= 60:
            score += 3
    
    trend_dir = trend.get("trend", "")
    trend_str = trend.get("strength", "")
    if "上升" in trend_dir or "上涨" in trend_dir:
        score += 10 if trend_str == "强" else 5
    elif "下降" in trend_dir or "下跌" in trend_dir:
        score -= 10 if trend_str == "强" else 5
    elif "缠绕" in trend_dir or "整理" in trend_dir:
        score -= 3
    
    vol_signal = volume.get("signal", "")
    if "放量" in vol_signal or "正常" in vol_signal:
        score += 5
    elif "缩量" in vol_signal:
        score -= 3
    
    if current_price and supports:
        first_support = supports[0].get("price", 0) if supports else 0
        if first_support and current_price > first_support * 0.95:
            score += 5
    if current_price and resistances:
        first_resistance = resistances[0].get("price", 0) if resistances else 0
        if first_resistance and current_price < first_resistance * 1.05:
            score -= 5
    
    return max(0, min(100, round(score, 1)))


def get_rating(score: float) -> str:
    """根据分数获取评级"""
    if score >= 80:
        return "强烈推荐"
    elif score >= 65:
        return "推荐"
    elif score >= 50:
        return "中性"
    elif score >= 35:
        return "谨慎"
    else:
        return "回避"


def save_result(data: Dict, stock_code: str):
    """保存分析结果到数据目录"""
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    data_path = DATA_DIR / f"{stock_code}.json"
    with open(data_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    DOCS_DATA_DIR.mkdir(parents=True, exist_ok=True)
    docs_path = DOCS_DATA_DIR / f"{stock_code}.json"
    with open(docs_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"  ✅ 结果已保存: {docs_path}")


def analyze_single_stock(stock_code: str, stock_name: str = "") -> bool:
    """分析单只股票"""
    print(f"\n📊 分析 {stock_name} ({stock_code})...")
    
    print(f"  1/3 获取行情数据...")
    raw_data = fetch_stock_data(stock_code)
    if not raw_data:
        return False
    
    if not stock_name:
        stock_name = raw_data.get("stock_name", "")
    
    print(f"  2/3 技术分析...")
    analysis = analyze_stock(stock_code)
    if not analysis:
        return False
    
    if "current_price" not in analysis:
        realtime = raw_data.get("realtime", {})
        if isinstance(realtime, dict):
            analysis["current_price"] = realtime.get("price", 0)
    
    print(f"  3/3 格式转换并保存...")
    system_data = convert_to_system_format(analysis, stock_code, stock_name)
    save_result(system_data, stock_code)
    
    score = system_data.get("technical", {}).get("score", 0)
    rating = system_data.get("technical", {}).get("rating", "")
    print(f"  🎯 技术评分: {score}分 - {rating}")
    
    return True


def main():
    parser = argparse.ArgumentParser(description="个股分析Skill集成脚本")
    parser.add_argument("--stocks", type=str, default="002837,301217,002409,002789",
                        help="股票代码列表，逗号分隔")
    parser.add_argument("--days", type=int, default=60, help="历史数据天数")
    args = parser.parse_args()
    
    stock_codes = [s.strip() for s in args.stocks.split(",") if s.strip()]
    
    print("=" * 60)
    print("🚀 个股分析Skill批量执行")
    print(f"📅 时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"📈 股票数量: {len(stock_codes)}只")
    print("=" * 60)
    
    stock_names = {
        "002837": "英维克",
        "301217": "铜冠铜箔",
        "002409": "雅克科技",
        "002789": "*ST建艺",
        "000021": "深科技",
        "002230": "科大讯飞",
        "300750": "宁德时代",
        "600519": "贵州茅台",
    }
    
    success_count = 0
    fail_count = 0
    
    for code in stock_codes:
        name = stock_names.get(code, code)
        try:
            if analyze_single_stock(code, name):
                success_count += 1
            else:
                fail_count += 1
        except Exception as e:
            print(f"  ❌ 异常: {e}")
            fail_count += 1
    
    print("\n" + "=" * 60)
    print("📊 执行结果")
    print(f"  成功: {success_count}只")
    print(f"  失败: {fail_count}只")
    print(f"  数据目录: {DOCS_DATA_DIR}")
    print("=" * 60)
    
    return fail_count == 0


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)


def fetch_news(stock_name: str, stock_code: str, limit: int = 10) -> List[Dict]:
    """
    获取股票相关新闻（基于搜索工具）
    注意：此函数需要在有搜索能力的环境中运行
    这里提供框架，实际调用通过子进程或API完成
    """
    # 占位实现：返回空列表，实际由外部调用填充
    # 完整实现需要调用搜索工具，然后做情绪分析
    return []


def analyze_news_sentiment(news_list: List[Dict]) -> Dict:
    """
    分析新闻情绪
    输入格式: [{"title": "...", "source": "...", "time": "...", "content": "..."}]
    """
    if not news_list:
        return {
            "total": 0,
            "positive": 0,
            "negative": 0,
            "neutral": 0,
            "sentiment_score": 50,
            "impact": "中性",
            "key_news": []
        }
    
    # 关键词匹配的情绪分析
    positive_keywords = [
        "增长", "上涨", "利好", "突破", "新高", "盈利", "业绩增长",
        "订单", "合作", "获批", "通过", "认证", "投产", "上线",
        "增持", "回购", "超预期", "利好", "涨价", "供不应求"
    ]
    negative_keywords = [
        "下跌", "亏损", "利空", "风险", "警示", "处罚", "违规",
        "减持", "解禁", "爆雷", "不及预期", "下滑", "下降",
        "诉讼", "调查", "召回", "停产", "事故"
    ]
    
    positive = 0
    negative = 0
    neutral = 0
    key_news = []
    
    for news in news_list:
        title = news.get("title", "")
        content = news.get("content", "")
        text = title + " " + content
        
        pos_count = sum(1 for kw in positive_keywords if kw in text)
        neg_count = sum(1 for kw in negative_keywords if kw in text)
        
        if pos_count > neg_count:
            positive += 1
            news["sentiment"] = "positive"
        elif neg_count > pos_count:
            negative += 1
            news["sentiment"] = "negative"
        else:
            neutral += 1
            news["sentiment"] = "neutral"
        
        # 前3条作为关键新闻
        if len(key_news) < 3:
            key_news.append({
                "title": title,
                "source": news.get("source", ""),
                "time": news.get("time", ""),
                "sentiment": news["sentiment"]
            })
    
    total = len(news_list)
    if total > 0:
        sentiment_score = round(50 + (positive - negative) / total * 25, 1)
    else:
        sentiment_score = 50
    
    # 影响判断
    if sentiment_score >= 70:
        impact = "正面偏强"
    elif sentiment_score >= 60:
        impact = "偏正面"
    elif sentiment_score >= 40:
        impact = "中性"
    elif sentiment_score >= 30:
        impact = "偏负面"
    else:
        impact = "负面偏强"
    
    return {
        "total": total,
        "positive": positive,
        "negative": negative,
        "neutral": neutral,
        "sentiment_score": sentiment_score,
        "impact": impact,
        "key_news": key_news
    }
