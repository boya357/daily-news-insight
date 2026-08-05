# currency

查询单个货币的详细信息和数据源覆盖。

**CLI 调用**：`python3 scripts/cli_wrapper.py call currency --param code=CNY`

**上游路径**：`GET /v2/currency/{code}`

## 参数

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `code` | string | ✅ | 货币代码（如 EUR、USD、CNY） |

## 返回示例

```json
{
  "code": "CNY",
  "name": "Chinese Yuan",
  "providers": ["ECB"]
}
```
