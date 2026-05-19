# 实用示例集

## 快速开始

### 安装依赖

```bash
cd scripts/
pip install -r requirements.txt --break-system-packages
```

### 最简示例

```python
from scripts.yuan_data import get_stock_price

# 查询贵州茅台股价
quote = get_stock_price("sh600519")
if quote:
    print(f"{quote['name']}: ¥{quote['current_price']}")
```

## 场景化示例

### 场景1：自选股实时监控

```python
from scripts.yuan_data import YuanData
import time

def monitor_watchlist(stock_codes: list, interval: int = 60):
    """
    监控自选股列表

    Args:
        stock_codes: 股票代码列表
        interval: 刷新间隔(秒)
    """
    data = YuanData()

    while True:
        print("\n" + "="*50)
        print(f"📊 自选股监控 - {time.strftime('%Y-%m-%d %H:%M:%S')}")
        print("="*50 + "\n")

        for code in stock_codes:
            quote = data.stock.get_quote(code)
            if quote:
                emoji = "📈" if quote['change'] > 0 else "📉" if quote['change'] < 0 else "➖"
                print(f"{emoji} {quote['name']} ({quote['code']})")
                print(f"   当前: ¥{quote['current_price']:<8.2f} "
                      f"涨跌: {quote['change']:+.2f} ({quote['change_percent']:+.2f}%)")
                print(f"   今开: ¥{quote['open']:<8.2f} "
                      f"最高: ¥{quote['high']:<8.2f} "
                      f"最低: ¥{quote['low']:<8.2f}")
                print()
            time.sleep(0.2)

        time.sleep(interval)

# 使用示例
my_stocks = [
    "sh600519",  # 贵州茅台
    "sz000858",  # 五粮液
    "hk00700",   # 腾讯控股
    "sh601318",  # 中国平安
]

monitor_watchlist(my_stocks, interval=300)  # 每5分钟刷新
```

### 场景2：基金收益计算器

```python
from scripts.yuan_data import get_fund_nav

def calculate_fund_return(fund_code: str, buy_nav: float, shares: float):
    """
    计算基金收益

    Args:
        fund_code: 基金代码
        buy_nav: 买入时净值
        shares: 持有份额
    """
    fund = get_fund_nav(fund_code)
    if not fund:
        print("无法获取基金数据")
        return

    current_nav = fund['nav']
    current_value = current_nav * shares
    cost = buy_nav * shares
    profit = current_value - cost
    profit_rate = (current_nav - buy_nav) / buy_nav * 100

    print(f"{'='*50}")
    print(f"基金: {fund['name']}")
    print(f"代码: {fund['code']}")
    print(f"{'='*50}")
    print(f"买入净值: ¥{buy_nav:.4f}")
    print(f"当前净值: ¥{current_nav:.4f} ({fund['nav_date']})")
    print(f"持有份额: {shares:,.2f}")
    print(f"-" * 50)
    print(f"持仓成本: ¥{cost:,.2f}")
    print(f"当前市值: ¥{current_value:,.2f}")
    print(f"{'='*50}")

    if profit >= 0:
        print(f"✅ 盈利: ¥{profit:,.2f} (+{profit_rate:.2f}%)")
    else:
        print(f"❌亏损: ¥{profit:,.2f} ({profit_rate:.2f}%)")

    # 估算今日收益
    if fund['estimated_nav'] > 0:
        today_profit = (fund['estimated_nav'] - current_nav) * shares
        print(f"📊 今日预估: {'+' if today_profit >= 0 else ''}{today_profit:.2f} ({fund['growth_rate']:+.2f}%)")

# 使用示例
calculate_fund_return(
    fund_code="161039",
    buy_nav=1.5200,
    shares=10000
)
```

### 场景3：行业板块分析

