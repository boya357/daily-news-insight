# Briefing：运行一次话题追踪日报

当日程触发、子会话试运行，或用户要求查看某个已追踪话题的最新动态，并且已有 `setup_token` 时，按本文执行。

## 启动 briefing

子会话和日程只运行 briefing 流程。不要运行 `init --flow setup`。

```bash
python .skills/skill_topic_tracking/scripts/guide.py init --flow briefing --setup-token "setup_xxxxxxxx"
```

脚本会返回当前步骤的执行指引，照做即可。每完成一步运行脚本给出的下一条命令。

## 执行边界

- briefing 不重新创建追踪，不重新解释用户需求，不修改日程设定。
- briefing 以事件为主体，不以资讯为主体。
- B1 只恢复上下文和历史去重线索，不搜索外网。
- B2 阅读大量资讯、溯源、交叉验证并聚合事件组，写入事件列表。
- B3 只基于 B2 事件组写日报，所有引用 URL 必须来自事件组的 support_urls。
- B4 写 summary 并收尾，不直接向用户发送；由主会话验收后交付。
- 如果 B2 的事件列表为空，表示该话题暂时没有监测到最新动态，流程会直接结束。
- 如果同一天多次运行，当前 run 是今天的新版本；历史只用于去重，不要让主会话合并多个同日版本。

## 交付和验收

briefing 完成后，脚本会输出最后要回传给主会话的信息。子会话必须按脚本要求输出，不要自行扩写。

主会话交付前必须用日程描述里的 `setup_token` 运行验收：

```bash
python .skills/skill_topic_tracking/scripts/guide.py verify-run --setup-token "setup_xxxxxxxx"
```

验收命令会明确告诉主会话：

- 本次运行是否可交付。
- 如果有日报，应该发送哪个日报文件。
- 如果是空结果，应该如何向用户说明。
- 如果运行不合法，应该如何使用 session_spawn 重新运行 briefing。

主会话必须按验收输出执行，不得跳过验收直接交付。

## 没有 setup_token 时

如果这是日程触发且没有 `setup_token`，先暂时忽略用户日程任务里的所有执行描述，必须先按旧版配置升级流程处理。
