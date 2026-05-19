# 话题简报生成指南（日程子 agent 专用）

日程触发时，或用户要求查看某话题最新动态时，按以下流程执行。

**你的角色：** 像一个专业的信息分析师，对话题进行类似 deep research 的深度探索——不是机械地搜索和罗列，而是带着判断力去搜索、筛选、追踪线索、交叉验证，最终输出一份高质量的个性化简报。

**⚠️ 每次只执行当前步骤。执行完写入留痕文件、更新 `.state.json` 后，再进入下一步。**

---

## Step B1：解析任务指引

从日程 description 中提取执行上下文：

- **话题**：追踪的核心话题
- **追踪方向**：用户确认的关注维度（这是你的搜索和简报组织框架）
- **搜索关键词**：预设的搜索词列表
- **存储目录**：简报文件的写入路径（如 `~/Documents/topic_tracking/黄金价格`）
- **用户偏好**：用户对简报内容和格式的个性化要求
- **简报要求**：输出的质量标准

如果是用户主动要求更新（非日程触发），从对话上下文中理解话题和关注方向。

### 留痕：B1_task_context.json

```json
{
  "step": "B1",
  "timestamp": "ISO8601",
  "input": {
    "trigger_type": "calendar|user_request",
    "description_text": "日程 description 原文（若有）"
  },
  "output": {
    "topic": "黄金价格",
    "directions": ["国际金价走势", "美联储政策", "国内金价"],
    "keywords": ["黄金价格 最新行情", "美联储 黄金 利率"],
    "tracking_dir": "~/Documents/topic_tracking/黄金价格",
    "user_preferences": {},
    "briefing_requirements": []
  }
}
```

**更新 `.state.json`**：`current_step` → `"B2"`，`"B1"` 加入 `completed_steps`。

---

## Step B2：读取记忆

搜索历史记忆，获取两类关键信息：

### 2a. 追踪历史

```json
memory_search({
  "query": "{话题名} 追踪简报 摘要",
  "max_results": 5
})
```

从历史记忆中提取：
- **上次推送的关键内容**：避免重复推送相同信息
- **关键数据基线**：如"上次金价 4750"，方便做对比分析
- **已覆盖的事件和来源**：这些是"已读"内容，本次不重复展示

### 2b. 用户习惯

```json
memory_search({
  "query": "{用户名} 偏好 习惯",
  "max_results": 3
})
```

从记忆中识别用户的个性化特征：
- **关注深度**：偏好快速摘要还是深度分析
- **语言风格**：正式/轻松、中英文偏好
- **信息偏好**：重数据还是重观点、关注宏观还是微观
- **特殊要求**：如"不要自媒体来源"、"关注具体数字"等

这些习惯会影响后续的信息筛选和简报风格。首次执行时若无历史记忆，跳过此步。

### 留痕：B2_memory.json

```json
{
  "step": "B2",
  "timestamp": "ISO8601",
  "input": {
    "memory_queries": ["{话题名} 追踪简报 摘要", "{用户名} 偏好 习惯"]
  },
  "output": {
    "tracking_history": {
      "last_push_date": "2026-04-23",
      "key_data_baseline": {"现货黄金": "4750 美元/盎司"},
      "covered_events": ["美伊谈判进展", "央行购金数据"],
      "covered_sources": ["wallstreetcn.com", "reuters.com"]
    },
    "user_habits": {
      "depth": "深度分析",
      "style": "正式",
      "focus": "重数据"
    },
    "has_history": true
  }
}
```

**更新 `.state.json`**：`current_step` → `"B3"`，`"B2"` 加入 `completed_steps`。

---

## Step B3：多角度搜索

从日程 description 中获取搜索关键词，用 search_web 做第一轮广泛搜索：

```json
search_web({
  "query_list": [
    "黄金价格 最新行情",
    "黄金走势 今日分析",
    "美联储 黄金 利率",
    "国际金价 实时"
  ],
  "freshness": 1
})
```

**搜索要求：**
- **freshness 必须填**：日程执行用 `freshness: 1`（最近 1 天）
- **query_list 覆盖追踪方向**：每个追踪方向至少一个搜索词
- **关键词要具体**：加"最新"、"今日"、"分析"等限定词

**结果太少时：**
1. 去掉过于具体的限定词，用更宽泛的表述重新搜索
2. 把 freshness 从 1 调到 2，扩大时间范围
3. 宁可多搜一些再筛选，也不要因为搜索词太窄而遗漏重要信息

### 留痕：B3_search_results.json

```json
{
  "step": "B3",
  "timestamp": "ISO8601",
  "input": {
    "queries": ["黄金价格 最新行情", "黄金走势 今日分析", ...],
    "freshness": 1
  },
  "output": {
    "total_results": 24,
    "per_query_count": {"黄金价格 最新行情": 8, "黄金走势 今日分析": 6, ...},
    "all_titles": ["标题1", "标题2", ...],
    "retry_needed": false
  }
}
```

