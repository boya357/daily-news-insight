"""
生成器基类模块 - 标准化生成器接口
所有Pro版生成器都应继承自此基类

V5.0 升级 - L1级内容深度增强（2026-07-03）:
- L1-1 数据来源标注+置信度+双源验证：新增 source_tag / verify_market_data 等组件方法
- L1-3 空方视角/证伪条件：新增 _risk_section() 模板方法，S级催化/持仓诊断强制接入
- L1-5 教训库接入：build_lessons_section() 自动挂载"📚 历史教训回顾"模块
"""
import sys
import os
import re
from typing import Dict, List, Optional, Any, Tuple
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from components.pro import ProPage, TabPane, CardGroup, DataGrid, GlassCard
from utils.data_loader import DataLoader, get_data_loader


# ============================================================
# 置信度常量 (L1-1)
# ============================================================
CONF_HIGH = "high"      # 🔴高：官方披露 / 交易所 / 多源交叉验证
CONF_MEDIUM = "medium"  # 🟡中：单一权威媒体（财联社/韭研公社/科创板日报等）
CONF_LOW = "low"        # ⚪低：传闻 / 网传 / 未证实 / 单一社交媒体

CONF_ICON = {
    CONF_HIGH: "🔴",
    CONF_MEDIUM: "🟡",
    CONF_LOW: "⚪",
}
CONF_LABEL = {
    CONF_HIGH: "高",
    CONF_MEDIUM: "中",
    CONF_LOW: "低",
}


def source_tag(source: str = "综合", confidence: str = CONF_MEDIUM,
               verified: bool = False, rumor: bool = False) -> str:
    """统一数据来源标注组件 (L1-1)
    
    输出格式: [来源: 财联社 | 置信度: 高🔴 | 双源验证✅]
    未验证传闻自动追加 ⚠️未经证实，仅供参考
    
    Args:
        source: 来源名称（财联社/韭研公社/上交所/公司公告/TheElec等）
        confidence: 置信度等级 CONF_HIGH/CONF_MEDIUM/CONF_LOW
        verified: 是否经过双源交叉验证
        rumor: 是否为未证实传闻
    """
    icon = CONF_ICON.get(confidence, "🟡")
    label = CONF_LABEL.get(confidence, "中")
    verify_html = ' | <span class="text-green-400">双源验证✅</span>' if verified else ''
    rumor_html = ' <span class="text-yellow-400 font-semibold">⚠️未经证实，仅供参考</span>' if rumor or confidence == CONF_LOW else ''
    return (
        f'<span class="inline-flex items-center gap-1 text-[11px] text-white/50 '
        f'bg-white/5 border border-white/10 rounded px-1.5 py-0.5 ml-1 align-middle">'
        f'来源: <span class="text-white/70">{source}</span> | '
        f'置信度: <span class="text-white/70">{label}</span>{icon}{verify_html}'
        f'</span>{rumor_html}'
    )


def unverified(source: str = "网传/社交媒体") -> str:
    """快捷方法：标注未证实传闻"""
    return source_tag(source=source, confidence=CONF_LOW, rumor=True)


