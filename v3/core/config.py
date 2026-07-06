# V3.0 核心配置 - 单一数据源原则 (SSOT)
# 所有路径、导航、颜色、尺寸都从这里统一引用，杜绝不一致

# ==========================================
# 站点基础配置
# ==========================================
SITE_NAME = "投资研究中心"
SITE_ICON = "📊"
BASE_PATH = "/daily-news-insight"
GITHUB_PAGES_BASE = "https://boya357.github.io/daily-news-insight"

# ==========================================
# 报告类型与目录映射（杜绝目录放错）
# ==========================================
REPORT_TYPES = {
    "index": {"name": "首页", "dir": "", "file": "index.html"},
    "daily": {"name": "日报", "dir": "daily", "list_file": "index.html"},
    "intraday": {"name": "盘中快报", "dir": "intraday", "list_file": "index.html"},
    "aftermarket": {"name": "盘后速递", "dir": "aftermarket", "list_file": "index.html"},
    "industry_chain": {"name": "产业链", "dir": "industry_chain", "list_file": "index.html"},
    "weekly_review": {"name": "周复盘", "dir": "weekly_review", "list_file": "index.html"},
    "weekly_outlook": {"name": "周三前瞻", "dir": "weekly_outlook", "list_file": "index.html"},
    "weekend_express": {"name": "周末速递", "dir": "weekend_express", "list_file": "index.html"},
    "tomorrow_catalyst": {"name": "明日催化剂", "dir": "tomorrow_catalyst", "list_file": "index.html"},
    "s_level_catalyst": {"name": "S级催化", "dir": "s_level_catalyst", "list_file": "index.html"},
    "monthly": {"name": "月报", "dir": "monthly", "list_file": "index.html"},
}

# ==========================================
# 导航栏配置（11个按钮，唯一数据源）
# ==========================================
NAV_ITEMS = [
    {"key": "index", "label": "首页", "icon": "🏠", "path": "/daily-news-insight/index.html"},
    {"key": "daily", "label": "日报", "icon": "📰", "path": "/daily-news-insight/daily/latest.html"},
    {"key": "intraday", "label": "盘中", "icon": "📈", "path": "/daily-news-insight/intraday/latest.html"},
    {"key": "aftermarket", "label": "盘后", "icon": "📉", "path": "/daily-news-insight/aftermarket/latest.html"},
    {"key": "industry_chain", "label": "产业链", "icon": "🔗", "path": "/daily-news-insight/industry_chain/latest.html"},
    {"key": "weekly_review", "label": "周复盘", "icon": "📋", "path": "/daily-news-insight/weekly_review/latest.html"},
    {"key": "weekly_outlook", "label": "周三前瞻", "icon": "🔮", "path": "/daily-news-insight/weekly_outlook/latest.html"},
    {"key": "weekend_express", "label": "周末速递", "icon": "📦", "path": "/daily-news-insight/weekend_express/latest.html"},
    {"key": "tomorrow_catalyst", "label": "明日催化", "icon": "⏰", "path": "/daily-news-insight/tomorrow_catalyst/latest.html"},
    {"key": "s_level_catalyst", "label": "S级催化", "icon": "⭐", "path": "/daily-news-insight/s_level_catalyst/latest.html"},
    {"key": "monthly", "label": "月报", "icon": "🗓️", "path": "/daily-news-insight/monthly/latest.html"},
]

# ==========================================
# 主题配色系统（升级为高级感配色方案）
# ==========================================
COLORS = {
    # 主色调 - 深邃靛蓝到魅惑紫渐变（高端感配色）
    "primary": "#4f46e5",
    "primary_light": "#818cf8",
    "secondary": "#7c3aed",
    "secondary_light": "#a78bfa",
    "gradient_start": "#4f46e5",
    "gradient_end": "#7c3aed",
    "gradient_hover_start": "#6366f1",
    "gradient_hover_end": "#8b5cf6",
    
    # 功能色
    "success": "#10b981",
    "success_light": "#34d399",
    "warning": "#f59e0b",
    "warning_light": "#fbbf24",
    "danger": "#ef4444",
    "danger_light": "#f87171",
    "info": "#3b82f6",
    "info_light": "#60a5fa",
    
    # 中性色
    "text_primary": "#1f2937",
    "text_secondary": "#6b7280",
    "text_light": "#9ca3af",
    "text_muted": "#d1d5db",
    "white": "#ffffff",
    "bg_card": "rgba(255, 255, 255, 0.95)",
    "bg_hover": "rgba(255, 255, 255, 0.98)",
    "border": "rgba(0, 0, 0, 0.08)",
    "border_light": "rgba(0, 0, 0, 0.05)",
}

