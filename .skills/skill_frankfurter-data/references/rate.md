# rate

查询单个货币对汇率。

**CLI 调用**：`python3 scripts/cli_wrapper.py call rate --param base=EUR --param quote=USD`

**上游路径**：`GET /v2/rate/{base}/{quote}`

## 参数

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `base` | string | ✅ | 基准货币代码（如 EUR、USD） |
| `quote` | string | ✅ | 目标货币代码（如 CNY、JPY） |
| `date` | string | 否 | 查询历史某天汇率，格式 YYYY-MM-DD |
| `providers` | string | 否 | 指定数据源 |

## 返回示例

```json
{
  "base": "EUR",
  "quote": "USD",
  "date": "2026-05-13",
  "rate": 1.0892
}
```
