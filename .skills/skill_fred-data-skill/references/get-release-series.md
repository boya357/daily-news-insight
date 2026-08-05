# get-release-series

按数据发布浏览 FRED 系列。每个 release 对应一个数据发布源（如 BLS Employment Situation）。

## 调用

```bash
# 浏览某个 release 下的系列
python3 ./scripts/_cli_wrapper.py call get-release-series --param release_id=151 --param limit=20
```

## 入参

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `release_id` | string | ✅ | FRED release ID（整数） |
| `order_by` | string | ❌ | 排序字段 |
| `sort_order` | string | ❌ | `asc` 或 `desc` |
| `limit` | integer | ❌ | 最大结果数（最大 1,000） |
| `offset` | integer | ❌ | 分页偏移 |

## 常用 Release ID

| Release ID | 名称 |
|------------|------|
| `53` | Gross Domestic Product |
| `50` | Employment Situation |
| `10` | Consumer Price Index |
| `18` | H.6 Money Stock Measures |
| `21` | H.15 Selected Interest Rates |
