# 创建订阅指南（主 agent 专用）

用户说"帮我追踪 XXX"、"我想关注 XXX"时，按以下步骤执行。

**⚠️ 每次只执行当前步骤。执行完写入留痕文件、更新 `.state.json` 后，再进入下一步。**

---

## Step S1：探索话题

先搜一轮，了解话题当前的热点方向和分支：

```json
search_web({
  "query_list": ["黄金价格 最新", "黄金行情 走势分析", "黄金 影响因素 今日"],
  "freshness": 2
})
```

- `query_list`：用 2-4 个不同角度的搜索词，覆盖话题的主要维度
- `freshness: 2`：探索阶段看最近 2 天，范围稍大

浏览搜索结果，识别出话题当前的 **核心分支方向**（通常 3-5 个）。比如"黄金价格"可能有：国际金价走势、央行购金、美联储政策、地缘政治避险需求、国内金饰零售价等。

### 留痕：S1_exploration.json

```json
{
  "step": "S1",
  "timestamp": "ISO8601",
  "input": {
    "topic": "黄金价格",
    "queries": ["黄金价格 最新", "黄金行情 走势分析", "黄金 影响因素 今日"]
  },
  "output": {
    "total_results": 15,
    "identified_directions": [
      "国际金价走势（现货黄金、COMEX期货）",
      "央行购金动态",
      "美联储政策对金价的影响",
      "地缘政治避险需求",
      "国内金价和品牌金店零售价"
    ],
    "top_results": [
      {"title": "...", "url": "...", "source": "..."}
    ]
  }
}
```

**更新 `.state.json`**：`current_step` → `"S2"`，`topic` → 话题名，`"S1"` 加入 `completed_steps`。

---

## Step S2：与用户确认

将探索结果和分支方向告诉用户，确认：

- 重点关注哪些方向
- 追踪频率（每天？每几小时？）
- **简报存储根目录**（如 `~/Documents/topic_tracking`）
- 是否有特殊关注点或偏好（如只看中文源、只关心数据不关心评论等）

**可跳过确认的情况：** 用户在请求中已经明确了方向和频率（如"每天早上帮我看看 AI 最新动态"），直接执行即可。但**存储根目录必须确认**。

示例回复：

> 我搜索了「黄金价格」最近的动态，目前有这些热点方向：
> 1. 国际金价实时走势（近日回调至 4750 附近）
> 2. 美联储利率决策对金价的影响
> 3. 地缘政治推动的避险需求
> 4. 国内品牌金店零售价变化
>
> 你希望重点关注哪些方向？建议每天推送一次，你觉得呢？
> 另外，简报文件存储在哪个目录？（如 ~/Documents/topic_tracking）

### 留痕：S2_confirmation.json

```json
{
  "step": "S2",
  "timestamp": "ISO8601",
  "input": {
    "proposed_directions": ["国际金价走势", "央行购金", "美联储政策", "地缘避险", "国内金价"],
    "proposed_frequency": "DAILY"
  },
  "output": {
    "confirmed_directions": ["国际金价走势", "美联储政策", "国内金价"],
    "frequency": "DAILY",
    "storage_root": "~/Documents/topic_tracking",
    "tracking_dir": "~/Documents/topic_tracking/黄金价格",
    "user_preferences": {
      "focus": "关注行情数据变化，需标注具体时分",
      "style": "重点关注对比上一次推送的变化"
    }
  }
}
```

**更新 `.state.json`**：`current_step` → `"S3"`，`tracking_dir` → 用户确认的路径，`"S2"` 加入 `completed_steps`。

---

## Step S3：创建定时日程

用户确认后，用 `calendar_create` 创建定时日程。

**日程的 `description` 是核心——它是日程触发时子 agent 的完整执行指引。** 写得好不好，直接决定简报的质量。

