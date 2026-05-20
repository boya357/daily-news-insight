# 表名: mf_etfprlist (公募基金ETF申购赎回清单信息)
说明:   
1.本表收录ETF基金每个交易日公布的ETF申购赎回清单，包括是否允许赎回、是否允许申购，及单个账户申购、赎回上限等信息。
2.历史数据：2008年4月起-至今。
3.数据来源：基金公司官网和交易所官网。

## 1. 业务唯一性与数据更新频率

- **业务唯一性**: innercode,TradingDay
- **数据更新频率**: 日更新

## 2. 字段信息

| 列序号 | 列名 | 中文名称 | 列类型 | 长度 | 精度 | 字段空否 | 字段备注 |
|--------|------|----------|--------|------|------|----------|----------|
| 1 | ID | ID | bigint |  |  | 否 |  |
| 2 | innercode | 基金内部编码 | int |  |  | 否 |  |
| 3 | InfoSource | 信息来源 | varchar | 100.0 |  | 是 |  |
| 4 | TradingDay | 交易日期 | datetime |  |  | 否 |  |
| 5 | PrimaryMarketCode | 一级市场基金代码 | varchar | 20.0 |  | 是 |  |
| 6 | TargetIndexCode | 标的指数代码 | varchar | 20.0 |  | 是 |  |
| 7 | TargetIndexinnercode | 标的指数内部编码 | int |  |  | 是 | 与innercode作用相同 |
| 8 | PreviousTradingDate | 上一交易日期 | datetime |  |  | 是 |  |
| 9 | CashBalance | 现金差额(元) | money |  |  | 是 |  |
| 10 | NAVPerLeastPRUnit | 最小申赎单位资产净值(元) | money |  |  | 是 |  |
| 11 | NAVPerShare | 基金份额净值(元) | money |  |  | 是 |  |
| 12 | CashForecasted | 预估现金部分(元) | money |  |  | 是 |  |
| 13 | CashSubstituteProportion | 现金替代比例上限 | decimal | 19.0 | 8.0 | 是 |  |
| 14 | LeastRedemptionUnit | 最小申赎单位(份) | int |  |  | 是 |  |
| 15 | DividendForLRU | 最小申赎单位分红金额(元) | money |  |  | 是 |  |
| 16 | IfIOPVDescription | 是否需要公布IOPV描述 | varchar | 100.0 |  | 是 |  |
| 17 | IfPuschasableDescrip | 是否允许申购描述 | varchar | 100.0 |  | 是 |  |
| 18 | IfRedeemableDescrip | 是否允许赎回描述 | varchar | 100.0 |  | 是 |  |
| 19 | IfIOPV | 是否需要公布IOPV | int |  |  | 是 | 1-是，2-否 |
| 20 | IfPuschasable | 是否允许申购 | int |  |  | 是 | 1-是，2-否 |
| 21 | IfRedeemable | 是否允许赎回 | int |  |  | 是 | 1-是，2-否 |
| 22 | PurchaseUL | 申购份额上限(份) | decimal | 19.0 | 0.0 | 是 | 申购份额上限（份）（PurchaseUL）：统计对象为上海证券交易所和深圳证券交易所上市交易的ETF，代表当日累计可申购的基金份额上限。 |
| 23 | RedemptionUL | 赎回份额上限(份) | decimal | 19.0 | 0.0 | 是 | 赎回份额上限（份）(RedemptionUL)：统计对象为上海证券交易所和深圳证券交易所上市交易的ETF，代表当日累计可赎回的基金份额上限。 |
| 24 | SglAccPurACUL | 单个账户当日累计申购上限(份) | decimal | 19.0 | 0.0 | 是 | 单个账户当日累计申购上限（份）(SglAccPurACUL)：统计对象为深圳证券交易所上市交易的ETF。 |
| 25 | SglAccReACUL | 单个账户当日累计赎回上限(份) | decimal | 19.0 | 0.0 | 是 | 单个账户当日累计赎回上限（份）(SglAccReACUL)：统计对象为深圳证券交易所上市交易的ETF。 |
| 26 | NetPurUL | 净申购份额上限(份) | decimal | 19.0 | 6.0 | 是 | 净申购份额上限（份）(NetPurUL)：统计对象为深圳证券交易所上市交易的ETF。 |
| 27 | NetReUL | 净赎回份额上限(份) | decimal | 19.0 | 6.0 | 是 | 净赎回份额上限（份）(NetReUL)：统计对象为深圳证券交易所上市交易的ETF。 |
| 28 | SglAccNetPurUL | 单个账户当日净申购上限(份) | decimal | 19.0 | 6.0 | 是 | 单个账户当日净申购上限（份）(SglAccNetPurUL)：统计对象为深圳证券交易所上市交易的ETF。 |
| 29 | SglAccNetReUL | 单个账户当日净赎回上限(份) | decimal | 19.0 | 6.0 | 是 | 单个账户当日净赎回上限（份）(SglAccNetReUL)：统计对象为深圳证券交易所上市交易的ETF。 |
| 30 | IOPV | IOPV收盘价 | decimal | 19.0 | 4.0 | 是 |  |
| 31 | UpdateTime | 更新日期 | datetime |  |  | 否 |  |
| 32 | JSID | JSID | bigint |  |  | 否 |  |
