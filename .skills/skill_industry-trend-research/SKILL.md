---
name: industry-trend-research
description: 当用户需要行业/赛道调研、市场现状、竞争格局、市场份额、区域市场分析、投资调研或商业化落地决策时使用，交付麦肯锡白皮书风格五板块深度报告，自动锚定当年最新市场动态；keywords: industry research, competitive landscape, market analysis
dependency:
  python:
    - httpx>=0.27
    - plotly>=5.18
    - kaleido>=0.2.1
    - matplotlib>=3.7
---

# 行业/赛道趋势调研 (Industry Trend Research Pro)

垂直行业/赛道趋势调研 Skill，输出**麦肯锡白皮书风格**的五大板块决策级报告。本 Skill 专为高客单价付费场景设计，**自动以执行时的当年作为时效基准**（不依赖任何硬编码年份），要求每个数据点可溯源、每个判断有论据、每条建议可落地。

## 任务目标

- **本 Skill 用于**：针对用户给出的行业/赛道（如"具身智能"、"减肥药 GLP-1"、"AI 编程助手"），交付可直接用于战略规划、投资决策、商业化落地的深度趋势报告。
- **能力包含**：
  1. 行业定义与边界划定 + 当年大局观（TAM / CAGR）
  2. 产业链全景图谱 + 核心玩家利润格局
  3. 核心驱动力与卡脖子痛点的因果链分析
  4. 未来 1-2 年趋势预测与红利爆发点
  5. 商业化落地路径与避坑指南
- **触发条件（高召回口径，路由到此 Skill 后用此清单做最终自检）**：
  - **中文触发词**：行业研究 / 赛道分析 / 行业现状 / 行业趋势 / 市场规模 / 市场调研 / 市场份额 / 品牌份额 / 占有率 / 竞争格局 / 竞争态势 / 产业链研究 / 产业链分析 / 投资调研 / 投资机会 / 商业化落地 / 商业模式分析 / 入局分析 / 区域市场（如"东南亚某行业"、"中东某市场"、"美国某赛道"）/ 政策影响 / 红利赛道 / 风口分析。
  - **English triggers**: industry research, sector analysis, market analysis, market sizing, competitive landscape, market share, industry trends, regional market research, vertical deep dive, investment thesis, go-to-market analysis, value chain analysis, regulatory impact, growth opportunity scan.
  - **不适用于**：单点事实查询（"X 公司 CEO 是谁"）、单家公司尽调（用 `tianyancha-data` 等专项 Skill）、单一财报解读、纯学术综述、非商业领域（如纯文化/艺术评论）。

## 前置准备

- **依赖说明**：脚本依赖 `httpx>=0.27`（用于 URL 健康检查），可通过 `pip install -r scripts/requirements.txt` 安装。
- **路径约定**：报告与素材产出在当前工作目录（`./`），不写入 Skill 内部目录。
- **输出文件命名**：`{topic}` 为行业/赛道核心短语 + 基准年（如 `具身智能赛道_{CURRENT_YEAR}`、`GLP1减肥药行业_{CURRENT_YEAR}`），中文 query → 中文 topic，文件名空格用下划线，禁止 `/\:*?"<>|` 等特殊字符。`{CURRENT_YEAR}` 在阶段 0 解算后替换为实际年份。
  - 证据底稿：`{topic}_evidence.md`
  - 最终报告：`{topic}_report.md`
  - 图表目录：`{topic}_assets/`

## 操作步骤

### 阶段 0｜认知重置（Epistemic Reset）

1. **强制时间解算（Time Resolution）**：通过 `date +%Y` 获取当前年份，定义以下三个变量并在后续所有提示、检索、写作中替换使用：
   - `{CURRENT_YEAR}` = 执行时的当年（如 2026 / 2027 / 2028）
   - `{LAST_YEAR}` = `{CURRENT_YEAR} - 1`
   - `{NEXT_YEAR}` = `{CURRENT_YEAR} + 1`
   - `{NEXT_2_YEARS}` = `{CURRENT_YEAR} + 2`
   - **若用户在 query 中明确指定其他基准年（如"2025 年的 X 行业"、"我想看 2030 年预测"），则以用户指定为准并显式声明本次基准年**。
