# hot / board / calendar / ipo / suspension — 市场数据

## 用途

获取市场热门排行、板块行情、财经日历、新股申购和停复牌信息。

## 数据源

腾讯自选股

## 调用

```bash
python3 ./scripts/stock_query.py call hot --param type=stock
python3 ./scripts/stock_query.py call board
python3 ./scripts/stock_query.py call calendar --param date=2024-06-01
python3 ./scripts/stock_query.py call ipo --param market=hs
python3 ./scripts/stock_query.py call suspension --param market=hs
```

## 入参

### hot — 热门排行

| 参数 | 必填 | 类型 | 说明 |
|------|------|------|------|
| type | ❌ | string | 排行类型: stock(个股)/board(板块)/etf(ETF)。默认 stock |
| limit | ❌ | int | 返回条数 |

### board — 板块行情

| 参数 | 必填 | 类型 | 说明 |
|------|------|------|------|
| code | ❌ | string | 板块代码。不传则返回板块列表概览，传入则返回指定板块详情及成分股 |

### calendar — 财经日历

| 参数 | 必填 | 类型 | 说明 |
|------|------|------|------|
| date | ❌ | string | 日期，格式 YYYY-MM-DD。默认当天 |
| limit | ❌ | int | 返回条数 |
| country | ❌ | int | 国家/市场: 1(中国)/2(美国)/3(港股) |
| indicator | ❌ | int | 事件类型: 1(经济数据)/2(央行动态)/3(重大事件)/4(休市安排) |

### ipo — 新股申购

| 参数 | 必填 | 类型 | 说明 |
|------|------|------|------|
| market | ✅ | string | 市场: hs(沪深)/hk(港股) |

### suspension — 停复牌

| 参数 | 必填 | 类型 | 说明 |
|------|------|------|------|
| market | ✅ | string | 市场: hs(沪深)/hk(港股) |

## 返回字段

返回 Markdown 表格，字段随操作不同而变化。

### hot 返回

| 字段 | 类型 | 说明 |
|------|------|------|
| rank | int | 排名 |
| code | string | 代码 |
| name | string | 名称 |
| change_percent | float | 涨跌幅(%) |
| hot_score | float | 热度值 |

### board 返回

| 字段 | 类型 | 说明 |
|------|------|------|
| code | string | 板块代码 |
| name | string | 板块名称 |
| change_percent | float | 涨跌幅(%) |
| turnover | float | 成交额 |
| top_stocks | string | 领涨股 |

### calendar 返回

| 字段 | 类型 | 说明 |
|------|------|------|
| time | string | 时间 |
| country | string | 国家/地区 |
| event | string | 事件名称 |
| importance | string | 重要性 |
| previous | string | 前值 |
| forecast | string | 预期值 |
| actual | string | 实际值 |

### ipo 返回

| 字段 | 类型 | 说明 |
|------|------|------|
| code | string | 新股代码 |
| name | string | 新股名称 |
| price | float | 发行价 |
| apply_date | string | 申购日期 |
| listing_date | string | 上市日期 |

### suspension 返回

| 字段 | 类型 | 说明 |
|------|------|------|
| code | string | 股票代码 |
| name | string | 股票名称 |
| suspend_date | string | 停牌日期 |
| resume_date | string | 复牌日期 |
| reason | string | 停牌原因 |

## 示例

```bash
# 热门个股排行(前10)
python3 ./scripts/stock_query.py call hot --param type=stock --param limit=10
# 热门板块
python3 ./scripts/stock_query.py call hot --param type=board
# 板块列表
python3 ./scripts/stock_query.py call board
# 指定板块成分股
python3 ./scripts/stock_query.py call board --param code=BK0477
# 今日财经日历(中国经济数据)
python3 ./scripts/stock_query.py call calendar --param country=1 --param indicator=1
# 沪深新股申购
python3 ./scripts/stock_query.py call ipo --param market=hs
# 港股停复牌
python3 ./scripts/stock_query.py call suspension --param market=hk
```
