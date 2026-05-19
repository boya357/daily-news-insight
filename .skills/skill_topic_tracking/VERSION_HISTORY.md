# skill_topic_tracking 版本变更记录

## 版本变更总览

| 版本号 | 日期时间 | 改动文件 | 主要改动内容 |
|--------|----------|----------|--------------|
| v1.0 | 2026-04-24 | topic_tracking_v3.zip | 初始版本 |
| v2.0 | 2026-04-29 12:02 | guide.py | 新增 setup/briefing 双流程架构 |
| v2.1 | 2026-04-29 12:11 | guide.py | 优化探索流程 |
| v2.2 | 2026-04-29 13:11 | guide.py, validate_tracking.py | 新增验证过滤逻辑 |
| v2.3 | 2026-04-29 13:18 | guide.py | 完善 briefing 流程 |
| v2.4 | 2026-04-29 14:36 | guide.py, validate_tracking.py | 引入 token 管理机制 |
| v2.5 | 2026-04-29 14:51 | guide.py, validate_tracking.py, SKILL.md | 新增 session 目录结构 |
| v2.6 | 2026-04-29 17:02 | guide.py, validate_tracking.py | 优化 URL 缓存机制 |
| v2.7 | 2026-04-29 17:49 | guide.py, validate_tracking.py, SKILL.md | 添加文本归一化处理 |
| v2.8 | 2026-04-29 18:02 | guide.py | 完善流程引导 |
| v2.9 | 2026-04-29 19:02 | guide.py | 优化 prompt |
| v2.10 | 2026-04-29 19:47 | guide.py, validate_tracking.py | 新增结构化决策字段 |
| v2.11 | 2026-04-30 12:04 | guide.py, validate_tracking.py | 完善字段校验规则 |
| v2.12 | 2026-04-30 12:14 | guide.py, validate_tracking.py | 优化验证逻辑 |
| v2.13 | 2026-04-30 14:44 | guide.py, validate_tracking.py | 新增 verification 字段 |
| v2.14 | 2026-04-30 16:13 | SKILL.md | 更新说明文档 |
| v2.15 | 2026-04-30 17:29 | guide.py | 优化流程 |
| v2.16 | 2026-04-30 17:43 | guide.py | 完善 prompt |
| v3.0 | 2026-05-06 12:05 | guide.py, SKILL.md | 新增 topic_analysis 结构 |
| v3.1 | 2026-05-06 12:10 | SKILL.md | 完善文档 |
| v3.2 | 2026-05-06 12:18 | SKILL.md | 更新说明 |
| v3.3 | 2026-05-06 12:52 | SKILL.md | 完善文档 |
| v3.4 | 2026-05-06 14:22 | SKILL.md, guide.py | 更新流程说明 |
| v3.5 | 2026-05-06 16:05 | guide.py, validate_tracking.py | 新增 authority.source_role |
| v3.6 | 2026-05-06 16:07 | guide.py, validate_tracking.py | 重构为 primary/supporting sources |
| v3.7 | 2026-05-06 17:24 | guide.py, validate_tracking.py | 调整字段结构 |
| v3.8 | 2026-05-06 17:25 | - | 无变化确认 |
| v3.9 | 2026-05-06 18:02 | guide.py, validate_tracking.py | 扩展 source_policy 结构 |
| v3.10 | 2026-05-06 18:02 | guide.py | 补充 source_policy 加载 |
| v3.11 | 2026-05-06 18:02 | validate_tracking.py | 从 contract.json 读取 source_policy |
| v3.12 | 2026-05-06 19:49 | guide.py | 更新 |
| v3.13 | 2026-05-06 20:36 | guide.py, validate_tracking.py | 调整结构 |
| v3.14 | 2026-05-06 20:42 | guide.py, validate_tracking.py | 调整结构 |
| v3.15 | 2026-05-06 21:01 | guide.py, validate_tracking.py | 调整结构 |
| v3.16 | 2026-05-07 11:15 | guide.py, SKILL.md | 更新流程 |
| v3.17 | 2026-05-07 12:12 | SKILL.md, references/legacy_upgrade.md | 新增 legacy_upgrade 参考文档 |
| v4.0 | 2026-05-07 12:12 | 目录重命名 | 重命名为 skill_topic_tracking，去除 v3 |
| v4.1 | 2026-05-11 22:17 | SKILL.md | 大量更新 |
| v4.2 | 2026-05-11 22:42 | guide.py, SKILL.md | 更新 |

---

## 详细改动记录

### v1.0 (2026-04-24)
**来源**: topic_tracking_v3.zip  
**内容**: 初始版本

---

### v2.0-v2.16 (2026-04-29 - 2026-04-30)
**主要特性**:
- setup/briefing 双流程架构
- token 管理机制 (setup_token, brief_token)
- session 目录和 tracking 目录分离
- URL 缓存机制
- 结构化决策字段 (quality, ctr_pred, dedup)
- verification 字段

---

### v3.0-v3.17 (2026-05-06 - 2026-05-07)

| 版本 | 核心改动 |
|------|----------|
| v3.0 | 新增 `topic_analysis` 结构，包含 topic_definition, core_intent, include/exclude_criteria 等 |
| v3.5 | `authority` 字段重构，新增 `source_role`（官方首发/官方转述/专业账号首发等） |
| v3.6 | 引入 `primary_source` / `supporting_sources` 结构 |
| v3.9 | 扩展 `topic_analysis.source_policy` 结构，支持 `single_source_allowed`/`strict` 模式 |
| v3.11 | validate_tracking 从 `tracking_contract.json` 读取 source_policy |
| v3.13 | 回退到旧结构（authority/quality/ctr_pred），新增 URL 缓存机制和 [[n]](url) 编号引用格式校验 |
| v3.17 | 新增 `references/legacy_upgrade.md`，支持旧版 topic_tracking 配置迁移 |

---

### v4.0 (2026-05-07)
**改动**: 
- 目录重命名：`topic_tracking_v3` → `skill_topic_tracking`
- 打包文件名：`topic_tracking_v3.skill` → `skill_topic_tracking.skill`
- 路径更新：`.skills/skill_topic_tracking/scripts/guide.py`
- SKILL.md 引用路径同步更新

---

## 当前版本信息

| 项目 | 值 |
|------|-----|
| 技能名称 | skill_topic_tracking |
| 当前版本 | v4.0 |
| 最新打包文件 | skill_topic_tracking.skill |
| 核心脚本 | guide.py, validate_tracking.py |
| 参考文档 | references/legacy_upgrade.md, references/briefing_guide.md, references/briefing_fewshot.md, references/setup_guide.md |