2. **时效基准规则**：任何早于 `{LAST_YEAR}` 的市场数据需标注 `[OUT-OF-WINDOW]` 并仅作历史参照；所有结论必须由 `{LAST_YEAR}` H2 至 `{CURRENT_YEAR}` 的检索证据支撑；趋势预测窗口为 `{CURRENT_YEAR}` - `{NEXT_2_YEARS}`。
3. 假设内部知识已过时，必须以检索到的最新公开证据替换内部记忆。
4. 检索语言与用户查询语言一致；中文查询优先在中文权威源（艾瑞、亿欧、36氪研究院、IT桔子、智研咨询、灼识咨询、头豹、信通院、工信部、各行业协会白皮书）与英文权威源（Gartner、IDC、McKinsey、BCG、Bain、CB Insights、PitchBook、a16z、统计局/SEC 文件）之间双轨检索。
5. **领域 Skill 预检（强制）**：本 Skill 提供调研工作流，不提供数据源。开始检索前必须按以下规则加载专业数据 Skill：
   - 宏观经济 / GDP / CPI / 利率 → 加载 `openecon-data`、`fred-data-skill`
   - 汇率 / 外汇 → 加载 `frankfurter-data`
   - A股 / 港股 / 美股行情 → 加载 `stock-data-skill`
   - 企业工商 / 股权 / 诉讼 / 尽调 → 加载 `tianyancha-data`
   - 影视 / 演员 → 加载 `tmdb-data-skill`
   - 移动 App / 应用市场 / ASO → 加载 `qimai-data-skill`
   - 法律 / 法规 / 合规 → 加载 `weko-data`
   - **专业源优先于 `search_web`**；存在多领域命中时全部加载，并显式列出"已加载 Skill ↔ 覆盖维度"映射表。

### 阶段 1｜行业定义与查询分解

参考 [references/industry_research_framework.md](references/industry_research_framework.md) 完成以下输出（必须在检索前显式打印）：

1. **行业核心定义**：用 1-2 句话锁定行业边界（包含什么 / 排除什么），避免大而无当。
2. **决策意图**：用户拿这份报告要做什么决策？（投资、入局、战略调整、产品定位）
3. **价值链分层假设**：上游 / 中游 / 下游初步划分（后续在第 2 板块校验）。
4. **维度清单**：基于 framework 中的"九大行业研究维度"勾选并展开本次需要覆盖的维度。

### 阶段 2｜结构化检索循环（≥18 轮）

针对行业趋势研究的特殊性，**最少执行 18 轮检索**（高于通用研究的 15 轮），分三段递进，禁止关键词重复：

> **占位符替换规则**：以下所有 query 模板中的 `{CURRENT_YEAR}` / `{LAST_YEAR}` / `{NEXT_YEAR}` / `{NEXT_2_YEARS}` 必须替换为阶段 0 解算的实际年份后再发起检索。例如执行年是 2027 → `{CURRENT_YEAR}=2027`、`{LAST_YEAR}=2026`、`{NEXT_YEAR}=2028`、`{NEXT_2_YEARS}=2029`。

#### 第一段：宏观锚定（4-5 轮，并行）
必须命中以下关键词组合，**强制带 `{CURRENT_YEAR}` 年份限定**：
- `"{行业} {CURRENT_YEAR} 行业白皮书 PDF"` / `"{industry} {CURRENT_YEAR} white paper"`
- `"{行业} 市场规模 CAGR {LAST_YEAR}-{CURRENT_YEAR+5}"` / `"{industry} market size CAGR"`
- `"{行业} TAM SAM SOM {CURRENT_YEAR}"`
- `"{行业} 全球 vs 中国 市场份额 {CURRENT_YEAR}"`
- `"{行业} {CURRENT_YEAR} 政策"` / `"{行业} 监管 合规"`

#### 第二段：产业链解剖（6-7 轮，并行）
- `"{行业} 产业链图谱 上下游"`
- `"{行业} 上游 核心供应商 议价能力"`
- `"{行业} 中游 利润率 毛利"` ←**重点：利润分配**
- `"{行业} 下游 客户结构 集中度"`
- `"{行业} 头部公司 市占率 TOP10 {CURRENT_YEAR}"`
- `"{行业} 融资 A轮 B轮 估值 {LAST_YEAR} {CURRENT_YEAR}"`
- `"{行业} 卡脖子 技术壁垒 国产替代"`

