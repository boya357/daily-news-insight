"""
Pro深色玻璃态组件库
专业投资监控界面组件，统一深色玻璃态视觉风格

【重要】为保证与现有Pro页面100%视觉兼容，
      组件CSS类名与原始portfolio_dashboard_pro保持一致。
      后续可逐步迁移到统一的pro-*命名规范。
"""
from .base import Component
from typing import List, Dict, Optional


class ProTheme:
    """Pro主题配置常量"""
    PRIMARY_COLOR = '#667eea'
    SECONDARY_COLOR = '#764ba2'
    ACCENT_COLOR = '#f093fb'
    
    BG_GRADIENT = 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)'
    
    GLASS_BG = 'rgba(139, 92, 246, 0.15)'
    GLASS_BORDER = 'rgba(255, 255, 255, 0.15)'
    GLASS_SHADOW = '0 15px 40px rgba(102, 126, 234, 0.4)'
    
    TEXT_PRIMARY = 'rgba(255, 255, 255, 0.95)'
    TEXT_SECONDARY = 'rgba(255, 255, 255, 0.8)'
    TEXT_MUTED = 'rgba(255, 255, 255, 0.6)'
    
    SUCCESS = '#10b981'
    WARNING = '#f59e0b'
    DANGER = '#ef4444'
    INFO = '#3b82f6'


def get_v4_theme_css() -> str:
    """获取V4主题全局CSS（深色玻璃态版）
    2026-07-03 更新：全站统一深色玻璃态，白底深字已废弃
    实际返回 get_pro_theme_css()
    """
    # 全站统一深色，V4白底彻底废弃
    return get_pro_theme_css()


