# 华海诚科（688535.SH）深度研究 — 证据库

> 数据截止：2026-07-20 14:30 CST（盘中收盘前）
> 生成时间：2026-07-20

---

## 一、行情与交易

### E1-01 7月20日盘中行情（前复权）
Claim: 2026年7月20日（周一）盘中前复权价格，收盘96.96元，开盘116元，最高117.88元，最低95.08元，成交量1152万股，成交额12.10亿元，换手率8.63%；当日跌幅约-13.16%（相对前收盘111.65元）
Source: westockdata（腾讯自选股）
URL: npx westock-data-clawhub kline sh688535
Date: 2026-07-20
Excerpt: |2026-07-20 | 116 | 96.96 | 117.88 | 95.08 | 11519066 | 1210308104 | 8.63|
Context: A股周一盘中，HBM/半导体板块继续回调
Scope fit: IN-SCOPE
Confidence: HIGH

### E1-02 近5日K线数据
Claim: 7月14日收盘153元，7月15日收盘136.88元（-10.54%），7月16日122.42元（-10.56%），7月17日111.65元（-8.80%），7月20日96.96元（-13.16%）；5个交易日内从153元跌至96.96元，累计跌幅约-36.6%
Source: westockdata
URL: npx westock-data-clawhub kline sh688535
Date: 2026-07-14 ~ 07-20
Excerpt: 同上
Context: 337调查（Netlist诉三星）7月15日立案后连续暴跌
Scope fit: IN-SCOPE
Confidence: HIGH

### E1-03 历史高点
Claim: 2026年7月1日盘中创下历史最高价199.99元；7月20日96.96元较高点回撤约-51.5%
Source: westockdata K线
URL: npx westock-data-clawhub kline sh688535 --limit 130
Date: 2026-07-01
Excerpt: 7月1日盘中触及199.99元（前复权）
Context: 6月8日-6月29日累计涨幅72.52%，6月30日公司发风险提示公告时PE 863.82倍
Scope fit: IN-SCOPE
Confidence: HIGH

### E1-04 技术指标（7月20日收盘）
Claim: 7月20日收盘技术指标：MA5=124.19、MA10=143.66、MA20=154.19、MA60=129.45、MA120=106.33；MACD DIF=-4.43、DEA=4.59、MACD柱=-18.05；KDJ K=7.36、D=16.83、J=-11.60；RSI2=1.22、RSI6=16.08、RSI12=29.52、RSI24=39.87；BOLL上轨201/中轨154.19/下轨107.38。股价已跌破BOLL下轨（107.38），RSI2和KDJ-J进入极端超卖区间
Source: westockdata technical
URL: npx westock-data-clawhub technical sh688535 --group macd,rsi,ma,boll,kdj
Date: 2026-07-20
Excerpt: |sh688535|华海诚科|2026-07-20|97.01|124.19|143.66|154.19|145.74|129.45|106.33|86.00|138.00|142.44|134.41|-4.43|4.59|-18.05|7.36|16.83|-11.60|1.22|16.08|29.52|39.87|201.00|154.19|107.38|
Context: 技术面极端超卖，但MA完全空头排列
Scope fit: IN-SCOPE
Confidence: HIGH

### E1-05 资金流向（7月20日）
Claim: 7月20日主力净流出-1029.2万元；超大单净流出-69.7万元，大单净流出-959.5万元，中单净流入+2380万，小单净流出-1350.8万；融资余额10.32亿元（FinanceValue=1,031,924,996），融券余额84.37万元；融资当日净偿还约4289万（买入1.23亿，偿还1.65亿），融资余额环比-3.99%
Source: westockdata asfund
URL: npx westock-data-clawhub asfund sh688535
Date: 2026-07-20
Excerpt: {"FinanceValue":"1031924996.00","SecurityValue":"843739.05","FinanceBuyValue":"122562161.00","FinanceRefundValue":"165455946.00","FinanceValueDOD":"-3.99"}
Context: 融资盘仍高达10亿+，存在被动平仓压力
Scope fit: IN-SCOPE
Confidence: HIGH

