# 系统架构规范文档 v1.0

**生效日期：** 2026年6月3日
**目的：** 彻底解决模块边界混乱、文件放错目录等问题，从源头上杜绝低级错误

---

## 一、目录结构与模块分类

### 1.1 两大模块核心原则

| 模块类型 | 命名规范 | 写入规则 | 可写入主体 |
|---------|---------|---------|-----------|
| **报告类模块** | `latest.html` = 列表页，单篇报告不允许写这个文件 | `YYYYMMDD_报告名称.html` | 生成报告的脚本/日程 |
| **工具类模块** | `index.html` = 工具入口 | 只有专门的更新脚本可以写 | 工具更新程序 |

### 1.2 16个目录完整分类

```
docs/
├── 报告类（11个，latest.html = 列表页）
│   ├── daily/              # 每日新闻洞察
│   ├── intraday/           # 盘中速递
│   ├── aftermarket/        # 盘后速递
│   ├── weekly_review/      # 周复盘
│   ├── weekly_outlook/     # 周前瞻
│   ├── monthly/            # 月报
│   ├── industry_chain/     # 产业链深度研究
│   ├── s级催化扫描/        # S级催化扫描 ⚠️ 不是"催化日历"
│   ├── 催化日历/           # ⚠️ 已废弃，彻底删除
│   ├── 周末速递/           # 周末速递
│   └── 明日催化剂/         # 明日催化剂
│
└── 工具类（5个，index.html = 工具入口）
    ├── 产业链时钟/         # 产业链时钟
    ├── 智能预警系统/       # 智能预警系统
    ├── 持仓智能预警仪表盘/ # 持仓智能预警仪表盘
    ├── 智能选题助手/       # 智能选题助手
    └── 预判验证/           # 预判验证
```

---

## 二、各模块正确目录映射表

| 日程/任务类型 | 正确目录 | 禁止写入的目录 | 文件名规范 |
|-------------|---------|---------------|-----------|
| 每日新闻洞察 | `docs/daily/` | 其他任何目录 | `YYYYMMDD.html` |
| 盘中速递 | `docs/intraday/` | 其他任何目录 | `YYYYMMDD_盘中速递.html` |
| 盘后速递 | `docs/aftermarket/` | 其他任何目录 | `YYYYMMDD_盘后速递.html` |
| 周复盘 | `docs/weekly_review/` | 其他任何目录 | `YYYYMMDD_周复盘.html` |
| 周前瞻 | `docs/weekly_outlook/` | 其他任何目录 | `YYYYMMDD_周前瞻.html` |
| 月报 | `docs/monthly/` | 其他任何目录 | `YYYYMMDD_月报.html` |
| 产业链深度报告 | `docs/industry_chain/` | 其他任何目录 | `YYYYMMDD_主题名称.html` |
| **S级催化扫描** | **`docs/s级催化扫描/`** | **❌ 绝对不能写 `催化日历/`** | `YYYYMMDD_盘前/盘后_S级催化扫描.html` |
| 周末速递 | `docs/周末速递/` | 其他任何目录 | `YYYYMMDD_周末速递.html` |
| 明日催化剂 | `docs/明日催化剂/` | 其他任何目录 | `YYYYMMDD_明日催化剂.html` |

---

## 三、强制检查清单（生成前必须逐项确认）

### 3.1 目录检查（3项）
- [ ] 我要写入的目录是否在上面的映射表中存在？
- [ ] 我要写入的目录是否与报告类型一一对应？
- [ ] 我绝对没有写错误目录（如S级催化 → 催化日历）？

### 3.2 文件命名检查（2项）
- [ ] 文件名是否符合 `YYYYMMDD_主题名称.html` 格式？
- [ ] 文件名没有使用中文拼音缩写？

### 3.3 列表页保护检查（3项）
- [ ] 我没有直接写 `latest.html`？
- [ ] 只有专门的更新列表脚本才能写 `latest.html`？
- [ ] 生成报告时只写单篇报告文件？

### 3.4 内容完整性检查（2项）
- [ ] 报告是否有完整的6个章节（如果是深度报告）？
- [ ] 导航栏是否是标准玻璃态样式（11个按钮，紫色渐变背景）？

---

