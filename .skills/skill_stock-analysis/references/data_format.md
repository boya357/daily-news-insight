# 股票数据格式说明

## 目录

- [概述](#概述)
- [数据结构](#数据结构)
- [字段说明](#字段说明)
- [使用示例](#使用示例)
- [常见问题](#常见问题)

## 概述

本文档详细说明了 `fetch_stock_data.py` 生成的股票数据文件格式。数据以 JSON 格式存储，包含实时行情和历史K线数据。

## 数据结构

```json
{
  "stock_code": "000001",
  "fetch_time": "2026-03-26 10:00:00",
  "data_source": "新浪财经",
  "real_time": { ... },
  "historical": [ ... ],
  "kline_data": [ ... ]
}
```

## 字段说明

### 顶层字段

| 字段名 | 类型 | 说明 | 示例 |
|--------|------|------|------|
| `stock_code` | string | 股票代码 | `"000001"` |
| `fetch_time` | string | 数据获取时间 | `"2026-03-26 10:00:00"` |
| `data_source` | string | 数据源名称 | `"新浪财经"` |
| `real_time` | object | 实时行情数据 | 见下方详细说明 |
| `historical` | array | 历史K线数据 | 见下方详细说明 |
| `kline_data` | array | 历史K线数据（兼容性字段） | 与 `historical` 完全相同 |

### real_time 字段说明

实时行情数据对象：

| 字段名 | 类型 | 说明 | 示例 |
|--------|------|------|------|
| `source` | string | 数据源 | `"新浪财经"` |
| `name` | string | 股票名称 | `"平安银行"` |
| `open` | float | 开盘价 | `10.50` |
| `pre_close` | float | 昨收价 | `10.30` |
| `current` | float | 当前价格 | `10.65` |
| `high` | float | 最高价 | `10.80` |
| `low` | float | 最低价 | `10.40` |
| `bid` | float | 买一价 | `10.64` |
| `ask` | float | 卖一价 | `10.65` |
| `volume` | float | 成交量（股） | `1000000.0` |
| `amount` | float | 成交额（元） | `10650000.0` |
| `date` | string | 交易日期 | `"2026-03-26"` |
| `time` | string | 交易时间 | `"10:00:00"` |

**注意**：
- 非交易时间，`current`、`open`、`high`、`low` 可能为 `0.00` 或 `null`
- 成交量单位为股，需要除以100转换为手

### historical / kline_data 字段说明

历史K线数据数组，每个元素为一个交易日的数据：

| 字段名 | 类型 | 说明 | 示例 |
|--------|------|------|------|
| `date` | string | 交易日期 | `"2025-12-22"` |
| `open` | float | 开盘价 | `39.99` |
| `high` | float | 最高价 | `40.46` |
| `low` | float | 最低价 | `39.86` |
| `close` | float | 收盘价 | `40.02` |
| `volume` | float | 成交量（股） | `25386347.0` |

**注意**：
- 数组按时间升序排列，第一个元素为最早日期
- 成交量单位为股，需要除以100转换为手

## 使用示例

### 示例1：读取数据并计算涨跌幅

```python
import json
import pandas as pd

# 读取数据
with open('stock_data_000001.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 方式1：使用 historical 字段（推荐）
df = pd.DataFrame(data['historical'])

# 方式2：使用 kline_data 字段（兼容性）
df = pd.DataFrame(data['kline_data'])

# 计算涨跌幅
df['涨跌幅'] = df['收盘价'].pct_change() * 100

print(df.tail(7))
```

### 示例2：获取实时价格

```python
import json

# 读取数据
with open('stock_data_000001.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 获取实时数据
real_time = data['real_time']
print(f"股票名称: {real_time['name']}")
print(f"当前价格: {real_time['current']:.2f}")
print(f"昨收价: {real_time['pre_close']:.2f}")

# 计算涨跌幅
if real_time['pre_close'] > 0:
    change_pct = (real_time['current'] - real_time['pre_close']) / real_time['pre_close'] * 100
    print(f"涨跌幅: {change_pct:+.2f}%")
```

### 示例3：计算市场情绪指标

```python
import json
import pandas as pd

# 读取数据
with open('stock_data_300418.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 提取K线数据（推荐使用 historical 字段）
df = pd.DataFrame(data['historical'])

# 计算情绪指标
df['涨跌幅'] = df['close'].pct_change() * 100
df['情绪'] = df['涨跌幅'].apply(
    lambda x: '极度恐慌' if x < -8 else (
        '恐慌' if x < -5 else (
            '偏空' if x < -3 else (
                '中性' if x < 3 else (
                    '偏多' if x < 5 else (
                        '强势' if x < 8 else '极度贪婪'
                    )
                )
            )
        )
    )
)

print('最近7个交易日的市场情绪:')
print(df[['date', 'close', '涨跌幅', '情绪']].tail(7).to_string(index=False))
```

## 常见问题

### Q1: `historical` 和 `kline_data` 有什么区别？

**A**: 两者完全相同。`historical` 是标准字段名，`kline_data` 是为了兼容性而添加的别名。推荐使用 `historical`。

### Q2: 为什么当前价格显示为 0.00？

**A**: 非交易时间（盘前、盘后、周末、节假日）时，实时行情数据可能为空或为0。建议使用 `historical` 数据的最后一项作为参考价格。

### Q3: 成交量单位是什么？

**A**: 成交量单位为"股"，需要除以100转换为"手"（1手=100股）。

### Q4: 如何判断数据是否为最新？

**A**: 查看 `fetch_time` 字段，这是数据获取的时间戳。对于实时数据，建议每次分析前重新获取。

### Q5: 字段名使用中文还是英文？

**A**: 数据文件中的字段名为英文（如 `close`），但你可以根据需要转换为中文显示。`analyze_stock.py` 内部使用英文字段名处理数据。

## 字段名映射表

| 英文字段名 | 中文名称 | 说明 |
|-----------|---------|------|
| `date` | 日期 | 交易日期 |
| `open` | 开盘价 | 当日开盘价 |
| `high` | 最高价 | 当日最高价 |
| `low` | 最低价 | 当日最低价 |
| `close` | 收盘价 | 当日收盘价 |
| `volume` | 成交量 | 成交股数 |

## 注意事项

1. **数据时效性**：实时行情数据仅在交易时间有效，非交易时间请使用历史数据
2. **数据完整性**：部分数据源可能缺少某些字段，使用前请检查字段是否存在
3. **数据精度**：价格数据保留2位小数，计算时注意浮点数精度问题
4. **异常处理**：建议在使用数据前检查 `current` 是否为0，避免除零错误
