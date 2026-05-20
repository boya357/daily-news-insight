# MEMORY.md - 核心知识库

## 报告命名规范（2026-05-20最终版）

| 报告类型 | 格式 | 示例 |
|---------|------|------|
| 每日新闻洞察 | `YYYYMMDD_每日新闻洞察.html` | `20260520_每日新闻洞察.html` |
| 盘中快报 | `YYYYMMDD_盘中快报.html` | `20260520_盘中快报.html` |
| 盘后速递 | `YYYYMMDD_盘后速递.html` | `20260520_盘后速递.html` |
| 周三前瞻 | `YYYYMMDD_周三前瞻.html` | `20260521_周三前瞻.html` |
| 周末前瞻 | `YYYYMMDD_周末前瞻.html` | `20260525_周末前瞻.html` |
| 周复盘 | `YYYYMMDD_周复盘.html` | `20260517_周复盘.html` |
| S级催化扫描 | `YYYYMMDD_S级催化扫描.html` | `20260518_S级催化扫描.html` |
| 产业链日报 | `YYYYMMDD_产业链名日报.html` | `20260520_存储产业链日报.html` |

**⚠️ 注意**：
- 日期在前，类型在后
- 产业链日报只放在 `docs/reports/产业链名/` 目录
- weekly_review目录不放产业链日报

### UI设计规范（2026-05-20用户确认）

**两种风格**：
| 页面类型 | 风格 | 示例 |
|---------|------|------|
| 列表页（latest.html） | 简洁卡片式 | 浅色背景 + 白色卡片 + 毛玻璃导航栏 |
| 内容页 | **沉浸光影风格** | 紫色渐变背景 + 大图标 + 脉冲动画 |

**沉浸光影UI特征**（参考 `docs/daily/20260518.html`）：
- 紫色渐变背景：`linear-gradient(135deg, #667eea 0%, #764ba2 100%)`
- 大图标+脉冲动画：`animation: pulse 3s ease-in-out infinite`
- 深阴影：`box-shadow: 0 15px 40px rgba(118, 75, 162, 0.35)`
- 渐变文字标题：`-webkit-background-clip: text`
- 导航栏毛玻璃效果：`backdrop-filter: blur(20px)`

**⚠️ HTML响应式必须项**：
- 表格：`.card-body { overflow-x: auto; }` + `min-width: 500px`
- 列表：统一`padding-left: 20px` + `line-height`
- 网格：`minmax(150px, 1fr)` 更紧凑
- 移动端：添加`@media`适配

### 推送规范（2026-05-20用户确认）

**所有推送都是精简版：news卡片 + 只发链接，不生成摘要**

| 报告类型 | 网站UI | 推送内容 |
|---------|--------|---------|
| 每日新闻洞察 | 沉浸光影 | 精简版，只发链接 |
| 盘中快报 | 沉浸光影 | 精简版，只发链接 |
| 盘后速递 | 沉浸光影 | 精简版，只发链接 |
| 新工具页面 | 沉浸光影 | 不推送 |

**网站所有页面统一UI**：
- ✅ 内容页：沉浸光影风格（紫色渐变 + header + nav-bar）
- ✅ 列表页：简洁卡片式
- ✅ 新工具页：全用沉浸光影风格

### 禁止操作
- ❌ 删除目录前未列出内容
- ❌ 删除目录前未备份
- ❌ 在旧目录操作
- ❌ 写文件到Git仓库时用相对路径（必须用`~/daily-news-insight-git/...`完整路径）
- ❌ HTML表格不加响应式处理（必须`overflow-x: auto`）
- ❌ 产业链日报放错目录（应放在 `reports/产业链名/`，不是 `weekly_review/`）
- ❌ 命名不规范（必须用 `YYYYMMDD_类型.html` 格式）

## 用户持仓标的

| 标的 | 代码 | 成本 | 目标价 | 止损 |
|------|------|------|--------|------|
| 英维克 | 002837 | 103.81元 | 110-115 | 95元 |

**操作建议**：持有/逢低加仓

## 核心日程（2026-05-20更新）

| 任务 | 时间 | 触发方式 | UI规范 |
|------|------|----------|--------|
| 每日新闻洞察 | 08:30 | 自动（日历） | 沉浸光影 |
| 盘中快报 | 12:30 | 自动（日历） | 沉浸光影 |
| 盘后速递 | 20:30（工作日） | 自动（日历） | 沉浸光影 |
| S级催化扫描 | 16:30 | 自动（S级事件触发） | 沉浸光影 |
| 产业链日报 | - | **手动触发** | - |
| 周复盘 | 每周六09:00 | 自动（日历） | 沉浸光影 |
| 周三前瞻汇总 | 每周三20:00 | 自动（日历） | 沉浸光影 |
| 月度报告 | 每月1日09:00 | 自动（日历） | 沉浸光影 |