def _deprecated_v4_white_theme() -> str:
    """[已废弃] 原V4白底样式，不再使用"""
    return '''
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@300;400;500;700;900&display=swap');
            
            * { font-family: 'Noto Sans SC', sans-serif; }
            
            body {
                background: linear-gradient(135deg, #f0f4ff 0%, #f8f0ff 100%);
                min-height: 100vh;
                padding-top: 80px;
                color: #1E293B;
            }
            
            .pro-container {
                max-width: 64rem;
                margin: 0 auto;
                padding: 0 1.5rem;
            }
            
            /* ===== V4 全局文字颜色转换（白→深） ===== */
            .pro-container .text-white,
            .pro-container .text-white\\/90,
            .pro-container .text-white\\/80,
            .pro-container .text-white\\/70,
            .pro-container .text-white\\/60,
            .pro-container .text-white\\/50,
            .pro-container .text-white\\/40,
            .pro-container .text-white\\/30,
            .pro-container .text-white\\/20,
            .pro-container .text-white\\/10,
            .pro-container .text-gray-100,
            .pro-container .text-gray-200,
            .pro-container .text-gray-300,
            .pro-container .text-blue-100,
            .pro-container .text-slate-100,
            .pro-container .text-slate-200,
            .pro-container .text-slate-300 { 
                color: #1E293B !important; 
            }
            .pro-container .text-white\\/90,
            .pro-container .text-white\\/80 { color: #334155 !important; }
            .pro-container .text-white\\/70 { color: #475569 !important; }
            .pro-container .text-white\\/60 { color: #64748B !important; }
            .pro-container .text-white\\/50 { color: #94A3B8 !important; }
            .pro-container .text-white\\/40,
            .pro-container .text-white\\/30,
            .pro-container .text-white\\/20,
            .pro-container .text-white\\/10 { color: #94A3B8 !important; }
            .pro-container .text-gray-200 { color: #334155 !important; }
            .pro-container .text-gray-300 { color: #475569 !important; }
            .pro-container .text-blue-100,
            .pro-container .text-slate-100,
            .pro-container .text-slate-200,
            .pro-container .text-slate-300 { color: #1E293B !important; }
            
            /* 导航栏文字转深色 */
            .glass-nav .text-white,
            .glass-nav .text-white\\/90,
            .glass-nav .text-white\\/80,
            .glass-nav .text-white\\/70 { color: #1E293B !important; }
            .glass-nav .text-white\\/80 { color: #334155 !important; }
            .glass-nav .text-white\\/70 { color: #475569 !important; }
            .glass-nav a:hover { color: #7C3AED !important; }
            .glass-nav .bg-white\\/20 { 
                background: rgba(124, 58, 237, 0.1) !important; 
                color: #7C3AED !important; 
            }
            
            /* 页脚文字转深色 */
            .pro-footer .text-white,
            .pro-footer .text-white\\/70,
            .pro-footer .text-white\\/60,
            .pro-footer .text-white\\/50,
            .pro-footer .text-white\\/40 { color: #64748B !important; }
            
            /* Hero区域标题 */
            .pro-container h1.text-white,
            .pro-container h1 { color: #1E293B !important; }
            .pro-container p.text-white\\/70 { color: #475569 !important; }
            
            /* ===== 深色背景元素保持白色文字 ===== */
            .bg-purple-600 .text-white,
            .bg-purple-700 .text-white,
            .bg-blue-600 .text-white,
            .bg-blue-700 .text-white,
            .bg-indigo-600 .text-white,
            .bg-indigo-700 .text-white,
            .bg-pink-500 .text-white,
            .bg-pink-600 .text-white,
            .bg-green-600 .text-white,
            .bg-green-700 .text-white,
            .bg-red-600 .text-white,
            .bg-red-700 .text-white,
            .bg-orange-500 .text-white,
            .bg-orange-600 .text-white,
            .bg-yellow-600 .text-white,
            .bg-emerald-600 .text-white,
            .bg-teal-600 .text-white,
            .bg-rose-600 .text-white,
            .bg-fuchsia-600 .text-white,
            .bg-violet-600 .text-white,
            .bg-sky-600 .text-white,
            .bg-purple-500 .text-white,
            .bg-blue-500 .text-white,
            .bg-indigo-500 .text-white { color: #FFFFFF !important; }
            .bg-purple-600 .text-white\\/70,
            .bg-blue-600 .text-white\\/70,
            .bg-indigo-600 .text-white\\/70,
            .bg-pink-500 .text-white\\/70,
            .bg-green-600 .text-white\\/70 { color: rgba(255,255,255,0.8) !important; }
            .risk-bar-fill .text-white,
            span.bg-purple-600,
            span.bg-blue-600,
            span.bg-green-600,
            span.bg-red-600,
            span.bg-pink-500,
            span.bg-orange-500 { color: #FFFFFF !important; }
            
            .card-glass {
                background: #FFFFFF;
                border: 1px solid #E2E8F0;
                box-shadow: 0 4px 20px rgba(0, 0, 0, 0.06);
                border-radius: 20px;
                color: #1E293B;
            }
            
            .card-glass .text-gray-800,
            .card-glass .text-gray-700,
            .card-glass .text-gray-600,
            .card-glass .text-gray-500,
            .card-glass .text-gray-400 { color: #475569 !important; }
            .card-glass .text-gray-500 { color: #64748B !important; }
            .card-glass .text-gray-400 { color: #94A3B8 !important; }
            
            /* 修复浅色背景子卡片文字颜色 */
            .card-glass .bg-white .text-gray-800 { color: #1f2937 !important; }
            .card-glass .bg-white .text-gray-700 { color: #374151 !important; }
            .card-glass .bg-white .text-gray-600 { color: #4b5563 !important; }
            .card-glass .bg-white .text-gray-500 { color: #6b7280 !important; }
            .card-glass .bg-white .text-gray-400 { color: #9ca3af !important; }
            
            .stock-card {
                transition: transform 0.3s ease, box-shadow 0.3s ease;
            }
            .stock-card:hover {
                transform: translateY(-4px);
                box-shadow: 0 12px 40px rgba(0, 0, 0, 0.1);
            }
            
            .risk-bar {
                height: 8px;
                border-radius: 4px;
                background: #E2E8F0;
                overflow: hidden;
            }
            .risk-bar-fill {
                height: 100%;
                border-radius: 4px;
                transition: width 0.5s ease;
            }
            
            .diagnosis-item {
                text-align: center;
                padding: 12px 8px;
                background: #F8FAFC;
                border-radius: 12px;
                border: 1px solid #E2E8F0;
            }
            
            .tag-badge {
                display: inline-block;
                padding: 4px 12px;
                border-radius: 20px;
                font-size: 12px;
                font-weight: 600;
            }
            
            .section-title {
                font-size: 1.25rem;
                font-weight: 700;
                color: #1E293B;
                margin-bottom: 1rem;
                display: flex;
                align-items: center;
                gap: 0.5rem;
            }
            
            .lhb-card {
                background: #F8FAFC;
                border-radius: 12px;
                padding: 1rem;
                border: 1px solid #E2E8F0;
            }
            
            .lhb-seat {
                font-size: 0.75rem;
                color: #64748B;
                margin-bottom: 0.25rem;
            }
            
            .fund-row {
                display: flex;
                justify-content: space-between;
                align-items: center;
                padding: 0.75rem 0;
                border-bottom: 1px solid #E2E8F0;
            }
            .fund-row:last-child {
                border-bottom: none;
            }
            
            .fund-trend-up {
                color: #DC2626;
                font-weight: 600;
            }
            .fund-trend-down {
                color: #16A34A;
                font-weight: 600;
            }
            
            .alert-section {
                border-left: 4px solid #ef4444;
                padding-left: 1rem;
                margin-bottom: 1rem;
            }
            
            .warning-section {
                border-left: 4px solid #f59e0b;
                padding-left: 1rem;
                margin-bottom: 1rem;
            }
            
            .safe-section {
                border-left: 4px solid #10b981;
                padding-left: 1rem;
                margin-bottom: 1rem;
            }
            
            /* 导航栏样式 - V4白色半透明 */
            .glass-nav {
                background: rgba(255, 255, 255, 0.9);
                backdrop-filter: blur(20px);
                -webkit-backdrop-filter: blur(20px);
                border-bottom: 1px solid rgba(0, 0, 0, 0.06);
                transition: background 0.3s ease;
            }
            
            .glass-nav.scrolled {
                background: rgba(255, 255, 255, 0.98);
                box-shadow: 0 2px 10px rgba(0, 0, 0, 0.06);
            }
            
            /* 导航文字颜色 - V4深色 */
            .glass-nav .nav-links a,
            .glass-nav .logo {
                color: #1E293B;
            }
            
            .glass-nav .nav-links a:hover,
            .glass-nav .nav-links a.bg-white\/20 {
                color: #667eea;
                background: rgba(102, 126, 234, 0.1);
            }
            
            /* 汉堡菜单按钮 - V4版本 */
            .hamburger-btn {
                display: none;
                background: rgba(0, 0, 0, 0.05);
                border: 1px solid rgba(0, 0, 0, 0.1);
                color: #1E293B;
                width: 40px;
                height: 40px;
                border-radius: 8px;
                cursor: pointer;
                font-size: 18px;
                transition: all 0.3s;
            }
            
            .hamburger-btn:hover {
                background: rgba(0, 0, 0, 0.08);
            }
            
            /* 移动端菜单 - V4版本 */
            .mobile-menu {
                display: none;
                position: fixed;
                top: 0;
                left: 0;
                right: 0;
                bottom: 0;
                background: rgba(255, 255, 255, 0.98);
                backdrop-filter: blur(20px);
                -webkit-backdrop-filter: blur(20px);
                z-index: 100;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                padding: 2rem;
            }
            
            .mobile-menu.show {
                display: flex;
            }
            
            .mobile-menu-item {
                color: #1E293B;
                font-size: 18px;
                font-weight: 600;
                padding: 15px 30px;
                text-decoration: none;
                text-align: center;
                width: 100%;
                max-width: 300px;
                border-bottom: 1px solid #E2E8F0;
                transition: all 0.3s;
            }
            
            .mobile-menu-item:hover {
                background: rgba(102, 126, 234, 0.05);
                color: #667eea;
            }
            
            .close-menu-btn {
                position: absolute;
                top: 20px;
                right: 20px;
                background: rgba(0, 0, 0, 0.05);
                border: 1px solid rgba(0, 0, 0, 0.1);
                color: #1E293B;
                width: 44px;
                height: 44px;
                border-radius: 8px;
                cursor: pointer;
                font-size: 20px;
                transition: all 0.3s;
            }
            
            .close-menu-btn:hover {
                background: rgba(0, 0, 0, 0.08);
            }
            
            /* 响应式断点 - 平板 */
            @media (max-width: 1024px) {
                .pro-container {
                    max-width: 100%;
                    padding: 0 1rem;
                }
            }
            
            /* 响应式断点 - 手机 */
            @media (max-width: 768px) {
                .nav-links {
                    display: none !important;
                }
                
                .hamburger-btn {
                    display: block !important;
                }
                
                body {
                    padding-top: 70px;
                }
                
                .pro-container {
                    padding: 0 0.75rem;
                }
                
                .card-glass {
                    border-radius: 16px;
                    padding: 1.25rem;
                }
                
                /* 移动端网格优化 */
                .grid-cols-2,
                .grid-cols-3,
                .grid-cols-4,
                .grid-cols-5 {
                    grid-template-columns: 1fr !important;
                }
                
                /* 移动端字体优化 */
                h1 { font-size: 1.75rem !important; }
                h2 { font-size: 1.35rem !important; }
                h3 { font-size: 1.15rem !important; }
            }
            
            /* 响应式断点 - 小屏手机 */
            @media (max-width: 480px) {
                body {
                    padding-top: 60px;
                }
                
                .pro-container {
                    padding: 0 0.5rem;
                }
                
                .card-glass {
                    border-radius: 12px;
                    padding: 1rem;
                }
                
                h1 { font-size: 1.5rem !important; }
                h2 { font-size: 1.2rem !important; }
            }

            /* ===== 交互动效增强 ===== */
            
            /* 卡片入场动画 */
            @keyframes fadeInUp {
                from {
                    opacity: 0;
                    transform: translateY(20px);
                }
                to {
                    opacity: 1;
                    transform: translateY(0);
                }
            }
            
            .animate-fade-in-up {
                animation: fadeInUp 0.6s ease-out forwards;
            }
            
            /* 数字滚动动画容器 */
            .counter-value {
                font-variant-numeric: tabular-nums;
            }
            
            /* 脉冲动画 */
            @keyframes pulse {
                0%, 100% { opacity: 1; }
                50% { opacity: 0.5; }
            }
            
            .animate-pulse {
                animation: pulse 2s cubic-bezier(0.4, 0, 0.6, 1) infinite;
            }
            
            /* 骨架屏加载效果 - V4版本 */
            @keyframes shimmer {
                0% { background-position: -200% 0; }
                100% { background-position: 200% 0; }
            }
            
            .skeleton {
                background: linear-gradient(90deg, #f0f0f0 25%, #e0e0e0 50%, #f0f0f0 75%);
                background-size: 200% 100%;
                animation: shimmer 1.5s infinite;
                border-radius: 8px;
            }
            
            /* 按钮点击效果 */
            .btn-press:active {
                transform: scale(0.95);
            }
            
            /* 标签悬浮效果 */
            .tag-badge {
                transition: all 0.2s ease;
            }
            
            .tag-badge:hover {
                transform: translateY(-2px);
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
            }
            

            /* 阅读进度条 */
            #progressBar {
                position: fixed;
                top: 0;
                left: 0;
                height: 3px;
                background: linear-gradient(90deg, #6366f1, #a855f7, #ec4899);
                z-index: 9999;
                width: 0%;
                transition: width 0.1s ease;
            }
            
            /* 回到顶部按钮 */
            #backToTop {
                position: fixed;
                bottom: 30px;
                right: 30px;
                width: 50px;
                height: 50px;
                background: linear-gradient(135deg, #6366f1, #a855f7);
                border-radius: 50%;
                display: flex;
                align-items: center;
                justify-content: center;
                color: white;
                cursor: pointer;
                z-index: 9998;
                opacity: 0;
                transform: translateY(20px);
                transition: all 0.3s ease;
                box-shadow: 0 4px 15px rgba(99, 102, 241, 0.3);
                border: none;
            }
            #backToTop:hover {
                transform: translateY(-3px);
                box-shadow: 0 6px 20px rgba(99, 102, 241, 0.4);
            }
            #backToTop.visible {
                opacity: 1;
                transform: translateY(0);
            }
            
            /* 操作按钮组 */
            .action-buttons {
                position: fixed;
                bottom: 30px;
                left: 30px;
                display: flex;
                flex-direction: column;
                gap: 12px;
                z-index: 9998;
            }
            .action-btn {
                width: 50px;
                height: 50px;
                background: rgba(255, 255, 255, 0.95);
                backdrop-filter: blur(20px);
                -webkit-backdrop-filter: blur(20px);
                border: 1px solid rgba(0, 0, 0, 0.1);
                border-radius: 50%;
                display: flex;
                align-items: center;
                justify-content: center;
                color: #1E293B;
                cursor: pointer;
                transition: all 0.3s ease;
                box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
            }
            .action-btn:hover {
                background: rgba(99, 102, 241, 0.1);
                color: #6366f1;
                transform: translateY(-3px);
                box-shadow: 0 6px 20px rgba(99, 102, 241, 0.2);
            }
            
            /* 打印优化 */
            @media print {
                #progressBar, #backToTop, .action-buttons, .glass-nav, .pro-footer {
                    display: none !important;
                }
                body {
                    background: white !important;
                    color: black !important;
                }
                .card-glass {
                    background: white !important;
                    border: 1px solid #ddd !important;
                    box-shadow: none !important;
                }
            }
            
            /* 移动端适配 */
            @media (max-width: 768px) {
                #backToTop {
                    bottom: 20px;
                    right: 20px;
                    width: 44px;
                    height: 44px;
                }
                .action-buttons {
                    bottom: 20px;
                    left: 20px;
                    gap: 10px;
                }
                .action-btn {
                    width: 44px;
                    height: 44px;
                }
            }
            /* 进度条动画增强 */
            .risk-bar-fill {
                transition: width 1s cubic-bezier(0.4, 0, 0.2, 1);
            }
            
            /* 卡片悬浮增强 */
            .card-glass {
                transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            }
            
            .card-glass:hover {
                transform: translateY(-4px);
                box-shadow: 0 12px 30px rgba(0, 0, 0, 0.1);
            }
            
            /* 导航项下划线动画 */
            .nav-links a {
                position: relative;
            }
            
            .nav-links a::after {
                content: '';
                position: absolute;
                bottom: -2px;
                left: 50%;
                width: 0;
                height: 2px;
                background: linear-gradient(90deg, #667eea, #764ba2);
                transition: all 0.3s ease;
                transform: translateX(-50%);
                border-radius: 1px;
            }
            
            .nav-links a:hover::after,
            .nav-links a.bg-white\/20::after {
                width: 60%;
            }
            
            /* 滚动显示动画 */
            .reveal {
                opacity: 0;
                transform: translateY(30px);
                transition: all 0.8s cubic-bezier(0.4, 0, 0.2, 1);
            }
            
            .reveal.visible {
                opacity: 1;
                transform: translateY(0);
            }
            
            /* 弹跳效果 */
            @keyframes bounce {
                0%, 100% { transform: translateY(0); }
                50% { transform: translateY(-10px); }
            }
            
            .animate-bounce {
                animation: bounce 2s infinite;
            }
            
            /* 旋转动画 */
            @keyframes spin {
                from { transform: rotate(0deg); }
                to { transform: rotate(360deg); }
            }
            
            .animate-spin {
                animation: spin 1s linear infinite;
            }
            
            /* ===== 移动端体验优化 ===== */
            
            /* 触摸区域优化 - 最小44px点击区域 */
            @media (max-width: 768px) {
                .mobile-menu-item {
                    min-height: 44px;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    padding: 12px 20px;
                    -webkit-tap-highlight-color: transparent;
                }
                
                .hamburger-btn,
                .close-menu-btn {
                    min-width: 44px;
                    min-height: 44px;
                    -webkit-tap-highlight-color: transparent;
                }
                
                /* 移动端卡片点击反馈 */
                .card-glass:active {
                    transform: scale(0.98);
                    transition: transform 0.1s ease;
                }
                
                /* 禁止双击缩放 */
                * {
                    touch-action: manipulation;
                }
                
                /* 底部安全区域适配 */
                .pro-container {
                    padding-bottom: calc(1rem + env(safe-area-inset-bottom, 0px));
                }
                
                /* 移动端滚动条样式 */
                ::-webkit-scrollbar {
                    width: 4px;
                    height: 4px;
                }
                
                ::-webkit-scrollbar-track {
                    background: transparent;
                }
                
                ::-webkit-scrollbar-thumb {
                    background: rgba(0, 0, 0, 0.2);
                    border-radius: 2px;
                }
                
                /* 移动端标题截断 */
                .section-title {
                    font-size: 1.1rem !important;
                }
                
                /* 移动端网格优化 - 2列布局 */
                .mobile-grid-2 {
                    grid-template-columns: repeat(2, 1fr) !important;
                }
                
                /* 移动端字体优化 */
                body {
                    font-size: 15px;
                    -webkit-font-smoothing: antialiased;
                    -moz-osx-font-smoothing: grayscale;
                }
            }
            
            /* 小屏手机额外优化 */
            @media (max-width: 480px) {
                .mobile-grid-2 {
                    grid-template-columns: 1fr !important;
                }
                
                /* 更小的内边距 */
                .card-glass {
                    padding: 0.875rem !important;
                }
                
                .section-title {
                    font-size: 1rem !important;
                }
            }
            
            /* ===== 深色模式优化 ===== */
            @media (prefers-color-scheme: dark) {
                .text-white\/60 {
                    color: rgba(255, 255, 255, 0.7) !important;
                }
            }
            
            /* ===== 减少动效模式 ===== */
            @media (prefers-reduced-motion: reduce) {
                *,
                *::before,
                *::after {
                    animation-duration: 0.01ms !important;
                    animation-iteration-count: 1 !important;
                    transition-duration: 0.01ms !important;
                }
            }
        
            /* ===== 悬浮目录导航 - V4版本 ===== */
            .toc-wrapper {
                position: fixed;
                top: 120px;
                width: 220px;
                max-height: calc(100vh - 160px);
                background: #FFFFFF;
                backdrop-filter: blur(20px);
                -webkit-backdrop-filter: blur(20px);
                border: 1px solid #E2E8F0;
                border-radius: 16px;
                box-shadow: 0 8px 30px rgba(0, 0, 0, 0.08);
                z-index: 90;
                overflow: hidden;
                transition: all 0.3s ease;
            }
            
            .toc-right {
                right: 20px;
            }
            
            .toc-left {
                left: 20px;
            }
            
            .toc-header {
                display: flex;
                align-items: center;
                justify-content: space-between;
                padding: 12px 16px;
                cursor: pointer;
                border-bottom: 1px solid #E2E8F0;
                user-select: none;
            }
            
            .toc-title {
                font-size: 0.875rem;
                font-weight: 600;
                color: #1E293B;
            }
            
            .toc-header svg {
                color: #64748B;
                transition: transform 0.3s ease;
            }
            
            .toc-wrapper.collapsed .toc-header svg {
                transform: rotate(-90deg);
            }
            
            .toc-content {
                max-height: calc(100vh - 220px);
                overflow-y: auto;
                padding: 8px 0;
                transition: max-height 0.3s ease;
            }
            
            .toc-wrapper.collapsed .toc-content {
                max-height: 0;
                padding: 0;
                overflow: hidden;
            }
            
            .toc-item {
                display: block;
                padding: 8px 16px;
                font-size: 0.8125rem;
                color: #64748B;
                text-decoration: none;
                border-left: 3px solid transparent;
                transition: all 0.2s ease;
                cursor: pointer;
            }
            
            .toc-item:hover {
                color: #1E293B;
                background: #F8FAFC;
                border-left-color: #CBD5E1;
            }
            
            .toc-item.active {
                color: #667eea;
                font-weight: 500;
                background: rgba(102, 126, 234, 0.08);
                border-left-color: #667eea;
            }
            
            .toc-item.pl-4 {
                padding-left: 32px;
                font-size: 0.75rem;
            }
            
            /* 滚动条样式 */
            .toc-content::-webkit-scrollbar {
                width: 4px;
            }
            
            .toc-content::-webkit-scrollbar-track {
                background: transparent;
            }
            
            .toc-content::-webkit-scrollbar-thumb {
                background: #CBD5E1;
                border-radius: 2px;
            }
            
            .toc-content::-webkit-scrollbar-thumb:hover {
                background: #94A3B8;
            }
            
            /* 大屏显示优化 */
            @media (min-width: 1400px) {
                .toc-wrapper {
                    width: 260px;
                }
                .toc-right {
                    right: calc((100vw - 64rem) / 2 - 300px);
                }
                .toc-left {
                    left: calc((100vw - 64rem) / 2 - 300px);
                }
            }
            
                        /* 平板端优化 - 折叠为悬浮按钮 */
            @media (max-width: 1200px) {
                .toc-wrapper {
                    top: auto;
                    bottom: 80px;
                    right: 16px;
                    width: 44px;
                    height: 44px;
                    border-radius: 50%;
                    overflow: hidden;
                    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
                }
                
                .toc-wrapper.expanded {
                    width: 240px;
                    height: auto;
                    max-height: 60vh;
                    border-radius: 16px;
                    top: auto;
                    bottom: 80px;
                }
                
                .toc-wrapper .toc-header {
                    justify-content: center;
                    padding: 12px;
                    border-bottom: none;
                }
                
                .toc-wrapper.expanded .toc-header {
                    justify-content: space-between;
                    padding: 12px 16px;
                    border-bottom: 1px solid #E2E8F0;
                }
                
                .toc-wrapper .toc-title {
                    display: none;
                }
                
                .toc-wrapper.expanded .toc-title {
                    display: block;
                    font-size: 0.875rem;
                }
                
                .toc-wrapper .toc-content {
                    max-height: 0;
                    padding: 0;
                    opacity: 0;
                    transition: all 0.3s ease;
                }
                
                .toc-wrapper.expanded .toc-content {
                    max-height: calc(60vh - 56px);
                    padding: 8px 0;
                    opacity: 1;
                }
                
                .toc-wrapper .toc-header svg {
                    width: 20px;
                    height: 20px;
                }
            }
            
            /* 手机端 - 更小的悬浮按钮 */
            @media (max-width: 480px) {
                .toc-wrapper {
                    width: 40px;
                    height: 40px;
                    bottom: 70px;
                    right: 12px;
                }
                
                .toc-wrapper.expanded {
                    width: 200px;
                }
                
                .toc-wrapper.expanded .toc-title {
                    font-size: 0.8rem;
                }
            }
            
            /* 页面内容区域适配 - 避免被目录遮挡 */
            @media (min-width: 1200px) {
                .pro-container.has-toc {
                    max-width: 48rem;
                }
            }
            
            /* Tab切换组件样式 - V4版本 */
            .tab-container {
                margin-bottom: 1rem;
            }
            
            .tab-buttons {
                display: flex;
                gap: 0.5rem;
                margin-bottom: 1rem;
                border-bottom: 1px solid #E2E8F0;
                padding-bottom: 0.5rem;
            }
            
            .tab-btn {
                padding: 0.5rem 1rem;
                background: #F8FAFC;
                border: 1px solid #E2E8F0;
                border-radius: 8px;
                color: #64748B;
                cursor: pointer;
                font-size: 0.875rem;
                transition: all 0.3s ease;
            }
            
            .tab-btn:hover {
                background: #F1F5F9;
                color: #475569;
            }
            
            .tab-btn-active {
                background: rgba(102, 126, 234, 0.1);
                border-color: rgba(102, 126, 234, 0.3);
                color: #667eea;
                font-weight: 500;
            }
            
            .tab-container .tab-content .tab-panel {
                display: none;
                animation: fadeIn 0.3s ease;
            }
            
            .tab-container .tab-content .tab-panel.tab-panel-active {
                display: block !important;
            }
            
            @keyframes fadeIn {
                from { opacity: 0; transform: translateY(10px); }
                to { opacity: 1; transform: translateY(0); }
            }
            
            /* Underline风格Tab - V4版本 */
            .tab-style-underline .tab-buttons {
                border-bottom: none;
                padding-bottom: 0;
                gap: 1.5rem;
            }
            
            .tab-style-underline .tab-btn {
                background: transparent;
                border: none;
                border-bottom: 2px solid transparent;
                border-radius: 0;
                padding: 0.5rem 0;
            }
            
            .tab-style-underline .tab-btn:hover {
                background: transparent;
                color: #475569;
            }
            
            .tab-style-underline .tab-btn-active {
                border-bottom-color: #667eea;
                color: #667eea;
                background: transparent;
            }
            
            /* 次级卡片样式 - V4版本 */
            .card-subtle {
                background: #F8FAFC;
                border: 1px solid #E2E8F0;
                border-radius: 12px;
                padding: 1rem;
                transition: all 0.3s ease;
            }
            
            .card-subtle:hover {
                background: #F1F5F9;
                border-color: #CBD5E1;
            }
            
            /* ===== 文字颜色工具类 - V4版本 ===== */
            .text-up { color: #DC2626 !important; }
            .text-down { color: #16A34A !important; }
            .text-flat { color: #64748B !important; }
            
            /* 页脚样式 */
            .pro-footer {
                margin-top: 3rem;
                padding: 2rem 0;
                text-align: center;
                color: #64748B;
                font-size: 0.875rem;
                border-top: 1px solid #E2E8F0;
            }
</style>
    '''


