# 📊 专业报告生成工具 - 完整版本

## 支持的报告类型

| 类型 | 目录 | 说明 |
|------|------|------|
| `daily` | 日报 | 每日新闻洞察 |
| `intraday` | 盘中 | 盘中快报（实时） |
| `aftermarket` | 盘后 | 盘后速递 |
| `industry_chain` | 产业链 | 产业链深度研究报告 |
| `weekly_review` | 周复盘 | 周度复盘总结 |

## 核心特性

✅ **智能章节识别** - 自动识别9种章节类型（核心结论、标的分析、风险提示等）

✅ **专业组件库** - 10+种精美组件（数据卡片、核心摘要、标的分析卡、风险提示框、表格等）

✅ **安全列表页** - 绝对不会覆盖成单篇报告，列表页与报告页完全分离

✅ **统一导航** - 所有页面共享同一导航栏，全站体验一致

✅ **原子写入** - 先写临时文件，成功后原子替换，杜绝半坏文件

## 使用方法

### 1. 生成单篇报告

```bash
cd report_converter
python generate_report.py convert <md文件> <html输出文件> [报告类型]
```

示例：
```bash
# 生成产业链深度报告
python generate_report.py convert \
    ../docs/industry_chain/20260530_英伟达N1X.md \
    ../docs/industry_chain/20260530_英伟达N1X.html \
    industry_chain
```

### 2. 更新列表页

```bash
# 更新所有列表页
python generate_report.py update-list ../docs

# 更新指定列表页
python generate_report.py update-list ../docs daily intraday weekly_review
```

### 3. 完整流程（转换 + 更新列表）

```bash
python generate_report.py full <md文件> <html文件> <报告类型> <docs目录>
```

示例：
```bash
python generate_report.py full \
    ../docs/daily/20260531.md \
    ../docs/daily/20260531.html \
    daily \
    ../docs
```

## 文件结构

```
report_converter/
├── converter.py          # 核心转换器
├── report_templates.py   # 各报告类型专用模板
├── list_updater.py       # 列表页更新器
├── generate_report.py    # 统一入口
└── README.md             # 本文档
```

## 安全机制

1. **原子写入** - 所有文件操作先写临时文件，成功后再原子替换
2. **列表页分离** - 列表页生成逻辑与单篇报告完全独立，永不混淆
3. **异常降级** - 专用模板失败时自动降级到通用模板
4. **文件存在检查** - 转换前先检查源文件是否存在

## 与定时任务集成

在定时任务脚本中调用：

```bash
# 每日新闻洞察
cd /path/to/report_converter
python generate_report.py full \
    ../docs/daily/$(date +%Y%m%d).md \
    ../docs/daily/$(date +%Y%m%d)_每日新闻洞察.html \
    daily \
    ../docs

# Git推送
cd ../docs
git add .
git commit -m "每日新闻洞察 $(date +%Y-%m-%d)"
git push origin main
```
