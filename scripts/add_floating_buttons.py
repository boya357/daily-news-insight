#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
为HTML页面批量添加悬浮按钮（回到顶部、阅读进度条、打印、分享）
"""

import os
import re
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DOCS_DIR = BASE_DIR / 'docs'

FLOATING_BUTTONS_HTML = '''
<!-- 悬浮按钮组 -->
<div id="floatingButtons" class="fixed right-6 bottom-6 flex flex-col gap-2 z-50">
    <!-- 阅读进度条 -->
    <div class="reading-progress-bar fixed top-0 left-0 h-1 bg-gradient-to-r from-indigo-500 to-purple-600 z-50" id="readingProgress" style="width: 0%;"></div>
    
    <!-- 回到顶部按钮 -->
    <button id="backToTop" class="w-10 h-10 rounded-full bg-white/90 backdrop-blur-sm shadow-lg hover:shadow-xl transition-all flex items-center justify-center text-gray-600 hover:text-indigo-600 opacity-0 translate-y-4 pointer-events-none" onclick="scrollToTop()" title="回到顶部">
        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 10l7-7m0 0l7 7m-7-7v18"/>
        </svg>
    </button>
    
    <!-- 打印按钮 -->
    <button class="w-10 h-10 rounded-full bg-white/90 backdrop-blur-sm shadow-lg hover:shadow-xl transition-all flex items-center justify-center text-gray-600 hover:text-indigo-600" onclick="window.print()" title="打印页面">
        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 17h2a2 2 0 002-2v-4a2 2 0 00-2-2H5a2 2 0 00-2 2v4a2 2 0 002 2h2m2 4h6a2 2 0 002-2v-4a2 2 0 00-2-2H9a2 2 0 00-2 2v4a2 2 0 002 2zm8-12V5a2 2 0 00-2-2H9a2 2 0 00-2 2v4h10z"/>
        </svg>
    </button>
    
    <!-- 分享按钮 -->
    <button class="w-10 h-10 rounded-full bg-white/90 backdrop-blur-sm shadow-lg hover:shadow-xl transition-all flex items-center justify-center text-gray-600 hover:text-indigo-600" onclick="sharePage()" title="分享">
        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8.684 13.342C8.886 12.938 9 12.482 9 12c0-.482-.114-.938-.316-1.342m0 2.684a3 3 0 110-2.684m0 2.684l6.632 3.316m-6.632-6l6.632-3.316m0 0a3 3 0 105.367-2.684 3 3 0 00-5.367 2.684zm0 9.316a3 3 0 105.367 2.684 3 3 0 00-5.367-2.684z"/>
        </svg>
    </button>
</div>

<style>
    .reading-progress-bar {
        transition: width 0.1s ease-out;
    }
    
    #backToTop.show {
        opacity: 1;
        transform: translateY(0);
        pointer-events: auto;
    }
    
    #floatingButtons button {
        transition: all 0.3s ease;
    }
    
    #floatingButtons button:hover {
        transform: scale(1.1);
    }
    
    @media print {
        #floatingButtons, .reading-progress-bar {
            display: none !important;
        }
    }
</style>

<script>
    // 回到顶部
    function scrollToTop() {
        window.scrollTo({ top: 0, behavior: 'smooth' });
    }
    
    // 分享页面
    function sharePage() {
        if (navigator.share) {
            navigator.share({
                title: document.title,
                url: window.location.href
            });
        } else {
            // 复制链接到剪贴板
            navigator.clipboard.writeText(window.location.href).then(function() {
                alert('链接已复制到剪贴板');
            }).catch(function() {
                prompt('复制链接：', window.location.href);
            });
        }
    }
    
    // 滚动监听 - 更新进度条和回到顶部按钮
    window.addEventListener('scroll', function() {
        const scrollTop = window.scrollY;
        const docHeight = document.documentElement.scrollHeight - window.innerHeight;
        const scrollPercent = docHeight > 0 ? (scrollTop / docHeight) * 100 : 0;
        
        // 更新进度条
        const progressBar = document.getElementById('readingProgress');
        if (progressBar) {
            progressBar.style.width = scrollPercent + '%';
        }
        
        // 显示/隐藏回到顶部按钮
        const backToTop = document.getElementById('backToTop');
        if (backToTop) {
            if (scrollTop > 300) {
                backToTop.classList.add('show');
            } else {
                backToTop.classList.remove('show');
            }
        }
    });
</script>
'''


def has_floating_buttons(html_content):
    """检查页面是否已经有悬浮按钮"""
    return 'backToTop' in html_content or 'floatingButtons' in html_content or 'readingProgress' in html_content


def add_floating_buttons_to_html(file_path):
    """为单个HTML文件添加悬浮按钮"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if has_floating_buttons(content):
            return 'skipped'
        
        # 在</body>标签前插入悬浮按钮
        if '</body>' in content:
            content = content.replace('</body>', FLOATING_BUTTONS_HTML + '\n</body>')
        else:
            # 如果没有</body>标签，就在文件末尾添加
            content += FLOATING_BUTTONS_HTML
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return 'success'
    except Exception as e:
        print(f"  ❌ 处理失败: {file_path} - {e}")
        return 'failed'