#### 第三段：趋势预测与避坑（6-7 轮）
- `"{行业} {NEXT_YEAR} 趋势预测 红利"`
- `"{行业} 颠覆性技术 新进入者"`
- `"{行业} 失败案例 倒闭 退出 {LAST_YEAR}"` ←**重点：避坑**
- `"{行业} 政策风险 合规 处罚 {CURRENT_YEAR}"`
- `"{行业} 商业模式 变现路径"`
- `"{行业} 反向观点 contrarian"`（强制检索反方观点）
- 时效性兜底：`"{行业} {CURRENT_YEAR} Q1/Q2/Q3/Q4 最新动态"`（按当前实际季度选择）

**并行检索原则**：相互独立的检索请求必须并行发起，每次 `search_web` 调用塞满允许的最大 query 数量。

### 阶段 3｜证据增量收集（每轮检索后立即追加）

每条关键证据使用统一 7 字段结构化证据块格式追加写入 `{topic}_evidence.md`：

```
Claim: [具体事实陈述，不含 URL]
Source: [来源名称]
URL: [来源 URL，禁止首页 URL，必须深链]
Date: [发布日期 YYYY-MM；无则 N/A]
Excerpt: [原文逐字摘录，禁止改写]
Context: [影响解读的上下文]
Confidence: [HIGH / MEDIUM / LOW]
```

**置信度规则**：
- `[HIGH]`：≥2 个独立权威源交叉确认。
- `[MEDIUM]`：1 个权威源，或多个二手源。
- `[LOW]`：单一未验证陈述、博客级证据。

**强制规则**：
- 每个核心数字（市场规模、CAGR、市占率、利润率、估值倍数、融资金额）**必须**附带具体来源 URL（深链，非首页）和数据日期；无来源的数字宁可不写。
- 矛盾不抑制，必须显式记录 `[TEMPORAL-CONFLICT]` 或 `[INTERPRETIVE-CONFLICT]`。
- 来源标签：`[SEARCH-SOURCED]` / `[FILE-SOURCED]` / `[MIXED]`。

### 阶段 4｜证据合并与 URL 校验

完成检索后：

1. 对 `{topic}_evidence.md` 进行去重、置信度升降级、删除无关条目。
2. **批量校验所有 URL 可达性**：
   ```bash
   pip install -r scripts/requirements.txt
   python scripts/verify_urls.py {topic}_evidence.md
   ```
   仅 ❌ FAIL 需要处理：在该证据块的 Confidence 字段追加 `[URL-UNVERIFIED]`（如 `Confidence: MEDIUM [URL-UNVERIFIED]`），不删除条目。✅ PASS 与 ⚠️ UNCERTAIN 均视为可达。
3. 检查每个研究维度证据是否充分；若关键维度（如"利润分配"、"政策风险"）证据稀薄，回到阶段 2 做补充检索。

### 阶段 5｜五大板块报告写作（核心交付）

参考 [references/report_template.md](references/report_template.md) 中的麦肯锡白皮书模板，**严格按以下五大板块**生成 `{topic}_report.md`：

| # | 板块 | 核心问题 |
|---|------|----------|
| 一 | 行业定义与 `{CURRENT_YEAR}` 市场大局观 | 这是什么生意？盘子多大？长得多快？ |
| 二 | 产业链图谱与核心玩家格局 | 谁在赚大钱？利润分布在产业链哪一层？ |
| 三 | 核心驱动力与行业发展痛点 | 为什么火？卡脖子在哪？ |
| 四 | `{CURRENT_YEAR}`-`{NEXT_YEAR}` 趋势预测与红利爆发点 | 未来 1-2 年的风口在哪？哪些信号要关注？ |
| 五 | 商业化落地建议与避坑指南 | 怎么赚到钱？哪些坑必须避开？ |

> 板块标题中的 `{CURRENT_YEAR}` / `{NEXT_YEAR}` 在最终报告中必须替换为阶段 0 解算出的实际数值（例如执行年解算为 2026 时，所有 `{CURRENT_YEAR}` 替换为 `2026`、`{NEXT_YEAR}` 替换为 `2027`）。具体的板块二级标题文字由 `assemble_report.py init` 阶段一次性注入，写作时无需自行书写。

