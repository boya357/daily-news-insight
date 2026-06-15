/**
 * 个股分析气泡卡片组件
 * 鼠标hover到.stock-badge元素时显示个股分析数据
 * 支持自动识别页面中的股票名称
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

    // 气泡卡片DOM
    function createPopupCard() {
        const card = document.createElement('div');
        card.className = 'stock-popup-card';
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

    // 渲染气泡卡片内容
    function renderCard(data) {
        if (!data) {
            return '<div class="stock-popup-loading">暂无分析数据</div>';
        }

        const overall = data.overall || {};
        const technical = data.technical || {};
        const fundamental = data.fundamental || {};
        
        // 评级样式
        const rating = overall.rating || '中性';
        let ratingClass = 'neutral';
        if (['买入', '强烈推荐', '推荐'].includes(rating)) {
            ratingClass = 'buy';
        } else if (['谨慎推荐', '持有', '观望'].includes(rating)) {
            ratingClass = 'hold';
        } else if (['卖出', '回避', '减持'].includes(rating)) {
            ratingClass = 'sell';
        }

        // 当前价
        const currentPrice = technical.ma?.ma5 || fundamental.current_price || overall.price || '--';
        
        // 涨跌幅
        const changePct = overall.change_pct || 0;
        const changeClass = changePct >= 0 ? 'up' : 'down';
        const changeSign = changePct >= 0 ? '+' : '';

        // 支撑压力位
        const support = technical.support_resistance?.support || '--';
        const resistance = technical.support_resistance?.resistance || '--';

        // 技术信号标签
        const signals = [];
        if (technical.ma?.trend) {
            const isBull = technical.ma.trend.includes('多头');
            signals.push({ text: technical.ma.trend, type: isBull ? 'positive' : 'negative' });
        }
        if (technical.macd?.signal) {
            const isBull = technical.macd.signal.includes('金叉') || technical.macd.signal.includes('红柱');
            signals.push({ text: technical.macd.signal, type: isBull ? 'positive' : 'negative' });
        }
        if (technical.rsi?.signal) {
            const isBull = technical.rsi.signal.includes('超卖');
            signals.push({ text: technical.rsi.signal, type: isBull ? 'positive' : 'negative' });
        }

        let signalsHtml = '';
        signals.slice(0, 3).forEach(s => {
            signalsHtml += `<span class="stock-popup-signal-tag ${s.type}">${s.text}</span>`;
        });

        // 指标数据
        const ma = technical.ma || {};
        const metrics = [
            { label: 'MA5', value: ma.ma5 ? (typeof ma.ma5 === 'number' ? ma.ma5.toFixed(2) : ma.ma5) : '--' },
            { label: 'MA20', value: ma.ma20 ? (typeof ma.ma20 === 'number' ? ma.ma20.toFixed(2) : ma.ma20) : '--' },
            { label: 'MA60', value: ma.ma60 ? (typeof ma.ma60 === 'number' ? ma.ma60.toFixed(2) : ma.ma60) : '--' },
            { label: 'RSI', value: technical.rsi?.rsi ? (typeof technical.rsi.rsi === 'number' ? technical.rsi.rsi.toFixed(1) : technical.rsi.rsi) : '--' },
        ];

        let metricsHtml = '';
        metrics.forEach(m => {
            metricsHtml += `
                <div class="stock-popup-metric">
                    <div class="stock-popup-metric-label">${m.label}</div>
                    <div class="stock-popup-metric-value">${m.value}</div>
                </div>
            `;
        });

        // 详情页链接
        const stockName = encodeURIComponent(data.name || '');
        const detailUrl = `/daily-news-insight/个股分析/${stockName}.html`;

        return `
            <div class="stock-popup-header">
                <div>
                    <span class="stock-popup-name">${data.name || '--'}</span>
                    <span class="stock-popup-code">${data.code || '--'}</span>
                </div>
                <span class="stock-popup-rating ${ratingClass}">${rating}</span>
            </div>
            
            <div class="stock-popup-price">
                <span class="stock-popup-current-price">${typeof currentPrice === 'number' ? currentPrice.toFixed(2) : currentPrice}</span>
                <span class="stock-popup-change ${changeClass}">${changeSign}${typeof changePct === 'number' ? changePct.toFixed(2) : changePct}%</span>
            </div>
            
            <div class="stock-popup-metrics">
                ${metricsHtml}
            </div>
            
            <div class="stock-popup-levels">
                <div class="stock-popup-level">
                    <div class="stock-popup-level-label">支撑位</div>
                    <div class="stock-popup-level-value support">${typeof support === 'number' ? support.toFixed(2) : support}</div>
                </div>
                <div class="stock-popup-level">
                    <div class="stock-popup-level-label">压力位</div>
                    <div class="stock-popup-level-value resistance">${typeof resistance === 'number' ? resistance.toFixed(2) : resistance}</div>
                </div>
            </div>
            
            <div class="stock-popup-signals">
                ${signalsHtml}
            </div>
            
            <div class="stock-popup-footer">
                <a href="${detailUrl}" class="stock-popup-detail-link" target="_blank">查看完整深度分析 →</a>
            </div>
        `;
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
