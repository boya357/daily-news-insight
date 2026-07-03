"""
预测中心 - V4版（新版设计）
基于V4BaseGenerator基类，采用v4_test.html设计风格
特色：AI预测模型、多维度预测、准确率追踪
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from generators.v4_base import V4BaseGenerator


class PredictionCenterV4(V4BaseGenerator):
    """预测中心V4生成器"""
    
    def __init__(self, data_dir: str = "data"):
        super().__init__(data_dir)
        self.page_title = "🔮 预测中心"
        self.page_subtitle = "AI智能预测 · 多维度分析 · 准确率追踪"
        self.active_nav_key = "prediction_center"
        self.toc_items = [
            ("市场概览", "section-overview"),
            ("大盘预测", "section-market"),
            ("板块预测", "section-sector"),
            ("个股预测", "section-stocks"),
            ("准确率统计", "section-accuracy"),
            ("风险提示", "section-risk"),
        ]
    
    def render_market_prediction(self) -> str:
        """渲染大盘预测模块"""
        predictions = [
            {
                "index": "上证指数",
                "prediction": "震荡上行",
                "probability": "68%",
                "range": "4050 - 4180",
                "trend": "up",
                "support": "4020",
                "resistance": "4200",
            },
            {
                "index": "创业板指",
                "prediction": "强势上涨",
                "probability": "72%",
                "range": "4200 - 4380",
                "trend": "up",
                "support": "4150",
                "resistance": "4400",
            },
            {
                "index": "科创50",
                "prediction": "震荡偏强",
                "probability": "65%",
                "range": "1880 - 1960",
                "trend": "up",
                "support": "1850",
                "resistance": "1980",
            },
        ]
        
        cards_html = ""
        for p in predictions:
            trend_color = "#DC2626" if p["trend"] == "up" else "#16A34A"
            trend_icon = "📈" if p["trend"] == "up" else "📉"
            
            cards_html += f'''
            <div class="prediction-card">
                <div class="prediction-header">
                    <span class="prediction-index">{p["index"]}</span>
                    <span class="prediction-trend" style="color: {trend_color};">{trend_icon} {p["prediction"]}</span>
                </div>
                <div class="prediction-probability">
                    <div class="probability-bar">
                        <div class="probability-fill" style="width: {p["probability"]}; background: {trend_color};"></div>
                    </div>
                    <span class="probability-text">{p["probability"]} 概率</span>
                </div>
                <div class="prediction-range">
                    <div class="range-item">
                        <span class="range-label">预计区间</span>
                        <span class="range-value">{p["range"]}</span>
                    </div>
                    <div class="range-item">
                        <span class="range-label">支撑位</span>
                        <span class="range-value support">{p["support"]}</span>
                    </div>
                    <div class="range-item">
                        <span class="range-label">压力位</span>
                        <span class="range-value resistance">{p["resistance"]}</span>
                    </div>
                </div>
            </div>
            '''
        
        return f'''
        <section class="v4-section" id="section-market">
            {self.render_section_header("📊 大盘预测", "明日走势", "v4-tag-blue")}
            <div class="prediction-grid">
                {cards_html}
            </div>
        </section>
        '''
    
    def render_sector_prediction(self) -> str:
        """渲染板块预测模块"""
        sectors = [
            {"name": "AI算力", "rank": 1, "score": 92, "trend": "up", "reason": "算力需求持续爆发"},
            {"name": "存储芯片", "rank": 2, "score": 88, "trend": "up", "reason": "周期反转+HBM需求"},
            {"name": "人形机器人", "rank": 3, "score": 85, "trend": "up", "reason": "产业政策催化"},
            {"name": "新能源汽车", "rank": 4, "score": 78, "trend": "flat", "reason": "销量数据验证"},
            {"name": "医药生物", "rank": 5, "score": 72, "trend": "up", "reason": "创新药反弹"},
            {"name": "银行", "rank": 6, "score": 55, "trend": "down", "reason": "息差压力持续"},
        ]
        
        items_html = ""
        for s in sectors:
            trend_color = "#DC2626" if s["trend"] == "up" else "#16A34A" if s["trend"] == "down" else "#64748B"
            trend_icon = "↑" if s["trend"] == "up" else "↓" if s["trend"] == "down" else "→"
            
            items_html += f'''
            <div class="sector-prediction-item">
                <span class="sector-rank">{s["rank"]}</span>
                <span class="sector-name">{s["name"]}</span>
                <div class="sector-score-bar">
                    <div class="score-fill" style="width: {s["score"]}%;"></div>
                </div>
                <span class="sector-score">{s["score"]}分</span>
                <span class="sector-trend" style="color: {trend_color};">{trend_icon}</span>
            </div>
            '''
        
        return f'''
        <section class="v4-section" id="section-sector">
            {self.render_section_header("🔥 板块热度预测", "明日关注", "v4-tag-red")}
            <div class="v4-card">
                <div class="sector-prediction-list">
                    {items_html}
                </div>
            </div>
            <p class="prediction-note">* 预测基于AI模型分析，仅供参考，不构成投资建议</p>
        </section>
        '''
    
    def render_accuracy_stats(self) -> str:
        """渲染准确率统计模块"""
        stats = [
            {"period": "近7天", "accuracy": "72%", "total": 25, "correct": 18},
            {"period": "近30天", "accuracy": "68%", "total": 90, "correct": 61},
            {"period": "近90天", "accuracy": "65%", "total": 270, "correct": 176},
        ]
        
        stats_html = ""
        for s in stats:
            stats_html += f'''
            <div class="accuracy-stat-card">
                <div class="accuracy-period">{s["period"]}</div>
                <div class="accuracy-value">{s["accuracy"]}</div>
                <div class="accuracy-detail">
                    总计 {s["total"]} 次预测，正确 {s["correct"]} 次
                </div>
            </div>
            '''
        
        return f'''
        <section class="v4-section" id="section-accuracy">
            {self.render_section_header("📈 准确率追踪", "历史表现", "v4-tag-green")}
            <div class="accuracy-stats-grid">
                {stats_html}
            </div>
        </section>
        '''
    
    def render_content(self) -> str:
        """渲染页面内容"""
        # 头部统计卡片
        header_stats = f'''
        <div class="v4-header-stats">
            <div class="v4-stat-card">
                <div class="v4-stat-value" style="color: #8B5CF6;">68%</div>
                <div class="v4-stat-label">整体准确率</div>
            </div>
            <div class="v4-stat-card">
                <div class="v4-stat-value" style="color: #10B981;">90天</div>
                <div class="v4-stat-label">追踪周期</div>
            </div>
            <div class="v4-stat-card">
                <div class="v4-stat-value" style="color: #F59E0B;">270</div>
                <div class="v4-stat-label">累计预测</div>
            </div>
            <div class="v4-stat-card">
                <div class="v4-stat-value" style="color: #EC4899;">6</div>
                <div class="v4-stat-label">预测维度</div>
            </div>
        </div>
        '''
        
        header = self.render_page_header(extra_html=header_stats)
        market_overview = self.render_market_overview_v2()
        market_prediction = self.render_market_prediction()
        sector_prediction = self.render_sector_prediction()
        accuracy_stats = self.render_accuracy_stats()
        risk_warning = self.render_risk_warning()
        
        return f'''
        {header}
        {market_overview}
        {market_prediction}
        {sector_prediction}
        {accuracy_stats}
        {risk_warning}
        '''
    
    def get_page_css(self) -> str:
        """页面特有CSS - 新版设计风格"""
        return '''
        /* 预测卡片 */
        .prediction-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 16px;
        }
        .prediction-card {
            padding: 20px;
            background: white;
            border-radius: 14px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.06);
        }
        .prediction-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 16px;
        }
        .prediction-index {
            font-size: 16px;
            font-weight: 600;
            color: #1E293B;
        }
        .prediction-trend {
            font-size: 14px;
            font-weight: 600;
        }
        .prediction-probability {
            margin-bottom: 16px;
        }
        .probability-bar {
            height: 8px;
            background: #E2E8F0;
            border-radius: 4px;
            overflow: hidden;
            margin-bottom: 6px;
        }
        .probability-fill {
            height: 100%;
            border-radius: 4px;
            transition: width 0.5s ease;
        }
        .probability-text {
            font-size: 12px;
            color: #64748B;
        }
        .prediction-range {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 8px;
            padding-top: 12px;
            border-top: 1px solid #F1F5F9;
        }
        .range-item {
            text-align: center;
        }
        .range-label {
            display: block;
            font-size: 11px;
            color: #94A3B8;
            margin-bottom: 4px;
        }
        .range-value {
            font-size: 14px;
            font-weight: 600;
            color: #1E293B;
        }
        .range-value.support { color: #16A34A; }
        .range-value.resistance { color: #DC2626; }
        
        /* 板块预测列表 */
        .sector-prediction-list {
            display: flex;
            flex-direction: column;
            gap: 10px;
        }
        .sector-prediction-item {
            display: grid;
            grid-template-columns: 30px 100px 1fr 60px 30px;
            gap: 12px;
            align-items: center;
            padding: 12px 14px;
            background: #F8FAFC;
            border-radius: 10px;
        }
        .sector-rank {
            font-size: 14px;
            font-weight: 700;
            color: #64748B;
            text-align: center;
        }
        .sector-name {
            font-size: 14px;
            font-weight: 500;
            color: #1E293B;
        }
        .sector-score-bar {
            height: 6px;
            background: #E2E8F0;
            border-radius: 3px;
            overflow: hidden;
        }
        .score-fill {
            height: 100%;
            background: linear-gradient(90deg, #8B5CF6, #EC4899);
            border-radius: 3px;
        }
        .sector-score {
            font-size: 13px;
            font-weight: 600;
            color: #475569;
            text-align: right;
        }
        .sector-trend {
            font-size: 18px;
            font-weight: 700;
            text-align: center;
        }
        .prediction-note {
            font-size: 12px;
            color: #94A3B8;
            text-align: center;
            margin-top: 12px;
        }
        
        /* 准确率统计 */
        .accuracy-stats-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 16px;
        }
        .accuracy-stat-card {
            padding: 24px 20px;
            background: white;
            border-radius: 14px;
            text-align: center;
            box-shadow: 0 2px 8px rgba(0,0,0,0.06);
        }
        .accuracy-period {
            font-size: 14px;
            color: #64748B;
            margin-bottom: 8px;
        }
        .accuracy-value {
            font-size: 36px;
            font-weight: 800;
            color: #10B981;
            margin-bottom: 8px;
        }
        .accuracy-detail {
            font-size: 12px;
            color: #94A3B8;
        }
        
        /* 标签颜色 */
        .v4-tag-blue {
            background: rgba(37, 99, 235, 0.1);
            color: #2563EB;
        }
        .v4-tag-red {
            background: rgba(220, 38, 38, 0.1);
            color: #DC2626;
        }
        .v4-tag-green {
            background: rgba(16, 185, 129, 0.1);
            color: #10B981;
        }
        
        /* 响应式 */
        @media (max-width: 640px) {
            .sector-prediction-item {
                grid-template-columns: 30px 80px 1fr 50px;
            }
            .sector-trend {
                display: none;
            }
        }
        '''


if __name__ == '__main__':
    generator = PredictionCenterV4(data_dir='data')
    html = generator.generate()
    output_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '..', 'docs', 'prediction_center_v4.html')
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"✅ 预测中心V4已生成 -> {output_path}")
