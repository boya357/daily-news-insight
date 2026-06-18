"""
V4 主题配置 - 白底清爽风格
专业、简洁、易读的投资研究界面

设计原则：
- 白底深色字，清晰易读
- 柔和阴影，层次分明
- 蓝色主调，专业可信
- 间距宽松，呼吸感强
"""


class V4Theme:
    """V4主题配置常量"""
    
    # 主色调
    PRIMARY_COLOR = '#2563EB'  # 主蓝色
    PRIMARY_LIGHT = '#3B82F6'
    PRIMARY_DARK = '#1D4ED8'
    
    SECONDARY_COLOR = '#64748B'  # 次级灰
    
    # 背景色
    BG_PAGE = '#F8FAFC'  # 页面背景 - 浅灰
    BG_CARD = '#FFFFFF'  # 卡片背景 - 纯白
    BG_SUBTLE = '#F1F5F9'  # 次级背景
    
    # 文字颜色
    TEXT_PRIMARY = '#1E293B'  # 主要文字 - 深灰
    TEXT_SECONDARY = '#64748B'  # 次级文字 - 中灰
    TEXT_MUTED = '#94A3B8'  # 弱化文字 - 浅灰
    TEXT_INVERTED = '#FFFFFF'  # 反白文字
    
    # 边框与分割线
    BORDER_COLOR = '#E2E8F0'  # 边框颜色
    BORDER_LIGHT = '#F1F5F9'  # 浅边框
    
    # 功能色
    SUCCESS = '#16A34A'  # 上涨/正收益 - 绿色
    DANGER = '#DC2626'   # 下跌/负收益 - 红色
    WARNING = '#F59E0B'  # 警示 - 橙色
    INFO = '#2563EB'     # 信息 - 蓝色
    
    # 红涨绿跌（A股习惯）
    UP_COLOR = '#DC2626'     # 上涨 - 红色
    DOWN_COLOR = '#16A34A'   # 下跌 - 绿色
    FLAT_COLOR = '#64748B'   # 平盘 - 灰色
    
    # 阴影
    SHADOW_SM = '0 1px 2px 0 rgba(0, 0, 0, 0.05)'
    SHADOW_DEFAULT = '0 1px 3px 0 rgba(0, 0, 0, 0.1), 0 1px 2px -1px rgba(0, 0, 0, 0.1)'
    SHADOW_MD = '0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -2px rgba(0, 0, 0, 0.1)'
    SHADOW_LG = '0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -4px rgba(0, 0, 0, 0.1)'
    SHADOW_CARD = '0 2px 8px rgba(0, 0, 0, 0.06)'
    
    # 圆角
    RADIUS_SM = '6px'
    RADIUS_DEFAULT = '10px'
    RADIUS_LG = '16px'
    RADIUS_XL = '20px'
    
    # 渐变
    GRADIENT_PRIMARY = 'linear-gradient(135deg, #2563EB 0%, #1D4ED8 100%)'
    GRADIENT_SUCCESS = 'linear-gradient(135deg, #10B981 0%, #059669 100%)'
    GRADIENT_DANGER = 'linear-gradient(135deg, #EF4444 0%, #DC2626 100%)'
    
    # 导航栏
    NAV_BG = 'rgba(255, 255, 255, 0.95)'
    NAV_BORDER = 'rgba(226, 232, 240, 0.8)'
    NAV_SHADOW = '0 1px 3px rgba(0, 0, 0, 0.05)'
    
    # 标签背景色
    TAG_BG_BLUE = 'rgba(37, 99, 235, 0.1)'
    TAG_BG_GREEN = 'rgba(22, 163, 74, 0.1)'
    TAG_BG_RED = 'rgba(220, 38, 38, 0.1)'
    TAG_BG_ORANGE = 'rgba(245, 158, 11, 0.1)'
    TAG_BG_GRAY = 'rgba(100, 116, 139, 0.1)'


