# currencies

列出所有可用货币及其数据源覆盖情况。

**CLI 调用**：`python3 scripts/cli_wrapper.py call currencies`

**上游路径**：`GET /v2/currencies`

## 参数

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `scope` | string | 否 | 设为 `all` 可包含历史/已退出流通的货币 |

## 返回示例

```json
{
  "EUR": {
    "name": "Euro",
    "providers": ["ECB"]
  },
  "USD": {
    "name": "US Dollar",
    "providers": ["ECB", "BOE"]
  },
  "CNY": {
    "name": "Chinese Yuan",
    "providers": ["ECB"]
  }
}
```
