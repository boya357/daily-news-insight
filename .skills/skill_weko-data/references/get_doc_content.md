# 获取正文接口

## get-doc - 获取文档正文

**CLI 调用**：`python3 scripts/_cli_wrapper.py call get-doc --param k=v ...`

**接口地址**：`GET /api/getDocContent`

**功能说明**：根据搜索接口返回的 `id` 获取文档完整正文。返回 JSON 结构，content 字段为全文文本，可直接用于解析、问答与摘要生成。

**调用场景**：
- 深入阅读单篇判例
- 提取裁判文书全文做摘要 / 抽取
- 法规原文获取

**请求参数**（Query string）：

| 参数名 | CLI flag | 类型 | 必填 | 说明 |
|--------|----------|------|------|------|
| type | `--type` | String | 是 | 文档类型，如 `case` |
| library | `--library` | String | 是 | 垂直库，如 `law` |
| docId | `--doc-id` | String | 是 | 搜索接口返回的 `id`（urlencoded 形式） |

**返回字段**：

```json
{
  "id": null,
  "title": "关于国家标准《网络安全技术 ...》征求意见的通知",
  "url": null,
  "additionalFields": {
    "content": "关于国家标准《网络安全技术 ...》征求意见的通知 2024-08-29\r\n\r\n各相关单位..."
  }
}
```

| 字段 | 类型 | 说明 |
|------|------|------|
| title | String | 文档标题 |
| additionalFields.content | String | 文档正文 |

**错误响应**：

| 状态码 | 含义 | 处理建议 |
|--------|------|----------|
| 500 message="用户没有权限" | aipkey 没有获取该文档正文的权限 | 联系网关方核对配额 |
| 500 其他 | 参数错误或上游异常 | 校验 docId 格式 |

**示例**：

```bash
# 直接传 base64 形式的 docId（CLI 会通过 url.Values 编码）
python3 scripts/_cli_wrapper.py call get-doc --param type=case --param library=law --param docId=MjAzOTQ4MzgzODk=
```
