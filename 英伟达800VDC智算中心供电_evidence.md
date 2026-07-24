# 英伟达800VDC智算中心供电 - Evidence File
> Compiled: 2026-07-24
> 所有引用均带内联URL，按主题分区

---

## 1. 技术背景与产业趋势

### E1-1 NVIDIA 800V HVDC架构官方定义
- **Claim**: NVIDIA于2025年5月正式定义800V HVDC高压直流供电架构，作为下一代AI工厂供配电标准。端到端效率提升5%，维护成本降70%，铜用量减45%，TCO降30%。
- **Source**: NVIDIA Developer Blog
- **URL**: https://developer.nvidia.com/blog/nvidia-800-v-hvdc-architecture-will-power-the-next-generation-of-ai-factories/
- **Date**: 2025-05-20
- **Confidence**: 高（官方一手源）
- **Excerpt**: "NVIDIA 800 V HVDC architecture will power the next generation of AI factories"；官方合作硅供应商Infineon/MPS/Navitas/ROHM/ST/TI/ADI/Innoscience/OnSemi/Renesas；电源系统组件Delta/Flex Power/Lead Wealth/LiteOn/Megmeet；电力系统Eaton/Schneider/Vertiv。

### E1-2 Rubin/Rubin Ultra/Kyber量产节奏
- **Claim**: Rubin标准版NVL72于2026Q4批量交付；Rubin Ultra NVL576(Kyber机架)2027年出货；800V高压供电与光互联按原时间表推进，黄仁勋7月11日路演否认延期传闻。
- **Source**: 东方财富/花旗/摩根士丹利调研
- **URL**: https://caifuhao.eastmoney.com/news/1741977368
- **Date**: 2026-07-12
- **Confidence**: 高
- **Excerpt**: "Rubin Ultra规划2027年正常出货...800V高压供电、光互联配套全部按原时间表推进...标准版NVL72 Rubin机柜将于2026年四季度如期交付"

### E1-3 Kyber/Rubin Ultra规格
- **Claim**: Kyber机架576颗Rubin Ultra GPU，单机柜约600kW+；Rubin Ultra NVL576 FP4推理15 ExaFLOPS，HBM4e带宽4.6PB/s，NVLink7带宽1.5PB/s，CX9机架间115.2TB/s，预计2027年下半年推出。
- **Source**: CSDN转载NVIDIA发布
- **URL**: https://blog.csdn.net/weixin_48827824/article/details/146591617
- **Date**: 2026-07-23
- **Confidence**: 中高

### E1-4 800V架构物理必然性
- **Claim**: 单机柜功率从200kW向1MW+迈进时，传统48/54V低压架构电流超12500A；800V将电流降至750A，线路损耗降至1/300，1GW负载年节电超50MW。
- **Source**: 新浪财经
- **URL**: http://finance.sina.cn/2026-05-29/detail-inhzqccr7633442.d.html
- **Date**: 2026-05-29
- **Confidence**: 高
- **Excerpt**: "单机柜功率突破600千瓦已成常态...800V直流将电流降至750安培、线路损耗骤降至近之前的三百分之一，数据中心整体能耗减少约5%"

### E1-5 四阶段演进
- **Claim**: SemiAnalysis将800V演进分为四阶段：2026-2027机柜侧装改造(Sidecar)→2027-2028原生设备落地→2028-2029全域直流配电→2029+SST固态变压器普及。
- **Source**: 新浪财经/SemiAnalysis引用
- **URL**: http://finance.sina.cn/2026-05-29/detail-inhzqccr7633442.d.html
- **Date**: 2026-05-29
- **Confidence**: 中高

### E1-6 路线之争：NVIDIA 800V单极 vs 云厂商±400V双极
- **Claim**: Google/Meta/Microsoft推动±400V双极（OCP Open Rack V3标准）；NVIDIA主导800V单极HVDC。当前NVIDIA凭借GPU话语权推动800V成为新建AI机房主流方向，但双极在存量改造中有兼容性优势。
- **Source**: 综合多源
- **URL**: https://m.weibo.cn/detail/5310948577644193
- **Date**: 2026-06-18
- **Confidence**: 中

