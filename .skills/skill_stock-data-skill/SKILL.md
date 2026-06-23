---
name: stock-data-skill
description: 多数据源实时股票行情查询与技术分析，支持A股/港股/美股/指数，腾讯/新浪自动切换；当用户需要查股票价格、实时行情、K线、搜索股票、资金流向或技术分析时使用
---

# 实时股票数据 Skill

通过腾讯行情/新浪财经获取A股、港股、美股、指数的实时行情与历史数据。所有调用走 `python3 scripts/stock_query.py`（内部转发到 `scripts/stock-cli`），agent 不需要知道 HTTP 细节。

> **网关说明**：所有请求通过 data-provider 网关（`COZE_DATA_GATEWAY_URL`）转发到上游数据源，用于计费和鉴权。服务端的 `StockForwarder` 根据路径前缀（如 `tencent-qt`、`tencent-web`）将请求分发到对应的上游主机。

## 何时使用

- 查询个股实时行情（价格、涨跌幅、成交量、市值、PE）
- 获取历史K线数据（日/周/月/分钟级，支持前复权/后复权）
- 按名称或拼音搜索股票代码
- 查看当日分时走势
- 查看个股资金流向（大单/中单/小单分级）
- 技术面分析（MA/MACD/RSI/支撑压力位/缺口/综合信号）

## 何时不使用

- 需要基本面财报数据（营收、利润等）→ 使用财报类 skill
- 需要新闻资讯 → 使用新闻类 skill
- 需要期货/期权数据 → 本 skill 不覆盖

## 快速开始

```bash
# 列出所有可用 operation
python3 scripts/stock_query.py list

# 查看某个 op 的入参 schema
python3 scripts/stock_query.py schema quote

# 查询贵州茅台实时行情
python3 scripts/stock_query.py call quote --param code=sh600519

# 搜索股票
python3 scripts/stock_query.py call search --param keyword=茅台

# 技术分析
python3 scripts/stock_query.py call analyze --param code=sh600519
```

> 本地联调时也可以直接运行 `./scripts/stock-cli list`（macOS 本地编译版），但 **coze claw 部署必须走 `python3 scripts/stock_query.py`**。

## 环境变量

| 变量 | 必填 | 默认 | 说明 |
|------|------|------|------|
| `DATA_PROVIDER_API_KEY` | ✅ | — | data-provider 网关鉴权密钥（`dp_xxx` 格式） |
| `COZE_DATA_GATEWAY_URL` | ❌ | `https://data.coze.cn` | 网关地址，通常无需修改 |
| `COZE_DATA_PROVIDER` | ❌ | `stock` | 网关路由 provider 名称 |
| `COZE_DATA_TIMEOUT_SEC` | ❌ | `15` | 请求超时（秒） |

> `DATA_PROVIDER_API_KEY` 由 coze claw 环境自动注入。本地联调时需手动设置。

## 支持市场

| 前缀 | 市场 | 示例 |
|------|------|------|
| sh | 上交所 A 股 | sh600519（贵州茅台） |
| sz | 深交所 A 股 | sz000001（平安银行） |
| hk | 港股 | hk00700（腾讯控股） |
| us | 美股 | usAAPL（苹果） |

常用指数：`sh000001`（上证指数）、`sz399001`（深证成指）、`hkHSI`（恒生指数）

## Operations

| Operation | 用途 | 主数据源 | 详情 |
|-----------|------|---------|------|
| `quote` | 实时行情（价格/涨跌/量/市值/PE） | 腾讯→新浪 | [references/quote.md](references/quote.md) |
| `kline` | 历史K线（日/周/月/分钟，支持复权） | 腾讯 | [references/kline.md](references/kline.md) |
| `search` | 按名称/拼音搜索股票 | 腾讯 | [references/search.md](references/search.md) |
| `minute` | 当日分时数据 | 腾讯 | [references/minute.md](references/minute.md) |
| `fund-flow` | 个股资金流向（大/中/小单） | 东方财富 | [references/fund-flow.md](references/fund-flow.md) |
| `analyze` | 技术分析（MA/MACD/RSI/支撑压力/缺口/综合信号） | 内置计算 | [references/analyze.md](references/analyze.md) |

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
output=$(python3 scripts/stock_query.py call quote --param code=sh600519 2>err.log)
case $? in
  0) echo "$output" | jq . ;;
  3|4) echo "上游错误"; cat err.log ;;
  5) echo "网络异常，建议重试"; cat err.log ;;
  *) echo "用法错"; cat err.log ;;
