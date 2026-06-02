# TOOLS.md - 工具使用经验与坑点记录

> **核心原则**：快速参考，详细记录见 `recent_memory/decision/`

---

## 📌 一、报告生成核心规范

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

## 📌 六、详细错误解决方案索引

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
