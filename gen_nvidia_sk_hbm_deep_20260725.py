#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
英伟达×SK集团 5000亿美元AI投资 HBM产业链深度研究
基于V3 DeepDiveGenerator 扩展的深度报告生成器
全站深色玻璃态 / 持仓股金色高亮 / 11项统一导航
"""

import sys
import os
import re
import html as html_mod
from pathlib import Path

ROOT = Path("/root/daily-news-insight")
os.chdir(str(ROOT))
sys.path.insert(0, str(ROOT / "v3"))

from generators.deep_dive import DeepDiveGenerator
from components.data import DataCard
from components.special import RiskAlert

# ============================================================
# 持仓股金色高亮列表
# ============================================================
HOLDING_STOCKS = ["雅克科技", "华海诚科", "长电科技", "铜冠铜箔", "英维克"]


# ============================================================
# 扩展 DeepDiveGenerator —— 注入 global-dark.css + 持仓股金色高亮
# ============================================================
class DarkGlassDeepDive(DeepDiveGenerator):
    """深色玻璃态版深度报告生成器
    继承 DeepDiveGenerator，在生成时注入 global-dark.css
    确保全站强制深色玻璃态，禁止白卡白字
    """

    def __init__(self, title: str, subtitle: str = None):
        super().__init__(title=title, subtitle=subtitle)
        self.report.report_type = "industry_chain"

    def generate(self) -> str:
        """重写generate：注入global-dark.css + 持仓股金色高亮"""
        html = super().generate()

        # 1. 注入 global-dark.css
        dark_css = (
            '\n    <!-- global-dark-theme v2.0 -->\n'
            '    <link rel="stylesheet" href="/daily-news-insight/assets/global-dark.css">\n'
            '    <link rel="stylesheet" '
            'href="https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.5.1/css/all.min.css">\n'
        )
        html = html.replace("</head>", dark_css + "</head>")

        # 2. 注入持仓股金色高亮+正文深色样式
        extra_css = """
    <style>
        /* 持仓股金色高亮 */
        .holding-stock-gold {
            background: linear-gradient(135deg, #fbbf24 0%, #f59e0b 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            font-weight: 700;
            padding: 0 2px;
        }
        /* 正文深色文字覆盖 */
        .prose-content p, .prose-content li, .prose-content span,
        .prose-content div, .prose-content blockquote {
            color: rgba(255,255,255,0.85) !important;
        }
        .prose-content h1, .prose-content h2, .prose-content h3, .prose-content h4 {
            color: #f1f5f9 !important;
            margin-top: 1.5rem;
            margin-bottom: 0.75rem;
            font-weight: 600;
        }
        .prose-content strong {
            color: #c4b5fd !important;
        }
        .prose-content a {
            color: #a78bfa !important;
            text-decoration: underline;
        }
        .prose-content em {
            color: rgba(255,255,255,0.7);
        }
        /* 表格深色玻璃态 */
        .prose-content table {
            width: 100%;
            border-collapse: collapse;
            margin: 1rem 0;
            background: rgba(255,255,255,0.04);
            border-radius: 12px;
            overflow: hidden;
            border: 1px solid rgba(255,255,255,0.08);
        }
        .prose-content th {
            background: rgba(139,92,246,0.2);
            color: #e9d5ff !important;
            padding: 10px 12px;
            text-align: left;
            font-weight: 600;
            font-size: 13px;
            border-bottom: 1px solid rgba(255,255,255,0.1);
        }
        .prose-content td {
            padding: 10px 12px;
            color: rgba(255,255,255,0.8) !important;
            font-size: 14px;
            border-bottom: 1px solid rgba(255,255,255,0.06);
        }
        .prose-content tr:hover td {
            background: rgba(255,255,255,0.04);
        }
        .prose-content tr:last-child td {
            border-bottom: none;
        }
        /* 多空卡片玻璃态覆盖 */
        .bg-green-50, .bg-red-50 {
            background: rgba(255,255,255,0.06) !important;
            border: 1px solid rgba(255,255,255,0.1) !important;
            border-radius: 16px !important;
            backdrop-filter: blur(10px);
        }
        .text-green-800, .text-green-700 { color: #86efac !important; }
        .text-red-800, .text-red-700 { color: #fca5a5 !important; }
        .border-green-200 { border-color: rgba(16,185,129,0.3) !important; }
        .border-red-200 { border-color: rgba(239,68,68,0.3) !important; }
        /* Section标题 */
        .section-title, h2 { color: #f1f5f9 !important; }
        /* 报告头 */
        .report-header h1, .report-header p { color: white !important; }
        /* 风险提示卡片深色 */
        .bg-red-50.bg-red-50 {
            background: rgba(239,68,68,0.08) !important;
            border: 1px solid rgba(239,68,68,0.2) !important;
        }
        /* 结论卡片 */
        .from-green-500.to-emerald-600,
        .from-blue-500.to-indigo-600 {
            /* 保持结论渐变不变，本身就是深色背景 */
        }
        /* 正文内容容器增加行高 */
        .prose-content p {
            line-height: 1.9;
            margin-bottom: 1rem;
        }
        .prose-content ul, .prose-content ol {
            margin: 0.75rem 0;
            padding-left: 1.5rem;
        }
        .prose-content li {
            margin-bottom: 0.4rem;
            line-height: 1.7;
        }
        .prose-content blockquote {
            margin: 1rem 0;
            font-style: italic;
            opacity: 0.85;
        }
        /* 图片样式 */
        .prose-content img {
            max-width: 100%;
            border-radius: 12px;
            margin: 1rem 0;
            box-shadow: 0 8px 32px rgba(0,0,0,0.3);
        }
    </style>
"""
        html = html.replace("</head>", extra_css + "</head>")

        # 3. 注入持仓股金色高亮JS
        holding_js = """
    <script>
    document.addEventListener('DOMContentLoaded', function() {
        const holdings = ['雅克科技', '华海诚科', '长电科技', '铜冠铜箔', '英维克'];
        // 在所有正文容器中高亮持仓股
        const allElements = document.querySelectorAll('.prose-content, .section-content');
        function walkNodes(node) {
            if (node.nodeType === Node.TEXT_NODE) {
                let text = node.textContent;
                let replaced = false;
                holdings.forEach(function(stock) {
                    if (text.indexOf(stock) !== -1) {
                        text = text.split(stock).join('<span class="holding-stock-gold">' + stock + '</span>');
                        replaced = true;
                    }
                });
                if (replaced) {
                    const span = document.createElement('span');
                    span.innerHTML = text;
                    node.parentNode.replaceChild(span, node);
                }
            } else if (node.nodeType === Node.ELEMENT_NODE) {
                // 跳过script/style/已经是gold的元素
                if (node.tagName === 'SCRIPT' || node.tagName === 'STYLE') return;
                if (node.classList && node.classList.contains('holding-stock-gold')) return;
                // 倒序遍历以避免替换导致的索引问题
                for (let i = node.childNodes.length - 1; i >= 0; i--) {
                    walkNodes(node.childNodes[i]);
                }
            }
        }
        allElements.forEach(function(el) {
            walkNodes(el);
        });
    });
    </script>
"""
        html = html.replace("</body>", holding_js + "\n</body>")

        return html


# ============================================================
# Markdown转HTML（基础）
# ============================================================
def inline_md(text: str) -> str:
    """行内Markdown处理"""
    text = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'(?<!\*)\*([^*\n]+)\*(?!\*)', r'<em>\1</em>', text)
    text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)',
                  r'<a href="\2" target="_blank" style="color:#a78bfa;text-decoration:underline;">\1</a>',
                  text)
    text = re.sub(r'`([^`]+)`',
                  r'<code style="background:rgba(139,92,246,0.2);padding:2px 6px;border-radius:4px;font-size:0.9em;color:#c4b5fd;">\1</code>',
                  text)
    return text


def md_to_html_simple(text: str) -> str:
    """轻量Markdown转HTML"""
    lines = text.strip().split('\n')
    html_lines = []
    in_list = False
    list_type = None
    in_table = False
    table_rows = []

    def close_list():
        nonlocal in_list, list_type
        if in_list:
            html_lines.append('</ul>' if list_type == 'ul' else '</ol>')
            in_list = False
            list_type = None

    def flush_table():
        nonlocal table_rows, in_table
        if not table_rows:
            return
        html_lines.append('<table>')
        html_lines.append('<thead><tr>')
        for h in table_rows[0]:
            html_lines.append(f'<th>{inline_md(h)}</th>')
        html_lines.append('</tr></thead><tbody>')
        for row in table_rows[1:]:
            html_lines.append('<tr>')
            for c in row:
                html_lines.append(f'<td>{inline_md(c)}</td>')
            html_lines.append('</tr>')
        html_lines.append('</tbody></table>')
        table_rows = []
        in_table = False

    for line in lines:
        line = line.rstrip()

        # 表格
        if line.startswith('|') and not re.match(r'^\|[-:| ]+\|\s*$', line):
            in_table = True
            cells = [c.strip() for c in line.strip('|').split('|')]
            table_rows.append(cells)
            continue
        elif re.match(r'^\|[-:| ]+\|\s*$', line) and in_table:
            continue  # 分隔行
        elif in_table and not line.startswith('|'):
            flush_table()

        # 空行
        if not line:
            close_list()
            continue

        # 标题
        if line.startswith('### '):
            close_list()
            html_lines.append(f'<h3>{inline_md(line[4:])}</h3>')
            continue
        if line.startswith('#### '):
            close_list()
            html_lines.append(f'<h4>{inline_md(line[5:])}</h4>')
            continue

        # 无序列表
        if re.match(r'^[-*] ', line):
            if not in_list or list_type != 'ul':
                close_list()
                html_lines.append('<ul>')
                in_list = True
                list_type = 'ul'
            html_lines.append(f'<li>{inline_md(line[2:])}</li>')
            continue

        # 有序列表
        if re.match(r'^\d+\. ', line):
            if not in_list or list_type != 'ol':
                close_list()
                html_lines.append('<ol>')
                in_list = True
                list_type = 'ol'
            html_lines.append(f'<li>{inline_md(re.sub(r"^\\d+\\. ", "", line))}</li>')
            continue

        # 引用
        if line.startswith('> '):
            close_list()
            html_lines.append(
                f'<blockquote style="border-left:3px solid #8b5cf6;padding-left:12px;'
                f'color:rgba(255,255,255,0.7);margin:1rem 0;font-style:italic;">'
                f'{inline_md(line[2:])}</blockquote>'
            )
            continue

        # 图片
        img_match = re.match(r'!\[([^\]]*)\]\(([^)]+)\)', line)
        if img_match:
            close_list()
            alt = img_match.group(1)
            src = img_match.group(2)
            html_lines.append(
                f'<div style="text-align:center;margin:1.5rem 0;">'
                f'<img src="{src}" alt="{alt}" '
                f'style="max-width:100%;border-radius:12px;box-shadow:0 8px 32px rgba(0,0,0,0.3);">'
                f'</div>'
            )
            continue

        # 普通段落
        close_list()
        html_lines.append(f'<p>{inline_md(line)}</p>')

    close_list()
    flush_table()

    return '\n'.join(html_lines)


# ============================================================
# 主生成函数
# ============================================================
def build_report():
    md_path = Path("/app/data/所有对话/主对话/nvidia_sk_ai_investment_report.md")
    md_content = md_path.read_text(encoding='utf-8')

    gen = DarkGlassDeepDive(
        title="英伟达×SK集团 5000亿美元AI投资 HBM产业链深度研究",
        subtitle="HBM产业链重构 · A股持仓股弹性测算 · 2026年最重磅产业催化"
    )

    # ================================================================
    # 一、核心结论摘要（多方+空方视角）
    # ================================================================
    gen.add_summary(
        core_view="2026年7月24日英伟达与SK集团宣布超5000亿美元AI战略合作，是AI算力产业链下半年最重磅产业级催化。但市场存在'5000亿=单方投资''5000亿=SK capex''太极实业是HBM封测龙头'三大普遍误读。本报告通过原始信源交叉验证，得出五个核心判断：5000亿为双向远期交易额（实际落地40-50%）、确定性排序雅克科技>华海诚科>长电科技、S档仅雅克+中际旭创、HBM上游材料弹性最大、短期情绪后必有分化。",
        bull_points=[
            "5000亿美元双向框架：HBM+AI工厂双轮驱动，2026-2030年实际落地2000-2500亿美元",
            "HBM量价齐升：2026年546亿美元→2028年1680亿美元，CAGR 78%，缺口43.5%",
            "三大持仓股确定性明确：雅克独家前驱体+长协至2031、华海GMC全球三家、长电封测龙头",
            "技术壁垒+国产替代双逻辑：材料环节验证周期1-2年，换料成本极高，护城河深",
            "三重共振催化：5000亿事件+Vera Rubin+HBM4量产，2026Q4-2027年业绩兑现主升浪"
        ],
        bear_points=[
            "5000亿为远期意向框架，非约束合同，实际落地率可能低于40%",
            "HBM2027H2-2028年产能集中释放，若AI需求放缓可能供过于求、ASP快速下跌",
            "韩国材料国产化政策长期施压，雅克/华海5-10年维度面临本土替代风险",
            "短期估值偏高：雅克涨停后2026E PE约56-60倍，华海PE-TTM 485倍，回调风险大",
            "美国对华芯片管制升级，可能影响中国材料企业向韩国供货的资质审查"
        ]
    )

    # ================================================================
    # 二、核心数据卡片
    # ================================================================
    cards = [
        DataCard(title="合作总规模", value="5000", unit="亿美元",
                 trend="双向远期框架", trend_up=True, variant="primary"),
        DataCard(title="实际落地率", value="40-50%",
                 trend="约2000-2500亿", trend_up=True, variant="warning"),
        DataCard(title="2028 HBM市场", value="1680", unit="亿美元",
                 trend="+78% CAGR", trend_up=True, variant="success"),
        DataCard(title="HBM供需缺口", value="43.5%",
                 trend="2026年", trend_up=True, variant="danger"),
    ]
    gen.add_data_cards(cards=cards, cols=4)

    # 持仓股快速概览
    holding_cards = [
        DataCard(title="⭐ 雅克科技", value="S档",
                 subtitle="HBM4前驱体独家",
                 trend="93分 · 20-25%仓", trend_up=True, variant="success"),
        DataCard(title="⭐ 华海诚科", value="A档",
                 subtitle="GMC塑封料全球三家",
                 trend="84分 · 8-12%仓", trend_up=True, variant="primary"),
        DataCard(title="⭐ 长电科技", value="B档",
                 subtitle="HBM3E外协封测",
                 trend="73分 · 10-15%仓", trend_up=True, variant="warning"),
        DataCard(title="⭐ 铜冠/英维克", value="B/C档",
                 subtitle="铜箔HVLP / 液冷",
                 trend="观望 · 减仓中", trend_up=False, variant="danger"),
    ]
    gen.add_data_cards(cards=holding_cards, cols=4)

    # ================================================================
    # 三、5000亿美元投资真相拆解
    # ================================================================
    ch2_match = re.search(r'## 2\. 事件深度挖掘.*?(?=\n## 3\.)', md_content, re.DOTALL)
    ch2_content = ch2_match.group(0) if ch2_match else ""
    ch2_html = md_to_html_simple(re.sub(r'^## .*\n', '', ch2_content, count=1))

    gen.add_analysis_section(
        title="三、5000亿美元投资真相拆解",
        content=f'<div class="prose-content">{ch2_html}</div>',
        icon="💰"
    )

    # ================================================================
    # 四、HBM产业链全景图与弹性排序
    # ================================================================
    ch3_match = re.search(r'## 3\. HBM产业链全景与增量空间.*?(?=\n## 4\.)', md_content, re.DOTALL)
    ch3_content = ch3_match.group(0) if ch3_match else ""
    ch3_html = md_to_html_simple(re.sub(r'^## .*\n', '', ch3_content, count=1))

    gen.add_analysis_section(
        title="四、HBM产业链全景图与弹性排序",
        content=f'<div class="prose-content">{ch3_html}</div>',
        icon="🔗"
    )

    # 产业链弹性排序对比表
    chain_table_headers = ["环节", "代表标的", "确定性", "弹性", "壁垒"]
    chain_table_rows = [
        ["半导体材料（前驱体/GMC/硅微粉）", "雅克科技、华海诚科、联瑞新材", "★★★★★", "★★★★★", "极高"],
        ["半导体设备（键合/测试/CMP）", "赛腾股份、拓荆科技、安集科技", "★★★☆☆", "★★★★☆", "高"],
        ["先进封装", "长电科技、通富微电", "★★★★☆", "★★★☆☆", "中高"],
        ["光模块/算力基础设施", "中际旭创、新易盛", "★★★★★", "★★★☆☆", "高"],
        ["液冷/供电（800V HVDC）", "英维克、麦格米特、泰永长征", "★★☆☆☆", "★★★☆☆", "中"],
        ["铜箔/PCB材料", "铜冠铜箔", "★★☆☆☆", "★★☆☆☆", "中低"],
    ]
    gen.add_competitive_analysis(
        headers=chain_table_headers,
        rows=chain_table_rows,
        highlight_rows=[0, 2]
    )

    # ================================================================
    # 五、雅克科技深度分析（S档）
    # ================================================================
    ch4_1_match = re.search(r'(### 4\.1 雅克科技.*?)(?=\n### 4\.2 )', md_content, re.DOTALL)
    yake_content = ch4_1_match.group(1) if ch4_1_match else ""

    yake_cards = [
        DataCard(title="HBM业务定位", value="S档",
                 subtitle="HBM4前驱体独家供应", variant="success"),
        DataCard(title="客户关系", value="SK海力士独家",
                 subtitle="长协至2031年", variant="primary"),
        DataCard(title="2026E PE", value="56-60x",
                 subtitle="涨停后估值", variant="warning"),
        DataCard(title="目标价", value="220-250", unit="元",
                 subtitle="2027年中股权回购催化", variant="success"),
    ]
    gen.add_data_cards(cards=yake_cards, cols=4)

    yake_html = md_to_html_simple(yake_content)
    gen.add_analysis_section(
        title="五、雅克科技深度分析（S档 · HBM4前驱体独家）",
        content=f'<div class="prose-content">{yake_html}</div>',
        icon="🏆"
    )

    # ================================================================
    # 六、华海诚科深度分析（A档）
    # ================================================================
    ch4_2_match = re.search(r'(### 4\.2 华海诚科.*?)(?=\n### 4\.3 )', md_content, re.DOTALL)
    huahai_content = ch4_2_match.group(1) if ch4_2_match else ""

    huahai_cards = [
        DataCard(title="HBM业务定位", value="A档",
                 subtitle="GMC塑封料全球三家", variant="primary"),
        DataCard(title="SK海力士份额", value="5%→20%",
                 subtitle="目标3-4年提升", trend_up=True, variant="success"),
        DataCard(title="2026E PE", value="93-114x",
                 subtitle="高估值高弹性", variant="warning"),
        DataCard(title="目标价", value="160-180", unit="元",
                 subtitle="份额提升主升浪", variant="primary"),
    ]
    gen.add_data_cards(cards=huahai_cards, cols=4)

    huahai_html = md_to_html_simple(huahai_content)
    gen.add_analysis_section(
        title="六、华海诚科深度分析（A档 · GMC塑封料国产唯一）",
        content=f'<div class="prose-content">{huahai_html}</div>',
        icon="🚀"
    )

    # ================================================================
    # 七、长电科技深度分析（B档）
    # ================================================================
    ch4_3_match = re.search(r'(### 4\.3 长电科技.*?)(?=\n### 4\.4 )', md_content, re.DOTALL)
    changdian_content = ch4_3_match.group(1) if ch4_3_match else ""

    changdian_cards = [
        DataCard(title="HBM业务定位", value="B档",
                 subtitle="HBM3E外协封测", variant="warning"),
        DataCard(title="技术实力", value="XDFOI 4nm",
                 subtitle="8Hi良率98.5%", variant="primary"),
        DataCard(title="净利率制约", value="≈4%",
                 subtitle="低毛利天花板", variant="danger"),
        DataCard(title="目标价", value="105-115", unit="元",
                 subtitle="底仓配置", variant="warning"),
    ]
    gen.add_data_cards(cards=changdian_cards, cols=4)

    changdian_html = md_to_html_simple(changdian_content)
    gen.add_analysis_section(
        title="七、长电科技深度分析（B档 · HBM3E外协封测）",
        content=f'<div class="prose-content">{changdian_html}</div>',
        icon="🏭"
    )

    # ================================================================
    # 八、三大持仓股横向对比
    # ================================================================
    ch4_4_match = re.search(r'### 4\.4 三大持仓股横向对比.*?(?=\n## 5\.)', md_content, re.DOTALL)
    compare_content = ch4_4_match.group(0) if ch4_4_match else ""
    compare_html = md_to_html_simple(compare_content)

    gen.add_analysis_section(
        title="八、三大持仓股横向对比",
        content=f'<div class="prose-content">{compare_html}</div>',
        icon="⚖️"
    )

    # ================================================================
    # 九、产业链其他受益标的（分档排序）
    # ================================================================
    ch5_match = re.search(r'## 5\. A股核心标的综合评分.*?(?=\n## 6\.)', md_content, re.DOTALL)
    ch5_content = ch5_match.group(0) if ch5_match else ""
    ch5_html = md_to_html_simple(re.sub(r'^## .*\n', '', ch5_content, count=1))

    gen.add_analysis_section(
        title="九、产业链其他受益标的（S/A/B/C四档排序）",
        content=f'<div class="prose-content">{ch5_html}</div>',
        icon="🎯"
    )

    # ================================================================
    # 十、催化节奏与投资时点
    # ================================================================
    ch6_match = re.search(r'## 6\. 催化节奏与投资时点判断.*?(?=\n## 7\.)', md_content, re.DOTALL)
    ch6_content = ch6_match.group(0) if ch6_match else ""
    ch6_html = md_to_html_simple(re.sub(r'^## .*\n', '', ch6_content, count=1))

    gen.add_analysis_section(
        title="十、催化节奏与投资时点判断",
        content=f'<div class="prose-content">{ch6_html}</div>',
        icon="⏰"
    )

    # ================================================================
    # 十一、风险提示（多维度）
    # ================================================================
    risks = [
        "5000亿美元为远期意向框架，非约束合同，实际落地率可能低于40%",
        "HBM 2027H2-2028年产能集中释放，若AI需求放缓可能供过于求、ASP快速下跌",
        "美国对华芯片管制升级，可能影响中国材料企业向韩国供货的资质审查",
        "韩国半导体材料国产化政策（目标2030年自给率50%）长期施压替代风险",
        "短期估值偏高，AI主题炒作后1-2周内普遍出现10-20%回调",
        "持仓股个体风险：铜冠铜箔HVLP3良率仅30-40%、英维克Q1利润-82%、*ST建艺无关主题"
    ]
    gen.add_risk_section(risks=risks)

    ch7_match = re.search(r'## 7\. 风险因素.*?(?=\n## 8\.)', md_content, re.DOTALL)
    ch7_content = ch7_match.group(0) if ch7_match else ""
    ch7_html = md_to_html_simple(re.sub(r'^## .*\n', '', ch7_content, count=1))

    gen.add_analysis_section(
        title="风险因素深度分析",
        content=f'<div class="prose-content">{ch7_html}</div>',
        icon="⚠️"
    )

    # ================================================================
    # 十二、关键预判与非共识判断
    # ================================================================
    ch8_match = re.search(r'## 8\. 关键预判与非共识判断.*?(?=\n## 9\.)', md_content, re.DOTALL)
    ch8_content = ch8_match.group(0) if ch8_match else ""
    ch8_html = md_to_html_simple(re.sub(r'^## .*\n', '', ch8_content, count=1))

    gen.add_analysis_section(
        title="十一、关键预判与非共识判断",
        content=f'<div class="prose-content">{ch8_html}</div>',
        icon="💡"
    )

    # ================================================================
    # 十三、操作建议与具体买卖点位
    # ================================================================
    ch9_match = re.search(r'## 9\. 持仓股具体操作建议.*?(?=\n## 10\.)', md_content, re.DOTALL)
    ch9_content = ch9_match.group(0) if ch9_match else ""
    ch9_html = md_to_html_simple(re.sub(r'^## .*\n', '', ch9_content, count=1))

    gen.add_analysis_section(
        title="十二、操作建议与具体买卖点位",
        content=f'<div class="prose-content">{ch9_html}</div>',
        icon="📈"
    )

    # ================================================================
    # 十四、结论与结语
    # ================================================================
    gen.add_conclusion(
        conclusion=(
            "英伟达-SK 5000亿美元AI合作是2026下半年最重磅产业催化，但市场普遍误读其口径。"
            "核心结论：①5000亿为双向远期交易额，实际落地40-50%（2000-2500亿美元）；"
            "②产业链确定性排序：材料>设备>封装>算力基建>电力设备；"
            "③三大持仓确定性：雅克(S)>华海(A)>长电(B)；"
            "④严格区分真受益（雅克/华海/中际旭创）与伪概念（太极实业）；"
            "⑤短期情绪后必分化，等待回调建仓，中期持有穿越2027年业绩兑现主升浪。"
            "雅克科技作为HBM4前驱体独家供应商，是本次浪潮中A股最具确定性的硬资产，"
            "建议20-25%核心仓位长期持有。"
        ),
        rating="强烈推荐"
    )

    ch10_match = re.search(r'## 10\. 结论与结语.*', md_content, re.DOTALL)
    ch10_content = ch10_match.group(0) if ch10_match else ""
    ch10_html = md_to_html_simple(re.sub(r'^## .*\n', '', ch10_content, count=1))

    gen.add_analysis_section(
        title="结语",
        content=f'<div class="prose-content">{ch10_html}</div>',
        icon="📝"
    )

    return gen


# ============================================================
# 执行生成
# ============================================================
if __name__ == "__main__":
    print("🚀 开始生成英伟达×SK HBM深度研究报告...")
    generator = build_report()

    filename = "20260725_英伟达SK_5000亿AI投资HBM深度研究.html"
    out_dir = ROOT / "docs" / "industry_chain"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / filename

    html = generator.generate()
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(html)

    size_kb = out_path.stat().st_size / 1024
    print(f"✅ 报告已生成: {out_path}")
    print(f"📊 文件大小: {size_kb:.1f} KB")

    # 统计正文字数
    import re
    clean = re.sub(r'<[^>]+>', '', html)
    chinese_chars = len(re.findall(r'[\u4e00-\u9fa5]', clean))
    print(f"📝 正文中文字数: {chinese_chars}")

    # 验证
    errors = generator.validate()
    if errors:
        print(f"⚠️  验证发现 {len(errors)} 个问题:")
        for e in errors[:10]:
            print(f"   - {e}")
    else:
        print("✅ 验证通过")