esac
```

## 调用约定

- **股票代码格式**：`{市场前缀}{代码}`，如 `sh600519`、`hk00700`、`usAAPL`。前缀小写，美股 ticker 保留大写
- **多数据源自动切换**：quote 操作依次尝试 腾讯→新浪，任一成功即返回。kline/search/minute/analyze 仅用腾讯
- **技术分析两步走**：`analyze` 内部自动获取 K 线数据再计算指标，无需手动传入 K 线文件

## 已知限制

- **quote** 依次尝试 腾讯→新浪，任一成功即返回
- **kline** 仅腾讯（日/周/月走 fqkline，分钟线走 mkline）；新浪 K 线 API 已下线
- **search** 仅腾讯 smartbox；结果约 10 条，适合精确匹配/自动补全场景
- **fund-flow** 仍依赖东方财富，暂无替代源
- 分时数据（minute）仅依赖腾讯，无备用源
- 技术分析至少需要 20 根 K 线才能给出有效信号

## 失败降级策略（重要）

CLI 任何 op 在以下情况下视为"取数失败"：
- exit code 为 3/4/5（上游业务/服务/网络错误）
- exit code 为 0 但返回数据为空、字段缺失或明显异常（如价格为 0、时间戳过期）

**取数失败时 agent 应主动降级，不要直接报错告诉用户"查不到"**，按以下顺序兜底：

1. **重试一次**：偶发网络抖动可能恢复，仅对 exit code 5 重试 1 次
2. **联网搜索兜底**：调用可用的联网搜索/网页浏览能力，从财经站点（如新浪财经、东方财富 Web、雪球、Yahoo Finance、Google Finance）抓取所需数据
   - 实时行情：搜索"`{股票名} 股价`"或"`{code} quote`"，从权威财经站点提取最新价、涨跌幅
   - K线/历史数据：搜索"`{股票名} 历史行情`"或访问财经站点的 K 线页面
   - 资金流向：搜索"`{股票名} 资金流向 大单`"
   - 公司基本信息/股票代码：直接搜索公司名定位代码与所在交易所
3. **明确标注数据来源**：兜底数据必须在回复中说明"数据来自联网搜索（非本 Skill 实时接口）"，并附引用链接，避免让用户误以为是 CLI 的稳定结果
4. **技术分析特例**：`analyze` 依赖 K 线数据，若 kline 失败导致 analyze 不可用，先用搜索补齐 K 线再由 agent 自行计算 MA/RSI 等基础指标，或直接给出基于公开研报/资讯的定性判断并说明限制

降级原则：**优先满足用户原始诉求**，CLI 是最优路径而非唯一路径；切勿因接口故障让用户空手而归。

## 不要做

- ❌ 不要试图绕过 CLI 直接 curl 数据源：所有请求必须通过网关转发，否则无法计费和鉴权
- ❌ 不要在 CLI 成功时擅自走联网搜索兜底：仅在确认取数失败后才降级

## 服务端配置（TCC）

需要在 TCC 的 `http_proxy_config` 中添加 provider 为 `stock` 的配置项。由于 `StockForwarder` 动态构建 `FullURL`，`base_url` 可以填任意占位值：

```json
{
  "provider_name": "stock",
  "base_url": "http://placeholder.stock",
  "description": "Stock data multi-upstream proxy (Tencent/EastMoney/Sina)"
}
```

路由规则由 `StockForwarder` 内置的 `stockUpstreams` 映射表决定，不需要在 TCC 中配置具体的上游地址。
- ❌ 不要修改 `scripts/stock-cli` 的源码（源码在 `tools/stock-cli/`）
- ❌ 不要修改 `scripts/stock_query.py`：该脚本是 coze claw env 注入的唯一桥接入口，任何修改都可能导致凭证注入失败
- ❌ 不要修改 `bin/_gateway_proxy.py`（如存在）：该脚本是 skill 网关计费集成的唯一入口
- ❌ 不要在 coze claw 部署时直接运行 `./scripts/stock-cli`（会读不到托管密钥），必须走 `python3 scripts/stock_query.py`
