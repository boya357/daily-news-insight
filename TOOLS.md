# TOOLS.md - 工具使用经验与坑点记录

> **核心原则**：快速参考，详细记录见 `recent_memory/decision/`

---

## 📌 一、核心工作流【最高优先级】

### 1. 标准工作流程
```
生成报告 → 脚本更新列表 → ./validate_system.sh全量校验
    ↓
✅ 15项校验通过 → Git提交 → 验证GitHub Pages返回200
❌ 不通过 → 修复后重新校验
```

### 2. 三大绝对禁令
1. ❌ **禁止手动编辑**任何 `latest.html`、禁止cp覆盖
2. ❌ **禁止覆盖整个** `index.html`，首页仅允许增量更新
3. ❌ **禁止自制HTML模板**，必须复制`industry_chain`标准模板

---

## 📌 二、列表页自动化脚本（V2.0）

### 核心原则
- **零手动编辑**：所有列表页100%脚本自动更新
- **布局永久固定**：脚本内置模板，HTML结构不变
- **一键更新**：`python update_all_lists.py`

### 脚本清单
**核心**：update_all_lists.py、update_index.py（首页增量）
**列表页**：update_*_list.py共10个
**安全防护**：safe_update_latest.py + validate_before_commit.py + fix_navbar_final.py + Git钩子

### 首页保护规则
- ✅ 5个功能模块+系统工具箱永久保留
- ✅ 仅更新【第一区】最新发布横幅
- ❌ 2026-06-04曾尝试简化首页，已恢复并永久禁止

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

## 📌 四、核心文档与流程速查

### 核心文档
- `validate_system.sh`：15项全量系统校验
- `ERROR_KNOWLEDGE_BASE.md`：错误知识库（8个案例）
- `SYSTEM_ARCHITECTURE.md`：系统架构规则（v2.0）

### 问题处理SOP
```
发现问题 → 记录错误 → 新增校验 → 修复
    ↓
✅ validate_system.sh全量通过 → Git提交
```

---

## 📌 五、其他要点速查

### deep-research-simple技能
- 3轮搜索→证据整理→Markdown→HTML转换
- 大段写入用write_file，markdown表格需`extensions=['tables']`

### 工具页面更新规则
- 不做自动化，布局100%固定，仅更新数字和文本
- 每日更新：持仓、预判、预警
- 每周更新：产业链时钟、智能选题

### 脚本修复记录
- 产业链列表脚本：修复标题硬编码
- S级催化列表脚本：修复"盘前/盘后"标识丢失
- 教训：删除文件后必须重跑列表更新脚本

---

## 📌 九、导航栏移动端适配

### 核心要点
- **汉堡按钮**：紫色`#667eea`，`nav-links`容器外同级，电脑端隐藏
- **文字颜色**：统一用`text-gray-700`，hover用`text-gray-900`，白背景禁白字
- **插入顺序**：先插移动端菜单HTML，再插汉堡按钮
- **CSS断点**：移动端768px，需包含完整`@media`查询
- **修复脚本**：`fix_navbar_final.py`，修复后需同步更新模板

---

## 📌 十、行情数据经验速查

### 龙虎榜API（东方财富）
- 接口：`datacenter-web.eastmoney.com/api/data/v1/get`
- 报表：`RPT_DAILYBILLBOARD_PROFILE`（每日概况）、`RPT_ORGANIZATION_TRADE_DETAILSNEW`（机构明细）
- 16:30后更新，参数：`source=WEB&client=WE`

### 指数代码坑点
- 000001双义（上证指数/平安银行），`_detect_prefix`需加`type_`参数区分
- 腾讯财经：上证指数`sh`前缀，深证成指`sz`前缀

---

## 📌 十一、Pro版报告生成器经验

### 核心架构
- **基类体系**：ProGenerator → ReportProGenerator（报告类）、ProPage（页面类）
- **7个报告Pro版**：日报、盘中快报、盘后速递、周复盘、周末速递、S级催化、明日催化
- **统一UI**：深色玻璃态风格，自动继承导航栏/悬浮按钮/TOC

### 使用注意事项
1. **必须先build再render**：ReportProGenerator子类需先调用`build_standard_report()`填充sections，再调用`render()`或`publish()`
2. **特殊生成器**：
   - `PortfolioDashboardProGenerator`：独立实现，不继承ProGenerator，参数为`data_path`
   - `TimeMachinePage`：继承自ProPage，不是ProGenerator体系，类名需注意
3. **测试命令**：`python3 -c "import sys; sys.path.insert(0,'v3'); from generators.daily_pro import DailyReportPro; r = DailyReportPro(); r.build_standard_report(); print(r.sections)"`

### daily_update.py集成
- 新增`generate_all_reports()`函数，统一生成7个报告Pro版
- 函数必须定义在`main()`之前，否则Python报NameError
- 路径映射使用`path_map`字典统一管理