def get_pro_theme_css() -> str:
    """获取Pro主题全局CSS
    
    与portfolio_dashboard_pro.py中的_generate_dark_theme_css完全一致
    确保视觉效果100%兼容
    """
    return '''
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@300;400;500;700;900&display=swap');
            
            * { font-family: 'Noto Sans SC', sans-serif; }
            
            body {
                background: linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%) !important;
                min-height: 100vh;
                padding-top: 80px;
                color: rgba(255,255,255,0.95);
            }
            
            .pro-container {
                max-width: 64rem;
                margin: 0 auto;
                padding: 0 1.5rem;
            }
            
            .card-glass {
                background: rgba(255, 255, 255, 0.07) !important;
                backdrop-filter: blur(20px);
                -webkit-backdrop-filter: blur(20px);
                border: 1px solid rgba(255, 255, 255, 0.12) !important;
                box-shadow: 0 8px 32px rgba(0, 0, 0, 0.35);
                border-radius: 20px;
                color: rgba(255,255,255,0.95) !important;
            }
            
            .card-glass .text-gray-800,
            .card-glass .text-gray-700,
            .card-glass .text-gray-600,
            .card-glass .text-gray-500,
            .card-glass .text-gray-400 { color: rgba(255, 255, 255, 0.9) !important; }
            .card-glass .text-gray-500 { color: rgba(255, 255, 255, 0.75) !important; }
            .card-glass .text-gray-400 { color: rgba(255, 255, 255, 0.6) !important; }
            
            /* 修复浅色背景子卡片文字颜色 */
            .card-glass .bg-white .text-gray-800 { color: #1f2937 !important; }
            .card-glass .bg-white .text-gray-700 { color: #374151 !important; }
            .card-glass .bg-white .text-gray-600 { color: #4b5563 !important; }
            .card-glass .bg-white .text-gray-500 { color: #6b7280 !important; }
            .card-glass .bg-white .text-gray-400 { color: #9ca3af !important; }
            
            .stock-card {
                transition: transform 0.3s ease, box-shadow 0.3s ease;
            }
            .stock-card:hover {
                transform: translateY(-4px);
                box-shadow: 0 20px 60px rgba(102, 126, 234, 0.5);
            }
            
            .risk-bar {
                height: 8px;
                border-radius: 4px;
                background: rgba(255,255,255,0.2);
                overflow: hidden;
            }
            .risk-bar-fill {
                height: 100%;
                border-radius: 4px;
                transition: width 0.5s ease;
            }
            
            .diagnosis-item {
                text-align: center;
                padding: 12px 8px;
                background: rgba(255,255,255,0.1);
                border-radius: 12px;
            }
            
            .tag-badge {
                display: inline-block;
                padding: 4px 12px;
                border-radius: 20px;
                font-size: 12px;
                font-weight: 600;
            }
            
            .section-title {
                font-size: 1.25rem;
                font-weight: 700;
                color: white;
                margin-bottom: 1rem;
                display: flex;
                align-items: center;
                gap: 0.5rem;
            }
            
            .lhb-card {
                background: rgba(255,255,255,0.05);
                border-radius: 12px;
                padding: 1rem;
                border: 1px solid rgba(255,255,255,0.1);
            }
            
            .lhb-seat {
                font-size: 0.75rem;
                color: rgba(255,255,255,0.6);
                margin-bottom: 0.25rem;
            }
            
            .fund-row {
                display: flex;
                justify-content: space-between;
                align-items: center;
                padding: 0.75rem 0;
                border-bottom: 1px solid rgba(255,255,255,0.1);
            }
            .fund-row:last-child {
                border-bottom: none;
            }
            
            .fund-trend-up {
                color: #10b981;
                font-weight: 600;
            }
            .fund-trend-down {
                color: #ef4444;
                font-weight: 600;
            }
            
            .alert-section {
                border-left: 4px solid #ef4444;
                padding-left: 1rem;
                margin-bottom: 1rem;
            }
            
            .warning-section {
                border-left: 4px solid #f59e0b;
                padding-left: 1rem;
                margin-bottom: 1rem;
            }
            
            .safe-section {
                border-left: 4px solid #10b981;
                padding-left: 1rem;
                margin-bottom: 1rem;
            }
            
            /* 导航栏样式 */
            .glass-nav {
                background: rgba(15, 12, 41, 0.75) !important;
                backdrop-filter: blur(30px);
                -webkit-backdrop-filter: blur(20px);
                border-bottom: 1px solid rgba(255, 255, 255, 0.1);
                transition: background 0.3s ease;
            }
            
            .glass-nav.scrolled {
                background: rgba(0, 0, 0, 0.7);
            }
            
            /* 汉堡菜单按钮 */
            .hamburger-btn {
                display: none;
                background: rgba(255, 255, 255, 0.1);
                border: 1px solid rgba(255, 255, 255, 0.2);
                color: white;
                width: 40px;
                height: 40px;
                border-radius: 8px;
                cursor: pointer;
                font-size: 18px;
                transition: all 0.3s;
            }
            
            .hamburger-btn:hover {
                background: rgba(255, 255, 255, 0.2);
            }
            
            /* 移动端菜单 */
            .mobile-menu {
                display: none;
                position: fixed;
                top: 0;
                left: 0;
                right: 0;
                bottom: 0;
                background: rgba(0, 0, 0, 0.95);
                backdrop-filter: blur(20px);
                -webkit-backdrop-filter: blur(20px);
                z-index: 100;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                padding: 2rem;
            }
            
            .mobile-menu.show {
                display: flex;
            }
            
            .mobile-menu-item {
                color: white;
                font-size: 18px;
                font-weight: 600;
                padding: 15px 30px;
                text-decoration: none;
                text-align: center;
                width: 100%;
                max-width: 300px;
                border-bottom: 1px solid rgba(255, 255, 255, 0.2);
                transition: all 0.3s;
            }
            
            .mobile-menu-item:hover {
                background: rgba(255, 255, 255, 0.1);
                color: #a78bfa;
            }
            
            .close-menu-btn {
                position: absolute;
                top: 20px;
                right: 20px;
                background: rgba(255, 255, 255, 0.1);
                border: 1px solid rgba(255, 255, 255, 0.2);
                color: white;
                width: 44px;
                height: 44px;
                border-radius: 8px;
                cursor: pointer;
                font-size: 20px;
                transition: all 0.3s;
            }
            
            .close-menu-btn:hover {
                background: rgba(255, 255, 255, 0.2);
            }
            
            /* 响应式断点 - 平板 */
            @media (max-width: 1024px) {
                .pro-container {
                    max-width: 100%;
                    padding: 0 1rem;
                }
            }
            
            /* 响应式断点 - 手机 */
            @media (max-width: 768px) {
                .nav-links {
                    display: none !important;
                }
                
                .hamburger-btn {
                    display: block !important;
                }
                
                body {
                    padding-top: 70px;
                }
                
                .pro-container {
                    padding: 0 0.75rem;
                }
                
                .card-glass {
                    border-radius: 16px;
                    padding: 1.25rem;
                }
                
                /* 移动端网格优化 */
                .grid-cols-2,
                .grid-cols-3,
                .grid-cols-4,
                .grid-cols-5 {
                    grid-template-columns: 1fr !important;
                }
                
                /* 移动端字体优化 */
                h1 { font-size: 1.75rem !important; }
                h2 { font-size: 1.35rem !important; }
                h3 { font-size: 1.15rem !important; }
            }
            
            /* 响应式断点 - 小屏手机 */
            @media (max-width: 480px) {
                body {
                    padding-top: 60px;
                }
                
                .pro-container {
                    padding: 0 0.5rem;
                }
                
                .card-glass {
                    border-radius: 12px;
                    padding: 1rem;
                }
                
                h1 { font-size: 1.5rem !important; }
                h2 { font-size: 1.2rem !important; }
            }

            /* ===== 交互动效增强 ===== */
            
            /* 卡片入场动画 */
            @keyframes fadeInUp {
                from {
                    opacity: 0;
                    transform: translateY(20px);
                }
                to {
                    opacity: 1;
                    transform: translateY(0);
                }
            }
            
            .animate-fade-in-up {
                animation: fadeInUp 0.6s ease-out forwards;
            }
            
            /* 数字滚动动画容器 */
            .counter-value {
                font-variant-numeric: tabular-nums;
            }
            
            /* 脉冲动画 */
            @keyframes pulse {
                0%, 100% { opacity: 1; }
                50% { opacity: 0.5; }
            }
            
            .animate-pulse {
                animation: pulse 2s cubic-bezier(0.4, 0, 0.6, 1) infinite;
            }
            
            /* 骨架屏加载效果 */
            @keyframes shimmer {
                0% { background-position: -200% 0; }
                100% { background-position: 200% 0; }
            }
            
            .skeleton {
                background: linear-gradient(90deg, rgba(255,255,255,0.1) 25%, rgba(255,255,255,0.2) 50%, rgba(255,255,255,0.1) 75%);
                background-size: 200% 100%;
                animation: shimmer 1.5s infinite;
                border-radius: 8px;
            }
            
            /* 按钮点击效果 */
            .btn-press:active {
                transform: scale(0.95);
            }
            
            /* 标签悬浮效果 */
            .tag-badge {
                transition: all 0.2s ease;
            }
            
            .tag-badge:hover {
                transform: translateY(-2px);
                box-shadow: 0 4px 12px rgba(102, 126, 234, 0.4);
            }
            

            /* 阅读进度条 */
            #progressBar {
                position: fixed;
                top: 0;
                left: 0;
                height: 3px;
                background: linear-gradient(90deg, #6366f1, #a855f7, #ec4899);
                z-index: 9999;
                width: 0%;
                transition: width 0.1s ease;
            }
            
            /* 回到顶部按钮 */
            #backToTop {
                position: fixed;
                bottom: 30px;
                right: 30px;
                width: 50px;
                height: 50px;
                background: linear-gradient(135deg, #6366f1, #a855f7);
                border-radius: 50%;
                display: flex;
                align-items: center;
                justify-content: center;
                color: white;
                cursor: pointer;
                z-index: 9998;
                opacity: 0;
                transform: translateY(20px);
                transition: all 0.3s ease;
                box-shadow: 0 4px 15px rgba(99, 102, 241, 0.4);
                border: none;
            }
            #backToTop:hover {
                transform: translateY(-3px);
                box-shadow: 0 6px 20px rgba(99, 102, 241, 0.5);
            }
            #backToTop.visible {
                opacity: 1;
                transform: translateY(0);
            }
            
            /* 操作按钮组 */
            .action-buttons {
                position: fixed;
                bottom: 30px;
                left: 30px;
                display: flex;
                flex-direction: column;
                gap: 12px;
                z-index: 9998;
            }
            .action-btn {
                width: 50px;
                height: 50px;
                background: rgba(30, 30, 50, 0.8);
                backdrop-filter: blur(20px);
                -webkit-backdrop-filter: blur(20px);
                border: 1px solid rgba(255, 255, 255, 0.1);
                border-radius: 50%;
                display: flex;
                align-items: center;
                justify-content: center;
                color: white;
                cursor: pointer;
                transition: all 0.3s ease;
                box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
            }
            .action-btn:hover {
                background: rgba(99, 102, 241, 0.8);
                transform: translateY(-3px);
                box-shadow: 0 6px 20px rgba(99, 102, 241, 0.4);
            }
            
            /* 打印优化 */
            @media print {
                #progressBar, #backToTop, .action-buttons, .glass-nav, .pro-footer {
                    display: none !important;
                }
                body {
                    background: white !important;
                    color: black !important;
                }
                .card-glass {
                    background: white !important;
                    border: 1px solid #ddd !important;
                    box-shadow: none !important;
                }
            }
            
            /* 移动端适配 */
            @media (max-width: 768px) {
                #backToTop {
                    bottom: 20px;
                    right: 20px;
                    width: 44px;
                    height: 44px;
                }
                .action-buttons {
                    bottom: 20px;
                    left: 20px;
                    gap: 10px;
                }
                .action-btn {
                    width: 44px;
                    height: 44px;
                }
            }
            /* 进度条动画增强 */
            .risk-bar-fill {
                transition: width 1s cubic-bezier(0.4, 0, 0.2, 1);
            }
            
            /* 卡片悬浮增强 */
            .card-glass {
                transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            }
            
            .card-glass:hover {
                transform: translateY(-4px);
                box-shadow: 0 20px 40px rgba(102, 126, 234, 0.3);
            }
            
            /* 导航项下划线动画 */
            .nav-links a {
                position: relative;
            }
            
            .nav-links a::after {
                content: '';
                position: absolute;
                bottom: -2px;
                left: 50%;
                width: 0;
                height: 2px;
                background: linear-gradient(90deg, #667eea, #764ba2);
                transition: all 0.3s ease;
                transform: translateX(-50%);
                border-radius: 1px;
            }
            
            .nav-links a:hover::after,
            .nav-links a.bg-white\/20::after {
                width: 60%;
            }
            
            /* 滚动显示动画 */
            .reveal {
                opacity: 0;
                transform: translateY(30px);
                transition: all 0.8s cubic-bezier(0.4, 0, 0.2, 1);
            }
            
            .reveal.visible {
                opacity: 1;
                transform: translateY(0);
            }
            
            /* 弹跳效果 */
            @keyframes bounce {
                0%, 100% { transform: translateY(0); }
                50% { transform: translateY(-10px); }
            }
            
            .animate-bounce {
                animation: bounce 2s infinite;
            }
            
            /* 旋转动画 */
            @keyframes spin {
                from { transform: rotate(0deg); }
                to { transform: rotate(360deg); }
            }
            
            .animate-spin {
                animation: spin 1s linear infinite;
            }
            
            /* ===== 移动端体验优化 ===== */
            
            /* 触摸区域优化 - 最小44px点击区域 */
            @media (max-width: 768px) {
                .mobile-menu-item {
                    min-height: 44px;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    padding: 12px 20px;
                    -webkit-tap-highlight-color: transparent;
                }
                
                .hamburger-btn,
                .close-menu-btn {
                    min-width: 44px;
                    min-height: 44px;
                    -webkit-tap-highlight-color: transparent;
                }
                
                /* 移动端卡片点击反馈 */
                .card-glass:active {
                    transform: scale(0.98);
                    transition: transform 0.1s ease;
                }
                
                /* 禁止双击缩放 */
                * {
                    touch-action: manipulation;
                }
                
                /* 底部安全区域适配 */
                .pro-container {
                    padding-bottom: calc(1rem + env(safe-area-inset-bottom, 0px));
                }
                
                /* 移动端滚动条隐藏 */
                ::-webkit-scrollbar {
                    width: 4px;
                    height: 4px;
                }
                
                ::-webkit-scrollbar-track {
                    background: transparent;
                }
                
                ::-webkit-scrollbar-thumb {
                    background: rgba(255, 255, 255, 0.3);
                    border-radius: 2px;
                }
                
                /* 移动端标题截断 */
                .section-title {
                    font-size: 1.1rem !important;
                }
                
                /* 移动端网格优化 - 2列布局 */
                .mobile-grid-2 {
                    grid-template-columns: repeat(2, 1fr) !important;
                }
                
                /* 移动端字体优化 */
                body {
                    font-size: 15px;
                    -webkit-font-smoothing: antialiased;
                    -moz-osx-font-smoothing: grayscale;
                }
            }
            
            /* 小屏手机额外优化 */
            @media (max-width: 480px) {
                .mobile-grid-2 {
                    grid-template-columns: 1fr !important;
                }
                
                /* 更小的内边距 */
                .card-glass {
                    padding: 0.875rem !important;
                }
                
                .section-title {
                    font-size: 1rem !important;
                }
            }
            
            /* ===== 深色模式优化 ===== */
            @media (prefers-color-scheme: dark) {
                .text-white\/60 {
                    color: rgba(255, 255, 255, 0.7) !important;
                }
            }
            
            /* ===== 减少动效模式 ===== */
            @media (prefers-reduced-motion: reduce) {
                *,
                *::before,
                *::after {
                    animation-duration: 0.01ms !important;
                    animation-iteration-count: 1 !important;
                    transition-duration: 0.01ms !important;
                }
            }
        
            /* ===== 悬浮目录导航 ===== */
            .toc-wrapper {
                position: fixed;
                top: 120px;
                width: 220px;
                max-height: calc(100vh - 160px);
                background: rgba(139, 92, 246, 0.15);
                backdrop-filter: blur(20px);
                -webkit-backdrop-filter: blur(20px);
                border: 1px solid rgba(255, 255, 255, 0.15);
                border-radius: 16px;
                box-shadow: 0 10px 40px rgba(102, 126, 234, 0.3);
                z-index: 90;
                overflow: hidden;
                transition: all 0.3s ease;
            }
            
            .toc-right {
                right: 20px;
            }
            
            .toc-left {
                left: 20px;
            }
            
            .toc-header {
                display: flex;
                align-items: center;
                justify-content: space-between;
                padding: 12px 16px;
                cursor: pointer;
                border-bottom: 1px solid rgba(255, 255, 255, 0.1);
                user-select: none;
            }
            
            .toc-title {
                font-size: 0.875rem;
                font-weight: 600;
                color: white;
            }
            
            .toc-header svg {
                color: rgba(255, 255, 255, 0.7);
                transition: transform 0.3s ease;
            }
            
            .toc-wrapper.collapsed .toc-header svg {
                transform: rotate(-90deg);
            }
            
            .toc-content {
                max-height: calc(100vh - 220px);
                overflow-y: auto;
                padding: 8px 0;
                transition: max-height 0.3s ease;
            }
            
            .toc-wrapper.collapsed .toc-content {
                max-height: 0;
                padding: 0;
                overflow: hidden;
            }
            
            .toc-item {
                display: block;
                padding: 8px 16px;
                font-size: 0.8125rem;
                color: rgba(255, 255, 255, 0.7);
                text-decoration: none;
                border-left: 3px solid transparent;
                transition: all 0.2s ease;
                cursor: pointer;
            }
            
            .toc-item:hover {
                color: white;
                background: rgba(255, 255, 255, 0.08);
                border-left-color: rgba(255, 255, 255, 0.3);
            }
            
            .toc-item.active {
                color: white;
                font-weight: 500;
                background: rgba(102, 126, 234, 0.3);
                border-left-color: #667eea;
            }
            
            .toc-item.pl-4 {
                padding-left: 32px;
                font-size: 0.75rem;
            }
            
            /* 滚动条样式 */
            .toc-content::-webkit-scrollbar {
                width: 4px;
            }
            
            .toc-content::-webkit-scrollbar-track {
                background: transparent;
            }
            
            .toc-content::-webkit-scrollbar-thumb {
                background: rgba(255, 255, 255, 0.2);
                border-radius: 2px;
            }
            
            .toc-content::-webkit-scrollbar-thumb:hover {
                background: rgba(255, 255, 255, 0.4);
            }
            
            /* 大屏显示优化 */
            @media (min-width: 1400px) {
                .toc-wrapper {
                    width: 260px;
                }
                .toc-right {
                    right: calc((100vw - 64rem) / 2 - 300px);
                }
                .toc-left {
                    left: calc((100vw - 64rem) / 2 - 300px);
                }
            }
            
                        /* 平板端优化 - 折叠为悬浮按钮 */
            @media (max-width: 1200px) {
                .toc-wrapper {
                    top: auto;
                    bottom: 80px;
                    right: 16px;
                    width: 44px;
                    height: 44px;
                    border-radius: 50%;
                    overflow: hidden;
                    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
                }
                
                .toc-wrapper.expanded {
                    width: 240px;
                    height: auto;
                    max-height: 60vh;
                    border-radius: 16px;
                    top: auto;
                    bottom: 80px;
                }
                
                .toc-wrapper .toc-header {
                    justify-content: center;
                    padding: 12px;
                    border-bottom: none;
                }
                
                .toc-wrapper.expanded .toc-header {
                    justify-content: space-between;
                    padding: 12px 16px;
                    border-bottom: 1px solid rgba(255, 255, 255, 0.1);
                }
                
                .toc-wrapper .toc-title {
                    display: none;
                }
                
                .toc-wrapper.expanded .toc-title {
                    display: block;
                    font-size: 0.875rem;
                }
                
                .toc-wrapper .toc-content {
                    max-height: 0;
                    padding: 0;
                    opacity: 0;
                    transition: all 0.3s ease;
                }
                
                .toc-wrapper.expanded .toc-content {
                    max-height: calc(60vh - 56px);
                    padding: 8px 0;
                    opacity: 1;
                }
                
                .toc-wrapper .toc-header svg {
                    width: 20px;
                    height: 20px;
                }
            }
            
            /* 手机端 - 更小的悬浮按钮 */
            @media (max-width: 480px) {
                .toc-wrapper {
                    width: 40px;
                    height: 40px;
                    bottom: 70px;
                    right: 12px;
                }
                
                .toc-wrapper.expanded {
                    width: 200px;
                }
                
                .toc-wrapper.expanded .toc-title {
                    font-size: 0.8rem;
                }
            }
            
            /* 页面内容区域适配 - 避免被目录遮挡 */
            @media (min-width: 1200px) {
                .pro-container.has-toc {
                    max-width: 48rem;
                }
            }
            
            /* Tab切换组件样式 */
            .tab-container {
                margin-bottom: 1rem;
            }
            
            .tab-buttons {
                display: flex;
                gap: 0.5rem;
                margin-bottom: 1rem;
                border-bottom: 1px solid rgba(255,255,255,0.1);
                padding-bottom: 0.5rem;
            }
            
            .tab-btn {
                padding: 0.5rem 1rem;
                background: rgba(255,255,255,0.05);
                border: 1px solid rgba(255,255,255,0.1);
                border-radius: 8px;
                color: rgba(255,255,255,0.6);
                cursor: pointer;
                font-size: 0.875rem;
                transition: all 0.3s ease;
            }
            
            .tab-btn:hover {
                background: rgba(255,255,255,0.1);
                color: rgba(255,255,255,0.9);
            }
            
            .tab-btn-active {
                background: rgba(139, 92, 246, 0.3);
                border-color: rgba(139, 92, 246, 0.5);
                color: white;
                font-weight: 500;
            }
            
            .tab-container .tab-content .tab-panel {
                display: none;
                animation: fadeIn 0.3s ease;
            }
            
            .tab-container .tab-content .tab-panel.tab-panel-active {
                display: block !important;
            }
            
            @keyframes fadeIn {
                from { opacity: 0; transform: translateY(10px); }
                to { opacity: 1; transform: translateY(0); }
            }
            
            /* Underline风格Tab */
            .tab-style-underline .tab-buttons {
                border-bottom: none;
                padding-bottom: 0;
                gap: 1.5rem;
            }
            
            .tab-style-underline .tab-btn {
                background: transparent;
                border: none;
                border-bottom: 2px solid transparent;
                border-radius: 0;
                padding: 0.5rem 0;
            }
            
            .tab-style-underline .tab-btn:hover {
                background: transparent;
                color: rgba(255,255,255,0.9);
            }
            
            .tab-style-underline .tab-btn-active {
                border-bottom-color: #8b5cf6;
                color: white;
                background: transparent;
            }
            
            /* 次级卡片样式 */
            .card-subtle {
                background: rgba(255,255,255,0.05);
                border: 1px solid rgba(255,255,255,0.1);
                border-radius: 12px;
                padding: 1rem;
                transition: all 0.3s ease;
            }
            
            .card-subtle:hover {
                background: rgba(255,255,255,0.08);
                border-color: rgba(255,255,255,0.2);
            }
</style>
    '''


