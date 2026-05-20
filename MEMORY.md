# MEMORY.md - 记忆文件

## 当前项目状态摘要（2026-05-19）

### GitHub仓库
- repo: boya357/daily-news-insight
- Pages: https://boya357.github.io/daily-news-insight/

### 页面结构
- 首页: docs/index.html (市场洞察中心)
- 产业链总览: docs/industry_chain/latest.html
- 每日洞察: docs/daily/latest.html
- 盘中快报: docs/intraday/latest.html  
- 盘后速递: docs/aftermarket/latest.html

### 产业链清单
- S级: MLCC、人形机器人、存储芯片、CPO/光器件、铜箔
- A级: 液冷温控(Token工厂/AI Agent/商业航天)
- B级: PCB/氦气/eVTOL/环氧树脂
- C级: AI眼镜/先进封装/算力租赁/算电协同

### 持仓
- 英维克(002837): 成本103.81元，关注98元支撑
- 川润股份(002272): 成本20.61元，液冷概念

### 关键脚本
- src/simple_push.py: 简化推送
- src/update_daily_latest.py: 增量更新daily
- src/update_report_latest.py: 更新盘中/盘后快报
- src/md_to_html.py: MD转HTML（沉浸光影风格）

### 导航栏规范
- 首页: https://boya357.github.io/daily-news-insight/
- 产业链: https://boya357.github.io/daily-news-insight/industry_chain/latest.html
- 每日洞察: https://boya357.github.io/daily-news-insight/daily/latest.html
- 盘中快报: https://boya357.github.io/daily-news-insight/intraday/latest.html
- 盘后速递: https://boya357.github.io/daily-news-insight/aftermarket/latest.html


## 页面结构规范（重要！2026-05-20更新）

### 首页链接（已验证正确）
- 首页标题: `<a href="/">📊 市场洞察中心</a>`
- 产业链4个卡片:
  - 人形机器人 → `reports/具身智能日报/具身智能产业链标准日报.html`
  - 存储芯片 → `reports/存储产业链/存储产业链核心标的深度研究.html`
  - 光纤光模块 → `reports/CPO产业链/CPO产业链标准日报.html`
  - 铜箔 → `reports/铜箔产业链/铜箔产业链标准日报.html`

### 各页面性质
| 页面 | latest.html 性质 | 内容页命名 |
|------|----------------|-----------|
| 首页 | 直接内容页 | - |
| 每日洞察 | 报告列表页 ✅ | daily/YYYYMMDD_标题.html |
| 盘中快报 | 报告列表页 ✅ | intraday/YYYYMMDD.html |
| 盘后速递 | 报告列表页 ✅ | aftermarket/YYYY-MM-DD.html |
| 产业链总览 | 直接内容页 | industry_chain/latest.html |

### 盘中快报特殊规则
- **intraday/latest.html** = 报告列表页（展示所有历史报告）
- **intraday/intraday_latest.html** = 今日盘中快报内容页

### 导航栏链接规范（相对路径）
子目录页面使用相对路径: `../daily/latest.html`
