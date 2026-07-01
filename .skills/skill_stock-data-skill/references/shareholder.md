# shareholder / dividend / chip — 股东/分红/筹码

## 用途

获取上市公司股东持股信息、历史分红数据和筹码分布情况。

## 数据源

腾讯自选股

## 调用

```bash
python3 ./scripts/stock_query.py call shareholder --param code=sh600519
python3 ./scripts/stock_query.py call dividend --param code=sh600519
python3 ./scripts/stock_query.py call chip --param code=sh600519
```

## 入参

### shareholder — 股东持股

| 参数 | 必填 | 类型 | 说明 |
|------|------|------|------|
| code | ✅ | string | 股票代码(仅A股和港股)。A股: sh600519; 港股: hk00700 |

### dividend — 分红派息

| 参数 | 必填 | 类型 | 说明 |
|------|------|------|------|
| code | ✅ | string | 股票代码 |
| years | ❌ | int | 返回最近N年的分红记录 |
| all | ❌ | flag | 传入则返回全部历史分红记录 |

### chip — 筹码分布

| 参数 | 必填 | 类型 | 说明 |
|------|------|------|------|
| code | ✅ | string | 股票代码(仅沪深京A股)。如 sh600519, sz000001 |
| start | ❌ | string | 起始日期，格式 YYYY-MM-DD |
| end | ❌ | string | 结束日期，格式 YYYY-MM-DD |

## 返回字段

返回 Markdown 表格，字段随操作不同而变化。

### shareholder 返回

| 字段 | 类型 | 说明 |
|------|------|------|
| rank | int | 排名 |
| holder_name | string | 股东名称 |
| hold_num | float | 持股数量(万股) |
| hold_ratio | float | 持股比例(%) |
| change | string | 较上期增减 |
| report_date | string | 报告期 |

### dividend 返回

| 字段 | 类型 | 说明 |
|------|------|------|
| year | string | 年度 |
| plan | string | 分红方案 |
| ex_date | string | 除权除息日 |
| record_date | string | 股权登记日 |
| dividend_per_share | float | 每股分红(元) |

### chip 返回

| 字段 | 类型 | 说明 |
|------|------|------|
| date | string | 日期 |
| avg_cost | float | 平均成本 |
| profit_ratio | float | 获利比例(%) |
| concentration | float | 筹码集中度 |
| price_ranges | string | 筹码分布区间 |

## 注意事项

- shareholder 仅支持A股和港股，不支持美股
- chip 仅支持沪深京A股

## 示例

```bash
# A股十大股东
python3 ./scripts/stock_query.py call shareholder --param code=sh600519
# 港股股东
python3 ./scripts/stock_query.py call shareholder --param code=hk00700
# 最近3年分红
python3 ./scripts/stock_query.py call dividend --param code=sh600519 --param years=3
# 全部历史分红
python3 ./scripts/stock_query.py call dividend --param code=sh600519 --param all=true
# 筹码分布(指定日期范围)
python3 ./scripts/stock_query.py call chip --param code=sh600519 --param start=2024-01-01 --param end=2024-06-30
```
