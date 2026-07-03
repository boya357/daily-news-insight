"""
生成器基类模块 - 标准化生成器接口
所有Pro版生成器都应继承自此基类
"""
import sys
import os
from typing import Dict, List, Optional, Any
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from components.pro import ProPage, TabPane, CardGroup, DataGrid
from utils.data_loader import DataLoader, get_data_loader


class ProGenerator(ProPage):
    """Pro版生成器基类
    
    统一所有Pro版生成器的接口规范：
    - 标准化的数据加载方式
    - 统一的发布流程
    - 一致的错误处理
    """
    
    # 子类必须设置的数据类型
    data_type: str = ""  # 数据类型标识，如 "portfolio"、"topics" 等
    
    def __init__(self, 
                 title: str = "投资研究中心", 
                 active_page: str = "", 
                 footer_text: str = "",
                 data_dir: str = "data",
                 show_toc: bool = False,
                 toc_position: str = "right",
                 theme: str = "dark"):
        super().__init__(
            title=title,
            active_page=active_page,
            footer_text=footer_text,
            update_time="",
            show_toc=show_toc,
            toc_position=toc_position,
            theme=theme
        )
        self.data_loader: DataLoader = get_data_loader(data_dir)
        self._data_loaded = False
        self._output_path = ""
    
    def load_data(self):
        """加载数据 - 子类可重写此方法加载特定数据
        
        子类应在此方法中：
        1. 从data_loader获取所需数据
        2. 进行数据预处理和计算
        3. 设置self.update_time
        """
        # 默认从数据加载器获取更新时间
        if self.data_type:
            update_time = self.data_loader.get_update_time(self.data_type)
            if update_time:
                self.update_time = update_time
        
        if not self.update_time:
            self.update_time = datetime.now().strftime('%Y年%m月%d日 %H:%M')
        
        self._data_loaded = True
    
    def render(self) -> str:
        """渲染完整HTML页面（确保数据已加载）"""
        if not self._data_loaded:
            self.load_data()
        return super().render()
    
    def _content(self) -> str:
        """页面主要内容 - 子类必须重写此方法"""
        raise NotImplementedError("子类必须实现 _content 方法")
    
    def save(self, filepath: str) -> str:
        """保存到文件"""
        self._output_path = filepath
        return super().save(filepath)
    
    def validate(self) -> List[str]:
        """验证生成的页面（含白卡白字自动检测）
        
        Returns:
            错误列表，如果为空则表示验证通过
        """
        errors = []
        html = self.render()
        
        # 基本验证
        if '<!DOCTYPE html>' not in html:
            errors.append("缺少DOCTYPE声明")
        if 'glass-nav' not in html:
            errors.append("缺少导航栏")
        if 'pro-container' not in html:
            errors.append("缺少内容容器")
        
        # 检查是否有实际内容
        if len(html.strip()) < 1000:
            errors.append("页面内容过少")
        
        # === 白卡白字自动检测 (2026-07-03) ===
        if 'global-dark.css' not in html:
            errors.append("未引入 global-dark.css 全局深色主题")
        
        return errors
    
    def publish(self, output_path: str) -> Dict[str, Any]:
        """发布页面
        
        Args:
            output_path: 输出文件路径
            
        Returns:
            发布结果字典
        """
        try:
            # 确保数据已加载
            if not self._data_loaded:
                self.load_data()
            
            # 渲染HTML
            html = self.render()
            
            # 验证
            errors = self.validate()
            if errors:
                return {
                    'success': False,
                    'errors': errors,
                    'output_path': output_path
                }
            
            # 兜底注入 global-dark.css（防止子类绕过父类模板）
            if 'global-dark.css' not in html:
                inject_tag = '<link rel="stylesheet" href="/daily-news-insight/assets/global-dark.css">'
                if '</head>' in html:
                    html = html.replace('</head>', inject_tag + '</head>', 1)
                elif '<head>' in html:
                    html = html.replace('<head>', '<head>' + inject_tag, 1)
            
            # 保存文件
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(html)
            
            return {
                'success': True,
                'output_path': output_path,
                'file_size': len(html),
                'update_time': self.update_time
            }
            
        except Exception as e:
            return {
                'success': False,
                'error': str(e),
                'output_path': output_path
            }
    
    def refresh_data(self):
        """刷新数据缓存"""
        self.data_loader.refresh()
        self._data_loaded = False
    
    # ==================== 通用组件便捷方法 ====================
    
    def create_tab_pane(self, tabs: list, tab_id: str = "tab", style: str = "default") -> str:
        """创建Tab切换组件HTML（可嵌入任意内容中）
        
        Args:
            tabs: Tab列表，每项含 label(标签) 和 content(内容HTML)
            tab_id: Tab组件唯一ID
            style: Tab样式: default / underline
        
        Returns:
            Tab组件的HTML字符串
        """
        return TabPane(tabs=tabs, tab_id=tab_id, style=style).render()
    
    def create_card_group(self, cards: list, cols: int = 2, card_style: str = "glass") -> str:
        """创建卡片组HTML（卡片套卡片布局，可嵌入任意内容中）
        
        Args:
            cards: 卡片列表，每项含 title(可选)、content(内容HTML)、icon(可选)
            cols: 列数: 1, 2, 3, 4
            card_style: 卡片样式: glass / subtle
        
        Returns:
            卡片组的HTML字符串
        """
        return CardGroup(cards=cards, cols=cols, card_style=card_style).render()
    
    def create_data_grid(self, items: list, cols: int = 2) -> str:
        """创建数据网格HTML（多图表/数据卡片布局，可嵌入任意内容中）
        
        Args:
            items: 数据项列表，每项含 title(可选)、value(数值/文本)、unit(单位可选)、icon(可选)
            cols: 列数: 1, 2, 3, 4, 6
        
        Returns:
            数据网格的HTML字符串
        """
        return DataGrid(items=items, cols=cols).render()


# 便捷函数
def create_generator(generator_class, **kwargs) -> ProGenerator:
    """创建生成器实例"""
    return generator_class(**kwargs)


class V4Generator(ProGenerator):
    """V4风格生成器基类 - 默认使用light主题
    
    所有V3.5生成器都可以通过设置theme='light'切换到V4风格
    继承此类可以省去手动设置theme参数
    """
    
    def __init__(self, **kwargs):
        # 默认使用dark主题（深色玻璃态）- 2026-07-03 全站统一深色
        if 'theme' not in kwargs:
            kwargs['theme'] = 'dark'
        super().__init__(**kwargs)
