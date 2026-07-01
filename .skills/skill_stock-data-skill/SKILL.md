---
name: stock-data-skill
description: 多数据源股票行情查询与分析，支持A股/港股/美股/指数，覆盖行情/K线/财务/技术指标/ETF/龙虎榜/板块等；当用户需要查股价、K线、财报、技术分析或市场数据时使用
---

# 实时股票数据 Skill

通过腾讯行情/新浪财经/腾讯自选股获取A股、港股、美股、指数的实时行情、历史数据、财务报表、技术指标及市场数据。所有调用走 `python3 scripts/stock_query.py`（内部转发到 `scripts/stock-cli`），agent 不需要知道 HTTP 细节。

> **网关说明**：所有请求通过 data-provider 网关（`COZE_DATA_GATEWAY_URL`）转发到上游数据源，用于计费和鉴权。

## 何时使用

- 查询个股实时行情（价格、涨跌幅、成交量、市值、PE）
- 获取历史K线数据（日/周/月/分钟级，支持前复权/后复权）
- 按名称或拼音搜索股票代码
- 查看当日分时走势
- 查看个股资金流向（大单/中单/小单分级）
- 技术面分析（MA/MACD/RSI/支撑压力位/缺口/综合信号）
- 查询财务报表（利润表/资产负债表/现金流量表）
- 查询技术指标（MA/MACD/KDJ/RSI/BOLL等）
- 查询ETF基金数据（详情/持仓/净值）
- 查询股东结构、分红数据、筹码成本
- 查询龙虎榜、大宗交易、融资融券
- 查看热搜股票/板块、投资日历、新股日历、板块行情
- 公司简况、业绩预告

## 何时不使用

- 需要新闻资讯 → 使用新闻类 skill
- 需要期货/期权数据 → 本 skill 不覆盖

## 快速开始

```bash
# 列出所有可用 operation
python3 ./scripts/stock_query.py list

# 查看某个 op 的入参 schema
python3 ./scripts/stock_query.py schema quote

# 查询贵州茅台实时行情
python3 ./scripts/stock_query.py call quote --param code=sh600519

# 搜索股票
python3 ./scripts/stock_query.py call search --param keyword=茅台

# 技术分析
python3 ./scripts/stock_query.py call analyze --param code=sh600519

# 查询财务报表
python3 ./scripts/stock_query.py call finance --param code=sh600519

# 查询技术指标
python3 ./scripts/stock_query.py call technical --param code=sh600519

# 查询ETF详情
python3 ./scripts/stock_query.py call etf --param code=sh510300

# 查询龙虎榜
python3 ./scripts/stock_query.py call lhb --param code=sh600519

# 查看热搜
python3 ./scripts/stock_query.py call hot --param type=stock
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

### 行情与分析（原有）

| Operation | 用途 | 主数据源 | 详情 |
|-----------|------|---------|------|
| `quote` | 实时行情（价格/涨跌/量/市值/PE） | 腾讯→新浪 | [references/quote.md](references/quote.md) |
| `kline` | 历史K线（日/周/月/分钟，支持复权） | 腾讯 | [references/kline.md](references/kline.md) |
| `search` | 按名称/拼音搜索股票 | 腾讯 | [references/search.md](references/search.md) |
| `minute` | 当日分时数据 | 腾讯 | [references/minute.md](references/minute.md) |
| `analyze` | 技术分析（MA/MACD/RSI/支撑压力/缺口/综合信号） | 内置计算 | [references/analyze.md](references/analyze.md) |

### 财务与公司信息

| Operation | 用途 | 主数据源 | 详情 |
|-----------|------|---------|------|
| `finance` | 财务报表（三大报表，支持多期，A/港/美股） | 腾讯自选股 | [references/finance.md](references/finance.md) |
| `profile` | 公司简况 | 腾讯自选股 | [references/finance.md](references/finance.md) |
| `reserve` | 业绩预告 | 腾讯自选股 | [references/finance.md](references/finance.md) |

### 技术指标与筹码

| Operation | 用途 | 主数据源 | 详情 |
|-----------|------|---------|------|
| `technical` | 技术指标（MA/MACD/KDJ/RSI/BOLL/BIAS/WR/DMI） | 腾讯自选股 | [references/technical.md](references/technical.md) |
| `chip` | 筹码成本（仅沪深京A股） | 腾讯自选股 | [references/technical.md](references/technical.md) |

### 股东与分红

| Operation | 用途 | 主数据源 | 详情 |
|-----------|------|---------|------|
| `shareholder` | 股东结构（仅A股和港股） | 腾讯自选股 | [references/shareholder.md](references/shareholder.md) |
| `dividend` | 分红数据 | 腾讯自选股 | [references/shareholder.md](references/shareholder.md) |

### 资金流向（按市场）

| Operation | 用途 | 主数据源 | 详情 |
|-----------|------|---------|------|
| `asfund` | A股资金流向 | 腾讯自选股 | [references/trading.md](references/trading.md) |
| `hkfund` | 港股资金流向 | 腾讯自选股 | [references/trading.md](references/trading.md) |
| `usfund` | 美股卖空数据 | 腾讯自选股 | [references/trading.md](references/trading.md) |

### 交易数据

| Operation | 用途 | 主数据源 | 详情 |
|-----------|------|---------|------|
| `lhb` | 龙虎榜（仅沪深） | 腾讯自选股 | [references/trading.md](references/trading.md) |
| `blocktrade` | 大宗交易（仅沪深） | 腾讯自选股 | [references/trading.md](references/trading.md) |
| `margintrade` | 融资融券（仅沪深） | 腾讯自选股 | [references/trading.md](references/trading.md) |

### ETF基金

| Operation | 用途 | 主数据源 | 详情 |
|-----------|------|---------|------|
| `etf` | ETF详情 | 腾讯自选股 | [references/etf.md](references/etf.md) |
| `etf-holdings` | ETF持仓明细 | 腾讯自选股 | [references/etf.md](references/etf.md) |
| `etf-nav` | ETF净值历史 | 腾讯自选股 | [references/etf.md](references/etf.md) |

### 市场总览

| Operation | 用途 | 主数据源 | 详情 |
|-----------|------|---------|------|
| `hot` | 热搜（股票/板块/ETF） | 腾讯自选股 | [references/market.md](references/market.md) |
| `board` | 板块行情 | 腾讯自选股 | [references/market.md](references/market.md) |
| `calendar` | 投资日历 | 腾讯自选股 | [references/market.md](references/market.md) |
| `ipo` | 新股日历（沪深/港股） | 腾讯自选股 | [references/market.md](references/market.md) |
| `exdiv` | 分红除权日历 | 腾讯自选股 | [references/market.md](references/market.md) |
| `suspension` | 停复牌信息 | 腾讯自选股 | [references/market.md](references/market.md) |

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
output=$(python3 ./scripts/stock_query.py call quote --param code=sh600519 2>err.log)
case $? in
  0) echo "$output" | jq . ;;
  3|4) echo "上游错误"; cat err.log ;;
  5) echo "网络异常，建议重试"; cat err.log ;;
  *) echo "用法错"; cat err.log ;;
esac
```

