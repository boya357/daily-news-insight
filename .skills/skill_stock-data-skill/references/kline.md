# kline — 历史K线数据

## 用途

获取股票的历史K线数据（OHLCV），支持日线/周线/月线/分钟线，支持前复权/后复权。

## 数据源

东方财富(主) → 腾讯行情(备)

## 调用

```bash
python3 ./scripts/stock_query.py call kline --param code=sh600519 --param period=day --param count=60
```

## 入参

| 参数 | 必填 | 类型 | 默认 | 说明 |
|------|------|------|------|------|
| code | ✅ | string | — | 股票代码 |
| period | ❌ | string | day | K线周期：day/week/month/1min/5min/15min/30min/60min |
| fq | ❌ | string | qfq | 复权类型：qfq=前复权, hfq=后复权, none=不复权 |
| begin | ❌ | string | — | 开始日期 YYYYMMDD |
| end | ❌ | string | — | 结束日期 YYYYMMDD |
| count | ❌ | int | 120 | 返回条数（1-500） |

## 返回字段

| 字段 | 类型 | 说明 |
|------|------|------|
| code | string | 股票代码 |
| period | string | K线周期 |
| fq | string | 复权类型 |
| count | int | 实际返回条数 |
| data[] | array | K线数组 |
| data[].date | string | 日期 |
| data[].open | float | 开盘价 |
| data[].close | float | 收盘价 |
| data[].high | float | 最高价 |
| data[].low | float | 最低价 |
| data[].volume | float | 成交量 |
| data[].amount | float | 成交额 |
| source | string | 数据源 |

## 示例

```bash
# 日线，最近60天
python3 ./scripts/stock_query.py call kline --param code=sh600519 --param count=60

# 周线
python3 ./scripts/stock_query.py call kline --param code=sh600519 --param period=week --param count=52

# 5分钟线
python3 ./scripts/stock_query.py call kline --param code=sh600519 --param period=5min --param count=100

# 后复权
python3 ./scripts/stock_query.py call kline --param code=sh600519 --param fq=hfq

# 指定日期范围
python3 ./scripts/stock_query.py call kline --param code=sh600519 --param begin=20260101 --param end=20260513
```