# ============================================================================
# 组件定义
# ============================================================================

class GlassCard(Component):
    """玻璃态卡片 - Pro风格基础容器
    
    对应原始CSS类: card-glass
    """
    
    def __init__(self, content: str = "", padding: str = "p-6", 
                 extra_class: str = "", hover_effect: bool = False):
        self.content = content
        self.padding = padding
        self.extra_class = extra_class
        self.hover_effect = hover_effect
    
    def render(self) -> str:
        hover_class = "transition-all duration-300 hover:scale-[1.02]" if self.hover_effect else ""
        return f'''
        <div class="card-glass {self.padding} {self.extra_class} {hover_class}">
            {self.content}
        </div>
        '''


class SectionTitle(Component):
    """章节标题
    
    对应原始CSS类: section-title
    支持主标题+副标题，增强视觉层次感
    """
    
    def __init__(self, text: str, icon: str = "", subtitle: str = ""):
        self.text = text
        self.icon = icon
        self.subtitle = subtitle
    
    def render(self) -> str:
        icon_html = f'<span class="text-2xl mr-3">{self.icon}</span>' if self.icon else ''
        
        if self.subtitle:
            return f'''
            <div class="mb-6">
                <h2 class="section-title flex items-center mb-2">
                    {icon_html}{self.text}
                </h2>
                <p class="text-white/50 text-sm ml-11 -mt-1">{self.subtitle}</p>
            </div>
            '''
        return f'<h2 class="section-title">{icon_html}{self.text}</h2>'


class TagBadge(Component):
    """标签徽章
    
    对应原始CSS类: tag-badge
    """
    
    def __init__(self, text: str, color: str = "purple"):
        """
        Args:
            text: 标签文字
            color: 背景色: green, red, yellow, blue, purple
        """
        self.text = text
        self.color = color
    
    def render(self) -> str:
        color_map = {
            'green': 'bg-green-500/20 text-green-400',
            'red': 'bg-red-500/20 text-red-400',
            'yellow': 'bg-yellow-500/20 text-yellow-400',
            'blue': 'bg-blue-500/20 text-blue-400',
            'purple': 'bg-purple-500/30 text-purple-300',
        }
        color_class = color_map.get(self.color, color_map['purple'])
        return f'<span class="tag-badge {color_class}">{self.text}</span>'




class FloatingButtons(Component):
    """悬浮按钮组 - 阅读进度条、回到顶部、操作按钮"""
    
    def __init__(self, show_print=True, show_share=True, show_back_to_top=True):
        self.show_print = show_print
        self.show_share = show_share
        self.show_back_to_top = show_back_to_top
    
    def render(self):
        progress_bar = '<div id="progressBar"></div>'
        
        action_buttons = ''
        if self.show_print or self.show_share:
            buttons_html = ''
            if self.show_print:
                buttons_html += '<button onclick="exportPDF()" class="action-btn" title="打印/导出PDF"><span style="font-size:20px">&#x1F4C4;</span></button>'
            if self.show_share:
                buttons_html += '<button onclick="shareReport()" class="action-btn" title="分享报告"><span style="font-size:20px">&#x1F517;</span></button>'
            action_buttons = '<div class="action-buttons">' + buttons_html + '</div>'
        
        back_to_top = ''
        if self.show_back_to_top:
            back_to_top = '<button id="backToTop" onclick="scrollToTop()" title="回到顶部"><svg width="24" height="24" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 10l7-7m0 0l7 7m-7-7v18"></path></svg></button>'
        
        return progress_bar + action_buttons + back_to_top



class TableOfContents(Component):
    """悬浮目录导航 - 页面内锚点跳转+滚动高亮
    
    支持自动提取标题或手动传入目录项
    """
    
    def __init__(self, items: list = None, title: str = "目录", 
                 position: str = "right", auto_extract: bool = True,
                 max_depth: int = 2):
        """
        Args:
            items: 手动目录项列表，每项为 {"title": "", "id": "", "level": 2}
                   为None时自动提取页面h2/h3标题
            title: 目录标题
            position: 位置: left 或 right
            max_depth: 自动提取时的最大深度（2=h2, 3=h2+h3）
        """
        self.items = items or []
        self.title = title
        self.position = position
        self.auto_extract = auto_extract
        self.max_depth = max_depth
    
    def render(self) -> str:
        position_class = 'toc-right' if self.position == 'right' else 'toc-left'
        
        # 生成目录项HTML
        items_html = ''
        if self.items:
            for item in self.items:
                level = item.get('level', 2)
                indent = 'pl-4' if level == 3 else ''
                item_html = '<a href="#' + item['id'] + '" class="toc-item ' + indent + '" data-level="' + str(level) + '">' + item['title'] + '</a>'
                items_html += item_html + '\n'
        
        # 如果自动提取，添加空容器由JS填充
        if self.auto_extract and not self.items:
            items_html = '<div id="tocContainer" class="toc-container"></div>'
        
        html = '<!-- 悬浮目录导航 -->\n'
        html += '<div id="tableOfContents" class="toc-wrapper ' + position_class + '">\n'
        html += '  <div class="toc-header" onclick="toggleTOC()">\n'
        html += '    <span class="toc-title">' + self.title + '</span>\n'
        html += '    <svg id="tocToggleIcon" width="16" height="16" fill="none" stroke="currentColor" viewBox="0 0 24 24" class="transition-transform duration-300">\n'
        html += '      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path>\n'
        html += '    </svg>\n'
        html += '  </div>\n'
        html += '  <div id="tocContent" class="toc-content">\n'
        html += '    ' + items_html + '\n'
        html += '  </div>\n'
        html += '</div>\n'
        
        return html

class RiskBar(Component):
    """风险进度条
    
    对应原始CSS类: risk-bar, risk-bar-fill
    """
    
    def __init__(self, value: int, max_value: int = 100, 
                 label: str = "", show_labels: bool = False):
        """
        Args:
            value: 当前值
            max_value: 最大值
            label: 标签文字（显示在左侧）
            show_labels: 是否显示底部标签（安全/警戒/危险）
        """
        self.value = value
        self.max_value = max_value
        self.label = label
        self.show_labels = show_labels
    
    def render(self) -> str:
        percentage = (self.value / self.max_value * 100) if self.max_value else 0
        
        label_html = ''
        if self.label:
            label_html = f'<div class="text-sm text-white/70 mb-1">{self.label}</div>'
        
        bottom_labels = ''
        if self.show_labels:
            bottom_labels = '''
            <div class="flex justify-between text-xs text-white/40 mt-1">
                <span>安全</span>
                <span>警戒</span>
                <span>危险</span>
            </div>
            '''
        
        return f'''
        {label_html}
        <div class="risk-bar">
            <div class="risk-bar-fill bg-gradient-to-r from-green-500 via-yellow-500 to-red-500" 
                 style="width: {percentage}%"></div>
        </div>
        {bottom_labels}
        '''


class DiagnosisItem(Component):
    """诊断项 - 用于四维诊断等
    
    对应原始CSS类: diagnosis-item
    """
    
    def __init__(self, icon: str, title: str, status: str = "neutral", desc: str = ""):
        """
        Args:
            icon: emoji图标
            title: 标题（如技术面）
            status: 状态: good, warning, danger, neutral
            desc: 描述文字
        """
        self.icon = icon
        self.title = title
        self.status = status
        self.desc = desc
    
    def render(self) -> str:
        status_colors = {
            'good': 'text-green-400',
            'warning': 'text-yellow-400',
            'danger': 'text-red-400',
            'neutral': 'text-gray-400',
        }
        color = status_colors.get(self.status, 'text-white/70')
        
        return f'''
        <div class="diagnosis-item">
            <div class="text-2xl mb-1">{self.icon}</div>
            <div class="text-sm font-medium {color}">{self.title}</div>
            <div class="text-xs text-white/50 mt-1">{self.desc}</div>
        </div>
        '''


class FundRow(Component):
    """资金流向行
    
    对应原始CSS类: fund-row, fund-trend-up, fund-trend-down
    """
    
    def __init__(self, label: str, value: str, trend: str = "up"):
        """
        Args:
            label: 标签文字
            value: 数值
            trend: 趋势: up 或 down
        """
        self.label = label
        self.value = value
        self.trend = trend
    
    def render(self) -> str:
        trend_class = 'fund-trend-up' if self.trend == 'up' else 'fund-trend-down'
        return f'''
        <div class="fund-row">
            <span class="text-white/70">{self.label}</span>
            <span class="{trend_class}">{self.value}</span>
        </div>
        '''


class LhbCard(Component):
    """龙虎榜卡片
    
    对应原始CSS类: lhb-card, lhb-seat
    """
    
    def __init__(self, seat: str, stock_name: str, reason: str, 
                 net_buy: str = "", net_sell: str = ""):
        self.seat = seat
        self.stock_name = stock_name
        self.reason = reason
        self.net_buy = net_buy
        self.net_sell = net_sell
    
    def render(self) -> str:
        buy_html = f'<div class="text-green-400 text-sm">净买入: {self.net_buy}</div>' if self.net_buy else ''
        sell_html = f'<div class="text-red-400 text-sm">净卖出: {self.net_sell}</div>' if self.net_sell else ''
        
        return f'''
        <div class="lhb-card">
            <div class="lhb-seat">{self.seat}</div>
            <div class="text-white font-medium mb-1">{self.stock_name}</div>
            <div class="text-xs text-white/60 mb-2">{self.reason}</div>
            {buy_html}
            {sell_html}
        </div>
        '''


