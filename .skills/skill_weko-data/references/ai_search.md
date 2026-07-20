# 法规问答引用文档接口（非流式）

## ai-search - 法规问答引用文档（一次性返回）

**CLI 调用**：`python3 scripts/_cli_wrapper.py call ai-search --param question=...`

**接口地址**：`POST /api/aiSearch`

**功能说明**：与 `case-gpt-search` 同一问题，一次性返回引用法规列表（结构化 JSON），适合智能体批量检索/对比、或不需要流式 UI 的场景。

**调用场景**：
- 给定问题，快速拿到所有相关法条（无观点总结）
- 批处理场景下的法规检索

**请求参数**（POST JSON Body）：

| 参数名 | CLI flag | 类型 | 必填 | 说明 |
|--------|----------|------|------|------|
| question | `--question` | String | 是 | 用户问题（2-1000 字符） |
| type | （CLI 自动注入 `lawGptSearch`） | String | 是 | 问答类型 |

**返回**：直接返回引用法规数组，结构与 `case-gpt-search` 末尾的 `ref_doc` 元素一致：

```json
[
  {
    "topicClassification": "劳动法,...",
    "industryClassification": "交通运输...",
    "promulgatingAgencySummary": "铁道部(已撤销)",
    "promulgatingDate": "1981.08.27",
    "levelEffect": "部门其他文件",
    "documentNumber": "〔81〕铁人字 1386 号",
    "validityStatus": "现行有效",
    "url": "https://law.wkinfo.com.cn/legislation/detail/...",
    "content": "职工父母双亡...",
    "effectiveDate": "1981.08.27",
    "legislationTitle": "铁道部关于贯彻执行《国务院关于职工探亲待遇的规定》的实施细则九、"
  }
]
```

字段含义同 [case_gpt_search.md](case_gpt_search.md#返回)。

**错误响应**：

| 状态码 | 含义 |
|--------|------|
| 500 message="问题长度不能超过 1000 个字符" | 题目长度超限（CLI 已先做检查） |

**示例**：

```bash
python3 scripts/_cli_wrapper.py call ai-search --param question=全国婚假的规定
```
