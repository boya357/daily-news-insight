# 第一步：明确研究对象

1. 如果用户没有提出需要分析的板块或者概念，则与用户澄清明确希望分析的板块或者垂类ETF，最终只能分析一个方向，基于这个方向，还要进一步确定对应的概念、行业、指数、ETF、个股
2. 确定相关指数和etf（各不超过2个）
  2.1 使用shell工具security-lookup，搜索相关的关键词，查找相关的指数和ETF，记录相关的innercode
  2.2 查询指数成交额Top2:查询指数行情表qt_indexquote,基于innercode和tradingday，查询turnovervalue，tradingday取最新的值
  2.3 查询etf成交额Top2:查询日行情表dz_dailyquote,基于innercode和tradingday，查询turnovervalue，tradingday取最新的值
3. 确定相关概念板块（不超过2个）:
  3.1 在qt_conceptquote表里查找是否有ConceptName包含相关关键词的概念板块，对应的conceptcode和conceptname
  3.2 查询概念板块成交额Top2：查询概念板块行情表qt_conceptquote,基于conceptcode和tradingday，查询turnovervalue，tradingday取最新的值
4. 确定相关个股（不超过5个）
  4.1 概念成分股：在qt_conceptquote表，查询在相关概念下对应的个股InnerCode清单，tradingday取最新的值
  4.2 查询成分股成交额Top5:查询日行情表dz_dailyquote,基于innercode和tradingday，查询turnovervalue，tradingday取最新的值
  4.3 确定Top5股票名称：在secumain查到2c-1里的innercode对应的companycode,secucode和secuname；secumarket应该为83-上海证券交易所，90-深圳证券交易所，81-三板市场，18-北京证券交易所
5. 建立一个researchlist.md，用来记录最终选择的：概念名称和代码conceptcode、指数名称和代码innercode、ETF名称和代码innercode、个股名称和代码innercode
6. 回复用户你确定的研究对象是哪些，并告知下一步计划

**完整查询完指数、概念、个股之后，再统一回复用户**
**先调用回复工具回复用户，再进行第二步。** 回复示例：
```
我将围绕下列研究对象，分析XX板块的热度：
概念板块（按成交量Top2）：XXXX
指数/ETF（按成交量TOP2）：XXX
主要个股（按成交量TOP5）：XXX,XXX……
接下来，我将先梳理板块的资金热度和当前价格价值水位，作为后续政策和产业分析归因的基础
```