### E1-06 大宗交易（7月20日）
Claim: 7月20日有一笔协议大宗交易，成交价125.70元/股，成交额628.5万元，折价率29.85%（相对收盘价）；买卖双方均为广发证券深圳福华一路营业部
Source: westockdata asfund BlockTradingInfos
URL: npx westock-data-clawhub asfund sh688535
Date: 2026-07-20
Excerpt: {"TradingType":"协议交易","TurnoverPrice":"125.70","TurnoverValue":"6285000.00","CloseDiscountRate":"29.85","BuySalesDepartment":"广发证券股份有限公司深圳福华一路证券营业部","SellSalesDepartment":"广发证券股份有限公司深圳福华一路证券营业部"}
Context: 同一营业部对倒，性质不明，折价近30%异常
Scope fit: IN-SCOPE
Confidence: MEDIUM

### E1-07 筹码分布
Claim: 7月20日筹码获利比例仅0.76%，平均成本151.69元，90%筹码集中度26.95%
Source: westockdata chip（之前获取）
URL: npx westock-data-clawhub chip sh688535
Date: 2026-07-20
Excerpt: 获利比例0.76%，平均成本151.69元
Context: 几乎全部筹码套牢，筹码分散
Scope fit: IN-SCOPE
Confidence: HIGH

---

## 二、公司基本面

### E2-01 公司简况
Claim: 华海诚科全称江苏华海诚科新材料股份有限公司，股票代码688535.SH，科创板；成立于2010年12月，2023年4月4日上市，发行价35元/股；注册地址江苏连云港；董事长/总经理韩江龙；注册资本约1.43亿元
Source: westockdata profile
URL: npx westock-data-clawhub profile sh688535
Date: 2026-07-20
Excerpt: 公司主营环氧塑封料（EMC）和电子胶黏剂
Context: 国内环氧塑封料龙头企业
Scope fit: IN-SCOPE
Confidence: HIGH

### E2-02 2025年全年业绩
Claim: 2025年实现营收4.58亿元（同比+38.12%），归母净利润0.24亿元（同比-39.47%），扣非净利润0.20亿元（同比-41.15%）；毛利率26.66%（+1.74pct）；环氧塑封料收入4.28亿（+35.61%，毛利率26.35%），胶黏剂0.28亿（+83.29%）；2025年EMC产量15731吨、销量14551吨；研发费用5006万元，占营收10.93%（+2.97pct）
Source: 华海诚科2025年年报
URL: https://stockmc.xueqiu.com/202603/688535_20260318_RWKH.pdf
Date: 2025年年报（2026-03-18披露）
Excerpt: 主要会计数据和财务指标
Context: 并购衡所华威2025年11月1日起并表，全年仅并表2个月
Scope fit: IN-SCOPE
Confidence: HIGH

### E2-03 2026年一季度业绩
Claim: 2026Q1营收2.23亿元（同比+165.58%，环比+38%）；归母净利润0.135亿元（同比+87.65%）；扣非0.132亿（+101.25%）；EPS 0.14元；经营现金流-2341万元（季节性因素+备料）
Source: 华海诚科2026年一季报
URL: http://vip.stock.finance.sina.com.cn/corp/view/vCB_AllBulletinDetail.php?id=12215501&stockid=688535
Date: 2026Q1（2026-04-29披露）
Excerpt: 营业收入222,757,181.42元，同比+165.58%；归母净利润13,527,139.17元，同比+87.65%
Context: 衡所华威完整并表+GMC放量驱动
Scope fit: IN-SCOPE
Confidence: HIGH

### E2-04 2025年末资产负债表要点
Claim: 2025年末总资产31.58亿元（同比+125%），归母净资产26.13亿元；有息负债约6.73亿（短期借款+长期借款+应付债券可转债）；应收账款4.09亿元，存货1.78亿元；资本公积19.02亿元（定增8亿配套募资后增厚）；商誉因衡所华威并购形成（未披露具体金额，预计数亿级）
Source: 华海诚科2025年年报
URL: https://stockmc.xueqiu.com/202603/688535_20260318_RWKH.pdf
Date: 2025-12-31
Excerpt: 资产负债表主要科目
Context: 完成衡所华威并购及8亿配套募资
Scope fit: IN-SCOPE
Confidence: HIGH

---

## 三、GMC产品与HBM国产化