**写作硬性要求**：

- **执行摘要（Executive Summary）**：300-500 字，开篇即给结论与关键数字，不写"本报告将探讨..."的废话。
- **总字数**：≥6,000 字（行业研究垂直场景，高于通用研究 5,000 字下限）。
- **段落规则**：每段 ≥100 字 / ≤1,000 字；每个二级小节至少 2 段。
- **可视化强制（视觉规范见 [references/visual_style_guide.md](references/visual_style_guide.md)）**：每个板块**至少包含 1 个非纯文本元素**（表格 / Mermaid / 图表 / LaTeX 公式）。所有 Mermaid 代码块**强制注入麦肯锡蓝灰风主题 init 头**与 classDef 节点分色，否则 `validate` 报警。
  - 第一板块：**市场规模与 CAGR 数据表** + **行业边界对照表**（"包含 / 排除"两列结构，废止 Mermaid 边界图——见 visual_style_guide §6.1）。
  - 第二板块：**主题化产业链图谱 Mermaid** + **核心玩家对比表**（含市占率、毛利率、估值倍数列）+ **Plotly 桑基图**（产业链利润分配，链宽 = 毛利率 × 营收占比；废止饼图——见 visual_style_guide §4）。
  - 第三板块：**驱动力 vs 痛点矩阵表** + **主题化因果链 Mermaid**（政策 primary / 受损 danger / 受益 positive）。
  - 第四板块：**`{CURRENT_YEAR}`-`{NEXT_YEAR}` 趋势预测表**（含触发条件、领先指标、反转信号列）。
  - 第五板块：**主题化决策树 Mermaid** + **避坑清单表**。
- **引用格式**：每条事实陈述后紧贴句末标点前使用 `[(来源)](深链URL)`，多源用空格分隔。禁止首页 URL，禁止编号引用。
- **图表生成**：所有图表（Plotly / matplotlib）保存到 `{topic}_assets/`，文件名描述性（如 `产业链利润桑基图_{CURRENT_YEAR}.png`），通过 `file_to_url` 转公网 URL 后以 `![标题](url)` 嵌入。**统一使用 visual_style_guide §1 的麦肯锡蓝灰配色**与 §5 的 `MCK_PALETTE`；中文图表必须配置 CJK 字体并设置 `axes.unicode_minus = False`。Plotly 输出 PNG 需 kaleido，若环境缺失则回退到 HTML 或 matplotlib 横向堆叠条形图（禁止退回饼图）。
- **每个图表前后必须有文字**：前置铺垫上下文，后置点出关键观察。
- **置信度披露**：LOW 置信度的判断必须用对冲语言（"初步信号显示..."、"未经核实的报道指出..."），禁止与 HIGH 同等口吻陈述。
- **行文调性**：禁用"颠覆"、"重塑未来"、"行业领先"等营销话术；保持麦肯锡式克制、专业、数据先行。

### 阶段 6｜分块安全拼接（避免长文本截断）

行业报告通常 6,000-12,000 字，单次模型输出极易触发截断或丢格式。**强制按板块分次写作并使用 `assemble_report.py` 拼接**：

```bash
# 步骤 1：先创建空报告骨架（标题与板块编号自动用阶段 0 的当年年份生成；
# 默认读取系统当年，也可显式 --current-year 覆盖，例如复盘历史年份时使用）
python scripts/assemble_report.py init --topic "{topic}" --title "{报告标题}"
# 或：python scripts/assemble_report.py init --topic "{topic}" --title "{报告标题}" --current-year {CURRENT_YEAR}

# 步骤 2：按板块逐次追加（每次只写 1 个板块，避免单轮输出过长）
python scripts/assemble_report.py append --topic "{topic}" --section-key exec_summary --content-file _section_tmp.md
python scripts/assemble_report.py append --topic "{topic}" --section-key part1 --content-file _section_tmp.md
python scripts/assemble_report.py append --topic "{topic}" --section-key part2 --content-file _section_tmp.md
python scripts/assemble_report.py append --topic "{topic}" --section-key part3 --content-file _section_tmp.md
python scripts/assemble_report.py append --topic "{topic}" --section-key part4 --content-file _section_tmp.md
python scripts/assemble_report.py append --topic "{topic}" --section-key part5 --content-file _section_tmp.md

# 步骤 3：完整性校验（字数、必备小节、可视化元素计数）
python scripts/assemble_report.py validate --topic "{topic}"
```

