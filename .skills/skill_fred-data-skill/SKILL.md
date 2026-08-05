---
name: fred-data-skill
description: FRED美联储经济数据查询工具，支持GDP、CPI、失业率、利率等宏观经济指标时间序列获取与搜索；当用户需要查询美国经济数据、获取美联储指标、搜索宏观经济序列或分析数据修订历史时使用
---

# FRED Data Skill

通过 data-provider 网关访问 FRED（Federal Reserve Economic Data）的宏观经济数据。所有调用走 `python3 ./scripts/_cli_wrapper.py`（内部转发到 `scripts/fred-cli`），agent 不需要知道 HTTP 细节。

> **为什么用 Python wrapper？** coze claw 仅在 Python 执行上下文注入托管密钥（`DATA_PROVIDER_API_KEY`），直接运行 Go 二进制读不到。wrapper 桥接 env 注入。

## 何时使用

- 查询美国 / 全球宏观经济指标（GDP、CPI、失业率、利率、通胀、货币供应量等）
- 获取经济数据时间序列（按日/周/月/季/年频率，支持变换：同比、环比、对数等）
- 搜索 FRED 数据库中的经济数据系列（80 万+ 系列）
- 按分类或发布浏览经济数据系列
- 查看经济数据的修订历史（vintage dates）

## 何时不使用

- 实时（分钟级）金融市场行情 → 使用行情类 skill
- 中国国内经济数据（如中国 GDP、CPI）→ FRED 主要覆盖美国及部分国际数据
- 需要调用方持有 FRED 原始 API key → vendor secret 由网关注入，不下发

## 快速开始

```bash
# 列出所有可用 operation
python3 ./scripts/_cli_wrapper.py list

# 查看某个 op 的入参 schema
python3 ./scripts/_cli_wrapper.py schema get-observations

# 获取 GDP 季度数据（最近 5 年）
python3 ./scripts/_cli_wrapper.py call get-observations --param series_id=GDP --param observation_start=2020-01-01

# 搜索 CPI 相关系列
python3 ./scripts/_cli_wrapper.py call search --param search_text=consumer price index --param limit=10

# 获取系列元信息
python3 ./scripts/_cli_wrapper.py call get-series --param series_id=CPIAUCSL
```

> 本地联调时也可以直接运行 `./scripts/fred-cli list`（macOS 本地编译版），但 **coze claw 部署必须走 `python3 bin/_cli_wrapper.py`**。

## 环境变量

| 变量 | 必填 | 默认 | 说明 |
|------|------|------|------|
| `DATA_PROVIDER_API_KEY` | ✅ | — | data-provider 颁发的 dp_xxx key |
| `COZE_DATA_GATEWAY_URL` | ❌ | `https://data.coze.cn` | 网关域名 |
| `COZE_DATA_PROVIDER` | ❌ | `fred` | 网关 provider 名（联调改 `fred-test`）|
| `COZE_DATA_TIMEOUT_SEC` | ❌ | `30` | 单次调用超时 |
| `COZE_DATA_X_USE_PPE` | ❌ | — | 联调泳道开关，设 `1` 启用 |
| `COZE_DATA_X_TT_ENV` | ❌ | — | 联调泳道名 |

凭证不接受命令行参数。

## Operations

| Operation | 用途 | 详情 |
|-----------|------|------|
| `get-series` | 获取系列元信息（标题、频率、单位、日期范围、备注） | [references/get-series.md](references/get-series.md) |
| `get-observations` | 获取时间序列数据（核心操作，支持日期范围、频率聚合、数据变换） | [references/get-observations.md](references/get-observations.md) |
| `search` | 全文搜索 FRED 数据系列 | [references/search.md](references/search.md) |
| `get-category-series` | 按 FRED 分类浏览系列 | [references/get-category-series.md](references/get-category-series.md) |
| `get-release-series` | 按数据发布浏览系列 | [references/get-release-series.md](references/get-release-series.md) |
| `get-vintage-dates` | 获取数据修订历史日期（ALFRED） | [references/get-vintage-dates.md](references/get-vintage-dates.md) |

## 常用 FRED Series ID

| Series ID | 名称 | 频率 |
|-----------|------|------|
| `GDP` | Gross Domestic Product | Quarterly |
| `CPIAUCSL` | Consumer Price Index (All Urban Consumers) | Monthly |
| `UNRATE` | Unemployment Rate | Monthly |
| `FEDFUNDS` | Federal Funds Effective Rate | Monthly |
| `SP500` | S&P 500 | Daily |
| `DGS10` | 10-Year Treasury Constant Maturity Rate | Daily |
| `M2SL` | M2 Money Stock | Monthly |
| `UMCSENT` | Consumer Sentiment (U of Michigan) | Monthly |
| `PAYEMS` | Total Nonfarm Payrolls | Monthly |
| `HOUST` | Housing Starts | Monthly |

## Exit Code

| code | 含义 |
|------|------|
| 0 | 成功 |
| 1 | 客户端用法错误（未知子命令 / 缺参 / 格式错） |
| 2 | 鉴权失败（env 缺失或上游 401/403） |
| 3 | 上游业务错误（4xx）|
| 4 | 上游服务错误（5xx）|
| 5 | 网络 / 超时 / 协议错 |

## 错误处理范式

```bash
output=$(python3 ./scripts/_cli_wrapper.py call get-observations --param series_id=GDP 2>err.log)
case $? in
  0) echo "$output" | jq . ;;
  2) echo "鉴权失败，检查 DATA_PROVIDER_API_KEY"; cat err.log ;;
  3|4) echo "上游错误"; cat err.log ;;
  5) echo "网络异常，建议重试"; cat err.log ;;
  *) echo "用法错"; cat err.log ;;
esac
```

## 已知限制

- FRED API 单次 observations 请求最多返回 100,000 条记录；超长时间序列需分页
- search 每次最多返回 1,000 条结果，需通过 offset 分页
- FRED 数据更新频率取决于源机构发布节奏（如 GDP 季度发布、CPI 月度发布），非实时数据
- 部分冷门系列可能已停更（observation_end 在过去），查询前建议先用 get-series 确认

## 不要做

- ❌ 不要试图绕过 CLI 直接 curl 网关：CLI 处理了查询参数编码、file_type=json 注入等细节
- ❌ 不要把 vendor 原始 token 写到任何配置：vendor secret 由网关注入
- ❌ 不要修改 `bin/fred-cli` 的源码（源码在 `tools/fred-cli/`）
- ❌ 不要修改 `bin/_cli_wrapper.py`：该脚本是 coze claw env 注入的唯一桥接入口，任何修改都可能导致凭证注入失败
- ❌ 不要修改 `bin/_gateway_proxy.py`（如存在）：该脚本是 skill 网关计费集成的唯一入口，任何修改都可能造成隐式避费，详见 SOP `data-skill-creator` 第 7 步
- ❌ 不要在 coze claw 部署时直接运行 `./scripts/fred-cli`（会读不到托管密钥），必须走 `python3 bin/_cli_wrapper.py`