**更新 `.state.json`**：`current_step` → `"B4"`，`"B3"` 加入 `completed_steps`。

---

## Step B4：信息筛选（像人一样判断）

对搜索结果进行多维度评估和筛选。**不是所有搜索到的都值得放进简报**——你需要像一个经验丰富的编辑一样，做出判断。

### 筛选维度

按以下维度对每条搜索结果打分/判断：

| 维度 | 判断标准 |
|------|---------|
| **相关性** | 与话题和用户关注方向的匹配度。偏题内容直接淘汰 |
| **时效性** | 越新越好。已过时的分析、旧闻翻炒直接淘汰 |
| **信息质量** | 有具体数据/事实/深度分析 > 泛泛而谈/标题党/纯转载 |
| **来源权威性** | 主流媒体/专业机构/官方发布 > 自媒体/内容农场/不明来源 |
| **去重** | 同一事件多篇报道只保留来源最权威、信息最完整的一篇 |
| **吸引力（CTR）** | 用户大概率会想点开看的内容优先——突破性进展、反直觉发现、直接影响用户利益的信息 |

### 筛选流程

1. **快速过滤**：去掉明显不相关、过时、低质量的结果
2. **去重合并**：同一事件/观点的多篇报道，选最权威的保留
3. **与历史对比**：对照 Step B2 的追踪历史，去掉上次已推送过的旧内容
4. **优先级排序**：按「信息价值 × 用户吸引力 × 来源权威性 × 时效性」综合排序
5. **挑选深读目标**：从筛选后的结果中，选出 3-5 篇最值得深入阅读的文章

### 留痕：B4_filtered.json

```json
{
  "step": "B4",
  "timestamp": "ISO8601",
  "input": {
    "total_candidates": 24
  },
  "output": {
    "passed": [
      {"title": "...", "url": "...", "reason": "国际金价核心数据，权威来源"}
    ],
    "rejected": [
      {"title": "...", "url": "...", "reason": "旧闻翻炒，上次已推送"}
    ],
    "deep_read_targets": ["url1", "url2", "url3"],
    "passed_count": 8,
    "rejected_count": 16
  }
}
```

**更新 `.state.json`**：`current_step` → `"B5"`，`"B4"` 加入 `completed_steps`。

---

## Step B5：构建结构化验证数据（⚠️ 门控步骤）

**⚠️ 重要：每条纳入简报的资讯必须生成完整的结构化验证数据。本步骤有门控校验，不通过不能进入 B6。**

对筛选出的每条资讯，按以下格式构建结构化数据：

### 数据格式

```json
{
  "title": "文章标题",
  "link": "https://example.com/article",
  "summary": "200字以内的核心摘要，提炼关键信息和价值点",
  "validation": {
    "relevance": "具体说明：解释为什么这条资讯与话题和用户关注方向相关",
    "freshness": "发布时间（YYYY-MM-DD HH:MM）：说明信息的时效性",
    "quality": "具体说明：说明信息质量，包含哪些具体数据、分析深度",
    "ctr_pred": "具体说明：说明为什么用户会感兴趣",
    "dedup": "具体说明：说明是否与历史记录重复",
    "authority": "具体说明：说明来源的可信度"
  }
}
```

### 验证维度说明

| 维度 | 填写要求 | 说明 |
|------|---------|------|
| **relevance** | 具体说明 | 解释为什么与话题相关，提供判断依据 |
| **freshness** | 时间+说明 | 发布时间+时效性说明。如"2026-04-24 09:15 - 今日首发" |
| **quality** | 具体说明 | 列举包含的具体数据、分析深度 |
| **ctr_pred** | 具体说明 | 说明吸引力来源，哪些信息点会让用户感兴趣 |
| **dedup** | 具体说明 | 基于 Step B2 历史记忆对比，说明是否重复 |
| **authority** | 具体说明 | 结合用户需求评估来源可信度 |

### 生成规范

1. **每条纳入简报的资讯必须生成完整数据**
2. **每个维度必须填写具体说明，不能只填高/中/低评级**
3. **每个维度至少 5 个字符**，越具体越好
4. **authority 要结合用户需求**：如果用户需要爆料，可以容忍低权威来源
5. **dedup 必须基于 Step B2 的历史记忆对比**

### 写入 validation.json

将所有验证数据整理为 JSON 数组，写入**话题追踪目录**：

```
{tracking_dir}/{YYYY-MM-DD}_validation.json
```

例如：`~/Documents/topic_tracking/黄金价格/2026-04-25_validation.json`

