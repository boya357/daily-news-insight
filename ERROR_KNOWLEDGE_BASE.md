
# 错误知识库 - 永久记录与预防机制

## 错误记录 #4：生成报告时导航栏样式与系统不统一

### 错误描述
- 生成产业链深度报告时，使用了旧版"MLCC Pro v2.0"导航栏样式，导致与全站统一的"投资研究中心"玻璃态导航栏不一致

### 根本原因
1. 使用了过时的模板文件，没有更新到最新的系统标准导航栏样式
2. CSS样式、标题文字、按钮数量、链接路径都没有统一

### 发生时间
- 2026年6月3日

### 影响范围
- docs/industry_chain/20260603_英伟达GTC与COMPUTEX催化超深度挖掘报告.html

### 修复方案
- 已将该报告导航栏完全替换为系统标准样式

### 预防措施（必须严格执行）

#### 1. 标准导航栏模板（复制以下内容，不得修改
```html
        .glass-nav {
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            border-bottom: 1px solid rgba(255, 255, 255, 0.2);
            z-index: 2147483647 !important;
            isolation: isolate !important;
            pointer-events: auto !important;
        }
        
        .glass-nav * {
            position: relative;
            z-index: 2147483647 !important;
            pointer-events: auto !important;
        }
        
        body {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            font-family: -apple-system, BlinkMacSystemFont, 'PingFang SC', 'Helvetica Neue', sans-serif;
        }
    </style>
</head>
<body>
    <nav class="fixed top-0 left-0 right-0 z-50 glass-nav">
        <div class="max-w-5xl mx-auto px-4 py-3 flex items-center justify-between">
            <div class="flex items-center space-x-3">
                <div class="w-8 h-8 rounded-lg bg-gradient-to-br from-indigo-500 to-purple-600 flex items-center justify-center">
                    <span class="text-white text-sm font-bold">📊</span>
                </div>
                <span class="text-white font-bold text-lg">投资研究中心</span>
            </div>
            <div class="flex items-center space-x-1 flex-wrap gap-1">
                <a href="/daily-news-insight/index.html" class="text-white/80 hover:text-white hover:bg-white/10 text-sm transition-colors px-3 py-1.5 rounded-lg">首页</a>
                <a href="/daily-news-insight/daily/latest.html" class="text-white/80 hover:text-white hover:bg-white/10 text-sm transition-colors px-3 py-1.5 rounded-lg">日报</a>
                <a href="/daily-news-insight/intraday/latest.html" class="text-white/80 hover:text-white hover:bg-white/10 text-sm transition-colors px-3 py-1.5 rounded-lg">盘中</a>
                <a href="/daily-news-insight/aftermarket/latest.html" class="text-white/80 hover:text-white hover:bg-white/10 text-sm transition-colors px-3 py-1.5 rounded-lg">盘后</a>
                <a href="/daily-news-insight/industry_chain/latest.html" class="text-white/80 hover:text-white hover:bg-white/10 text-sm transition-colors px-3 py-1.5 rounded-lg">产业链</a>
                <a href="/daily-news-insight/weekly_review/latest.html" class="text-white/80 hover:text-white hover:bg-white/10 text-sm transition-colors px-3 py-1.5 rounded-lg">周复盘</a>
                <a href="/daily-news-insight/weekly_outlook/latest.html" class="text-white/80 hover:text-white hover:bg-white/10 text-sm transition-colors px-3 py-1.5 rounded-lg">周三前瞻</a>
                <a href="/daily-news-insight/周末速递/latest.html" class="text-white/80 hover:text-white hover:bg-white/10 text-sm transition-colors px-3 py-1.5 rounded-lg">周末速递</a>
                <a href="/daily-news-insight/明日催化剂/latest.html" class="text-white/80 hover:text-white hover:bg-white/10 text-sm transition-colors px-3 py-1.5 rounded-lg">明日催化</a>
                <a href="/daily-news-insight/s级催化扫描/latest.html" class="text-white/80 hover:text-white hover:bg-white/10 text-sm transition-colors px-3 py-1.5 rounded-lg">S级催化</a>
                <a href="/daily-news-insight/monthly/latest.html" class="text-white/80 hover:text-white hover:bg-white/10 text-sm transition-colors px-3 py-1.5 rounded-lg">月报</a>
            </div>
        </div>
    </nav>
```

#### 2. 生成新报告的强制检查清单
生成任何新报告前，必须对照以上模板检查：
- ✅ CSS样式是否完全一致
- ✅ 标题是否为"投资研究中心" + 📊图标
- ✅ 导航按钮数量是否为11个（首页、日报、盘中、盘后、产业链、周复盘、周三前瞻、周末速递、明日催化、S级催化、月报
- ✅ 所有链接是否使用绝对路径`/daily-news-insight/`开头
- ✅ z-index是否为2147483647
- ✅ body背景是否为紫蓝渐变`#667eea → #764ba2`

#### 3. 提交前校验
任何报告生成后，必须打开浏览器验证导航栏是否与周复盘列表页完全一致后再提交
