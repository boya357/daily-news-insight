
---
name: sector-hotness-analysis
description: 基于恒生聚源A股数据库和公开新闻搜索，针对指定的板块，从政策-产业-资金三方面分析板块的热度
dependency:
  python:
    - pandas
---

# A股板块政策与热度分析

## 重要的合规红线
1. 不能以扣子的身份提供任何投资建议、买卖建议、操作建议、股票代码推荐
2. 所有用代码从financeMCP数据库取出来的数据，在发给用户时，都需要注明数据来源是恒生聚源数据库。来自搜索的数据，要注明具体网站来源。
3. 所有分析内容里都要告知用户：仅供理论学习和理论练习使用，不构成投资建议，不能作为投资依据，注意投资风险，股市有风险，投资需谨慎

## 所有代码查询数据库都要先初始化MCP连接并调整sys.path
注意，finance_query在`sector-hotness-analysis/scripts/`目录下，需要将该目录加入sys.path。另外，MCP不需要手动断开连接。
你的起始路径很可能在/app/data/files目录下，如果你不调整sys.path，可能会出现找不到模块或者无法连接数据库的问题。

```python
# ================= MANDATORY SETUP =================
import sys
import os
import pandas as pd

# 必须调整sys.path，否则会找不到模块
scripts_path = os.path.join(os.getcwd(), "sector-hotness-analysis", "scripts")
if scripts_path not in sys.path:
    sys.path.insert(0, scripts_path)

from finance_query import FinanceMCP

mcp = FinanceMCP()
mcp.connect()
mcp.query(sql)
# ================= SETUP END =================
```
### 代码查询数据库指引

1. 读取相关表介绍文档，明确查询字段
  - 表介绍文档在`sector-hotness-analysis/references`目录下，文件名为表名.md
2. 编写代码获取数据并进行分析
  - 使用 create_file 工具创建 Python 代码文件（文件使用英文命名，如 info_analysis.py）
  - 代码开头需要[初始化MCP连接](#初始化MCP连接)，才能使用数据库，注意sys.path的设置
  - 数据表名称一定要小写，查询时要注意具体字段的数据格式
  - 运行代码，获取分析结果。若代码运行失败，根据错误信息，使用 edit_file 工具调试代码。
  - 允许受控 SQL JOIN，优先采用分步查询;

## 工作流程

### 第一步：明确研究对象
阅读并执行`sector-hotness-analysis/references/step1.md`

### 第二步：分析资金热度和当前价格价值水位
阅读并执行`sector-hotness-analysis/references/step2.md`

### 第三步：梳理政策时间线
阅读并执行`sector-hotness-analysis/references/step3.md`

### 第四步：梳理产业发展情况
阅读并执行`sector-hotness-analysis/references/step4.md`

### 第五步：总结并回复用户
参考`sector-hotness-analysis/references/summary.md`给用户回复完整的分析结果


## 核心数据表

| 表名称 | 说明 | 业务唯一性字段 |
|------|------|------|
| dz_dailyquote | 日行情表,有每日开收盘价、最高最低价、成交量成交额数据。没有涨幅振幅数据。 | innercode, TradingDay |
| qt_indexquote | 指数行情表 | innercode,TradingDay |
| dz_dindicesforvaluation | 公司估值分析日指标表，PE,PB等等各类估值指标 | innercode,TradingDay |
| lc_coconcept | 公司所属概念查询表 | innercode,ConceptCode,InDate |
| qt_conceptquote | 概念板块行情表 | ConceptCode,TradingDay |
| mf_etfprcomponents | 公募ETF申购赎回成分股 | innercode,TradingDay,SecuCode |
| mf_etfprlist | 公募ETF申购赎回清单 | innercode,TradingDay |
| mt_tradingdetail | 融资融券交易明细 | innercode,TradingDay |
| qt_tradingcapitalflow | 股票交易资金流向,有超大单大单（主力资金）等数据 | innercode,TradingDate,QuoteType,ValueRange |
| lc_shszhsctradeflow | 沪深港通个股交易流向，时效性比较特殊，不是单纯的T+1，是每个交易日更新前一个交易日数据 | TradingDay,innercode |

补充表（一般不从行业维度查询，都从概念为度查询，仅供用户指定要求既看概念也看板块时备用）：
| 表名称 | 说明 | 业务唯一性字段 |
|------|------|------|
| dz_exgindustry | 公司所属行业查询表，通常只用standard=38 | CompanyCode,InfoPubDate,Standard,Industry |
| lc_industryvaluation | 行业估值表 | IndustryNum,TradingDay,StatType,SectorCode |
| lc_indfinindicators | 行业财务指标表，在dz_exgindustry中取standard=38的thirdindustrycode，对应这个表的standard=41的industrynum | IndustryNum, SectorCode, InfoPubDate, EndDate, DataMark |
| lc_shszhscindtradeflow | 沪深港通行业资金流向，时效性比较特殊，不是单纯的T+1，是每个交易日更新前一个交易日数据，优先用standard=38和41 | TradingDay,TradingType,Standard,IndustryNum |

## shell工具

### security-lookup

基础流程中用于确定股票或ETF或指数代码信息，通过股票名称/代码定位证券并返回所属市场、innercode、companycode
使用示例：
`python3 sector-hotness-analysis/scripts/security_lookup_cli.py --keywords "AAPL BRK.B 000001" --format table`
`python3 sector-hotness-analysis/scripts/security_lookup_cli.py --keywords "600000" --format csv`

命名与结构
- 命令使用 kebab-case；脚本位于 `sector-hotness-analysis/scripts/*.py`；入口函数为 `main()`，支持 `--help`。
- 输入参数尽量简单明确，避免交互式输入；输出统一支持 `--format csv|table`。

输入输出约定
- 所有工具默认 UTF-8；失败时返回非 0 退出码并打印明确错误信息。
- 输出字段尽量可直接消费；涉及枚举时同时提供中文翻译字段（如 `...Desc`）。