```python
from scripts.yuan_data import YuanData
import time

def analyze_industry(industry_name: str, stock_codes: list):
    """
    分析行业板块表现

    Args:
        industry_name: 行业名称
        stock_codes: 该行业代表股票列表
    """
    data = YuanData()
    results = []

    for code in stock_codes:
        quote = data.stock.get_quote(code)
        if quote:
            results.append(quote)
        time.sleep(0.2)

    if not results:
        print("未获取到任何数据")
        return

    # 统计分析
    up_count = sum(1 for r in results if r['change'] > 0)
    down_count = sum(1 for r in results if r['change'] < 0)
    flat_count = len(results) - up_count - down_count
    avg_change = sum(r['change_percent'] for r in results) / len(results)

    # 找出涨跌幅前三
    sorted_by_change = sorted(results, key=lambda x: x['change_percent'], reverse=True)

    print(f"\n{'='*60}")
    print(f"📊 {industry_name} 板块分析")
    print(f"{'='*60}\n")

    print(f"样本数量: {len(results)} 只")
    print(f"上涨: {up_count} | 下跌: {down_count} | 平盘: {flat_count}")
    print(f"平均涨跌幅: {avg_change:+.2f}%\n")

    print(f"{'─'*60}")
    print("涨幅前三:")
    for i, stock in enumerate(sorted_by_change[:3], 1):
        print(f"{i}. {stock['name']} ({stock['code']}): {stock['change_percent']:+.2f}%")

    print(f"\n跌幅前三:")
    for i, stock in enumerate(sorted_by_change[-3:], 1):
        print(f"{i}. {stock['name']} ({stock['code']}): {stock['change_percent']:+.2f}%")

# 使用示例：白酒板块
liquor_stocks = [
    "sh600519",  # 贵州茅台
    "sz000858",  # 五粮液
    "sz000568",  # 泸州老窖
    "sz000799",  # 酒鬼酒
    "sh603369",  # 今世缘
]

analyze_industry("白酒", liquor_stocks)
```

### 场景4：宏观经济仪表盘

```python
from scripts.yuan_data import YuanData

def economic_dashboard():
    """展示宏观经济数据仪表盘"""
    data = YuanData()

    print("\n" + "="*70)
    print(" "*20 + "🇨🇳 中国宏观经济数据")
    print("="*70 + "\n")

    # GDP
    gdp_list = data.macro.get_gdp(page_size=2)
    if gdp_list:
        latest_gdp = gdp_list[0]
        print("【国内生产总值 GDP】")
        print(f"  报告期: {latest_gdp['TIME']}")
        print(f"  GDP总值: {latest_gdp['DOMESTICL_PRODUCT_BASE']} 万亿元")
        print(f"  同比增速: {latest_gdp['SUM_SAME']}%")

        if len(gdp_list) > 1:
            prev_gdp = gdp_list[1]
            print(f"  环比增速: {float(latest_gdp['DOMESTICL_PRODUCT_BASE']) - float(prev_gdp['DOMESTICL_PRODUCT_BASE']):.2f} 万亿")
        print()

    # CPI
    cpi_list = data.macro.get_cpi(page_size=12)
    if cpi_list:
        latest_cpi = cpi_list[0]
        print("【居民消费价格指数 CPI】")
        print(f"  报告期: {latest_cpi['TIME']}")
        print(f"  全国同比: {latest_cpi['NATIONAL_SAME']}%")
        print(f"  全国环比: {latest_cpi['NATIONAL_BASE']}%")

        # 近12个月趋势
        trend = [float(item['NATIONAL_SAME']) for item in cpi_list[:12]]
        avg_cpi = sum(trend) / len(trend)
        print(f"  近12月均值: {avg_cpi:.2f}%")
        print()

    # PPI
    ppi_list = data.macro.get_ppi(page_size=1)
    if ppi_list:
        latest_ppi = ppi_list[0]
        print("【工业生产者出厂价格指数 PPI】")
        print(f"  报告期: {latest_ppi['TIME']}")
        print(f"  同比涨幅: {latest_ppi['BASE_SAME']}%")
        print()

    # PMI
    pmi_list = data.macro.get_pmi(page_size=1)
    if pmi_list:
        latest_pmi = pmi_list[0]
        print("【采购经理指数 PMI】")
        print(f"  报告期: {latest_pmi['TIME']}")
        print(f"  制造业PMI: {latest_pmi['MAKE_INDEX']}")

        if float(latest_pmi['MAKE_INDEX']) > 50:
            print(f"  景气度: 扩张区间 ✅")
        elif float(latest_pmi['MAKE_INDEX']) < 50:
            print(f"  景气度: 收缩区间 ⚠️")
        else:
            print(f"  景气度: 临界点")

        print(f"  非制造业PMI: {latest_pmi['NMAKE_INDEX']}")
        print()

    print("="*70)

# 运行仪表盘
economic_dashboard()
```