## 调用约定

- **股票代码格式**：`{市场前缀}{代码}`，如 `sh600519`、`hk00700`、`usAAPL`。前缀小写，美股 ticker 保留大写
- **多数据源自动切换**：quote 操作依次尝试多个数据源，任一成功即返回。kline/search/minute 同理
- **技术分析两步走**：`analyze` 内部自动获取 K 线数据再计算指标，无需手动传入 K 线文件
- **派生指标**：本 skill 未直接提供的指标（如 PB、PCF、PS、股息率等）可通过组合现有接口数据计算得出。例如：
  - PB（市净率）= 总市值（`quote`）÷ 净资产（`finance` 资产负债表）
  - PCF（市现率）= 总市值（`quote`）÷ 经营现金流净额（`finance` 现金流量表）
  - PS（市销率）= 总市值（`quote`）÷ 营业收入（`finance` 利润表）
  - 股息率 = 每股分红（`dividend`）÷ 当前股价（`quote`）

## 已知限制

### 行情与分析

- **quote** 依次尝试多个数据源，任一成功即返回
- **kline** 日/周/月走 fqkline，分钟线走 mkline；历史数据量上限约 120 根
- **search** 结果约 10 条，适合精确匹配/自动补全场景
- 分时数据（minute）无备用源
- 技术分析至少需要 20 根 K 线才能给出有效信号

### 数据覆盖范围

- **龙虎榜（lhb）/大宗交易（blocktrade）/融资融券（margintrade）**：仅支持沪深市场
- **筹码成本（chip）**：仅支持沪深京A股
- **股东结构（shareholder）**：仅支持A股和港股
- **货币单位**：港股返回港元/美元，美股返回美元

## 不要做

- ❌ 不要试图绕过 CLI 直接 curl 数据源：所有请求必须通过网关转发，否则无法计费和鉴权

## 服务端配置（TCC）

需要在 TCC 的 `http_proxy_config` 中添加 provider 为 `stock` 的配置项：

```json
{
  "provider_name": "stock",
  "base_url": "http://placeholder.stock",
  "description": "Stock data multi-upstream proxy"
}
```
- ❌ 不要修改 `scripts/stock-cli` 的源码（源码在 `tools/stock-cli/`）
- ❌ 不要修改 `scripts/stock_query.py`：该脚本是 coze claw env 注入的唯一桥接入口，任何修改都可能导致凭证注入失败
- ❌ 不要修改 `bin/_gateway_proxy.py`（如存在）：该脚本是 skill 网关计费集成的唯一入口
- ❌ 不要在 coze claw 部署时直接运行 `./scripts/stock-cli`（会读不到托管密钥），必须走 `python3 scripts/stock_query.py`
