# TOOLS.md - 工具使用经验与坑点记录

> **核心原则**：快速参考，详细记录见 `recent_memory/decision/`

---

## 📌 一、核心工作流【最高优先级】

### 1. 标准工作流程
```
生成报告 → 运行脚本更新列表页 → ./validate_system.sh全量校验
    ↓
✅ 15项校验全部通过 → Git提交 → 验证GitHub Pages返回200
❌ 任何一项不通过 → 修复后重新校验
```

### 2. 三大绝对禁令（违反即重罚）
1. ❌ **禁止手动编辑**任何 `latest.html`、禁止cp覆盖
2. ❌ **禁止覆盖整个** `index.html`，首页仅允许增量更新
3. ❌ **禁止自制HTML模板**，必须复制`industry_chain`标准模板

---

## 📌 二、列表页自动化脚本（V2.0，2026-06-04）

### 核心原则
- **零手动编辑**：所有列表页100%通过脚本自动更新
- **布局永久固定**：脚本内置模板，HTML结构永远不变
- **一键更新**：`python update_all_lists.py` 完成全部更新

### 脚本清单（12个）
**核心脚本**：update_all_lists.py（一键更新全部：10个列表页+首页）、update_index.py（首页仅增量更新第一区）

**列表页脚本**：update_daily_list.py、update_intraday_list.py、update_aftermarket_list.py、update_industry_chain_list.py、update_weekly_review_list.py、update_weekly_outlook_list.py、update_weekend_express_list.py、update_tomorrow_catalyst_list.py、update_slevel_catalyst_list.py、update_monthly_list.py

### 首页特殊保护规则
- ✅ **布局完全固定**：5个功能模块+系统工具箱永久保留
- ✅ **增量更新模式**：只更新【第一区】最新发布横幅，其他不动
- ❌ **错误教训**：2026-06-04曾尝试简化首页，已恢复并永久禁止此类操作

---

## 📌 三、核心规范速查

### 1. 报告命名规范
- 格式：`YYYYMMDD_报告类型.html`

### 2. 导航栏规范
- 玻璃态样式 + 11个标准按钮 + 标题"投资研究中心"
- 按钮命名统一："周三前瞻"

### 3. 目录规范
- ❌ 禁止URL带`/docs/`前缀
- ❌ "催化日历"目录已永久删除
- ✅ 正确路径：S级催化→`s级催化扫描/`，明日催化→`明日催化剂/`

### 4. 数据规范
- 价格数据必须用`search_web`查**当日**数据，禁止历史数据
- 数据源优先级：韭研公社 > 财联社 > 东方财富 > 同花顺

### 5. 企业微信推送规范
- 仅推送链接，不生成长篇摘要

---

## 📌 四、核心文档索引

| 文档 | 作用 |
|------|------|
| `validate_system.sh` | 15项全量系统完整性校验 |
| `ERROR_KNOWLEDGE_BASE.md` | 永久错误知识库（v1.2，含8个错误案例） |
| `SYSTEM_ARCHITECTURE.md` | 完整系统架构与规则手册（v2.0） |
| `MEMORY.md` | 核心知识库（v5.0） |
| `USER.md` | 用户核心信息与持仓记录 |

---

## 📌 五、问题处理标准流程

```
发现问题 → 更新ERROR_KNOWLEDGE_BASE.md记录错误
    ↓
新增对应校验项到validate_system.sh
    ↓
修复问题 → 运行./validate_system.sh全量校验
    ↓
✅ 全部通过 → Git提交部署
```

---

## 📌 六、deep-research-simple 技能要点

- **流程**：3轮搜索→证据整理→Markdown报告→HTML转换
- **坑点**：大段写入用write_file，markdown表格需`extensions=['tables']`
- **证据格式**：Claim+Source+URL+Date+Excerpt+Confidence

---

## 📌 七、工具页面更新规则（2026-06-04确认）

### 核心原则
- **不做自动化**：5个工具页面保持手动更新，避免正则匹配破坏布局
- **布局100%固定**：仅允许更新数字和文本内容，禁止任何HTML结构修改
- **更新频率**：
  - 每日更新：持仓仪表盘、预判验证、智能预警系统
  - 每周更新：产业链时钟、智能选题助手

### 更新操作方法
1. 找到对应位置的数字/文本
2. 直接修改，不动任何HTML标签
3. 提交GitHub

---

## 📌 八、脚本修复记录（2026-06-04）

### update_industry_chain_list.py
- **问题**：标题硬编码为"产业链深度报告"，未显示真实产业链名称
- **修复**：从文件名完整提取标题

### update_slevel_catalyst_list.py
- **问题**：标题丢失"盘前"、"盘后"标识
- **修复**：完整提取文件名中信息，保留时间标识

### 重要经验教训
- ⚠️ **删除文件后必须重新运行列表更新脚本**，否则列表中可能仍有已删除文件的链接
- ⚠️ 列表脚本按修改时间排序，最新文件自动置顶

---

> **详细错误案例、完整SOP、历史决策记录**见：`recent_memory/decision/` 目录
