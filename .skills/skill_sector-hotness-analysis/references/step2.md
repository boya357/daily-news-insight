# 第二步：分析资金热度和当前价格价值水位

1. 使用[代码查询数据库](#代码查询数据库)整理相关行业、个股、概念、指数、ETF 的过去10、30、120天这三个区间的资金面和价格情况。
- 基于step1里整理出来的指数innercode，etf innercode，个股innercode，概念的conceptcode和行业industrynum
- 个股和etf：日行情表dz_dailyquote,基于innercode和tradingday，查询openprice，closeprice，highprice,lowprice，turnovervalue -> 计算区间涨跌幅、成交额、最新价格、MA10、MA30、MA120、过去120天最高价、最低价、波动率
- 指数：指数行情表qt_indexquote,基于innercode和tradingday，查询openprice，closeprice，highprice,lowprice，turnovervalue -> 计算区间涨跌幅、成交额、最新价格、MA10、MA30、MA120、过去120天最高价、最低价、波动率
- 概念：概念板块行情表qt_conceptquote,基于conceptcode和tradingday，查询openprice，closeprice，highprice,lowprice，turnovervalue -> 计算区间涨跌幅、成交额、最新价格、MA10、MA30、MA120、过去120天最高价、最低价、波动率
- 个股和指数：股票交易资金流向qt_tradingcapitalflow，基于innercode和tradingdate，查询buyvalue和sellvalue -> 计算区间主力资金净流入额(buy-sell)、单日净流入峰值（buy-sell）
- 个股：公司估值分析日指标表dz_dindicesforvaluation，基于tradingday和innerday，查询PE（动态市盈率），forwardpehr（PE历史分位），PSTTM （动态市销率），forwardpshr（PS历史分位） ->得到个股最新PE、PE历史分位，最新PS，PS的历史分位
2. 基于获取的数据，分析是否最近有热度，是否价值处于被低估状态
3. 回复用户资金、价格、估值分析一句话总结，并告知下一步将进行政策分析

除非查询报错，否则接受数据有空值的情况
