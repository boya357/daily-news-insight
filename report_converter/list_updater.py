#!/usr/bin/env python3
"""
安全的列表页更新工具
绝对不会覆盖成单篇报告
"""
import os
import sys
import glob


class ListPageUpdater:
    """安全的列表页更新器"""
    
    def __init__(self, docs_dir: str):
        self.docs_dir = docs_dir
        self.page_configs = {
            'industry_chain': {
                'title': '产业链全景追踪',
                'subtitle': '覆盖AI算力、新能源、半导体等核心赛道',
                'report_type_mapping': self._industry_chain_mapping
            },
            'daily': {
                'title': '每日新闻洞察',
                'subtitle': '每日市场动态与行业资讯',
                'report_type_mapping': self._daily_mapping
            },
            'intraday': {
                'title': '盘中快报',
                'subtitle': '实时市场动态追踪',
                'report_type_mapping': self._simple_mapping
            },
            'aftermarket': {
                'title': '盘后速递',
                'subtitle': '收盘后重要资讯汇总',
                'report_type_mapping': self._simple_mapping
            },
            'weekly_review': {
                'title': '周复盘报告',
                'subtitle': '一周市场回顾与总结',
                'report_type_mapping': self._simple_mapping
            }
        }
    
    def update_all(self):
        """更新所有列表页"""
        for page_type in self.page_configs.keys():
            self.update_single(page_type)
    
    def update_single(self, page_type: str):
        """更新单个列表页"""
        config = self.page_configs.get(page_type)
        if not config:
            print(f"⚠️  未知的页面类型: {page_type}")
            return False
        
        list_file = os.path.join(self.docs_dir, page_type, 'latest.html')
        
        # 查找所有HTML报告（排除latest.html自己）
        pattern = os.path.join(self.docs_dir, page_type, '*.html')
        html_files = glob.glob(pattern)
        html_files = [f for f in html_files if 'latest.html' not in os.path.basename(f)]
        
        if not html_files:
            print(f"⚠️  {page_type}: 未找到报告文件")
            return False
        
        # 按文件名排序（最新的在前）
        html_files.sort(reverse=True)
        
        # 生成报告卡片
        report_cards = []
        for html_file in html_files[:12]:  # 只显示最新12篇
            filename = os.path.basename(html_file)
            title, icon, tag, tag_class = config['report_type_mapping'](filename)
            
            report_cards.append(f'''
            <a href="{filename}" class="report-card block p-5 bg-white border border-gray-100 rounded-xl text-center group hover:shadow-lg transition-all">
                <div class="text-3xl mb-2">{icon}</div>
                <div class="font-semibold text-gray-800 text-sm mb-1 group-hover:text-indigo-600 transition-colors line-clamp-2">{title}</div>
                <span class="inline-block px-2 py-1 text-xs font-bold {tag_class} rounded">{tag}</span>
            </a>
            ''')
        
        # 生成完整列表页
        list_html = self._generate_list_page(
            title=config['title'],
            subtitle=config['subtitle'],
            current_page=page_type,
            cards_html=''.join(report_cards),
            grid_cols='grid-cols-2 md:grid-cols-4'
        )
        
        # 安全写入：先写临时文件，再原子替换
        temp_file = list_file + '.tmp'
        with open(temp_file, 'w', encoding='utf-8') as f:
            f.write(list_html)
        
        os.replace(temp_file, list_file)
        print(f"✅ {page_type}列表页已更新: {len(report_cards)}篇报告")
        return True
    
    def _industry_chain_mapping(self, filename: str) -> tuple:
        """产业链报告类型映射"""
        filename_lower = filename.lower()
        if 'n1x' in filename_lower or '英伟达' in filename or 'computex' in filename_lower:
            return filename.replace('.html', '').replace('_', ' '), '🎮', 'COMPUTEX前瞻', 'bg-green-100 text-green-700'
        elif 'mlcc' in filename_lower:
            return filename.replace('.html', '').replace('_', ' '), '🧩', '终极深度', 'bg-red-50 text-red-600'
        elif '璇玑' in filename or '比亚迪' in filename:
            return filename.replace('.html', '').replace('_', ' '), '🚗', '产业链深度', 'bg-purple-100 text-purple-700'
        elif '存储' in filename or 'hbm' in filename_lower:
            return filename.replace('.html', '').replace('_', ' '), '💾', '存储芯片', 'bg-blue-100 text-blue-700'
        elif '先进封装' in filename:
            return filename.replace('.html', '').replace('_', ' '), '🔬', '先进封装', 'bg-cyan-100 text-cyan-700'
        else:
            return filename.replace('.html', '').replace('_', ' '), '📋', '深度研究', 'bg-gray-100 text-gray-700'
    
    def _daily_mapping(self, filename: str) -> tuple:
        """每日新闻映射"""
        return filename.replace('.html', '').replace('_', ' '), '📰', '新闻洞察', 'bg-indigo-100 text-indigo-700'
    
    def _simple_mapping(self, filename: str) -> tuple:
        """简单映射"""
        return filename.replace('.html', '').replace('_', ' '), '📊', '最新报告', 'bg-indigo-100 text-indigo-700'
    
    def _generate_list_page(self, title: str, subtitle: str, current_page: str, cards_html: str, grid_cols: str = 'grid-cols-2') -> str:
        """生成标准列表页 - 独立页面，与单篇报告完全分离"""
        return f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.5.1/css/all.min.css">
    <style>
        .glass-nav {{
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            border-bottom: 1px solid rgba(255, 255, 255, 0.2);
        }}
        
        body {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            font-family: -apple-system, BlinkMacSystemFont, 'PingFang SC', 'Helvetica Neue', sans-serif;
        }}
        
        .line-clamp-2 {{
            display: -webkit-box;
            -webkit-line-clamp: 2;
            -webkit-box-orient: vertical;
            overflow: hidden;
        }}
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
                <a href="/daily-news-insight/daily/latest.html" class="{'bg-white/20 text-white' if current_page == 'daily' else 'text-white/80 hover:text-white hover:bg-white/10'} text-sm transition-colors px-3 py-1.5 rounded-lg">日报</a>
                <a href="/daily-news-insight/intraday/latest.html" class="{'bg-white/20 text-white' if current_page == 'intraday' else 'text-white/80 hover:text-white hover:bg-white/10'} text-sm transition-colors px-3 py-1.5 rounded-lg">盘中</a>
                <a href="/daily-news-insight/aftermarket/latest.html" class="{'bg-white/20 text-white' if current_page == 'aftermarket' else 'text-white/80 hover:text-white hover:bg-white/10'} text-sm transition-colors px-3 py-1.5 rounded-lg">盘后</a>
                <a href="/daily-news-insight/industry_chain/latest.html" class="{'bg-white/20 text-white' if current_page == 'industry_chain' else 'text-white/80 hover:text-white hover:bg-white/10'} text-sm transition-colors px-3 py-1.5 rounded-lg">产业链</a>
                <a href="/daily-news-insight/weekly_review/latest.html" class="{'bg-white/20 text-white' if current_page == 'weekly_review' else 'text-white/80 hover:text-white hover:bg-white/10'} text-sm transition-colors px-3 py-1.5 rounded-lg">周复盘</a>
            </div>
        </div>
    </nav>

    <div class="pt-24 pb-8 px-4">
        <div class="max-w-5xl mx-auto text-center">
            <h1 class="text-3xl md:text-4xl font-black text-white mb-3 leading-tight">
                <i class="fa fa-book mr-2"></i>{title}
            </h1>
            <p class="text-white/80">{subtitle}</p>
        </div>
    </div>

    <div class="max-w-5xl mx-auto px-4 pb-20">
        <div class="bg-white/95 backdrop-blur-sm rounded-3xl shadow-2xl p-8">
            <h2 class="text-sm font-bold text-indigo-800 uppercase tracking-wider mb-6">
                <i class="fa fa-file-text-o mr-2"></i>报告列表 · 按时间倒序
            </h2>
            
            <div class="grid {grid_cols} gap-4">
                {cards_html}
            </div>
        </div>
    </div>

    <div class="text-center py-10 px-4">
        <div class="text-white/60 text-sm">
            <p class="mb-2">💡 投资研究中心 · 专业深度研究</p>
            <p class="text-xs text-white/40">数据仅供参考，不构成投资建议</p>
        </div>
    </div>
</body>
</html>'''


def main():
    docs_dir = '/app/data/所有对话/主对话/docs'
    updater = ListPageUpdater(docs_dir)
    
    if len(sys.argv) > 1:
        # 更新指定页面
        for page_type in sys.argv[1:]:
            updater.update_single(page_type)
    else:
        # 更新所有页面
        updater.update_all()


if __name__ == '__main__':
    main()
