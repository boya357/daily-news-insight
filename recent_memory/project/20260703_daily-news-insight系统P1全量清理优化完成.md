# 2026-07-03 daily-news-insight 系统P1全量清理优化完成

## 完成情况
### P0 白卡修复 ✅
- 编写fix_toolpage_whitecards.py批量替换18个工具页内联硬编码浅色背景!important为深色半透明底，调整深色文字为浅色
- 保留@media print打印样式、评分黄色/红绿买卖/蓝紫徽章等彩色元素不变
- 非打印区硬编码白底!important剩余数：0

### P1 重复目录合并 ✅
- sector-heatmap/、alerts/、longhubang_perspective/保持原有跳转配置
- topic_health/、topic_health_report/改为跳转至/topic-health/
- weekly-evolution/旧版文件归档，跳转至/weekly_review/

### P1 遗留reports归档 ✅
- 2.2MB共27个子目录的旧产业链报告移动到docs/_archives/legacy/reports/
- 原位置新建跳转页指向/industry_chain/

### P2 空目录清理 ✅
- docs/js/stock-hover-card.js因有440处引用保留
- report_converter、_templates旧模板归档到legacy目录
- docs/data/因有运行时JSON数据保留

### P2 生成器旧版本归档 ✅
- 创建v3/generators/_legacy，移入40个旧版本备份文件
- 保留被日常调度依赖的非_pro版本，29个核心模块import全量通过

### P1 首页链接修复 ✅
- 补充缺失的changelog.html跳转页
- 首页所有链接目标校验0缺失，锚点#today/#tools/#archive全部有效

### 收尾 ✅
- update_list_pages.py运行成功，10个目录列表页全部刷新深色玻璃态
- validate_system.sh 41项全过，无失败无警告
- 提交并推送origin/main，commit: ac20f5f
