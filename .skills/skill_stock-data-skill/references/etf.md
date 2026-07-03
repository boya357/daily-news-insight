# etf / etf-holdings / etf-nav — ETF 数据

## 用途

获取 ETF 基金的基本信息、持仓明细和净值历史数据。

## 数据源

腾讯自选股

## 调用

```bash
python3 ./bin/_cli_wrapper.py call etf --param code=sh510300
python3 ./bin/_cli_wrapper.py call etf-holdings --param code=sh510300
python3 ./bin/_cli_wrapper.py call etf-nav --param code=sh510300
```

## 入参

### etf — ETF 基本信息

| 参数 | 必填 | 类型 | 说明 |
|------|------|------|------|
| code | ✅ | string | ETF 代码，支持批量(逗号分隔)。如 sh510300, sz159919 |

### etf-holdings — ETF 持仓

| 参数 | 必填 | 类型 | 说明 |
|------|------|------|------|
| code | ✅ | string | ETF 代码，支持批量(逗号分隔) |

### etf-nav — ETF 净值

| 参数 | 必填 | 类型 | 说明 |
|------|------|------|------|
| code | ✅ | string | ETF 代码，支持批量(逗号分隔) |
| start | ❌ | string | 起始日期，格式 YYYY-MM-DD |
| end | ❌ | string | 结束日期，格式 YYYY-MM-DD |

## 返回字段

返回 Markdown 表格，字段随操作不同而变化。

### etf 返回

| 字段 | 类型 | 说明 |
|------|------|------|
| code | string | ETF 代码 |
| name | string | ETF 名称 |
| nav | float | 最新净值 |
| price | float | 最新价 |
| premium_rate | float | 溢价率(%) |
| volume | float | 成交量 |
| amount | float | 成交额 |

### etf-holdings 返回

| 字段 | 类型 | 说明 |
|------|------|------|
| stock_code | string | 持仓股票代码 |
| stock_name | string | 持仓股票名称 |
| weight | float | 持仓权重(%) |
| shares | float | 持仓股数 |

### etf-nav 返回

| 字段 | 类型 | 说明 |
|------|------|------|
| date | string | 日期 |
| nav | float | 单位净值 |
| acc_nav | float | 累计净值 |
| change_percent | float | 日涨跌幅(%) |

## 示例

```bash
# 沪深300ETF 基本信息
python3 ./bin/_cli_wrapper.py call etf --param code=sh510300
# ETF 持仓明细
python3 ./bin/_cli_wrapper.py call etf-holdings --param code=sh510300
# ETF 净值(指定日期范围)
python3 ./bin/_cli_wrapper.py call etf-nav --param code=sh510300 --param start=2024-01-01 --param end=2024-06-30
# 批量查询
python3 ./bin/_cli_wrapper.py call etf --param code=sh510300,sz159919
```
