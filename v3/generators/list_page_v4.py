"""
V4 列表页生成器
基于 V4BaseGenerator，实现三级导航架构：首页 → 列表页 → 详情页
每个报告频道都有对应的列表页，展示历史报告列表
"""
import sys
import os
import glob
import re
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Optional

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from generators.v4_base import V4BaseGenerator


# 频道配置 - 统一管理所有报告频道
CHANNEL_CONFIGS = {
    'daily': {
        'title': '每日日报',
        'nav_text': '日报',
        'icon': '📰',
        'description': '每日市场复盘与操作策略',
        'tag': '每日洞察',
        'list_file_pattern': r'^\d{8}_daily_report.*\.html$',
        'detail_url_prefix': 'daily_report_v4',
        'latest_file': 'daily_report_v4.html',
    },
    'intraday': {
        'title': '盘中快报',
        'nav_text': '盘中',
        'icon': '⚡',
        'description': '盘中异动与实时机会跟踪',
        'tag': '实时追踪',
        'list_file_pattern': r'^\d{8}_intraday_report.*\.html$',
        'detail_url_prefix': 'intraday_report_v4',
        'latest_file': 'intraday_report_v4.html',
    },
    'aftermarket': {
        'title': '盘后速递',
        'nav_text': '盘后',
        'icon': '📊',
        'description': '收盘数据总结与热点复盘',
        'tag': '盘后总结',
        'list_file_pattern': r'^\d{8}_aftermarket.*\.html$',
        'detail_url_prefix': 'aftermarket_report_v4',
        'latest_file': 'aftermarket_report_v4.html',
    },
    's_catalyst': {
        'title': 'S级催化扫描',
        'nav_text': 'S级催化',
        'icon': '🚀',
        'description': '超级催化剂深度扫描与机会分析',
        'tag': '顶级题材',
        'list_file_pattern': r'^\d{8}_s_level_catalyst.*\.html$',
        'detail_url_prefix': 's_level_catalyst_v4',
        'latest_file': 's_level_catalyst_v4.html',
    },
    'sector_heatmap': {
        'title': '板块热度分析',
        'nav_text': '板块热度',
        'icon': '🔥',
        'description': '行业轮动把握与热点板块分析',
        'tag': '板块分析',
        'list_file_pattern': r'^\d{8}_sector_heatmap.*\.html$',
        'detail_url_prefix': 'sector_heatmap_v4',
        'latest_file': 'sector_heatmap_v4.html',
    },
    'tomorrow_catalyst': {
        'title': '明日催化剂',
        'nav_text': '明日催化',
        'icon': '⏰',
        'description': '明日重要事件与催化机会预判',
        'tag': '前瞻预判',
        'list_file_pattern': r'^\d{8}_tomorrow_catalyst.*\.html$',
        'detail_url_prefix': 'tomorrow_catalyst_v4',
        'latest_file': 'tomorrow_catalyst_v4.html',
    },
    'weekend_express': {
        'title': '周末速递',
        'nav_text': '周末速递',
        'icon': '📦',
        'description': '周末重要资讯与下周投资机会',
        'tag': '周度策略',
        'list_file_pattern': r'^\d{8}_weekend_express.*\.html$',
        'detail_url_prefix': 'weekend_express_v4',
        'latest_file': 'weekend_express_v4.html',
    },
    'weekly_outlook': {
        'title': '周三前瞻',
        'nav_text': '周三前瞻',
        'icon': '👁️',
        'description': '周中行情展望与策略调整建议',
        'tag': '周中展望',
        'list_file_pattern': r'^\d{8}_weekly_outlook.*\.html$',
        'detail_url_prefix': 'weekly_outlook_v4',
        'latest_file': 'weekly_outlook_v4.html',
    },
    'weekly_review': {
        'title': '周复盘',
        'nav_text': '周复盘',
        'icon': '📋',
        'description': '每周行情回顾与经验教训总结',
        'tag': '复盘总结',
        'list_file_pattern': r'^\d{8}_weekly_review.*\.html$',
        'detail_url_prefix': 'weekly_review_v4',
        'latest_file': 'weekly_review_v4.html',
    },
    'longhubang': {
        'title': '龙虎榜分析',
        'nav_text': '龙虎榜',
        'icon': '🏆',
        'description': '龙虎榜数据解读与游资动向追踪',
        'tag': '资金动向',
        'list_file_pattern': r'^\d{8}_longhubang.*\.html$',
        'detail_url_prefix': 'longhubang_v4',
        'latest_file': 'longhubang_v4.html',
    },
    'prediction_center': {
        'title': '预测中心',
        'nav_text': '预测',
        'icon': '🔮',
        'description': 'AI智能预测与历史验证',
        'tag': '智能预测',
        'list_file_pattern': r'^\d{8}_prediction.*\.html$',
        'detail_url_prefix': 'prediction_center_v4',
        'latest_file': 'prediction_center_v4.html',
    },
    'alert_system': {
        'title': '智能预警系统',
        'nav_text': '预警',
        'icon': '🚨',
        'description': '实时风险监控与智能预警提醒',
        'tag': '风险监控',
        'list_file_pattern': r'^\d{8}_alert.*\.html$',
        'detail_url_prefix': 'alert_system_v4',
        'latest_file': 'alert_system_v4.html',
    },
    'portfolio_dashboard': {
        'title': '持仓仪表盘',
        'nav_text': '持仓',
        'icon': '📊',
        'description': '多维持仓诊断与收益分析',
        'tag': '持仓管理',
        'list_file_pattern': r'^\d{8}_portfolio.*\.html$',
        'detail_url_prefix': 'portfolio_dashboard_v4',
        'latest_file': 'portfolio_dashboard_v4.html',
    },
}


