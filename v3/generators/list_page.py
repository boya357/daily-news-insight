"""
List page generator - Safe list page update mechanism
Fix historical issues: latest.html being overwritten, list page structure corruption
"""
import os
import re
from datetime import datetime

import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.config import REPORT_TYPES, BASE_PATH, PROTECTED_FILES, BASE_CSS


class ListPageGenerator:
    """
    List page generator
    Safely update list page, only incrementally insert new report cards
    """
    
    LIST_START_MARKER = "<!-- LIST_START -->"
    LIST_END_MARKER = "<!-- LIST_END -->"
    
    def __init__(self, report_type: str):
        self.report_type = report_type
        self.type_info = REPORT_TYPES.get(report_type, {})
    
    def _make_card_html(self, title: str, date: str, url: str, excerpt: str = None, tag: str = None) -> str:
        """Generate report card HTML"""
        tag_html = f'<span class="inline-block px-2 py-0.5 rounded-full text-xs font-medium bg-indigo-100 text-indigo-700">{tag}</span>' if tag else ""
        excerpt_html = f'<p class="text-gray-500 text-sm mt-2 line-clamp-2">{excerpt}</p>' if excerpt else ""
        
        return f"""
            <!-- REPORT_CARD_START -->
            <a href="{url}" class="block bg-white/90 backdrop-blur-sm rounded-xl p-5 border border-gray-100 shadow-sm hover:shadow-md transition-all hover:-translate-y-0.5">
                <div class="flex items-start justify-between">
                    <div class="flex-1">
                        <h3 class="font-semibold text-gray-800 hover:text-indigo-600 transition-colors">{title}</h3>
                        {excerpt_html}
                    </div>
                    {tag_html}
                </div>
                <p class="text-xs text-gray-400 mt-3">{date}</p>
            </a>
            <!-- REPORT_CARD_END -->
"""
    
    def insert_report(self, list_filepath: str, title: str, date: str, url: str, 
                      excerpt: str = None, tag: str = None) -> bool:
        """
        Insert new report into list page (insert at the front)
        Safe operation: only modify content between markers, keep everything else unchanged
        
        Args:
            list_filepath: List page file path
            title: Report title
            date: Date string
            url: Report link
            excerpt: Summary
            tag: Tag
        
        Returns:
            Whether successful
        """
        # Security check: list page updates MUST go to index.html (list page), NEVER to latest.html (latest report copy)
        if list_filepath.endswith("latest.html"):
            print(f"[BLOCKED] 禁止写入 latest.html！列表页必须写入 index.html。路径: {list_filepath}")
            return False
        is_list_file = list_filepath.endswith("index.html") or "/list_" in list_filepath
        if not is_list_file:
            for protected in PROTECTED_FILES:
                if protected in list_filepath:
                    print(f"[WARNING] Cannot modify protected file: {list_filepath}")
                    return False
        
        # Read original file
        if not os.path.exists(list_filepath):
            print(f"[ERROR] List page does not exist: {list_filepath}")
            return False
        
        with open(list_filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if markers exist
        if self.LIST_START_MARKER not in content or self.LIST_END_MARKER not in content:
            print(f"[ERROR] List page missing markers, cannot safely insert")
            return False
        
        # Generate new card
        new_card = self._make_card_html(title, date, url, excerpt, tag)
        
        # Find insertion position (after LIST_START_MARKER)
        start_pos = content.find(self.LIST_START_MARKER) + len(self.LIST_START_MARKER)
        
        # Insert new card
        new_content = content[:start_pos] + "\n" + new_card + content[start_pos:]
        
        # Write file
        backup_path = list_filepath + ".bak"
        with open(backup_path, 'w', encoding='utf-8') as f:
            f.write(content)  # Backup
        
        with open(list_filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"[SUCCESS] Report inserted: {title}")
        print(f"[BACKUP] Original saved as: {backup_path}")
        
        return True
    
    def create_list_page(self, output_path: str, title: str, description: str = "") -> str:
        """
        Create a brand new list page (with standard navigation and list container)
        
        Args:
            output_path: Output path
            title: List page title
            description: Description
        
        Returns:
            File path
        """
        from components.layout import Navbar, Footer
        
        html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - 投资研究中心</title>
    <script src="https://cdn.tailwindcss.com"></script>
    {Navbar.get_css()}
    <style>
        body {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            font-family: -apple-system, BlinkMacSystemFont, 'PingFang SC', 'Helvetica Neue', sans-serif;
            padding-top: 80px;
        }}
        .content-area {{
            max-width: 64rem;
            margin: 0 auto;
            padding: 0 1rem;
        }}
        .page-header {{
            color: white;
            margin-bottom: 2rem;
        }}
        .page-header h1 {{
            font-size: 2rem;
            font-weight: 700;
            margin-bottom: 0.5rem;
        }}
        .report-list {{
            display: flex;
            flex-direction: column;
            gap: 1rem;
        }}
        .back-button {{
            display: inline-flex;
            align-items: center;
            color: white;
            opacity: 0.9;
            text-decoration: none;
            margin-bottom: 1rem;
        }}
        .back-button:hover {{
            opacity: 1;
        }}
    </style>
</head>
<body>
    {Navbar(active_key=self.report_type).render()}
    
    <div class="content-area">
        <a href="{BASE_PATH}/index.html" class="back-button">← 返回首页</a>
        <div class="page-header">
            <h1>{title}</h1>
            {'<p class="text-white/80">' + description + '</p>' if description else ''}
        </div>
        
        <div class="report-list">
            {self.LIST_START_MARKER}
            {self.LIST_END_MARKER}
        </div>
    </div>
    
    {Footer().render()}
</body>
</html>"""
        
        # Ensure directory exists
        os.makedirs(os.path.dirname(output_path) or '.', exist_ok=True)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html)
        
        return output_path
    
    def get_report_count(self, list_filepath: str) -> int:
        """Get number of reports in list page"""
        if not os.path.exists(list_filepath):
            return 0
        
        with open(list_filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        return content.count("<!-- REPORT_CARD_START -->")
    
    def validate_list_integrity(self, list_filepath: str) -> bool:
        """Check list page integrity"""
        if not os.path.exists(list_filepath):
            return False
        
        with open(list_filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        checks = [
            self.LIST_START_MARKER in content,
            self.LIST_END_MARKER in content,
            "glass-nav" in content,
            "投资研究中心" in content,
        ]
        
        return all(checks)
