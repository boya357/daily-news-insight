# 表名: secumain (证券主表)

## 1. 业务唯一性与数据更新频率

- **业务唯一性**: innercode
- **数据更新频率**: 日处理，不定时更新

## 2. 字段信息

| 列序号 | 列名 | 中文名称 | 列类型 | 长度 | 精度 | 字段空否 | 字段备注 |
|--------|------|----------|--------|------|------|----------|----------|
| 1 | ID | ID | bigint |  |  | 否 |  |
| 2 | innercode | 证券内部编码 | int |  |  | 否 |  |
| 3 | CompanyCode | 公司代码 | int |  |  | 是 | 公司代码(CompanyCode)：当本表SecuCategory IN (8,13)即基金相关时，对应的基金管理人代码可通过本表innercode关联MF_FundArchives.innercode，取MF_FundArchives.InvestAdvisorCode |
| 4 | SecuCode | 证券代码 | varchar | 30.0 |  | 是 |  |
| 5 | ChiName | 中文名称 | varchar | 200.0 |  | 是 |  |
| 6 | ChiNameAbbr | 中文名称缩写 | varchar | 100.0 |  | 是 |  |
| 7 | EngName | 英文名称 | varchar | 200.0 |  | 是 |  |
| 8 | EngNameAbbr | 英文名称缩写 | varchar | 50.0 |  | 是 |  |
| 9 | SecuAbbr | 证券简称 | varchar | 100.0 |  | 是 |  |
| 10 | ChiSpelling | 拼音证券简称 | varchar | 50.0 |  | 是 |  |
| 11 | ExtendedAbbr | 扩位简称 | varchar | 100.0 |  | 是 |  |
| 12 | ExtendedSpelling | 拼音扩位简称 | varchar | 50.0 |  | 是 |  |
| 13 | SecuMarket | 证券市场 | int |  |  | 是 | 18-北京证券交易所,81-三板市场,83-上海证券交易所,90-深圳证券交易所 |
| 14 | SecuCategory | 证券类别 | int |  |  | 是 | 证券类别(SecuCategory)与表(CT_SystemConst)中的字段DM关联，令LB = 1177 AND DM IN (1,2,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,23,26,27,28,29,30,31,32,33,35,36,37,38,39,40,41,42,43,44,45,46,47,55,79,80,211)，得到证券类别的描述 |
| 15 | ListedDate | 上市日期 | datetime |  |  | 是 |  |
| 16 | ListedSector | 上市板块 | int |  |  | 是 | 1-主板，2-中小企业板，3-三板，4-其他，5-大宗交易系统，6-创业板，7-科创板，8-北交所股票 |
| 17 | ListedState | 上市状态 | int |  |  | 是 | 1-上市，3-暂停，5-终止，9-其他 |
| 18 | ISIN | ISIN代码 | varchar | 20.0 |  | 是 |  |
| 19 | XGRQ | 更新时间 | datetime |  |  | 否 |  |
| 20 | JSID | JSID | bigint |  |  | 否 |  |
