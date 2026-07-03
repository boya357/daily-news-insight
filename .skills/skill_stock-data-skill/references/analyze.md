# analyze — 技术分析

## 用途

自动获取 K 线数据并计算完整的技术指标，包括均线(MA)、MACD、RSI、支撑位/压力位、缺口识别、趋势判断，以及综合操作信号。

## 数据源

K 线数据来自东财/腾讯（自动切换），技术指标由 CLI 内置计算。

## 调用

```bash
python3 ./bin/_cli_wrapper.py call analyze --param code=sh600519
```

## 入参

| 参数 | 必填 | 类型 | 默认 | 说明 |
|------|------|------|------|------|
| code | ✅ | string | — | 股票代码 |
| days | ❌ | int | 120 | 分析使用的K线天数（20-500） |

## 返回字段

| 字段 | 类型 | 说明 |
|------|------|------|
| code | string | 股票代码 |
| indicators | object | 技术指标集合 |
| indicators.ma5/ma10/ma20/ma60 | float | 均线值 |
| indicators.macd | object | {dif, dea, macd} |
| indicators.rsi6/rsi12/rsi24 | float | RSI 指标 |
| ma_arrangement | string | 均线排列：bullish_arrangement(多头) / bearish_arrangement(空头) / mixed(缠绕) |
| macd_cross | object | MACD 金叉/死叉检测 |
| macd_cross.type | string | golden_cross(金叉) / death_cross(死叉) / neutral |
| macd_cross.signal | string | bullish / bearish / none |
| support_resistance | object | 支撑位和压力位 |
| support_resistance.support | float[] | 支撑位列表（最多3个，从高到低） |
| support_resistance.resistance | float[] | 压力位列表（最多3个，从低到高） |
| gaps | array | 缺口列表 |
| gaps[].type | string | up(向上缺口) / down(向下缺口) |
| gaps[].date | string | 缺口形成日期 |
| gaps[].gap_range | [float, float] | 缺口价格区间 |
| gaps[].filled | bool | 是否已回补 |
| gaps[].filled_date | string | 回补日期 |
| trend | string | 趋势：strong_bullish/bullish/sideways/bearish/strong_bearish |
| signal | string | 综合信号：buy/sell/hold/hold(偏向买入)/hold(偏向卖出) |
| signal_reason | string | 信号理由 |
| source | string | K线数据源 |

## 信号生成逻辑

综合以下因子生成操作建议：
1. **均线排列**：多头排列→买入信号，空头排列→卖出信号
2. **MACD 金/死叉**：金叉→买入，死叉→卖出
3. **RSI**：>70 超买→卖出，<30 超卖→买入，>50 偏强
4. **趋势方向**：向上→利多，向下→利空
5. **未回补缺口**：作为参考信息

两个及以上买入信号→buy，两个及以上卖出信号→sell，否则 hold（可能偏向某方）。

## 示例

```bash
# 默认120天分析
python3 ./bin/_cli_wrapper.py call analyze --param code=sh600519

# 用250天数据做长期分析
python3 ./bin/_cli_wrapper.py call analyze --param code=sh600519 --param days=250

# 港股技术分析
python3 ./bin/_cli_wrapper.py call analyze --param code=hk00700
```
