# HBF产业链深度研究 - 证据文件

## E1: HBF定义与标准规范
Claim: HBF（High Bandwidth Flash，高带宽闪存）是介于HBM与SSD之间的新型存储层级，由SK海力士与闪迪于2026年8月4日在FMS 2026峰会上联合发布全球首个标准规范，通过OCP发布为开放标准。
Source: SK海力士官网新闻稿
URL: https://news.skhynix.com/en/hbf-at-fms-2026/
Date: 2026-08-04
Excerpt: "SK hynix and Sandisk released the first open HBF standard via OCP to ease AI memory bottlenecks, with up to 512GB and 3TB/s bandwidth, UCIe support, and a 375-layer 4D NAND that is 2.5 times more power efficient. Capacity specifications cover up to 512GB based on two stack configurations (8-high and 16-high NAND dies). Bandwidth is categorized into three grades (Grade1~3), delivering scalable performance from approximately 0.4TB/s to 3.0TB/s."
Context: 官方新闻稿，定义HBF的核心规格与架构
Scope fit: IN-SCOPE
Confidence: HIGH

## E2: HBF技术参数细节
Claim: 首版HBF标准定义8层/16层两种NAND堆叠配置，最高512GB容量；带宽分Grade 1-3三档，0.4-3.0TB/s；采用UCIe互联接口连接GPU/CPU；含互联接口/电气特性/堆叠可靠性/封装指南/软件IO指南。
Source: 电子工程专辑转载SK海力士官方稿
URL: https://www.eet-china.com/news/202608044353.html
Date: 2026-08-04
Excerpt: "该规范定义了两种容量配置，分别采用8层和16层NAND芯片堆叠，最高支持512GB容量；并按三个等级（Grade 1~3）设定带宽标准，数据传输能力覆盖约0.4TB/s至3.0TB/s。HBF与处理器之间采用行业标准UCIe互联，该规范由OCP正式发布，成为行业通用开放标准。"
Context: 中文转载官方信息
Scope fit: IN-SCOPE
Confidence: HIGH

## E3: HBF生态联盟成员
Claim: HBF联盟目前已汇聚谷歌（Google DeepMind）与Tenstorrent参与技术验证与标准制定；SK海力士计划继续扩大生态体系。
Source: SK海力士官网 & 韩国Economy Tribune
URL: https://www.economytribune.co.kr/news/articleView.html?idxno=3903532
Date: 2026-08-04
Excerpt: "구글·텐스토렌트 생태계 참여…2030년 시장 120억달러 전망. 구글 딥마인드 연구진은 오는 6일 SK하이닉스·샌디스크와 함께 HBF를 활용한 '메모리 월' 극복 방안을 논의한다."
Context: 韩文权威经济媒体报道
Scope fit: IN-SCOPE
Confidence: HIGH

## E4: HBF市场规模预测
Claim: 韩国新荣证券（Shinyoung Securities）预测HBF市场从2027年约10亿美元增长至2030年约120亿美元；HBF之父金正浩教授预测2038年HBF需求可能超越HBM。
Source: 韩国Economy Tribune / 新浪BigNews
URL: https://www.economytribune.co.kr/news/articleView.html?idxno=3903532
Date: 2026-08-04
Excerpt: "신영증권은 HBF 시장이 2027년 약 10억달러(약 1조4500억원)에서 2030년 120억달러(약 17조4000억원) 규모로 성장할 것으로 전망했다."
Context: 韩国券商预测
Scope fit: IN-SCOPE
Confidence: MEDIUM (单一券商预测)

