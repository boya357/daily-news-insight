"""
持仓智能预警仪表盘生成器 - 经典手动版
基于原始手动版本的视觉风格，1:1还原设计
使用Jinja2模板引擎，数据驱动渲染
"""
import sys
import os
import json
from jinja2 import Environment, FileSystemLoader

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class PortfolioDashboardClassicGenerator:
    """持仓智能预警仪表盘 - 经典手动版生成器
    
    完全复刻原始手动版本的视觉风格和布局
    """
    
    def __init__(self, data_path: str = "data/portfolio.json"):
        self.data_path = data_path
        self._load_data()
        self._setup_template()
    
    def _load_data(self):
        """加载持仓数据"""
        with open(self.data_path, 'r', encoding='utf-8') as f:
            self.data = json.load(f)
        self.portfolio = self.data.get('portfolio', {})
        self.stocks = self.data.get('stocks', [])
        self.longhubang = self.data.get('longhubang', {})
    
    def _setup_template(self):
        """设置模板环境"""
        template_dir = os.path.join(os.path.dirname(__file__), 'templates')
        self.env = Environment(loader=FileSystemLoader(template_dir))
        self.template = self.env.get_template('portfolio_dashboard_dynamic.html')
    
    def _prepare_template_data(self) -> dict:
        """准备模板所需的数据"""
        return {
            'portfolio': self.portfolio,
            'stocks': self.stocks,
            'longhubang': self.longhubang,
            'update_time': self.data.get('update_time', ''),
            'total_return_pct': self.data.get('total_return_pct', 0),
        }
    
    def generate(self) -> str:
        """生成完整的HTML页面"""
        data = self._prepare_template_data()
        return self.template.render(**data)
    
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
    generator = PortfolioDashboardClassicGenerator()
    html = generator.generate()
    
    output_path = '/tmp/test_classic_dashboard.html'
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"✅ 生成完成")
    print(f"   输出文件: {output_path}")
    print(f"   文件大小: {len(html)} 字节")
    print(f"   股票数量: {len(generator.stocks)} 只")
    print(f"   组合名称: {generator.portfolio.get('name', 'N/A')}")
