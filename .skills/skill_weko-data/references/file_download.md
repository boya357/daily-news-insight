# 文档下载接口

## file-download - 下载法规/判例原文

**CLI 调用**：`python3 scripts/_cli_wrapper.py call file-download --param k=v ...`

**接口地址**：`GET /api/fileDownload`

**功能说明**：下载法规或判例的完整文档文件（doc 或 pdf 格式）。

**调用场景**：
- 下载完整判决书 / 法规原文（doc 或 pdf）
- 留存归档

**请求参数**（Query string）：

| 参数名 | CLI flag | 类型 | 必填 | 说明 |
|--------|----------|------|------|------|
| type | `--type` | String | 是 | 文档类型，如 `legislation`、`case` |
| library | `--library` | String | 是 | 垂直库，如 `law` |
| docId | `--doc-id` | String | 是 | 文档 id（urlencoded 形式） |
| fileType | `--file-type` | String | 是 | 下载格式，可选 `doc` 或 `pdf` |
| - | `--output` | Path | 是 | 输出文件本地路径 |

**返回**：

| 类型 | 说明 |
|------|------|
| octet-stream | 二进制流（doc / pdf / zip），CLI 自动写入本地 |

**错误响应**：

| 状态码 | 含义 |
|--------|------|
| 500 message="用户没有权限" | aipkey 没有该文档下载权限 |
| 500 其他 | 参数错误 / 上游异常 |

**示例**：

```bash
# 下载判决书 PDF
python3 scripts/_cli_wrapper.py call file-download --param type=case --param library=law --param docId=... --param fileType=pdf --param output=/tmp/case.pdf

# 下载法规 doc
python3 scripts/_cli_wrapper.py call file-download --param type=legislation --param library=law --param docId=... --param fileType=doc --param output=/tmp/law.doc
```