class ProGenerator(ProPage):
    """Pro版生成器基类
    
    统一所有Pro版生成器的接口规范：
    - 标准化的数据加载方式
    - 统一的发布流程
    - 一致的错误处理
    - V5.0：来源标注 / 空方视角 / 教训库 三大组件
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
                 theme: str = "dark",
                 # V5.0 L2 参数透传
                 tldr: list = None, operation_advice: str = "",
                 quick_anchors: list = None,
                 holding_stocks: list = None,
                 og_description: str = "", og_image: str = "",
                 risk_level: str = "", suggested_position: str = ""):
        super().__init__(
            title=title,
            active_page=active_page,
            footer_text=footer_text,
            update_time="",
            show_toc=show_toc,
            toc_position=toc_position,
            theme=theme,
            # V5.0 L2
            tldr=tldr, operation_advice=operation_advice,
            quick_anchors=quick_anchors,
            holding_stocks=holding_stocks,
            og_description=og_description, og_image=og_image,
            risk_level=risk_level, suggested_position=suggested_position,
        )
        self.data_loader: DataLoader = get_data_loader(data_dir)
        self._data_loaded = False
        self._output_path = ""
        # V5.0：当日上下文关键词（供教训库匹配用）
        self._context_keywords: List[str] = []
        self._lessons_matched: List[Dict[str, Any]] = []
        # V5.0：本报告引用的数据来源统计（用于末尾数据溯源）
        self._source_stats: Dict[str, int] = {}
        # V5.0：双源验证失败记录
        self._verify_failures: List[str] = []
    
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
        
        # V5.0 L2：默认持仓配置（未手动传入时使用主人核心持仓）
        if not self.holding_stocks:
            self.holding_stocks = [
                {"name": "英维克", "code": "002837"},
                {"name": "铜冠铜箔", "code": "301217"},
                {"name": "雅克科技", "code": "002409"},
                {"name": "*ST建艺", "code": "002789"},
            ]
        # 默认快速锚点（未手动传入时使用标准5项）
        if not self.quick_anchors:
            self.quick_anchors = [
                {"id": "portfolio", "title": "持仓诊断", "icon": "💼"},
                {"id": "slevel", "title": "S级催化", "icon": "🔥"},
                {"id": "topics", "title": "热点题材", "icon": "📊"},
                {"id": "longhubang", "title": "龙虎榜", "icon": "🐉"},
                {"id": "risk", "title": "风险提示", "icon": "⚠️"},
            ]
        
        self._data_loaded = True
    
    # ==================== V5.0 L1-1 数据来源+置信度+双源验证 ====================
    
    def cite(self, source: str = "综合", confidence: str = CONF_MEDIUM,
             verified: bool = False, rumor: bool = False) -> str:
        """实例方法：在生成器内部引用数据来源（自动统计）"""
        self._source_stats[source] = self._source_stats.get(source, 0) + 1
        return source_tag(source=source, confidence=confidence,
                          verified=verified, rumor=rumor)
    
    def add_context_keywords(self, keywords: List[str]):
        """注入当日上下文关键词，用于教训库匹配"""
        for kw in keywords:
            if kw and kw not in self._context_keywords:
                self._context_keywords.append(kw)
    
    def verify_market_data(self, primary: Any, secondary: Any,
                           tolerance: float = 0.02, label: str = "") -> Tuple[bool, Any, str]:
        """关键行情数据双源验证 (L1-1)
        
        关键行情数据（指数/股价/涨跌幅/资金流向）必须双源交叉验证。
        允许 tolerance 内的数值差异（默认2%）。
        不一致时记录到 _verify_failures 并采用 primary 值，同时标注待复核。
        
        Args:
            primary: 主源数值
            secondary: 副源数值
            tolerance: 允许的相对误差
            label: 数据项名称（用于日志）
        
        Returns:
            (通过, 采用值, 提示HTML)
        """
        try:
            p = float(primary)
            s = float(secondary)
            diff = abs(p - s)
            base = max(abs(p), abs(s), 1e-6)
            rel = diff / base
            if rel <= tolerance:
                return True, primary, ""
            else:
                msg = f"{label}双源分歧: 主源={primary} 副源={secondary} 偏差{rel:.2%}"
                self._verify_failures.append(msg)
                warn_html = (
                    f'<span class="text-yellow-400 text-[11px] ml-1">'
                    f'⚠️双源偏差{rel:.1%}，采用主源{primary}</span>'
                )
                return False, primary, warn_html
        except (TypeError, ValueError):
            msg = f"{label}双源验证失败: 非数值"
            self._verify_failures.append(msg)
            return False, primary, '<span class="text-red-400 text-[11px] ml-1">⚠️待复核</span>'
    
    def _source_summary_section(self) -> str:
        """末尾"数据来源统计"模块（仅当有引用时渲染）"""
        if not self._source_stats:
            return ""
        items = sorted(self._source_stats.items(), key=lambda x: -x[1])
        tags = ' '.join([
            f'<span class="bg-white/5 text-white/70 text-xs px-2 py-1 rounded border border-white/10">{s} <span class="text-white/40">×{c}</span></span>'
            for s, c in items
        ])
        fail_html = ""
        if self._verify_failures:
            fail_html = '<div class="mt-2 text-xs text-yellow-400/80">⚠️ 存在' + str(len(self._verify_failures)) + '项双源偏差，已标注待复核</div>'
        return f'''
        <div class="mt-4 p-3 bg-white/[0.03] rounded-lg border border-white/5">
            <div class="text-xs text-white/40 mb-2">📡 本报告数据来源（{len(items)}个源 / {sum(self._source_stats.values())}次引用）</div>
            <div class="flex flex-wrap gap-1.5">{tags}</div>
            {fail_html}
        </div>
        '''
    
    # ==================== V5.0 L1-3 空方视角/证伪条件模块 ====================
    
    def _risk_section(self, title: str = "🔴 证伪条件/空方逻辑",
                      falsify_signals: List[str] = None,
                      stop_loss: str = "",
                      bear_logic: List[str] = None,
                      contrarian_view: str = "") -> str:
        """通用风险/空方视角模块 (L1-3)
        
        每个S级机会 / 持仓诊断必须回答：
        1) 什么信号会证伪做多逻辑？
        2) 跌到哪里必须止损？
        3) 空方的核心反驳逻辑是什么？
        """
        falsify_signals = falsify_signals or ["核心催化落空", "龙头放量跌破关键均线"]
        bear_logic = bear_logic or ["情绪退潮高位补跌", "资金切换至低位板块"]
        
        falsify_html = ''.join([
            f'<li class="flex gap-2 mb-1"><span class="text-red-400 flex-shrink-0">✗</span><span class="text-white/70 text-sm">{x}</span></li>'
            for x in falsify_signals
        ])
        bear_html = ''.join([
            f'<li class="flex gap-2 mb-1"><span class="text-yellow-400 flex-shrink-0">◌</span><span class="text-white/70 text-sm">{x}</span></li>'
            for x in bear_logic
        ])
        stop_html = ""
        if stop_loss:
            stop_html = f'''
            <div class="bg-red-500/10 border border-red-500/30 rounded-lg px-3 py-2 mb-3">
                <span class="text-red-400 text-xs font-bold">⛔ 硬止损位：</span>
                <span class="text-white font-bold text-sm">{stop_loss}</span>
                <span class="text-white/50 text-xs ml-1">（跌破无条件离场）</span>
            </div>
            '''
        contra_html = ""
        if contrarian_view:
            contra_html = f'''
            <div class="bg-yellow-500/5 border border-yellow-500/20 rounded-lg px-3 py-2 mb-3">
                <div class="text-yellow-400 text-xs font-bold mb-1">💡 反方观点</div>
                <p class="text-white/70 text-sm leading-relaxed">{contrarian_view}</p>
            </div>
            '''
        return f'''
        <div class="bg-gradient-to-r from-red-900/20 via-red-500/10 to-transparent border-l-4 border-red-500/60 rounded-r-xl p-4 mt-3">
            <div class="flex items-center gap-2 mb-3">
                <span class="text-lg">🔴</span>
                <span class="text-red-400 font-bold">{title}</span>
                <span class="ml-auto text-[10px] text-white/40 bg-white/5 px-2 py-0.5 rounded">V5.0 必选项</span>
            </div>
            {contra_html}
            {stop_html}
            <div class="grid grid-cols-1 md:grid-cols-2 gap-3">
                <div>
                    <div class="text-xs text-red-400/80 font-bold mb-1">❌ 证伪信号（出现即离场）</div>
                    <ul class="list-none p-0 m-0">{falsify_html}</ul>
                </div>
                <div>
                    <div class="text-xs text-yellow-400/80 font-bold mb-1">⚠️ 空方核心逻辑</div>
                    <ul class="list-none p-0 m-0">{bear_html}</ul>
                </div>
            </div>
        </div>
        '''
    
    # ==================== V5.0 L1-5 历史教训库接入 ====================
    
    def load_lessons(self, keywords: List[str] = None, top_k: int = 3) -> List[Dict[str, Any]]:
        """加载并匹配错误教训库 (L1-5)
        
        根据当日关键词/板块/事件匹配历史教训，供报告末尾展示。
        """
        if keywords:
            self.add_context_keywords(keywords)
        try:
            from lessons_learner import LessonsLearner
            learner = LessonsLearner()
            self._lessons_matched = learner.match(self._context_keywords, top_k=top_k)
        except Exception as e:
            self._lessons_matched = []
            print(f"[Warn] load_lessons 失败: {e}")
        return self._lessons_matched
    
    def build_lessons_section(self, keywords: List[str] = None,
                              title: str = "📚 历史教训回顾",
                              top_k: int = 3) -> str:
        """构建"📚 历史教训回顾"模块
        
        应在每份报告末尾调用，自动匹配相关历史教训。
        """
        if not self._lessons_matched:
            self.load_lessons(keywords=keywords, top_k=top_k)
        if not self._lessons_matched:
            return ""
        cards = []
        for lesson in self._lessons_matched[:top_k]:
            score = lesson.get("score", 0)
            tag_html = ""
            tags = lesson.get("tags", [])
            if tags:
                tag_html = '<div class="flex flex-wrap gap-1 mt-2">' + ' '.join([
                    f'<span class="bg-white/5 text-white/50 text-[10px] px-1.5 py-0.5 rounded">{t}</span>'
                    for t in tags
                ]) + '</div>'
            cards.append(f'''
            <div class="bg-white/[0.03] border border-white/10 rounded-lg p-3">
                <div class="flex items-start justify-between gap-2 mb-1">
                    <div class="text-white/90 font-semibold text-sm">📌 {lesson.get('title', '历史教训')}</div>
                    <span class="text-[10px] text-orange-400 bg-orange-500/10 px-1.5 py-0.5 rounded flex-shrink-0">相关度 {score:.0%}</span>
                </div>
                <p class="text-white/60 text-xs leading-relaxed">{lesson.get('summary', '')}</p>
                {tag_html}
            </div>
            ''')
        return f'''
        <div class="mt-4">
            <h3 class="text-sm font-bold text-white/90 mb-2 flex items-center gap-2">
                <span>{title}</span>
                <span class="text-white/40 text-[11px] font-normal">（基于当日关键词自动匹配）</span>
            </h3>
            <div class="grid grid-cols-1 md:grid-cols-{min(3, max(1, len(cards)))} gap-2">
                {''.join(cards)}
            </div>
        </div>
        '''
    
    # ==================== 历史报告入口（2026-07-07） ====================

    # 报告频道名到 docs 子目录的映射（用于"📚 查看历史报告"链接推导）
    # 键：子类中常见的 report_type / data_type 标识；值：docs/ 下的目录名
    _CHANNEL_DIR_MAP = {
        "daily": "daily",
        "intraday": "intraday",
        "aftermarket": "aftermarket",
        "s_level_catalyst": "s_level_catalyst",
        "tomorrow_catalyst": "tomorrow_catalyst",
        "weekend_express": "weekend_express",
        "weekly_review": "weekly_review",
        "industry_chain": "industry_chain",
        "industry_chain_clock": "industry_chain",
        "monthly": "monthly",
    }
    # 报告频道中文名（用于按钮文案）
    _CHANNEL_LABEL_MAP = {
        "daily": "历史日报",
        "intraday": "历史盘中",
        "aftermarket": "历史盘后",
        "s_level_catalyst": "历史S级催化",
        "tomorrow_catalyst": "历史明日催化",
        "weekend_express": "历史周末速递",
        "weekly_review": "历史周度复盘",
        "industry_chain": "产业链历史报告",
        "monthly": "历史月报",
    }

    def _detect_channel_dir(self) -> Optional[str]:
        """根据当前生成器的 report_type / data_type / active_page 自动推导频道目录名。
        无法识别时返回 None（不渲染历史入口，避免无效链接）。
        """
        candidates = []
        for attr in ("report_type", "data_type"):
            v = getattr(self, attr, None)
            if v:
                candidates.append(v)
        ap = getattr(self, "active_page", "") or ""
        _AP_MAP = {
            "日报": "daily",
            "盘中": "intraday",
            "盘后": "aftermarket",
            "S级": "s_level_catalyst",
            "明日催化": "tomorrow_catalyst",
            "周末速递": "weekend_express",
            "周度复盘": "weekly_review",
            "产业链": "industry_chain",
            "月报": "monthly",
        }
        if ap in _AP_MAP:
            candidates.append(_AP_MAP[ap])
        for c in candidates:
            if c in self._CHANNEL_DIR_MAP:
                return self._CHANNEL_DIR_MAP[c]
        return None

    def _history_entry_html(self) -> str:
        """渲染"📚 查看历史报告"入口卡片 HTML。
        放在报告正文末尾、footer 之前；非报告页面（检测不到频道）返回空串。
        """
        channel = self._detect_channel_dir()
        if not channel:
            return ""
        label = self._CHANNEL_LABEL_MAP.get(channel, "历史报告")
        # 相对路径：报告页位于 docs/<channel>/xxx.html → 列表页 docs/<channel>/index.html
        href = "./index.html"
        return f"""
        <div class="history-entry-wrap" style="margin:2.5rem auto 0.5rem auto; max-width:32rem; text-align:center;">
            <a href="{href}"
               class="history-entry-link"
               style="display:inline-flex !important; align-items:center !important; gap:0.5rem !important;
                      padding:0.7rem 1.4rem !important;
                      background:rgba(255,255,255,0.06) !important;
                      border:1px solid rgba(255,255,255,0.14) !important;
                      border-radius:999px !important;
                      color:rgba(255,255,255,0.82) !important;
                      font-size:0.92rem !important;
                      font-weight:500 !important;
                      text-decoration:none !important;
                      backdrop-filter:blur(12px) !important;
                      -webkit-backdrop-filter:blur(12px) !important;
                      box-shadow:0 6px 20px rgba(0,0,0,0.25) !important;
                      transition:all .25s ease !important;">
                <span style="font-size:1.05rem;">📚</span>
                <span>查看{label}</span>
                <span style="opacity:.75; margin-left:2px;">→</span>
            </a>
        </div>
        <style>
            .history-entry-link:hover {{
                background:rgba(102,126,234,0.22) !important;
                border-color:rgba(139,92,246,0.45) !important;
                color:#fff !important;
                transform:translateY(-1px) !important;
                box-shadow:0 10px 28px rgba(102,126,234,0.35) !important;
            }}
            @media (max-width: 640px) {{
                .history-entry-wrap {{ margin-top:1.75rem !important; }}
                .history-entry-link {{ font-size:0.88rem !important; padding:0.6rem 1.1rem !important; }}
            }}
        </style>
        """

    def render(self) -> str:
        """渲染完整HTML页面（确保数据已加载）。
        在正文末尾、footer 之前自动注入"📚 查看历史报告"入口。
        """
        if not self._data_loaded:
            self.load_data()
        html = super().render()
        entry = self._history_entry_html()
        if entry:
            footer_patterns = [
                '<div class="pro-footer',
                '<div class="text-center text-white/40 text-sm py-10"',
            ]
            inserted = False
            for pat in footer_patterns:
                idx = html.find(pat)
                if idx != -1:
                    html = html[:idx] + entry + html[idx:]
                    inserted = True
                    break
            if not inserted:
                main_marker = 'id="mainContent"'
                mi = html.find(main_marker)
                if mi != -1:
                    last_close = html.rfind('</div>', mi)
                    if last_close != -1:
                        html = html[:last_close] + entry + html[last_close:]
                        inserted = True
        return html

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

    # ==================== V5.0 L2-1 TL;DR + 快速锚点 + 持仓金色高亮 便捷方法 ====================
    
    def set_tldr(self, key_points: List[str], operation_advice: str = "",
                risk_level: str = "", suggested_position: str = ""):
        """设置TL;DR卡片：3条核心结论+今日操作建议+风险/仓位
        
        Args:
            key_points: 3条以内核心结论
            operation_advice: 今日操作建议（红/绿色高亮）
            risk_level: 风险等级（中低/中/中高/高）
            suggested_position: 建议仓位（如3-4成）
        """
        self.tldr = key_points[:3]
        self.operation_advice = operation_advice
        self.risk_level = risk_level
        self.suggested_position = suggested_position
    
    def set_quick_anchors(self, anchors: List[Dict[str, str]]):
        """设置右侧悬浮快速锚点
        
        Args:
            anchors: [{"id":"xxx","title":"持仓诊断","icon":"💼"}, ...]
        """
        self.quick_anchors = anchors
    
    def set_holdings(self, stocks: List[Dict[str, str]]):
        """设置持仓股，用于报告中自动金色高亮
        
        Args:
            stocks: [{"name":"英维克","code":"002837"}, ...]
        """
        self.holding_stocks = stocks
    
    def set_og(self, description: str = "", image: str = ""):
        """设置OG分享元信息"""
        if description:
            self.og_description = description
        if image:
            self.og_image = image
    
    @staticmethod
    def stock_tag(name: str, code: str = "", is_holding: bool = False, 
                  change_pct: float = None, tag: str = "") -> str:
        """股票标签组件 (V5.0 L2-4)
        
        持仓股自动金色边框+持仓图标；非持仓股默认玻璃态样式。
        
        Args:
            name: 股票名称
            code: 股票代码
            is_holding: 是否为持仓股（金色高亮）
            change_pct: 涨跌幅%，自动红绿色
            tag: 额外标签（如"主线"/"ST"）
        """
        classes = "stock-tag"
        if is_holding:
            classes += " stock-tag-holding"
        pct_html = ""
        if change_pct is not None:
            color = "text-red-400" if change_pct >= 0 else "text-green-400"
            sign = "+" if change_pct >= 0 else ""
            pct_html = f'<span class="{color} font-bold ml-1">{sign}{change_pct:.2f}%</span>'
        code_html = f'<span class="text-white/40 text-[10px] ml-1">{code}</span>' if code else ""
        tag_html = ""
        if is_holding:
            tag_html = '<span class="holding-badge">⭐持仓</span>'
        elif tag:
            tag_html = f'<span class="text-white/50 text-[10px] bg-white/5 px-1 rounded ml-1">{tag}</span>'
        return (
            f'<span class="{classes}">'
            f'{tag_html}'
            f'<span class="stock-tag-name">{name}</span>'
            f'{code_html}'
            f'{pct_html}'
            f'</span>'
        )
    
    @staticmethod
    def highlight_number(value: str, color: str = "primary", size: str = "lg") -> str:
        """关键数据大号加粗高对比组件
        
        Args:
            value: 要显示的数值
            color: primary/warning/danger/success/info
            size: sm/md/lg/xl/2xl
        """
        color_map = {
            "primary": "text-purple-300",
            "warning": "text-yellow-400",
            "danger": "text-red-400",
            "success": "text-green-400",
            "info": "text-blue-400",
        }
        size_map = {
            "sm": "text-base", "md": "text-lg", "lg": "text-xl", "xl": "text-2xl", "2xl": "text-3xl",
        }
        c = color_map.get(color, "text-white")
        s = size_map.get(size, "text-xl")
        return f'<span class="{c} {s} font-black tracking-tight">{value}</span>'
    
    @staticmethod
    def details(summary: str, content: str, open: bool = False) -> str:
        """次要信息折叠组件（HTML5 details标签）
        
        Args:
            summary: 折叠标题
            content: 折叠内容HTML
            open: 是否默认展开
        """
        open_attr = " open" if open else ""
        return (
            f'<details class="pro-details"{open_attr}>'
            f'<summary class="pro-details-summary">{summary}</summary>'
            f'<div class="pro-details-body">{content}</div>'
            f'</details>'
        )


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

