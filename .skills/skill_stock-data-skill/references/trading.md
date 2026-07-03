# asfund / hkfund / usfund / lhb / blocktrade / margintrade — 资金与交易分析

## 用途

获取资金流向、龙虎榜、大宗交易和融资融券等交易分析数据。

## 数据源

腾讯自选股

## 调用

```bash
python3 ./bin/_cli_wrapper.py call asfund --param code=sh600519
python3 ./bin/_cli_wrapper.py call hkfund --param code=hk00700
python3 ./bin/_cli_wrapper.py call usfund --param code=usAAPL
python3 ./bin/_cli_wrapper.py call lhb --param code=sh600519
python3 ./bin/_cli_wrapper.py call blocktrade --param code=sh600519
python3 ./bin/_cli_wrapper.py call margintrade --param code=sh600519
```

## 入参

### asfund — A股资金流向

| 参数 | 必填 | 类型 | 说明 |
|------|------|------|------|
| code | ✅ | string | A股代码。如 sh600519, sz000001 |
| date | ❌ | string | 日期，格式 YYYY-MM-DD。默认最新交易日 |

### hkfund — 港股资金流向

| 参数 | 必填 | 类型 | 说明 |
|------|------|------|------|
| code | ✅ | string | 港股代码。如 hk00700 |
| date | ❌ | string | 日期，格式 YYYY-MM-DD。默认最新交易日 |

### usfund — 美股卖空数据

| 参数 | 必填 | 类型 | 说明 |
|------|------|------|------|
| code | ✅ | string | 美股代码。如 usAAPL |
| date | ❌ | string | 日期，格式 YYYY-MM-DD。默认最新交易日 |

### lhb — 龙虎榜

| 参数 | 必填 | 类型 | 说明 |
|------|------|------|------|
| code | ✅ | string | 股票代码(仅沪深)。如 sh600519, sz000001 |
| date | ❌ | string | 日期，格式 YYYY-MM-DD。默认最新交易日 |

### blocktrade — 大宗交易

| 参数 | 必填 | 类型 | 说明 |
|------|------|------|------|
| code | ✅ | string | 股票代码(仅沪深)。如 sh600519, sz000001 |

### margintrade — 融资融券

| 参数 | 必填 | 类型 | 说明 |
|------|------|------|------|
| code | ✅ | string | 股票代码(仅沪深)。如 sh600519, sz000001 |

## 返回字段

返回 Markdown 表格，字段随操作不同而变化。

### asfund 返回

| 字段 | 类型 | 说明 |
|------|------|------|
| date | string | 日期 |
| main_inflow | float | 主力流入(万元) |
| main_outflow | float | 主力流出(万元) |
| main_net | float | 主力净流入(万元) |
| retail_net | float | 散户净流入(万元) |
| total_net | float | 总净流入(万元) |

### hkfund 返回

| 字段 | 类型 | 说明 |
|------|------|------|
| date | string | 日期 |
| buy_amount | float | 买入金额(万港元) |
| sell_amount | float | 卖出金额(万港元) |
| net_amount | float | 净买入金额(万港元) |

### usfund 返回

| 字段 | 类型 | 说明 |
|------|------|------|
| date | string | 日期 |
| short_volume | float | 卖空量 |
| short_ratio | float | 卖空比例(%) |
| total_volume | float | 总成交量 |

### lhb 返回

| 字段 | 类型 | 说明 |
|------|------|------|
| date | string | 日期 |
| reason | string | 上榜原因 |
| buy_seats | string | 买入营业部 |
| sell_seats | string | 卖出营业部 |
| buy_amount | float | 买入金额(万元) |
| sell_amount | float | 卖出金额(万元) |

### blocktrade 返回

| 字段 | 类型 | 说明 |
|------|------|------|
| date | string | 成交日期 |
| price | float | 成交价(元) |
| volume | float | 成交量(万股) |
| amount | float | 成交额(万元) |
| premium_rate | float | 溢价率(%) |
| buyer | string | 买方营业部 |
| seller | string | 卖方营业部 |

### margintrade 返回

| 字段 | 类型 | 说明 |
|------|------|------|
| date | string | 日期 |
| margin_buy | float | 融资买入额(万元) |
| margin_balance | float | 融资余额(万元) |
| short_sell | float | 融券卖出量(股) |
| short_balance | float | 融券余额(万元) |
| total_balance | float | 融资融券余额(万元) |

## 注意事项

- lhb、blocktrade、margintrade 仅支持沪深市场
- usfund 返回的是卖空(short selling)数据

## 示例

```bash
# A股资金流向
python3 ./bin/_cli_wrapper.py call asfund --param code=sh600519
# A股资金流向(指定日期)
python3 ./bin/_cli_wrapper.py call asfund --param code=sh600519 --param date=2024-06-01
# 港股资金流向
python3 ./bin/_cli_wrapper.py call hkfund --param code=hk00700
# 美股卖空数据
python3 ./bin/_cli_wrapper.py call usfund --param code=usAAPL
# 龙虎榜
python3 ./bin/_cli_wrapper.py call lhb --param code=sh600519
# 大宗交易
python3 ./bin/_cli_wrapper.py call blocktrade --param code=sh600519
# 融资融券
python3 ./bin/_cli_wrapper.py call margintrade --param code=sh600519
```
