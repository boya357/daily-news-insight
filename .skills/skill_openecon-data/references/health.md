# health

健康检查，返回服务状态信息。

**CLI 调用**：`python3 ./bin/_cli_wrapper.py call health`

**上游路径**：`GET /api/health`

## 参数

无。

## 返回示例

```json
{
  "status": "ok",
  "environment": "production"
}
```
