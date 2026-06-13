"""
持仓监控仪表盘生成器 - V3.0 升级版
增加：利好/利空因素分析、风险等级、操作建议、组合诊断、预判跟踪
"""
import sys
import os
import json

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.report import Report
from components.layout import Section


class PortfolioDashboardGenerator:
    """持仓监控仪表盘生成器"""
    
    def __init__(self, data_path: str = "data/portfolio.json"):
        self.data_path = data_path
        with open(data_path, 'r', encoding='utf-8') as f:
            self.data = json.load(f)
        self.portfolio = self.data.get('portfolio', {})
        self.stocks = self.data.get('stocks', [])
        
        self.report = Report(
            title="持仓监控仪表盘",
            report_type="portfolio_dashboard",
            subtitle="实时监控 · 风险预警 · 智能诊断"
        )
        self._components = []
    
    def add_overview(self):
        """添加组合总览"""
        p = self.portfolio
        total_return = p.get('total_return', 0) * 100
        health_score = p.get('health_score', 0)
        stock_count = p.get('stock_count', 0)
        profit_count = p.get('profit_count', 0)
        loss_count = p.get('loss_count', 0)
        
        return_color = '#10b981' if total_return >= 0 else '#ef4444'
        return_sign = '+' if total_return >= 0 else ''
        
        html = f'''
        <div style="background: linear-gradient(135deg, #f0f4ff 0%, #f5f3ff 100%); 
                    padding: 28px; border-radius: 20px; 
                    border: 1px solid rgba(79, 70, 229, 0.15);">
            <div style="display: grid; grid-template-columns: 2fr 1fr 1fr 1fr; gap: 20px; align-items: center;">
                <!-- 总收益率 -->
                <div style="text-align: center;">
                    <div style="font-size: 48px; font-weight: 900; color: {return_color}; line-height: 1;">
                        {return_sign}{total_return:.1f}%
                    </div>
                    <div style="font-size: 14px; color: #6b7280; margin-top: 8px;">
                        组合总收益率
                    </div>
                </div>
                
                <!-- 健康度 -->
                <div style="text-align: center; background: rgba(255,255,255,0.7); border-radius: 16px; padding: 20px;">
                    <div style="font-size: 32px; font-weight: 800; color: #4f46e5;">{health_score}</div>
                    <div style="font-size: 12px; color: #6b7280; margin-top: 4px;">健康度评分</div>
                </div>
                
                <!-- 持仓数 -->
                <div style="text-align: center; background: rgba(255,255,255,0.7); border-radius: 16px; padding: 20px;">
                    <div style="font-size: 32px; font-weight: 800; color: #1f2937;">{stock_count}</div>
                    <div style="font-size: 12px; color: #6b7280; margin-top: 4px;">持仓标的</div>
                </div>
                
                <!-- 盈亏分布 -->
                <div style="text-align: center; background: rgba(255,255,255,0.7); border-radius: 16px; padding: 20px;">
                    <div style="display: flex; justify-content: center; gap: 12px; margin-bottom: 4px;">
                        <span style="font-size: 20px; font-weight: 700; color: #10b981;">{profit_count}盈</span>
                        <span style="font-size: 20px; font-weight: 700; color: #ef4444;">{loss_count}亏</span>
                    </div>
                    <div style="font-size: 12px; color: #6b7280;">盈亏分布</div>
                </div>
            </div>
            
            <!-- 总评 -->
            <div style="margin-top: 20px; padding: 16px 20px; background: rgba(255,255,255,0.8); border-radius: 14px;
                       border-left: 4px solid #4f46e5;">
                <div style="font-size: 13px; font-weight: 600; color: #4f46e5; margin-bottom: 6px;">
                    💡 组合诊断
                </div>
                <div style="font-size: 14px; color: #374151; line-height: 1.7;">
                    {p.get('overall_advice', '')}
                </div>
            </div>
        </div>
        '''
        
        section = Section(title="📊 组合总览", content=html, icon="chart")
        self._components.append(section)
    
    def add_stock_detail(self, stock):
        """生成单只股票的详细卡片"""
        name = stock.get('name', '')
        code = stock.get('code', '')
        cost = stock.get('cost_price', 0)
        current = stock.get('current_price', 0)
        profit_pct = (current - cost) / cost * 100
        today_change = stock.get('today_change', 0) * 100
        stop_loss = stock.get('stop_loss_price', 0)
        distance_sl = stock.get('distance_to_stop_loss', 0) * 100
        risk_level = stock.get('risk_level', '')
        risk_progress = stock.get('risk_progress', 0)
        main_fund = stock.get('main_fund', '')
        advice = stock.get('advice', '')
        diagnosis = stock.get('diagnosis', {})
        stress_test = stock.get('stress_test', {})
        
        profit_color = '#10b981' if profit_pct >= 0 else '#ef4444'
        profit_sign = '+' if profit_pct >= 0 else ''
        today_color = '#10b981' if today_change >= 0 else '#ef4444'
        today_sign = '+' if today_change >= 0 else ''
        
        # 风险进度条颜色
        if risk_progress < 50:
            risk_bar_color = '#10b981'
        elif risk_progress < 75:
            risk_bar_color = '#f59e0b'
        else:
            risk_bar_color = '#ef4444'
        
        # 诊断信息
        diag_items = []
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
                    'title': value.get('title', key),
                    'value': value.get('value', ''),
                    'desc': value.get('desc', ''),
                    'color': color
                })
        
        diag_html = ''
        for item in diag_items:
            diag_html += f'''
            <div style="text-align: center; flex: 1;">
                <div style="font-size: 14px; font-weight: 600; color: {item['color']};">{item['value']}</div>
                <div style="font-size: 11px; color: #6b7280; margin-top: 2px;">{item['title']}</div>
            </div>
            '''
        
        html = f'''
        <div style="background: white; border-radius: 18px; padding: 24px; 
                    border: 1px solid rgba(0,0,0,0.06);
                    box-shadow: 0 2px 12px rgba(0,0,0,0.04);">
            <!-- 头部 -->
            <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 20px;">
                <div>
                    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 6px;">
                        <span style="font-size: 20px; font-weight: 700; color: #1f2937;">{name}</span>
                        <span style="font-size: 12px; color: #9ca3af;">{code}</span>
                    </div>
                    <div style="display: flex; gap: 16px; font-size: 13px;">
                        <span style="color: #6b7280;">成本: <span style="color: #374151; font-weight: 500;">¥{cost:.2f}</span></span>
                        <span style="color: #6b7280;">现价: <span style="color: #374151; font-weight: 500;">¥{current:.2f}</span></span>
                    </div>
                </div>
                <div style="text-align: right;">
                    <div style="font-size: 24px; font-weight: 800; color: {profit_color};">
                        {profit_sign}{profit_pct:.1f}%
                    </div>
                    <div style="font-size: 12px; color: {today_color};">
                        今日 {today_sign}{today_change:.1f}%
                    </div>
                </div>
            </div>
            
            <!-- 多维度诊断 -->
            <div style="display: flex; gap: 10px; margin-bottom: 20px; padding: 14px; background: #f8fafc; border-radius: 12px;">
                {diag_html}
            </div>
            
            <!-- 风险预警 -->
            <div style="margin-bottom: 16px;">
                <div style="display: flex; justify-content: space-between; font-size: 12px; margin-bottom: 6px;">
                    <span style="color: #6b7280;">风险等级</span>
                    <span style="color: #374151; font-weight: 500;">{risk_level}</span>
                </div>
                <div style="width: 100%; height: 8px; background: #e5e7eb; border-radius: 4px; overflow: hidden;">
                    <div style="height: 100%; width: {risk_progress}%; background: {risk_bar_color}; border-radius: 4px;"></div>
                </div>
                <div style="display: flex; justify-content: space-between; font-size: 11px; color: #9ca3af; margin-top: 4px;">
                    <span>安全区</span>
                    <span>止损价: ¥{stop_loss:.2f} (距{distance_sl:.1f}%)</span>
                </div>
            </div>
            
            <!-- 操作建议 -->
            <div style="background: #f0fdf4; border-radius: 12px; padding: 14px 16px;
                       border-left: 3px solid #10b981;">
                <div style="font-size: 12px; font-weight: 600; color: #059669; margin-bottom: 6px;">
                    🎯 操作建议
                </div>
                <div style="font-size: 13px; color: #047857; line-height: 1.6;">
                    {advice}
                </div>
            </div>
        </div>
        '''
        
        return html
    
    def add_holdings_list(self):
        """添加持仓列表"""
        html = '<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(380px, 1fr)); gap: 20px;">'
        for stock in self.stocks:
            html += self.add_stock_detail(stock)
        html += '</div>'
        
        section = Section(title="💼 持仓明细", content=html, icon="briefcase")
        self._components.append(section)
    
    def add_risk_warnings(self):
        """添加风险预警列表"""
        high_risk = [s for s in self.stocks if s.get('risk_progress', 0) >= 70]
        
        if not high_risk:
            html = '''
            <div style="background: #f0fdf4; border-radius: 16px; padding: 24px; text-align: center;">
                <div style="font-size: 48px; margin-bottom: 12px;">✅</div>
                <div style="font-size: 16px; font-weight: 600; color: #059669;">暂无高风险预警</div>
                <div style="font-size: 13px; color: #6b7280; margin-top: 6px;">所有持仓均在安全区间内</div>
            </div>
            '''
        else:
            html = '<div style="display: flex; flex-direction: column; gap: 12px;">'
            for stock in high_risk:
                html += f'''
                <div style="background: #fef2f2; border-radius: 14px; padding: 16px 20px;
                           border: 1px solid #fecaca; display: flex; align-items: center; gap: 16px;">
                    <div style="font-size: 28px;">⚠️</div>
                    <div style="flex: 1;">
                        <div style="font-size: 15px; font-weight: 600; color: #b91c1c; margin-bottom: 4px;">
                            {stock['name']} - {stock.get('risk_level', '')}
                        </div>
                        <div style="font-size: 12px; color: #6b7280;">
                            距离止损价仅剩 {stock.get('distance_to_stop_loss', 0)*100:.1f}%，建议密切关注
                        </div>
                    </div>
                    <div style="text-align: right;">
                        <div style="font-size: 18px; font-weight: 700; color: #ef4444;">
                            {stock.get('risk_progress', 0)}%
                        </div>
                        <div style="font-size: 11px; color: #9ca3af;">风险度</div>
                    </div>
                </div>
                '''
            html += '</div>'
        
        section = Section(title="🚨 风险预警", content=html, icon="alert-triangle")
        self._components.append(section)
    
    def add_operation_plan(self):
        """添加明日操作计划"""
        # 基于持仓数据生成操作要点
        key_points = []
        
        for stock in self.stocks:
            name = stock['name']
            risk = stock.get('risk_progress', 0)
            profit = (stock.get('current_price', 0) - stock.get('cost_price', 0)) / stock.get('cost_price', 1) * 100
            
            if risk >= 70:
                key_points.append(f"<strong>{name}</strong>：风险度较高，接近止损线，建议设置止损单，若有效跌破立即止损")
            elif profit > 30:
                key_points.append(f"<strong>{name}</strong>：盈利丰厚，建议分批止盈，锁定部分利润")
            elif profit > 10:
                key_points.append(f"<strong>{name}</strong>：盈利态势良好，持有为主，关注能否突破前高")
            elif profit > -10:
                key_points.append(f"<strong>{name}</strong>：小幅波动，耐心持有，等待催化")
            else:
                key_points.append(f"<strong>{name}</strong>：浮亏较大，关注支撑位，若基本面无变化可考虑补仓")
        
        html = '<div style="background: white; padding: 24px; border-radius: 18px; border: 1px solid rgba(0,0,0,0.06);">'
        html += '<div style="font-size: 16px; font-weight: 700; color: #1f2937; margin-bottom: 16px;">📋 明日操作要点</div>'
        html += '<ol style="margin: 0; padding-left: 20px;">'
        for point in key_points:
            html += f'<li style="font-size: 14px; color: #374151; line-height: 1.8; margin-bottom: 8px;">{point}</li>'
        html += '</ol></div>'
        
        section = Section(title="🎯 操作计划", content=html, icon="target")
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
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
        return filepath
    
    def publish(self, output_path: str = "docs/持仓监控/index.html"):
        """发布"""
        self.save(output_path)
        print(f'✓ 持仓监控仪表盘已发布: {output_path}')
        return output_path


if __name__ == '__main__':
    gen = PortfolioDashboardGenerator()
    gen.add_overview()
    gen.add_holdings_list()
    gen.add_risk_warnings()
    gen.add_operation_plan()
    gen.publish()
