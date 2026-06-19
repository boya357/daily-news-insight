# 行业/赛道趋势调研｜查询分解框架

本框架专用于"行业/赛道趋势调研"垂直场景，作为 SKILL.md 阶段 1（查询分解）与阶段 2（结构化检索循环）的对照表。

> **年份占位符约定**：本文件中的 `{CURRENT_YEAR}` / `{LAST_YEAR}` / `{NEXT_YEAR}` / `{NEXT_2_YEARS}` 由 SKILL.md 阶段 0 的 `date +%Y` 解算填入，自动随执行年份滚动；用户在 query 中显式指定基准年时以用户指定为准。

## 目录

- [1. 强制四问](#1-强制四问)
- [2. 行业研究九大维度](#2-行业研究九大维度)
- [3. 行业类型 → 重点维度映射](#3-行业类型--重点维度映射)
- [4. 检索关键词字典（中英双语）](#4-检索关键词字典中英双语)
- [5. 时效性与权威源排序规则](#5-时效性与权威源排序规则)
- [6. 验证规则](#6-验证规则)

---

## 1. 强制四问

开始检索前必须显式回答以下 4 个问题，作为后续维度覆盖检查的基线：

| # | 问题 | 输出要求 |
|---|------|---------|
| 1 | **行业核心定义** | 1-2 句话锁定边界，必须显式说明"包含什么 / 排除什么" |
| 2 | **决策意图** | 投资 / 入局创业 / 战略调整 / 产品定位 / 学习理解（影响第五板块的写作权重） |
| 3 | **行业类型** | 硬科技 / 消费医疗 / 软件 SaaS / 平台互联网 / 制造业 / 新能源 / 文娱 / 金融服务（决定维度权重，参见第 3 节） |
| 4 | **维度清单** | 基于第 2 节九大维度，勾选本次必须覆盖的子维度 |

---

## 2. 行业研究九大维度

任何一份合格的行业趋势报告必须覆盖以下九个维度。每个维度下列出对应的检索子问题，每个子问题必须能直接形成 1-2 条 `search_web` 查询。

### 维度 1：行业定义与边界

- 行业的官方/学术定义是什么？是否存在多种口径？
- 与相邻行业（替代品、互补品）的边界在哪里？
- 行业生命周期阶段（导入期 / 成长期 / 成熟期 / 衰退期）？

### 维度 2：市场规模与 CAGR

- 全球 TAM / SAM / SOM `{CURRENT_YEAR}` 数据（必须 ≥2 个独立来源交叉）
- 中国市场规模与全球占比
- `{LAST_YEAR}` 至 `{CURRENT_YEAR+5}` CAGR 区间预测（不同机构口径必须并列展示，矛盾不抑制）
- 市场规模测算方法（自上而下 / 自下而上 / 类比法）

### 维度 3：产业链结构

- 上游 / 中游 / 下游划分及核心环节
- **每一层的毛利率/净利率**（核心：利润分配在哪一层最厚）
- 各层核心供应商集中度（CR3、CR5）
- 关键卡脖子环节及国产替代进度

### 维度 4：核心玩家格局

- 头部 5-10 家公司：业务定位、市占率、最近一轮估值/市值、毛利率
- 融资活跃度（`{LAST_YEAR}`-`{CURRENT_YEAR}` A/B/C 轮代表案例与估值倍数）
- 上市/拟上市公司的二级市场表现（PE / PS / EV/EBITDA）
- 新进入者（AI 原生公司、跨界巨头）

### 维度 5：核心驱动力

- 技术驱动（关键技术拐点、SOTA 突破）
- 政策驱动（国家级规划、地方补贴、税收优惠）
- 需求驱动（C 端消费趋势、B 端数字化转型）
- 资本驱动（一二级市场资金流向）
- 供给侧驱动（成本下降曲线、规模化拐点）

### 维度 6：发展痛点与卡脖子

- 技术瓶颈（精度、能耗、稳定性、规模化）
- 商业化瓶颈（PMF 难找、单价高、教育成本高）
- 供应链瓶颈（关键原材料、设备、IP）
- 合规与伦理瓶颈

### 维度 7：政策与合规风险

- 中国监管动态（部委文件、地方试点、行业自律）
- 海外监管（美国出口管制、欧盟法案、东南亚/中东市场准入）
- 反垄断、数据合规、伦理审查
- 历史处罚案例与失败教训

### 维度 8：趋势预测与领先指标

- `{CURRENT_YEAR}`-`{NEXT_YEAR}` 关键事件日历（政策落地、产品发布、行业大会）
- 红利爆发的触发条件（成本下降至 X 元/单位、用户渗透率突破 Y%）
- 反转信号（什么发生即说明判断错误）
- 反方观点（强制至少 2 个反方论点）

### 维度 9：商业化路径与避坑

- 主流商业模式与单位经济（CAC / LTV / 毛利率 / 回本周期）
- 不同决策者的差异化路径（VC / CVC / 创业者 / 大厂战投）
- 失败案例库（已倒闭/退出公司及核心原因）
- 进入壁垒与可防御性（技术、品牌、规模、生态）

---

## 3. 行业类型 → 重点维度映射

不同行业类型下，九大维度的权重不同。下表给出推荐权重（H=高 / M=中 / L=低），用于指导检索深度分配。

| 维度 | 硬科技 | 消费医疗 | 软件 SaaS | 平台互联网 | 制造业 | 新能源 | 文娱 | 金融服务 |
|------|--------|----------|-----------|------------|--------|--------|------|----------|
| 1 定义 | M | M | M | M | M | M | M | M |
| 2 规模 | H | H | H | H | H | H | M | H |
| 3 产业链 | **H** | **H** | M | M | **H** | **H** | M | M |
| 4 玩家 | H | H | H | H | H | H | H | H |
| 5 驱动力 | H | M | M | H | M | **H** | H | M |
| 6 痛点 | **H** | H | M | M | H | H | M | M |
| 7 政策 | H | **H** | L | **H** | M | **H** | M | **H** |
| 8 趋势 | H | H | H | H | M | H | H | M |
| 9 落地 | H | H | H | M | M | H | H | H |

**用法**：判定行业类型后，对该列标记为 H 的维度必须有充分证据（≥3 条 HIGH 证据），M 维度 ≥2 条，L 维度 ≥1 条。

---

## 4. 检索关键词字典（中英双语）

### 4.1 时效性强制前缀

每个核心 query 必须叠加以下前缀之一（`{CURRENT_YEAR}` / `{LAST_YEAR}` 用阶段 0 解算的实际年份替换）：

- 中文：`{CURRENT_YEAR}`、`{LAST_YEAR}年最新`、`{CURRENT_YEAR} H1`、`最近6个月`
- 英文：`{CURRENT_YEAR}`、`latest {CURRENT_YEAR}`、`Q1 {CURRENT_YEAR}`、`H2 {LAST_YEAR}`

### 4.2 关键词模板表

| 维度 | 中文关键词 | 英文关键词 |
|------|-----------|------------|
| 行业定义 | `{行业} 定义 范围` `{行业} 行业分类` | `{industry} definition scope` |
| 市场规模 | `{行业} 市场规模 {CURRENT_YEAR}` `{行业} CAGR 增速` `{行业} {CURRENT_YEAR} 行业白皮书 PDF` | `{industry} market size {CURRENT_YEAR}` `{industry} CAGR forecast` `{industry} white paper {CURRENT_YEAR} PDF` |
| 产业链 | `{行业} 产业链图谱` `{行业} 上下游` `{行业} 价值链` | `{industry} value chain` `{industry} supply chain map` |
| 利润分配 | `{行业} 毛利率 利润率` `{行业} 各环节 利润分布` | `{industry} margin breakdown` `{industry} profit pool` |
| 核心玩家 | `{行业} 头部公司 市占率 {CURRENT_YEAR}` `{行业} TOP10 排名` | `{industry} top players market share` `{industry} competitive landscape` |
| 估值 | `{行业} 估值 PE PS {CURRENT_YEAR}` `{行业} 融资 估值倍数` | `{industry} valuation multiples {CURRENT_YEAR}` `{industry} EV/EBITDA` |
| 驱动力 | `{行业} 增长驱动 技术拐点` | `{industry} growth drivers` `{industry} catalysts` |
| 痛点 | `{行业} 卡脖子 技术瓶颈` `{行业} 国产替代` | `{industry} bottleneck` `{industry} pain points` |
| 政策 | `{行业} 政策 监管 合规 {CURRENT_YEAR}` `{行业} 部委文件` | `{industry} regulation policy {CURRENT_YEAR}` `{industry} compliance risk` |
| 趋势 | `{行业} {NEXT_YEAR} 预测 趋势` `{行业} 红利` | `{industry} {NEXT_YEAR} forecast trends` `{industry} emerging opportunities` |
| 反方 | `{行业} 泡沫 质疑 风险` `{行业} 唱空` | `{industry} bubble skeptic` `{industry} risks downside` |
| 失败 | `{行业} 倒闭 失败案例 退出 {LAST_YEAR}` | `{industry} failed startups shutdown` |
| 商业模式 | `{行业} 商业模式 变现` `{行业} 单位经济 LTV CAC` | `{industry} business model unit economics` |

### 4.3 权威源限定符

强制叠加站点限定（site:）以提升来源权威性：

- 中文：`site:gov.cn`、`site:miit.gov.cn`、`site:ndrc.gov.cn`、`site:cnki.net`、`site:36kr.com`、`site:iresearch.com.cn`、`site:leadleo.com`、`site:zhiyanzixun.com`
- 英文：`site:gartner.com`、`site:idc.com`、`site:mckinsey.com`、`site:bcg.com`、`site:bain.com`、`site:cbinsights.com`、`site:pitchbook.com`、`site:sec.gov`

---

## 5. 时效性与权威源排序规则

### 5.1 时效性优先级

| 数据类型 | 强制时效窗口 |
|---------|-------------|
| 市场规模 / CAGR | `{LAST_YEAR}` H2 - `{CURRENT_YEAR}` |
| 公司财务（季度数据） | 最近 2 个季度 |
| 公司估值 / 融资 | 最近 12 个月 |
| 政策文件 | 最近 24 个月 |
| 技术 SOTA | 最近 6 个月 |
| 趋势预测 | 仅采用 `{CURRENT_YEAR}` 发布的对 `{CURRENT_YEAR}` 之后的预测 |

任何超出窗口的数据必须 `[OUT-OF-WINDOW]` 标注或降级为 `[HISTORICAL-CONTEXT]`。

### 5.2 权威源排序

同一事实多源时按以下优先级引用：

1. **一级**：政府/监管文件、上市公司年报/招股书（SEC/港交所/Wind）、行业协会白皮书、学术期刊
2. **二级**：Gartner、IDC、McKinsey、BCG、Bain、艾瑞、亿欧、灼识咨询、头豹研究院
3. **三级**：CB Insights、PitchBook、a16z、Bloomberg、FT、36氪、虎嗅
4. **四级（仅作辅助）**：知乎、公众号、个人博客（必须降级为 LOW）

**严禁**：内容农场、AI 生成站、SEO 聚合站、来源不明的"大数据 XX 报告网"。

---

## 6. 验证规则

阶段 1 输出完成后，按以下 checklist 自检（任一项不通过则补做）：

- [ ] 是否已通过 `date +%Y` 解算并显式声明 `{CURRENT_YEAR}` 等基准年变量？
- [ ] 行业核心定义是否说清"包含 / 排除"边界？
- [ ] 决策意图是否落到具体动作（不能是"了解一下"）？
- [ ] 行业类型是否在 8 类中选定？
- [ ] 维度清单是否覆盖该类型所有 H 标记维度？
- [ ] 每个维度是否能展开为 ≥2 个具体可检索的子问题？
- [ ] 是否已识别需要加载的专业数据 Skill（参见 SKILL.md 阶段 0 第 5 步）？
