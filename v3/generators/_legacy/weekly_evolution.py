"""
每周进化报告生成器 - V1.0
认知飞轮的核心：记录每一周的预判验证、错误复盘、方法论升级
"""
import sys
import os
import json
from datetime import datetime, timedelta

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.report import Report
from components.layout import Section


class WeeklyEvolutionGenerator:
    """每周进化报告生成器"""
    
    def __init__(self, predictions_path: str = "data/predictions.json"):
        with open(predictions_path, 'r', encoding='utf-8') as f:
            self.pred_data = json.load(f)
        
        self.system_info = self.pred_data.get('system_info', {})
        self.pending = self.pred_data.get('pending_predictions', [])
        self.history = self.pred_data.get('history_records', [])
        
        self.report = Report(
            title="系统周度进化报告",
            report_type="weekly_evolution",
            subtitle="认知飞轮 · 持续进化 · 第1期"
        )
        self._components = []
    
    def add_week_summary(self):
        """本周进化总览"""
        total = self.system_info.get('total_predictions', 0)
        correct = self.system_info.get('correct_count', 0)
        wrong = self.system_info.get('wrong_count', 0)
        accuracy = self.system_info.get('accuracy', '0%')
        streak = self.system_info.get('streak', 0)
        level = self.system_info.get('analyst_level', 'C')
        
        accuracy_num = float(accuracy.replace('%', ''))
        
        # 进化速度评估
        if accuracy_num >= 70:
            evolution_level = '快速进化中 🚀'
        elif accuracy_num >= 60:
            evolution_level = '稳步提升 📈'
        elif accuracy_num >= 50:
            evolution_level = '缓慢爬坡 🐢'
        else:
            evolution_level = '需要反思 🤔'
        
        html = f'''
        <div style="background: linear-gradient(135deg, #f0f4ff 0%, #f5f3ff 100%); 
                    padding: 32px; border-radius: 24px; 
                    border: 1px solid rgba(79, 70, 229, 0.15);">
            <div style="text-align: center; margin-bottom: 28px;">
                <div style="font-size: 48px; margin-bottom: 12px;">🧠</div>
                <h1 style="font-size: 28px; font-weight: 800; color: #1f2937; margin: 0 0 8px 0;">
                    系统周度进化报告
                </h1>
                <div style="font-size: 15px; color: #6b7280;">认知飞轮 · 持续迭代 · 每周复盘</div>
            </div>
            
            <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px; margin-bottom: 24px;">
                <div style="background: white; border-radius: 16px; padding: 20px; text-align: center;
                           box-shadow: 0 2px 8px rgba(0,0,0,0.04);">
                    <div style="font-size: 32px; font-weight: 800; color: #4f46e5;">{accuracy}</div>
                    <div style="font-size: 12px; color: #6b7280; margin-top: 6px;">预判准确率</div>
                </div>
                <div style="background: white; border-radius: 16px; padding: 20px; text-align: center;
                           box-shadow: 0 2px 8px rgba(0,0,0,0.04);">
                    <div style="font-size: 32px; font-weight: 800; color: #10b981;">{correct}</div>
                    <div style="font-size: 12px; color: #6b7280; margin-top: 6px;">正确预判</div>
                </div>
                <div style="background: white; border-radius: 16px; padding: 20px; text-align: center;
                           box-shadow: 0 2px 8px rgba(0,0,0,0.04);">
                    <div style="font-size: 32px; font-weight: 800; color: #ef4444;">{wrong}</div>
                    <div style="font-size: 12px; color: #6b7280; margin-top: 6px;">错误预判</div>
                </div>
                <div style="background: white; border-radius: 16px; padding: 20px; text-align: center;
                           box-shadow: 0 2px 8px rgba(0,0,0,0.04);">
                    <div style="font-size: 32px; font-weight: 800; color: #f59e0b;">{streak}</div>
                    <div style="font-size: 12px; color: #6b7280; margin-top: 6px;">连胜场次</div>
                </div>
            </div>
            
            <div style="background: rgba(255,255,255,0.8); border-radius: 16px; padding: 20px; text-align: center;">
                <div style="font-size: 14px; color: #6b7280; margin-bottom: 8px;">分析师等级</div>
                <div style="font-size: 24px; font-weight: 800; color: #4f46e5; margin-bottom: 4px;">{level}级</div>
                <div style="font-size: 13px; color: #10b981;">{evolution_level}</div>
            </div>
        </div>
        '''
        
        section = Section(title="📊 本周进化总览", content=html, icon="chart")
        self._components.append(section)
    
    def add_prediction_review(self):
        """预判复盘"""
        # 正确案例
        correct = [h for h in self.history if h.get('result') == '正确']
        # 错误案例
        wrong = [h for h in self.history if h.get('result') == '错误']
        
        html = '<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px;">'
        
        # 成功经验
        html += '''
        <div style="background: #f0fdf4; border-radius: 18px; padding: 24px; border: 1px solid #bbf7d0;">
            <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 16px;">
                <span style="font-size: 24px;">✅</span>
                <span style="font-size: 18px; font-weight: 700; color: #059669;">成功经验</span>
            </div>
        '''
        
        if correct:
            for idx, item in enumerate(correct[:3]):
                html += f'''
                <div style="background: white; border-radius: 12px; padding: 14px; margin-bottom: 12px;">
                    <div style="font-size: 14px; font-weight: 600; color: #166534; margin-bottom: 6px;">
                        {item.get('title', '')}
                    </div>
                    <div style="font-size: 12px; color: #6b7280; line-height: 1.6;">
                        {item.get('description', '')}
                    </div>
                    <div style="display: flex; gap: 12px; margin-top: 8px; font-size: 11px;">
                        <span style="color: #10b981;">{item.get('type', '')}</span>
                        <span style="color: #f59e0b;">{item.get('price_change', '')}</span>
                    </div>
                </div>
                '''
        else:
            html += '<div style="text-align: center; color: #6b7280; font-size: 14px;">暂无成功案例</div>'
        
        html += '</div>'
        
        # 错误教训
        html += '''
        <div style="background: #fef2f2; border-radius: 18px; padding: 24px; border: 1px solid #fecaca;">
            <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 16px;">
                <span style="font-size: 24px;">❌</span>
                <span style="font-size: 18px; font-weight: 700; color: #dc2626;">错误教训</span>
            </div>
        '''
        
        if wrong:
            for idx, item in enumerate(wrong[:3]):
                reason = item.get('wrong_reason', '待分析')
                html += f'''
                <div style="background: white; border-radius: 12px; padding: 14px; margin-bottom: 12px;">
                    <div style="font-size: 14px; font-weight: 600; color: #991b1b; margin-bottom: 6px;">
                        {item.get('title', '')}
                    </div>
                    <div style="font-size: 12px; color: #6b7280; line-height: 1.6;">
                        {item.get('description', '')}
                    </div>
                    <div style="margin-top: 8px; padding: 8px 12px; background: #fef2f2; border-radius: 8px;">
                        <div style="font-size: 11px; font-weight: 600; color: #dc2626; margin-bottom: 2px;">错误原因</div>
                        <div style="font-size: 11px; color: #6b7280; line-height: 1.5;">{reason}</div>
                    </div>
                </div>
                '''
        else:
            html += '<div style="text-align: center; color: #6b7280; font-size: 14px;">暂无错误记录</div>'
        
        html += '</div></div>'
        
        section = Section(title="🔍 本周预判复盘", content=html, icon="search")
        self._components.append(section)
    
    def add_methodology_upgrade(self):
        """方法论升级"""
        upgrades = [
            {
                'title': '题材强度评分模型优化',
                'description': '新增「筹码集中度」和「机构持仓比例」两个维度，提升对机构抱团股的识别准确率',
                'impact': '预计提升准确率 5-8%',
                'status': '已上线'
            },
            {
                'title': '情绪指标权重调整',
                'description': '根据近期市场风格变化，调整了市场情绪在整体评分中的权重，从25%降至20%',
                'impact': '降低情绪扰动影响',
                'status': '已上线'
            },
            {
                'title': '催化事件时间窗口优化',
                'description': '优化了事件驱动型预判的时间窗口计算，从固定T+3改为根据事件类型动态调整',
                'impact': '提升事件类预判时效性',
                'status': '测试中'
            },
        ]
        
        html = '<div style="display: flex; flex-direction: column; gap: 14px;">'
        for up in upgrades:
            status_color = '#10b981' if up['status'] == '已上线' else '#f59e0b'
            html += f'''
            <div style="background: white; border-radius: 16px; padding: 20px; 
                       border: 1px solid rgba(0,0,0,0.06);
                       box-shadow: 0 2px 8px rgba(0,0,0,0.04);">
                <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 10px;">
                    <div style="font-size: 16px; font-weight: 600; color: #1f2937;">
                        {up['title']}
                    </div>
                    <span style="padding: 4px 10px; border-radius: 10px; font-size: 11px; font-weight: 600;
                               background: {status_color}20; color: {status_color};">
                        {up['status']}
                    </span>
                </div>
                <div style="font-size: 13px; color: #4b5563; line-height: 1.7; margin-bottom: 10px;">
                    {up['description']}
                </div>
                <div style="font-size: 12px; color: #10b981; font-weight: 500;">
                    📈 预期影响：{up['impact']}
                </div>
            </div>
            '''
        html += '</div>'
        
        section = Section(title="⚙️ 方法论升级", content=html, icon="settings")
        self._components.append(section)
    
    def add_next_week_outlook(self):
        """下周展望"""
        html = '''
        <div style="background: linear-gradient(135deg, #f0fdf4 0%, #ecfdf5 100%); 
                    padding: 24px; border-radius: 18px; border: 1px solid #a7f3d0;">
            <div style="font-size: 16px; font-weight: 700; color: #047857; margin-bottom: 16px;">
                🚀 下周进化目标
            </div>
            <ol style="margin: 0; padding-left: 20px; color: #065f46; font-size: 14px; line-height: 2;">
                <li>完善行业轮动模型，提升板块切换预判准确率</li>
                <li>新增基本面财务健康度评分维度</li>
                <li>优化止损策略，加入动态止损算法</li>
                <li>积累更多预判样本，向A级分析师迈进</li>
            </ol>
        </div>
        
        <div style="margin-top: 16px; background: #fffbeb; padding: 20px; border-radius: 16px; border: 1px solid #fde68a;">
            <div style="font-size: 14px; font-weight: 600; color: #92400e; margin-bottom: 10px;">
                💡 核心思考
            </div>
            <p style="font-size: 13px; color: #78350f; line-height: 1.8; margin: 0;">
                投资是一场认知的马拉松。每一次预判都是对认知的检验，每一次错误都是进化的养分。
                坚持复盘、持续迭代，让系统在实战中不断进化，最终形成稳定的投资决策框架。
            </p>
        </div>
        '''
        
        section = Section(title="🎯 下周展望", content=html, icon="target")
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
    
    def publish(self, output_path: str = "docs/weekly-evolution/index.html"):
        """发布"""
        self.save(output_path)
        print(f'✓ 周度进化报告已发布: {output_path}')
        return output_path


if __name__ == '__main__':
    gen = WeeklyEvolutionGenerator()
    gen.add_week_summary()
    gen.add_prediction_review()
    gen.add_methodology_upgrade()
    gen.add_next_week_outlook()
    gen.publish()
