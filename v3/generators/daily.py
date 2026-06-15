"""
每日新闻洞察生成器 - V3.5 专业升级版
核心定位：早盘前的深度市场分析，为交易决策提供支撑
特色模块：市场情绪仪表盘、热点板块深度解读、核心题材推演、明日预判

设计原则：
1. 数据驱动 - 所有内容基于统一数据层
2. 深度分析 - 不是数据罗列，要有逻辑推演和观点
3. 专业美观 - 投研级视觉呈现
4. 严谨可靠 - 数据来源明确，观点有依据
"""
import sys
import os
import json
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.report import Report
from components.layout import Section
from utils.data_loader import get_market_summary, get_hot_sectors, get_cold_sectors


class DailyReportGenerator:
    """每日新闻洞察生成器 - V3.5专业版"""
    
    def __init__(self, date_str: str = None, weekday: str = None, subtitle: str = None):
        self.date_str = date_str or datetime.now().strftime('%Y-%m-%d')
        self.weekday = weekday or ''
        sub = subtitle or f"{self.date_str} {self.weekday} · 龙空龙策略专用"
        self.report = Report(title="每日新闻洞察", report_type="daily", subtitle=sub)
        self._components = []
        
        # 加载数据
        self._load_data()
    
    def _load_data(self):
        """加载所有需要的数据"""
        # 市场数据
        self.market_data = get_market_summary()
        self.hot_sectors = get_hot_sectors()
        self.cold_sectors = get_cold_sectors()
        
        # 指数数据
        from utils.data_loader import get_indices_for_daily
        self.indices = get_indices_for_daily()
        
        # 题材数据
        try:
            with open('data/topics.json', 'r', encoding='utf-8') as f:
                topics_data = json.load(f)
            self.topics = topics_data
        except:
            self.topics = {}
        
        # 持仓数据
        try:
            with open('data/portfolio.json', 'r', encoding='utf-8') as f:
                portfolio_data = json.load(f)
            self.portfolio = portfolio_data
        except:
            self.portfolio = {}
        
        # 预判数据
        try:
            with open('data/predictions.json', 'r', encoding='utf-8') as f:
                pred_data = json.load(f)
            self.predictions = pred_data
        except:
            self.predictions = {}
    

    def _parse_change_pct(self, change_str):
        """解析涨跌幅字符串，返回浮点数"""
        if isinstance(change_str, (int, float)):
            return float(change_str)
        if isinstance(change_str, str):
            # 移除%号和+号
            clean = change_str.replace('%', '').replace('+', '').strip()
            try:
                return float(clean) / 100
            except:
                return 0
        return 0
    
    def _format_change_pct(self, change_val):
        """格式化涨跌幅为带+号的字符串"""
        if isinstance(change_val, str):
            return change_val
        pct = change_val * 100
        sign = '+' if pct >= 0 else ''
        return f'{sign}{pct:.2f}%'

    def add_market_overview(self):
        """添加市场总览 - 专业版
        包含：四大指数表现、市场整体数据、情绪仪表盘
        """
        indices = self.indices
        market = self.market_data
        sentiment = market.get('sentiment', {})
        market_data = market.get('market_data', {})
        
        # 指数卡片
        index_cards_html = ''
        for idx in indices:
            name = idx.get('name', '')
            price = idx.get('price', 0)
            change_pct = self._parse_change_pct(idx.get('change_pct', 0))
            change_str = idx.get('change_pct_str', '')
            up = idx.get('up', True)
            
            # 颜色
            if change_pct > 0:
                color = '#ef4444'
                bg_color = 'linear-gradient(135deg, #fef2f2 0%, #fff7ed 100%)'
                sign = '+'
            elif change_pct < 0:
                color = '#10b981'
                bg_color = 'linear-gradient(135deg, #f0fdf4 0%, #ecfdf5 100%)'
                sign = ''
            else:
                color = '#6b7280'
                bg_color = '#f8fafc'
                sign = ''
            
            index_cards_html += f'''
            <div style="background: {bg_color}; border-radius: 16px; padding: 18px;
                       border: 1px solid rgba(0,0,0,0.04);
                       transition: all 0.3s ease;"
                 onmouseover="this.style.transform='translateY(-2px)';this.style.boxShadow='0 8px 20px rgba(0,0,0,0.08)';"
                 onmouseout="this.style.transform='translateY(0)';this.style.boxShadow='none';">
                <div style="font-size: 13px; color: #6b7280; margin-bottom: 8px;">{name}</div>
                <div style="font-size: 22px; font-weight: 700; color: #1f2937; margin-bottom: 4px;">
                    {price}
                </div>
                <div style="font-size: 13px; font-weight: 600; color: {color};">
                    {sign}{change_str}
                </div>
            </div>
            '''
        
        # 市场概览数据
        turnover = market_data.get('turnover', '—')
        up_count = market_data.get('up_count', 0)
        down_count = market_data.get('down_count', 0)
        limit_up = market_data.get('limit_up_count', 0)
        limit_down = market_data.get('limit_down_count', 0)
        
        # 情绪分数
        fg_score = sentiment.get('fear_greed', 50)
        if fg_score >= 80:
            fg_level = '极度贪婪'
            fg_color = '#ef4444'
        elif fg_score >= 60:
            fg_level = '贪婪'
            fg_color = '#f97316'
        elif fg_score >= 40:
            fg_level = '中性'
            fg_color = '#3b82f6'
        elif fg_score >= 20:
            fg_level = '恐惧'
            fg_color = '#10b981'
        else:
            fg_level = '极度恐惧'
            fg_color = '#059669'
        
        bar_gradient = 'linear-gradient(90deg, #10b981 0%, #f59e0b 50%, #ef4444 100%)'
        
        html = f'''
        <div style="background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%); 
                    padding: 28px; border-radius: 20px; 
                    border: 1px solid rgba(0,0,0,0.06);
                    box-shadow: 0 4px 16px rgba(0,0,0,0.04);">
            
            <!-- 四大指数 -->
            <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 14px; margin-bottom: 24px;">
                {index_cards_html}
            </div>
            
            <!-- 分割线 -->
            <div style="height: 1px; background: #e5e7eb; margin: 20px 0;"></div>
            
            <!-- 市场数据 + 情绪 -->
            <div style="display: grid; grid-template-columns: 3fr 2fr; gap: 24px; align-items: center;">
                <!-- 左侧：市场数据 -->
                <div>
                    <div style="font-size: 15px; font-weight: 600; color: #1f2937; margin-bottom: 14px;">
                        📊 市场概况
                    </div>
                    <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 12px;">
                        <div style="text-align: center; padding: 12px; background: #f8fafc; border-radius: 10px;">
                            <div style="font-size: 18px; font-weight: 700; color: #1f2937;">{turnover}</div>
                            <div style="font-size: 11px; color: #6b7280; margin-top: 4px;">成交额</div>
                        </div>
                        <div style="text-align: center; padding: 12px; background: #fef2f2; border-radius: 10px;">
                            <div style="font-size: 18px; font-weight: 700; color: #ef4444;">{up_count}</div>
                            <div style="font-size: 11px; color: #6b7280; margin-top: 4px;">上涨家数</div>
                        </div>
                        <div style="text-align: center; padding: 12px; background: #f0fdf4; border-radius: 10px;">
                            <div style="font-size: 18px; font-weight: 700; color: #10b981;">{down_count}</div>
                            <div style="font-size: 11px; color: #6b7280; margin-top: 4px;">下跌家数</div>
                        </div>
                        <div style="text-align: center; padding: 12px; background: #fffbeb; border-radius: 10px;">
                            <div style="font-size: 18px; font-weight: 700; color: #f59e0b;">{limit_up}/{limit_down}</div>
                            <div style="font-size: 11px; color: #6b7280; margin-top: 4px;">涨停/跌停</div>
                        </div>
                    </div>
                </div>
                
                <!-- 右侧：情绪温度计 -->
                <div style="background: linear-gradient(135deg, #fefce8 0%, #fef3c7 100%); 
                            border-radius: 16px; padding: 20px; text-align: center;">
                    <div style="font-size: 13px; font-weight: 600; color: #92400e; margin-bottom: 10px;">
                        🌡️ 市场情绪
                    </div>
                    <div style="font-size: 36px; font-weight: 900; color: {fg_color}; line-height: 1;">
                        {fg_score}
                    </div>
                    <div style="font-size: 13px; font-weight: 600; color: #b45309; margin-top: 4px;">
                        {fg_level}
                    </div>
                    <div style="width: 100%; height: 8px; background: #fde68a; border-radius: 4px; overflow: hidden; margin-top: 12px;">
                        <div style="height: 100%; width: {fg_score}%; background: {bar_gradient}; border-radius: 4px;"></div>
                    </div>
                    <div style="display: flex; justify-content: space-between; font-size: 10px; color: #92400e; margin-top: 6px;">
                        <span>恐惧</span>
                        <span>中性</span>
                        <span>贪婪</span>
                    </div>
                </div>
            </div>
        </div>
        '''
        
        section = Section(title="🌍 市场总览", content=html, icon="globe")
        self._components.append(section)
    
    def add_sector_analysis(self):
        """添加热点板块深度分析
        每个板块包含：涨幅、领涨股、上涨逻辑、持续性评估
        """
        hot = self.hot_sectors
        cold = self.cold_sectors
        
        if not hot and not cold:
            return
        
        html = '<div style="display: flex; flex-direction: column; gap: 16px;">'
        
        # 热门板块
        if hot:
            html += '''
            <div>
                <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 14px;">
                    <span style="font-size: 18px;">🔥</span>
                    <span style="font-size: 16px; font-weight: 700; color: #1f2937;">强势板块</span>
                </div>
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 14px;">
            '''
            
            for sector in hot:
                name = sector.get('name', '')
                change_pct = self._parse_change_pct(sector.get('change_pct', 0))
                change_str = f"+{change_pct*100:.1f}%" if change_pct > 0 else f"{change_pct*100:.1f}%"
                leader = sector.get('leader', '')
                reason = sector.get('reason', '')
                
                # 持续性评估
                sustainability = self._assess_sustainability(sector)
                
                html += f'''
                <div style="background: linear-gradient(135deg, #fef2f2 0%, #fff7ed 100%); 
                            border-radius: 16px; padding: 18px;
                            border: 1px solid rgba(239, 68, 68, 0.15);
                            transition: all 0.3s ease;"
                     onmouseover="this.style.transform='translateY(-2px)';this.style.boxShadow='0 8px 20px rgba(239,68,68,0.1)';"
                     onmouseout="this.style.transform='translateY(0)';this.style.boxShadow='none';">
                    <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 12px;">
                        <div style="font-size: 16px; font-weight: 700; color: #991b1b;">{name}</div>
                        <div style="font-size: 16px; font-weight: 700; color: #ef4444;">{change_str}</div>
                    </div>
                    <div style="font-size: 13px; color: #7f1d1d; line-height: 1.7; margin-bottom: 12px;">
                        <strong>领涨：</strong>{leader}
                    </div>
                    <div style="font-size: 13px; color: #6b7280; line-height: 1.7; margin-bottom: 12px;">
                        {reason}
                    </div>
                    <div style="display: flex; align-items: center; gap: 8px;">
                        <span style="font-size: 11px; color: #6b7280;">持续性评估：</span>
                        <div style="flex: 1; height: 6px; background: #fecaca; border-radius: 3px; overflow: hidden;">
                            <div style="height: 100%; width: {sustainability['score']}%; background: #ef4444; border-radius: 3px;"></div>
                        </div>
                        <span style="font-size: 11px; font-weight: 600; color: #991b1b;">{sustainability['level']}</span>
                    </div>
                </div>
                '''
            
            html += '</div></div>'
        
        # 弱势板块
        if cold:
            html += '''
            <div>
                <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 14px;">
                    <span style="font-size: 18px;">🧊</span>
                    <span style="font-size: 16px; font-weight: 700; color: #1f2937;">弱势板块</span>
                </div>
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 14px;">
            '''
            
            for sector in cold:
                name = sector.get('name', '')
                change_pct = self._parse_change_pct(sector.get('change_pct', 0))
                change_str = f"{change_pct*100:.1f}%"
                reason = sector.get('reason', '')
                
                html += f'''
                <div style="background: linear-gradient(135deg, #f0fdf4 0%, #ecfdf5 100%); 
                            border-radius: 16px; padding: 18px;
                            border: 1px solid rgba(16, 185, 129, 0.15);">
                    <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 10px;">
                        <div style="font-size: 16px; font-weight: 700; color: #065f46;">{name}</div>
                        <div style="font-size: 16px; font-weight: 700; color: #10b981;">{change_str}</div>
                    </div>
                    <div style="font-size: 13px; color: #6b7280; line-height: 1.7;">
                        {reason}
                    </div>
                </div>
                '''
            
            html += '</div></div>'
        
        html += '</div>'
        
        section = Section(title="🏢 板块深度分析", content=html, icon="building")
        self._components.append(section)
    
    def _assess_sustainability(self, sector):
        """评估板块持续性"""
        reason = sector.get('reason', '')
        change_pct = self._parse_change_pct(sector.get('change_pct', 0))
        
        score = 50  # 基准分
        
        # 基于关键词加分
        keywords_high = ['周期反转', '需求爆发', '政策支持', '技术突破', '国产替代']
        keywords_mid = ['业绩超预期', '行业景气', '资金流入']
        
        for kw in keywords_high:
            if kw in reason:
                score += 15
        
        for kw in keywords_mid:
            if kw in reason:
                score += 10
        
        # 涨幅过大反而降低持续性
        if change_pct > 0.05:
            score -= 10
        
        score = max(10, min(95, score))
        
        if score >= 80:
            level = '很强'
        elif score >= 60:
            level = '较强'
        elif score >= 40:
            level = '一般'
        else:
            level = '较弱'
        
        return {'score': score, 'level': level}
    
    def add_topic_deep_dive(self):
        """核心题材深度推演
        从S级题材中选1-2个进行深度分析
        """
        s_topics = self.topics.get('s_level_topics', [])
        if not s_topics:
            return
        
        # 取第一个S级题材做深度分析
        topic = s_topics[0]
        name = topic.get('name', '')
        level = topic.get('level', 'S')
        core_logic = topic.get('core_logic', '')
        total_score = topic.get('total_score', 0)
        dim_scores = topic.get('dimension_scores', {})
        
        html = f'''
        <div style="background: linear-gradient(135deg, #fffbeb 0%, #fef3c7 100%); 
                    padding: 28px; border-radius: 20px; 
                    border: 1px solid rgba(245, 158, 11, 0.2);">
            
            <!-- 标题区 -->
            <div style="display: flex; align-items: flex-start; justify-content: space-between; margin-bottom: 24px;">
                <div style="flex: 1;">
                    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 8px;">
                        <span style="font-size: 28px;">⚡</span>
                        <span style="font-size: 20px; font-weight: 800; color: #92400e;">{name}</span>
                        <span style="background: linear-gradient(135deg, #ef4444 0%, #f97316 100%);
                                   color: white; padding: 4px 10px; border-radius: 12px;
                                   font-size: 12px; font-weight: 700;">{level}级题材</span>
                    </div>
                    <div style="font-size: 14px; color: #78350f; line-height: 1.8; max-width: 600px;">
                        {core_logic}
                    </div>
                </div>
                <div style="text-align: center; margin-left: 20px; flex-shrink: 0;">
                    <div style="font-size: 32px; font-weight: 900; 
                               background: linear-gradient(135deg, #f59e0b 0%, #ef4444 100%);
                               -webkit-background-clip: text; -webkit-text-fill-color: transparent;
                               background-clip: text;">
                        {total_score}
                    </div>
                    <div style="font-size: 11px; color: #92400e;">综合评分</div>
                </div>
            </div>
            
            <!-- 六维评分 -->
            <div style="display: grid; grid-template-columns: repeat(6, 1fr); gap: 10px; margin-bottom: 24px;">
        '''
        
        dim_labels = {
            'policy': ('政策', '📋'),
            'industry': ('产业', '🏭'),
            'capital': ('资金', '💰'),
            'sentiment': ('情绪', '🔥'),
            'valuation': ('估值', '📐'),
            'catalyst': ('催化', '⚡'),
        }
        
        for key, (label, icon) in dim_labels.items():
            score = dim_scores.get(key, 0)
            if score >= 85:
                bar_color = '#10b981'
            elif score >= 70:
                bar_color = '#f59e0b'
            else:
                bar_color = '#ef4444'
            
            html += f'''
            <div style="text-align: center; background: rgba(255,255,255,0.7); 
                       border-radius: 12px; padding: 12px 8px;">
                <div style="font-size: 20px; margin-bottom: 4px;">{icon}</div>
                <div style="font-size: 16px; font-weight: 700; color: #1f2937;">{score}</div>
                <div style="font-size: 10px; color: #6b7280; margin-top: 2px;">{label}</div>
                <div style="width: 100%; height: 4px; background: #fde68a; border-radius: 2px; margin-top: 8px; overflow: hidden;">
                    <div style="height: 100%; width: {score}%; background: {bar_color}; border-radius: 2px;"></div>
                </div>
            </div>
            '''
        
        html += '</div>'
        
        # 催化剂事件
        catalysts = topic.get('catalyst_events', [])
        if catalysts:
            html += '''
            <div style="margin-top: 20px;">
                <div style="font-size: 14px; font-weight: 600; color: #92400e; margin-bottom: 12px;">
                    📅 核心催化事件
                </div>
                <div style="display: flex; flex-wrap: wrap; gap: 8px;">
            '''
            for cat in catalysts:
                html += f'''
                <span style="background: rgba(255,255,255,0.8); color: #78350f;
                           padding: 6px 12px; border-radius: 8px; font-size: 12px;
                           border: 1px solid #fde68a;">
                    {cat}
                </span>
                '''
            html += '</div></div>'
        
        # 核心标的
        leader = topic.get('leader_stock', '')
        mid = topic.get('mid_cap_stock', '')
        flexible = topic.get('flexible_stock', '')
        
        if leader or mid or flexible:
            html += '''
            <div style="margin-top: 20px;">
                <div style="font-size: 14px; font-weight: 600; color: #92400e; margin-bottom: 12px;">
                    🎯 核心标的
                </div>
                <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px;">
            '''
            if leader:
                html += f'''
                <div style="background: rgba(255,255,255,0.9); border-radius: 10px; padding: 12px; text-align: center;
                           border: 1px solid #fde68a;">
                    <div style="font-size: 12px; color: #6b7280; margin-bottom: 4px;">龙头</div>
                    <div style="font-size: 14px; font-weight: 600; color: #1f2937;">{leader}</div>
                </div>
                '''
            if mid:
                html += f'''
                <div style="background: rgba(255,255,255,0.9); border-radius: 10px; padding: 12px; text-align: center;
                           border: 1px solid #fde68a;">
                    <div style="font-size: 12px; color: #6b7280; margin-bottom: 4px;">中坚</div>
                    <div style="font-size: 14px; font-weight: 600; color: #1f2937;">{mid}</div>
                </div>
                '''
            if flexible:
                html += f'''
                <div style="background: rgba(255,255,255,0.9); border-radius: 10px; padding: 12px; text-align: center;
                           border: 1px solid #fde68a;">
                    <div style="font-size: 12px; color: #6b7280; margin-bottom: 4px;">弹性</div>
                    <div style="font-size: 14px; font-weight: 600; color: #1f2937;">{flexible}</div>
                </div>
                '''
            html += '</div></div>'
        
        html += '</div>'
        
        section = Section(title="💡 核心题材深度推演", content=html, icon="zap")
        self._components.append(section)
    
    def add_tomorrow_prediction(self):
        """明日关键预判 - 专业版
        基于当前市场数据和题材逻辑，给出结构化的预判
        """
        predictions = []
        
        # 基于热门板块生成看涨预判
        hot = self.hot_sectors
        if hot:
            top_sector = hot[0]
            predictions.append({
                'direction': '看涨',
                'name': top_sector.get('name', ''),
                'confidence': 70,
                'reason': top_sector.get('reason', '行业景气度持续') + '，关注龙头持续性。'
            })
        
        # 大盘预判
        sentiment = self.market_data.get('sentiment', {})
        fg = sentiment.get('fear_greed', 50)
        if fg > 60:
            market_pred = '震荡上行'
            market_conf = 55
            market_reason = '市场情绪偏乐观，资金活跃度较高，但需警惕高位分歧。'
        elif fg > 40:
            market_pred = '震荡整理'
            market_conf = 60
            market_reason = '情绪中性，市场缺乏明确方向，预计维持区间震荡。'
        else:
            market_pred = '震荡下行'
            market_conf = 55
            market_reason = '市场情绪偏谨慎，风险偏好下降，注意控制仓位。'
        
        predictions.insert(0, {
            'direction': '震荡',
            'name': '大盘指数',
            'confidence': market_conf,
            'reason': market_reason
        })
        
        # 风险提示
        predictions.append({
            'direction': '看跌',
            'name': '高位题材股',
            'confidence': 60,
            'reason': '近两日涨幅较大的题材股存在回调风险，注意高低切换。'
        })
        
        # 渲染
        direction_styles = {
            '看涨': {'gradient': 'linear-gradient(135deg, #ef4444 0%, #f97316 100%)', 'icon': '📈'},
            '看跌': {'gradient': 'linear-gradient(135deg, #10b981 0%, #059669 100%)', 'icon': '📉'},
            '震荡': {'gradient': 'linear-gradient(135deg, #6b7280 0%, #475569 100%)', 'icon': '📊'},
        }
        
        pred_html = '<div style="display: flex; flex-direction: column; gap: 14px;">'
        for p in predictions:
            direction = p.get('direction', '震荡')
            style = direction_styles.get(direction, direction_styles['震荡'])
            name = p.get('name', '')
            confidence = p.get('confidence', 60)
            reason = p.get('reason', '')
            
            # 置信度颜色
            if confidence >= 75:
                conf_color = '#10b981'
            elif confidence >= 60:
                conf_color = '#f59e0b'
            else:
                conf_color = '#6b7280'
            
            pred_html += f'''
            <div style="background: rgba(255, 255, 255, 0.85); backdrop-filter: blur(10px);
                        border-radius: 16px; padding: 18px 20px; 
                        border: 1px solid rgba(0, 0, 0, 0.06);">
                <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 10px;">
                    <div style="display: flex; align-items: center; gap: 10px;">
                        <span style="font-size: 20px;">{style['icon']}</span>
                        <span style="font-size: 15px; font-weight: 700; color: #1f2937;">{name}</span>
                    </div>
                    <div style="text-align: right;">
                        <span style="background: {style['gradient']};
                                     color: white; font-size: 12px; font-weight: 700;
                                     padding: 5px 12px; border-radius: 20px;">
                            {direction}
                        </span>
                        <div style="font-size: 11px; color: {conf_color}; margin-top: 4px; font-weight: 600;">
                            置信度 {confidence}%
                        </div>
                    </div>
                </div>
                <p style="font-size: 13px; color: #4b5563; line-height: 1.7; margin: 0;">
                    {reason}
                </p>
            </div>
            '''
        
        pred_html += '</div>'
        
        # 免责声明
        pred_html += '''
        <div style="margin-top: 16px; text-align: center; font-size: 11px; color: #9ca3af; line-height: 1.6;">
            ⚠️ 预判仅供参考，不构成投资建议。市场有风险，投资需谨慎。
            <br>预判基于当前市场数据和逻辑推演，实际走势受多种因素影响。
        </div>
        '''
        
        html = f'''
        <div style="background: linear-gradient(135deg, #f0f4ff 0%, #f5f3ff 100%); 
                    padding: 24px; border-radius: 20px; 
                    border: 1px solid rgba(79, 70, 229, 0.15);">
            {pred_html}
        </div>
        '''
        
        section = Section(title="🎯 明日关键预判", content=html, icon="target")
        self._components.append(section)
    
    def add_holdings_tracking(self):
        """持仓跟踪 - 专业版
        展示持仓股的详细分析和操作建议
        """
        stocks = self.portfolio.get('stocks', [])
        portfolio_info = self.portfolio.get('portfolio', {})
        
        if not stocks:
            return
        
        html = '<div style="display: flex; flex-direction: column; gap: 14px;">'
        
        for stock in stocks:
            name = stock.get('name', '')
            code = stock.get('code', '')
            cost = stock.get('cost_price', 0)
            current = stock.get('current_price', 0)
            profit_pct = (current - cost) / cost * 100
            today_change = stock.get('today_change', 0) * 100
            risk_level = stock.get('risk_level', '')
            risk_progress = stock.get('risk_progress', 0)
            advice = stock.get('advice', '')
            diagnosis = stock.get('diagnosis', {})
            
            profit_color = '#ef4444' if profit_pct >= 0 else '#10b981'
            profit_sign = '+' if profit_pct >= 0 else ''
            today_color = '#ef4444' if today_change >= 0 else '#10b981'
            today_sign = '+' if today_change >= 0 else ''
            
            # 风险条颜色
            if risk_progress < 50:
                risk_bar_color = '#10b981'
            elif risk_progress < 75:
                risk_bar_color = '#f59e0b'
            else:
                risk_bar_color = '#ef4444'
            
            # 诊断指标
            diag_items = []
            if isinstance(diagnosis, dict):
                for key, value in diagnosis.items():
                    if isinstance(value, dict):
                        status = value.get('status', 'normal')
                        status_colors = {
                            'good': '#10b981',
                            'normal': '#3b82f6',
                            'bad': '#ef4444',
                            'warning': '#f59e0b'
                        }
                        color = status_colors.get(status, '#6b7280')
                        diag_items.append({
                            'label': value.get('title', key),
                            'value': value.get('value', ''),
                            'color': color
                        })
            
            diag_html = ''
            for item in diag_items[:4]:
                diag_html += f'''
                <div style="text-align: center; flex: 1;">
                    <div style="font-size: 12px; font-weight: 600; color: {item['color']};">{item['value']}</div>
                    <div style="font-size: 10px; color: #6b7280; margin-top: 2px;">{item['label']}</div>
                </div>
                '''
            
            # 如果没有诊断数据，显示默认
            if not diag_html:
                diag_html = '''
                <div style="text-align: center; flex: 1;">
                    <div style="font-size: 12px; font-weight: 600; color: #3b82f6;">--</div>
                    <div style="font-size: 10px; color: #6b7280; margin-top: 2px;">技术面</div>
                </div>
                <div style="text-align: center; flex: 1;">
                    <div style="font-size: 12px; font-weight: 600; color: #3b82f6;">--</div>
                    <div style="font-size: 10px; color: #6b7280; margin-top: 2px;">资金面</div>
                </div>
                <div style="text-align: center; flex: 1;">
                    <div style="font-size: 12px; font-weight: 600; color: #3b82f6;">--</div>
                    <div style="font-size: 10px; color: #6b7280; margin-top: 2px;">基本面</div>
                </div>
                '''
            
            html += f'''
            <div style="background: white; border-radius: 16px; padding: 18px 20px;
                       border: 1px solid rgba(0,0,0,0.06);
                       box-shadow: 0 2px 8px rgba(0,0,0,0.03);">
                <!-- 头部信息 -->
                <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 14px;">
                    <div>
                        <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 6px;">
                            <span style="font-size: 16px; font-weight: 700; color: #1f2937;">{name}</span>
                            <span style="font-size: 11px; color: #9ca3af;">{code}</span>
                        </div>
                        <div style="display: flex; gap: 14px; font-size: 12px;">
                            <span style="color: #6b7280;">成本: <span style="color: #374151; font-weight: 500;">¥{cost:.2f}</span></span>
                            <span style="color: #6b7280;">现价: <span style="color: #374151; font-weight: 500;">¥{current:.2f}</span></span>
                        </div>
                    </div>
                    <div style="text-align: right;">
                        <div style="font-size: 20px; font-weight: 800; color: {profit_color};">
                            {profit_sign}{profit_pct:.1f}%
                        </div>
                        <div style="font-size: 11px; color: {today_color}; margin-top: 2px;">
                            今日 {today_sign}{today_change:.1f}%
                        </div>
                    </div>
                </div>
                
                <!-- 诊断指标 -->
                <div style="display: flex; gap: 8px; margin-bottom: 14px; padding: 10px; background: #f8fafc; border-radius: 10px;">
                    {diag_html}
                </div>
                
                <!-- 风险条 -->
                <div style="margin-bottom: 12px;">
                    <div style="display: flex; justify-content: space-between; font-size: 11px; margin-bottom: 4px;">
                        <span style="color: #6b7280;">风险等级</span>
                        <span style="color: #374151; font-weight: 500;">{risk_level}</span>
                    </div>
                    <div style="width: 100%; height: 6px; background: #e5e7eb; border-radius: 3px; overflow: hidden;">
                        <div style="height: 100%; width: {risk_progress}%; background: {risk_bar_color}; border-radius: 3px;"></div>
                    </div>
                </div>
                
                <!-- 操作建议 -->
                {self._render_advice_html(advice)}
            </div>
            '''
        
        html += '</div>'
        
        section = Section(title="💼 持仓跟踪", content=html, icon="briefcase")
        self._components.append(section)
    
    def _render_advice_html(self, advice):
        """渲染操作建议HTML - 支持字典和字符串两种格式"""
        if not advice:
            return ''
        
        # 如果是字典，渲染成带标签的样式
        if isinstance(advice, dict):
            type_label = advice.get('type_label', '操作建议')
            text = advice.get('text', '')
            color = advice.get('color', 'green')
            
            # 颜色映射
            color_map = {
                'red': ('#fef2f2', '#dc2626', '#b91c1c'),
                'green': ('#f0fdf4', '#10b981', '#047857'),
                'yellow': ('#fefce8', '#ca8a04', '#854d0e'),
                'blue': ('#eff6ff', '#2563eb', '#1d4ed8'),
            }
            bg_color, border_color, text_color = color_map.get(color, color_map['green'])
            
            return f'''
            <div style="background: {bg_color}; border-radius: 10px; padding: 10px 14px;
                       border-left: 3px solid {border_color};">
                <div style="font-size: 11px; font-weight: 600; color: {text_color}; margin-bottom: 4px;">
                    {type_label}
                </div>
                <div style="font-size: 12px; color: {text_color}; line-height: 1.6; opacity: 0.9;">
                    {text}
                </div>
            </div>
            '''
        
        # 如果是字符串，直接渲染
        return f'''
        <div style="background: #f0fdf4; border-radius: 10px; padding: 10px 14px;
                   border-left: 3px solid #10b981;">
            <div style="font-size: 11px; font-weight: 600; color: #059669; margin-bottom: 4px;">
                💡 操作建议
            </div>
            <div style="font-size: 12px; color: #047857; line-height: 1.6;">
                {advice}
            </div>
        </div>
        '''
    
    def add_risk_warning(self):
        """风险提示 - 专业版
        系统性风险、板块风险、个股风险
        """
        risks = []
        
        # 基于市场情绪的风险
        fg = self.market_data.get('sentiment', {}).get('fear_greed', 50)
        if fg > 80:
            risks.append({
                'level': 'high',
                'title': '情绪过热风险',
                'content': '市场情绪进入极度贪婪区间，短期回调风险加大，建议适当降低仓位。'
            })
        elif fg > 70:
            risks.append({
                'level': 'medium',
                'title': '情绪偏热',
                'content': '市场情绪偏乐观，注意热门板块冲高回落风险，避免追高。'
            })
        
        # 持仓风险
        stocks = self.portfolio.get('stocks', [])
        high_risk_stocks = [s for s in stocks if s.get('risk_progress', 0) >= 70]
        if high_risk_stocks:
            names = '、'.join([s['name'] for s in high_risk_stocks])
            risks.append({
                'level': 'high',
                'title': '个股止损预警',
                'content': f'{names} 已接近止损位，建议密切关注，若有效跌破严格执行止损纪律。'
            })
        
        # 通用风险
        risks.append({
            'level': 'medium',
            'title': '宏观政策风险',
            'content': '关注国内外宏观政策变化对市场的影响，保持对政策面的跟踪。'
        })
        risks.append({
            'level': 'low',
            'title': '外围市场风险',
            'content': '美股及港股市场波动可能对A股产生情绪传导，注意外围市场变化。'
        })
        
        html = '<div style="display: flex; flex-direction: column; gap: 12px;">'
        
        for risk in risks:
            level = risk.get('level', 'medium')
            level_styles = {
                'high': {
                    'bg': 'linear-gradient(135deg, #fef2f2 0%, #fff7ed 100%)',
                    'border': '#fecaca',
                    'title_color': '#b91c1c',
                    'content_color': '#7f1d1d',
                    'icon': '🔴'
                },
                'medium': {
                    'bg': 'linear-gradient(135deg, #fffbeb 0%, #fef3c7 100%)',
                    'border': '#fde68a',
                    'title_color': '#92400e',
                    'content_color': '#78350f',
                    'icon': '🟡'
                },
                'low': {
                    'bg': 'linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%)',
                    'border': '#bae6fd',
                    'title_color': '#0369a1',
                    'content_color': '#075985',
                    'icon': '🔵'
                }
            }
            style = level_styles.get(level, level_styles['medium'])
            
            html += f'''
            <div style="background: {style['bg']}; border-radius: 14px; padding: 16px 18px;
                       border: 1px solid {style['border']};">
                <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 8px;">
                    <span style="font-size: 16px;">{style['icon']}</span>
                    <span style="font-size: 14px; font-weight: 700; color: {style['title_color']};">
                        {risk['title']}
                    </span>
                </div>
                <div style="font-size: 13px; color: {style['content_color']}; line-height: 1.7; padding-left: 26px;">
                    {risk['content']}
                </div>
            </div>
            '''
        
        html += '</div>'
        
        section = Section(title="⚠️ 风险提示", content=html, icon="alert-triangle")
        self._components.append(section)
    
    def add_daily_summary(self):
        """每日总结 - 专业版"""
        # 基于市场数据生成总结
        market = self.market_data
        market_data = market.get('market_data', {})
        sentiment = market.get('sentiment', {})
        
        turnover = market_data.get('turnover', '')
        fg = sentiment.get('fear_greed', 50)
        
        hot = self.hot_sectors
        hot_names = '、'.join([s.get('name', '') for s in hot[:3]]) if hot else ''
        
        summary = f"""
        今日市场整体呈现情绪{"偏强" if fg > 50 else "偏弱"}格局，成交额{turnover}，市场活跃度{"较高" if fg > 60 else "一般"}。
        板块方面，{hot_names}等板块表现强势，市场结构性机会依然存在。
        操作上，建议聚焦业绩确定性强的优质标的，避免追高，保持合理仓位。
        """
        
        html = f'''
        <div style="background: linear-gradient(135deg, #fafafa 0%, #f5f5f4 100%); 
                    padding: 24px; border-radius: 18px;
                    border: 1px solid rgba(0,0,0,0.05);">
            <div style="font-size: 15px; font-weight: 600; color: #1f2937; margin-bottom: 12px;">
                📝 今日总结
            </div>
            <div style="font-size: 14px; color: #4b5563; line-height: 1.9;">
                {summary.strip()}
            </div>
        </div>
        '''
        
        section = Section(title="", content=html, icon="")
        self._components.append(section)
    
    def generate(self) -> str:
        """生成完整HTML"""
        self.report.components.clear()
        for comp in self._components:
            self.report.add(comp)
        return self.report.generate()
    
    def save(self, filepath: str) -> str:
        """保存到文件"""
        html = self.generate()
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
        return filepath
    
    def publish(self, title: str = None, report_type: str = None,
                filename: str = None, excerpt: str = None,
                auto_deploy: bool = True, docs_root: str = "docs") -> dict:
        """一键发布"""
        html_content = self.generate()
        
        import sys
        import os
        sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        from workflow import ReportPublisher
        
        rtype = report_type or self.report.report_type
        display_title = title or self.report.title or rtype
        
        publisher = ReportPublisher(docs_root=docs_root)
        return publisher.publish(
            html_content=html_content,
            title=display_title,
            report_type=rtype,
            filename=filename,
            excerpt=excerpt,
            auto_deploy=auto_deploy
        )
    
    def build_standard_report(self):
        """构建标准版本的日报
        按照标准顺序组装所有模块
        """
        self.add_market_overview()
        self.add_sector_analysis()
        self.add_topic_deep_dive()
        self.add_holdings_tracking()
        self.add_tomorrow_prediction()
        self.add_risk_warning()
        self.add_daily_summary()
        return self


if __name__ == '__main__':
    # 测试生成
    gen = DailyReportGenerator('2026-06-13', '周五')
    gen.build_standard_report()
    html = gen.generate()
    print(f'日报生成成功，长度: {len(html)} 字符')
    
    # 保存测试
    gen.save('docs/daily/test_daily_v35.html')
    print('已保存到 docs/daily/test_daily_v35.html')
