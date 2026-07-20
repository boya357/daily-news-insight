# 附件下载接口

## get-appendix - 下载文档关联附件

**CLI 调用**：`python3 scripts/_cli_wrapper.py call get-appendix --param k=v ...`

**接口地址**：`GET /api/getAppendixFile`

**功能说明**：下载文档关联的附件压缩包（zip）。仅在搜索结果中 `appendixFile=true` 时可用。

**调用场景**：
- 判决书附件（证据材料、判决书原件 zip）下载

**请求参数**（Query string）：

| 参数名 | CLI flag | 类型 | 必填 | 说明 |
|--------|----------|------|------|------|
| type | `--type` | String | 是 | 文档类型 |
| library | `--library` | String | 是 | 垂直库 |
| docId | `--doc-id` | String | 是 | 文档 id |
| - | `--output` | Path | 是 | 输出文件本地路径 |

**返回**：

| 类型 | 说明 |
|------|------|
| octet-stream | 二进制流（zip 压缩包），CLI 自动写入 `--output` 指定的本地路径 |

**错误响应**：

| 状态码 | 含义 |
|--------|------|
| 500 message="用户没有权限" | aipkey 没有该附件下载权限 |
| 500 其他 | 文档不含附件 / 上游异常 |

**示例**：

```bash
python3 scripts/_cli_wrapper.py call get-appendix --param type=case --param library=law --param docId=MjAzOTQ4MzgzODk= --param output=/tmp/appendix.zip
ls -la /tmp/appendix.zip
unzip -l /tmp/appendix.zip
```
