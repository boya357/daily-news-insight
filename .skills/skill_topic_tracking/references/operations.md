# Operations：查看、验收、删除和排障

本文用于非新建、非正文 briefing 的管理操作。

## 列举当前追踪

```bash
python .skills/skill_topic_tracking/scripts/guide.py list
```

用于：

- 新建前查重。
- 用户问当前追踪了哪些话题。
- 用户手动要求查看某话题最新动态但没有提供 `setup_token`。
- 排查某个话题对应的 setup_token、目录或最近产物。

## 查看进度

随时查看某个 token 的当前状态和下一步指引：

```bash
python .skills/skill_topic_tracking/scripts/guide.py status <token>
```

适用于：agent 上下文丢失后快速恢复、确认某个 setup 或 briefing 是否已完成。

## 校验本次运行

主会话验收本次子会话/日程产物时，必须直接用日程描述里的 `setup_token` 运行：

```bash
python .skills/skill_topic_tracking/scripts/guide.py verify-run --setup-token "setup_xxxxxxxx"
```

验收命令会给出本次运行是否可交付、如何交付、是否需要重跑的具体说明。主会话必须按命令输出执行，不得跳过验收直接交付。

内部排障时也可以指定 token、run_status 或 after 参数，以脚本 help 为准。

## 删除 / 取消某个追踪

删除命令默认只预览，不会真正删除。确认无误后再追加 `--yes`。

按话题名预览删除：

```bash
python .skills/skill_topic_tracking/scripts/guide.py delete --topic "话题名"
```

按 setup_token 预览删除：

```bash
python .skills/skill_topic_tracking/scripts/guide.py delete --setup-token "setup_xxxxxxxx"
```

确认删除状态、session 和话题产物目录：

```bash
python .skills/skill_topic_tracking/scripts/guide.py delete --setup-token "setup_xxxxxxxx" --yes
```

只删除状态和 session，保留历史日报/事件文件：

```bash
python .skills/skill_topic_tracking/scripts/guide.py delete --setup-token "setup_xxxxxxxx" --keep-files --yes
```

如果用户是要取消定时追踪，删除本地追踪记录后，还需要删除或更新对应日程。

## Token 规则

- setup 流程 token 形如 `setup_xxxxxxxx`，用于标识一个已创建的话题追踪。
- briefing 流程 token 形如 `brief_xxxxxxxx`，每次子会话或重复日程运行都要重新 init，生成不同 token。
- 主会话和日程一般只需要保存 `setup_token`；`brief token` 只用于推进单次流程，不要暴露给用户。
