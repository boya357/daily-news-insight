# Setup：创建或订阅话题追踪

当用户表达“追踪、关注、订阅、持续跟进、每天看看、定期汇总某话题”等意愿，并且不是旧版配置升级时，按本文执行。

## 先查重

新建前必须先列举当前所有已追踪话题，避免重复创建：

```bash
python .skills/skill_topic_tracking/scripts/guide.py list
```

`list` 会输出当前已追踪的话题、对应 setup_token、存储目录、手动更新命令和未完成流程。

如果已经存在同一话题或明显相同边界的追踪，优先复用已有追踪；如用户只是想看最新动态，改读 `briefing.md`。

## 启动 setup

由当前主会话运行 setup 流程，不要交给日程或子会话运行 setup：

```bash
python .skills/skill_topic_tracking/scripts/guide.py init --flow setup --topic "话题名"
```

旧版配置升级、用户明确要求快速跑一版，或用户已经授权 agent 自行决定时，使用 `--quick` 跳过 S2 用户确认，直接进入首次 briefing 试运行：

```bash
python .skills/skill_topic_tracking/scripts/guide.py init --flow setup --topic "话题名" --quick
```

脚本会输出 S1/S2 的逐步指引。严格按脚本输出执行，每完成一步运行脚本给出的下一条命令。

## 确认与试运行

- 默认先与用户确认追踪方向、频率、存储目录和偏好。
- 如果用户明确说“快速跑一下”“先跑一版”“你定就行”“不用确认”“赶紧跑”等，可以用 `--quick` 跳过确认并直接试运行。
- 旧日程升级场景必须用 `--quick`，按 `legacy_upgrade.md` 执行，不再向用户确认。
- setup 完成后只能先启动子会话执行首次 briefing 试运行。
- 必须等待首次试运行成功返回最终结果后，才允许创建定时日程。
- 如果试运行失败、未完成、未返回最终结果，或用户/agent 还在调整话题边界、来源要求、偏好、频率，禁止创建日程。

## 日程写法

首次试运行成功后，才能创建或更新后续定时日程。

日程标题：

```text
扣子话题追踪 - 「{topic}」
```

日程描述保持简洁，只写版本和 briefing 命令：

```text
版本：V2
python .skills/skill_topic_tracking/scripts/guide.py init --flow briefing --setup-token "setup_xxxxxxxx"
```

日程触发后只运行 briefing，不要重新 setup。

## setup token 规则

- setup 流程 token 形如 `setup_xxxxxxxx`，用于标识一个已创建的话题追踪。
- briefing 阶段只传 `--setup-token`，脚本会自动恢复话题、目录和用户偏好。
- 如果 setup 阶段没有保存 tracking-dir，脚本默认使用 `/app/data/所有对话/主对话/热点资讯追踪/{话题名}`，并保存为绝对路径。