class AlertSection(Component):
    """警告/提示区域
    
    对应原始CSS类: alert-section, warning-section, safe-section
    """
    
    def __init__(self, title: str, content: str, level: str = "warning"):
        """
        Args:
            title: 标题
            content: 内容HTML
            level: 级别: danger(红), warning(黄), safe(绿)
        """
        self.title = title
        self.content = content
        self.level = level
    
    def render(self) -> str:
        level_class = {
            'danger': 'alert-section',
            'warning': 'warning-section',
            'safe': 'safe-section',
        }.get(self.level, 'warning-section')
        
        title_color = {
            'danger': 'text-red-400',
            'warning': 'text-yellow-400',
            'safe': 'text-green-400',
        }.get(self.level, 'text-yellow-400')
        
        return f'''
        <div class="{level_class}">
            <h3 class="font-semibold {title_color} mb-2">{self.title}</h3>
            <div class="text-white/80 text-sm">
                {self.content}
            </div>
        </div>
        '''


def get_pro_components_css() -> str:
    """获取所有Pro组件的完整CSS（对外统一入口）"""
    return get_pro_theme_css()



class NavBar(Component):
    """导航栏组件 - 包含桌面导航和移动端汉堡菜单"""
    
    def __init__(self, active_page: str = ""):
        self.active_page = active_page
    
    def render(self) -> str:
        # 从核心配置导入导航项，保持全站统一
        from core.config import NAV_ITEMS
        nav_items = [(item['label'], item['path']) for item in NAV_ITEMS]
        
        nav_links = ''
        for name, url in nav_items:
            is_active = self.active_page == name
            active_class = 'text-white bg-white/20' if is_active else 'text-white/80 hover:text-white hover:bg-white/10'
            nav_links += f'<a href="{url}" class="{active_class} text-sm transition-colors px-3 py-1.5 rounded-lg">{name}</a>'
        
        # 移动端菜单项（从配置生成，与桌面导航一致）
        mobile_icons = {
            '首页': '🏠', '日报': '📰', '盘中': '📈', '盘后': '📉',
            '产业链': '🔗', '周复盘': '📋', '周三前瞻': '🔮',
            '周末速递': '📦', '明日催化': '⏰', 'S级催化': '⚡', '月报': '📅',
        }
        mobile_items = []
        for item in NAV_ITEMS:
            icon = mobile_icons.get(item['label'], '📄')
            mobile_items.append((f'{icon} {item["label"]}', item['path']))
        
        mobile_links = ''
        for name, url in mobile_items:
            mobile_links += f'<a href="{url}" class="mobile-menu-item" onclick="toggleMobileMenu()">{name}</a>'
        
        return f'''
    <nav class="fixed top-0 left-0 right-0 z-50 glass-nav">
        <div class="max-w-5xl mx-auto px-4 py-3 flex items-center justify-between">
            <div class="flex items-center space-x-3">
                <div class="w-8 h-8 rounded-lg bg-gradient-to-br from-indigo-500 to-purple-600 flex items-center justify-center">
                    <span class="text-white text-sm font-bold">📊</span>
                </div>
                <span class="text-white font-bold text-lg">投资研究中心</span>
            </div>
            <div class="nav-links flex items-center space-x-1 flex-wrap gap-1">
                {nav_links}
            </div>
            <button class="hamburger-btn" onclick="toggleMobileMenu()">☰</button>
        </div>
    </nav>
    
    <!-- 移动端全屏菜单 -->
    <div id="mobileMenu" class="mobile-menu">
        <button class="close-menu-btn" onclick="toggleMobileMenu()">✕</button>
        {mobile_links}
    </div>
        '''


class Footer(Component):
    """页脚组件"""
    
    def __init__(self, text: str = "", update_time: str = ""):
        self.text = text
        self.update_time = update_time
    
    def render(self) -> str:
        time_html = f'<p class="text-xs mt-2">数据更新时间：{self.update_time}</p>' if self.update_time else ''
        text_html = f'<p>{self.text}</p>' if self.text else '<p>投资研究中心 · 专业投资决策辅助</p>'
        
        return f'''
        <div class="text-center text-white/40 text-sm py-10">
            {text_html}
            {time_html}
        </div>
        '''


class PageScript(Component):
    """页面JavaScript脚本 - 包含菜单切换、滚动效果和交互动效"""
    
    def render(self) -> str:
        return '''
    <script>
        // ==================== 移动端菜单切换 ====================
        function toggleMobileMenu() {
            const menu = document.getElementById('mobileMenu');
            if (menu) {
                menu.classList.toggle('show');
                document.body.style.overflow = menu.classList.contains('show') ? 'hidden' : '';
            }
        }
        
        // 点击菜单项后关闭菜单
        document.addEventListener('click', function(e) {
            if (e.target.classList.contains('mobile-menu-item')) {
                setTimeout(toggleMobileMenu, 100);
            }
        });
        
        // ==================== 导航栏滚动效果 ====================
        window.addEventListener('scroll', function() {
            const nav = document.querySelector('.glass-nav');
            if (nav) {
                if (window.scrollY > 10) {
                    nav.classList.add('scrolled');
                } else {
                    nav.classList.remove('scrolled');
                }
            }
        });
        
        // ==================== 滚动触发动画 ====================
        function initScrollReveal() {
            if ('IntersectionObserver' in window) {
                const observer = new IntersectionObserver(function(entries) {
                    entries.forEach(function(entry) {
                        if (entry.isIntersecting) {
                            entry.target.classList.add('visible');
                        }
                    });
                }, {
                    threshold: 0.1,
                    rootMargin: '0px 0px -50px 0px'
                });
                
                document.querySelectorAll('.reveal, .card-glass').forEach(function(el, index) {
                    observer.observe(el);
                    el.style.animationDelay = (index * 0.1) + 's';
                });
            }
        }
        
        // ==================== 数字滚动动画 ====================
        function animateValue(element, start, end, duration) {
            var startTimestamp = null;
            var step = function(timestamp) {
                if (!startTimestamp) startTimestamp = timestamp;
                var progress = Math.min((timestamp - startTimestamp) / duration, 1);
                var value = Math.floor(progress * (end - start) + start);
                element.textContent = value.toLocaleString();
                if (progress < 1) {
                    window.requestAnimationFrame(step);
                }
            };
            window.requestAnimationFrame(step);
        }
        
        function initCounters() {
            var counters = document.querySelectorAll('.counter-value');
            if ('IntersectionObserver' in window) {
                var observer = new IntersectionObserver(function(entries) {
                    entries.forEach(function(entry) {
                        if (entry.isIntersecting && !entry.target.dataset.animated) {
                            entry.target.dataset.animated = 'true';
                            var target = parseInt(entry.target.dataset.target || entry.target.textContent);
                            animateValue(entry.target, 0, target, 1500);
                        }
                    });
                }, { threshold: 0.5 });
                
                counters.forEach(function(counter) { observer.observe(counter); });
            }
        }
        
        // ==================== 进度条动画 ====================
        function initProgressBars() {
            var bars = document.querySelectorAll('.risk-bar-fill');
            if ('IntersectionObserver' in window) {
                var observer = new IntersectionObserver(function(entries) {
                    entries.forEach(function(entry) {
                        if (entry.isIntersecting && !entry.target.dataset.animated) {
                            entry.target.dataset.animated = 'true';
                            var width = entry.target.style.width;
                            entry.target.style.width = '0%';
                            setTimeout(function() {
                                entry.target.style.width = width;
                            }, 100);
                        }
                    });
                }, { threshold: 0.5 });
                
                bars.forEach(function(bar) { observer.observe(bar); });
            }
        }
        
        // ==================== 卡片入场动画 ====================
        function initCardAnimations() {
            var cards = document.querySelectorAll('.card-glass');
            cards.forEach(function(card, index) {
                card.style.opacity = '0';
                card.style.transform = 'translateY(20px)';
                card.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
                
                setTimeout(function() {
                    card.style.opacity = '1';
                    card.style.transform = 'translateY(0)';
                }, 100 + index * 100);
            });
        }
        

        // ==================== 阅读进度条 & 回到顶部 ====================
        function initProgressAndBackToTop() {
            const progressBar = document.getElementById('progressBar');
            const backToTop = document.getElementById('backToTop');
            
            function updateProgress() {
                const winScroll = document.body.scrollTop || document.documentElement.scrollTop;
                const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
                const scrolled = height > 0 ? (winScroll / height) * 100 : 0;
                
                if (progressBar) {
                    progressBar.style.width = scrolled + '%';
                }
                
                if (backToTop) {
                    if (winScroll > 300) {
                        backToTop.classList.add('visible');
                    } else {
                        backToTop.classList.remove('visible');
                    }
                }
            }
            
            window.addEventListener('scroll', updateProgress);
            updateProgress();
        }
        
        function scrollToTop() {
            window.scrollTo({ top: 0, behavior: 'smooth' });
        }
        
        function exportPDF() {
            window.print();
        }
        
        function shareReport() {
            const url = window.location.href;
            if (navigator.share) {
                navigator.share({ title: document.title, url: url });
            } else {
                navigator.clipboard.writeText(url).then(function() {
                    alert('链接已复制到剪贴板！');
                }).catch(function() {
                    prompt('复制以下链接分享：', url);
                });
            }
        }
        
        // ==================== 平滑滚动 ====================
        function initSmoothScroll() {
            document.querySelectorAll('a[href^="#"]').forEach(function(anchor) {
                anchor.addEventListener('click', function(e) {
                    e.preventDefault();
                    var target = document.querySelector(this.getAttribute('href'));
                    if (target) {
                        target.scrollIntoView({
                            behavior: 'smooth',
                            block: 'start'
                        });
                    }
                });
            });
        }
        
        
        // ==================== 悬浮目录导航 ====================
        function toggleTOC() {
            const toc = document.getElementById('tableOfContents');
            if (toc) {
                // 移动端使用expanded类，桌面端使用collapsed类
                if (window.innerWidth <= 1200) {
                    toc.classList.toggle('expanded');
                } else {
                    toc.classList.toggle('collapsed');
                }
            }
        }

        // 监听窗口大小变化，重置TOC状态
        window.addEventListener('resize', function() {
            const toc = document.getElementById('tableOfContents');
            if (toc) {
                if (window.innerWidth > 1200) {
                    toc.classList.remove('expanded');
                } else {
                    toc.classList.remove('expanded');
                }
            }
        });
        
        function initTableOfContents() {
            const tocContainer = document.getElementById('tocContainer');
            if (!tocContainer) return;
            
            // 自动提取页面中的h2和h3标题
            const headings = document.querySelectorAll('.pro-container h2, .pro-container h3');
            if (headings.length === 0) {
                // 没有标题则隐藏目录
                const toc = document.getElementById('tableOfContents');
                if (toc) toc.style.display = 'none';
                return;
            }
            
            // 为标题生成id（如果没有的话）
            headings.forEach(function(heading, index) {
                if (!heading.id) {
                    const text = heading.textContent || heading.innerText;
                    heading.id = 'section-' + index + '-' + text.trim().replace(/\s+/g, '-').replace(/[^\w\-\u4e00-\u9fa5]/g, '').substring(0, 30);
                }
            });
            
            // 生成目录HTML
            var tocHTML = '';
            headings.forEach(function(heading) {
                const level = parseInt(heading.tagName.substring(1));
                const title = heading.textContent || heading.innerText;
                const indent = level === 3 ? 'pl-4' : '';
                tocHTML += '<a href="#' + heading.id + '" class="toc-item ' + indent + '" data-level="' + level + '">' + title.trim() + '</a>';
            });
            
            tocContainer.innerHTML = tocHTML;
            
            // 为目录项添加平滑滚动
            tocContainer.querySelectorAll('.toc-item').forEach(function(item) {
                item.addEventListener('click', function(e) {
                    e.preventDefault();
                    var target = document.querySelector(this.getAttribute('href'));
                    if (target) {
                        // 考虑导航栏高度
                        var offset = 100;
                        var targetPosition = target.getBoundingClientRect().top + window.pageYOffset - offset;
                        window.scrollTo({
                            top: targetPosition,
                            behavior: 'smooth'
                        });
                    }
                });
            });
            
            // 初始化滚动高亮
            initTOCScrollSpy();
        }
        
        function initTOCScrollSpy() {
            const tocItems = document.querySelectorAll('.toc-item');
            if (tocItems.length === 0) return;
            
            // 获取所有章节
            const sections = [];
            tocItems.forEach(function(item) {
                const id = item.getAttribute('href').substring(1);
                const section = document.getElementById(id);
                if (section) {
                    sections.push({
                        element: section,
                        navItem: item,
                        top: section.offsetTop - 120
                    });
                }
            });
            
            if (sections.length === 0) return;
            
            // 滚动时更新高亮
            function updateActiveTOC() {
                const scrollPosition = window.pageYOffset;
                
                // 找到当前处于视口的章节
                var currentIndex = 0;
                for (var i = 0; i < sections.length; i++) {
                    if (scrollPosition >= sections[i].top) {
                        currentIndex = i;
                    }
                }
                
                // 更新高亮状态
                tocItems.forEach(function(item, index) {
                    item.classList.remove('active');
                });
                if (sections[currentIndex]) {
                    sections[currentIndex].navItem.classList.add('active');
                }
            }
            
            window.addEventListener('scroll', updateActiveTOC);
            updateActiveTOC();
        }
// ==================== 页面加载完成后初始化 ====================
        function initAllAnimations() {
            initProgressAndBackToTop();
            initScrollReveal();
            initCounters();
            initProgressBars();
            initCardAnimations();
            initSmoothScroll();
            initTableOfContents();

        }
        
        document.addEventListener('DOMContentLoaded', function() {
            setTimeout(initAllAnimations, 100);
        });
        
        if (document.readyState !== 'loading') {
            setTimeout(initAllAnimations, 100);
        }
    </script>
        '''


class TabPane(Component):
    """Tab切换组件 - Pro版深色玻璃态风格"""
    
    def __init__(self, tabs: list, tab_id: str = "tab", style: str = "default"):
        """
        Args:
            tabs: Tab列表，每项含 label(标签) 和 content(内容HTML)
            tab_id: Tab组件唯一ID
            style: Tab样式: default / underline
        """
        super().__init__()
        self.tabs = tabs
        self.tab_id = tab_id
        self.style = style
    
    def render(self) -> str:
        tabs_html = ''
        panels_html = ''
        
        for i, tab in enumerate(self.tabs):
            label = tab.get('label', f'Tab {i+1}')
            content = tab.get('content', '')
            active_class = 'tab-btn-active' if i == 0 else ''
            active_panel_class = 'tab-panel-active' if i == 0 else ''
            
            tabs_html += f'''
                <button class="tab-btn {active_class}" 
                        onclick="switchTab('{self.tab_id}', {i})"
                        data-tab-index="{i}">
                    {label}
                </button>
            '''
            
            # 给激活的面板添加内联样式，确保显示
            inline_style = ' style="display: block !important;"' if active_panel_class else ''
            panels_html += f'''
                <div class="tab-panel {active_panel_class}" 
                     id="{self.tab_id}-panel-{i}"
                     data-tab-index="{i}"{inline_style}>
                    {content}
                </div>
            '''
        
        style_class = f'tab-style-{self.style}'
        
        return f'''
        <div class="tab-container {style_class}" id="{self.tab_id}-container">
            <div class="tab-buttons">
                {tabs_html}
            </div>
            <div class="tab-content">
                {panels_html}
            </div>
        </div>
        <script>
        function switchTab(tabId, index) {{
            const container = document.getElementById(tabId + '-container');
            if (!container) return;
            
            // 更新按钮状态
            container.querySelectorAll('.tab-btn').forEach((btn, i) => {{
                if (i === index) {{
                    btn.classList.add('tab-btn-active');
                }} else {{
                    btn.classList.remove('tab-btn-active');
                }}
            }});
            
            // 更新面板显示（双保险：类名 + 内联样式）
            container.querySelectorAll('.tab-panel').forEach((panel, i) => {{
                if (i === index) {{
                    panel.classList.add('tab-panel-active');
                    panel.style.display = 'block';
                }} else {{
                    panel.classList.remove('tab-panel-active');
                    panel.style.display = 'none';
                }}
            }});
        }}
        </script>
        '''


