# MEMORY.md - 记忆文件（系统架构总览）

## 核心信息

### GitHub仓库
- repo: boya357/daily-news-insight
- Pages: https://boya357.github.io/daily-news-insight/
- 本地Git目录: ~/daily-news-insight-git/docs/
- 工作目录: docs/（唯一正确路径）

### 持仓
- 英维克(002837): 成本103.81元，关注98元支撑
- 川润股份(002272): 成本20.61元，液冷概念

### 产业链清单
- S级: MLCC、人形机器人、存储芯片、CPO/光器件、铜箔
- A级: 液冷温控(Token工厂/AI Agent/商业航天)
- B级: PCB/氦气/eVTOL/环氧树脂
- C级: AI眼镜/先进封装/算力租赁/算电协同

---

## ⭐ 系统架构规范（2026-05-20最终版）

### 目录结构
```
docs/
├── index.html                    # 首页（市场洞察中心）
├── daily/                        # 每日新闻洞察
│   ├── latest.html               # 报告列表页
│   └── YYYYMMDD_每日新闻洞察.html
├── intraday/                     # 盘中快报
│   ├── latest.html               # 报告列表页
│   └── YYYYMMDD_盘中快报.html
├── aftermarket/                  # 盘后速递
│   ├── latest.html               # 报告列表页
│   └── YYYYMMDD_盘后速递.html
├── industry_chain/               # 产业链总览
│   └── latest.html
├── weekly_review/                # 前瞻催化（S级催化扫描、周复盘、周三前瞻）
│   ├── latest.html
│   ├── YYYYMMDD_S级催化扫描.html
│   └── YYYYMMDD_周复盘.html
└── reports/                      # 产业链深度报告
    ├── 具身智能日报/
    ├── 存储产业链/
    ├── CPO产业链/
    └── 铜箔产业链/
```

### 文件命名规范（强制执行）
| 报告类型 | 命名格式 | 示例 |
|---------|---------|------|
| 每日新闻洞察 | `YYYYMMDD_每日新闻洞察.html` | `20260520_每日新闻洞察.html` |
| 盘中快报 | `YYYYMMDD_盘中快报.html` | `20260520_盘中快报.html` |
| 盘后速递 | `YYYYMMDD_盘后速递.html` | `20260520_盘后速递.html` |
| S级催化扫描 | `YYYYMMDD_S级催化扫描.html` | `20260520_S级催化扫描.html` |
| 周复盘 | `YYYYMMDD_周复盘.html` | `20260517_周复盘.html` |
| 周三前瞻汇总 | `YYYYMMDD_前瞻汇总.html` | `20260521_前瞻汇总.html` |

### UI设计规范（强制执行）

**新UI标准**（参考：`docs/daily/20260518.html`）：
- 背景：`#f8fafc` 或 `linear-gradient(135deg, #f8fafc 0%, #eef1f8 100%)`
- 卡片背景：`#ffffff`
- 图标渐变：`linear-gradient(135deg, #6366f1, #8b5cf6)`
- 导航栏：顶部固定，毛玻璃效果
- 必须包含：导航栏 + 页面标题区 + 分类卡片 + 风险提示框

**禁止**：
- 深色背景（`#1a1a2e`等）
- 简单表格布局
- 无导航栏的单页设计

### 深度广度标准（强制执行）

**S级催化必须包含**：
1. 催化来源（具体出处和日期）
2. 量化数据（市场规模、份额、价格弹性）
3. 竞争格局（龙头/跟随者/替代品对比）
4. A股映射深度（至少5只核心标的，每只有业务关联度+受益逻辑+弹性测算）
5. IMPS强度评估（I-1到I-5）
6. TVRC节奏（催化窗口期、爆发期、消退期）
7. 产业链全景（上中下游）

**A级/B级催化**：
- 至少3只核心标的
- 简要逻辑推导

**必选数据板块**：
- 指数涨跌（A股+美股）
- 板块资金流向
- 外资动向
- 持仓标的跟踪

### 操作流程规范

**生成日报后必须执行**：
1. 生成HTML到对应目录
2. 更新latest.html（在顶部添加新卡片）
3. Git同步：`git add -A && git commit && git push`
4. 企业微信推送

