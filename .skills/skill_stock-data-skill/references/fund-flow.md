# fund-flow — 个股资金流向

## 用途

获取个股的每日资金流向数据，包含主力、超大单、大单、中单、小单的净流入金额。

## 数据源

东方财富

## 调用

```bash
python3 ./scripts/stock_query.py call fund-flow --param code=sh600519 --param days=30
```

## 入参

| 参数 | 必填 | 类型 | 默认 | 说明 |
|------|------|------|------|------|
| code | ✅ | string | — | 股票代码 |
| days | ❌ | int | 30 | 返回天数（1-365） |

## 返回字段

| 字段 | 类型 | 说明 |
|------|------|------|
| code | string | 股票代码 |
| count | int | 数据天数 |
| data[] | array | 每日资金流向 |
| data[].date | string | 日期 |
| data[].main_net_inflow | float | 主力净流入(元) |
| data[].small_net_inflow | float | 小单净流入(元) |
| data[].mid_net_inflow | float | 中单净流入(元) |
| data[].large_net_inflow | float | 大单净流入(元) |
| data[].super_net_inflow | float | 超大单净流入(元) |
| source | string | 数据源 |

## 数据口径说明

- 主力 = 超大单 + 大单
- 正值表示净流入，负值表示净流出
- 金额单位：元

## 示例

```bash
# 最近30天
python3 ./scripts/stock_query.py call fund-flow --param code=sh600519

# 最近7天
python3 ./scripts/stock_query.py call fund-flow --param code=sh600519 --param days=7
```