## E5: HBF量产路线图
Claim: 闪迪计划2026年下半年送出首批HBF样品，2027年初推出搭载HBF的AI推理装置样品，2027年启动商业化量产；SK海力士未明确HBF量产时间，但375层V10 4D NAND计划2027年初量产用于eSSD；日本为HBF试产线候选地。
Source: TrendForce
URL: https://www.trendforce.com/news/2026/08/04/sk-hynix-sandisk-debut-hbf-standard-to-challenge-ai-memory-bottlenecks-with-google-tenstorrent-support/
Date: 2026-08-04
Excerpt: "SanDisk aims to introduce HBF prototypes in the second half of this year, with Japan emerging as a leading candidate for the production site. A pilot production line is expected to be completed in the second half and begin operation around year-end, with commercialization targeted for 2027. SK hynix plans to initiate mass production of high-performance, high capacity eSSDs based on the 375-layer 4D NAND early next year."
Context: TrendForce产业新闻
Scope fit: IN-SCOPE
Confidence: HIGH

## E6: HBF技术原理——HBM+H3混合架构
Claim: HBF采用与HBM类似的3D堆叠架构和TSV硅通孔，将DRAM替换为3D NAND闪存；SK海力士提出H3（Hybrid HBM+HBF）混合架构，HBM负责热数据/计算，HBF负责冷数据/模型权重/KV Cache存储，与eSSD构成G1.5新层级。
Source: SK海力士官网 / 36氪
URL: https://36kr.com/p/3903123133466500
Date: 2026-07-20
Excerpt: "SK海力士内存系统研究高级副总裁Hoshik Kim指出：HBF通过将先进的3D封装和垂直堆叠技术应用于NAND闪存，能够提供远超标准NVMe存储的带宽。推理场景中，静态的数十亿参数模型权重或预计算的KV缓存等读密集型数据，可存放于HBF层级，HBM充当高速暂存区。"
Context: 36氪深度技术报道
Scope fit: IN-SCOPE
Confidence: HIGH

## E7: HBF vs HBM参数对比
Claim: HBF单栈容量512GB（8栈可达4TB），是HBM的8-16倍；初代读带宽约1.6TB/s，接近HBM3水平；单位成本仅为HBM的1/5-1/7；延迟约5μs（HBM约<100ns，差距约50倍）；写入耐久约10万次（HBM无限）。
Source: 新浪BigNews / CSDN
URL: https://news.sina.cn/bignews/insight/2026-07-09/detail-inihfazc5404412.d.html
Date: 2026-07-09
Excerpt: "单栈容量HBM 16-32GB vs HBF 512GB（8栈可达4TB，HBM的8-16倍）；带宽HBM 1.2-3.2TB/s vs HBF 初代约1.6TB/s；成本HBM极高 vs HBF单位成本仅HBM的1/7；延迟HBM<100ns vs HBF~5μs（HBM的50倍）；写入耐久HBM无限 vs HBF约10万次。"
Context: 多源交叉验证的参数对比
Scope fit: IN-SCOPE
Confidence: MEDIUM (部分数字为估算)

## E8: 英伟达未加入HBF联盟——核心风险
Claim: 英伟达未加入HBF联盟，其路线为BlueField-4 DPU+NVMe SSD的"CMX Context Memory Storage"方案，用闪存共享pod层级扩展KV Cache；HBF生态的核心不确定性在于英伟达是否采纳。
Source: 韩国Economy Tribune
URL: https://www.economytribune.co.kr/news/articleView.html?idxno=3903532
Date: 2026-08-04
Excerpt: "엔비디아는 HBF 컨소시엄에는 참여하지 않은 채 블루필드4 기반 'CMX 컨텍스트 메모리 스토리지'를 앞세우고 있다. GPU 내부 HBM에 장기간 보관하기 어려운 KV 캐시 등을 플래시 기반의 공유 포드 단위 계층으로 확장하는 구조다."
Context: 韩国权威媒体报道英伟达的差异化路线
Scope fit: IN-SCOPE
Confidence: HIGH

## E9: HBF核心催化事件时间线
Claim: HBF产业化时间线：2025年8月SK海力士+闪迪启动标准化合作→2026年2月成立联盟→2026年8月4日发布首个标准（OCP）→2026H2闪迪送样→2027年初HBF搭载AI推理装置样品+375层NAND量产→2027年小规模量产→2028年规模化（英伟达/谷歌/AMD可能采纳）。
Source: SK海力士官网 / TrendForce / 新浪BigNews
URL: https://news.skhynix.com/en/hbf-at-fms-2026/
Date: 2026-08-04
Excerpt: "This milestone comes about six months after launching the consortium in February this year, following the initial standardization partnership with Sandisk in August 2025."
Context: 官方时间线与行业预测综合
Scope fit: IN-SCOPE
Confidence: HIGH