# ==========================================
# 尺寸规范（优化后的尺寸系统）
# ==========================================
SIZES = {
    "content_max_width": "max-w-4xl",
    "content_padding": "px-6",
    "nav_height": "64px",
    "chart_height": "320px",
    "card_radius": "18px",
    "section_spacing": "48px",
    "section_radius": "24px",
}

# ==========================================
# 阴影系统（多层次阴影，增强层次感）
# ==========================================
SHADOWS = {
    "sm": "shadow-sm",
    "md": "shadow-md",
    "lg": "shadow-lg",
    "xl": "shadow-xl",
    "card": "shadow-md hover:shadow-lg transition-shadow duration-300",
    "card_hover": "shadow-lg",
}

# ==========================================
# 响应式断点
# ==========================================
BREAKPOINTS = {
    "mobile": "768px",
}

# ==========================================
# 公共CSS样式（单一数据源，确保全站统一）
# ==========================================
BASE_CSS = """
    <style>
        body {
            background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 50%, #6366f1 100%);
            min-height: 100vh;
            font-family: -apple-system, BlinkMacSystemFont, 'PingFang SC', 'Helvetica Neue', sans-serif;
            padding-top: 80px;
            color: #1f2937;
        }
        .content-area {
            max-width: 56rem;
            margin: 0 auto;
            padding: 0 1.5rem;
        }
        .back-button {
            display: inline-flex;
            align-items: center;
            color: white;
            opacity: 0.9;
            text-decoration: none;
            margin-bottom: 1.5rem;
            transition: opacity 0.2s;
            font-weight: 500;
        }
        .back-button:hover {
            opacity: 1;
        }
        /* 内容排版优化 */
        .prose-content p {
            margin-bottom: 1rem;
            line-height: 1.8;
            color: #374151;
            font-size: 15px;
        }
        .prose-content h3 {
            font-size: 1.25rem;
            font-weight: 700;
            margin-top: 1.75rem;
            margin-bottom: 0.75rem;
            color: #1f2937;
        }
        .prose-content h4 {
            font-size: 1.1rem;
            font-weight: 600;
            margin-top: 1.25rem;
            margin-bottom: 0.5rem;
            color: #374151;
        }
        .prose-content ul, .prose-content ol {
            margin-bottom: 1rem;
            padding-left: 1.5rem;
        }
        .prose-content li {
            margin-bottom: 0.5rem;
            line-height: 1.7;
            color: #4b5563;
        }
        .prose-content strong {
            color: #1f2937;
            font-weight: 600;
        }
        .prose-content code {
            background: #f3f4f6;
            padding: 0.125rem 0.375rem;
            border-radius: 0.375rem;
            font-size: 0.875rem;
            font-family: 'SF Mono', Monaco, 'Courier New', monospace;
        }
        .prose-content pre {
            background: #1f2937;
            color: #e5e7eb;
            padding: 1rem;
            border-radius: 0.75rem;
            overflow-x: auto;
            margin-bottom: 1rem;
        }
        .prose-content pre code {
            background: none;
            padding: 0;
            color: inherit;
        }
        /* 卡片通用样式 */
        .card {
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
            border-radius: 1rem;
            border: 1px solid rgba(0, 0, 0, 0.08);
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -2px rgba(0, 0, 0, 0.05);
            transition: all 0.3s ease;
        }
        .card:hover {
            box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -4px rgba(0, 0, 0, 0.05);
            transform: translateY(-1px);
        }
        /* 渐变文字 */
        .gradient-text {
            background: linear-gradient(135deg, #4f46e5, #7c3aed);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        @media (max-width: 768px) {
            body {
                padding-top: 70px;
            }
            .content-area {
                padding: 0 1rem;
            }
        }
    </style>
"""


# ==========================================
# 受保护文件（绝对不能覆盖）
# ==========================================
PROTECTED_FILES = [
    "index.html",
    "latest.html",
    "docs/templates/standard_navigation.html",
]

# ==========================================
# 已废弃目录（链接不应该指向这些）
# ==========================================
DEPRECATED_DIRS = [
    "催化日历",
]

# ==========================================
# 文件命名规范
# ==========================================
FILENAME_PATTERN = r"^\d{8}_.*\.html$"
