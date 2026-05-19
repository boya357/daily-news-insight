# 股票数据API参考

## 数据源

本技能支持多个股票数据源，按推荐顺序排列：

1. **新浪财经** (首选) - 实时性好，稳定性高
2. **腾讯财经** (备用) - 数据字段丰富
3. **东方财富** (备用) - 可通过网页抓取补充

## 新浪财经接口

### 基本用法

```python
from scripts.yuan_data import get_stock_price

# 获取A股行情
moutai = get_stock_price("sh600519")
print(f"{moutai['name']}: ¥{moutai['current_price']}")

# 获取港股行情
tencent = get_stock_price("hk00700")
print(f"{tencent['name']}: HK${tencent['current_price']}")
```

### 返回数据字段

| 字段名 | 类型 | 说明 | 示例 |
|--------|------|------|------|
| `code` | str | 股票代码 | "sh600519" |
| `name` | str | 股票名称 | "贵州茅台" |
| `current_price` | float | 当前价格 | 1685.00 |
| `open` | float | 开盘价 | 1670.00 |
| `high` | float | 最高价 | 1698.50 |
| `low` | float | 最低价 | 1665.00 |
| `pre_close` | float | 昨收价 | 1646.30 |
| `volume` | int | 成交量(股) | 1258000 |
| `amount` | float | 成交额(元) | 2115430000 |
| `change` | float | 涨跌额 | 38.70 |
| `change_percent` | float | 涨跌幅(%) | 2.35 |
| `date` | str | 日期 | "2026-02-12" |
| `time` | str | 时间 | "15:00:03" |

### 港股特殊说明

港股代码**必须是5位数字**，不足需补零：

```python
# ❌ 错误
get_stock_price("hk700")     # 缺少前导零

# ✅ 正确
get_stock_price("hk00700")   # 腾讯控股
get_stock_price("hk09988")   # 阿里巴巴
```

自动修正逻辑已内置在 `_StockAPI.get_quote()` 中。

## 腾讯财经接口（备用）

如果新浪接口失效，可尝试腾讯接口：

```python
data = YuanData()
# 需要修改 yuan_data.py 以支持选择数据源
```

腾讯接口返回字段略有不同，但包含额外的市盈率、换手率等数据。

## 东方财富网页抓取（备用）

通过 BeautifulSoup 解析东方财富网页：

```python
from bs4 import BeautifulSoup

# 访问 https://quote.eastmoney.com/sh600519.html
# 抓取页面中的价格信息
```

适用于需要更详细财务数据的场景。

## 错误处理

接口可能返回 `None`，需要妥善处理：

```python
quote = get_stock_price("sh600519")
if quote:
    print(f"价格: {quote['current_price']}")
else:
    print("获取失败，可能原因：")
    print("1. 股票代码错误")
    print("2. 股票停牌")
    print("3. 网络连接问题")
```

## 常见股票代码

### 沪市主板 (sh6xxxxx)

| 代码 | 名称 | 行业 |
|------|------|------|
| sh600000 | 浦发银行 | 银行 |
| sh600519 | 贵州茅台 | 白酒 |
| sh600036 | 招商银行 | 银行 |
| sh601318 | 中国平安 | 保险 |
| sh601888 | 中国中免 | 零售 |

### 深市主板/中小板 (sz000xxx, sz002xxx)

| 代码 | 名称 | 行业 |
|------|------|------|
| sz000001 | 平安银行 | 银行 |
| sz000858 | 五粮液 | 白酒 |
| sz002594 | 比亚迪 | 新能源汽车 |
| sz002475 | 立讯精密 | 电子 |

### 科创板 (sh688xxx)

| 代码 | 名称 | 行业 |
|------|------|------|
| sh688981 | 中芯国际 | 半导体 |
| sh688599 | 天合光能 | 光伏 |

### 港股 (hk0xxxx)

| 代码 | 名称 | 行业 |
|------|------|------|
| hk00700 | 腾讯控股 | 互联网 |
| hk09988 | 阿里巴巴 | 电商 |
| hk03690 | 美团 | 本地生活 |
| hk01211 | 比亚迪 | 新能源汽车 |
| hk02318 | 中国平安 | 保险 |

## 性能优化建议

1. **批量查询**：如需查询多只股票，在每次请求间加入0.1-0.5秒延迟
2. **缓存机制**：同一股票短时间内无需重复查询
3. **并发控制**：避免同时发起大量请求
4. **错误重试**：网络波动时自动重试2-3次

```python
import time

codes = ["sh600519", "sh600036", "sz000858"]
results = []

for code in codes:
    quote = get_stock_price(code)
    if quote:
        results.append(quote)
    time.sleep(0.2)  # 避免请求过快
```