### E1-7 铜用量节省
- **Claim**: 单机柜1MW需200kg铜排，1GW数据中心需20万kg铜；800V方案铜用量减少45%（NVIDIA官方）。
- **Source**: NVIDIA Blog
- **URL**: https://developer.nvidia.com/blog/nvidia-800-v-hvdc-architecture-will-power-the-next-generation-of-ai-factories/
- **Date**: 2025-05-20
- **Confidence**: 高

---

## 2. 市场空间与渗透率

### E2-1 花旗渗透率预测
- **Claim**: 花旗预测2030年全球数据中心容量241GW，800VDC渗透率2026年0%、2027年16%、2028年58.3%、2029年72.9%、2030年79.1%。
- **Source**: 花旗研报（行业引用）
- **Date**: 2026年中
- **Confidence**: 中高（二手引用）

### E2-2 兴业证券市场规模
- **Claim**: 兴业证券：柜外电源市场2025年340亿→2030年2710亿，CAGR=51%；2030年UPS/HVDC/SST分别92/858/1760亿元。
- **Source**: 兴业证券研报
- **Date**: 2026
- **Confidence**: 中高

### E2-3 摩根大通AI电力半导体
- **Claim**: 摩根大通：AI电力半导体市场2025年27亿→2028年160亿美元，CAGR 82%。
- **Source**: 摩根大通
- **Date**: 2026
- **Confidence**: 中高

### E2-4 摩根士丹利/ABB渗透率
- **Claim**: 摩根士丹利调研行业专家预测2030年800VDC渗透率约30%；ABB给出40-50%。
- **Source**: 摩根士丹利/ABB
- **Date**: 2026
- **Confidence**: 中

### E2-5 SemiAnalysis柜外电源与SST
- **Claim**: SemiAnalysis：电源侧柜(Power Shelf/Sidecar)市场2028年峰值110亿美元；SST市场约130亿美元(2030年)。
- **Source**: SemiAnalysis
- **Date**: 2025-2026
- **Confidence**: 中高

### E2-6 SST市场预测
- **Claim**: 英飞凌预测SST市场2030年10亿美元；第三方预测AI数据中心SST从2025年约4030万美元→2034年5.68亿美元(CAGR 30.8%)。
- **Source**: 英飞凌/行业研报
- **Date**: 2026
- **Confidence**: 中

### E2-7 磁性元件市场
- **Claim**: 可立克定增预案：2026年全球数据中心磁性元件市场190-210亿元。
- **Source**: 可立克公告
- **Date**: 2025-2026
- **Confidence**: 高

### E2-8 AI服务器电源模组市场
- **Claim**: 铭普光磁披露引用IEA：AI服务器电源模组市场2026年150亿美元、2027年325亿美元，CAGR 110%。
- **Source**: 铭普光磁/IEA
- **URL**: https://mentech-magnetic.cn/mentech-2026-world-ai-server-power-conference-magnetic-components.html
- **Date**: 2026-05-27
- **Confidence**: 中高

### E2-9 GB200/300出货预估
- **Claim**: 零氪调研预测2026年GB200/GB300全年出货67000-72000台整机柜，单柜液冷配套价值约70万元，对应液冷450-484亿元。
- **Source**: 东方财富/产业调研
- **URL**: https://caifuhao.eastmoney.com/news/20260715145956658765750
- **Date**: 2026-07-15
- **Confidence**: 中

---

## 3. 产业链标的 - 电源整机