### 定时任务UID（用于查询和修改）
- 每日新闻洞察：`11dc83c5-2874-4419-92d0-27ecc9cc87f9`
- 盘中快报：`b0e48f06-9c3f-4040-9b03-8b23c30331a9`
- 盘后速递：`0e2ff3d7-e147-49ed-9343-4a7d0bf7f555`
- 周复盘：`5d210aaa-38ec-45c9-8b1a-317cf5af0d15`
- 周三前瞻：`6798d85d-1686-4544-b297-db934f2488ff`
- 月度报告：`c65e2531-455a-4310-a3ad-1b58371dd074`

### 重要日程节点
- 英伟达Q1财报：5月21日04:20（明日凌晨）

## 系统架构已稳定（2026-05-20确认）
- ✅ 命名规范确定
- ✅ 目录结构确定  
- ✅ Git同步流程确定
- ✅ 新UI设计规范确定
- ✅ 深度广度标准确定

## 下一步改进方向（2026-05-20用户确认）
1. **报告质量提升**：深度广度、实用度
2. **数据可靠性提升**：建立数据源库和验证流程
3. **报告缺失补全**：周复盘、盘后速递等

## 英伟达产业链核心标的

| 梯队 | 标的 | 代码 |
|------|------|------|
| 🔴超弹性 | 铂科新材 | 300811 |
| 🔴超弹性 | 工业富联 | 601138 |
| 🔴超弹性 | 中际旭创 | 300308 |
| 🟠高确定性 | 天孚通信 | 300394 |
| 🟠高确定性 | 胜宏科技 | 300476 |
| 🟠高确定性 | 沪电股份 | 002463 |

## 存储产业链（2026-05-20 S级催化）

**双雄**：长鑫科技（Q1净利+1688%）+ 长江存储（IPO辅导中，估值3000亿）

**核心标的**：
- 兆易创新(603986)、万润科技(002654)
- 深科技(000021)、中微公司(688012)
- 北方华创(002371)、华海清科(688120)

## 今日S级催化扫描（2026-05-20 16:30）

| 产业链 | IMPS | 核心催化 |
|--------|------|----------|
| 存储芯片 | 20+ | 长江存储IPO + 长鑫Q1净利+1688% |
| 人形机器人 | 18 | 上海10万台进工厂 + 三雄IPO |
| CPO/光器件 | 15-16 | 格罗方德SCALE CPO方案 |

**已生成日报**：
- `docs/reports/存储产业链/20260520_存储产业链日报.html`
- `docs/reports/具身智能日报/20260520_具身智能产业链日报.html`
- `docs/reports/CPO产业链/20260520_CPO光通信产业链日报.html`

## 推理模型

| IMPS强度 | 预期涨幅 |
|----------|----------|
| I-5 | +50-200% |
| I-4 | +25-100% |
| I-3 | +15-50% |
| I-2 | +8-25% |
| I-1 | +3-15% |

**关键规则**：T+0不追脉冲、T+3~T+5龙头生死窗口、二板定龙头、不买3-4板中位股

## 目录结构（2026-05-20最终版）

```
docs/
├── daily/                    # 每日新闻洞察
│   ├── 20260520_每日新闻洞察.html
│   └── latest.html
├── intraday/                 # 盘中快报
│   ├── 20260520_盘中快报.html
│   └── latest.html
├── aftermarket/              # 盘后速递
│   ├── 20260520_盘后速递.html
│   └── latest.html
├── s级催化扫描/               # 明日催化剂
│   ├── 20260521_S级催化扫描.html
│   └── latest.html
├── weekly_review/             # 前瞻催化（导航名：前瞻催化）
│   ├── 20260521_周三前瞻.html    # 周三20:00发
│   ├── 20260525_周末前瞻.html    # 周日20:00发
│   ├── 20260517_周复盘.html      # 周六09:00发
│   ├── 20260518_S级催化扫描.html
│   └── latest.html              # 统一列表页
├── industry_chain/            # 产业链总览（导航名：产业链）
│   └── latest.html
├── reports/                   # 各产业链日报
│   ├── 存储产业链/
│   │   └── 20260520_存储产业链日报.html
│   ├── CPO产业链/
│   ├── 具身智能日报/
│   └── ...其他产业链
├── monthly/                   # 月度报告
│   └── latest.html
└── 系统架构规范文档.md
```

**目录用途说明**：
- `weekly_review/`：只放前瞻催化相关（周三前瞻、周末前瞻、周复盘、S级催化扫描）
- `reports/`：只放各产业链日报
- `industry_chain/`：产业链总览入口页

## 页面归属规范

