"""
列表页生成器 - Pro版
基于Pro组件库重构，深色玻璃态风格
支持11个报告频道的列表页生成
"""
import sys
import os
import glob
import re
from datetime import datetime
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from components.pro import GlassCard, SectionTitle
from generators.pro_base import ProGenerator


# 频道配置
CHANNEL_CONFIGS = {
    'daily': {
        'title': '每日新闻洞察', 'nav_text': '日报',
        'patterns': [r'^\d{8}_每日新闻洞察.*\.html$'],
        'icon': '📰', 'tag': '每日洞察',
        'description': '隔夜新闻与当日操作策略',
    },
    'intraday': {
        'title': '盘中快报', 'nav_text': '盘中',
        'patterns': [r'^\d{8}_盘中快报.*\.html$'],
        'icon': '⚡', 'tag': '盘中快报',
        'description': '盘中异动与实时机会跟踪',
    },
    'aftermarket': {
        'title': '盘后速递', 'nav_text': '盘后',
        'patterns': [r'^\d{8}_盘后速递.*\.html$'],
        'icon': '📊', 'tag': '盘后速递',
        'description': '收盘后热点复盘与机会挖掘',
    },
    'industry_chain': {
        'title': '产业链总览', 'nav_text': '产业链',
        'patterns': [r'^\d{8}_.*产业链.*\.html$', r'^\d{8}_.*深度研究.*\.html$'],
        'icon': '🔬', 'tag': '深度研究',
        'description': '产业链深度研究与投资机会分析',
    },
    'weekly_review': {
        'title': '周复盘', 'nav_text': '周复盘',
        'patterns': [r'^\d{8}_周复盘.*\.html$'],
        'icon': '📋', 'tag': '周度复盘',
        'description': '每周行情回顾与经验总结',
    },
    'weekly_outlook': {
        'title': '周三前瞻', 'nav_text': '周三前瞻',
        'patterns': [r'^\d{8}_周三前瞻.*\.html$'],
        'icon': '🔮', 'tag': '前瞻分析',
        'description': '下周行情前瞻与策略预判',
    },
    's级催化扫描': {
        'title': 'S级催化扫描', 'nav_text': 'S级催化',
        'patterns': [r'^\d{8}_.*[Ss]级催化.*\.html$'],
        'icon': '🚀', 'tag': 'S级催化',
        'description': '超级催化剂深度扫描与机会分析',
    },
    '周末速递': {
        'title': '周末速递', 'nav_text': '周末速递',
        'patterns': [r'^\d{8}_周末速递.*\.html$'],
        'icon': '📦', 'tag': '周末速递',
        'description': '周末重要资讯与下周投资机会',
    },
    '明日催化剂': {
        'title': '明日催化剂', 'nav_text': '明日催化',
        'patterns': [r'^\d{8}_明日催化剂.*\.html$'],
        'icon': '💡', 'tag': '明日催化',
        'description': '明日重要事件与催化机会预判',
    },
    'monthly': {
        'title': '月度总结', 'nav_text': '月报',
        'patterns': [r'^\d{8}_.*月报.*\.html$', r'^\d{6}_.*月报.*\.html$'],
        'icon': '🗓️', 'tag': '月度报告',
        'description': '月度行情总结与下月展望',
    },
    '题材健康度报告': {
        'title': '题材健康度', 'nav_text': '题材健康度',
        'patterns': [r'^\d{8}_.*题材.*\.html$', r'^health_report_\d{8}\.html$'],
        'icon': '💚', 'tag': '题材分析',
        'description': '市场题材热度与健康度分析',
    },
}


