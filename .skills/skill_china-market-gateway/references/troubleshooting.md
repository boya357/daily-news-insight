# 故障排查指南

## 常见问题与解决方案

### 1. 股票代码查询无数据

**症状**：调用 `get_stock_price()` 返回 `None`

**可能原因及解决方案**：

#### 原因1：港股代码格式错误

港股代码必须是5位数字：

```python
# ❌ 错误
get_stock_price("hk700")      # 只有3位
get_stock_price("hk2259")     # 只有4位

# ✅ 正确
get_stock_price("hk00700")    # 补齐到5位
get_stock_price("hk02259")    # 补齐到5位
```

**自动修正**：`yuan_data.py` 已内置自动补零逻辑。

#### 原因2：股票停牌或退市

检查股票是否正常交易：

```python
from scripts.yuan_data import YuanData

data = YuanData()

# 尝试多个数据源
sina_result = data.stock.get_quote("sh600519")
if sina_result is None:
    print("新浪财经无数据，可能股票停牌或退市")
```

**判断方法**：
- 访问东方财富官网查询股票状态
- 使用百度股市通验证代码有效性

#### 原因3：交易时间外查询

**现象**：非交易时间返回昨日收盘数据或无数据

**交易时间**：
- 上午：9:30 - 11:30
- 下午：13:00 - 15:00
- 周末及法定节假日休市

**解决方案**：
```python
from datetime import datetime

now = datetime.now()
hour = now.hour
minute = now.minute
weekday = now.weekday()

# 判断是否交易时间
is_trading_time = (
    weekday < 5 and  # 非周末
    (
        (9 <= hour < 11) or  # 上午盘
        (hour == 11 and minute <= 30) or
        (13 <= hour < 15)  # 下午盘
    )
)

if not is_trading_time:
    print("当前非交易时间，数据为上一交易日收盘价")
```

### 2. 网络连接问题

**症状**：所有接口均返回 `None` 或超时

**诊断步骤**：

#### 步骤1：检查基础网络

```bash
# 测试网络连通性
ping baidu.com
ping finance.sina.com.cn
```

#### 步骤2：测试数据源可访问性

```python
import requests

urls = [
    "https://finance.sina.com.cn",
    "https://fund.eastmoney.com",
    "https://www.cls.cn"
]

for url in urls:
    try:
        response = requests.get(url, timeout=5)
        print(f"✅ {url} 可访问 (状态码: {response.status_code})")
    except Exception as e:
        print(f"❌ {url} 不可访问: {e}")
```

#### 步骤3：配置代理（境外访问必需）

```python
from scripts.yuan_data import YuanData

# 使用代理
data = YuanData(proxy="http://localhost:10809")
quote = data.stock.get_quote("sh600519")
```

**常用代理类型**：
- HTTP代理：`http://host:port`
- HTTPS代理：`https://host:port`
- SOCKS5代理：需要额外配置

### 3. 数据解析错误

**症状**：日志显示 "数据解析失败"

**原因**：数据源返回格式变化

**解决方案**：

#### 方案1：查看原始响应

```python
import requests

url = "http://hq.sinajs.cn/list=sh600519"
response = requests.get(url)
print("原始数据:", response.text)
```

对比 `yuan_data.py` 中的解析逻辑，检查字段位置是否改变。

#### 方案2：更新解析代码

如果数据源格式确实变化，需修改 `_parse_sina_data()` 方法。

### 4. 基金净值查询失败

**症状**：`get_fund_nav()` 返回 `None`

**诊断**：

```python
from scripts.yuan_data import YuanData

data = YuanData()
fund = data.fund.get_quote("161039")

if fund is None:
    # 手动检查接口
    import requests
    url = "https://fundgz.1234567.com.cn/js/161039.js"
    response = requests.get(url)
    print("原始响应:", response.text)
```

**常见问题**：
- 基金代码错误（6位数字）
- 基金已清盘
- QDII基金在海外市场休市时无估值

### 5. 宏观数据为空列表

**症状**：`get_gdp_data()` 等方法返回空列表 `[]`

**原因分析**：

```python
from scripts.yuan_data import YuanData

data = YuanData()
gdp = data.macro.get_gdp()

if not gdp:
    print("可能原因:")
    print("1. 东方财富数据中心接口变更")
    print("2. 访问频率过高被限制")
    print("3. 数据暂时维护中")
```

**解决方案**：
- 等待一段时间后重试
- 检查东方财富官网是否正常
- 联系维护者更新接口

### 6. 财经新闻搜索无结果

**症状**：`data.news.search()` 返回空列表

**诊断流程**：

```python
from scripts.yuan_data import YuanData

data = YuanData()
news = data.news.search("茅台", limit=10)

if not news:
    # 手动测试接口
    import requests
    url = "https://www.cls.cn/searchPage"
    params = {'keyword': '茅台', 'type': 'telegraph'}
    response = requests.get(url, params=params)
    print("HTTP状态码:", response.status_code)
    print("响应内容长度:", len(response.text))
```

**可能原因**：
- 关键词过于生僻
- 财联社网站结构调整
- 被识别为爬虫限制访问

**建议**：
- 更换常见关键词尝试
- 添加 User-Agent 随机化
- 降低请求频率

## 调试技巧

### 启用详细日志

```python
import logging

# 设置为DEBUG级别查看详细信息
logging.basicConfig(level=logging.DEBUG)

from scripts.yuan_data import get_stock_price
quote = get_stock_price("sh600519")
```

### 捕获完整异常信息

```python
import traceback
from scripts.yuan_data import YuanData

try:
    data = YuanData()
    quote = data.stock.get_quote("sh600519")
except Exception as e:
    print("错误详情:")
    traceback.print_exc()
```

### 手动测试HTTP请求

```python
import requests

# 模拟库的请求方式
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    'Accept': 'application/json, text/html',
}

response = requests.get(
    "http://hq.sinajs.cn/list=sh600519",
    headers=headers,
    timeout=30
)

print("状态码:", response.status_code)
print("响应内容:", response.text[:500])
```

## 性能问题

### 查询速度慢

**优化方案**：

1. **使用连接池**（已内置）
2. **添加超时设置**：
```python
data = YuanData()
data.session.timeout = 10  # 设置全局超时
```

3. **批量查询优化**：
```python
import time

codes = ["sh600519", "sh600036", "sz000858"]
for code in codes:
    quote = get_stock_price(code)
    time.sleep(0.2)  # 避免请求过快
```

### 内存占用高

长期运行时注意清理 session：

```python
data = YuanData()
# ... 使用数据 ...
data.session.close()  # 手动关闭连接
```

## 联系维护者

如果上述方法都无法解决问题，可能是数据源接口发生重大变化，请联系技能包维护者。

提供以下信息有助于快速定位问题：
1. 完整的错误信息或日志
2. 使用的 Python 版本
3. 测试的股票/基金代码
4. 是否使用代理
5. 所在地区（境内/境外）
