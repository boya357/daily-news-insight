#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
个股消息面+基本面分析模块
- 消息面：新闻情绪分析、重要性评级
- 基本面：估值、盈利能力、成长性
- 综合评分：技术面+消息面+基本面加权
"""

import json
import re
from datetime import datetime, timedelta
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass, field, asdict


@dataclass
class NewsItem:
    """单条新闻"""
    title: str
    source: str = ""
    publish_time: str = ""
    sentiment: str = "neutral"  # positive/negative/neutral
    sentiment_score: float = 50.0  # 0-100
    importance: str = "normal"  # critical/important/normal
    impact: str = ""  # 影响描述
    url: str = ""


@dataclass
class NewsAnalysisResult:
    """消息面分析结果"""
    total_count: int = 0
    positive_count: int = 0
    negative_count: int = 0
    neutral_count: int = 0
    sentiment_score: float = 50.0  # 整体情绪评分 0-100
    sentiment_label: str = "中性"
    key_news: List[NewsItem] = field(default_factory=list)
    latest_news: List[NewsItem] = field(default_factory=list)
    impact_assessment: str = ""  # 整体影响评估
    risk_hints: List[str] = field(default_factory=list)
    catalyst_hints: List[str] = field(default_factory=list)


@dataclass
class FundamentalData:
    """基本面数据"""
    # 估值
    pe_ttm: Optional[float] = None
    pe_static: Optional[float] = None
    pb: Optional[float] = None
    market_cap: Optional[float] = None  # 亿元
    
    # 盈利能力
    gross_margin: Optional[float] = None  # 毛利率%
    net_margin: Optional[float] = None  # 净利率%
    roe: Optional[float] = None  # ROE%
    
    # 成长性
    revenue_growth: Optional[float] = None  # 营收同比%
    profit_growth: Optional[float] = None  # 净利润同比%
    
    # 最新财报
    latest_revenue: Optional[float] = None  # 最新季度营收（亿元）
    latest_profit: Optional[float] = None  # 最新季度净利润（亿元）
    
    # 评级
    analyst_rating: str = ""  # 分析师评级
    target_price: Optional[float] = None  # 目标价（元）
    analyst_count: int = 0  # 分析师数量
    
    # 基本面评分
    score: float = 50.0
    rating: str = "中性"


class StockNewsAnalyzer:
    """新闻情绪分析器"""
    
    # 正面关键词
    POSITIVE_KEYWORDS = [
        '增长', '上涨', '利好', '突破', '新高', '盈利', '订单',
        '合作', '获批', '通过', '认证', '投产', '上线', '增持',
        '回购', '超预期', '涨价', '供不应求', '满产', '扩产',
        '强劲', '亮眼', '超预期', '大增', '暴涨', '飙升',
        '买入', '推荐', '看好', '利好', '催化剂', '受益',
        '高速增长', '快速增长', '大幅增长', '持续增长',
    ]
    
    # 负面关键词
    NEGATIVE_KEYWORDS = [
        '下跌', '亏损', '利空', '风险', '警示', '处罚', '违规',
        '减持', '解禁', '爆雷', '不及预期', '下滑', '下降',
        '诉讼', '调查', '召回', '停产', '事故', '净流出',
        '卖出', '减持', '抛售', '暴跌', '跳水', '泡沫',
        '高估', '估值过高', '风险提示', '警惕', '谨防',
        '压力', '挑战', '困难', '问题', '隐患', '争议',
        '下调', '降低', '缩减', '收紧', '放缓',
    ]
    
    # 重要性关键词
    CRITICAL_KEYWORDS = [
        '业绩预告', '年报', '半年报', '季报', '重大合同',
        '并购', '重组', 'IPO', '退市', '监管', '处罚',
        '重大事项', '停牌', '复牌', '增持', '减持',
        '股票交易异常波动', '严重异常波动',
    ]
    
    def analyze(self, news_list: List[Dict], stock_name: str = "") -> NewsAnalysisResult:
        """分析新闻列表"""
        result = NewsAnalysisResult()
        result.total_count = len(news_list)
        
        analyzed_news = []
        for news in news_list:
            item = self._analyze_single(news)
            analyzed_news.append(item)
            
            if item.sentiment == 'positive':
                result.positive_count += 1
            elif item.sentiment == 'negative':
                result.negative_count += 1
            else:
                result.neutral_count += 1
        
        # 计算整体情绪评分
        if result.total_count > 0:
            pos_ratio = result.positive_count / result.total_count
            neg_ratio = result.negative_count / result.total_count
            result.sentiment_score = round(50 + (pos_ratio - neg_ratio) * 40, 1)
        else:
            result.sentiment_score = 50
        
        # 情绪标签
        if result.sentiment_score >= 75:
            result.sentiment_label = "正面偏强"
        elif result.sentiment_score >= 62:
            result.sentiment_label = "偏正面"
        elif result.sentiment_score >= 38:
            result.sentiment_label = "中性"
        elif result.sentiment_score >= 25:
            result.sentiment_label = "偏负面"
        else:
            result.sentiment_label = "负面偏强"
        
        # 关键新闻（按重要性+情绪强度排序，取前5条）
        sorted_news = sorted(analyzed_news, key=lambda x: self._importance_weight(x) + abs(x.sentiment_score - 50), reverse=True)
        result.key_news = sorted_news[:5]
        
        # 最新新闻（按时间排序，取前3条）
        sorted_by_time = sorted(analyzed_news, key=lambda x: x.publish_time, reverse=True)
        result.latest_news = sorted_by_time[:3]
        
        # 风险提示
        result.risk_hints = list(set([
            n.title for n in sorted_news 
            if n.sentiment == 'negative' and n.importance in ['critical', 'important']
        ][:3]))
        
        # 催化剂提示
        result.catalyst_hints = list(set([
            n.title for n in sorted_news 
            if n.sentiment == 'positive' and n.importance in ['critical', 'important']
        ][:3]))
        
        # 整体影响评估
        result.impact_assessment = self._generate_impact_assessment(result, stock_name)
        
        return result
    
    def _analyze_single(self, news: Dict) -> NewsItem:
        """分析单条新闻"""
        title = news.get('title', '')
        content = news.get('content', '')
        source = news.get('source', '')
        publish_time = news.get('publish_time', '')
        url = news.get('url', '')
        
        text = title + ' ' + content
        
        # 计算情绪分数
        pos_count = sum(1 for kw in self.POSITIVE_KEYWORDS if kw in text)
        neg_count = sum(1 for kw in self.NEGATIVE_KEYWORDS if kw in text)
        
        # 基础分50，正负关键词调整
        score = 50 + (pos_count - neg_count) * 8
        score = max(0, min(100, score))  # 限制在0-100
        
        # 情绪判断
        if score >= 60:
            sentiment = 'positive'
        elif score <= 40:
            sentiment = 'negative'
        else:
            sentiment = 'neutral'
        
        # 重要性判断
        importance = 'normal'
        for kw in self.CRITICAL_KEYWORDS:
            if kw in title:
                importance = 'critical'
                break
        
        # 重要新闻（但不是critical的）
        if importance == 'normal':
            important_indicators = ['主力资金', '机构', '研报', '评级', '目标价', '业绩']
            for ind in important_indicators:
                if ind in title:
                    importance = 'important'
                    break
        
        return NewsItem(
            title=title,
            source=source,
            publish_time=publish_time,
            sentiment=sentiment,
            sentiment_score=round(score, 1),
            importance=importance,
            url=url
        )
    
    def _importance_weight(self, news: NewsItem) -> int:
        """重要性权重"""
        weights = {'critical': 30, 'important': 15, 'normal': 5}
        return weights.get(news.importance, 5)
    
    def _generate_impact_assessment(self, result: NewsAnalysisResult, stock_name: str) -> str:
        """生成影响评估文本"""
        if result.total_count == 0:
            return "近期无重大消息面影响"
        
        if result.sentiment_score >= 70:
            return f"近期消息面整体偏多，正面信息占主导，对股价形成支撑"
        elif result.sentiment_score >= 55:
            return f"消息面整体中性偏多，利好利空交织但正面因素略占优"
        elif result.sentiment_score >= 45:
            return f"消息面整体中性，多空因素相对平衡"
        elif result.sentiment_score >= 30:
            return f"消息面整体偏空，负面信息较多，需警惕回调风险"
        else:
            return f"消息面整体偏空，负面信息集中，短期承压明显"


class FundamentalAnalyzer:
    """基本面分析器"""
    
    def analyze_from_text(self, text: str, current_price: float = 0) -> FundamentalData:
        """从文本中提取基本面数据并评分"""
        data = FundamentalData()
        
        # 提取PE（优先找带"倍"字的，排除年份和行业平均干扰）
        # 先找出所有PE相关的表述，然后过滤掉"平均""行业"的
        pe_all_pattern = r'((?:平均|行业)?(?:动态|滚动|静态)?(?:市盈率|PE)).{0,40}?(\d+(?:\.\d+)?)\s*倍'
        pe_all_matches = re.findall(pe_all_pattern, text)
        
        # 过滤掉行业平均、平均PE的，只保留公司自身的
        pe_values = []
        for prefix, val in pe_all_matches:
            if '平均' not in prefix and '行业' not in prefix:
                pe_val = float(val)
                # 排除年份数字（2020-2030之间的大概率是年份）
                if not (2020 <= pe_val <= 2030):
                    pe_values.append(pe_val)
        
        # 如果带"倍"的没找到，试试不带"倍"的（如"市盈率TTM 196.23"）
        if not pe_values:
            pe_pattern_no_bei = r'(?:动态|滚动|静态)?(?:市盈率|PE)\s*(?:TTM)?[^0-9]{0,15}(\d+(?:\.\d+)?)(?!\d)'
            pe_no_bei = re.findall(pe_pattern_no_bei, text)
            pe_values = [float(p) for p in pe_no_bei if not (2020 <= float(p) <= 2030)]
        
        if pe_values:
            # 取第一个PE值（通常是公司自身的TTM）
            data.pe_ttm = pe_values[0]
            # 如果有多个，第二个可能是静态PE
            if len(pe_values) >= 2:
                data.pe_static = pe_values[1]
        
        # 提取PB
        pb_match = re.search(r'市净率[^0-9]{0,10}([\d.]+)', text)
        if not pb_match:
            pb_match = re.search(r'PB[^0-9]{0,5}([\d.]+)', text)
        if pb_match:
            data.pb = float(pb_match.group(1))
        
        # 提取市值
        mcap_match = re.search(r'总?市值[^0-9]{0,10}([\d.]+)\s*亿', text)
        if mcap_match:
            data.market_cap = float(mcap_match.group(1))
        
        # 提取毛利率
        margin_match = re.search(r'毛利率[^0-9]{0,10}([\d.]+)', text)
        if margin_match:
            data.gross_margin = float(margin_match.group(1))
        
        # 提取营收增长
        rev_patterns = [
            # 优先匹配"营收/营业收入/主营收入"开头的
            (r'(?:营收|营业收入|主营收入).{0,40}?同比(增长|上升|上涨|下降|下滑|下跌)(\d+(?:\.\d+)?)%', 'direction'),
            (r'(?:营收|营业收入|主营收入).{0,40}?同比([+-]\d+(?:\.\d+)?)%', 'signed'),
            (r'营收增长(\d+(?:\.\d+)?)%', 'positive'),
            (r'营收下降(\d+(?:\.\d+)?)%', 'negative'),
        ]
        
        rev_growth = None
        for pattern, mode in rev_patterns:
            match = re.search(pattern, text)
            if match:
                if mode == 'direction':
                    direction, val = match.groups()
                    positive_dirs = ['增长', '上升', '上涨', '增加', '提升']
                    rev_growth = float(val) if direction in positive_dirs else -float(val)
                elif mode == 'signed':
                    rev_growth = float(match.group(1))
                elif mode == 'positive':
                    rev_growth = float(match.group(1))
                elif mode == 'negative':
                    rev_growth = -float(match.group(1))
                break
        
        if rev_growth is not None:
            data.revenue_growth = rev_growth
        
        # 提取净利润增长
        # 先找"同比增长/下降/上升/下滑"的模式，用最近的同比匹配
        profit_patterns = [
            # 模式：净利润...同比(增长|上升|上涨|下降|下滑|下跌)XX%
            (r'(?:归母净利润|净利润).{0,40}?同比(增长|上升|上涨|下降|下滑|下跌)(\d+(?:\.\d+)?)%', 'direction'),
            # 模式：净利润...同比+/-XX%
            (r'(?:归母净利润|净利润).{0,40}?同比([+-]\d+(?:\.\d+)?)%', 'signed'),
            # 简单模式
            (r'净利润增长(\d+(?:\.\d+)?)%', 'positive'),
            (r'净利润下降(\d+(?:\.\d+)?)%', 'negative'),
            (r'净利润同比增(\d+(?:\.\d+)?)%', 'positive'),
        ]
        
        profit_growth = None
        for pattern, mode in profit_patterns:
            match = re.search(pattern, text)
            if match:
                if mode == 'direction':
                    direction, val = match.groups()
                    # 正面方向词：增长、上升、上涨、增加
                    positive_dirs = ['增长', '上升', '上涨', '增加', '提升']
                    profit_growth = float(val) if direction in positive_dirs else -float(val)
                elif mode == 'signed':
                    profit_growth = float(match.group(1))
                elif mode == 'positive':
                    profit_growth = float(match.group(1))
                elif mode == 'negative':
                    profit_growth = -float(match.group(1))
                break
        
        if profit_growth is not None:
            data.profit_growth = profit_growth
        
        # 提取目标价
        target_patterns = [
            r'目标均价[^0-9]{0,10}(\d+(?:\.\d+)?)',
            r'目标价[^0-9]{0,10}(\d+(?:\.\d+)?)元',
            r'目标价中枢[^0-9]{0,10}(\d+(?:\.\d+)?)',
            r'目标价预测平均价为(\d+(?:\.\d+)?)',
        ]
        for pattern in target_patterns:
            match = re.search(pattern, text)
            if match:
                data.target_price = float(match.group(1))
                break
        
        # 提取分析师数量
        analyst_match = re.search(r'(\d+)\s*家机构', text)
        if analyst_match:
            data.analyst_count = int(analyst_match.group(1))
        
        # 计算基本面评分
        data.score, data.rating = self._calc_fundamental_score(data, current_price)
        
        return data
    
    def _calc_fundamental_score(self, data: FundamentalData, current_price: float) -> Tuple[float, str]:
        """计算基本面评分（0-100分）"""
        scores = []  # 存储各项得分
        weights = []  # 存储各项权重
        
        # 1. 盈利能力（权重30%）
        if data.profit_growth is not None:
            if data.profit_growth >= 200:
                profit_score = 95
            elif data.profit_growth >= 100:
                profit_score = 85
            elif data.profit_growth >= 50:
                profit_score = 75
            elif data.profit_growth >= 30:
                profit_score = 68
            elif data.profit_growth >= 10:
                profit_score = 60
            elif data.profit_growth >= 0:
                profit_score = 50
            elif data.profit_growth >= -20:
                profit_score = 35
            elif data.profit_growth >= -50:
                profit_score = 25
            else:
                profit_score = 15
            scores.append(profit_score)
            weights.append(0.30)
        
        # 2. 营收增长（权重20%）
        if data.revenue_growth is not None:
            if data.revenue_growth >= 50:
                rev_score = 85
            elif data.revenue_growth >= 30:
                rev_score = 75
            elif data.revenue_growth >= 15:
                rev_score = 65
            elif data.revenue_growth >= 0:
                rev_score = 55
            elif data.revenue_growth >= -15:
                rev_score = 40
            else:
                rev_score = 30
            scores.append(rev_score)
            weights.append(0.20)
        
        # 3. 估值水平（权重30%）- 结合PEG
        if data.pe_ttm is not None and data.profit_growth is not None and data.profit_growth > 0:
            peg = data.pe_ttm / data.profit_growth
            if peg <= 0.5:
                val_score = 95
            elif peg <= 1.0:
                val_score = 85
            elif peg <= 1.5:
                val_score = 75
            elif peg <= 2.0:
                val_score = 65
            elif peg <= 3.0:
                val_score = 50
            elif peg <= 5.0:
                val_score = 35
            else:
                val_score = 20
            scores.append(val_score)
            weights.append(0.30)
        elif data.pe_ttm is not None:
            # 只看PE绝对值
            if data.pe_ttm <= 15:
                val_score = 90
            elif data.pe_ttm <= 30:
                val_score = 80
            elif data.pe_ttm <= 50:
                val_score = 68
            elif data.pe_ttm <= 80:
                val_score = 55
            elif data.pe_ttm <= 120:
                val_score = 42
            elif data.pe_ttm <= 200:
                val_score = 30
            else:
                val_score = 18
            scores.append(val_score)
            weights.append(0.30)
        
        # 4. 机构预期（权重20%）
        if data.target_price is not None and current_price > 0:
            upside = (data.target_price - current_price) / current_price * 100
            if upside >= 80:
                target_score = 95
            elif upside >= 50:
                target_score = 85
            elif upside >= 30:
                target_score = 75
            elif upside >= 10:
                target_score = 65
            elif upside >= -10:
                target_score = 50
            elif upside >= -30:
                target_score = 35
            else:
                target_score = 20
            scores.append(target_score)
            weights.append(0.20)
        
        # 计算加权平均分
        if scores and weights:
            total_weight = sum(weights)
            score = sum(s * w for s, w in zip(scores, weights)) / total_weight
        else:
            score = 50.0  # 无数据时中性
        
        score = round(score, 1)
        
        # 评级
        if score >= 80:
            rating = "优秀"
        elif score >= 65:
            rating = "良好"
        elif score >= 50:
            rating = "中性"
        elif score >= 35:
            rating = "一般"
        else:
            rating = "较差"
        
        return score, rating


def calc_comprehensive_score(technical_score: float, news_score: float, fundamental_score: float,
                             tech_weight: float = 0.5, news_weight: float = 0.25, 
                             fund_weight: float = 0.25) -> Tuple[float, str]:
    """
    计算综合评分
    默认权重：技术面50%，消息面25%，基本面25%
    """
    score = technical_score * tech_weight + news_score * news_weight + fundamental_score * fund_weight
    score = round(score, 1)
    
    if score >= 80:
        rating = "强烈推荐"
    elif score >= 70:
        rating = "推荐"
    elif score >= 55:
        rating = "中性偏多"
    elif score >= 45:
        rating = "中性"
    elif score >= 30:
        rating = "中性偏空"
    else:
        rating = "回避"
    
    return score, rating


def update_stock_analysis(stock_file: str, news_list: List[Dict], 
                          fundamental_text: str = "") -> Dict:
    """
    更新个股分析数据，补充消息面和基本面
    """
    # 读取现有数据
    with open(stock_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    current_price = data.get('market', {}).get('current_price', 0)
    stock_name = data.get('name', '')
    
    # 1. 消息面分析
    news_analyzer = StockNewsAnalyzer()
    news_result = news_analyzer.analyze(news_list, stock_name)
    
    # 转换为字典
    data['news'] = {
        'sentiment_score': news_result.sentiment_score,
        'sentiment_label': news_result.sentiment_label,
        'total_count': news_result.total_count,
        'positive_count': news_result.positive_count,
        'negative_count': news_result.negative_count,
        'impact_assessment': news_result.impact_assessment,
        'key_news': [asdict(n) for n in news_result.key_news],
        'latest_news': [asdict(n) for n in news_result.latest_news],
        'risk_hints': news_result.risk_hints,
        'catalyst_hints': news_result.catalyst_hints,
    }
    
    # 2. 基本面分析
    if fundamental_text:
        fund_analyzer = FundamentalAnalyzer()
        fund_result = fund_analyzer.analyze_from_text(fundamental_text, current_price)
        data['fundamental'] = asdict(fund_result)
    else:
        # 如果没有基本面文本，用news里的信息尝试提取
        all_text = ' '.join([n.get('title', '') + ' ' + n.get('content', '') for n in news_list])
        if all_text.strip():
            fund_analyzer = FundamentalAnalyzer()
            fund_result = fund_analyzer.analyze_from_text(all_text, current_price)
            data['fundamental'] = asdict(fund_result)
    
    # 3. 综合评分
    tech_score = data.get('technical', {}).get('score', 50)
    news_score = news_result.sentiment_score
    fund_score = data.get('fundamental', {}).get('score', 50)
    
    comp_score, comp_rating = calc_comprehensive_score(tech_score, news_score, fund_score)
    
    data['overall'] = {
        'score': comp_score,
        'rating': comp_rating,
        'price': current_price,
        'change_pct': data.get('market', {}).get('change_pct', 0),
        'technical_score': tech_score,
        'news_score': news_score,
        'fundamental_score': fund_score,
        'update_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    }
    
    # 保存
    with open(stock_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    return data


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        stock_file = sys.argv[1]
        # 测试：用空新闻列表更新
        update_stock_analysis(stock_file, [])
        print(f"已更新: {stock_file}")