## 四、错误案例库

### 错误案例 #1：S级催化扫描放错目录
**错误：** 把S级催化扫描报告写入了 `docs/催化日历/` 目录
**正确：** 应该写入 `docs/s级催化扫描/` 目录
**根本原因：** 历史遗留名称与当前实际目录不匹配
**预防措施：** 所有日程任务的description中必须明确写明正确目录路径

### 错误案例 #2：英伟达报告内容被人形机器人覆盖
**错误：** 为了修导航栏，直接复制了整个人形机器人报告文件，导致内容覆盖
**正确：** 只修改导航栏相关的代码部分，绝不整个文件替换
**根本原因：** 偷懒走捷径
**预防措施：** 修改单个文件时，必须使用sed或edit_file精确替换目标部分

### 错误案例 #3：周复盘列表页被单篇报告覆盖
**错误：** Skill生成时直接写 `latest.html`，把列表页变成了单篇报告
**正确：** 生成报告时只写 `YYYYMMDD_xxx.html`，列表页由专门脚本更新
**根本原因：** 模块边界混乱，报告类脚本越权写列表页
**预防措施：** 所有生成报告的脚本严禁写入 `latest.html`

### 错误案例 #4：导航栏样式不统一
**错误：** 不同时期的报告使用了不同的导航栏样式（旧版MLCC vs 玻璃态）
**正确：** 所有报告必须使用完全相同的标准玻璃态导航栏
**根本原因：** 没有建立标准模板库
**预防措施：** 建立标准导航栏模板，所有新报告直接复制使用

---

## 五、标准玻璃态导航栏模板（必须100%一致）

```html
<nav class="fixed top-0 left-0 right-0 z-50 glass-nav">
    <div class="max-w-5xl mx-auto px-4 py-3 flex items-center justify-between">
        <div class="flex items-center space-x-3">
            <div class="w-8 h-8 rounded-lg bg-gradient-to-br from-indigo-500 to-purple-600 flex items-center justify-center">
                <span class="text-white text-sm font-bold">📊</span>
            </div>
            <span class="text-white font-bold text-lg">投资研究中心</span>
        </div>
        <div class="flex items-center space-x-1 flex-wrap gap-1">
            <a href="/daily-news-insight/index.html" class="text-white/80 hover:text-white hover:bg-white/10 text-sm transition-colors px-3 py-1.5 rounded-lg">首页</a>
            <a href="/daily-news-insight/daily/latest.html" class="text-white/80 hover:text-white hover:bg-white/10 text-sm transition-colors px-3 py-1.5 rounded-lg">日报</a>
            <a href="/daily-news-insight/intraday/latest.html" class="text-white/80 hover:text-white hover:bg-white/10 text-sm transition-colors px-3 py-1.5 rounded-lg">盘中</a>
            <a href="/daily-news-insight/aftermarket/latest.html" class="text-white/80 hover:text-white hover:bg-white/10 text-sm transition-colors px-3 py-1.5 rounded-lg">盘后</a>
            <a href="/daily-news-insight/industry_chain/latest.html" class="text-white/80 hover:text-white hover:bg-white/10 text-sm transition-colors px-3 py-1.5 rounded-lg">产业链</a>
            <a href="/daily-news-insight/weekly_review/latest.html" class="text-white/80 hover:text-white hover:bg-white/10 text-sm transition-colors px-3 py-1.5 rounded-lg">周复盘</a>
            <a href="/daily-news-insight/weekly_outlook/latest.html" class="text-white/80 hover:text-white hover:bg-white/10 text-sm transition-colors px-3 py-1.5 rounded-lg">周三前瞻</a>
            <a href="/daily-news-insight/周末速递/latest.html" class="text-white/80 hover:text-white hover:bg-white/10 text-sm transition-colors px-3 py-1.5 rounded-lg">周末速递</a>
            <a href="/daily-news-insight/明日催化剂/latest.html" class="text-white/80 hover:text-white hover:bg-white/10 text-sm transition-colors px-3 py-1.5 rounded-lg">明日催化</a>
            <a href="/daily-news-insight/s级催化扫描/latest.html" class="text-white/80 hover:text-white hover:bg-white/10 text-sm transition-colors px-3 py-1.5 rounded-lg">S级催化</a>
            <a href="/daily-news-insight/monthly/latest.html" class="text-white/80 hover:text-white hover:bg-white/10 text-sm transition-colors px-3 py-1.5 rounded-lg">月报</a>
        </div>
    </div>
</nav>
```

