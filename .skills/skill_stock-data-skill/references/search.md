# search — 股票搜索

## 用途

按股票名称、拼音首字母或代码搜索匹配的股票列表。

## 数据源

东方财富搜索 API

## 调用

```bash
python3 ./bin/_cli_wrapper.py call search --param keyword=茅台
```

## 入参

| 参数 | 必填 | 类型 | 说明 |
|------|------|------|------|
| keyword | ✅ | string | 搜索关键词（股票名称、拼音、代码均可） |

## 返回字段

| 字段 | 类型 | 说明 |
|------|------|------|
| keyword | string | 搜索关键词 |
| count | int | 匹配数量 |
| items[] | array | 匹配结果 |
| items[].code | string | 股票代码（不含市场前缀） |
| items[].name | string | 股票名称 |
| items[].market | string | 市场前缀：sh/sz/hk/us |
| items[].type | string | 类型（如 沪A、深A、港股 等） |
| items[].quote_id | string | 东财 QuoteID |
| source | string | 数据源 |

## 使用技巧

搜索返回的 `market` + `code` 可以组合成其他 operation 需要的股票代码参数。例如搜索到 `market=sh, code=600519`，则用 `sh600519` 调用 quote/kline 等。

## 示例

```bash
# 按名称搜索
python3 ./bin/_cli_wrapper.py call search --param keyword=茅台

# 按拼音搜索
python3 ./bin/_cli_wrapper.py call search --param keyword=gzmt

# 按代码搜索
python3 ./bin/_cli_wrapper.py call search --param keyword=600519

# 搜索美股
python3 ./bin/_cli_wrapper.py call search --param keyword=apple
```