def process_directory(dir_path, recursive=True):
    """处理目录下的所有HTML文件"""
    dir_path = Path(dir_path)
    success_count = 0
    skip_count = 0
    fail_count = 0
    
    if recursive:
        html_files = list(dir_path.rglob('*.html'))
    else:
        html_files = list(dir_path.glob('*.html'))
    
    # 排除一些不需要的文件
    exclude_patterns = ['_templates', 'test', 'backup']
    html_files = [
        f for f in html_files 
        if not any(pattern in str(f) for pattern in exclude_patterns)
    ]
    
    print(f"找到 {len(html_files)} 个HTML文件")
    
    for i, file_path in enumerate(html_files, 1):
        result = add_floating_buttons_to_html(file_path)
        
        if result == 'success':
            success_count += 1
            print(f"  ✅ [{i}/{len(html_files)}] {file_path.name}")
        elif result == 'skipped':
            skip_count += 1
        else:
            fail_count += 1
    
    print(f"\n📊 处理完成：")
    print(f"   成功: {success_count}")
    print(f"   跳过(已有): {skip_count}")
    print(f"   失败: {fail_count}")
    
    return success_count, skip_count, fail_count


def main():
    if len(sys.argv) > 1:
        # 处理指定目录或文件
        target = sys.argv[1]
        target_path = Path(target)
        if target_path.is_file():
            result = add_floating_buttons_to_html(target_path)
            print(f"处理结果: {result}")
        elif target_path.is_dir():
            process_directory(target_path)
        else:
            print(f"错误: {target} 不存在")
            sys.exit(1)
    else:
        # 默认处理docs目录下的所有报告目录
        report_dirs = [
            'daily',
            'aftermarket', 
            'intraday',
            'industry_chain',
            'weekly_review',
            'weekly_outlook',
            'monthly',
            's_level_catalyst',
            'weekend_express',
            'tomorrow_catalyst',
            '题材深度',
            '题材健康度报告',
            'reports',
        ]
        
        total_success = 0
        total_skip = 0
        total_fail = 0
        
        for dir_name in report_dirs:
            dir_path = DOCS_DIR / dir_name
            if dir_path.exists():
                print(f"\n📁 处理目录: {dir_name}")
                s, k, f = process_directory(dir_path)
                total_success += s
                total_skip += k
                total_fail += f
        
        print(f"\n{'='*50}")
        print(f"🎉 总统计：")
        print(f"   成功添加: {total_success}")
        print(f"   跳过(已有): {total_skip}")
        print(f"   失败: {total_fail}")
        print(f"{'='*50}")


if __name__ == '__main__':
    main()
