# 表名: qt_conceptquote (概念行情)
说明:   
1.收录了概念每日的行情数据，包括了常用指数的高、开、低、收等信息；
2.历史数据：2016年2月29日至今；
3.信息来源：聚源计算

## 1. 业务唯一性与数据更新频率

- **业务唯一性**: ConceptCode,TradingDay
- **数据更新频率**: 日更新

## 2. 字段信息

| 列序号 | 列名 | 中文名称 | 列类型 | 长度 | 精度 | 字段空否 | 字段备注 |
|--------|------|----------|--------|------|------|----------|----------|
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| 1 | ID | ID |  | 100.0 | bigint | 否 |  |
| 2 | ConceptCode |  | 概念代码 | 100.0 | int | 否 | 概念代码（ConceptCode）：与“ 概念板块常量表（lc_conceptlist）”中的“概念代码（ConceptCode）”关联，得到概念的名称、生成日期、备注等。 |
| 3 | ConceptName |  | 概念名称 | 100.0 | varchar(100) | 否 |  |
| 4 | HSSecuMarket |  | 恒生行情编码 | 100.0 | varchar(100) | 否 |  |
| 5 | TradingDay |  | 交易日 | 100.0 | datetime | 否 |  |
| 6 | OpenPrice |  | 开盘价 | 100.0 | decimal(19,4) | 否 |  |
| 7 | HighPrice |  | 最高价 | 100.0 | decimal(19,4) | 否 |  |
| 8 | LowPrice |  | 最低价 | 100.0 | decimal(19,4) | 否 |  |
| 9 | ClosePrice |  | 收盘价 | 100.0 | decimal(19,4) | 否 |  |
| 10 | TurnoverVolume |  | 成交量 | 100.0 | decimal(19,2) | 否 |  |
| 11 | TurnoverValue |  | 成交金额(元) | 100.0 | decimal(19,4) | 否 |  |
| 12 | ChangePCT |  | 涨跌幅(%) | 100.0 | decimal(19,2) |  |  |
| 13 | InsertTime |  | 发布时间 | 100.0 | datetime | 否 |  |
| 14 | UpdateTime |  | 修改时间 | 100.0 | datetime | 否 |  |
| 15 | JSID |  | JSID | 100.0 | bigint | 否 |  |