### E3-1 麦格米特(002851) - NVIDIA官方认证
- **Claim**: A股唯一在NVIDIA 800V HVDC官方名单中的电源系统供应商(Megmeet)；全球仅台达/光宝/麦格米特三家NV认证。2025年营收94.03亿元；AI电源8.17亿(+66.52%)，电源产品整体26.80亿(占28.5%)。产品覆盖GB200/GB300/Rubin全系列5.5kW PSU+800V Sidecar；泰国工厂布局海外交付。
- **Source**: NVIDIA官网/公司年报/研报
- **URL**: https://developer.nvidia.com/blog/nvidia-800-v-hvdc-architecture-will-power-the-next-generation-of-ai-factories/
- **Date**: 2025-05-20至2026
- **Confidence**: 极高

### E3-2 中恒电气(002364) - HVDC龙头
- **Claim**: 国内HVDC市占率第一(28%-50%)，800V巴拿马电源核心供应商；阿里、字节核心HVDC供应商；墨西哥工厂服务北美；算力HVDC营收约14.2亿(占46%)。
- **Source**: 公司公告/研报
- **Date**: 2025-2026
- **Confidence**: 高

### E3-3 欧陆通(300870) - Google链
- **Claim**: 2025年数据中心电源20.15亿(+38.15%)，高功率电源12.99亿(+66.52%)；供货Google GPU电源项目，客户含浪潮/富士康/联想；2026年营收目标增长率90%；越南基地2027量产；据天风调研已被NV列入Power Shelf合作伙伴名录（技术交流阶段）。
- **Source**: 公司年报/天风调研
- **Date**: 2025-2026
- **Confidence**: 高

### E3-4 科华数据(002335) - UPS+HVDC+SST
- **Claim**: 2025年营收81.6亿(+5.2%)；智算中心35.23亿(占43.17%)；ZL310-G系列800VDC模块累计交付超5000台；腾讯HVDC份额超40%；国内UPS市占第一；牵头行业标准。
- **Source**: 公司年报
- **Date**: 2025-2026
- **Confidence**: 高

### E3-5 科士达(002518)
- **Claim**: 2025年营收52.7亿(+26.72%)；数据中心29.55亿(+13.76%)；海外占比>50%；800V HVDC/SST/巴拿马研发中尚未规模化订单。
- **Source**: 公司年报
- **Date**: 2025
- **Confidence**: 高

### E3-6 新雷能(300593) - 二三次电源
- **Claim**: 全栈电源（一次+二次+三次VPD）覆盖能力A股稀缺；800V/±400V高压变换模块小批量送样；绑定ADI合作进入谷歌/Meta等海外大客户；通信及数据中心电源基地2025年10月投产，2026Q1月产能20万只/月（7月30万），马来西亚基地2026Q4批量认证；2026Q1营收+38.8%。据产业链信息2026年AI电源营收预计8-10亿。
- **Source**: 投资者关系活动记录表/九阳公社
- **URL**: https://www.163.com/dy/article/KTOTRD7G0550WHYR.html
- **Date**: 2026-05-25（投资者活动）
- **Confidence**: 中高
- **Excerpt**: "公司针对800V及±400V供电架构做了诸多产品布局包括高压变换模块、热插拔模块等，目前这部分产品处于小批量送样中"

### E3-7 中国长城(000066) - 长城电源
- **Claim**: 长城电源PowerShelf高功率60kW机架电源，单机柜最高66kW输出，80PLUS钛金效率；服务器电源国内市占第一、国际前三；2025年营收158.09亿(+11.31%)，归母净利-5572万（亏损收窄96.23%）。目前800V HVDC产品主要面向国内信创/国产算力客户。
- **Source**: 国投证券研报
- **URL**: http://www.huiyunyan.com/doc-d939933122f1c4130795d6dbfbd67ea8.html
- **Date**: 2026-06-10
- **Confidence**: 中高

---

## 4. 功率半导体（SiC/IGBT）

### E4-1 斯达半导(603290)
- **Claim**: 国内IGBT模块出货量第一；1200V SiC MOSFET模块据称通过NV 800VDC认证（通过台达/施耐德间接供货），2025Q4起批量供货；覆盖工控/新能源/算力。
- **Source**: 公司公告/研报
- **Date**: 2025-2026
- **Confidence**: 中高

