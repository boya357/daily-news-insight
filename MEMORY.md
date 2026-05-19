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
