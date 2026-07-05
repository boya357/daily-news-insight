/**
 * V5.0 L2 工具箱增强脚本
 * - 龙虎榜页：持仓股筛选 / 主线题材筛选 / 游资筛选
 * - 预判验证页：准确率仪表盘 / 时间线 / 胜率统计
 * - 题材健康度：自动更新时间戳
 * - 页面加载后自动识别当前页面类型，按需注入对应功能
 */
(function() {
    'use strict';

    const PAGE_URL = location.pathname;

    // ---------- 通用：持仓股金色高亮（静态页兜底） ----------
    const HOLDINGS = [
        {name: '英维克', code: '002837'},
        {name: '铜冠铜箔', code: '301217'},
        {name: '雅克科技', code: '002409'},
        {name: '*ST建艺', code: '002789'},
        {name: 'ST建艺', code: '002789'},
    ];
    const MAIN_TOPICS = ['AI算力','人形机器人','存储','先进封装','液冷','HBM','PCB','半导体','机器人','贵金属','算力','光模块','CoWoS','金刚石散热','CCL','MLCC','光刻胶'];

    function autoHighlightHoldings(root) {
        root = root || document.getElementById('mainContent') || document.body;
        const walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT, null, false);
        const nodes = [];
        while (walker.nextNode()) nodes.push(walker.currentNode);
        nodes.forEach(function(n) {
            if (!n.parentNode) return;
            const p = n.parentNode;
            if (p.classList && (p.classList.contains('holding-stock-tag') || p.classList.contains('stock-tag'))) return;
            const tag = p.tagName;
            if (tag === 'SCRIPT' || tag === 'STYLE' || tag === 'NOSCRIPT') return;
            const text = n.nodeValue;
            if (!text || text.length < 2) return;
            let match = null, idx = -1;
            for (let i = 0; i < HOLDINGS.length; i++) {
                const j = text.indexOf(HOLDINGS[i].name);
                if (j >= 0) { match = HOLDINGS[i]; idx = j; break; }
            }
            if (!match) return;
            const frag = document.createDocumentFragment();
            const before = text.substring(0, idx);
            const after = text.substring(idx + match.name.length);
            if (before) frag.appendChild(document.createTextNode(before));
            const span = document.createElement('span');
            span.className = 'holding-stock-tag';
            span.setAttribute('data-code', match.code);
            span.textContent = match.name;
            frag.appendChild(span);
            if (after) frag.appendChild(document.createTextNode(after));
            p.replaceChild(frag, n);
        });
    }

    // ---------- 龙虎榜筛选功能 ----------
    function enhanceLonghubang() {
        // 找到龙虎榜股票列表容器（通常是卡片或表格）
        const cards = document.querySelectorAll('.card-glass, .stock-card, tbody tr, [class*="stock"]');
        if (cards.length < 3) return;

        // 注入筛选栏
        const filterBar = document.createElement('div');
        filterBar.className = 'lhb-filter-bar';
        filterBar.innerHTML = `
            <div class="lhb-filter-title">🔍 龙虎榜筛选</div>
            <div class="lhb-filters">
                <button class="lhb-filter-btn active" data-filter="all">全部</button>
                <button class="lhb-filter-btn" data-filter="holding">⭐我的持仓</button>
                <button class="lhb-filter-btn" data-filter="main">🔥主线题材</button>
                <button class="lhb-filter-btn" data-filter="institution">🏛机构净买</button>
                <button class="lhb-filter-btn" data-filter="hotmoney">💸游资</button>
                <input type="text" class="lhb-search" placeholder="搜索股票/题材..." />
            </div>
        `;
        // 插入到第一个卡片之前
        const firstSection = document.querySelector('.card-glass, .pro-container > div, h2');
        if (firstSection && firstSection.parentNode) {
            firstSection.parentNode.insertBefore(filterBar, firstSection);
        }

        // 筛选逻辑
        const btns = filterBar.querySelectorAll('.lhb-filter-btn');
        const search = filterBar.querySelector('.lhb-search');
        function applyFilter() {
            const active = filterBar.querySelector('.lhb-filter-btn.active').dataset.filter;
            const kw = (search.value || '').trim();
            cards.forEach(function(card) {
                const text = card.textContent || '';
                let show = true;
                if (active === 'holding') {
                    show = HOLDINGS.some(h => text.indexOf(h.name) >= 0);
                } else if (active === 'main') {
                    show = MAIN_TOPICS.some(t => text.indexOf(t) >= 0);
                } else if (active === 'institution') {
                    show = text.indexOf('机构') >= 0 && (text.indexOf('净买') >= 0 || text.indexOf('买入') >= 0);
                } else if (active === 'hotmoney') {
                    show = text.indexOf('游资') >= 0 || text.indexOf('营业部') >= 0;
                }
                if (show && kw) show = text.indexOf(kw) >= 0;
                card.style.display = show ? '' : 'none';
            });
        }
        btns.forEach(b => b.addEventListener('click', function() {
            btns.forEach(x => x.classList.remove('active'));
            b.classList.add('active');
            applyFilter();
        }));
        search.addEventListener('input', applyFilter);
    }

    // ---------- 预判验证可视化 ----------
    function enhancePrediction() {
        // 从页面中解析预判数据
        const pageText = document.body.innerText;
        // 提取准确率（简单正则）
        const m = pageText.match(/准确率[^0-9]*(\d+(?:\.\d+)?)%/);
        const rate = m ? parseFloat(m[1]) : null;
        const correctN = (pageText.match(/正确/g) || []).length;
        const wrongN = (pageText.match(/错误/g) || []).length;
        const pendingN = (pageText.match(/待验证|pending/gi) || []).length;

        if (rate === null && correctN === 0) return;

        const dash = document.createElement('div');
        dash.className = 'prediction-dashboard';

        const rateDeg = rate !== null ? (rate / 100 * 180) : 0;
        const grade = rate >= 80 ? '🏆 S级' : rate >= 60 ? '🥇 A级' : rate >= 40 ? '🥈 B级' : rate >= 20 ? '🥉 C级' : '❌ D级';
        const gradeColor = rate >= 80 ? '#fbbf24' : rate >= 60 ? '#c084fc' : rate >= 40 ? '#60a5fa' : '#f87171';

        dash.innerHTML = `
            <div class="pd-title">🎯 预判准确率仪表盘</div>
            <div class="pd-gauge">
                <div class="pd-gauge-bg"></div>
                <div class="pd-gauge-fill" style="transform:rotate(${rateDeg - 90}deg);"></div>
                <div class="pd-gauge-center">
                    <div class="pd-rate">${rate !== null ? rate.toFixed(1) : '—'}<span class="pd-pct">%</span></div>
                    <div class="pd-grade" style="color:${gradeColor}">${grade}分析师</div>
                </div>
            </div>
            <div class="pd-stats">
                <div class="pd-stat pd-correct"><div class="pd-stat-n">${correctN}</div><div class="pd-stat-l">✅ 正确</div></div>
                <div class="pd-stat pd-wrong"><div class="pd-stat-n">${wrongN}</div><div class="pd-stat-l">❌ 错误</div></div>
                <div class="pd-stat pd-pending"><div class="pd-stat-n">${pendingN}</div><div class="pd-stat-l">⏳ 待验证</div></div>
            </div>
        `;

        const cont = document.querySelector('.pro-container') || document.body;
        const firstH = cont.querySelector('h1,h2');
        if (firstH && firstH.parentNode === cont) {
            firstH.parentNode.insertBefore(dash, firstH.nextSibling);
        } else {
            cont.insertBefore(dash, cont.firstChild);
        }

        // 给预判条目添加时间线样式
        const items = document.querySelectorAll('li, .card-glass');
        items.forEach(function(it) {
            const t = it.textContent || '';
            if (t.indexOf('预判') >= 0 && t.length < 500) {
                it.classList.add('pd-timeline-item');
                if (t.indexOf('正确') >= 0 || t.indexOf('✅') >= 0) it.classList.add('pd-correct-item');
                else if (t.indexOf('错误') >= 0 || t.indexOf('❌') >= 0) it.classList.add('pd-wrong-item');
            }
        });
    }

    // ---------- 题材健康度自动更新 ----------
    function enhanceTopicHealth() {
        const stamp = document.createElement('div');
        stamp.className = 'th-update-stamp';
        const now = new Date();
        stamp.innerHTML = `🔄 数据最后刷新：${now.toLocaleString('zh-CN')} · 自动更新中`;
        const cont = document.querySelector('.pro-container');
        if (cont) cont.insertBefore(stamp, cont.firstChild);
    }

    // ---------- 首页"今日必看"动态排序 ----------
    function enhanceHomepage() {
        // 按卡片标题中的S级/持仓/紧急程度重排
        const container = document.querySelector('.pro-container');
        if (!container) return;
        const cards = Array.from(container.children);
        const scored = cards.map(function(c) {
            const text = c.textContent || '';
            let score = 0;
            if (text.indexOf('S级') >= 0 || text.indexOf('🔥') >= 0) score += 100;
            if (HOLDINGS.some(h => text.indexOf(h.name) >= 0)) score += 50;
            if (text.indexOf('风险') >= 0 || text.indexOf('⚠️') >= 0) score += 30;
            if (text.indexOf('今日必看') >= 0) score += 80;
            return {el: c, score: score};
        });
        scored.sort(function(a, b) { return b.score - a.score; });
        scored.forEach(function(s) { container.appendChild(s.el); });
    }

    // ---------- 注入筛选/仪表盘所需CSS ----------
    function injectCSS() {
        if (document.getElementById('l2-toolbox-css')) return;
        const css = document.createElement('style');
        css.id = 'l2-toolbox-css';
        css.textContent = `
            .lhb-filter-bar{background:linear-gradient(135deg,rgba(139,92,246,0.15),rgba(236,72,153,0.08));border:1px solid rgba(168,85,247,0.3);border-radius:14px;padding:12px 16px;margin-bottom:16px;backdrop-filter:blur(12px);}
            .lhb-filter-title{font-size:13px;color:rgba(255,255,255,0.6);margin-bottom:8px;}
            .lhb-filters{display:flex;gap:8px;flex-wrap:wrap;align-items:center;}
            .lhb-filter-btn{background:rgba(255,255,255,0.06);border:1px solid rgba(255,255,255,0.1);color:rgba(255,255,255,0.7);padding:5px 12px;border-radius:8px;font-size:12px;cursor:pointer;transition:all 0.2s;}
            .lhb-filter-btn:hover{background:rgba(255,255,255,0.12);color:white;}
            .lhb-filter-btn.active{background:linear-gradient(135deg,#6366f1,#a855f7);color:white;border-color:transparent;box-shadow:0 4px 12px rgba(168,85,247,0.3);}
            .lhb-search{background:rgba(0,0,0,0.3);border:1px solid rgba(255,255,255,0.1);color:white;padding:6px 12px;border-radius:8px;font-size:12px;outline:none;flex:1;min-width:140px;max-width:220px;}
            .lhb-search::placeholder{color:rgba(255,255,255,0.4);}
            .lhb-search:focus{border-color:#a855f7;}
            .prediction-dashboard{background:linear-gradient(135deg,rgba(99,102,241,0.15),rgba(168,85,247,0.1));border:1px solid rgba(168,85,247,0.3);border-radius:18px;padding:18px;margin:16px 0;}
            .pd-title{font-size:14px;font-weight:700;color:rgba(255,255,255,0.9);margin-bottom:14px;}
            .pd-gauge{position:relative;width:180px;height:100px;margin:0 auto 14px;overflow:hidden;}
            .pd-gauge-bg{position:absolute;bottom:0;left:0;right:0;height:90px;border-radius:90px 90px 0 0;background:rgba(255,255,255,0.08);border:1px solid rgba(255,255,255,0.1);border-bottom:none;}
            .pd-gauge-fill{position:absolute;bottom:0;left:50%;width:90px;height:90px;background:conic-gradient(from -90deg,#10b981 0%,#fbbf24 50%,#ef4444 100%);transform-origin:bottom center;border-radius:90px 90px 0 0;clip-path:polygon(0 100%,100% 100%,100% 0,0 0);}
            .pd-gauge-fill::after{content:'';position:absolute;bottom:0;left:10px;right:10px;top:10px;background:rgba(15,12,41,0.95);border-radius:80px 80px 0 0;}
            .pd-gauge-center{position:absolute;bottom:8px;left:0;right:0;text-align:center;z-index:2;}
            .pd-rate{font-size:28px;font-weight:900;background:linear-gradient(135deg,#c4b5fd,#fbbf24);-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;line-height:1;}
            .pd-pct{font-size:14px;}
            .pd-grade{font-size:12px;font-weight:600;margin-top:2px;}
            .pd-stats{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;}
            .pd-stat{background:rgba(255,255,255,0.05);border:1px solid rgba(255,255,255,0.08);border-radius:10px;padding:8px;text-align:center;}
            .pd-stat-n{font-size:18px;font-weight:800;}
            .pd-stat-l{font-size:10px;color:rgba(255,255,255,0.5);margin-top:2px;}
            .pd-correct .pd-stat-n{color:#34d399;}
            .pd-wrong .pd-stat-n{color:#f87171;}
            .pd-pending .pd-stat-n{color:#fbbf24;}
            .pd-timeline-item{border-left:3px solid rgba(255,255,255,0.1);padding-left:12px;}
            .pd-correct-item{border-left-color:#10b981 !important;}
            .pd-wrong-item{border-left-color:#ef4444 !important;}
            .th-update-stamp{background:rgba(16,185,129,0.1);border:1px solid rgba(16,185,129,0.3);border-radius:10px;padding:8px 14px;font-size:12px;color:#34d399;margin-bottom:14px;display:inline-block;}
            @media(max-width:768px){
                .pd-gauge{width:150px;height:85px;}
                .pd-rate{font-size:22px;}
                .lhb-search{max-width:100%;flex-basis:100%;}
            }
        `;
        document.head.appendChild(css);
    }

    // ---------- 主流程 ----------
    function boot() {
        injectCSS();
        autoHighlightHoldings();

        if (PAGE_URL.indexOf('longhubang') >= 0) {
            enhanceLonghubang();
        } else if (PAGE_URL.indexOf('prediction') >= 0) {
            enhancePrediction();
        } else if (PAGE_URL.indexOf('topic-health') >= 0 || PAGE_URL.indexOf('topic_health') >= 0) {
            enhanceTopicHealth();
        } else if (PAGE_URL.endsWith('/daily-news-insight/') || PAGE_URL.endsWith('/daily-news-insight/index.html') || PAGE_URL.endsWith('/docs/') || PAGE_URL.endsWith('/docs/index.html')) {
            enhanceHomepage();
        }
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', boot);
    } else {
        setTimeout(boot, 100);
    }
})();
