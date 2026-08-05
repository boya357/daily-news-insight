---
name: frankfurter-data
description: Frankfurter 汇率数据查询工具 — 覆盖 200+ 种货币、55 家央行数据源，支持最新汇率、历史汇率、时间序列查询；当用户需要查询美元兑人民币汇率、欧元走势、今日日元汇率或支持货币列表时使用
---

# Frankfurter Data Skill

通过 data-provider 网关访问 Frankfurter 汇率 API。所有调用走 `python3 scripts/cli_wrapper.py`（内部转发到 `scripts/frankfurter-cli`），agent 不需要知道 HTTP 细节。

> **为什么用 Python wrapper？** coze claw 仅在 Python 执行上下文注入托管密钥（`DATA_PROVIDER_API_KEY`），直接运行 Go 二进制读不到。wrapper 桥接 env 注入。

## 何时使用

- 用户查询某种货币对的最新汇率（如"美元兑人民币多少"）
- 用户查询历史某天的汇率（如"去年1月1号的欧元汇率"）
- 用户需要一段时间的汇率走势（时间序列）
- 用户想知道支持哪些货币或数据来源
- 用户需要做货币换算（先查汇率，再计算）

## 何时不使用

- 需要实时秒级汇率推送（Frankfurter 数据为日频更新）
- 需要加密货币（BTC/ETH 等）汇率 — 仅覆盖法定货币
- 需要银行买入/卖出价 — 仅提供央行参考汇率

## 快速开始

```bash
# 列出所有可用 operation
python3 scripts/cli_wrapper.py list

# 查看某个 op 的入参 schema
python3 scripts/cli_wrapper.py schema rates

# 查最新汇率（默认基准 EUR）
python3 scripts/cli_wrapper.py call rates --param base=USD --param quotes=CNY,EUR,JPY

# 查某天的单一货币对汇率
python3 scripts/cli_wrapper.py call rate --param base=USD --param quote=CNY --param date=2026-01-15

# 查时间序列
python3 scripts/cli_wrapper.py call rates --param base=USD --param quotes=CNY --param from=2026-04-01 --param to=2026-05-01

# 列出所有可用货币
python3 scripts/cli_wrapper.py call currencies

# 查看数据源
python3 scripts/cli_wrapper.py call providers
```

> 本地联调时也可以直接运行 `./scripts/frankfurter-cli list`，但 **coze claw 部署必须走 `python3 scripts/cli_wrapper.py`**。

## 环境变量

| 变量 | 必填 | 默认 | 说明 |
|------|------|------|------|
| `DATA_PROVIDER_API_KEY` | 是 | — | data-provider 颁发的 dp_xxx key |
| `COZE_DATA_GATEWAY_URL` | 否 | `https://data.coze.cn` | 网关域名 |
| `COZE_DATA_PROVIDER` | 否 | `frankfurter` | 网关 provider 名（联调改 `frankfurter-test`）|
| `COZE_DATA_TIMEOUT_SEC` | 否 | `30` | 单次调用超时 |
| `COZE_DATA_X_USE_PPE` | 否 | — | 联调泳道开关，设 `1` 启用 |
| `COZE_DATA_X_TT_ENV` | 否 | — | 联调泳道名 |

凭证不接受命令行参数。

## Operations

| Operation | 用途 | 详情 |
|-----------|------|------|
| `rates` | 查询汇率（最新/历史/时间序列），支持多目标货币 | [references/rates.md](references/rates.md) |
| `rate` | 查询单个货币对汇率 | [references/rate.md](references/rate.md) |
| `currencies` | 列出所有可用货币及数据源覆盖 | [references/currencies.md](references/currencies.md) |
| `currency` | 查询单个货币详情 | [references/currency.md](references/currency.md) |
| `providers` | 列出所有汇率数据源（央行） | [references/providers.md](references/providers.md) |

## 典型查询流程

### 查询美元兑人民币最新汇率

```bash
python3 scripts/cli_wrapper.py call rate --param base=USD --param quote=CNY
```

### 查询欧元兑多种货币最新汇率

```bash
python3 scripts/cli_wrapper.py call rates --param base=EUR --param quotes=USD,CNY,JPY,GBP
```

### 查询某天的历史汇率

```bash
python3 scripts/cli_wrapper.py call rates --param base=USD --param quotes=CNY --param date=2025-12-31
```

### 查询时间序列（按月降采样）

```bash
python3 scripts/cli_wrapper.py call rates --param base=USD --param quotes=CNY --param from=2025-01-01 --param to=2025-12-31 --param group=month
```

### 货币换算

Frankfurter 不提供直接换算接口，需要先查汇率再计算：

```bash
# 1. 查 USD→CNY 汇率
python3 scripts/cli_wrapper.py call rate --param base=USD --param quote=CNY
# 返回 {"base":"USD","quote":"CNY","date":"2026-05-13","rate":7.24}

# 2. 计算：100 USD = 100 × 7.24 = 724 CNY
```

## Exit Code

| code | 含义 |
|------|------|
| 0 | 成功 |
| 1 | 客户端用法错误（未知子命令 / 缺参 / 格式错） |
| 2 | 鉴权失败（env 缺失或上游 401/403） |
| 3 | 上游业务错误（4xx）— 如货币代码不存在（404）、参数无效（400/422）|
| 4 | 上游服务错误（5xx）|
| 5 | 网络 / 超时 / 协议错 |

## 错误处理范式

```bash
output=$(python3 scripts/cli_wrapper.py call rate --param base=USD --param quote=CNY 2>err.log)
case $? in
  0) echo "$output" | jq . ;;
  2) echo "鉴权失败，检查 DATA_PROVIDER_API_KEY"; cat err.log ;;
  3) echo "上游业务错误（货币不存在/参数无效）"; cat err.log ;;
  4) echo "上游服务错误"; cat err.log ;;
  5) echo "网络异常，建议重试"; cat err.log ;;
  *) echo "用法错"; cat err.log ;;
esac
```

## 已知限制

- 汇率为日频更新（央行参考汇率），非实时行情
- 不含加密货币
- 默认基准货币为 EUR，查其他基准需指定 `base` 参数
- 历史数据最早可追溯到 1948 年（取决于数据源）
- 不提供银行买卖价差，仅央行中间价

## 不要做

- 不要试图绕过 CLI 直接 curl 网关：CLI 处理了鉴权 header 和 exit code 映射
- 不要把 vendor 原始 token 写到任何配置：vendor secret 由网关注入
- 不要修改 `scripts/frankfurter-cli` 的源码（源码在 `tools/frankfurter-cli/`）
- 不要修改 `scripts/cli_wrapper.py`：该脚本是 coze claw env 注入的唯一桥接入口
- 不要在 coze claw 部署时直接运行 `./scripts/frankfurter-cli`，必须走 `python3 scripts/cli_wrapper.py`

## 资源索引

- 脚本:见 [scripts/cli_wrapper.py](scripts/cli_wrapper.py)(用途:Python wrapper，桥接环境变量注入)
- 脚本:见 [scripts/frankfurter-cli](scripts/frankfurter-cli)(用途:Go CLI二进制，汇率API客户端)
- 参考:见 [references/rates.md](references/rates.md)(用途:汇率查询参数与返回格式)
- 参考:见 [references/rate.md](references/rate.md)(用途:单货币对汇率查询)
- 参考:见 [references/currencies.md](references/currencies.md)(用途:货币列表查询)
- 参考:见 [references/currency.md](references/currency.md)(用途:单个货币详情)
- 参考:见 [references/providers.md](references/providers.md)(用途:数据源列表查询)