### E3-01 GMC国内唯一量产地位
Claim: 华海诚科是国内唯一量产HBM专用颗粒状环氧塑封料（GMC）的企业；产品通过SK海力士HBM4 MR-MUF全工艺验证，通过三星认证，已批量供货长电科技/通富微电/华天科技等国内头部封测厂
Source: 公司公告/多家券商研报/媒体报道
URL: http://m.toutiao.com/group/7657059388296905279/
Date: 2026-06-30
Excerpt: 国内唯一实现HBM专用GMC量产企业，GMC适配MR-MUF工艺通过SK海力士HBM全工艺验证
Context: HBM-GMC国产化核心标的
Scope fit: IN-SCOPE
Confidence: MEDIUM-HIGH（多源交叉验证，但具体"通过"时间节点和出货量级缺乏官方定量披露）

### E3-02 GMC毛利率40%+
Claim: HBM专用GMC毛利率可达40%以上，显著高于传统EMC（26%左右）；产品结构升级将显著拉升公司整体毛利率
Source: 行业研报/自媒体综合
URL: http://m.toutiao.com/group/7657059388296905279/
Date: 2026-06-30
Excerpt: 先进封装GMC毛利率可超40%，显著拉升产品结构
Context: 公司2025年报未单独披露GMC毛利率，此为行业一致预期
Scope fit: IN-SCOPE
Confidence: MEDIUM

### E3-03 GMC产能规划
Claim: 原有GMC产能2000吨/年，正在扩建至5000吨/年（2026年内投产），中长期规划2万吨/年；并购衡所华威后总EMC产能2.5万吨/年，全球排名第二（仅次于日本住友电木）
Source: 公司公告/行业研究
URL: http://m.toutiao.com/group/7661773908877509160/
Date: 2026-07-13
Excerpt: 2025年收购衡所华威后合并年产销量突破2.5万吨，跃居全球出货量第二
Context: 5000吨GMC扩建进度、2万吨长周期规划属公司公开披露，但具体投产时间存在不确定性
Scope fit: IN-SCOPE
Confidence: MEDIUM

### E3-04 GMC价值量
Claim: HBM专用GMC单价约为传统基础EMC的5-10倍（传统EMC约3-7万元/吨，先进封装GMC可达30-70万元/吨）；单颗HBM芯片GMC用量约数十至数百毫克，随堆叠层数增加而线性增长
Source: 行业研究综合
URL: https://www.jiuyangongshe.com/h5/article/2z5unhdpzg7
Date: 2026-07-12
Excerpt: 国内独能量产HBM多层堆叠专用颗粒塑封料，单价为普通塑封料5-10倍
Context: 单价70万/吨、华为6亿订单等极端数据为自媒体推测，无官方来源；标注为市场预期区间
Scope fit: IN-SCOPE
Confidence: MEDIUM（单价区间合理但具体数值无官方披露）

### E3-05 [待验证] 华为6亿订单传闻
Claim: 自媒体报道"2026年GMC订单超6亿元、三年长单"，涉及华为订单
Source: 雪球/头条自媒体
URL: N/A（仅自媒体）
Date: 2026年5-6月
Excerpt: 多篇自媒体报道提及但公司未公告
Context: **公司6月30日风险提示公告明确表示"未发现对公司股票交易价格可能发生重大影响的、需要公司澄清或回应的媒体报道或市场传闻"；且公司2025全年营收仅4.58亿，单一客户6亿订单可信度存疑**
Scope fit: IN-SCOPE
Confidence: LOW（传闻性质，无官方公告支撑，与公司现有营收规模矛盾，不予采信为事实）

### E3-06 LMC/Underfill进展
Claim: 液态环氧塑封料（LMC）开始客户测试；FC底填胶（Underfill）在研；XL封装底部填充材料导热系数>2W/m·K；车规级EMC通过AEC-Q100认证
Source: 公司公开信息/研报
URL: http://m.toutiao.com/group/7657059388296905279/
Date: 2026-06
Excerpt: LMC（液态塑封料）、FC底填胶同步推进，车规级EMC通过AEC-Q100认证
Context: 产品矩阵横向拓展
Scope fit: IN-SCOPE
Confidence: MEDIUM

---

## 四、并购与资本运作

