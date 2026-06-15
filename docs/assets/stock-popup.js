/**
 * 个股分析气泡卡片组件 V2.0
 * 鼠标hover到.stock-badge元素时显示个股分析数据
 * 支持自动识别页面中的股票名称
 * 四维分析：技术面、行情面、题材面、基本面
 */
(function() {
    'use strict';

    // 股票名称 -> 代码 映射表（会从stock_list.json动态加载）
    let stockMap = {};
    let stockDataCache = {};
    let isLoading = false;
    let currentCard = null;
    let hideTimer = null;
    let currentBadge = null;
    let autoDetectDone = false;
    let currentTab = 'technical'; // 当前选中的Tab

    // 气泡卡片DOM
    function createPopupCard() {
        const card = document.createElement('div');
        card.className = 'stock-popup-card v2';
        card.id = 'stockPopupCard';
        card.innerHTML = '<div class="stock-popup-loading"><div class="stock-popup-spinner"></div><div>加载中...</div></div>';
        document.body.appendChild(card);
        return card;
    }

    // 加载股票列表
    async function loadStockList() {
        if (isLoading) return;
        if (Object.keys(stockMap).length > 0) return;
        
        isLoading = true;
        try {
            // 尝试加载股票列表
            const response = await fetch('/daily-news-insight/data/stock_analysis/stock_list.json?_=' + Date.now());
            if (response.ok) {
                const data = await response.json();
                stockMap = data.stocks || {};
            }
        } catch (e) {
            console.log('[StockPopup] 加载股票列表失败，使用内置列表');
            // 内置默认列表（持仓股）
            stockMap = {
                '英维克': '002837',
                '铜冠铜箔': '301217',
                '*ST建艺': '002789',
                'ST建艺': '002789',
                '雅克科技': '002409',
            };
        }
        isLoading = false;
    }

    // 自动识别页面中的股票名称并添加标记
    function autoDetectStocks() {
        if (autoDetectDone) return;
        if (Object.keys(stockMap).length === 0) return;
        
        // 需要扫描的选择器（优先内容区域）
        const selectors = ['.pro-content', '.report-content', '.card-glass', 'main', 'article', '.container', '.page-content'];
        let rootElements = [];
        
        for (const selector of selectors) {
            const elements = document.querySelectorAll(selector);
            if (elements.length > 0) {
                rootElements = Array.from(elements);
                break;
            }
        }
        
        // 如果没找到指定区域，就扫描整个body
        if (rootElements.length === 0) {
            rootElements = [document.body];
        }
        
        const stockNames = Object.keys(stockMap);
        if (stockNames.length === 0) return;
        
        // 构建正则表达式，按名称长度排序（长的优先匹配）
        const sortedNames = stockNames.sort((a, b) => b.length - a.length);
        const escapedNames = sortedNames.map(name => name.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'));
        const regex = new RegExp(`(${escapedNames.join('|')})`, 'g');
        
        // 遍历文本节点，替换股票名称
        function walkTextNodes(node) {
            if (node.nodeType === Node.TEXT_NODE) {
                const text = node.textContent;
                if (!text || text.trim().length === 0) return;
                if (!regex.test(text)) return;
                
                const parent = node.parentNode;
                if (!parent) return;
                // 跳过已经是stock-badge的元素
                if (parent.classList && parent.classList.contains('stock-badge')) return;
                // 跳过script、style、code等标签
                const tag = parent.tagName;
                if (['SCRIPT', 'STYLE', 'CODE', 'PRE', 'TEXTAREA', 'INPUT', 'BUTTON'].includes(tag)) return;
                // 跳过已有链接的
                if (tag === 'A') return;
                
                const fragment = document.createDocumentFragment();
                let lastIndex = 0;
                let match;
                regex.lastIndex = 0;
                
                while ((match = regex.exec(text)) !== null) {
                    // 添加匹配前的文本
                    if (match.index > lastIndex) {
                        fragment.appendChild(document.createTextNode(text.slice(lastIndex, match.index)));
                    }
                    
                    // 创建股票标记
                    const badge = document.createElement('span');
                    badge.className = 'stock-badge';
                    badge.dataset.code = stockMap[match[0]];
                    badge.dataset.name = match[0];
                    badge.textContent = match[0];
                    fragment.appendChild(badge);
                    
                    lastIndex = match.index + match[0].length;
                }
                
                // 添加剩余文本
                if (lastIndex < text.length) {
                    fragment.appendChild(document.createTextNode(text.slice(lastIndex)));
                }
                
                parent.replaceChild(fragment, node);
                return;
            }
            
            // 递归遍历子节点
            if (node.childNodes && node.childNodes.length > 0) {
                // 跳过已经处理过的元素
                if (node.classList && node.classList.contains('stock-badge')) return;
                
                // 倒序遍历，避免替换节点导致索引问题
                for (let i = node.childNodes.length - 1; i >= 0; i--) {
                    walkTextNodes(node.childNodes[i]);
                }
            }
        }
        
        rootElements.forEach(el => {
            try {
                walkTextNodes(el);
            } catch (e) {
                console.warn('[StockPopup] 自动识别出错', e);
            }
        });
        
        autoDetectDone = true;
    }

    // 加载单只股票分析数据
    async function loadStockData(code) {
        if (stockDataCache[code]) {
            return stockDataCache[code];
        }
        
        try {
            const response = await fetch(`/daily-news-insight/data/stock_analysis/${code}.json?_=` + Date.now());
            if (response.ok) {
                const data = await response.json();
                stockDataCache[code] = data;
                return data;
            }
        } catch (e) {
            console.log(`[StockPopup] 加载股票 ${code} 数据失败`);
        }
        return null;
    }

    // 格式化数字
    function formatNum(val, decimals = 2) {
        if (val === null || val === undefined || val === '--') return '--';
        if (typeof val === 'number') return val.toFixed(decimals);
        return val;
    }

    // 格式化大数字（如成交额、市值）
    function formatBigNum(val) {
        if (val === null || val === undefined || val === '--') return '--';
        const num = typeof val === 'number' ? val : parseFloat(val);
        if (isNaN(num)) return val;
        if (num >= 100000000) return (num / 100000000).toFixed(2) + '亿';
        if (num >= 10000) return (num / 10000).toFixed(2) + '万';
        return num.toFixed(2);
    }

    // 渲染技术面Tab内容
    function renderTechnicalTab(technical) {
        const ma = technical.ma || {};
        const macd = technical.macd || {};
        const rsi = technical.rsi || {};
        const kdj = technical.kdj || {};
        const boll = technical.boll || {};
        const volume = technical.volume || {};
        const sr = technical.support_resistance || {};

        // 技术信号标签
        const signals = [];
        if (ma.trend) {
            const isBull = ma.trend.includes('多头');
            signals.push({ text: ma.trend, type: isBull ? 'positive' : 'negative' });
        }
        if (macd.signal) {
            const isBull = macd.signal.includes('金叉') || macd.signal.includes('红柱');
            signals.push({ text: macd.signal, type: isBull ? 'positive' : 'negative' });
        }
        if (rsi.signal) {
            const isBull = rsi.signal.includes('超卖');
            signals.push({ text: rsi.signal, type: isBull ? 'positive' : 'negative' });
        }
        if (kdj.signal) {
            const isBull = kdj.signal.includes('金叉') || kdj.signal.includes('超卖');
            signals.push({ text: kdj.signal, type: isBull ? 'positive' : 'negative' });
        }

        let signalsHtml = '';
        signals.slice(0, 4).forEach(s => {
            signalsHtml += `<span class="signal-tag ${s.type}">${s.text}</span>`;
        });

        // 指标网格
        const metrics = [
            { label: 'MA5', value: formatNum(ma.ma5) },
            { label: 'MA20', value: formatNum(ma.ma20) },
            { label: 'MA60', value: formatNum(ma.ma60) },
            { label: 'RSI', value: formatNum(rsi.rsi, 1) },
            { label: 'MACD', value: formatNum(macd.dif, 2) },
            { label: 'KDJ-J', value: formatNum(kdj.j, 1) },
            { label: '布林上轨', value: formatNum(boll.upper) },
            { label: '布林下轨', value: formatNum(boll.lower) },
        ];

        let metricsHtml = '';
        metrics.forEach(m => {
            metricsHtml += `
                <div class="metric-item">
                    <div class="metric-label">${m.label}</div>
                    <div class="metric-value">${m.value}</div>
                </div>
            `;
        });

        return `
            <div class="tab-content active" data-tab="technical">
                <div class="section-title">技术指标</div>
                <div class="metrics-grid">${metricsHtml}</div>
                
                <div class="section-title">支撑压力位</div>
                <div class="levels-row">
                    <div class="level-item">
                        <div class="level-label">支撑位</div>
                        <div class="level-value support">${formatNum(sr.support)}</div>
                    </div>
                    <div class="level-item">
                        <div class="level-label">压力位</div>
                        <div class="level-value resistance">${formatNum(sr.resistance)}</div>
                    </div>
                </div>
                
                <div class="section-title">技术信号</div>
                <div class="signals-row">${signalsHtml || '<span class="signal-tag neutral">暂无信号</span>'}</div>
                
                <div class="section-title">成交量分析</div>
                <div class="volume-info">
                    <span class="volume-text">${volume.analysis || '暂无分析'}</span>
                </div>
            </div>
        `;
    }

    // 渲染行情面Tab内容
    function renderMarketTab(market, overall) {
        if (!market && !overall) {
            return '<div class="tab-content active" data-tab="market"><div class="empty-state">暂无行情数据</div></div>';
        }
        
        market = market || {};
        overall = overall || {};

        const changePct = overall.change_pct || market.change_pct || 0;
        const changeClass = changePct >= 0 ? 'up' : 'down';
        const changeSign = changePct >= 0 ? '+' : '';

        const metrics = [
            { label: '今开', value: formatNum(market.open || overall.open) },
            { label: '最高', value: formatNum(market.high || overall.high) },
            { label: '最低', value: formatNum(market.low || overall.low) },
            { label: '昨收', value: formatNum(market.pre_close || overall.pre_close) },
            { label: '成交额', value: formatBigNum(market.amount || overall.amount) },
            { label: '换手率', value: formatNum(market.turnover_rate || overall.turnover_rate, 2) + '%' },
            { label: '量比', value: formatNum(market.volume_ratio || overall.volume_ratio, 2) },
            { label: '振幅', value: formatNum(market.amplitude || overall.amplitude, 2) + '%' },
        ];

        let metricsHtml = '';
        metrics.forEach(m => {
            metricsHtml += `
                <div class="metric-item">
                    <div class="metric-label">${m.label}</div>
                    <div class="metric-value">${m.value}</div>
                </div>
            `;
        });

        return `
            <div class="tab-content active" data-tab="market">
                <div class="price-large">
                    <span class="price-value">${formatNum(overall.price || market.current_price)}</span>
                    <span class="price-change ${changeClass}">${changeSign}${formatNum(changePct)}%</span>
                </div>
                <div class="metrics-grid">${metricsHtml}</div>
            </div>
        `;
    }

    // 渲染题材面Tab内容
    function renderThemeTab(themes) {
        if (!themes || themes.length === 0) {
            return '<div class="tab-content active" data-tab="theme"><div class="empty-state">暂无题材数据</div></div>';
        }

        let themesHtml = '';
        themes.forEach((theme, index) => {
            const isCore = index < 3; // 前3个标为核心
            themesHtml += `
                <span class="theme-tag ${isCore ? 'core' : ''}">
                    ${isCore ? '⭐ ' : ''}${theme}
                </span>
            `;
        });

        return `
            <div class="tab-content active" data-tab="theme">
                <div class="section-title">所属题材</div>
                <div class="themes-container">${themesHtml}</div>
                <div class="theme-tip">共 ${themes.length} 个题材概念，⭐为核心题材</div>
            </div>
        `;
    }

    // 渲染基本面Tab内容
    function renderFundamentalTab(fundamental) {
        if (!fundamental) {
            return '<div class="tab-content active" data-tab="fundamental"><div class="empty-state">暂无基本面数据</div></div>';
        }

        const metrics = [
            { label: '市盈率(PE)', value: formatNum(fundamental.pe_ratio, 2) },
            { label: '市净率(PB)', value: formatNum(fundamental.pb_ratio, 2) },
            { label: '总市值', value: formatBigNum(fundamental.market_cap) },
            { label: 'ROE', value: formatNum(fundamental.roe, 2) + '%' },
            { label: '每股收益', value: formatNum(fundamental.eps) + '元' },
            { label: '每股净资产', value: formatNum(fundamental.bps) + '元' },
            { label: '毛利率', value: formatNum(fundamental.gross_margin, 2) + '%' },
            { label: '净利率', value: formatNum(fundamental.net_margin, 2) + '%' },
        ];

        let metricsHtml = '';
        metrics.forEach(m => {
            metricsHtml += `
                <div class="metric-item">
                    <div class="metric-label">${m.label}</div>
                    <div class="metric-value">${m.value}</div>
                </div>
            `;
        });

        return `
            <div class="tab-content active" data-tab="fundamental">
                <div class="metrics-grid">${metricsHtml}</div>
                ${fundamental.summary ? `<div class="fund-summary">${fundamental.summary}</div>` : ''}
            </div>
        `;
    }

    // 渲染气泡卡片内容（V2.0带Tab切换）
    function renderCard(data) {
        if (!data) {
            return '<div class="stock-popup-loading">暂无分析数据</div>';
        }

        const overall = data.overall || {};
        const technical = data.technical || {};
        const fundamental = data.fundamental || {};
        const market = data.market || {};
        const themes = data.themes || [];

        // 评级样式
        const rating = overall.rating || '中性';
        let ratingClass = 'neutral';
        let ratingColor = '#9ca3af';
        if (['买入', '强烈推荐', '推荐'].includes(rating)) {
            ratingClass = 'buy';
            ratingColor = '#10b981';
        } else if (['谨慎推荐', '持有', '观望'].includes(rating)) {
            ratingClass = 'hold';
            ratingColor = '#f59e0b';
        } else if (['卖出', '回避', '减持'].includes(rating)) {
            ratingClass = 'sell';
            ratingColor = '#ef4444';
        }

        // 当前价和涨跌幅
        const currentPrice = overall.price || market.current_price || technical.ma?.ma5 || '--';
        const changePct = overall.change_pct || market.change_pct || 0;
        const changeClass = changePct >= 0 ? 'up' : 'down';
        const changeSign = changePct >= 0 ? '+' : '';

        // 综合评分
        const score = overall.score || fundamental.score || 50;
        const scorePercent = Math.min(100, Math.max(0, score));

        // 详情页链接
        const stockName = encodeURIComponent(data.name || '');
        const detailUrl = `/daily-news-insight/个股分析/${stockName}.html`;

        // Tab导航
        const tabsHtml = `
            <div class="tabs-nav">
                <div class="tab-item active" data-tab="technical">技术面</div>
                <div class="tab-item" data-tab="market">行情面</div>
                <div class="tab-item" data-tab="theme">题材面</div>
                <div class="tab-item" data-tab="fundamental">基本面</div>
            </div>
        `;

        // Tab内容区域（默认显示技术面）
        const tabsContentHtml = `
            <div class="tabs-content">
                ${renderTechnicalTab(technical)}
                <div class="tab-content" data-tab="market">${renderMarketTab(market, overall).replace('active', '')}</div>
                <div class="tab-content" data-tab="theme">${renderThemeTab(themes).replace('active', '')}</div>
                <div class="tab-content" data-tab="fundamental">${renderFundamentalTab(fundamental).replace('active', '')}</div>
            </div>
        `;

        return `
            <div class="card-header">
                <div class="header-left">
                    <span class="stock-name">${data.name || '--'}</span>
                    <span class="stock-code">${data.code || '--'}</span>
                </div>
                <span class="stock-rating ${ratingClass}">${rating}</span>
            </div>
            
            <div class="card-price-section">
                <div class="price-row">
                    <span class="current-price">${formatNum(currentPrice)}</span>
                    <span class="price-change ${changeClass}">${changeSign}${formatNum(changePct)}%</span>
                </div>
                <div class="score-bar-container">
                    <div class="score-bar">
                        <div class="score-bar-fill" style="width: ${scorePercent}%; background: linear-gradient(90deg, #ef4444, #f59e0b, #10b981);"></div>
                    </div>
                    <span class="score-text">综合评分 ${score.toFixed(0)}分</span>
                </div>
            </div>
            
            ${tabsHtml}
            ${tabsContentHtml}
            
            <div class="card-footer">
                <a href="${detailUrl}" class="detail-link" target="_blank">查看完整深度分析 →</a>
            </div>
        `;
    }

    // 绑定Tab切换事件
    function bindTabEvents() {
        if (!currentCard) return;
        
        const tabItems = currentCard.querySelectorAll('.tab-item');
        const tabContents = currentCard.querySelectorAll('.tab-content');
        
        tabItems.forEach(tab => {
            tab.addEventListener('click', function(e) {
                e.stopPropagation();
                const tabName = this.dataset.tab;
                currentTab = tabName;
                
                // 切换Tab状态
                tabItems.forEach(t => t.classList.remove('active'));
                this.classList.add('active');
                
                // 切换内容
                tabContents.forEach(c => {
                    c.classList.remove('active');
                    if (c.dataset.tab === tabName) {
                        c.classList.add('active');
                    }
                });
                
                // 重新定位（内容变化可能导致尺寸变化）
                if (currentBadge) {
                    positionCard(currentBadge);
                }
            });
        });
    }

    // 定位气泡卡片
    function positionCard(badge) {
        const card = currentCard;
        if (!card) return;

        const rect = badge.getBoundingClientRect();
        const cardRect = card.getBoundingClientRect();
        
        let top = rect.bottom + 8;
        let left = rect.left;

        // 防止超出右边界
        if (left + cardRect.width > window.innerWidth - 16) {
            left = window.innerWidth - cardRect.width - 16;
        }
        if (left < 16) left = 16;

        // 防止超出下边界，显示在上方
        if (top + cardRect.height > window.innerHeight - 16) {
            top = rect.top - cardRect.height - 8;
        }

        card.style.top = top + 'px';
        card.style.left = left + 'px';
    }

    // 显示气泡卡片
    async function showPopup(badge) {
        // 清除隐藏定时器
        if (hideTimer) {
            clearTimeout(hideTimer);
            hideTimer = null;
        }

        currentBadge = badge;
        currentTab = 'technical'; // 重置到技术面Tab
        
        // 获取股票代码
        let code = badge.dataset.code;
        const name = badge.dataset.name || badge.textContent.trim();
        
        if (!code && name) {
            // 从映射表查找
            await loadStockList();
            code = stockMap[name];
        }

        if (!code) {
            return; // 没有找到股票代码，不显示
        }

        // 创建或获取卡片
        if (!currentCard) {
            currentCard = createPopupCard();
        }

        // 显示加载状态
        currentCard.innerHTML = '<div class="stock-popup-loading"><div class="stock-popup-spinner"></div><div>加载中...</div></div>';
        currentCard.classList.add('visible');
        
        // 定位
        positionCard(badge);

        // 加载数据
        const data = await loadStockData(code);
        if (currentBadge === badge) {
            // 只有当前badge没变时才渲染
            currentCard.innerHTML = renderCard(data);
            bindTabEvents(); // 绑定Tab事件
            positionCard(badge); // 重新定位（内容变化可能导致尺寸变化）
        }
    }

    // 隐藏气泡卡片
    function hidePopup() {
        if (hideTimer) {
            clearTimeout(hideTimer);
        }
        hideTimer = setTimeout(() => {
            if (currentCard) {
                currentCard.classList.remove('visible');
            }
            currentBadge = null;
        }, 200); // 200ms延迟，防止鼠标移动到卡片上时闪烁
    }

    // 初始化
    function init() {
        // 事件委托：监听所有.stock-badge的hover事件
        document.addEventListener('mouseover', function(e) {
            const badge = e.target.closest('.stock-badge');
            if (badge) {
                showPopup(badge);
            }
        });

        document.addEventListener('mouseout', function(e) {
            const badge = e.target.closest('.stock-badge');
            const card = e.target.closest('.stock-popup-card');
            if (badge || card) {
                hidePopup();
            }
        });

        // 鼠标在卡片上时不隐藏
        document.addEventListener('mouseover', function(e) {
            if (e.target.closest('.stock-popup-card')) {
                if (hideTimer) {
                    clearTimeout(hideTimer);
                    hideTimer = null;
                }
            }
        });

        // 移动端：点击显示/隐藏
        document.addEventListener('click', function(e) {
            const badge = e.target.closest('.stock-badge');
            const card = e.target.closest('.stock-popup-card');
            
            if (badge) {
                e.preventDefault();
                if (currentBadge === badge && currentCard && currentCard.classList.contains('visible')) {
                    hidePopup();
                } else {
                    showPopup(badge);
                }
            } else if (!card && currentCard) {
                hidePopup();
            }
        });

        // 滚动时隐藏
        window.addEventListener('scroll', function() {
            if (currentCard && currentCard.classList.contains('visible')) {
                hidePopup();
            }
        }, { passive: true });

        // 加载股票列表后自动识别
        loadStockList().then(() => {
            // 延迟一下，等页面渲染完成
            setTimeout(() => {
                autoDetectStocks();
            }, 500);
        });
    }

    // 页面加载完成后初始化
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }

    // 暴露API
    window.StockPopup = {
        show: showPopup,
        hide: hidePopup,
        refresh: function() {
            autoDetectDone = false;
            loadStockList().then(() => autoDetectStocks());
        },
        addStock: function(name, code) {
            stockMap[name] = code;
            autoDetectDone = false;
            autoDetectStocks();
        }
    };
})();
