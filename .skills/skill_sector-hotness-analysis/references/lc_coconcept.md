# 表名: lc_coconcept (概念所属公司表)

## 1. 业务唯一性与数据更新频率

- **业务唯一性**: innercode,ConceptCode,InDate。
- **数据更新频率**: 不定时更新。

## 2. 字段信息

| 列序号 | 列名 | 中文名称 | 列类型 | 长度 | 精度 | 字段空否 | 字段备注 |
|--------|------|----------|--------|------|------|----------|----------|
| ---- | ---- | ---- | ---- | ---- | ---- | ---- |  |
| 1 | ID | ID | 100.0 | bigint | 否 |  |  |
| 2 | innercode | 证券内部编码 | 100.0 | int | 否 |  |  |
| 3 | ConceptCode | 概念代码 | 100.0 | int | 否 | 与“概念板块表(lc_conceptlist)”中的“概念代码(ConceptCode)”关联，得到所属概念的信息。 |  |
| 4 | InDate | 纳入日期 | 100.0 | datetime | 否 |  |  |
| 5 | OutDate | 剔除日期 | 93.53 | datetime |  |  |  |
| 6 | IndiState | 所属状态 | 100.0 | int | 否 | 1-正常，0-终止 |  |
| 7 | Remark | 备注 | 98.87 | varchar(1000) |  | 备注(Remark):字段解释了该成分股属于此概念的原因及逻辑。 |  |
| 8 | InfoPublDate | 发布时间 | 100.0 | datetime | 否 |  |  |
| 9 | UpdateTime | 更新时间 | 100.0 | datetime | 否 |  |  |
| 10 | JSID | JSID | 100.0 | bigint | 否 |  |  |