### E4-2 时代电气(688187)
- **Claim**: 轨交IGBT独家龙头+SiC IDM；650V-6500V全电压覆盖；SiC模块通过四方/金盘SST验证，2026年批量供货。
- **Source**: 公司公告/研报
- **Date**: 2025-2026
- **Confidence**: 高

### E4-3 宏微科技(688711) - 全栈功率器件
- **Claim**: IGBT+SiC混合模块已批量（适配CRPS电源PFC+LLC）；1200V SiC MOS模块小批量（适配800V HVDC高压平台）；1700V GWB模块布局SST；650V GaN HEMT送样头部ODM；规划800V GaN匹配NV 2027年800V HVDC；与北美SST龙头合作超两年，UPS份额超1/3，SST方案锁定，预计2026Q4推成品；2026H1工控(含AI电源)两位数增长，在手订单看至2027Q2。
- **Source**: 公司官网/雪球调研
- **URL**: http://www.macmicst.com/news/company-news/66
- **Date**: 2025-09-30 / 2026-07-14
- **Confidence**: 高
- **Excerpt**: "针对即将在2027年规模化部署的英伟达800V HVDC架构，公司也将推出适配该系统的GaN器件产品"

### E4-4 派瑞股份(300831)
- **Claim**: A股唯一特高压直流大功率晶闸管上市企业，国内市占65%、全球超80%；产品用于800V HVDC系统保护、稳压控制；但主业聚焦电网特高压，AI算力增量尚不显著。
- **Source**: 今日头条/东方财富
- **URL**: http://m.toutiao.com/group/7657003030612541988/
- **Date**: 2026-06-30
- **Confidence**: 中（主业非AI）

---

## 5. 电容

### E5-1 江海股份(002484) - 超级电容
- **Claim**: LIC(锂离子电容)全球双寡头之一(与日本JM武藏)；供NV BBU/VPD瞬态响应；2025年超容3.52亿(+52.51%)，薄膜电容占10.4%，铝电解81%；AI超容2026Q1仅1200万元（尚处爬坡）；薄膜电容应用于数据中心电源。
- **Source**: 公司年报/调研
- **Date**: 2025-2026
- **Confidence**: 高

### E5-2 法拉电子(600563) - 薄膜电容龙头
- **Claim**: 薄膜电容国内龙头；2025年营收53.27亿/净利11.92亿；AI薄膜电容份额35%+；单机薄膜电容用量从4颗→16颗，价值从300→1500元；间接供货台达/光宝/维谛；2026E AI收入7-10亿元；薄膜电容2026年涨价周期。
- **Source**: 公司年报/研报
- **Date**: 2025-2026
- **Confidence**: 高

### E5-3 铜峰电子(600237) - BOPP膜+薄膜电容
- **Claim**: 国内少数"拉膜-金属化-电容器"全链条厂商；电子级薄膜年产能2万吨(8条布鲁克纳产线)；金属化膜7500吨；超薄1.8μm基膜供货法拉电子等；Rubin/NVL72单机20-28颗薄膜电容；2025年AI订单占比15%+；客户覆盖比亚迪/华为/阳光电源；2026年全线涨价。
- **Source**: 第一财经研报/雪球
- **URL**: https://doccdn.yicai.com/doc/2026/07/46498f4f218b4f81906eada9a7b0031d.pdf
- **Date**: 2026-07
- **Confidence**: 中高

---

## 6. 连接器/配电/线缆

### E6-1 华丰科技(688629)
- **Claim**: 高速连接器军工背景；2025年营收25.28亿(+131.5%)；高速线模组15.55亿(+322.4%)；在手订单6.16亿；112Gbps量产/224G送样；华为核心供应商；主要高速互联而非800V配电连接器。
- **Source**: 公司年报
- **Date**: 2025
- **Confidence**: 高

