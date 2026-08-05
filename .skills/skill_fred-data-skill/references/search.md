# search

全文搜索 FRED 数据系列。FRED 有 80 万+ 经济数据系列，用此接口找到需要的系列 ID。

## 调用

```bash
# 搜索 CPI 相关系列
python3 ./scripts/_cli_wrapper.py call search --param search_text=consumer price index --param limit=10

# 按流行度排序搜索 GDP
python3 ./scripts/_cli_wrapper.py call search --param search_text=GDP --param order_by=popularity --param sort_order=desc

# 过滤月度数据
python3 ./scripts/_cli_wrapper.py call search --param search_text=unemployment --param filter_variable=frequency --param filter_value=Monthly
```

## 入参

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `search_text` | string | ✅ | 搜索关键词 |
| `search_type` | string | ❌ | `full_text`（默认）或 `series_id` |
| `order_by` | string | ❌ | 排序字段：search_rank, series_id, title, units, frequency, popularity, last_updated 等 |
| `sort_order` | string | ❌ | `asc` 或 `desc` |
| `limit` | integer | ❌ | 最大结果数（最大 1,000） |
| `offset` | integer | ❌ | 分页偏移 |
| `filter_variable` | string | ❌ | 过滤字段：frequency, units, seasonal_adjustment |
| `filter_value` | string | ❌ | 过滤值（配合 filter_variable 使用） |

## 返回字段

| 字段 | 说明 |
|------|------|
| `count` | 总匹配数 |
| `seriess[].id` | 系列 ID |
| `seriess[].title` | 系列标题 |
| `seriess[].frequency` | 频率 |
| `seriess[].units` | 单位 |
| `seriess[].popularity` | 流行度 |
| `seriess[].observation_start` | 最早日期 |
| `seriess[].observation_end` | 最新日期 |
| `seriess[].last_updated` | 最后更新 |
| `seriess[].notes` | 备注 |
