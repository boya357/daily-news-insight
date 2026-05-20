# 表名: mf_etfprcomponents (公募基金ETF申购赎回成份股信息)
说明:   
1.本表收录ETF基金每个交易日公布的申购赎回成份股信息，包括成分股的名称、代码、现金替代标志等数据。
2.历史数据：2006年4月起-至今。
3.数据来源：基金公司官网和交易所官网。

## 1. 业务唯一性与数据更新频率

- **业务唯一性**: innercode,TradingDay,SecuCode
- **数据更新频率**: 日更新

## 2. 字段信息

| 列序号 | 列名 | 中文名称 | 列类型 | 长度 | 精度 | 字段空否 | 字段备注 |
|--------|------|----------|--------|------|------|----------|----------|
| 1 | ID | ID | bigint |  |  | 否 |  |
| 2 | innercode | 基金内部编码 | int |  |  | 否 |  |
| 3 | InfoSource | 信息来源 | varchar | 100.0 |  | 是 |  |
| 4 | TradingDay | 交易日期 | datetime |  |  | 否 |  |
| 5 | SecuCode | 成份股代码 | varchar | 50.0 |  | 否 |  |
| 6 | SecuAbbr | 成份股简称 | varchar | 50.0 |  | 是 |  |
| 7 | Secuinnercode | 成份股内部编码 | int |  |  | 是 | 成份股内部编码（Secuinnercode）：当Secuinnercode<1000000时是A股，与“证券主表（SecuMain）”中的“证券内部编码（innercode）”关联；当Secuinnercode在1000000与2000000之间时是港股，与“港股证券主表（HK_SecuMain）”中的“证券内部编码（innercode）”关联；当Secuinnercode在7000000与10000000之间时是美股，与“美股证券主表（US_SecuMain）”中的“证券内部编码（innercode）”关联；Secuinnercode在2000000与3000000之间时，与“期货合约（Fut_ContractMain）”中的“合约内部编码（Contractinnercode）”关联；得到ETF成份股的交易代码、简称等信息。 |
| 8 | StockAmount | 股票数量(股) | int |  |  | 是 |  |
| 9 | CashSubstituteSignDescrip | 现金替代标志描述 | varchar | 50.0 |  | 是 |  |
| 10 | CashSubstituteSign | 现金替代标志 | int |  |  | 是 | 1-允许，2-必须，3-禁止，4-退补 |
| 11 | CashSubstituteProportion | 现金替代比例 | decimal | 19.0 | 8.0 | 是 |  |
| 12 | ApplyCashPremiumRate | 申购现金替代溢价比例 | decimal | 19.0 | 8.0 | 是 |  |
| 13 | RedeemCashDiscountRate | 赎回现金替代折价比例 | decimal | 19.0 | 8.0 | 是 |  |
| 14 | FixedSubstituteSum | 固定替代金额(元) | money |  |  | 是 |  |
| 15 | ApplySubstituteSum | 申购替代金额(元) | money |  |  | 是 |  |
| 16 | RedeemSubstituteSum | 赎回替代金额(元) | money |  |  | 是 |  |
| 17 | UpdateTime | 更新日期 | datetime |  |  | 否 |  |
| 18 | JSID | JSID | bigint |  |  | 否 |  |