### E6-2 永贵电器(300351) - 液冷+高压
- **Claim**: 2025年营收22.42亿(+10.99%)，净利0.62亿(-50.32%)；UQD液冷快接获维谛定点(3000-4000万/年)；通过NV RVL(Rack Level)认证；液冷超充枪华为独家。高压互连+液冷双布局。
- **Source**: 公司年报/调研
- **Date**: 2025
- **Confidence**: 高

### E6-3 维峰电子(301328)
- **Claim**: 2025年营收7.13亿(+33.46%)；工业连接器为主；AI+布局中但800V相关收入尚未起量。
- **Source**: 公司年报
- **Date**: 2025
- **Confidence**: 高

### E6-4 沃尔核材(002130) - 高速铜缆
- **Claim**: 高速通信线(铜缆)；2025年高速通信线10.17亿(+238%)；224G大批量交付/448G样品验证；全球第三大通信电缆商；属于信号互联而非800V电力传输。
- **Source**: 公司年报
- **Date**: 2025
- **Confidence**: 高

### E6-5 宝胜股份(600973) - 电力+信号线缆
- **Claim**: 800V高压直流特种供电电缆（机房主动脉）+224G NVLink DAC铜缆（国内少数拿到NV官方NVLink认证，浸没液冷耐冷媒）；6N高纯铜自产；2024年算力DAC+通信线缆4.17亿；2025年算力板块8.1亿(翻倍)，224G占40%、毛利率35%；2026年6月产能扩张完成；中标腾讯韶关液冷算力中心总包。
- **Source**: 东方财富财富号
- **URL**: https://caifuhao.eastmoney.com/news/20260618084958887060330
- **Date**: 2026-06
- **Confidence**: 中（部分为自媒体分析）

### E6-6 泰永长征(002927) - SSCB固态断路器
- **Claim**: A股高压大功率SSCB（固态断路器）绝对龙头；MBS1系列DC800V SSCB 2026年6月正式在国内头部运营商800V数据中心投运；额定电流40-6300A，DC800-1500V；10μs分断速度；500-2500A全功率覆盖；深度绑定台达电子（NV Rubin供应链）；通过CCS船级社认证；移相变压器已规模化量产；SST在研。全球仅泰永/ABB/伊顿3家量产800V/2500A SSCB。
- **Source**: 证券时报/公司新闻/九阳公社
- **URL**: http://m.toutiao.com/group/7650301477650448948/
- **Date**: 2026-06-12（运营商投运）
- **Confidence**: 高
- **Excerpt**: "自研量产的MBS1系列DC800V固态断路器(SSCB)正式在国内头部运营商800V高压直流数据中心项目完成投运，标志国产高压直流固态保护产品...全面走向运营商规模化落地应用"

### E6-7 宏发股份(600885) - 高压直流继电器
- **Claim**: 全球电磁继电器市占第一(连续13年双增长)；2025年继电器收入157.03亿(占91.28%)；高压直流继电器全球市占约40%；AIDC电源/UPS继电器间接受益800V趋势；新能源高压直流继电器2026Q1发货+50%；75+战略低压电器成套2026Q1+70%。
- **Source**: 今日头条/公司年报
- **URL**: http://m.toutiao.com/group/7662194641864753705/
- **Date**: 2026-07-14
- **Confidence**: 中高
- **Caveat**: AIDC业务目前非主力，主要弹性在新能源+储能

### E6-8 中熔电气(301031) - 高压熔断器
- **Claim**: 与台达/维谛合作供应800V HVDC熔断器；AI数据中心单柜熔断器价值量4000-6000元（传统10倍）；2026H1净利超2亿（2024H1为1.37亿）；"算力卫士"微型直流熔断器模组打入中科曙光/寒武纪/昆仑芯供应链；单台熔断器价值50-100美元，远期市场10-20亿美元。
- **Source**: 搜狐/东方财富
- **URL**: https://caifuhao.eastmoney.com/news/20260605164936063442370
- **Date**: 2026-06/07
- **Confidence**: 中高

