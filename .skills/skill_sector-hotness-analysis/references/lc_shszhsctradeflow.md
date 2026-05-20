# 表名: lc_shszhsctradeflow (沪(深)港通交易流向)
说明:   
1.内容说明：收录沪深港通标的南北流向持股及资金变动信息，包括最近1日、近3日、近5日、近10日、近1月、近3月、近1年等区间统计信息。
2.数据范围：2017年3月起-至今
3.信息来源：聚源按照港交所披露衍生计算

## 1. 业务唯一性与数据更新频率

- **业务唯一性**: TradingDay,innercode
- **数据更新频率**: 日更新

## 2. 字段信息

| 列序号 | 列名 | 中文名称 | 列类型 | 长度 | 精度 | 字段空否 | 字段备注 |
|--------|------|----------|--------|------|------|----------|----------|
| 1 | ID | ID | bigint |  |  | 否 |  |
| 2 | TradingDay | 交易日期 | datetime |  |  | 否 |  |
| 3 | innercode | 证券内部编码 | int |  |  | 否 | 当TradingType=1或3时，与“证券主表（SecuMain）”中的“证券内部编码（innercode）”关联，得到A股的证券代码、证券简称及市场等信息；当TradingType=5时，与“港股证券主表（HK_SecuMain）”中的“证券内部编码（innercode）”关联，得到港股的证券代码、证券简称及市场等信息。 |
| 4 | TradingType | 交易类型 | int |  |  | 是 | 1-沪股通，3-深股通，5-港股通（沪深） |
| 5 | SHSZHSCode | 沪(深)港通证券代码 | varchar | 20.0 |  | 是 |  |
| 6 | SecuAbbr | 证券简称 | varchar | 100.0 |  | 是 |  |
| 7 | SecuCode | 股票代码 | varchar | 10.0 |  | 是 |  |
| 8 | StockChangeRD | 日变动股数(股) | decimal | 19.0 | 2.0 | 是 |  |
| 9 | MVChangeRD | 日变动市值(元) | decimal | 19.0 | 2.0 | 是 |  |
| 10 | StockChangeRDThree | 三日变动股数(股) | decimal | 19.0 | 2.0 | 是 |  |
| 11 | MVChangeRDThree | 三日变动市值(元) | decimal | 19.0 | 2.0 | 是 |  |
| 12 | StockChangeRDFive | 五日变动股数(股) | decimal | 19.0 | 2.0 | 是 |  |
| 13 | MVChangeRDFive | 五日变动市值(元) | decimal | 19.0 | 2.0 | 是 |  |
| 14 | StockChangeRDTen | 十日变动股数(股) | decimal | 19.0 | 2.0 | 是 |  |
| 15 | MVChangeRDTen | 十日变动市值(元) | decimal | 19.0 | 2.0 | 是 |  |
| 16 | StockChangeRM | 月变动股数(股) | decimal | 19.0 | 2.0 | 是 |  |
| 17 | MVChangeRM | 月变动市值(元) | decimal | 19.0 | 2.0 | 是 |  |
| 18 | StockChangeRQ | 季变动股数(股) | decimal | 19.0 | 2.0 | 是 |  |
| 19 | MVChangeRQ | 季变动市值(元) | decimal | 19.0 | 2.0 | 是 |  |
| 20 | StockChangeRY | 年变动股数(股) | decimal | 19.0 | 2.0 | 是 |  |
| 21 | MVChangeRY | 年变动市值(元) | decimal | 19.0 | 2.0 | 是 |  |
| 22 | InsertTime | 发布时间 | datetime |  |  | 否 |  |
| 23 | UpdateTime | 更新时间 | datetime |  |  | 否 |  |
| 24 | JSID | JSID | bigint |  |  | 否 |  |