class ListPageV4Generator(V4BaseGenerator):
    """V4列表页生成器
    
    为每个报告频道生成统一风格的列表页
    遵循V4设计规范：白色卡片 + 紫色背景 + 深色文字
    """
    
    def __init__(self, 
                 channel_key: str,
                 docs_dir: str = None,
                 data_dir: str = "data"):
        """
        Args:
            channel_key: 频道键名，对应 CHANNEL_CONFIGS 中的 key
            docs_dir: 文档目录路径，用于扫描历史报告
            data_dir: 数据目录路径
        """
        super().__init__(data_dir)
        
        if channel_key not in CHANNEL_CONFIGS:
            raise ValueError(f"未知频道: {channel_key}")
        
        self.channel_key = channel_key
        self.config = CHANNEL_CONFIGS[channel_key]
        
        # 设置页面标题和导航
        self.page_title = f"{self.config['icon']} {self.config['title']}"
        self.page_subtitle = self.config['description']
        self.active_nav_key = channel_key
        
        # TOC目录
        self.toc_items = [
            ("最新报告", "section-latest"),
            ("历史报告", "section-history"),
            ("频道说明", "section-about"),
        ]
        
        # 文档目录
        if docs_dir is None:
            self.docs_dir = Path(__file__).parent.parent.parent / 'docs'
        else:
            self.docs_dir = Path(docs_dir)
    
    def _scan_history_reports(self) -> List[Dict]:
        """扫描历史报告文件
        
        Returns:
            报告列表，每项包含 filename, date, title 等信息
        """
        pattern = re.compile(self.config['list_file_pattern'])
        reports = []
        
        # 扫描docs目录下的所有文件
        if self.docs_dir.exists():
            for f in self.docs_dir.iterdir():
                if f.is_file() and pattern.match(f.name):
                    # 从文件名提取日期
                    date_match = re.search(r'(\d{8})', f.name)
                    date_str = date_match.group(1) if date_match else ''
                    
                    # 格式化日期显示
                    if len(date_str) == 8:
                        display_date = f"{date_str[:4]}-{date_str[4:6]}-{date_str[6:8]}"
                    else:
                        display_date = '未知日期'
                    
                    # 提取标题（去掉日期前缀和_v4.html后缀）
                    title = re.sub(r'^\d{8}_', '', f.stem)
                    title = title.replace('_v4', '').replace('_', ' ')
                    if not title:
                        title = self.config['title']
                    
                    reports.append({
                        'filename': f.name,
                        'path': str(f),
                        'date_str': date_str,
                        'display_date': display_date,
                        'title': title,
                        'size': f.stat().st_size,
                    })
        
        # 按日期倒序排列
        reports.sort(key=lambda x: x['date_str'], reverse=True)
        return reports
    
    def render_latest_report(self) -> str:
        """渲染最新报告区域（高亮大卡片）"""
        reports = self._scan_history_reports()
        
        if not reports:
            # 没有历史报告时，显示占位
            return f'''
            <section class="v4-section" id="section-latest">
                {self.render_section_header("✨ 最新报告", "本期", "v4-tag-blue")}
                <div class="v4-card v4-latest-empty">
                    <div class="v4-empty-icon">📭</div>
                    <h3>暂无报告</h3>
                    <p>该频道的第一份报告即将发布，敬请期待</p>
                </div>
            </section>
            '''
        
        latest = reports[0]
        
        return f'''
        <section class="v4-section" id="section-latest">
            {self.render_section_header("✨ 最新报告", "本期", "v4-tag-blue")}
            <a href="{latest['filename']}" class="v4-latest-card v4-card">
                <div class="v4-latest-badge">
                    <span class="v4-tag v4-tag-purple">最新发布</span>
                    <span class="v4-latest-date">{latest['display_date']}</span>
                </div>
                <h2 class="v4-latest-title">{latest['title']}</h2>
                <p class="v4-latest-desc">{self.config['description']}</p>
                <div class="v4-latest-footer">
                    <span class="v4-latest-tag">{self.config['tag']}</span>
                    <span class="v4-latest-read">立即阅读 →</span>
                </div>
            </a>
        </section>
        '''
    
    def render_history_list(self) -> str:
        """渲染历史报告列表（卡片网格）"""
        reports = self._scan_history_reports()
        history_reports = reports[1:] if len(reports) > 1 else []
        
        if not history_reports:
            return f'''
            <section class="v4-section" id="section-history">
                {self.render_section_header("📚 历史报告", f"共 {len(reports)} 期", "v4-tag-gray")}
                <div class="v4-card v4-history-empty">
                    <p>暂无更多历史报告</p>
                </div>
            </section>
            '''
        
        cards_html = ""
        for report in history_reports:
            cards_html += f'''
            <a href="{report['filename']}" class="v4-history-card">
                <div class="v4-history-icon">{self.config['icon']}</div>
                <div class="v4-history-content">
                    <h3 class="v4-history-title">{report['title']}</h3>
                    <div class="v4-history-meta">
                        <span class="v4-history-date">📅 {report['display_date']}</span>
                        <span class="v4-tag v4-tag-gray">{self.config['tag']}</span>
                    </div>
                </div>
                <div class="v4-history-arrow">→</div>
            </a>
            '''
        
        return f'''
        <section class="v4-section" id="section-history">
            {self.render_section_header("📚 历史报告", f"共 {len(reports)} 期", "v4-tag-gray")}
            <div class="v4-history-grid">
                {cards_html}
            </div>
        </section>
        '''
    
    def render_channel_about(self) -> str:
        """渲染频道说明区域"""
        return f'''
        <section class="v4-section" id="section-about">
            {self.render_section_header("ℹ️ 频道说明", "关于", "v4-tag-gray")}
            <div class="v4-card">
                <div class="v4-about-content">
                    <div class="v4-about-icon">{self.config['icon']}</div>
                    <div class="v4-about-text">
                        <h3>{self.config['title']}</h3>
                        <p>{self.config['description']}</p>
                        <div class="v4-about-features">
                            <div class="v4-about-feature">
                                <span class="feature-icon">📊</span>
                                <span>数据驱动</span>
                            </div>
                            <div class="v4-about-feature">
                                <span class="feature-icon">🤖</span>
                                <span>AI分析</span>
                            </div>
                            <div class="v4-about-feature">
                                <span class="feature-icon">⚡</span>
                                <span>及时更新</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        '''
    
    def render_content(self) -> str:
        """渲染页面主体内容"""
        # 页面头部
        page_header = f'''
        <div class="v4-page-header">
            <h1>{self.page_title}</h1>
            <p class="v4-page-subtitle">{self.page_subtitle}</p>
            <div class="v4-page-stats">
                <div class="v4-page-stat">
                    <span class="stat-value">{len(self._scan_history_reports())}</span>
                    <span class="stat-label">期报告</span>
                </div>
                <div class="v4-page-stat">
                    <span class="stat-value">{self.config['tag']}</span>
                    <span class="stat-label">内容类型</span>
                </div>
            </div>
        </div>
        '''
        
        latest_section = self.render_latest_report()
        history_section = self.render_history_list()
        about_section = self.render_channel_about()
        
        return f'''
        {page_header}
        {latest_section}
        {history_section}
        {about_section}
        '''
    
    def get_page_css(self) -> str:
        """页面特有CSS"""
        return '''
        /* 页面头部 */
        .v4-page-header {
            text-align: center;
            padding: 60px 20px 40px;
        }
        .v4-page-header h1 {
            font-size: 36px;
            font-weight: 800;
            color: #FFFFFF;
            margin: 0 0 12px 0;
            text-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }
        .v4-page-subtitle {
            font-size: 16px;
            color: rgba(255, 255, 255, 0.85);
            margin: 0 0 24px 0;
        }
        .v4-page-stats {
            display: flex;
            justify-content: center;
            gap: 40px;
            flex-wrap: wrap;
        }
        .v4-page-stat {
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 4px;
        }
        .v4-page-stat .stat-value {
            font-size: 24px;
            font-weight: 700;
            color: #FFFFFF;
        }
        .v4-page-stat .stat-label {
            font-size: 13px;
            color: rgba(255, 255, 255, 0.7);
        }
        
        /* 最新报告卡片 */
        .v4-latest-card {
            display: block;
            padding: 32px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            border-radius: 20px;
            color: white;
            text-decoration: none;
            transition: all 0.3s ease;
            box-shadow: 0 10px 40px rgba(102, 126, 234, 0.3);
            position: relative;
            overflow: hidden;
        }
        .v4-latest-card::before {
            content: '';
            position: absolute;
            top: -50%;
            right: -20%;
            width: 300px;
            height: 300px;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 50%;
        }
        .v4-latest-card:hover {
            transform: translateY(-4px);
            box-shadow: 0 20px 60px rgba(102, 126, 234, 0.4);
        }
        .v4-latest-badge {
            display: flex;
            align-items: center;
            gap: 12px;
            margin-bottom: 16px;
            position: relative;
            z-index: 1;
        }
        .v4-latest-badge .v4-tag {
            background: rgba(255, 255, 255, 0.2);
            color: white;
            border: 1px solid rgba(255, 255, 255, 0.3);
        }
        .v4-latest-date {
            font-size: 13px;
            color: rgba(255, 255, 255, 0.8);
        }
        .v4-latest-title {
            font-size: 28px;
            font-weight: 700;
            margin: 0 0 12px 0;
            position: relative;
            z-index: 1;
        }
        .v4-latest-desc {
            font-size: 15px;
            opacity: 0.9;
            margin: 0 0 24px 0;
            position: relative;
            z-index: 1;
        }
        .v4-latest-footer {
            display: flex;
            justify-content: space-between;
            align-items: center;
            position: relative;
            z-index: 1;
        }
        .v4-latest-tag {
            padding: 6px 14px;
            background: rgba(255, 255, 255, 0.15);
            border-radius: 20px;
            font-size: 12px;
            font-weight: 500;
        }
        .v4-latest-read {
            font-size: 14px;
            font-weight: 600;
        }
        
        /* 空状态 */
        .v4-latest-empty, .v4-history-empty {
            text-align: center;
            padding: 60px 20px;
            color: #64748B;
        }
        .v4-empty-icon {
            font-size: 48px;
            margin-bottom: 16px;
        }
        .v4-latest-empty h3, .v4-history-empty p {
            margin: 0 0 8px 0;
            color: #1E293B;
        }
        
        /* 历史报告网格 */
        .v4-history-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
            gap: 16px;
        }
        .v4-history-card {
            display: flex;
            align-items: center;
            gap: 16px;
            padding: 20px;
            background: #FFFFFF;
            border-radius: 16px;
            text-decoration: none;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
            border: 1px solid #E2E8F0;
            transition: all 0.3s ease;
        }
        .v4-history-card:hover {
            transform: translateY(-2px);
            box-shadow: 0 12px 28px rgba(102, 126, 234, 0.15);
            border-color: rgba(102, 126, 234, 0.3);
        }
        .v4-history-icon {
            width: 48px;
            height: 48px;
            border-radius: 12px;
            background: linear-gradient(135deg, #667eea15, #764ba215);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 24px;
            flex-shrink: 0;
        }
        .v4-history-content {
            flex: 1;
            min-width: 0;
        }
        .v4-history-title {
            font-size: 15px;
            font-weight: 600;
            color: #1E293B;
            margin: 0 0 8px 0;
            line-height: 1.4;
            overflow: hidden;
            text-overflow: ellipsis;
            display: -webkit-box;
            -webkit-line-clamp: 2;
            -webkit-box-orient: vertical;
        }
        .v4-history-meta {
            display: flex;
            align-items: center;
            gap: 10px;
            flex-wrap: wrap;
        }
        .v4-history-date {
            font-size: 12px;
            color: #64748B;
        }
        .v4-history-arrow {
            font-size: 18px;
            color: #94A3B8;
            flex-shrink: 0;
            transition: transform 0.2s;
        }
        .v4-history-card:hover .v4-history-arrow {
            transform: translateX(4px);
            color: #667eea;
        }
        
        /* 频道说明 */
        .v4-about-content {
            display: flex;
            gap: 24px;
            align-items: flex-start;
        }
        .v4-about-icon {
            width: 64px;
            height: 64px;
            border-radius: 16px;
            background: linear-gradient(135deg, #667eea15, #764ba215);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 32px;
            flex-shrink: 0;
        }
        .v4-about-text {
            flex: 1;
        }
        .v4-about-text h3 {
            font-size: 18px;
            font-weight: 700;
            color: #1E293B;
            margin: 0 0 8px 0;
        }
        .v4-about-text p {
            font-size: 14px;
            color: #64748B;
            line-height: 1.6;
            margin: 0 0 16px 0;
        }
        .v4-about-features {
            display: flex;
            gap: 24px;
            flex-wrap: wrap;
        }
        .v4-about-feature {
            display: flex;
            align-items: center;
            gap: 8px;
            font-size: 13px;
            color: #475569;
        }
        .v4-about-feature .feature-icon {
            font-size: 16px;
        }
        
        /* 响应式适配 */
        @media (max-width: 768px) {
            .v4-page-header h1 {
                font-size: 28px;
            }
            .v4-page-stats {
                gap: 24px;
            }
            .v4-latest-title {
                font-size: 22px;
            }
            .v4-history-grid {
                grid-template-columns: 1fr;
            }
            .v4-about-content {
                flex-direction: column;
            }
        }
        '''