## E10: 华海诚科——GMC封装材料核心标的
Claim: 华海诚科(688535)是国内唯一实现HBM专用GMC（颗粒状环氧塑封料）量产的企业，已通过SK海力士HBM4全工艺验证并批量供货，同步通过三星认证；GMC国产化率不足5%，长期被日本住友电木和Resonac垄断；2026Q1营收同比增长165.58%；8月4日股价87.42元（+7.05%）。
Source: 东方财富股吧 / 投研局座 / 雪球
URL: https://guba.eastmoney.com/news,gssz,1752110143.html
Date: 2026-07-30
Excerpt: "华海诚科是国内唯一实现HBM专用GMC量产的企业，也是国内唯一进入SK海力士GMC供应链的厂商。公司GMC产品已完整通过SK海力士HBM4全工艺验证，可适配12至16层高阶HBM堆叠方案，同步通过三星认证。2026年一季度，公司营收同比增长165.58%。"
Context: 多源验证
Scope fit: IN-SCOPE
Confidence: MEDIUM (股吧来源，交叉验证于其他源)

## E11: 雅克科技——HBM前驱体核心供应商
Claim: 雅克科技(002409)子公司UP Chemical是SK海力士HBM4/HBM5 ALD前驱体核心供应商，全球HBM前驱体市占率约18%，为SK海力士独家供应商（部分材料），已通过三星/美光认证；长期合同排到2031年；前驱体纯度7N级；机构一致预期2026E归母净利13.28亿(+32.8%)，2027E 16.66亿(+25.4%)；8月4日股价126.35元（+4.5%）。
Source: 雪球
URL: https://xueqiu.com/4408072670/402132509
Date: 2026-07-26
Excerpt: "雅克科技前驱体纯度达7N级（99.99999%）。据光大证券测算，公司全球HBM前驱体市占率约18%，是SK海力士前驱体的独家供应商，并已通过三星、美光认证。2026E归母净利13.28亿（+32.8%）、EPS 2.79元、对应PE约55倍；2027E 16.66亿（+25.4%）。综合目标价约102.78元（对应2027年约35倍PE）。"
Context: 雪球综合光大证券等机构观点
Scope fit: IN-SCOPE
Confidence: MEDIUM

## E12: 太极实业——SK海力士合资封测
Claim: 太极实业(600667)子公司海太半导体（太极持股55%，SK海力士45%）是SK海力士在中国大陆唯一DRAM/HBM专属封测基地，承接其70%以上HBM封测订单；双方签署《第四期后工序服务合同》2025.7.1-2030.6.30锁定5年，采用"全部成本+约定收益"模式；8月4日股价16.68元（+2.46%）。
Source: 投研局座
URL: http://m.toutiao.com/group/7668895285862548018/
Date: 2026-08-02
Excerpt: "太极实业与SK海力士合资成立海太半导体（太极持股55%，SK海力士45%）。这是SK海力士在中国大陆唯一的DRAM/HBM专属封测基地，承接其70%以上HBM封测订单。双方已签署《第四期后工序服务合同》，2025年7月1日至2030年6月30日，采用'全部成本+约定收益'模式。"
Context: 头条号综合公开信息
Scope fit: IN-SCOPE
Confidence: MEDIUM

## E13: 香农芯创——SK海力士HBM/HBF分销商
Claim: 香农芯创(300475)是SK海力士HBM产品在中国区授权代理商，取得SK海力士代理权及AMD经销商资质；阿里、腾讯、字节为主要客户；上半年净利预增超21倍；8月4日股价139.61元（+4.16%）。
Source: 博学吾股丰登
URL: http://m.toutiao.com/group/7666848004241900082/
Date: 2026-07-26
Excerpt: "香农芯创(300475)——HBM授权代理商。公司是SK海力士HBM产品在中国区的授权代理商。英伟达的AI芯片大量捆绑HBM出货，作为核心分销商营收弹性显著。上半年净利预增超21倍。"
Context: 头条号综合公开信息
Scope fit: IN-SCOPE
Confidence: MEDIUM

