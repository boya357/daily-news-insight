---
name: weko-data
description: 威科法规库查询工具，支持法规、判例、裁判文书的全文搜索、正文获取、附件下载、PDF/Word下载及法规问答；当用户需要查询中国法律法规、做法律问题问答或获取法律依据时使用
---

# 威科法规库 Data Skill

通过 data-provider 网关访问威科（Wkinfo）的中国法律法规、裁判文书与法律问答数据。所有调用走 `scripts/weko-cli`，agent 不接触任何 vendor secret。

## 何时使用

- 检索中国法律法规、判例、裁判文书（关键词、本院认为、判决日期、案由等多维过滤）
- 获取某份判决书 / 法规的正文文本
- 下载司法文档附件（zip）或文档全文（pdf / doc）
- 做法律领域问答（流式 markdown / 非流式 JSON 引用列表）

## 何时不使用

- 实时（分钟级）法律新闻 → 使用新闻类 skill
- 海外法律 → 威科目前主要覆盖中国大陆
- 任何调用方持有 vendor 原始 token 的诉求 → vendor secret 由网关注入，不下发

## 快速开始

```bash
# 列出所有 operation
python3 scripts/_cli_wrapper.py list

# 查看入参 schema
python3 scripts/_cli_wrapper.py schema search

# 调用
python3 scripts/_cli_wrapper.py call search \
  --param type=case --param library=law \
  --param body=婚假 --param limit=5
```

## 环境变量

| 变量 | 必填 | 默认 | 说明 |
|------|------|------|------|
| `DATA_PROVIDER_API_KEY` | 是 | — | data-provider 颁发的 API Key（凭证变量） |
| `DATA_PROVIDER_API_KEY_NEW` | 是 | — | data-provider 新版 API Key（凭证变量） |
| `COZE_DATA_GATEWAY_URL` | 否 | `https://data.coze.cn` | 网关域名 |
| `COZE_DATA_PROVIDER` | 否 | `weko` | 网关 provider 名（联调改 `weko-test`）|
| `COZE_DATA_TIMEOUT_SEC` | 否 | `30` | 单次调用超时 |
| `COZE_DATA_X_USE_PPE` | 否 | — | 联调泳道开关，设 `1` 启用 |
| `COZE_DATA_X_TT_ENV` | 否 | — | 联调泳道名 |

凭证不接受命令行参数。

## Operations

| Operation | 用途 | 输出 | 详情 |
|-----------|------|------|------|
| `search` | 多字段检索（标题、本院认为、判决日期等 18 字段）| JSON | [search.md](references/search.md) |
| `get-doc` | 取某份文档的正文 | JSON | [get_doc_content.md](references/get_doc_content.md) |
| `get-appendix` | 下载文档附件（octet-stream → 本地文件） | binary | [get_appendix_file.md](references/get_appendix_file.md) |
| `file-download` | 下载文档全文（doc/pdf）| binary | [file_download.md](references/file_download.md) |
| `ai-search` | 法规问答引用文档（非流式 JSON） | JSON | [ai_search.md](references/ai_search.md) |
| `case-gpt-search` | 法规问答（OpenAI delta SSE → 干净 markdown） | streaming | [case_gpt_search.md](references/case_gpt_search.md) |

## Exit Code

| code | 含义 |
|------|------|
| 0 | 成功 |
| 1 | 客户端用法错误（未知子命令 / 缺参 / 格式错） |
| 2 | 鉴权失败（env 缺失或上游 401/403） |
| 3 | 上游业务错误（4xx 非 401/403）|
| 4 | 上游服务错误（5xx）|
| 5 | 网络 / 超时 / 协议错 |

## 错误处理范式

```bash
output=$(python3 scripts/_cli_wrapper.py call search --param type=case --param library=law --param body=婚假 2>err.log)
case $? in
  0) echo "$output" | jq '.documentList[0]' ;;
  2) echo "鉴权失败"; cat err.log ;;
  3|4) echo "上游错误"; cat err.log ;;
  5) echo "网络异常，建议重试"; cat err.log ;;
  *) cat err.log ;;
esac
```

## 调用约定

- **检索 → 取详情** 两步走：`search` 拿 `documentList[].id`（base64），把 id 作为 `docId` 传给 `get-doc` / `get-appendix` / `file-download`
- **流式问答**：`case-gpt-search` 上游用 OpenAI delta SSE 协议，CLI 已拼为干净 markdown 输出 stdout（含 `[[法规标题]]` 引用标记），末尾 `ref_doc` JSON 单独一行。详见 [references/case_gpt_search.md](references/case_gpt_search.md)
- **二进制下载**：`get-appendix` / `file-download` 必须传 `--param output=<本地路径>`，stdout 写元信息 `{"output":...,"bytes":N}`，二进制流落到 `output` 文件

## 已知限制

- 部分文档没有附件，`get-appendix` 会返回 500 + `"无下载文件"`，这是上游业务正确响应（非系统错）
- 单次问答 `question` 长度 2~1000 字符
- 大附件下载受 `COZE_DATA_TIMEOUT_SEC` 限制，超大文件可临时调高

## 不要做

- 不要试图绕过 CLI 直接 curl 网关：CLI 处理了 SSE 拼接、二进制流、错误码映射
- 不要把 vendor 原始 token / aipkey 写到任何地方：vendor secret 由网关从 TCC 注入，agent 不感知
- 不要修改 `scripts/weko-cli` 的源码：源码在 `tools/weko-cli/`，发布物只走 skill 包

## 资源索引

- 脚本:见 [scripts/weko-cli](scripts/weko-cli)(用途:威科法规库CLI工具)
- 脚本:见 [scripts/_cli_wrapper.py](scripts/_cli_wrapper.py)(用途:环境变量注入包装器)
- 参考:见 [references/search.md](references/search.md)(用途:多维条件检索接口)
- 参考:见 [references/get_doc_content.md](references/get_doc_content.md)(用途:文档正文获取接口)
- 参考:见 [references/get_appendix_file.md](references/get_appendix_file.md)(用途:附件下载接口)
- 参考:见 [references/file_download.md](references/file_download.md)(用途:文档全文下载接口)
- 参考:见 [references/ai_search.md](references/ai_search.md)(用途:法规问答非流式接口)
- 参考:见 [references/case_gpt_search.md](references/case_gpt_search.md)(用途:法规问答流式接口)
