#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
批量为所有列表页脚本添加移动端适配CSS
在</style>之前插入
"""
import re
import os

# 需要处理的文件列表
FILES = [
    'update_daily_list.py',
    'update_intraday_list.py',
    'update_aftermarket_list.py',
    'update_weekly_review_list.py',
    'update_weekly_outlook_list.py',
    'update_weekend_express_list.py',
    'update_tomorrow_catalyst_list.py',
    'update_slevel_catalyst_list.py',
    'update_monthly_list.py',
]

# 移动端适配CSS（插入到</style>之前）
MOBILE_CSS = '''        
        /* ========== 汉堡菜单样式 ========== */
        .hamburger-btn {{
            display: none;
            background: rgba(255,255,255,0.2);
            border: none;
            color: white;
            width: 44px;
            height: 44px;
            border-radius: 8px;
            cursor: pointer;
            font-size: 20px;
            z-index: 99999;
        }}
        
        .mobile-menu {{
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            z-index: 99998;
            display: none;
            padding-top: 80px;
            overflow-y: auto;
        }}
        
        .mobile-menu.show {{
            display: block;
        }}
        
        .mobile-menu-item {{
            display: block;
            color: white !important;
            padding: 16px 24px;
            text-decoration: none;
            font-size: 18px;
            border-bottom: 1px solid rgba(255,255,255,0.1);
        }}
        
        .mobile-menu-item:hover {{
            background: rgba(255,255,255,0.1);
        }}
        
        .close-menu-btn {{
            position: absolute;
            top: 16px;
            right: 16px;
            background: rgba(255,255,255,0.2);
            border: none;
            color: white;
            width: 44px;
            height: 44px;
            border-radius: 8px;
            cursor: pointer;
            font-size: 20px;
        }}
        
        /* ========== 移动端响应式优化 ========== */
        @media (max-width: 768px) {{
            /* 导航栏：隐藏按钮，显示汉堡 */
            .nav-links {{
                display: none !important;
            }}
            .hamburger-btn {{
                display: block !important;
            }}
            
            /* 卡片网格改为2列 */
            .grid-cols-4 {{
                grid-template-columns: repeat(2, 1fr) !important;
            }}
            
            /* 字体响应式缩放 */
            .text-4xl {{ font-size: 1.875rem !important; }}
            .text-3xl {{ font-size: 1.5rem !important; }}
            .text-2xl {{ font-size: 1.25rem !important; }}
            
            /* 内边距紧凑化 */
            .p-8 {{ padding: 1.5rem !important; }}
            .p-6 {{ padding: 1.25rem !important; }}
            
            /* 表格横向滚动 */
            table {{ 
                display: block; 
                overflow-x: auto;
                -webkit-overflow-scrolling: touch;
            }}
            
            /* 增大点击区域 */
            a, button {{ 
                min-height: 44px; 
                display: inline-flex;
                align-items: center;
            }}
        }}
        
        /* ========== 平板端专用样式 ========== */
        @media (min-width: 769px) and (max-width: 1024px) {{
            .grid-cols-4 {{ grid-template-columns: repeat(3, 1fr) !important; }}
        }}'''

def process_file(filename):
    """处理单个文件"""
    if not os.path.exists(filename):
        print(f'❌ {filename} 不存在，跳过')
        return False
    
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 检查是否已经有hamburger样式了
    if 'hamburger-btn' in content:
        print(f'✅ {filename}: 已有移动端CSS，跳过')
        return True
    
    # 在</style>之前插入CSS
    if '</style>' in content:
        content = content.replace('</style>', MOBILE_CSS + '\n    </style>')
        print(f'✅ {filename}: 移动端CSS已添加')
    else:
        print(f'❌ {filename}: 未找到</style>标签')
        return False
    
    # 写回文件
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return True

def main():
    print('=' * 50)
    print('开始批量添加移动端适配CSS...')
    print('=' * 50)
    
    success_count = 0
    for f in FILES:
        if process_file(f):
            success_count += 1
        print('---')
    
    print('=' * 50)
    print(f'完成！成功处理 {success_count}/{len(FILES)} 个文件')
    print('=' * 50)

if __name__ == '__main__':
    main()
