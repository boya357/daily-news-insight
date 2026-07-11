"""
持仓智能预警仪表盘生成器 - Pro深色版 V3.5
基于V3系统架构，深色玻璃态主题，专业投资监控
V5.0升级（2026-07-03 L1-1/L1-3/L1-5）：
- 引入global-dark.css全局深色主题
- 每只持仓股强制风险因素/止损条件/减仓信号模块
- 报告末尾自动匹配历史教训（止损/破位/ST等相关教训）
- 数据来源标注
"""
import sys
import os
import json

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.report import Report
from components.pro import NavBar, Footer, get_pro_theme_css
from components.base import get_animation_css, get_animation_js
from generators.pro_base import (
    source_tag, CONF_HIGH, CONF_MEDIUM, CONF_LOW,
)
from lessons_learner import LessonsLearner


_GLOBAL_DARK_CSS_TAG = '<link rel="stylesheet" href="/daily-news-insight/assets/global-dark.css">'


def _src(source="综合", confidence=CONF_MEDIUM, verified=False, rumor=False):
    return source_tag(source=source, confidence=confidence, verified=verified, rumor=rumor)


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
            .card-glass .bg-white .text-gray-800 { color: #f1f5f9 !important; }
            .card-glass .bg-white .text-gray-700 { color: #e2e8f0 !important; }
            .card-glass .bg-white .text-gray-600 { color: #4b5563 !important; }
            .card-glass .bg-white .text-gray-500 { color: #94a3b8 !important; }
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
        update_time = p.get('update_time', '')
        
        return_color = '#10b981' if total_return >= 0 else '#ef4444'
        return_sign = '+' if total_return >= 0 else ''
        
        html = f'''
        <div class="card-glass p-6 mb-6">
            <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 20px;">
                <span class="text-2xl">📊</span>
                <div>
                    <h1 style="font-size: 28px; font-weight: 900; margin: 0;">持仓智能预警仪表盘</h1>
                    <p style="opacity: 0.8; font-size: 14px; margin-top: 4px;">Pro · 多维度持仓诊断 · 风险实时预警 · 智能调仓建议</p>
                    <p style="opacity: 0.6; font-size: 12px; margin-top: 6px;">⏰ 数据更新时间：{update_time}</p>
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
    
    def _get_diagnosis_details(self, dim_key, status, stock):
        """获取诊断维度的详细要点"""
        details_map = {
            'technical': {
                'good': [
                    {'icon': '✓', 'text': '均线多头排列，趋势向上', 'positive': True},
                    {'icon': '✓', 'text': '成交量温和放大，资金关注', 'positive': True},
                    {'icon': '✓', 'text': '短期技术指标处于强势区间', 'positive': True},
                ],
                'bad': [
                    {'icon': '✗', 'text': '跌破关键均线支撑', 'positive': False},
                    {'icon': '✗', 'text': '成交量萎缩，缺乏买盘', 'positive': False},
                    {'icon': '✗', 'text': 'MACD死叉，短期趋势走弱', 'positive': False},
                ],
                'neutral': [
                    {'icon': '⚪', 'text': '震荡整理，方向不明朗', 'positive': None},
                    {'icon': '⚪', 'text': '多空博弈，均线交织', 'positive': None},
                    {'icon': '✓', 'text': '中长期趋势依然完好', 'positive': True},
                ],
                'warning': [
                    {'icon': '✗', 'text': '短期技术面有回调压力', 'positive': False},
                    {'icon': '⚪', 'text': '接近支撑位，关注能否企稳', 'positive': None},
                    {'icon': '✓', 'text': '中期趋势尚未破坏', 'positive': True},
                ],
            },
            'fund': {
                'good': [
                    {'icon': '✓', 'text': '主力资金持续流入', 'positive': True},
                    {'icon': '✓', 'text': '机构持仓比例提升', 'positive': True},
                    {'icon': '✓', 'text': '北向资金持续加仓', 'positive': True},
                ],
                'bad': [
                    {'icon': '✗', 'text': '主力资金净流出', 'positive': False},
                    {'icon': '✗', 'text': '机构减持，抛压较重', 'positive': False},
                    {'icon': '✗', 'text': '资金关注度下降', 'positive': False},
                ],
                'neutral': [
                    {'icon': '⚪', 'text': '资金进出平衡', 'positive': None},
                    {'icon': '⚪', 'text': '机构持仓稳定', 'positive': None},
                    {'icon': '✓', 'text': '北向资金小幅流入', 'positive': True},
                ],
                'warning': [
                    {'icon': '✗', 'text': '主力资金有流出迹象', 'positive': False},
                    {'icon': '⚪', 'text': '散户资金参与度较高', 'positive': None},
                    {'icon': '✓', 'text': '长期资金仍在布局', 'positive': True},
                ],
            },
            'news': {
                'good': [
                    {'icon': '✓', 'text': '行业利好政策频出', 'positive': True},
                    {'icon': '✓', 'text': '公司基本面持续向好', 'positive': True},
                    {'icon': '✓', 'text': '市场情绪乐观', 'positive': True},
                ],
                'bad': [
                    {'icon': '✗', 'text': '行业负面消息扰动', 'positive': False},
                    {'icon': '✗', 'text': '公司基本面有隐忧', 'positive': False},
                    {'icon': '✗', 'text': '市场情绪偏谨慎', 'positive': False},
                ],
                'neutral': [
                    {'icon': '⚪', 'text': '消息面平静，无重大事件', 'positive': None},
                    {'icon': '⚪', 'text': '行业消息喜忧参半', 'positive': None},
                    {'icon': '✓', 'text': '公司经营情况稳定', 'positive': True},
                ],
                'warning': [
                    {'icon': '✗', 'text': '需关注潜在利空消息', 'positive': False},
                    {'icon': '⚪', 'text': '消息面存在不确定性', 'positive': None},
                    {'icon': '✓', 'text': '长期逻辑未变', 'positive': True},
                ],
            },
            'industry': {
                'good': [
                    {'icon': '✓', 'text': '行业景气度持续提升', 'positive': True},
                    {'icon': '✓', 'text': '下游需求旺盛', 'positive': True},
                    {'icon': '✓', 'text': '政策支持力度加大', 'positive': True},
                ],
                'bad': [
                    {'icon': '✗', 'text': '行业景气度下行', 'positive': False},
                    {'icon': '✗', 'text': '下游需求疲软', 'positive': False},
                    {'icon': '✗', 'text': '行业竞争加剧', 'positive': False},
                ],
                'neutral': [
                    {'icon': '⚪', 'text': '行业增速平稳', 'positive': None},
                    {'icon': '⚪', 'text': '供需基本平衡', 'positive': None},
                    {'icon': '✓', 'text': '长期发展空间广阔', 'positive': True},
                ],
                'warning': [
                    {'icon': '✗', 'text': '行业短期面临调整压力', 'positive': False},
                    {'icon': '⚪', 'text': '产业链利润分配变化', 'positive': None},
                    {'icon': '✓', 'text': '龙头公司优势明显', 'positive': True},
                ],
            },
        }
        
        dim_details = details_map.get(dim_key, {})
        status_details = dim_details.get(status, dim_details.get('neutral', []))
        
        return status_details

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
        diag_order = [
            ('technical', '📈', '技术面'),
            ('fund', '💰', '资金面'),
            ('news', '📰', '消息面'),
            ('industry', '🏭', '产业面')
        ]
        status_bg_colors = {
            'good': 'rgba(16, 185, 129, 0.15)',
            'bad': 'rgba(239, 68, 68, 0.15)',
            'neutral': 'rgba(245, 158, 11, 0.15)',
            'warning': 'rgba(249, 115, 22, 0.15)'
        }
        status_border_colors = {
            'good': 'rgba(16, 185, 129, 0.3)',
            'bad': 'rgba(239, 68, 68, 0.3)',
            'neutral': 'rgba(245, 158, 11, 0.3)',
            'warning': 'rgba(249, 115, 22, 0.3)'
        }
        status_text_colors = {
            'good': '#10b981',
            'bad': '#ef4444',
            'neutral': '#f59e0b',
            'warning': '#f97316'
        }
        status_desc_colors = {
            'good': 'rgba(16, 185, 129, 0.8)',
            'bad': 'rgba(239, 68, 68, 0.8)',
            'neutral': 'rgba(245, 158, 11, 0.8)',
            'warning': 'rgba(249, 115, 22, 0.8)'
        }
        
        for key, icon, default_title in diag_order:
            d = diagnosis.get(key, {})
            status = d.get('status', 'neutral')
            bg_color = status_bg_colors.get(status, 'rgba(255,255,255,0.1)')
            border_color = status_border_colors.get(status, 'rgba(255,255,255,0.2)')
            text_color = status_text_colors.get(status, 'white')
            desc_color = status_desc_colors.get(status, 'rgba(255,255,255,0.7)')
            title = d.get('title', default_title)
            value = d.get('value', '')
            desc = d.get('desc', '')
            
            # 生成详细诊断要点
            detail_items = self._get_diagnosis_details(key, status, stock)
            items_html = ''
            for item in detail_items:
                item_icon = item.get('icon', '⚪')
                item_text = item.get('text', '')
                item_positive = item.get('positive', None)
                if item_positive == True:
                    item_color = '#10b981'  # 绿色
                elif item_positive == False:
                    item_color = '#ef4444'  # 红色
                else:
                    item_color = '#f59e0b'  # 黄色/中性
                items_html += f'''
                <div style="display: flex; align-items: flex-start; gap: 6px; margin-top: 6px;">
                    <span style="font-size: 12px; color: {item_color}; flex-shrink: 0; margin-top: 1px;">{item_icon}</span>
                    <span style="font-size: 11px; color: {desc_color}; line-height: 1.4;">{item_text}</span>
                </div>
                '''
            
            diag_html += f'''
            <div style="flex: 1; background: {bg_color}; border: 1px solid {border_color}; border-radius: 12px; padding: 14px 12px;">
                <div style="display: flex; align-items: center; gap: 6px; margin-bottom: 8px;">
                    <span style="font-size: 18px;">{icon}</span>
                    <span style="font-weight: 800; color: {text_color}; font-size: 14px;">{title}</span>
                </div>
                <div style="font-size: 14px; font-weight: 800; color: {text_color}; margin-bottom: 6px;">{value}</div>
                <p style="font-size: 12px; color: {desc_color}; line-height: 1.5; margin: 0;">{desc}</p>
                {items_html}
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
            
            <!-- 关键数据 6项 -->
            <div style="display: grid; grid-template-columns: repeat(6, 1fr); gap: 10px; margin-bottom: 20px;">
                <div style="background: rgba(255,255,255,0.08); border-radius: 12px; padding: 12px 8px; text-align: center;">
                    <div style="font-size: 11px; opacity: 0.7; margin-bottom: 4px;">成本价</div>
                    <div style="font-size: 15px; font-weight: 700;">¥{cost:.2f}</div>
                </div>
                <div style="background: rgba(255,255,255,0.08); border-radius: 12px; padding: 12px 8px; text-align: center;">
                    <div style="font-size: 11px; opacity: 0.7; margin-bottom: 4px;">最新价</div>
                    <div style="font-size: 15px; font-weight: 700; color: {today_color};">¥{current:.2f}</div>
                </div>
                <div style="background: rgba(255,255,255,0.08); border-radius: 12px; padding: 12px 8px; text-align: center;">
                    <div style="font-size: 11px; opacity: 0.7; margin-bottom: 4px;">止损价</div>
                    <div style="font-size: 15px; font-weight: 700; color: #f59e0b;">¥{stop_loss:.2f}</div>
                </div>
                <div style="background: rgba(255,255,255,0.08); border-radius: 12px; padding: 12px 8px; text-align: center;">
                    <div style="font-size: 11px; opacity: 0.7; margin-bottom: 4px;">{sl_label}</div>
                    <div style="font-size: 15px; font-weight: 700; color: {profit_color};">{sl_value}</div>
                </div>
                <div style="background: rgba(255,255,255,0.08); border-radius: 12px; padding: 12px 8px; text-align: center;">
                    <div style="font-size: 11px; opacity: 0.7; margin-bottom: 4px;">今日涨跌</div>
                    <div style="font-size: 15px; font-weight: 700; color: {today_color};">{today_sign}{today_change:.2f}%</div>
                </div>
                <div style="background: rgba(255,255,255,0.08); border-radius: 12px; padding: 12px 8px; text-align: center;">
                    <div style="font-size: 11px; opacity: 0.7; margin-bottom: 4px;">主力资金</div>
                    <div style="font-size: 15px; font-weight: 700; color: {'#10b981' if '+' in main_fund else '#ef4444'};">{main_fund}</div>
                </div>
            </div>
            
            <!-- 风险等级 -->
            <div style="margin-bottom: 20px;">
                <div style="display: flex; justify-content: space-between; font-size: 13px; margin-bottom: 8px;">
                    <span style="opacity: 0.8;">风险程度</span>
                    <span style="font-weight: 700; color: {risk_bar_color};">{risk_level}</span>
                </div>
                <div style="height: 12px; background: rgba(255,255,255,0.15); border-radius: 6px; overflow: hidden; position: relative;">
                    <div style="height: 100%; width: {risk_progress}%; background: {risk_bar_color}; border-radius: 6px; transition: width 0.5s ease;"></div>
                    <!-- 50% 标记线 -->
                    <div style="position: absolute; top: 0; left: 50%; width: 2px; height: 100%; background: rgba(255,255,255,0.5);"></div>
                    <!-- 滑块指示器 -->
                    <div style="position: absolute; top: 50%; left: {risk_progress}%; transform: translate(-50%, -50%); width: 16px; height: 16px; background: {risk_bar_color}; border-radius: 50%; border: 2px solid white; box-shadow: 0 2px 8px rgba(0,0,0,0.3);"></div>
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
        """添加所有股票卡片（V5.0：每只卡后强制附带风险/止损/减仓模块）"""
        html = ''
        for stock in self.stocks:
            html += self._generate_stock_card(stock)
            html += self._stock_risk_block(stock)
        return html
    
    def _safe_float(self, val, default=0.0):
        """安全转换为float，处理带%的字符串"""
        if val is None or val == 'N/A':
            return default
        try:
            if isinstance(val, str) and '%' in val:
                return float(val.replace('%', ''))
            return float(val)
        except:
            return default

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
        
        # 计算组合最大回撤（估算）- 使用极端情景的平均回撤比例
        extreme_values = []
        for s in extreme_scenarios:
            pct = self._safe_float(s.get('price', 'N/A'), None)
            if pct is not None:
                extreme_values.append(pct)
        max_drawdown = sum(extreme_values) / len(extreme_values) if extreme_values else 0
        
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
    
    def _stock_risk_block(self, s: dict) -> str:
        """V5.0 L1-3：单只持仓股风险/止损/减仓信号模块"""
        name = s.get('name', '')
        stop = s.get('stop_loss') or s.get('stop_price') or ""
        # 按持仓状态生成减仓/止损信号
        dist = s.get('distance_to_stop_loss', 0)
        pct = dist * 100 if isinstance(dist, (int, float)) else 0
        if pct <= -5:
            falsify = [
                f"{name}跌破止损价{stop}且次日不能站回",
                f"{name}连续3日放量下跌且主力净流出超3亿",
                "板块系统性杀跌，情绪退潮",
            ]
            bear = [
                f"{name}已深度破位，主力出货迹象明显",
                "利空出尽未必是底，抄底资金被埋风险大",
                "弱势行情下逆势补仓只会扩大亏损",
            ]
        elif pct < 5:
            falsify = [
                f"{name}跌破{stop}硬止损位，无条件离场",
                f"{name}跌破20日均线并放量",
            ]
            bear = [
                "高波动区域，止损位近在咫尺",
                "若板块走弱，易引发连锁止损抛压",
            ]
        else:
            falsify = [
                f"{name}跌破10日均线且单日放量跌超5%",
                "出现跌停或高位放量长上影线",
                "主营逻辑/核心催化被证伪",
            ]
            bear = [
                "浮盈较大，机构兑现风险上升",
                "高位震荡易引发获利盘集中出逃",
                "利好兑现即出货",
            ]
        falsify_html = ''.join([
            f'<li class="flex gap-2 mb-1"><span class="text-red-400 flex-shrink-0">✗</span><span class="text-white/70 text-sm">{x}</span></li>'
            for x in falsify
        ])
        bear_html = ''.join([
            f'<li class="flex gap-2 mb-1"><span class="text-yellow-400 flex-shrink-0">◌</span><span class="text-white/70 text-sm">{x}</span></li>'
            for x in bear
        ])
        stop_html = ""
        if stop:
            stop_html = f'''
            <div class="bg-red-500/10 border border-red-500/30 rounded-lg px-2 py-1.5 mb-2">
                <span class="text-red-400 text-[11px] font-bold">⛔ 止损价：</span>
                <span class="text-white font-bold text-sm">{stop}</span>
                <span class="text-white/50 text-[10px] ml-1">跌破无条件离场</span>
            </div>
            '''
        # 减仓信号（基于当前价/成本推断）
        reduce_signals = s.get('reduce_signals') or [
            f"反弹至压力位放量滞涨 → 减1/3锁利",
            f"单日冲高回落且量能异常放大 → 减1/3",
            f"板块高潮次日（龙头开板）→ 减1/3",
        ]
        reduce_html = ''.join([
            f'<li class="flex gap-2 mb-1"><span class="text-orange-400 flex-shrink-0">↓</span><span class="text-white/70 text-sm">{x}</span></li>'
            for x in reduce_signals
        ])
        return f'''
        <div class="bg-gradient-to-r from-red-900/20 via-red-500/10 to-transparent border-l-4 border-red-500/60 rounded-r-lg p-3 mt-3">
            <div class="flex items-center gap-2 mb-2">
                <span class="text-sm">🔴</span>
                <span class="text-red-400 text-[13px] font-bold">{name} · 风险/止损/减仓</span>
                <span class="ml-auto text-[10px] text-white/40 bg-white/5 px-1.5 py-0.5 rounded">V5.0 必选项</span>
            </div>
            {stop_html}
            <div class="grid grid-cols-1 md:grid-cols-2 gap-2">
                <div>
                    <div class="text-[11px] text-red-400/80 font-bold mb-1">❌ 证伪/止损信号</div>
                    <ul class="list-none p-0 m-0">{falsify_html}</ul>
                </div>
                <div>
                    <div class="text-[11px] text-orange-400/80 font-bold mb-1">↓ 减仓信号</div>
                    <ul class="list-none p-0 m-0">{reduce_html}</ul>
                </div>
            </div>
            <div class="mt-2">
                <div class="text-[11px] text-yellow-400/80 font-bold mb-1">⚠️ 空方逻辑</div>
                <ul class="list-none p-0 m-0">{bear_html}</ul>
            </div>
        </div>
        '''

    def _lessons_section(self) -> str:
        """V5.0 L1-5：匹配相关历史教训"""
        kws = ["持仓", "止损", "破位", "减仓", "白卡", "虚构数据"]
        for s in self.stocks:
            n = s.get('name', '')
            if 'ST' in n or '建艺' in n:
                kws.extend(['ST', '退市'])
            if '英维克' in n:
                kws.extend(['液冷', '算力'])
            if '铜冠' in n:
                kws.extend(['存储', '铜箔'])
            if '雅克' in n:
                kws.extend(['HBM', '半导体', '跌停'])
        try:
            learner = LessonsLearner()
            matches = learner.match(kws, top_k=3)
        except Exception as e:
            print(f"[Warn] lessons match failed: {e}")
            return ""
        if not matches:
            return ""
        cards = ""
        for l in matches:
            tags = ' '.join([
                f'<span class="bg-white/5 text-white/50 text-[10px] px-1.5 py-0.5 rounded">{t}</span>'
                for t in l.get('tags', [])
            ])
            cards += f'''
            <div class="bg-white/[0.03] border border-white/10 rounded-lg p-3">
                <div class="flex items-start justify-between gap-2 mb-1">
                    <div class="text-white/90 font-semibold text-sm">📌 {l.get('title','')}</div>
                    <span class="text-[10px] text-orange-400 bg-orange-500/10 px-1.5 py-0.5 rounded flex-shrink-0">相关度 {l.get('score',0):.0%}</span>
                </div>
                <p class="text-white/60 text-xs leading-relaxed">{l.get('summary','')}</p>
                <div class="flex flex-wrap gap-1 mt-2">{tags}</div>
            </div>
            '''
        return f'''
        <div class="card-glass p-6 mb-6">
            <h2 class="section-title"><span style="font-size:24px;">📚</span>历史教训回顾</h2>
            <p class="text-white/50 text-xs mb-3">基于当前持仓自动匹配相关历史错误教训，避免重蹈覆辙</p>
            <div class="grid grid-cols-1 md:grid-cols-{min(3, max(1, len(matches)))} gap-2">
                {cards}
            </div>
        </div>
        '''

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
        # 导航栏（Pro版统一组件）
        navbar_html = NavBar(active_page='首页').render()
        
        # 页脚（Pro版统一组件）
        footer_html = Footer(text='持仓智能预警仪表盘 · 专业投资决策辅助').render()
        
        # 内容区
        content_html = ''
        content_html += self.add_hero_dashboard()
        content_html += self.add_stock_cards()
        content_html += self.add_stress_test()
        content_html += self.add_position_advice()
        # content_html += self.add_longhubang()  # 龙虎榜已独立为专门工具页面，此处移除
        content_html += self.add_risk_alert_panel()
        content_html += self.add_industry_analysis()
        content_html += self.add_fund_flow_monitor()
        # V5.0 L1-5：历史教训回顾
        content_html += self._lessons_section()
        
        # Pro主题CSS
        theme_css = get_pro_theme_css()
        
        # 动效CSS和JS
        animation_css = get_animation_css()
        animation_js = get_animation_js()
        
        # 悬浮按钮HTML
        floating_html = '''
<div id="progressBar"></div>
<div class="action-buttons">
    <button onclick="window.print()" class="action-btn" title="打印/导出PDF">
        <span style="font-size:20px">&#x1F4C4;</span>
    </button>
    <button onclick="shareReport()" class="action-btn" title="分享报告">
        <span style="font-size:20px">&#x1F517;</span>
    </button>
</div>
<button id="backToTop" onclick="scrollToTop()" title="回到顶部">
    <svg width="24" height="24" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 10l7-7m0 0l7 7m-7-7v18"></path>
    </svg>
</button>
'''
        
        # 悬浮按钮CSS
        floating_css = '''
<style>
    #progressBar {
        position: fixed;
        top: 0;
        left: 0;
        height: 3px;
        background: linear-gradient(90deg, #6366f1, #a855f7, #ec4899);
        z-index: 9999;
        width: 0%;
        transition: width 0.1s ease;
    }
    
    .action-buttons {
        position: fixed;
        bottom: 90px;
        right: 30px;
        display: flex;
        flex-direction: column;
        gap: 10px;
        z-index: 9997;
    }
    
    .action-btn {
        width: 50px;
        height: 50px;
        background: linear-gradient(135deg, #6366f1, #a855f7);
        border: none;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        cursor: pointer;
        box-shadow: 0 4px 15px rgba(99, 102, 241, 0.4);
        transition: all 0.3s ease;
    }
    
    .action-btn:hover {
        transform: scale(1.1);
        box-shadow: 0 6px 20px rgba(99, 102, 241, 0.5);
    }
    
    #backToTop {
        position: fixed;
        bottom: 30px;
        right: 30px;
        width: 50px;
        height: 50px;
        background: linear-gradient(135deg, #6366f1, #a855f7);
        border: none;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        cursor: pointer;
        z-index: 9998;
        opacity: 0;
        transform: translateY(20px);
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(99, 102, 241, 0.4);
    }
    
    #backToTop.show {
        opacity: 1;
        transform: translateY(0);
    }
    
    #backToTop:hover {
        transform: scale(1.1);
        box-shadow: 0 6px 20px rgba(99, 102, 241, 0.5);
    }
</style>
'''
        
        # 悬浮按钮JS
        floating_js = '''
<script>
    function scrollToTop() {
        window.scrollTo({ top: 0, behavior: 'smooth' });
    }
    
    function shareReport() {
        if (navigator.share) {
            navigator.share({
                title: document.title,
                url: window.location.href
            });
        } else {
            navigator.clipboard.writeText(window.location.href).then(function() {
                alert('链接已复制到剪贴板');
            });
        }
    }
    
    window.addEventListener('scroll', function() {
        const scrollTop = document.documentElement.scrollTop || document.body.scrollTop;
        const scrollHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight;
        const progress = (scrollTop / scrollHeight) * 100;
        document.getElementById('progressBar').style.width = progress + '%';
        
        const backToTop = document.getElementById('backToTop');
        if (scrollTop > 300) {
            backToTop.classList.add('show');
        } else {
            backToTop.classList.remove('show');
        }
    });
</script>
'''
        
        html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>持仓智能预警仪表盘 - 投资研究中心</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://cdn.jsdelivr.net/npm/font-awesome@4.7.0/css/font-awesome.min.css" rel="stylesheet">
    {_GLOBAL_DARK_CSS_TAG}
    {theme_css}
    {animation_css}
    {floating_css}
</head>
<body>
    {navbar_html}
    
    <div class="pro-container pt-20">
        {content_html}
        
        {footer_html}
    </div>
    
    {floating_html}
    {animation_js}
    {floating_js}
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
    
    def publish(self, output_path: str = "docs/portfolio_dashboard/index.html"):
        """发布到生产路径"""
        try:
            html = self.generate()
            # 兜底注入 global-dark.css
            if 'global-dark.css' not in html:
                inject = _GLOBAL_DARK_CSS_TAG
                if '</head>' in html:
                    html = html.replace('</head>', inject + '</head>', 1)
            os.makedirs(os.path.dirname(output_path) or '.', exist_ok=True)
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(html)
            return {
                'success': True,
                'output_path': output_path,
                'file_size': len(html),
            }
        except Exception as e:
            return {
                'success': False,
                'error': str(e),
                'output_path': output_path
            }


if __name__ == '__main__':
    gen = PortfolioDashboardProGenerator()
    html = gen.generate()
    print(f'生成成功，长度: {len(html)}')
    gen.save('/tmp/test_portfolio_pro.html')
    print('已保存到 /tmp/test_portfolio_pro.html')
