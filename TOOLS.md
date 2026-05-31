# TOOLS.md - 工具使用经验与坑点记录

## 📌 一、报告生成工具规范

### 1. report_converter.py 完整使用流程
```
# 1. 生成HTML报告
cd report_converter
python generate_report.py --type daily --date YYYYMMDD

# 2. 更新列表页（绝对不能用cp命令覆盖！）
python list_updater.py --type daily

# 3. 验证文件存在
ls ../daily/YYYYMMDD_每日新闻洞察.html
ls ../daily/latest.html

# 4. Git推送
cd ..
git add daily/YYYYMMDD_每日新闻洞察.html daily/latest.html
git commit -m "[每日新闻]: YYYYMMDD 市场热点与个股机会"
git push

# 5. Pages验证
# 访问 https://boya357.github.io/daily-news-insight/daily/latest.html 确认无404
```

### 2. 核心禁令（违反必出问题）
- ❌ 禁止用 `cp 报告.html latest.html` 覆盖列表页 → 必须用 `list_updater.py` 独立生成
- ❌ 禁止只推送 latest.html 不推送报告本体 → 必须两个文件一起 add 和 push
- ❌ 禁止只替换报告标题不替换主体内容 → 必须100%完全替换，核心内容验证
- ❌ 禁止保留 v2/v3/v4 等中间版本 → 最终版重命名，立即清理所有中间版本
- ❌ 禁止三层导航不一致 → 首页/列表/报告三层必须同时验证

---

## 📌 二、5大核心错误的完整解决方案

### 错误1：Git推送404
**问题**：只推送latest.html链接，忘记推送报告本体文件
**解决方案**：
```
# 推送前必须两个文件都在
git status  # 确认两个文件都被add
git add daily/YYYYMMDD_报告.html daily/latest.html
git commit -m "..."
git push

# 推送后立即验证
curl -I https://boya357.github.io/daily-news-insight/daily/YYYYMMDD_报告.html
# 返回200才完成，返回404立即补救
```
**根本解决**：专业报告生成系统V1.0已内置原子写入机制，两个文件同时生成

---

### 错误2：HTML模板替换错误
**问题**：基于MLCC模板生成N1X报告时，只替换标题不替换主体
**解决方案**：
```
# 替换后必须验证3处核心内容
1. 标题是否正确
2. 核心章节是否与主题匹配
3. 图表数据是否与主题匹配
```
**根本解决**：模板参数化，所有内容通过配置文件传入，不允许手动局部替换

---

### 错误3：列表页覆盖错误
**问题**：用cp命令将单篇报告覆盖到latest.html，导致列表页消失
**解决方案**：
```
# 绝对禁止
cp report.html latest.html  ❌ 绝对不能这么做

# 必须用
python list_updater.py --type daily  ✅ 正确方式
```
**根本解决**：list_updater.py独立维护，与报告生成完全解耦

---

### 错误4：重复报告清理错误
**问题**：报告生成过程中产生v2/v3/v4等多个中间版本，未及时清理导致列表页显示重复
**解决方案**：
```
# 生成最终版后立即执行
rm -f *v2.html *v3.html *v4.html *final.html  # 清理所有中间版本
mv 报告_v5.html 报告.html  # 最终版重命名
```
**根本解决**：专业报告生成系统V1.0已内置版本清理机制

---

### 错误5：导航栏统一错误
**问题**：首页、列表页、单篇报告三个层级导航栏样式、链接数量、路径前缀不一致
**解决方案**：
```
# 导航栏必须100%统一：
1. 12个完整导航链接（首页、每日新闻、盘中快报、盘后速递、周复盘、周三前瞻、月报、产业链、催化日历、周末速递、明日催化、S级催化）
2. max-w-7xl 超宽容器
3. 紫色渐变背景风格
4. 当前页面高亮 bg-white/20

# 三层同时验证
1. 首页导航栏 ✅
2. 列表页导航栏 ✅
3. 单篇报告导航栏 ✅
```
**根本解决**：统一导航栏模板组件，所有页面从同一组件渲染

---

## 📌 三、专业报告功能实现

### MLCC Pro 终极模板功能清单
| 功能 | 实现方式 | 优先级 |
|-----|---------|-------|
| 阅读进度条 | CSS position: fixed + JS滚动监听 | P0 |
| 回到顶部按钮 | fixed定位 + JS scrollTo | P0 |
| 一键导出PDF | window.print() + 打印样式优化 | P0 |
| 目录自动高亮 | Intersection Observer API | P1 |
| 平滑滚动 | html { scroll-behavior: smooth } | P1 |
| 报告信息区 | 底部专业信息展示（版本/生成时间/标签） | P1 |
| Chart.js图表支持 | CDN引入 + canvas渲染 | P0 |
| 移动端响应式 | Tailwind sm/md/lg断点 | P0 |

---

## 📌 四、企业微信推送规范

### 推送脚本使用
```
python simple_push.py \
  --title "2026年5月31日 每日新闻洞察" \
  --url "https://boya357.github.io/daily-news-insight/daily/20260531_每日新闻洞察.html" \
  --type "daily"
```

### 推送规则
- 仅推送链接，不生成长篇摘要
- 标题格式：`YYYY年MM月DD日 报告类型`
- 链接必须是GitHub Pages完整URL，不含/docs/前缀

---

## 📌 五、搜索与数据规范

### 价格数据获取
- **强制要求**：生成报告必须用 `search_web` 查询当日收盘价
- **禁止**：使用历史价格数据生成报告
- **数据源优先级**：韭研公社 > 财联社 > 东方财富 > 同花顺

### 搜索工具使用
```
# 产业链深度研究必须搜索
search_web(query="英伟达N1X 最新进展 2026", num=5)
search_web(query="黄仁勋 COMPUTEX 2026 演讲内容", num=3)

# 个股弹性必须查最新价
search_web(query="胜宏科技 最新股价 2026-05-31", num=2)
```

---

## 📌 六、Git提交规范

### 提交信息格式
```
# 新增报告
[报告类型]: YYYYMMDD 描述
例：[产业链]: 20260530 英伟达N1X芯片深度研究报告

# 系统修复
[修复]: 描述
例：[修复]: PDF导出改用浏览器原生打印功能

# 系统升级
[升级]: 描述
例：[升级]: MLCC Pro终极模板，16项功能优化

# 历史教训记录
[教训]: 描述
例：[教训]: 列表页cp覆盖错误，必须用list_updater.py
```

### 推送前检查清单
- [ ] 报告文件存在且大小正常（>10KB）
- [ ] latest.html存在且是完整列表页（>5KB）
- [ ] 所有链接指向的文件都已存在
- [ ] 导航栏三层统一
- [ ] 没有v2/v3/v4等中间版本残留