class CardGroup(Component):
    """卡片组组件 - 卡片套卡片布局，Pro版深色玻璃态风格"""
    
    def __init__(self, cards: list, cols: int = 2, card_style: str = "glass"):
        """
        Args:
            cards: 卡片列表，每项含 title(可选)、content(内容HTML)、icon(可选)
            cols: 列数: 1, 2, 3, 4
            card_style: 卡片样式: glass / subtle
        """
        super().__init__()
        self.cards = cards
        self.cols = cols
        self.card_style = card_style
    
    def render(self) -> str:
        col_class = {
            1: 'grid-cols-1',
            2: 'grid-cols-1 md:grid-cols-2',
            3: 'grid-cols-1 md:grid-cols-3',
            4: 'grid-cols-2 md:grid-cols-4',
        }.get(self.cols, 'grid-cols-2')
        
        style_class = f'card-{self.card_style}'
        
        cards_html = ''
        for card in self.cards:
            if isinstance(card, dict):
                title = card.get('title', '')
                content = card.get('content', '')
                icon = card.get('icon', '')
                
                title_html = f'<div class="text-sm font-medium text-white/90 mb-2 flex items-center gap-2">{icon} {title}</div>' if title else ''
                body_html = f'<div class="text-sm text-white/70 leading-relaxed">{content}</div>'
                
                card_content = f'''
                    <div class="{style_class} rounded-xl p-4 h-full">
                        {title_html}
                        {body_html}
                    </div>
                '''
                cards_html += card_content
            else:
                cards_html += str(card)
        
        return f'''
        <div class="grid {col_class} gap-4">
            {cards_html}
        </div>
        '''


class DataGrid(Component):
    """数据网格组件 - 多数据卡片网格布局，Pro版深色玻璃态风格"""
    
    def __init__(self, items: list, cols: int = 2):
        """
        Args:
            items: 数据项列表，每项为字典（含title、value、icon、unit等）或HTML字符串
            cols: 列数: 1, 2, 3, 4, 6
        """
        super().__init__()
        self.items = items
        self.cols = cols
    
    def render(self) -> str:
        col_class = {
            1: 'grid-cols-1',
            2: 'grid-cols-1 md:grid-cols-2',
            3: 'grid-cols-1 md:grid-cols-3',
            4: 'grid-cols-2 md:grid-cols-4',
            6: 'grid-cols-2 md:grid-cols-3 lg:grid-cols-6',
        }.get(self.cols, 'grid-cols-2')
        
        items_html = ''
        for item in self.items:
            if isinstance(item, dict):
                title = item.get('title', '')
                value = item.get('value', '')
                icon = item.get('icon', '')
                unit = item.get('unit', '')
                desc = item.get('desc', '')
                
                icon_html = f'<span class="text-2xl mb-2">{icon}</span>' if icon else ''
                title_html = f'<div class="text-xs text-white/50 mb-1">{title}</div>' if title else ''
                value_html = f'<div class="text-xl font-bold text-white">{value}{unit}</div>' if value else ''
                desc_html = f'<div class="text-xs text-white/40 mt-1">{desc}</div>' if desc else ''
                
                card_content = f'''
                    <div class="flex flex-col items-center text-center">
                        {icon_html}
                        {title_html}
                        {value_html}
                        {desc_html}
                    </div>
                '''
                items_html += f'<div class="card-glass p-4">{card_content}</div>'
            else:
                # 字符串或HTML直接使用
                items_html += f'<div class="card-glass p-4">{item}</div>'
        
        return f'''
        <div class="grid {col_class} gap-4">
            {items_html}
        </div>
        '''


class ProPage:
    """Pro页面基类 - 快速构建标准Pro页面
    
    使用方法:
    1. 继承ProPage
    2. 实现_content()方法，返回页面主要内容HTML
    3. 调用render()生成完整页面
    
    示例:
        class MyPage(ProPage):
            def __init__(self):
                super().__init__(title="我的页面", active_page="首页")
            
            def _content(self):
                return "<p>页面内容</p>"
    """
    
    def __init__(self, title: str = "投资研究中心", active_page: str = "", 
                 footer_text: str = "", update_time: str = "",
                 show_toc: bool = False, toc_items: list = None,
                 toc_position: str = "right", theme: str = "dark"):
        self.title = title
        self.active_page = active_page
        self.footer_text = footer_text
        self.update_time = update_time
        self.show_toc = show_toc
        self.toc_items = toc_items
        self.toc_position = toc_position
        self.theme = theme  # 'dark'=V3.5深色玻璃态, 'light'=V4白底深字
    
    def _content(self) -> str:
        """页面主要内容 - 子类重写此方法"""
        return ""
    
    def render(self) -> str:
        """渲染完整HTML页面"""
        # 根据主题选择CSS
        if self.theme == 'light':
            theme_css = get_v4_theme_css()
        else:
            theme_css = get_pro_theme_css()
        nav = NavBar(active_page=self.active_page).render()
        footer = Footer(text=self.footer_text, update_time=self.update_time).render()
        script = PageScript().render()
        floating = FloatingButtons().render()
        content = self._content()
        
        # 渲染目录（如果启用）
        toc_html = ""
        if self.show_toc:
            toc = TableOfContents(items=self.toc_items, position=self.toc_position)
            toc_html = toc.render()
        
        return f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{self.title} - 投资研究中心</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
    <link rel="stylesheet" href="/daily-news-insight/assets/global-dark.css">
    <link rel="stylesheet" href="/daily-news-insight/assets/stock-popup.css">
    {theme_css}
    <style>
        .line-clamp-2 {{
            display: -webkit-box;
            -webkit-line-clamp: 2;
            -webkit-box-orient: vertical;
            overflow: hidden;
        }}
    </style>
</head>
<body>
    {nav}
    
    <div class="pro-container pt-20 {"has-toc" if self.show_toc and self.toc_position == "right" else ""}">
        {content}
        
        {footer}
    </div>
    
    {floating}
    {toc_html}
    <script src="/daily-news-insight/assets/stock-popup.js"></script>
    {script}
