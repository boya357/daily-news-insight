"""
工作流监控页面生成器 - Pro版
基于Pro组件库重构，深色玻璃态风格
"""
import sys
import os
import json
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from components.pro import GlassCard
from generators.pro_base import ProGenerator


class WorkflowStatusProGenerator(ProGenerator):
    """工作流监控中心 - Pro版生成器"""
    
    data_type = "workflow"
    
    def __init__(self, data_dir: str = "data", config_dir: str = "config"):
        super().__init__(
            title="工作流监控中心",
            active_page="首页",
            footer_text="自动化工作流 · 实时监控",
            data_dir=data_dir,
            show_toc=True,
        )
        self.config_dir = config_dir
        self._load_config()
    
    def _load_config(self):
        """加载定时任务配置"""
        config_path = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            '..', '..', self.config_dir, 'schedule.json'
        )
        config_path = os.path.abspath(config_path)
        
        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                self.schedule_config = json.load(f)
        except:
            self.schedule_config = {'tasks': []}
    
    def load_data(self):
        """加载工作流状态数据"""
        super().load_data()
        
        # 工作流步骤状态（从状态文件读取，没有的话用默认值）
        self.workflow_steps = [
            {'id': 'data_collection', 'name': '数据采集', 'status': 'pending', 'description': '获取市场行情、持仓数据等', 'last_run': '-'},
            {'id': 'report_generation', 'name': '报告生成', 'status': 'pending', 'description': '生成各类分析报告', 'last_run': '-'},
            {'id': 'list_update', 'name': '列表页更新', 'status': 'pending', 'description': '更新各栏目最新列表', 'last_run': '-'},
            {'id': 'git_deploy', 'name': 'Git部署', 'status': 'pending', 'description': '提交并部署到GitHub Pages', 'last_run': '-'},
        ]
        
        # 从配置获取定时任务
        self.scheduled_tasks = self.schedule_config.get('tasks', [])
        
        # 系统状态
        self.system_status = {
            'overall': 'running',
            'last_deploy': '-',
            'uptime': '99.8%',
            'total_reports': 0,
        }
    
    def _generate_status_overview(self) -> str:
        """生成系统状态概览"""
        status_text = {
            'running': '运行正常',
            'error': '异常',
            'maintenance': '维护中',
            'pending': '待运行',
        }
        
        status = self.system_status
        current_status = status_text.get(status['overall'], '未知')
        
        content = f'''
            <h2 class="text-lg font-bold text-white mb-4">
                <span class="text-blue-400 mr-2">📊</span>系统状态
            </h2>
            <div class="grid grid-cols-2 md:grid-cols-4 gap-4">
                <div class="bg-white/5 rounded-xl p-4 text-center">
                    <div class="text-3xl mb-2">🟢</div>
                    <div class="text-xl font-bold text-white">{current_status}</div>
                    <div class="text-sm text-white/60 mt-1">整体状态</div>
                </div>
                <div class="bg-white/5 rounded-xl p-4 text-center">
                    <div class="text-3xl mb-2">📅</div>
                    <div class="text-xl font-bold text-white">{status['last_deploy']}</div>
                    <div class="text-sm text-white/60 mt-1">最后部署</div>
                </div>
                <div class="bg-white/5 rounded-xl p-4 text-center">
                    <div class="text-3xl mb-2">⏱️</div>
                    <div class="text-xl font-bold text-white">{status['uptime']}</div>
                    <div class="text-sm text-white/60 mt-1">可用率</div>
                </div>
                <div class="bg-white/5 rounded-xl p-4 text-center">
                    <div class="text-3xl mb-2">📄</div>
                    <div class="text-xl font-bold text-white">{status['total_reports']}</div>
                    <div class="text-sm text-white/60 mt-1">报告总数</div>
                </div>
            </div>
        '''
        
        return GlassCard(content=content, padding="p-6", extra_class="mb-6").render()
    
    def _generate_workflow_steps(self) -> str:
        """生成工作流步骤"""
        steps_html = ''
        
        status_icons = {
            'success': '✅',
            'running': '🔄',
            'pending': '⏳',
            'error': '❌',
        }
        
        status_border_colors = {
            'success': 'border-green-500/30 bg-green-500/10',
            'running': 'border-blue-500/30 bg-blue-500/10',
            'pending': 'border-gray-500/30 bg-gray-500/10',
            'error': 'border-red-500/30 bg-red-500/10',
        }
        
        for step in self.workflow_steps:
            icon = status_icons.get(step['status'], '⏳')
            border_class = status_border_colors.get(step['status'], status_border_colors['pending'])
            
            steps_html += f'''
            <div class="border {border_class} rounded-xl p-5 mb-3">
                <div class="flex items-center justify-between mb-2">
                    <div class="flex items-center gap-3">
                        <span class="text-2xl">{icon}</span>
                        <div>
                            <h3 class="font-bold text-white">{step['name']}</h3>
                            <p class="text-white/60 text-sm">{step['description']}</p>
                        </div>
                    </div>
                    <span class="text-xs text-white/40">
                        上次执行: {step['last_run']}
                    </span>
                </div>
            </div>
            '''
        
        content = f'''
            <h2 class="text-lg font-bold text-white mb-4" id="steps">
                <span class="text-purple-400 mr-2">⚙️</span>执行步骤
            </h2>
            {steps_html}
        '''
        
        return GlassCard(content=content, padding="p-6", extra_class="mb-6").render()
    
    def _generate_scheduled_tasks(self) -> str:
        """生成定时任务列表"""
        if not self.scheduled_tasks:
            return ''
        
        tasks_html = ''
        
        for task in self.scheduled_tasks:
            name = task.get('name', '')
            cron = task.get('cron', '')
            description = task.get('description', '')
            enabled = task.get('enabled', True)
            
            status_dot = '🟢' if enabled else '⚫'
            
            tasks_html += f'''
            <div class="flex items-center justify-between py-3 border-b border-white/10 last:border-0">
                <div class="flex items-center gap-3">
                    <span>{status_dot}</span>
                    <div>
                        <div class="font-semibold text-white">{name}</div>
                        <div class="text-sm text-white/50">{cron}</div>
                    </div>
                </div>
                <div class="text-white/70 text-sm">
                    {description}
                </div>
            </div>
            '''
        
        content = f'''
            <h2 class="text-lg font-bold text-white mb-4" id="schedules">
                <span class="text-yellow-400 mr-2">⏰</span>定时任务
            </h2>
            {tasks_html}
        '''
        
        return GlassCard(content=content, padding="p-6").render()
    
    def _content(self) -> str:
        """页面主要内容"""
        return f'''
        <div class="max-w-4xl mx-auto">
            <div class="text-center mb-10">
                <h1 class="text-3xl font-bold text-white mb-2">
                    ⚙️ 工作流监控中心
                </h1>
                <p class="text-white/70">实时监控自动化工作流运行状态</p>
            </div>
            
            {self._generate_status_overview()}
            {self._generate_workflow_steps()}
            {self._generate_scheduled_tasks()}
        </div>
        '''
    
    def publish(self, output_path: str) -> dict:
        """发布页面"""
        result = super().publish(output_path)
        return result


if __name__ == "__main__":
    generator = WorkflowStatusProGenerator()
    result = generator.publish('../../docs/workflow_status.html')
    print(f"生成结果: {result}")