## E14: 澜起科技——内存接口/CXL/UCIe
Claim: 澜起科技(688008)是全球内存缓冲芯片龙头，市占率超50%，适配英伟达Vera Rubin平台HBM4，单GPU配套8颗缓冲芯片，三星/海力士/美光全部认证；HBF采用UCIe互联，澜起在互联接口芯片领域具备CXL/DDR5技术储备；8月4日股价198.74元（+4.63%）。
Source: 商途观万象
URL: http://m.toutiao.com/group/7666888548615832110/
Date: 2026-07-27
Excerpt: "澜起科技(688008): HBM内存缓冲芯片全球龙头，市占率超50%，适配英伟达Vera Rubin平台HBM4，单GPU配套8颗缓冲芯片，三星/海力士/美光全部认证。"
Context: 综合公开信息
Scope fit: IN-SCOPE
Confidence: MEDIUM

## E15: SK海力士Q2业绩与HBM4量产
Claim: SK海力士2026Q2营收79.3万亿韩元（同比+257%），营业利润60.5万亿韩元（同比+557%），营业利润率76%；HBM4已于Q2量产出货，下半年扩大生产；与十余家客户签订LTA长期供货协议（含保证金机制）；321层NAND占比提升至50%。
Source: SK海力士IR新闻稿
URL: https://news.skhynix.co.kr/q2-2026-business-results/
Date: 2026-07-29
Excerpt: "매출 79조 3,187억 원, 영업이익 60조 5,426억 원, 순이익 93조 9,226억 원. HBM4 2분기 양산 출하, 하반기 생산 본격 확대. 핵심 고객 포함 10여 곳과 장기공급계약(LTA) 진행."
Context: 官方财报
Scope fit: IN-SCOPE
Confidence: HIGH

## E16: 江波龙——存储模组+闪迪合作
Claim: 江波龙(301308)是全球第二大独立存储模组厂商，2026上半年业绩爆发（毛利率55.53%创历史新高，H1净利约92-110亿区间）；与闪迪签订合作，不赌晶圆涨跌赚加工费；企业级存储2025营收17.83亿(+93.3%)；8月4日股价331.80元（+3.75%）。
Source: 公开财报信息综合
URL: https://cj.sina.cn/articles/view/7879849562/1d5acf65a06801ubeg
Date: 2026-08-02
Excerpt: "江波龙上半年毛利率55.53%创历史新高。2025年企业级存储营收17.83亿元，同比增长93.3%。去年和存储原厂闪迪签了合作。"
Context: 财经头条分析
Scope fit: IN-SCOPE
Confidence: MEDIUM

## E17: 8月4日A股盘面——科技股超跌反弹+CPO/HBF催化
Claim: 2026年8月4日A股全线反弹，创业板指半日涨4.83%，半日成交1.36万亿；CPO/算力/半导体领涨，芯片板块主力净流入320亿；HBF标准发布叠加CPO交换机出货催化；半导体普涨，源杰科技+12%、澜起科技、佰维存储、通富微电、兆易创新跟涨；协创数据涨超15%。
Source: 每经午评 / 21财经
URL: https://www.163.com/dy/article/L3G2T17N0512B07B.html
Date: 2026-08-04 11:54
Excerpt: "8月4日早盘创业板指大涨4.83%，CPO概念震荡反弹，东山精密涨停；半导体普涨，源杰科技涨超12%，澜起科技、德明利、佰维存储、通富微电、兆易创新上涨超2%。"
Context: 实时盘面报道
Scope fit: IN-SCOPE
Confidence: HIGH

