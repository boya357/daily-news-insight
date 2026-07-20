# 法规问答接口（流式）

## case-gpt-search - 法规问答（SSE 流式）

**CLI 调用**：`python3 scripts/_cli_wrapper.py call case-gpt-search --param question=...`

**接口地址**：`POST /api/caseGptSearch`

**功能说明**：基于威科 LLM 的法规问答能力。上游使用 **OpenAI 风格 SSE delta 协议** 流式推送，CLI 内部把 delta 拼接成完整 markdown 后输出到 stdout。响应中包含 `[[法规标题]]` 引用标记，可对照末尾的 `ref_doc` JSON 数组获取法规元数据（免密访问链接、法条内容、效力级别等）。

**调用场景**：
- 法律领域智能问答
- 实时返回 LLM 生成内容（适合对话式 UI）

**请求参数**（POST JSON Body）：

| 参数名 | CLI flag | 类型 | 必填 | 说明 |
|--------|----------|------|------|------|
| question | `--question` | String | 是 | 用户问题（2-1000 字符）；CLI 已做长度校验 |
| type | （CLI 自动注入 `lawGptSearch`） | String | 是 | 问答类型 |

**上游协议（实测）**：

威科上游推 SSE 帧，每帧形如：

```
event:message
data:{"choices":[{"delta":{"content":"##"},"finish_reason":null}]}

event:message
data:{"choices":[{"delta":{"content":" 结论\n"},"finish_reason":null}]}
...
```

CLI 自动做这两件事：
1. **OpenAI delta 拼接** —— 把所有 `choices[].delta.content` 直接 `Fprint` 到 stdout，无换行/空格缓冲，即拼即出
2. **未知 JSON 兜底** —— 如果某帧不是 OpenAI delta（典型：威科末尾推 ref_doc 元数据），CLI 把整段 JSON 单独输出到一行，让 agent 用 grep/jq 自行截取

> ⚠️ 历史文档（威科 PDF 第 13 页）写"观点总结数据以 markdown 的格式流式返回"，**已过时**：实际上游协议是 OpenAI delta，不是裸 markdown。CLI 已做适配。

**输出（CLI 拼接后）**：

```markdown
## 结论
全国层面并无统一的"婚假天数"规定，但明确了劳动者在依法享受婚假期间工资照发。具体婚假天数主要由地方性法规或单位内部规定确定。...

## 具体分析
1. **全国层面的基本保障与争议处理**
- 法律明确用人单位应在劳动者依法享受婚假期间支付工资，即"婚假期间工资照发"。参见：[[《中华人民共和国劳动法（2018修正）》第五十一条]]、...
- 婚假属于休息休假权益的一部分，如发生争议，纳入劳动争议范围...
...

{"ref_doc":[{"legislationTitle":"中华人民共和国劳动法（2018修正）第五十一条","content":"...","url":"https://law.wkinfo.com.cn/legislation/detail/..."}]}
```

注意末尾的 `ref_doc` JSON 块是 CLI 兜底逻辑识别出 OpenAI 帧之外的 JSON 后单独打印的，agent 应**先按 markdown 渲染主体内容，再用 jq 等工具截取末尾 JSON 行做引用元数据展开**。

**ref_doc 字段说明**：

| 字段 | 类型 | 说明 |
|------|------|------|
| topicClassification | String | 主题分类 |
| industryClassification | String | 行业分类 |
| promulgatingAgencySummary | String | 发布部门 |
| promulgatingDate | String | 发布日期 |
| levelEffect | String | 效力级别 |
| documentNumber | String | 发文字号 |
| validityStatus | String | 时效（现行有效 / 已失效） |
| url | String | 免密访问链接（含 cipher，可直接打开） |
| content | String | 法条内容 |
| effectiveDate | String | 生效日期 |
| legislationTitle | String | 法条标题（与正文中 `[[ ]]` 标记一致，可做精准匹配） |

**错误响应**：

| 状态码 | 含义 |
|--------|------|
| 500 message="问题长度不能超过 1000 个字符" | 题目长度超限（CLI 已先做检查） |

**示例**：

```bash
python3 scripts/_cli_wrapper.py call case-gpt-search --param question=全国婚假的规定
python3 scripts/_cli_wrapper.py call case-gpt-search --param question="股权激励纠纷是否属于劳动争议？"
```

**注意事项**：
- 流式接口，CLI 内部不设客户端超时
- 上游协议如果未来回退到裸 markdown 流，CLI 也能透明处理（兜底分支会按行原样输出）
- 智能体侧拿到的已经是拼好的 markdown，**不要**再尝试解析 SSE 帧
