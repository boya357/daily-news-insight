# 表名: dz_exgindustry (公司行业划分表)

## 1. 业务唯一性与数据更新频率

- **业务唯一性**: `CompanyCode,InfoPubDate,Standard,Industry`。
- **数据更新频率**: 日更新。

## 2. 字段信息

| 列序号 | 列名 | 中文名称 | 列类型 | 长度 | 精度 | 字段空否 | 字段备注 |
|--------|------|----------|--------|------|------|----------|----------|
| ---- | ---- | ---- | ---- | ---- | ---- | ---- |  |
| 1 | ID | ID | 100.0 | bigint | 否 |  |  |
| 2 | CompanyCode | 公司代码 | 100.0 | int | 否 | 注1 |  |
| 3 | InfoPubDate | 信息发布日期 | 100.0 | datetime | 否 |  |  |
| 4 | InfoSource | 信息来源 | 94.43 | varchar(100) |  |  |  |
| 5 | Standard | 行业划分标准 | 100.0 | int | 否 | 注2 | 只需要取值38 |
| 6 | Industry | 所属行业 | 100.0 | int | 否 | 注3 |  |
| 7 | IfPerformed | 是否执行 | 100.0 | int | 否 | 注4 | 1-是；2-否 |
| 8 | CancelDate | 取消日期 | 28.04 | datetime |  |  |  |
| 9 | FirstIndustryCode | 一级行业代码 | 100.0 | varchar(20) |  |  |  |
| 10 | FirstIndustryName | 一级行业名称 | 100.0 | varchar(100) |  |  |  |
| 11 | SecondIndustryCode | 二级行业代码 | 91.03 | varchar(20) |  |  |  |
| 12 | SecondIndustryName | 二级行业名称 | 91.03 | varchar(100) |  |  |  |
| 13 | ThirdIndustryCode | 三级行业代码 | 67.09 | varchar(20) |  |  |  |
| 14 | ThirdIndustryName | 三级行业名称 | 67.09 | varchar(100) |  |  |  |
| 15 | FourthIndustryCode | 四级行业代码 | 48.37 | varchar(20) |  |  |  |
| 16 | FourthIndustryName | 四级行业名称 | 48.37 | varchar(100) |  |  |  |
| 17 | InsertTime | 发布时间 | 100.0 | datetime | 否 |  |  |
| 18 | XGRQ | 修改日期 | 100.0 | datetime | 否 |  |  |
| 19 | JSID | JSID | 100.0 | bigint | 否 |  |  |
