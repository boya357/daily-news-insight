# 表名: mt_tradingdetail (融资融券交易明细表)

## 1. 业务唯一性与数据更新频率

- **业务唯一性**: innercode,TradingDay。
- **数据更新频率**: 日更新。

## 2. 字段信息

| 列序号 | 列名 | 中文名称 | 列类型 | 长度 | 精度 | 字段空否 | 字段备注 |
|--------|------|----------|--------|------|------|----------|----------|
| ---- | ---- | ---- | ---- | ---- | ---- | ---- |  |
| 1 | ID | ID | 100.0 | bigint | 否 |  |  |
| 2 | InfoSource | 信息来源 | 100.0 | varchar(50) |  |  |  |
| 3 | innercode | 内部编码 | 100.0 | int | 否 |  |  |
| 4 | TradingDay | 信用交易日期 | 100.0 | datetime | 否 |  |  |
| 5 | SecuMarket | 证券市场 | 100.0 | int |  | 注2 |  |
| 6 | FinanceValue | 融资余额(元) | 100.0 | decimal(19,4) |  |  |  |
| 7 | FinanceBuyValue | 融资买入额(元) | 100.0 | decimal(19,4) |  |  |  |
| 8 | FinanceRefundValue | 融资偿还额(元) | 99.96 | decimal(19,4) |  | 注3 |  |
| 9 | SecurityVolume | 融券余量(股) | 100.0 | decimal(18,2) |  |  |  |
| 10 | SecuritySellVolume | 融券卖出量(股) | 100.0 | decimal(18,2) |  |  |  |
| 11 | SecurityRefundVolume | 融券偿还量(股) | 99.96 | decimal(18,2) |  |  |  |
| 12 | SecurityValue | 融券余额(元) | 100.0 | decimal(19,4) |  | 注4 |  |
| 13 | TradingValue | 融资融券余额(元) | 100.0 | decimal(19,4) |  | 注5 |  |
| 14 | FinanTotalRatio | 融资占交易所融资余额比(%) | 100.0 | decimal(9,6) |  | 注6 |  |
| 15 | SecuriTotalRatio | 融券占交易所融券余额比(%) | 99.78 | decimal(9,6) |  | 注7 |  |
| 16 | UpdateTime | 更新时间 | 100.0 | datetime | 否 |  |  |
| 17 | JSID | JSID | 100.0 | bigint | 否 |  |  |


[ 注2 ]	18-北京证券交易所，83-上海证券交易所，90-深圳证券交易所。
[ 注3 ]	融资偿还额（FinanceRefundValue）：深/北交所=前日融资余额+本日融资买入额-本日融资余额；上交所=公布数据
[ 注4 ]	融券余额（SecurityValue）：深/北交所=公布数据；上交所=融券余量与对应的股价乘积
[ 注5 ]	融资融券余额（TradingValue）：深/北交所=公布数据；上交所=融资余额+融券余额
[ 注6 ]	融资占交易所融资余额比（FinaInTotalRatio）=融资余额/当日交易所融资余额*100
[ 注7 ]	融券占交易所融券余额比（SecuInTotalRatio）=融券余额/当日交易所融券余量金额*100