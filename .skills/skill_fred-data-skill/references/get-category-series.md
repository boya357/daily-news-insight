# get-category-series

按 FRED 分类浏览经济数据系列。FRED 将数据组织为层级分类树。

## 调用

```bash
# 浏览分类下的系列
python3 ./scripts/_cli_wrapper.py call get-category-series --param category_id=32145

# 按流行度排序
python3 ./scripts/_cli_wrapper.py call get-category-series --param category_id=32145 --param order_by=popularity --param sort_order=desc --param limit=20
```

## 入参

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `category_id` | string | ✅ | FRED 分类 ID（整数） |
| `order_by` | string | ❌ | 排序字段 |
| `sort_order` | string | ❌ | `asc` 或 `desc` |
| `limit` | integer | ❌ | 最大结果数（最大 1,000） |
| `offset` | integer | ❌ | 分页偏移 |

## 常用分类 ID

| Category ID | 名称 |
|-------------|------|
| `32991` | Money, Banking, & Finance |
| `32992` | Population, Employment, & Labor Markets |
| `32455` | National Accounts |
| `32263` | Prices |
| `33060` | International Data |
