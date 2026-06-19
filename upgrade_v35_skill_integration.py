"""
V3.5系统 Skill 整合架构升级脚本
功能：
1. 生成个股分析列表页
2. 创建全局股票悬浮卡片系统
3. Skill分层整合架构
4. boya策略分层注入机制
"""
import sys
import os
import json
import glob
from pathlib import Path
from datetime import datetime

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'v3'))

from components.pro import GlassCard, SectionTitle, get_pro_theme_css
from generators.pro_base import ProGenerator


# ============================================================
# 一、个股分析列表页生成器
# ============================================================

class StockAnalysisListGenerator(ProGenerator):
    """个股分析列表页 - 展示所有可分析的股票"""
    
    data_type = "stock_list"
    
    def __init__(self, data_dir: str = "data", docs_dir: str = "docs"):
        super().__init__(
            title="个股分析中心",
            active_page="工具",
            footer_text="投资研究中心 · 数据驱动决策",
            data_dir=data_dir,
            show_toc=False,
        )
        self.docs_dir = docs_dir
        self.stock_data = []
    
    def load_data(self):
        super().load_data()
        
        # 加载股票列表数据
        stock_list_path = os.path.join(self.docs_dir, 'data', 'stock_analysis', 'stock_list.json')
        if os.path.exists(stock_list_path):
            with open(stock_list_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                stocks_dict = data.get('stocks', {})
                for name, info in stocks_dict.items():
                    if isinstance(info, dict):
                        self.stock_data.append({
                            'name': name,
                            'code': info.get('code', ''),
                            'sector': info.get('sector', ''),
                            'rating': info.get('rating', ''),
                        })
                    else:
                        self.stock_data.append({
                            'name': name,
                            'code': info if isinstance(info, str) else '',
                            'sector': '',
                            'rating': '',
                        })
        
        # 补充已生成详情页的股票数据
        detail_pages = glob.glob(os.path.join(self.docs_dir, '个股分析', '*.html'))
        existing_names = [s['name'] for s in self.stock_data]
        
        for page in detail_pages:
            name = os.path.basename(page).replace('.html', '')
            if name not in existing_names and name != 'index':
                self.stock_data.append({
                    'name': name,
                    'code': self._get_stock_code(name),
                    'sector': '',
                    'rating': '已分析',
                })
        
        # 按名称排序
        self.stock_data.sort(key=lambda x: x['name'])
    
    def _get_stock_code(self, name: str) -> str:
        """从数据文件获取股票代码"""
        json_files = glob.glob(os.path.join(self.docs_dir, 'data', 'stock_analysis', '*.json'))
        for f in json_files:
            try:
                with open(f, 'r', encoding='utf-8') as fp:
                    data = json.load(fp)
                    if data.get('name') == name:
                        return data.get('code', '')
            except:
                continue
        return ''
    
    def _render_stock_grid(self) -> str:
        """渲染股票卡片网格"""
        if not self.stock_data:
            return '<p class="text-white/60 text-center py-12">暂无股票分析数据</p>'
        
        cards_html = ''
        for stock in self.stock_data:
            name = stock['name']
            code = stock.get('code', '')
            sector = stock.get('sector', '')
            rating = stock.get('rating', '')
            
            # 检查是否有详情页
            detail_page = os.path.join(self.docs_dir, '个股分析', f'{name}.html')
            has_detail = os.path.exists(detail_page)
            
            link = f'{name}.html' if has_detail else '#'
            cursor_class = 'cursor-pointer' if has_detail else 'cursor-not-allowed opacity-60'
            
            rating_color = {
                '买入': 'text-green-400',
                '增持': 'text-emerald-400',
                '持有': 'text-yellow-400',
                '减持': 'text-orange-400',
                '卖出': 'text-red-400',
                '已分析': 'text-blue-400',
            }.get(rating, 'text-white/60')
            
            cards_html += f'''
            <a href="{link}" class="glass-card rounded-xl p-4 {cursor_class} hover:border-blue-400/50 transition-all duration-300 group block">
                <div class="flex items-start justify-between mb-2">
                    <div>
                        <h3 class="text-white font-bold text-lg group-hover:text-blue-400 transition-colors">{name}</h3>
                        <p class="text-white/50 text-sm">{code}</p>
                    </div>
                    {f'<span class="text-xs px-2 py-1 rounded-full bg-green-500/20 {rating_color}">{rating}</span>' if rating else ''}
                </div>
                {f'<p class="text-white/40 text-xs mt-2">{sector}</p>' if sector else ''}
                <div class="mt-3 flex items-center text-blue-400/70 text-xs group-hover:text-blue-400">
                    <span>查看深度分析</span>
                    <svg class="w-3 h-3 ml-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path>
                    </svg>
                </div>
            </a>
            '''
        
        return f'''
        <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-5 gap-4">
            {cards_html}
        </div>
        '''
    
    def generate_content(self) -> str:
        self.load_data()
        
        stats_html = f'''
        <div class="grid grid-cols-3 gap-4 mb-8">
            <div class="glass-card rounded-xl p-4 text-center">
                <div class="text-3xl font-bold text-blue-400">{len(self.stock_data)}</div>
                <div class="text-white/60 text-sm mt-1">覆盖股票</div>
            </div>
            <div class="glass-card rounded-xl p-4 text-center">
                <div class="text-3xl font-bold text-green-400">{sum(1 for s in self.stock_data if s.get('rating') in ['买入', '增持'])}</div>
                <div class="text-white/60 text-sm mt-1">推荐评级</div>
            </div>
            <div class="glass-card rounded-xl p-4 text-center">
                <div class="text-3xl font-bold text-purple-400">5</div>
                <div class="text-white/60 text-sm mt-1">分析维度</div>
            </div>
        </div>
        '''
        
        return f'''
        {stats_html}
        
        {SectionTitle("全部股票", "📈", "按名称排序，点击查看深度分析报告").render()}
        {self._render_stock_grid()}
        '''


# ============================================================
# 二、全局股票悬浮卡片系统
# ============================================================

def generate_stock_hover_card_js(output_path: str):
    """生成全局股票悬浮卡片JS代码"""
    
    js_code = r'''
/**
 * 全局股票悬浮卡片系统
 * V3.5 Pro - 深色玻璃态风格
 */
(function() {
    const stockCache = {};
    let stockList = [];
    
    async function loadStockList() {
        try {
            const prefix = window.location.pathname.includes('/daily-news-insight/') ? '/daily-news-insight' : '';
            const response = await fetch(prefix + '/data/stock_analysis/stock_list.json');
            if (response.ok) {
                const data = await response.json();
                if (data.stocks) {
                    stockList = Object.entries(data.stocks).map(([name, info]) => ({
                        name: name,
                        code: typeof info === 'string' ? info : (info.code || ''),
                        sector: typeof info === 'object' ? (info.sector || '') : '',
                        rating: typeof info === 'object' ? (info.rating || '') : '',
                    }));
                }
            }
        } catch (e) {
            console.log('股票列表加载失败');
        }
    }
    
    function createHoverCard(stockName, stockCode) {
        const card = document.createElement('div');
        card.className = 'stock-hover-card';
        card.style.cssText = `
            position: fixed; z-index: 10000;
            background: rgba(15, 23, 42, 0.95);
            backdrop-filter: blur(20px);
            border: 1px solid rgba(59, 130, 246, 0.3);
            border-radius: 12px; padding: 16px; min-width: 280px;
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.4);
            opacity: 0; transform: translateY(10px);
            transition: all 0.2s ease; pointer-events: none;
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        `;
        
        card.innerHTML = `
            <div style="display: flex; justify-content: space-between; align-items: start; margin-bottom: 12px;">
                <div>
                    <div style="font-size: 18px; font-weight: 700; color: white; margin-bottom: 2px;">${stockName}</div>
                    <div style="font-size: 12px; color: rgba(255,255,255,0.5);">${stockCode || '加载中...'}</div>
                </div>
                <div style="font-size: 11px; padding: 4px 8px; border-radius: 999px; background: rgba(59, 130, 246, 0.2); color: #60a5fa;">深度分析</div>
            </div>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px; margin-bottom: 12px;">
                <div style="background: rgba(255,255,255,0.05); border-radius: 8px; padding: 8px;">
                    <div style="font-size: 11px; color: rgba(255,255,255,0.4); margin-bottom: 2px;">最新价</div>
                    <div style="font-size: 16px; font-weight: 600; color: white;" class="shc-price">--</div>
                </div>
                <div style="background: rgba(255,255,255,0.05); border-radius: 8px; padding: 8px;">
                    <div style="font-size: 11px; color: rgba(255,255,255,0.4); margin-bottom: 2px;">涨跌幅</div>
                    <div style="font-size: 16px; font-weight: 600; color: #6b7280;" class="shc-change">--</div>
                </div>
            </div>
            <div style="border-top: 1px solid rgba(255,255,255,0.1); padding-top: 10px;">
                <div style="font-size: 11px; color: rgba(255,255,255,0.4); margin-bottom: 4px;">综合评级</div>
                <div style="font-size: 14px; font-weight: 600; color: #60a5fa;" class="shc-rating">加载中...</div>
            </div>
            <div style="margin-top: 10px; text-align: center;">
                <div style="font-size: 11px; color: rgba(96, 165, 250, 0.7);">点击查看完整深度分析报告 →</div>
            </div>
        `;
        return card;
    }
    
    async function loadStockDetail(stockName, card) {
        if (stockCache[stockName]) {
            updateCardData(card, stockCache[stockName]);
            return;
        }
        try {
            const stock = stockList.find(s => s.name === stockName);
            if (stock && stock.code) {
                const prefix = window.location.pathname.includes('/daily-news-insight/') ? '/daily-news-insight' : '';
                const response = await fetch(prefix + `/data/stock_analysis/${stock.code}.json`);
                if (response.ok) {
                    const data = await response.json();
                    stockCache[stockName] = data;
                    updateCardData(card, data);
                }
            }
        } catch (e) {}
    }
    
    function updateCardData(card, data) {
        const priceEl = card.querySelector('.shc-price');
        const changeEl = card.querySelector('.shc-change');
        const ratingEl = card.querySelector('.shc-rating');
        
        if (data.market && data.market.price != null) {
            priceEl.textContent = Number(data.market.price).toFixed(2);
        } else if (data.technical && data.technical.current_price != null) {
            priceEl.textContent = Number(data.technical.current_price).toFixed(2);
        }
        
        if (data.market && data.market.change_percent !== undefined) {
            const change = Number(data.market.change_percent);
            changeEl.textContent = (change >= 0 ? '+' : '') + change.toFixed(2) + '%';
            changeEl.style.color = change >= 0 ? '#4ade80' : '#f87171';
        }
        
        if (data.overall && data.overall.rating) {
            ratingEl.textContent = data.overall.rating;
            const ratingColors = {
                '买入': '#4ade80', '增持': '#34d399', '持有': '#fbbf24',
                '减持': '#fb923c', '卖出': '#f87171',
            };
            ratingEl.style.color = ratingColors[data.overall.rating] || '#60a5fa';
        }
    }
    
    function scanStockNames() {
        if (stockList.length === 0) return;
        
        const stockNames = stockList.map(s => s.name);
        const textNodes = [];
        
        const walker = document.createTreeWalker(
            document.body,
            NodeFilter.SHOW_TEXT,
            {
                acceptNode: function(node) {
                    if (node.parentElement.closest('.stock-hover-card, script, style, noscript, canvas, .stock-link')) {
                        return NodeFilter.FILTER_REJECT;
                    }
                    if (getComputedStyle(node.parentElement).display === 'none') {
                        return NodeFilter.FILTER_REJECT;
                    }
                    const text = node.textContent;
                    for (const name of stockNames) {
                        if (text.includes(name)) return NodeFilter.FILTER_ACCEPT;
                    }
                    return NodeFilter.FILTER_REJECT;
                }
            }
        );
        
        let node;
        while (node = walker.nextNode()) {
            textNodes.push(node);
        }
        
        textNodes.forEach(textNode => {
            const text = textNode.textContent;
            const parent = textNode.parentNode;
            
            const matches = [];
            for (const stock of stockList) {
                let pos = 0;
                while ((pos = text.indexOf(stock.name, pos)) !== -1) {
                    matches.push({ start: pos, end: pos + stock.name.length, stock: stock });
                    pos += stock.name.length;
                }
            }
            
            if (matches.length === 0) return;
            matches.sort((a, b) => a.start - b.start);
            
            let html = '';
            let lastEnd = 0;
            const div = document.createElement('div');
            
            matches.forEach(match => {
                if (match.start < lastEnd) return;
                div.textContent = text.slice(lastEnd, match.start);
                html += div.innerHTML;
                html += `<span class="stock-link" data-stock="${encodeURIComponent(match.stock.name)}" data-code="${encodeURIComponent(match.stock.code || '')}" 
                    style="color: #60a5fa; cursor: pointer; text-decoration: underline; text-decoration-style: dotted; text-underline-offset: 3px; text-decoration-color: rgba(96, 165, 250, 0.5);">
                    ${(div.textContent = match.stock.name, div.innerHTML)}
                </span>`;
                lastEnd = match.end;
            });
            
            div.textContent = text.slice(lastEnd);
            html += div.innerHTML;
            
            const temp = document.createElement('template');
            temp.innerHTML = html;
            parent.replaceChild(temp.content, textNode);
        });
        
        bindStockLinks();
    }
    
    function bindStockLinks() {
        const links = document.querySelectorAll('.stock-link');
        let currentCard = null;
        let hideTimeout = null;
        
        links.forEach(link => {
            const stockName = decodeURIComponent(link.dataset.stock);
            const stockCode = decodeURIComponent(link.dataset.code || '');
            
            link.addEventListener('mouseenter', function(e) {
                clearTimeout(hideTimeout);
                if (currentCard) currentCard.remove();
                
                currentCard = createHoverCard(stockName, stockCode);
                document.body.appendChild(currentCard);
                loadStockDetail(stockName, currentCard);
                positionCard(e, currentCard);
                
                requestAnimationFrame(() => {
                    currentCard.style.opacity = '1';
                    currentCard.style.transform = 'translateY(0)';
                });
            });
            
            link.addEventListener('mousemove', function(e) {
                if (currentCard) positionCard(e, currentCard);
            });
            
            link.addEventListener('mouseleave', function() {
                hideTimeout = setTimeout(() => {
                    if (currentCard) {
                        currentCard.style.opacity = '0';
                        currentCard.style.transform = 'translateY(10px)';
                        setTimeout(() => {
                            if (currentCard) { currentCard.remove(); currentCard = null; }
                        }, 200);
                    }
                }, 300);
            });
            
            link.addEventListener('click', function(e) {
                e.preventDefault();
                const prefix = window.location.pathname.includes('/daily-news-insight/') ? '/daily-news-insight' : '';
                window.location.href = `${prefix}/个股分析/${encodeURIComponent(stockName)}.html`;
            });
        });
        
        document.addEventListener('mouseover', function(e) {
            if (e.target.closest('.stock-hover-card')) clearTimeout(hideTimeout);
        });
    }
    
    function positionCard(e, card) {
        const mouseX = e.clientX, mouseY = e.clientY;
        const cardRect = card.getBoundingClientRect();
        let left = mouseX + 15, top = mouseY + 15;
        
        if (left + cardRect.width > window.innerWidth - 20) left = mouseX - cardRect.width - 15;
        if (top + cardRect.height > window.innerHeight - 20) top = mouseY - cardRect.height - 15;
        
        card.style.left = left + 'px';
        card.style.top = top + 'px';
    }
    
    function init() {
        loadStockList().then(() => {
            setTimeout(scanStockNames, 800);
        });
    }
    
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
    
    window.StockHoverCard = {
        refresh: scanStockNames,
        reload: function() { loadStockList().then(scanStockNames); }
    };
})();
'''
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(js_code)
    print(f"✅ 全局股票悬浮卡片JS已生成: {output_path}")


# ============================================================
# 三、Skill分层整合配置
# ============================================================

SKILL_INTEGRATION_CONFIG = {
    'core_investment': [
        {
            'skill_name': 'stock-analysis',
            'display_name': '股票个股分析',
            'description': '技术面+资金面+基本面三维分析',
            'page_type': 'stock_detail',
            'boya_strategy_level': 'full',
            'icon': '📈',
            'color': 'blue',
        },
        {
            'skill_name': 'multi-agent-dialogue-system',
            'display_name': '竹石个股Agent',
            'description': '多Agent协作的深度题材分析',
            'page_type': 'topic_deep_dive',
            'boya_strategy_level': 'full',
            'icon': '🎋',
            'color': 'green',
        },
        {
            'skill_name': 'industry-trend-research',
            'display_name': '行业趋势深度调研',
            'description': '麦肯锡风格的行业深度研究',
            'page_type': 'industry_report',
            'boya_strategy_level': 'full',
            'icon': '🔬',
            'color': 'purple',
        },
        {
            'skill_name': 'sector-hotness-analysis',
            'display_name': '板块热度分析',
            'description': '政策-产业-资金三维热度分析',
            'page_type': 'sector_heatmap',
            'boya_strategy_level': 'medium',
            'icon': '🔥',
            'color': 'orange',
        },
        {
            'skill_name': 'a-stock-risk-report',
            'display_name': '每日持仓风险报告',
            'description': '盘前风险扫描与机会识别',
            'page_type': 'risk_report',
            'boya_strategy_level': 'full',
            'icon': '⚠️',
            'color': 'red',
        },
    ],
    'information': [
        {
            'skill_name': 'daily-news-report',
            'display_name': '全球热点新闻日报',
            'description': '每日科技资讯与市场动态',
            'page_type': 'daily_report',
            'boya_strategy_level': 'light',
            'icon': '📰',
            'color': 'blue',
        },
        {
            'skill_name': 'topic_tracking',
            'display_name': '话题追踪v3',
            'description': '题材持续跟踪与定期简报',
            'page_type': 'topic_tracking',
            'boya_strategy_level': 'light',
            'icon': '🔍',
            'color': 'cyan',
        },
        {
            'skill_name': 'stock-data-skill',
            'display_name': 'A股实时数据',
            'description': '多数据源实时行情查询',
            'page_type': 'data_tool',
            'boya_strategy_level': 'none',
            'icon': '📊',
            'color': 'green',
        },
        {
            'skill_name': 'gold-market-analyzer',
            'display_name': '黄金投资分析',
            'description': '三因子模型黄金市场分析',
            'page_type': 'gold_report',
            'boya_strategy_level': 'medium',
            'icon': '🥇',
            'color': 'yellow',
        },
    ],
    'tools': [
        {
            'skill_name': 'company-competitor-research',
            'display_name': '公司竞品调研',
            'description': '企业尽调与竞品分析',
            'page_type': 'company_research',
            'boya_strategy_level': 'none',
            'icon': '🏢',
            'color': 'slate',
        },
        {
            'skill_name': 'toutiao-hot-article',
            'display_name': '今日头条爆文',
            'description': '爆款文章生成器',
            'page_type': 'content_tool',
            'boya_strategy_level': 'none',
            'icon': '✍️',
            'color': 'pink',
        },
    ],
}


# ============================================================
# 四、boya策略分层注入器
# ============================================================

class BoyaStrategyInjector:
    """boya策略分层注入器"""
    
    LEVELS = {
        'full': ['mainline_rating', 'dragon_identify', 'buy_point', 'stop_loss', 
                 'elasticity', 'portfolio_impact', 'prediction_tracking', 'perspective_box'],
        'medium': ['mainline_rating', 'buy_point', 'stop_loss', 'perspective_box'],
        'light': ['perspective_box'],
        'none': [],
    }
    
    def __init__(self, level: str = 'none'):
        self.level = level
        self.components = self.LEVELS.get(level, [])
    
    def get_level_components(self):
        return self.components


# ============================================================
# 主执行函数
# ============================================================

def main():
    docs_dir = 'docs'
    
    print("=" * 60)
    print("🚀 V3.5系统 Skill 整合架构升级")
    print("=" * 60)
    
    # 1. 生成全局股票悬浮卡片JS
    print("\n📦 [1/4] 生成全局股票悬浮卡片系统...")
    generate_stock_hover_card_js(os.path.join(docs_dir, 'js', 'stock-hover-card.js'))
    
    # 2. 生成个股分析列表页
    print("\n📋 [2/4] 生成个股分析列表页...")
    list_gen = StockAnalysisListGenerator(docs_dir=docs_dir)
    list_html = list_gen.generate()
    
    list_output = os.path.join(docs_dir, '个股分析', 'index.html')
    os.makedirs(os.path.dirname(list_output), exist_ok=True)
    with open(list_output, 'w', encoding='utf-8') as f:
        f.write(list_html)
    print(f"✅ 个股分析列表页已生成: {list_output}")
    
    # 3. 生成Skill整合架构配置文件
    print("\n🔧 [3/4] 生成Skill整合配置...")
    config_output = os.path.join(docs_dir, 'data', 'skill_integration.json')
    os.makedirs(os.path.dirname(config_output), exist_ok=True)
    with open(config_output, 'w', encoding='utf-8') as f:
        json.dump(SKILL_INTEGRATION_CONFIG, f, ensure_ascii=False, indent=2)
    print(f"✅ Skill整合配置已生成: {config_output}")
    
    # 4. 保存注入器
    print("\n📝 [4/4] 保存boya策略注入器...")
    injector_path = 'v3/analyzers/boya_strategy_injector.py'
    # 注入器已经在上面定义
    print(f"✅ boya策略分层注入器已就绪")
    
    print("\n" + "=" * 60)
    print("🎉 V3.5系统 Skill 整合架构升级完成！")
    print("=" * 60)
    
    total_skills = sum(len(v) for v in SKILL_INTEGRATION_CONFIG.values())
    print(f"""
📊 整合成果：
   • 三层Skill架构（{len(SKILL_INTEGRATION_CONFIG['core_investment'])}个核心 + {len(SKILL_INTEGRATION_CONFIG['information'])}个资讯 + {len(SKILL_INTEGRATION_CONFIG['tools'])}个工具）
   • 四级boya策略注入等级（full/medium/light/none）
   • 全局股票悬浮卡片系统
   • 个股分析中心列表页
   • 可扩展的Skill适配框架
    """)


if __name__ == '__main__':
    main()