```json
calendar_create({
  "summary": "话题追踪：黄金价格",
  "description": "【话题追踪任务 - 请使用 topic_tracking_v3 技能执行】\n\n## 话题\n黄金价格\n\n## 追踪方向\n- 国际金价走势（现货黄金、COMEX期货）\n- 美联储政策对金价的影响\n- 国内金价和品牌金店零售价\n\n## 搜索关键词\n黄金价格 最新行情, 黄金走势 今日分析, 美联储 黄金 利率, 国际金价 实时, 国内金价 金店\n\n## 存储目录\n~/Documents/topic_tracking/黄金价格\n\n## 用户偏好\n- 关注行情数据变化，需标注具体时分\n- 重点关注对比上一次推送的变化\n\n## 简报要求\n- 按追踪方向分段归纳，不逐条罗列\n- 每个关键信息附引用链接和发布时间\n- 行情数据标注具体时分\n- 末尾列出 1-2 个值得关注的后续看点\n- 必须同时输出 validation.json 验证数据",
  "dtstart": "202604250900",
  "rrule": {
    "freq": "DAILY",
    "interval": 1
  },
  "time_range": {
    "earliest_schedule_time": "202604250830",
    "latest_schedule_time": "202604250930"
  }
})
```

### description 编写规范

description 要让未来执行的子 agent 能独立完成任务，必须包含：

1. **开头标记**：`【话题追踪任务 - 请使用 topic_tracking_v3 技能执行】` — 触发技能加载
2. **话题**：明确的话题名称
3. **追踪方向**：列出用户确认的关注方向（子 agent 按这些方向组织搜索和简报）
4. **搜索关键词**：具体的搜索词列表，子 agent 直接拿来用
5. **存储目录**：简报文件的存储路径 `{根目录}/{话题名}`（不含日期，日期在写入时自动生成）
6. **用户偏好**：根据确认环节中用户表达的偏好填写
7. **简报要求**：输出格式和质量标准
8. **validation 要求**：必须同时输出 validation.json

不要写模糊描述（如"搜索相关内容"），要给出能直接执行的具体指令。搜索关键词应根据 Step S1 探索结果动态生成——不是简单地把话题名重复几遍，而是根据实际分支方向构造差异化搜索词。

### 频率建议

| 话题类型 | 建议频率 | rrule |
|---------|---------|-------|
| 突发新闻 / 战争 / 危机 | 每 2-4 小时 | `{"freq": "HOURLY", "interval": 3}` |
| 行情 / 股价 / 汇率 | 每天 1-2 次 | `{"freq": "DAILY", "interval": 1}` |
| 行业动态 / 技术趋势 | 每天 1 次 | `{"freq": "DAILY", "interval": 1}` |
| 长期跟踪 / 竞品监控 | 每天或每周 | `{"freq": "WEEKLY", "interval": 1}` |

### 留痕：S3_calendar.json

```json
{
  "step": "S3",
  "timestamp": "ISO8601",
  "input": {
    "topic": "黄金价格",
    "frequency": "DAILY",
    "tracking_dir": "~/Documents/topic_tracking/黄金价格"
  },
  "output": {
    "calendar_id": "返回的日程ID",
    "summary": "话题追踪：黄金价格",
    "description": "完整 description 文本",
    "dtstart": "202604250900",
    "rrule": {"freq": "DAILY", "interval": 1}
  }
}
```

**更新 `.state.json`**：`current_step` → `"S4"`，`"S3"` 加入 `completed_steps`。

---

## Step S4：立即执行首次简报

创建日程后，**马上执行一次简报**，让用户立刻看到第一份简报。

用户说"帮我追踪"时，期望现在就看到内容，不是明天才收到。先出一份简报，用户满意了才有信心等后续定时推送。

**状态切换**：将 `.state.json` 的 `flow` 改为 `"briefing"`，`current_step` 改为 `"B1"`，然后按 `references/briefing_guide.md` 从 B1 开始执行。

---

## 管理已有订阅

- **查看订阅**：用 `calendar_search` 搜索"话题追踪"查看所有追踪日程
- **修改订阅**：用 `calendar_update` 修改日程的搜索关键词、频率等
- **取消订阅**：用 `calendar_delete` 删除对应的追踪日程
- **临时更新**：用户说"看看 XXX 最新的"时，直接按 `references/briefing_guide.md` 执行一次
