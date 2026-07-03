"""
lessons_learner.py - 错误教训库匹配模块 (V5.0 L1-5)

功能：
1. 启动时读取 基础设定/错误教训库.md
2. 解析为结构化教训条目
3. 根据当日关键词/板块/事件匹配相关历史教训（关键词命中 + 简单TF-IDF打分）
4. 提供 build_section() 供报告末尾输出"📚 历史教训回顾"模块

使用方式：
    from lessons_learner import LessonsLearner
    learner = LessonsLearner()
    lessons = learner.match(["费半暴跌", "半导体", "跌停"], top_k=3)
"""
import os
import re
from typing import List, Dict, Any, Optional


# 候选路径（兼容多种工作目录）
_HERE = os.path.dirname(os.path.abspath(__file__))
_CANDIDATE_PATHS = [
    os.path.abspath(os.path.join(_HERE, "..", "基础设定", "错误教训库.md")),
    "/app/data/所有对话/主对话/基础设定/错误教训库.md",
    "/root/daily-news-insight/基础设定/错误教训库.md",
    "/app/data/基础设定/错误教训库.md",
]

# 板块/事件扩展关键词词典：一个触发词可以扩展成多个同义词
# 用于提高召回率（比如"费半"暴跌应匹配"费城半导体"相关历史教训）
_SYNONYM_MAP = {
    "费半": ["费城半导体", "费半", "SOX"],
    "费城半导体": ["费半", "SOX", "半导体指数"],
    "半导体": ["芯片", "IC", "集成电路", "费半"],
    "跌停": ["暴跌", "崩盘", "重挫", "大跌", "一字跌停", "天量"],
    "暴跌": ["跌停", "崩盘", "重挫", "大跌", "费半"],
    "重挫": ["暴跌", "跌停", "大跌"],
    "天量": ["放量", "成交", "天量成交", "机构兑现"],
    "暴涨": ["涨停", "连板", "拉升", "大涨"],
    "连板": ["龙头", "连板", "高标", "情绪"],
    "机器人": ["人形机器人", "Optimus", "减速器", "丝杠"],
    "算力": ["AI算力", "液冷", "IDC", "GPU", "光模块"],
    "液冷": ["英维克", "液冷服务器", "算力"],
    "存储": ["HBM", "DRAM", "NAND", "兆易", "铜冠铜箔", "雅克"],
    "HBM": ["存储", "前驱体", "雅克科技", "铜箔"],
    "持仓": ["止损", "破位", "减仓", "套牢", "浮亏"],
    "止损": ["破位", "减仓", "止损位", "无条件离场"],
    "ST": ["退市", "ST股", "*ST"],
    "非交易日": ["周末", "节假日", "周六", "周日"],
    "404": ["链接失效", "推送失败"],
    "虚构数据": ["假数据", "模板数据", "编造", "硬编码"],
    "白卡": ["白色背景", "白字", "样式错乱"],
    "推送": ["企业微信", "推送失败", "空消息"],
    "中报": ["业绩", "财报", "业绩预告"],
}


def _expand_keywords(keywords: List[str]) -> List[str]:
    """关键词扩展（同义词）"""
    expanded = []
    for kw in keywords:
        kw = (kw or "").strip()
        if not kw:
            continue
        expanded.append(kw)
        for trigger, syns in _SYNONYM_MAP.items():
            if trigger in kw or kw in trigger:
                expanded.extend(syns)
    # 去重保序
    seen = set()
    out = []
    for w in expanded:
        if w and w not in seen:
            seen.add(w)
            out.append(w)
    return out


def _tokenize(text: str) -> List[str]:
    """简易中文分词：按非中文字符切分 + 2-4字滑窗"""
    text = re.sub(r"[#*`>\-\|]+", " ", text)
    # 英文/数字
    en_tokens = re.findall(r"[A-Za-z0-9\+\-/]+", text)
    # 中文连续段做2-gram/3-gram
    cn_segs = re.findall(r"[\u4e00-\u9fa5]+", text)
    tokens = [t.lower() for t in en_tokens if len(t) >= 2]
    for seg in cn_segs:
        # 标题类长句也保留整段作为一个token
        if len(seg) <= 8:
            tokens.append(seg)
        for n in (2, 3, 4):
            for i in range(len(seg) - n + 1):
                tokens.append(seg[i:i+n])
    return tokens