---

## 7. 磁元件/磁材

### E7-1 可立克(002782)
- **Claim**: 定增3.89亿扩产AI算力电源磁性元件（LLC/DAB变压器、平面变压器、谐振电感）；2025年磁性元件收入46.3亿(占83.70%)；已开发10kV SST高频变压器(20kHz-100kHz/15-120kW)；拟定增1.28亿专项投向SST研发。
- **Source**: 公司公告/新浪财经研报
- **URL**: http://stock.finance.sina.com.cn/stock/go.php/vReport_Show/kind/lastest/rptid/837782604661/index.phtml
- **Date**: 2026-07-19
- **Confidence**: 高

### E7-2 京泉华(002885)
- **Claim**: MFT隔离变压器（SST核心部件）重点产品；2026H1预告归母净利6500-7300万(+57.40%-76.77%)；AI服务器用超薄扁平化一体成型电感打入英伟达GB200液冷服务器二级供应链（上半年贡献毛利超2800万）；客户覆盖光储/充电桩/数据中心。
- **Source**: 搜狐/公司官网
- **URL**: https://m.sohu.com/a/1049731388_122066679/
- **Date**: 2026-07-13
- **Confidence**: 中高

### E7-3 铭普光磁(002902)
- **Claim**: 已成功开发适配400V-800V高压平台的完整电源磁性器件解决方案；覆盖一次到三次电源（驱动变压器/共模/PFC/主功率/滤波电感/TLVR/一体成型）；SST高压隔离变压器量产交付（据公司互动易）；自研专属磁材配方+利兹线绕线工艺；AI服务器电源模组市场2026-2027年CAGR 110%。
- **Source**: 公司官网/互动易
- **URL**: https://mentech-magnetic.cn/mentech-2026-world-ai-server-power-conference-magnetic-components.html
- **Date**: 2026-05-27 / 2026-07-03
- **Confidence**: 中高
- **Caveat**: 雪球等自媒体宣传"国内唯一SST高压隔离变压器规模化量产"存在争议，四方股份/伊戈尔均有SST进展，需谨慎

### E7-4 伊戈尔(002922)
- **Claim**: 发布君诺JUNO系列SST（35kV/10MVA，效率98.3%，功率密度1.8MW/m³）；巴拿马电源移相变压器阿里云唯一/核心供应商(市占75%+)、腾讯70%份额；2025年AIDC订单+400%锁定至2027；斩获谷歌2.5亿、微软1.8亿订单，台达日本东京数据中心5亿；与国网电科院联合攻关高频铁芯材料；与阿里云联合开发35kV/10MVA SST预计2027年量产；KEMA认证推进中。
- **Source**: 雪球/新浪财经研报
- **URL**: https://xueqiu.com/1089149407/380846565
- **Date**: 2026-03
- **Confidence**: 中高（部分为自媒体）

### E7-5 铂科新材(300811) - VPD/TLVR电感
- **Claim**: 金属软磁粉芯+芯片电感垂直整合；VPD(垂直供电)模块电感全球双寡头之一，直供NV一级电源厂(MPS/伟创力/广达)，GB200/Rubin标配；2025年模块式电感占电感营收30-40%，2026E突破50%；芯片电感产能2026年扩至3-4亿片；TLVR电感2025年批量出货，2026年大幅增加；惠东新基地2026年投产后产能+400%；Rubin VPD单颗21-22元（传统TLVR 2.8-3.5元），毛利率45-52%；全球VPD电感市占率超70%。
- **Source**: 公司调研/新浪财经
- **URL**: https://finance.sina.com.cn/stock/aigc/jgdy/2026-07-01/doc-inifheyw4281958.shtml.md
- **Date**: 2026-06-25至30日调研
- **Confidence**: 高

