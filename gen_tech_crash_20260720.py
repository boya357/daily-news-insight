#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
科技板块大跌深度分析报告生成器 2026-07-20
基于 ProGenerator 基类（v3/generators/pro_base.py），深色玻璃态主题
内容来源: /app/data/所有对话/主对话/科技板块大跌深度分析_20260720.md
输出: docs/industry_chain/20260720_科技板块大跌深度分析.html
"""
import sys
import os
import re

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'v3'))

from generators.pro_base import ProGenerator, source_tag, CONF_HIGH, CONF_MEDIUM, CONF_LOW

MD_PATH = "/app/data/所有对话/主对话/科技板块大跌深度分析_20260720.md"
OUT_PATH = "/root/daily-news-insight/docs/industry_chain/20260720_科技板块大跌深度分析.html"

# 章节id映射（用于快速锚点）
SECTION_IDS = {
    "〇": "summary", "一": "review", "二": "sectors", "三": "attribution",
    "四": "judgment", "五": "bottom", "六": "forecast", "七": "strategy", "八": "appendix",
}


def inline_format(text):
    """行内格式转换"""
    # markdown转义星号还原（\*ST建艺 -> *ST建艺）
    text = text.replace('\\*', '*')
    # 图片
    text = re.sub(r'!\[([^\]]*)\]\(([^)]+)\)',
                  r'<figure class="my-5"><img src="\2" alt="\1" class="max-w-full rounded-xl border border-white/10 shadow-lg" loading="lazy">'
                  r'<figcaption class="text-white/40 text-xs mt-2">\1</figcaption></figure>', text)
    # [(名称)](url) 引用格式 -> 来源标签链接
    text = re.sub(r'\[\(([^)]+)\)\]\((https?://[^)]+)\)',
                  r'<a href="\2" target="_blank" rel="noopener" class="text-indigo-300 hover:text-indigo-200 text-xs align-super no-underline">[\1]</a>', text)
    # 普通链接
    text = re.sub(r'\[([^\]]+)\]\((https?://[^)]+)\)',
                  r'<a href="\2" target="_blank" rel="noopener" class="text-indigo-300 hover:text-indigo-200">\1</a>', text)
    # 粗体（非贪婪匹配以支持 \* 转义星号，如 \*ST建艺）
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong class="text-white font-bold">\1</strong>', text)
    # 斜体（排除已处理的）
    text = re.sub(r'(?<!\*)\*([^*\n]+)\*(?!\*)', r'<em class="text-amber-300/90 not-italic">\1</em>', text)
    # 【推断】/【事实】标记
    text = text.replace('【推断】', '<span class="inline-block bg-amber-500/15 text-amber-300 border border-amber-500/30 px-1.5 py-0.5 rounded text-xs font-bold">推断</span>')
    text = text.replace('【事实】', '<span class="inline-block bg-emerald-500/15 text-emerald-300 border border-emerald-500/30 px-1.5 py-0.5 rounded text-xs font-bold">事实</span>')
    # 行内代码
    text = re.sub(r'`([^`]+)`', r'<code class="bg-purple-500/15 text-purple-300 px-1.5 py-0.5 rounded text-sm">\1</code>', text)
    return text


def convert_table(lines):
    """表格转换（深色玻璃态）"""
    rows = []
    for ln in lines:
        cells = [c.strip() for c in ln.strip().strip('|').split('|')]
        rows.append(cells)
    if len(rows) < 2:
        return '\n'.join('<p class="text-white/80">' + inline_format(l) + '</p>' for l in lines)
    html = '<div class="overflow-x-auto my-4 rounded-xl border border-white/10"><table class="w-full text-sm">'
    # 表头
    html += '<thead><tr class="bg-indigo-500/20">'
    for c in rows[0]:
        html += '<th class="px-3 py-2.5 text-left text-white font-bold border-b border-indigo-400/30 whitespace-nowrap">' + inline_format(c) + '</th>'
    html += '</tr></thead><tbody>'
    # 数据行（跳过分隔行 rows[1]）
    for row in rows[2:]:
        html += '<tr class="border-b border-white/5 hover:bg-purple-500/5 transition-colors">'
        for c in row:
            html += '<td class="px-3 py-2 text-white/80">' + inline_format(c) + '</td>'
        html += '</tr>'
    html += '</tbody></table></div>'
    return html


def md_block_to_html(lines):
    """将一个章节内的markdown行列表转为HTML"""
    html_parts = []
    i = 0
    in_list = None  # 'ul' or 'ol'
    while i < len(lines):
        ln = lines[i]
        stripped = ln.strip()

        # 空行：关闭列表
        if not stripped:
            if in_list:
                html_parts.append('</' + in_list + '>')
                in_list = None
            i += 1
            continue

        # 表格块
        if stripped.startswith('|') and i + 1 < len(lines) and re.match(r'^\s*\|[\s:\-|]+\|\s*$', lines[i + 1]):
            if in_list:
                html_parts.append('</' + in_list + '>')
                in_list = None
            tbl = []
            while i < len(lines) and lines[i].strip().startswith('|'):
                tbl.append(lines[i])
                i += 1
            html_parts.append(convert_table(tbl))
            continue

        # h3
        if stripped.startswith('### '):
            if in_list:
                html_parts.append('</' + in_list + '>')
                in_list = None
            html_parts.append('<h3 class="text-lg md:text-xl font-bold text-purple-300 mt-6 mb-3 flex items-center gap-2">'
                              '<span class="w-1 h-5 bg-gradient-to-b from-indigo-400 to-purple-500 rounded-full inline-block"></span>'
                              + inline_format(stripped[4:]) + '</h3>')
            i += 1
            continue

        # h4
        if stripped.startswith('#### '):
            if in_list:
                html_parts.append('</' + in_list + '>')
                in_list = None
            html_parts.append('<h4 class="text-base font-bold text-indigo-300 mt-4 mb-2">' + inline_format(stripped[5:]) + '</h4>')
            i += 1
            continue

        # 引用块
        if stripped.startswith('>'):
            if in_list:
                html_parts.append('</' + in_list + '>')
                in_list = None
            quote_lines = []
            while i < len(lines) and lines[i].strip().startswith('>'):
                quote_lines.append(lines[i].strip().lstrip('>').strip())
                i += 1
            html_parts.append('<div class="bg-amber-500/10 border-l-4 border-amber-500/60 rounded-r-xl px-5 py-3 my-4 text-amber-200/90 text-sm leading-relaxed">'
                              + inline_format(' '.join(quote_lines)) + '</div>')
            continue

        # 分隔线
        if stripped == '---':
            if in_list:
                html_parts.append('</' + in_list + '>')
                in_list = None
            html_parts.append('<hr class="border-white/10 my-6">')
            i += 1
            continue

        # 无序列表
        if stripped.startswith('- '):
            if in_list != 'ul':
                if in_list:
                    html_parts.append('</' + in_list + '>')
                html_parts.append('<ul class="space-y-2 my-3 pl-1">')
                in_list = 'ul'
            html_parts.append('<li class="text-white/80 text-[15px] leading-relaxed flex gap-2">'
                              '<span class="text-purple-400 flex-shrink-0 mt-1">▪</span><span>' + inline_format(stripped[2:]) + '</span></li>')
            i += 1
            continue

        # 有序列表
        m = re.match(r'^(\d+)\.\s+(.*)$', stripped)
        if m:
            if in_list != 'ol':
                if in_list:
                    html_parts.append('</' + in_list + '>')
                html_parts.append('<ol class="space-y-2 my-3 pl-1 list-none">')
                in_list = 'ol'
            html_parts.append('<li class="text-white/80 text-[15px] leading-relaxed flex gap-2">'
                              '<span class="text-indigo-400 font-bold flex-shrink-0">' + m.group(1) + '.</span><span>'
                              + inline_format(m.group(2)) + '</span></li>')
            i += 1
            continue

        # 普通段落
        if in_list:
            html_parts.append('</' + in_list + '>')
            in_list = None
        html_parts.append('<p class="text-white/80 text-[15px] leading-relaxed my-3">' + inline_format(stripped) + '</p>')
        i += 1

    if in_list:
        html_parts.append('</' + in_list + '>')
    return '\n'.join(html_parts)


def md_to_sections(md_text):
    """将整篇markdown按 ## 切分为 前言 + 各章节"""
    lines = md_text.split('\n')
    preamble = []
    sections = []  # [(title, content_lines)]
    cur_title = None
    cur_lines = []
    for ln in lines:
        if ln.startswith('## '):
            if cur_title is not None:
                sections.append((cur_title, cur_lines))
            elif cur_lines:
                preamble = cur_lines
            cur_title = ln[3:].strip()
            cur_lines = []
        else:
            cur_lines.append(ln)
    if cur_title is not None:
        sections.append((cur_title, cur_lines))
    return preamble, sections