### E4-01 衡所华威并购
Claim: 2025年3月公告以11.2亿元收购衡所华威70%股权（股份支付3.2亿+可转债4.8亿+现金3.2亿），配套募资8亿元；9月1日上交所并购重组委过会，9月19日证监会注册批复，10月29日完成过户，12月完成8亿配套募资发行（发行价56.13-56.35元/股，净额7.82亿元）；2025年11月1日起并表
Source: 证监会/上交所公告
URL: http://www.csrc.gov.cn/csrc/c106192/c7584431/content.shtml
Date: 2025-09-19 / 2025-10-29
Excerpt: 证监会关于同意江苏华海诚科新材料股份有限公司向特定对象发行股票注册的批复
Context: 并购后产能翻倍、客户协同，2026Q1业绩增长主要驱动力之一
Scope fit: IN-SCOPE
Confidence: HIGH

### E4-02 股权结构（2026-05-11最新）
Claim: 前十大股东：韩江龙11.73%（1665.56万股）、德裕丰7.89%、陶军3.62%、成兴明3.38%、绍兴署辉2.69%、华天科技2.40%、上海衡所2.17%、杨森茂2.10%；实控人为韩江龙/成兴明/陶军（一致行动人）；华为哈勃投资IPO时持股3%，2025Q4-2026Q1已大幅减持，2026年5月十大股东中已不见哈勃
Source: 东方财富/同花顺/公司公告
URL: https://finance.sina.com.cn/wm/2026-05-26/doc-inhzevau9122745.shtml
Date: 2026-05-11
Excerpt: 2026年5月十大股东
Context: 哈勃退出是重要信号，但不排除仍持有未进十大的少量股份
Scope fit: IN-SCOPE
Confidence: HIGH

### E4-03 股东户数变化
Claim: 股东户数：2025-09-30为12892户→2025-12-31为14739户→2026-02-28为14116户→2026-03-31为13608户；筹码先分散后集中
Source: westockdata shareholder
URL: npx westock-data-clawhub shareholder sh688535
Date: 2026-03-31
Excerpt: |2026-03-31 | 13608|
Context: 4-6月暴涨期间股东户数大概率进一步分散（待中报披露确认）
Scope fit: IN-SCOPE
Confidence: HIGH

---

## 五、减持与解禁

### E5-01 华天科技清仓减持
Claim: 2026年5月24日华海诚科公告，第七大股东华天科技拟清仓减持340.0265万股（占总股本2.40%），减持期间为2026-05-28至2026-08-27；按当时137元/股估算可套现约4.6亿元；华天科技此前已于2026年1月完成96.01万股减持（套现1.13亿元）；减持理由系华天自身资本开支需要（南京二期30亿+华羿微电29.96亿并购）
Source: 公司减持公告/时代周报
URL: https://finance.sina.com.cn/wm/2026-05-26/doc-inhzevau9122745.shtml
Date: 2026-05-25
Excerpt: 华天科技拟减持340.0265万股，5月28日至8月27日
Context: 清仓式减持持续形成抛压
Scope fit: IN-SCOPE
Confidence: HIGH

### E5-02 其他减持
Claim: 杨森茂2026年5月完成142万股减持（占1%）；德裕丰5月询价转让减持2.85%（约404万股）
Source: 公司公告
URL: http://www.sse.com.cn/disclosure/listedinfo/announcement/c/new/2026-05-25/688535_20260525_INMU.pdf
Date: 2026-05-25
Excerpt: 减持股份计划公告
Context: 多位原始股东集中减持
Scope fit: IN-SCOPE
Confidence: HIGH

### E5-03 限售解禁
Claim: 2026-04-07已解禁2824万股（首发原股东限售，占总股本29.41%）；2026-06-23已解禁1424万股（定增限售，占10.03%，发行价56.13元/股）；2026-11-12待解禁843.5万股（定增，占5.89%，成本约37.87元/股）
Source: 同花顺/东方财富/公司公告
URL: http://www.sse.com.cn
Date: 2026
Excerpt: 限售解禁时间表
Context: 6月23日定增解禁（成本56元）在当前97元价位仍有73%浮盈，存在持续减持动力；11月12日定增成本仅37.87元，解禁后浮盈更高
Scope fit: IN-SCOPE
Confidence: HIGH

### E5-04 分红除权
Claim: 2025年年度利润分配方案为10转4.8派1元，2026年4月30日除权除息
Source: 公司2025年报
URL: https://stockmc.xueqiu.com/202603/688535_20260318_RWKH.pdf
Date: 2026-04-30
Excerpt: 以资本公积向全体股东每10股转增4.8股，派发现金红利1元
Context: 转增后总股本从约0.96亿增至约1.43亿股
Scope fit: IN-SCOPE
Confidence: HIGH

