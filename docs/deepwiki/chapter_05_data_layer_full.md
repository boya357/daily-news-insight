# 第5章 数据层 - 系统的数据基石

> "数据是智能系统的血液，稳定可靠的数据层是一切上层能力的基础。"
>
> —— DeepWiki 设计理念

## 目录

- [5.1 数据层架构总览](#51-数据层架构总览)
- [5.2 稳定行情数据获取器 - 多数据源冗余机制](#52-稳定行情数据获取器---多数据源冗余机制)
- [5.3 市场数据管理器 - 统一数据更新入口](#53-市场数据管理器---统一数据更新入口)
- [5.4 统一股票管理器 - 三级覆盖模型](#54-统一股票管理器---三级覆盖模型)
- [5.5 股票发现管理器 - 自动识别与注册](#55-股票发现管理器---自动识别与注册)
- [5.6 数据质量校验器 - 可靠性保障体系](#56-数据质量校验器---可靠性保障体系)
- [5.7 统一数据加载器 - 标准化数据访问](#57-统一数据加载器---标准化数据访问)
- [5.8 数据层设计哲学与最佳实践](#58-数据层设计哲学与最佳实践)

---

## 5.1 数据层架构总览

### 5.1.1 核心定位

数据层是整个 DeepWiki 系统的「数据基石」，承担着从外部数据源获取信息、加工处理、质量校验到统一分发的全链路职责。它向上层的报告生成器、分析引擎、可视化组件提供标准化的数据服务，确保整个系统使用**同源、可信、及时**的数据。

### 5.1.2 整体架构

数据层采用「获取-管理-校验-访问」的四层架构设计：

```
┌─────────────────────────────────────────────────────────────┐
│                        上层应用层                             │
│  日报生成器  │  周报生成器  │  个股分析  │  产业链分析  │  ...  │
└─────────────┴──────────────┴────────────┴───────────────┴────┘
                              ▲
                              │ 标准化数据接口
┌─────────────────────────────────────────────────────────────┐
│                     统一数据加载器 (DataLoader)               │
│  缓存机制 │ 格式转换 │ 面向对象访问 │ 历史快照管理            │
└─────────────────────────────────────────────────────────────┘
                              ▲
                              │
┌─────────────────────────────────────────────────────────────┐
│                     数据管理层                                │
│  市场数据管理器 │ 统一股票管理器 │ 股票发现管理器              │
└─────────────────────────────────────────────────────────────┘
                              ▲
                              │
┌─────────────────────────────────────────────────────────────┐
│                     数据获取层                                │
│  稳定行情数据获取器 (多数据源冗余) │ 数据质量校验器             │
└─────────────────────────────────────────────────────────────┘
                              ▲
                              │
┌─────────────────────────────────────────────────────────────┐
│                     外部数据源                                │
│  腾讯财经 API  │  东方财富 API  │  龙虎榜数据  │  其他...     │
└─────────────────────────────────────────────────────────────┘
```

### 5.1.3 模块协作关系

各模块之间的协作遵循明确的职责边界：

```
外部数据源
    │
    ▼
┌──────────────────┐     ┌──────────────────┐
│ 稳定行情数据获取器 │────▶│ 数据质量校验器    │
│ (stable_market_  │     │ (data_quality_   │
│  fetcher.py)     │     │  checker.py)     │
└────────┬─────────┘     └──────────────────┘
         │
         ▼
┌──────────────────┐
│ 市场数据管理器    │
│ (market_data_    │
│  manager.py)     │
└────────┬─────────┘
         │ 写入 data/*.json
         ▼
┌──────────────────┐
│ JSON 数据文件    │
│ (market.json,    │
│  portfolio.json, │
│  topics.json...) │
└────────┬─────────┘
         │ 读取
         ▼
┌──────────────────┐
│ 统一数据加载器    │
│ (data_loader.py) │
└────────┬─────────┘
         │
         ▼
    上层应用
```

### 5.1.4 核心设计原则

| 原则 | 描述 |
|------|------|
| **单一数据源** | 所有上层应用通过统一入口访问数据，杜绝数据不一致 |
| **多源冗余** | 关键数据采用多数据源冗余，任一数据源故障不影响整体可用性 |
| **失败安全** | 数据获取失败时保留旧数据，确保系统始终可用 |
| **质量可观测** | 数据质量可校验、可报告，问题可追溯 |
| **访问透明** | 上层应用无需关心数据来源和存储格式，通过标准接口访问 |

---

## 5.2 稳定行情数据获取器 - 多数据源冗余机制

### 5.2.1 功能定位

**稳定行情数据获取器**（`stable_market_fetcher.py`）是数据层的最底层模块，负责从外部数据源获取实时行情数据。它的核心价值在于通过**多数据源冗余**和**自动重试**机制，将不稳定的外部API转化为稳定可靠的数据输入。

### 5.2.2 核心实现

#### 多数据源架构

系统设计了主备双数据源架构，按优先级依次尝试：

```
                    ┌─────────────────┐
                    │   数据请求      │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │  腾讯财经 (主)  │
                    │  Qt.gtimg.cn    │
                    └────────┬────────┘
                             │
                 ┌───────────┴───────────┐
                 │ 成功                  │ 失败
                 ▼                        ▼
        ┌─────────────────┐     ┌─────────────────┐
        │  返回格式化数据 │     │  东方财富 (备)  │
        └─────────────────┘     │  push2.eastm   │
                                │  oney.com       │
                                └────────┬────────┘
                                         │
                                ┌────────┴────────┐
                                │ 成功           │ 失败
                                ▼                 ▼
                        ┌──────────────┐  ┌──────────────────┐
                        │ 返回格式化数据│  │ 返回None(调用方   │
                        └──────────────┘  │ 使用历史数据)     │
                                        └──────────────────┘
```

**数据源配置：**

```python
# 数据源优先级（按稳定性排序）
DATA_SOURCES = ['tencent', 'eastmoney']
```

#### 自动重试机制

HTTP请求层实现了指数退避重试策略，应对网络抖动和临时故障：

```python
def _http_get(url, timeout=10, max_retries=2, encoding='utf-8'):
    """带重试的HTTP GET请求"""
    for i in range(max_retries):
        try:
            req = urllib.request.Request(url, headers=_get_headers())
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                raw = resp.read()
                return raw.decode(encoding)
        except Exception as e:
            if i < max_retries - 1:
                time.sleep(1 + i)  # 指数退避：1秒、2秒
            else:
                raise e
    return None
```

**关键设计：**
- 重试次数：默认 2 次（共 3 次尝试）
- 退避策略：线性退避 `1 + i` 秒
- 超时控制：默认 10 秒超时，避免长时间阻塞
- 随机UA：每次请求使用随机 User-Agent，降低被封禁风险

#### 股票代码智能识别

腾讯财经接口需要根据股票代码前缀判断市场归属，系统实现了智能的前缀检测：

```python
def _detect_prefix(code, type_='stock'):
    """判断股票代码属于沪市还是深市"""
    if type_ == 'index':
        # 指数判断
        if code.startswith('000') or code.startswith('001') or code.startswith('006'):
            return 'sh'  # 上证指数、科创50等沪市指数
        elif code.startswith('399'):
            return 'sz'  # 深证成指、创业板指等深市指数
        # ...
    else:
        # 股票判断
        if code.startswith('6') or code.startswith('900'):
            return 'sh'  # 沪市主板、B股
        elif code.startswith('0') or code.startswith('3') or code.startswith('200'):
            return 'sz'  # 深市主板、创业板、B股
        elif code.startswith('8') or code.startswith('4'):
            return 'bj'  # 北交所
        else:
            return 'sh'
```

#### 统一输出格式

无论使用哪个数据源，最终输出格式完全一致：

```python
{
    'name': '贵州茅台',      # 股票名称
    'code': '600519',       # 股票代码
    'price': 1688.00,       # 当前价格
    'change': 28.50,        # 涨跌额
    'change_pct': 0.0172,   # 涨跌幅（小数形式）
    'up': True,             # 涨跌方向
    'high': 1700.00,        # 最高价
    'low': 1670.00,         # 最低价
    'open': 1675.00,        # 开盘价
    'pre_close': 1659.50,   # 昨收价
    'source': 'tencent',    # 实际使用的数据源
}
```

### 5.2.3 安全更新机制

#### 失败保护（Fail-Safe）

数据更新采用「失败不覆盖」策略，确保系统始终有数据可用：

```python
def safe_update_market_data():
    """安全更新市场数据 - 失败时不覆盖原有数据"""
    market_file = DATA_DIR / 'market.json'
    old_data = None
    if market_file.exists():
        with open(market_file, 'r', encoding='utf-8') as f:
            old_data = json.load(f)
    
    # 获取指数数据
    indices = fetch_indexes()
    
    if len(indices) < 3:
        print(f"⚠️  仅获取到 {len(indices)} 个指数数据，保留原有数据")
        return old_data  # 数据不完整时返回旧数据
    
    # ... 数据处理 ...
    
    # 只有数据完整时才写入新数据
    with open(market_file, 'w', encoding='utf-8') as f:
        json.dump(new_data, f, ensure_ascii=False, indent=4)
    
    return new_data
```

**保护策略：**
- 指数数据不足 3 个时，判定为获取失败，保留旧数据
- 单只股票获取失败时，保留原价，不影响其他股票
- 异常捕获到顶层，确保任何异常都不会导致数据文件损坏

#### 历史归档

每次成功更新后自动归档历史数据，支持回溯分析：

```python
# 归档到 history/market/ 目录
history_dir = DATA_DIR / 'history' / 'market'
history_dir.mkdir(parents=True, exist_ok=True)
today = datetime.now().strftime('%Y-%m-%d')
history_file = history_dir / f'{today}.json'
with open(history_file, 'w', encoding='utf-8') as f:
    json.dump(new_data, f, ensure_ascii=False, indent=4)
```

### 5.2.4 龙虎榜数据接口

除了基础行情数据，获取器还支持龙虎榜数据的获取和整合：

#### 数据整合流程

```
┌─────────────────┐   ┌─────────────────┐
│ 机构买卖明细     │   │ 每日概况数据     │
│ (RPT_ORGANIZATION│   │ (RPT_DAILYBILL- │
│  _TRADE_DETAILS) │   │  BOARD_PROFILE) │
└────────┬────────┘   └────────┬────────┘
         │                      │
         └──────────┬───────────┘
                    ▼
            ┌──────────────┐
            │ 数据整合模块   │
            │  - 去重合并   │
            │  - 板块识别   │
            │  - 统计计算   │
            └──────┬───────┘
                   ▼
            ┌──────────────┐
            │ 标准化输出    │
            └──────────────┘
```

#### 智能板块识别

系统内置关键词匹配算法，自动为龙虎榜股票打上板块标签：

```python
sector_keywords = {
    'AI算力': ['算力', '服务器', 'AI', '人工智能', '芯片', ...],
    '存储芯片': ['存储', '内存', '闪存', '兆易', '佰维', ...],
    '人形机器人': ['机器人', '智元', '拓普', '三花', ...],
    # ... 更多板块
}
```

### 5.2.5 设计亮点

| 亮点 | 说明 | 价值 |
|------|------|------|
| **主备自动切换** | 腾讯财经为主，东方财富为辅，自动降级 | 99%+ 的数据获取成功率 |
| **失败不覆盖** | 数据异常时保留历史数据 | 确保系统始终可用 |
| **统一输出格式** | 多数据源输出统一结构 | 上层应用无需感知数据源差异 |
| **历史归档** | 每次更新自动存档 | 支持回溯分析、趋势对比 |
| **反封禁设计** | 随机UA、请求间隔、Referer伪装 | 降低被数据源封禁风险 |

### 5.2.6 注意事项

1. **依赖第三方服务**：行情数据依赖腾讯财经和东方财富的公开接口，存在接口变更或封禁风险
2. **数据延迟**：公开接口通常有 3-10 秒延迟，不适合高频交易场景
3. **编码差异**：腾讯使用 GBK 编码，东方财富使用 UTF-8，需注意编码转换
4. **字段差异**：不同数据源返回的字段精度和范围可能不同，统一输出时需做归一化

---

## 5.3 市场数据管理器 - 统一数据更新入口

### 5.3.1 功能定位

**市场数据管理器**（`market_data_manager.py`）是数据更新的统一入口，封装了所有市场相关数据的更新操作，向上层提供「一键更新」能力。它负责协调底层获取器、处理衍生指标、管理风险状态。

### 5.3.2 核心实现

#### 类结构设计

```python
class MarketDataManager:
    """统一市场数据管理器"""
    
    def __init__(self, data_dir: str = None):
        # 数据目录配置
        self.data_dir = Path(data_dir) if data_dir else ...
        self.portfolio_file = self.data_dir / 'portfolio.json'
        self.market_file = self.data_dir / 'market.json'
    
    # 指数数据更新
    def update_indices(self) -> Tuple[List[dict], bool]: ...
    
    # 持仓数据更新
    def update_portfolio(self) -> Tuple[List[dict], bool]: ...
    
    # 热门板块更新
    def update_hot_sectors(self) -> bool: ...
    
    # 完整更新
    def update_all(self, force_update: bool = False) -> dict: ...
```

**设计模式：** 外观模式（Facade），为复杂的子系统提供统一的高层接口。

#### 持仓数据更新流程

持仓更新不仅获取价格，还会计算风险状态、更新组合汇总：

```
调用 fetch_stock_price()
        │
        ▼
  更新 current_price
  更新 today_change
  更新 today_high/low/open
        │
        ▼
  调用 _update_risk_status()
  计算风险等级
  设置风险颜色和图标
        │
        ▼
  调用 _update_portfolio_summary()
  计算总收益
  统计盈亏数量
  计算健康分数
        │
        ▼
  保存到 portfolio.json
```

#### 风险状态计算

基于持仓浮盈/浮亏比例，自动计算风险等级：

```python
def _update_risk_status(self, stock: dict):
    """更新股票的风险状态"""
    cost_price = stock.get('cost_price', 0)
    current_price = stock.get('current_price', 0)
    stop_loss_price = stock.get('stop_loss_price', 0)
    
    if stop_loss_price > 0 and current_price <= stop_loss_price:
        stock['risk_level'] = '高危区 - 已跌破止损'
        stock['risk_color'] = 'text-red-600'
        stock['risk_progress'] = 95
        stock['icon'] = '🆘'
    elif cost_price > 0:
        profit_pct = (current_price - cost_price) / cost_price
        if profit_pct > 0.5:
            stock['risk_level'] = '安全区 - 大幅盈利'
            stock['risk_progress'] = 20
            # ...
        elif profit_pct > 0:
            stock['risk_level'] = '安全区 - 正常波动'
            stock['risk_progress'] = 40
            # ...
```

**风险等级映射：**

| 等级 | 状态 | 进度值 | 颜色 | 图标 |
|------|------|--------|------|------|
| 高危区 | 跌破止损 | 95 | 红色 | 🆘 |
| 危险区 | 浮亏较大 | 80 | 红色/橙色 | 📉 |
| 警戒区 | 小幅浮亏 | 65 | 黄色 | ⚠️ |
| 安全区 | 正常波动 | 40 | 蓝色/绿色 | 📈 |
| 安全区 | 大幅盈利 | 20 | 绿色 | ✅ |

#### 市场情绪计算

基于指数平均涨跌幅，计算市场情绪指标（恐惧贪婪指数）：

```python
def _calculate_sentiment(self, avg_change: float) -> dict:
    """根据指数平均涨跌幅计算市场情绪"""
    if avg_change > 0.03:
        fear_greed = 90
        fg_text = "极度贪婪"
    elif avg_change > 0.02:
        fear_greed = 80
        fg_text = "贪婪"
    elif avg_change > 0.01:
        fear_greed = 68
        fg_text = "乐观"
    # ... 更多区间
    return {
        'fear_greed': fear_greed,
        'fear_greed_text': fg_text,
    }
```

### 5.3.3 单例模式

为了确保全局只有一个数据管理器实例，避免重复加载和状态不一致，采用单例模式：

```python
_manager = None

def get_market_manager(data_dir: str = None) -> MarketDataManager:
    """获取市场数据管理器单例"""
    global _manager
    if _manager is None:
        _manager = MarketDataManager(data_dir)
    return _manager
```

### 5.3.4 完整更新流程

`update_all()` 方法提供了一键更新能力，返回结构化的更新结果：

```python
def update_all(self, force_update: bool = False) -> dict:
    """完整更新所有市场数据"""
    results = {
        'indices': False,
        'portfolio': False,
        'sectors': False,
        'update_time': datetime.now().isoformat(),
    }
    
    # 1. 更新指数
    _, results['indices'] = self.update_indices()
    
    # 2. 更新持仓
    _, results['portfolio'] = self.update_portfolio()
    
    # 3. 更新板块
    results['sectors'] = self.update_hot_sectors()
    
    return results
```

### 5.3.5 设计亮点

| 亮点 | 说明 | 价值 |
|------|------|------|
| **统一入口** | 所有数据更新通过一个管理器完成 | 简化上层调用，降低维护成本 |
| **风险状态自动计算** | 价格更新后自动计算风险等级 | 报告生成时直接使用，无需重复计算 |
| **结构化结果** | 更新返回结构化的成功/失败状态 | 便于上层做逻辑判断和UI展示 |
| **单例模式** | 全局唯一实例 | 避免重复初始化和状态不一致 |

---

## 5.4 统一股票管理器 - 三级覆盖模型

### 5.4.1 功能定位

**统一股票管理器**（`unified_stock_manager.py`）负责管理所有股票的分析数据和详情页面。它提出了「三级覆盖模型」，确保股票从被发现到拥有完整分析页面的全生命周期管理。

### 5.4.2 三级覆盖模型

```
Level 1: 已发现
    股票名称已加入股票池
    仅有基本信息（名称、代码、板块）
    ▲
    │ 调用 generate_analysis_data()
    │
Level 2: 有分析数据
    已生成完整的分析JSON数据
    包含技术面、基本面、消息面分析
    ▲
    │ 调用 generate_detail_page()
    │
Level 3: 有详情页
    已生成独立的HTML详情页
    用户可直接访问浏览
```

**数据结构定义：**

```python
{
    'stocks': {
        '贵州茅台': {
            'code': '600519',
            'sector': '白酒',
            'rating': '买入',
            'score': 85,
            'data_level': 3,        # 覆盖级别
            'analyze_time': '2024-01-15 10:30:00'
        },
        # ... 更多股票
    },
    'total': 156,
    'update_time': '2024-01-15 10:30:00'
}
```

### 5.4.3 核心功能

#### 股票发现（Level 1）

将新股票添加到股票池，建立基本档案：

```python
def discover_stocks(self, stock_names: List[str], 
                   stock_codes: Dict[str, str] = None,
                   sectors: Dict[str, str] = None) -> int:
    """发现新股票并添加到列表"""
    data = self.load_stock_list()
    existing = set(data['stocks'].keys())
    new_stocks = set(stock_names) - existing
    
    for name in new_stocks:
        code = stock_codes.get(name, '') if stock_codes else ''
        sector = sectors.get(name, '') if sectors else ''
        data['stocks'][name] = {
            'code': code,
            'sector': sector,
            'rating': '待分析',
            'data_level': 1  # Level 1: 仅名称
        }
    
    return len(new_stocks)
```

#### 分析数据生成（Level 2）

调用 StockAnalyzer 生成完整的多维度分析数据：

```python
def generate_analysis_data(self, stock_code: str, stock_name: str) -> Optional[Dict]:
    """生成股票分析数据"""
    try:
        analyzer = StockAnalyzer(stock_code, stock_name)
        
        # 尝试加载K线数据
        kline_file = self.data_dir / f'kline_{stock_code}.json'
        if kline_file.exists():
            with open(kline_file, 'r', encoding='utf-8') as f:
                prices = json.load(f)
            analyzer.load_historical_data(prices)
        
        analysis = analyzer.analyze_all()
        
        # 保存分析数据
        output_file = self.data_dir / f'{stock_code}.json'
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(analysis, f, ensure_ascii=False, indent=2)
        
        # 更新股票列表级别
        data = self.load_stock_list()
        data['stocks'][stock_name].update({
            'rating': analysis.get('overall', {}).get('rating', ''),
            'score': analysis.get('overall', {}).get('score', 0),
            'data_level': 2,
            'analyze_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        })
        self.save_stock_list(data)
        
        return analysis
    except Exception as e:
        print(f"  ❌ {stock_name} 分析数据生成失败: {e}")
        return None
```

#### 详情页生成（Level 3）

基于分析数据生成可视化的 HTML 详情页：

```python
def generate_detail_page(self, stock_code: str, stock_name: str) -> bool:
    """生成个股分析详情页"""
    try:
        output_path = str(self.pages_dir / f'{stock_name}.html')
        html = generate_stock_detail(stock_code, stock_name, 
                                    str(self.data_dir), str(self.pages_dir))
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(html)
        
        # 更新级别
        data = self.load_stock_list()
        data['stocks'][stock_name]['data_level'] = 3
        self.save_stock_list(data)
        
        return True
    except Exception as e:
        return False
```

#### 列表页生成

管理器还支持生成股票分析列表索引页，自动展示所有已覆盖的股票：

```python
def generate_list_page(self, output_path: str = None) -> str:
    """生成个股分析列表页"""
    # 读取所有股票数据
    # 按名称排序
    # 生成卡片式HTML
    # 包含三维评分展示
    # ...
```

### 5.4.4 批量处理

支持批量提升股票覆盖级别：

```python
def batch_process(self, stock_names: List[str] = None, level: int = 3) -> Dict:
    """批量处理股票
    
    Args:
        stock_names: 股票名称列表，None表示处理所有已发现的股票
        level: 处理级别 (1=仅发现, 2=生成数据, 3=生成页面)
    """
    # 遍历股票，逐级提升
    # ...
```

### 5.4.5 覆盖统计

实时统计各等级的覆盖率：

```python
def get_coverage_stats(self) -> Dict:
    """获取覆盖统计"""
    data = self.load_stock_list()
    stocks = data['stocks']
    total = len(stocks)
    
    level2 = sum(1 for s in stocks.values() if s.get('data_level', 1) >= 2)
    level3 = sum(1 for s in stocks.values() if s.get('data_level', 1) >= 3)
    
    return {
        'total': total,
        'level1': total,
        'level2': level2,
        'level3': level3,
        'level2_pct': f'{level2/total*100:.1f}%' if total else '0%',
        'level3_pct': f'{level3/total*100:.1f}%' if total else '0%',
    }
```

### 5.4.6 设计亮点

| 亮点 | 说明 | 价值 |
|------|------|------|
| **三级递进模型** | 从发现到数据再到页面，渐进式覆盖 | 降低初始成本，支持按需深化 |
| **元数据集中管理** | 所有股票的元信息统一存储在 stock_list.json | 便于查询、统计和管理 |
| **自动化生成** | 分析和页面生成全自动化 | 可扩展到数千只股票的覆盖规模 |
| **覆盖率可观测** | 实时统计各等级覆盖率 | 便于评估数据完备性和进度 |

---

## 5.5 股票发现管理器 - 自动识别与注册

### 5.5.1 功能定位

**股票发现管理器**（`stock_discovery_manager.py`）是一个自动化工具，负责从各类报告和页面中自动识别股票名称，并将其注册到股票池中。它解决了「股票越来越多，手动管理跟不上」的问题。

### 5.5.2 股票提取算法

#### 多策略提取

系统采用三重提取策略，确保尽可能多地识别股票：

```
策略1: 格式匹配
  匹配「名称(代码)」格式
  如：贵州茅台(600519)
  精度：★★★★★  召回：★★☆☆☆

策略2: 已知词匹配
  匹配已知股票名称
  基于已有的股票池
  精度：★★★★☆  召回：★★★★☆

策略3: 上下文推断
  根据板块、行业关键词
  结合常见股票名称模式
  （当前版本未实现，预留扩展）
```

#### 格式匹配实现

```python
def extract_stocks_from_text(self, text: str) -> List[Tuple[str, str]]:
    """从文本中提取股票名称和代码"""
    found = {}  # name -> code
    
    # 1. 匹配「名称(代码)」格式（最可靠）
    # 支持：中文名(6位数字)、中文名(5位数字港股)
    pattern = r'([\u4e00-\u9fa5A-Za-z][\u4e00-\u9fa5A-Za-z0-9\*\-]{1,9})\s*[\(（](\d{4,6}[\.\w]*)[\)）]'
    matches = re.findall(pattern, text)
    for name, code in matches:
        name = name.strip()
        if len(name) >= 2:
            found[name] = code
    
    # 2. 匹配已知股票名称
    known = self.get_known_stocks()
    code_map = self.get_stock_code_map()
    
    # 按长度降序排序，避免子串匹配
    sorted_stocks = sorted(known, key=len, reverse=True)
    
    for stock_name in sorted_stocks:
        if stock_name in text and stock_name not in found:
            # 防误判：确保名称前后不是其他中文字符
            idx = text.find(stock_name)
            before = text[idx-1] if idx > 0 else ''
            after = text[idx+len(stock_name)] if idx+len(stock_name) < len(text) else ''
            
            if not before or not re.match(r'[\u4e00-\u9fa5]', before) or \
               not after or not re.match(r'[\u4e00-\u9fa5]', after):
                found[stock_name] = code_map.get(stock_name, '')
    
    return [(name, code) for name, code in found.items()]
```

**关键设计：**
- **长度优先匹配**：按名称长度降序匹配，避免「茅台」匹配到「贵州茅台」的子串
- **边界检测**：检查前后字符是否为中文字符，避免误匹配到更长的词中
- **去重合并**：两种策略结果合并，格式匹配结果优先（因为带代码）

#### HTML文本提取

在处理HTML文件时，先提取纯文本再进行股票识别：

```python
def _extract_html_text(self, html_content: str) -> str:
    """从HTML中提取纯文本"""
    # 移除script和style标签内容
    text = re.sub(r'<(script|style)[^>]*>.*?</\1>', '', html_content, flags=re.DOTALL)
    # 移除HTML标签
    text = re.sub(r'<[^>]+>', '', text)
    # 清理空白
    text = re.sub(r'\s+', ' ', text)
    return text.strip()
```

### 5.5.3 注册与同步机制

#### 批量注册

支持从目录下所有文件批量发现并注册股票：

```python
def discover_from_directory(self, dir_path: str, pattern: str = '*.html') -> Dict[str, List[str]]:
    """从目录下所有文件中发现股票"""
    results = {}
    dir_p = Path(dir_path)
    for f in dir_p.glob(pattern):
        stocks = self.discover_from_html(str(f))
        if stocks:
            results[f.name] = [s[0] for s in stocks]
    return results
```

#### 文件同步

定期根据实际文件状态同步股票列表元数据，确保数据一致性：

```python
def sync_stock_list_from_files(self):
    """根据实际文件同步更新股票列表元数据"""
    data = self.load_stock_list()
    stocks = data.get('stocks', {})
    
    for name, info in stocks.items():
        code = info.get('code', '')
        
        # 检查分析数据文件是否存在
        has_data = (self.data_dir / f'{code}.json').exists() if code else False
        
        # 检查详情页是否存在
        has_page = (self.pages_dir / f'{name}.html').exists()
        
        # 更新 data_level
        if has_page:
            info['data_level'] = 3
        elif has_data:
            info['data_level'] = 2
        else:
            info['data_level'] = 1
    
    self.save_stock_list(data)
```

### 5.5.4 设计亮点

| 亮点 | 说明 | 价值 |
|------|------|------|
| **自动发现** | 从报告中自动提取股票名称 | 无需手动维护股票池 |
| **多策略提取** | 格式匹配+已知词匹配双重策略 | 高准确率与高召回率兼得 |
| **智能防误判** | 边界检测、长度优先 | 降低误识别率 |
| **自动同步** | 根据文件状态自动同步元数据 | 确保数据一致性 |

### 5.5.5 注意事项

1. **识别准确率**：纯文本股票名称识别存在误判可能，特别是对于名称常见的股票（如「东方」可能匹配到「东方财富」「东方雨虹」等多只股票）
2. **性能考虑**：大文件或大量文件处理时，正则匹配可能较慢，建议异步处理
3. **缓存机制**：已知股票列表使用缓存，避免重复加载文件

---

## 5.6 数据质量校验器 - 可靠性保障体系

### 5.6.1 功能定位

**数据质量校验器**（`data_quality_checker.py`）是数据层的「质检员」，负责验证市场数据和持仓数据的合理性，检测异常数据，确保报告数据质量可信。

### 5.6.2 校验维度

#### 持仓数据校验

| 校验项 | 检查规则 | 严重程度 |
|--------|----------|----------|
| 文件存在性 | portfolio.json 必须存在 | 严重 ❌ |
| 股票列表非空 | stocks 数组不能为空 | 严重 ❌ |
| 价格合理性 | current_price > 0 且 < 10000 | 警告 ⚠️ |
| 涨跌幅合理性 | 非ST股 ≤ ±20%，ST股 ≤ ±5% | 警告 ⚠️ |
| 成本价合理性 | cost_price > 0 | 警告 ⚠️ |
| 数据时效性 | 更新时间在4小时以内 | 警告 ⚠️ |
| 涨跌幅格式 | 应为小数形式（0.xx），而非百分比数值（xx） | 警告 ⚠️ |

**核心校验代码：**

```python
def check_portfolio_data(self) -> Tuple[bool, List[str]]:
    """检查持仓数据质量"""
    issues = []
    
    # ... 加载文件 ...
    
    for stock in stocks:
        name = stock.get('name', '未知')
        code = stock.get('code', stock.get('id', ''))
        current_price = stock.get('current_price', 0)
        today_change = stock.get('today_change', 0)
        
        # 检查价格合理性
        if current_price <= 0:
            issues.append(f"❌ {name}({code}): 当前价格为 0 或负数")
        elif current_price < 1:
            issues.append(f"⚠️  {name}({code}): 当前价格过低 ({current_price}元)")
        elif current_price > 10000:
            issues.append(f"⚠️  {name}({code}): 当前价格过高 ({current_price}元)")
        
        # 检查涨跌幅合理性
        change_pct = abs(today_change) * 100
        is_st = 'ST' in name or 'st' in name.lower()
        max_change = 5 if is_st else 20
        
        if change_pct > max_change:
            issues.append(f"⚠️  {name}({code}): 涨跌幅异常 ({today_change*100:+.2f}%)")
```

#### 市场数据校验

| 校验项 | 检查规则 | 严重程度 |
|--------|----------|----------|
| 文件存在性 | market.json 必须存在 | 严重 ❌ |
| 指数非空 | indices 数组不能为空 | 严重 ❌ |
| 指数点位合理性 | price > 0 | 严重 ❌ |
| 指数涨跌幅 | ±10% 以内 | 警告 ⚠️ |
| 涨跌家数 | 总和在 100-10000 之间 | 警告 ⚠️ |
| 恐惧贪婪指数 | 在 0-100 范围内 | 警告 ⚠️ |
| 数据时效性 | 更新时间在4小时以内 | 警告 ⚠️ |

### 5.6.3 质量报告

校验器生成结构化的质量报告，包含详细问题列表和总体判定：

```python
result = {
    'is_valid': True/False,
    'portfolio': {
        'valid': True/False,
        'issues': [
            "✅ 持仓数据质量良好",
            "⚠️  贵州茅台: 涨跌幅异常 (15.5%)",
            # ...
        ],
    },
    'market': {
        'valid': True/False,
        'issues': [...],
    },
    'all_issues': [...],
    'summary': "数据质量良好，共 X 项检查结果",
}
```

### 5.6.4 设计亮点

| 亮点 | 说明 | 价值 |
|------|------|------|
| **分级告警** | 区分严重错误和警告 | 避免过度告警，聚焦关键问题 |
| **多维度校验** | 从存在性、合理性、时效性多维度检查 | 全面保障数据质量 |
| **结构化输出** | 返回结构化的检查结果 | 便于UI展示和自动化处理 |
| **ST股特殊处理** | 识别ST股并应用不同的涨跌幅阈值 | 提高校验准确性 |

### 5.6.5 注意事项

1. **校验粒度**：当前版本为轻量校验，主要检查明显的异常。如需更严格的校验，可扩展接入历史数据做对比校验
2. **时效性阈值**：4小时阈值是为非交易时段设计的，交易时段可适当调小
3. **误报率**：部分校验（如涨跌幅）可能在极端行情下误报，需结合实际情况判断

---

## 5.7 统一数据加载器 - 标准化数据访问

### 5.7.1 功能定位

**统一数据加载器**（`data_loader.py`）是数据层向上层应用提供的标准访问接口。它封装了底层数据存储细节，提供面向对象的数据访问能力，并内置缓存机制提升性能。

### 5.7.2 两种访问模式

数据加载器提供**函数式**和**面向对象**两种访问模式，满足不同场景需求：

```
┌───────────────────────────────────────────────────────┐
│                     上层应用                            │
│                                                       │
│  简单场景 ◀─── 函数式接口 ──── 复杂场景 ───▶ 面向对象接口 │
│  (get_holdings_for_   │     (DataLoader 类)          │
│   daily)              │                             │
└───────────────────────┼──────────────────────────────┘
                        │
                        ▼
                ┌─────────────────┐
                │ JSON 数据文件    │
                └─────────────────┘
```

### 5.7.3 函数式接口（轻量便捷）

针对常见场景提供便捷的独立函数，直接返回格式化数据：

```python
# 持仓相关
def get_holdings_for_daily(include_comments=True):
    """获取日报格式的持仓列表"""
    # 返回 [{name, code, price, change, up, comment, ratio}, ...]

def get_position_info():
    """获取仓位信息"""
    # 返回 {total, cash, risk_level}

# 市场相关
def get_indices_for_daily():
    """获取日报格式的大盘指数数据"""

def get_market_summary():
    """获取市场概览数据"""

def get_hot_sectors(limit=5):
    """获取热门板块"""

# 题材相关
def get_topics_by_level(level='S'):
    """获取指定级别的题材列表"""

def get_all_topics():
    """获取所有题材"""
```

**设计特点：**
- 直接返回 UI 友好的格式化数据（如涨跌符号、百分比字符串）
- 可直接用于模板渲染，无需额外处理
- 适合简单报表和快速开发

### 5.7.4 面向对象接口（强大灵活）

`DataLoader` 类提供更全面的数据访问能力，支持缓存、刷新、历史快照等高级功能。

#### 类结构

```python
class DataLoader:
    """统一数据加载器 - 面向对象的统一数据访问接口"""
    
    # 单例模式
    _instance = None
    _cache = {}
    _cache_time = {}
    
    # ============ 持仓数据 ============
    def get_portfolio(self) -> dict: ...
    def get_stocks(self) -> list: ...
    def get_portfolio_overview(self) -> dict: ...
    def get_longhubang(self) -> dict: ...
    
    # ============ 题材数据 ============
    def get_topics(self) -> dict: ...
    def get_s_level_topics(self) -> list: ...
    def get_topic_by_id(self, topic_id: str): ...
    
    # ============ 市场数据 ============
    def get_market(self) -> dict: ...
    def get_indices(self) -> list: ...
    def get_hot_sectors(self, limit: int = None) -> list: ...
    def get_market_sentiment(self) -> dict: ...
    
    # ============ 预警/预判 ============
    def get_alerts(self) -> dict: ...
    def get_predictions(self) -> dict: ...
    
    # ============ 历史数据 ============
    def get_history_snapshot(self, date: str) -> dict: ...
    def get_available_history_dates(self) -> list: ...
    
    # ============ 通用方法 ============
    def get_data(self, data_type: str) -> dict: ...
    def get_update_time(self, data_type: str) -> str: ...
    def refresh(self): ...  # 清空缓存
```

#### 智能缓存机制

为了避免重复读取文件，DataLoader 实现了基于文件修改时间的智能缓存：

```python
def _load_json(self, filename: str, force_reload: bool = False):
    """加载JSON文件，支持缓存"""
    filepath = os.path.join(self.data_dir, filename)
    
    # 检查缓存是否有效
    if not force_reload and filename in self._cache:
        mtime = os.path.getmtime(filepath)
        if filename in self._cache_time and self._cache_time[filename] == mtime:
            return self._cache[filename]  # 缓存命中
    
    # 读取文件
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # 更新缓存
    self._cache[filename] = data
    self._cache_time[filename] = os.path.getmtime(filepath)
    
    return data
```

**缓存策略：**
- **缓存键**：文件名
- **有效性判断**：比较文件修改时间（mtime）
- **刷新方式**：调用 `refresh()` 方法清空所有缓存
- **内存占用**：JSON 文件通常在几十 KB 级别，全量缓存也仅数 MB

#### 通用数据获取

`get_data()` 方法提供统一的动态数据访问入口：

```python
def get_data(self, data_type: str) -> dict:
    """通用数据获取方法
    
    Args:
        data_type: 数据类型标识，如 'portfolio'、'market'、'topics' 等
    """
    mapping = {
        'portfolio': 'get_portfolio',
        'market': 'get_market',
        'topics': 'get_topics',
        'alerts': 'get_alerts',
        'predictions': 'get_predictions',
        'industry_chain': 'get_industry_chains',
        'topic_details': 'get_topic_details',
    }
    
    if data_type not in mapping:
        raise ValueError(f"不支持的数据类型: {data_type}")
    
    method = getattr(self, mapping[data_type], None)
    if method:
        return method()
    return {}
```

### 5.7.5 数据格式转换

加载器负责将原始 JSON 数据转换为各场景需要的格式：

**示例：持仓数据转换为日报格式**

```python
def get_holdings_for_daily(include_comments=True):
    """获取日报格式的持仓列表"""
    data = load_portfolio()
    stocks = data['stocks']
    
    holdings = []
    for stock in stocks:
        name = stock['name']
        code = stock['id']
        price = f"{stock['current_price']:.2f}"
        
        # 涨跌幅格式化
        change_pct = stock.get('today_change', 0)
        if change_pct >= 0:
            change = f"+{change_pct*100:.2f}%"
            up = True
        else:
            change = f"{change_pct*100:.2f}%"
            up = False
        
        # 仓位占比（使用默认分配或从配置读取）
        default_ratios = {"英维克": 30, "铜冠铜箔": 30, ...}
        ratio = default_ratios.get(name, 25)
        
        holdings.append({
            "name": name,
            "code": code,
            "price": price,
            "change": change,
            "up": up,
            "comment": comment,
            "ratio": ratio
        })
    
    return holdings
```

### 5.7.6 历史快照管理

支持按日期查询历史数据快照，用于复盘和趋势分析：

```python
def get_history_snapshot(self, date: str) -> dict:
    """获取指定日期的历史快照"""
    filename = f"history/{date}.json"
    try:
        return self._load_json(filename)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def get_available_history_dates(self) -> list:
    """获取可用的历史快照日期列表"""
    history_dir = os.path.join(self.data_dir, "history")
    if not os.path.exists(history_dir):
        return []
    
    dates = []
    for f in os.listdir(history_dir):
        if f.endswith('.json'):
            dates.append(f.replace('.json', ''))
    
    return sorted(dates, reverse=True)  # 按日期倒序
```

### 5.7.7 设计亮点

| 亮点 | 说明 | 价值 |
|------|------|------|
| **双模式访问** | 函数式轻量便捷 + 面向对象强大灵活 | 满足不同复杂度的需求 |
| **智能缓存** | 基于文件mtime的缓存机制 | 提升性能，减少IO |
| **格式友好** | 直接返回UI友好的格式化数据 | 减少上层重复代码 |
| **单例模式** | 全局唯一实例，共享缓存 | 节省内存，保证一致性 |
| **历史回溯** | 支持按日期查询历史快照 | 支持复盘和趋势分析 |
| **统一入口** | 所有数据访问通过加载器完成 | 底层存储变化不影响上层 |

### 5.7.8 注意事项

1. **缓存时效**：缓存基于文件修改时间判断，数据更新后会自动失效
2. **内存占用**：缓存所有加载过的文件，极端情况下可能占用较多内存
3. **线程安全**：当前实现非线程安全，多线程环境需注意
4. **扩展类型**：新增数据类型需要在 `mapping` 字典中注册

---

## 5.8 数据层设计哲学与最佳实践

### 5.8.1 核心设计原则

#### 1. 单一数据源原则 (Single Source of Truth)

> 所有上层应用必须通过统一数据加载器访问数据，禁止直接读取 JSON 文件。

**为什么重要：**
- 避免数据不一致：不同模块各自读取文件可能导致版本不一致
- 便于演进优化：底层存储格式变化时，只需修改加载器，上层无感
- 质量可控：所有数据访问经过同一入口，便于注入校验和监控

#### 2. 失败安全原则 (Fail-Safe)

> 任何数据获取失败都不应导致系统崩溃，应优雅降级使用历史数据。

**实现方式：**
- 多数据源冗余：主数据源失败自动切换备用
- 失败不覆盖：更新失败时保留旧数据文件
- 异常兜底：所有外部调用都有异常捕获
- 空值处理：返回合理的默认值而非 None

#### 3. 渐进式覆盖原则 (Progressive Coverage)

> 数据覆盖度不求一步到位，而是分级逐步完善。

**三级模型的价值：**
- Level 1 成本极低（仅名称），可快速覆盖大量标的
- Level 2 需要计算资源，但自动化程度高
- Level 3 需要页面渲染，成本最高但体验最好
- 根据资源和优先级决定哪些股票升级到哪一级

#### 4. 可观测性原则 (Observability)

> 数据质量应该是可度量、可检查、可报告的。

**实践：**
- 数据质量校验器提供结构化检查报告
- 每类数据都有明确的更新时间戳
- 覆盖率可统计、可展示
- 异常情况有日志记录和告警标识

### 5.8.2 关键技术权衡

#### 权衡1：实时性 vs 稳定性

| 方案 | 实时性 | 稳定性 | 实现复杂度 |
|------|--------|--------|------------|
| 每次请求实时拉取 | 极高 | 低（依赖网络） | 高 |
| 定时更新 + 文件缓存 | 中等（取决于更新频率） | 高 | 低 |
| 混合模式（关键数据实时，其他定时） | 较高 | 中 | 中 |

**系统选择**：定时更新 + 文件缓存方案。

**理由**：
- 投资分析场景对秒级实时性要求不高
- 稳定性和可靠性更重要
- 实现简单，维护成本低
- 失败安全机制容易实现

#### 权衡2：数据完整性 vs 获取效率

| 方案 | 数据完整性 | 获取效率 | 实现复杂度 |
|------|-----------|----------|------------|
| 全量获取所有字段 | 高 | 慢 | 高 |
| 按需获取（懒加载） | 按需 | 快 | 中 |
| 核心字段预取 + 扩展字段按需 | 较高 | 较快 | 中 |

**系统选择**：核心字段预取方案。

**理由**：
- 常用字段（价格、涨跌幅、名称）每次都需要
- 扩展字段（如龙虎榜、资金流向）使用频率低
- 平衡了获取效率和数据完整性

#### 权衡3：集中式管理 vs 分布式存储

| 方案 | 一致性 | 扩展性 | 维护成本 |
|------|--------|--------|----------|
| 单一JSON文件集中存储 | 高 | 低 | 低 |
| 按主题分文件存储 | 中 | 中 | 中 |
| 数据库存储 | 高 | 高 | 高 |

**系统选择**：按主题分文件存储（market.json、portfolio.json、topics.json 等）。

**理由**：
- 文件数量适中（10个以内），维护成本低
- 不同数据更新频率不同，分开存储避免频繁写入大文件
- 便于按主题做权限控制和缓存策略
- 相比数据库，部署简单，无需额外服务

### 5.8.3 最佳实践清单

#### ✅ 文件组织

- [ ] 数据文件统一存放在 `data/` 目录下
- [ ] 历史数据按 `data/history/{类型}/{日期}.json` 归档
- [ ] 文件名使用有意义的英文名称，见名知意
- [ ] JSON 文件使用 UTF-8 编码，indent=2 格式化

#### ✅ 数据更新

- [ ] 数据更新操作必须原子化（先写临时文件，再rename）
- [ ] 更新失败时绝对不能覆盖原有数据
- [ ] 每次成功更新后记录更新时间戳
- [ ] 更新操作支持幂等（多次调用结果一致）

#### ✅ 数据访问

- [ ] 上层应用必须通过 DataLoader 访问数据
- [ ] 禁止在业务代码中直接 open() 数据文件
- [ ] 频繁访问的数据利用缓存提升性能
- [ ] 访问不存在的数据时返回合理默认值

#### ✅ 质量保障

- [ ] 关键数据在使用前必须经过质量校验
- [ ] 异常数据要有明确的告警标识（如 ⚠️、❌）
- [ ] 数据校验报告要易于理解和排查
- [ ] 定期巡检数据质量，及时发现潜在问题

#### ✅ 扩展性

- [ ] 新增数据源要符合统一输出格式
- [ ] 新增数据类型要在 DataLoader 中注册
- [ ] 模块间通过明确定义的接口交互
- [ ] 配置与代码分离，便于调整参数

### 5.8.4 演进方向

数据层的未来演进将围绕以下方向展开：

1. **数据源扩展**：接入更多数据源（如新浪财经、同花顺、交易所公开数据），进一步提升数据丰富度和冗余度

2. **实时推送**：从「定时拉取」演进为「WebSocket 实时推送」，满足更高实时性需求

3. **数据仓库**：当数据量达到一定规模后，引入时序数据库存储历史行情，支持更复杂的量化分析

4. **数据血缘**：建立数据血缘追踪，每个数据点都可追溯来源、更新时间、校验状态

5. **智能告警**：基于数据质量校验结果，自动推送异常告警（如数据长时间未更新、价格异动等）

---

## 本章小结

数据层是 DeepWiki 系统的基石，通过「获取-管理-校验-访问」四层架构，将不稳定的外部数据转化为稳定、可靠、标准化的数据服务。

**核心模块回顾：**

| 模块 | 核心职责 | 关键特性 |
|------|----------|----------|
| 稳定行情数据获取器 | 多数据源获取行情 | 主备切换、自动重试、失败安全 |
| 市场数据管理器 | 统一数据更新入口 | 一键更新、风险计算、情绪指标 |
| 统一股票管理器 | 股票全生命周期管理 | 三级覆盖模型、批量处理、覆盖率统计 |
| 股票发现管理器 | 自动识别与注册 | 多策略提取、智能防误判、目录扫描 |
| 数据质量校验器 | 数据可靠性保障 | 多维度校验、分级告警、质量报告 |
| 统一数据加载器 | 标准化数据访问 | 双模式接口、智能缓存、历史快照 |

这些模块共同构成了一个健壮、可扩展、高质量的数据底座，支撑着上层所有的分析、展示和决策能力。

> 下一章我们将深入「分析层」，看看如何基于这些数据生成有洞察力的投资分析。
