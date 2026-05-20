# MEMORY.md - 核心知识库

## 系统架构规范（2026-05-20制定，详见TOOLS.md）

### 核心规则
- **工作目录**：`docs/`（唯一正确路径）
- **Git仓库**：`~/daily-news-insight-git/docs/`
- **命名规范**：`YYYYMMDD_类型.html`（日期在前，类型在后）
- **MD必须保留**：每份日报同时保存.md和.html
- **删除前必备份**：任何删除操作前先备份

### 禁止操作
- ❌ 删除目录前未列出内容
- ❌ 删除目录前未备份
- ❌ 在旧目录操作
- ❌ MD源文件只保存一份

### 内容页UI规范（2026-05-20制定）

**模板位置**：`docs/_templates/内容页标准模板.md`

#### 导航栏结构（必须）
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
**注意**：当前页添加 `class="current"`

#### 响应式表格（必须）
```html
<div style="overflow-x: auto;">
    <table class="data-table" style="min-width: 600px;">
        ...
    </table>
</div>
```

#### 禁止使用的旧样式
- ❌ `class="nav"` 老式导航
- ❌ 表格外层无 `overflow-x: auto`

## 用户持仓标的

| 标的 | 代码 | 成本 | 目标价 | 止损 |
|------|------|------|--------|------|
| 英维克 | 002837 | 103.81元 | 110-115 | 95元 |

**操作建议**：持有/逢低加仓

## 核心日程

| 任务 | 时间 |
|------|------|
| 每日新闻洞察 | 8:30 |
| 盘中快报 | 12:30 |
| S级催化扫描 | 16:30 |
| 盘后速递 | 20:30 |
| 周复盘 | 周六9:00 |
| 英伟达Q1财报 | 5月21日04:20 |

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

## 页面归属规范（2026-05-20更新）

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

## 推理模型

| IMPS强度 | 预期涨幅 |
|----------|----------|
| I-5 | +50-200% |
| I-4 | +25-100% |
| I-3 | +15-50% |
| I-2 | +8-25% |
| I-1 | +3-15% |

**关键规则**：T+0不追脉冲、T+3~T+5龙头生死窗口、二板定龙头、不买3-4板中位股

## 访问地址

- **GitHub Pages**：https://boya357.github.io/daily-news-insight/
- **产业链总览**：https://boya357.github.io/daily-news-insight/industry_chain/latest.html
- **前瞻催化**：https://boya357.github.io/daily-news-insight/weekly_review/latest.html