## E18: 目前无A股公司直接量产HBF芯片——伪概念风险提示
Claim: 目前国内尚无A股公司直接量产HBF芯片成品，A股公司主要沿存储芯片/颗粒→先进封装→封装材料→互联接口→设备载板等环节布局或潜在受益；HBF尚处标准推进/原型阶段（闪迪+SK海力士主导，预计2027年前后量产），相关公司多为技术同源或供应链配套，实际HBF订单落地仍需跟踪验证。
Source: 东方财富财富号
URL: https://caifuhao.eastmoney.com/news/20260627214625378584260
Date: 2026-06-27
Excerpt: "目前国内尚无A股公司直接量产HBF芯片成品，主要是沿存储芯片/颗粒→先进封装→封装材料→互联接口→设备载板等产业链环节布局或潜在受益。HBF尚处标准推进/原型阶段（闪迪+SK海力士主导，预计2027年前后量产），上述公司多为技术同源或供应链配套，实际HBF订单落地仍需跟踪验证进度，注意题材炒作风险。"
Context: 股友提示风险，与多源信息一致
Scope fit: IN-SCOPE
Confidence: HIGH

## E19: 兴福电子——SK海力士直接持股
Claim: 兴福电子(688545)2026Q1获SK海力士（无锡）新进前十大流通股东（持500万股），是SK海力士在A股罕见的直接持股案例；公司主营超高纯电子级磷酸、硫酸、清洗蚀刻液；8月4日股价65.18元（+6.0%）。
Source: 投研局座
URL: http://m.toutiao.com/group/7668895285862548018/
Date: 2026-08-02
Excerpt: "兴福电子(688545)——SK海力士直接战略入股。2026年一季报显示，SK海力士（无锡）投资有限公司新进成为兴福电子前十大流通股股东，持股500万股。公司主营超高纯电子级磷酸、硫酸、清洗蚀刻液，是SK海力士无锡厂区核心湿电子化学品供应商。"
Context: 头条号
Scope fit: IN-SCOPE
Confidence: MEDIUM

## E20: 半导体设备国产替代与HBF相关性
Claim: 北方华创(002371)在刻蚀/薄膜/清洗全面布局；拓荆科技(688072)是国内唯一量产级混合键合设备供应商；中微公司(688012)CCP深孔刻蚀适配375层NAND与HBM TSV；华海清科(688120)CMP抛光/晶圆减薄；赛腾股份(603283)收购日本OPTIMA供HBM检测设备；快克智能(603203)A股唯一量产HBM核心TCB热压键合设备。8月4日北方华创672.8元(+4.9%)、中微318元(+2.6%)、拓荆604.3元(+2.1%)、华海清科229.4元(+1.1%)、赛腾38.9元(+6.2%)、快克39.05元(+10%)。
Source: 博学吾股丰登 / 腾讯自选股行情
URL: http://m.toutiao.com/group/7666848004241900082/
Date: 2026-07-26
Excerpt: "北方华创国内半导体设备平台型龙头；中微公司CCP深孔刻蚀设备适配375层NAND与HBM TSV工艺；快克智能A股唯一量产HBM核心TCB热压键合设备；赛腾股份收购日本OPTIMA，为三星、SK海力士提供HBM检测设备。"
Context: 综合公开信息
Scope fit: IN-SCOPE
Confidence: MEDIUM

## E21: 存储涨价斜率收窄——周期风险
Claim: TrendForce数据显示2026年存储产品均价Q1环比涨90%+、Q2环比50%+、Q3预期环比涨幅已降至15%左右；OPPO、Vivo等下游开始拒涨；SK海力士Q2营收79万亿低于市场85万亿预期。
Source: 企管干货铺
URL: http://m.toutiao.com/group/7669714877061284415/
Date: 2026-08-03
Excerpt: "存储涨价斜率正从一季度90%、二季度50%一路滑向三季度预期的15%，OPPO、Vivo等下游已开始拒涨。Q2营收79.3万亿虽刷新纪录，低于85万亿的市场预期。"
Context: 基于SK海力士财报+TrendForce数据
Scope fit: IN-SCOPE
Confidence: MEDIUM