def generate_all_list_pages(docs_dir: str = None) -> Dict:
    """生成所有频道的列表页
    
    Args:
        docs_dir: 文档目录路径
        
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
            generator = ListPageV4Generator(channel_key, docs_dir=docs_dir)
            html = generator.generate()
            
            # 输出文件名：list_<channel>_v4.html
            output_filename = f"list_{channel_key}_v4.html"
            output_path = generator.docs_dir / output_filename
            
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(html)
            
            results['success'].append({
                'channel': channel_key,
                'title': CHANNEL_CONFIGS[channel_key]['title'],
                'output_file': output_filename,
            })
            print(f"✅ {CHANNEL_CONFIGS[channel_key]['title']} → {output_filename}")
        except Exception as e:
            results['failed'].append({
                'channel': channel_key,
                'error': str(e),
            })
            print(f"❌ {channel_key}: {e}")
            import traceback
            traceback.print_exc()
    
    print(f"\n🎉 完成！成功 {len(results['success'])}/{results['total']} 个频道")
    return results


if __name__ == "__main__":
    # 默认生成所有列表页
    if len(sys.argv) > 1:
        # 生成指定频道的列表页
        channel = sys.argv[1]
        generator = ListPageV4Generator(channel)
        html = generator.generate()
        output_path = generator.docs_dir / f"list_{channel}_v4.html"
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"✅ 已生成: {output_path}")
    else:
        # 生成所有频道
        generate_all_list_pages()
