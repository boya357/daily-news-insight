# 搜索接口

## 目录
- [search - 多维条件检索](#search---多维条件检索)

---

## search - 多维条件检索

**CLI 调用**：`python3 scripts/_cli_wrapper.py call search --param k=v ...`（用 `python3 scripts/_cli_wrapper.py schema search` 查看完整入参）

**接口地址**：`POST /api/search`

**功能说明**：在威科法规库进行组合条件检索，支持文本/标题/文号/案由/判决日期/立案日期/法律依据等多个维度的搜索。结果包含文档摘要、当事人、本院认为、裁判结果、法律依据等字段，并支持分页。

**调用场景**：
- 关键词检索同类判例
- 按案由 / 法律依据 / 案件类型筛选
- 按时间范围检索（判决日期 / 立案日期）
- 翻页加载更多结果

**请求参数**（POST JSON Body）：

| 参数名 | CLI flag | 类型 | 必填 | 说明 |
|--------|----------|------|------|------|
| type | `--type` | String | 是 | 文档类型，如 `case`、`legislation` |
| library | `--library` | String | 是 | 垂直库，如 `law` |
| body | `--body` | String | 否 | 全文搜索关键字 |
| title | `--title` | String | 否 | 标题搜索关键字 |
| documentNumber | `--document-number` | String | 否 | 文号搜索关键字 |
| judgedReason | `--judged-reason` | String | 否 | 「本院认为」关键字 |
| judgmentResult | `--judgment-result` | String | 否 | 裁判结果搜索关键字 |
| courtFoundOut | `--court-found-out` | String | 否 | 「本院查明」搜索关键字 |
| focusOfDispute | `--focus-of-dispute` | String | 否 | 争议焦点搜索关键字 |
| causeOfAction | `--cause-of-action` | String | 否 | 案由搜索关键字 |
| preciseLegalBasis | `--precise-legal-basis` | String | 否 | 法律依据搜索关键词 |
| judgmentDate | `--judgment-date` | String | 否 | 判决日期，开始/结束用 `;` 分隔；缺省用 `*` 代替（例：`2020.08.26;2024.08.26`、`*;2024.08.26`、`2024.08.26;*`） |
| filingDate | `--filing-date` | String | 否 | 立案日期，格式同上 |
| typeOfCase | `--type-of-case` | String | 否 | 案件类型 |
| typeOfDecision | `--type-of-decision` | String | 否 | 文书类型，如「判决书」 |
| party | `--party` | String | 否 | 当事人 |
| docId | `--doc-id` | String | 否 | 威科内部文档 id（urlencode） |
| limit | `--limit` | Integer | 否 | 每页条数（默认 10） |
| offset | `--offset` | Integer | 否 | 偏移量 = (页码-1) × 每页条数 |

**返回字段**：

```json
{
  "hotSearchTerm": null,
  "documentList": [{
    "id": "MjAzOTQ4MzgzODk=",
    "title": "于某芝、张某凤机动车交通事故责任纠纷民事一审民事判决书",
    "url": "https://law.wkinfo.com.cn/judgment-documents/detail/MjAzOTQ4MzgzODk%3D?...",
    "additionalFields": {
      "judgmentDate": "2024.08.26",
      "summary": "...",
      "instance": "一审",
      "documentNumber": "(2024)冀 0903 民初 4783 号",
      "referenceLevel": "其他",
      "courtLevel": "基层人民法院",
      "judgedReason": "本院认为...",
      "courtText": "河北省沧州市运河区人民法院",
      "appendixFile": false,
      "party": "于某芝/张某凤",
      "judgedResult": "...",
      "preciseLegalBasis": "[\"《中华人民共和国民法典》第一千一百八十三条\",...]"
    }
  }],
  "relationList": null,
  "count": 53412028
}
```

| 字段 | 类型 | 说明 |
|------|------|------|
| count | Integer | 总命中数 |
| documentList | List | 文档列表 |
| documentList[].id | String | 威科内部文档 id；用于获取正文与下载附件 |
| documentList[].title | String | 文档标题 |
| documentList[].url | String | 上游免密访问链接 |
| additionalFields.summary | String | 文档摘要 |
| additionalFields.judgmentDate | String | 裁判日期 |
| additionalFields.documentNumber | String | 文号 |
| additionalFields.instance | String | 审判程序（一审/二审/再审） |
| additionalFields.courtText | String | 审理法院 |
| additionalFields.courtLevel | String | 法院级别 |
| additionalFields.judgedReason | String | 本院认为 |
| additionalFields.judgedResult | String | 裁判结果 |
| additionalFields.party | String | 当事人 |
| additionalFields.preciseLegalBasis | String | 法律依据（JSON 字符串） |
| additionalFields.referenceLevel | String | 参照级别 |
| additionalFields.appendixFile | Boolean | 是否包含附件（true 时可调用 get-appendix） |

**错误响应**：

| 状态码 | 含义 | 处理建议 |
|--------|------|----------|
| 500 | 数据出错 / 用户没有权限 / 请求数据非法 | 检查参数；联系网关方核对 aipkey 配额 |
| 200 但 documentList 为空 | 无命中 | 放宽关键字或时间范围 |

**示例**：

```bash
# 1. 按全文关键字搜索
python3 scripts/_cli_wrapper.py call search \
  --param type=case --param library=law \
  --param body=婚假 --param limit=5

# 2. 按案由 + 时间范围
python3 scripts/_cli_wrapper.py call search \
  --param type=case --param library=law \
  --param causeOfAction="机动车交通事故责任纠纷" \
  --param judgmentDate="2024.01.01;2024.12.31" \
  --param limit=20

# 3. 翻页（第 3 页，每页 20）
python3 scripts/_cli_wrapper.py call search \
  --param type=case --param library=law \
  --param body=劳动合同 --param limit=20 --param offset=40
```