## E22: 封装材料/填料产业链
Claim: 联瑞新材(688300)球硅/Low-α球铝是GMC配套填料；飞凯材料(300398)临时键合材料/EMC验证导入；安集科技(688019)CMP抛光液进入SK海力士产线；壹石通(688733)球形氧化铝散热填料；江丰电子(300666)高纯溅射靶材进入三星/SK海力士；华特气体(688268)特种气体。8月4日联瑞109.86元(+9.6%)、飞凯31.87元(+6.3%)、安集225.73元(+4.1%)、壹石通26.04元(+5.2%)、江丰197.74元(+6.9%)、华特128.01元(+5.4%)。
Source: 博学吾股丰登 / 东方财富
URL: http://m.toutiao.com/group/7666848004241900082/
Date: 2026-07-26
Excerpt: "联瑞新材HBM封装材料GMC所用球硅和Low-α球铝的配套供应商；安集科技抛光液、抛光垫进入三星、SK海力士存储产线；江丰电子高纯溅射靶材批量进入三星、SK海力士；华特气体特种气体国产替代龙头进入三星、SK海力士。"
Context: 综合
Scope fit: IN-SCOPE
Confidence: MEDIUM

## E23: 先进封装封测企业
Claim: 长电科技(600584)XDFOI平台支持HBM/HBF封装，SK海力士/美光认证；通富微电(002156)AMD核心封测伙伴，HBM相关封装良率98%，募资44亿扩产；华天科技(002185)3D堆叠封装跟进；深科技(000021)沛顿科技高端存储封测，三星高端存储资质。
Source: 博学吾股丰登 / CSDN
URL: http://m.toutiao.com/group/7666848004241900082/
Date: 2026-07-26
Excerpt: "长电科技国内HBM封测绝对龙头，XDFOI高性能封装技术平台；通富微电AMD核心封测伙伴，募资44亿元投入存储芯片封测产能提升项目；深科技国内高端存储芯片封测龙头，拿到三星高端存储封测资质。"
Context: 综合
Scope fit: IN-SCOPE
Confidence: MEDIUM

## E24: 东芯股份——SLC NAND介质分支
Claim: 东芯股份(688110)是国内少数量产SLC NAND的Fabless设计企业（512Mb-32Gb全容量，1xnm制程已批量出货）；SLC NAND因低延迟/高擦写/高带宽特性被认为是HBF底层介质之一（但有争议，HBF标准明确用3D NAND，并非SLC）；8月4日股价100.41元(+3.4%)。
Source: 东方财富财富号
URL: https://caifuhao.eastmoney.com/news/1728076252
Date: 2026-06-17
Excerpt: "东芯是国内少数能量产标准化SLC NAND的Fabless设计企业。行业权威TrendForce、SK海力士、闪迪公开资料明确：只有SLC具备低延迟、高擦写、高带宽特性，才能堆叠做成AI推理专用HBF模组。公司从未在互动易公告研发、生产HBF成品。"
Context: 股吧，SLC说法存疑（HBF标准基于3D NAND而非SLC）
Scope fit: PARTIAL (SLC论与HBF官方3D NAND路线有出入，需谨慎)
Confidence: LOW

## E25: 佰维存储/协创数据等模组
Claim: 佰维存储(688525)存储主控+先进封测一体化，华为AI终端核心存储供应商；协创数据(300857)存储模组，8月4日涨超15%（236.03元）；兆易创新(603986)NOR/NAND/DRAM全平台，受益存储周期反转；8月4日佰维214元(+3.5%)、兆易350元(+2.8%)。
Source: 盘面综合
URL: https://www.163.com/dy/article/L3G2T17N0512B07B.html
Date: 2026-08-04
Excerpt: "半导体普涨，澜起科技、德明利、佰维存储、通富微电、兆易创新上涨超2%；协创数据涨超10%。"
Context: 实时行情
Scope fit: IN-SCOPE
Confidence: MEDIUM
