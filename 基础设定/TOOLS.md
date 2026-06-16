# 工具使用指南（精简版）

## ⚠️ 数据验证铁律
**任何数据必须反复验证后才能写入报告，绝对不能凭记忆或未经核实直接引用！**

## 📋 核心检查清单（每日工作必看）
1. **价格数据**：必须查当日收盘价，禁止使用历史数据
2. **目录检查**：先`ls docs/`确认，禁止创建"催化日历"目录
3. **列表页保护**：`latest.html`>3KB，**绝对禁止覆盖整个文件**
4. **列表页更新**：读取→插入新卡片→原"最新"改普通标签
5. **导航栏**：玻璃态+11按钮+统一"周三前瞻"
6. **提交前**：必须运行`./validate_system.sh`
7. **持仓限制**：共4个（英维克、铜冠铜箔、雅克科技、*ST建艺）
8. **文件修改**：仅改目标部分，严禁全文件替换
9. **白卡白字**：检查所有style标签，注意后面覆盖前面
10. **指数数据**：必须区分指数/股票类型，000001既是上证指数也是平安银行

> **详细规范**：详见 `recent_memory/decision/` 目录下的完整文档

---

## 🏗️ 系统架构速查

### 工作目录
- **Git仓库**：`/root/daily-news-insight/`
- **工作目录**：`/app/data/所有对话/主对话/docs/`

### 目录规范
- 周三前瞻→`weekly_outlook/`，周复盘→`weekly_review/`
- "催化日历"已永久删除：S级催化→`s级催化扫描/`，明日催化→`明日催化剂/`
- 报告类→`latest.html`，工具类→`index.html`

### 核心脚本
- **simple_push.py**：企业微信推送
- **update_all_lists.py**：列表页更新
- **report_converter/generate_report.py**：专业报告生成系统
- **scripts/daily_update.py**：每日数据自动更新（15:30+17:00两次）
- **v3/generators/pro_base.py**：Pro生成器基类

### V3.5 Pro架构
- 基类统一提供：导航栏、悬浮按钮、TOC、深色玻璃态
- 已Pro化：13个工具页面 + 7个报告（全部集成daily_update.py）
- 整体进度：约95%，全流程验证通过
- 特殊生成器：PortfolioDashboardProGenerator（独立实现）、TimeMachinePage（继承ProPage）

---

## 🚨 三大绝对禁令
1. **禁止覆盖**：`latest.html`、首页`index.html` 禁止全量覆盖
2. **禁止自制模板**：必须用Pro生成器或复制标准模板
3. **禁止假数据**：价格数据必须查当日真实数据

---

## 🐛 常见问题速查

### 白卡白字
- 原因：底部`.card-glass`白色背景覆盖头部深色样式
- 解决：用Pro生成器统一生成，或检查style标签CSS优先级

### 列表页覆盖
- 铁律：报告输出`YYYYMMDD_报告名.html`，列表页由独立脚本维护，**禁止直接写latest.html**
- 视觉区分：列表页需与报告页有明显视觉差异，避免用户混淆
  - 列表页title加「· 报告列表」后缀
  - 列表页顶部加「📂 报告归档」标识
  - 列表页显示报告总数+「按时间倒序」说明
- list_page_pro.py的ListPageProGenerator继承自ProGenerator基类

### 指数数据错误
- 原因：指数/股票代码重叠（如000001）
- 解决：`_detect_prefix`必须传`type_`参数区分类型

### 百分比转float错误
- 解决：`float(pct_str.replace('%', ''))`
- 相关：持仓仪表盘压力测试

### publish返回格式
- 标准：`{success: bool, file_size: int, error: str, output_path: str}`
- 注意：PortfolioDashboardProGenerator曾返回字符串，需判断类型

### Pro报告必须先build再render
- 原因：子类内容由build方法填充，直接render是空页面
- 顺序：实例化 → `build_standard_report()` → `render()`/`publish()`

### Pro生成器self.data_dir缺失
- 问题：`_load_data()`依赖`self.data_dir`，但基类不保存该属性
- 表现：topics为空，核心题材等模块不显示
- 修复：子类`__init__`中`super()`前加 `self.data_dir = data_dir`
- 影响：daily_pro.py、aftermarket_pro.py等自定义load_data的生成器

### Tab切换组件
- 旧版：重要新闻汇总8个分类tab（政策、宏观、市场、行业、公司、科技、金融、周期）
- Pro版：核心题材按级别分3个tab（S/A/B级题材）、重要新闻汇总8个分类tab（2026-06-16补回）
- 注意：用户说的"tap按钮"即tab标签切换按钮，用户发音/输入习惯问题
- 实现方式：news-tabs-container + news-tab-btn + news-tab-panel 类名 + switchNewsTab JS函数
- 位置：daily_pro.py 的 add_important_news() 方法



### Git合并冲突
- 禁止`git merge -X theirs`，会残留冲突标记
- 优先手动解决，或`git reset --hard origin/main`回退

---

## 📊 数据层要点
- 双数据源同步：`data/`（本地）↔ `docs/data/`（部署）
- 字段兼容：price/current_price、change_pct/today_change、sectors_hot/hot_sectors
- 校验规则：上证指数3000-5000点区间，异常值需二次验证

## Pro生成器使用注意
独立实现的生成器方法签名不统一：PortfolioDashboardProGenerator入参为data_path，用generate()生成内容；HomePageProGenerator用render()生成内容。调用前必须先grep查询公开方法，避免硬编码错误。