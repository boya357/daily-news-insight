# rates

查询汇率（最新/历史/时间序列）。

**CLI 调用**：`python3 scripts/cli_wrapper.py call rates [--param ...]`

**上游路径**：`GET /v2/rates`

## 参数

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `base` | string | 否 | 基准货币代码，默认 EUR |
| `quotes` | string | 否 | 目标货币代码，逗号分隔（如 USD,CNY,JPY） |
| `date` | string | 否 | 查询某天历史汇率，格式 YYYY-MM-DD |
| `from` | string | 否 | 时间序列起始日期 YYYY-MM-DD |
| `to` | string | 否 | 时间序列结束日期 YYYY-MM-DD |
| `group` | string | 否 | 降采样粒度：`week` 或 `month` |
| `providers` | string | 否 | 指定数据源（如 ECB） |
| `expand` | string | 否 | 设为 `providers` 可查看每个汇率的数据来源 |

## 查询模式

- **最新汇率**：不传 date/from/to
- **历史某天**：传 `date=YYYY-MM-DD`
- **时间序列**：传 `from` + `to`（可选 `group` 降采样）

## 返回示例

### 最新/单日

```json
{
  "date": "2026-05-13",
  "base": "EUR",
  "rates": {
    "USD": 1.0892,
    "GBP": 0.8567,
    "CNY": 7.8901
  }
}
```

### 时间序列

```json
{
  "base": "USD",
  "start_date": "2026-04-01",
  "end_date": "2026-05-01",
  "rates": {
    "2026-04-01": {"CNY": 7.24},
    "2026-04-02": {"CNY": 7.25},
    ...
  }
}
```
