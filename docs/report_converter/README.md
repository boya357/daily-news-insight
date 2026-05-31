# MLCC Pro v2.0 报告模板体系

## 📋 概述

所有报告已升级为统一的 MLCC Pro v2.0 标准模板，包含：
- ✅ 全站统一导航栏（12个固定链接，glass-nav毛玻璃效果）
- ✅ 阅读进度条
- ✅ 回到顶部按钮
- ✅ 一键导出PDF（使用浏览器原生打印）
- ✅ 一键分享功能
- ✅ 平滑滚动
- ✅ 移动端完美适配
- ✅ 打印优化
- ✅ 标准的报告信息区和免责声明

## 🎯 三级模板体系

### Level 1: 深度研报模板
**适用场景**: 产业链深度研究、重大专题报告

**包含功能**:
- 完整的6章报告结构
- 10+交互式图表支持
- 核心数据卡片
- 五星标的推荐
- 目录卡片导航（支持高亮）
- 完整的报告信息区和标签系统

**文件**: `templates/level1_deep_report.html`

---

### Level 2: 标准报告模板
**适用场景**: 周复盘、月报、催化日历等

**包含功能**:
- 3-4章内容结构
- 支持3-5个图表
- 保留所有MLCC Pro核心功能
- 简洁的报告头部

**文件**: `templates/level2_standard_report.html`

---

### Level 3: 轻量快报模板
**适用场景**: 每日新闻洞察、盘中快报、盘后速递等

**包含功能**:
- 极简的报告结构
- 保留统一导航栏
- 极简的内容展示

**文件**: `templates/level3_quick_report.html`

---

## 📁 目录结构

```
report_converter/
├── templates/
│   ├── level1_deep_report.html    # 深度研报模板
│   ├── level2_standard_report.html # 标准报告模板
│   └── level3_quick_report.html   # 轻量快报模板
├── scripts/
│   └── converter.py               # 批量转换脚本
└── README.md
```

## 🚀 使用方法

### 批量转换旧报告

```bash
cd report_converter/scripts
python converter.py <文件或目录> [输出目录]
```

**示例**:

```bash
# 转换单个文件
python converter.py ../../daily/20260530_每日新闻洞察.html

# 批量转换整个目录
python converter.py ../../daily/ ../../converted/
```

### 自动级别判断

转换工具会根据文件名自动判断报告级别：
- 包含"深度"、"产业链"、"N1X"、"HBM" → Level 1
- 包含"daily"、"盘中"、"盘后" → Level 3
- 其他 → Level 2

也可以手动指定级别：

```python
converter.convert_file('report.html', level='level1')
```

---

## 🔧 模板变量说明

所有模板使用统一的变量格式 `{{变量名}}`:

| 变量 | 说明 |
|------|------|
| `{{REPORT_TITLE}}` | 报告标题 |
| `{{REPORT_DATE}}` | 发布日期 |
| `{{REPORT_SUBTITLE}}` | 副标题 (Level1) |
| `{{REPORT_SUMMARY}}` | 核心摘要 (Level1) |
| `{{REPORT_CONTENT}}` | 报告主体内容 |
| `{{REPORT_TYPE}}` | 报告类型 |
| `{{REPORT_TAGS}}` | 核心标签 |
| `{{CORE_DATA_CARDS}}` | 核心数据卡片 (Level1) |
| `{{STAR_RECOMMENDATIONS}}` | 五星标的推荐 (Level1) |
| `{{TOC_CARDS}}` | 目录导航卡片 (Level1) |
| `{{REPORT_LEVEL_LABEL}}` | 级别标签 (Level1) |
| `{{REPORT_TYPE_TAGS}}` | 报告类型标签 (Level1) |
| `{{COVERAGE_TICKERS}}` | 覆盖标的数量 (Level1) |

---

## 📊 全站导航栏统一规范

所有页面统一使用以下12个导航链接（顺序固定）：

1. 首页 → `/daily-news-insight/index.html`
2. 日报 → `/daily-news-insight/daily/latest.html`
3. 盘中 → `/daily-news-insight/intraday/latest.html`
4. 盘后 → `/daily-news-insight/aftermarket/latest.html`
5. 产业链 → `/daily-news-insight/industry_chain/latest.html`
6. 周复盘 → `/daily-news-insight/weekly_review/latest.html`
7. 周前瞻 → `/daily-news-insight/weekly_outlook/latest.html`
8. 催化日历 → `/daily-news-insight/催化日历/latest.html`
9. 周末速递 → `/daily-news-insight/周末速递/latest.html`
10. 明日催化 → `/daily-news-insight/明日催化剂/latest.html`
11. S级催化 → `/daily-news-insight/s级催化扫描/latest.html`
12. 月报 → `/daily-news-insight/monthly/latest.html`

**样式统一**:
- `px-3 py-1.5 rounded-lg`
- 激活状态：`bg-white/20 text-white`
- 未激活状态：`text-white/80 hover:text-white hover:bg-white/10`

---

## ✅ 已完成工作

1. ✅ 三级模板体系创建完成（Level1/Level2/Level3）
2. ✅ `_templates/报告页标准模板.html` 升级为MLCC Pro标准
3. ✅ 批量转换脚本 `converter.py` 完成
4. ✅ 所有工具系统页面导航栏统一
5. ✅ 首页重新设计并上线
6. ✅ 产业链时钟导航栏修复

---

## 📝 版本历史

### v2.0 (2026-05-31)
- ✅ 全站导航栏统一为glass-nav标准
- ✅ 报告页标准模板升级为MLCC Pro
- ✅ 三级模板体系建立
- ✅ 批量转换工具完成
- ✅ 首页重新设计上线

### v1.0 (2026-05-30)
- ✅ MLCC Pro终极模板首次应用于英伟达N1X深度报告
- ✅ 16项核心功能全部实现
