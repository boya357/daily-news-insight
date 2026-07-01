# finance — 财务报表

## 用途

获取上市公司财务报表数据，包括利润表、资产负债表、现金流量表。支持A股、港股、美股。

## 数据源

腾讯自选股

## 调用

```bash
python3 ./scripts/stock_query.py call finance --param code=sh600519
```

## 入参

| 参数 | 必填 | 类型 | 说明 |
|------|------|------|------|
| code | ✅ | string | 股票代码，支持批量(逗号分隔)。A股: sh600519; 港股: hk00700; 美股: usAAPL |
| type | ❌ | string | 报表类型。A股: lrb(利润表)/zcfz(资产负债表)/xjll(现金流量表); 港股: zhsy(综合损益)/zcfz/xjll; 美股: income/balance/cashflow。默认利润表 |
| num | ❌ | int | 返回报告期数，默认 1，最大 20 |

## 返回字段

返回 Markdown 表格，字段随报表类型变化。通用字段:

| 字段 | 类型 | 说明 |
|------|------|------|
| code | string | 股票代码 |
| report_date | string | 报告期 |
| (各财务科目) | float | 具体科目随 type 参数不同而变化 |

## 注意事项

- 港股返回值单位为港元或美元(视公司报表币种)
- 美股返回值单位为美元
- 支持批量查询，code 以逗号分隔多个代码

## 示例

```bash
# A股利润表(最近1期)
python3 ./scripts/stock_query.py call finance --param code=sh600519
# A股资产负债表(最近5期)
python3 ./scripts/stock_query.py call finance --param code=sh600519 --param type=zcfz --param num=5
# 港股现金流量表
python3 ./scripts/stock_query.py call finance --param code=hk00700 --param type=xjll
# 美股利润表
python3 ./scripts/stock_query.py call finance --param code=usAAPL --param type=income
# 批量查询
python3 ./scripts/stock_query.py call finance --param code=sh600519,sz000858
```