class TechCrashReportGenerator(ProGenerator):
    data_type = "industry_chain"

    def __init__(self):
        super().__init__(
            title="科技板块大跌深度分析：归因、定性与抄底路线图",
            active_page="产业链",
            footer_text="科技板块大跌深度分析 · PCB/铜箔/存储/HBM/设备材料 · 2026-07-20收盘",
            show_toc=False,
            theme="dark",
            tldr=[
                "【定性】7·20科技股大跌是7·17开启的<b class='text-amber-300'>牛市中期结构性调整第二阶段</b>（置信度70%）：沪指尾盘V型收涨0.85%报3796.28，但全市场186只跌停——政策托指数+杠杆出清成长的复合形态，非趋势反转。",
                "【归因】337-TA-1511调查+澜起反垄断+Kyber争议+Kimi时刻+油价破90五大利空，撞上两融单周-1678亿(2019年来最大)的去杠杆火药桶；铜冠铜箔业绩+486%仍20cm跌停=杀斜率不杀逻辑。",
                "【抄底】可以抄但不接第一刀：按<b class='text-green-300'>铜箔＞PCB龙头＞存储(有业绩者)＞HBM材料＞设备</b>优先级分三批，左侧≤30%仓位，单票-15%减半/-25%清仓，沪指破3600全面退出。",
            ],
            operation_advice="持仓处理：守铜冠(破88减半)/守雅克(破110减半不加仓)/减英维克(Q1业绩-82%硬伤，反弹60上方减)/*ST建艺独立处理；新仓等跌停打开+龙虎榜/两融信号，7/27长鑫挂牌是关键节点。",
            risk_level="高（科技板块单日186只跌停，杠杆出清未确认结束）",
            suggested_position="左侧抄底≤30%，总仓位建议60-70%，保留现金等右侧",
            quick_anchors=[
                {"id": "summary", "title": "核心结论", "icon": "🎯"},
                {"id": "review", "title": "盘面复盘", "icon": "📊"},
                {"id": "sectors", "title": "板块拆解", "icon": "🔬"},
                {"id": "attribution", "title": "深度归因", "icon": "🔍"},
                {"id": "judgment", "title": "牛熊判断", "icon": "⚖️"},
                {"id": "bottom", "title": "抄底策略", "icon": "💰"},
                {"id": "forecast", "title": "情景推演", "icon": "🔮"},
                {"id": "strategy", "title": "持仓操作", "icon": "💼"},
            ],
            holding_stocks=[
                {"name": "英维克", "code": "002837"},
                {"name": "铜冠铜箔", "code": "301217"},
                {"name": "雅克科技", "code": "002409"},
                {"name": "*ST建艺", "code": "002789"},
            ],
            og_description="2026-07-20科技板块大跌深度分析：PCB/铜箔/存储/HBM/设备材料五大板块归因拆解，牛市中期调整定性（70%置信度），分板块抄底价位表+止损纪律+四只持仓操作优先级。",
        )

    def load_data(self):
        super().load_data()
        self.update_time = "2026年7月20日 15:30（收盘后）"
        self.cite("腾讯自选股实时行情接口(2026-07-20收盘)", CONF_HIGH)
        self.cite("证监会/中国国新/中国诚通公告(2026-07-20)", CONF_HIGH)
        self.cite("公司业绩预告:铜冠铜箔/富创精密/澜起科技/香农芯创(2026-07)", CONF_HIGH)
        self.cite("财联社/证券时报:两融与ETF资金数据(2026-07-20)", CONF_HIGH)
        self.cite("美国ITC 337-TA-1511立案公告(2026-07-15)", CONF_HIGH)
        self.cite("界面新闻/上证报/中国证券报(2026-07-19/20)", CONF_HIGH)
        self.cite("十大券商策略观点汇总(2026-07-19/20)", CONF_MEDIUM)
        self.cite("SemiAnalysis报告与黄仁勋表态(2026-07，矛盾并列)", CONF_MEDIUM)
        self.cite("东方财富Choice/自媒体复盘(交叉验证后采用)", CONF_MEDIUM)

    def _hero_kpi(self):
        items = [
            ("沪指收盘", "3796.28", "text-green-400", "+0.85% 尾盘V型"),
            ("全市场跌停", "186只", "text-red-400", "14时许口径"),
            ("两市成交", "2.70万亿", "text-white", "连续放量"),
            ("铜冠铜箔", "-20.00%", "text-red-400", "业绩+486%仍跌停"),
            ("雅克科技", "-10.00%", "text-red-400", "跌停封死"),
            ("澜起科技", "+3.45%", "text-green-400", "先跌40%先企稳"),
            ("两融周变动", "-1678亿", "text-red-400", "2019年来最大"),
            ("ETF周流入", "+2113亿", "text-green-400", "配置盘逆势买入"),
        ]
        html = '<div class="grid grid-cols-2 md:grid-cols-4 gap-3 mb-6">'
        for label, value, color, sub in items:
            html += ('<div class="bg-white/[0.04] border border-white/10 rounded-xl p-3 text-center">'
                     '<div class="text-xs text-white/50 mb-1">' + label + '</div>'
                     '<div class="' + color + ' text-xl md:text-2xl font-black tracking-tight">' + value + '</div>'
                     '<div class="text-[10px] text-white/40 mt-1">' + sub + '</div></div>')
        html += '</div>'
        return html

    def _content(self):
        with open(MD_PATH, 'r', encoding='utf-8') as f:
            md = f.read()

        preamble, sections = md_to_sections(md)

        parts = []
        # Hero KPI
        parts.append(self._hero_kpi())

        # 前言（报告头+风险声明）
        pre_html = md_block_to_html([l for l in preamble if not l.startswith('# ')])
        if pre_html.strip():
            parts.append('<div class="card-glass p-5 mb-6 text-sm">' + pre_html + '</div>')

        # 各章节
        for title, lines in sections:
            # 提取章节序号汉字 -> id
            m = re.match(r'^([〇一二三四五六七八])、', title)
            sec_id = SECTION_IDS.get(m.group(1), "sec") if m else "sec"
            body = md_block_to_html(lines)
            parts.append(
                '<section id="' + sec_id + '" class="mb-8 scroll-mt-24">'
                '<div class="flex items-center gap-3 mb-4 pb-3 border-b border-white/10">'
                '<h2 class="text-xl md:text-2xl font-black text-white tracking-tight">'
                '<span class="inline-block w-1.5 h-7 bg-gradient-to-b from-indigo-400 to-purple-500 rounded-full mr-2 align-middle"></span>'
                + inline_format(title) + '</h2></div>'
                '<div class="card-glass p-5 md:p-7">' + body + '</div>'
                '</section>'
            )

        # 数据溯源说明
        parts.append(
            '<div class="card-glass p-5 mt-8 text-xs text-white/50">'
            '<b class="text-white/70">数据溯源：</b>行情数据来自腾讯自选股实时行情接口（2026-07-20 15:00收盘终值）；'
            '新闻与公告均标注来源媒体、URL与数据日期；推断性内容以<span class="text-amber-300">[推断]</span>标记。'
            '完整证据链见 evidence 文件。本报告不构成投资建议。'
            '</div>'
        )
        return '\n'.join(parts)


def main():
    g = TechCrashReportGenerator()
    g.load_data()
    res = g.publish(OUT_PATH)
    print("结果:", res)
    if not res.get('success'):
        print("ERRORS:", res.get('errors'))
        return 1
    print("OK 报告已生成:", OUT_PATH)
    print("   文件大小: %.1f KB" % (res['file_size'] / 1024))
    return 0


if __name__ == "__main__":
    sys.exit(main())