### 场景5：财经新闻推送

```python
from scripts.yuan_data import YuanData
import time

def news_alert(keywords: list, check_interval: int = 300):
    """
    关键词新闻推送

    Args:
        keywords: 关键词列表
        check_interval: 检查间隔(秒)
    """
    data = YuanData()
    seen_titles = set()

    while True:
        for keyword in keywords:
            news_list = data.news.search(keyword, limit=5)

            for news in news_list:
                title = news['title']
                if title not in seen_titles:
                    print(f"🔔 [{keyword}] {title}")
                    seen_titles.add(title)

            time.sleep(1)

        print(f"\n⏰ 下次检查: {check_interval}秒后...")
        time.sleep(check_interval)

# 使用示例
news_alert(
    keywords=["央行", "降息", "A股", "茅台"],
    check_interval=600  # 每10分钟检查
)
```

### 场景6：简易量化回测准备

```python
from scripts.yuan_data import YuanData
import json

def collect_historical_data(stock_codes: list, output_file: str):
    """
    收集多只股票数据用于回测
    (注意: 当前仅获取实时数据，历史数据需其他接口)

    Args:
        stock_codes: 股票代码列表
        output_file: 输出JSON文件路径
    """
    data = YuanData()
    results = []

    for code in stock_codes:
        quote = data.stock.get_quote(code)
        if quote:
            results.append(quote)

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    print(f"✅ 已保存 {len(results)} 只股票数据到 {output_file}")

# 使用示例
collect_historical_data(
    stock_codes=["sh600519", "sz000858", "hk00700"],
    output_file="stock_snapshot.json"
)
```

## 高级技巧

### 技巧1：错误重试机制

```python
import time

def get_with_retry(func, *args, max_retries=3, **kwargs):
    """带重试的数据获取"""
    for attempt in range(max_retries):
        try:
            result = func(*args, **kwargs)
            if result:
                return result
        except Exception as e:
            print(f"尝试 {attempt + 1}/{max_retries} 失败: {e}")

        if attempt < max_retries - 1:
            time.sleep(2 ** attempt)  # 指数退避

    return None

# 使用
quote = get_with_retry(get_stock_price, "sh600519")
```

### 技巧2：并发查询(需安装 `concurrent.futures`)

```python
from concurrent.futures import ThreadPoolExecutor
from scripts.yuan_data import get_stock_price

def batch_query(stock_codes: list, max_workers: int = 5):
    """并发批量查询"""
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        results = list(executor.map(get_stock_price, stock_codes))
    return [r for r in results if r is not None]

# 使用
codes = ["sh600519", "sz000858", "hk00700", "sh601318"]
quotes = batch_query(codes)
for q in quotes:
    print(f"{q['name']}: {q['current_price']}")
```

### 技巧3：数据缓存

```python
import time
from functools import lru_cache

@lru_cache(maxsize=128)
def cached_stock_price(code: str, timestamp: int):
    """带时间戳的缓存查询"""
    return get_stock_price(code)

# 使用 (每分钟刷新缓存)
current_minute = int(time.time() // 60)
quote = cached_stock_price("sh600519", current_minute)
```

## 注意事项

1. **请求频率**：在循环中添加适当延迟，避免被封IP
2. **异常处理**：所有接口都可能返回 `None`，务必检查
3. **数据时效**：实时数据有延迟，不可用于高频交易
4. **合规使用**：仅用于个人学习研究，不可商业化
