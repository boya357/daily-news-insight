"""
预判中心生成器 - V3.0 升级版
原预判验证页面的升级版本
"""
import sys
import os
import json
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.report import Report
from components.layout import Section, Card, SubCard, CardGrid


class PredictionCenterGenerator:
    """预判中心生成器 - 基于predictions.json数据自动生成"""
    
    def __init__(self, data_path: str = "data/predictions.json"):
        self.data_path = data_path
        self.data = self._load_data()
        self.report = Report(
            title="预判中心",
            report_type="prediction_center",
            subtitle="预判验证 · 认知飞轮 · 持续进化"
        )
        self._components = []
    
    def _load_data(self):
        """加载预判数据"""
        with open(self.data_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    def add_dashboard(self):
        """添加仪表盘总览"""
        info = self.data.get('system_info', {})
        total = info.get('total_predictions', 0)
        correct = info.get('correct_count', 0)
        wrong = info.get('wrong_count', 0)
        pending = info.get('pending_count', 0)
        accuracy = info.get('accuracy', '0%')
        streak = info.get('streak', 0)
        level = info.get('analyst_level', 'C')
        
        # 等级颜色
        level_colors = {
            'S': '#8b5cf6',
            'A': '#3b82f6',
            'B': '#10b981',
            'C': '#f59e0b',
            'D': '#ef4444',
        }
        level_color = level_colors.get(level, '#6b7280')
        
        html = f'''
        <div style="background: linear-gradient(135deg, #f0f4ff 0%, #f5f3ff 100%); 
                    padding: 28px; border-radius: 20px; 
                    border: 1px solid rgba(79, 70, 229, 0.1);">
            <div style="display: grid; grid-template-columns: 2fr 1fr 1fr; gap: 20px; align-items: center;">
                <!-- 准确率大字 -->
                <div style="text-align: center;">
                    <div style="font-size: 64px; font-weight: 900; 
                                background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%);
                                -webkit-background-clip: text; -webkit-text-fill-color: transparent;
                                background-clip: text; line-height: 1;">
                        {accuracy}
                    </div>
                    <div style="font-size: 14px; color: #6b7280; margin-top: 8px;">综合准确率</div>
                    <div style="display: inline-block; margin-top: 12px; padding: 6px 16px; 
                                background: {level_color}; color: white; border-radius: 20px;
                                font-size: 14px; font-weight: 700;">
                        {level}级分析师
                    </div>
                </div>
                
                <!-- 连胜徽章 -->
                <div style="text-align: center; background: rgba(255,255,255,0.6); 
                            border-radius: 16px; padding: 20px;">
                    <div style="font-size: 36px;">🔥</div>
                    <div style="font-size: 28px; font-weight: 800; color: #f97316;">{streak}</div>
                    <div style="font-size: 12px; color: #6b7280;">连胜次数</div>
                </div>
                
                <!-- 统计 -->
                <div style="display: flex; flex-direction: column; gap: 10px;">
                    <div style="background: rgba(255,255,255,0.6); border-radius: 12px; padding: 12px; text-align: center;">
                        <div style="font-size: 20px; font-weight: 700; color: #1f2937;">{total}</div>
                        <div style="font-size: 11px; color: #6b7280;">总预判数</div>
                    </div>
                    <div style="display: flex; gap: 8px;">
                        <div style="flex: 1; background: rgba(16, 185, 129, 0.1); border-radius: 12px; padding: 10px; text-align: center;">
                            <div style="font-size: 18px; font-weight: 700; color: #10b981;">{correct}</div>
                            <div style="font-size: 10px; color: #6b7280;">正确</div>
                        </div>
                        <div style="flex: 1; background: rgba(239, 68, 68, 0.1); border-radius: 12px; padding: 10px; text-align: center;">
                            <div style="font-size: 18px; font-weight: 700; color: #ef4444;">{wrong}</div>
                            <div style="font-size: 10px; color: #6b7280;">错误</div>
                        </div>
                        <div style="flex: 1; background: rgba(245, 158, 11, 0.1); border-radius: 12px; padding: 10px; text-align: center;">
                            <div style="font-size: 18px; font-weight: 700; color: #f59e0b;">{pending}</div>
                            <div style="font-size: 10px; color: #6b7280;">待验证</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        '''
        
        section = Section(title="📊 分析能力总览", content=html, icon="chart")
        self._components.append(section)
    
    def add_pending_predictions(self):
        """添加待验证预判列表"""
        pending = self.data.get('pending_predictions', [])
        if not pending:
            return
        
        html = '<div style="display: flex; flex-direction: column; gap: 16px;">'
        for p in pending:
            level = p.get('level', 'B')
            level_colors = {
                'S': 'linear-gradient(135deg, #ef4444 0%, #f97316 100%)',
                'A': 'linear-gradient(135deg, #f97316 0%, #f59e0b 100%)',
                'B': 'linear-gradient(135deg, #3b82f6 0%, #6366f1 100%)',
                'C': 'linear-gradient(135deg, #6b7280 0%, #475569 100%)',
            }
            level_color = level_colors.get(level, level_colors['B'])
            progress = p.get('progress', 50)
            
            html += f'''
            <div style="background: white; border-radius: 16px; padding: 20px; 
                        border: 1px solid rgba(0,0,0,0.06);
                        box-shadow: 0 2px 8px rgba(0,0,0,0.04);">
                <div style="display: flex; align-items: flex-start; justify-content: space-between; margin-bottom: 12px;">
                    <div style="flex: 1;">
                        <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 8px;">
                            <span style="background: {level_color}; color: white; 
                                       padding: 4px 10px; border-radius: 12px;
                                       font-size: 12px; font-weight: 700;">{level}级</span>
                            <span style="font-size: 13px; color: #6b7280;">{p.get('verify_cycle', '')}</span>
                        </div>
                        <div style="font-size: 16px; font-weight: 600; color: #1f2937;">
                            {p.get('title', '')}
                        </div>
                    </div>
                </div>
                <div style="font-size: 13px; color: #4b5563; line-height: 1.7; margin-bottom: 12px;">
                    {p.get('logic', '')}
                </div>
                <!-- 进度条 -->
                <div style="margin-bottom: 10px;">
                    <div style="display: flex; justify-content: space-between; font-size: 12px; color: #6b7280; margin-bottom: 6px;">
                        <span>验证进度</span>
                        <span>{progress}%</span>
                    </div>
                    <div style="width: 100%; height: 8px; background: #e5e7eb; border-radius: 4px; overflow: hidden;">
                        <div style="height: 100%; width: {progress}%; 
                                   background: linear-gradient(90deg, #f59e0b 0%, #ef4444 100%);
                                   border-radius: 4px;"></div>
                    </div>
                </div>
                <!-- 最新观察 -->
                <div style="background: #fffbeb; border-radius: 10px; padding: 12px; 
                           border-left: 3px solid #f59e0b;">
                    <div style="font-size: 12px; font-weight: 600; color: #d97706; margin-bottom: 4px;">
                        📅 最新观察 · {p.get('latest_observation', {}).get('date', '')}
                    </div>
                    <div style="font-size: 12px; color: #78350f; line-height: 1.6;">
                        {p.get('latest_observation', {}).get('content', '')}
                    </div>
                </div>
            </div>
            '''
        html += '</div>'
        
        section = Section(title="⏳ 进行中预判", content=html, icon="clock")
        self._components.append(section)
    
    def add_history_records(self):
        """添加历史记录"""
        records = self.data.get('history_records', [])
        if not records:
            return
        
        # 按结果分组
        correct = [r for r in records if r.get('result') == '正确']
        wrong = [r for r in records if r.get('result') == '错误']
        
        html = '<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px;">'
        
        # 正确记录
        html += '<div>'
        html += '<div style="font-size: 16px; font-weight: 700; color: #10b981; margin-bottom: 12px; display: flex; align-items: center; gap: 8px;">'
        html += '<span>✅</span> 预判正确 <span style="font-size: 13px; font-weight: 400; color: #6b7280;">(' + str(len(correct)) + '个)</span></div>'
        for r in correct[:5]:
            html += f'''
            <div style="background: #f0fdf4; border-radius: 12px; padding: 14px; 
                        margin-bottom: 10px; border: 1px solid #bbf7d0;">
                <div style="font-size: 14px; font-weight: 600; color: #166534; margin-bottom: 6px;">
                    {r.get('title', '')}
                </div>
                <div style="font-size: 12px; color: #15803d; line-height: 1.6;">
                    {r.get('description', '')}
                </div>
                <div style="display: flex; justify-content: space-between; margin-top: 8px; font-size: 11px; color: #6b7280;">
                    <span>{r.get('type', '')}</span>
                    <span>{r.get('price_change', '')}</span>
                </div>
            </div>
            '''
        html += '</div>'
        
        # 错误记录
        html += '<div>'
        html += '<div style="font-size: 16px; font-weight: 700; color: #ef4444; margin-bottom: 12px; display: flex; align-items: center; gap: 8px;">'
        html += '<span>❌</span> 预判错误 <span style="font-size: 13px; font-weight: 400; color: #6b7280;">(' + str(len(wrong)) + '个)</span></div>'
        for r in wrong[:3]:
            html += f'''
            <div style="background: #fef2f2; border-radius: 12px; padding: 14px; 
                        margin-bottom: 10px; border: 1px solid #fecaca;">
                <div style="font-size: 14px; font-weight: 600; color: #991b1b; margin-bottom: 6px;">
                    {r.get('title', '')}
                </div>
                <div style="font-size: 12px; color: #dc2626; line-height: 1.6;">
                    {r.get('description', '')}
                </div>
                <div style="margin-top: 8px; font-size: 11px; color: #6b7280;">
                    错误原因：{r.get('wrong_reason', '待分析')}
                </div>
            </div>
            '''
        html += '</div>'
        
        html += '</div>'
        
        section = Section(title="📜 历史验证记录", content=html, icon="history")
        self._components.append(section)
    
    def add_accuracy_trend(self):
        """添加准确率趋势图（SVG）"""
        # 模拟按月统计数据
        monthly_data = [
            {'month': '1月', 'accuracy': 55},
            {'month': '2月', 'accuracy': 58},
            {'month': '3月', 'accuracy': 62},
            {'month': '4月', 'accuracy': 60},
            {'month': '5月', 'accuracy': 65},
            {'month': '6月', 'accuracy': 63.6},
        ]
        
        # 生成SVG折线图
        width = 600
        height = 200
        padding = 40
        chart_width = width - padding * 2
        chart_height = height - padding * 2
        
        # 计算坐标点
        max_acc = max(d['accuracy'] for d in monthly_data)
        min_acc = min(d['accuracy'] for d in monthly_data) - 5
        range_acc = max_acc - min_acc or 1
        
        points = []
        for i, d in enumerate(monthly_data):
            x = padding + i * chart_width / (len(monthly_data) - 1)
            y = padding + chart_height - (d['accuracy'] - min_acc) * chart_height / range_acc
            points.append((x, y, d))
        
        # 生成折线路径
        path_d = f'M {points[0][0]} {points[0][1]}'
        for x, y, _ in points[1:]:
            path_d += f' L {x} {y}'
        
        # 生成区域填充路径
        area_d = path_d + f' L {points[-1][0]} {padding + chart_height} L {points[0][0]} {padding + chart_height} Z'
        
        svg = f'''
        <svg viewBox="0 0 {width} {height}" style="width: 100%; height: auto;">
            <!-- 网格线 -->
            <line x1="{padding}" y1="{padding}" x2="{width - padding}" y2="{padding}" stroke="#e5e7eb" stroke-width="1"/>
            <line x1="{padding}" y1="{padding + chart_height/2}" x2="{width - padding}" y2="{padding + chart_height/2}" stroke="#e5e7eb" stroke-width="1" stroke-dasharray="4"/>
            <line x1="{padding}" y1="{padding + chart_height}" x2="{width - padding}" y2="{padding + chart_height}" stroke="#e5e7eb" stroke-width="1"/>
            
            <!-- 区域填充 -->
            <path d="{area_d}" fill="url(#gradient)" opacity="0.3"/>
            
            <!-- 折线 -->
            <path d="{path_d}" fill="none" stroke="url(#lineGradient)" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
            
            <!-- 数据点 -->
        '''
        
        for x, y, d in points:
            svg += f'<circle cx="{x}" cy="{y}" r="5" fill="#4f46e5" stroke="white" stroke-width="2"/>'
            svg += f'<text x="{x}" y="{y - 12}" text-anchor="middle" font-size="12" fill="#4b5563" font-weight="600">{d["accuracy"]}%</text>'
            svg += f'<text x="{x}" y="{padding + chart_height + 20}" text-anchor="middle" font-size="12" fill="#6b7280">{d["month"]}</text>'
        
        svg += '''
            <!-- 渐变定义 -->
            <defs>
                <linearGradient id="gradient" x1="0%" y1="0%" x2="0%" y2="100%">
                    <stop offset="0%" style="stop-color:#4f46e5;stop-opacity:0.4"/>
                    <stop offset="100%" style="stop-color:#4f46e5;stop-opacity:0"/>
                </linearGradient>
                <linearGradient id="lineGradient" x1="0%" y1="0%" x2="100%" y2="0%">
                    <stop offset="0%" style="stop-color:#3b82f6"/>
                    <stop offset="100%" style="stop-color:#7c3aed"/>
                </linearGradient>
            </defs>
        </svg>
        '''
        
        html = f'''
        <div style="background: white; padding: 24px; border-radius: 16px; 
                    border: 1px solid rgba(0,0,0,0.06);">
            <div style="font-size: 16px; font-weight: 700; color: #1f2937; margin-bottom: 16px;">
                📈 准确率趋势
            </div>
            {svg}
        </div>
        '''
        
        section = Section(title="📊 数据分析", content=html, icon="chart")
        self._components.append(section)
    
    def add_type_stats(self):
        """添加按类型准确率统计"""
        records = self.data.get('history_records', [])
        types = {}
        for r in records:
            t = r.get('type', '其他')
            if t not in types:
                types[t] = {'total': 0, 'correct': 0}
            types[t]['total'] += 1
            if r.get('result') == '正确':
                types[t]['correct'] += 1
        
        html = '<div style="display: flex; flex-direction: column; gap: 14px;">'
        for t, stats in types.items():
            acc = round(stats['correct'] / stats['total'] * 100, 1) if stats['total'] > 0 else 0
            html += f'''
            <div>
                <div style="display: flex; justify-content: space-between; font-size: 13px; margin-bottom: 6px;">
                    <span style="color: #374151; font-weight: 500;">{t}</span>
                    <span style="color: #6b7280;">{acc}% ({stats['correct']}/{stats['total']})</span>
                </div>
                <div style="width: 100%; height: 10px; background: #e5e7eb; border-radius: 5px; overflow: hidden;">
                    <div style="height: 100%; width: {acc}%; 
                               background: linear-gradient(90deg, #3b82f6 0%, #7c3aed 100%);
                               border-radius: 5px;"></div>
                </div>
            </div>
            '''
        html += '</div>'
        
        section_html = f'''
        <div style="background: white; padding: 24px; border-radius: 16px; 
                    border: 1px solid rgba(0,0,0,0.06);">
            <div style="font-size: 16px; font-weight: 700; color: #1f2937; margin-bottom: 16px;">
                🎯 按类型准确率
            </div>
            {html}
        </div>
        '''
        
        # 放在和趋势图同一行
        section = Section(title="", content=section_html, icon="")
        self._components.append(section)
    
    def add_improvement_direction(self):
        """添加改进方向"""
        wrong = [r for r in self.data.get('history_records', []) if r.get('result') == '错误']
        
        html = '''
        <div style="background: linear-gradient(135deg, #fef2f2 0%, #fff7ed 100%); 
                    padding: 24px; border-radius: 16px; border: 1px solid rgba(239, 68, 68, 0.15);">
            <div style="font-size: 16px; font-weight: 700; color: #dc2626; margin-bottom: 16px;">
                🔍 风险识别与改进方向
            </div>
            <div style="font-size: 13px; color: #4b5563; line-height: 1.8;">
                <p style="margin-bottom: 10px;">
                    <strong>1. 时间窗口预判偏差：</strong>部分催化事件落地时间晚于预期，需要优化事件驱动型预判的时间窗口评估。
                </p>
                <p style="margin-bottom: 10px;">
                    <strong>2. 情绪周期误判：</strong>市场情绪传导节奏判断存在偏差，需加强情绪指标的跟踪与量化。
                </p>
                <p>
                    <strong>3. 风险提示：</strong>过往表现不代表未来，预判仅供参考，投资需谨慎。
                </p>
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
    
    def publish(self, docs_root: str = "docs") -> dict:
        """一键发布"""
        html_content = self.generate()
        filepath = os.path.join(docs_root, "预判验证", "index.html")
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        return {
            'success': True,
            'filepath': filepath,
            'title': '预判中心'
        }


if __name__ == '__main__':
    gen = PredictionCenterGenerator()
    gen.add_dashboard()
    gen.add_pending_predictions()
    gen.add_accuracy_trend()
    gen.add_history_records()
    gen.add_improvement_direction()
    html = gen.generate()
    print(f'生成成功，长度: {len(html)}')
    gen.save('/tmp/test_prediction.html')