class LessonsLearner:
    """错误教训库加载与匹配"""
    
    def __init__(self, lessons_path: Optional[str] = None):
        self.lessons_path = lessons_path or self._find_lessons_file()
        self.lessons: List[Dict[str, Any]] = []
        self._load()
    
    def _find_lessons_file(self) -> str:
        for p in _CANDIDATE_PATHS:
            if os.path.exists(p):
                return p
        return _CANDIDATE_PATHS[-1]  # 最后一个兜底
    
    def _load(self):
        """解析错误教训库.md为结构化条目"""
        if not os.path.exists(self.lessons_path):
            print(f"[LessonsLearner] 教训库文件不存在: {self.lessons_path}")
            return
        with open(self.lessons_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        # 按二级/三级/四级标题切分（## / ### / #### 开头）
        # 错误条目通常以 "### ❌ 错误XXX"、"## 错误记录 #XXX"、"## 2026-XX-XXX" 开头
        pattern = re.compile(r"^(#{2,4})\s+(.+?)$", re.MULTILINE)
        matches = list(pattern.finditer(content))
        self.lessons = []
        for i, m in enumerate(matches):
            start = m.end()
            end = matches[i+1].start() if i + 1 < len(matches) else len(content)
            title = m.group(2).strip()
            body = content[start:end].strip()
            # 过滤：标题必须含"错误"/"事故"/"问题"/"教训"，或正文含"问题描述"/"根本原因"/"修复"
            title_kw = any(k in title for k in ["错误", "事故", "问题", "教训", "质量事故"])
            body_kw = any(k in body for k in ["问题描述", "根本原因", "修复", "根因", "教训"])
            # 过滤统计/说明类条目（正文为表格且长度过短）
            is_table = body.lstrip().startswith("|") and body.count("|") > 6
            is_meta = any(k in title for k in ["统计", "使用说明", "适用范围", "检查机制", "规范", "标准", "状态", "最后更新"])
            if is_meta or is_table:
                continue
            if not (title_kw or body_kw):
                continue
            # 提取摘要：取"问题描述"/"根本原因"段，或正文前150字
            summary = self._extract_summary(title, body)
            tags = self._extract_tags(title, body)
            tokens = set(_tokenize(title + "\n" + body))
            self.lessons.append({
                "title": self._clean_title(title),
                "summary": summary,
                "tags": tags,
                "tokens": tokens,
                "raw": body[:2000],
            })
        print(f"[LessonsLearner] 已加载 {len(self.lessons)} 条历史教训 from {self.lessons_path}")
    
    def _clean_title(self, title: str) -> str:
        # 去掉emoji和编号
        t = re.sub(r"^[❌⚠️📊✅📌\s]+", "", title)
        t = re.sub(r"^错误\s*#?\d*[:：]?\s*", "", t)
        t = re.sub(r"^\d{4}-\d{2}-\d{2}\s+", "", t)
        return t.strip()[:40] or "历史教训"
    
    def _extract_summary(self, title: str, body: str) -> str:
        """提取教训条目的一句话摘要"""
        # 优先取"问题描述"段第一句
        m = re.search(r"\*\*问题描述\*\*[:：]?\s*(.+?)(?:\n\n|\n\*\*|$)", body, re.DOTALL)
        if m:
            text = m.group(1).strip()
        else:
            m = re.search(r"### 问题描述\s*(.+?)(?:\n###|\n##|$)", body, re.DOTALL)
            if m:
                text = m.group(1).strip()
            else:
                text = body.strip()
        # 取前1-2句，不超过120字
        text = re.sub(r"\s+", " ", text)
        text = re.sub(r"[#*`>\-]+", "", text).strip()
        sentences = re.split(r"[。！？；\n]", text)
        summary = "。".join([s for s in sentences if s][:2])
        if len(summary) > 120:
            summary = summary[:117] + "…"
        return summary or "详见错误教训库"
    
    def _extract_tags(self, title: str, body: str) -> List[str]:
        """提取条目标签（板块/错误类型/资产类别）"""
        tags = []
        # 板块/资产
        for kw in ["半导体", "算力", "机器人", "存储", "液冷", "ST", "持仓",
                    "推送", "非交易日", "404", "白卡", "虚构数据", "中报", "龙虎榜",
                    "创业板", "科创板", "费半", "美股", "HBM"]:
            if kw in title or kw in body:
                tags.append(kw)
        # 错误类型
        for kw in ["数据错误", "链接", "格式", "推送问题", "深度缺失", "假数据"]:
            if kw in body:
                tags.append(kw)
        return tags[:6]
    
    def match(self, keywords: List[str], top_k: int = 3) -> List[Dict[str, Any]]:
        """根据关键词匹配Top-K历史教训
        
        Returns:
            list of {title, summary, tags, score, ...}
        """
        if not self.lessons:
            return []
        expanded = _expand_keywords(keywords)
        q_tokens = set()
        for kw in expanded:
            q_tokens.update(_tokenize(kw))
            q_tokens.add(kw.lower())
        if not q_tokens:
            return []
        scored = []
        for lesson in self.lessons:
            # Jaccard相似度 + 命中数加权
            hit = q_tokens & lesson["tokens"]
            if not hit:
                continue
            inter = len(hit)
            union = len(q_tokens | lesson["tokens"])
            jaccard = inter / union if union else 0
            # 标签命中加分
            tag_bonus = 0.2 if any(t in expanded for t in lesson["tags"]) else 0
            # 标题命中加分
            title_hit = sum(1 for q in expanded if q in lesson["title"])
            title_bonus = min(0.3, 0.1 * title_hit)
            score = jaccard + tag_bonus + title_bonus
            scored.append((score, lesson))
        scored.sort(key=lambda x: -x[0])
        result = []
        for score, lesson in scored[:top_k]:
            item = {k: v for k, v in lesson.items() if k != "tokens" and k != "raw"}
            item["score"] = min(score, 0.99)
            item["hit_keywords"] = list(q_tokens & lesson["tokens"])[:5]
            result.append(item)
        return result
    
    def add_lesson(self, title: str, problem: str, root_cause: str, fix: str,
                   prevention: str = "", tags: List[str] = None):
        """追加新的错误教训到文件（V5.0预留）
        
        注意：此方法仅做追加，调用方需保证传入的信息完整。
        """
        from datetime import datetime
        ts = datetime.now().strftime("%Y-%m-%d %H:%M")
        block = f"\n\n---\n\n### ❌ {title}\n\n"
        block += f"**发生时间**：{datetime.now().strftime('%Y-%m-%d')}\n\n"
        block += f"**问题描述**：{problem}\n\n"
        block += f"**根本原因**：{root_cause}\n\n"
        block += f"**修复方案**：{fix}\n\n"
        if prevention:
            block += f"**预防措施**：{prevention}\n\n"
        if tags:
            block += f"**标签**：{' / '.join(tags)}\n\n"
        block += f"**状态**：✅ 已修复\n"
        try:
            with open(self.lessons_path, "a", encoding="utf-8") as f:
                f.write(block)
            self._load()  # 重新加载
            return True
        except Exception as e:
            print(f"[LessonsLearner] 追加教训失败: {e}")
            return False


# 单例缓存
_learner_instance: Optional[LessonsLearner] = None

def get_learner() -> LessonsLearner:
    global _learner_instance
    if _learner_instance is None:
        _learner_instance = LessonsLearner()
    return _learner_instance


if __name__ == "__main__":
    # 自测
    learner = LessonsLearner()
    print(f"Loaded {len(learner.lessons)} lessons")
    test_cases = [
        ["费半暴跌", "半导体", "跌停"],
        ["非交易日", "虚构数据"],
        ["推送链接", "404"],
        ["ST股", "止损"],
        ["机器人", "连板"],
    ]
    for case in test_cases:
        print(f"\n=== 关键词: {case} ===")
        for l in learner.match(case, top_k=2):
            print(f"  [{l['score']:.2f}] {l['title']}")
            print(f"      {l['summary']}")
