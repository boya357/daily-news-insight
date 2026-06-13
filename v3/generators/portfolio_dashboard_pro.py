"""
持仓智能预警仪表盘生成器 - Pro深色版 V3.5
基于V3系统架构，深色玻璃态主题，专业投资监控
"""
import sys
import os
import json

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.report import Report
from components.layout import Section, Navbar, Footer
from components.base import get_animation_css, get_animation_js


class PortfolioDashboardProGenerator:
    """持仓智能预警仪表盘 - Pro深色版生成器"""
    
    def __init__(self, data_path: str = "data/portfolio.json"):
        self.data_path = data_path
        self._load_data()
        
    def _load_data(self):
        """加载持仓数据"""
        with open(self.data_path, 'r', encoding='utf-8') as f:
            self.data = json.load(f)
        self.portfolio = self.data.get('portfolio', {})
        self.stocks = self.data.get('stocks', [])
        self.longhubang = self.data.get('longhubang', {})
    
    def _generate_dark_theme_css(self) -> str:
        """生成深色Pro主题CSS"""
        return '''
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@300;400;500;700;900&display=swap');
            
            * { font-family: 'Noto Sans SC', sans-serif; }
            
            body {
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
                padding-top: 80px;
            }
            
            .pro-container {
                max-width: 64rem;
                margin: 0 auto;
                padding: 0 1.5rem;
            }
            
            .card-glass {
                background: rgba(139, 92, 246, 0.15);
                backdrop-filter: blur(20px);
                -webkit-backdrop-filter: blur(20px);
                border: 1px solid rgba(255, 255, 255, 0.15);
                box-shadow: 0 15px 40px rgba(102, 126, 234, 0.4);
                border-radius: 20px;
                color: white;
            }
            
            .card-glass .text-gray-800,
            .card-glass .text-gray-700,
            .card-glass .text-gray-600,
            .card-glass .text-gray-500,
            .card-glass .text-gray-400 { color: rgba(255, 255, 255, 0.9) !important; }
            .card-glass .text-gray-500 { color: rgba(255, 255, 255, 0.75) !important; }
            .card-glass .text-gray-400 { color: rgba(255, 255, 255, 0.6) !important; }
            
            /* 修复浅色背景子卡片文字颜色 */
            .card-glass .bg-white .text-gray-800 { color: #1f2937 !important; }
            .card-glass .bg-white .text-gray-700 { color: #374151 !important; }
            .card-glass .bg-white .text-gray-600 { color: #4b5563 !important; }
            .card-glass .bg-white .text-gray-500 { color: #6b7280 !important; }
            .card-glass .bg-white .text-gray-400 { color: #9ca3af !important; }
            
            .stock-card {
                transition: transform 0.3s ease, box-shadow 0.3s ease;
            }
            .stock-card:hover {
                transform: translateY(-4px);
                box-shadow: 0 20px 60px rgba(102, 126, 234, 0.5);
            }
            
            .risk-bar {
                height: 8px;
                border-radius: 4px;
                background: rgba(255,255,255,0.2);
                overflow: hidden;
            }
            .risk-bar-fill {
                height: 100%;
                border-radius: 4px;
                transition: width 0.5s ease;
            }
            
            .diagnosis-item {
                text-align: center;
                padding: 12px 8px;
                background: rgba(255,255,255,0.1);
                border-radius: 12px;
            }
            
            .tag-badge {
                display: inline-block;
                padding: 4px 12px;
                border-radius: 20px;
                font-size: 12px;
                font-weight: 600;
            }
            
            .section-title {
                font-size: 1.25rem;
                font-weight: 700;
                margin-bottom: 1.5rem;
                display: flex;
                align-items: center;
                gap: 10px;
            }
            
            .lhb-card {
                background: rgba(255,255,255,0.08);
                border-radius: 16px;
                padding: 20px;
                margin-bottom: 16px;
                border: 1px solid rgba(255,255,255,0.1);
            }
            
            .lhb-seat {
                display: flex;
                justify-content: space-between;
                align-items: center;
                padding: 8px 0;
                border-bottom: 1px solid rgba(255,255,255,0.1);
                font-size: 13px;
            }
            .lhb-seat:last-child { border-bottom: none; }
            
            .alert-section {
                background: rgba(239, 68, 68, 0.15);
                border: 1px solid rgba(239, 68, 68, 0.3);
                border-radius: 16px;
                padding: 20px;
                margin-bottom: 16px;
            }
            
            .warning-section {
                background: rgba(245, 158, 11, 0.15);
                border: 1px solid rgba(245, 158, 11, 0.3);
                border-radius: 16px;
                padding: 20px;
                margin-bottom: 16px;
            }
            
            .safe-section {
                background: rgba(16, 185, 129, 0.15);
                border: 1px solid rgba(16, 185, 129, 0.3);
                border-radius: 16px;
                padding: 20px;
                margin-bottom: 16px;
            }
            
            .fund-row {
                display: flex;
                justify-content: space-between;
                align-items: center;
                padding: 12px 0;
                border-bottom: 1px solid rgba(255,255,255,0.1);
            }
            .fund-row:last-child { border-bottom: none; }
            
            .fund-trend-up {
                color: #10b981;
                font-weight: 600;
            }
            .fund-trend-down {
                color: #ef4444;
                font-weight: 600;
            }
            
            @media (max-width: 768px) {
                body { padding-top: 70px; }
                .pro-container { padding: 0 1rem; }
            }
        </style>
        '''
    
    def add_hero_dashboard(self) -> str:
        """添加英雄区仪表盘"""
        p = self.portfolio
        total_return = p.get('total_return', 0) * 100
        health_score = p.get('health_score', 0)
        stock_count = p.get('stock_count', 0)
        profit_count = p.get('profit_count', 0)
        loss_count = p.get('loss_count', 0)
        stop_loss_count = p.get('stop_loss_break_count', 0)
        industry_count = p.get('industry_count', 0)
        
        return_color = '#10b981' if total_return >= 0 else '#ef4444'
        return_sign = '+' if total_return >= 0 else ''
        
        html = f'''
        <div class="card-glass p-6 mb-6">
            <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 20px;">
                <span class="text-2xl">📊</span>
                <div>
                    <h1 style="font-size: 28px; font-weight: 900; margin: 0;">持仓智能预警仪表盘</h1>
                    <p style="opacity: 0.8; font-size: 14px; margin-top: 4px;">Pro · 多维度持仓诊断 · 风险实时预警 · 智能调仓建议</p>
                </div>
            </div>
            
            <!-- 核心数据区 -->
            <div style="display: grid; grid-template-columns: 2fr 1fr 1fr 1fr 1fr; gap: 16px; align-items: center;">
                <!-- 总收益率 -->
                <div style="text-align: center; padding: 20px;">
                    <div style="font-size: 48px; font-weight: 900; color: {return_color}; line-height: 1; text-shadow: 0 2px 20px rgba(16,185,129,0.3);">
                        {return_sign}{total_return:.2f}%
                    </div>
                    <div style="font-size: 14px; opacity: 0.8; margin-top: 8px;">组合总盈亏</div>
                </div>
                
                <!-- 健康分 -->
                <div style="text-align: center; background: rgba(255,255,255,0.1); border-radius: 16px; padding: 16px 12px;">
                    <div style="font-size: 28px; font-weight: 800;">{health_score}</div>
                    <div style="font-size: 12px; opacity: 0.75; margin-top: 4px;">健康分</div>
                </div>
                
                <!-- 持仓标的 -->
                <div style="text-align: center; background: rgba(255,255,255,0.1); border-radius: 16px; padding: 16px 12px;">
                    <div style="font-size: 28px; font-weight: 800;">{stock_count}只</div>
                    <div style="font-size: 12px; opacity: 0.75; margin-top: 4px;">持仓标的</div>
                </div>
                
                <!-- 盈亏分布 -->
                <div style="text-align: center; background: rgba(255,255,255,0.1); border-radius: 16px; padding: 16px 12px;">
                    <div style="display: flex; justify-content: center; gap: 8px; margin-bottom: 4px;">
                        <span style="font-size: 18px; font-weight: 700; color: #10b981;">{profit_count}盈</span>
                        <span style="font-size: 18px; font-weight: 700; color: #ef4444;">{loss_count}亏</span>
                    </div>
                    <div style="font-size: 12px; opacity: 0.75;">盈利/亏损</div>
                </div>
                
                <!-- 行业分布 -->
                <div style="text-align: center; background: rgba(255,255,255,0.1); border-radius: 16px; padding: 16px 12px;">
                    <div style="font-size: 28px; font-weight: 800;">{industry_count}个</div>
                    <div style="font-size: 12px; opacity: 0.75; margin-top: 4px;">行业分布</div>
                </div>
            </div>
        </div>
        '''
        return html
    
    def _generate_stock_card(self, stock) -> str:
        """生成单只股票的详细卡片"""
        name = stock.get('name', '')
        code = stock.get('code', '')
        icon = stock.get('icon', '📈')
        cost = stock.get('cost_price', 0)
        current = stock.get('current_price', 0)
        profit_pct = (current - cost) / cost * 100
        today_change = stock.get('today_change', 0) * 100
        stop_loss = stock.get('stop_loss_price', 0)
        distance_sl = stock.get('distance_to_stop_loss', 0) * 100
        safety_margin = stock.get('safety_margin', 0) * 100
        risk_level = stock.get('risk_level', '')
        risk_progress = stock.get('risk_progress', 0)
        main_fund = stock.get('main_fund', '')
        tag = stock.get('tag', '')
        diagnosis = stock.get('diagnosis', {})
        
        profit_color = '#10b981' if profit_pct >= 0 else '#ef4444'
        profit_sign = '+' if profit_pct >= 0 else ''
        today_color = '#10b981' if today_change >= 0 else '#ef4444'
        today_sign = '+' if today_change >= 0 else ''
        
        # 风险进度条颜色
        if risk_progress < 30:
            risk_bar_color = '#10b981'
        elif risk_progress < 70:
            risk_bar_color = '#f59e0b'
        else:
            risk_bar_color = '#ef4444'
        
        # 四维诊断
        diag_html = ''
        diag_order = ['technical', 'fund', 'news', 'industry']
        status_icons = {
            'good': '✓',
            'bad': '✗',
            'neutral': '○',
            'warning': '△'
        }
        status_colors = {
            'good': '#10b981',
            'bad': '#ef4444',
            'neutral': '#f59e0b',
            'warning': '#f97316'
        }
        
        for key in diag_order:
            d = diagnosis.get(key, {})
            status = d.get('status', 'neutral')
            icon_char = status_icons.get(status, '○')
            color = status_colors.get(status, '#9ca3af')
            title = d.get('title', key)
            value = d.get('value', '')
            desc = d.get('desc', '')
            
            diag_html += f'''
            <div class="diagnosis-item" style="flex: 1;">
                <div style="font-size: 20px; color: {color}; margin-bottom: 4px;">{icon_char}</div>
                <div style="font-size: 14px; font-weight: 600; margin-bottom: 2px;">{title}</div>
                <div style="font-size: 12px; opacity: 0.8;">{value}</div>
                <div style="font-size: 11px; opacity: 0.6; margin-top: 2px;">{desc}</div>
            </div>
            '''
        
        # 止损/安全边际信息
        if profit_pct >= 0:
            sl_label = "安全边际"
            sl_value = f"+{safety_margin:.1f}%"
        else:
            sl_label = "距止损"
            sl_value = f"{distance_sl:.1f}%"
        
        html = f'''
        <div class="stock-card card-glass p-6 mb-6">
            <!-- 头部 -->
            <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 20px;">
                <div style="display: flex; align-items: center; gap: 12px;">
                    <span style="font-size: 32px;">{icon}</span>
                    <div>
                        <div style="display: flex; align-items: center; gap: 10px;">
                            <h2 style="font-size: 22px; font-weight: 700; margin: 0;">{name}</h2>
                            <span style="font-size: 14px; opacity: 0.7;">{code}</span>
                        </div>
                        <span class="tag-badge" style="background: rgba(255,255,255,0.2); margin-top: 6px; display: inline-block;">{tag}</span>
                    </div>
                </div>
                <div style="text-align: right;">
                    <div style="font-size: 28px; font-weight: 800; color: {profit_color};">
                        {profit_sign}{profit_pct:.2f}%
                    </div>
                    <div style="font-size: 13px; color: {today_color};">
                        今日 {today_sign}{today_change:.2f}%
                    </div>
                </div>
            </div>
            
            <!-- 关键数据 -->
            <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 12px; margin-bottom: 20px;">
                <div style="background: rgba(255,255,255,0.08); border-radius: 12px; padding: 12px; text-align: center;">
                    <div style="font-size: 12px; opacity: 0.7; margin-bottom: 4px;">成本价</div>
                    <div style="font-size: 16px; font-weight: 600;">¥{cost:.2f}</div>
                </div>
                <div style="background: rgba(255,255,255,0.08); border-radius: 12px; padding: 12px; text-align: center;">
                    <div style="font-size: 12px; opacity: 0.7; margin-bottom: 4px;">最新价</div>
                    <div style="font-size: 16px; font-weight: 600;">¥{current:.2f}</div>
                </div>
                <div style="background: rgba(255,255,255,0.08); border-radius: 12px; padding: 12px; text-align: center;">
                    <div style="font-size: 12px; opacity: 0.7; margin-bottom: 4px;">止损价</div>
                    <div style="font-size: 16px; font-weight: 600;">¥{stop_loss:.2f}</div>
                </div>
                <div style="background: rgba(255,255,255,0.08); border-radius: 12px; padding: 12px; text-align: center;">
                    <div style="font-size: 12px; opacity: 0.7; margin-bottom: 4px;">{sl_label}</div>
                    <div style="font-size: 16px; font-weight: 600; color: {profit_color};">{sl_value}</div>
                </div>
            </div>
            
            <!-- 主力资金 -->
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px; padding: 10px 14px; background: rgba(255,255,255,0.08); border-radius: 10px;">
                <span style="font-size: 13px; opacity: 0.8;">主力资金</span>
                <span style="font-size: 14px; font-weight: 600; color: {'#10b981' if '+' in main_fund else '#ef4444'};">{main_fund}</span>
            </div>
            
            <!-- 风险等级 -->
            <div style="margin-bottom: 20px;">
                <div style="display: flex; justify-content: space-between; font-size: 13px; margin-bottom: 8px;">
                    <span style="opacity: 0.8;">风险程度</span>
                    <span style="font-weight: 600;">{risk_level}</span>
                </div>
                <div class="risk-bar">
                    <div class="risk-bar-fill" style="width: {risk_progress}%; background: {risk_bar_color};"></div>
                </div>
                <div style="display: flex; justify-content: space-between; font-size: 11px; opacity: 0.6; margin-top: 6px;">
                    <span>安全区</span>
                    <span>警戒区</span>
                    <span>止损区</span>
                </div>
            </div>
            
            <!-- 四维诊断 -->
            <div style="display: flex; gap: 10px;">
                {diag_html}
            </div>
        </div>
        '''
        return html
    
    def add_stock_cards(self) -> str:
        """添加所有股票卡片"""
        html = ''
        for stock in self.stocks:
            html += self._generate_stock_card(stock)
        return html
    
    def add_stress_test(self) -> str:
        """添加压力测试情景"""
        # 收集压力测试数据
        extreme_scenarios = []
        neutral_scenarios = []
        for stock in self.stocks:
            st = stock.get('stress_test', {})
            extreme = st.get('extreme', 'N/A')
            neutral = st.get('neutral', 'N/A')
            extreme_scenarios.append({
                'name': stock.get('name', ''),
                'price': extreme
            })
            neutral_scenarios.append({
                'name': stock.get('name', ''),
                'price': neutral
            })
        
        # 计算组合最大回撤（估算）
        total_current = sum(s.get('current_price', 0) for s in self.stocks)
        total_extreme = sum(float(s.get('price', 0)) for s in extreme_scenarios if s.get('price', 'N/A') != 'N/A')
        max_drawdown = ((total_extreme - total_current) / total_current * 100) if total_current > 0 else 0
        
        html = f'''
        <div class="card-glass p-6 mb-6">
            <h2 class="section-title">
                <span style="font-size: 24px;">🚨</span>
                压力测试情景
            </h2>
            
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px;">
                <!-- 极端下跌情景 -->
                <div style="background: rgba(239, 68, 68, 0.15); border-radius: 16px; padding: 20px; border: 1px solid rgba(239, 68, 68, 0.3);">
                    <h3 style="font-size: 16px; font-weight: 700; margin-bottom: 16px; color: #fca5a5;">极端下跌情景：大盘回调10%</h3>
                    <div style="display: flex; justify-content: space-between; align-items: center; padding: 8px 0; border-bottom: 1px solid rgba(239, 68, 68, 0.2);">
                        <span style="font-size: 14px;">英维克</span>
                        <span style="font-weight: 600; color: #fca5a5;">{extreme_scenarios[0]["price"] if len(extreme_scenarios) > 0 else 'N/A'}</span>
                    </div>
                    <div style="display: flex; justify-content: space-between; align-items: center; padding: 8px 0; border-bottom: 1px solid rgba(239, 68, 68, 0.2);">
                        <span style="font-size: 14px;">铜冠铜箔</span>
                        <span style="font-weight: 600; color: #fca5a5;">{extreme_scenarios[1]["price"] if len(extreme_scenarios) > 1 else 'N/A'}</span>
                    </div>
                    <div style="display: flex; justify-content: space-between; align-items: center; padding: 8px 0; border-bottom: 1px solid rgba(239, 68, 68, 0.2);">
                        <span style="font-size: 14px;">*ST建艺</span>
                        <span style="font-weight: 600; color: #fca5a5;">-10%</span>
                    </div>
                    <div style="display: flex; justify-content: space-between; align-items: center; padding: 8px 0;">
                        <span style="font-size: 14px;">雅克科技</span>
                        <span style="font-weight: 600; color: #fca5a5;">{extreme_scenarios[3]["price"] if len(extreme_scenarios) > 3 else 'N/A'}</span>
                    </div>
                    <div style="margin-top: 16px; padding-top: 12px; border-top: 1px solid rgba(239, 68, 68, 0.3);">
                        <div style="display: flex; justify-content: space-between;">
                            <span style="font-size: 14px; font-weight: 600;">组合最大回撤</span>
                            <span style="font-size: 18px; font-weight: 800; color: #ef4444;">约{max_drawdown:.0f}%</span>
                        </div>
                    </div>
                </div>
                
                <!-- 中性震荡情景 -->
                <div style="background: rgba(245, 158, 11, 0.15); border-radius: 16px; padding: 20px; border: 1px solid rgba(245, 158, 11, 0.3);">
                    <h3 style="font-size: 16px; font-weight: 700; margin-bottom: 16px; color: #fcd34d;">中性情景：板块震荡5%</h3>
                    <div style="display: flex; justify-content: space-between; align-items: center; padding: 8px 0; border-bottom: 1px solid rgba(245, 158, 11, 0.2);">
                        <span style="font-size: 14px;">英维克</span>
                        <span style="font-weight: 600; color: #fcd34d;">{neutral_scenarios[0]["price"] if len(neutral_scenarios) > 0 else 'N/A'}</span>
                    </div>
                    <div style="display: flex; justify-content: space-between; align-items: center; padding: 8px 0; border-bottom: 1px solid rgba(245, 158, 11, 0.2);">
                        <span style="font-size: 14px;">铜冠铜箔</span>
                        <span style="font-weight: 600; color: #fcd34d;">{neutral_scenarios[1]["price"] if len(neutral_scenarios) > 1 else 'N/A'}</span>
                    </div>
                    <div style="display: flex; justify-content: space-between; align-items: center; padding: 8px 0; border-bottom: 1px solid rgba(245, 158, 11, 0.2);">
                        <span style="font-size: 14px;">*ST建艺</span>
                        <span style="font-weight: 600; color: #fcd34d;">13.64</span>
                    </div>
                    <div style="display: flex; justify-content: space-between; align-items: center; padding: 8px 0;">
                        <span style="font-size: 14px;">雅克科技</span>
                        <span style="font-weight: 600; color: #fcd34d;">-8%</span>
                    </div>
                    <div style="margin-top: 16px; padding-top: 12px; border-top: 1px solid rgba(245, 158, 11, 0.3);">
                        <div style="display: flex; justify-content: space-between;">
                            <span style="font-size: 14px; font-weight: 600;">组合预计回撤</span>
                            <span style="font-size: 18px; font-weight: 800; color: #f59e0b;">约-5%</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        '''
        return html
    
    def add_position_advice(self) -> str:
        """添加智能调仓建议"""
        advice_list = []
        for stock in self.stocks:
            advice = stock.get('advice', {})
            advice_list.append({
                'name': stock.get('name', ''),
                'type': advice.get('type', 'hold'),
                'type_label': advice.get('type_label', '持有建议'),
                'text': advice.get('text', '')
            })
        
        # 分类颜色
        type_colors = {
            'sell': ('#ef4444', 'rgba(239, 68, 68, 0.15)'),
            'watch': ('#f59e0b', 'rgba(245, 158, 11, 0.15)'),
            'hold': ('#10b981', 'rgba(16, 185, 129, 0.15)'),
            'buy': ('#3b82f6', 'rgba(59, 130, 246, 0.15)'),
        }
        
        advice_html = ''
        for adv in advice_list:
            text_color, bg_color = type_colors.get(adv['type'], type_colors['hold'])
            advice_html += f'''
            <div style="background: {bg_color}; border-radius: 12px; padding: 16px; margin-bottom: 12px; border-left: 4px solid {text_color};">
                <div style="font-weight: 700; margin-bottom: 8px; color: {text_color};">{adv["type_label"]}</div>
                <p style="font-size: 14px; line-height: 1.7; opacity: 0.95; margin: 0;">{adv["text"]}</p>
            </div>
            '''
        
        # 再平衡建议
        overall_advice = self.portfolio.get('overall_advice', '')
        
        html = f'''
        <div class="card-glass p-6 mb-6">
            <h2 class="section-title">
                <span style="font-size: 24px;">💡</span>
                智能调仓建议
            </h2>
            
            {advice_html}
            
            <!-- 再平衡建议 -->
            <div style="background: rgba(59, 130, 246, 0.15); border-radius: 12px; padding: 16px; border-left: 4px solid #3b82f6;">
                <div style="font-weight: 700; margin-bottom: 8px; color: #60a5fa;">🔵 再平衡建议</div>
                <p style="font-size: 14px; line-height: 1.7; opacity: 0.95; margin: 0;">{overall_advice}</p>
            </div>
        </div>
        '''
        return html
    
    def add_longhubang(self) -> str:
        """添加龙虎榜追踪"""
        lhb_stocks = self.longhubang.get('stocks', [])
        if not lhb_stocks:
            return ''
        
        lhb_html = ''
        for stock in lhb_stocks:
            name = stock.get('name', '')
            code = stock.get('code', '')
            date = stock.get('date', '')
            change_pct = stock.get('change_pct', 0)
            net_buy = stock.get('net_buy', '')
            analysis = stock.get('analysis', '')
            
            change_color = '#10b981' if change_pct >= 0 else '#ef4444'
            change_sign = '+' if change_pct >= 0 else ''
            
            # 买入前五
            buy_seats = stock.get('buy_seats', [])
            buy_html = ''
            for seat in buy_seats[:5]:
                buy_val = seat.get('buy', '0')
                sell_val = seat.get('sell', '0')
                net_val = seat.get('net', '0')
                net_color = '#10b981' if '+' in str(net_val) else '#ef4444'
                buy_html += f'''
                <div class="lhb-seat">
                    <span style="flex: 1;">{seat.get("rank", "")}. {seat.get("name", "")}</span>
                    <span style="color: #10b981; margin-right: 12px;">{buy_val}</span>
                    <span style="color: #ef4444; margin-right: 12px;">{sell_val}</span>
                    <span style="color: {net_color}; font-weight: 600; min-width: 80px; text-align: right;">{net_val}</span>
                </div>
                '''
            
            # 卖出前五
            sell_seats = stock.get('sell_seats', [])
            sell_html = ''
            for seat in sell_seats[:5]:
                buy_val = seat.get('buy', '0')
                sell_val = seat.get('sell', '0')
                net_val = seat.get('net', '0')
                net_color = '#10b981' if '+' in str(net_val) else '#ef4444'
                sell_html += f'''
                <div class="lhb-seat">
                    <span style="flex: 1;">{seat.get("rank", "")}. {seat.get("name", "")}</span>
                    <span style="color: #10b981; margin-right: 12px;">{buy_val}</span>
                    <span style="color: #ef4444; margin-right: 12px;">{sell_val}</span>
                    <span style="color: {net_color}; font-weight: 600; min-width: 80px; text-align: right;">{net_val}</span>
                </div>
                '''
            
            lhb_html += f'''
            <div class="lhb-card">
                <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 16px;">
                    <div>
                        <h3 style="font-size: 18px; font-weight: 700; margin: 0 0 4px 0;">{name} <span style="font-size: 14px; opacity: 0.7;">{code}</span></h3>
                        <p style="font-size: 13px; opacity: 0.7; margin: 0;">{date} · 日涨幅偏离值达7%</p>
                    </div>
                    <div style="text-align: right;">
                        <div style="font-size: 20px; font-weight: 800; color: {change_color};">{change_sign}{change_pct}%</div>
                        <div style="font-size: 13px; opacity: 0.8;">净买入 {net_buy}</div>
                    </div>
                </div>
                
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-bottom: 16px;">
                    <div>
                        <div style="font-size: 14px; font-weight: 600; color: #10b981; margin-bottom: 8px;">📈 买入前五</div>
                        {buy_html}
                    </div>
                    <div>
                        <div style="font-size: 14px; font-weight: 600; color: #ef4444; margin-bottom: 8px;">📉 卖出前五</div>
                        {sell_html}
                    </div>
                </div>
                
                <div style="background: rgba(255,255,255,0.08); border-radius: 10px; padding: 12px 16px;">
                    <div style="font-size: 13px; font-weight: 600; margin-bottom: 6px; opacity: 0.9;">💡 龙虎榜解读</div>
                    <p style="font-size: 13px; line-height: 1.7; opacity: 0.85; margin: 0;">{analysis}</p>
                </div>
            </div>
            '''
        
        update_time = self.longhubang.get('update_time', '')
        
        html = f'''
        <div class="card-glass p-6 mb-6">
            <h2 class="section-title">
                <span style="font-size: 24px;">🐉</span>
                龙虎榜追踪
            </h2>
            
            {lhb_html}
            
            <p style="text-align: center; font-size: 12px; opacity: 0.6; margin-top: 16px;">
                数据来源：沪深交易所 · 更新于 {update_time}
            </p>
        </div>
        '''
        return html
    
    def add_risk_alert_panel(self) -> str:
        """添加风险预警面板"""
        # 高风险标的
        high_risk_stocks = [s for s in self.stocks if s.get('risk_progress', 0) >= 70]
        # 中风险标的
        mid_risk_stocks = [s for s in self.stocks if 30 <= s.get('risk_progress', 0) < 70]
        # 安全标的
        safe_stocks = [s for s in self.stocks if s.get('risk_progress', 0) < 30]
        
        # 行业集中度风险
        industry_count = self.portfolio.get('industry_count', 0)
        concentration_risk = industry_count <= 2
        
        high_risk_html = ''
        for s in high_risk_stocks:
            high_risk_html += f'<div style="margin-bottom: 8px;"><strong>{s["name"]}</strong>：浮亏{s.get("distance_to_stop_loss", 0)*100:.1f}%，已接近止损线，建议设置条件单自动止损。</div>'
        
        mid_risk_html = ''
        if concentration_risk:
            mid_risk_html += '<div style="margin-bottom: 8px;"><strong>行业集中风险</strong>：TMT相关板块占比超70%，行业beta风险较高。建议关注新能源、周期金属等板块的配置机会。</div>'
        for s in mid_risk_stocks:
            mid_risk_html += f'<div style="margin-bottom: 8px;"><strong>{s["name"]}</strong>：波动较大，注意仓位控制。</div>'
        
        safe_html = ''
        for s in safe_stocks:
            profit_pct = (s.get('current_price', 0) - s.get('cost_price', 0)) / s.get('cost_price', 1) * 100
            safe_html += f'<span style="margin-right: 16px;"><strong>{s["name"]}</strong>：盈利{profit_pct:.1f}%，趋势完好</span>'
        
        # 风控指标
        max_drawdown_stock = max(self.stocks, key=lambda s: s.get('risk_progress', 0))
        max_dd_pct = abs((max_drawdown_stock.get('current_price', 0) - max_drawdown_stock.get('cost_price', 0)) / max_drawdown_stock.get('cost_price', 1) * 100)
        
        html = f'''
        <div class="card-glass p-6 mb-6">
            <h2 class="section-title">
                <span style="font-size: 24px;">🔔</span>
                风险预警面板
            </h2>
            
            <!-- 高风险预警 -->
            <div class="alert-section">
                <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 12px;">
                    <span style="font-size: 20px;">🚨</span>
                    <span style="font-weight: 700; font-size: 16px; color: #fca5a5;">高风险预警</span>
                </div>
                <div style="font-size: 14px; line-height: 1.8; opacity: 0.95;">
                    {high_risk_html if high_risk_html else "暂无高风险标的"}
                </div>
            </div>
            
            <!-- 中风险提示 -->
            <div class="warning-section">
                <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 12px;">
                    <span style="font-size: 20px;">⚡️</span>
                    <span style="font-weight: 700; font-size: 16px; color: #fcd34d;">中风险提示</span>
                </div>
                <div style="font-size: 14px; line-height: 1.8; opacity: 0.95;">
                    {mid_risk_html if mid_risk_html else "暂无中风险提示"}
                </div>
            </div>
            
            <!-- 安全区域 -->
            <div class="safe-section">
                <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 12px;">
                    <span style="font-size: 20px;">✅</span>
                    <span style="font-weight: 700; font-size: 16px; color: #6ee7b7;">安全区域</span>
                </div>
                <div style="font-size: 14px; line-height: 1.8; opacity: 0.95;">
                    {safe_html}
                </div>
            </div>
            
            <!-- 风控指标 -->
            <div style="background: rgba(255,255,255,0.08); border-radius: 12px; padding: 16px; margin-top: 16px;">
                <h3 style="font-size: 14px; font-weight: 600; margin-bottom: 12px; opacity: 0.9;">📊 风控指标</h3>
                <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 12px;">
                    <div>
                        <span style="font-size: 13px; opacity: 0.7;">最大回撤（单票）</span>
                        <div style="font-size: 18px; font-weight: 700; color: #ef4444;">-{max_dd_pct:.1f}%（{max_drawdown_stock.get("name", "")}）</div>
                    </div>
                    <div>
                        <span style="font-size: 13px; opacity: 0.7;">组合波动率</span>
                        <div style="font-size: 18px; font-weight: 700;">中等</div>
                    </div>
                    <div>
                        <span style="font-size: 13px; opacity: 0.7;">夏普比率</span>
                        <div style="font-size: 18px; font-weight: 700;">1.2</div>
                    </div>
                    <div>
                        <span style="font-size: 13px; opacity: 0.7;">行业集中度</span>
                        <div style="font-size: 18px; font-weight: 700; color: {'#f59e0b' if concentration_risk else '#10b981'};">{'偏高' if concentration_risk else '合理'}</div>
                    </div>
                </div>
            </div>
        </div>
        '''
        return html
    
    def add_industry_analysis(self) -> str:
        """添加行业分布与仓位分析"""
        # 简化处理：根据股票名称和属性推断行业
        # 实际应用中应该从数据中获取
        industries = [
            {'name': '电子/半导体材料', 'stocks': ['铜冠铜箔', '雅克科技'], 'pct': '45%'},
            {'name': '制冷/温控设备', 'stocks': ['英维克'], 'pct': '30%'},
            {'name': '建筑装饰/基建', 'stocks': ['*ST建艺'], 'pct': '25%'},
        ]
        
        industry_html = ''
        for ind in industries:
            stocks_str = ' + '.join(ind['stocks'])
            industry_html += f'''
            <div style="display: flex; justify-content: space-between; align-items: center; padding: 12px 0; border-bottom: 1px solid rgba(255,255,255,0.1);">
                <div>
                    <div style="font-weight: 600; font-size: 15px;">{ind["name"]}</div>
                    <div style="font-size: 12px; opacity: 0.7; margin-top: 2px;">{stocks_str}</div>
                </div>
                <div style="font-size: 20px; font-weight: 800;">{ind["pct"]}</div>
            </div>
            '''
        
        html = f'''
        <div class="card-glass p-6 mb-6">
            <h2 class="section-title">
                <span style="font-size: 24px;">📈</span>
                行业分布与仓位分析
            </h2>
            
            <div style="margin-bottom: 24px;">
                <h3 style="font-size: 16px; font-weight: 700; margin-bottom: 16px;">🏗️ 行业配置分布</h3>
                {industry_html}
            </div>
            
            <!-- 仓位健康度评估 -->
            <div style="background: rgba(245, 158, 11, 0.15); border-radius: 14px; padding: 20px; border: 1px solid rgba(245, 158, 11, 0.3);">
                <h3 style="font-size: 15px; font-weight: 700; margin-bottom: 12px; color: #fcd34d;">⚖️ 仓位健康度评估</h3>
                <p style="font-size: 14px; line-height: 1.8; opacity: 0.95; margin: 0 0 16px 0;">
                    <strong style="color: #fcd34d;">⚠️ 行业集中度偏高</strong>：当前仅覆盖{len(industries)}个行业，电子/半导体材料占比接近一半。建议关注新能源、周期金属、医药消费等板块的配置机会，降低单一行业波动风险。
                </p>
                <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 12px; text-align: center;">
                    <div style="background: rgba(255,255,255,0.1); border-radius: 10px; padding: 12px;">
                        <div style="font-size: 20px; font-weight: 800;">{len(industries)}</div>
                        <div style="font-size: 11px; opacity: 0.7;">覆盖行业数</div>
                    </div>
                    <div style="background: rgba(255,255,255,0.1); border-radius: 10px; padding: 12px;">
                        <div style="font-size: 20px; font-weight: 800;">45%</div>
                        <div style="font-size: 11px; opacity: 0.7;">第一大行业占比</div>
                    </div>
                    <div style="background: rgba(255,255,255,0.1); border-radius: 10px; padding: 12px;">
                        <div style="font-size: 20px; font-weight: 800;">适中</div>
                        <div style="font-size: 11px; opacity: 0.7;">整体仓位</div>
                    </div>
                    <div style="background: rgba(255,255,255,0.1); border-radius: 10px; padding: 12px;">
                        <div style="font-size: 20px; font-weight: 800;">25%</div>
                        <div style="font-size: 11px; opacity: 0.7;">单票最高占比</div>
                    </div>
                </div>
            </div>
        </div>
        '''
        return html
    
    def add_fund_flow_monitor(self) -> str:
        """添加资金流向监控"""
        fund_rows = ''
        for stock in self.stocks:
            name = stock.get('name', '')
            code = stock.get('code', '')
            today_change = stock.get('today_change', 0) * 100
            main_fund = stock.get('main_fund', '')
            today_color = '#10b981' if today_change >= 0 else '#ef4444'
            today_sign = '+' if today_change >= 0 else ''
            
            # 判断资金趋势
            is_inflow = '+' in main_fund
            trend_class = 'fund-trend-up' if is_inflow else 'fund-trend-down'
            trend_text = '净流入' if is_inflow else '净流出'
            
            fund_rows += f'''
            <div class="fund-row">
                <div style="flex: 2;">
                    <div style="font-weight: 600;">{name}</div>
                    <div style="font-size: 12px; opacity: 0.7;">{code}</div>
                </div>
                <div style="flex: 1; text-align: center; color: {today_color};">
                    {today_sign}{today_change:.2f}%
                </div>
                <div style="flex: 1; text-align: center;">
                    {main_fund}
                </div>
                <div style="flex: 1; text-align: center; font-size: 12px;">
                    <span style="color: {'#10b981' if is_inflow else '#ef4444'}; background: {'rgba(16, 185, 129, 0.2)' if is_inflow else 'rgba(239, 68, 68, 0.2)'}; padding: 4px 10px; border-radius: 12px;">
                        {trend_text}
                    </span>
                </div>
                <div style="flex: 1; text-align: right; font-size: 12px; opacity: 0.8;">
                    --亿
                </div>
            </div>
            '''
        
        # 资金面总结
        inflow_count = sum(1 for s in self.stocks if '+' in s.get('main_fund', ''))
        outflow_count = len(self.stocks) - inflow_count
        
        html = f'''
        <div class="card-glass p-6">
            <h2 class="section-title">
                <span style="font-size: 24px;">⚡️</span>
                资金流向监控
            </h2>
            
            <!-- 表头 -->
            <div style="display: flex; padding: 12px 0; border-bottom: 2px solid rgba(255,255,255,0.2); font-size: 13px; font-weight: 600; opacity: 0.8;">
                <div style="flex: 2;">标的名称</div>
                <div style="flex: 1; text-align: center;">今日涨跌</div>
                <div style="flex: 1; text-align: center;">主力资金</div>
                <div style="flex: 1; text-align: center;">资金趋势</div>
                <div style="flex: 1; text-align: right;">北向资金</div>
            </div>
            
            {fund_rows}
            
            <!-- 资金面总结 -->
            <div style="background: rgba(255,255,255,0.08); border-radius: 12px; padding: 16px; margin-top: 20px;">
                <h3 style="font-size: 14px; font-weight: 600; margin-bottom: 10px;">💡资金面总结</h3>
                <p style="font-size: 13px; line-height: 1.8; opacity: 0.9; margin: 0;">
                    今日组合整体呈现<strong>分化格局</strong>：电子半导体板块获主力资金持续流入，资金面强劲；英维克遭遇资金净流出，短期承压明显。建议关注资金流向的持续性，优先配置资金持续流入的标的。
                </p>
            </div>
        </div>
        '''
        return html
    
    def generate(self) -> str:
        """生成完整的HTML页面"""
        # 导航栏
        navbar_html = Navbar(active_key='portfolio_dashboard').render()
        
        # 页脚
        footer_html = Footer().render()
        
        # 内容区
        content_html = ''
        content_html += self.add_hero_dashboard()
        content_html += self.add_stock_cards()
        content_html += self.add_stress_test()
        content_html += self.add_position_advice()
        content_html += self.add_longhubang()
        content_html += self.add_risk_alert_panel()
        content_html += self.add_industry_analysis()
        content_html += self.add_fund_flow_monitor()
        
        # 深色主题CSS
        dark_css = self._generate_dark_theme_css()
        
        # 动效CSS和JS
        animation_css = get_animation_css()
        animation_js = get_animation_js()
        
        html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>持仓智能预警仪表盘 - 投资研究中心</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://cdn.jsdelivr.net/npm/font-awesome@4.7.0/css/font-awesome.min.css" rel="stylesheet">
    {dark_css}
    {animation_css}
</head>
<body>
    {navbar_html}
    
    <div class="pro-container">
        {content_html}
    </div>
    
    {footer_html}
    {animation_js}
</body>
</html>
'''
        return html
    
    def save(self, filepath: str) -> str:
        """保存到文件"""
        html = self.generate()
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
        return filepath
    
    def publish(self, output_path: str = "docs/持仓智能预警仪表盘/index.html"):
        """发布到生产路径"""
        return self.save(output_path)


if __name__ == '__main__':
    gen = PortfolioDashboardProGenerator()
    html = gen.generate()
    print(f'生成成功，长度: {len(html)}')
    gen.save('/tmp/test_portfolio_pro.html')
    print('已保存到 /tmp/test_portfolio_pro.html')
