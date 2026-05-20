# 表名: lc_shszhscindtradeflow (沪(深)港通行业资金流向)
说明:   
1、内容说明：收录不同行业分类下沪(深)港通标的南北向资金变动信息，包括日频、周频、月频、季频、年频等区间统计信息。
2、数据范围：2017年3月起-至今
3、信息来源：聚源按照港交所披露衍生计算

## 1. 业务唯一性与数据更新频率

- **业务唯一性**: TradingDay,TradingType,Standard,IndustryNum
- **数据更新频率**: 日更新

## 2. 字段信息

| 列序号 | 列名 | 中文名称 | 列类型 | 长度 | 精度 | 字段空否 | 字段备注 |
|--------|------|----------|--------|------|------|----------|----------|
| 1 | ID | ID | bigint |  |  | 否 |  |
| 2 | TradingDay | 交易日期 | datetime |  |  | 否 |  |
| 3 | TradingType | 交易类型 | int |  |  | 否 | 当TradingType=1时，表示陆股通行业资金流向；当TradingType=2时，表示港股通行业资金流向。 |
| 4 | IndustryNum | 行业内部编码 | int |  |  | 否 | 行业内部编码(IndustryNum)与(CT_IndustryType)表中的IndustryNum字段关联，令IndustryNum=IndustryNum，得到行业内部编码的具体描述。 |
| 5 | IndustryName | 行业名称 | varchar | 50.0 |  | 是 |  |
| 6 | IndustryCode | 行业代码 | varchar | 50.0 |  | 是 |  |
| 7 | Standard | 行业划分标准 | int |  |  | 否 | 优先用38和41。22-证监会行业分类2012版，37-中信行业2019分类，38-申万行业分类(新)，41-申万行业分类2021版 |
| 8 | SharesHolding | 持股数量(股) | decimal | 19.0 | 2.0 | 是 |  |
| 9 | MarketValue | 持股市值(元) | decimal | 19.0 | 2.0 | 是 |  |
| 10 | DailyNBV | 日净流入额(元) | decimal | 19.0 | 2.0 | 是 |  |
| 11 | DailyMRatioChange | 日净流入额占行业市值比变化(%) | decimal | 19.0 | 2.0 | 是 |  |
| 12 | WeeklyNBV | 周净流入额(元) | decimal | 19.0 | 2.0 | 是 |  |
| 13 | WeeklyMRatioChange | 周净流入额占行业市值比变化(%) | decimal | 19.0 | 2.0 | 是 |  |
| 14 | MonthlyNBV | 月净流入额(元) | decimal | 19.0 | 2.0 | 是 |  |
| 15 | MonthlyMRatioChange | 月净流入额占行业市值比变化(%) | decimal | 19.0 | 2.0 | 是 |  |
| 16 | QuarterlyNBV | 季净流入额(元) | decimal | 19.0 | 2.0 | 是 |  |
| 17 | QuarterlyMRatioChange | 季净流入额占行业市值比变化(%) | decimal | 19.0 | 2.0 | 是 |  |
| 18 | YearlyNBV | 年净流入额(元) | decimal | 19.0 | 2.0 | 是 |  |
| 19 | YearlyMRatioChange | 年净流入额占行业市值比变化(%) | decimal | 19.0 | 2.0 | 是 |  |
| 20 | InsertTime | 发布时间 | datetime |  |  | 否 |  |
| 21 | UpdateTime | 更新时间 | datetime |  |  | 否 |  |
| 22 | JSID | JSID | bigint |  |  | 否 |  |