---

## 六、7天稳定观察期执行计划（2026.06.04 - 2026.06.10）

### 每日执行清单
1. ✅ 所有日程任务执行前，先对照本规范检查目录路径
2. ✅ 每日结束时，运行目录一致性检查脚本
3. ✅ 发现任何目录错误立即修复并记录到错误案例库
4. ✅ 每天结束时提交一份《系统稳定性报告》

### 观察期目标
- 0个目录放错错误
- 0个列表页被覆盖错误
- 0个导航栏样式不统一错误

---

## 七、模板+数据分离架构（v2.0 新增）

### 7.1 核心设计思想

**问题根源：** 此前所有列表页都由人工手动编辑HTML，容易出现：
- 手动复制粘贴时漏掉部分内容
- 手动修改时不小心破坏页面布局
- 每次新增报告都需要手动编辑列表页
- 不同时期的页面样式不统一

**解决方案：** 所有页面采用 **"固定HTML模板 + 脚本自动填充数据"** 架构

```
┌─────────────────────────────────────────────────┐
│              固定HTML模板（永远不变）            │
│  ┌─────────────────────────────────────────┐  │
│  │  • 导航栏（11个标准按钮                │  │
│  │  • 页面布局（网格/卡片样式）          │  │
│  │  • CSS样式（玻璃态、紫色渐变）         │  │
│  │  • 页脚文字                            │  │
│  └─────────────────────────────────────────┘  │
│                     ↓                         │
│         Python脚本自动扫描目录              │
│           • 扫描所有报告文件                │
│           • 按时间倒序排序                 │
│           • 生成报告卡片HTML              │
│                     ↓                         │
│         插入到模板中 → 生成最终HTML         │
└─────────────────────────────────────────────────┘
```

### 7.2 所有页面脚本清单（共11个）

| 页面 | 脚本文件 | 功能 |
|------|---------|------|
| 每日新闻洞察列表页 | `update_daily_list.py` | 扫描docs/daily/下所有报告 |
| 盘中快报列表页 | `update_intraday_list.py` | 扫描docs/intraday/下所有报告 |
| 盘后速递列表页 | `update_aftermarket_list.py` | 扫描docs/aftermarket/下所有报告 |
| 产业链总览列表页 | `update_industry_chain_list.py` | 扫描docs/industry_chain/下所有报告 |
| 周复盘列表页 | `update_weekly_review_list.py` | 扫描docs/weekly_review/下所有报告 |
| 周三前瞻列表页 | `update_weekly_outlook_list.py` | 扫描docs/weekly_outlook/下所有报告 |
| 周末速递列表页 | `update_weekend_express_list.py` | 扫描docs/周末速递/下所有报告 |
| 明日催化剂列表页 | `update_tomorrow_catalyst_list.py` | 扫描docs/明日催化剂/下所有报告 |
| S级催化扫描列表页 | `update_slevel_catalyst_list.py` | 扫描docs/s级催化扫描/下所有报告 |
| 月报列表页 | `update_monthly_list.py` | 扫描docs/monthly/下所有报告 |
| 首页最新发布模块 | `update_index.py` | 扫描所有模块的最新报告 |

### 7.3 统一执行脚本

```bash
# 一键更新所有页面（推荐）
python3 update_all_lists.py

# 单独更新某个页面
python3 update_daily_list.py
python3 update_intraday_list.py
...
```

### 7.4 强制规范

1. ✅ **绝对禁止** 手动编辑任何 `latest.html` 文件**
2. ✅ **绝对禁止** 手动编辑 `index.html` 首页**
3. ✅ 所有列表页更新 **必须** 通过脚本完成**
4. ✅ 所有新报告生成后，只需运行脚本自动更新列表**
5. ✅ 如需调整页面样式时，**只修改脚本中的PAGE_TEMPLATE**，然后重新运行脚本

---

**文档版本：** v2.0
**最后更新：** 2026.06.04
**维护人：** boya
