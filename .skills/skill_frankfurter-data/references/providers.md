# providers

列出所有汇率数据源（央行等）。

**CLI 调用**：`python3 scripts/cli_wrapper.py call providers`

**上游路径**：`GET /v2/providers`

## 参数

无。

## 返回示例

```json
{
  "ECB": {
    "name": "European Central Bank",
    "url": "https://www.ecb.europa.eu"
  },
  "BOE": {
    "name": "Bank of England",
    "url": "https://www.bankofengland.co.uk"
  }
}
```
