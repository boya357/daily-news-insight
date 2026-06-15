"""
明日催化剂生成器 - Pro版
基于ReportProGenerator基类重构，深色玻璃态风格
明日重要事件 + 题材催化 + 交易提示
"""
import sys
import os
from datetime import datetime, timedelta

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from generators.report_pro_base import ReportProGenerator


class TomorrowCatalystProGenerator(ReportProGenerator):
    """明日催化剂生成器 - Pro版"""
    
    def __init__(self, date_str: str = None, subtitle: str = None, data_dir: str = "data"):
        if date_str:
            date = date_str
        else:
            tomorrow = datetime.now() + timedelta(days=1)
            date = tomorrow.strftime('%Y-%m-%d')
        
        sub = subtitle or f"{date} · 明日投资机会早知道"
        
        super().__init__(
            title="明日催化剂",
            report_type="tomorrow_catalyst",
            subtitle=sub,
            date_str=date,
            data_dir=data_dir,
        )
        
        self.active_page = "明日催化"
    
    def add_catalyst_overview(self, catalysts_count: int = 5, key_topics: list = None):
        """添加催化剂总览"""
        if key_topics is None:
            key_topics = ["AI算力", "人形机器人", "存储芯片"]
        
        topics_str = "、".join(key_topics)
        
        content = f'''
        <div class="bg-gradient-to-r from-yellow-500/20 to-orange-500/15 border border-yellow-500/30 rounded-xl p-5">
            <div class="flex items-center gap-2 mb-3">
                <span class="text-2xl">⚡</span>
                <span class="text-white font-bold">明日催化总览</span>
            </div>
            <p class="text-white/80 leading-relaxed text-sm">
                明日共有 <span class="text-yellow-400 font-bold">{catalysts_count}</span> 个重要催化事件，
                重点关注 <span class="text-yellow-400 font-semibold">{topics_str}</span> 等方向。
            </p>
        </div>
        '''
        self.add_section("催化总览", content, "⚡")
    
    def add_key_catalysts(self, catalysts: list = None):
        """添加重点催化事件"""
        if catalysts is None:
            catalysts = [
                {
                    "time": "09:30",
                    "title": "重要经济数据公布",
                    "topic": "宏观经济",
                    "impact": "高",
                    "desc": "国家统计局公布最新经济数据，可能对市场整体走势产生影响。"
                },
                {
                    "time": "10:00",
                    "title": "AI行业大会召开",
                    "topic": "AI算力",
                    "impact": "高",
                    "desc": "人工智能行业大会召开，多家巨头将发布最新技术和产品。"
                },
                {
                    "time": "全天",
                    "title": "新股申购",
                    "topic": "新股",
                    "impact": "中",
                    "desc": "两只新股开启申购，分别属于半导体和生物医药行业。"
                },
                {
                    "time": "全天",
                    "title": "限售股解禁",
                    "topic": "市场",
                    "impact": "中",
                    "desc": "多家公司限售股解禁，注意相关个股的流动性影响。"
                },
                {
                    "time": "盘后",
                    "title": "业绩公告",
                    "topic": "业绩",
                    "impact": "低",
                    "desc": "多家公司发布业绩报告，关注业绩超预期的标的。"
                },
            ]
        
        impact_colors = {
            "高": ("bg-red-500", "border-red-500/30", "text-red-400", "bg-red-500/20"),
            "中": ("bg-yellow-500", "border-yellow-500/30", "text-yellow-400", "bg-yellow-500/20"),
            "低": ("bg-green-500", "border-green-500/30", "text-green-400", "bg-green-500/20"),
        }
        
        catalysts_html = '<div class="space-y-3">'
        
        for cat in catalysts:
            time = cat.get("time", "")
            title = cat.get("title", "")
            topic = cat.get("topic", "")
            impact = cat.get("impact", "中")
            desc = cat.get("desc", "")
            
            dot_color, border_color, text_color, bg_color = impact_colors.get(impact, impact_colors["中"])
            
            catalysts_html += f'''
            <div class="bg-white/5 rounded-xl p-4 border {border_color}/20">
                <div class="flex items-start gap-4">
                    <!-- 时间 -->
                    <div class="text-center flex-shrink-0 w-16">
                        <div class="text-lg font-bold text-white">{time}</div>
                        <div class="text-xs text-white/40">时间</div>
                    </div>
                    
                    <!-- 分割线 -->
                    <div class="w-px bg-white/10 h-auto self-stretch"></div>
                    
                    <!-- 内容 -->
                    <div class="flex-1">
                        <div class="flex items-center gap-2 mb-2">
                            <span class="text-white font-semibold text-sm">{title}</span>
                            <span class="{bg_color} {text_color} text-xs px-2 py-0.5 rounded-full">
                                {topic}
                            </span>
                            <span class="ml-auto text-xs font-medium {text_color}">
                                {impact}影响
                            </span>
                        </div>
                        <p class="text-white/60 text-xs m-0 leading-relaxed">{desc}</p>
                    </div>
                </div>
            </div>
            '''
        
        catalysts_html += '</div>'
        
        self.add_section("重点催化事件", catalysts_html, "📅")
    
    def add_topic_opportunities(self, topics: list = None):
        """添加题材机会提示"""
        if topics is None:
            topics = [
                {"name": "AI算力", "catalyst": "行业大会", "confidence": "高", "targets": ["英伟达", "寒武纪"]},
                {"name": "人形机器人", "catalyst": "产业催化", "confidence": "中", "targets": ["拓普集团", "三花智控"]},
                {"name": "存储芯片", "catalyst": "价格上涨", "confidence": "高", "targets": ["兆易创新", "北京君正"]},
            ]
        
        topics_html = '<div class="grid md:grid-cols-3 gap-3">'
        
        for topic in topics:
            name = topic.get("name", "")
            catalyst = topic.get("catalyst", "")
            confidence = topic.get("confidence", "中")
            targets = topic.get("targets", [])
            
            conf_colors = {
                "高": "text-green-400",
                "中": "text-yellow-400",
                "低": "text-red-400",
            }
            conf_color = conf_colors.get(confidence, "text-white/60")
            
            targets_html = ''
            if targets:
                target_tags = ' '.join([
                    f'<span class="bg-blue-500/20 text-blue-400 text-xs px-2 py-0.5 rounded">{t}</span>'
                    for t in targets
                ])
                targets_html = f'''
                <div class="mt-3 pt-3 border-t border-white/10">
                    <div class="text-xs text-white/40 mb-2">关注标的</div>
                    <div class="flex flex-wrap gap-1.5">{target_tags}</div>
                </div>
                '''
            
            topics_html += f'''
            <div class="bg-gradient-to-br from-blue-500/15 to-purple-500/10 border border-blue-500/20 rounded-xl p-4">
                <div class="flex items-center justify-between mb-2">
                    <span class="text-white font-semibold text-sm">{name}</span>
                    <span class="text-xs {conf_color} font-medium">{confidence}确定性</span>
                </div>
                <div class="text-xs text-white/60">
                    催化：{catalyst}
                </div>
                {targets_html}
            </div>
            '''
        
        topics_html += '</div>'
        
        self.add_section("题材机会提示", topics_html, "🎯")
    
    def add_trading_tips(self, tips: list = None):
        """添加交易提示"""
        if tips is None:
            tips = [
                "关注开盘量能变化，若放量可积极参与",
                "高位股注意风险，避免追高",
                "重点关注催化事件落地后的市场反应",
                "控制仓位，保持合理的风险敞口",
            ]
        
        tips_html = '<div class="space-y-2">'
        
        for i, tip in enumerate(tips):
            tips_html += f'''
            <div class="flex items-start gap-3 bg-white/5 rounded-lg p-3">
                <div class="w-5 h-5 rounded-full bg-blue-500/20 flex items-center justify-center flex-shrink-0 mt-0.5">
                    <span class="text-blue-400 text-xs font-bold">{i+1}</span>
                </div>
                <p class="text-white/70 text-sm m-0 leading-relaxed">{tip}</p>
            </div>
            '''
        
        tips_html += '</div>'
        
        content = f'''
        <div class="bg-gradient-to-r from-purple-500/10 to-pink-500/10 border border-purple-500/20 rounded-xl p-4">
            <div class="flex items-center gap-2 mb-3">
                <span class="text-lg">💡</span>
                <span class="text-white font-semibold">交易提示</span>
            </div>
            {tips_html}
        </div>
        '''
        
        self.add_section("交易提示", content, "💡")
    
    def add_risk_warning(self):
        """添加风险提示"""
        content = '''
        <div class="bg-gradient-to-r from-red-500/15 to-orange-500/10 border border-red-500/20 rounded-xl p-4">
            <div class="flex items-center gap-2 mb-3">
                <span class="text-lg">⚠️</span>
                <span class="text-white font-semibold">风险提示</span>
            </div>
            <ul class="text-sm text-white/60 leading-relaxed space-y-1 m-0 pl-4">
                <li>催化事件可能不及预期，注意利好落地风险</li>
                <li>市场情绪变化可能影响题材持续性</li>
                <li>个股受多因素影响，单一催化不构成投资建议</li>
                <li>本内容仅供参考，不构成任何投资建议</li>
            </ul>
        </div>
        '''
        
        self.add_section("风险提示", content, "⚠️")
    
    def build_standard_report(self):
        """构建标准版本的明日催化剂"""
        self.add_catalyst_overview()
        self.add_key_catalysts()
        self.add_topic_opportunities()
        self.add_trading_tips()
        self.add_risk_warning()
        
        return self


if __name__ == '__main__':
    # 测试生成
    gen = TomorrowCatalystProGenerator('2026-06-16')
    gen.build_standard_report()
    html = gen.render()
    print(f'Pro版明日催化剂生成成功，长度: {len(html)} 字符')
    
    # 保存测试
    os.makedirs('../docs/明日催化剂', exist_ok=True)
    with open('../docs/明日催化剂/20260616_明日催化剂.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print('已保存到 docs/明日催化剂/20260616_明日催化剂.html')
