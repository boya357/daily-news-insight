# quote — 实时股票行情

## 用途

获取单只股票的实时行情数据，包括最新价、开盘价、最高价、最低价、涨跌幅、成交量、成交额、换手率、市值、市盈率等。

## 数据源

腾讯行情(主) → 东方财富(备1) → 新浪财经(备2)，自动切换。

## 调用

```bash
python3 ./bin/_cli_wrapper.py call quote --param code=sh600519
```

## 入参

| 参数 | 必填 | 类型 | 说明 |
|------|------|------|------|
| code | ✅ | string | 股票代码。A股: sh600519/sz000001; 港股: hk00700; 美股: usAAPL; 指数: sh000001 |
| source | ❌ | string | 强制指定数据源：tencent/eastmoney/sina（默认自动切换） |

## 返回字段

| 字段 | 类型 | 说明 |
|------|------|------|
| code | string | 股票代码 |
| name | string | 股票名称 |
| close | float | 最新价 |
| open | float | 开盘价 |
| high | float | 最高价 |
| low | float | 最低价 |
| pre_close | float | 昨收价 |
| change | float | 涨跌额 |
| change_percent | float | 涨跌幅(%) |
| volume | float | 成交量(手) |
| amount | float | 成交额(元) |
| turnover_rate | float | 换手率(%) |
| market_cap | float | 总市值(亿) |
| pe_ratio | float | 市盈率 |
| date | string | 日期 |
| time | string | 时间 |
| source | string | 实际使用的数据源 |

## 示例

```bash
# A股
python3 ./bin/_cli_wrapper.py call quote --param code=sh600519
# 港股
python3 ./bin/_cli_wrapper.py call quote --param code=hk00700
# 美股
python3 ./bin/_cli_wrapper.py call quote --param code=usAAPL
# 上证指数
python3 ./bin/_cli_wrapper.py call quote --param code=sh000001
# 强制用新浪
python3 ./bin/_cli_wrapper.py call quote --param code=sh600519 --param source=sina
```