class ListPageProGenerator(ProGenerator):
    """列表页 - Pro版生成器
    
    为每个报告频道生成统一风格的列表页
    遵循卡片套卡片设计原则、深色玻璃态风格
    """
    
    data_type = "list"
    
    def __init__(self, 
                 channel_key: str,
                 docs_dir: str = "docs",
                 data_dir: str = "data"):
        """
        Args:
            channel_key: 频道键名，如 'daily', 'weekly_review'
            docs_dir: 文档根目录路径
            data_dir: 数据目录路径
        """
        if channel_key not in CHANNEL_CONFIGS:
            raise ValueError(f"未知频道: {channel_key}")
        
        self.channel_key = channel_key
        self.config = CHANNEL_CONFIGS[channel_key]
        self.docs_dir = Path(docs_dir).resolve()
        
        super().__init__(
            title=f"{self.config['title']} · 报告列表",
            active_page=self.config['nav_text'],
            footer_text=f"{self.config['title']} · 投资研究中心",
            data_dir=data_dir,
            show_toc=False,
        )
    
    def _scan_report_files(self):
        """扫描目录下的报告文件"""
        dir_path = self.docs_dir / self.channel_key
        if not dir_path.exists():
            return []
        
        all_files = []
        seen_files = set()  # 去重集合
        for pattern in self.config['patterns']:
            regex = re.compile(pattern)
            for f in dir_path.iterdir():
                if f.is_file() and regex.match(f.name) and f.name != 'latest.html':
                    # 去重：同一个文件只添加一次
                    if f.name in seen_files:
                        continue
                    seen_files.add(f.name)
                    
                    # 尝试从文件名提取日期
                    date_match = re.search(r'(\d{8})', f.name)
                    date_str = date_match.group(1) if date_match else ''
                    
                    all_files.append({
                        'name': f.stem,
                        'filename': f.name,
                        'path': str(f),
                        'date': date_str,
                        'size': f.stat().st_size,
                    })
        
        # 按日期倒序排列
        all_files.sort(key=lambda x: x['date'], reverse=True)
        return all_files
    
    def _generate_report_cards(self, files):
        """生成报告卡片网格 - 内层小卡片"""
        if not files:
            return '''
            <div class="text-center py-12 text-white/50">
                <div class="text-4xl mb-4">📭</div>
                <p>暂无报告</p>
            </div>
            '''
        
        cards_html = ''
        for idx, file_info in enumerate(files):
            filename = file_info['filename']
            date_str = file_info['date']
            name = file_info['name']
            
            # 格式化日期显示
            if len(date_str) == 8:
                display_date = f"{date_str[:4]}-{date_str[4:6]}-{date_str[6:8]}"
            else:
                display_date = date_str or '未知日期'
            
            # 提取标题（去掉日期前缀）
            title = re.sub(r'^\d{8}_', '', name)
            if len(title) > 20:
                title = title[:20] + '...'
            
            cards_html += f'''
            <a href="{filename}" class="group block bg-white/5 hover:bg-white/10 border border-white/10 rounded-xl p-4 transition-all duration-300 hover:scale-105 hover:shadow-lg" style="animation-delay: {idx * 0.05}s">
                <div class="text-2xl mb-3">{self.config['icon']}</div>
                <h3 class="font-semibold text-white text-sm mb-2 line-clamp-2 h-10">{title}</h3>
                <div class="flex items-center justify-between text-xs text-white/50">
                    <span>{display_date}</span>
                    <span class="px-2 py-0.5 bg-white/10 rounded-full">{self.config['tag']}</span>
                </div>
            </a>
            '''
        
        return cards_html
    
    def _generate_header(self) -> str:
        """生成页面头部"""
        return f'''
        <div class="text-center mb-10">
            <div class="inline-flex items-center gap-2 px-4 py-1 bg-white/10 rounded-full text-xs text-white/60 mb-4">
                <span>📂</span>
                <span>报告归档</span>
            </div>
            <h1 class="text-3xl md:text-4xl font-black text-white mb-3">
                {self.config["icon"]} {self.config["title"]}
            </h1>
            <p class="text-white/70">{self.config["description"]}</p>
            <div class="mt-4">
                <span class="inline-block px-4 py-1 bg-white/10 rounded-full text-sm text-white/70">
                    共 {len(self._files)} 份报告 · 按时间倒序
                </span>
            </div>
        </div>
        '''
    
    def _generate_list_section(self) -> str:
        """生成列表区域 - 卡片套卡片结构"""
        cards_html = self._generate_report_cards(self._files)
        
        content = f'''
            <div class="flex items-center justify-between mb-6">
                <h2 class="text-sm font-bold text-white/80 uppercase tracking-wider flex items-center">
                    <i class="fa fa-file-text-o mr-2"></i>报告列表 · 按时间倒序
                </h2>
                <span class="text-xs text-white/40">Pro v3.5</span>
            </div>
            <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">
                {cards_html}
            </div>
        '''
        
        # 外层大卡片包裹内层小卡片网格 - 卡片套卡片
        return GlassCard(
            content=content, 
            padding="p-6 md:p-8", 
            extra_class="mb-6"
        ).render()
    
    def load_data(self):
        """加载数据"""
        super().load_data()
        self._files = self._scan_report_files()
    
    def _content(self) -> str:
        """页面主要内容"""
        return f'''
        <div class="max-w-6xl mx-auto">
            {self._generate_header()}
            {self._generate_list_section()}
        </div>
        '''
    
    def publish(self, output_path: str = None) -> dict:
        """发布页面
        
        Args:
            output_path: 输出路径，默认保存到对应频道的 latest.html
        """
        if output_path is None:
            output_path = str(self.docs_dir / self.channel_key / 'latest.html')
        
        result = super().publish(output_path)
        result['channel'] = self.channel_key
        result['file_count'] = len(self._files)
        return result


def generate_all_list_pages(docs_dir: str = "docs") -> dict:
    """生成所有频道的列表页
    
    Args:
        docs_dir: 文档根目录
        
    Returns:
        生成结果统计
    """
    results = {
        'success': [],
        'failed': [],
        'total': len(CHANNEL_CONFIGS),
    }
    
    for channel_key in CHANNEL_CONFIGS:
        try:
            generator = ListPageProGenerator(channel_key, docs_dir=docs_dir)
            result = generator.publish()
            results['success'].append({
                'channel': channel_key,
                'title': CHANNEL_CONFIGS[channel_key]['title'],
                'file_count': result['file_count'],
            })
            print(f"✅ {CHANNEL_CONFIGS[channel_key]['title']} → {result['file_count']} 份报告")
        except Exception as e:
            results['failed'].append({
                'channel': channel_key,
                'error': str(e),
            })
            print(f"❌ {channel_key}: {e}")
    
    print(f"\n🎉 完成！成功 {len(results['success'])}/{results['total']} 个频道")
    return results


if __name__ == "__main__":
    # 默认生成所有列表页
    docs_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '..', 'docs')
    docs_dir = os.path.abspath(docs_dir)
    
    if len(sys.argv) > 1:
        channel = sys.argv[1]
        if channel in CHANNEL_CONFIGS:
            generator = ListPageProGenerator(channel, docs_dir=docs_dir)
            result = generator.publish()
            print(f"\n✅ 生成完成: {result['output_path']}")
            print(f"   报告数量: {result['file_count']}")
        else:
            print(f"❌ 未知频道: {channel}")
            print(f"可用频道: {', '.join(CHANNEL_CONFIGS.keys())}")
    else:
        generate_all_list_pages(docs_dir=docs_dir)