每次写作一个板块时：
1. 将该板块完整 Markdown 内容写入临时文件 `_section_tmp.md`（用 `write_file` 工具）。
2. 调用 `assemble_report.py append` 将该板块原样追加到最终报告。
3. 拼接完成后运行 `validate` 自检；若校验失败按提示补写。

**【标题注入铁律 / SINGLE-SOURCE-OF-TRUTH】**

报告的所有 `# 一级标题` 与 `## 二级板块标题`（执行摘要 / 一二三四五板块 / 结语，共 7 个）在 `init` 阶段已由脚本一次性注入。**权威定义见 `scripts/assemble_report.py` 的 `section_headings()` 函数**——任何标题文字调整只动该函数一处，其余文档与正文自动跟随。

写作 `_section_tmp.md` 时**必须**遵守：
- ❌ **禁止**写入任何 `# ` 一级标题或 `## ` 二级标题
- ✅ **只写** `### 1.1`、`### 5.4`、`#### ` 等三级及以下小节标题与正文
- 违反将被 `assemble_report.py append` 命令拒绝（exit code=1，返回 `H2_HEADING_FORBIDDEN`），需删除后重试

这条铁律根除二级标题在最终报告中重复出现的问题——所有二级标题只允许 `init` 阶段写一次。

## 使用示例

> 以下示例中的年份均为说明性，实际值由阶段 0 的时间解算自动决定（执行年=2026 时为 2026/2027；执行年=2027 时为 2027/2028，依此类推）。

### 示例 1：具身智能（中文 query，垂直硬科技）

- **场景/输入**：用户："帮我深度调研一下具身智能赛道，我要决定要不要投这个方向。"（假设执行年 = `{CURRENT_YEAR}`）
- **预期产出**：
  - `具身智能赛道_{CURRENT_YEAR}_evidence.md`：≥40 条结构化证据，覆盖大模型本体公司（Figure、1X、银河通用、宇树）、上游传感器与减速器、下游应用场景。
  - `具身智能赛道_{CURRENT_YEAR}_report.md`：6,000+ 字五板块报告，含 `{CURRENT_YEAR}` 市场规模 CAGR 表、上中下游利润桑基图（Plotly Sankey，链宽=毛利率×营收占比）、Figure/1X/特斯拉 Optimus 估值对比表、`{CURRENT_YEAR}`-`{NEXT_YEAR}` 量产节奏预测表、避坑清单（数据稀缺、Sim2Real 鸿沟、单价过高的商业化困境）。
  - `具身智能赛道_{CURRENT_YEAR}_assets/`：≥5 张图表。
- **关键要点**：
  - 上游必须细化到伺服电机、谐波减速器、力矩传感器等卡脖子环节及对应公司毛利率。
  - 必须包含反方观点（如 LeCun 对 LLM 路径的质疑）。
  - 决策建议要分场景（VC 早期投资 / CVC 战略投资 / 创业入局）给出差异化路径。

### 示例 2：GLP-1 减肥药（消费医疗，全球视角）

- **场景/输入**：用户："分析一下 GLP-1 减肥药这个赛道最新的趋势和投资机会。"
- **预期产出**：
  - 强调全球（诺和诺德、礼来）vs 国产（信达、华东医药、恒瑞）双轨对比。
  - 第二板块利润格局必须包含 API 原料药 → 制剂 → 渠道（药店/医院/电商）的逐层利润率。
  - 第三板块痛点要覆盖：医保支付、停药反弹、长期安全性、专利悬崖（按执行年实际状态描述，如司美格鲁肽中国专利到期窗口）。
  - 第四板块红利点：口服 GLP-1、双靶点（GLP-1/GIP）、第三代长效制剂。
- **关键要点**：与示例 1 不同，本场景**政策与合规风险权重极高**，第三、五板块需放大处理，并强制加载 `weko-data`（医药法规）。

### 示例 3：AI 编程助手（toC/toB 双重市场）

