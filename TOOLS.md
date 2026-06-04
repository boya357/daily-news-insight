# TOOLS.md - 工具使用经验与坑点记录

> **核心原则**：快速参考，详细记录见 `recent_memory/decision/`

---

## 📌 一、报告生成核心规范

### 0. 提交前强制校验【2026-06-03 最高优先级】
```
提交前必须运行：./validate_system.sh
✅ 15项全量校验全部通过 → 可以提交
❌ 任何一项不通过 → 修复后再提交
```

### 1. report_converter 核心流程
```
1. python generate_report.py --type daily --date YYYYMMDD
2. python list_updater.py --type daily  ❌ 禁止用cp覆盖
3. git add 报告.html latest.html
4. git push 后立即验证Pages返回200
5. rm -f *v2.html *v3.html 清理中间版本
```

### 2. 5大禁令（绝对不能犯）
| 禁令 | 后果 | 正确方式 |
|------|------|---------|
| ❌ cp 报告.html latest.html | 列表页变单页 | python list_updater.py |
| ❌ 只推送latest.html | 404错误 | 两个文件一起add+push |
| ❌ 只替换标题不替换内容 | 报告内容错误 | 100%完全替换+核心内容验证 |
| ❌ 保留v2/v3/v4版本 | 列表页重复 | 最终版重命名后立即清理 |
| ❌ 三层导航栏不一致 | 用户体验混乱 | 首页/列表/报告三层同时验证 |

---

## 📌 二、核心验证标准

### 1. Markdown渲染验证（2026-05-31修复后）
所有报告生成后必须验证：
- ✅ 表格：检查 `<table>` 标签存在，而非 `|` 纯文本
- ✅ 加粗：`**文本**` 转为 `<strong>文本</strong>`
- ✅ 列表：`- 列表项` 转为 `<ul><li>列表项</li></ul>`
- ✅ 混合内容：表格后紧跟文本正确渲染

### 2. 导航栏统一标准
- 12个完整导航链接
- max-w-7xl 超宽容器
- 紫色渐变背景风格
- 当前页面高亮 bg-white/20

---

## 📌 三、企业微信推送规范

```python
python simple_push.py \
  --title "YYYY年MM月DD日 报告类型" \
  --url "GitHub Pages完整URL（不含/docs/）" \
  --type "daily"
```

- 仅推送链接，不生成长篇摘要

---

## 📌 四、搜索与数据规范

- **价格数据**：必须用 `search_web` 查当日收盘价，禁止历史数据
- **数据源优先级**：韭研公社 > 财联社 > 东方财富 > 同花顺

---

## 📌 五、Git提交规范

| 类型 | 格式 | 示例 |
|------|------|------|
| 新增报告 | `[报告类型]: YYYYMMDD 描述` | `[产业链]: 20260530 英伟达N1X芯片深度研究` |
| 系统修复 | `[修复]: 描述` | `[修复]: Markdown表格渲染引擎修复` |
| 系统升级 | `[升级]: 描述` | `[升级]: MLCC Pro终极模板` |
| 教训记录 | `[教训]: 描述` | `[教训]: cp命令覆盖latest.html错误` |

---

## 📌 六、核心文档索引（2026-06-03新增）

| 文档 | 作用 | 位置 |
|------|------|------|
| validate_system.sh | 15项全量系统完整性校验 | 根目录 |
| ERROR_KNOWLEDGE_BASE.md | 永久错误知识库，记录所有历史问题+根因+教训 | 根目录 |
| SYSTEM_ARCHITECTURE.md | 完整系统架构与规则手册 | 根目录 |
| DIRECTORY_RULES.md | 目录规则与禁忌，物理隔离规范 | 根目录 |
| update_homepage.py | 首页自动更新脚本 | 根目录 |

---

## 📌 七、发现新问题标准流程

```
发现问题 → 更新ERROR_KNOWLEDGE_BASE.md → 新增对应校验项到validate_system.sh → 修复问题 → 运行./validate_system.sh → 全部通过后提交
```

---

## 📌 八、详细错误解决方案索引

| 错误 | 详细记录位置 |
|------|-------------|
| Git推送404 | `recent_memory/decision/xxx_Git推送404错误.md` |
| HTML模板替换错误 | `recent_memory/decision/xxx_模板替换错误.md` |
| 列表页cp覆盖错误 | `recent_memory/decision/xxx_列表页覆盖错误.md` |
| 重复报告清理错误 | `recent_memory/decision/xxx_版本清理错误.md` |
| 导航栏统一错误 | `recent_memory/decision/xxx_导航栏统一错误.md` |
| Markdown渲染错误 | `recent_memory/decision/20260531_report_converter表格渲染修复.md` |
| 报告卡片样式不统一 | `recent_memory/decision/20260601_报告卡片样式不统一问题修复.md` |
| 重复报告卡片 | `recent_memory/decision/20260601_重复报告卡片问题修复.md` |
| 导航栏CSS不统一 | `recent_memory/decision/20260603_导航栏CSS彻底统一.md` |
| 新报告CSS缺失 | `recent_memory/decision/20260603_新报告导航栏CSS缺失问题修复.md` |
| 悬浮按钮格式不统一 | `recent_memory/decision/20260603_悬浮按钮格式标准化.md` |
| 目录混淆覆盖问题 | `recent_memory/decision/20260603_目录混淆问题彻底修复.md` |
| 首页链接404问题 | `recent_memory/decision/20260603_首页链接404问题修复.md` |
| weekly_preview冗余目录问题 | `recent_memory/decision/20260603_冗余目录问题终极解决.md` |

---

## 📌 九、deep-research-simple 技能使用规范【2026-06-03新增】

### 1. 标准工作流程
```
1. skill_load 加载 deep-research-simple
2. 获取当前日期，创建任务相关目录
3. 第一轮搜索：宽泛搜索，获取整体概览
4. 整理第一轮证据写入 *_evidence.md
5. 第二轮搜索：补充细节，针对缺口定向搜索
6. 整理第二轮证据，继续追加到证据库
7. 第三轮搜索：技术细节、成本结构、良率瓶颈等
8. 撰写完整Markdown深度研究报告
9. Python markdown库转换为专业HTML报告
10. 验证文件完整性后提交
```

### 2. 工具使用坑点
| 坑点 | 现象 | 解决方案 |
|------|------|---------|
| edit_file写回失败 | 追加大段内容时报错"写回文件失败" | 改用 write_file 完全覆盖写入 |
| Python markdown转换表格 | 默认不支持表格渲染 | 使用 `markdown.markdown(content, extensions=['tables'])` |
| 搜索结果过大 | search_web返回超过100KB | 保存到临时文件，只提取关键证据 |

### 3. 深度研究报告结构标准
```
执行摘要 → 技术路线深度分析 → 产业链全景图谱 → 核心玩家梳理
→ 市场空间测算 → 催化因素分析 → 风险因素 → 投资机会图谱
→ 重点公司深度 → 结论与展望
```

### 4. 证据块标准格式
```
Claim: [核心论断]
Source: [来源名称]
URL: [完整链接]
Date: [YYYY-MM-DD]
Excerpt: [原文摘录]
Context: [上下文说明]
Confidence: [HIGH/MEDIUM/LOW]
```
