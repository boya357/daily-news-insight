# get-series

获取 FRED 系列的元信息。

## 调用

```bash
python3 ./scripts/_cli_wrapper.py call get-series --param series_id=GDP
```

## 入参

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `series_id` | string | ✅ | FRED 系列 ID（如 GDP, CPIAUCSL, SP500, UNRATE） |

## 返回字段

| 字段 | 说明 |
|------|------|
| `seriess[].id` | 系列 ID |
| `seriess[].title` | 系列标题 |
| `seriess[].frequency` | 频率（Quarterly, Monthly, Daily 等） |
| `seriess[].frequency_short` | 频率缩写（Q, M, D 等） |
| `seriess[].units` | 单位（Billions of Dollars, Percent 等） |
| `seriess[].units_short` | 单位缩写 |
| `seriess[].seasonal_adjustment` | 季节调整方式 |
| `seriess[].observation_start` | 最早观测日期 |
| `seriess[].observation_end` | 最新观测日期 |
| `seriess[].last_updated` | 最后更新时间 |
| `seriess[].popularity` | 流行度评分 |
| `seriess[].notes` | 系列说明 |
