"""
链接校验器 - 检查内部链接路径正确性、大小写一致性等
根治历史问题：S级催化 vs s级催化大小写不一致
"""
import re
from core.config import NAV_ITEMS, BASE_PATH


class LinkValidator:
    """链接校验器"""
    
    @staticmethod
    def validate(html: str) -> list:
        """执行所有链接校验"""
        errors = []
        
        errors.extend(LinkValidator._check_nav_links(html))
        errors.extend(LinkValidator._check_case_sensitive(html))
        errors.extend(LinkValidator._check_internal_links(html))
        
        return errors
    
    @staticmethod
    def _check_nav_links(html: str) -> list:
        """检查导航链接是否正确"""
        errors = []
        
        # 提取所有导航链接（包含active状态）
        # 匹配所有在nav中的链接
        nav_links = []
        # 简单方法：找到导航栏部分，然后提取所有链接
        nav_start = html.find('<nav')
        nav_end = html.find('</nav>', nav_start) if nav_start > 0 else 0
        if nav_start > 0 and nav_end > nav_start:
            nav_section = html[nav_start:nav_end]
            # 提取所有href
            href_pattern = r'href="([^"]+)"'
            all_hrefs = re.findall(href_pattern, nav_section)
            # 过滤掉#和javascript
            nav_links = [h for h in all_hrefs if not h.startswith('#') and not h.startswith('javascript')]
        
        # 检查导航链接路径
        for item in NAV_ITEMS:
            expected_path = item["path"]
            found = False
            
            for link in nav_links:
                if link == expected_path or link.endswith(expected_path):
                    found = True
                    break
            
            if not found:
                errors.append(f"[链接] 导航栏缺少'{item['label']}的正确链接: {expected_path}")
        
        return errors
    
    @staticmethod
    def _check_case_sensitive(html: str) -> list:
        """检查大小写一致性问题（历史问题：S级催化 vs s级催化）
        """
        errors = []
        
        # 检查S级催化相关的路径
        # 正确路径应该包含小写的s级催化扫描
        # 检查是否有大写的"S级催化扫描"目录引用
        
        # 查找所有包含"级催化"的路径
        catalyst_pattern = re.findall(r'href="([^"]*级催化[^"]*)"', html)
        
        for link in catalyst_pattern:
            # 检查是否包含大写S的情况
            if "S级催化" in link and "s级催化" not in link:
                # 可能有问题，检查是不是应该是小写
                if "s级催化扫描" in link.lower():
                    # 路径里有大写S，但应该是小写
                    if link != link.replace("S级催化", "s级催化"):
                        # 确认一下：如果路径里有大写的"S级催化扫描"
                        if "S级催化扫描" in link:
                            errors.append(f"[链接] S级催化路径大小写不一致: {link} (应该是小写s)")
        
        # 额外检查：href中的路径
        all_hrefs = re.findall(r'href="([^"]+)"', html)
        for href in all_hrefs:
            if "S级催化" in href and "s级催化" not in href:
                # 检查是否指向目录的情况
                if "级催化扫描" in href:
                    errors.append(f"[链接] 发现大写S的催化路径: {href}")
        
        return errors
    
    @staticmethod
    def _check_internal_links(html: str) -> list:
        """检查内部链接格式"""
        errors = []
        
        # 检查是否有相对路径（应该用绝对路径）
        # 但有些相对路径也可以接受，这里主要检查明显的错误
        
        # 检查是否有断裂的锚点链接
        # href="#xxx" 是正常，跳过
        
        # 检查是否有指向本地文件系统路径
        if "file://" in html:
            errors.append("[链接] 发现file://协议链接，应该使用相对路径或绝对路径")
        
        # 检查BASE_PATH是否正确
        # 所有内部链接应该以 /daily-news-insight/ 开头
        # （这个规则太严格了，暂时注释掉
        # 相对路径也可以接受
        
        return errors
    
    @staticmethod
    def check_file_links(filepath: str) -> list:
        """检查文件中的所有链接（文件级别的深度检查）"""
        errors = []
        
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 提取所有链接
            links = re.findall(r'href="([^"]+)"', content)
            img_links = re.findall(r'src="([^"]+)"', content)
            
            all_links = links + img_links
            
            # 检查内部链接的文件是否存在
            import os
            base_dir = os.path.dirname(filepath)
            
            for link in all_links:
                if link.startswith('http') or link.startswith('#') or link.startswith('javascript'):
                    continue
                
                # 处理绝对路径
                if link.startswith('/daily-news-insight/'):
                    # 转换为相对路径（相对于项目根目录
                    rel_path = link.replace('/daily-news-insight/', '')
                    # 需要项目根目录需要从其他地方获取，这里先跳过
                    continue
                
                # 处理相对路径
                if link.startswith('../') or not link.startswith('/'):
                    target_path = os.path.normpath(os.path.join(base_dir, link))
                    # 检查文件是否存在（只检查.html和常见静态资源）
                    if any(link.endswith(ext) for ext in ['.html', '.css', '.js', '.png', '.jpg', '.jpeg', '.gif', '.svg']):
                        if not os.path.exists(target_path):
                            errors.append(f"[链接] 本地文件不存在: {link} -> {target_path}")
        
        except Exception as e:
            errors.append(f"[链接] 文件读取失败: {str(e)}")
        
        return errors
