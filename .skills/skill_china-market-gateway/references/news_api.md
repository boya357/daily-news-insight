# 财经新闻API参考

## 数据源

**财联社 (CLS)** - 中国专业财经新闻平台

- 覆盖：A股、港股、美股、商品、外汇、债券
- 特色：7×24小时电报快讯
- 时效性：重大事件秒级推送

## 基本用法

```python
from scripts.yuan_data import YuanData

data = YuanData()
news = data.news.search("新能源汽车", limit=10)

for item in news:
    print(f"📰 {item['title']}")
    print(f"   来源: {item['source']} | {item['timestamp']}\n")
```

## 返回数据字段

| 字段名 | 类型 | 说明 | 示例 |
|--------|------|------|------|
| `title` | str | 新闻标题 | "比亚迪1月新能源汽车销量同比增长30%" |
| `source` | str | 数据来源 | "CLS" |
| `timestamp` | str | 查询时间戳 | "2026-02-12T14:30:00" |

**注意**：当前实现仅返回标题，不包含正文内容。

## 搜索技巧

### 按公司名称搜索

```python
# 搜索特定公司相关新闻
news = data.news.search("茅台")
news = data.news.search("腾讯")
news = data.news.search("宁德时代")
```

### 按行业搜索

```python
# 搜索行业相关新闻
news = data.news.search("芯片")
news = data.news.search("房地产")
news = data.news.search("医药")
```

### 按主题搜索

```python
# 搜索热点主题
news = data.news.search("降息")
news = data.news.search("人工智能")
news = data.news.search("碳中和")
```

## 搜索结果数量控制

```python
# 获取更多结果
news = data.news.search("新能源", limit=50)

# 只看最新几条
news = data.news.search("A股", limit=5)
```

**默认限制**：20条
**最大建议**：50条（过多可能影响性能）

## 实际应用示例

### 监控特定股票新闻

```python
from scripts.yuan_data import YuanData

def monitor_stock_news(stock_name: str, keywords: list):
    """监控特定股票的相关新闻"""
    data = YuanData()

    print(f"=== {stock_name} 新闻监控 ===\n")

    for keyword in keywords:
        news = data.news.search(keyword, limit=5)
        if news:
            print(f"关键词: {keyword}")
            for item in news[:3]:
                print(f"  • {item['title']}")
            print()

# 示例：监控宁德时代
monitor_stock_news(
    "宁德时代",
    ["宁德时代", "动力电池", "新能源汽车"]
)
```

### 行业热点追踪

```python
def track_industry_hotspots(industry: str):
    """追踪行业热点新闻"""
    data = YuanData()
    news = data.news.search(industry, limit=20)

    if news:
        print(f"=== {industry}行业动态 ===\n")
        for i, item in enumerate(news, 1):
            print(f"{i}. {item['title']}")
    else:
        print(f"未找到与'{industry}'相关的新闻")

# 示例
track_industry_hotspots("人工智能")
```

### 多主题新闻汇总

```python
def daily_news_digest(topics: list):
    """每日财经新闻摘要"""
    data = YuanData()

    print("=== 今日财经要闻 ===\n")

    for topic in topics:
        news = data.news.search(topic, limit=3)
        if news:
            print(f"【{topic}】")
            for item in news:
                print(f"  • {item['title']}")
            print()

# 示例：获取每日财经摘要
daily_news_digest([
    "央行",
    "A股",
    "美联储",
    "人民币汇率"
])
```

## 注意事项

### 1. 搜索结果特点

- **标题为主**：当前实现仅抓取标题，不含正文
- **时效性**：结果按时间倒序排列（最新的在前）
- **相关性**：使用关键词匹配，可能包含不太相关的内容

### 2. 数据局限性

- **缺少时间戳**：返回的 `timestamp` 是查询时间，非新闻发布时间
- **无正文链接**：未提供新闻详情页URL
- **无分类标签**：缺少行业、类型等分类信息

### 3. 搜索限制

- **关键词长度**：建议2-10个字符
- **中文优先**：英文关键词可能效果较差
- **避免过于宽泛**：如"股票"、"市场"等词搜索结果过多且不精准

### 4. 访问频率

- 避免短时间大量搜索
- 建议每次搜索间隔1-2秒
- 过于频繁可能被限制访问

## 错误处理

```python
news = data.news.search("不存在的关键词xyz123")
if not news:
    print("未找到相关新闻")
    print("可能原因：")
    print("1. 关键词过于生僻")
    print("2. 网络连接问题")
    print("3. 数据源暂时不可用")
```

## 扩展建议

如需更完整的新闻数据，可考虑：

1. **增加数据源**：
   - 新浪财经新闻
   - 东方财富资讯
   - 金十数据快讯

2. **爬取详情页**：
   - 基于标题提取URL
   - 进一步抓取正文内容

3. **时间过滤**：
   - 添加日期筛选功能
   - 仅返回最近N天的新闻

4. **分类整理**：
   - 按行业自动分类
   - 识别重要性标签

## 合规声明

- 数据来源于财联社公开网页
- 仅用于个人学习研究
- 禁止商业化使用
- 尊重数据源版权
