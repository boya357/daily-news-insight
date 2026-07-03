# minute — 当日分时数据

## 用途

获取股票当日的分时数据（每分钟价格和成交量），用于日内走势分析。

## 数据源

腾讯行情

## 调用

```bash
python3 ./bin/_cli_wrapper.py call minute --param code=sh600519
```

## 入参

| 参数 | 必填 | 类型 | 说明 |
|------|------|------|------|
| code | ✅ | string | 股票代码 |

## 返回字段

| 字段 | 类型 | 说明 |
|------|------|------|
| code | string | 股票代码 |
| date | string | 交易日期 |
| pre_close | float | 昨收价 |
| count | int | 分时数据条数 |
| data[] | array | 分时数组 |
| data[].time | string | 时间（HHMM） |
| data[].price | float | 当分钟价格 |
| data[].volume | float | 累计成交量 |
| source | string | 数据源 |

## 已知限制

- 仅返回当日数据
- A股交易时间：9:30-15:00，约242个数据点
- 非交易时段返回上一交易日数据

## 示例

```bash
python3 ./bin/_cli_wrapper.py call minute --param code=sh600519
python3 ./bin/_cli_wrapper.py call minute --param code=hk00700
```
