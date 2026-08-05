# query

自然语言查询经济数据。后端通过 LLM 解析查询意图，自动匹配数据源和指标，返回结构化时间序列数据。

**CLI 调用**：`python3 ./bin/_cli_wrapper.py call query --param "query=US GDP growth last 10 years"`

**上游路径**：`POST /api/query`

## 参数

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `query` | string | ✅ | 自然语言经济数据查询，如「US GDP growth last 10 years」「中国 CPI 近5年」「Japan unemployment rate」|
| `conversation_id` | string | ❌ | 会话 ID，保持上下文用于追问。从上一次返回的 `conversationId` 字段获取 |

## 返回结构

```json
{
  "conversationId": "conv_abc123",
  "clarificationNeeded": false,
  "data": [
    {
      "metadata": {
        "source": "FRED",
        "indicator": "GDP",
        "country": "US",
        "frequency": "quarterly",
        "unit": "billions of dollars"
      },
      "data": [
        {"date": "2025-Q1", "value": 28000},
        {"date": "2024-Q4", "value": 27500}
      ]
    }
  ]
}
```

## 字段说明

| 字段 | 说明 |
|------|------|
| `conversationId` | 会话 ID，传入下次查询可保持上下文 |
| `clarificationNeeded` | `true` 表示查询意图不够明确，需用户补充 |
| `data` | 数据集数组，每个元素包含一个指标的数据 |
| `data[].metadata` | 数据元信息：来源、指标名、国家、频率、单位 |
| `data[].data` | 时间序列数据点，每个点包含 date 和 value |

## 查询示例

```bash
# 美国 GDP
python3 ./bin/_cli_wrapper.py call query --param "query=US GDP growth last 10 years"

# 中国 CPI
python3 ./bin/_cli_wrapper.py call query --param "query=中国 CPI 近 5 年变化趋势"

# 多国比较
python3 ./bin/_cli_wrapper.py call query --param "query=Compare inflation rates of US, EU, Japan 2020-2025"

# 贸易数据
python3 ./bin/_cli_wrapper.py call query --param "query=US-China bilateral trade volume last 5 years"

# 追问
python3 ./bin/_cli_wrapper.py call query --param "query=now show quarterly breakdown" --param "conversation_id=conv_abc123"
```

## 注意事项

- 响应较慢（10-30 秒），因为后端需要 LLM 解析查询意图
- 中英文查询均支持
- 当 `clarificationNeeded=true` 时，应提示用户补充更具体的查询
- 单次可能返回多个数据集（如查询 "US GDP and CPI" 会返回两个数据集）
