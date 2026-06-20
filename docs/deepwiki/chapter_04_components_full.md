# 第4章 组件库系统

> "组件是UI的原子，好的组件库让复杂界面的构建如同搭积木般简单，同时保持视觉的一致性和体验的连贯性。"
>
> —— DeepWiki 设计哲学

---

## 目录

- [章节概述](#章节概述)
- [4.1 组件库架构总览 - 设计理念与分层体系](#41-组件库架构总览---设计理念与分层体系)
- [4.2 基础组件层 - 原子级UI单元](#42-基础组件层---原子级ui单元)
- [4.3 数据展示组件 - 信息可视化单元](#43-数据展示组件---信息可视化单元)
- [4.4 交互组件 - 用户交互单元](#44-交互组件---用户交互单元)
- [4.5 布局组件 - 页面结构单元](#45-布局组件---页面结构单元)
- [4.6 图表组件 - 数据可视化单元](#46-图表组件---数据可视化单元)
- [4.7 主题系统 - 视觉风格引擎](#47-主题系统---视觉风格引擎)
- [4.8 组件渲染机制 - 模板渲染与数据绑定](#48-组件渲染机制---模板渲染与数据绑定)
- [4.9 组件库的扩展与维护 - 规范与最佳实践](#49-组件库的扩展与维护---规范与最佳实践)
- [本章小结](#本章小结)

---

## 章节概述

组件库系统是 DeepWiki 投资研究系统 Pro 版 UI 的基石，提供可复用的 UI 组件，支撑整个系统的视觉一致性和开发效率。从 V1 时代的零散 HTML 片段，到 V2 时代的模板函数，再到 V3/V4 时代的面向对象组件体系，组件库经历了三代演进，最终形成了一套完整的、面向投资研究场景的专业组件库。

### 4.0.1 组件库的核心定位

组件库位于系统的"展现层"，是连接数据分析结果与用户视觉感知的桥梁：

```
┌─────────────────────────────────────────────────────────┐
│                     生成器层 (Generators)                │
│     日报 / 午报 / 盘后 / 持仓 / 题材 / 预警 / 周报       │
└───────────────────────────┬─────────────────────────────┘
                            │ 组装调用
┌───────────────────────────▼─────────────────────────────┐
│                     组件库层 (Components)                 │
│                                                           │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐ │
│  │ 基础组件 │  │ 数据展示 │  │ 交互组件 │  │ 布局组件 │ │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘ │
│                                                           │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐               │
│  │ 图表组件 │  │ 主题系统 │  │ 图标系统 │               │
│  └──────────┘  └──────────┘  └──────────┘               │
└───────────────────────────┬─────────────────────────────┘
                            │ 渲染输出
┌───────────────────────────▼─────────────────────────────┐
│                     最终 HTML 页面                        │
│          玻璃态设计 / 专业排版 / 响应式布局               │
└─────────────────────────────────────────────────────────┘
```

### 4.0.2 组件库的价值体现

组件库不仅仅是代码复用的工具，它承载着多重价值：

| 价值维度 | 具体体现 | 业务影响 |
|---------|---------|---------|
| **视觉一致性** | 统一的配色、间距、圆角、阴影规范 | 专业感、品牌识别 |
| **开发效率** | 一次开发、多处复用，避免重复造轮子 | 迭代速度提升 3-5 倍 |
| **质量保障** | 每个组件经过单独测试和优化 | 减少 Bug、提升稳定性 |
| **体验连贯** | 交互模式统一，降低用户学习成本 | 易用性提升、用户留存 |
| **主题切换** | 样式与结构分离，支持多主题 | 深色/浅色模式、定制化 |
| **响应式适配** | 内置多断点适配逻辑 | 移动端/平板/桌面端全覆盖 |

### 4.0.3 三代演进历程

DeepWiki 组件库经历了三个主要发展阶段：

**第一阶段：模板函数时代（V1-V2）**
- 以 Python 函数形式返回 HTML 字符串
- 函数命名随意，参数不统一
- 样式内联，难以维护和复用
- 代表：`render_stock_card()`、`render_section()`

**第二阶段：类组件时代（V3）**
- 引入 Component 基类，统一 `render()` 接口
- 组件按功能分类组织到不同模块
- 样式开始从内联向 CSS 类迁移
- 代表：`Section`、`Card`、`DataGrid`

**第三阶段：专业组件库时代（V3.5 Pro / V4）**
- 完整的主题系统（Pro 深色玻璃态 / V4 白底清爽）
- 专业投资业务组件（股票卡片、诊断面板、雷达图等）
- 动效系统、响应式系统、图标系统
- 代表：`V4StockCard`、`V4RadarChart`、`RiskAlert`

本章将深入剖析组件库的架构设计、核心组件实现、主题系统、渲染机制以及扩展规范，帮助读者全面理解这套专业投资研究界面的构建之道。

---

## 4.1 组件库架构总览 - 设计理念与分层体系

### 4.1.1 核心设计理念

DeepWiki 组件库的设计围绕五大核心理念展开，这些理念贯穿于每一个组件的实现细节中。

#### 理念一：内容与展现分离

> 组件只负责"如何展示"，不负责"展示什么"。数据由上层传入，组件专注于视觉呈现。

这一理念确保了组件的通用性——同一个 `DataCard` 组件既可以展示股票涨跌幅，也可以展示成交量、市盈率等任意指标。组件内部不包含业务逻辑，只接收 `title`、`value`、`trend` 等展示参数。

**技术权衡**：
- ✅ 优点：组件高度可复用，业务逻辑与 UI 解耦
- ⚠️ 代价：上层需要组装更多参数，调用代码相对冗长
- 💡 平衡：提供业务封装组件（如 `V4StockCard`）作为补充

#### 理念二：渐进式复杂度

> 简单场景用简单 API，复杂场景可深度定制。每个组件都有"默认配置"和"高级配置"两层接口。

以 `ProgressBar` 为例：
- 简单用法：`ProgressBar(value=75)` → 输出标准进度条
- 高级用法：可定制颜色、高度、标签、是否显示百分比、动画效果等

**技术权衡**：
- ✅ 优点：降低上手门槛，同时满足专业需求
- ⚠️ 代价：组件内部逻辑复杂度增加，需要处理多组默认值
- 💡 平衡：采用"配置对象 + 默认值合并"模式，核心逻辑清晰

#### 理念三：原子化与组合化

> 小组件可以组合成大组件，大组件可以拆分为小组件。组件之间是组合关系而非继承关系。

例如：
- `Badge`（徽章） → 嵌入 `Card` 的标题栏
- `DataCard` + `Sparkline` → 组成带趋势图的数据卡片
- 多个 `V4StockCard` → 组成持仓面板

**技术权衡**：
- ✅ 优点：灵活性高，组件可按需组合
- ⚠️ 代价：需要设计良好的组合接口，避免组件间强耦合
- 💡 平衡：组件输出纯 HTML 字符串，通过字符串拼接实现组合，简单高效

#### 理念四：面向投资场景优化

> 组件库不是通用 UI 库，而是深度面向投资研究场景的专业组件库。

这体现在大量的业务专用组件：
- 股票卡片（支持 A 股红涨绿跌习惯）
- 风险警示条（不同风险等级配色）
- 诊断维度面板（四维/六维诊断）
- 催化剂标签（热点题材标识）
- 市场情绪仪表盘

**技术权衡**：
- ✅ 优点：专业场景下开发效率极高，体验统一
- ⚠️ 代价：通用性降低，跨领域复用成本高
- 💡 平衡：基础组件保持通用，业务组件基于基础组件构建

#### 理念五：无障碍与可读性优先

> 投资研究是高强度阅读场景，信息密度与可读性的平衡至关重要。

设计原则：
- 字号梯度清晰（12px/13px/14px/16px/18px/24px）
- 行高宽松（1.5-1.6 倍）
- 色彩对比度符合 WCAG 标准
- 关键数据加粗高亮，辅助信息弱化处理

### 4.1.2 分层架构

组件库采用清晰的四层架构，每层职责明确，依赖关系自下而上：

```
┌──────────────────────────────────────────────────────┐
│  第四层：业务组件层 (Business Components)             │
│  V4StockCard · V4TopicCard · V4MarketOverview        │
│  BoyaBuyPointCard · RiskAlert · LhbCard              │
├──────────────────────────────────────────────────────┤
│  第三层：复合组件层 (Composite Components)            │
│  DataGrid · CardGrid · MetricsRow · KeyPoints        │
│  Tabs · SplitLayout · ChartCard                      │
├──────────────────────────────────────────────────────┤
│  第二层：基础组件层 (Base Components)                 │
│  Card · Badge · Button · ProgressBar · Section       │
│  DataCard · Sparkline · GaugeChart · Timeline        │
├──────────────────────────────────────────────────────┤
│  第一层：基础设施层 (Infrastructure)                 │
│  Component 基类 · 主题系统 · 图标系统 · 动效系统      │
│  响应式系统 · CSS 变量体系                           │
└──────────────────────────────────────────────────────┘
```

**各层职责说明**：

| 层级 | 职责 | 特点 | 依赖方向 |
|------|------|------|---------|
| **基础设施层** | 提供所有组件的基础能力 | 抽象、通用、无业务含义 | 被所有层依赖 |
| **基础组件层** | 原子级 UI 单元，单一功能 | 可独立使用，功能单一 | 依赖基础设施层 |
| **复合组件层** | 由基础组件组合而成，完成特定布局或展示模式 | 提供结构化的展示模式 | 依赖基础组件层 |
| **业务组件层** | 面向投资业务场景的专用组件 | 业务语义强，开箱即用 | 依赖复合组件层 + 基础组件层 |

### 4.1.3 统一接口规范

所有组件都继承自 `Component` 基类，遵循统一的接口规范：

```python
class Component:
    """组件基类 - 所有组件的统一接口"""
    
    def __init__(self, **kwargs):
        """构造函数 - 接收组件配置参数"""
        self.props = kwargs
    
    def render(self) -> str:
        """渲染组件为HTML字符串 - 子类必须实现"""
        raise NotImplementedError("子类必须实现 render 方法")
    
    def __str__(self) -> str:
        """字符串表示 - 直接返回渲染结果"""
        return self.render()
    
    def __add__(self, other):
        """支持组件相加拼接 - 方便组合使用"""
        if isinstance(other, Component):
            return self.render() + other.render()
        elif isinstance(other, str):
            return self.render() + other
        return NotImplemented
```

**代码佐证：Component 基类核心实现**

```python
# 文件: v3/components/base.py

class Component:
    """组件基类"""
    
    def __init__(self, **kwargs):
        self.props = kwargs
    
    def render(self) -> str:
        """渲染组件为HTML字符串"""
        raise NotImplementedError("子类必须实现 render 方法")
    
    def __str__(self) -> str:
        return self.render()
    
    def __add__(self, other):
        """支持组件相加拼接"""
        if isinstance(other, Component):
            return self.render() + other.render()
        elif isinstance(other, str):
            return self.render() + other
        return NotImplemented
```

**设计亮点**：
1. **`__str__` 魔法方法**：让组件可以直接插入字符串格式化表达式，如 `f"内容：{my_component}"`
2. **`__add__` 运算符重载**：支持 `component1 + component2` 的直观写法，降低组合成本
3. **纯字符串输出**：组件只输出 HTML 字符串，不依赖任何前端框架，可在任意 Python 环境中使用

### 4.1.4 模块组织

组件库的代码按功能模块组织，每个模块聚焦一类组件：

```
v3/components/
├── __init__.py          # 统一导出入口
├── base.py              # Component 基类 + 动效资源
├── layout.py            # 布局组件：Section, Card, Navbar, Footer 等
├── data.py              # 数据展示组件：DataCard, DataGrid, Badge 等
├── charts.py            # 图表组件：LineChart, BarChart, PieChart 等
├── special.py           # 特殊/交互组件：RiskAlert, Timeline, Tabs 等
├── icons.py             # SVG 图标系统
├── pro.py               # Pro 版专用组件（深色玻璃态）
├── v4_components.py     # V4 版专业组件库（白底清爽风）
└── v4_theme.py          # V4 主题配置与全局样式
```

**`__init__.py` 的导出设计**：

```python
# 文件: v3/components/__init__.py

from .base import Component, get_animation_assets, get_animation_css, get_animation_js
from .layout import Navbar, Footer, Section, Card, SubCard, CardGrid, DataTable, SplitLayout, ChartCard
from .data import (DataCard, DataGrid, CompareTable, MetricsRow, KeyPoints, StockTags, Badge, 
                   ProgressBar, Sparkline, GaugeChart, Tabs, StatCard)
from .charts import LineChart, BarChart, PieChart, get_chartjs_cdn
from .special import RiskAlert, QuoteBlock, Timeline, ButtonGroup, CatalystTag, NewsItem, SectionHeader

__all__ = [
    "Component", "get_animation_assets", "get_animation_css", "get_animation_js",
    "Navbar", "Footer", "Section", "Card", "SubCard", "CardGrid", "DataTable", "SplitLayout", "ChartCard",
    "DataCard", "DataGrid", "CompareTable", "MetricsRow", "KeyPoints", "StockTags", "Badge", 
    "ProgressBar", "Sparkline", "GaugeChart", "Tabs", "StatCard",
    "LineChart", "BarChart", "PieChart", "get_chartjs_cdn",
    "RiskAlert", "QuoteBlock", "Timeline", "ButtonGroup", "CatalystTag", "NewsItem", "SectionHeader",
]
```

**设计亮点**：统一导出入口使得上层代码只需 `from v3.components import Section, Card, DataGrid` 即可使用所有组件，无需关心内部模块划分。

### 4.1.5 两大主题体系

组件库支持两大并行的主题体系，分别面向不同的使用场景：

| 主题 | 风格描述 | 适用场景 | 核心文件 |
|------|---------|---------|---------|
| **Pro 深色玻璃态** | 紫色渐变背景 + 毛玻璃卡片 + 白色文字 | 专业投资者、大屏展示、夜间阅读 | `pro.py` |
| **V4 白底清爽风** | 纯白卡片 + 柔和阴影 + 深色文字 | 日常阅读、文档报告、日间使用 | `v4_components.py`、`v4_theme.py` |

两大主题共享组件架构，但在视觉表现上各有侧重：

```
        Component 基类
             │
     ┌───────┴───────┐
     ▼               ▼
V3 基础组件     V4 专业组件
 (layout.py)    (v4_components.py)
     │               │
     └───────┬───────┘
             ▼
    主题样式系统
       /    \
  Pro深色   V4白底
```

> 💡 **设计洞察**：为什么需要两套主题？
> 
> 投资研究产品的用户群体差异很大：专业交易员偏好深色界面（减少眼睛疲劳、数据更突出），而研究员和管理者偏好白底风格（适合长时间阅读、打印友好）。
> 两套主题体系覆盖了不同用户群体的使用习惯，同时共享核心组件逻辑，避免重复开发。

---

## 4.2 基础组件层 - 原子级 UI 单元

基础组件是组件库的"原子"，每个组件只负责一种单一的视觉功能。它们是构建更复杂组件的基石。

### 4.2.1 Badge 徽章组件

**功能定位**：用于标记状态、分类、等级等信息的小型标签组件。是使用频率最高的基础组件之一。

**核心实现**：

```python
# 文件: v3/components/data.py

class Badge(Component):
    """徽章/标签组件"""
    
    def __init__(self, text: str, variant: str = "default"):
        super().__init__()
        self.text = text
        self.variant = variant
    
    def render(self) -> str:
        variants = {
            "default": {"bg": "#f3f4f6", "color": "#374151"},
            "primary": {"bg": "linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%)", "color": "white"},
            "success": {"bg": "linear-gradient(135deg, #10b981 0%, #059669 100%)", "color": "white"},
            "warning": {"bg": "linear-gradient(135deg, #f59e0b 0%, #ea580c 100%)", "color": "white"},
            "danger": {"bg": "linear-gradient(135deg, #ef4444 0%, #dc2626 100%)", "color": "white"},
            "info": {"bg": "linear-gradient(135deg, #3b82f6 0%, #2563eb 100%)", "color": "white"},
            "purple": {"bg": "linear-gradient(135deg, #8b5cf6 0%, #7c3aed 100%)", "color": "white"},
        }
        
        v = variants.get(self.variant, variants["default"])
        
        return f'''
        <span style="display: inline-block; padding: 4px 12px; 
                    border-radius: 16px; font-size: 11px; font-weight: 700;
                    background: {v["bg"]}; color: {v["color"]};
                    letter-spacing: 0.3px; text-transform: uppercase;">
            {self.text}
        </span>
        '''
```

**设计亮点**：
1. **渐变背景**：所有彩色变体都采用 135° 线性渐变，比纯色更有质感
2. **字重与间距**：font-weight: 700 + letter-spacing: 0.3px，专业感强
3. **圆角适度**：16px 圆角（高度的一半），形成"药丸"形状，识别度高

**变体体系**：

| 变体 | 颜色 | 适用场景 | 示例 |
|------|------|---------|------|
| `default` | 灰色 | 普通标签、次要标记 | 「已发布」 |
| `primary` | 紫色渐变 | 主要分类、核心标签 | 「深度分析」 |
| `success` | 绿色渐变 | 正面消息、上涨、达标 | 「超预期」 |
| `warning` | 橙色渐变 | 警告、注意、中等风险 | 「需关注」 |
| `danger` | 红色渐变 | 危险、下跌、高风险 | 「高风险」 |
| `info` | 蓝色渐变 | 信息提示、中性说明 | 「数据来源」 |
| `purple` | 紫色渐变 | 主题色标签 | 「Pro 专属」 |

**技术权衡**：
- 采用内联样式而非 CSS 类，牺牲了一定的代码复用性，但换来了**无需外部依赖**、**即时渲染**的优势
- 对于 Badge 这种简单组件，内联样式的冗余度很低，完全在可接受范围内

### 4.2.2 Button 按钮组件

按钮是交互的核心入口。V4 组件库中的按钮组件体现了专业的设计考量。

**核心实现**：

```python
# 文件: v3/components/v4_components.py

class V4Button(V4Component):
    """按钮组件"""
    
    VARIANTS = {
        'primary': ('#8B5CF6', '#7C3AED', '#FFFFFF'),
        'secondary': ('#F3F4F6', '#E5E7EB', '#1F2937'),
        'success': ('#10B981', '#059669', '#FFFFFF'),
        'danger': ('#EF4444', '#DC2626', '#FFFFFF'),
        'outline': ('transparent', '#8B5CF6', '#8B5CF6'),
    }
    
    def __init__(self, text: str, variant: str = "primary", 
                 size: str = "md", href: str = None, 
                 class_name: str = "", icon: str = ""):
        super().__init__(class_name)
        self.text = text
        self.variant = variant
        self.size = size
        self.href = href
        self.icon = icon
        
        size_map = {
            'sm': 'padding: 6px 14px; font-size: 13px;',
            'md': 'padding: 10px 20px; font-size: 14px;',
            'lg': 'padding: 14px 28px; font-size: 16px;',
        }
        self.size_style = size_map.get(size, size_map['md'])
        
        bg, hover_bg, color = self.VARIANTS.get(variant, self.VARIANTS['primary'])
        self.bg = bg
        self.hover_bg = hover_bg
        self.color = color
    
    def render(self) -> str:
        style = f'{self.size_style} background: {self.bg}; color: {self.color};'
        base_class = f"v4-btn {self.class_name}".strip()
        
        icon_html = f'<span>{self.icon}</span>' if self.icon else ''
        content = f'{icon_html}<span>{self.text}</span>'
        
        if self.href:
            return f'<a href="{self.href}" class="{base_class}" style="{style}">{content}</a>'
        else:
            return f'<button class="{base_class}" style="{style}">{content}</button>'
```

**设计亮点**：
1. **多形态支持**：同时支持 `<a>` 链接和 `<button>` 按钮两种语义标签
2. **图标支持**：内置 icon 参数，方便快速构建带图标的按钮
3. **三档尺寸**：sm/md/lg 满足不同场景需求（表格内操作、表单提交、页面主按钮）

### 4.2.3 V4Tag 标签组件

V4 版的标签组件在 Badge 基础上进行了增强，提供了更丰富的变体和更专业的投资场景适配。

**核心实现**：

```python
# 文件: v3/components/v4_components.py

class V4Tag(V4Component):
    """标签组件 - 用于状态标记、分类标签等"""
    
    VARIANTS = {
        'primary': ('#8B5CF6', 'rgba(139, 92, 246, 0.1)'),
        'success': ('#10B981', 'rgba(16, 185, 129, 0.1)'),
        'warning': ('#F59E0B', 'rgba(245, 158, 11, 0.1)'),
        'danger': ('#EF4444', 'rgba(239, 68, 68, 0.1)'),
        'info': ('#3B82F6', 'rgba(59, 130, 246, 0.1)'),
        'gray': ('#6B7280', 'rgba(107, 114, 128, 0.1)'),
        'green': ('#10B981', 'rgba(16, 185, 129, 0.1)'),  # 涨
        'red': ('#EF4444', 'rgba(239, 68, 68, 0.1)'),      # 跌
        'blue': ('#3B82F6', 'rgba(59, 130, 246, 0.1)'),
        'orange': ('#F59E0B', 'rgba(245, 158, 11, 0.1)'),
        'purple': ('#8B5CF6', 'rgba(139, 92, 246, 0.1)'),
    }
```

**设计洞察**：注意到 `green` 和 `red` 变体的命名——这是面向 A 股市场的特殊设计。在国内投资场景中，红色代表上涨、绿色代表下跌，与国际惯例相反。组件库专门提供了 `green`/`red` 语义化变体，而不是使用 `up`/`down`，就是为了贴合国内用户的认知习惯。

### 4.2.4 HTMLComponent 包装组件

**功能定位**：将任意 HTML 字符串包装为 Component 实例，使其能够参与组件运算（如 `+` 拼接）。

**核心实现**：

```python
# 文件: v3/components/base.py

class HTMLComponent(Component):
    """纯HTML包装组件，直接返回HTML字符串"""
    
    def __init__(self, html: str):
        super().__init__()
        self.html = html
    
    def render(self) -> str:
        return self.html
```

**设计亮点**：这是一个典型的**适配器模式**应用，让第三方 HTML 或手写 HTML 能够无缝融入组件体系。当需要在组件之间插入自定义 HTML 时，只需 `HTMLComponent(custom_html)` 即可统一处理。

### 4.2.5 基础组件的设计原则

所有基础组件都遵循以下设计原则：

**原则一：单一职责**
> 每个组件只做一件事，做到极致。Badge 只负责展示标签，不承载点击交互（那是 Button 的事）。

**原则二：无状态**
> 基础组件是"纯函数"——给定相同的输入，永远产生相同的输出。不保存内部状态，不依赖外部上下文。

**原则三：可组合**
> 组件输出标准 HTML 字符串，可以任意拼接、嵌套，产生更复杂的 UI。

**原则四：可预测**
> 组件的行为是确定的，不会有意外的副作用（如自动添加全局 CSS、修改 DOM 等）。

这些原则确保了基础组件的稳定性和可复用性，是整个组件库大厦的牢固基石。

---

## 4.3 数据展示组件 - 信息可视化单元

数据展示组件是投资研究系统中使用最频繁的组件类型，负责将各类金融数据以清晰、直观的方式呈现给用户。

### 4.3.1 DataCard 数据卡片

**功能定位**：展示单个关键指标的卡片组件，是数据仪表盘的基本单元。

**核心实现**：

```python
# 文件: v3/components/data.py

class DataCard(Component):
    """精致数据卡片 - 展示关键指标
    升级为精美渐变设计，带图标、趋势指示
    """
    
    def __init__(self, title: str, value: str, trend: str = None, 
                 trend_up: bool = True, unit: str = "", 
                 icon: str = None, variant: str = "default",
                 subtitle: str = None):
        super().__init__()
        self.title = title
        self.value = value
        self.trend = trend
        self.trend_up = trend_up
        self.unit = unit
        self.icon = icon
        self.variant = variant
        self.subtitle = subtitle
    
    def render(self) -> str:
        # 趋势样式
        trend_color = "#10b981" if self.trend_up else "#ef4444"
        trend_icon = "↑" if self.trend_up else "↓"
        trend_html = f'''
        <div style="display: flex; align-items: center; color: {trend_color}; 
                    font-size: 13px; font-weight: 600; margin-top: 4px;">
            <span style="margin-right: 2px;">{trend_icon}</span>
            <span>{self.trend}</span>
        </div>
        ''' if self.trend else ''
        
        # 图标
        icon_html = ''
        if self.icon:
            from .icons import icon_svg
            icon_html = f'''
            <div style="width: 40px; height: 40px; 
                        background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%); 
                        border-radius: 12px; display: flex; align-items: center; 
                        justify-content: center; margin-bottom: 12px;">
                {icon_svg(self.icon, 20, "white")}
            </div>
            '''
        
        variants = {
            "default": {
                "bg": "white",
                "border": "rgba(0, 0, 0, 0.06)",
                "value_color": "#1f2937"
            },
            "primary": {
                "bg": "linear-gradient(135deg, #f0f4ff 0%, #f5f3ff 100%)",
                "border": "rgba(79, 70, 229, 0.1)",
                "value_color": "#4f46e5"
            },
            # ... 更多变体
        }
        
        v = variants.get(self.variant, variants["default"])
        
        subtitle_html = f'<div style="font-size: 12px; color: #9ca3af; margin-top: 2px;">{self.subtitle}</div>' if self.subtitle else ''
        
        return f'''
        <div style="background: {v["bg"]}; 
                    border: 1px solid {v["border"]};
                    border-radius: 16px; 
                    padding: 20px; 
                    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
                    transition: all 0.3s ease;
                    cursor: default;"
             onmouseover="this.style.transform='translateY(-2px)'; this.style.boxShadow='0 8px 24px rgba(0, 0, 0, 0.08)';"
             onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 2px 8px rgba(0, 0, 0, 0.04)';">
            {icon_html}
            <div style="font-size: 13px; color: #6b7280; margin-bottom: 6px;">
                {self.title}
            </div>
            <div style="font-size: 24px; font-weight: 700; color: {v["value_color"]}; line-height: 1.2;">
                {self.value}<span style="font-size: 13px; font-weight: 400; color: #9ca3af; margin-left: 2px;">{self.unit}</span>
            </div>
            {subtitle_html}
            {trend_html}
        </div>
        '''
```

**设计亮点**：

1. **分层视觉**：通过图标、标题、数值、副标题、趋势的纵向排列，形成清晰的信息层级
2. **悬停动效**：`onmouseover`/`onmouseout` 实现悬浮上浮效果，增强交互反馈
3. **单位弱化**：单位使用较小字号和灰色，避免干扰主数值的视觉重点
4. **趋势指示**：内置涨跌趋势展示，箭头 + 变色 + 文字，三重信息强化

**变体设计**：

| 变体 | 背景 | 适用场景 |
|------|------|---------|
| `default` | 纯白 | 常规数据展示，最常用 |
| `primary` | 紫色渐变 | 重点指标、核心数据 |
| `success` | 绿色渐变 | 正面数据、增长指标 |
| `warning` | 橙色渐变 | 警示数据、关注指标 |
| `danger` | 红色渐变 | 风险数据、下跌指标 |

> 💡 **设计洞察**：为什么 DataCard 的 variant 配色是"背景浅色渐变 + 文字深色"，而 Badge 是"背景深色渐变 + 文字白色"？
> 
> 这涉及到**信息密度**的考量：
> - Badge 是小尺寸元素，需要高对比度才能醒目，因此用深色背景
> - DataCard 是较大的信息容器，如果用深色背景，内部的标题、数值、副标题等多层文字会难以形成清晰的灰度层次
> - 浅色背景可以支持更丰富的文字灰度层级（主文字 #1f2937、次文字 #6b7280、辅助文字 #9ca3af）

### 4.3.2 ProgressBar 进度条组件

**功能定位**：以可视化方式展示百分比数据、完成度、风险度等连续型指标。

**核心实现**：

```python
# 文件: v3/components/data.py

class ProgressBar(Component):
    """渐变进度条组件 - 展示百分比数据"""
    
    def __init__(self, value: float, max_value: float = 100, 
                 label: str = None, show_percent: bool = True,
                 variant: str = "default", height: str = "8px"):
        super().__init__()
        self.value = value
        self.max_value = max_value
        self.label = label
        self.show_percent = show_percent
        self.variant = variant
        self.height = height
    
    def render(self) -> str:
        percent = min((self.value / self.max_value) * 100, 100)
        
        variants = {
            "default": "linear-gradient(90deg, #4f46e5 0%, #7c3aed 100%)",
            "success": "linear-gradient(90deg, #10b981 0%, #059669 100%)",
            "warning": "linear-gradient(90deg, #f59e0b 0%, #ea580c 100%)",
            "danger": "linear-gradient(90deg, #ef4444 0%, #dc2626 100%)",
            "rainbow": "linear-gradient(90deg, #ef4444 0%, #f59e0b 50%, #10b981 100%)",
        }
        
        gradient = variants.get(self.variant, variants["default"])
        
        label_html = ''
        if self.label:
            percent_html = f'<span style="font-weight: 600; color: #4f46e5;">{percent:.0f}%</span>' if self.show_percent else ''
            label_html = f'''
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                <span style="font-size: 13px; font-weight: 500; color: #374151;">{self.label}</span>
                {percent_html}
            </div>
            '''
        
        return f'''
        <div style="width: 100%;">
            {label_html}
            <div style="width: 100%; height: {self.height}; 
                        background: #f3f4f6; border-radius: 999px; 
                        overflow: hidden; box-shadow: inset 0 1px 2px rgba(0,0,0,0.06);">
                <div style="width: {percent}%; height: 100%; 
                            background: {gradient};
                            border-radius: 999px; 
                            transition: width 1s ease-out;
                            box-shadow: 0 1px 3px rgba(0,0,0,0.1);">
                </div>
            </div>
        </div>
        '''
```

**设计亮点**：

1. **彩虹变体**：`rainbow` 变体从红到黄到绿，特别适合展示风险等级、评分等有"好坏"方向性的指标
2. **内阴影增强质感**：轨道使用 `inset` 内阴影，营造凹陷感，让进度条更有立体感
3. **平滑过渡动画**：`transition: width 1s ease-out` 实现进度条平滑增长的动画效果

**rainbow 变体的应用场景**：
- 风险指数：0%（低风险/绿色）→ 100%（高风险/红色）
- 综合评分：低分红色 → 高分绿色
- 估值分位：低估（绿色）→ 高估（红色）

### 4.3.3 Sparkline 迷你趋势图

**功能定位**：纯 SVG 实现的小型折线图，用于在紧凑空间内展示数据趋势。

**核心实现**：

```python
# 文件: v3/components/data.py

class Sparkline(Component):
    """迷你趋势图组件 - 纯SVG实现的小型折线图"""
    
    def __init__(self, data: list, width: int = 120, height: int = 40,
                 color: str = "#4f46e5", fill: bool = True,
                 stroke_width: int = 2):
        super().__init__()
        self.data = data
        self.width = width
        self.height = height
        self.color = color
        self.fill = fill
        self.stroke_width = stroke_width
    
    def render(self) -> str:
        if not self.data:
            return '<div style="width: {width}px; height: {height}px;"></div>'
        
        min_val = min(self.data)
        max_val = max(self.data)
        range_val = max_val - min_val if max_val != min_val else 1
        
        padding = self.stroke_width
        graph_width = self.width - padding * 2
        graph_height = self.height - padding * 2
        
        # 生成路径点
        points = []
        step = graph_width / (len(self.data) - 1) if len(self.data) > 1 else graph_width
        
        for i, val in enumerate(self.data):
            x = padding + i * step
            y = padding + graph_height - ((val - min_val) / range_val) * graph_height
            points.append((x, y))
        
        # 生成折线路径
        path_d = f"M {points[0][0]:.1f} {points[0][1]:.1f}"
        for i in range(1, len(points)):
            path_d += f" L {points[i][0]:.1f} {points[i][1]:.1f}"
        
        # 生成填充区域路径
        fill_d = ''
        if self.fill:
            fill_d = path_d + f" L {points[-1][0]:.1f} {padding + graph_height:.1f} L {points[0][0]:.1f} {padding + graph_height:.1f} Z"
        
        fill_color = self.color.replace(')', ', 0.1)').replace('rgb', 'rgba')
        if '#' in self.color:
            fill_color = self.color + '1A'  # 10% 透明度
        
        return f'''
        <svg width="{self.width}" height="{self.height}" viewBox="0 0 {self.width} {self.height}" style="display: block;">
            {'<path d="' + fill_d + '" fill="' + fill_color + '" />' if self.fill else ''}
            <path d="{path_d}" fill="none" stroke="{self.color}" stroke-width="{self.stroke_width}" stroke-linecap="round" stroke-linejoin="round" />
        </svg>
        '''
```

**设计亮点**：

1. **纯 SVG 无依赖**：不依赖 Chart.js 等外部库，直接输出 SVG，加载快、渲染清晰
2. **面积填充**：折线下方半透明填充，比单纯的折线更有视觉分量
3. **自动缩放**：自动根据数据范围计算 Y 轴坐标，充分利用显示空间
4. **性能优秀**：几十条数据的 SVG 图只有几百字节，远小于 PNG 图片

**技术权衡**：
- ✅ 优点：轻量、清晰、无依赖、可缩放
- ⚠️ 局限：功能有限，只适合简单趋势展示；不支持交互（tooltip 等）
- 💡 适用场景：数据卡片内的小趋势图、表格内嵌趋势、移动端展示

### 4.3.4 GaugeChart 仪表盘组件

**功能定位**：环形仪表盘，用于展示指数、评分、风险度等有明确范围的指标。

**核心实现**：

```python
# 文件: v3/components/data.py

class GaugeChart(Component):
    """仪表盘组件 - SVG环形仪表盘，展示指数类数据"""
    
    def __init__(self, value: float, max_value: float = 100,
                 label: str = "", size: int = 100, stroke_width: int = 8,
                 color: str = None, show_value: bool = True):
        super().__init__()
        self.value = min(value, max_value)
        self.max_value = max_value
        self.label = label
        self.size = size
        self.stroke_width = stroke_width
        self.show_value = show_value
        
        # 根据数值自动变色
        if color is None:
            percent = value / max_value
            if percent >= 0.8:
                self.color = "#ef4444"  # 红色 - 高风险
            elif percent >= 0.6:
                self.color = "#f59e0b"  # 黄色 - 中等
            elif percent >= 0.4:
                self.color = "#3b82f6"  # 蓝色 - 正常
            else:
                self.color = "#10b981"  # 绿色 - 低风险
        else:
            self.color = color
    
    def render(self) -> str:
        # ... SVG 路径计算 ...
        return f'''
        <div style="text-align: center;">
            <div style="position: relative; width: {self.size}px; height: {self.size}px; margin: 0 auto;">
                <svg width="{self.size}" height="{self.size}" viewBox="0 0 {self.size} {self.size}">
                    <!-- 背景弧 -->
                    <path d="..." fill="none" stroke="#f3f4f6" stroke-width="{self.stroke_width}" stroke-linecap="round" />
                    <!-- 前景弧 -->
                    <path d="..." fill="none" stroke="{self.color}" stroke-width="{self.stroke_width}" stroke-linecap="round" style="filter: drop-shadow(0 2px 4px {self.color}40);" />
                </svg>
                {value_html}
            </div>
            {'<div style="font-size: 12px; color: #6b7280; margin-top: 4px;">' + self.label + '</div>' if self.label else ''}
        </div>
        '''
```

**设计亮点**：
1. **智能配色**：根据数值自动选择颜色（绿→蓝→黄→红），无需调用方判断
2. **发光效果**：使用 `drop-shadow` 滤镜给前景弧添加同色系发光，增强视觉冲击力
3. **270° 弧设计**：不是完整的圆，而是从左下到右下的 270° 弧，顶部留出标签空间，更符合仪表盘的视觉习惯

### 4.3.5 MetricsRow 指标行

**功能定位**：在一行内并列展示多个关键指标，充分利用横向空间。

**核心实现**：

```python
# 文件: v3/components/data.py

class MetricsRow(Component):
    """指标行 - 一行展示多个指标"""
    
    def __init__(self, metrics: list):
        super().__init__()
        self.metrics = metrics  # [(label, value, trend_up?), ...]
    
    def render(self) -> str:
        items_html = ""
        for i, metric in enumerate(self.metrics):
            label = metric[0]
            value = metric[1]
            trend_up = metric[2] if len(metric) > 2 else None
            
            trend_html = ""
            if trend_up is not None:
                trend_color = "#10b981" if trend_up else "#ef4444"
                trend_icon = "↑" if trend_up else "↓"
                trend_html = f'<span style="color: {trend_color}; font-size: 12px; margin-left: 4px; font-weight: 600;">{trend_icon}</span>'
            
            # 分隔线（最后一个不加）
            border_style = "" if i == len(self.metrics) - 1 else 'border-right: 1px solid #f3f4f6;'
            
            items_html += f'''
                <div style="flex: 1; text-align: center; padding: 0 12px; {border_style}">
                    <div style="font-size: 20px; font-weight: 700; color: #1f2937;">
                        {value}
                        {trend_html}
                    </div>
                    <div style="font-size: 12px; color: #6b7280; margin-top: 4px;">{label}</div>
                </div>
            '''
        
        return f'''
        <div style="background: white; border-radius: 16px; 
                    padding: 20px 12px; border: 1px solid rgba(0, 0, 0, 0.06);
                    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
                    display: flex; align-items: center;">
            {items_html}
        </div>
        '''
```

**设计亮点**：
1. **分割线设计**：指标之间用细竖线分隔，清晰但不突兀
2. **弹性布局**：使用 `flex: 1` 平均分配宽度，自动适配不同数量的指标
3. **趋势可选**：每个指标可以选择性地显示涨跌趋势，灵活适配不同场景

### 4.3.6 DataGrid 数据网格

**功能定位**：将多个 DataCard 按网格排列，形成数据看板。

**核心实现**：

```python
# 文件: v3/components/data.py

class DataGrid(Component):
    """数据卡片网格 - 展示多个数据卡片"""
    
    def __init__(self, cards: list, cols: int = 4, gap: str = "16px"):
        super().__init__()
        self.cards = cards
        self.cols = cols
        self.gap = gap
    
    def render(self) -> str:
        cards_html = "".join(
            f'<div style="flex: 1; min-width: 0;">{card.render() if hasattr(card, "render") else str(card)}</div>'
            for card in self.cards
        )
        
        return f'''
        <div style="display: flex; gap: {self.gap}; flex-wrap: wrap;">
            {cards_html}
        </div>
        '''
```

**设计洞察**：注意 DataGrid 使用的是 `flex` 布局而非 `grid` 布局。这是一个有意的选择：
- Flex 布局的 `flex-wrap: wrap` 可以自动处理响应式换行
- 相比 `grid-template-columns: repeat(N, 1fr)`，flex 在卡片数量不能被列数整除时，最后一行的卡片不会被拉伸
- `min-width: 0` 是一个关键细节，防止 flex 子项内容溢出时破坏布局

### 4.3.7 CompareTable 对比表格

**功能定位**：多列数据对比展示，支持高亮行、高亮列、斑马纹等高级特性。

**核心实现**：

```python
# 文件: v3/components/data.py

class CompareTable(Component):
    """对比表格 - 多列数据对比"""
    
    def __init__(self, headers: list, rows: list, 
                 highlight_rows: list = None, 
                 highlight_col: int = None,
                 striped: bool = True):
        super().__init__()
        self.headers = headers
        self.rows = rows
        self.highlight_rows = highlight_rows or []
        self.highlight_col = highlight_col
        self.striped = striped
    
    def render(self) -> str:
        # 表头
        headers_html = "".join(
            f'<th style="padding: 14px 16px; text-align: left; font-size: 12px; font-weight: 600; color: #6b7280; text-transform: uppercase; letter-spacing: 0.5px; background: #f9fafb;">{h}</th>'
            for h in self.headers
        )
        
        # 表行
        rows_html = ""
        for i, row in enumerate(self.rows):
            highlight = i in self.highlight_rows
            row_bg = "rgba(79, 70, 229, 0.04)" if highlight else ("white" if i % 2 == 0 or not self.striped else "#fafafa")
            
            cells_html = ""
            for j, cell in enumerate(row):
                cell_style = ""
                if self.highlight_col is not None and j == self.highlight_col:
                    cell_style = "font-weight: 600; color: #4f46e5;"
                
                cells_html += '<td style="padding: 14px 16px; font-size: 13px; color: #374151; ' + cell_style + '">' + str(cell) + '</td>'
            
            rows_html += '<tr style="background: ' + row_bg + '; transition: background 0.2s;">' + cells_html + '</tr>'
        
        return f'''
        <div style="overflow-x: auto; border-radius: 16px; 
                    border: 1px solid rgba(0, 0, 0, 0.06); 
                    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);">
            <table style="width: 100%; border-collapse: collapse;">
                <thead>
                    <tr style="border-bottom: 1px solid #e5e7eb;">
                        {headers_html}
                    </tr>
                </thead>
                <tbody>
                    {rows_html}
                </tbody>
            </table>
        </div>
        '''
```

**设计亮点**：
1. **表头大写**：`text-transform: uppercase` + `letter-spacing: 0.5px`，专业感极强
2. **斑马纹可选**：`striped` 参数控制是否启用斑马纹，适应不同密度的数据
3. **多重高亮**：支持行高亮（重点行）和列高亮（关键列），可组合使用
4. **横向滚动**：`overflow-x: auto` 确保在窄屏设备上表格可横向滚动而不破坏布局

---

## 4.4 交互组件 - 用户交互单元

交互组件负责处理用户操作，提供反馈和引导，是用户体验的关键组成部分。

### 4.4.1 Tabs 标签页组件

**功能定位**：在有限空间内展示多组内容，通过标签切换实现内容的分类展示。

**核心实现**：

```python
# 文件: v3/components/data.py

class Tabs(Component):
    """标签页组件 - 支持切换多个内容面板"""
    
    def __init__(self, tabs: list, default_index: int = 0):
        super().__init__()
        self.tabs = tabs  # [(label, content), ...]
        self.default_index = default_index
    
    def render(self) -> str:
        import random
        tab_id = f"tabs_{random.randint(10000, 99999)}"
        
        # 标签按钮
        tab_buttons = ""
        for i, (label, _) in enumerate(self.tabs):
            active_style = ""
            if i == self.default_index:
                active_style = """
                    background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%);
                    color: white;
                    box-shadow: 0 2px 8px rgba(79, 70, 229, 0.3);
                """
            else:
                active_style = """
                    background: transparent;
                    color: #6b7280;
                """
            
            tab_buttons += f'''
            <button class="tab-btn" 
                    style="padding: 10px 20px; border: none; border-radius: 10px;
                           font-size: 13px; font-weight: 600; cursor: pointer;
                           transition: all 0.3s ease; {active_style}"
                    onclick="switchTab_{tab_id}({i})">
                {label}
            </button>
            '''
        
        # 内容面板
        tab_panels = ""
        for i, (_, content) in enumerate(self.tabs):
            display_style = "block" if i == self.default_index else "none"
            content_html = content.render() if hasattr(content, "render") else str(content)
            tab_panels += f'''
            <div class="tab-panel" id="{tab_id}_panel_{i}" style="display: {display_style}; padding-top: 20px;">
                {content_html}
            </div>
            '''
        
        # JavaScript
        js_script = f'''
        <script>
        function switchTab_{tab_id}(index) {{
            const container = document.getElementById("{tab_id}");
            const buttons = container.querySelectorAll(".tab-btn");
            const panels = container.querySelectorAll(".tab-panel");
            
            buttons.forEach((btn, i) => {{
                if (i === index) {{
                    btn.style.background = "linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%)";
                    btn.style.color = "white";
                    btn.style.boxShadow = "0 2px 8px rgba(79, 70, 229, 0.3)";
                }} else {{
                    btn.style.background = "transparent";
                    btn.style.color = "#6b7280";
                    btn.style.boxShadow = "none";
                }}
            }});
            
            panels.forEach((panel, i) => {{
                panel.style.display = i === index ? "block" : "none";
            }});
        }}
        </script>
        '''
        
        return f'''
        <div id="{tab_id}" style="width: 100%;">
            <div style="display: flex; gap: 8px; padding: 4px; 
                        background: #f3f4f6; border-radius: 12px; flex-wrap: wrap;">
                {tab_buttons}
            </div>
            {tab_panels}
            {js_script}
        </div>
        '''
```

**设计亮点**：

1. **胶囊式标签栏**：标签按钮放在一个圆角容器内，激活态使用渐变填充，视觉效果精致
2. **自包含 JS**：组件自带 JavaScript 交互逻辑，无需外部依赖
3. **唯一 ID 机制**：使用随机数生成唯一 ID，确保页面内多个 Tabs 组件互不干扰
4. **内容多态**：tab 内容可以是字符串，也可以是任意 Component 实例，灵活组合

**技术权衡**：
- ✅ 优点：自包含、不依赖外部 JS 库、使用简单
- ⚠️ 代价：JS 代码随 HTML 重复输出，页面有多个 Tabs 时会有一定冗余
- 💡 平衡：JS 代码量很小（每个约 500 字节），冗余代价可以接受；未来可优化为公共函数

### 4.4.2 RiskAlert 风险提示组件

**功能定位**：醒目展示风险提示、警告信息，是投资场景中非常重要的信息传达组件。

**核心实现**：

```python
# 文件: v3/components/special.py

class RiskAlert(Component):
    """风险提示组件"""
    
    def __init__(self, text: str, level: str = "warning", title: str = None):
        super().__init__()
        self.text = text
        self.level = level
        self.title = title or "风险提示"
    
    def render(self) -> str:
        levels = {
            "warning": {
                "bg": "linear-gradient(135deg, #fffbeb 0%, #fef3c7 100%)",
                "border": "rgba(245, 158, 11, 0.2)",
                "icon": "⚠️",
                "title_color": "#92400e",
                "text_color": "#b45309",
            },
            "danger": {
                "bg": "linear-gradient(135deg, #fef2f2 0%, #fee2e2 100%)",
                "border": "rgba(239, 68, 68, 0.2)",
                "icon": "🚨",
                "title_color": "#991b1b",
                "text_color": "#b91c1c",
            },
            "info": {
                "bg": "linear-gradient(135deg, #eff6ff 0%, #dbeafe 100%)",
                "border": "rgba(59, 130, 246, 0.2)",
                "icon": "ℹ️",
                "title_color": "#1e40af",
                "text_color": "#1d4ed8",
            },
        }
        
        v = levels.get(self.level, levels["warning"])
        
        return f'''
        <div style="background: {v["bg"]}; 
                    border: 1px solid {v["border"]};
                    border-radius: 14px; 
                    padding: 18px 20px;
                    margin: 16px 0;">
            <div style="display: flex; align-items: flex-start;">
                <span style="font-size: 20px; margin-right: 12px; flex-shrink: 0; margin-top: -2px;">
                    {v["icon"]}
                </span>
                <div style="flex: 1;">
                    <div style="font-weight: 600; color: {v["title_color"]}; 
                               font-size: 14px; margin-bottom: 6px;">
                        {self.title}
                    </div>
                    <div style="color: {v["text_color"]}; 
                               font-size: 13px; line-height: 1.6;">
                        {self.text}
                    </div>
                </div>
            </div>
        </div>
        '''
```

**设计亮点**：
1. **三档风险等级**：info（信息提示）/ warning（警告）/ danger（危险），色彩区分明确
2. **左对齐图标 + 顶部微偏移**：图标 `margin-top: -2px` 让视觉重心与标题文字对齐，细节精致
3. **渐变背景**：135° 线性渐变让背景不单调，比纯色更有层次感
4. **适度的 margin**：上下 16px 外边距，确保在文档流中自然分隔

### 4.4.3 Timeline 时间线组件

**功能定位**：按时间顺序展示事件发展历程，适合公告时间线、事件推演、历史回顾等场景。

**核心实现**：

```python
# 文件: v3/components/special.py

class Timeline(Component):
    """时间线组件 - 展示重要事件时间线"""
    
    def __init__(self, items: list):
        super().__init__()
        self.items = items  # [{time, title, content, type}]
    
    def render(self) -> str:
        type_colors = {
            "primary": "#4f46e5",
            "success": "#10b981",
            "warning": "#f59e0b",
            "danger": "#ef4444",
            "info": "#3b82f6",
        }
        
        items_html = ""
        for i, item in enumerate(self.items):
            item_type = item.get("type", "primary")
            color = type_colors.get(item_type, type_colors["primary"])
            is_last = i == len(self.items) - 1
            
            line_html = ''
            if not is_last:
                line_html = f'''
                <div style="position: absolute; left: 9px; top: 28px; 
                           width: 2px; height: calc(100% - 8px); 
                           background: linear-gradient(to bottom, {color}, #e5e7eb);">
                </div>
                '''
            
            items_html += f'''
            <div style="position: relative; padding-left: 32px; padding-bottom: 24px;">
                {line_html}
                <div style="position: absolute; left: 0; top: 4px; 
                           width: 20px; height: 20px; 
                           background: {color};
                           border-radius: 50%;
                           border: 3px solid white;
                           box-shadow: 0 2px 8px rgba(0, 0, 0, 0.15);
                           z-index: 1;">
                </div>
                <div style="font-size: 12px; color: #6b7280; font-weight: 500; 
                           margin-bottom: 4px;">
                    {item.get("time", "")}
                </div>
                <div style="font-size: 15px; font-weight: 600; color: #1f2937; 
                           margin-bottom: 6px;">
                    {item.get("title", "")}
                </div>
                <div style="font-size: 13px; color: #6b7280; line-height: 1.6;">
                    {item.get("content", "")}
                </div>
            </div>
            '''
        
        return f'''
        <div style="padding: 8px 0;">
            {items_html}
        </div>
        '''
```

**设计亮点**：
1. **渐变连接线**：时间线不是纯色，而是从上到下由深变浅的渐变，细节精致
2. **节点投影**：时间节点使用 `box-shadow` 添加投影，营造悬浮感
3. **三色边框**：节点是彩色圆 + 白色边框 + 外部投影，三层结构立体感强
4. **最后一项无连接线**：`is_last` 判断确保时间线在最后一项终止，视觉完整

### 4.4.4 QuoteBlock 引用块

**功能定位**：突出展示重要观点、金句、专家言论等引用内容。

**核心实现**：

```python
# 文件: v3/components/special.py

class QuoteBlock(Component):
    """引用块 - 用于引用重要观点或金句"""
    
    def __init__(self, text: str, author: str = None, source: str = None):
        super().__init__()
        self.text = text
        self.author = author
        self.source = source
    
    def render(self) -> str:
        author_html = ""
        if self.author:
            source_text = f' · {self.source}' if self.source else ''
            author_html = f'''
            <div style="text-align: right; font-size: 13px; color: #9ca3af; 
                       margin-top: 12px; font-style: italic;">
                —— {self.author}{source_text}
            </div>
            '''
        
        return f'''
        <div style="background: linear-gradient(135deg, #faf5ff 0%, #f5f3ff 100%); 
                    border-left: 4px solid #8b5cf6;
                    border-radius: 0 12px 12px 0; 
                    padding: 20px 24px;
                    margin: 16px 0;">
            <div style="font-size: 15px; color: #581c87; line-height: 1.8; 
                       font-weight: 500; font-style: italic;">
                "{self.text}"
            </div>
            {author_html}
        </div>
        '''
```

**设计亮点**：
1. **左边框强调**：4px 紫色左边框是引用块的标志性设计，在文字流中非常醒目
2. **斜体字重**：`font-style: italic + font-weight: 500`，斜体但不飘，有分量感
3. **右下对齐署名**：作者信息右对齐，符合引用格式的传统习惯

### 4.4.5 ButtonGroup 按钮组

**功能定位**：将一组操作按钮组织在一起，提供统一的间距和对齐方式。

**核心实现**：

```python
# 文件: v3/components/special.py

class ButtonGroup(Component):
    """按钮组组件 - 用于操作按钮组"""
    
    def __init__(self, buttons: list = None):
        super().__init__()
        self.buttons = buttons or []  # [{"text": "按钮", "url": "#", "variant": "primary"}, ...]
    
    def render(self) -> str:
        buttons_html = ""
        for btn in self.buttons:
            variant = btn.get("variant", "default")
            text = btn.get("text", "")
            url = btn.get("url", "#")
            
            variants = {
                "primary": "background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%); color: white;",
                "success": "background: linear-gradient(135deg, #10b981 0%, #059669 100%); color: white;",
                "warning": "background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%); color: white;",
                "danger": "background: linear-gradient(135deg, #ef4444 0%, #dc2626 100%); color: white;",
                "default": "background: #f3f4f6; color: #374151;",
            }
            
            style = variants.get(variant, variants["default"])
            
            buttons_html += f'''
            <a href="{url}" style="
                display: inline-block;
                padding: 10px 20px;
                border-radius: 10px;
                font-size: 14px;
                font-weight: 500;
                text-decoration: none;
                {style}
                transition: all 0.2s ease;
                margin-right: 8px;
            " onmouseover="this.style.opacity='0.9'; this.style.transform='translateY(-1px)';"
               onmouseout="this.style.opacity='1'; this.style.transform='translateY(0)';">
                {text}
            </a>
            '''
        
        return f'''
        <div style="display: flex; align-items: center; flex-wrap: wrap; gap: 8px;">
            {buttons_html}
        </div>
        '''
```

**设计洞察**：ButtonGroup 虽然简单，但体现了组件库的一个重要设计原则——**即使是简单的组合模式，也应该封装为组件**。如果没有 ButtonGroup，每个页面都要手写 `flex` 布局和 `gap` 间距，既繁琐又容易不一致。

### 4.4.6 NewsItem 新闻条目

**功能定位**：列表形式展示新闻、公告、资讯等内容。

**核心实现**：

```python
# 文件: v3/components/special.py

class NewsItem(Component):
    """新闻条目组件 - 用于新闻列表"""
    
    def __init__(self, title: str, content: str = None, 
                 time: str = None, source: str = None,
                 tag: str = None, tag_variant: str = "default",
                 important: bool = False):
        super().__init__()
        self.title = title
        self.content = content
        self.time = time
        self.source = source
        self.tag = tag
        self.tag_variant = tag_variant
        self.important = important
    
    def render(self) -> str:
        from .data import Badge
        
        tag_html = ""
        if self.tag:
            tag_html = f'<div style="margin-right: 10px;">{Badge(self.tag, self.tag_variant).render()}</div>'
        
        meta_html = ""
        if self.time or self.source:
            parts = []
            if self.time:
                parts.append(self.time)
            if self.source:
                parts.append(self.source)
            meta_html = f'''
            <div style="font-size: 12px; color: #9ca3af; margin-top: 6px;">
                {" · ".join(parts)}
            </div>
            '''
        
        content_html = ""
        if self.content:
            content_html = f'''
            <div style="font-size: 13px; color: #6b7280; line-height: 1.6; 
                       margin-top: 8px;">
                {self.content}
            </div>
            '''
        
        title_weight = "700" if self.important else "600"
        title_color = "#1f2937" if self.important else "#374151"
        
        return f'''
        <div style="padding: 14px 16px; 
                    border-radius: 12px;
                    background: #fafafa;
                    margin-bottom: 10px;
                    transition: all 0.2s ease;"
             onmouseover="this.style.background='#f5f5f5';"
             onmouseout="this.style.background='#fafafa';">
            <div style="display: flex; align-items: flex-start;">
                {tag_html}
                <div style="flex: 1; min-width: 0;">
                    <div style="font-size: 14px; font-weight: {title_weight}; 
                               color: {title_color}; line-height: 1.5;">
                        {self.title}
                    </div>
                    {content_html}
                    {meta_html}
                </div>
            </div>
        </div>
        '''
```

**设计亮点**：
1. **重要性区分**：`important` 参数控制标题字重和颜色，重要新闻更醒目
2. **标签 + 内容的左对齐布局**：标签在左，内容在右，形成清晰的两栏结构
3. **元信息分隔符**：使用 ` · `（中间点）作为时间和来源的分隔符，是新闻类 UI 的经典设计
4. **悬停反馈**：背景色微变，提供轻量的交互反馈

---

## 4.5 布局组件 - 页面结构单元

布局组件负责页面的整体结构组织，是页面骨架的构建工具。

### 4.5.1 Section 章节组件

**功能定位**：页面的主要内容区块，每个 Section 代表一个独立的内容主题，带标题、图标和内容区域。

**核心实现**：

```python
# 文件: v3/components/layout.py

class Section(Component):
    """章节组件 - 用于分隔内容区域
    带精致的标题图标和渐变设计
    """
    
    def __init__(self, title: str = "", content=None, 
                 icon: str = None, variant: str = "default",
                 subtitle: str = None, extra=None):
        super().__init__()
        self.title = title
        self.content = content
        self.icon = icon
        self.variant = variant
        self.subtitle = subtitle
        self.extra = extra  # 右侧额外内容，如徽章等
    
    def render(self) -> str:
        # 标题区域
        title_html = ""
        if self.title:
            from .icons import icon_svg
            
            icon_html = ""
            if self.icon:
                icon_html = f'''
                <div style="width: 40px; height: 40px; 
                            background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%); 
                            border-radius: 12px; display: flex; align-items: center; 
                            justify-content: center; margin-right: 14px; flex-shrink: 0;
                            box-shadow: 0 4px 12px rgba(79, 70, 229, 0.3);">
                    {icon_svg(self.icon, 20, "white")}
                </div>
                '''
            
            subtitle_html = f'''
            <div style="font-size: 13px; color: #9ca3af; margin-top: 2px; font-weight: 400;">
                {self.subtitle}
            </div>
            ''' if self.subtitle else ''
            
            extra_html = f'<div style="margin-left: auto;">{self.extra.render() if hasattr(self.extra, "render") else self.extra}</div>' if self.extra else ''
            
            title_html = f'''
            <div style="display: flex; align-items: center; margin-bottom: 20px;">
                {icon_html}
                <div style="flex: 1; min-width: 0;">
                    <h2 style="font-size: 20px; font-weight: 700; color: #1f2937; 
                               margin: 0; line-height: 1.3;">
                        {self.title}
                    </h2>
                    {subtitle_html}
                </div>
                {extra_html}
            </div>
            '''
        
        # 内容
        content_html = ""
        if self.content is not None:
            if hasattr(self.content, 'render'):
                content_html = self.content.render()
            else:
                content_html = str(self.content)
        
        # 变体样式
        variants = {
            "default": {
                "bg": "white",
                "padding": "28px",
                "border": "1px solid rgba(0, 0, 0, 0.06)",
                "radius": "20px",
                "shadow": "0 4px 16px rgba(0, 0, 0, 0.04), 0 1px 0 rgba(255, 255, 255, 0.8) inset, 0 -1px 0 rgba(0, 0, 0, 0.02) inset",
                "title_color": "#1f2937",
            },
            "highlight": {
                "bg": "linear-gradient(135deg, #f0f4ff 0%, #f5f3ff 100%)",
                "padding": "28px",
                "border": "1px solid rgba(79, 70, 229, 0.1)",
                "radius": "20px",
                "shadow": "0 4px 16px rgba(79, 70, 229, 0.08), 0 1px 0 rgba(255, 255, 255, 0.6) inset",
                "title_color": "#1f2937",
            },
            "dark": {
                "bg": "linear-gradient(135deg, rgba(15, 23, 42, 0.95) 0%, rgba(30, 41, 59, 0.95) 100%)",
                "padding": "28px",
                "border": "1px solid rgba(255, 255, 255, 0.1)",
                "radius": "20px",
                "shadow": "0 8px 32px rgba(0, 0, 0, 0.3), 0 1px 0 rgba(255, 255, 255, 0.05) inset",
                "title_color": "white",
            },
            "subtle": {
                "bg": "transparent",
                "padding": "0",
                "border": "none",
                "radius": "0",
                "shadow": "none",
                "title_color": "#1f2937",
            },
        }
        
        v = variants.get(self.variant, variants["default"])
        
        # 更新标题颜色
        if self.title:
            title_html = title_html.replace(
                'color: #1f2937;',
                f'color: {v["title_color"]};'
            )
        
        return f'''
        <section style="margin-bottom: 32px;">
            {title_html}
            <div style="background: {v["bg"]}; 
                        padding: {v["padding"]}; 
                        border: {v["border"]};
                        border-radius: {v["radius"]};
                        box-shadow: {v["shadow"]};">
                {content_html}
            </div>
        </section>
        '''
```

**设计亮点**：

1. **图标 + 标题 + 副标题 + 额外内容**的四栏标题栏，信息层次丰富
2. **图标渐变背景 + 投影**：图标不是简单的平铺贴图，而是有渐变背景和柔和投影，视觉层次分明
3. **四档变体**：
   - `default`：白底卡片，最常用
   - `highlight`：浅紫渐变，用于重点章节
   - `dark`：深色模式，用于强调或对比
   - `subtle`：无背景，仅标题 + 内容，适合嵌入其他容器

4. **双层阴影**：`default` 变体的阴影使用了三层阴影（外阴影 + 上内高光 + 下内阴影），模拟了物理世界的光照效果，质感细腻

> 💡 **设计洞察**：为什么 Section 的 `shadow` 属性这么复杂？
> 
> 这是拟物化设计的一种现代演绎。真实世界中，物体受到光照会产生：
> 1. 下方的投影（外阴影）
> 2. 顶部的高光（上内阴影 - 亮）
> 3. 底部的暗部（下内阴影 - 暗）
> 
> 三层阴影组合起来，就能营造出"卡片是凸起的、受光的"立体错觉，让界面不再扁平。这是专业设计与业余设计的重要区别之一。

### 4.5.2 Card 卡片组件

**功能定位**：通用内容容器，是最基础的布局单元。

Card 组件与 Section 有什么区别？

| 维度 | Section | Card |
|------|---------|------|
| **层级** | 页面级内容区块 | 区块内的内容容器 |
| **尺寸** | 大（占满页面宽度） | 中小（可在网格中排列） |
| **标题** | 必有标题（h2级别） | 可选标题（h3级别） |
| **内边距** | 28px（宽松） | 24px（适中） |
| **圆角** | 20px | 18px |
| **使用场景** | 章节分隔、大主题 | 数据展示、小模块 |

简单来说：Section 是"大章节"，Card 是"小卡片"。Card 可以放在 Section 内部，也可以独立使用。

### 4.5.3 SubCard 子卡片组件

**功能定位**：在 Section 或 Card 内部使用的次级卡片，提供更细粒度的内容分组。

**设计特点**：
- 更浅的背景色（#f9fafb）
- 更小的内边距（18px 20px）
- 更小的圆角（14px）
- 更淡的边框
- 支持 primary/success/warning/danger 等色彩变体

**设计洞察**：SubCard 的存在体现了设计的**层次粒度**。当页面内容复杂时，只有 Section 和 Card 两级是不够的——Card 内部还需要进一步的视觉分组。SubCard 就是 Card 的"次一级"，通过更浅的背景、更小的尺寸来表达"这是大卡片内的小模块"的语义。

### 4.5.4 CardGrid 卡片网格

**功能定位**：将多个卡片（通常是 SubCard）按网格排列。

**核心实现**：

```python
# 文件: v3/components/layout.py

class CardGrid(Component):
    """卡片网格组件 - 在Section内排列多个SubCard"""
    def __init__(self, cards, cols=2, gap="16px"):
        super().__init__()
        self.cards = cards
        self.cols = cols
        self.gap = gap
    
    def render(self):
        cards_html = ""
        for card in self.cards:
            if hasattr(card, 'render'):
                c = card.render()
            else:
                c = str(card)
            cards_html += '<div style="min-width: 0;">' + c + '</div>'
        
        min_width = "260px" if self.cols >= 3 else "280px"
        grid_style = 'display: grid; grid-template-columns: repeat(auto-fit, minmax(' + min_width + ', 1fr)); gap: ' + self.gap + '; margin-bottom: 8px;'
        return '<div style="' + grid_style + '">' + cards_html + '</div>'
```

**设计亮点**：使用 `auto-fit + minmax` 的 Grid 布局技巧，实现了**响应式自动折行**。当容器宽度足够时，显示指定列数；当宽度不足时，自动减少列数，确保卡片不会被挤压得过窄。

### 4.5.5 SplitLayout 左右分栏布局

**功能定位**：实现左右两栏布局，支持自定义左栏宽度和间距。

**核心实现**：

```python
# 文件: v3/components/layout.py

class SplitLayout(Component):
    """左右分栏布局组件 - 实现左右两栏布局
    支持左图右文、左列表右详情等布局
    """
    
    def __init__(self, left=None, right=None, left_width="50%", gap="24px"):
        super().__init__()
        self.left = left
        self.right = right
        self.left_width = left_width
        self.gap = gap
    
    def render(self) -> str:
        left_html = ""
        if self.left is not None:
            if hasattr(self.left, 'render'):
                left_html = self.left.render()
            else:
                left_html = str(self.left)
        
        right_html = ""
        if self.right is not None:
            if hasattr(self.right, 'render'):
                right_html = self.right.render()
            else:
                right_html = str(self.right)
        
        return f'''
        <div style="display: flex; gap: {self.gap}; flex-wrap: wrap;">
            <div style="flex: 0 0 {self.left_width}; min-width: 280px;">
                {left_html}
            </div>
            <div style="flex: 1; min-width: 280px;">
                {right_html}
            </div>
        </div>
        '''
```

**设计亮点**：
- 左栏固定宽度 + 右栏弹性填充，是经典的"侧边栏 + 主内容"布局模式
- `min-width: 280px` 确保窄屏下自动换行，实现响应式
- `flex-wrap: wrap` 允许换行，避免内容溢出

### 4.5.6 Navbar 导航栏

**功能定位**：全站统一的顶部导航栏，提供页面跳转和品牌展示。

**核心实现**：

```python
# 文件: v3/components/layout.py

class Navbar(Component):
    """导航栏组件 - 全站统一glass-nav玻璃态风格
    与首页标准完全一致
    """
    
    from core.config import NAV_ITEMS as _NAV_ITEMS
    NAV_ITEMS = _NAV_ITEMS
    
    def __init__(self, active_key: str = "index"):
        super().__init__()
        self.active_key = active_key
    
    @classmethod
    def get_css(cls):
        """获取导航栏CSS样式 - glass-nav玻璃态风格"""
        return """
        <style>
            .glass-nav {
                position: fixed;
                top: 0;
                left: 0;
                right: 0;
                z-index: 2147483647 !important;
                background: rgba(0, 0, 0, 0.3);
                backdrop-filter: blur(20px);
                -webkit-backdrop-filter: blur(20px);
                border-bottom: 1px solid rgba(255, 255, 255, 0.1);
                transition: background 0.3s ease;
            }
            
            .glass-nav.scrolled {
                background: rgba(0, 0, 0, 0.7);
            }
            /* ... 更多样式 ... */
        </style>
        """
    
    def render(self) -> str:
        # 构建导航链接
        links_html = ""
        for item in self.NAV_ITEMS:
            active_class = "active" if item["key"] == self.active_key else ""
            links_html += f'\n            <a href="{item["path"]}" class="glass-nav-link {active_class}">{item["label"]}</a>'
        
        # 移动端菜单
        # ... 移动端菜单实现 ...
        
        return f"""
        <nav class="glass-nav">
            <div class="glass-nav-inner">
                <a href="/" class="glass-nav-logo">
                    <div class="glass-nav-logo-icon">📊</div>
                    <span class="glass-nav-logo-text">投资研究中心</span>
                </a>
                <div class="glass-nav-links">
                    {links_html}
                </div>
                <button class="hamburger-btn" onclick="toggleMenu()">
                    ☰
                </button>
            </div>
        </nav>
        <!-- 移动端菜单 -->
        <!-- ... -->
        <script>
            // 导航栏滚动加深效果
            window.addEventListener('scroll', function() {
                const nav = document.querySelector('.glass-nav');
                if (nav) {
                    if (window.scrollY > 50) {
                        nav.classList.add('scrolled');
                    } else {
                        nav.classList.remove('scrolled');
                    }
                }
            });
        </script>
        """
```

**设计亮点**：

1. **玻璃态设计**：`backdrop-filter: blur(20px)` 实现毛玻璃效果，是现代 UI 的标志性设计
2. **滚动加深**：页面滚动时导航栏背景加深，提升可读性和沉浸感
3. **极高 z-index**：`z-index: 2147483647`（32 位 int 最大值），确保导航栏永远在最上层
4. **响应式汉堡菜单**：移动端自动切换为汉堡按钮 + 全屏菜单
5. **数据驱动**：导航项从 `core.config.NAV_ITEMS` 配置读取，单一数据源，修改方便

> 💡 **技术洞察**：为什么导航栏的 CSS 要单独用 `get_css()` 方法输出，而不是像其他组件那样写内联样式？
> 
> 因为导航栏需要：
> 1. 响应式布局（`@media` 查询）——内联样式不支持
> 2. 伪类选择器（`:hover`）——内联样式不支持
> 3. 滚动状态类（`.scrolled`）——JS 切换类名
> 
> 这些都需要真实的 CSS 类来实现。因此 Navbar 采用了"CSS 类 + 内联样式"混合模式：基础样式用 CSS 类，动态样式（如激活态）用内联补充。

### 4.5.7 Footer 页脚

**功能定位**：页面底部的版权和品牌信息区。

**设计特点**：
- 顶部细边框分隔
- 居中对齐
- 品牌名使用渐变文字效果
- 辅助文字使用浅灰色，弱化处理

### 4.5.8 布局体系总结

DeepWiki 的布局组件形成了一个完整的层级体系：

```
页面
├── Navbar（顶部导航）
├── 页面标题区
├── Section（大章节）
│   ├── Card（卡片）
│   │   ├── SubCard（子卡片）
│   │   └── CardGrid（卡片网格）
│   │       └── SubCard
│   ├── SplitLayout（左右分栏）
│   │   ├── 左栏内容
│   │   └── 右栏内容
│   └── DataTable（数据表格）
├── 更多 Section...
└── Footer（页脚）
```

这套体系的设计哲学是**"从大到小、层层嵌套"**，每一层都有明确的视觉权重和语义含义。用户在浏览页面时，能够通过视觉层次快速理解内容的组织结构。

---

## 4.6 图表组件 - 数据可视化单元

图表是金融数据可视化的核心手段。DeepWiki 组件库提供了基于 Chart.js 的图表组件封装。

### 4.6.1 设计思路：轻量封装而非重造轮子

图表是一个非常复杂的领域，涉及画布渲染、交互、动画、多图表类型等。DeepWiki 没有选择从零实现图表库，而是采用了**"基于 Chart.js 的轻量封装"**策略：

- ✅ 利用成熟的开源图表库，保证功能完整性
- ✅ 封装常用配置，简化调用方式
- ✅ 统一视觉风格（配色、字体、间距）
- ✅ 保持一定的扩展性，高级用户可传入自定义配置

### 4.6.2 BaseChart 基类

**核心实现**：

```python
# 文件: v3/components/charts.py

class BaseChart(Component):
    """图表基类"""
    
    def __init__(self, title: str = None, height: str = None):
        super().__init__()
        self.title = title
        self.height = height or SIZES["chart_height"]
        self.chart_id = _get_chart_id()
    
    def _get_options(self) -> dict:
        """获取图表配置选项 - 子类可覆盖"""
        return {
            "responsive": True,
            "maintainAspectRatio": True,
            "plugins": {
                "legend": {
                    "display": True,
                    "position": "bottom",
                    "labels": {
                        "usePointStyle": True,
                        "padding": 20,
                        "font": {
                            "size": 12,
                            "family": "-apple-system, BlinkMacSystemFont, 'PingFang SC', sans-serif"
                        },
                        "color": "#6b7280"
                    }
                },
                "title": {
                    "display": bool(self.title),
                    "text": self.title or "",
                    "font": {
                        "size": 16,
                        "weight": "bold",
                        "family": "-apple-system, BlinkMacSystemFont, 'PingFang SC', sans-serif"
                    },
                    "padding": {"bottom": 20},
                    "color": "#1f2937"
                },
                "tooltip": {
                    "backgroundColor": "rgba(31, 41, 55, 0.95)",
                    "titleFont": {
                        "size": 13,
                        "weight": "600",
                        "family": "-apple-system, BlinkMacSystemFont, 'PingFang SC', sans-serif"
                    },
                    "bodyFont": {
                        "size": 12,
                        "family": "-apple-system, BlinkMacSystemFont, 'PingFang SC', sans-serif"
                    },
                    "padding": 12,
                    "cornerRadius": 8,
                    "displayColors": True
                }
            },
            "scales": {
                "y": {
                    "beginAtZero": False,
                    "grid": {
                        "color": "rgba(0,0,0,0.05)",
                        "drawBorder": False
                    },
                    "ticks": {
                        "font": {
                            "size": 11,
                            "family": "-apple-system, BlinkMacSystemFont, 'PingFang SC', sans-serif"
                        },
                        "color": "#9ca3af"
                    }
                },
                "x": {
                    "grid": {
                        "display": False,
                        "drawBorder": False
                    },
                    "ticks": {
                        "font": {
                            "size": 11,
                            "family": "-apple-system, BlinkMacSystemFont, 'PingFang SC', sans-serif"
                        },
                        "color": "#9ca3af"
                    }
                }
            },
            "elements": {
                "point": {
                    "radius": 3,
                    "hoverRadius": 5,
                    "pointStyle": "circle"
                },
                "line": {
                    "tension": 0.4,
                    "borderWidth": 2
                }
            }
        }
    
    def render(self) -> str:
        """渲染图表HTML"""
        config = self._get_chart_config()
        config_json = json.dumps(config, ensure_ascii=False)
        
        return f"""
        <div class="bg-white rounded-2xl p-6 border border-gray-100 shadow-sm">
            <div class="chart-wrapper" style="height: {self.height}px;">
                <canvas id="{self.chart_id}"></canvas>
            </div>
            <script>
                (function() {{
                    const ctx = document.getElementById('{self.chart_id}').getContext('2d');
                    new Chart(ctx, {config_json});
                }})();
            </script>
        </div>
        """
```

**设计亮点**：

1. **统一样式规范**：字体、配色、间距、圆角全部统一，确保所有图表风格一致
2. **配置驱动**：通过 `_get_options()` 返回配置字典，子类可以增量修改，而非重写全部
3. **自执行函数封装**：每个图表的 JS 代码用 IIFE 包裹，避免变量污染全局作用域
4. **Y 轴不从零开始**：`beginAtZero: False` 是金融图表的常见设置——股价波动通常在百分之几的范围内，如果从 0 开始，波动会显得非常平缓，无法看出变化

> ⚠️ **重要历史教训**：代码中 `maintainAspectRatio: True` 是一个被特别标注的配置。注释写道："必须为 true，历史教训"。
> 
> 这很可能是因为：
> - 当 `maintainAspectRatio: false` 时，图表高度由容器决定，但在响应式布局中容易出现高度塌陷或无限拉伸的问题
> - 设为 `true` 时，图表按比例缩放，行为更可预测
> - 这是一个踩过坑之后的经验总结，被固化在了基类默认配置中

### 4.6.3 LineChart 折线图

**功能定位**：展示趋势型数据，如股价走势、净值曲线、业绩增长等。

**核心实现**：

```python
# 文件: v3/components/charts.py

class LineChart(BaseChart):
    """折线图"""
    
    def __init__(self, labels: list, datasets: list, title: str = None, 
                 height: str = None, fill: bool = True):
        super().__init__(title=title, height=height)
        self.labels = labels
        self.datasets = datasets  # [{label, data, color?}, ...]
        self.fill = fill
    
    def _get_chart_config(self) -> dict:
        config = self._get_options()
        
        default_colors = [
            COLORS["primary"],
            COLORS["success"],
            COLORS["warning"],
            COLORS["danger"],
            COLORS["secondary"],
            COLORS["info"],
        ]
        
        chart_datasets = []
        for i, ds in enumerate(self.datasets):
            color = ds.get("color", default_colors[i % len(default_colors)])
            chart_datasets.append({
                "label": ds["label"],
                "data": ds["data"],
                "borderColor": color,
                "backgroundColor": color.replace(")", ", 0.1)").replace("rgb", "rgba") if "rgb" in color else f"{color}20",
                "fill": self.fill,
                "tension": 0.4,
                "pointRadius": 3,
                "pointHoverRadius": 5,
                "borderWidth": 2
            })
        
        config["type"] = "line"
        config["data"] = {
            "labels": self.labels,
            "datasets": chart_datasets
        }
        
        return config
```

**设计亮点**：
1. **默认调色板**：内置 6 种默认颜色，调用方不传颜色时自动分配，简单易用
2. **曲线平滑**：`tension: 0.4` 让折线呈现平滑的贝塞尔曲线，比生硬的折线更美观
3. **面积填充**：`fill: True` 默认填充折线下方区域，增强视觉分量感
4. **点大小优化**：数据点半径 3px，悬停时放大到 5px，提供良好的交互反馈

### 4.6.4 BarChart 柱状图

**功能定位**：展示分类对比数据，如各行业涨幅、各公司营收对比等。

**核心特性**：
- 支持横向柱状图（`horizontal: True`）
- 圆角柱形（`borderRadius: 6`）
- 自适应柱宽（`barThickness: "flex"`）
- 与折线图共享默认配色方案

### 4.6.5 PieChart 饼图/环形图

**功能定位**：展示占比数据，如持仓结构、行业分布、营收构成等。

**核心特性**：
- 默认环形图（`donut: True`），更现代美观
- 圆角扇区（`borderRadius: 4`）
- 悬停放大效果（`hoverOffset: 8`）
- 10 色默认调色板，支持较多分类

**设计洞察**：为什么默认是环形图（donut）而不是饼图（pie）？
1. **更现代**：环形图是近年的设计趋势，比传统饼图更轻盈
2. **中心可利用**：环形图的中心空白可以放置总数、百分比等关键数据
3. **视觉干扰小**：完整的饼图容易给人"压迫感"，环形更通透
4. **便于多图对比**：多个环形图可以嵌套展示层级关系

### 4.6.6 图表组件的使用模式

图表组件的典型使用方式：

```python
from v3.components import LineChart, Section

# 准备数据
labels = ["1月", "2月", "3月", "4月", "5月", "6月"]
datasets = [
    {"label": "产品A", "data": [120, 190, 230, 180, 260, 310]},
    {"label": "产品B", "data": [80, 120, 150, 130, 180, 220]},
]

# 创建图表
chart = LineChart(labels=labels, datasets=datasets, title="销售趋势", height=300)

# 放入章节
section = Section(title="数据分析", icon="chart", content=chart)
```

### 4.6.7 技术权衡

**Chart.js 方案的优势**：
- ✅ 功能完整，支持多种图表类型和交互
- ✅ Canvas 渲染，大数据量性能好
- ✅ 社区活跃，文档完善
- ✅ 响应式支持良好

**局限性与应对**：
- ❌ 需要外部库加载 → 通过 CDN 引入，页面加载时注入
- ❌ 服务端渲染时图表还是空的 → 这是所有 JS 图表的共性问题，静态页面场景下可接受
- ❌ 自定义样式不够灵活 → 通过 `_get_options()` 暴露配置，高级用户可自定义

---

## 4.7 主题系统 - 视觉风格引擎

主题系统是组件库的"皮肤"，决定了整个界面的视觉风格。DeepWiki 拥有两套并行的主题体系。

### 4.7.1 主题系统的演进

DeepWiki 的主题系统经历了从无到有、从简单到完善的过程：

**第一阶段：零散的内联样式**
- 每个组件自己写颜色值
- 风格不统一，修改困难
- 没有"主题"的概念

**第二阶段：常量配置**
- 将颜色、尺寸等提取为 `COLORS`、`SIZES` 常量
- 组件引用常量，确保一致性
- 有了"主题"的雏形，但只能整体修改，不能切换

**第三阶段：双主题体系**
- Pro 深色玻璃态主题（v1）
- V4 白底清爽主题（v2）
- 主题与组件分离，可独立演进

### 4.7.2 Pro 深色玻璃态主题

**设计语言**：深色背景 + 毛玻璃卡片 + 紫色主调

**适用场景**：
- 专业投资者看盘界面
- 大屏展示
- 夜间阅读模式
- 追求视觉冲击力的页面

**核心色彩系统**：

| 色彩层级 | 色值 | 用途 |
|---------|------|------|
| 主色 | `#667eea` → `#764ba2`（135°渐变） | 品牌色、强调元素、主按钮 |
| 背景色 | 深紫色渐变 | 页面背景 |
| 卡片背景 | `rgba(255, 255, 255, 0.1)` | 玻璃态卡片 |
| 文字主色 | `rgba(255, 255, 255, 0.95)` | 标题、正文 |
| 文字次色 | `rgba(255, 255, 255, 0.7)` | 次要信息、辅助文字 |
| 文字弱化 | `rgba(255, 255, 255, 0.5)` | 占位符、时间戳 |
| 边框色 | `rgba(255, 255, 255, 0.1)` | 卡片边框、分割线 |

**玻璃态实现原理**：

玻璃态（Glassmorphism）的核心 CSS 属性：
```css
.glass-card {
    background: rgba(255, 255, 255, 0.1);  /* 半透明白色 */
    backdrop-filter: blur(20px);             /* 背景模糊 */
    -webkit-backdrop-filter: blur(20px);     /* Safari 兼容 */
    border: 1px solid rgba(255, 255, 255, 0.2);  /* 半透明边框 */
    border-radius: 16px;
}
```

**三个关键要素**：
1. **半透明背景**：让背景色透过来，形成"玻璃"的基底
2. **背景模糊**：`backdrop-filter: blur()` 让背景内容虚化，模拟毛玻璃效果
3. **半透明边框**：增强玻璃的边缘感，让卡片更有立体感

> 💡 **技术洞察**：玻璃态设计的关键在于"层次感"。
> 
> 如果背景是纯色的，玻璃态效果会大打折扣——因为没有东西可以"透"。玻璃态需要背景有丰富的色彩或纹理（如渐变色、图片、复杂布局），透过半透明的卡片看到模糊的背景，才能产生"玻璃"的质感。
> 
> 这也是为什么 Pro 主题使用紫色渐变背景——纯色背景无法体现玻璃态的魅力。

### 4.7.3 V4 白底清爽主题

**设计语言**：纯白卡片 + 柔和阴影 + 清晰文字层次

**适用场景**：
- 研究报告、分析文章
- 日间使用
- 追求可读性的内容页面
- 需要打印的页面

**核心色彩系统**：

| 色彩层级 | 色值 | 用途 |
|---------|------|------|
| 主色 | `#8B5CF6`（紫色） | 品牌色、强调、链接 |
| 页面背景 | `#F8FAFC`（浅灰蓝） | 页面底色 |
| 卡片背景 | `#FFFFFF`（纯白） | 内容卡片 |
| 文字主色 | `#1F2937`（深灰） | 标题、正文 |
| 文字次色 | `#6B7280`（中灰） | 次要信息 |
| 文字弱化 | `#9CA3AF`（浅灰） | 辅助信息、时间戳 |
| 边框色 | `#E5E7EB` | 边框、分割线 |

**V4 主题的设计原则**：

1. **内容优先**：一切设计为内容可读性服务，不炫技
2. **充足留白**：大间距、大行距，呼吸感强，长时间阅读不累
3. **柔和阴影**：`0 4px 6px -1px rgba(0, 0, 0, 0.1)`，不重不轻刚刚好
4. **色彩克制**：除了紫色主色，其他颜色尽量低饱和度，不抢内容的注意力

### 4.7.4 主题系统的架构设计

**分层架构**：

```
┌───────────────────────────────────────────┐
│              业务组件层                    │
│  V4StockCard / BoyaStrategySummary 等     │
├───────────────────────────────────────────┤
│              基础组件层                    │
│  Section / Card / DataCard / Badge 等     │
├───────────────────────────────────────────┤
│              主题配置层                    │
│  V4Theme 常量 / ProTheme 常量             │
│  (颜色、字体、圆角、阴影、间距)            │
├───────────────────────────────────────────┤
│              全局样式层                    │
│  get_v4_theme_css() / 全局 CSS 变量       │
└───────────────────────────────────────────┘
```

**设计模式：配置驱动的主题系统**

主题不是硬编码在组件里的，而是通过配置对象注入的：

```python
class V4Theme:
    """V4主题配置常量"""
    PRIMARY_COLOR = '#8B5CF6'
    SECONDARY_COLOR = '#6366F1'
    BG_CARD = '#FFFFFF'
    TEXT_PRIMARY = '#1F2937'
    # ... 更多配置
```

这种模式的优势：
- ✅ 主题与组件解耦，修改主题不需要改组件代码
- ✅ 可以轻松新增主题（只要配置一套新的颜色常量）
- ✅ 配置集中，便于维护和查阅

### 4.7.5 响应式设计体系

主题系统不仅包含颜色，还包含响应式布局规范。

**断点设计**：

| 断点 | 设备类型 | 典型宽度 | 布局变化 |
|------|---------|---------|---------|
| `> 1024px` | 桌面端 | 1280px+ | 多列布局、完整导航 |
| `768px - 1024px` | 平板 | 768-1024px | 列数减少、导航简化 |
| `< 768px` | 手机 | 375-428px | 单列布局、汉堡菜单 |
| `< 480px` | 小屏手机 | 320px | 进一步压缩间距和字号 |

**响应式实现方式**：
- 优先使用 Flex/Grid 的自动折行特性（如 `flex-wrap: wrap`、`auto-fit`）
- 关键布局使用 `@media` 查询调整
- 容器使用 `max-width` + 水平 `padding`，而非固定宽度

### 4.7.6 动效系统

动效是主题体验的"润滑剂"，好的动效让界面感觉流畅、精致。

**动效分类**：

| 动效类型 | 用途 | 典型时长 | 缓动函数 |
|---------|------|---------|---------|
| 悬停动效 | 按钮、卡片、链接的鼠标悬停反馈 | 0.2s | ease |
| 过渡动效 | 颜色、位置、大小的平滑变化 | 0.3s | cubic-bezier(0.4, 0, 0.2, 1) |
| 入场动效 | 元素进入视口时的淡入/滑入 | 0.6s | ease-out |
| 数字滚动 | 数据变化时的数字递增动画 | 1.5s | easeOutExpo |

**动效设计原则**：
1. **快**：动效时长不超过 300ms，避免让用户等待
2. **轻**：动效幅度小、变化柔和，不抢注意力
3. **少**：不是所有元素都要有动效，只在关键交互点使用
4. **顺**：缓动曲线自然，符合物理直觉

### 4.7.7 主题系统的技术挑战与解决方案

**挑战一：内联样式难以支持响应式**
- 问题：组件大量使用内联样式，但 `@media` 查询不能写在内联样式中
- 方案：关键响应式样式通过 CSS 类提供，组件使用 class 而非 style 控制布局

**挑战二：深色模式下的图片适配**
- 问题：深色背景上的图片可能显得突兀
- 方案：图片添加柔和的边框和阴影，融入深色背景

**挑战三：玻璃态的性能问题**
- 问题：`backdrop-filter: blur` 比较消耗 GPU，低端设备可能卡顿
- 方案：控制玻璃态元素的数量和大小，只在关键元素上使用；避免滚动时大量重绘

---

## 4.8 组件渲染机制 - 模板渲染与数据绑定

### 4.8.1 渲染流程总览

DeepWiki 组件采用**纯字符串拼接**的渲染方式，这是一种简单但高效的服务端渲染（SSR）模式。

```
组件初始化
    ↓
接收 props 参数
    ↓
计算内部状态（变体样式、尺寸、颜色等）
    ↓
构建子组件 HTML（递归渲染）
    ↓
拼接自身 HTML 模板
    ↓
返回完整 HTML 字符串
```

### 4.8.2 为什么选择字符串渲染？

在众多前端渲染方案中（React/Vue/Web Components/字符串模板），DeepWiki 选择了最朴素的字符串拼接，这是基于以下考量：

**1. 静态页面场景**
- DeepWiki 生成的是静态 HTML 页面，不需要复杂的客户端交互
- 服务端生成完整 HTML 后直接交付，不需要 hydration
- 字符串渲染最直接、最高效

**2. 技术栈统一**
- 整个系统用 Python 编写，组件也用 Python
- 不需要引入 Node.js 等额外技术栈
- 降低系统复杂度和维护成本

**3. 性能足够**
- 字符串拼接在 Python 中非常快
- 即使是复杂页面，渲染时间也在毫秒级
- 对于日更/时更的报告来说，性能够用

**4. 调试友好**
- 输出就是纯 HTML，可以直接在浏览器中查看
- 不需要 React DevTools 等调试工具
- 出问题直接看 HTML 源码就能定位

### 4.8.3 组件的多态渲染

DeepWiki 组件支持多种内容类型的传入，这被称为"内容多态"：

```python
# 可以传入字符串
Section(title="标题", content="这是内容")

# 可以传入另一个组件
Section(title="标题", content=Card(content="卡片内容"))

# 可以传入组件列表（需要手动拼接）
cards_html = "".join(card.render() for card in cards)
Section(title="标题", content=cards_html)

# 甚至可以是任何实现了 __str__ 方法的对象
```

**实现原理**：

```python
# 在组件的 render 方法中
content_html = ""
if self.content is not None:
    if hasattr(self.content, 'render'):
        # 如果是 Component 实例，调用 render()
        content_html = self.content.render()
    else:
        # 否则转为字符串
        content_html = str(self.content)
```

这种设计让组件组合非常灵活，不需要严格的类型系统约束。

### 4.8.4 样式注入机制

组件的样式有三种注入方式，根据复杂度不同选择不同的方案：

**方式一：内联样式（最常用）**
- 直接写在元素的 `style` 属性中
- 优点：简单直接，随组件一起输出
- 缺点：不支持伪类、媒体查询、动画
- 适用：Badge、DataCard、ProgressBar 等简单组件

**方式二：组件内联 `<style>` 标签**
- 在组件 HTML 中包含 `<style>` 标签
- 优点：支持伪类、动画，样式与组件绑定
- 缺点：多个相同组件会产生重复的 style 标签
- 适用：V4 组件库的复杂组件（V4StockCard 等）

**方式三：全局 CSS 注入**
- 通过 `get_xxx_css()` 方法统一输出全局样式
- 优点：无重复，支持所有 CSS 特性
- 缺点：需要单独调用，与组件分离
- 适用：Navbar、主题系统等全局样式

### 4.8.5 JavaScript 嵌入模式

对于需要交互的组件（如 Tabs），JavaScript 代码直接嵌入在组件 HTML 中。

**三种嵌入模式**：

| 模式 | 实现方式 | 适用场景 | 示例 |
|------|---------|---------|------|
| 事件处理器 | `onclick="..."` | 简单交互 | 按钮点击、折叠面板 |
| 内联脚本 | `<script>...</script>` | 组件级逻辑 | Tabs 切换 |
| 外部脚本 | `<script src="...">` | 大型库 | Chart.js |

**自包含设计哲学**：
每个组件都是"自包含"的——你只需要创建组件实例并调用 `render()`，它就会输出完整的 HTML+CSS+JS，不需要额外引入依赖（除了 Chart.js 等大型库）。

### 4.8.6 ID 生成与唯一性保证

当页面中有多个同类型组件时（如多个 Tabs），如何避免 ID 冲突？

**方案：随机数 + 前缀**

```python
import random

tab_id = f"tabs_{random.randint(10000, 99999)}"
```

生成的 ID 形如 `tabs_48291`，冲突概率极低。

**适用场景**：
- Tabs 组件的 tab 面板 ID
- 图表组件的 canvas ID
- 折叠面板的内容区 ID
- 所有需要 JS 通过 ID 定位元素的场景

### 4.8.7 性能优化策略

虽然字符串渲染已经很快，但在组件数量较多时，仍有优化空间：

**1. 字符串构建优化**
- 使用 `"".join(list)` 而非多次 `+=` 拼接
- 减少中间字符串的创建
- 对于大组件，分段构建后再合并

**2. 缓存机制**
- 不变化的组件（如 Navbar、Footer）可以缓存渲染结果
- 相同配置的组件可以复用计算结果

**3. 延迟渲染**
- 只在需要时才渲染组件
- 条件渲染的内容放在判断内部

**4. 减少嵌套层级**
- 过深的组件嵌套会导致递归调用栈过深
- 适当使用扁平结构，减少渲染层级

### 4.8.8 与主流前端框架的对比

| 特性 | DeepWiki 组件 | React | Vue | Web Components |
|------|-------------|-------|-----|----------------|
| 渲染方式 | 字符串拼接 | Virtual DOM | Virtual DOM | 真实 DOM |
| 运行环境 | Python 服务端 | 浏览器 | 浏览器 | 浏览器 |
| 响应式 | 无（静态） | 有 | 有 | 有 |
| 组件化 | 是 | 是 | 是 | 是 |
| 学习成本 | 极低 | 高 | 中 | 中 |
| 构建工具 | 不需要 | 需要 | 需要 | 可选 |
| 首屏性能 | 极高（直出 HTML） | 差（需 JS 执行） | 差 | 中 |
| 交互能力 | 弱 | 强 | 强 | 强 |
| 适用场景 | 静态内容展示 | 复杂应用 | 复杂应用 | 组件复用 |

**结论**：DeepWiki 的组件系统是一个**面向静态内容展示场景的轻量化组件方案**。它牺牲了客户端交互能力，换来了极致的简单性和首屏性能，对于投资研究报告这类内容为主的场景非常适用。

---

## 4.9 组件库的扩展与维护 - 规范与最佳实践

### 4.9.1 新增组件的规范

当需要新增组件时，遵循以下规范：

**一、组件定义规范**

1. **继承基类**：所有组件继承 `Component` 基类
2. **实现 render**：必须实现 `render()` 方法，返回 HTML 字符串
3. **构造函数参数**：
   - 第一个参数是核心内容/标题（必须）
   - 然后是重要配置项
   - 最后是可选配置项，提供默认值
   - 使用 keyword-only 参数，提高可读性

```python
# 好的示例
class MyComponent(Component):
    def __init__(self, title: str, content=None, variant: str = "default", size: str = "md"):
        super().__init__()
        self.title = title
        self.content = content
        self.variant = variant
        self.size = size
```

**二、命名规范**

| 元素类型 | 命名规则 | 示例 |
|---------|---------|------|
| 组件类 | 大驼峰（PascalCase） | `DataCard`, `ProgressBar` |
| 组件文件 | 小写 + 下划线 | `data.py`, `special.py` |
| 方法名 | 小驼峰（camelCase）或蛇形 | `render()`, `get_css()` |
| 变量名 | 蛇形（snake_case） | `title_html`, `items_list` |
| 常量 | 全大写 + 下划线 | `PRIMARY_COLOR`, `DEFAULT_RADIUS` |

**三、文档规范**

每个组件类都应该有 docstring，说明：
- 组件的功能定位
- 主要参数说明
- 使用场景
- 简单的使用示例

```python
class DataCard(Component):
    """精致数据卡片 - 展示关键指标
    
    用于展示单个关键数据指标，支持图标、趋势、副标题等。
    通常与 DataGrid 组合使用，形成数据看板。
    
    Args:
        title: 卡片标题
        value: 数值内容（字符串，支持格式化）
        trend: 趋势描述文本（可选）
        trend_up: 趋势方向（True=上涨/绿色，False=下跌/红色）
        unit: 单位文本（可选）
        icon: 图标名称（可选，来自 icons.py）
        variant: 样式变体（default/primary/success/warning/danger）
        subtitle: 副标题文字（可选）
    
    Example:
        >>> card = DataCard("总收益", "+12.5%", trend="较昨日+0.3%", 
                          trend_up=True, icon="trending_up", variant="success")
        >>> print(card.render())
    """
```

**四、变体设计规范**

1. **至少提供 default 变体**：所有组件都应该有一个默认样式
2. **变体命名语义化**：用 `primary`、`success`、`warning`、`danger` 等语义化名称，而非颜色名
3. **变体数量适中**：通常 3-5 个变体足够，太多会增加使用和维护成本
4. **变体遵循同一设计语言**：同一组件的不同变体应该只是颜色/大小变化，结构保持一致

**五、可访问性规范**

1. **颜色对比度**：文字与背景的对比度至少达到 WCAG AA 标准（4.5:1）
2. **语义化标签**：使用 `<section>`、`<nav>`、`<footer>` 等语义化 HTML 标签
3. **图标替代文本**：纯图标按钮需要有 `aria-label`
4. **键盘可用**：交互元素（按钮、链接）支持 Tab 键聚焦和 Enter 键触发

### 4.9.2 组件的分层组织

组件按功能分类组织到不同模块中：

| 模块 | 职责 | 包含组件 |
|------|------|---------|
| `base.py` | 基类与基础工具 | Component, HTMLComponent, 动效资源 |
| `layout.py` | 布局类组件 | Section, Card, Navbar, Footer, SplitLayout |
| `data.py` | 数据展示组件 | DataCard, Badge, ProgressBar, DataGrid, MetricsRow |
| `charts.py` | 图表组件 | LineChart, BarChart, PieChart |
| `special.py` | 特殊/交互组件 | RiskAlert, Timeline, Tabs, QuoteBlock, NewsItem |
| `icons.py` | 图标系统 | Icon, icon_svg, gradient_icon |
| `pro.py` | Pro 主题业务组件 | BoyaBuyPointCard, RiskBar 等 |
| `v4_components.py` | V4 主题专业组件 | V4StockCard, V4TopicCard, V4MarketOverview |
| `v4_theme.py` | V4 主题配置 | 主题 CSS、颜色常量 |

**扩展原则**：
- 基础组件放 `layout.py` 或 `data.py`
- 业务组件放 `pro.py` 或 `v4_components.py`
- 如果一类组件数量超过 5 个，可以考虑单独建模块
- 保持模块间的单向依赖，避免循环引用

### 4.9.3 版本管理策略

组件库的版本号遵循 **语义化版本（SemVer）** 规范：

- **主版本号（Major）**：不兼容的 API 改动（如删除组件、修改参数名）
- **次版本号（Minor）**：向下兼容的功能新增（如新组件、新参数）
- **修订号（Patch）**：向下兼容的问题修正（如修复样式 bug、优化渲染性能）

**版本演进原则**：
1. **保持向后兼容**：新增参数必须有默认值，不能破坏现有调用
2. **废弃而非删除**：要删除的功能先标记 deprecated，至少保留一个大版本再删除
3. **渐进式重构**：大型重构分步骤进行，每一步都保持可用
4. **文档同步更新**：版本更新时同步更新使用文档和示例

### 4.9.4 常见设计模式

**模式一：配置合并模式**
组件有一组默认配置，用户可以传入自定义配置进行覆盖。

```python
class MyComponent(Component):
    DEFAULT_CONFIG = {
        "color": "#333",
        "size": "md",
        "rounded": True,
    }
    
    def __init__(self, content, **kwargs):
        self.config = {**self.DEFAULT_CONFIG, **kwargs}
```

**模式二：变体字典模式**
多种视觉变体，通过 variant 参数选择。

```python
class Badge(Component):
    VARIANTS = {
        "primary": {"bg": "...", "color": "white"},
        "success": {"bg": "...", "color": "white"},
        # ...
    }
    
    def render(self):
        v = self.VARIANTS.get(self.variant, self.VARIANTS["default"])
        # 使用 v 构建样式
```

**模式三：多态内容模式**
内容可以是字符串或组件实例。

```python
def render(self):
    if hasattr(self.content, 'render'):
        content_html = self.content.render()
    else:
        content_html = str(self.content)
```

**模式四：自包含 JS 组件**
带交互的组件，自己打包 JS 代码。

```python
def render(self):
    js = f'''
    <script>
    function switchTab_{self.id}(index) {{
        // ... 交互逻辑
    }}
    </script>
    '''
    return html + js
```

### 4.9.5 性能最佳实践

**1. 避免重复计算**
- 不变的样式常量提到模块级别
- 相同配置的计算结果可以缓存
- 图标 SVG 等静态资源预生成

**2. 减少字符串拼接次数**
- 使用列表收集 HTML 片段，最后 `"".join()`
- 避免在循环中使用 `+=` 拼接长字符串

**3. 合理使用组件组合**
- 不要为了"组件化"而过度拆分
- 简单的 HTML 直接写字符串，不必封装成组件
- 平衡复用性与复杂度

**4. 图片优化**
- 图标使用 SVG，不使用位图
- 渐变使用 CSS 实现，不使用背景图
- 外部图片使用适当尺寸，避免大图被缩小显示

### 4.9.6 测试策略

组件库的测试主要覆盖三个方面：

**1. 渲染正确性测试**
- 组件是否能正常渲染，不抛出异常
- 输出的 HTML 是否包含预期的内容
- 不同参数组合下的渲染结果

**2. 视觉回归测试**
- 组件渲染后的截图与参考图对比
- 检测意外的样式变化
- 可以使用 Puppeteer 等工具自动化

**3. 边界情况测试**
- 空内容、超长内容
- 特殊字符、HTML 注入
- 极端参数值（如 0、负数、极大值）

### 4.9.7 文档与示例

好的组件库需要好的文档。建议维护以下文档：

1. **组件索引页**：列出所有组件，快速浏览
2. **单个组件文档**：功能说明、参数列表、使用示例、效果预览
3. **设计规范文档**：色彩系统、间距规范、字体规范、动效规范
4. **最佳实践指南**：如何组合组件、常见布局模式、避免踩坑
5. **更新日志**：每个版本的改动说明

---

## 本章小结

组件库系统是 DeepWiki 投资研究系统的 UI 基石，经过三代演进，形成了一套完整的、面向金融场景的专业组件体系。

### 核心要点回顾

**1. 四层架构**
- 基础设施层：Component 基类、主题系统、图标系统、动效系统
- 基础组件层：Badge、Button、Card、ProgressBar 等原子组件
- 复合组件层：DataGrid、CardGrid、MetricsRow、Tabs 等组合组件
- 业务组件层：V4StockCard、V4TopicCard、RiskAlert 等面向投资场景的组件

**2. 两大主题**
- Pro 深色玻璃态：紫色渐变背景 + 毛玻璃卡片，适合专业场景
- V4 白底清爽风：纯白卡片 + 柔和阴影，适合内容阅读

**3. 设计理念**
- 内容与展现分离：组件只负责展示，不包含业务逻辑
- 渐进式复杂度：简单场景简单用，复杂场景可定制
- 面向投资场景优化：红涨绿跌、风险提示、数据看板等专业设计
- 无障碍优先：清晰的文字层次、足够的对比度、宽松的间距

**4. 渲染机制**
- 纯字符串拼接的服务端渲染
- 自包含设计：HTML + CSS + JS 一体化输出
- 内容多态：支持字符串、组件、任意可转字符串对象
- 三种样式注入方式：内联样式、组件 style 标签、全局 CSS

**5. 扩展与维护**
- 明确的新增组件规范
- 语义化版本管理
- 四种常用设计模式
- 性能优化与测试策略

### 组件库的价值

DeepWiki 组件库不仅仅是 UI 组件的集合，更是一套**设计语言的载体**。它将专业的设计原则、金融场景的特性、用户体验的最佳实践固化为可复用的代码，让整个系统的视觉呈现保持高度一致，同时极大提升了开发效率。

从更深层的意义上说，组件库是系统"品质感"的来源。用户可能说不出具体哪里好，但会感觉这个系统"看起来很专业"、"用起来很舒服"——这种感觉，正是由每一个组件的圆角、阴影、间距、色彩、动效共同构成的。