**latest.html卡片格式**：
```html
<a href="/daily-news-insight/daily/YYYYMMDD_每日新闻洞察.html" class="card">
    <div class="card-icon">🆕</div>
    <div class="card-content">
        <div class="card-title">每日新闻洞察 - YYYY年M月D日</div>
        <div class="card-subtitle">报告摘要</div>
    </div>
    <span class="card-tag">今日</span>
    <span class="card-arrow">›</span>
</a>
```

---

## 定时任务清单（2026-05-20最终确认）

### 核心日报任务

| 任务 | 时间 | 频率 | 最新UID | 状态 |
|------|------|------|---------|------|
| 每日新闻洞察 | 08:30 | 每天 | `11dc83c5...split_7641938092990923054` | ✅ 有效 |
| 盘中快报 | 12:30 | 每天 | `b0e48f06...split_7641935137919336713` | ✅ 有效 |
| 盘后速递 | 20:30 | 工作日 | `0e2ff3d7...split_7634797521478451466` | ⚠️ 需确认 |
| S级催化扫描 | 16:30 | 工作日 | `97f8f4e0...split_7639711122316214579` | ✅ 有效 |
| 明日催化剂 | 21:00 | 工作日 | `af53d363...split_7641236004392845606` | ✅ 有效 |

### 周期性报告任务

| 任务 | 时间 | 频率 | 最新UID | 状态 |
|------|------|------|---------|------|
| 周三前瞻汇总 | 周三20:00 | 每周 | `6798d85d...split_7641943634409111846` | ✅ 有效（曾设错已修正） |
| 周复盘推送 | 周六09:00 | 每周 | `5d210aaa...split_7641942696986444082` | ✅ 有效 |
| 月度报告推送 | 每月1日09:00 | 每月 | `c65e2531...split_7641946133396373770` | ✅ 有效 |

### 目录结构规范

```
docs/
├── daily/              # 每日新闻洞察
│   ├── latest.html     # 报告列表页
│   └── YYYYMMDD_每日新闻洞察.html
├── intraday/           # 盘中快报
│   ├── latest.html
│   └── YYYYMMDD_盘中快报.html
├── aftermarket/        # 盘后速递
│   ├── latest.html
│   └── YYYYMMDD_盘后速递.html
├── weekly_review/      # 周复盘 + S级催化扫描
│   ├── latest.html
│   └── YYYYMMDD_周复盘.html
├── weekly_outlook/     # 周三前瞻汇总（新建）
│   ├── latest.html
│   └── YYYYMMDD_前瞻汇总.html
├── monthly/            # 月度报告（新建）
│   ├── latest.html
│   └── YYYYMM_月度报告.html
├── s级催化扫描/        # 明日催化剂扫描
│   ├── latest.html
│   └── YYYYMMDD_S级催化扫描.html
└── reports/            # 产业链深度报告
    ├── 具身智能/
    ├── 存储产业链/
    ├── CPO产业链/
    └── ...
```

### ⚠️ 关键注意
1. **所有UID使用latest_active_uid**：日历查询显示的旧UID已过期，必须使用带`_split_`后缀的最新UID
2. **产业链日报批量任务已停用**：改为主动触发，用户需要时再生成
3. **所有日报任务已更新新UI规范**：必须使用沉浸光影风格

---

## 禁止操作（最高优先级）

1. ❌ 在非docs/目录操作
2. ❌ 删除目录前未备份
3. ❌ 使用旧UI生成日报
4. ❌ 生成日报后不更新latest.html
5. ❌ 修改任务后不验证执行

---

## 新UI模板参考

**文件**：`docs/daily/20260518.html`

**关键样式特征**：
- 浅色渐变背景
- 卡片式布局
- 紫色渐变图标
- 导航栏毛玻璃效果
- 风险提示框

---

## 错误教训记录

- **2026-05-20**: submodule误删导致22个文件丢失
  - 原因：repo_temp被错误配置为submodule
  - 教训：不再使用git submodule
- **2026-05-20**: 每日新闻洞察使用旧UI
  - 原因：任务描述未强调使用新UI模板
  - 教训：所有任务描述已更新新UI规范
- **2026-05-20**: 18号报告未显示在列表页
  - 原因：latest.html更新时遗漏
  - 教训：生成日报后必须检查latest.html
