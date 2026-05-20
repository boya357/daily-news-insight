# 表名: ct_industrytype (行业类型表)

## 1. 业务唯一性与数据更新频率

- **业务唯一性**: `Standard,IndustryNum,EffectiveDate`。
- **数据更新频率**: 不定时更新。

## 2. 字段信息

| 列序号 | 列名 | 中文名称 | 列类型 | 长度 | 精度 | 字段空否 | 字段备注 |
|--------|------|----------|--------|------|------|----------|----------|
| ---- | ---- | ---- | ---- | ---- | ---- | ---- |  |
| 1 | `ID` | ID | 100.0 | `bigint` | 否 |  |  |
| 2 | `EffectiveDate` | 生效日期 | 42.1 | `datetime` |  |  |  |
| 3 | `CancelDate` | 取消日期 | 6.07 | `datetime` |  |  |  |
| 4 | `IsEffected` | 是否有效 | 42.1 | `int` |  | 1-是，2-否 |  |
| 5 | `Standard` | 行业分类标准 | 100.0 | `int` | 否 | 根据查询需求取38或41 |  |
| 6 | `IndustryNum` | 行业内容编码 | 100.0 | `bigint` |  |  |  |
| 7 | `Classification` | 行业级别 | 99.95 | `int` |  | 1-一级行业；2-二级行业；3-三级行业；4-四级行业；5-五级行业；6-六级行业 |  |
| 8 | `IndustryCode` | 行业代码 | 100.0 | `varchar(20)` |  |  |  |
| 9 | `IndustryName` | 行业名称 | 100.0 | `varchar(50)` |  |  |  |
| 10 | `IndustryNameE` | 行业英文名称 | 24.93 | `varchar(200)` |  |  |  |
| 11 | `SectCode` | 行业板块编码 | 0.0 | `int` |  |  |  |
| 12 | `FirstIndustryCode` | 对应一级行业代码 | 93.12 | `varchar(20)` |  |  |  |
| 13 | `FirstIndustryName` | 对应一级行业名称 | 93.12 | `varchar(100)` |  |  |  |
| 14 | `SecondIndustryCode` | 对应二级行业代码 | 87.33 | `varchar(20)` |  |  |  |
| 15 | `SecondIndustryName` | 对应二级行业名称 | 87.33 | `varchar(100)` |  |  |  |
| 16 | `ThirdIndustryCode` | 对应三级行业代码 | 70.57 | `varchar(20)` |  |  |  |
| 17 | `ThirdIndustryName` | 对应三级行业名称 | 70.16 | `varchar(100)` |  |  |  |
| 18 | `FourthIndustryCode` | 对应四级行业代码 | 35.65 | `varchar(20)` |  |  |  |
| 19 | `FourthIndustryName` | 对应四级行业名称 | 35.65 | `varchar(100)` |  |  |  |
| 20 | `UpdateTime` | 修改日期 | 100.0 | `datetime` | 否 |  |  |
| 21 | `JSID` | JSID | 100.0 | `bigint` | 否 |  |  |