- **场景/输入**：用户："AI 编程赛道现在的格局如何？我们公司想做企业级 AI Coding 产品。"
- **预期产出**：默认决策意图为"toB 入局"，第五板块商业化建议突出企业级与 toC 工具的差异化路径。第二板块产业链图谱需重构为"模型层 → 工具层（Cursor/Copilot/Windsurf/Cline）→ 渠道层（IDE 插件/CLI/Cloud IDE）"。
- **关键要点**：与示例 1（硬科技）和示例 2（医药）不同，AI 编程赛道**迭代周期以月计**，时效要求极高，证据中 6 个月以上的数据需明确标注时效降级。

### 示例 4：Southeast Asia EV market（English query, regional market research）

- **Input**: User: "Do a deep-dive on the electric two-wheeler market in Southeast Asia, including competitive landscape and market share by country."
- **Expected output**: Five-section English report `SEA_E2W_market_{CURRENT_YEAR}_report.md` + evidence file. Section 1 must break down market size by country (Indonesia / Vietnam / Thailand / Philippines / Malaysia). Section 2 must compare Yadea, VinFast, Selis, Gogoro and local players with country-level market share. Section 4 must cover battery-swapping policy and subsidy timelines per country.
- **Key points**: Output language matches query language (English query → English report). Regional market research requires per-country granularity in Sections 1-2; pan-regional aggregation alone is insufficient. Currency in USD with local-currency in parentheses for key figures.

## 资源索引

| 资源 | 用途与参数 | 何时使用 |
|------|-----------|----------|
| [scripts/verify_urls.py](scripts/verify_urls.py) | 批量校验证据中所有 URL 可达性，支持文件/参数/stdin 三种输入：`python scripts/verify_urls.py {topic}_evidence.md` | 阶段 4 证据合并后 |
| [scripts/assemble_report.py](scripts/assemble_report.py) | 分块拼接报告，避免单次长文本截断；子命令：`init` / `append` / `validate`；接收 `--topic`、`--title`、`--current-year`（可选，缺省取系统当年，板块标题自动随年份变化）、`--section-key`（exec_summary/part1-5/conclusion）、`--content-file` 参数；通过 stdout 返回 JSON 结果 | 阶段 5、6 写作时分章节调用 |
| [scripts/requirements.txt](scripts/requirements.txt) | 脚本依赖清单（httpx） | 首次使用前 `pip install -r` |
| [references/industry_research_framework.md](references/industry_research_framework.md) | 行业研究查询分解框架，含九大研究维度、行业类型映射、检索关键词字典 | 阶段 1 查询分解、阶段 2 关键词补全 |
| [references/report_template.md](references/report_template.md) | 麦肯锡白皮书风格五大板块完整模板，含每个板块的子小节结构、必备表格列、可视化建议 | 阶段 5 写作时严格对照 |
| [references/visual_style_guide.md](references/visual_style_guide.md) | 麦肯锡蓝灰风视觉规范：配色系统、字体、Mermaid 主题 init 模板与 classDef、Plotly 桑基图标准代码、matplotlib 兜底配色、图与表的取舍规则 | 阶段 5 任何图表生成前必读 |

## 注意事项

- 仅在需要时加载参考文件，保持上下文简洁；阶段 1 必读 `industry_research_framework.md`，阶段 5 必读 `report_template.md`。
- **时效性是高客单价交付的生命线**：早于 `{LAST_YEAR}` 的数据必须显式降级或替换；`{LAST_YEAR}` H2 至 `{CURRENT_YEAR}` 的证据为主力；前瞻判断聚焦 `{CURRENT_YEAR}`-`{NEXT_YEAR}`。所有占位符在阶段 0 解算后自动随当年滚动，无需手动维护。
- **数字必须可溯源**：核心数字若找不到深链来源，宁可写"暂无公开权威数据"也不要编造。
- **长报告必须分块拼接**：禁止试图一次性输出 6,000+ 字完整报告，必须按阶段 6 流程逐板块写入再拼接，避免截断与格式丢失。
- **专业 Skill 优先**：宏观/财务/法规等数据领域优先调用专业 Skill，`search_web` 仅作叙事性补充与兜底。
- 报告产出在用户当前工作目录（`./`），Skill 自身目录只读。