def get_v4_theme_css() -> str:
    """获取V4主题全局CSS"""
    return '''
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@300;400;500;600;700;900&display=swap');
            
            * { 
                font-family: 'Noto Sans SC', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
                box-sizing: border-box;
            }
            
            body {
                background: #F8FAFC;
                min-height: 100vh;
                padding-top: 70px;
                color: #1E293B;
                line-height: 1.6;
            }
            
            .v4-container {
                max-width: 1200px;
                margin: 0 auto;
                padding: 0 24px;
            }
            
            .v4-container.narrow {
                max-width: 800px;
            }
            
            /* 卡片样式 */
            .v4-card {
                background: #FFFFFF;
                border: 1px solid #E2E8F0;
                border-radius: 16px;
                box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
                color: #1E293B;
                transition: box-shadow 0.2s ease, transform 0.2s ease;
            }
            
            .v4-card:hover {
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
            }
            
            .v4-card-header {
                padding: 20px 24px;
                border-bottom: 1px solid #F1F5F9;
                font-weight: 600;
                font-size: 1.125rem;
                color: #1E293B;
                display: flex;
                align-items: center;
                gap: 10px;
            }
            
            .v4-card-body {
                padding: 24px;
            }
            
            .v4-card-footer {
                padding: 16px 24px;
                border-top: 1px solid #F1F5F9;
                background: #F8FAFC;
                border-radius: 0 0 16px 16px;
            }
            
            /* 文字颜色 */
            .text-primary { color: #1E293B !important; }
            .text-secondary { color: #64748B !important; }
            .text-muted { color: #94A3B8 !important; }
            .text-up { color: #DC2626 !important; }
            .text-down { color: #16A34A !important; }
            .text-flat { color: #64748B !important; }
            .text-blue { color: #2563EB !important; }
            .text-orange { color: #F59E0B !important; }
            
            /* 背景色 */
            .bg-white { background: #FFFFFF !important; }
            .bg-gray-50 { background: #F8FAFC !important; }
            .bg-gray-100 { background: #F1F5F9 !important; }
            .bg-blue-50 { background: rgba(37, 99, 235, 0.05) !important; }
            .bg-green-50 { background: rgba(22, 163, 74, 0.05) !important; }
            .bg-red-50 { background: rgba(220, 38, 38, 0.05) !important; }
            
            /* 标签徽章 */
            .v4-tag {
                display: inline-block;
                padding: 4px 12px;
                border-radius: 20px;
                font-size: 12px;
                font-weight: 500;
                line-height: 1.5;
            }
            
            .v4-tag-blue {
                background: rgba(37, 99, 235, 0.1);
                color: #2563EB;
            }
            
            .v4-tag-green {
                background: rgba(22, 163, 74, 0.1);
                color: #16A34A;
            }
            
            .v4-tag-red {
                background: rgba(220, 38, 38, 0.1);
                color: #DC2626;
            }
            
            .v4-tag-orange {
                background: rgba(245, 158, 11, 0.1);
                color: #F59E0B;
            }
            
            .v4-tag-gray {
                background: rgba(100, 116, 139, 0.1);
                color: #64748B;
            }
            
            /* 章节标题 */
            .v4-section-title {
                font-size: 1.25rem;
                font-weight: 700;
                color: #1E293B;
                margin-bottom: 1rem;
                display: flex;
                align-items: center;
                gap: 0.75rem;
            }
            
            .v4-section-title .icon {
                font-size: 1.5rem;
            }
            
            /* 数据网格 */
            .v4-data-grid {
                display: grid;
                gap: 16px;
            }
            
            .v4-data-grid.cols-2 { grid-template-columns: repeat(2, 1fr); }
            .v4-data-grid.cols-3 { grid-template-columns: repeat(3, 1fr); }
            .v4-data-grid.cols-4 { grid-template-columns: repeat(4, 1fr); }
            
            @media (max-width: 768px) {
                .v4-data-grid.cols-2,
                .v4-data-grid.cols-3,
                .v4-data-grid.cols-4 {
                    grid-template-columns: 1fr;
                }
            }
            
            /* 数据项 */
            .v4-data-item {
                text-align: center;
                padding: 20px;
                background: #F8FAFC;
                border-radius: 12px;
            }
            
            .v4-data-item .label {
                font-size: 0.875rem;
                color: #64748B;
                margin-bottom: 8px;
            }
            
            .v4-data-item .value {
                font-size: 1.5rem;
                font-weight: 700;
                color: #1E293B;
            }
            
            .v4-data-item .value.small {
                font-size: 1.125rem;
            }
            
            /* 分割线 */
            .v4-divider {
                height: 1px;
                background: #E2E8F0;
                margin: 16px 0;
            }
            
            /* 进度条 */
            .v4-progress-bar {
                height: 8px;
                border-radius: 4px;
                background: #F1F5F9;
                overflow: hidden;
            }
            
            .v4-progress-fill {
                height: 100%;
                border-radius: 4px;
                transition: width 0.5s ease;
            }
            
            .v4-progress-fill.blue { background: linear-gradient(90deg, #2563EB, #3B82F6); }
            .v4-progress-fill.green { background: linear-gradient(90deg, #10B981, #34D399); }
            .v4-progress-fill.red { background: linear-gradient(90deg, #EF4444, #F87171); }
            .v4-progress-fill.orange { background: linear-gradient(90deg, #F59E0B, #FBBF24); }
            
            /* 股票卡片 */
            .v4-stock-card {
                background: #FFFFFF;
                border: 1px solid #E2E8F0;
                border-radius: 12px;
                padding: 20px;
                transition: all 0.2s ease;
            }
            
            .v4-stock-card:hover {
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
                transform: translateY(-2px);
            }
            
            .v4-stock-card .stock-header {
                display: flex;
                justify-content: space-between;
                align-items: center;
                margin-bottom: 12px;
            }
            
            .v4-stock-card .stock-name {
                font-size: 1.125rem;
                font-weight: 600;
                color: #1E293B;
            }
            
            .v4-stock-card .stock-code {
                font-size: 0.875rem;
                color: #94A3B8;
            }
            
            .v4-stock-card .stock-price {
                font-size: 1.75rem;
                font-weight: 700;
                margin: 8px 0;
            }
            
            .v4-stock-card .stock-change {
                font-size: 0.875rem;
                font-weight: 500;
            }
            
            /* 诊断指标 */
            .v4-diagnosis-grid {
                display: grid;
                grid-template-columns: repeat(4, 1fr);
                gap: 8px;
                margin-top: 16px;
            }
            
            .v4-diagnosis-item {
                text-align: center;
                padding: 10px 8px;
                background: #F8FAFC;
                border-radius: 8px;
            }
            
            .v4-diagnosis-item .dim-name {
                font-size: 0.75rem;
                color: #94A3B8;
                margin-bottom: 4px;
            }
            
            .v4-diagnosis-item .dim-value {
                font-size: 0.875rem;
                font-weight: 600;
                color: #1E293B;
            }
            
            .v4-diagnosis-item.good .dim-value { color: #16A34A; }
            .v4-diagnosis-item.bad .dim-value { color: #DC2626; }
            .v4-diagnosis-item.neutral .dim-value { color: #F59E0B; }
            
            /* 导航栏 */
            .v4-nav {
                position: fixed;
                top: 0;
                left: 0;
                right: 0;
                height: 60px;
                background: rgba(255, 255, 255, 0.95);
                backdrop-filter: blur(10px);
                -webkit-backdrop-filter: blur(10px);
                border-bottom: 1px solid rgba(226, 232, 240, 0.8);
                box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
                z-index: 1000;
                display: flex;
                align-items: center;
                padding: 0 24px;
            }
            
            .v4-nav-logo {
                font-size: 1.25rem;
                font-weight: 700;
                color: #2563EB;
                margin-right: 32px;
            }
            
            .v4-nav-menu {
                display: flex;
                gap: 4px;
                flex: 1;
            }
            
            .v4-nav-item {
                padding: 8px 16px;
                border-radius: 8px;
                font-size: 0.875rem;
                font-weight: 500;
                color: #64748B;
                cursor: pointer;
                transition: all 0.2s ease;
                text-decoration: none;
            }
            
            .v4-nav-item:hover {
                background: #F1F5F9;
                color: #1E293B;
            }
            
            .v4-nav-item.active {
                background: rgba(37, 99, 235, 0.1);
                color: #2563EB;
            }
            
            /* 页面标题区 */
            .v4-page-header {
                text-align: center;
                padding: 40px 0 32px;
            }
            
            .v4-page-header h1 {
                font-size: 2rem;
                font-weight: 800;
                color: #1E293B;
                margin: 0 0 8px 0;
            }
            
            .v4-page-header .subtitle {
                font-size: 1rem;
                color: #64748B;
                margin-bottom: 8px;
            }
            
            .v4-page-header .update-time {
                font-size: 0.875rem;
                color: #94A3B8;
            }
            
            /* 列表项 */
            .v4-list-item {
                display: flex;
                justify-content: space-between;
                align-items: center;
                padding: 12px 0;
                border-bottom: 1px solid #F1F5F9;
            }
            
            .v4-list-item:last-child {
                border-bottom: none;
            }
            
            .v4-list-item .item-label {
                color: #64748B;
                font-size: 0.875rem;
            }
            
            .v4-list-item .item-value {
                color: #1E293B;
                font-weight: 500;
            }
            
            /* 风险警示条 */
            .v4-alert {
                padding: 16px 20px;
                border-radius: 12px;
                border-left: 4px solid;
                margin-bottom: 16px;
            }
            
            .v4-alert.warning {
                background: rgba(245, 158, 11, 0.05);
                border-left-color: #F59E0B;
                color: #92400E;
            }
            
            .v4-alert.danger {
                background: rgba(220, 38, 38, 0.05);
                border-left-color: #DC2626;
                color: #991B1B;
            }
            
            .v4-alert.info {
                background: rgba(37, 99, 235, 0.05);
                border-left-color: #2563EB;
                color: #1E40AF;
            }
            
            .v4-alert.success {
                background: rgba(22, 163, 74, 0.05);
                border-left-color: #16A34A;
                color: #166534;
            }
            
            /* 回到顶部按钮 */
            #backToTop {
                position: fixed;
                bottom: 30px;
                right: 30px;
                width: 48px;
                height: 48px;
                background: #FFFFFF;
                border: 1px solid #E2E8F0;
                border-radius: 50%;
                display: flex;
                align-items: center;
                justify-content: center;
                color: #64748B;
                cursor: pointer;
                z-index: 9998;
                opacity: 0;
                transform: translateY(20px);
                transition: all 0.3s ease;
                box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
            }
            
            #backToTop:hover {
                background: #F8FAFC;
                color: #2563EB;
                box-shadow: 0 4px 12px rgba(37, 99, 235, 0.2);
            }
            
            #backToTop.visible {
                opacity: 1;
                transform: translateY(0);
            }
            
            /* 阅读进度条 */
            #progressBar {
                position: fixed;
                top: 0;
                left: 0;
                height: 3px;
                background: linear-gradient(90deg, #2563EB, #7C3AED);
                z-index: 1001;
                width: 0%;
                transition: width 0.1s ease;
            }
            
            /* 响应式 */
            @media (max-width: 768px) {
                body {
                    padding-top: 60px;
                }
                
                .v4-container {
                    padding: 0 16px;
                }
                
                .v4-page-header h1 {
                    font-size: 1.5rem;
                }
                
                .v4-card-body {
                    padding: 16px;
                }
                
                .v4-diagnosis-grid {
                    grid-template-columns: repeat(2, 1fr);
                }
                
                .v4-nav {
                    padding: 0 16px;
                }
                
                .v4-nav-menu {
                    overflow-x: auto;
                    -webkit-overflow-scrolling: touch;
                }
            }
        </style>
    '''
