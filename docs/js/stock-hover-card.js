
/**
 * 全局股票悬浮卡片系统
 * V3.5 Pro+ - 深色玻璃态风格 · Skill增强版
 * 自动识别页面中所有股票名称，悬停显示深度分析卡片
 */
(function() {
    const stockCache = {};
    let stockList = [];
    let stockNameMap = {};  // 股票名称 -> 详情
    
    async function loadStockList() {
        try {
            const prefix = getPrefix();
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
                    stockNameMap = {};
                    stockList.forEach(s => stockNameMap[s.name] = s);
                }
            }
        } catch (e) {
            console.log('股票列表加载失败', e);
        }
    }
    
    function getPrefix() {
        return window.location.pathname.includes('/daily-news-insight/') ? '/daily-news-insight' : '';
    }
    
    function createHoverCard(stockName, stockCode) {
        const card = document.createElement('div');
        card.className = 'stock-hover-card';
        card.style.cssText = `
            position: fixed; z-index: 10000;
            background: rgba(15, 23, 42, 0.95);
            backdrop-filter: blur(20px);
            border: 1px solid rgba(59, 130, 246, 0.3);
            border-radius: 14px; padding: 18px; min-width: 320px;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.5);
            opacity: 0; transform: translateY(10px) scale(0.98);
            transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1); 
            pointer-events: auto;
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            cursor: pointer;
        `;
        
        card.innerHTML = `
            <div style="display: flex; justify-content: space-between; align-items: start; margin-bottom: 14px;">
                <div>
                    <div style="font-size: 20px; font-weight: 700; color: white; margin-bottom: 3px;" class="shc-name">${stockName}</div>
                    <div style="font-size: 12px; color: rgba(255,255,255,0.5);" class="shc-code">${stockCode || '加载中...'}</div>
                </div>
                <div style="text-align: right;">
                    <div style="font-size: 11px; color: rgba(255,255,255,0.4); margin-bottom: 2px;">综合评级</div>
                    <div style="font-size: 14px; font-weight: 600; color: #60a5fa;" class="shc-rating">加载中...</div>
                </div>
            </div>
            
            <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 8px; margin-bottom: 14px;">
                <div style="background: rgba(255,255,255,0.05); border-radius: 8px; padding: 10px 8px; text-align: center;">
                    <div style="font-size: 10px; color: rgba(255,255,255,0.4); margin-bottom: 4px;">最新价</div>
                    <div style="font-size: 16px; font-weight: 600; color: white;" class="shc-price">--</div>
                </div>
                <div style="background: rgba(255,255,255,0.05); border-radius: 8px; padding: 10px 8px; text-align: center;">
                    <div style="font-size: 10px; color: rgba(255,255,255,0.4); margin-bottom: 4px;">涨跌幅</div>
                    <div style="font-size: 16px; font-weight: 600; color: #6b7280;" class="shc-change">--</div>
                </div>
                <div style="background: rgba(255,255,255,0.05); border-radius: 8px; padding: 10px 8px; text-align: center;">
                    <div style="font-size: 10px; color: rgba(255,255,255,0.4); margin-bottom: 4px;">换手率</div>
                    <div style="font-size: 16px; font-weight: 600; color: #a78bfa;" class="shc-turnover">--</div>
                </div>
            </div>
            
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin-bottom: 14px;">
                <div style="background: linear-gradient(135deg, rgba(74, 222, 128, 0.1), rgba(34, 197, 94, 0.05)); border: 1px solid rgba(74, 222, 128, 0.2); border-radius: 8px; padding: 10px;">
                    <div style="font-size: 10px; color: #4ade80; margin-bottom: 3px; display: flex; align-items: center; gap: 3px;">
                        <span>⬆️</span> 压力位
                    </div>
                    <div style="font-size: 14px; font-weight: 600; color: #4ade80;" class="shc-resistance">--</div>
                </div>
                <div style="background: linear-gradient(135deg, rgba(248, 113, 113, 0.1), rgba(239, 68, 68, 0.05)); border: 1px solid rgba(248, 113, 113, 0.2); border-radius: 8px; padding: 10px;">
                    <div style="font-size: 10px; color: #f87171; margin-bottom: 3px; display: flex; align-items: center; gap: 3px;">
                        <span>⬇️</span> 支撑位
                    </div>
                    <div style="font-size: 14px; font-weight: 600; color: #f87171;" class="shc-support">--</div>
                </div>
            </div>
            
            <div style="margin-bottom: 14px;">
                <div style="font-size: 10px; color: rgba(255,255,255,0.4); margin-bottom: 5px;">三维评分</div>
                <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 6px;">
                    <div style="background: rgba(255,255,255,0.05); border-radius: 6px; padding: 8px 4px; text-align: center;">
                        <div style="font-size: 9px; color: rgba(255,255,255,0.4); margin-bottom: 2px;">技术面</div>
                        <div style="font-size: 14px; font-weight: 700; color: #9ca3af;" class="shc-tech-score">--</div>
                    </div>
                    <div style="background: rgba(255,255,255,0.05); border-radius: 6px; padding: 8px 4px; text-align: center;">
                        <div style="font-size: 9px; color: rgba(255,255,255,0.4); margin-bottom: 2px;">消息面</div>
                        <div style="font-size: 14px; font-weight: 700; color: #9ca3af;" class="shc-news-score">--</div>
                    </div>
                    <div style="background: rgba(255,255,255,0.05); border-radius: 6px; padding: 8px 4px; text-align: center;">
                        <div style="font-size: 9px; color: rgba(255,255,255,0.4); margin-bottom: 2px;">基本面</div>
                        <div style="font-size: 14px; font-weight: 700; color: #9ca3af;" class="shc-fund-score">--</div>
                    </div>
                </div>
            </div>
            
            <div style="margin-bottom: 14px;">
                <div style="font-size: 10px; color: rgba(255,255,255,0.4); margin-bottom: 5px;">所属板块</div>
                <div style="display: flex; gap: 5px; flex-wrap: wrap;" class="shc-sectors">
                    <span style="font-size: 11px; padding: 2px 8px; background: rgba(96, 165, 250, 0.15); color: #60a5fa; border-radius: 999px;">加载中...</span>
                </div>
            </div>
            
            <div style="border-top: 1px solid rgba(255,255,255,0.1); padding-top: 12px;">
                <div style="display: flex; align-items: center; justify-content: space-between;">
                    <div style="display: flex; align-items: center; gap: 6px;">
                        <span style="font-size: 11px; color: rgba(255,255,255,0.5);">💡 Skill 深度分析</span>
                    </div>
                    <div style="font-size: 11px; color: #fbbf24; font-weight: 500; display: flex; align-items: center; gap: 3px;">
                        查看完整报告 <span>→</span>
                    </div>
                </div>
                <div style="margin-top: 8px; display: flex; gap: 6px;">
                    <div class="shc-tag-gap" style="font-size: 10px; padding: 3px 8px; background: rgba(251, 191, 36, 0.1); color: #fbbf24; border-radius: 6px; display: none;">缺口分析</div>
                    <div class="shc-tag-sentiment" style="font-size: 10px; padding: 3px 8px; background: rgba(167, 139, 250, 0.1); color: #a78bfa; border-radius: 6px; display: none;">情绪分析</div>
                    <div class="shc-tag-action" style="font-size: 10px; padding: 3px 8px; background: rgba(74, 222, 128, 0.1); color: #4ade80; border-radius: 6px; display: none;">操作建议</div>
                </div>
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
            const stock = stockNameMap[stockName];
            if (stock && stock.code) {
                const prefix = getPrefix();
                const response = await fetch(prefix + `/data/stock_analysis/${stock.code}.json`);
                if (response.ok) {
                    const data = await response.json();
                    stockCache[stockName] = data;
                    updateCardData(card, data);
                }
            }
        } catch (e) {
            console.log('加载股票详情失败', e);
        }
    }
    
    function updateCardData(card, data) {
        const priceEl = card.querySelector('.shc-price');
        const changeEl = card.querySelector('.shc-change');
        const ratingEl = card.querySelector('.shc-rating');
        const codeEl = card.querySelector('.shc-code');
        const turnoverEl = card.querySelector('.shc-turnover');
        const resistanceEl = card.querySelector('.shc-resistance');
        const supportEl = card.querySelector('.shc-support');
        const sectorsEl = card.querySelector('.shc-sectors');
        const techScoreEl = card.querySelector('.shc-tech-score');
        const newsScoreEl = card.querySelector('.shc-news-score');
        const fundScoreEl = card.querySelector('.shc-fund-score');
        
        // 价格
        let price = null;
        if (data.market && data.market.price != null) {
            price = Number(data.market.price);
        } else if (data.technical && data.technical.current_price != null) {
            price = Number(data.technical.current_price);
        } else if (data.overall && data.overall.price != null) {
            price = Number(data.overall.price);
        }
        if (price != null) {
            priceEl.textContent = price.toFixed(2);
        }
        
        // 涨跌幅
        let change = null;
        if (data.market && data.market.change_percent !== undefined) {
            change = Number(data.market.change_percent);
        } else if (data.overall && data.overall.change_pct !== undefined) {
            change = Number(data.overall.change_pct);
        }
        if (change != null) {
            changeEl.textContent = (change >= 0 ? '+' : '') + change.toFixed(2) + '%';
            changeEl.style.color = change >= 0 ? '#4ade80' : '#f87171';
        }
        
        // 换手率
        if (data.market && data.market.turnover_rate != null) {
            turnoverEl.textContent = Number(data.market.turnover_rate).toFixed(2) + '%';
        } else if (data.technical && data.technical.volume) {
            turnoverEl.textContent = '有量';
        }
        
        // 评级
        if (data.overall && data.overall.rating) {
            ratingEl.textContent = data.overall.rating;
            const ratingColors = {
                '买入': '#4ade80', '增持': '#34d399', '持有': '#fbbf24',
                '减持': '#fb923c', '卖出': '#f87171', '观望': '#94a3b8',
            };
            ratingEl.style.color = ratingColors[data.overall.rating] || '#60a5fa';
        }
        
        // 代码
        if (data.code && codeEl.textContent === '加载中...') {
            codeEl.textContent = data.code;
        }
        
        // 支撑位/压力位
        if (data.technical && data.technical.support_resistance) {
            const sr = data.technical.support_resistance;
            if (sr.resistance && sr.resistance.length > 0) {
                resistanceEl.textContent = Number(sr.resistance[0]).toFixed(2);
            }
            if (sr.support && sr.support.length > 0) {
                supportEl.textContent = Number(sr.support[0]).toFixed(2);
            }
        } else if (data.technical && data.technical.boll) {
            const boll = data.technical.boll;
            if (boll.upper) resistanceEl.textContent = Number(boll.upper).toFixed(2);
            if (boll.lower) supportEl.textContent = Number(boll.lower).toFixed(2);
        }
        
        // 三维评分
        function getScoreColor(score) {
            if (score == null || isNaN(score)) return '#9ca3af';
            if (score >= 70) return '#4ade80';
            if (score >= 50) return '#fbbf24';
            return '#f87171';
        }
        
        // 技术面评分
        let techScore = null;
        if (data.technical) {
            const techIndicators = ['ma', 'macd', 'rsi', 'kdj', 'boll', 'volume'];
            let sum = 0, count = 0;
            techIndicators.forEach(key => {
                if (data.technical[key] && data.technical[key].score != null) {
                    sum += data.technical[key].score;
                    count++;
                }
            });
            if (count > 0) techScore = Math.round(sum / count * 10) / 10;
            else if (data.technical.overall_score != null) techScore = data.technical.overall_score;
        }
        if (techScore != null) {
            techScoreEl.textContent = techScore;
            techScoreEl.style.color = getScoreColor(techScore);
        }
        
        // 基本面评分
        let fundScore = null;
        if (data.fundamental && data.fundamental.score != null) {
            fundScore = data.fundamental.score;
        }
        if (fundScore != null) {
            fundScoreEl.textContent = Math.round(fundScore * 10) / 10;
            fundScoreEl.style.color = getScoreColor(fundScore);
        }
        
        // 消息面评分
        let newsScore = null;
        if (data.news && data.news.sentiment_score != null) {
            newsScore = data.news.sentiment_score;
        } else if (data.sentiment && data.sentiment.score != null) {
            newsScore = data.sentiment.score;
        }
        if (newsScore != null) {
            newsScoreEl.textContent = Math.round(newsScore * 10) / 10;
            newsScoreEl.style.color = getScoreColor(newsScore);
        }
        
        // 所属板块/题材
        let sectors = [];
        if (data.sector) sectors.push(data.sector);
        if (data.themes && Array.isArray(data.themes)) {
            sectors = sectors.concat(data.themes.slice(0, 3));
        }
        if (sectors.length > 0) {
            sectorsEl.innerHTML = sectors.map(s => 
                `<span style="font-size: 11px; padding: 2px 8px; background: rgba(96, 165, 250, 0.15); color: #60a5fa; border-radius: 999px; white-space: nowrap;">${s}</span>`
            ).join('');
        }
        
        // Skill标签显示
        const gapTag = card.querySelector('.shc-tag-gap');
        const sentimentTag = card.querySelector('.shc-tag-sentiment');
        const actionTag = card.querySelector('.shc-tag-action');
        
        // 检查是否有缺口分析数据
        if (data.technical && (data.technical.gap_analysis || data.technical.gaps)) {
            gapTag.style.display = 'block';
        }
        // 检查是否有情绪分析
        if (data.sentiment || (data.overall && data.overall.sentiment)) {
            sentimentTag.style.display = 'block';
        }
        // 检查是否有操作建议
        if (data.action || data.advice || (data.overall && data.overall.rating)) {
            actionTag.style.display = 'block';
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
                    if (node.parentElement.closest('.stock-hover-card, script, style, noscript, canvas, .stock-link, pre, code')) {
                        return NodeFilter.FILTER_REJECT;
                    }
                    if (getComputedStyle(node.parentElement).display === 'none') {
                        return NodeFilter.FILTER_REJECT;
                    }
                    const text = node.textContent;
                    if (text.length < 2) return NodeFilter.FILTER_REJECT;
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
            
            // 处理重叠匹配（长的优先）
            const filtered = [];
            let lastEnd = -1;
            for (const match of matches.sort((a, b) => b.end - b.start - (a.end - a.start))) {
                if (match.start >= lastEnd) {
                    filtered.push(match);
                    lastEnd = match.end;
                }
            }
            filtered.sort((a, b) => a.start - b.start);
            
            if (filtered.length === 0) return;
            
            let html = '';
            let lastEnd2 = 0;
            const div = document.createElement('div');
            
            filtered.forEach(match => {
                if (match.start < lastEnd2) return;
                div.textContent = text.slice(lastEnd2, match.start);
                html += div.innerHTML;
                html += `<span class="stock-link" data-stock="${encodeURIComponent(match.stock.name)}" data-code="${encodeURIComponent(match.stock.code || '')}" 
                    style="color: #60a5fa; cursor: pointer; text-decoration: none; border-bottom: 1px dotted rgba(96, 165, 250, 0.5); transition: all 0.2s;"
                    onmouseover="this.style.color='#93c5fd'; this.style.borderBottomColor='rgba(147, 197, 253, 0.8)';"
                    onmouseout="this.style.color='#60a5fa'; this.style.borderBottomColor='rgba(96, 165, 250, 0.5)';">
                    ${(div.textContent = match.stock.name, div.innerHTML)}
                </span>`;
                lastEnd2 = match.end;
            });
            
            div.textContent = text.slice(lastEnd2);
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
                
                // 点击卡片跳转到分析页
                currentCard.addEventListener('click', function(e) {
                    e.stopPropagation();
                    const prefix = getPrefix();
                    window.location.href = `${prefix}/个股分析/${encodeURIComponent(stockName)}.html`;
                });
                
                requestAnimationFrame(() => {
                    currentCard.style.opacity = '1';
                    currentCard.style.transform = 'translateY(0) scale(1)';
                });
            });
            
            link.addEventListener('mousemove', function(e) {
                if (currentCard) positionCard(e, currentCard);
            });
            
            link.addEventListener('mouseleave', function() {
                hideTimeout = setTimeout(() => {
                    if (currentCard) {
                        currentCard.style.opacity = '0';
                        currentCard.style.transform = 'translateY(10px) scale(0.98)';
                        setTimeout(() => {
                            if (currentCard) { currentCard.remove(); currentCard = null; }
                        }, 250);
                    }
                }, 200);
            });
            
            // 点击文字也跳转
            link.addEventListener('click', function(e) {
                e.preventDefault();
                const prefix = getPrefix();
                window.location.href = `${prefix}/个股分析/${encodeURIComponent(stockName)}.html`;
            });
        });
        
        // 鼠标移到卡片上时不消失
        document.addEventListener('mouseover', function(e) {
            if (e.target.closest('.stock-hover-card')) {
                clearTimeout(hideTimeout);
            }
        });
    }
    
    function positionCard(e, card) {
        const mouseX = e.clientX, mouseY = e.clientY;
        const cardRect = card.getBoundingClientRect();
        let left = mouseX + 18, top = mouseY + 18;
        
        if (left + cardRect.width > window.innerWidth - 20) {
            left = mouseX - cardRect.width - 18;
        }
        if (top + cardRect.height > window.innerHeight - 20) {
            top = mouseY - cardRect.height - 18;
        }
        if (top < 10) top = 10;
        if (left < 10) left = 10;
        
        card.style.left = left + 'px';
        card.style.top = top + 'px';
    }
    
    function init() {
        loadStockList().then(() => {
            // 分阶段扫描，避免阻塞
            setTimeout(scanStockNames, 500);
            // 二次扫描，确保动态内容也被覆盖
            setTimeout(scanStockNames, 2000);
        });
    }
    
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
    
    // 暴露API
    window.StockHoverCard = {
        refresh: scanStockNames,
        reload: function() { loadStockList().then(scanStockNames); }
    };
})();
