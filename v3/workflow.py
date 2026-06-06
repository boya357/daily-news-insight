"""
V3.0 发布工作流
报告生成 → 自动分类归档 → 列表页自动更新 → 全量校验 → Git部署
一条命令走完整个发布流程
"""
import os
import sys
import subprocess
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from core.config import REPORT_TYPES, PROTECTED_FILES, BASE_PATH
from generators.list_page import ListPageGenerator
from validators.structure import StructureValidator
from validators.links import LinkValidator
from validators.content import ContentValidator


class ReportPublisher:
    """
    报告发布器
    一站式完成：归档 → 更新列表 → 校验 → 部署
    """
    
    def __init__(self, docs_root: str = "docs"):
        # git根目录（v3的上一级）
        self.git_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        # docs目录（相对于git根目录）
        if os.path.isabs(docs_root):
            self.docs_root = docs_root
        else:
            self.docs_root = os.path.join(self.git_root, docs_root)
    
    def publish(self, html_content: str, title: str, report_type: str, 
                filename: str = None, excerpt: str = None, 
                auto_deploy: bool = True) -> dict:
        """
        完整发布流程
        
        Args:
            html_content: 报告HTML内容
            title: 报告标题
            report_type: 报告类型（对应REPORT_TYPES的key）
            filename: 文件名，不传则自动生成
            excerpt: 摘要（用于列表页展示）
            auto_deploy: 是否自动Git部署
            
        Returns:
            发布结果字典
        """
        result = {
            "success": False,
            "title": title,
            "report_type": report_type,
            "filepath": None,
            "list_updated": False,
            "validated": False,
            "deployed": False,
            "errors": []
        }
        
        # 1. 验证报告类型
        if report_type not in REPORT_TYPES:
            result["errors"].append(f"未知的报告类型: {report_type}")
            return result
        
        type_info = REPORT_TYPES[report_type]
        category_dir = type_info.get("dir", "")
        
        # 2. 自动生成文件名
        if not filename:
            date_str = datetime.now().strftime("%Y%m%d")
            # 从标题生成安全文件名
            safe_title = self._make_safe_filename(title)
            filename = f"{date_str}_{safe_title}.html"
        
        # 3. 归档报告
        target_dir = os.path.join(self.docs_root, category_dir) if category_dir else self.docs_root
        os.makedirs(target_dir, exist_ok=True)
        filepath = os.path.join(target_dir, filename)
        
        # 安全检查：不能覆盖受保护文件
        if self._is_protected(filename):
            result["errors"].append(f"不能覆盖受保护文件: {filename}")
            return result
        
        # 写入文件
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        result["filepath"] = filepath
        print(f"✅ 报告已归档: {filepath}")
        
        # 4. 校验报告
        validation_passed = self._validate_report(filepath)
        result["validated"] = validation_passed
        
        if not validation_passed:
            result["errors"].append("报告校验未通过")
            # 校验失败不阻止发布，但给出警告
            print("⚠️  报告校验存在问题，但继续发布流程")
        
        # 5. 更新列表页
        list_updated = self._update_list_page(
            report_type=report_type,
            title=title,
            date=datetime.now().strftime("%Y-%m-%d"),
            url=filename,  # 相对路径
            excerpt=excerpt
        )
        result["list_updated"] = list_updated
        
        if not list_updated:
            result["errors"].append("列表页更新失败")
            print("⚠️  列表页更新失败")
        
        # 6. Git部署
        if auto_deploy:
            deployed = self._git_deploy(f"新增{type_info.get('name', '')}报告: {title}")
            result["deployed"] = deployed
            if deployed:
                print("✅ 已部署到GitHub Pages")
            else:
                result["errors"].append("Git部署失败")
                print("❌ Git部署失败")
        
        result["success"] = True
        return result
    
    def _make_safe_filename(self, title: str) -> str:
        """生成安全的文件名"""
        # 简单处理：替换特殊字符
        safe = title.replace(' ', '_').replace('/', '_').replace('\\', '_')
        safe = safe.replace(':', '_').replace('*', '_').replace('?', '_')
        safe = safe.replace('"', '_').replace('<', '_').replace('>', '_')
        safe = safe.replace('|', '_')
        # 限制长度
        if len(safe) > 50:
            safe = safe[:50]
        return safe
    
    def _is_protected(self, filename: str) -> bool:
        """检查是否是受保护文件"""
        for protected in PROTECTED_FILES:
            if protected.endswith(filename) or filename == protected:
                return True
        return False
    
    def _validate_report(self, filepath: str) -> bool:
        """校验报告完整性"""
        print(f"🔍 正在校验报告...")
        all_passed = True
        
        # 读取文件内容
        with open(filepath, 'r', encoding='utf-8') as f:
            html = f.read()
        
        # 结构校验
        struct_errors = StructureValidator.validate(html)
        if struct_errors:
            all_passed = False
            for err in struct_errors:
                print(f"   ❌ 结构: {err}")
        
        # 链接校验
        link_errors = LinkValidator.validate(html)
        if link_errors:
            all_passed = False
            for err in link_errors:
                print(f"   ❌ 链接: {err}")
        
        # 文件链接校验
        file_link_errors = LinkValidator.check_file_links(filepath)
        if file_link_errors:
            all_passed = False
            for err in file_link_errors:
                print(f"   ❌ 文件链接: {err}")
        
        # 内容校验
        content_errors = ContentValidator.validate(html)
        if content_errors:
            all_passed = False
            for err in content_errors:
                print(f"   ⚠️  内容: {err}")
        
        if all_passed:
            print("   ✅ 全部校验通过")
        
        return all_passed
    
    def _update_list_page(self, report_type: str, title: str, date: str, 
                          url: str, excerpt: str = None) -> bool:
        """更新列表页"""
        type_info = REPORT_TYPES.get(report_type, {})
        category_dir = type_info.get("dir", "")
        list_file = type_info.get("list_file", "latest.html")
        
        list_filepath = os.path.join(self.docs_root, category_dir, list_file) if category_dir \
            else os.path.join(self.docs_root, list_file)
        
        if not os.path.exists(list_filepath):
            print(f"⚠️  列表页不存在，跳过更新: {list_filepath}")
            return False
        
        # 尝试使用V3.0增量更新（有标记的情况）
        try:
            generator = ListPageGenerator(report_type)
            success = generator.insert_report(
                list_filepath=list_filepath,
                title=title,
                date=date,
                url=url,
                excerpt=excerpt,
                tag=type_info.get("name", "")
            )
            if success:
                print(f"✅ 列表页已更新(V3.0增量): {list_filepath}")
                return True
        except Exception as e:
            print(f"⚠️  V3.0列表更新失败，尝试兼容模式: {e}")
        
        # 兼容模式：直接在列表开头插入卡片（针对旧版列表页）
        return self._update_list_page_compat(list_filepath, title, date, url, type_info)
    
    def _update_list_page_compat(self, list_filepath: str, title: str, 
                                  date: str, url: str, type_info: dict) -> bool:
        """
        兼容旧版列表页的更新方式
        直接在网格开头插入新卡片
        """
        try:
            with open(list_filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 查找报告卡片网格
            grid_pattern = r'<div class="grid[^"]*gap-[^"]*"'
            import re
            match = re.search(grid_pattern, content)
            
            if not match:
                print(f"⚠️  未找到列表网格，无法更新")
                return False
            
            # 找到网格div的闭合位置（第一个完整的卡片后面）
            # 简化处理：找到第一个report-card链接，在它前面插入
            card_pattern = r'(\s*<a[^>]*class="[^"]*report-card[^"]*"[^>]*>)'
            card_match = re.search(card_pattern, content)
            
            if not card_match:
                print(f"⚠️  未找到报告卡片，无法更新")
                return False
            
            # 生成新卡片（模仿旧版样式）
            tag_name = type_info.get("name", "报告")
            new_card = f'''
                <a href="{url}" class="report-card block p-5 bg-gradient-to-br from-green-50 to-emerald-50 border-2 border-green-200 rounded-xl text-center group hover:shadow-lg transition-all">
                    <div class="text-3xl mb-2">🔗</div>
                    <div class="font-semibold text-gray-800 text-sm mb-1 group-hover:text-green-600 transition-colors line-clamp-2">{date.replace("-", "")} {title}</div>
                    <span class="inline-block px-2 py-1 text-xs font-bold bg-red-100 text-red-700 rounded">🆕 最新</span>
                </a>
            '''
            
            # 在第一个卡片前面插入
            insert_pos = card_match.start()
            new_content = content[:insert_pos] + new_card + content[insert_pos:]
            
            # 备份原文件
            backup_path = list_filepath + ".bak"
            with open(backup_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            # 写入新内容
            with open(list_filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            print(f"✅ 列表页已更新(兼容模式): {list_filepath}")
            return True
            
        except Exception as e:
            print(f"❌ 列表页更新失败: {e}")
            return False
    
    def _git_deploy(self, commit_message: str) -> bool:
        """Git提交并部署"""
        try:
            # 切换到git根目录
            original_dir = os.getcwd()
            os.chdir(self.git_root)
            
            # 添加所有变更
            subprocess.run(["git", "add", "-A"], capture_output=True, text=True)
            
            # 提交
            result = subprocess.run(
                ["git", "commit", "-m", commit_message],
                capture_output=True, text=True
            )
            
            if result.returncode != 0:
                # 可能是没有变更
                if "nothing to commit" in result.stdout:
                    print("   ℹ️  没有需要提交的变更")
                    os.chdir(original_dir)
                    return True
                print(f"   ❌ Git提交失败: {result.stderr}")
                os.chdir(original_dir)
                return False
            
            # 推送
            push_result = subprocess.run(
                ["git", "push"],
                capture_output=True, text=True
            )
            
            if push_result.returncode != 0:
                print(f"   ❌ Git推送失败: {push_result.stderr}")
                os.chdir(original_dir)
                return False
            
            os.chdir(original_dir)
            return True
            
        except Exception as e:
            print(f"   ❌ Git部署异常: {e}")
            return False


# 便捷函数
def publish_deep_dive(generator, title: str, report_type: str = "industry_chain",
                      filename: str = None, excerpt: str = None, 
                      auto_deploy: bool = True) -> dict:
    """
    便捷函数：发布深度研究报告
    
    Args:
        generator: DeepDiveGenerator实例
        title: 报告标题
        report_type: 报告类型
        filename: 文件名
        excerpt: 摘要
        auto_deploy: 是否自动部署
    
    Returns:
        发布结果
    """
    # 生成HTML
    html_content = generator.report.generate()
    
    # 发布
    publisher = ReportPublisher(docs_root="docs")
    return publisher.publish(
        html_content=html_content,
        title=title,
        report_type=report_type,
        filename=filename,
        excerpt=excerpt,
        auto_deploy=auto_deploy
    )