</body>
</html>
'''
    
    def save(self, filepath: str) -> str:
        """保存到文件"""
        import os
        html = self.render()
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
        return filepath


# ============================================================
# Pro版图表组件 - 深色玻璃态主题
# 基于Chart.js，适配深色背景
# ============================================================

_pro_chart_counter = 0

def get_pro_chart_cdn() -> str:
    """获取Chart.js CDN引用"""
    return '<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>'


class ProBaseChart:
    """Pro版图表基类 - 深色主题"""
    
    def __init__(self, title: str = "", height: int = 280):
        self.title = title
        self.height = height
        global _pro_chart_counter
        _pro_chart_counter += 1
        self.chart_id = f"pro_chart_{_pro_chart_counter}"
    
    def _get_base_options(self) -> dict:
        return {
            "responsive": True,
            "maintainAspectRatio": False,
            "plugins": {
                "legend": {
                    "display": True,
                    "position": "bottom",
                    "labels": {
                        "usePointStyle": True,
                        "padding": 16,
                        "font": {"size": 11, "family": "'Noto Sans SC', sans-serif"},
                        "color": "rgba(255, 255, 255, 0.7)"
                    }
                },
                "title": {
                    "display": bool(self.title),
                    "text": self.title or "",
                    "font": {"size": 14, "weight": "600", "family": "'Noto Sans SC', sans-serif"},
                    "padding": {"bottom": 16},
                    "color": "rgba(255, 255, 255, 0.9)"
                },
                "tooltip": {
                    "backgroundColor": "rgba(0, 0, 0, 0.85)",
                    "titleFont": {"size": 12, "weight": "600"},
                    "bodyFont": {"size": 11},
                    "padding": 10,
                    "cornerRadius": 8,
                    "borderColor": "rgba(255, 255, 255, 0.1)",
                    "borderWidth": 1
                }
            }
        }


class ProLineChart(ProBaseChart):
    """Pro版折线图"""
    
    def __init__(self, labels: list, datasets: list, title: str = "", height: int = 280, smooth: bool = True):
        super().__init__(title, height)
        self.labels = labels
        self.datasets = datasets
        self.smooth = smooth
    
    def render(self) -> str:
        import json
        
        default_colors = [
            {'bg': 'rgba(102, 126, 234, 0.3)', 'border': '#667eea'},
            {'bg': 'rgba(240, 147, 251, 0.3)', 'border': '#f093fb'},
            {'bg': 'rgba(16, 185, 129, 0.3)', 'border': '#10b981'},
        ]
        
        chart_datasets = []
        for i, ds in enumerate(self.datasets):
            color = ds.get('color', {})
            default = default_colors[i % len(default_colors)]
            chart_datasets.append({
                'label': ds.get('label', ''),
                'data': ds.get('data', []),
                'borderColor': color.get('border', default['border']),
                'backgroundColor': color.get('bg', default['bg']),
                'borderWidth': 2,
                'fill': True,
                'tension': 0.4 if self.smooth else 0,
                'pointRadius': 4,
                'pointBackgroundColor': color.get('border', default['border']),
                'pointBorderColor': '#fff',
                'pointBorderWidth': 2,
            })
        
        options = self._get_base_options()
        options['scales'] = {
            'x': {
                'grid': {'color': 'rgba(255,255,255,0.05)', 'drawBorder': False},
                'ticks': {'color': 'rgba(255,255,255,0.5)', 'font': {'size': 10}}
            },
            'y': {
                'beginAtZero': False,
                'grid': {'color': 'rgba(255,255,255,0.05)', 'drawBorder': False},
                'ticks': {'color': 'rgba(255,255,255,0.5)', 'font': {'size': 10}}
            }
        }
        
        config = {'type': 'line', 'data': {'labels': self.labels, 'datasets': chart_datasets}, 'options': options}
        
        return f'''
        <div style="height: {self.height}px; width: 100%;">
            <canvas id="{self.chart_id}"></canvas>
        </div>
        <script>
        (function() {{
            const ctx = document.getElementById('{self.chart_id}').getContext('2d');
            new Chart(ctx, {json.dumps(config, ensure_ascii=False)});
        }})();
        </script>
        '''


class ProPieChart(ProBaseChart):
    """Pro版饼图/环形图"""
    
    def __init__(self, labels: list, data: list, title: str = "", height: int = 280, donut: bool = True):
        super().__init__(title, height)
        self.labels = labels
        self.data = data
        self.donut = donut
    
    def render(self) -> str:
        import json
        
        colors = ['#667eea', '#f093fb', '#10b981', '#f59e0b', '#ef4444', '#3b82f6', '#8b5cf6', '#ec4899']
        bg_colors = [colors[i % len(colors)] for i in range(len(self.data))]
        
        options = self._get_base_options()
        options['cutout'] = '60%' if self.donut else '0%'
        
        config = {
            'type': 'doughnut' if self.donut else 'pie',
            'data': {
                'labels': self.labels,
                'datasets': [{'data': self.data, 'backgroundColor': bg_colors, 'borderColor': 'rgba(0,0,0,0.3)', 'borderWidth': 2, 'borderRadius': 4}]
            },
            'options': options
        }
        
        return f'''
        <div style="height: {self.height}px; width: 100%;">
            <canvas id="{self.chart_id}"></canvas>
        </div>
        <script>
        (function() {{
            const ctx = document.getElementById('{self.chart_id}').getContext('2d');
            new Chart(ctx, {json.dumps(config, ensure_ascii=False)});
        }})();
        </script>
        '''


class ProBarChart(ProBaseChart):
    """Pro版柱状图"""
    
    def __init__(self, labels: list, datasets: list, title: str = "", height: int = 280, horizontal: bool = False):
        super().__init__(title, height)
        self.labels = labels
        self.datasets = datasets
        self.horizontal = horizontal
    
    def render(self) -> str:
        import json
        
        default_colors = [
            {'bg': 'rgba(102, 126, 234, 0.8)', 'border': '#667eea'},
            {'bg': 'rgba(240, 147, 251, 0.8)', 'border': '#f093fb'},
            {'bg': 'rgba(16, 185, 129, 0.8)', 'border': '#10b981'},
        ]
        
        chart_datasets = []
        for i, ds in enumerate(self.datasets):
            color = ds.get('color', {})
            default = default_colors[i % len(default_colors)]
            chart_datasets.append({
                'label': ds.get('label', ''),
                'data': ds.get('data', []),
                'backgroundColor': color.get('bg', default['bg']),
                'borderColor': color.get('border', default['border']),
                'borderWidth': 1,
                'borderRadius': 4,
            })
        
        options = self._get_base_options()
        options['indexAxis'] = 'y' if self.horizontal else 'x'
        options['scales'] = {
            'x': {
                'grid': {'color': 'rgba(255,255,255,0.05)', 'drawBorder': False},
                'ticks': {'color': 'rgba(255,255,255,0.5)', 'font': {'size': 10}}
            },
            'y': {
                'beginAtZero': True,
                'grid': {'color': 'rgba(255,255,255,0.05)', 'drawBorder': False},
                'ticks': {'color': 'rgba(255,255,255,0.5)', 'font': {'size': 10}}
            }
        }
        
        config = {'type': 'bar', 'data': {'labels': self.labels, 'datasets': chart_datasets}, 'options': options}
        
        return f'''
        <div style="height: {self.height}px; width: 100%;">
            <canvas id="{self.chart_id}"></canvas>
        </div>
        <script>
        (function() {{
            const ctx = document.getElementById('{self.chart_id}').getContext('2d');
            new Chart(ctx, {json.dumps(config, ensure_ascii=False)});
        }})();
        </script>
        '''


# ============================================================
# Boya Strategy Components - boya投资体系专属UI组件
# ============================================================

class BoyaPerspectiveBox(Component):
    """boya视角批注框 - 沉浸式融入每个章节"""
    
    def __init__(self, perspective: str, avatar: str = "🎯"):
        self.perspective = perspective
        self.avatar = avatar
    
    def render(self) -> str:
        return f'''
        <div class="boya-perspective-box">
            <div class="boya-perspective-header">
                <span class="boya-avatar">{self.avatar}</span>
                <span class="boya-perspective-label">boya视角</span>
            </div>
            <div class="boya-perspective-content">
                {self.perspective}
            </div>
        </div>
        <style>
            .boya-perspective-box {{
                background: linear-gradient(135deg, rgba(251, 146, 60, 0.15) 0%, rgba(236, 72, 153, 0.15) 100%);
                border-left: 3px solid #fb923c;
                border-radius: 12px;
                padding: 16px 20px;
                margin: 16px 0;
                backdrop-filter: blur(10px);
                border: 1px solid rgba(251, 146, 60, 0.3);
            }}
            .boya-perspective-header {{
                display: flex;
                align-items: center;
                gap: 10px;
                margin-bottom: 8px;
            }}
            .boya-avatar {{
                font-size: 20px;
            }}
            .boya-perspective-label {{
                color: #fb923c;
                font-weight: 600;
                font-size: 14px;
            }}
            .boya-perspective-content {{
                color: rgba(255, 255, 255, 0.9);
                font-size: 14px;
                line-height: 1.7;
                padding-left: 30px;
            }}
        </style>
        '''


class BoyaThemeRatingCard(Component):
    """主线评级卡片"""
    
    def __init__(self, level: str, score: float, dimensions: Dict[str, float], summary: str):
        self.level = level
        self.score = score
        self.dimensions = dimensions
        self.summary = summary
    
    def _get_level_color(self) -> str:
        colors = {
            'S': '#fbbf24',  # 金色
            'A': '#f87171',  # 红色
            'B': '#60a5fa',  # 蓝色
            'C': '#34d399',  # 绿色
            'D': '#9ca3af',  # 灰色
        }
        return colors.get(self.level, '#9ca3af')
    
    def render(self) -> str:
        color = self._get_level_color()
        
        # 维度条
        dim_bars = ''
        dim_names = {
            'catalyst_density': '催化密度',
            'capital_focus': '资金关注度',
            'performance_realization': '业绩兑现度',
            'policy_friendliness': '政策友好度',
            'story_telling': '故事想象空间',
        }
        for dim_key, dim_score in self.dimensions.items():
            dim_name = dim_names.get(dim_key, dim_key)
            dim_bars += f'''
            <div class="dim-item">
                <div class="dim-label">{dim_name}</div>
                <div class="dim-bar-bg">
                    <div class="dim-bar-fill" style="width: {dim_score}%; background: {color};"></div>
                </div>
                <div class="dim-score">{dim_score:.0f}</div>
            </div>
            '''
        
        return f'''
        <div class="boya-rating-card">
            <div class="rating-header">
                <div class="rating-badge" style="background: {color};">
                    <span class="rating-level">{self.level}</span>
                    <span class="rating-label">级主线</span>
                </div>
                <div class="rating-score-box">
                    <span class="rating-score">{self.score}</span>
                    <span class="rating-score-label">综合评分</span>
                </div>
            </div>
            <div class="rating-summary">{self.summary}</div>
            <div class="rating-dimensions">
                {dim_bars}
            </div>
        </div>
        <style>
            .boya-rating-card {{
                background: rgba(255, 255, 255, 0.05);
                border: 1px solid rgba(255, 255, 255, 0.1);
                border-radius: 16px;
                padding: 24px;
                color: white;
            }}
            .rating-header {{
                display: flex;
                justify-content: space-between;
                align-items: center;
                margin-bottom: 16px;
            }}
            .rating-badge {{
                display: flex;
                align-items: baseline;
                gap: 6px;
                padding: 8px 20px;
                border-radius: 30px;
            }}
            .rating-level {{
                font-size: 32px;
                font-weight: 900;
                color: white;
                line-height: 1;
            }}
            .rating-label {{
                font-size: 14px;
                color: rgba(255, 255, 255, 0.9);
                font-weight: 500;
            }}
            .rating-score-box {{
                text-align: right;
            }}
            .rating-score {{
                font-size: 36px;
                font-weight: 700;
                color: white;
                line-height: 1;
            }}
            .rating-score-label {{
                font-size: 12px;
                color: rgba(255, 255, 255, 0.6);
            }}
            .rating-summary {{
                color: rgba(255, 255, 255, 0.85);
                font-size: 14px;
                line-height: 1.6;
                margin-bottom: 20px;
                padding-bottom: 16px;
                border-bottom: 1px solid rgba(255, 255, 255, 0.1);
            }}
            .rating-dimensions {{
                display: flex;
                flex-direction: column;
                gap: 12px;
            }}
            .dim-item {{
                display: flex;
                align-items: center;
                gap: 12px;
            }}
            .dim-label {{
                width: 100px;
                font-size: 13px;
                color: rgba(255, 255, 255, 0.7);
                flex-shrink: 0;
            }}
            .dim-bar-bg {{
                flex: 1;
                height: 8px;
                background: rgba(255, 255, 255, 0.1);
                border-radius: 4px;
                overflow: hidden;
            }}
            .dim-bar-fill {{
                height: 100%;
                border-radius: 4px;
                transition: width 0.5s ease;
            }}
            .dim-score {{
                width: 30px;
                text-align: right;
                font-size: 13px;
                color: rgba(255, 255, 255, 0.8);
                font-weight: 600;
                flex-shrink: 0;
            }}
        </style>
        '''


class BoyaDragonTroupeCard(Component):
    """龙头梯队卡片"""
    
    def __init__(self, dragon_one: Dict, dragon_two: Dict, dragon_three: Dict, rationale: str):
        self.dragon_one = dragon_one
        self.dragon_two = dragon_two
        self.dragon_three = dragon_three
        self.rationale = rationale
    
    def _render_dragon_slot(self, dragon: Dict, rank: int) -> str:
        if not dragon or not dragon.get('name'):
            return ''
        
        rank_colors = {1: '#fbbf24', 2: '#d1d5db', 3: '#cd7f32'}
        rank_labels = {1: '龙一', 2: '龙二', 3: '龙三'}
        color = rank_colors.get(rank, '#9ca3af')
        label = rank_labels.get(rank, f'龙{rank}')
        
        name = dragon.get('name', '')
        gain = dragon.get('gain', 0)
        theme_purity = dragon.get('theme_purity', 0) * 100
        reason = dragon.get('core_reason', '')
        
        return f'''
        <div class="dragon-slot" style="border-color: {color};">
            <div class="dragon-rank" style="background: {color};">{label}</div>
            <div class="dragon-info">
                <div class="dragon-name">{name}</div>
                <div class="dragon-stats">
                    <span class="dragon-gain">累计涨幅 +{gain:.1f}%</span>
                    <span class="dragon-purity">题材正宗度 {theme_purity:.0f}%</span>
                </div>
                {f'<div class="dragon-reason">{reason}</div>' if reason else ''}
            </div>
        </div>
        '''
    
    def render(self) -> str:
        return f'''
        <div class="boya-dragon-card">
            <div class="dragon-title">
                <span class="dragon-icon">🐉</span>
                <span>龙头梯队</span>
            </div>
            <div class="dragon-troupe">
                {self._render_dragon_slot(self.dragon_one, 1)}
                {self._render_dragon_slot(self.dragon_two, 2)}
                {self._render_dragon_slot(self.dragon_three, 3)}
            </div>
            <div class="dragon-rationale">
                <span class="rationale-label">梯队逻辑：</span>
                {self.rationale}
            </div>
            <div class="dragon-strategy-note">
                💡 龙空龙策略：只做龙头，不碰杂毛。龙头有溢价，杂毛有风险。
            </div>
        </div>
        <style>
            .boya-dragon-card {{
                background: rgba(255, 255, 255, 0.05);
                border: 1px solid rgba(255, 255, 255, 0.1);
                border-radius: 16px;
                padding: 24px;
                color: white;
            }}
            .dragon-title {{
                font-size: 18px;
                font-weight: 700;
                margin-bottom: 20px;
                display: flex;
                align-items: center;
                gap: 10px;
            }}
            .dragon-icon {{
                font-size: 24px;
            }}
            .dragon-troupe {{
                display: flex;
                flex-direction: column;
                gap: 12px;
                margin-bottom: 20px;
            }}
            .dragon-slot {{
                display: flex;
                align-items: stretch;
                gap: 0;
                border: 1px solid;
                border-radius: 12px;
                overflow: hidden;
            }}
            .dragon-rank {{
                display: flex;
                align-items: center;
                justify-content: center;
                width: 60px;
                color: white;
                font-weight: 700;
                font-size: 14px;
                flex-shrink: 0;
            }}
            .dragon-info {{
                flex: 1;
                padding: 12px 16px;
                background: rgba(255, 255, 255, 0.03);
            }}
            .dragon-name {{
                font-size: 16px;
                font-weight: 600;
                color: white;
                margin-bottom: 4px;
            }}
            .dragon-stats {{
                display: flex;
                gap: 16px;
                font-size: 12px;
                color: rgba(255, 255, 255, 0.6);
            }}
            .dragon-gain {{
                color: #34d399;
                font-weight: 600;
            }}
            .dragon-reason {{
                margin-top: 6px;
                font-size: 12px;
                color: rgba(255, 255, 255, 0.5);
            }}
            .dragon-rationale {{
                font-size: 13px;
                color: rgba(255, 255, 255, 0.8);
                line-height: 1.6;
                padding-top: 16px;
                border-top: 1px solid rgba(255, 255, 255, 0.1);
            }}
            .rationale-label {{
                font-weight: 600;
                color: rgba(255, 255, 255, 0.9);
            }}
            .dragon-strategy-note {{
                margin-top: 12px;
                padding: 10px 14px;
                background: rgba(251, 191, 36, 0.1);
                border-radius: 8px;
                font-size: 12px;
                color: #fbbf24;
                line-height: 1.5;
            }}
        </style>
        '''


class BoyaBuyPointCard(Component):
    """买点评级卡片"""
    
    def __init__(self, score: float, level: str, suggest_price: float = None, 
                 support_level: float = None, rationale: str = ''):
        self.score = score
        self.level = level
        self.suggest_price = suggest_price
        self.support_level = support_level
        self.rationale = rationale
    
    def _get_level_style(self) -> Dict:
        styles = {
            '强烈推荐': {'color': '#34d399', 'bg': 'rgba(52, 211, 153, 0.15)'},
            '谨慎追高': {'color': '#fbbf24', 'bg': 'rgba(251, 191, 36, 0.15)'},
            '观望为主': {'color': '#60a5fa', 'bg': 'rgba(96, 165, 250, 0.15)'},
            '建议回避': {'color': '#f87171', 'bg': 'rgba(248, 113, 113, 0.15)'},
            '坚决不碰': {'color': '#ef4444', 'bg': 'rgba(239, 68, 68, 0.15)'},
        }
        return styles.get(self.level, {'color': '#9ca3af', 'bg': 'rgba(156, 163, 175, 0.15)'})
    
    def render(self) -> str:
        style = self._get_level_style()
        
        # 环形进度计算
        circumference = 2 * 3.14159 * 45
        offset = circumference - (self.score / 100) * circumference
        
        return f'''
        <div class="boya-buy-point-card">
            <div class="buy-point-header">
                <span class="buy-point-icon">🎯</span>
                <span>买点评级</span>
            </div>
            <div class="buy-point-body">
                <div class="score-ring">
                    <svg width="120" height="120" viewBox="0 0 120 120">
                        <circle cx="60" cy="60" r="45" fill="none" 
                                stroke="rgba(255,255,255,0.1)" stroke-width="8"/>
                        <circle cx="60" cy="60" r="45" fill="none" 
                                stroke="{style['color']}" stroke-width="8"
                                stroke-dasharray="{circumference}"
                                stroke-dashoffset="{offset}"
                                stroke-linecap="round"
                                transform="rotate(-90 60 60)"/>
                    </svg>
                    <div class="score-ring-center">
                        <span class="score-value">{self.score:.0f}</span>
                        <span class="score-unit">分</span>
                    </div>
                </div>
                <div class="buy-point-info">
                    <div class="buy-level" style="color: {style['color']}; background: {style['bg']};">
                        {self.level}
                    </div>
                    <div class="buy-details">
                        {f'<div class="buy-detail"><span class="detail-label">建议买入价</span><span class="detail-value">{self.suggest_price:.2f} 元</span></div>' if self.suggest_price else ''}
                        {f'<div class="buy-detail"><span class="detail-label">支撑位</span><span class="detail-value">{self.support_level:.2f} 元</span></div>' if self.support_level else ''}
                    </div>
                </div>
            </div>
            <div class="buy-point-rationale">
                {self.rationale}
            </div>
        </div>
        <style>
            .boya-buy-point-card {{
                background: rgba(255, 255, 255, 0.05);
                border: 1px solid rgba(255, 255, 255, 0.1);
                border-radius: 16px;
                padding: 24px;
                color: white;
            }}
            .buy-point-header {{
                font-size: 18px;
                font-weight: 700;
                margin-bottom: 20px;
                display: flex;
                align-items: center;
                gap: 10px;
            }}
            .buy-point-icon {{
                font-size: 24px;
            }}
            .buy-point-body {{
                display: flex;
                align-items: center;
                gap: 24px;
                margin-bottom: 16px;
            }}
            .score-ring {{
                position: relative;
                width: 120px;
                height: 120px;
                flex-shrink: 0;
            }}
            .score-ring-center {{
                position: absolute;
                top: 50%;
                left: 50%;
                transform: translate(-50%, -50%);
                text-align: center;
            }}
            .score-value {{
                display: block;
                font-size: 32px;
                font-weight: 800;
                color: white;
                line-height: 1;
            }}
            .score-unit {{
                font-size: 12px;
                color: rgba(255, 255, 255, 0.6);
            }}
            .buy-point-info {{
                flex: 1;
            }}
            .buy-level {{
                display: inline-block;
                padding: 6px 16px;
                border-radius: 20px;
                font-weight: 600;
                font-size: 16px;
                margin-bottom: 16px;
            }}
            .buy-details {{
                display: flex;
                flex-direction: column;
                gap: 8px;
            }}
            .buy-detail {{
                display: flex;
                justify-content: space-between;
                font-size: 13px;
            }}
            .detail-label {{
                color: rgba(255, 255, 255, 0.6);
            }}
            .detail-value {{
                color: rgba(255, 255, 255, 0.9);
                font-weight: 600;
            }}
            .buy-point-rationale {{
                font-size: 13px;
                color: rgba(255, 255, 255, 0.8);
                line-height: 1.6;
                padding-top: 16px;
                border-top: 1px solid rgba(255, 255, 255, 0.1);
            }}
        </style>
        '''


class BoyaStopLossCard(Component):
    """止损纪律卡片"""
    
    def __init__(self, fixed_stop_pct: float, ma_stop: int, position_limit_pct: int, rationale: str):
        self.fixed_stop_pct = fixed_stop_pct
        self.ma_stop = ma_stop
        self.position_limit_pct = position_limit_pct
        self.rationale = rationale
    
    def render(self) -> str:
        return f'''
        <div class="boya-stoploss-card">
            <div class="stoploss-header">
                <span class="stoploss-icon">🛡️</span>
                <span>止损纪律</span>
                <span class="stoploss-warning">铁律！</span>
            </div>
            <div class="stoploss-rules">
                <div class="stoploss-rule">
                    <div class="rule-icon">📉</div>
                    <div class="rule-content">
                        <div class="rule-title">固定止损</div>
                        <div class="rule-value">{self.fixed_stop_pct}%</div>
                        <div class="rule-desc">亏损达到上限必须无条件止损</div>
                    </div>
                </div>
                <div class="stoploss-rule">
                    <div class="rule-icon">📊</div>
                    <div class="rule-content">
                        <div class="rule-title">均线止损</div>
                        <div class="rule-value">{self.ma_stop}日线</div>
                        <div class="rule-desc">有效跌破趋势线立即离场</div>
                    </div>
                </div>
                <div class="stoploss-rule">
                    <div class="rule-icon">💰</div>
                    <div class="rule-content">
                        <div class="rule-title">仓位上限</div>
                        <div class="rule-value">{self.position_limit_pct}%</div>
                        <div class="rule-desc">单票仓位绝不超过此比例</div>
                    </div>
                </div>
            </div>
            <div class="stoploss-footer">
                ⚠️ {self.rationale}
            </div>
        </div>
        <style>
            .boya-stoploss-card {{
                background: rgba(239, 68, 68, 0.08);
                border: 1px solid rgba(239, 68, 68, 0.3);
                border-radius: 16px;
                padding: 24px;
                color: white;
            }}
            .stoploss-header {{
                display: flex;
                align-items: center;
                gap: 10px;
                margin-bottom: 20px;
            }}
            .stoploss-icon {{
                font-size: 24px;
            }}
            .stoploss-header span:nth-child(2) {{
                font-size: 18px;
                font-weight: 700;
                flex: 1;
            }}
            .stoploss-warning {{
                background: #ef4444;
                color: white;
                padding: 4px 12px;
                border-radius: 12px;
                font-size: 12px;
                font-weight: 600;
            }}
            .stoploss-rules {{
                display: grid;
                grid-template-columns: repeat(3, 1fr);
                gap: 12px;
                margin-bottom: 16px;
            }}
            .stoploss-rule {{
                background: rgba(255, 255, 255, 0.05);
                border-radius: 12px;
                padding: 16px;
                text-align: center;
            }}
            .rule-icon {{
                font-size: 28px;
                margin-bottom: 8px;
            }}
            .rule-title {{
                font-size: 13px;
                color: rgba(255, 255, 255, 0.6);
                margin-bottom: 4px;
            }}
            .rule-value {{
                font-size: 24px;
                font-weight: 800;
                color: #f87171;
                margin-bottom: 4px;
            }}
            .rule-desc {{
                font-size: 11px;
                color: rgba(255, 255, 255, 0.5);
                line-height: 1.4;
            }}
            .stoploss-footer {{
                font-size: 12px;
                color: rgba(255, 255, 255, 0.7);
                line-height: 1.6;
                padding-top: 16px;
                border-top: 1px solid rgba(239, 68, 68, 0.2);
            }}
        </style>
        '''


class BoyaFlexibilityCard(Component):
    """弹性测算卡片"""
    
    def __init__(self, short_term_upside: float, mid_term_upside: float,
                 drawdown_risk: float, risk_reward_ratio: float, rationale: str):
        self.short_term_upside = short_term_upside
        self.mid_term_upside = mid_term_upside
        self.drawdown_risk = drawdown_risk
        self.risk_reward_ratio = risk_reward_ratio
        self.rationale = rationale
    
    def render(self) -> str:
        # 盈亏比评价
        if self.risk_reward_ratio >= 3:
            rr_level = '优秀'
            rr_color = '#34d399'
        elif self.risk_reward_ratio >= 2:
            rr_level = '良好'
            rr_color = '#fbbf24'
        else:
            rr_level = '一般'
            rr_color = '#f87171'
        
        return f'''
        <div class="boya-flex-card">
            <div class="flex-header">
                <span class="flex-icon">📈</span>
                <span>弹性测算</span>
            </div>
            <div class="flex-metrics">
                <div class="flex-metric">
                    <div class="metric-label">短期上涨空间</div>
                    <div class="metric-value up">+{self.short_term_upside}%</div>
                </div>
                <div class="flex-metric">
                    <div class="metric-label">中期上涨空间</div>
                    <div class="metric-value up">+{self.mid_term_upside}%</div>
                </div>
                <div class="flex-metric">
                    <div class="metric-label">回调风险</div>
                    <div class="metric-value down">-{self.drawdown_risk}%</div>
                </div>
                <div class="flex-metric highlight">
                    <div class="metric-label">盈亏比</div>
                    <div class="metric-value rr" style="color: {rr_color};">{self.risk_reward_ratio}:1</div>
                    <div class="metric-level" style="color: {rr_color};">{rr_level}</div>
                </div>
            </div>
            <div class="flex-rationale">
                💡 {self.rationale}
            </div>
        </div>
        <style>
            .boya-flex-card {{
                background: rgba(255, 255, 255, 0.05);
                border: 1px solid rgba(255, 255, 255, 0.1);
                border-radius: 16px;
                padding: 24px;
                color: white;
            }}
            .flex-header {{
                font-size: 18px;
                font-weight: 700;
                margin-bottom: 20px;
                display: flex;
                align-items: center;
                gap: 10px;
            }}
            .flex-icon {{
                font-size: 24px;
            }}
            .flex-metrics {{
                display: grid;
                grid-template-columns: repeat(4, 1fr);
                gap: 12px;
                margin-bottom: 16px;
            }}
            .flex-metric {{
                background: rgba(255, 255, 255, 0.05);
                border-radius: 12px;
                padding: 16px 12px;
                text-align: center;
            }}
            .flex-metric.highlight {{
                background: rgba(251, 191, 36, 0.1);
                border: 1px solid rgba(251, 191, 36, 0.3);
            }}
            .metric-label {{
                font-size: 12px;
                color: rgba(255, 255, 255, 0.6);
                margin-bottom: 8px;
            }}
            .metric-value {{
                font-size: 22px;
                font-weight: 800;
            }}
            .metric-value.up {{
                color: #34d399;
            }}
            .metric-value.down {{
                color: #f87171;
            }}
            .metric-level {{
                font-size: 12px;
                font-weight: 600;
                margin-top: 2px;
            }}
            .flex-rationale {{
                font-size: 13px;
                color: rgba(255, 255, 255, 0.8);
                line-height: 1.6;
                padding-top: 16px;
                border-top: 1px solid rgba(255, 255, 255, 0.1);
            }}
        </style>
        '''


class BoyaPortfolioImpactCard(Component):
    """组合影响分析卡片"""
    
    def __init__(self, concentration_risk: str, correlation_risk: str, suggestion: str):
        self.concentration_risk = concentration_risk
        self.correlation_risk = correlation_risk
        self.suggestion = suggestion
    
    def render(self) -> str:
        return f'''
        <div class="boya-portfolio-card">
            <div class="portfolio-header">
                <span class="portfolio-icon">💼</span>
                <span>组合影响分析</span>
            </div>
            <div class="portfolio-impacts">
                <div class="impact-item">
                    <div class="impact-label">集中度风险</div>
                    <div class="impact-value">{self.concentration_risk}</div>
                </div>
                <div class="impact-item">
                    <div class="impact-label">相关性风险</div>
                    <div class="impact-value">{self.correlation_risk}</div>
                </div>
            </div>
            <div class="portfolio-suggestion">
                <div class="suggestion-label">操作建议</div>
                <div class="suggestion-content">{self.suggestion}</div>
            </div>
        </div>
        <style>
            .boya-portfolio-card {{
                background: rgba(255, 255, 255, 0.05);
                border: 1px solid rgba(255, 255, 255, 0.1);
                border-radius: 16px;
                padding: 24px;
                color: white;
            }}
            .portfolio-header {{
                font-size: 18px;
                font-weight: 700;
                margin-bottom: 20px;
                display: flex;
                align-items: center;
                gap: 10px;
            }}
            .portfolio-icon {{
                font-size: 24px;
            }}
            .portfolio-impacts {{
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 16px;
                margin-bottom: 20px;
            }}
            .impact-item {{
                background: rgba(255, 255, 255, 0.05);
                border-radius: 12px;
                padding: 16px;
            }}
            .impact-label {{
                font-size: 13px;
                color: rgba(255, 255, 255, 0.6);
                margin-bottom: 8px;
            }}
            .impact-value {{
                font-size: 14px;
                font-weight: 600;
                color: rgba(255, 255, 255, 0.9);
                line-height: 1.5;
            }}
            .portfolio-suggestion {{
                background: rgba(96, 165, 250, 0.1);
                border-radius: 12px;
                padding: 16px;
                border-left: 3px solid #60a5fa;
            }}
            .suggestion-label {{
                font-size: 13px;
                font-weight: 600;
                color: #60a5fa;
                margin-bottom: 6px;
            }}
            .suggestion-content {{
                font-size: 13px;
                color: rgba(255, 255, 255, 0.85);
                line-height: 1.6;
            }}
        </style>
        '''


class BoyaPredictionList(Component):
    """预判记录列表"""
    
    def __init__(self, predictions: List[Dict]):
        self.predictions = predictions
    
    def _render_prediction(self, pred: Dict, index: int) -> str:
        content = pred.get('content', '')
        confidence = pred.get('confidence', 0) * 100
        verify_date = pred.get('verify_date', '')
        category = pred.get('category', '')
        status = pred.get('status', 'pending')
        
        status_config = {
            'pending': {'icon': '⏳', 'text': '待验证', 'color': '#fbbf24'},
            'right': {'icon': '✅', 'text': '正确', 'color': '#34d399'},
            'wrong': {'icon': '❌', 'text': '错误', 'color': '#f87171'},
            'partial': {'icon': '🔶', 'text': '部分正确', 'color': '#fb923c'},
        }
        sc = status_config.get(status, status_config['pending'])
        
        return f'''
        <div class="prediction-item">
            <div class="prediction-index">{index}</div>
            <div class="prediction-content">
                <div class="prediction-text">{content}</div>
                <div class="prediction-meta">
                    <span class="prediction-category">{category}</span>
                    <span class="prediction-confidence">置信度 {confidence:.0f}%</span>
                    <span class="prediction-date">验证日: {verify_date}</span>
                </div>
            </div>
            <div class="prediction-status" style="color: {sc['color']};">
                <span>{sc['icon']}</span>
                <span>{sc['text']}</span>
            </div>
        </div>
        '''
    
    def render(self) -> str:
        items_html = ''
        for i, pred in enumerate(self.predictions, 1):
            items_html += self._render_prediction(pred, i)
        
        return f'''
        <div class="boya-prediction-card">
            <div class="prediction-header">
                <span class="prediction-icon">🔮</span>
                <span>预判记录</span>
                <span class="prediction-badge">纳入验证闭环</span>
            </div>
            <div class="prediction-list">
                {items_html}
            </div>
        </div>
        <style>
            .boya-prediction-card {{
                background: rgba(255, 255, 255, 0.05);
                border: 1px solid rgba(255, 255, 255, 0.1);
                border-radius: 16px;
                padding: 24px;
                color: white;
            }}
            .prediction-header {{
                display: flex;
                align-items: center;
                gap: 10px;
                margin-bottom: 20px;
            }}
            .prediction-icon {{
                font-size: 24px;
            }}
            .prediction-header span:nth-child(2) {{
                font-size: 18px;
                font-weight: 700;
                flex: 1;
            }}
            .prediction-badge {{
                background: rgba(168, 85, 247, 0.2);
                color: #c084fc;
                padding: 4px 12px;
                border-radius: 12px;
                font-size: 12px;
                font-weight: 500;
            }}
            .prediction-list {{
                display: flex;
                flex-direction: column;
                gap: 12px;
            }}
            .prediction-item {{
                display: flex;
                align-items: flex-start;
                gap: 12px;
                background: rgba(255, 255, 255, 0.03);
                border-radius: 10px;
                padding: 14px 16px;
            }}
            .prediction-index {{
                width: 28px;
                height: 28px;
                border-radius: 50%;
                background: rgba(168, 85, 247, 0.3);
                color: #c084fc;
                display: flex;
                align-items: center;
                justify-content: center;
                font-weight: 700;
                font-size: 14px;
                flex-shrink: 0;
            }}
            .prediction-content {{
                flex: 1;
            }}
            .prediction-text {{
                font-size: 14px;
                color: rgba(255, 255, 255, 0.9);
                line-height: 1.6;
                margin-bottom: 6px;
            }}
            .prediction-meta {{
                display: flex;
                gap: 12px;
                font-size: 11px;
                color: rgba(255, 255, 255, 0.5);
            }}
            .prediction-category {{
                background: rgba(255, 255, 255, 0.1);
                padding: 2px 8px;
                border-radius: 8px;
            }}
            .prediction-status {{
                display: flex;
                flex-direction: column;
                align-items: center;
                gap: 4px;
                font-size: 12px;
                font-weight: 600;
                flex-shrink: 0;
            }}
        </style>
        '''


class BoyaStrategySummaryCard(Component):
    """boya策略总纲卡片 - 第10章总结用"""
    
    def __init__(self, level: str, dragon_name: str, buy_suggestion: str,
                 stop_loss: str, risk_reward: str, overall_rating: str):
        self.level = level
        self.dragon_name = dragon_name
        self.buy_suggestion = buy_suggestion
        self.stop_loss = stop_loss
        self.risk_reward = risk_reward
        self.overall_rating = overall_rating
    
    def render(self) -> str:
        return f'''
        <div class="boya-strategy-summary">
            <div class="summary-title">
                <span class="summary-icon">⚡</span>
                <span>boya投资策略 · 总纲</span>
            </div>
            <div class="summary-grid">
                <div class="summary-item main">
                    <div class="summary-label">主线评级</div>
                    <div class="summary-value level">{self.level}级</div>
                </div>
                <div class="summary-item">
                    <div class="summary-label">核心标的</div>
                    <div class="summary-value">{self.dragon_name}</div>
                </div>
                <div class="summary-item">
                    <div class="summary-label">操作建议</div>
                    <div class="summary-value">{self.buy_suggestion}</div>
                </div>
                <div class="summary-item">
                    <div class="summary-label">止损策略</div>
                    <div class="summary-value">{self.stop_loss}</div>
                </div>
                <div class="summary-item">
                    <div class="summary-label">盈亏比</div>
                    <div class="summary-value">{self.risk_reward}</div>
                </div>
                <div class="summary-item">
                    <div class="summary-label">综合评级</div>
                    <div class="summary-value rating">{self.overall_rating}</div>
                </div>
            </div>
            <div class="summary-footer">
                以上分析仅供参考，不构成投资建议。投资有风险，入市需谨慎。
            </div>
        </div>
        <style>
            .boya-strategy-summary {{
                background: linear-gradient(135deg, rgba(168, 85, 247, 0.2) 0%, rgba(251, 146, 60, 0.2) 100%);
                border: 2px solid rgba(251, 146, 60, 0.4);
                border-radius: 20px;
                padding: 28px;
                color: white;
                margin-top: 20px;
            }}
            .summary-title {{
                text-align: center;
                font-size: 22px;
                font-weight: 800;
                margin-bottom: 24px;
                display: flex;
                align-items: center;
                justify-content: center;
                gap: 10px;
            }}
            .summary-icon {{
                font-size: 28px;
            }}
            .summary-grid {{
                display: grid;
                grid-template-columns: repeat(3, 1fr);
                gap: 16px;
                margin-bottom: 20px;
            }}
            .summary-item {{
                background: rgba(255, 255, 255, 0.08);
                border-radius: 12px;
                padding: 16px;
                text-align: center;
            }}
            .summary-item.main {{
                background: rgba(251, 191, 36, 0.15);
                border: 1px solid rgba(251, 191, 36, 0.4);
            }}
            .summary-label {{
                font-size: 12px;
                color: rgba(255, 255, 255, 0.6);
                margin-bottom: 6px;
            }}
            .summary-value {{
                font-size: 18px;
                font-weight: 700;
                color: white;
            }}
            .summary-value.level {{
                color: #fbbf24;
                font-size: 24px;
            }}
            .summary-value.rating {{
                color: #34d399;
            }}
            .summary-footer {{
                text-align: center;
                font-size: 11px;
                color: rgba(255, 255, 255, 0.4);
                padding-top: 16px;
                border-top: 1px solid rgba(255, 255, 255, 0.1);
            }}
        </style>
        '''
