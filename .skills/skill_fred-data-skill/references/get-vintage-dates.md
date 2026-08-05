# get-vintage-dates

获取 FRED 系列的数据修订历史日期（ALFRED 功能）。每个 vintage date 代表该系列数据被修订或新值发布的时间点。

## 调用

```bash
# 获取 GDP 的所有修订日期
python3 ./scripts/_cli_wrapper.py call get-vintage-dates --param series_id=GDP

# 按降序获取最近 10 个修订日期
python3 ./scripts/_cli_wrapper.py call get-vintage-dates --param series_id=GDP --param sort_order=desc --param limit=10
```

## 入参

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `series_id` | string | ✅ | FRED 系列 ID |
| `sort_order` | string | ❌ | `asc`（默认）或 `desc` |
| `limit` | integer | ❌ | 最大结果数（最大 10,000） |
| `offset` | integer | ❌ | 分页偏移 |

## 返回字段

| 字段 | 说明 |
|------|------|
| `vintage_dates[]` | 修订日期数组，格式 YYYY-MM-DD |

## 使用场景

- 追踪经济数据（如 GDP）历次修订的时间线
- 研究「初值 → 修正值 → 终值」的修订幅度
- 构建 point-in-time 数据集避免 look-ahead bias