---

## 六、风险事件与催化

### E6-01 公司风险提示公告
Claim: 2026年6月29日公司发布风险提示公告（公告编号2026-025）：6月8日至6月29日累计涨幅72.52%，滚动PE 863.82倍、静态PE 1088.87倍；公司Q1经营规模较小；不存在应披露未披露信息；**特别声明"未发现需要澄清或回应的媒体报道或市场传闻"**
Source: 公司公告
URL: https://biznews.sohu.com/a/1043464647_120988533
Date: 2026-06-30
Excerpt: 截至2026年6月29日滚动市盈率863.82倍，静态市盈率1088.87倍
Context: 公司主动提示炒作风险，官方否认华为订单等重大传闻
Scope fit: IN-SCOPE
Confidence: HIGH

### E6-02 337调查事件
Claim: 2026年7月15日Netlist起诉三星/谷歌/英伟达/博通/超微337调查立案（案号337-TA-1511），调查范围为TSV/RCD专利；**不涉及封装材料EMC/GMC**；华海诚科未被列为被告；公司未单独发布澄清公告
Source: ITC公告/媒体
URL: N/A（USITC官网）
Date: 2026-07-15
Excerpt: 调查TSV、RCD相关专利侵权
Context: 引发HBM板块整体恐慌性抛售，但对华海诚科基本面无实质影响
Scope fit: IN-SCOPE
Confidence: HIGH

### E6-03 HBM板块暴跌
Claim: 7月14日-7月20日HBM板块指数本周累计跌超30%；电子板块单周跌18.84%；同期韩股公平交易委调查RCD/DB串通报价、长鑫科技IPO抽血（拟募资295亿）、两融资金连续流出等叠加
Source: 媒体报道
URL: https://www.jiuyangongshe.com/h5/article/2z5unhdpzg7
Date: 2026-07-17
Excerpt: HBM板块大幅回调
Context: 板块系统性回调，非华海个股问题
Scope fit: IN-SCOPE
Confidence: MEDIUM

### E6-04 SK海力士HBM4量产
Claim: 2026年7月14日SK海力士启动向英伟达Vera Rubin平台量产出货HBM4，9月扩大出货；SK会长崔泰源预警2027年AI半导体需求+60-100%
Source: 韩媒/DigiTimes
URL: https://www.jiuyangongshe.com/h5/article/2z5unhdpzg7
Date: 2026-07-12
Excerpt: SK海力士HBM4量产交付，2027年HBM4价格2-5美元/Gb
Context: HBM需求长期向好，GMC作为关键耗材直接受益
Scope fit: IN-SCOPE
Confidence: MEDIUM-HIGH

### E6-05 住友电木涨价
Claim: 日本住友电木宣布自2026年6月1日起全系半导体塑封料涨价10-20%
Source: 行业媒体
URL: N/A
Date: 2026-06-01
Excerpt: 住友电木半导体塑封料涨价
Context: 日系龙头涨价利好国产替代
Scope fit: IN-SCOPE
Confidence: MEDIUM

### E6-06 长鑫科技IPO
Claim: 长鑫科技5月底科创板过会，拟募资295亿元，为国产DRAM+HBM龙头；华海诚科HBM-GMC在长鑫供应链中为第三波（2026末-2028）受益标的
Source: 媒体/研报
URL: http://m.toutiao.com/group/7661773908877509160/
Date: 2026-07-13
Excerpt: 长鑫科技拟上市，国产HBM材料配套受益
Context: 长鑫IPO短期抽资，长期利好国产HBM链
Scope fit: IN-SCOPE
Confidence: MEDIUM

---

## 七、竞争格局

### E7-01 全球EMC市场
Claim: 2025年全球环氧塑封料市场约48亿美元，CAGR 6.3%；住友电木全球市占率约28-40%（不同来源差异大）、Resonac（原昭和电工+日立化成）约16-20%；华海+衡所合并后全球约18%排第二；高端HBM-GMC被住友+Resonac双寡头占95%份额
Source: 多家研报/行业数据综合
URL: http://m.toutiao.com/group/7657059388296905279/
Date: 2026-06-30
Excerpt: 高性能EMC国产化率仅10-20%，HBM专用GMC国产化率不足5%
Context: 市占率数据不同来源差异大
Scope fit: IN-SCOPE
Confidence: MEDIUM