### E7-6 顺络电子(002138) - TLVR龙头
- **Claim**: 全球TLVR市场份额15-20%（全球第二，仅次于村田/TDK合计80%）；国内首家、全球少数三家（村田/TDK/顺络）稳定量产TLVR厂商；掌握模压/铜磁共烧/组装三条TLVR工艺（国内唯一全工艺）；通过英飞凌/MPS/ADI认证，间接批量导入NV整机；国内智算(浪潮/华为/超聚变)二供；单机8卡AI服务器TLVR用量80-120颗；TLVR毛利率35-45%，高端70%。
- **Source**: 顺络官网/今日头条
- **URL**: https://www.sunlordinc.com/uploads/files/20251218/
- **Date**: 2025-12至2026-06
- **Confidence**: 中高

---

## 8. SST固态变压器

### E8-1 四方股份(601126)
- **Claim**: SST龙头；10kV直转800V SiC SST效率98-99%已落地智算中心；直流控保市占>70%；SST国内市占率超30%。
- **Source**: 微博/研报
- **URL**: https://m.weibo.cn/detail/5310948577644193
- **Date**: 2026-06
- **Confidence**: 中高

### E8-2 金盘科技(688676)
- **Claim**: 干式变压器+SST双布局；2.4MW SiC SST批量交付海外IDC；NV白皮书国内SST供应商；配套字节、阿里海外算力集群。
- **Source**: 研报/头条
- **Date**: 2025-2026
- **Confidence**: 中高

### E8-3 SST核心材料
- **Claim**: 纳米晶合金是SST高频变压器磁芯最优选择（损耗仅为非晶的1/2-1/3），占原材料成本33-35%；云路股份2025年纳米晶收入3.5亿(占18.7%)；新特电气中频隔离变压器已交付200MW光伏项目。
- **Source**: 新浪财经研报
- **URL**: http://stock.finance.sina.com.cn/stock/go.php/vReport_Show/kind/lastest/rptid/837782604661/index.phtml
- **Date**: 2026-07-19
- **Confidence**: 高

---

## 9. 液冷协同

### E9-1 英维克(002837)
- **Claim**: 液冷龙头；在手液冷订单>85亿；冷板式市占>42%；国内唯一NV NPN Tier1认证液冷厂商；2026Q1液冷收入+250-290%；产品"无缝适配800V高压直流架构"。
- **Source**: 公司公告/研报
- **Date**: 2026Q1
- **Confidence**: 高

---

## 10. 其他配套

### E10-1 豪鹏科技 BBU
- **Claim**: 推出毫秒级响应(<5ms)BBU电池系统，已成为全球领先服务器厂商合格供应商并批量出货；越南基地投产；2026年2月起储能产品涨价5-10%。
- **Source**: 搜狐
- **URL**: https://m.sohu.com/a/1053980473_122066679/
- **Date**: 2026-07-23
- **Confidence**: 中
- **Caveat**: "全球领先服务器厂商"未点名，是否为NV生态链待确认

### E10-2 SSCB必要性
- **Claim**: 800V HVDC直流短路故障电流di/dt极高，传统毫秒级机械保护无效，必须SSCB微秒级切断；SiC SSCB响应1-10μs；ABB SACE Infinitus、LS电气1500V直流断路器为国际代表。
- **Source**: 电子发烧友/新浪财经
- **URL**: https://m.elecfans.com/article/7905982.html
- **Date**: 2026-05-08
- **Confidence**: 高

---

## 11. NVIDIA供应链官方口径（核心）
- 硅(10家): Infineon, MPS, Navitas, ROHM, ST, TI, ADI, Innoscience(英诺赛科), OnSemi, Renesas
- 电源系统组件(5家): Delta(台达), Flex Power(伟创力), Lead Wealth(立锜/力玮), LiteOn(光宝), Megmeet(麦格米特)
- 数据中心电力系统(3家): Eaton, Schneider(施耐德), Vertiv(维谛)
- Source: NVIDIA 2025-05-20官方博客
- Note: A股仅麦格米特在NV直接官宣名单中；其余均通过Tier1/ODM间接供货
