
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
