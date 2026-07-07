"""
盘后速递生成器 - V3.0 高级版
收盘数据总结 + 晚间公告 + 龙虎榜
"""
import sys
import os
import json

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.report import Report
from components.layout import Section, HighlightBox, SubCard, CardGrid, SplitLayout
from components.data import DataCard, DataGrid, StockTags, Badge, StatCard, Sparkline, Tabs, GaugeChart, ProgressBar
from components.special import RiskAlert, NewsItem


class AftermarketGenerator:
    """盘后速递生成器 - V3.0高级版"""
    
    def __init__(self, date_str: str, subtitle: str = None):
        self.date_str = date_str
        self.subtitle = subtitle or f"{date_str} · 盘后速递"
        self.report = Report(
            title="盘后速递",
            report_type="aftermarket",
            subtitle=self.subtitle
        )
        self._components = []
    
    def add_today_highlight(self, highlight: str):
        """添加今日核心亮点"""
        box = HighlightBox(content=highlight, icon="star", variant="primary", title="今日核心")
        self._components.append(box)
    
    def add_market_summary(self, indices: list, volume: str = "", northbound: str = ""):
        """添加市场收盘总结（V3.0增强版：渐变统计卡）"""
        cards = []
        for idx in indices:
            variant = "success" if idx.get('up', True) else "danger"
            cards.append(StatCard(
                title=idx['name'],
                value=idx['value'],
                subtitle=idx.get('change', ''),
                icon=idx.get('icon', 'trending_up'),
                variant=variant,
                trend=idx.get('change', ''),
                trend_up=idx.get('up', True)
            ))
        
        grid = CardGrid(cards, cols=min(len(cards), 4))
        
        extra_html = ''
        if volume or northbound:
            extra_html = '<div style="margin-top: 16px; display: flex; gap: 12px;">'
            if volume:
                extra_html += f'''
                <div style="flex: 1; background: rgba(255,255,255,0.05); border-radius: 12px; padding: 14px;">
                    <div style="font-size: 12px; color: #94a3b8; margin-bottom: 4px;">成交额</div>
                    <div style="font-size: 16px; font-weight: 700; color: #f1f5f9;">{volume}</div>
                </div>'''
            if northbound:
                extra_html += f'''
                <div style="flex: 1; background: rgba(255,255,255,0.05); border-radius: 12px; padding: 14px;">
                    <div style="font-size: 12px; color: #94a3b8; margin-bottom: 4px;">北向资金</div>
                    <div style="font-size: 16px; font-weight: 700; color: #f1f5f9;">{northbound}</div>
                </div>'''
            extra_html += '</div>'
        
        content = grid.render() + extra_html
        section = Section(title="📊 市场收盘总结", content=content, icon="chart")
        self._components.append(section)
    
    def add_evening_news(self, news_list: list):
        """添加晚间重要新闻"""
        news_html = '<div style="display: flex; flex-direction: column;">'
        for news in news_list:
            item = NewsItem(
                title=news.get("title", ""),
                content=news.get("content", ""),
                time=news.get("time", ""),
                source=news.get("source", ""),
                tag=news.get("tag", "要闻"),
                tag_variant=news.get("tag_variant", "default")
            )
            news_html += item.render()
        news_html += '</div>'
        
        section = Section(title="🌙 晚间重要新闻", content=news_html, icon="moon")
        self._components.append(section)
    
    def add_earnings_forecast(self):
        """添加半年报业绩预增追踪模块"""
        # 加载业绩预告数据
        earnings_data = None
        try:
            data_path = os.path.join('data', 'earnings_forecast', 'earnings_big_growth.json')
            with open(data_path, 'r', encoding='utf-8') as f:
                earnings_data = json.load(f)
        except:
            pass
        
        if not earnings_data or not earnings_data.get("items"):
            content = '''
            <div style="text-align: center; padding: 30px; color: var(--text-secondary);">
                <div style="font-size: 2rem; margin-bottom: 10px;">📊</div>
                <div>暂无业绩大增预告数据</div>
            </div>
            '''
            section = Section(title="📈 业绩预增追踪", content=content, icon="trending_up")
            self._components.append(section)
            return
        
        items = earnings_data.get("items", [])
        update_time = earnings_data.get("update_time", "")
        threshold = earnings_data.get("threshold", 100)
        
        items_html = '<div style="display: flex; flex-direction: column; gap: 12px;">'
        
        for item in items:
            name = item.get("name", "")
            code = item.get("code", "")
            amp_lower = item.get("add_amp_lower", 0)
            amp_upper = item.get("add_amp_upper")
            predict_type = item.get("predict_type", "")
            reason = item.get("change_reason", "")[:80] + ("..." if len(item.get("change_reason", "")) > 80 else "")
            notice_date = item.get("notice_date", "")[:10]
            first_found = item.get("first_found_time", "")
            
            # 增幅显示
            if amp_upper:
                try:
                    amp_str = f"{amp_lower:.0f}% ~ {float(amp_upper):.0f}%"
                except:
                    amp_str = f"{amp_lower:.0f}%"
            else:
                amp_str = f"{amp_lower:.0f}%"
            
            # 根据增幅设置颜色
            if amp_lower >= 500:
                amp_color = '#c084fc'  # purple-400
                amp_bg = 'rgba(192, 132, 252, 0.15)'
            elif amp_lower >= 200:
                amp_color = '#f472b6'  # pink-400
                amp_bg = 'rgba(244, 114, 182, 0.15)'
            elif amp_lower >= 100:
                amp_color = '#4ade80'  # green-400
                amp_bg = 'rgba(74, 222, 128, 0.15)'
            else:
                amp_color = '#60a5fa'  # blue-400
                amp_bg = 'rgba(96, 165, 250, 0.15)'
            
            items_html += f'''
            <div style="background: var(--glass-bg); border: 1px solid var(--glass-border); 
                        border-radius: 12px; padding: 16px; backdrop-filter: blur(10px);">
                <div style="display: flex; justify-content: space-between; align-items: flex-start; gap: 16px;">
                    <div style="flex: 1;">
                        <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 6px;">
                            <span style="color: var(--text-primary); font-weight: 600; font-size: 15px;">{name}</span>
                            <span style="color: var(--text-muted); font-size: 12px;">{code}</span>
                            <span style="font-size: 11px; padding: 2px 8px; border-radius: 10px; 
                                  background: {amp_bg}; color: {amp_color};">{predict_type}</span>
                        </div>
                        <div style="color: var(--text-secondary); font-size: 13px; line-height: 1.5; margin-bottom: 8px;">
                            {reason}
                        </div>
                        <div style="display: flex; gap: 16px; font-size: 12px; color: var(--text-muted);">
                            <span>📅 披露: {notice_date}</span>
                            <span>🔍 发现: {first_found}</span>
                        </div>
                    </div>
                    <div style="text-align: right; flex-shrink: 0;">
                        <div style="font-size: 20px; font-weight: 700; color: {amp_color};">{amp_str}</div>
                        <div style="font-size: 12px; color: var(--text-muted);">净利润增幅</div>
                    </div>
                </div>
            </div>
            '''
        
        items_html += '</div>'
        
        # 顶部统计信息
        stats_html = f'''
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-bottom: 16px;">
            <div style="background: var(--glass-bg); border: 1px solid var(--glass-border); 
                        border-radius: 10px; padding: 14px; text-align: center;">
                <div style="font-size: 24px; font-weight: 700; color: #4ade80; margin-bottom: 4px;">{len(items)}</div>
                <div style="font-size: 12px; color: var(--text-muted);">业绩大增公司</div>
            </div>
            <div style="background: var(--glass-bg); border: 1px solid var(--glass-border); 
                        border-radius: 10px; padding: 14px; text-align: center;">
                <div style="font-size: 24px; font-weight: 700; color: #60a5fa; margin-bottom: 4px;">≥{threshold}%</div>
                <div style="font-size: 12px; color: var(--text-muted);">增幅阈值</div>
            </div>
        </div>
        '''
        
        content = stats_html + items_html
        
        # 添加更新时间
        if update_time:
            content += f'''
            <div style="text-align: right; font-size: 12px; color: var(--text-muted); margin-top: 12px;">
                数据更新时间: {update_time}
            </div>
            '''
        
        section = Section(title="📈 业绩预增追踪", content=content, icon="trending_up")
        self._components.append(section)
    
    def add_holdings_tracking(self, holdings: list):
        """
        添加持仓股跟踪
        
        Args:
            holdings: 持仓列表 [{"name": "英维克", "code": "002837", "price": "68.90", "change": "+1.2%", "up": True, "comment": "..."}, ...]
        """
        content_html = '<div style="display: flex; flex-direction: column; gap: 12px;">'
        for h in holdings:
            change_class = "#10b981" if h.get('up', True) else "#ef4444"
            name = h["name"]
            code = h.get("code", "")
            price = h.get("price", "")
            change = h.get("change", "")
            comment = h.get("comment", "")
            
            content_html += f'''
            <div style="background: rgba(30,30,50,0.5); border: 1px solid rgba(255,255,255,0.08);
                       border-radius: 14px; padding: 16px 18px;
                       box-shadow: 0 2px 8px rgba(0,0,0,0.2);">
                <div style="display: flex; align-items: center;">
                    <div style="flex: 1;">
                        <div style="display: flex; align-items: center; margin-bottom: 4px;">
                            <span style="font-size: 15px; font-weight: 600; color: #f1f5f9;">
                                {name}
                            </span>
                            <span style="font-size: 12px; color: #9ca3af; margin-left: 8px;">
                                {code}
                            </span>
                        </div>
                        <div style="font-size: 12px; color: #94a3b8; line-height: 1.5; max-width: 400px;">
                            {comment}
                        </div>
                    </div>
                    <div style="text-align: right;">
                        <div style="font-size: 18px; font-weight: 700; color: {change_class};">
                            {price}
                        </div>
                        <div style="font-size: 13px; font-weight: 500; color: {change_class};">
                            {change}
                        </div>
                    </div>
                </div>
            </div>
            '''
        content_html += '</div>'
        
        section = Section(
            title="💼 持仓股跟踪",
            content=content_html,
            icon="briefcase"
        )
        self._components.append(section)
    
    def add_holdings_from_data_layer(self):
        """
        从统一数据层（data/portfolio.json）加载持仓数据并添加持仓跟踪
        确保所有报告使用同源数据，杜绝数据不一致问题
        """
        from utils.data_loader import get_holdings_for_intraday
        
        holdings = get_holdings_for_intraday(include_comments=True)
        self.add_holdings_tracking(holdings=holdings)
    
    def add_market_summary_from_data_layer(self):
        """
        从统一数据层（data/market.json）加载市场收盘总结数据
        """
        from utils.data_loader import get_indices_for_daily, get_market_summary
        
        indices_data = get_indices_for_daily()
        market_data = get_market_summary()
        
        # 转换格式
        indices = []
        for idx in indices_data:
            indices.append({
                'name': idx['name'],
                'value': idx['price'],
                'change': idx['change_pct_str'],
                'up': idx['up']
            })
        
        volume = market_data.get('volume', '')
        northbound = market_data.get('northbound', '')
        
        self.add_market_summary(indices=indices, volume=volume, northbound=northbound)
    
    def add_sector_performance_from_data_layer(self, up_limit=5, down_limit=3):
        """
        从统一数据层（data/market.json）加载板块涨跌排行
        """
        from utils.data_loader import get_hot_sectors, get_cold_sectors
        
        hot_sectors = get_hot_sectors(limit=up_limit)
        cold_sectors = get_cold_sectors(limit=down_limit)
        
        # 转换格式
        up_sectors = []
        for s in hot_sectors:
            up_sectors.append({
                'name': s['name'],
                'change': s['change_pct'],
                'up': True,
                'leader': s['leader']
            })
        
        down_sectors = []
        for s in cold_sectors:
            down_sectors.append({
                'name': s['name'],
                'change': s['change_pct'],
                'up': False,
                'leader': s['leader']
            })
        
        self.add_sector_performance(up_sectors=up_sectors, down_sectors=down_sectors)
    
    def add_dragon_tiger_list(self, stocks: list):
        """添加龙虎榜数据"""
        from components.icons import icon_svg
        
        content_html = '<div style="display: flex; flex-direction: column; gap: 12px;">'
        for stock in stocks:
            change_color = "#10b981" if stock.get('up', True) else "#ef4444"
            inst_count = stock.get('institutions', 0)
            inst_html = f'<span style="font-size: 12px; color: #f59e0b; margin-left: 8px;">🏛️ 机构净买</span>' if inst_count > 0 else ''
            
            content_html += f'''
            <div style="background: rgba(30,30,50,0.5); border: 1px solid rgba(255,255,255,0.08);
                       border-radius: 14px; padding: 16px 18px;
                       box-shadow: 0 2px 8px rgba(0,0,0,0.2);">
                <div style="display: flex; align-items: center; margin-bottom: 8px;">
                    <div style="flex: 1;">
                        <span style="font-size: 15px; font-weight: 600; color: #f1f5f9;">{stock["name"]}</span>
                        <span style="font-size: 12px; color: #9ca3af; margin-left: 6px;">{stock.get("code", "")}</span>
                        {inst_html}
                    </div>
                    <span style="font-size: 16px; font-weight: 700; color: {change_color};">{stock.get("change", "")}</span>
                </div>
                <div style="display: flex; gap: 16px; font-size: 12px; color: #94a3b8;">
                    <span>上榜原因：{stock.get("reason", "")}</span>
                    <span>净买入：{stock.get("net_buy", "")}</span>
                </div>
            </div>'''
        content_html += '</div>'
        
        section = Section(title="🐉 龙虎榜解析", content=content_html, icon="award")
        self._components.append(section)
    
    def add_sector_performance(self, up_sectors: list, down_sectors: list):
        """添加板块涨跌幅排行"""
        content_html = '<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px;">'
        
        up_html = '<div style="background: rgba(16,185,129,0.1); border-radius: 14px; padding: 16px;">'
        up_html += '<div style="font-size: 14px; font-weight: 600; color: #059669; margin-bottom: 12px;">📈 领涨板块</div>'
        for s in up_sectors:
            up_html += f'''<div style="display: flex; justify-content: space-between; align-items: center; padding: 6px 0; border-bottom: 1px dashed #bbf7d0;">
                <span style="font-size: 13px; color: #166534;">{s["name"]}</span>
                <span style="font-size: 13px; font-weight: 600; color: #059669;">{s["change"]}</span></div>'''
        up_html += '</div>'
        
        down_html = '<div style="background: rgba(239,68,68,0.1); border-radius: 14px; padding: 16px;">'
        down_html += '<div style="font-size: 14px; font-weight: 600; color: #dc2626; margin-bottom: 12px;">📉 领跌板块</div>'
        for s in down_sectors:
            down_html += f'''<div style="display: flex; justify-content: space-between; align-items: center; padding: 6px 0; border-bottom: 1px dashed #fecaca;">
                <span style="font-size: 13px; color: #f87171;">{s["name"]}</span>
                <span style="font-size: 13px; font-weight: 600; color: #dc2626;">{s["change"]}</span></div>'''
        down_html += '</div>'
        
        content_html += up_html + down_html + '</div>'
        section = Section(title="🏢 板块涨跌幅排行", content=content_html, icon="building")
        self._components.append(section)
    

    def add_market_deep_analysis(self, strong_sectors, weak_sectors, core_view):
        """添加盘面深度解读（V3.0新增）
        
        Args:
            strong_sectors: 强势板块列表 [{"name": "AI算力", "reason": "..."}, ...]
            weak_sectors: 弱势板块列表 [{"name": "消费电子", "reason": "..."}, ...]
            core_view: 核心观点字符串
        """
        # 强势板块
        strong_html = '<div style="background: linear-gradient(135deg, rgba(239,68,68,0.12) 0%, rgba(234,88,12,0.08) 100%); border-radius: 16px; padding: 20px; border: 1px solid rgba(239,68,68,0.3);">'
        strong_html += '<div style="font-size: 14px; font-weight: 700; color: #dc2626; margin-bottom: 10px;">📈 强势板块</div>'
        strong_html += '<div style="font-size: 13px; color: #4b5563; line-height: 1.7;">'
        for s in strong_sectors:
            strong_html += '<p><strong>' + s.get('name', '') + '</strong>：' + s.get('reason', '') + '</p>'
        strong_html += '</div></div>'
        
        # 弱势板块
        weak_html = '<div style="background: linear-gradient(135deg, rgba(16,185,129,0.12) 0%, rgba(5,150,105,0.08) 100%); border-radius: 16px; padding: 20px; border: 1px solid rgba(16,185,129,0.3);">'
        weak_html += '<div style="font-size: 14px; font-weight: 700; color: #059669; margin-bottom: 10px;">📉 弱势板块</div>'
        weak_html += '<div style="font-size: 13px; color: #4b5563; line-height: 1.7;">'
        for w in weak_sectors:
            weak_html += '<p><strong>' + w.get('name', '') + '</strong>：' + w.get('reason', '') + '</p>'
        weak_html += '</div></div>'
        
        # 核心观点
        view_html = '<div style="background: linear-gradient(135deg, #eff6ff 0%, #eef2ff 100%); border-radius: 16px; padding: 20px; border: 1px solid rgba(59, 130, 246, 0.15);">'
        view_html += '<div style="font-size: 14px; font-weight: 700; color: #2563eb; margin-bottom: 10px;">🎯 核心观点</div>'
        view_html += '<p style="font-size: 13px; color: #4b5563; line-height: 1.8; margin: 0;">' + core_view + '</p>'
        view_html += '</div>'
        
        content_html = '<div style="background: rgba(30,30,50,0.5); padding: 28px; border: 1px solid rgba(255,255,255,0.08); border-radius: 20px; box-shadow: 0 4px 16px rgba(0,0,0,0.2), 0 1px 0 rgba(255,255,255,0.05) inset;">'
        content_html += '<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-bottom: 20px;">'
        content_html += strong_html + weak_html
        content_html += '</div>' + view_html + '</div>'
        
        section = Section(title="盘面深度解读", content=content_html, icon="chart")
        self._components.append(section)
    
    def add_sentiment_thermometer(self, temperature, volume, up_count, down_count, limit_up_count):
        """添加情绪温度计（V3.0新增）
        
        Args:
            temperature: 情绪温度 0-100
            volume: 成交额（字符串，如"3.24万亿"）
            up_count: 上涨家数（字符串，如"2867↑"）
            down_count: 下跌家数（字符串，如"2145↓"）
            limit_up_count: 涨停数（字符串，如"62"）
        """
        # 判断情绪等级
        if temperature >= 80:
            level = "极度贪婪"
        elif temperature >= 60:
            level = "偏乐观"
        elif temperature >= 40:
            level = "中性"
        elif temperature >= 20:
            level = "偏悲观"
        else:
            level = "极度恐慌"
        
        content_html = '<div style="background: rgba(30,30,50,0.5); padding: 28px; border: 1px solid rgba(255,255,255,0.08); border-radius: 20px; box-shadow: 0 4px 16px rgba(0,0,0,0.2), 0 1px 0 rgba(255,255,255,0.05) inset;">'
        
        # 温度大数字
        content_html += '<div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 24px;">'
        content_html += '<div><div style="font-size: 48px; font-weight: 900; background: linear-gradient(135deg, #f59e0b 0%, #ef4444 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;">' + str(temperature) + '°</div>'
        content_html += '<div style="font-size: 13px; color: #94a3b8; margin-top: 4px;">市场情绪温度</div></div>'
        content_html += '<div style="text-align: right;"><div style="font-size: 16px; font-weight: 600; color: #f59e0b;">' + level + '</div>'
        content_html += '<div style="font-size: 12px; color: #9ca3af; margin-top: 4px;">20°=极度恐慌 · 100°=极度贪婪</div></div></div>'
        
        # 进度条
        content_html += '<div style="width: 100%; height: 20px; background: #e5e7eb; border-radius: 12px; overflow: hidden; margin-bottom: 24px;">'
        content_html += '<div style="height: 100%; width: ' + str(temperature) + '%; background: linear-gradient(90deg, #10b981 0%, #eab308 50%, #ef4444 100%); border-radius: 12px;"></div></div>'
        
        # 四项数据
        content_html += '<div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 12px; text-align: center;">'
        content_html += '<div><div style="font-size: 18px; font-weight: 800; color: #e2e8f0;">' + volume + '</div><div style="font-size: 12px; color: #9ca3af; margin-top: 4px;">成交额</div></div>'
        content_html += '<div><div style="font-size: 18px; font-weight: 800; color: #ef4444;">' + up_count + '</div><div style="font-size: 12px; color: #9ca3af; margin-top: 4px;">上涨家数</div></div>'
        content_html += '<div><div style="font-size: 18px; font-weight: 800; color: #10b981;">' + down_count + '</div><div style="font-size: 12px; color: #9ca3af; margin-top: 4px;">下跌家数</div></div>'
        content_html += '<div><div style="font-size: 18px; font-weight: 800; color: #f59e0b;">' + str(limit_up_count) + '</div><div style="font-size: 12px; color: #9ca3af; margin-top: 4px;">涨停数</div></div>'
        content_html += '</div></div>'
        
        section = Section(title="情绪温度计", content=content_html, icon="thermometer")
        self._components.append(section)
    
    def add_tomorrow_prediction(self, predictions):
        """添加明日关键预判（V3.0新增）
        predictions: [{"name": "AI算力", "direction": "看涨", "confidence": 75, "reason": "..."}, ...]
        """
        direction_styles = {
            '看涨': {'gradient': 'linear-gradient(135deg, #ef4444 0%, #f97316 100%)', 'icon': '📈'},
            '看跌': {'gradient': 'linear-gradient(135deg, #10b981 0%, #059669 100%)', 'icon': '📉'},
            '震荡': {'gradient': 'linear-gradient(135deg, #6b7280 0%, #475569 100%)', 'icon': '📊'},
        }
        
        pred_html = '<div style="display: flex; flex-direction: column; gap: 16px;">'
        for p in predictions:
            direction = p.get('direction', '震荡')
            style = direction_styles.get(direction, direction_styles['震荡'])
            pred_html += '<div style="background: rgba(30,30,50,0.5); backdrop-filter: blur(10px); border-radius: 16px; padding: 20px; border: 1px solid rgba(255,255,255,0.08);">'
            pred_html += '<div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px;">'
            pred_html += '<div style="display: flex; align-items: center; gap: 10px;">'
            pred_html += '<span style="font-size: 22px;">' + style['icon'] + '</span>'
            pred_html += '<span style="font-weight: 700; color: #f1f5f9;">' + p.get('name', '') + '</span></div>'
            pred_html += '<span style="background: ' + style['gradient'] + '; color: white; font-size: 12px; font-weight: 700; padding: 6px 14px; border-radius: 20px;">'
            pred_html += direction + ' · ' + str(p.get('confidence', 60)) + '%</span></div>'
            pred_html += '<p style="font-size: 13px; color: #4b5563; line-height: 1.7; margin: 0;">' + p.get('reason', '') + '</p>'
            pred_html += '</div>'
        
        pred_html += '</div>'
        pred_html += '<div style="margin-top: 20px; text-align: center; font-size: 12px; color: #9ca3af;">⚠️ 预判仅供参考，不构成投资建议</div>'
        
        content_html = '<div style="background: linear-gradient(135deg, rgba(79,70,229,0.15) 0%, rgba(124,58,237,0.1) 100%); padding: 28px; border: 1px solid rgba(139,92,246,0.2); border-radius: 20px; box-shadow: 0 4px 16px rgba(79,70,229,0.15), 0 1px 0 rgba(255,255,255,0.05) inset;">'
        content_html += pred_html + '</div>'
        
        section = Section(title="明日关键预判", content=content_html, icon="target")
        self._components.append(section)

    def add_risk_warning(self, risks: list):
        """添加风险提示"""
        risk_text = "；".join(risks) if isinstance(risks, list) else risks
        risk = RiskAlert(level="warning", title="⚠️ 风险提示", text=risk_text)
        self._components.append(risk)
    
    def add_trading_plan(self, plan: str):
        """添加下一交易日操作计划"""
        content = f'<div style="line-height: 1.8; color: #e2e8f0; font-size: 14px;">{plan}</div>'
        section = Section(title="🎯 明日操作计划", content=content, icon="target", variant="highlight")
        self._components.append(section)
    
    def generate(self) -> str:
        """生成完整HTML"""
        self.report.components.clear()  # 清空避免重复添加
        for comp in self._components:
            self.report.add(comp)
        return self.report.generate()
    
    def save(self, filepath: str) -> str:
        """保存到文件"""
        self.generate()
        return self.report.save(filepath)
    
    def validate(self) -> list:
        """验证报告"""
        self.generate()
        return self.report.validate()

    def publish(self, title=None, report_type=None, filename=None, excerpt=None, auto_deploy=True, docs_root="docs"):
        """一键发布"""
        html_content = self.generate()
        import sys, os
        sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        from workflow import ReportPublisher
        rtype = report_type or self.report.report_type
        display_title = title or self.report.title or rtype
        publisher = ReportPublisher(docs_root=docs_root)
        return publisher.publish(html_content=html_content, title=display_title, report_type=rtype, filename=filename, excerpt=excerpt, auto_deploy=auto_deploy)
