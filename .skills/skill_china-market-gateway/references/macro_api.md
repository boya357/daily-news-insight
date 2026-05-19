# 宏观经济数据API参考

## 数据源

**东方财富数据中心** - 提供权威的中国宏观经济指标

- 数据来源：国家统计局
- 更新频率：按指标发布周期（月度/季度/年度）
- 覆盖范围：GDP、CPI、PPI、PMI等核心指标

## 支持的经济指标

### GDP（国内生产总值）

```python
from scripts.yuan_data import get_gdp_data

gdp = get_gdp_data()
latest = gdp[0]  # 最新数据
print(f"报告期: {latest['REPORT_DATE']}")
print(f"GDP总值: {latest['DOMESTICL_PRODUCT_BASE']}万亿元")
print(f"同比增长: {latest['SUM_SAME']}%")
```

**返回字段**：
- `REPORT_DATE`: 报告期（如"2024-12-31"）
- `TIME`: 时间描述（如"2024年"）
- `DOMESTICL_PRODUCT_BASE`: GDP绝对值（万亿元）
- `SUM_SAME`: 同比增长率(%)
- `FIRST_PRODUCT_BASE`: 第一产业增加值
- `SECOND_PRODUCT_BASE`: 第二产业增加值
- `THIRD_PRODUCT_BASE`: 第三产业增加值

**发布周期**：季度发布，每季度后15-20天公布

### CPI（居民消费价格指数）

```python
from scripts.yuan_data import get_cpi_data

cpi = get_cpi_data()
latest = cpi[0]
print(f"报告期: {latest['REPORT_DATE']}")
print(f"全国CPI同比: {latest['NATIONAL_SAME']}%")
print(f"城市CPI同比: {latest.get('CITY_SAME', 'N/A')}%")
```

**返回字段**：
- `REPORT_DATE`: 报告期
- `TIME`: 时间描述
- `NATIONAL_SAME`: 全国同比涨幅(%)
- `NATIONAL_BASE`: 全国环比涨幅(%)
- `NATIONAL_ACCUMULATE`: 全国累计涨幅(%)
- `CITY_SAME`: 城市同比涨幅(%)
- `RURAL_SAME`: 农村同比涨幅(%)

**发布周期**：月度发布，每月10日左右公布上月数据

### PPI（工业生产者出厂价格指数）

```python
from scripts.yuan_data import get_ppi_data

ppi = get_ppi_data()
latest = ppi[0]
print(f"报告期: {latest['REPORT_DATE']}")
print(f"PPI同比: {latest['BASE_SAME']}%")
```

**返回字段**：
- `REPORT_DATE`: 报告期
- `TIME`: 时间描述
- `BASE`: 定基指数
- `BASE_SAME`: 同比涨幅(%)
- `BASE_ACCUMULATE`: 累计涨幅(%)

**发布周期**：月度发布，每月9-10日公布上月数据

### PMI（采购经理指数）

```python
from scripts.yuan_data import get_pmi_data

pmi = get_pmi_data()
latest = pmi[0]
print(f"报告期: {latest['REPORT_DATE']}")
print(f"制造业PMI: {latest['MAKE_INDEX']}")
print(f"非制造业PMI: {latest['NMAKE_INDEX']}")
```

**返回字段**：
- `REPORT_DATE`: 报告期
- `TIME`: 时间描述
- `MAKE_INDEX`: 制造业PMI指数
- `MAKE_SAME`: 制造业同比
- `NMAKE_INDEX`: 非制造业PMI指数
- `NMAKE_SAME`: 非制造业同比

**PMI解读**：
- **50以上**：经济扩张
- **50以下**：经济收缩
- **50**: 临界点

**发布周期**：月度发布，每月月初1日公布上月数据

## 使用示例

### 查看最新经济数据汇总

```python
from scripts.yuan_data import YuanData

data = YuanData()

print("=== 中国经济数据一览 ===\n")

# GDP
gdp = data.macro.get_gdp(page_size=1)
if gdp:
    print(f"【GDP】 {gdp[0]['TIME']}")
    print(f"  总值: {gdp[0]['DOMESTICL_PRODUCT_BASE']}万亿元")
    print(f"  增速: {gdp[0]['SUM_SAME']}%\n")

# CPI
cpi = data.macro.get_cpi(page_size=1)
if cpi:
    print(f"【CPI】 {cpi[0]['TIME']}")
    print(f"  同比: {cpi[0]['NATIONAL_SAME']}%")
    print(f"  环比: {cpi[0]['NATIONAL_BASE']}%\n")

# PPI
ppi = data.macro.get_ppi(page_size=1)
if ppi:
    print(f"【PPI】 {ppi[0]['TIME']}")
    print(f"  同比: {ppi[0]['BASE_SAME']}%\n")

# PMI
pmi = data.macro.get_pmi(page_size=1)
if pmi:
    print(f"【PMI】 {pmi[0]['TIME']}")
    print(f"  制造业: {pmi[0]['MAKE_INDEX']}")
    print(f"  非制造业: {pmi[0]['NMAKE_INDEX']}")
```

### 获取历史数据对比

```python
# 获取近12个月CPI数据
cpi_data = data.macro.get_cpi(page_size=12)

print("近12个月CPI走势:")
for item in cpi_data:
    print(f"{item['TIME']}: {item['NATIONAL_SAME']}%")
```

## 数据特点

### 发布时间规律

| 指标 | 发布频率 | 通常发布时间 | 时效性 |
|------|---------|-------------|--------|
| GDP | 季度 | 季后15-20天 | T+15天 |
| CPI | 月度 | 次月10日 | T+10天 |
| PPI | 月度 | 次月9-10日 | T+9天 |
| PMI | 月度 | 次月1日 | T+1天 |

### 数据修正

- 国家统计局可能对已公布数据进行修正
- 通常在年度数据公布时进行调整
- 历史数据可能与首次公布值不同

## 注意事项

1. **数据时效**：
   - 接口返回的是已公布的历史数据
   - 无法获取未来或实时数据
   - 最新数据通常有一定滞后

2. **数据来源**：
   - 所有数据源自国家统计局
   - 通过东方财富数据中心获取
   - 权威性高，可信度强

3. **字段缺失**：
   - 部分历史数据字段可能为空
   - 统计口径调整会导致字段变化
   - 使用时需检查字段是否存在

4. **访问频率**：
   - 宏观数据更新频率低
   - 无需高频查询
   - 建议按需查询或缓存使用

## 错误处理

```python
gdp = get_gdp_data()
if not gdp:
    print("获取失败，可能原因：")
    print("1. 网络连接问题")
    print("2. 数据源接口变更")
    print("3. 访问受限")
else:
    print(f"成功获取 {len(gdp)} 条数据")
```

## 应用场景

- **宏观经济分析**：判断经济周期阶段
- **投资决策参考**：结合经济数据选择资产配置
- **行业研究**：分析特定行业与宏观环境关系
- **学术研究**：获取真实经济数据进行建模分析