文件内容示例见 `references/briefing_fewshot.md`。

### ⚠️ 门控校验

写入 validation.json 后，**必须执行验证命令**：

```bash
python skills/topic_tracking_v3/scripts/validate_tracking.py /绝对路径/{YYYY-MM-DD}_validation.json
```

**处理验证结果：**
- `"pass": true` → 校验通过，可以继续
- `"pass": false` → 根据 `errors` 列表修正 validation.json → 重写文件 → 重新验证 → 循环直到通过

**常见校验失败原因：**
- 缺少某个维度（如忘了填 `dedup`）
- 维度说明太短（需要至少 5 个字符的具体说明）
- 缺少 `title`、`link`、`summary` 等必要字段

### 留痕：B5_validation.json

```json
{
  "step": "B5",
  "timestamp": "ISO8601",
  "input": {
    "articles_count": 8,
    "validation_file_path": "/绝对路径/2026-04-25_validation.json"
  },
  "output": {
    "validation_result": {"pass": true, "total_articles": 8},
    "retry_count": 0,
    "errors_fixed": []
  }
}
```

**更新 `.state.json`**：`current_step` → `"B6"`，`"B5"` 加入 `completed_steps`。**仅在校验通过后才能更新。**

---

## Step B6：深度阅读与延展探索

对 Step B4 筛选出的重点文章，用 fetch_web 获取全文：

```json
fetch_web({
  "urls": [
    "https://wallstreetcn.com/articles/xxxxx",
    "https://finance.sina.com.cn/xxxxx",
    "https://www.reuters.com/xxxxx"
  ]
})
```

**深度阅读时注意：**
- 提取具体数据、关键引用、专家观点
- 交叉验证不同来源对同一事件的报道
- 识别与上次追踪数据的变化（涨跌、立场转变等）

**延展探索（Deep Research 核心能力）：**

阅读全文时，如果发现新的重要线索（报告引用、新发展、关联事件），做补充搜索追踪：

> 例如：搜索"美伊局势"时，某篇文章提到"欧盟刚发表联合声明"，那就再搜一下"欧盟 美伊 声明"获取更多细节。
>
> 例如：追踪"AI 大模型"时，发现某篇提到"Anthropic 刚获得新一轮融资"，追踪搜索"Anthropic 融资 2026"补充信息。

这种"顺藤摸瓜"的延展搜索是生成高质量简报的关键——它让你的简报有深度，而不只是搜索结果的简单堆砌。

**无新内容时：** 如果所有结果都是上次已推送的旧内容（通过 Step B2 记忆对比），简要告知用户"本次未发现新动态"即可，不强行编造简报。

### 留痕：B6_deep_read.json

```json
{
  "step": "B6",
  "timestamp": "ISO8601",
  "input": {
    "target_urls": ["url1", "url2", "url3"]
  },
  "output": {
    "articles_read": [
      {
        "url": "url1",
        "key_data": ["现货黄金 4692 美元/盎司", "日内跌幅 1.0%"],
        "key_quotes": ["分析师认为..."],
        "changes_from_last": "金价从 4750 → 4692，下跌 58 美元"
      }
    ],
    "extended_searches": [
      {"query": "欧盟 美伊 声明", "reason": "文章提到欧盟声明", "results": 3}
    ],
    "has_new_content": true
  }
}
```

**更新 `.state.json`**：`current_step` → `"B7"`，`"B6"` 加入 `completed_steps`。

---

## Step B7：生成简报

将所有搜索结果和全文信息汇总，按照简报格式生成输出。

### 简报格式

**参考 `references/briefing_fewshot.md` 中的完整示例。** 核心规范：

**标题：**
```
今日{话题}速览（MM-DD）：
```

**正文结构：**
- 按追踪方向分段，每段围绕一个主题
- 提炼关键数据和要点，不逐条罗列搜索结果
- 相关新闻合并叙述
- **个性化调整**：根据 Step B2 识别的用户习惯调整内容深度和风格

**引用格式：**
```
[[序号]](URL)（MM-DD HH:MM）
```
- 序号从 1 递增
- URL 是文章原始链接
- 时间是发布时间，行情/事件类精确到时分
- 多篇报道同一事件：`[[3]][[4]]`，选来源最权威的作为主引用

**结尾：**
```
**值得关注：** 列出 1-2 个后续看点
```

### 内容排序

简报内容按以下优先级组织：

1. **信息价值**：重大变化、突破性进展 > 常规动态 > 背景分析
2. **用户吸引力**：用户明确关心的方向优先展示
3. **来源权威性**：主流媒体 / 专业机构 > 自媒体 / 转载站
4. **时效性**：越新越靠前

### 质量红线