### E7-02 国内竞争
Claim: 飞凯材料为国内EMC第二（产能约1.5万吨/年，GMC待量产，预计2026Q2送样/小批量）；长华科技、长春塑封料等在中低端EMC市场
Source: 行业研报
URL: http://m.toutiao.com/group/7657059388296905279/
Date: 2026-06-30
Excerpt: 飞凯材料HBM液态封装胶已在SK海力士量产，三星仅送样
Context: 飞凯在液态EMC(LMC/Underfill)有先发优势，华海在颗粒GMC领先
Scope fit: IN-SCOPE
Confidence: MEDIUM

---

## 八、估值与机构预期

### E8-01 当前估值（7月17日收盘）
Claim: 7月17日收盘111.65元，总市值约159.97亿元，PE(TTM)约524-660倍（不同数据源），PB约7.29倍；7月20日盘中97元对应总市值约139亿元
Source: 同花顺F10/东方财富/westockdata
URL: npx westock-data-clawhub kline sh688535
Date: 2026-07-17 / 07-20
Excerpt: 总市值=股价×1.43亿股
Context: PE极高，市值大幅回落但仍远超基本面
Scope fit: IN-SCOPE
Confidence: HIGH

### E8-02 机构盈利预测
Claim: 同花顺F10一致预期（2家机构覆盖）：2026年净利润1.05亿元（EPS 0.73元），2027年1.39亿（EPS 0.97），2028年1.89亿（EPS 1.32元）；按7月20日97元计算，2026E PE约133倍，2027E PE约100倍，2028E PE约73倍
Source: 同花顺F10
URL: N/A
Date: 2026年中
Excerpt: 机构覆盖家数仅2家，一致预期样本极小
Context: 自媒体"2026中报净利润1.6-1.9亿"为非官方估算（来源：头条自媒体），显著高于机构一致预期（全年1.05亿），需高度警惕
Scope fit: IN-SCOPE
Confidence: MEDIUM（仅2家覆盖，样本极小；中报高增为自媒体预测无官方预告）

### E8-03 富途目标价
Claim: 富途分析师一致目标价约111元/股
Source: 富途
URL: N/A
Date: 2026年中
Excerpt: 目标价111元
Context: 目标价与7月17日收盘价基本持平，隐含对当前价位"合理"判断
Scope fit: PARTIAL
Confidence: LOW（单一来源）

---

## 九、HBM行业空间

### E9-01 HBM价格翻倍预期
Claim: DigiTimes 2026年7月报道：HBM4价格2027年有望翻倍，从2026H2约2美元/Gb涨至4-5美元/Gb；三大原厂签3-5年长协锁货；HBM生产周期4-6个月、耗晶圆为DDR5的3倍
Source: DigiTimes/韭研公社
URL: https://www.jiuyangongshe.com/h5/article/2z5unhdpzg7
Date: 2026-07-11
Excerpt: HBM4价格2027年翻倍（约2→4-5美元/千兆比特）
Context: 利好上游材料
Scope fit: IN-SCOPE
Confidence: MEDIUM

### E9-02 全球先进封装市场
Claim: 2026年全球高端先进封装市场规模约587亿美元（同比+97%），2030年接近800亿美元；HBM专用GMC国产化率不足5%
Source: 行业研报
URL: http://m.toutiao.com/group/7661773908877509160/
Date: 2026-07-13
Excerpt: 2026年全球高端先进封装市场规模587亿美元
Context: 行业高景气
Scope fit: IN-SCOPE
Confidence: MEDIUM

---

## 十、龙虎榜
Claim: 7月20日龙虎榜：当日无龙虎榜数据
Source: westockdata lhb
URL: npx westock-data-clawhub lhb sh688535
Date: 2026-07-20
Excerpt: 当日无龙虎榜数据
Context: 科创板涨跌幅偏离值7%才上龙虎榜，今日跌13%但板块整体暴跌，可能因科创板指同步大跌未触发偏离值条件
Scope fit: IN-SCOPE
Confidence: HIGH
