# get-observations

获取 FRED 系列的时间序列数据。这是最核心的操作。

## 调用

```bash
# 获取 GDP 全部历史数据
python3 ./scripts/_cli_wrapper.py call get-observations --param series_id=GDP

# 获取 CPI 月度数据，2020 年至今，百分比变化
python3 ./scripts/_cli_wrapper.py call get-observations --param series_id=CPIAUCSL --param observation_start=2020-01-01 --param units=pch

# 获取 SP500 日数据，最近 100 条
python3 ./scripts/_cli_wrapper.py call get-observations --param series_id=SP500 --param sort_order=desc --param limit=100
```

## 入参

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `series_id` | string | ✅ | FRED 系列 ID |
| `observation_start` | string | ❌ | 起始日期 YYYY-MM-DD |
| `observation_end` | string | ❌ | 截止日期 YYYY-MM-DD |
| `units` | string | ❌ | 数据变换：`lin`=原值, `chg`=变化量, `ch1`=距年初变化, `pch`=环比%, `pc1`=同比%, `pca`=年化%, `cch`=累计变化, `cca`=年化累计, `log`=自然对数 |
| `frequency` | string | ❌ | 频率聚合：`d`=日, `w`=周, `bw`=双周, `m`=月, `q`=季, `sa`=半年, `a`=年 |
| `aggregation_method` | string | ❌ | 聚合方法：`avg`=平均, `sum`=求和, `eop`=期末值 |
| `sort_order` | string | ❌ | `asc`（默认）或 `desc` |
| `limit` | integer | ❌ | 最大返回条数（最大 100,000） |
| `offset` | integer | ❌ | 分页偏移 |

## 返回字段

| 字段 | 说明 |
|------|------|
| `observations[].date` | 观测日期 YYYY-MM-DD |
| `observations[].value` | 观测值（缺失值为 `.`） |
| `realtime_start` | 实时期间起始 |
| `realtime_end` | 实时期间截止 |
| `count` | 总观测数 |
| `offset` | 当前偏移 |
| `limit` | 当前限制 |

## 数据变换说明

| units 值 | 含义 | 公式 |
|----------|------|------|
| `lin` | 原始水平值 | x(t) |
| `chg` | 变化量 | x(t) - x(t-1) |
| `ch1` | 距年初变化 | x(t) - x(年初) |
| `pch` | 环比百分比 | (x(t)/x(t-1) - 1) * 100 |
| `pc1` | 同比百分比 | (x(t)/x(t-n) - 1) * 100 |
| `pca` | 年化百分比变化 | ((x(t)/x(t-1))^(n/1) - 1) * 100 |
| `log` | 自然对数 | ln(x(t)) |
