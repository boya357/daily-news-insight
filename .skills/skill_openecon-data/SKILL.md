---
name: openecon-data-skill
description: |
  OpenEcon 经济数据查询工具 — 自然语言查询全球宏观经济数据，覆盖 FRED、World Bank、IMF、Eurostat、BIS、OECD、UN Comtrade、Statistics Canada、ExchangeRate-API、CoinGecko 等 10 个数据源，33 万+ 指标。当用户问「美国 GDP 增速」「中国 CPI 近 5 年」「日本失业率」「全球贸易数据」时使用。触发词：GDP、CPI、PPI、失业率、通胀、经济数据、宏观经济、macro、economic data、FRED、World Bank、IMF。
---

# OpenEcon Data Skill

通过 data-provider 网关访问 OpenEcon Data 的经济数据 API。所有调用走 `python3 scripts/_cli_wrapper.py`（内部转发到 `scripts/openecon-cli`），agent 不需要知道 HTTP 细节。

> **为什么用 Python wrapper？** coze claw 仅在 Python 执行上下文注入托管密钥（`DATA_PROVIDER_API_KEY`），直接运行 Go 二进制读不到。wrapper 桥接 env 注入。

## 何时使用

- 用户查询宏观经济指标（GDP、CPI、PPI、失业率、利率、贸易额等）
- 用户需要某个国家/地区的经济时间序列数据
- 用户想比较不同国家的经济指标
- 用户查询汇率或加密货币价格（通过 ExchangeRate-API / CoinGecko）
- 用户的查询涉及 FRED、World Bank、IMF、Eurostat、OECD 等国际经济数据库

## 何时不使用

- 需要实时行情/秒级推送 — OpenEcon 为批量数据查询，非实时流
- 需要企业级微观数据（公司财报、股价） — 仅覆盖宏观经济指标
- 需要中国特有数据（A 股、国内政策文件） — 数据源以国际机构为主

## 快速开始

```bash
# 列出所有可用 operation
python3 ./scripts/_cli_wrapper.py list

# 查看 query 操作的入参 schema
python3 ./scripts/_cli_wrapper.py schema query

# 自然语言查询经济数据
python3 ./scripts/_cli_wrapper.py call query --param "query=US GDP growth last 10 years"

# 中文查询也支持
python3 ./scripts/_cli_wrapper.py call query --param "query=中国 CPI 近 5 年变化趋势"

# 追问（保持上下文）
python3 ./scripts/_cli_wrapper.py call query --param "query=show me the trend" --param "conversation_id=conv_xxx"

# 健康检查
python3 ./scripts/_cli_wrapper.py call health
```

> 本地联调时也可以直接运行 `./scripts/openecon-cli list`，但 **coze claw 部署必须走 `python3 scripts/_cli_wrapper.py`**。

## 环境变量

| 变量 | 必填 | 默认 | 说明 |
|------|------|------|------|
| `DATA_PROVIDER_API_KEY` | ✅ | — | data-provider 颁发的 dp_xxx key |
| `COZE_DATA_GATEWAY_URL` | ❌ | `https://data.coze.cn` | 网关域名 |
| `COZE_DATA_PROVIDER` | ❌ | `openecon` | 网关 provider 名（联调改 `openecon-test`）|
| `COZE_DATA_TIMEOUT_SEC` | ❌ | `120` | 单次调用超时（LLM 解析较慢，默认 2 分钟）|
| `COZE_DATA_X_USE_PPE` | ❌ | — | 联调泳道开关，设 `1` 启用 |
| `COZE_DATA_X_TT_ENV` | ❌ | — | 联调泳道名 |

凭证不接受命令行参数。

## Operations

| Operation | 用途 | 详情 |
|-----------|------|------|
| `query` | 自然语言查询经济数据（POST /api/query） | [references/query.md](references/query.md) |
| `health` | 服务健康检查（GET /api/health） | [references/health.md](references/health.md) |

## 典型查询流程

### 查询美国 GDP

```bash
python3 ./scripts/_cli_wrapper.py call query --param "query=US GDP growth last 10 years"
```

返回结构化数据，包含数据源（如 FRED）、指标名称、频率、单位、时间序列等。

### 多国比较

```bash
python3 ./scripts/_cli_wrapper.py call query --param "query=Compare unemployment rates of US, Japan, Germany from 2020 to 2025"
```

### 追问（多轮对话）

```bash
# 第一轮
output=$(python3 ./scripts/_cli_wrapper.py call query --param "query=China CPI last 5 years")
# 从返回中提取 conversationId
conv_id=$(echo "$output" | jq -r '.conversationId')

# 第二轮追问
python3 ./scripts/_cli_wrapper.py call query --param "query=now show me PPI for comparison" --param "conversation_id=$conv_id"
```

### 查询支持的数据源范围

OpenEcon 覆盖 10 个数据源：

| 数据源 | 覆盖范围 |
|--------|----------|
| FRED | 美联储经济数据（美国为主，87K+ 指标）|
| World Bank | 全球发展指标（200+ 国家）|
| IMF | 国际货币基金组织（全球宏观/财政/贸易）|
| Eurostat | 欧盟统计局（欧洲经济/社会/环境）|
| BIS | 国际清算银行（金融市场/银行统计）|
| OECD | 经合组织（38 成员国经济指标）|
| UN Comtrade | 联合国贸易统计（国际贸易流向）|
| Statistics Canada | 加拿大统计局 |
| ExchangeRate-API | 汇率数据 |
| CoinGecko | 加密货币价格 |

## Exit Code

| code | 含义 |
|------|------|
| 0 | 成功 |
| 1 | 客户端用法错误（未知子命令 / 缺参 / 格式错） |
| 2 | 鉴权失败（env 缺失或上游 401/403） |
| 3 | 上游业务错误（4xx）— 如查询无法理解（400）|
| 4 | 上游服务错误（5xx）|
| 5 | 网络 / 超时 / 协议错 |

## 错误处理范式

```bash
output=$(python3 ./scripts/_cli_wrapper.py call query --param "query=US GDP" 2>err.log)
case $? in
  0) echo "$output" | jq . ;;
  2) echo "鉴权失败，检查 DATA_PROVIDER_API_KEY"; cat err.log ;;
  3) echo "上游业务错误（查询无法解析）"; cat err.log ;;
  4) echo "上游服务错误"; cat err.log ;;
  5) echo "网络异常或超时，建议重试（默认超时 120s）"; cat err.log ;;
  *) echo "用法错"; cat err.log ;;
esac
```

## 已知限制

- 查询依赖 LLM 解析自然语言 → 响应较慢（通常 10-30 秒），默认超时 120 秒
- 返回的数据取决于 LLM 对查询意图的理解，复杂/模糊查询可能需要追问澄清
- 数据源以国际机构为主，中国本土数据覆盖有限
- 单次查询结果可能包含多个数据集（多指标/多国家），需要从返回 JSON 中筛选
- `clarificationNeeded=true` 时表示 LLM 需要更多信息，应提示用户补充查询

## 不要做

- ❌ 不要试图绕过 CLI 直接 curl 网关：CLI 处理了鉴权 header 和 exit code 映射
- ❌ 不要把 vendor 原始 token 写到任何配置：vendor secret 由网关注入
- ❌ 不要修改 `scripts/openecon-cli` 的源码（源码在 `tools/openecon-cli/`）
- ❌ 不要修改 `scripts/_cli_wrapper.py`：该脚本是 coze claw env 注入的唯一桥接入口
- ❌ 不要在 coze claw 部署时直接运行 `./scripts/openecon-cli`，必须走 `python3 scripts/_cli_wrapper.py`