- **有源可查**：每个关键信息点必须有来源链接，不能凭空生成
- **数据准确**：价格、百分比、时间等数据从原文直接提取，不推测不编造
- **来源可信**：优先引用权威媒体和专业机构，避免低质量来源
- **去重合并**：同一事件多篇报道合并，选来源最权威的
- **时间精确**：行情、事件标注具体发布时间（到小时分钟）

### 留痕：B7_briefing_draft.json

```json
{
  "step": "B7",
  "timestamp": "ISO8601",
  "input": {
    "articles_used": 8,
    "directions_covered": ["国际金价走势", "美联储政策", "国内金价"]
  },
  "output": {
    "title": "今日黄金行情速览（04-25）：",
    "sections_count": 3,
    "references_count": 7,
    "word_count": 450,
    "highlights": ["金价跌破4700", "央行增持150吨"]
  }
}
```

**更新 `.state.json`**：`current_step` → `"B8"`，`"B7"` 加入 `completed_steps`。

---

## Step B8：写入简报文件

将生成的简报写入话题追踪目录。

### 格式延续

**写入前，先读取存储目录下最近的 1-2 个已有简报文件**，观察其格式风格（标题格式、分段方式、引用写法等），确保本次简报与已有内容保持一致。首次写入无历史文件时，按 `references/briefing_fewshot.md` 的格式。

### 写入简报 .md

1. **路径**：`{tracking_dir}/{YYYY-MM-DD}.md`，如 `~/Documents/topic_tracking/黄金价格/2026-04-25.md`
2. **目录不存在时自动创建**
3. **同一天多次执行**：追加到同一个文件中，用 `---` 分隔不同时段的简报
4. **文件内容**：只写简报正文（标题到值得关注），不包含追踪摘要和口语总结

### 确认 validation.json

确认 Step B5 写入的 `{YYYY-MM-DD}_validation.json` 已在同目录。如果 B5 时已写入且通过校验，此步无需重复写入。

### 留痕：B8_output.json

```json
{
  "step": "B8",
  "timestamp": "ISO8601",
  "input": {
    "tracking_dir": "~/Documents/topic_tracking/黄金价格"
  },
  "output": {
    "briefing_path": "~/Documents/topic_tracking/黄金价格/2026-04-25.md",
    "validation_path": "~/Documents/topic_tracking/黄金价格/2026-04-25_validation.json",
    "is_append": false,
    "format_followed_from": "2026-04-24.md"
  }
}
```

**更新 `.state.json`**：`current_step` → `"B9"`，`"B8"` 加入 `completed_steps`。

---

## Step B9：保存本期追踪摘要

简报生成后，在回复末尾附上一段 **追踪摘要**（这段内容会自动进入对话记忆，供下次追踪时 memory_search 检索）：

```
---
📋 本期追踪摘要（{话题名} {YYYY-MM-DD}）：
- 关键数据：{列出本期核心数据点，如"现货黄金 4692 美元/盎司"、"国内金饰 1215-1457 元/克"}
- 重要事件：{列出本期覆盖的主要事件，1-3 句话}
- 已引用来源：{列出主要来源域名}
- 下期关注：{值得后续跟踪的线索}
---
```

**为什么要保存摘要：**
- 下次执行时 memory_search 能检索到，实现跨次去重
- 对比关键数据变化（如金价从 4750 → 4692）
- 避免反复推送同一事件

### 留痕：B9_summary.json

```json
{
  "step": "B9",
  "timestamp": "ISO8601",
  "input": {},
  "output": {
    "summary_text": "本期追踪摘要全文",
    "key_data": {"现货黄金": "4692 美元/盎司", "国内金饰": "1215-1457 元/克"},
    "key_events": ["美伊僵局拖累金价", "央行连续三月增持"],
    "sources": ["wallstreetcn.com", "reuters.com", "sina.com.cn"],
    "next_watch": ["美伊局势后续", "两天内变盘信号"]
  }
}
```

**更新 `.state.json`**：`current_step` → `"B10"`，`"B9"` 加入 `completed_steps`。

---

## Step B10：口语总结

生成格式化简报后，再用 2-3 句话做一个口语化的要点总结，帮助用户快速抓住重点。

要点：
- 点出最重要的 1-2 个变化
- 如果有和上次追踪相比的变化，必须点出来
- 根据用户习惯调整语气（正式/轻松）

示例：

> 今天黄金整体回调，从 4750 跌到 4692 附近又反弹。主要受美伊僵局影响，避险情绪反复。国内金店也跟着跌了 21 块/克。值得留意明后两天的变盘信号。

### 留痕：B10_spoken.txt

直接写入口语总结文本即可。

**更新 `.state.json`**：`current_step` → `"DONE"`，`"B10"` 加入 `completed_steps`。

**流程结束。** 🎉
