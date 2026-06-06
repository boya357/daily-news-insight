"""
结构校验器 - 检查HTML结构是否完整、导航栏是否正确
"""
import re
from core.config import NAV_ITEMS


class StructureValidator:
    """结构校验器"""
    
    @staticmethod
    def validate(html: str) -> list:
        """执行所有结构校验，返回错误列表"""
        errors = []
        
        errors.extend(StructureValidator._check_basic_structure(html))
        errors.extend(StructureValidator._check_navbar(html))
        errors.extend(StructureValidator._check_mobile_menu(html))
        errors.extend(StructureValidator._check_tailwind(html))
        errors.extend(StructureValidator._check_content_spacing(html))
        
        return errors
    
    @staticmethod
    def _check_basic_structure(html: str) -> list:
        """检查基础HTML结构"""
        errors = []
        
        checks = [
            ("<!DOCTYPE html>", "缺少DOCTYPE声明"),
            ("<html", "缺少html标签"),
            ("<head", "缺少head标签"),
            ("<body", "缺少body标签"),
            ("</body>", "缺少body闭合标签"),
            ("</html>", "缺少html闭合标签"),
            ("<meta charset", "缺少charset声明"),
            ('<meta name="viewport"', "缺少viewport声明"),
        ]
        
        for pattern, msg in checks:
            if pattern not in html:
                errors.append(f"[结构] {msg}")
        
        return errors
    
    @staticmethod
    def _check_navbar(html: str) -> list:
        """检查导航栏是否完整正确"""
        errors = []
        
        # 检查导航栏存在（通过glass-nav类检测）
        if 'glass-nav' not in html:
            errors.append("[结构] 缺少标准导航栏")
            return errors
        
        # 检查导航项数量（通过导航链接的href模式检测）
        # 匹配 /daily-news-insight/xxx/latest.html 或 index.html 格式的导航链接
        nav_pattern = r'href="/daily-news-insight/[^"]+"'
        nav_links = re.findall(nav_pattern, html)
        
        # 去重（桌面端和移动端各有一套）
        unique_links = set(nav_links)
        expected_count = len(NAV_ITEMS)
        
        # 检查是否包含所有预期的导航项
        found_labels = []
        for item in NAV_ITEMS:
            # 通过路径匹配来检查导航项是否存在
            if item["path"] in html:
                found_labels.append(item["label"])
        
        if len(found_labels) < expected_count:
            missing = [item["label"] for item in NAV_ITEMS if item["label"] not in found_labels]
            errors.append(f"[结构] 导航栏缺少{len(missing)}个链接: {', '.join(missing)}")
        
        # 检查glass-nav样式
        if "backdrop-filter" not in html and "backdrop-filter" not in html:
            errors.append("[结构] 导航栏缺少玻璃态样式")
        
        # 检查z-index（确保导航在最上层）
        if "z-50" not in html and "2147483647" not in html:
            errors.append("[结构] 导航栏z-index不正确")
        
        # 检查Logo/标题
        if "投资研究中心" not in html:
            errors.append("[结构] 导航栏缺少站点名称")
        
        return errors
    
    @staticmethod
    def _check_mobile_menu(html: str) -> list:
        """检查移动端菜单"""
        errors = []
        
        checks = [
            ('id="mobileMenu"', "缺少移动端菜单容器"),
            ("toggleMobileMenu()", "缺少toggleMobileMenu函数"),
            ("hamburger-btn", "缺少汉堡按钮"),
            ("close-menu-btn", "缺少关闭按钮"),
            ("mobile-menu-item", "缺少移动端菜单项"),
        ]
        
        for pattern, msg in checks:
            if pattern not in html:
                errors.append(f"[结构] {msg}")
        
        # 检查响应式断点（768px或1024px都可以）
        if "@media (max-width: 768px)" not in html and "@media (max-width: 1024px)" not in html:
            errors.append("[结构] 缺少移动端响应式样式")
        
        return errors
    
    @staticmethod
    def _check_tailwind(html: str) -> list:
        """检查Tailwind CSS是否加载"""
        errors = []
        
        if "cdn.tailwindcss.com" not in html:
            errors.append("[结构] 缺少Tailwind CSS CDN")
        
        return errors
    
    @staticmethod
    def _check_content_spacing(html: str) -> list:
        """检查内容区域是否有顶部间距（避免被导航栏遮挡）"""
        errors = []
        
        if "padding-top" not in html and "pt-" not in html:
            errors.append("[结构] 内容区域缺少顶部间距，可能被导航栏遮挡")
        
        return errors
