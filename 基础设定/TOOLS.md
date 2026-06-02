# 工具使用指南（精简版）

## 核心脚本
- **simple_push.py**：企业微信推送（`python3 simple_push.py "标题" "URL"`）
- **md_to_html.py**：Markdown转HTML（已废弃，改用report_converter）
- **update_all_lists.py**：修复技能生成的跳转latest.html为列表页，路径：`/app/data/所有对话/主对话/update_all_lists.py`（不在src目录）
- **report_converter/generate_report.py**：专业报告生成系统V1.0，统一入口，支持全部11种报告类型

## 🎯 专业报告生成系统V1.0（2026-05-31发布）

### 核心信息
- **工具位置**：`/app/data/所有对话/主对话/docs/report_converter/`
- **入口脚本**：`scripts/converter.py`
- **支持报告数**：11种全类型
- **核心价值**：彻底解决latest.html覆盖问题，统一报告风格

### 核心功能（5项）
智能Markdown解析、专业组件库、11种报告类型、原子写入机制、列表页独立生成

### MLCC Pro三级模板体系
| 级别 | 适用场景 | 核心功能 |
|------|---------|---------|
| **Level 1 深度研报 | 产业链深度研究、重大专题报告 | 6章完整结构、10+交互式图表、核心数据卡片、五星标的推荐、目录卡片导航高亮 |
| **Level 2 标准报告** | 周复盘、月报、催化日历 | 3-4章内容、支持3-5个图表、所有MLCC Pro核心功能 |
| **Level 3 轻量快报** | 每日新闻洞察、盘中快报、盘后速递 | 极简结构、保留统一导航栏 |

### 快速使用（3种模式）
```bash
cd /app/data/所有对话/主对话/docs/report_converter/scripts

# 1. 单篇转换
python converter.py convert <md文件> <html文件> [类型]

# 2. 批量转换目录
python converter.py batch <目录> [输出目录]

# 3. 单个文件
python converter.py daily/20260530_每日新闻洞察.html
```

### 报告类型参数（常用5种）
`daily`日报、`intraday`盘中、`aftermarket`盘后、`industry_chain`产业链、`weekly_review`周复盘

> 完整11种类型、Python API、安全特性说明：见 `recent_memory/project/20260531_专业报告生成系统V1.0发布.md`

### MLCC Pro模板核心特性
> 完整16项功能列表、详细文档：见 `recent_memory/project/20260531_专业报告生成系统V1.0发布.md`

## ⚠️ 数据验证铁律
**任何数据必须反复验证后才能写入报告，绝对不能凭记忆或未经核实直接引用！**

## 🏗️ 系统架构规范

### 工作目录
- **Git仓库**：`/app/data/所有对话/主对话/docs/`

### 两大模块分类原则（核心）
| 模块类型 | 命名规范 | 包含目录 |
|---------|---------|---------|
| **报告类（11个）** | `latest.html` | daily、intraday、aftermarket、weekly_review、weekly_outlook、monthly、industry_chain、s级催化扫描、催化日历、周末速递、明日催化剂 |
| **工具类（5个）** | `index.html` | 产业链时钟、智能预警系统、持仓智能预警仪表盘、智能选题助手、预判验证 |

## 🚨 核心工作流程与防错原则

### 修改前强制检查
1. **列目录**：`ls docs/`确认目标目录存在（共16个目录）
2. **模块判断**：报告类→latest.html，工具类→index.html，禁止跨模块
3. **文件验证**：`ls docs/目标目录/`确认文件真实存在

### 三大防错原则（绝对不能违反）
1. 不存在的目录绝对不能写
2. 绝对不能跨模块乱放报告
3. 文件名必须匹配模块类型

### Git同步流程
- 工作目录：`/app/data/所有对话/主对话`
- 安全检查：pwd确认 → ls验证 → 确认latest.html>3KB → 只add目标目录，绝不add -A

### 🔴 技能缺陷与修复
- **问题**：skill_daily-news-report的.so模块会写跳转latest.html
- **强制修复**：改用`report_converter/generate_report.py`
- **补充修复**：用`update_all_lists.py`恢复列表页

## 📋 核心错误检查清单
| 检查项 | 要求 |
|-------|------|
| 价格数据 | 必须查当日收盘价，禁止用历史数据 |
| latest.html | >3KB，是列表页不是跳转页/单篇报告 |
| 目录检查 | 先`ls docs/`确认存在，禁止跨模块 |
| 链接验证 | 修改后抽查3-5个链接 |
| 持仓限制 | 仅3个持仓，禁止添加其他标的 |
| 重复报告 | 立即删除v2/v3/v4等中间版本 |
| 导航栏统一 | 同时验证首页、列表页、单篇报告 |
| 模板验证 | 深度报告必须用MLCC同款模板 |
| 重复报告卡片 | 插入前必须搜索文件，确认没有相同文件名已存在 |
| 卡片样式一致性 | 必须完整复制既有卡片的HTML结构，绝对禁止自创样式 |

> **完整规范、定时任务、错误教训**：详见 `recent_memory/` 相关文档