| 报告类型 | 触发方式 | 存放页面 |
|----------|----------|----------|
| 产业链日报 | **手动触发**，用户提出需求才生成 | 产业链总览 |
| S级催化扫描日报 | 自动生成（S级催化触发） | **前瞻催化页面** |
| 每日新闻洞察 | 自动生成 | 每日新闻洞察页面 |

**S级催化扫描日报内容要求**：
- 包含利空催化 + 利多催化（不能只有利好）
- 每个催化：来源+影响机制+核心标的(≥5只)+逻辑推理+预判+风险
- 产业链全景图（上中下游）
- 核心标的表格（含代码、评级、逻辑）
- 盘面回顾数据 + 明确的操作建议

**配色要求**：浅色清新（避免深色）
- 背景：`#f8fafc` 或 `#fefefe`
- 卡片背景：`#ffffff`

## 企业微信推送规范（2026-05-20简化版）

**推送脚本**：`~/daily-news-insight-git/src/simple_push.py`

**使用方法**：
```bash
python3 ~/daily-news-insight-git/src/simple_push.py "标题" "链接"
```

**推送类型**：news卡片，只推送链接，不生成摘要（省积分）

**各报告推送命令**：
| 报告类型 | 推送命令 |
|---------|---------|
| 每日新闻洞察 | `simple_push.py "每日新闻洞察" "https://boya357.github.io/daily-news-insight/daily/latest.html"` |
| 盘中快报 | `simple_push.py "盘中快报" "https://boya357.github.io/daily-news-insight/intraday/latest.html"` |
| 盘后速递 | `simple_push.py "盘后速递" "https://boya357.github.io/daily-news-insight/aftermarket/latest.html"` |
| S级催化扫描 | `simple_push.py "明日催化剂" "https://boya357.github.io/daily-news-insight/s级催化扫描/latest.html"` |
| 周三前瞻 | `simple_push.py "周三前瞻" "https://boya357.github.io/daily-news-insight/weekly_review/latest.html"` |
| 周复盘 | `simple_push.py "周复盘" "https://boya357.github.io/daily-news-insight/weekly_review/latest.html"` |
| 月度报告 | `simple_push.py "月度报告" "https://boya357.github.io/daily-news-insight/monthly/latest.html"` |

## 内容页标准规范（2026-05-20制定）

**模板位置**：`docs/_templates/内容页标准模板.md`

### 导航栏结构（必须）

```html
<header class="header">
    <div class="header-inner">
        <a href="/daily-news-insight/" style="text-decoration: none;">
            <span class="header-title">📊 市场洞察中心</span>
        </a>
    </div>
</header>
<div class="nav-bar">
    <a href="/daily-news-insight/" class="nav-item">首页</a>
    <a href="/daily-news-insight/daily/latest.html" class="nav-item">每日新闻洞察</a>
    <a href="/daily-news-insight/intraday/latest.html" class="nav-item">盘中快报</a>
    <a href="/daily-news-insight/aftermarket/latest.html" class="nav-item">盘后速递</a>
    <a href="/daily-news-insight/industry_chain/latest.html" class="nav-item">产业链</a>
    <a href="/daily-news-insight/weekly_review/latest.html" class="nav-item current">前瞻催化</a>
</div>
```

**关键规则**：
- 6项导航固定不变
- 当前页添加 `class="nav-item current"`
- 导航名：前瞻催化（不是周复盘）

### 响应式表格（必须）

```html
<div style="overflow-x: auto;">
    <table class="data-table" style="min-width: 600px;">
        ...
    </table>
</div>
```

### 禁止使用的旧样式
- ❌ `class="nav"` 老式导航栏
- ❌ 表格外层无 `overflow-x: auto`
- ❌ 导航项写成"周复盘"（应统一叫"前瞻催化"）

---

## Git submodule问题总结（2026-05-20）

**问题原因**：
1. repo_temp 被错误添加为 git submodule（mode 160000）
2. 没有配置 .gitmodules 文件
3. 导致 GitHub Pages 构建失败

**修复过程**：
1. 移除 submodule 引用
2. 删除 submodule 目录

**损失**：
- ❌ 4月23日-5月14日的每日新闻洞察日报MD文件（共22个）
- ❌ 英伟达Q1财报超预期A股受益标的专题报告

**教训**：
- 避免使用 git submodule
- 删除目录前必须列出内容并备份
- MD源文件必须和HTML一起提交到git主仓库

**英伟达报告已恢复**：
- 2026-05-20 重新生成HTML
- 已添加到产业链总览专题报告区域

## 访问地址

- **GitHub Pages**：https://boya357.github.io/daily-news-insight/
- **产业链总览**：https://boya357.github.io/daily-news-insight/industry_chain/latest.html
- **前瞻催化**：https://boya357.github.io/daily-news-insight/weekly_review/latest.html
