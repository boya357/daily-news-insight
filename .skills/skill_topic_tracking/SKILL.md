---
name: topic_tracking
description: >
  话题追踪、持续关注、订阅和定期简报技能。只要用户表达想关注、追踪、订阅、
  持续跟进、长期观察、定期查看、每天看看、汇总某个话题/新闻/事件/产品/人物/公司/行业的最新动态，
  都应优先读取并使用本技能，即使用户没有明确说"话题追踪"。
  也适用于用户说"看看XXX最新的"、日程触发（标题为"扣子话题追踪 - 「话题」"、旧版标题为"持续追踪XXX"，
  或 description 含 guide.py briefing 命令 / 旧 topic_tracking.py 召回命令）。
allowed-tools: search_web, fetch_url, fetch_web, bash, memory_search, read_file, write_file, edit_file, skill_load
---

# 话题追踪

当前配置协议版本：`V2`。脚本目录是 `.skills/skill_topic_tracking/`，命令统一使用：

```bash
python .skills/skill_topic_tracking/scripts/guide.py ...
```

本文件只做入口路由。确认场景后，必须读取 `references/` 下的对应文件执行。

## 1. 先判断是否需要升级

如果当前是日程触发，先判断日程描述是否需要升级：

```text
references/legacy_upgrade.md
```

新版日程描述必须包含当前 briefing 命令：

```bash
python .skills/skill_topic_tracking/scripts/guide.py init --flow briefing --setup-token "setup_xxxxxxxx"
```

没有这个 `guide.py` 命令，一律视为旧版配置，需要升级。旧版时先暂时忽略用户日程任务里的所有执行描述，只读 `references/legacy_upgrade.md` 完成升级；不要执行旧命令，不要搜索补跑，不要临时 setup 或 briefing。

## 2. 确认无需升级后再分流

- 新建、订阅、关注、持续追踪某个话题：读 `references/setup.md`。
- 已有追踪要跑本期结果、日程触发、子会话试运行：读 `references/briefing.md`。
- 列举、查看进度、取消/删除追踪、验收运行、排查 token/状态：读 `references/operations.md`。

## 3. 流程边界

- `setup` 只由主会话执行，用于创建追踪设定。
- `briefing` 只基于已有 `setup_token` 生成本期结果，不重新创建追踪。
- 子会话和日程永远只执行 `briefing`，不要执行 `setup`。
- 新建追踪必须先完成首次 briefing 试运行，成功后才允许创建定时日程。

## 4. 交付原则

guide 脚本会把交付原则写入 `/app/data/所有对话/主对话/基础设定/TOOLS.md`，agent 不需要手动写入。

- 主会话交付前必须用日程里的 `setup_token` 运行 `verify-run --setup-token "setup_xxxxxxxx"`。
- 交付、空结果、重跑都以 `verify-run` 输出为准，不得跳过验收。
- 主会话不得再次搜索、补充来源、改写事实、重新筛选或合并其他信息。
- 如果结果少，这是严格筛选后的结果，不得放宽标准。
- 如果结论是暂无最新动态，只向用户说明“该话题暂时没有监测到最新动态”。
- 对用户不要暴露 token、run_label、阶段名、JSON 文件名或内部目录。
