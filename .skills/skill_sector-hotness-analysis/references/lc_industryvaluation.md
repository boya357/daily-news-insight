# 表名: lc_industryvaluation (行业估值指标表)
说明:   
内容说明：本表记录不同行业标准下的的衍生指标，包括行业静态市盈率、滚动市盈率、市净率、股息率等指标。
数据范围：2014-01-01至今
信息来源：聚源计算

## 1. 业务唯一性与数据更新频率

- **业务唯一性**: IndustryNum,TradingDay,StatType,SectorCode
- **数据更新频率**: 日更新

## 2. 字段信息

| 列序号 | 列名 | 中文名称 | 列类型 | 长度 | 精度 | 字段空否 | 字段备注 |
|--------|------|----------|--------|------|------|----------|----------|
| 1 | ID | ID | bigint |  |  | 否 |  |
| 2 | IndustryNum | 行业内部编码 | int |  |  | 否 |  |
| 3 | IndustryName | 行业名称 | varchar | 50 |  |  |  |
| 4 | Classification | 行业类别 | int |  |  |  |  |
| 5 | TradingDay | 交易日 | datetime |  |  | 否 |  |
| 6 | StatType | 统计类型 | int |  |  | 否 | 2-整体法不剔除负值 |
| 7 | SectorCode | 统计板块 | int |  |  | 否 | 5-沪、深及北交所市场 |
| 8 | Standard | 行业分类标准 | int |  |  |  | 选用41-申万行业分类2021版。 |
| 9 | IndustryCode | 行业代码 | varchar | 20 |  |  |  |
| 10 | ListedSecuNum | 上市证券数量(只) | int |  |  |  |  |
| 11 | TotalMV | 总市值(元) | decimal | 19 | 2 |  |  |
| 12 | NegotiableMV | A股流通市值(元) | decimal | 19 | 2 |  |  |
| 13 | FreeFloatMV | A股自由流通市值(元) | decimal | 19 | 2 |  |  |
| 14 | PE_TTM | 滚动市盈率 | decimal | 19 | 4 |  |  |
| 15 | PE_LYR | 静态市盈率(LVR) | decimal | 19 | 4 |  |  |
| 16 | PB_LF | 市净率(LF) | decimal | 19 | 4 |  |  |
| 17 | DividendRatio | 滚动股息率(%) | decimal | 19 | 4 |  |  |
| 18 | PCF_TTM | 滚动市现率 | decimal | 19 | 4 |  |  |
| 19 | PCF_LYR | 静态市现率(LVR) | decimal | 19 | 4 |  |  |
| 20 | PS_TTM | 滚动市销率 | decimal | 19 | 4 |  |  |
| 21 | PS_LYR | 静态市销率(LVR) | decimal | 19 | 4 |  |  |
| 22 | InsertTime | 发布时间 | datetime |  |  | 否 |  |
| 23 | UpdateTime | 修改时间 | datetime |  |  | 否 |  |
| 24 | JSID | JSID | bigint |  |  | 否 |  |

## 3. 备注说明

**注1**: 统计类型(StatType)，该字段固定以下常量：2-整体法(不剔除负值)

**注2**: 统计板块(SectorCode)，该字段固定以下常量：5-沪、深北交所市场

**注3**: 选用41。
