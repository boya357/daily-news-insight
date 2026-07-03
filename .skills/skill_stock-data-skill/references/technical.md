# technical — 技术指标

## 用途

获取股票技术分析指标数据，包括均线(MA)、MACD、KDJ、RSI、布林带(BOLL)、乖离率(BIAS)、威廉指标(WR)、趋向指标(DMI)等。

## 数据源

腾讯自选股

## 调用

```bash
python3 ./bin/_cli_wrapper.py call technical --param code=sh600519
```

## 入参

| 参数 | 必填 | 类型 | 说明 |
|------|------|------|------|
| code | ✅ | string | 股票代码，支持批量(逗号分隔)。A股: sh600519; 港股: hk00700; 美股: usAAPL |
| group | ❌ | string | 指标组: ma/macd/kdj/rsi/boll/bias/wr/dmi/all。默认 all(全部指标) |
| start | ❌ | string | 起始日期，格式 YYYY-MM-DD |
| end | ❌ | string | 结束日期，格式 YYYY-MM-DD |

## 返回字段

返回 Markdown 表格，字段随 group 参数变化。以 group=all 为例:

| 字段 | 类型 | 说明 |
|------|------|------|
| date | string | 日期 |
| ma5/ma10/ma20/ma60 | float | 各周期均线值 |
| dif/dea/macd | float | MACD 指标 |
| k/d/j | float | KDJ 指标 |
| rsi6/rsi12/rsi24 | float | RSI 指标 |
| upper/mid/lower | float | 布林带上/中/下轨 |
| bias6/bias12/bias24 | float | 乖离率 |
| wr6/wr10 | float | 威廉指标 |
| pdi/mdi/adx/adxr | float | DMI 指标 |

## 示例

```bash
# 获取全部技术指标
python3 ./bin/_cli_wrapper.py call technical --param code=sh600519
# 仅获取MACD
python3 ./bin/_cli_wrapper.py call technical --param code=sh600519 --param group=macd
# 指定日期范围
python3 ./bin/_cli_wrapper.py call technical --param code=sh600519 --param group=kdj --param start=2024-01-01 --param end=2024-06-30
# 批量查询
python3 ./bin/_cli_wrapper.py call technical --param code=sh600519,sz000858 --param group=rsi
```
